# -*- coding: utf-8 -*-
"""Paper metadata through fetch.py (robots, 1 req/host, >=3 s): Crossref title search -> DOI record; Semantic Scholar by DOI for abstract/tldr.
Usage: python3 meta.py OUT.json "title 1" "title 2" ...   (or DOI:10.xxx/yyy to skip the title search)
Raw responses stay in RAW via fetch.py; OUT keeps the parsed fields plus raw_key for traceability."""
import json, re, sys, urllib.parse, difflib
from pathlib import Path
import fetch

def last_log():
    return json.loads(fetch.LOG.read_text().splitlines()[-1])

def get_json(url):
    fetch.fetch_one(url)
    rec = last_log()
    if rec.get('result') != 'read':
        return None, rec
    return json.loads((fetch.RAW / f"{rec['raw_key']}.raw").read_bytes()), rec

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', re.sub(r'<[^>]+>', '', s or '').lower()).strip()

def strip_jats(s):
    return ' '.join(re.sub(r'<[^>]+>', ' ', s or '').split()) or None

def one(q):
    row = dict(query=q)
    if q.startswith('DOI:'):
        doi = q[4:]
        d, rec = get_json('https://api.crossref.org/works/' + urllib.parse.quote(doi))
        item = d['message'] if d else None
    else:
        d, rec = get_json('https://api.crossref.org/works?rows=3&query.bibliographic=' + urllib.parse.quote(q))
        items = [it for it in (d['message']['items'] if d else []) if it.get('type') not in ('component', 'peer-review', 'grant') and not str(it.get('DOI', '')).endswith(('.s001', '.s002'))]
        best = max(items, key=lambda it: difflib.SequenceMatcher(None, norm(q), norm((it.get('title') or [''])[0])).ratio(), default=None)
        item = best
    row['crossref_raw_key'] = rec.get('raw_key')
    if item:
        t = (item.get('title') or [''])[0]
        row.update(doi=item.get('DOI'), cr_title=t, title_ratio=round(difflib.SequenceMatcher(None, norm(q[4:] if q.startswith('DOI:') else q), norm(t)).ratio(), 3),
                   container=(item.get('container-title') or [None])[0], volume=item.get('volume'), issue=item.get('issue'), page=item.get('page') or item.get('article-number'),
                   published_online=item.get('published-online', {}).get('date-parts', [[None]])[0], published_print=item.get('published-print', {}).get('date-parts', [[None]])[0],
                   type=item.get('type'), authors=[' '.join(x for x in [a.get('given'), a.get('family')] if x) for a in item.get('author', [])],
                   cr_abstract=strip_jats(item.get('abstract')), is_referenced_by=item.get('is-referenced-by-count'))
    if row.get('doi') and not row.get('cr_abstract'):  # Semantic Scholar only when Crossref has no abstract (rate limit)
        s, srec = get_json('https://api.semanticscholar.org/graph/v1/paper/DOI:' + urllib.parse.quote(row['doi']) + '?fields=title,abstract,tldr,year,venue,citationCount,authors')
        row['s2_raw_key'] = srec.get('raw_key'); row['s2_result'] = srec.get('result'); row['s2_status'] = srec.get('http_status')
        if s:
            row.update(s2_title=s.get('title'), s2_abstract=s.get('abstract'), s2_tldr=(s.get('tldr') or {}).get('text'), s2_citations=s.get('citationCount'))
    row['abstract_source'] = 'crossref' if row.get('cr_abstract') else ('semanticscholar' if row.get('s2_abstract') else None)
    return row

if __name__ == '__main__':
    out = Path(sys.argv[1])
    rows = json.loads(out.read_text()) if out.exists() else []
    for q in sys.argv[2:]:
        rows.append(one(q))
        out.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    for r in rows:
        print(r.get('title_ratio'), r.get('doi'), r.get('abstract_source'), r.get('s2_status'), (r.get('cr_title') or '')[:70])

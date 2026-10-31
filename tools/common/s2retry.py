# Retry Semantic Scholar for rows still without an abstract: by DOI if present, else title search.
# S2-only policy (data-contract v0.3 addendum): on HTTP 429 wait 60 s then 180 s, at most 2 retries per paper; never for other hosts.
# Count sent requests for this URL in local fetch-log*.jsonl, excluding robots skips.
# A prior fetch_meta DOI HTTP 429 uses a different fields URL and adds one attempt; total requests stay <= 3.
import json, sys, time, urllib.parse, difflib
from pathlib import Path
import meta
WAITS = [60, 180]
def was_requested(rec):
    return (rec.get('result') != 'not-fetched-robots' and rec.get('kind') != 'note'
            and (rec.get('http_status') is not None or bool(rec.get('request_started_at'))))
def logged_requests(url):
    records = []
    for p in sorted(Path('.').glob('fetch-log*.jsonl')):
        for line in p.read_text().splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get('url') == url and was_requested(rec):
                records.append(rec)
    return records
def s2(url, prior_requests=0):
    sent = 0
    for i in range(prior_requests, len(WAITS) + 1):
        if i:
            time.sleep(WAITS[i - 1])
        d, rec = meta.get_json(url)
        sent += int(was_requested(rec))
        if rec.get('http_status') != 429 or i == len(WAITS):
            return d, rec, i, sent
for slug in sys.argv[1:]:
    p = Path(f'{slug}-meta.json'); rows = json.loads(p.read_text())
    for r in rows:
        if r.get('abstract_source'):
            continue
        if r.get('doi'):
            url = 'https://api.semanticscholar.org/graph/v1/paper/DOI:' + urllib.parse.quote(r['doi']) + '?fields=title,abstract,year,venue,citationCount,authors,externalIds'
        else:
            url = 'https://api.semanticscholar.org/graph/v1/paper/search?limit=3&fields=title,abstract,year,venue,externalIds,authors&query=' + urllib.parse.quote(r.get('title') or '')
        prior_429 = bool(r.get('doi')) and r.get('s2_status') == 429
        logged = logged_requests(url)
        prior_requests = len(logged) + int(prior_429)
        terminal = next((rec for rec in logged if rec.get('http_status') != 429), None)
        sent, skipped = 0, None
        if terminal is not None:
            d, rec = None, terminal
            tries = min(max(prior_requests - 1, 0), len(WAITS))
            skipped = 'non-429-response'
        elif prior_requests >= len(WAITS) + 1:
            d, rec = None, logged[-1]
            tries = len(WAITS)
            skipped = 'request-limit'
        else:
            d, rec, tries, sent = s2(url, prior_requests=prior_requests)
        r['s2_retry'] = dict(url=url, status=rec.get('http_status'), raw_key=rec.get('raw_key'), retries=tries,
                             prior_requests=prior_requests, requests_sent=sent)
        if skipped:
            r['s2_retry']['skipped'] = skipped
        if prior_429:
            r['s2_retry']['prior_429'] = True
        if d:
            if 'data' in d:
                cand = max(d.get('data') or [], key=lambda it: difflib.SequenceMatcher(None, meta.norm(r.get('title')), meta.norm(it.get('title'))).ratio(), default=None)
                if cand and difflib.SequenceMatcher(None, meta.norm(r.get('title')), meta.norm(cand.get('title'))).ratio() >= 0.92:
                    d = cand
                else:
                    d = None
            if d and d.get('abstract'):
                r.update(s2_title=d.get('title'), s2_abstract=d.get('abstract'), s2_authors=[a.get('name') for a in d.get('authors', [])],
                         s2_ids=d.get('externalIds'), abstract_source='semanticscholar')
        p.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    prim = [x for x in rows if x.get('tier') == 'primary']
    print(slug, 'primary with abstract', sum(1 for x in prim if x.get('abstract_source')), '/', len(prim), '| all', sum(1 for x in rows if x.get('abstract_source')), '/', len(rows))

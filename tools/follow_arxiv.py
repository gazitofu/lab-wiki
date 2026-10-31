# For rows without an abstract whose paper_page links to arXiv, fetch arxiv.org/abs/<id> (robots-checked via fetch.py) and take the posted abstract.
# Usage (inside batch folder): python3 ../tools/follow_arxiv.py SLUG [SLUG ...]
import json, re, sys, difflib
from pathlib import Path
sys.path.insert(0, '.')
import meta
for slug in sys.argv[1:]:
    p = Path(f'{slug}-meta.json'); rows = json.loads(p.read_text())
    for r in rows:
        if r.get('abstract_source'):
            continue
        ids = []
        pp = r.get('paper_page') or {}
        if pp.get('raw_key'):
            for l in json.loads((meta.fetch.RAW / f"{pp['raw_key']}.links.json").read_text()):
                m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', l['href'])
                if m and m.group(1) not in ids: ids.append(m.group(1))
        m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', r.get('doi_or_link') or '')
        if m and m.group(1) not in ids: ids.insert(0, m.group(1))
        for aid in ids[:2]:
            url = f'https://arxiv.org/abs/{aid}'
            meta.fetch.fetch_one(url); rec = meta.last_log()
            if rec.get('result') != 'read':
                r['arxiv_page'] = dict(url=url, result=rec.get('result')); continue
            txt = (meta.fetch.RAW / f"{rec['raw_key']}.txt").read_text()
            title = re.sub(r'^\[\d{4}\.\d{4,5}v?\d*\]\s*', '', (rec.get('title') or ''))
            ratio = difflib.SequenceMatcher(None, meta.norm(r.get('title')), meta.norm(title)).ratio()
            mm = re.search(r'Abstract:\s*(.+?)\n(?:Comments:|Subjects:|Submission history|Cite as:)', txt, re.S)
            r['arxiv_page'] = dict(url=url, raw_key=rec['raw_key'], title=title, title_ratio=round(ratio, 3))
            if mm and ratio >= 0.85:
                r['arxiv_abstract'] = ' '.join(mm.group(1).split()); r['abstract_source'] = 'arxiv-page'; r['arxiv_id'] = aid
                break
        p.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    prim = [x for x in rows if x.get('tier') == 'primary']
    print(slug, 'primary with abstract', sum(1 for x in prim if x.get('abstract_source')), '/', len(prim), '| all', sum(1 for x in rows if x.get('abstract_source')), '/', len(rows))

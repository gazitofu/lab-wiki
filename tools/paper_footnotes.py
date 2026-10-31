# Emit [^pN] footnote definitions for representative papers in order from {slug}-meta.json.
# Usage: python3 ../tools/paper_footnotes.py SLUG DOI1,DOI2,...  -> prints markdown lines
import json, re, sys, html
from pathlib import Path
slug, dois = sys.argv[1], [d.strip().lower() for d in sys.argv[2].split(',')]
rows = json.loads(Path(f'{slug}-meta.json').read_text())
by = {(r.get('doi') or '').lower(): r for r in rows if r.get('doi')}
by.update({f"r{r['rank']}": r for r in rows})
SRC = {'crossref': '초록 기준', 'semanticscholar': '초록 기준(Semantic Scholar 등록 초록)', 'arxiv': '초록 기준(arXiv 판)', 'paper-page': '초록 기준(논문 페이지 게시 초록)', 'publisher-page': '초록 기준(출판사 논문 페이지)', 'pure': '초록 기준(KAIST 연구자 포털 PURE 게시 초록)', 'europepmc': '초록 기준(Europe PMC 등록 초록)', 'conference-archive': '초록 기준(학회 아카이브 게시 초록)', 'proceedings-page': '초록 기준(학회 논문집 페이지 게시 초록)'}
def short(n):
    # 'Seungwon (Eugene) Jeong': drop a parenthetical nickname before abbreviating
    parts = re.sub(r'\s*\([^)]*\)', '', n).replace('‐', '-').split()
    if len(parts) < 2: return n
    ini = ' '.join('-'.join(p[0] + '.' for p in w.split('-') if p) for w in parts[:-1])
    return f'{ini} {parts[-1]}'
for i, d in enumerate(dois, 1):
    r = by[d]
    if r.get('match_warning'):
        # Crossref matched a different work: never reuse its authors/container/dates; fall back to the lab-posted record
        r = dict(r, authors=[re.sub(r'^and\s+', '', re.sub(r'[*†‡#+✝]', '', x).strip()) for x in re.split(r',| and ', r.get('authors_posted') or '') if x.strip() and x.strip() != 'and'],
                 s2_authors=None, container=r.get('venue'), volume=None, page=None, published_online=[None], published_print=[r.get('year')])
    au = r.get('authors') or r.get('s2_authors') or []
    names = [short(a) for a in au]
    who = ', '.join(names) if len(names) <= 4 else f"{names[0]} 외, {names[-1]}"
    c = html.unescape(r.get('container') or '')
    vol = r.get('volume'); pg = r.get('page')
    on = r.get('published_online') or [None]
    date = f" (온라인 {on[0]}-{on[1]:02d}-{on[2]:02d})" if on and len(on) == 3 and all(on) else (f" ({(r.get('published_print') or [None])[0] or on[0]})" if (r.get('published_print') or on) else '')
    src = SRC.get(r.get('abstract_source'), '초록 기준')
    vp = ' '.join(x for x in [c, str(vol) if vol else ''] if x) + (f", {pg}" if pg else '')
    link = f"https://doi.org/{r['doi']}" if r.get('doi') else (r.get('link') or (r.get('pure_page') or {}).get('url') or (r.get('paper_page') or {}).get('url') or r.get('doi_or_link'))
    print(f"[^p{i}]: {who}, {vp}{date}. <{link}> {src}.")

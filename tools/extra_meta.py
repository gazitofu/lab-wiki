#!/usr/bin/env python3
"""선정 후보 추가 + Crossref/S2 메타 조회 (batch 폴더에서 실행, 그 폴더의 meta.py 사용)

사용: python3 ../tools/extra_meta.py SLUG PUBS.json "제목 앞부분" ...
PUBS.json은 [{title, year, venue, authors, ...}] 목록. 제목 앞부분으로 찾아 {slug}-selection.json 에 backup 후보로 붙이고
meta.one 결과를 {slug}-meta.json 에 붙인다. 제목 일치도 0.9 미만이면 DOI·초록을 채택하지 않는다.
"""
import json, sys
from pathlib import Path
sys.path.insert(0, '.')
import meta

slug, pubs_path, prefixes = sys.argv[1], sys.argv[2], sys.argv[3:]
P = json.loads(Path(pubs_path).read_text())
sel = json.loads(Path(f'{slug}-selection.json').read_text())
rows = json.loads(Path(f'{slug}-meta.json').read_text())
have = {c['title'] for c in sel['candidates']}
nxt = max(c['rank'] for c in sel['candidates']) + 1
for pre in prefixes:
    p = next((x for x in P if x['title'].startswith(pre)), None)
    if not p or p['title'] in have:
        print('skip', pre[:50]); continue
    row = meta.one(p['title'])
    c = dict(rank=nxt, tier='backup', theme=None, year=p.get('year'), title=p['title'], venue=p.get('venue'), authors=p.get('authors'),
             doi_or_link=p.get('board_url') or p.get('doi_or_link'), pi_role=None, pi_role_basis='랩 목록 * 표기', why='추가 후보')
    row.update({k: c.get(k) for k in ('rank', 'tier', 'theme', 'title', 'year', 'venue', 'pi_role', 'pi_role_basis', 'why', 'doi_or_link')})
    row['authors_posted'] = p.get('authors')
    if row.get('title_ratio') is not None and row['title_ratio'] < 0.9:
        row['match_warning'] = 'Crossref title match below 0.9; DOI/abstract not adopted'
        for k in ('doi', 'cr_abstract', 's2_abstract'):
            row.pop(k, None)
        row['abstract_source'] = None
    sel['candidates'].append(c); rows.append(row); have.add(p['title']); nxt += 1
    Path(f'{slug}-selection.json').write_text(json.dumps(sel, ensure_ascii=False, indent=1))
    Path(f'{slug}-meta.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    print(c['rank'], row.get('doi'), row.get('title_ratio'), row.get('abstract_source'), p['title'][:60])

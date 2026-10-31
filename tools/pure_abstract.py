#!/usr/bin/env python3
"""KAIST PURE 논문 페이지에서 초록 보강 (batch 폴더에서 실행, 그 폴더의 fetch.py 사용)

사용: python3 ../tools/pure_abstract.py SLUG [rank ...]
초록이 없는 {slug}-meta.json 행마다 제목으로 PURE 주소(소문자·영숫자·하이픈, 앞 65자)를 만들어 한 번 요청하고,
페이지 제목과 논문 제목이 0.9 이상 일치할 때만 Abstract 문단을 pure_abstract로 저장한다(abstract_source='pure').
목록 페이지는 403이라 요청하지 않는다. 호스트 crawl-delay(5초)는 fetch.py가 지킨다.
"""
import difflib, json, re, sys
from pathlib import Path
sys.path.insert(0, '.')
import fetch

def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())

slug, ranks = sys.argv[1], {int(x) for x in sys.argv[2:]}
mp = Path(f'{slug}-meta.json'); rows = json.loads(mp.read_text())
for r in rows:
    if (r.get('abstract_source') and r.get('abstract_source') != 'pure') or (ranks and r['rank'] not in ranks):
        continue
    t = r['title']  # 랩 게시 제목 기준 (cr_title은 Crossref 오매칭일 수 있음)
    s = re.sub(r'\s+', '-', re.sub(r'[^a-z0-9\s-]', '', t.lower()).strip())[:65].rstrip('-')
    url = f'https://pure.kaist.ac.kr/en/publications/{s}/'
    fetch.fetch_one(url)
    rec = json.loads(fetch.LOG.read_text().splitlines()[-1])
    page = dict(url=url, result=rec.get('result'), raw_key=rec.get('raw_key'))
    r['pure_page'] = page
    r.pop('pure_abstract', None); r['abstract_source'] = None
    if rec.get('result') == 'read' and rec.get('raw_key'):
        L = [l.strip() for l in (fetch.RAW / f"{rec['raw_key']}.txt").read_text().splitlines() if l.strip()]
        title = (rec.get('title') or '').split(' - ')[0]
        ratio = difflib.SequenceMatcher(None, norm(title), norm(t)).ratio()
        page['title_ratio'] = round(ratio, 3)
        if ratio >= 0.9 and 'Abstract' in L:
            ab = L[L.index('Abstract') + 1]
            if len(ab) > 200:
                r['pure_abstract'] = ab; r['abstract_source'] = 'pure'
    mp.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    print(r['rank'], page.get('result'), page.get('title_ratio'), bool(r.get('pure_abstract')), t[:60])

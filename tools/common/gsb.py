# Print Google Sites page text after the last navigation-menu line LASTMENU (within the first 80 lines), minus site chrome.
# Usage: python3 gsb.py SLUG URL_SUFFIX LASTMENU [MAXLINES]   (URL_SUFFIX must match the end of the crawled URL)
import json, re, sys, fetch
slug, end, last = sys.argv[1], sys.argv[2], sys.argv[3]; n = int(sys.argv[4]) if len(sys.argv) > 4 else 100000
JUNK = ('Google Sites', '불건전 게시물 신고', '페이지 세부정보', '페이지 업데이트 시간:', '삽입된 파일', '이 사이트 검색', '메인 콘텐츠로 건너뛰기', '탐색으로 건너뛰기', '더보기')
for o in json.load(open('crawl.json')).get(slug, []):
    if o['url'].rstrip('/').endswith(end) and o.get('raw_key'):
        ls = [y for y in (' '.join(re.sub('[​⁡⁢⁣﻿]', '', x).replace('\xa0', ' ').split()) for x in (fetch.RAW / f"{o['raw_key']}.txt").read_text().split('\n')) if y and y != '|']
        i = max((j for j, x in enumerate(ls[:80]) if x == last), default=-1)
        print('#####', o['url'], o['raw_key'])
        print('\n'.join(x for x in ls[i + 1:i + 1 + n] if x not in JUNK))
        break

# Print page text after the breadcrumb line '홈으로' (gnuboard/PHP lab sites with a repeated menu). Usage: python3 hb.py SLUG URL_SUFFIX [MAXLINES]
import json, sys, fetch
slug, end = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
for o in json.load(open('crawl.json')).get(slug, []):
    if o['url'].rstrip('/').endswith(end) and o.get('raw_key'):
        ls = [' '.join(x.split()) for x in (fetch.RAW / f"{o['raw_key']}.txt").read_text().split('\n') if x.strip()]
        i = max((j for j, x in enumerate(ls) if x == '홈으로'), default=-1)
        k = next((j for j, x in enumerate(ls) if x.startswith('Department of Materials Science and Engineering, Korea Advanced')), len(ls))
        print('#####', o['url'], o['raw_key']); print('\n'.join(ls[i + 1:k][:n])); break

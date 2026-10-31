# Print Wix page text between the site menu ('Contact' line after 'Board') and the footer. Usage: python3 wixb.py SLUG URL_SUFFIX [MAXLINES]
import json, re, sys, fetch
slug, end = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
for o in json.load(open('crawl.json')).get(slug, []):
    if o['url'].rstrip('/').endswith(end) and o.get('raw_key'):
        ls = [y for y in (' '.join(re.sub('[​﻿]', '', x).replace('\xa0', ' ').split()) for x in (fetch.RAW / f"{o['raw_key']}.txt").read_text().split('\n')) if y]
        i = next((j for j in range(len(ls) - 1) if ls[j] == 'Board' and ls[j + 1] == 'Contact'), -2) + 2
        k = next((j for j, x in enumerate(ls) if x.startswith('Laboratory of Emerging Electronics, LEE Research Group')), len(ls))
        print('#####', o['url'], o['raw_key']); print('\n'.join(ls[i:k][:n])); break

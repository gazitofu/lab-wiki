# Print saved page text for a crawled URL. Usage: python3 show.py SLUG URL_SUBSTR [MAXCHARS]
import json, sys
from pathlib import Path
import fetch
slug, sub = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
for o in json.loads(Path('crawl.json').read_text()).get(slug, []):
    if sub in o['url'] and o.get('raw_key'):
        print('#####', o['url'], o['raw_key']); print((fetch.RAW / f"{o['raw_key']}.txt").read_text()[:n])

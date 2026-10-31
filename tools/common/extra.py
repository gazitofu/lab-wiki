# Fetch extra same-site pages for a lab through fetch.py and append them to crawl.json. Usage: python3 extra.py SLUG URL [URL ...]
import json, sys
from pathlib import Path
import fetch
slug, urls = sys.argv[1], sys.argv[2:]
out = []
for u in urls:
    fetch.fetch_one(u)
    r = [json.loads(l) for l in fetch.LOG.read_text().splitlines() if json.loads(l).get('kind') == 'page'][-1]
    out.append(dict(url=r['url'], result=r.get('result'), raw_key=r.get('raw_key'), title=r.get('title'), chars=r.get('text_chars')))
db = Path('crawl.json'); d = json.loads(db.read_text())
d.setdefault(slug, []).extend(out); db.write_text(json.dumps(d, ensure_ascii=False, indent=1))

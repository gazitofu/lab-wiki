# Fetch publisher article pages (robots-checked via fetch.py, own log) for rows still without an abstract; records slug/rank/url/raw_key in pub-pages.json.
# Usage: FETCH_LOG=fetch-log-pages.jsonl python3 pub_pages.py SLUG:RANK:URL [...]
import json, sys
from pathlib import Path
import fetch
db = Path('pub-pages.json'); d = json.loads(db.read_text()) if db.exists() else []
for a in sys.argv[1:]:
    slug, rank, url = a.split(':', 2)
    fetch.fetch_one(url)
    rec = [json.loads(l) for l in fetch.LOG.read_text().splitlines() if json.loads(l).get('kind') == 'page'][-1]
    d.append(dict(slug=slug, rank=int(rank), url=url, result=rec.get('result'), http_status=rec.get('http_status'), raw_key=rec.get('raw_key'), robots=rec.get('robots')))
    db.write_text(json.dumps(d, ensure_ascii=False, indent=1))
for x in d: print(x['slug'], x['rank'], x['result'], x['http_status'], x['robots'], x['url'])

# Fetch a lab homepage and its same-site menu pages (research/people/alumni/publications/patents/news/contact/professor) via fetch.py.
# Usage: python3 crawl_lab.py SLUG HOME_URL [EXTRA_URL ...]   -> appends {slug: [{url, raw_key, title, chars}]} to crawl.json
import json, re, sys, urllib.parse
from pathlib import Path
import fetch
KEYS = re.compile(r'research|people|member|team|alumni|graduate|publication|paper|journal|conference|patent|news|notice|board|contact|professor|faculty|pi\b|about|award|project|연구|구성원|멤버|졸업|논문|특허|소식|공지|연락|교수|수상|과제', re.I)
def last():
    return json.loads(fetch.LOG.read_text().splitlines()[-1])
def get(url):
    fetch.fetch_one(url)
    rows = [json.loads(l) for l in fetch.LOG.read_text().splitlines()]
    r = [x for x in rows if x.get('kind') == 'page'][-1]
    return r
slug, home, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
host = urllib.parse.urlsplit(home).netloc
out = []
r = get(home); out.append(dict(url=r['url'], result=r.get('result'), raw_key=r.get('raw_key'), title=r.get('title'), chars=r.get('text_chars')))
cands = []
if r.get('raw_key'):
    for l in json.loads((fetch.RAW / f"{r['raw_key']}.links.json").read_text()):
        h = urllib.parse.quote(l['href'].split('#')[0], safe=':/?&=%+;,@!$\'()*~')  # percent-encode non-ASCII paths/queries
        u = urllib.parse.urlsplit(h)
        if u.netloc == host and h.rstrip('/') != home.rstrip('/') and (KEYS.search(l['text']) or KEYS.search(u.path)) and not re.search(r'\.(pdf|jpg|png|zip|pptx?)$', u.path, re.I) and not re.search(r'login|logout|join|signup|register|mypage|account|wp-admin|write\.php|(?:^|[?&])w=\w', u.path + '?' + u.query, re.I):  # never open board write/edit forms
            if h not in cands: cands.append(h)
for h in (cands[:26] + [e for e in extra if e not in cands]):
    r = get(h); out.append(dict(url=r['url'], result=r.get('result'), raw_key=r.get('raw_key'), title=r.get('title'), chars=r.get('text_chars')))
db = Path('crawl.json'); d = json.loads(db.read_text()) if db.exists() else {}
d.setdefault(slug, []).extend(out); db.write_text(json.dumps(d, ensure_ascii=False, indent=1))
for o in out: print(slug, o['result'], o.get('chars'), o['url'][:110])

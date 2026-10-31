# -*- coding: utf-8 -*-
"""Contract-bound public page reader: robots check, one request per host, >=3 s spacing, no retry on 403/429/CAPTCHA.

Usage: python3 fetch.py URL [URL ...]
Raw bytes stay outside Vault; this batch keeps only the attempt log with hashes.
census-09: each lab runs from its own folder (own fetch-log.jsonl next to its copy of this file); host spacing is shared through RAW/host-locks.
fetch-log.jsonl has one row per HTTP request (kind robots|page). request_started_at is stamped
right before the request (after the host wait) and is the row's observed_at; elapsed_seconds is the request duration.
Redirects are not followed automatically: a 3xx is logged as its own row (result redirect, location), and the
Location is requested as a new call that goes through robots and wait_host again (hop, redirected_from).
Raw files are keyed by sha256(url|request_started_at) so a second read of the same URL never overwrites the first;
url_key = sha256(url)[:16] groups reads of one URL.
Link extraction strips the href before urljoin (batch-23 N1).
"""
import datetime as dt
import hashlib
import html.parser
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from pathlib import Path

R = Path(__file__).resolve().parent
RAW = Path('__RAW__')
# new_batch.py의 전체 문자열 치환이 종료 조건까지 바꾸지 않도록 나눠 쓴다.
if str(RAW) == '__' + 'RAW__':
    raise SystemExit('RAW 자리표시가 치환되지 않음: new_batch.py로 차수를 생성하세요')
import os
LOG = R / os.environ.get('FETCH_LOG', 'fetch-log.jsonl')  # a second concurrent process uses its own log file
LOCKS = Path('/Users/gazitofu/Library/Application Support/Lab-wiki/host-locks')  # one file per host: last request start time, guarded by flock across processes
UA = 'Lab-wiki-collector/0.1 (public research pages; 1 req/host, 3s spacing)'
SPACING = 3.0
TIMEOUT = 20
MAX_HOPS = 5
RAW.mkdir(parents=True, exist_ok=True)
LOCKS.mkdir(parents=True, exist_ok=True)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # surface the 3xx as HTTPError so each hop is a separate logged call


OPENER = urllib.request.build_opener(NoRedirect)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


DELAY = {}  # host -> robots Crawl-Delay seconds; spacing is max(SPACING, crawl-delay)


def wait_host(host):
    # census-09 runs labs in parallel processes: the per-host lock is held across read, sleep and write,
    # so two processes never start requests to the same host less than `need` seconds apart
    import fcntl
    with open(LOCKS / (host.replace(':', '_') + '.last'), 'a+') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        gap = time.time() - (float(raw) if raw else 0.0)
        need = max(SPACING, DELAY.get(host, 0))
        if gap < need:
            time.sleep(need - gap)
        f.seek(0)
        f.truncate()
        started_at = time.time()
        f.write(repr(started_at))
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)
    return dict(required_spacing_seconds=need, waited_seconds=round(max(0.0, need - gap), 3),
                request_started_at=dt.datetime.fromtimestamp(started_at, dt.timezone.utc).isoformat())


def get(url, rec):
    host = urllib.parse.urlsplit(url).hostname.lower()
    rec.update(wait_host(host))
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'ko,en;q=0.8'})
    rec['observed_at'] = rec['request_started_at']
    t0 = time.monotonic()
    try:
        with OPENER.open(req, timeout=TIMEOUT) as r:
            return r.status, r.headers, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers, e.read() if e.fp else b''
    finally:
        rec['elapsed_seconds'] = round(time.monotonic() - t0, 3)


def log(rec):
    with LOG.open('a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


def rfc9309_allows(text, url):
    # urllib.robotparser returns the first matching rule, so "Allow: /" listed before "Disallow: /api" allowed /api
    # (census-09 sound, 2026-10-21). RFC 9309: the longest matching path wins; on a tie Allow wins.
    groups, cur, last_was_agent = [], None, False
    for line in text.splitlines():
        line = line.split('#', 1)[0].strip()
        if ':' not in line:
            continue
        k, v = (x.strip() for x in line.split(':', 1))
        k = k.lower()
        if k == 'user-agent':
            if not last_was_agent:
                cur = dict(agents=[], rules=[]); groups.append(cur)
            cur['agents'].append(v.lower()); last_was_agent = True
            continue
        last_was_agent = False
        if cur is not None and k in ('allow', 'disallow'):
            cur['rules'].append((k, v))
    token = 'lab-wiki-collector'
    mine = [g for g in groups if any(a != '*' and a in token for a in g['agents'])] or [g for g in groups if '*' in g['agents']]
    rules = [r for g in mine for r in g['rules']]
    parts = urllib.parse.urlsplit(url)
    path = (parts.path or '/') + (('?' + parts.query) if parts.query else '')
    best = None
    for kind, pat in rules:
        if not pat:
            continue  # empty Disallow allows everything
        rx = '^' + re.escape(pat).replace(r'\*', '.*')
        if rx.endswith(r'\$'):
            rx = rx[:-2] + '$'
        if re.match(rx, path) or re.match(rx, urllib.parse.unquote(path)):
            if best is None or len(pat) > len(best[1]) or (len(pat) == len(best[1]) and kind == 'allow'):
                best = (kind, pat)
    return best is None or best[0] == 'allow'


def robots_allows(url):
    parts = urllib.parse.urlsplit(url)
    rurl = f'{parts.scheme}://{parts.netloc}/robots.txt'
    cache = RAW / ('robots-' + parts.scheme + '-' + parts.netloc.replace(':', '_') + '.txt')
    status = None
    if not cache.exists():
        target, body, chain = rurl, b'', []
        for hop in range(MAX_HOPS + 1):  # robots redirects are followed hop by hop, each a logged call
            rec = dict(kind='robots', url=target, attempts=1, hop=hop, redirected_from=chain[-1] if chain else None)
            try:
                status, headers, body = get(target, rec)
                rec.update(http_status=status, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            except Exception as e:  # network failure: record and treat as unknown
                status, headers, body = f'error:{type(e).__name__}', None, b''
                rec.update(http_status=None, detail=str(e)[:200])
            loc = headers.get('Location') if headers and status in (301, 302, 303, 307, 308) else None
            rec['result'] = f'robots-{status}'
            if loc:
                rec['location'] = urllib.parse.urljoin(target, loc)
            log(rec)
            if not loc:
                break
            chain.append(target)
            target = rec['location']
            if hop == MAX_HOPS:
                status, body = 'redirect-hop-limit', b''
        cache.write_bytes(json.dumps(dict(url=rurl, final_url=target, redirect_chain=chain, status=status, at=rec.get('request_started_at'))).encode() + b'\n' + body)
    meta, _, body = cache.read_bytes().partition(b'\n')
    status = json.loads(meta)['status']
    if status == 200:
        rp = urllib.robotparser.RobotFileParser()
        rp.parse(body.decode('utf-8', 'replace').splitlines())
        delay = rp.crawl_delay(UA)
        if delay:
            DELAY[parts.hostname.lower()] = float(delay)
        return rfc9309_allows(body.decode('utf-8', 'replace'), url), f'robots 200 parsed (longest match)' + (f'; crawl-delay {delay}s honored' if delay else '')
    if isinstance(status, int) and 400 <= status < 500 and status not in (401, 403):
        return True, f'robots {status}: no robots file'
    return False, f'robots {status}: unresolved, not fetched'

class Text(html.parser.HTMLParser):
    BLOCK = {'p', 'div', 'br', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'th', 'section', 'article', 'header', 'footer', 'dt', 'dd', 'table', 'ul', 'ol'}
    SKIP = {'script', 'style', 'noscript', 'svg'}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.out, self.links, self.skip, self.href, self.atext, self.title, self.in_title = base, [], [], 0, None, [], '', False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self.skip += 1
        if tag == 'title':
            self.in_title = True
        if tag in self.BLOCK:
            self.out.append('\n')
        if tag == 'td' or tag == 'th':
            self.out.append(' | ')
        if tag == 'a' and a.get('href') and a['href'].strip():
            # strip before urljoin: a leading-space href was joined onto the page URL in batch-23 (N1)
            self.href, self.atext = urllib.parse.urljoin(self.base, a['href'].strip()), []
        if tag == 'img' and a.get('alt'):
            self.out.append(f' [img:{a["alt"]}] ')

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag == 'title':
            self.in_title = False
        if tag == 'a' and self.href:
            self.links.append(dict(href=self.href, text=' '.join(''.join(self.atext).split())))
            self.href = None
        if tag in self.BLOCK:
            self.out.append('\n')

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.skip:
            return
        self.out.append(data)
        if self.href is not None:
            self.atext.append(data)

    def text(self):
        t = ''.join(self.out)
        t = re.sub(r'[ \t\r\f\v]+', ' ', t)
        return re.sub(r'\n\s*\n+', '\n', t).strip()


def main(urls):
    for url in urls:
        fetch_one(url)


def fetch_one(url, hop=0, redirected_from=None):
    rec = dict(kind='page', url=url, attempts=1, hop=hop, redirected_from=redirected_from)
    allowed, why = robots_allows(url)
    rec['robots'] = why
    if not allowed:
        rec.update(result='not-fetched-robots', http_status=None, observed_at=now())
    else:
        try:
            status, headers, body = get(url, rec)
            ctype = headers.get('Content-Type', '') if headers else ''
            final = url
            rec.update(http_status=status, final_url=final, content_type=ctype, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            # A 'captcha' string alone is not a challenge (e.g. a contact-form plugin); flag it and inspect the text.
            rec['captcha_string_present'] = b'captcha' in body.lower()
            if status in (301, 302, 303, 307, 308):
                loc = headers.get('Location') if headers else None
                rec.update(result='redirect', location=urllib.parse.urljoin(url, loc) if loc else None)
            elif status in (403, 429):
                rec['result'] = 'blocked-not-retried'
            elif status == 200:
                key = hashlib.sha256((url + '|' + rec['request_started_at']).encode()).hexdigest()[:16]
                assert not (RAW / f'{key}.raw').exists(), key
                (RAW / f'{key}.raw').write_bytes(body)
                charset = re.search(r'charset=([\w-]+)', ctype or '')
                doc = body.decode(charset.group(1) if charset else 'utf-8', 'replace')
                p = Text(final)
                p.feed(doc)
                (RAW / f'{key}.txt').write_text(p.text())
                (RAW / f'{key}.links.json').write_text(json.dumps(p.links, ensure_ascii=False, indent=1))
                rec.update(result='read', title=' '.join(p.title.split()), raw_key=key, url_key=hashlib.sha256(url.encode()).hexdigest()[:16], text_chars=len(p.text()), links=len(p.links))
            else:
                rec['result'] = f'http-{status}'
        except Exception as e:
            rec.update(result=f'error:{type(e).__name__}', http_status=None, detail=str(e)[:200])
            rec.setdefault('observed_at', now())
    log(rec)
    print(json.dumps({k: rec.get(k) for k in ['url', 'hop', 'result', 'http_status', 'location', 'robots', 'title', 'raw_key', 'text_chars', 'links']}, ensure_ascii=False))
    if rec.get('result') == 'redirect' and rec.get('location'):
        if hop + 1 > MAX_HOPS:
            log(dict(kind='note', url=rec['location'], result='redirect-hop-limit-not-fetched', observed_at=now(), hop=hop + 1, redirected_from=url))
        else:
            fetch_one(rec['location'], hop + 1, url)


if __name__ == '__main__':
    main(sys.argv[1:])

# Lab checks beyond check_doc/check_gloss/check_tags (offline). Each key is a rule marked [검사] in
# collection-staging/brief-common.md §5; keys starting with warn_ need a reading of the source, the rest must be empty/true.
# Successor of the batch copies census-57/_codex/main_check.py and snu-23/_codex/main_check.py.
# usage: python3 check_lab.py SLUG [SLUG ...]      (run in the batch folder or in the lab folder)
#        python3 check_lab.py --docs PAGE.md [...]  (document checks only, e.g. registered wiki/{kaist,snu} pages)
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inst import INSTS, detect
from names import same_person

PROCESS = ['웹 도구', 'web tool', '봇 확인', '확인 화면', 'Crawled', 'tags.json', '(403)', '(429)', 'HTTP 4', 'HTTP 5',
           'Internal Error', 'not accessible', 'Cache miss', '재요청', '재시도', 'fetch.py', 'evidence/', '.web.txt',
           'precheck', 'snu:', 'kaist:', '리디렉트', '리다이렉트', 'plan.md', 'plan §', 'data-contract', '독립 QA',
           'QA에서', '검토에서', '지적되어', '이전 등록본', '미수집', '미검증', 'Between Jobs', '구직 중']
# 「robots」 alone is a research word (soft robots); the access sense is robots.txt or robots followed by Korean
ROBOTS = re.compile(r'robots(?:\.txt|[가-힣]| 규칙| 금지| 파일)')
BODY_ONLY = ['영향력 지수']  # the sources page may state that impact factors were left out
HISTORY = re.compile(r'(?:어휘|태그)[^.\n]{0,40}(?:요청|제안)|(?:요청|제안)[^.\n]{0,20}어휘|census-\d+|snu-\d+')
# pictographs only: dingbat arrows (U+2794) and the posted author mark (U+271D) are text
EMOJI = re.compile('[%s-%s%s-%s%s]' % (chr(0x1F000), chr(0x1F2FF), chr(0x1F300), chr(0x1FAFF),
                   ''.join(map(chr, (0x2764, 0x2728, 0x2705, 0x274C, 0x2B50, 0x270C, 0xFE0F)))))
OBFUSCATED = re.compile(r'[A-Za-z0-9._-]+\s*[(\[{]\s*(?:at|AT|At)\s*[)\]}]\s*[A-Za-z0-9-]+\.[A-Za-z]')
# spaced @ is also a job line (CEO @ Softly.ai), so it is a warning
SPACED_AT = re.compile(r'[A-Za-z0-9._-]+ +@ *[A-Za-z0-9-]+\.[A-Za-z]|[A-Za-z0-9._-]+ *@ +[A-Za-z0-9-]+\.[A-Za-z]')
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+')
WARN = {
    'warn_scale': re.compile(r'\bTop[ -]?\d+|out of \d+|\d+\s?대 (?:기술|과제|발명)|경쟁률|상위 \d+(?:\.\d+)?\s?%'),
    'warn_cover': re.compile(r'(?:Front|Back|Inside|Supplementary)[ -][Cc]over|[Cc]over (?:[Aa]rticle|[Ii]mage|[Aa]rt|[Pp]age)|Frontispiece|Highlighted in|Hot [Pp]aper|표지 (?:논문|선정|게재)'),
    'warn_military': re.compile(r'전문연구요원|산업기능요원|병역|군 복무|[Mm]ilitary [Ss]ervice|\bROKA\b|Korean (?:Army|Navy|Air Force)|Republic of Korea (?:Army|Navy|Air Force)'),
    'warn_orders_of_magnitude': re.compile(r'자릿수'),
}
QUANTITY = re.compile(r'(?<![\w.])\d+(?:\.\d+)?[MKB](?![\w-])')  # '300 K' with a space is kelvin
GLOSS_COMPARE = ['더 ', '덜 ', '보다', '할수록', '수록 ', '처럼', '같은 모양', '얻기 어려운']
GLOSS_SIZE = ['아주 ', '매우 ', '비교적', '흐릿', '덜 중요']
LIST_PAGE = re.compile(r'Publications?|논문 목록|Papers|Members?|People|구성원|Alumni|졸업생|News|소식|Equipment|Facilit|장비|Gallery|갤러리')


def read(f):
    # an EUC-KR raw page is read as cp949; raw HTML character references are unescaped (emails written as &#104;...)
    b = f.read_bytes()
    try:
        t = b.decode('utf-8')
    except UnicodeDecodeError:
        t = b.decode('cp949', 'replace')
    return html.unescape(t) if f.suffix == '.raw' else t


def doc_checks(body, src):
    res = {}
    lines = body.splitlines()
    head = body.split('\n## ', 1)[0]
    res['readme_head_ok'] = (len(lines) > 2 and lines[0].startswith('# ') and lines[1] == ''
                             and lines[2].startswith('**') and lines[2].endswith('**') and ' · ' in lines[2])
    res['footnote_on_affiliation_line'] = len(lines) > 2 and '[^' in lines[2]
    res['summary_line'] = any(ln.startswith('> ') for ln in head.splitlines())
    res['summary_section'] = bool(re.search(r'^## 한 줄 요약', body, re.M))
    res['warn_no_sources_line'] = not any(ln.startswith('- 근거와 출처:') for ln in head.splitlines())
    both = {'body': body.replace('로봇', ''), 'sources': src.replace('로봇', '')}
    for k, t in both.items():
        words = PROCESS + (BODY_ONLY if k == 'body' else [])
        res[f'process_words_in_{k}'] = sorted({w for w in words if w in t} | set(ROBOTS.findall(t)))
    res['history_in_docs'] = sorted({m.group(0) for m in HISTORY.finditer(src + '\n' + body)})
    res['emoji'] = sorted({m.group(0) for m in EMOJI.finditer(src + '\n' + body)})
    res['obfuscated_email'] = sorted({m.group(0) for m in OBFUSCATED.finditer(src + '\n' + body)})
    res['warn_spaced_at'] = sorted({m.group(0) for m in SPACED_AT.finditer(src + '\n' + body)})
    # cover and military words may be quoted in the sources page as the criterion (brief-common §5.1-6, §5.5-3); scale may not
    for k, rx in WARN.items():
        res[k] = sorted({m.group(0) for m in rx.finditer(body if k in ('warn_cover', 'warn_military') else src + '\n' + body)})
    # quantities written as 1.3M·31K in prose (head part, not footnote definitions or list rows)
    prose = [ln for ln in head.splitlines() + body.split('\n## 구성원', 1)[0].splitlines()
             if not ln.startswith(('[^', '|', '- 태그', '- 홈페이지', '- 근거'))]
    res['warn_quantity_suffix'] = sorted({m.group(0) for ln in prose for m in QUANTITY.finditer(re.sub(r'\[\^[^\]]+\]|<[^>]+>|`[^`]*`', '', ln))})
    res.update(tag_checks(body))
    return res


def tag_checks(body):
    # brief-common §5.10-3: a tag footnote should also carry a body sentence (outside the head list), and not only list/member pages
    lines = body.splitlines()
    tag_line = next((ln for ln in lines if ln.startswith('- 태그: ')), '')
    defs = dict(re.findall(r'^\[\^([^\]]+)\]:\s*(.*)$', body, re.M))
    head_end = next((i for i, ln in enumerate(lines) if ln.startswith('## ')), len(lines))
    body_lines = [ln for ln in lines[head_end:] if not ln.startswith('[^')]
    cited = set(re.findall(r'\[\^([^\]]+)\]', '\n'.join(body_lines)))
    not_in_body, list_only = [], []
    for item in tag_line.removeprefix('- 태그: ').split(', ') if tag_line else []:
        name = re.sub(r'\[\^[^\]]+\]', '', item).strip()
        fns = re.findall(r'\[\^([^\]]+)\]', item)
        if fns and not any(f in cited for f in fns):
            not_in_body.append(name)
        if fns and all(LIST_PAGE.search(defs.get(f, '').split('<')[0]) and not re.fullmatch(r'p\d+', f) for f in fns):
            list_only.append(name)
    return {'warn_tag_fn_not_in_body': not_in_body, 'warn_tag_fn_list_pages_only': list_only}


def lab_checks(lab, slug, wiki):
    body = (lab / wiki / f'{slug}.md').read_text()
    src = (lab / wiki / f'{slug}-sources.md').read_text()
    res = dict(lab=slug, **doc_checks(body, src))
    lines = body.splitlines()
    gpath = lab / f'{slug}-gloss.json'
    bad = []
    if gpath.exists():
        g = json.loads(gpath.read_text())
        items = g if isinstance(g, list) else ((g.get('pages') or {}).get(slug) or g.get('terms') or [])
        if isinstance(items, dict):
            items = [dict(term=k, **v) if isinstance(v, dict) else dict(term=k, definition=v) for k, v in items.items()]
        for it in items:
            ctx = it.get('context') or ''
            on_line = any(ctx and ctx in ln and not ln.startswith('#') for ln in lines)
            if not on_line or not (40 <= len(ctx) <= 80):
                bad.append(dict(term=it.get('term'), len=len(ctx), on_line=on_line))
            tip = it.get('tip') or it.get('definition') or ''
            hits = [w for w in GLOSS_COMPARE + GLOSS_SIZE if w in tip]
            if hits:
                bad.append(dict(term=it.get('term'), words=hits, tip=tip))
        res['gloss_n'] = len(items)
    else:
        res['gloss_missing'] = True
    res['gloss_problems'] = bad
    # emails in the body must be posted on a cited page whose screen text has no 「수집」+「거부」 notice (brief-common §5.1-4)
    ev = lab / 'evidence'
    pages = []
    for f in (sorted(ev.glob('*.web.txt')) + sorted(ev.glob('*.browser.txt')) + sorted(ev.glob('*.chrome.txt'))
              + sorted(ev.glob('*.fetch.raw')) + sorted(ev.glob('*.fetch.txt')) + sorted(ev.glob('*.saved.txt'))
              + sorted((lab / 'precheck').glob('*.raw'))):
        t = read(f)
        screen = f.with_suffix('.txt') if f.suffix == '.raw' else f
        pages.append((f, t, read(screen) if screen.exists() else t))
    emails = sorted(set(EMAIL.findall(body)))
    res['body_emails'] = len(emails)
    res['emails_only_on_refusal_pages_or_absent'] = [
        e for e in emails if not any((e in t or e in scr) and not ('수집' in scr and '거부' in scr) for _, t, scr in pages)]
    # 「대표 논문 참여」 marks need the identical name in that paper's author list (brief-common §5.6-2)
    mpath = lab / f'{slug}-meta.json'
    wrong = []
    if mpath.exists():
        meta = json.loads(mpath.read_text())
        meta = meta if isinstance(meta, list) else meta.get('papers') or list(meta.values())
        def authors(r):
            au = r.get('authors') if isinstance(r.get('authors'), list) else []
            if not au and r.get('authors_posted'):
                au = re.split(r',| and ', r['authors_posted'])
            return au
        rows = [r for r in meta if isinstance(r, dict)]
        by_rank = {int(r['rank']): authors(r) for r in rows if r.get('rank') is not None}
        # render_lists numbers the marks by the body's representative-paper table rows (the --order from order_from_head),
        # which need not equal meta rank (snu-24 yunhochem kept candidate numbers as rank), so map the table row to its meta row
        norm = lambda s: re.sub(r'[^a-z0-9]', '', (s or '').lower())
        by_num = {}
        for n, cell in re.findall(r'^\| (\d+) \| \d{4} \| (.*?) \|', body, re.M):
            m = re.search(r'https://doi\.org/(10\.[^)\s]+)', cell)
            hit = [r for r in rows if m and (r.get('doi') or '').lower() == m.group(1).lower()]
            if not hit:
                t = norm(re.sub(r'^\[|\]\(.*$', '', cell.split(' · ')[0]))
                hit = [r for r in rows if t and norm(r.get('title')) and (t in norm(r.get('title')) or norm(r.get('title')) in t)]
            if len(hit) == 1:
                by_num[int(n)] = authors(hit[0])
        by_rank = by_num or by_rank
        header = None
        for ln in lines:
            if ln.startswith('| ') and '대표 논문 참여' in ln:
                header = [c.strip() for c in ln.strip('|').split('|')]
                continue
            if header and ln.startswith('|') and not ln.startswith('|---'):
                cells = [c.strip() for c in ln.strip('|').split('|')]
                if len(cells) != len(header):
                    continue
                marks = re.findall(r'\d+', cells[header.index('대표 논문 참여')])
                if not marks:
                    continue
                # a name cell may carry a footnote mark (snu-24 songroup 「Seungwon Jeong[^member-seungwon]」)
                nm = re.sub(r'\[\^[^\]]+\]', '', cells[0]).replace('\\|', '|').strip()
                outside = re.sub(r'\(.*?\)', '', nm).strip()
                par = re.findall(r'\((.*?)\)', nm)
                latin = outside if re.search('[A-Za-z]', outside) else next((x for x in par if re.search('[A-Za-z]', x)), outside)
                for k in marks:
                    if not any(same_person(latin, a) for a in by_rank.get(int(k), [])):
                        wrong.append(f'{nm} → {k}')
            elif not ln.startswith('|'):
                header = None
    res['member_marks_without_identical_author'] = wrong
    return res


def problems(res):
    bad = []
    for k, v in res.items():
        if k in ('lab', 'doc', 'gloss_n', 'body_emails') or k.startswith('warn_'):
            continue
        if k in ('readme_head_ok', 'summary_line'):
            if not v:
                bad.append(k)
        elif v:
            bad.append(k)
    return bad


def main(argv):
    if argv[:1] == ['--docs']:
        rc = 0
        for p in map(Path, argv[1:]):
            src = p.with_name(p.stem + '-sources.md')
            res = dict(doc=str(p), **doc_checks(p.read_text(), src.read_text() if src.exists() else ''))
            print(json.dumps(res, ensure_ascii=False))
            rc |= bool(problems(res))
        return rc
    inst = detect()
    wiki = INSTS[inst]['wiki']
    rc = 0
    for slug in argv:
        cwd = Path.cwd()
        lab = cwd if cwd.name == slug and (cwd / wiki).is_dir() else cwd / slug
        res = lab_checks(lab, slug, wiki)
        res['problems'] = problems(res)
        print(json.dumps(res, ensure_ascii=False))
        rc |= bool(res['problems'])
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# Render reference sections (members, alumni, recent papers, patents, projects, news) from {slug}-lists.json + {slug}-meta.json.
# Usage (run inside a batch folder): python3 ../tools/render_lists.py SLUG [--order DOI1,DOI2,...]  -> writes {slug}.lists.md
import html, json, re, sys
from pathlib import Path
slug = sys.argv[1]
args = dict(zip(sys.argv[2::2], sys.argv[3::2]))
L = json.loads(Path(f'{slug}-lists.json').read_text())
meta = json.loads(Path(f'{slug}-meta.json').read_text()) if Path(f'{slug}-meta.json').exists() else []
order = [d.strip().lower() for d in args.get('--order', '').split(',') if d.strip()]
norm = lambda s: re.sub(r'[^a-z]', '', (s or '').lower())
def authors_of(key):
    # key: a DOI, or 'r<rank>' for rows without DOI (authors from Crossref/S2/arXiv lists, else the lab-posted author string)
    for r in meta:
        if (key.startswith('r') and key[1:].isdigit() and r.get('rank') == int(key[1:])) or (r.get('doi') or '').lower() == key:
            au = r.get('authors') if isinstance(r.get('authors'), list) and not r.get('match_warning') else []
            au = au or r.get('s2_authors') or r.get('arxiv_authors') or []
            if not au and r.get('authors_posted'):
                au = [re.sub(r'[*†‡#+✝]', '', x).replace(' and ', ' ').strip() for x in re.split(r',| and ', r['authors_posted'])]
            return [x for x in au if x]
    return []
def toks(n):
    return [t for t in re.split(r'[^a-z]+', (n or '').lower().replace('-', '')) if t]
def same_person(a, b):
    if _same_person(a, b):
        return True
    # 'Lim, Yoon Seop' vs 'Yoon-Seop Lim': merge adjacent given-name tokens and retry
    for va in _variants(a):
        for vb in _variants(b):
            if (va, vb) != (a, b) and _same_person(va, vb):
                return True
    return False
def _variants(n):
    t = toks(n); out = [n]
    if len(t) == 3:
        out += [f'{t[0]}{t[1]} {t[2]}', f'{t[0]} {t[1]}{t[2]}']
    return out
def _same_person(a, b):
    # order-insensitive token match; single-letter tokens match initials (handles 'Jung, Hyunwoo' vs 'Hyunwoo Jung', 'Hung D. Nguyen' vs 'Nguyen Duy Hung')
    ta, tb = toks(a), toks(b)
    if ta and tb and abs(len(ta) - len(tb)) == 1:
        # 'Y. Han' vs 'Yoon Seong Han': shorter name = full surname + initials, longer has one extra given-name token
        sh, lo = (ta, tb) if len(ta) < len(tb) else (tb, ta)
        if len(sh) >= 2 and all(len(x) > 1 for x in sh) and all(x in lo for x in sh):
            return True  # 'Rachel Kim' vs 'Rachel Jungmin Kim'
        if any(len(t) == 1 for t in sh):
            left = list(lo)
            for t in sh:
                hit = next((x for x in left if x == t), None) if len(t) > 1 else next((x for x in left if x[0] == t and len(x) > 1), None)
                if not hit: return False
                left.remove(hit)
            return sum(1 for t in sh if len(t) > 1) >= 1
    if not ta or not tb or len(ta) != len(tb):
        return norm(a) == norm(b) and bool(norm(a))
    left = list(tb)
    for t in ta:
        hit = next((x for x in left if x == t), None) or next((x for x in left if (len(x) == 1 and t[0] == x) or (len(t) == 1 and x[0] == t)), None)
        if not hit: return False
        left.remove(hit)
    return sum(1 for t in ta if len(t) > 1 and t in tb) >= 1
rep_authors = [(i + 1, authors_of(d)) for i, d in enumerate(order)]
STAGE = [(r'post[- ]?doc|postdoctoral|박사후', '박사후연구원'), (r'^graduate student$', '대학원생'), (r'post-?master', '연구원'), (r'integrated|통합|m\.?s\.?\s*/\s*ph\.?\s?d|master-ph\.?\s?d|m\.?s\.?\s*[-+&]\s*ph\.?\s?d|ph\.?\s?d\.?\s*[-+&/]\s*m\.?s|joint\s+program|combined', '석박사통합과정'), (r'ph\.?\s?d|doctoral|박사', '박사과정'),
         (r'm\.?\s?sc?\b|master|석사', '석사과정'), (r'undergrad\w*\s+(?:research\s+)?intern|학부\s*(?:연구\s*)?인턴', '학부 인턴'), (r'undergrad|학부', '학부 연구생'), (r'intern', '인턴'), (r'visiting student|방문 학생', '방문 학생'), (r'visit|방문', '방문 연구원'),
         (r'research\s+associate\s+professor', '연구부교수'), (r'research\s+assistant\s+professor', '연구조교수'), (r'research\s+professor|연구교수', '연구교수'), (r'graduate\s+researcher', '대학원 연구원'), (r'research\s+staff', '연구 직원'), (r'research(er| fellow| scientist| engineer| associate)|연구원', '연구원'), (r'staff|secretary|admin|행정', '행정 직원')]
def stage_ko(s):
    s0 = (s or '').lower()
    paren = re.search(r'\(([^()]*)\)\s*$', s or '')  # keep a posted qualifier such as an affiliation or period
    pre = '입학 예정 ' if re.search(r'upcoming|incoming', s0) else ''  # 'Upcoming M.S. Student' must not read as a current student
    for pat, ko in STAGE:
        if re.search(pat, re.sub(r'\([^()]*\)\s*$', '', s0).strip()):
            return pre + (f'{ko} ({paren.group(1)})' if paren else ko)
    return s or ''
def esc(s):
    # posted titles sometimes carry an em dash; the wiki style bans it, so ' — ' becomes ': ' and a bare one a hyphen
    # inline markup in posted titles (CO<sub>2</sub>, <i>PN</i>) would pass through as raw HTML; keep the text only
    s = re.sub(r'</?(?:sub|sup|i|b|em|strong)>', '', s or '', flags=re.I)
    # a posted '[x](y)' (e.g. news '[초순수 국산화](하)') would render as a link
    s = s.replace('](', r'\](')
    return s.replace(' — ', ': ').replace('—', '-').replace('|', '／').replace('*', r'\*').strip()
out = []
M = L.get('members') or []
if M:
    has = {k: any(m.get(k) for m in M) for k in ('stage_posted', 'start_posted', 'topic_posted', 'email_posted')}
    cols = ['이름'] + (['과정'] if has['stage_posted'] else []) + (['시작'] if has['start_posted'] else []) + (['연구 주제'] if has['topic_posted'] else []) + (['이메일'] if has['email_posted'] else []) + (['대표 논문 참여'] if order else [])
    out += ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    for m in M:
        nm = m.get('name') or ''
        par = re.findall(r'\((.*?)\)', nm)
        outside = re.sub(r'\(.*?\)', '', nm).strip()
        # '박준하(Joonha Park)' → parenthetical Latin; 'Kim, Min Seo (Mason)' → nickname ignored
        latin = outside if re.search('[A-Za-z]', outside) else next((x for x in par if re.search('[A-Za-z]', x)), outside)
        names = [latin] + list(m.get('aliases') or [])  # aliases: other spellings the lab itself uses for the member
        hits = [str(i) for i, au in rep_authors if any(same_person(n, x) for n in names for x in au)]
        row = [esc(nm)] + ([stage_ko(m.get('stage_posted'))] if has['stage_posted'] else [])
        if has['start_posted']: row.append(esc(m.get('start_posted') or ''))
        if has['topic_posted']: row.append(esc(m.get('topic_posted') or ''))
        if has['email_posted']: row.append(esc(m.get('email_posted') or ''))
        if order: row.append(', '.join(hits))
        out.append('| ' + ' | '.join(row) + ' |')
    out.append('')
A = L.get('alumni') or []
if A:
    th = any(a.get('thesis_posted') for a in A)
    aw = any(a.get('award_posted') for a in A)
    out += ['<!--ALUMNI-->', '| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |' + (' 학위 논문 |' if th else '') + (' 랩이 적은 수상 |' if aw else ''), '|---|---|---|' + ('---|' if th else '') + ('---|' if aw else '')]
    for a in A:
        deg = ' '.join(x for x in [a.get('degree_posted') or '', f"({a['year_posted']})" if a.get('year_posted') else ''] if x)
        out.append(f"| {esc(a.get('name'))} | {esc(deg)} | {esc(a.get('destination_posted') or '')} |" + (f" {esc(a.get('thesis_posted') or '')} |" if th else '') + (f" {esc(a.get('award_posted') or '')} |" if aw else ''))
    out.append('')
P = L.get('publications') or []
if P:
    out.append('<!--PAPERS-->')
    cur = None
    for p in sorted(P, key=lambda x: -(x.get('year') or 0)):
        if p.get('year') != cur:
            cur = p.get('year'); out += ['', f"**{cur if cur else '연도 표기 없음'}**", '']
        if p.get('text_posted') and not p.get('title'):
            # a posted line whose author/title/venue boundaries the lab does not mark (no quotes): carried as one line
            tp = re.sub(r',?\s*accept(?:ance)?\s+rate:?\s*\d+(?:\.\d+)?\s*%', '', html.unescape(p['text_posted']), flags=re.I)  # no acceptance rates (data-contract v0.3)
            tp = re.sub(r'\s*\[(?:project page|paper|code|video|pdf|link)\]', '', tp, flags=re.I)  # link labels without their links
            out.append(f"- {esc(tp)}"); continue
        t = html.unescape((p.get('title') or '').strip().strip('"“”').rstrip(',.'))
        v = html.unescape(re.sub(r'\s+', ' ', (p.get('venue') or '')).strip().rstrip(',.'))
        # never carry journal metrics or acceptance rates (data-contract v0.3)
        v = re.sub(r'\s*\[(?:SCIE|SSCI|SCI|A&HCI|AHCI|ESCI|SCOPUS|KCI|Q[1-4])\b[^\]]*\]', '', v, flags=re.I)  # index/quartile/percentile tags
        v = re.sub(r'\s*\[\s*(?:IF\b|Impact Factor)\s*[:=]?[^\]]*\]', '', v, flags=re.I)
        v = re.sub(r'\s*\((?:Impact Factor|IF\b)\s*[:=]?[^)]*\)|\s*\(\s*\d+(?:\.\d+)?\s*%\s*acceptance rate[^)]*\)|\s*IF\s*=\s*[\d.]+', '', v, flags=re.I)
        au = (p.get('authors') or '').strip().rstrip(',')
        out.append(f"- {esc(au)}{'' if au.endswith('.') else '.'} \"{esc(t)}\". *{esc(v)}*.")
    out.append('')
for key, label in (('patents', 'PATENTS'), ('projects', 'PROJECTS'), ('news', 'NEWS'), ('awards', 'AWARDS')):
    items = L.get(key) or []
    if items:
        out.append(f'<!--{label}-->')
        for it in items:
            if isinstance(it, str):
                out.append(f'- {esc(it)}'); continue
            parts = [it.get(k) for k in ('date_posted', 'date', 'year') if it.get(k)]
            body = it.get('title') or it.get('name') or it.get('text_posted') or json.dumps({k: v for k, v in it.items() if k not in ('source_url', 'raw_key')}, ensure_ascii=False)
            body = re.sub(r'\s*\[(?:SCIE|SSCI|SCI|A&HCI|AHCI|ESCI|SCOPUS|KCI|Q[1-4])\b[^\]]*\]', '', body, flags=re.I)
            LBL = {'sponsor_posted': '지원', 'period_posted': '기간', 'application_number_posted': '출원번호', 'application_date_posted': '출원일',
                   'registration_number_posted': '등록번호', 'registration_date_posted': '등록일', 'status_posted': '상태', 'role_posted': '역할',
                   'number_posted': '번호', 'year_posted': '연도', 'funder_posted': '지원', 'inventors_posted': '발명자', 'country_posted': '국가', 'partner_posted': '협력 기관', 'amount_posted': '연구비', 'area_posted': '분야', 'program_posted': '사업'}
            extra = [f"{LBL.get(k, k.replace('_posted', ''))} {it[k]}" for k in it if k.endswith('_posted') and k not in ('text_posted', 'date_posted', 'title_posted', 'section_posted') and 'note' not in k and it.get(k)]
            out.append(f"- {(str(parts[0]) + ' · ') if parts else ''}{esc(body)}{(' (' + '; '.join(extra) + ')') if extra else ''}")
        out.append('')
Path(f'{slug}.lists.md').write_text('\n'.join(out) + '\n')
print(slug, 'members', len(M), 'alumni', len(A), 'papers', len(P), {k: len(L.get(k) or []) for k in ('patents', 'projects', 'news', 'awards')})

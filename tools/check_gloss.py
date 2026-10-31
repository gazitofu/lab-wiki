# Check glossary entries against the registered lab pages: every term must be markable in the
# 「무엇을 연구하나」·「주요 연구 주제」 region (same rule as the screen builder), and tips follow the writing rules.
# Usage: python3 check_gloss.py FILE.json [FILE.json ...]   (gloss-G*.json or the merged glossary.json)
import json, re, sys
from pathlib import Path
import markdown
sys.path.insert(0, '/Users/gazitofu/Vault/appdev/Lab-wiki/design')
from glossary_mark import mark

import os
import argparse
from inst import REPO, detect, split_key
parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=Path)
parser.add_argument('files', nargs='*')
args = parser.parse_args()

def wiki(inst):
    if args.repo is not None:
        return args.repo / 'wiki' / inst
    if 'GLOSS_WIKI' in os.environ:
        return Path(os.environ['GLOSS_WIKI'])
    local = Path('wiki') / inst
    return local if local.is_dir() else REPO / 'wiki' / inst
EXTS = ['tables', 'fenced_code', 'sane_lists', 'footnotes']
BANNED = ['처럼', '비슷한', '가장', '혁신', '—', '아주 작', '매우 작']
errors = warns = 0
for f in args.files:
    pages = json.loads(Path(f).read_text(encoding='utf-8'))['pages']
    for slug, entries in sorted(pages.items()):
        institution, page_slug = split_key(slug, detect())
        page = wiki(institution) / f'{page_slug}.md'
        if not page.exists():
            print(f'{f}: {slug}: 오류 문서 없음'); errors += 1; continue
        body = page.read_text(encoding='utf-8')
        out = markdown.Markdown(extensions=EXTS).convert(body)
        _, missing = mark(out, entries)
        for t in missing:
            print(f'{slug}: 오류 본문 범위에 없음(또는 링크·각주·굵은 글씨 경계에 걸림): {t}'); errors += 1
        seen = set()
        for e in entries:
            t, tip = e.get('term', ''), e.get('tip', '')
            if not t or not tip:
                print(f'{slug}: 오류 빈 항목 {e}'); errors += 1; continue
            if t in seen:
                print(f'{slug}: 오류 중복 용어 {t}'); errors += 1
            seen.add(t)
            if re.search(r'\d', tip):
                print(f'{slug}: 경고 풀이에 숫자: {t}: {tip}'); warns += 1
            for w in BANNED:
                if w in tip:
                    print(f'{slug}: 경고 풀이에 「{w}」: {t}: {tip}'); warns += 1
            if len(tip) > 120:
                print(f'{slug}: 경고 풀이 {len(tip)}자: {t}'); warns += 1
        print(f'{slug}: 용어 {len(entries)}')
print(f'오류 {errors} | 경고 {warns}')
sys.exit(1 if errors else 0)

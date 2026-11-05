# Tag evidence table for writers and QA (brief-common §5.10): for each tag on a page, the tags.json definition next to
# the body sentences that cite the same footnotes and the footnote sources, so "does this sentence say the lab studies
# what the definition names?" is judged side by side.
# usage: python3 tag_table.py PAGE.md [PAGE.md ...]   (markdown to stdout; --repo defaults to the Lab-wiki checkout)
import argparse
import json
import re
from pathlib import Path

from inst import REPO


def sentences(lines, fn):
    out = []
    for ln in lines:
        if f'[^{fn}]' not in ln:
            continue
        # split on sentence ends and keep the pieces that carry this footnote
        for s in re.split(r'(?<=[다요음])\.\s+|(?<=\.)\s+(?=[가-힣A-Z])', ln):
            if f'[^{fn}]' in s:
                out.append(re.sub(r'\[\^[^\]]+\]', '', s).strip(' -|'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=REPO)
    ap.add_argument('pages', nargs='+', type=Path)
    a = ap.parse_args()
    vocab = json.loads((a.repo / 'wiki' / 'tags.json').read_text())
    tags = vocab['tags'] if isinstance(vocab['tags'], list) else list(vocab['tags'].values())
    by_name = {t['name_ko']: t for t in tags}
    for page in a.pages:
        text = page.read_text()
        lines = text.splitlines()
        defs = dict(re.findall(r'^\[\^([^\]]+)\]:\s*(.*)$', text, re.M))
        head_end = next((i for i, ln in enumerate(lines) if ln.startswith('## ')), len(lines))
        body = [ln for ln in lines[head_end:] if not ln.startswith('[^')]
        tag_line = next((ln for ln in lines if ln.startswith('- 태그: ')), '')
        print(f'## {page.stem} (tags.json {vocab.get("version")})\n')
        print('| 태그 | definition | 각주 | 본문에서 같은 각주를 단 문장 | 각주 출처 |')
        print('|---|---|---|---|---|')
        for item in tag_line.removeprefix('- 태그: ').split(', ') if tag_line else []:
            name = re.sub(r'\[\^[^\]]+\]', '', item).strip()
            fns = re.findall(r'\[\^([^\]]+)\]', item)
            d = (by_name.get(name) or {}).get('definition', '(어휘에 없음)')
            sent = ' / '.join(dict.fromkeys(s for fn in fns for s in sentences(body, fn))) or '(본문 문장 없음)'
            src = ' / '.join(re.sub(r'\s*<[^>]+>.*$', '', defs.get(fn, '(정의 없음)'))[:120] for fn in fns)
            print('| ' + ' | '.join(x.replace('|', '\\|') for x in (name, d, ', '.join(fns), sent[:600], src)) + ' |')
        print()


if __name__ == '__main__':
    main()

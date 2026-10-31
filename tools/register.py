"""기관별 문서·용어 풀이·README를 잠금 안에서 등록한다. push는 하지 않는다."""
import argparse
import fcntl
import json
from pathlib import Path
import re
import subprocess
import sys
import time

from inst import INSTS, REPO, gloss_key


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inst', required=True, choices=INSTS)
    parser.add_argument('--batch-dir', required=True, type=Path)
    parser.add_argument('--slugs', required=True)
    parser.add_argument('--repo', type=Path, default=REPO)
    parser.add_argument('--lock', type=Path, default=Path('/Users/gazitofu/Library/Application Support/Lab-wiki/register.lock'))
    parser.add_argument('--commit-message')
    args = parser.parse_args()
    slugs = args.slugs.split(',')
    if len(set(slugs)) != len(slugs) or any(not re.fullmatch(r'[\w-]+', s) for s in slugs):
        parser.error('--slugs에는 중복 없는 파일 이름 줄기를 쉼표로 잇는다')
    if any(s.endswith('-sources') for s in slugs):
        parser.error('--slugs에는 근거 페이지 접미사 -sources로 끝나는 이름을 쓸 수 없다')
    repo = args.repo.resolve()

    def git(*cmd, **kwargs):
        return subprocess.run(['git', '-C', str(repo), *cmd], check=True, **kwargs)

    args.lock.parent.mkdir(parents=True, exist_ok=True)
    with args.lock.open('a') as lock:
        deadline = time.monotonic() + 600
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise SystemExit('등록 잠금 대기 600초 초과')
                time.sleep(min(0.1, max(0, deadline - time.monotonic())))
        if git('status', '--porcelain', stdout=subprocess.PIPE, text=True).stdout:
            raise SystemExit('작업 트리가 깨끗하지 않아 등록하지 않음')

        gp = repo / 'wiki/glossary.json'
        original = gp.read_text(encoding='utf-8')
        g = json.loads(original)
        pending = []
        # 모든 랩의 충돌·입력을 먼저 확인해 기존 대상 발견 시 부분 등록을 막는다.
        for slug in slugs:
            folder = args.batch_dir / slug
            for name in (f'{slug}.md', f'{slug}-sources.md'):
                src = folder / INSTS[args.inst]['wiki'] / name
                dst = repo / INSTS[args.inst]['wiki'] / name
                if dst.exists() or dst.is_symlink():
                    raise SystemExit(f'already registered: {dst}')
                pending.append((dst, src.read_bytes()))
            key = gloss_key(args.inst, slug)
            if key in g['pages']:
                raise SystemExit(f'already registered: {key}')
            entries = json.loads((folder / f'{slug}-gloss.json').read_text(encoding='utf-8'))['pages'][slug]
            g['pages'][key] = [{'term': e['term'], 'tip': e['tip']} for e in entries]
        targets = [dst for dst, _ in pending]
        if len(set(targets)) != len(targets):
            raise SystemExit('등록 대상 경로가 중복되어 등록하지 않음')
        g['pages'] = dict(sorted(g['pages'].items()))
        for dst, content in pending:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(content)
        gp.write_text(json.dumps(g, ensure_ascii=False, indent=1) + ('\n' if original.endswith('\n') else ''), encoding='utf-8')
        readme = repo / 'README.md'
        subprocess.run([sys.executable, str(Path(__file__).resolve().with_name('mkreadme.py')),
                        str(readme), '--repo', str(repo)], check=True)
        changed = [str(p.relative_to(repo)) for p in targets] + ['wiki/glossary.json', 'README.md']
        if args.commit_message is not None:
            git('add', '--', *changed)
            git('commit', '--only', '-m', args.commit_message, '--', *changed)
        print('changed files:')
        print('\n'.join(changed))
        print('glossary pages', len(g['pages']))


if __name__ == '__main__':
    main()

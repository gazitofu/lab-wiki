"""기관별 차수 폴더와 RAW 경로를 채운 공용 도구 사본을 만든다."""
import argparse
import datetime
import os
from pathlib import Path
import re
import shutil

from inst import INSTS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inst', required=True, choices=INSTS)
    parser.add_argument('--date', required=True)
    parser.add_argument('--batch', required=True)
    parser.add_argument('--labs', required=True)
    parser.add_argument('--baseline')
    parser.add_argument('--root', type=Path, default=Path('/Users/gazitofu/Vault/appdev/Lab-wiki/collection-staging'))
    args = parser.parse_args()
    if args.inst == 'snu' and not args.baseline:
        parser.error('서울대는 --baseline이 필요하다')
    for date in (args.date, args.baseline):
        if date:
            try:
                if datetime.date.fromisoformat(date).isoformat() != date:
                    raise ValueError(date)
            except ValueError:
                parser.error(f'날짜 형식은 YYYY-MM-DD: {date}')
    labs = args.labs.split(',')
    if (any(not re.fullmatch(r'[\w-]+', value) for value in [args.batch, *labs])
            or len(set(labs)) != len(labs) or any(s in ('common', 'tools') for s in labs)):
        parser.error('차수·랩 이름에는 중복 없는 파일 이름 줄기를 쓴다')
    here = Path(__file__).resolve().parent
    root = args.root.resolve()
    batch = root / args.date / args.batch if args.inst == 'kaist' else root / 'snu' / args.date / args.batch
    if batch.exists() or batch.is_symlink():
        raise SystemExit(f'이미 있는 차수 폴더: {batch}')
    baseline = '2026-10-13' if args.inst == 'kaist' else args.baseline
    raw = (Path('/Users/gazitofu/Library/Application Support/Lab-wiki/collections')
           / args.inst / baseline / f'raw-{args.date}-{args.batch}')
    batch.mkdir(parents=True)
    for dst in [batch / 'common', *(batch / s for s in labs)]:
        shutil.copytree(here / 'common', dst, ignore=shutil.ignore_patterns('__pycache__'))
        fetch = dst / 'fetch.py'
        fetch.write_text(fetch.read_text().replace('__RAW__', str(raw)))
    (batch / 'tools').symlink_to(os.path.relpath(here, batch), target_is_directory=True)
    print(batch)


if __name__ == '__main__':
    main()

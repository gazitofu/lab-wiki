"""기관별 경로와 용어 풀이 키."""
import os
from pathlib import Path

INSTS = {
    'kaist': dict(name='KAIST', wiki='wiki/kaist', strip=('KAIST ',)),
    'snu': dict(name='서울대', wiki='wiki/snu', strip=('서울대학교 ', '서울대 ')),
}
REPO = Path('/Users/gazitofu/Developer/Lab-wiki')


def detect():
    if 'LABWIKI_INST' in os.environ:
        value = os.environ['LABWIKI_INST']
        if value not in INSTS:
            raise SystemExit(f'알 수 없는 기관: {value}')
        return value
    return 'snu' if '/collection-staging/snu/' in str(Path.cwd().resolve()) + '/' else 'kaist'


def gloss_key(inst, slug):
    return slug if inst == 'kaist' else f'{inst}/{slug}'


def split_key(key, default_inst):
    return tuple(key.split('/', 1)) if '/' in key else (default_inst, key)

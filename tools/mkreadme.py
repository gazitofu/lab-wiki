import collections,glob,re,sys
import argparse
from inst import INSTS, REPO
parser = argparse.ArgumentParser()
parser.add_argument('out', nargs='?', default='README.new.md')
parser.add_argument('--repo', type=type(REPO), default=REPO)
args = parser.parse_args()
OUT=args.out
def load(inst):
    docs={}
    for f in sorted((args.repo / INSTS[inst]['wiki']).glob('*.md')):
        if f.name.endswith('-sources.md'): continue
        L=f.read_text().splitlines()
        slug=f.stem
        title=L[0][2:].strip(); dept,prof=L[2].strip('*').split(' · ',1)
        q=next(l for l in L if l.startswith('> '))[2:]
        q=re.sub(r'\[\^[^\]]+\]','',q).strip()
        first=re.split(r'(?<=다\.)\s',q)[0]
        if inst == 'kaist':
            dept=dept.replace('KAIST ','')
        else:
            dept=', '.join(part.removeprefix('서울대학교 ').removeprefix('서울대 ') for part in dept.split(', '))
        docs[slug]=(title,dept,prof,first)
    return docs

def table(inst, docs):
    G=collections.defaultdict(list)
    for slug,(t,d,p,s) in docs.items():
        G[d.split('·' if inst == 'kaist' else ', ')[0]].append((t,slug,p,s,d))
    rows=[]
    for d in sorted(G,key=lambda k:(-len(G[k]),k)):
        rows += [f'### {d} ({len(G[d])})','','| 연구실 | 교수 | 한 줄 요약 |','|---|---|---|']
        for t,slug,p,s,full in sorted(G[d]):
            extra='' if full==d else f' ({full})'
            rows.append(f'| [{t}]({INSTS[inst]["wiki"]}/{slug}.md) | {p}{extra} | {s} |')
        rows.append('')
    return rows

docs=load('kaist')
snu=load('snu')
out=['# Lab wiki','',
'KAIST 연구실을 한 곳에서 찾아보는 위키다. 연구실마다 한 문서에 무엇을 연구하는지, 대표 논문과 그 내용을 쉽게 풀어 쓴 설명, 교수와 전문 분야, 구성원·졸업생·논문·과제·특허·소식 목록을 담았다.','',
'## 문서 읽는 법','',
'- 문서 맨 위 인용문이 연구실을 한두 문장으로 요약한다. 「무엇을 연구하나」는 연구 갈래별로 대표 논문을 이어 설명한다.',
'- 「대표 논문」 표의 "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 쓴 풀이다.',
'- 문서 머리의 「대분야」는 연구실이 속한 큰 분야 1–2개이고, 「태그」는 연구 주제를 미리 정한 주제 이름 목록에서 골라 적은 검색용 꼬리표다. 태그마다 근거가 된 본문 각주를 달았다. 태그의 뜻과 다른 표기는 [wiki/tags.json](wiki/tags.json)에, 트렌드 검색어와 그에 맞는 태그 묶음은 [wiki/trend-queries.json](wiki/trend-queries.json)에 있다.',
'- 「무엇을 연구하나」·「주요 연구 주제」에 나오는 어려운 용어의 짧은 풀이는 [wiki/glossary.json](wiki/glossary.json)에 연구실별로 있다. 위키 화면에서는 점선 밑줄이 그어진 용어에 마우스를 올리면 풀이가 뜬다.',
'- 본문의 각주는 문장마다 근거가 된 연구실 누리집, 학과 페이지, 논문 서지를 가리킨다. 각 문서에 딸린 「근거」 페이지에 읽은 자료, 이름·직급 표기 차이, 대표 논문을 고른 이유, 확인한 범위를 적었다.',
'- 구성원·졸업생·논문·과제·소식 목록은 연구실이 게시한 내용을 옮긴 것이다. 기준일은 각 문서의 구성원 절과 각주에 있다. 최근 논문 목록은 2021년 이후 논문이다.','',
f'## KAIST 연구실 ({len(docs)}곳)','']
out+=table('kaist',docs)
if snu:
    out += [f'## 서울대 연구실 ({len(snu)}곳)',''] + table('snu',snu)
out+=['## 범위와 기준','',
'- 2026년 10월 19일부터 각 연구실 누리집, KAIST 학과 페이지, 논문 서지를 읽어 썼다. 연구실 누리집이 바뀌면 내용이 달라질 수 있다.',
'- 연구실이 공개한 기관 이메일만 옮기고, 개인 휴대전화, 사진, 사생활에 관한 소식은 싣지 않는다.',
'- 누리집에 이메일 무단 수집 거부를 밝힌 연구실은 이메일을 싣지 않는다.','- 누리집이 기호로 풀어 쓴(at, dot 등) 이메일은 옮기지 않는다.','- 학술지 영향력 지수, 학술지 등급, 학회 채택률은 싣지 않는다.','']
if snu:
    out[2]=out[2].replace('KAIST 연구실을', 'KAIST·서울대 연구실을', 1)
    i=out.index('## 범위와 기준')+2
    out[i]='- KAIST는 2026년 10월 19일부터, 서울대는 2026년 10월 22일부터 각 연구실 누리집, 학과 페이지, 논문 서지를 읽어 썼다. 연구실 누리집이 바뀌면 내용이 달라질 수 있다.'
open(OUT,'w').write('\n'.join(out))
print(len(docs)); print('\n'.join(out[12:22]))

# 전산역학 및 구조시스템 연구실 (CMSS Laboratory, Computational Mechanics and Structural Systems)

**KAIST 기계공학과 · 이필승 교수**

- 분야: 유한요소법, 유체–구조 상호작용, 해양 구조물과 해양 원전 같은 구조 시스템, 기계학습 기반 구조 해석과 이상 진단, 충격·폭발 해석
- 대분야: 기계·로봇·제조, 건설·도시·인프라
- 태그: 유체역학·유동[^research][^p5][^p6], 과학·공학 AI[^research][^p3], 고장 진단·수명 예측[^research][^p4], 원자로·원자력 시스템[^research][^p7][^p8], 전산역학·수치 해석[^about], 충격·내충돌·폭발 방호[^p7], 고체역학·소성[^research]
- 홈페이지: <http://cmss.kaist.ac.kr/>
- 근거와 출처: [전산역학 및 구조시스템 연구실 근거 페이지](cmss-sources.md)

> 구조물과 유체가 받는 힘과 그에 따른 움직임을 수학 모델로 나타내고, 유한요소법을 바탕으로 효율적인 수치 해석 방법을 만드는 연구실이다. 이 해석 기술을 바탕으로 플렉서블 디스플레이, 해양 원전 같은 새로운 형태의 구조 시스템을 개발한다.[^about]

## 무엇을 연구하나

연구실 소개 글은 각종 구조역학·유체역학 문제에 대해 수학 모델을 연구하고, 유한요소법(물체를 작은 조각으로 나눠 각 조각의 방정식을 이어 풀어 전체의 변형과 힘을 계산하는 수치 해석 방법)에 바탕을 둔 효율적인 수치 해석 기법을 개발한다고 적는다. 연구실은 이것이 기계 시스템 디지털 트윈의 근간이라고 적고, 혁신적인 아이디어를 바탕으로 플렉서블 디스플레이, 해양 원전 같은 새로운 형태의 구조 시스템을 개발해 관련 산업에 비전을 제시한다고 소개한다.[^about]

연구 페이지는 여러 물리·역학 문제를 풀기 위한 효과적인 수학 모델과 수치 계산 절차를 만드는 것을 관심사로 들고, 구조 문제와 유체–구조 상호작용(흐르는 유체와 그 흐름에 밀려 움직이거나 변형하는 구조물이 서로 영향을 주고받는 현상) 문제를 해석하는 수치 방법을 연구한다고 적는다. 주요 연구 영역은 유한요소법, 유체–구조 상호작용, 구조 시스템, 인공지능 기반 해석, 동물 원격 제어 시스템의 다섯 가지다.[^research]

기계공학과 교수 소개는 교수의 연구분야를 Computational Mechanics, Structural Systems, Experimental Biology로 적는다.[^meprof] 학과 연구분야 안내 두 항목은 이 연구실의 연구주제로 Structural Systems, Fluid-Structure Interaction, Computational Mechanics, Experimental Biology를, 주요 응용 산업으로 중공업·조선해양, 자동차·항공·디스플레이, 해양국방을 든다.[^meres]

## 주요 연구 주제

### 1. 유한요소 기술: 고체·구조 요소 개발

연구실은 여러 물리·역학 문제를 푸는 데 쓰는 유한요소 기술을 연구하고 고체 요소와 구조 요소(얇은 판과 껍질 모양 구조를 나타내는 셸 요소, 가늘고 긴 부재를 나타내는 보 요소)를 개발한다. 연구 페이지는 연속체 역학 기반 셸·보 요소, 변형률 평활화 요소 방법(요소 안의 변형률을 주변 값과 고르게 다듬어 계산 정확도를 높이는 방법), 강화 유한요소법, 평활화 MITC3+ 셸 요소, 층을 이룬 보 요소를 그림으로 소개한다.[^research]

최근 논문은 변형률 평활화를 다각형 요소로 넓힌 연구(대표 논문 1)와, 변형률 평활화 3절점 삼각형 요소에서 체적 잠김을 덜어 낸 연구(대표 논문 2)가 있다.[^p1][^p2] 논문 목록에는 단순화한 MITC4+ 셸 요소, 2차원 MITC4 요소의 개선, 층 사이 미끄럼을 고려한 다층 셸 요소, 위상장 모델(서로 다른 상태 사이의 경계를 연속적으로 변하는 값으로 나타내는 계산 모델)의 계산 효율 개선 연구도 있다.[^pubs] 연구실 소식은 졸업생 두 사람이 개발한 셸 유한요소가 상용 유한요소 해석 소프트웨어 ADINA에 들어갔다고 2020년 12월에 알렸다.[^news]

### 2. 유체–구조 상호작용: 부유 구조물과 입자법

연구실은 변형하는 부유식 구조물(물에 떠 있는 구조물)의 유체역학적 해석과 유체–구조 상호작용 문제를 푸는 수치 방법을 유한요소법, 경계요소법, 입자 완화 유체동역학(SPH)으로 개발한다. 연구 페이지는 유탄성 해석과 유탄소성 해석, SPH 계산을 그림으로 소개한다.[^research]

최근 논문은 SPH에서 압력장 계산의 정확도를 높이는 밀도 보정 방법(대표 논문 5)과, 경계 입자 없이 벽 경계 조건을 직접 부여하는 방법(대표 논문 6)이 있다.[^p5][^p6] 논문 목록에는 유탄성 해석에서 응력 응답을 직접 계산하는 방법, 유연한 부유 구조물의 정수압·동수압 통합 해석 연구도 있다.[^pubs]

### 3. 구조 시스템: 해양 구조물과 원자력 시설 방호

연구실은 고체·구조역학의 기초를 연구하고, 해양 원전, 부유식 풍력발전기, 선박 같은 해양 구조물에 초점을 둔 새로운 구조 시스템을 개발한다. 연구 페이지는 중력식 해양 원전, 부유식 원전과 부유식 풍력발전기를 그림으로 소개한다.[^research]

최근 논문은 원자력 시설 안에서 일어나는 폭발의 하중을 계산 모델로 다룬 연구(대표 논문 7)와, 원자력발전소 로드블록에 차량이 부딪히는 상황을 시뮬레이션한 연구(대표 논문 8)가 있다.[^p7][^p8] 논문 목록에는 원자력 시설에 세우는 차량 돌진 방지 볼라드의 성능 등급 기준, 하이퍼튜브 차량과 가이드웨이의 3차원 동적 상호작용, 실험실 규모 재킷 구조물에서 실시간 변형률 분포를 추정하는 가상 센싱(직접 재지 않은 위치의 값을 측정값과 모델로 추정하는 방법), 큰 선박 블록에 걸린 하중을 적은 센서로 역추정하는 연구도 있다.[^pubs]

### 4. 인공지능 기반 해석과 이상 진단

연구실은 기계학습으로 구조 시스템의 선형·비선형 해석을 위한 데이터 기반 유한요소 모델을 연구한다. 연구 페이지는 기계학습을 쓴 큰 변형 해석과 기계 시스템의 손상 탐지·진단을 그림으로 소개한다.[^research]

최근 논문은 딥러닝으로 요소의 굽힘 방향을 찾아 반복할수록 해가 정확해지는 자기 갱신 유한요소(대표 논문 3)와, 여러 센서 자료로 양수 발전소의 이상을 탐지하고 진단하는 시스템(대표 논문 4)이 있다.[^p3][^p4] 논문 목록에는 한 대의 카메라로 찍은 바다 영상에서 딥러닝으로 파고를 분류하는 연구도 있다.[^pubs]

### 5. 동물 원격 제어 시스템

연구실은 몸에 붙인 장치와 특수한 자극으로 살아 있는 동물을 원격으로 이끄는 시스템을 개발하고, 심부 뇌 자극(뇌 깊은 곳에 전기 자극을 주는 방법) 기술도 개발한다. 연구 페이지는 거북과 생쥐의 원격 유도, 대상을 탐하는 뇌 회로를 이용한 생쥐 조종 시스템, 무선 심부 뇌 자극을 그림으로 소개한다.[^research]

## 대표 논문

이필승 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 연구 갈래마다 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [Strain-smoothed polygonal finite elements](https://doi.org/10.12989/sem.2023.86.3.311) · Structural Engineering and Mechanics | 변형률 평활화 요소(SSE) 방법은 최근 삼각형·사각형 유한요소에 쓰여 요소의 성능을 높였다. 다각형 요소는 격자(계산 영역을 나눈 조각들의 배열)를 유연하게 다룰 수 있어 쓰임이 많지만, 실제 공학에 효과적으로 쓰려면 더 개발해야 한다. 이 연구는 구간 선형 형상 함수(요소 안의 값을 꼭짓점 값으로 나타내는 함수)를 쓰고, 다각형 요소를 삼각형으로 나눠 SSE 방법을 적용해 요소 안에 평활화된 변형률 장을 만들었다. 이 요소는 기본 시험을 통과했고 여러 수치 문제에서 수렴 거동이 나아졌다.[^p1] | 1저자 H. Jung, 마지막·교신 저자 이필승 (3명) |
| 2 | 2025 | [Treatment of volumetric locking in the strain-smoothed 3-node triangular finite element](https://doi.org/10.12989/sem.2025.96.3.225) · Structural Engineering and Mechanics | 최근 개발된 변형률 평활화 3절점 삼각형 요소는 성능이 좋지만, 푸아송 비(재료를 한 방향으로 늘일 때 옆 방향으로 줄어드는 비율)가 0.5에 가까워지면 체적 잠김 때문에 예측 능력이 떨어진다. 이 연구는 부피 변형률에만 절점별 평활화를 적용하고, 모양을 바꾸는 편차 변형률에는 원래 요소의 정식화를 그대로 두었다. 제안한 요소는 기본 시험을 통과하고 체적 잠김을 덜었으며, 여러 수치 문제로 성능을 보였다.[^p2] | 1저자 H. Jung, 마지막 저자 이필승 (3명) |
| 3 | 2022 | [Self-updated four-node finite element using deep learning](https://doi.org/10.1007/s00466-021-02081-7) · Computational Mechanics | 자기 갱신 유한요소(SUFE)라는 새 개념을 내놓았다. 격자를 더 잘게 나누지 않고 반복 계산으로 해의 정확도를 높이는 요소다. 4절점 요소에 모드 기반 정식화를 만들고 굽힘 모드에 가정 모드 변형률을 썼으며, 전단 잠김을 줄이도록 주어진 요소 변형에 대한 최적 굽힘 방향을 딥러닝으로 찾는다. 요소는 패치 시험과 영 에너지 모드 시험(요소가 갖춰야 할 기본 성질을 확인하는 표준 시험)을 통과했고, 반복할수록 해가 정확해져 몇 번의 반복으로 크게 정확한 해를 얻었다. 격자가 거칠고 심하게 일그러졌을 때 특히 효과적이다.[^p3] | 1저자 J. Jung, 마지막·교신 저자 이필승 (3명) |
| 4 | 2023 | [Multi-sensor data-based anomaly detection and diagnosis of a pumped storage hydropower plant](https://doi.org/10.12989/sem.2023.88.6.569) · Structural Engineering and Mechanics | 양수 발전소(아래 저수지의 물을 위 저수지로 퍼 올려 두었다가 흘려보내며 발전하는 발전소)의 이상을 탐지하고 진단하는 시스템을 소개한다. 온도·진동·전력 등을 재는 여러 센서의 자료를 모아 운전 모드(펌프 운전, 터빈 운전)별로 나누고, 바깥 환경의 영향을 없애도록 정규화했다. 정상 자료의 분포를 학습하는 다변량 정규 분포 분석으로 이상을 탐지하고 그 유형을 진단한다. 실제 양수 발전소의 감시 자료로 타당성을 평가했고, 고쳐 쓰면 다른 발전소의 상태 감시 시스템에도 쓸 수 있다.[^p4] | 1저자 S. Shin, 마지막 저자 이필승 (교신 표시 2명 중 1명, 4명) |
| 5 | 2025 | [A novel density correction method for improved prediction of pressure fields in SPH](https://doi.org/10.1002/nme.70116) · International Journal for Numerical Methods in Engineering | SPH는 수십 년 동안 연구됐지만 압력장을 정확히 계산하기 어려워 실제 공학에 널리 쓰이지 못했다. 이 연구는 고체 경계 근처와 유체 안쪽 모두에서 정수압 분포의 정확도를 높이는 새 밀도 보정 방법을 만들었다. 보간 격자와 보충 입자라는 두 개념으로 밀도 분포를 다듬으며, 구현이 간단하다. 고체 경계 가까운 고압 영역의 정수압 장을 잘 계산하고, 동수압 장의 비물리적 진동과 튀는 값을 억누르며, 장시간 계산에서 생기는 의도치 않은 수치 소산을 줄인다. 보정 간격을 정하는 데 융통성이 크고 여러 고체 경계 처리 방법과 잘 맞으며, 여러 수치 시험과 다른 방법과의 비교로 성능을 확인했다.[^p5] | 1저자 Y. Jeong, 마지막·교신 저자 이필승 (2명) |
| 6 | 2021 | [Direct imposition of the wall boundary condition for simulating free surface flows in SPH](https://doi.org/10.12989/sem.2021.78.4.497) · Structural Engineering and Mechanics | SPH에서 벽 경계를 다루는 새 방법으로 자유 표면 흐름(액체 표면이 벽에 갇히지 않고 움직이는 흐름)을 효과적으로 계산한다. 보통은 벽에 경계 입자를 깔아 경계를 나타내지만, 이 방법은 질량·운동량 보존 방정식에 경계 절단 항을 더해 벽 경계 조건을 직접 부여하므로 경계 입자를 쓰지 않는다. 그 결과 경계 조건이 정확히 부여되고 경계 모델링이 단순해지며, 안정성을 잃지 않고 계산이 효율적이 된다. 댐 붕괴, 쐐기가 있는 댐 붕괴, 슬로싱(용기 안 액체의 출렁임), 경사 바닥, 교차 레버 회전, 맥동 탱크, 유연한 칸막이가 있는 슬로싱 예제로 성능을 보였고, 실험·해석해·경계 입자법 결과와 비교했다.[^p6] | 1저자 H.-J. Park, 마지막·교신 저자 이필승 (3명) |
| 7 | 2026 | [TNT equivalency of MegaMEX and CONWEP-based modeling of fully vented internal explosions in nuclear facilities](https://doi.org/10.12989/sem.2026.97.3.393) · Structural Engineering and Mechanics | 상용 고폭약 MegaMEX의 TNT 당량(같은 폭발 효과를 내는 TNT의 양으로 나타낸 값)을 추정하고, 원자력 시설에서 완전 개방형 내부 폭발이 일어날 때 CONWEP 기반 폭발 모델을 쓸 수 있는지 평가했다. 경험적 폭발 하중 모델은 TNT 당량에 기대지만, TNT가 아닌 상용 폭약이거나 시설 안에서 폭발이 일어나면 불확실성이 생긴다. 열 기반과 폭속(폭발 반응이 퍼져 나가는 속도) 기반 환산 방법으로 MegaMEX의 TNT 당량을 추정하고, LS-DYNA의 CONWEP 기반 LBE 카드로 계산한 결과를 완전 개방형 내부 폭발 시험에서 잰 최대 과압과 양의 위상 충격량과 비교했다. 원래 개방된 공간의 폭발용으로 만든 LBE 카드도 이 조건에서 합리적인 정확도를 보였고, 환산 방법 가운데서는 폭속 기반 방법이 실험값과 가장 가깝게 맞았다.[^p7] | 1저자 S. Lee, 마지막·교신 저자 이필승 (3명) |
| 8 | 2023 | [Vehicle collision simulation for roadblocks in nuclear power plants using LS-DYNA](https://doi.org/10.7734/coseik.2023.36.2.113) · Journal of the Computational Structural Engineering Institute of Korea | 차량 강습 위협이 원자력발전소의 설계 기준에 들어가면서 차량 방벽의 성능을 평가할 필요가 커졌다. 차량 방벽은 보통 충돌 실험으로 성능을 인증받지만 국내에는 시험 시설이 없어 시뮬레이션으로만 검증할 수 있다. 충돌 해석에 특화된 프로그램 LS-DYNA로 로드블록에서 가장 핵심인 차량 차단막 모듈의 유한요소 모델을 만들어 차량 충돌을 계산했고, 계산 결과를 NCHRP 179의 차량 안전 시설 충돌 시뮬레이션 검증 기준으로 확인했다.[^p8] | 1저자 S. Lee, 마지막·교신 저자 이필승 (3명) |

## 교수와 전문 분야

이필승 교수는 KAIST 기계공학과 교수이고, 연구실 PEOPLE 페이지는 해양시스템공학 대학원(Graduate School of Ocean Systems Engineering)도 함께 적는다.[^people][^meprof] 기계공학과 교수 소개는 연구분야를 Computational Mechanics, Structural Systems, Experimental Biology로, 최종학위를 Ph.D., MIT (2004)로 적는다.[^meprof]

PEOPLE 페이지에 따르면 교수는 한양대학교 토목공학 학사(1997), KAIST 토목및환경공학 석사(1999), Massachusetts Institute of Technology 토목및환경공학 박사(2004)를 받았다. 한국건설기술연구원 구조시스템그룹 연구원(1999–2000), MIT 기계공학 박사후연구원(2003–2004), McGill University 토목공학·응용역학 박사후연구원(2004–2005), 삼성중공업 해양콘크리트구조팀 매니저(2005–2009)를 거쳐, KAIST 해양시스템공학 부교수(2009–2015), 기계공학과 부교수(2015–2019), 기계공학과 교수(2019–)다. 강의는 유한요소법을 통한 공학 설계, 유체–구조 상호작용 개론, 구조물의 유한요소 해석, 고급 고체·구조 해석이다.[^people] 연구실 소식에 따르면 교수는 2023년 KAIST 리서치데이 연구상을 받았다.[^rd]

교수의 2021년 이전 논문은 MITC3+·MITC4+ 셸 요소와 강화 고체 요소 같은 유한요소 개발, 큰 구조물의 계산을 줄이는 부분구조·동적 축약 방법, 부유 구조물의 유탄성 해석, 해양 원전 설계 개념, 동물 원격 유도를 다룬다.[^pubs] 논문으로 보면 최근의 전문 분야는 변형률 평활화 요소를 중심으로 한 유한요소 개발(대표 논문 1, 2), 딥러닝과 센서 자료를 쓰는 해석·진단(대표 논문 3, 4), 입자 완화 유체동역학 계산 방법(대표 논문 5, 6), 원자력 시설의 폭발·충돌 방호 해석(대표 논문 7, 8)이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

학과 연구분야 안내는 이 연구실 연구의 주요 응용 산업으로 중공업·조선해양, 자동차·항공·디스플레이, 조선해양·해양국방을 든다.[^meres] 연구 페이지의 과제 목록에는 조선·해양 기업(한국조선해양, 삼성중공업, 현대중공업, 대우조선해양), 한국철도기술연구원(하이퍼튜브), 국방과학연구소(무인잠수정 진·회수 도킹), 한국원자력안전재단(원자력시설 물리적 방벽), 풍산 방산기술연구원(화포용 추진제의 강내탄도 예측)과의 과제가 있다.[^research] 2021–2022년 특허에는 플렉서블 디스플레이 주름 방지 장치, 롤러블 디스플레이 장치, 기계학습 기반 펌프수차 고장 진단 방법과 시스템이 있다.[^pubs] 대표 논문으로는 양수 발전소의 상태 감시(대표 논문 4), 원자력 시설의 내부 폭발 하중 평가(대표 논문 7), 원자력발전소 차량 방벽의 성능 검증(대표 논문 8)이 있다.[^p4][^p7][^p8]

## 구성원

누리집 PEOPLE 페이지 STUDENTS 칸의 15명이다. 누리집은 학생마다 이름, 국문 이름, 연구실에 들어온 해, 이전 학위, 관심 주제를 적고 과정(석사·박사)은 따로 적지 않는다. 「시작」은 들어온 해, 「연구 주제」는 관심 주제(Interest) 줄이다. 이메일은 적혀 있지 않다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Yoon Sung Jeong (정윤성) | 2023 | SPH (Smoothed Particle Hydrodynamics) | 2, 5 |
| Sanghoon Lee (이상훈) | 2023 |  |  |
| Jihoon Lee (이지훈) | 2023 |  |  |
| Dongho Cho (조동호) | 2023 |  |  |
| Hyeokwon Kim (김혁원) | 2024 | Virtual sensing for offshore platforms |  |
| Gyeongeun Bong (봉경은) (Lab Representative) | 2024 | Projection-Based Stiffness Reduction |  |
| Youra Jun (전유라) | 2024 | Optomechanical analysis with FEM |  |
| Yechan Kim (김예찬) | 2025 | Robust nonlinear FEM solvers |  |
| Kiseong Byun (변기성) | 2025 |  |  |
| Dongju Lee (이동주) | 2025 | Interior/Exterior ballistics of guns |  |
| Jeonghwan Yeon (연정환) | 2025 | FEM element development and Impact analysis |  |
| Dukhwan Kim (김덕환) | 2026 |  |  |
| Junhyeok Choe (최준혁) | 2026 | SPH (Smoothed Particle Hydrodynamics) |  |
| Daewon Kim (김대원) | 2026 | Virtual sensing for robotic systems |  |
| Sung Jooyeon (성주연) | 2026 |  |  |

## 졸업생

누리집 ALUMNI 페이지의 49명이다. 괄호 안 연도는 누리집이 이름 옆에 적은 연구실 재적 기간이다. 학위 칸은 각 카드의 맨 위 학위 줄 그대로이며, 다른 학교의 학위가 맨 위에 적힌 카드도 있다(Ho-Soo Kim, Seong-Pil Cho, Ki-Tae Kim). 진로 칸은 카드의 직장·직위 줄이며, 그 줄이 없는 카드는 비워 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Piotr Krzysztof Chrustowski (표트르) | M.S. KAIST, Mechanical Eng. (2025–2026) |  |
| Jungro Kim (김정로) | M.S. KAIST, Mechanical Eng. (2024–2026) |  |
| SeungGyu Lee (이승규) | Ph.D. KAIST, Mechanical Eng. (2022–2025) | Researcher, ADD (Agency for Defense Development) |
| SoJin Shin (신소진) | Ph.D. KAIST, Mechanical Eng. (2017–2025) | Researcher, KFE (Korea Institute of Fusion Energy) |
| Seunghwan Park (박승환) | Ph.D. KAIST, Mechanical Eng. (2019–2025) | Researcher, KAERI (Korea Atomic Energy Research Institute) |
| Jaehyun Sung (성재현) | M.S. KAIST, Mechanical Eng. (2023–2024) | Researcher, KSOE (Korea Shipbuilding & Offshore Engineering) |
| Seungbo Lee (이승보) | Ph.D. KAIST, Mechanical Eng. (2019–2024) | Assistant Professor, Pusan National University |
| Hoontae Jung (정훈태) | Ph.D. KAIST, Mechanical Eng. (2015–2024) | Researcher, KSOE (Korea Shipbuilding & Offshore Engineering) |
| Moonsu Park (박문수) | Ph.D. KAIST, Mechanical Eng. (2018–2023) | Researcher, KAERI (Korea Atomic Energy Research Institute) |
| Ho-Soo Kim (김호수) | M.S. Jeonbuk National University, Mechanical Eng. (2014–2023) | Researcher, ADD (Agency for Defense Development) |
| Junhan Bae (배준한) | M.S. KAIST, Mechanical Eng. (2021–2023) | Researcher, Samsung Electronics |
| HyungGyu Choi (최형규) | Ph.D. KAIST, Mechanical Eng. (2017–2023) | Researcher, ADD (Agency for Defense Development) |
| Gihwan Kim (김기환) | Ph.D. KAIST, Mechanical Eng. (2016–2023) | Assistant Professor, Kumoh National Institute of Technology |
| Donghyeon Yoon (윤동현) | M.S. KAIST, Mechanical Eng. (2020–2022) | Researcher, ADD (Agency for Defense Development) |
| Yun-Ho Kim (김윤호) | Ph.D. KAIST, Mechanical Eng. (2015–2023) | Researcher, KRISO (Korea Research Institute of Ships and Ocean Engineering) |
| Daehyun Yoon (윤대현) | M.S. KAIST, Mechanical Eng. (2020–2022) | Researcher, Samsung Electronics |
| Cheolgyu Hyun (현철규) | Ph.D. KAIST, Mechanical Eng. (2016–2022) | Researcher, ANSYS |
| Dong-Hwa Lee (이동화) | Ph.D. KAIST, Mechanical Eng. (2014–2022) | Researcher, KAERI (Korea Atomic Energy Research Institute) |
| HyungJun Park (박형준) | Ph.D. KAIST, Mechanical Eng. (2015–2021) | CTO, LG Chem Ltd. |
| Hyun-Duk Seo (서현덕) | Ph.D. KAIST, Mechanical Eng. (2014–2021) | Assistant Professor, Korea Maritime and Ocean University |
| Juneho Lee (이준호) | M.S. KAIST, Mechanical Eng. (2019–2021) | Researcher, Hyundai motor company |
| Jinhwan Lee (이진환) | M.S. KAIST, Mechanical Eng. (2019–2021) | Researcher, Samsung Electronics |
| JaeHo Jung (정재호) | Ph.D. KAIST, Mechanical Eng. (2017–2021) | Assistant Professor, Chungbuk National University |
| JiIn Kim (김지인) | M.S. KAIST, Mechanical Eng. (2018–2020) |  |
| Chaemin Lee (이채민) | Ph.D. KAIST, Mechanical Eng. (2015–2020) | Assistant Professor, Chungbuk National University |
| Hyo-Jin Kim (김효진) | Ph.D. KAIST, Mechanical Eng. (2013–2020) | Postdoctoral Researcher, KAIST Innocore PRISM-AI center |
| Min-han Oh (오민한) | Ph.D. KAIST, Mechanical Eng. (2013–2020) | Senior Researcher, KSOE (Korea Shipbuilding & Offshore Engineering) |
| San Kim (김산) | Ph.D. KAIST, Mechanical Eng. (2013–2019) | Assistant Professor, Gyeongsang National University |
| Jeong-Ho Kim (김정호) | Ph.D. KAIST, Mechanical Eng. (2012–2018) | Researcher, KINS (Korea Institute of Nuclear Safety) |
| Yeongbin Ko (고영빈) | Ph.D. KAIST, Mechanical Eng. (2011–2017) | Researcher, ADINA R&D, Inc. |
| Seung-Hwan Boo (부승환) | Ph.D. KAIST, Mechanical Eng. (2013–2017) | Associate Professor, Korea Maritime and Ocean University |
| Dae-Gun Kim (김대건) | Ph.D. KAIST, Mechanical Eng. (2011–2017) | Research Professor, KAIST and CEO, ACTNOVA |
| Sung-Yun Kim (김성윤) | Ph.D. KAIST, Mechanical Eng. (2011–2017) | Senior Researcher, LS Cable & System |
| Joo-Seong Yoon (윤주성) | Ph.D. KAIST, Mechanical Eng. (2010–2017) | Researcher, KAERI (Korea Atomic Energy Research Institute) |
| Jae-Min Kim (김재민) | M.S. KAIST, Ocean Systems Eng. (2014–2016) | Assistant Professor, Changwon National University |
| Cheol-Hu Kim (김철후) | Ph.D. KAIST, Mechanical Eng. (2010–2016) | Researcher, KIMM (Korea Institute of Machinery and Materials) |
| Kang-Heon Lee (이강헌) | Ph.D. KAIST, Mechanical Eng. (2010–2016) | Researcher, KAERI (Korea Atomic Energy Research Institute) |
| Sung-Ho Kim (김성호) | M.S. KAIST, Ocean Systems Eng. (2013–2015) | LT CDR, Engineering Duty Officer for Shipbuilding, ROKN HQ (Republic of Korea Navy Headquarter) |
| Youngyu Lee (이윤규) | Ph.D. KAIST, Ocean Systems Eng. (2009–2015) | Researcher, ADD (Agency for Defense Development) |
| Hyeong-Min Jeon (전형민) | Ph.D. KAIST, Ocean Systems Eng. (2012–2015) | Associate Professor, Jeonbuk National University |
| Kyungho Yoon (윤경호) | Ph.D. KAIST, Ocean Systems Eng. (2010–2015) | Assistant Professor, Yonsei University |
| Seong-Pil Cho (조성필) | Ph.D. NTNU (Norwegian University of Science and Technology) (2011–2014) | Assistant Professor, Korea Aerospace University |
| Ki-Tae Kim (김기태) | Ph.D. Massachusetts Institute of Technology, Mechanical Eng. (2009–2014) | Researcher, LAM Reasearch |
| Zhang Bilin (장삐린) | M.S. KAIST, Ocean Systems Eng. (2012–2014) | Researcher, HHI (Hyundai Heavy Industries) |
| Jin-Gyun Kim (김진균) | Ph.D. KAIST, Ocean Systems Eng. (2010–2014) | Associate Professor, Kyung Hee University |
| Byoung-Do Lee (이병도) | M.S. KAIST, Ocean Systems Eng. (2011–2013) | Researcher, STX Offshore & Shipbuilding |
| Ki-Hwan Lee (이기환) | M.S. KAIST, Ocean Systems Eng. (2010–2012) | Researcher, KSOE (Korea Shipbuilding & Offshore Engineering) |
| Randi Gusto Jiwinangun (란디 구스토) | M.S. KAIST, Ocean Systems Eng. (2010–2012) |  |
| Jae-Seok Ma (마재석) | M.S. KAIST, Ocean Systems Eng. (2009–2011) | Researcher, KIMST (Korea Institute of Marine Science & Technology Promotion) |

## 최근 논문 목록 (2021–2026)

누리집 PUBLICATIONS 페이지 PAPERS 목록의 2021–2026년 연도 구역 30편(학술지 논문)이다. 저자 표기, 제목, 학술지와 권·쪽·발행 월은 누리집 그대로이고, 이름 뒤 *는 누리집이 밑줄로 표시한 교신저자다. 2021년 구역에는 2021년 10월 전(1·4·5월)에 나온 논문 3편도 들어 있다.[^pubs]

**2026**

- Jeong WH, Kim YC, Yeon JH, Lee PS\*. Performance Rating Standards for Anti-Ram Bollards in Nuclear Facilities based on LS-DYNA Analysis, Computational Structural Engineering Institute of Korea, 39(4), 211~218, Aug 2026.
- Yoon DH, Kim HJ\*, Lee PS. Sparse-sensor inverse load estimation of large-scale ship blocks using process-informed POD basis, Ocean Engineering, 363, 126664, Aug 2026.
- Lee SG, Lee S, Lee PS\*. TNT equivalency of MegaMEX and CONWEP-based modeling of fully vented internal explosions in nuclear facilities, Structural Engineering and Mechanics, 97, 393-416, Feb 2026.
- Park S, Jung J, Lee PS\*. Towards improving the self-updated four-node finite element, Computers & Structures, 321, 108014, Jan 2026.

**2025**

- Jung H, Jeong Y, Lee PS. Treatment of volumetric locking in the strain-smoothed 3-node triangular finite element, Structural Engineering and Mechanics, 96, 225-237, Oct 2025.
- Jeong Y, Lee PS\*. A novel density correction method for improved prediction of pressure fields in SPH, International Journal of Numerical Methods in Engineering, Volume 126, Issue 17, Sep 2025.
- Lee SG, Shim J, Lee PS. Self-restoring energy dissipation mechanism via a contact-driven buckling mode transition, International Journal of Mechanical Sciences, 303, 110610, Oct 2025.
- Lee S, Lee PS. Strain sensor placement method considering operational loads for virtual sensing of structural deformation, Computers & Structures, 315, 107763, May 2025.
- Park S, Lee J, Lee PS\*. Multi-layered shell finite element with interlayer slips, Computers & Structures, 310, 107662, Apr 2025.

**2024**

- Park S, Baek SM, Jung HJ, Lee PS, Kim MC. Analysis of 3D dynamic interaction between Hypertube Express (HTX) and its guideway, Structural Engineering and Mechanics, 92, 365-380, Nov 2024.
- Park M, Lee S, Kim KT, Lee PS\*. Direct calculation of stress RAOs in hydroelastic analysis, Ocean Engineering, 312, 118894, Aug 2024.
- Lee S, Park M, Oh MH, Lee PS\*. Virtual sensing for real-time strain field estimation and its verification on a laboratory-scale jacket structure under water waves, Computers & Structures, 298, 107344, Jul 2024.

**2023**

- Shin S, Hyun C, Cho S\*, Lee PS\*. Multi-sensor data-based anomaly detection and diagnosis of a pumped storage hydropower plant, Structural Engineering and Mechanics, 88, 569-581, Dec 2023.
- Kim YH, Cho S, Lee PS\*. Wave height classification via deep learning using monoscopic ocean videos, Ocean Engineering, 288, 116002, Oct 2023.
- Choi HG, Lee PS\*. The simplified MITC4+ shell element and its performance in linear and nonlinear analysis, Computers & Structures, 290, 107177, Sep 2023.
- Kim G, Lee PS\*. Mesh coarsening using the phantom-node method in the phase field model, Finite Elements in Analysis and Design, 228, 104048, Sep 2023.
- Park M, Lee PS\*. Integrated hydrostatic and hydrodynamic analysis of flexible floating structures, Ocean Engineering, 288, 114945, May 2023.
- Lee SG, Kim D, Lee PS\*. Vehicle collision simulation for roadblocks in nuclear power plants using LS-DYNA(LS-DYNA를 이용한 원자력발전소의 로드블록에 대한 차량 충돌 시뮬레이션), Journal of COSEIK, 36(2), 113-120, Apr 2023.
- Jung H, Lee C, Lee PS\*. Strain-smoothed polygonal finite elements, Structural Engineering and Mechanics, 86, 311-324, Mar 2023.
- Kim G, Lee PS\*. Towards improving the computational efficiency of the phase field model, Computers & Structures, 276, 106951, Mar 2023.

**2022**

- Choi HG, Lee PS\*. Towards improving the 2D-MITC4 element for analysis of plane stress and strain problems, Computers & Structures, 275, 106933, Oct 2022.
- Lee C, Lee DH, Lee PS\*. The strain-smoothed MITC3+ shell element in nonlinear analysis, Computers & Structures, 265, 106768, Jun 2022.
- Jung J, Jun H, Lee PS\*. Self-updated four-node finite element using deep learning, Computational Mechanics, 69, 23-24, Jan 2022.

**2021**

- Hyun C, Lee PS\*. A load balancing algorithm for the parallel automated multilevel substructuring method, Computers & Structures, 257, 106649, Dec 2021.
- Lee DH, Kim HJ, Lee PS\*. Direct calculation of interface warping functions for considering longitudinal discontinuities in beams, Structural Engineering and Mechanics, 80, 625-643, Dec 2021.
- Kim HJ, Lee DH, Yoon K, Lee PS\*. A multi-director continuum beam finite element for efficient analysis of multi-layer strand cables, Computers & Structures, 256, 106621, Nov 2021.
- Oh MH, Kim HJ, Yoon K, Lee PS. Direct evaluation of the local stability of structures using nonlinear FE solutions, Structural Engineering and Mechanics, 80, 477-490, Nov 2021.
- Park HJ, Seo H, Lee PS\*. Direct imposition of the wall boundary condition for simulating free surface flows in SPH, Structural Engineering and Mechanics, 78, 497-518, May 2021.
- Seo H, Park HJ, Kim J, Lee PS\*. The particle-attached element interpolation for density correction in smoothed particle hydrodynamics, Advances in Engineering Software, 154, 102972, Apr 2021.
- Lee C, Kim S, Lee PS\*. The strain-smoothed 4-node quadrilateral finite element, Computer Methods in Applied Mechanics and Engineering, 373, 113481, Jan 2021.

## 특허

누리집 PUBLICATIONS 페이지 PATENTS 목록 가운데 연도가 2021–2022년인 4건이다. 누리집은 특허마다 이름과 연도만 적고 출원·등록 구분과 번호, 날짜는 적지 않아, 2021년 2건은 2021년 10월 전의 것일 수 있다.[^pubs]

- 2022 · Anti-wrinkle apparatus of flexible display (플렉서블 디스플레이의 주름 방지 장치)
- 2022 · Fluid outflow blocking apparatus by using water glider (수중 글라이더를 이용한 파공봉쇄장치)
- 2021 · Rollable display apparatus (롤러블 디스플레이 장치)
- 2021 · Method and system for fault diagnosis of pump-turbines based on machine learning (기계학습 기반 펌프수차 고장 진단 방법 및 시스템)

## 과제

누리집 RESEARCH 페이지 PROJECTS 목록 가운데 기간이 2021년 10월 이후에 걸친 18건이다. 지원 기관, 과제 이름, 기간은 목록 그대로이고, 2021년 이전에 시작한 과제와 2027년까지 이어지는 과제도 있다.[^research]

- 초고속 하이퍼튜브와 가이드웨이 상호작용 해석 기법 개발 및 설계 하중 산정 (지원 KRRI(한국철도기술연구원); 기간 April 2026-Dec 2026)
- 외부 공격 및 충격에 대비한 해양 원자력 추진선 및 발전선 원자로 방호구조 개발 (지원 KSOE (한국조선해양); 기간 Mar 2025-Dec 2025)
- 의장구조 안전성 평가를 위한 전용 1D BEAM 구조진동 해석 솔버 개발 (지원 KSOE (한국조선해양); 기간 Feb 2024-Sep 2024)
- 화포용 추진제의 강내탄도 예측 프로그램 개발 (지원 Poongsan Corporation (풍산 방산기술연구원); 기간 Jan 2024-Dec 2026)
- 하이퍼튜브 차량(HTX)과 가이드웨이 3차원 상호작용 해석 기법 개발 (지원 KRRI(한국철도기술연구원); 기간 May 2023-Dec 2024)
- 드로그를 이용한 무인잠수정 진·회수 도킹 시스템 개발 (지원 ADD (국방과학연구소); 기간 Nov 2022-Dec 2026)
- 선박 열선 방호 및 차폐 개념 연구 (지원 DSME (대우조선해양); 기간 Jul 2022-Jun 2023)
- 폴더블 디스플레이 주름 방지 메커니즘 개발 (지원 KAIST (한국과학기술원); 기간 Jun 2022-Dec 2022)
- 조선/해양플랜트/전기전자/건설기계/로봇 등 신기술/신제품/신사업의 기술개발 타당성 연구 (지원 KSOE (한국조선해양); 기간 Jan 2022-Dec 2027)
- 거주구/엔진룸 변형 원인 분석 연구 (지원 SHI (삼성중공업); 기간 Dec 2021-Mar 2023)
- 노후 플랫폼 수명 연장을 위한 구조건전성모니터링(SHM) 기술 개발 (지원 HHI (현대중공업); 기간 Oct 2021-Sep 2022)
- 탄소성 재료 거동 Shell Solver 개발 (지원 KSOE (한국조선해양); 기간 Aug 2021-Dec 2021)
- 폴더블 스마트폰용 플렉시블 디스플레이 주름 방지 장치 (지원 KAIST (한국과학기술원); 기간 May 2021-Dec 2021)
- 폭발물 및 차량강습 위협에 대한 원자력시설 물리적방벽 성능검증을 위한 DB 구축 (지원 KoFONS (한국원자력안전재단); 기간 Apr 2021-Dec 2026)
- 스마트야드 전문인력양성 (지원 RIMS (재단법인 중소조선연구원); 기간 Mar 2021-Feb 2026)
- 장주기 다목적 무인잠수모함 핵심기술 개발 (지원 ADD (국방과학연구소); 기간 Nov 2019-Nov 2024)
- 해상 복합 발전 시스템 융합 설계 및 운영 지능화 고급트랙 (지원 KETEP (한국에너지기술평가원); 기간 Apr 2018-Dec 2022)
- Numerical methods for analysis of highly nonlinear multi-physics problems in ocean systems engineering (해양공학에서 고도의 비선형성을 갖는 다물리 상호작용 문제들의 수치해석 기법 개발) (지원 NRF (한국연구재단); 기간 Mar 2018-Feb 2023)

## 소식

누리집 NEWS 게시판 첫 쪽의 2021년 10월–2026년 8월 글 가운데 졸업생 교수 임용, 학회 참가, 세미나, 수상, 기획 기사 25건이다. 날짜는 제목 앞에 적힌 연·월이고, 제목은 게시판 표기 그대로다.[^news]

- 2026.08 · 이승보 박사(2024년 졸업, 지도교수: 이필승) 부산대학교 교수 임용 (번호 221)
- 2025.11 · 2025년도 전산구조공학회 학술심포지엄 (번호 213)
- 2025.08 · The 2025 World Congress on Advances in Structural Engineering and Mechanics (ASEM25) (번호 211)
- 2025.04 · 기계공학 세미나 (김기환 교수님, 김재민 교수님) (번호 205)
- 2025.02 · 김기환 박사(2023년 졸업, 지도교수: 이필승) 국립금오공과대학교 교수 임용 (번호 200)
- 2025.01 · 김재민 박사(2016년 졸업, 지도교수: 이필승) 국립창원대학교 교수 임용 (번호 198)
- 2024.10 · 11th KAIST-SJTU-UTokyo Joint Academic Symposium (번호 195)
- 2024.04 · 2024년도 전산구조공학회 정기학술대회 (번호 188)
- 2023.11 · 2023년도 전산구조공학회 정기학술대회 (번호 182)
- 2023.08 · The 2023 World Congress on Advances in Structural Engineering and Mechanics (ASEM23) (번호 181)
- 2023.05 · Research Day 연구상 수상 (번호 179)
- 2023.03 · 조성필 박사(2013년 졸업, 지도교수: 이필승) 한국항공대학교 교수 임용 (번호 175)
- 2023.03 · 정재호 박사(2021년 졸업, 지도교수: 이필승) 충북대학교 교수 임용 (번호 174)
- 2023.02 · 글로벌리더십 포상 (번호 172)
- 2022.11 · 2022년도 전산구조공학회 정기학술대회 (번호 167)
- 2022.09 · 이채민 박사(2020년 졸업, 지도교수: 이필승) 충북대학교 교수 임용 (번호 166)
- 2022.08 · The 14th CST and 11th ECT Conferences in France (번호 165)
- 2022.07 · 기계공학 세미나 (김재민 선배님) (번호 163)
- 2022.06 · 기계공학 세미나 (이기환 선배님) (번호 161)
- 2022.04 · 2022년도 전산구조공학회 정기학술대회 (번호 158)
- 2022.03 · 서현덕 박사(2021년 졸업, 지도교수: 이필승) 한국해양대학교 교수임용 (번호 157)
- 2021.12 · "해양 원자력 발전소 이야기", 전산구조공학 기획특집기사 (번호 155)
- 2021.12 · 윤경호 박사(2015년 졸업, 지도교수: 이필승) 연세대학교 교수임용 (번호 154)
- 2021.11 · 2021년도 전산구조공학회 정기학술대회 (번호 153)
- 2021.10 · 이채민군 기계공학과 우수상 수상 (번호 151)

## 연락과 위치

- 연구실: Office Room 2100, Eureka Hall N27, Department of Mechanical Engineering (Ocean Systems Engineering), KAIST, 전화 82-42-350-1552[^about][^home]
- 교수실과 전화: 유레카관(N27) 2103, 042-350-1512[^meprof]
- 교수 이메일: phillseung@kaist.edu[^meprof]
[^p1]: H. Jung, C. Lee, P.-S. Lee, Structural Engineering and Mechanics 86, 311-324 (2023). <https://doi.org/10.12989/sem.2023.86.3.311> 초록 기준(출판사 논문 페이지).
[^p2]: H. Jung, Y. S. Jeong, P.-S. Lee, Structural Engineering and Mechanics 96, 225-237 (2025). <https://doi.org/10.12989/sem.2025.96.3.225> 초록 기준(출판사 논문 페이지).
[^p3]: J. Jung, H. Jun, P.-S. Lee, Computational Mechanics 69, 23-44 (온라인 2021-08-24). <https://doi.org/10.1007/s00466-021-02081-7> 초록 기준.
[^p4]: S. Shin, C. Hyun, S. Cho, P.-S. Lee, Structural Engineering and Mechanics 88, 569-581 (2023). <https://doi.org/10.12989/sem.2023.88.6.569> 초록 기준(출판사 논문 페이지).
[^p5]: Y. S. Jeong, P.-S. Lee, International Journal for Numerical Methods in Engineering 126, e70116 (온라인 2025-09-03). <https://doi.org/10.1002/nme.70116> 초록 기준.
[^p6]: H.-J. Park, H.-D. Seo, P.-S. Lee, Structural Engineering and Mechanics 78, 497-518 (2021). <https://doi.org/10.12989/sem.2021.78.4.497> 초록 기준(출판사 논문 페이지).
[^p7]: S. Lee, S. Lee, P.-S. Lee, Structural Engineering and Mechanics 97, 393-416 (2026). <https://doi.org/10.12989/sem.2026.97.3.393> 초록 기준(출판사 논문 페이지).
[^p8]: S. Lee, D. Kim, P.-S. Lee, Journal of the Computational Structural Engineering Institute of Korea 36, 113-120 (온라인 2023-04-30). <https://doi.org/10.7734/coseik.2023.36.2.113> 초록 기준(출판사 논문 페이지).
[^home]: 전산역학 및 구조시스템 연구실 누리집 첫 화면 <http://cmss.kaist.ac.kr/> (메뉴, 바닥글 주소·전화, 2026-10-23 열람)
[^about]: 연구실 누리집 ABOUT US 페이지 <http://cmss.kaist.ac.kr/bbs/content.php?ct_id=1&cate_id=10> (MISSION, CONTACT, 2026-10-23 열람)
[^people]: 연구실 누리집 PEOPLE 페이지 <http://cmss.kaist.ac.kr/bbs/content.php?ct_id=26&cate_id=20> (PRINCIPAL INVESTIGATOR, STUDENTS, 2026-10-23 열람)
[^research]: 연구실 누리집 RESEARCH 페이지 <http://cmss.kaist.ac.kr/bbs/content.php?ct_id=3&cate_id=30> (연구 영역 다섯, PROJECTS, 2026-10-23 열람)
[^pubs]: 연구실 누리집 PUBLICATIONS 페이지 <http://cmss.kaist.ac.kr/bbs/content.php?ct_id=4&cate_id=40> (PAPERS, PATENTS, 2026-10-23 열람)
[^alumni]: 연구실 누리집 ALUMNI 페이지 <http://cmss.kaist.ac.kr/bbs/content.php?ct_id=16&cate_id=50> (2026-10-23 열람)
[^news]: 연구실 누리집 NEWS 게시판 첫 쪽 <http://cmss.kaist.ac.kr/bbs/board.php?bo_table=tb02&cate_id=60> (글 123–222번, 2026-10-23 열람)
[^rd]: 연구실 누리집 NEWS 게시판 글 「2023.05. Research Day 연구상 수상」 <http://cmss.kaist.ac.kr/bbs/board.php?bo_table=tb02&wr_id=203&cate_id=60> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(이필승) <https://me.kaist.ac.kr/pop/team.html?uid=51&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 사무실, 전화, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 안내 두 항목 <https://me.kaist.ac.kr/research/research_010200.html> , <https://me.kaist.ac.kr/research/research_010300.html> (이필승 교수 항목, 2026-10-23 열람)

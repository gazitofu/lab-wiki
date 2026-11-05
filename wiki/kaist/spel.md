# 스마트공정공학 연구실 (Smart Process Engineering Laboratory, SPEL)

**KAIST 생명화학공학과 · 허성민 부교수**

- 분야: 화학 공정 설계·운전, 배터리 수명 예측, 수소 공급망, 분리 공정, 공정 제어
- 대분야: 화학공정·바이오공학, 에너지·환경·지구
- 태그: 배터리 관리 시스템[^storage], 스마트 그리드·전력 관리[^hydrogen], 수소 저장·운송[^hydrogen], 분리막[^separation], 탄소 포집·저장[^separation], 제어 이론·제어 공학[^design], 수리 최적화·최적화 알고리즘[^design]
- 홈페이지: <https://spel.kaist.ac.kr/>
- 근거와 출처: [스마트공정공학 연구실 근거 페이지](spel-sources.md)

> 화학 공정(원료를 원하는 물질로 바꾸는 생산 단계의 체계)의 구조와 운전 방법, 설비 투자를 계산으로 설계하는 연구실이다.[^home][^research]

## 무엇을 연구하나

허성민 교수가 이끄는 연구실은 공정시스템공학(생산 단계들을 하나의 체계로 보고 설계와 운전을 다루는 공학)을 바탕으로 계산 방법을 개발한다. 최적화(주어진 제약 조건 안에서 목표값을 가장 좋게 하는 선택을 찾는 계산), 모사(대상의 동작을 모형으로 재현해 살피는 일), 제어(측정한 상태에 따라 입력을 조절해 원하는 동작을 얻는 일), 기계학습(자료에서 규칙을 학습해 예측이나 판단에 이용하는 계산 방법)을 결합한다. 모형은 현상을 수식이나 계산 규칙으로 표현한 것이다.[^home][^research]

연구 대상에는 충전해 쓰는 배터리의 수명과 운영 신뢰성, 수소의 생산·저장·운송과 전력 설비의 계획이 있다. 에너지(일을 하거나 변화를 일으킬 수 있는 능력)를 저장하고 공급하는 설비의 운전 조건과 투자를 함께 다루며, 날씨와 가격의 불확실성을 계산에 반영한다. 배터리에서는 물리 법칙과 사용 이력 자료를 결합하고, 서로 다른 종류의 배터리와 사용 상황에 맞춰 예측 모형을 옮겨 적용한다.[^storage][^hydrogen]

다른 갈래는 물 처리와 이산화탄소 포집을 위한 분리 공정이다.[^separation] 분리막(특정 물질을 선택적으로 통과시켜 혼합물을 나누는 막)이 놓인 통로의 흐름을 계산하고, 막 사이의 간격을 유지하는 구조물의 모양과 운전 조건을 함께 설계한다. 계산 결과를 바탕으로 현장 설비와 연결된 가상 모형을 만들고, 통로 수준의 결과를 막 묶음과 전체 설비의 운전에 연결하려 한다.[^separation]

공정 합성 연구에서 연구실은 설비 설계와 운전 방법을 순서대로 따로 최적화하는 대신 두 결정을 함께 다룬다. 연구실은 가능한 장치·경로·연결을 함께 나열한 공정 구조와 제어 구조를 동시에 고르는 계산 방법을 개발한다. 또한 대규모 문제를 나누어 계산하고 초기 선택값을 정하는 데 인공지능을 보조적으로 쓰되, 제약 조건을 만족하는지 확인하는 절차를 둔다.[^design]

## 주요 연구 주제

### 1. 배터리의 상태·수명 예측과 충전

리튬이온전지(리튬 이온이 양쪽 전극 사이를 오가며 충전과 방전을 하는 전지)의 물리적 거동과 현장 자료를 함께 반영하는 예측 모형을 연구한다. 이온은 전자를 잃거나 얻어 전기를 띠는 원자나 분자이고, 전극은 전기가 물질로 들어가거나 나오는 경계를 이루는 부분이다. 충전과 방전은 각각 에너지를 저장하고 전기로 꺼내 쓰는 일이다. 자료의 잡음과 누락, 사용 중 사건이 불규칙하게 기록되는 문제를 다루고, 상태 진단을 충전 방법·보증·설비 관리 결정과 연결한다. 예측 오차와 불확실성을 고려하면서 배터리를 안전하게 충방전할 수 있도록 진단과 현실적 제약 안에서의 최적 충전 방법을 연구한다.[^storage]

### 2. 수소 공급망과 전력 시스템의 공동 계획

재생에너지(자연 과정으로 지속적으로 보충되는 에너지원)를 이용한 수소 생산과 전력의 저장·공급을 함께 계획한다. 수소를 옮기는 배관·저장 시설·항만의 배치와 설비 용량을 정하고, 배터리와 수소 생산 설비의 운전 일정 및 전력 시장 참여를 함께 최적화한다.[^hydrogen] 전력·열·수송 부문을 연결한 계획을 세우며 날씨·가격 변동과 정책 지원의 영향을 분석한다.[^hydrogen]

### 3. 물 처리·탄소 포집을 위한 분리 공정

막 통로의 유동(액체나 기체가 흐르는 현상)을 계산하는 방법과, 물리 법칙을 학습 조건에 넣은 신경망(자료의 특징을 계산하는 단위들을 연결하고 연결의 값을 학습하는 모형)을 결합한다. 통로의 구조와 운전 범위를 바꾸며 투과 플럭스(막의 단위 면적을 단위 시간 동안 통과하는 물질의 양)·에너지 소비·막 오염의 관계를 다루고, 물 처리와 탄소 포집에 쓰는 막 공정을 설계·최적화한다.[^separation] 디지털트윈(관측 자료와 연결된 실제 대상의 가상 모형)을 개발해 통로 수준의 결과를 설비 설계와 실시간 감시에 연결하려 한다.[^separation]

### 4. 공정·제어 구조의 동시 설계와 최적화 방법

그래프(대상 사이의 연결 관계를 점과 선으로 나타낸 수학 구조)를 이용해 공정의 설계와 제어 구조를 동시에 정하는 방법을 개발한다.[^design] 여러 제어기를 둔 구조를 어떻게 나눌지 살피고 전체 설비 사례로 검증한다. 인공지능 보강 확률 최적화는 불확실한 값의 발생 가능성을 반영한 의사결정 계산에 인공지능을 보조적으로 결합하는 접근이다. 연구실은 대규모 전력·수소 시스템을 위한 이 계산 틀을 개발하며 문제 분할·초기값 설정·계산 조정을 지원한다.[^design]

## 대표 논문

허성민 교수가 저자로 참여한 KAIST 재직 시기의 논문을 연구 주제와 초록에 따라 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 사전 공개본은 발표처에 표시했다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자와 교수 역할 |
|---|---|---|---|---|
| 1 | 2024 | [Gaussian Process Regression-Based Lithium-Ion Battery End-of-Life Prediction Model under Various Operating Conditions](https://doi.org/10.48550/arXiv.2410.19886) · arXiv 사전 공개본 | 기존 배터리 수명 예측 모형은 입력 구성이 복잡한데, 운전 조건만을 입력으로 명목 수명 종료 시점을 예측하는 모형을 제안했다. 충전율·주변 온도·방전 깊이를 바꾸는 전기화학 모사로 열화(사용하면서 성능이 떨어지는 현상) 자료 100개를 만들고 가우스 과정 회귀 모형을 개발했다. 가우스 과정 회귀는 입력에 따른 값들의 관계를 확률적으로 표현해 예측하는 방법이다. 운전 조건별 특성을 반영한 커널(입력 사이의 관계를 정하는 함수)을 제안해 기존 커널 대비 수명 예측 오차를 46.62% 줄였다고 보고했다.[^p1] | 1저자 Seyeong Park, 교신저자 허성민 |
| 2 | 2025 | [Multi-period Deployment of Electrochemical CO2-to-CO Reduction Technology Considering Time Varying Uncertainties](https://doi.org/10.1007/s11814-024-00373-1) · Korean Journal of Chemical Engineering | 전기로 이산화탄소를 일산화탄소로 바꾸는 기술을 언제 도입하고 확대할지 계획했다. 미래 현금 흐름을 현재 가치로 환산해 한 시점에 결정하는 평가 대신, 확장과 지연 같은 선택을 여러 시점에 둘 수 있는 모형을 만들었다. 강화학습(행동과 그 결과로 얻는 보상을 통해 선택 방법을 학습하는 기계학습)을 이용해 계산하고 기존 평가와 비교했으며, 정책과 에너지 가격의 불확실성이 도입 계획에 미치는 영향을 시나리오별로 살폈다.[^p2] | 1저자 Woopill Chun, 마지막 저자 허성민(누리집 표시 *) |
| 3 | 2024 | [Superstructure Optimization of International Hydrogen Supply Chain with Technological Options](https://doi.org/10.1016/j.ifacol.2024.08.437) · IFAC-PapersOnLine | 수소 생산지와 소비지가 멀리 떨어져 있을 때 운송 수단과 수소를 담는 형태를 함께 고르는 공급망 모형을 제시했다. 중동 생산지와 미국 텍사스 수요지를 연결하는 사례에서 기존 기술과 유망 기술을 함께 포함한 초구조를 구성했다. 초구조는 가능한 설비와 연결 대안을 함께 포함한 구조다. 정수와 연속값을 함께 선택하는 선형 최적화로 비용 효율적인 수소 공급 경로를 찾는 틀을 제시했다.[^p3] | 1저자 Juyeong Jung, 마지막 저자 허성민(누리집 표시 *) |
| 4 | 2023 | [Applying real options with reinforcement learning to assess commercial CCU deployment](https://doi.org/10.1016/j.jcou.2023.102613) · Journal of CO2 Utilization | 탄소 포집·활용 기술의 상용 설비 투자를 평가하기 위해, 가격·시장·기술·정책의 변화와 설비 용량 확대 결정을 함께 다루는 틀을 제안했다. 실물옵션은 투자를 확대·지연·포기할 수 있는 선택의 가치를 평가하는 방법이다. 이를 강화학습과 결합하고, 복잡한 계산을 대신하는 대리 모형·불확실성 모형·평가 모형의 세 단계로 구성했다. 유럽에서 이산화탄소를 수소와 반응시켜 메탄올로 바꾸는 공정 사례로 적용을 보였다.[^p4] | 공동 1저자 Jeehwan S. Lee·Woopill Chun, 허성민 저자 참여(누리집 표시 *) |

## 교수와 전문 분야

허성민 교수는 서울대학교에서 화학생물공학 학사 학위를 2009년에, University of Minnesota에서 화학공학 박사 학위를 2015년에 받았다. 박사 지도교수는 Prodromos Daoutidis다. 2015년 6월–2020년 2월 KAIST에서 박사후연구원으로 일했고, 2020년 3월–2023년 6월 단국대학교 화학공학과 조교수를 지냈다. 2023년 7월 KAIST 생명화학공학과 조교수로 부임했으며, 2026년 9월부터 부교수다.[^professor][^faculty]

학과 소개의 전문 분야는 공정 모형화와 모사, 공정 제어, 최적화, 기계학습이다.[^faculty] 연구실의 최근 연구에서는 이를 배터리 예측, 수소 공급망 설계, 탄소 활용 기술의 투자 평가로 연결한다.[^storage][^hydrogen][^p2][^p4] International Journal of Control, Automation, and Systems의 Associate Editor를 2022년 3월부터, Korean Journal of Chemical Engineering의 Associate Editor를 2021년 1월부터 맡고 있다.[^professor]

## 응용 분야

배터리 진단·충전과 유지보수, 재생에너지 기반 수소와 전력의 공동 계획, 물 처리용 막 공정, 이산화탄소 포집·전환, 생산 설비의 구조와 운전 계획이 주요 응용 대상이다.[^storage][^hydrogen][^separation][^design]

## 구성원

구성원 페이지의 박사후연구원·재학생·학부 인턴 13명이다. 연구 주제는 연구 소개의 구성원 연결 표기다. ‘대표 논문 참여’는 전체 저자 명단과 이름이 같은 경우에 논문 번호를 표시한다.[^members][^research]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Sungjin Bae (배성진) | 박사후연구원 | 2025.08– | Membrane & Separation Processes |  |
| Ji Hee Kim (김지희) | 박사과정 | 2023 Fall– | Graph-Theoretic Co-Design and AI-Augmented Optimization |  |
| Hana Kim (김한아) | 박사과정 | 2025 Spring– | Hydrogen & Sector-Coupled Energy Systems |  |
| Hae Yong Jung (정해용) | 박사과정 | 2025 Fall– | Hydrogen & Sector-Coupled Energy Systems |  |
| Naeun Choi (최나은) | 박사과정 | 2025 Fall– | Process Systems Synthesis & AI-Driven Design |  |
| Sunwook Kim (김선욱) | 박사과정 | 2026 Spring– | Process Systems Synthesis & AI-Driven Design |  |
| Hyunji Kwon (권현지) | 석박사통합과정 | 2025 Spring– | Process Systems Synthesis & AI-Driven Design |  |
| Jongwoo Kim (김종우) | 석사과정 | 2025 Spring– | Membrane & Separation Processes |  |
| Yooil Son (손유일) | 석사과정 | 2025 Spring– | Electrochemical Energy Storage |  |
| Yoojung Yoon (윤유정) | 석사과정 | 2026 Spring– | Graph-Theoretic Co-Design and AI-Augmented Optimization |  |
| Eunji Seo (서은지) | 석사과정 | 2026 Fall– | Membrane & Separation Processes |  |
| Seo Yoon Lee (이서윤) | 석사과정 | 2026 Fall– | Electrochemical Energy Storage |  |
| Yerin Kim (김예린) | 학부 인턴 |  |  |  |

최나은은 구성원 페이지에 Lab Manager를 겸한 박사과정 학생으로 적혀 있다.[^members]

### 진학 예정

구성원 페이지의 Prospective Graduate Students 구획에 실린 4명이다.[^members]

| 이름 | 예정 과정 | 누리집의 시작 표기 |
|---|---|---|
| Jiun Yun (윤지운) | 박사과정 | 2027 Spring– |
| Juho Yoo (유주호) | 석사과정 | 2027 Spring– |
| Jonghwan Lee (이종환) | 석사과정 | 2027 Spring– |
| Hyeonseok Jin (진현석) | 석사과정 | 2027 Spring– |

## 졸업생 진로

졸업생 페이지의 박사후연구원·박사·석사 구획에 실린 16명이다. 학위와 연도, 진로는 누리집 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dongho Han (한동호) | 박사후연구원 2024/09–2025/02; Ph.D. (2024) | LG Energy Solution |
| Sunwoo Kim (김선우) | Ph.D. (2026) | Korea Institute of Energy Research |
| Joungho Park (박정호) | Ph.D. (2024) | Principal Researcher @ Korea Institute of Energy Research |
| Derrick Adams (데릭 아담스) | Ph.D. (2025) | DOFTECH |
| Hyemin Choi (최혜민) | Ph.D. (2026) | Samsung Electronics |
| Woohyun Jeong (정우현) | Ph.D. (2025) | LG Energy Solution |
| Jaewook Lee (이재욱) | Ph.D. (2025) | Postdoc @ Seoul National University |
| Juyeong Jung (정주영) | Ph.D. (2024) | Samsung Electronics |
| Yechan Choi (최예찬) | Ph.D. (2024) | Samsung Electronics |
| Hongbum Choi (최홍범) | Ph.D. (2024) | Samsung Electronics |
| Hyungmuk Lim (임형묵) | Ph.D. (2024) | POSCO |
| Sangjun Jeon (전상준) | M.S. (2026) | Ph.D. student @ University of Wisconsin–Madison |
| Byoungyoun Lee (이병연) | M.S. (2026) |  |
| Mingyu Kim (김민규) | M.S. (2025) |  |
| Seyeong Park (박세영) | M.S. (2024) | SK on |
| Woopill Chun (천우필) | M.S. (2024) | S-Oil |

## 최근 5년 논문 목록

2021–2026년 목록으로 학술지 논문 25편, 심사 학회 논문 4편, 책 장 2편과 사전 공개본 1편이다. 사전 공개본은 연구실 게시 목록에 없어 교수가 저자인 것을 확인한 서지를 더했다. 허성민 교수의 2023년 7월 KAIST 부임 전 항목이 섞여 있다. 학술지·학회·책 장은 연구실 게시 표기를 따르며, 별표는 누리집 표시이고 †는 누리집이 밝힌 공동 1저자 표시다. 책 장의 연도는 등록 출판일 기준이며, 사전 공개본에는 판본과 날짜를 표시했다.[^pubs][^bibliography][^professor][^p1]

**2026**

- Physics-informed lithium-ion battery end-of-life prediction model for data-efficient deployment, Jaewook Lee†, Seyeong Park†, Sangjun Jeon, Seongmin Heo\*, Journal of Energy Storage 182, 124739, 2026. <https://doi.org/10.1016/j.est.2026.124739>
- Economic mitigation strategy for the duck curve phenomenon: Revealing the effectiveness of green hydrogen, Hana Kim, Seongmin Heo\*, Joungho Park\*, Energy 362, 142158, 2026. <https://doi.org/10.1016/j.energy.2026.142158>
- Uncertainty-aware process design using constrained Bayesian optimization: An application to Fischer-Tropsch mixture separation, Sunwook Kim, Seongmin Heo\*, Energy Conversion and Management 368, 121988, 2026. <https://doi.org/10.1016/j.enconman.2026.121988>
- Interpretable noninvasive framework for lithium-ion battery degradation diagnosis: Joint prediction of capacity and power fade and mechanism-aware health index classification, Sangjun Jeon†, Jaewook Lee†, Seongmin Heo\*, Applied Energy 417, 128036, 2026. <https://doi.org/10.1016/j.apenergy.2026.128036>
- A sensitivity-based graph-theoretic framework for robust distributed control system design considering uncertainty, Ji Hee Kim, Seongmin Heo\*, Computers & Chemical Engineering 212, 109693, 2026. <https://doi.org/10.1016/j.compchemeng.2026.109693>
- System-level comparison of green and blue hydrogen for cogeneration of clean hydrogen and electricity, Yechan Choi†, Byoungyoun Lee†, Seongmin Heo\*, Energy Conversion and Management 358, 121505, 2026. <https://doi.org/10.1016/j.enconman.2026.121505>
- Dynamic optimization of coke formation in dry reforming of methane using a neural quasi-steady-state model, Hye Min Choi, Seongmin Heo\*, Jay H. Lee\*, Chemical Engineering Journal 535, 175565, 2026. <https://doi.org/10.1016/j.cej.2026.175565>
- Evaluation of geographic and climatic impacts on joint planning of green hydrogen and renewable electricity supply chains, Yechan Choi†, Byoungyoun Lee†, Seongmin Heo\*, International Journal of Hydrogen Energy 224, 154471, 2026. <https://doi.org/10.1016/j.ijhydene.2026.154471>
- Health-conscious charging of lithium-ion batteries using Bayesian optimization guided by a semi-empirical aging model, Woohyun Jeong, Seongmin Heo\*, Jay H. Lee\*, Journal of Energy Storage 141, 119348, 2026. <https://doi.org/10.1016/j.est.2025.119348>

**2025**

- End-effect mitigation in renewable energy systems with energy storage using value function approximation of terminal energy level, Dongho Han, Seongmin Heo\*, Applied Energy 401, 126785, 2025. <https://doi.org/10.1016/j.apenergy.2025.126785>
- Noninvasive inline imaging and computer vision-based quality variable estimation for continuous slug-flow crystallizers, Derrick Adams, Jay H. Lee, Shin Hyuk Kim\*, Seongmin Heo\*, Computers & Chemical Engineering 197, 109067, 2025. <https://doi.org/10.1016/j.compchemeng.2025.109067>
- Techno-economic analysis of amine-based post-combustion carbon capture process with flexibility considerations, Hae Yong Jung†, Hyungmuk Lim†, Seongmin Heo\*, Fuel 390, 134634, 2025. <https://doi.org/10.1016/j.fuel.2025.134634>
- Multi-period deployment of electrochemical CO2 reduction technology considering time varying uncertainties, Woopill Chun, Suhyeon Lee, Kosan Roh\*, Seongmin Heo\*, Korean Journal of Chemical Engineering 42, 1549–1559, 2025. <https://doi.org/10.1007/s11814-024-00373-1>
- Synergy evaluation for joint expansion planning of green hydrogen and renewable electricity supply chains: A South Korea case, Yechan Choi, Mingyu Kim, Shin Hyuk Kim, Seongmin Heo\*, Applied Energy 381, 125123, 2025. <https://doi.org/10.1016/j.apenergy.2024.125123>
- Extracting key temporal and cyclic features from VIT data to predict lithium-ion battery knee points using attention mechanisms, Jaewook Lee, Seongmin Heo, Jay H. Lee\*, Computers & Chemical Engineering 193, 108931, 2025. <https://doi.org/10.1016/j.compchemeng.2024.108931>

**2024**

- Multi-period, multi-timescale stochastic optimization model for simultaneous capacity investment and energy management decisions for hybrid Micro-Grids with green hydrogen production under uncertainty, Sunwoo Kim, Yechan Choi, Joungho Park, Derrick Adams, Seongmin Heo, Jay H. Lee\*, Renewable & Sustainable Energy Reviews 190, 114049, 2024. <https://doi.org/10.1016/j.rser.2023.114049>
- Techno-economic analysis of solar powered green hydrogen system based on multi-objective optimization of economics and productivity, Joungho Park, Sungho Kang, Sunwoo Kim, Hyun-Seok Cho, Seongmin Heo, Jay H. Lee\*, Energy Conversion and Management 299, 117823, 2024. <https://doi.org/10.1016/j.enconman.2023.117823>
- Juyeong Jung, Jay H. Lee, Wonsuk Chung, Seongmin Heo\*, “Superstructure optimization of international hydrogen supply chain with technological options,” 12th IFAC Symposium on Advanced Control of Chemical Processes (ADCHEM), pp. 811–816, 2024. <https://doi.org/10.1016/j.ifacol.2024.08.437>
- Seyeong Park, Jaewook Lee, Seongmin Heo. "Gaussian Process Regression-Based Lithium-Ion Battery End-of-Life Prediction Model under Various Operating Conditions". arXiv:2410.19886 (사전 공개본, 2024-10-25). <https://doi.org/10.48550/arXiv.2410.19886>

**2023**

- Applying real options with reinforcement learning to assess commercial CCU deployment, Jeehwan S. Lee†, Woopill Chun†, Kosan Roh, Seongmin Heo\*, Jay H. Lee\*, Journal of CO2 Utilization 77, 102613, 2023. <https://doi.org/10.1016/j.jcou.2023.102613>
- A hybrid modeling framework for efficient development of Fischer-Tropsch kinetic models, Ji Hee Kim†, Geun Bae Rhim†, Naeun Choi, Min Hye Youn, Dong Hyun Chun\*, Seongmin Heo\*, Journal of Industrial & Engineering Chemistry 118, 318–329, 2023. <https://doi.org/10.1016/j.jiec.2022.11.016>

**2022**

- An iterative constrained least squares method for continuous piecewise linear approximation, Ji Hee Kim†, Naeun Choi†, Seongmin Heo\*, Computers & Chemical Engineering 168, 108056, 2022. <https://doi.org/10.1016/j.compchemeng.2022.108056>
- Sustainability analysis framework based on global market dynamics: A carbon capture and utilization industry case, Kyung Hwan Ryu, Boeun Kim, Seongmin Heo\*, Renewable & Sustainable Energy Reviews 166, 112639, 2022. <https://doi.org/10.1016/j.rser.2022.112639>
- Risk-based uncertainty assessment to identify key sustainability hurdles for emerging CO2 utilization technologies, Jeehwan S. Lee, Juyeong Jung, Kosan Roh, Seongmin Heo, Ung Lee, Jay H. Lee\*, Green Chemistry 24, 4588–4605, 2022. <https://doi.org/10.1039/D2GC00514J>
- Electrode design and performance of flow-type electrochemical lithium recovery (ELR) systems, Seon Yeop Jung, Hwajoo Joo, Ji Hee Kim, Seoni Kim, Seongmin Heo\*, Jeyong Yoon\*, Desalination 532, 115732, 2022. <https://doi.org/10.1016/j.desal.2022.115732>
- Feature variance regularization method for autoencoder-based one-class classification, Boeun Kim, Kyung Hwan Ryu, Ji Hee Kim, Seongmin Heo\*, Computers & Chemical Engineering 161, 107776, 2022. <https://doi.org/10.1016/j.compchemeng.2022.107776>
- Mean squared error criterion for model-based design of experiments with subset selection, Boeun Kim, Kyung Hwan Ryu, Seongmin Heo\*, Computers & Chemical Engineering 159, 107667, 2022. <https://doi.org/10.1016/j.compchemeng.2022.107667>
- Boeun Kim, Seongmin Heo, Kyung Hwan Ryu\*, “Optimal process design of hydrogen production using response surface methodology,” 13th IFAC Symposium on Dynamics and Control of Process Systems, including Biosystems (DYCOPS), pp. 620–625, 2022. <https://doi.org/10.1016/j.ifacol.2022.07.512>
- Jeehwan S. Lee, Seongmin Heo, Jay H. Lee\*, “Modeling and sustainability assessment of outdoor chlorella vulgaris cultivation in South Korea for renewable bioplastic feedstock production,” 13th IFAC Symposium on Dynamics and Control of Process Systems, including Biosystems (DYCOPS), pp. 242–247, 2022. <https://doi.org/10.1016/j.ifacol.2022.07.451>
- Boeun Kim, Kyung Hwan Ryu, Seongmin Heo\*, “A neural network regularization method to address variance inflation in autoencoders,” 13th IFAC Symposium on Dynamics and Control of Process Systems, including Biosystems (DYCOPS), pp. 744–749, 2022. <https://doi.org/10.1016/j.ifacol.2022.07.533>

**2021**

- Seongmin Heo, Jay H. Lee. Chapter 20: Superstructure optimization of microalgal biorefinery producing biodiesel, in A-Z of Biorefinery: A Comprehensive View, Elsevier. <https://doi.org/10.1016/B978-0-12-819248-1.00010-5>
- Seongmin Heo, Jay H. Lee. Chapter 4: Algal based feedstocks, in A-Z of Biorefinery: A Comprehensive View, Elsevier. <https://doi.org/10.1016/B978-0-12-819248-1.00007-5>

## 과제

수행 기간이 2021-10-13–2026-10-13과 겹치는 14건이다. 허성민 교수의 2023년 7월 KAIST 부임 전 시작한 과제가 섞여 있다. 제목·사업·지원기관·기간은 연구실 과제 페이지 표기다.[^projects][^professor]

- 넷제로 해수 리파이너리; AI를 활용한 해수로부터 담수, 유용자원, 탄소네거티브 제품 생산 통합 플랫폼 개발 (사업 InnoCORE 연구단; 지원 KAIST; 기간 2026.07–2030.12)
- 대기 중 CO2로부터 알코올 생산을 위한 포집-전환 일체형 모듈 시스템 개발 (사업 CO2동시포집-전환(RCC)융합기술개발사업; 지원 한국연구재단; 기간 2026.04–2030.12)
- 불확실성을 고려한 인공지능 보강 대규모 에너지 시스템 의사결정 프레임워크 개발 (사업 신진연구(유형B); 지원 한국연구재단; 기간 2026.03–2031.02)
- 지능형 수소기술 혁신연구단 (사업 InnoCORE 연구단; 지원 UNIST; 기간 2025.07–2029.12)
- CO2 포집-저장-활용 기술 온실가스 감축량 평가기술 개발 (사업 글로벌탄소규제대응 통합관리기술개발사업; 지원 한국환경산업기술원; 기간 2025.04–2028.12)
- 분산형 저탄소 수소생산 연구센터 (사업 선도연구센터(ERC); 지원 한국연구재단; 기간 2024.03–2029.02)
- 합성가스 전환 경로별 타당성 검토 (지원 HD현대오일뱅크; 기간 2026.05–2026.10)
- CCU 공정의 경제성 및 CO2 저감효과 기반 실용성 평가 및 향상을 위한 전산모사, 분석과 최적화 (사업 유용물질 생산을 위한 Carbon to X 기술개발사업; 지원 한국연구재단; 기간 2020.07–2025.04)
- 지속 가능한 분리 공정 설계를 위한 최적 공정 구조 및 제어 구조의 동시 설계 방법 개발 (사업 기본연구; 지원 한국연구재단; 기간 2022.06–2025.02)
- 합성가스로부터 고순도 선형 알파올레핀 생산 기술개발 (사업 소재부품기술개발-전략핵심소재자립화; 지원 한국산업기술평가관리원; 기간 2020.08–2024.12)
- 스마트 디지털 엔지니어링 전문인력 양성 (사업 스마트디지털엔지니어링전문인력양성사업; 지원 서울대학교 산학협력단; 기간 2023.07–2024.02)
- 공정 지표를 반영한 직접 공기 포집용 이산화탄소 흡착 소재의 인공지능 기반 발굴 (지원 Saudi Aramco; 기간 2025.09–2026.08)
- 셀 구성 물질과 상황에 따른 가스 생성 예측 개발 연구 (지원 LG에너지솔루션; 기간 2025.06–2026.05)
- 가변형 생산공정 최적화 solver 개발 (지원 CJ제일제당; 기간 2024.06–2025.05)

## 수상과 선정

연구실 소식의 2023-11-10–2026-09-04 수상 글 5건이다.[^news]

- 2026-09-04 · 김한아 학생이 한국에너지기술연구원에서 학연 학술상을 수상했다.
- 2025-10-17 · 김선욱, 이병연 학생이 한국화학공학회 주관 2025년도 가을 총회 및 국제 학술대회에서 우수 포스터 발표상을 수상했다.
- 2024-05-13 · 한동호 학생이 2024년 봄 화학공학회에서 우수 구두 발표상을 수상했다.
- 2023-12-02 · 박세영 학생이 The 34th International Symposium on Chemical Engineering 학회에서 Outstanding Oral Presentation Award를 수상했다.
- 2023-11-10 · 허성민 교수가 International Journal of Control, Automation, and Systems 저널에서 Best Associate Editor Award를 수상했다.

## 소식

연구실 소식의 2023-10-24–2026-09-20 논문 게재·과제 참여 소식 28건이다.[^news]

- 2026-09-20 · 이재욱 졸업생(박사), 박세영 졸업생(석사)의 논문이 Journal of Energy Storage에 출판되었다.
- 2026-08-04 · 김한아 학생의 논문이 Energy에 출판되었다.
- 2026-07-31 · 김선욱 학생의 논문이 Energy Conversion and Management에 출판되었다.
- 2026-07-01 · KAIST 주관 InnoCORE 연구단에 참여하게 되었다: 넷제로 해수 리파이너리; AI를 활용한 해수로부터 담수, 유용자원, 탄소네거티브 제품 생산 통합 플랫폼 개발.
- 2026-05-09 · 전상준 학생, 이재욱 졸업생(박사)의 논문이 Applied Energy에 출판되었다.
- 2026-05-08 · 김지희 학생의 논문이 Computers & Chemical Engineering에 출판되었다.
- 2026-05-01 · HD현대오일뱅크의 지원을 받아 다음 과제를 수행하게 되었다: 합성가스 전환 경로별 타당성 검토.
- 2026-04-20 · 최예찬 졸업생(박사), 이병연 학생의 논문이 Energy Conversion and Management에 출판되었다.
- 2026-04-01 · 한국연구재단의 지원을 받아 다음 과제를 수행하게 되었다: 대기 중 CO2로부터 알코올 생산을 위한 포집-전환 일체형 모듈 시스템 개발.
- 2026-03-25 · 최혜민 졸업생(박사)의 논문이 Chemical Engineering Journal에 출판되었다.
- 2026-03-11 · 최예찬 졸업생(박사), 이병연 학생의 논문이 International Journal of Hydrogen Energy에 출판되었다.
- 2026-03-01 · 한국연구재단의 지원을 받아 다음 과제를 수행하게 되었다: 불확실성을 고려한 인공지능 보강 대규모 에너지 시스템 의사결정 프레임워크 개발.
- 2025-11-14 · 정우현 졸업생(박사)의 논문이 Journal of Energy Storage에 출판되었다.
- 2025-09-27 · 한동호 졸업생(박사/포닥)의 논문이 Applied Energy에 출판되었다.
- 2025-09-01 · Saudi Aramco의 지원을 받아 공정 지표를 반영한 직접 공기 포집용 이산화탄소 흡착 소재의 인공지능 기반 발굴 과제를 수행하게 되었다.
- 2025-07-01 · UNIST 주관 InnoCORE 연구단에 참여하게 되었다: 지능형 수소기술 혁신연구단.
- 2025-06-01 · LG에너지솔루션의 지원을 받아, 다음 과제를 수행하게 되었다: 셀 구성 물질과 상황에 따른 가스 생성 예측 개발 연구.
- 2025-04-01 · 환경부(한국환경산업기술원)의 지원을 받아, 다음 과제를 수행하게 되었다: CO2 포집-저장-활용 기술 온실가스 감축량 평가기술(주관기관: 한국화학연구원).
- 2025-02-19 · Derrick Adams 학생의 논문이 Computers & Chemical Engineering에 출판되었다.
- 2025-02-17 · 정해용 졸업생(석사), 임형묵 졸업생(박사)의 논문이 Fuel에 출판되었다.
- 2025-01-08 · 천우필 졸업생(석사)의 논문이 Korean Journal of Chemical Engineering에 출판되었다.
- 2024-12-16 · 최예찬 졸업생(박사)의 논문이 Applied Energy에 출판되었다.
- 2024-11-16 · 이재욱 학생의 논문이 Computers & Chemical Engineering에 출판되었다.
- 2024-06-01 · CJ제일제당의 지원을 받아, 다음 과제를 수행하게 되었다: 가변형 생산공정 최적화 solver 개발.
- 2024-03-01 · 우리 학과 이재우 교수가 센터장으로 계신 선도연구센터(ERC) 과제에 참여하게 되었다(과제명: 분산형 저탄소 수소생산 연구센터).
- 2023-11-15 · 김선우 학생의 논문이 Renewable and Sustainable Energy Reviews에 출판되었다.
- 2023-11-03 · 박정호 학생의 논문이 Energy Conversion and Management에 출판되었다.
- 2023-10-24 · 천우필 학생의 논문이 Journal of CO2 Utilization에 출판되었다.

## 연락과 위치

- 교수 이메일: smheo@kaist.ac.kr[^home]
- 교수 전화: +82-42-350-3920[^home][^faculty]
- 교수실: W1-3 건물 4101호[^faculty]
- 주소: 34141 대전광역시 유성구 대학로 291 KAIST 생명화학공학과[^home]
[^home]: 연구실 첫 화면, About SPEL·Contact. <https://spel.kaist.ac.kr/> 관측일 2026-11-05.
[^research]: 연구실 연구 소개. <https://spel.kaist.ac.kr/research.html> 관측일 2026-11-05.
[^storage]: 연구실 연구 소개, Electrochemical Energy Storage. <https://spel.kaist.ac.kr/research.html> 관측일 2026-11-05.
[^hydrogen]: 연구실 연구 소개, Hydrogen & Sector-Coupled Energy Systems. <https://spel.kaist.ac.kr/research.html> 관측일 2026-11-05.
[^separation]: 연구실 연구 소개, Membrane & Separation Processes. <https://spel.kaist.ac.kr/research.html> 관측일 2026-11-05.
[^design]: 연구실 연구 소개, Process Systems Synthesis & AI-Driven Design·Graph-Theoretic Co-Design and AI-Augmented Optimization. <https://spel.kaist.ac.kr/research.html> 관측일 2026-11-05.
[^faculty]: KAIST 생명화학공학과 허성민 교수 소개. <https://cbe.kaist.ac.kr/boards/view/faculty/72/1/> 관측일 2026-11-05.
[^professor]: 연구실 Professor, Education·Professional Experiences·Professional Activities. <https://spel.kaist.ac.kr/member/professor.html> 관측일 2026-11-06.
[^members]: 연구실 Current Members. <https://spel.kaist.ac.kr/member/current.html> 관측일 2026-11-06.
[^alumni]: 연구실 Alumni. <https://spel.kaist.ac.kr/member/alumni.html> 관측일 2026-11-06.
[^pubs]: 연구실 Publication, Books & Book Chapters·Journal Articles·Refereed Conference Proceedings. <https://spel.kaist.ac.kr/publication.html> 관측일 2026-11-05.
[^bibliography]: 허성민 저자 논문·책 장의 OpenAlex 등록 서지. <https://openalex.org/A5081909035> 관측일 2026-11-05.
[^projects]: 연구실 Project, 진행·종료된 정부·산업체 지원 과제. <https://spel.kaist.ac.kr/project.html> 관측일 2026-11-05.
[^news]: 연구실 News. <https://spel.kaist.ac.kr/news.html> 관측일 2026-11-05.
[^p1]: S. Park, J. Lee, S. Heo, arXiv (2024). <https://doi.org/10.48550/arxiv.2410.19886> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.19886>. 관측일 2026-11-06. 저자 소속·교신 표기 <https://arxiv.org/html/2410.19886v1>.
[^p2]: W. Chun, S. H. Lee, K. Roh, S. Heo, Korean Journal of Chemical Engineering (2025). <https://doi.org/10.1007/s11814-024-00373-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5081909035>. 관측일 2026-11-05.
[^p3]: J. Jung, J. H. Lee, W. Chung, S. Heo, IFAC-PapersOnLine (2024). <https://doi.org/10.1016/j.ifacol.2024.08.437> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5081909035>. 관측일 2026-11-05.
[^p4]: J. S. Lee 외, J. Lee, Journal of CO2 Utilization (2023). <https://doi.org/10.1016/j.jcou.2023.102613> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5081909035>. 관측일 2026-11-05.

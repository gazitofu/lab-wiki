# 뉴로모픽 재료 및 소자 연구실 (NMDL, Neuromorphic Materials and Devices Lab)

**서울대학교 공과대학 재료공학부 · 김상범 부교수**

- 분야: 뇌 모방 계산을 위한 재료·소자·회로, 아날로그 메모리 내 연산, 반도체 소자와 학습 방법의 공동 설계
- 대분야: 전기전자·반도체·광학, 소재
- 태그: 뉴로모픽 소자[^home][^p1], 산화물 반도체[^p1][^p2], 메모리 내 연산[^p1][^p5], 메모리 반도체 소자[^p3], 멤리스터[^p4], AI 반도체·가속기[^home][^p6]
- 홈페이지: <https://neuromorphic.snu.ac.kr/>
- 근거와 출처: [뉴로모픽 재료 및 소자 연구실 근거 페이지](neuromorphic-sources.md)

> 정보를 저장하는 반도체에 계산과 학습 기능을 더하고, 재료·소자·회로·학습 방법을 함께 설계하는 연구실이다.[^home][^p1][^p2]

## 무엇을 연구하나

김상범 교수가 이끄는 연구실은 뉴로모픽 컴퓨팅(신경세포와 그 연결의 정보 처리 방식을 본뜬 계산)을 위한 재료와 소자(전자 회로의 기능을 이루는 개별 부품), 계산 구조와 학습 방법을 연구한다. 새로운 메모리(정보를 저장하고 다시 읽는 장치)와 반도체 재료·소자도 주요 관심사다.[^home] 인공 신경망(연결된 계산 단위들이 정보를 주고받으며 입력과 출력의 관계를 학습하는 계산 모형)의 연결 강도를 전자 소자로 저장하고 바꾸는 인공 시냅스를 만들고, 그 소자의 실제 특성에 맞춰 학습 방법을 설계한다.[^p1][^p2]

첫째 갈래는 **산화물 반도체 시냅스와 칩 위 학습**이다. IGZO(인듐·갈륨·아연 산화물, indium gallium zinc oxide) 박막 트랜지스터(TFT, thin-film transistor; 얇은 반도체층에서 전기의 흐름을 조절하는 소자)와 커패시터(전기를 띤 입자를 분리해 전기 에너지를 저장하는 부품)를 결합해 가중치(학습 모형에서 연결 강도를 나타내는 값)를 저장한다. 전기가 새어 나가는 현상을 억제해 보존 시간을 확보하고, 가중치를 높이고 낮추는 동작과 학습 방법을 함께 맞춘다.[^p1] 실제 시냅스 배열과 별도의 뉴런 회로(신경망 계산 단위의 정보 처리 기능을 구현한 회로)를 결합해 칩 위 학습(반도체 칩에서 학습 모형의 값을 갱신하는 학습)을 수행하는 시스템으로도 이어졌다.[^p2]

둘째는 **저항 상태를 쓰는 메모리와 소재**다. 소자의 저항(전기가 흐르는 것을 방해하는 정도)을 정보 저장에 활용한다. 상변화 메모리(원자 배열의 질서가 바뀔 때 생기는 저항 차이로 정보를 저장하는 메모리)를 수직으로 쌓고 금속 라이너(구조 안쪽을 따라 형성한 금속층)를 넣어, 시간이 지나면서 저장 상태의 저항이 변하는 현상을 억제한다.[^p3] 멤리스터(전기 자극의 이력에 따라 저항이 바뀌고 그 상태를 기억하는 두 단자 소자)에서는 금속 나노클러스터(원자들이 모여 독립된 군집을 이루는 나노 구조)를 재료 안에 넣어 저항이 변하는 방식을 조절한다. 이온(전기를 띤 원자나 원자 집단)의 반응을 제어해 연결 강도를 점진적으로 높이거나 낮추는 연구다.[^p4]

셋째는 **메모리 내 연산 구조와 학습 방법**이다. 아날로그(정보를 연속적인 물리량으로 나타내는 방식) 메모리 내 연산(정보를 저장하는 장치 안이나 가까이에서 수행하는 계산)을 이용해 특징 추출과 유사도 검색을 함께 처리하는 구조를 만든다. 실제 하드웨어를 학습 과정에 넣어 기기 안에서 표현 학습을 수행하는 연구다.[^p5] 다른 축에서는 아날로그 기본 신경망에 디지털(정보를 구분된 상태로 나타내는 방식) 주의 블록(입력의 각 부분을 고려하는 비중을 조절하는 계산 부분)을 결합한다. 소자의 불완전한 동작 특성을 고려해 신경망의 학습과 전력 사용을 함께 다룬다.[^p6]

넷째는 **스파이크 기반 확률 계산**이다. 스파이크(짧은 시간 동안 발생하는 전기 신호)를 주고받는 신경망으로 볼츠만 머신(계산 단위들의 상호작용에 따라 확률적으로 상태를 바꾸며 자료의 특징을 학습하는 신경망)을 구현한다. 상변화 메모리 시냅스를 쓰는 칩에서 조합 최적화 문제를 푸는 방법을 연구했고,[^p7] 저항 변화 메모리와 문턱 스위치(일정한 전기적 문턱에 이르면 전기가 흐르는 상태로 전환되는 소자)를 직렬로 연결해 전달 지연에서 무작위성을 얻는 방법도 제안했다. 이 지연을 신경망의 학습에 활용한다.[^p8]

## 주요 연구 주제

### 1. 산화물 반도체 시냅스와 칩 위 학습

IGZO 박막 트랜지스터와 커패시터를 결합한 시냅스 소자, 저장된 연결 강도의 유지, 소자 배열과 뉴런 회로를 결합한 학습 시스템을 연구한다.[^p1][^p2]

### 2. 저항 상태를 쓰는 메모리와 소재

수직 적층 상변화 메모리에서 저장 상태의 저항 변화를 억제하고, 금속 나노클러스터를 넣은 멤리스터에서 저항 변화의 선형성을 조절한다.[^p3][^p4]

### 3. 메모리 내 연산 구조와 학습 방법

아날로그 메모리에서 특징 추출과 유사도 검색을 수행하는 계산 구조, 아날로그 신경망과 디지털 주의 블록을 결합한 학습 방법을 연구한다.[^p5][^p6]

### 4. 스파이크 기반 확률 계산

무작위성을 활용하는 신경망을 반도체 소자와 칩으로 구현해 조합 최적화와 자료 학습에 적용하고, 시냅스 지연을 무작위성의 원천으로 활용한다.[^p7][^p8]

## 대표 논문

2021–2026년 김상범 교수의 논문 가운데 서울대 재직 시기에 출판되었고 초록이 있는 여덟 편을 네 연구 갈래에 고르게 골랐다. 김상범 교수가 마지막 저자인 논문 여섯 편과 중간 저자인 공저 논문 두 편이다. "쉽게 말하면" 칸은 각 논문의 OpenAlex 등록 초록만을 근거로 썼다.[^works]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Device‐Algorithm Co‐Optimization for an On‐Chip Trainable Capacitor‐Based Synaptic Device with IGZO TFT and Retention‐Centric Tiki‐Taka Algorithm](https://doi.org/10.1002/advs.202303018) · Advanced Science | 신경망을 칩 위에서 학습시키려면 연결 강도를 원하는 만큼 바꾸고 그 값을 유지해야 한다. 트랜지스터 여섯 개와 커패시터 한 개로 구성한 IGZO 6T1C 시냅스를 제안해 연결 강도를 조절하고 보존 시간을 확보했다. 기준값의 이동과 장기 보존 손실을 보정하는 학습 방법도 함께 제안했다.[^p1] | 1저자 Jongun Won, 마지막 저자 김상범 |
| 2 | 2025 | [An Analog Neuromorphic On-Chip Training System With IGZO TFT-Based 6T1C Synaptic Memory](https://doi.org/10.1109/jssc.2025.3556123) · IEEE Journal of Solid-State Circuits | IGZO 박막 트랜지스터로 만든 시냅스 배열과 별도의 뉴런 회로를 결합한 아날로그 학습 시스템이다. 전류(단위 시간에 흐르는 전기의 양)와 커패시터 크기를 조절해 개별 시냅스와 배열의 전류를 처리했다. 이 시스템의 마지막 신경망 층을 칩 위에서 학습시켜 MNIST(Modified National Institute of Standards and Technology, 손글씨 숫자 영상 자료)에서 정확도 97.1%를 얻었다.[^p2] | 1저자 Minil Kang, 중간 저자 김상범 (8/9번째) |
| 3 | 2026 | [Vertical 3D Phase-Change Memory with Metallic Liner for Enhanced Resistance Drift Suppression](https://doi.org/10.1007/s13391-026-00655-2) · Electronic Materials Letters | 상변화 메모리는 시간이 지나면서 저장 상태의 저항이 달라져, 여러 값을 구별해 저장하는 데 어려움이 생긴다. 수직으로 적층한 메모리에 금속 라이너를 넣고 계산과 실제 제작·전기 측정으로 그 효과를 살폈다. 저장 상태의 저항 변화가 억제됨을 확인했으며, 적층 사이 전류의 영향은 별도의 단순화 모형으로 평가했다.[^p3] | 1저자 Youngsoo Choi, 마지막 저자 김상범 |
| 4 | 2022 | [Cluster-type analogue memristor by engineering redox dynamics for high-performance neuromorphic computing](https://doi.org/10.1038/s41467-022-31804-4) · Nature Communications | 멤리스터의 저항을 연속적으로 조절하려고 비정질 실리콘(원자가 규칙적으로 반복 배열되지 않은 실리콘)에 티타늄 나노클러스터를 넣었다. 이 구조는 은 이온의 환원(전자를 받는 반응)을 유도해 전기가 흐르는 정도를 선형적으로 높이고 낮출 수 있게 한다. 넣는 금속에 따라 선형성 개선 정도를 조절했고, 영상 처리 모의실험으로 시냅스 모형의 작동을 확인했다.[^p4] | 1저자 Jaehyun Kang, 중간 저자 김상범 (10/11번째) |
| 5 | 2026 | [Physically implemented analog in-memory distance computing with InGaZnO transistor-based capacitive unit](https://doi.org/10.1038/s44335-026-00091-3) · npj Unconventional Computing | 기기 안에서 환경 변화에 적응하도록, IGZO 트랜지스터 기반 커패시터 연산 단위가 특징 추출과 유사도 검색을 함께 수행하는 AIMDC(analog in-memory distance computing, 아날로그 메모리 내 거리 계산) 구조를 제안했다. 연속적인 아날로그 출력을 이용해 실제 하드웨어를 학습 과정에 넣었다. 적은 예시로 분류를 배우는 실험에서 그래픽 처리 장치와 견줄 만한 정확도를 보이고 에너지 효율(소비한 에너지에 대한 유용한 처리의 비율)은 최대 576배 개선했다.[^p5] | 1저자 Changhoon Joe, 마지막 저자 김상범 |
| 6 | 2026 | [SALMON: Self-Adaptive Learning Model on Neuromorphic Hardware](https://doi.org/10.1109/tnnls.2026.3687785) · IEEE Transactions on Neural Networks and Learning Systems | 아날로그 메모리의 불완전한 특성을 고려해 SALMON(Self-Adaptive Learning Model on Neuromorphic Hardware) 학습 방법을 제안했다. 아날로그 기본 신경망에 디지털 주의 블록을 붙여 신경망 성능을 높이는 방식이다. 소자 모형과 신경망 크기를 달리하며 CIFAR-10(대상별로 분류된 영상 자료)에서 효과를 평가했고, 학습 중 붙이는 디지털 부분의 사용을 줄이는 전략도 제시했다.[^p6] | 1저자 Young Woon Cho, 마지막 저자 김상범 |
| 7 | 2024 | [Solving Max‐Cut Problem Using Spiking Boltzmann Machine Based on Neuromorphic Hardware with Phase Change Memory](https://doi.org/10.1002/advs.202406433) · Advanced Science | 연결된 점들을 나눠 두 집단 사이 연결의 가중치 합을 최대로 만드는 최대 절단 문제를 대상으로 한다. 스파이크 기반 볼츠만 머신의 무작위 동작과 시간 구간을 활용하는 방법을 제안하고, 상변화 메모리 시냅스를 쓰는 뉴로모픽 칩에서 구현했다. 모의실험과 칩 실험으로 조합 문제를 푸는 접근을 검증했다.[^p7] | 1저자 Yu Gyeong Kang, 마지막 저자 김상범 |
| 8 | 2026 | [Stochastic sampling via synaptic delay in spiking RBMs using integrated resistive and threshold switching devices](https://doi.org/10.1039/d6nh00158k) · Nanoscale Horizons | 스파이크 기반 볼츠만 머신의 학습에 필요한 무작위성을 시냅스의 전달 지연에서 얻었다. 저항 변화 메모리와 문턱 스위치를 직렬 연결하고 저항값으로 스위치가 켜지는 지연을 조절했다. 소자 측정·회로 모형·모의실험을 연결했으며, 이 지연을 쓴 손글씨 숫자 학습은 지연이 없는 기준 방법과 난수 생성기를 쓴 구현보다 정확도가 높았다.[^p8] | 1저자 Suyeon Jang, 마지막 저자 김상범 |

## 교수와 전문 분야

김상범 교수는 서울대학교 공과대학 재료공학부 부교수다.[^faculty][^pi] 서울대학교 전기공학 학사(2001), Stanford University 전기공학 석사(2005)와 박사(2010)를 받았다. IBM Thomas J. Watson Research Center에서 박사후연구원(2010–2012), Research Staff Member(2012–2018)로 일했고, 2018년 서울대 조교수로 부임해 2022년부터 부교수로 재직하고 있다.[^members]

최근 논문으로 보면 전문 분야는 저장 소자의 특성과 신경망 학습을 연결하는 공동 설계다. IGZO 시냅스의 값 유지와 가중치 갱신, 상변화 메모리의 수직 적층, 멤리스터 재료 안에서 일어나는 반응 제어를 연구한다.[^p1][^p3][^p4] 이를 바탕으로 실제 칩에서의 학습, 메모리 안의 거리 계산, 소자의 불완전한 특성을 고려하는 학습 구조, 스파이크를 이용한 확률 계산으로 연구를 확장한다.[^p2][^p5][^p6][^p7][^p8]

## 응용 분야

기기 자체에서 학습하고 환경 변화에 적응하는 인공지능 하드웨어가 주요 응용이다. 대표 논문은 손글씨 숫자와 영상의 분류, 적은 예시를 이용한 분류 학습, 연결된 점들을 집단으로 나누는 최대 절단 문제를 대상으로 소자와 계산 방법을 평가한다.[^p2][^p5][^p6][^p7] 재료 수준의 저장 특성을 회로와 학습 방법에 연결해 인공지능 계산에 사용하는 방향이다.[^home][^p1]

## 구성원

Members의 대학원생 구획은 2026년 3월, 학부생 구획은 2026년 1월 기준이다. 대학원생 44행과 학부생 1행이며, 대학원생 구획에서 이훈로·허원준·강운현·전제현은 각각 두 번 적혀 있다. 과정은 누리집의 대학원생·학부생 구분을 따르며, 석사와 박사는 따로 구분하지 않는다.[^members]

| 이름 | 과정 |
|---|---|
| 조영운 | 대학원생 |
| 서형준 | 대학원생 |
| 강동훈 | 대학원생 |
| 윤민식 | 대학원생 |
| 진영훈 | 대학원생 |
| 장수연 | 대학원생 |
| 최원석 | 대학원생 |
| 조창훈 | 대학원생 |
| 이재상 | 대학원생 |
| 강재현 | 대학원생 |
| 한나래 | 대학원생 |
| 강민승 | 대학원생 |
| 권순완 | 대학원생 |
| 노영채 | 대학원생 |
| 최진하 | 대학원생 |
| 이성민 | 대학원생 |
| 김현우 | 대학원생 |
| 강유경 | 대학원생 |
| 박예지 | 대학원생 |
| 박재원 | 대학원생 |
| 최영수 | 대학원생 |
| 이훈로 | 대학원생 |
| 허원준 | 대학원생 |
| 강운현 | 대학원생 |
| 정세윤 | 대학원생 |
| 한동민 | 대학원생 |
| 허원준 | 대학원생 |
| 이훈로 | 대학원생 |
| 강운현 | 대학원생 |
| 김민기 | 대학원생 |
| 문현인 | 대학원생 |
| 이대규 | 대학원생 |
| 김민욱 | 대학원생 |
| 이승현 | 대학원생 |
| 송윤호 | 대학원생 |
| 최은영 | 대학원생 |
| 김종민 | 대학원생 |
| 전제현 | 대학원생 |
| 허태림 | 대학원생 |
| 전제현 | 대학원생 |
| 황현조 | 대학원생 |
| 이건희 | 대학원생 |
| 김채현 | 대학원생 |
| 이수민 | 대학원생 |
| 박홍근 | 학부생 |

## 졸업생

Members의 Alumni 구획은 2026년 3월 기준이며, 석사 5행·박사 8행·학사 6행이다. 학위와 연도는 누리집 표기다. 연도가 적힌 항목은 2021–2026년이고 학사 항목은 연도 표기가 없다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 전한솔 | 석사 (2021) |  |
| 홍상준 | 석사 (2021) |  |
| 이재상 | 석사 (2022) |  |
| 김영훈 | 석사 (2023) |  |
| 조웅 | 석사 (2024) |  |
| 신의철 | 박사 (2024) |  |
| 최세정 | 박사 (2025) |  |
| 최인혁 | 박사 (2025) |  |
| 박은표 | 박사 (2025) |  |
| 강재현 | 박사 (2025) |  |
| 변강현 | 박사 (2026) |  |
| 원종운 | 박사 (2026) |  |
| 강재현 | 박사 (2026) |  |
| 윤성원 | 학사 |  |
| 강덕영 | 학사 |  |
| 고두용 | 학사 |  |
| 정찬아 | 학사 |  |
| 이준모 | 학사 |  |
| 김형근 | 학사 |  |

## 최근 논문 목록 (2021–2026)

김상범 교수의 공개 서지에 등록된 2021–2026년 항목 46건이다. OpenAlex의 논문 유형 38건, 학회 논문 유형 5건, 사전 공개본 3건으로 구성되며, 사전 공개본은 학술지·학회명 칸에 표시했다. 연도·제목·저자·학술지와 학회 이름은 OpenAlex 등록 표기다.[^works]

**2026**

- Keonhee Lee; Hoonroe Lee; Sang‐Bum Kim. "Exact N:4 pruning and recurrent dependence: a retrospective case study in an adaptive spiking network". *Zenodo (CERN European Organization for Nuclear Research) (사전 공개본)*.
- Ye-Han Kwon; Youngchae Roh; Changhoon Joe; Sang‐Bum Kim; Sung‐Min Hong. "Impact of Channel Scaling on IGZO TFT-Based 6T1C Synaptic Cells for Analog Neuromorphic Operation". *IEEE Transactions on Electron Devices*.
- Changhoon Joe; K. Aiden. Byun; Minseung Kang; Jongun Won; Youngchae Roh; Sang‐Bum Kim. "Physically implemented analog in-memory distance computing with InGaZnO transistor-based capacitive unit". *npj Unconventional Computing*.
- Sang‐Bum Kim. "Building a Memory Hierarchy for Analog Compute-in-Memory through Device–Algorithm Co-Optimization". *Neuronics Conference*.
- Youngsoo Choi; Wonseok Choi; Jinha Choi; Dongmin Han; Donghoon Kang; Sang‐Bum Kim. "Vertical 3D Phase-Change Memory with Metallic Liner for Enhanced Resistance Drift Suppression". *Electronic Materials Letters*.
- Young Woon Cho; Sungmin Lee; Sang‐Bum Kim. "SALMON: Self-Adaptive Learning Model on Neuromorphic Hardware". *IEEE Transactions on Neural Networks and Learning Systems*.
- JinGyeong Hwang; Jaesang Lee; Jiin Bang; Younghyun Lee; Unhyeon Kang; Seungmin Oh; Kyungmin Lee; Jaehyun Park; Seongsik Park; Hyun Jae Jang; Sang‐Bum Kim; Min Hi Park Min Hi Park; Suyoun Lee. "Neuronal arithmetic operators based on Ovonic threshold switches (OTS) for biologically inspired analog computing". *arXiv (Cornell University) (사전 공개본)*.
- Sejeung Choi; J H Choi; Sang‐Bum Kim. "Co-Design of 3D Vertical Phase-Change Memory Crossbars and Mixer Architecture for Analog In-Memory Computing". *IEEE Electron Devices Technology & Manufacturing Conference (EDTM)*.
- Suyeon Jang; Dae Kyu Lee; Uicheol Shin; Yu Gyeong Kang; Youngsoo Choi; Dongmin Han; Joon Young Kwak; Sang‐Bum Kim. "Stochastic sampling via synaptic delay in spiking RBMs using integrated resistive and threshold switching devices". *Nanoscale Horizons*.
- Jinha Choi; Hansol Jun; Minseung Kang; Sang‐Bum Kim. "Battery-Physics-Inspired Interfacial Mechanisms Analysis of Programming Nonidealities in Electrochemical Random Access Memory". *SSRN Electronic Journal (사전 공개본)*.

**2025**

- Unhyeon Kang; Jae Sang Lee; Seungmin Oh; Hanchan Song; Jongkil Park; Jaewook Kim; Seongsik Park; Hyun Jae Jang; Sang‐Bum Kim; Su‐in Yi; Suhas Kumar; Suyoun Lee. "Ovonic Switches Enable Energy-Efficient Dendrite-like Computing". *Nano Letters*.
- Sungmin Lee; Hyunin Moon; Minsik Yoon; Wonjun Heo; Sang‐Bum Kim. "SOLO: Spatial online learning at once for spiking neural networks". *Neurocomputing*.
- Jaehyun Kang; Sungmin Lee; Tae-Yoon Kim; Suman Hu; Suyoun Lee; Kyeong‐Seok Lee; Jong‐Keuk Park; In Ho Kim; Gyu Weon Hwang; Sang‐Bum Kim; YeonJoo Jeong. "Achieving Low‐Power Analog Resistive Switching in Filamentary Memristive Devices for Energy‐Efficient Analog In‐Memory Computing". *Small*.
- Narae Han; Youngchae Roh; Ha‐Jun Sung; Minseung Kang; Jongun Won; Joo-Hun Han; Younjin Jang; Jee-Eun Yang; Sang‐Wook Kim; Sang‐Bum Kim. "Enhancement of On-Current and Reliability in InGaZnO Thin-Film Transistors for Synaptic Circuit Applications through Gate Insulator Stack Engineering". *ACS Applied Materials & Interfaces*.
- Jaehyeon Kang; Sangjun Hong; Sangwook Kim; Sang‐Bum Kim. "Selective Update for Hardware‐Friendly On‐Chip Training in Distributed Analog In‐Memory Computing Systems". *Advanced Intelligent Systems*.
- Hyeong Jun Seo; Kanghyeon Byun; Minseung Kang; Youngchae Roh; Changhoon Joe; Sang‐Bum Kim. "Ternary Content Addressable Memory with In–Ga–Zn–O Thin‐Film Transistor Technology for Enhanced Uniformity and Endurance in Efficient Distance‐Based Algorithm Acceleration". *Advanced Intelligent Systems*.
- Ye-Han Kwon; Youngchae Roh; Changhoon Joe; Sang‐Bum Kim; Sung‐Min Hong. "Numerical Investigation of Electrical Performance and Scaling Properties in 6T1C IGZO-Based Synaptic Devices". *Silicon Nanoelectronics Workshop (SNW)*.
- Jaehyeon Kang; Jongun Won; Narae Han; Sangjun Hong; Jee‐Eun Yang; Sangwook Kim; Sang‐Bum Kim. "Disturbance‐Aware On‐Chip Training with Mitigation Schemes for Massively Parallel Computing in Analog Deep Learning Accelerator". *Advanced Science*.
- Minil Kang; Minseong Um; Jongun Won; Jaehyeon Kang; Sangjun Hong; Narae Han; Sangwook Kim; Sang‐Bum Kim; Hyung‐Min Lee. "An Analog Neuromorphic On-Chip Training System With IGZO TFT-Based 6T1C Synaptic Memory". *IEEE Journal of Solid-State Circuits*.
- Sejeung Choi; Sang‐Bum Kim. "V-PCMixer: incorporating 3D vertical phase-change memory based analog in-memory computing in mixer architecture". *Nanoscale*.
- Minseung Kang; Mingi Kim; Jaehyeon Kang; Jongun Won; Hyeong Jun Seo; Changhoon Joe; Youngchae Roh; Yeaji Park; Sang‐Bum Kim. "Enabling Selective and Tunable Weight Updates in All-InGaZnO 3-Transistor 1-Capacitor Synaptic Circuits for On-Chip Training". *IEEE Journal of the Electron Devices Society*.

**2024**

- Hyunwoo Kim; Suyeon Jang; Uicheol Shin; Masatoshi Ishii; Atsuya Okazaki; Megumi Ito; Akiyo Nomura; Kohji Hosokawa; Sungmin Lee; Matthew J. BrightSky; Sang‐Bum Kim. "Energy‐Efficient Hardware Implementation of Spiking‐Restricted Boltzmann Machines Using Pseudo‐Synaptic Sampling". *Advanced Intelligent Systems*.
- Yu Gyeong Kang; Masatoshi Ishii; Jaeweon Park; Uicheol Shin; Suyeon Jang; Seongwon Yoon; Mingi Kim; Atsuya Okazaki; Megumi Ito; Akiyo Nomura; Kohji Hosokawa; Matthew J. BrightSky; Sang‐Bum Kim. "Solving Max‐Cut Problem Using Spiking Boltzmann Machine Based on Neuromorphic Hardware with Phase Change Memory". *Advanced Science*.
- Dae Kyu Lee; Gichang Noh; Seungmin Oh; Yooyeon Jo; Eunpyo Park; Min Jee Kim; Dong Yeon Woo; Heerak Wi; YeonJoo Jeong; Hyun Jae Jang; Sang‐Bum Kim; Suyoun Lee; Kibum Kang; Joon Young Kwak. "Crystallinity‐controlled volatility tuning of ZrO 2 memristor for physical reservoir computing". *InfoMat*.
- Sejeung Choi; Sang‐Bum Kim. "In-Series Phase-Change Memory Pair for Enhanced Data Retention and Large Window in Automotive Application". *IEEE Electron Device Letters*.
- Minseung Kang; Ung Cho; Jaehyeon Kang; Narae Han; Hyeong Jun Seo; Jee‐Eun Yang; Seokyeon Shin; Taehyun Kim; Sangwook Kim; Changwook Jeong; Sang‐Bum Kim. "Field Induced Off‐State Instability in InGaZnO Thin‐Film Transistor and its Impact on Synaptic Circuits". *Advanced Electronic Materials*.
- Minil Kang; Minseong Um; Jongun Won; Jaehyeon Kang; Sangjun Hong; Narae Han; Sangwook Kim; Sang‐Bum Kim; Hyung‐Min Lee. "An Analog Neuromorphic On-Chip Training System with IGZO TFT-Based 6T1C 367-State Synaptic Memory Achieving 0.99-R2 Linearity and 104-Times Enhanced Retention Time". *Custom Integrated Circuits Conference*.
- Ji Hyun Baek; In Hyuk Im; Eun‐Mi Hur; Jungwon Park; Jongwoo Lim; Sang‐Bum Kim; Kibum Kang; Soo Young Kim; Jae Yong Song; Ho Won Jang. "Artificial synaptic devices based on biomimetic electrochemistry: A review". *Materials Research Bulletin*.
- Eunpyo Park; Dong Yeon Woo; Gichang Noh; Yooyeon Jo; Dae Kyu Lee; Jongkil Park; Jaewook Kim; YeonJoo Jeong; Seongsik Park; Hyun Jae Jang; Nakwon Choi; Sang‐Bum Kim; Joon Young Kwak. "IGZO charge trap flash device for reconfigurable logic functions". *Applied Physics Letters*.

**2023**

- Eunpyo Park; Suyeon Jang; Gichang Noh; Yooyeon Jo; Dae Kyu Lee; In Soo Kim; Hyun‐Cheol Song; Sang‐Bum Kim; Joon Young Kwak. "Indium–Gallium–Zinc Oxide-Based Synaptic Charge Trap Flash for Spiking Neural Network-Restricted Boltzmann Machine". *Nano Letters*.
- Jongun Won; Jaehyeon Kang; Sangjun Hong; Narae Han; Minseung Kang; Yeaji Park; Youngchae Roh; Hyeong Jun Seo; Changhoon Joe; Ung Cho; Minil Kang; Minseong Um; Kwanghee Lee; Jee‐Eun Yang; Moonil Jung; Hyung‐Min Lee; Saeroonter Oh; Sangwook Kim; Sang‐Bum Kim. "Device‐Algorithm Co‐Optimization for an On‐Chip Trainable Capacitor‐Based Synaptic Device with IGZO TFT and Retention‐Centric Tiki‐Taka Algorithm". *Advanced Science*.
- Jongun Won; Youngchae Roh; Minseung Kang; Yeaji Park; Jaehyeon Kang; Hyeong Jun Seo; Changhoon Joe; Sang‐Bum Kim. "A Capacitor-Based Synaptic Device with IGZO Access Transistors for Neuromorphic Computing". *ECS Transactions*.

**2022**

- Junmo Lee; Joon Hwang; Youngwoon Cho; Minkyu Park; Woo Young Choi; Sang‐Bum Kim; Jong‐Ho Lee. "CRUS: A Hardware-Efficient Algorithm Mitigating Highly Nonlinear Weight Update in CIM Crossbar Arrays for Artificial Neural Networks". *IEEE Journal on Exploratory Solid-State Computational Devices and Circuits*.
- Kanghyeon Byun; Inhyuk Choi; Soonwan Kwon; Younghoon Kim; Donghoon Kang; Young Woon Cho; Seung Keun Yoon; Sang‐Bum Kim. "Recent Advances in Synaptic Nonvolatile Memory Devices and Compensating Architectural and Algorithmic Methods Toward Fully Integrated Neuromorphic Chips". *Advanced Materials Technologies*.
- Jongmin Park; Tae‐Hyeon Kim; Osung Kwon; Muhammad Ismail; Chandreswar Mahata; Yoon Kim; Sang‐Bum Kim; Sungjun Kim. "Implementation of convolutional neural network and 8-bit reservoir computing in CMOS compatible VRRAM". *Nano Energy*.
- Hyunjoon Lee; Da Gil Ryu; Giho Lee; Min‐Kyu Song; Hyungjin Moon; Jaehyeong Lee; Jongchan Ryu; Ji‐Hoon Kang; Jun Min Suh; Sang‐Bum Kim; Jongwoo Lim; Dongsuk Jeon; Seyoung Kim; Jeehwan Kim; Yun Seog Lee. "Vertical Metal‐Oxide Electrochemical Memory for High‐Density Synaptic Array Based High‐Performance Neuromorphic Computing". *Advanced Electronic Materials*.
- Jaehyun Kang; Tae-Yoon Kim; Suman Hu; Jaewook Kim; Joon Young Kwak; Jongkil Park; Jong‐Keuk Park; Inho Kim; Suyoun Lee; Sang‐Bum Kim; YeonJoo Jeong. "Cluster-type analogue memristor by engineering redox dynamics for high-performance neuromorphic computing". *Nature Communications*.
- Uicheol Shin; Masatoshi Ishii; Atsuya Okazaki; Megumi Ito; Malte J. Rasch; Wanki Kim; Akiyo Nomura; Wonseok Choi; Dooyong Koh; Kohji Hosokawa; Matthew J. BrightSky; Seiji Munetoh; Sang‐Bum Kim. "Pattern Training, Inference, and Regeneration Demonstration Using On‐Chip Trainable Neuromorphic Chips for Spiking Restricted Boltzmann Machine". *Advanced Intelligent Systems*.
- Eunpyo Park; Jae Eun Seo; Gichang Noh; Yooyeon Jo; Dong Yeon Woo; In Soo Kim; Jongkil Park; Jaewook Kim; YeonJoo Jeong; Suyoun Lee; Inho Kim; Jong‐Keuk Park; Sang‐Bum Kim; Jiwon Chang; Joon Young Kwak. "A pentagonal 2D layered PdSe 2 -based synaptic device with a graphene floating gate". *Journal of Materials Chemistry C*.
- Jaesang Lee; Seong Won Cho; Young Woong Lee; Joon Young Kwak; Jaewook Kim; YeonJoo Jeong; Gyu Weon Hwang; Seongsik Park; Sang‐Bum Kim; Suyoun Lee. "Rational engineering of a switching material for an Ovonic threshold switching (OTS) device with mitigated electroforming". *Journal of Materials Chemistry C*.

**2021**

- Deokyoung Kang; Suyeon Jang; Sejeung Choi; Sang‐Bum Kim. "1/ f noise in amorphous Sb 2 Te 3 for energy-efficient stochastic synapses in neuromorphic computing". *Semiconductor Science and Technology*.
- Jaehyun Kim; Donghoon Kang; Sang‐Bum Kim; Ho Won Jang. "Catalyze Materials Science with Machine Learning". *ACS Materials Letters*.
- Yangho Jeong; Hyunjoon Lee; Da Gil Ryu; Seong Ho Cho; Ga‐Won Lee; Sang‐Bum Kim; Seyoung Kim; Yun Seog Lee. "Elucidating Ionic Programming Dynamics of Metal‐Oxide Electrochemical Memory for Neuromorphic Computing". *Advanced Electronic Materials*.
- Inhyuk Choi; Sang‐Bum Kim. "Simulation-based analysis of novel phase change memory structure with separated program and read paths for low program current and endurance enhancement". *Materials Science in Semiconductor Processing*.
- Young‐Seok Kim; Soon‐Cheon Seo; Paul C. Jamison; Steven P. Consiglio; H. Higuchi; Hiroyuki Miyazoe; Paul Michael Solomon; Sang‐Bum Kim; Tayfun Gokmen; Kandabara Tapily; Robert D. Clark; Takaaki Tsunomura; Cory S. Wajda; Wilfried Hänsch; Robert J. Soave; Gert J. Leusink; Vijay Narayanan; Takashi Ando. "Hardware Algorithm Co-optimization on Resistive RAM Cross-bar Array for Scalable Analog Compute Technology for AI application". *학술지·학회명 표기 없음*.
- Sol‐Kyu Lee; Young Woon Cho; Jong‐Sung Lee; Young‐Ran Jung; Seung‐Hyun Oh; Jeong‐Yun Sun; Sang‐Bum Kim; Young‐Chang Joo. "Nanofiber Channel Organic Electrochemical Transistors for Low‐Power Neuromorphic Computing and Wide‐Bandwidth Sensing Platforms". *Advanced Science*.

## 연락과 위치

- 교수 업무 이메일: sangbum.kim@snu.ac.kr[^home]
- 위치(Mailstop): 33-110[^pi]
- 전화: 880-7359[^pi]
- 소속 주소: 서울특별시 관악구 관악로 1 서울대학교 공과대학 재료공학부[^pi]

## 각주
[^home]: NMDL, Home, 연구실 이름·Main research interests·업무 이메일. <https://neuromorphic.snu.ac.kr/> (열람 2026-10-31).

[^members]: NMDL, Members, 교수 학력·경력, Graduate students·Undergraduate students·Alumni 구획. <https://neuromorphic.snu.ac.kr/members> (열람 2026-10-31).

[^faculty]: 서울대학교 재료공학부, Faculty, 김상범 교수 카드. <https://mse.snu.ac.kr/snumse-main/people/professors/> (열람 2026-10-31).

[^pi]: 서울대학교 재료공학부, 김상범 교수 소개, Associate Professor·Education·Career·Mailstop·Phone. <https://mse.snu.ac.kr/kim-sangbum/> (열람 2026-10-31).

[^works]: OpenAlex, ORCID 0000-0001-7460-3750 저자 기록의 2021–2026년 출판물과 등록 초록. <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p1]: J. Won 외, S.-B. Kim, Advanced Science (OpenAlex 등록 연도 2023). <https://doi.org/10.1002/advs.202303018> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p2]: M. Kang 외, H.-M. Lee, IEEE Journal of Solid-State Circuits (OpenAlex 등록 연도 2025). <https://doi.org/10.1109/jssc.2025.3556123> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p3]: Y. Choi 외, S.-B. Kim, Electronic Materials Letters (OpenAlex 등록 연도 2026). <https://doi.org/10.1007/s13391-026-00655-2> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p4]: J. Kang 외, Y. Jeong, Nature Communications (OpenAlex 등록 연도 2022). <https://doi.org/10.1038/s41467-022-31804-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p5]: C. Joe 외, S.-B. Kim, npj Unconventional Computing (OpenAlex 등록 연도 2026). <https://doi.org/10.1038/s44335-026-00091-3> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p6]: Y. W. Cho, S. Lee, S.-B. Kim, IEEE Transactions on Neural Networks and Learning Systems (OpenAlex 등록 연도 2026). <https://doi.org/10.1109/tnnls.2026.3687785> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p7]: Y. G. Kang 외, S.-B. Kim, Advanced Science (OpenAlex 등록 연도 2024). <https://doi.org/10.1002/advs.202406433> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

[^p8]: S. Jang 외, S.-B. Kim, Nanoscale Horizons (OpenAlex 등록 연도 2026). <https://doi.org/10.1039/d6nh00158k> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.orcid:0000-0001-7460-3750,publication_year:2021-2026> (열람 2026-10-31).

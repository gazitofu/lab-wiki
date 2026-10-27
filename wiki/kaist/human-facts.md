# 인적 요소 중심 교통 안전 연구실 (Human Factors Centered Transport Safety Laboratory, Human-FACTS)

**KAIST 조천식모빌리티대학원 · Tiantian (Nicole) Chen 부교수**

- 분야: 사람 중심 교통안전, 운전자 행동, 통행 선택, 사람과 차량의 상호작용[^home][^prof]
- 대분야: 건설·도시·인프라, 컴퓨팅·AI
- 태그: 교통·도시 계획[^r2][^p3][^p4], 자율주행[^r1][^r4], 대형 언어 모델[^r4][^p2][^p5], 인간–컴퓨터 상호작용[^r4][^p2], 멀티모달 AI[^r4]
- 홈페이지: <https://human-facts.kaist.ac.kr/>

> 사람의 판단과 행동을 중심에 놓고 교통사고 위험을 분석하며, 운전 시뮬레이션·통행 선택 분석·언어 모델 기반 차량 보조를 연구한다.[^home][^r1][^r2][^r3][^r4]

## 무엇을 연구하나

이 연구실은 운전자가 경고를 어떻게 받아들이고, 어떤 교통수단과 경로를 선택하며, 보행자와 차량이 어떤 상황에서 충돌 위험에 놓이는지를 연구한다. 사람의 능력·판단·행동을 기술 및 환경과 함께 살피는 인적 요소 연구를 교통안전과 연결하는 접근이다. 운전 행동, 통신으로 연결된 차량과 자율주행차, 교통안전, 교통정책이 연구 범위에 들어간다.[^home][^r1][^r2][^r3]

첫째는 운전 시뮬레이션(운전 상황을 모의 환경으로 재현하는 방법)을 통한 행동 분석이다. 차량이 주변 차량·도로 설비 등과 정보를 주고받는 C-V2X(Cellular Vehicle-to-Everything) 환경에서 통신 이상이 사람의 운전 판단에 미치는 영향을 살핀다. 대표 논문은 신호 교차로에서 멈출지 지나갈지를 결정하는 행동을 분석했다. 통신이 상실되면 통신 정보가 없는 경우보다 교차로를 통과하려는 경향이 커졌고, 원활한 통신과 일시적으로 중단된 통신에서는 그 경향이 대체로 줄었다. 이러한 결과를 바탕으로 통신 정보의 제공 방식과 운전자의 반응을 함께 고려한다.[^r1][^p1]

둘째는 통행 수단과 경로의 선택이다. 서로 다른 교통수단을 연계하는 이동 환경에서 개인에게 맞는 경로를 제안하고, 운전자의 과속 억제 정책이나 대중교통·항공 이동의 선택을 분석한다. 경로 추천 연구에서는 LLM(Large Language Model, 글을 이해하고 생성하도록 많은 언어 자료로 학습한 인공지능 모델)과 RAG(Retrieval-Augmented Generation, 관련 자료를 검색해 생성 모델의 응답에 활용하는 방법)를 결합한다. 실시간 교통 정보, 이용자 특성, 도로 상황을 함께 고려해 개인의 선호와 상황에 맞는 안내를 목표로 한다.[^r2]

셋째는 교통사고 위험을 자료와 모형으로 설명하는 일이다. 실제 사고를 기다리는 대신 교통 상충(충돌로 이어질 수 있는 교통 참여자 사이의 상황)을 분석하고, 충돌 직전의 위험을 나타내는 대리 지표를 사용한다. 사고 위험 분석에서는 기계학습(자료에서 규칙이나 관계를 학습하는 계산 방법)으로 비정상적인 상충을 찾고, 극단값 이론(확률분포의 극단 영역에서 나타나는 사건을 다루는 통계 이론)으로 사고 빈도를 추정한다. 거리 사진에서는 도로의 물리적 특성과 사람이 느끼는 거리의 인상을 함께 살펴 안전을 고려한 거리 계획과 연결한다.[^r3]

넷째는 언어 모델을 이용한 사람과 차량의 소통이다. 자율주행차의 탑승자뿐 아니라 주변 운전자·보행자까지 고려해, 사람이 원하는 바를 차량이 이해하고 차량의 판단을 사람이 이해할 수 있도록 설명하는 인터페이스(사람이 기기와 정보를 주고받는 접점)를 연구한다. 개인별 운전 보조에서는 VLM(Vision Language Model, 영상과 언어 정보를 함께 다루는 인공지능 모델)을 포함한 여러 종류의 정보 처리를 차량 내 보조 프로그램과 결합해 위험을 인식하고 운전자에게 맞는 경고와 대화를 제공하는 방향을 제시한다.[^r4]

## 주요 연구 주제

### 1. 운전 시뮬레이션과 교통 참여자 사이의 안전

통신으로 연결된 차량의 운전 행동, 고령 운전자용 보조 시스템, 택시·트럭 운전자의 주의 분산과 피로, 자율주행차와 보행자·자전거·전동킥보드 이용자의 상호작용이 대상이다. 연구 소개는 여러 교통수단과 가상현실(컴퓨터로 만든 환경을 경험하게 하는 기술)을 결합한 실험 플랫폼 개발을 제시한다.[^r1]

### 2. 통행 수단·경로 선택과 교통정책

개인별 경로 추천, 직업 운전자의 단속·벌점 정책에 대한 선택, 대중교통 수단 선택, 감염병 유행기의 항공 이동, 자율주행 서비스의 이용자 수용성을 다룬다. 이용자가 새 이동 서비스를 실제로 어떻게 받아들이는지를 분석해 교통서비스 설계와 연결한다.[^r2] 대표 논문 4는 홍콩 이용자의 대중교통 선택과 방역조치에 대한 선호를 설문과 선택 모형으로 분석했다.[^p4]

### 3. 사고 위험 분석과 거리 환경

사고 직전 상황을 나타내는 안전 대리 지표, 거리 사진에 나타난 환경과 사람의 인식, 도로 특성과 사고의 통계적 관계, 드문 사고 자료의 불균형을 다룬다. 생성 모형(자료의 분포를 학습해 새 자료를 만들어 내는 계산 모형)으로 사고 자료를 생성하는 연구도 소개한다.[^r3] 대표 논문 3은 거리 경관에 대한 인식과 사고의 관계를 공간적으로 분석하고, 대표 논문 6은 보행자와 차량이 서로의 움직임과 위험을 고려하는 행동을 모형화한다.[^p3][^p6]

### 4. 언어 모델 기반 차량 인터페이스와 개인별 보조

언어 모델로 사람의 상태·의도와 차량의 신호를 해석하고, 차량의 판단을 설명하며, 운전자와 상황에 맞춘 경고를 제공하는 연구다. 사람과 기기의 의사소통·신뢰·사용 경험을 연구 대상으로 삼고, 영상과 언어를 함께 활용하는 차량 내 보조 프로그램을 개발하는 방향이다.[^r4] 대표 논문 2와 5는 운전자 특성과 교통 상황을 해석해 개인별 경고를 만드는 언어 모델 기반 시스템을 제안한다.[^p2][^p5]

## 대표 논문

2021–2026년 목록 가운데 Tiantian Chen 교수의 KAIST 재직 시기인 2024–2025년 논문 6편을 운전 시뮬레이션·통행 선택·사고 위험·차량 인터페이스 갈래에 걸쳐 골랐다. 아래의 "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 표의 연도는 랩 목록의 연도이며, 4번은 랩 목록이 2024년, OpenAlex 기록이 2023년으로 적는다.[^prof][^journals][^conferences][^p4]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 저자 참여 |
|---|---|---|---|---|
| 1 | 2025 | [How do the drivers react to different C-V2X-based communication conditions in dilemma zones? A driving simulator study](https://doi.org/10.1016/j.aap.2025.108208) · Accident Analysis & Prevention | 신호 교차로에서 차량 통신 정보가 운전자의 정지·통과 판단과 적색 신호 통과에 어떤 영향을 주는지 운전 모의실험으로 분석했다. 통신이 상실되면 정보가 없는 경우보다 교차로를 통과하려는 경향이 커졌고, 원활한 통신과 일시적으로 중단된 통신은 대체로 그 경향을 줄였다. 통신 상태와 운전 이력을 함께 고려하는 정보 제공의 필요성을 보여 준다.[^p1] | 첫째 저자 Shi Ye, 둘째 저자 Tiantian Chen |
| 2 | 2025 | [Personalizing Driver Agent Using Large Language Models for Driving Safety and Smarter Human–Machine Interactions](https://doi.org/10.1109/MITS.2025.3551736) · IEEE Intelligent Transportation Systems Magazine | 운전자마다 위험을 알아보는 능력과 원하는 경고 방식이 다르다는 점에서 출발해, 언어 모델 기반 개인별 운전 보조 프로그램을 만들었다. 기억·지각·제어·행동 기능을 갖춘 구조로 시각·음성·촉각 경고를 제공한다. 실험에서는 서로 다른 운전자와 상황에 맞춰 경고 내용을 조정하는 결과를 보였다.[^p2] | 첫째 저자 Zixuan Xu, 둘째 저자 Tiantian Chen |
| 3 | 2025 | [Is there an emotional dimension to road safety? A spatial analysis for traffic crashes considering streetscape perception and built environment](https://doi.org/10.1016/j.amar.2025.100374) · Analytic Methods in Accident Research | 거리의 물리적 환경뿐 아니라 사람이 거리에서 느끼는 인상이 사고와 어떤 관계가 있는지 분석했다. 대전의 사고·거리 사진·도로망·시설 자료를 결합하고, 장소에 따른 차이를 고려하는 통계 모형으로 경관 인식과 사고를 함께 살폈다. 경관 인식과 경상 사고 건수의 관계가 장소에 따라 달랐으며, 거리 정비 때 안전을 살펴볼 구간을 찾는 데 결과를 활용했다.[^p3] | 첫째 저자 Yiping Liu, 둘째 저자 Tiantian Chen |
| 4 | 2024 | [Effects of proactive and reactive health control measures on public transport preferences of passengers–A stated preference study during the COVID-19 pandemic](https://doi.org/10.1016/j.tranpol.2023.11.011) · Transport Policy | 감염병 유행기에 방역조치가 대중교통 수단 선택과 어떻게 연결되는지 홍콩 이용자의 설문으로 분석했다. 후회에 기반한 선택 모형을 사용해 이용자 특성·통행 특성과 선호의 관계를 살폈다. 이용자는 방역조치를 대체로 긍정적으로 평가했지만 선택에 미치는 영향은 제한적이어서, 교통수단에 맞춰 선별적으로 활용할 필요가 있다고 제시했다.[^p4] | 첫째 저자 Tiantian Chen, 마지막 저자 N.N. Sze |
| 5 | 2024 | [A LLM-based Multimodal Warning System for Driver Assistance](https://doi.org/10.1109/ITSC58415.2024.10919879) · IEEE ITSC 2024 | 운전자별로 필요한 경고 내용과 전달 방식을 정하는 언어 모델 기반 시스템 LLM-MW를 제안했다. 교통 환경과 운전자 특성을 해석해 여러 방식의 경고를 계획하고 전달한다. 실험에서는 서로 다른 운전자와 상황에 맞는 경고를 제공하는 개인화 결과를 보였다.[^p5] | 첫째 저자 Zixuan Xu, 둘째 저자 Tiantian Chen |
| 6 | 2025 | [Modelling pedestrian-vehicle interaction behaviours at non-signalised crosswalks using a game theory approach incorporating the risk perception](https://doi.org/10.1080/23249935.2025.2479084) · Transportmetrica A: Transport Science | 신호가 없는 횡단보도에서 보행자와 차량이 느끼는 위험과 서로의 움직임을 함께 분석했다. 심리학 이론과 학습 모형으로 위험 인식을 수량화하고, 게임 이론(서로의 선택이 각자의 결과에 영향을 주는 상황을 분석하는 수학 이론)으로 상호작용 행동을 모형화했다. 현장 관측 자료로 예측을 평가하고 다른 무신호 횡단보도에서 모형의 적응성도 시험했다.[^p6] | 첫째 저자 Tao Li, 마지막 저자 Tiantian Chen |

## 교수와 전문 분야

Tiantian (Nicole) Chen은 조천식모빌리티대학원 부교수다. 연구실 교수 소개는 2022년 10월부터 KAIST 부교수로 재직한다고 적는다. 그전에는 Centre for Advances in Reliability and Safety에서 선임연구원으로, The Hong Kong Polytechnic University에서 박사후연구원으로 일했다. 2014년 Zhejiang Gongshang University 환경과학 학사, 2015년 Hong Kong University of Science & Technology 환경보건안전 석사, 2021년 The Hong Kong Polytechnic University 토목·환경공학 박사 학위를 받았다.[^prof][^dept]

교수 소개가 제시하는 전문 분야는 인적 요소와 사람·기기 상호작용, 교통안전, 운전 시뮬레이션과 디지털 트윈 플랫폼, 통행 행동 분석, 계량경제 및 인공지능 모형이다. 디지털 트윈은 관측 자료와 연결해 실제 대상의 상태를 반영하는 디지털 모형이다. 계량경제 모형은 경제·사회 현상에서 변수 사이의 관계를 자료와 통계로 분석하는 모형이다. 연구 소개의 통행 선택 분석, 사고 위험 분석, 개인별 운전 보조가 이 전문 분야를 구체화한다.[^prof][^r2][^r3][^r4]

학술 활동으로는 Case Studies on Transport Policy 편집, 교통 관련 학술지의 특별호 편집, World Transport Convention 및 IEEE Emerging Transportation Technology Testing 기술위원회 활동 등이 교수 소개에 올라 있다. 2026년 소식에는 Analytic Methods in Accident Research의 Associate Editor로 선임됐다는 내용이 있다.[^prof][^n243]

## 응용 분야

운전 보조 시스템과 차량 내 경고 설계, 고령 운전자와 직업 운전자 안전, 보행자·자전거 등 여러 교통 참여자가 함께 이용하는 도로의 안전 평가, 이용자의 선호를 반영한 경로 추천과 대중교통 정책, 사고 위험을 고려한 거리 계획에 연구를 연결한다.[^r1][^r2][^r3][^r4] 최근 과제는 사람 중심 자율주행 인공지능과 여러 차량을 감독하는 원격 운전의 안전을 대상으로 한다.[^n244]

## 구성원

2026년 10월 26일 누리집의 박사과정 8명, 석사과정 4명, Visiting Students 3명과 Internship의 현 인턴 2명이다. 방문 학생과 인턴은 원문 구분을 유지했다. Neha Sengar의 이름 옆에는 "RA - The Robotics Program"이 함께 적혀 있다. 방문 학생의 괄호 안 기간은 누리집의 방문 기간이다.[^phd][^ms][^visiting][^intern] "대표 논문 참여"는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Shi Ye | 박사과정 | Driving behavior, driving simulator experiments Driving safety, human factors in connected environment Applications of statistical models | ye.shi@kaist.ac.kr | 1 |
| Zixuan Xu | 박사과정 | Generative AI (LLM, VLM) Human-Machine Interaction (HMI) in Autonomous Vehicles Human Factors AI Trustworthiness | zixuan.xu@kaist.ac.kr | 2, 5 |
| Yukai Wang | 박사과정 | Traffic safety Traffic conflict Data analysis Autonomous Driving | yukai@kaist.ac.kr |  |
| Yiping Liu | 박사과정 | Advanced Modeling in Traffic Safety Travel Behavior Large Language Model in Mobility | yiping.liu@kaist.ac.kr | 3 |
| Xiaoyu(Raina) Shi | 박사과정 | Reinforcement learning Vehicle trajectory optimization | raina0414@kaist.ac.kr |  |
| Chengxi Hu | 박사과정 | Low-carbon oriented traffic management and control Human-vehicle interaction behavior modeling Autonomous driving taxonomy and terminology | chengxi.hu43@kaist.ac.kr | 6 |
| Caiyin Dong | 박사과정 | Traffic Safety Travel Behavior Analysis Trajectory Prediction | cydongst@kaist.ac.kr |  |
| Neha Sengar （RA - The Robotics Program） | 박사과정 | Autonomous Vehicle Vision and Perception Intelligent Surveillance | neha.sengar@kaist.ac.kr |  |
| Shovon Munshi | 석사과정 | Transportation safety AI & Data Science |  |  |
| Yang Cao | 석사과정 | Large language models in mobility Human factors in transportation: fatigue, EEG-based physiological monitoring Low-altitude aviation and UAV safety | chadcao@kaist.ac.kr |  |
| Yegi Yoo | 석사과정 | Crowd dynamics, Traffic safety | yegi.yoo@kaist.ac.kr |  |
| Sohyeong Bae | 석사과정 | Traffic safety Human behavior | hg1350@kaist.ac.kr |  |
| Yuanyuan BU | 방문 학생 (2026.10-2026.12) | Cross-border driving safety assistant Human factors in transportation |  |  |
| Huijie Ouyang | 방문 학생 (2026–2027) | Pedestrian safety Pedestrian-vehicles interaction Data mining |  |  |
| Qianfang Wang | 방문 학생 (2025-2026) | Driving behavior and safety Human-machine interaction Data Mining |  |  |
| Lunar Sebastian Widjaja | 학부 인턴 |  | lunarwidjaja@kaist.ac.kr |  |
| Seungheon Lee | 학부 인턴 |  |  |  |

## 졸업생과 이전 구성원

2026년 10월 26일 Alumni 페이지의 5명과 Internship 페이지의 Previous Intern 2명이다. 학위·연도는 누리집에 적힌 것만 표시했다.[^alumni][^intern]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Huimin Tang |  |  |
| Yunjie Ju |  |  |
| Sangmi Kang | MS (2026) |  |
| Suji Lim | MS (2026) |  |
| Songmi Paek | M.S. |  |
| Seohyun Baik | previous intern |  |
| Aow Si Li Sara (Julia) | Previous Intern |  |

## 최근 논문 목록 (2021–2026)

Journal 게시판의 2021–2026년 게시 항목 가운데 46개와 Conference 게시판의 같은 연도 구역 6개를 담은 목록이다. 학술지 논문뿐 아니라 학회 발표·사전 공개본과 「Safety of professional drivers in Hong Kong」 항목도 게시판 구분대로 포함한다. 같은 제목의 반복 게시도 누리집 표기다. Conference의 TRB Annual Meeting 2025 두 항목은 누리집의 Year가 2024라 2024년 구역에 두었다. 교수의 KAIST 부임은 2022년 10월이며, 이 목록에는 부임 전 항목도 함께 들어 있다.[^journals][^journals2][^conferences][^prof]

**2026**

- Caiyin Dong, Chenyang Wu, Hyungchul Chung, Sisi Jian, Tiantian Chen. "When safety is not free: mitigating the transportation pink tax through safety-oriented policy interventions". *Transportation Research Part A: Policy and Practice*.
- Yang Cao, Tianlin Liu, YJ Zhou, Oscar Oviedo-Trespalacios, Tiantian Chen, Hongliang Ding. "Why low-altitude aviation accidents become fatal: Evidence from US National Transportation Safety Board Findings". *Accident Analysis & Prevention*.
- Shi Ye, Taeho Oh, Yasir Ali, Inhi Kim, Seunghee Park, Tiantian Chen. "Impact of C-V2X-enabled stop/go advisory system on driving behavior in yellow-light dilemmas: evidence from a bivariate copula model". *Analytic Methods in Accident Research*.
- Zixuan Xu, Zihao Sheng, Sikai Chen, Tiantian Chen. "Large language models for enhancing human-machine interaction in autonomous vehicles: A comprehensive survey". *Transportation Research Part C: Emerging Technologies*.
- Huimin Tang, Chunyang Han, Yiping Liu, Zhanbo Sun, Tiantian Chen, Anthony Chen. "Safety-aware traffic assignment model in mixed CAV-HDV networks: a multi-player perspective". *Transportation Research Part E: Logistics and Transportation Review*.
- Xiaoyu Shi, Yuhuan Lu, Zihao Sheng, Jian Zhang, Sikai Chen, Heye Huang, Tiantian Chen. "Learning to drive from naturalistic trajectories: Offline reinforcement learning for safe speed guidance at signalized intersections". *Journal of Intelligent and Connected Vehicles*.
- Shi Ye, Xiaowen Fu, Kun Wang, Tiantian Chen. "Initiating Barrier-free Ride Services for Disabled Passengers: An Empathy Training Program Designed for Taxi Drivers". *Transport Policy*.

**2025**

- Jiqian Dong, Sikai Chen, Samuel Labi, Tiantian Chen. "Transfusor: Transformer diffusor for controllable human-like vehicle lane-changing trajectory generation".
- Yansong Qu, Zixuan Xu, Zilin Huang, Zihao Sheng, Sikai Chen, Tiantian Chen. "MetaSSC: Enhancing 3D semantic scene completion for autonomous driving through meta-learning and long-sequence modeling". *Communications in Transportation Research*.
- Shi Ye, Tiantian Chen, Oscar Oviedo-Trespalacios, Yasir Ali, Taeho Oh, Inhi Kim. "How do the drivers react to different C-V2X-based communication conditions in dilemma zones? A driving simulator study". *Accident Analysis & Prevention*.
- Hongliang Ding, Sicong Wang, Yang Cao, Xiaowen Fu, Hanlong Fu, Quan Yuan, Tiantian Chen. "What Patterns Contribute to Autonomous Vehicle Crashes? A Study of Level 2 and 4 Automation via Association Rule Analysis". *Journal of Intelligent and Connected Vehicles*.
- Zhonghui Jiang, Hyung-Chul Chung, Tianlin Liu, Zhuo Liu, Hongliang Ding, Tiantian Chen, Tianqi Gu. "Understanding the effect of urban liveliness on walking behavior in 15-minute cities using a hybrid approach combining random forest-based SHAP model with random parameter negative binomial regression model". *Journal of Transport Geography*.
- Brad Hutchins, Yasir Ali, Tiantian Chen, Ashraf El-Hamalawi, Md Mazharul Haque. "Modelling gap selection of mobile phone distracted drivers at roundabouts: A mixed multinomial logit with heterogeneity-in-means approach". *Transportation Research Part F: Traffic Psychology and Behaviour*.
- Hongliang Ding, Zhuo Liu, Hanlong Fu, Xiaowen Fu, Tiantian Chen, Jinhua Zhao. "Can AV crash datasets provide more insight if missing information is supplemented? Employing Generative Adversarial Imputation Networks to Tackle Data Quality Issues". *Transportation Research Part C: Emerging Technologies*.
- Zixuan Xu, Neha Sengar, Tiantian Chen, Hyungchul Chung, Oscar Oviedo-Trespalacios. "Where is morality on wheels? Decoding large language model (LLM)-driven decision in the ethical dilemmas of autonomous vehicles". *Travel Behaviour and Society*.
- Zixuan Xu, Tiantian Chen, Zilin Huang, Yang Xing, Sikai Chen. "Personalizing Driver Agent Using Large Language Models for Driving Safety and Smarter Human–Machine Interactions". *IEEE Intelligent Transportation Systems Magazine*.
- Tao Li, Ruiqi Wang, Hongliang Ding, Tiantian Chen, Hyungchul Chung. "Bicycle crash frequency modeling across different crash severities using a random-forest-based Shapley Additive explanations approach". *International Journal of Injury Control and Safety Promotion*.
- Tao Li, Chengxi Hu, NN Sze, Zhanbo Sun, Hongliang Ding, Tiantian Chen. "Modelling pedestrian-vehicle interaction behaviours at non-signalised crosswalks using a game theory approach incorporating the risk perception". *Transportmetrica A: Transport Science*.
- Seunghyeon Lee, Tiantian Chen, NN Sze, Tuo Mao, Yuming Ou, Adriana-Simona Mihaita, Fang Chen. "Analysing driver behaviour and crash frequency at railway level crossings using connected vehicle and GIS data". *Travel Behaviour and Society*.
- Yiping Liu, Tiantian Chen, Hyungchul Chung, Kitae Jang, Pengpeng Xu. "Is there an emotional dimension to road safety? A spatial analysis for traffic crashes considering streetscape perception and built environment". *Analytic Methods in Accident Research*.
- Yuhuan Lu, Zhen Zhang, Wei Wang, Yiting Zhu, Tiantian Chen, Yasser D Al-Otaibi, Ali Kashif Bashir, Xiping Hu. "Knowledge-Driven Lane Change Prediction for Secure and Reliable Internet of Vehicles". *IEEE Transactions on Intelligent Transportation Systems*.
- Seunghyeon Lee, Tiantian Chen, NN Sze, Tuo Mao, Yuming Ou, Adriana-Simona Mihaita, Fang Chen. "Analysing driver behaviour and crash frequency at railway level crossings using connected vehicle and GIS data". *Travel Behaviour and Society*.
- Ziqian Zhang, Haojie Li, Tiantian Chen, NN Sze, Wenzhang Yang, Yihao Zhang, Gang Ren. "Decision-making of autonomous vehicles in interactions with jaywalkers: A risk-aware deep reinforcement learning approach". *Accident Analysis & Prevention*.

**2024**

- Hongliang Ding, Ruiqi Wang, Tiantian Chen, NN Sze, Hyungchul Chung, Ni Dong. "A hybrid approach for modeling bicycle crash frequencies: Integrating random forest based SHAP model with random parameter negative binomial regression model". *Accident Analysis & Prevention*.
- Hanlong Fu, Shi Ye, Xiaowen Fu, Tiantian Chen, Jinhua Zhao. "New insights into factors affecting the severity of autonomous vehicle crashes from two sources of AV incident records". *Travel Behaviour and Society*.
- Shi Ye, Tiantian Chen, Oscar Oviedo-Trespalacios, NN Sze, Sikai Chen. "Investigating work-related distraction’s impact on male taxi driver safety: A hazard-based duration model". *Analytic Methods in Accident Research*.
- Ziqian Zhang, Haojie Li, Haodong Hu, Tiantian Chen, Gang Ren. "Do non-motorists understand the traffic safety laws protecting them? Results from a Chinese survey". *Travel Behaviour and Society, 36, 100779*.
- Tiantian Chen, Xiaowen Fu, David A Hensher, Zhi-Chun Li, NN Sze. "Effects of proactive and reactive health control measures on public transport preferences of passengers–A stated preference study during the COVID-19 pandemic". *Transport Policy*.
- Runjia Du, Sikai Chen, Jiqian Dong, Tiantian Chen, Xiaowen Fu, Samuel Labi. "Dynamic urban traffic rerouting with fog‐cloud reinforcement learning". *Computer‐Aided Civil and Infrastructure Engineering*.
- Yiping Liu, Tiantian Chen\*, Hyungchul Chung, Kitae Jang, Pengpeng Xu. "How does subjective perception of streetscape affect traffic crashes? A spatial analysis for integrating safety into street planning". *TRB Annual Meeting 2025*.
- Yukai Wang, Tiantian Chen, Sikai Chen. "ProSafeAV: Enhancing Proactive Safety Performance of AVs using World Model-Based Reinforcement Learning and Extreme Value Theory". *TRB Annual Meeting 2025*.
- Zixuan Xu, Tiantian Chen\*, Sikai Chen. "A LLM-based Multimodal Warning System for Driver Assistance". *IEEE International Conference on Intelligent Transportation Systems (ITSC)*.
- Yukai Wang, Tiantian Chen (Corresponding Author), Kitae Jang. "A Synergistic Approach to Real-Time Crash Risk Estimation at Signalized Intersections: Integrating Learning-Based Anomaly Detection with Extreme Value Theory". *2024 Conference in Emerging Technologies in Transportation Systems (TRC-30), September 2-4, 2024*.
- Shi Ye, Tiantian Chen (Corresponding Author), Oscar Oviedo-Trespalacios, Taeho Oh and Inhi Kim. "Assessing Driver Decision-Making and Behavior in the Dilemma Zone Across Different Connected Environments: A Driving Simulator Study". *2024 Conference in Emerging Technologies in Transportation Systems (TRC-30), September 2-4,2024*.

**2023**

- Jiqian Dong, Sikai Chen, Mohammad Miralinaghi, Tiantian Chen, Pei Li, Samuel Labi. "Why did the AI make that decision? Towards an explainable artificial intelligence (XAI) for autonomous driving systems". *Transportation Research Part C: Emerging Technologies, 156*.
- Sikai Chen, Shuya Zong, Tiantian Chen, Zilin Huang, Yanshen Chen, Samuel Labi. "A taxonomy for autonomous vehicles considering ambient road infrastructure". *Sustainability, 15, Sustainability*.
- Qiang Zeng, Fangzhou Wang, Tiantian Chen, NN Sze. "Incorporating real-time weather conditions into analyzing clearance time of freeway accidents: A grouped random parameters hazard-based duration model with time-varying covariates". *Analytic Methods in Accident Research, 38, 100267*.

**2022**

- Jiqian Dong, Sikai Chen, Mohammad Miralinaghi, Tiantian Chen, Samuel Labi. "Development and testing of an image transformer for explainable autonomous driving systems". *Journal of Intelligent and Connected Vehicles, 5, 3*.
- Tiantian Chen, Xiaowen Fu, David A Hensher, Zhi-Chun Li, NN Sze. "Air travel choice, online meeting and passenger heterogeneity–An international study on travellers’ preference during a pandemic". *Transportation Research Part A: Policy and Practice, 165, 439-453*.
- Tiantian Chen, Oscar Oviedo-Trespalacios, NN Sze, Sikai Chen. "Distractions by work-related activities: The impact of ride-hailing app and radio system on male taxi drivers". *Accident Analysis & Prevention, 178, 106849*.
- Tiantian Chen, Xiaowen Fu, David A Hensher, Zhi-Chun Li, Nang Ngai Sze. "The effect of online meeting and health screening on business travel: A stated preference case study in Hong Kong". *Transportation Research Part E: Logistics and Transportation Review, 164, 102823*.
- Tiantian Chen, Yuhuan Lu, Xiaowen Fu, NN Sze, Hongliang Ding. "A resampling approach to disaggregate analysis of bus-involved crashes using panel data with excessive zeros". *Accident Analysis & Prevention, 164, 106496*.
- Hongliang Ding, Yuhuan Lu, NN Sze, Tiantian Chen, Yanyong Guo, Qinghai Lin. "A deep generative approach for crash frequency model with heterogeneous imbalanced data". *Analytic methods in accident research, 34, 100212*.

**2021**

- Jiqian Dong, Sikai Chen, Shuya Zong, Tiantian Chen, Samuel Labi. "Image transformer for explainable autonomous driving system". *2021 IEEE International Intelligent Transportation Systems Conference (ITSC),19 September, 2732-2737*.
- Tiantian Chen. "Safety of professional drivers in Hong Kong".
- Yujie Li, Tiantian Chen, Sikai Chen, Samuel Labi. "Tradeoffs between safe/comfortable headways versus mobility-enhancing headways in an automated driving environment: preliminary insights using a driving simulator experiment". *Frontiers in engineering and built environment, 1, 2*.
- Runjia Du, Sikai Chen, Jiqian Dong, Tiantian Chen, Xiaowen Fu, Samuel Labi. "Urban traffic dynamic rerouting framework: A DRL-based model with fog-cloud architecture". *arXiv preprint arXiv:2110.05532*.
- Kan Wai Hong Tsui, Xiaowen Fu, Tiantian Chen, Zheng Lei, Hanjun Wu. "Analyzing Hong Kong's inbound tourism: The impact of the COVID-19 pandemic". *IATSS Research, 45, 440-450*.
- Tiantian Chen, NN Sze, Sharon Newnam, Lu Bai. "Effectiveness of the compensatory strategy adopted by older drivers: Difference between professional and non-professional drivers". *Transportation research part F: traffic psychology and behaviour, 77, 168-180*.
- Tiantian Chen, NN Sze, Sikai Chen, Samuel Labi, Qiang Zeng. "Analysing the main and interaction effects of commercial vehicle mix and roadway attributes on crash rates using a Bayesian random-parameter Tobit model". *Accident Analysis & Prevention, 154, 106089*.
- Meng Fanyu, NN Sze, Song Cancan, Chen Tiantian, Zeng Yiping. "Temporal instability of truck volume composition on non-truck-involved crash severity using uncorrelated and correlated grouped random parameters binary logit models with space-time variations". *Analytic Methods in Accident Research, 100168*.
- Jiqian Dong, Sikai Chen, Shuya Zong, Tiantian Chen, Samuel Labi. "Image transformer for explainable autonomous driving system". *2021 IEEE International Intelligent Transportation Systems Conference (ITSC), 2021/9/19*.

## 과제

2024년 5월 13일·9월 9일과 2026년 10월 5일 소식에 소개된 과제·연구비 지원 4건이다. 기간과 연구비는 원문 표기이며, 국제 공동연구의 전체 과제 금액과 KAIST 배정액은 구분해 적었다.[^n244][^n287][^n288]

- 2026-10-05 (게시일) · Modular Chiplet Structure-Based Human-Centered AI Foundation Models for Robust, Scalable Automated Driving (기간 2026년 8월–2031년 7월; 역할 KAIST 참여 연구를 이끎; 전체 주관 BOS Semiconductors; 지원 Global Industrial Technology Cooperation Center (GITCC) Program; MOTIR; KIAT; 협력 기관 Purdue University; 연구비 전체 한국 정부 지원액 100억 원; KAIST 배정액 10억 원)
- 2026-10-05 (게시일) · Development of a Detachable On-Board Device for Multi-Vehicle Remote Operation and Safety Enhancement Technologies (DOVE) (기간 2026년 7월–2029년 12월; 역할 KAIST 참여 연구를 이끎; 전체 주관 BYDA; 지원 Smart Car sub-program of MOTIR's Automotive Industry Technology Development Program; KEIT; 연구비 전체 예산 109억 7천만 원; KAIST 배정액 7억 원)
- 2024-09-09 (게시일) · Maritime Accident Reduction Project (사업 ASPIRE League Partnership Seed Fund Award (2024))
- 2024-05-13 (게시일) · Empowering Mobility for a Smart Aging Society: Development and Testing of Large Language Model-Based Driver Assistance Agent (사업 2024 Outstanding Young Scientist Grant Program; 지원 NRF; 연구비 4억 원; 기간 2024–2027; 역할 Project manager: Dr. Chen Tiantian)

## 수상과 선정

교수 소개와 구성원 페이지의 2022–2024년 항목, News에 적힌 2025–2026년 수상·선정을 합친 13건이다. 연도만 있는 것은 그 표기를 유지하고, 날짜를 게시일로 알 수 있는 항목에는 게시일이라고 적었다. 교수는 2022년 10월에 KAIST에 부임했으며, 2022년 수상의 월일은 적혀 있지 않다. 90회 대한교통학회 발표상 날짜는 교수 소개의 표기다.[^prof][^phd][^n247][^n248][^n250][^n274][^n275][^n276][^n277]

- 2022 · HKIE-SSC Project Competition 2021 (Runner-up Award)
- 2023-12-11–12 · The First-Prize of the 27th HKSTS Outstanding Student Paper Award (Shi Ye)
- 2023 · Award Winner, International Category, 2023 KAIST Q-Day
- 2024 · Best paper (Second Prize), the 28th International Conference of Hong Kong Society for Transportation Studies
- 2024 · EWON Associate (Chair) Professorship, KAIST Outstanding Young Faculty Award
- 2024-03-27–28 (교수 소개 표기) · Best paper presentation award, the 90th Korean Society of Transportation Conference (Yiping Liu)
- 2026-09-08 (게시일) · 2026 Kim Young-han Global Leader Scholar (Ye Shi)
- 2026-07-16 · Best Lightning Talk Award at CICTP 2026 (Ye Shi and Zixuan Xu)
- 2026-06-26 (게시일) · Outstanding Student Research Award, KAIST–KORAIL Railway Standard Mobility Program (Sangmi Kang and Suji Lim)
- 2026-02-12 · 2026 KAIST Globalization Excellence Lab Award
- 2026-02-11 · Readers’ Choice Award for KAIST Breakthroughs (2025)
- 2026-02-12 · Tiantian Chen, KAIST Prize for Excellence in Teaching 수상
- 2025-12-17 · Tiantian Chen, KAIST Impact Research Award 수상

## 소식

2025년 11월 13일–2026년 10월 5일 게시된 학술대회 참가·발표·기조강연·초청 세미나 소식 15건이다. 항목 맨 앞 날짜는 게시일이며, 행사일이 원문에 있으면 내용에 따로 적었다.[^n241][^n242][^n246][^n249][^n251][^n252][^n255][^n272][^n278][^n279][^n280][^n281][^n282][^n283][^n284]

- 2026-10-05 · Caiyin Dong, hEART 2026에서 연구 발표
- 2026-10-05 · Yiping Liu와 Chengxi Hu, IEEE ITSC 2026 참가
- 2026-09-08 · Tiantian Chen, KSR 2026에서 교통약자를 위한 대중교통 설계를 주제로 기조강연 (행사 2026-08-25–27)
- 2026-06-28 · Shi Ye, RSS 2026에서 C-V2X 정지·통과 안내와 운전 행동에 관한 포스터 발표
- 2026-06-26 · Tiantian Chen·Suji Lim·Sangmi Kang, TRA 2026에서 연구 발표 (행사 2026-05-18–21)
- 2026-06-07 · Lunar Sebastian Widjaja, 제9회 APRU Sustainable Cities and Landscapes 학술대회에서 연구 발표
- 2026-04-13 · Tiantian Chen, Qian Weichang International Summit에서 사람 중심 도시와 이동 안전에 관한 발표 (행사 2026-03-31)
- 2026-04-13 · Bingyu Zhao(TU Wien), KAIST 초청 세미나 (행사 2026-04-08)
- 2025-11-13 · Chenyang Wu(Northwestern Polytechnical University), KAIST 초청 세미나 (행사 2025-11-06)
- 2025-11-13 · Oscar Oviedo-Trespalacios(Delft University of Technology), KAIST 초청 세미나 (행사 2025-10-30)
- 2025-11-13 · Tiantian Chen, IPTF 2025 참가 및 세션 좌장 (행사 2025-10-29)
- 2025-11-13 · 제3회 Jeju Summer Camp에서 Shimul Haque와 Elisabetta Cherchi의 발표 및 연구실과의 학술 토론 (행사 2025-06-24–07-04)
- 2025-11-13 · Zixuan Xu·Yiping Liu, IEEE IV 2025 참가; Zixuan Xu의 개인별 LLM 운전 보조 연구 발표 (행사 2025-06-22–25)
- 2025-11-13 · 연구실 학생들, ITS Asia Pacific Forum 2025 참가 (행사 2025-05-28–30)
- 2025-11-13 · Tiantian Chen, Southwest Jiaotong University의 Intelligent Transportation & Optimization Seminar에서 발표 (행사 2025-05-15)

## 연락과 위치

- 교수 이메일: nicole.chen@kaist.ac.kr[^prof]
- 연구실 누리집 주소: 대전광역시 유성구 문지로 193 KAIST 문지캠퍼스 F306호, 우편번호 34051[^home][^prof]
- 학과 교수 명단의 사무실: F435호[^dept]
- 전화: 042-350-1260[^prof]
[^home]: 연구실 누리집 첫 화면 <https://human-facts.kaist.ac.kr/> (2026-10-26 열람)
[^dept]: 조천식모빌리티대학원 교수 명단 <https://mo.kaist.ac.kr/professor/> (2026-10-26 열람)
[^prof]: 연구실 Professor 페이지 <https://human-facts.kaist.ac.kr/sub3_1.php> (2026-10-26 열람)
[^phd]: Ph.D. Students 페이지 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (2026-10-26 열람)
[^ms]: M.S. Students 페이지 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub3_3> (2026-10-26 열람)
[^visiting]: Visiting Students 페이지 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub3_4> (2026-10-26 열람)
[^alumni]: Alumni 페이지 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub3_5> (2026-10-26 열람)
[^intern]: Internship 페이지 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub3_6> (2026-10-26 열람)
[^r1]: Simulation Experiments 연구 소개 <https://human-facts.kaist.ac.kr/sub4_1.php> (2026-10-26 열람)
[^r2]: Travel Behavior Analysis 연구 소개 <https://human-facts.kaist.ac.kr/sub4_2.php> (2026-10-26 열람)
[^r3]: Crash Risk Analysis 연구 소개 <https://human-facts.kaist.ac.kr/sub4_3.php> (2026-10-26 열람)
[^r4]: LLMs for Human-Machine Interaction 연구 소개 <https://human-facts.kaist.ac.kr/sub4_4.php> (2026-10-26 열람)
[^journals]: Journal 게시판 첫째 쪽 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1> (2026-10-26 열람) 게시글 상세: <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=53>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=52>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=51>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=50>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=49>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=48>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=47>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=46>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=45>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=44>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=43>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=42>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=41>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=40>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=39>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=38>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=37>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=36>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=35>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=34>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=33>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=32>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=31>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=30>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=29>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=28>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=27>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=26>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=25>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=24> (2026-10-27 열람).
[^journals2]: Journal 게시판 둘째 쪽 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&page=2> (2026-10-27 열람) 게시글 상세: <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=21&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=23&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=22&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=14&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=15&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=13&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=12&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=11&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=10&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=9&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=17&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=16&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=8&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=6&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=4&page=2>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=3&page=2> (2026-10-27 열람).
[^conferences]: Conference 게시판 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2> (2026-10-26 열람) 게시글 상세: <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=9>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=8>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=7>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=6>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=4>, <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=2> (2026-10-27 열람).
[^n241]: Ph.D. Student Caiyin Dong Attends hEART 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=34> (2026-10-27 열람)
[^n242]: Ph.D. Students Yiping Liu and Chengxi Hu Attend IEEE ITSC 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=33> (2026-10-27 열람)
[^n243]: Congratulations to Prof. Tiantian (Nicole) Chen on Her Appointment as Associate Editor of Analytic Methods in Accident Research (AMAR) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=32> (2026-10-27 열람)
[^n244]: Professor Tiantian Chen Leads Two International Mobility Projects on Automated Driving and Remote Operation <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=31> (2026-10-27 열람)
[^n246]: Prof. Chen Invited to Deliver a Keynote Speech at KSR 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=29> (2026-10-27 열람)
[^n247]: PhD Student Ye Shi Selected as a Kim Young-han Global Leader Scholar <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=28> (2026-10-27 열람)
[^n248]: PhD Students Ye Shi and Zixuan Xu Received the Best Lightning Talk Award at CICTP 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=27> (2026-10-27 열람)
[^n249]: NEWS – PhD Student Shi Ye Presented a Poster at RSS 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=26> (2026-10-27 열람)
[^n250]: Congratulations to Suji and Sangmi on Receiving Outstanding Student Awards <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=25> (2026-10-27 열람)
[^n251]: Prof. Chen, Suji, and Sangmi Presented at the Transport Research Arena (TRA) 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=24> (2026-10-27 열람)
[^n252]: Intern Student Lunar Sebastian Widjaja Presented at the 9th APRU Sustainable Cities and Landscapes Conference 2026 <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=23> (2026-10-27 열람)
[^n255]: Prof. Chen Presented at the PolyU Qian Weichang International Summit 2026 (March 31, 2026) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=19> (2026-10-27 열람)
[^n272]: Prof. Bingyu Zhao is invited to give a seminar and visit HF Lab (April 8, 2026) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=18> (2026-10-27 열람)
[^n274]: 2026 KAIST Globalization Excellence Lab Award <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=16> (2026-10-27 열람)
[^n275]: Readers’ Choice Award for KAIST Breakthroughs (2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=15> (2026-10-27 열람)
[^n276]: Prof. Chen Received KAIST Prize for Excellence in Teaching <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=14> (2026-10-27 열람)
[^n277]: Prof. Chen Received the KAIST Impact Research Award <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=13> (2026-10-27 열람)
[^n278]: Prof. Chenyang Wu is invited to give a seminar and visit HF Lab (Nov 6, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=12> (2026-10-27 열람)
[^n279]: Prof. Oscar Oviedo-Trespalacios is invited to give a seminar and visit HF Lab (October 30, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=11> (2026-10-27 열람)
[^n280]: Prof. Chen attend and chair a session at the IPTF 2025 (October 29, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=10> (2026-10-27 열람)
[^n281]: Prof. Shimul Haque and Prof. Elisabetta Cherchi are invited to deliver presentations at the 3rd Jeju Summer Camp (June 24 – July 4, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=9> (2026-10-27 열람)
[^n282]: PhD students (Zixuan, Yiping) attended the 2025 IEEE Intelligent Vehicles Symposium (IV) in Cluj-Napoca, Romania (June 22–25, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=8> (2026-10-27 열람)
[^n283]: HumanFACTS students attend the 2025 ITS Asia Pacific Forum (May 28–30, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=7> (2026-10-27 열람)
[^n284]: Prof. Chen present at the “Intelligent Transportation & Optimization Seminar” at Southwest Jiaotong University (May 15, 2025) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=6> (2026-10-27 열람)
[^n287]: ASPIRE League Partnership Seed Fund Award for Maritime Accident Reduction Project (2024) <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=3> (2026-10-27 열람)
[^n288]: NEWS-  NRF Award – 2024 Outstanding Young Scientist Grant Program <https://human-facts.kaist.ac.kr/bbs/board.php?bo_table=sub6_1&wr_id=2> (2026-10-27 열람)
[^p1]: S. Ye 외, I. Kim, Accident Analysis & Prevention 221, 108208 (온라인 2025-08-20). <https://doi.org/10.1016/j.aap.2025.108208> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/40840241/> (2026-10-27 열람).
[^p2]: Z. Xu 외, S. Chen, IEEE Intelligent Transportation Systems Magazine. <https://doi.org/10.1109/MITS.2025.3551736> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.aap.2024.107778%7C10.1016/j.aap.2025.108251%7C10.1016/j.aap.2025.108311%7C10.1016/j.amar.2025.100374%7C10.1016/j.tranpol.2023.11.011%7C10.1080/23249935.2025.2479084%7C10.1109/itsc58415.2024.10919879%7C10.1109/mits.2025.3551736> (2026-10-27 열람). 랩 목록 연도 2025.
[^p3]: Y. Liu 외, P. Xu, Analytic Methods in Accident Research. <https://doi.org/10.1016/j.amar.2025.100374> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.aap.2024.107778%7C10.1016/j.aap.2025.108251%7C10.1016/j.aap.2025.108311%7C10.1016/j.amar.2025.100374%7C10.1016/j.tranpol.2023.11.011%7C10.1080/23249935.2025.2479084%7C10.1109/itsc58415.2024.10919879%7C10.1109/mits.2025.3551736> (2026-10-27 열람). 랩 목록 연도 2025.
[^p4]: T. Chen 외, N. Sze, Transport Policy. <https://doi.org/10.1016/j.tranpol.2023.11.011> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.aap.2024.107778%7C10.1016/j.aap.2025.108251%7C10.1016/j.aap.2025.108311%7C10.1016/j.amar.2025.100374%7C10.1016/j.tranpol.2023.11.011%7C10.1080/23249935.2025.2479084%7C10.1109/itsc58415.2024.10919879%7C10.1109/mits.2025.3551736> (2026-10-27 열람). 랩 목록 연도 2024.
[^p5]: Z. Xu, T. Chen, S. Chen, 2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC). <https://doi.org/10.1109/ITSC58415.2024.10919879> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.aap.2024.107778%7C10.1016/j.aap.2025.108251%7C10.1016/j.aap.2025.108311%7C10.1016/j.amar.2025.100374%7C10.1016/j.tranpol.2023.11.011%7C10.1080/23249935.2025.2479084%7C10.1109/itsc58415.2024.10919879%7C10.1109/mits.2025.3551736> (2026-10-27 열람). 랩 목록 연도 2024.
[^p6]: T. Li 외, T. Chen, Transportmetrica A: Transport Science. <https://doi.org/10.1080/23249935.2025.2479084> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.aap.2024.107778%7C10.1016/j.aap.2025.108251%7C10.1016/j.aap.2025.108311%7C10.1016/j.amar.2025.100374%7C10.1016/j.tranpol.2023.11.011%7C10.1080/23249935.2025.2479084%7C10.1109/itsc58415.2024.10919879%7C10.1109/mits.2025.3551736> (2026-10-27 열람). 랩 목록 연도 2025.

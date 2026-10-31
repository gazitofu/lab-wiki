# Manufacturing and Service Systems Lab

**KAIST 산업및시스템공학과·녹색성장지속가능대학원(겸임) · 김현정 부교수**

- 분야: 제조 시스템의 일정 계획과 최적화, 로봇을 이용한 생산 설비의 모델링과 분석, 생산·물류 관리와 창고 자동화
- 대분야: 산업·시스템, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^p1][^p3][^p5], 강화학습[^p4][^p6][^p7], 그래프 기계학습·지식 그래프[^p7]
- 홈페이지: <https://msslab.kaist.ac.kr>
- 근거와 출처: [Manufacturing and Service Systems Lab 근거 페이지](msslab-sources.md)

> 공장의 설비·로봇과 물류 자원이 어떤 순서로 일할지 정하는 방법을 연구하며, 수학적 최적화와 학습 방법으로 생산 일정과 창고 운영 문제를 푼다.[^home][^p1]

## 무엇을 연구하나

김현정 부교수가 이끄는 Manufacturing and Service Systems Lab은 제조 시스템의 스케줄링(작업에 자원과 실행 시점을 배정하는 일정 계획), 생산·물류 관리, 창고 자동화 시스템의 설계와 운영을 연구한다. 로봇을 이용한 제조 시스템의 모델링(대상의 구조와 작동을 수학이나 계산으로 나타내는 일)과 분석도 연구 분야로 내세운다.[^home][^prof]

연구 방법은 최적화(정해진 조건 안에서 목적 함수의 값을 최소화하거나 최대화하는 선택을 찾는 방법), 페트리넷(상태와 사건을 서로 다른 종류의 점으로 나타내고 표식의 이동으로 상태 변화를 나타내는 수학 모형), 강화학습(행동에 따른 보상으로 누적 보상을 키우는 행동 방식을 배우는 기계학습), 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습)이다. 첫 화면은 이 방법들의 적용 대상으로 제조 일정, 물류 관리, 생산 계획, 창고 자동화를 제시한다.[^home]

생산 현장의 조건을 일정 문제에 넣는 것이 한 갈래다. 반도체 장비 연구는 서로 다른 웨이퍼(반도체 회로를 만드는 바탕이 되는 얇은 판)가 함께 처리될 때 투입 순서와 운반 로봇의 행동 순서를 함께 정한다.[^p4] 배터리 제조 연구는 재료를 누르는 설비의 마모 상태에 따라 처리할 수 있는 작업이 달라진다는 조건과 설비 보전(설비의 상태와 기능을 유지하거나 회복하는 관리)을 일정에 반영한다.[^p3] 제철 공정 연구는 작업자의 과거 판단을 학습한 모형을 수학적 최적화와 결합해 작업 배정을 정한다.[^p5]

작업들이 서로 영향을 주고받는 관계도 학습의 대상이다. 강판 코일 창고에서는 같은 선로를 쓰는 여러 크레인이 충돌을 피하면서 작업을 나누고 순서를 정하도록, 그래프(대상과 그 관계를 점과 선으로 나타내는 구조) 신경망(점과 연결 관계를 이용해 자료를 학습하는 신경망)을 쓰는 강화학습 방법을 제안했다.[^p6] 병렬 설비(여러 설비에 작업을 나누어 처리하는 생산 구성) 연구는 작업 시작 가능 시점, 사용 가능한 설비, 준비 시간 조건을 나타내는 새로운 그래프 표현과 그래프 신경망 기반 강화학습을 함께 설계했다. 학습을 마치면 작업이나 설비의 수에 관계없이 적용할 수 있다고 보고했다.[^p7]

일정 문제를 푸는 학습 방법 자체도 연구한다. PGMPO(Preference-Guided Multi-Policy Optimization, 선호 관계를 이용한 다중 정책 최적화)는 하나의 신경망에서 여러 정책(상태에 따라 행동을 선택하는 규칙)을 나타내고, 정책 사이의 선호 관계로 서로 다른 해결 전략을 배우게 한다. 별도의 보상 함수(행동이나 결과에 보상값을 부여하는 규칙)를 설계하지 않는 방법이다.[^p1] 다른 논문은 공통 목표를 가진 여러 정책을 자가 표지(모형이 스스로 학습에 쓸 표지를 만드는 방식)로 학습시키고, 표지의 품질에 따라 모방 학습(제시된 행동 예시를 따라 행동 방식을 배우는 방법)의 강도를 조절한다.[^p2]

## 주요 연구 주제

### 반도체 장비의 비순환 일정

클러스터 장비(여러 처리 모듈과 이들 사이의 운반 장치를 결합한 생산 장비)에서는 웨이퍼의 투입과 로봇 이동을 함께 정해야 한다. 연구실은 같은 순서의 반복을 가정하지 않는 비순환 일정을 심층 강화학습(딥러닝을 결합해 행동 방식을 학습하는 강화학습)으로 푸는 방법을 제안했다. 웨이퍼의 처리 시간과 흐름을 파악하고, 계속 바뀌는 일정 정보로 교착(작업들이 서로의 완료나 자원 반환을 기다려 진행할 수 없는 상태)을 피하며 다음 로봇 행동을 고른다. 여러 장비 구조와 웨이퍼 종류의 실험에서 기존 로봇 작업 순서와 탐색 방법에 비해 성능 향상을 보고했다.[^p4]

### 설비 보전과 제철 공정의 일정

배터리 제조의 단일 설비 일정 연구는 설비 상태가 각 작업의 요구를 충족해야 작업을 처리할 수 있고, 보전으로 상태가 회복되는 조건을 다룬다. 작업의 완료 시각에서 납기(작업 완료가 요구되는 시점)를 뺀 값 중 최댓값을 줄이도록 정수계획법(결정 변수에 정수 조건을 두는 최적화 방법) 모형과 분기한정법(후보를 갈래로 나누고 평가값의 한계로 최적해가 될 수 없는 갈래를 제외하는 풀이 방법)을 개발했다. 규모가 큰 문제에는 휴리스틱(최적해를 보장하지 않으면서 실용적인 해를 찾도록 만든 풀이 방법)을 제안했다.[^p3]

제강·연속주조(녹인 금속을 연속으로 굳혀 소재를 만드는 공정)의 일정 연구는 정련(금속의 불순물을 줄이고 성분을 조정하는 공정) 단계의 작업 배정을 다룬다. 작업자의 과거 판단을 학습한 신경망이 먼저 판단하고, 그 판단의 신뢰도가 부족할 때 혼합정수계획법(정수 조건이 있는 변수와 그렇지 않은 변수를 함께 쓰는 최적화 방법)으로 얻은 판단을 보태는 방식이다. 정련 단계 작업 완료 시각의 합을 줄이는 실험 결과와 국내 제철 회사에 구현한 사례를 보고했다.[^p5]

### 여러 해결 전략을 배우는 일정 계획

유연 작업장 일정(작업별로 처리할 설비와 설비에서의 처리 순서를 함께 정하는 일정)에서는 다양한 해결 전략을 탐색하고 학습하는 방법을 연구한다. PGMPO는 여러 정책을 하나의 신경망으로 나타내고 정책 사이의 선호 관계를 학습 신호로 쓴다.[^p1] 자가 표지 기반 다중 정책 학습은 공통 목표를 가진 정책들이 서로 다른 전략을 배우도록 하며, 표지의 품질에 따라 모방 강도를 조절한다. 두 논문 모두 보상 함수를 따로 설계하지 않는 학습 방법을 제안한다.[^p1][^p2]

### 창고 크레인과 병렬 설비의 작업 배정

강판 코일 창고의 일정 연구는 작업이 새로 들어오고 먼저 처리해야 하는 작업 관계가 있으며, 여러 크레인이 같은 선로를 사용하는 상황을 다룬다. 작업의 평균 대기 시간을 줄이도록 작업을 크레인에 배정하고 실행 순서를 정하는 실시간 강화학습 방법을 제안했다.[^p6]

병렬 설비 연구는 작업별 시작 가능 시점과 사용 가능한 설비, 작업 순서와 설비에 따라 달라지는 준비 시간을 함께 다룬다. 작업별 납기 초과 시간에 중요도를 반영한 가중치를 곱해 합친 값을 줄이는 것이 목표다. 이 조건들을 다루는 새로운 그래프 표현을 만들고 그래프 신경망과 강화학습을 결합했다.[^p7]

## 대표 논문

교수의 KAIST 재직 시기에 나온 논문 가운데 학습 방법, 설비 보전, 반도체·제철 공정, 물류와 생산 일정의 연구 갈래를 고르게 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 연도는 학술지 권호·학회 연도이며 온라인 공개일은 각주에 적었다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Preference-Guided Multi-Policy Optimization for Flexible Job Shop Scheduling](https://doi.org/10.24963/ijcai.2026/685) · IJCAI | 유연 작업장 일정 문제에서 하나의 신경망으로 여러 행동 전략을 나타내고, 전략 사이의 선호 관계를 이용해 다양한 해결 방식을 배우게 했다. 별도의 보상 함수 설계 없이 기존 신경망 기반 풀이 방법의 성능을 여러 기준 문제에서 높였다고 보고했다.[^p1] | 마지막 저자 Hyun-Jung Kim |
| 2 | 2025 | [Towards Generalizable Multi-Policy Optimization with Self-Evolution for Job Scheduling](https://doi.org/10.52202/085713-0828) · NeurIPS | 작업 일정 문제의 여러 행동 전략을 공통 목표와 하나의 신경망으로 학습한다. 모형이 만든 학습 표지의 품질에 따라 모방 강도를 조절하며, 보상 함수를 별도로 설계하지 않는다. 여러 작업 일정 문제에서 기존 강화학습 방법과 비교해 성능 향상을 보고했다.[^p2] | 마지막 저자 Hyun-Jung Kim |
| 3 | 2025 | [Single machine scheduling with variable maintenance in the battery manufacturing](https://doi.org/10.1080/00207543.2025.2516764) · International Journal of Production Research | 배터리 제조에서 설비가 마모되면 처리 가능한 작업이 달라지고, 보전하면 상태가 회복되는 문제다. 작업 완료 시각에서 납기를 뺀 값 중 최댓값을 줄이는 정수계획 모형과 분기한정법을 개발했다. 규모가 큰 문제에는 실용적인 해를 찾는 별도 방법을 제안했다.[^p3] | 마지막 저자 Hyun-Jung Kim |
| 4 | 2025 | [Noncyclic Scheduling of Cluster Tools Using Deep Reinforcement Learning](https://doi.org/10.1109/TASE.2025.3632534) · IEEE Transactions on Automation Science and Engineering | 서로 다른 웨이퍼 종류가 함께 처리되는 반도체 장비에서 투입 순서와 운반 로봇 행동을 함께 정하는 심층 강화학습 방법이다. 처리 시간·흐름과 바뀌는 일정 정보를 이용해 교착을 피하도록 설계했고, 순환 작업을 가정하지 않는 여러 장비 구성의 실험에서 성능을 보였다.[^p4] | 마지막 저자 Hyun-Jung Kim |
| 5 | 2025 | [Scheduling of steelmaking-continuous casting process by integrating deep neural networks with mixed integer programming](https://doi.org/10.1080/00207543.2024.2439369) · International Journal of Production Research | 제철 정련 단계에서 작업자의 과거 판단을 학습한 신경망을 쓰되, 그 판단의 신뢰도가 부족할 때 혼합정수계획으로 얻은 판단을 보탠다. 작업 완료 시각의 합을 줄이는 실험 결과와 국내 제철 회사에 구현한 사례를 보고했다.[^p5] | 마지막 저자 Hyun-Jung Kim |
| 6 | 2024 | [Dynamic Crane Scheduling with Reinforcement Learning for a Steel Coil Warehouse](https://doi.org/10.1109/icra57147.2024.10610858) · ICRA | 강판 코일 창고에서 여러 크레인이 같은 선로를 사용하고 작업이 새로 들어오는 상황을 다룬다. 충돌을 피하면서 작업의 평균 대기 시간을 줄이도록, 그래프 신경망과 강화학습으로 크레인별 작업과 처리 순서를 정했다.[^p6] | 마지막 저자 Hyun-Jung Kim |
| 7 | 2024 | [Reinforcement Learning for Unrelated Parallel Machine Scheduling with Release Dates, Setup Times, and Machine Eligibility](https://doi.org/10.1109/wsc63780.2024.10838725) · Winter Simulation Conference | 작업이 시작될 수 있는 시점, 사용 가능한 설비, 작업 순서와 설비에 따라 다른 준비 시간을 함께 고려한다. 납기 초과 시간의 가중 합을 줄이도록 새 그래프 표현과 그래프 신경망 기반 강화학습을 제안했다. 학습 뒤 작업·설비 수에 관계없이 적용할 수 있다고 보고했다.[^p7] | 공저자(3명 중 2번째) |

## 교수와 전문 분야

김현정은 KAIST 산업및시스템공학과에서 2009년 2월 학사, 2011년 2월 석사, 2013년 8월 박사 학위를 받았다. 2013년 10월부터 2014년 12월까지 미국 캘리포니아대학교 버클리의 산업공학·경영과학 분야 박사후연구원이었고, 2015년 3월부터 2019년 8월까지 성균관대학교 시스템경영공학과 조교수로 재직했다. 2019년 9월 KAIST 산업및시스템공학과 조교수로 부임했으며, 2022년 3월부터 부교수로 재직한다고 소개한다.[^prof]

연구실 소개와 논문을 함께 보면 전문 분야는 로봇을 이용하는 생산 장비의 일정 계획, 제조·물류 시스템의 최적화, 일정 계획을 위한 학습 알고리즘이다. 반도체와 배터리 제조, 제철 공정, 창고의 운반 작업을 대상으로 연구해 왔다.[^home][^p3][^p4][^p5][^p6] 녹색성장지속가능대학원 교수 명단은 김현정의 연구 분야를 「스마트 제조, 스케줄링, 운영 관리」로 적는다.[^gggs]

교수 소개는 2024년 11월부터 IEEE Transactions on Automation Science and Engineering의 Senior Editor, 2024년 7월부터 Applied Operations and Analytics의 Editor, 2025년 2월부터 Naval Research Logistics의 Associate Editor, 2024년 11월부터 Journal of Scheduling의 Associate Editor, 2023년 8월부터 International Journal of Production Research의 Associate Editor를 맡는다고 적는다. IEEE CASE의 Editor는 2025년부터, IEEE RAS 반도체 제조 자동화 기술위원회의 공동 의장은 2026년부터라고 적는다.[^prof]

## 응용 분야

연구실이 제시하는 응용은 제조 일정, 물류 관리, 생산 계획, 창고 자동화다.[^home] 과제 목록에는 반도체 공장 일정, 생산 설비 설치, 가공 라인과 공급사슬 운영, 디스플레이 생산, 타이어 생산, 선박 생산의 작업 부하, 크레인 운반과 반도체 회로의 배선 문제가 포함된다.[^projects]

## 구성원

2026년 10월 31일 Researchers 페이지 기준으로 박사후연구원 1명, 박사과정 13명, 석사과정 5명이다. 연구 주제와 학교 이메일은 페이지의 표기다. 「대표 논문 참여」는 위 논문 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 사람에게 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Sang-Wook Lee | 박사후연구원 | Scheduling, planning, and optimization in manufacturing systems | sw_lee@kaist.ac.kr | 3, 5 |
| Sang-Hyun Cho | 박사과정 | Parallel machine scheduling, neural combinatorial optimization | ie02002@kaist.ac.kr | 1, 2, 6, 7 |
| Sanghyun Joo | 박사과정 | Cluster tool scheduling, petri-net based optimization method | toughshj@kaist.ac.kr | 6 |
| Sohyun Jeong | 박사과정 | Scheduling, optimization | sohyunj1224@kaist.ac.kr |  |
| Hong-Yeon Kim | 박사과정 | Reinforcement learning, circuit routing | ghd4567@kaist.ac.kr |  |
| Jimin Park | 박사과정 | Interactive scheduling, multi-objective scheduling, LLMs for scheduling | jiminpark@kaist.ac.kr |  |
| Min-Chan Kim | 박사과정 | Cluster tool scheduling | minchan@kaist.ac.kr |  |
| Yonghwan Kim | 박사과정 | Scheduling, optimization, reinforcement learning | yhwan_kim@kaist.ac.kr |  |
| Inguk Choi | 박사과정 | Neural combinatorial optimization | inguk0826@kaist.ac.kr | 1, 2 |
| Yong Jae Kim | 박사과정 | Warehousing, scheduling | yongjae9@kaist.ac.kr |  |
| Dong-Ha Lee | 박사과정 | Combinatorial optimization, reinforcement learning | dongha929@kaist.ac.kr |  |
| Dong-Yoon Oh | 박사과정 | Neural combinatorial optimization | odong@kaist.ac.kr |  |
| Minju Jang | 박사과정 | Production and manufacturing systems, scheduling | minjujang@kaist.ac.kr |  |
| Min Geon Kim | 박사과정 | AI-enabled optimization | kt7447@kaist.ac.kr |  |
| Hoang Thi Thuc Hien | 석사과정 | Optimization | hien.htt254081@kaist.ac.kr |  |
| Jung Min Lee | 석사과정 | Scheduling, optimization | 0619dlwjdals@kaist.ac.kr |  |
| Seung Kyu Yoon | 석사과정 | Scheduling, reinforcement learning | skyoon1109@kaist.ac.kr |  |
| Su-Hyun Choi | 석사과정 | Scheduling, optimization | suhyun.choi@kaist.ac.kr |  |
| Jin Seok Chun | 석사과정 | Scheduling, reinforcement learning | martin3433@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 페이지의 2017–2026년 학위 항목 24건으로, 석사 18건과 박사 6건이다. 학위·소속 학교·학위 논문은 연구실 표기다. 현재 구성원이 이전에 받은 학위와 성균관대학교 재직 시기의 학위 항목도 포함한다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seojin Kim | M.S. in Data Science, KAIST (2026.08) |  | The Stack Loading Problem with Load-Bearing and Stack Height Limits: A Learning-Accelerated Decomposition Approach |
| Woo-Jin Shin | Ph.D. in Industrial & Systems Engineering, KAIST (2026.02) |  | Optimization Models and Algorithms for Multi-Crane Scheduling |
| Dong-Ha Lee | M.S. in Industrial & Systems Engineering, KAIST (2026.02) |  | Parallel Machine Scheduling under Quality Uncertainty in Wafer Manufacturing |
| Zuhdi Faturrahman | M.S. in Industrial & Systems Engineering, KAIST (2026.02) |  | Fine-tuning Large Language Models for Algorithm Selection in the Flexible Job Shop Scheduling Problem |
| Ji-Yun Shin | M.S. in Industrial & Systems Engineering, KAIST (2026.02) |  | Deep Reinforcement Learning for Reconnaissance Drone Path Planning with Clustered Targets |
| Sang-Wook Lee | Ph.D. in Industrial & Systems Engineering, KAIST (2025.08) |  | Scheduling with Maintenance and Position-Based Job Eligibility |
| So-Young Lee | M.S. in Data Science, KAIST (2025.08) |  | Parallel machine scheduling with resource constraints and sequence dependent setup costs |
| Seon-Young Hwang | M.S. in Industrial & Systems Engineering, KAIST (2025.08) |  | Bi-objective Parallel Machine Scheduling for the Upstream Process (USP) in Biopharmaceutical Production |
| Duyeon Kim | Ph.D. in Industrial & Systems Engineering, KAIST (2025.02) |  | Learning-based noncyclic scheduling of cluster tools |
| Jehun Lee | Ph.D. in Industrial & Systems Engineering, KAIST (2025.02) |  | Learning schedulers for job shop scheduling problems |
| Jeongsun Ahn | Ph.D. in Industrial & Systems Engineering, KAIST (2025.02) |  | Non-cyclic scheduling of cluster tools: analysis and optimization |
| Chae-Young Kim | M.S. in Industrial & Systems Engineering, KAIST (2024.02) |  | Hybrid flowshop scheduling with no-wait and blocking constraints |
| Hong-Yeon Kim | M.S. in Industrial & Systems Engineering, KAIST (2024.02) |  | Cycle planning and input sequencing for concurrent processing in semiconductor manufacturing tool |
| Sang-Hyun Cho | M.S. in Industrial & Systems Engineering, KAIST (2023.02) |  | Resource leveling for LNG carrier production with deep reinforcement learning |
| Sung-Ho Min | M.S. in Industrial & Systems Engineering, KAIST (2022.08) |  | Identical parallel machine scheduling with peak energy consumption constraints |
| Hyungjoon Yang | M.S. in Industrial & Systems Engineering, KAIST (2022.02) |  | Multi-manned assembly line worker assignment and balancing problem with positional constraints |
| Jeongsun Ahn | M.S. in Industrial & Systems Engineering, KAIST (2022.02) |  | A branch and bound algorithm for scheduling of flexible manufacturing systems |
| Jun Kim | Ph.D. in Industrial Engineering, SKKU (2022.02) |  | Scheduling of manufacturing systems with multiple processing alternatives |
| Jehun Lee | M.S. in Industrial Engineering, SKKU (2021.02) |  | A genetic algorithm for hybrid flow shop scheduling problems with multiple assembly stages |
| Sang-Su Park | M.S. in Industrial Engineering, SKKU (2020.02) |  | Genetic algorithm with deadlock prevention conditions for scheduling of automated assembly lines |
| Young-In Kim | M.S. in Industrial Engineering, SKKU (2019.02) |  | Rescheduling of unrelated parallel machines with sequence-dependent setup times under the prediction of machine disruptions |
| Kyu-Min Lee | M.S. in Industrial Engineering, SKKU (2018.08) |  | Case-based reasoning for rail-guided vehicle scheduling in EDS line |
| Sung Il Kim | M.S. in Industrial Engineering, SKKU (2017.08) |  | Dynamic supply chain design and operation for smart factory |
| Soo-Young Kim | M.S. in Industrial Engineering, SKKU (2017.02) |  | Two-stage flexible flow shop scheduling problem with multiple assembly machines and family setup times |

## 최근 논문 목록 (2021–2026)

연구실 Publications 페이지에 2021–2026년으로 적힌 국제 학술지 논문 35건, 국제 학회 발표 55건, 국내 학회 발표 53건, 합계 143건이다. 제목·저자·발표처는 연구실 표기다. 연도만 적힌 2021년 항목도 포함하며, 학술지와 학회에 따로 게시된 항목은 각각 싣는다. 별표는 누리집 표시 그대로다.[^pubs] 「A unified learning framework for the block relocation problem: A new performance baseline」의 연도는 OpenAlex의 출판 연도다.[^year]

**2026**

- W.-J. Shin, J.-K. Jung, S.-H. Cho, I. Choi, S. Tanaka, and H.-J. Kim\*. "A unified learning framework for the block relocation problem: A new performance baseline". *European Journal of Operational Research, DOI: 10.1016/j.ejor.2026.09.016*.
- S. Joo and H.-J. Kim\*. "Optimal k-wafer cyclic sequence of dual-armed cluster tool with purge operation". *IEEE Transactions on Automation Science and Engineering, vol. 23, pp. 13950-13965, 2026*.
- J. Park, K. S. Kim, Z. Faturrahman, and H.-J. Kim\*. "MARS: Multi-agent rescheduling framework with large language models for human-centric manufacturing". *Journal of Manufacturing Systems, vol. 88, pp. 903-923, 2026*.
- J. Ahn, S.-H. Cho, H.-Y. Kim, H. Kim, H. Choi, D. Ham, Y. Kim, and H.-J. Kim\*. "A novel health index framework for semiconductor equipment using multi-view data". *IEEE Transactions on Semiconductor Manufacturing, vol. 39, no. 2, pp. 330-343, 2026*.
- W.-J. Shin, I. Choi, S.-H. Cho, and H.-J. Kim\*. "Learning to retrieve containers: A scale-diverse deep reinforcement learning approach for the container retrieval problem". *Transportation Research Part C: Emerging Technologies, vol. 183, 105496, 2026*.
- S.-W. Lee, D.-H. Lee, M.-C. Kim, S.-Y. Lee, and H.-J. Kim\*. "A decomposition-based optimization method for parallel machine scheduling under quality uncertainty in wafer manufacturing". *Journal of Manufacturing Systems, vol. 85, pp. 386-401, 2026*.
- J. Park, I. Choi, and H.-J. Kim\*. "A multi-view attention-based encoder-decoder framework for clustered traveling salesman problem". *IEEE Robotics & Automation Letters, vol. 11, no. 1, pp. 137-144, 2026*.
- W.-J. Shin and H.-J. Kim\*. "Advances in multi-crane scheduling: Extended non-interference modeling and temporal-constraint-based valid inequalities". *European Journal of Operational Research, vol. 331, no. 1, pp. 35-47, 2026*.
- J. Park and H.-J. Kim. "LLM-assisted Rich Preference Elicitation for Multi-Objective Parallel Machine Scheduling". *International Conference on Advances in Production Management Systems (APMS), Bergamo, Italy, 2026*.
- S. Joo and H.-J. Kim. "Optimal Robot Operation Set for Dual-Armed Cluster Tools with Purge Operation". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- S.-H. Cho, D.-Y. Lim, and H.-J. Kim. "Leveraging Product Mix Information for Flexible Job Shop Scheduling in Production Environments". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- H.-Y. Kim, M.-C. Kim, S.-W. Lee, D.-Y. Oh, C.-W. Jung, H.-B. Park, J.-A. Roh, and H.-J. Kim. "Long-Term Outsourcing Planning for Semiconductor Back-End Processes via Dynamic Network Flow Optimization". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- Y. J. Kim, M.-C. Kim, D.-H. Lee, S. K. Yoon, K. Kim, J. Lee, J. Seo, H. Bang, T. Jeong, and H.-J. Kim. "Imitation Learning for Activity Sequencing in Semiconductor Equipment Installation". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- J. Park, J. H. Kim, and H.-J. Kim. "Multi-Objective Scheduling Preference Elicitation with LLMs". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- D.-H. Lee, I. Choi, W.-J. Shin, Y. Lu, and H.-J. Kim. "Real-Time Robotic Assembly Cell Scheduling via Generalizable Multi-Agent Reinforcement Learning". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- M.-C. Kim and H.-J. Kim. "Optimal Control Framework for Timed Event Graphs with Token Delay Regulation: Applications to Robotized Manufacturing Systems". *IEEE International Conference on Automation Science and Engineering (CASE), Shenyang, China, 2026*.
- I. Choi, W.-J. Shin, S. Cho, and H.-J. Kim. "Preference-Guided Multi-Policy Optimization for Flexible Job Shop Scheduling". *the 35th International Joint Conference on Artificial Intelligence (IJCAI), Bremen, Germany, 2026*.
- S.-H. Cho, S.-H. Jung, I. Choi, B.-Y. Choi, B. Han, and H.-J. Kim. "Graph Reinforcement Learning-based Integrated Scheduling for OLED TFT Array Manufacturing". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- S. Joo and H.-J. Kim. "Optimal Robot Operation Set for Dual-Armed Cluster Tools with Purge Operation". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- J. Park, I. Choi, S. Joo, Y. Kim, G. Oh, Y. Song, and H.-J. Kim. "Natural Language-based Modification of Semiconductor Supply Management Spreadsheets using Retrieval-Augmented Generation". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- Y.-H. Kim, S.-W. Lee and H.-J. Kim. "Single Machine Scheduling for a Heat Treatment Process in Display Manufacturing". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- D.-H. Lee, S.-W. Lee and H.-J. Kim. "Manufacturing Environment Prediction Model for Continuous Learning of Bi-Objective Wafer Manufacturing Scheduling". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- D.-Y. Oh, Y. Lim, W.-J. Shin and H.-J. Kim. "Dynamic Control of Scheduling Parameters for Semiconductor Production Lines under Uncertainty". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- W.-J. Shin, J.-K. Jung, S.-H. Cho, I. Choi, S. Tanaka, and H.-J. Kim. "A Learning Framework for the Container Relocation Problem in Container Yards". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- W.-J. Shin, I. Choi, J.-Y Shin, and H.-J. Kim. "Learning-Based UAV Path Planning for Clustered Reconnaissance Targets". *the Spring Conference of Korean Institute of Industrial Engineers, Gyeongju, 2026*.
- S.-W. Lee and H.-J. Kim. "AI-based dark factory design and operation solution". *the Winter Conference of Society for Computational Design and Engineering, Pyeongchang, 2026*.

**2025**

- D. Kim and H.-J. Kim\*. "Noncyclic scheduling of cluster tools using deep reinforcement learning". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 24009-24023, 2025*.
- S.-W. Lee and H.-J. Kim\*. "Single machine scheduling with variable maintenance in the battery manufacturing". *International Journal of Production Research, vol. 63, no. 23, pp. 8859-8879, 2025*.
- J. Ahn and H.-J. Kim\*. "Analysis of conventional robot task sequences during lot switching periods in cluster tools". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 14407-14421, 2025*.
- W.-J. Shin, S.-W. Lee, J.-H. Lee, M.-H. Song, and H.-J. Kim\*. "Scheduling of steelmaking-continuous casting process by integrating deep neural networks with mixed integer programming". *International Journal of Production Research, vol. 63, no. 11, pp.4180-4201, 2025*.
- J.-H. Lee, and H.-J. Kim\*. "Graph-based imitation learning for real-time job shop dispatcher". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 8593-8606, 2025*.
- J.-H. Lee, and H.-J. Kim\*. "Optimal scheduling of timed Petri nets with resource marking and ready times: Application to robotic flow shops". *IEEE Robotics and Automation Letters, vol. 10, no. 4, pp. 3684-3691, 2025*.
- J. Ahn, and H.-J. Kim\*. "A novel mixed integer programming model with precedence relation-based decision variables for non-cyclic scheduling of cluster tools". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 2893-2908, 2025*.
- S.-H. Min, S.-W. Lee, and H.-J. Kim\*. "Parallel machine scheduling with peak energy consumption limit". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 18063-8075, 2025*.
- H.-J. Kim, and J.-H. Lee\*. "Scheduling cluster tools for concurrent processing: deep reinforcement learning with adaptive search". *IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 3783-3796, 2025*.
- S.-H. Cho, S. Jeong, J. Park, B. Choi, P. Han, and H.-J. Kim. "Graph-Based Reinforcement Learning for Dynamic Photolithography Scheduling". *Winter Simulation Conference, Seattle, USA, 2025*.
- I. Choi, S.-Y. Hwang, J. Ahn, J. Lee, S. Joo, K. Kim, H. Lee, Y. Song, and H.-J. Kim. "An Empirical Study on the Assessment of Demand Forecasting Reliability for Fabless Semiconductor Companies". *Winter Simulation Conference, Seattle, USA, 2025*.
- W.-J. Shin, D. Oh, I. Choi, M. Wiktorsson, E. Flores-García, Y. Jeong, and H.-J. Kim. "Learning-based Scheduling for Stochastic Job Shop Scheduling with Mobile Robots". *Winter Simulation Conference, Seattle, USA, 2025*.
- I. Choi, W.-J. Shin, S. Cho, and H.-J. Kim. "Towards Generalizable Multi-Policy Optimization with Self-Evolution for Job Scheduling". *the 39th Annual Conference on Neural Information Processing Systems (NeurIPS), San Diego, USA, 2025*.
- Z. Faturrahman, J. Park, S.-H. Cho, and H.-J. Kim. "Fine-Tuning Large Language Models for Algorithm Selection in the Flexible Job Shop Scheduling Problem". *the 25th Asia-Pacific Industrial Engineering and Management Systems Conference & the 4th International Conference on Smart Manufacturing, Industrial & Logistics Engineering, Hangzhou, China, 2025*.
- S. Joo and H.-J. Kim. "K-Wafer Cyclic Sequence for Scheduling of Dual-Armed Cluster Tool with Purge Operation". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- M.-C. Kim and H.-J. Kim. "Analysis for Steady Schedule Convergence Against Random Time Disruption in Dual-armed Cluster Tools". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- I. Choi and H.-J. Kim. "Adaptive Self-Supervised Learning for Solving Flow Shop Scheduling Problems". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- J. Park, Z. Faturrahman, and H.-J. Kim. "In-Context Learning for User-specified Constraint Enforcement in Discrete Event Simulation". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- W.-J. Shin, J.-K. Jung, S.-H. Cho, and H.-J. Kim. "Deep Reinforcement Learning for the Container Retrieval Problem". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- H.-Y. Kim, W.-J. Shin, S. Joo and H.-J. Kim. "Resource-Constrained Parallel Machine Scheduling for Tire Manufacturing". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- S.-W. Lee, D.-H. Lee, M.-C. Kim, S.-Y. Lee and H.-J. Kim. "Decomposition-Based Optimization Method for Parallel Machine Scheduling under Quality Uncertainty in Wafer Manufacturing". *IEEE International Conference on Automation Science and Engineering (CASE), Los Angeles, USA, 2025*.
- W.-J. Shin and H.-J. Kim. "Mathematical Models and Heuristics for the Multi-Crane Scheduling Problem with Temporal Constraints". *the 11th IFAC Conference on Manufacturing Modelling, Management and Control (IFAC MIM), Trondheim, Norway, 2025*.
- S. Jeong, C. Kwon and H.-J. Kim. "Self-Supervised Job Grouping for Parallel Machine Scheduling with Family Setups". *the 11th IFAC Conference on Manufacturing Modelling, Management and Control (IFAC MIM), Trondheim, Norway, 2025*.
- H.-Y. Kim, S.-W. Lee, M.-C. Kim, D.-Y. Oh, H.-J. Kim, C.-W. Jung, H.-B. Park and J.-A. Roh. "Optimization of Outsourcing Allocation across Periods in the Semiconductor EDS Process". *the Autumn Conference of Korean Institute of Industrial Engineers, Daejeon, 2025*.
- J. Park, K. S. Kim, Z. Faturrahman, and H.-J. Kim. "In-Context Learning for User-driven Rescheduling". *the Autumn Conference of Korean Institute of Industrial Engineers, Daejeon, 2025*.
- M.-C. Kim and H.-J. Kim. "Convergence Analysis of 1-Cyclic Schedule in Dual-armed Cluster Tools". *the Autumn Conference of Korean Institute of Industrial Engineers, Daejeon, 2025*.
- K. S. Kim, M. Jang, J. Park, S.-W. Lee and H.-J. Kim. "A multi-objective scheduling framework for batching and dispatching in parallel machine scheduling with job families". *the Autumn Conference of Korean Institute of Industrial Engineers, Daejeon, 2025*.
- Z. Faturrahman, J. Park and H.-J. Kim. "Fine-Tuning Large Language Models for Algorithm Selection in the Flexible Job Shop Scheduling Problem". *the Autumn Conference of Korean Institute of Industrial Engineers, Daejeon, 2025*.
- S.-H. Cho, S.-H. Jung, I. Choi, B. Choi, B. Han and H.-J. Kim. "Multi-objective Scheduling for Photo Process Using Reinforcement Learning". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.
- W.-J. Shin and H.-J. Kim. "Solving the Container Retrieval Problem Using a Deep Reinforcement Learning Approach". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.
- S.-W. Lee, D.-H. Lee, M.-C. Kim, S.-Y. Lee and H.-J. Kim. "Parallel Machine Scheduling Considering Quality Uncertainty in Wafer Manufacturing". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.
- S. Jeong, C. Kwon and H.-J. Kim. "Self-Supervised Job Grouping for Parallel Machine Scheduling with Family Setups". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.
- I. Choi and H.-J. Kim. "A Self-Imitation Learning Framework for Neural Constructive Heuristics Optimization". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.
- S. Hwang and H.-J. Kim. "Bi-objective Parallel Machine Scheduling for the Upstream Process (USP) in Biopharmaceutical Production". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2025*.

**2024**

- J. Ahn, and H.-J. Kim\*. "A branch and bound algorithm for scheduling of flexible manufacturing systems". *IEEE Transactions on Automation Science and Engineering, vol. 21, no. 3, pp. 4382-4396, 2024*.
- S.-W. Lee, and H.-J. Kim\*. "Single machine scheduling with maintenance and position-based job eligibility constraints for battery manufacturing". *Optimization Letters, vol. 18, pp. 2221-2234, 2024*.
- H.-J. Kim, and J.-H. Lee\*. "Deep reinforcement learning with a look-ahead search for robotic cell scheduling". *IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 54, no. 1, pp. 622-633, 2024*.
- S.-H. Cho, H.-J. Kim, and L. Mönch. "Reinforcement Learning for Unrelated Parallel Machine Scheduling with Release Dates, Setup Times, and Machine Eligibility". *Winter Simulation Conference, Orlando, USA, 2024*.
- D. Kim, M.-C. Kim and H.-J. Kim. "Noncyclic Scheduling of Single-Armed Cluster Tools with Multiple Wafer Types and Wafer Residency Time Constraints Using Deep Reinforcement Learning". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- M.-C. Kim and H.-J. Kim. "Analysis and Control of Time Delays in a Cluster Tool for a Cyclic Schedule". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- J.-K. Jung, S.-H. Cho, W.-J. Shin and H.-J. Kim. "Block Relocation Problem with Deep Reinforcement Learning". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- J. Park, S.-W. Lee, S. Jeong, H.-J. Kim, J. Li and S.-I. Mun. "Variable Neighborhood Search with Reinforcement Learning for Parallel Machine Batching Scheduling". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- W.-J. Shin and H.-J. Kim. "Graph-based Deep Reinforcement Learning for Crane Scheduling with Temporal Constraints". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- J.-H. Lee, J. Park and H.-J. Kim. "Tree-based Dispatcher for Job Shop Scheduling". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- J. Ahn and H.-J. Kim. "Analysis of Backward Sequence in Lot Switching Periods for Single-Armed Cluster Tools". *IEEE International Conference on Automation Science and Engineering (CASE), Bari, Italy, 2024*.
- S.-Y. Lee, J.-H. Lee, S.-Y. Hwang and H.-J. Kim. "Multi-Objective Parallel Machine Scheduling with Sequence-Dependent Setups and Additional Resource Constraints: A Case Study of Refrigerator Manufacturing Lines". *22nd Triennial Congress of the International Ergonomics Association (IEA), Jeju, Korea, 2024*.
- S. Jeong, S.-W. Lee, J. Park and H.-J. Kim. "A hybrid VNS-RL approach for parallel machine batch scheduling in air conditioner manufacturing". *22nd Triennial Congress of the International Ergonomics Association (IEA), Jeju, Korea, 2024*.
- D. Kim and H.-J. Kim. "Reinforcement learning for noncyclic scheduling of cluster tools with residency time constraints". *IEEE International Conference on Automation in Manufacturing, Transportation and Logistices (ICAMaL), Hong Kong, China, 2024*.
- S.-H. Cho, W.-J. Shin, J. Ahn, S. Joo and H.-J. Kim. "Dynamic Crane Scheduling with Reinforcement Learning for a Steel Coil Warehouse". *IEEE International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 2024*.
- W.-J. Shin, S.-H. Cho, J. Ahn, S. Joo and H.-J. Kim. "Dynamic Crane Scheduling with Reinforcement Learning". *the 7th International Workshop on Production and Logistics, Yokohama, Japan, 2024*.
- J. Ahn and H.-J. Kim. "Dual-armed cluster tool scheduling with neural assisted heuristic search". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- J. Park, I. Choi, S.-H. Cho and H.-J. Kim. "Deep Reinforcement Learning-based Encoder-Decoder Framework for The Clustered Traveling Salesman Problem". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- S.-W. Lee and H.-J. Kim. "Scheduling on two parallel machines with maintenance and position-based job eligibility". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- S. Joo and H.-J. Kim. "K-Wafer Cyclic Sequence for Scheduling of Dual-Armed Cluster Tool with 1-Periodic Cleaning". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- S.-H. Cho, J. Jeong, W.-J. Shin and H.-J. Kim. "Self-Supervised Imitation Learning for the Blocks Relocation Problem". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- W.-J. Shin and H.-J. Kim. "A novel non-interference strategy and mixed integer programming models for the multi-crane scheduling problem". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2024*.
- H.-Y. Kim, W.-J. Shin, S.-H. Joo, C.-W. Kim, T.-J. Park, M.-J. Kim and H.-J. Kim. "Resource-constrained parallel machine scheduling". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.
- J.-H. Lee and H.-J. Kim. "Tree-based dispatcher for solving job shop scheduling problems". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.
- W.-J. Shin and H.-J. Kim. "Crane scheduling with graph-based deep reinforcement learning". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.
- D.-Y. Kim and H.-J. Kim. "Deep reinforcement learning for noncyclic cluster tool scheduling considering wafer residency time". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.
- M.-C. Kim and H.-J. Kim. "Scheduling cluster tools under wafer quality control: time delay analysis". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.
- K.S. Kim, M. Jang, S.-W. Lee, J. Park and H.-J.Kim. "Dynamic batching for multi-objective parallel machine scheduling". *the Spring Conference of Korean Institute of Industrial Engineers, Yeosu, 2024*.

**2023**

- H.-J. Kim, and J.-H. Lee\*. "Look-ahead based reinforcement learning for robotic flow shop scheduling". *Journal of Manufacturing Systems, 68, pp. 160-175, 2023*.
- J.-H. Lee and H.-J. Kim\*. "The impact of processing time variations on swap sequence performance in dual-armed cluster tools". *IEEE Transactions on Automation Science and Engineering, vol. 20, no. 4, pp. 2668-2677, 2023*.
- W.-J. Shin and H.-J. Kim. "An Efficient Simulation-Based Optimization Algorithm for a Crane Scheduling Problem in a Steelmaking Shop". *Winter Simulation Conference, San Antonio, USA, 2023*.
- J. Ahn, H.-Y. Kim, S.-H. Cho, H.-Y. Kim, H. Choi, D. Ham and H.-J. Kim. "Semiconductor Equipment Health Monitoring with Multi-View Data". *Winter Simulation Conference, San Antonio, USA, 2023*.
- W.-J. Shin and H.-J. Kim. "An Exact Algorithm for the Crane Scheduing Problem in a Steelmaking Shop". *IEEE International Conference on Automation Science and Engineering (CASE), Auckland, New Zealand, 2023*.
- S. Joo, H.-J. Kim and T.-E. Lee. "Strategic Backward Operation Ordering for Scheduling Single Armed Cluster Tools with Purge Operation". *IEEE International Conference on Automation Science and Engineering (CASE), Auckland, New Zealand, 2023*.
- H.-Y. Kim, J.-H. Lee and H.-J. Kim. "Cycle Planning for Concurrent Processing in a Dual-Armed Cluster Tool". *IEEE International Conference on Automation Science and Engineering (CASE), Auckland, New Zealand, 2023*.
- D.-Y. Kim and H.-J. Kim. "Reinforcement Learning for Non-cyclic Scheduling of Single-armed Cluster Tools with Multiple Wafer Types". *IEEE International Conference on Automation Science and Engineering (CASE), Auckland, New Zealand, 2023*.
- H.-Y. Kim, J.-H. Lee and H.-J. Kim. "Determining the Input Sequence of Wafer Type in Semiconductor Manufacturing Equipment for Concurrent Processing". *the Autumn Conference of Korean Institute of Industrial Engineers, Ulsan, 2023*.
- W.-J. Shin, S.-H. Cho, J. Ahn, S. Joo and H.-J. Kim. "Solving the Dynamic Crane Scheduling Problem in a Steel Coil Warehouse with Reinforcement Learning". *the Autumn Conference of Korean Institute of Industrial Engineers, Ulsan, 2023*.
- S. Joo, J. Ahn, H.-Y. Kim, J. Park, J. Kim, S. Park and H.-J. Kim. "Routing Algorithm for Enhancement of Semiconductor Chip Quality". *the Autumn Conference of Korean Institute of Industrial Engineers, Ulsan, 2023*.
- C.-Y. Kim and H.-J. Kim. "Hybrid Flow-Shop Scheduling Problem with No-wait and Blocking". *the Autumn Conference of Korean Institute of Industrial Engineers, Ulsan, 2023*.
- S.-W. Lee, and H.-J. Kim. "Scheduling for battery manufacturing with position-based allocation constraints". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- J.-H. Lee and H.-J. Kim. "Active schedule-based imitation learning for job shop scheduling". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- S.-H. Cho, J.-H. Lee, D.-Y. Kim, M.-C. Kim, D.-H. Yang, J.-H. Park, and H.-J. Kim. "Optimization algorithm for long-term load balancing in shipbuilding". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- H.-J. Kim, W.-J. Shin, S.-W. Lee, C.-Y. Kim, I. Song, S. Moon, S. Lee, and D. Seo. "Scheduling application cases: focused on insulation material production". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- W.-J. Shin and H.-J. Kim. "Crane scheduling problem in a steelmaking shop". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- D.-Y. Kim and H.-J. Kim. "Reinforcement learning for non-cyclic scheduling of single-armed cluster tool". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.
- J. Ahn and H.-J.Kim. "A novel mixed integer programming for non-cyclic cluster tool scheduling with a timed Petri net". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2023*.

**2022**

- H. Yang, J.-H. Lee, S. H. Lee, S. G. Lee, H. R. Kim, and H.-J. Kim\*. "A multi-manned assembly line worker assignment and balancing problem with positional constraints". *IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 7786-7793, 2022*.
- J. Ahn, D.-Y. Kim, M. Song, J. Min, J. Hwang, J. Kwon, and H.-J. Kim\*. "l1 trend filtering-based change point detection for pumping line balance of deposition equipment". *IEEE Transactions on Semiconductor Manufacturing, vol. 35, no. 1, pp. 137-145, 2022*.
- H.-J. Kim and J.-H. Lee\*. "Scheduling of dual-gripper robotic cells with reinforcement learning". *IEEE Transactions on Automation Science and Engineering, vol. 19, no. 2, pp. 1120-1136, 2022*.
- J. Kim and H.-J. Kim\*. "An exact algorithm for an identical parallel additive machine scheduling problem with multiple processing alternatives". *International Journal of Production Research, vol. 60, no. 13, pp. 4070-4089, 2022*.
- H.-J. Kim, E.-S. Kim, and J.-H. Lee\*. "Scheduling of step-improving jobs with an identical improving rate". *Journal of the Operational Research Society, vol. 73, no. 5, pp. 1127-1136, 2022*.
- J.-H. Lee and H.-J. Kim\*. "Reinforcement learning for robotic flow shop scheduling with processing time variations". *International Journal of Production Research, vol. 60, no. 7, pp. 2346-2368, 2022*.
- H.-J. Kim, E.-S. Kim, J.-H. Lee\*, L. Tang, and Y. Yang. "Single-machine scheduling with energy generation and storage systems". *International Journal of Production Research, vol. 60, no. 23, pp. 7033-7052, 2022*.
- D.-Y. Kim and H.-J. Kim. "Monte Carlo tree search-based algorithm for dynamic job shop scheduling with automated guided vehicles". *Winter Simulation Conference, Singapore, 2022*.
- J.-H. Lee and H.-J. Kim. "Imitation learning for real-time job shop scheduling using graph-based representation". *Winter Simulation Conference, Singapore, 2022*.
- S.-H. Cho, J. Ahn, D.-Y. Kim, D. Ham, H.-Y. Kim and H.-J. Kim. "Maintenance time reduction for semiconductor manufacturing tools". *International Symposium on Semiconductor Manufacturing Intelligence, Kinmen, Taiwan, 2022*.
- J. H. Lee and H.-J. Kim. "Job shop scheduling using graph-based imitation learning". *Informs Annual Meeting, Indianapolis, USA, 2022*.
- J. Ahn and H.-J. Kim. "A timed petri net based optimization approach for flexible manufacturing system scheduling". *Informs Annual Meeting, Indianapolis, USA, 2022*.
- D.-Y. Kim and H.-J. Kim. "Integrated scheduling of machines and transport robots in dynamic job shops with a timed petri net". *IEEE International Conference on Automation Science and Engineering (CASE), Online, 2022*.
- J. Ahn and H.-J. Kim. "Optimal scheduling of flexible manufacturing systems with a timed petri net". *IEEE International Conference on Automation Science and Engineering (CASE), Online, 2022*.
- W.-J. Shin, S.-W. Lee, M. Song, Y. Kim, J.-H. Lee and H.-J. Kim. "Machine learning and mixed integer programming for the machine assignment in steelmaking-process". *the Autumn Conference of Korean Institute of Industrial Engineers, Incheon, 2022*.
- S.-H. Cho and H.-J. Kim. "Graph-based deep reinforcement learning for the resource constrained project scheduling problem". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.
- S.-H Min and H.-J. Kim. "Identical parallel machine scheduling with peak energy consumption constraints". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.
- J. Ahn and H.-J. Kim. "Optimal algorithm for flexible manufacturing systems". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.
- J.-H. Lee, D.-Y. Kim, S.-H. Cho, and H.-J. Kim. "Reinforcement Learning for Resource Leveling in Multiple Projects". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.
- J.-H. Lee and H.-J. Kim. "Dynamic Job Shop Scheduling using Graph-based Imitation Learning". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.
- S.-W. Lee, W.-J. Shin, M. Song, Y. Kim, J.-H. Lee and H.-J. Kim. "Machine assignment for steelmaking-continuous casting manufacturing with machine learning". *the Spring Conference of Korean Institute of Industrial Engineers, Jeju, 2022*.

**2021**

- J.-H. Lee and H.-J. Kim\*. "A heuristic algorithm for identical parallel machine scheduling: splitting jobs, sequence-dependent setup times, and limited setup operators". *Flexible Services and Manufacturing Journal, vol. 33, pp. 992-1026, 2021*.
- J. Kim and H.-J. Kim\*. "Parallel machine scheduling with multiple processing alternatives and sequence-dependent setup times". *International Journal of Production Research, vol. 59, no. 18, pp. 5438-5453, 2021*.
- Y.-I. Kim and H.-J. Kim\*. "Rescheduling of unrelated parallel machines with job-dependent setup times under forecasted machine breakdown". *International Journal of Production Research, vol. 59, no. 17, pp. 5236-5258, 2021*.
- H.-J. Kim and J.-H. Lee\*. "Scheduling uniform parallel dedicated machines with job splitting, sequence-dependent setup times, and multiple servers". *Computers & Operations Research, vol. 126, pp. 105115, 2021*.
- H.-J. Kim and J.-H. Lee\*. "Cyclic robot scheduling for 3D printer-based flexible assembly systems". *Annals of Operations Research, vol. 298, pp. 339-359, 2021*.
- J.-H. Lee, H. Jang and H.-J. Kim\*. "Iterative job splitting algorithms for parallel machine scheduling with job splitting and setup resource constraints". *Journal of the Operational Research Society, vol. 72, no. 4, pp. 780-799, 2021*.
- J.-H. Lee, H.-J. Kim, Y. Kim, Y. B. Kim, B.-H. Kim, and G.-H. Chung. "Machine learning-based periodic setup changes for semiconductor manufacturing machines". *Winter Simulation Conference, Online, 2021, pp. 1-10*.
- W.-J. Shin, S.-W. Lee, S.-S. Park, and H.-J. Kim. "Integrated scheduling of machines and cranes for steelmaking-continuous casting production". *INFORMS Annual Meeting, Online, 2021*.
- S.-W. Lee, W. -J. Shin, and H.-J. Kim. "Single machine scheduling with job quality levels for battery manufacturing". *INFORMS Annual Meeting, Online, 2021*.
- H. Yang, J.-H. Lee, and H.-J. Kim. "Assembly line worker assignment and balancing problem with positional constraints". *Advances in Production Management Systems (APMS), Online, 2021, pp. 3-11*.
- D.-Y. Kim, H.-J. Kim. "Integrated Production and Material Handling Scheduling with Reinforcement Learning". *IEEE International Conference on Automation Science and Engineering (CASE), Online, 2021*.
- J. Ahn, D.-Y. Kim, M. Song, J. Min, J. Hang, J. Kwon and H.-J. Kim. "Change point detection for pumping line balance of deposition equipment". *IEEE International Conference on Automation Science and Engineering (CASE), Online, 2021*.
- S.-W. Lee, and H.-J. Kim. "Single machine scheduling for a pressing process in battery manufacturing". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2021*.
- D.-Y. Kim, J.-H.Lee, S.-H. Min, S.-H. Cho, J.-H. Park, H.-S. Min, G.-W. Kim, M.-S. Kim, and H.-J.Kim. "Resource leveling in shipyard cargo hold process through reinforcement learning". *the Autumn Conference of Korean Institute of Industrial Engineers, Seoul, 2021*.
- H. Yang, J.-H. Lee, and H.-J. Kim. "Operation and optimization of the automotive parts assembly line considering worker skill levels". *the Summer Conference of Society for Computational Design and Engineering, Online, 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제 32건이다. 과제명·지원기관·기간은 연구실 표기다. 교수의 성균관대학교 재직 시기에 시작해 KAIST 부임 뒤까지 이어지는 과제도 포함한다.[^projects][^prof]

- 반도체 Fab 생산 예측 시뮬레이션 활용 강화학습 연구 (지원 Samsung Electronics; 기간 2026.03-2027.02; translation Reinforcement learning for semiconductor fab scheduling)
- AI 기반 생산설비 설치 최적 스케줄링 기술 개발 (지원 Samsung Electronics; 기간 2025.10-2030.09; translation Development of AI-based scheduling for production equipment installation)
- 산업 특화형 피지컬 AI 선도모델 수립 및 PoC (PI: Prof. Jang) (지원 과학기술정보통신부; 기간 2025.08-2025.12; translation Industry-specific physical AI model and PoC)
- 인공지능기반 추계최적화 알고리즘 개발 기초연구실 (지원 기초연구실/한국연구재단; 기간 2025.06-2028.05; translation Basic research lab for AI-based stochastic optimization algorithms)
- 강화학습/LLM을 활용한 가공라인 스케줄링 엔진 개발 (지원 LG Electronics; 기간 2025.05-2025.12; translation Scheduling algorithm for a production line with reinforcement learning and LLM)
- LLM기반 공급사슬망 운영 최적화 방법론 개발 (지원 Samsung Electronics; 기간 2025.04-2026.03; translation Optimization of supply chain network operations with LLM)
- AI 기반 목표 외주비 산출 모델링 방법론 개발 (지원 Samsung Electronics; 기간 2025.03-2026.02; translation Modeling target outsourcing cost estimation with AI)
- 프로젝트 시운전 및 Master 스케줄 최적화 (지원 Samsung E&A; 기간 2024.11-2025.10; translation Commissioning and master schedule optimization)
- 국방지능형 군집체계 연구센터 (PI: Prof. Moon) (지원 ITRC; 기간 2024.07-2031.12; translation Defense intelligent swarm systems research center)
- 제조 환경 변화에 유연하게 대응가능한 자율운영 스케줄링 방법론 개발 (지원 한우물파기/한국연구재단; 기간 2024.05-2034.04; translation Autonomous scheduling for swift and efficient adaptation to dynamic manufacturing environments)
- 강화학습 기반 OLED FAB Multi-agent 생산스케줄링 연구 (지원 Samsung Display; 기간 2024.03-2027.02; translation Reinforcement learning-based OLED FAB multi-agent scheduling)
- AI 기반 시나리오별 최적 운영계획 수립 알고리즘 개발 (지원 Samsung Electronics; 기간 2024.03-2025.02; translation AI-based algorithm for optimal operation plans for various scenarios)
- Fab 대상 생산 계획 운영 최적화를 위한 스케줄링 알고리즘 개발 (지원 소부장 으뜸기업 국책과제 (SK Siltron); 기간 2024.04-2024.12; translation Scheduling algorithm to optimize production planning operations)
- 디지털트윈 기반 반제품 생산 스케줄링 (with Prof. Hayong Shin) (지원 Hankook Tire; 기간 2023.11-2024.10; translation Production scheduling with a digital twin)
- 강화학습 기반 unrelated parallel machine 스케줄링 (지원 VMS Solutions; 기간 2023.06-2024.05; translation Unrelated parallel machine scheduling with reinforcement learning)
- 생산계획 최적화를 위한 AI기반 방법론 개발 (지원 LG Electronics; 기간 2023.07-2024.02; translation Production planning with AI)
- 강화학습 기반의 동적 크레인 스케줄링 (지원 KAIST; 기간 2023.07-2023.12; translation Solving dynamic crane scheduling problem using reinforcement learning)
- DRAM 제품 설계 품질 향상을 위한 Router 개발 (지원 SK Hynix; 기간 2023.03-2023.10; translation Routing algorithm for DRAM circuit design)
- 최적화 기반의 제강 크레인 관제 알고리즘 개발 (지원 POSCO; 기간 2022.10-2023.09; translation Optimization-based crane scheduling)
- 최적 혼류 생산계획 수립 모델 개발 (지원 LG Electronics; 기간 2022.05-2022.12; translation Production planning and scheduling for multiple orders)
- 강화학습 기반 Job Shop 스케줄링 알고리즘 개발 (지원 VMS Solutions; 기간 2022.04-2023.03; translation Reinforcement learning for job shop scheduling)
- 제조시스템 최적화를 위한 강화학습 기반의 메타 스케줄링 방법론 개발 (지원 중견연구/한국연구재단; 기간 2022.03-2025.02; translation Reinforcement learning based meta-scheduling for manufacturing systems)
- 강화학습 기반 프로젝트 스케줄링 (지원 Samsung Heavy Industries; 기간 2022.03 - 2024.02; translation Reinforcement learning for project scheduling)
- X-DEC Slim Layout 배선 최적화 알고리즘 개발 (지원 SK Hynix; 기간 2022.03-2022.09; translation Development of a wiring optimization algorithm for X-DEC Slim layout)
- 강화학습을 활용한 크레인 스케줄링 (지원 정석물류학술재단; 기간 2022.01-2022.12; translation Reinforcement learning for crane scheduling)
- 강화학습을 통한 화물창 부하 최적화 (지원 Samsung Heavy Industries; 기간 2021.07-2021.11; translation Development of a reinforcement learning algorithm for workload balancing of ship cargo production)
- 반도체 자동 반송장비 OHT 시스템 트랙 이물질 감지 알고리즘 개발 (지원 KAIST; 기간 2021.07-2021.12; translation Abnormal substances detection algorithm for the semiconductor OHT system)
- 제강 Crane 관제 알고리즘 개발 (지원 POSCO; 기간 2021.06-2022.05; translation Development of an algorithm for crane control)
- 원익IPS-KAIST 반도체 장비 디지털 혁신 연구센터 (지원 Wonik IPS; 기간 2020.04-2023.03; translation Wonik IPS-KAIST research center for digital transformation of semiconductor equipment)
- 글로벌 공급 사슬의 조립 및 물류를 위한 사이버물리시스템 (지원 산업통상자원부 국제공동기술개발사업; 기간 2019.06-2022.05; translation Cyber-physical assembly and logistics systems in global supply chains)
- 강화학습 기반 생산시스템 스케줄링 이론 및 알고리즘 개발 (지원 신진연구/한국연구재단; 기간 2019.03-2022.02; translation Development of scheduling theory and algorithms with reinforcement learning for manufacturing systems)
- 에너지를 고려한 생산시스템 최적화: 생산계획, 스케줄링, 강화학습 (지원 글로벌연구네트워크/한국연구재단; 기간 2019.03-2021.12; translation Optimization of production systems for industrial energy efficiency: production planning & scheduling and reinforcement learning)

## 수상과 선정

교수 소개와 News 페이지에서 날짜를 확인한 수상·선정·후보 지명 23건이다. 범위는 2022년 2월–2026년 2월이며, 연도만 있는 항목은 그 연도만 적었다. 같은 논문상을 두 페이지가 함께 적은 경우에는 한 번만 싣는다.[^prof][^news]

- 2026-02 · Woo-Jin Shin이 KAIST 공과대학의 Best Ph.D. Dissertation Award를 받았다.
- 2025-11 · Jehun Lee가 대한산업공학회 추계학술대회 박사학위논문 경진대회에서 우수상을 받았다.
- 2025-11 · Zuhdi Faturrahman, Jimin Park, Sang-Hyun Cho가 유연한 작업장 일정 문제의 알고리즘 선택을 위한 대형 언어 모델 연구로 APIEMS·SMILE 공동 학술대회에서 Excellent Paper Award를 받았다.
- 2025-11 · 김현정이 과학기술정보통신부 장관 표창을 받았다.
- 2025-11 · 김현정이 대한산업공학회의 우헌신진연구자상을 받았다.
- 2025-08 · Sanghyun Joo가 퍼지 작업이 있는 양팔 클러스터 장비의 순환 일정 연구로 2025 IEEE CASE의 Best Student Paper Award를 받았다.
- 2024-12 · 김현정이 KAIST 산업및시스템공학과의 Best Teacher Award를 받았다.
- 2024-11 · Inguk Choi, Jimin Park, Sang-Hyun Cho가 강화학습을 이용한 무인기 임무 계획 연구로 국방대학교·KAIST 공동학술대회에서 금상을 받았다.
- 2024-07 · Jeongsun Ahn이 2024 김영한글로벌리더장학생으로 선정됐다.
- 2024-01 · Woo-Jin Shin, Sang-Hyun Cho, Jeongsun Ahn, Sang-Hyun Joo가 강화학습을 이용한 동적 크레인 일정 과제로 2023 Advanced Manufacturing and Intelligence Challenge 성과발표회에서 최우수상을 받았다.
- 2024 · 김현정이 IEEE Transactions on Automation Science and Engineering의 Outstanding Associate Editor로 선정됐다.
- 2024 · 김현정이 IEEE Transactions on Automation Science and Engineering의 Outstanding Reviewer로 선정됐다.
- 2024 · 김현정이 한국경영과학회지의 Best Reviewer Award를 받았다.
- 2023-12 · Jehun Lee, Duyeon Kim, Woo-Jin Shin, Jeongsun Ahn이 Winter Simulation Conference의 2023 Simulation Challenge에서 1위를 차지했다.
- 2023-12 · 김현정이 로봇 셀의 강화학습 일정 연구로 IEEE Robotics & Automation Society의 반도체 제조 자동화 기술위원회에서 2023 Best Semiconductor Manufacturing Automation Paper in Theory를 받았다.
- 2023-09 · Jehun Lee가 한국앤컴퍼니·KAIST AI 경진대회에서 우수상을 받았다.
- 2023-06 · Jeongsun Ahn, Duyeon Kim, 김현정이 증착 장비 배기선의 균형 변화 탐지 논문으로 2022 IEEE T-SM Best Paper Award의 Honorable Mention(입선)을 받았다.
- 2023-06 · 김현정이 2022 IEEE Robotics and Automation Letters의 Outstanding Associate Editor 후보로 지명됐다.
- 2023-06 · Woo-Jin Shin이 대한산업공학회 석사학위논문 경진대회에서 우수상을 받았다.
- 2023 · 김현정이 IEEE Robotics and Automation Letters의 Distinguished Service Award를 받았다.
- 2022-12 · 김현정이 KAIST 공과대학의 Technology Innovation Award를 받았다.
- 2022-12 · 김현정이 KAIST 산업및시스템공학과의 Best Academic Award를 받았다.
- 2022-02 · 김현정이 KAIST의 Song-Am Distinguished Research Award를 받았다.

## 연구실 소식

News 페이지의 2023년 8월–2026년 9월 연구 발표 소식 20건이다. 수상과 선정은 앞 절에 모았다.[^news]

- 2026-09 · Jimin Park가 이탈리아 베르가모의 2026 APMS에서 연구를 발표했다.
- 2026-08 · Sang-Hyun Cho, Sanghyun Joo, Hong-Yeon Kim, Jimin Park, Min-Chan Kim, Yong Jae Kim, Dong-Ha Lee가 중국 선양의 2026 IEEE CASE에서 연구를 발표했다.
- 2026-08 · Inguk Choi가 독일 브레멘의 IJCAI에서 연구를 발표했다.
- 2026-06 · Sang-Hyun Cho, Sanghyun Joo, Jimin Park, Yonghwan Kim, Dong-Ha Lee, Dong-Yoon Oh, Woo-Jin Shin이 경주의 대한산업공학회 춘계학술대회에서 연구를 발표했다.
- 2026-02 · Sang-Wook Lee가 평창의 한국CDE학회 동계학술대회에서 연구를 발표했다.
- 2025-12 · Sang-Hyun Cho, Inguk Choi, Woo-Jin Shin이 미국 시애틀의 2025 Winter Simulation Conference에서 연구를 발표했다.
- 2025-12 · Inguk Choi가 미국 샌디에이고의 NeurIPS에서 연구를 발표했다.
- 2025-11 · Zuhdi Faturrahman이 중국 항저우의 APIEMS에서 연구를 발표했다.
- 2025-11 · Hong-Yeon Kim, Min-Chan Kim, Jimin Park, Zuhdi Faturrahman, Seojin Kim이 대전의 대한산업공학회 추계학술대회에서 연구를 발표했다.
- 2025-08 · Sanghyun Joo, Woo-Jin Shin, Hong-Yeon Kim, Jimin Park, Min-Chan Kim, Inguk Choi, Dong-Ha Lee가 미국 로스앤젤레스의 2025 IEEE CASE에서 연구를 발표했다.
- 2025-07 · Woo-Jin Shin과 Sohyun Jung이 노르웨이 트론헤임의 IFAC MIM에서 연구를 발표했다.
- 2025-06 · Sang-Wook Lee, Inguk Choi, Sang-Hyun Cho, Sohyun Jung, Woo-Jin Shin, Seon-Young Hwang이 제주의 대한산업공학회 춘계학술대회에서 연구를 발표했다.
- 2024-12 · Sang-Hyun Cho가 미국 올랜도의 2024 Winter Simulation Conference에서 연구를 발표했다.
- 2024-08 · Duyeon Kim, Jehun Lee, Jeongsun Ahn, Woo-Jin Shin, Min-Chan Kim, Jimin Park, Ji-Kwang Jung이 이탈리아 바리의 2024 IEEE CASE에서 연구를 발표했다.
- 2024-08 · Sohyun Jung과 So-Young Lee가 제주의 2024 국제인간공학회 학술대회에서 연구를 발표했다.
- 2024-08 · Duyeon Kim이 홍콩의 2024 ICAMaL에서 연구를 발표했다.
- 2024-05 · Sang-Hyun Cho가 일본 요코하마의 2024 ICRA에서 연구를 발표했다.
- 2024-03 · Woo-Jin Shin이 일본 요코하마의 International Workshop on Production and Logistics에서 연구를 발표했다.
- 2023-12 · Jeongsun Ahn과 Woo-Jin Shin이 미국 샌안토니오의 2023 Winter Simulation Conference에서 연구를 발표했다.
- 2023-08 · Duyeon Kim, Woo-Jin Shin, Sang-Hyun Joo, Hong-Yeon Kim이 뉴질랜드 오클랜드의 2023 IEEE CASE에서 연구를 발표했다.

## 연락과 위치

- 주소: 대전광역시 유성구 대학로 291 KAIST 산업경영학동 E2-1[^home]
- 교수 사무실: E2-1 4207호, 전화 042-350-3134, 이메일 hyunjungkim@kaist.ac.kr[^prof]
- 연구실: E2-1 4226호, 전화 042-350-3174[^members]
## 각주

[^home]: 연구실 첫 화면. 「Manufacturing and Service Systems Lab」, 연구 분야, 연구 방법, 응용, 주소. <https://msslab.kaist.ac.kr>, 관측 2026-10-30.
[^prof]: 연구실 Professor 페이지. 이름·직위·학력·경력·학술 활동·수상·교수 연락처. <https://msslab.kaist.ac.kr/Professor/professor>, 관측 2026-10-31.
[^gggs]: KAIST 녹색성장지속가능대학원 전체 교수진의 김현정 카드. 소속 「녹색성장지속가능대학원」「산업및시스템공학과」, 연구 분야 「스마트 제조, 스케줄링, 운영 관리」. <https://gggs.kaist.ac.kr/all-professor>, 관측 2026-10-30.
[^members]: 연구실 Researchers 페이지. 현재 구성원의 과정·연구 주제·학교 이메일과 연구실 위치·전화. <https://msslab.kaist.ac.kr/Professor/students>, 관측 2026-10-31.
[^alumni]: 연구실 Alumni 페이지. 2017–2026년 학위 항목·학위 논문. <https://msslab.kaist.ac.kr/Professor/alumni>, 관측 2026-10-31.
[^pubs]: 연구실 Publications 페이지. 국제 학술지·국제 학회·국내 학회의 제목·전체 저자·발표처·연도 표기. <https://msslab.kaist.ac.kr/Publications/publications>, 관측 2026-10-31.
[^projects]: 연구실 Projects 페이지. 과제명·지원기관·기간. <https://msslab.kaist.ac.kr/Publications/projects>, 관측 2026-10-31.
[^news]: 연구실 News 페이지. 날짜별 연구 발표와 수상·선정 소식. <https://msslab.kaist.ac.kr/news>, 관측 2026-10-31.
[^p1]: I. Choi, W.-J. Shin, S.-H. Cho, H.-J. Kim, Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence, 6156-6165 (2026). <https://doi.org/10.24963/ijcai.2026/685> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^p2]: I. Choi, W.-J. Shin, S.-H. Cho, H.-J. Kim, Advances in Neural Information Processing Systems 38 Main Conference (NeurIPS 2025) (2025). <https://doi.org/10.52202/085713-0828> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper_files/paper/2025/hash/2330c4be5e12c504705ba1db8a507966-Abstract-Conference.html>, 관측 2026-10-31.
[^p3]: S.-W. Lee, H.-J. Kim, International Journal of Production Research 63, 8859-8879 (온라인 2025-06-12). <https://doi.org/10.1080/00207543.2025.2516764> 초록 기준(OpenAlex 등록 초록). 서지: Crossref 등록 기록 <https://api.crossref.org/works/10.1080/00207543.2025.2516764>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^p4]: D. Kim, H.-J. Kim, IEEE Transactions on Automation Science and Engineering 22, 24009-24023 (2025). <https://doi.org/10.1109/TASE.2025.3632534> 초록 기준(OpenAlex 등록 초록). 서지: Crossref 등록 기록 <https://api.crossref.org/works/10.1109/TASE.2025.3632534>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^p5]: W.-J. Shin 외, H.-J. Kim, International Journal of Production Research 63, 4180-4201 (온라인 2024-12-10). <https://doi.org/10.1080/00207543.2024.2439369> 초록 기준(OpenAlex 등록 초록). 서지: Crossref 등록 기록 <https://api.crossref.org/works/10.1080/00207543.2024.2439369>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^p6]: S.-H. Cho 외, H.-J. Kim, 2024 IEEE International Conference on Robotics and Automation (ICRA), 16545-16552 (2024). <https://doi.org/10.1109/icra57147.2024.10610858> 초록 기준(OpenAlex 등록 초록). 서지: Crossref 등록 기록 <https://api.crossref.org/works?rows=3&query.bibliographic=Dynamic%20Crane%20Scheduling%20with%20Reinforcement%20Learning%20for%20a%20Steel%20Coil%20Warehouse>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^p7]: S.-H. Cho, H.-J. Kim, L. Mönch, 2024 Winter Simulation Conference (WSC), 1773-1784 (2024). <https://doi.org/10.1109/wsc63780.2024.10838725> 초록 기준(OpenAlex 등록 초록). 서지: Crossref 등록 기록 <https://api.crossref.org/works?rows=3&query.bibliographic=Reinforcement%20Learning%20for%20Unrelated%20Parallel%20Machine%20Scheduling%20with%20Release%20Dates%2C%20Setup%20Times%2C%20and%20Machine%20Eligibility>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.
[^year]: OpenAlex의 「A unified learning framework for the block relocation problem: A new performance baseline」 등록 기록. DOI 10.1016/j.ejor.2026.09.016, 출판 연도 2026. <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.ejor.2026.09.016%7C10.1016/j.jmsy.2026.07.015%7C10.1080/00207543.2024.2439369%7C10.1080/00207543.2025.2516764%7C10.1109/icra57147.2024.10610858%7C10.1109/tase.2025.3632534%7C10.1109/wsc63780.2024.10838725%7C10.24963/ijcai.2026/685>, 관측 2026-10-31.

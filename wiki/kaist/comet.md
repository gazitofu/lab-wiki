# Computational Optimization Methods Lab (COMET)

**KAIST 산업및시스템공학과·조천식모빌리티대학원(겸임) · 권창현 부교수**

- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^home][^p2], 강화학습[^p4], 교통·도시 계획[^home][^mobility], 양자 컴퓨팅[^p7], 대형 언어 모델[^p7]
- 홈페이지: <https://comet.kaist.ac.kr/>

> 차량·드론의 배송 경로와 제조 작업 일정을 정하는 수학적 최적화 방법을 만들고, 기계학습과 탐색 알고리즘을 결합해 큰 문제를 푸는 계산 절차를 연구한다.[^home][^p6]

## 무엇을 연구하나

COMET은 권창현이 이끄는 계산 최적화 연구실이다. 수리 최적화(제약 조건 안에서 목적 함수를 최소화하거나 최대화하는 수학적 모형과 풀이)를 중심으로, 교통·물류·이동 서비스·제조·서비스 운영에서 생기는 대규모 문제를 다룬다. 연구실은 정확한 최적화 알고리즘(주어진 모형의 최적해를 보증하며 구하는 계산 절차), 휴리스틱(문제의 구조를 이용해 후보해를 찾는 절차), 기계학습(자료에서 규칙을 배우는 계산 방법), 양자 컴퓨팅(양자 중첩과 얽힘을 이용하는 계산)과 이들을 결합한 방법을 계산 도구로 삼는다.[^home]

첫 갈래는 차량 경로 문제(차량이 고객을 방문하는 순서와 경로를 정하는 문제)의 계산이다. 물류 거점에 고객을 배정하거나 거점 위치를 고른 뒤 배송 경로를 계산해야 하는 문제에서는, 상위 결정 하나를 평가할 때마다 경로 문제를 다시 풀어야 한다. GANCP(Genetic Algorithm with Neural Cost Predictor)는 신경망(자료를 바탕으로 연결의 가중치를 학습하는 계산 모형)으로 경로 비용을 예측하고, 그 예측을 유전 알고리즘(해의 선택·교차·변이를 반복하는 탐색 방법)에 넣는다. 그래프 신경망(점과 연결로 표현한 자료의 관계를 학습하는 신경망)을 이용해 비용을 예측하는 것이 핵심이다.[^p1]

둘째 갈래는 최적화 알고리즘의 일부를 학습으로 만드는 연구다. NeuralSep은 그래프를 축약하면서 차량 경로 문제의 유효 부등식(가능한 모든 해가 만족하는 부등식)을 찾는다. 이 부등식으로 해를 찾는 범위를 제한해 정확한 최적화 계산을 돕는다. PARCO(Parallel AutoRegressive Combinatorial Optimization)는 강화학습(행동 결과로 받는 보상을 바탕으로 행동 규칙을 배우는 학습 방법)을 써서 여러 행위자의 경로·일정 결정을 병렬로 생성한다. NGS(Neural Genetic Search)는 생성 모델(학습한 자료의 분포를 바탕으로 새 자료를 만드는 모형)이 부모 해를 조건으로 새 해를 만들게 해, 학습과 진화적 탐색을 결합한다.[^p2][^p4][^p5]

셋째 갈래는 서로 다른 운송 수단과 작업 사이의 조정이다. 트럭과 드론이 함께 배송하는 문제에서는 두 운송 수단의 방문 순서를 나누어 만들고, 동적 계획법(하위 문제의 결과를 연결해 전체 문제를 푸는 방법)과 국소 탐색(현재 해의 일부를 바꾸며 주변 해를 살피는 방법)을 결합한다. 제조에서는 병렬 기계에 작업을 배정할 때 작업 종류를 바꾸는 준비 비용과 납기 지연을 함께 고려한다. 최근에는 대형 언어 모델(많은 글을 학습해 글을 이해하고 생성하는 인공지능 모델)을 이용해 양자 회로 합성(원하는 계산을 수행하는 양자 연산의 배열을 만드는 과정)의 탐색 규칙을 설계하는 연구도 한다.[^p3][^p6][^p7]

## 주요 연구 주제

### 물류 거점과 트럭·드론의 경로

고객을 어느 거점에 배정할지와 차량이 어떤 순서로 방문할지를 함께 정하는 문제, 트럭과 드론이 협업하는 배송 문제를 다룬다. GANCP는 거점 결정에 필요한 경로 비용을 예측하고, 트럭·드론 연구는 두 운송 수단의 순서를 표현하는 방식과 탐색·평가 절차의 역할을 나눈다.[^p1][^p3]

### 학습으로 만드는 탐색과 최적화 도구

NeuralSep은 최적화 계산에 넣을 부등식을 찾는 방법을 학습한다. PARCO는 여러 행위자의 결정을 동시에 만들고 충돌을 조정하며, NGS는 학습한 생성 모델을 유전 탐색의 교차 연산에 넣는다. 이처럼 최적화 문제를 통째로 학습에 맡기는 방식뿐 아니라, 기존 계산 절차 안의 특정 역할을 학습으로 구성하는 연구를 한다.[^p2][^p4][^p5]

### 제조 작업의 묶음과 일정

에어컨 조립 공정의 작업 일정 문제에서 출발해 작업을 묶는 방법과 병렬 기계의 일정을 연구한다. 자기지도학습(자료 자체에서 학습 목표를 만들어 배우는 방법)으로 작업을 묶고, 납기 지연을 평가해 그 묶음을 반복해서 다듬는다.[^p6]

### 양자 회로 합성의 탐색 규칙

QuantumEvo는 양자 회로를 만드는 과정에서 변수의 순서를 정하는 규칙을 대형 언어 모델로 생성하고 탐색한다. 이진 결정 다이어그램(이진 변수에 따른 함수의 분기를 그래프로 나타낸 구조)의 크기만을 기준으로 삼지 않고, 그 구조에서 만들어진 회로의 양자 비용을 기준으로 규칙을 고른다.[^p7]

## 대표 논문

2024–2026년 논문 가운데 권창현이 저자로 참여하고, 경로 최적화·학습 기반 계산·제조 일정·양자 회로를 보여 주는 7편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 마지막 논문은 연구실 목록의 게재 승인 항목이다.[^pubs]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 권창현의 저자 위치 |
|---|---|---|---|---|
| 1 | 2025 | [Genetic Algorithms with Neural Cost Predictor for Solving Hierarchical Vehicle Routing Problems](https://doi.org/10.1287/trsc.2023.0369) · Transportation Science | 고객을 어느 거점에 배정할지, 거점을 어디에 둘지 결정할 때 후보마다 배송 경로를 다시 계산하는 부담을 다룬다. 미리 학습한 그래프 신경망으로 경로 비용을 예측하고 그 예측을 유전 알고리즘에 넣는 GANCP를 제안했다. 여러 거점을 쓰는 경로 문제와 거점 위치·경로를 함께 정하는 문제에서 표준 비교 문제로 성능을 평가했다.[^p1] | 전체 4명 중 마지막 |
| 2 | 2024 | [A Neural Separation Algorithm for the Rounded Capacity Inequalities](https://doi.org/10.1287/ijoc.2022.0310) · INFORMS Journal on Computing | 차량 경로의 최적해를 찾는 계산에 필요한 용량 부등식을 학습으로 찾았다. 작은 고객 집합으로 학습한 그래프 신경망과 그래프 축약을 결합해 큰 문제에 적용했다. 비교한 CVRPSEP은 고객이 300명 미만인 문제에서 강점을 보였고, 제안한 방법은 300명이 넘는 큰 문제에서 비용의 하한을 더 높게 잡았다.[^p2] | 전체 3명 중 마지막 |
| 3 | 2024 | [A Hybrid Genetic Algorithm with Type-Aware Chromosomes for Traveling Salesman Problems with Drone](https://doi.org/10.1016/j.ejor.2024.05.009) · European Journal of Operational Research | 트럭과 드론이 함께 배송할 때 두 운송 수단의 방문 순서를 따로 만들고, 고객이 어느 수단에 배정되는지를 표현하는 유전 알고리즘을 제안했다. 동적 계획법으로 해를 평가하고 국소 탐색으로 해를 다듬는다. 비교 문제 대부분에서 기존 알고리즘보다 해의 품질과 계산 시간에서 좋은 결과를 얻었다.[^p3] | 전체 2명 중 마지막 |
| 4 | 2025 | [PARCO: Learning parallel autoregressive policies for efficient multi-agent combinatorial optimization](https://arxiv.org/abs/2409.03811) · NeurIPS 2025 | 여러 행위자가 경로와 일정을 결정하는 문제에서 결정을 병렬로 생성하는 강화학습 방법을 제안했다. 여러 결정을 동시에 선택하는 장치, 우선순위에 따른 충돌 처리, 행위자 사이의 통신 층을 결합했다. 경로·일정 문제에서 기존 계산 방법 및 신경망 기반 방법과 해의 품질·계산 속도를 비교했다.[^p4] | 전체 9명 중 7번째 |
| 5 | 2025 | [Neural Genetic Search in Discrete Spaces](https://arxiv.org/abs/2502.10433) · ICML 2025 | 학습이 끝난 생성 모델이 답을 만드는 동안 유전 알고리즘의 탐색을 수행하는 NGS를 제안했다. 부모 해를 조건으로 새 해를 생성하는 연산을 교차로 사용한다. 경로 문제, 언어 모델을 대상으로 한 적대적 프롬프트 생성, 분자 설계에서 방법의 효과와 유연성을 평가했다.[^p5] | 전체 5명 중 마지막 |
| 6 | 2025 | [Self-Supervised Job Grouping for Parallel Machine Scheduling with Family Setups](https://doi.org/10.1016/j.ifacol.2025.09.172) · MIM 2025 | 에어컨 조립 공정에서 생기는 병렬 기계의 작업 일정 문제를 다룬다. 작업 종류를 바꿀 때 드는 준비 비용과 전체 납기 지연을 줄이기 위해, 자기지도학습으로 작업을 묶고 지연 평가로 묶음을 반복 개선했다. 실제 상황을 참고한 자료에서 비교 방법보다 납기 지연과 준비 비용을 줄였다.[^p6] | 전체 3명 중 2번째 |
| 7 | 2026 | [LLM-Driven Algorithm Design for Quantum Circuit Synthesis based on Binary Decision Diagrams](https://arxiv.org/abs/2609.05327) · Transactions on Machine Learning Research (게재 승인) | 양자 회로를 합성할 때 이진 결정 다이어그램의 변수 순서가 결과에 미치는 영향을 다룬다. 언어 모델이 순서를 직접 예측하게 하는 대신, 순서를 바꾸는 탐색 규칙을 생성하게 하는 QuantumEvo를 제안했다. 최종 회로의 양자 비용으로 후보 규칙을 골라, 여러 비교 문제에서 경쟁력 있는 결과를 보였다.[^p7] | 전체 5명 중 마지막 |

## 교수와 전문 분야

권창현은 COMET의 책임연구자다. 조천식모빌리티대학원의 소개는 산업및시스템공학과 부교수이자 조천식모빌리티대학원 겸임교수로 적는다. KAIST 기계공학 학사(2000), Pennsylvania State University 산업공학·경영과학 석사(2005), 산업공학 박사(2008)를 받았다. University at Buffalo와 University of South Florida에서 근무한 뒤 2023년 KAIST에 합류했다.[^people][^mobility]

교수의 연구 목표는 현재와 미래의 교통·물류 시스템 운영을 위한 계산 최적화 방법을 발전시키는 것이다. 현재 관심은 기계학습과 경영과학의 방법을 결합해 계산 효율을 높이는 데 있다. 대표 논문으로 보면 전문 분야는 차량 경로와 거점 결정의 통합 최적화, 학습을 이용한 최적화 계산, 트럭·드론 협업 경로, 제조 작업 일정이다.[^people][^mobility][^p1][^p2][^p3][^p6]

## 응용 분야와 공개 도구

연구실은 최종 배송 구간, 도시 물류, 차량 경로, 창고 운영, 공유 이동 서비스, 지속가능 교통, 도심 항공 이동 서비스 등을 응용 분야로 든다. 교통망의 균형과 게임, 위험물 운송의 위험 관리, 사람의 행동과 기반시설의 상호작용도 연구 대상으로 적는다.[^home]

공개 도구로 트럭·드론 순회 문제를 푸는 TSPDrone.jl, 불확실성을 고려한 최단 경로를 찾는 RobustShortestPath.jl, 교통 균형을 구하는 TrafficAssignment.jl 등이 있다. 경로를 세고 길이 분포를 추정하는 PathDistribution.jl, 변분 부등식 문제를 푸는 VariationalInequality.jl, 상보성 문제와 균형 제약 최적화를 표현하는 Complementarity.jl도 제공한다. TSP·차량 경로 계산 패키지를 연결하는 TSPSolvers.jl, Concorde.jl, LKH.jl, Hygese.jl, PyHygese, CVRPLIB.jl, CVRPSEP.jl도 소개한다.[^code]

## 구성원

2026년 10월 31일 People 페이지의 Current Members 중 책임연구자를 제외한 대학원생 13명, Visiting Students의 방문 학생 1명, Undergraduate Researchers의 학부 연구생 21개 게시 항목이다. 학부 연구생의 시기는 2023 Winter–2026 Summer이며, 현재 대학원생과 같은 이름의 과거 참여 항목도 원문 구획대로 함께 적었다. 과정·소속·합류 시기·연구 주제는 게시 표기다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Yoonju Sim (심윤주) | 박사과정 (ISE) | 2023 | large-scale optimization, vehicle routing problems, and LLMs | 7 |
| Jae Hyeok Lee (이재혁) | 박사과정 (ISE) | 2024 | neural combinatorial optimization, GPU computing and quantum computing |  |
| Jihye Na (나지혜) | 박사과정 (ISE) | 2024 | mathematical optimization, machine learning, and bilevel optimization |  |
| Sohyun Jeong (정소현) | 박사과정 (GSDS; 주지도 Hyun-Jung Kim, 공동지도 Changhyun Kwon) | 2024 (공동지도 시작) | combinatorial optimization, scheduling, and reinforcement learning | 6 |
| Taekang Hwang (황태강) | 박사과정 (ISE) | 2024 | mathematical optimization, integer programming and polyhedral combinatorics |  |
| Junhak Lee (이준학) | 석사과정 (GSDS) | 2025 | combinatorial optimization and graph neural network |  |
| Jaehwan Lee (이재환) | 박사과정 (GSDS) | 2025 | the integration of quantum computing and operations research |  |
| Suyeon Choi (최수연) | 박사과정 (ISE) | 2025 | mathematical optimization, machine learning and market design |  |
| Thi Thao Vy Bui (Bùi Thị Thảo Vy · 배초위) | 석사과정 (ISE) | 2025 | optimization, vehicle routing problems, and humanitarian logistics |  |
| Shiwon Park (박시원) | 석사과정 (AI4Math; 공동지도 Donghwan Kim) | 2026 | combinatorial optimization, reinforcement learning, and quantum computing |  |
| Sangil Han (한상일) | 박사과정 (ISE) | 2026 | combinatorial optimization and deep learning |  |
| Jimin Nam (남지민) | 석사과정 (ISE) | 2026 | combinatorial optimization, reinforcement learning, and AI agent |  |
| Irina Pavlova (Ирина Павлова · 이리나 파블로바) | 석사과정 (ISE) | 2026 | artificial intelligence, smart manufacturing, simulation-based optimization, and operations research |  |
| Viktorie Valdmanová | 방문 학생 (Czech Technical University in Prague) | 2026 Fall | decomposition methods, branch and price, machine learning |  |
| Taeyeong Yoo (유태영) | 학부 연구생 (KAIST ISE) | 2026 Summer | network design, Benders decomposition |  |
| Nurbolat Polatkhan (너르볼랏 폴라트한) | 학부 연구생 (KAIST ISE) | 2026 Summer | column generation, dual stabilization |  |
| Janghyeok Choi (최장혁) | 학부 연구생 (SNU IE) | 2026 Summer | nneural combinatorial optimization, decoder |  |
| Jungwon Ahn (안정원) | 학부 연구생 (KAIST ISE) | 2025 Winter | large-scale optimization, AI agent |  |
| Donghyun Im (임동현) | 학부 연구생 (SKKU IE) | 2025 Winter | primal-dual hybrid gradient, GPU computing |  |
| Agata Kazakevič (아가타 카자케비치) | 학부 연구생 (KAIST ISE) | 2025 Fall | cooperative game theory |  |
| Ji-Min Nam (남지민) | 학부 연구생 (KAIST EE) | 2025 Summer | column generation |  |
| Geonwoo Han (한건우) | 학부 연구생 (KAIST CS) | 2025 Summer | multi-armed bandit |  |
| Minwoo Kim (김민우) | 학부 연구생 (KAIST ISE) | 2025 Summer | neural combinatorial optimization |  |
| Yuil Kim (김유일) | 학부 연구생 (KAIST Math Sci) | 2025 Summer | valid inequalities |  |
| Malik Tolegen (말릭 톨레겐) | 학부 연구생 (KAIST ISE) | 2024 Winter | hybrid genetic algorithms, multiple traveling salesman problem |  |
| Hyungyoon Kim (김형윤) | 학부 연구생 (SNU Math) | 2024 Winter | Probabilistic Study of TSP |  |
| Gyutae Park (박규태) | 학부 연구생 (KAIST ISE) | 2024 Winter | decomposition-based optimization |  |
| JeongYeon Choi (최정연) | 학부 연구생 (KAIST ISE) | 2024 Summer | data science, market design |  |
| Sumin Kim (김수민) | 학부 연구생 (KAIST ISE) | 2024 Summer | reinforcement learning, hybrid genetic algorithms |  |
| Jaehwan Lee (이재환) | 학부 연구생 (Yonsei Applied Statistics) | 2024 Summer | reinforcement learning, pickup-and-delivery problems |  |
| Sangwoo Cho (조상우) | 학부 연구생 (KAIST ISE) | 2024 Summer | genetic algorithms, combinatorial optimization |  |
| Haewon Son (손해원) | 학부 연구생 (KAIST ISE) | 2024 Summer | pickup-and-delivery problems, local search algorithms |  |
| Junhak Lee (이준학) | 학부 연구생 (KAIST ISE) | 2024 Spring | traveling salesman problem, neural networks |  |
| ByeongJun An (안병준) | 학부 연구생 (KAIST ISE) | 2023 Winter | pickup-and-delivery problems, dynamic programming |  |
| Sangil Han (한상일) | 학부 연구생 (POSTECH IME) | 2023 Winter | cut separation problems, simulated annealing |  |

## 졸업생과 이전 구성원

People의 Past Members에 실린 KAIST 4개, University of South Florida 9개, University at Buffalo 15개, 총 28개 게시 항목이다. Zulqarnain Haider는 서로 다른 기관·학위로 두 번 올라 있다. 교수의 이전 소속 시기 구성원을 포함하며, 아래 표는 진로 대신 원문에 적힌 학위와 학위 논문을 담았다. Merve Doganbas의 학위·연도 칸은 게시 표기대로 비어 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 | 학위·활동 기관 |
|---|---|---|---|---|
| Merve Doganbas (메르베 도안바시) |  |  | Routing Problems at the Intersection of Classical Optimization and Learning-Based Methods (primary advisor Professor Hayong Shin ) | KAIST |
| Junpyo Lee (이준표) | M.S. (2025) |  | User Behavior-Driven Temporal Segmentation Optimization for Bike-Sharing Systems | KAIST |
| Doyoung Lee (이도영) | M.S. (2025) |  | Graph Transformer-based Neural Embedded Mixed-Integer Optimization for Solving Hierarchical Vehicle Routing Problems | KAIST |
| Hyeonah Kim (김현아) | Ph.D. (2025) |  | Algorithmic Priors for Neural Combinatorial Optimization (primary advisor Dr. Jinkyoo Park ) | KAIST |
| Abhay Sobhanan | Ph.D. (2025) |  | Pathways to Efficient and Equitable Solutions for Large-Scale Routing Problems (co-advisor Dr. Hadi Charkhgard ) | University of South Florida |
| Sasan Mahmoudinazlou | Ph.D. (2024) |  | Routing Problems Through the Lens of Hybrid Algorithms (co-advisor Dr. Hadi Charkhgard ) | University of South Florida |
| Xufei Liu | Ph.D. (2022) |  | Computational Methods for Solving the Combinatorial Optimization Problems in Transportation | University of South Florida |
| Aigerim Bogyrbayeva | Ph.D. (2021) |  | Optimization and Machine Learning Methods for Solving Combinatorial Problems in Urban Transportation | University of South Florida |
| Zulqarnain Haider | Ph.D. (2020) |  | Using Optimization Methods for Solving Problems in Sustainable Urban Mobility and Conservation Planning (co-advisor Dr. Hadi Charkhgard ) | University of South Florida |
| Mahdi Takalloo | Ph.D. (2020) |  | Game Theory Approaches for Transportation Problems | University of South Florida |
| Kevin Melendez | Ph.D. (2020) |  | On the Convergence of Transportation and Power Systems in Smart and Connected Communities (co-advisor Dr. Tapas Das ) | University of South Florida |
| Liu Su | Ph.D. (2019) |  | Routing and Designing Networks for Two Transportation Problems | University of South Florida |
| Aritra Pal | Ph.D. (2017) |  | Improving Service Level of Free-Floating Bike Sharing Systems | University of South Florida |
| Anpeng Zhang | Ph.D. (2018) |  | Understanding and Modeling New Transportation Markets with Emerging Vehicle Technologies (co-advisor Dr. Jee Eun Kang ) | University at Buffalo |
| Nan Ding | Ph.D. (2017) |  | Enabling Urban Parcel Pick-up and Delivery using All-Electric Trucks (co-advisor Dr. Rajan Batta ) | University at Buffalo |
| Longsheng Sun | Ph.D. (2016) |  | Designing Regulation Policies for Hazardous Materials Transportation (co-advisor Dr. Mark Karwan ) | University at Buffalo |
| Masoumeh Taslimi | Ph.D. (2015) |  | On the Analysis of Two Problems related to Risk Management in Urban Transportation Networks (co-advisor Dr. Rajan Batta ) | University at Buffalo |
| Tolou Esfandeh | Ph.D. (2015) |  | Regulating Hazardous Materials Transportation by Dual-Toll Pricing and Time-Dependent Network Design Policies (co-advisor Dr. Rajan Batta ) | University at Buffalo |
| Iakovos Toumazis | Ph.D. (2015) |  | Dynamic Chemotherapy Scheduling for Metastatic Colorectal Cancer Patients: Assessments and Improvements | University at Buffalo |
| Md. Tanveer Ahmed | Ph.D. (2013) |  | Revenue Management for Online Advertisement Services | University at Buffalo |
| Paul Berglund | Ph.D. (2012) |  | Three Problems in Discrete Network Facility Location | University at Buffalo |
| Yingying Kang | Ph.D. (2011) |  | Value-at-Risk Models for Hazardous Materials Transportation (co-advisor Dr. Rajan Batta ) | University at Buffalo |
| Ali Sattarzadeh | M.S. (2015) |  | Hazmat Network Design Considering Risk and Cost Equity | University at Buffalo |
| Zulqarnain Haider | M.S. (2014) |  | Inventory Rebalancing through Pricing in Public Bike Sharing Systems | University at Buffalo |
| Chelsea Greene | M.S. (2013) |  | OR/MS Approaches to Problems involving Hazardous Materials Risk and Impacts from a Natural Disaster (co-advisor Dr. Rajan Batta ) | University at Buffalo |
| Anand Srinivasan | M.S. (2010) |  | Operations of Online Advertising Services and Publisher’s Options | University at Buffalo |
| Amod Anand Agashe | M.S. (2010) |  | Stochastic Revenue Optimization in Online Advertising | University at Buffalo |
| Varun Narayana Kutty | M.S. (2010) |  | Accept-Reject Decision in Online Advertising using Geometric Brownian Motion | University at Buffalo |

## 최근 논문 목록 (2021–2026)

교수 개인의 전체 연구 목록에 실린 2021–2026년 학술지 논문 15편, 학회 논문 9편, 책 장 1편과 심사 중 원고 9편이다. 2023년 KAIST 합류 전 논문도 포함한다. 제목·저자·발표처는 연구실 게시 표기이며, 연도는 목록의 연도 분류다. 게재 승인 항목은 그 상태를 표시했고, 심사 중 원고의 연도는 연결된 arXiv 식별자의 연도이며 연도가 없는 2편은 별도로 표시했다. 「A Reinforcement Learning Approach for Rebalancing Electric Vehicle Sharing Systems」는 목록에서 2022년으로 분류했지만 서지 줄은 2020으로 적고 있다.[^pubs][^mobility]

**2026**

- Jaehwan Lee, Changhyun Kwon. "Quantum End-to-End Learning for Contextual Combinatorial Optimization". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2605.20222)
- Jae Hyeok Lee, Taekang Hwang, Changhyun Kwon. "Asymptotic Bounds for the Traveling Salesman Problem with Drone". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2603.00328)
- Sasan Mahmoudinazlou, Changhyun Kwon, Hadi Charkhgard. "Solving Various Classes of Arc Routing Problems with a Memetic Algorithm-based Framework". *Journal of the Operational Research Society , 게재 승인*. [논문 링크](https://optimization-online.org/2023/11/a-generic-hybrid-genetic-algorithm-based-framework-for-solving-various-classes-of-arc-routing-problems/)
- Yoonju Sim, Federico Berto, Chuanbo Hua, Jinkyoo Park, Changhyun Kwon. "LLM-Driven Algorithm Design for Quantum Circuit Synthesis based on Binary Decision Diagrams". *Transactions on Machine Learning Research , 게재 승인*. [arXiv](https://arxiv.org/abs/2609.05327)
- Youngjun Park, Jihye Na, Keonhee Jang, Dongman Lee, Changhyun Kwon, Yoonjin Yoon. "Food Deserts in Context: How Site-Specific Factors Reshape Food Deserts Discussion". *npj Urban Sustainability , 게재 승인*. [DOI](https://doi.org/10.1038/s42949-026-00458-2) · [연구실 PDF](http://comet.kaist.ac.kr/papers/park_food.pdf)
- Jiwoo Son, Zhikai Zhao, Federico Berto, Chuanbo Hua, Zhiguang Cao, Changhyun Kwon, Jinkyoo Park. "RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization". *The Fourteenth International Conference on Learning Representations, ICLR 2026*. [논문 링크](https://openreview.net/forum?id=sKvo9ZZfpe)
- Chuanbo Hua, Federico Berto, Zhikai Zhao, Jiwoo Son, Changhyun Kwon, Jinkyoo Park. "USPR: Learning a Unified Solver for Profiled Routing". *Proceedings of the AAAI Conference on Artificial Intelligence, 40, AAAI 2026*. [arXiv](https://arxiv.org/abs/2505.05119)

**2025**

- Yoonju Sim, Hyeonah Kim, Changhyun Kwon. "Test-Time Search in Neural Graph Coarsening Procedures for the Capacitated Vehicle Routing Problem". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2510.00958) · [코드](https://github.com/syj5268/neuralsep-tts)
- Suyeon Choi, Changhyun Kwon, Seungki Min. "Dynamic Pricing of an Expiring Item under Strategic Buyers with Stochastic Arrival". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2509.24720)
- Abhay Sobhanan, Changhyun Kwon, Hadi Charkhgard. "Arc Routing Problems with Multiple Trucks and Drones: A Hybrid Genetic Algorithm". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2508.18105)
- Jae Hyeok Lee, Minwoo Kim, Minjun Kim, Jinkyoo Park, Changhyun Kwon. "The Iterative Chainlet Partitioning Algorithm for the Traveling Salesman Problem with Drone and Neural Acceleration". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2504.15147) · [코드](https://github.com/kaist-comet/TSPDroneICP.jl)
- Xufei Liu, Sung Hoon Chung, Changhyun Kwon. "An Adaptive Large Neighborhood Search Method for the Drone-Truck Arc Routing Problem". *Computers & Operations Research , 176, 106959*. [DOI](https://doi.org/10.1016/j.cor.2024.106959) · [연구실 PDF](http://comet.kaist.ac.kr/papers/liu_adaptive.pdf)
- Abhay Sobhanan, Junyoung Park, Jinkyoo Park, Changhyun Kwon. "Genetic Algorithms with Neural Cost Predictor for Solving Hierarchical Vehicle Routing Problems". *Transportation Science , 59(2), 207–450*. [DOI](https://doi.org/10.1287/trsc.2023.0369) · [arXiv](https://arxiv.org/abs/2310.14157) · [코드](https://github.com/abhaysobhanan/GANCP)
- Sohyun Jeong, Changhyun Kwon, Hyun-Jung Kim. "Self-Supervised Job Grouping for Parallel Machine Scheduling with Family Setups". *Proceedings of the 11th IFAC Conference on Manufacturing Modelling, Management and Control MIM 2025*. [DOI](https://doi.org/10.1016/j.ifacol.2025.09.172)
- Federico Berto, Chuanbo Hua, Laurin Luttmann, Jiwoo Son, Junyoung Park, Kyuree Ahn, Changhyun Kwon, Lin Xie, Jinkyoo Park. "PARCO: Learning parallel autoregressive policies for efficient multi-agent combinatorial optimization". *Advances in Neural Information Processing Systems 39: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025*. [arXiv](https://arxiv.org/abs/2409.03811) · [코드](https://github.com/ai4co/parco)
- Federico Berto, Chuanbo Hua, Junyoung Park, Laurin Luttmann, Yining Ma, Fanchen Bu, Jiarui Wang, Haoran Ye, Minsu Kim, Sanghyeok Choi, Nayeli Gast Zepeda, Andre Hottung, Jianan Zhou, Jieyi Bi, Yu Hu, Fei Liu, Hyeonah Kim, Jiwoo Son, Haeyeon Kim, Davide Angioni, Wouter Kool, Zhiguang Cao, Qingfu Zhang, Joungho Kim, Jie Zhang, Kijung Shin, Cathy Wu, Sungsoo Ahn, Guojie Song, Changhyun Kwon, Kevin Tierney, Lin Xie, Jinkyoo Park. "RL4CO: an Extensive Reinforcement Learning for Combinatorial Optimization Benchmark". *KDD ’25: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining , V.2, 5278–5289*. [DOI](https://doi.org/10.1145/3711896.3737433) · [arXiv](https://arxiv.org/abs/2306.17100) · [코드](https://github.com/ai4co/rl4co)
- Hyeonah Kim, Sanghyeok Choi, Jiwoo Son, Jinkyoo Park, Changhyun Kwon. "Neural Genetic Search in Discrete Spaces". *ICML ’25: Proceedings of the 42nd International Conference on Machine Learning , in Proceedings of Machine Learning Research, 267:29969–29987*. [arXiv](https://arxiv.org/abs/2502.10433) · [논문 링크](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25b/kim25b.pdf) · [코드](https://github.com/hyeonahkimm/ngs)
- Chuanbo Hua, Federico Berto, Jiwoo Son, Seunghyun Kang, Changhyun Kwon, Jinkyoo Park. "CAMP: Collaborative Attention Model with Profiles for Vehicle Routing Problems". *AAMAS ’25: Proceedings of the 2025 International Conference on Autonomous Agents and Multiagent Systems, 1015–1024*. [arXiv](https://arxiv.org/abs/2501.02977) · [코드](https://github.com/ai4co/camp)

**2024**

- Waquar Kaleem, Doyoung Lee, Changhyun Kwon, Anirudh Subramanyam. "Neural Embedded Mixed-Integer Optimization for Location-Routing Problems". *arXiv 사전 공개본 (심사 중)*. [arXiv](https://arxiv.org/abs/2412.05665)
- Sasan Mahmoudinazlou, Changhyun Kwon. "A Hybrid Genetic Algorithm with Type-Aware Chromosomes for Traveling Salesman Problems with Drone". *European Journal of Operational Research , 318(3), pp. 719–739*. [DOI](https://doi.org/10.1016/j.ejor.2024.05.009) · [arXiv](https://arxiv.org/abs/2303.00614) · [코드](https://github.com/Sasanm88/TSPDroneHGATAC.jl)
- Hyeonah Kim, Jinkyoo Park, Changhyun Kwon. "A Neural Separation Algorithm for the Rounded Capacity Inequalities". *INFORMS Journal on Computing , 36(4), pp. 987–1005*. [DOI](https://doi.org/10.1287/ijoc.2022.0310) · [arXiv](https://arxiv.org/abs/2306.17283) · [코드](https://github.com/hyeonahkimm/neuralsep)
- Sasan Mahmoudinazlou, Changhyun Kwon. "A Hybrid Genetic Algorithm for the min-max Multiple Traveling Salesman Problem". *Computers & Operations Research , 162, 106455*. [DOI](https://doi.org/10.1016/j.cor.2023.106455) · [arXiv](https://arxiv.org/abs/2307.07120) · [코드](https://github.com/Sasanm88/m-TSP)
- Sobhanan, A., S. Mahmoudinazlou, H. Charkhgard, C. Kwon. "A branch-and-price algorithm for emergency humanitarian logistics with a mixed truck-drone fleet". *Proceedings of the IISE Annual Conference & Expo 2024 , 6pages*. [연구실 PDF](http://comet.kaist.ac.kr/papers/sobhanan_branch.pdf)

**2023**

- Xufei Liu, Sang Won Kim, Changhyun Kwon. "An Adaptive Large Neighborhood Search Method for Rebalancing Free-Floating Electric Vehicle Sharing Systems". *Computers & Operations Research , 155, 106220*. [DOI](https://doi.org/10.1016/j.cor.2023.106220) · [연구실 PDF](http://comet.kaist.ac.kr/papers/liu_adaptive_ev.pdf)
- Aigerim Bogyrbayeva, Taehyun Yoon, Hanbum Ko, Sungbin Lim, Hyokun Yun, Changhyun Kwon. "A Deep Reinforcement Learning Approach for Solving the Traveling Salesman Problem with Drone". *Transportation Research Part C: Emerging Technologies , 148, 103981*. [DOI](https://doi.org/10.1016/j.trc.2022.103981) · [arXiv](https://arxiv.org/abs/2112.12545) · [코드](https://github.com/chkwon/TSPDrone.jl)
- Junyoung Park, Changhyun Kwon, Jinkyoo Park. "Learn to solve the min-max multiple traveling salesmen problem with reinforcement learning". *Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023) , 878-886, 9 pages*. [논문 링크](https://dl.acm.org/doi/10.5555/3545946.3598725) · [연구실 PDF](http://comet.kaist.ac.kr/papers/park_learn.pdf)

**2022**

- Zulqarnain Haider, Yujie Hu, Hadi Charkhgard, David Himmelgreen, Changhyun Kwon. "Creating Grocery Delivery Hubs for Food Deserts at Local Convenience Stores via Spatial and Temporal Consolidation". *Socio-Economic Planning Sciences , 82(B), 101301*. [DOI](https://doi.org/10.1016/j.seps.2022.101301) · [연구실 PDF](http://comet.kaist.ac.kr/papers/haider_creating.pdf)
- Aigerim Bogyrbayeva, Sungwook Jang, Ankit Shah, Young Jae Jang, Changhyun Kwon. "A Reinforcement Learning Approach for Rebalancing Electric Vehicle Sharing Systems". *IEEE Transactions on Intelligent Transportation Systems , 23(7), 8704–8714*. [DOI](https://doi.org/10.1109/TITS.2021.3085217) · [arXiv](https://arxiv.org/abs/2010.02369) · [연구실 PDF](http://comet.kaist.ac.kr/papers/bogyrbayeva_RL.pdf) · [코드](https://github.com/aigerimb/FFEVSS)
- Chung, S. H. and C. Kwon. "Drone-Truck Routing Problems". *, in Encyclopedia of Optimization (Eds.:P. Pardalos and O. Prokopyev), Springer*. [연구실 PDF](http://comet.kaist.ac.kr/papers/chung_drone.pdf)

**2021**

- Aigerim Bogyrbayeva, Changhyun Kwon. "Pessimistic Evasive Flow Capturing Problems". *European Journal of Operational Research , 293(1), 133-148*. [DOI](https://doi.org/10.1016/j.ejor.2020.12.001) · [연구실 PDF](http://comet.kaist.ac.kr/papers/bogyrbayeva_pessimistic.pdf)
- Aigerim Bogyrbayeva, Mahdi Takalloo, Hadi Charkhgard, Changhyun Kwon. "An Iterative Combinatorial Auction Design for Fractional Ownership of Autonomous Vehicles". *International Transactions in Operational Research , 28(4), 1681–1705*. [DOI](https://doi.org/10.1111/itor.12903) · [연구실 PDF](http://comet.kaist.ac.kr/papers/bogyrbayeva_iterative.pdf)
- Mahdi Takalloo, Aigerim Bogyrbayeva, Hadi Charkhgard, Changhyun Kwon. "Solving the Winner Determination Problem in Combinatorial Auctions for Fractional Ownership of Autonomous Vehicles". *International Transactions in Operational Research , 28(4), 1658–1680. Fractional Ownership; Combinatorial Auction; Bidder-Defined Items; Clique*. [DOI](https://doi.org/10.1111/itor.12868) · [연구실 PDF](http://comet.kaist.ac.kr/papers/takalloo_solving.pdf)

**연도 표기 없음**

- Thi Thao Vy Bui, Yantong Dou, Changhyun Kwon, Yoonjin Yoon, Yu Zhang. "Repurposing Existing Helipads for Scheduled Urban Air Mobility: An Optimization Framework for Vertipad Selection and Timetable Design". *심사 중 (연도 표기 없음)*.
- Merve Doganbas, Junhak Lee, Hayong Shin, Changhyun Kwon. "A Learning-Based Separation Algorithm for the Strengthened Comb Inequalities". *심사 중 (연도 표기 없음)*.

## 연구 과제

Projects의 과제 중 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 국내 지원 13건과 미국 지원 4건이다. 교수의 2023년 KAIST 합류 전 과제와 KAIST 안식년 중 참여한 과제도 포함한다. 제목·지원기관·기간·책임 역할은 게시 표기다. 종료일이 비어 있는 GS-KAIST 과제는 원문 표기대로 두었다.[^projects][^mobility]

- (Co-PI) “AI-Based Dark Factory Design and Integration Solution (AI 기반 다크팩토리 설계-구축 솔루션 개발),” National IT Industry Promotion Agency (정보통신산업진흥원), 2026.08.01–2030.12.31
- (PI) “Heterogeneous Collaborative Agent Routing: Theory, Algorithms, and Application to Logistics (이기종 협업 에이전트 경로 최적화: 이론, 알고리즘 및 물류 시스템 응용),” National Research Foundation of Korea (NRF, 한국연구재단), 2026.03.01–2029.02.28
- (PI) “AI-Based Solution Methods for Stochastic Location-Routing Problems (불확실성을 고려한 입지-경로 통합 최적화 연구: 인공지능 기반 해법 개발),” Jungseok Logistics Foundation (정석물류학술재단), 2026.01.01–2026.12.31
- (PI) “Pallet Loading Optimization System (팔레트 로딩 최적화 시스템 개발),” Foundation of Korea Logistics Industry Promotion (물류산업진흥재단), 2025.08.01–2025.12.31
- (PI) “Enhancing SCM Planning Processes through Integrated Optimization Methodologies (최적화 방법론 융합 연구를 통한 SCM 계획 수립 프로세스 효율화),” Samsung Electronics, 2024.10.15–2025.10.14
- (Co-PI) “Core AI Technologies for Future Cities: GS-KAIST Joint R&D Project (GS-KAIST 미래 도시 인공지능 핵심 기술 연구개발),” GS Engineering & Construction, 2024.08.12–
- (PI) “Integrating machine learning prediction and optimization for routing wildfire detection drones (머신러닝 예측과 최적화의 융합을 통한 산불 탐색 드론의 경로 결정),” National Research Foundation (NRF) of Korea, 2024.09.01–2025.08.31
- (Co-PI) “Deep Learning Foundation Model for Combinatorial Optimization and Its Applications to Various Industrial Problems (조합 최적화 문제 해결을 위한 인공지능 기초모델 개발과 이를 활용한 다양한 산업문제 해결),” National Research Foundation (NRF) of Korea, 2024.08.01–2027.04.30
- (PI) “KAIST반도체연구지원금 2기,” 삼성전자, 2024.03.01–2027.02.28
- (PI) “항공 모빌리티 운임 계획 및 재무적영향 분석,” 라니아키아, 2024.03.04–2024.06.04
- (Co-PI) “GS-버티포트 운용개념 수립,” GS건설, 2024.06.01–2024.12.31
- (PI) “AI-based Next-Generation Optimization Algorithms for Smart Logistics (스마트 물류를 위한 인공지능 기반 차세대 최적화 알고리즘),” National Research Foundation (NRF) of Korea, 2023.10.01–2026.12.31
- (co-PI) “Hybrid Neural Combinatorial Optimization Methods for Smart Factory Material Handling (스마트 공장 물류 자동화를 위한 인공신경망 기반 하이브리드 조합적 최적화 기술 개발 ),” National Research Foundation (NRF) of Korea, PI: Young Jae Jang (KAIST), 2021.07.01–2022.06.30 (This project supports my research during sabbatical at KAIST.)
- (co-PI) “POSE: Phase II: CONNECT: Consortium of Open-source plaNNing models for Next-generation Equitable and efficient Communities and Transportation,” National Science Foundation (NSF), , 08/15/2023–07/31/2025, [TI-2303748]
- (PI) “Collaborative Research: Arc Routing Problems in Combined Drone/Truck Fleets,” National Science Foundation (NSF), 7/1/2021–6/30/2024, [CMMI-2032458]
- (PI) “The 17th INFORMS Computing Society Conference 2022,” USF Research & Innovation Conference Support Grant, , co-PI: Hadi Charkhgard (USF), Tapas Das (USF), 1/23/2022–1/25/2022
- (PI) “Market Design Approaches for Fashion Goods Distribution,” 2019 USF Nexus Initiative Awards: Faculty Global/National Collaborations, 5/28/2019–12/31/2021

## 수상·선정

논문 목록에 기재된 최근 선정 항목이다.[^pubs]

- 2024 · Abhay Sobhanan, Sasan Mahmoudinazlou, Hadi Charkhgard, Changhyun Kwon의 「A branch-and-price algorithm for emergency humanitarian logistics with a mixed truck-drone fleet」: IISE OR Track Best Paper Award 최종 후보

## 연락과 위치

- 교수 연구실: 대전광역시 유성구 대학로 291 KAIST E2-1 산업경영학동 4210호, 우편번호 34141[^home]
- 전화: +82-42-350-3138[^home]
- 이메일: chkwon@kaist.ac.kr[^gsds][^mobility]

## 각주
[^home]: COMET, Home. 교통·물류·모빌리티·제조·서비스 운영의 대규모 최적화 문제를 위한 계산 방법을 개발한다고 적으며, 정확한 알고리즘·휴리스틱·기계학습·양자 컴퓨팅을 방법으로 든다. <https://comet.kaist.ac.kr/> 관측 2026-10-30.
[^people]: COMET, People. 교수 소개와 Current Members·Visiting Students·Undergraduate Researchers·Past Members. <https://comet.kaist.ac.kr/people/> 관측 2026-10-31.
[^pubs]: COMET, Publications. 학술지·학회·심사 중 원고·책 장·책 목록과 게시 초록. <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^projects]: COMET, Projects. Funded in Korea·Funded in the U.S.의 연구비 지원 과제 목록. <https://comet.kaist.ac.kr/projects/> 관측 2026-10-31.
[^code]: COMET, Code. Julia 패키지와 경로 최적화 관련 공개 도구. <https://comet.kaist.ac.kr/code/> 관측 2026-10-31.
[^gsds]: KAIST 데이터사이언스대학원, People의 권창현 항목. <https://gsds.kaist.ac.kr/people> 관측 2026-10-30.
[^mobility]: KAIST 조천식모빌리티대학원, 권창현 소개. 산업및시스템공학과 Associate Professor·모빌리티대학원 겸임, 2023년 합류, 교통·물류 운영을 위한 계산 최적화 연구를 적는다. <https://mo.kaist.ac.kr/professor/%EA%B6%8C%EC%B0%BD%ED%98%84/> 관측 2026-10-31.
[^p1]: A. Sobhanan, J. Park, J. Park, C. Kwon, Transportation Science 59, 207–450 (2025). <https://doi.org/10.1287/trsc.2023.0369> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p2]: H. Kim, J. Park, C. Kwon, INFORMS Journal on Computing 36, 987–1005 (2024). <https://doi.org/10.1287/ijoc.2022.0310> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p3]: S. Mahmoudinazlou, C. Kwon, European Journal of Operational Research 318, 719–739 (2024). <https://doi.org/10.1016/j.ejor.2024.05.009> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p4]: F. Berto 외, J. Park, Advances in Neural Information Processing Systems 39 (2025). <https://arxiv.org/abs/2409.03811> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p5]: H. Kim 외, C. Kwon, Proceedings of Machine Learning Research 267, 29969–29987 (2025). <https://arxiv.org/abs/2502.10433> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p6]: S. Jeong, C. Kwon, H.-J. Kim, Proceedings of the 11th IFAC Conference on Manufacturing Modelling, Management and Control MIM 2025 (2025). <https://doi.org/10.1016/j.ifacol.2025.09.172> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.
[^p7]: Y. Sim 외, C. Kwon, Transactions on Machine Learning Research (게재 승인) (2026). <https://arxiv.org/abs/2609.05327> 초록 기준(논문 페이지 게시 초록). COMET Publications에 게시된 초록. 초록 원문 <https://comet.kaist.ac.kr/publications/> 관측 2026-10-31.

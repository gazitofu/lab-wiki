# Complex System Design Laboratory (CSD Lab.)

**KAIST 산업및시스템공학과 · 이태식 교수**

- 분야: 복잡한 서비스 시스템의 설계·운영, 불확실성 아래 의사결정, 의료서비스 시스템, 다중 행위자 학습
- 대분야: 산업·시스템, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^p1][^p2][^p5], 다중 에이전트 시스템·분산 의사결정[^p1][^p2], 강화학습[^p1][^p2]
- 홈페이지: <https://csdlab.kaist.ac.kr/>
- 교수: 이태식(Taesik Lee)[^gsds][^prof]

> 환자·병원·운전자처럼 각자 판단하는 주체들의 행동을 수학적 모형과 모의실험으로 연결하고, 전체 서비스 시스템의 구성과 운영 방침을 설계하는 연구실이다.

## 무엇을 연구하나

이 연구실은 한 부분의 성능뿐 아니라 여러 부분이 연결된 시스템 전체의 작동을 연구한다. 수요와 사람의 선택을 미리 확정하기 어려운 상황에서 자원을 어디에 두고 어떤 운영 방침을 적용할지 묻는다. 이를 위해 수학적 모델링(대상의 관계와 작동을 수식으로 나타내는 일)과 수치 시뮬레이션(모형의 작동을 컴퓨터 계산으로 재현하는 방법)을 함께 쓰며, 의료서비스와 물류를 주요 대상으로 삼는다.[^home]

의료서비스 연구에서는 환자가 병원을 선택하는 방식과 병원의 경쟁·보상 구조를 함께 다룬다. 연구 소개는 이산 선택 모형(여러 대안 가운데 하나를 고르는 결정을 수학적으로 나타내는 모형)의 구조와 추정 알고리즘(관측 자료에서 모형의 값을 계산하는 절차)을 개발한다고 적는다. 사람마다 효용을 평가하는 방식이 다르다는 점을 잠재 집단(직접 관측되지 않지만 선택 특성으로 구분하는 집단)으로 표현하고, 환자 선택 자료로 병원의 계층 구조도 찾으려 한다. 의료비 지불 체계 연구는 병원 경쟁과 진료량·질의 관계를 수리 모형으로 표현해 정책의 영향을 분석하는 것이 목표다.[^projects]

또 다른 축은 다중 에이전트 시스템(여러 행위자가 각자의 정보와 판단을 바탕으로 서로 영향을 주고받는 체계)의 구성과 의사결정을 설계하는 일이다. 강화학습(행동의 결과로 받는 보상을 이용해 행동 방침을 배우는 방법)을 이용해 행위자들이 어떤 행동을 할지 학습한다. 일부 행위자만 설계자가 제어할 수 있는 상황에서는 제어할 행위자의 수와 행동 방침을 함께 정한다. 하이퍼네트워크(다른 신경망의 가중치를 생성하는 신경망)를 이용한 연구는 여러 구성의 행동 방침을 하나의 학습 구조에서 만들어 계산 부담을 줄이는 방법을 제안했다.[^p1] 계약 설계 연구는 보상과 참여자 모집을 함께 정하는 최적화(조건을 지키면서 정한 목표 값을 가장 크게 또는 작게 만드는 해를 찾는 방법)를 다룬다.[^p2]

감염병 대응에서도 정책과 사람의 판단을 연결한다. 사회적 거리두기를 따를지에 관한 개인 선택을 게임 이론(서로의 선택이 결과에 영향을 주는 상황에서 각 주체의 의사결정을 분석하는 이론)으로 나타내고, 그 선택이 정책 효과에 미치는 영향을 모의실험한다.[^p4] 집단별 격리 정책 연구는 감염자 수와 격리 일수라는 서로 다른 목표를 함께 다루며, 집단마다 접촉 추적 범위와 격리 기간을 정하는 방법을 제시했다.[^p5]

의료 시스템 공학의 연구 동향을 정리하는 분석 절차도 개발했다. ChatGPT를 이용한 연구는 학회 발표의 초록을 주제별로 나누고 연도별 흐름과 세부 주제를 분석하는 절차를 제안했다. 질문·지시를 전달하는 프롬프트와 ChatGPT API(Application Programming Interface, 프로그램 사이에서 기능과 자료를 주고받도록 정한 접점)를 단계별로 구성해 문헌 검토의 부담을 줄일 가능성을 살폈다.[^p6]

## 주요 연구 주제

### 일부 행위자만 제어하는 시스템과 계약 설계

전체 행위자를 직접 제어할 수 없을 때 제어 가능한 행위자를 얼마나 둘지, 이들이 어떤 행동을 하게 할지 함께 설계한다. 뉴욕시 택시 자료를 이용한 연구는 제어 가능한 행위자와 자율적으로 행동하는 행위자 양쪽의 행동 방침을 만들어 시스템 구성을 비교했다.[^p1] 계약 설계에서는 베이즈 최적화(확률모형으로 평가 결과를 갱신하며 다음 평가 대상을 고르는 최적화 방법)와 다중 에이전트 강화학습을 결합해, 제약을 만족하는 보상·모집 결정을 찾는 방법을 제안했다.[^p2]

### 환자의 병원 선택과 의료서비스 제공 체계

병원의 위치만이 아니라 환자가 그 병원을 선택하는 이유와 의료기관 사이의 관계를 다룬다. 연구 소개는 병원 선택 모형의 구조와 추정 방법, 의료비 지불 체계의 수리 모형, 의료서비스 권역을 나누는 수정된 방법, 환자 공동 이용 관계로 병원망을 분석하는 절차를 제시한다. 병원 선택과 서비스 공급을 함께 다루어 의료체계를 설계·분석하려는 연구다.[^projects]

### 개인의 정책 순응과 집단별 격리

거리두기 정책을 강화하더라도 사람들이 따르지 않으면 효과가 달라질 수 있다. 사전 공개본은 개인의 이익을 고려한 선택을 모형에 넣어 정책 효과와 사회적 비용을 함께 살폈다.[^p4] 집단별 격리 연구에서는 행위자 기반 시뮬레이션(개별 행위자의 행동과 상호작용으로 전체 변화를 계산하는 방법)과 진화 알고리즘(후보 해의 선택과 변형을 반복해 해를 탐색하는 방법)을 결합했다. 이를 통해 한 목표를 개선하면 다른 목표가 악화되는 대안들의 경계를 찾아 집단별 정책을 비교했다.[^p5]

### 여러 로봇의 구성과 연구 초록 분석

로봇 집단의 구성이 달라지면 학습한 행동과 탐사 성능도 달라진다. BOFD(Bayesian Optimization for Fleet Design, 로봇 집단 설계를 위한 베이즈 최적화) 연구는 성능과 비용을 함께 고려하면서 모든 구성을 일일이 평가하지 않고 유망한 구성을 탐색하는 방법을 제안했다. 검증은 합성 문제와 시뮬레이션 환경에서 수행했다.[^p3] 의료 시스템 공학의 문헌 분석에서는 학회 초록을 분석하는 절차를 구성해 ChatGPT를 활용한 연구 검토의 가능성을 살폈다.[^p6]

## 대표 논문

이태식 교수가 KAIST에 재직한 시기의 연구에서 시스템 구성·계약·로봇 집단·감염병 정책·연구 동향 분석을 보여 주는 6편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 사전 공개본은 arXiv 판으로 표시했다. 5번은 arXiv가 학회 논문집을 IISE Annual Conference and Expo 2022로 명시한 항목이다.[^prof][^p5]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2025 | [Hypernetwork-based approach for optimal composition design in partially controlled multi-agent systems](https://doi.org/10.48550/arXiv.2502.12605) · arXiv 사전 공개본 | 일부 행위자는 설계자가 제어하고 나머지는 스스로 행동하는 시스템에서, 제어할 행위자의 수와 각자의 행동 방침을 함께 정하는 문제를 다뤘다. 구성마다 별도 모형을 학습하는 대신 하이퍼네트워크로 양쪽 행위자의 행동 방침을 생성하는 방법을 제안했다. 뉴욕시 택시 자료를 이용한 실험에서 기존 방법과 비교해 균형 행동 방침의 근사와 주문 응답·수요 처리 지표가 개선되었다고 보고했다.[^p1] | 마지막 저자 |
| 2 | 2024 | [Algorithmic Contract Design with Reinforcement Learning Agents](https://doi.org/10.48550/arXiv.2408.09686) · arXiv 사전 공개본 | 동적으로 변하고 확률적 결과가 생기는 환경에서 강화학습 행위자들과 맺을 계약을 설계하는 문제를 제시했다. 보상과 참여자 모집에 관한 제약을 다루기 위해 cPMES(Constrained Pareto Maximum Entropy Search)라는 다목적 베이즈 최적화 방법을 제안했다. 합성 문제와 시뮬레이션에서 제약을 만족하며 계약 설계자의 목표를 키우는 계약을 찾는 능력을 보였다.[^p2] | 5명 중 4번째 |
| 3 | 2024 | [Bayesian Optimization Framework for Efficient Fleet Design in Autonomous Multi-Robot Exploration](https://doi.org/10.48550/arXiv.2408.11751) · arXiv 사전 공개본 | 서로 다른 로봇으로 이루어진 탐사 집단의 성능과 비용을 함께 고려하는 구성 설계 문제를 다뤘다. 구성마다 강화학습을 다시 수행하는 비용을 줄이기 위해 BOFD를 제안했다. 설계 공간의 불확실성을 반영해 성능과 비용의 대안을 탐색하며, 합성 문제와 시뮬레이션 실험에서 집단 평가 횟수를 줄이면서 효율적인 구성을 찾았다고 보고했다.[^p3] | 8명 중 6번째 |
| 4 | 2024 | [Effectiveness of Social Distancing under Partial Compliance of Individuals](https://doi.org/10.48550/arXiv.2408.14226) · arXiv 사전 공개본 | 지역사회 구성원이 자신의 이익을 고려해 거리두기 정책을 따를지 정하는 상황을 모형화했다. 수치 실험은 지나치게 엄격한 정책이 불순응과 효과 감소로 이어질 수 있고, 방역 효과와 사회적 비용을 함께 고려해야 함을 시사했다. 재감염 위험이 낮은 질병에서는 면역이 있는 사람을 면제하는 구분 정책이 감염과 사회경제적 비용을 줄일 수 있다고 제안했다.[^p4] | 마지막 저자 |
| 5 | 2022 | [Segmentized quarantine policy for managing a tradeoff between containment of infectious disease and social cost of quarantine](https://doi.org/10.48550/arXiv.2411.08059) · IISE Annual Conference and Expo 2022, 초록은 arXiv 판 | 집단별로 접촉 추적 범위와 격리 기간을 달리 정하는 정책을 연구했다. 감염자 수와 격리 일수를 함께 줄이는 대안을 찾기 위해 행위자 기반 감염병 시뮬레이션과 진화 알고리즘을 결합했다. 집단별 정책이 일률적인 정책보다 효과적일 수 있으며 일부 집단은 맞춤 조치의 이익을 얻을 수 있음을 보였다.[^p5] | 마지막 저자 |
| 6 | 2024 | [Systematic Review on Healthcare Systems Engineering utilizing ChatGPT](https://doi.org/10.48550/arXiv.2405.11817) · arXiv 사전 공개본 | 의료 시스템 공학의 학회 발표 초록 9,809개를 ChatGPT로 분석하는 절차를 제시했다. 단계마다 프롬프트와 API 사용을 구성해 연구를 11개 주제 범주로 나누고 연도별 흐름과 세부 주제를 분석했다. 이 절차가 문헌 검토의 부담을 줄일 가능성을 살폈다.[^p6] | 마지막 저자 |

## 교수와 전문 분야

이태식 교수는 서울대학교 기계공학 학사(1997), MIT 기계공학 석사(1999)와 박사(2003)를 받았다. 2007년 9월 KAIST 산업및시스템공학과 조교수로 부임했고, 2012년 9월 부교수, 2019년 9월 교수로 재직하기 시작했다. 교수 소개는 2026년 7월부터 KAIST 공과대학장을 맡고 있다고 적는다.[^prof]

교수 소개의 연구 관심은 의료 데이터 분석, 재난 대응 시스템, 대규모 시스템의 모델링·시뮬레이션, 시스템 공학과 불확실성 아래 의사결정이다.[^prof] 최근 연구에서는 일부 행위자의 제어와 시스템 구성 설계, 보상·계약을 통한 의사결정 조정이 한 축이고,[^p1][^p2] 개인의 선택을 반영한 감염병 정책 모형이 다른 축이다.[^p4][^p5] 연구실의 병원 선택·지불 체계 연구 소개와 함께 보면, 사람과 기관의 행동을 전체 서비스 체계의 설계 문제로 연결하는 것이 전문 분야다.[^projects]

## 응용 분야

연구실은 의료서비스와 물류 시스템의 설계·운영을 주요 응용으로 적는다.[^home] 현재 연구 소개는 병원 선택, 의료비 지불 체계, 의료서비스 권역과 병원 사이 환자 공동 이용 관계를 다룬다.[^projects] 대표 연구의 적용 대상은 뉴욕시 택시 운영,[^p1] 자율 로봇 집단의 탐사,[^p3] 거리두기와 격리 정책[^p4][^p5]이다. 의료 시스템 공학의 연구 초록을 정리하는 분석 절차도 개발했다.[^p6]

## 구성원

2026년 10월 31일 구성원 페이지 기준으로 박사과정 구획 5명, 석사과정 구획 4명이다. 이름·구획·연구 관심·학교 이메일은 그 페이지의 표기이며 시작 시점은 개인 소개의 현재 과정 시작 시점이다.[^people][^huijae][^jungwoo][^joon][^jeongmin][^minyoung][^ryangha][^yeowon][^seonghun][^jeongyeon] 개인 소개에서 Jungwoo Kim은 산업및시스템공학 석박사통합과정, Minyoung Kim은 데이터사이언스 석박사통합과정으로 적혀 있다.[^jungwoo][^minyoung] 「대표 논문 참여」는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 사람에게 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Huijae Kim | 박사과정 | Mar 2021 | Healthcare Service System Design, Data Analytics, Optimization | huijae.kim@kaist.ac.kr | 6 |
| Jungwoo Kim | 박사과정 | Mar 2021 | Discrete Choice Model, Epidemics, Applied Statistics, Agent-based Simulation, Healthcare Systems | jungwoo415@kaist.ac.kr | 5, 6 |
| Joon Im | 박사과정 | Feb 2025 | Decision Making under Uncertainty, Decision-focused Learning | joonim14@kaist.ac.kr |  |
| Jeongmin Son | 박사과정 | Mar 2026 | Optimization, Reinforcement Learning, AI-enabled Decision-making | jmson@kaist.ac.kr |  |
| Minyoung Kim | 박사과정 | Feb 2025 | Mathematical Modelling, Computational Statistics | mk5718@kaist.ac.kr |  |
| RyangHa Kim | 석사과정 | Feb 2025 | Healthcare Data Science, Data Analytics | ryangk2025@kaist.ac.kr |  |
| Yeowon Yun | 석사과정 | Mar 2026 | Data Science, Applied Statistics | yeowon@kaist.ac.kr |  |
| Seonghun Hong | 석사과정 | Aug 2026 | Operations Research, Reinforcement Learning | hshoon@kaist.ac.kr |  |
| JeongYeon Choi | 석사과정 | Aug 2026 | Healthcare System Optimization, Data Science | angels0501@kaist.ac.kr |  |

## 졸업생과 학위 논문

구성원 페이지의 박사 졸업생 13행과 석사 졸업생 28행이다(2010–2026년). 학위·연도·학위 논문 제목은 연구실 표기다. 같은 사람이 석사와 박사 학위로 각각 게시된 행은 그대로 두었다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Ji-Su Lee | Ph.D. (2026) |  | Designing Payment Schemes to Mitigate Patient Concentration in Competitive Hospital Markets |
| Kyeonghyeon Park | Ph.D. (2025) |  | System design framework for non-cooperative multi-agent systems |
| Hyelim Shin | Ph.D. (2024) |  | Optimal epidemic control incorporating the effect of individual policy compliance decision on the spread of disease |
| Hyunjin Lee | Ph.D. (2020) |  | Data-driven approach for demand estimation and optimization of EMS system operation |
| Hyun-Rok Lee | Ph.D. (2020) |  | Algorithm and application of imitation learning and reinforcement learning for sequential decision making problems with multiple agents |
| Kyohong Shin | Ph.D. (2019) |  | Sequential Decision Making Problems for Operation Management of Emergency Medical Services System in Mass-casualty Incidents |
| Kyosang Hwang | Ph.D. (2019) |  | Location Problem of Medical Institutions in the Medically Under-served Areas in Korea Considering Demand Patterns Using Choice Model |
| Hochang Nam | Ph.D. (2019) |  | Analysis of Effect of Information in Application-based Taxi Service System |
| Hyunil Noh | Ph.D. (2017) |  | Modeling and Analysis of Enhanced Information and Decision-Making through Introduction of Combat Information System |
| Inkyung Sung | Ph.D. (2016) |  | Optimal Allocation of Emergency Medical Resources in Mass Casualty Incidents |
| Youngwoo Lee | Ph.D. (2016) |  | Development of Combat Effectiveness Metric Using Network Representation of Combat Environment |
| Hoon Jang | Ph.D. (2014) |  | Location Problems for Designing Trauma Care System in Korea |
| Soonyong Bae | Ph.D. (2011) |  | A Research Model for Consumer's Perception of Online Consumer Reviews |
| Jihwan Bae | M.S. (2026) |  | Constructed Experience Measure and Hospital Choice: Decomposing Preference Heterogeneity and State Dependence |
| Haoyuan Cui | M.S. (2026) |  | Learning Coordinated Policies for Multi-Agent Navigation in Mixed-Motive Environments |
| Eunbi Na | M.S. (2026) |  | Estimating the Causal Effects of Universal Policies Using Spatial Panel Models |
| Jeongmin Son | M.S. (2026) |  | Dynamic Control Group Selection and Policy Design in Partially Controllable Multi-Agent Systems |
| Joongchan Ahn | M.S. (2026) |  | Balancing Distance and Volume for Optimizing Emergency Medical Systems |
| Anurag Yadav | M.S. (2025) |  | Unveiling True Patient Demand: A Novel Approach Using Modified Kaplan-Meier Estimator |
| Yong Hoon Choi | M.S. (2025) |  | A Study on Combat-Effect-Oriented Resource Allocation Under Limeted Logistical Capabilities |
| Jeong Yeo | M.S. (2024) |  | Analyzing the Supply Chain Network Created from the Conventional Relation Extraction Model and ChatGPT: Focusing on S&P 500 Companies |
| Junyoung Jung | M.S. (2023) |  | Estimation of the First Arrival Time on the Epidemic Disease Transmission Network |
| Yuna Kim | M.S. (2022) |  | Rethinking the Value of Representation Pairs via Supervised Momentum Contrastive Learning |
| Hyewon Park | M.S. (2022) |  | Effectiveness of network-based social distancing policy considering adherence with quarantine policy |
| Yoorim Song | M.S. (2021) |  | Optimization of Bus Operation System Considering the Passenger Arrival Pattern |
| Huijae Kim | M.S. (2021) |  | Designing and Analizing a Deep-learning-based Multi-input model to Predict the Outcome of R&D Projects |
| Tooba Binte Asif | M.S. (2021) |  | Healthcare Resource Allocation Model Incorporating Consumer Choice and Its Uncertainty |
| Kyeonghyeon Park | M.S. (2020) |  | Analyzing Korean Inpatient Care Supply Structure Reform Strategies With a Dynamic Simulation Model |
| Monica Campana | M.S. (2020) |  | Case Study on the Ambulance Location in the Dominican Republic |
| Taehyun Kim | M.S. (2019) |  | Impact of Price Regulation and Market Intervention in Health Care Market Competition with Semi-Altruistic Providers |
| Kyuhyeon Shin | M.S. (2018) |  | Improving the Measurement of the Korean Emergency Medical System's Spatial Accessibility |
| Soochan Kim | M.S. (2018) |  | Countermaneuver Support Mission Scheduling Considering the Job Splitting and Cooperation Property |
| Mohamed T.A. Mohamed | M.S. (2017) |  | Mathematical Modelling and Optimization of Distributed Capacitated Kidney Paired Donation Programs with Transportability Kidneys After Nephrectomy |
| Yona Kim | M.S. (2017) |  | Defining Health Serivce Areas in Korea for Research on Geographic Variations in Health Service Utilization |
| Inseon Baek | M.S. (2016) |  | Maximal Covering Location Problem Modeling on the Passive Bistatic Radar Systems for Detecting Small Unmanned Aerial Vehicles |
| Jukrin Moon | M.S. (2014) |  | Infrastructure Interdependency Modeling for Cascading Failure Assessment |
| KyungHyeok Baek | M.S. (2012) |  | Study on the Optimal Location of Low Altitude Air Defense Radar |
| Seungeun Lee | M.S. (2011) |  | The Effect of Each Measure of the Network Centralities in the Aspect of Disease Intervention |
| Nara Yeon | M.S. (2011) |  | A Study on Scenario Screening for Stochastic Disease Spreading Models Using Simulation |
| Jihyun Yoon | M.S. (2010) |  | Factors Affecting Consumer's Trust on Internet Health Information |
| Heoksung Lee | M.S. (2010) |  | Factors Affecting User Acceptance of the Online Health Information Providing Service |

## 최근 논문 목록 (2021–2026)

아래 목록은 의료서비스의 입지·권역·지불·선택 모형과 정책 설계, 다중 행위자 학습, 항공 교통시설 입지, 문서 관계 추출과 도시 접근성 분석을 다룬다. 연구실 Publications와 교수·구성원 개인 소개의 50개 게시 행에 arXiv 사전 공개본 4개를 더한 54행이다. 같은 제목의 다른 학회 발표와 학술지판도 게시 행별로 실었다. 연구실 목록의 제목·저자·발표처·날짜는 게시 표기이며, 별도로 덧붙인 사전 공개본은 판본과 등록일을 표시했다. 2022년 격리 정책 학회 논문의 연결된 arXiv 판은 2024년에 등록되었다.[^pubs][^huijae][^jungwoo][^prof][^p1][^p2][^p3][^p4][^p5]

**2026**

- Optimal social distancing policy incorporating compliance of individuals, Shin, H. and Lee, T., Socio-Economic Planning Sciences, August, 2026 <https://doi.org/10.1016/j.seps.2026.102577>
- From Feasible to Valuable Infeasible: a Dual-Population Framework for Healthcare Districting, Kim, H. and Lee, T., 2026 INFORMS Healthcare Conference, Raleigh, NC, USA, July 28, 2026
- Modular Latent Class Choice Model, Kim, J. and Lee, T., International Choice Modelling Conference 2026, Gold Coast, Australia, July 22, 2026
- Learning Coordinated Policies for Multi-Agent Navigation in Mixed-Motive Environments, Cui, H. and Lee, T., 2026 KIIE Annual Spring Conference, Gyeongju, Korea, June 05, 2026
- 의료이용경험 지표의 구조화와 병원선택 선호 이질성 분석, Bae, J., Kim, J., and Lee, T., 2026 KIIE Annual Spring Conference, Gyeongju, Korea, June 05, 2026
- 데이터 기반 지역보건의료 인프라 배치 최적화 모형 개발, Kim, R., Im, J., Lee, J., and Lee, T., 2026 KIIE Annual Spring Conference, Gyeongju, Korea, June 05, 2026
- "A Conceptual Framework for Spatial Accessibility: Aligning Metrics with Urban Service Determinants", Ahn, J., Kim, H., Yoon, Y., and Lee, T., Mar 16, 2026 [SSRN] <https://doi.org/10.2139/ssrn.6355478>[^supp-access]
- "Urban Accessibility Analytics via LLM-MCP: Service-Aware Metric Recommendation and GIS Execution", Kim, H., Ahn, J., Yoon, Y., and Lee, T., KCC 2026, Jeju, Korea, Jun 25, 2026
- "Constructed Experience Measure and Hospital Choice: Decomposing Preference Heterogeneity and State Dependence", Bae, J., Kim, J., and Lee, T., 2026 KIIE Annual Spring Conference, Gyeongju, Korea, June 5, 2026

**2025**

- Agent-based Model of Dynamics between Objective and Perceived Quality of Healthcare System, Kim J., Lee M., Lee J., Do Y., and Lee T., 2025 Winter Simulation Conference, Seattle, WA, USA, December 09, 2025 <https://doi.org/10.1109/wsc68292.2025.11339019>
- Disentangling Experience and Attribute Effects in State Dependence Hospital Choice Model, Bae, J., Kim, J. and Lee, T., 2025 KIIE Annual Fall Conference, Daejeon, Korea, November 07, 2025
- Balancing Distance and Volume for Optimizing Emergency Medical Systems, Ahn, J., Lee, J. and Lee, T., 2025 KIIE Annual Fall Conference, Daejeon, Korea, November 06, 2025
- Dynamic control group and policy design in partially controllable multi-agent systems, Son, J., Park, K. and Lee, T., 2025 KIIE Annual Fall Conference, Daejeon, Korea, November 06, 2025
- Combinatorial Latent Class Choice Model for Capturing Multidimensional Preference Heterogeneity, Kim, J. and Lee, T., 2025 INFORMS Annual Meeting, Atlanta, GA, USA, October 28, 2025
- Multi-Objective Evolutionary Optimization for Healthcare Districting: A Customized NSGA-II Approach, Kim, H. and Lee, T., 2025 INFORMS Annual Meeting, Atlanta, GA, USA, October 28, 2025
- Gatekeeper’s Competition and Optimal Payment Scheme in Healthcare, Lee, J., Hwang, W. and Lee, T., 2025 INFORMS Annual Meeting, Atlanta, GA, USA, October 27, 2025
- Agent-Based Model of Quality–Perception Dynamics in Healthcare System: Does Providing Quality Information Mitigate or Intensify Patient Concentration?, Kim, J., Lee, M., Lee, J., Do, Y. and Lee, T., 2025 Korean Society for Preventive Medicine Annual Fall Conference, Busan, Korea, October 24, 2025
- Gatekeeper’s Competition and Optimal Payment Scheme in Healthcare, Lee, J., Hwang W. and Lee T., 2025 KIIE Annual Spring Conference, Jeju, Korea, June 18, 2025
- Multi-objective Optimization Algorithm for Delineating Healthcare Service Areas Based on NSGA-II, Kim, H. and Lee, T., 2025 KIIE Annual Spring Conference, Jeju, Korea, June 18, 2025
- Effectiveness of social distancing under partial compliance of individuals, Shin, H. and Lee, T., European Journal of Operational Research, May, 2025 <https://doi.org/10.1016/j.ejor.2024.11.006>
- Reward design in multi-agent systems using successor features and multi-information source bayesian optimization, Park, K., Molina Concha, D., Lee, H-R., Lee, T. and Lee, C-G., International Journal of Machine Learning and Cybernetics, April, 2025 <https://doi.org/10.1007/s13042-025-02622-z>
- Kyeonghyeon Park, David Molina Concha, Hyun-Rok Lee, Chi-Guhn Lee, Taesik Lee. "Hypernetwork-based approach for optimal composition design in partially controlled multi-agent systems". arXiv:2502.12605 (사전 공개본, 2025-02-18). <https://arxiv.org/abs/2502.12605>

**2024**

- Ammunition Distribution Planning in Lanchester type Multi-unit Combat, Choi, Y., Kim, J. and Lee, T., 2024 KIIE Annual Fall Conference, Seoul, Korea, October 25, 2024
- Korea’s Healthcare Service Areas: A Review of Delineation Methods and Proposal for an Adjustment Framework, Kim, H., Lee, J. S. and Lee, T., Korea Society of Preventive Medicine Fall Conference, Busan, Korea, October 24, 2024
- Optimization for Delineating Healthcare Service Areas Integrating Geographical Contiguity and Soft Constraints, Kim, H. and Lee, T., Korea Society of Preventive Medicine Fall Conference, Busan, Korea, October 24, 2024
- A Game Theoretic Approach to Efficient and Equitable Healthcare Quality Improvement Policies for Regional Disparity, Lee, J., Hwang, W. and Lee, T., INFORMS Annual Meeting 2024, Seattle, USA, October 23, 2024
- An Extended Latent Class Choice Model for Characterizing Context-driven hospital choice, Kim, J. and Lee, T., INFORMS Annual Meeting 2024, Seattle, USA, October 23, 2024
- Hypernetwork-based approach for optimal composition design in partially controlled multi-agent systems, Park, K., Molina Concha, D., Lee, H., Lee, C. and Lee, T., INFORMS Annual Meeting 2024, Seattle, USA, October 22, 2024
- Reward function design method to achieve system-level objectives in ambulance diversion problem, Lee, H-R. and Lee, T., European Journal of Operational Research, September, 2024 <https://doi.org/10.1016/j.ejor.2024.04.033>
- Systematic review on Healthcare Systems Engineering utilizing ChatGPT, Kim, J., Lee, J.-S., Kim, H. and Lee, T., arXiv, May, 2024
- 의료이용 데이터를 활용한 의료기관 기능 강화 최적화 모형, Choi, Y., Lee, J. and Lee, T., 2024 KIIE Annual Spring Conference, Yeosu, Korea, May 03, 2024
- Analysis Framework for deriving patient sharing communities in hospital networks, Im, J., Kim, J. and Lee, T., 2024 KIIE Annual Spring Conference, Yeosu, Korea, May 03, 2024
- Unveiling True Patient Demand: A Novel Approach Using Modified Kaplan-Meier Estimator, Yadav, A., Kim, J. and Lee, T., 2024 KIIE Annual Spring Conference, Yeosu, Korea, May 03, 2024
- David Molina Concha, Kyeonghyeon Park, Hyun-Rok Lee, Taesik Lee, Chi-Guhn Lee. "Algorithmic Contract Design with Reinforcement Learning Agents". arXiv:2408.09686 (사전 공개본, 2024-08-19). <https://arxiv.org/abs/2408.09686>
- David Molina Concha, Jiping Li, Haoran Yin, Kyeonghyeon Park, Hyun-Rok Lee, Taesik Lee, Dhruv Sirohi, Chi-Guhn Lee. "Bayesian Optimization Framework for Efficient Fleet Design in Autonomous Multi-Robot Exploration". arXiv:2408.11751 (사전 공개본, 2024-08-21). <https://arxiv.org/abs/2408.11751>
- Hyelim Shin, Taesik Lee. "Effectiveness of Social Distancing under Partial Compliance of Individuals". arXiv:2408.14226 (사전 공개본, 2024-08-26). <https://arxiv.org/abs/2408.14226>

**2023**

- Exploring optimal policies for alleviating patient concentration in metropolitan large hospitals using mathematical models and game theory, Lee, J. S. and Lee, T., 2023 Korean Society for Preventive Medicine Annual Fall Conference, Incheon, Korea, November, 2023
- Characterizing Multi-class Heterogeneity of Cancer Patients’ Local Hospital Bypassing Choices, Kim, J., Lee, J. and Lee, T., 2023 Korean Society for Preventive Medicine Annual Fall Conference, Incheon, Korea, November, 2023
- Comparing Document Relation Extraction Utilizing Conventional Relation Extraction Model and Chat-GPT: A Focus on 5 Companies, Yeo. J., Lee, T., Moon, I. C., 2023 KIIE Annual Fall Conference, Ulsan, Korea, November, 2023
- An Improved Methodology for Delineating Hospital Service Area, Kim, H., Lee, J. S. and Lee, T., 2023 KIIE Annual Fall Conference, Ulsan, Korea, November, 2023
- Optimal policies for alleviating patient concentration in metropolitan large hospitals, Lee, J. S. and Lee, T., 2023 KIIE Annual Fall Conference, Ulsan, Korea, November, 2023
- Exploring Research Trends of Healthcare System Engineering using Chat-GPT, Kim, J., Kim, H., Lee, J. and Lee, T., 2023 KIIE Annual Fall Conference, Ulsan, Korea, November, 2023
- Patient Sharing Network Analysis of South Korean Hospitals using NHIS Claim Data, Im, J., Kim, J., and Lee, T., 2023 KIIE Annual Fall Conference, Ulsan, Korea, November, 2023
- Skyport location problem for urban air mobility system, Shin, H., and Lee, T., 2023 INFORMS annual meeting, Pheonix, USA, November, 2023
- Optimal social distancing policy under partial social compliance, Shin, H., and Lee, T., 2023 INFORMS annual meeting, Pheonix, USA, October, 2023
- A Novel Choice Analysis Technique for Understanding Patients’ Hospital Selection, Kim, J., Lee, J., and Lee, T., INFORMS Healthcare Conference 2023, Toronto, Canada, July 27, 2023
- Designing optimal payment system for functionally distinguishing medical institutions based on the characteristics of medical services, Lee, J. S. and Lee, T., 2023 KIIE Annual Spring Conference, Jeju, Korea, June 01, 2023
- Optimal social distancing policy under partial social compliance, Shin, H., and Lee, T., 2023 KIIE Annual Spring Conference, Jeju, Korea, June 01, 2023

**2022**

- Effectiveness of Social Distancing under Partial Compliance of Individuals, Shin, H., Park, K., Kim, H., and Lee, T., 2022 INFORMS annual meeting, Indianapolis, USA, October 16, 2022
- 보상구조 설계를 위한 Successor Feature 기반 다중에이전트 강화학습 알고리즘, Molina Concha, D., Park, K., Lee, H., Lee, T., and Lee, C., 2022 KIIE Annual Spring Conference, Jeju, Korea, June 2, 2022
- Segmentized quarantine policy for managing a tradeoff between containment of infectious disease and social cost of quarantine, Kim, J. and Lee, T., IISE Annual Conference and Expo 2022, Seattle, USA, May 23, 2022
- "Choice-driven location-allocation model for healthcare facility location problem" Hwang, K., Asif, TB., Lee, T., Flexible Services and Manufacturing Journal, 2022 <https://doi.org/10.1007/s10696-021-09441-8>

**2021**

- Effect of a policy adherence on the efficacy of a 'bubble' social distancing strategy, Park, H. and Lee, T., 2021 KIIE Annual Fall Conference, Seoul, Korea, November 12, 2021
- Skyport location problem for urban air mobility system, Shin, H., Lee, T., Lee, H. R., Computers and Operations Research, November, 2021

## 연구과제

구성원 개인 소개에 게시된 과제 가운데 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 아래 12개 게시 문구다. 과제명·지원 기관·기간은 게시 표기다. Patient Journey 기반 의료전달체계 분석 과제는 한글·영문 표기를 각각 두었다.[^huijae][^jungwoo][^joon]

- Patient Journey 데이터 기반 의료전달체계 취약성 분석 연구 (지원 한국연구재단; 기간 Sep 2026 - Present)
- GS건설-KAIST 미래 도시 인공지능 핵심 기술 연구개발 (지원 GS건설; 기간 Jul 2024 - Mar 2026)
- 순천형 공공보건의료 마스터플랜 추진전략 수립 연구용역 (지원 순천시; 기간 Jan 2024 - Mar 2024)
- 지역 필수의료 제공체계 진료권 조정 (지원 국립중앙의료원; 기간 Jul 2023 - Jan 2024)
- 국가 연구개발사업의 전략적 예산배분을 위한 기계학습/최적화 기반 의사결정모형 설계 (지원 한국연구재단; 기간 Jan 2020 - Feb 2022)
- Simulation-Based Counterfactual Experiments for Explainable Causal Insights in Complex Adaptive Healthcare Systems (지원 NRF; 기간 Jul 2026 - Present)
- Statistical Modeling Study on Demands of Essential Healthcare Services and Infectious Disease Care, Based on Pandemic Scenarios (지원 National Medical Center (NMC); 기간 Apr 2025 - Present)
- Analysis of Patients and Providers’ Decision Making to Achieve Social Optimum of Korean Healthcare System (지원 NRF; 기간 May 2024 - Present)
- 감염병원 서비스를 위한 시스템 운영 모델 (2021년도) (지원 KAIST; 기간 Mar 2021 - Dec 2021)
- Data-driven Analysis of Healthcare Delivery System Vulnerability Based on Patient Journey (지원 NRF; 기간 Sep 2026 - Present)
- 국방 지능형 군집체계 연구 및 인력양성 (지원 ITRC; 기간 Jul 2024 - Present)
- 데이터 기반 지역보건의료 인프라 배치 최적화 모형 개발 (지원 한국건강증진개발원; 기간 Jul 2025 - Dec 2025)

## 수상과 선정

구성원 개인 소개에 게시된 2022–2025년 수상·선정 5건이다. 날짜는 게시된 연도·학기 또는 연월이며 수상·선정 이름의 등급은 원문대로 적었다.[^jungwoo][^jeongmin][^jeongyeon]

- 2023 · Jungwoo Kim: 대한예방의학회 제75차 가을학술대회 학생학술상 금상
- 2025-08 · Jeongmin Son: Next Generation Engineering Researcher Award, Institute for Promotion of Engineering and Science of Korea
- 2024 · JeongYeon Choi: Next Generation Engineering Researcher Award, Institute for Promotion of Engineering and Science of Korea
- 2023 Spring · JeongYeon Choi: Dean's List
- 2022 Fall · JeongYeon Choi: Dean's List

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 산업경영학동 2113호[^home]
- 연구실 전화: +82-42-350-3166[^home]
- 연구실 연락 이메일: joonim14@kaist.ac.kr[^home]
- 교수 이메일: taesiklee@kaist.ac.kr[^prof]
- 교수 전화·연구실: 042-350-2212, N7동 2501호(교수 개인 소개 표기)[^prof]
- 학부생 방문 안내의 교수연구실: E2 산업경영학동 2102호[^undergrads]
[^home]: 연구실 첫 화면. <https://csdlab.kaist.ac.kr/> (관측일 2026-10-30).

[^gsds]: KAIST 데이터사이언스대학원 구성원, 이태식 항목. <https://gsds.kaist.ac.kr/people> (관측일 2026-10-30).

[^people]: 연구실 People. <https://csdlab.kaist.ac.kr/people/> (관측일 2026-10-31).

[^pubs]: 연구실 Publications. <https://csdlab.kaist.ac.kr/publications/> (관측일 2026-10-31).

[^projects]: 연구실 Projects. <https://csdlab.kaist.ac.kr/projects/> (관측일 2026-10-31).

[^undergrads]: 연구실 For Undergrads. <https://csdlab.kaist.ac.kr/for-undergrads/> (관측일 2026-10-31).

[^prof]: 이태식 교수 개인 소개. <https://csdlab.kaist.ac.kr/people/Professor> (관측일 2026-10-31).

[^huijae]: Huijae Kim 개인 소개. <https://csdlab.kaist.ac.kr/people/huijae> (관측일 2026-10-31).

[^jungwoo]: Jungwoo Kim 개인 소개. <https://csdlab.kaist.ac.kr/people/jungwoo> (관측일 2026-10-31).

[^joon]: Joon Im 개인 소개. <https://csdlab.kaist.ac.kr/people/joonseok> (관측일 2026-10-31).

[^jeongmin]: Jeongmin Son 개인 소개. <https://csdlab.kaist.ac.kr/people/jeongmin> (관측일 2026-10-31).

[^minyoung]: Minyoung Kim 개인 소개. <https://csdlab.kaist.ac.kr/people/minyoung> (관측일 2026-10-31).

[^ryangha]: RyangHa Kim 개인 소개. <https://csdlab.kaist.ac.kr/people/ryangha> (관측일 2026-10-31).

[^yeowon]: Yeowon Yun 개인 소개. <https://csdlab.kaist.ac.kr/people/yeowon> (관측일 2026-10-31).

[^seonghun]: Seonghun Hong 개인 소개. <https://csdlab.kaist.ac.kr/people/seonghun.html> (관측일 2026-10-31).

[^jeongyeon]: JeongYeon Choi 개인 소개. <https://csdlab.kaist.ac.kr/people/jeongyeon> (관측일 2026-10-31).

[^p1]: K. Park 외, T. Lee, arXiv (사전 공개본) (온라인 2025-02-18). <https://doi.org/10.48550/arXiv.2502.12605> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.12605> (관측일 2026-10-31).

[^p2]: D. M. Concha 외, C.-G. Lee, arXiv (사전 공개본) (온라인 2024-08-19). <https://doi.org/10.48550/arXiv.2408.09686> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.09686> (관측일 2026-10-31).

[^p3]: D. M. Concha 외, C.-G. Lee, arXiv (사전 공개본) (온라인 2024-08-21). <https://doi.org/10.48550/arXiv.2408.11751> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.11751> (관측일 2026-10-31).

[^p4]: H. Shin, T. Lee, arXiv (사전 공개본) (온라인 2024-08-26). <https://doi.org/10.48550/arXiv.2408.14226> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.14226> (관측일 2026-10-31).

[^p5]: J. Kim, T. Lee, IISE Annual Conference and Expo 2022 (arXiv 사전 공개본) (온라인 2024-11-09). <https://doi.org/10.48550/arXiv.2411.08059> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2411.08059> (관측일 2026-10-31).

[^p6]: J. Kim, J.-S. Lee, H. Kim, T. Lee, arXiv (사전 공개본) (온라인 2024-05-20). <https://doi.org/10.48550/arXiv.2405.11817> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2405.11817> (관측일 2026-10-31).

[^supp-access]: J. Ahn, H. Kim, T. Lee, A Conceptual Framework for Spatial Accessibility: Aligning Metrics with Urban Service Determinants, SSRN Electronic Journal (2026). <https://doi.org/10.2139/ssrn.6355478> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=A%20Conceptual%20Framework%20for%20Spatial%20Accessibility%3A%20Aligning%20Metrics%20with%20Urban%20Service%20Determinants> (관측일 2026-10-31).

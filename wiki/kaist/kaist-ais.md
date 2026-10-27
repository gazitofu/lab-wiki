# 자율 지능형 시스템 연구실 (Autonomous and Intelligent Systems Laboratory, AIS Lab)

**KAIST 조천식모빌리티대학원 · 신효상 교수**

- 분야: 무인·자율 시스템의 계획·제어·인지, 다중 에이전트 의사결정, 정보 기반 추정
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^p1], 다중 에이전트 시스템·분산 의사결정[^multi], 상태 추정·필터링(데이터 동화)[^p7]
- 홈페이지: <https://sites.google.com/view/kaist-ais/home>
- 근거와 출처: [자율 지능형 시스템 연구실 근거 페이지](kaist-ais-sources.md)

> 도시 같은 복잡한 환경에서 무인·자율 시스템이 상황을 파악하고 움직이며, 여러 시스템이 서로 연결돼 임무를 수행하도록 계획·제어·정보 처리 방법을 연구한다.[^vision]

## 무엇을 연구하나

신효상(Hyo-Sang Shin) 교수가 이끄는 연구실로, 2024년 3월 KAIST 조천식모빌리티대학원에서 문을 열었다.[^dept][^news24] 연구 비전은 복잡한 환경에서 무인·자율 시스템을 운용하는 일, 서로 연결된 여러 무인 시스템의 협력, 그리고 정보를 중심으로 한 접근법 개발이다. 개별 시스템의 움직임뿐 아니라 여러 시스템의 연결과 자율적인 판단을 함께 다룬다.[^vision]

**시스템과 제어** 갈래는 자율 시스템을 위한 알고리즘(문제를 푸는 계산 절차)에 초점을 두며, 계획·행동·인지가 주요 연구 범위다.[^control] 대표 논문은 확률적으로 표현된 불확실성 아래의 안전 제어, 날개를 기울여 수직이착륙하는 무인기의 제어, 센서 측정과 근사 모형을 이용하는 안전 제어를 다룬다.[^p1][^p2][^p3]

**다중 에이전트 시스템**은 여러 행위자가 각자의 정보와 행동으로 서로 영향을 주고받는 시스템이다. 연구실은 수학적 최적화(조건을 만족하는 후보 가운데 평가 기준에 맞는 해를 찾는 계산)와 수치적 방법으로 협력 의사결정을 설계하고 분석한다. 목표는 여러 시스템이 필요한 임무를 수행하면서 운용자의 지시에 예측 가능한 방식으로 반응하게 하는 것이다.[^multi] 대표 논문에서는 여러 기체의 표적 배정과 경로를 함께 정하는 방법, 우주비행체들이 충돌을 피하며 배치를 바꾸는 경로 계획을 연구했다.[^p4][^p5]

**정보 기반 접근** 갈래는 인공지능과 대규모 자료를 자율 시스템 연구에 활용한다. 예상한 고장과 예상하지 못한 고장을 모두 견뎌야 하는 시스템을 다루고, 이론과 실험 양쪽에서 계산 방법을 연구한다고 소개한다.[^info] 대표 논문은 관측 자료와 모형으로 직접 알 수 없는 상태를 계산하는 상태 추정을 다룬다. 이동체가 어디로 향하는지와 그 움직임을 함께 추론하거나, 로봇이 거리 관측만으로 전파원의 위치를 찾을 때 생기는 불완전한 관측을 다룬다.[^p6][^p7]

## 주요 연구 주제

### 1. 불확실성과 센서 오차를 고려한 비행 제어

모형 예측 제어(Model Predictive Control, MPC)는 모형으로 앞으로의 상태를 예측해 일정 기간의 입력을 계산하고, 그중 앞부분을 적용한 뒤 새 자료로 다시 계산하는 제어 방법이다. Spectral-IRA 논문은 여러 안전 조건 중 하나라도 위반할 확률에 한도를 두는 결합 확률 제약을 다룬다. 제약 위반 위험을 대신 계산하는 선형 모형(변수들의 일차식으로 관계를 나타내는 모형)을 자료로 보정하고, 위험 허용량을 조정한다. 보정 자료의 분포에 대한 경험적 안전성을 고려한 방법이며, 모의실험에서 정해진 위험 허용량을 만족했다고 보고했다.[^p1]

틸트윙 무인기 제어 논문은 날개를 기울여 수직이착륙하는 무인기가 모형 오차와 외란(시스템 밖에서 들어오는 영향)이 있는 환경에서 기준 응답(시스템이 따르도록 정한 목표 반응)을 따르도록 한다. 안쪽과 바깥쪽의 제어 고리를 함께 쓰고, 운용 방식에 따라 제어 명령을 여러 구동 수단에 배분한다. 비선형 비행 동역학 모형(상태와 입력의 관계가 변수들의 일차식으로 표현되지 않는 비행 모형)으로 제어 성능을 살폈다.[^p2]

센서 기반 안전 제어 논문은 제어 장벽 함수(Control Barrier Function, 안전 영역 안에 머물도록 입력에 조건을 부여하는 함수)를 다룬다. 센서 기반의 차수를 줄인 근사 모형(시스템의 움직임을 적은 수의 상태 변수로 나타낸 모형)을 사용한 MRICBFs(Measurement-Robust Incremental Control Barrier Functions, 측정 오차에 강건한 증분 제어 장벽 함수)를 제안한다. 증분은 현재 상태 부근의 변화량을 중심으로 계산한다는 뜻이다. 센서 정확도와 근사 오차를 고려하면서 모형 일부를 실시간 측정으로 대신하고, 논문이 다룬 종류의 모형 불확실성 아래에서 안전 조건을 보장하도록 구성했다. 검증은 수치 모의실험이다.[^p3]

### 2. 여러 기체의 배정과 충돌 회피 경로 계획

여러 유도탄과 표적을 다룬 논문에서는 표적 배정과 비행 경로를 따로 정하지 않고 같은 목적함수(해의 좋고 나쁨을 수치로 평가하는 함수) 아래에서 함께 최적화했다. 시간에 따른 제어 입력 계획을 국소 근사로 반복 계산하는 미분 동적 계획법을 바탕으로 두 문제를 연결하고, 수치 모의실험으로 방법을 평가했다.[^p4]

우주비행체 군집 재배치 논문은 도달 가능 집합(주어진 조건에서 시스템이 도달할 수 있는 상태들의 집합)을 이용한다. 현재와 미래의 충돌을 피하는 조건을 경로 계산에 넣어, 여러 우주비행체가 배치를 바꿀 때 충돌을 피하고 연료를 고려하는 경로를 만든다. 계산 시점 사이에서 일어날 수 있는 충돌도 다루며, 결과는 수치 모의실험으로 확인했다.[^p5]

### 3. 이동체의 의도와 위치를 함께 추정

목적지 추론 논문은 이동체의 목적지를 그 이동체의 의도로 보고, 관측 전의 가설 확률을 새 관측을 이용해 갱신하는 베이지안 추론으로 목적지와 시간에 따른 상태를 함께 추정한다. 목적지가 주어졌을 때의 움직임을 조건부 마르코프 과정(주어진 조건 아래에서 다음 상태의 분포가 현재 상태에 의존하고 그 이전 경로에는 추가로 의존하지 않는 확률 과정)으로 나타내고, 여러 목적지 후보 가운데 관측 후 확률이 가장 큰 후보를 고른다. 여러 칼만 필터(선형 모형의 예측과 관측을 오차의 크기에 따라 결합해 상태를 갱신하는 필터)의 결과를 결합하며, 수치 모의실험으로 평가했다.[^p6]

전파원 탐색 연구는 측정 자료가 대상의 상태를 모두 보여 주지 않는 부분 관측 문제를 다룬다. 제안한 가우스 혼합 필터(Gaussian Mixture Filter)는 여러 정규 분포를 결합한 확률 분포로 상태를 표현하고 관측에 따라 갱신하는 방법이다. 확률 분포는 가능한 값이나 값의 범위에 확률을 대응시키는 수학적 표현이다. 정규 분포는 평균과 분산으로 정해지며 평균을 중심으로 좌우 대칭인 연속 확률 분포다. 분산은 값과 평균의 차이를 제곱해 평균 낸 값으로, 값들이 퍼진 정도를 나타낸다. 연구진은 수치 문제와 실제 로봇 현장 실험에서 기존 필터와 비교했으며, 거리만 관측하는 조건과 측정 모형의 불확실성을 다뤘다.[^p7]

## 대표 논문

교수가 저자로 참여한 KAIST 재직 시기의 논문 7편을 시스템·제어 3편, 다중 에이전트 2편, 정보 기반 접근 2편으로 골랐다. 「쉽게 말하면」은 각주에 밝힌 OpenAlex 등록 초록 3편, Crossref 등록 초록 2편, arXiv 판 초록 2편만을 근거로 썼다. 연도는 연구실 게시 연도 구역이며, arXiv 사전 공개본은 표에 판본을 구분했다. 3번 arXiv 개정판은 ACC 2025 채택을 명시한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

| 번호 | 연도 | 논문·확인한 판본 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Calibration-Aware Convex Surrogate MPC for Nonlinear Joint Chance-Constrained Control via Spectral Risk Allocation](https://doi.org/10.1109/lcsys.2026.3710526) · IEEE Control Systems Letters | 여러 안전 조건 중 하나라도 위반할 확률에 한도를 두는 제어 방법이다. 자료로 보정한 위험 대체 모형을 사용하고 위험 허용량을 조정한다. 보정 자료의 분포에 대한 경험적 안전성을 다루며, 모의실험에서 정해진 위험 허용량을 만족했다고 보고했다.[^p1] | 마지막 저자(전체 3명) |
| 2 | 2025 | [Complementary Filter‐Based Incremental Nonlinear Model Following Control Design for a Tilt‐Wing UAV](https://doi.org/10.1002/rnc.7743) · International Journal of Robust and Nonlinear Control | 틸트윙 수직이착륙 무인기가 모형 오차와 외란이 있어도 기준 응답을 따르도록 하는 비선형 제어다. 안팎의 제어 고리와 운용 방식에 따른 제어 명령 배분을 결합했다. 비행 동역학 모형을 이용해 성능을 평가했다.[^p2] | 마지막 저자(전체 2명) |
| 3 | 2025 | [Sensor-Based Safety-Critical Control Using an Incremental Control Barrier Function Formulation via Reduced-Order Approximate Models](https://arxiv.org/abs/2410.08096) · arXiv 개정판, ACC 2025 채택 | 센서 기반 근사 모형으로 제어 장벽 함수를 만들고, 측정 오차와 근사 오차를 고려해 모형 일부를 실시간 측정으로 바꾼다. 특정 종류의 모형 불확실성에 대해 안전 보장을 유지하는 방법을 제안하고 수치 모의실험으로 살폈다.[^p3] | 마지막 저자(전체 2명) |
| 4 | 2024 | [Integrated Target Assignment and Trajectory Optimization for Many-to-Many Midcourse Guidance](https://doi.org/10.1109/taes.2024.3448408) · IEEE Transactions on Aerospace and Electronic Systems | 여러 유도탄과 표적이 있는 문제에서 표적 배정과 경로 최적화를 함께 푼다. 미분 동적 계획법을 바탕으로 두 문제가 같은 목적함수를 공유하게 하고, 수치 모의실험과 비교로 방법의 유효성을 평가했다.[^p4] | 전체 4명 중 2번째 공저자 |
| 5 | 2024 | [Trajectory Planning of Spacecraft Swarm Reconfiguration Using Reachable Set-Based Collision Constraints](https://doi.org/10.1109/taes.2024.3406312) · IEEE Transactions on Aerospace and Electronic Systems | 여러 우주비행체가 배치를 바꿀 때 충돌을 피하고 연료를 고려하는 경로를 계산한다. 도달 가능 집합을 이용한 현재·미래 충돌 조건을 적용하며, 계산 시점 사이의 충돌도 다룬다. 수치 모의실험으로 유효성을 확인했다.[^p5] | 마지막 저자(전체 5명) |
| 6 | 2024 | [Destination and time-series inference of moving objects via conditionally Markov process](https://doi.org/10.1007/s13272-024-00763-5) · CEAS Aeronautical Journal | 이동체가 향하는 목적지를 의도로 보고 목적지와 움직임을 함께 추정한다. 조건부 마르코프 모형과 여러 목적지 가설, 칼만 필터 추정값의 결합을 이용한다. 알려지지 않은 최종 조건에는 상대적 위치 관계를 이용한 매개변수 보정을 적용하고 수치 모의실험으로 평가했다.[^p6] | 마지막 저자(전체 2명) |
| 7 | 2025 | [Autonomous Robotic Radio Source Localization via a Novel Gaussian Mixture Filtering Approach](https://arxiv.org/abs/2503.10349) · arXiv 사전 공개본 | 로봇이 알지 못하는 환경에서 전파원을 찾을 때 쓰는 가우스 혼합 필터를 제안했다. 수치 문제와 실제 로봇 현장 실험에서 기존 필터와 비교했다. 거리만 관측하는 조건에서도 추정 성능과 계산 부담, 강건성 측면의 개선을 보고했다.[^p7] | 전체 5명 중 4번째 공저자 |

## 교수와 전문 분야

신효상 교수는 2024년 3월부터 KAIST 조천식모빌리티대학원 교수이며 Cranfield University 겸임교수이기도 하다. 그 전에는 Cranfield University에서 Lecturer, Senior Lecturer, Reader를 거쳐 2019년 10월부터 2024년 2월까지 교수로 재직했다. 2004년 부산대학교 항공우주공학 학사, 2006년 KAIST 항공우주공학 석사, 2011년 Cranfield University Informatics & Systems Engineering 박사 학위를 받았다고 소개한다.[^prof]

교수가 직접 적은 관심 분야는 다중 에이전트 의사결정, 도심 항공 모빌리티(Urban Air Mobility, UAM), 무인 항공 교통 관리(Unmanned Traffic Management, UTM), 정보 기반 센싱과 융합, 정밀 항법·시간 정보, 여러 기체의 협력, 인공지능 기반 유도·제어다.[^prof] 대표 논문에서 확인되는 전문 분야는 불확실성과 모형·센서 오차를 고려하는 제어,[^p1][^p2][^p3] 여러 기체의 배정·충돌 회피 경로 계획,[^p4][^p5] 이동체의 의도와 상태 추정이다.[^p6][^p7]

학술 활동으로 IEEE Transactions on Aerospace and Electronic Systems, Chinese Journal of Aeronautics, Journal of Intelligent and Robotic Systems 등의 편집 업무를 소개한다. 강의에는 센서 융합과 네트워크로 연결된 다중 에이전트 시스템의 최적화를 다루는 MO869가 있다.[^prof][^lectures]

## 응용 분야

연구실이 밝힌 응용 대상은 도시 같은 복잡한 환경에서 운용하는 무인 시스템과 연결된 여러 무인 시스템이다.[^vision] 교수 소개에는 도심 항공 모빌리티와 무인 항공 교통 관리가 있고, 과제에는 도심 무인 항공기의 위험 예측·평가, 자율 전기 수직이착륙 항공기의 기술, 유무인 협력을 위한 센서 융합·임무 계획이 있다.[^prof][^projects] 대표 논문은 무인기의 비행 제어, 여러 유도탄의 배정·경로 계산, 우주비행체 군집의 재배치, 이동체와 전파원의 추정을 다룬다.[^p2][^p4][^p5][^p6][^p7]

## 구성원

2026년 10월 26일 누리집 Members에 게시된 22명이다. 박사후 연구원 2명, 박사과정 9명, 석사과정 8명, 방문 학생 2명, 학부생 1명이며, 과정·시작 시기·연구 주제는 원문 표기다. 시작 칸의 학기와 역할 표기도 원문대로다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| On Park | 박사후연구원 |  | Flight dynamics; Optimisation and Reinforcement Learning in Control Design for Unmanned Aerial Vehicle |  |
| Bhaskar Biswas | 박사후연구원 |  | Stability Analysis; Control Systems; Guidance |  |
| Soyeon Koo | 박사과정 | Lab Representative, Fall 2024 | Decision Making; Multi-Agent Systems | 1 |
| Sejin Jang | 박사과정 | Fall 2024 | Multi-Agent Systems |  |
| Lai Dang Quoc Vinh | 박사과정 | Fall 2024 | Deep Learning; Time Series Forecasting |  |
| Medhavi Mishra | 박사과정 | Spring 2025 | Multi-Modal Perception; Deep Learning Application in ITS |  |
| Hong-Woo Seok | 박사과정 | Spring 2026 | Multi-Agent Systems; Cooperative Localization |  |
| Eun-Woo Sung | 박사과정 | Spring 2026 | Distributed Control and Estimation; Multi-Agent Systems |  |
| Suyoung Shin | 박사과정 | Spring 2026 | Air Traffic Management |  |
| Gangsan Kim | 박사과정 | Fall 2026 | Optimization; Multi-agent Systems |  |
| Haoyuan Cui | 박사과정 | Fall 2026 | Learning-based Control; Multi-Agent Systems |  |
| Jinyoung Jeong | 석사과정 | Spring 2025 | Flight Dynamics and Control; Probabilistic Risk Mapping; Multi-Agent Systems |  |
| Sohyun Kim | 석사과정 | Spring 2025 | Bayesian Inference |  |
| Sungmin Lee | 석사과정 | Fall 2025 | Sensor Fusion; Localization and Mapping |  |
| Jun Choi | 석사과정 | Fall 2025 | Flight Dynamics and Control |  |
| Ha-Eun Kim | 석사과정 | Fall 2025 | Multi-Agent Systems; Decision Making |  |
| Seunghyeon Choi | 석사과정 | Spring 2026 | Dynamic Behavior; Control and Optimization |  |
| Minwoo Lee | 석사과정 | Spring 2026 | Decision Making; Facility Layout Problem |  |
| Hong Minh Pham | 석사과정 | Spring 2026 | Multi-Agent Systems |  |
| Raphaël Marschall | 방문 학생 | Fall 2026 - Supmeca | Multi-Agent Systems; Causal Analysis; Machine Learning |  |
| Margaux Venis | 방문 학생 | Fall 2026 - Supmeca | Multi-Agent Systems; Causal Analysis; Fault Diagnosis |  |
| Wenqu Fang | 학부 연구생 | Summer 2025 - URP | Multi-Agent Systems; Path Planning; Reinforcement Learning |  |

## 졸업생과 이전 구성원

Alumni의 이전 Research Fellow 15명, PhD 졸업생 22명, MSc 졸업생 77명이다. 학위 졸업 연도는 2012–2026년이며, 이전 Research Fellow 구획에는 연도가 없다. 2024년 3월 KAIST 부임 전 Cranfield 연구그룹의 구성원이 함께 실린 목록으로, 모두 KAIST 졸업생이라는 뜻은 아니다. 학위·주제·진로는 누리집 표기다.[^alumni][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seokwon Lee | 이전 Research Fellow | Currently Assistant Professor at Chung-Ang University |  |
| Vijay Shankar Dwivedi | 이전 Research Fellow |  |  |
| Teng Li | 이전 Research Fellow |  |  |
| Joongsup Yun | 이전 Research Fellow |  |  |
| Shuoyuan Xu | 이전 Research Fellow |  |  |
| Jose Castiblanco Quintero | 이전 Research Fellow |  |  |
| Ruifan Liu | 이전 Research Fellow |  |  |
| Namhoon Cho | 이전 Research Fellow | Currently Assistant Professor at Seoul National University |  |
| Sabyasachi Mondal | 이전 Research Fellow | Currently Lecturer at Cranfield University |  |
| Hae-In Lee | 이전 Research Fellow | Currently Lecturer at Cranfield University |  |
| Kacper Grzedzinski | 이전 Research Fellow |  |  |
| Oscar Gonzales | 이전 Research Fellow |  |  |
| Minguk Seo | 이전 Research Fellow |  |  |
| Juhyeon Hong | 이전 Research Fellow |  |  |
| Dmitry Ignatyev | 이전 Research Fellow | Currently Senior Lecturer at Cranfield University |  |
| Sukkeun Kim | PhD (2026) |  | Hybrid Bayesian Estimation Approaches for Tracking and Localisation in Complex Environments |
| Jongyun Kim | PhD (2025) |  | Flocking Control Methods for a Multi-Agent System Using Deep Reinforcement Learning and Lazy Workers |
| Matthew Osborne | PhD (2024) |  | Safe online learning for nonlinear dynamical systems using control contraction metrics |
| Saki Omi | PhD (2024) |  | Development of the Performance Evaluation of COTM Satellite Antenna Systems Using an Autonomous Vehicle Swarm |
| Ruifan Liu | PhD (2023) |  | Decentralized Mission Planning for Multiple Unmanned Aerial Vehicles |
| On Park | PhD (2023) |  | Trajectory Optimization With Sparse Gauss-Hermite Quadrature |
| Shuoyuan Xu | PhD (2022) |  | Multi-sensor and multi-target tracking |
| Byoungju Jeon | PhD (2021) |  | Extreme learning to aerospace big data |
| Zsomber Öreg | PhD (2021) |  | Cyber-physical resilience of cooperating autonomous systems |
| Teng Li | PhD (2021) |  | Decision making for multi-agent systems |
| Serena Iovino | PhD (2021) |  | Development, implementation and testing of an advanced guidance law for USVs |
| Dewi Habsari Budiarti | PhD (2020) |  | Adaptive flight control system |
| Shaoming He | PhD (2020) | Professor at Beijing Institute of Technology | Multiple target tracking |
| Charles Philippe | PhD (2020) |  | Task allocation and sequencing for multi-agent system |
| Sangjun Bae | PhD (2019) | Currently Assistant Professor at Sejong Cyber University | Trajectory optimisation |
| Hae-In Lee | PhD (2019) | Currently Lecturer at Cranfield University | Network management for multiple UAVs |
| Inmo Jang | PhD (2019) | Currently Assistant Professor at Korea Aerospace University | Task allocation for multi-agent systems |
| Dario Turchi | PhD (2018) |  | Behaviour monitoring |
| Pau Segui Gasco | PhD (2018) | Currently Assistant Professor at Universitat Politècnica de València | UAV cooperation improvement |
| Chang How Lo | PhD (2016) |  | Fault tolerant guidance and control |
| Francis Salama | PhD (2015) |  | Multi-objective control allocation |
| Cedric Leboucher | PhD (2015) |  | Weapon target assignment |
| Geunwoo Lee | MSc (2026) |  | Shaping-Filter Augmented Constrained EKF for Equivalent Conicity Estimation of Railway Vehicles |
| Mansoor Almansoori | MSc (2023) |  | Decision making for low-speed interceptors |
| Rajesh Sankaran | MSc (2023) |  | Design of a precision landing control algorithm for a PX4-based multirotor UAV using IR beacon in a GPS-denied environment |
| Yuyao Yang | MSc (2023) |  | Data fusion versus data integration |
| Aref Michael Bitar | MSc (2023) |  | Air traffic sensor data fusion |
| Tarik Tajmilur Khemlani | MSc (2022) |  | Autonomous Obstacle Detection during Landing Operations |
| Maheedhar Korimi | MSc (2022) |  | Deep Learning for Safety Critical Control |
| Mo Tianyu | MSc (2022) |  | Deep Learning Tracking and Prediction |
| Aroun Settouraman | MSc (2022) |  | Forced Landing Flight Path Planning Tool |
| Shima Maleki | MSc (2022) |  | ML in UAV detection and tracking |
| Anthony Juhel | MSc (2022) |  | Optimising swarm searches |
| Guillermo Villalobos | MSc (2022) |  | Precision Positioning |
| Shihab Hannan | MSc (2022) |  | Route and track of UAVs |
| Antoine Wamster | MSc (2022) |  | Taxiway Centerline Tracking |
| Siddharth Singh | MSc (2022) |  | UAV detection and classification |
| Alejandra Martinez Farina | MSc (2021) |  | Drone Teaming |
| Louy Barnawi | MSc (2021) |  | Optimising C-UAS countermeasures for use against swarming UAS threat |
| Huai-Che Chou | MSc (2021) |  | Sensor fusion and signal filtering of noisy / biased (e.g. multipath) signals for PNT |
| David Romero Chamorro | MSc (2020) |  | Automated Contingency and Emergency RPAS Operations |
| Sai Praneeth Sunkesula | MSc (2020) |  | Multiple Drone Teaming |
| Enver Bildik | MSc (2020) |  | Persistent Decoys |
| Romain Guy Delabeye | MSc (2020) |  | Target localisation |
| Simon Van Den Heuvel | MSc (2019) |  | Advance flight control design for EVTOL air taxi concept, supported by Rolls Royce |
| Markos Lopez Roso | MSc (2019) |  | Advance flight control design for VOLANTE Personal Air Vehicle concept |
| Wai Keong Choo | MSc (2019) |  | Detect and avoid for autonomous aircraft |
| Vinorth Varatharasan | MSc (2019) | BAE Systems |  |
| Chengkai Wu | MSc (2019) |  | Predicting drone flight patterns |
| Johannes Autenrieb | MSc (2019) |  | UAV to detect anomalies using machine intelligence |
| Matthew Perks | MSc (2018) |  | Rough Diamond |
| Itxaso Diaz Perez | MSc (2018) |  | Swarm Drone Sensors |
| Olatz Diaz Perez | MSc (2018) |  | Visual Cue based (Vehicle to vehicle) cooperative positioning |
| Zsomber Oreg | MSc (2017) |  | Adaptive Flight Control |
| Cristina MacHado | MSc (2017) |  | Drone swarm centralised control |
| Jiankun Ding | MSc (2017) |  | Drone swarm distributed control |
| Elene Fernandez Mardones | MSc (2017) |  | Multiple drone control |
| Pablo Dona Giron | MSc (2017) |  | Objective focussed UAV control |
| Rafael Martinez Silva | MSc (2017) |  | Optimal path planning for a racing car in a racing circuit |
| Clement Imbert | MSc (2016) |  | UAV smart systems for autonomous UAV flying in Antarctica |
| Alvaro Rodriguez | MSc (2016) |  | Adaptive Flight Control |
| Benjamin Semal | MSc (2016) |  | UAV Swarms |
| Emmanuel Doucet | MSc (2016) |  | A study of hybrid geolocation solutions for automated road vehicles |
| Oscar Gonzalez | MSc (2016) |  | Objective focussed UAV control |
| Zarudzki Mateusz | MSc (2016) |  | Multiple targets tracking of an quad-tilt rotor UAV - image based visual servoing approach ﻿ |
| Luis Contreras | MSc (2016) |  | Learning-6Dof flight control |
| Dawid Machala | MSc (2016) |  | Guidance & Control Design for a Long Range Projectile |
| Maria Morante | MSc (2016) |  | Countering Improvised Cruise Missiles (CICM) |
| Pierre Bauerle | MSc (2015) |  | Autonomous Operation in Un-segregated Airspace/Guidance - Outer Loop Control Laws |
| Nicholas Picon | MSc (2015) |  | Autonomous Operation in Un-segregated Airspace/Guidance - Decision Making |
| Florian Cabaret | MSc (2015) |  | Three-axis Homing Guidance |
| Miguel Encinas | MSc (2015) |  | UAV Sensor Mix |
| Chiara Gei | MSc (2015) |  | UAV Sensor Management |
| Sergio Rubio Madronal | MSc (2015) |  | Adaptive Flight Control |
| Victor Journe | MSc (2015) |  | Multiple UAV Sensor Optimization |
| Jules Humbert | MSc (2015) |  | Optimal UAV Swarm Manoeuvring to reduce SAM intercept probability |
| Quentin Vichard | MSc (2015) |  | Mothership UAV and SUAS operations |
| Robin Maheo | MSc (2015) |  | Heterogeneous Fleet Analysis |
| Robert Finger | MSc (2015) |  | Game Theory UAV Comms Management |
| Ignacio Munoz Ybarra | MSc (2015) |  | Fusion of Target Motion Analysis and Geographic Data |
| Servando German | MSc (2014) |  | UAV intelligent fleet composition |
| David Torres Ocana | MSc (2014) |  | Adaptive and fault-tolerant flight control systems |
| Ernest Lillo | MSc (2014) |  | Integrated reconfigurable control and guidance based on evaluation of degraded performance |
| Daniel Pastor | MSc (2014) |  | Visual odometry in hardware : an application to agile platforms |
| Victor Gomez Garcia | MSc (2014) |  | Visual odometry application: landing and docking controller design |
| Maria Jose Sanchez Garcia | MSc (2014) |  | Active Aircraft Fault Detection, Accommodation and Evaluation of Performance Reduction |
| Mario Ferrandiz Gomis | MSc (2014) |  | Frequency planning of networked UAVs: a game theoretical approach |
| Thomas de Corlieu | MSc (2013) |  | GPS jammer localisation from the air |
| Sahel Iskander Flores Gomez | MSc (2013) |  | Fusion of target motion analysis (TMA) and geographic data |
| Lucia Hernandez Hernandez | MSc (2013) |  | Multi-objective UAV routing |
| Marek Malinowski | MSc (2013) |  | Autonomous navigation in unknown terrain based on information matrix |
| Roberto Gorriz Vilar | MSc (2013) |  | Communication-aware path planning in urban environments |
| Borja Fortuny Lopez | MSc (2013) |  | Development of a novel variable-pitch quadrotor UAV |
| Edoardo Tome | MSc (2012) |  | Search strategy for indoor exploration and target search |
| Henoc Gimeno Simo | MSc (2012) |  | Flight data acquisition system and parameter estimation for a small glider UAV |
| Benoit Romito | MSc (2012) |  | Optimal sensing configuration for standoff tracking UAVs |
| Quentin Mauviel | MSc (2012) |  | Development and validation of a miniature air vehicle model |
| Pau Segui Gasco | MSc (2012) |  | Development of a dual axis tilt rotorcraft UAV : modelling, simulation and control |
| Yazan Al-Rihani | MSc (2012) |  | Development of a dual axis tilt rotorcraft UAV : design, prototyping and control |

## 최근 논문·저술 목록 (2021–2026)

무인 항공기의 제어·경로 계획, 여러 시스템의 임무 배분, 표적과 상태의 추정 등을 다룬다. 누리집 연도 구역 기준 학술지 논문 65편과 선별 학회 논문 51편, Books의 단행본·특집 2건과 Book Chapters의 책 장 1편을 합친 119건이다. 신효상 교수의 2024년 3월 KAIST 부임 전 Cranfield 재직 시절 항목이 함께 있다. 2021년 연도 구역은 연초 논문도 포함한다. 2026년 10월로만 적힌 항목은 일자를 덧붙이지 않고 누리집 표기를 따른다.[^journals][^conferences][^others][^prof]

학술지의 Early Access는 온라인 선게재 표기다. 학회 목록은 누리집이 선별해 게시한 목록이다. 아래 저자·제목·서지는 누리집 게시 문구이고, Books에는 특집 제목도 포함된다.[^journals][^conferences][^others]

**2026**

- S. Koo, S. Han, H.-S. Shin, "Calibration-Aware Convex Surrogate MPC for Nonlinear Joint Chance-Constrained Control via Spectral Risk Allocation", IEEE Control Systems Letters, Early Access
- F. Chen, Q. Hu, T. Han, H.-S. Shin, "Nonlinear three-dimensional constrained guidance law: An analytical higher-order shaping approach", Automatica, 192, 113170, Oct 2026
- N. Lucotte, A. Perrusquía, A. Tsourdos, W. Guo, H.-S. Shin, "Interception of adversarial drones in urban spaces using a modified deep reinforcement learning approach", Applied Soft Computing, 202, 115797, Oct 2026
- M. Mishra, S. Mishra, H.-S. Shin, ''Cross-modal distillation for real-time wildfire detection and localization in edge-deployed aerial vehicles,'' ISPRS Journal of Photogrammetry and Remote Sensing, 235, 551-564, May 2026
- L. G. L. de Paula, J. M. C. Quintero, H.-S. Shin, A.  Tsourdos, ''Visual Servoing Model Predictive Control for Autonomous Shipboard Rotorcraft Landing in High Sea States,'' Journal of Guidance, Control, and Dynamics, Jan 2026

**2025**

- T. Li, H.-S. Shin, A. Tsourdos,  "Efficient Decentralised Parallel Task Allocation for Multiple Robots", IEEE Transactions on Robotics, 41, 6006-6023, Sep. 2025
- S. Kim, M. Sun, I. Petrunin, H.-S. Shin, "DBSCAN-based particle Gaussian mixture filters", Digital Signal Processing, 105546, Aug. 2025
- S. He, H. Luo, C.-H. Lee, H.-S. Shin, A. Tsourdos, "Review of data-driven computational guidance for unmanned aerospace vehicles", Progress in Aerospace Sciences, 157, 101129, Aug. 2025
- T. Han, S. Zhang, Q. Hu, H.-S. Shin, Q. Wang, "Field-of-View Reduced Impact Angle Guidance Law via Range Shaping Approach", IEEE Transactions on Aerospace and Electronic Systems, Early Access, , Jun. 2025
- R. Chai, T. Liu, S. He, K. Chen, Y. Xia, H.-S. Shin, A. Tsourdos, "Adaptive dual-loop disturbance observer-based robust model predictive tracking control for autonomous hypersonic vehicles", IEEE/CAA Journal of Automatica Sinica, Early Access, , May. 2025
- J. Autenrieb,  H.-S. Shin, "Complementary Filter-Based Incremental Nonlinear Model Following Control Design for a Tilt-Wing UAV", International Journal of Robust and Nonlinear Control, 35(4), 1596-1615, Mar. 2025
- S. Kim, I. Petrunin, H.-S. Shin, "A review of Bayes filters with machine learning techniques and their applications", Information Fusion, 114, 102707, Feb. 2025
- S. Jang, H.-S. Shin, "Hybrid Consensus ADMM for Multi-Robot Task Allocation via a Minimum Dominating Set", In: 13th International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, 2025
- S. Koo, H.-S. Shin, "Delaunay Triangulation-based Path Planning under Collision Probability Constraints", In: 13th International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, 2025
- J. Jeong, O. Park, H.-S. Shin, "Robust Path-Following Control for a Tilt-Wing UAV Using Incremental Nonlinear Dynamic Inversion", In: 13th International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, 2025
- J. Jeong, O. Park, H.-S. Shin, "Wind Disturbances Rejection for Multirotor via an Incremental Backstepping Flight Control Method", In: KSAS 2025 Fall Conference, Gangwon, South Korea, 2025
- Q.-V. Lai-Dang, H.-S. Shin, "Two-Stage Fine-Grained Military Aircraft Recognition in Imbalanced Dataset", In: KSAS 2025 Fall Conference, Gangwon, South Korea, 2025
- J. Yang, M. Jeong, H.-S. Shin, S. Han, "RFF-Lifted Physics-Informed Koopman Network (RFF-PIKN)", In: KSAS 2025 Fall Conference, Gangwon, South Korea, 2025
- S. Singh, H.-S. Shin, L. Felicetti, A. Tsourdos, "Point cloud completion based pose estimation for spacecraft", In: 2025 11th European Conference for AeroSpace Sciences, Rome, Italy, 2025
- J. Autenrieb, H.-S. Shin, "Sensor-Based Safety-Critical Control Using an Incremental Control Barrier Function Formulation via Reduced-Order Approximate Models", In: 2025 American Control Conference (ACC), Denver, USA, 2025
- S. Kim, S. Moon, I. Petrunin, H.-S. Shin, S. Khattak, "Autonomous Robotic Radio Source Localization via a Novel Gaussian Mixture Filtering Approach", In: 2025 28th International Conference on Information Fusion (FUSION), Rio de Janeiro, Brazil, 2025
- H.-I. Lee, Q.-V. Lai-Dang, H.-W. Seok, H.-S. Shin, T. Gong, A. Mendez, R. Gojon, "Communication RSSI Prediction and Validation Framework for Advanced Air Mobility", In: 2025 International Wireless Communications and Mobile Computing (IWCMC), Abu Dhabi, UAE, 2025
- L. G. L. de Paula, V. S. Dwivedi, H.-S. Shin, A. Tsourdos, "Towards Autonomous Landing on Dynamic Naval Surfaces Under Harsh Sea State Motion", In: AIAA SCITECH 2025 Forum, Orlando, USA, 2025
- L. G. L. de Paula, V. S. Dwivedi, H.-S. Shin, A. Tsourdos, "Visual Servoing MPC Framework for Shipboard Autonomous Landing", In: 2025 AIAA AVIATION Forum and 2025 ASCEND, Las Vegas, USA, 2025

**2024**

- Y. Nam , K. Lee, H.-S. Shin, C. Kwon, "Fault tolerant motion planning for a quadrotor subject to complete rotor failure", Aerospace Science and Technology, 154, 109529, Nov. 2024
- S. Lee, H.-S. Shin, "Destination and time-series inference of moving objects via conditionally Markov process", CEAS Aeronautical Journal, 15(4), 1189-1199, Sep. 2024
- T. Jin, H.-S. Shin, A. Tsourdos, S. He, "Integrated Target Assignment and Trajectory Optimization for Many-to-Many Midcourse Guidance", IEEE Transactions on Aerospace and Electronic Systems, 61(1), 853-867, Aug. 2024
- Y. Kim, S. Kim, J. Suk, H.-S. Shin, "Robust Controller Design for UAM Using Incremental Nonlinear Dynamic Inversion With Double-Loop Structure", 61(1), 76-92, Aug. 2024
- T. Han, Q. Hu, Q. Wang, M. Xin, H.-S. Shin, "Constrained 3-D trajectory planning for aerial vehicles without range measurement", IEEE Transactions on Systems, Man, and Cybernetics: Systems, 54(10), 6001-6013, Jul 2024
- B. Cui, X. Chen, R. Chai, Y. Xia, H.-S. Shin, "Trajectory Planning of Spacecraft Swarm Reconfiguration Using Reachable Set-based Collision Constraints", IEEE Transactions on Aerospace and Electronic Systems, 60(5), 6474-6487,  Jun. 2024
- N. Cho, H.-S. Shin, A. Tsourdos, D. Amato, "Online Corrections to Neural Policy Guidance for Pinpoint Powered Descent", Journal of Guidance, Control, and Dynamics, 47(5), 945–963, May 2024
- S. Lee, Z. Yuan, I. Petrunin, H.-S. Shin, "Impact Analysis of Time Synchronization Error in Airborne Target Tracking Using a Heterogeneous Sensor Network", Drones, 8(5), 167, Apr. 2024
- R. Chai, Y. Guo, Z. Zuo, K. Chen, H.-S. Shin, A. Tsourdos, "Cooperative motion planning and control for aerial-ground autonomous systems: Methods and applications", Progress in Aerospace Sciences, 146, 101005, Apr. 2024
- S. Kim, I. Petrunin, H.-S. Shin, "AFJPDA: A Multiclass Multi-Object Tracking with Appearance Feature-Aided Joint Probabilistic Data Association", Journal of Aerospace Information Systems, 21(4), 294-304, Apr. 2024
- J. Chai, S. He, H-S Shin, A. Tsourdos, ''Domain-knowledge-aided airborne ground moving targets tracking'', Aerospace Science and Technology, 144, 108807, Jan. 2024
- N. Cho, H.-S. Shin, "A Passivity-Based Method for Accelerated Convex Optimisation", In: 2024 IEEE 63rd Conference on Decision and Control (CDC), Milan, Italy, 2024
- V.S. Dwivedi, H.-S. Shin, A. Tsourdos, "Wind Field Estimation from UAV Data Using Machine Learning", International Conference on Robot Intelligence Technology and Applications, Ulsan, South Korea, 2024
- S. Koo, H.-S. Shin, G.-Y. Jeon, "Static Weapon Target Assignment Considering Interception Damage", In: Proceedings of the 2024 Korea Society for Simulation Conference, Seoul, South Korea, 2024
- R. Liu, H.-S. Shin, A. Tsourdos, "Cross-Observability Learning for Vehicle Routing Problems", In: 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Abu Dhabi, UAE, 2024
- N. Cho, Y. Min, H.-S. Shin, N. Azizan, "Π-ORFit: One-Pass Learning with Bregman Projection", In: 2024 American Control Conference (ACC), Toronto, Canada, 2024
- J. Kim, M. Jung, H.-S. Shin, H. Oh, A. Tsourdos, "Deep Reinforcement Learning-Based Neighbor Selection of a Cucker-Smale Flocking Algorithm", In: 2024 10th International Conference on Control, Decision and Information Technologies (CoDIT), Valetta, Malta, 2024
- T. Jin, S. He, H.-S. Shin, "Distributed Neighborhood Search Algorithm for Target Assignment", In: 2024 European Control Conference (ECC), Stockholm, Sweden, 2024
- N. Cho, T. Lee, H.-S. Shin, "Recursive Least Squares with Log-Determinant Divergence Regularisation for Online Inertia Identification", In: 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 2024
- H.-I. Lee, D. Ignatyev, H.-S. Shin, A. Tsourdos, "Project-Based Learning Course Design for Multi-Agent Autonomy Using Quadrotors", In: 2024 Workshop on Aerospace Control Education (WACE), Bertinoro, Italy, 2024
- B. Ince, H.-S. Shin, A. Tsourdos, "Adversarial Proximal Policy Optimisation for Robust Reinforcement Learning", In: AIAA SCITECH 2024 Forum, Orlando, USA, 2024
- O. Park, H.-S. Shin, "Dynamics Modeling of Multirotor type UAV with the Blade Element Momentum Theory and Nonlinear Controller Design for a Wind Environment", In: AIAA SCITECH 2024 Forum, Orlando, USA, 2024
- V. Celdran Martinez, H.-S. Shin, A. Tsourdos, "Risk Assessment for sUAS in Urban Environments: A Comprehensive Analysis, Modelling and Validation for Safe Operations", In: AIAA SCITECH 2024 Forum, Orlando, USA, 2024
- A. L'Afflitto, G. Inalhan, H-S Shin. Control of Autonomous Aerial Vehicles, Springer, Cham, India, 2024

**2023**

- S. Lee, H-S Shin, A. Tsourdos, ''Intent-Informed State Estimation for Tracking Guided Targets'', Aerospace Science and Technology, 143, 108713, Dec. 2023
- J. Chai, S. He, H-S Shin, A. Tsourdos, ''Dynamic Knowledge-Based Tracking and Autonomous Anomaly Detection'', IEEE Transactions on Aerospace and Electronic Systems, 60(2), 1597-1611, Nov. 2023
- G. M. Skaltsis, H-S Shin, A. Tsourdos, ''A Review of Task Allocation Methods for UAVs'', Journal of Intelligent & Robotic Systems, 109(4), 76, Nov. 2023
- T. Kim, S. Kim, H-S Shin, ''Data-Driven Diagnosis of Multicopter Thrust Fault Using Supervised Learning with Inertial Sensors'', Journal of Aerospace Information Systems, 20(11), 60-701, Nov. 2023
- L. Hou, H. Luo, H. Shi, H-S Shin, S. He, ''An Optimal Geometrical Guidance Law for Impact Time and Angle Control'', IEEE Transactions on Aerospace and Electronic Systems, 59(6), 9821-9830, Aug. 2023
- Z. Oreg, H-S Shin, A. Tsourdos, ''Analysis of the traffic conflict situation for speed probability distributions'', The Aeronautical Journal, 127(1314), 1380-1434, Aug. 2023
- X. Yang, H. Yin, S. He, Y. Xie, H-S Shin, ''Trajectory Optimization for Multi-Sensor Multi-Target Search and Tracking with Bearing-Only Measurements'', Aerospace, 10(7), 652, Jul. 2023
- D. I. Ignatyev, H-S Shin, A. Tsourdos, ''Sparse online Gaussian process adaptation for incremental backstepping flight control'', Aerospace Science and Technology, 136, 108157, May 2023
- R. Liu, H-S Shin, A. Tsourdos, ''Edge-Enhanced Attentions for Drone Delivery in Presence of Winds and Recharging Stations'', Journal of Aerospace Information Systems, 20(4), 216-228, Apr. 2023
- X. Zheng, H. Guan, D. Lin, S. He, H-S Shin, ''Game-Theoretic Flexible-Final-Time Differential Dynamic Programming Using Gaussian Quadrature'', Journal of Guidance, Control, and Dynamics, 46(4), 742-751, Apr. 2023
- Z. Oreg, H-S Shin, A. Tsourdos, ''On the underlying dynamics of traffic conflicts related to stochastic behaviour'', IMechE Part G: Journal of Aerospace Engineering, 237(5), 1078-1093, Apr. 2023
- Y. Song, H. Lee, C. Kwon, H-S Shin, H. Oh, ''Distributed Estimation of Stochastic Multiagent Systems for Cooperative Control With a Virtual Network'', IEEE Transactions on Systems, Man, and Cybernetics, 53(4), 2350-2362, Apr. 2023
- N. Cho, S. Lee, H-S Shin, T-H Kim, ''Three-Dimensional Biased Proportional Navigation Guidance Based on Spatial Rotation of Predicted Final Velocity'', IEEE Transactions on Aerospace and Electronic Systems, 59(2), 1354-1370, Apr. 2023
- S. Bae, H-S Shin, A. Tsourdos, ''Structured Urban Airspace Capacity Analysis: Four Drone Delivery Cases'', Applied Sciences, 13(6), 3833, Mar. 2023
- T. Kim, H. Jeaong, S. Kim, I. Kim, S. Kim, J. Suk, H-S Shin, ''Design and Flight Testing of the Ducted-fan UAV Flight Array System'', Journal of Intelligent & Robotic Systems, 107(3), 32, Mar. 2023
- N. Cho, H.-S. Shin, Y. Kim, A. Tsourdos, "Composite Model Reference Adaptive Control under Finite Excitation with Unstructured Uncertainties", In: 2023 62nd IEEE Conference on Decision and Control (CDC), Marina Bay, Singapore, 2023
- J. Yun, H-S Shin, A. Tsourdos. ''Perimeter Intrusion Prediction Method Using Trajectory Frequency and Naive Bayes Classifier'' In: 2023 23rd International Conference on Control, Automation and Systems (ICCAS), Yeosu, South Korea, 2023
- S. He, H-S Shin, A. Tsourdos. ''Target Identity Probability Analysis for Multi-Target Tracking'' In: 2023 35th Chinese Control and Decision Conference (CCDC), Yichang, China, 2023
- R. Liu, H-S Shin, A. Tsourdos. ''Mission Planning for a Multiple-UAV Patrol System in an Obstructed Airport Environment'' In: DASC 2023, Barcelona, Spain, 2023
- G. E. Villalobos Hernandez, I. Petrunin, H-S Shin, J. Gilmour. ''Robust Multi-Sensor Navigation in GNSS Degraded Environments'' In: AIAA SCITECH 2023 Forum, Orlando, USA, 2023
- B. Ince, H-S Shin, A. Tsourdos. ''Optimization of a Robust Reinforcement Learning Policy'' In: AIAA SCITECH 2023 Forum, Orlando, USA, 2023
- S. Bertrand, H-S Shin. Special Issue on Unmanned Aerial Vehicles, Applied Sciences (Switzerland), 2023

**2022**

- J. Choi, M-G Seo, H-S Shin, H. Oh, ''Adversarial Swarm Defence Using Multiple Fixed-Wing Unmanned Aerial Vehicles'', IEEE Transactions on Aerospace and Electronic Systems, 58(6), 5204-5219, Dec. 2022
- H-I Lee, H-S Shin, A. Tsourdos, ''A Probabilistic–Geometric Approach for UAV Detection and Avoidance Systems'', Sensors, 22(23), 9230, Nov. 2022
- N. Cho, J. Park, Y. Kim, H-S Shin, ''Unified Control Parametrisation Approach for Finite-Horizon Feedback Control with Trajectory Shaping'', IEEE Transactions on Aerospace and Electronic Systems, 58(5), 4782-4795, Oct. 2022
- T. Han, H-S Shin, Q. Hu, A. Tsourdos, M. Xin, ''Differentiator-Based Incremental Three-Dimensional Terminal Angle Guidance With Enhanced Robustness'', IEEE Transactions on Aerospace and Electronic Systems, 58(5), 4020-4032, Oct. 2022
- X. Yang, S. He, H-S Shin, A. Tsourdos, ''Trajectory Optimization for Target Localization and Sensor Bias Calibration with Bearing-Only Information'', Guidance, Navigation and Control, 2(2), 2250015, Sep. 2022
- H-S Shin, T. Li, H-I Lee, A. Tsourdos, ''Sample greedy based task allocation for multiple robot systems'', Swarm Intelligence, 16, 233-260, Aug. 2022
- K. B. Li, Z. H. Bai, H-S Shin, A. Tsourdos, M-J Tahk, ''Capturability of 3D RTPN guidance law against true-arbitrarily maneuvering target with maneuverability limitation'', Chinese Journal of Aeronautics, 35(7), 75-90, Jul. 2022
- Z. Oreg, H-S Shin, A. Tsourdos, ''Traffic conflict reduction based on distributed stochastic task allocation'', The Aeronautical Journal, 126(1300), 993-1025, Jun. 2022
- V. Lappas, H-S Shin, A. Tsourdos, D. Lindgren, S. Bertrand, J. Marzat, H. Piet-Lahanier, Y. Daramouskas, V. Kostopoulos, ''Autonomous Unmanned Heterogeneous Vehicles for Persistent Monitoring'', Drones, 6(4), 94, Apr. 2022
- S. Lee, N. Cho, H-S Shin, ''Analysis of Guidance Laws with Non-monotonic Line-of-Sight Rate Convergence'', IEEE Transactions on Aerospace and Electronic Systems, 58(2), 1029-1041, Apr. 2022
- V. Lappas, G. Zoumponos, V. Kostopoulos, H-I Lee, H-S Shin, A. Tsourdos, M. Tantardini, D. Shomko, J. Munoz, E. Amoratis, A. Maragkakis, ''EuroDRONE, a European Unmanned Traffic Management Testbed for U-Space'', Drones, 6(2), 53, Feb. 2022
- T. Han, Q. Hu, H-S Shin, A. Tsourdos, M. Xin, ''Incremental Twisting Fault Tolerant Control for Hypersonic Vehicles With Partial Model Knowledge'', IEEE Transactions on Industrial Informatics, 18(2), 1050-1060, Feb. 2022
- T. R. Tajmilur Khemlani, Y. Xing, H-S Shin. ''Development and Feasibility Study of an Autonomous Obstacle Detection System for Landing Operations'' In: International Conference on Robot Intelligence Technology and Applications, Gold Coast, Australia, 2022
- S. Lee, H-S Shin. ''Destination and time-series inference of moving objects using conditionally markov sequences'' In: CEAS EuroGNC 2022, Berlin, Germany, 2022
- R. Liu, H-S Shin, M. Seo, A. Tsourdos. ''Energy-aware Route Planning for Drone Delivery Systems'' In: CEAS EuroGNC 2022, Berlin, Germany, 2022
- N. Cho, Y. Kim, H-S Shin, Y. Kim. ''Guidance of Gliding Vehicles with Energy Management Based on Approximate Prediction of Speed'' In: CEAS EuroGNC 2022, Berlin, Germany, 2022
- S. Kim, I. Petrunin, H-S Shin. ''A Review of Kalman Filter with Artificial Intelligence Techniques'' In: 2022 Integrated Communication,  Navigation and Surveillance Conference (ICNS) 2022, Virginia, USA, 2022
- S. Omi, H-S Shin, A. Tsourdos, J. Espeland, A. Buchi. ''Multi-beam Tracking for Phased Array Antenna Measurement by multiple UAVs'' In: 2022 16th European Conference on Antennas and Propagation (EuCAP), Madrid, Spain, 2022
- R. Liu, H-S Shin, M. Seo, A. Tsourdos. ''Delivery Route Planning for Unmanned Aerial System in Presence of Recharging Stations'' In: AIAA AVIATION 2022 Forum, Chicago, USA, 2022
- G. M. Skaltsis, H-S Shin, A. Tsourdos. ''Self play with parameter sharing in n-player mixed competitive-cooperative games'' In: AIAA SCITECH 2022 Forum, San Diego, USA, 2022
- D. Ignatyev, H-S Shin, A. Tsourdos. ''Gaussian Process Adaptive Incremental Backstepping Flight Control'' In: AIAA SCITECH 2022 Forum, San Diego, USA, 2022
- H. Li, S. He, J. Wang, H-S Shin, A. Tsourdos. ''Three-Dimensional Nonlinear Optimal Guidance against Maneuvering Target with Large Initial Heading Error'' In: AIAA SCITECH 2022 Forum, San Diego, USA, 2022
- K. B. Li, Z. H. Bai, H-S Shin, A. Tsourdos, M-J Tahk. Capturability of 3D RTPN Against True-Arbitrarily Maneuvering Target with Maneuverability Limitation, Advances in Guidance, Navigation and Control, Yan L., Duan H., Yu X. (eds), Springer Singapore, pp.4511-4528, 2022.

**2021**

- Z. Liu, J. Wang, S. He, H-S Shin, A. Tsourdos, ''Learning prediction-correction guidance for impact time control'', Aerospace Science and Technology, 119, 107187, Dec. 2021
- Y. Wang, J. Wang, S. He, H-S Shin, A. Tsourdos, ''Optimal Guidance with Active Observability Enhancement for Scale Factor Error Estimation of Strapdown Seeker'', IEEE Transactions on Aerospace and Electronic Systems, 57(6), 4347-4362, Dec. 2021
- T. Han, Q. Hu, H-S Shin, A. Tsourdos, ''Sensor-Based Robust Incremental Three-Dimensional Guidance Law with Terminal Angle Constraint'', Journal of Guidance, Control, and Dynamics, 44(11), 2016-2030, Nov. 2021
- Y. Song, M. Gu, J. Choi, H. Oh, S.L im, H-S Shin, A.Tsourdos, ''Using Lazy Agents to Improve the Flocking Efficiency of Multiple UAVs'', Journal of Intelligent & Robotic Systems, 103(53), 1-17, Oct. 2021
- H-S Shin, K-B Li, ''An Improvement in Three-Dimensional Pure Proportional Navigation Guidance'', IEEE Transactions on Aerospace and Electronic Systems, 57(5), 3004-3014, Oct. 2021
- S. He, H-S Shin, A. Tsourdos, ''Computational Missile Guidance: A Deep Reinforcement Learning Approach'', Journal of Aerospace Information Systems, 18(8), 571-582, Aug. 2021
- L. Zhang, T. Zhang, H-S Shin, ''An Efficient Constrained Weighted Least Squares Method with Bias Reduction for TDOA-Based Localization'', IEEE Sensors Journal, 21(8), 10122-10131, Apr. 2021
- S. He, H-S Shin, A. Tsourdos, ''Information-Theoretic Joint Probabilistic Data Association Filter'', IEEE Transactions on Automatic Control, 66(3), 1262-1269, Mar. 2021
- C. Hu, G. Qu, H-S Shin, A. Tsourdos, ''Distributed synchronous cooperative tracking algorithm for ground moving target in urban by UAVs'', International Journal of Systems Science, 52(4), 832-847, Mar. 2021
- T. Li, H-S Shin, A. Tsourdos, ''A sample decreasing threshold greedy-based algorithm for big data summarisation'', Journal of Big Data, 8(30), 1-21, Feb. 2021
- M-G Seo, H-S Shin, A. Tsourdos, ''Soil Moisture Retrieval Model Design with Multispectral and Infrared Images from Unmanned Aerial Vehicles Using Convolutional Neural Network'', Agronomy, 11(2), 398, Feb. 2021
- B-J Jeon, M-G Seo, H-S Shin, A. Tsourdos, ''Understandings of incremental backstepping controller considering measurement delay with model uncertainty'', Aerospace Science and Technology, 109, 106408, Feb. 2021
- C. Hu, Z. Meng, G. Qu, H-S Shin, A. Tsourdos, ''Distributed Cooperative Path Planning for Tracking Ground Moving Target by Multiple Fixed-Wing UAVs via DMPC-GVD in Urban Environment'', International Journal of Control, Automation and Systems, 19, 823-836, Feb. 2021
- S. He, C-H Lee, H-S Shin, A. Tsourdos, ''Optimal Three-Dimensional Impact Time Guidance with Seeker’s Field-of-View Constraint'', Chinese Journal of Aeronautics, 34(2), 240-251, Feb 2021
- H. Li, S. He, J. Wang, H-S Shin, A. Tsourdos, ''Near-Optimal Midcourse Guidance for Velocity Maximization with Constrained Arrival Angle'', Journal of Guidance, Control, and Dynamics, 44(1), 172-180, Jan. 2021
- D. Ignatyev, H-S Shin, A. Zolotas, A. Tsourdos. ''Group Design Project in Control Engineering: Adapting to COVID-19 Pandemic'' In: 2021 Workshop on Aerospace Control Education (WACE), Milano, Italy, 2021
- S. Omi, H-S Shin, A. Tsourdos, J. Espeland, A. Buchi. ''Reinforcement Learning System of UAV for Antenna Beam Localization'' In: 2021 IEEE Conference on Antenna Measurements & Applications (CAMA), Antibes Juan-les-Pins, France, 2021
- O. Park, H-S Shin, H-I Lee, A. Tsourdos. ''Optimal and Adaptive Control Design Using Recursive Least Square with a New Exponential Forgetting Factor'' In: 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, South Korea, 2021
- M. Jung, H. Oh, H-S Shin. ''Heterogeneous Mission Planning of UAVs with Attention-Based Deep Reinforcement Learning'' In: 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, South Korea, 2021
- R. Delabeye, H-S Shin, G. Inalhan. ''Feature-Aided SMC-PHD filter for nonlinear multi-target tracking in cluttered environments'' In: 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, South Korea, 2021
- G. Kim, O. Park, S. Kim, H-S Shin. ''Application of Reinforcement Learning to UAV Guidance'' In: Asia-Pacific International Symposium on Aerospace Technology (APISAT), Jeju, South Korea, 2021
- S. Omi, H-S Shin, A. Tsourdos, J. Espeland, A. Buchi. ''Stochastic Filtering Technique for UAV-Based Communications On The Move Terminal Tracking Accuracy Evaluation'' In: 2021 Antenna Measurement Techniques Association Symposium (AMTA), Florida, USA, 2021
- S. He, H-S Shin, M. Qi, A. Tsourdos. ''Distributed Three-Dimensional Pseudo Measurement Kalman Filter with Angle-Only Measurements'' In: 2021 European Control Conference (ECC), Delft, Netherlands, 2021
- G. M. Skaltsis, H-S Shin, A. Tsourdos. ''A survey of task allocation techniques in MAS'' In: 2021 International Conference on Unmanned Aircraft Systems (ICUAS), Athens, Greece, 2021
- M. Osborne, H-S Shin, A. Tsourdos. ''A Review of Safe Online Learning for Nonlinear Control Systems'' In: 2021 International Conference on Unmanned Aircraft Systems (ICUAS), Athens, Greece, 2021
- S. Omi, H-S Shin, A. Tsourdos, J. Espeland, A. Buchi. ''Introduction to UAV swarm utilization for communication on the move terminals tracking evaluation with reinforcement learning technique'' In: 15th European Conference on Antennas and Propagation (EuCAP), Dusseldorf, Germany, 2021

## 연구 과제

2021년 10월 13일–2026년 10월 13일과 기간이 겹치는 과제 21건이다. Current Projects 5건과 Completed Projects 16건으로, 진행·완료 구분은 누리집 구획이다. 연도만 적힌 기간은 연도만 옮겼으며, 종료가 2027년 이후인 항목도 그 기간 그대로다. 신효상 교수의 KAIST 부임 전 Cranfield 재직 시절 과제가 함께 있다. PI·co-I 표기는 각각 연구책임자·공동연구자 역할 표기다.[^projects][^prof]

- Development of Risk-based Prediction and Assessment Technology for Safe UAS Flight in Urban Areas (기간 Apr. 2025-Dec. 2029; 지원 KAIA; 역할 co-I; 상태 Current Projects; 분야 Systems & Control)
- Research on autonomous eVTOL core convergence technology for urban air mobility (UAM) (기간 Mar. 2025-Dec.2031; 지원 IITP; 역할 co-I; 상태 Current Projects; 분야 Systems & Control)
- Sensor Fusion and Autonomous Mission Planning for Manned-Unmanned Teaming (기간 May. 2024-Nov. 2028; 지원 KRIT; 역할 PI; 상태 Current Projects; 분야 Information-Driven Approaches)
- Urban Air Mobility Specialist Training Program (기간 Mar. 2024-Mar. 2027; 지원 KIAT; 역할 co-I; 상태 Current Projects; 분야 Others)
- AI-Transformed Aerospace Research Center (기간 Jul.2025-Dec.2029; 지원 Ministry of Science and ICT; 역할 co-I; 상태 Current Projects; 분야 Others)
- Precision Guidance and Navigation for Deep Space Exploration (기간 2022-2027; 지원 Inha University; 상태 Completed Projects; 분야 Systems & Control)
- Knowledge transfer partnerships (KTP) (기간 2022-2024; 지원 Innovate UK; 상태 Completed Projects; 분야 Systems & Control)
- Control Allocation Algorithms (기간 2022-2022; 지원 BAE Systems; 상태 Completed Projects; 분야 Systems & Control)
- Last Mile Delivery of non-GNSS resilient time, frequency and synchronisation (TFS) (기간 2021-2022; 지원 Innovate UK; 상태 Completed Projects; 분야 Systems & Control)
- Sensor Synchronisation for CUAS and UTM applications (기간 2021-2022; 지원 Innovate UK; 상태 Completed Projects; 분야 Systems & Control)
- Development of Seamless Information Sharing Platform and Operation Technologies for Multiple Heterogeneous Mobile Systems in Maritime Search and Accident Investigation (기간 2024-2024; 지원 NRF; 상태 Completed Projects; 분야 Multi-Agent System)
- A Study on Operation Procedure of UAM/AAM Take-Off/Landing at Vertiport Adjacent to Airport (기간 2023-2023; 지원 IAIAC; 상태 Completed Projects; 분야 Multi-Agent System)
- Project BLUEPRINT - Developing a Blueprint for Scalable UTM-Enabled BVLOS Drone Operations Across the UK (기간 2022-2024; 지원 Innovate UK; 상태 Completed Projects; 분야 Multi-Agent System)
- Project HADO - High intensity Autonomous Drone Operations project (기간 2022-2024; 지원 Innovate UK; 상태 Completed Projects; 분야 Multi-Agent System)
- Project SafeZone Phase 3 (기간 2022-2024; 지원 Innovate UK; 상태 Completed Projects; 분야 Multi-Agent System)
- Technical Study on Human Swarm Teaming (기간 2022-2022; 지원 Qinetiq; 상태 Completed Projects; 분야 Multi-Agent System)
- Human Factors in Robotic and Autonomous Systems: an interdisciplinary analysis of the current state of the art for military applications (기간 2021-2022; 지원 DSTL; 상태 Completed Projects; 분야 Multi-Agent System)
- Advanced air mobility: Communication Evaluation for Safe and Seamless operations (기간 2024-2025; 지원 KAIA; 상태 Completed Projects; 분야 Information-Driven Approaches)
- LANDOne - Towards Artificial Intelligence Enabled Landing Gear with Trustworthy Autonomy (기간 2023-2026; 지원 ATI; 상태 Completed Projects; 분야 Information-Driven Approaches)
- Adaptive flight control to enhance survivability & availability (기간 2019-2022; 지원 BAE Systems; 상태 Completed Projects; 분야 Information-Driven Approaches)
- Real-time Decision Making for Autonomous Systems (기간 2019-2022; 지원 US Air Force; 상태 Completed Projects; 분야 Information-Driven Approaches)

## 수상과 선정

2022–2025년 수상·선정 5건이다. 교수 소개의 2022년 항목 3건과 소식의 수상 글 2건이다. 2022년 항목은 신효상 교수의 KAIST 부임 전 경력이다. ICNS의 Best Student Paper Award는 교수 소개에 기재된 수상 항목이다.[^prof][^news24][^news25]

- 2025년 12월 11일 · Sejin Jang 박사과정이 RiTA 2025 Best Student Paper Award를 받았다.
- 2024년 12월 11일 · 신효상 교수가 KAIST Global Research Collaboration Award를 받았다.
- 2022 · 신효상 교수의 Jeong Hun Cho Academic Award, KAIST
- 2022 · 신효상 교수의 Excellent Reviewer, Journal of Guidance, Control, and Dynamics
- 2022 · 신효상 교수 소개에 기재된 Best Student Paper Award, Integrated Communication, Navigation & Surveillance Conference

## 소식

2024년 3월–2026년 7월 연구실 개소·학술대회 참가·초청 세미나 22건이다. News 세 쪽의 해당 글 14건과 Seminars에 별도로 실린 행사 8건을 모았다. 외부 연사의 세미나 주제는 초청 행사 내용이다.[^news24][^news25][^news26][^seminars]

- 2026년 4월 3일 · 연구실 구성원이 한국항공우주학회 2026 춘계학술대회에 참가했다.
- 2026년 2월 11일 · 연구실 구성원이 2026 항공우주 유도·항법·제어 심포지엄에 참가했다.
- 2025년 7월 14일 · Hojin Lee(UNIST) 초청 세미나를 열었다.
- 2025년 7월 4일 · 연구실 구성원이 Avionics Systems Symposium Korea 2025에 참가했다.
- 2025년 7월 7일 · Namhoon Cho(Cranfield University) 교수 초청 세미나를 열었다.
- 2025년 6월 4일 · Inseok Hwang(Purdue University) 교수 초청 세미나를 열었다.
- 2025년 5월 29일 · Jin Gyu Lee(서울대학교) 교수 초청 세미나를 열었다.
- 2025년 3월 19일 · Jongyun Kim(University of Manchester) 박사 초청 세미나를 열었다.
- 2025년 2월 12–14일 · Hangju Cho 박사 초청 세미나를 열었다.
- 2025년 2월 5–7일 · 연구실 구성원이 2025 항공우주 유도·항법·제어 심포지엄에 참가했다.
- 2025년 1월 10일 · Inmo Jang(Korea Aerospace University) 교수 초청 세미나를 열었다.
- 2025년 1월 8일 · Namhoon Cho(Cranfield University) 교수 초청 세미나를 열었다.
- 2024년 12월 9일 · Mirko Kovac(Imperial College London·EPFL) 교수 초청 세미나를 열었다.
- 2024년 3월 1일 · KAIST 조천식모빌리티대학원에서 AIS Lab이 문을 열었다.
- 2026-07-14 · Ivan Petrunin(Cranfield University) 교수 초청 세미나: 측위·항법·시각 정보의 신뢰성과 인공지능 활용.
- 2026-06-11 · Hiroyasu Tsukamoto(University of Illinois Urbana-Champaign) 교수 초청 세미나: 비선형 시스템의 지능형 제어를 위한 수축 이론.
- 2026-06-05 · Doo-Hyun Cho(D.Notitia) 박사 초청 세미나: 생성형 인공지능을 활용한 연구개발 생산성 향상.
- 2026-05-21 · Daehyung Park(KAIST) 교수 초청 세미나: 정밀하고 제약 조건을 고려하는 로봇 행동.
- 2026-05-14 · Dae-Sung Jang(Korea Aerospace University) 교수 초청 세미나: 미래 항공 모빌리티의 자율성.
- 2025-10-16 · Beomjun Choi(KAIST) 교수 초청 세미나: 변분법·편미분방정식과 기하학을 통한 최적화.
- 2025-09-25 · Sungwoo Hong(KAIST) 교수 초청 세미나: 입자물리학을 통한 우주 탐구.
- 2025-09-11 · Seunghan Lim(Korea Conformity Laboratories) 초청 세미나: 공학자의 역할과 기술의 산업화.

## 연락과 위치

- 교수 이메일: hyosangshin@kaist.ac.kr[^dept]
- 교수연구실: KAIST 문지캠퍼스 F438[^prof][^dept]
- 주소: 대전광역시 유성구 문지로 193, KAIST F438, 우편번호 34051[^contact]
- 전화: +82 (0)42-350-1761[^contact]
[^dept]: KAIST 조천식모빌리티대학원 교수 목록. <https://mo.kaist.ac.kr/professor/> 신효상 교수, Cranfield University 박사 2011년, F438, 학교 이메일. 관측 2026-10-27.
[^prof]: 연구실 Professor. <https://sites.google.com/view/kaist-ais/people/professor> 학력·경력·연구 관심·학술 활동·수상. 관측 2026-10-26.
[^vision]: 연구실 Research Vision. <https://sites.google.com/view/kaist-ais/research/research-vision> 복잡한 환경의 무인·자율 시스템 운용, 여러 무인 시스템의 협력, 정보 기반 접근을 연구 비전으로 적는다. 관측 2026-10-26.
[^control]: 연구실 Systems & Control. <https://sites.google.com/view/kaist-ais/research/systems-control> 알고리즘에 초점을 두고 planning, acting, perception을 연구 범위로 적는다. 관측 2026-10-26.
[^multi]: 연구실 Multi-Agent System. <https://sites.google.com/view/kaist-ais/research/multi-agent-system> 다중 에이전트의 협력 의사결정을 수학적 최적화와 수치적 방법으로 설계·분석한다고 설명한다. 관측 2026-10-26.
[^info]: 연구실 Information-Driven Approaches. <https://sites.google.com/view/kaist-ais/research/information-driven-approaches> 인공지능·대규모 자료의 활용과 고장을 견디는 시스템의 이론·실험 연구를 소개한다. 관측 2026-10-26.
[^members]: 연구실 Members. <https://sites.google.com/view/kaist-ais/people/members> Postdoc·Ph.D. Student·M.S. Student·Visiting Student·Undergraduate Student 명단. 관측 2026-10-26.
[^alumni]: 연구실 Alumni. <https://sites.google.com/view/kaist-ais/people/alumni> 이전 Research Fellow, PhD 졸업생, MSc 졸업생 목록. 관측 2026-10-26.
[^journals]: 연구실 Journal Articles. <https://sites.google.com/view/kaist-ais/publication/journal-articles> Journal Papers의 연도 구역과 게시 서지. 관측 2026-10-26.
[^conferences]: 연구실 Conference Papers. <https://sites.google.com/view/kaist-ais/publication/conference-papers> Selected Conference Papers의 연도 구역과 게시 서지. 관측 2026-10-26.
[^others]: 연구실 Others. <https://sites.google.com/view/kaist-ais/publication/others> Books·Book Chapters·Patents 구획. 관측 2026-10-26.
[^projects]: 연구실 Projects. <https://sites.google.com/view/kaist-ais/research/projects> Current Projects·Completed Projects의 분야별 목록, 지원기관·기간·역할. 관측 2026-10-26.
[^lectures]: 연구실 Lectures. <https://sites.google.com/view/kaist-ais/teaching/lectures> MO869 센서 융합 및 다중 에이전트 최적화 강의 소개. 관측 2026-10-26.
[^seminars]: 연구실 Seminars. <https://sites.google.com/view/kaist-ais/teaching/seminars> 초청 세미나의 연사·주제·날짜. 관측 2026-10-26.
[^news26]: 연구실 News. <https://sites.google.com/view/kaist-ais/news> 2026년 소식. 관측 2026-10-26.
[^news25]: 연구실 News-2025. <https://sites.google.com/view/kaist-ais/news-2025> 2025년 소식과 Sejin Jang의 수상. 관측 2026-10-27.
[^news24]: 연구실 News-2024. <https://sites.google.com/view/kaist-ais/news-2024> 2024년 3월 1일 연구실 개소와 교수 부임, 12월 11일 수상 소식. 관측 2026-10-27.
[^contact]: 연구실 Contact Us. <https://sites.google.com/view/kaist-ais/contact-us> 주소·전화와 문의 안내. 관측 2026-10-26.
[^p1]: S. Koo, S. Han, H.-S. Shin, IEEE Control Systems Letters. <https://doi.org/10.1109/lcsys.2026.3710526> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/rnc.7743|10.1007/s13272-024-00763-5|10.1016/j.asoc.2026.115797|10.1016/j.automatica.2026.113170|10.1016/j.paerosci.2024.101005|10.1016/j.paerosci.2025.101129|10.1109/jas.2025.125291|10.1109/lcsys.2026.3710526|10.1109/taes.2024.3406312|10.1109/taes.2024.3443024|10.1109/taes.2024.3448408|10.1109/taes.2025.3576080|10.1109/tro.2025.3613566|10.1109/tsmc.2024.3414411|10.2139/ssrn.4837939|10.2139/ssrn.4838451|10.2139/ssrn.5158079|10.2514/1.g007234|10.2514/1.i011301|10.3390/drones8050167> (관측 2026-10-27).
[^p2]: J. Autenrieb, H.-S. Shin, International Journal of Robust and Nonlinear Control. <https://doi.org/10.1002/rnc.7743> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/rnc.7743> (관측 2026-10-27).
[^p3]: J. Autenrieb, H.-S. Shin, arXiv (온라인 2024-10-10). <https://arxiv.org/abs/2410.08096> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.08096> (개정 2025-03-24, 관측 2026-10-27).
[^p4]: T. Jin, H.-S. Shin, A. Tsourdos, S. He, IEEE Transactions on Aerospace and Electronic Systems. <https://doi.org/10.1109/taes.2024.3448408> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/rnc.7743|10.1007/s13272-024-00763-5|10.1016/j.asoc.2026.115797|10.1016/j.automatica.2026.113170|10.1016/j.paerosci.2024.101005|10.1016/j.paerosci.2025.101129|10.1109/jas.2025.125291|10.1109/lcsys.2026.3710526|10.1109/taes.2024.3406312|10.1109/taes.2024.3443024|10.1109/taes.2024.3448408|10.1109/taes.2025.3576080|10.1109/tro.2025.3613566|10.1109/tsmc.2024.3414411|10.2139/ssrn.4837939|10.2139/ssrn.4838451|10.2139/ssrn.5158079|10.2514/1.g007234|10.2514/1.i011301|10.3390/drones8050167> (관측 2026-10-27).
[^p5]: B. Cui 외, H.-S. Shin, IEEE Transactions on Aerospace and Electronic Systems. <https://doi.org/10.1109/taes.2024.3406312> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/rnc.7743|10.1007/s13272-024-00763-5|10.1016/j.asoc.2026.115797|10.1016/j.automatica.2026.113170|10.1016/j.paerosci.2024.101005|10.1016/j.paerosci.2025.101129|10.1109/jas.2025.125291|10.1109/lcsys.2026.3710526|10.1109/taes.2024.3406312|10.1109/taes.2024.3443024|10.1109/taes.2024.3448408|10.1109/taes.2025.3576080|10.1109/tro.2025.3613566|10.1109/tsmc.2024.3414411|10.2139/ssrn.4837939|10.2139/ssrn.4838451|10.2139/ssrn.5158079|10.2514/1.g007234|10.2514/1.i011301|10.3390/drones8050167> (관측 2026-10-27).
[^p6]: S. Lee, H.-S. Shin, CEAS Aeronautical Journal. <https://doi.org/10.1007/s13272-024-00763-5> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Destination%20and%20time-series%20inference%20of%20moving%20objects%20via%20conditionally%20Markov%20process> (관측 2026-10-27).
[^p7]: S. Kim 외, S. Khattak, arXiv (온라인 2025-03-13). <https://arxiv.org/abs/2503.10349> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.10349> (개정 2025-06-13, 관측 2026-10-27).

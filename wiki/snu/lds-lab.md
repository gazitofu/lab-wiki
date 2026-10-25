# 학습 및 의사결정 시스템 연구실 (Learning and Decision Systems Lab, LDS Lab)

**서울대학교 공과대학 전기·정보공학부 · 양인순 교수**

- 분야: 불확실성 아래 학습과 의사결정, 강화학습과 확률 제어, 기계학습을 위한 최적화
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 강화학습[^home][^p4], 제어 이론·제어 공학[^home], 로봇 항법·SLAM[^p8]
- 홈페이지: <https://lds-lab.github.io/>

> 자료로 환경을 배우고, 배운 내용에 오차가 있어도 행동을 결정할 수 있도록 기계학습·최적화·제어 이론을 함께 연구하는 연구실이다.[^home]

## 무엇을 연구하나

LDS Lab은 불확실한 상황에서 학습과 의사결정의 이론·알고리즘을 발전시키는 것을 목표로 한다. 기계학습(자료에서 규칙을 학습하는 계산 방법), 최적화(목표와 제약에 맞는 해를 찾는 수학적 방법), 제어 이론(시스템의 동작을 목표에 맞추는 입력을 설계·분석하는 분야)의 관계를 연구한다. 첫 화면은 의사결정·제어를 위한 Physical AI(물리적 환경과 상호작용하는 인공지능), 강화학습(행동으로 얻는 보상을 바탕으로 행동 방식을 학습하는 방법)과 확률 제어(무작위 요인을 포함한 시스템의 입력을 정하는 방법), 기계학습을 위한 최적화를 연구 분야로 든다.[^home]

연구의 한 축은 학습에 쓰는 수학적 방법 자체를 이해하는 일이다. 가속 경사법(기울기와 이전 계산의 정보를 이용해 목적함수를 줄여 가는 방법)을 볼록·강볼록 문제에서 통합하는 연구와, 손실의 평탄함을 고려하는 학습 알고리즘이 원래 문제의 해가 아닌 곳에 멈추는 현상을 분석한 연구가 있다.[^p2][^p1] 다른 축은 환경의 모든 성질을 똑같이 배우기보다 행동 결정에 필요한 정보를 학습하고, 학습 중의 탐색까지 포함해 제어 성능을 분석하는 일이다.[^p4][^p3]

불확실한 환경에서는 관측 자료와 실제 시스템 사이의 차이도 고려한다. 분포 강건 추정(확률분포의 오차를 고려해 시스템 상태를 추정하는 방법)으로 잡음에 대한 가정이 달라도 상태를 추정하고, 로봇 항법(로봇이 위치와 주변 상황을 바탕으로 이동을 정하는 기술)에서는 예측 오차 가운데 충돌 안전에 영향을 주는 부분을 따로 평가한다.[^p5][^p8] 이동 궤적 예측(대상이 앞으로 이동할 위치의 흐름을 예측하는 일)에는 비선형 동역학(상태 변화가 입력·상태에 선형으로 비례하지 않는 시스템의 변화 법칙)을 선형 표현으로 다루는 이론을 신경망(연결된 계산 단위의 가중치를 학습해 입력을 출력으로 바꾸는 모형)과 결합한다.[^p7]

## 주요 연구 주제

### 기계학습 최적화의 원리와 한계

네스테로프 가속 경사법은 이전 계산의 정보를 다음 갱신에 반영하는 최적화 방법이다. 2023년 논문은 볼록 함수(두 입력 사이의 함수값이 양 끝의 함수값을 직선으로 이은 값을 넘지 않는 함수)와 강볼록 함수(일정한 양의 이차항을 빼도 볼록성이 유지되는 함수)에 따로 쓰이던 가속 방법을 하나의 틀로 묶었다. 계산 알고리즘과 연속시간 모형(시간을 연속적인 값으로 다루는 수학적 표현)을 함께 다루고, 강볼록성이 약한 문제에서도 쓸 수 있는 통합 방법을 제시했다.[^p2]

2026년 수정본은 SAM(Sharpness-Aware Minimization, 손실의 주변 변화를 고려하는 최소화 방법)이 원래 손실의 기울기가 남아 있는 점에서도 멈출 수 있음을 보였다. 섭동(분석이나 계산을 위해 값에 가하는 변화)을 준 위치의 기울기만 사라져 멈추는 점을 hallucinated minimizers라고 부른다. 신경망 학습에서도 이 현상을 확인하고, SAM을 쓰기 전에 확률적 경사하강법(자료의 일부 등으로 구한 기울기로 값을 갱신하는 최적화 방법)으로 초기 학습을 하는 방식을 완화책으로 시험했다.[^p1]

### 자료를 활용하는 강화학습

메타 강화학습(여러 과제의 경험으로 새 과제에 적응하는 법을 학습하는 방법)은 새 환경에서 어떤 정보를 배울지가 중요하다. 2024년 논문은 과제 추론 모듈(현재 수행 중인 과제의 성질을 추정하는 계산 부분)과 환경 모형을 학습할 때, 모형의 오차와 가치 추정(행동으로 앞으로 얻을 누적 보상을 추정하는 일)을 함께 반영하는 손실함수(학습 과정에서 줄일 오차를 수치로 나타낸 함수)를 설계했다. 로봇 제어 실험을 통해 과제를 푸는 데 필요한 정보를 관측에서 추출하는 방법을 평가했다.[^p4]

2025년 논문은 선형 이차 조절기(LQR, Linear Quadratic Regulator, 선형 시스템에서 상태·입력의 이차 비용을 줄이는 제어기)를 학습하는 톰프슨 샘플링(추정한 모형의 확률분포에서 표본을 뽑아 행동을 정하는 방법)을 제안했다. 근사 사후분포 표본(관측 자료를 반영한 확률분포에서 근사적으로 뽑은 값)을 이용하고, 시스템을 알아내기 위한 입력을 더해 탐색과 제어를 결합했다.[^p3]

### 불확실성 아래 추정과 성능 분석

칼만 필터(동작 모형과 관측을 결합해 시스템 상태를 갱신하는 추정 방법)는 모형에 둔 잡음의 가정이 실제와 다르면 성능이 달라질 수 있다. 2025년 논문은 바서슈타인 모호성 집합(확률분포 사이의 거리를 나타내는 바서슈타인 거리로 정한 범위 안의 확률분포를 모은 집합)으로 시스템 변화와 측정의 잡음 분포에 대한 불확실성을 표현했다. 반정정부호 계획법(행렬이 나타내는 이차식의 값이 모든 입력에서 음수가 되지 않도록 제약하는 최적화 방법)을 미리 풀어 일정한 추정 이득(새 관측을 상태 추정에 반영하는 가중치)을 얻고, 시간에 따라 달라지는 필터가 이 해에 수렴(반복 계산으로 얻는 값이 일정한 값에 가까워지는 성질)하는 조건도 분석했다.[^p5]

순차 의사결정의 성능은 후회값(최선의 선택을 알았을 때와 실제 선택 사이의 누적 성과 차이)으로 분석한다. 2022년 논문은 선형 밴딧(행동의 특징과 기대 보상의 선형 관계를 이용하는 순차 선택 문제)과 선형 혼합 마르코프 의사결정 과정(기본 모형들을 선형 결합해 상태 변화 확률을 나타내는 의사결정 모형)에서 후회값의 상한을 분석했다. 잡음의 분산을 미리 모르는 조건을 다루며, 후자의 경우에는 한 번의 시행에서 얻는 누적 보상이 정해진 범위 안이라는 가정 아래 결과를 제시했다.[^p6]

### 이동 예측과 안전한 항법

KoopCast는 어디로 갈지와 어떻게 갈지를 나눠 이동 궤적을 예측한다. 확률적 신경망 목표 추정기가 장기 목표를 예측하고, 쿠프만 연산자(비선형 시스템에서 관측 함수의 시간 변화를 선형으로 나타내는 연산자)를 쓰는 부분이 의도와 이동 이력을 반영한다. 여러 보행자·차량 이동 자료에서 예측 정확도와 해석 가능성, 계산 효율을 평가했다.[^p7]

안전한 항법 연구는 장애물의 위치를 틀리게 예측한 모든 경우를 똑같이 취급하지 않는다. 2025년 논문은 등각 예측(보정 자료를 이용해 통계적 보장을 갖는 예측 집합을 만드는 방법)을 제어와 연결하고, 장애물이 후보 차량 위치에 예상보다 얼마나 가까운지를 점수로 나타냈다. 이를 모델 예측 제어(미래 동작을 예측해 입력을 계산하고 새 관측으로 다시 계산하는 제어 방법)에 넣어 각 후보 상태의 안전을 평가하고, 장애물의 움직임 변화에 맞춰 보정을 조절했다.[^p8]

## 대표 논문

서울대 부임 이후 연구 가운데 네 연구 갈래를 보여 주는 8편을 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 1·5·7·8은 연결한 arXiv 사전 공개본을 기준으로 설명하고, 1의 연도는 수정본 연도다. 나머지는 학회 논문집 판이다. 1·7은 랩이 각각 ICML 2026·ICRA 2026 채택을 공지했다.[^people][^home]

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Sharpness-Aware Minimization Can Hallucinate Minimizers](https://doi.org/10.48550/arXiv.2509.21818) · arXiv v2 | 주변 손실을 고려하는 SAM이 원래 손실을 줄일 여지가 남은 점에서도 멈추는 조건과 그곳으로 수렴하는 조건을 분석했다. 신경망 학습에서 이 현상을 확인했으며, SAM 전에 짧은 초기 학습을 하는 방법으로 현상과 설정값 민감도를 완화했다.[^p1] | 마지막 저자 |
| 2 | 2023 | [Unifying Nesterov’s Accelerated Gradient Methods for Convex and Strongly Convex Objective Functions](https://proceedings.mlr.press/v202/kim23y.html) · ICML | 볼록 문제와 강볼록 문제에 나누어 쓰던 가속 경사법의 수학적 모형과 알고리즘을 통합했다. 두 형태를 이어 주는 알고리즘을 만들고, 비유클리드 공간(거리를 유클리드 공간과 다른 기하로 다루는 공간)에도 틀을 확장했다.[^p2] | 마지막 저자 |
| 3 | 2025 | [Approximate Thompson Sampling for Learning Linear Quadratic Regulators with $O(\sqrt{T})$ Regret](https://proceedings.mlr.press/v283/kim25b.html) · L4DC | 시스템 모형을 학습하며 제어하는 톰프슨 샘플링에 근사 표본 추출과 탐색용 입력을 결합했다. 추정 분포의 성질과 시스템 상태를 분석해 베이지안 후회값(모형의 불확실성에 대해 기댓값을 낸 누적 성과 차이)의 상한을 보였다.[^p3] | 마지막 저자 |
| 4 | 2024 | [On task-relevant loss functions in meta-reinforcement learning](https://proceedings.mlr.press/v242/shin24a.html) · L4DC | 과제 수행에 중요한 환경 정보를 배우도록 모형 오차와 가치 추정을 연결한 손실함수를 설계했다. 과제와 행동을 배우는 데 드는 자료량을 줄이는 방법을 제안하고 고차원 로봇 제어에서 평가했다.[^p4] | 마지막 저자 |
| 5 | 2025 | [On the Steady-State Distributionally Robust Kalman Filter](https://doi.org/10.48550/arXiv.2503.23742) · arXiv v1 | 시스템 변화와 측정의 잡음 분포가 부정확할 때를 고려하는 상태 추정기를 제안했다. 최적화 문제를 미리 풀어 일정한 추정 이득을 얻고, 시간에 따라 바뀌는 추정기의 해가 이 결과에 가까워지는 조건을 분석했다. 수치 실험에서 기존 필터와 비교했다.[^p5] | 마지막 저자 |
| 6 | 2022 | [Improved Regret Analysis for Variance-Adaptive Linear Bandits and Horizon-Free Linear Mixture MDPs](https://doi.org/10.52202/068431-0078) · NeurIPS | 자료를 얻으면서 행동을 고르는 두 종류의 문제에서 누적 성과 차이의 상한을 새로 분석했다. 선형 밴딧에서는 잡음의 분산을 반영하고, 선형 혼합 의사결정 모형에서는 누적 보상에 관한 가정 아래 시행 길이에 의존하지 않는 상한을 제시했다.[^p6] | 3명 중 두 번째 저자 |
| 7 | 2025 | [KoopCast: Trajectory Forecasting via Koopman Operators](https://doi.org/10.48550/arXiv.2509.15513) · arXiv v1 | 장기 이동 목표를 예측하는 부분과, 의도·이력을 반영해 이동 경로를 다듬는 부분을 결합했다. 비선형 움직임을 선형 연산으로 예측할 수 있게 표현하고 보행자·차량 자료에서 정확도, 해석 가능성, 실행 효율을 평가했다.[^p7] | 마지막 저자 |
| 8 | 2025 | [Egocentric Conformal Prediction for Safe and Efficient Navigation in Dynamic Cluttered Environments](https://doi.org/10.48550/arXiv.2504.00447) · arXiv v1 | 예측 오차가 충돌 위험에 미치는 영향을 기준으로 로봇 항법을 설계했다. 장애물이 예상보다 얼마나 가까운지 평가하는 점수와 적응형 예측 보정을 제어에 넣었다. 이론 분석과 보행자가 밀집한 실제 자료 실험으로 안전 수준과 비용 효율을 평가했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

양인순 교수는 2009년 서울대학교 기계항공공학부·수리과학부에서 학사를, UC Berkeley에서 2012년 전기컴퓨터공학 석사, 2013년 수학 석사, 2015년 전기컴퓨터공학 박사를 받았다. 2015–2016년 MIT LIDS 박사후연구원, 2016–2018년 University of Southern California 조교수를 거쳐 2018년 서울대학교에 부임했다. 학과 교수 소개는 전공을 강화학습·최적화로, 연구 관심을 강화학습·머신러닝을 위한 최적화·Physical AI로 적는다.[^prof][^people]

최근 논문으로 보면 전문 분야는 기계학습 최적화 알고리즘의 수렴·한계 분석,[^p1][^p2] 환경 모형을 학습하는 강화학습과 학습 중 제어,[^p3][^p4] 불확실한 분포를 고려한 상태 추정과 순차 의사결정 이론,[^p5][^p6] 이동 예측과 안전한 로봇 제어다.[^p7][^p8] 랩 첫 화면은 2026년 8월 IEEE Transactions on Automatic Control 부편집위원 임명과 2025년 9월 IEEE Open Journal of Control Systems의 기계학습·제어 교차 분야 특별 섹션 Guest Senior Editor 임명을 알렸다.[^home]

## 응용 분야와 공개 소프트웨어

대표 논문은 로봇 제어에서 과제에 필요한 정보를 학습하고,[^p4] 보행자·차량의 이동을 예측하며,[^p7] 움직이는 장애물이 있는 환경에서 안전한 이동을 결정하는 문제를 다룬다.[^p8] 랩 첫 화면은 인공지능 기반 자율성의 사회적 가치를 실현하는 것을 비전으로 내세운다.[^home]

Software 페이지는 분포 강건 의사결정, 강화학습, 기계학습 최적화 세 묶음으로 코드를 공개한다. DR-LQR, DR-DDP, DR-UT-MPC, DR-Risk Map은 강건 제어·경로 계획 연구에, Approximate Thompson Sampling for LQR, Task Relevant Meta-RL, MPC-PEARL, HJ-DQN, AA-POMDP는 학습·제어 연구에, UNAG와 RNAG는 가속 최적화 연구에 대응하는 코드다.[^software]

## 구성원

2026년 10월 25일 People 페이지의 Ph.D. Program 11명과 Hyundai Mobility M.S. Program 1명이다. 연구 주제는 카드의 Research Interest 표기를 옮겼다.[^people] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Giho Kim | 박사과정 | Reinforcement Learning, Optimization for Machine Learning | 4 |
| Chanwoong Park | 박사과정 | Optimization for Machine Learning | 1 |
| Jaeseok Joo | 박사과정 | Reinforcement Learning |  |
| Joon Ho Han | 박사과정 | Reinforcement Learning | 4, 7 |
| Howon Lee | 박사과정 | Autonomous Systems | 4 |
| Jungjin Lee | 박사과정 | Stochastic Control, Trajectory Forecasting | 7, 8 |
| Sukchul Jung | 박사과정 | Reinforcement Learning, Physical AI |  |
| Sungkwon On | 박사과정 | Reinforcement Learning, Physical AI |  |
| Se Jin Kim | 박사과정 | Optimization, Physical AI |  |
| Donghoon Ryu | 박사과정 | Physical AI, Continual Learning |  |
| Gun Choi | 박사과정 | Distributionally Robust Control, Partially Observable Systems |  |
| Hyeongjun Song | 석사과정 | Autonomous Driving |  |

## 졸업생과 이전 구성원

People 페이지 Alumni의 16명이다. 학위·과정과 연도는 랩이 적은 그대로이며, 박사후연구원과 방문 구성원도 포함한다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaeuk Shin | Ph.D. (2026) | Naver Labs |
| Astghik Hakobyan | Ph.D. (2023) | Assistant Professor, National Polytechnic University of Armenia |
| Youngchae Cho | Postdoc. (2024) | Research Associate, Tokyo Institute of Technology |
| Yeoneung Kim | Postdoc. (2022) | Assistant Professor, Dept. of Industrial Engineering, Yonsei University |
| Jeongho Kim | Postdoc. (2021) | Assistant Professor, Dept. of Applied Mathematics, Kyung Hee University |
| Gihun Kim | M.S. (2023) |  |
| Melike Ermis | M.S. (2021) | Startup |
| Subin Huh | M.S. (2020) | Samsung Electronics |
| Taewoo Kang | M.S. (2020) | TmaxSoft |
| Minhyuk Jang | B.S. (2025) | Ph.D. program, UIUC ME |
| Jihoon Kim | B.S. (2022) | Ph.D. program, UC Berkeley IEOR |
| Keunwoo Lim | B.S. (2021) | Ph.D. program, Univ. of Washington Applied Math |
| Kihyun Kim | B.S. (2021) | Ph.D. program, MIT EECS |
| Wonkyung Do | B.S. (2019) | Ph.D. program, Stanford University |
| Sunho Jang | B.S. (2019) | Ph.D. program, Univ. of Michigan EECS |
| Juan Moreno Nadales | Visitor (2022) | Ph.D. program, Universidad de Sevilla, Spain |

## 최근 논문 목록 (2021–2026)

Publications 페이지의 2021–2026년 구역에 있는 43편이다. 연도·제목·저자·발표처는 랩 목록의 표기를 따른다. 2026년 NeurIPS·CDC 항목은 첫 화면의 공지에 따라 채택으로 표시했다. ICML·ICRA 2026 두 항목은 랩 채택 공지와 연결된 arXiv 사전 공개본을 구분해 적었다. 다른 항목의 학회 연도만으로 채택 여부를 추가하지 않았다.[^pubs][^home]

**2026**

- Sukchul Jeong, and Insoon Yang. "Distributionally robust domain randomization with learned risk-sensitive dynamics samplers". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (Spotlight) (채택)*.
- Jaesuk Joo, and Insoon Yang. "AdaptFlow: State-achored modulation with flow matching for offline goal-conditioned RL". *Advances in Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Chanwoong Park, Uijeong Jang, Ernest K. Ryu, and Insoon Yang. "Sharpness-aware minimization can hallucinate minimizers". *International Conference on Machine Learning (ICML), 2026 (누리집 채택 공지, 연결 자료는 arXiv 사전 공개본)*.
- Jungjin Lee, Jaeuk Shin, Gihwan Kim, Joonho Han, and Insoon Yang. "KoopCast: Trajectory forecasting via Koopman operators". *IEEE International Conference on Robotics and Automation (ICRA), 2026 (누리집 채택 공지, 연결 자료는 arXiv 사전 공개본)*.
- Sung Kwon On, Sukchul Jeong, Jungjin Lee, and Insoon Yang. "Physics-informed causal reasoning in physical AI: A review on modeling non-stationary environments for safety–critical control". *International Journal of Control, Automation, and Systems (IJCAS), 24:726-752, 2026*.
- Jaeuk Shin, Joon Ho Han, Gihwan Kim, Jungjin Lee, and Insoon Yang. "CANVAS: Competency-aware navigation assessment suite for pedestrian trajectory forecasting". *IEEE Open Journal of Control Systems, 5:378-393, 2026*.
- Minhyuk Jang, Jungjin Lee, Astghik Hakobyan, Naira Hovakimyan, and Insoon Yang. "Residual-aware distributionally robust EKF: Absorbing linearization mismatch via Wasserstein ambiguity". *IEEE Conference on Decision and Control (CDC), 2026 (채택)*.
- Giho Kim, and Insoon Yang. "Zero-shot generalization in LQR via D-optimal successor-feature coverage". *IEEE Conference on Decision and Control (CDC), 2026 (채택)*.
- Chanwoong Park, Youngchae Cho, and Insoon Yang. "Lookahead-gradient dynamics for Nesterov acceleration in continuous time". *IEEE Conference on Decision and Control (CDC), 2026 (채택)*.

**2025**

- Yeoneung Kim, Gihun Kim, Jiwhan Park, and Insoon Yang. "Approximate Thompson sampling for learning linear quadratic regulators with $O(\sqrt{T})$ regret". *Learning for Dynamics and Control (L4DC), 2025. (Oral)*.
- Jaeuk Shin, Jungjin Lee, and Insoon Yang. "Egocentric conformal prediction for safe and efficient navigation in dynamic cluttered environments". *IEEE Conference on Decision and Control (CDC), 2025*.
- Minhyuk Jang, Astghik Hakobyan, and Insoon Yang. "On the steady-state distributionally robust Kalman filter". *IEEE Conference on Decision and Control (CDC), 2025*.
- Youngchae Cho, Insoon Yang, and Takayuki Ishizaki. "Robust continuous-time generation scheduling under power demand uncertainty: An affine decision rule approach". *IEEE Conference on Decision and Control (CDC), 2025*.

**2024**

- Astghik Hakobyan, and Insoon Yang. "Wasserstein distributionally robust control of partially observable linear stochastic systems". *IEEE Transactions on Automatic Control, 69(9):6121–6136, 2024*.
- Juan Moreno Nadales, Astghik Hakobyan, David Munoz de la Pena, Daniel Limon, and Insoon Yang. "Risk-aware Wasserstein distributionally robust control of vessels in natural waterways". *IEEE Transactions on Control Systems Technology, 32(4):1471–1478, 2024*.
- Jaeuk Shin, Giho Kim, Howon Lee, Joonho Han, and Insoon Yang. "On task-relevant loss functions in meta-reinforcement learning". *Learning for Dynamics and Control (L4DC), 2024*.
- Jaeuk Shin, and Insoon Yang. "Multiparametric analysis of multi-task Markov decision processes: Structure, invariance, and reducibility". *IEEE Control Systems Letters, 8:928–933, 2024. (Selected for presentation at CDC'24)*.
- Youngchae Cho, and Insoon Yang. "Wasserstein distributionally robust regret minimization". *IEEE Control Systems Letters, 8:820–825, 2024. (Selected for presentation at CDC'24)*.
- Mingyu Park, Jaeuk Shin, and Insoon Yang. "Anderson acceleration for partially observable Markov decision processes: A maximum entropy approach". *Automatica, 163:111557, 2024*.
- Giho Kim, Jaeuk Shin, Gihun Kim, Joonrak Kim, and Insoon Yang. "Control of fab lifters via deep reinforcement learning: A semi-MDP approach". *IEEE Transactions on Automation Science and Engineering, 21(4):5136–5148, 2024*.

**2023**

- Jungbin Kim, and Insoon Yang. "Convergence analysis of ODE models for accelerated first-order methods via positive semidefinite kernels". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Astghik Hakobyan, and Insoon Yang. "Distributionally robust differential dynamic programming with Wasserstein distance". *IEEE Control Systems Letters, 7:2329–2334, 2023. (Selected for presentation at CDC'23)*.
- Youngchae Cho, and Insoon Yang. "Data-driven stochastic optimization using upper confidence bounds: Performance guarantees and distributional robustness". *IEEE Conference on Decision and Control (CDC), 2023*.
- Yeoneung Kim, Gihun Kim, and Insoon Yang. "On concentration bounds for Bayesian identification of linear non-Gaussian systems". *IEEE Conference on Decision and Control (CDC), 2023*.
- Jungbin Kim, and Insoon Yang. "Unifying Nesterov’s accelerated gradient methods for convex and strongly convex objective functions". *International Conference on Machine Learning (ICML), 2023. (Oral)*.
- Astghik Hakobyan, and Insoon Yang. "Distributionally robust optimization with unscented transform for learning-based motion control in dynamic environments". *IEEE International Conference on Robotics and Automation (ICRA), 2023*.
- Jeongho Kim, and Insoon Yang. "Maximum entropy optimal control of continuous-time dynamical systems". *IEEE Transactions on Automatic Control, 68(4):2018–2033, 2023*.
- Kihyun Kim, and Insoon Yang. "Distributional robustness in minimax linear quadratic control with Wasserstein distance". *SIAM Journal on Control and Optimization, 61(2):458-483, 2023*.
- Astghik Hakobyan, and Insoon Yang. "Distributionally robust risk map for learning-based motion planning and control: A semidefinite programming approach". *IEEE Transactions on Robotics, 39(1):718-737, 2023*.

**2022**

- Yeoneung Kim, Insoon Yang, and Kwang-Sung Jun. "Improved regret analysis for variance-adaptive linear bandits and horizon-free linear mixture MDPs". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Astghik Hakobyan, and Insoon Yang. "Wasserstein distributionally robust control of partially observable linear systems: Tractable approximation and performance guarantee". *IEEE Conference on Decision and Control (CDC), 2022*.
- Youngchae Cho, and Insoon Yang. "On affine policies for Wasserstein distributionally robust unit commitment". *IEEE Conference on Decision and Control (CDC), 2022*.
- Jaeuk Shin, Astghik Hakobyan, Mingyu Park, Yeoneung Kim, Gihun Kim, and Insoon Yang. "Infusing model predictive control into meta-reinforcement learning for mobile robots in dynamic environments". *IEEE Robotics and Automation Letters, 7(4):10065–10072, 2022. (Selected for presentation at IROS'22)*.
- Yeoneung Kim, and Insoon Yang. "On representation formulas for optimal control: A Lagrangian perspective". *IET Control Theory & Applications, 16(16):1633-1644, 2022*.
- Jungbin Kim, and Insoon Yang. "Accelerated gradient methods for geodesically convex optimization: Tractable algorithms and convergence analysis". *International Conference on Machine Learning (ICML), 2022*.
- Margaret P. Chapman, Riccardo Bonalli, Kevin M. Smith, Insoon Yang, Marco Pavone, and Claire J. Tomlin. "Risk-sensitive safety analysis using conditional value-at-risk". *IEEE Transactions on Automatic Control, 67(12):6521-6536, 2022*.
- Astghik Hakobyan, and Insoon Yang. "Wasserstein distributionally robust motion control for collision avoidance using conditional value-at-risk". *IEEE Transactions on Robotics, 38(2):939–957, 2022*.
- Seung-Yeal Ha, Myeongju Kang, Dohyun Kim, Jeongho Kim, and Insoon Yang. "Stochastic consensus dynamics for nonconvex optimization on the Stiefel manifold: Mean-field limit and convergence". *Mathematical Models and Methods in Applied Sciences, 32(3):533–617, 2022*.

**2021**

- Jeongho Kim, Jaeuk Shin, and Insoon Yang. "Hamilton-Jacobi deep Q-learning for deterministic continuous-time systems with Lipschitz continuous controls". *Journal of Machine Learning Research (JMLR), 22(206):1–34, 2021*.
- Insoon Yang. "Wasserstein distributionally robust stochastic control: A data-driven approach". *IEEE Transactions on Automatic Control, 66(8):3863–3870, 2021*.
- Woo-Kyun Jung, Dong-Ryul Kim, Hyunsu Lee, Tae-Hun Lee, Insoon Yang, Byeng D. Youn, Daniel Zontar, Matthias Brockmann, Christian Brecher, and Sung-Hoon Ahn. "Appropriate Smart Factory for SMEs: Concept, Application and Perspective". *International Journal of Precision Engineering and Manufacturing, 22:201–215, 2021*.
- Melike Ermis, Mingyu Park, and Insoon Yang. "On Anderson acceleration for partially observable Markov decision processes". *IEEE Conference on Decision and Control (CDC), 2021*.
- Astghik Hakobyan, and Insoon Yang. "Toward improving the distributional robustness of risk-aware controllers in learning-enabled environments". *IEEE Conference on Decision and Control (CDC), 2021*.

## 수상

2021년 10월 22일–2026년 10월 22일 범위의 첫 화면 소식에 게시된 수상이다.[^home]

- Aug. 2023 · Astghik Hakobyan, Distinguished ECE Ph.D. Dissertation Award 수상

## 소식

같은 기간의 첫 화면 News에서 논문 채택과 학술 편집 활동을 알린 17건이다. 날짜는 누리집이 적은 월이다.[^home]

- Sep. 2026 · Two papers (1 Spotlight) have been accepted to NeurIPS 2026: "Distributionally robust domain randomization with learned risk-sensitive dynamics samplers", and "AdaptFlow: State-anchored modulation with flow matching for offline goal-conditioned RL.
- Aug. 2026 · Appointed as Associate Editor for IEEE Transactions on Automatic Control.
- Jul. 2026 · Three papers have been accepted to IEEE Conference on Decision and Control (CDC) 2026.
- Jul. 2026 · "CANVAS: Competency-aware navigation assessment suite for pedestrian trajectory forecasting" has been accepted to IEEE Open Journal of Control Systems.
- May. 2026 · "Sharpness-Aware Minimization Can Hallucinate Minimizers" has been accepted to International Conference on Machine Learning (ICML).
- Apr. 2026 · "Physics-Informed Causal Reasoning in Physical AI: A Review on Modeling Non-stationary Environments for Safety–Critical Control" has been accepted to IJCAS.
- Feb. 2026 · "KoopCast: Trajectory Forecasting via Koopman Operators" has been accepted to IEEE International Conference on Robotics and Automation (ICRA).
- Sep. 2025 · Appointed as Guest Senior Editor for the Special Section on the Intersection of ML and Control, IEEE Open Journal of Control Systems.
- Jul. 2025 · Three papers have been accepted to IEEE Conference on Decision and Control (CDC) 2025.
- Mar. 2025 · "Approximate Thompson sampling for learning linear quadratic regulators with $O(\sqrt{T})$ regret" has been accepted to Learning for Dynamics and Control (L4DC). (Oral)
- Apr. 2024 · "Wasserstein distributionally robust control of partially observable linear stochastic systems" has been accepted to IEEE Transactions on Automatic Control.
- Mar. 2024 · "On task-relevant loss functions in meta-reinforcement learning" has been accepted to Learning for Dynamics and Control (L4DC).
- Jan. 2024 · "Anderson acceleration for partially observable Markov decision processes: A maximum entropy approach" has been accepted to Automatica.
- Dec. 2023 · "Risk-aware Wasserstein distributionally robust control of vessels in natural waterways" has been accepted to IEEE Transactions on Control Systems Technology.
- Sep. 2023 · "Convergence analysis of ODE models for accelerated first-order methods via positive semidefinite kernels" has been accepted to Advances in Neural Information Processing Systems (NeurIPS).
- Aug. 2023 · "Control of fab lifters via deep reinforcement learning: A semi-MDP approach" has been accepted to IEEE Transactions on Automation Science and Engineering.
- Apr. 2023 · "Unifying Nesterov's accelerated gradient methods for convex and strongly convex objective functions" has been accepted to International Conference on Machine Learning (ICML). (Oral)

## 연락과 위치

- 연구실 주소 1: 서울특별시 관악구 관악로 1 서울대학교 301동 708호, 우편번호 08826[^contact]
- 연구실 주소 2: 같은 캠퍼스 133동 405호, Automation and Systems Research Institute[^contact]
- 교수실 전화: 02-880-1729[^prof]
[^home]: LDS Lab 첫 화면, 연구 목적·연구 분야·소속 목록·소식. <https://lds-lab.github.io/> (열람 2026-10-25).
[^people]: LDS Lab People, 교수 이력·구성원·Alumni. <https://lds-lab.github.io/People/> (열람 2026-10-25).
[^prof]: 서울대학교 전기·정보공학부 양인순 교수 소개, 학력·경력·연구 관심·전화·교수실. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p824> (열람 2026-10-25).
[^pubs]: LDS Lab Publications, 연도별 논문 목록. <https://lds-lab.github.io/publications/> (열람 2026-10-25).
[^software]: LDS Lab Software, 연구 논문에 대응하는 공개 코드 목록. <https://lds-lab.github.io/Software/> (열람 2026-10-25).
[^contact]: LDS Lab Contact, 두 연구실 주소. <https://lds-lab.github.io/contact/> (열람 2026-10-25).
[^p1]: C. Park, U. Jang, E. K. Ryu, I. Yang, arXiv:2509.21818v2 (온라인 2026-02-05). <https://doi.org/10.48550/arXiv.2509.21818> 초록 기준(arXiv 판).
[^p2]: J. Kim, I. Yang, Proceedings of the 40th International Conference on Machine Learning 202, 16897–16954 (2023). <https://proceedings.mlr.press/v202/kim23y.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p3]: Y. Kim, G. Kim, J. Park, I. Yang, Proceedings of the 7th Annual Learning for Dynamics & Control Conference 283, 378–391 (2025). <https://proceedings.mlr.press/v283/kim25b.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p4]: J. Shin 외, I. Yang, Proceedings of the 6th Annual Learning for Dynamics & Control Conference 242, 1174–1186 (2024). <https://proceedings.mlr.press/v242/shin24a.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: M. Jang, A. Hakobyan, I. Yang, arXiv:2503.23742v1 (온라인 2025-03-31). <https://doi.org/10.48550/arXiv.2503.23742> 초록 기준(arXiv 판).
[^p6]: Y. Kim, I. Yang, K.-S. Jun, Advances in Neural Information Processing Systems 35 (2022). <https://doi.org/10.52202/068431-0078> 초록 기준(학회 논문집 페이지 게시 초록).
[^p7]: J. Lee 외, I. Yang, arXiv:2509.15513v1 (온라인 2025-09-19). <https://doi.org/10.48550/arXiv.2509.15513> 초록 기준(arXiv 판).
[^p8]: J. Shin, J. Lee, I. Yang, arXiv:2504.00447v1 (온라인 2025-04-01). <https://doi.org/10.48550/arXiv.2504.00447> 초록 기준(arXiv 판).

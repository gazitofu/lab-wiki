# Reinforced Decision Intelligence Lab

**KAIST 전기및전자공학부 · 이동환 부교수**

- 분야: 강화학습의 수학적 분석, 학습 기반 제어, 자율 시스템과 산업 공정의 의사결정
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 강화학습[^research], 제어 이론·제어 공학[^control], 다중 에이전트 시스템·분산 의사결정[^home][^p3]
- 홈페이지: <https://sites.google.com/site/donghwanleehome>
- 근거와 출처: [Reinforced Decision Intelligence Lab 근거 페이지](rdi-sources.md)

> 행동을 배우는 알고리즘이 왜 제대로 작동하는지 수학적으로 분석하고, 안정성과 안전을 고려한 학습 방법을 로봇·자율주행·산업 시스템에 연결하는 연구실이다.[^home][^research]

## 무엇을 연구하나

이동환 부교수가 이끄는 연구실은 강화학습(행동에 따른 보상을 바탕으로 앞으로 얻을 보상의 합을 크게 하는 행동 방법을 배우는 기계학습)을 연구한다.[^research] 기계학습은 자료에서 규칙을 배워 예측이나 결정을 수행하는 계산 방법이다. 중심 질문은 학습하는 시스템이 효과적으로 판단하면서도 안정성, 강건성, 안전성과 효율을 어떻게 지킬 수 있느냐는 것이다. 안정성은 작은 변화가 생겼을 때 시스템의 상태가 기준 상태에서 크게 벗어나지 않는 성질이고, 강건성은 외부 영향이나 모형의 오차가 있어도 요구하는 동작을 유지하는 성질이다.[^home][^research]

이론 연구는 Q학습(각 상태에서 행동을 택한 뒤 얻을 보상 합의 추정값을 경험으로 갱신하는 강화학습 방법)과 시간차 학습(Temporal-Difference Learning, 뒤 시점의 가치 추정값과 현재 추정값의 차이를 이용해 가치를 갱신하는 방법)을 다룬다. 상태와 행동마다 값을 따로 저장하는 경우뿐 아니라 함수 근사(관계식의 매개변수로 여러 상태의 값을 함께 표현하는 방법)를 쓰는 경우도 분석한다. 갱신을 반복하면 목표 값에 가까워지는지, 정해진 갱신 횟수 뒤 오차는 어느 범위에 있는지, 필요한 경험 자료는 얼마나 되는지를 묻는다.[^research][^p1][^p2]

학습 기반 제어에서는 측정값을 바탕으로 시스템에 줄 입력을 정하는 제어 이론과 학습 알고리즘을 연결해 제어기를 설계하고 안정성을 분석한다.[^control] 외부 교란(의도한 입력과 별개로 시스템에 작용하는 영향), 모형의 불확실성, 위험한 행동을 시험하는 문제를 설계에 반영한다. 리아푸노프 방법(시스템의 상태를 나타내는 함수가 시간에 따라 어떻게 변하는지로 안정성을 판단하는 방법)을 비롯한 수학적 도구로 학습과 제어가 요구하는 성질을 따진다.[^research]

연구 소개는 최근 협업 사례로 로봇의 위치 추정·지도 작성, 자율주행의 주변 인식과 판단, 산업 가열 공정의 온도 제어, 그래픽 처리 장치 서버의 전력 관리를 든다. 또 로봇의 카메라 시점 선택, 공정 제어, 이미 모인 기록으로 배우는 방법을 이론과 실제 시스템을 연결하는 대상으로 든다.[^research] 대표 사례로 사람이 보여 준 행동을 활용해 로봇의 시각적 위치 추적 실패를 줄이는 연구와, 산업용 가열기의 가열 단계에 따라 학습 제어 방식을 달리하는 연구가 있다.[^p7][^p8]

## 주요 연구 주제

### 강화학습의 오차와 안정성 분석

Q학습의 갱신 규칙을 전환 시스템(상황에 따라 적용되는 동작 방정식이 바뀌는 시스템)으로 표현하고, 학습 오차가 어떻게 변하는지 분석한다. 평균낸 갱신값뿐 아니라 마지막 갱신값의 오차를 다룬다.[^p2] 시간차 학습에서는 선형 함수 근사와 비정책 학습(행동을 정해 자료를 모은 방법과 평가하려는 행동 방법이 다른 학습)을 함께 사용할 때의 안정성을 분석하는 틀과 새로운 갱신 방법을 연구한다.[^p5]

### 분산 학습과 오프라인 학습

여러 에이전트(환경의 정보를 받아 행동을 선택하는 주체)가 각자의 정보로 판단하면서 정보를 나누는 분산 강화학습과 다중 에이전트 게임을 연구하고, 학습의 오차와 필요한 자료량에 관한 수학적 보장을 다룬다.[^home][^research] 대표 논문은 통신으로 연결된 여러 학습자가 함께 가치를 평가하는 시간차 학습을 분석한다.[^p3] 오프라인 강화학습(환경과 추가로 상호작용하지 않고 이미 모인 자료에서 행동 방법을 배우는 강화학습)에서는 다음 상태와 행동 가치를 함께 예측하도록 학습망을 미리 훈련해, 적은 자료로 학습하는 방법을 다룬다.[^p4]

### 안전성과 강건성을 고려한 학습·제어

학습 중 위험한 행동을 피하는 탐색, 외부 교란을 줄이는 제어, 안정성을 뒷받침하는 수학적 조건을 연구한다.[^research] 퍼지 시스템(상황별 규칙이 어느 정도 적용되는지를 가중치로 나타내 결합하는 시스템)을 다룬 대표 논문은 상태와 규칙 가중치에 함께 의존하는 리아푸노프 함수를 제안한다. 이를 이용해 측정 가능한 출력으로 입력을 정하는 제어기를 설계하고, 안정적으로 제어할 수 있는 초기 상태의 영역을 추정한다.[^p6]

### 자율 시스템과 산업 공정의 의사결정

연구 소개는 자율주행의 인식·판단과 로봇의 시각적 위치 추적 신뢰성을 협업 사례로 든다.[^application] 로봇 연구에서는 무늬가 적은 벽이나 방의 출입구를 지날 때 카메라가 어디를 보아야 위치 추적을 이어갈 수 있는지 다룬다.[^p7] 산업 공정 연구에서는 가열 초기에 전력을 직접 정하는 학습과 가열 후기에 기존 제어기의 조정값을 정하는 학습을 결합해 온도를 제어한다.[^p8]

## 대표 논문

KAIST 재직 시기의 논문 가운데 강화학습 이론, 분산·오프라인 학습, 안정성과 제어, 로봇·산업 응용을 고르게 보여 주는 논문을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 교신저자 표시는 연구실 논문 목록의 별표 표기다.[^pub]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자와 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [TD-Learning and Q-Learning: A Survey of Theory, Analysis, and Trends](https://doi.org/10.1007/s12555-026-00161-z) · International Journal of Control, Automation, and Systems | 시간차 학습과 Q학습이 언제 목표 값에 가까워지는지 설명한 이론을 정리한 리뷰다. 값을 표로 저장하는 경우, 선형 함수로 표현하는 경우, 신경망으로 표현하는 경우를 구분한다. 신경망은 연결된 계산 단위와 연결 강도를 조정해 입력과 출력의 관계를 배우는 모형이다. 오래 갱신했을 때의 성질과 제한된 자료·갱신 횟수에서의 오차를 함께 검토하고, 안정화를 위한 기존 방법과 남은 이론적 과제를 정리한다.[^p1] | 1저자 Han-Dong Lim, 마지막·교신저자 이동환 |
| 2 | 2024 | [Final Iteration Convergence Bound of Q-Learning: Switching System Approach](https://doi.org/10.1109/tac.2024.3355326) · IEEE Transactions on Automatic Control | Q학습에서 여러 갱신값을 평균내는 대신 마지막 갱신값 자체가 얼마나 정확한지 분석한다. 학습을 확률적인 전환 시스템으로 보고, 정해진 횟수 뒤 마지막 갱신값의 오차 상한을 도출한다. 여러 조건을 다루며 Q학습과 전환 시스템 사이의 연결을 설명한다.[^p2] | 단독 저자 이동환 |
| 3 | 2025 | [A Primal-dual Perspective for Distributed TD-learning](https://doi.org/10.24963/ijcai.2025/634) · IJCAI 2025 | 통신으로 연결된 여러 학습자의 시간차 학습을 분산 최적화 관점에서 분석한다. 최적화는 주어진 조건 안에서 목표 값을 가장 크게 하거나 작게 하는 값을 찾는 일이다. 갱신 크기가 일정한 경우와 줄어드는 경우, 관측 자료가 서로 독립적인 경우와 이전 상태에 영향을 받는 경우를 다룬다. 특정한 통신 가중치 행렬의 가정 없이 마지막 갱신값의 동작을 분석한다.[^p3] | 1저자 Han Dong Lim, 마지막 저자 이동환 |
| 4 | 2025 | [Pretraining a Shared Q-Network for Data-Efficient Offline Reinforcement Learning](https://doi.org/10.52202/085713-4350) · NeurIPS 2025 | 다음 상태와 행동 가치를 함께 예측하는 공유 학습망을 만들고, 다음 상태를 예측하는 과제로 먼저 훈련한다. 이렇게 준비한 학습망을 여러 오프라인 강화학습 방법에 결합한다. 여러 시험 자료에서 기존 방법의 성능과 자료 효율이 개선되는지 확인하고, 자료의 품질과 분포가 달라지는 경우도 평가한다.[^p4] | 1저자 Jong-Chan Park, 마지막·교신저자 이동환 |
| 5 | 2023 | [New Versions of Gradient Temporal-Difference Learning](https://doi.org/10.1109/tac.2022.3213763) · IEEE Transactions on Automatic Control | 선형 함수 근사와 비정책 학습을 함께 사용할 수 있는 기울기 시간차 학습의 변형들을 제안한다. 기울기는 입력의 변화에 따라 함수값이 바뀌는 방향과 정도를 나타낸다. 여러 변형을 공통된 수학적 틀로 해석하고, 그 틀에서 안정성을 분석한다. 수치 비교로 제안한 방법들을 평가한다.[^p5] | 1저자 이동환, 뒤이어 Han-Dong Lim·Jihoon Park·Okyong Choi |
| 6 | 2026 | [Regional Output-Feedback Control for T--S Fuzzy Systems Using Lyapunov Functions With Polynomial Dependency on States and Membership Functions](https://doi.org/10.1109/tsmc.2026.3692406) · IEEE Transactions on Systems, Man, and Cybernetics: Systems | 연속적으로 변하는 퍼지 시스템을 측정 가능한 출력으로 제어하는 문제를 다룬다. 시스템 상태와 규칙 가중치에 함께 의존하는 새로운 리아푸노프 함수를 사용해 안정성 조건과 제어기 설계 조건을 만든다. 먼저 상태가 줄어드는 속도를 조정하고, 그 속도를 고정한 뒤 안정적으로 제어할 수 있는 초기 상태 영역을 넓히는 계산 절차를 제안한다.[^p6] | 1저자 Yara Quilles Marinho, 중간 저자 이동환 |
| 7 | 2025 | [Help Me Through: Imitation Learning Based Active View Planning to Avoid SLAM Tracking Failures](https://doi.org/10.1109/tro.2025.3582817) · IEEE Transactions on Robotics | 로봇이 방을 드나들거나 무늬가 적은 벽을 지날 때 시각적 위치 추적에 실패하는 문제를 다룬다. 이런 구간을 통과하지 못하면 필요한 행동을 배우기 어렵다는 점을 분석하고, 사람이 지도하는 학습으로 카메라의 시점 선택을 훈련한다. 사람의 지도 뒤 추가 학습으로 조정하는 방법도 시험하고, 어려운 전환 구간을 담은 학습 자료를 공개한다.[^p7] | 1저자 Kanwal Naveed, 중간 저자 이동환 |
| 8 | 2026 | [High-Precision Temperature Control in Industrial Evaporation Heaters via Hybrid Reinforcement Learning Approach](https://doi.org/10.1109/access.2026.3724687) · IEEE Access | 디스플레이 제조의 증발 공정에서 가열기 온도를 제어한다. 운전 자료로 만든 가열 시뮬레이터에서 학습한 뒤, 초기에는 전력을 직접 정하고 후기에는 기존 제어기의 조정값을 정하는 두 학습기를 결합한다. 시뮬레이터와 실제 가열 시스템에서 안정적인 온도 제어를 확인하고, 기존 제어 방식과 지연·목표 온도를 넘는 정도·안정된 온도에 이르는 시간을 비교한다.[^p8] | 1저자 Bumgeun Park, 마지막·교신저자 이동환 |

## 교수와 전문 분야

이동환 부교수는 건국대학교 전기공학 학사, 연세대학교 전기공학 석사, Purdue University 수학 석사와 전기·컴퓨터공학 박사 학위를 받았다. 2017–2020년 University of Illinois Urbana-Champaign의 Coordinated Science Laboratory에서 박사후연구원으로 일했다. 교수 소개는 KAIST 전기및전자공학부 조교수 경력을 2020–2025년, 부교수 경력을 2026년부터로 적고, 로봇공학 학제전공 겸임교수 경력을 2020년부터로 적는다. 구성원 쪽의 교수 시작 표기는 2020년 3월이다.[^pi][^people] 학부 교수 소개의 직위는 부교수다.[^dept]

최근 논문으로 본 전문 분야는 강화학습의 수학적 분석과 제어 이론의 연결이다. Q학습의 마지막 갱신값에 대한 오차 분석,[^p2] 여러 학습자가 연결된 시간차 학습,[^p3] 함수 근사를 쓰는 학습의 안정성 분석[^p5]이 이를 보여 준다. 퍼지 시스템의 제어기 설계[^p6]와 산업용 가열기의 학습 제어[^p8]는 안정성을 분석하는 수학적 방법을 실제 제어 문제에 연결한 사례다.

## 응용 분야

연구실은 로봇·드론·자율 시스템, 자율주행의 인식·판단·제어, 산업 공정·에너지·컴퓨팅 시스템을 응용 영역으로 든다. 학술·공공·산업 파트너와 알고리즘 설계, 수학적 분석, 모의실험, 실제 플랫폼이나 운전 자료를 이용한 공동 검증을 협업 방식으로 제시한다.[^collab][^research] 논문에서 다룬 구체적인 대상은 로봇의 카메라 시점 선택[^p7]과 디스플레이 제조용 가열기의 온도 제어[^p8]다.

## 구성원

2026년 11월 9일 연구실 People 쪽에 게시된 박사과정 9명, 공동지도 학생 1명, 박사후연구원 1명이다. 공동지도 학생의 과정은 별도로 적혀 있지 않아 공동지도 표기를 그대로 둔다. 이름·시작·연구 주제는 누리집 표기다.[^people] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Hyunjun Na | 박사과정 | 2022.03~ | Reinforcement learning theory and convergence | 1 |
| Seohyun Jeon | 박사과정 | 2022.09~ | Reinforcement learning, robotics |  |
| Jin Woo Kim | 박사과정 | 2024.03~ | Reinforcement learning, autonomous driving, and perception |  |
| Han Dong Lim | 박사과정 | 2021.03~ | Reinforcement-learning theory and convergence | 3 |
| Bum Geun Park | 박사과정 | 2024.03~ | Reinforcement learning |  |
| Narim Jeong | 박사과정 | 2023.03~ | Reinforcement learning | 8 |
| Taeho Lee | 박사과정 | 2023.03~ | Reinforcement learning | 1 |
| Hyukjun Yang | 박사과정 | 2024.03~ | Reinforcement learning, offline RL | 8 |
| Hayeon Oh | 박사과정 | 2026.09~ | Large language models and perception |  |
| Jongeui Park | 공동지도 학생(성영철 교수와 공동) |  | Reinforcement learning |  |
| Yara Quilles Marinho | 박사후연구원 | 2024.09~ | Reinforcement learning, nonlinear systems,  and fuzzy systems | 6 |

## 졸업생과 이전 방문자

연구실 People의 졸업생 구획에 게시된 14명이다. 학위과정 졸업생뿐 아니라 이전 연구원과 방문 학생도 포함하며, 괄호 안 기간과 진로는 누리집 표기다. 석사 졸업 뒤 같은 연구실 박사과정을 이어가는 사람은 현재 구성원에도 나온다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyukjun Yang | M.S. alumnus (2024.03~2026.02) | continuing as a Ph.D. student in the lab |
| Heechan Chung | M.S. alumnus (2023.09~2025.08) |  |
| Taeho Lee | M.S. alumnus (2023.03~2025.02) | continuing as a Ph.D. student in the lab |
| Narim Jeong | M.S. alumnus (2023.03~2025.02) | continuing as a Ph.D. student in the lab |
| HyeAnn Lee | M.S. alumnus (2023.03~2025.02) | SANSUNG Research |
| Jong-Chan Park | M.S. alumnus (2023.09~2025.02) | Hyundai Motor Company |
| Yeeun Lim | M.S. alumnus (2023.03~2025.02) | HD Korea Shipbuilding & Offshore Engineering |
| Mingyu Park | M.S. alumnus (2023.03~2025.02, ETRI) | ETRI |
| Kihong Park | M.S. alumnus (MS 2022.03-2024.02) | LIG Nexone |
| Hoang T. Nguyen | researcher (2023.06~2024.06) | Ph.D. at MIT EE |
| Yara Quilles Marinho | visiting student (2023.03~2023.09) | UNICAMP, Brazil |
| Han Dong Lim | M.S. alumnus (M.S. 2021.03-2023.02) | continuing as a Ph.D. student in the lab |
| Okyong Choi | M.S. alumnus (M.S. 2020.8-2022.8) | Shinhan Bank Research Team |
| Jihoon Park | M.S. alumnus (MS 2021.3-2023.2) |  |

## 최근 5년 논문 목록

연구실 Publication의 2022–2026년 연도 구역에 게시된 논문 58편이다. 이 목록은 교수의 개인 논문 목록으로, 누리집에는 KAIST 부임 전 논문도 함께 게시되어 있다. 아래에는 2021–2026년 연도 구역의 항목을 싣는다. 저자 이름·논문 제목·발표처와 연도 구역은 누리집 표기이며, 같은 논문의 등록 서지로 확인되는 DOI를 함께 적었다. 누리집은 별표를 교신저자 표시로 설명한다. 2026년 학회 항목은 누리집 기재 연도·발표처를 따르며, 학회 이름만으로 발표 완료를 뜻하지 않는다.[^pub]

**2026**

- Hayeon Oh, Donghwan Lee\*, "Teaching VLMs what to say, not what to see: the role of counterfactual reasoning in autonomous driving," NeurIPS2026.
- Donghwan Lee, Hyukjun Yang, "Bellman residual minimization for control: geometry, stationarity, and convergence," NeurIPS2026.
- Min-Gyu Park, Samyeul Noh, Hyun Myung\*, Donghwan Lee\*, "VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning," NeurIPS2026.
- Bum Geun Park, Donghwan Lee\*, Explore beyond the boundary using entropic information," RiTA2026.
- Bum Geun Park, Narim Jeong, Hyukjun Yang, Donghwan Lee\*, High-precision temperature control in industrial evaporation heaters via hybrid reinforcement learning approach, IEEE Access, 2026. DOI: 10.1109/access.2026.3724687.
- Hyukjun Yang, Han-Dong Lim, Donghwan Lee\*, "Contraction-aligned analysis of soft Bellman residual minimization with weighted Lp-norm for Markov decision problem," CDC2026.
- Han-Dong Lim, Hyeann Lee, Donghwan Lee\*, "Learning the model while learning Q: finite-time sample complexity of online SyncMBQ" CDC2026.
- Han-Dong Lim, Hyunjun Na, Taeho Lee, Donghwan Lee\*, "TD learning and Q-learning: a survey of theory, analysis, and trends," International Journal of Control, Automation, and Systems (IJCAS), 2026. DOI: 10.1007/s12555-026-00161-z.
- Bum Geun Park, Donghwan Lee\*, Adaptive policy backbone via shared network, ICML2026.
- Taeho Lee, Donghwan Lee\*, "Robust deterministic policy gradient for disturbance attenuation and its application to quadrotor control," IFAC world congress 2026.
- Yara Q. Marinho, Donghwan Lee, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, "Homogeneous rational Lyapunov functions for stability analysis of continuous-time Takagi-Sugeno fuzzy systems," IFAC world congress, 2026.
- Donghwan Lee, Hyukjun Yang, Bum Geun Park, "Analysis of approximate linear programming solution to Markov decision problem with log barrier function," ICLR 2026.
- Hyunjun Na, Donghwan Lee\*, "Finite-time analysis of simultaneous double Q-learning," Neurocomputing, 2026.
- Bum Geun Park, Taeho Lee, Donghwan Lee\*, "Deep Q-learning with gradient target tracking," IEEE Access.
- Yara Q. Marinho, Donghwan Lee, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, "Regional output-feedback control for T-S fuzzy systems using Lyapunov functions with polynomial dependency on states and membership functions," IEEE Transactions on System, Man, and Cybernetics, 2026. DOI: 10.1109/tsmc.2026.3692406.
- Yara Q. Marinho, Donghwan Lee, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, "Regional stabilization and estimation of domains of attraction for discrete-time T-S fuzzy Systems via fuzzy-modeled membership functions," IEEE Transactions on Fuzzy Systems, 2025. DOI: 10.1109/tfuzz.2025.3650219.

**2025**

- Jong-Chan Park, Min-Gyu Park, Donghwan Lee\*, "Pretraining a shared Q-network for data-efficient offline reinforcement learning," NeurIPS2025. DOI: 10.52202/085713-4350.
- Han-Dong Lim, Donghwan Lee\*, "A primal-dual perspective for distributed TD-learning," IJCAI2025. DOI: 10.24963/ijcai.2025/634.
- Kanwal Naveed, Wajahat Hussain, Irfan Hussain, Donghwan Lee, Muhammad Latif Anjum , "Help me through: imitation learning based active view planning to avoid SLAM tracking failures," IEEE Transactions on Robotics, 2025. DOI: 10.1109/tro.2025.3582817.
- Narim Jeong, Donghwan Lee,\* "Unified finite-time error analysis of soft Q-learning," Neurocomputing, 2025.
- Narim Jeong, Donghwan Lee\*, "Finite-time analysis of minimax Q-learning," RLC2025, RLJ2025 .
- Han-Dong Lim, Donghwan Lee\*, "A finite-time analysis of distributed Q-learning" RLC2025, RLJ2025.
- Jinwoo Kim, Hayeon O, Yongmin Oh, Kyounghwan An, Donghwan Lee, "SADWA: fine-grained weather awareness with vision-language models for seamless autonomous driving in real time," ICCV2025 Workshop. .
- Heechan Chung, Yeeun Im, Jongchan Park, Taeho Lee, Tae-Young Kim, Hyungjun Kim, and Donghwan Lee\*, "Power consumption optimization of GPU server with offline reinforcement learning," IEEE Access 2025. DOI: 10.1109/access.2025.3569803.
- Yara Q. Marinho, Donghwan Lee\*, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, " Harnessing membership function dynamics for stability analysis of discrete-time T-S fuzzy systems," IEEE Control Systems Letters, 2025.
- Yara Q. Marinho, Donghwan Lee\*, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, " Harnessing membership function dynamics for stability analysis of discrete-time T-S fuzzy systems," IEEE CDC 2025.
- Yara Q. Marinho, Donghwan Lee\*, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, " Harnessing membership function dynamics for output-feedback stabilization of T-S fuzzy systems," IEEE International Conference on Fuzzy Systems, 2025. DOI: 10.1109/fuzz62266.2025.11152283.
- Moon Hwan Kim, Do Wan Kim, Donghwan Lee, "Three-dimensional path following control of nonlinear autonomous underwater vehicles with actuator saturation", Ocean Engineering, 2025. DOI: 10.1016/j.oceaneng.2024.119966.
- Do Wan Kim, Donghwan Lee\*, "Relaxed conditions for parameterized linear matrix inequality in the form of nested fuzzy summations", Applied Mathematics and Computation, vol. 487, 2025. DOI: 10.1016/j.amc.2024.129079.

**2024**

- Han-Dong Lim,  Donghwan Lee\*, "Regularized Q-learning," NeurIPS2024. DOI: 10.52202/079017-4125.
- Han-Dong Lim, Donghwan Lee\*, "Finite-time analysis of asynchronous  Q-learning under diminishing step-size from control-theoretic view" IEEE Access 2024. DOI: 10.1109/access.2024.3476564.
- Han-Dong Lim, Donghwan Lee\*, "Finite-time analysis of temporal difference learning with experience replay," Transactions on Machine Learning Research (TMLR), 2024.
- Hyeann Lee, Donghwan Lee\*, "Suppressing overestimation in Q-learning through adversarial behaviors," Annual Allerton Conference on Communication, Control, and Computing, 2024. DOI: 10.1109/allerton63246.2024.10735317.
- Narim Jeong, Donghwan Lee\*, "Finite-time error analysis of soft Q-learning: switching system approach," IEEE CDC2024.
- Donghwan Lee, "Analysis of off-policy multi-step TD-learning with linear function approximation," IEEE CDC2024. DOI: 10.1109/cdc56724.2024.10886545.
- Donghwan Lee, "Final iteration convergence bound of Q-Learning: switching system approach," IEEE Transactions on Automatic Control, vol. 69, no. 7, 2024. DOI: 10.1109/tac.2024.3355326.
- Donghwan Lee, "Lossless convexification and duality," Journal of the Franklin Institute, vol. 361, no. 14, 2024. DOI: 10.1016/j.jfranklin.2024.107084.
- Donghwan Lee, Han-Dong Lim, and Do Wan Kim, "Continuous-time distributed dynamic programming for networked multi-agent Markov decision processes," IEEE ICCA2024, Iceland. DOI: 10.1109/icca62789.2024.10591854.
- Donghwan Lee, Do Wan Kim, "On the local quadratic stability of T-S fuzzy systems in the vicinity of the origin," Fuzzy Sets and Systems, vol. 497, 2024. DOI: 10.1016/j.fss.2024.109113.
- Donghwan Lee, Do Wan Kim, "Harnessing membership function dynamics for stability analysis of T-S fuzzy systems" Information Science, vol. 681, 2024. DOI: 10.1016/j.ins.2024.121236.
- Jianghai Hu, Jinglai Shen, Donghwan Lee, "Optimal stabilizing rates of switched linear control systems under arbitrary known switchings," Automatica, vol. 159, 2024. DOI: 10.1016/j.automatica.2023.111331.
- Kanwal Naveed, Wajahat Hussain, Irfan Hussain, Donghwan Lee, Muhammad Latif Anjum, "Deeper introspective SLAM: how to avoid tracking failures over longer routes?," IROS2024, October 14-18, Abu Dhabi, UAE, 2024. DOI: 10.1109/iros58592.2024.10801911.
- Jinwoo Kim, Kyounghwan An, Donghwan Lee, RoSA Dataset: Road construct zone Segmentation for Autonomous Driving, ECCV 2024 W-CODA Workshop 2024. DOI: 10.1007/978-3-031-91767-7_22.
- Yara Q. Marinho, Donghwan Lee, Ricardo C. L. F. Oliveira, Pedro L. D. Peres, "Local stability analysis and estimation of domains of attraction for discrete-time Takagi-Sugeno fuzzy systems via fuzzy-modeled membership functions," ACC2024 , July 10-12, 2024, Toronto, Canada. DOI: 10.23919/acc60939.2024.10644856.
- Mingyu Park, Donghwan Lee\*, "A combination of dueling architecture with alternative smooth max operator in reinforcement learning," KCC2024, South Korea, 2024.
- Heechan Chung, Taeho Lee, Jongchan Park, Yeeun Lee, Tae-Young Kim, Hyungjun Kim, Donghwan Lee\*, "Optimizing power consumption of GPU server by reinforcement learning algorithms," KCC2024, SouthKorea, 2024.

**2023**

- Han-Dong Lim, Donghwan Lee\*, "Backstepping temporal-difference learning," ICLR2023, Kigali, Rwanda, May 1-5, 2023.
- Donghwan Lee, Jianghai Hu, and Niao He, “A discrete-time switching system analysis of Q-learning,”  SIAM Journal on Control and Optimization, vol. 61, no. 3, 2023. DOI: 10.1137/22m1489976.
- Donghwan Lee, Han-Dong Lim, Jihoon Park, and Okyong Choi, "New versions of gradient temporal-difference learning," IEEE Transactions on Automatic Control, vol. 68, no. 8, 2023. DOI: 10.1109/tac.2022.3213763.
- Donghwan Lee and Do Wan Kim, "Data-driven control design with LMIs and dynamic programming," IEEE Access, vol. 11, 2023. DOI: 10.1109/access.2023.3241926.
- Donghwan Lee, "Multi-objective LQG design with primal-dual method," mathematics, vol. 11, no. 8, 2023. DOI: 10.3390/math11081857.
- Donghwan Lee, "On some geometric behaior of value iteration on the orthant: switching system perspective," CDC2023, Dec. 13-15, 2023, Singapore. DOI: 10.1109/cdc49753.2023.10383253.
- Do Wan Kim, Donghwan Lee\*, "Relaxed conditions for parameterized linear matrix inequality in the form of double sum" IEEE Transactions on Fuzzy Systems, vol. 32, no. 3, 2023.

**2022**

- Donghwan Lee, "Convergence of dynamic programming on the semidefininte cone for discrete-time infinite-horizon LQR," IEEE Transactions on Automatic Control, vol. 67, no. 10, 2022. DOI: 10.1109/tac.2022.3181752.
- Donghwan Lee, Do Wan Kim, Jianghai Hu, "Distributed off-policy temporal difference learning using primal-dual method," IEEE Access, vol. 10, 2022. DOI: 10.1109/access.2022.3211395.
- Donghwan Lee and Do Wan Kim "Formulations for data-driven control design and reinforcement learning," ICCA2022, June 27-30, 2022, Naples, Italy. DOI: 10.1109/icca54724.2022.9831901.
- Kanwal Naveed, Muhammad Latif Anjum, Wajahat Hussain, Donghwan Lee, "Deep introspective SLAM: deep reinforcement learning based approach to avoid tracking failure in visual SLAM," Autonomous Robots, vol. 46, 2022. DOI: 10.1007/s10514-022-10046-9.
- Junmo Cho, Donghwan Lee, Young-Gyu Yoon, ``Inducing functions through reinforcement learning without task specification,'' NeurIPS2023 workshop, 2022.

## 수상과 선정

연구실 첫 화면과 논문 목록의 2025년 수상 1건이다. 연도는 누리집의 연도 구역과 학회 연도 표기이고 날짜는 게시되어 있지 않다.[^home][^pub]

- 2025 · 「SADWA: fine-grained weather awareness with vision-language models for seamless autonomous driving in real time」의 ICCV2025 Workshop Best Paper Award 수상

## 소식

연구실 첫 화면의 2025년 논문 채택 소식 1건이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^home]

- 2025 · 「Pretraining a Shared Q-Network for Data-Efficient Offline Reinforcement Learning」이 NeurIPS 2025에 채택되었다.

## 연락과 위치

- 교수 업무 이메일: donghwan@kaist.ac.kr.[^collab]
- 학부 교수 소개의 위치: IT융합빌딩(N1) 307호.[^dept]
- 학부 교수 소개의 연락처 표기: 7462.[^dept]

## 각주
[^home]: 연구실 첫 화면, 연구실 이름·연구 소개·소식. <https://sites.google.com/site/donghwanleehome> 관측일 2026-11-09.
[^research]: 연구실 Research, 연구 갈래와 방법. <https://sites.google.com/site/donghwanleehome/research> 관측일 2026-11-09.
[^control]: 연구실 Research의 Safe and Robust Learning-Based Control, 제어 방법 개발과 안정성 분석. <https://sites.google.com/site/donghwanleehome/research> 관측일 2026-11-09.
[^application]: 연구실 Research의 Autonomous and Industrial Intelligence, 자율주행과 로봇 위치 추적을 위한 의사결정 연구. <https://sites.google.com/site/donghwanleehome/research> 관측일 2026-11-09.
[^collab]: 연구실 Collaboration, 협업 영역·교수 업무 이메일. <https://sites.google.com/site/donghwanleehome/collaboration> 관측일 2026-11-09.
[^pub]: 연구실 Publication, 논문 목록·저자 표시·수상. <https://sites.google.com/site/donghwanleehome/publication> 관측일 2026-11-09.
[^people]: 연구실 People, 구성원·졸업생·교수 시작 시점. <https://sites.google.com/site/donghwanleehome/people> 관측일 2026-11-09.
[^pi]: 연구실 PI, 교수 학력·경력·전문 분야. <https://sites.google.com/site/donghwanleehome/pi> 관측일 2026-11-09.
[^dept]: KAIST 전기및전자공학부 이동환 교수 소개, 직위·연구실·연락과 위치. <https://ee.kaist.ac.kr/professor/17375/> 관측일 2026-11-09.
[^p1]: H.-D. Lim, H. Na, T. Lee, D. Lee, International Journal of Control Automation and Systems (2026). <https://doi.org/10.1007/s12555-026-00161-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p2]: D. Lee, IEEE Transactions on Automatic Control 69 (2024). <https://doi.org/10.1109/tac.2024.3355326> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p3]: H. D. Lim, D. Lee, International Joint Conference on Artificial Intelligence (2025). <https://doi.org/10.24963/ijcai.2025/634> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p4]: J.-C. Park, M. Park, D. Lee, NeurIPS (2025). <https://doi.org/10.52202/085713-4350> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p5]: D. Lee, H.-D. Lim, J. Park, O. Choi, IEEE Transactions on Automatic Control 68 (2023). <https://doi.org/10.1109/tac.2022.3213763> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p6]: Y. Q. Marinho, D. Lee, R. C. L. F. Oliveira, P. L. D. Peres, IEEE Transactions on Systems Man and Cybernetics Systems (2026). <https://doi.org/10.1109/tsmc.2026.3692406> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p7]: K. Naveed 외, M. L. Anjum, IEEE Transactions on Robotics (2025). <https://doi.org/10.1109/tro.2025.3582817> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.
[^p8]: B. Park 외, D. Lee, IEEE Access (2026). <https://doi.org/10.1109/access.2026.3724687> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100654317>의 해당 DOI 등록 초록. 관측일 2026-11-09.

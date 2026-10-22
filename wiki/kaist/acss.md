# ACSS 연구실 (Autonomous Control for Stochastic Systems Lab)

**KAIST 전기및전자공학부 · 한수진 교수**

- 분야: 확률 제어, 불확실성 아래의 자율 의사결정, 생성형 AI로 하는 안전한 경로 계획, 대규모 네트워크·다중 에이전트 시스템의 분산 제어와 상태 추정, 데이터 효율적 학습과 적응 제어, 강화학습
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 로봇 항법·SLAM[^modals][^p1][^p2], 생성 인공지능[^modals][^p1], 강화학습[^about][^p6]
- 홈페이지: <http://acss.kaist.ac.kr>
- 근거와 출처: [ACSS 연구실 근거 페이지](acss-sources.md)

> 정전, 지연, 예측하기 어려운 보행자와 차량처럼 현실 곳곳에 있는 불확실성 속에서도 로봇과 자율 시스템이 안전하고 믿을 만하게 판단하고 움직이도록, 제어 이론과 최적화를 최신 인공지능과 결합하는 연구실이다.[^about]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 한수진 교수가 이끄는 Autonomous Control for Stochastic Systems(ACSS) 연구실이다.[^ee][^home] 연구실 소개는 현실 세계 곳곳에 불확실성이 있다는 데서 출발한다. 집에서 갑자기 정전이 나고, 항공편·택배·이메일이 늦어지며, 출퇴근길에는 행동을 예측하기 어려운 보행자·자전거·차량이 함께 다닌다. 그래도 사람은 불완전한 예측 속에서 적응하고 계획하며 믿을 만한 결정을 내리므로, 사이버물리 시스템(컴퓨터 계산과 물리 장치가 맞물려 움직이는 시스템)과 로봇 같은 자율 시스템의 제어·의사결정 방법도 같은 원리를 따라야 한다고 적는다.[^about]

소개는 기술 배경도 설명한다. 확률 과정과 확률 미분방정식(무작위 요소가 들어간 미분방정식) 같은 확률 개념은 무작위 현상의 영향을 받는 시스템을 모델링하는 핵심 수학 도구다. 이런 모델 기반 방법은 해석할 수 있고 이론적으로 정립되어 있어 안정성·안전성·강인성(외란이나 오차가 있어도 성능을 지키는 성질)을 보장할 수 있지만, 실제의 많은 불확실한 시스템은 정확히 모델링하기에 너무 복잡하다. 그래서 인공지능 같은 데이터 기반, 곧 모델 없이(모델 프리) 배우는 방법이 주목받지만, 이 방법은 좋은 데이터와 많은 계산이 필요하고 해석이 어려워 안정성·안전성을 인증하기 어렵다. 연구실은 두 방법 사이를 연구해 모델 프리 방법의 유연성과 모델 기반 방법의 구조·신뢰성·인증 가능성을 결합하는 것을 목표로 한다.[^about]

연구실은 제어 이론, 최적화, 최신 인공지능 도구를 결합해 확률적 자율 시스템을 위한 구조적이고 데이터 효율적인 의사결정 알고리즘을 개발하고, 이 알고리즘이 안전성·안정성·강건성과 불확실성 아래에서의 믿을 만한 적응에 대한 이론적 보장을 유지하게 한다고 밝힌다. 특히 데이터가 적고, 모델이 실제와 맞지 않고, 고장이나 분포 밖(OOD, 학습 때 보지 못한 범위) 거동이 나타나는 현실의 자율성에 관심을 두며, 응용으로 동작 계획, 분포 변화와 OOD 거동, 강화학습(시행착오로 보상을 가장 크게 하는 행동을 배우는 기계학습), 다중 에이전트·네트워크 시스템, 체화된 AI(몸을 가진 기계가 환경 속에서 보고 움직이며 판단하는 인공지능)를 든다.[^about] Research 절은 연구를 불확실한 환경·시스템 아래의 자율 의사결정, 적응형 자율성을 위한 데이터 효율적 학습, 네트워크·다중 에이전트 시스템을 위한 대규모 제어의 세 갈래로 나눈다.[^research] 교수 개인 누리집은 연구 관심을 확률 최적 제어 이론과 학습 기반 적응형 의사결정이 만나는 곳으로 소개하고, 성능·안정성·강건성을 엄밀히 보장하는 방법에 중점을 둔다고 적는다.[^pihome]

대표 논문으로 보면 연구는 세 갈래로 모인다. 첫째, 생성형 AI로 경로를 만들되 안전을 보장하고, 위험한 장애물에 예측 계산을 몰아주는 경로 계획이다(대표 논문 1, 2).[^p1][^p2] 둘째, 동작 방식이 확률적으로 바뀌는 대규모 네트워크 시스템을 안정시키고 상태를 분산 추정하며 센서 일정을 정하는 연구와, 신호등 혼잡 제어를 다중 에이전트 강화학습으로 다룬 연구다(대표 논문 3–6).[^p3][^p4][^p5][^p6] 셋째, 데이터로 비선형 동역학의 장기 예측 모델을 배우고, 정해진 확률 이상으로 안전 조건을 지키는 데이터 기반 예측 제어를 만드는 연구다(대표 논문 7, 8).[^p7][^p8]

## 주요 연구 주제

### 1. 불확실한 환경에서 안전하게 계획하는 생성형 AI

로봇 계획 문제에서 확산 모델·흐름 정합 같은 생성형 AI는 컵을 여러 다른 위치에서 집는 로봇 팔처럼 여러 갈래의 행동을 표현할 수 있지만, 이 유연성은 폐루프 제어(결과를 다시 측정해 다음 조작에 반영하는 제어)에 꼭 필요한 안전·안정성 보장과 부딪친다. 연구실은 여러 갈래의 유연성을 잃지 않으면서 안전·안정성 제약을 담는 생성형 AI 계획 알고리즘을 개발하며, 계층형 안전 필터와 분포 제어 정식화를 연구한다. 또 시간에 따라 성질이 바뀌는 불확실성에 견고하고 적응적인 경로 계획기를 모델 기반 방법과 데이터 기반 방법을 결합해 만들고, 집합 예측·전파, 학습 기반 OOD 탐지기, 온라인 강화학습을 쓴다.[^modals] 대표 논문 1, 2.

### 2. 대규모 네트워크·다중 에이전트 시스템의 제어와 상태 추정

확률 제어와 상태 추정 알고리즘을 대규모로 구현하면 네트워크 연결 구조가 바뀌거나 에이전트 사이 정보 전달이 늦어지는 불확실성, 통신 대역폭이 제한되고 에이전트끼리 조율이 부족한 제약이 더해진다. 연구실은 고차원 네트워크 불확실성에 견고하고 적응적이며 규모를 키울 수 있는 분산·탈중앙 확률 제어와 상태 추정 알고리즘을 시스템 수준 합성과 합의 방법 등으로 개발한다. 무선 센서 네트워크로 넓은 환경을 실시간 파악할 때 모든 측정을 중앙으로 보내 생기는 혼잡과 중복 통신을 줄이려고, 센서 스케줄링과 3차원 가우스 스플래팅(사진들로 3차원 장면을 가우스 분포 모양의 점 덩어리 여러 개로 표현하는 기법)으로 네트워크 효율과 장면 재구성 성능의 균형을 맞추는 구조도 연구한다.[^modals] 대표 논문 3–6.

### 3. 데이터로 배우는 동역학 모델과 확률 제약 제어

연구실은 시각·언어 입력으로 행동을 정하는 시각-언어-행동 모델(VLAM) 같은 범용 인공지능 구조의 내부 표현을 분석하기 어렵다는 문제를 다룬다. 이런 의사결정기의 제어에 쓸모 있는 잠재 표현과 잠재 공간의 기하 모델을 개발해, 의미가 같은 관측이 서로 가깝게 놓이는 유사도 척도를 만들려 한다. 또 로봇 제어용 실제 데이터 수집은 비싸고 드물며 안전이 중요하므로, 가장 가치 있는 데이터 표본을 찾고 최적의 하이퍼파라미터(학습 방식을 정하는 설정값)로 빨리 수렴하게 하는 방법을 적응적 경사 하강, 능동 학습, 확률적 최적화로 연구한다.[^modals] 대표 논문으로는 쿠프만 연산자 학습으로 비선형 동역학의 장기 예측을 다룬 논문과 확률 제약 모델 예측 제어 논문이 있다.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

교수 개인 누리집 논문 목록에서 KAIST 부임(2023년 8월) 이후 학회·학술지에 나온 논문 가운데 연구 갈래마다 고르게 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions](https://arxiv.org/abs/2509.24243) · ICLR 2026 | 흐름 정합(flow matching, 무작위 잡음을 데이터 모양으로 바꾸는 흐름을 배워 새 결과를 만드는 생성형 AI 방법)으로 경로를 만드는 계획기는 미분방정식을 한 번이나 몇 번만 풀어도 좋은 경로를 내지만, 만드는 과정에 안전을 보장하는 장치가 없어 제약 근처에서 경로가 불완전해질 수 있다. 이 논문은 흐름 정합에 제어 장벽 함수(CBF, 시스템이 위험 구역에 들어가지 않도록 거는 수학적 조건)를 결합한 SafeFlowMatcher를 내놓았다. 학습한 흐름을 한 번(또는 몇 번) 풀어 후보 경로를 얻는 예측 단계와, 점점 작아지는 시간 척도의 벡터장과 그 벡터장을 최소한만 바꾸는 CBF 기반 이차 계획법(제약 아래에서 이차식을 최소로 만드는 최적화)으로 경로를 다듬는 보정 단계로 나눴다. 이 흐름이 견고한 안전 집합 안에 머물고 유한 시간 안에 그 집합에 들어온다는 것을 증명했고, 중간 단계의 잠재 경로가 아니라 실제로 실행할 경로에만 안전 조건을 걸어 분포가 어긋나는 문제와 국소 함정 문제를 줄였다. 미로 이동, 보행, 로봇 팔 조작 과제에서 확산 모델·흐름 정합 기반 비교 방법보다 더 빠르고 매끄럽고 안전한 경로를 냈다.[^p1] | 1저자 J. Yang·S. Jang(공동 1저자 * 표시), 마지막 저자 한수진 |
| 2 | 2026 | [Heterogeneous Predictor-based Risk-Aware Planning with Conformal Prediction in Dense, Uncertain Environments](https://arxiv.org/abs/2507.11920) · NeuS 2026 | 불확실하게 움직이는 장애물이 많은 곳에서 실시간으로 경로를 계획할 때, 모든 장애물을 정밀하게 예측하는 것은 필요하지도 않고 계산도 많이 든다. 이 논문은 예측에 드는 계산을 필요한 곳에 나눠 주는 H-PRAP을 내놓았다. 등각 예측(conformal prediction, 데이터 분포를 가정하지 않고 정해진 확률로 맞는 오차 범위를 정하는 통계 방법)으로 보정한 가우스 근사에서 충돌 위험 지수(P-CRI)를 닫힌 식으로 얻고, 이 지수로 위험이 큰 장애물은 정확하지만 비싼 예측기에, 위험이 작은 장애물은 가벼운 예측기에 맡겼다. 고른 예측과 그 오차 반경을 확률 제약 모델 예측 제어(MPC, 앞으로의 움직임을 예측해 매 순간 최적의 조작을 다시 계산하는 제어)에 넣어 안전 여유가 드러나는 정책을 만들었다. 예측 계산 예산 아래에서 안전과 효율이 맞바뀌는 관계를 분석했고, 혼잡하고 불확실한 환경의 수치 모의실험에서 한 가지 예측기만 쓰는 구조보다 충돌 없는 성공률과 목표 도달 시간 사이의 균형이 가장 좋았다.[^p2] | 1저자 J. Yang·K. Lee(공동 1저자 * 표시), 마지막 저자 한수진 |
| 3 | 2024 | [A Stochastic Robust Adaptive Systems Level Approach to Stabilizing Large-Scale Uncertain Markovian Jump Linear Systems](https://doi.org/10.1109/cdc56724.2024.10886289) · IEEE CDC 2024 | 외란을 받고, 모드(시스템의 동작 방식)가 바뀌면 네트워크 연결 구조까지 달라질 수 있는 대규모 네트워크형 불확실 마르코프 점프 선형 시스템(MJLS, 모드가 확률적으로 바뀌는 선형 시스템)을 견고하고 적응적으로 안정시키는 통합 틀을 제안했다. 외란에 대한 최소한의 정보로 관측 데이터와 맞는 모드를 가려내 적응하고, 시스템 수준 합성(SLS, 제어기 설계를 시스템 전체 응답을 직접 정하는 볼록 최적화 문제로 바꾸는 방법)을 넓혀 여러 시스템을 동시에 안정시키는 문제를 두 단계 볼록 최적화로 풀었다. 현재 모드의 가능도 분포를 계산해 동시 안정화의 확률 가중치로 쓰고 베이즈 추론으로 갱신하므로, 실제 모드가 바뀔 때 이전 방법에서 보였던 갑작스러운 불안정화를 겪지 않는다. SLS의 분리 가능성 덕분에 하위 시스템마다 국소 제어기를 계산해 네트워크 규모를 키울 수 있고, 정보 합의 방법으로 모드 추정도 국소적으로 했다. 동적 전력망 네트워크 두 예제의 외란 제거로 수치 검증했다.[^p3] | 1저자 한수진(공동 1저자 * 표시는 랩 페이지 표기) |
| 4 | 2025 | [Distributed Kalman-IMM Cooperative Estimator Synthesis for Large-Scale Networked Switching Systems](https://doi.org/10.1109/cdc57313.2025.11312399) · IEEE CDC 2025 | 연결이 끊기거나 일정이 바뀌어 네트워크 구조가 수시로 달라지는 대규모 네트워크 시스템에서 상태를 분산 추정하는 일은 어려운 과제다. 이 논문은 하위 시스템 종류에 따라 다른 추정기를 섞어 완전히 분산·국소화된 설계에 넣는 분산 칼만-IMM 추정기(DKIE)를 제안했다. 네트워크형 MJLS로 모델링한 전환 시스템에서 하위 시스템을 이웃 노드 사이 연결을 바꿀 수 있는 재구성형과 고정형으로 가르고, SLS로 재구성형에는 IMM 추정기(여러 모델의 추정을 확률로 섞는 다중 모델 추정기)의 변형을, 고정형에는 칼만 필터(잡음 섞인 측정에서 상태를 추정하는 필터)의 변형을 설계했다. 협력 규약을 더한 확장판 DKICE는 베이즈 추론 아래 연결 구조 정보를 써서 IMM 하위 추정기들을 국소적으로 조율한다. 가능한 연결 구조가 24가지인 전력망 네트워크에서 기존 분산 추정 방법과 비교해, DKICE가 전환 네트워크 전체의 상태와 모드를 믿을 수 있게 알아내는 확장 가능한 방법임을 보였다.[^p4] | 1저자 E. Sung, 마지막 저자 한수진 |
| 5 | 2026 | [Scalable Sensor Scheduling for Continuous-Discrete Kalman Filtering via Information-Form Surrogate Dynamics](https://doi.org/10.1109/lcsys.2026.3717953) · IEEE Control Systems Letters | 측정값이 포아송 과정(무작위 시각에 사건이 일어나는 확률 모형)에 따라 도착하는 연속-이산 칼만 필터링에서 센서를 어떤 강도로 쓸지 정하는 센서 스케줄링을 연구했다. 대규모 오프라인 설계를 위해 정보 형식의 결정론적 대리 모델을 제안했는데, 공분산 형식 대리 모델과 달리 감지 강도가 센서별로 더해지는 정보 증가분으로 들어가 비선형 계획 문제의 도함수 구조가 단순해진다. 공분산 형식 대리 모델과 함께 쓰면, 측정이 확률적으로 도착할 때 주어진 일정의 목적 함수 값에 대해 계산 가능한 위·아래 경계를 준다는 것도 보였다. 수치 실험에서 특히 센서가 많을 때 계산을 크게 줄이면서도 실제 몬테카를로 성능은 비슷하게 유지했다.[^p5] | 1저자 H. Choe, 마지막 저자 한수진 |
| 6 | 2024 | [Efficient Replay Memory Architectures in Multi-Agent Reinforcement Learning for Traffic Congestion Control](https://doi.org/10.1109/itsc58415.2024.10920085) · IEEE ITSC 2024 | 사람 뇌의 일화 기억에서 착안한 일화 제어는 높은 보상을 받았던 과거 경험을 다시 써서 모델 없는 강화학습의 샘플 비효율을 개선해 왔지만, 차량 교통 관리처럼 큰 다중 에이전트 문제에서는 기억이 계속 커지는 것이 문제다. 이 논문은 신호등 일정을 적응적으로 정해 혼잡을 제어하는 다중 에이전트 강화학습에 덧붙이는 재현 메모리 구조 Dual-Memory Integrated Learning을 내놓았다. 의미 기억과 일화 기억, 단기와 장기 기억을 함께 써 네트워크에서 자주 나타나는 높은 보상 상태는 기억하고 그렇지 않은 상태는 걸러 내며, 같은 행동(신호 순서)으로 제어할 수 있는 비슷한 상태-행동 쌍을 동치류로 묶는다. 기억이 늘어나는 양의 상한을 이론으로 보였고, 여러 교차로 네트워크 모의실험에서 차량 처리량 같은 혼잡 성능이 나아졌다.[^p6] | 1저자 M. Chodhary, 마지막 저자 한수진 |
| 7 | 2026 | [Scalable Infinitesimal Generator–Based Koopman Learning for Long-Horizon Prediction](https://proceedings.mlr.press/v331/jeong26a.html) · L4DC 2026 (PMLR 331) | 쿠프만 연산자 이론(비선형으로 움직이는 시스템을 선형 연산자로 나타내는 이론)은 장기 예측에 쓸모가 크지만, 기존 방법 대부분은 한 단계씩 맞추는 스냅숏 학습에 기대어 긴 예측에서 오차가 쌓인다. 앞선 연구는 학습 구간을 늘리거나 물리 정보를 넣은 생성자 기반 정식화를 썼지만, 저주파 성분에 치우치는 다층 퍼셉트론 기반 관측 함수에 의존해 한계가 있었다. 이 논문은 생성자 손실을 직접 줄이는 무작위 푸리에 특징 기반 물리 정보 쿠프만 네트워크(RFF-PIKN)를 내놓았다. 스냅숏 기반 국소 전이 맞춤이 생성자 기반 학습보다 장기 안정성에서 근본적인 한계가 있음을 보이고, RFF-PIKN이 생성자 손실 아래에서 참 모집단 위험의 국소 최솟값으로 안정적으로 수렴함을 증명했다. 실험에서 다층 퍼셉트론·다항식 기반 관측 함수보다 장기 예측이 낫고 계산을 크게 줄였으며, 커널 기반 기준(오라클) 방법의 주요 동작과도 맞았다.[^p7] | 1저자 M. Jeong, 한수진 교수는 3명 중 2번째 저자 |
| 8 | 2026 | [Calibration-Aware Convex Surrogate MPC for Nonlinear Joint Chance-Constrained Control via Spectral Risk Allocation](https://doi.org/10.1109/lcsys.2026.3710526) · IEEE Control Systems Letters | 확률적 불확실성 아래에서 비선형 결합 확률 제약(JCC, 여러 안전 조건이 함께 지켜질 확률을 정해진 수준 이상으로 두라는 제약)을 다루는 데이터 기반 확률 모델 예측 제어 틀 Spectral-IRA를 제안했다. 계산 부담과 위험 평가의 균형을 맞추려고, 상태 공간의 물리적 안전 경계, 특징 공간의 결정론적 선형 점수, 확률 공간의 위험 예산을 한데 묶은 단계별 위반 위험의 보정된 선형 대리 모델을 만들었다. 커널 평균 임베딩(확률 분포를 함수 공간의 한 점으로 나타내는 방법)으로 비가우스 분포 모양에 민감한 비선형 무작위 특징의 기댓값을 전파해, 다루기 어려운 확률 제약을 볼록한 선형 부등식으로 바꿨다. 오프라인에서 보정한 공간 여유로 근사 오차를 반영해 보정 분포에서의 안전을 확보했고, 위험 예산을 적응적으로 다시 나눠 지나친 보수성을 줄였다. 모의실험에서 정한 위험 예산을 지키면서 안전·성능·계산 효율 사이의 실용적인 균형을 보였다.[^p8] | 1저자 S. Koo, 한수진 교수는 3명 중 2번째 저자 |

## 교수와 전문 분야

한수진 교수는 KAIST 전기및전자공학부 조교수다. 학부 교수 소개는 주요 연구분야를 Robotics & Control로, 주요 연구를 Autonomous Control, Artificial Intelligence, Network Decision-Making으로, 디비전을 Signal division으로 적는다.[^ee] 조천식모빌리티대학원 교수진 명단에는 전기및전자공학부 소속 겸임교수로 올라 있고,[^mo] 반도체시스템공학과 교수 명단(연구분야 「컴퓨터, 인공지능 및 소프트웨어」)과 연구실 명단에도 올라 있다.[^sseprof][^sselab]

교수 개인 누리집에 따르면 UC 버클리에서 전기공학·컴퓨터과학(EECS)과 응용수학 학사(2016년 가을)를, 캘리포니아공과대학(Caltech)에서 John C. Doyle 교수와 Soon-Jo Chung 교수의 지도로 제어 및 동역학 시스템(Control and Dynamical Systems) 박사학위를 받았다. 학위 논문은 「Control and State-Estimation of Jump Stochastic Systems by Learning Recurrent Spatiotemporal Patterns」이고 2023년 1월 심사를 마쳤으며, 박사과정 동안 NSF GRFP와 Caltech Special EAS Fellowship 지원을 받았다.[^bio] 2023년 8월 KAIST 조교수로 부임했고, 2025년 1월부터 IEEE Robotics and Automation Letters(RA-L)의 Associate Editor를 맡고 있으며, 2025년 10월 교재 「Linear Systems: Theory and Applications」를 Springer에서 냈다.[^pihome] 누리집은 연구실이 AFOSR AOARD, NRF, ADD, ETRI, KIAST의 지원을 받고, KAIST·서울대학교·경희대학교 등 국내와 미국 UIUC 등의 연구자와 협력한다고 적는다.[^pihome]

교수 누리집의 논문 목록으로 보면 KAIST 부임 전에는 마르코프 점프 시스템을 반복 패턴 학습으로 예측 제어하는 연구(Automatica, 2023), 레비 잡음(갑작스러운 도약이 섞인 무작위 잡음)을 받는 확률 시스템의 증분 비선형 안정성 분석(International Journal of Robust and Nonlinear Control, 2022), 차량 교통 네트워크의 혼잡 제어(L4DC, 2023)를 냈다.[^pubs] KAIST에서는 EE899 Stochastic Control, EE210 Probability and Random Processes, EE202 Signals and Systems, EE581 Linear Systems Theory, EE488F Learning Patterns for Autonomous Control을 가르쳤다.[^teaching]

논문으로 보면 전문 분야는 세 갈래다. 첫째, 흐름 정합 같은 생성 모델과 제어 장벽 함수·등각 예측을 엮어 안전을 보장하는 로봇 경로 계획이다(대표 논문 1, 2).[^p1][^p2] 둘째, 마르코프 점프 선형 시스템과 시스템 수준 합성을 바탕으로 한 대규모 네트워크의 견고·적응 제어, 분산 상태 추정, 센서 스케줄링, 다중 에이전트 강화학습이다(대표 논문 3–6).[^p3][^p4][^p5][^p6] 셋째, 쿠프만 연산자 학습과 데이터 기반 확률 제약 예측 제어다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

Research 절의 세부 항목은 응용 분야로 로봇용 생성형 AI, 안전·견고한 자율성, 궤적·동작 계획, 고장 허용 시스템, 제어를 위한 OOD 탐지, 다중 에이전트 시스템과 대규모 네트워크, 분산 데이터 수집과 다중 표적 추적, 분산 3차원 재구성, 로봇 센서 네트워크, 시각-언어-행동 모델, 월드 모델, 체화된 AI, 인간-로봇 상호작용, 데이터 효율적 제어를 든다.[^modals] 대표 논문들은 미로 이동·보행·로봇 팔 조작의 경로 계획(대표 논문 1), 동적 전력망 네트워크의 외란 제거와 상태·모드 추정(대표 논문 3, 4), 교차로 네트워크의 신호등 혼잡 제어(대표 논문 6)를 실험 대상으로 삼았다.[^p1][^p3][^p4][^p6] 교수 누리집 논문 목록에는 윈치로 묶인 쿼드로터(프로펠러 네 개로 나는 드론)의 계층형 견고 제어 논문도 있다.[^pubs] Team 절이 적은 석사 졸업생의 진로는 NTU (Singapore) EEE, UW A&A, KAIST Mobility Graduate School, MIDAS Asset Management, Hyundai Motors R&D다.[^team]

## 구성원

연구실 누리집 Team 절의 현재 구성원이다(객원교수 1, 박사후연구원 1, 박사과정 2, 석사과정 9, 연구인턴 2). 과정과 시작 시기는 페이지 표기 그대로이고, Incoming은 입학 예정 표기다. 연구 주제 칸은 페이지가 사람마다 붙인 연구 관심 분야 표지(페이지 범례의 영문 이름)다.[^team] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Hiroyasu Tsukamoto, Ph.D. | 객원교수 (Visiting Professor) | May 2026 - Aug 2026 |  |  |
| Sunidhi Pandey, Ph.D. | 박사후연구원 | May 2026 - |  |  |
| Minseok Jeong (정민석) | 박사과정 | Mar 2025 - | Uncertain Decision-Making, Dynamics Modeling, Statistical Learning Theory | 7 |
| Doyoung Heo (허도영) | 입학 예정 박사과정 | Aug 2026 | Uncertain Decision-Making, Online Learning, Dynamics Modeling |  |
| Jungyo Jung (정준교) | 석사과정 | Feb 2025- | Application: Robotics, Filtering & State-Estimation, Adaptive Control |  |
| Hyeongmin Choe (최형민) | 석사과정 | Feb 2025- | Stochastic Control, Distributed / Multiagent Control | 5 |
| Hyewon Choi (최혜원) | 석사과정 | Nov 2024- | Online Learning, Application: Robotics, Modeling with Generative AI |  |
| Yechan Lee (이예찬) | 석사과정 | Feb 2025- | Reinforcement Learning, Online Learning, Application: Robotics |  |
| Nakgyu Yang (양낙규) | 석사과정 | Feb 2025- | Stochastic Control, Modeling with Generative AI, Statistical Learning Theory |  |
| Mincheol Kang (강민철) | 석사과정 | Feb 2026- | Control with Safety, Reinforcement Learning, World Model, Application: Robotics |  |
| Yuil Kim (김유일) | 석사과정 | Aug 2026- | Stochastic Control, Uncertainty Quantification, Reinforcement Learning |  |
| Munki Jeong (정문기) | 입학 예정 석사과정 | Mar 2027- | Stochastic Control, Distributed / Multiagent Control, Dynamics Modeling, Application: Cyber-Physical Systems |  |
| Jaewon Joung (정재원) | 입학 예정 석사과정 | Mar 2027- | World Model, Control with Safety, Dynamics Modeling, Application: Robotics |  |
| Injun Jo (조인준) | 연구인턴 (Research Intern) |  |  |  |
| Nafi Abrisam Suling | 연구인턴 (Research Intern) |  |  |  |

## 졸업생과 이전 구성원

Team 절 「Past Students & Affiliates」에 실린 25명이다(석사과정 8명, 학부 인턴·게스트 연구원 등 17명). 과정·기간·진로는 페이지 표기 그대로이고, Yongmin Kim은 과정 표기가 없다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeonghyeon Noh (노정현) | 석사과정 (Aug 2024 - Aug 2026) |  |
| Kwang Bin Lee (이광빈) | 석사과정 (Aug 2024 - Aug 2026) |  |
| Seunghwan Jang (장승환) | 석사과정 (Aug 2024 - Jun 2026) | NTU (Singapore), EEE |
| Jeongyong Yang (양정용) | 석사과정 (Jan 2024 - Feb 2026), Research Assistant (Feb 2026 - Jun 2026) | UW A&A |
| Eunwoo Sung (성은우) | 석사과정 (Feb 2024 - Feb 2026) | KAIST Mobility Graduate School |
| Donggyu Kim (김동규) | 석사과정 (Feb 2025 - Feb 2026) | MIDAS Asset Management |
| Sanghun Park (박상훈) | 석사과정 (Feb 2024 - Jan 2026) | Hyundai Motors R&D |
| Hojin Ju (주호진) | 석사과정 (Jan 2024 - Feb 2026) |  |
| Jaewon Jeong (정재원) | 학부 인턴 |  |
| Munki Jeong (정문기) | 학부 인턴 |  |
| Eren Park | 게스트 연구원, 학부 인턴 |  |
| Yongmin Kim (김용민) |  |  |
| Nitchawee (Meena) Piromchotesiri | 학부 인턴 |  |
| Junwon Yang (양준원) | 학부 인턴 |  |
| Hohyeon Song (송호현) | 학부 인턴 |  |
| Chaewoo Lim (임채우) | 게스트 연구원, 학부 인턴 |  |
| Woojin Shin (신우진) | 게스트 연구원, 학부 인턴 |  |
| Yejun Jang (장예준) | 게스트 연구원, 학부 인턴 |  |
| Nijat Abbasov | KAIST URP Fellow, 학부 인턴 |  |
| Jeonghun You (유정훈) | 학부 인턴 |  |
| SeungEon Lee (이승언) | 학부 인턴 |  |
| Jiwoo Park (박지우) | 학부 인턴 |  |
| Sanghyun Lee (이상현) | 학부 인턴 |  |
| Jerry Song (송제리) | 학부 인턴 |  |
| Seongjun Mun (문성준) | 학부 인턴 |  |

## 최근 논문 목록 (2021–2026)

한수진 교수 개인 누리집 Publications 페이지의 2021–2026년 항목 29건이다. 저자·제목·학회·학술지 표기와 Accepted(게재 확정)·Preprint(사전 공개)·Tutorial Session 같은 상태 표기는 누리집 그대로이고, 저자 이름 뒤의 *는 누리집의 공동 기여 표시다. 2023년 8월 KAIST 부임 전의 논문도 누리집 목록대로 들어 있다.[^pubs]

**2026**

- Minseok Jeong, Yechan Lee, Hyewon Choi, Jeongyong Yang, SooJean Han, "Mitigating Overgeneralization in RND via Spectral Target Design." Accepted, Neural Information Processing Systems (NeurIPS), Sep 2026.
- Seunghwan Jang, Wonje Jeung, SooJean Han, "Systematic Hazard Sampling: Minimal-Variance Inference for Discrete Diffusion and Flow Models." Accepted, Neural Information Processing Systems (NeurIPS), Sep 2026.
- Seunghwan Jang, Jeongyong Yang, Siddharth Ancha, SooJean Han, "Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics." Accepted, Conference on Robot Learning (CoRL), Sep 2026.
- Nakgyu Yang\*, Kwang Bin Lee\*, SooJean Han, "G2SD: Graph-Guided Diffusion Planning under Inference-Time Safety Constraints." Preprint, Aug 2026.
- Jungyo Jung, SooJean Han, "Hierarchical Robust Control of Winch-Tethered Quadrotors via Adaptive Bias Compensation and Distance-Based Winch Regulation." Accepted, International Conference on Control, Automation and Systems (ICCAS), Aug 2026.
- Hyeongmin Choe, SooJean Han, "Scalable Sensor Scheduling for Continuous-Discrete Kalman Filtering via Information-Form Surrogate Dynamics." Accepted, IEEE Control Systems Letters (L-CSS), Jul 2026.
- Luca Furieri\*, SooJean Han\*, Andrea Martin\*, Jing Yu\*, John C. Doyle, "Learning, Adapting, and Certifying Control Policies in System-Level Coordinates." Accepted, Tutorial Session, IEEE Conference on Decision and Control (CDC), Jul 2026.
- Jeonghyeon Noh, SooJean Han, "Communication Architecture Co-Design for Distributed Control via System Level Synthesis." Accepted, IEEE Conference on Decision and Control (CDC), Jul 2026.
- Eunwoo Sung, SooJean Han, Hyo-Sang Shin, "Localized Markov Jump Quadratic Optimal Control: A System-Level Approach." Accepted, IEEE Conference on Decision and Control (CDC), Jul 2026.
- Man Jun Koh, Hyochoong Bang, SooJean Han, "Chance-Constrained Nonlinear Covariance Control via Robust Linearization Remainder Bounds." Accepted, IEEE Conference on Decision and Control (CDC), Jul 2026.
- Soyeon Koo, SooJean Han, Hyo-Sang Shin, "Calibration-Aware Convex Surrogate MPC for Nonlinear Joint Chance-Constrained Control via Spectral Risk Allocation." Accepted, IEEE Control Systems Letters (L-CSS) and IEEE Conference on Decision and Control (CDC), Jul 2026.
- Jeongyong Yang\*, KwangBin Lee\*, SooJean Han, "Heterogeneous Predictor-based Risk-Aware Planning with Conformal Prediction in Dense, Uncertain Environments." Neuro-Symbolic Systems (NeuS), Jun 2026.
- Minseok Jeong, SooJean Han, Hyo-Sang Shin, "Scalable Infinitesimal Generator–Based Koopman Learning for Long-Horizon Prediction," Learning for Dynamics and Control Conference (L4DC), Jun 2026.
- Jeongyong Yang\*, Seunghwan Jang\*, SooJean Han, "SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions." International Conference on Learning Representations (ICLR), Apr 2026.

**2025**

- Jeongyong Yang, Minseok Jeong, Hyo-Sang Shin, and SooJean Han, “Random Fourier Features Lifted Physics-Informed Koopman Network.” (in Korean.) in Proceedings of the Korean Society for Aeronautical & Space Sciences (KSAS), Nov 2025.
- SooJean Han, "Linear Systems: Theory and Applications." Springer, Oct 2025.
- Sanghun Park, SooJean Han, "Approximate Orthogonal Gradient Descent for the Continual Reinforcement Learning of Robot Control." Conference of Korean Artificial Intelligence Association (CKAIA), Aug 2025.
- Eunwoo Sung, SooJean Han, "Distributed Kalman-IMM Cooperative Estimator Synthesis for Large-Scale Networked Switching Systems." IEEE Conference on Decision and Control (CDC), Dec 2025.
- Hyeongmin Choe, SooJean Han, "Advantages of Feedback in Distributed Data-Gathering for Accurate and Power-Efficient State-Estimation." Preprint, Jul 2025.
- Jeongyong Yang, Hojin Ju, SooJean Han, "Curvature and Energy-based Trajectory Optimization in Unstructured Environments." (in Korean.) Korean Robotics Conference (KRoC), 2025.
- Seunghwan Jang, SooJean Han, "Comparison of Compression Codec Algorithms to Image Datasets in 3D Gaussian Splatting Models." (in Korean.) Workshop on Image Processing and Image Understanding (IPIU), 2025.

**2024**

- SooJean Han, Minwoo Kim, Ieun Choo, "A Stochastic Robust Adaptive Systems Level Approach to Stabilizing Large-Scale Uncertain Markovian Jump Linear Systems." IEEE Conference on Decision and Control (CDC), Sep 2024.
- Mukul Chodhary, Kevin Octavian, SooJean Han, "Efficient Replay Memory Architectures in Multi-Agent Reinforcement Learning for Traffic Congestion Control." IEEE Intelligent Transportation Systems Conference (ITSC), Jul 2024.

**2023**

- SooJean Han, Soon-Jo Chung, Johanna Gustafson, "Congestion Control of Vehicle Traffic Networks by Learning Structural and Temporal Patterns." Learning for Dynamics and Control Conference (L4DC), Jun 2023.
- SooJean Han, Soon-Jo Chung, John C. Doyle, "Predictive Control of Linear Discrete-Time Markovian Jump Systems by Learning Recurrent Patterns." Automatica, May 2023.
- Shih-Hao Tseng, SooJean Han, Adam Wierman, "Trading Throughput for Freshness: Freshness-Aware Traffic Engineering and In-Network Freshness Control." ACM Transactions on Modeling and Performance Evaluation of Computing Systems (ToMPECS), vol. 8, no. 4, p. 1-26, Mar 2023.

**2022**

- SooJean Han, Soon-Jo Chung, "Incremental Nonlinear Stability Analysis for Stochastic Systems Perturbed by Lévy Noise." International Journal of Robust and Nonlinear Control, vol. 32, no. 12, p. 7174-7201, Aug 2022.
- SooJean Han, Michelle Effros, Richard Murray, "OUTformation: Distributed Data Gathering with Feedback under Unknown Environment and Communication Delay Constraints." ArXiv, Aug 2022.

**2021**

- Mo Chen\*, Sylvia L. Herbert\*, Haimin Hu, Ye Pu, Jaime F. Fisac, Somil Bansal, SooJean Han, Claire J. Tomlin, "FaSTrack: a Modular Framework for Real-Time Motion Planning and Guaranteed Safe Tracking." IEEE Transactions on Automatic Control, vol. 66, no. 12, p. 5861-5876, Dec 2021.

## 소식

한수진 교수 개인 누리집 Recent News 가운데 KAIST 부임(2023-08-28) 이후 글 25건이다. 날짜는 글의 날짜이고 내용은 게시된 문장 그대로다.[^pihome]

- 2026-09-25 · Our paper, Mitigating Overgeneralization in RND via Spectral Target Design has been accepted to the Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS).
- 2026-09-25 · Our paper, Systematic Hazard Sampling: Minimal-Variance Inference for Discrete Diffusion and Flow Models has been accepted to the Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS).
- 2026-09-04 · Our paper, Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics has been accepted to the Conference on Robot Learning (CoRL).
- 2026-08-03 · Our paper, Hierarchical Robust Control of Winch-Tethered Quadrotors via Adaptive Bias Compensation and Distance-Based Winch Regulation has been accepted to the International Conference on Control, Automation and Systems (ICCAS).
- 2026-07-18 · Our paper, Scalable Sensor Scheduling for Continuous-Discrete Kalman Filtering via Information-Form Surrogate Dynamics has been accepted to the IEEE Control Systems Letters (L-CSS).
- 2026-07-17 · We'll be holding a tutorial session, Learning, Adapting, and Certifying Control Policies in System-Level Coordinates at the 66th IEEE Conference on Decision and Control (CDC). See you in Hawaii!
- 2026-07-17 · 3 of our papers, Communication Architecture Co-Design for Distributed Control via System Level Synthesis, Chance-Constrained Nonlinear Covariance Control via Robust Linearization Remainder Bounds, and Localized Markov Jump Quadratic Optimal Control: A System-Level Approach have been accepted to the 66th IEEE Conference on Decision and Control (CDC).
- 2026-06-09 · Our paper, Calibration-Aware Convex Surrogate MPC for Nonlinear Joint Chance-Constrained Control via Spectral Risk Allocation has been accepted to the IEEE Control Systems Letters (L-CSS) and the 66th IEEE Conference on Decision and Control (CDC).
- 2026-04-25 · Our paper, Heterogeneous Predictor-based Risk-Aware Planning with Conformal Prediction in Dense, Uncertain Environments has been accepted to the 3rd International Conference on Neuro-Symbolic Systems (NeuS).
- 2026-01-26 · Our paper, SafeFlowMatcher: Safe and Fast Planning using Flow Matching with Control Barrier Functions has been accepted to the 14th International Conference on Learning Representations (ICLR).
- 2026-01-23 · Our paper, Scalable Infinitesimal Generator–Based Koopman Learning for Long-Horizon Prediction has been accepted to the 8th Annual Learning for Dynamics & Control (L4DC) Conference.
- 2025-12-11 · I gave an invited seminar talk to the Graduate School of Dynamics/Control at Seoul National University, hosted by Prof. Dongjun Lee. Thank you for hosting me!
- 2025-10-30 · I gave an invited seminar talk to the Department of Intelligent Robotics at Sungkyunkwan University, hosted by Prof. Kyunam Kim. Thank you for hosting me!
- 2025-10-09 · My first and newest textbook "Linear Systems: Theory and Applications", is published on Springer!
- 2025-08-21 · I gave an invited talk for the IT Scientific Session at the 6th International Conference for Women in Science and Technology (BIEN).
- 2025-07-15 · Our paper, Distributed Kalman-IMM Cooperative Estimator Synthesis for Large-Scale Networked Switching Systems has been accepted to the 64th IEEE Conference on Decision and Control (CDC).
- 2025-06-25 · I gave an invited talk for the Outstanding Young Faculty Seminar at the 2025 Institute of Control Robotics and Systems (ICROS).
- 2025-02-27 · I gave an invited seminar talk to the KAIST Cho Chun Shik Graduate School of Mobility, hosted by Prof. Hyo-Sang Shin. Thank you for hosting me!
- 2025-01-22 · I began service as an Associate Editor for the IEEE Robotics and Automation Letters (RA-L).
- 2024-12-05 · I gave an invited talk at the 2024 Institute of Control Robotics and Systems (ICROS), Daejeon Chungcheong Branch Conference.
- 2024-08-02 · I gave an invited talk at Caltech on the past, present, and future work in our ACSS Lab. My presentation was on Learning Patterns for Autonomous Control: Data-Efficient AI and Adaptive Decisions.
- 2024-07-24 · Our paper, A Stochastic Robust Adaptive Systems Level Approach to Stabilizing Large-Scale Uncertain Markovian Jump Linear Systems has been accepted to the 63rd IEEE Conference on Decision and Control (CDC).
- 2024-07-10 · Our paper, Efficient Replay Memory Architectures in Multi-Agent Reinforcement Learning for Traffic Congestion Control has been accepted to the 27th IEEE International Conference on Intelligent Transportation Systems (ITSC).
- 2024-02-22 · I gave an invited talk for the New Faculty Seminar at the 2024 Korea Robotics Conference (KROS KRoC).
- 2023-08-28 · I began as an assistant professor at KAIST.

## 연락과 위치

- 연구실: (34141) 대전광역시 유성구 대학로 291 KAIST 전기및전자공학부동(E3-2) 2228호[^home]
- 교수 연구실: 전기및전자공학부동(E3-2) 2225호, 교내 전화 7474[^ee][^mo]
- 교수 이메일: soojean@kaist.ac.kr[^ee]
- 연구실 문의: acss-admins@kaist.ac.kr (연구실은 교수에게 직접 보낸 이메일은 놓칠 수 있다고 안내한다)[^about]
- 모집 안내: 2026년 봄 기준 석사·박사과정과 박사후연구원 지원은 받지 않으며, 학부 인턴은 이력서와 성적표를 연구실 문의 주소로 보내라고 안내한다.[^about]
[^p1]: J. Yang, S. Jang, S. Han, International Conference on Learning Representations (ICLR) (2026). <https://arxiv.org/abs/2509.24243> 초록 기준(arXiv 판).
[^p2]: J. Yang, K. Lee, S. Han, International Conference on Neuro-symbolic Systems (NeuS) (2026). <https://arxiv.org/abs/2507.11920> 초록 기준(arXiv 판).
[^p3]: S. Han, M. M. Kim, I. Choo, 2024 IEEE 63rd Conference on Decision and Control (CDC), 6904-6909 (2024). <https://doi.org/10.1109/cdc56724.2024.10886289> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: E. Sung, S. Han, 2025 IEEE 64th Conference on Decision and Control (CDC), 515-522 (2025). <https://doi.org/10.1109/cdc57313.2025.11312399> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Choe, S. Han, IEEE Control Systems Letters 10, 2179-2184 (2026). <https://doi.org/10.1109/lcsys.2026.3717953> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: M. Chodhary, K. Octavian, S. Han, 2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC), 1932-1937 (2024). <https://doi.org/10.1109/itsc58415.2024.10920085> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. Jeong, S. Han, H.-S. Shin, Proceedings of Machine Learning Research 331 (L4DC), 1966-1980 (2026). <https://proceedings.mlr.press/v331/jeong26a.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p8]: S. Koo, S. Han, H.-S. Shin, IEEE Control Systems Letters 10, 1969-1974 (2026). <https://doi.org/10.1109/lcsys.2026.3710526> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <http://acss.kaist.ac.kr/> (바닥글 주소, 2026-10-22 열람)
[^about]: About 절 <http://acss.kaist.ac.kr/subpages/about.html> (영문·국문 소개, Our Vision, 지원 안내, 2026-10-22 열람)
[^research]: Research 절 <http://acss.kaist.ac.kr/subpages/research.html> (세 갈래, 2026-10-22 열람)
[^modals]: Research 절의 갈래별 세부 항목 <http://acss.kaist.ac.kr/subpages/research_modals.html> (Broad Problem, Research Goal, Application Areas, 2026-10-22 열람)
[^team]: Team 절 <http://acss.kaist.ac.kr/subpages/team.html> (교수, 객원교수, 박사후연구원, 박사과정, 석사과정, 연구 관심 분야 범례, 연구인턴, Past Students & Affiliates, 2026-10-22 열람)
[^pihome]: 한수진 교수 개인 누리집 첫 화면 <https://soojean.github.io/> (소개, Recent News, 2026-10-22 열람)
[^bio]: 같은 누리집 Bio 페이지 <https://soojean.github.io/bio/> (2026-10-22 열람)
[^pubs]: 같은 누리집 Publications 페이지 <https://soojean.github.io/publications/> (2026-10-22 열람)
[^teaching]: 같은 누리집 Teaching 페이지 <https://soojean.github.io/teaching/> (2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(한수진) <https://ee.kaist.ac.kr/professor/%ed%95%9c%ec%88%98%ec%a7%84/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-22 열람)
[^mo]: KAIST 조천식모빌리티대학원 교수진 <https://mo.kaist.ac.kr/professor/> (겸임교수 칸, 2026-10-22 열람)
[^sseprof]: KAIST 반도체시스템공학과 교수 명단 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 명단 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)

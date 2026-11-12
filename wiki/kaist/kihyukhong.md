# Reinforcement Learning Lab (RLLab)

**KAIST 산업및시스템공학과·데이터사이언스대학원·AX학과(겸임) · 홍기혁 조교수**

- 영문 이름: Kihyuk (Ki) Hong
- 분야: 강화학습 이론과 알고리즘, 제한된 자료와 안전 제약 아래의 학습, 로봇·운영과학 응용
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 강화학습[^lab]
- 홈페이지: <https://www.kihyukhong.com/>
- 근거와 출처: [Reinforcement Learning Lab 근거 페이지](kihyukhong-sources.md)

> 행동의 결과에서 배우는 학습 방법을 수학적으로 분석하고, 자료와 계산량이 제한되거나 안전 조건이 있는 상황에서 쓸 수 있는 알고리즘을 만드는 연구실이다.[^lab]

## 무엇을 연구하나

홍기혁 조교수가 이끄는 연구실은 기계학습(자료에서 예측이나 판단 방법을 배우는 분야)의 한 갈래인 강화학습(Reinforcement Learning, RL; 행동 결과에 대한 수치 평가를 이용해 장기적인 성과를 높이는 행동 선택 방법을 배우는 학습)을 연구한다. 그 수치 평가를 보상이라고 부른다. 연구실은 현실의 문제에서 출발해 학습 방법을 설계하고, 어떤 조건에서 그 방법이 성능 기준을 만족하는지 수학적으로 밝히는 것을 목표로 한다.[^lab]

이론 연구에서는 학습에 필요한 자료의 양과 계산량을 함께 다룬다. 오프라인 학습(새로운 환경 상호작용 없이 이미 모은 자료만으로 배우는 방식)과 안전 등의 제약이 있는 강화학습에서, 조건을 지키면서 보상을 크게 하는 정책(상황에 따라 어떤 행동을 선택할지 정하는 규칙)을 구하는 알고리즘(문제를 풀기 위한 계산 절차)을 개발한다.[^lab]

실용적인 학습 방법에서는 분포 변화(학습할 때와 실제로 쓸 때 자료가 발생하는 확률 규칙이 달라지는 현상), 자료 훼손(자료 일부가 손상되거나 잘못 바뀐 상태), 제한된 탐색(학습을 위해 아직 충분히 알지 못하는 행동을 시도하는 일), 안전 제약 아래의 신뢰성을 다룬다. 현재 응용으로는 로봇과 운영과학(복잡한 운영 의사결정을 수학 모형으로 분석하고 선택하는 분야)을 들며, 영상·언어 모형(영상과 언어를 함께 다루는 기계학습 모형)을 활용해 안전한 운전 정책을 계산 효율적으로 배우는 자율주행도 연구한다.[^lab]

## 주요 연구 주제

### 1. 자료와 계산량을 함께 고려하는 강화학습 이론

제한된 자료·상호작용·안전 요구 아래에서 학습 성능을 수학적으로 보장하는 알고리즘을 설계한다. 제약이 있는 순차 의사결정에서 이론적 최적 성능에 도달하는 온라인 학습(환경과 새로 상호작용하며 자료를 얻어 배우는 방식)도 연구한다.[^lab] 대표 논문 2는 관측 결과에 따라 환경에 대한 믿음을 갱신하며 행동하는 방법의 이론적 성능을 분석한다.[^p2]

### 2. 제약을 지키는 오프라인 학습과 실제 환경으로의 전환

이미 모은 자료만으로 보상을 크게 하면서 제약을 지키는 정책을 구하는 방법을 연구한다. 대표 논문 3은 자료에 담긴 행동의 범위가 제한된 경우의 학습을 다룬다.[^p3] 현재 연구에는 오프라인 자료에서 온라인 상호작용으로 넘어갈 때 훼손된 자료의 영향을 견디는 학습과, 이미 모은 자료만으로 일련의 행동 전체에 대한 안전을 보장하는 학습도 있다.[^lab]

### 3. 로봇과 자율주행을 위한 실용적인 학습 방법

이론에서 얻은 통찰을 실제로 쓸 수 있는 강화학습 방법으로 연결하고 로봇·운영과학에 적용한다. 자율주행에서는 영상·언어 모형을 활용해 안전한 운전 정책을 효율적으로 배우는 방법을 연구한다.[^lab] 대표 논문 1은 연속적인 값으로 행동을 고르는 과제에서 행동이 심하게 진동하는 문제를 다루며, 누적 보상을 우선하면서 행동의 급격한 변화를 줄이는 학습 방법을 제안한다.[^p1]

## 대표 논문

홍기혁 교수의 KAIST 재직 시기에 공개된 자료에서 강화학습 이론, 제약 아래의 학습, 연속 행동의 학습을 다루는 세 편을 골랐다. 두 편은 2026년 사전 공개본이고, 세 번째는 2025년 첫 공개 뒤 2026년 5월 12일에 수정된 사전 공개본 제2판이다. 표의 세 번째 연도는 설명 대상인 제2판의 연도다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [DAMPER: Return-Prioritized Gradient Control for Smooth Policies](https://doi.org/10.48550/arXiv.2609.38903) · arXiv 사전 공개본 | 행동을 고르는 학습과 행동의 시간적 일관성을 위한 학습을 결합할 때, 행동을 고르는 학습의 방향에 맞서는 일관성 학습 성분은 제거하고, 남긴 일관성 방향의 크기는 행동을 고르는 학습 방향의 크기에 맞춰 조절하는 DAMPER(Direction-Aware Magnitude-Controlled Projection with Explicit Return Priority)를 제안했다. 실험에서 행동의 진동을 줄였으며, 누적 보상과 매끄러운 행동 사이의 상충은 과제에 따라 달랐다.[^p1] | 1저자 Seokmin Ko, 마지막 저자 Kihyuk Hong |
| 2 | 2026 | [Minimax-Optimality of Posterior Sampling for Reinforcement Learning](https://doi.org/10.48550/arXiv.2609.33246) · arXiv 사전 공개본 | 유한한 단계 동안 행동하는 표 형태의 의사결정 모형에서, 관측 후 갱신한 확률에 따라 환경 모형을 뽑아 행동하는 방법을 분석했다. 보상과 상태 변화에 대한 사전 확률(관측 전에 가정한 확률)이 서로 연관되어 있어도, 그 사전 확률에 대해 평균 낸 누적 보상 손실(처음부터 최선의 행동을 알았을 때 얻는 보상과의 총 차이)의 주요 항이 이론적 최적 수준에 도달함을 보였다. 선형혼합 모형(정해진 기본 모형에 비중을 주어 더하는 방식으로 상태 변화 확률을 나타내는 모형)에도 같은 증명 원리를 적용했다.[^p2] | 1저자 Taewon Goo, 마지막 저자 Kihyuk Hong |
| 3 | 2026 | [Offline Constrained Reinforcement Learning under Partial Data Coverage](https://doi.org/10.48550/arXiv.2505.17506) · arXiv 사전 공개본 제2판 | 자료를 생성한 확률 규칙을 몰라도 행동 선택 규칙을 직접 계산 변수로 삼아 학습하는 방법을 제안했다. 최적 정책이 사용하는 행동을 자료가 뒷받침하고, 최적 정책과 관련된 값을 표현하는 함수가 논문이 제시한 조건을 만족하면, 제한된 자료에서 최적에 가까우면서 제약도 거의 만족하는 정책을 얻는다는 것을 보였다.[^p3] | 1저자 Seokmin Ko, 마지막 저자 Kihyuk Hong |

## 교수와 전문 분야

홍기혁 교수는 KAIST 산업및시스템공학과 조교수이며 데이터사이언스대학원에 소속되고 AX학과를 겸임한다. 2025년 9월 1일 KAIST에 부임했다.[^home] 학위는 Johns Hopkins University 학사(2008), Stanford University 석사(2010), University of Michigan 박사(2025)이며, 박사 지도교수는 Ambuj Tewari다.[^home]

박사과정 전에는 Meta(2010–2013)와 Naver(2013–2018, 2019–2020)에서 기계학습 엔지니어로 추천 시스템과 검색 엔진을 다뤘다. 현재의 주요 전문 분야는 계산 효율적인 강화학습 알고리즘의 설계와 분석이다. 교수 소개는 비정상 밴딧(선택지의 보상 규칙이 시간에 따라 달라지는 순차 선택 문제), 오프라인 강화학습, 제약 강화학습을 연구해 왔다고 적으며, 최근에는 확산 모형(자료에 잡음을 더하는 과정을 되돌리는 방식으로 새 자료를 생성하는 모형)에도 관심이 있다고 밝힌다.[^home]

## 응용 분야

연구실이 현재 응용으로 내세우는 분야는 로봇과 운영과학이다. 구체적인 연구 문제로는 자료 훼손을 고려한 학습, 일련의 행동 전체에서 안전 조건을 지키는 학습, 영상·언어 모형을 활용한 안전한 자율주행 정책 학습을 제시한다.[^lab]

## 구성원

연구실 구성원 쪽의 현재 구성원 5명이다(2026-11-12). 석사과정 4명과 학사과정을 뜻하는 B.S. 표기 1명이며, 시작 시점과 연구 주제는 누리집 표기다.[^lab] "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Seokmin Ko (고석민) | 석사과정 | Dec. 2025 | Offline reinforcement learning under constraints: How can we efficiently learn a reward-maximizing policy subject to constraints using only offline data? | 1, 3 |
| Seobeom Jung (정서범) | 석사과정 | Mar 2026 | Robust offline-to-online reinforcement learning: How can we design RL algorithms that remain robust to data corruption when transitioning from offline data to online interaction? |  |
| Jihun Kim (김지훈) | 석사과정 | Mar 2026 | Trajectory-level safe reinforcement learning: How can we design safe RL algorithms that provide trajectory-level safety guarantees using only offline data? |  |
| Yeonseo Jang (장연서) | 석사과정 | Aug 2026 | Autonomous driving: How can we design computationally efficient RL algorithms for learning safe driving policies with vision-language models? |  |
| Taewon Goo (구태원) | B.S. | Mar 2026 | Optimal algorithms for constrained MDPs: Can we design online algorithms for constrained Markov decision processes that achieve information-theoretically optimal performance? | 1, 2 |

## 최근 5년 논문 목록

교수 누리집의 2021–2026년 논문 가운데 게시된 10편으로, 사전 공개본 2편과 학회 논문 구획 8편이다. 홍기혁 교수가 2025년 9월 1일 KAIST에 부임하기 전의 논문도 포함한다.[^home][^pubs] 제목·저자·학회명과 연도는 누리집 표기이며, 누리집이 연결한 사전 공개본을 함께 표시했다. 2026년 NeurIPS 논문은 소식에서 확인되는 상태인 "채택"으로 표시했다. 저자 이름 옆의 별표는 누리집이 밝힌 공동 기여 표시다.[^pubs]

**2026**

- Seokmin Ko, Taewon Goo, Kihyuk Hong. "DAMPER: Return-Prioritized Gradient Control for Smooth Policies". *Preprints (사전 공개본)*. <https://doi.org/10.48550/arXiv.2609.38903>
- Taewon Goo, Kihyuk Hong. "Minimax-Optimality of Posterior Sampling for Reinforcement Learning". *Preprints (사전 공개본)*. <https://doi.org/10.48550/arXiv.2609.33246>
- Seokmin Ko, Ambuj Tewari, Kihyuk Hong. "Offline Constrained Reinforcement Learning under Partial Coverage". *Advances in Neural Information Processing Systems 39 (채택)*. 사전 공개본 <https://arxiv.org/abs/2505.17506>

**2025**

- Marc Brooks\*, Gabriel Durham\*, Kihyuk Hong\*, Ambuj Tewari. "Generator-Mediated Bandits: Thompson Sampling for GenAI-Powered Adaptive Interventions". *Advances in Neural Information Processing Systems 38*. 사전 공개본 <https://arxiv.org/abs/2505.16311>
- Kihyuk Hong, Ambuj Tewari. "A Computationally Efficient Algorithm for Infinite-Horizon Average-Reward Linear MDPs". *Proceedings of the 42nd International Conference on Machine Learning*. 사전 공개본 <https://arxiv.org/abs/2504.11997>
- Kihyuk Hong, Woojin Chae, Yufan Zhang, Dabeen Lee, Ambuj Tewari. "Reinforcement Learning for Infinite-Horizon Average-Reward Linear MDPs via Approximation by Discounted-Reward MDPs". *Proceedings of the 28th International Conference on Artificial Intelligence and Statistics*. 사전 공개본 <https://arxiv.org/abs/2405.15050>
- Woojin Chae, Kihyuk Hong, Yufan Zhang, Ambuj Tewari, Dabeen Lee. "Learning Infinite-Horizon Average-Reward Linear Mixture MDPs of Bounded Span". *Proceedings of the 28th International Conference on Artificial Intelligence and Statistics*. 사전 공개본 <https://arxiv.org/abs/2410.14992>

**2024**

- Kihyuk Hong, Ambuj Tewari. "A Primal-Dual Algorithm for Offline Constrained Reinforcement Learning with Linear MDPs". *Proceedings of the 41st International Conference on Machine Learning*. 사전 공개본 <https://arxiv.org/abs/2402.04493>
- Kihyuk Hong, Yuhang Li, Ambuj Tewari. "A Primal-Dual-Critic Algorithm for Offline Constrained Reinforcement Learning". *Proceedings of the 27th International Conference on Artificial Intelligence and Statistics*. 사전 공개본 <https://arxiv.org/abs/2306.07818>

**2023**

- Kihyuk Hong, Yuhang Li, Ambuj Tewari. "An Optimization-Based Algorithm for Non-Stationary Kernel Bandits without Prior Knowledge". *Proceedings of the 26th International Conference on Artificial Intelligence and Statistics*. 사전 공개본 <https://arxiv.org/abs/2205.14775>

## 소식

교수 누리집 소식의 2021-10-13–2026-10-13 사이 논문 채택 소식 2건이다.[^home]

- 2026-09-25 · 「Offline Constrained Reinforcement Learning under Partial Coverage」 논문이 NeurIPS 2026에 채택됐다.
- 2025-09-19 · 「Generator-Mediated Bandits: Thompson Sampling for GenAI-Powered Adaptive Interventions」 논문이 NeurIPS 2025에 채택됐다.

## 연락과 위치

- 교수 업무 이메일: kihyukh@kaist.ac.kr[^home]
- 기관 전화: 042-350-3112[^dept]
- 교수 연구실: KAIST 산업경영학동 E2-2, 3104호(원문: IE B/D E2-2, #3104).[^dept]

## 각주
[^home]: Kihyuk Hong, 교수 소개와 News. <https://www.kihyukhong.com/> 관측 2026-11-12.
[^lab]: Reinforcement Learning Lab, 연구실 소개와 연구 주제. <https://www.kihyukhong.com/lab> 관측 2026-11-12.
[^pubs]: Kihyuk Hong, Publications. <https://www.kihyukhong.com/publication> 관측 2026-11-12.
[^dept]: KAIST 데이터사이언스대학원, 사람들: 홍기혁 교수 항목. <https://gsds.kaist.ac.kr/people> 관측 2026-11-12.
[^p1]: S. Ko, T. Goo, K. Hong, arXiv (사전 공개본) (온라인 2026-09-30). <https://doi.org/10.48550/arXiv.2609.38903> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.38903> 관측 2026-11-12.
[^p2]: T. Goo, K. Hong, arXiv (사전 공개본) (온라인 2026-09-27). <https://doi.org/10.48550/arXiv.2609.33246> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.33246> 관측 2026-11-12.
[^p3]: S. Ko, A. Tewari, K. Hong, arXiv (사전 공개본) (온라인 2025-05-23). <https://doi.org/10.48550/arXiv.2505.17506> 초록 기준(arXiv 판). 설명 대상은 2026-05-12 수정 제2판이다. 초록 원문 <https://arxiv.org/abs/2505.17506> 관측 2026-11-12.

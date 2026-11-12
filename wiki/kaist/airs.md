# AI and Robotic Systems Lab (AIRS)

**KAIST 산업및시스템공학과·데이터사이언스대학원 · 김우준 조교수**

- 영문 교수 이름: Woojun Kim
- 분야: 다중 에이전트 학습, 강화학습, 로봇의 계획과 제어
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 강화학습[^research], 다중 에이전트 시스템·분산 의사결정[^research], 다중 로봇 협업·물류 자동화[^research]
- 홈페이지: <https://airs.kaist.ac.kr/>
- 근거와 출처: [AI and Robotic Systems Lab 근거 페이지](airs-sources.md)

> 여러 주체가 각자 판단하면서 함께 일하고, 환경과 동료가 달라져도 행동을 조정하도록 학습 방법을 만드는 연구실이다. 이를 여러 대의 로봇이 일을 나누고 이동하는 시스템으로 연결한다.[^home][^research]

## 무엇을 연구하나

AIRS는 에이전트(주변 정보를 받아 행동을 정하는 주체) 여럿이 상호작용하는 시스템을 연구한다.[^research] 중심 방법은 강화학습(행동의 결과로 얻는 점수나 이득을 늘리는 방향으로 행동을 배우는 방법)이며, 에이전트의 탐색(아직 해 보지 않은 행동을 시도해 정보를 얻는 일)과 의사소통을 조정하는 학습 방법을 개발한다.[^research] 여러 주체가 상호작용하며 배우는 다중 에이전트 강화학습의 영문 이름은 Multi-Agent Reinforcement Learning(MARL)이다. 연구실은 이 방법으로 공동 목표를 위한 협력, 서로 이익이 충돌하는 경쟁, 두 상황이 섞인 의사결정을 다룬다. 로봇 시스템에서는 무엇을 할지 정하는 상위 계획과 실제 움직임을 조절하는 제어를 연결하고, 팀 규모·환경 변화·안전·공정성 문제를 연구한다.[^research]

대표 논문 1은 협력과 경쟁이 섞인 상황에서 다른 에이전트가 나눠 주는 보상에 지나치게 의존해 스스로 성과를 내는 행동을 배우지 못하는 문제를 다룬다. 받은 보상의 일부를 자신의 학습 신호(행동을 고치는 데 쓰는 보상 정보)에서 선택적으로 거절하는 장치를 기존 보상 공유 방법에 붙였다. 초록은 여러 실험 환경에서 의존과 희생 행동의 고착을 줄이고 공정성 지표를 개선했다고 설명한다.[^p1]

공동 목표가 있는 팀에서는 실행 중의 조정도 연구 대상이다. 대표 논문 2는 팀 전체의 상태를 관측할 수 있고 목표가 달라지는 장기 협력 시스템을 대상으로, 학습할 때만 전체 정보를 쓰는 방식의 한계를 논한다. 각 에이전트가 현장에서 행동을 정하되 조정자가 간헐적으로 상위 신호를 보내는 문제 설정을 제안한다. 환경 변화 뒤 팀이 다시 협력하도록 만드는 정보 구조에 관한 입장 논문이다.[^p2]

연구실은 기존 자료에서 행동을 배우는 오프라인 강화학습(학습 중 환경과 새로 상호작용하지 않고 이미 모인 경험 자료로 행동을 배우는 방법)과 모방학습(시범 행동에서 행동 선택 방법을 배우는 방법)도 다룬다. 배운 정책(상황에 따라 행동을 선택하는 규칙)을 실제 상호작용으로 조정하고, 새로운 동료·팀 구성·환경에서도 작동하는 일반화(학습에서 겪지 않은 대상이나 조건에도 배운 방법을 적용하는 능력)를 목표로 한다.[^research] 부임 전 KAIST 소속 시기의 대표 논문 3은 과제에 따라 탐색 전략을 선택하는 방법이고, 대표 논문 4·5는 협력 행동의 조정과 학습 구조의 표현력을 다룬다.[^p3][^p4][^p5]

로봇 연구에서는 여러 대에 작업을 배분하고 서로 충돌하지 않는 경로를 정하는 학습 방법을 개발한다. 관측과 사전 지식을 이용한 이동·점검·환경 관찰, 로봇 사이의 정보 공유, 현실 자료와 시뮬레이션(대상의 동작을 계산 모형으로 재현하는 방법)을 연결한 학습을 연구한다. 또 언어를 이용한 추론을 지각·계획·학습된 로봇 동작과 연결해 복잡한 일을 수행하고, 실행 결과를 계획과 실패 회복에 반영하는 방법을 다룬다.[^research]

## 주요 연구 주제

### 협력·경쟁 상황의 다중 에이전트 학습

공동 목표를 위한 행동 조정·탐색·의사소통 방법을 개발한다. 이익이 충돌하거나 일부만 일치하는 상황에서는 전략 적응과 인센티브(특정 행동을 선택하도록 만드는 이익이나 유인), 공정성을 다룬다.[^research] 대표 논문 1은 타인의 보상에 의존하는 학습 문제를, 대표 논문 4는 여러 에이전트의 행동 사이 정보 관계를 이용한 조정을 다룬다.[^p1][^p4]

### 기존 자료를 이용한 학습과 변화에 대한 적응

오프라인 강화학습·모방학습으로 배운 정책을 다른 에이전트와의 실제 상호작용에 맞춘다. 낯선 동료와의 협력, 불완전한 정보, 통신 실패와 예상하지 못한 혼란 속에서도 조정을 유지하는 방법을 연구한다.[^research]

### 로봇 팀의 작업 배분과 이동

팀의 크기나 환경이 바뀌어도 작업을 나누고 이동 경로를 조정하는 정책을 학습한다. 로봇이 관측 정보를 모으면서 이동·점검·환경 관찰을 수행하고, 그 정보를 팀 안에서 공유하는 방법을 개발한다.[^research] 대표 논문 2는 창고 로봇을 한 예로 드는 장기 협력 시스템에서 실행 중 조정이 필요한 조건을 논한다.[^p2]

### 언어 추론과 로봇 동작의 연결

언어를 이용한 추론과 주변 상황의 인식, 작업 계획, 배운 동작을 결합한다. 시뮬레이션과 실제 실행에서 얻은 결과로 계획·동작 선택·실패 회복 방법을 개선하는 것이 연구 방향이다.[^research]

## 대표 논문

교수가 저자로 참여한 KAIST 소속 시기의 논문 5편이다. 1·2는 2026년 8월 조교수 부임 이후의 연구이며, 3–5는 부임 전 KAIST 소속 시기의 논문이다.[^prof][^affiliation2023] 연구 갈래와 저자 역할, 초록을 기준으로 골랐다. 1·2는 NeurIPS 2026에 채택된 논문의 사전 공개본이며, '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.[^home][^p1][^p2]

| 번호 | 연도 | 논문·발표처 | 주요 저자와 교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](https://doi.org/10.48550/arXiv.2611.02875) · arXiv 사전 공개본, NeurIPS 2026 채택[^p1] | Woohyeon Byeon 외, Youngchul Sung. 김우준 교신저자 | 협력과 경쟁이 섞인 상황에서 다른 주체가 주는 보상에 지나치게 의존하는 문제를 찾아, 받은 보상의 일부를 학습 신호에서 선택적으로 거절하게 했다. 기존 보상 공유 방식에 붙일 수 있으며, 여러 환경에서 의존과 희생 행동의 고착을 줄였다. |
| 2 | 2026 | [Position: Beyond Training Time, Test-Time Coordination is Essential for Cooperative MARL](https://doi.org/10.48550/arXiv.2610.17409) · arXiv 사전 공개본, NeurIPS 2026 Position Paper Track 채택[^p2] | Dongsu Lee, Sooraj Sathish, Joonkyung Kim, Woojun Kim, Amy Zhang. 김우준 공저자 | 팀 전체의 상태를 볼 수 있고 목표가 변하는 장기 협력 시스템에서는 학습 이후에도 조정 통로가 필요하다고 주장한다. 개별 주체는 현장에서 행동하고 조정자는 때때로 상위 신호를 보내는 문제 설정을 제안한다. |
| 3 | 2023 | [LESSON: Learning to Integrate Exploration Strategies for Reinforcement Learning via an Option Framework](https://proceedings.mlr.press/v202/kim23k.html) · ICML, PMLR 202, 16619–16638[^p3] | Woojun Kim, Jeonghye Kim, Youngchul Sung. 김우준 첫 번째 저자, 누리집의 *는 동등 기여 | 여러 탐색 전략을 한 학습 구조에 묶고, 과제에 맞는 전략을 스스로 선택하도록 했다. 새 행동을 알아보는 탐색과 이미 유리하다고 배운 행동을 쓰는 활용 사이의 균형을 학습하며, MiniGrid와 Atari 환경에서 평가했다. |
| 4 | 2023 | [A Variational Approach to Mutual Information-Based Coordination for Multi-Agent Reinforcement Learning](https://doi.org/10.65109/tgsd6546) · AAMAS[^p4] | Woojun Kim, Whiyoung Jung, Myungsik Cho, Youngchul Sung. 김우준 1저자 | 여러 에이전트의 행동 사이 정보 관계를 누적 성과와 함께 고려해 협력 행동을 배우게 했다. 계산 가능한 목표식과 학습 방법을 만들고, 함께 학습한 뒤 각자가 행동하는 방식으로 조정이 필요한 게임에서 평가했다. |
| 5 | 2023 | [Parameter Sharing with Network Pruning for Scalable Multi-Agent Deep Reinforcement Learning](https://doi.org/10.65109/vuzv6508) · AAMAS[^p5] | Woojun Kim, Youngchul Sung. 김우준 1저자 | 여러 에이전트가 같은 매개변수(학습으로 정해지는 모형의 조절값)를 쓰면 학습 시간이 줄고 자료를 효율적으로 쓸 수 있지만 서로 다른 행동을 표현하는 데 제약이 생긴다. 신경망(연결된 계산 단위들의 연결 강도를 조절하며 자료의 관계를 학습하는 모형)의 일부를 구조 단위로 제거해, 매개변수를 늘리지 않고 팀의 행동 표현력을 높이는 방법을 제안했다. |

## 교수와 전문 분야

김우준(Woojun Kim)은 KAIST 산업및시스템공학과와 데이터사이언스대학원의 조교수다. 2026년 8월 산업및시스템공학과 조교수로 부임했다. 이전에는 Carnegie Mellon University의 Robotics Institute에서 Katia Sycara 교수의 지도로 박사후연구원으로 일했으며(2023년 10월–2026년 8월), 2023년 3–9월에는 KAIST 전기공학 분야의 박사후연구원이었다.[^prof]

고려대학교 전기공학 학사(2016), KAIST 전기공학 석사(2018)·박사(2023)를 받았다. KAIST 석사·박사와 박사후연구원 과정의 지도교수는 Youngchul Sung이다.[^prof] 전문 분야는 다중 에이전트 강화학습과 협력·경쟁 의사결정, 탐색 방법, 기존 자료를 이용한 학습, 로봇 팀의 계획과 제어다. 연구 소개는 개별 에이전트의 학습 방법부터 팀의 실행 중 조정까지를 연구 주제로 든다.[^research] 2026년 가을학기 강의로 'Convex optimization'을 게시했다.[^teaching]

## 응용 분야

여러 로봇의 작업 배분과 충돌 없는 이동, 이동 중 정보 수집, 점검과 환경 관찰이 연구실이 제시한 응용이다. 현실에서 모은 자료와 시뮬레이션을 연결해 배운 동작을 실제 로봇에 적용하고, 실패 뒤 회복하는 방법을 목표로 한다.[^research] 수행 과제로는 인공지능 기반 다크 팩토리(Dark Factory) 설계·통합과 대규모 산업용 로봇 시스템의 다중 에이전트 학습을 제시한다.[^research]

## 구성원

2026년 11월 12일 People 페이지에 게시된 대학원생 2명과 인턴 3명이다. 과정·소속 약어와 시작 표기는 누리집을 따른다. GSDS는 데이터사이언스대학원, ISE는 산업및시스템공학과다.[^members][^prof] 연구 주제는 두 대학원생의 개별 소개에 게시된 영어 문장을 한국어로 옮긴 것이다.[^member-changsung][^member-rindi] '대표 논문 참여'는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Changsung Lee | 석사과정 (GSDS) | 2026.09- | 다중 에이전트 강화학습과 다중 에이전트 경로 찾기(MAPF, Multi-Agent Path Finding)를 연구한다. 지도가 바뀌어도 많은 로봇이 막히지 않고 계속 움직이는 문제에 집중하며, 공장·창고 자동화에 적용하는 데 관심이 있다. |  |
| Rindi Kusumawardani | 박사과정 (ISE) | 2026.09- | 지능형 제조 시스템, 특히 인공지능 기반 로봇 항법·자동화·최적화를 연구 관심으로 적는다. |  |
| Jisoo Kim | 인턴 | 2026.09- |  |  |
| Seheon Kim | 인턴 | 2026.09- |  |  |
| Jiwan Shin | 인턴 | 2026.10- |  |  |

## 최근 5년 논문 목록

연구실 Publications에 게시된 2021–2026년 구역의 학회·학술지·워크숍 논문 중 아래 39편이다. 교수의 2026년 8월 KAIST 조교수 부임 전 연구를 포함한다.[^prof][^pubs] 누리집의 *는 동등 기여, †는 교신·지도 저자 표시이며, 개별 저자의 역할은 그 표기 범위를 따른다. NeurIPS 2026 논문 3편은 누리집 소식에 따라 '채택'으로 표시했다. HICSS 논문의 2026년 표기는 누리집 기재 연도다. 같은 제목의 학회판과 워크숍판은 각각 별도 게시 항목이다.[^home][^pubs]

**2026**

- Woohyeon Byeon, Seongmin Kim, Jiwon Jeon, Woojun Kim†(Equal advising), Youngchul Sung†. "AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games". *Conference on Neural Information Processsing Systems (NeurIPS) 2026 (채택), 사전 공개본 DOI: 10.48550/arXiv.2611.02875*.
- Jiwon Jeon, Myungsik Cho, Woojun Kim, Seongmin Kim, Woohyeon Byeon, Seungyul Han, Youngchul Sung. "MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals". *Conference on Neural Information Processsing Systems (NeurIPS) 2026 (채택)*.
- Dongsu Lee, Sooraj Sathish, Joonkyung Kim, Woojun Kim, Amy Zhang. "Beyond Training Time, Test-Time Coordination is Essential for Cooperative MARL". *Conference on Neural Information Processsing Systems (NeurIPS), Position Paper Track, 2026 (채택), 사전 공개본 DOI: 10.48550/arXiv.2610.17409*.
- Ini Oguntola, Renos Zabounidis, Simon Stepputtis, Joseph Campbell, Woojun Kim, Katia Sycara. "Deception Is Its Own Reward: Competitive Multi-Agent Reinforcement Learning via Theory of Mind". *The 60th Hawaii International Conference on System Sciences (HICSS), 2026*.
- Emanuel Munoz Panduro, Siva Kailas, Woojun Kim, Wenhao Luo, Katia Sycara. "Risk-Aware Navigation in Dynamic Smoke Environments via Probabilistic Fourier Neural Operators". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2026*.
- Renos Zabounidis, Roy Siegelmann, Mohamad Qadri, Woojun Kim, Simon Stepputtis, Katia Sycara. "Overcoming Valid Action Suppression in Unmasked Policy Gradient Algorithms". *Reinforcement Learning Conference (RLC) 2026*.
- Srujan Deolasee, Siva Kailas, Wenhao Luo, Katia Sycara, Woojun Kim†. "DyPNIPP: Predicting Environment Dynamics for RL-based Robust Informative Path Planning". *Learning for Dynamics and Control Conference (L4DC) 2026*.
- Srikar Babu Gadipudi, Srujan Deolasee, Siva Kailas, Wenhao Luo, Katia Sycara, Woojun Kim†. "OffRIPP: Offline RL-based Informative Path Planning". *Learning for Dynamics and Control Conference (L4DC) 2026*.
- Woojun Kim, Katia Sycara. "B3C: A Minimalist Approach to Offline Multi-Agent Reinforcement Learning". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2026*.
- Andrew Ni, Simon Stepputtis, Stefanos Nikolaidis, Michael Lewis, Katia Sycara, Woojun Kim†. "Theory of Mind Guided Strategy Adaptation for Zero-Shot Coordination". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2026*.
- Seongmin Kim, Giseung Park, Woojun Kim, Jeewon Jeon, Seungyul Han, Youngchul Sung. "Generalized Per-Agent Advantage Estimation for Multi-Agent Policy Optimization". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2026*.

**2025**

- Woojun Kim, Katia Sycara. "Fair Cooperation in Mixed-Motive Games via Conflict-Aware Gradient Adjustment". *Conference on Neural Information Processsing Systems (NeurIPS) 2025*.
- Benjamin Li, Shuyang Shi, Lucia Romero, Huao Li, Yaqi Xie, Woojun Kim, Stefanos Nikolaidis, Charles Michael Lewis, Katia Sycara, Simon Stepputtis†. "Adaptively Coordinating with Novel Partners via Learned Latent Strategies". *Conference on Neural Information Processsing Systems (NeurIPS) 2025*.
- Joonkyung Kim, Joonyeol Sim, Woojun Kim, Katia Sycara, Changjoo Nam†. "CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation". *Conference on Robot Learning (CoRL) 2025*.
- Lingpeng Chen, Siva Kailas, Srujan Deolasee, Wenhao Luo, Katia Sycara, Woojun Kim†. "Distributed Multi-robot Source Seeking in Unknown Environments with Unknown Number of Sources". *IEEE International Conference on Robotics and Automation (ICRA) 2025*.
- Joonkyung Kim, Sangjin Park, Wonjong Lee, Woojun Kim, Nakju Doh, Changjoo Nam†. "Escaping Local Minima: Hybrid Artificial Potential Field with Wall-Follower for Decentralized Multi-Robot Navigation". *IEEE International Conference on Robotics and Automation (ICRA) 2025*.
- Siva Kailas, Srujan Deolasee, Wenhao Luo, Woojun Kim, Katia Sycara†. "Integrating Multi-Robot Adaptive Sampling and Informative Path Planning for Spatiotemporal Natural Environment Prediction". *IEEE International Conference on Robotics and Automation (ICRA) 2025*.
- Renos Zabounidis, Ini Oguntola, Konghao Zhao, Joseph Campbell, Woojun Kim, Simon Stepputtis, Katia Sycara. "Disentangled Concept-Residual Models: Bridging the Interpretability–Performance Gap for Incomplete Concept Sets". *Transactions on Machine Learning Research (TMLR), 2025*.
- Muhan Lin, Shuyang Shi, Yue Guo, Vaishnav Tadiparthi, Behdad Chalaki, Ehsan Moradi Pari, Simon Stepputtis, Woojun Kim, Joseph Campbell, Katia Sycara†. "Speaking the Language of Teamwork: LLM-Guided Credit Assignment in Multi-Agent Reinforcement Learning". *NeurIPS Workshop on Aligning Reinforcement Learning Experimentalists and Theorists, 2025*.
- Benjamin Li, Shuyang Shi, Lucia Romero, Huao Li, Yaqi Xie, Woojun Kim, Stefanos Nikolaidis, Charles Michael Lewis, Katia Sycara, Simon Stepputtis†. "Modeling Latent Partner Strategies for Adaptive Zero-Shot Human-Agent Collaboration". *RSS Workshop on Generative AI and Human-Robot Interaction, 2025*.
- Srikar Babu Gadipudi, Srujan Deolasee, Siva Kailas, Wenhao Luo, Katia Sycara, Woojun Kim†. "OffRIPP: Offline RL-based Informative Path Planning". *ICRA Workshop on Beyond the Lab: Robust Planning and Control in Real World Scenarios, 2025*.
- Srujan Deolasee, Siva Kailas, Wenhao Luo, Katia Sycara, Woojun Kim†. "DyPNIPP: Predicting Environment Dynamics for RL-based Robust Informative Path Planning". *ICRA Workshop on Beyond the Lab: Robust Planning and Control in Real World Scenarios, 2025*.

**2024**

- Jeonghye Kim, Suyoung Lee, Woojun Kim, Youngchul Sung†. "Adaptive Q-Aid for Conditional Supervised Learning in Offline Reinforcement Learning". *Conference on Neural Information Processsing Systems (NeurIPS) 2024*.
- Samuel Li, Sarthak Bhagat, Joseph Campbell, Yaqi Xie, Woojun Kim, Katia Sycara, Simon Stepputtis†. "ShapeGrasp: Zero-Shot Object Grasping with LLMs via Geometric Decomposition". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2024*.
- Jeonghye Kim, Suyoung Lee, Woojun Kim†(Equal advising), Youngchul Sung†. "Decision ConvFormer: Local Filtering in MetaFormer is Sufficient for Decision Making". *International Conference on Learning Representation (ICLR), 2024*.
- Zirui Wang, Xinran Zhao, Simon Stepputtis, Woojun Kim, Tongshuang Wu, Katia Sycara, Yaqi Xie†. "HiMemFormer: Hierarchical Memory-Aware Transformer for Multi-Agent Action Anticipation". *NeurIPS Workshop on Video-Language Models, 2024*.
- Samuel Li, Sarthak Bhagat, Joseph Campbell, Yaqi Xie, Woojun Kim, Katia Sycara, Simon Stepputtis†. "ShapeGrasp: Zero-Shot Object Grasping with LLMs via Geometric Decomposition". *ICRA Workshop on 3D Visual Representations for Robot Manipulation, 2024*.

**2023**

- Woojun Kim\*, YongJae Shin\*, Jongeui Park, Youngchul Sung†. "Sample-Efficient and Safe Reinforcement Learning via Reset Deep Ensemble Agents". *Conference on Neural Information Processsing Systems (NeurIPS) 2023*.
- Sungho Choi, Seungyul Han†, Woojun Kim, Jongseong Chae, Whiyoung Jung, Youngchul Sung. "Domain Adaptive Imitation Learning with Visual Observation". *Conference on Neural Information Processsing Systems (NeurIPS) 2023*.
- Woojun Kim\*, Jeonghye Kim\*, Youngchul Sung†. "LESSON: Learning to Integrate Exploration Strategies for Reinforcement Learning via an Option Framework". *International Conference on Machine Learning (ICML) 2023*.
- Woojun Kim, Youngchul Sung†. "An Adaptive Entropy-Regularization Framework for Multi-Agent Reinforcement Learning". *International Conference on Machine Learning (ICML) 2023*.
- Woojun Kim, Youngchul Sung†. "Parameter Sharing with Network Pruning for Multi-Agent Deep Reinforcement Learning". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2023, DOI: 10.65109/vuzv6508[^biblio2023]*.
- Woojun Kim, Whiyoung Jung, Myungsik Cho, Youngchul Sung†. "A Variational Approach to Mutual Information-Based Coordination for Multi-Agent Reinforcement Learning". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2023, DOI: 10.65109/tgsd6546[^biblio2023]*.
- Jeonghye Kim, Suyoung Lee, Woojun Kim†(Equal advising), Youngchul Sung†. "Decision ConvFormer: Local Filtering in MetaFormer is Sufficient for Decision Making". *NeurIPS Workshop on Foundation Model for Decision Making (FMDM), 2023*.
- Seongmin Kim, Seungyul Han, Woojun Kim, Jeewon Jeon, Youngchul Sung†. "Off-Policy Multi-Agent Policy Optimization with Multi-Step Counterfactual Advantage Estimation". *Adaptive and Learning Agents (ALA) Workshop at AAMAS 2023*.

**2022**

- Jeewon Jeon, Woojun Kim†(Equal advising), Whiyoung Jung, Youngchul Sung†. "MASER: Multi-Agent Reinforcement Learning with Subgoals Generated from Experience Replay Buffer". *International Conference on Machine Learning (ICML) 2022*.
- Md. Shahjalal, Woojun Kim, Waqas Khalid, Seokjae Moon, Murad Khan, ShuZhi Liu, Suhyeon Lim, Eunjin Kim, Deok-Won Yun, Joohyun Lee, Won-Cheol Lee , Seung-Hoon Hwang, Dongkyun Kim, Jang-Won Lee, Heejung Yu, Youngchul Sung, Yeong Min Jang†. "Enabling Technologies for AI Empowered 6G Massive Radio Access Networks". *ICT Express, July 2022*.
- Woojun Kim, Youngchul Sung†. "An Adaptive Entropy-Regularization Framework for Multi-Agent Reinforcement Learning". *Decision Awareness in Reinforcement Learning (DARL) Workshop at ICML 2022*.
- Woojun Kim, Whiyoung Jung, Myungsik Cho, Youngchul Sung†. "A Variational Approach to Mutual Information-Based Coordination for Multi-Agent Reinforcement Learning". *International AI for Agent-Based Modelling (AI4ABM) Workshop at ICML 2022*.

## 과제

연구 소개에 게시된 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제 2건이다. 제목·지원 기관·기간은 누리집 표기를 따른다.[^research]

- AI-Based Dark Factory Design and Integration Solution (지원 National IT Industry Promotion Agency (NIPA); 기간 2026.08-2030.12)
- Scalable and Resilient Multi-Agent Reinforcement Learning for Large-Scale Industrial Robotic Systems (지원 KAIST; 기간 2026.08-2029.12)

## 수상과 선정

연구 소개·소식·논문 목록에 게시된 2021년 10월 13일–2026년 10월 13일의 수상·후보 선정 3건이다. 모두 교수의 2026년 8월 KAIST 조교수 부임 전 연구에 관한 항목이다. 월 표기는 소식의 연월이며, 한 논문의 두 부문 후보 선정은 한 항목에 함께 적었다.[^home][^research][^pubs][^prof]

- 2026-03 · Generalized Per-Agent Advantage Estimation for Multi-Agent Policy Optimization: AAMAS 2026 Best Paper Nomination
- 2025-07 · Modeling Latent Partner Strategies for Adaptive Zero-Shot Human-Agent Collaboration: RSS 2025 GenAI-HRI Workshop Best Paper Award
- 2025-05 · Distributed Multi-Robot Source Seeking in Unknown Environments with Unknown Number of Sources: ICRA 2025 Best Conference Paper Finalist 및 Best Paper Finalist on Multi-Robot Systems

## 소식

첫 화면 소식의 논문 채택 12건이다. 2023년 1월–2026년 9월의 월 표기를 따르며, 교수의 2026년 8월 KAIST 조교수 부임 전 연구를 포함한다.[^home][^prof]

- 2026-09 · NeurIPS 2026에 논문 3편이 채택되었다.
- 2026-06 · IROS 2026에 논문 1편이 채택되었다.
- 2026-01 · L4DC 2026에 논문 2편이 채택되었으며, 그중 1편은 구두 발표다.
- 2026-01 · AAMAS 2026에 논문 3편이 채택되었다.
- 2025-09 · NeurIPS 2025에 논문 2편이 채택되었으며, 그중 1편은 스포트라이트 발표다.
- 2025-01 · ICRA 2025에 논문 3편이 채택되었다.
- 2024-09 · NeurIPS 2024에 논문 1편이 채택되었다.
- 2024-07 · IROS 2024에 논문 1편이 구두 발표로 채택되었다.
- 2024-01 · ICLR 2024에 논문 1편이 스포트라이트 발표로 채택되었다.
- 2023-09 · NeurIPS 2023에 논문 2편과 워크숍 논문 1편이 채택되었다.
- 2023-04 · ICML 2023에 논문 2편이 채택되었다.
- 2023-01 · AAMAS 2023에 논문 2편과 워크숍 논문 1편이 채택되었다.

## 연락과 위치

- 김우준 교수 업무 이메일: woojun.kim@kaist.ac.kr.[^home][^members][^dept]
- 기관 전화: 042-350-3119.[^dept]

## 각주
[^home]: AIRS 첫 화면. <https://airs.kaist.ac.kr/> (관측일 2026-11-12).
[^members]: AIRS, People. <https://airs.kaist.ac.kr/People-b57f2623b66e82e385358175e11e64ce> (관측일 2026-11-12).
[^research]: AIRS, Research. <https://airs.kaist.ac.kr/Research-116f2623b66e823f8d278163e0fb0b0a> (관측일 2026-11-12).
[^pubs]: AIRS, Publications. <https://airs.kaist.ac.kr/Publications-061f2623b66e82a9a38801fc4a4652f4> (관측일 2026-11-12).
[^teaching]: AIRS, Teaching. <https://airs.kaist.ac.kr/Teaching-b29f2623b66e839ca01101dd527d5c7d> (관측일 2026-11-12).
[^prof]: AIRS, Woojun Kim 교수 소개. <https://airs.kaist.ac.kr/Woojun-Kim-b94f2623b66e821baf8a0180d8a66d89> (관측일 2026-11-12).
[^dept]: KAIST 데이터사이언스대학원, 사람들. <https://gsds.kaist.ac.kr/people> (관측일 2026-11-12).
[^member-changsung]: AIRS, Changsung Lee 개별 소개. <https://airs.kaist.ac.kr/Changsung-Lee-MS-GSDS-2026-09-3ccf2623b66e8078bb87ff9795e01e98> (관측일 2026-11-12).
[^member-rindi]: AIRS, Rindi Kusumawardani 개별 소개. <https://airs.kaist.ac.kr/Rindi-Kusumawardani-PhD-ISE-2026-09-3ccf2623b66e8058a8edd1999aacdcb2> (관측일 2026-11-12).
[^biblio2023]: W. Kim·Y. Sung, “Parameter Sharing with Network Pruning for Scalable Multi-Agent Deep Reinforcement Learning”, DOI 10.65109/vuzv6508; W. Kim·W. Jung·M. Cho·Y. Sung, “A Variational Approach to Mutual Information-Based Coordination for Multi-Agent Reinforcement Learning”, DOI 10.65109/tgsd6546. AAMAS (2023), OpenAlex 등록 서지. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084429594,publication_year:2021-2026> (관측일 2026-11-12).
[^affiliation2023]: OpenAlex, Woojun Kim의 2023년 논문 저자 소속 기록. LESSON의 소속은 arXiv 판 DOI 10.48550/arxiv.2310.03342 기록에 근거하며, AAMAS 두 편은 DOI 10.65109/tgsd6546·10.65109/vuzv6508의 기록이다. <https://api.openalex.org/works?per-page=5&select=id,doi,title,publication_date,primary_location,authorships&search=LESSON%3A%20Learning%20to%20Integrate%20Exploration%20Strategies%20for%20Reinforcement%20Learning%20via%20an%20Option%20Framework> <https://api.openalex.org/works?per-page=5&select=id,doi,title,publication_date,primary_location,authorships&search=A%20Variational%20Approach%20to%20Mutual%20Information-Based%20Coordination%20for%20Multi-Agent%20Reinforcement%20Learning> <https://api.openalex.org/works/doi:10.65109/vuzv6508?select=id,doi,title,publication_date,primary_location,authorships> (관측일 2026-11-13).
[^p1]: W. Byeon 외, Y. Sung, arXiv:2611.02875v2; NeurIPS 2026 (채택) (온라인 2026-11-02). <https://doi.org/10.48550/arXiv.2611.02875> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2611.02875> (관측일 2026-11-12).
[^p2]: D. Lee 외, A. Zhang, arXiv:2610.17409v1; NeurIPS 2026 Position Paper Track (채택) (온라인 2026-10-12). <https://doi.org/10.48550/arXiv.2610.17409> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.17409> (관측일 2026-11-12).
[^p3]: W. Kim, J. Kim, Y. Sung, Proceedings of the 40th International Conference on Machine Learning 202, 16619-16638 (2023). <https://proceedings.mlr.press/v202/kim23k.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/kim23k.html> (관측일 2026-11-12).
[^p4]: W. Kim, W. Jung, M. Cho, Y. Sung, International Conference on Autonomous Agents and Multiagent Systems (AAMAS) (2023). <https://doi.org/10.65109/tgsd6546> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084429594,publication_year:2021-2026> (관측일 2026-11-12).
[^p5]: W. Kim, Y. Sung, International Conference on Autonomous Agents and Multiagent Systems (AAMAS) (2023). <https://doi.org/10.65109/vuzv6508> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084429594,publication_year:2021-2026> (관측일 2026-11-12).

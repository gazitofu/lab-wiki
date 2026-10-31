# 시스템 지능 연구실 (System Intelligence Lab, SILAB)

**KAIST 산업및시스템공학과·데이터사이언스대학원·AI대학원 · 박진규 부교수**

- 분야: 다중 에이전트 의사결정, 강화학습, 생성 모형을 이용한 탐색, 조합 최적화와 블랙박스 최적화
- 대분야: 컴퓨팅·AI, 산업·시스템
- 태그: 강화학습[^home][^p6][^p7], 수리 최적화·최적화 알고리즘[^p1][^p3][^p7], 다중 에이전트 시스템·분산 의사결정[^home][^p3][^p5]
- 홈페이지: <http://silab.kaist.ac.kr/>
- 근거와 출처: [SILAB 근거 페이지](silab-sources.md)

> 여러 행동 주체의 의사결정과 복잡한 최적화 문제를 다루며, 강화학습과 생성 모형으로 경로·일정·설계안을 찾는 알고리즘을 만드는 연구실이다.[^home][^p1][^p3]

## 무엇을 연구하나

SILAB은 박진규 부교수가 이끄는 KAIST 연구실이다. 복잡한 현실의 의사결정 문제를 여러 종류에 걸쳐 풀 수 있는 범용 에이전트(여러 과제에서 상황을 판단하고 행동을 선택하는 주체)를 개발하는 것이 목표다. 특히 생성 모형(학습한 자료의 분포를 바탕으로 새 자료를 만드는 계산 모형), 강화학습(행동의 결과에 따라 주어지는 보상을 바탕으로 행동 규칙을 배우는 기계학습), 다중 에이전트 시스템(여러 주체가 각자의 정보와 판단을 바탕으로 서로 영향을 주고받는 체계)에 관심을 둔다. 기계학습은 자료에서 예측·판단 규칙을 배우는 계산 방법을 뜻한다.[^home][^team]

첫 갈래는 **여러 주체의 행동을 조정하는 방법**이다. PARCO(Parallel AutoRegressive Combinatorial Optimization)는 차량 경로와 일정 문제에서 여러 주체가 다음 행동을 병렬로 정하도록 하고, 서로 정보를 전달하는 부분과 선택이 충돌할 때 우선순위로 처리하는 부분을 결합했다. 이는 가능한 선택의 조합 가운데 목표에 맞는 답을 찾는 조합 최적화를 강화학습으로 푸는 연구다. STRIL(Strategy Representation for Imitation Learning)은 다중 에이전트 게임의 행동 기록에서 전략을 나타내는 표현을 배우고, 그 표현으로 모방할 자료를 고른다. 모방학습은 다른 주체의 행동 기록에서 행동 규칙을 배우는 방법이다.[^p3][^p5]

둘째는 **생성 모형으로 새로운 설계 후보를 찾는 방법**이다. 블랙박스 최적화(목적 함수의 내부 식을 직접 이용하지 않고 입력과 평가 결과로 좋은 입력을 찾는 방법)에서는 후보를 평가할 기회와 예측의 불확실성을 함께 고려해야 한다. DiBO는 확산 모형(자료에 잡음을 더하는 과정의 역방향 변환을 학습해 자료를 만드는 생성 모형)과 여러 예측 모형을 결합하고, 관측 자료를 반영한 후보 분포에서 다음 후보를 고른다. 제약이 있는 문제를 다룬 논문은 목적값과 제약 위반을 예측하고, 생성 모형이 자료를 표현하는 잠재 공간(관측 자료를 나타내는 내부 변수의 공간)에서 제약 조건을 지키는 유망한 후보를 찾는다.[^p2][^p1]

셋째는 **행동 기록과 문제의 구조를 이용한 학습·탐색**이다. GTA(Generative Trajectory Augmentation)는 환경과 새로 상호작용하지 않고 기존 기록으로 배우는 오프라인 강화학습을 위해, 보상이 높으면서 환경의 움직임에도 맞는 행동 경로 자료를 생성한다. Sym-NCO는 문제와 해를 회전하거나 반사해도 성질이 유지되는 대칭성을 학습에 반영한다. Neural Genetic Search(NGS)는 여러 부모 후보의 특성을 조합하는 유전 알고리즘의 교차를 생성 모형에 넣어, 학습을 마친 모형에서 답을 찾는 과정을 바꾼다. 이 논문은 경로 문제, 언어 모형을 공격하는 입력문 생성, 분자 설계에서 방법을 시험했다.[^p6][^p7][^p4]

생물 서열 설계도 알고리즘의 연구 대상이다. 「Improved Off-policy Reinforcement Learning in Biological Sequence Design」은 원하는 성질의 서열을 찾을 때, 실제 평가를 대신하는 예측 모형이 낯선 서열에서 잘못된 점수를 낼 수 있다는 문제를 다룬다. 제안한 탐색 방법은 점수가 높은 기존 서열의 일부를 가린 뒤 다시 채우며, 예측의 불확실성에 맞춰 탐색 범위를 조절한다. 단백질과 유전 물질의 서열을 대상으로 하는 새 탐색 방법의 개발이다.[^p8]

## 주요 연구 주제

### 1. 다중 에이전트의 협력과 전략 학습

여러 주체가 동시에 경로·일정을 만들 때의 정보 전달과 충돌 처리, 게임의 행동 기록에서 전략을 구분하고 학습에 쓸 자료를 고르는 방법을 연구한다. 대표 논문은 PARCO와 STRIL이다.[^p3][^p5]

### 2. 생성 모형을 이용한 블랙박스 최적화

평가 결과와 불확실성으로 다음 후보를 고르는 DiBO, 목적값을 높이면서 제약 조건을 지키는 후보를 잠재 공간에서 찾는 방법을 연구한다. 내부 계산식을 이용하기 어려운 문제의 탐색 알고리즘이 중심이다.[^p1][^p2]

### 3. 오프라인 강화학습과 조합 최적화

GTA로 학습용 행동 경로를 보완하고, Sym-NCO로 문제와 해의 대칭성을 활용하며, NGS로 생성 모형의 후보 조합과 탐색을 설계한다. 학습 자료를 바꾸는 방법과 답을 만드는 절차를 함께 다룬다.[^p6][^p7][^p4]

### 4. 생물 서열을 위한 탐색 방법

평가를 대신하는 모형의 신뢰도를 고려해 새로운 서열을 찾는 방법을 개발한다. 기존 서열의 점수와 예측의 불확실성에 맞춰 탐색을 조절하는 강화학습 연구가 여기에 해당한다.[^p8]

## 대표 논문

연구 갈래를 나누어 2022–2026년 논문 8편을 골랐다. 아래 연도와 학회 이름은 연구실 목록의 표기이며, 제목 링크와 각주의 초록은 arXiv 사전 공개본이다. NeurIPS 2026 항목은 연구실 소식의 채택 표기를 따랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 저자 위치는 전체 저자 순서이며 교신저자 역할을 뜻하지 않는다.[^pubs][^home]

| 번호 | 연도 | 논문 | 발표처 | 박진규의 저자 위치 | 쉽게 말하면 |
|---|---|---|---|---|---|
| 1 | 2026 | [Posterior Inference in Latent Space for Scalable Constrained Black-box Optimization](https://arxiv.org/abs/2507.00480) | NeurIPS 2026 (채택), arXiv 판 | 마지막 | 목적값과 제약 위반을 예측하는 모형을 배우고, 생성 모형의 내부 표현 공간에서 제약을 지키는 유망한 후보를 찾는 방법을 제안했다.[^p1] |
| 2 | 2025 | [Posterior Inference with Diffusion Models for High-dimensional Black-box Optimization](https://arxiv.org/abs/2502.16824) | ICML 2025, arXiv 판 | 마지막 | 확산 모형과 불확실성을 예측하는 여러 모형을 결합해, 새 영역을 살피는 일과 유망한 후보를 찾는 일을 함께 고려하는 DiBO를 제안했다.[^p2] |
| 3 | 2025 | [PARCO: Parallel AutoRegressive Models for Multi-Agent Combinatorial Optimization](https://arxiv.org/abs/2409.03811) | NeurIPS 2025, arXiv 판 | 마지막 | 여러 주체가 차량 경로와 일정을 병렬로 만들도록 하고, 정보 전달과 선택 충돌 처리를 결합한 강화학습 틀을 제안했다.[^p3] |
| 4 | 2025 | [Neural Genetic Search in Discrete Spaces](https://arxiv.org/abs/2502.10433) | ICML 2025, arXiv 판 | 5명 중 넷째 | 부모 후보를 조건으로 새 후보를 생성하는 방식으로 유전 알고리즘의 교차를 구현했다. 경로 문제, 언어 모형 공격용 입력문, 분자 설계에서 시험했다.[^p4] |
| 5 | 2025 | [Learning Strategy Representation for Imitation Learning in Multi-Agent Games](https://arxiv.org/abs/2409.19363) | AAAI 2025, arXiv 판 | 마지막 | 게임 참여자의 행동 기록에서 전략 표현을 배우고, 그 표현을 바탕으로 모방학습에 적합한 자료를 고르는 STRIL을 제안했다.[^p5] |
| 6 | 2024 | [GTA: Generative Trajectory Augmentation with Guidance for Offline Reinforcement Learning](https://arxiv.org/abs/2405.16907) | NeurIPS 2024, arXiv 판 | 마지막 | 기존 행동 경로에 잡음을 더한 뒤 확산 모형으로 복원하면서, 보상이 높고 환경의 움직임에도 맞는 학습 자료를 만들었다.[^p6] |
| 7 | 2022 | [Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization](https://arxiv.org/abs/2205.13209) | NeurIPS 2022, arXiv 판 | 마지막 | 회전·반사와 같은 문제·해의 대칭성을 강화학습에 반영해, 경로와 방문 순서를 정하는 문제의 풀이를 학습했다.[^p7] |
| 8 | 2025 | [Improved Off-policy Reinforcement Learning in Biological Sequence Design](https://arxiv.org/abs/2410.04461) | ICML 2025, arXiv 판 | 마지막 | 예측 모형이 믿을 만한 영역에서 서열을 탐색하도록 하는 새 방법을 제안했다. 기존 서열의 일부를 가렸다가 채우고, 예측의 불확실성에 맞춰 탐색을 조절했다.[^p8] |

## 교수와 전문 분야

박진규(Jinkyoo Park)는 산업및시스템공학과 부교수이며 데이터사이언스대학원과 AI대학원 겸임 부교수다.[^team][^gsds] 연구실의 목표는 현실의 복잡한 의사결정 문제를 푸는 범용 에이전트의 개발이다.[^home]

대표 논문으로 본 전문 분야는 생성 모형을 이용한 블랙박스 최적화, 강화학습 기반 조합 최적화, 다중 에이전트의 협력·전략 학습이다. 목적값과 제약을 함께 고려한 후보 선택(대표 논문 1, 2), 여러 주체의 병렬 의사결정과 행동 기록 학습(3, 5), 생성 자료·대칭성·교차를 이용한 학습과 탐색(4, 6, 7)을 다뤘다. 생물 서열 설계에서도 예측 모형의 불확실성을 고려한 탐색 알고리즘을 제안했다(8).[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

대표 논문은 차량 경로와 일정 계획, 여러 참여자가 경쟁하는 게임의 학습, 언어 모형 공격용 입력문 생성, 분자 설계, 단백질과 유전 물질의 서열 설계를 다룬다.[^p3][^p4][^p5][^p8] 연구실 논문 목록에는 풍력발전단지 배치, 교통 신호 체계, 반도체 공장의 운반 시스템, 복합재 구조와 사출성형 공정의 설계·운영도 올라 있다.[^pubs]

## 구성원

2026년 10월 31일 Our Team의 현 구성원 구획에 게시된 박사과정 7명, 석사과정 6명, 학부 인턴 1명이다. Taeyoung Yun은 Ph.D Candidate로, 나머지 박사과정 학생은 Ph.D Student로 적혀 있다. 과정·연구 주제는 구성원 카드, 시작 시기는 같은 사람의 합류 소식에 근거한다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름을 확인한 경우에 표시했다.[^team]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Taeyoung Yun | 박사과정 |  | Generative Models, Reinforcement Learning, Black-box Optimization | 1, 2, 6, 8 |
| Zihan Ma | 박사과정 |  | Multi-Agent Reinforcement Learning |  |
| Jaewoo Lee | 박사과정 |  | Decision-making intelligence, Industrial AI | 2, 6 |
| Woojin Jeong | 박사과정 | Spring 2025 | Reinforcement Learning, Combinatorial Optimization |  |
| Sunmin Kweon | 박사과정 | Spring 2025 | Decision-focused learning, Sequential decision making |  |
| Seonghwan Kim | 박사과정 | Spring 2025 | Multi-Agent Reinforcement Learning |  |
| Jinwoo Park | 박사과정 | Summer 2025 | Reinforcement Learning, Language Model, Causal Representation Learning |  |
| Inhyuk Song | 석사과정 | Spring 2025 | Reinforcement Learning, Generative Models |  |
| Woocheol Shin | 석사과정 | Spring 2025 | Reinforcement Learning, Generative Models |  |
| Kyuil Sim | 석사과정 |  | Neural Combinatorial Optimization | 1 |
| Hyeongyu Kang | 석사과정 (Lab Representative) | Spring 2025 | Reinforcement Learning, AI-Agent | 1 |
| Dohyun Kim | 석사과정 | Summer 2025 | Vision Language Action model, Generative model |  |
| Jeongmin Park | 석사과정 | Spring 2026 | Reinforcement Learning, Generative Model, AI-Agent |  |
| Junhyeok Oh | 학부 인턴 | 2025 Summer, 2026 Fall |  |  |

## 졸업생과 이전 구성원

Our Team의 Alumni 구획에 게시된 박사 11명, 석사 25명, 이전 학부 인턴 11명이다. 학위 연도는 2019–2026년, 이전 학부 인턴의 활동 시기는 2024–2026년이다. 진로는 연구실 게시 표기다. Kanghoon Lee의 진로에는 SILAB·KAIST 박사후연구원이 적혀 있으며 Alumni 구획에 함께 올라 있다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Chihyeon Song | Ph.D (2026) | MongooseAI |
| Kanghoon Lee | Ph.D (2026) | Postdoctoral Fellow @ SILAB, KAIST |
| Federico Berto | Ph.D (2025) | AI Scientist @ Radical Numerics |
| Chuanbo Hua | Ph.D (2025) | Research Scientist @ Shanda Tokyo Research Center |
| Minsu Kim | Ph.D (2025) | Senior Researcher @ Microsoft |
| Hyeonah Kim | Ph.D (2025) | Assistant Professor @ UNIST |
| Jaeyeon Jo | Ph.D (2025) | Samsung SDS |
| Kyuree Ahn | Ph.D (2023) | Omelet |
| Minjun Kim | Ph.D (2023) | Samsung Advanced Institute of Technology (SAIT) |
| Yohan Jung | Ph.D (2023) | Assistant Professor @ Jeonbuk National University |
| Junyoung Park | Ph.D (2023) | Senior Researcher @ Qualcomm |
| Junho Park | M.S (2026) | Omelet |
| Zhikai Zhao | M.S (2026) | Huawei Research |
| Kiyoung Om | M.S (2026) | Ph.D Student at UT Austin, Amy Zhang |
| Sanghyeok Choi | M.S (2025) | Ph.D Student at Edinburgh, Nikolay Malkin |
| Yujin Shin | M.S (2025) | LG CNS |
| Hyunjun Kim | M.S (2025) | Korea Military Academy |
| Sujin Yun | M.S (2025) | Ph.D student at Mila, Aaron Courville |
| Nayoung Kim | M.S (2024) | Ph.D student at KAIST, SPML Lab |
| Huijie Tang | M.S (2024) | Omelet |
| Jiwoo Son | M.S (2024) | Omelet |
| Heemang Park | M.S (2024) | Clobot |
| Jihwan Yu | M.S (2023) | Omelet |
| Haewon Jung | M.S (2023) | Ph.D student at KAIST, IM^2 Lab |
| Fangying Chen | M.S (2021) | Samsung SDI |
| Kanghoon Yoon | M.S (2021) | Huawei Research Singapore |
| Jaehyuk Yi | M.S (2021) | Twelve Labs |
| Sanjar Bakhtiyarov | M.S (2020) | Founder at startup, Sol.ai |
| Hyunsoo Sim | M.S (2020) | SK.inc |
| Michael Poli | M.S (2020) | Ph.D Student at Stanford, Ermon group |
| Seunghoon Lee | M.S (2020) | WorldQuant |
| Jaehyeong Chun | M.S (2020) | MedInTech |
| Juneyoung Yeon | M.S (2020) | Tmax |
| Woojin Cho | M.S (2019) | ITDA Semiconductor |
| Seongcheol Woo | M.S (2019) | Korea Institute of Industrial Technology (KITECH) |
| Joonho Bae | M.S (2019) | Assistant Professor, School of Business at Indiana University |
| Junseong Park | Undergraduate Intern (2026 Summer) |  |
| Minseok Kim | Undergraduate Intern (2025 Winter) |  |
| Sujeong Baek | Undergraduate Intern (2025 Winter) |  |
| Hyoyeon Yang | Undergraduate Intern (2025 Winter) |  |
| Yomori Achiza | Undergraduate Intern (2025 Winter) |  |
| Chaeeun Lee | Undergraduate Intern (2025 Summer) |  |
| Eunhyo Kim | Undergraduate Intern (2024 Winter) |  |
| Seongjun Yun | Undergraduate Intern (2024 Winter) |  |
| Jungmin Lee | Undergraduate Intern (2024 Summer) |  |
| Junhan Jo | Undergraduate Intern (2024 Summer) |  |
| Kyuil Sim | Undergraduate Intern (2024 Summer) |  |

## 최근 논문 목록 (2021–2026)

차량 경로·일정 계획, 생성 모형과 강화학습, 생물 서열·분자 설계, 공정·구조 설계와 확률 모형을 다룬다. 연구실 게시 목록 가운데 2021–2026년 학회 59건, 워크숍 10건, 학술지 8건, 공학 학회 2건의 게시항목이다. 같은 연구의 본학회·워크숍 항목은 각각 표시한다. 연도만 있는 2021년 학회 항목은 해당 연도 표기를 따랐다. 제목·저자·발표처는 연구실 표기다. arXiv로 연결된 항목의 링크는 사전 공개본을 가리키며, NeurIPS 2026 세 항목은 연구실 소식에서 확인한 「채택」으로 표시했다.[^pubs][^home]

**2026**

- Jaewoo Lee\*, Hyeongyu Kang\*, Dohyun Kim, Kyuil Sim, Woocheol Shin, Minsu Kim, Taeyoung Yun, Jeongjae Lee, Sanghyeok Choi, Tabitha Edith Lee, Jong Chul Ye†, Jinkyoo Park†. "Aligning Few-Step Generative Model via Amortizing Sample-Based Variational Inference". *Neural Information Processing Systems (NeurIPS) 2026 (채택)*.
- Taeyoung Yun\*, Woocheol Shin\*, Inhyuck Song, Jaewoo Lee, Jinkyoo Park. "Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization". *Neural Information Processing Systems (NeurIPS) 2026 (채택)*.
- Kiyoung Om\*, Kyuil Sim\*, Taeyoung Yun\*, Hyeongyu Kang, Jinkyoo Park. "Posterior Inference in Latent Space for Scalable Constrained Black-box Optimization". *Neural Information Processing Systems (NeurIPS) 2026 (채택)*.
- Sanghyeok Choi, Sarthak Mittal, Victor Elvira, Jinkyoo Park, Nikolay Malkin. "Reinforced sequential Monte Carlo for amortised sampling". *International Conference on Machine Learning (ICML) 2026 – Spotlight*.
- Taeyoung Yun, Pierre-Luc St-Charles, Jinkyoo Park, Yoshua Bengio, Minsu Kim. "Active Attacks: Red-teaming LLMs via Adaptive Environments". *International Conference on Machine Learning (ICML) 2026*.
- Jaewoo Lee, Minsu Kim, Sanghyeok Choi, Inhuck Song, Sujin Yun, Hyeongyu Kang, Woocheol Shin, Taeyoung Yun, Kiyoung Om, Jinkyoo Park. "Diffusion Alignment as Variational Expectation-Maximization". *International Conference on Learning Representation (ICLR) 2026*.
- Hyeongyu Kang\*, Jaewoo Lee\*, Woocheol Shin\*, Kiyoung Om, Jinkyoo Park. "Diffusion Fine-Tuning via Reparameterized Policy Gradient of the Soft Q-Function". *International Conference on Learning Representation (ICLR) 2026*.
- Jiwoo Son\*, Zhikai Zhao\*, Federico Berto\*, Chuanbo Hua, Zhiguang Cao, Changhyun Kwon, Jinkyoo Park. "Towards Real-World Routing with Neural Combinatorial Optimization". *International Conference on Learning Representation (ICLR) 2026*.
- Chihyeon Song, Jaewoo Lee, Jinkyoo Park. "Adaptive Replay Buffer for Offline-to-Online Reinforcement Learning". *Artificial Intelligence and Statistics (AISTATS) 2026*.
- Zhikai Zhao, Chuanbo Hua, Federico Berto, Kanghoon Lee, Zihan Ma, Jiachen Li, Jinkyoo Park. "TrajEvo: Designing Trajectory Prediction Heuristics via LLM-driven Evolution". *AAAI Conference on Artificial Intelligence (AAAI) 2026*.
- Chuanbo Hua, Federico Berto, Zhikai Zhao, Jiwoo Son, Changhyun Kwon, Jinkyoo Park. "USPR: Learning a Unified Solver for Profiled Routing". *AAAI Conference on Artificial Intelligence (AAAI) 2026*.
- Taeyoung Yun, Inhyuck Song, Woocheol Shin, Yujin Shin, Sungpil Woo, Sunhwan Lim, Jinkyoo Park. "Traffic Network Layout Optimization with Guided Discrete Diffusion Models". *International Conference on Web Search and Data Mining (WSDM) 2026*.

**2025**

- Federico Berto\*, Chuanbo Hua\*, Laurin Luttmann\*, Jiwoo Son, Junyoung Park, Kyuree Ahn, Changhyun Kwon, Lin Xie, Jinkyoo Park. "PARCO: Parallel AutoRegressive Models for Multi-Agent Combinatorial Optimization". *Neural Information Processing Systems (NeurIPS) 2025*.
- Hyeonjun Kim\*, Kanghoon Lee\*, Junho Park, Jiachen Li, Jinkyoo Park. "Human Implicit Preference-Based Policy Fine-Tuning for Multi-Agent Reinforcement Learning in USV Swarm". *International Conference on Intelligent Robots and Systems (IROS) 2025*.
- Federico Berto\*, Chuanbo Hua\*, Junyoung Park\*, Laurin Luttmann\*, Yining Ma, Fanchen Bu, Jiarui Wang, Haoran Ye, Minsu Kim, Sanghyeok Choi, Nayeli Gast Zepeda, André Hottung, Jianan Zhou, Jieyi Bi, Yu Hu, Fei Liu, Hyeonah Kim, Jiwoo Son, Haeyeon Kim, Davide Angioni, Wouter Kool, Zhiguang Cao, Qingfu Zhang, Joungho Kim, Jie Zhang, Kijung Shin, Cathy Wu, Sungsoo Ahn, Guojie Song, Changhyun Kwon, Kevin Tierney, Lin Xie, Jinkyoo Park. "RL4CO: an Extensive Reinforcement Learning for Combinatorial Optimization Benchmark". *ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD) 2025*.
- Yujin Shin\*, Taeyoung Yun\*, Sujin Yun, Sungpil Woo, Sunhwan Lim, Jinkyoo Park. "Wind Farm Layout Optimization with Diffusion Models". *ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD) 2025*.
- Hyeonah Kim, Minsu Kim, Taeyoung Yun, Sanghyeok Choi, Emmanuel Bengio, Alex Hernández-García, Jinkyoo Park. "Improved Off-policy Reinforcement Learning in Biological Sequence Design". *International Conference on Machine Learning (ICML) 2025*.
- Hyeonah Kim\*, Sanghyeok Choi\*, Jiwoo Son, Jinkyoo Park, Changhyun Kwon. "Neural Genetic Search in Discrete Spaces". *International Conference on Machine Learning (ICML) 2025*.
- Taeyoung Yun\*, Kiyoung Om\*, Jaewoo Lee, Sujin Yun, Jinkyoo Park. "Posterior Inference with Diffusion Models for High-dimensional Black-box Optimization". *International Conference on Machine Learning (ICML) 2025*.
- Taeyoung Yun, Dinghuai Zhang, Jinkyoo Park, Ling Pan. "Learning to Sample Effective and Diverse Prompts for Text-to-Image Generation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2025*.
- Minsu Kim\*, Sanghyeok Choi\*, Taeyoung Yun, Emmanuel Bengio, Leo Feng, Jarrid Rector-Brooks, Sungsoo Ahn, Jinkyoo Park, Nikolay Malkin, Yoshua Bengio. "Adaptive Teachers for Amortized Samplers". *International Conference on Learning Representation (ICLR) 2025*.
- Nayoung Kim, Seongsu Kim, Minsu Kim, Jinkyoo Park, Sungsoo Ahn. "MOFFlow: Flow Matching for Structure Prediction of Metal-Organic Frameworks". *International Conference on Learning Representation (ICLR) 2025*.
- Seonghwan Seo, Minsu Kim, Tony Shen, Martin Ester, Jinkyoo Park, Sungsoo Ahn, Woo Youn Kim. "Generative Flows on Synthetic Pathways for Drug Design". *International Conference on Learning Representation (ICLR) 2025*.
- Minsu Kim\*, Sanghyeok Choi\*, Hyeonah Kim, Jiwoo Son, Jinkyoo Park, Yoshua Bengio. "Ant Colony Sampling with GFlowNets for Combinatorial Optimization". *Artificial Intelligence and Statistics (AISTATS) 2025*.
- Chuanbo Hua\*, Federico Berto\*, Jiwoo Son, Seunghyun Kang, Changhyun Kwon, Jinkyoo Park. "CAMP: Collaborative Attention Model with Profiles for Vehicle Routing Problems". *International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2025*.
- Shiqi Lei\*, Kanghoon Lee\*, Linjing Li, Jinkyoo Park. "Learning Strategy Representation for Imitation Learning in Multi-Agent Games". *AAAI Conference on Artificial Intelligence (AAAI) 2025*.
- Om, K.\*, Sim, K.\*, Yun, T.\*, Kang, H., & Park, J. (2025). Posterior Inference in Latent Space for Scalable Constrained Black-box Optimization. In NeurIPS SPIGM Workshop (Oral)

**2024**

- Hyeonah Kim, Minsu Kim, Sanghyeok Choi, Jinkyoo Park. "Genetic-guided GFlowNets for Sample Efficient Molecular Optimization". *Neural Information Processing Systems (NeurIPS) 2024*.
- Jaewoo Lee\*, Sujin Yun\*, Taeyoung Yun, Jinkyoo Park. "GTA: Generative Trajectory Augmentation with Guidance for Offline Reinforcement Learning". *Neural Information Processing Systems (NeurIPS) 2024*.
- Taeyoung Yun, Sujin Yun, Jaewoo Lee, Jinkyoo Park. "Guided Trajectory Generation with Diffusion Models for Offline Model-based Optimization". *Neural Information Processing Systems (NeurIPS) 2024*.
- Hyosoon Jang, Yunhui Jang, Minsu Kim, Jinkyoo Park, Sungsoo Ahn. "Pessimistic Backward Policy for GFlowNets". *Neural Information Processing Systems (NeurIPS) 2024*.
- Haoran Ye, Jiarui Wang, Zhiguang Cao, Federico Berto, Chuanbo Hua, Haeyeon Kim, Jinkyoo Park, Guojie Song. "Large Language Models as Hyper-Heuristics for Combinatorial Optimization". *Neural Information Processing Systems (NeurIPS) 2024*.
- Heemang Park\*, Kyuree Ahn\*, Jinkyoo Park. "NLNS-MASPF for solving Multi-Agent Scheduling and Path-Finding". *International Conference on Intelligent Robots and Systems (IROS) 2024*.
- Huijie Tang\*, Federico Berto\*, Jinkyoo Park. "Ensembling Prioritized Hybrid Policies for Multi-agent Pathfinding". *International Conference on Intelligent Robots and Systems (IROS) 2024*.
- Taeyoung Yun\*, Kanghoon Lee\*, Sujin Yun, Ilmyung Kim, Won-Woo Jung, Min-Cheol Kwon, Kyujin Choi, Yoohyeon Lee, and Jinkyoo Park. "An Offline Meta Black-box Optimization Framework for Adaptive Design of Urban Traffic Light Management Systems". *ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD) 2024*.
- Hyeonah Kim, Minsu Kim, Sungsoo Ahn, and Jinkyoo Park. "Symmetric Replay Training: Enhancing Sample Efficiency in Deep Reinforcement Learning for Combinatorial Optimization". *International Conference on Machine Learning (ICML) 2024*.
- Minsu Kim\*, Joohwan Ko\*, Taeyoung Yun\*, Dinghuai Zhang, Ling Pan, Woo Chang Kim, Jinkyoo Park, Emmanuel Bengio, Yoshua Bengio. "Learning to Scale Logits for Temperature-Conditional GFlowNets". *International Conference on Machine Learning (ICML) 2024*.
- Minsu Kim, Taeyoung Yun, Emmanuel Bengio, Dinghuai Zhang, Yoshua Bengio, Sungsoo Ahn and Jinkyoo Park. "Local Search GFlowNets". *International Conference on Learning Representation (ICLR) 2024 – Spotlight*.
- Jiwoo Son\*, Minsu Kim\*, Sanghyeok Choi, Hyeonah Kim, and Jinkyoo Park. "Equity-Transformer: Solving NP-hard Min-max Routing Problems as Sequential Generation with Equity Context". *AAAI Conference on Artificial Intelligence (AAAI) 2024*.
- Berto, F\*., Hua, C\*., Zepeda, N.G.\*, Hottung, A., Wouda, N., Lan, L., Tierney, K. and Park, J. (2024). RouteFinder: Towards foundation models for vehicle routing problems, In ICML FM-Wild Workshop (Oral)
- Lee, J.\*, Yun, S.\*, Yun, T., Park, J. (2024) GTA: Generative Trajetory Augmentation with Guidance for Offline Reinforcement Learning, In ICLR GenAI4DM Workshop (Spotlight)

**2023**

- Minsu Kim, Federico Berto, Sungsoo Ahn, and Jinkyoo Park. "Bootstrapped Training of Score-Conditioned Generator for Offline Design of Biological Sequences". *Neural Information Processing Systems (NeurIPS) 2023*.
- Chuanbo Hua\*, Federico Berto\*, Michael Poli, Stefano Massaroli, and Jinkyoo Park. "Learning Efficient Surrogate Dynamic Models with Graph Spline Networks". *Neural Information Processing Systems (NeurIPS) 2023*.
- Kyuree Ahn\*, Heemang Park\*, and Jinkyoo Park. "Learning to Schedule in Multi-Agent Pathfinding". *International Conference on Intelligent Robots and Systems (IROS) 2023*.
- Kanghoon Yoon\*, Youngjun Im\*, Jingyu Choi, Taehwan Jeong, and Jinkyoo Park. "Learning Multivariate Hawkes Process via Graph Recurrent Neural Network". *ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD) 2023*.
- Jiwoo Son\*, Minsu Kim\*, Hyeonah Kim, and Jinkyoo Park. "Meta-SAGE: A Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Large Scale Combinatorial Optimization". *International Conference on Machine Learning (ICML) 2023 (based on the preliminary version of the NeurIPS Distsift Workshop)*.
- Haeyeon Kim\*, Minsu Kim\*, Federico Berto, Joungho Kim and Jinkyoo Park. "DevFormer: A Symmetric Transformer for Context-Aware Device Placement". *International Conference on Machine Learning (ICML) 2023 (based on the preliminary version of the NeurIPS Offline RL Workshop)*.
- Minjun Kim\*, Junyoung Park\*, and Jinkyoo Park. "Neuro CROSS-exchange: Learning to CROSS-exchange to solve realistic vehicle routing problems". *International Conference on Learning Representation (ICLR) 2023*.
- Yohan Jung and Jinkyoo Park. "Bayesian Convolutional Deep Sets with Task-Dependent Stationary Prior". *International Conference on Artificial Intelligence and Statistics (AISTATS) 2023*.
- Junyoung Park, Changhyun Kwon, and Jinkyoo Park. "SchelduleNet: Learning to solve multi-robot scheduling problems with reinforcement learning". *International Conference on Autonomous Agents and MultiAgent Systems (AAMAS) 2023*.
- Berto, F.\*, Hua, C.\*, Park, J.\*, Luttmann, L.\*, Ma, Y., Bu, F., Wang, J., Ye, H., Kim, M., Choi, S., Zepeda, N.G., Hottung, A., Zhou, J., Bi, J., Hu, Y., Liu, F., Kim, H., Son, J., Kim, H., Angioni, D., Kool, W., Cao, Z., Zhang, J., Shin, K., Wu, C., Ahn, S., Song, G., Kwon, C., Xie, L., Park, J. (2023). RL4CO: an Extensive Reinforcement Learning for Combinatorial Optimization Benchmark, In NeurIPS 2023 GLFrontiers Workshop (Oral)
- Kim, H., Kim, M., Ahn, S,. Park, J. (2023). Symmetric Exploration in Combinatorial Optimization is Free! In ICML 2023 SODS Workshop.
- Jung, J; Park, K; Cho, B; Park, J; Ryu, S; “Optimization of injection molding process using multi-objective bayesian optimization and constrained generative inverse design networks”, JOURNAL OF INTELLIGENT MANUFACTURING, vol.34, no.8, pp.3623~3636, 2023.12; DOI(http://dx.doi.org/10.1007/s10845-022-02018-8)
- Bae, J; Park, J; Choi, J; Soh, SB; “A recommending system for mobile games using the dynamic nonparametric model”, JOURNAL OF BUSINESS RESEARCH, vol.167, 2023.11; DOI(http://dx.doi.org/10.1016/j.jbusres.2023.114079)
- Park, K; Song, C; Park, J; Ryu, S; “Multi-objective Bayesian optimization for the design of nacre-inspired composites: optimizing and understanding biomimetics through AI”, MATERIALS HORIZONS, vol.10, no.10, pp.4329~4343, 2023.10; DOI(http://dx.doi.org/10.1039/d3mh00137g)
- Kanghoon Lee, Jiachen Li, David Isele, Jinkyoo Park, Kikuo Fujimura, Mykel J Kochenderfer, “Robust Driving Policy Learning with Guided Meta Reinforcement Learning”, IEEE ITSC 2023

**2022**

- Minsu Kim, Junyoung Park, and Jinkyoo Park. "Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization". *Neural Information Processing Systems (NeurIPS) 2022*.
- Hyunwook Kang, Taehwan Kwon, Jinkyoo Park, James R. Morrison. "Learning NP-Hard multi-vehicle/machine scheduling: GNN theory for random graph embedding and fast fitted Q-iteration with provable guarantee". *Neural Information Processing Systems (NeurIPS) 2022*.
- Micheal Poli\*, Massaroli Stefano\*, Federico Berto\*, Jinkyoo Park, Tri Dao, Christopher Re, and Stefano Ermon. "Transform Once: Efficient Operator Learning in Frequency Domain". *Neural Information Processing Systems (NeurIPS) 2022*.
- Yohan Jung, Kyungwoo Song, and Jinkyoo Park. "Efficient Approximate Inference for Stationary Kernel on Frequency Domain". *International Conference on Machine Learning (ICML) 2022*.
- Junyoung Park, Jinhyun Choo, and Jinkyoo Park. "Convergent graph solver". *International Conference on Learning Representations (ICLR) 2022*.
- Federico Berto, Massaroli Stefano, Micheal Poli, and Jinkyoo Park. "Neural Solvers for Fast and Accurate Numerical Optimal Control". *International Conference on Learning Representations (ICLR) 2022*.
- Heechang Ryu, Hayong Shin, and Jinkyoo Park. "REMAX: Relational Representation for Multi-Agent Exploration". *International Conference on Autonomous Agents and MultiAgent Systems (AAMAS) 2022*.
- Kim, H., Kim, M., Kwon, C., Park, J. (2022). Neural Coarsening Process for Multi-level Graph Combinatorial Optimization, In NeurIPS GLFrontiers Workshop.
- Kim, H.\*, Kim, M.\*, Kim, J., Park, J. (2022). Collaborative symmetricity exploitation for offline learning of hardware design solver, In NeurIPS offline RL Workshop.
- Kim, M.\*, Son, J.\*, Kim, H., Park, J. (2022). Scale-conditioned Adaptation for Large Scale Combinatorial Optimization. In NeurIPS Workshop of DistShift.
- Hua, C.\*, Berto, F.\*, Poli, M., Massaroli, S., & Park, J. (2022). Efficient Continuous Spatio-Temporal Simulation with Graph Spline Networks. In ICML 2022 2nd AI for Science Workshop (Oral).
- Poli, M., Massaroli, S., Berto, F., Park, J., Dao, T., Re, C., & Ermon, S. (2022). Transform Once: Efficient Operator Learning in Frequency Domain. In ICML 2022 2nd AI for Science Workshop.
- Ahn, K; Lee, K; Yeon, J; Park, J; “Congestion-aware dynamic routing for an overhead hoist transporter system using a graph convolutional gated recurrent unit”, IISE TRANSACTIONS, vol.54, no.8, pp.803~816, 2022.08; DOI(http://dx.doi.org/10.1080/24725854.2021.2000680)
- Jung, Y; Park, J; “Scalable Inference for Hybrid Bayesian Hidden Markov Model Using Gaussian Process Emission”, JOURNAL OF COMPUTATIONAL AND GRAPHICAL STATISTICS, vol.31, no.3, pp.666~683, 2022.07; DOI(http://dx.doi.org/10.1080/10618600.2021.2023021)
- Jung, JY; Kim, Y; Park, J; Ryu, S; “Transfer learning for enhancing the homogenization-theory-based prediction of elasto-plastic response of particle/short fiber-reinforced composites”, COMPOSITE STRUCTURES, vol.285, 2022.04; DOI(http://dx.doi.org/10.1016/j.compstruct.2022.115210)
- Park, K; Kim, Y; Kim, M; Song, C; Park, J; Ryu, S; “Designing staggered platelet composite structure with Gaussian process regression based Bayesian optimization”, COMPOSITES SCIENCE AND TECHNOLOGY, vol.220, 2022.03; DOI(http://dx.doi.org/10.1016/j.compscitech.2021.109254)
- Massaroli, S; Poli, M; Peluchetti, S; Park, J; Yamashita, A; Asama, H; “Learning Stochastic Optimal Policies via Gradient Descent”, IEEE CONTROL SYSTEMS LETTERS, vol.6, pp.1094~1099, 2022; DOI(http://dx.doi.org/10.1109/LCSYS.2021.3086672)

**2021**

- Michael Poli\*, Massaroli Stefano\*, Luca Scimeca, Sanghyuk Chun, Seong Joon Oh, Atsushi Yamashita, Hajime Asama, Jinkyoo Park, Animesh Garg. "Neural Hybrid Automata: Learning Dynamics With Multiple Modes and Stochastic Transitions". *Neural Information Processing Systems (NeurIPS) 2021*.
- Stefano Massaroli\*, Michael Poli\*, Sho Sonoda, Taji Suzuki, Jinkyoo Park, Atsushi Yamashita, and Hajime Asama. "Differentiable Multiple Shooting Layers". *Neural Information Processing Systems (NeurIPS) 2021*.
- Minsu Kim, Jinkyoo Park, and Joungho Kim. "Learning Collaborative Policies to Solve NP-hard Routing Problems". *Neural Information Processing Systems (NeurIPS) 2021*.
- Jaehyuk Yi, and Jinkyoo Park. "Semi-supervised Bearing Fault Diagnosis with Adversarially-Trained Phase-Consistent Network". *ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD) 2021*.
- Heechang Ryu, Hayong Shin, and Jinkyoo Park. "Cooperative Biases for Multi-Agent Reinforcement Learning". *International Conference on Autonomous Agents and MultiAgent Systems (AAMAS) 2021*.
- Massaroli, S, Poli, M, Peluchetti , M, Park, J, Yamashita, A, Asama, H, “Learning Stochastic Optimal Policies via Gradient Descent” (IEEE CDC 2021)

## 연도 표기 없는 학술지 논문

연구실이 Published Papers 구획에 게시한 연도 없는 항목 5건이다. 이 가운데 Accepted로 적힌 4건은 「게재 승인」으로 표시한다.[^pubs]

- Kanghoon Lee, Hyeonjun Kim, Jiachen Li, Jinkyoo Park, “Priority-Aware Multi-Robot Coverage Path Planning”, IEEE Robotics and Automation Letters (RA-L) (게재 승인)
- Jaeyeon Jo, Jihwan Yu, Jinkyoo Park, “Incentive Design of Shared ESS Energy Trading Game,” IEEE Transactions on Control Systems Technology (게재 승인)
- Alexandros Tzikas, Jinkyoo Park, Mykel Kochenderfer, Ross Allen, “Distributed Online Planning for Min-Max Problems in Networked Markov Games”, IEEE Robotics and Automation Letters (RA-L) (게재 승인)
- Li, J; Isele, D; Lee, K; Park, J; Fujimura, K; Kochenderfer, M; “Interactive Autonomous Navigation with Internal State Inference and Interactivity Estimation”, IEEE Transactions on Robotics (게재 승인)
- Kim, H; Park, J; Kwon, C; “A Neural Separation Algorithm for the Rounded Capacity Inequalities”, INFORMS Journal on Computing; DOI(https://doi.org/10.1287/ijoc.2022.0310)

## 소식

첫 화면의 2024년 2월–2026년 9월 논문 채택 소식 20건이다.[^home]

- 2026.09 · NeurIPS 2026 논문 3편 채택
- 2026.05 · ICML 2026 논문 2편 채택
- 2026.01 · ICLR 2026 논문 3편 채택
- 2026.01 · AISTATS 2026 논문 1편 채택
- 2025.11 · AAAI 2026 논문 2편 채택
- 2025.10 · WSDM 2026 논문 1편 채택
- 2025.09 · NeurIPS 2025 논문 1편 채택
- 2025.06 · IROS 2025 논문 1편 채택
- 2025.05 · KDD 2025 논문 2편 채택
- 2025.05 · ICML 2025 논문 3편 채택
- 2025.02 · CVPR 2025 논문 1편 채택
- 2025.01 · ICLR 2025 논문 3편 채택
- 2025.01 · AISTATS 2025 논문 1편 채택
- 2024.12 · AAMAS 2025 논문 1편 채택
- 2024.12 · AAAI 2025 논문 1편 채택
- 2024.09 · NeurIPS 2024 논문 5편 채택
- 2024.06 · IROS 2024 논문 2편 채택
- 2024.05 · KDD 2024 논문 1편 채택
- 2024.05 · ICML 2024 논문 2편 채택
- 2024.02 · ICLR 2024 논문 1편 채택

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291, KAIST E2-1 4218호[^home][^team]
- 연구실 전화: (+82) 042-350-3173[^home][^team]
- 교수 이메일: jinkyoo.park@kaist.ac.kr[^home][^gsds]
- 데이터사이언스대학원 구성원 페이지의 교수 전화: 042-350-3133[^gsds]
[^home]: System Intelligence Lab, 첫 화면의 연구실 소개·모집 안내·News·Contact. <http://silab.kaist.ac.kr/> 관측일 2026-10-30.
[^team]: System Intelligence Lab, Our Team의 Principal Investigator·현 구성원·Alumni·Events·Contact. <http://silab.kaist.ac.kr/our-team-2/> 관측일 2026-10-31.
[^pubs]: System Intelligence Lab, Publications의 ML Conference Papers·Workshop Papers·International Journal Articles·Engineering Conference Papers. <http://silab.kaist.ac.kr/publications-2/> 관측일 2026-10-31.
[^gsds]: KAIST 데이터사이언스대학원, 구성원 페이지의 박진규 이름·연구 분야·이메일·전화와 홈페이지 링크. <https://gsds.kaist.ac.kr/people> 관측일 2026-10-30.
[^p1]: K. Om 외, J. Park, arXiv:2507.00480 (온라인 2025-07-01). <https://arxiv.org/abs/2507.00480> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2507.00480> 관측일 2026-10-31.
[^p2]: T. Yun 외, J. Park, arXiv:2502.16824 (온라인 2025-02-24). <https://arxiv.org/abs/2502.16824> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.16824> 관측일 2026-10-31.
[^p3]: F. Berto 외, J. Park, arXiv:2409.03811 (온라인 2024-09-05). <https://arxiv.org/abs/2409.03811> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.03811> 관측일 2026-10-31.
[^p4]: H. Kim 외, C. Kwon, arXiv:2502.10433 (온라인 2025-02-09). <https://arxiv.org/abs/2502.10433> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.10433> 관측일 2026-10-31.
[^p5]: S. Lei, K. Lee, L. Li, J. Park, arXiv:2409.19363 (온라인 2024-09-28). <https://arxiv.org/abs/2409.19363> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.19363> 관측일 2026-10-31.
[^p6]: J. Lee, S. Yun, T. Yun, J. Park, arXiv:2405.16907 (온라인 2024-05-27). <https://arxiv.org/abs/2405.16907> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2405.16907> 관측일 2026-10-31.
[^p7]: M. Kim, J. Park, J. Park, arXiv:2205.13209 (온라인 2022-05-26). <https://arxiv.org/abs/2205.13209> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2205.13209> 관측일 2026-10-31.
[^p8]: H. Kim 외, J. Park, arXiv:2410.04461 (온라인 2024-10-06). <https://arxiv.org/abs/2410.04461> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.04461> 관측일 2026-10-31.

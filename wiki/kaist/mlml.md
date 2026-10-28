# 머신러닝 & 마인드 랩 (Machine Learning and Mind Lab, MLML)

**KAIST 전산학부 · 안성진 부교수**

- 분야: 범용 지능 에이전트를 위한 표현학습, 월드 모델, 강화학습, 생성 모델, 로봇학습[^research][^faculty]
- 대분야: 컴퓨팅·AI
- 태그: 월드 모델[^research][^p2], 강화학습[^research][^p3], 생성 인공지능[^p2][^p6], 대형 언어 모델[^research][^p5]
- 홈페이지: <https://mlml.kaist.ac.kr/>
- 근거와 출처: [별도 문서](mlml-sources.md)

> 장면을 물체와 개념으로 나누어 이해하고, 앞으로 일어날 일을 예상하며, 기억과 추론으로 행동을 계획하는 범용 인공지능의 학습 방법을 만드는 연구실이다.[^research][^home]

## 무엇을 연구하나

머신러닝 & 마인드 랩은 에이전트(환경을 관찰하고 행동하며 목표를 수행하는 주체)가 여러 종류의 문제를 풀 수 있도록 하는 기계학습(자료와 경험에서 규칙을 익히는 계산 방법)을 연구한다. 목표는 지각·인지·행동의 기반이 되는 학습 알고리즘(자료에서 규칙을 익히는 계산 절차)을 만들어 사람과 같은 범용 인공지능(여러 영역의 과제를 수행할 수 있는 인공지능)에 다가가는 것이다. 이 계산적 접근을 통해 사람의 마음이 작동하는 방식에도 통찰을 얻고자 한다.[^research]

핵심은 무엇을 보고, 어떻게 기억하고, 무엇이 일어날지 예상할 것인가다. 연구실은 표현학습(자료에서 과제 수행에 필요한 특징과 구조를 배우는 방법), 월드 모델(행동이나 조건에 따른 환경의 변화와 상태를 예측하도록 학습한 모형), 강화학습(행동의 결과로 얻는 보상을 바탕으로 행동 방식을 배우는 방법)을 연결한다. 물체의 색·모양·움직임을 구별해 배우고, 이미 익힌 개념을 조합해 새로운 장면을 다루는 능력에 관심이 있다.[^research][^lab][^p1][^p2]

이러한 학습에는 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)과 확률적 생성 모델(자료가 생겨나는 확률적 관계를 학습해 새로운 자료를 만들어 내는 모형)을 사용한다. 신경망은 연결된 계산 단위의 결합 방식과 값을 학습하는 모형이다. 연구 대상에는 인지과학·뇌과학에서 착안한 학습과 기억, 언어 모델을 결합한 에이전트, 로봇과 게임 속에서 행동하는 인공지능이 함께 들어 있다.[^research]

## 주요 연구 주제

### 물체와 속성을 나누어 배우는 표현과 월드 모델

Neural Systematic Binder는 장면을 물체별 표현과 물체 내부의 속성별 표현으로 나누어 배우는 방법이다. 정답 이름표 없이 자료의 구조를 익히는 비지도학습으로 이러한 구분을 얻고, 학습할 때 보지 못한 속성 조합을 영상으로 만드는 실험을 제시했다. Dreamweaver는 시간에 따라 움직이는 영상에서 물체와 속성을 분리하고 미래 장면을 만든다. 글이나 물체 경계 표시 같은 보조 자료 없이, 익힌 속성을 다시 조합한 영상을 생성하는 것이 연구의 한 갈래다.[^p1][^p2]

### 긴 행동 계획과 추론에 쓰는 계산량

확산 모델(자료에 잡음을 더하고 제거하는 과정을 학습해 자료를 생성하는 모형)을 행동 계획에 쓰는 연구다. PlanDQ는 이미 모은 상호작용 자료로 학습하는 오프라인 강화학습에서, 상위 계획기가 중간 목표를 정하고 하위 정책(상태나 관찰에 따라 행동을 선택하는 규칙)이 이를 수행하도록 나눈다. Monte Carlo Tree Diffusion은 잡음을 줄여 가는 계획 과정을 가지를 뻗는 탐색 구조로 구성한다. 후보 계획을 평가·제거·수정하면서 계산을 더 투입할 때 해의 품질을 높이는 방향이다.[^p3][^p4]

### 기억을 갖춘 언어 기반 에이전트와 글 생성

대형 언어 모델(많은 글을 학습해 언어를 이해하고 생성하는 모형)을 결합한 에이전트가 장기간 과제를 수행하도록 연구한다. MrSteve는 Minecraft에서 과거 사건의 무엇·어디·언제 정보를 저장하고 찾아 쓰는 기억을 하위 행동 제어기에 넣는다. Loopholing은 글을 병렬로 생성하는 이산 확산 모델에서, 후보 단어들의 확률 정보가 단계 사이에 사라지는 문제를 다룬다. 확률 정보가 흐르는 별도 내부 경로를 두어 글 생성과 산술 문제 풀이를 개선했다.[^research][^p5][^p6]

### 관찰을 설명하는 프로그램과 여러 경로의 추론

Learning to Theorize는 다음 장면을 맞히는 데서 나아가, 관찰을 설명하는 실행 가능한 프로그램을 배우려는 연구다. 배운 기본 요소를 재조합해 새로운 현상을 설명한다. Generative Recursive Reasoning은 재귀 추론(공유하는 계산 규칙을 반복 적용하며 내부 표현을 고쳐 가는 추론)을 확률적인 여러 풀이 경로로 확장한다. 계산의 반복 깊이와 병렬 경로 수를 통해 추론에 쓰는 계산량을 늘리고, 서로 다른 가설이나 해법을 다룬다.[^p7][^p8]

## 대표 논문

물체·개념 표현과 월드 모델, 행동 계획, 언어 기반 에이전트, 생성·추론을 고르게 보여 주는 여덟 편이다. 연도와 학회 이름은 연구실 논문 목록 기준이며, 연결한 판본은 arXiv 사전 공개본이다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.[^pubs][^home]

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2023 | [Neural Systematic Binder](https://arxiv.org/abs/2211.01177) · ICLR 23, arXiv 판 | 장면 속 물체 하나를 나타내는 표현을 여러 독립적인 속성 표현으로 구성한다. 장면 전체에서 물체를 구분하는 과정과 물체 안에서 속성을 구분하는 과정을 번갈아 적용해, 정답 이름표 없이 구조를 배운다. 실험에서는 기존 물체 중심 방법보다 물체 안의 속성을 잘 분리했으며, 학습 때 보지 못한 속성 조합을 풀어내어 장면을 생성했다.[^p1] | 마지막 저자 Sungjin Ahn |
| 2 | 2025 | [Dreamweaver: Learning Compositional World Models from Pixels](https://arxiv.org/abs/2501.14174) · ICLR 25, arXiv 판 | 영상을 물체와 색·모양·움직임 같은 속성으로 나누고, 이를 조합해 미래 영상을 생성하는 모형이다. 글이나 물체 경계를 알려 주는 보조 자료를 쓰지 않는다. 영상에서 계층적인 개념을 발견하는 Recurrent Block-Slot Unit과 여러 미래 프레임을 예측하는 학습 목표를 사용한다. 여러 자료 집합의 표현 평가에서 기존 비교 방법을 앞섰고, 익힌 물체의 속성을 재조합한 새 영상을 생성했다.[^p2] | 마지막 저자 Sungjin Ahn |
| 3 | 2024 | [PlanDQ: Hierarchical Plan Orchestration via D-Conductor and Q-Performer](https://arxiv.org/abs/2406.06793) · ICML 24, arXiv 판 | 기존 자료로 학습하는 강화학습에서 짧은 과제와 긴 과제를 함께 다루려는 계층형 계획 방법이다. 상위 D-Conductor는 확산 모델로 중간 목표를 정한다. 하위 Q-Performer는 행동의 가치를 학습하는 Q-learning을 이용해 각 목표를 수행한다. 연속 제어와 긴 수행 단계가 필요한 과제 실험에서 기존 방법보다 좋거나 경쟁력 있는 성능을 낼 수 있음을 보였다.[^p3] | 마지막 저자 Sungjin Ahn |
| 4 | 2025 | [Monte Carlo Tree Diffusion for System 2 Planning](https://arxiv.org/abs/2502.07202) · ICML 25 Spotlight, arXiv 판 | 확산 모델의 생성 능력과 몬테카를로 나무 탐색(Monte Carlo Tree Search, 여러 후보 가지를 평가하며 탐색하는 방법)을 결합한다. 아직 잡음이 남은 계획을 반복 평가하고, 후보를 제거하거나 고치며, 유망한 경로를 선택적으로 늘린다. 긴 과제 실험에서 추론에 쓰는 계산량을 늘릴 때 기존 확산 기반 방법보다 품질이 높은 해를 얻었다.[^p4] | 마지막 저자 Sungjin Ahn |
| 5 | 2025 | [MrSteve: Instruction-Following Agents in Minecraft with What-Where-When Memory](https://arxiv.org/abs/2411.06736) · ICLR 25, arXiv 판 | 대형 언어 모델 기반 상위 계획기 아래에서 행동하는 제어기에 과거 사건을 기억하는 기능을 넣는다. Place Event Memory는 무엇이 어디에서 언제 일어났는지를 저장해 긴 과제에서 과거 사건을 찾아 쓰고 이동하게 한다. 기억에 따라 탐색과 과제 수행을 번갈아 하는 방식도 제안했으며, 기존 방법보다 과제 수행과 탐색 효율을 높였다.[^p5] | 마지막 저자 Sungjin Ahn |
| 6 | 2026 | [Loopholing Discrete Diffusion: Deterministic Bypass of the Sampling Wall](https://arxiv.org/abs/2510.19304) · ICLR 26 (채택), arXiv 판 | 여러 글자·단어 후보를 병렬로 다루는 이산 확산 모델은 한 후보를 뽑는 순간 나머지 후보의 확률 정보를 잃는다. Loopholing은 그 정보가 단계 사이에 흐르도록 별도 내부 경로를 만든다. 현재 예측을 다음 예측의 조건으로 쓰는 자기조건화로 학습하며, 기존 비교 방법보다 자연스러운 글 생성과 산술 과제 성능을 개선했다.[^p6] | 마지막 저자 Sungjin Ahn |
| 7 | 2026 | [Learning to Theorize the World from Observation](https://arxiv.org/abs/2605.03413) · ICML 26 Oral Presentation (채택), arXiv 판 | 글이 아닌 관찰 자료에서 세상이 작동하는 방식을 설명하는 이론을 배우게 한다. Neural Theorizer는 관찰을 실행 가능한 프로그램으로 나타내고 공통의 상태 변화 모형으로 실행한다. 학습한 기본 요소를 재조합해 새로운 현상을 설명하며, 관찰을 만들어 내는 프로그램을 바탕으로 일반화하는 방식을 실험으로 보여 주었다.[^p7] | 마지막 저자 Sungjin Ahn |
| 8 | 2026 | [Generative Recursive Reasoning](https://arxiv.org/abs/2605.19376v3) · NeurIPS 26 (채택), arXiv 판 | 같은 계산 규칙으로 내부 표현을 반복 수정하는 재귀 추론을 확률적인 여러 경로로 확장한다. Generative Recursive reAsoning Models는 복수의 가설과 풀이 전략을 다루며, 반복 깊이와 병렬 경로 수로 추론 계산량을 늘린다. 구조가 있는 추론 및 여러 해가 가능한 제약 만족 과제에서 기존 결정적 방식보다 성능을 높였고, 입력 조건 없이 자료를 생성하는 능력도 보였다.[^p8] | 마지막 저자 Sungjin Ahn |

## 교수와 전문 분야

안성진은 2021년부터 KAIST 전산학부 부교수로 재직하고 있다. 학과 소개가 적은 주 연구 분야는 기계학습·강화학습·로봇학습이며, 여러 과제를 수행하는 지능 에이전트의 범용성을 높이는 모델과 알고리즘 개발에 관심을 둔다. KAIST 부임 전에는 Rutgers 대학교 전산학과와 인지과학센터에서 조교수로 재직했고, 몬트리올대학교 Mila에서 박사후연구를 했다. 2015년 University of California, Irvine에서 전산학 박사학위를 받았다.[^faculty]

최근 논문에서 이어지는 전문 분야는 물체와 속성으로 나누는 표현학습, 영상을 이해하고 생성하는 월드 모델, 계층형 강화학습과 확산 기반 계획, 기억을 사용하는 에이전트, 프로그램과 반복 계산을 통한 추론이다.[^p1][^p2][^p3][^p4][^p5][^p7][^p8] 학과 소개는 이전 수상으로 ICML 2012와 ParLearning 2016 최우수 논문상을 적는다.[^faculty]

## 응용 분야

연구실은 로봇학습·게임 인공지능과 대형 언어 모델 기반 에이전트를 응용 대상으로 제시한다.[^research] 대표 논문의 구체적인 예는 익힌 물체 속성을 재조합한 영상 생성, 중간 목표를 나누는 연속 제어와 긴 행동 계획, Minecraft에서 기억을 활용하는 지시 수행, 병렬 글 생성과 산술 추론이다.[^p2][^p3][^p5][^p6]

연구실 연구와 연결된 별도 조직으로 KAIST-Mila Prefrontal AI Research Center가 있다. 센터 소개는 안성진을 센터장으로, 홍승훈·안성수와 Mila의 Yoshua Bengio를 연구진으로 적는다. 센터는 사람 전전두피질의 고차 인지 기능에서 착안한 학습 알고리즘, 안전을 보장하는 범용 인공지능, 과학을 위한 인공지능을 연구 주제로 제시한다. 센터 소개의 출범일 표기는 2024년 7월 1일이다.[^center]

## 구성원

2026년 10월 28일 연구실 People 페이지의 교수 외 현재 구성원 17명이다. Postdoc 1명, PhD 7명, MS 3명, Intern 6명이며 과정은 해당 표기다. ‘대표 논문 참여’는 위 표의 전체 저자 목록에서 같은 영문 이름을 확인한 번호다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kangil Lee | 박사후연구원 |  |
| Jaesik Yoon | 박사과정 | 4, 6 |
| Yohan Lee | 박사과정 |  |
| Junyeob Baek | 박사과정 | 2, 3, 7, 8 |
| Junyeong Park | 박사과정 | 5 |
| Dongwoo Lee | 박사과정 |  |
| Doojin Baek | 박사과정 | 4, 7 |
| Hyeonseo Cho | 박사과정 | 4 |
| Gyubin Lee | 석사과정 | 7 |
| Hosung Lee | 석사과정 | 7 |
| Mingyu Jo | 석사과정 | 6, 8 |
| Taegu Kang | 인턴 |  |
| Seungju Back | 인턴 |  |
| Seongho Cho | 인턴 |  |
| Hanjin Tak | 인턴 |  |
| Daehan Won | 인턴 |  |
| Minjun Jee | 인턴 |  |

## 졸업생과 이전 구성원

People 페이지의 Alumni 31명이다. Postdoc 1명, PhD 5명, MS 9명, Interns & Visiting 16명이며, 연도·과정·진로는 연구실 표기다. 24F·25S·25F·26F는 원문의 기간 표시이고, 기간이 없는 사람은 연도 칸을 비웠다. Advanced to PhD는 박사과정 진학 표기다. 현재 구성원과 석사 졸업생에 함께 있는 사람도 각 구획에 실린 대로 적었다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Minsu Kim | Postdoc | Microsoft |
| Chang Chen | PhD (25S) | Meta |
| Jindong Jiang | PhD (25S) | Nvidia |
| Yi-Fu Wu | PhD (25S) | Nvidia |
| Gautam Singh | PhD (24F) | Lawrence Livermore National Laboratory |
| Fei Deng | PhD (24F) | Google |
| Doojin Baek | MS (26F) | Advanced to PhD |
| Hyeonseo Cho | MS (26F) | Advanced to PhD |
| Truong Nhat Nguyen Bao | MS (25F) |  |
| Junyeob Baek | MS (25S) | Advanced to PhD |
| Junyeong Park | MS (25S) | Advanced to PhD |
| Subin Kim | MS (25S) |  |
| Hany Hamed | MS (24F) |  |
| Minseung Lee | MS (24F) |  |
| Yeongbin Kim | MS (24S) |  |
| Changhyeon Lim | Interns & Visiting |  |
| Minseok Kang | Interns & Visiting |  |
| Sejong Kim | Interns & Visiting |  |
| Luncanu Stefan Valentin | Interns & Visiting |  |
| Do-Hyeon Lee | Interns & Visiting |  |
| Taewook Kang | Interns & Visiting |  |
| Dongyeong Kim | Interns & Visiting |  |
| Ian Porada (Mila) | Interns & Visiting |  |
| Seonho Yoo | Interns & Visiting |  |
| Hwanhee Kim | Interns & Visiting |  |
| Myeongkyun Cho | Interns & Visiting |  |
| SeungAn Jung | Interns & Visiting |  |
| Prin Phunyaphibarn | Interns & Visiting |  |
| Ahmed Magd | Interns & Visiting |  |
| Sungwon Yang | Interns & Visiting |  |
| Hyea Kang | Interns & Visiting |  |

## 최근 논문 목록 (2021–2026)

물체와 개념의 표현, 미래 장면 예측, 행동 계획과 강화학습, 언어 기반 에이전트와 추론을 다룬 논문들이다. Publications의 2021–2026년 구역 41개 항목이며, 학회 논문·워크숍 논문·arXiv 원고를 포함한다. 연구실의 이전 소속 시기 항목이 섞일 수 있는 목록이며, 안성진 교수는 2021년 KAIST에 부임했다. 2021년 각 항목의 부임 전후 관계는 따로 구분하지 않는다. 연도·제목·저자·발표처는 연구실 표기를 따른다. 별표는 원문 표시이며 저자 역할로 풀지 않았다. arXiv 사전 공개본이 함께 연결된 항목은 판본을 구분해 표시했다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다.[^pubs][^faculty][^home]

**2026**

- Junyeob Baek\*, Mingyu Jo\*, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn. "Generative Recursive Reasoning". *NeurIPS 26 (arXiv 사전 공개본 연결) (채택)*.
- Doojin Baek\*, Junyeob Baek\*,  Mingyu Jo, Hosung Lee, Taegu Kang, Gyubin Lee, Sungjin Ahn. "BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone". *NeurIPS 26 (채택)*.
- Junyeong Park, Hyeonseo Cho, Sungjin Ahn. "CrafterDojo: A Suite of Foundation Models for Building Open-Ended Embodied Agents in Crafter". *NeurIPS 26 (arXiv 사전 공개본 연결) (채택)*.
- Doojin Baek\*, Gyubin Lee\*, Junyeob Baek, Hosung Lee, Sungjin Ahn. "Learning to Theorize the World from Observation". *ICML 26 Oral Presentation (arXiv 사전 공개본 연결) (채택)*.
- Seungju Back\*, Dongwoo Lee\*, Naun Kang, Taehee Lee, S. K. Hong, Youngjune Gwon, Sungjin Ahn. "Understanding LoRA as Knowledge Memory". *ICML 26 (arXiv 사전 공개본 연결) (채택)*.
- Mingyu Jo, Jaesik Yoon, Justin Deschenaux, Caglar Gulcehre, Sungjin Ahn. "Loopholing Discrete Diffusion: Deterministic Bypass of the Sampling Wall". *ICLR 26 (arXiv 사전 공개본 연결) (채택)*.
- Minsu Kim, Jean-Pierre Falet, Oliver E. Richardson, Xiaoyin Chen, Moksh Jain, Sungjin Ahn, Sungsoo Ahn, Yoshua Bengio. "Latent Veracity Inference for Identifying Errors in Stepwise Reasoning". *ICLR 26 (arXiv 사전 공개본 연결) (채택)*.
- Chang Chen\*, Hany Hamed\*, Doojin Baek, Taegu Kang, Samyeul Noh, Yoshua Bengio, Sungjin Ahn. "Extendable Planning via Multiscale Diffusion". *AAAI 26 Oral Presentation (arXiv 사전 공개본 연결) (채택)*.
- Taegu Kang, Jaesik Yoon, Sungjin Ahn. "Inference-Time Scaling in Diffusion Models through Iterative Partial Refinement". *ICLR 26 Workshop on AI with Recursive Self-Improvement (RSI) (arXiv 사전 공개본 연결)*.

**2025**

- Jaesik Yoon\*, Hyeonseo Cho\*, Yoshua Bengio, Sungjin Ahn. "Fast Monte Carlo Tree Diffusion: 100x Speedup via Parallel Sparse Planning". *NeurIPS 25 Spotlight (arXiv 사전 공개본 연결)*.
- Jaesik Yoon, Hyeonseo Cho, Sungjin Ahn. "Compositional Monte Carlo Tree Diffusion for Extendable Planning". *NeurIPS 25 Spotlight (arXiv 사전 공개본 연결)*.
- Gyubin Lee\*, Truong Nhat Nguyen Bao\*, Jaesik Yoon, Dongwoo Lee, Minsu Kim, Yoshua Bengio, Sungjin Ahn. "Adaptive Inference-Time Scaling via Cyclic Diffusion Search". *NeurIPS 25 (arXiv 사전 공개본 연결)*.
- Jaesik Yoon, Hyeonseo Cho, Doojin Baek, Yoshua Bengio, Sungjin Ahn. "Monte Carlo Tree Diffusion for System 2 Planning". *ICML 25 Spotlight (arXiv 사전 공개본 연결)*.
- Junyeob Baek, Yi-Fu Wu, Gautam Singh, Sungjin Ahn. "Dreamweaver: Learning Compositional World Models from Pixels". *ICLR 25 (arXiv 사전 공개본 연결)*.
- Junyeong Park\*, Junmo Cho\*, Sungjin Ahn. "MrSteve: Instruction-Following Agents in Minecraft with What-Where-When Memory". *ICLR 25 (arXiv 사전 공개본 연결)*.
- Junyeob Baek, Hosung Lee, Christopher Hoang, Mengye Ren, Sungjin Ahn. "Discrete JEPA: Learning Discrete Token Representations without Reconstruction". *ICML 25 Tokenization Workshop (TokShop) (arXiv 사전 공개본 연결)*.
- Jindong Jiang\*, Xiuyu Li\*, Zhijian Liu, Muyang Li, Guo Chen, Zhiqi Li, De-An Huang, Guilin Liu, Zhiding Yu, Kurt Keutzer, Sungjin Ahn, Jan Kautz, Hongxu Yin, Yao Lu, Song Han, Wonmin Byeon. "STORM: Token-Efficient Long Video Understanding for Multimodal LLMs". *arXiv 사전 공개본*.

**2024**

- Jindong Jiang, Fei Deng, Gautam Singh, Minseung Lee, Sungjin Ahn. "Slot State Space Models". *NeurIPS 24 (arXiv 사전 공개본 연결)*.
- Chang Chen, Junyeob Baek, Fei Deng, Kenji Kawaguchi, Caglar Gulcehre, Sungjin Ahn. "PlanDQ: Hierarchical Plan Orchestration via D-Conductor and Q-Performer". *ICML 24 (arXiv 사전 공개본 연결)*.
- Gautam Singh, Yue Wang, Jiawei Yang, Boris Ivanovic, Sungjin Ahn, Marco Pavone, Tong Che. "Parallelized Spatiotemporal Slot Binding for Videos". *ICML 24 (arXiv 사전 공개본 연결)*.
- Hany Hamed\*, Subin Kim\*, Dongyeong Kim, Jaesik Yoon, Sungjin Ahn. "Dr. Strategy: Model-Based Generalist Agents with Strategic Dreaming". *ICML 24 (arXiv 사전 공개본 연결)*.
- Yi-Fu Wu, Minseung Lee, Sungjin Ahn. "Neural Language of Thought Models". *ICLR 24 (arXiv 사전 공개본 연결)*.
- Junmo Cho\*, Jaesik Yoon\*, Sungjin Ahn. "Spatially-Aware Transformers for Embodied Agents". *ICLR 24 Spotlight (arXiv 사전 공개본 연결)*.
- Chang Chen, Fei Deng, Kenji Kawaguchi, Caglar Gulcehre, Sungjin Ahn. "Simple Hierarchical Planning with Diffusion". *ICLR 24 (arXiv 사전 공개본 연결)*.
- Whie Jung, Jaehoon Yoo, Sungjin Ahn, Seunghoon Hong. "Learning to Compose: Improving Object Centric Learning by Injecting Compositionality". *ICLR 24*.

**2023**

- Jindong Jiang, Fei Deng, Gautam Singh, Sungjin Ahn. "Object-Centric Slot Diffusion". *NeurIPS 23 Spotlight (arXiv 사전 공개본 연결)*.
- Fei Deng, Junyeong Park, Sungjin Ahn. "Facing Off World Model Backbones: RNNs, Transformers, and S4". *NeurIPS 23 (arXiv 사전 공개본 연결)*.
- Yeongbin Kim\*, Gautam Singh\*, Junyeong Park, Caglar Gulcehre, Sungjin Ahn. "Imagine the Unseen World: A Benchmark for Systematic Generalization in Visual World Models". *NeurIPS 23 (arXiv 사전 공개본 연결)*.
- Jaesik Yoon, Yi-Fu Wu, Heechul Bae, Sungjin Ahn. "An Investigation into Pre-Training Object-Centric Representations for Reinforcement Learning". *ICML 23 (arXiv 사전 공개본 연결)*.
- Gautam Singh, Yeongbin Kim, Sungjin Ahn. "Neural Systematic Binder". *ICLR 23 (arXiv 사전 공개본 연결)*.
- Yi-Fu Wu, Minseung Lee, Sungjin Ahn. "Object-Centric Semantic Vector Quantization". *NeurIPS 23 Workshop on Causal Representation Learning*.

**2022**

- Gautam Singh, Yi-Fu Wu, Sungjin Ahn. "Simple Unsupervised Object-Centric Learning for Complex and Naturalistic Videos". *NeurIPS 22 (arXiv 사전 공개본 연결)*.
- Fei Deng, Ingook Jang, Sungjin Ahn. "DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations". *ICML 22*.
- Gautam Singh, Fei Deng, Sungjin Ahn. "Illiterate DALLE Learns to Compose". *ICLR 22 (arXiv 사전 공개본 연결)*.

**2021**

- Gautam Signh, Skand Peri, Junghyun Kim, Hyunseok Kim, Sungjin Ahn. "Structured World Belief for Reinforcement Learning in POMDP". *ICML 21*.
- Yi-Fu Wu, Jaesik Yoon, Sungjin Ahn. "Generative Video Transformer: Can Objects be the Words?". *ICML 21*.
- Fei Deng, Zuo Zhi, Donghun Lee, Sungjin Ahn. "Generative Scene Graph Networks". *ICLR 21*.
- Chang Chen\*, Fei Deng\*, Sungjin Ahn. "ROOTS: Object-Centric Representation and Rendering of 3D Scenes". *JMLR 21*.
- Fei Deng, Ingook Jang, Sungjin Ahn. "DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations". *NeurIPS 21 Deep RL Workshop (arXiv 사전 공개본 연결)*.
- Chang Chen, Jaesik Yoon, Yi-Fu Wu, Sungjin Ahn. "TransDreamer: Reinforcement Learning with Transformer World Models". *NeurIPS 21 Deep RL Workshop*.
- Gautam Singh, Fei Deng, Sungjin Ahn. "Learning Representations for Zero-Shot Image Generation without Text". *NeurIPS 21 Workshop on Controllable Generative Modeling in Language and Vision*.

## 수상과 선정

2021-10-13–2026-10-13 범위에 게시된 수상 소식 1건이다. 아래 날짜는 수상일이 아닌 게시일이다.[^award][^pubs]

- 2026-07-29 · Learning to Theorize the World from Observation 논문의 ICML 2026 Workshop on Compositional Learning Best Paper Award(최우수논문상) 수상 소식.[^pubs][^award]

## 소식

연구실이 게시한 2023년 2월–2026년 9월의 연구·학술 행사 소식 15건이다. 날짜는 소식에 적힌 날짜이며, 연구 소개 글 세 건은 게시일이다. 연구실 소식에는 이전 소속 시기 글도 함께 있으나, 아래 목록은 KAIST 부임 뒤 날짜가 적힌 항목이다.[^home][^faculty][^crafter][^abcd][^fast]

- 2026-09-25 · NeurIPS 2026에 논문 세 편이 채택되었다.[^home]
- 2026-05-01 · ICML 2026에 논문 두 편이 채택되었고, 그중 한 편은 구두 발표 논문이다.[^home]
- 2026-01-27 · ICLR 2026에 논문 두 편이 채택되었다.[^home]
- 2025-11-08 · Extendable Planning via Multiscale Diffusion이 AAAI 2026 구두 발표 논문으로 채택되었다.[^home]
- 2025-09-19 · NeurIPS 2025에 논문 세 편이 채택되었고, 그중 두 편은 Spotlight 논문이다.[^home]
- 2025-08-25 · CrafterDojo의 기반 모델 묶음을 소개하는 글을 게시했다.[^crafter]
- 2025-06-28 · 확산 기반 추론 계산량 확장 연구인 Adaptive Cyclic Diffusion for Inference Scaling 소개 글을 게시했다.[^abcd]
- 2025-06-25 · Fast Monte Carlo Tree Diffusion의 병렬 희소 계획 연구 소개 글을 게시했다.[^fast]
- 2025-05-01 · Monte Carlo Tree Diffusion for System 2 Planning이 ICML 2025 Spotlight 논문으로 채택되었다.[^home]
- 2025-01-22 · ICLR 2025에 논문 두 편이 채택되었다.[^home]
- 2024-07-29 · KAIST-Mila Prefrontal AI Research Center 출범과 Yoshua Bengio 교수와의 System 2 Deep Learning 공동 연구를 알렸다.[^home]
- 2024-02-06 · Yoshua Bengio 교수가 연사인 두 번째 KAIST AGI Seminar Series를 개최했다.[^home]
- 2024-01-16 · ICLR 2024에 논문 네 편이 채택되었고, Spatially-Aware Transformer 논문은 Spotlight 논문으로 선정되었다.[^home]
- 2023-11-17 · Jim Fan이 연사인 첫 번째 KAIST Seminar Series on AGI를 개최했다.[^home]
- 2023-02 · 안성진 교수가 DeepMind에서 Toward Neural Systematic Binder를 주제로 초청 강연을 했다.[^home]

## 연락과 위치

- 주소: E3-1 3435, 291 Daehak-ro, Yuseong-gu, Daejeon, South Korea[^home]
- 전화: 042-350-3588[^home]
- 교수연구실: E3-1 3435호(교수 소개·교수 명단 표기)[^faculty][^roster]
- 학과 연구실 소개의 사무실 표기: E3 3435호[^lab]
[^home]: Machine Learning and Mind Lab 첫 화면, 연구 목표·연구 갈래·연구실 소식(접힌 지난 소식 포함)·연락처. <https://mlml.kaist.ac.kr/> 관측 2026-10-27·2026-10-28.
[^research]: 연구실 Research, 연구 목표·현재 연구·방법·응용. <https://mlml.kaist.ac.kr/868a546b-3b18-4309-b4ad-3b7e3fd9e9ad> 관측 2026-10-28.
[^pubs]: 연구실 Publications, 2021–2026년 논문 목록·저자·발표처. <https://mlml.kaist.ac.kr/338b2614-886e-45ee-ae83-ef3b6dd8998a> 관측 2026-10-28.
[^members]: 연구실 People, 현재 구성원·협력자·이전 구성원. <https://mlml.kaist.ac.kr/people> 관측 2026-10-28.
[^center]: KAIST-Mila Prefrontal AI Research Center, 센터 연구·구성·출범일. <https://mlml.kaist.ac.kr/998ebcf3-3f9e-449c-bd8c-fbfc9e3c9c29> 관측 2026-10-28.
[^lab]: KAIST 전산학부 연구실 소개, 국문 이름·교수·연구 소개·위치. <https://cs.kaist.ac.kr/research/labView?sn=115&menu=64> 관측 2026-10-27.
[^roster]: KAIST 전산학부 교수 명단, 안성진 부교수·전공·교수연구실. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-27.
[^faculty]: KAIST 전산학부 안성진 교수 소개, 직위·부임 연도·경력·학위·전문 분야. <https://cs.kaist.ac.kr/people/view?idx=622&kind=faculty&menu=160> 관측 2026-10-28.
[^crafter]: 연구실 CrafterDojo 연구 소개 글, 게시일 2025-08-25. <https://mlml.kaist.ac.kr/25ad50e9-3ef1-8046-983e-dcedba985fad> 관측 2026-10-28.
[^abcd]: 연구실 The ABCD of Diffusion-Based Inference Scaling! 소개 글, 게시일 2025-06-28. <https://mlml.kaist.ac.kr/220d50e9-3ef1-8076-a24a-c0acb9e621ce> 관측 2026-10-28.
[^fast]: 연구실 Fast Monte Carlo Tree Diffusion 소개 글, 게시일 2025-06-25. <https://mlml.kaist.ac.kr/21dd50e9-3ef1-80ff-a07f-cf413434494a> 관측 2026-10-28.
[^award]: 연구실 Best Paper Award in ICML Compositional Learning Workshp, Created 2026/07/29 06:13(게시일). <https://mlml.kaist.ac.kr/3acd50e9-3ef1-8003-9c28-e3be0475ec50> 관측 2026-10-28.
[^p1]: G. Singh, Y. Kim, S. Ahn, arXiv (온라인 2022-11-02). <https://doi.org/10.48550/arXiv.2211.01177> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2211.01177> 관측 2026-10-28.
[^p2]: J. Baek, Y.-F. Wu, G. Singh, S. Ahn, arXiv (온라인 2025-01-24). <https://doi.org/10.48550/arXiv.2501.14174> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2501.14174> 관측 2026-10-28.
[^p3]: C. Chen 외, S. Ahn, arXiv (온라인 2024-06-10). <https://doi.org/10.48550/arXiv.2406.06793> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2406.06793> 관측 2026-10-28.
[^p4]: J. Yoon 외, S. Ahn, arXiv (온라인 2025-02-11). <https://doi.org/10.48550/arXiv.2502.07202> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.07202> 관측 2026-10-28.
[^p5]: J. Park, J. Cho, S. Ahn, arXiv (온라인 2024-11-11). <https://doi.org/10.48550/arXiv.2411.06736> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2411.06736> 관측 2026-10-28.
[^p6]: M. Jo 외, S. Ahn, arXiv (온라인 2025-10-22). <https://doi.org/10.48550/arXiv.2510.19304> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.19304> 관측 2026-10-28.
[^p7]: D. Baek 외, S. Ahn, arXiv (온라인 2026-05-05). <https://doi.org/10.48550/arXiv.2605.03413> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.03413> 관측 2026-10-28.
[^p8]: J. Baek 외, S. Ahn, arXiv (온라인 2026-05-19). <https://doi.org/10.48550/arXiv.2605.19376> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.19376v3> 관측 2026-10-28.

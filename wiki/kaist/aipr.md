# KAIST AIPR Lab (Artificial Intelligence & Probabilistic Reasoning Lab)

**KAIST 김재철AI대학원 · 김기응 교수**

- 분야: 불확실한 환경의 의사결정, 강화학습과 모사학습, 언어 모델의 학습·안전성·내부 해석, 여러 관측의 공통 표현 학습[^pi][^home][^p6][^p8]
- 대분야: 컴퓨팅·AI
- 태그: 강화학습[^pi][^home], 대형 언어 모델[^home][^p1][^p3], 생성 인공지능[^home][^p2]
- 홈페이지: <https://ailab.kaist.ac.kr/>
- 근거와 출처: [KAIST AIPR Lab 근거 페이지](aipr-sources.md)

> 불확실한 상황에서 행동을 정하는 학습 알고리즘을 연구하고, 저장된 경험을 활용한 의사결정부터 언어·이미지 생성의 학습과 안전성까지 다룬다.[^pi][^home][^p5][^p6]

## 무엇을 연구하나

KAIST AIPR Lab은 김기응 교수의 인공지능(Artificial Intelligence, AI) 연구실이다. 기계학습(자료에서 예측이나 판단에 쓸 규칙을 배우는 계산 기술)을 연구한다. 교수의 연구 소개는 의사결정 문제를 표현하는 모형, 그 모형을 자료에서 배우는 방법, 효율적인 알고리즘(문제를 풀기 위해 정해진 순서로 수행하는 계산 절차)과 응용을 연구 대상으로 든다. 특히 마르코프 의사결정 과정(Markov Decision Process, MDP: 현재 상태와 행동으로 다음 상황의 확률과 보상을 나타내는 의사결정 모형)과 부분 관측 마르코프 의사결정 과정(Partially Observable Markov Decision Process, POMDP: 실제 상태를 모두 알 수 없어 관측값으로 상태를 확률적으로 추정하며 행동하는 의사결정 모형)을 다룬다. 강화학습(Reinforcement Learning, RL: 장기적인 누적 보상을 키우는 행동 규칙을 배우는 기계학습 방법)이 교수의 주요 전문 분야다.[^pi][^gsai]

한 갈래는 **저장된 경험으로 배우는 의사결정**이다. 오프라인 강화학습(환경과 새로 상호작용하지 않고 이미 모은 경험으로 행동 규칙을 배우는 방법)에서는 학습한 행동과 자료를 모을 때의 행동이 달라져 생기는 문제가 중요하다. 연구실은 전문가의 상태 관측만으로 행동을 따라 배우는 방법, 목표에 맞춰 경험의 일부를 이어 계획을 만드는 방법, 여러 에이전트(주변 정보를 받아 판단하고 행동하는 주체)의 결합 행동을 배우는 알고리즘을 개발한다. 전문가의 행동 표시가 없는 관측 자료와 별도의 행동 표시 자료를 함께 쓰는 연구, 여러 주체의 행동이 결합될 때 자료 범위를 벗어나는 선택을 피하는 연구가 여기에 속한다.[^p7][^p5][^p6]

또 다른 갈래는 **글과 이미지를 만드는 모형의 학습과 안전성**이다. 대형 언어 모델(Large Language Model, LLM: 많은 글을 학습해 글을 이해하고 생성하는 큰 계산 모형)의 답변을 강화학습으로 개선하면서, 답변의 중간 단계가 결과에 얼마나 기여하는지 배우는 방법을 연구한다.[^home][^p1] 사용자의 요청이 시스템 지시와 충돌할 때 시스템 지시를 우선하도록 직접 선호 최적화(Direct Preference Optimization, DPO: 선호하는 답변과 선호하지 않는 답변의 비교로 언어 모델을 학습하는 방법)를 적용하는 학습 방법을 개발한다.[^home][^p3] 신경망(연결된 계산 단위들이 입력을 변환하도록 구성한 모형) 내부의 개념을 분리해 해석하고 매개변수에 담긴 지식을 조절하는 구조도 다룬다.[^home][^p4] 이미지 생성에서는 확산 모형(자료에 잡음을 더하는 과정의 반대 방향을 학습해 새 자료를 만드는 생성 모형)이 이미지를 만드는 도중 원치 않는 개념을 억제하는 방법을 개발한다.[^home][^p2]

**여러 관측을 공통 표현으로 묶는 학습**도 연구한다. 표현 학습(원자료에서 과제에 유용한 특징을 나타내는 방법을 자료로 배우는 일)은 서로 다른 관측이 공유하는 정보를 계산에 쓸 수 있는 형태로 정리한다. 연구실은 관측들 사이의 상관을 담으면서도 간결한 표현을 배우도록 학습 목표를 세우고, 일부 관측이 불규칙하게 빠진 경우로 방법을 확장했다. 서로 다른 관측 사이의 변환과 분류 과제로 방법을 평가했다.[^p8]

## 주요 연구 주제

### 1. 오프라인 강화학습과 관측 기반 모사학습

행동을 직접 시험하기 어려운 환경에서 저장된 경험을 활용한다. 전문가가 어떤 행동을 했는지 표시되지 않은 상태 관측으로부터 행동 규칙을 배운다.[^p7] 목표와 기대 가치를 조건으로 확산 모형이 미래 계획을 생성하고 경험의 일부를 연결하는 학습 방법을 개발한다.[^p5]

### 2. 다중 에이전트의 결합 행동과 분포 차이

여러 에이전트가 함께 행동할 때 각각의 선택만으로는 드러나지 않는 결합 행동의 문제를 다룬다. 중앙에서 에이전트를 하나씩 번갈아 학습시키며, 저장된 자료의 범위를 벗어나는 결합 행동을 피하는 알고리즘을 제안했다.[^p6]

### 3. 언어·이미지 생성의 학습, 안전성, 해석

언어 모델의 답변 중간 단계에 가치(그 단계 뒤에 기대되는 누적 보상)를 부여하는 학습, 시스템 지시를 우선하는 안전 학습, 내부 개념을 분리하는 신경망 구조를 연구한다. 이미지 생성에서는 모형의 잡음 예측으로 원치 않는 개념의 존재를 추정하고 생성 과정의 제어 강도를 조절한다.[^p1][^p3][^p4][^p2]

### 4. 여러 관측 사이의 공통 표현

서로 다른 관측들의 상관을 공통 표현에 담는 학습 목표를 연구한다. 자료 일부가 빠진 상황에서도 공통 표현을 배우는 방법을 다루며 관측 사이 변환과 분류에 적용한다.[^p8]

## 대표 논문

김기응 교수가 저자로 참여한 2021–2026년 논문을 연구 갈래와 시기에 걸쳐 골랐다. 발표처와 연도는 연구실 기재를 따랐다. 「쉽게 말하면」 칸은 각 논문의 연구실 게시 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Group-Normalized Implicit Value Optimization for Language Models](https://ailab.kaist.ac.kr/publications) · International Conference on Learning Representations(ICLR), 연구실 기재 | 언어 모델의 답변 전체에만 보상이 주어지면 중간 단계의 기여를 배우기 어렵다. 별도의 가치 평가 신경망을 두지 않고, 여러 답변을 묶어 값을 정규화하는 학습 목표로 단계별 가치를 정책 자체에서 배우는 방법을 제안했다. 글 생성과 추론 과제로 효과를 평가했다.[^p1] | 1저자 Yunseon Choi, 마지막 저자 김기응 |
| 2 | 2026 | [Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling](https://ailab.kaist.ac.kr/publications) · International Conference on Machine Learning(ICML), 연구실 기재 | 글로 요청한 이미지를 생성할 때 원치 않는 개념을 억제하는 제어를 제안했다. 추가 학습 없이 모형의 잡음 예측만으로 각 생성 단계의 개념 존재를 추정하고, 설정한 한계를 지키도록 억제 강도를 조절한다. 여러 공격 평가에서 공격 성공률을 낮추면서 정상 요청의 이미지 충실도를 높였다.[^p2] | 1저자 Yoonseok Choi, 마지막 저자 김기응 |
| 3 | 2025 | [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://ailab.kaist.ac.kr/publications) · Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics(NAACL), 연구실 기재 | 언어 모델의 안전 지침을 우회하는 요청에 대응하기 위해, 사용자 지시보다 시스템 지시를 우선하도록 목표를 조건으로 학습하는 방법을 제안했다. 다양한 공격에서 안전성과 일반 성능의 균형을 평가했으며, Vicuna-7B에서는 일반 성능을 저하시키지 않고 공격 성공률을 67.1%에서 5.0%로 낮췄다.[^p3] | 1저자 Joo Bon Maeng, 마지막 저자 김기응 |
| 4 | 2025 | [Monet: Mixture of Monosemantic Experts for Transformers](https://ailab.kaist.ac.kr/publications) · ICLR, 연구실 기재 | 신경망의 한 계산 단위가 여러 무관한 개념에 반응하면 내부 동작을 해석하기 어렵다. 학습 과정에 개념을 분리하는 구조를 직접 넣어 여러 전문 모듈을 학습하는 모형을 제안했다. 모듈에 담긴 지식을 분석하고, 일반 성능을 떨어뜨리지 않으면서 분야·언어·유해성 관련 지식을 조절할 수 있음을 보였다.[^p4] | 1저자 Jungwoo Park, 공저자 김기응, 마지막 저자 Jaewoo Kang |
| 5 | 2024 | [Stitching Sub-Trajectories with Conditional Diffusion Model for Goal-Conditioned Offline RL](https://doi.org/10.1609/aaai.v38i12.29215) · AAAI Conference on Artificial Intelligence, 연구실 기재 | 목표에 도달할 때만 보상이 주어지고 최적이 아닌 경험이 유한하게 주어진 상황에서, 저장된 경험의 유용한 부분들을 연결해 계획을 만드는 방법을 제안했다. 목표와 가치를 조건으로 확산 모형이 미래 계획을 생성하게 하며, 최적이지 않은 경험 조각을 이어 높은 품질의 계획을 만들 수 있음을 평가했다.[^p5] | 1저자 Sungyoon Kim, 마지막 저자 김기응 |
| 6 | 2023 | [AlberDICE: Addressing Out-Of-Distribution Joint Actions in Offline Multi-Agent RL via Alternating Stationary Distribution Correction Estimation](https://ailab.kaist.ac.kr/publications) · Advances in Neural Information Processing Systems(NeurIPS), 연구실 기재 | 여러 에이전트가 각각 무난한 행동을 골라도 그 조합은 저장된 경험의 범위를 벗어날 수 있다. 중앙 학습에서 에이전트를 하나씩 번갈아 개선하고 분포를 최적화하는 알고리즘을 제안했다. 결합 행동의 선택 문제를 다루며 여러 다중 에이전트 강화학습 과제에서 기존 방법과 비교했다.[^p6] | 1저자 Daiki E. Matsunaga, 마지막 저자 김기응 |
| 7 | 2022 | [LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation](https://ailab.kaist.ac.kr/publications) · NeurIPS, 연구실 기재 | 전문가가 어떤 행동을 했는지 모르는 상태 관측만으로 전문가를 따라 배우는 문제를 다룬다. 환경과 새로 상호작용하지 않고, 품질이 알려지지 않은 별도의 행동 표시 자료를 함께 이용한다. 전문가와 학습 주체가 만드는 상태 변화의 분포 차이를 줄이는 최적화 문제로 행동을 학습했다.[^p7] | 1저자 Geon-Hyeong Kim, 마지막 저자 김기응 |
| 8 | 2021 | [Multi-View Representation Learning via Total Correlation Objective](https://ailab.kaist.ac.kr/publications) · NeurIPS, 연구실 기재 | 여러 관측에 공통으로 담긴 정보를 간결한 표현으로 배우는 방법을 제안했다. 공통 표현이 관측 사이의 상관을 얼마나 설명하는지에 따라 학습 목표를 세운다. 관측 일부가 불규칙하게 빠지는 경우에도 적용하도록 확장하고, 관측 사이 변환과 분류 과제에서 효과를 평가했다.[^p8] | 1저자 HyeongJoo Hwang, 마지막 저자 김기응 |

## 교수와 전문 분야

김기응 교수는 KAIST 김재철AI대학원 전임교수다. 대학원은 연구분야를 인공지능, 기계학습, 강화학습으로 소개한다.[^gsai] 교수의 연구 소개는 대규모 마르코프 의사결정 과정과 부분 관측 의사결정 문제의 표현·모형 학습·효율적인 알고리즘을 핵심으로 든다.[^pi] 2021년 ICML의 OptiDICE 논문에도 KAIST 전산학부와 AI대학원 소속 저자로 참여했다.[^history]

최근 논문에서 드러나는 전문 분야는 저장된 자료만으로 행동을 배우는 강화학습과 모사학습, 여러 주체의 결합 행동 학습, 언어 모델의 학습·안전성·내부 해석, 여러 관측 사이 공통 표현 학습이다. 이는 관측 기반 모사학습, 다중 에이전트의 결합 행동, 언어 모델의 단계별 기여도와 안전 지시, 공통 표현의 학습 목표를 다룬 논문들에 근거한 요약이다.[^p7][^p6][^p1][^p3][^p4][^p8]

## 응용 분야

언어 모델에서는 글 생성·추론의 학습과 안전 지시 준수, 이미지 생성에서는 원치 않는 개념의 억제를 다룬다.[^p1][^p3][^p2] 행동 학습에서는 저장된 경험으로 목표 지향 과제의 계획을 만들고 여러 에이전트의 결합 행동을 학습한다.[^p5][^p6] 관측 표현 학습은 서로 다른 관측 사이의 변환과 분류에 적용한다.[^p8]

## 구성원

2026년 11월 9일 연구실 People의 박사과정 8명과 석사과정 4명이다. 과정은 게시 구획을 따랐다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Daiki E. Matsunaga | 박사과정 | 5, 6 |
| Heesan Kong | 박사과정 |  |
| Doohwan Hwang | 박사과정 | 1 |
| Namho Koh | 박사과정 |  |
| Sungkuk Shyn | 박사과정 |  |
| Seungjin Kim | 박사과정 |  |
| Sanghee Park | 박사과정 |  |
| Taeseung You | 박사과정 |  |
| Chaeyoung Oh | 석사과정 | 1, 2 |
| Tien Tran | 석사과정 |  |
| Seungwan Kang | 석사과정 |  |
| Changwoo Yoo | 석사과정 |  |

## 졸업생과 이전 구성원

연구실 People의 Alumni에 적힌 51명이다. MS는 Master of Science(석사), PhD는 Doctor of Philosophy(박사)이며, Post Doc은 박사후연구원 경력을 가리킨다. 학위·역할과 연도는 연구실의 게시 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Junyoung Jang (장준영) | MS (2026) |  |
| Junho Na (나준호) | MS (2026) |  |
| Yoonseok Choi (최윤석) | MS (2026) |  |
| Myriam Schoenenberger (미리얌) | MS (2026) |  |
| Hyunjun Choi (최현준) | Post Doc (2026) |  |
| Yunseon Choi (최윤선) | PhD (2026) |  |
| Seokin Seo (서석인) | PhD (2026) |  |
| Myeongheon Choi (최명헌) | MS (2026) |  |
| Young Jin Ahn (안영진) | MS (2025) |  |
| Youngjae Joo (주영재) | MS (2025) |  |
| Seongmin Lee (이성민) | MS (2025) |  |
| JooBon Maeng (맹주본) | MS (2025) |  |
| Haanvid Lee (이한빛) | PhD (2024) |  |
| HyeongJoo Hwang (황형주) | PhD (2024) |  |
| Ohjoon Kwon (권오준) | MS (2024) |  |
| Tri Wahyu Guntara (군타라) | MS (2024) |  |
| Jinjae Lee (이진재) | MS (2024) |  |
| Seonghyun Ban (반성현) | MS (2023) |  |
| Jaewook Shin (신재욱) | MS (2023) |  |
| Seunghyun Hwang (황승현) | MS (2023) |  |
| Jaeseok Yoon (윤재석) | MS (2023) |  |
| Haeju Lee (이해주) | MS (2023) |  |
| Sungyoon Kim (김성윤) | MS (2023) |  |
| Youngsoo Jang (장영수) | PhD (2022) |  |
| Geon-Hyeong Kim (김건형) | PhD (2022) |  |
| Jongmin Lee (이종민) | PhD (2022) |  |
| Sunghoon Hong (홍성훈) | MS (2022) |  |
| Deunsol Yoon (윤든솔) | MS (2022) |  |
| Jinhyeon Kim (김진현) | MS (2022) |  |
| Youngjune Lee (이영준) | MS (2022) |  |
| Donghoon Ham (함동훈) | MS (2021) |  |
| Jeong-Gwan Lee (이정관) | MS (2021) |  |
| Byung-Jun Lee (이병준) | PhD (2021) |  |
| Shinhyung Kim (김신형) | MS (2020) |  |
| Wonseok Jeon (전원석) | Post Doc (2019) |  |
| Kanghoon Lee (이강훈) | PhD (2019) |  |
| Soohyun Lim (임수현) | MS (2019) |  |
| Jiyeon Ham (함지연) | MS (2018) |  |
| Daehyun Lee (이대현) | MS (2018) |  |
| Taekgyu Hong (홍택규) | MS (2016) |  |
| Jungpyo Hong (홍정표) | MS (2016) |  |
| Hyeoneun Kim (김현은) | MS (2014) |  |
| Daejoong Kim (김대중) | MS (2014) |  |
| Jaedeug Choi (최재득) | PhD (2013) |  |
| Bongseok Goh (고봉석) | MS (2013) |  |
| Beom-Yong Ha (하범용) | MS (2013) |  |
| Heejin Lim (임희진) | MS (2012) |  |
| Dongho Kim (김동호) | PhD (2011) |  |
| Eunsoo Oh (오은수) | MS (2011) |  |
| Youngwook Kim (김영욱) | MS (2009) |  |
| Dajinseol Jeon (전다진솔) | MS (2008) |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 2021–2026년 구역에서 김기응 교수가 저자로 참여한 55편이다. 제목·저자·발표처는 연구실 표기를 따랐다. 연도는 게시 연도 구역이며, 2021년 항목 중 날짜가 연도까지만 제시된 것은 그 연도 구역에 둔다. 학회명만 적힌 항목의 발표처는 연구실 기재이며, arXiv로 적힌 항목은 사전 공개본이다.[^pubs]

**2026**

- Myriam Schonenberger, Kee-Eung Kim. "Discovering Control Symmetries via Transition Manifold Tangency". *Conference on Robot Learning (CoRL)*.
- Seokin Seo, Sung Kuk Shyn, Minji Seo, Yisoo Lee†, Jongmin Lee†, Hongseok Yang†, Kee-Eung Kim†. "DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning". *Advances in Neural Information Processing Systems (NeurIPS)*.
- Doo Hwan Hwang, Junyoung Jang, Junho Na, Hosung Lim, Kee-Eung Kim. "Behavior-Preserving KV Cache Compression". *Empirical Methods in Natural Language Procesesing (EMNLP)*.
- Junho Na, Daiki E. Matsunaga, Namho Koh, Jongmin Lee, Pascal Poupart, Kee-Eung Kim. "Dynamic Context Allocation for Concurrent Multi-Agent LLMs". *Empirical Methods in Natural Language Procesesing (EMNLP)*. <https://doi.org/10.18653/2026.emnlp-main.1785>
- Tien Tran\*, Namho Koh\*, Daiki E. Matsunaga, Ayush Jain, Kee-Eung Kim. "Same Tasks, Different Apps: Why Mobile GUI Agents Fail to Generalize?". *Findings of Empirical Methods in Natural Language Procesesing (EMNLP)*.
- Sanghee Park, Kee-Eung Kim. "PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models". *Findings of Empirical Methods in Natural Language Procesesing (EMNLP)*.
- 황두환, 김기응. "Hindsight PPO : RLHF를 위한 토큰 수준 기여도 할당". *한국컴퓨터종합학술대회(KCC)*.
- 장준영, 강승완, 김기응. "Stein 사후분포 수송을 이용한 Flow 기반 오프라인 강화학습". *한국컴퓨터종합학술대회(KCC)*.
- 김승진, 최윤석, 김기응. "이미지 유사도 기반 디퓨전 모델의 동적 부정 VLM 프롬프팅 가속화". *한국컴퓨터종합학술대회(KCC)*.
- 신성국, 김기응. "방해 요소 환경에서의 강건한 잠재 행동 학습: 변분 정보 병목과 SIGReg의 결합". *한국컴퓨터종합학술대회(KCC)*.
- Yoonseok Choi, Chaeyoung Oh, Hyunjun Choi, Seokin Seo, Kee-Eung Kim. "Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling". *International Conference on Machine Learning (ICML)*.
- Doohwan Hwang, Kee-Eung Kim. "PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF". *International Conference on Machine Learning (ICML)*.
- Daiki E. Matsunaga, Junho Na, Tri Wahyu Guntara, Scott Sanner, Pascal Poupart†, Jongmin Lee†, Kee-Eung Kim† (†Equal advising). "ACPO: Agent-Chained Policy Optimization for Multi-Agent Reinforcement Learning". *Reinforcement Learning Conference (RLC)*.
- Yunseon Choi, Junyoung Jang, Chaeyoung Oh, Minchan Jeong, Doohwan Hwang, Kee-Eung Kim. "Group-Normalized Implicit Value Optimization for Language Models". *International Conference on Learning Representations (ICLR)*.

**2025**

- Yunseon Choi, Minchan Jeong, Soobin Um, Kee-Eung Kim. "DPAIL: Training Diffusion Policy for Adversarial Imitation Learning without Policy Optimization". *Advances in Neural Information Processing Systems (NeurIPS)*.
- 나준호, 김기응. "조건부 변분 오토인코더를 활용한 대규모 언어 모델의 추론 성능 향상 기법". *한국컴퓨터종합학술대회(KCC)*.
- 장준영, 김기응. "순위 가중 보상을 활용한 대규모 언어 모델의 강화학습 기반 최적화". *한국컴퓨터종합학술대회(KCC)*.
- Joo Bon Maeng\*, Seongmin Lee\*, Seokin Seo, Kee-Eung Kim. "Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions". *Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL)*.
- Jungwoo Park\*, Young Jin Ahn\*, Kee-Eung Kim, Jaewoo Kang. "Monet: Mixture of Monosemantic Experts for Transformers". *International Conference on Learning Representations (ICLR)*.

**2024**

- Seonghyun Ban\*, Heesan Kong\*, Kee-Eung Kim. "Data Augmentation with Diffusion for Open-Set Semi-Supervised Learning". *Advances in Neural Information Processing Systems (NeurIPS)*. <https://doi.org/10.52202/079017-2074>
- Seokin Seo, Byung-Jun Lee, Jongmin Lee, HyeongJoo Hwang, Hongseok Yang, Kee-Eung Kim. "Mitigating Covariate Shift in Behavioral Cloning via Robust Stationary Distribution Correction". *Advances in Neural Information Processing Systems (NeurIPS)*. <https://doi.org/10.52202/079017-3466>
- Seongmin Lee\*, Jaewook Shin\*, Young Jin Ahn, Seokin Seo, Ohjoon Kwon, Kee-Eung Kim. "Zero-Shot Multi-Hop Question Answering via Monte-Carlo Tree Search with Large Language Models". *arXiv*. <https://doi.org/10.48550/arxiv.2409.19382>
- Oh Joon Kwon, Daiki E. Matsunaga, Kee-Eung Kim. "GDPO: Learning to Directly Align Language Models with Diversity Using GFlowNets". *Empirical Methods in Natural Language Procesesing (EMNLP)*. <https://doi.org/10.18653/v1/2024.emnlp-main.951>
- Young Jin Ahn\*, Jungwoo Park\*, Sangha Park, Jonghyun Choi, Kee-Eung Kim. "SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization". *Interspeech*. <https://doi.org/10.21437/interspeech.2024-432>
- Yunseon Choi, Sangmin Bae, Seonghyun Ban, Minchan Jeong, Chuheng Zhang, Lei Song, Li Zhao, Jiang Bian, Kee-Eung Kim. "Hard Prompts Made Interpretable: Sparse Entropy Regularization for Prompt Tuning with RL". *Association for Computational Linguistics (ACL)*. <https://doi.org/10.18653/v1/2024.acl-long.449>
- Yunseon Choi, Li Zhao, Chuheng Zhang, Lei Song, Jiang Bian, Kee-Eung Kim. "Diversification of Adaptive Policy for Effective Offline Reinforcement Learning". *International Joint Conference on Artificial Intelligence (IJCAI)*. <https://doi.org/10.24963/ijcai.2024/427>
- 최윤선, 황두환, 김기응. "디퓨전 모델의 소량 데이터 학습자로서 활용한 다양한 데모 데이터로부터의 오프라인 모사 학습". *한국컴퓨터종합학술대회(KCC)*.
- Haanvid Lee, Tri Wahyu Guntara, Jongmin Lee, Yung-Kyun Noh, Kee-Eung Kim. "Kernel Metric Learning for In-Sample Off-Policy Evaluation of Deterministic RL Policies". *International Conference on Learning Representations (ICLR)*.
- Kyungsik Lee, Hana Yoo, Sumin Shin, Wooyoung Kim, Yeonung Baek, Hyunjin Kang, Jaehyun Kim, Kee-Eung Kim. "A Submodular Optimization Approach to Accountable Loan Approval". *IAAI Technical Track on Deployed Highly Innovative Applications of AI (IAAI)*. <https://doi.org/10.1609/aaai.v38i21.30310>
- Sungyoon Kim, Yunseon Choi, Daiki E. Matsunaga, Kee-Eung Kim. "Stitching Sub-Trajectories with Conditional Diffusion Model for Goal-Conditioned Offline RL". *AAAI Conference on Artificial Intelligence*. <https://doi.org/10.1609/aaai.v38i12.29215>
- 윤재석, 황승현, 김기응. "대규모 언어 모델을 활용한 음성 기반 대화 시스템의 가능성 연구". *한국통신학회*.

**2023**

- 최윤선, 반성현, 김기응. "해석 가능한 프롬프트 최적화에 관한 강화학습 연구". *한국소프트웨어종합학술대회(KSC) 2023, 한국정보과학회*.
- Mihye Kim, Jimyung Choi, Jaehyun Kim, Wooyoung Kim, Yeonung Baek, Gisuk Bang, Kwangwoon Son, Yeonman Ryou, Kee-Eung Kim. "Trustworthy residual vehicle value prediction for auto finance". *AI Magazine*.
- Haeju Lee\*, Minchan Jeong\*, Se-Young Yun, and Kee-Eung Kim. "Bayesian Multi-Task Transfer Learning for Soft Prompt Tuning". *Findings of Empirical Methods in Natural Language Processing (EMNLP)*. <https://doi.org/10.18653/v1/2023.findings-emnlp.329>
- Seokin Seo, HyeongJoo Hwang, Hongseok Yang, and Kee-Eung Kim. "Regularized Behavior Cloning for Blocking the Leakage of Past Action Information". *Advances in Neural Information Processing Systems (NeurIPS)*.
- Daiki E. Matsunaga\*, Jongmin Lee\*, Jaeseok Yoon, Stefanos Leonardos, Pieter Abbeel, and Kee-Eung Kim. "AlberDICE: Addressing Out-Of-Distribution Joint Actions in Offline Multi-Agent RL via Alternating Stationary Distribution Correction Estimation". *Advances in Neural Information Processing Systems (NeurIPS)*.
- Jaeseok Yoon\*, Seunghyun Hwang\*, Ran Han, Jeonguk Bang, and Kee-Eung Kim. "Adapting Text-based Dialogue State Tracker for Spoken Dialogues". *Special Interest Group on Discourse and Dialogue (SIGDIAL) DSTC11 Workshop*.
- HyeongJoo Hwang, Seokin Seo, Youngsoo Jang, Sungyoon Kim, Geon-Hyeong Kim, Seunghoon Hong, and Kee-Eung Kim. "Information-Theoretic State Space Model for Multi-View Reinforcement Learning". *Proceedings of International Conference on Machine Learning (ICML)*.
- Mihye Kim, Jimyung Choi, Jaehyun Kim, Wooyoung Kim, Yeonung Baek, Gisuk Bang, Kwangwoon Son, Yeonman Ryou, and Kee-Eung Kim. "Trustworthy Residual Vehicle Value Prediction for Auto Finance". *Proceedings of IAAI Technical Track on deployed Highly Innovative Applications of AI*. <https://doi.org/10.1609/aaai.v37i13.26842>

**2022**

- 서석인, 황형주, 양홍석, and 김기응. "특징조합 교란자 균형을 통한 인과정규화된 로지스틱 회귀 개선". *한국소프트웨어종합학술대회(KSC) 2022, 한국정보과학회*.
- Geon-Hyeong Kim\*, Jongmin Lee\*, Youngsoo Jang, Hongseok Yang, and Kee-Eung Kim. "LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation". *Advances in Neural Information Processing Systems (NeurIPS)*.
- Haanvid Lee, Jongmin Lee, Yunseon Choi, Wonseok Jeon, Byung-Jun Lee, Yung-Kyun Noh, and Kee-Eung Kim. "Local Metric Learning for Off-Policy Evaluation in Contextual Bandits with Continuous Actions". *Advances in Neural Information Processing Systems (NeurIPS)*.
- Sanghoon Myung, In Huh, Wonik Jang, Jae Myung Choe, Jisu Ryu, Daesin Kim, Kee-Eung Kim, and Changwook Jeong. "PAC-Net: A Model Pruning Approach to Inductive Transfer Learning". *Proceedings of International Conference on Machine Learning (ICML)*.
- Jinhyeon Kim and Kee-Eung Kim. "Data Augmentation for Learning to Play in Text-Based Games". *Proceedings of International Joint Conference on Artificial Intelligence (IJCAI)*. <https://doi.org/10.24963/ijcai.2022/436>
- Haeju Lee\*, Oh Joon Kwon\*, Yunseon Choi\*, Minho Park, Ran Han, Yoonhyung Kim, Jinhyeon Kim, Youngjune Lee, Haebin Shin, Kangwook Lee, and Kee-Eung Kim. "Learning to Embed Multi-Modal Contexts for Situated Conversational Agents". *Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) Findings*. <https://doi.org/10.18653/v1/2022.findings-naacl.61>
- Haeju Lee\*, Oh Joon Kwon\*, Yunseon Choi\*, Jinhyeon Kim, Youngjune Lee, Ran Han, Yoonhyung Kim, Minho Park, Kangwook Lee, Haebin Shin, and Kee-Eung Kim. "Tackling Situated Multi-Modal Task-Oriented Dialogs with a Single Transformer Model". *AAAI Conference on Artificial Intelligence (AAAI) DSTC10 Workshop*.
- Sunghoon Hong, Deunsol Yoon, and Kee-Eung Kim. "Structure-Aware Transformer Policy for Inhomogeneous Multi-Task Reinforcement Learning". *International Conference on Learning Representations (ICLR)*.
- Youngsoo Jang, Jongmin Lee, and Kee-Eung Kim. "GPT-Critic: Offline Reinforcement Learning for End-to-End Task-Oriented Dialogue Systems". *International Conference on Learning Representations (ICLR)*.
- Geon-Hyeong Kim, Seokin Seo, Jongmin Lee, Wonseok Jeon, HyeongJoo Hwang, Hongseok Yang, and Kee-Eung Kim. "DemoDICE: Offline Imitation Learning with Supplementary Imperfect Demonstrations". *International Conference on Learning Representations (ICLR)*.
- Jongmin Lee, Cosmin Paduraru, Daniel J. Mankowitz, Nicolas Heess, Doina Precup, Kee-Eung Kim, and Arthur Guez. "COptiDICE: Offline Constrained Reinforcement Learning via Stationary Distribution Correction Estimation". *International Conference on Learning Representations (ICLR)*.

**2021**

- HyeongJoo Hwang, Geon-Hyeong Kim, Seunghoon Hong, and Kee-Eung Kim. "Multi-View Representation Learning via Total Correlation Objective". *Advances in Neural Information Processing Systems (NeurIPS)*.
- 김건형, 장영수, 이종민, and 김기응. "효율적인 다중태스크 오프라인 모델기반 강화학습 알고리즘에 대한 연구". *한국소프트웨어종합학술대회, 한국정보과학회*.
- Youngjune Lee, Oh Joon Kwon, Haeju Lee, Joonyoung Kim, Kangwook Lee, and Kee-Eung Kim. "Augment & Valuate : A Data Enhancement Pipeline for Data-Centric AI". *Neural Information Processing Systems (NeurIPS) Data-Centric AI workshop*.
- Youngjune Lee and Kee-Eung Kim. "Dual Correction Strategy for Ranking Distillation in Top-N Recommender System". *Proceedings of the 30th ACM International Conference on Information and Knowledge Management (CIKM)*. <https://doi.org/10.1145/3459637.3482093>
- Jinhyeon Kim, Donghoon Ham, Jeong-Gwan Lee, and Kee-Eung Kim. "End-to-End Document-Grounded Conversation with Encoder-Decoder Pre-Trained Language Model". *AAAI Conference on Artificial Intelligence (AAAI) DSTC9 Workshop*.

## 수상과 선정

연구실 Publications의 논문 옆에 적힌 2022–2024년 수상 4건이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다. 수상 이름은 게시 표기 그대로다.[^pubs]

- 2024 · Innovative application award · A Submodular Optimization Approach to Accountable Loan Approval
- 2023 · Track best paper · Adapting Text-based Dialogue State Tracker for Spoken Dialogues
- 2023 · Innovative application award · Trustworthy Residual Vehicle Value Prediction for Auto Finance
- 2022 · Track best paper · Tackling Situated Multi-Modal Task-Oriented Dialogs with a Single Transformer Model

## 연락과 위치

- 교수 이메일: kekim@kaist.ac.kr[^gsai]
- 교수 페이지의 위치: 서울특별시 서초구 태봉로 108 KAIST 양재캠퍼스(서울AI허브) 604호[^pi]
- 대학원 구성원 페이지의 사무실 표기: 양재캠퍼스 별관[^gsai]
[^p1]: Y. Choi 외, K.-E. Kim, International Conference on Learning Representations (ICLR) (2026). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p2]: Y. Choi 외, K.-E. Kim, International Conference on Machine Learning (ICML) (2026). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p3]: J. B. Maeng, S. Lee, S. Seo, K.-E. Kim, Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL) (2025). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p4]: J. Park, Y. J. Ahn, K.-E. Kim, J. Kang, International Conference on Learning Representations (ICLR) (2025). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p5]: S. Kim, Y. Choi, D. E. Matsunaga, K.-E. Kim, AAAI Conference on Artificial Intelligence (2024). <https://doi.org/10.1609/aaai.v38i12.29215> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p6]: D. E. Matsunaga 외, K.-E. Kim, Advances in Neural Information Processing Systems (NeurIPS) (2023). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p7]: G.-H. Kim 외, K.-E. Kim, Advances in Neural Information Processing Systems (NeurIPS) (2022). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^p8]: H. Hwang, G.-H. Kim, S. Hong, K.-E. Kim, Advances in Neural Information Processing Systems (NeurIPS) (2021). <https://ailab.kaist.ac.kr/publications> 초록 기준(연구실 Publications 게시 초록). 초록 원문 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^pi]: 김기응 교수 소개, Research Overview와 위치 <https://ailab.kaist.ac.kr/people/kekim> (2026-11-09 관측).
[^home]: KAIST AIPR Lab 첫 화면, 연구실 이름과 Featured Recent Publications의 논문별 초록 <https://ailab.kaist.ac.kr/> (2026-11-09 관측).
[^gsai]: KAIST 김재철AI대학원 구성원, 전임교수 구획의 김기응 교수 직위·연구분야·이메일·사무실 <https://gsai.kaist.ac.kr/people-2/?lang=ko> (2026-11-09 관측).
[^people]: 연구실 People, Lab Members와 Alumni <https://ailab.kaist.ac.kr/people/> (2026-11-09 관측).
[^pubs]: 연구실 Publications, 연도별 논문 목록과 개별 초록·수상 표기 <https://ailab.kaist.ac.kr/publications> (2026-11-09 관측).
[^history]: J. Lee, W. Jeon, B.-J. Lee, J. Pineau, K.-E. Kim, OptiDICE: Offline Policy Optimization via Stationary Distribution Correction Estimation, Proceedings of the 38th International Conference on Machine Learning (2021). 연구실 게시 논문의 초록과 첫 쪽 저자 소속 <https://ailab.kaist.ac.kr/papers/pdfs/LJLPK2021.pdf> (2026-11-11 관측).

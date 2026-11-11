# OSI LAB (Optimization and Statistical Inference Lab)

**KAIST 김재철AI대학원 · 윤세영 부교수**

- 분야: 행동 선택과 통계 추론, 인공지능의 생성·계산·평가, 여러 참여자의 공동 학습
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 강화학습[^home], 생성 인공지능[^home]
- 홈페이지: <https://osi.kaist.ac.kr/>
- 근거와 출처: [OSI LAB 근거 페이지](osi-sources.md)

> 어떤 행동을 선택하고 그 결과를 얼마나 믿을지 수학으로 분석하며, 글과 분자를 생성하는 인공지능의 학습·계산·평가 방법을 연구한다.[^home][^p1][^p2][^p3][^p7]

## 무엇을 연구하나

OSI LAB은 윤세영 교수가 이끄는 연구실로, 서울 홍릉캠퍼스에 있다. 연구실은 강화학습(Reinforcement Learning, 행동으로 얻는 보상의 합을 키우도록 시행착오로 행동을 배우는 방법)의 이론부터 생성 인공지능(Generative Artificial Intelligence, 학습한 자료의 특성을 바탕으로 새 글·이미지·소리 등을 만드는 인공지능)까지 연구한다고 소개한다.[^home]

한 갈래는 불확실한 상황에서 관측과 행동을 연결하는 수학적 방법이다. 밴딧(선택한 행동의 보상만 관측하며 행동을 고르는 순차적 의사결정 문제)에서는 한 선택지를 쓸수록 얻는 결과가 나빠질 때 어떤 선택을 해야 하는지 분석한다. 또 관측이 쌓이는 동안 알 수 없는 값을 어느 범위로 추정할지 계산하고, 그 범위로 다음 행동을 정하는 알고리즘(문제를 풀기 위한 계산 절차)을 제안한다.[^p1][^p2]

다른 갈래는 언어 모델(글을 이루는 단위들의 배열에 확률을 부여하는 계산 모형)의 비용과 평가다. 모델의 층을 반복해서 쓰면서 토큰(글을 쪼개 처리할 때 쓰는 기본 단위)마다 반복 깊이를 달리하는 방법, 확산 모델(자료에 잡음을 더했다가 되돌리는 과정을 학습해 새 자료를 만드는 모형)이 생성 중 확신한 부분을 함께 확정하는 방법을 개발한다. 글로 된 추론 설명으로 학습한 평가자가 이미지와 영상도 판단하도록 하는 연구도 있다.[^p3][^p4][^p5]

생성 결과를 원하는 방향으로 바꾸는 연구에서는 사람이 선호하지 않는 결과를 선호하는 결과로 옮기는 흐름을 학습한다. 분자(원자가 화학 결합으로 묶인 입자)의 입체 구조를 생성할 때 원하는 화학적 성질을 유도하면서도 타당한 구조를 유지하는 계산 방법도 제안한다.[^p6][^p7] 연합학습(자료를 한곳에 모으지 않고 여러 참여자가 각자 학습한 모형을 합쳐 함께 학습하는 방법)에서는 지역별 학습 때문에 앞서 배운 지식을 잊는 현상을 분석하고, 이를 줄이는 학습 방법을 개발한다.[^p8]

## 주요 연구 주제

### 1. 선택과 통계 추론

선택지를 사용할 때마다 보상이 줄어드는 문제에서 변화가 천천히 쌓이는 경우와 갑자기 일어나는 경우를 다룬다. 관측 자료에 맞춰 행동을 바꾸는 방법이 얻을 수 있는 성과의 한계를 분석한다. 일반화 선형 모형(입력의 가중합을 정해진 함수를 거쳐 관측 결과의 평균과 연결하는 통계 모형)에서는 관측이 계속 추가되어도 쓸 수 있는 추정 범위를 만들고 이를 행동 선택으로 연결한다.[^p1][^p2]

### 2. 언어 모델의 계산과 평가

반복 계산에 같은 층을 공유하고 토큰마다 계산 깊이를 정해, 매개변수(모형의 동작과 결과를 정하는 내부 수치)와 계산 자원의 사용을 함께 다룬다. 확산 생성의 반복 횟수를 줄이는 방법과, 글로 된 설명에서 배운 판단을 여러 종류의 자료에 적용하는 평가 방법도 연구한다.[^p3][^p4][^p5]

### 3. 선호에 맞는 결과와 분자 생성

사람의 선호 자료로 생성 결과를 바꾸는 흐름을 학습하고, 분자 생성에서는 원하는 성질과 생성된 구조의 타당성을 함께 고려한다. 분자 구조를 만드는 과정에서 진행 시점을 보정하는 새 생성 방법을 제안한다.[^p6][^p7]

### 4. 분산된 자료로 학습

연합학습에서 참여자마다 자료의 구성이 다를 때 공동 모형과 개별 모형이 기존 지식을 잊는 현상을 살핀다. 각 자료의 정답이 아닌 다른 범주(같은 기준으로 묶은 자료의 분류)에 대해서는 공동 모형의 판단을 보존하는 학습 방법을 제안한다.[^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문에서 선택·추론, 언어 모델의 계산·평가, 생성, 분산 학습을 고르게 보여 주는 논문을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자는 전체 저자 목록의 순서에 따른 표시다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [An Adaptive Approach for Infinitely Many-armed Bandits under Generalized Rotting Constraints](https://doi.org/10.52202/079017-0281) · NeurIPS 2024 | 선택지가 무한히 많고 한 선택지를 쓸 때마다 평균 보상이 줄어드는 문제를 다룬다. 보상이 줄어든 양의 합이 제한된 경우와 줄어드는 사건의 횟수가 제한된 경우를 나누고, 최근 관측을 사용하는 구간의 길이를 적응적으로 바꾸는 알고리즘을 제안했다. 두 경우의 성과 손실을 이론으로 분석하고 수치 실험으로 방법의 성능을 보였다.[^p1] | 1저자 Jung-hun Kim, 마지막 저자 Se-Young Yun |
| 2 | 2024 | [A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits](https://doi.org/10.52202/079017-3960) · NeurIPS 2024 | 관측이 계속 추가되는 동안 모르는 값을 추정하는 범위를 일반화 선형 모형에 공통으로 계산하는 방법을 제안했다. 이를 이용해 다음 행동을 고르는 알고리즘을 만들고, 여러 종류의 모형에서 성과 손실을 분석했다. 논문의 밴딧 수치 실험에서는 기존 알고리즘과 같거나 나은 성능을 보였다.[^p2] | 1저자 Junghyun Lee, 전체 3명 중 2번째 저자 Se-Young Yun |
| 3 | 2025 | [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](https://doi.org/10.52202/085713-3229) · NeurIPS 2025 | 언어 모델의 층을 여러 반복 단계에서 공유하고, 각 토큰에 필요한 반복 깊이를 달리 배정하는 MoR(Mixture-of-Recursions)을 제안했다. 각 깊이에서 아직 계산 중인 토큰끼리만 정보를 주고받도록 하고 필요한 중간 결과만 저장한다. 같은 학습 계산량과 작은 모델 크기에서 검증 자료의 글 예측 성능과 적은 예시를 주는 과제의 정확도를 개선했으며, 비교 모델보다 처리량을 높였다.[^p3] | 1저자 Sangmin Bae, 마지막 저자 Se-Young Yun |
| 4 | 2025 | [KLASS: KL-Guided Fast Inference in Masked Diffusion Models](https://doi.org/10.52202/085713-3087) · NeurIPS 2025 | 아직 정해지지 않은 토큰을 반복해서 채우는 확산 생성에서, 토큰별 예측이 얼마나 안정적인지 살펴 한 번에 여러 토큰을 확정하는 KLASS(KL-Adaptive Stability Sampling)를 제안했다. 모델을 추가로 학습시키지 않고 생성 속도를 높이면서 생성 자료의 품질을 유지했다. 글뿐 아니라 이미지와 분자 생성에서도 적용 가능성을 보였다.[^p4] | 1저자 Seo Hyun Kim, 마지막 저자 Se-Young Yun |
| 5 | 2025 | [Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators](https://doi.org/10.52202/085713-3625) · NeurIPS 2025 | 사람의 선호를 대신 평가하는 모델이 자료 종류마다 많은 학습 자료를 요구하는 문제를 다룬다. 적은 양의 글로 된 추론 설명으로 학습한 Flex-Judge가 이미지·영상 등 서로 다른 자료와 평가 형식을 판단하도록 했다. 실험에서는 상용 서비스와 여러 종류의 자료로 학습한 평가자에 견줄 만하거나 나은 성능을 보였고, 평가 자료가 드문 분자 분야에도 적용했다.[^p5] | 1저자 Jongwoo Ko, 마지막 저자 Se-Young Yun |
| 6 | 2024 | [Preference Alignment with Flow Matching](https://doi.org/10.52202/079017-1108) · NeurIPS 2024 | 사람이 선호하지 않는 결과를 선호하는 결과로 바꾸는 흐름을 선호 자료에서 직접 배우는 PFM(Preference Flow Matching)을 제안했다. 이미 학습한 모델 전체를 폭넓게 다시 조정하는 부담을 줄이고, 별도의 보상 함수를 추정하지 않고도 생성 결과를 사람의 선호와 맞추려는 방법이다. 기존 선호 기반 강화학습의 목표와의 관계를 이론으로 설명하고 실험으로 실용성을 보였다.[^p6] | 1저자 Minu Kim, 마지막 저자 Se-Young Yun |
| 7 | 2024 | [Conditional Synthesis of 3D Molecules with Time Correction Sampler](https://doi.org/10.52202/079017-2417) · NeurIPS 2024 | 원하는 화학적 성질을 만족시키는 것과 자료의 특성에 맞는 타당한 분자 구조를 만드는 일을 함께 다룬다. 생성 중 유도 강도를 적응적으로 조절하는 TACS(Time-Aware Conditional Synthesis)와 진행 시점을 보정하는 TCS(Time Correction Sampler)를 제안했다. 조건을 준 분자 입체 구조 생성에서 성능을 보였으며, 신약 탐색과 재료 연구를 위한 분자 역설계(원하는 성질에 맞는 분자 구조를 찾는 설계)에 활용할 가능성을 제시했다.[^p7] | 1저자 Hojung Jung, 전체 8명 중 7번째 저자 Se-Young Yun |
| 8 | 2022 | [Preservation of the Global Knowledge by Not-True Distillation in Federated Learning](https://doi.org/10.52202/068431-2787) · NeurIPS 2022 | 여러 참여자가 각자 자료로 학습한 결과를 합칠 때 자료의 차이 때문에 기존 지식을 잊는 문제를 분석했다. 지역 자료의 정답 범주를 제외한 다른 범주에 대해서는 공동 모형의 관점을 보존하는 FedNTD(Federated Not-True Distillation)를 제안했다. 실험에서는 자료를 직접 공유하거나 추가 통신 비용을 들이지 않으면서 여러 조건에서 성능을 높였다.[^p8] | 1저자 Gihun Lee, 마지막 저자 Se-Young Yun |

## 교수와 전문 분야

윤세영 교수는 KAIST에서 전기공학 학사와 박사 학위를 받았다. 교수 이력은 산업및시스템공학과 근무를 2017년 7월부터, AI대학원 근무를 2019년 5월부터로 적는다. 이전에는 KTH, MSR-INRIA Joint Research Center, Microsoft Research, Los Alamos National Laboratory에서 연구했다.[^prof] 김재철AI대학원 전임교수 목록의 직위는 부교수이며, 교수 개인 소개도 Associate Professor로 적는다.[^gsai][^prof]

최근 논문에서 확인되는 전문 분야는 관측에 따른 행동 선택의 이론과 통계 추론, 언어 모델의 계산량 조절과 평가, 선호에 맞춘 생성, 분산 학습에서의 지식 보존이다. 선택 과정의 한계를 수학으로 분석하는 연구와 실제 학습·생성 알고리즘을 설계하는 연구를 함께 수행한다.[^p1][^p2][^p3][^p5][^p6][^p8]

## 응용 분야

대표 연구의 대상은 글·이미지·영상·분자를 다루는 생성과 평가, 분산된 참여자의 공동 학습이다. 분자 생성 연구는 분자 역설계의 가능성을 다루며, 신약 탐색과 재료 연구를 응용 방향으로 든다.[^p4][^p5][^p7][^p8] 호흡음 분류에서는 녹음 자료의 일부를 섞는 자료 증강(기존 자료를 변형해 학습용 자료를 늘리는 방법)과 새로운 학습 방법을 제안했다.[^health] 감염병 탐지에서는 뉴스 자료를 그래프(대상과 관계를 점과 선으로 나타낸 구조)로 바꾸고 뉴스 주제를 묶어 관련 정보를 추리는, 판단의 이유를 설명하는 실시간 탐지 방법을 제안했다.[^epidemic]

## 구성원

2026년 11월 9일 People 페이지의 Postdoc Researchers·PhD Students·MS Students·Interns 구획에 있는 38명이다. 카드의 과정과 시작 시기, 연구 주제를 옮겼다. PhD Students 구획 안의 MS/PhD 표기는 석박사통합과정으로 표시했다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Sangmin Bae | 박사후연구원 | Fall 2025– | Adaptive Compute, Multimodal | 3, 8 |
| Sungnyun Kim | 박사후연구원 | Fall 2026– | Multimodal Interaction | 3, 5 |
| Narae Ryu | 박사과정 | Fall 2019– | GNN, Community detection |  |
| Yongsik Lee | 박사과정 | Spring 2020– | RL, LLM | 6 |
| Huzama Ahmad | 박사과정 | Fall 2021– | LLMs, Efficiency, Training Dynamics |  |
| Sanghwa Kim | 박사과정 | Spring 2022– | RL, Theory |  |
| Felix den Breejen | 석박사통합과정 | Spring 2022– | Tabular |  |
| Gahee Kim | 박사과정 | Spring 2023– | GNN |  |
| Junghyun Lee | 박사과정 | Spring 2023– | Theory, RL, LLM | 2 |
| Sehyeok Kang | 박사과정 | Spring 2023– | RL, Multi-Agent RL, LLM | 6 |
| Boryeong Cho | 석박사통합과정 | Fall 2022– | Multimodal, Time-series |  |
| Namgyu Ho | 박사과정 | Fall 2023– | Reasoning, Efficiency, Long-Context |  |
| Jihwan Oh | 박사과정 | Spring 2024– | LLM, RL | 6 |
| Hojung Jung | 박사과정 | Spring 2025– | Diffusion, AI4Science, AI systems | 4, 7 |
| Jaehyun Kwak | 박사과정 | Spring 2025– | Multimodal, Visual Reasoning |  |
| Minsu Kim | 박사과정 | Spring 2025– | LLM, Interpretability, Reasoning |  |
| Minu Kim | 석박사통합과정 | Spring 2024– | LLM Agents, RL | 6 |
| Yujin Kim | 박사과정 | Spring 2025– | Reasoning, Efficiency | 3 |
| Soowon Oh | 박사과정 | Fall 2025– | Efficiency, RL |  |
| Sungwoo Cho | 박사과정 | Spring 2026– | Audio-Visual, Multimodal, CV | 5 |
| Youngrok Park | 박사과정 | Spring 2026– | Generative Models, Stochastic Process | 4, 7 |
| Vinnam Kim | 박사과정 | Fall 2026– | Efficiency |  |
| Woosung (Reiss) Koh | 석박사통합과정 | Fall 2025– | Superintelligence |  |
| Seongbeom Heo | 석사과정 | Spring 2024– | Efficient NLP, Instruction Tuning |  |
| Seo Hyun Kim | 석사과정 | Fall 2024– | NLP, LLM | 4 |
| Hyun Ryu | 석사과정 | Spring 2025– | NLP, Efficient Inference |  |
| Nam Cao | 석사과정 | Spring 2025– | dLLM, Efficient LLM |  |
| Sunwoo Hong | 석사과정 | Spring 2025– | Visual Reasoning, dLLM, WorldModel | 4 |
| Junhyeok Yang | 석사과정 | Fall 2025– |  |  |
| Segyu Lee | 석사과정 | Fall 2025– | Multimodal, Safety |  |
| Changhae Lee | 석사과정 | Spring 2026– | Theory, RL |  |
| Sangmin Hwang | 석사과정 | Spring 2026– | Efficient NLP, Agent, Alignment |  |
| Jaejun Ryu | 석사과정 | Fall 2026– | LLM |  |
| JuHyeong Kim | 석사과정 | Fall 2026– | Diffusion Models, Generative Models |  |
| Sujin Kim | 석사과정 | Fall 2026– | Multi-agent, RL, LLM |  |
| Jungwoo Lee | 인턴 | 2025 | Multimodal |  |
| Jaewan Park | 인턴 | 2026 | RL, LLM |  |
| Minseok Kim | 인턴 | 2026 | RL, LLM |  |

## 졸업생과 이전 참여자

People의 Alumni 34명과 Past Interns 18명이다. 과정과 종료·참여 시기, 진로는 누리집 표기이며 Alumni의 MS/PhD와 Postdoc도 그대로 적었다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Minchan Jeong | MS/PhD (–Fall 2026) | AI Fellow, KIAS |
| Hwankyu Sung | MS (–Fall 2026) |  |
| Euiin Yi | MS (–Fall 2026) |  |
| Murad Aghazada | MS (–Fall 2026) | Research Engineer, ROBROS |
| Seongyoon Kim | MS/PhD (–Spring 2026) |  |
| Andrew Wan Ju Kang | PhD (–Spring 2026) |  |
| Jongwoo Ko | PhD (–Fall 2025) | Senior Researcher, Microsoft |
| Tergel Munkhbat | MS (–Fall 2025) |  |
| Yongjin Yang | MS (–Fall 2025) | PhD Student, Univ. of Toronto |
| Taehyeon Kim | PhD (–Spring 2025) | Research Scientist, LG AI Research |
| Sihyeon Kim | MS (–Spring 2025) | Samsung Research |
| Mingyu Kim | PhD (–Fall 2024) | Postdoc, UBC |
| Gihun Lee | PhD (–Fall 2024) | Research Scientist, Hyperconnect |
| Woojin Chung | MS (–Fall 2024) |  |
| Stephen Cha | MS (–Fall 2024) | Data Scientist, Merck Group |
| Laura Schmid | Postdoc (–Fall 2024) | Chief Editor, Nature Reviews Computing |
| Joonkee Kim | MS (–Spring 2024) | LG AI Research |
| Seongha Eom | MS (–Spring 2024) | Software Engineer, Google |
| Sumyeong Ahn | PhD (–Fall 2023) | Assistant Professor, KENTECH |
| Jung-hun Kim | PhD (–Fall 2023) | Postdoc, CREST/ENSAE Paris |
| SangMook Kim | PhD (–Fall 2023) | Assistant Professor, Chungnam National University |
| Seungjoon Park | MS (–Fall 2023) | Twelve Labs |
| Jaehoon Oh | MS/PhD (–Spring 2023) | Assistant Professor, Pusan National University |
| Donggyu Kim | MS (–Spring 2023) | Medipixel |
| Jaewoo Shin | MS (–Spring 2023) | Minds and Company |
| Nak Yil Kim | MS (–Fall 2022) | Shinhan Bank |
| Jaeyeon Ahn | MS (–Spring 2022) | Amazon |
| Jinhwan Choi | MS (–Spring 2022) | LBox |
| Sangwook Cho | MS (–Spring 2022) | Samsung Electronics |
| Kyeongryeol Go | MS (–Fall 2021) | Superb AI |
| ChangHwan Kim | MS (–Spring 2021) | XCENA |
| JongHyup Kim | MS (–Spring 2021) | Samsung Electronics |
| Hyungjun Yoo | MS (–Fall 2020) | NeuroFusion inc |
| Gauvain Marseille | MS (–Fall 2020) | Neubility |
| Se June Joo | Intern (2022) |  |
| Eric Patarin | Intern (2022) |  |
| Jinsu Park | Intern (2022) |  |
| Seaone Ok | Intern (2022–2023) |  |
| Shinhyeok Hwang | Intern (2023) |  |
| Mohammed Benabbassi | Intern (2023) |  |
| Marc Bartholet | Intern (2023) |  |
| Hyoung Jo Bhang | Intern (2023) |  |
| Kunwoo Na | Intern (2023–2025) |  |
| Toghrul Abbasov | Intern (2023–2024) |  |
| Deokgyu Yoon | Intern (2023–2024) |  |
| Tadiwos Meaza | Intern (2023–2024) |  |
| Eric Kim | Intern (2024) |  |
| Jaewook Jeong | Intern (2024–2025) |  |
| Daehan Yoon | Intern (2024–2025) |  |
| Jaewook Lee | Intern (2024–2025) |  |
| Wonjun Chang | Intern (2025–2026) |  |
| Gilles Massoulié | Intern (2026) |  |

## 최근 5년 논문 목록

연구실 Publications의 2021–2026년 구역에서 윤세영 교수가 저자로 참여한 165개 게시 항목이다. 학술지·학회·워크숍을 포함하며 같은 논문의 서로 다른 발표처 항목도 각각 적었다. 저자·제목·발표처는 연구실 표기이고 별표와 ^는 누리집 표시다. 학회명과 연도는 연구실 기재이며 출판일을 뜻하지 않는다. 연구실 소식이 채택을 알린 NeurIPS 2026 항목은 「채택」으로 표시했다. 날짜가 없는 2021년 항목은 누리집의 연도 구역을 따른다.[^pubs]

**2026**

- Youngrok Park\*, Sangmin Bae\*, Hojung Jung, Jongwoo Ko, Yunseon Choi, Young Jin Kim, Pashmina Cameron, Aaron Courville, Se-Young Yun. "Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation". *NeurIPS 2026 Workshop on Continual Learning in the Era of Foundation Models and Embodied Agents (CL4FMAgents)*.
- Boryeong Cho, Sumyeong Ahn^, Se-Young Yun^. "PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization". *NeurIPS 2026 Workshop on Foundations of LLM Post-Training in Changing Environments (FLLMPT)*.
- Hyun Ryu\*, Jihwan Oh\*, Sumyeong Ahn^, Se-Young Yun^. "Diagnose, Then Select: What Makes Critique-Based Refinement Effective?". *NeurIPS 2026 Workshop on Resource-Aware Agentic AI (RAAAI)*.
- Segyu Lee\*, Boryeong Cho\*, Hojung Jung\*, Seokhyun An, Juhyeong Kim, Jaehyun Kwak, Yongjin Yang, Sangwon Jang, Youngrok Park, Wonjun Chang, Se-Young Yun. "UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models". *NeurIPS 2026 Workshop on Trustworthy AI for Good (AI4GOOD) (Oral)*.
- Hojung Jung\*, Juhyeong Kim\*, Jaehyun Kwak, Boryeong Cho, Junhyeok Yang, Youngrok Park, Sangmin Bae, Se-Young Yun. "DualDrift: Combining Forward and Reverse Drifts for One-Step Generative Modeling". *NeurIPS 2026 (채택)*.
- Hojung Jung, Rodrigo Hormazabal, Jaehyeong Jo, Youngrok Park, Kyunggeun Roh, Se-Young Yun, Sehui Han, Dae-Woong Jeong. "MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models". *NeurIPS 2026 (채택)*.
- Jaehyun Kwak, Nam Cao, Boryeong Cho, Segyu Lee, Sumyeong Ahn^, Se-Young Yun^. "Stage-wise Attention-Guided Region Sequencing for Adversarial Attacks on Large Vision-Language Models". *NeurIPS 2026 (채택)*.
- Junghyun Lee\*, Sanghwa Kim\*, Yassir Jedra, Alexandre Proutière, Se-Young Yun. "Instance-Optimal Estimation with Multiple LLM Judges on a Budget". *NeurIPS 2026 (채택)*.
- Junghyun Lee, Minju Hong, Kwang-Sung Jun, Chulhee Yun, Se-Young Yun. "Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences". *NeurIPS 2026 (채택)*.
- Junghyun Lee, Yujun Kim, Chulhee Yun, Se-Young Yun. "Looking Through the Mirror: Minimax-Optimal Regularized Regrets in Online Learning and Bandits". *NeurIPS 2026 (채택)*.
- Minchan Jeong\*, Jongha Jon Ryu\*, Se-Young Yun, Gregory W. Wornell. "Variational Monte Carlo for Quantum Excited States via Nested Low-Rank Approximation". *NeurIPS 2026 (채택)*.
- Soowon Oh\*, Nam Cao\*, Yujin Kim, Hojung Jung, Huzama Ahmad, Sangmin Bae^, Se-Young Yun^. "BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting". *NeurIPS 2026 (채택)*.
- Youngrok Park\*, Hojung Jung\*, Sangmin Bae, Se-Young Yun. "Temporal Alignment Guidance: On-manifold Sampling in Diffusion Models". *NeurIPS 2026 (채택)*.
- Yujin Kim\*, Namgyu Ho\*, Sangmin Hwang\*, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun^, Hwanjun Song^. "LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL". *NeurIPS 2026 (채택)*.
- Woosung (Reiss) Koh, Jeyoung Jeon, Youngjin Song, Yujin Cheon, Soowon Oh, Jaehyeong Choi, Se-Young Yun. "mSFT: Addressing Dataset Mixtures Overfitting Heterogeneously in Multi-task SFT". *AACL 2026*. DOI: <https://doi.org/10.18653/2026.aacl-short.25>.
- Boryeong Cho, Sumyeong Ahn^, Se-Young Yun^. "PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization". *Findings of EMNLP 2026*. DOI: <https://doi.org/10.18653/2026.findings-emnlp.1899>.
- Seo Hyun Kim\*, Sunwoo Hong\*, Younwoo Choi, Chen-Hao Chao, Se-Young Yun^, Rahul G Krishnan^. "Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models". *EMNLP 2026 (Oral)*. DOI: <https://doi.org/10.18653/2026.emnlp-main.2146>.
- Sehyeok Kang\*, Jaejun Ryu\*, Se-Young Yun. "MELD: Multilingual Ensemble via Logical Debate". *COLM 2026*.
- Seungwon Lim\*, Minu Kim\*, Seokhee Hong, Jinyoung Yeo, Se-Young Yun, Joonkee Kim. "Learning to Comply: Workflow-Grounded Environment Generation for Training Procedurally Compliant Agents". *COLM 2026*.
- Sehyeok Kang\*, Jaewook Jeong\*, Se-Young Yun. "CUDA: Capturing Uncertainty and Diversity in Preference Feedback Augmentation". *Transactions on Machine Learning Research (2026)*.
- Sunwoo Hong\*, Seo Hyun Kim\*, Chen-Hao Chao, Younwoo Choi, Se-Young Yun^, Rahul G Krishnan^. "Logical Equivariance in Diffusion Language Models". *ICML 2026 Workshop on Foundations of Deep Generative Models (FoGen)*.
- Soowon Oh\*, Nam Cao\*, Yujin Kim, Hojung Jung, Huzama Ahmad, Sangmin Bae^, Se-Young Yun^. "BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting". *ICML 2026 Workshop on Resource-Adaptive Foundation Model Inference (AdaptFM)*.
- Sehyeok Kang\*, Jaejun Ryu\*, Se-Young Yun. "MELD: Multilingual Ensemble via Logical Debate". *ACL 2026 Workshop on Multilinguality in the Era of Large Language Models (MeLLM)*.
- Junghyun Lee\*, Sanghwa Kim\*, Yassir Jedra, Alexandre Proutière, Se-Young Yun. "Instance-Optimal Estimation with Multiple LLM Judges on a Budget". *ICML 2026 Workshop on Combining Theory and Benchmarks (CTB) (Best Paper Award in the Long Paper track)*.
- Junghyun Lee, Minju Hong, Kwang-Sung Jun, Chulhee Yun, Se-Young Yun. "Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences". *ICML 2026 Pluralistic Alignment Workshop*.
- Woosung (Reiss) Koh\*, Sungjun Han\*, Segyu Lee, Se-Young Yun, Jay Shin. "Generative Visual Code Mobile World Models". *ICML 2026*.
- Jihwan Oh, Murad Aghazada, Yooju Shin, Se-Young Yun, Taehyeon Kim. "MERIT Feedback Elicits Better Bargaining in LLM Negotiators". *ACL 2026*. DOI: <https://doi.org/10.18653/v1/2026.acl-long.1155>.
- Sungnyun Kim\*, Kangwook Jang\*, Sungwoo Cho, Joon Son Chung, Hoi-Rin Kim, Se-Young Yun. "Two Heads Are Better Than One: Audio-Visual Speech Error Correction with Dual Hypotheses". *Findings of ACL 2026*. DOI: <https://doi.org/10.18653/v1/2026.findings-acl.26>.
- Taehyeon Kim, Hojung Jung, Se-Young Yun. "Multi-Drafter Speculative Decoding with Alignment Feedback". *Findings of ACL 2026*. DOI: <https://doi.org/10.18653/v1/2026.findings-acl.1629>.
- Sehyeok Kang, Jihwan Oh, Se-Young Yun. "Bridging the Gap between Theory of Mind and Action in LLMs". *ICLR 2026 Workshop: "Agents in the Wild: Safety, Security, and Beyond(AIWILD)"*.
- Minsu Kim, Se-Young Yun. "Process-Verified Reinforcement Learning for Theorem Proving via Lean". *ICLR 2026*.
- Woosung (Reiss) Koh, Juyoung Suk, Sungjun Han, Se-Young Yun, Jay Shin. "Predicting LLM Reasoning Performance with Small Proxy Model". *ICLR 2026*.
- Junghyun Lee, Kyoungseok Jang, Kwang-Sung Jun, Milan Vojnovic, Se-Young Yun. "GL-LowPopArt: A Nearly Instance-Wise Minimax-Optimal Estimator for Generalized Low-Rank Trace Regression". *AISTATS 2026*.
- Junghyun Lee, Yassir Jedra, Alexandre Proutière, Se-Young Yun. "Near-Optimal Clustering in Mixture of Markov Chains". *AISTATS 2026*.
- Jihwan Oh\*, Minchan Jeong\*, Jongwoo Ko^, Se-Young Yun^. "From Belief Entrenchment to Robust Reasoning in LLM Agents". *Transactions of the Association for Computational Linguistics (2026)*. DOI: <https://doi.org/10.1162/tacl.a.728>.
- Jihwan Oh\*, Murad Aghazada\*, Se-Young Yun. "Distilling Robustness: Mitigating Persona Sensitivity in Language Models via RLVR Teacher-Student Training". *AAAI 2026 Workshop: "Depolyable AI"*.

**2025**

- Sehyeok Kang, Minu Kim, Jihwan Oh, Se-Young Yun. "Dual Preference Learning for Multi-Agent Reinforcement Learning". *IEEE Access (2025)*. DOI: <https://doi.org/10.1109/access.2025.3645778>.
- Gahee Kim, Seongjin Choi, Se-Young Yun. "A Mutual Information-Based Framework for Enhancing Graph Neural Networks on Heterophily". *IEEE Access (2025)*. DOI: <https://doi.org/10.1109/access.2025.3624415>.
- Sehyeok Kang, Youngjin Ko, Hyeonjun Kim, Myungjoo Kang, Se-Young Yun. "From Vision-Language to Preference: CLIP as a Discriminator". *IROS 2025 Workshop: "Embodied AI and Robotics for Future Scientific Discovery (AIR4S)"*.
- Minsu Kim, Se-Young Yun. "Process-Verified Reinforcement Learning for Theorem Proving via Lean". *NeurIPS 2025 Workshop: Mathematical Reasoning and AI (MATH-AI)*.
- Youngrok Park\*, Hojung Jung\*, Sangmin Bae, Se-Young Yun. "Temporal Alignment Guidance: On-manifold Sampling in Diffusion Models". *NeurIPS 2025 Workshop: Structured Probabilistic Inference & Generative Modeling*.
- Sangmin Bae\*, Yujin Kim\*, Reza Bayat\*, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron Courville, Se-Young Yun. "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation". *NeurIPS 2025*. DOI: <https://doi.org/10.52202/085713-3229>.
- Seo Hyun Kim\*, Sunwoo Hong\*, Hojung Jung, Youngrok Park, Se-Young Yun. "KLASS: KL-Guided Fast Inference in Masked Diffusion Models". *NeurIPS 2025 (Spotlight)*. DOI: <https://doi.org/10.52202/085713-3087>.
- Jongwoo Ko\*, Sungnyun Kim\*, Sungwoo Cho, Se-Young Yun. "Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators". *NeurIPS 2025*. DOI: <https://doi.org/10.52202/085713-3625>.
- Minchan Jeong\*, Jongha Jon Ryu\*, Se-Young Yun, Gregory W. Wornell. "Efficient Parametric SVD of Koopman Operator for Stochastic Dynamical Systems". *NeurIPS 2025*. DOI: <https://doi.org/10.52202/085713-0860>.
- Woosung (Reiss) Koh, Wonbeen Oh, Jaein Jang, MinHyung Lee, Hyeongjin Kim, Ah Yeon Kim, Joonkee Kim, Junghyun Lee, Taehyeon Kim, Se-Young Yun. "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners". *NeurIPS 2025*. DOI: <https://doi.org/10.52202/085713-3061>.
- Jongwoo Ko\*, Sungnyun Kim\*, Sungwoo Cho, Se-Young Yun. "Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators". *ICCV 2025 Workshop: "Knowledge-Intensive Multimodal Reasoning"*.
- Sihyeon Kim, Boryeong Cho, Sangmin Bae, Sumyeong Ahn, Se-Young Yun. "VSCoDe: Visual-Augmentation Selection for Contrastive Decoding". *Transactions on Machine Learning Research (2025)*.
- Yujin Kim\*, Euiin Yi\*, Minu Kim, Se-Young Yun, Taehyeon Kim. "Guiding Reasoning in Small Language Models with LLM Assistance". *COLM 2025 Workshop: "The 1st Workshop on Test-time Scaling and Reasoning Models(SCALR)"*.
- Sungwoo Cho, Jeongsoo Choi, Sungnyun Kim, Se-Young Yun. "MAVFlow: Preserving Paralinguistic Elements with Conditional Flow Matching for Zero-Shot AV2AV Multilingual Translation". *ICCV 2025*. DOI: <https://doi.org/10.1109/iccv51701.2025.01222>.
- Yongjin Yang\*, Euiin Yi\*, Jongwoo Ko, Kimin Lee, Zhijing Jin, Se-Young Yun. "Revisiting Multi-Agent Debate as Test-Time Scaling: A Systematic Study of Conditional Effectiveness". *ICML 2025 Workshop: "Multi-Agent Systems in the Era of Foundation Models: Opportunities, Challenges and Futures(MAS)"*.
- Sangmin Bae\*, Yujin Kim\*, Reza Bayat\*, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron Courville, Se-Young Yun. "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation". *ICML 2025 Workshop: "ES-FoMo III: 3rd Workshop on Efficient Systems for Foundation Models"*.
- Sehyeok Kang\*, Jaewook Jeong\*, Se-Young Yun. "CUDA: Capturing Uncertainty and Diversity in Preference Feedback Augmentation". *ICML 2025 Workshop : "Models of Human Feedback for AI Alignment(MOFA)" (Oral)*.
- Tergel Munkhbat\*, Namgyu Ho\*, Seo Hyun Kim\*, Yongjin Yang, Yujin Kim, Se-Young Yun. "Self-Training Elicits Concise Reasoning in Large Language Models". *Findings of ACL 2025*. DOI: <https://doi.org/10.18653/v1/2025.findings-acl.1289>.
- Jongwoo Ko, Tianyi Chen, Sungnyun Kim, Tianyu Ding, Luming Liang, Ilya Zharkov, Se-Young Yun. "DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs". *ICML 2025 (Oral)*.
- Jaehyun Kwak, Ramahdani Muhammad Izaaz Inhar, Se-Young Yun, Sung-Ju Lee. "QuRe: Query-Relevant Retrieval through Hard Negative Sampling in Composed Image Retrieval". *ICML 2025*.
- Kaito Ariu, Alexandre Proutière, Se-Young Yun. "Revisiting Instance-Optimal Cluster Recovery in the Labeled Stochastic Block Model". *ICML 2025*.
- Sungnyun Kim, Kangwook Jang, Sangmin Bae, Sungwoo Cho, Se-Young Yun. "MoHAVE: Mixture of Hierarchical Audio-Visual Experts for Robust Speech Recognition". *ICML 2025*.
- Kunwoo Na, Junghyun Lee, Se-Young Yun, Sungbin Lim. "Probability-Flow ODE in Infinite-Dimensional Function Spaces". *ICLR Workshop: "Deep Generative Model in Machine Learning: Theory, Principle and Efficacy (DeLTa)" 2025*.
- Jihwan Oh, Minchan Jeong, Jongwoo Ko, Se-Young Yun. "When Debate Fails: Bias Reinforcement in Large Language Models". *ICLR Workshop: "LLM Reason and Plan" 2025*.
- Seongyoon Kim, Minchan Jeong, Sungnyun Kim, Sungwoo Cho, Sumyeong Ahn\*, Se-Young Yun\*. "FedDr+: Stabilizing Dot-regression with Global Feature Distillation for Federated Learning". *Transactions on Machine Learning Research (2025)*.
- Sehyeok Kang\*, Yongsik Lee\*, Gahee Kim, Song Chong, Se-Young Yun. "MA2E: Addressing Partial Observability in Multi-Agent Reinforcement Learning with Masked Auto-Encoder". *ICLR 2025*.
- Sungnyun Kim, Sungwoo Cho, Sangmin Bae, Kangwook Jang, Se-Young Yun. "Multi-Task Corrupted Prediction for Learning Robust Audio-Visual Speech Representation". *ICLR 2025*.
- Woosung Koh\*, Jang Han Yoon\*, MinHyung Lee, Youngjin Song, Jaegwan Cho, Jaehyun Kang, Taehyeon Kim, Se-Young Yun, Youngjae Yu, Bongshin Lee. "C^2: Scalable Auto-Feedback for LLM-based Chart Generation". *NAACL 2025 (Oral)*. DOI: <https://doi.org/10.18653/v1/2025.naacl-long.232>.
- Woosung Koh, Wonbeen Oh, Siyeol Kim, Suhin Shin, Hyeongjin Kim, Jaein Jang, Junghyun Lee, Se-Young Yun. "FlickerFusion: Intra-trajectory Domain Generalizing Multi-agent Reinforcement Learning". *ICLR 2025*.
- Yongjin Yang\*, Sihyeon Kim\*, Hojung Jung, Sangmin Bae, SangMook Kim, Se-Young Yun, Kimin Lee. "Automated Filtering of Human Feedback Data for Aligning Text-to-Image Diffusion Models". *ICLR 2025*.

**2024**

- Taehyeon Kim, Donggyu Kim, Se-Young Yun. "FLR: Label-Mixture Regularization for Federated Learning with Noisy Labels". *Transactions on Machine Learning Research (2024)*.
- Woosung Koh, Wonbeen Oh, Siyeol Kim, Suhin Shin, Hyeongjin Kim, Jaein Jang, Junghyun Lee, Se-Young Yun. "FlickerFusion: Intra-trajectory Domain Generalizing Multi-agent Reinforcement Learning". *NeurIPS Workshop: "Open-World Agents (OWA)" 2024*.
- Taehyeon Kim\*, Hojung Jung\*, Se-Young Yun. "A Unified Framework for Speculative Decoding with Multiple Drafters as a Bandit". *NeurIPS Workshop: "Efficient Natural Language and Speech Processing (ENLSP-IV)" 2024*.
- Hojung Jung\*, Youngrok Park\*, Laura Schmid, Jaehyeong Jo, Dongkyu Lee, Bongsang Kim, Se-Young Yun, Jinwoo Shin. "Conditional Synthesis of 3D Molecules with Time Correction Sampler". *NeurIPS 2024*. DOI: <https://doi.org/10.52202/079017-2417>.
- Jung-hun Kim, Milan Vojnovic, Se-Young Yun. "An Adaptive Approach for Infinitely Many-armed Bandits under Generalized Rotting Constraints". *NeurIPS 2024*. DOI: <https://doi.org/10.52202/079017-0281>.
- Junghyun Lee, Se-Young Yun, Kwang-Sung Jun. "A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits". *NeurIPS 2024*. DOI: <https://doi.org/10.52202/079017-3960>.
- Minu Kim\*, Yongsik Lee\*, Sehyeok Kang, Jihwan Oh, Song Chong, Se-Young Yun. "Preference Alignment with Flow Matching". *NeurIPS 2024*. DOI: <https://doi.org/10.52202/079017-1108>.
- Namgyu Ho\*, Sangmin Bae\*, Taehyeon Kim, Hyunjik Jo, Yireun Kim, Tal Schuster, Adam Fisch, James Thorne, Se-Young Yun. "Block Transformer: Global-to-Local Language Modeling for Fast Inference". *NeurIPS 2024*.
- Euiin Yi\*, Taehyeon Kim\*, Hongseok Jeung, Du-Seong Chang, Se-Young Yun. "Towards Fast Multilingual LLM Inference: Speculative Decoding and Specialized Drafters". *EMNLP 2024*. DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.602>.
- Gihun Lee, Minchan Jeong, Yujin Kim, Hojung Jung, Jaehoon Oh, Sangmook Kim, Se-Young Yun. "BAPO: Base-Anchored Preference Optimization for Personalized Alignment in Large Language Models". *Findings of EMNLP 2024*.
- Woojin Chung, Jiwoo Hong, Na Min An, James Thorne, Se-Young Yun. "Stable Language Model Pre-training by Reducing Embedding Variability". *EMNLP 2024*. DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.606>.
- Yongjin Yang\*, Jongwoo Ko\*, Se-Young Yun. "Towards Difficulty-Agnostic Efficient Transfer Learning for Vision-Language Models". *EMNLP 2024*. DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.124>.
- Seonghyun Park\*, Narae Ryu\*, Gahee Kim, Dongyeop Woo, Se-Young Yun, Sungsoo Ahn. "Non-backtracking Graph Neural Networks". *Transactions on Machine Learning Research (2024)*.
- Sungnyun Kim\*, Kangwook Jang\*, Sangmin Bae, Hoirin Kim, Se-Young Yun. "Learning Video Temporal Dynamics with Cross-Modal Attention for Robust Audio-Visual Speech Recognition". *SLT 2024*. DOI: <https://doi.org/10.1109/slt61566.2024.10832305>.
- Jihwan Oh, Sungnyun Kim, Gahee Kim, SeongHwan Kim, Se-Young Yun. "Diffusion-based Episodes Augmentation for Offline Multi-Agent Reinforcement Learning". *ICML Workshop: "Structured Probabilistic Inference & Generative Modeling (SPIGM)" 2024*.
- Seongyoon Kim, Minchan Jeong, Sungnyun Kim, Sungwoo Cho, Sumyeong Ahn\*, Se-Young Yun\*. "FedDr+: Stabilizing Dot-regression with Global Feature Distillation for Federated Learning". *KDD Workshop: "International Joint Workshop on Federated Learning for Data Mining and Graph Analytics (FedKDD)" 2024*.
- Junghyun Lee, Se-Young Yun, Kwang-Sung Jun. "A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits". *ICML Workshop: "Aligning Reinforcement Learning Experimentalists and Theorists (ARLET)" 2024 (Oral)*.
- Sihyeon Kim\*, Boryeong Cho\*, Sangmin Bae, Sumyeong Ahn^, Se-Young Yun^. "VACoDe: Visual Augmented Contrastive Decoding". *ICML Workshop: "Trustworthy Multi-modal Foundation Models and AI Agents (TiFA)" 2024*.
- Sehyeok Kang, Yongsik Lee, Se-Young Yun. "DPM: Dual Preferences-based Multi-Agent Reinforcement Learning". *ICML Workshop: "Models of Human Feedback for AI Alignment (MFHAIA)" 2024*.
- Jongwoo Ko, Sungnyun Kim, Tianyi Chen, Se-Young Yun. "DistiLLM: Towards Streamlined Distillation for Large Language Models". *ICML 2024*.
- Mingyu Kim, Jun-Seong Kim, Se-Young Yun, Jin-Hwa Kim. "Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs". *ICML 2024*.
- Sumyeong Ahn, Sihyeon Kim, Jongwoo Ko, Se-Young Yun. "Fine-tuning Pre-trained Models for Robustness Under Noisy Labels". *IJCAI 2024*. DOI: <https://doi.org/10.24963/ijcai.2024/403>.
- Sehyeok Kang, Yongsik Lee, Gahee Kim, Song Chong, Se-Young Yun. "MA2E: Implicit Communication Through Masked Auto-Encoder in Multi-Agent Reinforcement Learning". *ICLR GenAI4DM Workshop 2024*.
- Yujin Kim, Jaehong Yoon, Seonghyeon Ye, Sangmin Bae, Namgyu Ho, Sung Ju Hwang, Se-Young Yun. "Carpe diem: On the Evaluation of World Knowledge in Lifelong Language Models". *NAACL 2024*. DOI: <https://doi.org/10.18653/v1/2024.naacl-long.302>.
- Kaito Ariu, Jungseul Ok, Alexandre Proutière, Se-Young Yun. "Optimal Clustering from Noisy Binary Feedback". *Machine Learning (2024)*. DOI: <https://doi.org/10.1007/s10994-024-06532-z>.
- Gihun Lee, Minchan Jeong, Sangmook Kim, Jaehoon Oh, Se-Young Yun. "FedSOL: Stabilized Orthogonal Learning in Federated Learning". *CVPR 2024*.
- Junghyun Lee, Se-Young Yun, Kwang-Sung Jun. "Improved Regret Bounds of (Multinomial) Logistic Bandits via Regret-to-Confidence-Set Conversion". *AISTATS 2024*.
- Taehyeon Kim\*, Joonkee Kim\*, Gihun Lee\*, Se-Young Yun. "Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions". *ICLR 2024 (Spotlight)*.
- Yongjin Yang, Taehyeon Kim, Se-Young Yun. "Leveraging Normalization Layer in Adapters With Progressive Learning and Adaptive Distillation for Cross-Domain Few-Shot Learning". *AAAI 2024*. DOI: <https://doi.org/10.1609/aaai.v38i15.29573>.

**2023**

- Felix den Breejen, Sangmin Bae, Stephen Cha, Tae-Young Kim, Seoung-Hyun Koh, Se-Young Yun. "Exploring the Retrieval Mechanism for Tabular Deep Learning". *NeurIPS Workshop: "Table Representation Learning" 2023*.
- Gihun Lee, Minchan Jeong, SangMook Kim, Jaehoon Oh, Se-Young Yun. "FedSoL: Bridging Global Alignment and Local Generality in Federated Learning". *NeurIPS Workshop: "Federated Learning in the Age of Foundation Models" 2023*.
- Junghyun Lee, Laura Schmid, Se-Young Yun. "Flooding with Absorption: An Efficient Protocol for Heterogeneous Bandits over Complex Networks". *OPODIS 2023 (Best Student Paper Award)*.
- Kangwook Jang\*, Sungnyun Kim\*, Se-Young Yun, Hoirin Kim. "Recycle-and-Distill: Universal Compression Strategy for Transformer-based Speech SSL Models with Attention Map Reusing and Masking Distillation". *NeurIPS Workshop: "Self-Supervised Learning - Theory and Practice" 2023*.
- Mingyu Kim, Jun-Seong Kim, Se-Young Yun, Jin-Hwa Kim. "Refined Tensorial Radiance Field: Harnessing Coordinate-Based Networks for Novel View Synthesis from Sparse Inputs". *NeurIPS Workshop: "Deep Learning and Inverse Problems" 2023*.
- Seonghyun Park\*, Narae Ryu\*, Gahee Kim, Dongyeop Woo, Se-Young Yun, Sungsoo Ahn. "Non-backtracking Graph Neural Networks". *NeurIPS Workshop: "New Frontiers in Graph Learning" 2023 (Oral)*.
- Seongjin Choi\*, Gahee Kim\*, Se-Young Yun. "Node Mutual Information: Enhancing Graph Neural Networks for Heterophily". *NeurIPS Workshop: "New Frontiers in Graph Learning" 2023*.
- Seongyoon Kim, Gihun Lee, Jaehoon Oh^, Se-Young Yun^. "FedFN: Feature Normalization for Alleviating Data Heterogeneity Problem in Federated Learning". *NeurIPS Workshop: "Federated Learning in the Age of Foundation Models" 2023*.
- Taehyeon Kim\*, Joonkee Kim\*, Gihun Lee\*, Se-Young Yun. "Distort, Distract, Decode: Instruction-Tuned Model Can Refine its Response from Noisy Instructions". *NeurIPS Workshop: "Instruction Tuning and Instruction Following" 2023*.
- Woojin Chung, Hyowon Cho, James Thorne, Se-Young Yun. "Parameter-Averaging Laws for Multitask Language Models". *NeurIPS Workshop: "Federated Learning in the Age of Foundation Models" 2023*.
- Yujin Kim, Jaehong Yoon, Seonghyeon Ye, Sung Ju Hwang, Se-Young Yun. "Carpe Diem: On the Evaluation of World Knowledge in Lifelong Language Models". *NeurIPS Workshop: "SyntheticData4ML" 2023 (Oral)*.
- Haeju Lee\*, Minchan Jeong\*, Se-Young Yun, Kee-Eung Kim. "Bayesian Multi-Task Transfer Learning for Soft Prompt Tuning". *Findings of EMNLP 2023*. DOI: <https://doi.org/10.18653/v1/2023.findings-emnlp.329>.
- Jongwoo Ko\*, Seungjoon Park\*, Yujin Kim, Sumyeong Ahn, Du-Seong Chang, Euijai Ahn, Se-Young Yun. "NASH: A Simple Unified Framework of Structured Pruning for Accelerating Encoder-Decoder Language Models". *Findings of EMNLP 2023*. DOI: <https://doi.org/10.18653/v1/2023.findings-emnlp.404>.
- Sangmin Bae\*, Jongwoo Ko\*, Hwanjun Song, Se-Young Yun. "Fast and Robust Early-Exiting Framework for Autoregressive Language Models with Synchronized Parallel Decoding". *EMNLP 2023*. DOI: <https://doi.org/10.18653/v1/2023.emnlp-main.362>.
- Yongjin Yang\*, Joonkee Kim\*, Yujin Kim\*, Namgyu Ho, James Thorne, Se-Young Yun. "HARE: Explainable Hate Speech Detection with Step-by-Step Reasoning". *Findings of EMNLP 2023*. DOI: <https://doi.org/10.18653/v1/2023.findings-emnlp.365>.
- Hojoon Lee\*, Hanseul Cho\*, Hyunseung Kim\*, Daehoon Gwak, Joonkee Kim, Jaegul Choo, Se-Young Yun, Chulhee Yun. "PLASTIC: Improving Input and Label Plasticity for Sample Efficient Reinforcement Learning". *NeurIPS 2023*.
- Junghyun Lee\*, Hanseul Cho\*, Se-Young Yun, Chulhee Yun. "Fair Streaming Principal Component Analysis: Statistical and Algorithmic Viewpoint". *NeurIPS 2023*.
- Kaito Ariu, Se-Young Yun, Alexandre Proutière. "An Optimal Clustering Algorithm for the Labeled Stochastic Block Model". *ICML Workshop: "Sampling and Optimization in Discrete Space" 2023*.
- Kangwook Jang\*, Sungnyun Kim\*, Se-Young Yun, Hoirin Kim. "Recycle-and-Distill: Universal Compression Strategy for Transformer-based Speech SSL Models with Attention Map Reusing and Masking Distillation". *INTERSPEECH 2023*. DOI: <https://doi.org/10.21437/interspeech.2023-1329>.
- Sangmin Bae\*, June-Woo Kim\*, Wonyang Cho, Hyerim Baek, Soyoun Son, Byungjo Lee, Changwan Ha, Kyungpil Tae, Sungnyun Kim, Se-Young Yun. "Patch-Mix Contrastive Learning with Audio Spectrogram Transformer on Respiratory Sound Classification". *INTERSPEECH 2023*. DOI: <https://doi.org/10.21437/interspeech.2023-1426>.
- Namgyu Ho, Laura Schmid, Se-Young Yun. "Large Language Models Are Reasoning Teachers". *ACL 2023*. DOI: <https://doi.org/10.18653/v1/2023.acl-long.830>.
- Mingyu Kim\*, Jihwan Oh\*, Yongsik Lee, Joonkee Kim, SeongHwan Kim, Song Chong, Se-Young Yun. "The StarCraft Multi-Agent Exploration Challenges: Learning Multi-Stage Tasks and Environmental Factors without Precise Reward Functions". *IEEE Access (2023)*. DOI: <https://doi.org/10.1109/access.2023.3266652>.
- Jongwoo Ko\*, Sumyeong Ahn\*, Se-Young Yun. "Efficient Utilization of Pre-trained Model for Learning with Noisy Labels". *ICLR Workshop: "Pitfalls of Limited Data and Computation for Trustworthy ML" 2023 (Oral)*.
- SangMook Kim\*, Sangmin Bae\*, Hwanjun Song, Se-Young Yun. "Re-thinking Federated Active Learning based on Inter-class Diversity". *CVPR 2023*. DOI: <https://doi.org/10.1109/cvpr52729.2023.00384>.
- Sungnyun Kim\*, Sangmin Bae\*, Se-Young Yun. "Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning". *CVPR 2023*. DOI: <https://doi.org/10.1109/cvpr52729.2023.00728>.
- Sungnyun Kim\*, Sangmin Bae\*, Se-Young Yun. "Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning". *CVPR Workshop: "Fine-Grained Visual Categorization" 2023 (Invited)*.
- Jongwoo Ko, Seungjoon Park, Minchan Jeong, Suk-Jin Hong, Euijai Ahn, Du-Seong Chang, Se-Young Yun. "Revisiting Intermediate Layer Distillation for Compressing Language Models: An Overfitting Perspective". *Findings of EACL 2023*. DOI: <https://doi.org/10.18653/v1/2023.findings-eacl.12>.
- Sumyeong Ahn\*, Jongwoo Ko\*, Se-Young Yun. "CUDA: Curriculum of Data Augmentation for Long-tailed Recognition". *ICLR 2023 (Spotlight, notable-top-25%)*.
- Sumyeong Ahn\*, Seongyoon Kim\*, Se-Young Yun. "Mitigating Dataset Bias by Using Per-Sample Gradient". *ICLR 2023*.
- Jung-hun Kim, Se-Young Yun, Minchan Jeong, Junhyun Nam, Jinwoo Shin, Richard Combes. "Contextual Linear Bandits under Noisy Features: Towards Bayesian Oracles". *AISTATS 2023*.
- Yassir Jedra\*, Junghyun Lee\*, Alexandre Proutière, Se-Young Yun. "Nearly Optimal Latent State Decoding in Block MDPs". *AISTATS 2023*.
- Jihwan Oh\*, Joonkee Kim\*, Minchan Jeong, Se-Young Yun. "Toward Risk-based Optimistic Exploration for Cooperative Multi-Agent Reinforcement Learning". *AAMAS 2023*. DOI: <https://doi.org/10.65109/pwex1553>.
- Jongwoo Ko\*, Bongsoo Yi\*, Se-Young Yun. "A Gift from Label Smoothing: Robust Training with Adaptive Label Smoothing via Auxiliary Classifier under Label Noise". *AAAI 2023*. DOI: <https://doi.org/10.1609/aaai.v37i7.26004>.
- Sangmin Bae\*, Sungnyun Kim\*, Jongwoo Ko, Gihun Lee, Seungjong Noh, Se-Young Yun. "Self-Contrastive Learning: Single-viewed Supervised Contrastive Framework using Sub-network". *AAAI 2023 (Oral)*. DOI: <https://doi.org/10.1609/aaai.v37i1.25091>.
- Sumyeong Ahn, Se-Young Yun. "Denoising After Entropy-based Debiasing A Robust Training Method for Dataset Bias with Noisy Labels". *AAAI 2023 (Oral)*. DOI: <https://doi.org/10.1609/aaai.v37i1.25088>.

**2022**

- KyeongRyeol Go, Mingyu Kim, Se-Young Yun. "Meta-learning Amidst Heterogeneity and Ambiguity". *IEEE Access (2022)*. DOI: <https://doi.org/10.1109/access.2022.3228829>.
- Jaehoon Oh\*, Jongwoo Ko\*, Se-Young Yun. "Synergy with Translation Artifacts for Training and Inference in Multilingual Tasks". *EMNLP 2022*. DOI: <https://doi.org/10.18653/v1/2022.emnlp-main.452>.
- Daniel Bienstock\*, Minchan Jeong\*, Apurv Shukla\*, Se-Young Yun\*. "Robust Streaming PCA". *NeurIPS 2022*. DOI: <https://doi.org/10.52202/068431-0306>.
- Gihun Lee\*, Minchan Jeong\*, Yongjin Shin, Sangmin Bae, Se-Young Yun. "Preservation of the Global Knowledge by Not-True Distillation in Federated Learning". *NeurIPS 2022*. DOI: <https://doi.org/10.52202/068431-2787>.
- Jaehoon Oh\*, Sungnyun Kim\*, Namgyu Ho\*, Jin-Hwa Kim, Hwanjun Song, Se-Young Yun. "Understanding Cross-Domain Few-Shot Learning Based on Domain Similarity and Few-Shot Difficulty". *NeurIPS 2022*. DOI: <https://doi.org/10.52202/068431-0190>.
- Jaewoo Shin, Taehyeon Kim, Se-Young Yun. "Revisiting the Activation Function for Federated Image Classification". *NeurIPS Workshop: "Federated Learning: Recent Advances and New Challenges" 2022*.
- Seongha Eom, Taehyeon Kim, Se-Young Yun. "Layover Intermediate Layer for Multi-Label Classification in Efficient Transfer Learning". *NeurIPS Workshop: "Has it Trained Yet? A Workshop for Algorithmic Efficiency in Practical Neural Network Training" 2022*.
- Sumyeong Ahn\*, Jongwoo Ko\*, Se-Young Yun. "CUDA: Curriculum of Data Augmentation for Long-tailed Recognition". *NeurIPS Workshop: "Machine Learning Safety" 2022*.
- Sumyeong Ahn\*, Jongwoo Ko\*, Se-Young Yun. "CUDA: Curriculum of Data Augmentation for Long-tailed Recognition". *NeurIPS Workshop: "Distribution Shifts: Connecting Methods and Applications" 2022*.
- Sumyeong Ahn\*, Seongyoon Kim\*, Se-Young Yun. "Mitigating Dataset Bias by Using Per-Sample Gradient". *NeurIPS Workshop: "Machine Learning Safety" 2022*.
- Sumyeong Ahn\*, Seongyoon Kim\*, Se-Young Yun. "Mitigating Dataset Bias by Using Per-Sample Gradient". *NeurIPS Workshop: "Distribution Shifts: Connecting Methods and Applications" 2022*.
- Sungnyun Kim\*, Sangmin Bae\*, Se-Young Yun. "Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning". *NeurIPS Workshop: "Self-Supervised Learning - Theory and Practice" 2022*.
- Jaehoon Oh\*, Sungnyun Kim\*, Namgyu Ho\*, Jin-Hwa Kim, Hwanjun Song, Se-Young Yun. "ReFine: Re-randomization before Fine-tuning for Cross-domain Few-shot Learning". *CIKM 2022 (Short)*. DOI: <https://doi.org/10.1145/3511808.3557681>.
- Sangmook Kim, Wonyoung Shin, Soohyuk Jang, Hwanjun Song, Se-Young Yun. "FedRN: Exploiting k-Reliable Neighbors Towards Robust Federated Learning". *CIKM 2022 (Long)*.
- Doosun Hong\*, Jaehoon Oh\*, Kihoon Bang, Soonho Kwon, Se-Young Yun, Hyuck Mo Lee. "Interpretable Deep Learning Model for Analyzing the Relationship between the Electronic Structure and Chemisorption Property". *The Journal of Physical Chemistry Letters (2022)*. DOI: <https://doi.org/10.1021/acs.jpclett.2c02293>.
- Milan Vojnovic, Se-Young Yun, Kaifang Zhou. "Accelerated MM Algorithms for Ranking Scores Inference from Comparison Data". *Operations Research (2022)*.
- Dabeen Lee, Milan Vojnovic, Se-Young Yun. "Test Score Algorithms for Budgeted Stochastic Utility Maximization". *INFORMS Journal of Optimization (2022)*. DOI: <https://doi.org/10.1287/ijoo.2022.0075>.
- Jaehoon Oh\*, Sungnyun Kim\*, Namgyu Ho\*, Jin-Hwa Kim, Hwanjun Song, Se-Young Yun. "ReFine: Re-randomization before Fine-tuning for Cross-domain Few-shot Learning". *ICML Workshop: "Updatable Machine Learning" 2022*.
- Mingyu Kim\*, Jihwan Oh\*, Yongsik Lee, Joonkee Kim, SeongHwan Kim, Song Chong, Se-Young Yun. "The StarCraft Multi-Agent Challenges+ : Learning of Multi-Stage Tasks and Environmental Factors without Precise Reward Functions". *ICML Workshop : "AI for Agent Based Modeling" 2022 (Spotlight)*.
- SangMook Kim\*, Sangmin Bae\*, Hwanjun Song, Se-Young Yun. "LG-FAL : Federated Active Learning Strategy using Local and Global Models". *ICML Workshop: "Adaptive Experimental Design and Active Learning in the Real World" 2022*.
- Taehyeon Kim, Se-Young Yun. "Supernet Training for Federated Image Classification under System Heterogeneity". *ICML Workshop: "Dynamic Neural Networks" 2022 (Oral)*.
- Yujin Kim\*, Jaehoon Oh\*, Sungnyun Kim, Se-Young Yun. "Revisiting the Updates of a Pre-trained Model for Few-shot Learning". *ICML Workshop: "Updatable Machine Learning" 2022 (Oral)*.
- Taehyeon Kim, Heesoo Myeong, Se-Young Yun. "Revisiting Architecture-aware Knowledge Distillation: Smaller Models and Faster Search". *ICML Workshop: "Hardware Aware Efficient Training (HAET)” 2022*.
- Sungnyun Kim\*, Jaewoo Shin\*, Seongha Eom, Jihwan Oh, Se-Young Yun. "Real-time and Explainable Detection of Epidemics with Global News Data". *ICML Workshop: "Healthcare AI and COVID-19" 2022*.
- Jihwan Oh, Joonkee Kim, Se-Young Yun. "Risk Perspective Exploration in Distributional Reinforcement Learning". *ICML Workshop: "AI for Agent Based Modeling" 2022*.
- Jung-hun Kim, Milan Vojnovic, Se-Young Yun. "Rotting Infinitely Many-Armed Bandits". *ICML 2022 (Spotlight)*.
- Taehyeon Kim, Se-Young Yun. "Revisiting Orthogonality Regularization: A Study for Convolutional Neural Networks in Image Classification". *IEEE Access (2022)*. DOI: <https://doi.org/10.1109/access.2022.3185621>.
- Sungnyun Kim, Se-Young Yun. "Calibration of Few-Shot Classification Tasks: Mitigating Misconfidence From Distribution Mismatch". *IEEE Access (2022)*. DOI: <https://doi.org/10.1109/access.2022.3176090>.
- Jongwoo Ko, Bongsoo Yi, Se-Young Yun. "ALASCA: Rethinking Label Smoothing for Deep Learning Under Label Noise". *ICML Workshop: “Principle of Distribution Shift (PODS)” 2022*.
- Jaehoon Oh\*, SangMook Kim\*, Se-Young Yun. "FedBABU: Towards Enhanced Representation for Federated Image Classification". *ICLR 2022*.
- Mingyu Kim, Kyeongryeol Go, Se-Young Yun. "Neural Processes with Stochastic Attention: Paying more attention to the context dataset". *ICLR 2022*.

**2021**

- Taehyeon Kim\*, Jongwoo Ko\*, Sangwook Cho, Jinhwan Choi, Se-Young Yun. "FINE Samples for Learning with Noisy Labels". *NeurIPS 2021*.
- Jaehoon Oh, SangMook Kim, Se-Young Yun. "FedBABU: Towards Enhanced Representation for Federated Image Classification". *NeurIPS Workshop: "New Frontiers in Federated Learning: Privacy, Fairness, Robustness, Personalization and Data Ownership" 2021*.
- Mingyu Kim, Kyeongryeol Go, Se-Young Yun. "Neural Processes with Stochastic Attention: Paying more attention to the context dataset". *NeurIPS Workshop: "5th Workshop on Meta-Learning" 2021*.
- Jin-woo Lee, Jaehoon Oh, Sungsu Lim, Se-Young Yun, Jae-Gil Lee. "TornadoAggregate: Accurate and Scalable Federated Learning via the Ring-based Architecture". *AAAI Workshop: "Toward Robust, Secure and Efficient Machine Learning" 2021*.

## 수상과 선정

연구실 소식·논문 목록과 교수 이력에 게시된 2021년 11월–2026년 7월의 수상·선정 14건이다. 연도만 적힌 두 항목의 연도는 누리집의 연도 표기이고 날짜는 게시되어 있지 않다. 각 상의 등급은 게시 표기대로 적었다.[^news][^pubs][^prof][^home]

- 2026-07-31 · 한국인공지능학회 CKAIA 2026 Distinguished Paper Award(우수논문상): Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences
- 2026-07-31 · 한국인공지능학회 CKAIA 2026 Distinguished Paper Award(우수논문상): Looking Through the Mirror: Minimax-Optimal Regularized Regrets in Online Learning and Bandits
- 2026-07-10 · ICML 2026 CTB Workshop Best Paper(Long Paper Track): Instance-Optimal Estimation with Multiple LLM Judges on a Budget
- 2025-11 · 한국인공지능학회 KAIA 2025 AI Frontier Challenge 1위. 팀: Sungnyun Kim, Sungwoo Cho. 과제: 극심한 소음 환경의 음성 대화 개선
- 2024-12 · QIFK 2024 Winner 선정: DistiLLM: Towards Streamlined Distillation for Large Language Models
- 2024-07 · 한국인공지능학회 CKAIA 2024 Best Paper: A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits
- 2024-04 · ICASSP 2024 Best Student Paper: STaR: Distilling Speech Temporal Relation for Lightweight Speech Self-Supervised Learning Models
- 2023-11 · OPODIS 2023 Best Student Paper: Flooding with Absorption: An Efficient Protocol for Heterogeneous Bandits over Complex Networks
- 2022-12 · NeurIPS 2022 Cell Segmentation Challenge 1위. 팀: Gihun Lee, Sangmook Kim, Joonkee Kim. MEDIAR: Harmony of Data-Centric and Model-Centric for Multi-Modality Microscopy
- 2022-07 · 한국인공지능학회 CKAIA 2022 Best Paper: Near-Optimal Clustering in Block MDPs with Implications on Reward-Free RL
- 2021-11 · 한국인공지능학회 JKAIA 2021 Best Paper: MMD-based Fair PCA via Manifold Optimization
- 2021-11 · 한국인공지능학회 JKAIA 2021 Honorable Mention(입선): Self-Contrastive Learning
- 2025 · ICORES 2025 Best Student Paper Award: Hierarchical Decomposition Framework for Steiner Tree Packing Problem
- 2024 · 윤세영 교수 KIISE/IEEE-CS Young Computer Researcher Award

## 소식

연구실 소식의 2022년 11월–2026년 9월 학술 발표 채택 소식 31건이다. 날짜는 소식의 연월 표기다. 아래 논문들은 해당 소식에서 「채택」을 알린 항목이다.[^news]

- 2026-09 · NeurIPS 2026 채택: DualDrift: Combining Forward and Reverse Drifts for One-Step Generative Modeling; MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models; Stage-wise Attention-Guided Region Sequencing for Adversarial Attacks on Large Vision-Language Models; Instance-Optimal Estimation with Multiple LLM Judges on a Budget; Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences; Looking Through the Mirror: Minimax-Optimal Regularized Regrets in Online Learning and Bandits; Variational Monte Carlo for Quantum Excited States via Nested Low-Rank Approximation; BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting; Temporal Alignment Guidance: On-manifold Sampling in Diffusion Models; LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- 2026-05 · ICML 채택: Generative Visual Code Mobile World Models
- 2026-04 · ACL 2026 채택: MERIT Feedback Elicits Better Bargaining in LLM Negotiators; Two Heads Are Better Than One: Audio-Visual Speech Error Correction with Dual Hypotheses
- 2026-01 · ICLR 2026 채택: Process-Verified Reinforcement Learning for Theorem Proving via Lean; Predicting LLM Reasoning Performance with Small Proxy Model
- 2026-01 · AISTATS 2026 채택: Near-Optimal Clustering in Mixture of Markov Chains; GL-LowPopArt: A Nearly Instance-Wise Minimax-Optimal Estimator for Generalized Low-Rank Trace Regression
- 2025-09 · NeurIPS 2025 채택: KLASS: KL-Adaptive Stability Sampling for Fast Inference in Masked Diffusion Models; AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners; Efficient Parametric SVD of Koopman Operator for Stochastic Dynamical Systems; Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators; Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation
- 2025-06 · ICCV 2025 채택: MAVFlow: Preserving Paralinguistic Elements with Conditional Flow Matching for Zero-Shot AV2AV Multilingual Translation
- 2025-05 · ICML 2025 채택: DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs; QuRe: Query-Relevant Retrieval through Hard Negative Sampling in Composed Image Retrieval; Revisiting Instance-Optimal Cluster Recovery in the Labeled Stochastic Block Model; MoHAVE: Mixture of Hierarchical Audio-Visual Experts for Robust Speech Recognition
- 2025-01 · ICLR 2025 채택: Automated Filtering of Human Feedback Data for Aligning Text-to-Image Diffusion Models; FlickerFusion: Intra-trajectory Domain Generalizing Multi-agent Reinforcement Learning; Multi-Task Corrupted Prediction for Learning Robust Audio-Visual Speech Representation; MA2E: Addressing Partial Observability in Multi-Agent Reinforcement Learning with Masked Auto-Encoder; When Debate Fails: Bias Reinforcement in Large Language Models; Probability-Flow ODE in Infinite-Dimensional Function Spaces
- 2025-01 · NAACL 2025 채택: C^2: Scalable Auto-Feedback for LLM-based Chart Generation
- 2024-10 · TMLR 채택: FLR: Label-Mixture Regularization for Federated Learning with Noisy Labels
- 2024-09 · NeurIPS 2024 채택: Conditional Synthesis of 3D Molecules with Time Correction Sampler; An Adaptive Approach for Infinitely Many-armed Bandits under Generalized Rotting Constraints; A Unified Confidence Sequence for Generalized Linear Models, with Applications to Bandits; Preference Alignment with Flow Matching; Block Transformer: Global-to-Local Language Modeling for Fast Inference; A Unified Framework for Speculative Decoding with Multiple Drafters as a Bandit; FlickerFusion: Intra-trajectory Domain Generalizing Multi-agent Reinforcement Learning
- 2024-09 · EMNLP 2024 채택: Towards Fast Multilingual LLM Inference: Speculative Decoding and Specialized Drafters; Stable Language Model Pre-training by Reducing Embedding Variability; Towards Difficulty-Agnostic Efficient Transfer Learning for Vision-Language Models; BAPO: Base-Anchored Preference Optimization for Personalized Alignment in Large Language Models
- 2024-09 · TMLR 채택: Non-backtracking Graph Neural Networks
- 2024-05 · ICML 2024 채택: DistiLLM: Towards Streamlined Distillation for Large Language Models; Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs
- 2024-03 · NAACL 2024 채택: Carpe diem: On the Evaluation of World Knowledge in Lifelong Language Models
- 2024-02 · CVPR 2024 채택: FedSOL: Stabilized Orthogonal Learning in Federated Learning
- 2024-01 · AISTATS 2024 채택: Improved Regret Bounds of (Multinomial) Logistic Bandits via Regret-to-Confidence-Set Conversion
- 2024-01 · ICLR 2024 (1 spotlight) 채택: Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions
- 2023-12 · AAAI 2024 채택: Leveraging Normalization Layer in Adapters With Progressive Learning and Adaptive Distillation for Cross-Domain Few-Shot Learning
- 2023-10 · OPODIS 2023 채택: Flooding with Absorption: An Efficient Protocol for Heterogeneous Bandits over Complex Networks
- 2023-10 · EMNLP 2023 (1 main, 3 findings) 채택: Fast and Robust Early-Exiting Framework for Autoregressive Language Models with Synchronized Parallel Decoding; HARE: Explainable Hate Speech Detection with Step-by-Step Reasoning; NASH: A Simple Unified Framework of Structured Pruning for Accelerating Encoder-Decoder Language Models; Bayesian Multi-Task Transfer Learning for Soft Prompt Tuning
- 2023-09 · NeurIPS 2023 채택: Fair Streaming Principal Component Analysis: Statistical and Algorithmic Viewpoint; PLASTIC: Improving Input and Label Plasticity for Sample Efficient Reinforcement Learning
- 2023-05 · INTERSPEECH 2023 채택: Patch-Mix Contrastive Learning with Audio Spectrogram Transformer on Respiratory Sound Classification; Recycle-and-Distill: Universal Compression Strategy for Transformer-based Speech SSL Models with Attention Map Reusing and Masking Distillation
- 2023-05 · ACL 2023 채택: Large Language Models Are Reasoning Teachers
- 2023-02 · CVPR 2023 채택: Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning; Re-thinking Federated Active Learning based on Inter-class Diversity
- 2023-01 · EACL 2023 (findings) 채택: Revisiting Intermediate Layer Distillation for Compressing Language Models: An Overfitting Perspective
- 2023-01 · ICLR 2023 (1 spotlight) 채택: CUDA: Curriculum of Data Augmentation for Long-tailed Recognition; Mitigating Dataset Bias by Using Per-Sample Gradient
- 2023-01 · AISTATS 2023 채택: Contextual Linear Bandits under Noisy Features: Towards Bayesian Oracles; Nearly Optimal Latent State Decoding in Block MDPs
- 2023-01 · AAMAS 2023 채택: Toward Risk-based Optimistic Exploration for Cooperative Multi-Agent Reinforcement Learning
- 2022-11 · AAAI 2023 (2 orals) 채택: Denoising After Entropy-based Debiasing A Robust Training Method for Dataset Bias with Noisy Labels; Self-Contrastive Learning: Single-viewed Supervised Contrastive Framework using Sub-network; A Gift from Label Smoothing: Robust Training with Adaptive Label Smoothing via Auxiliary Classifier under Label Noise

## 연락과 위치

연구실은 KAIST 서울 홍릉캠퍼스에 있다. 누리집 주소 표기는 85, Hoegi-ro, Dongdaemun-gu, Seoul, South Korea이다.[^home]

김재철AI대학원 교수 목록의 사무실 표기는 9호관, 9501이다. 교수 업무 이메일은 yunseyoung@kaist.ac.kr이다.[^gsai]

## 각주
[^home]: OSI LAB, 첫 화면의 연구실 소개·주소·수상 안내. <https://osi.kaist.ac.kr/> 관측일 2026-11-09.
[^people]: OSI LAB, People의 교수·현재 구성원·Alumni·Past Interns. <https://osi.kaist.ac.kr/students/> 관측일 2026-11-09.
[^pubs]: OSI LAB, Publications의 학술지·학회·워크숍 목록. <https://osi.kaist.ac.kr/publications/> 관측일 2026-11-09.
[^news]: OSI LAB, News. <https://osi.kaist.ac.kr/news/> 관측일 2026-11-09.
[^gsai]: KAIST 김재철AI대학원, 구성원의 전임교수 윤세영 항목. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측일 2026-11-09.
[^prof]: Se-Young Yun, 교수 개인 소개의 학력·경력·수상. <https://fbsqkd.github.io/> 관측일 2026-11-11.
[^epidemic]: S. Kim, J. Shin, S. Eom, J. Oh, S.-Y. Yun, Real-time and Explainable Detection of Epidemics with Global News Data, Proceedings of the 1st Workshop on Healthcare AI and COVID-19, ICML 2022, PMLR 184, 73–90 (2022). <https://proceedings.mlr.press/v184/kim22a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v184/kim22a.html>. 관측일 2026-11-11.
[^health]: S. Bae 외, S.-Y. Yun, Patch-Mix Contrastive Learning with Audio Spectrogram Transformer on Respiratory Sound Classification, INTERSPEECH 2023. <https://doi.org/10.21437/interspeech.2023-1426> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p1]: J.-h. Kim, M. Vojnović, S.-Y. Yun, NeurIPS 2024 (2024). <https://doi.org/10.52202/079017-0281> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p2]: J. Lee, S.-Y. Yun, K.-S. Jun, NeurIPS 2024 (2024). <https://doi.org/10.52202/079017-3960> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p3]: S. Bae 외, S.-Y. Yun, NeurIPS 2025 (2025). <https://doi.org/10.52202/085713-3229> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p4]: S. H. Kim 외, S.-Y. Yun, NeurIPS 2025 (Spotlight) (2025). <https://doi.org/10.52202/085713-3087> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p5]: J. Ko, S. Kim, S. Cho, S.-Y. Yun, NeurIPS 2025 (2025). <https://doi.org/10.52202/085713-3625> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p6]: M. Kim 외, S.-Y. Yun, NeurIPS 2024 (2024). <https://doi.org/10.52202/079017-1108> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p7]: H. Jung 외, J. Shin, NeurIPS 2024 (2024). <https://doi.org/10.52202/079017-2417> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.
[^p8]: G. Lee 외, S.-Y. Yun, NeurIPS 2022 (2022). <https://doi.org/10.52202/068431-2787> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5091674853,publication_year:2021-2026>. 관측일 2026-11-11.

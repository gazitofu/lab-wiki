# Scalable Trustworthy AI (STAI Lab)

**KAIST 김재철AI대학원 · 오성준 부교수**

- 분야: 신뢰할 수 있는 인공지능, 에이전트와 기억, 정보 검색, 프라이버시, 학습 자료의 영향 설명[^home][^overview][^gsai]
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^overview][^home], AI·기계학습 보안·프라이버시[^overview][^home], 설명 가능한 AI(XAI)[^prof][^overview]
- 홈페이지: <https://stai-lab.org/>
- 근거와 출처: [STAI Lab 근거 페이지](stai-sources.md)

> 사람이 지식을 추적하고 고치며 통제할 수 있는 인공지능을 목표로, 에이전트의 기억과 검색, 시스템 평가, 정보 보호와 판단 근거를 연구한다.[^home][^overview]

## 무엇을 연구하나

STAI Lab은 인공지능(Artificial Intelligence, AI)의 신뢰성을 연구한다. 중심 방향은 **지식과 지능의 분리**다. 대형 언어 모델(Large Language Model, LLM: 많은 글을 학습해 글을 이해하고 생성하는 인공지능 모델) 안에 지식을 모두 담기보다, 사람이 해석하고 수정할 수 있는 외부 저장 부분에 지식을 두고 모델은 추론(주어진 정보로 결론이나 답을 도출하는 계산)과 일반화(학습에 쓰지 않은 입력에도 배운 규칙을 적용하는 능력)를 맡게 하려는 접근이다.[^overview] 연구실은 이를 통해 지식 수정과 삭제, 학습 자료의 영향 추적, 개인에 맞춘 변경을 가능하게 하려 한다.[^overview] 사생활과 사람의 통제권을 지키는 인공지능을 현재 연구 목표로 명시한다.[^overview][^home]

한 갈래는 **에이전트의 기억과 시스템 평가**다. 에이전트는 목표를 이루기 위해 정보를 받아 행동을 선택하고 도구를 사용하는 소프트웨어다. 연구실은 계획, 도구 사용, 여러 에이전트 사이의 협력을 포함한 시스템 전체를 개선하고, 새로운 정보와 사용자 수정을 매번 다시 학습하지 않고 받아들이는 기억을 연구한다.[^home] 대표 논문 1의 MEME(Multi-entity & Evolving Memory Evaluation)는 여러 대화에 걸쳐 정보가 바뀔 때 개체 사이의 의존 관계와 삭제 뒤 상태를 평가한다. 정적인 정보 검색에서 작동하던 기억 시스템도 이런 관계 추론에서는 어려움을 겪었다.[^p1] 대표 논문 2의 MASEval은 시스템 구성을 고정한 채 모델만 바꿔 비교하는 기존 평가에서 벗어나 시스템의 연결 구조, 실행 관리, 오류 처리 같은 구현 선택을 비교하는 평가 도구를 제안했다.[^p2]

또 다른 갈래는 **관련 근거를 찾아 쓰는 검색**이다. 연구실은 모델을 글과 이미지의 관련성 있는 최신 근거에 연결하는 방법을 연구한다.[^home] 대표 논문 4는 한 연구 분야의 아이디어를 다른 분야의 문제에 옮겨 쓸 수 있는 논문을 찾는 과제를 다룬다. 서로 다른 주제 사이의 인용을 이용해 학습·평가 자료를 만들었고, 그 자료로 검색기를 학습시키면 학습에서 보지 않은 분야와 유추를 요구하는 검색에서도 성능 향상이 이어짐을 보였다.[^p4]

**정보 보호와 지식 삭제**도 주요 갈래다. 대표 논문 3의 TULIP(Targeted Unlearning at Layers Identified Per-input)은 대형 언어 모델이 답을 형성하는 내부 층(입력을 단계마다 변환해 다음 단계로 넘기는 계산 단위)이 입력마다 다르다는 점에 착안해, 입력별로 층을 골라 지우려는 답과 연결되는 내부 표현을 바꾸는 방법이다.[^p3] 대표 논문 6은 정보를 무조건 숨기는 것보다 상황에 맞게 공개하도록 학습시키는 문제를 다룬다. 과제 수행에 필요한 정보 보존과 적절한 정보 공개를 분리해 함께 학습시켜, 사생활 보호와 과제 수행 사이의 충돌을 줄이려 했다.[^p6]

마지막 갈래는 **판단에 영향을 준 학습 자료를 설명하는 일**이다. 오성준 교수는 판단 근거를 설명하고 입력 변화에도 믿을 수 있게 작동하는 모델을 만드는 일과, 필요한 사람의 감독을 효율적으로 얻는 일을 연구 관심으로 밝힌다.[^prof] 대표 논문 5는 훈련 자료의 영향을 재는 기법이 과제의 의미보다 답변 형식에 반응하는지 조사했다. 과제와 답변 형식을 독립적으로 바꾸자, 자료를 학습할 때 모델 매개변수(학습해 모델의 계산과 출력을 결정하는 값)가 바뀌는 방향의 유사성이 답변 형식을 따르는 경향을 확인했다. 이런 영향 설명을 해석할 때 과제와 형식을 나누어 시험해야 한다는 결과다.[^p5]

## 주요 연구 주제

### 1. 지식을 수정할 수 있는 기억과 에이전트 평가

새 정보와 사용자 수정을 반영하는 기억, 여러 개체 사이의 정보 갱신과 삭제, 모델과 시스템 구현을 함께 비교하는 평가를 연구한다. 기억은 에이전트가 이후 작업에서 재사용하도록 보관하는 정보와 그 관리 기능이다.[^home][^p1][^p2]

### 2. 분야를 넘는 정보 검색과 근거 연결

모델에 관련 근거를 제공하는 검색과, 다른 연구 분야에서 활용할 수 있는 아이디어를 찾는 방법을 다룬다. 검색기는 질의에 관련된 자료를 찾아 순위를 매기는 프로그램이다.[^home][^p4]

### 3. 상황에 맞는 정보 공개와 모델의 지식 삭제

개인정보를 다루는 에이전트의 공개 결정을 학습시키고, 모델 안에서 지우려는 정보가 형성되는 위치를 찾아 변경하는 방법을 연구한다. 개인정보는 식별되었거나 식별할 수 있는 개인에 관한 정보다.[^overview][^p3][^p6]

### 4. 학습 자료의 영향과 설명의 신뢰성

특정 학습 자료가 모델의 결과에 미친 영향을 설명하고, 그 분석이 실제 과제의 의미를 반영하는지 평가한다.[^overview][^p5]

## 대표 논문

최근 5년 범위에서 오성준 교수의 KAIST 소속이 적힌 2026년 원고 6편을 골랐다. 기억·에이전트 평가·검색·정보 보호·학습 자료의 영향 설명을 고르게 다루며, 마지막 저자 논문 2편과 공동저자 논문 4편이다. 아래 판본은 arXiv 사전 공개본이며, 학회 이름은 연구실 기재를 함께 적었다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [MEME: Multi-entity & Evolving Memory Evaluation](https://doi.org/10.48550/arXiv.2605.12477) · arXiv 사전 공개본; NeurIPS Evaluations and Datasets Track(연구실 기재) | 대화가 여러 번 이어지는 동안 여러 대상의 정보가 바뀌고 지워질 때, 기억 시스템이 그 관계를 따라 답하는지 평가했다. 정보가 서로 의존하는 문제에서는 정적인 정보 검색이 되던 시스템도 어려움을 겪었고, 검색 깊이나 질문 지시의 개선만으로 그 차이가 해소되지 않았다.[^p1] | 1저자 Seokwon Jung, 마지막 저자 Seong Joon Oh |
| 2 | 2026 | [MASEval: Extending Multi-Agent Evaluation from Models to Systems](https://doi.org/10.48550/arXiv.2603.08835) · arXiv 사전 공개본; ACL System Demo(연구실 기재) | 에이전트의 성능을 모델 하나의 성능으로만 보지 않고, 전체 시스템의 연결 구조와 실행 관리, 오류 처리까지 비교하는 도구를 만들었다. 비교 실험에서는 시스템을 구현하는 틀의 선택도 모델의 선택만큼 성능에 영향을 주었다.[^p2] | 1저자 Cornelius Emde, 공동저자 Seong Joon Oh, 마지막 저자 Martin Gubri |
| 3 | 2026 | [TULIP: Targeted LLM Unlearning at Layers Identified Per-input](https://doi.org/10.48550/arXiv.2609.34591) · arXiv 사전 공개본 | 지우려는 답이 모델 안에서 형성되는 층을 입력마다 찾은 뒤, 그 층의 내부 표현과 지우려는 답의 연결을 약화하는 방법을 제안했다. 여러 모델과 평가 자료에서 비교 방법을 앞섰고, 질문을 바꾸거나 모델의 수치 표현을 바꾸는 공격에도 견디는 결과를 보였다.[^p3] | 1저자 Yejin Kim, 마지막 저자 Seong Joon Oh |
| 4 | 2026 | [Cross-Pollination Retrieval: Finding Transferable Ideas Across Fields in Scientific Literature](https://doi.org/10.48550/arXiv.2610.25678) · arXiv 사전 공개본 | 다른 분야의 문제에 옮겨 쓸 수 있는 아이디어를 담은 논문을 찾는 검색 과제를 만들었다. 서로 다른 주제 사이의 인용으로 학습 자료를 구성했으며, 그 자료로 학습한 검색기는 학습에서 제외한 분야와 유추·추론이 필요한 검색에서도 성능 향상을 보였다.[^p4] | 1저자 Seokwon Jung, 공동저자 Seong Joon Oh, 마지막 저자 Sangdoo Yun |
| 5 | 2026 | [Form Over Content In Gradient-Based Data Attribution Methods](https://doi.org/10.48550/arXiv.2609.19589) · arXiv 사전 공개본 | 훈련 자료의 영향을 재는 방법이 과제의 의미를 보는지 답변 형식을 보는지 분리해 시험했다. 모델이 학습하면서 바뀌는 방향의 유사성은 과제보다 답변 형식과 관련됐으며, 이런 기법을 의미상의 영향으로 해석할 때 독립적인 형식 검사가 필요함을 보였다.[^p5] | 1저자 Sunwoo Kim, 공동저자 Seong Joon Oh, 마지막 저자 Alice Oh |
| 6 | 2026 | [It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs](https://doi.org/10.48550/arXiv.2605.20258) · arXiv 사전 공개본; NeurIPS(연구실 기재) | 개인정보를 다루는 모델이 상황에 맞게 정보를 공개하면서도 과제를 수행하도록 학습시키는 방법을 제안했다. 과제에 필요한 정보 보존과 적절한 공개를 서로 구분해 함께 학습했으며, 평가에서는 비교 방법보다 나은 결과를 보이고 새로운 분야의 에이전트 작업에도 그 경향이 이어졌다.[^p6] | 1저자 Sangwoo Park, 공동저자 Seong Joon Oh, 마지막 저자 Sung Ju Hwang |

## 교수와 전문 분야

오성준 교수(Seong Joon Oh)는 KAIST 김재철AI대학원 부교수다. 대학원은 연구 분야를 Agentic AI, Trustworthy AI, AI Safety로 소개한다.[^gsai] 교수는 믿을 수 있는 기계학습 모델을 만드는 일과, 필요한 사람의 감독·지도를 비용 효율적으로 얻는 일을 연구한다고 밝힌다. 기계학습은 자료에서 규칙이나 예측 방법을 학습하는 계산 방법이다. 강건성은 입력 변화나 오류 같은 교란에도 필요한 성질과 성능을 유지하는 능력이며, 확률적인 모델은 가능한 결과와 그 가능성을 함께 다루는 모델이다.[^prof]

2026년 2월 연구 그룹을 튀빙겐 대학에서 KAIST로 옮겼다.[^pi-home] 이전에는 튀빙겐 AI 센터와 튀빙겐대학의 W2 교수로 4년, NAVER AI Lab의 연구 과학자로 3년 반 일했다. 2018년 Max-Planck Institute for Informatics에서 컴퓨터 비전과 기계학습 분야 박사 학위를 받았고, 학위 연구는 그 기술의 프라이버시·보안 문제를 다뤘다. 케임브리지대학에서 2013년 수학 학사, 2014년 수학 석사 학위를 받았다.[^prof]

대표 논문에서 드러나는 전문 분야는 장기 기억과 에이전트 시스템의 평가, 분야 간 검색, 모델 지식의 삭제와 상황별 정보 보호, 학습 자료의 영향 분석이다.[^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

여러 차례 대화하며 정보를 갱신하는 개인 비서와 에이전트, 과제에 맞는 시스템 구현의 비교, 다른 학문 분야에서 쓸 아이디어를 찾는 과학 문헌 검색에 연결된다.[^p1][^p2][^p4] 민감한 정보를 다루는 작업에서 정보 공개를 통제하고, 모델에 남은 특정 지식을 지우며, 모델의 결과와 학습 자료 사이의 관계를 설명하는 문제도 다룬다.[^p3][^p5][^p6]

## 구성원

2026년 11월 9일 연구실 Members 페이지 기준, PhD Student 10명, Collaborating PhD Student 5명, MSc Student 4명, Research Intern 7명으로 모두 26명이다. 협력 박사과정 5명은 연구실이 Collaborating PhD Student로 적은 사람들이다. 연구 주제는 게시 표기다.[^members] "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Stefano Woerner | 박사과정 | Few-shot Learning; Domain Generalisation; Human-inspired Machine Learning | stefano.woerner@uni-tuebingen.de |  |
| Alexander Rubinstein | 박사과정 | Trustworthy Machine Learning; Robustness; Uncertainty |  | 1, 2, 4 |
| Elisa Nguyen | 박사과정 | Trustworthy AI; Explainable AI; Human-Computer Interaction |  |  |
| Arnas Uselis | 박사과정 | Out-of-distribution generalization; Representation Learning; Causality |  | 1, 4 |
| Ankit Sonthalia | 박사과정 | Trustworthy Machine Learning; Robustness; OOD Generalization | ankit.sonthalia@uni-tuebingen.de |  |
| Darina Koishigarina | 박사과정 | Compositional Generalization; Representation Learning; Trustworthy Machine Learning | darina.koishigarina@uni-tuebingen.de |  |
| Lennart Bramlage | Collaborating PhD Student | Probabilistic Machine Learning; Reinforcement Learning; Human-Computer Interaction | lennart.bramlage@reutlingen-university.de |  |
| Sohyung Kim | 박사과정 | AI Safety; LLM Efficiency (Linear Attention, memory efficiency, human-inspired AI); Interpretability |  | 5 |
| Hoyeon Chang | Collaborating PhD Student | Systematicity; Compositional Generalization; Neural Belief Revision |  |  |
| Yunjae Won | Collaborating PhD Student | Preference Optimization; Continual Learning; Knowledge Distillation | yunjae.won@kaist.ac.kr |  |
| Bryan Truong | 박사과정 | Trustworthy Machine Learning; Uncertainty; Explainability |  |  |
| Shuman Peng | Collaborating PhD Student |  |  |  |
| Yejin Kim | 박사과정 | AI safety; Machine Unlearning; Trustworthy AI |  | 3, 4 |
| Hyeonbin Hwang | 박사과정 | LLM Post-Training: Reasoning & Agents | hbin0701@kaist.ac.kr |  |
| Sangwoo Park | Collaborating PhD Student | LLM Reasoning; Distillation; Alignment |  | 4, 6 |
| Jihyeok Jung | 석사과정 | Multimodal LLM; Vision-Language Reasoning & Alignment; Human-Centered AI | ji9759@kaist.ac.kr |  |
| Seokwon Jung | 석사과정 | Information Retrieval; Retrieval-Augmented Generation; Agentic Memory Systems |  | 1, 3, 4, 5 |
| Dohyun Kim | 석사과정 | Mechanistic interpretability; AI alignment | kimdoh0423@kaist.ac.kr |  |
| Viacheslav Sinii | 석사과정 | Knowledge-Intelligence Separation; Interpretable and Controllable AI; Reinforcement Learning |  |  |
| Seungwon Park | Research Intern | Representation; Multimodal; Trustworthy Machine Learning |  |  |
| Daeun Park | Research Intern | Agentic AI Systems; Human-Centered AI; Human-AI Collaboration |  | 3 |
| Junho Jeong | Research Intern | Mechanistic Interpretability; Knowledge Mechanisms |  |  |
| Seunghyun Park | Research Intern | Representation learning; Multimodal learning; Alignment |  |  |
| Yerang Kim | Research Intern | Information Retrieval; Reasoning; Linguistic Interpretability |  | 4 |
| Sam Lee | Research Intern | AI Safety |  |  |
| Denis Dokhyon Lim | Research Intern | Model Reasoning; Representation; Mechanistic Interpretability |  |  |

## 졸업생과 이전 구성원

연구실 Members 페이지 Alumni 구획의 11명이다. 과정과 현재 진로는 게시 표기이며, 이 구획에는 학위를 마쳤다는 뜻으로 한정되지 않는 이전 구성원도 포함된다. 교수가 연구 그룹을 튀빙겐 대학에서 KAIST로 옮기기 전의 구성원도 포함될 수 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Elif Akata | PhD Student | PhD Student, Helmholtz Munich |
| Michael Kirchhof | Collaborating PhD Student | Research Scientist, Apple |
| Bálint Mucsányi | MSc Student | PhD Candidate in Machine Learning, University of Tübingen |
| Evgenii Kortukov | MSc Student | Research Associate & PhD Candidate, Fraunhofer HHI |
| Anastasiia Alekseeva | MSc Student | AI Engineer, digetiers |
| Albert Catalan Tatjer | MSc Student | PhD Student, ELLIS Institute Tübingen |
| Johannes Bertram | MSc Student | PhD Student, ELLIS Institute Tübingen |
| Bora Kargi | MSc Student | Research Engineer, ELLIS Institute Tübingen |
| Philipp Davydov | MSc Student | JOSEPHA |
| Fabian Morelli | MSc Student | PhD Student, KTH Royal Institute of Technology |
| Luca Füger | MSc Student |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications 페이지의 게시 항목 64건이다. 2026년 29건, 2025년 13건, 2024년 8건, 2023년 10건, 2022년 4건이며, 연도는 연구실의 연도 구역 표기다. 제목·저자·발표처는 연구실 기재이고 학회명만 적힌 항목도 그 표기를 따른다. 오성준 교수는 2026년 2월 연구 그룹을 튀빙겐 대학에서 KAIST로 옮겼으며, 목록에는 이전 소속 시절 항목이 함께 포함되어 있다.[^pubs][^pi-home] 대표 논문 표에 든 항목은 그 표에 적힌 arXiv 사전 공개본의 초록을 설명했다. 저자 뒤 \*는 연구실의 표시이며, 뜻은 별도로 풀지 않는다. 같은 제목이 학회·워크숍 두 항목으로 적힌 경우에는 각각의 게시 항목을 둔다. 2023년 UAI-EAI의 Best Student Paper 표시는 해당 논문의 발표처 칸에 함께 적혀 있다.[^pubs]

**2026**

- Arnas Uselis, Yujin Jeong, Yanpeng Zhao, Alexander Rubinstein, Seong Joon Oh, Yonatan Bitton, Paul Gavrikov. "CRISP: Compositional Reasoning over Images via Stackable Programs for VLMs". *NeurIPS Evaluations and Datasets Track*.
- Sangwoo Park, Woongyeong Yeo, Yumin Choi, Hyomin Lee, Kangsan Kim, Seanie Lee, Jinheon Baek, Seong Joon Oh, Sung Ju Hwang. "It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs". *NeurIPS*. DOI: <https://doi.org/10.48550/arXiv.2605.20258>.
- Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh. "MEME: Multi-Entity & Evolving Memory Evaluation". *NeurIPS Evaluations and Datasets Track*. DOI: <https://doi.org/10.48550/arXiv.2605.12477>.
- Bora, Arnas Uselis, Seong Joon Oh. "Half-Truths Break Similarity-Based Retrieval". *NeurIPS*.
- Philipp, Ameya Prabhu, Matthias Bethge, Elisa Nguyen, Seong Joon Oh. "LLM generation novelty through the lens of semantic similarity". *EMNLP Findings*.
- Arnas Uselis\*, Darina Koishigarina\*, Seong Joon Oh. "How can embedding models bind concepts?". *ICML Spotlight*.
- Yujin Jeong, Arnas Uselis, Iro Laina, Seong Joon Oh, Anna Rohrbach. "When Do Diffusion Models learn to Generate Multiple Objects?". *ICML*.
- Arnas Uselis, Andrea Dittadi, Seong Joon Oh. "Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models". *ICML Oral*.
- Stefano, Seong Joon Oh, Christian F. Baumgartner. "Universal Algorithm-Implicit Learning". *ICML*.
- Hoyeon, Bálint, Seong Joon Oh. "Dynamics Reveals Structure: Challenging the Linear Propagation Assumption". *ICML Spotlight*.
- Cornelius Emde, Alexander Rubinstein\*, Anmol Goel\*, Ahmed Heakl\*, Sangdoo Yun, Seong Joon Oh, Martin Gubri. "MASEval: Extending Multi-Agent Evaluation from Models to Systems". *ACL System Demo*. DOI: <https://doi.org/10.48550/arXiv.2603.08835>.
- Anmol Goel, Cornelius Emde, Sangdoo Yun, Seong Joon Oh, Martin Gubri. "Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models". *ACL*.
- Darina Koishigarina, Arnas Uselis, Seong Joon Oh. "CLIP Behaves like a Bag-of-Words Model Cross-modally but not Uni-modally". *ICLR*.
- Alexander Rubinstein, Benjamin Raible, Martin Gubri, Seong Joon Oh. "DISCO: Diversifying Sample Condensation for Efficient Model Evaluation". *ICLR*.
- Ahmed Heakl, Martin Gubri, Salman Khan, Sangdoo Yun, Seong Joon Oh. "Dr.LLM: Dynamic Layer Routing for LLMs". *ICLR*.
- Minyoung Lee, Yeji Park, Dongjun Hwang, Yejin Kim, Seong Joon Oh, Junsuk Choe. "Enhancing Multi-Image Understanding through Delimiter Token Scaling". *ICLR*.
- Michael, Luca, Adam Golinski, Eeshan Gunesh Dhekane, Arno Blaas, Seong Joon Oh, Sinead Williamson. "SelfReflect: Can LLMs Communicate Their Internal Answer Distribution?". *ICLR*.
- Yejin Kim, William F. Shen, Seokwon Jung, Seong Joon Oh. "Break the Output Geometry for Large Language Model Unlearning". *ICML 2026 MemFM Workshop*.
- Cornelius Emde, Anmol Goel, Sangdoo Yun, Seong Joon Oh, Martin Gubri. "Lost in Communication: Uncertainty Propagation in Multi-Agent Systems". *ICML 2026 AgenticUQ Workshop*.
- Shuman Peng, Arnas Uselis, Darina Koishigarina, Martin Ester, Seong Joon Oh. "CLIP Models Generalize Less Than Compositional Benchmarks Suggest". *ICML 2026 CompLearn Workshop*.
- Ankit Sonthalia, Arnas Uselis, Seong Joon Oh. "Do vision models know that three is three?". *arXiv*.
- Seokwon Jung, Yerang Kim, Yejin Kim, Alexander Rubinstein, Arnas Uselis\*, Sangwoo Park\*, Seong Joon Oh, Sangdoo Yun. "Cross-Pollination Retrieval: Finding Transferable Ideas Across Fields in Scientific Literature". *arXiv*. DOI: <https://doi.org/10.48550/arXiv.2610.25678>.
- Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh. "Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?". *arXiv*.
- Yejin Kim, William F. Shen, Seokwon Jung, Daeun, Seong Joon Oh. "TULIP: Targeted LLM Unlearning at Layers Identified Per-input". *arXiv*. DOI: <https://doi.org/10.48550/arXiv.2609.34591>.
- Sunwoo Kim, Seokwon Jung, Sohyung Kim, Seong Joon Oh, Alice Oh. "Form Over Content In Gradient-Based Data Attribution Methods". *arXiv*. DOI: <https://doi.org/10.48550/arXiv.2609.19589>.
- Jihyeok Jung, Jeewu Lee, Sanghyeop Kim, Chanhee Han, Seong Joon Oh. "EgoGapBench: Benchmarking Egocentric Action Selection in Multi-Agent Scenes". *arXiv*.
- Elena Sofia Ruzzetti, Cornelius Emde, Sangdoo Yun, Seong Joon Oh, Martin Gubri. "MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations". *arXiv*.
- Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek. "Predicting Future Behaviors in Reasoning Models Enables Better Steering". *arXiv*.
- Fabian, Arnas Uselis, Ankit Sonthalia, Seong Joon Oh. "Sparse Autoencoders enable Robust and Interpretable Fine-tuning of CLIP models". *arXiv*.

**2025**

- Yujin Jeong\*, Arnas Uselis\*, Seong Joon Oh, Anna Rohrbach. "Diffusion Classifiers Understand Compositionality, but Conditions Apply". *NeurIPS D&B*.
- Ankit Sonthalia, Arnas Uselis, Seong Joon Oh. "On the Rankability of Visual Embeddings". *NeurIPS*.
- Dongjun Hwang, Yejin Kim, Minyoung Lee, Seong Joon Oh, Junsuk Choe. "OVS Meets Continual Learning: Towards Sustainable Open-Vocabulary Segmentation". *NeurIPS*.
- Haritz Puerto, Martin Gubri, Tommaso Green, Seong Joon Oh, Sangdoo Yun. "C-SEO Bench: Does Conversational SEO Work?". *NeurIPS D&B*.
- Tommaso Green, Martin Gubri, Haritz Puerto, Sangdoo Yun, Seong Joon Oh. "Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers". *EMNLP*.
- Arnas Uselis, Andrea Dittadi, Seong Joon Oh. "Does Data Scaling Lead to Visual Compositional Generalization?". *ICML*.
- Ankit Sonthalia, Alexander Rubinstein, Ehsan Abbasnejad, Seong Joon Oh. "Do Deep Neural Network Solutions Form a Star Domain?". *ICLR*.
- Arnas Uselis, Seong Joon Oh. "Intermediate Layer Classifiers for OOD Generalization". *ICLR*.
- Jaehyun Pahk, Donghyeon Kwon, Seong Joon Oh, Suha Kwak. "Decoupled Finetuning for Domain Generalizable Semantic Segmentation". *ICLR*.
- Elif, Lion Schulz, Julian Coda-Forno, Seong Joon Oh, Matthias Bethge, Eric Schulz. "Playing repeated games with Large Language Models". *Nature Human Behaviour*.
- Alexander Rubinstein, Ameya Prabhu, Matthias Bethge, Seong Joon Oh. "Are We Done with Object-Centric Learning?". *SCSL @ ICLR*.
- Luca Scimeca, Alexander Rubinstein, Damien Teney, Seong Joon Oh, Yoshua Bengio. "Mitigating Shortcut Learning with Diffusion Counterfactuals and Diverse Ensembles". *SCSL @ ICLR*.
- Sohyun Lee, Nayeong Kim, Juwon Kang, Seong Joon Oh, Suha Kwak. "DiCoTTA: Domain-invariant Learning for Continual Test-time Adaptation". *arXiv*.

**2024**

- Bálint, Michael, Seong Joon Oh. "Benchmarking Uncertainty Disentanglement: Specialized Uncertainties for Specialized Tasks". *NeurIPS D&B (Spotlight)*.
- Haritz Puerto, Martin Gubri, Sangdoo Yun, Seong Joon Oh. "Scaling Up Membership Inference: When and How Attacks Succeed on Large Language Models". *NAACL Findings*.
- Evgenii, Alexander Rubinstein, Elisa Nguyen, Seong Joon Oh. "Studying Large Language Model Behaviors Under Realistic Knowledge Conflicts". *CoLM*.
- Dennis Ulmer, Martin Gubri, Hwaran Lee, Sangdoo Yun, Seong Joon Oh. "Calibrating Large Language Models Using Their Generations Only". *ACL*.
- Martin Gubri, Dennis Ulmer, Hwaran Lee, Sangdoo Yun, Seong Joon Oh. "TRAP: Targeted Random Adversarial Prompt Honeypot for Black-Box Identification". *ACL Findings*.
- Elisa Nguyen, Johannes, Evgenii, Jean Y. Song, Seong Joon Oh. "Towards User-Focused Research in Training Data Attribution for Human-Centered Explainable AI". *arXiv*.
- Alexander Rubinstein, Luca Scimeca, Damien Teney, Seong Joon Oh. "Scalable Ensemble Diversification for OOD Generalization and Detection". *arXiv*.
- Michael, Mark Collier, Seong Joon Oh, Enkelejda Kasneci. "Pretrained Visual Uncertainties". *arXiv*.

**2023**

- Elisa Nguyen, Minjoon Seo, Seong Joon Oh. "A Bayesian Perspective On Training Data Attribution". *NeurIPS*.
- Damien Teney, Lin Yong, Seong Joon Oh, Ehsan Abbasnejad. "ID and OOD Performance Are Sometimes Inversely Correlated on Real-world Datasets". *NeurIPS*.
- Michael, Bálint, Seong Joon Oh, Enkelejda Kasneci. "URL: A Representation Learning Benchmark for Transferable Uncertainty Estimates". *NeurIPS D&B*.
- Siwon Kim, Sangdoo Yun, Hwaran Lee, Martin Gubri, Sungroh Yoon, Seong Joon Oh. "ProPILE: Probing Privacy Leakage in Large Language Models". *NeurIPS Spotlight*.
- Dongyoon Han\*, Junsuk Choe\*, Seonghyeok Chun, John Joon Young Chung, Minsuk Chang, Sangdoo Yun, Jean Y. Song, Seong Joon Oh. "Neglected Free Lunch -- Learning Image Classifiers Using Annotation Byproducts". *ICCV*.
- Hyeon-Woo Nam, Yu-Ji Kim, Byeongho Heo, Dongyoon Han, Seong Joon Oh, Tae-Hyun Oh. "Scratching Visual Transformer's Back with Uniform Attention". *ICCV*.
- Michael, Enkelejda Kasneci, Seong Joon Oh. "Probabilistic Contrastive Learning Recovers the Correct Aleatoric Uncertainty of Ambiguous Inputs". *ICML*.
- Elisa Nguyen, Evgenii, Jean Y. Song, Seong Joon Oh. "Exploring Practitioner Perspectives On Training Data Attribution Explanations". *NeurIPS XAI in Action Workshop*.
- Michael, Bálint, Seong Joon Oh, Enkelejda Kasneci. "URL: A Representation Learning Benchmark for Transferable Uncertainty Estimates". *UAI-EAI Best Student Paper*.
- Bálint, Michael, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh. "Trustworthy Machine Learning". *arXiv*.

**2022**

- Sanghyuk Chun, Wonjae Kim, Song Park, Minsuk Chang, Seong Joon Oh. "ECCV Caption: Correcting False Negatives by Collecting Machine-and-Human-verified Image-Caption Associations for MS-COCO". *ECCV*.
- Jang-Hyun Kim, Jinuk Kim, Seong Joon Oh, Sangdoo Yun, Hwanjun Song, Joonhyun Jeong, Jung-Woo Ha, Hyun Oh Song. "Dataset Condensation via Efficient Synthetic-Data Parameterization". *ICML*.
- Jungbeom Lee, Seong Joon Oh, Sangdoo Yun, Junsuk Choe, Eunji Kim, Sungroh Yoon. "Weakly Supervised Semantic Segmentation Using Out-of-Distribution Data". *CVPR*.
- Luca Scimeca\*, Seong Joon Oh\*, Sanghyuk Chun, Michael Poli, Sangdoo Yun. "Which Shortcut Cues Will DNNs Choose? A Study from the Parameter-Space Perspective". *ICLR*.

## 연락과 위치

- 교수 업무 이메일: coallaoh@kaist.ac.kr[^contact]
- 연구실 연락 주소: 서울 AI 허브, 서울특별시 서초구 태봉로 108, 우편번호 06764[^contact]
- 교수 사무실: 양재캠퍼스 5층(504)[^gsai]
[^home]: STAI Lab, 연구실 첫 화면. <https://stai-lab.org/> 관측 2026-11-09.
[^overview]: STAI Lab, 연구 방향 소개. <https://stai-lab.org/overview/overview/> 관측 2026-11-09.
[^prof]: STAI Lab, Seong Joon Oh 소개와 이력. <https://stai-lab.org/member/joon/> 관측 2026-11-09.
[^pi-home]: Seong Joon Oh, 개인 누리집의 연구 그룹 이전 이력. <https://seongjoonoh.com/> 관측 2026-11-11.
[^gsai]: KAIST 김재철AI대학원, 전임교수 오성준의 직위·연구 분야·사무실. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-11-09.
[^members]: STAI Lab, Members의 현재 구성원과 Alumni. <https://stai-lab.org/members/> 관측 2026-11-09.
[^pubs]: STAI Lab, Publications의 2022–2026년 게시 논문. <https://stai-lab.org/publication/> 관측 2026-11-09.
[^contact]: STAI Lab, Contact의 교수 업무 이메일과 주소. <https://stai-lab.org/contact/> 관측 2026-11-11.
[^p1]: S. Jung 외, S. J. Oh, arXiv (온라인 2026-05-12). <https://doi.org/10.48550/arXiv.2605.12477> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.12477>. 관측 2026-11-11.
[^p2]: C. Emde 외, M. Gubri, arXiv (온라인 2026-03-09). <https://doi.org/10.48550/arXiv.2603.08835> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.08835>. 관측 2026-11-11.
[^p3]: Y. Kim 외, S. J. Oh, arXiv (온라인 2026-09-28). <https://doi.org/10.48550/arXiv.2609.34591> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.34591>. 관측 2026-11-11.
[^p4]: S. Jung 외, S. Yun, arXiv (온라인 2026-10-19). <https://doi.org/10.48550/arXiv.2610.25678> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.25678>. 관측 2026-11-11.
[^p5]: S. Kim 외, A. Oh, arXiv (온라인 2026-09-17). <https://doi.org/10.48550/arXiv.2609.19589> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.19589>. 관측 2026-11-11.
[^p6]: S. Park 외, S. J. Hwang, arXiv (온라인 2026-05-18). <https://doi.org/10.48550/arXiv.2605.20258> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.20258>. 관측 2026-11-11.

# MLAI

**KAIST 김재철AI대학원 · 황성주 부교수**

- 분야: 기계학습, 인공지능의 시각 인식과 언어 이해[^gsai]
- 대분야: 컴퓨팅·AI
- 태그: 생성 인공지능[^prof][^p3], 대형 언어 모델[^prof][^p2], 모델 경량화·양자화[^prof][^p2], 연속학습[^prof][^p5], 연합학습·분산 학습[^prof][^p4], 과학·공학 AI[^prof][^p6], AI·기계학습 보안·프라이버시[^prof][^p4][^p8]
- 홈페이지: <https://www.mlai-kaist.com/>
- 근거와 출처: [MLAI 근거 페이지](mlai-sources.md)

> 언어와 영상의 이해·생성, 새 지식의 학습, 분자 설계에 필요한 기계학습 방법을 연구한다.

## 무엇을 연구하나

MLAI는 실제 응용 환경에서 인공지능을 사용하는 데 필요한 새 모형과 알고리즘(문제를 해결하기 위한 절차)을 개발한다. 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 방법)의 학습 방식과 활용 방법을 다루며, 교수의 연구 관심은 생성 방법과 언어 모형, 스스로 개선하는 인공지능, 과학적 발견, 기기에서의 학습, 안전한 학습이다.[^prof] 언어 모델(언어 자료의 규칙을 학습해 표현의 가능성을 계산하거나 문장을 만드는 모형)에서는 긴 문서의 근거를 연결해 답을 구하는 방법과, 검색·코드 실행을 이용해 과제를 푸는 방법을 제안했다.[^p1][^p2]

생성 방법도 연구한다. 확산 모델(자료에 잡음을 더하는 과정과 그 반대 과정을 이용해 새로운 자료를 만드는 모형)을 언어 자료에 맞게 설계하고, 그래프(대상과 그 사이의 관계를 점과 선으로 나타낸 구조)의 점과 연결 관계를 함께 생성하는 방법을 제안했다. 분자(원자들이 화학 결합으로 연결된 독립된 입자) 설계에서는 목표 성질에 기여하는 조각을 찾아 조립하고 바꾸는 생성 방법을 개발했다. 생성 모형과 과학적 발견을 주요 연구 갈래로 삼아 새로운 언어 자료와 분자 구조를 만드는 방법을 연구한다.[^prof][^p3][^p6][^p7]

학습의 지속성과 안전성도 다룬다. 지속학습(과제가 순차적으로 주어질 때 앞서 배운 지식을 유지하며 새 내용을 배우는 방법)을 영상 분할(영상의 각 위치를 영역이나 대상에 배정하는 작업)에 적용하는 새 방법을 제안했다. 연합학습(자료를 중앙에 모으지 않고 여러 참여자가 각자 가진 자료로 함께 모형을 학습하는 방법)에서는 개인정보 보호를 위한 잡음 때문에 학습이 불안정해지는 문제를 다뤘다. 적대적 공격(모형의 잘못된 판단을 유도하도록 입력 등을 의도적으로 조작하는 행위)에 견디는 학습 방법도 제안했다. 이들은 교수 소개가 연구 주제로 제시한 온라인 지속학습·연합학습과 다양한 공격에 대한 방어에 해당한다.[^prof][^p4][^p5][^p8]

## 주요 연구 주제

### 언어 추론과 도구를 사용하는 모형

긴 문서를 입력받는 것과 문서 사이의 근거를 연결하는 것은 별개의 문제다. TOTAL(Thought Template Augmented Long-Context Language Models)은 앞선 문제 풀이에서 얻은 사고 절차를 재사용 가능한 틀로 만들고, 자연어로 주어진 피드백을 이용해 그 틀을 갱신한다. Agent Distillation은 지식 증류(한 모형의 출력이나 내부 표현 등을 이용해 다른 모형을 학습시키는 방법)를 통해 큰 모형의 추론과 검색·코드 도구 사용 행동을 작은 모형에 전달한다. 여기서 에이전트는 목표를 수행하기 위해 행동이나 도구 사용을 선택하는 시스템이다.[^p1][^p2]

언어 모형과 자동 연구 에이전트를 주요 연구 주제로 삼으며, 계산 부담을 줄이기 위해 큰 언어 모형의 과제 해결 행동을 작은 모형으로 전달하는 모델 경량화(모형의 구조·수치 표현·추론 경로를 바꾸어 계산량이나 저장 공간 사용을 줄이는 방법)를 연구한다.[^prof][^p2]

### 언어·그래프·분자를 생성하는 방법

언어 생성에서는 서로 구별되는 범주로 이루어진 자료의 구조를 반영해 연속적인 확산 과정을 설계했다. 그래프 생성에서는 점과 선 사이의 의존 관계를 함께 다루는 확산 과정을 제안했다. 분자 생성에서는 목표 성질에 맞는 조각을 추출하고, 조립과 수정을 반복하면서 사용할 조각의 목록을 갱신한다.[^p3][^p6][^p7]

### 기존 지식을 보존하는 영상 학습

새로운 종류의 대상을 학습하는 동안 이전 종류에 관한 지식을 잊는 문제를 다룬다. ECLIPSE는 영상의 대상 종류와 개별 대상을 함께 구분하는 작업에서 기본 모형을 고정하고, 입력에 덧붙이는 학습 가능한 표현을 조정한다. 여러 종류가 공유하는 지식을 활용하도록 출력 점수도 조작한다.[^p5]

### 개인정보 보호와 공격에 대한 견고성

FedSVD는 여러 참여자가 함께 언어 모형을 갱신할 때 개인정보 보호를 위한 잡음이 증폭되는 문제를 다룬다. 매개변수(모형의 동작을 정하며 학습으로 조정되는 수치)의 표현 방식을 바꾸어 학습의 안정성과 성능을 개선했다. 적대적 학습 연구에서는 같은 자료를 서로 다르게 변형한 뒤 공격하더라도 예측이 일관되도록 학습시켜, 학습 때 사용하지 않은 공격에 대한 일반화도 평가했다.[^p4][^p8]

## 대표 논문

언어 추론·생성, 영상의 지속학습, 분산 환경의 개인정보 보호, 분자 설계와 공격에 대한 견고성을 나누어 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [When Thoughts Meet Facts: Reusable Reasoning for Long-Context LMs](https://doi.org/10.18653/v1/2026.findings-acl.81) · Findings of ACL | 여러 문서를 한꺼번에 입력해도 그 안의 근거를 연결하지 못하는 문제를 다룬다. 과거 문제 풀이에서 얻은 사고 절차를 재사용 가능한 틀로 만들고, 자연어 피드백으로 갱신하는 TOTAL을 제안했다. 여러 평가 과제에서 검색을 사용하는 경우와 사용하지 않는 경우 모두에서 기준 방법보다 성능을 개선했고, 최적화한 틀을 작은 공개 모형으로 전달할 수 있음을 보였다.[^p1] | 1저자 Soyeong Jeong, 공저자 황성주 |
| 2 | 2025 | [Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://doi.org/10.52202/085713-3553) · NeurIPS | 큰 언어 모형의 풀이 문장만 작은 모형에 가르치면 드문 사실이나 정확한 계산이 필요한 문제에서 어려움이 생긴다. 추론과 함께 검색·코드 도구를 사용하는 행동을 전달하는 Agent Distillation을 제안했다. 교사가 만드는 행동 기록의 품질과 작은 에이전트의 행동 선택을 개선하는 방법을 함께 사용했고, 사실·수학 추론 과제에서 작은 도구 사용 에이전트의 가능성을 보였다.[^p2] | 1저자 Minki Kang, 마지막 저자 황성주 |
| 3 | 2025 | [Continuous Diffusion Model for Language Modeling](https://doi.org/10.52202/085713-3256) · NeurIPS | 언어처럼 서로 구별되는 값으로 이루어진 자료를 연속적인 확산 과정으로 생성한다. 범주형 확률분포의 기하 구조를 반영해 기존 이산 확산과 연속 흐름의 관계를 정리하고, 모의 실행을 하지 않는 학습 방식을 제안했다. 언어와 다른 종류의 자료를 이용한 실험에서 기존 이산 확산 모형보다 좋은 결과를 보였고, 앞선 값에 이어 다음 값을 생성하는 모형의 성능에 접근했다.[^p3] | 1저자 Jaehyeong Jo, 마지막 저자 황성주 |
| 4 | 2025 | [FedSVD: Adaptive Orthogonalization for Private Federated Learning with LoRA](https://doi.org/10.52202/085713-3998) · NeurIPS | 학습된 언어 모형을 적은 수의 수치로 갱신하는 LoRA, 즉 Low-Rank Adaptation을 개인정보 보호 학습과 함께 사용할 때 잡음이 증폭되는 문제를 다룬다. 각 참여자가 보낸 갱신을 서버에서 합친 뒤 수치의 표현을 다시 분해하는 FedSVD를 제안했다. 이론 분석과 여러 평가 과제에서 안정성·성능 개선을 보였으며, 개인정보 보호를 적용한 경우와 적용하지 않은 경우를 함께 평가했다.[^p4] | 1저자 Seanie Lee, 마지막 저자 황성주 |
| 5 | 2024 | [ECLIPSE: Efficient Continual Learning in Panoptic Segmentation with Visual Prompt Tuning](https://doi.org/10.1109/cvpr52733.2024.00322) · CVPR | 영상의 각 위치가 어떤 종류인지와 개별 대상 중 어디에 속하는지를 함께 구분하면서, 새로운 종류를 순차적으로 학습한다. 기본 모형을 고정하고 적은 수의 입력 표현만 학습하는 방법과 출력 점수를 조작하는 방법을 제안했다. ADE20K의 지속학습 평가에서 과거 지식을 잊는 현상과 새 종류를 배우는 능력을 함께 다뤘다.[^p5] | 1저자 Beomyoung Kim, 마지막 저자 황성주 |
| 6 | 2024 | [Drug Discovery with Dynamic Goal-aware Fragments](https://doi.org/10.48550/arxiv.2310.00841) · arXiv, ICML 2024 표기 | 약물 후보를 만드는 과정에서 목표 성질에 기여하는 분자 조각을 찾고, 그 조각을 조립·수정하는 GEAM, 즉 Goal-aware fragment Extraction, Assembly, and Modification을 제안했다. 생성 중 새로 찾은 목표 지향 조각으로 목록을 갱신해 처음의 조각 목록 밖으로 탐색할 수 있게 했다. 여러 약물 탐색 과제에서 이 생성 절차를 평가했다.[^p6] | 1저자 Seul Lee, 마지막 저자 황성주 |
| 7 | 2022 | [Score-based Generative Modeling of Graphs via the System of Stochastic Differential Equations](https://doi.org/10.48550/arxiv.2202.02514) · arXiv, 연구실 ICML 2022 표기 | 그래프를 생성할 때 점과 연결 관계 사이의 의존성을 함께 배울 필요가 있다. 이 둘의 결합 분포를 다루는 연속 시간 확산 과정과 그 반대 방향에서 자료를 생성하는 계산 방법을 제안했다. 여러 자료에서 기준 방법과 비교했고, 분자 생성에서 학습 자료의 분포에 가까우면서 화학 결합 규칙을 어기지 않는 분자를 만들 수 있음을 보였다.[^p7] | 1저자 Jaehyeong Jo, 마지막 저자 황성주 |
| 8 | 2022 | [Consistency Regularization for Adversarial Robustness](https://doi.org/10.1609/aaai.v36i8.20817) · AAAI | 공격에 견디도록 계속 학습하다가 오히려 견고성이 떨어지는 문제를 다룬다. 같은 자료를 두 가지로 변형하고 각각 공격한 뒤에도 예측 분포가 비슷하도록 학습시키는 조건을 추가했다. 여러 적대적 학습 방법의 평가 정확도를 개선했으며, 학습 때와 종류가 다르거나 변화량이 큰 공격에 대한 일반화에도 도움이 됨을 보였다.[^p8] | 1저자 Jihoon Tack, 공저자 황성주 |

## 교수와 전문 분야

황성주 교수는 2013년 텍사스대학교 오스틴에서 컴퓨터과학 박사학위를 받았다.[^csprof] Disney Research의 박사후 연구원, UNIST 전기·컴퓨터공학 분야 조교수를 거쳐 KAIST에서 연구하고 있다. 연구실 소개는 김재철AI대학원과 전산학부의 부교수로 소개하고,[^people] 전산학부 교수 소개의 직위는 겸임교수다.[^csprof] 김재철AI대학원은 연구 분야를 기계학습과 인공지능의 시각 인식·언어 이해로 적는다.[^gsai]

교수 개인 누리집의 경력은 2018년 1월 KAIST 전산학부 조교수 부임, 2020년 3월부터 인공지능대학원과 전산학부의 부교수 재직을 적는다. 연구 관심은 생성 인공지능과 큰 언어 모형, 스스로 개선하는 인공지능, 과학적 발견을 위한 인공지능, 기기에서의 학습, 안전한 학습이다. 세부 주제로 모형 압축·지속학습·연합학습, 불확실성의 모형화와 정량화, 다양한 공격에 대한 방어를 제시한다.[^prof]

대표 논문으로 보면 전문 분야는 언어 모형의 추론·도구 사용, 언어와 그래프의 생성 방법, 순차적인 시각 지식 학습, 개인정보 보호와 공격에 견디는 학습이다. 분자 조각을 이용한 약물 후보 생성도 연구한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

문서에 근거한 질문 응답과 도구를 쓰는 작은 언어 에이전트,[^p1][^p2] 새로운 대상이 추가되는 영상 인식,[^p5] 여러 참여자의 자료를 한곳에 모으지 않는 언어 모형 학습,[^p4] 목표 성질을 갖는 약물 후보 탐색[^p6]에 연구 방법을 적용한다. 연구실 과제에는 기계학습 모형의 취약점 시험과 방어, 응용 인공지능 연구, 대규모 기계학습, 드론 기술의 학습·추론이 있다.[^projects]

## 구성원

2026년 11월 9일 연구실 People의 Research Fellow, PhD Students, MS Students, Interns 구획에 게시된 45명이다. 과정·직위와 연구 주제는 게시 표기를 따랐다.[^people] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jinheon Baek | 연구원 | Machine Learning for Language and Knowledge | jinheon.baek@kaist.ac.kr |  |
| Jaehyeong Jo | 연구원 | Diffusion Models, AI4Science | harryjo97@kaist.ac.kr | 3, 7 |
| Bedionita Soro | 연구원 | Weight-Space Learning | sorobedio@kaist.ac.kr |  |
| Taewook Nam | 박사과정 | Meta Learning, Reinforcement Learning, Bayesian Deep Learning | namsan@kaist.ac.kr |  |
| Youngwan Lee | 박사과정 | Object Detection/Segmentation, Self-Supervised Learning |  |  |
| Dongki Kim | 박사과정 | AI4Science | cleverki@kaist.ac.kr |  |
| Jenny Yang | 박사과정 | LLM Reasoning, RAG | jenny_yang@kaist.ac.kr |  |
| Heejun Lee | 박사과정 | Network Compression, Computer Vision | ainl@kaist.ac.kr |  |
| Sangwoo Park | 박사과정 | Reasoning, Distillation | swgger@kaist.ac.kr | |
| Junhyun Park | 박사과정 | Computer Vision, Reinforcement Learning |  |  |
| Dongchan Min | 박사과정 | Speech, Generative Models | alsehdcks95@kaist.ac.kr |  |
| Jaewoong Lee | 박사과정 | Computer Vision, Multimodal |  |  |
| Junmo Cho | 박사과정 | Embodied AI | junmokane@kaist.ac.kr |  |
| Yukyeong Lee | 박사과정 | Agentic AI, Self-Evolving AI | yukyeong@kaist.ac.kr |  |
| Minki Kang | 박사과정 | LLMs, Agent, Distillation | zzxc1133@kaist.ac.kr | 2 |
| Beomyoung Kim | 박사과정 | Computer Vision, Segmentation, Detection | beomyoung.kim@kaist.ac.kr | 5 |
| Soyeong Jeong | 박사과정 | Natural Language Processing, RAG | starsuzi@kaist.ac.kr | 1 |
| Sangwon Jang | 박사과정 | Generative Models, Computer Vision | sangwon.jang@kaist.ac.kr |  |
| Taekyung Ki | 박사과정 | Generative Models, Computer Vision | taekyung.ki@kaist.ac.kr |  |
| Dongbok Lee | 박사과정 | Natural Language Processing, Generative Models |  |  |
| Geon Park | 박사과정 | Neural Architecture Search, Federated Learning, Neural Network Quantization | geon.park@kaist.ac.kr |  |
| Jin Jiongdao | 박사과정 | Continual Learning | jinjiongdao@kaist.ac.kr |  |
| Kangsan Kim | 박사과정 | Agents, Multimodal | kksan07@kaist.ac.kr |  |
| Jun Hyeong Kim | 박사과정 | Large Language Models, RAG, AI in Biomedicine | tommy0906@snu.ac.kr |  |
| Yumin Choi | 석사과정 | Large Language Models | yuminchoi@kaist.ac.kr |  |
| ByeongHun Bang | 석사과정 | Large Language Models, Agentic AI, Knowledge Distillation | bh.bang@kaist.ac.kr |  |
| Daegyu Sung | 석사과정 | Coding Agent, Agentic AI | sbigstar0310@kaist.ac.kr |  |
| Sangwoo Park | 석사과정 | LLMs, RAG, AI4Science, Agents | jackson0530@kaist.ac.kr | |
| Aoxuan Silvia Zhang | 석사과정 | LLMs, Generative Models, Weight Space Learning | aoxuan-silvia-zhang@kaist.ac.kr |  |
| Sehee Kim | 석사과정 | Self-Evolving AI, Agentic AI, AI for finance | sehee.kim@kaist.ac.kr |  |
| Woongyeong Yeo | 석사과정 | Multimodal Learning, LLMs | wgcyeo@kaist.ac.kr |  |
| Hyunbin Kwak | 석사과정 | Self-Improving Agents, Research Agent, LLMs | hbin.gk@kaist.ac.kr |  |
| Hanna Lee | 석사과정 | Agentic AI, Parameter-Efficient Fine-Tuning | dlgkssk38@snu.ac.kr |  |
| Hyomin Lee | 석사과정 | Safe & Trustworthy AI | hyomin.lee@kaist.ac.kr |  |
| Dohyeon Kim | 석사과정 | LLMs, Weight Space Learning | dhkim011030@kaist.ac.kr |  |
| Nahyun Kim | 인턴 | Generative Models, AI in biology | hyun0414@kaist.ac.kr |  |
| Jaehyuk Sung | 인턴 | LLMs, Agentic AI |  |  |
| Myeongkyun Cho | 인턴 | Self-Evolving AI, Data-Efficient Learning | myeongkyuncho@kaist.ac.kr |  |
| Taeil Kim | 인턴 | Agentic AI, Memory | kti5589@kaist.ac.kr |  |
| Yeonjun Hwang | 인턴 | LLM, Agentic AI |  |  |
| Dongmin Kim | 인턴 | Weight-Space Learning | kdm2337@kaist.ac.kr |  |
| Chanuk Lee | 인턴 | LLMs, Reinforcement Learning | tallyforce@kaist.ac.kr |  |
| Chaewoon Ki | 인턴 | LLM Reasoning, Agentic AI, LLM Application | befilledwith@kaist.ac.kr |  |
| Minjae Kim | 인턴 | LLMs, Agentic AI, RAG | kmj200392@korea.ac.kr |  |
| Geunhyoung Kim | 인턴 | Agentic AI, Attention Optimization, Tokenization and Embedding | skybluejacket@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 People의 Alumni 구획에 게시된 40명이다. 학위·과정과 진로는 게시 표기를 따랐다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jin Myung Kwak | KAIST, Ph.D., AI, 2026 |  |
| Bruno Anreis | KAIST, PhD, AI, 2025 | Postdoctoral Researcher at Oxford |
| Jaehong Yoon | KAIST, Ph.D, CS, 2023 | Assistant Professor at Nanyang Technological University |
| Seul Lee | KAIST, Ph.D., AI, 2026 | Research Scientist at NVIDIA |
| Minseon Kim | KAIST, PhD A.I., 2024 | Senior Researcher at Microsoft Research Montreal |
| Jay Heo | KAIST, Ph.D, CS, 2023 | CPO at Deepauto.ai |
| Jeff Willette | KAIST Ph.D., AI, 2026 | Research Scientist at NVIDIA |
| Wonyeong Jeong | KAIST, Ph.D, AI, 2023 |  |
| Hae Beom Lee | KAIST PhD., AI, 2022 | Assistant Professor at Korea University |
| Seanie Lee | KAIST, Ph.D, AI, 2026 | Research Scientist at Apple |
| Hayeon Lee | KAIST, Ph.D, CS, 2023 | Research Scientist at Meta GenAI |
| Ahra Jo | UNIST, Ph.D., CS, 2016 | LG AI Research |
| Wonbin Lee | KAIST, M.S, AI, 2026 |  |
| Jeonghwan Kim | Alumni (MS Students) | Research Scientist at KRAFTON |
| Eunji Ko | KAIST, M.S, AI, 2024 | Samsung Electronics |
| Hyunsu Rhee | KAIST, M.S. AI 2022 | NCSOFT |
| Eunyoung Hyung | KAIST, M.S., AI, 2021 | Research Scientist at Samsung Research |
| Tuan Nguyen | KAIST, M.S., CS, 2020 | ML Researcher at Jane Street |
| Suji Kim | KAIST, M.S, AI, 2026 | Researcher at SAIT |
| Joonho Ko | KAIST M.S. AI, 2025 |  |
| Hyeonjeong Ha | KAIST, M.S., AI, 2024 | PhD student at UIUC |
| Sunil Hwang | KAIST, M.S. AI 2022 | Defense Acquisition Program Administration |
| Hyewon Jeong | KAIST, M.S., CS, 2021 | Ph.D. student at MIT |
| Donghyun Na | KAIST, M.S., CS, 2019 | Research Scientist at KRAFTON |
| Minju Seo | KAIST, M.S., AI, 2025 | AI Scientist at LG AI Research |
| Jaewoo Lee | KAIST, M.S., AI, 2024 | PhD Student at UNC Chapel HIll |
| Seongjae Kang | KAIST, M.S. AI 2024 | Research Scientist at VUNO |
| Minyoung Song | KAIST, M.S., AI, 2021 | ML Engineer at Danngn |
| Divyam Madaan | KAIST, M.S., CS, 2021 | Ph.D. student at NYU |
| Moonsu Han | UNIST, M.S., CS, 2019 | Research Scientist at NCSOFT Language AI Research |
| Simon Aytes | KAIST, M.S., AI, 2025 | Senior Data Scientist at Penta Group |
| Sohyun An | KAIST, M.S., AI, 2024 | PhD student at UCLA (CS) |
| Haebin Seong | KAIST, M.S., AI, 2023 | CTO at AdaL (San Francisco) |
| Jaewoong Shin | KAIST, M.S., AI, 2021 | Research Scientist at Lunit |
| Jeongun Ryu | KAIST, M.S., CS, 2021 | Research Scientist at Lunit |
| Wuhyun Shin | Visiting Researcher, KAIST | Research Scientist at KakaoBrain |
| Byungjoo Kim | Alumni (Visiting Researchers) |  |
| Daeun Lee | Visiting Researcher, KAIST | PhD Student at UNC Chapel Hill |
| Jina Kim | Alumni (Visiting Researchers) | PhD Student at Princeton |
| Jaduk Suh | Alumni (Visiting Researchers) | MS Student at Stanford |

## 최근 5년 논문 목록

연구실 Publication의 2021–2026년 논문 140편이다. 2021년 항목 중 연도만으로 적힌 논문도 포함한다. 저자·제목·발표처는 연구실 표기이며, 괄호의 Oral·Spotlight·Highlight와 공동 기여 표시는 누리집 표기다.[^pubs]

**2026**

- Yanlai Yang, Minki Kang, Divyam Madaan, Sung Ju Hwang, and Mengye Ren. "On the Geometry and Latent-Space Composition of Hypernetwork-Generated LoRAs". *NeurIPS 2026*.
- Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang, Pavlo Molchanov, Yu-Chiang Frank Wang, and Byung-Kwan Lee. "Agent Explorative Policy Optimization for Multimodal Agentic Reasoning". *NeurIPS 2026*.
- Patara Trirat, Jay Heo, Heejun Lee, and Sung Ju Hwang. "Visual Anchoring for Scenario-Guided Forecasting". *NeurIPS 2026*.
- Wonbin Lee, Dongki Kim, and Sung Ju Hwang. "ES-Merging: Biological MLLM Merging via Embedding Space Signals". *NeurIPS 2026*.
- Nahyun Kim, Seul Lee, and Sung Ju Hwang. "Synthon Contrastive Learning for Synthesizable 3D Molecule Generation". *NeurIPS 2026*.
- Yumin Choi, Sangwoo Park, Minki Kang, Jinheon Baek, and Sung Ju Hwang. "PREPING: Building Agent Memory without Tasks". *NeurIPS 2026*.
- Seanie Lee, Sangwoo Park, Yumin Choi, Gyeongman Kim, Minki Kang, Jihun Yun, Dongmin Park, Jongho Park, and Sung Ju Hwang. "ThinkSafe: Self-Generated Safety Alignment for Reasoning Models". *NeurIPS 2026*.
- Sangwoo Park, Woongyeong Yeo, Seanie Lee, Yumin Choi, Hyomin Lee, Kangsan Kim, Jinheon Baek, Seong Joon Oh, and Sung Ju Hwang. "It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs". *NeurIPS 2026*.
- Patara Trirat, Jin Myung Kwak, Jay Heo, Heejun Lee, and Sung Ju Hwang. "Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning". *EMNLP 2026*.
- Jun Hyeong Kim, Dongki Kim, Yinhua Piao, and Sung Ju Hwang. "AdaPath: Query-Adaptive Path-Finding via Path-Bank for Multi-Hop Implicit Biomedical KGQA". *EMNLP 2026. DOI: <https://doi.org/10.18653/2026.emnlp-main.2395>[^adapath]*.
- Kangsan Kim, Minki Kang, Taeil Kim, Yanlai Yang, Mengye Ren, and Sung Ju Hwang. "Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents". *EMNLP 2026*.
- Hyomin Lee, Sangwoo Park, Yumin Choi, Sohyun An, Seanie Lee, and Sung Ju Hwang. "T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search". *EMNLP 2026 (Oral)*.
- Daegyu Sung, Yukyeong Lee, Geon Park, Yumin Choi, and Sung Ju Hwang. "Super Library Agent: Joint Generation and Maintenance of Multiple Applications Beyond the Single Codebase". *EMNLP Findings 2026. DOI: <https://doi.org/10.18653/2026.findings-emnlp.252>*.
- Woongyeng Yeo, Yumin Choi, Taekyung Ki, and Sung Ju Hwang. "HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents". *EMNLP Findings 2026*.
- Dohyeon Kim, Bedionita Soro, and Sung Ju Hwang. "Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts". *EMNLP Findings 2026*.
- Taeil Kim, Kangsan Kim, and Sung Ju Hwang. "Agentic Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory". *EMNLP Findings 2026*.
- Dong Bok Lee, Seanie Lee, Sangwoo Park, Minki Kang, Jinheon Baek, Dongki Kim, Dominik Wagner, Jiongdao Jin, Heejun Lee, Tobias Bocklet, Jinyu Wang, Jingjing Fu, Sung Ju Hwang, Jiang Bian, Lei Song. "Rethinking Reward Models for Multi-Domain Test-Time Scaling". *TMLR, June 2026*.
- Beomgyoung Kim and Sung Ju Hwang. "Learning from Adversity: Semantic-Aware Mask Refinement through Adversarial Perturbation". *ECCV 2026*.
- Youngwan Lee, Soojin Jang, Yoorhim Cho, Seunghwan Lee, Yong-Ju Lee and Sung Ju Hwang. "MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model". *ECCV 2026*.
- Sangwon Jang, Taekyung Ki, Jaehyeong Jo, Saining Xie, Jaehong Yoon and Sung Ju Hwang. "Self-Refining Video Sampling". *ICML 2026*.
- Chanuk Lee, Minki Kang and Sung Ju Hwang. "SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs". *ICML 2026*.
- Woongyeong Yeo, Kangsan Kim, Soyeong Jeong, Jinheon Baek and Sung Ju Hwang. "UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities". *ACL 2026 (Oral). DOI: <https://doi.org/10.18653/v1/2026.acl-long.177>*.
- Soyeong Jeong, Taehee Jung, Sung Ju Hwang, Joo-Kyung Kim and Dongyeop Kang. "When Thoughts Meet Facts: Reusable Reasoning for Long-Context LMs". *ACL 2026 (Findings). DOI: <https://doi.org/10.18653/v1/2026.findings-acl.81>*.
- Youngwan Lee, Kangsan Kim, Kwanyong Park, Ilchae Jung, Sujin Jang, Seanie Lee, Yong-Ju Lee, and Sung Ju Hwang. "HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model". *CVPR 2026 (Findings)*.
- Woongyeong Yeo, Kangsan Kim, Jaehong Yoon and Sung Ju Hwang. "WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning". *CVPR 2026 (Highlight)*.
- Taekyung Ki, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon and Sung Ju Hwang. "Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation". *CVPR 2026*.
- Bedionita Soro, Aoxuan Silvia Zhang, Bruno Andreis, Jaehyeong Jo, Song Chong and Sung Ju Hwang. "LS-Merge: Merging Language Models in Latent Space". *ICLR 2026*.
- Yumin Choi, Dongki Kim, Jinheon Baek and Sung Ju Hwang. "Multimodal Prompt Optimization: Why Not Leverage Multiple Modalities for MLLMs". *ICLR 2026*.
- Patara Trirat, Wonyong Jeong and Sung Ju Hwang. "Multi-View Encoders for Performance Prediction in LLM-Based Agentic Workflows". *ICLR 2026*.
- Sangwon Jang, Taekyung Ki, Jaehyeong Jo, Jaehong Yoon, Soo Ye Kim, Zhe Lin and Sung Ju Hwang. "Frame Guidance: Training-Free Guidance for Frame-Level Control in Video Diffusion Model". *ICLR 2026*.
- Minju Seo, Jinheon Baek, Seongyun Lee and Sung Ju Hwang. "Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning". *ICLR 2026*.

**2025**

- Minki Kang, Jongwon Jeong, Seanie Lee, Jaewoong Cho and Sung Ju Hwang. "Distilling LLM Agent into Small Models with Retrieval and Code Tools". *NeurIPS 2025 (Spotlight). DOI: <https://doi.org/10.52202/085713-3553>*.
- Jeffrey Willette, Heejun Lee and Sung Ju Hwang. "Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction". *NeurIPS 2025. DOI: <https://doi.org/10.52202/085713-0403>*.
- Jaehyeong Jo and Sung Ju Hwang. "Continuous Diffusion Model for Language Modeling". *NeurIPS 2025. DOI: <https://doi.org/10.52202/085713-3256>*.
- Dongki Kim, Wonbin Lee and Sung Ju Hwang. "Mol-LLaMA: Towards General Understanding of Molecules in Large Molecular Language Model". *NeurIPS 2025*.
- Yumin Choi, Jinheon Baek and Sung Ju Hwang. "System Prompt Optimization with Meta-Learning". *NeurIPS 2025. DOI: <https://doi.org/10.52202/085713-1854>*.
- Seanie Lee, Sangwoo Park, Dong Bok Lee, Dominik Wagner, Haebin Seong, Tobias Bocklet, Juho Lee and Sung Ju Hwang. "FedSVD: Adaptive Orthogonalization for Private Federated Learning with LoRA". *NeurIPS 2025. DOI: <https://doi.org/10.52202/085713-3998>*.
- Dong Bok Lee, Aoxuan Silvia Zhang, Byungjoo Kim, Junhyeon Park, Steven Adriaensen, Juho Lee, Sung Ju Hwang and Hae Beom Lee. "Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning". *NeurIPS 2025. DOI: <https://doi.org/10.52202/085713-5644>*.
- Simon A. Aytes, Jinheon Baek and Sung Ju Hwang. "Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching". *EMNLP 2025. DOI: <https://doi.org/10.18653/v1/2025.emnlp-main.1236>*.
- Joonho Ko, Jinheon Baek and Sung Ju Hwang. "Efficient Real-time Refinement of Language Model Text Generation". *EMNLP 2025. DOI: <https://doi.org/10.18653/v1/2025.emnlp-main.1753>*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang and Jong C. Park. "Database-Augmented Query Representation for Information Retrieval". *EMNLP 2025 (Oral). DOI: <https://doi.org/10.18653/v1/2025.emnlp-main.840>*.
- Minju Seo, Jinheon Baek, Seongyun Lee and Sung Ju Hwang. "Efficient Long Context Language Model Retrieval with Compression". *ACL 2025. DOI: <https://doi.org/10.18653/v1/2025.acl-long.740>*.
- Soyeong Jeong, Kangsan Kim, Jinheon Baek and Sung Ju Hwang. "VideoRAG: Retrieval-Augmented Generation over Video Corpus". *ACL Findings 2025. DOI: <https://doi.org/10.18653/v1/2025.findings-acl.1096>*.
- Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee and Sung Ju Hwang. "SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models". *ACL Findings 2025. DOI: <https://doi.org/10.18653/v1/2025.findings-acl.105>*.
- Patara Trirat, Wonyong Jeong and Sung Ju Hwang. "AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML". *ICML 2025*.
- Dongwoo Lee, Dong Bok Lee, Steven Adriaensen, Juho Lee, Sung Ju Hwang, Frank Hutter, Seon Joo Kim and Hae Beom Lee. "Bayesian Neural Scaling Laws Extrapolation with Prior-Fitted Networks". *ICML 2025*.
- Kangsan Kim, Geon Park, Youngwan Lee, Woongyeong Yeo, Sung Ju Hwang. "VideoICL: Confidence-based Iterative In-context Learning for Out-of-Distribution Video Understanding". *CVPR 2025. DOI: <https://doi.org/10.1109/cvpr52734.2025.00313>*.
- Sangwon Jang, June Suk Choi, Jaehyeong Jo, Kimin Lee, Sung Ju Hwang. "Silent Branding Attack: Trigger-free Data Poisoning Attack on Text-to-Image Diffusion Models". *CVPR 2025. DOI: <https://doi.org/10.1109/cvpr52734.2025.00768>*.
- Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, Sung Ju Hwang. "ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models". *NAACL 2025. DOI: <https://doi.org/10.18653/v1/2025.naacl-long.342>*.
- Heejun Lee, Geon Park, Youngwan Lee, Jaduk Suh, Jina Kim, Wonyong Jeong, Bumsik Kim, Hyemin Lee, Myeongjae Jeon, Sung Ju Hwang. "A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention". *ICLR 2025*.
- Seanie Lee, Haebin Seong, Dong Bok Lee, Minki Kang, Xiaoyin Chen, Dominik Wagner, Yoshua Bengio, Juho Lee, Sung Ju Hwang. "HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models". *ICLR 2025*.
- Seanie Lee, Minsu Kim, Lynn Cherif, David Dobre, Juho Lee, Sung Ju Hwang, Kenji Kawaguchi, Gauthier Gidel, Yoshua Bengio, Nikolay Malkin, Moksh Jain. "Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning". *ICLR 2025*.
- Jeffrey Willette, Heejun Lee, Youngwan Lee, Myeongjae Jeon, Sung Ju Hwang. "Training Free Exponential Context Extension via Cascading KV Cache". *ICLR 2025*.
- Bedionita Soro, Bruno_Andreis, Hayeon Lee, Wonyong Jeong, Song Chong, Frank Hutter, Sung Ju Hwang. "Diffusion-based Neural Network Weights Generation". *ICLR 2025*.

**2024**

- Youngwan Lee, Kwanyong Park, Yoorhim Cho, Yong-Ju Lee, Sung Ju Hwang. "KOALA: Empirical Lessons Toward Memory-Efficient and Fast Diffusion Models for Text-to-Image Synthesis". *NeurIPS 2024*.
- Bruno Andreis, Soro Bedionita, Philip Torr, Sung Ju Hwang. "Set-based Neural Network Encoding Without Weight Tying". *NeurIPS 2024*.
- Minki Kang, Sung Ju Hwang, Gibbeum Lee, Jaewoong Cho. "Latent Paraphrasing: Perturbation on Layers Improves Knowledge Injection in Language Models". *NeurIPS 2024. DOI: <https://doi.org/10.52202/079017-3803>*.
- Sangwon Jang\*, Jaehyeong Jo\*, Kimin Lee, Sung Ju Hwang. "Identity Decoupling for Multi-Subject Personalization of Text-to-Image Models". *NeurIPS 2024. DOI: <https://doi.org/10.52202/079017-3200>*.
- Minju Seo, Jinheon Baek, Sung Ju Hwang. "Rethinking Code Refinement: Learning to Judge Code Efficiency". *EMNLP 2024. DOI: <https://doi.org/10.18653/v1/2024.findings-emnlp.645>*.
- Jaewoo Lee, Boyang Li, Sung Ju Hwang. "Concept-skill Transferability-based Data Selection for Large Vision-Language Models". *EMNLP 2024. DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.291>*.
- Jaewoo Lee, Jaehong Yoon, Wonjae Kim, Yunji Kim and Sung Ju Hwang. "STELLA: Continual Audio-Video Pre-training with SpatioTemporal Localized Alignment". *ICML 2024*.
- Jaehyeong Jo and Sung Ju Hwang. "Generative Modeling on Manifolds Through Mixture of Riemannian Diffusion Processes". *ICML 2024*.
- Jaehyeong Jo, Dongki Kim and Sung Ju Hwang. "Graph Generation with Diffusion Mixture". *ICML 2024*.
- Seul Lee, Seanie Lee, Kenji Kawaguchi and Sung Ju Hwang. "Drug Discovery with Dynamic Goal-aware Fragments". *ICML 2024. DOI: <https://doi.org/10.48550/arxiv.2310.00841>*.
- Daeun Lee, Jaehong Yoon and Sung Ju Hwang. "BECoTTA: Input-dependent Online Blending of Experts for Continual Test-time Adaptation". *ICML 2024*.
- Sunil Hwang, Jaehong Yoon, Youngwan Lee and Sung Ju Hwang. "EVEREST: Efficient Masked Video Autoencoder by Removing Redundant Spatiotemporal Tokens". *ICML 2024*.
- Ruochen Wang, Sohyun An, Minhao Cheng, Tianyi Zhou, Sung Ju Hwang and Cho-Jui Hsieh. "One Prompt is not Enough: Automated Construction off a Mixture-of-Experts Prompts". *ICML 2024*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang and Jong C. Park. "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity". *NAACL 2024. DOI: <https://doi.org/10.18653/v1/2024.naacl-long.389>*.
- Yujin Kim, Jaehong Yoon, Seonghyeon Ye, Sangmin Bae, Namgyu Ho, Sung Ju Hwang and Se-Young Yun. "Carpe diem: On the Evaluation of World Knowledge in Lifelong Language Models". *NAACL 2024. DOI: <https://doi.org/10.18653/v1/2024.naacl-long.302>*.
- Beomgyoung Kim, Joonsang Yu and Sung Ju Hwang. "ECLIPSE: Efficient Continual Learning in Panoptic Segmentation with Visual Prompt Tuning". *CVPR 2024. DOI: <https://doi.org/10.1109/cvpr52733.2024.00322>*.
- Heejun Lee, Jina Kim, Jeffrey Willette, and Sung Ju Hwang. "SEA: Sparse Linear Attention with Estimated Attention Mask". *ICLR 2024*.
- Sohyun An, Hayeon Lee, Jaehyeong Jo, Seanie Lee, Sung Ju Hwang. "DiffusionNAG: Predictor-guided Neural Architecture Generation with Diffusion Models". *ICLR 2024*.
- Dong Bok Lee\*, Seanie Lee\*, Joonho Ko, Kenji Kawaguchi, Juho Lee, Sung Ju Hwang. "Self-Supervised Dataset Distillation for Transfer Learning". *ICLR 2024*.
- Haeyong Kang, Jaehong Yoon, DaHyun Kim, Sung Ju Hwang and Chang D. Yoo. "Progressive Fourier Neural Representation for Sequential Video Compilation". *ICLR 2024*.

**2023**

- Jinheon Baek, Soyeong Jeong, Minki Kang, Jong C. Park and Sung Ju Hwang. "Learning to Verify Knowledge-Augmented Language Models". *EMNLP 2023*.
- Hayeon Lee, Rui Hou, Jongpil Kim, Davis Liang, Hongbo Zhang, Sung Ju Hwang, Alexander Min. "Co-training and Co-distillation for Quality Improvement and Compression of Language Models". *Findings of EMNLP 2023*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, Jong C. Park. "Test-Time Self-Adaptive Small Language Models for Question Answering". *Findings of EMNLP 2023*.
- Minki Kang, Seanie Lee, Jinheon Baek, Kenji Kawaguchi and Sung Ju Hwang. "Knowledge-Augmented Reasoning Distillation for Small Language Models in Knowledge-Intensive Tasks". *NeurIPS 2023*.
- Hyeonjeong Ha, Minseon Kim and Sung Ju Hwang. "Generalizable Lightweight Proxy for Robust NAS against Diverse Perturbations". *NeurIPS 2023*.
- Minseon Kim, Hyeonjeong Ha, Sooel Son and Sung Ju Hwang. "Effective Targeted Attacks for Adversarial Self-Supervised Learning". *NeurIPS 2023*.
- Sujin Jang, Dae Ung Jo, Sung Ju Hwang, Dongwook Lee, Daehyun Ji. "STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection". *NeurIPS 2023*.
- Jaewoong Lee, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon, Yunji Kim, Jin-Hwa Kim, Jung-Woo Ha and Sung Ju Hwang. "Text-Conditioned Sampling Framework for Text-to-Image Generation with Masked Generative Models". *ICCV 2023. DOI: <https://doi.org/10.1109/iccv51070.2023.02125>*.
- Minki Kang, Wooseok Han, Sung Ju Hwang and Eunho Yang. "ZET-Speech: Zero-shot adaptive Emotion-controllable Text-to-Speech Synthesis with Diffusion and Style-based Models". *Interspeech 2023. DOI: <https://doi.org/10.21437/interspeech.2023-754>*.
- Jinheon Baek, Alham Fikri Aji, Jens Lehmann and Sung Ju Hwang. "Direct Fact Retrieval from Knowledge Graphs without Entity Linking". *ACL 2023 (long paper). DOI: <https://doi.org/10.18653/v1/2023.acl-long.558>*.
- Jinmyung Kwak, Minseon Kim, and Sung Ju Hwang. "Language Detoxification with Attribute-Discriminative Latent Space". *ACL 2023 (long paper). DOI: <https://doi.org/10.18653/v1/2023.acl-long.565>*.
- Hayeon Lee, Rui Hou, Jongpil Kim, Davis Liang, Sung Ju Hwang and Alexander Min. "A Study on Knowledge Distillation from Weak Teacher for Scaling Up Pre-trained Language Model". *Findings of ACL 2023*.
- Soyeong Jeong, Jinheon Baek, Sung Ju Hwang and Jong C. Park. "Phrase Retrieval for Open Domain Conversational Question Answering with Conversational Dependency Modeling via Contrastive Learning". *Findings of ACL 2023. DOI: <https://doi.org/10.18653/v1/2023.findings-acl.374>*.
- Seul Lee, Jaehyeong Jo, Sung Ju Hwang. "Exploring Chemical Space with Score-based Out-of-distribution Generation". *ICML 2023*.
- Jeffrey Willette\*, Seanie Lee\*, Bruno Andreis, Kenji Kawaguchi, Juho Lee, Sung Ju Hwang. "Scalable Set Encoding with Universal Mini-Batch Consistency and Unbiased Full Set Gradient Approximation". *ICML 2023*.
- Jinheon Baek, Wonyong Jeong, Jiongdao Jin, Jaehong Yoon, Sung Ju Hwang. "Personalized Subgraph Federated Learning". *ICML 2023*.
- Byungjoo Kim, Suyoung Lee, Seanie Lee, Sooel Son, Sung Ju Hwang. "Margin-based Neural Network Watermarking". *ICML 2023*.
- Jaehong Yoon, Sung Ju Hwang, and Yue Cao. "Continual Learners are Incremental Model Generalizers". *ICML 2023*.
- Taesik Gong, Yewon Kim, Adiba Orzikulova, Yunxin Liu, Sung Ju Hwang. "DAPPER: Label-Free Performance Estimation after Personalization for Heterogeneous Mobile Sensing". *UbiComp (IMWUT) 2023*.
- Beomyoung Kim, Joonhyun Jeong, Dongyoon Han, Sung Ju Hwang. "The Devil is in the Points: Weakly Semi-Supervised Instance Segmentation via Point-Guided Mask Representation". *CVPR 2023. DOI: <https://doi.org/10.1109/cvpr52729.2023.01093>*.
- Minki Kang, Dongchan Min and Sung Ju Hwang. "Any-speaker Adaptive Text-To-Speech Synthesis with Diffusion Models". *ICASSP 2023*.
- Soyeong Jeong, Jinheon Baek, Sung Ju Hwang, Jong C. Park, E. "Realistic Conversational Question Answering with Answer Selection based on Calibrated Confidence and Uncertainty Measurement". *ACL 2023. DOI: <https://doi.org/10.18653/v1/2023.eacl-main.35>*.
- Hayeon Lee\*, Sohyun An\*, Minseon Kim and Sung Ju Hwang. "Meta-prediction Model for Distillation-Aware NAS on Unseen Datasets". *ICLR 2023*.
- Seanie Lee, Minki Kang, Juho Lee, Sung Ju Hwang, Kenji Kawaguchi. "Self-Distillation for Further Pre-training of Transformers". *ICLR 2023*.
- Heejun Lee, Minki Kang, Youngwan Lee and Sung Ju Hwang. "Sparse Token Transformers with Attention Back Tracking". *ICLR 2023*.
- Dong Bok Lee\*, Seanie Lee\*, Kenji Kawaguchi, Yunji Kim, Jihwan Bang, Jung-Woo Ha and Sung Ju Hwang, (\*: equal contribution). "Self-Supervised Set Representation Learning for Unsupervised Meta-Learning". *ICLR 2023*.
- Youngwan Lee\*, Jeffrey Ryan Willete\*, Jonghee Kim, Juho Lee and Sung Ju Hwang (\*: equal contribution). "Exploring the Role of Mean Teacher in Self-supervised Masked Auto-Encoders". *ICLR 2023*.
- Haeyong Kang, Jaehong Yoon, Sultan Rizky, Hikmawan Madjid, Sung Ju Hwang and Chang D. Yoo. "On the Soft-Subnetwork for Few-Shot Class Incremental Learning". *ICLR 2023*.
- Minseon Kim, Jihoon Tack, Jinwoo Shin, and Sung Ju Hwang. "Rethinking the Entropy of Instance in Adversarial Training". *SaTML 2023. DOI: <https://doi.org/10.1109/satml54575.2023.00029>*.

**2022**

- Hoyong Jeong, Suyoung Lee, Sung Ju Hwang and Sooel Son. "Learning to Generate Inversion-Resistant Model Explanations". *NeurIPS 2022*.
- Seanie Lee\*, Bruno Andreis\*, Kenji Kawaguchi, Juho Lee, Sung Ju Hwang (\*: equal contribution). "Set-based Meta-Interpolation for Few-Task Meta-Learning". *NeurIPS 2022*.
- Wonyong Jeong and Sung Ju Hwang. "Factorized-FL: Personalized Federated Learning with Parameter Factorization & Similarity Matching". *NeurIPS 2022*.
- Dongki Kim\*, Jinheon Baek\*, Sung Ju Hwang (\*: equal contribution). "Graph Self-supervised Learning with Accurate Discrepancy Learning". *NeurIPS 2022*.
- Bruno Andreis, Seanie Lee, A. Tuan Nguyen, Juho Lee, Eunho Yang, Sung Ju Hwang. "Set Based Stochastic Subsampling". *ICML 2022*.
- Jaehyeong Jo (＊), Seul Lee (＊), Sung Ju Hwang (＊: equal contribution). "Score-based Generative Modeling of Graphs via the System of Stochastic Differential Equations". *ICML 2022. DOI: <https://doi.org/10.48550/arxiv.2202.02514>*.
- Haeyong Kang, Rusty J. L. Mina, Sultan R. H. Madjid, Jaehong Yoon, Chang D. Yoo, Sung Ju Hwang, and Mark Hasegawa-Johnson. "Forget-free Continual Learning with Winning Subnetworks". *ICML 2022*.
- Jaehong Yoon\*, Geon Park\*, Wonyong Jeong, Sung Ju Hwang (\*: equal contribution). "Bitwidth Heterogeneous Federated Learning with Progressive Weight Dequantization". *ICML 2022*.
- Minki Kang\*, Jinheon Baek\*, Sung Ju Hwang (\*: equal contribution). "KALA: Knowledge-Augmented Language Model Adaptation". *NAACL 2022. DOI: <https://doi.org/10.18653/v1/2022.naacl-main.379>*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang and Jong C. Park. "Augmenting Document Representations for Dense Retrieval with Interpolation and Perturbation". *ACL 2022. DOI: <https://doi.org/10.18653/v1/2022.acl-short.48>*.
- Youngwan Lee, Jonghee Kim, Jeffrey Willette, and Sung Ju Hwang. "MPViT : Multi-Path Vision Transformer for Dense Prediction". *CVPR 2022. DOI: <https://doi.org/10.1109/cvpr52688.2022.00714>*.
- Divyam Madaan, Jaehong Yoon, Yuanchun Li, Yunxin Liu and Sung Ju Hwang. "Rethinking the Representational Continuity: Towards Unsupervised Continual Learning". *ICLR 2022 (oral)*.
- Hae Beom Lee, Hayeon Lee, JaeWoong Shin, Eunho Yang, Timothy Hospedales and Sung Ju Hwang. "Online Hyperparameter Meta-Learning with Hypergradient Distillation". *ICLR 2022*.
- Youngmin Oh, Jinwoo Shin, Eunho Yang and Sung Ju Hwang. "Model-augmented Prioritized Experience Replay". *ICLR 2022*.
- Jaehong Yoon, Divyam Madaan, Eunho Yang and Sung Ju Hwang. "Online Coreset Selection for Rehearsal-based Continual Learning". *ICLR 2022*.
- Jeffrey Ryan Willette, Hae Beom Lee, Juho Lee and Sung Ju Hwang. "Meta Learning Low Rank Covariance Factors for Energy Based Deterministic Uncertainty". *ICLR 2022*.
- Seanie Lee, Hae Beom Lee, Juho Lee and Sung Ju Hwang. "Sequential Reptile: Inter-Task Gradient Alignment for Multilingual Learning". *ICLR 2022*.
- Taewook Nam, Shao-Hua Sun, Karl Pertsch, Sung Ju Hwang and Joseph J Lim. "Skill-based Meta-Reinforcement Learning". *ICLR 2022*.
- Jihoon Tack, Sihyun Yu, Jongheon Jeong, Minseon Kim, Sung Ju Hwang, Jinwoo Shin. "Consistency Regularization for Adversarial Robustness". *AAAI 2022. DOI: <https://doi.org/10.1609/aaai.v36i8.20817>*.
- Joonhyung Park, June Yong Yang, Jinwoo Shin, Sung Ju Hwang, Eunho Yang. "Saliency Grafting: Innocuous Attribution-Guided Mixup with Calibrated Label Mixing". *AAAI 2022. DOI: <https://doi.org/10.1609/aaai.v36i7.20766>*.

**2021**

- Wonyong Jeong\*, Hayeon Lee\*, Geon Park\*, Eunyoung Hyung, Jinheon Baek and Sung Ju Hwang. "Task-Adaptive Neural Network Search with Meta-Contrastive Learning". *NeurIPS 2021 (spotlight)*.
- Hayeon Lee\*, Sewoong Lee\*, Song Chong and Sung Ju Hwang. "Hardware-adaptive Efficient Latency Prediction for NAS via Meta-Learning". *NeurIPS 2021 (spotlight)*.
- Andreis Bruno, Jeffrey Ryan Willette, Juho Lee and Sung Ju Hwang. "Mini-Batch Consistent Slot Set Encoder for Scalable Set Encoding". *NeurIPS 2021*.
- Jaehyeong Jo\*, Jinheon Baek\*, Seul Lee\*, Dongki Kim, Minki Kang and Sung Ju Hwang. "Edge Representation Learning with Hypergraphs". *NeurIPS 2021*.
- Soojung Yang, Doyeong Hwang, Seul Lee, Seongok Ryu and Sung Ju Hwang. "Hit and Lead Discovery with Explorative RL and Fragment-based Molecule Generation". *NeurIPS 2021*.
- Jung Hyun Lee, Jihun Yun, Sung Ju Hwang and Eunho Yang. "Cluster-Promoting Quantization with Bit-Drop for Minimizing Network Quantization Loss". *ICCV 2021. DOI: <https://doi.org/10.1109/iccv48922.2021.00532>*.
- Jongmin Yoon, Sung Ju Hwang, Juho Lee. "Adversarial Purification with Score-based Generative Models". *ICML 2021*.
- Jaewoong Shin, Hae Beom Lee, Boqing Gong, Sung Ju Hwang. "Large-Scale Meta-Learning with Continual Trajectory Shifting". *ICML 2021*.
- Divyam Madaan, Jinwoo Shin, Sung Ju Hwang. "Learning to Generate Noise for Robustness Against Multiple Perturbations". *ICML 2021*.
- Dongchan Min, Dong Bok Lee, Eunho Yang, Sung Ju Hwang. "Meta-StyleSpeech : Multi-Speaker Adaptive Text-to-Speech Generation". *ICML 2021*.
- Jaehong Yoon\*, Wonyong Jeong\*, Giwoong Lee, Eunho Yang, Sung Ju Hwang. "Federated Continual Learning with Weighted Inter-client Transfer". *ICML 2021*.
- Jinheon Baek, Minki Kang and Sung Ju Hwang. "Accurate Learning of Graph Representations with Graph Multiset Pooling". *ICLR 2021*.
- Hayeon Lee, Eunyoung Hyung and Sung Ju Hwang. "Rapid Neural Architecture Search by Learning to Generate Graphs from Datasets". *ICLR 2021*.
- Seanie Lee, Dong Bok Lee and Sung Ju Hwang. "Contrastive Learning with Adversarial Perturbations for Conditional Text Generation". *ICLR 2021*.
- Wonyong Jeong, Jaehong Yoon, Eunho Yang and Sung Ju Hwang. "Federated Semi-Supervised Learning with Inter-Client Consistency & Disjoint Learning". *ICLR 2021*.
- Youngmin Oh, Kimin Lee, Jinwoo Shin Eunho Yang and Sung Ju Hwang. "Learning to Sample with Local and Global Contexts from Experience Replay Buffers". *ICLR 2021*.
- Tehrim Yoon, Sumin Shin, Sung Ju Hwang and Eunho Yang. "FedMix: Approximation of Mixup under Mean Augmented Federated Learning". *ICLR 2021*.

## 과제

연구실 Project에 게시된 과제 가운데 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 4건이다. 과제명·지원기관·기간은 게시 표기다.[^projects]

- Penetration Security Testing of ML Model Vulnerabilities and Defense (지원 Institution for Information & Communications & Technology Promotion (IITP); 기간 2020-04–2027-12)
- Center for Applied Research in Artificial Intelligence (CARAI) (지원 ADD (Agency for Defense Development); 기간 2019-12–2025-12)
- Massive Machine Learning – KAIST MARS AI Integrated Research Center (지원 National Research Foundation; 기간 2018-08–2024-02)
- Deep Learning Based AI for Learning and Inference in Drone Technology (지원 National Research Foundation; 기간 2020-04–2023-12)

## 수상과 선정

연구실 News가 2021년 10월 13일–2026년 10월 13일에 게시한 선정 2건이다. 같은 Apple 장학 선정을 알린 공지 두 건은 하나로 합쳤다.[^news]

- 2022-12-14 · Seanie Lee가 2023 Apple Scholars in AI ML PhD fellowship 수혜자로 선정되었다(2023-03-03에 같은 선정을 다시 알림)
- 2021-10-27 · Haebom Lee가 2021 Google PhD fellowship을 받았다

## 소식

연구실 News의 논문 채택·게재 승인 공지 29건이다. 날짜는 연구실 News의 게시일이다. Home이 다른 날짜로 알린 NeurIPS 2026과 CVPR 2025 두 공지는 두 날짜를 함께 표시했다.[^news][^home]

- 2026-08-20 (NEWS) / 2026-09-24 (HOME) · NeurIPS 2026에 논문 9편이 채택되었다
- 2026-08-20 · EMNLP 2026에 논문 8편이 채택되었다 (게시 표기: 1 Oral, 3 Main and 4 Findings)
- 2026-06-26 · TMLR에 논문 1편이 게재 승인되었다
- 2026-06-18 · ECCV 2026에 논문 2편이 채택되었다
- 2026-05-01 · ICML 2026에 논문 2편이 채택되었다
- 2026-02-21 · ACL 2026에 논문 2편이 채택되었다 (게시 표기: 1 Findings)
- 2026-02-21 · CVPR 2026에 논문 3편이 채택되었다 (게시 표기: 1 Highlight and 1 Findings)
- 2026-02-10 · ICLR 2026에 논문 5편이 채택되었다
- 2025-09-26 · NeurIPS 2025에 논문 7편이 채택되었다
- 2025-09-26 · EMNLP 2025에 논문 3편이 채택되었다
- 2025-09-26 · ACL 2025에 논문 3편이 채택되었다
- 2025-09-26 · ICML 2025에 논문 2편이 채택되었다
- 2025-03-01 (NEWS) / 2025-03-04 (HOME) · CVPR 2025에 논문 2편이 채택되었다
- 2025-01-23 · ICLR 2025에 논문 5편이 채택되었다
- 2025-01-23 · NAACL 2025에 논문 1편이 채택되었다
- 2024-09-26 · EMNLP 2024에 논문 2편이 채택되었다
- 2024-09-26 · NeurIPS 2024에 논문 4편이 채택되었다
- 2024-05-24 · ICML 2024에 논문 7편이 채택되었다
- 2024-01-25 · ICLR 2024에 논문 4편이 채택되었다
- 2023-12-13 · EMNLP 2023에 논문 3편이 채택되었다
- 2023-12-13 · NeurIPS 2023에 논문 4편이 채택되었다
- 2023-07-13 · ICCV 2023에 논문 1편이 채택되었다
- 2023-05-17 · Interspeech 2023에 논문 1편이 채택되었다
- 2023-05-05 · ACL 2023에 논문 3편이 채택되었다
- 2023-04-26 · ICML 2023에 논문 5편이 채택되었다
- 2023-01-21 · ICLR 2023에 논문 6편이 채택되었다
- 2022-09-15 · NeurIPS 2022에 논문 4편이 채택되었다
- 2022-05-26 · ICML 2022에 논문 4편이 채택되었다
- 2022-01-21 · ICLR 2022에 논문 7편이 채택되었다

## 연락과 위치

- 교수 이메일: sungju.hwang@kaist.ac.kr[^people]
- 전산학부에 게시된 전화번호: 3576[^csprof]
- 사무실: KAIST AI 서울 양재캠퍼스 702호[^contact][^gsai]
- 주소: 서울특별시 서초구 태봉로 108[^contact]
- 교수 개인 누리집의 사무실: KAIST 전산학부 E3-1 1427호, 대전광역시 유성구 대학로 291[^prof]
[^gsai]: KAIST 김재철AI대학원, 전임교수 황성주 소개. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-11-09.
[^people]: MLAI, People, 교수 소개·구성원·Alumni. <https://www.mlai-kaist.com/people> 관측 2026-11-09.
[^pubs]: MLAI, Publication, 논문 목록. <https://www.mlai-kaist.com/publication> 관측 2026-11-09. 덧붙인 DOI와 2021년 시점은 OpenAlex 교수 저작 목록 및 Crossref의 해당 논문 서지에 따른다. <https://openalex.org/A5070302452> <https://api.crossref.org/works/10.1109/iccv48922.2021.00532> <https://api.crossref.org/works/10.18653/v1/2021.acl-long.434> 관측 2026-11-11.
[^projects]: MLAI, Project, 과제명·지원기관·기간. <https://www.mlai-kaist.com/project> 관측 2026-11-09.
[^news]: MLAI, News, 논문 채택과 선정 공지. <https://www.mlai-kaist.com/news> 관측 2026-11-09.
[^home]: MLAI, Home, Recent News. <https://www.mlai-kaist.com/> 관측 2026-11-09.
[^contact]: MLAI, Contact, 사무실·주소. <https://www.mlai-kaist.com/contact> 관측 2026-11-11.
[^csprof]: KAIST 전산학부, 황성주 교수 소개. <https://cs.kaist.ac.kr/people/view?idx=562&kind=faculty&menu=160> 관측 2026-11-11.
[^prof]: 황성주, 교수 개인 누리집, Brief Bio·Research Interests·Work·Contact. <http://www.sungjuhwang.com/> 관측 2026-11-11.
[^adapath]: J. H. Kim, D. Kim, Y. Piao, S. J. Hwang, AdaPath: Query-Adaptive Path-Finding via Path-Bank for Multi-Hop Implicit Biomedical KGQA, Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (2026). <https://doi.org/10.18653/2026.emnlp-main.2395> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.18653/2026.emnlp-main.2395> 관측 2026-11-11.
[^p1]: S. Jeong 외, D. Kang, Findings of the Association for Computational Linguistics: ACL (Findings of ACL) (2026). <https://doi.org/10.18653/v1/2026.findings-acl.81> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p2]: M. Kang 외, S. J. Hwang, neural information processing systems (2025). <https://doi.org/10.52202/085713-3553> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p3]: J. Jo, S. J. Hwang, neural information processing systems (2025). <https://doi.org/10.52202/085713-3256> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p4]: S. Lee 외, S. J. Hwang, neural information processing systems (2025). <https://doi.org/10.52202/085713-3998> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p5]: B. Kim, J. Yu, S. J. Hwang, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2024). <https://doi.org/10.1109/cvpr52733.2024.00322> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p6]: S. Lee, S. Lee, K. Kawaguchi, S. J. Hwang, arXiv, ICML 2024 표기 (2023). <https://doi.org/10.48550/arxiv.2310.00841> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2310.00841> 관측 2026-11-11.
[^p7]: J. Jo, S. Lee, S. J. Hwang, arXiv; 연구실 ICML 2022 표기 (2022). <https://doi.org/10.48550/arxiv.2202.02514> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.
[^p8]: J. Tack 외, J. Shin, Proceedings of the AAAI Conference on Artificial Intelligence (2022). <https://doi.org/10.1609/aaai.v36i8.20817> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070302452> 관측 2026-11-11.

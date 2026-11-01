# Users & Information Lab. (U&I Lab)

**KAIST 전산학부 · 오혜연 교수, 석좌교수(Endowed Chair Professor)**

- 영문 이름: Users & Information Lab.; 학과 표기 Users and Information Lab[^home][^lab]
- 대분야: 컴퓨팅·AI, 인문·사회·경제
- 태그: 자연어 처리·계산언어학[^home][^p2], 대형 언어 모델[^home], 책임 있는 AI·공정성[^home], 계산 사회과학[^faculty][^p6], 설명 가능한 AI(XAI)[^home][^p7], 그래프 기계학습·지식 그래프[^p8]
- 홈페이지: <https://uilab.kr/>
- 교수: 오혜연(Alice Oh)[^faculty][^members]

> 언어와 문화에 따라 인공지능의 이해·판단이 어떻게 달라지는지 측정하고, 여러 언어와 공동체를 고려하는 언어 기술을 만드는 연구실이다.[^home]

## 무엇을 연구하나

U&I Lab은 **자연어 처리(Natural Language Processing, 사람이 쓰는 언어를 컴퓨터로 분석·이해·생성하는 기술)**와 **계산 사회과학(대규모 자료와 계산 방법으로 사회 현상을 연구하는 분야)**을 함께 연구한다. 중심 대상은 대형 언어 모델(LLM, Large Language Model: 많은 언어 자료를 학습해 글을 이해하고 만들어 내는 인공지능 모델)이다. 서로 다른 언어·문화·공동체에서 이 모델이 사람을 어떻게 이해하는지 드러내는 평가 자료와 방법을 만들고, 문화적 지식·안전·사회적 맥락을 고려하는 방법을 개발한다.[^home]

첫째 관심은 **언어와 문화에 따른 성능의 차이**다. BLEnD는 여러 지역 사람들이 일상에서 아는 지식을 묻는 벤치마크(공통 기준으로 성능을 비교하기 위한 평가 자료와 절차)다. 인터넷에서 쉽게 모으기 어려운 생활 지식을 질문으로 구성해 문화권별 차이를 살핀다.[^p1] 또 코드 전환(한 문장이나 대화 안에서 서로 다른 언어를 번갈아 쓰는 현상)을 모델의 추론에 활용한다. 비영어 입력에서 영어로 점차 옮겨 가는 예시를 주어, 비영어 입력과 영어 중심의 내부 표현을 연결하는 방법을 연구한다.[^p2]

둘째는 **평가 방법과 공정성**이다. LLM-as-an-Interviewer는 평가하는 모델이 후속 질문과 피드백을 주는 면접식 평가다. 고정된 첫 답변뿐 아니라 피드백을 받은 뒤의 적응과 추가 질문에 대한 대응을 살핀다. 시작 질문을 동적으로 바꾸어 데이터 오염(평가할 문항이 사전학습 자료 등에 이미 포함되는 현상)도 줄이려 한다.[^p3] KoBBQ는 미국에서 만든 편향 평가 자료를 한국어로 번역하는 데서 그치지 않고, 한국의 문화와 고정관념에 맞게 항목을 바꾸거나 새로 구성하는 틀을 제안했다.[^p4]

셋째는 **교육과 사회 현상을 위한 언어 기술**이다. DREsS는 외국어로 영어를 배우는 학습자의 작문을 평가 기준표의 항목에 따라 채점할 수 있도록 자료를 구축하고, 글을 변형해 학습 자료를 늘리는 방법을 제안한다.[^p5] 법안 연구에서는 법안의 문구가 그대로 복사되거나 순서와 표현이 바뀌는 관계를 분류하고, 합성 자료를 먼저 쓰고 사람이 주석을 단 자료를 이어 써서 언어 모델을 미세조정(기존에 학습한 모델을 특정 자료나 목적에 맞춰 추가 학습하는 과정)한다. 이를 통해 문서의 일부와 법안 전체 수준에서 유사성을 측정한다.[^p6]

넷째는 **모델 내부의 작동과 관계망 학습 방법**이다. 추론의 문제 설정·목표 분해·연역 같은 단계가 표현 공간(입력 정보를 벡터로 나타내 배치한 모델 내부의 공간)에서 구별되는지 살핀다. 어텐션(입력 요소 사이의 관련도를 가중치로 반영하는 계산)을 가리는 개입으로 앞선 추론 문맥의 영향도 분석한다.[^p7] 그래프(대상과 그 사이의 관계를 점과 연결로 나타낸 구조) 연구에서는 하위 그래프(전체 그래프 일부의 노드와 연결)를 새 그래프의 노드로 바꾼다. 그래프 신경망(그래프의 연결을 이용해 대상과 주변 정보를 학습하는 계산 모형)을 이 새 구조에 적용해 관계망 일부의 특징을 배우면서, 전체와 부분의 구조를 함께 반영하는 방법을 개발한다.[^p8]

## 주요 연구 주제

### 1. 여러 언어와 문화를 고려하는 언어 모델

생활 지식의 문화권별 평가, 비영어 입력과 영어 중심 추론의 연결, 한국어·한자 문헌을 위한 언어 자원과 번역을 연구한다. 문화와 언어에 따른 차이를 평가 자료로 드러내고, 언어 사용을 바꾸는 방법까지 다룬다.[^home][^p1][^p2][^demos]

### 2. 동적 평가와 편향·안전성

후속 질문과 피드백을 쓰는 평가, 문화에 맞게 재구성한 편향 평가, 유해한 내용과 사회적 가치에 관한 언어 모델의 판단을 연구한다. 평가 자료 자체가 어떤 문화와 사용 상황을 반영하는지도 연구 대상이다.[^home][^p3][^p4]

### 3. 교육 지원과 계산 사회과학

외국어 작문 학습을 위한 채점·상호작용 자료와 교육용 인공지능을 연구한다. 사회과학에서는 법안 사이의 관계, 온라인 공격 행동, 입법 과정의 로비를 언어 자료로 분석한다.[^home][^p5][^p6]

### 4. 언어 모델의 해석과 그래프 표현 학습

추론 단계와 내부 표현의 관계, 문화적 편향이 모델 내부에 나타나는 방식을 연구한다. 대형 그래프의 일부를 새 노드로 바꾸어 학습하는 방법처럼, 자료의 구조와 계산 비용을 함께 다루는 기계학습 방법도 개발한다.[^home][^p7][^p8]

## 대표 논문

2021–2026년 논문 가운데 연구 갈래를 보여 주는 8편을 골랐다. 오혜연 교수는 6편의 마지막 저자이며 KoBBQ와 Beneath the Surface에서는 중간 저자다. 연도·학회는 연구실 표기이며, arXiv 판으로 설명한 논문은 표에 그 판본을 밝혔다. “쉽게 말하면”은 각 논문의 초록만을 근거로 썼다.[^pubs]

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자와 오혜연 교수의 위치 |
|---|---|---|---|---|
| 1 | 2024 | [BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages](https://arxiv.org/abs/2406.09948) · NeurIPS 2024 (채택), 설명은 arXiv v2 | 여러 문화권의 일상 지식을 묻는 짧은 답변형·객관식 평가 자료를 만들었다. 인터넷에 많이 나타나는 문화권에서 모델의 성능이 높았고, 자료가 적은 언어에서는 현지 언어보다 영어로 물었을 때 성능이 높은 경우가 나타났다. 평가 자료는 공개했다.[^p1] | 첫 저자 Junho Myung, 마지막 저자 Alice Oh |
| 2 | 2026 | [Gradual Code-Switching as Inference-Time Cross-Lingual Representational Alignment for LLMs](https://arxiv.org/abs/2510.05678) · COLM 2026, 설명은 arXiv v2 | 코드 전환 문맥 학습(CSICL, code-switching in-context learning)을 제안했다. 목표 언어에서 영어로 점차 전환하는 예시로 추론 경로를 안내하여 비영어 입력을 영어 중심의 추론 공간과 연결한다. 여러 모델·자료·언어를 대상으로 한 비교에서 다언어 문맥 학습 기준 방법보다 성능이 향상됐고, 평가에 새로 넣은 언어에도 효과가 이어졌다.[^p2] | Haneul Yoo, Jiho Jin, Kyunghyun Cho, Alice Oh. 마지막 저자 Alice Oh |
| 3 | 2025 | [LLM-as-an-Interviewer: Beyond Static Testing Through Dynamic LLM Evaluation](https://doi.org/10.18653/v1/2025.findings-acl.1357) · ACL Findings 2025 | 언어 모델이 면접관이 되어 다른 모델의 답변에 피드백을 주고 추가 질문을 하는 평가 틀이다. 첫 질문을 동적으로 바꾸고, 첫 답변의 질과 피드백 적응·명확화 질문 대응을 함께 평가한다. 면접 과정의 사례와 장단점을 종합한 보고서도 제안했다.[^p3] | 첫 저자 Eunsu Kim, 마지막 저자 Alice Oh |
| 4 | 2024 | [KoBBQ: Korean Bias Benchmark for Question Answering](https://doi.org/10.1162/tacl_a_00661) · TACL 2024 | 미국의 편향 평가 자료를 다른 문화로 옮길 때 그대로 쓸 항목, 대상을 바꿀 항목, 제외할 항목을 나누는 틀을 제안했다. 한국 문화에 맞는 편향 범주를 추가하고 설문으로 검증한 자료를 만들었다. 이 자료와 단순 기계번역 자료로 측정한 모델의 편향이 달라, 문화에 맞춘 평가가 필요함을 보였다.[^p4] | 첫 저자 Jiho Jin, Alice Oh는 6명 중 5번째 저자 |
| 5 | 2025 | [DREsS: Dataset for Rubric-based Essay Scoring on EFL Writing](https://doi.org/10.18653/v1/2025.acl-long.659) · ACL 2025 | 외국어로 영어를 배우는 학습자의 글을 여러 평가 기준에 따라 채점하는 자료를 공개했다. 실제 수업에서 모은 글과 전문가 채점, 기존 자료의 표준화, 글의 일부를 변형해 만든 합성 자료를 함께 담았다. 글을 변형하는 증강 방법을 학습에 사용했을 때 기준 모델의 결과가 개선됐다.[^p5] | Haneul Yoo, Jieun Han, So-Yeon Ahn, Alice Oh. 마지막 저자 Alice Oh |
| 6 | 2021 | [Learning Bill Similarity with Annotated and Augmented Corpora of Bills](https://doi.org/10.18653/v1/2021.emnlp-main.787) · EMNLP 2021 | 법안 사이의 복사·순서 변경·표현 변경을 반영하는 관계 분류 과제를 만들었다. 합성 자료로 먼저 학습한 뒤 사람이 법안의 작은 구획끼리의 관계를 표시한 자료로 미세조정했다. 두 자료를 함께 쓴 모델은 예측 성능이 개선됐고, 법안의 구획과 전체 수준의 유사성을 포착했다.[^p6] | Jiseon Kim, Elden Griggs, In Song Kim, Alice Oh. 마지막 저자 Alice Oh |
| 7 | 2026 | [Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs](https://arxiv.org/abs/2609.04753) · EMNLP 2026 (채택), 설명은 arXiv v1 | 언어로 드러나는 추론 단계가 모델 내부에서도 서로 다른 구조로 나타나는지 분석했다. 추론 단계는 따로 보관한 평가 자료의 내부 표현에서도 구별됐고, 그 구별은 중간 층에서 두드러졌다. 같은 단어도 주변 추론 단계에 따라 표현이 달랐으며, 어텐션을 가리는 개입은 앞선 문맥이 단계 시작 부분의 표현에 영향을 준다는 점을 보였다.[^p7] | 첫 저자 Seogyeong Jeong, Alice Oh는 6명 중 5번째 저자 |
| 8 | 2024 | [Translating Subgraphs to Nodes Makes Simple GNNs Strong and Efficient for Subgraph Representation Learning](https://proceedings.mlr.press/v235/kim24aa.html) · ICML 2024 | 전체 그래프의 일부를 각각 새 노드로 바꾸어 다른 그래프를 만드는 Subgraph-To-Node(S2N) 방법이다. 관계망 일부의 특징을 학습할 때 부분과 전체의 구조를 함께 반영하면서 메모리와 계산 비용을 줄였다. 비교 실험에서는 비슷하거나 나은 예측 성능을 유지하면서 처리할 수 있는 하위 그래프 표본 수가 늘었다.[^p8] | Dongkwan Kim, Alice Oh. 마지막 저자 Alice Oh |

## 교수와 전문 분야

오혜연 교수(Alice Oh)는 KAIST 전산학부의 교수·석좌교수다. 학과는 전문 분야를 기계학습과 전산사회과학으로, 연구 분야를 인공지능·정보서비스, 소셜 컴퓨팅, 인터랙티브 컴퓨팅으로 소개한다.[^faculty] MIT에서 수학 학사(1996)와 컴퓨터과학 박사(2008), Carnegie Mellon University에서 Language and Information Technologies 석사(2000)를 받았다.[^members]

최근 연구의 전문 분야는 **다언어·문화적 언어 모델 평가와 공정성**, **교육·정치사회 자료의 언어 분석**, **모델 내부 표현과 그래프 학습 방법**으로 묶을 수 있다. 문화 지식을 묻는 자료와 한국 문화의 편향 평가, 작문 채점과 법안 유사도 학습, 추론 단계 분석과 그래프 변환 방법이 이를 보여 준다.[^p1][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

- 여러 언어와 문화에 맞는 언어 모델의 평가·개선, 편향과 안전성 평가.[^home][^p1][^p4]
- 외국어 작문 교육의 채점·학습 지원과 교육용 언어 모델.[^home][^p5]
- 법안의 관계와 로비 등 사회·정치 현상을 문서 자료로 분석하는 연구.[^home][^p6]
- 한자 역사 문헌의 문장부호 복원·이름 식별·한국어와 영어 번역을 돕는 공개 도구.[^demos]

## 구성원

누리집의 Ph.D. Candidates 13명과 Master Candidates 5명이다(2026-11-01). 과정과 연구 주제는 연구실 표기다. 대표 논문 참여는 전체 저자 목록에서 같은 영문 이름을 확인한 경우에 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jae Won Kim | 박사과정 | Computational Social Science, Topic Modeling, Big Data Analysis | jaewonk@kaist.ac.kr |  |
| Changyoon Lee | 박사과정 | NLP Application, LLMs for Education | changyoon.lee@kaist.ac.kr |  |
| Jiho Jin | 박사과정 |  | jinjh0123@kaist.ac.kr | 1, 2, 4 |
| Kiwoong Park | 박사과정 | NLP Application | marspak@kaist.ac.kr | 1 |
| Juhyun Oh | 박사과정 | Natural Language Processing | 411juhyun@kaist.ac.kr |  |
| Faiz Ghifari Haznitrama | 박사과정 | Low-Resource & Efficient NLP, Machine Translation | haznitrama@kaist.ac.kr |  |
| Jieun Han | 박사과정 | NLP Application, Language Learning | jieun_han@kaist.ac.kr | 5 |
| Jisu Shin | 박사과정 |  | jisu.shin@kaist.ac.kr |  |
| Junho Myung | 박사과정 | Natural Language Processing | junho00211@kaist.ac.kr | 1 |
| Seyoung Song | 박사과정 | Multilingual NLP | seyoung.song@kaist.ac.kr |  |
| Dongkeun Yoon | 박사과정 |  | dkyoon@kaist.ac.kr |  |
| Junyeong Park | 박사과정 | Multicultural LLM, LLM for Education | junyeong.park@kaist.ac.kr |  |
| Seogyeong Jeong | 박사과정 | Interpretability, Agent, Explainability, Reasoning | sg.jeong28@kaist.ac.kr | 7 |
| Jaewon Cho | 석사과정 | Multimodal LLM | cho35750@kaist.ac.kr |  |
| Jun Seong Kim | 석사과정 |  | 09jkim@kaist.ac.kr |  |
| Jihyun Yoo | 석사과정 |  | yoojihyun6933@kaist.ac.kr |  |
| Sunwoo Kim | 석사과정 | AI Safety & Reliability | sunwoo.kim@kaist.ac.kr |  |
| Yen Shin | 석사과정 |  | yeeun@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Members의 Alumni 구역 38명이다. 학위·과정과 연도는 연구실 표기로, 2010–2026년을 포함한다. 진로는 해당 쪽에 게시된 소속·직위다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jiseon Kim | Ph.D. (2026) | Distinguished Postdoctoral Fellow @ Vector Institute/University of Toronto |
| Haneul Yoo | Ph.D. (2026) | Assistant Professor/Faculty Fellow @ New York University |
| Eunsu Kim | Master's (2026) | Ph.D. Student @ Carnegie Mellon University |
| Dongkwan Kim | Ph.D. (2025) | Postdoctoral Researcher @ Texas A&M University |
| Chani Jung | Master's (2025) | Ph.D. Student @ University of British Columbia |
| Rifki Afina Putri | Ph.D. (2025) | Lecturer @ Universitas Gadjah Mada |
| Nayeon Lee | Master's (2024) | Research Engineer @ Samsung Research |
| Jungbin Son | Master's (2023) | Research Engineer @ Lomin |
| Jungkook Park | Ph.D. (2023) | CTO @ Elice |
| Youngin Lee | Master's (2023) | Machine Learning Engineer @ Daangn (Karrot) |
| Juhee Son | Master's (2023) | Machine Learning Engineer @ Amazon |
| Younghoon Jeong | Researcher (2022) | Research Engineer @ NAVER Corp. |
| Yeon Seonwoo | Ph.D. (2022) | Applied Scientist @ Amazon |
| Khiati Abdel-ilah Zakaria | Ph.D. (2022) | Assistant Professor @ Abu Dhabi University |
| Sungjoon Park | Ph.D. (2022) | CEO @ Softly.ai |
| Jaimeen Ahn | Master's (2022) | Machine Learning Engineer @ Daangn (Karrot) |
| Jeongmin Byun | Ph.D. (2021) | Research Director @ Xenoimpact |
| Changmin Lee | Master's (2021) | Research Scientist @ Kakao Enterprise |
| Donghoon Han | Master's (2021) | Machine Learning Engineer @ Skelter Labs |
| Suin Kim | Ph.D. (2021) | Platform Lead @ Elice |
| JinYeong Bak | Ph.D. (2020) | Assistant Professor @ Sungkyunkwan University |
| Jooyeon Kim | Ph.D. (2020) | Assistant Professor @ UNIST |
| Christoffer Øhrstrøm | Master's (2020) | Data Scientist @ Visma |
| Junsoo Park | Master's (2019) | Engineer @ NCSOFT Co. |
| Jeongmin Cha | Master's (2019) | Software Engineer @ Yanolja |
| Joon Hee Kim | Ph.D. (2017) | Applied Scientist @ Amazon |
| Sooyoung Kim | Master's (2016) | Developer @ SAP Korea |
| Sohyeong Kim | Master's (2017) | Data Scientist @ SAP Germany |
| Dongwoo Kim | Master's (2015) | Software Engineer @ Return Zero Inc. |
| Dongwoo Kim | Ph.D. (2015) | Assistant Professor @ Postech |
| Yeooul Kim | Master's (2013) | Software Engineer @ Hyundai Mobis North America |
| Bumsoo Kang | Master's (2013) | Ph.D. student, NC Lab @ KAIST |
| Trung Nguyen | Undergraduate Researcher (2011) | Principal Data Scientist @ Suncorp Group |
| Yohan Jo | Master's (2012) | Assistant Professor @ Seoul National University |
| Sunjun Kim | Master's (2011) | Assistant Professor @ DGIST |
| Youngmin Kim | Master's (2010) | Official @ Government of the Republic of Korea |
| Hyunjong Peter Lee | Master's (2010) | Software Engineer @ PUBG Corp |
| Francisco Arturo Rojas | Master's (2010) | Senior Software Engineer @ L3Harris Technologies |

## 최근 논문 목록 (2021–2026)

문화·언어 모델 평가, 교육 지원, 사회 현상의 언어 분석, 그래프 학습을 다룬다. 연도는 연구실 Publications의 연도 구역이며 제목·저자·발표처는 연구실 표기다. 저자명 뒤 \*는 누리집 표시다. arXiv가 연결된 항목은 연결된 사전 공개본을 함께 표시했다. arXiv가 NeurIPS 2024 채택을 명시한 BLEnD와 EMNLP 2026 발표 예정을 명시한 Beneath the Surface는 채택으로 표시했다.[^pubs][^p1][^p7]

**2026**

- Kiwoong Park, Seyoung Song, Donghyun Woo, Alice Oh. "North or South? Diagnosing LLMs' Understanding of North Korean Language, Society, and Knowledge". *Proceedings of The 5th Asia-Pacific Chapter of the Association for Computational Linguistics & the 15th International Joint Conference on Natural Language Processing (AACL-IJCNLP 2026, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2610.15282).
- Faiz Ghifari Haznitrama, Alice Oh. "Evaluating Communicative Success in Machine-Translated Conversation". *Real-Time Conversational Agents @ NeurIPS 2026*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2609.19885).
- Sunwoo Kim, Seokwon Jung, Sohyung Kim, Seong Joon Oh, Alice Oh. "Form Over Content In Gradient-Based Data Attribution Methods". *Attributing Model Behavior at Scale @ NeurIPS 2026*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2609.19589).
- Soyeon Park, Seogyeong Jeong\*, Sunwoo Kim\*, Alice Oh. "The Role of Fine-grained Harm Signals in LLM Safety". *Interpretability as a Science @ NeurIPS 2026*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2609.19366).
- Yang Ou, Carlos Rodriguez-Pardo, Alaa Al Khourdajie, Joeri Rogelj, Peijie Zhou, S. Karthik Mukkavilli, Massimo Tavoni, Leon Clarke, Yong Liu, Tengjiao Wang, Alice Oh, Haewon McJeon. "Artificial intelligence to support cross-disciplinary climate change research". *Nature Climate Change*.
- Jiho Jin\*, Junho Myung\*, Juhyun Oh, Junyeong Park, Rifki Afina Putri, Sunipa Dev, Vinodkumar Prabhakaran, Alice Oh. "JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors". *Advances in Neural Information Processing Systems (NeurIPS 2026, Evaluations and Datasets Track)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2605.26955).
- Eunsu Kim\*, Haneul Yoo\*, Guijin Son, Hitesh Patel, Amit Agarwal, Alice Oh. "Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub". *Advances in Neural Information Processing Systems (NeurIPS 2026, Evaluations and Datasets Track)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2506.00482).
- Seogyeong Jeong, Jaehui Hwang, Dongyoon Han, Geonmo Gu, Alice Oh, Taekyung Kim. "Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs". *Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026, Long)*. 채택; [arXiv 사전 공개본 연결](https://arxiv.org/abs/2609.04753); DOI <https://doi.org/10.48550/arXiv.2609.04753>.
- Siddhesh Pawar\*, Sarah Masud\*, Haneul Yoo, Alice Oh, Isabelle Augenstein. "Not What, But How: A Framework for Auditing LLM Responses across Positioning, Generalization, Anthromorphism, and Maxims". *Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026, Long)*. [arXiv 사전 공개본 연결](http://arxiv.org/abs/2606.02493).
- Changyoon Lee, Junyeong Park, Seungju Kim, Alice Oh. "TutorLens: An Adaptive Framework for Evaluating AI Tutors in Active Learning Settings". *5th Workshop on NLP for Positive Impact (EMNLP 2026)*.
- Haneul Yoo, Jiho Jin, Kyunghyun Cho, Alice Oh. "Gradual Code-Switching as Inference-Time Cross-Lingual Representational Alignment for LLMs". *Third Conference on Language Modeling (COLM 2026)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2510.05678); DOI <https://doi.org/10.48550/arXiv.2510.05678>.
- Jaehong Kim\*, Hyeonseung Kim\*, Jiseon Kim, Alice Oh, Thorsten Holz, Wonjae Lee, Meeyoung Cha. "Cross-National Information Attacks: A Two-Decade Analysis of Troll Behavior in Korea". *Proceedings of the 35th USENIX Security Symposium (USENIX Security '26)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2606.22785).
- Nedjma Ousidhoum, Junho Myung, Carla Perez-Almendros, Jiho Jin, Amr Keleg, Meriem Beloucif, Yi Zhou, Rodrigo Agerri, Vladimir Araujo, Naomi Baes, James Barry, Joanne Boisson, Nancy F. Chen, Christine de Kock, Aleksandra Edwards, Joseba Fernandez de Landa, Mohamed Fazli Imam, Huda Hakami, Shu-Kai Hsieh, Joseph Marvin Imperial, Roy Ka-Wei Lee, Zhengyuan Liu, Chenyang Lyu, Younes Samih, Johan Sjons, Bryan Tan, Asahi Ushio, Weihua Zheng, Alice Oh, Jose Camacho-Collados. "SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures". *Proceedings of the 20th International Workshop on Semantic Evaluation (2026)*.
- Seogyeong Jeong\*, Kiwoong Park\*, Seyoung Song, Eunsu Kim, Ken E Friedl, Jaeho Kim, Alice Oh. "LoCar: Localization-Aware Evaluation of In-Vehicle Assistants through Fine-Grained Sociolinguistic Control". *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026, Industry Track)*. [arXiv 사전 공개본 연결](https://arxiv.org/pdf/2605.21086).
- Shubin Kim\*, Yejin Son\*, Junyeong Park, Keummin Ka, Seungbeen Lee, Jaeyoung Lee, Hyeju Jang, Alice Oh, Youngjae Yu. "Investigating Counterfactual Unfairness in LLMs towards Identities through Humor". *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2604.18729).
- Jisu Shin, Hoyun Song, Juhyun Oh, Changgeon Ko, Eunsu Kim, Chani Jung, Alice Oh. "RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity". *Findings of the Association for Computational Linguistics: ACL 2026 (ACL-Findings 2026, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2509.25897).
- Juhyun Oh, Haneul Yoo, Faiz Ghifari Haznitrama, Alice Oh. "OLA: Output Language Alignment in Code-Switched LLM Interactions". *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2601.03589).
- Eunsu Kim, Junyeong Park, Juhyun Oh, Kiwoong Park, Seyoung Song, A. Seza Doğruöz, Alice Oh, Najoung Kim. "Are they lovers or friends? Evaluating LLMs' Social Reasoning in English and Korean Dialogues". *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2510.19028).
- Junho Myung, Hyunseung Lim\*, Hana Oh\*, Hyoungwook Jin, Nayeon Kang, So-Yeon Ahn, Hwajung Hong, Alice Oh, Juho Kim. "When Scaffolding Breaks: Investigating Student Interaction with LLM-Based Writing Support in Real-Time K-12 EFL Classrooms". *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI 2026)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2512.05506).
- Eunsu Kim\*, Junyeong Park\*, Na Min An\*, Junseong Kim, Hitesh Laxmichand Patel, Jiho Jin, Julia Kruk, Amit Agarwal, Srikant Panda, Fenal Ashokbhai Ilasariya, Hyunjung Shim, Alice Oh. "World in a Frame: Understanding Culture Mixing as a New Challenge for Vision-Language Models". *The IEEE/CVF Conference on Computer Vision and Pattern Recognition 2026 (CVPR 2026)*. [arXiv 사전 공개본 연결](https://www.arxiv.org/abs/2511.22787).
- Seyoung Song, Nawon Kim, Songeun Chae, Kiwoong Park, Jiho Jin, Haneul Yoo, Kyunghyun Cho, Alice Oh. "Open Korean Historical Corpus: A Millennia-Scale Diachronic Collection of Public Domain Texts". *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2510.24541).
- Juhyun Oh, Nayeon Lee, Chani Jung, Jiho Jin, Junho Myung, Jongwon Lee, Taieui Song, Alice Oh. "FINEST: Improving LLM Responses to Sensitive Topics Through Fine-Grained Evaluation". *Findings of the Association for Computational Linguistics: EACL 2026 (EACL-Findings 2026, Long)*.

**2025**

- Seyoung Song, Haneul Yoo, Jiho Jin, Kyunghyun Cho, Alice Oh. "Shared Heritage, Distinct Writing: Rethinking Resource Selection for East Asian Historical Documents". *Findings of the Association for Computational Linguistics: IJCNLP-AACL 2025 (IJCNLP-AACL-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2411.04822).
- Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Wenchao Dong, Alice Oh, Meeyoung Cha. "Mind the Gap: LLM Actions vs. Human Social Understanding in Moral Dilemmas". *Workshop for Women in Machine Learning (WiML) @ NeurIPS 2025*.
- Jiyoung Lee, Seungho Kim, Jieun Han, Jun-Min Lee, Kitaek Kim, Alice Oh, Edward Choi. "Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties". *The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS 2025, Datasets and Benchmarks Track)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2505.20875).
- Seyoung Song, Seogyeong Jeong, Eunsu Kim, Jiho Jin, Dongkwan Kim, Jay Shin, Alice Oh. "MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language". *Findings of the Association for Computational Linguistics: EMNLP 2025 (EMNLP-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2505.14395).
- Juhyun Oh, Inha Cha, Michael Saxon, Hyunseung Lim, Shaily Bhatt, Alice Oh. "Culture is Everywhere: A Call for Intentionally Cultural Evaluation". *Findings of the Association for Computational Linguistics: EMNLP 2025 (EMNLP-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/pdf/2509.01301).
- Juhyun Oh, Eunsu Kim, Jiseon Kim, Wenda Xu, Inha Cha, William Yang Wang, Alice Oh. "Uncovering Factor Level Preferences to Improve Human-Model Alignment". *Findings of the Association for Computational Linguistics: EMNLP 2025 (EMNLP-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2410.06965).
- Jieun Han, Daniel Lee, Haneul Yoo, Jinsung Yoon, Junyeong Park, So‑Yeon Ahn, Alice Oh. "One‑Topic‑Doesn’t‑Fit‑All: Transcreating Reading Comprehension Test for Personalized Learning". *Workshop on Tailoring AI: Exploring Active and Pasive LLM Personalization (PALS) @ EMNLP 2025*. [arXiv 사전 공개본 연결](http://arxiv.org/abs/2511.09135).
- Haneul Yoo, Jieun Han, So-Yeon Ahn, Alice Oh. "DREsS: Dataset for Rubric-based Essay Scoring on EFL Writing". *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2402.16733); DOI <https://doi.org/10.18653/v1/2025.acl-long.659>.
- Zahra Bayramli, Ayhan Suleymanzade, Na Min An, Huzama Ahmad, Eunsu Kim, Junyeong Park, James Thorne, Alice Oh. "Diffusion Models Through a Global Lens: Are They Culturally Inclusive?". *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2502.08914).
- Shivalika Singh, Angelika Romanou, Clémentine Fourrier, David I. Adelani, Jian Gang Ngui, Daniel Vila-Suero, Peerat Limkonchotiwat, Kelly Marchisio, Wei Qi Leong, Yosephine Susanto, Raymond Ng, Shayne Longpre, Wei-Yin Ko, Madeline Smith, Antoine Bosselut, Alice Oh, Andre F. T. Martins, Leshem Choshen, Daphne Ippolito, Enzo Ferrante, Marzieh Fadaee, Beyza Ermis, Sara Hooker. "Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation". *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2412.03304).
- Wooyoung Go, Hyoungshick Kim, Alice Oh, Yongdae Kim. "XDAC: XAI-Driven Detection and Attribution of LLM-Generated News Comments in Korean". *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Long)*.
- Jiho Jin, Woosung Kang, Junho Myung, Alice Oh. "Social Bias Benchmark for Generation: A Comparison of Generation and QA-Based Evaluations". *Findings of the Association for Computational Linguistics: ACL 2025 (ACL-Findings 2025, Short)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2503.06987).
- Eunsu Kim, Juyoung Suk, Seungone Kim, Niklas Muennighoff, Dongkwan Kim, Alice Oh. "LLM-as-an-Interviewer: Beyond Static Testing Through Dynamic LLM Evaluation". *Findings of the Association for Computational Linguistics: ACL 2025 (ACL-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2412.10424); DOI <https://doi.org/10.18653/v1/2025.findings-acl.1357>.
- Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee. "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs". *Findings of the Association for Computational Linguistics: ACL 2025 (ACL-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2411.02460).
- Jisu Shin, Juhyun Oh, Eunsu Kim, Hoyun Song, Alice Oh. "Spotting Out-of-Character Behavior: Atomic-Level Evaluation of Persona Fidelity in Open-Ended Generation". *Findings of the Association for Computational Linguistics: ACL 2025 (ACL-Findings 2025, Long)*. [arXiv 사전 공개본 연결](https://www.arxiv.org/abs/2506.19352).
- Siddhesh Pawar, Junyeong Park, Jiho Jin, Arnav Arora, Junho Myung, Srishti Yadav, Faiz Ghifari Haznitrama, Inhwa Song, Alice Oh, Isabelle Augenstein. "Survey of Cultural Awareness in Language Models: Text and Beyond". *Computational Linguistics (CL 2025)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2411.00860).
- Junho Myung, Yeon Su Park, Sunwoo Kim, Shin Yoo, Alice Oh. "PapersPlease: A Benchmark for Evaluating Motivational Values of Large Language Models Based on ERG Theory". *Workshop on Generation, Evaluation & Metrics (GEM) @ ACL 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2506.21961).
- Daniel Lee, Harsh Sharma, Jieun Han, Sunny Jeong, Alice Oh, Vered Shwartz. "Team ACK at SemEval-2025 Task 2: Beyond Word-for-Word Machine Translation for English-Korean Pairs". *Workshop on SemEval @ ACL 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2504.20451).
- Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Alice Oh, Meeyoung Cha. "Exploring Persona-dependent LLM Alignment for the Moral Machine Experiment". *Workshop on Bi-directional Human-AI Alignment @ ICLR 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2504.10886).
- Juhyun Oh, Eunsu Kim, Alice Oh. "Flex-TravelPlanner: A Benchmark for Flexible Planning with Language Agents". *Workshop on Reasoning and Planning for Large Language Models @ ICLR 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2506.04649).
- Jun Seong Kim, Kyaw Ye Thu, Javad Ismayilzada, Junyeong Park, Eunsu Kim, Huzama Ahmad, Na Min An, James Thorne, Alice Oh. "When Tom Eats Kimchi: Evaluating Cultural Bias of Multimodal Large Language Models in Cultural Mixture Contexts". *Workshop on Cross-Cultural Considerations in NLP (C3NLP) at NAACL 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2503.16826).
- Junyeong Park, Seogyeong Jeong, Seyoung Song, Yohan Lee, Alice Oh. "LLM-C3MOD: A Human-LLM Collaborative System for Cross-Cultural Hate Speech Moderation". *Workshop on Cross-Cultural Considerations in NLP (C3NLP) at NAACL 2025*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2503.07237).
- Genta Indra Winata, Frederikus Hudi, Patrick Amadeus Irawan, David Anugraha, Rifki Afina Putri, Yutong Wang, Adam Nohejl, Ubaidillah Ariq Prathama, Nedjma Ousidhoum, Afifa Amriani, Anar Rzayev, Anirban Das, Ashmari Pramodya, Aulia Adila, Bryan Wilie, Candy Olivia Mawalim, Ching Lam Cheng, Daud Abolade, Emmanuele Chersoni, Enrico Santus, Fariz Ikhwantri, Garry Kuwanto, Hanyang Zhao, Haryo Akbarianto Wibowo, Holy Lovenia, Jan Christian Blaise Cruz, Jan Wira Gotama Putra, Junho Myung, Lucky Susanto, Maria Angelica Riera Machin, Marina Zhukova, Michael Anugraha, Muhammad Farid Adilazuarda, Natasha Santosa, Peerat Limkonchotiwat, Raj Dabre, Rio Alexander Audino, Samuel Cahyawijaya, Shi-Xiong Zhang, Stephanie Yulia Salim, Yi Zhou, Yinxuan Gui, David Ifeoluwa Adelani, En-Shiun Annie Lee, Shogo Okada, Ayu Purwarianti, Alham Fikri Aji, Taro Watanabe, Derry Tanti Wijaya, Alice Oh, Chong-Wah Ngo. "WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines". *Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2025, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2410.12705).
- Dongkwan Kim, Alice Oh. "Generalizing Weisfeiler-Lehman Kernels to Subgraphs". *The Thirteenth International Conference on Learning Representations (ICLR 2025)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2412.02181).

**2024**

- Olga Viberg, Rene F. Kizilcec, Ioana Jivet, Alejandra Martínez Monés, Alice Oh, Chantal Mutimukwe, Stefan Hrastinski, Maren Scheffel. "Cultural differences in students’ privacy concerns in learning analytics across Germany, South Korea, Spain, Sweden, and the United States". *Computers in Human Behavior Reports (2024)*.
- Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Afina Putri, Dimosthenis Antypas, Hsuvas Borkakoty, Eunsu Kim, Carla Perez-Almendros, Abinew Ali Ayele, Víctor Gutiérrez-Basulto, Yazmín Ibáñez-García, Hwaran Lee, Shamsuddeen Hassan Muhammad, Kiwoong Park, Anar Sabuhi Rzayev, Nina White, Seid Muhie Yimam, Mohammad Taher Pilehvar, Nedjma Ousidhoum, Jose Camacho-Collados, Alice Oh. "BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages". *Advances in Neural Information Processing Systems (NeurIPS 2024, Datasets and Benchmarks Track)*. 채택; [arXiv 사전 공개본 연결](https://arxiv.org/abs/2406.09948); DOI <https://doi.org/10.48550/arXiv.2406.09948>.
- Dongkwan Kim, Junho Myung, Alice Oh. "Salad-Bowl-LLM: Multi-Culture LLMs by In-Context Demonstrations from Diverse Cultures". *Workshop on Socially Responsible Language Modelling Research (SoLaR) at NeurIPS 2024*.
- Jiseon Kim, Dongkwan Kim, Joohye Jeong, In Song Kim, Alice Oh. "Understanding Lobbying Strategies in Legislative Process: Bill Position Dataset and Lobbying Analysis". *Workshop for Women in Machine Learning (WiML) @ NeurIPS 2024*.
- Chani Jung, Dongkwan Kim, Jiho Jin, Jiseon Kim, Yeon Seonwoo, Yejin Choi, Alice Oh, Hyunwoo Kim. "Perceptions to Beliefs: Exploring Precursory Inferences for Theory of Mind in Large Language Models". *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2407.06004).
- Rifki Afina Putri, Faiz Ghifari Haznitrama, Dea Adhista, Alice Oh. "Can LLM Generate Culturally Relevant Commonsense QA Data? Case Study in Indonesian and Sundanese". *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2402.17302).
- Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. "LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction". *Workshop on Customizable NLP (CustomNLP4U) at EMNLP 2024*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2310.05191).
- Sheikh Shafayat, Eunsu Kim, Juhyun Oh, Alice Oh. "Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore". *First Conference on Language Modeling (COLM 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2402.18045).
- Juhee Son, Yeon Seonwoo, Alice Oh, James Thorne, Seunghyun Yoon. "Multi-hop Database Reasoning with Virtual Knowledge Graph". *Proceedings of the 1st Workshop on Knowledge Graphs and Large Language Models (KaLLM 2024)*.
- Sheikh Shafayat, H M Quamran Hasan, Minhajur Rahman Chowdhury Mahim, Rifki Afina Putri, James Thorne, Alice Oh. "BEnQA: A Question Answering Benchmark for Bengali and English". *Findings of the Association for Computational Linguistics: ACL 2024 (ACL-Findings 2024, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2403.10900).
- Changyoon Lee, Junho Myung, Jieun Han, Jiho Jin, Alice Oh. "Learning from Teaching Assistants to Program with Subgoals: Exploring the Potential for AI Teaching Assistants". *Educational Datamining ’24 Human-Centric eXplainable AI in Education and Leveraging Large Language Models for Next-Generation Educational Technologies Workshop Joint Proceedings (L3MNGET 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2309.10419).
- Dongkwan Kim, Alice Oh. "Translating Subgraphs to Nodes Makes Simple GNNs Strong and Efficient for Subgraph Representation Learning". *Forty-first International Conference on Machine Learning (ICML 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2204.04510).
- Nayeon Lee, Chani Jung, Junho Myung, Jiho Jin, Jose Camacho-Collados, Juho Kim, Alice Oh. "Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis". *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2308.16705).
- Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Tak Yeon Lee, So-Yeon Ahn, Alice Oh. "RECIPE4U: Student-ChatGPT Interaction Dataset in EFL Writing Education". *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2403.08272).
- Eunsu Kim, Juyoung Suk, Philhoon Oh, Haneul Yoo, James Thorne, Alice Oh. "CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean". *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2403.06412).
- Juhyun Oh, Eunsu Kim, Inha Cha, Alice Oh. "The Generative AI Paradox in Evaluation: "What It Can Solve, It May Not Evaluate". *EACL 2024 Student Research Workshop*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2402.06204).
- Jiho Jin, Jiseon Kim, Nayeon Lee, Haneul Yoo, Alice Oh, Hwaran Lee. "KoBBQ: Korean Bias Benchmark for Question Answering". *Transactions of the Association for Computational Linguistics (TACL 2024)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2307.16778); DOI <https://doi.org/10.1162/tacl_a_00661>.

**2023**

- Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Tak Yeon Lee, So-Yeon Ahn, Alice Oh. "Exploring Student-ChatGPT Dialogue in EFL Writing Education". *Workshop on Generative AI for Education (GAIED) at NeurIPS 2023*.
- Jungbin Son, Alice Oh. "Time-Aware Representation Learning for Time-Sensitive Question Answering". *Findings of the Association for Computational Linguistics: EMNLP 2023 (EMNLP-Findings 2023, Short)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2310.12585).
- Haneul Yoo, Rifki Afina Putri, Changyoon Lee, Youngin Lee, So-Yeon Ahn, Dongyeop Kang, Alice Oh. "Rethinking Annotation: Can Language Learners Contribute?". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2210.06828).
- Yeon Seonwoo, Guoyin Wang, Changmin Seo, Sajal Choudhary, Jiwei Li, Xiang Li, Puyang Xu, Sunghyun Park, Alice Oh. "Ranking-Enhanced Unsupervised Sentence Representation Learning". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2209.04333).
- Soyoung Yoon, Sungjoon Park, Gyuwan Kim, Junhee Cho, Kihyo Park, Gyu Tae Kim, Minjoon Seo, Alice Oh. "Towards standardizing Korean Grammatical Error Correction: Datasets and Annotation". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2210.14389).
- Hwaran Lee, Seokhee Hong, Joonsuk Park, Takyoung Kim, Meeyoung Cha, Yejin Choi, Byoungpil Kim, Gunhee Kim, Eun-Ju Lee, Yong Lim, Alice Oh, Sangchul Park, Jung-Woo Ha. "SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created through Human-Machine Collaboration". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023, Long)*.
- Jungkook Park, Alice Oh. "EliRank: A Code Editing History Based Ranking Model for Early Detection of Students in Need". *Proceedings of the Tenth ACM Conference on Learning @ Scale (L@S 2023)*.
- Jieun Han, Haneul Yoo, Yoonsu Kim, Junho Myung, Minsun Kim, Hyunseung Lim, Juho Kim, Tak Yeon Lee, Hwajung Hong, So-Yeon Ahn, Alice Oh. "RECIPE: How to Integrate ChatGPT into EFL Writing Education". *Proceedings of the Tenth ACM Conference on Learning @ Scale (L@S 2023, WiP)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2305.11583).
- Nayeon Lee, Chani Jung, Alice Oh. "Hate Speech Classifiers are Culturally Insensitive". *Workshop on Cross-Cultural Considerations in NLP (C3NLP) at EACL 2023*.
- Rene Kizilcec, Olga Viberg, Ioana Jivet, Alejandra Martinez Mones, Alice Oh, Stefan Hratinski, Chantal Mutimukwe, Maren Scheffel. "The Role of Gender in Students’ Privacy Concerns about Learning Analytics". *Proceedings of the 2023 Conference on Learning Analytics and Knowledge (LAK 2023)*.

**2022**

- Younghoon Jeong, Juhyun Oh, Jaimeen Ahn, Jongwon Lee, Jihyung Moon, Sungjoon Park, Alice Oh. "KOLD: Korean Offensive Language Dataset". *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2205.11315).
- Rifki Afina Putri, Alice Oh. "IDK-MRC: Unanswerable Questions for Indonesian Machine Reading Comprehension". *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2210.13778).
- Juhee Son, Jiho Jin, Haneul Yoo, JinYeong Bak, Kyunghyun Cho, Alice Oh. "Translating Hanja Historical Documents to Contemporary Korean and English". *Findings of the Association for Computational Linguistics: EMNLP 2022 (EMNLP-Findings 2022)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2205.10019).
- Yeon Seonwoo, Seunghyun Yoon, Franck Dernoncourt, Trung Bui, Alice Oh. "Virtual Knowledge Graph Construction for Zero-Shot Domain-Specific Document Retrieval". *Proceedings of the 29th International Conference on Computational Linguistics (COLING 2022, Long)*.
- Dongkwan Kim, Jiho Jin, Jaimeen Ahn, Alice Oh. "Models and Benchmarks for Representation Learning of Partially Observed Subgraphs". *31st ACM International Conference on Information and Knowledge Management (CIKM 2022, Short Papers Track)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2209.00508).
- Jaimeen Ahn, Hwaran Lee, Jinhwa Kim, Alice Oh. "Why Knowledge Distillation Amplifies Gender Bias and How to Mitigate from the Perspective of DistilBERT". *Workshop on Gender Bias in Natural Language Processing (GeBNLP) at NAACL 2022*.
- Haneul Yoo, Jiho Jin, Juhee Son, JinYeong Bak, Kyunghyun Cho, Alice Oh. "HUE: Pretrained Model and Dataset for Understanding Hanja Documents of Ancient Korea". *Findings of the Association for Computational Linguistics: NAACL 2022 (NAACL-Findings 2022, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2210.05112).
- Changyoon Lee, Yeon Seonwoo, Alice Oh. "CS1QA: A Dataset for Assisting Code-based Question Answering in an Introductory Programming Course". *Proceedings of the 2022 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2022, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2210.14494).
- Yeon Seonwoo, Juhee Son, Jiho Jin, Sang-Woo Lee, Ji-Hoon Kim, Jung-Woo Ha, Alice Oh. "Two-Step Question Retrieval for Open-Domain QA". *Findings of the Association for Computational Linguistics: ACL 2022 (ACL-Findings 2022, Short)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2205.09393).
- Dongkwan Kim, Alice Oh. "Efficient Representation Learning of Subgraphs by Subgraph-To-Node Translation". *Workshop on Geometrical and Topological Representation Learning at ICLR 2022*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2204.04510v1).

**2021**

- Jooyeon Kim, Alice Oh. "Emergent Communication under Varying Sizes and Connectivities". *Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS 2021, Long)*.
- Sungjoon Park, Jihyung Moon, Sungdong Kim, Won Ik Cho, Ji Yoon Han, Jangwon Park, Chisung Song, Junseong Kim, Youngsook Song, Taehwan Oh, Joohong Lee, Juhyun Oh, Sungwon Lyu, Younghoon Jeong, Inkwon Lee, Sangwoo Seo, Dongjun Lee, Hyunwoo Kim, Myeonghwa Lee, Seongbo Jang, Seungwon Do, Sunkyoung Kim, Kyungtae Lim, Jongwon Lee, Kyumin Park, Jamin Shin, Seonghyun Kim, Lucy Park, Alice Oh, Jung-Woo Ha, Kyunghyun Cho. "KLUE: Korean Language Understanding Evaluation". *Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS 2021 Datasets and Benchmarks Track, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2105.09680).
- Yohan Jo, Haneul Yoo, JinYeong Bak, Alice Oh, Chris Reed, Eduard Hovy. "Knowledge-Enhanced Evidence Retrieval for Counterargument Generation". *Findings of the Association for Computational Linguistics: EMNLP 2021 (EMNLP-Findings 2021, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2109.09057).
- Jiseon Kim, Elden Griggs, In Song Kim, Alice Oh. "Learning Bill Similarity with Annotated and Augmented Corpora of Bills". *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2109.06527); DOI <https://doi.org/10.18653/v1/2021.emnlp-main.787>.
- Sungjoon Park, Jiseon Kim, Seonghyeon Ye, Jaeyeol Jeon, Hee Young Park, Alice Oh. "Dimensional Emotion Detection from Categorical Emotion". *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/1911.02499); DOI <https://doi.org/10.18653/v1/2021.emnlp-main.358>.
- Seonghyeon Ye, Jiseon Kim, Alice Oh. "Efficient Contrastive Learning via Novel Data Augmentation and Curriculum Learning". *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021, Short)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2109.05941).
- Jaimeen Ahn, Alice Oh. "Mitigating Language-Dependent Ethnic Bias in BERT". *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2109.05704).
- Yeon Seonwoo, Sang-Woo Lee, Ji-Hoon Kim, Jung-Woo Ha, Alice Oh. "Weakly Supervised Pre-Training for Multi-Hop Retriever". *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 (ACL-Findings 2021, Long)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2106.09983).
- Jeongmin Byun, Jungkook Park, Alice Oh. "Cocode: Providing Social Presence with Co-learner Screen Sharing in Online Programming Classes". *Proceedings of the ACM on Human-Computer Interaction Vol. 5, No. CSCW2 (CSCW 2021)*.
- Dongkwan Kim, Alice Oh. "How to Find Your Friendly Neighborhood: Graph Attention Design with Self-Supervision". *The Ninth International Conference on Learning Representations (ICLR 2021)*. [arXiv 사전 공개본 연결](https://arxiv.org/abs/2204.04879).
- Jeongmin Byun, Jungkook Park, Alice Oh. "Pythonpad: Server-free Python Hands-on Exercise for Online Programming Classes". *Proceedings of the 52nd ACM Technical Symposium on Computer Science Education (SIGCSE TS 2021, Poster)*.

## 사전 공개 원고

분류와 연도는 연구실 Manuscripts 구역의 표기다. 학술지·학회 출판 목록과 구분하여 arXiv 사전 공개본으로 적었다. 저자명 뒤 \*는 누리집 표시다.[^pubs]

| 연도 | 원고 · 상태 | 저자 |
|---|---|---|
| 2026 | [EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers](https://arxiv.org/abs/2608.02024) · arXiv 사전 공개본[^m1] | Junyeong Park\*, Jieun Han\*, Haneul Yoo, So-Yeon Ahn, Jinsung Yoon, Alice Oh |
| 2026 | [A Neuropsychologically Grounded Evaluation of LLM Cognitive Abilities](https://arxiv.org/abs/2603.02540) · arXiv 사전 공개본[^m2] | Faiz Ghifari Haznitrama, Faeyza Rishad Ardi, Alice Oh |
| 2026 | [Cultural Compass: A Framework for Organizing Societal Norms to Detect Violations in Human-AI Conversations](https://arxiv.org/abs/2601.07973) · arXiv 사전 공개본[^m3] | Myra Cheng, Vinodkumar Prabhakaran, Alice Oh, Hayk Stepanyan, Aishwarya Verma, Charu Kalia, Erin MacMurray van Liemt, Sunipa Dev |
| 2026 | [Solar Open Technical Report](https://arxiv.org/abs/2601.07022) · arXiv 사전 공개본[^m4] | Sungrae Park, Sanghoon Kim, Jungho Cho, Gyoungjin Gim, Dawoon Jung, Mikyoung Cha, Eunhae Choo, Taekgyu Hong, Minbyul Jeong, SeHwan Joo, Minsoo Khang, Eunwon Kim, Minjeong Kim, Sujeong Kim, Yunsu Kim, Hyeonju Lee, Seunghyun Lee, Sukyung Lee, Siyoung Park, Gyungin Shin, Inseo Song, Wonho Song, Seonghoon Yang, Seungyoun Yi, Sanghoon Yoon, Jeonghyun Ko, Seyoung Song, Keunwoo Choi, Hwalsuk Lee, Sunghun Kim, Du-Seong Chang, Kyunghyun Cho, Junsuk Choe, Hwaran Lee, Jae-Gil Lee, KyungTae Lim, Alice Oh |
| 2025 | [Understanding EFL Learners' Code-Switching and Teachers' Pedagogical Approaches in LLM-Supported Speaking Practice](https://arxiv.org/abs/2512.23136v1) · arXiv 사전 공개본[^m5] | Junyeong Park, Jieun Han, Yeon Su Park, Youngbin Lee, Suin Kim, Juho Kim, Alice Oh, So-Yeon Ahn |
| 2025 | [KORMo: Korean Open Reasoning Model for Everyone](https://arxiv.org/abs/2510.09426) · arXiv 사전 공개본[^m6] | Minjun Kim, Hyeonseok Lim, Hangyeol Yoo, Inho Won, Seungwoo Song, Minkyung Cho, Junhun Yuk, Changsu Choi, Dongjae Shin, Huije Lee, Hoyun Song, Alice Oh, Kyungtae Lim |
| 2025 | [Entangled in Representations: Mechanistic Investigation of Cultural Biases in Large Language Models](https://arxiv.org/abs/2508.08879v1) · arXiv 사전 공개본[^m7] | Haeun Yu, Seogyeong Jeong, Siddhesh Pawar, Jisu Shin, Jiho Jin, Junho Myung, Alice Oh, Isabelle Augenstein |
| 2025 | [BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge](https://arxiv.org/abs/2505.21092) · arXiv 사전 공개본[^m8] | Daeen Kabir, Minhajur Rahman Chowdhury Mahim, Sheikh Shafayat, Adnan Sadik, Arian Ahmed, Eunsu Kim, Alice Oh |
| 2025 | [Measuring Interest Group Positions on Legislation: An AI-Driven Analysis of Lobbying Reports](https://arxiv.org/abs/2504.15333) · arXiv 사전 공개본[^m9] | Jiseon Kim, Dongkwan Kim, Joohye Jeong, Alice Oh, In Song Kim |
| 2025 | [HERITAGE: An End-to-End Web Platform for Processing Korean Historical Documents in Hanja](https://arxiv.org/abs/2501.11951) · arXiv 사전 공개본[^m10] | Seyoung Song, Haneul Yoo, Jiho Jin, Kyunghyun Cho, Alice Oh |

## 공개 데모

연구실 Demos에 게시된 도구와 자료다. 게시 날짜가 없는 항목들이다.[^demos]

- CultureMix: 문화적 단서가 섞인 장면을 그림·글을 함께 다루는 모델이 이해하는지 살피는 연구 허브.
- JuICE: 언어 모델이 긴 답변에서 문화적 오류를 찾아내는지 평가하는 자료.
- HERITAGE: 한자 역사 문헌의 문장부호 복원·이름 식별·기계번역과 대화형 용어집을 제공하는 플랫폼.
- KoBBQ: 한국 문화의 사회적 편향을 묻는 평가 자료와 평가 코드.
- KOLD: 한국어 뉴스 댓글의 공격성과 혐오 대상을 표시한 자료.
- H2KE: 한자 역사 문헌을 현대 한국어와 영어로 번역하는 모델과 공개 번역.
- Mitigating Language-Dependent Ethnic Bias in BERT: 여러 언어의 언어 모델에서 민족적 편향을 분석·완화하는 연구 데모.

## 수상과 선정

Research의 수상·후보 표시 중 발표처의 학회·워크숍 연도로 시점이 확인되는 5건이다. 2025년 3건, 2024년 1건, 2023년 1건이며 원문의 수상 등급을 유지했다. Best Paper Nominated는 후보 선정이다.[^pubs]

- 2025 · One‑Topic‑Doesn’t‑Fit‑All: Transcreating Reading Comprehension Test for Personalized Learning, PALS @ EMNLP 2025 Best Paper
- 2025 · When Tom Eats Kimchi: Evaluating Cultural Bias of Multimodal Large Language Models in Cultural Mixture Contexts, C3NLP @ NAACL 2025 Outstanding Paper
- 2025 · WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines, NAACL 2025 Best Theme Paper
- 2024 · Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis, NAACL 2024 Resource Award
- 2023 · SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created through Human-Machine Collaboration, ACL 2023 Best Paper Nominated(후보 선정)

## 연락과 위치

- 연구실: KAIST 전산학부 건물 E3-1, 4417호.[^contact]
- 주소: 대전광역시 유성구 대학로 291, KAIST, 우편번호 34141.[^contact]
- 교수연구실: E3-1, 4404호.[^faculty]
- 교수 이메일: alice.oh@kaist.edu.[^members]
- 대학원·학부 연구 참여 안내: <https://uilab.kr/joinus>.[^joinus]
[^home]: Users & Information Lab., 첫 화면. 여러 언어·문화·공동체를 위한 AI를 목표로 평가 자료·평가 틀과 포용적이고 안전하며 사회적 맥락을 고려하는 방법을 개발한다고 소개한다. 연구 주제는 문화·다언어 AI, 언어 모델 평가, 안전·공정성·가치, 사회적 지능·계산 사회과학, 교육 AI, 모델 내부 해석이다. <https://uilab.kr/> (2026-11-01).
[^lab]: KAIST 전산학부, Users and Information Lab 소개. 대용량 사회 자료의 문제를 풀기 위한 기계학습 방법과 텍스트·소셜 네트워크 연구를 소개한다. <https://cs.kaist.ac.kr/research/labView?sn=83&menu=64> (2026-10-27).
[^faculty]: KAIST 전산학부, 오혜연 교수 소개. 직급, 전문 분야, 소속과 교수연구실. <https://cs.kaist.ac.kr/people/view?idx=18&kind=faculty&menu=160> (2026-11-01).
[^members]: Users & Information Lab., Members. 교수의 학력·영문 이름·이메일과 박사·석사과정, 졸업생의 학위·과정·연도·진로. <https://uilab.kr/members> (2026-11-01).
[^pubs]: Users & Information Lab., Research. 연도별 Publications·Manuscripts와 Presentations·Software 구역. <https://uilab.kr/research> (2026-11-01).
[^demos]: Users & Information Lab., Demos. 일곱 공개 데모·자료의 소개. <https://uilab.kr/demos> (2026-11-01).
[^contact]: Users & Information Lab., Contact. 연구실 주소. <https://uilab.kr/contact> (2026-11-01).
[^joinus]: Users & Information Lab., Join Us. 대학원 입학과 학부 연구 참여 안내. <https://uilab.kr/joinus> (2026-11-01).
[^p1]: J. Myung 외, A. Oh, arXiv (온라인 2024-06-14). <https://doi.org/10.48550/arXiv.2406.09948> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2406.09948> (2026-11-01).
[^p2]: H. Yoo, J. Jin, K. Cho, A. Oh, arXiv (온라인 2025-10-07). <https://doi.org/10.48550/arXiv.2510.05678> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.05678> (2026-11-01).
[^p3]: E. Kim 외, A. Oh, Findings of the Association for Computational Linguistics: ACL 2025, 26456–26493 (2025). <https://doi.org/10.18653/v1/2025.findings-acl.1357> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.findings-acl.1357/> (2026-11-01).
[^p4]: J. Jin 외, H. Lee, Transactions of the Association for Computational Linguistics 12, 507–524 (2024). <https://doi.org/10.1162/tacl_a_00661> 초록 기준(ACL Anthology 학술지 논문 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.tacl-1.28/> (2026-11-01).
[^p5]: H. Yoo, J. Han, S.-Y. Ahn, A. Oh, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 13439–13454 (2025). <https://doi.org/10.18653/v1/2025.acl-long.659> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.acl-long.659/> (2026-11-01).
[^p6]: J. Kim, E. Griggs, I. S. Kim, A. Oh, Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, 10048–10064 (2021). <https://doi.org/10.18653/v1/2021.emnlp-main.787> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2021.emnlp-main.787/> (2026-11-01).
[^p7]: S. Jeong 외, T. Kim, arXiv (온라인 2026-09-04). <https://doi.org/10.48550/arXiv.2609.04753> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.04753> (2026-11-01).
[^p8]: D. Kim, A. Oh, Proceedings of the 41st International Conference on Machine Learning 235, 24415–24436 (2024). <https://proceedings.mlr.press/v235/kim24aa.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/kim24aa.html> (2026-11-01).
[^m1]: Junyeong Park, Jieun Han, Haneul Yoo, So-Yeon Ahn, Jinsung Yoon, Alice Oh (연구실 게시 저자 순서), EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers. <https://arxiv.org/abs/2608.02024> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2608.02024 (2026-11-01).
[^m2]: Faiz Ghifari Haznitrama, Faeyza Rishad Ardi, Alice Oh (연구실 게시 저자 순서), A Neuropsychologically Grounded Evaluation of LLM Cognitive Abilities. <https://arxiv.org/abs/2603.02540> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2603.02540 (2026-11-01).
[^m3]: Myra Cheng, Vinodkumar Prabhakaran, Alice Oh, Hayk Stepanyan, Aishwarya Verma, Charu Kalia, Erin MacMurray van Liemt, Sunipa Dev (연구실 게시 저자 순서), Cultural Compass: A Framework for Organizing Societal Norms to Detect Violations in Human-AI Conversations. <https://arxiv.org/abs/2601.07973> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2601.07973 (2026-11-01).
[^m4]: Sungrae Park, Sanghoon Kim, Jungho Cho, Gyoungjin Gim, Dawoon Jung, Mikyoung Cha, Eunhae Choo, Taekgyu Hong, Minbyul Jeong, SeHwan Joo, Minsoo Khang, Eunwon Kim, Minjeong Kim, Sujeong Kim, Yunsu Kim, Hyeonju Lee, Seunghyun Lee, Sukyung Lee, Siyoung Park, Gyungin Shin, Inseo Song, Wonho Song, Seonghoon Yang, Seungyoun Yi, Sanghoon Yoon, Jeonghyun Ko, Seyoung Song, Keunwoo Choi, Hwalsuk Lee, Sunghun Kim, Du-Seong Chang, Kyunghyun Cho, Junsuk Choe, Hwaran Lee, Jae-Gil Lee, KyungTae Lim, Alice Oh (연구실 게시 저자 순서), Solar Open Technical Report. <https://arxiv.org/abs/2601.07022> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2601.07022 (2026-11-01).
[^m5]: Junyeong Park, Jieun Han, Yeon Su Park, Youngbin Lee, Suin Kim, Juho Kim, Alice Oh, So-Yeon Ahn (연구실 게시 저자 순서), Understanding EFL Learners' Code-Switching and Teachers' Pedagogical Approaches in LLM-Supported Speaking Practice. <https://arxiv.org/abs/2512.23136v1> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2512.23136 (2026-11-01).
[^m6]: Minjun Kim, Hyeonseok Lim, Hangyeol Yoo, Inho Won, Seungwoo Song, Minkyung Cho, Junhun Yuk, Changsu Choi, Dongjae Shin, Huije Lee, Hoyun Song, Alice Oh, Kyungtae Lim (연구실 게시 저자 순서), KORMo: Korean Open Reasoning Model for Everyone. <https://arxiv.org/abs/2510.09426> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2510.09426 (2026-11-01).
[^m7]: Haeun Yu, Seogyeong Jeong, Siddhesh Pawar, Jisu Shin, Jiho Jin, Junho Myung, Alice Oh, Isabelle Augenstein (연구실 게시 저자 순서), Entangled in Representations: Mechanistic Investigation of Cultural Biases in Large Language Models. <https://arxiv.org/abs/2508.08879v1> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2508.08879 (2026-11-01).
[^m8]: Daeen Kabir, Minhajur Rahman Chowdhury Mahim, Sheikh Shafayat, Adnan Sadik, Arian Ahmed, Eunsu Kim, Alice Oh (연구실 게시 저자 순서), BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge. <https://arxiv.org/abs/2505.21092> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2505.21092 (2026-11-01).
[^m9]: Jiseon Kim, Dongkwan Kim, Joohye Jeong, Alice Oh, In Song Kim (연구실 게시 저자 순서), Measuring Interest Group Positions on Legislation: An AI-Driven Analysis of Lobbying Reports. <https://arxiv.org/abs/2504.15333> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2504.15333 (2026-11-01).
[^m10]: Seyoung Song, Haneul Yoo, Jiho Jin, Kyunghyun Cho, Alice Oh (연구실 게시 저자 순서), HERITAGE: An End-to-End Web Platform for Processing Korean Historical Documents in Hanja. <https://arxiv.org/abs/2501.11951> 초록 기준(arXiv 사전 공개본). DOI 10.48550/arXiv.2501.11951 (2026-11-01).

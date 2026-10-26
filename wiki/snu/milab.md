# 머신 인텔리전스 연구실 (Machine Intelligence Lab, MILAB)

**서울대학교 공과대학 전기·정보공학부, 대학원 협동과정 인공지능전공 · 정교민 교수**

- 분야: 자연어 처리, 대형 언어 모델의 안전성과 지식 활용, 대화 검색, 논리 추론, 영상·언어 학습, 음성 합성, 그래프 학습
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^home][^p1][^p3], 생성 인공지능[^p5][^p8], 멀티모달 AI[^research][^p7], 음향·오디오 AI[^research][^p8], 그래프 기계학습·지식 그래프[^research], 컴퓨터 비전[^research][^p7]
- 홈페이지: <https://milab.snu.ac.kr/>
- 근거와 출처: [머신 인텔리전스 연구실 근거 페이지](milab-sources.md)

> 사람의 말과 글을 이해하고 생성하는 인공지능을 중심으로, 언어 모델이 안전하게 행동하고 지식을 활용하도록 만드는 방법, 대화에서 필요한 정보를 찾는 방법, 규칙을 추론하는 방법, 영상과 음성을 함께 다루는 학습을 연구한다.[^research][^p1][^p3][^p4][^p5][^p7][^p8]

## 무엇을 연구하나

정교민 교수가 이끄는 연구실로, 자연어 처리(컴퓨터로 사람의 말과 글을 분석하고 생성하는 기술), 딥러닝(여러 층의 신경망으로 자료의 특징과 관계를 배우는 방법), 데이터 분석과 웹 서비스를 연구한다.[^eceprof][^research] 질문에 맞는 답을 고르고 문맥에 맞는 답변을 만드는 질의응답, 앞선 대화를 고려하는 대화 시스템, 주변 문장과 언어적 특징을 활용하는 기계 번역을 주요 분야로 소개한다. 글·그림·음성처럼 종류가 다른 자료를 함께 배우는 멀티모달 학습도 연구한다. 이 밖에 개체와 관계를 점과 선으로 표현한 자료를 배우는 그래프 신경망, 여러 사람에게 일을 나누어 맡기고 결과를 모으는 크라우드소싱의 답 추정 알고리즘, 사용자 취향을 파악하는 추천 시스템, 뉴스 제목과 본문이 어긋나는지를 가리는 모델을 개발한다.[^research]

첫째 갈래는 대형 언어 모델(Large Language Model, LLM, 많은 글을 학습해 문맥에 맞는 글을 이해하고 생성하는 모델)의 안전성과 유해성 평가다. CausalArmor는 에이전트(주어진 목표에 따라 도구를 사용하고 행동을 정하는 인공지능)가 읽는 외부 문서나 도구 결과에 악성 명령이 숨어 있는 상황을 다룬다. 입력 일부를 제거해 보며 사용자 요청과 외부 자료가 행동 선택에 미치는 영향을 평가하고, 외부 자료가 사용자 의도를 압도할 때 해당 부분을 정리하는 선택적 방어를 제안했다.[^p1] LifeTox는 생활 조언처럼 문맥을 보아야 유해성을 판단할 수 있는 질문들을 담은 데이터셋(학습이나 평가에 쓰도록 모은 자료)과 유해성 분류 모델을 제시했다.[^p2]

둘째 갈래는 언어 모델이 지식을 이용하는 방식과 대화 검색이다. 학습 중 모델에 저장된 지식과 답변할 때 입력으로 받은 지식이 충돌하면 무엇을 따르는지 연구한다. 통제한 합성 말뭉치(실험 조건에 맞게 만든 글 모음)로 실험한 논문은 문서 안 반복, 일정한 정도의 문서 안 불일치, 지식 분포의 치우침이 함께 나타날 때 두 지식원을 균형 있게 쓰는 성질이 생김을 보였다.[^p3] IterCQR는 앞선 대화에 의존하는 질문을 독립적으로 검색할 수 있는 질문으로 고쳐 쓰는 방법이다. 사람이 만든 질문 수정문 대신 검색 성능에서 얻은 신호로 모델을 반복 학습한다.[^p4]

셋째 갈래는 사례에서 규칙을 알아내는 귀납 추론과 프로그램의 의미 검증이다. 언어 모델이 여러 가설을 만들더라도 뜻이 같은 가설을 반복하면 계산을 낭비할 수 있다. Mixture of Concepts(MoC)는 글의 품질을 유지하면서 의미가 다양한 가설을 생성하는 방법으로, 여러 귀납 추론 평가에서 성능이 향상됐다.[^p5] 또 자연어를 실행 가능한 프로그램으로 바꾸는 의미 분석 연구에서는 최종 답은 맞지만 뜻은 틀린 프로그램을 걸러 낸다. 각 프로그램을 여러 입력에서 실행한 결과로 표현한 뒤 다수결을 적용해 다른 프로그램들과 의미가 크게 다른 후보를 제거했다.[^p6]

넷째 갈래는 영상·언어 검색과 음성 생성이다. 영상 구간 검색은 글로 된 질문에 맞는 영상의 시간 구간을 찾는 일이다. MVMR는 정답 영상이 이미 주어졌다고 가정하는 대신, 방해 영상이 섞인 영상 집합에서 해당 구간을 찾도록 평가 조건을 바꾸고 학습 방법 CroCs를 제안했다.[^p7] 음성 합성(Text-to-Speech, TTS, 글을 말소리로 바꾸는 기술)에서는 여러 출력의 운율(말의 리듬·강세·높낮이)이 다양하도록 만드는 DPP-TTS를 제안했다. 듣는 사람이 느끼는 한 음성 안의 다양성과 여러 음성 사이의 다양성을 함께 고려하며, 비교 청취 평가에서 자연스러움을 고려하면서 운율을 다양화했다.[^p8]

## 주요 연구 주제

### 1. 언어 모델의 안전성과 유해성 평가

외부 자료에 숨겨진 명령이 에이전트의 행동을 바꾸는 간접 프롬프트 주입 공격을 방어하고, 생활 조언 속의 암묵적인 유해성을 분류하는 자료와 모델을 만든다. CausalArmor는 행동에 영향을 주는 입력을 평가하는 선택적 방어이고, LifeTox는 문맥을 고려하는 유해성 평가 자료다.[^p1][^p2]

### 2. 언어 지식 활용과 대화 검색

학습으로 얻은 지식과 입력 문맥의 지식을 모델이 선택하는 조건을 실험하고, 대화 이력을 반영한 검색 질문을 학습한다. 전자는 학습 자료의 성질과 모델 행동 사이의 관계를, 후자는 검색 결과를 이용해 질문 수정 모델을 학습하는 방법을 다룬다.[^p3][^p4]

### 3. 규칙 추론과 프로그램의 의미 검증

관측한 사례를 설명하는 가설을 다양하게 만들고, 정답만 일치하는 프로그램과 의미까지 일치하는 프로그램을 구별한다. 가설의 다양성을 높이는 MoC와 여러 입력의 실행 결과를 이용하는 프로그램 필터링을 연구했다.[^p5][^p6]

### 4. 영상 검색과 음성 생성

글로 묻는 영상 검색에서 방해 영상에 대한 반응까지 평가하고, 글에서 생성한 말소리의 운율을 다양하게 만든다. 여러 종류의 자료를 연결하는 학습과 생성 결과의 평가를 함께 다루는 연구다.[^p7][^p8]

## 대표 논문

정교민 교수가 저자로 참여한 서울대 재직 시기의 2021–2026년 논문에서 네 갈래를 두 편씩 골랐다. 2026년 연구를 포함했고, 아래 교수 역할은 읽은 초록 페이지의 저자 순서만 따른다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 3번의 연도와 학회명은 연구실의 ACL 2026 표기이며, 설명은 같은 제목의 arXiv 수정판을 따른다.[^pubs]

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution](https://arxiv.org/abs/2602.07918) · ICML 2026, arXiv 판 | 도구를 쓰는 인공지능은 외부 자료에 숨은 명령 때문에 허가받지 않은 행동을 할 수 있다. 사용자 요청과 외부 자료의 일부를 빼 보며 행동 선택에 대한 영향을 계산하고, 외부 자료가 사용자 의도를 압도할 때 필요한 부분만 정리한다. 이미 오염된 추론 내용이 다음 행동에 쓰이지 않도록 가리는 방법도 썼다. 두 평가 환경에서 강한 방어 방법에 맞먹는 보안 수준을 보이면서 유용성과 응답 지연을 유지했다고 보고했다.[^p1] | 8명 중 5번째 저자 |
| 2 | 2024 | [LifeTox: Unveiling Implicit Toxicity in Life Advice](https://doi.org/10.18653/v1/2024.naacl-short.60) · NAACL | 일상적인 조언을 구하는 질문에서 문맥에 따라 드러나는 유해성을 찾기 위한 자료 LifeTox를 만들었다. 개인 경험에서 나온 개방형 질문으로 다양한 상황을 담았다. 이 자료로 추가 학습한 RoBERTa 모델은 유해성 분류에서 예시를 주지 않고 사용한 대형 언어 모델의 성능에 맞먹거나 이를 넘었다. 자료와 유해성 판별 모델을 공개했다.[^p2] | 마지막 저자 |
| 3 | 2026 | [How Training Data Shapes the Use of Parametric and In-Context Knowledge in Language Models](https://arxiv.org/abs/2510.02370) · ACL 2026(연구실 표기), arXiv v3 | 모델이 학습 중 얻은 지식과 답변할 때 입력으로 받은 지식이 충돌하면 어떤 쪽을 따르는지 연구했다. 합성한 글 모음의 조건을 통제한 실험에서 문서 안 반복, 일정한 정도의 문서 안 불일치, 지식 분포의 치우침이 함께 있어야 두 지식원을 안정적으로 활용하는 성질이 나타났다. 실제 언어 모델의 사전 학습에서도 이런 현상을 보였고, 후속 학습이 지식 선택 전략을 어떻게 바꾸는지 분석했다.[^p3] | 6명 중 5번째 저자 |
| 4 | 2024 | [IterCQR: Iterative Conversational Query Reformulation with Retrieval Guidance](https://doi.org/10.18653/v1/2024.naacl-long.449) · NAACL | 대화의 앞부분을 알아야 이해할 수 있는 질문을 검색기에 바로 넣을 수 있는 질문으로 고쳐 쓴다. 사람이 작성한 수정문에 의존하지 않고, 검색에서 얻는 신호를 보상으로 삼아 질문 수정 모델을 반복 학습한다. 두 데이터셋과 서로 다른 검색 방식에서 성능을 평가했고, 처음 보는 자료와 학습 자료가 적은 조건에서도 효과를 보였다.[^p4] | 마지막 저자 |
| 5 | 2025 | [Generating Diverse Hypotheses for Inductive Reasoning](https://doi.org/10.18653/v1/2025.naacl-long.429) · NAACL | 사례를 설명할 규칙을 언어 모델이 여러 번 생성하면 의미가 겹치는 가설이 생긴다. 출력의 다양성을 조절하는 설정값만 높이는 방식은 글의 품질이 무너져 한계가 있음을 분석했다. 글의 품질과 의미적 다양성을 함께 고려하는 MoC를 제안했고, 여러 귀납 추론 평가에서 기존 후보 생성 방식보다 성능이 향상됐다.[^p5] | 마지막 저자 |
| 6 | 2023 | [Weakly Supervised Semantic Parsing with Execution-based Spurious Program Filtering](https://doi.org/10.18653/v1/2023.emnlp-main.425) · EMNLP | 최종 답만 맞고 뜻은 틀린 프로그램이 학습에 섞이는 문제를 다룬다. 프로그램마다 여러 입력에서의 실행 결과를 모아 의미를 표현하고, 그 표현들에 다수결을 적용해 다른 후보들과 의미가 크게 다른 프로그램을 걸러 낸다. 기존 프로그램 탐색 방식에 덧붙일 수 있으며, 시각적 논리 추론과 표를 이용하는 질의응답 평가에서 성능이 향상됐다.[^p6] | 마지막 저자 |
| 7 | 2024 | [MVMR: A New Framework for Evaluating Faithfulness of Video Moment Retrieval against Multiple Distractors](https://doi.org/10.1145/3627673.3679838) · CIKM 2024, arXiv 판 | 질문과 맞는 구간을 찾을 때 정답 영상이 이미 주어졌다고 가정하면, 잘못된 영상에서도 모델이 확신하는 문제를 드러내기 어렵다. 방해 영상이 섞인 영상 집합에서 구간을 찾는 MVMR 과제와 자료 구축 방법을 제안했다. 서로 다른 두 방식으로 자료 사이의 구별을 학습하는 CroCs도 제안했고, 실험에서 방해 영상에 대응하는 성능을 보였다.[^p7] | 마지막 저자 |
| 8 | 2023 | [DPP-TTS: Diversifying prosodic features of speech via determinantal point processes](https://doi.org/10.18653/v1/2023.emnlp-main.267) · EMNLP | 같은 글을 읽어도 운율이 다양한 음성을 만들기 위한 합성 모델이다. 개별 음성 안의 지각적 다양성과 여러 음성 사이의 다양성을 함께 고려하도록, 여러 결과의 다양성을 다루는 수학적 확률 모형과 운율 다양화 모듈을 결합했다. 나란히 듣고 비교하는 평가에서 자연스러움을 고려하면서 기존 방법보다 운율이 다양한 음성을 만들었다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

정교민 교수(Kyomin Jung)는 서울대학교 공과대학 전기·정보공학부 교수이며 대학원 협동과정 인공지능전공 교수진에도 올라 있다.[^eceprof][^gsai] 교수 개인 페이지는 서울대 수리과학부 겸임교수도 맡고 있다고 소개한다.[^faculty] 서울대학교 수학과에서 학사 학위(2003년), MIT 수학과에서 박사 학위(2009년)를 받았다. 2009–2013년 KAIST 전산학과 조교수를 지냈고, 2013년 서울대 전기·정보공학부 조교수로 부임해 2016–2021년 부교수, 2021년부터 정교수로 재직하고 있다.[^eceprof] 2021–2023년 학부 학생 담당 부학부장을 맡았다.[^faculty]

교수 소개는 전문 분야를 자연어 처리, 딥러닝 알고리즘, 데이터 분석과 웹 서비스로 적는다.[^faculty] 최근 대표 논문으로 보면 언어 모델의 안전성과 유해성 평가, 모델 안 지식과 입력 지식의 활용, 대화 검색, 규칙 추론과 프로그램 검증, 영상 검색과 음성 생성으로 구체화된다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8] 학술 활동으로는 AAAI 2022 Senior Technical Program Committee와 Knowledge and Information Systems의 Associate Editor(2022년 표기), EMNLP·ICML·ACL 2021의 심사 활동이 게시되어 있다.[^faculty]

## 응용 분야

연구실은 외부 지식을 활용하는 질의응답과 대화형 비서, 문맥을 반영한 기계 번역, 글·그림을 이용하는 질문 응답과 글·음성을 함께 다루는 감정 인식, 음성 인식, 추천 서비스, 뉴스 제목과 본문 불일치 검출을 응용 분야로 소개한다.[^research] 대표 논문의 구체적인 쓰임은 도구 사용 에이전트에 대한 간접 명령 주입 방어, 생활 조언의 유해성 분류, 대화 검색 질문의 자동 수정, 방해 영상이 있는 환경에서의 영상 구간 검색, 운율이 다양한 말소리 생성이다.[^p1][^p2][^p4][^p7][^p8]

## 구성원

2026년 10월 26일 연구실 Members 페이지의 Current Students 17명이다. 게시 과정은 Ph.D. Candidate 10명과 M.S. Candidate 7명이며, 연구 주제와 학교 이메일은 이름별 게시 표기를 따른다. Minsung Kim의 Lab Representative 표기도 함께 적었다.[^members] "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Yunah Jang | 박사과정 | Natural Language Processing Sentiment Analysis | vn2209@snu.ac.kr | 4 |
| Seongho Joo | 박사과정 | Differential Privacy Unlearning for LLMs | seonghojoo@snu.ac.kr | 8 |
| Dongryeol Lee | 박사과정 | Question Answering Evaluation | drl123@snu.ac.kr | 5 |
| Younhyung Chae | 박사과정 | LLM Agent Reasoning | yhchae0811@snu.ac.kr |  |
| Hyukhun Koh | 박사과정 | Educational Reliable Agentic AI | hyukhunkoh-ai@snu.ac.kr | 5, 8 |
| Jahyun Koo | 박사과정 | Efficient AI | koojahyun@snu.ac.kr | 2 |
| Minsung Kim | 박사과정 (Lab Representative) | LLM training | kms0805@snu.ac.kr | 3, 5, 7 |
| Kyungmin Min | 박사과정 | Multimodal LLM Multi-agent System | kyungmin97@snu.ac.kr |  |
| Minha Jhang | 박사과정 | Diffusion Model Text Generation | jminha2014@snu.ac.kr |  |
| Kyeongman Park | 박사과정 | Generation Task | zzangmane@snu.ac.kr |  |
| Jiwon Moon | 석사과정 | Instruction Following Agentic AI | wldnjs913@snu.ac.kr |  |
| Junseok Kim | 석사과정 | LLM based Multi Agent Collaboration Personalized LLM | kim.junseok@snu.ac.kr |  |
| Sangmook Lee | 석사과정 | Reasoning | helmsman@snu.ac.kr |  |
| Dohyung Kim | 석사과정 | Reasoning Diffusion Models | kimdohyung@snu.ac.kr |  |
| Junsu Park | 석사과정 | World Model Diffusion Language Model | junsu0115@snu.ac.kr |  |
| Dongyeon Kim | 석사과정 | Small Language Models Personalization | topswamp@snu.ac.kr |  |
| Hyojeong Yu | 석사과정 | LLM Personalization Controllable Text Generation | hyoj.yu@snu.ac.kr |  |

## 졸업생과 이전 구성원

Members 페이지의 Alumni 35명이다. 학위·과정과 시기, 진로는 랩 게시 표기다. 학위나 연도가 함께 적힌 경우와 진로만 적힌 경우를 구분했다. 교수의 서울대 부임 전인 2011–2013년 이전 구성원도 함께 있는 목록이다.[^members][^eceprof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 황예린 Yerin Hwang | Ph.D. (Fall 2026) | Assistant Professor in Department of Computer Science and Artificial Intelligence at Dongguk University |
| 김민범 Minbeom Kim | Ph.D. (Fall 2026) | SK hynix Research |
| 이강일 Kangil Lee | Ph.D. (Fall 2026) | Postdoc researcher @ MLML KAIST |
| 양낙영 Nakyeong Yang | Postdoc (Fall 2026) | Postdoc at Max Planck Institute for Software Systems |
| 김용일 Yongil Kim | Ph.D. (Fall 2024) | Assistant Professor in Department of Artificial Intelligence at Catholic University |
| 이윤형 Yoonhyung Lee | Ph.D. (Fall 2024) | Qualcomm AI Research, Korea |
| 이민우 Minwoo Lee | Ph.D. (Spring 2024) | LG AI Research |
| 원승필 Seungpil Won | Ph.D. (Spring 2023) | LG AI Research |
| 유총재 Chongjae Yoo | M.S. (Spring 2023) | LG전자 |
| 이환희 Hwanhee Lee | Ph.D. (Fall 2022) | Assistant Professor in Department of Artificial Intelligence at Chung-Ang University |
| 곽희영 Heeyoung Kwak | Ph.D. (Fall 2022) | NAVER AI Lab |
| 강태관 Taegwan Kang | Ph.D. (Fall 2022) | LG AI Research |
| 김세광 Segwang Kim | Ph.D. (Fall 2022) | Samsung Electronics |
| 윤현구 Hyeongu Yun | Ph.D. (Fall 2022) | DE Shaw Research |
| 최병진 Byungjin Choe | Ph.D. (Spring 2022) | Samsung Research |
| 배현경 Hyunkyung Bae | M.S. (Spring 2022) | LG AI Research |
| 황용근 Youngkeun Hwang | Ph.D. (Spring 2022) | 42dot |
| 김양훈 Yanghoon Kim | Ph.D. (Fall 2021) | 미래에셋 자산운용 |
| 신중보 Joongbo Shin | Ph.D. (Spring 2021) | LG AI Research |
| 이동현 Donghyeon Lee | Ph.D. (Spring 2021) |  |
| 김준영 Joonyoung Kim | Ph.D. (Spring 2021) | Samsung Research |
| 윤승현 Seunghyun Yoon | Ph.D. (Fall 2020) | Adobe Research, San Jose |
| 최준영 Joonyoung Choi | M.S. (Spring 2020) | NC SOFT |
| 변석현 Seokhyun Byun | M.S. (Spring 2019) | LinkedIn, Dublin |
| Pablo Estarda | M.S. (Fall 2016) | Google, Seattle |
| 김정명 Jungmyung Kim | M.S. (Fall 2015) | NAVER Clova AI Research |
| 임성수 Sungsu Lim |  | Assistant Professor in Department of Computer Science and Engineering at Chungnam University |
| 임용섭 Yongsub Lim |  | Founder & Principal Data Scientist of MAKINA ROCKS (in Seoul, Korea, and Sunny Vale, CA, USA) |
| 임우상 Woosang Lim |  | Senior Applied ML Scientist in Microsoft AI and Research |
| 김민환 Minhwan Kim | (Spring 2013) | CTO & Co-founder at Unveiled Inc |
| 강병곤 Byungkon Kang | (Spring 2013) | Assistant Professor in Department of Computer Science at SUNY Korea |
| 허우람 Wooram Heo | (Spring 2012) | NHN |
| 이슬기 Seulki Lee | (Spring 2012) | LEGO BrickLink, Inc |
| 곽남주 Nam-ju Kwak | (Summer 2011) | 한국산업은행 |
| 김보영 Boyoung Kim | (Summer 2011) | 코오롱인베스트먼트 |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 국제 학회, 학술지, 워크숍, 국내 학회 네 구획에서 2021–2026년으로 적은 119행이다. 같은 제목이라도 학회와 워크숍에 따로 실린 행은 각각 적고, 저자·제목·발표처와 연월은 랩 표기를 따른다. 2021년은 해당 연도의 전체 항목을 포함한다. LiSA의 NeurIPS 2026 항목은 첫 화면이 채택을 알린 발표 전 논문이다. Erase or Hide? 항목은 학회명을 ICLR 2026, 행사 시기를 April 2027로 함께 적은 누리집 표기를 따른다.[^pubs][^home]

**2026**

- Minbeom Kim, Lesly Miculicich, Bhavana Dalvi Mishra, Mihir Parmar, Phillip Wallis, Bharath Chandrasekhar, Kyomin Jung, Tomas Pfister, and Long T. Le. "LiSA: Lifelong Safety Adaptation via Conservative Policy Induction". *NeurIPS 2026 December 2026 Sydney, Australia*.
- Hyukhun Koh, Seongho Joo, Haesung Pyun, Kyomin Jung. "When i.i.d. Factorization Breaks Language: The Structural Failure of Discrete Diffusion Language Models". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Jiwon Moon, Yerin Hwang, Kyomin Jung. "Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Yunah Jang, Megha Sundriyal, Kyomin Jung, Meeyoung Cha. "How You Ask Matters! Adaptive RAG Robustness to Query Variations". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Yerin Hwang, Jiwon Moon, Changho Lee, Kwangmin Ki, taegwan kang, Jinsik Lee, Honglak Lee, Kyomin Jung. "How Instruction Hierarchy Breaks Under Pairwise Multi-Conflict Pressure". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Sangmook Lee, Minbeom Kim, Jeonghye Kim, Dohyung Kim, Sojeong Rhee, Kyomin Jung. "Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung. "PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations". *EMNLP 2026 October 2026 Budapest, Hungary*.
- Yunah Jang, Kang-il Lee, Joongbo Shin, Kyomin Jung. "CompCQR: Compositional Query Generation for Training-Free Conversational Search". *Findings of EMNLP 2026 October 2026 Budapest, Hungary*.
- Kyeongman Park, Kang-il Lee, Janghoon Han, Yerin Hwang, taegwan kang, Minwoo Lee, Changho Lee, Kyomin Jung. "A Benchmark for the Generation and Evaluation of Scientific Architecture Diagrams in HTML/SVG". *Findings of EMNLP 2026 October 2026 Budapest, Hungary*.
- Junseok Kim, Nakyeong Yang, Kyomin Jung. "Personalized Privacy Control in LLMs via Attention Head Intervention". *Findings of EMNLP 2026 October 2026 Budapest, Hungary*.
- Kyungmin Min, Minbeom Kim, Kang-il Lee, Seunghyun Yoon, Kyomin Jung. "ReflectCAP: Detailed Image Captioning with Reflective Memory". *ECCV 2026 September 2026 Malmö, Sweden*.
- Minbeom Kim, Mihir Parmar, Phillip Wallis, Lesly Miculicich, Kyomin Jung, Krishnamurthy Dj Dvijotham, Long T. Le, and Tomas Pfister. "CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution". *ICML 2026 July 2026 Seoul, South Korea*.
- Dohyung Kim, Minbeom Kim, Jeonghye Kim, Sangmook Lee, Sojeong Rhee, and Kyomin Jung. "Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR". *ICML 2026 July 2026 Seoul, South Korea*.
- Seongho Joo, Hyukhun Koh, and Kyomin Jung. "PEARL: Differentially Private and Entropy-Aware Regulated Language Generation". *ICML 2026 July 2026 Seoul, South Korea*.
- Minsung Kim, Dong-Kyum Kim, Jea Kwon, Nakyeong Yang, Kyomin Jung, and Meeyoung Cha. "How Training Data Shapes the Use of Parametric and In-Context Knowledge in Language Models". *The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) July 2026 San Diego, USA*.
- Minha Jhang, Kyeongman Park, Hyukhun Koh, and Kyomin Jung. "Evaluating Visual Narrative Coherence in Story Visualization via Diversified Storylines". *The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) oral July 2026 San Diego, USA*.
- Junseok Kim, Nakyeong Yang, Kyungmin Min, and Kyomin Jung. "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning". *Findings of the Association for Computational Linguistics: ACL 2026 (Findings of ACL) July 2026 San Diego, USA*.
- Minsung Kim, Nakyeong Yang, and Kyomin Jung. "Rethinking Post-Unlearning Behavior of Large Vision-Language Models". *Findings of the Association for Computational Linguistics: ACL 2026 (Findings of ACL) July 2026 San Diego, USA*.
- Kyeongman Park, Minha Jhang, and Kyomin Jung. "A Universal Avoidance Method for Diverse Multi-branch Generation". *Findings of the Association for Computational Linguistics: ACL 2026 (Findings of ACL) July 2026 San Diego, USA*.
- Nakyeong Yang, Dong-Kyum Kim, Jea Kwon, Minsung Kim, Kyomin Jung, and Meeyoung Cha. "Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning". *The Fourteenth International Conference on Learning Representations (ICLR 2026) April 2027 Rio de Janeiro, Brazil*.
- Jiwon Moon, Yerin Hwang, Dongryeol Lee, Taegwan Kang, Yongil Kim, and Kyomin Jung. "Don't Judge Code by Its Cover: Exploring Biases in LLM Judges for Code Evaluation". *Findings of The 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) March 2026 Rabat, Morocco*.
- Junseok Kim, Nakyeong Yang, and Kyomin Jung. "Persona Switch: Mixing Distinct Perspectives in Decoding Time". *Findings of The 19th Conference of the European Chapter of the Association for Computational Linguistics (Findings of EACL 2026) March 2026 Rabat, Morocco*.
- Sangmook Lee\*, Dohyung Kim\*, Hyukhun Koh, Nakyeong Yang, and Kyomin Jung. "Confidence-Guided Stepwise Model Routing for Cost-Efficient Reasoning". *The 40th Annual AAAI Conference on Artificial Intelligence (AAAI 2026) January 2026 Singapore*.
- Sangmook Lee , Minbeom Kim, Jeonghye Kim , Dohyung Kim , Sojeong Rhee , and Kyomin Jung. "Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning". *ICML 2026 AI for Math Workshop spotlight July 2026 Seoul, South Korea*.
- Hyojeong Yu\*, Hyukhun Koh\*, Minsung Kim, and Kyomin Jung. "Casual as an Anchor: Resolving Supervision Misalignment in Formality Transfer Dataset". *CHI Workshop on Human-Centered Evaluation and Auditing of Language Models April 2026 Barcelona, Spain*.
- Junsu Park, Kyomin Jung. "Instructional Video 기반 멀티모달 절차 계획 생성 방식 비교". *정보과학회 August 2026*.

**2025**

- Junseok Kim, Nakyeong Yang, and Kyomin Jung. "Persona is a Double-Edged Sword: Rethinking the Impact of Role-play Prompts in Zero-shot Reasoning Tasks". *International Joint Conference on Natural Language Processing & Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025) December 2025 Mumbai, India*.
- Kang-il Lee, Jahyun Koo, Seunghyun Yoon, Minbeom Kim, Hyukhun Koh, Dongryeol Lee, and Kyomin Jung. "Program Synthesis via Test-Time Transduction". *The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS 2025) December 2025 San Diego, CA, USA*.
- Hyukhun Koh\*, Minha Jhang\*, Dohyung Kim, Sangmook Lee, and Kyomin Jung. "Conditional [MASK] Discrete Diffusion Language Model". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Kyeongman Park, Nakyeong Yang, and Kyomin Jung. "Avoidance Decoding for Diverse Multi-Branch Story Generation". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Yerin Hwang\*, Dongryeol Lee\*, Kyungmin Min, Taegwan Kang, Yongil Kim, and Kyomin Jung. "Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Nakyeong Yang, Minsung Kim, Seunghyun Yoon, Joongbo Shin, and Kyomin Jung. "FaithUn: Toward Faithful Forgetting in Language Models by Investigating the Interconnectedness of Knowledge". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Seongho Joo, Hyukhun Koh, and Kyomin Jung. "Harmful Prompt Laundering: Jailbreaking LLMs with Abductive Styles and Symbolic Encoding". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Jeonghye Kim\*, Sojeong Rhee\*, Minbeom Kim, Dohyung Kim, Sangmook Lee, Youngchul Sung, and Kyomin Jung. "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection". *The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) November 2025 Suzhou, China*.
- Seongho Joo, Hyukhun Koh, and Kyomin Jung. "Public Data Assisted Differentially Private In-Context Learning". *Findings of The 2025 Conference on Empirical Methods in Natural Language Processing (Findings of EMNLP 2025) November 2025 Suzhou, China*.
- Yerin Hwang, Dongryeol Lee, Taegwan Kang, Yongil Kim, and Kyomin Jung. "Can You Trick the Grader? Adversarial Persuasion of LLM Judges". *Findings of The 2025 Conference on Empirical Methods in Natural Language Processing (Findings of EMNLP 2025) November 2025 Suzhou, China*.
- Minbeom Kim, Kang-il Lee, Seongho Joo, Hwaran Lee, Thibaut Thonet, and Kyomin Jung. "Drift: Decoding-time Personalized Alignments with Implicit User Preferences". *Findings of The 2025 Conference on Empirical Methods in Natural Language Processing (Findings of EMNLP 2025) November 2025 Suzhou, China*.
- Nakyeong Yang, Jiwon Moon, Junseok Kim, Yunah Jang, and Kyomin Jung. "Unplug and Play Language Models: Decomposing Experts in Language Models at Inference Time". *The 34th ACM International Conference on Information and Knowledge Management (CIKM 2025) November 2025 Seoul, Korea*.
- Kyeongman Park, Seongho Joo, and Kyomin Jung. "MultiActor-Audiobook: Zero-Shot Audiobook Generation with Faces and Voices of Multiple Speakers". *26th edition of the Interspeech Conference (InterSpeech 2025) August 2025 Rotterdam, The Netherlands*.
- Yerin Hwang, Yongil Kim, Jahyun Koo, Taegwan Kang, Hyunkyung Bae, and Kyomin Jung. "LLMs can be easily Confused by Instructional Distractions". *The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) July 2025 Vienna, Austria*.
- Kyeongman Park, Minbeom Kim, and Kyomin Jung. "A Character-Centric Creative Story Generation via Imagination". *The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) July 2025 Vienna, Austria*.
- Minbeom Kim, Thibaut Thonet, Jos Rozen, Hwaran Lee, Kyomin Jung, and Marc Dymetman. "Guaranteed Generation from Large Language Models". *The Thirteenth International Conference on Learning Representations (ICLR 2025) April 2025 Singapore, Singapore*.
- Dongryeol Lee\*, Yerin Hwang\*, Yongil Kim, Joonsuk Park, and Kyomin Jung. "Are LLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers on LLM-based Evaluation". *2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) Oral April 2025 New Mexico, USA*.
- Kang-il Lee, Hyukhun Koh, Dongryeol Lee, Seunghyun Yoon, Minsung Kim, and Kyomin Jung. "Generating Diverse Hypotheses for Inductive Reasoning". *2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) Oral April 2025 New Mexico, USA*.
- Minbeom Kim, Hwanhee Lee, Joonsuk Park, Hwaran Lee, and Kyomin Jung. "AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence". *2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) April 2025 New Mexico, USA*.
- Jahyun Koo, Yerin Hwang, Yongil Kim, Taegwan Kang, Hyunkyung Bae, and Kyomin Jung. "SWITCH: Studying with Teacher for Knowledge Distillation of Large Language Models". *Findings of The 2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (Findings of NAACL) April 2025 New Mexico, USA*.
- Kang-il Lee, Minbeom Kim, Seunghyun Yoon, Minsung Kim, Dongryeol Lee, Hyukhun Koh, and Kyomin Jung. "VLind-Bench: Measuring Language Priors in Large Vision-Language Models". *Findings of The 2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (Findings of NAACL) April 2025 New Mexico, USA*.
- Kyungmin Min, Minbeom Kim, Kang-il Lee, Dongryeol Lee, and Kyomin Jung. "Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding". *Findings of The 2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (Findings of NAACL) April 2025 New Mexico, USA*.
- Dongryeol Lee, Minwoo Lee, Kyungmin Min, Joonsuk Park, and Kyomin Jung. "Return of EM: Entity-driven Answer Set Expansion for QA Evaluation". *The 31st International Conference on Computational Linguistics (COLING) Oral January 2025 Abu Dhabi, UAE*.
- Yoonhyung Lee, and Kyomin Jung. "adaStride: Using Time Adaptive Strides in Audio Data for Effective Downsampling". *Computer Speech and Langauge January 2025*.

**2024**

- Hyukhun Koh, Dohyung Kim, Minwoo Lee, and Kyomin Jung. "Can LLMs Recognize Toxicity? A Structured Investigation Framework and Toxicity Metric". *Findings of the The 2024 Conference on Empirical Methods in Natural Language Processing (Findings of EMNLP) November 2024 Miami, USA*.
- Yerin Hwang, Yongil Kim, Yunah Jang, Jeesoo Bang, Hyunkyung Bae, and Kyomin Jung. "MP2D: An Automated Topic Shift Dialogue Generation Framework Leveraging Knowledge Graphs". *The 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP) November 2024 Miami, USA*.
- Nakyeong Yang, Minsung Kim, Seunghyun Yoon, Joongbo Shin, and Kyomin Jung. "MVMR: A New Framework for Evaluating Faithfulness of Video Moment Retrieval against Multiple Distractors". *33rd ACM International Conference on Information and Knowledge Management (CIKM) Oral October 2024 Boise, USA*.
- Nakyeong Yang, Taegwan Kang, Jungkyu Choi, Honglak Lee, and Kyomin Jung. "Mitigating Biases for Instruction-following Language Models via Bias Neurons Elimination". *The 62nd Annual Meeting of the Association for Computational Linguistics (ACL) August 2024 Bangkok, Thailand*.
- Minbeom Kim, Jahyun Koo, Hwanhee Lee, Joonsuk Park, Hwaran Lee, and Kyomin Jung. "LifeTox: Unveiling Implicit Toxicity in Life Advice". *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) Oral June 2024 Mexico city, Mexico*.
- Minwoo Lee, Hyukhun Koh, Minsung Kim, and Kyomin Jung. "Fine-grained Gender Control in Machine Translation with Large Language Models". *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) June 2024 Mexico city, Mexico*.
- Yunah Jang, Kang-il Lee, Hyunkyung Bae, Hwanhee Lee, and Kyomin Jung. "IterCQR: Iterative Conversational Query Reformulation with Retrieval Guidance". *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) June 2024 Mexico city, Mexico*.
- Yerin Hwang, Yongil Kim, Hyunkyung Bae, Jeesoo Bang, Hwanhee Lee, and Kyomin Jung. "Kosmic: Korean Text Similarity Metric Reflecting Honorific Distinctions". *The 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING) May 2024 Italy*.
- Kyeongman Park, Nakyeong Yang, and Kyomin Jung. "LongStory: Coherent, Complete and Length Controlled Long story Generation". *Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD) Oral May 2024 Taipei, Taiwan*.
- Yoonhyung Lee, and Kyomin Jung. "Boosting Speech Enhancement with Clean Self-Supervised Features via Conditional Variational Autoencoders". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) April 2024 Korea*.
- Kyungmin Min, Minbeom Kim, Kang-il Lee, Dongryeol Lee, and Kyomin Jung. "Mitigating Hallucinations in LVLMs via Summary-Guided Decoding". *Neurips Workshop on Safe Generative AI December 2024 Vancouver, Canada*.
- Dongryeol Lee, Kyungmin Min, Yerin Hwang, Joonsuk Park, and Kyomin Jung. "Reference-Centric QA Evaluation Leveraging Contrastive Decoding". *정보과학회 December 2024*.

**2023**

- Seongho Joo, Hyukhun Koh, and Kyomin Jung. "DPP-TTS: Diversifying prosodic features of speech via determinantal point processes". *The 2023 Conference on Empirical Methods in Natural Language Processing: EMNLP 2023 (EMNLP) December 2023 Singapore, Singapore*.
- Kang-il Lee, Segwang Kim, and Kyomin Jung. "Weakly Supervised Semantic Parsing with Execution-based Spurious Program Filtering". *The 2023 Conference on Empirical Methods in Natural Language Processing: EMNLP 2023 (EMNLP) December 2023 Singapore, Singapore*.
- Minwoo Lee, Hyukhun Koh, Kang-il Lee, Dongdong Zhang, Minsung Kim, and Kyomin Jung. "Target-Agnostic Gender-Aware Contrastive Learning for Mitigating Bias in Multilingual Machine Translation". *The 2023 Conference on Empirical Methods in Natural Language Processing: EMNLP 2023 (EMNLP) December 2023 Singapore, Singapore*.
- Yerin Hwang\*, Yongil Kim\*, Hyunkyung Bae, Hwanhee Lee, Jeesoo Bang, and Kyomin Jung. "Dialogizer: Context-aware Conversational-QA Dataset Generation from Textual Sources". *The 2023 Conference on Empirical Methods in Natural Language Processing: EMNLP 2023 (EMNLP) December 2023 Singapore, Singapore*.
- Dongryeol Lee\*, Segwang Kim\*, Minwoo Lee, Hwanhee Lee, Joonsuk Park, Sang-woo Lee, and Kyomin Jung. "Asking Clarification Questions to Handle Ambiguity in Open-Domain QA". *Findings of the Association for Computational Linguistics: EMNLP 2023 (Findings of EMNLP) December 2023 Singapore, Singapore*.
- Yongil Kim, Yerin Hwang, Hyeongu Yun, Seunghyun Yoon, Trung Bui, and Kyomin Jung. "PR-MCS: Perturbation Robust Metric for MultiLingual Image Captioning". *Findings of the Association for Computational Linguistics: EMNLP 2023 (Findings of EMNLP) December 2023 Singapore, Singapore*.
- Seungpil Won, Heeyoung Kwak, Joongbo Shin, Janghoon Han, and Kyomin Jung. "BREAK: Breaking the Dialogue State Tracking Barrier with Beam Search and Re-ranking". *60th Annual Meeting of the Association for Computational Linguistics: ACL 2023 (ACL) July 2023 Toronto, Canada*.
- Minbeom Kim, Hwanhee Lee, Kang Min Yoo, Joonsuk Park, Hwaran Lee, and Kyomin Jung. "Critic-Guided Decoding for Controlled Text Generation". *60th Annual Meeting of the Association for Computational Linguistics: ACL 2023 (ACL) spotlight July 2023 Toronto, Canada*.
- Yongil Kim\*, Yerin Hwang\*, Joongbo Shin, Hyunkyung Bae, and Kyomin Jung. "Injecting Comparison Skills in Task-Oriented Dialogue Systems for Database Search Results Disambiguation". *Findings of the Association for Computational Linguistics: ACL 2023 (Findings of ACL) July 2023 Toronto, Canada*.
- Nakyeong Yang, Yunah Jang, Hwanhee Lee, Seohyeong Jeong, and Kyomin Jung. "Task-specific Compression for Multi-task Language Models using Attribution-based Pruning". *Findings of the Association for Computational Linguistics: EACL 2023 (Findings of EACL) May 2023 Dubrovnik, Croatia*.
- Siun Kim, Taegwan Kang, Tae Kyu Chung, Yoona Choi, YeSol Hong, Kyomin Jung, and Howard Lee. "Automatic Extraction of Comprehensive Drug Safety Information from Adverse Drug Event Narratives in the Korea Adverse Event Reporting System Using Natural Language Processing Techniques". *Drug Safety June 2023*.
- Yoonsang Lee\*, Dongryeol Lee\*, and Kyomin Jung. "Enhancing Cross-Domain Generalization through Data Augmentation with Reduced Uncertainty". *EMNLP Workshop on Argument Mining December 2023 Singapore, Singapore*.
- Seongho Joo\*, Kang-il Lee\*, Kyungmin Min\*, Joongbo Shin, Janghoon Han, Seungpil Won, and Kyomin Jung. "Leveraging Ensemble Techniques and Metadata for Subjective Knowledge-grounded Conversational Systems". *SIGDial 2023 Workshop on The Eleventh Dialog System Technology Challenge (DSTC11) September 2023 Prague, Czech Republic*.
- Hyukhun Koh, Haesung Pyun, Nakyeong Yang, and Kyomin Jung. "Multi-View Zero-Shot Open Intent Induction from Dialogues: Multi Domain Batch and Proxy Gradient Transfer". *SIGDial 2023 Workshop on The Eleventh Dialog System Technology Challenge (DSTC11) September 2023 Prague, Czech Republic*.
- Minsung Kim, and Kyomin Jung. "Self-Prompt Generation for Text Classification via Masked Language Modeling Ability". *정보과학회 December 2023*.
- Yongil Kim, Yerin Hwang, Younhyung Chae, and Kyomin Jung. "KLIPScore: A Highly Human-Correlated Korean Image Captioning Metric". *정보과학회 June 2023*.
- Yerin Hwang, Younhyung Chae, Yongil Kim, and Kyomin Jung. "Thinking Fast and Slow in Multimodal Emotion Recognition Task". *정보과학회 June 2023*.
- Hyukhun Koh, Seongho Joo, and Kyomin Jung. "Reflecting dialogue and pretrained information into Multi Modal Emotion Recognition: Focusing on Text and Audio". *정보과학회 June 2023*.
- Yunah Jang, Yoonhyung Lee, Sungdong Kim, Hwaran Lee, and Kyomin Jung. "Enhancing Engagement in Persona-Grounded Dialogue Systems via Fine-grained Response Generation and Ranking". *정보과학회 June 2023*.

**2022**

- Hwanhee Lee, Kang Min Yoo, Joonsuk Park, Hwaran Lee, and Kyomin Jung. "Masked Summarization to Generate Factually Inconsistent Summaries for Improved Factual Consistency Checking". *Findings of the Association for Computational Linguistics: NAACL 2022 (Findings of NAACL) July 2022 Seattle, WA, USA*.
- Hyeongu Yun\*, Yongil Kim\*, and Kyomin Jung. "Modality Alignment between Deep Representations for Effective Video-and-Language Learning". *International Conference on Language Resources and Evaluation (LREC) June 2022 Marseille, France*.
- Yoonhyung Lee, Jinhyeok Yang, and Kyomin Jung. "VarianceFlow: High-quality and Controllable Text-to-Speech Using Variance Information via Normalizing Flow". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) May 2022 Singapore*.
- Nakyeong Yang, Taegwan Kang, and Kyomin Jung. "Deriving Explainable Discriminative Attributes using Confusion about Counterfactual Class". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) Oral May 2022 Singapore*.
- Heeyoung Kwak, Hyunkyung Bae, and Kyomin Jung. "Subgraph Representation Learning With Hard Negative Samples for Inductive Link Prediction". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) May 2022 Singapore*.
- Taegwan Kang, Segwang Kim, Hyeongu Yun, Hwanhee Lee, and Kyomin Jung. "Gated Relational Encoder-Decoder Model for Target-Oriented Opinion Word Extraction". *IEEE Access December 2022*.
- Minbeom Kim, Kyeongha Rho, Yong-duk Kim, and Kyomin Jung. "Action-Driven Contrastive Representation for Reinforcement Learning". *PLOS ONE March 2022*.
- Hwanhee Lee, Cheoneum Park, Seunghyun Yoon, Trung Bui, Franck Dernoncourt, Juae Kim, and Kyomin Jung. "Factual Error Correction for Abstractive Summaries Using Entity Retrieval". *EMNLP Workshop on Generation, Evaluation & Metrics (GEM) December 2022 Abu Dhabi, UAE*.
- Yongil Kim, Yerin Hwang, Seunghyun Yoon, Hyungu Yun, and Kyomin Jung. "Improving Cross-modal Attention via Object Detection". *NeurIPS Workshop on All Things Attention: Bridging Different Perspectives on Attention December 2022 New Orleans, LA, USA*.
- Yunah Jang, Dongryeol Lee, Hyung Joo Park, Taegwan Kang, Hwanhee Lee, Hyunkyung Bae, and Kyomin Jung. "Improving Multiple Documents Grounded Goal-Oriented Dialog Systems via Diverse Knowledge Enhanced Pre-trained Language Model". *ACL Workshop on Document-grounded Dialogue and Conversational Question Answering (DialDoc) May 2022 Dublin, Ireland*.
- Yongil Kim, Hyeongu Yun, Yerin Hwang, and Kyomin Jung. "Improving Cross-modal Attention via Object detection". *정보과학회 June 2022*.

**2021**

- Yongkeun Hwang, Hyeongu Yun, and Kyomin Jung. "Contrastive Learning for Context-aware Neural Machine Translation Using Coreference Information". *Sixth Conference on Machine Translation (WMT) November 2021 Punta Cana, Dominican Republic*.
- Hwanhee Lee, Thomas Scialom, Seunghyun Yoon, Franck Dernoncourt, and Kyomin Jung. "QACE: Asking Questions to Evaluate an Image Caption". *Findings of the Association for Computational Linguistics: EMNLP 2021 (Findings of EMNLP) November 2021 Punta Cana, Dominican Republic*.
- Taegwan Kang, Minwoo Lee, Nakyeong Yang, and Kyomin Jung. "RABERT: Relation-Aware BERT for Target-Oriented Opinion Words Extraction". *30th ACM International Conference on Information and Knowledge Management (CIKM) November 2021 Virtual Conference*.
- Minwoo Lee, Seungpil Won, Juae Kim, Hwanhee Lee, Cheoneum Park, and Kyomin Jung. "CrossAug: A Contrastive Data Augmentation Method for Debiasing Fact Verification Models". *30th ACM International Conference on Information and Knowledge Management (CIKM) November 2021 Virtual Conference*.
- Hwanhee Lee, Seunghyun Yoon, Franck Dernoncourt, Trung Bui, and Kyomin Jung. "UMIC: An Unreferenced Metric for Image Captioning via Contrastive Learning". *The Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (ACL-IJCNLP) August 2021 Virtual Conference*.
- Taegwan Kang, Hwanhee Lee, Byeongjin Choe, and Kyomin Jung. "Entangled Bidirectional Encoder to Autoregressive Decoder for Sequential Recommendation". *International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR) July 2021 Virtual Conference*.
- Hwanhee Lee, Seunghyun Yoon, Franck Dernoncourt, Doo Soon Kim, Trung Bui, Joongbo Shin, and Kyomin Jung. "KPQA: A Metric for Generative Question Answering Using Keyphrase Weights". *Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) June 2021 Virtual Conference*.
- Yoonhyung Lee, Joongbo Shin, and Kyomin Jung. "Bidirectional Variational Inference for Non-Autoregressive Text-to-Speech". *International Conference on Learning Representations (ICLR) April 2021 Virtual Conference*.
- Segwang Kim, Hyoungwook Nam, Joonyoung Kim, and Kyomin Jung. "Neural Sequence-to-grid Module for Learning Symbolic Rules". *AAAI Conference on Artificial Intelligence (AAAI) February 2021 Virtual Conference*.
- Joonyoung Choi, Joonyoung Kim, and Kyomin Jung. "Air Quality Prediction with 1-Dimensional Convolution and Attention on Multi-modal Features". *IEEE International Conference on Big Data and Smart Computing (BigComp) February 2021 Jeju Island, Korea*.
- Heeyoung Kwak, Jooyoung Chang, Byeongjin Choe, Sangmin Park, and Kyomin Jung. "Interpretable Disease Prediction Using Heterogeneous Patient Records with Self-Attentive Fusion Encoder". *Journal of the American Medical Informatics Association July 2021*.
- Yongkeun Hwang, Yanghoon Kim, and Kyomin Jung. "Context-aware Neural Machine Translation for Korean Honorific Expressions". *MDPI Electronics June 2021*.
- Byeongjin Choe, Taegwan Kang, and Kyomin Jung. "Recommendation System with Hierarchical Recurrent Neural Network for Long-term Time Series". *IEEE Access May 2021*.
- Vincent Blondel, Kyomin Jung, Pushmeet Kohli, Devavrat Shah, and Seungpil Won. "Partition-Merge: Distributed Inference and Modularity Optimization". *IEEE Access March 2021*.
- Hyeongu Yun, Yongil Kim, Taegwan Kang, and Kyomin Jung. "Pairwise Context Similarity for Image Retrieval System using Variational Auto-Encoder". *IEEE Access February 2021*.
- Seunghyun Yoon, Kunwoo Park, Minwoo Lee, Taegyun Kim, Meeyoung Cha, and Kyomin Jung. "Learning to Detect Incongruence in News Headline and Body Text via a Graph Neural Network". *IEEE Access February 2021*.
- Hyeongu Yun, Taegwan Kang, and Kyomin Jung. "Analyzing and Controlling Inter-Head Diversity in Multi-Head Attention". *MDPI Applied Sciences February 2021*.
- Segwang Kim, Joonyoung Kim, and Kyomin Jung. "Compositional Generalization via Parsing Tree Annotation". *IEEE Access January 2021*.
- Joonyoung Kim, Hyowoon Seo, Wan Choi, and Kyomin Jung. "Homeostasis-Inspired Continual Learning: Learning to Control Structural Regularization". *IEEE Access January 2021*.
- Donghyeon Lee, Joonyoung Kim, and Kyomin Jung. "Improving Object Detection Quality by Incorporating Global Contexts via Self-Attention". *MDPI Electronics January 2021*.
- Joonyoung Kim, Donghyeon Lee, and Kyomin Jung. "Iterative Learning for K-Approval Votes in Crowdsourcing Systems". *MDPI Electronics January 2021*.
- Jaewoong Lee\*, Heejoon Lee\*, Hwanhee Lee, and Kyomin Jung. "Learning to Select Question-Relevant Relations for Visual Question Answering". *NAACL Workshop on Multimodal Artificial Intelligence (MAI) June 2021 Virtual*.
- Hyunkyung Bae, Minwoo Lee, Ahhyeon Kim, Hwanhee Lee, Cheongjae Lee, Cheoneum Park, Donghyeon Kim, and Kyomin Jung. "Relevance Similarity Scorer and Entity Guided Reranking for Knowledge Grounded Dialog System". *AAAI Workshop on Dialog System Technology Challenge (DSTC) February 2021 Virtual*.
- Sungho Joo, Yoonhyung Lee, and Kyomin Jung. "Emotional Text-to-Speech with Variational Autoencoder using a Multimodal Gaussian Prior". *정보과학회 June 2021*.
- Hyunkyung Bae, Hwanhee Lee, Minwoo Lee, and Kyomin Jung. "Evidence Retrieval toward an explainable model for Document Level Relation Extraction". *정보과학회 June 2021*.
- Yongil Kim, Hyeongu Yun, Seungpil Won, and Kyomin Jung. "모달리티 정렬을 통한 비디오 질의 응답 시스템 개선". *정보과학회 June 2021*.
- Taegwan Kang, Yanghoon Kim, and Kyomin Jung. "표준국어대사전을 활용한 문장쌍 표현 모델 자기지도 학습 방법 연구". *정보과학회 June 2021*.

## 과제

연구실 Research에 게시된 과제 가운데 기간이 2021년 10월 22일–2026년 10월 22일과 겹치는 7건이다. 제목과 지원·협력 기관은 누리집 표기를 따른다.[^research]

- 점차 강화되고 있는 윤리 정책에 발맞춰 유연하게 진화하는 인공지능 기술 개발 연구 (IITP) (기간 2022–2026)
- Learning 기반 한국어 자연어 처리 시스템 및 영-한 기계번역 시스템 개발 (한우물로 홈런치기, 서울대학교 공학연구원) (기간 2016–2026)
- 상황 인지를 위한 빠르고 효율적인 딥러닝 기반의 Language Representation 개발 (삼성DS) (기간 2020–2025)
- 대용량 언어모델의 신뢰성 향상 및 지식 기반 대화모델에의 응용 (네이버) (기간 2021–2024)
- 논리적 추론이 가능한 딥러닝 기반 질의 응답 시스템 개발 (중견연구자지원사업, 한국연구재단) (기간 2021–2024)
- 지식에 근거한 일관적이고 확장성 있는 대화모델 개발 (LG AI Research) (기간 2022–2023)
- IITP 글로벌 핵심인재 양성지원 사업 (Microsoft Research Asia) (기간 2021–2022)

## 수상과 선정

첫 화면의 2021년 12월–2026년 8월 수상·대회 성과 7건과 교수 소개에 적힌 2023년 신양학술상 1건이다. 날짜는 게시 연월 또는 게시 연도이며, 학위논문상의 최우수·우수 구분과 대회 수상·순위를 게시 표기대로 적었다.[^home][^faculty]

- 2026-08 · 연구실 김민범 학생 2026년 8월 협동과정 인공지능전공 박사 졸업 최우수논문상 (Best Ph.D Dissertation Award) 수상.
- 2026-08 · Junsu Park et al., "Instructional Video 기반 멀티모달 절차 계획 생성 방식 비교" KCC 2026 우수발표논문상 수상
- 2026-02 · 연구실 양낙영 학생 2026년 2월 협동과정 인공지능전공 박사 졸업 우수논문상 (Distinguished Ph.D Dissertation Award) 수상.
- 2023-08 · Our paper "Leveraging Ensemble Techniques and Metadata for Subjective Knowledge-grounded Conversational Systems" is awarded as the Best paper in DSTC11 workshop.
- 2023-04 · Seongho Joo, Kangil Lee, Kyungmin Min ranked first in the response accuracy category in DSTC11 challenge.
- 2022-08 · 연구실 이환희 학생 박사 졸업 우수논문상 (Distinguished Ph.D Dissertation Award) 수상.
- 2021-12 · Prof. Jung receives the 2021 IEEE ICDM 10-Year Highest-Impact Paper Award for the paper "IRIE: Scalable and Robust Influence Maximization in Social Networks".
- 2023 · 정교민 교수, 서울대학교 공과대학 신양학술상(2023 Sinyang Academic Award for Engineering) 수상

## 소식

첫 화면에서 2021년 10월 22일–2026년 10월 22일 범위에 드는 날짜가 붙은 연구 성과 소식 27건이다. 게시 연월과 논문 채택 안내를 따른다.[^home]

- 2026-09 · Our 1 paper is accepted to NeurIPS 2026.; Minbeom Kim et al., "LiSA: Lifelong Safety Adaptation via Conservative Policy Induction" is accepted to NeurIPS 2026.
- 2026-08 · Our 9 papers are accepted to EMNLP 2026.; Hyukhun Koh et al., "When i.i.d. Factorization Breaks Language: The Structural Failure of Discrete Diffusion Language Models" is accepted to EMNLP 2026.; Jiwon Moon et al., "Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs" is accepted to EMNLP 2026.; Yunah Jang et al., "How You Ask Matters! Adaptive RAG Robustness to Query Variations" is accepted to EMNLP 2026.; Yerin Hwang et al., "How Instruction Hierarchy Breaks Under Pairwise Multi-Conflict Pressure" is accepted to EMNLP 2026.; Sangmook Lee et al., "Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning" is accepted to EMNLP 2026.; Hyojeong Yu et al., "PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations" is accepted to EMNLP 2026.; Yunah Jang et al., "CompCQR: Compositional Query Generation for Training-Free Conversational Search" is accepted to Findings of EMNLP 2026.; Kyeongman Park et al., "A Benchmark for the Generation and Evaluation of Scientific Architecture Diagrams in HTML/SVG" is accepted to Findings of EMNLP 2026.; Junseok Kim et al., "Personalized Privacy Control in LLMs via Attention Head Intervention" is accepted to Findings of EMNLP 2026.
- 2026-06 · Our paper "ReflectCAP: Detailed Image Captioning with Reflective Memory" is accepted to ECCV 2026.
- 2026-05 · Our 3 papers are accepted to ICML 2026.; Our paper "CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution" is accepted to ICML 2026.; Our paper "Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR" is accepted to ICML 2026.; Our paper "PEARL: Differentially Private and Entropy-Aware Regulated Language Generation" is accepted to ICML 2026.
- 2026-04 · Our 5 papers are accepted to ACL 2026.; Our paper "How Training Data Shapes the Use of Parametric and In-Context Knowledge in Language Models" is accepted to ACL 2026.; Our paper "Evaluating Visual Narrative Coherence in Story Visualization via Diversified Storylines" is accepted to ACL 2026 as an Oral presentation.; Our paper "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning" is accepted to ACL 2026 Findings.; Our paper "Rethinking Post-Unlearning Behavior of Large Vision-Language Models" is accepted to ACL 2026 Findings.; Our paper "A Universal Avoidance Method for Diverse Multi-branch Generation" is accepted to ACL 2026 Findings.
- 2026-01 · Our paper "Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning" is accepted to ICLR 2026.
- 2026-01 · Our 2 papers are accepted to EACL 2026.; Our paper "Don't Judge Code by Its Cover: Exploring Biases in LLM Judges for Code Evaluation" is accepted to EACL 2026 Findings.; Our paper "Persona Switch: Mixing Distinct Perspectives in Decoding Time" is accepted to EACL 2026 Findings.
- 2026-01 · Our paper "Confidence-Guided Stepwise Model Routing for Cost-Efficient Reasoning" is accepted to AAAI 2026.
- 2025-09 · Our paper "Program Synthesis via Test-Time Transduction" is accepted to NeurIPS 2025.
- 2025-08 · Our 9 papers are accepted to EMNLP 2025.; Our paper "Conditional [MASK] Discrete Diffusion Language Model" is accepted to EMNLP 2025.; Our paper "Avoidance Decoding for Diverse Multi-Branch Story Generation" is accepted to EMNLP 2025.; Our paper "Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation" is accepted to EMNLP 2025.; Our paper "FaithUn: Toward Faithful Forgetting in Language Models by Investigating the Interconnectedness of Knowledge" is accepted to EMNLP 2025.; Our paper "Harmful Prompt Laundering: Jailbreaking LLMs with Abductive Styles and Symbolic Encoding" is accepted to EMNLP 2025.; Our paper "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection" is accepted to EMNLP 2025.; Our paper "Public Data Assisted Differentially Private In-Context Learning" is accepted to EMNLP 2025 Findings.; Our paper "Can You Trick the Grader? Adversarial Persuasion of LLM Judges" is accepted to EMNLP 2025 Findings.; Our paper "Drift: Decoding-time Personalized Alignments with Implicit User Preferences" is accepted to EMNLP 2025 Findings.
- 2025-08 · Our paper "Unplug and Play Language Models: Decomposing Experts in Language Models at Inference Time" is accepted to CIKM 2025.
- 2025-06 · Our 2 papers are accepted to ACL 2025.; Our paper "LLMs can be easily Confused by Instructional Distractions" is accepted to ACL 2025.; Our paper "A Character-Centric Creative Story Generation via Imagination" is accepted to ACL 2025.
- 2025-01 · Our paper "Guaranteed Generation from Large Language Models" is accepted to ICLR 2025.
- 2025-01 · Our 6 papers are accepted to NAACL 2025.; Our paper "Are LLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers on LLM-based Evaluation" is accepted to NAACL 2025 as an Oral presentation.; Our paper "Generating Diverse Hypotheses for Inductive Reasoning" is accepted to NAACL 2025 as an Oral presentation.; Our paper "AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence" is accepted to NAACL 2025.; Our paper "SWITCH: Studying with Teacher for Knowledge Distillation of Large Language Models" is accepted to NAACL 2025 Findings.; Our paper "VLind-Bench: Measuring Language Priors in Large Vision-Language Models" is accepted to NAACL 2025 Findings.; Our paper "Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding" is accepted to NAACL 2025 Findings.
- 2024-12 · Our paper "Return of EM: Entity-driven Answer Set Expansion for QA Evaluation" is accepted to COLING 2025 as an Oral presentation.
- 2024-09 · Our 2 papers are accepted to EMNLP 2024.; Our paper "MP2D: An Automated Topic Shift Dialogue Generation Framework Leveraging Knowledge Graphs" is accepted to EMNLP 2024.; Our paper "Can LLMs Recognize Toxicity? A Structured Investigation Framework and Toxicity Metric" is accepted to EMNLP 2024 Findings.
- 2024-08 · Our paper "MVMR: A New Framework for Evaluating Faithfulness of Video Moment Retrieval against Multiple Distractors" is accepted to CIKM 2024.
- 2024-08 · Our paper "Mitigating Biases for Instruction-following Language Models via Bias Neurons Elimination" is accepted to ACL 2024.
- 2024-06 · Our 3 papers are accepted to NAACL 2024.; Our paper "LifeTox: Unveiling Implicit Toxicity in Life Advice" is accepted to NAACL 2024 as an Oral presentation.; Our paper "Fine-grained Gender Control in Machine Translation with Large Language Models" is accepted to NAACL 2024.; Our paper "IterCQR: Iterative Conversational Query Reformulation with Retrieval Guidance" is accepted to NAACL 2024.
- 2023-12 · Our paper "LongStory: Coherent, Complete and Length Controlled Long story Generation" from our new member is accepted to PAKDD 2024 as an Oral presentation.
- 2023-12 · Our paper "Boosting Speech Enhancement with Clean Self-Supervised Features via Conditional Variational Autoencoders" is accepted to ICASSP 2024.
- 2023-12 · Our 6 papers are accepted to EMNLP 2023.; Our paper "DPP-TTS: Diversifying prosodic features of speech via determinantal point processes" is accepted to EMNLP 2023.; Our paper "Weakly Supervised Semantic Parsing with Execution-based Spurious Program Filtering" is accepted to EMNLP 2023.; Our paper "Target-Agnostic Gender-Aware Contrastive Learning for Mitigating Bias in Multilingual Machine Translation" is accepted to EMNLP 2023.; Our paper "Dialogizer: Context-aware Conversational-QA Dataset Generation from Textual SourcesA" is accepted to EMNLP 2023.; Our paper "Asking Clarification Questions to Handle Ambiguity in Open-Domain QA" is accepted to EMNLP 2023 Findings.; Our paper "PR-MCS: Perturbation Robust Metric for MultiLingual Image Captioning" is accepted to EMNLP 2023 Findings.
- 2023-05 · Our 3 papers are accepted to ACL 2023.; Our paper "BREAK: Breaking the Dialogue State Tracking Barrier with Beam Search and Re-ranking" is accepted to ACL 2023.; Our paper "Critic-Guided Decoding for Controlled Text Generation" is accepted to ACL 2023 Findings.; Our paper "Injecting Comparison Skills in Task-Oriented Dialogue Systems for Database Search Results Disambiguation" is accepted to ACL 2023 Findings.
- 2023-01 · Our paper "Task-specific Compression for Multi-task Language Models using Attribution-based Pruning" is accepted to EACL 2023 Findings.
- 2022-04 · Our paper "Masked Summarization to Generate Factually Inconsistent Summaries for Improved Factual Consistency Checking" is accepted to NAACL 2022 Findings.
- 2022-04 · Our paper "Modality Alignment between Deep Representations for Effective Video-and-Language Learning" is accepted to LREC 2022.
- 2022-01 · Three papers "VarianceFlow: High-quality and Controllable Text-to-Speech Using Variance Information via Normalizing Flow", "Deriving Explainable Discriminative Attributes using Confusion about Counterfactual Class" and "Subgraph Representation Learning With Hard Negative Samples for Inductive Link Prediction" are accepted to ICASSP 2022.

## 연락과 위치

- 교수 이메일: kjung@snu.ac.kr[^contact]
- 교수 연구실: 서울대학교 301동 1005호[^contact][^eceprof]
- 학생 연구실: 서울대학교 303동 561-2호, 133동 314호[^contact]
- 주소: 서울특별시 관악구 관악로 1 서울대학교 공과대학 전기·정보공학부, 08826[^contact]
- 교수실 전화: 02-880-1937[^eceprof]
[^home]: 머신 인텔리전스 연구실 첫 화면, 연구 소개와 Latest News. <https://milab.snu.ac.kr/> (2026-10-26 열람).
[^research]: 연구실 Research, Research Areas와 Selected Projects. <https://milab.snu.ac.kr/research> (2026-10-26 열람).
[^pubs]: 연구실 Publications, International Conference Proceedings·Journal Publications·Workshops·Domestic Conference Proceedings. <https://milab.snu.ac.kr/publications> (2026-10-26 열람).
[^members]: 연구실 Members, Current Students와 Alumni. <https://milab.snu.ac.kr/members> (2026-10-26 열람).
[^faculty]: 정교민 교수 개인 소개, 경력·연구 분야·수상·Academic Activities. <https://milab.snu.ac.kr/kjung/index.html> (2026-10-26 열람).
[^eceprof]: 서울대학교 전기·정보공학부 정교민 교수 소개, 직위·학력·주요경력·연구 분야·교수실. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p805> (2026-10-26 열람).
[^gsai]: 서울대학교 대학원 협동과정 인공지능전공 첫 화면과 교수진 목록의 정교민 교수 항목. <https://gsai.snu.ac.kr/> <https://gsai.snu.ac.kr/%ea%b5%90%ec%88%98%ec%a7%84-%eb%aa%a9%eb%a1%9d/> (2026-10-26 열람).
[^contact]: 연구실 Contact, 교수실·학생 연구실·교수 이메일. <https://milab.snu.ac.kr/contact> (2026-10-26 열람).
[^p1]: M. Kim 외, T. Pfister, International Conference on Machine Learning (ICML) 2026, arXiv 판 (온라인 2026-02-08). <https://arxiv.org/abs/2602.07918> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.07918>. 최초 공개일과 수정일은 arXiv 날짜다. (2026-10-26 열람).
[^p2]: M. Kim 외, K. Jung, Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers), 688–698 (2024). <https://doi.org/10.18653/v1/2024.naacl-short.60> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.naacl-short.60/>. (2026-10-26 열람).
[^p3]: M. Kim 외, M. Cha, arXiv, 2026-04-20 수정판(v3) (온라인 2025-09-29). <https://arxiv.org/abs/2510.02370> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.02370>. 최초 공개일과 수정일은 arXiv 날짜다. 읽은 판은 2026-04-20 수정판(v3)이며, 학회 표기는 연구실 목록을 따른다. (2026-10-26 열람).
[^p4]: Y. Jang 외, K. Jung, Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 8121–8138 (2024). <https://doi.org/10.18653/v1/2024.naacl-long.449> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.naacl-long.449/>. (2026-10-26 열람).
[^p5]: K.-i. Lee 외, K. Jung, Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 8461–8474 (2025). <https://doi.org/10.18653/v1/2025.naacl-long.429> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.naacl-long.429/>. (2026-10-26 열람).
[^p6]: K.-i. Lee, S. Kim, K. Jung, Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 6884–6894 (2023). <https://doi.org/10.18653/v1/2023.emnlp-main.425> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2023.emnlp-main.425/>. (2026-10-26 열람).
[^p7]: N. Yang 외, K. Jung, CIKM 2024, arXiv 판 (온라인 2023-08-15). <https://doi.org/10.1145/3627673.3679838> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2309.16701>. 최초 공개일과 수정일은 arXiv 날짜다. arXiv가 CIKM 2024 채택과 관련 DOI를 명시한다. (2026-10-26 열람).
[^p8]: S. Joo, H. Koh, K. Jung, Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 4402–4417 (2023). <https://doi.org/10.18653/v1/2023.emnlp-main.267> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2023.emnlp-main.267/>. (2026-10-26 열람).

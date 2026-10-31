# Data Intelligence System Lab (DISLab)

**KAIST 산업및시스템공학과·데이터사이언스대학원·AX학과 · 송환준 조교수**

- 분야: 데이터 중심 인공지능, 에이전트의 인식·추론·기억, 언어 모델의 요약·검색·평가, 개인화 추천
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^p1][^p2], 생성 인공지능[^p2][^p6], 멀티모달 AI[^home][^p6], 데이터 중심 AI·데이터 효율 학습[^home][^p2], 다중 에이전트 시스템·분산 의사결정[^p7], 추천 시스템[^p5], 모델 경량화·양자화[^home]
- 홈페이지: <https://disl-lab.github.io>
- 근거와 출처: [Data Intelligence System Lab 근거 페이지](disl-sources.md)

> 자료의 품질과 활용 방식을 바탕으로, 긴 문맥과 불완전한 정보 속에서도 신뢰할 수 있게 판단하고 행동하는 인공지능 에이전트를 연구한다.[^home]

## 무엇을 연구하나

DISLab은 송환준 조교수가 이끄는 연구실로, 데이터 중심 인공지능(자료의 품질·구조·활용을 중심에 두는 인공지능)을 바탕으로 신뢰할 수 있는 에이전트(목표에 따라 정보를 받아 판단하고 행동하는 소프트웨어)를 만드는 데 초점을 둔다. 연구실은 모델(자료에서 관계를 배워 결과를 내는 계산 체계)의 규모뿐 아니라 자료를 어떻게 인식하고 구조화하며 기억하고 쓰는지가 지능을 좌우한다고 설명한다. 잡음(자료에 섞인 불필요한 성분·변동)이 있는 입력, 긴 문맥, 불완전한 정보에서도 안정적으로 작동하는 에이전트가 목표다.[^home][^members]

한 축은 글을 만들고 평가하는 방법이다. 대형 언어 모델(Large Language Model, LLM; 많은 글을 학습해 언어를 이해하고 생성하는 모델)이 만든 요약에는 원문에 없는 내용, 핵심 정보의 누락, 불필요한 장황함이 생길 수 있다. 연구실은 충실성(원문과 내용이 맞는 정도), 완전성(핵심 정보가 담긴 정도), 간결성을 함께 평가하고, 이 평가를 요약 생성 모델의 학습에 활용한다. 평가 자료의 문맥·길이와 평가 관점을 넓히는 벤치마크(성능 비교에 쓰는 공통 자료와 평가 체계)도 만든다.[^p2][^p4]

다른 축은 에이전트가 어떤 정보를 받아들이고 기억하는가다. 연구실은 멀티모달 AI(글·이미지·영상처럼 종류가 다른 자료를 함께 다루는 인공지능)와 긴 문맥의 인식을 연구한다. 또 지식을 정리하고 저장하고 다시 찾는 기억 및 정보 압축(내용의 표현을 줄이는 처리)을 설계해, 에이전트가 긴 시간에 걸쳐 일관되게 행동하도록 하는 것을 목표로 한다.[^home]

신뢰성은 답변을 만든 뒤의 평가뿐 아니라 학습 자료와 모델 설계의 문제이기도 하다. 연구실은 추론(주어진 정보에서 결론을 도출하는 과정)과 의사결정을 가치 정렬(인간의 가치·기준에 맞추는 조정)과 연결하고, 지식 증류(모델의 출력·내부 표현으로 다른 모델을 학습시키는 방법), 모델 압축(모델의 표현·구조·계산 경로를 바꾸어 저장·계산 부담을 줄이는 방법), 안전 위반을 막는 조건과 자동 평가를 통해 효율적이고 제어 가능한 에이전트를 만드는 방향을 제시한다. 과제에서는 언어 모델 평가, 과학기술 문헌의 검색·요약, 제조 현장의 인공지능 시스템으로 이 연구를 넓히고 있다.[^home][^projects]

## 주요 연구 주제

### 인식: 여러 종류의 자료와 긴 문맥 이해

Agent Perception은 글·이미지·영상과 감각 입력에서 환경을 이해하는 연구다. 이미지 설명 생성 연구에서는 문맥 전체뿐 아니라 사용자가 강조한 부분을 반영하도록 생성 과정을 조절한다. 프롬프트(모델에 원하는 작업을 전달하는 입력)로 생성 방향을 지정하는 방식과, 강조한 부분의 내부 표현을 조정하는 방식을 제안하고 설명문의 품질을 평가했다.[^home][^p6]

### 지능: 피드백을 숙고하고 판단하기

Agent Intelligence는 환경 이해와 가치 정렬을 결합해 목적에 맞고 안전한 판단을 하는 능력을 다룬다. ReFeed는 요약에 대한 여러 관점의 피드백(결과에 대한 평가 정보)을 숙고하며 요약을 수정하는 체계다. 요약 평가 연구에서는 여러 에이전트에 서로 다른 초기 입장을 주고 토론하게 해 내용의 오류와 모호함을 찾는 방법도 제안했다.[^home][^p3][^p7]

### 기억: 필요한 근거와 사용자 정보 유지

Agent Memory는 지식을 정리·저장·검색하고 압축해 지속적인 행동에 활용하는 연구다. 검색 증강 생성(Retrieval-Augmented Generation, RAG; 외부에서 찾은 자료를 활용하는 생성)에서는 검색 결과에 잡음이 섞일 수 있다는 점을 다룬다. Ext2Gen은 질문과 관련 있는 근거의 선택과 답변 생성을 함께 학습한다. 개인화 추천 연구의 PURE는 사용자 리뷰에서 정보를 추출하고 요약해 프로필(사용자의 특성을 정리한 정보)을 갱신하며 추천에 사용한다.[^home][^p1][^p5]

### 모델링: 효율적인 모델과 자동 평가

Agent Modeling은 지식 증류, 압축, 안전 제약과 자동 평가를 통해 효율적이고 조절 가능한 모델을 만드는 연구다. 요약 학습 연구는 언어 모델이 만든 피드백의 품질·평가 관점·세밀함이 학습 결과에 미치는 영향을 살피고, 그 피드백으로 요약 모델을 학습한다. UniSumEval은 입력 문맥과 평가 관점을 넓히고 세부적인 평가 정보를 제공해, 요약 모델과 자동 평가기를 비교하는 자료를 제시한다.[^home][^p2][^p4]

## 대표 논문

근거 검색과 개인화 기억, 요약의 개선과 평가, 이미지·언어 결합 연구를 보여 주는 7편이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. arXiv로 표시한 항목의 설명은 사전 공개본 초록 기준이며, 교신저자 표시는 연구실 목록이 정의한 별표를 따른다.[^pubs]

| 번호 | 연도·판본 | 논문 | 쉽게 말하면 | 송환준의 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Aligning Extraction and Generation for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2503.04789) · WSDM 채택, arXiv 판 | 검색 결과에 잡음이 있거나 관련 내용의 위치가 일정하지 않으면 답변에 오류가 생길 수 있다. Ext2Gen은 관련 근거를 골라내는 일과 답변을 만드는 일을 결합한다. 선별한 답변 쌍의 피드백으로 학습하며, 잡음이 있는 검색 결과에서도 정확하고 근거에 충실한 답변을 생성하도록 한다.[^p1] | 1저자·교신저자 |
| 2 | 2025 | [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38/) · NAACL | 여러 분야의 다양한 품질의 요약에 언어 모델이 평가를 붙인 FeedSum 자료를 만든다. 평가의 품질, 관점의 수, 세밀함이 요약 학습에 미치는 영향을 살피고, 원문 충실성·완전성·간결성을 반영하는 요약 모델을 학습한다. 지도 미세 조정(주어진 정답 예시로 모델을 조정하는 학습)과 직접 선호 최적화(선호하는 답변 쌍으로 모델을 조정하는 학습)를 비교한다.[^p2] | 1저자·교신저자 |
| 3 | 2025 | [ReFeed: Multi-dimensional Summarization Refinement with Reflective Reasoning on Feedback](https://arxiv.org/abs/2503.21332) · arXiv 판 | 여러 관점의 피드백을 함께 숙고하며 요약을 수정하는 ReFeed를 제안한다. 이런 추론을 학습할 자료 SumFeed-CoT도 제시한다. 평가 관점의 수, 피드백 노출, 추론 방식이 결과에 미치는 영향을 살피고, 여러 피드백을 함께 다루는 숙고가 평가 관점 사이의 상충을 완화하는 데 중요함을 보인다.[^p3] | 마지막 저자·교신저자 |
| 4 | 2024 | [UniSumEval: Towards Unified, Fine-Grained, Multi-Dimensional Summarization Evaluation for LLMs](https://arxiv.org/abs/2409.19898) · arXiv 판, EMNLP Findings 채택 | 요약 평가 자료의 입력 분야와 길이를 넓히고, 여러 관점의 세부 평가를 담은 UniSumEval을 만든다. 자료 제작과 사람의 평가 작업에 인공지능의 도움을 활용한다. 이 자료로 요약 모델과 자동 평가기를 비교해, 입력 문맥과 평가 관점에 따라 성능을 살핀다.[^p4] | 마지막 저자·교신저자 |
| 5 | 2025 | [LLM-based User Profile Management for Recommender System](https://arxiv.org/abs/2502.14541) · arXiv 판, SIGIR Workshop 채택 | 구매 이력뿐 아니라 사용자 리뷰에서 선호와 상품의 특징을 추출해 추천에 반영하는 PURE를 제안한다. 정보를 요약해 사용자 프로필을 계속 갱신하고, 그 프로필로 개인화 추천을 수행한다. 리뷰가 시간에 따라 추가되는 순차 추천 과제로 이 과정을 평가한다.[^p5] | 마지막 저자·교신저자 |
| 6 | 2024 | [Controllable Contextualized Image Captioning: Directing the Visual Narrative through User-Defined Highlights](https://arxiv.org/abs/2407.11449) · arXiv 판, ECCV 2024 기재 | 문맥 정보와 사용자가 강조한 부분에 맞춰 이미지 설명을 생성하는 문제를 제시한다. 강조한 내용을 반영한 입력으로 생성을 유도하는 방식과, 강조 부분의 내부 표현을 조정하는 방식을 개발한다. 생성된 설명을 평가하는 방법도 함께 제시한다.[^p6] | 공저자 |
| 7 | 2025 | [Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation](https://arxiv.org/abs/2502.08514) · arXiv 판 | 요약을 평가하는 여러 언어 모델 에이전트에 서로 다른 초기 입장을 주고, 그 입장을 뒷받침하는 이유를 제시하며 토론하게 한다. 합의에 이르는 과정을 통해 오류를 찾고, 원문에 충실한지 아닌지만으로 나누기 어려운 모호한 사례를 별도 평가 대상으로 제시한다.[^p7] | 공저자 |

## 교수와 전문 분야

송환준(Hwanjun Song)은 DISLab의 연구책임자이며, 구성원 페이지는 직위를 Ewon Assistant Professor로 적는다. 연구실 소식은 해당 직함의 임기를 2026년 3월–2029년 2월로 밝힌다.[^members][^news] KAIST Data Mining Lab의 2023년 11월 13일 임용 소식은 송환준이 KAIST 산업및시스템공학과에 정년보장 심사 대상 조교수로 합류했다고 전한다.[^appointment]

최근 논문에서 드러나는 전문 분야는 언어 모델의 요약 평가와 피드백 학습, 검색 근거와 생성의 결합, 사용자 정보의 지속적인 갱신, 문맥에 맞춘 이미지 설명 생성이다. 요약의 품질을 평가하는 자료를 설계하는 데서 그치지 않고, 평가 정보를 이용해 모델의 출력을 학습·수정하는 방법까지 연결한다.[^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

과학기술 문헌을 이해하고 정리하는 연구 보조가 주요 응용이다. 과제에는 과학 문헌의 자동 이해·종합을 위한 Survey 에이전트, 문헌 이해부터 가설 생성과 실험 설계까지 연구 과정을 돕는 AI Meta-Scientist, 여러 문서의 분석과 생성을 위한 RAG가 있다. 문헌 인용망을 활용한 검색, 문맥 확장과 요약, 일관성과 사실성 점검을 개발 목표로 삼는다.[^projects]

산업 응용에는 개인화 비디오 에이전트, 개인화 지속 에이전트, 소매업 특화 RAG, 도로 설계 문서의 이미지·표·글을 이해하는 시스템이 있다. 제조 분야에서는 공장 설계·생산·물류·안전 운영을 결합하는 다크팩토리 솔루션 개발에 참여하며, 인공지능 일정 계획, 디지털 트윈(관측 자료와 연결되는 현실 시스템의 디지털 모형), 로봇 통합 제어와 안전 감시를 목표로 한다. 갈등 중재를 위한 공정하고 투명한 다중양식 에이전트 플랫폼과, 게임 환경에서 적응하고 일반화하는 에이전트도 과제에 포함된다.[^projects]

연구실은 요약 모델 SummLlama, RAG 생성 모델 Ext2Gen, 요약 평가 자료 UniSumEval·ToFuEval, 잡음이 있는 정답 표기 자료 ANIMAL-10N, 검색·인식·강건 학습·지속 학습 관련 코드와 자료를 공개한다.[^opensource]

## 구성원

2026년 10월 31일 구성원 페이지에 게시된 박사후연구원 1명, 박사과정 구획 6명, 석사과정 8명, 공동 지도 학생 3명, 연구 인턴 6명이다. 박사과정 구획의 Jeonghwan Choi는 카드의 석박사통합과정 표기를 따른다. 공동 지도 학생의 학위 과정은 별도로 표시되지 않는다. 「대표 논문 참여」는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 경우 표시했다.[^members]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Jeesu Jung | 박사후연구원 (Lab Manager) | March 2026~ |  |
| Hyangsuk Min | 박사과정 (Full Time) | Fall 2024~ | 3 |
| Jeonghwan Choi | 석박사통합과정 (Full Time) | Spring 2025~ | 1 |
| Yuho Lee | 박사과정 (Full Time) | Fall 2025~ | 2, 3, 4 |
| Taewon Yun | 박사과정 (Full Time) | Fall 2025~ | 2, 3, 4 |
| Jihwan Oh | 박사과정 (Full Time) | Spring 2026~ | 2, 3 |
| Jisu Shin | 박사과정 (Full Time) | Spring 2026~ |  |
| Jiaqi Deng | 석사과정 (Full Time) | Fall 2024~ |  |
| Minjeong Ban | 석사과정 (Full Time) | Spring 2025~ |  |
| Kibum Kim | 석사과정 (Hankook Tire) | Spring 2025~ |  |
| Mingyu Choi | 석사과정 (Full Time) | Spring 2026~ |  |
| Gyeonghun Sun | 석사과정 (Full Time) | Spring 2026~ |  |
| Seunghwan Bang | 석사과정 (Full Time) | September 2026~ | 5 |
| Jibin Hwang | 석사과정 (Full Time) | September 2026~ |  |
| Yeeun Choi | 석사과정 (Full Time) | September 2026~ |  |
| Jihwan Bang | 공동 지도 학생 (Co-advised by Prof. Jae-Gil Lee; Qualcomm) | Fall 2023~ | 3 |
| Donghee Han | 공동 지도 학생 (Co-advised by Prof. Mun Yong Yi) | Fall 2023~ |  |
| Yujin Kim | 공동 지도 학생 (Full Time; Co-advised by Se-Young Yun) | Spring 2025~ |  |
| Hwan Chang | 인턴 (MS Intern) | July 2026~ |  |
| Hyeonseong Park | 학부 인턴 | January 2026~ |  |
| Juseon Do | 학부 인턴 | March 2026~ |  |
| Hayoon Park | 학부 인턴 | March 2026~ |  |
| Byeongjun Joung | 학부 인턴 | July 2026~ |  |
| Chanjoong Kim | 학부 인턴 | July 2026~ |  |

구성원 페이지는 다음 산업계 인턴십 이력도 적는다.[^members]

| 구성원 | 시기 | 기관·팀 |
|---|---|---|
| Yuho Lee | Summer 2025 | Amazon Web Services, Bedrock |
| Yujin Kim | Summer 2026 | NVIDIA Corp. |
| Taewon Yun | Summer 2026 | Amazon Web Services, Agentic AI |

## 졸업생과 진로

구성원 페이지의 Graduates 구획에 게시된 5행이다. 시기는 랩의 학기 표기이며, 학위 종류를 따로 적지는 않는다. Jeonghwan Choi, Yuho Lee, Taewon Yun, Jihwan Oh는 현재 구성원 구획에도 올라 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jeonghwan Choi | (Spring 2025) | PhD Program at KAIST |
| Yuho Lee | (Fall 2025) | PhD Program at KAIST |
| Taewon Yun | (Fall 2025) | PhD Program at KAIST |
| Jihwan Oh | (Fall 2025) | PhD Program at KAIST |
| Heeyoen Kim | (Fall 2025) |  |

## 최근 논문 목록 (2021–2026)

언어 모델의 요약·검색·추천, 영상 이해, 자료 품질과 지속 학습 등을 다룬 논문·발표·사전 공개본 83항목이다. 송환준의 2023년 11월 KAIST 합류 전 연구도 포함한다. 연도는 연구실 목록의 연도 구역이고, 제목·저자·발표처는 랩 표기를 따른다. 사전 공개본 4편은 발표처에 「사전 공개본」을 붙였다. 연구실 소식에서 채택을 알린 학회 항목은 「채택」으로 표시했으며, NAACL의 Learning to Summarize from LLM-generated Feedback은 논문집 서지를 따른다. 별표는 교신저자, 중괄호는 공동 1저자를 뜻한다.[^pubs][^news][^appointment][^p2]

**2026**

- Sungrae Park, Sanghoon Kim, Gyoungjin Gim, et al. , Minjeong Ban, Taewon Yun, Hwanjun Song, Jae-Gil Lee, KyungTae Lim, and Alice Oh (53 authors). "Solar Open 2 Technical Report". *arXiv preprint arXiv:2607.20062, 2026 (사전 공개본)*.
- Yuho Lee, Jisu Shin, Hee-Yeon Kim, Jihwan Bang, Juntae Lee, Kyuwoong Hwang, Fatih Porikli, and Hwanjun Song\*. "Rethinking RAG in Long Videos: What to Retrieve and How to Use It?". *arXiv preprint arXiv:2606.13141, 2026 (사전 공개본)*.
- Taewon Yun, Hyeonseong Park, Jeonghwan Choi, Hayoon Park, Yeeun Choi, and Hwanjun Song\*. "SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations". *arXiv preprint arXiv:2606.05563, 2026 (사전 공개본)*.
- Seunghwan Bang, and Hwanjun Song\*. "Reasoning over Video: Evaluating How MLLMs Extract, Integrate, and Reconstruct Spatiotemporal Evidence". *arXiv preprint arXiv:2603.13091, 2026 (사전 공개본)*.
- Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun\*, and Hwanjun Song\*. "LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL". *In Advances in Neural Information Processing Systems, 2026 (채택)*.
- Donghee Han, Jiwon Jeong, Hwanjun Song\*, and Mun Yong Yi\*. "PRISMIC: Reconstructing User Preference via Intent Decomposition and Consolidation". *In Advances in Neural Information Processing Systems, 2026 (채택)*.
- Jihwan Bang, Sumyeong Ahn, Hwanjun Song, and Jae-Gil Lee\*. "Training-Free Active Test-Time Adaptation for Vision-Language Models". *In Advances in Neural Information Processing Systems, 2026 (채택)*.
- {Jihwan Oh, Gyeonghun Sun}, Jisoo Kim, Yuho Lee, Taewon Yun, Jisu Shin, and Hwanjun Song\*. "Show Me How You Cite: Citation Fidelity, Usage, and Topology in the Evidence Behavior of AI Scientific Writing". *In International Conference on Empirical Methods in Natural Language Processing (Main), 2026 (채택)*.
- Donghee Han, Jiwon Jeong, Hwanjun Song\*, and Mun Yong Yi\*. "Illuminating the Path: Reachability-Aware Supervision Curation for LLM-Based Recommendation". *In International Conference on Empirical Methods in Natural Language Processing (Main), 2026 (채택)*.
- Juseon Do, Sangmin Bae, Jeesu Jung\*, and Hwanjun Song\*. "TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens". *In International Conference on Empirical Methods in Natural Language Processing (Main), 2026 (채택)*.
- Hyangsuk Min and Hwanjun Song\*. "Don’t Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2026 (채택)*.
- Minkyu Che, Jihwan Oh, Jeonghwan Choi, Jeesu Jung\*, and Hwanjun Song\*. "Towards Robust Retrieval-Augmented Generation via Reliability-Aware Adaptive Evidence Selection". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2026 (채택)*.
- Youngeun Nam, Joeun Kim, Hwanjun Song, Susik Yoon, Jae-Gil Lee\*, and Byung Suk Lee. "TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2026 (채택)*.
- Donghee Han, Jiwon Jeong, Hwanjun Song\*, and Mun Yong Yi\*. "TAG-Rec: Grounding LLM-based Recommendation via Trigger-Anchored GRPO". *In International Conference on Information and Knowledge Management, 2026*.
- Donghee Han, Jiwon Jeong, Hwanjun Song\*, and Mun Yong Yi\*. "No Logs, Only Catalogs: Catalog-to-Supervision Training for Recommendation with LLM-Simulated Preferences". *In International Conference on Information and Knowledge Management, 2026*.
- Jeonghwan Choi, Jibin Hwang, Gyeonghun Sun, Minjeong Ban, Taewon Yun, Hyeonjae Cheon, and Hwanjun Song\*. "What Makes a Sale? Rethinking End-to-End Seller–Buyer Retail Dynamics with LLM Agents". *In Conference on Language Modeling, 2026 (채택)*.
- Jihwan Oh, Taewon Yun, Minkyu Che, Sundong Kim, and Hwanjun Song\*. "Quality of Rejections Matters: Preference Data Construction for Faithful Summarization". *In Conference on Language Modeling, 2026 (채택)*.
- Gyeonghun Sun, Jeonghwan Choi, Sundong Kim, and Hwanjun Song\*. "RAQE: Reranker-Aligned Query Expansion via Label-Free Group-Relative Policy Optimization". *In Conference on Language Modeling, 2026 (채택)*.
- Jeonghwan Choi, Taewon Yun, Minjeong Ban, Jae-Gil Lee, and Hwanjun Song\*. "Towards Query-Agnostic RAG Evaluation via Query Coverage and Claim Verifiability". *In Conference on Language Modeling, 2026 (채택)*.
- Youngjun Lee, Doyoung Kim, Junhyeok Kang, Hwanjun Song, and Jae-Gil Lee\*. "CURE: Cumulative Knowledge Reuse for Efficient Device-Server Hybrid Inference in Vision-Language Models". *In International Conference on European Conference on Computer Vision, 2026 (채택)*.
- Doyoung Kim, Youngjun Lee, Joeun Kim, Jihwan Bang, Hwanjun Song, Susik Yoon, and Jae-Gil Lee\*. "Breaking the Reference Bottleneck via Learning to Rewrite Conversational Queries without Gold Reference Passages". *In International Conference on Machine Learning, 2026 (채택)*.
- Soyoung Park, Hwanjun Song, and Sungsu Lim\*. "Quantile-Free Uncertainty Quantification in Graph Neural Networks". *In International Conference on Machine Learning, 2026 (채택)*.
- Hwanjun Song\* (Sole-authored!). "Alignment Tuning for Large Language Models: A Data-Centric Lens on Alignment Data Pipelines". *In Annual Meeting of the Association for Computational Linguistics (Findings), 2026 (채택)*.
- Joeun Kim, Seunghyouk Yoon, Xuan-Bach Le, Youngeun Nam, Doyoung Kim, Hwanjun Song, and Jae-Gil Lee\*. "QuDAR: Query-Wise Dual-Perspective Adaptive Retrieval". *In Annual Meeting of the Association for Computational Linguistics (Main), 2026 (채택)*.
- Taewon Yun, Jisu Shin, Jeonghwan Choi, Seunghwan Bang, Hwanjun Song\*. "Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding". *In Annual Meeting of the Association for Computational Linguistics (Findings), 2026 (채택)*.
- Donghee Han, Daeyoung Roh, A Young Kim, Hwanjun Song\*, Mun Yong Yi\*. "Distilling LLM Reasoning into Dense Encoders: Bridging the Accuracy-Efficiency Gap in Recommendation". *In Annual Meeting of the Association for Computational Linguistics (Findings), 2026 (채택)*.
- {Minjeong Ban, Jeonghwan Choi, Hyangsuk Min}, Nicole Hee-Yeon Kim, Minseok Kim, Jae-Gil Lee, and Hwanjun Song\*. "Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks". *In International Conference on Learning Representations, 2026 (채택)*.
- Hwanjun Song\*, Jeonghwan Choi, and Minseok Kim. "Aligning Extraction and Generation for Robust Retrieval-Augmented Generation". *In International Conference on Web Search and Data Mining, 2026 (채택)*.

**2025**

- {Yuho Lee, Jiaqi Deng}, Nicole Hee-yeon Kim, Hyangsuk Min, Taewon Yun, Minjeong Ban, Yul Kim, and Hwanjun Song\*. "Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts". *In International Conference on Empirical Methods in Natural Language Processing (Main), 2025 (채택)*.
- Donghee Han, Hwanjun Song\*, and Mun Young Yi\*. "Rethinking LLM-Based Recommendations: A Personalized Query-Driven Parallel Integration". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2025 (채택)*.
- Taewon Yun, Jihwan Oh, Hyangsuk Min, Yuho Lee, Jihwan Bang, Jason Cai, and Hwanjun Song\*. "ReFeed: Multi-Dimensional Summarization Refinement with Reflective Reasoning on Feedback". *In Conference on Language Modeling, 2025 (채택)*.
- Nicole Hee-Yeon Kim and Hwanjun Song\*. "Robust Dataset Condensation using Supervised Contrastive Learning". *In International Conference on Computer Vision, 2025 (채택)*.
- Donghee Han, Daeyoung Roh, Euihwan Han, Hwanjun Song\*, and Mun Yong Yi\*. "Fine-Grained Multi-Prompt Essay Scoring with Multi-Level Disentanglement". *Data Mining and Knowledge Discovery, 2025*.
- Seunghwan Bang, and Hwanjun Song\*. "LLM-based User Profile Management for Recommender System". *International ACM SIGIR Conference on Research and Development in Information Retrieval (GENNEXT Workshop), 2025 (채택)*.
- {Hyangsuk Min, Yuho Lee}, Minjeong Ban, Jiaqi Deng, Nicole Hee-Yeon Kim, Taewon Yun, Hang Su, Jason Cai, and Hwanjun Song\*. "Towards Multi-dimensional Evaluation of LLM Summarization across Domains and Languages". *Annual Meeting of the Association for Computational Linguistics (Main), 2025 (채택)*.
- Jeonghwan Choi, Minjeong Ban, Minseok Kim, and Hwanjun Song\*. "Word2Passage : Word-level Importance Re-weighting for Query Expansion". *In Annual Meeting of the Association for Computational Linguistics (Findings), 2025 (채택)*.
- Youngeun Nam, Jihye Na, Susik Yoon, Hwanjun Song, Jae-Gil Lee\*, and Byung Suk Lee. "Bi-Modal Learning for Networked Time Series". *In International Conference on Knowledge Discovery and Data Mining, 2025 (채택)*.
- Jihye Na, Youngeun Nam, Susik Yoon, Hwanjun Song, Byung Suk Lee, and Jae-Gil Lee\*. "Mobility Networked Time-Series Forecasting Benchmark Datasets". *In International AAAI Conference on Web and Social Media, 2025 (채택)*.
- Hwanjun Song\*, Taewon Yun, Yuho Lee, Jihwan Oh, Gihun Lee, Jason Cai, and Hang Su. "Learning to Summarize from LLM-generated Feedback". *In Annual Conference of the North American Chapter of the Association for Computational Linguistics (Main), 2025*.
- Mahnaz Koupaee, Jake W. Vincent, Saab Mansour, Igor Shalyminov, Han He, Hwanjun Song, Raphael Shu, Jianfeng He, Yi Nian, Amy Wing-mei Wong, and Kyu J. Han, Hang Su\*. "Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation". *In Annual Conference of the North American Chapter of the Association for Computational Linguistics (Main), 2025 (채택)*.
- Youngjun Lee, Doyoung Kim, Junhyeok Kang, Jihwan Bang, Hwanjun Song, and Jae-Gil Lee\*. "RA-TTA: Retrieval-Augmented Test-Time Adaptation for Vision-Language Models". *In International Conference on Learning Representations, 2025 (채택)*.
- Jihwan Oh, Jeonghwan Choi, Nicole Hee-Yeon Kim, Taewon Yun, and Hwanjun Song\*. "Learning to Verify Summary Facts with Fine-Grained LLM Feedback". *In International Conference on Computational Linguistics, 2025 (채택)*.

**2024**

- {Yuho Lee, Taewon Yun}, Jason Cai, Hang Su, and Hwanjun Song\*. "UniSumEval: Towards Unified, Fine-grained, Multi-dimensional Summarization Evaluation for LLMs". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2024*.
- Yooju Shin, Jaehyun Park, Susik Yoon, Hwanjun Song, Byung Suk Lee, and Jae-Gil Lee\*. "Exploiting Representation Curvature for Boundary Detection in Time Series". *In Advances in Neural Information Processing Systems, 2024*.
- Shunqi Mao, Chaoyi Zhang, Hang Su, Hwanjun Song, Igor Shalyminov, and Weidong Cai\*. "Controllable Contextualized Image Captioning: Directing the Visual Narrative through User-Defined Highlights". *In International Conference on European Conference on Computer Vision, 2024*.
- {Hwanjun Song\* and Jihwan Bang}. "Prompt-Guided DETR with RoI-Pruned Masked Attention for Open-Vocabulary Object Detection". *Pattern Recognition, 2024*.
- Jemin Lee, Yongin Kwon, Sihyeong Park, Misun Yu, Jeman Park, and Hwanjun Song\*. "Q-HyViT: Post-Training Quantization of Hybrid Vision Transformers with Bridge Block Reconstruction for IoT Systems". *IEEE Internet of Things Journal, 2024*.
- Hwanjun Song\*, Hang Su, Igore Shalyminov, Jason Cai, and Saab Mansour. "FineSurE: Fine-grained Summarization Evaluation using LLMs". *In Annual Meeting of the Association for Computational Linguistics (Main), 2024*.
- Yuwei Zhang, Siffi Singh, Sailik Sengupta, Igor Shalyminov, Hwanjun Song, and Saab Mansour. "Can Your Model Tell a Negation from an Implicature? Unravelling Challenges With Intent Encoders". *In Annual Meeting of the Association for Computational Linguistics (Main), 2024*.
- Doyoung Kim, Susik Yoon, Dongmin Park, Youngjun Lee, Hwanjun Song, Jihwan Bang, and Jae-Gil Lee\*. "One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning". *In International Conference on Machine Learning, 2024*.
- Hossein Aboutalebi, Hwanjun Song\*, Yusheng Xie, Arshit Gupta, Justin Sun, Hang Su, Igor Shalyminov, Nikolaos Pappas, Siffi Singh, and Saab Mansour. "MAGID: An Automated Pipeline for Generating Synthetic Multi-modal Datasets". *In Annual Conference of the North American Chapter of the Association for Computational Linguistics (Main), 2024*.
- Liyan Tang, Igor Shalyminov, Amy Wing-mei Wong, Jon Burnsky, Jake W Vincent, Yu’an Yang, Siffi Singh, Song Feng, Hwanjun Song, Hang Su, Lijia Sun, Yi Zhang, Saab Mansour, and Kathleen McKeown. "TofuEval: Evaluating Hallucinations of LLMs on Topic-Focused Dialogue Summarization". *In Annual Conference of the North American Chapter of the Association for Computational Linguistics (Main), 2024*.
- Jianfeng He, Hang Su, Jason Cai, Igor Shalyminov, Hwanjun Song, and Saab Mansour. "Semi-Supervised Dialogue Abstractive Summarization via High-Quality Pseudolabel Selection". *In Annual Conference of the North American Chapter of the Association for Computational Linguistics (Main), 2024*.
- Youngeun Nam, Susik Yoon, Yooju Shin, Minyoung Bae, Hwanjun Song, Jae-Gil Lee\*, and Byung Suk Lee. "Breaking the Time-Frequency Granularity Discrepancy in Time-Series Anomaly Detection". *In Proceedings of The Web Conference, 2024*.
- Doyoung Kim, Dongmin Park, Yooju Shin, Jihwan Bang, Hwanjun Song, and Jae-Gil Lee\*. "Adaptive Shortcut Debiasing for Online Continual Learning". *In AAAI Conference on Artificial Intelligence, 2024*.
- Hwanjun Song\*, Minseok Kim, and Jae-Gil Lee. "Toward Robustness in Multi-label Classification: A Data Augmentation Strategy against Imbalance and Noise". *In AAAI Conference on Artificial Intelligence, 2024*.

**2023**

- Hwanjun Song\*, Igor Shalyminov, Hang Su, Siffi Singh, Kaisheng Yao, and Saab Mansour. "Enhancing Abstractiveness of Summarization Models through Calibrated Distillation". *In International Conference on Empirical Methods in Natural Language Processing (Findings), 2023*.
- {Sangmin Bae, Jongwoo Ko}, Hwanjun Song\*, and Se-Young Yun\*. "Fast and Robust Early-Exiting Framework for Autoregressive Language Models with Synchronized Parallel Decoding". *In International Conference on Empirical Methods in Natural Language Processing (Main), 2023*.
- Dongmin Park, Seola Choi, Doyoung Kim, Hwanjun Song, and Jae-Gil Lee\*. "Robust Data Pruning under Label Noise via Maximizing Re-labeling Accuracy". *In Advances in Neural Information Processing Systems, 2023*.
- Dahuin Jung, Dongyoon Han, Jihwan Bang, and Hwanjun Song\*. "Generating instance-level prompts for rehearsal-free continual learning". *In International Conference on Computer Vision, 2023*.
- Yooju Shin, Susik Yoon, Hwanjun Song, Dongmin Park, Byunghyun Kim, Jae-Gil Lee\*, and Byung Suk Lee. "Context Consistency Regularization for Label Sparsity in Time Series". *In International Conference on Machine Learning, 2023*.
- {SangMook Kim, Sangmin Bae}, Hwanjun Song\*, and Se-Young Yun\*. "Re-thinking Federated Active Learning based on Inter-class Diversity". *In International Conference on Computer Vision and Pattern Recognition, 2023*.
- Hyunseo Koh, Minhyuk Seo, Jihwan Bang, Hwanjun Song, Deokki Hong, Seulki Park, Jung-Woo Ha, and Jonghyun Choi\*. "Online Boundary-Free Continual Learning by Scheduled Data Prior". *In International Conference on Learning Representations, 2023*.
- Steven Euijong Whang, Yuji Roh, Hwanjun Song, and Jae-Gil Lee\*. "Data Collection and Quality Challenges in Deep Learning: A Data-centric AI Perspective". *The VLDB Journal, 2023*.

**2022**

- Dongmin Park, Yooju Shin, Jihwan Bang, Youngjun Lee, Hwanjun Song\*, and Jae-Gil Lee\*. "Meta-Query-Net: Resolving Purity-Informativeness Dilemma in Open-set Active Learning". *In Advances in Neural Information Processing Systems, 2022*.
- {Jaehoon Oh, Sungnyun Kim, Namgyu Ho}, Jin-Hwa Kim, Hwanjun Song\*, and Se-Young Yun\*. "Understanding Cross-Domain Few-Shot Learning: An Experimental Study". *In Advances in Neural Information Processing Systems, 2022*.
- Dongmin Park, Junhyeok Kang, Hwanjun Song, Susik Yoon, and Jae-Gil Lee\*. "Multi-View POI-level Cellular Trajectory Reconstruction for Digital Contact Tracing of Infectious Diseases". *In International Conference on Data Mining, 2022*.
- Wonyoung Shin, Jonghun Park, Taekang Woo, Yongwoo Cho, Kwangjin Oh, and Hwanjun Song\*. "E-CLIP: Large-Scale Vision-Language Representation Learning in E-Commerce". *In International Conference on Information and Knowledge Management, 2022*.
- Sangmook Kim, Wonyoung Shin, Soohyuk Jang, Hwanjun Song\*, and Se-Young Yun\*. "FedRN: Exploiting k-Reliable Neighbors Towards Robust Federated Learning". *In International Conference on Information and Knowledge Management, 2022*.
- {Jaehoon Oh, Sungnyun Kim, Namgyu Ho}, Jin-Hwa Kim, Hwanjun Song\*, and Se-Young Yun\*. "ReFine: Re-randomization before Fine-tuning for Cross-domain Few-shot Learning". *In International Conference on Information and Knowledge Management, 2022*.
- Hwanjun Song, Minseok Kim, Dongmin Park, Yooju Shin, and Jae-Gil Lee\*. "Learning from Noisy Labels with Deep Neural Networks: A Survey". *IEEE Transactions on Neural Networks and Learning Systems, 2022*.
- Sukmin Yun, Jaehyung Kim, Dongyoon Han, Hwanjun Song, Jung-Woo Ha, and Jinwoo Shin\*. "Time Is MattEr: Temporal Self-supervision for Video Transformers". *In International Conference on Machine Learning, 2022*.
- Jang-Hyun Kim, Jinuk Kim, Seong Joon Oh, Sangdoo Yun, Hwanjun Song, Joonhyun Jeong, Jung-Woo Ha, and Hyun Oh Song\*. "Dataset Condensation via Efficient Synthetic-Data Parameterization". *In International Conference on Machine Learning, 2022*.
- Yooju Shin, Susik Yoon, Sundong Kim, Hwanjun Song, Jae-Gil Lee\*, and Byung Suk Lee. "Coherence-based Label Propagation over Time Series for Accelerated Active Learning". *In International Conference on Learning Representations, 2022*.
- Hwanjun Song\*, Deqing Sun, Sanghyuk Chun, Varun Jampani, Dongyoon Han, Byeongho Heo, Wonjae Kim, and Ming-Hsuan Yang. "VIDT: An Efficient and Effective Fully Transformer-based Object Detector". *In International Conference on Learning Representations, 2022*.
- Minseok Kim, Hwanjun Song, Yooju Shin, Dongmin Park, Kijung Shin, and Jae-Gil Lee\*. "Meta-Learning for Online Update of Recommender Systems". *In AAAI Conference on Artificial Intelligence, 2022*.
- Doyoung Kim, Hyangsuk Min, Youngeun Nam, Hwanjun Song, Susik Yoon, Minseok Kim, and Jae-Gil Lee\*. "Covid-EENet: Predicting Fine-Grained Impact of COVID-19 on Local Economies". *In AAAI Conference on Artificial Intelligence, 2022*.
- Jihwan Bang, Hyunseo Koh, Seulki Park, Hwanjun Song, Jung-Woo Ha, and Jonghyun Choi\*. "Online Continual Learning on A Contaminated Data Stream with Blurry Task Boundaries". *In International Conference on Computer Vision and Pattern Recognition, 2022*.

**2021**

- Dongmin Park, Hwanjun Song, MinSeok Kim, and Jae-Gil Lee\*. "Task-agnostic undesirable feature deactivation using out-of-distribution data". *In Advances in Neural Information Processing Systems, 2021*.
- Hwanjun Song\*, Eunyoung Kim, Varun Jampan, Deqing Sun, Jae-Gil Lee, and Ming-Hsuan Yang. "Exploiting Scene Depth for Object Detection with Multimodal Transformers". *In British Machine Vision Conference, 2021*.
- Hwanjun Song, Minseok Kim, Dongmin Park, Yooju Shin, and Jae-Gil Lee\*. "Robust Learning by Self-Transition for Handling Noisy Labels". *In International Conference on Knowledge Discovery and Data Mining, 2021*.
- Jae-Gil Lee, Yuji Roh, Hwanjun Song, and Steven Euijong Whang\*. "Machine Learning Robustness, Fairness, and their Convergence". *In International Conference on Knowledge Discovery and Data Mining (Tutorial), 2021*.
- Minseok Kim, Hwanjun Song, Doyoung Kim, Kijung Shin, and Jae-Gil Lee\*. "Premere: Meta-Reweighting via Self-Ensembling for Point-of-Interest Recommendation". *In AAAI Conference on Artificial Intelligence, 2021*.

Pincette는 이동 통신 기록에 도로망과 장소 정보를 결합해 방문 장소 단위의 이동 궤적을 복원하는 자료 분석 알고리즘이다.[^poi]

## 연구 과제

과제 페이지의 국가 연구 과제 8건, 기업 연구 과제 2건, 완료 과제 6건이다. 아래 수행 기간은 모두 2021년 10월 13일–2026년 10월 13일과 겹친다. 과제명·기간·역할과 공개된 지원 기관은 연구실 표기다.[^projects]

- 고품질 데이터 및 자동 품질 평가를 통한 언어 모델 신뢰성 향상 시스템 (A System for Enhancing Language Model Reliability with High-Quality Data and Automated Quality Assessment) (기간 2024.04 – 2027.03; 역할 Principal Investigator)
- 도메인 특화 자동 가치 연계 평가를 통한 AI 모델 신뢰성 향상 (Enhancing AI Model Reliability Through Domain-Specific Automated Value Alignment Assessment) (기간 2024.09 – 2027.08; 역할 Principal Investigator)
- AI가 그려내는 화합의 세계: 공정성과 투명성을 갖춘 갈등 중재용 멀티모달 에이전틱 플랫폼 (AI’s Vision of Harmony: A Fair and Transparent Multimodal Agentic Platform for Conflict Mediation) (기간 2025.10 – 2028.09; 역할 Co-Principal Investigator)
- AI Co-Scientist 실현을 위한 지능형 Survey 에이전트 (Intelligent Survey Agents toward AI Co-Scientists) (기간 2026.04 – 2027.03; 역할 Principal Investigator)
- AI 메타 과학자 연구단 (AI Meta-Scientist) - InnoCore PostDoc Fund (기간 2026.05 – 2030.12; 역할 Participating Investigator)
- 다중문서 분석 및 생성을 위한 RAG 기술 연구 (Research on RAG for Multi-Document Analysis and Generation) (기간 2026.04 – 2026.11; 역할 Collaborating Investigator)
- 독자 파운데이션 모델 (with Upstage AI Consortium) (기간 2026.03 –; 역할 Collaborating Researcher)
- AI기반 다크팩토리 설계-구축 솔루션 개발 (Development of AI-based Dark Factory Design and Construction Solutions) (기간 2026.08 – 2030.12; 역할 Participating Investigator; 지원 NIPA (National IT Industry Promotion Agency))
- 개인화 비디오 에이전트 (Personalized Video Agent) (기간 2025.12 – 2026.12 (1st Round); 역할 Principal Researcher; 지원 Qualcomm Inc.)
- 개인화 지속 에이전트 (Personalized Continual Agent) (기간 2026.05 – 2027.05; 역할 Principal Researcher; 지원 Samsung SDS)
- 리테일 특화 RAG 프레임워크 (Retrieval-augmented Generation for Retail) (기간 2026.01 – 2026.05; 역할 Principal Researcher; 지원 GS Retail (in GS Holdings Corp.))
- 과학기술정보 특화 LLM을 위한 RAG 지원 데이터 구축 (RAG-Supported Data Building for Scientific Information Specialized LLMs) (기간 2024.06 – 2024.12; 역할 Collaborating Investigator)
- 과학기술정보에 대한 RAG 시스템의 출력 품질 향상 기술 연구 (Improving the Output Quality of the Scientific Information Specialized RAG System) (기간 2025.06 – 2025.12; 역할 Collaborating Investigator)
- VLM 기반 PDF 문서 이해 및 도로 노선 좌표 자동화 기술 개발 (Development of VLM-based PDF Document Understanding and Automated Road Alignment Coordinate Extraction Technology) (기간 2025.09 – 2025.11; 역할 Principal Investigator)
- 네이버 클라우드 컨소시엄: 옴니 파운데이션 모델 (Omni Foundation Model) (기간 2025.08 – 2025.12 (1st Round); 역할 Collaborating Researcher)
- 튜링 테스트 그 너머: 확장하고 적응하는 인간 수준 게임 플레잉 에이전트 연구 (Beyond the Turing Test: Human-Level Game-Playing Agents with Generalization and Adaptation) (기간 2025.08 – 2025.12; 역할 Co-Principal Investigator)

## 수상과 선정

2025–2026년 소식에 게시된 수상·대표 선정 가운데 2건이다. 날짜는 소식 게시일이다.[^news]

- 2026-06-12 · 송환준이 APEC ASPIRE Award 한국 대표로 선정됐다.
- 2026-01-11 · 송환준이 2025년 기술 성과를 바탕으로 KAIST Technology Innovation Award를 받았다.

## 연구실 소식

2025년 1월 3일–2026년 8월 21일의 논문 채택, 학술 활동과 직함 소식이다. 날짜는 게시일이며, 학회 논문 수는 해당 소식의 표기다. CKIM은 소식에 적힌 이름이다.[^news]

- 2026-08-21 · NeurIPS 2026에 논문 3편이 채택됐다.
- 2026-08-21 · EMNLP 2026에 논문 6편, CKIM 2026에 논문 2편이 채택됐다.
- 2026-07-09 · COLM 2026에 검색 증강 생성, 시뮬레이션, 요약 관련 논문 4편이 채택됐다.
- 2026-06-26 · ECCV 2026에 효율적인 비전·언어 모델 관련 논문 1편이 채택됐다.
- 2026-04-07 · ICML 2026에 대화형 검색과 그래프 신경망 관련 논문 2편이 채택됐다.
- 2026-04-07 · ACL 2026에 정렬 학습, 추론, 분석 관련 논문 7편이 채택됐다.
- 2026-02-26 · 송환준이 Ewon Assistant Professor에 임명됐다. 임기는 2026년 3월–2029년 2월이다.
- 2026-01-28 · ICLR 2026에 정보 검색 관련 논문 1편이 채택됐다.
- 2026-01-03 · WSDM 2026에 강건한 검색 증강 생성 관련 논문 1편이 채택됐다.
- 2025-08-21 · EMNLP 2025에 긴 문서 이해와 대형 언어 모델 기반 추천 관련 논문 2편이 채택됐다.
- 2025-08-06 · 송환준이 CIKM 연계 International Workshop on Retrieval-Driven Generative AI & ScienceON AI Challenge의 기조연사로 초청받았다.
- 2025-07-21 · 송환준이 AAAI 2026의 Area Chair로 지명됐다.
- 2025-07-08 · COLM 2025에 피드백을 숙고하는 추론을 활용한 문서 요약 논문 1편이 채택됐다.
- 2025-06-26 · ICCV 2025에 잘못된 정답 표기가 있는 자료의 데이터셋 압축 논문 1편이 채택됐다.
- 2025-06-14 · 송환준이 ICLR 2026의 Area Chair로 지명됐다.
- 2025-05-23 · SIGIR 2025 GENNEXT Workshop에 대형 언어 모델 기반 추천 논문 1편이 채택됐다.
- 2025-05-16 · ACL 2025에 대형 언어 모델 평가와 검색 증강 생성의 검색 관련 논문 2편이 채택됐다.
- 2025-05-16 · KDD 2025 연구 트랙에 시계열의 두 방식 학습 관련 논문 1편이 채택됐다.
- 2025-03-20 · ICWSM 2025에 시계열 평가용 데이터셋 논문 1편이 채택됐다.
- 2025-01-24 · NAACL 2025 Main에 환각과 선호 최적화 관련 논문 2편이 채택됐고, 두 편 모두 구두 발표로 선정됐다.
- 2025-01-23 · ICLR 2025에 검색 증강 생성을 활용한 시험 시점 적응 논문 1편이 채택됐다.
- 2025-01-03 · COLING 2025에 사실 검증 논문 1편이 채택됐고 구두 발표로 선정됐다.

## 연락

- 홈페이지: <https://disl-lab.github.io>[^home]
- 교수 전화: 042-350-3116[^gsds]

## 각주
[^home]: Data Intelligence System Lab, 연구실 소개와 소속. <https://disl-lab.github.io> (관측 2026-10-30).
[^members]: DISLab, Members의 현재 구성원·공동 지도 학생·연구 인턴·Graduates 구획. <https://disl-lab.github.io/projects/> (관측 2026-10-31).
[^pubs]: DISLab, Publications & Preprints. 별표는 교신저자, 중괄호는 공동 1저자를 뜻한다고 명시한다. <https://disl-lab.github.io/publications/> (관측 2026-10-31).
[^projects]: DISLab, Projects의 국가·기업·완료 과제. <https://disl-lab.github.io/Lab_Project/> (관측 2026-10-31).
[^opensource]: DISLab, Opensource의 모델·평가 자료·알고리즘. <https://disl-lab.github.io/opensource/> (관측 2026-10-31).
[^news]: DISLab, News & Announcements의 2025–2026년 게시 글. <https://disl-lab.github.io/news/> (관측 2026-10-31).
[^gsds]: KAIST 데이터사이언스대학원, People의 송환준 항목. <https://gsds.kaist.ac.kr/people> (관측 2026-10-30).
[^appointment]: KAIST Data Mining Lab, Graduate News의 2023년 11월 13일 「Assistant Professor Appointment at KAIST」. <https://www.kaistdmlab.org/news-1/categories/graduate-news> (관측 2026-10-31).
[^poi]: D. Park 외, J.-G. Lee, 2022 IEEE International Conference on Data Mining (ICDM) (2022). <https://doi.org/10.1109/ICDM54844.2022.00144> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/icdm54844.2022.00144> (관측 2026-10-31).
[^p1]: H. Song, J. Choi, M. Kim, arXiv:2503.04789 (온라인 2025-02-28). <https://doi.org/10.48550/arXiv.2503.04789> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.04789> (관측 2026-10-31).
[^p2]: H. Song 외, H. Su, Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 835–857 (2025). <https://doi.org/10.18653/v1/2025.naacl-long.38> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.naacl-long.38/> (관측 2026-10-31).
[^p3]: T. Yun 외, H. Song, arXiv:2503.21332 (온라인 2025-03-27). <https://doi.org/10.48550/arXiv.2503.21332> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.21332> (관측 2026-10-31).
[^p4]: Y. Lee 외, H. Song, arXiv:2409.19898 (온라인 2024-09-30). <https://doi.org/10.48550/arXiv.2409.19898> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.19898> (관측 2026-10-31).
[^p5]: S. Bang, H. Song, arXiv:2502.14541 (온라인 2025-02-20). <https://doi.org/10.48550/arXiv.2502.14541> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.14541> (관측 2026-10-31).
[^p6]: S. Mao 외, W. Cai, arXiv:2407.11449 (온라인 2024-07-16). <https://doi.org/10.48550/arXiv.2407.11449> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2407.11449> (관측 2026-10-31).
[^p7]: M. Koupaee 외, H. Su, arXiv:2502.08514 (온라인 2025-02-12). <https://doi.org/10.48550/arXiv.2502.08514> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.08514> (관측 2026-10-31).

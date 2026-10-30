# 지식공학 및 인공지능 연구실 (Knowledge Engineering and Artificial Intelligence, KEAI)

**KAIST 전산학부 · 최호진 KAIST교수**

- 분야: 자연어 이해와 질의응답, 개인화된 대화, 이미지와 언어를 함께 다루는 인공지능, 설명 가능한 인공지능과 영상 분석
- 대분야: 컴퓨팅·AI
- 태그: 멀티모달 AI[^p2][^kt], 대형 언어 모델[^p2], 컴퓨터 비전[^p7][^p8], 설명 가능한 AI(XAI)[^p8]
- 홈페이지: <https://keai.kaist.ac.kr>
- 근거와 출처: [KEAI 근거 페이지](keai-sources.md)

> 말과 글, 이미지에서 지식을 찾아 대화에 활용하고, 사용자의 맥락을 반영하는 대화 시스템과 판단 근거를 설명하는 인공지능을 연구한다.[^prof][^kt][^smc]

## 무엇을 연구하나

KEAI는 최호진 교수가 이끄는 KAIST 전산학부 연구실이다. 학과는 연구실의 목표를 다양한 자료에서 유용한 지식을 추출하고, 이를 기계가 학습에 활용할 수 있는 경험으로 쌓는 것으로 설명한다. 지식공학(지식을 컴퓨터가 활용할 수 있도록 표현하고 조직하는 분야)과 데이터마이닝(자료 속의 패턴과 관계를 찾아내는 방법)을 현실의 문제에 적용한다. 교수의 관심 분야에는 자연어 처리(사람의 말과 글을 컴퓨터로 다루는 기술), 여러 종류의 자료를 함께 쓰는 대화, 기억을 활용한 챗봇(사람과 대화를 주고받는 프로그램), 설명 가능한 인공지능(인공지능이 판단한 근거를 사람이 이해할 수 있게 드러내는 방법)이 있다.[^lab][^prof]

대화 연구에서는 문장에 맞는 이미지를 고르거나 사용자의 특성과 지난 대화를 반영하는 방법을 만든다. KT 공동 과제는 사용자에게 부여된 특성인 페르소나와 짧거나 긴 기간의 기억을 활용해 대화하는 시스템을 목표로 한다. 대표 논문 DialogCC는 대화 중 이미지를 공유할 지점을 언어 모델(언어 자료의 규칙과 관계를 학습한 모형)로 추론하고, 대화와 이미지가 맞는 학습 자료를 자동으로 만든다. Stark는 인물 특성, 시간 간격, 이미지를 담은 장기 대화 자료를 구성한다. 이런 멀티모달(글·이미지·소리처럼 종류가 다른 자료를 함께 다루는 방식) 연구는 텍스트만 주고받는 대화의 범위를 넓힌다.[^kt][^p2][^p3]

언어를 이해하는 과정 자체도 연구한다. 문장 분류에서 뜻이 모호한 사례를 찾고, 금융 문서로 계산 문제를 풀 때 필요한 항목을 고르도록 학습시키며, 서로 다른 언어의 표현을 맞춘다. 임베딩(자료의 특징이나 관계를 벡터로 나타낸 표현)을 활용하는 연구에서는 과제에 맞는 의미 표현으로 모호성을 찾거나 영어와 다른 언어의 표현을 연결한다. Exobrain 과제에서는 한국어 문장에서 시간 정보를 추출하고, 질문을 다른 표현으로 바꾸거나 질문 사이의 의미 관계를 다루는 역할을 맡았다.[^p4][^p5][^p6][^exobrain]

영상과 음성을 다루는 공학 연구도 있다. 경찰 훈련 과제에서 연구실이 맡은 것은 음성 인식·합성과 영상 속 행동 인식이다. SMC 과제는 병리 영상으로부터 분석 결과를 내는 플랫폼을 개발하며, 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야) 모형의 판단 근거를 보여 주는 기술과 영상의 결함 영역을 표시하는 도구를 만든다고 설명한다.[^police][^smc] 일반 영상 연구에서는 물체 중심 학습(장면을 개별 물체의 표현들로 나타내며 학습하는 방법)을 안정적으로 수행하는 방법을 제안했다. 또 영상 분류기가 학습한 속성을 강조 지도(입력의 어느 부분이 모형의 판단과 관련되는지 표시한 자료)에 반영하고, 관련된 예시 이미지도 함께 제시하는 방법을 연구했다.[^p7][^p8]

## 주요 연구 주제

### 1. 개인화된 멀티모달 대화와 학습 자료

대화와 이미지의 관련성을 유지하며 자료를 자동으로 만들고, 인물 특성과 지난 대화를 반영하는 대화 시스템을 연구한다. DialogCC는 이미지가 들어간 대화 자료를 만드는 절차를, Stark는 시간 간격을 포함한 장기 대화 자료를 제안한다. 외국어 교육용 가상 조교와 영어 회화 학습 보조도 과제로 다뤘다.[^p2][^p3][^kt][^vta][^voucher]

### 2. 문장 의미, 질문 이해와 언어 간 표현

문장의 뜻이 모호한 사례를 탐지하고, 문서에 있는 여러 후보 중 계산에 쓸 항목을 선택하며, 영어와 비영어의 의미 표현을 연결한다. LANGALIGN은 영어 표현과 대상 언어의 표현을 맞추는 방법을 제안하고, 한국어·일본어·중국어 실험에서 성능 향상을 보고한다.[^p4][^p5][^p6]

### 3. 여러 차례 이어지는 대화의 평가

한 번의 질문에 답하는 능력뿐 아니라 여러 차례 이어지는 상호작용을 평가한다. MultiVerse는 다양한 영상·언어 과제를 대화로 구성하고, 지각의 정확성·언어의 명료성·사실의 정확성 등을 점검하는 항목으로 평가하는 방법을 제안했다. 전체 대화 맥락을 제공했을 때 일부 모형의 성능이 나아진다는 결과도 보고했다.[^p1]

### 4. 영상 인식과 판단 근거 설명

장면을 물체별 표현으로 나누어 학습할 때 배경의 방해를 억제하고 집중할 위치를 알려 주는 방법을 제안했다. 영상 분류 결과를 해석하는 연구에서는 이미 학습한 분류기의 속성을 이용해 판단에 관련된 영역과 예시 이미지를 함께 보여 준다.[^p7][^p8] 병리 영상에서 모형의 판단 근거를 보여 주는 기술과 영상의 결함 영역을 표시하는 도구도 개발한다. 경찰 훈련에서는 영상 속 행동 인식과 음성 인식·합성을 맡는다.[^smc][^police]

## 대표 논문

최호진 교수가 저자인 2021–2026년 연구 중 대화 자료 생성, 언어 이해·표현, 대화 평가, 영상 인식과 판단 근거 설명을 다루는 여덟 편이다. 두 편은 arXiv 사전 공개본이며, “쉽게 말하면”은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 저자 순서 |
|---|---|---|---|---|
| 1 | 2025 | [MultiVerse: A Multi-Turn Conversation Benchmark for Evaluating Large Vision and Language Models](https://arxiv.org/abs/2510.16641) · arXiv 사전 공개본 | 기존 영상·언어 평가 과제들을 여러 차례 이어지는 대화로 구성한 평가 자료를 제안했다. 자동 평가자가 점검 항목에 따라 답변을 평가하도록 하고, 여러 모형을 시험해 복잡한 대화에서의 어려움을 보였다. 전체 대화 맥락을 제공하면 일부 모형의 성능이 향상된다고 보고했다.[^p1] | 1저자 Young-Jun Lee, 마지막 저자 Ho-Jin Choi |
| 2 | 2024 | [DialogCC: An Automated Pipeline for Creating High-Quality Multi-Modal Dialogue Dataset](https://doi.org/10.18653/v1/2024.naacl-long.108) · NAACL | 대화 속에서 이미지를 공유할 발화·화자·이유·이미지 설명을 GPT-4가 추론하게 하고, 발화와 관련된 여러 이미지의 일관성을 유지하는 자동 생성 절차를 제안했다. 이렇게 만든 자료로 학습한 대화 모형은 보지 못한 다른 대화 자료에서 성능이 향상됐다.[^p2] | 1저자 Young-Jun Lee, 마지막 저자 Ho-Jin Choi |
| 3 | 2024 | [Stark: Social Long-Term Multi-Modal Conversation with Persona Commonsense Knowledge](https://doi.org/10.18653/v1/2024.findings-emnlp.708) · Findings of EMNLP | 다양한 인물 특성, 시간 간격, 이미지를 포함하는 장기 대화 자료를 제안했다. ChatGPT와 이미지 대응 방법으로 대화를 자동 구성하고, 이를 이용해 이미지와 언어를 함께 다루는 대화 모형을 학습시켰다. 사람의 평가로 자료의 유효성도 살폈다.[^p3] | 1저자 Young-Jun Lee, 마지막 저자 Ho-Jin Choi |
| 4 | 2023 | [Semantic Ambiguity Detection in Sentence Classification using Task-Specific Embeddings](https://doi.org/10.18653/v1/2023.acl-industry.41) · ACL Industry Track | 문장 분류 서비스에 맥락이 부족하면 의미 모호성을 해결하기 어렵다는 문제를 다룬다. 의미 표현 사이의 유사성과 과제에 맞춘 표현을 이용해 서비스 시나리오와 학습 자료의 모호성을 탐지했다. 모호성으로 생기는 정답 표지 오류를 찾고 서비스 오류 분석에 활용할 수 있음을 보였다.[^p4] | 1저자 Jong Myoung Kim, 마지막 저자 Ho-jin Choi |
| 5 | 2024 | [Enhancing Arguments Recognition for Financial Mathematical Reasoning over Hybrid Data](https://doi.org/10.18653/v1/2024.findings-emnlp.228) · Findings of EMNLP | 긴 금융 문서의 계산 문제에서는 계산에 쓸 항목을 잘못 고를 수 있다. 정답에 포함된 항목의 가중치를 높이는 학습 방법을 제안했다. 금융 수리 질의응답 자료에서 기존 모형보다 계산 실행 정확도와 계산 절차의 정확도가 높아졌고, 정답과 고른 항목의 유사성도 향상됐다고 보고했다.[^p5] | 1저자 Jinsu Lim, 마지막 저자 Ho-Jin Choi |
| 6 | 2025 | [LANGALIGN: Enhancing Non-English Language Models via Cross-Lingual Embedding Alignment](https://arxiv.org/abs/2503.18603) · arXiv 사전 공개본 | 영어 자료로 비영어 언어 모형을 학습할 때 언어 간 표현의 차이를 다룬다. 언어 모형과 과제 처리 부분이 만나는 지점에서 영어와 대상 언어의 표현을 맞추는 방법을 제안했다. 한국어·일본어·중국어에서 성능 향상을 보고했고, 반대로 대상 언어 자료를 영어 기반 모형이 처리할 표현으로 바꾸는 활용도 보였다.[^p6] | 1저자 Jong Myoung Kim, Ho-Jin Choi는 4명 중 3번째 |
| 7 | 2023 | [Shepherding Slots to Objects: Towards Stable and Robust Object-Centric Learning](https://doi.org/10.1109/CVPR52729.2023.01840) · CVPR | 한 장의 이미지에서 장면을 물체별 표현으로 나누어 학습할 때 결과가 일관되지 않는 문제를 다룬다. SLASH(SLot Attention via SHepherding)라는 방법에 배경의 방해를 억제하는 구성 요소와 집중할 위치를 알려 주는 구성 요소를 넣었다. 보조 표지를 활용하는 학습 방법도 제안했으며, 학습한 모형을 적용할 때는 보조 표지 없이 사용할 수 있다. 여러 영상 자료에서 물체 표현을 일관되게 학습하는 결과를 보고했다.[^p7] | 1저자 Jinwoo Kim, Ho-Jin Choi는 4명 중 3번째 |
| 8 | 2025 | [Attribute-guided Relevance Propagation for interpreting image classifier based on Deep Neural Networks](https://doi.org/10.1016/j.cviu.2025.104370) · Computer Vision and Image Understanding | 영상 분류 모형이 어떤 근거로 판단했는지 해석하는 ARP(Attribute-guided Relevance Propagation)를 제안했다. 이미 학습한 분류기의 특정 계산 층에서 속성을 학습하고 이를 강조 지도에 반영한다. 지도에 표시된 핵심 영역과 관련된 예시 이미지도 제시한다. 여러 영상 분류기를 이용한 수치 평가와 결과 해석을 통해 방법의 유효성을 살폈다.[^p8] | 1저자 Seung-Ho Han, 마지막 저자 Ho-Jin Choi |

## 교수와 전문 분야

최호진은 전산학부 교수 명단과 상세 소개에 “KAIST교수”로 올라 있다. 1982년 서울대학교 컴퓨터공학 학사, 1985년 영국 Newcastle University의 Computing Software and Systems Design 석사, 1995년 Imperial College London의 인공지능 박사 학위를 받았다. 학과는 전공을 인공지능·소프트웨어공학으로 적는다.[^faculty][^prof]

연구실 교수 소개는 2018년부터 Smart Energy AI Research Center, 2020년부터 Center for Artificial Intelligence Research(CAIR)의 센터장을 맡는다고 적는다. 관심 분야로 지능형 에이전트(주어진 환경의 정보를 바탕으로 판단하고 행동하는 계산 주체), 설명 가능한 인공지능, 자연어 처리, 멀티모달 대화 생성, 기억 기반 챗봇, 음성의 감정 이해, 이상 탐지와 자료 정리, 전력 수요 예측, 윤리적 인공지능을 든다.[^prof]

대표 논문에서 확인되는 전문 분야는 대화 자료의 자동 구성과 개인화된 이미지·언어 대화, 문장 의미의 모호성 탐지와 문서 기반 수리 질의응답, 언어 간 표현의 연결, 대화 평가다.[^p1][^p2][^p3][^p4][^p5][^p6] 영상 쪽에서는 물체별 표현을 학습하는 방법과 영상 분류 결과의 판단 근거를 해석하는 방법을 연구한다.[^p7][^p8]

## 응용 분야

KT 공동 연구는 개인의 맥락과 기억을 활용하는 대화를, 가상 조교 과제는 외국어 교육과 학생·교수 지원을, United Associates 공동 과제는 초등학생의 영어 회화 학습 보조를 대상으로 한다.[^kt][^vta][^voucher] 병리 영상 과제는 분석 결과의 근거 표시와 영상 품질 확인 도구를 개발하며,[^smc] 경찰 훈련 과제는 가상 훈련 환경의 음성과 행동 인식을 다룬다.[^police]

## 구성원

2026년 10월 30일 연구실 Members 페이지의 11명이다. 과정·연구 관심은 게시된 표기를 기준으로 적었다. “대표 논문 참여”는 위 표의 논문 전체 저자 이름과 같은 이름을 대조한 번호다. YoungJun Lee와 Young-Jun Lee는 이름의 붙임 표기 차이로 보았다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyo-Joong Oh | 박사과정 | Data Mining, Deep Learning, Personalization | aomaru@kaist.ac.kr |  |
| Chae-Gyun Lim | 박사과정 | Data Mining, Bioinformatics | rayote@kaist.ac.kr |  |
| Jonghwan Hyeon | 박사과정 | Artificial Intelligence | hyeon0145@kaist.ac.kr | 2, 3 |
| Dongkun Lee | 박사과정 | Artificial Intelligence | hagg30@kaist.ac.kr |  |
| Seung Ho Han | 박사과정 | Machine Learning, Artificial Intelligence | seunghohan@kaist.ac.kr | 1, 8 |
| Moonjong Jang | 박사과정 | Artificial Intelligence | m.jang@kaist.ac.kr |  |
| YoungJun Lee | 박사과정 | NLP | yj2961@kaist.ac.kr | 1, 2, 3, 4, 5, 6 |
| Mahe Zabin | 박사과정 | Machine Learning | mahezabin@kaist.ac.kr |  |
| Yechan Hwang | 석박사통합과정 (Doctoral) | Bioinformatics, NLP | yemintmint@kaist.ac.kr | 1, 5 |
| Jong Myoung Kim | 박사과정 | NLP | grayapple@kaist.ac.kr | 4, 6 |
| Eojin Joo | 석사과정 | Artificial Intelligence | akwkek11@kaist.ac.kr | 1 |

## 졸업생과 이전 구성원

2026년 10월 30일 Alumni 페이지의 44명이다. 학위·과정과 진로는 페이지 표기다. 연도가 붙은 학위·과정은 그 표기에 함께 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jinsu Lim | Master |  |
| Janghyuk Choi | Master |  |
| Faiz Ghifari Haznitrama | Master | PhD Candidate in Users & Information Lab. at KAIST |
| Jongwhoa Lee | Master | ACTNOVA |
| Minho Sim | Master | MX Division, Samsung Electronics |
| Nyoungwoo Lee | Master | Scatterlab |
| Jehyun Nam | Master | Naviworks |
| Bowon Ko | Master | TmaxSoft |
| Minsu Kwon | Master | Samsung Research, Samsung Electronics |
| Hye Young Lee | Master | Government Officer |
| Zhun Li | Master | INEEJI |
| Chanyong Park | Master | SK Telecom |
| Hangyu Kim | PhD | NAVER Cloud |
| ByungSoo Ko | Master | Meta |
| You Jin Kim | Master | NAVER Cloud |
| Zae Myung Kim | Master | PhD Candidate at University of Minnesota Twin Cities |
| Ahmed Abdelli | Master | Jordan Army Officer |
| Young-Seob Jeong | PhD | Faculty Member at Chungbuk National University |
| Jong Myoung Kim | Master | SK Telecom |
| Hyo Jin Do | Master | IBM Research |
| Won-Jo Lee | Master | SAIT, Samsung Electronics |
| Giryong Choi | Master | RideFlux |
| Nur Aziza Azis | Master |  |
| Sou-Young Jin | PhD Candidate | Faculty Member at Dartmouth College |
| Jun-Beom Kim | Master | Smilegate Holdings |
| Hend Ben Hadji | PhD (ITTS) in 2013 Feb |  |
| Elbashir Abbas | Master in 2013 Feb | Lecturer at University of Medical Sciences and Technology |
| Sang-Hun Lee | Master in 2013 Feb | ADD |
| Yun Her | Master in 2012 Feb |  |
| Eugene Seo | Master in 2011 Feb | Postdoctoral Researcher at Brown University |
| Dong-Yeop Kang | Master in 2010 Sep | Assistant Professor at University of Minnesota Twin Cities |
| Syed Ahsan Fahmi | Master |  |
| Il-Sun Song | Master |  |
| Husain Abdali | Master |  |
| Hyun-Jeong Kim | Master | TTA |
| Hwa-Youn Lee | Master | Samsung Electronics |
| Young-Kyu Park | Master |  |
| Hyun-Il Shin | Master | Samsung Electronics |
| MaríaJosé Acosta-Mayorga | Master | Regulation Officer, Ministry of Transport and Telecom, Chile |
| Prakash Kadel | Master | Daumsoft Inc. |
| Ki-Hyeon Kim | Master | TmaxSoft |
| Jun-Young Park | Master |  |
| Ahmad Ibrahim | Master | Lecturer, National University of Computer Emerging Sciences, Pakistan |
| Enkhbold Nyamsuren | Master | PhD Student at University of Auckland, New Zealand |

## 최근 논문 목록 (2021–2026)

대화와 문장 이해, 시간 정보 처리, 영상·행동 인식, 설명 가능한 인공지능, 산업 설비의 이상 탐지 등을 다룬다. 연구실 논문 목록의 2021–2026년 행 가운데 47편이며, 제목·저자·발표처와 연도는 연구실 게시 시트 표기를 따랐다.[^pubs]

**2024**

- Young-Jun Lee, Byungsoo Ko, Han-Gyu Kim, Jonghwan Hyeon, and Ho-Jin Choi. "DialogCC: An Automated Pipeline for Creating High-Quality Multi-Modal Dialogue Datasets". *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL2024), Mexico City, Mexico, June 16–21, 2024*. <https://doi.org/10.18653/v1/2024.naacl-long.108>
- Chae-Gyun Lim, Young-Seob Jeong, Woo-Jin Kim, Youngjin Kim, and Ho-Jin Choi. "Text Preprocessing and Annotation Tool for Time Information". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Jinsu Lim, Ye Chan Hwang, Young-Jun Lee, and Ho-Jin Choi. "Improving Financial QA via Enhancing Argument Understanding with an Argument Predictor". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Eojin Joo, Dokyung Lee, Junyoung Youn, Joo-Won Sung, and Ho-Jin Choi. "Enhancing Knowledge Selection with Data Processing Based on Multiple Turns of Dialog in Knowledge-Grounded Open-Domain Conversations". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Dongkun Lee, Jonghwan Hyeon, and Ho-Jin Choi. "Enhanced Deep Electric Pole Anomaly Detection Using Generative Adversarial Network-based Data Augmentation". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Ye-Chan Hwang, Jinsu Lim, Young-Jun Lee, and Ho-Jin Choi. "Enhancing Numerical Reasoning Performance by Augmenting Distractor Numerical Values". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Seung-Ho Han and Ho-Jin Choi. "Refining Saliency Maps Using Gaussian Mixture Model". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Mahe Zabin, Anika Nahian Binte Kabir, Muhammad Khubayeeb Kabir, Ho-Jin Choi, and Jia Uddin. "Machine Fault Diagnosis Using EMD-Gammatone Texture Representation and A Lightweight Self-Attention SqueezeNet". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*.
- Chae-Gyun Lim, Medard Edmund Mswahili, Goodwill Erasmo Ndomba, Ho-Jin Choi, and Young-Seob Jeong. "Machine Feeling by Knowledge Acquisition with Emotion Map". *11th International Conference on Big Data and Smart Computing (BigComp2024), Bangkok, Thailand, February 18-21, 2024*. <https://doi.org/10.1109/bigcomp60711.2024.00023>

**2023**

- Ye-Chan Hwang, Jinsu Lim, Young-Jun Lee, and Ho-Jin Choi. "Augmentation for Context in Financial Numerical Reasoning over Textual and Tabular Data with Large-Scale Language Model". *2nd Table Representation Learning Workshop in NeurIPS 2023, December 15, 2023*.
- Jonghwan Hyeon, Yung-Hwan Oh, Young-Jun Lee, and Ho-Jin Choi. "Improving speech emotion recognition by fusing self-supervised learning and spectral features via mixture of experts". *Data & Knowledge Engineering, 150: 102262, December, 2023*. <https://doi.org/10.1016/j.datak.2023.102262>
- 오교중, 최호진, 안현각, 김일구. "대규모 언어모델 활용을 통한 통계자료 처리 및 온라인 가격지표 개발 방법론 연구". *제35회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT2023), 제주, 한국, 10월 12-13일, 2023*.
- 오교중, 최호진, 김일구, 김건수. "인공지능 기반 사회 통계 생산 방법론 고도화 방안: 가계동향조사와 생활시간조사 사례". *제35회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT2023), 제주, 한국, 10월 12-13일, 2023*.
- 주어진, 임채균, 이도경, 윤준영, 성주원, 최호진. "전문 지식 및 대화 정책 예측이 결합된 프롬프트를 활용한 지식 기반 대화 생성". *제35회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT2023), 제주, 한국, 10월 12-13일, 2023*.
- 황예찬, 임진수, 이영준, 최호진. "대규모 언어 모델 및 인컨텍스트 러닝을 활용한 수치 추론 데이터셋 증강". *제35회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT2023), 제주, 한국, 10월 12-13일, 2023*.
- Minho Sim, Young-Jun Lee, Dongkun Lee, and Ho-Jin Choi. "A Simple Framework for Out-of-Distribution Detection in Human Action Recognition". *26th European Conference on Artificial Intelligence (ECAI2023), Kraków, Poland, September 30-October 5, 2023*.
- Mahe Zabin, Anika Nahian Binte Kabir, Muhammad Khubayeeb Kabir, Ho-Jin Choi, and Jia Uddin. "Contrastive self-supervised representation learning framework for metal surface defect detection". *Journal of Big Data, 10.1: 145, September, 2023*.
- Jong Myoung Kim, Young-Jun Lee, Sangkeun Jung, and Ho-Jin Choi. "Semantic Ambiguity Detection in Sentence Classification using Task-Specific Embeddings". *61st Annual Meeting Of The Association For Computational Linguistics (ACL 2023), Industry Track, Toronto, Canada, July 9-14, 2023*. <https://doi.org/10.18653/v1/2023.acl-industry.41>
- Dongkun Lee, Han-Gyu Kim, and Ho-Jin Choi. "Road Anomaly Segmentation Based on Pixel-wise Logit Variance with Iterative Background Highlighting". *2023 International Conference on Robotics and Automation (ICRA2023), London, UK, May 29-June 2, 2023*.
- Chae-Gyun Lim, Young-Seob Jeong, and Ho-Jin Choi. "Multi-task Learning Approach for Utilizing Temporal Relations in Natural Language Understanding Tasks". *Scientific Reports, 13.1, May, 2023*.
- Jongwhoa Lee, Minho Sim, and Ho-Jin Choi. "MMTS: Multimodal Teacher-Student Learning for One-Shot Human Action Recognition". *10th IEEE International Conference on Big Data and Smart Computing (BigComp2023), Jeju, Korea, February 13-16, 2023*.
- Minho Sim, Jongwhoa Lee, and Ho-Jin Choi. "Attention Masking for Improved Near Out-of-Distribution Image Detection". *10th IEEE International Conference on Big Data and Smart Computing (BigComp2023), Jeju, Korea, February 13-16, 2023*.
- 임채균, 오교중, 최호진. "시간적 관계정보를 활용한 사전학습 언어모델 기반의 멀티태스크 학습 기법". *정보과학회논문지, Vol. 50, No. 1, pp. 25-31, January, 2023*.

**2022**

- 정영섭, 임채균, 이승동, Medard Edmund Mswahili, Goodwill Erasmo Ndomba, 최호진. "상대적인 시간정보의 규칙기반 정규화". *한국컴퓨터정보학회논문지, Vol. 27, No. 12, pp. 41-49, December 30, 2022*.
- 임채균, 정영섭, 옥창원, 최호진. "현업 서비스를 위한 도메인 수준 학습 방법을 활용한 지식 기반 대화생성". *제34회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT 2022), 경주, 한국, 10월 18-19일, 2022*.
- 이영준, 최윤수, 임지희, 최호진. "Pseudo Labeling을 통한 한국어 대화 추론 데이터셋 구축". *제34회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT 2022), 경주, 한국, 10월 18-19일, 2022*.
- Young-Jun Lee, Chae-Gyun Lim, Yunsu Choi, Ji-Hui Lim and Ho-Jin Choi. "PERSONACHATGEN: Generating Personalized Dialogues using GPT-3". *1st workshop on Customized Chat Grounding Persona and Knowledge (CCGPK) in COLING 2022, Gyeongju, Korea, October 16, 2022*.
- Young-Jun Lee, Chae-Gyun Lim, and Ho-Jin Choi. "Does GPT-3 Generate Empathetic Dialogues? A Novel In-Context Example Selection Method and Automatic Evaluation Metric for Empathetic Dialogue Generation". *29th International Conference on Computational Linguistics (COLING 2022), Gyeongju, Korea, October 13, 2022*.
- Mahe Zabin, Ho-Jin Choi, and Jia Uddin. "Hybrid deep transfer learning architecture for industrial fault diagnosis using Hilbert transform and DCNN–LSTM". *Journal of Supercomputing, 1-20, October, 2022*.
- 이동건, 최호진. "전이학습 및 프레임워크 결합형 원샷 2D 아바타 생성 모델". *2022 한국컴퓨터종합학술대회, 제주, 한국, 6월 29일-7월 1일, 2022*.
- 이종화, 심민호, 최호진. "행동 유사도 임베딩 기반 실시간 훈련원 행동 인식". *2022 한국컴퓨터종합학술대회, 제주, 한국, 6월 29일-7월 1일, 2022*.
- Moonjong Jang, Ho-Jin Choi, Chae-Gyun Lim, Byoungwoong An, and Jungsub Sim. "Optimization of ESS Scheduling for Cost Reduction in Commercial and Industry Customers in Korea". *Sustainability, 14.6: 3605, March, 2022*.
- 최종우, 이영준, 임채균, 최호진. "소프트웨어 요구사항 분류 모델의 성능 향상을 위한 불균형 데이터 처리에 관한 연구". *제24회 한국 소프트웨어공학 학술대회 논문집 (KCSE 2022), 평창, 한국, pp. 56-57, 1월 19-21일, 2022*.
- Taesung Choi, Dongkun Lee, Yuchae Jung, Ho-Jin Choi. "Multivariate Time-series Anomaly Detection using SeqVAE-CNN Hybrid Model". *36th International Conference on Information Networking (ICOIN 2022), Jeju, Korea, January 12-15, 2022*.
- Youngrae Kim, Jinsu Lim, Hoonhee Cho,Minji Lee, Dongman Lee, Kuk-Jin Yoon and Ho-Jin Choi. "Efficient Reference-based Video Super-Resolution (ERVSR): Single Reference Image Is All You Need". *2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Hawaii Waikoloa, USA, January 3, 2022*.

**2021**

- 오교중, 김진원, 김일훈, 임채균, 최호진. "긴급 신고 접수 지원을 위한 대화 상태 추적 및 요약 기반 실시간 텍스트 분석". *제33회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT 2021), 온라인, 10월 14-15일, 2021*.
- 임채균, 오교중, 최호진. "시간적 관계정보를 활용한 멀티태스크 심층신경망 모델 학습 기법". *제33회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT 2021), 온라인, 10월 14-15일, 2021*.
- Nyoungwoo Lee, Suwon Shin, Jaegul Choo, Ho-Jin Choi, and Sung-Hyon Myaeng. "Constructing a Multi-Modal Dialogue Dataset with Text-to-Image Replacement". *59th Annual Meeting of the Association for Computational Linguistics (ACL 2021), Online, August, 2021*.
- 심민호, 최호진. "RNN 기반 멀티에이전트 심층강화학습을 활용한 자연스러운 경로 생성". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- 이종화, 최호진. "다중 실행 불가한 시뮬레이터 기반 지능형 에이전트를 위한 분산 학습 방법". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- 황예찬, 최호진. "합리적인 강화학습 에이전트 행동 유도를 위한 심층신경망 활용방안". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- 이녕우, 최호진. "KoBERT 기반 한국어 시나리오 개체명 인식 모델 성능과 한국어 조사의 관계 분석". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- 이동건, 최호진. "시나리오 기반 군사 모의 자동화를 위한 군사배치 생성기 및 시뮬레이션 기반 자동평가". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- 현종환, 최호진. "지능형 에이전트의 강화 학습을 위한 통신 인터페이스 구축 방법". *2021 한국컴퓨터종합학술대회 (KCC 2021), 제주, 한국, 6월 23-25일, 2021*.
- Yeon-Jee Jung, Seung-Ho Han, and Ho-Jin Choi. "SLRP: Improved Heatmap Generation via Selective Layer-wise Relevance Propagation". *Electronics Letters, April 20, 2021*.
- Yeon-Jee Jung, Seung-Ho Han, and Ho-Jin Choi. "Explaining CNN and RNN using Selective Layer-wise Relevance Propagation". *IEEE Access, Vol. 9, pp. 18670-18681, March, 2021*.
- Mahe Zabin, Jia Uddin, Ho-Jin Choi, Md. Hasan Furhad and Abu.Barkat Ullah. "Industrial Fault Diagnosis using Hilbert Transform and Texture Features". *8th IEEE International Conference on Big Data and Smart Computing (BigComp2021), Jeju, Korea, January 17-20, 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 여섯 과제다. 과제명·지원 기관·기간은 연구실 게시 표기다.[^police][^smc][^kt][^exobrain][^vta][^voucher]

- XR counter-terrorism education and training test bed establishment (기간 2021-04-01 ~ 2025-12-31 (4.75 years); 지원 Government (National Police Agency))
- Development of integrated analysis platform based on digital pathology data of high incidence cancer in Korea (기간 2021-04-01 ~ 2025-12-31 (4.75 years); 지원 Samsung Medical Center)
- Development of task-oriented persona-based dialogue generation combining multi-modal interaction and knowledge modeling (기간 2021-11-01 ~ 2024-10-31 (3 years); 지원 KT Corporation)
- WiseQA platform technology for human knowledge enhancement services (기간 2013-06-01 ~ 2022-12-31 (9.6 years); 지원 Government (IITP))
- Development of affective virtual TA service based on deep learning for foreign language education (기간 2020-07-01 ~ 2022-12-31 (2.5 years); 지원 Government (KEIT))
- Smart home platform technology for AI learning assistant for English conversation (기간 2021-06-01~2022-05-31 (1 year); 지원 Government (IITP))

## 수상과 선정

연구실 논문 목록의 Best Award 칸에 “우수논문 선정”으로 적힌 세 건이다. 날짜는 각 논문 행에 적힌 학술행사 날짜다.[^pubs]

- 2023 10월 12-13일 · 우수논문 선정: 한국어-영어 공감대화 데이터셋과 성격을 기반으로 한 언어모델 평가 (발표처 제35회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT2023); 저자 이영준, 현종환, 이도경, 성주원, 최호진)
- 2022 1월 19-21일 · 우수논문 선정: 소프트웨어 요구사항 분류 모델의 성능 향상을 위한 불균형 데이터 처리에 관한 연구 (발표처 제24회 한국 소프트웨어공학 학술대회 논문집 (KCSE 2022); 저자 최종우, 이영준, 임채균, 최호진)
- 2021 10월 14-15일 · 우수논문 선정: 시간적 관계정보를 활용한 멀티태스크 심층신경망 모델 학습 기법 (발표처 제33회 한글 및 한국어 정보처리 학술대회 논문집 (HCLT 2021); 저자 임채균, 오교중, 최호진)

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 한국과학기술원 N1 전산학부 724호, 우편번호 34141.[^contact]
- 연구실 전화: +82-42-350-7761.[^contact]
- 교수 전화: +82-42-350-3561, 팩스 +82-42-350-7861.[^prof]
- 교수 사무실: 연구실 누리집은 N1 707호, 전산학부 교수 상세 소개는 E3-1 1420호로 적는다.[^prof][^faculty]

## 각주
[^lab]: KAIST 전산학부, 「지식공학 및 인공지능 연구실」. 유용한 지식 추출과 경험 축적, 인공지능·지식공학·데이터마이닝 응용 목표. <https://cs.kaist.ac.kr/research/labView?sn=54&menu=64> 관측 2026-10-27.
[^prof]: KEAI, Professor. 소속·학력·경력·연구 관심·전화·사무실. <https://keai.kaist.ac.kr/people/professor/> 관측 2026-10-30.
[^faculty]: KAIST 전산학부, 최호진 교수 상세 소개. 직위 “KAIST교수”, 전공·학위·사무실·학력. <https://cs.kaist.ac.kr/people/view?idx=366&kind=faculty&menu=160> 관측 2026-10-30.
[^members]: KEAI, Members. 박사과정·석박사통합과정·석사과정 구성원과 연구 관심·학교 이메일. <https://keai.kaist.ac.kr/people/members/> 관측 2026-10-30.
[^alumni]: KEAI, Alumni. 학위·과정과 게시 진로. <https://keai.kaist.ac.kr/people/alumni/> 관측 2026-10-30.
[^pubs]: KEAI, 연구실 논문 목록(게시 시트). 2021–2026년 행의 제목·전체 저자·발표처·기간과 우수논문 선정 표기. <https://keai.kaist.ac.kr/research_current/> 관측 2026-10-30.
[^kt]: KEAI, KT-KAIST Natural Interaction Project. 과제명·기간·지원, 페르소나 기반 대화와 개인화된 기억 모형, 여러 종류의 자료와 맥락을 활용하는 대화 연구. <https://keai.kaist.ac.kr/projects/kt-kaist-natural-interaction/> 관측 2026-10-30.
[^smc]: KEAI, SMC Digital Pathology Consortium. 과제명·기간·지원, 병리 영상 분류와 판단 근거 표시 기술, 영상 분할 모형을 통한 결함 영역 표시 도구, 고해상도 영상에서 안정적으로 분류 모형을 학습시키는 방법 개발. <https://keai.kaist.ac.kr/projects/smc-digital-pathology-consortium/> 관측 2026-10-30.
[^police]: KEAI, XR-based Police Training Platform. 과제명·기간·지원, 연구실의 음성 인식·합성과 영상 행동 인식 역할. <https://keai.kaist.ac.kr/projects/police-training-platform/> 관측 2026-10-30.
[^exobrain]: KEAI, Exobrain Project. 과제명·기간·지원, 한국어 시간 정보 추출과 질문 표현·의미 관계에 관한 연구실 역할. <https://keai.kaist.ac.kr/projects/exobrain/> 관측 2026-10-30.
[^vta]: KEAI, Affective Virtual TA Project. 과제명·기간·지원, 외국어 교육용 가상 조교 플랫폼과 기능 개발. <https://keai.kaist.ac.kr/projects/affective-virtual-ta/> 관측 2026-10-30.
[^voucher]: KEAI, United Associates Voucher Project. 과제명·기간·지원, 영어 회화 학습 보조를 위한 대화·개인화·아바타 기술 개발. <https://keai.kaist.ac.kr/projects/united-associates-voucher/> 관측 2026-10-30.
[^contact]: KEAI, Contact Us. 연구실 전화·주소. <https://keai.kaist.ac.kr/contact/> 관측 2026-10-30.
[^p1]: Y.-J. Lee 외, H.-J. Choi, arXiv 사전 공개본 (온라인 2025-10-18). <https://doi.org/10.48550/arXiv.2510.16641> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.16641>. 관측 2026-10-30.
[^p2]: Y.-J. Lee 외, H.-J. Choi, Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 1938–1963 (2024). <https://doi.org/10.18653/v1/2024.naacl-long.108> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.naacl-long.108/>. 관측 2026-10-30.
[^p3]: Y.-J. Lee 외, H.-J. Choi, Findings of the Association for Computational Linguistics: EMNLP 2024, 12137–12162 (2024). <https://doi.org/10.18653/v1/2024.findings-emnlp.708> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.findings-emnlp.708/>. 관측 2026-10-30.
[^p4]: J. M. Kim, Y.-j. Lee, S. Jung, H.-j. Choi, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 5: Industry Track), 425–437 (2023). <https://doi.org/10.18653/v1/2023.acl-industry.41> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2023.acl-industry.41/>. 관측 2026-10-30.
[^p5]: J. Lim, Y. Hwang, Y.-J. Lee, H.-J. Choi, Findings of the Association for Computational Linguistics: EMNLP 2024, 3961–3973 (2024). <https://doi.org/10.18653/v1/2024.findings-emnlp.228> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2024.findings-emnlp.228/>. 관측 2026-10-30.
[^p6]: J. M. Kim, Y.-J. Lee, H.-J. Choi, S. Jung, arXiv 사전 공개본 (온라인 2025-03-24). <https://doi.org/10.48550/arXiv.2503.18603> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.18603>. 관측 2026-10-30.
[^p7]: J. Kim, J. Choi, H.-J. Choi, S. J. Kim, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2023). <https://doi.org/10.1109/CVPR52729.2023.01840> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.cviu.2025.104370%7C10.1109/cvpr52729.2023.01840>. 관측 2026-10-30.
[^p8]: S.-H. Han, H.-J. Choi, Computer Vision and Image Understanding (2025). <https://doi.org/10.1016/j.cviu.2025.104370> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.cviu.2025.104370%7C10.1109/cvpr52729.2023.01840>. 관측 2026-10-30.

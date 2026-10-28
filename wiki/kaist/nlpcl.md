# 자연언어처리 및 계산언어학 연구실 (Natural Language Processing and Computational Linguistics Laboratory, NLP*CL Lab.)

**KAIST 전산학부 · 박종철 교수**

- 분야: 자연언어처리, 계산언어학, 문서 검색과 신뢰도 분석, 수어 번역·생성, 유해 언어 탐지와 대응 문장 생성, 언어 사용 분석, 바이오인포매틱스
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^p1][^p2][^p3], 생성 인공지능[^p5], 멀티모달 AI[^p3], 책임 있는 AI·공정성[^p1], 다중 에이전트 시스템·분산 의사결정[^p1], 설명 가능한 AI(XAI)[^p4], 바이오정보학·계산생물학[^research]
- 홈페이지: <http://nlpcl.kaist.ac.kr/home>
- 근거와 출처: [자연언어처리 및 계산언어학 연구실 근거 페이지](nlpcl-sources.md)

> 사람의 언어를 분석하는 기술로 문서를 찾고 신뢰도를 판단하며, 수어로 소통하고 온라인 유해 언어에 대응하는 방법을 연구한다. 최근에는 여러 언어모델의 의사결정, 검색 자료를 이용한 답변 생성, 언어 사용과 정신건강의 관계를 다루는 계산 방법도 개발한다.[^lab][^p1][^p2][^p4]

## 무엇을 연구하나

박종철 교수가 이끄는 연구실은 자연언어처리(컴퓨터가 사람의 말과 글을 분석하고 만들어 내는 기술)와 계산언어학(언어의 구조와 사용을 계산 모형으로 연구하는 분야)을 바탕으로 사람 사이와 사람·컴퓨터 사이의 의사소통을 돕는 서비스를 연구한다. 전산학부의 연구실 소개는 한국어·한국수어 번역, 언어 장애 진단·재활을 위한 분석, 생물학 문헌의 지식 발견, 문서 신뢰도 예측과 증강을 주요 응용으로 든다.[^lab][^research]

문서를 읽고 판단하는 연구에서는 필요한 자료를 찾는 과정과 그 자료를 어떻게 믿고 활용할지를 함께 다룬다. 연구실의 신뢰도 연구는 문장 표현을 분석하고 관련 증거 문서를 모아 문서가 얼마나 신뢰받을지 예측하며, 표현을 바꾸어 신뢰를 높이는 보조도구를 목표로 한다. 최근의 검색 증강 생성(RAG; Retrieval-Augmented Generation, 외부 자료를 검색해 답변 생성에 연결하는 방식) 연구인 EXIT는 검색 문서 안의 문맥 관계를 보존하며 필요한 문장을 골라 답변 모델에 전달한다. 또 대형 언어모델(LLM; Large Language Model, 많은 언어 자료를 학습해 글을 이해하고 생성하는 모형)들이 의견을 주고받을 때, 동료 모델의 수와 주장 방식 같은 사회적 맥락이 최종 판단에 어떤 영향을 주는지도 분석한다.[^research][^p1][^p2]

의사소통의 형태를 바꾸는 연구에는 수어 영상과 문장을 서로 연결하는 기술이 있다. SpaMo는 수어 영상에서 몸의 공간 배치와 시간에 따른 움직임을 뽑아 언어모델에 전달한다. 연구실은 한국어 문장을 한국수어 표현으로 바꾸는 연구에서 수어의 공간성과 동시성을 고려한다고 설명한다. 자료가 적은 언어도 연구 대상이다. 티그리냐어 연구에서는 말뭉치(언어 연구와 처리 기술 개발을 위해 모은 말과 글의 자료)를 모아 사전 학습(목표 과제를 배우기 앞서 자료의 일반적인 규칙과 특징을 익히는 과정)을 수행했다. 단일 언어모델과 여러 언어를 함께 다루는 모델을 품사 표지(단어에 명사·동사 등 문법적 부류를 붙이는 작업)와 감정 분석(말과 글에 나타난 정서나 평가를 판별하는 작업) 과제로 비교했다.[^lab][^p3][^p7]

온라인 유해 언어 연구는 공격적인 글을 찾아내는 것에 더해 그 글에 어떻게 대응할지를 다룬다. 연구실은 맥락과 화자·독자의 특성을 고려해 유해도를 분석하고, 독자가 경고·차단을 선택하거나 작성자가 대체 표현을 받아 볼 수 있는 시스템을 목표로 한다. ELF22는 도발 댓글과 대응 문장을 짝짓고 대응 전략을 표시한 자료를 제시한다. 이 자료로 미세조정(이미 학습한 모형을 목적에 맞는 추가 자료로 학습하는 과정)한 모델이 지정된 전략에 맞는 문장을 생성하는지를 자동 평가와 사람 평가로 살폈다.[^research][^p5]

언어에서 사람의 상태나 생물학 지식을 읽어 내는 연구도 한다. 정신건강 관련 논문은 소셜 미디어 글의 의미를 증상 설명과 비교하는 탐지 모형을 개발하고, 다른 정신질환으로의 적용과 결과 해석을 실험 자료에서 분석했다. 생물학 문헌 분석 연구팀은 논문에서 정보를 뽑아 구조화하는 텍스트 마이닝(글에서 필요한 정보와 관계를 추출하는 기술), 온톨로지(개념과 그 관계를 형식적으로 정리한 지식 표현)의 모순을 찾는 품질 관리, 이미 알려진 정보에서 새 관계를 유도하는 추론을 연구한다고 소개한다. 이 소개에는 유전자 기능 용어와 단백질 관계를 다루는 도구 개발이 포함된다.[^p4][^research]

## 주요 연구 주제

### 1. 문서 검색·신뢰도와 언어모델 의사결정

EXIT는 문장을 서로 독립적으로 고르지 않고 문맥 의존성(표현을 해석할 때 주변 표현과 상황의 정보가 필요한 성질)을 보존하는 추출식 압축(원문 일부를 골라 길이를 줄이는 방식)을 제안한다. 여러 단계의 정보 연결이 필요한 질의응답에서도 답변 정확도와 처리 시간을 평가했다. 한국어 금융기사 요약 연구에서는 사전 학습 자료와 미세조정 자료의 분야가 일치하는지에 따른 성능을 분석했다. 다중 에이전트 시스템(여러 행위자가 각자의 정보와 판단을 바탕으로 서로 영향을 주고받는 체계) 연구는 사회적 동조, 상대의 전문성에 대한 인식, 발언 분량과 설득 방식에 의한 판단 변화를 실험한다.[^p1][^p2][^p6]

### 2. 수어 번역과 자료가 적은 언어

SpaMo는 수어 동작을 단어로 적은 주석인 글로스(gloss) 없이 수어 영상을 문장으로 바꾸는 방법이다. 기존 시각 분석 모델에서 공간·움직임 특징을 얻고, 영상 특징과 텍스트를 대응시키는 학습을 거쳐 언어모델에 연결한다. 티그리냐어 연구는 해당 언어의 자료로 언어모델을 사전 학습하고, 단어의 문법적 역할을 붙이는 품사 표지와 글의 정서를 분류하는 감정 분석에서 평가한다.[^p3][^p7]

### 3. 유해 언어 탐지와 대응 문장 생성

연구실은 혐오 발언, 적의적 발언과 저속 언어 등 온라인 언어폭력의 유형을 자동으로 탐지하고, 반박 문장을 생성할 자료와 시스템을 연구한다. ELF22는 댓글의 맥락과 대응 전략을 함께 제공하며, 생성 모델이 전략을 바꾸어 대응 문장을 만들 수 있도록 구성했다.[^lab][^p5]

### 4. 언어 사용과 정신건강·생물 지식 분석

정신건강 연구에서는 소셜 미디어 글의 의미와 임상 설문지의 증상 관련 설명을 비교해 탐지 결과를 해석할 수 있는 모형을 개발했다. 생물학 문헌 분석에서는 논문에서 실험 관련 정보를 추출하고, 온톨로지(개념과 그 관계를 형식적으로 정리한 지식 표현)의 모순을 찾아내거나 새 용어·단백질 관계의 후보를 추론하는 도구를 연구한다.[^p4][^research]

## 대표 논문

연구 갈래와 발표 시기를 나누어 고른 7편이다. 아래에서 arXiv 판이라고 적은 논문은 그 판의 초록을 기준으로 설명한다. 모든 논문에서 박종철 교수는 마지막 저자로 올라 있다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

| 번호 | 논문·발표처 | 쉽게 말하면 |
|---|---|---|
| 1 | **Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives**. ACL 2026, 설명은 arXiv 판.[^p1] | 여러 언어모델의 의견을 종합하는 대표 모델이 동료들의 수, 능력, 발언 길이와 설득 방식에 영향을 받는지 분석했다. 사회적 압력이 커질 때 대표 모델의 판단 정확도가 낮아지는 현상과, 상황에 따라 설득 전략의 영향이 달라짐을 보였다. |
| 2 | **EXIT: Context-Aware Extractive Compression for Enhancing Retrieval-Augmented Generation**. Findings of ACL 2025, 설명은 arXiv 판.[^p2] | 검색한 문서의 문장 사이 관계를 유지하며 답변에 필요한 문장을 골라내는 방법이다. 질의응답 평가에서 문서를 줄이지 않은 경우와 기존 압축 방법을 비교해 답변 정확도, 처리 시간과 입력 길이를 평가했다. |
| 3 | **An Efficient Sign Language Translation Using Spatial Configuration and Motion Dynamics with LLMs**. NAACL 2025 채택, 설명은 arXiv 판.[^p3] | 수어 영상의 공간 배치와 움직임 특징을 기존 시각 분석 모델에서 뽑아 언어모델에 전달한다. 영상과 텍스트의 대응을 먼저 학습한 뒤 수어 번역을 학습하며, 글로스 주석 없이 영상을 문장으로 번역하는 성능을 평가했다. |
| 4 | **A Simple and Flexible Modeling for Mental Disorder Detection by Learning from Clinical Questionnaires**. ACL 2023, 설명은 arXiv 판.[^p4] | 소셜 미디어 글의 의미를 증상 설명과 비교해 정신질환을 탐지하는 모형을 제안했다. 실험에서는 관련 비교 모형에 대한 성능, 다른 정신질환으로의 적용, 결과 해석 가능성을 분석했다. |
| 5 | **ELF22: A Context-based Counter-Trolling Dataset to Combat Internet Trolls**. LREC 2022.[^p5] | 도발 댓글과 대응 문장을 짝지은 자료에 대응 전략을 표시했다. 이 자료로 학습한 모델이 지정된 전략에 맞춰 대응 문장을 생성하는지를 자동 평가와 사람 평가로 살폈다. |
| 6 | **Optimizing Domain Specificity of Transformer-based Language Models for Extractive Summarization of Financial News Articles in Korean**. PACLIC 35, 2021.[^p6] | 한국어 금융기사의 문장을 골라 요약하는 모형에서, 사전 학습 자료와 미세조정 자료의 분야 조합을 분석했다. 두 자료의 분야가 일치하면 그것이 금융 분야가 아니어도 요약 성능이 좋아지는 결과를 보고했다. |
| 7 | **Monolingual Pre-Trained Language Models for Tigrinya**. WiNLP 2021.[^p7] | 티그리냐어 말뭉치로 단일 언어모델을 학습하고 여러 언어를 함께 다루는 모델과 비교했다. 품사 표지와 감정 분석 과제에서 평가했으며, 자료와 학습한 모델을 공개한다고 밝혔다. |

## 교수와 전문 분야

박종철 교수의 전산학부 교수진 소개는 전문 분야를 자연언어처리, 계산언어학, 바이오인포매틱스(생물 자료를 계산 방법으로 분석하는 분야)로 적는다. 연구실 구성원 페이지의 영문 이름은 Jong C. Park다.[^faculty][^members] 최근 논문을 함께 보면 문서 검색과 언어모델의 판단, 수어와 텍스트의 연결, 유해 언어에 대한 대응, 언어 사용을 이용한 해석 가능한 탐지 모형이 전문 분야의 구체적인 연구 갈래를 이룬다.[^p1][^p2][^p3][^p4][^p5]

교수 소개는 관심 분야로 생물학·의학에서의 언어, 수어와 삶의 질을 돕는 기술, 언어 사용 장애의 진단·치료를 위한 분석, 정서가 중요한 사람·로봇 및 사람 사이의 상호작용, 텍스트 이야기를 애니메이션과 이미지로 바꾸는 기술, 개인 맞춤 자연어 정보 서비스를 든다.[^prof]

서울대학교에서 공학학사(1984년 2월)와 공학석사(1986년 2월)를 받았고, University of Pennsylvania에서 1996년 5월 박사학위를 받았다. 박사과정 지도교수는 Mark Steedman이다. 2010년 8월–2011년 8월에는 University of Edinburgh의 방문교수였다.[^prof]

학술 활동으로는 아시아 자연언어처리 연맹(Asian Federation of Natural Language Processing, AFNLP)의 부회장(2019년 6월–2022년 5월)과 회장(2022년 6월–2024년 12월)을 맡았다. Journal of Computing Science and Engineering(JCSE)의 창간 및 운영 편집장으로 2007–2024년에 활동했다.[^prof]

## 응용 분야

연구실이 제시한 응용은 농인을 위한 한국어·한국수어 번역, 독자가 문서의 신뢰도를 판단하도록 돕는 읽기 보조, 온라인 언어폭력의 탐지·대응, 언어 사용 분석을 통한 정신건강 관련 탐지, 생물학 문헌에서의 지식 발견이다.[^lab][^research] 논문에서는 검색 자료를 활용하는 질의응답, 금융기사 요약, 학습 자료가 적은 언어의 처리도 다룬다.[^p2][^p6][^p7]

## 구성원

구성원 페이지 Current Members의 인턴 6명이다(2026-10-28 열람). 시작 시점은 같은 페이지 Interns 칸의 기간 표기를 따른다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 |
|---|---|---|---|
| Archit Narumanchi | 인턴 | June, 2025 | Continual Learning; Low-resource Methods for NLP; Mental health |
| Azamat Rashidov | 인턴 | December, 2024 | Machine Learning; Explainable AI |
| Javad Ismayilzada | 인턴 | March, 2026 | Multimodal Learning; Generative AI; Explainable and Trustworthy AI |
| Antonio Recuero Bule | 인턴 | March, 2026 | Controlled Text Generation |
| Bobin Kim | 인턴 | March, 2026 | Mechanistic Interpretability; Multilingual / Cross-lingual LLM Interpretability |
| Yerassyl Temirzhanov | 인턴 | July, 2026 | Mechanistic Interpretability |

## 졸업생과 이전 구성원

구성원 페이지의 Alumni (PhD) 12명과 Alumni (MS) 37명이다. 학위·연도·진로는 연구실 표기다. 학위논문 제목은 Publications에 실린 2021–2026년 학위논문을 연결했으며, 괄호 속 연도는 그 목록의 연도다.[^members][^pubs]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Huije Lee | Ph.D. (2026) |  |  |
| Eui Jun Hwang | Ph.D. (2026) |  |  |
| Hoyun Song | Ph.D. (2025) |  |  |
| Fitsum Gaim | Ph.D. (2025) |  |  |
| Hancheol Park | Ph.D. (2024) | Nota AI | Capturing Ambiguity in Natural Language Understanding Tasks with Information from Internal Layers (PhD Dissertation, KAIST, 2023.) |
| Jung-Ho Kim | Ph.D. (2023) | EQ4ALL | Korean to Korean Sign Language Translation via Graph Generation (PhD Dissertation, KAIST, 2022.) |
| Jin-Woo Chung | Ph.D. (2018) | Samsung Advanced Institute of Technology |  |
| Hee-Jin Lee | Ph.D. (2014) | University of Texas Health Science Center at Houston (Postdoctoral researcher) |  |
| Hye-Jin Min | Ph.D. (2012) | Naver Corp. |  |
| Ho-Joon Lee | Ph.D. (2010) | U1 University |  |
| Hodong Lee | Ph.D. (2008) | Samsung Advanced Institute of Technology |  |
| Jung-jae Kim | Ph.D. (2006) | Institute for Infocomm Research, Singapore |  |
| Changgeon Ko | M.S. (2026) |  |  |
| Edyta Ołów | M.S. (2026) |  |  |
| SeungYoon Han | M.S. (2025) |  |  |
| Jeong yeon Seo | M.S. (2025) |  |  |
| Taeho Hwang | M.S. (2025) |  |  |
| Sukmin Cho | M.S. (2024) | School of Computing, KAIST | Template-based Document Labeling for Dense Retrieval (MS Thesis, KAIST, 2022.) |
| Soyeong Jeong | M.S. (2024) | Graduate School of AI, KAIST | Information Retrieval by Augmenting Document Representation (MS Thesis, KAIST, 2021) |
| Jisu Shin | M.S. (2024) | School of Computing, KAIST | Data Augmentation for Abusive Language Detection via Back-translation and Domain Knowledge (MS Thesis, KAIST, 2022.) |
| KyungGeun Roh | M.S. (2024) |  | Effective Pre-processing on Hand Keypoints for Sign Language Recognition (MS Thesis, KAIST, 2024) |
| Aujin Kim | M.S. (2024) |  | Augmentation of Sign Language Poses by Including the Understanding of the Sign Language Domain by Body Part (MS Thesis, KAIST, 2023.) |
| Dongho Choi | M.S. (2023) | Standigm | Knowledge Transfer for Enhanced Sentiment-Based Abusive Language Detection: Insights from Sarcasm Detection (MS Thesis, KAIST, 2023.) |
| ChaeHun Park | M.S. (2021) | Graduate School of AI, KAIST |  |
| Eugene Jang | M.S. (2021) | S2W | Detecting quoted claims and claim speakers in news articles using transformer-based language models (MS Thesis, KAIST, 2021.) |
| Junseop Ji | M.S. (2021) | NC |  |
| Seungwon Yoon | M.S. (2020) | peoplefund |  |
| Jinseon You | M.S. (2018) |  |  |
| Wonsuk Yang | M.S. (2018) | Lawtalk |  |
| Jimin Park | M.S. (2017) | Bluehole Studio |  |
| Joon-Yeob Kim | M.S. (2014) | Bluehole Studio |  |
| Sang-Chae Kim | M.S. (2013) | NTD |  |
| SeungJoo An | M.S. (2012) | LG CTO |  |
| Eunyoung Chang | M.S. (2010) | NHN Entertainment |  |
| Yoonjae Choi | M.S. (2009) | Georgia Institute of Technology |  |
| Seung-Cheol Baek | M.S. (2009) | Agency for Defense Development (ADD) |  |
| Sangha Kim | M.S. (2008) | Samsung Advanced Institute of Technology |  |
| Doojin Park | M.S. (2007) | Google Korea |  |
| Ji-yong Jung | M.S. (2006) | 5rocks |  |
| Chan-Goo Kang | M.S. (2006) | Venture |  |
| Semin Jang | M.S. (2004) | Samsung Electronics |  |
| Kyung Wha Hong | M.S. (2004) | NC State University (Ph.D., 2014) Samsung Electronics |  |
| Changsu Lee | M.S. (2004) | 5rocks (CEO) |  |
| Jiwon Choi | M.S. (2004) | Samsung Electronics |  |
| Hwa Jin Lee | M.S. (2002) | ParkingCloud (CSO) |  |
| O Shik Kwon | M.S. (2002) | Samsung Electronics |  |
| Hyun Sook Kim | M.S. (2002) | KT |  |
| Jin-Bok Lee | M.S. (2001) | WoowaBrothers |  |
| Hyung-joon Cho | M.S. (2000) | KT |  |

### 이전 인턴과 연구원

Interns 칸에는 현재 인턴과 이전 인턴의 기간이 함께 적혀 있다. 아래는 Current Members에 없는 인턴 15명과 Researchers 칸의 연구원 2명이다. 기간·연구 주제·소속은 해당 칸의 표기를 따른다.[^members]

| 이름 | 구분 | 기간 | 연구 주제 | 당시 소속 |
|---|---|---|---|---|
| Seungho Cho | Intern | August, 2024–July, 2026 | Machine Learning; AI Ethics; Explainable AI |  |
| Anis Rashidov | Intern | March, 2026–July, 2026 | Retrieval Augmented Generation |  |
| Youha Jin | Intern | December, 2024–February, 2025 |  |  |
| Hyeyeon Kim | Intern | June, 2024–December, 2024 | Machine Learning |  |
| Jeewoon Hong | Intern | September, 2021–December, 2021 |  | KAIST |
| Young Ju NA | Intern | February, 2021–September, 2021 | Detection of Alzheimer’s diseases; Automatic Speech Recongition; Detection of criminals using forensic linguistics | Université Sorbonne Nouvelle |
| Emil Gasimov | Intern | August, 2021–August, 2021 |  | KAIST |
| Ada Carpenter | Intern | November, 2018–December, 2019 | Journalism argument analysis | KAIST |
| Chloé Paris | Intern | May, 2019–August, 2019 | Sign language processing | École Normale Supérieure de Lyon (ENS) |
| Najoung Kim | Intern | September, 2015–June, 2016 | Linguistics | Johns Hopkins University (Ph.D. student) |
| Umang Sehgal | Intern | May, 2015–July, 2015 | Big data in the biomedical domain | LNM Institute of Information Technology |
| Van Nham Le | Intern | June, 2014–December, 2014 | Word segmentation | KAIST |
| Benjamin Renoust | Intern | September, 2008–July, 2009 | Empathy in human-machine interaction | INA (Paris) / LaBRI (Bordeaux) |
| Alok Upadhyay | Intern | May, 2009–July, 2009 | Summarization of product reviews | Bank of America |
| Il Park | Intern | May, 2004–May, 2005 | Cytokine database | Stony Brook University (Assistant Professor) |
| Soo Hyun Ryu | Researcher | June, 2019–August, 2020 | Psycholinguistics | |
| Rize Jin | Researcher | January, 2015–August, 2015 | Big data; Data architecture | Ajou University (Assistant Professor) |

## 최근 논문 목록 (2021–2026)

연구실이 게시한 학술지·책 장·학회 논문·발표 가운데 2021–2026년의 63편이다. 주제는 문서 검색·요약, 언어모델의 판단과 편향, 수어 번역·생성, 유해 언어 탐지, 자료가 적은 언어와 언어 사용 분석 등이다. 제목·저자·발표처는 연구실 표기를 따른다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. ‘To appear’ 항목은 게재 승인으로 표시하고 연구실이 적은 연도에 두었다.[^pubs][^news]

**2026**

- Azamat Rashidov, Anis Rashidov, Archit Narumanchi, and Jong C. Park. "TALIM: A Benchmark Dataset for Tajik Academic Language Intelligence Measurement". *Findings of the Association for Computational Linguistics: EMNLP 2026 (Findings of EMNLP), Oct 24-29, 2026. (채택)*.
- Seungho Cho, Changgeon Ko, Taeho Hwang, Jeong yeon Seo, and Jong C. Park. "The Impact of Retrieved Document Bias on Generated Responses in RAG: An Analysis through Political Bias Experiments". *Journal of KIISE, 53(9), 824-831, September, 2026*.
- Huije Lee, Jisu Shin, Hoyun Song, Changgeon Ko, and Jong C. Park. "Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation". *The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026), July 2 - 7, 2026. (채택)*.
- Changgeon Ko, Jisu Shin, Hoyun Song, Huije Lee, Eui Jun Hwang, and Jong C. Park. "Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives". *The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026), July 2 - 7, 2026. (채택)*.

**2025**

- Fitsum Gaim, Hoyun Song, Huije Lee, Changgeon Ko, Eui Jun Hwang, and Jong C. Park. "A Multi-Task Benchmark for Abusive Language Detection in Low-Resource Settings". *The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS, Datasets and Benchmarks Track), Dec 2-7, 2025*.
- Seungho Cho, Changgeon Ko, Eui Jun Hwang, Junmyeong Lee, Huije Lee, and Jong C. Park. "Language over Content: Tracing Cultural Understanding in Multilingual Large Language Models". *The workshop on Human-Centric AI: From Explainability and Trustworthiness to Actionable Ethics at CIKM 2025 (HCAI@CIKM 2025), Nov 14, 2025*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C. Park. "Database-Augmented Query Representation for Information Retrieval". *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP), Nov 4-9, 2025*.
- SeungYoon Han, Taeho Hwang, Sukmin Cho, Soyeong Jeong, Hoyun Song, Huije Lee, and Jong C. Park. "Temporal Information Retrieval via Time-Specifier Model Merging". *The workshop on Knowledgeable Foundation Model at ACL 2025 (KnowFM@ACL2025), Aug 1, 2025*.
- Hoyun Song, Huije Lee, Jisu Shin, Sukmin Cho, Changgeon Ko, and Jong C. Park. "Does Rationale Quality Matter? Enhancing Mental Disorder Detection via Selective Reasoning Distillation". *Findings of The 63rd Annual Meeting of the Association for Computational Linguistics: ACL 2025, July 27-Aug 1, 2025 (채택)*.
- Taeho Hwang, Sukmin Cho, Soyeong Jeong, Hoyun Song, SeungYoon Han, and Jong C. Park. "EXIT: Context-Aware Extractive Compression for Enhancing Retrieval-Augmented Generation". *Findings of The 63rd Annual Meeting of the Association for Computational Linguistics: ACL 2025, July 27-Aug 1, 2025 (채택)*.
- Eui Jun Hwang, Sukmin Cho, Junmyeong Lee, and Jong C. Park. "An Efficient Sign Language Translation Using Spatial Configuration and Motion Dynamics with LLMs". *Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Apr 29-May 4, 2025 (채택)*.
- Sukmin Cho, SJ Choi, Taeho Hwang, Jeongyeon Seo, Soyeong Jeong, Huije Lee, Hoyun Song, Jong C. Park, and YJ Kwon. "Lossless Acceleration of Large Language Models with Hierarchical Drafting based on Temporal Locality in Speculative Decoding". *Findings of the Association for Computational Linguistics: NAACL 2025, Apr 29-May 4, 2025 (채택)*.
- Taeho Hwang, Soyeong Jeong, Sukmin Cho, and Jong C. Park. "Retrieval-Augmented Generation through Zero-shot Sentence-Level Passage Refinement using LLMs". *Journal of KIISE, 54(3), March, 2025. (To appear) (게재 승인)*.
- Eui Jun Hwang, Sukmin Cho, Huije Lee, Youngwoo Yoon, and Jong C. Park. "A Spatio-Temporal Representation Learning as an Alternative to Traditional Glosses in Sign Language Translation and Production". *2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2025), Feb 28-Mar 4, 2025 (채택)*.
- Jeong yeon Seo, Sukmin Cho, and Jong C. Park. "Political Bias in Large Language Models and its Implications on Downstream Tasks". *Journal of KIISE, 52(1), 18-28, January, 2025*.

**2024**

- Seungho Cho, Changgeon Ko, Taeho Hwang, Jeong yeon Seo, and Jong C. Park. "The Impact of Retrieved Document Bias on Generated Responses in RAG: An Analysis through Political Bias Experiments". *Korea Software Congress (KSC2024), Dec 18-20, 2024*.
- Hyeyeon Kim, Junmyeong Lee, Eui Jun Hwang, and Jong C. Park. "Improving Keypoint-based Korean Sign Language Translation Performance Through Frame-wise Contrastive Learning". *Korea Software Congress (KSC2024), Dec 18-20, 2024*.
- Changgeon Ko, Jisu Shin, Hoyun Song, Jeong yeon Seo, and Jong C. Park. "Different Bias Under Different Criteria: Assessing Bias in LLMs with a Fact-Based Approach". *The workshop on Socially Responsible Language Modelling Research at NeurIPS 2024 (SoLaR@NeurIPS 2024), Dec 14, 2024. (채택)*.
- Junmyeong Lee, Eui Jun Hwang, Sukmin Cho, and Jong C. Park. "PiLaMIM: Toward Richer Visual Representations by Integrating Pixel and Latent Masked Image Modeling". *The workshop on Self-Supervised Learning - Theory and Practice at NeurIPS 2024 (SSL@NeurIPS 2024), Dec 14, 2024. (채택)*.
- Sukmin Cho, Soyeong Jeong, Jeong yeon Seo, Taeho Hwang, and Jong C. Park. "Typos that Broke the RAG's Back: Genetic Attack on RAG Pipeline by Simulating Documents in the Wild via Low-level Perturbations". *Findings of the Association for Computational Linguistics: EMNLP 2024 (Findings of EMNLP), Nov 12-14, 2024. (채택)*.
- Huije Lee, Hoyun Song, Jisu Shin, Sukmin Cho, SeungYoon Han, and Jong C. Park. "Towards Effective Counter-Responses: Aligning Human Preferences with Strategies to Combat Online Trolling". *Findings of the Association for Computational Linguistics: EMNLP 2024 (Findings of EMNLP), Nov 12-14, 2024. (채택)*.
- Taeho Hwang, Soyeong Jeong, Sukmin Cho, SeungYoon Han, and Jong C. Park. "DSLR: Document Refinement with Sentence-Level Re-ranking and Reconstruction to Enhance Retrieval-Augmented Generation". *The Third workshop on knowledge-augmented methods for NLP at ACL 2024 (KnowledgeNLP@ACL 2024), Aug 16, 2024. (채택)*.
- Jisu Shin, Hoyun Song, Huije Lee, Soyeong Jeong, and Jong C. Park. "Ask LLMs Directly, "What shapes your bias?": Measuring Social Bias in Large Language Models". *Findings of the Association for Computational Linguistics: ACL 2024 (Findings of ACL), Aug 11-16, 2024. (채택)*.
- Taeho Hwang, Soyeong Jeong, Sukmin Cho, and Jong C. Park. "Retrieval-Augmented Generation through Zero-shot Sentence-Level Passage Refinement using LLMs". *Proceedings of the Korea Computer Congress (KCC 2024), June 26-28, 2024*.
- SeungYoon Han, Aujin Kim, KyungGeun Roh, and Jong C. Park. "Enhancing Sign Language Recognition with Pose-Based Data Augmentation: Focusing on Hand Keypoints". *Proceedings of the Korea Computer Congress (KCC 2024), June 26-28, 2024*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C. Park. "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity". *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Jun 16-21, 2024. (채택)*.
- Eui Jun Hwang, Huije Lee, and Jong C. Park. "A Gloss-free Sign Language Production with Discrete Representation". *The 18th IEEE International Conference on Automatic Face and Gesture Recognition (FG 2024), May 27-31, 2024. (채택)*.
- KyungGeun Roh, Huije Lee, Eui Jun Hwang, Sukmin Cho, and Jong C. Park. "Preprocessing Mediapipe Keypoints with Keypoint Reconstruction and Anchors for Isolated Sign Language Recognition". *Proceedings of the LREC-COLING 2024 11th Workshop on the Representation and Processing of Sign Languages: Evaluation of Sign Language Resources (SignLang@LREC-COLING 2024), May 20-25, 2024. (채택)*.

**2023**

- Sukmin Cho, Jeong yeon Seo, Soyeong Jeong, and Jong C. Park. "Improving Zero-shot Reader by Reducing Distractions from Irrelevant Documents in Open-Domain Question Answering". *Findings of the Association for Computational Linguistics: EMNLP 2023 (Findings of EMNLP), Dec 6-10, 2023*.
- Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C. Park. "Test-Time Self-Adaptive Small Language Models for Question Answering". *Findings of the Association for Computational Linguistics: EMNLP 2023 (Findings of EMNLP), Dec 6-10, 2023*.
- Jinheon Baek, Soyeong Jeong, Minki Kang, Jong C. Park, and Sung Ju Hwang. "Knowledge-Augmented Language Model Verification". *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), Dec 6-10, 2023*.
- Jisu Shin, Hoyun Song, Huije Lee, Fitsum Gaim, and Jong C. Park. "Generation of Korean Offensive Language by Leveraging Large Language Models via Prompt Design". *Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL), Nov 1-4, 2023*.
- Taeho Hwang, Hoyun Song, Jisu Shin, Sukmin Cho, and Jong C. Park. "Iterative Feedback-based Personality Persona Generation for Diversifying Linguistic Patterns in Large Language Models". *Proceedings of the 35th Annual Conference on Human & Cognitive Language Technology (HCLT), Oct 12-13, 2023*.
- Jeong yeon Seo, Sukmin Cho, and Jong C. Park. "Political Bias in Large Language Models and Implications on Downstream Tasks". *Proceedings of the 35th Annual Conference on Human & Cognitive Language Technology (HCLT), Oct 12-13, 2023*.
- Hancheol Park and Jong C. Park. "Deep Model Compression Also Helps Models Capture Ambiguity". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), July 9-14, 2023*.
- Sukmin Cho, Soyeong Jeong, Jeong yeon Seo, and Jong C. Park. "Discrete Prompt Optimization via Constrained Generation for Zero-shot Re-ranker". *Findings of the Association for Computational Linguistics: ACL 2023 (Findings of ACL), July 9-14, 2023*.
- Soyeong Jeong, Jinheon Baek, Sung Ju Hwang, and Jong C. Park. "Phrase Retrieval for Open Domain Conversational Question Answering with Conversational Dependency Modeling via Contrastive Learning". *Findings of the Association for Computational Linguistics: ACL 2023 (Findings of ACL), July 9-14, 2023*.
- Hoyun Song, Jisu Shin, Huije Lee, and Jong C. Park. "A Simple and Flexible Modeling for Mental Disorder Detection by Learning from Clinical Questionnaires". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), July 9-14, 2023*.
- Fitsum Gaim, Wonsuk Yang, Hancheol Park, and Jong C. Park. "Question-Answering in a Low-resourced Language: Benchmark dataset and Models for Tigrinya". *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), July 9-14, 2023*.
- KyungGeun Roh, Eui Jun Hwang, Huije Lee, and Jong C. Park. "Korean Sign Language Recognition on Keypoints with a Transformer Model". *Proceedings of the Korea Computer Congress (KCC 2023), June 17-20, 2023*.
- Jinseok Kim, Sukmin Cho, Soyeong Jeong, and Jong C. Park. "Controllable prompt tuning with relation dependent tokens". *Proceedings of the Korea Computer Congress (KCC 2023), June 17-20, 2023*.
- Jaewoo Kim, Huije Lee, Sukmin Cho, and Jong C. Park. "Sign Language Gloss Translation using Copy Mechanism". *Proceedings of the Korea Computer Congress (KCC 2023), June 17-20, 2023*.
- Huije Lee, Jung-Ho Kim, Eui Jun Hwang, Jaewoo Kim, and Jong C. Park. "Leveraging Large Language Models with Vocabulary Sharing for Sign Language Translation". *SLTAT 2023 Workshop at ICASSP 2023, June 4-10, 2023 (채택)*.
- Soyeong Jeong, Jinheon Baek, Sung Ju Hwang, and Jong C. Park. "Realistic Conversational Question Answering with Answer Selection based on Calibrated Confidence and Uncertainty Measurement". *Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics (EACL), May 2-4, 2023. (채택)*.

**2022**

- Jisu Shin, Hoyun Song, and Jong C. Park. "Detecting Implicitly Abusive Language by Applying Out-of-Distribution Problem". *Journal of KIISE, 49(11), 948-957, November, 2022*.
- Soo Hyun Ryu, Wonsuk Yang, and Jong C. Park. "Flexible acceptance condition of generics from a probabilistic viewpoint: Towards formalization of the semantics of generics". *Journal of Psycholinguistic Research, 2022*.
- Aujin Kim, Jisu Shin, Soyeong Jeong, Sukmin Cho, and Jong C. Park. "Assessing automatic summarization model as a reading assistant". *Proceedings of the Korea Computer Congress (KCC 2022), June 29-July 1, 2022*.
- Jisu Shin, Hoyun Song, Huije Lee, and Jong C. Park. "Constructing Korean Abusive Language Dataset using Machine Translation". *Proceedings of the Korea Computer Congress (KCC 2022), June 29-July 1, 2022*.
- Jung-Ho Kim, Eui Jun Hwang, Sukmin Cho, Du Hui Lee, and Jong C. Park. "Sign Language Production With Avatar Layering: A Critical Use Case over Rare Words". *Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), June 21-23, 2022 (채택)*.
- Fitsum Gaim, Wonsuk Yang, and Jong C. Park. "GeezSwitch: Language Identification in Typologically Related Low-resourced East African Languages". *Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), June 21-23, 2022 (채택)*.
- Huije Lee, Young Ju NA, Hoyun Song, Jisu Shin, and Jong C. Park. "ELF22: A Context-based Counter-Trolling Dataset to Combat Internet Trolls". *Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), June 21-23, 2022 (채택)*.
- Soyeong Jeong, JinHeon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C. Park. "Augmenting Document Representations for Dense Retrieval with Interpolation and Perturbation". *60th Annual Meeting of the Association for Computational Linguistics (ACL 2022) (채택)*.
- Sukmin Cho, Soyeong Jeong, Wonsuk Yang, and Jong C. Park. "Query Generation with External Knowledge for Dense Retrieval". *Proceedings of Deep Learning Inside Out (DeeLIO): The 3rd Workshop on Knowledge Extraction and Integration for Deep Learning Architectures*. <https://doi.org/10.18653/v1/2022.deelio-1.3>[^qgek]

**2021**

- Jisu Shin, Hoyun Song, and Jong C. Park. "Detecting Implicitly Abusive Language by Applying Out-of-Distribution Problem". *Proceedings of the Korea Software Congress (KSC 2021), December 20-22, 2021*.
- Huije Lee, Wonsuk Yang, ChaeHun Park, Hoyun Song, Eugene Jang, and Jong C. Park. "Optimizing Domain Specificity of Transformer-based Language Models for Extractive Summarization of Financial News Articles in Korean". *35th Pacific Asia Conference on Language on Language, Information and Computation (PACLIC 35), November 5-7, 2021*.
- Eui Jun Hwang, Jung-Ho Kim, and Jong C. Park. "Non-Autoregressive Sign Language Production with Gaussian Space". *The 32nd British Machine Vision Conference (BMVC 2021), November 22-25, 2021 (채택)*.
- Hoyun Song, Soo Hyun Ryu, Huije Lee, and Jong C. Park. "A Large-scale Comprehensive Abusiveness Detection Dataset with Multifaceted Labels from Reddit". *Proceedings of the 25th Conference on Computational Natural Language Learning (CoNLL 2021), November 10-11, 2021*.
- Fitsum Gaim, Wonsuk Yang, and Jong C. Park. "Monolingual Pre-Trained Language Models for Tigrinya". *WiNLP 2021 Workshop at EMNLP 2021, November 7-11, 2021*.
- Sukmin Cho, Wonsuk Yang, ChaeHun Park, and Jong C. Park. "The Relationship between the Quality of Automatically Generated Questions and the Quantity of the Context given for the Generation". *Proceedings of the Korea Computer Congress (KCC 2021), June 22-25, 2021*.
- Soyeong Jeong, Jinheon Baek, ChaeHun Park, and Jong C. Park. "Unsupervised Document Expansion for Information Retrieval with Stochastic Text Generation". *Second Workshop on Scholarly Document Processing (SDP 2021), June 6-11, 2021*.
- ChaeHun Park, Eugene Jang, Wonsuk Yang, and Jong C. Park. "Generating Negative Samples by Manipulating Golden Responses for Unsupervised Learning of a Response Evaluation Model". *2021 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT 2021), June 6-11, 2021*.
- Soyeong Jeong, Wonsuk Yang, ChaeHun Park, and Jong C. Park. "Calibration of Pre-trained Language Model for Korean". *Journal of KIISE, Vol. 48, No. 4, pp. 434-443, April, 2021*.
- Eugene Jang, Wonsuk Yang, and Jong C. Park. "Target-Agnostic Detection of Stances Toward Entities in News Articles". *Human-Computer Interaction Korea (HCI), Korea, January 27-29, 2021*.

## 과제

누리집의 Current Projects와 Past Projects 가운데 수행 기간이 2021-10-13–2026-10-13과 겹치는 4건이다. 첫 과제는 종료일 없이 시작 시점부터의 수행 기간이 적혀 있다.[^projects]

- 청각장애인을 위한 인공지능 기반 쌍방향 수어 통역 서비스 개발 (Neural Network-Based Bidirectional Sign Language Translation for the Deaf) (기간 2021.4~; 지원 산업기술통상자원부 디지털헬스케어)
- 언어학적 분석 및 증거문서 자동 수집을 통한 신뢰도 분포 자동 예측 및 자동 증강 (Prediction and augmentation of the credibility distribution via linguistic analysis and automated evidence document collection) (기간 2018.4~2024.12; 지원 과학기술정보통신부 SW컴퓨팅산업원천기술개발 SW스타랩)
- 온라인 환경 내 언어폭력 및 혐오 표현 사용 예방을 위한 언어학적 분석 기반 유해 텍스트 자동 검출 및 순화 피드백 시스템 (A system for offensive language detection and automatic feedback with correction) (기간 2020.3~2023.2; 지원 한국연구재단 기초연구사업 중견연구자지원사업 개인연구사업)
- 한국어에서 한국수어로의 인공신경망 기반 기계 번역 연구 (Neural Machine Translation for Korean-to-KSL) (기간 2019.6~2021.11; 지원 ETRI 위탁과제: 시청각 장애인의 방송시청을 지원하는 감성표현서비스 개발)

## 수상

2021-10-13–2026-10-13 범위의 논문 수상 7건과 교수 공로상·연구성과 선정 2건이다. 연월일이 있는 행은 소식 게시일, 연월만 있는 행은 교수 소개의 수상·선정 시점, 연도만 있는 행은 논문 목록의 학회 연도와 일정이다.[^news][^pubs][^prof]

- 2024-12-18 · Seungho Cho, Changgeon Ko, Taeho Hwang, Jeong Yeon Seo, Jong C. Park의 「The Impact of Retrieved Document Bias on Generated Responses in RAG: An Analysis through Political Bias Experiments」가 Korea Software Congress 2024 Best Paper Award를 받았다.
- 2024-12-18 · Hyeyeon Kim, Junmyeong Lee, Eui Jun Hwang, Jong C. Park의 「Improving Keypoint-based Korean Sign Language Translation Performance Through Frame-wise Contrastive Learning」가 Korea Software Congress 2024 Best Paper Award를 받았다.
- 2024-06 · 박종철 교수가 Journal of Computing Science and Engineering의 편집장 활동으로 한국정보과학회(KIISE)의 Distinguished Service Award(공로상)를 받았다.
- 2024-05 · KAIST의 2023년 대표 연구성과 선정.
- 2024 · 「Retrieval-Augmented Generation through Zero-shot Sentence-Level Passage Refinement using LLMs」: (selected as the outstanding paper). Proceedings of the Korea Computer Congress (KCC 2024), June 26-28, 2024.
- 2023-07-11 · Fitsum Gaim, Wonsuk Yang, Hancheol Park, Jong C. Park의 「Question-Answering in a Low-resourced Language: Benchmark Dataset and Models for Tigrinya」가 ACL 2023 Outstanding Paper Award를 받았다.
- 2023 · 「Political Bias in Large Language Models and Implications on Downstream Tasks」: (selected as best paper). Proceedings of the 35th Annual Conference on Human & Cognitive Language Technology (HCLT), Oct 12-13, 2023.
- 2022 · 「GeezSwitch: Language Identification in Typologically Related Low-resourced East African Languages」: (selected as best paper). Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), June 21-23, 2022
- 2021 · 「Detecting Implicitly Abusive Language by Applying Out-of-Distribution Problem」: (selected as best paper). Proceedings of the Korea Software Congress (KSC 2021), December 20-22, 2021

## 소식

소식 페이지에 게시된 2021-10-15–2026-09-08 논문 채택·기조강연·학회 활동 소식 21건이다. 날짜는 소식 게시일이다.[^news]

- 2026-09-08 · 「CASCADE: Cognitive Assessment via Sentence Context and Distortion Extraction」가 Findings of AACL-IJCNLP 2026에 채택됐다.
- 2026-08-21 · 「TALIM: A Benchmark Dataset for Tajik Academic Language Intelligence Measurement」가 Findings of EMNLP 2026에 채택됐다.
- 2026-04-07 · 「Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation」와 「Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives」가 ACL 2026 본 학회에 채택됐다.
- 2025-08-01 · 「Does Rationale Quality Matter? Enhancing Mental Disorder Detection via Selective Reasoning Distillation」와 「EXIT: Context-Aware Extractive Compression for Enhancing Retrieval-Augmented Generation」가 Findings of ACL 2025에 채택됐다.
- 2025-05-01 · 수어 번역 논문 「An Efficient Sign Language Translation Using Spatial Configuration and Motion Dynamics with LLMs」가 NAACL 2025에, 언어모델 생성 가속 논문 「Lossless Acceleration of Large Language Models with Hierarchical Drafting based on Temporal Locality in Speculative Decoding」가 Findings of NAACL 2025에 채택됐다.
- 2025-03-02 · 수어 번역·생성의 시공간 표현 학습 논문 「A Spatio-Temporal Representation Learning as an Alternative to Traditional Glosses in Sign Language Translation and Production」의 WACV 2025 워크숍 채택을 알렸다.
- 2024-12-14 · 언어모델 편향 분석 논문 「Different Bias Under Different Criteria: Assessing Bias in LLMs with a Fact-Based Approach」와 시각 표현 학습 논문 「PiLaMIM: Toward Richer Visual Representations by Integrating Pixel and Latent Masked Image Modeling」가 각각 NeurIPS 2024의 SoLaR·SSL 워크숍에 채택됐다.
- 2024-11-12 · 검색 증강 생성 공격 논문 「Typos that Broke the RAG’s Back: Genetic Attack on RAG Pipeline by Simulating Documents in the Wild via Low-level Perturbations」와 온라인 도발 대응 논문 「Towards Effective Counter-Responses: Aligning Human Preferences with Strategies to Combat Online Trolling」가 Findings of EMNLP 2024에 채택됐다.
- 2024-05-17 · 「Ask LLMs Directly, "What shapes your bias?": Measuring Social Bias in Large Language Models」가 Findings of ACL 2024에, 「DSLR: Document Refinement with Sentence-Level Re-ranking and Reconstruction to Enhance Retrieval-Augmented Generation」가 ACL 2024의 KnowledgeNLP 워크숍에 채택됐다.
- 2024-03-21 · 「Preprocessing Mediapipe Keypoints with Keypoint Reconstruction and Anchors for Isolated Sign Language Recognition」가 LREC-COLING 2024의 수어 자원 평가 워크숍에 채택됐다.
- 2024-03-14 · 「Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity」가 NAACL 2024에 채택됐다.
- 2024-03-14 · 「A Gloss-free Sign Language Production with Discrete Representation」가 FG 2024에 채택됐다.
- 2023-12-06 · 논문 3편이 EMNLP 2023에 채택됐다.
- 2023-12-06 · 박종철 교수가 EMNLP 2023에서 「Human-Centric Natural Language Processing」를 주제로 기조강연을 했다.
- 2023-11-02 · 박종철 교수가 인도네시아 발리에서 열린 IJCNLP-AACL 2023의 General Chair(대회 총괄 의장)를 맡았다. 학회 기간은 2023년 11월 1–4일이다.
- 2023-07-09 · 논문 5편이 ACL 2023에 채택됐다.
- 2023-06-10 · 「Leveraging Large Language Models with Vocabulary Sharing for Sign Language Translation」가 ICASSP 2023의 SLTAT 워크숍에 채택됐다.
- 2023-05-02 · 「Realistic Conversational Question Answering with Answer Selection based on Calibrated Confidence and Uncertainty Measurement」가 EACL 2023에 채택됐다.
- 2022-04-05 · 「Sign Language Production With Avatar Layering: A Critical Use Case over Rare Words」, 「GeezSwitch: Language Identification in Typologically Related Low-resourced East African Languages」와 「ELF22: A Context-based Counter-Trolling Dataset to Combat Internet Trolls」가 LREC 2022에 채택됐다.
- 2022-02-24 · 「Augmenting Document Representations for Dense Retrieval with Interpolation and Perturbation」가 ACL 2022에 채택됐다.
- 2021-10-15 · 「Non-Autoregressive Sign Language Production with Gaussian Space」가 BMVC 2021에 채택됐다.

## 연락과 위치

- 주소: 34141 대전광역시 유성구 대학로 291, KAIST 전산학부[^home]
- 연구실 대표 전화: (+82) 042-350-7741, 팩스: (+82) 042-350-7841[^home]
- 교수 연락 전화: 042-350-3541[^lab][^faculty]
- 교수 연구실: E3-1, 2406호(전산학부 교수진 표기). 학과 연구실 소개 쪽의 사무실 표기는 E3-1, 2415호다.[^faculty][^lab]
[^home]: KAIST NLP*CL Lab., 첫 화면. <http://nlpcl.kaist.ac.kr/home> 관측일 2026-10-28.
[^lab]: KAIST 전산학부, 「자연언어처리 및 계산언어학 연구실」. 연구실 명칭·박종철 교수·연구 소개·사무실. <https://cs.kaist.ac.kr/research/labView?sn=81&menu=64> 관측일 2026-10-27.
[^faculty]: KAIST 전산학부 교수진, 박종철 교수 항목. 직급·교수 연구실·전문 분야·전화. <https://cs.kaist.ac.kr/people/faculty> 관측일 2026-10-27.
[^members]: KAIST NLP*CL Lab., Members, Current Members·Researchers·Interns·Alumni (PhD)·Alumni (MS). <https://nlpcl.kaist.ac.kr/members?category=all> 관측일 2026-10-28.
[^research]: KAIST NLP*CL Lab., Research. 문서 신뢰도 분석, 수어 번역, 유해 언어 탐지·순화, 언어 사용 분석, 생물학 문헌의 정보 추출·자원 관리·추론 기술 소개. <http://nlpcl.kaist.ac.kr/research/> 관측일 2026-10-28.
[^pubs]: KAIST NLP*CL Lab., Publications, All. 학술지·책 장·학회 논문·학위논문·발표 목록. <https://nlpcl.kaist.ac.kr/publications?category=all> 관측일 2026-10-28.
[^projects]: KAIST NLP*CL Lab., Projects, Current Projects·Past Projects. <http://nlpcl.kaist.ac.kr/projects/> 관측일 2026-10-28.
[^news]: KAIST NLP*CL Lab., News, All. <http://nlpcl.kaist.ac.kr/news?category=all> 관측일 2026-10-28.
[^prof]: KAIST NLP*CL Lab., Prof. Jong C. Park. 현재 소속·관심 분야·학력·방문교수·학술 활동·수상. 페이지 최근 갱신 2024-11-22. <http://nlpcl.kaist.ac.kr/prof> 관측일 2026-10-28.
[^qgek]: S. Cho, S. Jeong, W. Yang, J. Park, Query Generation with External Knowledge for Dense Retrieval. Crossref 서지의 Proceedings of Deep Learning Inside Out (DeeLIO 2022): The 3rd Workshop on Knowledge Extraction and Integration for Deep Learning Architectures. <https://doi.org/10.18653/v1/2022.deelio-1.3> OpenAlex 발표 연도도 2022. 관측일 2026-10-28.
[^p1]: C. Ko 외, J. C. Park, arXiv (온라인 2026-04-07). <https://doi.org/10.48550/arXiv.2604.06091> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.06091> 관측일 2026-10-28.
[^p2]: T. Hwang 외, J. C. Park, arXiv (온라인 2024-12-17). <https://doi.org/10.48550/arXiv.2412.12559> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2412.12559> 관측일 2026-10-28.
[^p3]: E. J. Hwang, S. Cho, J. Lee, J. C. Park, arXiv (온라인 2024-08-20). <https://doi.org/10.48550/arXiv.2408.10593> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2408.10593> 관측일 2026-10-28.
[^p4]: H. Song, J. Shin, H. Lee, J. C. Park, arXiv (온라인 2023-06-05). <https://doi.org/10.48550/arXiv.2306.02955> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2306.02955> 관측일 2026-10-28.
[^p5]: H. Lee 외, J. C. Park, Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), June 21-23, 2022 (2022). <https://nlpcl.kaist.ac.kr/publications?category=all> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://nlpcl.kaist.ac.kr/publications?category=all> 관측일 2026-10-28.
[^p6]: H. Lee 외, J. C. Park, 35th Pacific Asia Conference on Language on Language, Information and Computation (PACLIC 35), November 5-7, 2021 (2021). <https://nlpcl.kaist.ac.kr/publications?category=all> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://nlpcl.kaist.ac.kr/publications?category=all> 관측일 2026-10-28.
[^p7]: F. Gaim, W. Yang, J. C. Park, WiNLP 2021 Workshop at EMNLP 2021, November 7-11, 2021 (2021). <https://nlpcl.kaist.ac.kr/publications?category=all> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://nlpcl.kaist.ac.kr/publications?category=all> 관측일 2026-10-28.

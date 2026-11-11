# Data Mining Lab

**KAIST 김재철AI대학원 · 신기정 부교수**

- 분야: 관계 자료의 구조 분석과 학습, 대규모 자료의 요약·압축, 맞춤형 추천
- 대분야: 컴퓨팅·AI
- 태그: 그래프 기계학습·지식 그래프[^p3][^p6], 추천 시스템[^pi][^p7][^p8], 대형 언어 모델[^p8]
- 홈페이지: <https://sites.google.com/view/kaistdata>
- 근거와 출처: [Data Mining Lab 근거 페이지](kaistdata-sources.md)

> 사람·물건·집단 사이의 관계에서 반복되는 구조를 찾고 배우며, 큰 관계 자료를 요약·압축하고 사용자에게 맞는 항목을 추천하는 방법을 연구한다.[^pi][^p1][^p4][^p5][^p7][^p8]

## 무엇을 연구하나

Data Mining Lab은 신기정 교수가 이끄는 연구실이다. 교수는 자신의 연구 관심을 데이터 마이닝(많은 자료에서 반복되는 구조나 유용한 규칙을 찾는 일), 그래프 알고리즘, 네트워크 과학, 추천 시스템으로 소개한다.[^pi] 그래프는 대상들을 점으로, 대상 사이의 관계를 선으로 나타낸 구조이며, 알고리즘은 문제를 해결하는 계산 절차다. 네트워크 과학은 대상 사이의 연결 구조와 그 구조에서 일어나는 현상을 연구하는 분야다.

한 중심축은 **집단 사이의 관계를 다루는 하이퍼그래프**다. 하이퍼그래프는 하나의 연결이 여러 대상을 함께 묶을 수 있는 관계 구조로, 공동 연구나 집단 소통처럼 여러 사람이 함께 참여하는 관계를 나타낸다. 교수의 리뷰 논문은 서로 다른 분야의 실제 하이퍼그래프에서 반복되는 패턴을 찾는 연구를 정리하고, 이를 분석하는 도구와 실제 자료를 닮은 구조를 생성하는 방법을 함께 다룬다.[^p1] 다른 논문들은 집단 관계가 이어지는 정도를 측정하거나, 개별 대상과 집단의 구조를 기계학습(자료에서 규칙이나 관계를 배워 새 자료를 처리하는 방법)으로 배우는 알고리즘을 제안한다.[^p2][^p3]

다른 중심축은 **큰 자료를 어떤 구조로 표현하고 보관할 것인가**다. 연결 관계가 많은 그래프를 작은 요약으로 나타내면서 원래 관계를 정확히 복원하는 방법과, 텐서(여러 축으로 값을 정렬한 다차원 배열)를 허용하는 오차 안에서 압축하는 방법을 연구한다.[^p4][^p5] 자료의 구조를 학습한 뒤 평소의 구조나 속성과 다른 그래프를 찾는 이상 탐지도 다룬다. 특히 입력을 다시 복원할 때 생기는 오차가 작으면 정상이라는 가정이 언제 어긋나는지 분석하고, 오차를 여러 측면에서 요약하는 탐지 방법을 제안했다.[^p6]

추천 시스템에서는 사용자 기록과 항목 정보를 이용해 사용자가 고를 만한 항목을 제시하는 알고리즘을 연구한다.[^pi][^p7][^p8] 최근에는 상품의 여러 형식 정보를 처리하는 기반 모델(여러 작업에 쓸 수 있도록 폭넓은 자료로 미리 학습한 모델)을 사용자 관심에 맞게 조정하는 연구와, 대규모 언어 모델(많은 언어 자료로 학습해 문장을 해석하고 생성하는 모델)이 추천할 때 개별 항목의 정보를 검색해 보완하는 연구를 발표했다.[^p7][^p8]

## 주요 연구 주제

### 집단 관계의 구조와 학습

하이퍼그래프 연구는 관계를 표시하는 데서 더 나아가 그 구조를 수치로 설명하고 학습에 이용하는 일이다. HyperTrans 연구는 집단 관계의 전이성(이웃을 공유하는 대상 사이에도 관계가 이어지는 성질)을 재는 기준과 계산 방법을 제안하고, 실제 자료와 무작위 구조의 차이를 살폈다. 이어 하이퍼그래프에 널리 나타나는 커뮤니티(연결이 몰려 있는 대상들의 무리) 구조를 이용해 관측한 전이성 패턴을 재현하는 생성 방법을 제안했다.[^p2]

TriCL(Tri-directional Contrastive Learning)은 하이퍼그래프의 표현 학습, 즉 자료의 성질을 계산에 쓸 수 있는 수치로 바꾸는 방법을 배우는 연구다. 대조 학습(관련 있는 자료의 표현은 일치를 높이고 관련 없는 자료의 표현은 구분하도록 배우는 방법)을 개별 대상, 집단, 집단과 그 구성 대상의 관계에 함께 적용한다. 같은 자료에서 변형해 만든 두 관점 사이에 이 관계들이 일치하도록 학습해 대상 수준과 집단 수준의 정보를 함께 담는다.[^p3]

### 큰 그래프와 다차원 자료의 요약·압축

SLUGGER는 비슷한 대상들을 묶되 그 묶음 안에 다른 묶음이 들어갈 수 있게 하여 그래프를 요약한다. 연결을 추가하거나 제외하는 표시로 원래의 연결 구조를 정확히 나타내고, 묶음들을 합친 뒤 불필요한 구조를 정리한다. 계산 과정에서는 일부 자료를 표본으로 고르는 방법과 이미 계산한 결과를 보관해 다시 쓰는 방법 등을 이용한다.[^p4]

TensorCodec은 자료 구조에 강한 가정을 두지 않고 텐서를 손실 압축(원래 자료와의 차이를 허용하며 저장 크기를 줄이는 방법)한다. 신경망(연결된 계산 단위 사이의 가중치를 조정해 입력과 출력 사이의 관계를 배우는 계산 모형)을 텐서 분해(텐서를 더 작은 조각들의 곱으로 나타내는 방법)에 결합하고, 축을 늘려 자료를 다시 배치하며, 각 축의 위치 순서를 바꾸어 압축에 이용할 패턴을 드러낸다. 압축 크기와 복원 오차를 함께 평가했다.[^p5]

### 그래프 이상 탐지

그래프 오토인코더(그래프를 압축한 표현으로 바꾼 뒤 다시 복원하도록 학습하는 신경망)를 이용한 이상 탐지는 보통 평균 복원 오차가 큰 그래프를 이상으로 본다. 연구진은 이 가정이 어긋나는 사례를 제시하고 성립 조건과 실패 조건을 분석했다. MUSE는 평균값에 한정하지 않고 복원 오차의 여러 요약값을 그래프의 특징으로 삼아 이상을 찾는 방법이다.[^p6]

### 사용자와 항목에 맞춘 추천

PerPEFT는 관심이 비슷한 사용자들을 묶고, 각 묶음에 서로 다른 모델 조정 부품을 배정한다. 상품의 여러 형식 정보를 처리하는 모델에서 조정값 일부만 학습하면서도, 각 사용자 묶음의 구매 판단과 관련된 상품 측면을 담도록 하는 방법이다.[^p7]

ItemRAG는 추천할 때 비슷한 사용자의 전체 구매 이력을 가져오는 대신, 사용자 이력과 추천 후보에 속한 항목 각각에 관련 정보를 덧붙인다. 관련 항목을 검색할 때는 내용의 의미뿐 아니라 함께 구매된 정보도 이용한다. 이 방법은 일반적인 추천과 구매 기록이 부족한 신규 항목의 추천을 함께 평가했다.[^p8]

## 대표 논문

신기정 교수가 KAIST 재직 시기에 저자로 참여한 논문에서 연구 갈래와 최근 연구를 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자의 「1저자」와 「마지막 저자」는 저자 순서를 뜻한다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [A Survey on Hypergraph Mining: Patterns, Tools, and Generators](https://doi.org/10.1145/3719002) · ACM Computing Surveys | 공동 연구처럼 여러 대상이 함께 맺는 관계를 하이퍼그래프로 나타내고, 이런 구조에 반복되는 패턴을 찾는 연구를 정리한 리뷰다. 패턴을 분석하는 도구를 무작위 기준 모형, 부분 구조, 구조를 재는 수치로 나누고, 실제 자료를 닮은 하이퍼그래프 생성 방법까지 분류했다.[^p1] | 1저자 Geon Lee, 마지막 저자 신기정 |
| 2 | 2023 | [How Transitive Are Real-World Group Interactions? - Measurement and Reproduction](https://doi.org/10.1145/3580305.3599382) · KDD 2023 | 실제 집단 관계가 얼마나 전이적인지 측정하려고 지표가 갖춰야 할 성질을 정하고 HyperTrans와 이를 빠르게 계산하는 방법을 제안했다. 실제 하이퍼그래프에서 무작위 구조와 구별되는 전이성 패턴을 찾았고, 하이퍼그래프에 널리 나타나는 커뮤니티 구조를 이용해 이 패턴을 재현하는 생성 방법 THera를 만들었다.[^p2] | 1저자 Sunwoo Kim, 마지막 저자 신기정 |
| 3 | 2023 | [I'm Me, We're Us, and I'm Us: Tridirectional Contrastive Learning on Hypergraphs](https://doi.org/10.1609/aaai.v37i7.26019) · AAAI 2023 | 사람이 정답을 붙인 자료에 대한 의존을 줄이기 위해 하이퍼그래프용 대조 학습 틀 TriCL을 제안했다. 변형한 두 관점에서 같은 대상끼리, 같은 집단끼리, 집단과 그 구성 대상 사이의 표현이 일치하도록 학습한다. 이를 통해 대상과 집단의 구조 정보를 함께 담았으며, 대상 분류 실험에서 비지도 방법과 지도·반지도 경쟁 방법을 비교했다.[^p3] | 1저자 Dongjin Lee, 마지막 저자 신기정 |
| 4 | 2022 | [SLUGGER: Lossless Hierarchical Summarization of Massive Graphs](https://doi.org/10.1109/icde53745.2022.00040) · ICDE 2022 | 서로 겹치지 않는 묶음만 쓰는 그래프 요약의 한계를 풀려고, 묶음이 다른 묶음을 포함할 수 있는 계층 구조를 도입했다. 묶음 사이의 양·음 연결 표시로 원래 그래프를 정확히 나타낸다. SLUGGER는 묶음을 합치고 정리하는 계산에 표본 추출, 근사, 계산 결과 재사용을 이용하며, 기존 무손실 요약 방법보다 작은 요약을 만드는 결과를 보고했다.[^p4] | 1저자 Kyu-Han Lee, 마지막 저자 신기정 |
| 5 | 2023 | [TensorCodec: Compact Lossy Compression of Tensors without Strong Data Assumptions](https://doi.org/10.1109/icdm58522.2023.00032) · ICDM 2023 | 다차원 수치 자료를 압축할 때 자료 구조에 강한 가정을 요구하는 문제를 다뤘다. 순환 신경망(앞 단계의 출력을 다음 단계 입력과 함께 받아 순서가 있는 자료를 처리하는 신경망)을 텐서 분해에 결합하고, 자료를 축이 많은 형태로 접으며, 각 축의 위치 순서를 바꿔 압축에 쓸 패턴을 드러낸다. 비슷한 복원 오차에서 저장 크기를 줄이거나, 같은 저장 크기에서 복원을 정확하게 하는 결과를 보였다.[^p5] | 1저자 Taehyung Kwon, 마지막 저자 신기정 |
| 6 | 2024 | [Rethinking Reconstruction-based Graph-Level Anomaly Detection: Limitations and a Simple Remedy](https://doi.org/10.52202/079017-3040) · NeurIPS 2024 | 학습한 그래프와 비슷한 그래프는 잘 복원되고 이상한 그래프는 복원 오차가 클 것이라는 가정이 언제 맞고 언제 실패하는지 분석했다. 오차의 평균만 쓰는 대신 여러 측면의 요약값을 특징으로 이용하는 MUSE를 제안했다. 여러 자료와 방법을 비교한 실험에서 이 접근의 효과를 평가했다.[^p6] | 1저자 Sunwoo Kim, 마지막 저자 신기정 |
| 7 | 2026 | [Personalized Parameter-Efficient Fine-Tuning of Foundation Models for Multimodal Recommendation](https://doi.org/10.1145/3774904.3792248) · WWW 2026 | 상품의 여러 형식 정보를 처리하는 모델을 추천에 맞게 조정해도, 사용자마다 관심을 두는 상품 측면이 다르다는 점을 반영하지 못할 수 있다. PerPEFT는 사용자들을 관심별로 묶고 각 묶음에 별도 조정 부품을 배정해, 구매 판단과 관련된 상품 측면을 배우게 한다. 여러 조정 방식과 함께 쓸 수 있으며, 실험에서 추천 성능 개선을 보고했다.[^p7] | 1저자 Sunwoo Kim, 마지막 저자 신기정 |
| 8 | 2026 | [ItemRAG: Item-Based Retrieval-Augmented Generation for LLM-Based Recommendation](https://doi.org/10.1145/3805712.3809942) · SIGIR 2026 | 언어 모델로 추천할 때 비슷한 사용자의 구매 이력을 가져오면 불필요한 정보가 섞이고 개별 후보 항목의 정보는 부족할 수 있다. ItemRAG는 사용자 이력과 후보 목록의 각 항목에 관련 항목 정보를 찾아 덧붙인다. 의미 정보와 공동 구매 정보를 함께 이용했으며, 일반 조건과 신규 항목 조건에서 기존 검색 보완 방법보다 나은 추천 결과를 보고했다.[^p8] | 1저자 Sunwoo Kim, 마지막 저자 신기정 |

## 교수와 전문 분야

신기정 교수는 서울대학교에서 컴퓨터공학 학사와 경제학 복수전공 학사를 2015년 8월에, Carnegie Mellon University에서 컴퓨터과학 석사를 2017년 12월에, 박사를 2019년 2월에 받았다. 박사 지도교수는 Christos Faloutsos다. 개인 누리집은 2019년 2월–2023년 2월 KAIST Ewon Endowed Assistant Professor, 2023년 3월부터 Associate Professor로 재직한다고 적는다.[^pi] 김재철AI대학원 구성원 명단의 국문 직위는 부교수이며, 연구분야는 데이터마이닝과 그래프 알고리즘이다.[^dept]

교수는 김재철AI대학원과 전기및전자공학부에 소속되어 연구실을 이끈다고 소개한다.[^pi][^team] 최근 논문으로 보면 전문 분야는 집단 관계의 구조 분석과 학습, 큰 그래프·텐서의 압축, 그래프 이상 탐지, 사용자와 항목 정보를 함께 고려하는 추천 알고리즘으로 이어진다.[^p1][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

관계 구조 연구는 연구자들의 협업과 집단 소통을 분석하는 데 연결되고, 그래프 요약은 온라인 사회관계망이나 웹 연결처럼 큰 자료를 보관하고 처리하는 문제를 다룬다.[^p1][^p2][^p4] 추천 연구는 상품의 여러 형식 정보와 구매 기록을 활용해 사용자별 추천을 만들거나, 기록이 부족한 항목을 다루는 문제에 연결된다.[^p7][^p8] 최근 논문 목록에는 위성 영상 검색, 강수 예측, 광고 순위 결정, 약물 추천용 알고리즘, 신경 활동 영상의 정렬 알고리즘도 있다.[^pubs]

## 구성원

2026년 11월 9일 연구실 Team 페이지의 박사후연구원 2명, 박사과정 10명, 석박사통합과정 5명, 석사과정 5명이다. 과정은 게시된 구획과 과정명에 따른다. 시작은 첫 화면 소식에서 연구실 합류를 알린 연월이며 현재 과정의 시작일을 뜻하지 않는다.[^team][^home] 「대표 논문 참여」는 위 표의 논문 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Taehyung Kwon (권태형) | 박사후연구원 |  | 5 |
| Geon Lee (이건) | 박사후연구원 |  | 1, 8 |
| Fanchen Bu | 박사과정 | 2022-02 | 1, 2, 6 |
| Jaewan Chun (전재완) | 박사과정 | 2023-02 |  |
| Minku Kang (강민구) | 박사과정 |  |  |
| Shinwhan Kang (강신환) | 박사과정 |  |  |
| Joonho Kim (김준호) | 박사과정 | 2026-03 |  |
| Sojeong Kim (김소정) | 박사과정 | 2023-02 |  |
| Sunwoo Kim (김선우) | 박사과정 | 2022-02 | 2, 6, 7, 8 |
| Jongha Lee (이종하) | 박사과정 | 2023-02 |  |
| Soo Yong Lee (이수용) | 박사과정 | 2021-08 | 6 |
| Heechan Moon (문희찬) | 박사과정 | 2022-08 |  |
| Minyoung Choe (최민영) | 석박사통합과정 |  | 2 |
| Taelim Choi (최태림) | 석박사통합과정 |  |  |
| Gyurim Hwang (황규림) | 석박사통합과정 | 2026-03 |  |
| Hyunjin Hwang (황현진) | 석박사통합과정 |  | 7 |
| Kyungho Kim (김경호) | 석박사통합과정 | 2024-09 | 6 |
| Chaewoon Bae (배채운) | 석사과정 | 2026-03 |  |
| Yeonje Choi (최연제) | 석사과정 | 2025-02 |  |
| Sejin Chung (정세진) | 석사과정 |  |  |
| Yeongho Kim (김영호) | 석사과정 | 2025-02 |  |
| Annika Lee (이주현) | 석사과정 | 2026-03 |  |

## 졸업생과 이전 구성원

연구실 Team 페이지 Alumni의 박사 8명과 석사 14명이다. 학위·학기는 게시 표기이며 진로와 학위 논문도 연구실이 적은 내용이다. 박사후연구원인 Taehyung Kwon과 Geon Lee는 박사 졸업생에도 올라 있다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Dongjin Lee (이동진) | PhD in Electrical Engineering (Fall 2023) | KaKao Brain → WorldQuant | Robust Unsupervised Representation Learning for Relational Data |
| Jihoon Ko (고지훈) | PhD in Artificial Intelligence (Fall 2024) | Moloco | Compression of Large-scale Real-world Graphs and Tensors |
| Kyuhan Lee (이규한) | PhD in Artificial Intelligence (Fall 2024) | GraphAI → Samsung Electronics | Clique-based Compression of Large Graphs |
| Manh Tuan Do | PhD in Artificial Intelligence (Fall 2024) | WorldQuant | Structural Analysis, Modelling, and Improvement of Real-world Hypergraphs with Applications |
| Hyunjin Choo (주현진) | PhD in Electrical Engineering (Fall 2024) | KAIST (Postdoctoral Researcher) → ETRI | Data Mining Approaches for Predicting the Presence, Persistence, and Emergence of Group Interactions |
| Hyeonsoo Jo (조현수) | PhD in Artificial Intelligence (Spring 2025) | WorldQuant | Enhancing Robustness of Machine Learning on Graphs via Adaptive Edge Weighting |
| Taehyung Kwon (권태형) | PhD in Artificial Intelligence (Fall 2025) | KAIST (Postdoctoral Researcher) | Compression and Distillation of Real-world Tensors |
| Geon Lee (이건) | PhD in Artificial Intelligence (Fall 2025) | KAIST (Postdoctoral Researcher) → University of Wisconsin-Madison (Postdoctoral Researcher) | Mining and Learning of Real-world Hypergraphs |
| Inkyu Park (박인규) | Master in Artificial Intelligence (Spring 2021) | Krafton |  |
| Hyeonju Lee (이현주) | Master in Artificial Intelligence (Spring 2021) | Upstage → Mistral AI |  |
| Hyeonjeong Shin (신현정) | Master in Artificial Intelligence (Fall 2022) | Samsung Research |  |
| Deukryeol Yoon (윤득렬) | Master in Artificial Intelligence (Fall 2022) | Agency for Defense Development |  |
| Seungwoo Lee (이승우) | Master in Electrical Engineering (Spring 2023) | Hyperconnect |  |
| Juwon Kim (김주원) | Master in Artificial Intelligence (Spring 2023) |  |  |
| Taehyung Yu (유태형) | Master in Artificial Intelligence (Spring 2023) | VUNO |  |
| Hyunju Kim (김현주) | Master in Artificial Intelligence (Fall 2023) | Georgia Tech (PhD Student) |  |
| Dongyeong Hwang (황동영) | Master in Artificial Intelligence (Fall 2023) | Hyperconnect |  |
| Seokbum Yoon (윤석범) | Master in Artificial Intelligence (Spring 2025) | Rapport Labs |  |
| Chunji Cui | Master in Artificial Intelligence (Spring 2025) | Alibaba |  |
| Yuyeong Kim (김유영) | Master in Artificial Intelligence (Fall 2025) | NC AI |  |
| Juyeon Kim (김주연) | Master in Artificial Intelligence (Spring 2026) | LG AI Research |  |
| Dongwon Choi (최동원) | Master in Artificial Intelligence (Spring 2026) | WorldQuant |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications 페이지의 논문·학술지·워크숍 목록 116편이다. 연도와 제목·저자·발표처는 연구실의 연도 구역과 게시 표기를 따른다. 2026년 구역의 표제는 「2026 or Forthcoming」이며, 개별 출판 또는 채택 상태를 적지 않은 항목의 학회·학술지 표기도 연구실 기재다. 저자 이름의 별표는 누리집 표시다.[^pubs]

**2026**

- Geon Lee, Kyungho Kim, Dongwon Choi, Juyeon Kim, Shinhwan Kang, and Kijung Shin. "Zero-Shot Tabular Learning via Hypergraph Reasoning with LLMs". *EMNLP 2026: Conference on Empirical Methods in Natural Language Processing 2026*. DOI: <https://doi.org/10.18653/2026.emnlp-main.1822>.
- Yeongho Kim, Yeonje Choi, and Kijung Shin. "TaLK: Text-Attributed Graph Dataset Distillation via Coupling Language Model with Graph-Aware Kernel". *EMNLP 2026 (Findings Paper): Conference on Empirical Methods in Natural Language Processing 2026*.
- Kyungho Kim, Sunwoo Kim, Geon Lee, Shinhwan Kang, Sojeong Kim, Liam Collins, Bhuvesh Kumar, Donald Loveland, and Kijung Shin. "Training-Free LLM-Based Recommendation with Post-LLM Item Refinement Using Collaborative Signals". *CIKM 2026 (Short Paper): ACM Conference on Information and Knowledge Management 2026*.
- Shinhwan Kang, Soo Yong Lee, Jaewon Kim, Kijung Shin, and Buru Chang. "Improving Rare Medication Recommendation with Counterfactual Data Augmentation and Large Language Models". *RecSys 2026: ACM Conference on Recommender Systems 2026*. DOI: <https://doi.org/10.1145/3773078.3831753>.
- Heechan Moon and Kijung Shin. "SLeDGe: Semi-Supervised Learning on Data Streams with Graph Structure Learning". *ECML-PKDD 2026: European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases 2026*.
- Geon Lee\*, Fanchen Bu\*, Soo Yong Lee\*, Sunwoo Kim, and Kijung Shin. "Toward a Science of AI Agent Societies". *KDD 2026 (Blue Sky Ideas Track): ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2026*. DOI: <https://doi.org/10.1145/3770855.3818651>.
- Geon Lee, Sunwoo Kim, Kyungho Kim, and Kijung Shin. "Rethinking Contrastive Learning for Graph Collaborative Filtering: Limitations and A Simple Remedy". *ICML 2026: International Conference on Machine Learning 2026*.
- Kyungho Kim\*, Yeonje Choi\*, Gyurim Hwang, Sejin Chung, Hongseok Lee, Myeong Ho Song, Yeongho Kim, Sunwoo Kim, Jongha Lee, Juyeon Kim, and Kijung Shin. "Pre-Deployment Advertisement Ranking under Data Scarcity via Context-Aware Criteria Generation with VLMs". *ACL 2026 (Industry Track): Annual Meeting of the Association for Computational Linguistics 2026*. DOI: <https://doi.org/10.18653/v1/2026.acl-industry.28>.
- Juyeon Kim, Geon Lee, Dongwon Choi, Taeuk Kim, and Kijung Shin. "Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy". *ACL 2026 (Findings Paper): Annual Meeting of the Association for Computational Linguistics 2026*. DOI: <https://doi.org/10.18653/v1/2026.findings-acl.54>.
- Sunwoo Kim, Geon Lee, Kyungho Kim, Jaemin Yoo, and Kijung Shin. "ItemRAG: Item-Based Retrieval-Augmented Generation for LLM-Based Recommendation". *SIGIR 2026 (Short Paper): International ACM SIGIR Conference on Research and Development in Information Retrieval 2026*. DOI: <https://doi.org/10.1145/3805712.3809942>.
- Jeeho Shin, Kyungho Kim, and Kijung Shin. "From Raw Features to Effective Embeddings: A Three-Stage Approach for Multimodal Recipe Recommendation". *SIGIR 2026 (Short Paper): International ACM SIGIR Conference on Research and Development in Information Retrieval 2026*. DOI: <https://doi.org/10.1145/3805712.3809863>.
- Taehyung Kwon\*, Yeonje Choi\*, Yeongho Kim, and Kijung Shin. "Effective Dataset Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression". *ICDE 2026: IEEE International Conference on Data Engineering 2026*.
- Sunwoo Kim, Hyunjin Hwang, and Kijung Shin. "Personalized Parameter-Efficient Fine-Tuning of Foundation Models for Multimodal Recommendation". *WWW 2026: The Web Conference 2026*. DOI: <https://doi.org/10.1145/3774904.3792248>.
- Kyungho Kim, Geon Lee, Juyeon Kim, Dongwon Choi, Shinhwan Kang, and Kijung Shin. "ReFuGe: Feature Generation for Prediction Tasks on Relational Databases with LLM Agents". *WWW 2026 (Short Paper): The Web Conference 2026*.
- Sunwoo Kim, Soo Yong Lee, Kyungho Kim, Hyunjin Hwang, Jaemin Yoo, and Kijung Shin. "Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption". *AAAI 2026: AAAI Conference on Artificial Intelligence 2026*.
- Geon Lee, Bhuvesh Kumar, Mingxuan Ju, Tong Zhao, Kijung Shin, Neil Shah, and Liam Collins. "Sequential Data Augmentation for Generative Recommendation". *WSDM 2026: ACM International Conference on Web Search and Data Mining 2026*.
- Jawan Chun\*, Fanchen Bu\*, Yeongho Kim, Atsushi Miyauchi, Francesco Bonchi, and Kijung Shin. "A Survey on Centrality and Importance Measures in Hypergraphs: Categorization and Empirical Insights". *ACM Computing Surveys*. DOI: <https://doi.org/10.1145/3843227>.
- Jaewan Chun, Seokbum Yoon, Minyoung Choe, Geon Lee, and Kijung Shin. "From Binary to General Attributes: Attributed Hypergraph Generation with Realistic Interplay Between Structure and Attributes". *Knowledge and Information Systems*. DOI: <https://doi.org/10.1007/s10115-026-02850-x>.
- Heechan Moon\*, Hyunju Kim\*, Sunwoo Kim, and Kijung Shin. "Four-Set Hypergraphlets for Characterization of Directed Hypergraphs". *IEEE Transactions on Knowledge and Data Engineering*. DOI: <https://doi.org/10.1109/tkde.2026.3677137>.
- Kyungho Kim, Sunwoo Kim, Geon Lee, Jinhong Jung, and Kijung Shin. "A Comprehensive Survey on Multi-Behavior Recommender Systems: Extended Taxonomy and Recent Advances". *International Journal of Data Science and Analytics*.
- Geon Lee, Kyungho Kim, Fanchen Bu, Langzhang Liang, and Kijung Shin. "Revisiting LightGCN: Unexpected Inflexibility, Inconsistency, and A Remedy Towards Improved Recommendation". *ACM TORS: ACM Transactions on Recommender Systems*. DOI: <https://doi.org/10.1145/3760763>.

**2025**

- Dongwon Choi, Sunwoo Kim, Juyeon Kim, Kyungho Kim, Geon Lee, Shinhwan Kang, Myunghwan Kim, and Kijung Shin. "RDB2G-Bench: A Comprehensive Benchmark for Automatic Graph Modeling of Relational Databases". *NeurIPS 2025 (Benchmark Track): Annual Conference on Neural Information Processing Systems 2025*. DOI: <https://doi.org/10.52202/085713-4078>.
- Sunwoo Kim, Hyunjin Hwang, and Kijung Shin. "Learning to Flow from Generative Pretext Tasks for Neural Architecture Encoding". *NeurIPS 2025: Annual Conference on Neural Information Processing Systems 2025*. DOI: <https://doi.org/10.52202/085713-3641>.
- Yushan Jiang, Wenchao Yu, Geon Lee, Dongjin Song, Kijung Shin, Wei Cheng, Yanchi Liu, and Haifeng Chen. "TimeXL: Explainable Multi-modal Time Series Prediction with LLM-in-the-Loop". *NeurIPS 2025: Annual Conference on Neural Information Processing Systems 2025*.
- Fanchen Bu, Ruochen Yang, Paul Bogdan, and Kijung Shin. "Edge Probability Graph Models Beyond Edge Independency: Concepts, Analyses, and Algorithms". *ICDM 2025: IEEE International Conference on Data Mining 2025*.
- Hyunjin Choo, Fanchen Bu, Hyunjin Hwang, Young-Gyu Yoon, and Kijung Shin. "HyperSearch: Prediction of New Hyperedges through Unconstrained yet Efficient Search". *ICDM 2025: IEEE International Conference on Data Mining 2025*.
- Jaewan Chun\*, Seokbum Yoon\*, Minyoung Choe, Geon Lee, and Kijung Shin. "Attributed Hypergraph Generation with Realistic Interplay Between Structure and Attributes". *ICDM 2025: IEEE International Conference on Data Mining 2025*.
- Fanchen Bu, Geon Lee, Minyoung Choe, and Kijung Shin. "Identifying Group Anchors in Real-World Group Interactions Under Label Scarcity". *ICDM 2025: IEEE International Conference on Data Mining 2025*. DOI: <https://doi.org/10.1109/icdm65498.2025.00116>.
- Sunwoo Kim, Soo Yong Lee, Jaemin Yoo, and Kijung Shin. "'Hello, World!': Making GNNs Talk with LLMs". *EMNLP 2025 (Findings, Short Paper): Conference on Empirical Methods in Natural Language Processing 2025*. DOI: <https://doi.org/10.18653/v1/2025.findings-emnlp.555>.
- Kyungho Kim, Sunwoo Kim, Geon Lee, and Kijung Shin. "A Self-Supervised Mixture-of-Experts Framework for Multi-behavior Recommendation". *CIKM 2025: ACM Conference on Information and Knowledge Management 2025*. DOI: <https://doi.org/10.1145/3746252.3761286>.
- Minyoung Choe\*, Geon Lee\*, Changhun Han\*, Suji Kim, Woong Hu, Hyebeen Hwang, Geunseok Park, Byeongyeon Kim, Hyesook Lee, Ha-Myung Park, and Kijung Shin. "SkySearch: Satellite Video Search at Scale". *KDD 2025 (Industry Track): ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2025*. DOI: <https://doi.org/10.1145/3711896.3737263>.
- Federico Berto\*, Chuanbo Hua\*, Junyoung Park\*, Laurin Luttmann\*, Yining Ma, Fanchen Bu, Jiarui Wang, Haoran Ye, Minsu Kim, Sanghyeok Choi, Zepeda Gast, Andre Hottung, Jianan Zhou, Jieyi Bi, Yu Hu, Fei Liu, Hyeonah Kim, Jiwoo Son, Haeyeon Kim, Davide Angioni, Wouter Kool, Zhiguang Cao, Jie Zhang, Kijung Shin, Cathy Wu, Sungsoo Ahn, Guojie Song, Changhyun Kwon, Lin Xie, and Jinkyoo Park. "RL4CO: An Extensive Reinforcement Learning for Combinatorial Optimization Benchmark". *KDD 2025 (Benchmark Track): ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2025*. DOI: <https://doi.org/10.1145/3711896.3737433>.
- Hyeonsoo Jo\*, Hyunjin Hwang\*, Fanchen Bu, Soo Yong Lee, Chanyoung Park,  and Kijung Shin. "On Measuring Unnoticeability of Graph Adversarial Attacks: Observations, New Measure, and Applications". *KDD 2025: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2025*. DOI: <https://doi.org/10.1145/3690624.3709163>.
- Langzhang Liang, Fanchen Bu, Zixing Song, Zenglin Xu, Shirui Pan, and Kijung Shin. "Mitigating Over-Squashing in Graph Neural Networks by Spectrum-Preserving Sparsification". *ICML 2025: International Conference on Machine Learning 2025*.
- Juyeon Kim, Geon Lee, Taeuk Kim,  and Kijung Shin. "KGMEL: Knowledge Graph-Enhanced Multimodal Entity Linking". *SIGIR 2025 (Short Paper): International ACM SIGIR Conference on Research and Development in Information Retrieval 2025*. DOI: <https://doi.org/10.1145/3726302.3730217>.
- Kyuhan Lee, Geon Lee, and Kijung Shin. "MARIOH: Multiplicity-Aware Hypergraph Reconstruction". *ICDE 2025: IEEE International Conference on Data Engineering 2025*. DOI: <https://doi.org/10.1109/icde65448.2025.00233>.
- Jongha Lee, Taehyung Kwon, Heechan Moon, and Kijung Shin. "Simple yet Effective Node Property Prediction on Edge Streams under Distribution Shifts". *ICDE 2025: IEEE International Conference on Data Engineering 2025*. DOI: <https://doi.org/10.1109/icde65448.2025.00190>.
- Kyungho Kim, Sunwoo Kim, Geon Lee, Jinhong Jung, and Kijung Shin. "Multi-Behavior Recommender Systems: A Survey". *PAKDD 2025 (Survey Paper): Pacific-Asia Conference on Knowledge Discovery and Data Mining 2025*. DOI: <https://doi.org/10.1007/978-981-96-8183-9_31>.
- Hyeonsoo Jo, Jongha Lee, Fanchen Bu, and Kijung Shin. "TiGer: Self-Supervised Purification for Time-evolving Graphs". *PAKDD 2025: Pacific-Asia Conference on Knowledge Discovery and Data Mining 2025*. DOI: <https://doi.org/10.1007/978-981-96-8173-0_16>.
- Minyoung Choe, Jihoon Ko, Taehyung Kwon, Kijung Shin, and Christos Faloutsos. "Kronecker Generative Models for Power-Law Patterns in Real-World Hypergraphs". *WWW 2025: The Web Conference 2025*. DOI: <https://doi.org/10.1145/3696410.3714893>.
- Yeongho Kim, Yuyeong Kim, Geon Lee,  and Kijung Shin. "Beyond Neighbors: Distance-Generalized Graphlets for Enhanced Graph Characterization". *WWW 2025: The Web Conference 2025*. DOI: <https://doi.org/10.1145/3696410.3714558>.
- Junghun Lee, Hyunju Kim, Fanchen Bu, Jihoon Ko,  and Kijung Shin. "DiffIM: Differentiable Influence Minimization with Surrogate Modeling and Continuous Relaxation". *AAAI 2025: AAAI Conference on Artificial Intelligence 2025*. DOI: <https://doi.org/10.1609/aaai.v39i17.33994>.
- Geon Lee,  Wenchao Yu, Kijung Shin, Wei Cheng, and Haifeng Chen. "TimeCAP: Learning to Contextualize, Augment, and Predict Time Series Events with Large Language Model Agents". *AAAI 2025: AAAI Conference on Artificial Intelligence 2025*. DOI: <https://doi.org/10.1609/aaai.v39i17.33989>.
- Hyunjin Choo, Minho Eom, Gyuri Kim, Young-Gyu Yoon,  and Kijung Shin. "RASP: Robust Mining of Frequent Temporal Sequential Patterns under Temporal Variations". *EDBT 2025: International Conference on Extending Database Technology 2025*.
- Jihoon Ko\*, Seojeong Kim\*, Kyuhan Lee, Shinhwan Kang, Dongyeong Hwang, Kijung Shin, and Noseong Park. "Inductive Influence Estimation and Maximization over Unseen Social Networks under Two Diffusion Models". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-025-01137-z>.
- Tae Hyun Kim\*, Harim Kim\*, Hyunjin Hwang\*, Shinwhan Kang\*, Kijung Shin, and Inhwa Baek. "Gene Expression Inference Based on Graph Neural Networks Using L1000 Data". *Briefings in Bioinformatics*. DOI: <https://doi.org/10.1093/bib/bbaf273>.
- Jihoon Ko, Taehyung Kwon, Jinhong Jung, and Kijung Shin. "Effective and Lightweight Lossy Compression of Tensors: Techniques and Applications". *Knowledge and Information Systems*. DOI: <https://doi.org/10.1007/s10115-025-02471-w>.
- Geon Lee\*, Fanchen Bu\*, Tina Eliassi-Rad, and Kijung Shin. "A Survey on Hypergraph Mining: Patterns, Tools, and Generators". *ACM Computing Surveys*. DOI: <https://doi.org/10.1145/3719002>.
- Hyunju Kim\*, Heechan Moon\*, Fanchen Bu, Jihoon Ko, and Kijung Shin. "Estimating Simplet Counts via Sampling". *The VLDB Journal*. DOI: <https://doi.org/10.1007/s00778-024-00890-9>.
- Jihoon Ko\*, Shinhwan Kang\*, Taehyung Kwon, Heechan Moon, and Kijung Shin. "BeGin: Extensive Benchmark Scenarios and An Easy-to-use Framework for Graph Continual Learning". *ACM TIST: ACM Transactions on Intelligent Systems and Technology*. DOI: <https://doi.org/10.1145/3702648>.
- Taehyung Kwon, Jihoon Ko, Jinhong Jung, Jun-Gi Jang, and Kijung Shin. "Compact Lossy Compression of Tensors via Neural Tensor-Train Decomposition". *Knowledge and Information Systems*. DOI: <https://doi.org/10.1007/s10115-024-02252-x>.
- Fanchen Bu and Kijung Shin. "On Training-Test (Mis)alignment in Unsupervised Combinatorial Optimization: Observation, Empirical Exploration, and Analysis". *PUT 2025: Workshop on Test-Time Adaptation: Putting Updates to the Test! 2025*.

**2024**

- Sunwoo Kim, Soo Yong Lee, Fanchen Bu, Shinhwan Kang, Kyungho Kim, Jaemin Yoo, and Kijung Shin. "Rethinking Reconstruction-based Graph-Level Anomaly Detection: Limitations and a Simple Remedy". *NeurIPS 2024: Annual Conference on Neural Information Processing Systems 2024*. DOI: <https://doi.org/10.52202/079017-3040>.
- Jihoon Ko, Taehyung Kwon, Jinhong Jung, and Kijung Shin. "ELiCiT: Effective and Lightweight Lossy Compression of Tensors". *ICDM 2024: IEEE International Conference on Data Mining 2024*. DOI: <https://doi.org/10.1109/icdm59182.2024.00024>.
- Ulugbek Ergashev, Geon Lee, Kijung Shin, Eduard Dragut, and Weiyi Meng. "Resource2Box: Learning To Rank Resources in Distributed Search Using Box Embedding". *ICDM 2024: IEEE International Conference on Data Mining 2024*.
- Geon Lee, Kyungho Kim, and Kijung Shin. "Revisiting LightGCN: Unexpected Inflexibility, Inconsistency, and A Remedy Towards Improved Recommendation". *RecSys 2024 (Short Paper): ACM Conference on Recommender Systems 2024*. DOI: <https://doi.org/10.1145/3640457.3688176>.
- Kyungho Kim, Sunwoo Kim, Geon Lee, and Kijung Shin. "Towards Better Utilization of Multiple Views for Bundle Recommendation". *CIKM 2024 (Short Paper): ACM Conference on Information and Knowledge Management 2024*. DOI: <https://doi.org/10.1145/3627673.3680003>.
- Geon Lee, Kyungho Kim, and Kijung Shin. "Post-Training Embedding Enhancement for Long-Tail Recommendation". *CIKM 2024 (Short Paper): ACM Conference on Information and Knowledge Management 2024*. DOI: <https://doi.org/10.1145/3627673.3679978>.
- Sunwoo Kim\*, Soo Yong Lee\*, Yue Gao, Alessia Antelmi, Mirko Polato, and Kijung Shin. "A Survey on Hypergraph Neural Networks: An In-Depth and Step-By-Step Guide". *KDD 2024 (Survey Paper): ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2024*. DOI: <https://doi.org/10.1145/3637528.3671457>.
- Taehyung Kwon, Jihoon Ko, Jinhong Jung, Jun-Gi Jang, and Kijung Shin. "Compact Decomposition of Irregular Tensors for Data Compression: From Sparse to Dense to High-Order Tensors". *KDD 2024: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2024*. DOI: <https://doi.org/10.1145/3637528.3671846>.
- Jongha Lee, Sunwoo Kim, and Kijung Shin. "SLADE: Detecting Dynamic Anomalies in Edge Streams without Labels via Self-Supervised Learning". *KDD 2024: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2024*. DOI: <https://doi.org/10.1145/3637528.3671845>.
- Manh Tuan Do and Kijung Shin. "Unsupervised Alignment of Hypergraphs with Different Scales". *KDD 2024: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2024*. DOI: <https://doi.org/10.1145/3637528.3671955>.
- Fanchen Bu, Hyeonsoo Jo, Soo Yong Lee, Sungsoo Ahn, and Kijung Shin. "Tackling Prevalent Conditions in Unsupervised Combinatorial Optimization: Cardinality, Minimum, Covering, and More". *ICML 2024: International Conference on Machine Learning 2024*.
- Soo Yong Lee, Sunwoo Kim, Fanchen Bu, Jaemin Yoo, Jiliang Tang, and Kijung Shin. "Feature Distribution on Graph Topology Mediates the Effect of Graph Convolution: Homophily Perspective". *ICML 2024: International Conference on Machine Learning 2024*.
- Langzhang Liang, Sunwoo Kim, Kijung Shin, Zenglin Xu, Shirui Pan, and Yuan Qi. "Sign is Not a Remedy: Multiset-to-Multiset Message Passing for Learning on Heterophilic Graphs". *ICML 2024: International Conference on Machine Learning 2024*.
- Dongyeong Hwang, Hyunju Kim, Sunwoo Kim, and Kijung Shin. "FlowerFormer: Empowering Neural Architecture Encoding using a Flow-aware Graph Transformer". *CVPR 2024: IEEE/CVF Computer Vision and Pattern Recognition Conference 2024*. DOI: <https://doi.org/10.1109/cvpr52733.2024.00586>.
- Geon Lee, Soo Yong Lee, and Kijung Shin. "VilLain: Self-Supervised Learning on Homogeneous Hypergraphs without Features via Virtual Label Propagation". *WWW 2024: The Web Conference 2024*. DOI: <https://doi.org/10.1145/3589334.3645454>.
- Yeonjun In, Kanghoon Yoon, Kibum Kim, Kijung Shin, and Chanyoung Park. "Self-Guided Robust Graph Structure Refinement". *WWW 2024: The Web Conference 2024*. DOI: <https://doi.org/10.1145/3589334.3645522>.
- Sunwoo Kim, Shinhwan Kang, Fanchen Bu, Soo Yong Lee, Jaemin Yoo, and Kijung Shin. "HypeBoy: Generative Self-Supervised Representation Learning on Hypergraphs". *ICLR 2024: International Conference on Learning Representations 2024*.
- Dongjin Lee, Juho Lee, and Kijung Shin. "Spear and Shield: Adversarial Attacks and Defense Methods for Model-Based Link Prediction on Continuous-Time Dynamic Graphs". *AAAI 2024: AAAI Conference on Artificial Intelligence 2024*. DOI: <https://doi.org/10.1609/aaai.v38i12.29239>.
- Taeri Kim, Jiho Heo, Hongil Kim, Kijung Shin, and Sang-Wook Kim. "VITA: 'Carefully Chosen and Weighted Less' Is Better in Medication Recommendation". *AAAI 2024: AAAI Conference on Artificial Intelligence 2024*. DOI: <https://doi.org/10.1609/aaai.v38i8.28704>.
- Minyoung Choe, Jaemin Yoo, Geon Lee, Woonsung Baek, U Kang, and Kijung Shin. "Representative and Back-In-Time Sampling from Real-world Hypergraphs". *ACM TKDD: ACM Transactions on Knowledge Discovery from Data*. DOI: <https://doi.org/10.1145/3653306>.
- Seok-Geun Oh, Seok-Woo Son, Young-Ha Kim, Chanil Park , Jihoon Ko, Kijung Shin, Ji-Hoon Ha, and Hyesook Lee. "Deep Learning Model for Heavy Rainfall Nowcasting in South Korea". *Weather and Climate Extremes*. DOI: <https://doi.org/10.1016/j.wace.2024.100652>.
- Jaewan Chun, Geon Lee, Kijung Shin, and Jinhong Jung. "Random Walk with Restart on Hypergraphs: Fast Computation and an Application to Anomaly Detection". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00995-9>.
- Geon Lee\*, Seokbum Yoon\*, Jihoon Ko, Hyunju Kim, and Kijung Shin. "Hypergraph Motifs and Their Extensions Beyond Binary". *The VLDB Journal*. DOI: <https://doi.org/10.1007/s00778-023-00827-8>.
- Taehyung Yu, Soo Yong Lee, Hyunjin Hwang, and Kijung Shin. "Prediction Is NOT Classification: On Formulation and Evaluation of Hyperedge Prediction". *HDM 2024: Workshop on High Dimensional Data Mining*. DOI: <https://doi.org/10.1109/icdmw65004.2024.00051>.
- Deukryeol Yoon, Dongjin Lee, Minyoung Choe, and Kijung Shin. "Graphlets over Time: A New Lens for Temporal Network Analysis". *MLH 2024: Workshop on Mining and Learning Real-world Dynamics via High-order Networks*. DOI: <https://doi.org/10.1007/978-3-032-25314-9_13>.

**2023**

- Taehyung Kwon, Jihoon Ko, Jinhong Jung, and Kijung Shin. "TensorCodec: Compact Lossy Compression of Tensors without Strong Data Assumptions". *ICDM 2023: IEEE International Conference on Data Mining 2023*. DOI: <https://doi.org/10.1109/icdm58522.2023.00032>.
- Hyeonsoo Jo, Fanchen Bu, and Kijung Shin. "Robust Graph Clustering via Meta Weighting for Noisy Graphs". *CIKM 2023: ACM International Conference on Information and Knowledge Management 2023*. DOI: <https://doi.org/10.1145/3583780.3615038>.
- Soo Yong Lee\*, Juwon Kim\*, Kiwoong Park, Dongkuk Ryu, Sangheun Shim, and Kijung Shin. "You’re Not Alone in Battle: Combat Threat Analysis Using Attention Networks and a New Open Benchmark". *CIKM 2023 (Short Paper): ACM International Conference on Information and Knowledge Management 2023*. DOI: <https://doi.org/10.1145/3583780.3615196>.
- Sunwoo Kim, Fanchen Bu, Minyoung Choe, Jaemin Yoo, and Kijung Shin. "How Transitive Are Real-World Group Interactions? - Measurement and Reproduction". *KDD 2023: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2023*. DOI: <https://doi.org/10.1145/3580305.3599382>.
- Fanchen Bu and Kijung Shin. "On Improving the Cohesiveness of Graphs by Merging Nodes: Formulation, Analysis, and Algorithm". *KDD 2023: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2023*.
- Minyoung Choe, Sunwoo Kim, Jaemin Yoo, and Kijung Shin. "Classification of Edge-dependent Labels of Nodes in Hypergraphs". *KDD 2023: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 2023*. DOI: <https://doi.org/10.1145/3580305.3599274>.
- Soo Yong Lee, Fanchen Bu, Jaemin Yoo, and Kijung Shin. "Towards Deep Attention in Graph Neural Networks: Problems and Remedies". *ICML 2023: International Conference on Machine Learning 2023*.
- Taehyung Kwon\*, Jihoon Ko\*, Jinhong Jung, and Kijung Shin. "NeuKron: Constant-Size Lossy Compression of Sparse Reorderable Matrices and Tensors". *WWW 2023: The Web Conference 2023*. DOI: <https://doi.org/10.1145/3543507.3583226>.
- Hyunju Kim, Jihoon Ko, Fanchen Bu, and Kijung Shin. "Characterization of Simplicial Complexes Using Simplets Beyond Four Nodes". *WWW 2023: The Web Conference 2023*.
- Hyunsik Yoo, Yeon-Chang Lee, Kijung Shin, and Sang-Wook Kim. "Disentangling Degree-related Biases and Interest for Out-of-Distribution Generalized Directed Network Embedding". *WWW 2023: The Web Conference 2023*. DOI: <https://doi.org/10.1145/3543507.3583271>.
- Dongjin Lee and Kijung Shin. "I'm Me, We're Us, and I'm Us: Tridirectional Contrastive Learning on Hypergraphs". *AAAI 2023: AAAI Conference on Artificial Intelligence 2023*. DOI: <https://doi.org/10.1609/aaai.v37i7.26019>.
- Junmo Cho\*, Seungjae Han\*, Eun-Seo Cho, Kijung Shin, and Young-Gyu Yoon. "Robust and Efficient Alignment of Calcium Imaging Data through Simultaneous Low Rank and Sparse Decomposition". *WACV 2023: IEEE/CVF Winter Conference on Applications of Computer Vision 2023*. DOI: <https://doi.org/10.1109/wacv56688.2023.00198>.
- Sunwoo Kim, Minyoung Choe, Jaemin Yoo, and Kijung Shin. "Reciprocity in Directed Hypergraphs: Measures, Findings, and Generators". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00955-3>.
- Sunwoo Kim\*, Dongjin Lee\*, Yul Kim, Jungho Park, Taeho Hwang, and Kijung Shin. "Datasets, Tasks, and Training Methods for Large-Scale Hypergraph Learning". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00952-6>.
- Manh Tuan Do and Kijung Shin. "Improving the Core Resilience of Real-world Hypergraphs". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00958-0>.
- Fanchen Bu, Geon Lee, and Kijung Shin. "Hypercore Decomposition for Non-Fragile Hyperedges: Concepts, Algorithms, Observations, and Applications". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00956-2>.
- Fanchen Bu, Shinhwan Kang, and Kijung Shin. "Interplay between Topology and Edge Weights in Real-World Graphs: Concepts, Patterns, and an Algorithm". *Data Mining and Knowledge Discovery*. DOI: <https://doi.org/10.1007/s10618-023-00940-w>.
- Geon Lee and Kijung Shin. "Temporal Hypergraph Motifs". *Knowledge and Information Systems*. DOI: <https://doi.org/10.1007/s10115-023-01837-2>.
- Seok-Geun Oh , Chanil Park, Seok-Woo Son, Jihoon Ko, Kijung Shin, Sunyoung Kim, and Junsang Park. "Evaluation of Deep-Learning-Based Very Short-Term Rainfall Forecasts in South Korea". *Asia-Pacific Journal of Atmospheric Sciences*. DOI: <https://doi.org/10.1007/s13143-022-00310-4>.
- Manh Tuan Do, Noseng Park, and Kijung Shin. "Two-Stage Training of Graph Neural Networks for Graph Classification". *Neural Processing Letters*. DOI: <https://doi.org/10.1007/s11063-022-10985-5>.

**2022**

- Sunwoo Kim, Minyoung Choe, Jaemin Yoo, and Kijung Shin. "Reciprocity in Directed Hypergraphs: Measures, Findings, and Generators". *ICDM 2022: IEEE International Conference on Data Mining 2022*. DOI: <https://doi.org/10.1109/icdm54844.2022.00122>.
- Geon Lee, Chanyoung Park, and Kijung Shin. "Set2Box: Similarity Preserving Representation Learning for Sets". *ICDM 2022: IEEE International Conference on Data Mining 2022*. DOI: <https://doi.org/10.1109/icdm54844.2022.00125>.
- Taeri Kim\*, Yeon-Chang Lee\*, Kijung Shin, and Sang-Wook Kim. "MARIO: Modality-Aware Attention and Modality-Preserving Decoders for Multimedia Recommendation". *CIKM 2022: ACM International Conference on Information and Knowledge Management 2022*.
- Geon Lee, Minyoung Choe, and Kijung Shin. "HashNWalk: Hash and Random Walk Based Anomaly Detection in Hyperedge Streams". *IJCAI 2022: International Joint Conference on Artificial Intelligence 2022*. DOI: <https://doi.org/10.24963/ijcai.2022/296>.
- Hyunjin Hwang\*, Seungwoo Lee\*, Chanyoung Park, and Kijung Shin. "AHP: Learning to Negative Sample for Hyperedge Prediction". *SIGIR 2022 (Short Paper): International ACM SIGIR Conference on Research and Development in Information Retrieval 2022*.
- Shinhwan Kang, Kyuhan Lee, and Kijung Shin. "Are Edge Weights in Summary Graphs Useful? - A Comparative Study". *PAKDD 2022: Pacific-Asia Conference on Knowledge Discovery and Data Mining 2022*. DOI: <https://doi.org/10.1007/978-3-031-05933-9_5>.
- Shinhwan Kang, Kyuhan Lee, and Kijung Shin. "Personalized Graph Summarization: Formulation, Scalable Algorithms, and Applications". *ICDE 2022: IEEE International Conference on Data Engineering 2022*. DOI: <https://doi.org/10.1109/icde53745.2022.00219>.
- Kyuhan Lee\*, Jihoon Ko\*, and Kijung Shin. "SLUGGER: Lossless Hierarchical Summarization of Massive Graphs". *ICDE 2022: IEEE International Conference on Data Engineering 2022*. DOI: <https://doi.org/10.1109/icde53745.2022.00040>.
- Minyoung Choe, Jaemin Yoo, Geon Lee, Woonsung Baek, U Kang, and Kijung Shin. "MiDaS: Representative Sampling from Real-world Hypergraphs". *WWW 2022: The Web Conference 2022*. DOI: <https://doi.org/10.1145/3485447.3512157>.
- Hyunjin Choo and Kijung Shin. "On the Persistence of Higher-Order Interactions in Real-World Hypergraphs". *SDM 2022: SIAM International Conference on Data Mining 2022*. DOI: <https://doi.org/10.1137/1.9781611977172.19>.
- Minseok Kim, Hwanjun Song, Yooju Shin, Dongmin Park, Kijung Shin, and Jae-Gil Lee. "Meta-Learning for Online Update of Recommender Systems". *AAAI 2022: AAAI Conference on Artificial Intelligence 2022*. DOI: <https://doi.org/10.1609/aaai.v36i4.20324>.
- Hyeonjeong Shin, Taehyung Kwon, Neil Shah, and Kijung Shin. "Finding a Concise, Precise, and Exhaustive Set of Near Bi-Cliques in Dynamic Graphs". *WSDM 2022: ACM International Conference on Web Search and Data Mining 2022*. DOI: <https://doi.org/10.1145/3488560.3498390>.
- Hyunsik Yoo\*, Yeon-Chang Lee\*, Kijung Shin, and Sang-Wook Kim. "Directed Network Embedding with Virtual Negative Edges". *WSDM 2022: ACM International Conference on Web Search and Data Mining 2022*. DOI: <https://doi.org/10.1145/3488560.3498470>.
- Jihoon Ko\*, Yunbum Kook\*, and Kijung Shin. "Growth Patterns and Models of Real-world Hypergraphs". *Knowledge and Information Systems*. DOI: <https://doi.org/10.1007/s10115-022-01739-9>.
- Jihoon Ko\*, Kyuhan Lee\*, Hyunjin Hwang\*, Seok-Geun Oh, Seok-Woo Son, and Kijung Shin. "Effective Training Strategies for Deep Learning-Based Precipitation Nowcasting and Estimation". *Computers and Geosciences*. DOI: <https://doi.org/10.1016/j.cageo.2022.105072>.
- Geon Lee, Se-eun Yoon, and Kijung Shin. "Simple Epidemic Models with Segmentation Can Be Better than Complex Ones". *PLOS ONE*. DOI: <https://doi.org/10.1371/journal.pone.0262244>.
- Siddharth Bhatia, Rui Liu, Bryan Hooi, Minji Yoon, Kijung Shin, and Christos Faloutsos. "Real-Time Anomaly Detection in Edge Streams". *ACM TKDD: ACM Transactions on Knowledge Discovery from Data*. DOI: <https://doi.org/10.1145/3494564>.
- Jihoon Ko\*, Kyuhan Lee\*, Hyunjin Hwang, and Kijung Shin. "Deep-Learning-Based Precipitation Nowcasting with Ground Weather Station Data and Radar Data". *SSTDM 2022: International Workshop on Spatial and Spatiotemporal Data Mining*. DOI: <https://doi.org/10.1109/icdmw58026.2022.00138>.

**2021**

- Geon Lee and Kijung Shin. "THyMe+: Temporal Hypergraph Motifs and Fast Algorithms for Exact Counting". *ICDM 2021: IEEE International Conference on Data Mining 2021*. DOI: <https://doi.org/10.1109/icdm51629.2021.00042>.

## 수상과 선정

첫 화면 소식과 Publications 페이지의 수상·선정 표기를 옮겼다. 연월은 소식의 게시 연월이다. 연도만 있는 항목은 논문 옆에 적힌 학회 연도이고 개별 날짜는 게시되어 있지 않다.[^home][^pubs]

- 2026-02 · Geon: KAIST 공과대학 Ph.D. Dissertation Award 수상
- 2025-11 · Jaewan, Seokbeom, Minyoung, Geon: IEEE ICDM Best Paper Award 수상
- 2025-06 · Kyungho, Sunwoo, Geon: PAKDD 2025 Best Survey Paper Award 수상
- 2024-12 · Fanchen, Geon, Jihoon, Soo Yong, Sunwoo: KDD 2025 outstanding reviewers 선정
- 2024-09 · Soo Yong: KDD 2024 top reviewer 선정
- 2023-12 · Taehyung, Jihoon: IEEE ICDM Best Student Paper Runner-up Award 수상
- 2025 · Edge Probability Graph Models Beyond Edge Independency: Concepts, Analyses, and Algorithms: ICDM 2025 우수 논문의 학술지 신속 심사 초청 대상 선정
- 2025 · Attributed Hypergraph Generation with Realistic Interplay Between Structure and Attributes: ICDM 2025 우수 논문의 학술지 신속 심사 초청 대상 선정
- 2025 · A Comprehensive Survey on Multi-Behavior Recommender Systems: Extended Taxonomy and Recent Advances: PAKDD 2025 우수 논문으로 학술지 초청
- 2024 · ELiCiT: Effective and Lightweight Lossy Compression of Tensors: ICDM 2024 우수 논문의 학술지 신속 심사 초청 대상 선정
- 2024 · Revisiting LightGCN: Unexpected Inflexibility, Inconsistency, and A Remedy Towards Improved Recommendation: ACM RecSys 2024 우수 단편 논문 후보 선정 및 우수 논문 학술지 초청
- 2024 · VITA: 'Carefully Chosen and Weighted Less' Is Better in Medication Recommendation: AAAI 2024 구두 발표 선정
- 2023 · TensorCodec: Compact Lossy Compression of Tensors without Strong Data Assumptions: ICDM 2023 우수 논문의 학술지 신속 심사 초청 대상 선정

## 연락과 위치

- 연구실: 서울특별시 동대문구 회기로 85, KAIST 9호관 9503호, 우편번호 02455[^contact]
- 전화: +82-2-958-3915[^contact]
- 교수 사무실: 9호관 9503호[^dept]
- 교수 업무 이메일: kijungs@kaist.ac.kr[^dept]
[^home]: Data Mining Lab, 첫 화면 News & Notices·Research Highlights. <https://sites.google.com/view/kaistdata> (관측 2026-11-09).
[^team]: Data Mining Lab, Team. <https://sites.google.com/view/kaistdata/team> (관측 2026-11-09).
[^pubs]: Data Mining Lab, Publications의 Tutorials·Publications. <https://sites.google.com/view/kaistdata/publications> (관측 2026-11-09).
[^dept]: KAIST 김재철AI대학원, 구성원의 전임교수 신기정 소개. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (관측 2026-11-09).
[^pi]: Kijung Shin, About Me·Education·Positions. <https://kijungs.github.io> (관측 2026-11-11).
[^contact]: Data Mining Lab, Contact. <https://sites.google.com/view/kaistdata/contact> (관측 2026-11-11).
[^p1]: G. Lee, F. Bu, T. Eliassi-Rad, K. Shin, ACM Computing Surveys (2025). <https://doi.org/10.1145/3719002> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p2]: S. Kim 외, K. Shin, ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD) (2023). <https://doi.org/10.1145/3580305.3599382> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p3]: D. Lee, K. Shin, Proceedings of the AAAI Conference on Artificial Intelligence (2023). <https://doi.org/10.1609/aaai.v37i7.26019> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p4]: K.-H. Lee, J. Ko, K. Shin, IEEE International Conference on Data Engineering (ICDE) (2022). <https://doi.org/10.1109/icde53745.2022.00040> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p5]: T. Kwon, J. Ko, J. Jung, K. Shin, Proceedings (2023). <https://doi.org/10.1109/icdm58522.2023.00032> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p6]: S. Kim 외, K. Shin, neural information processing systems (2024). <https://doi.org/10.52202/079017-3040> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p7]: S. Kim, H. Hwang, K. Shin, International World Wide Web Conference (WWW) (2026). <https://doi.org/10.1145/3774904.3792248> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).
[^p8]: S. Kim 외, K. Shin, International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR) (2026). <https://doi.org/10.1145/3805712.3809942> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5028609723,publication_year:2021-2026> (관측 2026-11-09).

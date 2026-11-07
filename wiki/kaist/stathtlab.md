# STAT HT LAB

**KAIST 수리과학과 · 전현호 부교수**

- 영문 이름: Hyonho Chun
- 분야: 다변량 통계(여러 관측 특성을 함께 분석하는 통계), 기계학습(자료에서 규칙을 학습하는 계산 방법), 통계적 지노믹스(유전정보 자료를 통계 방법으로 분석하는 분야)[^dept]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 생성 인공지능[^research-gen], 바이오정보학·계산생물학[^research-bio]
- 홈페이지: <https://stathtlab.kaist.ac.kr>
- 근거와 출처: [STAT HT LAB 근거 페이지](stathtlab-sources.md)

> 자료의 구조를 배우고 새 자료를 만드는 모형과, 많은 생물 관측값에서 세포별 특성과 관측 항목 사이의 관계를 밝히는 통계 분석 방법을 연구한다.[^research]

## 무엇을 연구하나

STAT HT LAB은 KAIST 수리과학과 전현호 부교수의 연구실이다. 누리집의 교수 소개는 영문 이름을 Hyonho Chun으로 적고, 연구 소개는 생성 모형(자료가 나오는 규칙을 학습해 새 자료를 만들어 내는 모형), 역문제(관측 결과에서 그 결과를 만든 원인이나 원래 대상을 추정하는 문제), 생물 자료의 통계 분석을 다룬다. 관계망(대상을 점으로, 대상 사이의 관계를 선으로 나타낸 구조)의 모형도 연구한다.[^members][^research] 생성 모형은 자료가 공간 전체에 어떻게 놓이는지를 모형화해 새 자료를 생성한다.[^research]

연구실은 다양한 생성 모형을 연구하고 영상 생성 등의 응용을 찾는 것을 목표로 밝힌다.[^research-gen] 생성 모형은 자료 공간에서 경계를 찾는 분류 모형(자료가 어느 묶음에 속하는지 가르는 모형)과 달리 자료가 공간 전체에 어떻게 놓이는지를 모형화한다. 연구 소개는 잡음(관심 있는 정보에 섞여 관측을 흐트러뜨리는 변동)을 단계적으로 더하는 과정과 제거하는 역과정을 학습하는 확산 모형도 다룬다.[^research]

생물 자료에서는 새로운 분석 모형을 제안한다. 연구실은 개별 세포(생명체의 구조와 기능을 이루는 기본 단위)의 유전자 발현(유전정보가 기능을 하는 산물로 구현되는 과정) 자료를 해석하기 위해 세포가 공유하는 성분과 세포별 성분을 나누는 방법을 개발한다.[^research-bio] 세포별 차이를 압축하면서도 어떤 성분이 결과를 설명하는지 파악하도록 하는 것이 이 방법의 목표다.[^research][^p2]

또 다른 갈래는 여러 생물 자료를 결합해 변수 사이의 의존 관계를 추정하는 연구다. 변수는 대상이나 관측에 따라 값이 달라지는 특성이고, 의존 관계는 한 변수의 값에 따라 다른 변수의 값이 나타날 가능성이 달라지는 관계다. 연구 소개는 추가 정보를 예측 변수로 넣는 관계망 모형과, 여러 관계망을 함께 추정하도록 확장한 연구를 설명한다.[^research]

## 주요 연구 주제

### 생성 모형과 자료의 차원 축소

차원 축소(많은 특성으로 표현한 자료를 적은 수의 특성으로 바꾸는 방법)를 생성 모형과 결합한다. 대표 논문 1은 자료 사이의 유사도 정보를 변분 자동부호화기(관측 자료를 압축된 표현의 확률분포로 바꾸고 그 표현에서 자료를 복원하도록 학습하는 생성 모형, Variational Autoencoder)에 넣는다. 이 논문은 집단 구조가 드러나는 표현을 얻고, 자료의 집단 구조와 함께 달라지는 부가 특성의 영향도 조정한다.[^p1] 대표 논문 2는 공통 성분과 세포별 성분을 나눈 뒤 세포별 성분에 이 모형을 적용해, 비선형 관계(입력과 출력의 관계를 일정한 비례와 합으로 나타낼 수 없는 관계)를 반영한 차원 축소와 세포 유형별 발현 추정을 수행한다.[^p2]

대표 논문 5는 생성한 자료를 목표 자료로 끌어당기고 생성 자료끼리는 밀어내며 학습하는 생성 모형을 이론적으로 분석한다. 학습이 멈췄을 때 목표 분포와 일치하는 조건을 증명하고, 관측 범위 안의 정보만으로 전체 오차를 제어할 수 없는 경우도 제시한다.[^p5]

### 불완전한 관측에서 원래 자료 복원

연구 소개는 잡음이 섞이거나 일부가 손상·누락된 관측에서 원래 자료를 복원하는 역문제를 설명한다. 자료가 나타날 가능성이 높은 방향을 추정해 관측을 반복적으로 바꾸는 방법과, 잡음을 단계적으로 더했다가 제거하는 확산 모형을 다룬다. 응용으로는 조건에 맞는 자료 생성, 영상 복원, 영상의 빈 부분 채우기와 해상도 향상을 든다. 해상도는 영상에서 서로 구별해 표현할 수 있는 세부 정보의 정도다.[^research]

### 단일 세포 자료의 해석과 분리

단일 세포 자료는 세포마다 관측값을 따로 기록한 자료다. 연구 소개는 음이 아닌 행렬 분해(음수가 없는 자료표를 음이 아닌 성분들의 곱으로 나타내는 방법)를 개발해 공통 성분과 세포별 성분을 구분하고, 그 결과가 생물학적으로 해석될 수 있도록 한다.[^research] 대표 논문 3은 여러 기증자의 세포를 함께 분석한 자료에서 유전형(개체가 가진 특정 유전정보의 구성)을 이용해 세포가 어느 기증자에게서 왔는지 추정하는 소프트웨어를 제안한다. 이 방법은 기증자별 기준 유전형 없이도 작동하도록 설계됐다.[^p3]

### 관계망의 집단 구조와 변수 간 의존 관계

연구 소개의 집단 탐지는 관계망 안에서 내부 연결이 촘촘하고 집단 사이의 연결은 드문 묶음을 찾는 문제다. 신경망(연결된 계산 단위 사이의 연결 강도를 자료로 조정해 배우는 계산 모형)을 이 문제와 결합하는 접근도 설명한다. 특히 집단 구조를 평가하는 지표와 그래프 신경망(Graph Neural Networks, 관계로 연결된 대상 사이에서 정보를 주고받으며 자료의 표현을 학습하는 모형)을 함께 다룬다.[^research] 생물 자료의 관계망 연구에서는 여러 자료의 정보를 결합해 유전자 사이 또는 유전자와 유전체(한 생물이 가진 유전정보 전체) 사이의 조절 관계를 모형화하고, 여러 관계망을 함께 추정한다.[^research]

## 대표 논문

생성 모형을 이용한 자료 표현과 이론, 생물 자료 분석 방법, 정상 세포의 발달 조절 원리를 나누어 골랐다. 전현호 부교수가 저자로 참여한 KAIST 재직 시기의 논문이며, 5번은 arXiv 사전 공개본이다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 주요 저자와 교수 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2023 | [Similarity-assisted variational autoencoder for nonlinear dimension reduction with application to single-cell RNA sequencing data](https://doi.org/10.1186/s12859-023-05552-1) · BMC Bioinformatics | Gwangwoo Kim, Hyonho Chun. 전현호는 마지막 저자 | 자료를 압축하고 복원하는 생성 모형에 자료 사이의 유사도 정보를 넣어 집단 구조를 드러낸다. 부가 특성의 영향도 조정하도록 확장했다.[^p1] |
| 2 | 2022 | [Deep Nonnegative Matrix Factorization Using a Variational Autoencoder With Application to Single-Cell RNA Sequencing Data](https://doi.org/10.1109/tcbb.2022.3172723) · IEEE Transactions on Computational Biology and Bioinformatics | Dong Jun Jee, Yixin Kong, Hyonho Chun. 전현호는 마지막 저자 | 세포들의 관측값을 공통 성분과 세포별 성분으로 나눈다. 세포별 성분에는 비선형 차원 축소를 적용하면서 세포 유형별 발현을 추정할 수 있도록 했다.[^p2] |
| 3 | 2022 | [scAVENGERS: a genotype-based deconvolution of individuals in multiplexed single-cell ATAC-seq data without reference genotypes](https://doi.org/10.1093/nargab/lqac095) · NAR Genomics and Bioinformatics | 첫 저자 Seung-Beom Han, 마지막 저자 Inkyung Jung. 전현호는 공동저자 | 기증자별 기준 유전형 없이, 여러 사람의 세포가 섞인 자료를 기증자별로 가르는 소프트웨어를 제안한다. 개인별 유전적 차이를 찾는 과정과 혼합 자료를 설명하는 모형을 조정했다.[^p3] |
| 4 | 2022 | [Biphasic regulation of osteoblast development via the ERK MAPK–mTOR pathway](https://doi.org/10.7554/elife.78069) · eLife | 첫 저자 Jung‐Min Kim, 마지막 저자 Jae‐Hyuck Shim. 전현호는 공동저자 | 뼈를 만드는 세포에서 같은 신호 전달 경로(세포 안에서 신호가 차례로 전해지는 단백질들의 연쇄)가 발달 초기와 후기에는 서로 다른 영향을 준다는 원리를 밝힌다. 신호를 억제하면 초기 분화(세포가 특정한 기능을 가진 세포로 되어 가는 과정)는 막히지만 후기 분화는 촉진되는 현상을 설명한다.[^p4] |
| 5 | 2026 | [Identifiability and Stability of Generative Drifting in the Companion-Elliptic Kernel Family](https://doi.org/10.48550/arxiv.2604.24196) · arXiv 사전 공개본 | Hak Geun Lee, Hyonho Chun. 전현호는 마지막 저자 | 목표 자료로의 끌림과 생성 자료 사이의 밀림으로 학습하는 생성 모형에서 학습이 멈췄을 때 목표 분포와 일치할 조건을 증명한다. 관측 범위 안의 정보만으로 전체 오차를 제어할 수 없는 경우도 제시한다.[^p5] |

## 교수와 전문 분야

전현호 부교수의 학과 소개는 전문 분야를 다변량 통계, 기계학습, 통계적 지노믹스로 적고, University of Wisconsin at Madison, Wisconsin 박사로 소개한다.[^dept] 학과의 부임 공지는 2019년 7월 22일 부교수로 부임했다고 밝힌다.[^appointment]

대표 논문에서 드러나는 방법론적 전문 분야는 생성 모형과 유사도 정보를 결합한 자료 표현, 해석 가능한 단일 세포 자료 분석, 유전정보를 활용한 혼합 자료의 분리다.[^p1][^p2][^p3] 정상 뼈 형성의 세포 발달 조절 원리를 다룬 공동연구에도 참여했다.[^p4]

## 응용 분야

연구 소개는 생성 모형의 영상 생성 응용, 불완전한 영상의 복원, 단일 세포의 유전자 발현 자료 분석, 생물 변수 사이의 조절 관계 추정을 다룬다.[^research] 대표 논문의 분석 방법은 단일 세포 자료의 집단 구조를 살피거나 서로 섞인 기증자 자료를 분리하는 데 쓰인다.[^p1][^p2][^p3]

## 구성원

2026년 11월 7일 Members 쪽의 현재 학생 명단이다. 박사과정 3명과 석박사통합과정 2명이며, 기간·연구 주제·학교 이메일은 게시 표기다. ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Gwangwoo Kim | 박사과정 | 2023.03 ~ present | generative models | urikokp@kaist.ac.kr | 1 |
| Hakgeun Lee | 석박사통합과정 | 2023.03 ~ present | Machine Learning | nas15464@kaist.ac.kr |  |
| Seonghyeon Jo | 박사과정 | 2025.03 ~ present | Graph Neural Network, Machine Learning | sungg93@kaist.ac.kr |  |
| Kyungjin Shin | 박사과정 | 2026.03 ~ present | Diffusion Model, Inverse Problem, Machine Learning | kj_shin@kaist.ac.kr |  |
| Youjin Park | 석박사통합과정 | 2025.03 ~ present | Machine Learning | tpdnjs0314@kaist.ac.kr |  |

Gwangwoo Kim, Seonghyeon Jo, Kyungjin Shin의 게시 소속은 Graduate School of Data Science이고, Hakgeun Lee와 Youjin Park의 게시 소속은 Mathematical Sciences다. Gwangwoo Kim은 KAIST 수리과학과 석사(2021–2023), Kwangwoon University 수학과 학사(2017–2021)를 적는다. Seonghyeon Jo의 석사과정 기간은 2023년 3월–2025년 2월, Kyungjin Shin의 석사과정 기간은 2024년 3월–2026년 2월로 적혀 있다.[^members]

## 최근 5년 논문 목록

연구실 Publications 쪽에 게시된 2021–2026년 항목 가운데 아래 논문 6편을 싣는다. 제목·저자·발표처와 연도는 누리집 표기이며, 논문 연도는 게시 목록의 연도다. bioRxiv 항목도 누리집의 발표처·연도 표기로 표시했다.[^publications]

**2023**

- Gwangwoo Kim and Hyonho Chun. "Similarity-assisted Variational Autoencoder for Nonlinear Dimension Reduction with Application to Single-cell RNA Sequencing Data". *BMC Bioinformatics (2023)*. <https://doi.org/10.1186/s12859-023-05552-1>

**2022**

- D. Jee, Y. Kong, and H. Chun. "Deep nonnegative matrix factorization using a variational autoencoder with application to single-cell RNA sequencing data". *IEEE/ACM Transactions on Computational Biology and Bioinformatics (2022)*. <https://doi.org/10.1109/tcbb.2022.3172723>
- Seungbeom Han, Kyukwang Kim, Seongwan Park, Andrew J Lee, Hyonho Chun, Inkyung Jung. "scAVENGERS: a genotype-based deconvolution of individuals in multiplexed single-cell ATAC-seq data without reference genotypes". *NAR Genomics and Bioinformatics (2022)*. <https://doi.org/10.1093/nargab/lqac095>
- Jung-Min Kim, Yeon-Suk Yang, Jaehyoung Hong, Sachin Chaugule, Hyonho Chun, Marjolein CH van Der Meulen, Ren Xu, Matthew B Greenblatt, Jae-hyuck Shim. "Biphasic regulation of osteoblast development via the ERK MAPK–mTOR pathway". *Elife (2022)*. <https://doi.org/10.7554/elife.78069>
- JM Kim, YS Yang, J Xie, O Lee, JH Kim, J Hong, B Boldyreff, O Filhol, H Chun, MB Greeblatt, G Gao, JH Shim. "Regulation of sclerostin by the SIRT1 stabilization pathway in osteocytes". *Cell Death & Differentiation (2022)*. <https://doi.org/10.1038/s41418-022-00952-x>[^supp-s06]
- JM Kim, YS Yang, J Hong, S Chaugule, H Chun, MCH van der Meulen, R Xu, MB Greenblatt, JH Shim. "Impaired ERK MAPK activation in mature osteoblasts enhances bone formation via the mTOR pathway". *bioRxiv (2022)*. <https://doi.org/10.1101/2022.01.24.477465>[^supp-s07]

## 수상과 선정

연구실 Gallery가 알린 수상 1건이다. 연도는 게시 제목 표기이며 날짜는 게시되어 있지 않다.[^gallery]

- 2024년 · FSI AIxData Challenge 2024 대상: 신경진·유현수 학생과 공동 참여자 이다현·문지유

## 연락과 위치

- 교수 업무 이메일: hyonhochun@kaist.ac.kr[^members]
- 교수 연구실 위치: 산업경영학동 3207[^dept]
- 학과 교수 목록의 기관 전화 표기: T2741[^dept]
[^dept]: KAIST 수리과학과, 「교수」의 전현호 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> 관측일 2026-11-07.
[^members]: STAT HT LAB, 「Members」. <https://stathtlab.kaist.ac.kr/27> 관측일 2026-11-07.
[^research]: STAT HT LAB, 「Research」. <https://stathtlab.kaist.ac.kr/29> 관측일 2026-11-07.
[^research-gen]: STAT HT LAB, 「Research」의 Generative model 설명. 다양한 생성 모형 자체를 연구하고 영상 생성 등의 응용을 찾는다는 연구 목표. <https://stathtlab.kaist.ac.kr/29> 관측일 2026-11-07.
[^research-bio]: STAT HT LAB, 「Research」의 High-Throughput data analysis 및 Graphical Models 설명. 단일 세포 자료 분석을 위한 새 모형 제안과 생물 변수 관계의 모형 개발. <https://stathtlab.kaist.ac.kr/29> 관측일 2026-11-07.
[^publications]: STAT HT LAB, 「Publications」. <https://stathtlab.kaist.ac.kr/30> 관측일 2026-11-07.
[^gallery]: STAT HT LAB, 「Gallery」의 FSI AIxData Challenge 2024 대상 게시 항목 두 개. <https://stathtlab.kaist.ac.kr/32> 관측일 2026-11-07.
[^appointment]: KAIST 수리과학과, 「Meet Our New Faculty: Hyonho Chun」, 2019-07-25. <https://mathsci.kaist.ac.kr/home/en/2019/07/meet-our-new-faculty-hyonho-chun/> 관측일 2026-11-07.
[^supp-s06]: J.-M. Kim 외, J.-H. Shim, Cell Death & Differentiation (2022). <https://doi.org/10.1038/s41418-022-00952-x> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41418-022-00952-x%22> 관측일 2026-11-07.
[^supp-s07]: J.-M. Kim 외, J.-H. Shim, bioRxiv (연구실 기재 2022). <https://doi.org/10.1101/2022.01.24.477465> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1101/2022.01.24.477465> 관측일 2026-11-07.
[^p1]: G. Kim, H. Chun, BMC Bioinformatics (2023). <https://doi.org/10.1186/s12859-023-05552-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101891706,publication_year:2021-2026> 관측일 2026-11-07.
[^p2]: D. J. Jee, Y. Kong, H. Chun, IEEE Transactions on Computational Biology and Bioinformatics (2022). <https://doi.org/10.1109/tcbb.2022.3172723> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101891706,publication_year:2021-2026> 관측일 2026-11-07.
[^p3]: S.-B. Han 외, I. Jung, NAR Genomics and Bioinformatics (2022). <https://doi.org/10.1093/nargab/lqac095> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101891706,publication_year:2021-2026> 관측일 2026-11-07.
[^p4]: J.-M. Kim 외, J.-H. Shim, eLife (2022). <https://doi.org/10.7554/elife.78069> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101891706,publication_year:2021-2026> 관측일 2026-11-07.
[^p5]: H. G. Lee, H. Chun, arXiv (Cornell University) (2026). <https://doi.org/10.48550/arxiv.2604.24196> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5101891706,publication_year:2021-2026> 관측일 2026-11-07.

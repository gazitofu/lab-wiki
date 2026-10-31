# Statistical Data Science Lab

**KAIST 산업및시스템공학과·Graduate School of AI for Math(겸임) · 안정연 교수**

- 분야: 고차원 통계적 학습, 조성 자료 분석, 해석 가능한 분류와 변수 선택, 전이학습, 개인정보 보호를 위한 합성 자료와 통계 분석
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 통계적 추론·검정[^resampling][^p5], AI·기계학습 보안·프라이버시[^home][^p6], 데이터 중심 AI·데이터 효율 학습[^home]
- 홈페이지: <https://statds.kaist.ac.kr/>
- 근거와 출처: [Statistical Data Science Lab 근거 페이지](statds-sources.md)

> 변수가 많거나 비율·곡선처럼 특별한 구조를 가진 자료를 분석하는 통계 방법을 만들고, 결과의 해석 가능성과 개인정보 보호를 함께 연구하는 연구실이다.[^home][^prof]

## 무엇을 연구하나

Statistical Data Science Lab은 KAIST 산업및시스템공학과 안정연 교수가 이끄는 연구실이다. 여러 과학 분야에서 생기는 고차원 자료(표본 하나에 기록하는 변수의 수가 많은 자료)와 복잡한 자료를 위한 통계 방법을 개발하며, 분석 결과를 사람이 해석할 수 있게 하는 데 중점을 둔다.[^home][^prof] 교수 소개는 지도학습(정답이 붙은 자료로 예측 규칙을 배우는 방법), 비지도학습(정답 없이 자료의 구조를 찾는 방법), 이상 탐지(자료에서 평소와 다른 관측을 찾는 방법)를 연구 관심으로 든다. 자료 유형으로는 시간 등에 따른 변화를 곡선으로 나타낸 함수형 자료, 센서 자료, 초고차원 자료, 텐서(여러 축으로 수를 배열한 자료), 조성 자료를 다룬다.[^prof]

첫 화면의 한 갈래는 전이학습(다른 자료나 과제에서 얻은 정보를 목표 자료의 분석에 활용하는 방법)이다. 목표 자료와 함께 다른 집단에서 얻은 원천 자료를 이용하는 방법을 개발한다. 예로 목표 자료와 원천 자료의 스펙트럼 유사성(행렬을 분해해 얻는 값과 방향의 구조가 닮은 정도)에 기반한 고차원 공분산 행렬(변수들이 함께 변하는 정도를 배열한 행렬) 추정 틀을 소개한다. 연구실은 이 추정의 개선이 PCA(Principal Component Analysis, 자료의 분산, 즉 값들이 평균에서 흩어진 정도를 기준으로 새 좌표축을 만드는 주성분 분석), LDA(Linear Discriminant Analysis, 집단을 구분하는 선형식을 찾는 선형 판별 분석), 네트워크 분석으로 이어질 수 있다고 설명한다.[^home]

조성 자료(성분들의 합이 일정하고 성분 사이의 상대적인 비율에 의미가 있는 자료)는 일반적인 좌표 자료와 다른 구조를 가진다. 연구실은 영 성분이 있을 때 로그 비율 변환(성분 사이 비율에 로그를 취하는 변환)이 겪는 문제를 다루며, 영을 다른 값으로 대체하지 않는 방법을 연구한다. 첫 화면은 초구면(차원에 관계없이 중심에서 같은 거리에 있는 점들의 집합)을 이용한 커널 밀도 추정(자료 사이 관계를 나타내는 함수를 이용해 확률 밀도를 추정하는 방법), 해석 가능한 차원 축소(자료의 핵심 정보를 유지하면서 표현에 쓰는 변수 수를 줄이는 방법), 고차원 조성 자료의 평균 추정을 소개한다.[^home] 대표 논문들은 조성 자료에 맞는 커널(자료 쌍 사이의 관계를 함수로 나타내는 도구)을 구성하고, 분석에 필요한 성분을 고르는 통계 방법을 제안한다.[^p2][^p3][^p4]

다른 갈래는 개인정보 보호를 위한 합성 자료(원자료의 통계적 성질을 반영해 새로 만든 자료)와 통계 분석이다. 연구실은 주요 분포, 변수 사이 의존 관계와 고차 구조를 보존하고, 자료가 따라야 하는 제약과 내부 일관성을 만족시키는 합성 자료 생성 방법을 개발한다. 동시에 멤버십 추론(어떤 개인의 자료가 학습에 쓰였는지 알아내는 공격)과 속성 노출 위험을 줄여 자료의 유용성과 개인정보 보호 사이 균형을 연구한다.[^home] 차분 프라이버시(한 개인의 자료가 달라져도 분석 결과를 통해 그 차이를 구별하기 어렵도록 제한하는 개인정보 보호 기준)를 만족시키는 추정과 커널 학습도 연구한다.[^p5][^p6]

## 주요 연구 주제

### 1. 해석 가능한 고차원 분류와 변수 선택

순서형 분류(범주 사이의 자연스러운 순서를 반영하는 분류)에서는 집단을 가르는 변수와 그 순서에 맞게 변하는 변수를 함께 다룬다. 대표 논문 1은 변수마다 순서 관련 가중치를 주고, 분류에 필요한 변수 또는 순서와 분류에 함께 관련된 변수를 선택하는 방법을 제안한다. 모의 자료와 실제 자료에서 선택 결과의 해석 가능성을 살폈다.[^p1] 교수 소개의 통계적 학습 관심은 지도·비지도학습과 이상 탐지를 함께 포함한다.[^prof]

### 2. 영 성분이 있는 조성 자료의 기하와 차원 축소

대표 논문 2는 영 성분을 바꾸지 않는 방사형 변환과 초구면의 커널을 연결한다. 대표 논문 3은 반응에 관한 정보를 유지하는 충분 차원 축소(축소한 표현을 알면 원자료가 반응에 추가 정보를 주지 않도록 하는 차원 축소)를 조성 자료에 맞게 구성하고 변수를 선택한다. 대표 논문 4는 조성 자료와 구면 사이의 기하 관계를 이용해 여러 커널 분석 방법의 이론적 틀을 제시한다.[^p2][^p3][^p4] 별도의 조성 회귀 논문은 표본 수가 적을 때 변수 선택과 재표집(관측 자료를 다시 뽑거나 배열해 분석을 반복하는 방법)을 결합해 개별 회귀 계수를 추론하는 절차를 제안했다.[^resampling]

### 3. 개인정보 보호 아래의 추론·학습과 합성 자료

대표 논문 5는 개인이 자료를 수집자에게 보내기 전에 보호하는 지역 차분 프라이버시에서 평균과 확률 밀도의 추정 오차를 분석한다. 개인정보 보호 제약 아래 가능한 오차의 한계와 그 한계를 달성하는 절차를 함께 다룬다.[^p5] 대표 논문 6은 일반 커널을 쓰는 학습과 분포 정보 공개를 차분 프라이버시 아래 수행하는 알고리즘을 제안하며, 개인정보를 보호하는 자료 생성 알고리즘도 개발한다.[^p6] 첫 화면의 합성 자료 연구는 생성된 자료의 통계적 성질과 제약 준수, 개인정보 노출 위험을 함께 목표로 삼는다.[^home]

### 4. 다른 집단의 자료를 활용하는 전이학습

고차원 목표 자료를 분석할 때 다른 집단의 원천 자료를 활용하고, 공분산 추정을 개선하는 방법을 연구한다. 연구실은 목표 자료와 원천 자료 사이의 스펙트럼 유사성을 이용한 틀을 개발했다고 소개하며, 주성분 분석과 선형 판별 분석, 네트워크 분석의 개선 가능성을 설명한다.[^home]

## 대표 논문

연구실이 게시한 논문 가운데 안정연 교수의 KAIST 재직 시기에 해당하는 2022–2025년 논문을 고차원 분류·조성 자료·개인정보 보호 갈래에서 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 대표 논문 1의 설명은 학술지판과의 관계가 표시된 arXiv 판을 따른다. 주요 저자는 초록 페이지에 적힌 전체 저자 순서이며, 교신 역할을 뜻하지 않는다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Variable selection and basis learning for ordinal classification](https://doi.org/10.1080/10618600.2025.2451680) · Journal of Computational and Graphical Statistics | 범주에 자연스러운 순서가 있는 고차원 자료를 분류하려고, 변수 선택과 분류에 쓸 표현을 함께 배우는 방법을 제안했다. 집단을 구분하는 데 관련된 변수뿐 아니라 범주의 순서와 맞게 변하는 변수도 찾는다. 변수마다 순서 관련 가중치를 만들고 이를 선택 과정에 반영한다. 변수 수가 표본 수보다 훨씬 빠르게 늘어나는 조건에서 조절값에 따라 분류에 관련된 변수 또는 순서와 분류에 함께 관련된 변수를 일관되게 선택한다는 성질을 보였고, 모의 자료와 실제 자료에서 해석 가능한 표현을 확인했다.[^p1] | Minwoo Kim, Sangil Han, Jeongyoun Ahn, Sungkyu Jung |
| 2 | 2022 | [Kernel Methods for Radial Transformed Compositional Data with Many Zeros](https://proceedings.mlr.press/v162/park22d.html) · Proceedings of the 39th International Conference on Machine Learning | 영 성분이 많은 비율 자료를 분석할 때 영을 작은 양수로 바꾸고 로그를 취하면 자료의 기하 구조가 왜곡될 수 있다. 영을 대체하지 않는 방사형 변환을 제안하고, 변환 전후 공간 사이의 관계를 이용해 초구면의 여러 커널을 조성 자료에 적용할 수 있음을 보였다. 커널 주성분 분석으로 이 접근의 적용 가능성을 예시했다.[^p2] | Junyoung Park, Changwon Yoon, Cheolwoo Park, Jeongyoun Ahn |
| 3 | 2023 | [Kernel Sufficient Dimension Reduction and Variable Selection for Compositional Data via Amalgamation](https://proceedings.mlr.press/v202/park23a.html) · Proceedings of the 40th International Conference on Machine Learning | 성분 수가 많고 영 성분도 많은 비율 자료에서, 분석 결과를 해석할 수 있게 차원을 줄이고 중요한 성분을 고르는 방법을 제안했다. 영 성분을 자연스럽게 다루면서 성분 사이의 비선형 관계와 겉보기 음의 상관을 반영한다. 실제 신호와 관련된 변수를 모으는 통계적 성질을 보였으며, 모의 자료와 실제 미생물군 자료로 기존 접근과 비교했다.[^p3] | Junyoung Park, Jeongyoun Ahn, Cheolwoo Park |
| 4 | 2023 | [Reproducing Kernels and New Approaches in Compositional Data Analysis](https://www.jmlr.org/papers/v24/21-1398.html) · Journal of Machine Learning Research | 비율 자료가 놓인 공간을 구면의 점들을 특정 관계에 따라 묶은 공간으로 해석했다. 이를 통해 조성 자료에 맞는 함수 공간과 커널을 구성하는 이론적 틀을 만들었다. 이 틀을 조성 자료의 확률 밀도를 추정하거나 자료를 분류하는 예에 적용해 활용 범위를 보였다.[^p4] | Binglin Li, Changwon Yoon, Jeongyoun Ahn |
| 5 | 2023 | [Minimax Risks and Optimal Procedures for Estimation under Functional Local Differential Privacy](https://doi.org/10.52202/075280-2526) · Advances in Neural Information Processing Systems | 개인의 자료를 수집자에게 보내기 전에 보호하는 조건에서 통계 분석을 얼마나 정확히 할 수 있는지 연구했다. 가설 검정으로 개인정보 보호 수준을 표현하는 틀에서 평균과 확률 밀도를 추정할 때 가능한 오차의 한계를 분석하고, 개인정보 보호 수준과 통계적 유용성 사이의 연속적인 균형을 제시했다. 이 한계를 달성하는 절차를 제안하고 수치 연구로 평가했다.[^p5] | Bonwoo Lee, Jeongyoun Ahn, Cheolwoo Park |
| 6 | 2024 | [Differential Privacy in Scalable General Kernel Learning via K-means Nyström Random Features](https://doi.org/10.52202/079017-0666) · Advances in Neural Information Processing Systems | 개인정보를 보호하면서 일반적인 커널로 학습하거나 자료의 분포 정보를 공개하는 알고리즘을 제안했다. 기존 커널 학습에서 쓰는 니스트룀 근사(커널 행렬의 일부를 이용해 전체를 근사하는 방법)를 개인정보 보호 조건에 맞게 구성해, 자료에 따라 정해지는 커널 행렬의 저랭크 근사(행렬이 담는 독립적인 정보의 수를 줄이는 근사)를 만든다. 학습 오차의 경계와 계산 복잡도를 제시했고, 여러 커널 모델을 배울 수 있는 개인정보 보호 자료 생성 알고리즘도 개발해 실험했다.[^p6] | Bonwoo Lee, Jeongyoun Ahn, Cheolwoo Park |

## 교수와 전문 분야

안정연(Jeongyoun Ahn) 교수는 서울대학교에서 통계학 학사·석사 학위를, University of North Carolina at Chapel Hill의 Statistics and Operations Research 학과에서 통계학 박사 학위를 받았다. 교수 소개의 경력은 University of Georgia 조교수(2006–2012), 부교수(2012–2021), KAIST 부교수(2021–2024), 교수(2024년부터) 순서다. University of Georgia의 Affiliated Faculty 경력도 2021–2023년으로 적혀 있다. 현재 교수 소개는 산업및시스템공학과 Professor와 Graduate School of AI for Math의 Adjunct Professor를 함께 적는다.[^prof]

전문 분야는 비표준 구조의 자료를 다루는 통계적 기계학습과 해석 가능한 분석 방법이다. 최근 논문은 순서형 고차원 분류와 변수 선택, 조성 자료의 커널 이론과 차원 축소, 개인정보 보호 아래의 통계 추론과 학습으로 이어진다.[^prof][^p1][^p2][^p3][^p4][^p5][^p6] 교수 소개는 The American Statistician의 Associate Editor(2014년부터), Journal of Korean Statistical Society의 Associate Editor(2018년부터), Chemometrics and Intelligent Laboratory System의 Editorial Board(2016년부터)도 적는다.[^prof]

## 응용 분야

연구실은 여러 과학 분야의 고차원·복잡 자료 분석을 대상으로 한다. 첫 화면은 미생물군 연구에서 만나는 고차원 조성 자료와, 개인정보 때문에 공유하기 어려운 자료를 위한 합성 자료 생성을 소개한다.[^home] 대표 논문에는 미생물군 자료에서 성분을 선택하고 차원을 줄이는 연구가 있으며,[^p3] 별도 논문은 소의 미생물군 자료로 새 통계 추론 절차를 평가했다.[^resampling] 개인정보 보호 연구는 자료 수집·공개와 커널 학습의 통계적 유용성을 함께 다룬다.[^p5][^p6]

## 구성원

2026년 10월 31일 Students 페이지의 박사과정 7명과 석사과정 6명이다. Bonwoo Lee는 Department of Mathematical Science의 공동지도(Co-advising)로 게시돼 있다. 시작 시점은 따로 적혀 있지 않으며, 연구 주제와 학교 이메일은 게시 표기다.[^students] 「대표 논문 참여」는 대표 논문의 전체 저자 목록에서 같은 이름을 확인한 경우에 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Changwon Yoon | 박사과정 | non-Euclidean data analysis, Data Privacy | cwyoon@kaist.ac.kr | 2, 4 |
| Giwon Kim | 박사과정 | Kernel-based ML, Dimension Reduction | 71_won@kaist.ac.kr |  |
| Yian Kim | 박사과정 | Statistical Learning | yian9995@kaist.ac.kr |  |
| Lars Kutschinski | 박사과정 | Transfer Learning | larskut@kaist.ac.kr |  |
| Bonwoo Lee | 박사과정 |  |  | 5, 6 |
| Junmo Lee | 박사과정 | Statistical Learning | bubblego0217@kaist.ac.kr |  |
| Seongbin An | 박사과정 | Transfer Learning, Distribution Shift | as_bean@kaist.ac.kr |  |
| Jinyoung Hong | 석사과정 | Interpretable AI | urared@kaist.ac.kr |  |
| Taewook Kim | 석사과정 | Synthetic Data Generation, Data Privacy | twkim@kaist.ac.kr |  |
| Yelin Suh | 석사과정 | Statistical Modeling for Social Phenomena | yelin1995@kaist.ac.kr |  |
| Junyong An | 석사과정 | Statistical Learning | junyong0364@kaist.ac.kr |  |
| ByeongJun An | 석사과정 | Statistical Learning | kwn08106@kaist.ac.kr |  |
| Danbi Kim | 석사과정 | Statistical Learning | danbi@kaist.ac.kr |  |

### 학부 연구 참여 기록

Students 페이지의 「Undergraduates (Lab Intern/Individual Research/Undergraduate Research Projects)」에 게시된 2022–2026년 기록 20행이다. 학부 인턴·개별 연구·학부생 연구 프로그램을 한 구획으로 적고 있으므로 각 행의 세부 참여 방식은 괄호 표기대로 둔다. 같은 이름이 다른 연도에 다시 게시된 행도 함께 싣는다.[^students]

| 이름 | 랩이 적은 소속·기간·프로그램 |
|---|---|
| Nikolai Kurlovich | KAIST Math, 2022-2023 |
| Diyar Tulenov | KAIST CS, 2022-2023, URP |
| 조성빈 | KAIST Math/ISE, 2023 |
| 황규림 | KAIST Math, 2023, URP |
| 최지호 | KAIST Math, 2023 |
| 이대환 | KAIST ISE, 2023 |
| 윤대한 | KAIST Math, 2023 |
| 심우용 | KAIST ISE, 2023-2024, URP |
| 이정준 | KAIST ISE, 2023 |
| 홍진영 | KAIST ISE, 2024 |
| 안정원 | KAIST ISE, 2024 |
| 박규태 | KAIST ISE, 2024 |
| 안병준 | KAIST ISE, 2025 |
| 송진형 | KAIST ISE, 2025 |
| 이찬민 | KAIST ISE, 2025 |
| 이한스 | KAIST Math, 2026 |
| 함지운 | KAIST ISE, 2026 |
| 김지하 | KAIST EE, 2026 |
| 안병준 | KAIST ISE, 2026 |
| 송진형 | KAIST ISE, 2026 |

## 졸업생과 이전 구성원

Students 페이지의 Former Students 17행이다. 학위 연도는 2013–2025년이며 교수의 KAIST 부임 전 지도 이력도 함께 포함된 목록이다. 학위·연도·학위 논문과 진로는 게시 표기를 따르고, Seongbin An의 석사 졸업과 현재 박사과정 표기는 각각 둔다.[^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Hyunbin Choi | MS. (2025) | SK hynix, South Korea | Dynamic Sample Weighting for Classification with Asymmetric Label Noise: Application to Postoperative Complication Prediction |
| Jiyu Moon | MS. (2025) | KT, South Korea | Predicting Sleep-Wake Times from Wearable Sensor Data using Gaussian Mixtures |
| Daeyoung Kim | MS. (2024) | SK hynix, South Korea | Graph-level Outlier Detection with Normalized Graph Kernel |
| Hyunwoo Cha | MS. (2024) | Samsung Electronics, South Korea | Ovarian Cancer Risk Prediction and Decision Making for Screening in Clinical Practice |
| Junyoung Park | Ph.D (2024) | Post-doc at University of Michigan, Ann Arbor, USA | Kernel Methods for Compositional Data and Dimension Reduction |
| Yunji Kim | MS. (2024) | Hyundai Motor Company, South Korea | Multiple imputation using predictive mean matching for canonical correlation analysis with block-wise missing data |
| Seongbin An | MS. (2024) | Ph.D. student at KAIST, South Korea | Monotone Clustering with Sparse Generalized Additive Model |
| Binglin Li | Ph.D (2023) | Assistant Professor, North Carolina Agricultural and Technical State University, USA | Geometric Techniques in Data Science |
| Di Xiao | Ph.D (2021) | AI and Data Science Associate, JP Morgan, USA | Learning Structure Changes in High-dimensional and Heavy-tailed Time Series |
| Seungwoo Kwak | Ph.D (2021) | Assistant Professor, Major of Big Data Application, Sungkonghoe University, South Korea | Application of differential privacy to a goodness-of-fit test and data release problems |
| Ziyang Ma | Ph.D (2021) | Quantitative Analytics Specialist, Wells Fargo Bank, USA | New Regularization Methods for Supervised Learning with High-Dimensional Data |
| JC Poythress | Ph.D (2020) | Assistant Professor, Department of Mathematics and Statistics, University of New Hampshire, USA | Regularization techniques for statistical methods utilizing matrix/tensor decompositions |
| Hee Cheol Chung | Ph.D (2020) | Assistant Professor, Department of Mathematics and Statistics, University of North Carolina-Charlotte, USA | Some Contributions to Statistical Inference on Small Sample Size Data: Small Area Estimation and High Dimension Low Sample Size Data Analysis |
| Debin Qiu | Ph.D (2015) | Vice President, Applied AI/ML Lead at JPMorgan Chase & Co, USA | Grouped Variable Screening for Ultrahigh Dimensional Data under Linear Model |
| Soyeon Jung | MS. (2015) | Senior Statistician, T-Mobile, USA | A New Approach for Error Correction in Multiple Goodness-of-Fit tests |
| Sandra S. Safo | Ph.D (2014) | Assistant Professor, Division of Biostatistics, University of Minnesota, USA | Design And Analysis Issues In High Dimension, Low Sample Size Problems |
| Jung Ae Lee-Bartlett | Ph.D (2013) | Assistant Professor, University of Messachusetts Medical School, USA | Sample Integrity in High Dimension |

## 최근 논문 목록 (2021–2026)

고차원 분류와 조성 자료 분석, 개인정보 보호를 위한 통계 방법을 다룬다. 연구실 Publications의 2021–2026년 표기 항목 가운데 21건이다. 이 페이지는 교수의 이전 소속 시기와 여러 기관 공동연구를 함께 담은 논문 목록이다. 제목·저자·발표처는 랩 표기이고, 2021년 두 항목은 월·일 없이 게시된 연도를 따른다. 「Monotone clusters with ordinal interpretation」는 날짜 없이 게재 승인으로 게시돼 있어 2026년 게시 연도에 두고 출판 논문과 구별했다. 「Local FDR Membership Inference Attacks」의 NeurIPS 2026 표기는 연구실이 적은 학회명·연도다. 저자 뒤 별표는 누리집 기호를 보존한 것이며 역할을 뜻하지 않는다.[^pubs]

**2026**

- Chung, H.C., An, S., Cha, H., and Ahn, J. (2026), Monotone clusters with ordinal interpretation, Statistical Analysis and Data Mining, 게재 승인.
- Hong, J.\*, Lee, B.\*, and Ahn, J. (2026), Local FDR Membership Inference Attacks: Multiple Testing and the Role of Ridge Regularization, Proceedings of the 40th Conference on Neural Information Processing Systems (NeurIPS) (연구실 기재).

**2025**

- Yoon, C.\*, Choi, H., and Ahn, J. (2025), Kernel density estimation for compositional data with zeros via hypersphere mapping, Computational Statistics and Data Analysis, 212:108249.
- Kim, M., Han, S., Ahn, J., and Jung, S. (2025), Variable selection and basis learning for ordinal classification, Journal of Computational and Graphical Statistics, 34(4):1432-1445.

**2024**

- Kim, T., Chang, W., Ahn, J., and Jung, S. (2024), Double Data Piling: A High-Dimensional Solution for Asymptotically Perfect Multi-Category Classification, Journal of the Korean Statistical Society, 1-34.
- Han, S., Kim, M., Jung, S., and Ahn, J. (2024), Sparse ordinal discriminant analysis, Biometrics, 80(1):ujad040.
- Kwak, S\*., Ahn, J., Lee, J. and Park, C. (2024), Differentially private goodness of fit tests for continuous variables,  Econometrics and Statistics, 31, 81-99.
- Lee, B.\*, Ahn, J., and Park, C. (2024), Differential privacy in scalable general kernel learning via K-means Nystrom random features, Proceedings of the 38th Conference on Neural Information Processing Systems (NeurIPS), 666:21141-21171.

**2023**

- Li, B.\*, Yoon, C.\*, and Ahn, J. (2023), Reproducing kernels and new approaches in compositional data analysis, Journal of Machine Learning Research, 24(327):1-34.
- Park, J.\*, Ahn, J., and Park, C. (2023), Kernel sufficient dimension reduction and variable selection for compositional data, Proceedings of the 40th International Conference on Machine Learning (ICML), 202:27034-27047.
- Lee, S., Jung, S., Lourenco, J., Pringle, D., and Ahn, J. (2023), Resampling-based inferences for compositional regression with application to beef cattle microbiomes, Statistical Methods in Medical Research, 32(1), 151-164.
- Yoon, C.\*, Jeon, Y., Choi, H., Kwon, S., and Ahn, J. (2023), Interpretable Classification for Multivariate Gait Analysis of Cerebral Palsy, BioMedical Engineering OnLine, 22, 109. [^supp-gait]
- Lee, B.\*, Ahn, J., and Park, C. (2023),  Minimax risks and optimal procedures for estimation under functional local differential privacy, Proceedings of the 37th Conference on Neural Information Processing Systems (NeurIPS), 2526:57964 - 57975.
- An, S.\*, Doan, T., Lee, J., Kim, J., Kim, YJ., Kim, Y.\*, Yoon, C.\*, Jung, S., Kim, D., Kwon, S., Kim, HJ., Ahn, J., and Park, C. (2023), A comparison of synthetic data approaches using utility and disclosure risk measures, The Korean Journal of Applied Statistics (in Korean), 36(2), 141-166.

**2022**

- Park, J.\*, Yoon, C.\*, Park, C., and Ahn, J. (2022), Kernel methods for radial transformed compositional data with many zeros, Proceedings of the 39th International Conference on Machine Learning (ICML), 162: 17458 - 17472.
- Poythress, J. C.\*, Ahn, J., and Park, C. (2022), A low-rank, orthogonally decomposable tensor regression with application to visual stimulus decoding with fMRI Data, Journal of Computational and Graphical Statistics, 31(1), 190-203. [^supp-tensor]
- Poythress, J. C.\*, Ahn, J., and Park, C. (2022), Dimension-wise sparse low-rank approximation of a matrix with application to variable selection in high-dimensional integrative analyses of association, Journal of Applied Statistics, 49(15):3889–3907.
- Park, J., Ahn, J., and Jeon, Y. (2022), Sparse functional linear discriminant analysis, Biometrika, 109(1):209-226.
- So, J., Ahn, J., and Guan, M. (2022), Beyond depth and breadth: Taking "types" of health information sought into consideration with cluster analysis, Journal of Health Communication, 27(1), 27 - 36. [^supp-health]

**2021**

- Chang, W., Ahn, J., and Jung, S. (2021), Double data piling leads to perfect classification, Electronic Journal of Statistics, 15(2):6382-6428.
- Chung, H. C.∗ and Ahn, J. (2021), Subspace rotations for high-dimensional outlier detection, Journal of Multivariate Analysis, 183, 104713.

## 공개 소프트웨어

Softwares 페이지는 순서형 해석을 위한 희소 단조 군집화의 R 패키지 SMOCL(Sparse Monotone Clustering with Ordinal Interpretation), Version 0.1.0을 소개한다. 관련 연구로 「Monotone Clusters with Ordinal Interpretation」를 적는다.[^software]

## 연락과 위치

- 연구실: Statistical Data Science Lab, E2-2 2111호, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 305-701, Republic of Korea[^home]
- 교수 사무실: E2-2 2104호[^prof]
- 교수 이메일: jyahn@kaist.ac.kr[^prof]
- 데이터사이언스대학원 구성원 페이지의 교수 연락처: 042-350-3140[^gsds]
[^home]: 연구실 첫 화면, Statistical Data Science Lab @ KAIST, 연구 소개와 위치. <https://statds.kaist.ac.kr/> 관측 2026-10-30.
[^prof]: 연구실 Professor, Jeongyoun Ahn의 소속·직위·연구 관심·학력·경력·학술 활동·사무실·이메일. <https://statds.kaist.ac.kr/professor> 관측 2026-10-31.
[^students]: 연구실 Students, Ph.D. Students·MS Students·Undergraduates·Former Students. <https://statds.kaist.ac.kr/students> 관측 2026-10-31.
[^pubs]: 연구실 Publications, Non-Euclid Data Analysis·High-dimensional Statistical Learning·Data Privacy·Interdisciplinary Research. <https://statds.kaist.ac.kr/publications> 관측 2026-10-31.
[^software]: 연구실 Softwares, SMOCL 패키지 설명. <https://statds.kaist.ac.kr/softwares> 관측 2026-10-31.
[^gsds]: KAIST 데이터사이언스대학원 구성원 페이지, 안정연 이름·연락처·홈페이지. <https://gsds.kaist.ac.kr/people> 관측 2026-10-30.
[^resampling]: S. Lee, S. Jung, J. Lourenco, D. Pringle, J. Ahn, Resampling-based inferences for compositional regression with application to beef cattle microbiomes, Statistical Methods in Medical Research 32(1), 151–164. DOI 10.1177/09622802221133550. 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.sagepub.com/doi/10.1177/09622802221133550> 관측 2026-10-31.
[^p1]: M. Kim, S. Han, J. Ahn, S. Jung, Journal of Computational and Graphical Statistics. <https://doi.org/10.1080/10618600.2025.2451680> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2208.10690> 관측 2026-10-31.
[^p2]: J. Park, C. Yoon, C. Park, J. Ahn, Proceedings of the 39th International Conference on Machine Learning 162, 17458–17472 (2022). <https://proceedings.mlr.press/v162/park22d.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v162/park22d.html> 관측 2026-10-31.
[^p3]: J. Park, J. Ahn, C. Park, Proceedings of the 40th International Conference on Machine Learning 202, 27034–27047 (2023). <https://proceedings.mlr.press/v202/park23a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/park23a.html> 관측 2026-10-31.
[^p4]: B. Li, C. Yoon, J. Ahn, Journal of Machine Learning Research 24, 1–34 (2023). <https://www.jmlr.org/papers/v24/21-1398.html> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://www.jmlr.org/papers/v24/21-1398.html> 관측 2026-10-31.
[^p5]: B. Lee, J. Ahn, C. Park, Advances in Neural Information Processing Systems 36 (2023). <https://doi.org/10.52202/075280-2526> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2023/hash/b4dde7f1bc45bf9c0fda8db8f272b758-Abstract-Conference.html> 관측 2026-10-31.
[^p6]: B. Lee, J. Ahn, C. Park, Advances in Neural Information Processing Systems 37 (2024). <https://doi.org/10.52202/079017-0666> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2024/hash/257c140d25d1f7fc10f8ae5e17296299-Abstract-Conference.html> 관측 2026-10-31.
[^supp-gait]: C. Yoon, Y. Jeon, H. Choi, S.-S. Kwon, J. Ahn, Interpretable classification for multivariate gait analysis of cerebral palsy, BioMedical Engineering OnLine 22(1), 109. <https://doi.org/10.1186/s12938-023-01168-x> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1186/s12938-023-01168-x> 관측 2026-10-31.
[^supp-tensor]: J. C. Poythress, J. Ahn, C. Park, Low-rank, Orthogonally Decomposable Tensor Regression With Application to Visual Stimulus Decoding of fMRI Data, Journal of Computational and Graphical Statistics 31(1), 190-203. <https://doi.org/10.1080/10618600.2021.1951741> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W3181597881> 관측 2026-10-31.
[^supp-health]: J. So, J. Ahn, M. Guan, Beyond Depth and Breadth: Taking “Types” of Health Information Sought into Consideration with Cluster Analysis, Journal of Health Communication 27(1), 27-36. <https://doi.org/10.1080/10810730.2022.2029978> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4210774200> 관측 2026-10-31.

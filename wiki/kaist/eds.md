# Engineering Data Science Lab

**KAIST 산업및시스템공학과·인공지능대학원(겸임) · 김희영 부교수, KAIST 지정 석좌교수**

- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 통계적 추론·검정[^p1][^p6], 이상·변화점 탐지[^p6], 상태 추정·필터링(데이터 동화)[^p4], 설명 가능한 AI(XAI)[^p1]
- 홈페이지: <https://eds.kaist.ac.kr/professor/>

> 자료의 불균형과 부족, 예측의 불확실성, 시간·공간의 관계를 다루는 통계·인공지능 방법을 개발해 산업 시스템의 품질 문제에 연결하는 연구실이다.[^prof][^research][^p4][^p5]

## 무엇을 연구하나

Engineering Data Science Lab은 김희영 부교수가 이끄는 산업및시스템공학과 연구실이다. 교수 소개와 연구 소개는 통계, 데이터 과학, 인공지능, 품질공학을 연구 관심으로 들고, 현실의 복잡한 문제를 해결하고 산업 시스템의 품질을 높이기 위해 데이터 과학의 방법론을 발전시키는 것을 연구 목표로 밝힌다.[^prof][^research]

한 갈래는 자료가 충분하지 않거나 종류별 개수가 고르지 않을 때의 학습이다. 반지도학습(정답이 표시된 자료와 표시되지 않은 자료를 함께 써서 배우는 방법)에서는 모델이 정답 없는 자료에 붙인 예측을 다시 학습에 활용한다. 이때 개수가 많은 종류로 예측이 치우치면 그 치우침도 학습에 들어간다. 보조 균형 분류기(ABC, Auxiliary Balanced Classifier) 연구는 종류별 균형을 고려하는 보조 분류기를 붙여 이 문제를 다룬다.[^p5] 최근 논문 목록에는 반도체 웨이퍼 검사 결과의 결함 유형 분류, 정답 표기가 부정확한 자료의 학습, 종류별 비율이 서로 다른 자료 묶음의 학습이 함께 올라 있다.[^research]

다른 갈래는 예측이 얼마나 불확실한지를 수치로 나타내고, 학습 때와 성질이 다른 입력을 가려내는 일이다. 연구실은 확률분포(가능한 값과 그 값이 나타날 가능성을 나타내는 수학적 표현)를 이용해 분류 예측의 불확실성을 표현하는 방법을 개발한다. Courtroom Analogy 연구는 종류별 판단을 모아 최종 예측을 만드는 구조를 두고 그 불확실성이 합쳐지는 과정을 해석할 수 있게 한다.[^p1] 또 분포 밖 탐지(학습 자료의 분포와 다른 성질을 가진 입력을 찾아내는 일)를 위해 가설 검정(자료가 어떤 가정과 맞는지 통계적으로 판단하는 방법)을 사용하는 연구도 있다.[^p6]

시간과 위치에 따라 달라지는 자료도 다룬다. 시공간 예측(시간과 위치의 관계를 함께 고려해 값을 예측하는 일)에서는 관측 시각이 일정하지 않고 일부 위치에 관측이 없으며, 멀리 떨어진 위치끼리도 영향을 주고받을 수 있다. 비국소 베이지안 시공간 모형(NLBST, NonLocal Bayesian Spatio-Temporal model) 연구는 이런 조건을 다루면서 관측이 들어올 때 상태를 갱신하고 예측의 불확실성도 나타내는 모형을 제안한다.[^p4] 별도의 인과 구조 학습 연구는 여러 단계로 이루어진 공정에서 각 변수가 어느 단계에 속하는지에 관한 지식을 이용해 변수 사이의 원인과 결과 관계를 추론한다.[^causal]

## 주요 연구 주제

### 불균형 자료와 반지도학습

ABC는 기존 반지도학습 모형이 배운 자료의 표현을 활용하되, 종류별 균형을 고려하는 분류기를 따로 학습한다. 정답이 없는 자료도 종류별로 같은 확률로 선택해 보조 분류기의 학습에 사용한다.[^p5] 연구실의 최근 목록에는 클래스 분포 불일치를 고려한 치우침 보정(CDMAD, Class-Distribution-Mismatch-Aware Debiasing)과 추정한 종류별 비율을 이용하는 재균형 방법도 있다.[^research] 클래스는 분류에서 구별하려는 대상의 종류를 뜻한다.

### 예측 불확실성과 분포 밖 탐지

증거 기반 딥러닝(Evidential Deep Learning)은 종류별 확률을 하나의 고정값으로만 내는 대신, 그 확률에 대한 분포를 예측해 불확실성을 표현하는 학습 방식이다.[^p2] 딥러닝은 여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야이며, 신경망은 연결된 계산 단위들이 가중치를 조절하며 입력과 출력의 관계를 배우는 모형이다. 연구실은 분류 확률에 유연한 분포를 사용하거나, 입력 주변에 학습 자료가 얼마나 분포하는지를 반영하는 방법을 제안했다.[^p2][^p3] Courtroom Analogy는 종류별 의견을 입력에 따른 가중치로 합쳐 불확실성을 해석할 수 있게 하는 방법이다.[^p1]

### 불규칙 관측을 다루는 시공간 모형

NLBST는 멀리 떨어진 위치의 관계를 직접 학습하는 시공간 모형이다. 베이지안 모형(자료를 보기 전의 가정과 관측 자료를 결합해 가능한 상태의 확률을 갱신하는 모형)을 사용해 예측과 불확실성을 함께 다룬다. 관측이 빠지거나 시각이 불규칙해도 순차적으로 상태를 갱신하고, 다시 학습하지 않고 관측하지 않은 위치의 값을 예측하도록 설계했다.[^p4]

### 공정 지식을 이용한 인과 구조 학습

인과 구조 학습은 변수 사이의 원인과 결과 관계를 자료에서 추론하는 방법이다. Order-based Causal Discovery for Multistage Processes의 arXiv 사전 공개본은 변수의 발생 단계에 관한 지식을 이용해 변수의 인과 순서를 정하고, 처음 만든 관계 모형에서 잘못 연결된 관계를 제거하는 방법을 제안한다. 여러 단계의 공정이 가진 계층과 순서 정보를 학습 과정에 반영한다.[^causal]

## 대표 논문

최근 연구의 불확실성 추정, 분포 밖 탐지, 불균형 자료 학습, 시공간 예측을 보여 주는 6편이다. 모두 김희영이 마지막 저자로 적힌 논문이며, 「쉽게 말하면」은 각 논문의 초록을 근거로 썼다. NLBST는 UAI 채택을 밝힌 arXiv 사전 공개본이다.[^p1][^p2][^p3][^p4][^p5][^p6]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [Courtroom Analogy: New Perspective on Uncertainty-Aware Classification](https://proceedings.mlr.press/v306/yoon26c.html) · ICML 2026 | 예측이 얼마나 불확실한지 나타내는 것에 더해, 불확실성이 어떤 구조로 합쳐졌는지 해석할 수 있게 하는 연구다. 종류별 의견을 확률분포로 표현하고 입력에 따라 그 의견을 합치는 가중치를 정하는 MoDEX(Mixture of Dirichlet EXperts) 구조를 제안했다. 이론적 성질을 제시하고 여러 평가 자료에서 불확실성 추정 성능을 보였다.[^p1] | 마지막 저자 |
| 2 | 2025 | [Uncertainty Estimation by Flexible Evidential Deep Learning](https://doi.org/10.52202/085713-3957) · NeurIPS 2025 | 기존 증거 기반 딥러닝은 종류별 확률이 디리클레 분포를 따른다고 가정한다. 디리클레 분포는 합이 일정한 여러 확률값에 대한 분포다. 이 연구는 이를 일반화한 유연한 분포를 예측하는 방법을 제안해 불확실성의 표현 범위를 넓혔다. 종류별 개수가 불균형하거나 자료에 잡음이 있는 조건을 포함한 평가에서 불확실성 추정 성능을 보였다.[^p2] | 마지막 저자 |
| 3 | 2024 | [Uncertainty Estimation by Density Aware Evidential Deep Learning](https://proceedings.mlr.press/v235/yoon24a.html) · ICML 2024 | 입력이 학습 자료와 떨어져 있다는 사실을 불확실성 계산에 반영하지 못하는 문제를 다룬다. 자료를 계산에 쓸 수 있게 표현한 공간에서 입력 주변의 밀도를 기존 모형의 출력과 결합하고, 분류 확률을 표현하는 방식도 바꾼 DAEDL(Density Aware Evidential Deep Learning)을 제안했다. 불확실성 추정과 분류에 관련된 여러 과제에서 성능을 보였다.[^p3] | 마지막 저자 |
| 4 | 2026 | [Nonlocal Bayesian Modeling of Continuous Spatio-Temporal Dynamics](https://doi.org/10.48550/arXiv.2606.14313) · arXiv 사전 공개본, UAI 2026 채택 | 관측 시각이 불규칙하고 관측 위치가 드문 상황에서, 멀리 떨어진 위치끼리의 관계까지 학습하는 NLBST를 제안했다. 관측이 들어올 때 상태를 갱신하며 관측하지 않은 위치도 다시 학습하지 않고 예측한다. 모의 자료와 실제 자료에서 예측 성능, 공간에 대한 일반화, 불확실성의 적절성을 평가했다.[^p4] | 마지막 저자 |
| 5 | 2021 | [ABC: Auxiliary Balanced Classifier for Class-imbalanced Semi-supervised Learning](https://papers.nips.cc/paper_files/paper/2021/hash/3953630da28e5181cffca1278517e3cf-Abstract.html) · NeurIPS 2021 | 정답이 없는 자료까지 학습할 때 종류별 개수가 다르면, 개수가 많은 종류로 기울어진 예측이 다음 학습에도 쓰이는 문제가 생긴다. 기존 모형이 배운 자료의 표현을 활용하는 보조 균형 분류기를 붙이고, 종류별 균형을 고려해 이 분류기를 학습하는 ABC를 제안했다. 여러 자료에서 불균형 반지도학습 성능을 평가했다.[^p5] | 마지막 저자 |
| 6 | 2021 | [Locally Most Powerful Bayesian Test for Out-of-Distribution Detection using Deep Generative Models](https://proceedings.neurips.cc/paper/2021/hash/7d3e28d14440d6c07f73b7557e3d9602-Abstract.html) · NeurIPS 2021 | 학습 자료와 성질이 다른 입력을 찾기 위해 베이지안 가설 검정에 기반한 탐지 점수를 제안했다. 비교하는 두 가정의 매개변수가 서로 가까운 조건에서, 다른 분포의 입력을 탐지할 확률을 최대화하도록 비교 가정을 정한다. 깊은 생성 모형에 적용하기 위한 수치 계산 방법도 제안하고 여러 자료에서 탐지 성능을 평가했다.[^p6] | 마지막 저자 |

## 교수와 전문 분야

김희영은 KAIST에서 산업공학 학사(2003년 2월)와 석사(2005년 2월)를, Georgia Institute of Technology에서 통계학 석사(2008년 5월)와 산업공학 박사(통계 전공, 2011년 8월)를 받았다. AT&T Labs에서 Senior Member of Technical Staff로 근무한 뒤 2013년 12월 KAIST 산업및시스템공학과 조교수로 부임했고, 2018년 3월부터 부교수로 적혀 있다. 교수 소개는 KAIST Endowed Chair Professor(원문 국문 칭호 「KAIST 지정 석좌교수」)와 인공지능대학원 Adjunct Professor를 함께 적는다.[^prof]

연구 관심은 통계·데이터 과학·인공지능·품질공학이다.[^prof] 대표 논문에서 드러나는 전문 분야는 확률 모형을 통한 예측 불확실성의 표현과 해석, 학습 분포에서 벗어난 입력의 탐지, 정답이 부족하고 종류별 비율이 고르지 않은 자료의 학습, 불규칙하게 관측한 시공간 자료의 예측이다.[^p1][^p4][^p5][^p6] Technometrics 부편집장(2025년 1월부터), IISE Transactions 부편집장(2020년 11월부터)을 맡고 있으며, IEEE Transactions on Automation Science and Engineering 부편집장으로 2021년 1월–2023년 12월 활동했다.[^prof]

## 응용 분야

연구실이 밝힌 응용 목표는 산업 시스템의 품질 향상이다.[^research] 최근 목록에는 웨이퍼 결함 지도와 칩 수준 불량 분류, 다단계 산업 공정의 시계열 이상 탐지, 모의실험 모형의 매개변수 추정이 올라 있다.[^research] 대표 연구는 자료 부족과 불균형 때문에 학습이 어려운 분류 문제, 예측의 불확실성을 함께 판단해야 하는 문제, 관측하지 않은 위치까지 예측해야 하는 시공간 자료에 연결된다.[^p1][^p4][^p5]

## 구성원

2026년 10월 31일 Members 페이지에 게시된 박사과정 6명과 석사과정 2명이다. 시작은 Entry의 연도이고, 연구 주제는 원문 표기다. 「대표 논문 참여」는 해당 논문의 전체 저자 목록과 같은 이름을 대조한 번호다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Junsub Jung | 박사과정 | 2021 | Causal Inference |  |  |
| Taeseong Yoon | 박사과정 | 2023 | Uncertainty Quantification |  | 1, 2, 3 |
| Taemin Park | 박사과정 | 2024 | Class Imbalanced Semi Supervised Learning |  |  |
| Jaeyeong Lee | 박사과정 | 2024 | Spatio-Temporal Modeling, Bayesian Deep Learning |  | 4 |
| Insoo Jung | 박사과정 | 2025 | Causal Inference |  |  |
| Seungjun Choi | 박사과정 | 2026 | Domain Generalization, Tabular Foundation Model |  |  |
| Kyeongjun Lee | 석사과정 | 2025 | Time-Series Analysis |  |  |
| Heeyeon Kim | 석사과정 | 2026 | Machine Learning | kimheeyeon@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 페이지의 박사 학위 11행과 석사 학위 30행이다. 연도 범위는 각각 2015–2026년, 2016–2026년이며, 학위별로 같은 사람이 반복되는 게시 항목도 그대로 실었다. 진로는 누리집 게시 시점의 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Woojin Soh | Ph.D. (2015) | NVIDIA | Development and Comparison of Parameter Design Methods for Multiple Performance Characteristics |
| Youngmin Lee | Ph.D. (2020) | Amazon Web Services (AWS) | Bayesian Nonparametric Models for Spatial Data Analysis |
| Taewon Jeong | Ph.D. (2021) | Samsung Electronics | Machine Learning Methods for Black-Box Optimization and Image Classification |
| Hyojoong Kim | Ph.D. (2022) | Assistant professor, Department of Industrial and Management Engineering, Myongji University | Machine Learning Methods for Contextual Anomaly Detection |
| Keunseo Kim | Ph.D. (2022) | Samsung Advanced Institute of Technology | Deep Learning Methods for Anomaly Detection and Robust Density Estimation |
| Jinman Bak | Ph.D. (2022) | Defense Agency of Technology and Quality (DTaQ) | Few-Shot Out-of-Distribution Detection and Classification for Mixed-Type Defect Patterns |
| Woojin Doo | Ph.D. (2022) | Samsung Electronics | Simultaneous Clustering and Feature Selection for High-dimensional Data |
| Hyuck Lee | Ph.D. (2024) | KRAFTON AI | Class-Imbalanced Semi-Supervised Learning |
| Heegeon Yoon | Ph.D. (2025) | Samsung Electronics | Deep Learning Models for Robust Training of Incomplete and Imbalanced Data |
| Eun-Yeol Ma | Ph.D. (2025) | Samsung AI Center | Deep Learning Methods for Discovering Causal Factors and Their Applications |
| Wonmo Koo | Ph.D. (2026) | Assistant Professor, Industrial Engineering, Pusan National University | Deep Learning Models for Multivariate Time Series Forecasting and Anomaly Detection |
| Jaehwan Lee | M.S. (2016) | SK Telecom | Hierarchical Spatially Varying Coefficient Process Models with Application to Housing Market Analysis |
| Yonghan Jung | M.S. (2016) | Assistant professor, School of Information Sciences, University of Illinois at Urbana-Champaign | Detection of Premature Ventricular Contraction Using Wavelet-Based Statistical ECG Monitoring |
| Hyojoong Kim | M.S. (2016) | Ph.D. student in iStat Lab | Functional Logistic Regression with Fused Lasso Penalty |
| Jinho Kim | M.S. (2016) | SK Hynix | Detection and Clustering of Mixed-Type Defect Patterns in Wafer Bin Maps |
| Keunseo Kim | M.S. (2016) | Ph.D. student in iStat Lab | TrailSense : A Crowdsensing System for Detecting Risky Mountain Trail Segments with Walking Pattern Analysis |
| Jihoon Chung | M.S. (2017) | Assistant professor, Department of Industrial Engineering, Hanyang University | Crime Risk Maps : Multivariate Analysis of Spatial Crime Data |
| Vinnam Kim | M.S. (2017) | Qualcomm | Spatio-Temporal Autoregressive Models of Monthly Air Passenger Flows |
| Kiryong Kyeong | M.S. (2018) | NCSoft | Classification of Mixed-Type Defects Patterns in Wafer Bin Maps Using Convolutional Neural Networks |
| Woojin Doo | M.S. (2018) | Ph.D. student in iStat Lab | Modeling the Probability of A Batter/Pitcher Matchup Dvent : A Bayesian Approach |
| Taeyoung Ko | M.S. (2019) | NICE | Fault Diagnosis for High-Dimensional Complex Process Using Semi-Dupervised Deep Convolutional Generative Models |
| Jeonghyun Choi | M.S. (2019) | TmaxSoft | Improving Baseball Pitch Type Classification Through Clustering of Pitchers |
| Eunyeol Ma | M.S. (2019) | Ph.D. student in iStat Lab | Phenotyping Obstructive Sleep Apnea Patients and Prognosis of Their Comorbidities Through Machine Learning Methods |
| Wonmo Koo | M.S. (2019) | Ph.D. student in iStat Lab | Bayesian Nonparametric Latent Class Model for Longitudinal Data |
| Jongwoo Ko | M.S. (2020) | Graduate School of AI, KAIST | Deep Gaussian Process Models for Integrating Multifidelity Experiments Having Non-stationary Relationship |
| Hyuk Lee | M.S. (2020) | Ph.D. student in iStat Lab | Semi-Supervised Multi-Label Learning for Classification of Wafer Bin Maps with Mixed-type Defect Patterns |
| Yunseung Hyun | M.S. (2020) |  | Memory-Augmented Convolutional Neural Networks with Triplet Loss for Imbalanced Wafer Defect Pattern Classification |
| Jonghyun Hwang | M.S. (2020) | Samsung Electronics | Variational Deep Clustering of Wafer Map Patterns |
| Sumin Park | M.S. (2021) | SK Hynix | A Bayesian Deep Learning Method for Predicting Highly Imbalanced Package Test Results |
| Sumin Kim | M.S. (2021) | Hyundai Card | Noisy Label Correction for Classification of Wafer Bin Maps with Mixed-Type Defect Patterns |
| Junsub Jung | M.S. (2021) | Ph.D. student in iStat Lab | Location Dependent Dirichlet Process Mixture Model for Clustering Spatially Correlated Time Series |
| Jaehyun Lee | M.S. (2022) | Samsung Electronics | Semi-Supervised Learning for Simultaneous Location Detection and Classification of Mixed-Type Defect Patterns in Wafer Bin Maps |
| Junchul Shin | M.S. (2022) | ClassOn | Open Set Recognition of Wafer Bin Map Defect Patterns |
| Hyeonwoo Kim | M.S. (2022) | Upstage | Weakly Supervised Semantic Segmentation for Classifying Wafer Chip-Level Defect Types |
| Hunsung Cho | M.S. (2023) | SK Hynix | Prediction of Highly Imbalanced Semiconductor Chip-Level Defects in Module Tests Using Multimodal Fusion and Logit Adjustment |
| Hyeonwoo Kim | M.S. (2023) | Samsung Electronics | Few-Shot Classification of Wafer Bin Maps Using Transfer Learning and Ensemble Learning |
| Jeongman Choi | M.S. (2023) | Samsung Electronics | Classification and Out-of-Distribution Detection for Wafer Bin Maps |
| Taemin Park | M.S. (2024) | Ph.D. student in iStat Lab | CDRA: Class Distribution-Based Re-Balancing Algorithm for Class-Imbalanced Semi-Supervised Learning |
| Jaeyeong Lee | M.S. (2024) | Ph.D. student in iStat Lab | Knowledge-Assisted Multi-Graph Structure Learning for Multivariate Time-Series Anomaly Detection in Multi-Stage Industrial Processes |
| Sanha Chang | M.S. (2026) | Alsemy | Robust Vessel Trajectory Prediction Under Long Missing Gaps |
| Seungjun Choi | M.S. (2026) | Ph.D. student in iStat Lab | Toward Uniformly Flat Minima for Domain Generalization |

## 최근 논문 목록 (2021–2026)

연구실 Research 페이지의 연도 구역을 따르며, 제목·저자·발표처는 연구실 표기다. 반지도학습과 예측 불확실성, 웨이퍼 결함 분류, 시공간 예측과 산업 공정 분석을 다룬다.[^research] 날짜 없이 게재 승인으로 적힌 학술지 항목은 연구실의 2026년 구역에 두고 「게재 승인」으로 표시했다. NLBST는 UAI 채택을 밝힌 arXiv 사전 공개본의 초록을 인용하며, 학회 목록에도 「채택」을 표시했다.[^p4]

**2026**

- W. Doo, J. Choi, and H. Kim. "Cluster-Based Classification for Mixed-Type Data Under Data Scarcity". *Statistical Analysis and Data Mining, 19(4), e70112*.
- H. Lee, T. Park, and H. Kim. "DAMEL: Dual-Axis Multi-Expert Learning for Class-Imbalanced Learning". *Knowledge-Based Systems, (게재 승인)*.
- J. Lee, T. Yoon, W. Koo, and H. Kim. "Knowledge-Assisted Multi-Graph Dependency Learning for Multivariate Time Series Anomaly Detection in Multi-Stage Industrial Processes". *IEEE Transactions on Automation Science and Engineering, (게재 승인)*.
- E.-Y. Ma, J. Jung, and H. Kim. "Order-based Causal Discovery for Multistage Processes". *IEEE Transactions on Knowledge and Data Engineering, (게재 승인)*.
- J. Lee and H. Kim. "Nonlocal Bayesian Modeling of Continuous Spatio-Temporal Dynamics". *Forty-Second Annual Conference on Uncertainty in Artificial Intelligence (UAI), Amsterdam, Netherlands, August 2026. (채택; 초록은 arXiv 사전 공개본)*.
- T. Yoon and H. Kim. "Courtroom Analogy: New Perspective on Uncertainty-Aware Classification". *International Conference on Machine Learning (ICML), Seoul, South Korea, July 2026*.
- H. Yoon and H. Kim. "Multimodal Deep Generative Model for Semi-Supervised Learning under Class Imbalance". *Technometrics, https://doi.org/10.1080/00401706.2026.2637593*.

**2025**

- T. Yoon and H. Kim. "Uncertainty Estimation by Flexible Evidential Deep Learning". *Conference on Neural Information Processing Systems (NeurIPS), San Diego, USA, December 2025*.
- H. Lee, T. Park, and H. Kim. "Learnable Logit Adjustment for Imbalanced Semi-Supervised Learning under Class Distribution Mismatch". *International Conference on Computer Vision (ICCV) 2025, Honolulu, Hawaii, USA, October 2025*.
- Y. Oh, H. Kim, and S. Kim. "TSSI: Time Series as Screenshot Images for multivariate time series classification using convolutional neural networks". *Computers & Industrial Engineering, 209, 111393*.
- E.-Y. Ma, U. Lee, and H. Kim. "Simultaneous Treatment Effect Estimation and Variable Selection for Observational Data". *IISE Transactions, 57(4), 380-392*.
- H. Kim, C. Park, and H. Kim. "Multi-task optimization with Bayesian neural network surrogates for parameter estimation of a simulation model". *Computational Statistics and Data Analysis, 204, 108097*.

**2024**

- T. Park, H. Lee, and H. Kim. "Rebalancing Using Estimated Class Distribution for Imbalanced Semi-Supervised Learning under Class Distribution Mismatch". *European Conference on Computer Vision (ECCV) 2024, Milan, Italy, September 2024*.
- T. Yoon and H. Kim. "Uncertainty Estimation by Density Aware Evidential Deep Learning". *International Conference on Machine Learning (ICML), Vienna, Austria, July 2024*.
- H. Kim, H. Yoon, and H. Kim. "Few-shot Classification of Wafer Bin Maps Using Transfer Learning and Ensemble Learning". *ASME Journal of Manufacturing Science and Engineering, 146(7), 070903*.
- H. Lee, H. Kim, and H. Kim. "Classification of Chip-level Defect Types in Wafer Bin Maps Using Only Wafer-level Labels". *ASME Journal of Manufacturing Science and Engineering, 146(7), 070902*.
- H. Lee and H. Kim. "CDMAD: Class-Distribution-Mismatch-Aware Debiasing for Class-Imbalanced Semi-Supervised Learning". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2024, Seattle, USA, June 2024*.
- W. Koo, E.-Y. Ma, and H. Kim. "Deep Latent Factor Model for Spatio-Temporal Forecasting". *Technometrics, 66(3), 470-482. (IISE Quality Control and Reliability Engineering (QCRE) Track Best Paper Competition Finalist)*.
- J. Choi, E.-Y. Ma, and H. Kim. "Simultaneous Classification and Out-of-Distribution Detection for Wafer Bin Maps". *Quality Engineering, 36(4), 713-725*.
- W. Doo and H. Kim. "Simultaneous Deep Clustering and Feature Selection via K-concrete Autoencoder". *IEEE Transactions on Knowledge and Data Engineering, 36, 2629-2642*.
- S. Kim and H. Kim. "Mixed-Type Defect Pattern Recognition in Noisy Labeled Wafer Bin Maps". *Quality Engineering, 36(4), 743-757*.
- J. Jung, S. Kim, and H. Kim. "Spatially-Correlated Time Series Clustering Using Location-Dependent Dirichlet Process Mixture Model". *Statistical Analysis and Data Mining, 17(1), e11649*.

**2023**

- H. Cho, W. Koo, and H. Kim. "Prediction of Highly Imbalanced Semiconductor Chip-Level Defects in Module Tests Using Multimodal Fusion and Logit Adjustment". *IEEE Transactions on Semiconductor Manufacturing, 36(3), 425-433*.
- H. Lee, J. Lee, and H. Kim. "Semi-supervised learning for simultaneous location detection and classification of mixed-type defect patterns in wafer bin maps". *IEEE Transactions on Semiconductor Manufacturing, 36(2), 220-230*.
- H. Kim and H. Kim. "Contextual anomaly detection for multivariate time series data". *Quality Engineering, 35(4), 686-695*.
- K. Kim, E.-Y. Ma, J. Choi, and H. Kim. "Inverse-Reference Priors for Fisher Regularization of Bayesian Neural Networks". *Thirty-Seventh AAAI Conference on Artificial Intelligence (AAAI-23), Washington, DC, USA, February 2023*.
- H. Kim and H. Kim. "Contextual anomaly detection for high-dimensional data using Dirichlet process variational autoencoder". *IISE Transactions, 55(5), 433-444*.
- H. Yoon and H. Kim. "Label-Noise Robust Deep Generative Model for Semi-Supervised Learning". *Technometrics, 65(1), 83-95*.
- S. Park, K. Kim, and H. Kim. "Prediction of highly imbalanced semiconductor chip-level defects using uncertainty-based adaptive margin learning". *IISE Transactions, 55(2), 147-155*.
- H. Kim and H. Kim. "Deep embedding kernel mixture networks for conditional anomaly detection in high-dimensional data". *International Journal of Production Research , 61(4), 1101-1113*.

**2022**

- J. Ko and H. Kim. "Deep Gaussian process models for integrating multifidelity experiments with non-stationary relationships". *IISE Transactions, 54(7), 686-698*.
- W. Doo and H. Kim. "Simultaneous band selection and segmentation of hyperspectral images via a mixture of finite maximum margin mixtures". *International Journal of Remote Sensing , 43(6), 2296-2314*.
- W.-S. Yun, S. Ko, M. Byun, H. Kim, I.-C. Moon, and T.-E. Lee. "Toward robust battle experimental design for command and control of mechanized infantry brigade". *Military Operations Research, 27(1), 45-72*.

**2021**

- H. Lee, S. Shin, and H. Kim. "ABC: Auxiliary Balanced Classifier for Class-imbalanced Semi-supervised Learning". *Conference on Neural Information Processing Systems (NeurIPS) 2021*.
- K. Kim, J. Shin, and H. Kim. "Locally Most Powerful Bayesian Test for Out-of-Distribution Detection using Deep Generative Models". *Conference on Neural Information Processing Systems (NeurIPS) 2021*.
- P. Tang, H. Jiang, H. Kim, and X. Deng. "Robust estimation of sparse precision matrix using adaptive weighted graphical Lasso approach". *Journal of Nonparametric Statistics, 33, 249-272*.
- W. Doo and H. Kim. "Bayesian Variable Selection in Clustering High-Dimensional Data via a Mixture of Finite Mixtures". *Journal of Statistical Computation and Simulation, 91, 2551-2568*.

## 수상과 선정

교수 소개의 Awards & Honors에 게시된 항목 중 2021년 10월 13일–2026년 10월 13일에 해당하는 수상·석좌교수 선정·논문 경진대회 최종 후보 항목이다. Finalist는 최종 후보 표기로, 수상과 구분한다.[^prof]

- 2025-05 · IISE Quality Control and Reliability Engineering (QCRE) Track Best Paper Competition Finalist, IISE Annual Conference
- 2025-03 · KAIST Endowed Chair Professor (KAIST 지정 석좌교수)
- 2024-05 · IISE Quality Control and Reliability Engineering (QCRE) Track Best Paper Competition Finalist, IISE Annual Conference
- 2023-12 · Academic Excellence Award, Department of Industrial and Systems Engineering, KAIST
- 2022-02 · KAIST Academic Excellence Award (Outstanding Faculty Award in Commemoration of the 51st Founding Anniversary), KAIST (KAIST 학술상)

## 연락과 위치

- 교수 사무실: E2-1 4214호[^prof]
- 교수 전화: +82-42-350-3125[^prof]
- 교수 이메일: heeyoungkim@kaist.ac.kr[^gsds]
- 우편 주소: 34141 대전광역시 유성구 대학로 291 KAIST[^prof]

## 각주
[^p1]: T. Yoon, H. Kim, Proceedings of the 43rd International Conference on Machine Learning 306, 149642-149676 (2026). <https://proceedings.mlr.press/v306/yoon26c.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v306/yoon26c.html>. 관측일 2026-10-31.
[^p2]: T. Yoon, H. Kim, Advances in Neural Information Processing Systems 38 (2025). <https://doi.org/10.52202/085713-3957> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2025/hash/abf0ea3ae33d1a931483e327ff8d94f8-Abstract-Conference.html>. 관측일 2026-10-31.
[^p3]: T. Yoon, H. Kim, Proceedings of the 41st International Conference on Machine Learning 235, 57217-57243 (2024). <https://proceedings.mlr.press/v235/yoon24a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/yoon24a.html>. 관측일 2026-10-31.
[^p4]: J. Lee, H. Kim, arXiv:2606.14313 (UAI 2026 채택) (온라인 2026-06-12). <https://doi.org/10.48550/arXiv.2606.14313> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2606.14313>. 관측일 2026-10-31.
[^p5]: H. Lee, S. Shin, H. Kim, Advances in Neural Information Processing Systems 34 (2021). <https://papers.nips.cc/paper_files/paper/2021/hash/3953630da28e5181cffca1278517e3cf-Abstract.html> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2021/hash/3953630da28e5181cffca1278517e3cf-Abstract.html>. 관측일 2026-10-31.
[^p6]: K. Kim, J. Shin, H. Kim, Advances in Neural Information Processing Systems 34 (2021). <https://proceedings.neurips.cc/paper/2021/hash/7d3e28d14440d6c07f73b7557e3d9602-Abstract.html> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper/2021/hash/7d3e28d14440d6c07f73b7557e3d9602-Abstract.html>. 관측일 2026-10-31.
[^prof]: Engineering Data Science Lab, Professor. <https://eds.kaist.ac.kr/professor/>. 관측일 2026-10-31.
[^research]: Engineering Data Science Lab, Research. <https://eds.kaist.ac.kr/research/>. 관측일 2026-10-31.
[^members]: Engineering Data Science Lab, Members. <https://eds.kaist.ac.kr/members/>. 관측일 2026-10-31.
[^alumni]: Engineering Data Science Lab, Alumni. <https://eds.kaist.ac.kr/alumni/>. 관측일 2026-10-31.
[^gsds]: KAIST 데이터사이언스대학원, People, 김희영 항목의 이메일·전화·홈페이지. <https://gsds.kaist.ac.kr/people>. 관측일 2026-10-30.
[^causal]: E.-Y. Ma, J. Jung, H. Kim, Order-based Causal Discovery for Multistage Processes, arXiv:2607.03971 (2026-07-04). <https://doi.org/10.48550/arXiv.2607.03971>. 초록 기준(arXiv 사전 공개본). 초록 원문 <https://arxiv.org/abs/2607.03971>. 관측일 2026-10-31.

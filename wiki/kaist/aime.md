# 생산혁신인공지능연구실 (Artificial Intelligence for M Excellence Lab, AIME)

**KAIST 산업및시스템공학과·데이터사이언스대학원 · 이종석 부교수**

- 분야: 제조·생산 혁신을 위한 기계학습과 최적화[^about]
- 대분야: 컴퓨팅·AI, 산업·시스템
- 태그: 스마트 제조[^about][^project70], 설명 가능한 AI(XAI)[^about], 수리 최적화·최적화 알고리즘[^project70], 인쇄 전자·용액 코팅 공정[^p1], 이상·변화점 탐지[^p3]
- 홈페이지: <https://aime.kaist.ac.kr>[^home]

> 제조 현장의 자료로 공정과 설비를 이해하고, 사전 지식·예측의 신뢰성·설명 가능성을 반영한 인공지능과 최적화 방법으로 생산과 운영을 개선하는 연구실이다.[^about]

## 무엇을 연구하나

AIME는 기계학습(자료에서 규칙을 배우고 예측이나 판단에 사용하는 방법)과 최적화(주어진 조건에서 목적에 맞는 최선의 해를 찾는 방법)를 제조·생산 문제에 연결한다. 연구실 이름의 M은 제조, 기계, 재료, 방법과 그 밖의 제조·생산 혁신 요소를 뜻한다. 현장의 문제를 풀면서 새로운 학습 방법도 함께 개발하고, 자료에 근거한 의사결정과 지능형 시스템을 만드는 것이 연구 방향이다.[^about]

한 갈래는 사전 지식과 물리적 조건을 학습 모형에 반영하는 것이다. 단조성(입력이 일정한 방향으로 바뀔 때 출력도 정해진 방향을 유지하는 성질)이나 볼록성(두 점 사이의 함수값이 두 점의 값을 잇는 직선보다 높지 않은 성질)처럼 모형이 따라야 할 조건을 신경망(연결된 계산 단위의 관계를 자료로 학습하는 모형)에 넣는다. 다른 갈래에서는 데이터 분포의 변화를 살펴 재학습 시점을 정하고, 모형의 작동 원리와 예측 근거를 설명하는 방법을 연구한다.[^about]

제조 현장에서 다루는 표형식 자료와 시계열(시간 순서에 따라 기록한 자료)도 연구 대상이다. 영상이나 글을 위해 발전한 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야)을 이런 자료에 맞게 바꾸며, 학습 결과를 공정 제어와 운영 최적화로 연결한다. 제조 특화 학습 알고리즘 과제에서는 예측 모형을 학습하고 설비의 제어 문제를 최적화 문제로 나타내는 연구를 제시한다.[^about][^project70]

인쇄 전자(재료를 인쇄해 전자 기능을 갖는 막·배선·소자를 만드는 기술)의 품질 평가가 구체적인 사례다. 2025년 논문은 딥러닝과 공간 연관성(위치에 따라 놓인 값들 사이의 관계)을 이용해 인쇄 품질을 실시간으로 수치화하는 방법을 제안했다. 이렇게 얻은 품질값을 반응표면법(입력 조건과 결과 사이의 관계를 근사한 모형으로 조건을 찾는 방법)에 연결해 공정 설정을 정하는 데 활용했다.[^p1]

학습 자료와 분포가 다른 자료인 분포 밖 자료(Out-of-Distribution, OOD)에 대한 예측의 신뢰성도 다룬다. 한 논문은 자료를 범주로 나누는 분류 모형에서 분류 마진(서로 다른 범주를 구분하기 위해 두는 여유 간격)을 넓히고 완만하게 형성하는 학습 방법으로 낯선 자료에 대한 과신을 완화했다.[^p2] 다른 논문은 방공 장비의 신호에서 시간과 장비에 따른 분포 변화를 다뤘다. 정규화(자료의 값을 정해진 척도나 기준에 맞추는 처리)와 시계열 생성 모형(시간 순서에 따른 자료의 특징을 배워 새 자료를 만드는 모형)을 결합해 분포가 변하는 상황에서의 이상 탐지 성능을 평가했다.[^p3]

## 주요 연구 주제

### 사전 지식과 설명 가능성을 갖춘 학습

입력과 출력이 따라야 하는 조건을 모형에 반영하고, 예측의 근거와 작동 원리를 사람이 이해할 수 있도록 하는 연구다. 연구실은 단조·볼록 신경망과 국지적으로 해석 가능한 전문가 모형의 결합, 예측 신뢰도를 구체적인 연구 대상으로 든다.[^about]

### 변화하는 현장 자료에 맞춘 예측

자료가 생기는 환경이 달라져도 예측 모형을 계속 사용할 수 있도록 데이터 분포를 감시하고 재학습을 결정한다. 표형식 시계열 자료에 맞춘 학습 방법을 개발하며, 학습 때 접하지 못한 자료에 대한 대응도 연구한다.[^about] 분포 밖 자료에 대한 과신 완화와 시간·장비 변화에 대응하는 이상 탐지는 그 구체적인 연구 사례다.[^p2][^p3]

### 제조 품질 평가와 설비 운영

품질 관리, 결함 탐지, 장비 성능과 자원 사용의 최적화, 유지보수 예측을 제조 응용으로 다룬다. 인쇄 품질을 정량화하는 논문과 설비 제어를 위한 학습 알고리즘 과제는 예측 결과를 현장 조건의 선택으로 연결하는 사례다.[^about][^p1][^project70]

## 대표 논문

제조 품질 평가, 낯선 자료에 대한 예측의 신뢰성, 시계열 이상 탐지를 보여 주는 세 편이다. 표의 연도·발표처는 연구실 표기이며, 「쉽게 말하면」은 각 논문 초록만을 근거로 썼다.[^p1][^p2][^p3]

| 번호 | 연도 | 논문 | 발표처 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2025 | [Quantifying Printing Quality for Printed Electrodes via Deep Learning and Spatial Association: Empowering Process Optimization](https://doi.org/10.1002/aisy.202500178)[^p1] | *Advanced Intelligent Systems* 7(11), 2500178 | 인쇄된 전극의 품질을 사람의 눈으로 평가하는 대신, 딥러닝과 공간 연관성을 이용해 실시간으로 수치화하는 방법을 제안했다. 품질값을 반응표면법에 연결해 인쇄 공정의 설정을 정하는 데 활용했다. |
| 2 | 2025 | [Gently Sloped and Extended Classification Margin for Overconfidence Relaxation of Out-of-Distribution Samples](https://doi.org/10.1109/tnnls.2024.3496473)[^p2] | *IEEE Transactions on Neural Networks and Learning Systems* 37(7), 12854-12865 | 학습 자료와 분포가 다른 자료에도 모형이 과도한 확신을 보이는 문제를 다뤘다. 자료의 특징을 수치로 나타낸 공간에서 분류 마진을 넓히고 완만하게 형성하는 방법을 제안해 이러한 과신을 완화했다. |
| 3 | 2025 | [Robust Anomaly Detection for RF Signals in Air Defense Systems Under Out-of-Distribution Shifts](https://doi.org/10.1109/access.2025.3647464)[^p3] | *IEEE Access* 13, 217222-217231 | 시간이나 장비가 달라져 신호의 분포가 변할 때에도 이상을 찾도록, 정규화와 시계열 생성 모형을 결합했다. 실험에서 원래 신호를 복원할 때의 오차를 줄이고 여러 분포 변화 상황의 이상 탐지 성능을 개선했다. |

## 교수와 전문 분야

이종석(Jong-Seok Lee)은 KAIST 산업및시스템공학과·데이터사이언스대학원 부교수다. 2024년 9월 KAIST에 부임했으며, 앞서 성균관대학교에서 2012년 3월부터 2018년 2월까지 조교수, 2018년 3월부터 2024년 8월까지 부교수로 근무했다. 2009년 아이오와주립대학교에서 산업공학 박사 학위를 받았다.[^professor]

전문 분야는 현장 자료를 활용한 기계학습 방법 개발과 제조·서비스 시스템의 최적화다. 사전 지식의 반영, 설명 가능한 예측, 변화하는 자료에 대응하는 학습을 제조 품질 관리와 설비 운영에 연결한다.[^about][^project70][^p1]

## 응용 분야

제조 분야에서는 공정 제어와 실시간 의사결정, 장비 성능과 수율의 최적화, 에너지 관리, 품질 관리, 고장 예측과 이상 탐지를 다룬다. 서비스 분야에서는 운영 과정과 자원 배분·일정의 최적화, 서비스 장비의 유지보수, 차량 운영을 위한 가격 예측, 금융 사기 탐지를 응용 대상으로 제시한다.[^about]

## 구성원

2026년 10월 31일 관측한 Students 목록의 12명이다. 과정·기간·연구 주제와 학교 이메일은 연구실 게시 표기이며, 시작 시점에는 KAIST 부임 이전의 연구실 활동도 포함된다. 대표 논문 참여는 논문의 전체 저자 목록과 같은 이름을 대조한 표시다.[^students]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Hyunho Kim (김현호) | 박사과정 | Mar.2018 ~ Present | Deep Learning, Domain-knowledge Informed Neural Networks, Explainable & Interpretable AI, | hyunho.kim@kaist.ac.kr |  |
| Juhuhn Kim (김주헌) | 박사과정 | Mar.2021 ~ Present | Machine Learning, Effective Representation of Data, Intelligent Manufacturing System | juhuhn@kaist.ac.kr | 1 |
| Francis Kim (김철규) | 박사과정 | Mar.2023 ~ Present | Heterogeneous matrix factorization and its application to transfer learning | kimfrancis.cg@kaist.ac.kr |  |
| Hyungkwon Lee (이형권) | 박사과정 | Mar.2023 ~ Present | Domain Generalization and Adaptation, Representation Learning, Distribution Modeling and Analysis | hyungkwon@kaist.ac.kr | 3 |
| Chanho Kim (김찬호) | 석사과정 | Mar.2024 ~ Present | To be determined | chanh99kim@kaist.ac.kr |  |
| Dohyun Bu (부도현) | 박사과정 | Mar.2024 ~ Present | Physics- and Constraint-Informed Learning, Theory-Grounded Learning Frameworks, Efficient Learning… | dohyun.bu@kaist.ac.kr |  |
| Yujung Byun (변유정) | 석사과정 | Feb.2025 ~ Present | To be determined | yujung4169@kaist.ac.kr |  |
| Hyewon Ryu (유혜원) | 석사과정 | Feb.2025 ~ Present | To be determined | hw.ryu@kaist.ac.kr | 3 |
| Kyungmin Ryu (류경민) | 석사과정 | Mar.2026 ~ Present | To be determined | kminryu@kaist.ac.kr |  |
| Minhee Hong (홍민희) | 석사과정 | Mar.2026 ~ Present | To be determined | minhee.h@kaist.ac.kr |  |
| Jinah Lee (이진아) | 석사과정 | Mar.2026 ~ Present | To be determined | yjinah@kaist.ac.kr |  |
| Keunjun Jang (장근준) | 석사과정 | Aug.2026 ~ Present | To be determined | kjun.jang@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 목록의 박사 6명과 석사 15명이다. 학위 연도는 2014–2025년이며, KAIST 부임 이전의 졸업생도 포함한다. 학위·진로·학위 논문 제목은 목록의 게시 표기다.[^alumni][^alumni2]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Yeontark Park (박연탁) | PH.D. (2022) | LG Energy Solution | Area Under ROC Curve as A Learning Objective for Balanced and Imbalanced Data Classification: Develo… |
| Jaesub Yun (윤재섭) | PH.D. (2023) | Hudson AI | Decision Boundary-Aware Training of Neural Networks for Imbalanced Data Classification |
| Minseok Han (한민석) | PH.D. (2023) | 포스코홀딩스 미래기술연구원 | Temporal Peak-Managing and Clustering System for Sustainable Learning |
| Doo Yeol Lee (이두열) | M.S. (2021) | Hyundai Elevator R&D본부 군제어팀 | Multiple indefinite kernel learning by integrating spectrum transformation techniques |
| Jisoo Kim (김지수) | M.S. (2022) | LG Energy Solution | Transfer Learning for Defect Detection of New Products Under Frequent Product Renewal: A Die-Casting… |
| Changjin Kim (김창진) | M.S. (2014) | 한국광해관리공단 | 공공기관 R&D사업의 효율성 분석 : 한국광해관리공단 사례를 중심으로 Efficiency analysis of R&D projects in public institution us… |
| Gunbum Lee (이건범) | PH.D. (2015) | 교수, 한국폴리텍대학 서울정수캠퍼스 | 연구소기업의 성장요인분석 / An analysis of growing factors of the research institute companies |
| Hanhee Youn (윤한희) | M.S. (2015) | KB증권 | 불균형 데이터 분류를 위한 AUC 기반의 부스팅 알고리즘 |
| Sungho Lee (이성호) | M.S. (2015) | 상무, Deloitte Consulting Korea | 불균형 데이터 분류를 위한 반복적 인공데이터 생성기법/A Repetitive Method of Artificial Data Generation for Unbalanced Data … |
| Taeheung Kim (김태흥) | PH.D. (2018) | 삼성전자 DS 혁신센터 | An optimization approach to learning weighted naive Bayesian classifiers |
| Donguk Kim (김동욱) | M.S. (2018) | Korea Credit Bureau | Gradient-Boosting 기반의 구성적 RBFN 학습 알고리즘 / Constructive RBFN Learning Algorithm based on Gradient-Boos… |
| Bonsung Gu (구본성) | M.S. (2018) | Audit division, KIA | Learning decorrelated weak learners in adaptive boosting |
| Hoeseon Lee (이회선) | PH.D. (2018) | 교수, 한국폴리텍대학 신기술교육원 | 흡수역량이 기업 핵심역량 및 경영성과에 미치는 영향에 관한 연구 : 직 · 간접효과 검증 / A study on the effects of absorptive capacity on… |
| Jaeho Lee (이재호) | M.S. (2020) | Research Engineer, Hyundai Elevator | A Data-driven Approach to Modeling Multiple Customer Satisfactions for New Product Development Using… |
| Minsoo Kim (김민수) | M.S. (2022) | 삼성전자 | Detection of Field Failure Chips by Ensemble Learned from Different Chip Areas |
| Jaemin Lee (이재민) | M.S. (2022) | 삼성전자 DS 혁신센터 | Convergence Analysis of Connection Center Evolution and Faster Clustering |
| Joohyung Lee (이주형) | M.S. (2023) | LG Energy Solution | Monotonicity-Incorporative Neural Network Training for Response Surface Methodology |
| Taewook Kim (김태욱) | M.S. (2024) | LG Energy Solution | Gently-sloped and extended classification margin for overconfidence relaxation of out-of-distributio… |
| Seokjun Kim (김석준) | M.S. (2022) | 우아한형제들(배달의민족) 데이터분석 | Conditional Tabular GAN combined with CAT2VEC to learn from mixed and class-imbalanced data |
| Soosang Eom (엄수상) | M.S. (2024) | Current Position: POSCO DX | Enhancing Deep-Learning-as-a-Service with Optimized Architectures: A Framework Focused on Service-Le… |
| Bonhyeok Ku (구본혁) | M.S. (2025) | 딜로이트 그룹 컨설팅부문 (AI&DATA) | Noise-Aware Weight Updating in AdaBoost for Handling Mislabeled Data |

## 최근 논문 목록 (2021–2026)

학술지 논문 17편과 학회 논문·발표 58건으로, 2021–2026년 항목이다. 학회 항목은 Conference 목록의 55건과 소식에서 채택을 알린 NeurIPS 2026 세 편이며, 이 세 편은 「채택」으로 표시했다. 이종석 교수의 KAIST 부임 이전 항목도 포함한다. 제목·저자·발표처는 연구실 게시 표기이고, 상세 글에 완전한 표기가 있는 항목은 그 표기를 따른다. 별표는 목록이 공동 기여로 밝힌 표시다.[^journal][^journal2][^journal-details][^conference][^conference2][^conference3][^conference4][^neurips][^health]

**2026**

- 김현호, 부도현, 이종석. "A Unified Neural Architecture for Variable-Wise Shape Constraints". *NeurIPS 2026 (채택)*.
- 이형권, 유혜원, 이종석 (이형권·유혜원 공동 제1저자). "Learning Informative Invariant Representations via Hierarchical Latent Decomposition". *NeurIPS 2026 (채택)*.
- 부도현, 김찬호, 최석운, 이종석 (부도현·김찬호 공동 제1저자). "Sparsely-Supervised Data Assimilation via Physics-Informed Schrödinger Bridge". *NeurIPS 2026 (채택)*.
- Ku, B. and Lee, J.-S. "Noise-Aware Weight Updating in AdaBoost for Handling Mislabeled Data". *Pattern Recognition, 177, 113240*.
- H. Lee\*, C. Kim\*, C. G. F. Kim, and J.-S. Lee. "Optimizing Length-Varying Process Profiles under Delayed Quality Feedback". *2026 IEEE CASE (22nd International Conference on Automation Science and Engineer…*.
- Y. Byun, D. Bu, K. Ryu, and J.-S. Lee. "Price-Constrained Demand Forecasting with Zero-inflated Observations for Replenishment and Pricing Decision". *2026 IEEE CASE (22nd International Conference on Automation Science and Engineer…*.
- S. Lee, J. Kim, D. Lee, and J.-S. Lee. "Improving Elevator Group Control through Data-Driven Learning of Time-Varying Demand and Simulation-Based Parameter Optimization". *2026 IEEE CASE (22nd International Conference on Automation Science and Engineer…*.
- H. Ryu, H. Lee, H. Park and J.-S. Lee. "도메인 일반화를 위한 계층적 잠재변수 분리 방법". *2026 Spring Conference of Korean Institute of Industrial Engineers*.
- Y. Byun, D. Bu and J.-S. Lee. "수렴 안정성을 고려한 비선형 제약 충족 문제의 기울기 기반 해 탐색 방법". *2026 Spring Conference of Korean Institute of Industrial Engineers*.
- D. Bu\*, Y. Byun\*, and J.-S. Lee. "Harmonized Cone for Feasible and Non-conflict Directions in Training Physics-Informed Neural Networks". *International Conference on Learning Representations (ICLR 2026)*.
- D. Bu, H. Kim, and J.-S. Lee. "Covariate-Guided Clusterwise Linear Regression for Generalization to Unseen Data". *International Conference on Learning Representations (ICLR 2026)*.

**2025**

- Ryu, H., Lee, H., Park, H., Oh., J., and Lee, J.-S. "Robust Anomaly Detection for RF Signals in Air Defense Systems Under Out-of-Distribution Shifts". *IEEE Access, 13, 217222-217231*.
- J. Kim, Y. Jung, S. Parajuli, S. Shrestha, J. Park, G. Cho, and J.-S. Lee. "Quantifying Printing Quality for Printed Electrodes via Deep Learning and Spatial Association: Empowering Process Optimization". *Advanced Intelligent Systems, 7(11), 2500178*.
- T. Kim and J.-S. Lee. "Gently Sloped and Extended Classification Margin for Overconfidence Relaxation of Out-of-Distribution Samples". *IEEE Transactions on Neural Networks and Learning Systems, 37(7), 12854-12865*.
- D. Bu, J. Han, S. Kwon, Y. So  and J. -S. Lee. "Subject-Adaptive Sparse Linear Models for Interpretable Personalized Health Prediction from Multimodal Lifelog Data". *2025 ICTC (16th International Conference on Information and Communication Technology Convergence)*.
- H. Lee, H. Ryu, Y. Kim, H. Park, J. Oh and J.-S. Lee. "An Empirical Investigation of Efficient Anomaly Detection Techniques for Resource-Constrained Systems". *2025 INFORMS Annual Meeting*.
- J. Kim and J.-S. Lee. "Covariance Aligned Gaussian Process". *2025 INFORMS Annual Meeting*.
- Y. Byun and J.-S. Lee. "Improving Few-Shot Tabular Regression via Latent Task Discovery and Meta-Learning". *2025 INFORMS Annual Meeting*.
- H. Ryu, H. Lee and J.-S. Lee. "Domain-General Reconstruction through Invariant and Specific Representations". *2025 INFORMS Annual Meeting*.
- H. Kim and J.-S. Lee. "Training Neural Networks with User-Defined Dimension-Specific Unimodality". *2025 INFORMS Annual Meeting*.
- C. Kim and J.-S. Lee. "Multi-Objective Trajectory Generation for Offline Model-Based Optimization". *2025 INFORMS Annual Meeting*.
- D. Bu and J.-S. Lee. "Stochastic Dual Cone Gradient Descent with Adaptive Moments: A Robust Approach to Conflict-Free Multi-Objective Optimization". *2025 INFORMS Annual Meeting*.
- J.-S. Lee. "Learning Monotonic Neural Networks for Data-Driven Control in Steel Manufacturing". *2025 IEEE CASE (21st International Conference on Automation Science and Engineer…*.
- J. Kim, Y. Jung, S. Parajuli, S. Shrestha, J. Park, G. Cho, and J.-S. Lee. "Quantifying Overlay Printing Registration Accuracy with Object Keypoint Detection for Automated Process Control in FPE Printing". *2025 IEEE CASE (21st International Conference on Automation Science and Engineer…*.
- B. Ku and J.-S. Lee. "오표기 데이터에 강건한 새로운 아다부스트 분류 방법". *2025 Spring Conference of Korean Institute of Industrial Engineers*.
- D. Bu and J.-S. Lee. "벡터 양자화를 활용한 군집별 선형 회귀 모형 학습 방법". *2025 Spring Conference of Korean Institute of Industrial Engineers*.
- J. Kim, Y. Jung, S. Parajuli, S. Shrestha, J. Park, G. Cho, and J.-S. Lee. "Automated OPRA Quantification in R2R Gravure Printing Using Deep Neural Network". *The 35th International Conference on Molecular Electronics and Devices (IC ME&D …*.
- H. Lee, Y. Kim, H. Park, S. Cho, J. Oh, and J.-S. Lee. "Radio Frequency Signal-Based Health Monitoring and Anomaly Detection in Air Defense Tracking Systems: A Case Study". *2025 Spring Conference of Korean Society for Internet Information*.
- H. Moon, D. Pradhan, J. Kim, Y. Jung, J. Park, G. Cho, J.-S. Lee, and J. Lee. "Response Surface-Based Optimization of Gravure Cell Design in Roll-to-Roll Printing". *2025 KSME Fluid Engineering Division Spring Conference*.
- H. Moon, D. Pradhan, J. Kim, Y. Jung, J. Park, G. Cho, J.-S. Lee, and J. Lee. "Gravure Cell Design of Roll-to-Roll Printing via Response Surface Optimization". *2025 KFPE Spring Meeting*.

**2024**

- "PFSC: Parameter-free sphere classifier for imbalanced data classification". *Expert Systems with Applications, 249-C, 123822*.
- "Learning from class-imbalanced data using misclassification-focusing generative adversarial networks". *Expert Systems with Applications, 240, 122288*.
- C. Kim, D. Bu, B. Koo, Y. So, G. Kim, W.-J. Lee, and J.-S. Lee. "Single-Attempt Hyperparameter Optimization Using Graph Neural Networks". *2024 INFORMS Annual Meeting*.
- F. Kim, D. Bu, C. Kim, and J.-S. Lee. "Utilizing Large Language Models for Improved Missing Data Handling in Classification Tasks". *2024 INFORMS Annual Meeting*.
- D. Bu, B. Koo, C. Kim, G. Kim, M. Jeong, Y. So, and J.-S. Lee. "Enhancing Representation Ability of CNN via Color Inversion Channel". *2024 INFORMS Annual Meeting*.
- H. Lee and J.-S. Lee. "Noise-Resistant Anomaly Detection in Multivariate Time Series Using Feature Correlation". *2024 INFORMS Annual Meeting*.
- H. Kim and J.-S. Lee. "Training Neural Networks with User-Defined Dimension-Specific Convexity". *2024 INFORMS Annual Meeting*.
- H. Kim and J.-S. Lee. "Scalable Monotonic Neural Networks". *International Conference on Learning Representations (ICLR 2024)*.
- S. Eom and J.-S. Lee. "반응 표면 방법론을 통한 서비스 아키텍처 구성 최적화 방법". *2024 Spring Conference of Korean Institute of Industrial Engineers*.
- D. Bu and J.-S. Lee. "국지적 단조성을 보장하는 전문가 혼합 모형 학습 방법". *2024 Spring Conference of Korean Institute of Industrial Engineers*.
- H. Lee, C. F. Kim, H.-K. Park, Y.-H. Kim, S.-H. Cho, and J.-S. Lee. "방공 탐지추적장치의 계측 정보를 활용한 건전성 모니터링 방안 연구". *2024 Spring Conference of Korean Institute of Industrial Engineers*.
- D. Bu, C. Kim, and J.-S. Lee. "전단사적 변환에 대응 가능한 회귀 모형 추정 방법". *2024 Spring Conference of Korean Institute of Industrial Engineers*.
- J. Kim, S. Shrestha, Y. Jung, J. Park, S. Parajuli, G. Cho, and J.-S. Lee. "Quantifying Print Quality of Printed Electrodes Using Object Detection and Spatial Association for Process Monitoring and Optimization". *2024 KFPE Spring Meeting*.
- H. Lee, C. F. Kim, M.-S. Kim, Y.-H. Kim, H.-K. Park, and J.-S. Lee. "Fault Detection of Air Defense Radar Systems Using Machine Learning". *IEEE International Conference on Ubiquitous Information Management and Communica…*.

**2023**

- "BAND: BAgging Noise Detectors with application to semiconductor wafer denoising". *Applied Soft Computing, 147, 110742*.
- "Graph-based density peak merging for identifying multi-peak clusters". *Applied Soft Computing, 146, 110657*.
- "A Systematic Approach to Identify Shipping Emissions Using Spatio-Temporally Resolved TROPOMI Data". *Remote Sensing, 15(13), 3453, 1-26*.
- "Learning From Imbalanced Data Using Triplet Adversarial Samples". *IEEE Access, 11, 31467-31478*.
- "Temporal Peak-Management and Clustering System for Sustainable Learning With Application to the Excimer Laser Annealing Process". *IEEE Access, 11, 24535-24544*.
- "Maximizing AUC to learn weighted naive Bayes for imbalanced data classification". *Expert Systems with Applications, 217, 119564*.
- J. Kim, S. Shrestha, Y. Jung, J. Park, S. Parajuli, G. Cho, and J.-S. Lee. "An AI-Based Approach to Quantifying Printing Quality of Flexible Printed Electronics with Application to Process Optimization". *2023 KFPE Fall Meeting*.
- C. F. Kim, M. Han, and J.-S. Lee. "Enhancing Interpretability and Prediction Reliability in Regression Tasks Through Constrained Mixture of Experts". *2023 INFORMS Annual Meeting*.
- H. Lee, J. Yun, and J.-S. Lee. "Incorporating Prior Function Belief into Neural Networks Through Dropout and Negative Correlation Learning". *2023 INFORMS Annual Meeting*.
- H. Kim and J.-S. Lee. "Discovering True Optimal Solutions from Response Surface Models with Error". *2023 INFORMS Annual Meeting*.
- H. Kim, M. Han, and J.-S. Lee. "단조성 보장을 위한 국지 선형 앙상블 모델". *2023 Spring Conference of Korean Institute of Industrial Engineers*.
- J.-S. Lee. "Transforming the steel industry with ML/AI: real-world application and use cases". *OECD NEA International workshop on disruptive technologies for nuclear safety ap…*.

**2022**

- "Convergence analysis of connection center evolution and faster clustering". *Pattern Recognition, 127, 108639*.
- "Exponential Loss Minimization for Learning Weighted Naive Bayes Classifiers". *IEEE Access, 10, 22724-22736*.
- "A Bayesian Approach to Predict Football Matches with Changed Home Advantage in Spectator-Free Matches after the COVID-19 Break". *Entropy, 24(3), 366*.
- M. Han and J.-S. Lee. "Temporal peak-managing and clustering for continual learning from manufacturing data". *2022 INFORMS Annual Meeting*.
- J. Kim and J.-S. Lee. "Estimating freight arrival time from historical procurement data: An electronics complete/semi-knock-down case". *2022 INFORMS Annual Meeting*.
- T. Kim and J.-S. Lee. "Out-of-distribution detection using angular margin loss and regularization between output and penultimate layers of neural networks". *2022 INFORMS Annual Meeting*.
- M. Han and J.-S. Lee. "여러 설비의 서로 다른 정비 주기에 기인한 공정 데이터 분포 변화 대응 지속적 학습 방법". *2022 Spring Conference of Korean Institute of Industrial Engineers, Jeju, Korea*.
- T. Kim and J.-S. Lee. "각도 마진 손실함수와 인공신경망 정규화를 통한 out-of-distribution 탐지". *2022 Spring Conference of Korean Institute of Industrial Engineers, Jeju, Korea*.
- J. Lee and J.-S. Lee. "Monotonicity-incorporative neural network training for response surface methodology". *2022 Fall Conference of Korea Data Mining Society*.
- J.-S. Lee. "미래공장 준비를 위한 가상협업공장 추진방안". *2022 Fall Conference of Korean Institute of Industrial Engineers, Incheon, Korea*.
- M. Han and J.-S. Lee. "Clustering by peak merging". *IEEE International Conference on Knowledge Graph (ICKG 2022)*.
- J. Yun and J.-S. Lee. "Learning from imbalanced data with triplet adversarial samples". *2022 INFORMS Annual Meeting*.

**2021**

- "A Learning Objective Controllable Sphere-Based Method for Balanced and Imbalanced Data Classification". *IEEE Access, 9, 158010 - 158026*.
- "Further Improvement on Two-Way Cooperative Collaborative Filtering Approaches for the Binary Market Basket Data". *Applied Sciences, 11(19), 8977*.
- S. KIm and J.-S. Lee. "Conditional Tabular GAN combined with CAT2VEC to learn from mixed and class-imbalanced data". *2021 Fall Conference of Korean Institute of Industrial Engineers, Seoul, Korea*.
- M.-S. Kim, J.-S. Lee, and J.-H. Chun. "Detection of Field Failure Chips by Ensemble Learned from Different Chip Areas". *IEEE Microelectronics Design & Test Symposium (MDTS)*.
- Lee, J., Kim, J., Kim, H., and Lee, J.-S. "Analysis of the Home Advantage Difference in Audience-free Soccer Games after COVID-19 Using Hierarchical Bayesian Poisson model". *2021 Spring Conference of Korean Institute of Industrial Engineers, Jeju, Korea*.
- 김현호, 한민석, 이재민, 김중재, 이정훈, 이종석. "인공신경망을 활용한 전기자동차 공조시스템 모사 및 최적 제어값 탐색". *2021 Spring Conference of Korean Institute of Industrial Engineers, Jeju, Korea*.
- Park, Y. and Lee, J.-S. "A sphere-based classifier for maximizing AUC". *2021 Spring Conference of Korean Institute of Industrial Engineers, Jeju, Korea*.

## 과제

월 단위로 게시된 수행 기간이 2021년 10월–2026년 10월과 겹치는 과제·교육 항목 27건이다. KAIST 부임 이전에 시작한 항목도 포함한다. 과제명·기간·지원 기관은 연구실 게시 표기를 따르며, 상세 글에 완전한 과제명이 있는 경우에는 그 이름을 썼다. 일부 과제의 종료 시점은 기준일 이후다.[^projects][^projects2][^project-details][^project70][^project73]

- 피지컬AI 기반 협업지능 Sim-to-Real 통합 플랫폼 기술 개발 (기간 2026.08-2030.12; 지원 정보통신산업진흥원)
- 제조현장에 활용 가능한 강건한 AI 모델 적용 방법론 (기간 2026.05-2026.10; 지원 포스코)
- 방산 방공 탐지추적장치 핵심 전자장비 예지보전 (2단계) (기간 2026.03-2028.12; 지원 한화시스템)
- 방산 해양 함정 전투체계 상태기반 예지보전 (2단계) (기간 2026.03-2028.12; 지원 한화시스템)
- 공기 단축을 위한 Resource 투입 최적화 (기간 2025.10-2026.06; 지원 Samsung E&A)
- 2차전지 특화 피지컬 AI 기술 실증 및 확산 (기간 2025.10-2026.06; 지원 한국산업기술진흥원)
- 제조 특화 파운데이션 모델(MFM) 핵심 기술 개발 (기간 2025.08-2028.02; 지원 한국산업기술기획평가원)
- 피지컬AI 선도모델 수립 및 PoC (기간 2025.08-2025.12; 지원 정보통신기획평가원)
- 시간대별 최적 호기 할당 기능 개발 (스마트 군관리 SW 연계) (기간 2025.05-2026.09; 지원 현대엘리베이터)
- 자율 제조 구현을 위한 현장 작업자 친화적 혁신 AI 에이전트 개발 (기간 2025.04-2025.12; 지원 정보통신기획평가원)
- Target VT에 최적화된 압출물 Profile 탐색 프로세스 개발 (기간 2024.12-2025.11; 지원 한국타이어)
- 인공지능 기반의 자율제조를 위한 제조 특화 학습 알고리즘 개발 (Development of Learning Algorithms for AI-Driven Autonomous Manufacturing) (기간 2024.05-2027.04; 지원 한국연구재단 (National Research Foundation of Korea))
- EPC 프로젝트 데이터를 활용한 물량-기간 곡선추정 및 Critical Activity 분석 (기간 2024.04-2024.09; 지원 Samsung E&A)
- 외기조건을 고려한 RH1%이하 드라이룸 공조기 제어 최적화 (기간 2023.12-2024.08; 지원 LG에너지솔루션)
- 해양 함정 전투체계 상태기반 예지보전 사업 시스템 구축 (1단계) (기간 2023.04-2025.12; 지원 한화시스템)
- 방공 탐지추적장치 핵심 전자장비 CBM+ 기술 개발 (… (기간 2023.04-2025.12; 지원 한화시스템)
- 제조 지능 고도화를 위한 AI 기술 개발 - 음극 프레… (기간 2023.03-2023.12; 지원 삼성SDI)
- [교육] AI/Big Data 인텐시브 과정 (기간 2023.03-2023.08; 지원 패스트캠퍼스/삼성전자)
- 군관리 AUTO-TUNING 알고리즘 개발 (기간 2022.03-2022.10; 지원 현대엘리베이터)
- 인공신경망 열관리시스템 모사 모듈화 모델 구축 및 이용… (기간 2022.04-2022.12; 지원 한온시스템)
- IT 운영 지능화 솔루션의 기능 고도화를 위한 머신러닝… (기간 2021.10-2022.02; 지원 엑셈)
- 7CGL AI 기반  Smart 자동제어 (기간 2022.01-2022.12; 지원 포스코)
- AI 기반 IT 운영 지능화 솔루션 고도화 (기간 2021.06-2021.10; 지원 엑셈)
- C/SKD 자재 DX 알고리즘 개발 (기간 2021.07-2021.10; 지원 LG전자PRI)
- 디지털트윈 기반의 제조 RPA 학습/생성/평가/적용 S… (기간 2021.04-2024.12; 지원 정보통신기획평가원)
- 시스템 모사 인공신경망기반 최적제어점 추적 제어모델 개… (기간 2021.05-2021.11; 지원 한온시스템)
- 엘리베이터 군제어 연동 학습/예측 모델 개발 Phase… (기간 2021.03-2021.12; 지원 현대엘리베이터)

## 수상과 선정

2023–2026년 게시 글 중 수상·선정 11건이다. 날짜는 게시일이고, 제목에 적힌 행사 연도와 게시 연도가 다른 항목도 있다. KAIST 부임 이전 항목도 포함한다.[^notice][^notice2][^notice3]

- 2026-07-06 · 부도현 학생이 2026년 대학원 대통령과학장학생으로 최종 선정되었다.
- 2026-06-23 · 홍민희 학생이 AI 기반 시험 예측 및 신뢰도 지수 도입을 통한 시험 리드타임 단축 방안으로 한국앤컴퍼니그룹-KAIST AI 경진대회 최우수상을 수상했다.
- 2026-02-15 · 부도현 학생이 참여한 팀이 2025 OIBC 빅데이터 챌린지 일사량 추정 경진대회 대상을 수상했다.
- 2025-11-14 · 이종석 교수가 포스코그룹 인프라-AI로봇 분야 초격차기술 특임교수로 선정되었다.
- 2025-04-02 · 부도현·김찬호 학생이 지원한 팀이 2025년 연구처 석박사모험연구 사업에 최종 선정되었다.
- 2026-02-15 · 부도현·김찬호 학생이 참여한 팀이 2024 제4회 K-인공지능 제조데이터 분석 경진대회 장려상을 수상했다.
- 2024-07-29 · 부도현·김찬호 학생과 구본영 학부연구생이 참여한 팀이 교내 Co-Deep Learning 프로젝트 최우수상을 수상했다.
- 2024-04-23 · 부도현·변유정 학생이 참여한 팀이 LG 에이머스 해커톤 최우수상을 수상했다.
- 2023-12-05 · 이형권 학생과 최승준·김찬호·변유정·부도현 학부연구생이 참여한 팀이 제5회 POSTECH OIBC CHALLENGE 태양광 발전예측 경진대회 우수상을 수상했다.
- 2023-12-05 · 이종석 교수가 대한산업공학회 국제화상을 수상했다.
- 2023-12-05 · 부도현·변유정·김찬호·최승준 학부연구생이 제19회 한국대학생 산업공학 프로젝트 경진대회 은상을 수상했다.

## 소식

2023–2026년 게시 글 중 학술 활동과 연구실 명칭 변경 등 20건이다. 날짜는 게시일이며 KAIST 부임 이전의 학술 활동도 포함한다. 학회 논문 채택 소식은 채택 사실로 표시했다.[^notice][^notice2][^notice3][^techcon]

- 2025-02-14 · 연구실 명칭을 생산혁신인공지능연구실로 바꾸고 홈페이지를 개편했다.
- 2026-09-28 · 논문 세 편이 NeurIPS 2026에 채택되었다.
- 2026-08-25 · 2026 한국데이터마이닝학회 하계학술대회에 참석해 연구를 발표했다.
- 2026-08-25 · IEEE CASE 2026에 참석해 연구를 발표했다.
- 2026-06-24 · 이종석 교수가 TechCon 2026 자율제조 세션에서 자율제조 실현을 위한 인공지능 기술을 주제로 발표했다.
- 2026-06-08 · 2026 춘계 대한산업공학회 학술대회에 참석해 연구를 발표했다.
- 2026-06-08 · ICLR 2026에 참석해 포스터 세션에서 연구를 발표했다.
- 2026-02-15 · 논문 두 편이 ICLR 2026에 채택되었다.
- 2026-01-06 · 연구실 학생들이 NeurIPS 2025에 참석했다.
- 2025-11-02 · 2025 INFORMS Annual Meeting에 참석했다.
- 2025-06-29 · 2025 춘계 대한산업공학회 학술대회에 참석해 연구를 발표했다.
- 2025-05-10 · 2025년 5월 9일 대한민국 AI 정책 포럼의 제조 AI 성공전략 토론 패널로 참여했다.
- 2025-03-04 · 연구실 연구 성과가 KAIST Breakthroughs에 소개되었다.
- 2024-05-08 · ICLR 2024에 참석해 포스터 세션에서 연구를 발표했다.
- 2024-05-07 · 2024 춘계 대한산업공학회 학술대회에 참석해 연구를 발표했다.
- 2024-04-13 · 김주헌 학생이 2024 한국유연인쇄전자학회 춘계학술대회에서 연구를 발표했다.
- 2024-01-17 · 논문이 ICLR 2024에 채택되었다.
- 2024-01-03 · 이형권·김철규 학생이 2024 IMCOM 학회에 참석했다.
- 2023-12-05 · 김주헌 학생이 2023 한국유연인쇄전자학회 추계학술대회에서 연구를 발표했다.
- 2023-12-05 · 2023 INFORMS Annual Meeting에 참석해 연구를 발표했다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST E2-2 4113호, 전화 +82-42-350-3160.[^about]
- 교수 연구실: E2-2 산업경영학동 4111호, 전화 +82-42-350-3120, 팩스 +82-42-350-3110.[^professor]
- 교수 이메일: jongseok.lee@kaist.ac.kr.[^professor]

## 각주
[^home]: AIME Lab. 첫 화면. <https://aime.kaist.ac.kr> 관측일 2026-10-30.
[^about]: AIME Lab., About. 제조·생산 혁신을 위한 기계학습 방법 개발, 사전 지식·물리 조건 반영, 변화하는 자료에 대한 학습, 모형의 작동 원리와 예측 근거 설명, 표형식 시계열 학습 및 제조·서비스 응용을 소개한다. <https://aime.kaist.ac.kr/page.php?p_id=about> 관측일 2026-10-31.
[^professor]: AIME Lab., Professor. Jong-Seok Lee(이종석), Associate Professor, 산업및시스템공학과·데이터사이언스대학원 소속, 2024년 9월 KAIST 부임, 학력·경력 및 교수 연락처. <https://aime.kaist.ac.kr/page.php?p_id=professor> 관측일 2026-10-31.
[^students]: AIME Lab., Students. PH.D. Students 5명, M.S. Students 7명의 과정·기간·연구 주제·학교 이메일. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=students> 관측일 2026-10-31.
[^alumni]: AIME Lab., Alumni 첫째 쪽. 7–21번 15명의 학위·연도·진로·학위 논문. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=alumni> 관측일 2026-10-31.
[^alumni2]: AIME Lab., Alumni 둘째 쪽. 1–6번 6명의 학위·연도·진로·학위 논문. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=alumni&page=2> 관측일 2026-10-31.
[^journal]: AIME Lab., Journal 첫째 쪽. 32–46번 15편, 2022–2026년 게시 구역. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal> 관측일 2026-10-31.
[^conference]: AIME Lab., Conference 첫째 쪽. 85–99번 15건, 2025–2026년 게시 구역. 99번·94번의 별표는 equal contribution으로 밝힌 표시다. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=conference> 관측일 2026-10-31.
[^conference3]: AIME Lab., Conference 셋째 쪽. 55–69번 15건, 2022–2024년 게시 구역. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=conference&page=3> 관측일 2026-10-31.
[^projects]: AIME Lab., Projects 첫째 쪽. 38–52번 15개 과제의 제목·기간·지원 기관. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project> 관측일 2026-10-31.
[^project70]: AIME Lab., 「인공지능 기반의 자율제조를 위한 제조 특화 학습 알고리즘 개발 (Development of Learning Algorithms for AI-Driven Autonomous Manufacturing)」. 제조 자료에 맞춘 학습 알고리즘을 개발하고 예측 모형을 설비 제어의 최적화 문제에 활용하는 과제다. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=70> 관측일 2026-10-31.
[^project73]: AIME Lab., 「시간대별 최적 호기 할당 기능 개발 (스마트 군관리 SW 연계)」. 기간 2025.05-2026.09, 지원 현대엘리베이터. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=73> 관측일 2026-10-31.
[^notice]: AIME Lab., News & Notice 첫째 쪽. 공지 1건과 30–43번 14건의 게시 글. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=notice> 관측일 2026-10-31.
[^notice2]: AIME Lab., News & Notice 둘째 쪽. 14–28번 15건의 게시 글. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=notice&page=2> 관측일 2026-10-31.
[^journal2]: AIME Lab., Journal 둘째 쪽. 17–31번 15편 중 2021년 구역의 30·31번. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&page=2> 관측일 2026-10-31.
[^journal-details]: AIME Lab., Journal 상세 글의 저자·발표처·연도·게시 초록. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&wr_id=53> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&wr_id=54> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&wr_id=55> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&wr_id=56> 관측일 2026-10-31.
[^conference2]: AIME Lab., Conference 둘째 쪽. 70–84번 15건. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=conference&page=2> 관측일 2026-10-31.
[^conference4]: AIME Lab., Conference 넷째 쪽. 40–54번 15건 중 2021–2022년의 45–54번 10건. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=conference&page=4> 관측일 2026-10-31.
[^projects2]: AIME Lab., Projects 둘째 쪽. 23–37번 15건 중 게시 기간이 기준 범위와 겹치는 12건. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&page=2> 관측일 2026-10-31.
[^project-details]: AIME Lab., Projects 상세 글의 과제명·기간·지원 기관. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=67> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=68> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=69> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=71> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=72> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=83> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=84> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=85> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=86> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=87> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=88> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=89> <https://aime.kaist.ac.kr/bbs/board.php?bo_table=project&wr_id=90> 관측일 2026-10-31.
[^notice3]: AIME Lab., News & Notice 셋째 쪽. 1–14번 14건. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=notice&page=3> 관측일 2026-10-31.
[^techcon]: AIME Lab., 「TechCon 2026 자율제조 세션 발표」. 이종석 교수의 발표를 밝힌 글. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=notice&wr_id=91> 관측일 2026-10-31.
[^neurips]: AIME Lab., 「Paper accepted to NeurIPS 2026」. 2026년 9월 28일 게시 글에서 세 편의 제목·저자·채택 사실을 밝혔다. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=notice&wr_id=96> 관측일 2026-10-31.
[^p1]: J. Kim 외, J.-S. Lee, Advanced Intelligent Systems 7, 2500178 (온라인 2025-06-22). <https://doi.org/10.1002/aisy.202500178> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500178> 관측일 2026-10-31.
[^p2]: T. Kim, J.-S. Lee, IEEE Transactions on Neural Networks and Learning Systems 37, 12854-12865. <https://doi.org/10.1109/tnnls.2024.3496473> 초록 기준(OpenAlex 등록 초록). 권호는 연구실 상세 글 표기. <https://aime.kaist.ac.kr/bbs/board.php?bo_table=journal&wr_id=53> 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.patcog.2026.113240%7C10.1109/access.2025.3647464%7C10.1109/ictc66702.2025.11389118%7C10.1109/tnnls.2024.3496473> 관측일 2026-10-31.
[^p3]: H. Ryu 외, J.-S. Lee, IEEE Access 13, 217222-217231 (2025). <https://doi.org/10.1109/access.2025.3647464> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.patcog.2026.113240%7C10.1109/access.2025.3647464%7C10.1109/ictc66702.2025.11389118%7C10.1109/tnnls.2024.3496473> 관측일 2026-10-31.
[^health]: D. Bu 외, J.-S. Lee, 2025 16th International Conference on Information and Communication Technology Convergence (ICTC). <https://doi.org/10.1109/ictc66702.2025.11389118> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.patcog.2026.113240%7C10.1109/access.2025.3647464%7C10.1109/ictc66702.2025.11389118%7C10.1109/tnnls.2024.3496473> 관측일 2026-10-31.

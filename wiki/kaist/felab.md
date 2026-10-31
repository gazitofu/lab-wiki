# Financial Engineering Lab.

**KAIST 산업및시스템공학과·경영대학(겸직) · 김우창 교수**

- 분야: 금융공학, 자산관리, 불확실한 상황의 의사결정, 학습 기반 최적화
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^research][^p3], 강화학습[^research], 통계적 추론·검정[^p7]
- 홈페이지: <https://felab.kaist.ac.kr/>

> 투자자의 목표와 금융시장의 불확실성을 수학 모형으로 표현하고, 투자 결정과 금융 계획을 계산할 최적화·기계학습 방법을 연구한다.[^research]

## 무엇을 연구하나

이 연구실은 금융공학(금융 문제를 수학 모형과 계산 방법으로 다루는 분야)을 연구한다. 중심 대상은 포트폴리오(여러 투자 자산을 묶은 구성)와 개인의 생애주기 자산관리다. 돈을 어떤 자산에 얼마나 투자할지, 여러 시점에 걸친 재무 목표를 어떻게 달성할지 정하기 위해 최적화(주어진 조건 안에서 정한 기준을 최대화하거나 최소화하는 값을 찾는 방법)를 개발한다. 연구 소개는 금융 인공지능, 핀테크(금융 서비스를 구현하는 기술), 투자관리, 금융 최적화의 네 갈래를 제시한다.[^home][^research]

금융 인공지능에서는 심층 강화학습(여러 층의 신경망을 쓰며 보상을 바탕으로 행동을 학습하는 방법)을 중심에 둔다. 호가장(가격별 매수·매도 주문을 모은 기록)의 움직임을 학습해 고빈도 거래(짧은 시간 간격으로 매매 결정을 반복하는 거래)의 정책을 개발하려 하며, 장기 투자에서는 여러 제약을 지키는 자산 배분을 연구한다. 금융 시계열(시간 순서대로 기록한 금융 관측값)을 이용한 제어 연구에서는 커리큘럼학습(학습 자료나 과제의 구성을 조절하며 학습시키는 방법)과 모방학습(다른 주체의 행동을 자료로 삼아 행동 방식을 학습하는 방법)을 분석했다.[^research][^p6]

개인 자산관리에서는 투자자의 서로 다른 목표와 우선순위를 반영한 생애주기 목표기반 투자 서비스를 개발했고, 계산 비용과 처리 시간을 줄이는 확장성을 연구한다고 소개한다. 최근에는 결정중심학습(최종 의사결정에 따른 손실 함수로 예측 모형을 학습하는 방법)을 통해 예측과 투자 결정을 연결한다. 보유할 자산의 개수를 정확히 제한하는 투자 문제와, 다양한 의사결정 문제에 쓸 손실 모형을 함께 다룬다.[^research][^p1][^p2]

계산 방법 자체도 연구 대상이다. 다단계 확률계획(불확실한 값을 확률분포로 표현하고 여러 시점의 결정을 함께 정하는 최적화)에서는 문제를 단계별로 나누고 가치함수(현재 상태에서 시작할 때 미래 비용이나 성과의 기댓값을 나타내는 함수)를 근사하는 방법을 개발한다. 트랜스포머(자료 요소 사이의 관계를 학습해 표현을 구성하는 신경망 구조), 입력 볼록 신경망(입력에 대한 볼록성을 유지하도록 설계한 신경망), 가치함수의 기울기를 학습하는 알고리즘이 대표적이다. 금융을 넘어 생산 최적화와 에너지 계획의 계산 문제도 예제로 다룬다.[^p3][^p4][^p5]

확률 모형에서는 변분추론(계산하기 어려운 확률분포를 다루기 쉬운 확률분포로 근사해 추론하는 방법)의 계산 복잡도와, 확률적인 생성 정책으로 구조를 만드는 GFlowNet(Generative Flow Network, 생성 흐름 네트워크)의 학습 구조를 연구했다. 변분추론 논문은 근사 분포의 구조와 자료 수에 따른 계산량을 분석한다. GFlowNet 논문은 온도 매개변수(생성 결과에 집중하는 정도를 조절하는 값)에 따라 학습된 함수로 출력 점수를 조정하는 새 구조를 제안한다.[^p7][^p8]

## 주요 연구 주제

### 1. 투자 목표와 예측을 함께 학습하기

예측 오차만 줄이는 대신 실제 투자 결정의 품질을 학습 목표에 반영한다. 대표 논문은 자산 선택·예측·재최적화를 함께 연결한 결정중심학습과, 일부 입력의 볼록성을 유지하는 손실 모형을 제안한다. 개인의 생애주기 목표기반 자산관리 서비스와 제약이 있는 포트폴리오가 주요 대상이다.[^research][^p1][^p2]

### 2. 여러 시점의 의사결정을 계산하는 알고리즘

단계별 하위 문제를 풀어 미래 의사결정의 영향을 계산한다. 가치함수의 모양이나 기울기를 학습하고, 트랜스포머와 신경망을 이용해 근사 함수를 만든다. 연구 소개는 강건 최적화(정해 둔 불확실한 값의 집합에 대해 조건을 지키는 결정을 찾는 방법), 확률계획, 동적계획(현재 선택과 이후 선택의 관계를 이용해 순차 의사결정을 푸는 방법)을 금융 의사결정의 주요 방법으로 든다.[^research][^p3][^p4][^p5]

### 3. 금융 거래와 시계열에서 행동 배우기

호가장 움직임을 학습하는 고빈도 거래 정책과 장기 투자 배분을 연구한다. 금융 시계열 제어에서는 학습 자료를 구성하는 방법과 다른 정책의 행동을 학습에 사용하는 방법을 이론·실험으로 분석한다. 연구실 과제에는 고빈도 트레이딩 모형 개발과 초단기 알고리즘 불공정 거래 적출 모형 개발이 있다.[^research][^p6][^projects]

### 4. 확률 추론과 생성 모형의 계산 구조

근사 확률분포의 구조를 바꿔 변분추론의 계산량을 분석하고, 확률적 생성 모형의 출력 점수를 조절하는 구조를 설계한다. 이 갈래는 특정 금융 상품의 실증 분석에 한정되지 않고, 자료에서 불확실성을 추론하거나 여러 가능한 구조를 생성하는 학습 방법 자체를 다룬다.[^p7][^p8]

## 대표 논문

연구실 논문 목록의 2021–2026년 논문 가운데 김우창 교수가 저자이고, 최적화·학습·확률 추론의 방법 개발을 다루는 여덟 편을 골랐다. 학회 이름과 함께 arXiv 판을 적은 행은 해당 학회 표기가 있는 사전 공개본의 초록을 썼다. VFGL은 arXiv 판, 나머지 세 편은 학회 논문집의 초록을 썼다. 연도는 학회 또는 연구실 목록의 연도이며, 각주에는 사전 공개본의 최초 게시일도 적었다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.[^research]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Decision-focused Sparse Tangent Portfolio Optimization](https://doi.org/10.48550/arXiv.2607.00581) · ICML 2026 (arXiv 판) | 보유 자산 수가 제한된 포트폴리오를 예측과 투자 결정이 이어지는 하나의 학습 과정으로 풀었다. 샤프 비율(수익의 변동에 대해 무위험 수익을 넘는 수익이 얼마나 되는지 나타내는 지표)을 최대화하는 문제를 볼록 최적화 층으로 만들고, 자산을 고르는 단계를 매끄러운 연산으로 바꿔 정확한 자산 개수를 유지했다. 네 주요 주식시장의 시험 자료에서 과거 자료 기반 방법과 예측 중심 방법에 견줄 만하거나 우수한 샤프 비율을 보였으며, 후보 자산이 많은 경우 성과 개선이 두드러졌다.[^p1] | 1저자 Haeun Jeon, 마지막 저자 김우창 |
| 2 | 2025 | [Locally Convex Global Loss Network for Decision-Focused Learning](https://doi.org/10.48550/arXiv.2403.01875) · AAAI 2025 (arXiv 판) | 의사결정의 손실을 예측 모형 학습에 반영할 때, 최적 결정의 변화율을 계산하기 어렵다는 문제를 다룬다. 일부 입력에 대한 볼록성을 보장하고 다른 입력에 대해서는 비볼록 구조를 유지하는 신경망으로 손실을 학습하는 LCGLN(Locally Convex Global Loss Network)을 제안했다. 적절한 수식 형태를 직접 골라야 하는 부담 없이 하나의 대리 손실을 사용하도록 했고, 세 확률적 의사결정 문제에서 효과와 유연성을 평가했다.[^p2] | 1저자 Haeun Jeon, 마지막 저자 김우창 |
| 3 | 2023 | [Transformer-based Stagewise Decomposition for Large-Scale Multistage Stochastic Optimization](https://proceedings.mlr.press/v202/kim23r.html) · ICML 2023 | 여러 단계의 불확실한 결정을 계산할 때 하위 문제의 크기와 개수가 늘어나는 어려움을 다룬다. 트랜스포머가 선형 근사 조각을 순서대로 결합해 가치함수를 구성하는 TranSDDP를 제안했다. 수치 실험에서 해의 품질을 유지하며 계산 시간을 줄였다.[^p3] | 1저자 Chanyeong Kim, 마지막 저자 김우창 |
| 4 | 2023 | [Deep Value Function Networks for Large-Scale Multistage Stochastic Programs](https://proceedings.mlr.press/v206/bae23a.html) · AISTATS 2023 | 단계별 가치함수를 신경망으로 근사하는 DVFN(Deep Value Function Networks)을 제안했다. 일반 신경망의 비볼록성이 학습을 불안정하게 할 수 있어 입력에 대한 볼록성을 보장하는 신경망을 사용했다. 생산 최적화와 에너지 계획의 선형·비선형 문제에서 기존 알고리즘과 비교했고, 정확성과 계산 효율을 확인했다.[^p4] | 1저자 Hyunglip Bae, 김우창은 세 번째 저자 |
| 5 | 2022 | [Value Function Gradient Learning for Large-Scale Multistage Stochastic Programming Problems](https://doi.org/10.48550/arXiv.2205.08934) · arXiv 판 | 가치함수의 기울기에 맞도록 매개변수를 학습하는 VFGL(Value Function Gradient Learning)을 제안했다. 매 반복마다 선형 제약을 누적하는 대신 정해진 수의 매개변수를 쓰므로, 반복 중에도 하위 문제의 크기를 일정하게 유지한다. 생산 계획, 수력·화력 발전, 생애주기 재무 계획 예제에서 해의 품질과 계산 효율을 평가했다.[^p5] | 1저자 Jinkyu Lee, 김우창은 세 번째 저자 |
| 6 | 2024 | [Curriculum Learning and Imitation Learning for Model-free Control on Financial Time-series](https://doi.org/10.48550/arXiv.2311.13326) · AAAI 2024 AI4TS Workshop (arXiv 판) | 무작위 변동이 있는 시계열을 대상으로 커리큘럼학습과 모방학습을 이론·실험으로 분석했다. 자료를 증강해 학습 구성을 바꾸고, 기준 정책에서 행동 방식을 학습하는 방법을 구현했다. 실험은 시계열 제어에서 커리큘럼학습의 가능성을 뒷받침했으며, 모방학습은 주의해서 써야 한다고 결론지었다.[^p6] | 1저자 Woosung Koh, 마지막 저자 김우창 |
| 7 | 2024 | [Provably Scalable Black-Box Variational Inference with Structured Variational Families](https://doi.org/10.48550/arXiv.2401.10989) · ICML 2024 (arXiv v2 판) | 계층적 베이지안 모형(여러 수준의 미지 값을 확률 관계로 연결한 모형)에서는 자료가 늘면 추론할 변수도 늘어난다. 근사 분포에 특정 행렬 구조를 두면 반복 복잡도의 자료 수 의존성을 제곱에서 선형으로 바꿀 수 있음을 증명했다. 대규모 계층 모형의 실험으로 이론 결과를 확인했다.[^p7] | 1저자 Joohwan Ko, 김우창은 세 번째 저자 |
| 8 | 2024 | [Learning to Scale Logits for Temperature-Conditional GFlowNets](https://proceedings.mlr.press/v235/kim24s.html) · ICML 2024 | 온도 조건에 따라 구조를 생성하는 GFlowNet의 학습을 위한 Logit-GFN을 제안했다. 온도에 따라 학습한 함수가 로짓(확률로 바꾸기 전의 점수)의 크기를 직접 조절하도록 설계했다. 생물·화학 과제에서 학습 속도, 이미 모은 자료에 대한 일반화, 학습 중 다양한 결과를 발견하는 능력을 실험했다.[^p8] | 1저자 Minsu Kim, 김우창은 여섯 번째 저자 |

## 교수와 전문 분야

김우창 교수의 영문 이름은 Woo Chang Kim이다. Team 페이지는 KAIST 산업및시스템공학과의 Professor 경력을 2009년부터 현재까지로, 경영대학의 Adjunct Professor 경력을 2021년부터 현재까지로 적는다. 서울대학교 산업공학 학사·석사를 각각 1999년·2001년에, Princeton University의 Operations Research & Financial Engineering 석사·박사를 각각 2007년·2009년에 받았다.[^team]

교수 소개에 적힌 교내 보직은 산업및시스템공학과장(2021–2022), 데이터사이언스대학원장(2022), 지식서비스공학대학원장(2022), 신한–KAIST 인공지능 금융 연구개발센터장(2019–2023)이다. Quantitative Finance의 Managing Editor(운영 편집자, 2017–2022)를 맡았고, 같은 학술지 Associate Editor(부편집자, 2023년부터 현재), Optimization and Engineering Associate Editor(2014년부터 현재), Journal of Portfolio Management Editorial Board Member(편집위원, 2013년부터 현재) 경력을 게시한다.[^team]

최근 논문에서 드러나는 전문 분야는 예측과 의사결정을 결합하는 학습, 다단계 확률 최적화의 분해·근사 알고리즘, 금융 시계열에서의 행동 학습, 확률 추론의 계산 구조다. 투자 결정을 계산하는 문제와 그 계산을 가능하게 하는 일반 방법론을 함께 다룬다는 점이 특징이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

## 응용 분야

연구 소개의 직접적인 응용은 개인별 생애주기 자산관리, 목표기반 투자, 투자 성과를 위한 정량적 의사결정, 고빈도 거래다. 과제 목록은 금융 데이터 기반 시장 가치 모형, 투자용 기술력 평가, 불공정 거래 적출도 포함한다. 확률 최적화 논문은 생산 계획과 에너지 계획을 계산 예제로 사용한다.[^research][^projects][^p4][^p5]

## 구성원

2026년 10월 31일 Team 페이지의 학생·박사후연구원 기준이다. 박사과정 6명, 석사과정 2명, 박사후연구원 1명이며, 과정은 게시 구획을 옮겼다. 「대표 논문 참여」는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인해 표시했다.[^team]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Munki Chung (정문기) | 박사과정 | moonki93@kaist.ac.kr |  |
| Haeun Jeon (전하은) | 박사과정 | haeun39@kaist.ac.kr | 1, 2 |
| Mingyu Yang (양민규) | 박사과정 | yangmg1216@kaist.ac.kr |  |
| Gwanghyun Lee (이광현) | 박사과정 | rhkdgus0414@kaist.ac.kr |  |
| Seunghoon Choi (최승훈) | 박사과정 | shchoi0307@kaist.ac.kr | 1 |
| Daho Cheon (천다호) | 박사과정 | hidaho@kaist.ac.kr |  |
| Gimin Kang (강기민) | 석사과정 | kgm4752@kaist.ac.kr | 6 |
| Sangwan Kim (김상완) | 석사과정 | sangwan.kim@kaist.ac.kr |  |
| Hwayong Choi (최화용) | 박사후연구원 | ganarisg@kaist.ac.kr |  |

## 졸업생 진로

2026년 10월 31일 Alumni 페이지의 박사 학위 15행(2014–2026), 석사 학위 32행(2011–2026)이다. 같은 사람이 서로 다른 학위로 다시 나올 수 있다. 진로와 학위 논문 제목은 연구실 게시 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Chanyoung Kim (김찬영) | Ph.D. (2026) | Blockchain Researcher, FairSquareLab, 2026 - | Balancing Scalability and Accuracy in Large-Scale Stochastic Optimization: Learning-Based Approaches to Value Function Approximation |
| Hyunglip Bae (배형립) | Ph.D. (2025) | Assistant Professor, Department of Big Data Convergence, Chonnam National University, 2026 - | Study on Approximation of Large-Scale Parametric Optimization via Deep Learning: with Applications on Financial Planning |
| Insu Choi (최인수) | Ph.D. (2025) | Assistant Professor, Department of Finance and Big Data, Gachon University, 2026 - | LUCIDE: A Lucid, User-Centric, Intelligent, Data-Inspired, End-to-End System Framework for Illustrative Decision-Making in Financial Asset Management Services |
| Minjeong Park (박민정) | Ph.D. (2025) | Postdoctoral Researcher, KAIST, 2025 - | Data-Driven Analysis of the Korean Housing Market, Government Budget Allocation Model, and Housing Recommendation System Development |
| Guhyuk Chung (정구혁) | Ph.D. (2024) | Quantitative Trader, LINE Investment Technologies, 2024 - | Order Book Modeling and Market Making Strategies: A Neural Approach |
| Dongyeol Lee (이동열) | Ph.D. (2024) | Long-term Insurance U/W Planning Dept, Samsung Fire & Marine Insurance, 2024 - | A Study on Investment Decisions by Large Institutional Investors under Existence of Socio-Economic Impact: The Case of National Pension Fund |
| Sanghyeon Bae (배상현) | Ph.D. (2024) | Assistant Professor, School of Business, Ajou University, 2025-; Senior Researcher, Big Data & AI Lab, Hana Institute of Technology, 2024 - 2025 | Modeling and computational methods for personalized financial decision making: machine learning, optimization, and decomposition techniques |
| Hyeongwoo Kong (공형우) | Ph.D. (2024) | Assistant Professor, Division of Finance and AI, Hankuk University of Foreign Studies (HUFS), 2025 -; Post-doctoral Researcher, Department of Industrial Engineering, UNIST, 2024 - 2025; Postdoctoral Researcher, Industrial Engineering, Financial Engineering Lab, UNIST, 2024 - | Enhancing Financial Services via Data Analytics and Machine Learning |
| Jinkyu Lee (이진규) | Ph.D. (2022) | Staff Engineer, AI Productivity Team, Samsung Research, 2025 -; Chief Technology Officer (CTO), HuGraph, 2021 - | Decomposition and Approximation Techniques for Large-Scale Multistage Stochastic Programs: With Applications in Finance |
| Woong-Bee Choi (최웅비) | Ph.D. (2019) | Researcher, GBI Team, Veranos Technologies, 2018 -; Deputy Research Fellow, Investment Policy Divison, National Pension Research Institute, 2019 - | A Study on the Effect of Korea Pension Management on Social System under Asset -Liability Management Framework |
| Do-Gyun Kwon (권도균) | Ph.D. (2018) | Vice President, Quantitative Development, World Quant, 2018 - | Stochastic Programming Models for Goal-based Asset-liability Management |
| Geum-il Bae (배금일) | Ph.D. (2016) | OCIO Management Team, Samsung Asset Management, 2016 - 2020; Chief Technology Officer (CTO), HuGraph, 2020 - 2023 | Three Essays on Financial Analysis under Regime Switching Framework |
| Yongjae Lee (이용재) | Ph.D. (2016) | Postdoctoral Researcher, Industrial Engineering & Management Research Institute, KAIST, 2016 - 2017; BK Assistant Professor, Graduate School of Convergence Science and Technology, Seoul National University, 2017 - 2018; Assistant Professor, School of Management Engineering, UNIST, 2018 - 2024; Associate Professor, School of Management Engineering, UNIST, 2024 - | Demystifying Diversification Strategies by using Portfolio Optimization Techniques |
| Min Jeong Kim (김민정) | Ph.D. (2015) | Manager, Research Team, Financial Engineering Ceter, Korea Asset Pricing, 2015 - 2017; Deputy Research Fellow, Investment Policy Divison, National Pension Research Institute, 2017 - | A Study on Optimization Models under Uncertainty and Their Applications in Financial Planning |
| Jang Ho Kim (김장호) | Ph.D. (2014) | Associate Professor, Department of Industrial and Management Systems Engineering, Kyung Hee University, 2015 - | Understanding Robust Optimization by Analyzing Robust Equity Portfolios |
| Sukmin Hwang (황석민) | M.S. (2026) |  | Shock-Biased Attention: Enhancing Transformer Hawkes Processes with Amplitude-Driven Temporal Kernels |
| Seunghoon Choi (최승훈) | M.S. (2026) | Doctoral Student, KAIST, 2026 - | Decision-Focused Learning for Cardinality-constrained Portfolio Optimization |
| Sungho Lee (이승호) | M.S. (2026) | Quantitative Trader, Multi-Asset Trading Team, Yuanta Securities, 2026 - | From Constituents to Index: Interpretable Price Movement Prediction via Cross-Asset Order Flow |
| Beomjun Kim (김범준) | M.S. (2026) |  | Latent Contextual Gating for Stock Return Forecasting |
| Woosang Yim (임우상) | M.S. (2025) | Associate, Global Stock Management Team, Samsung Asset Management, 2026 - | Surrogate Model-Based Parameter Optimization Framework for Goal-Based Investing |
| Minsu Park (박민수) | M.S. (2025) | Manager, Mirae Asset Life Insurance, 2026 - | A Decision-focused Learning Framework for Goal-based Investing |
| Minsuk Kim (김민석) | M.S. (2025) | Grade Health Chain, 2025 - | SDOpt: Semi-Definite Optimization Layer for Index Tracking |
| Mingyu Yang (양민규) | M.S. (2024) | Doctoral Student, KAIST, 2024 - | Type-Based Representation of Limit Order Book Events for Predicting Mid-Price Change Using Deep Neural Network |
| Joohwan Ko (고주환) | M.S. (2024) | Doctoral Student, UMass Amherst, 2024 - | A Study on Scalable and Provable Black-Box Variational Inference |
| Seokhwan Choi (최석환) | M.S. (2023) | Associate, Hana Financial Investment, 2024 - | TranSort: Transformer for Differentiable Sorting |
| Hyun Kim (김현) | M.S. (2023) | Quantitative Researcher, FnPricing, 2023 - | AC-DQN: Action Constrained Deep Q-Network for Goal Based Investment |
| Jongwoong Park (박종웅) | M.S. (2023) | NC Soft, 2023 - | SDDP-Transformer: Applying the Transformer to Generation of Piecewise Linear Value Function |
| Haeun Jeon (전하은) | M.S. (2023) | Doctoral Student, KAIST, 2023 - | OSCAR: An Asset Selection Heuristic for Cardinality Constrained Portfolio Optimization |
| Wonje Yun (윤원제) | M.S. (2022) | Master's Student, Chicago University, 2022 - | Analysis Framework of Dependency Measures in the Stock Market, and its Applications |
| Chanyoung Kim (김찬영) | M.S. (2022) | Doctoral Student, KAIST, 2022 - 2026 | Optimizing High-Frequency Pairs Trading via Reinforcement Learning with Spread Prediction Model |
| Minseong Kim (김민성) | M.S. (2022) | Quantitative Researcher, WorldQuant, 2021 - | Using Graph Convolutional Networks to Approximate Cardinality Constraints in Portfolio Optimization |
| Hyojin Lim (임효진) | M.S. (2021) | Associate, Multi-Asset Investment Team, Korea Investment Management, 2021 - | Enhancing Hedge Fund Index Tracking Factor Model via Deep Reinforcement Learning |
| Insu Choi (최인수) | M.S. (2021) | Doctoral Student, KAIST, 2021 - 2025 | Empirical Analysis of Politically-Themed Stocks Using Text Mining Techniques and Entropy-Based Network Dynamics |
| Seulah Choi (최슬아) | M.S. (2020) | KB Securities, 2020; Quantitative Researcher, WorldQuant, 2020 - | Interpretation of Put-Call Parity Violation and Tax Effect |
| Sungmin Jang (장성민) | M.S. (2020) | Researcher, JSOL, 2020 - | Information Flow Between Bitcoin and Other Investment Assets |
| Gu-Hyuk Chung (정구혁) | M.S. (2019) | Doctoral Student, KAIST, 2019 - | Scenario Tree Generation and Stochastic Programming under Heston Framework |
| Sangyeon Kim (김상연) | M.S. (2019) | Researcher, TmaxSoft, 2020 - | Optimal Building Blocks for Single- and Multi-period Investment Management |
| Munki Chung (정문기) | M.S. (2018) | Doctoral Student, KAIST, 2018 - | The Effects of Errors in Means, Variances, and Correlations on All Feasible Portfolios |
| Jieun Kim (김지은) | M.S. (2018) | Junior Assistant Manager, Korea Technology Finance Corporation, 2018 - 2021; Researcher, Agency for Defense Development, 2021 - | Longevity Risk Management for Individual Investors in the Retirement Stage using SDDP algorithm |
| Beom Hyeon Kim (김범현) | M.S. (2018) | Researcher, Index Team/ Quant Department, FnGuide, 2018 - 2021; Researcher, Presto Labs, 2021 - | Measuring the Certainty Equivalent Loss of Target Date Fund using Multi-stage Stochastic Programming |
| Jeonghyun Kim (김정현) | M.S. (2017) | Assistant Manager, Risk Engineering Team, Shinhan, 2017 - | Optimal Control of Defined Benefit National Pension Plans |
| Ju Ri Jang (장주리) | M.S. (2016) | Financial Business Division, NICE Information Service, 2016 - 2021; Receptionist, Korea Credit Information Services, 2021 - | Sparse and Robust Portfolio Selection via Semi-Definite Relaxation |
| Je-Hyuk Lee (이제혁) | M.S. (2014) | Doctoral Student, Seoul National University, 2014 - 2019; Senior Engineer, Samsung Electronics, 2020 - | Catastrophe Bond Issuance Strategy (Case of Korean Typhoon) |
| Natasia Engeline | M.S. (2012) | Manager, Bank of Indonesia, 2012 - 2019; Manager, Advisory, EY Indonesia, 2019 - | CMO & TIPS Modeling Under Inflation Adjusted Scenarios (Case of Indonesia) |
| Geum Il Bae (배금일) | M.S. (2012) | Doctoral Student, KAIST, 2012 - 2016 | What Are the Regimes in the Commodity Market? |
| Joonsuk Pyo (표준석) | M.S. (2011) | Analyst, Fixed Income Trading Department, Korean Investment & Securities, 2011 - | Why Do Expensive Warrants Traded More Heavily Than Cheaper Ones Exist in the Korean Equity Linked Market? |
| So Hyoung Ahn (안소형) | M.S. (2011) | Analyst, Equity Team, Dongbu Insurance, 2011 - | What Do Robust Portfolios Really Do? |

## 최근 5년 논문 목록

연구실 Research의 Refereed Journal Papers 목록이다. 연도는 연구실의 2021–2026년 구역을 따르며 제목·저자·발표처는 게시 표기를 유지했다. 학회·워크숍 논문도 이 구획의 게시 위치를 따랐다. 저자 뒤 기호는 누리집 표시다.[^research]

**2026**

- Hyunglip Bae, Jang Ho Kim, Hwayong Choi, Frank J. Fabozzi, Woo Chang Kim (2026). Deep Financial Planning. Annals of Operations Research.
- Haeun Jeon\*, Seunghoon Choi\*, Hyunglip Bae, Yongjae Lee, Woo Chang Kim (2026). Decision-Focused Sparse Tangent Portfolio Optimization. International Conference on Machine Learning (ICML).
- Mingyu Yang, Guhyuk Chung, Chanyeong Kim, Woo Chang Kim (2026). Enhancing Limit Order Book Modeling Through Type-Based Representation. Pacific-Asia Conference on Knowledge Discovery and Data Mining.
- Insu Choi, Soyeong Lim, Seoyeon Kim, Yeona Choi, Subin Han, Woo Chang Kim (2026). Metric-based Technical Indicators for Yield Forecasting. Pacific-Basin Finance Journal.
- Insu Choi, Woo Chang Kim (2026). Beyond Linear Insights in the Feldstein–Horioka Puzzle: Delving Into Monotonic and Nonlinear Statistical Dependencies With Moving Windows. International Finance.
- Hyunglip Bae∗, Minsu Park∗, Haeun Jeon, Woo Chang Kim (2025), A Decision-focused Learning Framework for Goal-based Investing, Quantitative Finance.
- Insu Choi, Woo Chang Kim (2026). Navigating the Flow: Unveiling Directional Information Transfer in Commodity Markets With Transfer Entropy and Moving Window Analysis. Complexity.

**2025**

- Jang Ho Kim, Yongjae Lee, Woo Chang Kim, Jae Wook Song, Frank J. Fabozzi (2025). Random Forests for Feature Selection: Concepts and Applications in Asset Management. Journal of Portfolio Management.
- Sungho Lee, Sukmin Hwang, Chanyeong Kim, Mingyu Yang, Yongjae Lee, and Woo Chang Kim (2025, November). From Constituents to Index: Interpretable Price Movement Prediction via Cross-Asset Order Flow. In Proceedings of the 6th ACM International Conference on AI in Finance (pp. 665-673).
- Sukmin Hwang, Sungho Lee, Chanyeong Kim, Yongjae Lee, and Woo Chang Kim (2025, November). Shock-Biased Attention: Enhancing Transformer Hawkes Processes with Amplitude-Driven Temporal Kernels. In Proceedings of the 6th ACM International Conference on AI in Finance (pp. 915-923).
- Myounggu Lee, Insu Choi, and Woo Chang Kim (2025), "Predicting Mobile Payment Behavior Through Explainable Machine Learning and Application Usage Analysis" Journal of Theoretical and Applied Electronic Commerce Research, 20(2), 117.
- Haeun Jeon\*, Hyunglip Bae\*, Minsu Park, Chanyeong Kim, and Woo Chang Kim (2025), "Locally Convex Global Loss Network for Decision-Focused Learning" presented at the Association for the Advancement of Artificial Intelligence (AAAI) (Oral Presentation).
- Insu Choi & Woo Chang Kim (2025). "A Multifaceted Graph-wise Network Analysis of Sector-Based Financial Instruments' Price-Based Discrepancies with Diverse Statistical Interdependencies". The North American Journal of Economics and Finance.

**2024**

- Jang Ho Kim, Yongjae Lee, Woo Chang Kim, Taehyeon Kang, and Frank J. Fabozzi (2024). "An Overview of Optimization Models for Portfolio Management". The Journal of Portfolio Management 51 (1).
- Insu Choi & Woo Chang Kim (2024). "Unlocking ETF Price Foreasting: Explring the Interconnections with Statistical Dependence-Based Graphs and xAI Techniques". Knowledge-Based Systems. 305, 112567.
- Lee, Yongjae; Kim, Jang Ho; Kim, Woo Chang; Fabozzi, Frank J (2024). “An Overview of Machine Learning for Portfolio Optimization". Journal of Portfolio Management.
- Jang Ho Kim\*, Seyoung Kim, Yongjae Lee, Woo Chang Kim, and Frank J. Fabozzi (2024). "Enhancing mean-variance portfolio optimization through GANs-based anomaly detection". Annals of Operation Research.
- Insu Choi\* and Woo Chang Kim\* (2024). "A Temporal Information Transfer Network Approach Considering Federal Funds Rate for an Interpretable Asset Fluctuation Prediction Framework". International Review of Economics and Finance.
- Sanghyeon Bae\*, Yongjae Lee, Woo Chang Kim\*, Jang Ho Kim, and Frank J. Fabozzi (2024). "Goal-based investing with goal postponement: Multistage stochastic mixed-integer programming approach", Annals of Operations Research, 1-25.
- Insu Choi\*, Woosung Koh\*, Gimin Kang, Yuntae Jang, & Woo Chang Kim (2024). "Encoding Temporal Statistical-space Priors via Augmented Representation under Data Scarcity", 3rd International Workshop on Spatio-Temporal Reasoning and Learning (STRL 2024) at International Joint Conference on Artificial Intelligence (IJCAI) 2024. CEUR-WS.org.
- Minsu Kim\*, Joohwan Ko\*, Taeyoung Yun\*, Dinghuai Zhang, Ling Pan, Woo Chang Kim, Jinkyoo Park, Emmanuel Bengio, Yoshua Bengio (2024), “Learning to Scale Logits for Temperature-Conditional GFlowNet”, International Conference on Machine Learning (ICML)
- Joohwan Ko\*, Kyurae Kim\*, Woo Chang Kim, Jacob R. Gardner (2024). “Provably Scalable Black-Box Variational Inference with Structured Variational Families”, International Conference on Machine Learning (ICML)
- Insu Choi and Woo Chang Kim (2024). Practical Forecasting of Risk Boundaries for Industrial Metals and Critical Minerals via Statistical Machine Learning Techniques. International Review of Financial Analysis. 103252.
- Guhyuk Chung, Yongjae Lee+, and Woo Chang Kim+ (2024), "Neural Marked Hawkes Process for Limit Order Book Modeling," Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD).
- Woosung Koh\*, Insu Choi\*, Yuntae Jang\*, Gimin Kang, and Woo Chang Kim (2024), "Curriculum Learning and Imitation Learning for Model-free Control on Financial Time-series," AI4TS: AI for Time Series Analysis: Theory, Algorithms, and Application Workshop at AAAI 2024.
- Insu Choi\*, Woosung Koh\*, Bonwoo Koo\*, and Woo Chang Kim (2024), "Network-based Exploratory Data Analysis and Explainable Clustering for Financial Customer Profiling," Engineering Applications of Artificial Intelligence.
- Insu Choi and Woo Chang Kim (2024), "Enhancing Exchange-Traded Fund Price Predictions: Insights from Information-Theoretic Networks and Node Embeddings". Entropy, 26(1), 70.

**2023**

- Insu Choi and Woo Chang Kim (2023), "Enhancing Financial Literacy in South Korea: Integrating AI and Data Visualization to Understand Financial Instruments’ Interdependencies," Societal Impacts.
- Insu Choi and Woo Chang Kim (2023), "Estimating Historical Downside Risks of Global Financial Market Indices via Inflation Rate-Adjusted Dependence Graphs," Research in International Business and Finance.
- Sanghyeon Bae, Yongjae Lee, and Woo Chang Kim (2023), "Optimal Portfolio Choice of Couples with Tax-deferred Accounts and Survival-contingent Products," Quantitative Finance.
- Yongjae Lee, John R. J. Thompson, Jang Ho Kim, Woo Chang Kim, and Francesco A. Fabozzi (2023), "An Overview of Machine Learning for Asset Management," Journal of Portfolio Management.
- Jang Ho Kim, Woo Chang Kim, Yongjae Lee, Bong-Geun Choi, and Frank J. Fabozzi (2023), "Robustness in Portfolio Optimization," Journal of Portfolio Management.
- Jinkyu Lee, Do-Gyun Kwon, Yongjae Lee, Jang Ho Kim, and Woo Chang Kim (2023), "Large-scale Financial Planning via a Partially Observable Stochastic Dual Dynamic Programming Framework," Quantitative Finance.
- Dongyeol Lee and Woo Chang Kim (2023), "Optimal Intertemporal Liquidation of Institutional Investors with Cash Requirements and Viable Loans," European Journal of Finance.
- Chan Yeong Kim, Jong Woong Park, Hyunglip Bae, and Woo Chang Kim (2023), "Transformer-based Stagewise Decomposition for Large-Scale Multistage Stochastic Optimization," presented at the International Conference on Machine Learning (ICML) (Oral Presentation).
- Hyunglip Bae, Jinkyu Lee, Woo Chang Kim, and Yongjae Lee (2023), "Deep Value Function Networks for Large-Scale Multistage Stochastic Programming Problems," 26th International Conference on Artificial Intelligence and Statistics (AISTATS 2023).
- Joohwan Ko, Michael Poli, Stefano Massarolli, and Woo Chang Kim (2023), "Multilevel Approach to Efficient Gradient Calculation in Stochastic Systems," ICLR 2023 Workshop on Physics for Machine Learning.
- Hyeongwoo Kong, Wonje Yun, and Woo Chang Kim (2023), "Tracking customer risk aversion," Finance Research Letters.
- Insu Choi, Myounggu Lee, Hyejin Kim, and Woo Chang Kim (2023), "Elucidating Directed Statistical Dependencies: Investigating Global Financial Market Indices' Influence on Korean Short Selling Activities," Pacific-Basin Finance Journal.

**2022**

- Jang Ho Kim, Yongjae Lee, Woo Chang Kim, and Frank J. Fabozzi (2022) "Goal-Based Investing Based on Multi-Stage Robust Portfolio Optimization", Annals of Operations Research .
- Insu Choi and Woo Chang Kim (2022) “Analyzing and Utilizing Thematic Stocks based on Text Mining Techniques and Information Flow-Based Networks – An Example of the Republic of Korea’s Mask-Themed Stocks”, Industrial Engineering and Management Systems , 21(2), 244-266.
- Munki Chung, Yongjae Lee, Jang Ho Kim, Woo Chang Kim and Frank J. Fabozzi (2022) “The effects of errors in means, variances, and correlations on the mean-variance framework”, Quantitative Finance ,
- Insu Choi and Woo Chang Kim (2022) “정보 흐름 네트워크를 활용한 국제 금융 시장 지수의 분석 및 국내 시장 지수 등락 예측”, 대한산업공학회지 , 48(4), 340-355.
- Jinkyu Lee, Sanghyeon Bae, Woo Chang Kim, and Yongjae Lee (2022) “Value Function Gradient Learning for Large-Scale Multistage Stochastic Programming Problems”, European Journal of Operational Research ,
- Insu Choi\*, Woosang Lim\*, Doyoung Lee\*, Minseok Kim\*, Taechan Ahn\*, and Woo Chang Kim (2022) “미국 시장에서의 암호화폐 ETF 도입 가능성 분석: 시스템 리스크와 평균-분산 포트폴리오 이론의 관점에서”, 대한산업공학회지 , 48(5), 509-518.
- Guhyuk Chung, Munki Chung, Yongjae Lee, and Woo Chang Kim (2022) “Market Making under Order Stacking Framework: A Deep Reinforcement Learning Approach”, ICAIF '22: 3rd ACM International Conference on AI in Finance .
- Insu Choi, Wonje Yun, and Woo Chang Kim (2022) "Improving Data Efficiency for Analyzing Global Exchange Rate Fluctuations Based on Nonlinear Causal Network-Based Clustering", Annals of Operations Research ,
- Hyeongwoo Kong, Wonje Yun, Weonyoung Joo, Ju-Hyun Kim, Kyoung-Kuk Kim, Il-Chul Moon, and Woo Chang Kim (2022) "Constructing a personalized recommender system for life insurance products with machine-learning techniques", Intelligent Systems in Accounting, Finance and Management

**2021**

- Woong Bee Choi, Dongyeol Lee, and Woo Chang Kim (2021) "Extending the Scope of ALM to Social Investment: Investing in Population Growth to Enhance Sustainability of the Korean National Pension Service", Sustainability 13.1 ,  (2021): 401.
- Jang Ho Kim, Yongjae Lee, Jaekyu Bae, and Woo Chang Kim (2021) "Recent Trends and Perspectives on the Korean Asset Management Industry", Journal of Portfolio Management ,
- Insu Choi and Woo Chang Kim (2021) "Detecting and Analyzing Politically-Themed Stocks Using Text Mining Techniques and Transfer Entropy - Focus on the Republic of Korea's Case". Entropy , 23(6), 734; .
- Jang Ho Kim, Woo Chang Kim, and Frank J. Fabozzi (2021), "Sparse Factor Model Based on Trend Filtering", Annals of Operations Research, Published online
- Jang Ho Kim, Yongjae Lee, Woo Chang Kim, and Frank J. Fabozzi (2021), "Mean-Variance Optimization for Asset Allocation", Journal of Portfolio Management, 47(5), 24-40
- Dongyeol Lee and Woo Chang Kim (2021), "Cost of Shareholder Engagement by Institutional Investors under Short-Swing Profit Rule", Finance Research Letters, 40, 101700

## 학회 발표 목록

연구실 Research의 Select Presentations 목록이다. 연도는 원문에 명시된 발표일을 우선하고, 발표일에 연도가 없으면 해당 행의 학회 연도를 따랐다. 제목·저자·학회·장소·날짜는 게시 표기를 유지했다. 같은 연구가 위 논문 목록과 발표 목록에 함께 게시된 경우 각각의 행을 실었다.[^research]

**2023**

- Choi, I. & Kim, W. C. (November 2023). Analyzing Shifts Centered Around International Organizations in Gross Domestic Capital Formation and Gross Domestic Savings. 2023 Fall Conference of the Korean Institute of Industrial Engineers.
- Choi, I. & Kim, W. C. (November 2023). Hierarchical Risk Parity Portfolio Optimization via Nonlinear Measures Considering Finite Size Effects. 2023 Fall Conference of Korean Information Processing Society (ACK 2023).
- Choi, I. & Kim, W. C. (November 2023). Financial Asset Return Prediction via Whole-Graph Embedding Leveraging Histogram-Based Mutual Information. 2023 Fall Conference of Korean Information Processing Society (ACK 2023).
- Choi, I. & Kim, W. C. (October 2023). Generating Technical Indicators and Utilization in Forecasting Issues based on Dynamic Time Warping. 2023 Spring Conference of Korean Institute of Intelligent Systems.
- Choi, I., Lim, S., Kim, S., Choi, Y., Han, S., & Kim, W. C. (October 2023). Statistical Dependency Estimation and Analysis between Financial Time Series based on Information Distance. 2023 Spring Conference of Korean Institute of Intelligent Systems.
- Choi, I. & Kim, W. C. (October 2023). Dynamic Analysis of Spatiotemporal Exchange Rate Networks. 2023 Spring Conference of Korean Institute of Intelligent Systems.
- Choi, I., Koh, W., Jang, Y., Kang, G., & Kim, W. C. (September 2023). Linear and Monotonic Statistical Dependency-Oriented Financial Asset Return Prediction via Diffusion Recurrent Graph Learning-Based Spatiotemporal Graph Learning. 2023 4th Korea Artificial Intelligence Conference.
- Choi, I. & Kim, W. C. (August 2023). Elucidating Impacts of Pearson Correlation Coefficient-Based Statistical Dependency Measures in Downside Risk Prediction Problems - Focusing on Machine Learning Models and Explainable Artificial Intelligence (xAI) Techniques. 2023 Summer Conference of the Korean Academic Society of Business Administration.
- Choi, I. & Kim, W. C. (May 2023). An Explanatory Forecasting Model Using Graph Embedding in Information Entropy-Based Networks. 2023 Spring Conference of the Korean Society of Industrial and Systems Engineering.
- Choi, I., Koh, W., Kim, S., Lee, D., Choi, H., Han, S., & Kim, W. C. (May 2023). A Brief Review on the Sector and Industry Group-Based Analysis in the Financial Market. 2023 Spring Conference of the Korean Society of Industrial and Systems Engineering.
- Choi, I., Kim, D., Park, M., An, S., Lim, S., Lee, D., Jeong, Y., & Kim, W. C. (May 2023). Leveraging Entropy-Based Graph Topology and Deep Learning for Risk Boundary Prediction in Industrial Metals and Critical Minerals. 2023 Spring Conference of the Korean Data and Information Science Society.

**2022**

- Choi, I., Nam, D., Koh, W., Kim, S., Park, S., Park, M., Yang, H., Lee, D., Lim, S., Choi, H., & Kim, W. C. (December 2022). Developing a Dependency and Causal Network-Based Analysis Methodology for the Risk of Stock Price Returns of Financial Companies Using Entropic Value-At-Risk and Gini’s Mean Difference. 2022 Fall Conference of the Korean Institute of Information Technology.
- Choi, I. & Kim, W. C. (November 2022). Developing Fine Dust-Themed Stock Detection and Analysis Algorithm Using Linear and Nonlinear Measures. 2022 Fall Conference of Korean Institute of Intelligent Systems.
- Choi, I., Nam, D., Koh, W., Kim, S., Kim, S., Kim, S., Park, M., Park, S., Lee, D., Lim, S., Choi, H., Hong, J., & Kim, W. C. (November 2022). Demystifying Intra-Sector Stock Return Dependencies Using Technical Indicator-Driven Symbolic Variables-Based Networks. 2022 Fall Conference of the Korean Data and Information Science Society.
- Sanghyeon Bae and Woo Chang Kim (2022). "Optimal portfolio choice of couples with tax deferred accounts and survival contingent products. 2022 European Conference on Stochastic Optimization Computational Management Science.
- Insu Choi and Woo Chang Kim (2022). Development of a Commodity Futures Portfolio Optimization Framework Using the Topology of Nonparametric Dependency and Causality Networks. 2022 Summer Conference of the Korean Statistical Society. Seoul, Republic of Korea, June 2022.
- Insu Choi, Lee, J., Cho, Y., Choi, H., and Woo Chang Kim (2022). An Analysis of the Information Flow of Thematic Cryptocurrencies and Tokens Using Transfer Entropy and Network Topology. 2022 Spring Conference of the Korea Intelligent Information Systems Society. Daegu, Republic of Korea, June 2022.
- Insu Choi and Woo Chang Kim (2022). Predicting Fluctuations Based on Nonlinear Network Using Return Data of Global Financial Market Indices. 2022 Korean Economic Association 70th Anniversary International Conference. Seoul, Republic of Korea, June 2022.
- Insu Choi and Woo Chang Kim (2022). Developing and Applying the Information Flow Network of Global Financial Markets’ Entropic Value-at-Risk (EVaR). 2022 Annual Conference of the Korea Money and Finance Association. Seoul, Republic of Korea, June 2022.
- Munki Chung, Yongjae Lee, and Woo Chang Kim (2022). The Effects of Errors in Means, Variances, and Correlations on the Mean-Variance Framework. 2022 Spring Conference of Korean Institute of Information Technology. Jeju, Republic of Korea, June 2022.
- Chanyeong Kim and Woo Chang Kim (2022). Deep Reinforcement Learning for High-Frequency Pairs Trading. 2022 Spring Conference of Korean Institute of Information Technology. Jeju, Republic of Korea, June 2022.
- Insu Choi and Woo Chang Kim (2022). Financial Crisis-Based Analysis of Machine Learning Models on Binary Classification Problems Using Global Financial Market Return Data. 2022 Spring Conference of Korean Institute of Information Technology. Jeju, Republic of Korea, June 2022.
- Insu Choi\*, Minseok Kim\*, Woosang Lim\*, Doyoung Lee\*, Taechan Ahn\*, and Woo Chang Kim (2022). Analyzing the Possibility of Incorporating Cryptocurrency ETF Into the Korean Financial Market: From the Perspective of Systemic Risk and Mean-Variance Portfolio Theory. 2022 Spring Conference of Korean Institute of Information Technology. Jeju, Republic of Korea, June 2022.
- Insu Choi , Jiyoung Yoo, Soyeong Lim, Jueun Hong, Minyoung Park, and Woo Chang Kim (2021). Illustrating Research Trends and Constructing an Information Theory-Based Network of the Energy Futures Market. 2022 Joint Spring Conference of the Korean Institute of Industrial Engineers and Korean Operations Research and Management Science Society. Jeju, Republic of Korea, June 2022.
- Wonje Yun, Insu Choi, and Woo Chang Kim (2022). Comparison Between Correlation and Causality Networks and its Community Detection Results: Focus on the Stock Price Index of Republic of Korea. 2022 Joint Spring Conference of the Korean Institute of Industrial Engineers and Korean Operations Research and Management Science Society. Jeju, Republic of Korea, June 2022.
- Haeun Jeon, Insu Choi, and Woo Chang Kim (2022). Why Was My Loan Rejected and What Should I Do?. 2022 Joint Spring Conference of the Korean Institute of Industrial Engineers and Korean Operations Research and Management Science Society. Jeju, Republic of Korea, June 2022.
- Insu Choi and Woo Chang Kim (2022). Developing an Entropic Drawdown-at-Risk (EDaR) Fluctuation Forecasting Model for Commodity Futures Market Using Entropy-Based Dependency and Causality Network Modularity. 2022 Annual Spring Conference of Korean Information Processing Society (ASK 2022). Seoul, Republic of Korea, May 2022.
- Insu Choi\*, Hyemin Ju\*, Eunhye Yang\*, Seungwoo Han\*, and Woo Chang Kim (2022). Anticipating Bitcoin Price Fluctuation Based on a Sentiment Analysis-Driven Indicator and Macro-Economic Data. 2022 Annual Spring Conference of Korean Information Processing Society (ASK 2022). Seoul, Republic of Korea, May 2022.
- Insu Choi and Woo Chang Kim (2022). A Study on the Linear and Non-linear Financial Market Networks Based on the Empirical Characteristics of the Global Financial Market Return Distributions. 2022 Spring Conference of the Korean Data and Information Science Society. Busan, Republic of Korea, May 2022.

**2021**

- Insu Choi, Wonje Yun, and Woo Chang Kim. Forecasting Exchange Rate Fluctuations Using Nonlinear Causal Network Analysis and Deep Learning Techniques. 2021 Korean Association of Financial Engineering and Sungkyunkwan University International Conference of Finance. Seoul, Republic of Korea, December 2021.
- Insu Choi and Woo Chang Kim. Developing a Cryptocurrency Price Prediction Model Using Complex Network Analysis and Cryptocurrency Sentiment Index Derived from Transformer-Based Models. 2021 Joint Winter Conference of the International Society for Innovation Cluster, Korea Technology Innovation Society, and Korea Society for Innovation Management and Economics. Online, December 2021.
- Insu Choi and Woo Chang Kim. Developing an Explainable Financial Market Indices Prediction Model Using the Information Flow-Based Causal Network and Shapley Additive Explanations (SHAP) Interaction Values. 2021 Fall Conference of the Korea Intelligent Information Systems Society. Online, December 2021.
- Insu Choi, Dalli Nam., and Woo Chang Kim. Designing a Reinforcement Learning-Based Investment Model Using Environmental, Social, and Governance (ESG) Indicators and Fundamental, Technical, and Sentimental Analysis Results Based on the Decision-Making Process Derived from Causality Measures and Explainable Artificial Intelligence Techniques. 2021 Fall Conference of the Korean Data and Information Science Society. Seoul, Republic of Korea, November 2021.
- Insu Choi and Woo Chang Kim. Metaverse and Non-Fungible Token Buying Surge in 2021 – Price Prediction Model of Non-Fungible Token-Related Cryptocurrencies and Stocks Based on the Sentiment Analysis and Causal Network Analysis. 2021 Fall Conference of Knowledge Management Society Korea, Online, November 2021.
- Insu Choi and Woo Chang Kim. A Legal Tender-Based Gold Price Prediction Model Based on Transfer Entropy, Network Clustering Algorithms, and Machine Learning Techniques. 2021 Fall Conference of the Korean Operations Research and Management Science Society, Seoul, Republic of Korea, November 2021.
- Insu Choi and Woo Chang Kim. Predicting the Korean Stock Market Indices Using Macroeconomic Indicators and Causality Measures and Analyzing Important Features Using Explainable Artificial Intelligence Techniques. 2021 Fall Conference of the Korean Society of Management Consulting. Seoul, Republic of Korea, November 2021.
- Insu Choi and Woo Chang Kim. Politically-Themed Stocks Revisited: Analyzing Politically-Themed Stocks Using Natural Language Processing Techniques, Information Theory, and Complex Network Dynamics. 17th Korea Institute of Industrial Engineers Master Thesis Competition, Seoul, Republic of Korea, November 2021.
- Insu Choi, Dalli Nam., Minjin Koo, Youkyoung Kong, Soyoung Lim, and Woo Chang Kim. Current Status of Global Environmental, Social, and Governance (ESG) Investment Paradigm Shift and Related Major Research. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Insu Choi, Dalli Nam., Tae Kyoung Kim, Doyoung Lee, Hyemin Joo, and Woo Chang Kim. Trend Analysis of Sustainable Service Models of Global Companies Combined with FinTech, TechFin, and Environmental, Social, and Governance (ESG) Management: A Multiple Case Study. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Insu Choi, Dalli Nam., Hyun Kim, Minjin Koo, Tae Kyoung Kim, Jaeyoung Kim, Soyoung Lim, and Woo Chang Kim. Empirically Analyzing the Importance of Environmental, Social, and Governance (ESG) Interests and Indicators for Forecasting Stock Prices in the Manufacturing and Logistics Industry Using Linear and Nonlinear Causality Measures and Explainable Artificial Intelligence Techniques. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Insu Choi, Dalli Nam., and Woo Chang Kim. Developing a Sustainable Portfolio Using Environmental, Social, and Governance (ESG) and Human Capital Concept – Focus On the Republic of Korea’s Case. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Insu Choi, Sangjae Lee, Yejin Han, Soyoung Bang, and Woo Chang Kim. Developing a Financial Asset Portfolio Recommender Service Using Human Capital-Based Data-Driven Persona and Black-Litterman Model. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Insu Choi, Eunhye Yang, Subeen Yang, and Woo Chang Kim. Developing an Exchange Trade Fund (ETF) Black-Litterman Model-Based Bottom-up Investment Strategy Using Shapley Additive Explanations (SHAP) Values and Causality Measures. 2021 Fall Conference of the Korean Institute of Industrial Engineers, Seoul, Republic of Korea, November 2021.
- Wonje Yun, Insu Choi, and Woo Chang Kim. Evaluation of Owner Reputation Risk Based on Text Sentiment Analysis Using Online News Title – Focus On Korean Conglomerate Firms. 2021 Fall Conference of the Korean Institute of Industrial Engineers. Written in Korean.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제다. 기간·지원기관·상태는 게시 표기이며, On going·Finished는 연구실이 붙인 분류다.[^projects]

- 심층 강화학습을 활용한 확장 및 설명 가능 생애주기 자산관리 모델 개발 (기간 2023.03. - 2024.02.; 지원 한국연구재단; 상태 On going)
- 투자용 기술력 평가모형 개발 및 업그레이드 (기간 2022.01. - 2022.06.; 지원 한국신용정보원; 상태 Finished)
- 금융 데이터 기반 시장 가치 모형 개발 (기간 2021.08. - 2022.01.; 지원 신한은행; 상태 Finished)
- 대규모 개인 맞춤형 생애주기 자산 관리 문제의 제약적 강화학습 기반 최적해 도출 (기간 2021.03. - 2022.02.; 지원 한국연구재단; 상태 Finished)
- 강화학습을 활용한 고빈도 트레이딩 모형 개발 (기간 2020.12. - 2021.12.; 지원 (주)하나은행; 상태 Finished)
- 초단기 알고리즘 불공정 거래 적출 AI모델 개발 (기간 2021.07. - 2021.12.; 지원 (주)한국거래소; 상태 Finished)

## 수상과 선정

2021년 11월–2024년 11월 News 페이지에 게시된 수상·선정이다. 사람의 과정은 소식 게시 당시 표기를 따른다.[^news]

- 2024-11 · 최인수 박사과정, 2024 한국경영과학회 추계학술대회 경쟁부문 우수논문상 수상
- 2024-11 · 최인수 박사과정, 2024 제11회 한국경영과학회 박사논문 우수논문 부문 우수논문상 수상
- 2024-05 · 최인수 박사과정, 2024 한국데이터정보과학회 춘계학술대회 박사과정 우수발표논문 부문 수상
- 2023-12 · 최인수 박사과정, 제1회 S&P Global-KAIST-UNIST-경희대학교 퀀트 투자 경진대회 특별상 수상
- 2023-11 · 배형립 박사과정 및 김찬영 박사과정, 2023 K-데이터사이언스 컨퍼런스 & 해커톤 연구발표 창의상 수상
- 2023-11 · 최인수 박사과정, 제4회 NH투자증권 빅데이터 경진대회 입선 수상
- 2023-11 · 최인수 박사과정, 2023 한국산업경영시스템학회 추계학술대회 우수발표논문상 수상
- 2023-11 · 최인수 박사과정, 2023 한국경영과학회 추계학술대회 경쟁부문 우수논문상 수상
- 2023-11 · 최인수 박사과정, 2023 한국데이터정보과학회 추계학술대회 박사과정 우수발표논문 부문 수상
- 2023-06 · 최인수 박사과정, 2023 한국정책학회 대학원생 논문 및 캡스톤디자인 공모전 우수논문 수상
- 2023-05 · 최인수 박사과정, 2023 한국데이터정보과학회 춘계학술대회 박사과정 우수발표논문 부문 수상
- 2022-12 · 최인수 박사과정, 제3회 NH투자증권 빅데이터 경진대회 장려상 수상
- 2022-12 · 최인수 박사과정, 2022 한국정보기술학회 추계종합학술대회 일반부문 우수논문상 수상
- 2022-11 · 최인수 박사과정, 제2회 디지털산업혁신 빅데이터 플랫폼 금융 아이디어 경진대회 대상 수상
- 2022-11 · 이진규 박사과정, 2022 한국경영과학회 시상 한국경영과학회지 최우수논문상 수상
- 2022-11 · 최인수 박사과정, 2022 한국데이터정보과학회 추계학술대회 박사과정 우수발표논문 부문 수상
- 2022-11 · 최인수 박사과정, KAIST ISySE & GSDS 산업/사회 문제 해결 포스터 경진대회 대상 수상
- 2022-11 · 최인수 박사과정, 2022 한국산업경영시스템학회 추계학술대회 우수발표논문상 수상
- 2022-08 · 최인수 박사과정, 김영한 글로벌리더 장학생 선정 및 장학금 수여
- 2022-06 · 최인수 박사과정, 2022 한국통계학회 하계학술논문발표회 발표논문부문 장려상 수상
- 2022-06 · 최인수 박사과정, 2022 한국정보기술학회 하계종합학술대회 일반부문 우수논문상 수상
- 2022-05 · 최인수 박사과정, 2022 한국데이터정보과학회 춘계학술대회 박사과정 우수발표논문 부문 수상
- 2021-12 · 최인수 박사과정, 한국지능정보사회진흥원 (NIA) 주최 제9회 빅콘테스트 운영위원장상 수상
- 2021-11 · 이진규 박사과정, 2021 한국경영과학회 경영과학 박사학위 우수논문 부문 최우수논문상 수상
- 2021-11 · 최인수 박사과정, 2021 한국데이터정보과학회 추계학술대회 박사과정 우수발표논문 부문 수상
- 2021-11 · 최인수 박사과정, 제2회 NH투자증권 빅데이터 경진대회 장려상 수상
- 2021-11 · 최인수 박사과정, 제17회 대한산업공학회 석사논문경진대회 우수논문상 수상

## 연락과 위치

- 교수 이메일: wkim@kaist.ac.kr[^gsds]
- 교수 전화: +82-42-350-3129[^team]
- 교수 연구실: IE B/D E2-2 #3107[^team]
- 연구실: KAIST 산업및시스템공학과 E2-2 #3117, 대전광역시 유성구 대학로 291, 우편번호 34141[^team]
- 연구실 전화: +82-42-350-3169[^team]

## 각주
[^home]: Financial Engineering Lab., 첫 화면. <https://felab.kaist.ac.kr/> 관측일 2026-10-30.
[^team]: Financial Engineering Lab., Team, 교수 경력·직위·학력과 현재 구성원, 연락·위치. <https://felab.kaist.ac.kr/team.html> 관측일 2026-10-31.
[^research]: Financial Engineering Lab., Research, AI for Finance·FinTech·Investment Management·Financial Optimization 소개와 Publications. <https://felab.kaist.ac.kr/research.html> 관측일 2026-10-31.
[^projects]: Financial Engineering Lab., Projects, 과제명·수행 기간·지원기관·게시 분류. <https://felab.kaist.ac.kr/projects.html> 관측일 2026-10-31.
[^alumni]: Financial Engineering Lab., Alumni, 박사·석사 학위와 진로·학위 논문. <https://felab.kaist.ac.kr/alumni.html> 관측일 2026-10-31.
[^news]: Financial Engineering Lab., News, 수상과 선정. <https://felab.kaist.ac.kr/news.html> 관측일 2026-10-31.
[^gsds]: KAIST 데이터사이언스대학원, People, 김우창의 이름·Focus Area·이메일·전화·홈페이지. <https://gsds.kaist.ac.kr/people> 관측일 2026-10-30.

[^p1]: H. Jeon 외, W. C. Kim, ICML 2026 (arXiv 판) (온라인 2026-07-01). <https://doi.org/10.48550/arXiv.2607.00581> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2607.00581> 관측일 2026-10-31.
[^p2]: H. Jeon 외, W. C. Kim, AAAI 2025 (arXiv 판) (온라인 2024-03-04). <https://doi.org/10.48550/arXiv.2403.01875> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.01875> 관측일 2026-10-31.
[^p3]: C. Kim, J. Park, H. Bae, W. C. Kim, Proceedings of the 40th International Conference on Machine Learning 202, 16747-16770 (2023). <https://proceedings.mlr.press/v202/kim23r.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/kim23r.html> 관측일 2026-10-31.
[^p4]: H. Bae, J. Lee, W. C. Kim, Y. Lee, Proceedings of The 26th International Conference on Artificial Intelligence and Statistics 206, 11267-11287 (2023). <https://proceedings.mlr.press/v206/bae23a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v206/bae23a.html> 관측일 2026-10-31.
[^p5]: J. Lee, S. Bae, W. C. Kim, Y. Lee, arXiv (온라인 2022-05-18). <https://doi.org/10.48550/arXiv.2205.08934> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2205.08934> 관측일 2026-10-31.
[^p6]: W. Koh 외, W. C. Kim, AAAI 2024 AI4TS Workshop (arXiv 판) (온라인 2023-11-22). <https://doi.org/10.48550/arXiv.2311.13326> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2311.13326> 관측일 2026-10-31.
[^p7]: J. Ko, K. Kim, W. C. Kim, J. R. Gardner, ICML 2024 (arXiv v2 판) (온라인 2024-01-19). <https://doi.org/10.48550/arXiv.2401.10989> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2401.10989v2> 관측일 2026-10-31.
[^p8]: M. Kim 외, Y. Bengio, Proceedings of the 41st International Conference on Machine Learning 235, 24248-24270 (2024). <https://proceedings.mlr.press/v235/kim24s.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/kim24s.html> 관측일 2026-10-31.

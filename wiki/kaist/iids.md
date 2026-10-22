# 데이터과학을 위한 추론 및 정보 연구실 (Inference and Information for Data Science Lab, IIDS Lab)

**KAIST 전기및전자공학부 · 정혜원 교수**

- 분야: 데이터 과학, 정보 이론, 통계 추론, 머신 러닝, 양자 정보
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 통계적 추론·검정[^home][^p3], 그래프 기계학습·지식 그래프[^p1][^news], 멀티모달 AI[^p6]
- 홈페이지: <https://iids.kaist.ac.kr/>
- 근거와 출처: [데이터과학을 위한 추론 및 정보 연구실 근거 페이지](iids-sources.md)

> 정보 이론과 통계적 추론의 도구로 데이터 과학의 이론 틀과 효율적인 알고리즘을 만드는 연구실이다. 연결망 짝 맞추기, 크라우드소싱 답 모으기, 무작위 행렬 속 약한 신호 검출의 근본 한계를 밝히는 이론 연구와, 적은 데이터와 계산으로 학습하는 딥러닝 방법 연구를 함께 한다.[^home][^research][^pubs]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 정혜원 교수가 이끄는 연구실이다.[^home][^ee] 연구 페이지는 연구 목표를 정보를 평가하고, 모으고, 뽑아내고, 활용하는 효율적인 전략으로 이어질 정보 과학의 이론·알고리즘 틀을 마련하는 것이라고 적는다. 데이터가 넘쳐나는 시대에 크고 풍부한 데이터 묶음을 충분히 써서 데이터 뒤에 있는 실제 현상을 효율적으로 추론하려 하며, 정보 이론(정보를 얼마나 줄여 담고 전달할 수 있는지 그 한계를 수학으로 다루는 이론)의 개념과 도구가 데이터에서 정보를 뽑아낼 때의 근본 한계를 세우고 득실을 따지는 데 쓸모 있다고 설명한다. 빅데이터를 처리하는 실제 정보 처리기를 만들 때 생기는 새 과제를 다루려면 고전적인 정보 이론의 해법을 넘어서는 새 기법과 개념도 필요하다고 덧붙인다.[^research]

연구의 초점은 결정을 제때 내야 하는 조건, 제한된 측정 자원, 데이터 처리의 계산 효율 같은 현실의 제약을 감당하는 데이터 과학의 이론 틀이다. 연구 페이지가 드는 질문은 이렇다. 가장 낮은 비용으로 알 수 없는 목표 값을 추정하려면 가장 관련 있는 관측을 얻도록 측정 전략을 어떻게 짤 것인가. 정보의 가치를 어떻게 수치로 매기고, 제한된 측정 자원으로 가장 가치 있는 정보를 어떻게 뽑아낼 것인가. 잡음이 섞인 많은 관측에서 정보를 효율적으로 되살리는 절차를 어떻게 설계할 것인가. 신뢰도를 모르는 여러 사람에게 나눠 묻는 질의를 어떻게 설계해 쓸모 있는 관측을 효율적으로 모을 것인가. 연구실은 이런 데이터 수집과 정보 복원 문제의 알고리즘을 만들고, 확률론·정보 이론·확률 해석(무작위로 변하는 대상을 다루는 수학 분석)의 도구로 그 알고리즘의 성능을 보장한다.[^research]

누리집 첫 화면의 교수 소개는 연구 관심을 데이터 과학, 정보 이론, 통계적 추론(관측한 자료로 그 뒤의 알 수 없는 값이나 가설을 판단하는 방법), 기계학습, 양자 정보로 적는다. 정보 이론·통계적 추론·기계학습의 도구로 데이터 과학에 이론 틀을 주고, 통계적 추론 문제에서 정보를 뽑아 쓰는 효율적인 알고리즘 도구를 만들려 한다고 쓴다.[^home] 반도체시스템공학과 연구실 목록은 연구실의 주제를 통계적 추론과 정보이론, 데이터사이언스 분야의 시스템 관점 분석, 효율적 추론 알고리즘 개발로 적는다.[^sselab]

누리집은 최근 주요 논문을 두 갈래로 묶는다. 하나는 데이터 과학과 기계학습의 알고리즘과 이론이고, 다른 하나는 효율적인 딥러닝과 견고하고 신뢰할 수 있는 AI다.[^research][^home] 대표 논문으로 보면 첫 갈래에는 네 주제가 있다. 첫째, 서로 닮은 두 연결망에서 점끼리의 대응을 찾는 그래프 매칭과, 이를 이용해 연결망 안에서 서로 촘촘히 이어진 점의 무리를 찾는 커뮤니티 탐지다(대표 논문 1).[^p1] 둘째, 실력이 작업마다 다른 여러 작업자의 답을 모아 올바른 정답 표시를 추론하는 크라우드소싱(여러 사람에게 작업을 나눠 맡겨 답을 모으는 방식) 추론이다(대표 논문 2).[^p2] 셋째, 잡음으로 채운 무작위 행렬 속에 약한 신호가 있는지를 가려내는 검출의 근본 한계다(대표 논문 3).[^p3] 넷째, 행렬 완성(일부 칸만 관측된 행렬의 나머지 칸을 채우는 문제)에서 경사 하강법(함숫값이 줄어드는 방향으로 값을 조금씩 고쳐 가는 최적화 방법)이 왜 정답으로 수렴하는지를 밝히는 학습 이론이다(대표 논문 4).[^p4] 둘째 갈래에는 모델을 학습시키지 않고 데이터 하나하나의 가치를 매기는 방법(대표 논문 5), 그림-글 쌍 데이터의 데이터셋 증류(큰 데이터 묶음을 대신해 학습에 쓸 작은 합성 데이터를 만드는 일)(대표 논문 6), 자기 증류(학습한 모델의 예측을 같은 구조의 모델이 다시 배우는 방법)의 작동 원리(대표 논문 7), 시험 때 바뀐 데이터 분포에 모델을 맞추는 테스트 시점 적응(대표 논문 8)이 있다.[^p5][^p6][^p7][^p8]

최근 논문 목록에는 그림과 글을 함께 배우는 CLIP 모델의 사전 학습 데이터 가치를 매기는 InfCLIP(NeurIPS 2026 채택), 견고한 교사 모델(지식을 넘겨주는 쪽 모델)이 적대적 증류(일부러 조금 바꾼 교란 입력에 강한 교사 모델을 따라 학생 모델도 교란에 강해지도록 배우게 하는 방법)에서 왜 실패하는지 살핀 연구(ICML 2026), 넓은 범위의 비율에서 쓰는 데이터 가지치기(학습 데이터에서 일부만 골라 남기는 일) 방법 BWS와 데이터셋 증류 방법 SelMatch(ICML 2024), 상관된 연결망에서 그래프 매칭으로 커뮤니티 복원을 개선하는 연구(ISIT 2025)도 있다.[^pubs]

## 주요 연구 주제

### 1. 연결망 짝 맞추기와 커뮤니티 탐지의 근본 한계

점의 속성과 연결이 함께 상관된 두 연결망에서 점의 대응을 정확히 찾는 조건과 알고리즘, 짝을 맞춘 연결망을 합쳐 커뮤니티 탐지를 강화하는 방법.[^p1] 상관된 확률적 블록 모형(점이 속한 무리에 따라 두 점이 이어질 확률이 정해지는 무작위 연결망 모형)에서 정확한 그래프 매칭을 하는 효율적 알고리즘(ICML 2023)도 같은 갈래다.[^pubs] 교수는 2024년 ISIT에서 Lele Wang(UBC)과 함께 「Graph Matching: Fundamental Limits and Efficient Algorithms」 튜토리얼을 열었다.[^news] 대표 논문 1.

### 2. 크라우드소싱 답 모으기의 추론

작업과 작업자의 유형에 따라 답의 신뢰도가 달라지는 모형에서 필요한 답의 수의 한계와 정답 추론 알고리즘.[^p2] 여러 선택지 문제에서 가장 그럴듯한 두 답과 그 둘을 헷갈릴 확률을 되살리는 연구(ICML 2023)와 이 모형을 일반화한 연구(ISIT 2022)도 있다.[^pubs] 대표 논문 2.

### 3. 무작위 행렬 속 약한 신호의 검출

스파이크 위그너 모형(잡음으로 채운 대칭 무작위 행렬에 한 방향의 신호를 더한 모형)에서 신호가 있는 경우와 없는 경우를 가려내는 검정(자료로 가설이 맞는지 판단하는 절차)의 극한 성질과 근본 한계.[^p3] 스파이크 무작위 행렬 모형의 검출 문제(IEEE TIT 2024), 스파이크 직사각 모형의 신호 검출(ICML 2021), 스파이크 위그너 모형의 약한 검출(IEEE TIT 2022)이 같은 갈래다.[^pubs] 대표 논문 3.

### 4. 학습 알고리즘의 이론

작은 무작위 초기값에서 출발한 경사 하강법이 랭크 1 행렬(두 벡터의 곱으로 나타낼 수 있는 행렬)의 완성에서 정답으로 수렴함을 증명한 연구.[^p4] 대표 논문 4.

### 5. 데이터 효율 학습

모델을 학습시키지 않고 계산하는 데이터 가치 점수, 그림-글 쌍의 데이터셋 증류, 데이터 가지치기.[^p5][^p6][^pubs] 누리집 소식에 따르면 연구실의 데이터 효율 학습 연구는 2025년 한국연구재단 중견연구 지원(NRF Mid-Career Research Funding, Leap Research Program)에 선정됐다.[^news] 대표 논문 5, 6.

### 6. 증류와 견고한 학습

여러 번 반복하는 자기 증류가 레이블(데이터에 붙인 정답 표시)을 평균내는 효과의 분석과 한 번에 끝나는 부분 레이블 증류, 레이블 분포가 바뀐 시험 데이터에 맞춘 테스트 시점 적응.[^p7][^p8] 적대적 증류(ICML 2026, TMLR 2026), 일부 종류에만 데이터가 몰린 긴 꼬리 학습에서 분포 밖 데이터(학습 때 보지 못한 종류의 입력)를 검출하는 연구(TMLR 2024)도 있다.[^pubs] 대표 논문 7, 8.

## 대표 논문

최근 5년 논문 가운데 정혜원 교수가 저자인 것에서 연구 갈래마다 고르게 골랐다. 8편 가운데 7편은 교수가 마지막 저자이고, 대표 논문 3은 교수가 첫 저자다. 누리집 목록은 교신저자를 따로 표시하지 않는다.[^pubs] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Exact Matching in Correlated Networks with Node Attributes for Improved Community Recovery](https://doi.org/10.1109/tit.2025.3592704) · IEEE Transactions on Information Theory | 여러 연결망에서 점(예를 들면 사용자)의 속성과 연결이 함께 상관된 상황의 커뮤니티 탐지를 연구했다. 소셜 플랫폼처럼 같은 사용자들이 여러 플랫폼에서 서로 상관된 친구 관계와 속성을 보이는 경우에 자연스럽게 생기는 상황이다. 연구진은 고전적인 확률적 블록 모형(SBM)과 여기에 점의 속성을 더한 문맥 SBM(CSBM)을 넓혀, 그래프 사이의 구조·속성 상관을 담은 상관 CSBM을 도입했다. 먼저 연결 없이 상관된 속성만 있는 상관 가우스 혼합 모형(여러 정규분포를 섞어 만든 확률 모형)을 분석해, 속성 사이의 거리를 가장 작게 만드는 추정량(관측값으로 알 수 없는 값을 짐작하는 계산 규칙)이 두 데이터베이스의 점을 정확히 짝짓는 조건을 밝혔다. 상관 CSBM에 대해서는 연결 정보로 대부분의 점을 k-코어 매칭(모든 점이 그 안에서 k개 이상의 점과 이어진 부분 연결망을 기준으로 짝짓는 방법)으로 먼저 짝짓고, 남은 점은 속성 거리 기반 추정량으로 짝을 다듬는 두 단계 방법을 만들어 이 방법이 점의 대응을 정확히 찾는 조건을 밝혔다. 정확히 짝지으면 상관된 연결을 합치고 속성을 평균내 커뮤니티 탐지를 강화할 수 있다. 특히 그래프를 맞추어 합치면, 그래프 하나만으로는 커뮤니티 탐지가 불가능하지만 상관된 그래프의 부가 정보를 더하면 가능해지는 영역이 있음을 밝혔다.[^p1] | 1저자 J. Yang, 마지막 저자 정혜원 |
| 2 | 2024 | [A Worker-Task Specialization Model for Crowdsourcing: Efficient Inference and Fundamental Limits](https://doi.org/10.1109/tit.2023.3315720) · IEEE Transactions on Information Theory | 크라우드소싱 시스템은 전문가가 아닌 작업자를 써서 비교적 적은 비용으로 데이터에 정답 표시(레이블)를 다는 플랫폼이 됐다. 그러나 답의 질이 작업과 작업자에 따라 크게 달라, 한 데이터에 대한 여러 개의 잡음 섞인 답에서 올바른 레이블을 추론하기는 어렵다. 기존 연구 다수는 작업자의 실력에 고정된 순서가 있다고 가정하고, 실력을 추정해 작업자마다 다른 가중치로 답을 모으는 데 집중했다. 실제로는 특히 작업들이 서로 다를 때 작업자의 실력이 작업마다 크게 바뀐다. 이 논문은 작업과 작업자마다 알려지지 않은 유형이 있고 작업자의 신뢰도가 작업의 유형과 작업자의 유형에 따라 달라지는 d-유형 특화 모형을 제안했다. 유형의 수 d가 작업 수에 따라 커지는 경우도 허용한다. 이 모형에서 정해진 정확도 안으로 레이블을 추론하는 데 필요한 최적 표본 복잡도(필요한 관측의 수)를 밝히고, 작업이나 작업자의 유형을 모를 때에도 상수배 차이 안에서 최적 한계에 이르는 레이블 추론 알고리즘을 제안했다. 합성 데이터와 실제 데이터 실험에서 더 엄격한 모형 가정에 기반한 기존 알고리즘보다 좋은 성능을 보였다.[^p2] | 1저자 D. Kim, 3명 중 마지막 저자 정혜원 |
| 3 | 2025 | [Asymptotic Normality of Log-Likelihood Ratio and Fundamental Limit of the Weak Detection for Spiked Wigner Matrices](https://doi.org/10.3150/24-bej1805) · Bernoulli | 랭크 1 스파이크 위그너 모형(잡음으로 채운 대칭 무작위 행렬에 한 방향의 신호를 더한 모형)에서 신호가 있는지를 가려내는 검출 문제를 다룬다. 잡음이 정규분포가 아닌 일반적인 분포이고 신호가 라데마허 사전분포(각 성분이 같은 크기의 양수나 음수 값을 같은 확률로 갖는 분포)에서 뽑힌다고 두고, 신호 대 잡음비가 어떤 문턱값보다 낮으면 신호가 있는 모형과 없는 모형의 로그 가능도비(관측 자료가 두 모형 가운데 어느 쪽에서 나왔을 법한지를 견주는 비의 로그)가 정규분포로 수렴함을 증명했다. 이 문턱값보다 높으면 변환한 주성분 분석(PCA, 자료가 가장 크게 퍼진 방향을 찾는 방법)으로 믿을 만한 검출이 가능하다는 뜻에서 이 문턱값은 최적이다. 극한 정규분포의 평균과 분산으로 가능도비 검정의 1종 오류(신호가 없는데 있다고 판단하는 잘못)와 2종 오류(신호가 있는데 없다고 판단하는 잘못)의 합의 극한을 계산했다. 잡음은 비대칭이지만 신호는 대칭인 랭크 1 스파이크 IID 모형(행렬 성분의 잡음이 서로 독립이고 같은 분포를 따르는 모형)에서도 비슷한 결과를 증명했다.[^p3] | 1저자 정혜원, 3명 중 마지막 저자 J. O. Lee |
| 4 | 2023 | [Rank-1 Matrix Completion with Gradient Descent and Small Random Initialization](https://doi.org/10.52202/075280-0463) · NeurIPS 2023 | 행렬 완성 문제의 비볼록 정식화(국소 최솟값이 여럿 생길 수 있는 꼴로 최적화 문제를 세우는 방식)는 볼록 정식화보다 계산량이 감당할 만해 최근 큰 관심을 받았다. 경사 하강법(GD, 함숫값이 줄어드는 방향으로 값을 조금씩 고쳐 가는 최적화 방법)은 비볼록 최적화 문제를 푸는 단순하면서도 효율적인 기본 알고리즘이고, 무작위 초기화와 함께 쓸 때 이론과 실제의 여러 문제에서 성공을 보여 왔다. 그러나 기존 행렬 완성 연구는 GD의 수렴을 증명하려면 신중한 초기화나 정규화 항이 필요했다. 이 논문은 랭크 1 대칭 행렬 완성에서 작은 무작위 초기값을 쓰면 GD가 참값으로 수렴함을 증명했다. 로그 규모의 반복 횟수 안에 경로가 국소 수렴이 일어나는 영역으로 들어감을 보였고, 수렴을 보장하는 초기값 크기의 상한을 주었으며, 표본이 많을수록 더 큰 초기값을 쓸 수 있음을 보였다. 분석에서는 GD의 암묵적 정규화 효과(따로 장치를 두지 않아도 알고리즘 자체가 해를 특정 성질 쪽으로 이끄는 효과)가 결정적인 역할을 하며, 전체 경로에서 어느 한 성분이 다른 성분보다 훨씬 커지지 않도록 막는다는 점을 관찰했다.[^p4] | 1저자 D. Kim, 마지막 저자 정혜원 |
| 5 | 2023 | [Data Valuation without Training of a Model](https://arxiv.org/abs/2301.00930) · ICLR 2023 | 딥러닝을 이해하려는 최근 연구 다수는 데이터 하나하나가 모델의 최적화와 일반화(처음 보는 데이터에서도 잘 맞히는 능력)에 얼마나 영향을 주는지 수치로 따지려 한다. 이런 시도는 개별 데이터의 특성과 중요도를 드러내 딥러닝을 진단하고 개선하는 데 쓸모 있는 정보를 줄 수 있다. 그러나 기존 데이터 가치 평가 연구 대부분은 모델을 실제로 학습시켜야 해 계산 비용이 큰 경우가 많다. 이 논문은 학습 없이 계산하는 데이터 가치 점수인 복잡도 격차 점수(complexity-gap score)를 제안했다. 이 점수는 과매개변수화된(매개변수가 학습 데이터에 비해 많은) 2층 신경망의 일반화에 개별 데이터가 주는 영향을 데이터 중심으로 수치화하며, 데이터의 불규칙성과, 학습 중 신경망 매개변수가 움직인 전체 양에 각 데이터가 얼마나 기여하는지를 잰다. 이 점수가 '불규칙하거나 잘못 표시된' 데이터를 찾는 데 효과적임을 이론 분석과 실험으로 보였고, 데이터 묶음을 분석하고 학습 과정을 진단하는 데 쓰는 예도 제시했다.[^p5] | 공동 1저자 N. Ki·H. Choi(\*), 3명 중 마지막 저자 정혜원 |
| 6 | 2025 | [CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder](https://doi.org/10.52202/085713-3398) · NeurIPS 2025 | 멀티모달 데이터셋 증류는 대규모 비전-언어 모델(그림과 글을 함께 다루는 인공지능 모델)을 효율적으로 학습시킬 수 있는 작은 그림-글 쌍 묶음을 합성하는 것을 목표로 한다. 데이터셋 증류는 한 종류의 자료만 쓰는 과제에서 가능성을 보였지만, 멀티모달 대조 학습(짝이 맞는 그림과 글은 가깝게, 맞지 않는 짝은 멀게 표현하도록 배우는 방식)으로 넓히면 서로 다른 종류의 자료 사이 정렬을 배우는 일과 큰 인코더(입력을 특징 벡터로 바꾸는 신경망)의 높은 계산 비용이 과제가 된다. 기존 방법은 규모 문제를 피하려고 글 인코더를 고정하고 그림 인코더와 글 투영 층만 갱신하는데, 연구진은 이 방식이 의미 정렬을 크게 제한해 성능 향상의 병목이 된다는 것을 발견했다. 연구진은 실제 특징과 합성 특징의 교차 공분산(두 종류 특징이 함께 변하는 정도를 모은 행렬)을 맞추고 각 자료 종류 안의 특징 분포를 정규화하는 데이터셋 증류 틀 CovMatch를 제안했다. CovMatch는 두 인코더를 함께 최적화할 수 있어 서로 다른 자료 사이의 정렬이 강해지고 성능이 좋아진다. Flickr30K와 COCO에서 평가한 결과, 합성 쌍 500개만으로 기존 최고 수준의 멀티모달 증류 방법보다 검색 정확도를 절대 기준으로 최대 6.8% 높였다.[^p6] | 1저자 Y. Lee, 마지막 저자 정혜원 |
| 7 | 2025 | [Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels](https://arxiv.org/abs/2402.10482) · ICLR 2025 | 이 논문은 여러 종류로 나누는 다중 분류에서 자기 증류(학습한 모델의 예측을 같은 구조의 모델이 다시 배우는 방법)가 어떻게 작동하는지 살폈다. 특히 특징 추출기를 고정하고 마지막 선형 분류기만 학습하는 선형 탐침(linear probing) 상황을 다루는데, 이때는 특징 학습으로 설명하는 기존 해석이 적용되지 않는다. 이론 분석 결과, 여러 번 반복하는 자기 증류는 입력 특징으로 만든 그람 행렬(데이터 쌍마다 두 특징 벡터의 성분끼리 곱해 더한 값을 모은 행렬)의 고유벡터(행렬을 곱해도 방향이 바뀌지 않는 벡터)에 따라 특징 상관이 높은 데이터끼리 레이블을 평균내는 효과를 낸다. 이 과정은 예측을 무리 짓게 하고 일반화를 높이며, 잘못 붙었을 수 있는 레이블에 모델이 덜 기대게 해 레이블 잡음의 영향을 줄인다. 레이블 잡음이 있어도 여러 번의 자기 증류가 모집단 전체에 대한 정확도 100%에 이르는 조건을 밝혔다. 또 교사 모델의 소프트맥스 출력(정답 후보마다 매긴 확률) 가운데 상위 두 개로 다듬은 부분 레이블을 쓰는 한 번짜리 자기 증류 방법(PLL 학생 모델)을 제안했다. 이 방법은 여러 번 증류의 이점을 한 번에 재현해, 특히 잡음이 많은 상황에서 비슷하거나 더 좋은 성능을 내면서 계산 비용을 크게 줄인다.[^p7] | 1저자 H. Jeong, 마지막 저자 정혜원 |
| 8 | 2025 | [Label Distribution Shift-Aware Prediction Refinement for Test Time Adaptation](https://arxiv.org/abs/2411.15204) · TMLR | 테스트 시점 적응(TTA, 이미 학습한 모델을 시험 때 들어오는 데이터에 맞춰 고치는 방법)은 시험 때 입력 분포가 바뀌어 성능이 떨어지는 것을 줄이는 효과적인 방법이다. 그러나 기존 TTA 방법은 정답 종류(클래스)의 분포까지 함께 바뀌면 성능이 크게 떨어지는 경우가 많다. 연구진은 레이블 분포가 바뀌는 상황에서 TTA 방법을 분석해, 서로 다른 입력 분포 변화에서도 공통으로 나타나는 클래스별 혼동 패턴이 있음을 확인했다. 이를 바탕으로 클래스별 혼동 패턴에 집중해 예측을 다듬는 TTA 방법 DART를 제안했다. DART는 학습과 시험 사이의 중간 단계에서 학습 데이터로 클래스 분포가 서로 다른 여러 묶음을 보여 주며 예측 보정 모듈을 학습시키고, 시험 때 이 모듈로 클래스 분포 변화를 찾아 바로잡아 시험 데이터에 스스로 붙인 추정 정답(가짜 레이블)의 정확도를 크게 높인다. CIFAR-10C에서 레이블 분포가 바뀐 경우 정확도를 5–18% 높였고, 바뀌지 않은 경우에는 성능이 떨어지지 않았다. CIFAR, PACS, OfficeHome, ImageNet 벤치마크 실험에서 시험 시점의 분포 변화로 생긴 잘못된 예측을 바로잡는 능력을 보였고, 기존 TTA 방법에 덧붙여 성능을 높이는 도구로 쓸 수 있다.[^p8] | 1저자 M. Jang, 마지막 저자 정혜원 |

## 교수와 전문 분야

정혜원 교수(Hye Won Chung)는 KAIST 전기및전자공학부 부교수(Associate Professor)이고, 전산학부(School of Computing)와 AI대학원(Graduate School of AI)에 겸임으로 소속돼 있다.[^home][^ee] 전기및전자공학부 교수 소개는 디비전을 Communication으로, 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding, Big Data로, 주요 연구를 데이터 과학, 정보 이론, 통계 추론, 머신 러닝, 양자 정보로 적는다.[^ee] 반도체시스템공학과 교수 명단은 연구분야를 컴퓨터, 인공지능 및 소프트웨어로 적고,[^sse] 반도체시스템공학과 연구실 목록에도 이 연구실이 올라 있다.[^sselab]

교수는 KAIST에서 학사 학위(summa cum laude)를, 미국 MIT에서 석사 학위와 2014년 박사 학위를 받았고 세 학위 모두 전기공학·컴퓨터과학(EECS) 전공이다. 2014년부터 2017년까지 University of Michigan에서 연구원(research fellow)으로 일했다.[^home] MIT 박사 학위 논문은 양자 상태에서 고전 정보를 뽑아내는 측정의 근본 한계와 적응형·유한 길이 측정을 다뤘다.[^pubs] 누리집 강의 목록은 2017년 가을학기 EE623 Information Theory부터 KAIST 강의를 적으며, EE623 Information Theory, EE210 Probability and Introductory Random Processes, EE326 Introduction to Information Theory and Coding Theory 등을 맡아 왔다.[^teaching]

누리집 소식에 따르면 교수는 2021년 12월 KAIST Technology Innovation Award를 받았고, 2023년 3월 EE623 Information Theory 강의로 학과 우수강의상(Departmental Outstanding Teaching Award)을 받았다. 강의 목록은 2017년과 2022년 가을학기 EE623 강의에 이 상을 적는다. 2025년 1월에는 2025–2026년 IEEE 정보이론학회(ITSOC) Distinguished Lecturer로 선정됐다.[^news][^teaching][^home] 학계 활동으로 누리집은 ICML 2026·NeurIPS 2026·ICLR 2027의 area chair(AC), ISIT 2025·2027의 TPC(프로그램 위원회) 위원, ISIT 2024 조직위원을 맡는다고 알린다.[^home][^news] 2026년 8월부터 2027년 7월까지는 MIT에서 연구년(sabbatical)을 보낸다고 누리집이 적는다.[^home]

교수는 2024년 ISIT에서 Lele Wang(UBC)과 함께 그래프 매칭의 근본 한계와 효율적 알고리즘을 주제로 튜토리얼을 열었고, 2026년 5월과 7월 소식은 IEEE European School of Information Theory(ESIT)와 IEEE East Asian School of Information Theory(EASIT, 대만)에서 data- and supervision-efficient learning을 주제로 3시간 튜토리얼을 맡는다고 알린다.[^news][^home] 초청 강연으로는 UCSD ITA(2023년 데이터 가치 평가, 2024년 다중 분류의 자기 증류), Institute of Data Science at National University of Singapore(2022), JCCI 2022 「Post-Shannon Communication」 패널, Princeton의 Conference on Information Sciences and Systems(CISS, 2022)가 누리집 소식에 올라 있다.[^news]

연구 지원으로는 2021년 3월부터 4년 동안 한국연구재단(NRF)의 Excellent Early-Career Research Funding을 받았다. 2024년 8월 소식은 교수가 기초연구실(BRL) 사업 「Theoretical Framework for Foundation Models」의 연구책임자로 Jaekyun Moon(KAIST), Jy-yong Sohn(연세대), Dohyun Kwon(서울시립대) 교수와 함께 파운데이션 모델(여러 과제에 두루 쓰도록 큰 데이터로 미리 학습한 모델)의 이론 틀과 알고리즘을 개발한다고 적는다. 2025년 2월에는 연구실의 데이터 효율 학습 연구가 한국연구재단 중견연구 지원(NRF Mid-Career Research Funding, Leap Research Program)에 선정됐다.[^news]

논문으로 보면 전문 분야는 두 갈래다. 하나는 그래프 매칭과 커뮤니티 탐지, 크라우드소싱 추론, 무작위 행렬 신호 검출, 행렬 완성처럼 정보 이론과 확률로 추론 문제의 근본 한계와 알고리즘을 밝히는 이론이다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 다른 하나는 데이터 가치 평가, 데이터셋 증류, 자기 증류, 테스트 시점 적응처럼 적은 데이터와 계산으로 견고하게 학습하는 딥러닝 방법이다(대표 논문 5–8).[^p5][^p6][^p7][^p8] 2018년까지의 논문에는 잡음 섞인 스무고개 문제의 질문 전략, 봉우리가 하나인 확률분포(단봉 분포)의 분산 한계, 손실이 있는 광통신 채널의 용량, 양자 상태로 정보를 보내는 통로의 부호화율 같은 정보 이론과 양자 정보 주제가 있다.[^pubs]

## 응용 분야

대표 논문이 든 쓰임은 다음과 같다. 연결망 짝 맞추기 연구는 같은 사용자들이 여러 소셜 플랫폼에서 상관된 친구 관계와 속성을 보이는 경우를 예로 든다.[^p1] 크라우드소싱 연구는 전문가가 아닌 작업자로 데이터에 정답 표시를 다는 플랫폼을 다룬다.[^p2] 데이터 가치 점수는 불규칙하거나 잘못 표시된 데이터를 찾고, 데이터 묶음을 분석하고, 학습 과정을 진단하는 데 쓰였다.[^p5] CovMatch는 그림-글 검색 정확도로 평가했다.[^p6]

## 구성원

2026년 10월 22일 연구실 누리집 Group 페이지 기준이다. Postdoc, PhD students, MS students 칸의 구성원이며, 과정과 이메일은 누리집 표기를 옮겼다.[^group] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Hyeonsu Jeong | 박사후연구원 | hsjeong1121@kaist.ac.kr | 7 |
| Nohyun Ki | 박사과정 | kinohyun@kaist.ac.kr | 5 |
| Yongmin Lee | 박사과정 | lym7505@kaist.ac.kr | 6 |
| Seunghun Cha | 박사과정 | tmdwk123456@kaist.ac.kr |  |
| Hongsin Lee | 박사과정 | hongsin04@kaist.ac.kr |  |
| Junmo Kim | 박사과정 | junmokim1@kaist.ac.kr |  |
| Junhyung Kim | 박사과정 | kjgud0831@kaist.ac.kr |  |
| Jaeeun Kim | 석사과정 | kumi1010@kaist.ac.kr |  |
| Jisoo Han | 석사과정 | jisoo.han@kaist.ac.kr |  |
| Youngsun Je | 석사과정 | jeyoungsun@kaist.ac.kr |  |
| Min Suk Suk | 석사과정 | msjk27@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Group 페이지 Alumni 칸의 20명이다(박사 8, 석사 12). 학위·연도·진로와 수상은 누리집 표기다. Hyeonsu Jeong은 박사 학위 뒤 이 연구실 박사후연구원으로, Nohyun Ki·Yongmin Lee·Seunghun Cha·Junmo Kim·Junhyung Kim은 석사 학위 뒤 이 연구실 박사과정 구성원으로 위 표에도 있다.[^group]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 랩이 적은 수상 |
|---|---|---|---|
| Hyeonsu Jeong | PhD (2026) | postdoc at KAIST |  |
| Dong Geun Shin | PhD (2026) | now at One More Security |  |
| Minguk Jang | PhD (2025) | now at Samsung Research |  |
| Joonhyuk Yang | PhD (2025) | now at Samsung Research |  |
| Hoyong Choi | PhD (2024) | now at Samsung Research |  |
| Dong Phil Shin | PhD (2024) | now at Samsung LSI |  |
| Daesumg Kim | PhD (2023) | now at SK Hynix | College of Engineering PhD Dissertation Award |
| Doyeon Kim | PhD (2023) | now at Samsung LSI |  |
| Junhyung Kim | MS (2026) | continuning PhD student |  |
| Hyumin Cho | MS (2026) | now at Samsung Research |  |
| Junmo Kim | MS (2026) | continuing PhD student |  |
| Minju Hong | MS (2026) |  |  |
| Jekyun Park | MS (2025) | PhD student at Univ. of Michigan |  |
| Yongmin Lee | MS (2024) | continuing PhD student |  |
| Seunghun Cha | MS (2024) | continuing PhD student |  |
| Nohyun Ki | MS (2023) | continuing PhD student |  |
| Jinhee Lee | MS (2022) | now at Lunit |  |
| Hae Ri Kim | MS (2021) | PhD student at CMU |  |
| Soyeon Kim | MS (2021) | now at Samsung Research |  |
| Seyoung Cho | MS (2019) | now at LINE |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 연도 구역 29편이다. 누리집이 J로 표시한 학술지·컴퓨터과학 학회 논문 24편([J7]–[J30])과 C로 표시한 동료 심사 학회 논문 5편([C13]–[C17])이다. 제목·저자·학술지·학회 이름은 누리집 표기 그대로이고, 저자 이름 뒤 *는 누리집이 밝힌 공동 기여 표시다. 2026년의 InfCLIP 한 편은 첫 화면이 2026년 9월에 채택을 알린 논문으로, 학회 발표 전이라 「NeurIPS 2026 채택」으로 표시했다.[^pubs][^home]

**2026**

- Nohyun Ki and Hye Won Chung. "InfCLIP: Unified Data Valuation for CLIP Pretraining via Influence-Inspired Scoring". *Conference on Neural Information Processing Systems (NeurIPS), 2026* (NeurIPS 2026 채택).
- Hongsin Lee and Hye Won Chung. "Towards Understanding Adversarial Distllation: Why Robust Teachers Fail". *International Conference on Machine Learning (ICML), 2026*.
- Hongsin Lee and Hye Won Chung. "Sample-wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation". *Transactions on Machine Learning Research (TMLR), 2026*.

**2025**

- Yongmin Lee and Hye Won Chung. "CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder". *Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Jaekyun Park and Hye Won Chung. "VIPAMIN: Visual Prompt Initialization via Embedding Selection and Subspace Expansion". *Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Hyeongheon Cha, Dong Min Kim, Taesik Gong, Hye Won Chung, and Sung-Ju Lee. "SNAP: Low-Latency Test-Time Adaptation with Sparse Updates". *Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Joonhyuk Yang and Hye Won Chung. "Exact Matching in Correlated Networks with Node Attributes for Improved Community Recovery". *IEEE Trans. on Information Theory, vol. 71, issue 10, pp. 7916-7941, 2025*.
- Hyeonsu Jeong and Hye Won Chung. "Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels". *International Conference on Learning Representations (ICLR), 2025*.
- Minguk Jang and Hye Won Chung. "Label Distribution Shift-Aware Prediction Refinement for Test Time Adaptation". *Transactions on Machine Learning Research (TMLR), 2025*.
- Hye Won Chung, Jiho Lee and Ji Oon Lee. "Asymptotic Normality of Log-Likelihood Ratio and Fundamental Limit of the Weak Detection for Spiked Wigner Matrices". *Bernoulli 31(3), pp. 2276-2301, 2025*.
- Joonhyuk Yang and Hye Won Chung. "Improving Community Recovery via Exact Matching in Correlated Contextual Stochastic Block Models". *IEEE International Symposium on Information Theory (ISIT), June 2025*.

**2024**

- Hoyong Choi\*, Nohyun Ki\* and Hye Won Chung. "BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges". *International Conference on Machine Learning (ICML), July 2024*.
- Yongmin Lee and Hye Won Chung. "SelMatch: Effectively Scaling Up Dataset Distillation via Selection-Based Initialization and Partial Updates by Trajectory Matching". *International Conference on Machine Learning (ICML), July 2024*.
- Dong Geun Shin and Hye Won Chung. "Representation Norm Amplification for Out-of-Distribution Detection in Long-Tail Learning". *Transactions on Machine Learning Research (TMLR), 2024*.
- Ji Hyung Jung, Hye Won Chung and Ji Oon Lee. "Detection Problems in the Spiked Random Matrix Models". *IEEE Trans. on Information Theory, vol. 70, issue 10, pp. 7193-7231, 2024*.
- Doyeon Kim, Jeonghwan Lee and Hye Won Chung. "A Worker-Task Specialization Model for Crowdsourcing: Efficient Inference and Fundamental Limits". *IEEE Trans. on Information Theory, vol. 70, issue 3, pp. 2076-2117, 2024*.
- Joonhyuk Yang and Hye Won Chung. "Exact Graph Matching in Correlated Gaussian-Attributed Erdos-Renyi Model". *IEEE International Symposium on Information Theory (ISIT), July 2024*.

**2023**

- Daesung Kim and Hye Won Chung. "Rank-1 Matrix Completion with Gradient Descent and Small Random Initialization". *Conference on Neural Information Processing Systems (NeurIPS), 2023*.
- Joonhyuk Yang\*, Dongphil Shin\* and Hye Won Chung. "Efficient Algorithms for Exact Graph Matching on Correlated Stochastic Block Models with Constant Correlation". *International Conference on Machine Learning (ICML), Jun. 2023*.
- Hyeonsu Jeong and Hye Won Chung. "Recovering Top-Two Answers and Confusion Probability in Multi-Choice Crowdsourcing". *International Conference on Machine Learning (ICML), Jun. 2023*.
- Nohyun Ki\*, Hoyong Choi\*, and Hye Won Chung. "Data Valuation without Training of a Model". *International Conference on Learning Representations (ICLR), 2023*.
- Minguk Jang, Sae-Young Chung, and Hye Won Chung. "Test-Time Adaptation via Self-Training with Nearest Neighbor Information". *International Conference on Learning Representations (ICLR), 2023*.
- Joonhyuk Yang and Hye Won Chung. "Graph Matching in Correlated Stochastic Block Models for Improved Graph Clustering". *IEEE Allerton Conference on Communication, Control, and Computing (Allerton), Monticello, IL, USA, Oct. 2023*.

**2022**

- Hye Won Chung and Ji Oon Lee. "Weak Detection in the Spiked Wigner Model". *IEEE Trans. on Information Theory, vol. 68, issue 11, pp. 7427-7453, Nov. 2022*.
- Doyeon Kim, Jeonghwan Lee and Hye Won Chung. "A Generalized Worker-Task Specialization Model for Crowdsourcing: Optimal Limits and Algorithm". *IEEE International Symposium on Information Theory (ISIT), June 2022*.

**2021**

- Jinhee Lee\*, Haeri Kim\*, Youngkyu Hong\*, and Hye Won Chung (\*:equal contribution). "Self-Diagnosing GAN: Diagnosing Underrepresented Samples in Generative Adversarial Networks". *Conference on Neural Information Processing Systems (NeurIPS), 2021*.
- Daesung Kim and Hye Won Chung. "Binary Classification with XOR Queries: Fundamental Limits and An Efficient Algorithm". *IEEE Trans. on Information Theory, vol. 67, issue 7, pp. 4588-4612, Jul. 2021*.
- Ji Hyung Jung, Hye Won Chung and Ji Oon Lee. "Detection of Signal in the Spiked Rectangular Models". *International Conference on Machine Learning (ICML), Jun. 2021*.
- Doyeon Kim and Hye Won Chung. "Crowdsourced Labelling for Worker-Task Specialization Model". *IEEE International Symposium on Information Theory (ISIT), Jul. 2021*.

## 소식

누리집 첫 화면 News 절(2026년)과 News 페이지(2025년 이전)에서 2021년 10월부터 2026년 10월 사이의 47건이다. 날짜는 누리집이 적은 연·월이고, 글은 누리집 표기 그대로다.[^home][^news]

- 2026-09 · One paper is accepted to NeurIPS 2026. Congrats Nohyun! InfCLIP: Unified Data Valuation for CLIP Pretraining via Influence-Inspired Scoring
- 2026-08 · I am on my sabbatical at MIT (host: Prof. Gregory Wornell) until July 2027.
- 2026-08 · I will be serving as an AC for ICLR 2027, and a TPC member for ISIT 2027.
- 2026-07 · I will be attending the IEEE East Asian School of Information Theory (EASIT) in Taiwan and provide a 3-hour tutorial on data- and supervision-efficient learning.
- 2026-05 · One paper is accepted to ICML 2026. Congrats Hongsin! Toward Understanding Adversarial Distillation: Why Robust Teachers Fail
- 2026-05 · I will attend the IEEE European School of Information Theory (ESIT) and provide a 3-hour tutorial on data- and supervision-efficient learning.
- 2026-04 · One paper is accepted to TMLR. Sample-Wise Adaptive Weighting for Transfer Consistency in Adversarial Distillation.
- 2026-04 · I will be serving as an area chair of NeurIPS 2026.
- 2026-01 · I will be serving as an area chair of ICML 2026.
- 2025-11 · I will be serving as an Area Chair for ICML 2026.
- 2025-09 · Three papers are accepted to NeurIPS 2025. Congrats to my co-authors! CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder VIPAMIN: Visual Prompt Initialization via Embedding Selection and Subspace Expansion SNAP: Low-Latency Test-Time Adaptation with Sparse Updates
- 2025-07 · One paper is accepted to IEEE TIT. Exact Matching in Correlated Networks with Node Attributes for Improved Community Recovery
- 2025-02 · Our lab's research on data-efficient learning has been selected for the NRF Mid-Career Research Funding (Leap Research Program), a newly established initiative supporting researchers with outstanding results to continue their work seamlessly. This achievement was highlighted as an exemplary case in the Republic of Korea Policy Briefing on the Ministry of Science and ICT.
- 2025-01 · One paper is accepted to TMLR. Label Distribution Shift-Aware Prediction Refinement for Test Time Adaptation
- 2025-01 · One paper is accepted to ICLR 2025. Rethinking Self-Distillation: Label Averaging and Enhanced Soft Label Refinement with Partial Labels
- 2025-01 · I am selected as a Distinguished Lecturer of IEEE Information Theory Society (ITSOC) for 2025-2026.
- 2025-01 · I will serve as a TPC for ISIT 2025.
- 2024-08 · PI for Basic Research Lab (BRL) on the topic of Theoretical Framework for Foundation Models Jointly with Prof. Jaekyun Moon (KAIST), Prof. Jy-yong Sohn (Yonsei), and Prof. Dohyun Kwon (Univ. of Seoul), our group will develop a theoretical framework and algorithms for foundation models. Great thanks to National Research Foundation (NRF).
- 2024-08 · A new paper is accepted to TMLR Representation Norm Amplification for Out-of-Distribution Detection in Long-Tail Learning
- 2024-07 · Jointly with Lele Wang (UBC), I delivered a tutorial at ISIT 2024 on the topic of "Graph Matching: Fundamental Limits and Efficient Algorithms." Here are the slides (Part I, Part II).
- 2024-03 · A new paper is accepted to IEEE TIT Detection Problems in the Spiked Random Matrix Models
- 2024-04 · Two papers are accepted to ICML 2024 BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges SelMatch: Effectively Scaling Up Dataset Distillation via Selection-Based Initialization and Partial Updates by Trajectory Matching
- 2024-04 · I will give a tutorial at IEEE ISIT 2024 on the topic of "Graph Matching: Fundamental Limits and Efficient Algorithms"
- 2024-04 · A new paper is accepted to IEEE ISIT 2024 Exact Graph Matching in Correlated Gaussian-Attributed Erods-Renyi Model
- 2024-03 · A new paper is published in IEEE TIT A Worker-Task Specialization Model for Crowdsourcing: Efficient Inference and Fundamental Limits
- 2024-02 · Delivered an invited talk at UCSD ITA on the topic of understanding self-distillation in multi-class classification
- 2024-01 · I will be serving as an organizing committee of ISIT 2024
- 2023-09 · A new paper is accepted to NeurIPS 2023 Rank-1 Matrix Completion with Gradient Descent and Small Random Initialization
- 2023-09 · A paper is accepted to IEEE Trans. on Information Theory A Worker-Task Specialization Model for Crowdsourcing: Efficient Inference and Fundamental Limits
- 2023-08 · A paper is accepted to Allerton 2023 Graph Matching in Correlated Stochastic Block Models for Improved Graph Clustering
- 2023-04 · Two papers are accepted to ICML2023 Recovering Top-Two Answers and Confusion Probability in Multi-Choice Crowdsourcing Efficient Algorithms for Exact Graph Matching on Correlated Stochastic Block Models with Constant Correlation
- 2023-03 · Received Departmental Outstanding Teaching Award for EE623 Information Theory.
- 2023-02 · Delivered an invited talk at UCSD ITA on the topic of "Data Valuation without Training of a Model".
- 2023-02 · Two first PhD graduates from our lab, Daesung Kim and Doyeon Kim. Congrats!
- 2023-02 · Daesung has been awarded College of Engineering PhD Dissertation award. Congrats!
- 2023-01 · Two papers are accepted to ICLR2023 Data Valuation without Training of a Model Test-Time Adaptation via Self-Training with Nearest Neighbor Information
- 2023-01 · Two new papers are available at arXiv. Data Valuation without Training of a Model Recovering Top-Two Answers and Confusion Probability in Multi-Choice Crowdsourcing
- 2022-12 · A new paper is available at arXiv. Rank-1 Matrix Completion with Gradient Descent and Small Random Initialization
- 2022-11 · A new paper is published at IEEE Transactions on Information Theory. Weak Detection in the Spiked Wigner Model
- 2022-10 · Delivered an invited talk at Institute of Data Science at National University of Singapore. Data Valuation: Understanding Value of Data in Training Neural Networks
- 2022-04 · Delivered an invited talk at "Post-Shannon Communication" panel session at JCCI 2022.
- 2022-04 · A paper accepted in ISIT 2022. A Generalized Worker-Task Specialization Model for Crowdsourcing: Optimal Limits and Algorithm
- 2022-03 · An invited talk at Conference on Information Sciences and Systems (CISS) at Princeton
- 2022-03 · Daesung has been awarded KAIST EE Best Research Achievement Award. Congrats Daesung!
- 2022-03 · Two new papers are available at arXiv A Worker-Task Specialization Model for Crowdsourcing: Efficient Inference and Fundamental Limits Asymptotic Normality of Log-Likelihood Ratio and Fundamental Limit of the Weak Detection for Spiked Wigner Matrices
- 2022-03 · Welcome new members, Youngmin Lee and Seunghun Cha
- 2021-12 · I received KAIST Technology Innovation Award.

## 연락과 위치

- 교수연구실: KAIST IT융합빌딩(N1) 206호, 전화 042-350-7441[^home][^ee]
- 연구실: KAIST N1 213호, 전화 042-350-7541[^group]
- 교수 이메일: hwchung@kaist.ac.kr[^home][^ee]
- 누리집 Group 페이지는 확률·통계·해석 같은 수학 배경이나 파이썬 같은 프로그래밍 능력이 있으면 연구를 시작하기 쉽다며 함께할 학생을 찾는다고 안내한다.[^group]
[^p1]: J. Yang, H. W. Chung, IEEE Transactions on Information Theory 71, 7916-7941 (2025). <https://doi.org/10.1109/tit.2025.3592704> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: D. Kim, J. Lee, H. W. Chung, IEEE Transactions on Information Theory 70, 2076-2117 (2024). <https://doi.org/10.1109/tit.2023.3315720> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. W. Chung, J. Lee, J. O. Lee, Bernoulli 31, 2276-2301 (2025). <https://doi.org/10.3150/24-bej1805> 초록 기준.
[^p4]: D. Kim, H. W. Chung, Advances in Neural Information Processing Systems 36, 10530-10566 (2023). <https://doi.org/10.52202/075280-0463> 초록 기준(arXiv 판).
[^p5]: N. Ki, H. Choi, H. W. Chung, International Conference on Learning Representations (ICLR) (2023). <https://arxiv.org/abs/2301.00930> 초록 기준(arXiv 판).
[^p6]: Y. Lee, H. W. Chung, Advances in Neural Information Processing Systems 38, 112560-112588 (2025). <https://doi.org/10.52202/085713-3398> 초록 기준(arXiv 판).
[^p7]: H. Jeong, H. W. Chung, International Conference on Learning Representations (ICLR) (2025). <https://arxiv.org/abs/2402.10482> 초록 기준(arXiv 판).
[^p8]: M. Jang, H. W. Chung, Transactions on Machine Learning Research (TMLR) (2025). <https://arxiv.org/abs/2411.15204> 초록 기준(arXiv 판).
[^home]: 연구실 누리집 첫 화면 <https://iids.kaist.ac.kr/> (교수 직위·소속, 연락처, Short bio, Selected recent papers, 2026년 News, 2026-10-22 열람)
[^research]: 연구실 누리집 Research 페이지 <https://iids.kaist.ac.kr/research> (Overview, Selected recent papers, 2026-10-22 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://iids.kaist.ac.kr/publications> (논문 목록, Theses, 2026-10-22 열람)
[^group]: 연구실 누리집 Group 페이지 <https://iids.kaist.ac.kr/people> (학생 모집 안내, 위치·전화, Postdoc·PhD students·MS students, Alumni, 2026-10-22 열람)
[^news]: 연구실 누리집 News 페이지 <https://iids.kaist.ac.kr/news> (2025년 이전 소식, 2026-10-22 열람)
[^teaching]: 연구실 누리집 Teaching 페이지 <https://iids.kaist.ac.kr/teaching> (2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(정혜원) <https://ee.kaist.ac.kr/professor/15247/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 교수 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)

# ProbAI Lab (Probabilistic Artificial Intelligence Laboratory)

**KAIST 수리과학과 · 황강욱 교수**

- 분야: 응용확률, 확률적·통계적 기계학습, 협력 학습, 생성 모형[^faculty][^research]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 연합학습·분산 학습[^federated], 생성 인공지능[^generative]
- 홈페이지: <https://sites.google.com/view/probai-lab/home>
- 근거와 출처: [ProbAI Lab 근거 페이지](probai-sources.md)

> 확률과 통계로 학습 결과의 불확실성을 다루고, 여러 기관이 자료를 모으지 않고 함께 배우는 방법과 새로운 자료를 만드는 모형을 연구한다.

## 무엇을 연구하나

ProbAI Lab은 확률과 통계를 바탕으로 기계학습(예시 자료에서 예측·판단 규칙을 배워 새 자료에 적용하는 계산 방법)을 연구한다. 학습 결과가 얼마나 확실한지와 처음 보는 자료에도 잘 맞는지를 수학적으로 분석하고, 실제 문제를 푸는 알고리즘(문제를 처리하는 계산 절차)을 개발한다.[^home][^research]

첫째는 **불확실성을 함께 나타내는 예측**이다. 확률적 기계학습은 예측값뿐 아니라 그 값이 달라질 가능성도 모형에 담는다. 통계적 기계학습에서는 일반화(학습에 쓰지 않은 자료에서도 예측 규칙이 통하는 성질)를 분석한다. 대표 논문은 전파가 이동하면서 약해지는 정도를 예측하는 모형과, 공기의 성분·안개·비로 전파가 약해지는 정도를 예측하는 모형을 다룬다. 두 연구 모두 예측의 불확실성을 함께 다룬다.[^research][^p4][^p6]

둘째는 **자료를 각자 보관하는 협력 학습**이다. 연합학습은 여러 참여자가 원자료를 한곳에 모으지 않은 채 함께 예측 모형을 배우는 방식이다. 연구실은 서로 다른 이용자의 자료를 가진 경우와 같은 이용자의 서로 다른 정보를 나눠 가진 경우를 모두 다룬다. 지식 증류(다른 모형이 내놓은 예측을 학습 목표로 삼아 지식을 전달하는 방법)를 이용하는 연합학습도 연구한다.[^federated] 대표 논문에서는 기관 사이에 대응하는 자료나 정답 표시가 빠진 상황을 다루고, 공개 자료로 지식을 나누는 학습 방법의 이론과 실제 알고리즘을 분석한다.[^p1][^p3][^p5]

셋째는 **새 자료를 만드는 생성 모형**이다. 생성 모형은 관측 자료가 따르는 확률적 규칙을 배워 같은 유형의 새 자료를 만드는 모형이다. 연구실은 학습 자료와 닮은 새 이미지를 만드는 생성 모형과 그 일반화 성능을 연구하며, 생성 모형을 이용해 빠진 자료가 있는 분산 학습도 다룬다.[^generative] 대표 논문에서는 주어진 조건에 맞는 영상을 만드는 과정에서 조건별 예시가 부족한 문제를 이웃한 조건의 자료를 함께 이용하는 방법으로 다뤘다.[^p2]

또한 메타학습(이전 과제의 경험으로 새 과제의 학습 방식을 개선하는 방법)과 전이학습(이전 영역·과제에서 배운 지식을 새 영역·과제에 옮기는 방법)의 알고리즘을 개발한다. 뉴럴 프로세스는 관측 자료를 신경망(연결된 계산 단위들이 자료에서 예측 규칙을 배우는 모형)으로 처리해 여러 입력의 출력들을 확률적으로 함께 나타내는 학습 방법이다. 연구실은 이를 적은 자료로 연속적인 값을 예측하는 데 이용하며, 주어진 자료가 어떤 과제를 나타내는지 표현하는 방법과 예측할 입력들 사이의 관계를 함께 고려하는 방법을 다룬다.[^research]

## 주요 연구 주제

### 1. 확률적·통계적 기계학습

관측 자료와 예측에 남는 불확실성을 모형에 반영하고, 새로운 자료에 대한 학습 방법의 성능을 이론적으로 분석한다.[^research] 무선 통신에서는 위치에 따른 전파 손실과 대기 감쇠를 예측한다. 대표 논문 4와 6에 해당한다.[^p4][^p6]

### 2. 협력 학습과 연합학습

자료를 여러 참여자가 보관하는 상황에서 지식을 합치는 방법을 연구한다. 자료 대응의 누락과 정답 표시의 부족을 다루는 학습, 지식 증류를 통한 협력 학습이 대표 논문 1·3·5의 주제다.[^research][^p1][^p3][^p5]

### 3. 생성 모형

새로운 이미지 등 자료를 만드는 모형과 그 일반화 성능을 연구하며, 자료 일부가 빠진 분산 학습에도 생성 모형을 이용한다. 대표 논문 2는 조건별 예시가 부족한 상황의 영상 생성을 다룬다.[^research][^p2]

### 4. 메타학습·전이학습과 뉴럴 프로세스

이전 과제의 경험을 이용한 학습 개선, 이전 영역에서 배운 지식의 이전, 적은 관측 자료에 기초한 확률적 예측을 연구한다. 이론적 이해와 실험 검증을 함께 이용해 알고리즘을 개발한다.[^research]

## 대표 논문

KAIST 재직 시기의 논문 가운데 협력 학습, 생성 모형, 확률 모형의 통신 응용을 고르게 살펴볼 수 있는 6편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. ICLR은 International Conference on Learning Representations, NeurIPS는 Conference on Neural Information Processing Systems, ICML은 International Conference on Machine Learning의 약칭이다. 학회 채택과 연결된 두 논문은 arXiv 사전 공개본의 초록을 설명한다.[^p1][^p3]

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Deep Latent Variable Model based Vertical Federated Learning with Flexible Alignment and Labeling Scenarios](https://doi.org/10.48550/arxiv.2505.11035) · ICLR 2026 채택, arXiv 사전 공개본 | 같은 이용자의 서로 다른 정보를 나눠 가진 기관들이 함께 학습할 때, 기관들의 자료가 서로 맞물리지 않는 빈틈을 빠진 자료의 문제로 해석했다. 자료의 대응과 정답 표시가 여러 방식으로 불완전한 상황에서 학습과 예측을 함께 수행하는 통합 방법을 제안했다.[^p1] | 1저자 Kihun Hong, 마지막 저자 Ganguk Hwang |
| 2 | 2026 | [VE-cGAN: Improved Generalization Analysis of Conditional Generative Adversarial Networks Using Vicinal Estimation](https://doi.org/10.1007/s10994-025-06953-4) · Machine Learning | 조건부 생성적 적대 신경망은 생성 모형과 진짜·가짜를 가리는 모형을 함께 학습시켜 주어진 조건에 맞는 자료를 만든다. 이 연구는 가까운 조건의 예시를 함께 이용해 조건별 자료 부족을 줄이고, 영상을 나타내는 값의 수에 의존하지 않는 일반화 오차의 상한을 제시했다. 실험에서는 비교 방법보다 생성 영상의 시각적 품질과 조건에 맞는 정도가 개선됐다.[^p2] | 1저자 Ki Joung Jang, 마지막 저자 Ganguk Hwang |
| 3 | 2024 | [A Kernel Perspective on Distillation-based Collaborative Learning](https://doi.org/10.48550/arxiv.2410.17592) · NeurIPS 2024 채택, arXiv 사전 공개본 | 통계적 성질이 다른 많은 참여자가 원자료나 각자의 모형을 직접 공유하지 않는 협력 학습을 분석했다. 공개 자료와 지식 증류를 이용하는 알고리즘의 성능을 수학적으로 분석하고, 그 결과에 기초해 신경망을 사용하는 실제 협력 학습 알고리즘을 제안했다. 여러 연속값 예측 과제로 이론과 실제 적용 가능성을 살폈다.[^p3] | 1저자 Sejun Park, 마지막 저자 Ganguk Hwang |
| 4 | 2024 | [Atmospheric Attenuation Model Using Gaussian Process in Sub-THz Terrestrial Wireless Communications](https://doi.org/10.1109/lawp.2023.3330189) · IEEE Antennas and Wireless Propagation Letters | 높은 주파수(전파가 1초에 진동하는 횟수)의 지상 무선 통신에서 기체·안개·비 때문에 생기는 전파 감쇠를 예측하는 모형을 제안했다. 관측값 사이의 관계와 예측의 불확실성을 함께 다루는 확률적 학습 방법을 대규모 자료에 맞게 사용해 장기간 측정 자료로 학습했다. 실험에서 기존 모형보다 좋은 예측 성능을 보였고, 감쇠가 들어갈 범위를 함께 제시했다.[^p4] | 1저자 Ki Joung Jang, 마지막 저자 Ganguk Hwang |
| 5 | 2023 | [Towards Understanding Ensemble Distillation in Federated Learning](https://proceedings.mlr.press/v202/park23e.html) · ICML 2023 | 여러 모형의 예측을 합쳐 다른 모형에 전달하는 앙상블 증류를 연합학습에서 분석했다. 커널 릿지 회귀(자료 사이 유사도를 이용하고 계수의 제곱합에 벌점을 주어 연속값을 예측하는 방법)에 맞는 알고리즘을 제안했다. 정답 표시가 없는 공개 자료가 충분히 많으면 각 참여자 모형의 일반화 오차가 모든 자료를 모아 학습한 모형과 같은 속도로 줄어드는 것을 보였다. 실험으로 이론 결과를 확인했다.[^p5] | 1저자 Sejun Park, 마지막 저자 Ganguk Hwang |
| 6 | 2022 | [Path Loss Model Based on Machine Learning Using Multi-Dimensional Gaussian Process Regression](https://doi.org/10.1109/access.2022.3217912) · IEEE Access | 전파가 이동하는 거리에서 오는 전체적인 손실 경향과 주변 환경 때문에 위치마다 달라지는 손실을 별도의 확률 모형으로 나타내고 함께 학습했다. 이 방법은 가까운 위치의 전파 특성이 서로 연관되는 성질과 예측의 불확실성을 함께 반영한다. 서로 다른 실내 환경의 측정 자료로 예측 성능을 평가했다.[^p6] | 1저자 Ki Joung Jang, 마지막 저자 Ganguk Hwang |

## 교수와 전문 분야

황강욱 교수(Ganguk Hwang)는 KAIST 수리과학과 교수이며, 학과는 전문 분야를 응용확률(확률론을 실제 현상의 모형화와 분석에 쓰는 분야)과 확률적 인공지능으로 적는다. KAIST에서 수학 학사(1991), 석사(1993), 응용확률 분야 박사(1997)를 받았다.[^faculty][^professor]

1997년 2월부터 2000년 3월까지 한국전자통신연구원에서 통신 시스템 개발에 참여했고, 2000년 3월부터 2002년 2월까지 University of Missouri–Kansas City의 컴퓨터과학·전기공학 분야 방문학자로 있었다. 2002년 3월부터 KAIST 수리과학과와 통신공학 프로그램에서 일했으며, 2010년 8월부터 2011년 7월까지 University of Washington 전기공학과에서 연구년을 보냈다.[^professor]

현재 연구 소개의 중심은 확률적·통계적 기계학습, 협력 학습, 뉴럴 프로세스와 생성 모형이다. 대표 논문은 협력 학습의 수학적 성능 분석과 알고리즘 개발, 생성 모형의 일반화 분석, 확률 모형을 이용한 무선 전파 예측으로 이어진다.[^research][^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

원자료를 기관 밖으로 모으기 어려운 공동 학습과, 조건에 맞는 이미지 생성이 주요 응용이다. 통신 분야에서는 전파가 이동하는 환경에 따른 손실과 대기 감쇠를 예측한다.[^research][^p1][^p2][^p4][^p6] 연구실 과제 소개는 전파 환경 이미지를 이용한 전파 손실 예측과 자율운항선박 항법 알고리즘 검증을 위한 확률적 연속값 예측을 응용 대상으로 든다.[^projects]

## 구성원

2026년 11월 7일 누리집 Members에 현재 학생으로 게시된 5명이다. 과정은 게시 구분을 옮겼다. 대표 논문 저자와 같은 이름의 저자를 같은 사람으로 보아 참여 번호를 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kihun Hong | 박사과정 | 1, 3, 5 |
| Haeeun Song | 박사과정 |  |
| Sungjong Lee | 박사과정 |  |
| Jaewon Kim | 박사과정 |  |
| Hyunbin Lim | 석사과정 |  |

## 졸업생과 이전 구성원

누리집의 Ph.D. Alumni 19명과 M.S. Alumni 16명, 총 35명이다. 학위와 진로는 게시 구분과 문구를 옮겼다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Bongjoo Kim | 박사 | Samsung Electronics |
| Yunju Park | 박사 | Korea Science Academy of KAIST |
| Yoora Kim | 박사 | University of Ulsan |
| Chanyong Lee | 박사 | Agency for Defense Development |
| Hongil Cho | 박사 | Korea Institute for Defense Analysis |
| Jaeman Park | 박사 | Samsung Electronics |
| Hyeonje Cho | 박사 | Samsung Electronics |
| Seunghee Lee | 박사 | Samsung Electronics |
| Yunbae Kim | 박사 | Electronics and Telecommunications Research Institute (ETRI) |
| Jaedeok Kim | 박사 | Samsung Electronics |
| Byeongchan Lee | 박사 | Samsung Electronics |
| Myungwoo Lee | 박사 | 주무르는 수 요리방 |
| Jonghun Yoon | 박사 | Samsung Electronics |
| Youngrock Oh | 박사 | Samsung SDS |
| Gyohun Jeong | 박사 | Samsung Electronics |
| Jeongseop Kim | 박사 | Samsung Research |
| Younghwan Jeon | 박사 | Samsung Advanced Institute of Technology |
| Kijoung Jang | 박사 | Samsung SDI |
| Sejun Park | 박사 | Samsung Research |
| Unsil Kim | 석사 | Zeroin |
| Hyesung Baek | 석사 | LG Electronics |
| Eunjin Kang | 석사 | Korea Exchange Bank |
| Ina Ko | 석사 | Ph.D. Candidate in University of Maryland |
| Soyoung Park | 석사 | Korean Air |
| Pani Fernando | 석사 |  |
| Subasha Wickramarachchi | 석사 |  |
| Yongsun Kim | 석사 |  |
| Cholong Kim | 석사 |  |
| Sangdon Park | 석사 | Ph.D. Student, Electrical Engineering Department, KAIST |
| Ahyoung Wi | 석사 |  |
| Yewon Jo | 석사 | 기술보증기금 |
| Sohee Bae | 석사 | Ph.D. Student, Electrical Engineering Department, KAIST |
| Soi Lee | 석사 |  |
| Jinhyun Ahn | 석사 | Ph.D. Student, Electrical Engineering Department, KAIST |
| Jiho Lee | 석사 | Ph.D. Student, Department of Mathematical Sciences, KAIST |

## 최근 논문 목록 (2021–2026)

누리집 International Journal Publications 구획의 최근 논문 9편이다. 이 구획은 주요 인공지능 학회 논문도 포함한다. 제목·저자·발표처는 누리집 표기이고 DOI를 덧붙였다. 2026년 전파 환경 이미지 논문은 게재 승인 상태다. ICLR 2026과 NeurIPS 2024 항목의 학회 채택은 arXiv 사전 공개본에도 적혀 있다.[^publications][^p1][^p3]

**2026**

- Sungjong Lee, Jonghun Yoon, Jaeho Jung, Sung Jun Lee, Bongsu Kim, and Ganguk Hwang. "Propagation-Aware Attention for Image-Based Path Loss Prediction". *IEEE Transactions on Antennas and Propagation, accepted for publication, September 2026 (게재 승인)*.
- Kihun Hong, Sejun Park and Ganguk Hwang. "Deep Latent Variable Model based Vertical Federated Learning with Flexible Alignment and Labeling Scenarios". *Proceedings of the 14th International Conference on Learning Representations (ICLR 2026), April 2026 (채택; arXiv 사전 공개본) <https://doi.org/10.48550/arxiv.2505.11035>*.
- Ki Joung Jang and Ganguk Hwang. "VE-cGAN: Improved Generalization Analysis of conditional Generative Adversarial Networks using Vicinal Estimation". *Machine Learning, Vol. 115, Article14, 2026 <https://doi.org/10.1007/s10994-025-06953-4>*.

**2024**

- Sejun Park, Kihun Hong, and Ganguk Hwang. "A Kernel Perspective on Distillation-based Collaborative Learning". *Proceedings of the 38th Annual Conference on Neural Information Processing Systems (NeurIPS 2024), December 2024 (채택; arXiv 사전 공개본) <https://doi.org/10.48550/arxiv.2410.17592>*.
- Ki Joung Jang, Jinhyung Oh, Youngkeun Yoon, Jongho Kim, and Ganguk Hwang. "Atmospheric Attenuation Model Using Gaussian Process in sub-THz Terrestrial Wireless Communications". *IEEE Antennas and Wireless Propagation Letters, Vol. 23, No. 2, pp. 568-572, February 2024 <https://doi.org/10.1109/lawp.2023.3330189>*.

**2023**

- Sejun Park, Kihun Hong, and Ganguk Hwang. "Towards Understanding Ensemble Distillation in Federated Learning". *Proceedings of the 40th International Conference on Machine Learning (ICML 2023), July 2023*.
- Younghwan Jeon and Ganguk Hwang. "Feature Selection with Scalable Variational Gaussian Process via Sensitivity Analysis based on L2 Divergence". *Neurocomputing, Vol. 518, pp. 577-592, January 2023 <https://doi.org/10.1016/j.neucom.2022.11.013>*.

**2022**

- Kijoung Jang, Sejun Park, Junseok Kim, Youngkeun Yoon, Chungsup Kim, Youngjun Chong, and Ganguk Hwang. "Path Loss Model Based on Machine Learning using Multi-Dimensional Gaussian Process Regression". *IEEE Access, Vol. 10, pp. 115061-115073, October 2022 <https://doi.org/10.1109/access.2022.3217912>*.
- Younghwan Jeon and Ganguk Hwang. "Bayesian Mixture of Gaussian Processes for Data Association Problem". *Pattern Recognition, Vol. 127, Article 108592, July 2022 <https://doi.org/10.1016/j.patcog.2022.108592>*.

## 연락과 위치

- 교수 연구실: KAIST 산업경영학동 3212호. 누리집 표기는 E2-1 3212다.[^faculty][^professor]
- 학생 공간: E2-1 3217, E2-1 2212. Jaewon Kim의 공간은 E2-1로 적혀 있다.[^members]
- 주소: E2-1 3212, KAIST, 373-1 Guseong-dong, Yuseong-gu, Daejeon, 305-701, South Korea[^professor]
- 전화: 042-350-2714[^professor]
- 팩스: 042-350-5710[^professor]
[^faculty]: KAIST 수리과학과 교수 목록, 황강욱 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> 관측 2026-11-07.
[^home]: ProbAI Lab 첫 화면. <https://sites.google.com/view/probai-lab/home> 관측 2026-11-07.
[^professor]: ProbAI Lab Professor, Ganguk Hwang의 학력·경력·연락. <https://sites.google.com/view/probai-lab/people> 관측 2026-11-07.
[^members]: ProbAI Lab Members, 현재 학생·박사 및 석사 졸업생. <https://sites.google.com/view/probai-lab/people/members> 관측 2026-11-07.
[^research]: ProbAI Lab 연구 주제 설명. <https://sites.google.com/view/probai-lab/research> 관측 2026-11-07.
[^federated]: ProbAI Lab 연구 소개의 Collaborative Learning: 자료를 분산 보관하는 공동 학습과 수평·수직·지식 증류 기반 연합학습. <https://sites.google.com/view/probai-lab/research> 관측 2026-11-07.
[^generative]: ProbAI Lab 연구 소개의 Generative Models: 새 이미지 생성과 생성 모형의 일반화 분석. <https://sites.google.com/view/probai-lab/research> 관측 2026-11-07.
[^projects]: ProbAI Lab Projects, 응용 대상 소개. <https://sites.google.com/view/probai-lab/research/projects> 관측 2026-11-07.
[^publications]: ProbAI Lab Publications, 전체 논문 목록. <https://sites.google.com/view/probai-lab/publications> 관측 2026-11-07.
[^p1]: K. Hong, S. Park, G. Hwang, arXiv:2505.11035 (ICLR 2026 채택) (온라인 2025-05-16). <https://doi.org/10.48550/arxiv.2505.11035> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2505.11035> 관측 2026-11-07.
[^p2]: K. J. Jang, G. Hwang, Machine Learning 115, 14 (온라인 2025-12-29). <https://doi.org/10.1007/s10994-025-06953-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070746145> 관측 2026-11-07.
[^p3]: S. Park, K. Hong, G. Hwang, arXiv:2410.17592 (NeurIPS 2024 채택) (온라인 2024-10-23). <https://doi.org/10.48550/arxiv.2410.17592> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.17592> 관측 2026-11-07.
[^p4]: K. J. Jang 외, G. Hwang, IEEE Antennas and Wireless Propagation Letters 23, 568-572 (온라인 2023-11-06). <https://doi.org/10.1109/lawp.2023.3330189> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070746145> 관측 2026-11-07.
[^p5]: S. Park, K. Hong, G. Hwang, Proceedings of the 40th International Conference on Machine Learning 202, 27132-27187 (2023). <https://proceedings.mlr.press/v202/park23e.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/park23e.html> 관측 2026-11-07.
[^p6]: K. J. Jang 외, G. Hwang, IEEE Access 10, 115061-115073 (2022). <https://doi.org/10.1109/access.2022.3217912> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5070746145> 관측 2026-11-07.

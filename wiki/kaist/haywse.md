# 하우석 교수 연구실

**KAIST 수리과학과 · 하우석 조교수**

- 영문 이름: Wooseok Ha
- 분야: 고차원 통계학, 기계학습, 희소·저랭크 최적화, 국소 그래프 군집화, 해석 가능한 기계학습, 분포 변화 아래의 통계적 학습[^home][^dept]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^home][^p4]
- 홈페이지: <https://haywse.github.io/>
- 근거와 출처: [하우석 교수 연구실 근거 페이지](haywse-sources.md)

> 자료에서 예측 규칙을 배우는 방법을 수학적으로 분석하고, 학습할 때와 사용할 때 자료의 성질이 달라져도 예측을 유지하는 방법을 연구한다.[^home]

## 무엇을 연구하나

하우석 교수 연구실은 고차원 통계학(관측마다 기록하는 변수의 수가 관측 수에 비해 많은 자료에서 알 수 없는 양을 구하고 예측을 다루는 통계학)과 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 계산 방법)을 연구한다. 교수는 현재 연구의 중심으로 희소·저랭크 최적화, 국소 그래프 군집화, 해석 가능한 기계학습, 자료 분포 변화 아래의 통계적 학습을 든다.[^home]

희소성은 여러 값 가운데 일부만 영이 아닌 성질이고, 저랭크는 행렬(수를 행과 열로 배열한 표)을 이루는 독립적인 행이나 열의 수가 적은 성질이다. 연구실은 이런 구조를 가진 문제의 최적화(정해진 조건 안에서 목표 값을 최소화하거나 최대화하는 변수 값을 찾는 일)를 연구한다.[^home]

또 다른 중심은 분포 변화다. 분포는 어떤 값이나 값의 범위가 나타날 확률을 나타내는 규칙이며, 분포 변화는 학습에 쓴 자료와 실제 예측할 자료의 확률적 성질이 달라지는 상황이다. 연구실은 이때의 학습 방법을 연구하며, 도메인 적응(학습 환경과 목표 환경의 자료 분포 차이를 고려해 목표 환경의 예측을 배우는 방법)과 학습 환경 밖에서의 일반화(학습하지 않은 자료에서도 예측 규칙이 성립하는 성질)를 현재 관심으로 밝힌다.[^home] 최근 논문에서는 정답이 없는 목표 자료를 활용하는 학습과 소량의 정답 자료까지 활용하는 학습을 각각 다룬다.[^p1][^p2]

연구실은 모델이 어떤 근거로 예측했는지 사람이 이해하도록 하는 해석 가능한 기계학습도 연구한다. 그래프(개체와 개체 사이의 관계를 점과 선으로 나타낸 구조)에서 일부 점 주변의 묶음을 찾는 국소 그래프 군집화가 또 다른 연구 갈래이며, 현재 관심에는 그래프 신경망(그래프의 관계 구조를 따라 정보를 주고받으며 학습하는 신경망)도 포함된다. 신경망은 연결된 계산 단위들의 결합 강도를 자료로 조절하는 계산 모형이다.[^home]

## 주요 연구 주제

### 1. 자료 분포가 바뀌는 환경의 예측

정답이 붙은 학습 자료와 정답이 없는 목표 자료를 함께 쓰는 비지도 도메인 적응을 다룬다. 대표 논문 1은 목표 자료가 적거나 학습 자료의 우연한 상관관계에 예측이 의존하는 상황을 다루기 위해, 입력 자료와 정답의 조건부 분포 양쪽의 불확실성을 고려하는 학습 틀을 제안한다. 조건부 분포는 어떤 값이나 조건이 주어졌을 때 다른 값이 나타날 확률의 관계다.[^p1]

대표 논문 3은 정답이 주어졌을 때 학습 환경과 목표 환경에서 분포가 유지되는 예측 성분을 다룬다. 이 성분을 이용하는 알고리즘(계산을 수행하는 정해진 절차)을 제안하고, 다른 도메인 적응 방법의 오차가 커지는 상황을 찾아내거나 실패 상황을 보완하는 역할을 분석한다.[^p3]

### 2. 소량의 목표 정답 자료를 쓰는 학습

대표 논문 2는 정답이 일부 있는 목표 자료를 쓰는 반지도 도메인 적응을 연구한다. 구조적 인과 모형(변수들이 서로 어떤 원인 관계로 생성되는지를 식으로 나타낸 모형) 아래에서 자료 분포의 변화를 분석하고, 학습 환경과 목표 환경이 공유하는 구조와 목표 환경에서만 고칠 부분을 구분한다. 여러 시작점에서 미세 조정(이미 학습한 모형을 새 자료로 추가 학습하는 일)한 뒤 목표 자료로 후보를 고르는 방법도 제안한다.[^p2]

### 3. 학습 계산과 특징 선택의 수학적 분석

대표 논문 4는 한 번의 갱신에 쓰는 자료 묶음의 크기인 배치 크기에 따라 학습 결과가 어떻게 달라지는지 분석한다. 대상은 입력을 압축한 뒤 다시 복원하도록 학습하는 오토인코더이며, 계산 단위가 하나이고 입력 자료가 서로 직교하는 경우를 다룬다. 직교는 벡터(크기와 방향 또는 여러 성분의 값을 나타내는 수학적 대상) 사이의 내적이 영인 관계이며, 내적은 대응하는 성분들의 곱을 더해 얻는 값이다.[^p4]

### 4. 예측의 근거를 이해하는 방법

모델이 어떤 근거로 결과를 내는지를 밝히는 해석 가능한 기계학습은 누리집이 직접 내세우는 주요 연구 갈래다. 누리집은 희소·저랭크 최적화와 함께 이 갈래를 현재 연구의 중심으로 든다.[^home]

## 대표 논문

하우석 교수가 2024년 4월 KAIST에 부임한 뒤 출판되었거나 공개된 논문 가운데, 분포 변화 대응과 학습 최적화를 다루는 네 편을 골랐다. 두 편은 2025년 학술지판이며, 두 편은 사전 공개본이다. ICLR 2026 논문은 채택 표기를 함께 적었다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.[^appointment]

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Distributionally Robust Classification for Multi-source Unsupervised Domain Adaptation](https://doi.org/10.48550/arXiv.2601.21315) · arXiv 사전 공개본, ICLR 2026(채택) | 정답이 있는 학습 자료와 정답이 없는 목표 자료를 함께 쓰되, 목표 자료가 부족하거나 학습 자료의 우연한 상관관계가 강할 때도 예측하도록 하는 방법이다. 입력 자료의 분포와 입력에 따른 정답 분포 양쪽의 불확실성을 고려하는 새 학습 틀과 계산 방법을 제안했다. 여러 학습 환경에서 얻은 자료뿐 아니라 단일 학습 환경에도 적용할 수 있도록 했다.[^p1] | 1저자 Seonghwi Kim, 공저자 Wooseok Ha, 마지막 저자 Minwoo Chae |
| 2 | 2025 | [When few labeled target data suffice: a theory of semi-supervised domain adaptation via fine-tuning from multiple adaptive starts](https://doi.org/10.48550/arXiv.2507.14661) · arXiv 사전 공개본, 심사 중 | 목표 환경의 정답 자료가 적을 때 다른 학습 환경의 자료와 정답 없는 목표 자료를 활용하는 방법이다. 자료가 생성되는 원인 관계를 모형으로 놓고, 환경 사이에 공유되는 구조와 목표 환경에서 고칠 부분을 나눠 분석한다. 여러 시작점에서 추가 학습한 모형 가운데 소량의 목표 검증 자료로 하나를 고르는 방법을 제안하고 모의 자료와 실제 자료로 효과를 확인했다.[^p2] | 1저자 Wooseok Ha, 마지막 저자 Yuansi Chen |
| 3 | 2025 | [Prominent Roles of Conditionally Invariant Components in Domain Adaptation: Theory and Algorithms](https://www.jmlr.org/papers/v26/23-1234.html) · Journal of Machine Learning Research 26(110), 1–92 | 학습 환경과 목표 환경에서 조건부로 분포가 유지되면서 예측에 도움이 되는 성분을 분석한다. 이 성분을 활용하는 새 알고리즘을 제안하고, 다른 적응 방법의 학습 오차와 목표 오차가 크게 벌어지는 상황을 알아내는 데 활용했다. 기존 방법이 정답을 뒤집는 특징 때문에 실패하는 상황을 보완하는 역할도 보였다.[^p3] | 1저자 Keru Wu·Yuansi Chen·Wooseok Ha(공동 기여), 마지막 저자 Bin Yu[^contribution] |
| 4 | 2025 | [The Effect of SGD Batch Size on Autoencoder Learning: Sparsity, Sharpness, and Feature Learning](https://www.jmlr.org/papers/v26/23-1022.html) · Journal of Machine Learning Research 26(49), 1–61 | 확률적 경사 하강법(SGD, Stochastic Gradient Descent, 무작위로 고른 자료로 목표 값이 줄어드는 방향을 추정하며 모형을 갱신하는 방법)으로 단일 계산 단위의 오토인코더를 학습할 때 배치 크기의 효과를 분석했다. 선형 함수(입력의 합과 배수 관계를 출력에도 보존하는 함수)나 ReLU(Rectified Linear Unit, 음수 입력을 영으로 바꾸고 그 밖의 입력은 그대로 내보내는 함수)를 쓰고 입력 자료가 직교하는 조건에서, 전체 자료를 한 번에 쓸 때와 일부만 쓸 때 서로 다른 특징 선택이 나타남을 보였다.[^p4] | 1저자 Nikhil Ghosh, 공저자 Wooseok Ha, 마지막 저자 Bin Yu |

## 교수와 전문 분야

하우석 조교수는 2024년 4월 1일 KAIST 수리과학과에 부임했다. 2018년 University of Chicago에서 통계학 박사학위를 받았으며 지도교수는 Rina Foygel Barber다. 서울대학교에서 2013년 통계학 석사, 2011년 통계학·경제학 학사학위를 받았고 수학을 부전공했다.[^appointment][^home]

KAIST 부임 전에는 AWS AI Labs에서 기계학습 연구자로 일했다. 학과 부임 공지는 Amazon Web Services의 Applied Scientist 재직 기간을 2023–2024년으로 적는다. 그 전에는 UC Berkeley 통계학과의 Neyman Visiting Assistant Professor와 같은 대학 연구기관의 박사후연구원을 지냈다.[^appointment][^home]

전문 분야는 고차원 통계학과 최적화, 자료 분포가 달라지는 환경의 통계적 학습이다. 최근 연구에서는 분포가 유지되는 예측 성분의 역할, 목표 자료가 부족할 때의 학습, 학습 계산에 쓰는 배치 크기의 영향을 수학적으로 분석한다.[^home][^p1][^p2][^p3][^p4]

## 응용 분야

누리집은 통계·최적화 방법의 응용 관심으로 집단유전학(집단 안 유전적 변이의 분포와 변화를 연구하는 분야)과 우주론(우주의 기원·구조·변화를 연구하는 분야)을 든다.[^home] 최근 대표 논문이 직접 다루는 공통 문제는 학습 자료와 사용 환경의 차이를 고려한 예측이며, 목표 환경의 정답 자료를 적게 쓰면서 학습하는 방법도 포함한다.[^p1][^p2]

## 구성원

People 쪽의 현재 구성원 6명이다. 과정과 시작 시점은 게시 표기이며, Habin Jung은 Ilmun Kim 교수와 공동지도한다고 적혀 있다. 「대표 논문 참여」는 위 대표 논문의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Minseok Kang | 석사과정 | Mar 2025 |  |
| Yeongchan Yun | 석사과정 | Mar 2025 |  |
| Habin Jung | 석사과정 | Mar 2025 |  |
| Youngjoo Kim | 석박사통합과정 | Mar 2026 |  |
| Seojin Park | 석사과정 | Mar 2026 |  |
| Dongwoo Won | 석박사통합과정 | Mar 2026 |  |

## 최근 논문 목록 (2021–2026)

Research 쪽의 Preprints / Publications에 게시된 논문 가운데 2021–2026년의 10편이다. 교수 개인 논문 목록이므로 2024년 4월 KAIST 부임 전의 연구가 포함된다. 연도는 발표처의 연도 또는 해당 판본의 출판·공개 연도다. 학회는 게시 표기대로 두되 채택만 확인된 항목은 「채택」, 초록이 있는 심사 중 원고는 「사전 공개본, 심사 중」으로 표시했다. 2024년 언어 모델 논문에 적힌 교수 소속은 Amazon AI Labs다. 별표는 누리집의 저자 표시이며, 이 목록에서 역할로 풀지 않았다.[^pubs][^appointment][^pubyears][^amazon]

**2026**

- Huiyun Noh and Wooseok Ha. "A unified pairwise distribution matching framework for graph domain adaptation under structure shift". *NeurIPS 2026 (채택)*.
- Seonghwi Kim, Sung Ho Jo, Wooseok Ha, and Minwoo Chae. "Distributionally robust classification for multi-source unsupervised domain adaptation". *14th International Conference on Learning Representations (ICLR 2026) (채택). arXiv:2601.21315 (사전 공개본). DOI: https://doi.org/10.48550/arXiv.2601.21315*.

**2025**

- Wooseok Ha and Yuansi Chen. "When few labeled target data suffice: a theory of semi-supervised domain adaptation via fine-tuning from multiple adaptive starts". *arXiv:2507.14661 (사전 공개본, 심사 중). DOI: https://doi.org/10.48550/arXiv.2507.14661*.
- Keru Wu\*, Yuansi Chen\*, Wooseok Ha\*, Bin Yu. "Prominent roles of conditionally invariant components in domain adaptation: theory and algorithms". *Journal of Machine Learning Research. arXiv:2309.10301*.
- Nikhil Ghosh, Spencer Frei, Wooseok Ha, Bin Yu. "The effect of SGD batch size on autoencoder learning: sparsity, sharpness, and feature learning". *Journal of Machine Learning Research. arXiv:2308.03215*.

**2024**

- Tanmay Gautam, Youngsuk Park, Hao Zhou, Parameswaran Raman, and Wooseok Ha. "Variance-reduced zeroth-order methods for fine-tuning language models". *41st International Conference on Machine Learning (ICML 2024). arXiv:2404.08080. DOI: https://doi.org/10.48550/arXiv.2404.08080*.

**2022**

- Nikhil Ghosh, Spencer Frei, Wooseok Ha, Bin Yu. "Gradient dynamics of single-neuron autoencoders on orthogonal data". *OPT 2022: Optimization for Machine Learning (NeurIPS 2022 Workshop)*.
- Chandan Singh\*, Wooseok Ha\*, Bin Yu. "Interpreting and improving deep-learning models with reality checks". *International Workshop on Extending Explainable AI Beyond Deep Models and Classifiers. arXiv:2108.06847. DOI: https://doi.org/10.1007/978-3-031-04083-2_12*.

**2021**

- Wooseok Ha, Chandan Singh, Francois Lanusse, Srigokul Upadhyayula, Bin Yu. "Adaptive wavelet distillation from neural networks through interpretations". *35th Annual Conference on Neural Information Processing Systems (NeurIPS 2021). arXiv:2107.09145*.
- Wooseok Ha\*, Kimon Fountoulakis\*, Michael, W. Mahoney. "Statistical guarantees for local graph clustering". *Journal version Journal of Machine Learning Research. arXiv:1906.04863*.

## 연락과 위치

- 교수 연구실: 산업경영학동 3201호[^dept]
- 전화: T2748(학과 게시 표기)[^dept]
- 교수 이메일: haywse@kaist.ac.kr[^home]
[^home]: Wooseok Ha, About me. 연구 소개·학력·이전 경력·연락처. <https://haywse.github.io/> (관측일 2026-11-07).
[^dept]: KAIST 수리과학과, 교수 목록의 하우석 항목. 국문 이름·직위·전공·학위·위치·전화. <https://mathsci.kaist.ac.kr/home/people/professor/> (관측일 2026-11-07).
[^appointment]: KAIST 수리과학과, 「하우석 신임교수 부임」, 게시 2024-04-01, 갱신 2024-04-11. <https://mathsci.kaist.ac.kr/home/2024/04/%ED%95%98%EC%9A%B0%EC%84%9D-%EC%8B%A0%EC%9E%84%EA%B5%90%EC%88%98-%EB%B6%80%EC%9E%84/> (관측일 2026-11-07).
[^people]: Wooseok Ha, People. Current Members의 이름·과정·시작 연월·공동지도. <https://haywse.github.io/people/> (관측일 2026-11-07).
[^pubs]: Wooseok Ha, Research, Preprints / Publications. 제목·저자·발표처·심사·채택 표기. <https://haywse.github.io/research/> (관측일 2026-11-07).
[^pubyears]: Journal of Machine Learning Research의 출판 연도: 조건부 불변 성분 논문 26(110), 1–92(2025), <https://www.jmlr.org/papers/v26/23-1234.html>; 오토인코더 논문 26(49), 1–61(2025), <https://www.jmlr.org/papers/v26/23-1022.html>; 국소 그래프 군집화 논문 22(148), 1–54(2021), <https://www.jmlr.org/papers/v22/20-029.html>. Interpreting and improving deep-learning models with reality checks는 OpenAlex 등록 출판 연도 2022, DOI 10.1007/978-3-031-04083-2_12. <https://openalex.org/A5025862439> (관측일 모두 2026-11-07).
[^amazon]: T. Gautam 외, Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models, arXiv:2404.08080v1의 저자 소속. <https://arxiv.org/html/2404.08080v1> 및 ICML 2024 논문집 서지 <https://proceedings.mlr.press/v235/gautam24a.html> (관측일 2026-11-07).
[^contribution]: K. Wu, Y. Chen, W. Ha, B. Yu, Prominent Roles of Conditionally Invariant Components in Domain Adaptation: Theory and Algorithms, arXiv:2309.10301v3 원고 머리의 Equal contribution 각주 및 저자 소속. <https://arxiv.org/html/2309.10301v3> (관측일 2026-11-07).

[^p1]: S. Kim, S. H. Jo, W. Ha, M. Chae, arXiv:2601.21315; ICLR 2026 (채택) (온라인 2026-01-29). <https://doi.org/10.48550/arXiv.2601.21315> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.21315> (관측일 2026-11-07).
[^p2]: W. Ha, Y. Chen, arXiv:2507.14661 (사전 공개본, 심사 중) (온라인 2025-07-19). <https://doi.org/10.48550/arXiv.2507.14661> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2507.14661> (관측일 2026-11-07).
[^p3]: K. Wu, Y. Chen, W. Ha, B. Yu, Journal of Machine Learning Research 26, 1–92 (2025). <https://www.jmlr.org/papers/v26/23-1234.html> 초록 기준(출판사 논문 페이지). 초록 원문 <https://www.jmlr.org/papers/v26/23-1234.html> (관측일 2026-11-07).
[^p4]: N. Ghosh, S. Frei, W. Ha, B. Yu, Journal of Machine Learning Research 26, 1–61 (2025). <https://www.jmlr.org/papers/v26/23-1022.html> 초록 기준(출판사 논문 페이지). 초록 원문 <https://www.jmlr.org/papers/v26/23-1022.html> (관측일 2026-11-07).

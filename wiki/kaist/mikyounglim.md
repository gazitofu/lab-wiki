# 임미경 교수 연구실

**KAIST 수리과학과 · 임미경 교수**

- 영문 이름: Mikyoung Lim
- 분야: 응용수학, 역문제, 복합재료의 수학적 해석, 미분·적분 연산자의 스펙트럼 분석[^home][^dept]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 전산역학·수치 해석[^home][^p2], 복합재료[^home][^p4], 수리 최적화·최적화 알고리즘[^home][^p7]
- 홈페이지: <https://www.mikyounglim.net/>
- 근거와 출처: [임미경 교수 연구실 근거 페이지](mikyounglim-sources.md)

> 외부에서 얻은 반응으로 물체의 모양과 성질을 알아내고, 재료 내부의 구조가 전체 반응을 어떻게 바꾸는지 수학으로 설명하는 연구실이다. 형상 복원 공식, 여러 재료를 결합한 구조의 계산 방법, 확률을 이용한 표적 추적과 학습 방법의 이론을 연구한다.[^home][^p1][^p4][^p7][^p8]

## 무엇을 연구하나

임미경 교수는 복합재료(서로 다른 재료가 구분되는 부분을 이루며 결합한 재료)의 편미분방정식(여러 변수에 따라 달라지는 양과 각 변수에 대한 변화율의 관계를 적은 방정식)과 수치 계산을 핵심 연구로 소개한다.[^home] 재료의 모양과 물성(재료가 나타내는 물리적 성질)이 주어졌을 때 주변의 전기적 반응이나 힘에 따른 변형을 계산하는 문제를 다룬다. 이 과정에서 재료 내부에 들어 있는 포함체(주변 재료와 성질이 다른 내부 영역)의 모양을 계산에 반영한다.[^p2][^p4]

반대로 외부에서 얻은 반응으로 내부의 모양이나 성질을 알아내는 역문제도 연구한다. 전도도(형상과 치수의 영향을 제외한 재료 자체의 전류 전달 능력)가 다른 포함체의 형상을 복원하거나, 힘을 받는 내부 영역의 모양을 구하는 공식을 만든다. 주요 도구인 등각사상(각도를 보존하며 한 영역을 다른 영역에 대응시키는 함수)을 이용해 형상 정보와 측정에서 얻는 계수 사이의 관계를 명시한다.[^home][^p1][^p2]

또 다른 갈래는 연산자(함수 등 수학적 대상에 작용하여 다른 수학적 대상을 만드는 규칙)의 스펙트럼(상수배 변환에서 그 연산자를 뺀 변환이 유계 역변환을 갖지 못하게 하는 상수들의 집합)을 분석하는 것이다. 경계에서의 적분 계산을 행렬로 나타내어 영역이 얇아지거나 모양이 바뀔 때의 특성을 연구한다. 고유값(영이 아닌 대상을 어떤 변환이 그 자신의 상수배로 보낼 때 그 상수)을 계산하는 방법과 계산 결과가 목표 값에 가까워지는 조건도 다룬다.[^home][^p5][^p6]

누리집은 역문제를 위한 최적화·베이지안 방법·기계학습(자료에서 규칙이나 예측 방법을 학습하는 계산 기법)도 핵심으로 든다.[^home] 베이지안 최적화(계산하려는 함수의 값을 확률로 예측하고 그 불확실성을 이용해 다음 평가 위치를 정하는 최적화 방법)를 움직이는 표적의 위치와 방향 추적에 맞게 설계한다.[^p7] 신경망(연결 강도를 조정할 수 있는 계산 단위들이 서로 이어진 계산 모형)이 함수를 어느 조건에서 근사하는지, 즉 정확한 함수 대신 어느 정도의 오차로 표현할 수 있는지도 이론적으로 연구한다.[^p8]

## 주요 연구 주제

### 전기·탄성 반응에서 내부 모양 복원

전기적 반응을 기록한 계수에서 포함체의 모양을 정하는 등각사상의 계수를 복원한다. 탄성(변형을 일으킨 힘을 없앴을 때 원래 상태로 돌아가려는 물질의 성질) 문제에서는 포함체가 주변 반응에 일으키는 변화를 이용해 평면 형상을 구한다. 탄성 형상 복원 연구는 원에서 변형된 형상을 가정하고, 반복적으로 모양을 고치는 대신 공식으로 계산하는 방법을 제시한다.[^p1][^p2]

### 복합재료의 전체 물성과 은폐 구조 설계

내부 구조의 모양으로부터 복합재료 전체의 유효 물성(내부 구조가 복잡한 재료를 위치별 성질이 일정한 재료로 대신할 때 같은 전체 반응을 내도록 정한 물리적 성질)을 계산한다. 변형하지 않는 것으로 가정한 포함체가 반복 배치된 탄성 복합재료를 분석하고, 외부에서 가한 조건에 대한 물체의 흔적을 줄이는 다층 재료도 설계한다. 은폐 구조 연구는 방향에 따라 성질이 달라지는 설계를 여러 층의 등방성 재료(방향에 따라 물리적 성질이 달라지지 않는 재료)로 근사한다.[^home][^p3][^p4]

### 영역의 모양과 연산자 특성의 관계

얇은 고리 모양 영역에서 경계 적분(영역의 경계를 따라 하는 적분) 연산자의 스펙트럼이 어떻게 변하는지 분석한다. 평면 영역의 등각사상으로 라플라스 연산자(각 공간 방향에 대한 이차 변화율을 합하는 미분 연산자)의 고유값 문제를 행렬 형태로 나타내고, 유한한 크기로 잘라 계산하는 방법과 그 오차가 줄어드는 조건을 연구한다.[^p5][^p6]

### 확률적 추적과 학습 방법의 수학적 보증

먼 거리에서 얻은 자료로 움직이는 표적의 위치와 방향을 함께 추적하는 베이지안 최적화 방법을 개발한다. 표적의 모양을 모르는 경우에는 미리 계산한 자료로 학습한 신경망으로 처음 모양을 정한다. 별도로 웨이블릿(양과 음의 면적이 상쇄되며 위치와 크기를 바꿔 함수의 국소적인 변화를 표현하는 기본 함수)을 이용해 신경망의 함수 근사 능력을 분석하고, 활성화 함수(신경망의 계산 단위에서 입력을 출력으로 바꾸는 함수)에 필요한 조건과 오차의 관계를 제시한다.[^p7][^p8]

## 대표 논문

KAIST 재직 시기의 논문에서 형상 복원, 재료 설계, 연산자 분석, 확률·학습 방법을 고르게 골랐다. 연도는 누리집의 연도 구역 표기이며, 사전 공개본은 따로 표시했다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Inverse Problem for a Planar Conductivity Inclusion](https://doi.org/10.1137/22m1522395) · SIAM Journal on Imaging Sciences | 외부 측정에서 얻을 수 있는 일반화 편극 텐서(GPT, Generalized Polarization Tensors; 물체가 주변의 전기적 상태에 일으키는 변화를 계수로 정리한 수학적 양)로 균질한 평면 포함체의 모양을 복원한다. 포함체의 전도도는 임의의 상수일 수 있다. 텐서를 행렬의 곱으로 분해해 포함체의 등각사상 계수를 구하는 역산 공식을 증명했다.[^p1] | Doosung Choi, Johan Helsing, Sangwoo Kang, Mikyoung Lim. 임미경 마지막 저자 |
| 2 | 2024 | [Analytic Shape Recovery of an Elastic Inclusion from Elastic Moment Tensors](https://doi.org/10.1137/24m1646479) · SIAM Journal on Applied Mathematics | 탄성 모멘트 텐서(포함체가 주변의 탄성 반응에 일으키는 변화를 계수로 정리한 수학적 양)에서 평면 등방성 포함체의 형상을 복원하는 비반복적 방법을 제시한다. 포함체를 원에서 변형된 모양으로 보고, 경계 적분 기법과 등각사상 이론으로 형상에 대한 명시적 근사 공식을 얻었다. 수치 실험으로 방법의 타당성과 한계를 살폈다.[^p2] | Daehee Cho, Mikyoung Lim. 임미경 마지막 저자 |
| 3 | 2026 | [Cloaking laminate design based on GPT-vanishing structures](https://doi.org/10.1007/s00208-026-03572-9) · Mathematische Annalen | 여러 겹의 코팅으로 일반화 편극 텐서를 정해진 차수까지 상쇄하는 구조에서 출발해 근사 은폐용 적층 재료를 설계한다. 방향에 따라 성질이 다른 은폐 구조를 유한한 층의 등방성 재료로 근사했다. 코팅이 없는 구조에 기반한 설계와 비교해 구성 재료 사이에 필요한 전도도 차이를 줄이고, 내부의 미세 구조를 더 성긴 규모로 둘 수 있음을 제시한다.[^p3] | Eleanor Gemida, Mikyoung Lim. 임미경 마지막 저자 |
| 4 | 2024 | [Analytic asymptotic formulas for effective parameters of planar elastic composites](https://doi.org/10.48550/arxiv.2403.15714) · arXiv 사전 공개본 | 같은 바탕 재료 속에 변형하지 않는 것으로 가정한 포함체가 주기적으로 드물게 배치된 평면 복합재료의 전체 탄성 성질을 분석한다. 임의 형상의 포함체가 만드는 탄성 반응의 계수를 등각사상으로 표현하고, 이를 이용해 복합재료 전체 물성을 구하는 점근 공식(어떤 조건의 한계에 접근할 때 값의 거동을 나타내는 공식)을 유도한다.[^p4] | Daehee Cho, Doosung Choi, Mikyoung Lim. 임미경 마지막 저자 |
| 5 | 2025 | [Spectral Analysis of the Neumann–Poincaré Operator for Thin Doubly Connected Domains](https://doi.org/10.1137/24m1649058) · SIAM Journal on Mathematical Analysis | 등각사상으로 정한 두 경계 사이의 얇은 영역에서 Neumann–Poincaré 경계 적분 연산자의 스펙트럼을 분석한다. 영역 두께가 영에 가까워질 때의 변화를 무한 행렬 표현으로 다루고, 고유값의 밀도가 얇은 원형 고리의 경우에 가까워짐을 보인다.[^p5] | Doosung Choi, Mikyoung Lim, Stephen P. Shipman. 임미경 저자 2/3 |
| 6 | 2026 | [The Eigenvalue Problem for the Laplacian via Conformal Mapping and the Gohberg–Sigal Theory](https://doi.org/10.1007/s11118-026-10283-y) · Potential Analysis | 구멍이 없는 평면 영역의 라플라스 고유값 문제를 경계 적분과 외부 등각사상(영역의 바깥을 원의 바깥으로 옮기는 각도 보존 함수)으로 무한 행렬 문제로 바꾼다. 행렬의 유한한 부분을 이용한 근사 계산법을 개발하고 그 결과가 목표 값에 가까워짐을 분석했다. 등각사상 계수가 달라질 때 고유값이 어떻게 변하는지에 대한 점근 공식도 유도한다.[^p6] | Marius Beceanu, Jiho Hong, Hyun‐Kyoung Kwon, Mikyoung Lim. 임미경 마지막 저자 |
| 7 | 2026 | [Bayesian optimization approach for tracking a moving target from far-field data in three dimensions](https://doi.org/10.48550/arxiv.2607.21135) · arXiv 사전 공개본 | 하나의 입사 조건에서 얻은 원거리 자료로 삼차원 표적의 위치와 방향을 시간에 따라 함께 추적한다. 평행이동과 회전을 서로 독립인 확률 과정으로 나타내고, 이동·회전에 따른 원거리 반응 공식으로 추적용 베이지안 최적화 절차를 설계한다. 모양이 알려지지 않은 표적은 미리 계산한 자료로 학습한 신경망으로 초기 형상을 정한다. 확률 모형의 사후 일치성(관측이 쌓일수록 갱신한 확률 판단이 참된 값에 집중하는 성질)을 증명하고 수치 실험을 제시했다.[^p7] | Woojoo Lee, Sangwoo Kang, Mikyoung Lim. 임미경 마지막 저자 |
| 8 | 2026 | [Provable wavelet-based neural approximation](https://doi.org/10.1016/j.amc.2025.129821) · Applied Mathematics and Computation | 웨이블릿 이론으로 여러 종류의 활성화 함수를 쓰는 신경망의 함수 근사 능력을 분석한다. 활성화 함수가 정하는 함수 공간에서 신경망이 함수를 근사할 충분조건과 오차를 구했다. 매끄러운 함수뿐 아니라 매끄럽지 않은 활성화 함수도 다루며, 두 종류 활성화 함수 사이의 차이로 근사 오차를 제어한다.[^p8] | Youngmi Hur, Hyojae Lim, Mikyoung Lim. 임미경 마지막 저자 |

## 교수와 전문 분야

임미경 교수는 KAIST 수리과학과 교수이며, AI수학대학원을 겸임한다. 서울대학교에서 학사(1998), 석사(2000), 수학 박사(2003) 학위를 받았다. 프랑스 École Polytechnique 박사후연구원(2004–2007), 미국 Colorado State University 조교수(2007–2008)를 지냈다. KAIST 경력은 조교수 2009–2011년, 부교수 2012–2019년, 교수 2019년부터 현재로 적혀 있다.[^home][^dept]

전문 분야는 재료와 내부 구조를 설명하는 방정식의 해석, 측정 반응에서 형상을 되찾는 역산, 영역의 모양과 연산자 특성의 관계다. 최근 논문은 전도성·탄성 포함체의 해석적 형상 복원, 복합재료의 물성 계산, 베이지안 표적 추적과 신경망의 함수 근사 이론으로 이어진다.[^home][^p1][^p2][^p4][^p7][^p8]

## 응용 분야

연구가 직접 다루는 대상은 외부 측정으로 내부 물체의 모양을 알아내는 영상화, 복합재료의 전체 탄성 성질 계산, 주변의 전기적 반응에 흔적을 줄이는 은폐용 적층 재료, 원거리 자료를 이용한 움직이는 표적 추적이다. 수학적 공식과 수치 계산을 만들고 그 성질을 분석하는 연구이며, 표적 추적과 탄성 형상 복원 논문은 수치 실험으로 방법을 살핀다.[^p1][^p2][^p3][^p4][^p7]

## 구성원

Research Team의 현재 학생 5명이다. 과정과 합류 시점은 게시 표기를 따랐으며, integrated MS Ph.D. program은 석박사통합과정으로 적었다. ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Woojoo Lee | 박사과정 |  | 7 |
| Dohyeong Han | 박사과정 | Fall 2024 |  |
| Moonsoo Park | 박사과정 | Fall 2024 |  |
| Yushin Kim | 석박사통합과정 (게시: MS Student, integrated MS Ph.D. program) | Fall 2025 |  |
| Phachara Jampa | 석박사통합과정 (게시: MS Student, integrated MS Ph.D. program) | Fall 2025 |  |

## 졸업생과 이전 구성원

Research Team의 박사 졸업생 6명, 석사 졸업생 6명, 이전 박사후연구원 2명이다. 학위·과정, 연월 또는 기간, 진로는 게시 표기대로 적었다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sanghyeon Yu | Ph.D. | Assistant Professor at Korea University |
| Younghoon Jung | Ph.D. | Mobilint |
| Junbeom Kim | Ph.D. | Samsung Research |
| Doosung Choi | PhD (2022) | Visiting Assistant Professor at Case Western Reserve University (CWRU), USA, starting in Fall 2025. |
| Jiho Hong | PhD (2023) | Post-doc researcher at the Chinese University of Hong Kong (CUHK), starting in December 2023. |
| Daehee Cho | PhD (2025) | Meritz Fire & Marine Insurance Co., Ltd., starting in Fall 2025. |
| 은정 | M.S. (2011.02) |  |
| 한지훈 | M.S. (2011.08) |  |
| Jensen, Kristian Rye | M.S. (2013.08) |  |
| 반영민 | M.S. (2015.02) |  |
| Andersen, Bo Jeppe | M.S. (2016.08) |  |
| 임종현 | M.S. (2019.02) |  |
| Habib Zribi | Former postdoc (2009~2010) |  |
| Sangwoo Kang | Former postdoc (2021~2023.03) | Assistant Professor, Pusan National University |

## 최근 논문 목록 (2021–2026)

교수 개인 누리집 Publication의 2021–2026년 논문 20편이다. 연도는 누리집의 연도 구역과 개별 게시 연도를 따르며, 연도 구역 앞의 원고 중 2026년 2편은 arXiv 공개 연도를 적었다.[^oa-list] 연도 구역 앞의 원고 5편은 모두 arXiv 사전 공개본이다. KAIST 경력은 2009년에 시작하며, 이 목록의 연도는 KAIST 재직 시기에 해당한다. 공저자를 with로 적은 줄은 누리집 형식을 유지했다.[^pubs][^home]

**2026**

- Faber-Walsh field expansions for the planar conductivity problem with multiple inclusions (Authors: Doosung Choi and Mikyoung Lim), arXiv: 2609.29239 (arXiv 사전 공개본) <https://arxiv.org/abs/2609.29239>
- Bayesian optimization approach for tracking a moving target from far-field data in three dimensions (with Woojoo Lee and Sangwoo Kang), arXiv: 2607.21135 (arXiv 사전 공개본) <https://arxiv.org/abs/2607.21135>
- [66] Cloaking laminate design based on GPT-vanishing structures (with Eleanor Gemida), Mathematische Annalen (2026) <https://doi.org/10.1007/s00208-026-03572-9>
- [65] On the first Steklov–Dirichlet eigenvalue on eccentric annuli in general dimensions (with Jiho Hong, and Dong-Hwi Seo), Applicable Analysis (2026) <https://doi.org/10.1080/00036811.2026.2650407>
- [64] The Eigenvalue Problem for the Laplacian via Conformal Mapping and the Gohberg--Sigal Theory (with Marius Beceanu, Jiho Hong, Hyun-Kyoung Kwon), Potential analysis, 64, 48 (2026) <https://doi.org/10.1007/s11118-026-10283-y>
- [63] Conformal mapping based Physics-informed neural networks for designing neutral inclusions , Daehee Cho, Hyeonmin Yun, Jaeyong Lee, and M. Lim, Computers and Mathematics with Applications, 206, 347-362 (2026) <https://doi.org/10.1016/j.camwa.2026.01.026>
- [62] Provable wavelet-based neural approximation (with Youngmi Hur and Hyojae Lim), Applied Mathematics and Computation, 514, 129821 (2026). <https://doi.org/10.1016/j.amc.2025.129821>

**2025**

- [61] Bayesian optimization approach for tracking the location and orientation of a moving target using far-field data (with Woojoo Lee and Sangwoo Kang), Journal of Computational Physics, 540, 114301 (2025). <https://doi.org/10.1016/j.jcp.2025.114301>
- [60] Approximation of the first Steklov-Dirichlet eigenvalue on eccentric spherical shells in general dimensions (with Jiho Hong and Woojoo Lee), Journal of Differential Equations, 437, 113295 (2025) <https://doi.org/10.1016/j.jde.2025.113295>
- [59] Spectral analysis of the Neumann-Poincaré operator for thin doubly connected domains (with Doosung Choi, and Stephen P. Shipman), SIAM Journal on Mathematical Analysis, 57(3), 2210-2228 (2025) <https://doi.org/10.1137/24m1649058>

**2024**

- A matrix formulation of the plane elastostatic inclusion problem via geometric function theory  (with Daehee Cho and Doosung Choi), 2024 (arXiv 사전 공개본) <https://arxiv.org/abs/2403.15713>
- Analytic asymptotic formulas for effective parameters of planar elastic composites  (with Daehee Cho, and Doosung Choi), 2024 (arXiv 사전 공개본) <https://arxiv.org/abs/2403.15714>
- Monostatic imaging of an extended target with MCMC sampling  (with Jiho Hong, Sangwoo Kang), 2024 (arXiv 사전 공개본) <https://arxiv.org/abs/2401.08628>
- [58] Analytic shape recovery of an elastic inclusion from elastic moment tensors (with Daehee Cho), SIAM J. Appl. Math., 84(6), 2417 - 2439 (2024) <https://doi.org/10.1137/24m1646479>
- [57] Construction of inclusions with vanishing generalized polarization tensors by imperfect interfaces (with Doosung Choi ), Studies in Applied Mathematics, 152(2), 673-695 (2024) <https://doi.org/10.1111/sapm.12656>

**2023**

- [56] Spectral analysis of the Neumann–Poincaré operator on the crescent-shaped domain and touching disks and analysis of plasmon resonance (with Younghoon Jung), Nonlinear Analysis: Real World Applications , 74,103951 (2023) <https://doi.org/10.1016/j.nonrwa.2023.103951>
- [55] Inverse problem for a planar conductivity inclusion (with Doosung Choi, Johan Helsing, and Sangwoo Kang), SIAM Journal on Imaging Sciences 16 (2), 969-995 (2023) <https://doi.org/10.1137/22m1522395>
- [54] Geometric multipole expansion and its application to semi-neutral inclusions of general shape (with Doosung Choi, and Junbeom Kim), Zeitschrift für angewandte Mathematik und Physik (ZAMP), 74, Article number: 39 (2023) <https://doi.org/10.1007/s00033-022-01929-z>

**2022**

- [53] Fast identification of short, linear perfectly conducting cracks in a bistatic measurement configuration (with Sangwoo Kang, and Won-Kwang Park), J. Comput. Phys., 468, 111479 (2022) <https://doi.org/10.1016/j.jcp.2022.111479>
- [52] Monostatic sampling methods in limited-aperture configuration (with Sangwoo Kang), Appl. Math. Comput., 427, 127170 (2022) <https://doi.org/10.1016/j.amc.2022.127170>

## 연구 과제

첫 화면 Group Grant의 과제 1건이다. 수행 기간은 2025년 6월–2028년 5월이며, 임미경 교수가 연구책임자(PI, Principal Investigator)로 적혀 있다. 아래 공동 참여자는 과제에 함께 적힌 연구자다.[^home][^brl]

- Analysis Guided Neural Operator for Inverse Problems (역문제 해결을 위한 해석적 방법 기반 Neural Operator 연구) (기간 June 2025 – May 2028; 사업 Global Basic Research Laboratory (BRL, 글로벌 기초연구실); 지원 National Research Foundation of Korea (NRF, 한국연구재단); 역할 Mikyoung Lim (임미경, PI); 공동 참여자 Hyeuknam Kwon (권혁남), Jaeyong Lee (이재용), Sangwoo Kang (강상우))

## 수상

Research Team에 게시된 한국수학회(KMS, Korean Mathematical Society)와 한국산업응용수학회(KSIAM, Korean Society for Industrial and Applied Mathematics)의 2022년·2024년 포스터 발표 수상 3건이다. 연도와 계절은 누리집의 학회 표기이며, 아래 수상 항목의 일자는 게시되어 있지 않다.[^team][^home]

- 2024 Spring · Daehee Cho: Grand Prize in Poster Presentation, KMS spring conference
- 2024 Spring · Woojoo Lee: Poster Presentation Award, KMS conference
- 2022 Spring · Jiho Hong: award in Poster Presentation, KSIAM conference

## 연락과 위치

- 교수 연구실: 산업경영학동 3203[^dept]
- 기관 전화 게시 표기: T2735[^dept]
- 누리집 주소 표기: Daejeon 34141, Republic of Korea[^home]

## 각주
[^home]: Mikyoung Lim, Home. 교수 소개·핵심 연구·경력·Group Grant. <https://www.mikyounglim.net/> (관측일 2026-11-07).

[^dept]: KAIST 수리과학과, 교수 명단의 임미경 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> (관측일 2026-11-07).

[^team]: Mikyoung Lim, Research Team. 현재 학생·졸업생·이전 박사후연구원·수상. <https://www.mikyounglim.net/research-team> (관측일 2026-11-07).

[^pubs]: Mikyoung Lim, Publication. Book·Papers 목록. <https://www.mikyounglim.net/publication> (관측일 2026-11-07).

[^brl]: Analysis Guided Neural Operator for Inverse Problems. <https://sites.google.com/view/mathai-ip-brl> (관측일 2026-11-07).

[^oa-list]: OpenAlex, Mikyoung Lim의 DOI 대응 논문 서지. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p1]: D. Choi, J. Helsing, S. Kang, M. Lim, SIAM Journal on Imaging Sciences (2023). <https://doi.org/10.1137/22m1522395> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p2]: D. Cho, M. Lim, SIAM Journal on Applied Mathematics (2024). <https://doi.org/10.1137/24m1646479> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p3]: E. Gemida, M. Lim, Mathematische Annalen (2026). <https://doi.org/10.1007/s00208-026-03572-9> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p4]: D. Cho, D. Choi, M. Lim, arXiv (Cornell University) (2024). <https://doi.org/10.48550/arxiv.2403.15714> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p5]: D. Choi, M. Lim, S. P. Shipman, SIAM Journal on Mathematical Analysis (2025). <https://doi.org/10.1137/24m1649058> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p6]: M. Beceanu, J. Hong, H.-K. Kwon, M. Lim, Potential Analysis (2026). <https://doi.org/10.1007/s11118-026-10283-y> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p7]: W. Lee, S. Kang, M. Lim, arXiv (Cornell University) (2026). <https://doi.org/10.48550/arxiv.2607.21135> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

[^p8]: Y. Hur, H. Lim, M. Lim, Applied Mathematics and Computation 514, 129821 (2026; 온라인 2025-11-13). <https://doi.org/10.1016/j.amc.2025.129821> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5009719640,publication_year:2021-2026> (관측일 2026-11-07).

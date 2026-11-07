# 기하위상수학 및 기하군론 연구실 (Team for Academic Research on GEometric Topology)

**KAIST 수리과학과 · 백형렬 부교수**

- 영문 교수 이름: Hyungryul Harry Baik
- 분야: 저차원 위상수학, 기하위상수학, 기하군론, 곡면의 변환과 동역학, 수학과 인공지능[^dept][^research]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 기하·위상수학[^research]
- 홈페이지: <https://www.hbaik.org/>
- 근거와 출처: [기하위상수학 및 기하군론 연구실 근거 페이지](hbaik-sources.md)

> 공간의 모양과 그 공간을 움직이는 변환의 규칙을 함께 연구하며, 이 수학을 인공지능의 수학 추론 평가와 시간 순서 자료의 학습에도 연결하는 연구실이다.[^research]

## 무엇을 연구하나

연구실의 중심은 저차원 위상수학(낮은 차원의 공간을 연속적으로 변형해도 유지되는 성질로 연구하는 분야)과 기하군론(대칭이나 변환의 합성 규칙을 이루는 군을 거리와 공간의 관점에서 연구하는 분야)이다. 군은 원소를 결합하는 연산에서 세 원소를 괄호로 묶는 방식이 결과를 바꾸지 않고, 어떤 원소와 결합해도 그 원소를 바꾸지 않는 원소가 있으며, 모든 원소에 연산을 되돌릴 짝이 있는 집합이다. 연구실은 기하 구조, 반복되는 변환의 움직임, 대수적 규칙이 서로 어떤 제약을 주는지 묻는다. 공간에 작용하는 변환들의 규칙에서 원래 공간의 구조를 알아낼 수 있는지, 곡면을 변환하는 방식에서 대수적 성질을 읽어낼 수 있는지가 주요 질문이다.[^research]

한 갈래는 원 위의 군 작용(군의 연산과 일치하도록 각 원소를 공간의 변환에 대응시키는 것)에서 기하를 복원하는 연구다. 원의 점들을 끝점으로 삼아 원판 안에서 서로 교차하지 않는 선들을 기록한 라미네이션을 다룬다. 불변 라미네이션이 있으면 그 작용이 쌍곡기하에서 나온 것인지 아닌지 가를 수 있다. 연구실은 곡면뿐 아니라 삼차원 공간과 그 안의 흐름을 원 위 작용에서 구성하는 문제도 다룬다.[^research]

다른 갈래는 곡면의 변환을 반복할 때 생기는 이동 거리와 군의 대수적 성질을 연결한다. 곡선 그래프는 곡면 위에서 본질적으로 다른 단순 닫힌 곡선을 꼭짓점으로 삼고, 서로 만나지 않게 놓을 수 있는 관계를 연결선으로 표현한 것이다. 연구실은 이 그래프에서 곡면의 변환이 점을 얼마나 움직이는지 측정하고, 그 값과 변환들이 군 전체를 만들어 내는 성질 사이의 관계를 연구한다. 무작위 보행(확률적으로 고른 변환을 차례로 합성하는 과정)이 만드는 이동 거리도 다룬다.[^research]

최근에는 인공지능의 수학 추론과 자료 학습도 연구한다. 대형 언어 모델(많은 글을 학습해 글을 이해하고 생성하는 인공지능 모델)의 연구 수준 수학 추론을 평가하며, 조건이 잘못된 문제를 알아보는지도 시험한다.[^research] 수학 명제를 컴퓨터가 검사할 수 있는 언어로 옮기는 작업에서는 원래 뜻과 형식화한 명제가 일치하는지에 주목한다. 또 시계열(시간 순서에 따라 기록한 자료)의 위상 구조를 학습하는 방법을 개발해, 자료를 변형하면서 잃을 수 있는 구조적 정보를 보존하려 한다.[^research]

## 주요 연구 주제

### 1. 원 위의 작용과 공간의 기하

불변 라미네이션에서 쌍곡기하(휘어진 정도가 어디서나 같고 음수인 공간의 기하)와 연결된 군을 판별하고, 원 위 작용에서 삼차원 공간과 흐름을 복원한다. 삼차원에서의 결과는 라미네이션 쌍(두 라미네이션을 함께 보존하는 구조, 영문 veering pair)을 보존하는 군을 다룬다. 이는 원 위의 동역학(변환을 반복하거나 시간이 흐를 때 상태가 변하는 방식을 연구하는 분야)과 공간의 기하를 잇는 연구다.[^research]

### 2. 곡면의 변환과 이동 거리

사상류군은 곡면의 방향을 보존하는 연속적인 일대일 변환을 연속 변형으로 같은 것끼리 묶고 합성한 군이다. 연구실은 이 군의 원소가 곡선 그래프에서 만드는 평균 이동 거리와, 변환 및 그 켤레들이 군 전체를 생성하는 성질의 관계를 연구한다. 켤레는 기준을 바꾸는 변환, 원래 변환, 그 역변환을 차례로 합성해 얻는 원소다. 역변환은 앞의 변환을 되돌리는 변환이다.[^research]

### 3. 군의 큰 규모 기하와 무작위성

점 사이 거리를 보존하는 변환을 등거리변환이라 한다. 연구실은 등거리변환들의 군에서 무작위 보행이 만드는 이동 거리의 증가를 연구한다. 점점 큰 거리 척도로 본 공간에서 모든 점을 그대로 두는 군 원소가 무엇인지도 계산한다. 이는 군이 공간에 작용할 때 드러나는 정보와 사라지는 정보를 가리는 문제다.[^research]

### 4. 수학과 인공지능

대형 언어 모델이 수학 문제를 풀고 문제의 조건을 판단하는 능력을 평가하며, 대학원 대수학(연산과 그 규칙을 추상적인 수학 구조로 연구하는 분야) 문제를 형식 언어(기호와 문장을 만드는 규칙을 엄밀히 정한 언어)로 옮긴 자료를 만든다. 시계열에서는 지속 호몰로지(자료를 살피는 척도를 바꿀 때 연결 성분과 구멍 같은 구조가 생기고 사라지는 것을 기록하는 방법)로 구조를 표현하고, 시간적 정보와 함께 학습하는 방법을 개발한다. 연구 소개는 이 두 방향을 수학적 추론의 평가와 수학적 구조를 이용한 학습으로 설명한다.[^research]

## 대표 논문

KAIST 재직 시기의 논문 중 원 위 작용, 곡면의 변환, 군의 큰 규모 기하, 수학과 인공지능을 보여 주는 8편이다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸은 전체 저자 목록에서 확인되는 교수의 참여를 적는다. Co-Hopfianity와 Lean-GAP은 사전 공개본이다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Groups acting on veering pairs and Kleinian groups](https://doi.org/10.1112/jlms.70052) · Journal of the London Mathematical Society | 원 위에서 특정한 라미네이션 쌍을 보존하는 변환들의 군 중 일부가 쌍곡 삼차원 오비폴드의 군임을 보였다. 오비폴드는 국소적으로 유한한 대칭으로 같은 점을 묶은 공간의 구조를 허용하는 공간이다. 이 접근은 처음부터 삼차원 공간이 있다고 가정하지 않고 원 위의 구조에서 공간의 기하를 얻는다.[^p1] | Hyungryul Baik, Hongtaek Jung, KyeongRo Kim |
| 2 | 2025 | [Minimal Asymptotic Translation Lengths on Curve Complexes and Homology of Mapping Tori](https://doi.org/10.1307/mmj/20226319) · The Michigan Mathematical Journal | 곡면 변환이 특정한 대수적 정보에 영향을 주지 않는다는 조건 아래, 곡선들을 기록한 공간에서 평균 이동 거리가 얼마나 작아질 수 있는지 상한과 하한을 제시했다. 또 이동 거리가 작으면서도 그 변환과 켤레들로 사상류군 전체를 생성하지 못하는 예를 구성했다.[^p2] | Hyungryul Baik, Dongryul M. Kim, Chenxi Wu |
| 3 | 2024 | [Linear growth of translation lengths of random isometries on Gromov hyperbolic spaces and Teichmüller spaces](https://doi.org/10.1017/s1474748023000373) · Journal of the Institute of Mathematics of Jussieu | 특정한 쌍곡형 거리 공간에서 비초등적 무작위 보행이 만드는 변환의 이동 거리가 적어도 선형으로 증가함을 증명했다. 비초등적이라는 조건은 보행이 생성하는 작용의 무한히 먼 극한 방향이 두 점 이하에 갇히지 않는다는 뜻이며, 선형 증가는 단계 수에 비례하는 증가다. 한 단계 이동 거리의 거듭제곱 평균인 모멘트에 조건을 두지 않는 결과다.[^p3] | Hyungryul Baik, Inhyeok Choi, Dongryul M. Kim |
| 4 | 2025 | [On the kernel of actions on asymptotic cones](https://doi.org/10.1515/jgth-2024-0126) · Journal of Group Theory | 군을 점점 큰 거리 척도로 보는 극한 공간인 점근뿔에서, 군의 자연스러운 작용이 모든 점을 그대로 두게 하는 원소들을 계산했다. 이 원소들의 집합을 무한히 먼 방향을 나타내는 경계에서의 작용과 연결했다. 일정 조건 아래 이 집합의 크기가 군이 비초등적 작용을 가질 수 있는지 판별하는 데 쓰임을 보였다.[^p4] | Hyungryul Baik, Wonyong Jang |
| 5 | 2026 | [Co-Hopfianity is not a profinite property](https://doi.org/10.48550/arxiv.2603.04197) · arXiv, 사전 공개본 | 유한한 군들을 통해 보는 구조는 같지만, 자신으로 가는 일대일 연산 보존 대응의 성질은 다른 두 군을 구성했다. 한 군에서는 그런 대응이 항상 군 전체를 덮고, 다른 군에서는 전체를 덮지 않는 대응이 존재한다. 원래 군의 이 자기 대응 성질이 유한한 군들을 통한 구조만으로는 결정되지 않는다는 반례다.[^p5] | Hyungryul Baik, Wonyong Jang |
| 6 | 2026 | [TopoCL: Topological Contrastive Learning for Time Series](https://doi.org/10.1109/tnnls.2026.3675422) · IEEE Transactions on Neural Networks and Learning Systems | 사례 쌍의 유사성과 차이를 학습 목표로 쓰는 대조학습에서 자료 변형으로 시계열의 구조적 정보가 손실되는 문제를 다뤘다. 지속 호몰로지로 얻은 구조를 신경망(연결된 계산 단위들이 입력을 조합하고 변환하는 계산 모형)으로 표현하고, 시간적 정보 안의 대조학습과 시간·위상 정보의 대응을 함께 학습하는 TopoCL을 제안했다. 분류·이상 탐지·예측과, 한 과제에서 배운 정보를 다른 과제에 활용하는 전이학습으로 평가했다.[^p6] | Nam-Woo Kim, Hyungryul Baik, Yoonjin Yoon |
| 7 | 2026 | [Lean-GAP: A Dataset of Formalized Graduate Algebra Problems](https://doi.org/10.48550/arxiv.2606.02588) · arXiv, 사전 공개본 | 대학원 대수학 문제 430개를 증명 보조 도구 Lean 4의 형식 언어로 옮긴 자료를 제시했다. 문서 전처리와 자동 형식화에 이어 원래 문제와 형식화한 명제의 뜻이 일치하는지 확인하는 절차를 만들었다. 이 마지막 검증에는 사람의 주의 깊은 확인이 필요함을 설명하고, 형식화 모델들의 성능과 병목을 분석했다.[^p7] | Seewoo Lee 외, Hyungryul Baik 공저 |
| 8 | 2026 | [Random groups at density d&lt;1/2: sharp length inequalities for generalized torsion and a fixed-width exclusion via first-order transfer](https://doi.org/10.1007/s00013-026-02291-6) · Archiv der Mathematik | 특정 밀도 범위의 무작위 군(생성원과 관계식을 확률적으로 골라 정의한 군)에서 같은 원소의 켤레들을 곱해 항등원(다른 원소와 결합해도 그 원소를 바꾸지 않는 원소)을 만드는 관계가 만족해야 하는 길이의 하한을 증명했다. 군 원소를 생성원들의 나열인 단어로 나타내어 길이를 재고, 그 관계를 표현하는 도형의 경계 길이를 이용해 제약을 얻었다.[^p8] | Hyungryul Baik 단독 |

## 교수와 전문 분야

백형렬 교수는 2009년 KAIST에서 수학 학사를 마치고, 2014년 8월 Cornell University에서 수학 박사 학위를 받았다. 박사 지도교수는 William Thurston, John Hubbard, Dylan Thurston이다. 2014년 9월부터 2017년 1월까지 University of Bonn에서 박사후연구원으로 일했으며, 2017년 2월 KAIST에 부임했다.[^about][^group] 학과 교수 목록의 직위는 부교수이고, 분야는 위상수학이며 세부 분야로 기하학·기하위상수학·기하군론·쌍곡기하학을 적는다.[^dept]

현재 전문 분야는 원 위 군 작용과 공간의 기하 복원, 곡면 변환의 이동 거리, 무작위 보행과 군의 큰 규모 기하다. 최근 논문에는 군의 자기 대응 성질과 무작위 군의 관계식, 위상 구조를 이용한 시계열 학습, 수학 문제의 형식화도 포함된다.[^research][^p1][^p3][^p5][^p6][^p7][^p8]

## 응용 분야

연구 소개가 직접 연결하는 응용은 수학 추론을 하는 인공지능의 평가와 시계열 표현 학습이다. TopoCL은 시간 순서 자료의 분류·이상 탐지·예측·전이학습을 다루고, Lean-GAP은 수학 교재 문제를 컴퓨터가 검사하는 형식으로 표현하고 그 의미를 확인하는 자료와 방법을 다룬다.[^research][^p6][^p7]

## 구성원

Research Group의 Current members에 적힌 8명이다. 과정과 연구 주제는 해당 구획의 표기이며, 시작은 같은 쪽의 합류 소식에 적힌 날짜다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시한다.[^group]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 김잔 (Jan Kim) | 박사후연구원 (KAIST) |  |  |  |
| Brendan Murran | 박사과정 (KAIST) | 2022.8 | Foliations and related topics |  |
| 이홍준 (Hongjun Lee) | 박사과정 (KAIST) | 2023.1.5 | Teichmüller theory and related topics |  |
| 오준성 (Junseong O) | 박사과정 (KAIST) | 2024.9.2 | Pseudo-Anosov diffeomorphisms |  |
| 황세현 | 박사과정 (KAIST) | 2025.7.16 | Hyperbolic geometry |  |
| 조민구 | 박사과정 (KAIST) | 2025.7.16 | Geometric Group Theory |  |
| Farisan Hafizh | 석사과정 (KAIST) | 2026.3.2 | Geometric Group Theory |  |
| Margarita Marchlewitz | 대학원생 (KAIST) |  |  |  |

## 졸업생과 이전 구성원

Alumni and supervision history의 14명과 Former postdoctoral researchers의 2명이다. 학위·과정과 기간은 게시 표기이며, PhD Student 기간은 학위 취득 연도를 뜻하지 않는다. KAIST 부임 전 Bonn에서 지도한 이력도 포함한다. 진로는 같은 쪽이 적은 내용이다.[^group][^about]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 이동하 (Dongha Lee) | PhD Student; 공동지도 Jingsung Park (KIAS) (2020.08–2026.02) |  |
| 백주헌 (Juhun Baik) | PhD Student (2019.06–2026.01) |  |
| 김준석 (Junseok Kim) | PhD Student; M.S. in Mathematics, KAIST, Feb. 2020 (2018.06–2025.08) |  |
| 장원용 (Wonyong Jang) | PhD Student (2018.01–2025.02) |  |
| 최인혁 (Inhyeok Choi) | PhD Student (2018.12–2023.02) | Professor at KIAS (2026.7.1 소식) |
| 정성구 (Sunggu Jeong) | PhD Student (2018.09–2023.02) |  |
| 김창섭 (Changsub Kim) | PhD Student (2018.01–2023.02) |  |
| Philippe Aurelio Tranchida | PhD student (2018.08–2022.08) |  |
| 오상록 (Sangrok Oh) | PhD student (2018.09–2022.02) |  |
| 김경로 (Kyeong-Ro Kim) | PhD student; Ph.D. in Mathematics, KAIST, Aug. 2021 (2017.06–2021.08) |  |
| 김동률 (Dongryul M. Kim) | Undergraduate research student (2019.08–2021.08) |  |
| 곽상훈 (Sanghoon Kwak) | Undergraduate research student (2018.01–2018.12) |  |
| Esmee Te Winkel | M.A. in Mathematics, University of Bonn (2016) | Subsequently received a Ph.D. at the University of Warwick |
| Benjamin Wassermann | M.A. in Mathematics, University of Bonn; secondary advisor (2016) | Subsequently received a Ph.D. at KIT |
| Khanh Le | Former postdoctoral researcher (ended September 2026) |  |
| 서동균 (Donggyun Seo) | Postdoc (2020.09–2021.08) |  |

## 최근 논문 목록 (2021–2026)과 연도 미상 게재 승인 원고

교수 개인 Publications 목록의 출판·게재 승인·사전 공개본 27편이다. 제목·공저자·발표처는 누리집 표기이며, 개인 목록에는 KAIST 부임 전 연구도 포함된다. 날짜가 확인되는 논문은 2021년 10월 13일 이후의 항목이고, 학술지 연도는 누리집 표기를 따른다. 사전 공개본은 처음 공개된 연도로 두며, 책 장 「Normal generators for mapping class groups」의 연도도 사전 공개본의 최초 공개 연도다. 게재 승인 3편 가운데 사전 공개 날짜가 구간 안에서 분명한 1편만 최초 공개 연도에 두었다. 학술지 게재 승인 연도가 없는 두 원고는 「연도 표기 없음」에 두고 「게재 승인」으로 표시한다. NeurIPS 2026 항목은 「채택」으로 표시한다.[^pubs][^normal][^simple]

**2026**

- Random groups at density d<1/2: sharp length inequalities for generalized torsion and a fixed-width exclusion via first-order transfer, Arch. Math. (2026), published online. DOI: 10.1007/s00013-026-02291-6. arXiv:2602.02183. <https://doi.org/10.1007/s00013-026-02291-6>
- Monodromy through narrow bifurcation locus of the Mandelbrot set (with J. Baik), Glasnik Matematicki (2026), 61(1), pp. 77–115. <https://doi.org/10.3336/gm.61.1.04>
- SH²: A Mathematician-Curated benchmark for Assessing Research-level Math Capabilities of LLMs (with Guijin Son et al.), accepted at NeurIPS 2026, Evaluations & Datasets Track (poster). Preprint title: Soohak: A Mathematician-Curated Benchmark for Evaluating Research-level Math Capabilities of LLMs. arXiv:2605.09063. (채택) [arXiv\](https://arxiv.org/abs/2605.09063)
- TopoCL: Topological Contrastive Learning for Time Series (With N. Kim, Y. Yoon), IEEE Transactions on Neural Networks and Learning Systems 37(9) (2026), pp. 4863–4874. 10.1109/TNNLS.2026.3675422. <https://doi.org/10.1109/tnnls.2026.3675422>
- Lean-GAP: A Dataset of Formalized Graduate Algebra Problems (with Seewoo Lee et al.), arXiv:2606.02588. (사전 공개본) [arXiv\](https://arxiv.org/abs/2606.02588)
- Co-Hopfianity is not a profinite property (with W. Jang), arXiv:2603.04197. (사전 공개본) [arXiv\](https://arxiv.org/abs/2603.04197)
- Uniform Perfectness and Centers in Sublinearly Morse Boundaries, arXiv:2602.14673. (사전 공개본) [arXiv\](https://arxiv.org/abs/2602.14673)
- Optimizing the Upper-Bound Constant for the Crossing Number of Polynomial Curve Systems, arXiv:2602.02144. (사전 공개본) [arXiv\](https://arxiv.org/abs/2602.02144)

**2025**

- Groups acting on veering pairs and Kleinian groups (with H. Jung, K. Kim), J. Lond. Math. Soc. 111(1), e70052 (2025), DOI 10.1112/jlms.70052. <https://doi.org/10.1112/jlms.70052>
- On the asymptotic translation lengths on the sphere complexes and the generalized fibered cone (with D.M. Kim, C. Wu), Trans. Amer. Math. Soc., Volume 378, Number 7, 2025, Pages 4739–4764. <https://doi.org/10.1090/tran/9371>
- Normal generators for mapping class groups (with D. M. Kim), forthcoming chapter in In the Tradition of Thurston: Geometry and Topology, Vol. 4 (edited by A. Papadopoulos and K. Ohshika). arXiv:2504.14759. (게재 승인) [arXiv\](https://arxiv.org/abs/2504.14759)
- Minimal asymptotic translation lengths on curve complexes and homology of mapping tori (with D. M. Kim, C. Wu), Michigan Math. J. 75(5): 927-942 (2025). <https://doi.org/10.1307/mmj/20226319>
- Reducible normal generators for mapping class groups are abundant (with D.M. Kim, C. Wu), J. Topol. Anal. Vol. 17, No. 05, pp. 1313-1323 (2025). <https://doi.org/10.1142/s1793525323500474>
- On the kernel of actions on asymptotic cones (with W. Jang), J. Group Theory., vol. 28, no. 4, 2025, pp. 753-809. <https://doi.org/10.1515/jgth-2024-0126>

**2024**

- On Translation Lengths of Pseudo-Anosov Maps on the Curve Graph (with C. Kim), Bull. Korean Math. Soc. 61 (2024), No. 3, pp. 585–595. [arXiv\](https://arxiv.org/abs/2212.09891)
- Topological and dynamical properties of Torelli groups of partitioned surfaces (with H. Shin, P. Tranchida), Geom. Dedicata. 218, 38 (2024). <https://doi.org/10.1007/s10711-024-00889-0>
- Linear growth of translation lengths of random isometries on Gromov hyperbolic spaces and Teichmüller spaces (with I. Choi, D. M. Kim), J. Inst. Math. Jussieu, Volume 23, Issue 4, 2024, pp. 1751 - 1795. <https://doi.org/10.1017/s1474748023000373>
- Reconstruction of Anosov flows from infinity (with C. Wu, B. Zhao), arXiv:2407.07634. (사전 공개본) [arXiv\](https://arxiv.org/abs/2407.07634)
- Acylindrical hyperbolicity of outer automorphism groups of right-angled Artin groups (with J. Kim), arXiv:2405.19702. (사전 공개본) [arXiv\](https://arxiv.org/abs/2405.19702)

**2023**

- Asymptotic translation lengths and normal generation for pseudo-Anosov monodromies of fibered 3-manifolds (with E. Kin, H. Shin, C. Wu), Algebr. Geom. Topol. 23-3 (2023), 1363--1398. <https://doi.org/10.2140/agt.2023.23.1363>
- On the finiteness property of hyperbolic simplicial actions: the right-angled Artin groups and their extension graphs (with D. Seo, H. Shin), Geom. Dedicata. 217, 7 (2023). <https://doi.org/10.1007/s10711-022-00736-0>

**2022**

- Foliations from left orders (with S. Hensel, C. Wu), J. Korean Math. Soc. 2022; 59(4): 699-715. [arXiv\](https://arxiv.org/abs/2108.09694)
- Random walks on mapping class groups (with I. Choi), EMS Surv. Math. Sci. 9 (2022), no. 2, pp. 279–320. <https://doi.org/10.4171/emss/59>
- On the surjectivity of the symplectic representation of the mapping class group (with I. Choi, D. M. Kim), Topol. Appl. 322 (2022): 108334. <https://doi.org/10.1016/j.topol.2022.108334>
- Topological entropy of pseudo-Anosov maps on punctured surfaces vs. homology of mapping tori (with J. Baik, C. Kim, P. Tranchida), Glasnik Matematicki (2022), Vol. 57(77), 291-312. <https://doi.org/10.3336/gm.57.2.09>

**연도 표기 없음**

- Characterization of Fuchsian Groups as Laminar Groups & the Structure Theorem of Hyperbolic 2-Orbifolds (with K. Kim), to appear in Glasnik Matematicki. arXiv:2110.06481. (게재 승인) [arXiv\](https://arxiv.org/abs/2110.06481)
- Simple length spectra as moduli for hyperbolic surfaces and rigidity of length identities (with I. Choi, D. M. Kim), to appear in Ann. Inst. Fourier. (게재 승인) [arXiv\](https://arxiv.org/abs/2012.05652)

## 수상과 선정

Research Group에 게시된 2021년 10월 13일–2026년 10월 13일의 수상·선정 2건이다.[^group]

- 2024.12.5 · 최인혁이 S-Oil의 Dissertation of the Year Awards를 받았다.
- 2023.12.29 · 백형렬 교수의 「Asymptotic translation lengths and normal generation for pseudo-Anosov monodromies of fibered 3-manifolds」가 KAIST 자연과학대학의 excellent paper로 선정됐다.

## 소식

Research Group에 게시된 2021년 10월 13일–2026년 10월 13일의 연구그룹 출범과 수학 해설 글 소식 4건이다. 날짜는 누리집 표기다.[^group]

- 2025.3 · KAIST-KIAS 공동 연구그룹 2K-GATE가 공식 출범했다.
- 2024.7.25 · 백형렬 교수의 「Flows in 3-manifolds」 글이 KIAS 웹진 Horizon에 실렸다.
- 2023.11.17 · 백형렬 교수의 「Ping-pong lemma」 글이 KIAS 웹진 Horizon에 실렸다.
- 2022.7 · 백형렬 교수의 「What is Topology?」 글이 KIAS 웹진 Horizon에 실렸다.

## 연락과 위치

- 소속과 주소: Department of Mathematical Sciences, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 교수 연구실: E6-1, 4407호. 학과 교수 목록은 자연과학동 4407로 적는다.[^home][^dept]
- 기관 전화: +82-42-350-2712[^home]
- 면담: 사전 약속[^home]

## 각주
[^dept]: KAIST 수리과학과 교수 목록, 백형렬 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> 관측 2026-11-07.
[^home]: Hyungryul Harry Baik, Home, 부임 시점·Contact. <https://www.hbaik.org/> 관측 2026-11-07.
[^group]: Hyungryul Harry Baik, Research Group, 연구 소개·Current members·Alumni and supervision history·Former postdoctoral researchers·News. <https://www.hbaik.org/lab.html> 관측 2026-11-07.
[^research]: Hyungryul Harry Baik, Research, 연구 질문과 네 갈래의 연구 설명. <https://www.hbaik.org/research.html> 관측 2026-11-07.
[^about]: Hyungryul Harry Baik, About me, 학력과 University of Bonn·KAIST 경력. <https://www.hbaik.org/myself.html> 관측 2026-11-07.
[^pubs]: Hyungryul Harry Baik, Publications, Published/Accepted Papers·Preprints·PhD Thesis·Other writings. <https://www.hbaik.org/publications.html> 관측 2026-11-07.
[^normal]: H. Baik, D. M. Kim, Normal generators for mapping class groups, arXiv:2504.14759. 최초 공개 2025-04-20, 최종판 수정 2026-04-10, 책 장 게재 예정 표시. <https://arxiv.org/abs/2504.14759> 관측 2026-11-07.
[^simple]: H. Baik, I. Choi, D. M. Kim, Simple length spectra as moduli for hyperbolic surfaces and rigidity of length identities, arXiv:2012.05652. 최초 공개 2020-12-10, 최종판 수정 2025-06-17, Annales de l'Institut Fourier 게재 예정 표시. <https://arxiv.org/abs/2012.05652> 관측 2026-11-07.
[^p1]: H. Baik, H. Jung, K. Kim, Journal of the London Mathematical Society 111, e70052 (2025). <https://doi.org/10.1112/jlms.70052> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p2]: H. Baik, D. M. Kim, C. Wu, The Michigan Mathematical Journal 75, 927–942 (2025). <https://doi.org/10.1307/mmj/20226319> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p3]: H. Baik, I. Choi, D. M. Kim, Journal of the Institute of Mathematics of Jussieu 23, 1751–1795 (2024). <https://doi.org/10.1017/s1474748023000373> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p4]: H. Baik, W. Jang, Journal of Group Theory 28, 753–809 (2025). <https://doi.org/10.1515/jgth-2024-0126> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p5]: H. Baik, W. Jang, arXiv (Cornell University) (2026). <https://doi.org/10.48550/arxiv.2603.04197> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p6]: N.-W. Kim, H. Baik, Y. Yoon, IEEE Transactions on Neural Networks and Learning Systems 37, 4863–4874 (2026). <https://doi.org/10.1109/tnnls.2026.3675422> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p7]: S. Lee 외, K.-H. Lee, arXiv (Cornell University) (2026). <https://doi.org/10.48550/arxiv.2606.02588> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.
[^p8]: H. Baik, Archiv der Mathematik (2026). <https://doi.org/10.1007/s00013-026-02291-6> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022148779,publication_year:2021-2026> 관측 2026-11-07.

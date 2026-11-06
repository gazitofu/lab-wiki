# Electronic Structure Theory Group

**KAIST 물리학과 · 한명준 교수**

- 분야: 응집물질 이론, 상관 전자계와 자성·초전도 물질의 이론·계산[^dept][^research]
- 대분야: 물리·양자, 소재
- 태그: 응집물질 이론[^theory], 강상관 전자계[^theory], 제1원리 계산[^methods], 초전도[^sc]
- 홈페이지: <https://sites.google.com/site/myungjoonhan/>
- 근거와 출처: [Electronic Structure Theory Group 근거 페이지](myungjoonhan-sources.md)

> 물질의 자석 성질과 전기가 흐르는 방식을 계산으로 설명하고, 새로운 물질을 찾는 이론 연구실이다.

## 무엇을 연구하나

한명준 교수 연구그룹은 응집물질 이론(고체와 액체 속 많은 입자가 함께 보이는 현상을 수학적 모형과 계산으로 설명하는 연구)을 한다.[^theory] 특히 전자(음의 전기를 띠는 기본 입자)들이 서로 미치는 영향을 따로 떼어 다루기 어려운 강상관 물질을 연구한다.[^theory] 전자 구조는 물질 안에서 전자들이 가질 수 있는 상태와 에너지(물리계가 일을 할 수 있는 능력을 나타내는 양)의 분포를 뜻하며, 연구실은 이를 계산해 물질의 자성(물질이 자석 성질을 보이거나 자기장에 반응하는 성질)과 전기적 특성을 설명한다.[^theory]

이 과정에서 계산을 쓰는 데 그치지 않고 개념과 방법도 개발한다. 제1원리 계산(실험으로 맞춘 물성값 대신 양자역학의 기본 방정식에서 출발해 물질의 성질을 구하는 계산)을 바탕으로 상관 전자 구조와 자성의 계산법을 만들고, 물질 계산 소프트웨어 OpenMX(Open source package for Materials eXplore)의 개발에 참여한다.[^methods] 양자역학은 원자와 전자 같은 미시적인 대상의 상태와 변화를 설명하는 물리 이론이다. 대표 논문 1은 전자 수를 바꿀 때 스핀(입자가 지니는 고유한 각운동량) 사이의 상관관계가 어떻게 달라지는지로 훈트 결합(서로 다른 원자 궤도의 전자 스핀이 나란해지는 상태를 선호하게 하는 상호작용)의 효과를 판별하는 방법을 제안했다. 각운동량은 회전 운동의 정도를 나타내는 양이며, 상관관계는 여러 물리량의 변화가 서로 연관되는 관계다. 원자는 물질의 기본적인 화학 성질을 지니는 단위 입자이며, 원자 궤도는 원자 안 전자의 공간적 분포를 나타내는 상태다.[^p1]

물질 연구에서는 고온 초전도체를 비롯한 상관 전자 물질을 다룬다. 초전도는 일정한 온도 아래에서 전기 저항이 사라지고 내부 자기장을 밀어내는 현상이며, 연구실은 초전도의 원리와 관련 현상을 밝히고 그 특성을 향상하는 문제를 연구한다.[^sc] 대표 논문 5는 무한층 니켈 산화물(니켈 산화물 층이 끝없이 이어지는 구조의 화합물)에서 훈트 결합의 효과가 나타나는 금속 상태를 제시했다. 대표 논문 4는 CrTe2(크롬과 텔루륨의 화합물)에서 움직이는 전자와 원자 부근에 머무는 자석 성질이 함께 나타나며, 이들의 상호작용이 자성을 이끄는 모습을 계산했다.[^p5][^p4]

또 하나의 갈래는 위상 물질(전자 상태가 연속적인 변형에도 유지되는 수학적 성질로 구분되는 물질)이다. 연구 소개는 물질 연구의 범위에 자성 물질과 위상 물질이 든다고 적는다.[^topo] 대표 논문 7은 NaZnBi에서 시간의 방향을 뒤집거나 결정을 거울에 비추는 대칭성 가운데 하나가 깨져도 특징적인 표면 전자 상태가 유지되는 계산 결과를 제시했다. 결정은 원자 배열이 공간적으로 반복되는 고체 구조를 뜻한다. 대표 논문 3은 전자 사이 상호작용 계산을 원자별 스핀의 움직임과 연결해, 얇은 물질 안에서 다양한 자석 성질의 공간 배열을 찾았다.[^p7][^p3]

## 주요 연구 주제

### 1. 상관 전자를 설명하는 개념과 계산 도구

훈트 상관관계를 판별하는 지표와 전자 상호작용을 계산하는 이론을 연구한다. 대표 논문 2는 TaS2(탄탈럼과 황의 화합물) 단일층에서 한 원자 부근의 전자끼리 미치는 영향과 서로 다른 위치의 전자끼리 미치는 영향을 계산하고, 이들을 다루는 계산 근사를 바꾸어 전자 구조를 살폈다.[^p1][^p2] 연구실이 개발에 참여하는 OpenMX 외에, Jx는 전자 구조 계산 결과를 받아 자석 성질의 상호작용을 계산하며, DMFT-pack과 Kai-EDJ는 상관 전자와 자성 계산을 위한 프로그램이다.[^methods] DMFT는 Dynamical Mean-Field Theory의 줄임말로, 주변 전자들의 영향을 시간에 따라 변하는 평균적인 환경으로 바꾸어 전자들의 집단 거동을 계산하는 동적 평균장 이론을 뜻한다.

### 2. 층상 자성 물질과 새로운 물질 탐색

대표 논문 3은 단일층 전이금속 칼코겐화물(전이금속과 황·셀레늄·텔루륨 같은 원소가 결합한 화합물)을 계산해 스커미온(스핀 방향이 공간에서 감기며 위상적으로 구분되는 자성 배열) 등을 안정하게 만들 후보를 찾았다.[^p3] 대표 논문 4는 CrTe2의 자성과 전자 상관관계를 연결했다. 단일층에서 자성을 유지하는 온도가 낮아지는 현상은 그 연구에서 차원 감소 자체보다 구조 변형과 관련되었다.[^p4]

### 3. 초전도 물질의 금속 상태와 구조 변화

초전도체와 훈트 금속(훈트 결합이 전자의 집단적 거동에 중요한 영향을 주는 금속), 콘도 현상(이동하는 전자와 국소적인 자석 성질의 상호작용으로 나타나는 저온 현상)을 연구한다.[^research] 대표 논문 5는 니켈 산화물의 금속 상태를 분석했고, 대표 논문 6은 VTe2(바나듐과 텔루륨의 화합물)의 결정 상태를 바꾸어 콘도 효과가 달라지는 현상을 다뤘다.[^p5][^p6]

### 4. 위상 물질과 카고메 금속의 전자 상태

연구 범위에는 위상 물질도 든다.[^topo] 대표 논문 7은 NaZnBi를 두 종류의 대칭성이 함께 보호하는 위상 절연체(내부는 전류가 흐르지 않지만 보호된 표면 전자 상태를 지니는 물질) 후보로 제안했다.[^p7] 대표 논문 8은 카고메(삼각형들이 꼭짓점을 공유하는 육각형 그물 배열) 금속 CsV3Sb5(세슘·바나듐·안티모니의 화합물)에서 안티모니 원자의 특정 전자 궤도가 전자 상태와 상호작용의 크기를 결정하는 데 중요한 역할을 한다고 밝혔다.[^p8]

## 대표 논문

KAIST 재직 시기의 논문 가운데 계산 방법, 자성 물질, 초전도 물질의 전자 상태, 위상 물질을 고르게 담도록 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Frozen spin ratio and the detection of Hund correlations](https://doi.org/10.1103/physrevresearch.5.033134) · Physical Review Research | 훈트 결합이 중요한 물질을 가릴 방법을 제안했다. 같은 위치의 스핀 사이에 오랜 시간이 지나도 남는 상관관계를 순간적인 값으로 나눈 비율을 사용했다. 전자 수가 바뀔 때 이 비율이 변하는 방향과 온도에 따른 변화를 분석하고, 여러 궤도를 다루는 모형 및 구리·철 화합물 사례로 판별 근거를 살폈다. 가능한 전자 자리의 절반을 채운 경우를 제외한 정수 채움과, 전자 수를 그 절반 채움 쪽으로 바꾼 경우에 적용할 수 있다고 제안했다.[^p1] | 1저자 Siheon Ryee, 마지막 저자 한명준 |
| 2 | 2023 | [First-principles investigation of screened Coulomb interaction and electronic structure of low-temperature TaS2](https://doi.org/10.1016/j.isci.2023.106681) · iScience | 저온에서 전자 밀도가 주기적으로 달라지는 TaS2 단일층을 대상으로, 주변 전자들이 전자 사이 힘을 가리는 효과와 전자 구조를 계산했다. 같은 위치와 서로 다른 위치의 전자 사이 상호작용을 두 가지 모형으로 추정하고, 서로 다른 위치의 효과를 다루는 근사를 단계적으로 바꾸며 전자 구조를 조사했다.[^p2] | 1저자 Taek Jung Kim, 마지막 저자 한명준 |
| 3 | 2026 | [First-principles-based search for emergent topological spin textures in transition-metal dichalcogenide monolayers](https://doi.org/10.1038/s41524-026-02162-2) · npj Computational Materials | 전자 수준의 계산, 자성 상호작용 계산, 원자별 스핀 운동의 모의를 연결해 새로운 자성 배열을 지닌 물질을 찾는 틀을 만들었다. 단일층 전이금속 칼코겐화물을 조사해 스커미온과 복잡한 자성 영역 등을 찾고, 서로 경쟁하는 자성 상호작용이 이 배열을 안정하게 만드는 원리를 분석했다.[^p3] | 1저자 Yuhyun Cha, 마지막 저자 한명준 |
| 4 | 2026 | [Many-body electronic structure, self-doped double-exchange, and Hund metallicity in 1T-CrTe2 bulk and monolayer](https://doi.org/10.1038/s41699-026-00670-9) · npj 2D Materials and Applications | CrTe2 안에서 자유롭게 움직이는 전자와 특정 위치에 머무는 자석 성질이 공존함을 계산했다. 두 종류의 전자 상태 사이에서 훈트 결합이 자성을 이끄는 원리를 제시했다. 이 설명은 단일층에서도 유지되지만, 단일층의 구조 변형은 자성을 유지하는 온도를 낮추는 데 중요한 역할을 했다.[^p4] | 1저자 Dong Hyun David Lee, 마지막 저자 한명준 |
| 5 | 2023 | [Infinite-layer nickelates as Ni-eg Hund’s metals](https://doi.org/10.1038/s41535-023-00568-5) · npj Quantum Materials | 무한층 니켈 산화물에서 온도와 전자 수가 바뀔 때 전자 상태와 전하·스핀·궤도의 반응이 어떻게 달라지는지 계산했다. 전하란 전기적 상호작용의 세기와 방향을 정하는 입자의 성질이다. 니켈 원자 궤도 사이의 훈트 결합 때문에 특정 궤도에 훈트 금속의 특징이 나타남을 보였다. 이를 철 기반 초전도체나 구리 산화물과 구별되는 금속 상태로 제시했다.[^p5] | 1저자 Byungkyun Kang, 한명준 공저 |
| 6 | 2024 | [Polymorphic Kondo effects driven by spin lattice coupling in VTe2](https://doi.org/10.1002/adfm.202313180) · Advanced Functional Materials | 빛을 조사해 VTe2의 서로 다른 결정 상태를 국소적으로 만들고, 저온에서 상태마다 다른 콘도 효과를 관찰했다. 계산에서는 한 상태에서 바나듐 전자의 자석 성질이 주변 전자에 의해 가려지는 효과가 강해졌으며, 이를 두 상태에서 다르게 관찰되는 전기 흐름의 특성과 연결했다.[^p6] | 1저자 Dongyeun Won, 한명준 공저 |
| 7 | 2022 | [Robust dual topological insulator phase in NaZnBi](https://doi.org/10.1038/s41427-022-00383-7) · NPG Asia Materials | 시간 반전과 결정의 거울 대칭성이 함께 위상적 성질을 지키는 물질로 NaZnBi를 제안했다. 계산에서는 두 대칭성 가운데 하나가 깨져도 특징적인 표면 전자 상태가 유지되었다. 이러한 성질을 바탕으로 외부 교란이 있는 조건의 소자에 사용할 물질 후보가 될 가능성을 제시했다.[^p7] | 1저자 Hyunggeun Lee, 한명준 공저 |
| 8 | 2022 | [Crucial role of out-of-plane Sb-p orbitals in Van Hove singularity formation and electronic correlation for superconducting Kagome metal CsV3Sb5](https://doi.org/10.1103/physrevb.105.235145) · Physical Review B | 초전도 카고메 금속 CsV3Sb5의 전자 구조를 설명하려면 평면 밖 안티모니 전자 궤도의 역할이 중요함을 보였다. 이 궤도는 특정 에너지에 전자 상태가 집중되는 특징과 전자 사이 상호작용에 영향을 주었다. 평면 밖 원자 간격을 바꾸는 변형과 압력에 따라 이 특징이 어떻게 달라지는지도 조사했다.[^p8] | 1저자 Min Yong Jeong, 마지막 저자 한명준 |

## 교수와 전문 분야

한명준 교수는 서울대학교에서 물리학 학사와 박사 학위를 각각 2001년과 2007년에 받았다. 서울대학교, University of California Davis, Columbia University, Argonne National Lab에서 박사후연구원으로 일했고, 교수 누리집은 2012년 7월부터 KAIST에서 재직한다고 적는다.[^home] KAIST 물리학과는 현재 직위를 교수로, 분야를 응집물질 이론으로 소개한다.[^dept][^faculty]

학과 연구 소개와 최근 논문을 함께 보면 전문 분야는 상관 전자계의 이론·계산, 자성의 미시적 원리, 초전도 물질의 전자 상태, 위상 물질 후보 탐색이다. 개념과 계산법을 개발하는 연구부터 실제 화합물의 전자 구조를 설명하는 연구까지 이어진다.[^dept][^p1][^p3][^p4][^p5][^p7]

## 응용 분야

연구실은 전이금속 산화물의 겹층 구조와 경계면에서 전자 상태를 조절하고 새 물질을 계산으로 설계하는 문제를 연구한다.[^dept] 대표 논문 3은 스핀 기반 기술에 쓸 자성 배열을 지닌 물질 탐색을, 대표 논문 7은 외부 교란에도 표면 상태를 유지하는 소자용 물질 후보를 제시한다. 두 경우 모두 물질 탐색과 가능성 제안의 수준이다.[^p3][^p7]

## 구성원

2026년 11월 7일 연구실 Group Members 페이지 기준이다. 박사후연구원과 대학원생의 이름·과정·연구 주제는 연구실 표기를 따른다. 「M. S. 2024」는 누리집의 이름 옆 표기다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Hyunggeun Lee | 박사후연구원 | Density functional theory, Inverse design of materials, topological materials | 7 |
| Dong Hyun David Lee | 박사과정 | 2D magnetism, strongly correlated system, nanoparticles | 4 |
| Yoon-Gu Kang | 박사과정 |  |  |
| Chulwan Lee | 박사과정 |  |  |
| Yuhyun Cha | 박사과정 |  | 3 |
| Byung Hyun Jeong | M. S. 2024 |  |  |
| Ji Won Choi | 박사과정 |  |  |
| Kangil Cho | 박사과정 |  |  |
| Yoonro Lee | 박사과정 |  |  |

## 졸업생과 이전 구성원

2026년 11월 7일 연구실 Alumni 구역의 이전 구성원이다. 학위·과정과 연도, 진로는 연구실 게시 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Heung Sik Kim | postdoc (2013-2014) | Assistant Professor (KENTECH) |
| Alex Tae Kyung Lee | postdoc (2013-2014) | Postdoctoral researcher (Yale University) |
| Yung Ting Lee | postdoc (2015-2017) | Assistant Professor (National Taitung University, Taiwan) |
| Myung-Chul Jung | postdoc (2018-2021) | Research Assistant Professor (Chosun University) |
| Hyeong Jun Lee | postdoc (2022-2024) | Research Staff (LG Energy Solution) |
| Hongkee Yoon | Ph. D (2018) | Assistant Professor (KangWon National University) |
| Jae-Hoon Sim | Ph. D (2018) | Staff (Korea Science Academy of KAIST) |
| Seung Woo Jang | Ph. D (2019) | Research Staff (Samsung Electronics) |
| Siheon Ryee | Ph. D (2020) | Assistant Professor (Pusan National University) |
| Min Yong Jeong | Ph. D (2021) | Research Staff (Samsung Electronics) |
| Taek Jung Kim | Ph. D (2021) | Research Staff (Samsung Advanced Institute of Technology) |
| Do Hoon Kiem | Ph. D (2023) | Postdoctoral Researcher (Oak Ridge National Laboratory) |
| Sang Jun Sim | M. S. (2024) |  |
| Jaewon Kim | M. S. (2024) |  |
| Matteo Ugliotti | Exchange student from ETH Zurich (2024) | Ph. D candidate, Georgia Institute of Technology |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 2021–2026년 연도 구역에 게시된 논문이다. 연도·제목·저자·발표처는 연구실 표기이며 DOI를 함께 적었다. 정확한 출판 날짜가 확인되는 논문은 2021년 10월 13일 이후를 대상으로 한다. 날짜가 따로 없는 논문은 연구실의 연도 구역을 따른다. 「published online」은 온라인 출판 표기다.[^pubs]

**2026**

- D. H. Kiem, M. Nauman, J. Choi, D. Graf, J. Kim, H. Yang, J.-G. Park, Y. Jo, M. J. Han. "Crucial Role of Magnetic Dipole and Anomalous Field Dependence in NiPS3". *Small (published online); https://doi.org/10.1002/smll.75903*.
- B.-H. Jeong, H. S. Kim, J. Choi, S. B. Lee and M. J. Han. "High-Throughput Discovery of Quantum Frustrated Materials". *Adv. Funct. Mater. (published online); arxiv:2603.12745; https://doi.org/10.1002/adfm.77777*.
- D. Wulferding, D. An, J. Choi. D. Mun, Y. Choi, S. Kuppusamy, S. Krishnamoorthi, R. Sankar, M. J. Han, S. K. Kim and K.-Y. Choi. "Plaid-Like Spin Splitting and Chirality of Magnon Bands in Antiferromagnetic MnTe2". *Advanced Science (published online); arxiv:2607.02114; https://doi.org/10.1002/advs.76555*.
- Y. Cha, D. H. Kiem, and M. J. Han. "First-principles-based search for emergent topological spin textures in transition-metal dichalcogenide monolayers". *npj Computational Materials 12 292 (2026); https://doi.org/10.1038/s41524-026-02162-2*.
- J. Cha, H. Lee, S. Sim, Y. Sur, K. -T. Kim, J. -H. Han, S. -W. Kim, G. Lee, J. Hyun, C. -y. Lim, Y. Ahn, S. Gim, J. D. Denlinger, S. Kim, K. H. Kim, S. Lee, M. J. Han, Y. Kim. "Evidence of time-reversal symmetry breaking above the charge density wave order in a kagome metal". *Nat. Phys. 22 1245 (2026); https://doi.org/10.1038/s41567-026-03331-2*.
- J. Pandey, D. Wulferding, W. Cho, M. -C. Jung, J. Jeong, N. Myoung,  M. J. Han, S. Cho, H. Yang. "Spin-phonon coupling and magnetic ordering in layered CrPS4". *ACS Appl. Mater. Interfaces 18 19797 (2026); https://doi.org/10.1021/acsami.5c25896*.
- P. Noh, H. Lee, M. J. Han, E. G. Moon. "Fully Generalized Spin Models with Strain Effects of Kitaev Spin Liquid Candidate Materials". *Commun. Phys. 9 199 (2026); arxiv:2505.23909; https://doi.org/10.1038/s42005-026-02607-6*.
- D. H. D. Lee, H. J. Lee, T. J. Kim, M. Y. Jeong, M. J. Han. "Many-body electronic structure, self-doped double-exchange, and Hund metallicity in 1T-CrTe2 bulk and monolayer". *npj 2D Materials and Applications 10 33 (2026); arxiv:2603.20713; https://doi.org/10.1038/s41699-026-00670-9*.
- B. H. Kim, C. -H. Park, Y. -W. Son, and M. J. Han. "(invited review in Korean) Theoretical and Computational Methods for Magnetic van der Waals Materials and Their Applications". *Physics and High Technology (물리학과 첨단기술) 35 18 (2026)*.

**2025**

- W. Cho, J. Cha, Y. -G. Kang, D. H. D. Lee, J. Oh, D. Kim, S. Yer, J. Lee, H. Hong, Y. Yang, Y. K. Kim, M. J. Han, H. Yang. "Polymorphic spin ordering in a single-crystalline cobalt-doped Fe3GaTe2". *ACS Nano 19 41033 (2025); arxiv:2505.05198; https://doi.org/10.1021/acsnano.5c12923*.
- H. J. Lee, T. J. Kim, H. Yoon, M. J. Han. "KaiEDJ: A program conducting dynamical mean-field theory and magnetic force theory calculation for correlated magnetic materials". *Comput. Phys. Comm. 316 109779 (2025); https://doi.org/10.1016/j.cpc.2025.109779*.
- D. Kim, D. H. D. Lee, D. W. Lee, H. J. Choi, H. Y. Woo, Y. Choi, S. H. Kim, M. Y. Yu, H. Choi, Y. Kim, S. J. Oh, T. Zhao, M. J. Han, T. Paik. "Antimony Sulfobromide Nanowire Bundles Exhibiting Ambipolar Photoelectrochemical Photocurrent Switching". *Small 21 e05782 (2025); doi.org/10.1002/smll.202505782*.
- J.-H. Chung, K. Shin, T. R. Yokoo, D. Ueta, M. Imai, H.-s. Kim, D. H. Kiem, M. J. Han, S.-i. Shamoto. "Massive Dirac magnons in the three-dimensional honeycomb magnetic oxide FeTiO3". *Scientific Reports 15 5978 (2025); https://doi.org/10.1038/s41598-025-90478-2*.

**2024**

- R. Roemer, D. H. D. Lee, S. Smit, X. Zhang, S. Godin, V. Hamza, T. Jian, J. Larkin, H. Shin, C. Liu, M. Michiardi, G. Levy, Z. Zhang, R. J. Green, C. Kim, D. Muller, A. Damascelli, M. J. Han, K. Zou. "Unraveling the Electronic Structure and Magnetic Transition Evolution Across Monolayer, Bilayer, and Multilayer Ferromagnetic Fe3GeTe2". *npj 2D Materials and Applications 8 63 (2024); https://doi.org/10.1038/s41699-024-00499-0*.
- J. Won, J. Bae, J. Won, T. Kim, S. Choi, H. Kim, S.-H. V. Oh, G. Lee, E. Lee, S. Jeon, M. Kim, H. W. Do, D. Seo, S. Kim, Y. Cho, H. Kang, B. Kim, H. Choi, J. Han, T. Kim, N. Nemati, C. Park, K. Lee, H. Moon, J. Kim, H. Lee, D. W. Davies, D. Kim, S. Kang, B.-K. Yu, J. Kim, M. K. Cho, J.- H. Bae, S. Park, J. Kim, H.-J. Sung, M.-C. Jung, I. Chung, H. Choi, H. Choi, D. Kim, H. Baik, J.-H. Lee, H. Yang, Y. Kim, H.-G. Park, W. Lee, K. J. Chang, M. Kim, D. W. Chun, M. J. Han, A. Walsh, A. Soon, J. Cheon, C. Park, J.-Y. Kim, W. Shim. "Cation-eutaxy enabled III-V-derived van der Waals crystals as memristive semiconductors". *Nat. Mater. 24 1402 (2024); https://doi.org/10.1038/s41563-024-01986-x*.
- D. W. Lee, S. Oh, D. H. D. Lee, H. Y. Woo, J. Ahn, S. H. Kim, B. K. Jung, Y. Choi, D. Kim, M. Y. Yu, C. G. Park, H. Yun, T. -H. Kim, M. J. Han, S. J. Oh, T. Paik. "Ultrathin, High-Aspect-Ratio Bismuth Sulfohalide Nanowire Bundles for Solution-Processed Flexible Photodetectors". *Adv. Sci. 11 2403463 (2024); https://doi.org/10.1002/advs.202403463*.
- H. Lee, M. J. Han, K. J. Chang. "Large-gap Z2 and topological crystalline insulating phase in RbZnBi and CsZnBi". *ACS Omega 9 29820 (2024); https://doi.org/10.1021/acsomega.4c03506*.
- W. Cho, Y. -G. Kang, J. Cha, D. H. D. Lee, D. H. Kiem, J. Oh, J. Park, C. Kim, Y. Yang, Y. K. Kim, M. J. Han, H. Yang. "Singular Hall Response from a Correlated Ferromagnetic Flat Nodal-line Semimetal". *Adv. Mater. 36 2402040 (2024); arxiv:2312.12889; https://doi.org/10.1002/adma.202402040*.
- S. Sim, M. Y. Jeong, H. Lee, D. H. D. Lee, and M. J. Han. "Chemical effect on the Van Hove singularity in superconducting kagome metal AV3Sb5 (A=K, Rb, Cs)". *Phys. Chem. Chem. Phys. 26 11715 (2024); https://doi.org/10.1039/d4cp00517a*.
- D. Won, D. H. Kiem, W. Cho, S. -H. Yang, Y. -H. Kim, Y. -M. Kim, S. Cho, M. J. Han, H. Yang. "Polymorphic Kondo effects driven by spin lattice coupling in VTe2". *Adv. Funct. Mater. 34 2313180 (2024); https://doi.org/10.1002/adfm.202313180*.
- J. Jeong, D. H. Kiem, D. Guo, R. Duan, K. Watanabe, T. Taniguchi, Z. Liu, M. J. Han, S. Zheng, H. Yang. "Spin-selective memtransistors with magnetized graphene". *Adv. Mater. 36 2310291 (2024); https://doi.org/10.1002/adma.202310291*.
- S. Jeon, J. Ahn, M. -C. Jung, H. K. Woo, J. Bang, B. K. Jung, S. Oh,  S. Y. Lee, K. J. Lee, T. Paik, D. -H. Ha, J. -P. Ahn, S. Jeong, D. H. Kim, J. H. Noh, H. S. Jang, M. J. Han and S. J. Oh. "Defect Engineering of Metal Halide Perovskite Nanocrystals via Spontaneous Diffusion of Ag Nanocrystals". *Small 20 2307032 (2024); https://doi.org/10.1002/smll.202307032*.

**2023**

- P. Park, W. Cho, C. Kim, Y. An, Y. -G. Kang, M. Avdeev, R. Sibille, K. Iida, R. Kajimoto, K. H. Lee, W. Ju, E. -J. Cho, H.-J. Noh, M. J. Han, S. -S. Zhang, C. D. Batista, J.-G. Park. "Tetrahedral triple-Q magnetic ordering and large spontaneous Hall conductivity in the metallic triangular antiferromagnet Co1/3TaS2". *Nature Communications 14 8346 (2023); https://doi.org/10.1038/s41467-023-43853-4*.
- J. Won, J. Bae, H. Kim, T. Kim, N. Nemati, S. Choi, H. Lee, S. Kim, H. Choi, B. Kim, D. Jin, M. J. Han, J. -Y. Kim, W. Shim. "Polytypic two-dimensional FeAs with high anisotropy". *Nano Letters 23 11057 (2023); https://doi.org/10.1021/acs.nanolett.3c03324*.
- Y. Ahn, G. Lee, N. Noh, C. Lee, D. D. Le, S. Kim, Y. Lee, J. Hyun, C. -y. Lim, J. Cha, M. Jho, S. Gim, J. Denlinger, C. -H. Yang, J. M. Yuk,  M. J. Han, Y. Kim. "Converting the Bulk Transition Metal Dichalcogenides Crystal into Stacked Monolayers via Ethylenediamine Interaction". *Nano Letters 23 9733 (2023); https://doi.org/10.1021/acs.nanolett.3c02268*.
- D. -H. Gim, D. Wulferding, C. Lee, H. Cui, K. Nam, M. J. Han  and K. H. Kim. "Fingerprints for anisotropic Kondo lattice behavior in the quasiparticle dynamics of the kagome metal Ni3In". *Phys. Rev. B 108 115143 (2023); https://doi.org/10.1103/physrevb.108.115143*.
- S. Ryee, S. Choi and M. J. Han. "Frozen spin ratio and the detection of Hund correlations". *Phys. Rev. Research 5 033134 (2023); arxiv:2207.10421; https://doi.org/10.1103/physrevresearch.5.033134*.
- Y. An, P. Park, K. Zhang, H. Kim, M. Avdeev, J. Kim, M. J. Han, H. -J. Noh, S. Seong, J. -S. Kang, H. -D. Kim and J. -G. Park. "Bulk properties of the chiral metallic triangular antiferromagnets Ni1/3NbS2 and Ni1/3TaS2". *Phys. Rev. B 108 054418 (2023); https://doi.org/10.1103/physrevb.108.054418*.
- B. Kang, C. Melnick, P. Semon, S. Ryee, M. J. Han, G. Kotliar and S. Choi. "Infinite-layer nickelates as Ni-eg Hund’s metals". *npj Quantum Materials 8 35 (2023); arXiv:2007.14610; https://doi.org/10.1038/s41535-023-00568-5*.
- K. -M. Kim, D. H. Kiem, G. Bednik, M. J. Han and M. J. Park. "Ab Initio Spin Hamiltonian and Topological Noncentrosymmetric Magnetism in Twisted Bilayer CrI3". *Nano Letters 23 6088 (2023); arxiv:2206.05264; https://doi.org/10.1021/acs.nanolett.3c01529*.
- H. -S. Kim, S. H. Park and M. J. Han. "Epitaxially strained ultrathin LaNiO3/LaAlO3 and LaNiO3/SrTiO3 superlattices: a density functional theory +U study". *Current Applied Physics 50 53 (2023); arxiv:2302.02424; https://doi.org/10.1016/j.cap.2023.03.012*.
- T. J. Kim, M. Y. Jeong and M. J. Han. "(invited contribution) First-principles investigation of screened Coulomb interaction and electronic structure of low-temperature TaS2". *iScience 26 106681 (2023); arxiv:2206.08519; https://doi.org/10.1016/j.isci.2023.106681*.
- H. Lee, M.-C. Jung, D. H. D. Lee and M. J. Han. "First-principles theory-based design of highly reflective metals for radiative cooling". *Current Applied Physics 49 1 (2023); https://doi.org/10.1016/j.cap.2023.02.010*.
- H. -J. Yang, H. S. Kim, M. Y. Jeong, Y. B. Kim, M. J. Han and S. B. Lee. "Intertwining orbital current order and superconductivity in Kagome metal". *SciPost Physics Core 6 8 (2023); arxiv:2203.07365; https://doi.org/10.21468/scipostphyscore.6.1.008*.

**2022**

- T. J. Kim, S. Ryee and M. J. Han. "Fe3GeTe2: A site-differentiated Hund metal". *npj Computational Materials 8 245 (2022); arxiv:2202.02022; https://doi.org/10.1038/s41524-022-00937-x*.
- D. H. Kiem, H. J. Lee and M. J. Han. "(invited review in Korean) Magnetic Force Response Theory". *J. Kor. Mag. Soc. 32 (4) 172-179 (2022); https://doi.org/10.4283/jkms.2022.32.4.172*.
- D. H. Kiem, M. Y. Jeong, H. Yoon, M. J. Han. "Strain engineering and the hidden role of magnetism in monolayer VTe2". *Nanoscale (communication) 14 10009 (2022); arxiv:2203.16023; https://doi.org/10.1039/d2nr03026h*.
- M. Y. Jeong, H. -J. Yang, H. S. Kim, Y. B. Kim, S. B. Lee and M. J. Han. "Crucial role of out-of-plane Sb-p orbitals in Van Hove singularity formation and electronic correlation for superconducting Kagome metal CsV3Sb5". *Phys. Rev. B 105 235145 (2022); arxiv:2203.09329; https://doi.org/10.1103/physrevb.105.235145*.
- Y. K. Choi, T. Park, D. H. D. Lee, J. Ahn, Y. H. Kim, S. Jeon, M. J. Han, and S. J. Oh. "Wearable anti-temperature interference strain sensor with metal nanoparticle thin film and hybrid ligand exchange". *Nanoscale 14 8628 (published online); https://doi.org/10.1039/d2nr02392j*.
- J. Hyun, M. Y. Jeong, M. -C. Jung, Y. Lee, Y. Kim, S. Jung, B. Seok, J. Song, C. -y. Lim, J. Cha, G. Lee, Y. An, M. Hashimoto, D. Lu, J. D. Denlinger, S. W. Kim, C. Kim, M. J. Han, S. Kim and Y. Kim. "Strain-controlled evolution of electronic structure indicating topological phase transition in the quasi-one-dimensional superconductor TaSe3". *Phys. Rev. B 105 115143 (2022); arXiv:2009.05917; https://doi.org/10.1103/physrevb.105.115143*.
- P. Park, Y. -G. Kang, J. Kim, K. H. Lee, H.-J. Noh, M. J. Han, J.-G. Park. "Field-tunable toroidal moment and anomalous Hall effect in noncollinear antiferromagnetic Weyl semimetal Co1/3TaS2". *npj Quantum Materials 7 42 (2022); arXiv:2008.13171; https://doi.org/10.1038/s41535-022-00449-3*.
- M. Lee, D. H. D. Lee, S. V. Hong, H. Y. Woo, J.-Y. Chae, D. W. Lee, M. J. Han, T. Paik. "Highly Luminescent and Multifunctional Zero-Dimensional Cesium Lanthanide Chloride (Cs3LnCl6) Colloidal Nanocrystals". *Adv. Opt. Mater. 10 2102727 (2022); https://doi.org/10.1002/adom.202102727*.
- M. Khazaei, A. Ranjbar, Y.-G. Kang, Y. Liang, R. Khaledialidusti, S. Bae, H. Raebiger, M. J. Han, H. Mizoguchi, M. S. Bahramy, T. D. Kuhne, K. Ohno, H. Hosono. "Electronic structures of group III-V element haeckelite compounds: A novel family of semiconductors, Dirac semimetals, and topological insulators". *Adv. Funct. Mater. 32 2110930 (2022); https://doi.org/10.1002/adfm.202110930*.
- H. Lee, Y. -G. Kang, M. -C. Jung, M. J. Han, and K. J. Chang. "Robust dual topological insulator phase in NaZnBi". *NPG Asia Materials 14 36 (2022); https://doi.org/10.1038/s41427-022-00383-7*.

**2021**

- Y. Cho, H. Yoon, S. Yi, J. Choo, M. J. Han, J. Lee, S. Kim. "Deep-DFT: A Physics-ML Hybrid Approach to Predict Molecular Energy using Transfomer". *Advances in Neural Information Processing Systems (NeurlIPS) Workshop (2021)*.
- Y. -G. Kang, I.-H. Lee, M. J. Han, and K. J. Chang. "Ab Initio prediction of nontrivial topological band and superconductivity in stable metallic Si allotropes at ambient pressure". *Phys. Rev. Materials 5 104802 (2021); https://doi.org/10.1103/physrevmaterials.5.104802*.
- S. Bae, Y. -G. Kang, K. Ichihashi, M. Khazaei, V. Swamy, M. J. Han, K. J. Chang, K. Shudo, H. Raebiger. "Strain engineering to release trapped hole carriers in p-type haeckelite GaN". *ACS Appl. Electron. Mater. 3 5257 (2021); https://doi.org/10.1021/acsaelm.1c00765*.

## 연락과 위치

- 교수 연구실: KAIST E6-2 4308호[^dept]
- 주소: 대전광역시 유성구 대학로 291, KAIST 물리학과[^dept]
- 교수 전화: +82-42-350-2544[^home][^dept]
- 팩스: +82-42-350-2510[^home]
- 교수 이메일: mj.han@kaist.ac.kr[^home]
[^home]: Myung Joon Han, 교수 소개·학력·경력·연락. <https://sites.google.com/site/myungjoonhan/> 관측일 2026-11-07.
[^dept]: KAIST 물리학과, Han, Myung Joon 교수 소개. <https://physics.kaist.ac.kr/index.php?document_srl=267&mid=p_people1> 관측일 2026-11-07.
[^faculty]: KAIST 물리학과, Professor 목록의 Han, Myung Joon. <https://physics.kaist.ac.kr/index.php?mid=p_people1&category=193> 관측일 2026-11-07.
[^members]: Myung Joon Han, Group Members의 Postdocs·Graduate Students·Alumni. <https://sites.google.com/site/myungjoonhan/Home/group-members> 관측일 2026-11-07.
[^pubs]: Myung Joon Han, Publications. <https://sites.google.com/site/myungjoonhan/Home/publication> 관측일 2026-11-07.
[^research]: Myung Joon Han, Research의 Correlated Quantum Materials. <https://sites.google.com/site/myungjoonhan/Home/research> 관측일 2026-11-07.
[^theory]: KAIST 물리학과, Han, Myung Joon 교수 소개의 Condensed Matter Theory·strongly correlated electron systems. <https://physics.kaist.ac.kr/index.php?document_srl=267&mid=p_people1> 관측일 2026-11-07.
[^methods]: Myung Joon Han, Research의 Concept, Method, Algorithm·Code and Software. <https://sites.google.com/site/myungjoonhan/Home/research> 관측일 2026-11-07.
[^sc]: KAIST 물리학과, Han, Myung Joon 교수 소개의 High temperature superconductivity. <https://physics.kaist.ac.kr/index.php?document_srl=267&mid=p_people1> 관측일 2026-11-07.
[^topo]: Myung Joon Han, Research의 Correlated Quantum Materials 중 magnetic and topological materials. <https://sites.google.com/site/myungjoonhan/Home/research> 관측일 2026-11-07.
[^p1]: S. Ryee, S. Choi, M. J. Han, Physical Review Research (2023). <https://doi.org/10.1103/physrevresearch.5.033134> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p2]: T. J. Kim, M. Y. Jeong, M. J. Han, iScience (2023). <https://doi.org/10.1016/j.isci.2023.106681> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p3]: Y. Cha, D. H. Kiem, M. J. Han, npj Computational Materials (2026). <https://doi.org/10.1038/s41524-026-02162-2> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p4]: D. H. D. Lee 외, M. J. Han, npj 2D Materials and Applications (2026). <https://doi.org/10.1038/s41699-026-00670-9> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p5]: B. Kang 외, S. Choi, npj Quantum Materials (2023). <https://doi.org/10.1038/s41535-023-00568-5> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p6]: D. Won 외, H. Yang, Advanced Functional Materials (2024). <https://doi.org/10.1002/adfm.202313180> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p7]: H. Lee 외, K. J. Chang, NPG Asia Materials (2022). <https://doi.org/10.1038/s41427-022-00383-7> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.
[^p8]: M. Y. Jeong 외, M. J. Han, Physical review. B./Physical review. B (2022). <https://doi.org/10.1103/physrevb.105.235145> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5046376217,publication_year:2021-2026> 관측일 2026-11-07.

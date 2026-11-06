# 응용역학 연구실 (Advanced Applied Mechanics Laboratory, AAML)

**KAIST 건설및환경공학과 · 홍정욱 교수**

- 영문 이름: Advanced Applied Mechanics Laboratory
- 분야: 구조물의 충격·폭발·지진 거동, 재료의 변형과 균열, 수치해석 방법, 자연모사 복합재료, 파동과 유체·구조 상호작용[^dept][^research]
- 대분야: 건설·도시·인프라, 기계·로봇·제조
- 태그: 전산역학·수치 해석[^dept], 고체역학·소성[^dept], 복합재료[^dept]
- 홈페이지: <https://aaml.kaist.ac.kr>
- 근거와 출처: [응용역학 연구실 근거 페이지](aaml-sources.md)

> 구조물과 재료가 힘을 받아 변형되고 부서지는 과정을 실험과 계산으로 밝히고, 이를 예측하는 해석 방법과 자연을 본뜬 복합재료를 연구한다.[^dept][^research]

## 무엇을 연구하나

홍정욱 교수가 이끄는 응용역학 연구실은 건물·벽·송전탑 같은 구조물과 그 재료가 외부 힘을 받을 때 어떻게 움직이고 손상되는지 연구한다. 학과 소개는 재료의 소성(힘을 없앤 뒤에도 변형이 남는 성질)과 균열, 구조물의 충격·폭발 반응, 자연모사(생물이나 자연의 구조·원리를 설계에 적용하는 접근) 복합재료(성질이 다른 재료를 구분되는 부분으로 결합한 재료)의 개발을 주요 연구로 설명한다.[^dept] 여러 물리 현상을 함께 다루는 멀티피직스와 여러 크기 수준을 연결하는 멀티스케일 시뮬레이션도 연구한다.[^dept] 시뮬레이션은 대상의 작동이나 변화를 모형으로 재현하는 일이다.

첫째 축은 해석 방법 자체의 개발이다. 연구실은 고체와 구조물의 거동을 지배방정식(현상의 변화와 관계를 나타내는 수학식)의 수치 계산으로 예측하는 전산역학을 다룬다.[^dept] 대상을 작은 구역으로 나누어 계산하는 유한요소법과, 구역을 잇는 고정된 격자 없이 흩어진 계산점을 이용하는 무요소법을 개발하고 결합한다.[^dept][^research] 페리다이나믹스는 한 점과 일정 거리 안의 다른 점들 사이 상호작용으로 변형과 파괴를 계산하는 비국소(한 점의 반응이 일정 거리 안 여러 점의 상태에 함께 달린) 역학 방법이다. 균열이 생긴 곳처럼 물체가 연속적이지 않은 영역을 다루고, 서로 다른 방법으로 계산한 영역의 변위(기준 위치에서 움직인 거리와 방향)가 연결되도록 만드는 것이 연구 문제다.[^research]

둘째 축은 재난과 큰 외력에 대한 구조물 안전이다. 하중(물체나 구조물에 작용하는 외부 힘)으로 인한 파괴를 예측하려고, 철근콘크리트의 손상 모형과 담장의 지진 거동을 분석한다.[^p2][^p3] 최근 연구에서는 손상 모형의 조절값이 같지 않으면 비슷하게 휘어진 구조물도 서로 다른 파괴 양상을 보일 수 있음을 설명했고, 담장 윗부분의 지지 유무를 고려한 내진 설계(구조물이 지진에 견디도록 하는 설계) 기준을 제안했다.[^p2][^p3] 토석류(물과 흙·돌이 섞여 흘러내리는 현상)가 송전탑에 부딪힐 때에는 흐르는 물질과 고체 구조물을 함께 계산해 손상이 집중되는 부분과 순차적인 파괴를 분석했다.[^p4]

셋째 축은 재료 구조와 파동·유동이다. 연구실은 재료의 소성과 균열을 해석하고 고성능 자연모사 복합재료를 개발하며, 입체적인 광학 나노복합구조의 거동을 연구한다.[^dept] 나노복합구조는 나노미터 단위의 구성 부분을 포함하는 복합 구조이고, 나노미터는 십억분의 일 미터다. 진주층(조개껍데기 안쪽의 겹겹이 쌓인 층)을 본뜬 적층 구조의 충격 반응과, 압축하면 빛의 통과 정도가 바뀌는 입체 재료가 연구 사례다.[^p5][^p6] 또한 파동(진동이나 교란이 공간으로 전달되는 현상)의 전파를 계산하고, 유체(흐를 수 있는 액체와 기체)가 구조물에 주는 힘과 해일의 전파를 다룬다.[^research][^p7][^p8]

## 주요 연구 주제

### 1. 균열을 다루는 수치해석 방법

유한요소법·무요소법·페리다이나믹스를 개발하고 결합한다. 연구 소개는 연결 영역에서 변위와 그 변화가 연속되게 만드는 문제를 설명한다. 대표 논문 1은 물체를 구획으로 나눈 격자 모형과 유한요소법을 연결하고, 탄성(힘을 없애면 본래 상태로 돌아가려는 변형 성질) 거동부터 파괴까지 계산한 결과를 이론·실험 등과 대조한다.[^research][^p1]

### 2. 충격·폭발·지진과 구조물의 파괴

연구실은 구조물이 충격과 폭발, 지진을 받을 때의 반응과 점진적 붕괴를 연구 주제로 든다.[^research] 대표 논문 2–4는 손상 모형의 조절값, 담장의 지지 조건, 토석류와 송전탑의 상호작용이 구조물의 파괴에 주는 영향을 다룬다.[^p2][^p3][^p4]

### 3. 자연모사 복합재료와 빛의 통과를 조절하는 구조

자연모사 복합재료의 개발과 입체 광학 나노복합구조의 거동을 연구한다.[^dept] 대표 논문 5는 진주층을 본뜬 구조에서 판 모양 구성 부분의 크기를 불규칙하게 바꾸고 충격 반응을 계산한다.[^p5] 대표 논문 6은 기공(재료 내부의 빈 공간)이 기울어진 방향으로 놓인 구조를 두께 방향으로 눌러 빛의 통과를 조절한다.[^p6]

### 4. 파동과 유체가 구조물에 주는 힘

연구 소개는 판을 따라 전달되는 램파와 비선형 파동의 계산, 부서지는 물결의 계산을 주요 주제로 든다. 비선형은 원인과 결과가 단순한 비례 관계로 표현되지 않는 성질이다. 대표 논문 7은 앞선 해일 계산에서 얻은 흐름 정보를 다음 계산의 경계조건(계산 영역의 가장자리에서 지정하는 물리량이나 관계)으로 넘긴다. 대표 논문 8은 두 분사 흐름이 서로 간섭하면서 벽 표면에 주는 전단응력(표면과 나란한 힘을 단위 면적으로 나눈 값)이 달라지는 원리를 분석한다.[^research][^p7][^p8]

## 대표 논문

홍정욱 교수가 저자로 참여한 KAIST 재직 시기의 2021–2026년 논문 중 해석 방법, 구조물 안전, 재료, 유동 연구를 고르게 보여 주는 8편이다. 마지막 저자와 공동 교신저자 논문을 우선하고 해일 계산 갈래도 함께 담았다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 연도와 게재 승인 표시는 연구실 목록을 따른다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [Compatible coupling of discrete elements and finite elements using Delaunay–Voronoi dual tessellations](https://doi.org/10.1007/s40571-022-00473-x) · Computational Particle Mechanics | 물체를 격자 모형으로 계산한 영역과 유한요소로 계산한 영역을, 서로 대응하는 두 공간 분할의 기하 관계를 이용해 연결했다. 연결을 위한 별도 요소 없이 두 영역을 구분하고, 유한요소의 변형 계산을 구역 경계에 맞춰 다듬었다. 탄성, 형상이 크게 바뀌는 거동, 파괴를 계산한 결과가 이론·수치·실험 결과와 잘 맞았다.[^p1] | 1저자 Young Kwang Hwang, 마지막 저자 홍정욱 |
| 2 | 2026 | [Sensitivity of blast responses in a reinforced concrete slab to damage evolution parameters](https://doi.org/10.1007/s00466-026-02836-0) · Computational Mechanics (게재 승인) | 폭발을 받는 철근콘크리트 판의 손상이 진행되는 방식을 조절할 수 있도록 기존 재료 모형을 확장하는 프로그램을 개발했다. 실험의 휨과 균열 양상으로 계산을 검증하고, 손상의 진행 속도·형태·한계와 계산 요소 제거 기준이 주는 영향을 분석했다. 최대 휨이 비슷하더라도 반응이 가장 커지는 시점과 파괴 양상이 달라질 수 있어, 휨 하나만으로 구조물 거동을 설명하기 어렵다고 밝혔다.[^p2] | 1저자 Dawon Park, 마지막 저자 홍정욱 |
| 3 | 2025 | [Geometric Limits for the Seismic Design of Unreinforced Masonry Fence Walls](https://doi.org/10.1002/eqe.70070) · Earthquake Engineering & Structural Dynamics | 벽돌이나 블록을 쌓은 담장은 윗부분이 구속되지 않아 건물의 구조벽과 지지 조건이 다르다는 점에서 출발했다. 흔들림을 가하는 진동대 시험과 비교해 계산 모형을 검증한 뒤, 길이·높이·지지 조건을 바꾸어 지진 성능을 분석했다. 담장의 높이와 길이를 두께에 대해 어느 범위로 제한할지 제안해 담장에 맞는 내진 설계 기준을 마련하고자 했다.[^p3] | 1저자 Youngjun Choi, 마지막 저자 홍정욱 |
| 4 | 2025 | [Failure analysis of a transmission tower by non-Newtonian debris flow impact with user-defined SPH particles and finite elements](https://doi.org/10.1016/j.rineng.2025.107183) · Results in Engineering | 토석류를 계산 입자의 움직임으로 표현하는 평활입자유체역학과 송전탑을 나타내는 유한요소법을 결합했다. 평활입자유체역학은 주변 입자의 정보를 매끈하게 평균하여 흐름을 계산하는 방법이며 SPH는 Smoothed Particle Hydrodynamics의 줄임말이다. 계산으로 탑 아래쪽 부재에 힘이 집중되고 파괴가 순차적으로 진행되는 원리를 살폈고, 토석류의 부피가 달라질 때의 손상 한계를 분석했다.[^p4] | 1저자 Dawon Park, 마지막 저자 홍정욱 |
| 5 | 2022 | [Numerical Study on Impact Resistance of Nonuniform Nacre-patterned Multi-layer Structures](https://doi.org/10.7734/coseik.2022.35.4.215) · Journal of Computational Structural Engineering Institute of Korea | 진주층을 본뜬 여러 겹의 구조에서 판 모양 구성 부분의 평면 면적을 무작위로 바꾸는 절차를 개발했다. 이 구조에 추를 떨어뜨리는 충격을 계산하고, 흡수한 에너지의 비율과 내부 힘의 분포, 시간에 따른 충격력을 분석했다. 에너지는 일을 하거나 변화를 일으킬 수 있는 물리량이다. 구조의 불규칙성이 충격 반응에 주는 영향을 밝혀 진주층 모사 구조를 설계하는 데 활용하고자 했다.[^p5] | 1저자 Tae Hee Lee, 마지막 저자 홍정욱 |
| 6 | 2024 | [Compression-sensitive smart windows: inclined pores for dynamic transparency changes](https://doi.org/10.1038/s41467-024-52305-6) · Nature Communications | 갑오징어에서 착안해 기울어진 기공이 있는 입체 구조를 만들었다. 옆으로 늘리는 대신 두께 방향으로 눌러 기공을 여닫기 때문에, 창의 가로·세로 크기에 따라 필요한 작동 공간이 함께 커지는 문제를 피하려 했다. 누르지 않았을 때는 불투명하고 누르면 투명해지는 방식으로 빛의 통과를 조절하며, 기공의 기울기가 압축에 대한 민감도를 높인다고 설명한다.[^p6] | 1저자 Haomin Chen, 홍정욱 공동 교신저자(연구실 표기)[^pubs] |
| 7 | 2024 | [An offline coupling approach for efficient SPH simulations of long-distance tsunami events using wave source boundary condition](https://doi.org/10.1016/j.advengsoft.2024.103632) · Advances in Engineering Software | 해일이 먼 거리를 이동해 연안 구조물에 닿는 과정을 하나의 큰 영역에서 모두 계산하는 대신, 앞선 계산의 흐름 정보를 다음 부분 영역 계산으로 전달하는 경계조건을 제안했다. 댐이 무너져 물이 흐르는 모의로 검증하고, 해일 실험을 전체 영역과 부분 영역으로 각각 계산해 비교했다. 두 계산에서 물결 모양과 구조물에 가해지는 힘 등이 잘 맞았다. 관심 영역으로 계산 범위를 줄이면서 상세한 유체·구조 상호작용을 다룰 수 있음을 보였다.[^p7] | 1저자 Young Kwang Hwang, 저자 홍정욱 |
| 8 | 2026 | [Physical similarity and scaling laws for ground shear stress in circular twin-jet impingement flow](https://doi.org/10.1063/5.0342742) · Physics of Fluids | 두 분사 흐름이 바닥에 부딪힐 때 표면을 나란히 미는 힘이 어떻게 바뀌는지 수치 계산했다. 실험 자료와 비교한 모형으로 분사구 사이 거리와 높이의 영향을 분석했다. 각각의 분사 흐름이 우세한 상태에서 서로 만난 흐름이 위로 솟는 상태로 바뀌는 것이 힘의 변화와 연결되며, 조사한 조건 안에서 속도와 표면 힘의 관계를 설명하는 규칙을 제시했다.[^p8] | 1저자 Homin Kim, 마지막 저자 홍정욱 |

## 교수와 전문 분야

홍정욱 교수는 1994년 연세대학교 토목공학과 학사, 1996년 KAIST 토목공학과 석사, 2004년 MIT 토목 및 환경공학 박사 학위를 받았다. 2008–2012년 Michigan State University 조교수를 지냈고, 2012년 KAIST에 부교수로 부임했으며 2020년부터 교수로 재직한다.[^dept][^professor] 연구실 구성원 소개는 AAML 책임자, 재난과학기술연구소 소장, Advances in Engineering Software 편집장으로 적는다.[^people]

학과가 밝힌 전문 분야는 멀티스케일 시뮬레이션, 멀티피직스, 전산역학, 유한요소법·무요소법, 소성재료, 극한 하중에서의 구조물 해석, 생체역학과 구조물 안전진단이다.[^dept] 대표 논문에서 확인되는 전문성은 서로 다른 수치해석 방법을 연결하는 계산 기술, 재난 하중을 받는 구조물의 손상 예측, 재료의 기하 구조를 이용한 기능 설계로 묶을 수 있다. 이는 논문의 연구 대상을 바탕으로 정리한 것이다.[^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

학과 소개는 국가안보, 사회기반시설, 구조물 안전진단을 응용 대상으로 든다.[^dept] 대표 논문은 폭발에 대한 철근콘크리트 구조물 안전 평가, 지진에 견디는 담장 설계, 토석류를 받는 송전탑 평가, 연안 구조물이 받는 해일 하중 계산, 빛의 통과를 조절하는 창문용 재료를 다룬다.[^p2][^p3][^p4][^p6][^p7]

## 구성원

2026년 11월 6일 연구실 People 페이지의 박사후연구원 3명, 박사과정 6명, 석사과정 4명이다. 과정은 게시 표기를 옮겼다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Dawon Park | 박사후연구원 | 2, 3, 4 |
| Yongwoo Kim | 박사후연구원 |  |
| Sung-Wuk Hong | 박사후연구원 |  |
| Seong Eun Oh | 박사과정 |  |
| Sunwoo Kim | 박사과정 | 3 |
| Tae Hee Lee | 박사과정 | 5, 6 |
| Homin Kim | 박사과정 | 8 |
| Yena Lee | 박사과정 |  |
| Minji Kim | 박사과정 |  |
| Hongwon Lee | 석사과정 |  |
| Yunmin Kim | 석사과정 |  |
| Minsu Lee | 석사과정 |  |
| Jaehee Kim | 석사과정 |  |

## 졸업생과 이전 구성원

연구실 People의 Alumni에 실린 36명이다. 학위·과정과 소속·기간은 게시 표기이며, 현재 구성원과 이름이 같은 항목도 학위·기간 표기대로 담았다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| SangHoon Kim | M.S., KAIST (2024-2026) |  |
| Dawon Park | M.S. & Ph.D., KAIST (2019-2025) ) |  |
| Kyung Bo Lee | Ph.D., KAIST (2021-2025) |  |
| Minji Kim | M.S., KAIST (2023-2025) ) |  |
| M. Seddiq Eskandari Nasab | Postdoctoral Researcher, KAIST (2024-2026) |  |
| Dong-Hun Han | M.S., KAIST (2023-2024) |  |
| Woo-Min Jang | M.S., KAIST (2022-2024) |  |
| Mujong Kim | Ph.D., KAIST (2020-2024) |  |
| Yena Lee | M.S., KAIST (2022-2024) |  |
| Youngjun Choi | M.S. & Ph.D., KAIST (2017-2024) |  |
| Tae Hee Lee | M.S. KAIST (2021-2023) |  |
| Sunwoo Kim | M.S. KAIST (2020-2022) |  |
| Suyeong Jin | M.S. & Ph.D., KAIST (2016-2022／ Postdoc 2022-2025) |  |
| Kwonhwan Ko | M.S. & Ph.D., KAIST (2015-2022) |  |
| Sangmin Lee | M.S. & Ph.D., KAIST (2015-2022) |  |
| Young Kwang Hwang | Postdoctoral Researcher, KAIST (2020-2021) |  |
| Heung Woon Jang | Integrated M.S.-Ph.D., KAIST (2014-2021) |  |
| Sangeon Lee | Integrated M.S.-Ph.D., KAIST (2014-2020) |  |
| Jae-Wook Jung | M.S. & Ph.D., KAIST (2012-2020) |  |
| Dias Bakhtiyarov | M.S. KAIST (2015-2017) |  |
| Furqan Ahmad | Postdoctoral Researcher, KAIST (2014-2016) |  |
| Jooeun Lee | Ph.D., KAIST (2013-2016) |  |
| Aleem Ullah | M.S., KAIST (2013-2015) |  |
| Yang Sun You | M.S., KAIST (2013-2015) |  |
| Seung Jin Yang | M.S., KAIST (2013-2015) |  |
| Young Woo Ko | M.S., KAIST (2013-2015) |  |
| Hee Kun Ju | M.S., KAIST (2013-2015) |  |
| Yeon Wook Jung | M.S., KAIST (2012-2014) |  |
| Hyeong Uk Lim | M.S., KAIST (2012-2014) |  |
| Kyoung Soo Lee | Research Professor, KAIST (2012-2013) |  |
| Binh Huy Nguyen | KAIST (2012) |  |
| Jungsil Kim | Postdoctoral Research Associate, MSU |  |
| Wenyang Liu | Ph.D., MSU |  |
| Jingjun Shen | M.S., MSU |  |
| Lassaad Mhamdi | M.S., co-advised with Dr. Lajnef, MSU |  |
| Corbin St. Aubun | B.S., MSU |  |

## 최근 논문과 발표 목록 (2021–2026)

연구실 Publications의 학술지 54편, 학회 논문집 4편과 Presentations의 발표 74건이다. 각 줄의 대괄호로 구획을 구분했다. 연도·저자·제목·발표처는 연구실 표기이며, 학술지 목록의 Accepted는 「게재 승인」으로 표시했다. 발표 목록의 날짜는 연구실 기재 날짜다. 학회 논문집과 발표 기록은 같은 제목이어도 각 구획의 기록으로 구분한다.[^pubs][^presentations]

**2026**

- [학술지] Y. Lee, T.H. Lee, and J.W. Hong, Data-Driven Parameter Optimization for Shape-Dependent Blast Load Prediction in ALE Simulations, Computers and Structures, 게재 승인, 2026.
- [학술지] H. Kim, S. Kim, S. Lee, and J.W. Hong, Viscous Scaling Laws for Wall Shear Stress in Asymmetric Twin-Jet Impingement, International Journal of Heat and Fluid Flow, 122:110747, 2026. DOI: https://doi.org/10.1016/j.ijheatfluidflow.2026.110747
- [학술지] S. Jin, J.W. Hong, and A.F. Fonseca, Geometry-Dependent Crack Interaction and Toughening in Graphene, Journal of Materials Research, 게재 승인, 2026.
- [학술지] D. Park, M. Kim, S. Kim, H. Lee, S. Jin, and J.W. Hong, Multi-Metric Optimization of Mohr–Coulomb Parameters in SPH Granular Flow Simulation, Engineering Geology, 게재 승인, 2026.
- [학술지] D. Park, Y. Kim, H. Lee, and J.W. Hong, Novel Detonation-Location Mapping Method for Blast Damage Assessment with Application to a 2D Concrete Slab, Structures, 94:113216, 2026. DOI: https://doi.org/10.1016/j.istruc.2026.113216
- [학술지] S. Jin, S. Kim, and J.W. Hong, Adaptive Finite Element–peridynamics Coupling for Crack Initiation and Propagation in Brittle 3D Solids, Engineering Fracture Mechanics, 347:112674, 2026. DOI: https://doi.org/10.1016/j.engfracmech.2026.112674
- [학술지] T. H. Lee, Y. Lee, D. Park, Y. Choi, and J.W. Hong, ALE Simulation and Machine Learning Surrogate Modeling of Airborne Blast Loading from Cuboid Explosives, Advances in Engineering Software, 223:104315, 2026. DOI: https://doi.org/10.1016/j.advengsoft.2026.104315
- [학술지] D. Park and J.W. Hong, Sensitivity of Blast Responses in a Reinforced Concrete Slab to Damage Evolution Parameters, Computational Mechanics, 게재 승인, 2026. DOI: https://doi.org/10.1007/s00466-026-02836-0
- [학술지] H. Kim, J. Park, J.W. Hong, and S. Lee, Large-eddy simulation of turbulent flow and coherent structures over rotated random-height building arrays, Physics of Fluids, 38:075167, 2026. DOI: https://doi.org/10.1063/5.0338303
- [학술지] H. Kim, S. Kim, S. Lee, and J.W. Hong, Physical Similarity and Scaling Laws for Ground Shear Stress in Circular Twin-Jet Impingement Flow, Physics of Fluids, 38:075157, 2026. DOI: https://doi.org/10.1063/5.0342742
- [학술지] S. Jin, J.W. Hong, and A.F. Fonseca, Effect of Interatomic Potential Choice on Fracture Modes of Graphene with Parallel Cracks, MRS Advances, 11:1374-1380, 2026. DOI: https://doi.org/10.1557/s43580-026-01682-9
- [학술지] S. Kim, H. Kim, S. Lee, and J.W. Hong, Physics-Guided Residual Learning for Predicting Aerodynamic Characteristics of 3D Wing under Diverse Operating Conditions, Aerospace Science and Technology, 176:112606, 2026. DOI: https://doi.org/10.1016/j.ast.2026.112606
- [학술지] D. Park, H. Kim, M. Kim, and J.W. Hong, AI Surrogate Model for Debris Flow Impact on a Transmission Tower Using SPH-FEM Simulations, Computers and Structures, 328:108260, 2026. DOI: https://doi.org/10.1016/j.compstruc.2026.108260
- [학술지] D. Park, S. Kim, H. Lee, and J.W. Hong, Experimental Assessment of the Dynamic Characteristics of Masonry Walls Under Incremental Shake-Table Loading, Journal of Building Engineering, 125:116165, 2026. DOI: https://doi.org/10.1016/j.jobe.2026.116165
- [학술지] D. Park, T.H. Lee, Y. Lee, and J.W. Hong, Numerical Study of RC Slab Failure Mechanisms Under Varying Blast Loads, Journal of Building Engineering, 120:115435, 2026. DOI: https://doi.org/10.1016/j.jobe.2026.115435
- [학술지] T.H. Lee, M. Kim, Y. Lee, S. Lee, and J.W. Hong, Effects of Impact Loadings on a Submerged Floating Tunnel: Experimental and Numerical Investigations, Marine Structures, 107:104015, 2026. DOI: https://doi.org/10.1016/j.marstruc.2026.104015
- [학술지] S. Kim, S. Jin, and J.W. Hong, Numerical Simulation of Heat Transfer Across Partial Discontinuities Using the Peridynamic Differential Operator, Computer Methods in Applied Mechanics and Engineering, 452:118749, 2026. DOI: https://doi.org/10.1016/j.cma.2026.118749
- [학술지] H. Kim, T.H. Lee, S. Kim, S. Lee, and J.W. Hong, Regression Analysis of Heat Transfer in Twin Slot Jet Impingement with Computational Fluid Dynamics and Machine Learning Techniques, International Journal of Heat and Fluid Flow, 118:110220, 2026. DOI: https://doi.org/10.1016/j.ijheatfluidflow.2025.110220
- [학술지] K.B. Lee, T.H. Lee, Y. Lee, and J.W. Hong, Numerical Study of Explosive–Soil Contact Angle Effects on Blast Pressure and Crater Morphology with TNT and Aluminized Explosives, Advances in Engineering Software, 213:104085, 2026. DOI: https://doi.org/10.1016/j.advengsoft.2025.104085
- [학회 발표] T.H. Lee, Y. Lee, D. Park and J.W. Hong, Numerical Simulation and Response Prediction of Structures under Blast Loads Using Data-Driven Approaches, KSCE 2026 Convention, Jeongseon, Korea, 23 October 2026.
- [학회 발표] H. Lee, T.H. Lee, E.S. Im, and J.W. Hong, Numerical Analysis of the Overtopping Failure Mechanism in Earth Dams Using the Adaptive SPH Method, KSCE 2026 Convention, Jeongseon, Korea, 23 October, 2026.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Ellipsoidal Kinematic Reconstruction for the Neighborhood Deformation Tracking in Nonlocal Analyses, The Thirteenth International Conference on Engineering Computational Technology (ECT 2026), Budapest, Hungary, 28 August 2026.
- [학회 발표] J.W. Hong, A Journey Through Meshless Methods for Solids and Fluids, 17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS 2026), Munich, Germany, 23 July 2026. (Plenary lecture)
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Heat Conduction Analysis Using a Nonlocal Gradient Operator, 17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS 2026), Munich, Germany, 22 July 2026.
- [학회 발표] S. Jin, S. Kim, and J.W. Hong, Adaptive Coupling of Peridynamics and Finite Element Method for Crack Propagation, 17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS 2026), Munich, Germany, 22 July 2026.
- [학회 발표] H. Kim, S. Kim, T.H. Lee, and J.W. Hong, Hybrid CFD-Machine Learning Framework for Three-Dimensional Flow Quantification in Twin-Slot Jet Impingement, 17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS 2026), Munich, Germany, 21 July 2026.
- [학회 발표] T.H. Lee, H. Kim, Y. Lee, S. Kim, and J.W. Hong, Fluid-Structure Interaction Analysis for Low-Frequency Heavyweight Floor Impact Sound, 17th World Congress on Computational Mechanics and 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS 2026), Munich, Germany, 21 July 2026.
- [학회 발표] S. Kim, H. Kim and J.W. Hong, Numerical Validation of 3D Wing Aerodynamic Characteristics Using ONERA M6 Experimental Data, KSCM Conference 2026, Daejeon, Korea, 11 February 2026. (Poster)
- [학회 발표] H. Lee, D. Park, and J.W. Hong, Optimization-driven Failure Analysis of Concrete Cylinders under Compression Using the Continuous Surface Cap Model, KSCM Conference 2026, Daejeon, Korea, 11 February 2026. (Poster)
- [학회 발표] Y. Kim, D. Park and J.W. Hong, Location-Dependent Damage Mapping and Fragility Analysis for Enhanced Blast Safety Assessment of 2D Concrete Slab, KSCM Conference 2026, Daejeon, Korea, 11 February 2026. (Poster)

**2025**

- [학술지] S. Jin, J.W. Hong, C. Daraio, and A.F. Fonseca, Abnormal Crack Coalescence and Ductility in Graphene, International Journal of Mechanical Sciences, 309:111025, 2025. DOI: https://doi.org/10.1016/j.ijmecsci.2025.111025
- [학술지] M.S. Eskandari Nasab and J.W. Hong, Quantile-Based Recursive Non-Additive Multi-Fidelity Emulator with Application to Seismic Response Prediction, Engineering Structures, 346:121618, 2025. DOI: https://doi.org/10.1016/j.engstruct.2025.121618
- [학술지] Y. Choi, D. Park, S. Kim, and J.W. Hong, Geometric Limits for the Seismic Design of Unreinforced Masonry Fence Walls, Earthquake Engineering & Structural Dynamics, 55:130-149, 2025. DOI: https://doi.org/10.1002/eqe.70070
- [학술지] D. Park, Y.K. Hwang, S. Jin, and J.W. Hong, Optimization of Rate-Dependent Material Parameters for Accurate Blast Response Prediction in Reinforced Concrete Slabs, Computers and Structures, 318:107961, 2025. DOI: https://doi.org/10.1016/j.compstruc.2025.107961
- [학술지] D. Park, W.M. Jang, E. Cheon, and J.W. Hong, Failure Analysis of a Transmission Tower by Non-Newtonian Debris Flow Impact with User-Defined SPH Particles and Finite Elements, Results in Engineering, 28:107183, 2025. DOI: https://doi.org/10.1016/j.rineng.2025.107183
- [학술지] D. Park, M. Kim, and J.W. Hong, Sequential Failure-Based Fragility Assessment of a Transmission Tower Under Debris Flows, Engineering Structures, 343:121097, 2025. DOI: https://doi.org/10.1016/j.engstruct.2025.121097
- [학술지] S. Jin, G. Kim, S. Lee, K. Subramanian, J.W. Hong, and C. Daraio, Thermo-mechanical behavior of three-phase shape memory polymers for a wide temperature change, Mechanics of Materials, 209:105409, 2025. DOI: https://doi.org/10.1016/j.mechmat.2025.105409
- [학술지] M.S. Eskandari Nasab, M. Bafandegan, and J.W. Hong, Numerical Evaluation of an Innovative Hybrid Seismic Control System with Amplified Energy Dissipation, Advances in Engineering Software, 204:103898, 2025. DOI: https://doi.org/10.1016/j.advengsoft.2025.103898
- [학술지] H. Kim, D.H. Han, T.H. Lee, and J.W. Hong, An Application of Machine Learning for Geometric Optimization of a Dual-Throat Bent Nozzle, Advances in Engineering Software, 202:103869, 2025. DOI: https://doi.org/10.1016/j.advengsoft.2025.103869
- [학술지] D. Park, S. Kim, S. Jin, Y. Choi, H. Kim, and J.W. Hong, Seismic Vulnerability Assessment of Leaning U-shaped Masonry Fence Walls, Earthquake Spectra, 41:2177-2202, 2025. DOI: https://doi.org/10.1177/87552930251320413
- [학술지] H. Kim, D.H. Han, S. Jin, and J.W. Hong, Computational Fluid Dynamics Simulations of a Novel Dual Throat Bent Nozzle, International Journal of Aeronautical and Space Sciences, 26:1415–1426, 2025. DOI: https://doi.org/10.1007/s42405-024-00849-8
- [학회 논문집] T.H. Lee, Y. Lee, and J.W. Hong, Random Forest-Based Surrogate Modeling of Blast Parameters from Cuboid Charges, Proceedings of the Eighteenth International Conference on Civil, Structural and Environmental Engineering Computing, 2025.
- [학회 발표] J.W. Hong, Recent Developments in Peridynamics for Computational Mechanics, Asian Pacific Congress on Computational Mechanics (APCOM2025), Brisbane, Australia, 9 December 2025. (Semi-plenary talk).
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Quasistatic Thermomechanical Simulation with Peridynamics, Asian Pacific Congress on Computational Mechanics (APCOM2025), Brisbane, Australia, 8 December 2025.
- [학회 발표] S. Kim, H. Kim, and J.W. Hong, Numerical Evaluation of Aerodynamic Characteristics for the NACA 2412 Airfoil, The Thirty-sixth KKHTCNN Symposium on Civil Engineering, Hong Kong, China, 4 December 2025.
- [학회 발표] H. Lee, D. Park, and J.W. Hong, Parametric Study on Cylindrical Concrete Compression Using the Continuous Surface Cap Model, The Thirty-sixth KKHTCNN Symposium on Civil Engineering, Hong Kong, China, 4 December 2025.
- [학회 발표] Y. Kim, T.H. Lee, and J.W. Hong, Numerical Study on Blast Effects of Dynamic TNT Charges Using ALE Method, The Thirty-sixth KKHTCNN Symposium on Civil Engineering, Hong Kong, China, 4 December 2025.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Fully-coupled Thermomechanical Simulations Using Peridynamics, COSEIK Academic Symposium, Daejeon, Korea, 28 November 2025.
- [학회 발표] D. Park, T.H. Lee, and J.W. Hong, Blast Damage Mechanism of RC Slabs Using the Continuous Surface Cap Model (CSCM), KSCE 2025 Convention, Osong, Korea, 14 November 2025.
- [학회 발표] T.H. Lee, Y. Lee, and J.W. Hong, Automated System for Blast Response Evaluation of Nuclear Containment Buildings, 2025 KNS Fall Conference, Changwon, Korea, 30 October 2025.
- [학회 발표] H. Kim, D.H. Han, S. Kim, and J.W. Hong, Numerical Investigation of Ground Effect for a VTOL Aircraft, APISAT 2025, Seoul, Korea, 29 October 2025.
- [학회 발표] S. Kim, H. Kim, and J.W. Hong, Thrust Based PID Attitude Control Algorithm For Vertical Take-Off and Landing(VTOL) Aircraft, APISAT 2025, Seoul, Korea, 28 October 2025. (Poster).
- [학회 발표] J.W. Hong, The New Horizon of Peridynamics, International Workshop on Multiscale, Multiphysics, and Multidisciplinary Research on Materials and Structures (m3MS), Singapore, 26 September 2025. (Invited keynote).
- [학회 발표] T.H. Lee, Y. Lee, and J.W. Hong, Random Forest-Based Surrogate Modeling of Blast Parameters from Cuboid Charges, The 18th International Conference on Civil, Structural and Environmental Engineering Computing, Sardinia, Italy, 28 August 2025.
- [학회 발표] S. Jin, S. Kim, and J.W. Hong, Adaptive coupling of peridynamics and finite element method for efficient fracture simulation, 18th U.S. National Congress on Computational Mechanics (USNCCM18), Chicago, USA, 22 July 2025
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Stabilization of Peridynamic Differential Operators Through Diagonal Scaling Preconditioning, The 4th International Conference on COMPSAFE2025, Kobe, Japan, 4 July 2025.
- [학회 발표] T.H. Lee, D. Park, Y. Lee, and J.W. Hong, Machine Learning-Based Surrogate Modeling of Blast Parameters for Cuboid Explosive Charges, The 4th International Conference on COMPSAFE2025, Kobe, Japan, 3 July 2025.
- [학회 발표] J.W. Hong, Recent Advances in Nonlocal Methods for Computational Mechanics, COMPSAFE2025, Kobe, Japan, 3 July 2025. (Plenary talk).
- [학회 발표] M. Kim, D. Park, and J.W. Hong, Simulations of Debris Flow Impact on a Transmission Tower Reinforced with a Wire System, COSEIK Academic Symposium, Busan, Korea, 4 April 2025.

**2024**

- [학술지] T.H. Lee, K. Ko, and J.W. Hong, A Novel Advanced Block Assembly Method with 3D Printed Channel Systems, Composite Structures, 118584, 2024. DOI: https://doi.org/10.1016/j.compstruct.2024.118584
- [학술지] D. Park, T.H. Lee, Y. Lee, Y. Choi, and J.W. Hong, Blast Simulations of a Reinforced Concrete Slab Using the Continuous Surface Cap Model (CSCM), Journal of Building Engineering, 96:110603, 2024. DOI: https://doi.org/10.1016/j.jobe.2024.110603
- [학술지] H. Chen, G. Chang, T.H. Lee, S. Min, S. Nam, D. Cho, K. Ko, G. Bae, Y. Lee, J. Feng, H. Zhang, J. Kim, J. Shin, J.W. Hong, S. Jeon, Compression-Sensitive Smart Windows: Inclined Pores for Dynamic Transparency Changes, Nature Communications, 15, 8074, 2024. (Co-corresponding author). DOI: https://doi.org/10.1038/s41467-024-52305-6
- [학술지] S. Jin, S. Kim, and J.W. Hong, Parallelized Plastic Coupling of Non-ordinary State-based Peridynamics and Finite Element Method, Advances in Engineering Software, 196:103718, 2024. DOI: https://doi.org/10.1016/j.advengsoft.2024.103718
- [학술지] Y.K. Hwang, S. Jin, J.W. Hong, and I. Sohn, An Offline Coupling Approach for Efficient SPH Simulations of Long-distance Tsunami Events Using Wave Source Boundary Condition, Advances in Engineering Software, 192:103632, 2024. DOI: https://doi.org/10.1016/j.advengsoft.2024.103632
- [학술지] J. Lee, S.E. Lee, S. Jin, H. Sohn, and J.W. Hong, An Application of Machine Learning for Material Crack Diagnosis Using Nonlinear Ultrasonics, Mechanical Systems and Signal Processing, 214:111371, 2024. DOI: https://doi.org/10.1016/j.ymssp.2024.111371
- [학술지] H. Kim, Y. Choi, D. Park, M.K. Lee, G.J. Lee, B.H. Kim, and J.W. Hong, Numerical Evaluation of Acoustic Emission (AE) Sensors by Lead-Zirconate-Titanate (PZT) Geometric Design, Sensors and Actuators A: Physical, 366:115031, 2024. DOI: https://doi.org/10.1016/j.sna.2024.115031
- [학회 논문집] S. Kim, S. Jin, and J.W. Hong, Performance Evaluation of Iterative Solvers for Vectorized Quasi-Static Heat Conduction in Peridynamics, Proceedings of the Fifteenth International Conference on Computational Structures Technology, 2024.
- [학회 논문집] T.H. Lee, D. Park, Y. Choi, Y. Lee, and J.W. Hong, Blast Responses of a Reinforced Concrete Slab Using the Arbitrary Lagrangian-Eulerian Method, Proceedings of the Fifteenth International Conference on Computational Structures Technology, 2024.
- [학회 논문집] H. Kim, D.H. Han, S. Jin, and J.W. Hong, Numerical Study of a Dual Throat Bent Nozzle Using Computational Fluid Dynamics, AIAA Aviation Forum and Ascend 2024, AIAA Paper 2024-4118, 2024.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Preconditioning Method for Enhancing the Stability of Peridynamic Differential Operators, KSCM Conference 2024, Seoul, Korea, 9 December 2024. (Poster).
- [학회 발표] T.H. Lee, D. Park, Y. Lee, and J.W. Hong, Machine Learning-Based Surrogate Model for Predicting Blast Parameters from Cuboid Charge, KSCM Conference 2024, Seoul, Korea, 9 December 2024. (Poster).
- [학회 발표] H. Kim, D.H. Han, and J.W. Hong, Heat Transfer Analysis of Twin-Jet Impingement on the Ground Surface using Computational Fluid Dynamics, KSCM Conference 2024, Seoul, Korea, 9 December 2024. (Poster).
- [학회 발표] H. Kim, D.H. Han, and J.W. Hong, Development of a High-fidelity Computational Fluid Dynamics Model for Twin-jet Flow Analysis, COSEIK Academic Symposium 2024, Jeonju, Korea, 22 November 2024.
- [학회 발표] D. Park, T.H. Lee, Y. Lee, and J.W. Hong, Failure Analyses of a Reinforced Concrete Slab Under Blast Loading, The Thirty-fifth KKHTCNN Symposium on Civil Engineering, Shanghai, China, 20 November 2024.
- [학회 발표] Y. Lee, T.H. Lee, and J.W. Hong, Numerical Study on Blast Effects for Various Explosive Geometries, The Thirty-fifth KKHTCNN Symposium on Civil Engineering, Shanghai, China, 20 November 2024.
- [학회 발표] M. Kim, D. Park, and J.W. Hong, Finite Element Analyses of a Transmission Tower Subjected to Debris Flow Impact, The Thirty-fifth KKHTCNN Symposium on Civil Engineering, Shanghai, China, 20 November 2024.
- [학회 발표] M. Kim, W.M. Jang, D. Park, and J.W. Hong, Fragility Analyses of Transmission Towers Under Debris Flows, KSCE 2024 Convention, Jeju, Korea, 18 October 2024. (Poster).
- [학회 발표] Y. Lee, T.H. Lee, and J.W. Hong, Numerical Investigation of Blast Pressure on a Steel Plate Using Three-dimensional ALE Method for Different Explosive Geometries, KSCE 2024 Convention, Jeju, Korea, 18 October 2024. (poster).
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Performance Evaluation of Iterative Solvers for Vectorized Quasi-Static Heat Conduction in Peridynamics, The Fifteenth International Conference on Computational Structures Technology (CST), Prague, Czech Republic, 5 September 2024.
- [학회 발표] T.H. Lee, D. Park, Y. Choi, Y. Lee, and J.W. Hong, Blast Responses of a Reinforced Concrete Slab Using the Arbitrary Lagrangian-Eulerian Method, The Fifteenth International Conference on Computational Structures Technology (CST), Prague, Czech Republic, 5 September 2024.
- [학회 발표] H. Kim, D.H. Han, S. Jin, and J.W. Hong, Numerical Study of a Dual Throat Bent Nozzle Using Computational Fluid Dynamics, AIAA Aviation Forum and Ascend 2024, Las Vegas, United States, 31 July 2024.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Performance Evaluation of Iterative Solvers for Vectorized Quasi-Static Heat Conduction in Peridynamics, 16th World Congress on Computational Mechanics and 4th Pan American Congress on Computational Mechanics, Vancouver, Canada, 25 July 2024.

**2023**

- [학술지] Y. Lee, T.H. Lee, D. Park, Y. Choi, and J.W. Hong, Optimal Mesh Size in Three-dimensional Arbitrary Lagrangian-Eulerian Method of Free-air Explosions, Journal of Computational Structural Engineering Institute of Korea, 36:355–364, 2023. DOI: https://doi.org/10.7734/COSEIK.2023.36.6.355
- [학술지] Y. Choi, D. Park, S. Kim, S. Jin, and J.W. Hong, Experimental and Numerical Analyses of Seismic Behaviors of L-shaped Unreinforced Masonry Walls, Engineering Structures, 297:116989, 2023. DOI: https://doi.org/10.1016/j.engstruct.2023.116989
- [학술지] M. Kim, S. Lee, T. H. Lee, and J.W. Hong, Dynamic Transient Analysis of a Submerged Floating Tunnel Under Impact Loading, Ocean Engineering, 287:115913, 2023. DOI: https://doi.org/10.1016/j.oceaneng.2023.115913
- [학술지] S. Jin and J.W. Hong, Convergence Study of Stabilized Non-ordinary State-based Peridynamics for Elastic and Fracture Problems, Engineering Fracture Mechanics, 289:109438, 2023. DOI: https://doi.org/10.1016/j.engfracmech.2023.109438
- [학술지] S. Jin, Y.K. Hwang, and J.W. Hong, Stabilized Non-ordinary State-based Peridynamics with Irregular Nodal Distribution, Mechanics Research Communications, 130:104130, 2023. DOI: https://doi.org/10.1016/j.mechrescom.2023.104130
- [학술지] Y. Choi, D. Park, S. Kim, and J.W. Hong, Investigation on the Behavior Factor of Leaning Masonry Wall Structures, Bulletin of Earthquake Engineering, 21:2987-3009, 2023. DOI: https://doi.org/10.1007/s10518-023-01646-6
- [학회 발표] Y. Lee, T.H. Lee, and J.W. Hong, Investigation of the Free-air Blast Effects by Moving Cylindrical Charges, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 24 November 2023.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Peridynamic Heat Conduction Simulation Using Peridynamic Differential Operators with Parameter Optimization, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 23 November 2023.
- [학회 발표] D. Park, T.H. Lee, Y. Lee, Y. Choi, and J.W. Hong, Numerical Analysis of a Reinforced Concrete Slab Subjected to Blast Loading, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 23 November 2023.
- [학회 발표] T.H. Lee, Y. Lee, and J.W. Hong, Blast Simulation of a Reinforced Concrete Beam Using the Arbitrary Lagrangian-Eulerian Method, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 23 November 2023.
- [학회 발표] W.M. Jang, E. Cheon, and J.W. Hong, Debris Flow Impact Simulation on a Transmission Tower Using the Smoothed Particle Hydrodynamics (SPH) Method, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 23 November 2023
- [학회 발표] D.H. Han, H. Kim, S. Jin, and J.W. Hong, Development of a High-fidelity Nozzle Thrust Analysis Model, The Thirty-fourth KKHTCNN Symposium on Civil Engineering, Pattaya, Thailand, 23 November 2023.
- [학회 발표] H. Kim, D. Park, M.K. Lee, G.J. Lee, B.H. Kim, and J.W. Hong, Numerical Analyses of Piezoelectric Element-based Stacked Accelerometers, COSEIK Academic Symposium, Chuncheon, Korea, 17 November 2023.
- [학회 발표] W.M. Jang, E. Cheon, and J.W. Hong, Debris Flow Simulation Using the Smoothed Particle Hydrodynamics (SPH) Method, COSEIK Academic Symposium, Chuncheon, Korea, 17 November 2023.
- [학회 발표] M. Kim and J.W. Hong, Study on the Dynamic Responses of a Submerged Floating Tunnel Using the Arbitrary Lagrangian Eulerian Description, KSCE 2023 Convention, Yeosu, Korea, 20 October 2023.
- [학회 발표] J.W. Hong, Peridynamics and Beyond, Ulsan National Institute of Science and Technology, Korea, 26 October 2023. (Invited seminar)
- [학회 발표] D. Park, Y. Choi, S. Kim, S. Jin, and J.W. Hong, Numerical Model of a Masonry Wall Subjected to Earthquakes Using the Continuous Surface Cap Model (CSCM), KSCE 2023 Convention, Yeosu, Korea, 20 October 2023.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Parameter Optimization of Peridynamic Differential Operators for Heat Conduction, KSCE 2023 Convention, Yeosu, Korea, 20 October 2023.
- [학회 발표] T.H. Lee, Y. Lee, and J.W. Hong, Blast Simulation of a Reinforced Concrete Beam Using the Three-dimensional ALE Method, KSCE 2023 Convention, Yeosu, Korea, 20 October 2023.
- [학회 발표] S. Jin, and J.W. Hong, Plastic Coupling Model of the Peridynamics and Finite Element Method, KSCM Conference 2023, Gangneung, 30 June, 2023.
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Peridynamic Analysis and Remedy for Boundary Condition Sensitivity in the Quasi-static Heat Transfer, KSCM Conference 2023, Gangneung, 30 June, 2023. (Poster).
- [학회 발표] H. Kim, Y. Choi, D. Park, M.K. Lee, G.J. Lee, B.H. Kim, and J.W. Hong, High-fidelity Finite Element Model for Acoustic Emission Sensors, KSCM Conference 2023, Gangneung, 30 June, 2023. (Poster).
- [학회 발표] Y. Lee, S. Lee, T.H. Lee, and J.W. Hong, Three-dimensional Arbitrary Lagrangian-Eulerian (ALE) Simulations of Free-air Explosions, KSCM Conference 2023, Gangneung, 30 June, 2023. (Poster).
- [학회 발표] S. Kim, S. Jin, and J.W. Hong, Formulation of the Peridynamic Heat Equation Confirming Conservation of Heat Energy from Heat Flux, KSIAM 2023 Spring Conference, PyeongChang, Korea, 20 May 2023.

**2022**

- [학술지] Y. Choi, D. Park, S. Kim, and J.W. Hong, Seismic Performance of Crack-damaged Masonry Wall Structures via Shaking Table Tests, Structures, 45:2272-2291, 2022. DOI: https://doi.org/10.1016/j.istruc.2022.09.120
- [학술지] D. Park, Y. Choi, S. Kim, and J.W. Hong, Failure Analysis of a U-shaped Concrete-block Masonry Wall Structure via Shaking Table Tests, Engineering Failure Analysis, 142:106832, 2022. DOI: https://doi.org/10.1016/j.engfailanal.2022.106832
- [학술지] M. Kim, S. Lee, and J.W. Hong, Empirical Estimation of the Breaker Index Using a Stereo Camera System, Ocean Engineering, 265:112522, 2022. DOI: https://doi.org/10.1016/j.oceaneng.2022.112522
- [학술지] G.J. Kim, S. Lee, M. Kim, H.G. Kwak, and J.W. Hong, Characterization of Single and Dual SFT through a Hydraulic Experiment under Regular and Irregular Waves, Ocean Engineering, 263:112365, 2022. DOI: https://doi.org/10.1016/j.oceaneng.2022.112365
- [학술지] T.H. Lee, K. Ko, and J.W. Hong, Numerical Study on Impact Resistance of Nonuniform Nacre-patterned Multi-layer Structures, Journal of Computational Structural Engineering Institute of Korea, 35:215-226, 2022. DOI: https://doi.org/10.7734/COSEIK.2022.35.4.215
- [학술지] K. Ko, S. Lee, Y.K. Hwang, S. Jin, and J.W. Hong, Investigation on the Impact Resistance of 3D Printed Nacre-like Composites, Thin-walled Structures, 177:109392, 2022. DOI: https://doi.org/10.1016/j.tws.2022.109392
- [학술지] Y.K. Hwang, J.E. Bolander, Y.M. Lim, and J.W. Hong, Compatible Coupling of Discrete Elements and Finite Elements Using Delaunay-Voronoi Dual Tessellations, Computational Particle Mechanics, 9:1351-1365, 2022. DOI: https://doi.org/10.1007/s40571-022-00473-x
- [학술지] Y.K. Hwang, Y.M. Lim, and J.W. Hong, Simulation of Structural Vibrations Using Voronoi-Cell Lattice Models, Journal of Mechanical Science and Technology, 36:647-654, 2022. DOI: https://doi.org/10.1007/s12206-022-0112-z
- [학술지] H. Chen, D. Cho, K. Ko, C. Qin, M. Kim, H. Zhang, J.H. Lee, E. Kim, D. Park, X. Shen, J. Yang, H. Ko, J.W. Hong, J.K. Kim, and S. Jeon, Interdigitated 3D Heterogeneous Nanocomposites for High-Performance Mechanochromic Smart Membranes, ACS Nano, 16:68-77, 2022. (Co-corresponding author). DOI: https://doi.org/10.1021/acsnano.1c06403
- [학회 발표] M. Kim, S. Lee, and J.W. Hong, Dynamic Transient Responses of a Submerged Floating Tunnel Under Impact Loads, COSEIK Academic Symposium, Gangwon, Korea, 24 November 2022.
- [학회 발표] D. Park, Y. Choi, S. Kim, and J.W. Hong, Failure Analysis of a U-shaped Masonry Wall via Shaking Table Tests, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] S. Kim, Y. Choi, D. Park, S. Ok, G. Byun, Y. Kim, and J.W. Hong, Precise Risk Assessment Method for Fire and Explosion in Urban Regeneration Area, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] T.H. Lee, K. Ko, and J.W. Hong, Three-dimensional Voronoi Bi-material Composites for Enhanced Impact Resistance, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] H. Kim, D. Park, Y. Choi, and J.W. Hong, Geometry Optimization of Resonance Acoustic Emission Sensors, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] Y. Lee, S. Lee, and J.W. Hong, Parameter Optimization for the Free-Air Blast Simulation Using an ALE Method, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] W.M. Jang, S. Kim, Y. Choi, D. Park, and J.W. Hong, Signal Filter Design for Acceleration to Measure Displacements of Masonry Walls, The Thirty-third KKHTCNN Symposium on Civil Engineering, Queenstown, Singapore, 17 November 2022.
- [학회 발표] S. Jin, and J.W. Hong, Crack propagation using weighted average stress estimation method of non-ordinary state-based peridynamics, KSME Annual Meeting 2022, Jeju, Korea, 9 November 2022.
- [학회 발표] Jung-Wuk Hong, Recent Developments of Technologies for Urban Disaster Mitigation and Case Studies, Urban Design Institute, 22 October 2022. (Plenary talk).
- [학회 발표] D. Park, Y. Choi, S. Kim, and J.W. Hong, Seismic Behavior and Analysis of a U-shaped Masonry Fence Wall, Earthquake Engineering Society of Korea (EESK) Annual Conference, 23 September 2022.
- [학회 발표] M. Kim, S. Lee, and J.W. Hong, Dynamic Transient Analysis of a Submerged Floating Tunnel by Collision Impact, IABMAS 2022: 11th International Conference on Bridge Maintenance, Safety and Management, Barcelona, Spain, 12 July 2022.
- [학회 발표] J.W. Hong, Recent Developments of Peridynamcis and Coupling Methodologies, KSCM Annual Conference, PyeongChang, Korea, 24 June 2022. (Plenary talk).
- [학회 발표] D. Park, Y. Choi, S.E. Lee, B.H. Kim, G.J. Lee, M.K. Lee, and J.W. Hong, Design Optimization of Acoustic Emission Sensor, KSCM Annual Conference, PyeongChang, Korea, 23 June 2022. (Poster).
- [학회 발표] T.H Lee, K. Ko, and J.W. Hong, Numerical Study on Impact Performance of Nonuniformly Patterned Nacre-like Structure Under an Extensive Velocity Range, KSCM Annual Conference, PyeongChang, Korea, 23 June 2022. (Poster).
- [학회 발표] M. Kim, S. Lee, and J.W. Hong, Estimation of Pressure Loading on the Submerged Floating Tunnel Using Arbitrary Lagrangian-Eulerian Method, COSEIK Annual Conference, Jeju, Korea, 14 April 2022.

**2021**

- [학술지] J.M. Sun, D. Cho, S. Lee, T.H. Lee, J.W. Jung, J. Lee, S.H. Cho, T.H. Eom, J.W. Hong, Y.S. Shim, S. Jeon, and H.W. Jang, Rationally Designed TiO2 Nanostructures of Continuous Pore Network for Fast-Responding and Highly Sensitive Acetone Sensor, Small Methods, 5:2100941, 2021. (Co-corresponding author). DOI: https://doi.org/10.1002/smtd.202100941
- [학술지] Y. Choi, S.E. Lee, J.W. Jung, and J.W. Hong, Collision Mechanism of Unmanned Aerial Vehicles onto Glass Panels, International Journal of Micro Air Vehicles, 13:1-18, 2021. DOI: https://doi.org/10.1177/17568293211060504

## 소프트웨어 등록

연구실 Patents & Software의 2022년 3월 30일 등록 4건이다. 제목과 등록번호, 참여자는 연구실 게시 표기다.[^patents]

- 2022-03-30 · Explosive Source Detection Model in Panoramic Images (Registration number: C-2022-015029) by Jung-Wuk Hong, Youngjun Choi, Dawon Park, Sunwoo Kim, Seungil Lee, Seungwon Ok, Donghwan Kim, and Yeongho Jeong, 30 March 2022.
- 2022-03-30 · Gas Pipe Housing Detection Model in Panoramic Images (Registration number: C-2022-015030) by Jung-Wuk Hong, Youngjun Choi, Dawon Park, Sunwoo Kim, Seungil Lee, Seungwon Ok, Donghwan Kim, and Yeongho Jeong, 30 March 2022.
- 2022-03-30 · Gas Tank Detection Model in Panoramic Images (Registration number: C-2022-015031) by Jung-Wuk Hong, Youngjun Choi, Dawon Park, Sunwoo Kim, Seungil Lee, Seungwon Ok, Donghwan Kim, and Yeongho Jeong, 30 March 2022.
- 2022-03-30 · Outdoor Unit Detection Model in Panoramic Images (Registration number: C-2022-015032) by Jung-Wuk Hong, Youngjun Choi, Dawon Park, Sunwoo Kim, Seungil Lee, Seungwon Ok, Donghwan Kim, and Yeongho Jeong, 30 March 2022.

## 수상과 선정

연구실 News의 수상 5건이다. 날짜가 연도뿐인 항목은 제목·본문이 밝힌 학회 연도를 적었으며, 일자는 게시되어 있지 않다.[^news]

- 2022 · Suyeong Jin이 대한기계학회 연차 학술대회 국제 세션에서 Best Presentation Award를 받았다.
- 2022 · Mujong Kim과 Sangmin Lee가 한국전산구조공학회 학술 심포지엄에서 Paper Presentation Award를 받았다.
- 2022 · 홍정욱 교수가 한국전산역학회 연차 학술대회에서 Academic Award를 받았다.
- 2022-04-01 · 홍정욱 교수가 학과 Best Teaching Award를 받았다.
- 2022-02-16 · Sang Eon Lee, Sangmin Lee, Kwonhwan Ko가 서울 코엑스에서 열린 Lab start-up 2022 전시 부문의 Grand Prize Award를 받았다.

## 소식

연구실 News가 전한 기고 소식이다.[^news]

- 2022-04-11 · 홍정욱 교수가 동아일보에 복합 재난을 설명하는 글을 기고했다.

## 연락과 위치

- 교수 연구실: KAIST W16동 306호[^dept]
- 교수 기관 전화: 042-350-3616[^dept]
- 교수 업무 이메일: j.hong@kaist.ac.kr[^dept]
[^dept]: KAIST 건설및환경공학과, 홍정욱 교수 소개(학력·경력·연구분야·연락). <https://cee.kaist.ac.kr/boards/view/professor/55/sc_category/1> 관측일 2026-11-06.
[^research]: 응용역학 연구실, Research. <https://aaml.kaist.ac.kr/research> 관측일 2026-11-06.
[^professor]: 응용역학 연구실, Professor Jung-Wuk Hong(학력·경력). <https://aaml.kaist.ac.kr/people/professor> 관측일 2026-11-06.
[^people]: 응용역학 연구실, People. <https://aaml.kaist.ac.kr/people> 관측일 2026-11-06.
[^pubs]: 응용역학 연구실, Publications(학술지·학회 논문집). <https://aaml.kaist.ac.kr/publications> 관측일 2026-11-06.
[^presentations]: 응용역학 연구실, Presentations. <https://aaml.kaist.ac.kr/presentations> 관측일 2026-11-06.
[^patents]: 응용역학 연구실, Patents & Software. <https://aaml.kaist.ac.kr/patents-software> 관측일 2026-11-06.
[^news]: 응용역학 연구실, News. <https://aaml.kaist.ac.kr/news> 관측일 2026-11-06.
[^p1]: Y. K. Hwang, J. E. Bolander, Y. M. Lim, J.-W. Hong, Computational Particle Mechanics 9, 1351–1365 (2022). <https://doi.org/10.1007/s40571-022-00473-x> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p2]: D. Park, J.-W. Hong, Computational Mechanics (2026). <https://doi.org/10.1007/s00466-026-02836-0> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p3]: Y. Choi, D. Park, S. Kim, J.-W. Hong, Earthquake Engineering & Structural Dynamics 55, 130–149 (2025). <https://doi.org/10.1002/eqe.70070> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p4]: D. Park, W.-M. Jang, E. Cheon, J.-W. Hong, Results in Engineering 28, 107183 (2025). <https://doi.org/10.1016/j.rineng.2025.107183> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p5]: T. H. Lee, K. Ko, J.-W. Hong, Journal of the Computational Structural Engineering Institute of Korea 35, 215–226 (2022). <https://doi.org/10.7734/coseik.2022.35.4.215> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p6]: H. Chen 외, S. Jeon, Nature Communications 15, 8074 (2024). <https://doi.org/10.1038/s41467-024-52305-6> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p7]: Y. K. Hwang, S. Jin, J.-W. Hong, I. Sohn, Advances in Engineering Software 192, 103632 (2024). <https://doi.org/10.1016/j.advengsoft.2024.103632> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.
[^p8]: H. Kim, S. Kim, S. Lee, J.-W. Hong, Physics of Fluids 38, 075157 (2026). <https://doi.org/10.1063/5.0342742> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5036044934,publication_year:2021-2026> 관측일 2026-11-06.

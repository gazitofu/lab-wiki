# 인공지능 x 모빌리티 연구실 (KAIST AI x Mobility Lab, AixMobility Lab)

**KAIST 건설및환경공학과 · 여화수 교수**

- 분야: 교통 흐름과 운전자 행태, 교통안전과 충돌 위험 예측, 교통신호·이동 서비스 운영, 도시 공간 설계, 교통 기반시설 유지관리[^dept][^research]
- 대분야: 건설·도시·인프라
- 태그: 교통·도시 계획[^dept]
- 홈페이지: <https://www.aimobility.kaist.ac.kr/>
- 근거와 출처: [KAIST AI x Mobility Lab 근거 페이지](aimobility-sources.md)

> 차량과 보행자의 움직임을 모형으로 설명하고 교통 상태와 사고 위험을 예측하며, 교통신호·이동 서비스·도시 공간과 교통 기반시설의 설계·운영·관리를 연구한다.[^dept][^research]

## 무엇을 연구하나

여화수 교수가 이끄는 연구실은 사람과 차량의 이동을 안전하고 효율적으로 운영하고, 지속가능한 교통 체계를 설계하는 방법을 연구한다. 학과 소개는 교통현상을 수학적인 관계로 나타내고 미래 상태를 예측하는 일, 정보통신기술을 결합한 지능형 교통 시스템(교통 정보를 모아 분석해 교통 운영에 쓰는 정보통신 기반 체계), 온실가스 감축을 위한 녹색교통도시 설계, 교통 기반시설의 유지관리를 연구 대상으로 설명한다.[^dept] 연구실은 연구를 「Mobility + AI」, 「Smart Cities and Urban Informatics」, 「Predictive Analytics」의 세 갈래로 나눈다. AI는 Artificial Intelligence의 약어인 인공지능이며, 예측 분석은 관측 자료에서 미래 상태를 추정하는 분석이다.[^research]

교통을 설명하는 한 축은 시뮬레이션(대상이나 현상의 변화를 모형으로 재현해 살피는 방법)이다. 연구실은 차량 한 대의 움직임을 다루는 미시 교통 모형부터 차량 무리와 도로 전체 흐름을 다루는 모형까지 연구하고, 보행자의 이동과 대피도 대상으로 삼는다.[^research] 대표 논문 1은 개별 차량을 상세하게 계산하는 방식과 차량 무리의 흐름을 계산하는 방식을 교통 상황에 따라 바꿔 배정한다. 두 방식 사이를 오갈 때 차량 정보와 교통 흐름의 일관성을 유지하도록 설계했고, 시험한 수요 조건들에서 중간 규모 모형보다 정확하면서 상세 모형보다 계산 부담이 작았다.[^p1]

또 다른 축은 사고가 일어나기 전 위험을 예측하는 일이다. 연구실은 운전 행태(운전자가 속도·차로·진로를 선택하는 행동), 교통사고 분석, 충돌 위험 예측, 미래 교통 상태 예측을 연구 대상으로 둔다.[^research] 대표 논문 2는 앞으로의 이동 경로를 하나로 단정하지 않고 가능한 경로들의 확률을 반영해 보행자와 차량의 충돌 위험을 평가한다.[^p2] 대표 논문 3은 도로의 합류·분류 형태(도로가 합쳐지거나 갈라지는 구간의 형태)와 차량 속도·진입 교통량(진입로에서 단위 시간 동안 들어오는 차량 수)을 함께 분석해 사고 위험이 달라지는 조건을 살핀다.[^p3] 대표 논문 8은 차량 탑재 카메라에서 물체를 검출하고 주행 차로 영역의 교통 밀도(도로의 일정 길이 안에 있는 차량 수)를 추정하는 방법을 제안한다.[^p8]

도시 차원에서는 도시 자료 분석과 교통 서비스 운영을 함께 다룬다.[^research] 연구 소개는 도시의 토지 이용, 전기차 충전소 입지, 도시 자료 분석, 안전하고 회복력 있는 기반시설을 연구 대상으로 든다.[^research] 대표 논문 6은 고령자가 여가를 위해 걸을 때와 상업 활동을 위해 걸을 때 도시 환경과 경로 선택의 관계가 달라짐을 분석한다.[^p6] 대표 논문 7은 각 차량이 따로 충전을 결정할 때 값싼 시간대로 수요가 몰리는 문제를 다룬다. 행동 관성이나 손실 회피 같은 요인을 충전 제어에 넣어 차량 무리의 반응을 분산하는 학회 포스터 연구다.[^p7]

## 주요 연구 주제

### 교통 흐름·자율주행과 신호 운영

연구실은 교통 흐름 이론, 운전 행태 이론, 자율 이동체 제어, 자동화 대중교통과 이동 서비스 운영을 연구한다.[^research] 대표 논문 4는 상용 적응형 순항 제어(Adaptive Cruise Control, 앞차와의 간격에 따라 속도를 자동 조절하는 주행 보조 기능)가 고속도로 혼잡과 안전에 미치는 영향을 분석한다. 차간 간격 설정에 따라 혼잡과 위험이 생기는 양상이 달랐고, 이런 차량들이 함께 달릴 때의 문제도 살폈다.[^p4]

교통신호 운영에서는 강화학습(행동의 결과로 받은 보상을 이용해 행동 선택 규칙을 배우는 방법)을 사용한 협력 제어를 개발했다. 대표 논문 5는 교차로마다 제어를 분산하면서 서로 정보를 주고받게 하고, 도로 사이의 공간적 관계를 그래프(대상과 대상 사이의 연결을 점과 선으로 나타낸 구조)로 표현한다. 서울 강남 지역을 재현한 시험에서 경험하지 않은 교통 수요 상황으로 학습한 규칙을 옮겨 쓰는 능력과 교차로 간 협력 효과를 평가했다.[^p5]

### 도시 공간·이동 서비스와 예측

연구 소개는 실시간 도시 자료 분석, 지리정보시스템(위치와 연결된 자료를 저장·분석하는 정보 체계), 원격탐사(대상과 직접 접촉하지 않고 떨어진 곳에서 성질을 관측하는 방법), 토지 이용과 전기차 충전소 위치의 최적화를 다룬다. 수요응답형 대중교통(이용자의 이동 수요에 따라 노선이나 운행 계획을 조정하는 대중교통)과 이동 서비스 운영도 연구 대상이다.[^research] 대표 논문 6은 녹지 비율·도로 연결성과 경로 선택의 관계가 보행 목적에 따라 달라짐을 구분했고, 대표 논문 7은 공유 에너지 기반시설에 걸리는 부담을 줄이기 위해 충전 신뢰성·비용·수요 집중을 함께 다뤘다.[^p6][^p7]

### 기반시설 상태 예측과 유지관리

연구실은 기반시설의 성능이 시간에 따라 저하되는 과정을 모형으로 나타내고, 특성이 다른 시설들이 함께 있는 체계에서 유지관리 결정을 최적화하는 방법을 연구한다. 상태기반 유지관리(관측한 설비 상태를 바탕으로 정비 여부와 시점을 정하는 방식)를 철도 시스템과 차량 부품에 적용하는 연구, 유지관리 행동 선택, 자료 기반 상태 예측을 연구 대상으로 제시한다.[^research] 학과 소개도 교통 기반시설 유지관리 최적화를 주요 연구 분야로 적는다.[^dept]

## 대표 논문

교수가 저자로 참여한 KAIST 재직 시기의 2021–2026년 연구 가운데 교통 모형, 위험 예측, 신호 운영, 도시 공간과 이동 서비스의 갈래를 보여 주는 논문 8편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 연도는 등록 서지의 출판 연도이며, 주요 저자는 전체 저자 순서에 따른 표시다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [NextSim: Multi-Level Traffic Simulation for Urban Networks Using Dynamic Level Assignment](https://doi.org/10.1109/tits.2026.3671220) · IEEE Transactions on Intelligent Transportation Systems | 도로 구간의 상황에 따라 개별 차량을 상세하게 계산하는 방식과 차량 무리의 흐름을 계산하는 방식을 바꿔 쓴다. 서로 다른 계산 방식 사이의 차량 정보와 교통 흐름을 일관되게 연결했고, 여러 수요 조건에서 중간 규모 모형보다 정확하면서 상세 모형보다 계산 부담을 줄였다. 실제 도시 도로망 적용에서는 교통관리에 활용할 가능성을 보였다.[^p1] | 1저자 Yeeun Kim, 마지막 저자 Hwasoo Yeo |
| 2 | 2026 | [Evaluation of Pedestrian Future Conflict at Non-Signalized Intersections Based on Probabilistic Trajectory Prediction](https://doi.org/10.1109/tits.2026.3661062) · IEEE Transactions on Intelligent Transportation Systems | 보행자와 차량의 미래 경로가 불확실하다는 점을 반영해 신호등 없는 교차로의 충돌 위험을 평가한다. 경로 예측과 새 안전 지표를 결합해 위험한 상황을 분류하고 위험이 진행되는 정도를 평가했으며, 보행자 행동의 불확실성이나 관측 누락이 큰 조건에서도 방법을 시험했다.[^p2] | 1저자 Tengfeng Lin, 참여 저자 Hwasoo Yeo |
| 3 | 2025 | [Section-Based Crash Risk Analysis Integrating the Effect of Traffic States and Road Geometry](https://doi.org/10.1049/itr2.70134) · IET Intelligent Transport Systems | 고속도로의 교통 상태와 도로 형상을 함께 분석해 사고 위험을 설명한다. 상류와 하류의 속도 차이, 합류·분류 구간의 형태, 진입 교통량을 함께 다뤘다. 시험한 조건에서 특히 분류 구간의 속도 차이가 클 때 위험이 높았고, 진입로와 본선 교통량 비율도 위험과 관계를 보였다.[^p3] | 1저자 Jihu Kim, 마지막 저자 Hwasoo Yeo |
| 4 | 2025 | [Impact of commercial adaptive cruise control on highway traffic congestion and safety](https://doi.org/10.1080/21680566.2025.2519630) · Transportmetrica B: Transport Dynamics | 상용 적응형 순항 제어 차량의 주행 자료로 차량추종 모형(앞차에 반응하는 뒤차의 움직임을 나타낸 모형)을 조정하고 고속도로 진입로 구간을 재현했다. 짧은 간격 설정은 국소 혼잡과 안전거리 문제를, 긴 간격 설정은 도로 수용량 저하와 끼어들기·급제동 문제를 보였다. 두 유형이 함께 달리면 혼잡과 안전 위험이 커져 이를 고려한 교통정책이 필요하다고 제안한다.[^p4] | 1저자 Hwapyeong Yu, 마지막 저자 Hwasoo Yeo |
| 5 | 2025 | [Decentralized and Communication-Based Multi-Agent Traffic Signal Control Model Employing a Graph Representation for the State](https://doi.org/10.1109/tits.2025.3548945) · IEEE Transactions on Intelligent Transportation Systems | 여러 교차로가 각자 신호를 정하면서 서로 협력하도록 학습한다. 도로의 공간적 관계를 연결 구조로 표현하고 교차로 간 통신을 사용했다. 서울 강남 지역을 재현한 시험에서 경험하지 못한 수요 상황에 적응하는 규칙을 얻었고, 교차로들이 함께 수요를 재배분해 도로망 신호 운영의 효율을 높였다.[^p5] | 1저자 Jinwon Yoon, 마지막 저자 Hwasoo Yeo |
| 6 | 2023 | [Sustainable, walkable cities for the elderly: Identification of the built environment for walkability by activity purpose](https://doi.org/10.1016/j.scs.2023.105004) · Sustainable Cities and Society | 고령자의 보행 자료를 이용해 활동 목적에 따라 어떤 도시 환경을 선택하는지 분석했다. 여가 보행에는 거리의 쾌적함과 도로망 특성이 중요했고, 녹지 비율과 도로 연결성이 경로 선택에 맺는 관계는 보행 목적에 따라 달랐다. 고령자의 목적에 맞는 보행 환경과 도시 설계를 위한 근거를 제시한다.[^p6] | 1저자 Yujin Kim, 참여 저자 Hwasoo Yeo |
| 7 | 2026 | [Behavioral Reinforcement Learning for Decentralized EV Fleet Charging: Reliability–Cost–Coordination Trade-offs Under Split Control Authority](https://doi.org/10.1145/3765611.3815391) · ACM Sustainability Week, 포스터 | 전기차들이 각자 저렴한 시간에 충전하려다 수요가 한꺼번에 몰리는 문제를 다룬다. 행동 관성·인식의 불확실성·손실 회피·주의의 한계를 개별 충전 제어에 반영했다. 한국 대도시 자료에 기반한 시험에서 비교 제어기와 같은 차량 무리의 충전 신뢰성을 얻으면서 비용과 수요 집중을 낮췄다고 보고한다.[^p7] | 1저자 Peijia Pok, 마지막 저자 Hwasoo Yeo |
| 8 | 2023 | [Urban Traffic Density Estimation from Vehicle-mounted Camera for Real-time Application](https://doi.org/10.1109/icaiic57133.2023.10066969) · International Conference on Artificial Intelligence in Information and Communication | 차량 탑재 카메라에서 검출한 차량과 차로 영역으로 도시 교통 밀도를 추정한다. 연속된 모든 영상을 처리해야 하는 방식 대신 일부 화면만으로도 작동하도록 물체 검출을 이용했다. 버스 노선 영상으로 밀도 추정 방법을 평가하고, 추정 결과를 교통 혼잡 지도에 나타냈다.[^p8] | 1저자 Haechan Cho, 마지막 저자 Hwasoo Yeo |

## 교수와 전문 분야

여화수 교수는 서울대학교 토목공학과 학사(1996), UC Berkeley 토목환경공학과 석사(2004)와 박사(2008)를 받았다. 학과는 직위를 교수, 연구 분야를 스마트 교통 시스템으로 소개한다.[^dept] 연구실 교수 소개는 2009년 3월 KAIST 조교수로 부임했고 2021년 3월부터 교수로 재직한다고 적으며, 건설및환경공학과 학과장 직책도 함께 적는다.[^about]

학과가 제시한 전문 분야는 교통 흐름 이론과 운영, 교통 시뮬레이션, 지능형 교통 시스템(Intelligent Transportation Systems), 사고 분석·예측, 사고 집중 지점 식별, 교통 기반시설 유지관리 최적화, 녹색교통도시 설계다.[^dept] 대표 연구로 보면 교통 상태를 계산하고 관측하는 모형 개발, 차량·보행자 충돌 위험 분석, 협력형 교통신호 제어, 이동 행태를 고려한 도시 설계와 서비스 운영이 이어진다.[^p1][^p2][^p3][^p5][^p6][^p7][^p8]

## 응용 분야

연구 소개는 자율 이동체 제어, 자동화 대중교통, 수요에 맞춘 이동 서비스, 전기차 충전소 입지, 철도와 차량 부품의 유지관리를 응용 대상으로 제시한다.[^research] 논문은 도시 도로망 시뮬레이션의 교통관리 활용 가능성, 보행자 보호를 위한 충돌 위험 알림과 차량 제동, 교차로 신호 협력, 고령자를 위한 보행 환경 설계, 전기차 충전 수요 분산을 다룬다.[^p1][^p2][^p5][^p6][^p7]

## 구성원

2026년 11월 6일 연구실 About 페이지 기준으로 박사후연구원 2명, 박사과정 7명, 석사과정 3명이다. 「대표 논문 참여」는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^about]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Jihu Kim | 박사후연구원 | jihukim1@kaist.ac.kr | 3, 8 |
| Hyunsoo Kim | 박사후연구원 | hyunsookim@kaist.ac.kr |  |
| Haechan Cho | 박사과정 |  | 8 |
| Peijia Pok | 박사과정 |  | 7 |
| Hyejin Lee | 박사과정 |  |  |
| Sujae Jeon | 박사과정 |  | 1 |
| Chaemin Na | 박사과정 |  |  |
| Yeonwoo Yoo | 박사과정 |  |  |
| Keunhee Cho | 박사과정 |  |  |
| Dongheon Lee | 석사과정 |  |  |
| Donghun Lee | 석사과정 |  |  |
| Sumin Kim | 석사과정 |  |  |

## 졸업생과 이전 구성원

연구실 About의 Alumni에 적힌 2011–2026년 학위 기록 43항목이다. 박사 17항목과 석사 26항목이며, 한 사람이 서로 다른 학위로 적힌 기록을 포함한다. 학위·연도·진로는 연구실 표기다.[^about]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yeonwoo Yu | MS (2026) | PHD course |
| Hye-young Tak | PhD (2026) | Samsung Fire & Marine Insurance Co, Korea |
| Jihu Kim | PhD (2026) | KAIST, Korea |
| Sharon Kim | MS (2026) | U of Michigan, USA |
| Sujae Jeon | MS (2025) | PHD course |
| Chaemin Na | MS (2025) | PHD course |
| Hwapyeong Yu | PhD (2024) | Myungji University |
| Safitri Syelfia Tanjung | MS (2024) | BYD, Indonesia |
| Hyejin Lee | MS (2024) | PHD course |
| Yeeun Kim | PhD (2023) | University of Central Florida, USA |
| Joohee Lee | MS (2023) | LG CNS, Korea |
| Zhixiong Jin | MS (2023) | Université Gustave Eiffel, France |
| Tengfeng Lin | MS (2022) | KAIST, Korea |
| Jiyoung Hwang | MS (2022) | Shinhan Card, Korea |
| Dongho Ka | PhD (2021) | Nota, Korea |
| Jeongyun Kim | PhD (2021) | Seoul National Univ. of Science & Technology, Korea |
| Seongjin Choi | PhD (2021) | Univ. of Minnesota, USA |
| Byunjoon Noh | PhD (2021) | Hanyang Univ. Korea |
| Jinwon Yoon | PhD (2021) | Korea University, Korea |
| Kyowon Song | PhD (2021) | Kookmin Univ., Korea |
| Jihu Kim | MS (2020) | PHD course |
| Hwapyeong Yu | MS (2019) | PHD course |
| Lee Sangjeong | MS (2018) |  |
| Kim, Sunghoon | PhD (2018) | KOTI, Korea |
| Lee, Donghoun | PhD (2018) | Sejong Univ., Korea |
| Kim, Yeeun | MS (2018) | PHD Course |
| Choi, Seongjin | MS (2017) | PHD course |
| Suh, Jonghae | PhD (2016) | SK C&C, Korea |
| Kim, Jeongyun | MS (2016) | PHD Course |
| Woo, Soomin | MS (2016) | Konkuk Univ., Korea |
| Ahn, Yongjoon | PhD (2016) | Daejeon Sejong Research Institute |
| Yoo, Suhyung | MS (2015) | Mirae Asset, Korea |
| Tak, Sehyun | PhD (2015) | KOTI, Korea |
| Oh, Simon | PhD (2015) | Korea Univ., Korea |
| Choi, Junyong | MS (2015) | KAIST, Korea |
| Park, Minju | PhD (2015) | Hannam Univ., Korea |
| Park, Jinhyun | MS (2015) | MOLIT, Korea |
| Jo, Subin | MS (2014) | Samsung C&T |
| Kim, Sunghoon | MS (2013) | PHD Course |
| Shin, Seongwook | MS (2013) | Hyundai Construction Co. |
| Jung, Yunhee | MS (2012) |  |
| Song, Sungjun | MS (2011) | LG CNS, Korea |
| Oh, Simon | MS (2011) | Korea Univ., Korea |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 국제학술지 25항목·국내학술지 6항목과 Conference Papers의 국제학회 64항목, 총 95항목이다. 연도는 연구실의 기재 연도이며 제목·저자·발표처는 연구실 표기다. 날짜가 없는 학회 항목은 기재 연도에 따라 묶었다.[^pubs][^conference] DOI가 함께 적힌 항목은 논문의 식별 주소다.[^bibliography]

**2026**

- Bortiorkor N. Alabi, Seunghwan Cha, Tengfeng Lin, Dawoon Keong, Alexandra Suchshenko, Hwasoo Yeo, Kunhee Choi. Breaking the Sound Barrier: Investigating Noise Challenges in the Development of Advanced Air Mobility. Transportation Research Record. Vol.2680-7(2026) https://doi.org/10.1177/03611981251393207
- Yeeun Kim. Seongjin Choi, Sujae Jeon, Hwasoo Yeo. NextSim: Multi-Level Traffic Simulation for Urban Networks Using Dynamic Level Assignment. IEEE Transactions on Intelligent Transportation Systems. Vol.27-7 (2026) http://doi.org/10.1109/TITS.2026.3671220
- Jinyue Yu. Chenqiang Zhu. Junfang Tian. Hwasoo Yeo. Jing Zhao. MCVae-CFM: a behavior-embedded dual calibration framework for time-varying car-following models via multichannel variational autoencoding. Transportation Research Part C: Emerging Technologies. Vol. 183, 105483. (2026) http://doi.org/10.1016/j.trc.2026.105636
- Hyunsoo Kim, Hwasoo Yeo. Hybrid approach for coordinated traffic signal control capturing offset-split interdependency using average phase statistics. Transportation Research Part C. Vol.188, 105718. (2026) https://doi.org/10.1016/j.trc.2026.105718
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. IEEE Transactions on Intelligent Transportation Systems. Vol.27-4 (2026) https://doi.org/10.1109/TITS.2026.3661062
- Phoebe Ho, Yeonwoo Yu. Sujae Jeon, Lindsay Park, Hwasoo Yeo, Kunhee Choi. Equity Considerations for Emerging Technologies in Transportation: A Comparative Study of Planning Practices in the United States and South Korea. Transportation Research Record. Vol.2680-1(2026) https://doi.org/10.1177/03611981251362811
- Hyejin Lee, Haechan Cho, Byeongjoon Noh, Hwasoo Yeo. Real-time Warning system for Vehicle-to-Pedestrian Collision on Intersection using Edge Computing Platform. The IEEE International Conference on Intelligent Transportation Systems (2026)
- Yeonwoo Yu, Hye-young Tak, Taeheon Lee, Hwasoo Yeo. Evaluating Driving Risk and Driver Profiles with Asymmetric Microscopic Behavior Theory. The IEEE International Conference on Intelligent Transportation Systems (2026)
- Peijia Pok, Hwasoo Yeo. Behavioral Reinforcement Learning for Decentralized EV Fleet Charging: Reliability–Cost–Coordination Trade-offs Under Split Control Authority. ACM Sustainability week (2026)
- Jihu Kim, Hwasoo Yeo. Utility-Driven Idle Vehicle Repositioning for Ride-Hailing System. World Conference on Transport Research (2026)
- Hyunsoo Kim, Hwasoo Yeo. Hybrid Approach for Coordinated Traffic Signal Control Capturing Offset-Split Interdependency Using Average Phase Demand. World Conference on Transport Research (2026)
- Hyejin Lee, Seokjun Hong, Byeonngjoon Noh, Hwasoo Yeo. DRIFT Open Dataset: A Drone-Derived Intelligence for Traffic Analysis in Urban Environment. Transportation Research Board Annual Meeting (2026)
- Sharon Kim, Hwapyeong Yu, Hwasoo Yeo, Kunhee Choi. Phase-Aware Modeling of Autonomous Vehicle Behavior at Urban Signalized Intersections. TransportationTransportation Research Board Annual Meeting (2026)
- Hyun Kim, Timothy Proctor, Sharon Kim. Peijia Pok, Hwasoo Yeo, Kunhee Choi. On the Road to Inclusion: Exploring Equity in Autonomous Public TransportationTransportation Research Board Annual Meeting (2026)

**2025**

- Jihu Kim, Yeeun Kim, Hwasoo Yeo. Section-Based Crash Risk Analysis Integrating the Effect of Traffic States and Road Geometry. The institution of Engineering and Technology. Vol. 20(1). (2025) https://doi.org/10.1049/itr2.70134
- Hyeyoung Tak, Hwasoo Yeo. Early detection of traffic flow breakdown at highway bottleneck using section-based transitional instability. Transportation Research Part C: Emerging Technologies. Vol. 183, 105483. (2025) https://doi.org/10.1016/j.trc.2025.105483
- Tengfeng Lin, Zhixiong Jin, Seongjin Choi, Hwasoo Yeo. Predicted lane-based time to collision: A novel surrogate safety measure for pedestrian potential risk evaluation at non-signalized intersections. Transportation Research Interdisciplinary Perspectives. Vol 34-101705 (2025). https://doi.org/10.1016/j.trip.2025.101705
- Dawoon Jung, Jiwoo Kim, Sophiya Shrestha, Hwasoo Yeo, Lisa Lim. Accessible bus stops: evaluating bus stop design guidelines for diverse transportation-disadvantaged groups. Journal of Urban Design. Journal of Urban Design.1-21 (2025) https://doi.org/10.1080/13574809.2025.2505742
- Hwapyeong Yu, Hwasoo Yeo. Impact of commercial adaptive cruise control on highway traffic congestion and safety. Transportmetrica B: Transport Dynamics. Vol 13-1 (2025). https://doi.org/10.1080/21680566.2025.2519630
- Jinwon Yoon, Kyuree Ahn, Kanghoon Lee, Jinkyoo Park, Hwasoo Yeo. Decentralized and Communication-Based Multi-Agent Traffic Signal Control Model Employing a Graph Representation for the State. IEEE Transactions on Intelligent Transportation Systems Vol. 26-5 (2025). https://doi.org/10.1109/TITS.2025.3548945
- Hwapyeong Yu, Hwasoo Yeo. Traffic control policies for minimizing the negative effect of Adaptive Cruise Control on highway. Transportation Research Part C Vol.173, https://doi.org/10.1016/j.trc.2025.105063 (2025)
- Hwapyeong Yu, Hwasoo Yeo. Dynamic characteristics of commercial Adaptive Cruise Control across driving situations: Response time, string stability, and asymmetric behavior. Transportation Research Part C Vol.170, 104931 (2025) https://doi.org/10.1016/j.trc.2024.104931
- 전수제. 김예은. 여화수. 비대칭 주행 행태를 반영한 2차원 차로 변경 모델. 대한교통학회지. 제 43권 제 6호 p.815 (2025.12)
- Chaemin Na, Hwasoo Yeo. Optimization of Modular Autonomous Electric Vehicle System with Mixed-Integer Linear Programming. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Sharon Kim, Hwasoo Yeo. Characteristics of Autonomous Vehicle Behaviors and Their Traffic Impacts at Signalized Intersections in Mixed Traffic Situations. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Hyejin Lee, Seokjun Hong, Byeongjoon Noh, Hwasoo Yeo. DRIFT Open Dataset: A Drone-Derived Intelligence for Traffic Analysis in Urban Environment. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Pei Jia Pok, Hwasoo Yeo. Agent-Based Modeling for Equitable EV Infrastructure Planning: A Comparative Analysis of Policy Mechanisms. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Dongheon Lee, Sujae Jeon, Pei Jia Pok, Hwasoo Yeo. Simulation-Based Assessment of Urban Traffic Impact from Trackless Rapid Transit. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Sujae Jeon, Yeeun Kim, Hwasoo Yeo. Multi-level Traffic Simulation for Urban Networks Using Dynamic Level Assignment for Real-World Network under an Event Condition. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Keunhee Cho, Hwasoo Yeo. Temporal Knowledge Graph-Based Accident Prediction from Dashcam. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Haechan Cho, Hwasoo Yeo. SwinTSE: Urban Traffic State Estimation for Camera Undetected. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Yeonwoo Yu, Hwasoo Yeo. Sequence-Based Analysis and Application Strategies of Autonomous Vehicle Crash Scenarios. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Hyunsoo Kim, Hwasoo Yeo. Hybrid Approach for Coordinated Traffic Signal Control Capturing Offset-Split Interdependency Using Average Phase Statistics. The 36th KKHTCNN Symposium on Civil Engineering. (2025)
- Hyunsoo Kim, Jung Won Lee, and Hwasoo Yeo. HyLight: Hybrid Approach of Reinforcement Learning and Rule-based Optimization for Coordinated Traffic Signal Control Based on Average Phase Demand. The IEEE International Conference on Intelligent Transportation Systems (2025)
- Chaemin Na, Hyunsoo Kim, and Hwasoo Yeo. Turn-level Maximum Queue Length Prediction Based on Dynamic Graph Deep Learning Considering Traffic Signal The IEEE International Conference on Intelligent Transportation Systems (2025)
- Sujae Jeon, Yeeun Kim, and Hwasoo Yeo. A Two-Dimensional Lane-Changing Model with Asymmetric Driving Behavior for Autonomous Vehicles. The IEEE International Conference on Intelligent Transportation Systems (2025)
- Hye-young Tak, Hwasoo Yeo. Quantifying Traffic Flow Instability at Highway Bottleneck Using Lyapunov Exponents. 10th international symposium on dynamic traffic assignment (2025)
- Jihu Kim, Jeongyun Kim, Hwasoo Yeo. Utility-Driven Idle Vehicle Repositioning Model for Ride-Hailing System. 10th international symposium on dynamic traffic assignment (2025)
- Pei Jia Pok, Hwasoo Yeo, Soomin Woo. Multi-Agent Game-Theoretic Modelling of Electric Vehicle Charging Behavior and Pricing Optimization in Dynamic Ecosystems. ANT 2025 : The 16th International Conference on Ambient Systems, Networks and Technologies (2025)
- Hye-young Tak, Hwasoo Yeo. Assessing Traffic Dynamics on Highway: Stability and Intensity in Breakdown and Recovery Pathways, ANT 2025 : The 16th International Conference on Ambient Systems, Networks and Technologies (2025)
- Jihu Kim, Jeongyun Kim, Hwasoo Yeo.A Study on Self-Rebalancing in Inter-Region Vehicle Distribution for Ride-Hailing Services, ANT 2025 : The 16th International Conference on Ambient Systems, Networks and Technologies (2025)
- Hye-young Tak, Hwasoo Yeo. INTERPRETING TRAFFIC BREAKDOWN PROBABILITY AT FREEWAY MERGE SEGMENTS: IMPACT OF TIME-LAGGED AND LANE-SPECIFIC TRAFFIC STATES. . Transportation Research Board Annual Meeting (2025)
- Yaoyuan Ji, Jing Zhao, Hwasoo Yeo, Pengfei Liu. Impact of Combined Alignments on Operating Speed: A Simulator Study for Expressway Tunnels. Transportation Research Board Annual Meeting (2025)
- Hyun Kim, Timothy Proctor, Sharon Kim, Peijia Pok, Hwasoo Yeo, Kunhee Choi. On the Road to Inclusion: Exploring Equity in Autonomous Public Transportation. Transportation Research Board Annual Meeting (2025)
- Bortiorkor Nii Tsui Alabi, Seunghwan Cha, Tengfeng Lin, Dawoon Jeong, Alexandra Suchshenko, Hwasoo Yeo, Kunhee Choi. Breaking the Sound Barrier: Investigating Noise Challenges in the Development of Advanced Air Mobility. Transportation Research Board Annual Meeting (2025)
- Phoebe Ho, Sujae Jeon, Yeonwoo Yu, Lindsay Park, Hwasoo Yeo, Kunhee Choi. Equity Considerations for Emerging Technologies in Transportation: A Comparative Study of Planning Practices in the United States and South Korea. Transportation Research Board Annual Meeting (2025)
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Inhi Kim. A Surrogate Safety Measure at Non-signalized Intersections Based on Probability Trajectory Prediction. Transportation Research Board Annual Meeting (2025)
- Jihu Kim, Yeeun Kim, Hwasoo Yeo. Analysis of Highway Traffic Crashes Risk Considering Traffic States in Merging and Diverging Areas. Transportation Research Board Annual Meeting (2025)

**2024**

- Yujin Kim, Hwasoo Yeo, Lisa Lim, Byeonjoon Noh. Integrating visual and community environments in a motorcycle crash and casualty estimation. Accident Analysis & Prevention (2024). https://www.sciencedirect.com/science/article/pii/S0001457524003373?dgcid=author DOI: https://doi.org/10.1016/j.aap.2024.107792
- Yeeun Kim, Hwasoo Yeo. Asymmetric repulsive force model: A new car-following model with psycho-physical characteristics. Transportation Research Part C Vol.161, 104571 (2024). https://doi.org/10.1016/j.trc.2024.104571
- Yujin Kim, Hwasoo Yeo, Lisa Lim. Sustainable, walkable cities for the elderly: Identification of the built environment for walkability by activity purpose. Sustainable Cities and Society. Vol.100 (2024) https://doi.org/10.1016/j.scs.2023.105004
- Yeeun Kim, Hye-Young Tak, Sunghoon Kim, Hwasoo Yeo, A hybrid approach of traffic simulation and machine learning techniques for enhancing real-time traffic prediction, Transportation Research Part C (2024) https://doi.org/10.1016/j.trc.2024.104490
- Pengfein Liu, Jing Zhao, Fanlei Zhang, Hwasoo Yeo, Modeling decision-making process of drivers during yellow signal phase at intersections based on drift-diffusion model. Transportation Research Part F: Traffic Psychology and Behaviour (2024) https://doi.org/10.1016/j.trf.2024.07.020
- Chaemin Na, Hyunsoo Kim, Hwasoo Yeo. Graph Deep Learning Based Maximum Queue Length Prediction at Signalized Intersection. The 35th KKHTCNN Symposium on Civil Engineering (2024)
- Keunhee Cho, Jacob Choi, Jiwoo Kim, Rimsha Ahmed, Kunhee Choi, Hwasoo Yeo. Optimizing Micro-Mobility Parking to Address Rebalancing Concerns and Safety. The 35th KKHTCNN Symposium on Civil Engineering (2024)
- Phoebe Ho, Sujae Jeon, Yeonwoo Yu, Lindsay Park, Hwasoo Yeo, Kunhee Choi. Equity Considerations for Emerging Technologies in Transportation:A Comparative Study of Planning Practices in the United States and South Korea. The 35th KKHTCNN Symposium on Civil Engineering (2024)
- Sharon Kim, Hwasoo Yeo. Adaptive Route Planning for Accessible Transport: Combining Base and Flexible Routes in Demand-Responsive Systems. The 35th KKHTCNN Symposium on Civil Engineering. (2024)
- Sujae Jeon, Yeeun Kim, Hwasoo Yeo. An Adaptive Driving Behavior Model with Consideration for Surrounding Vehicle Dynamics. The 35th KKHTCNN Symposium on Civil Engineering (2024)
- Pei Jia Pok, Hwasoo Yeo, Soomin Woo. Optimization of Electric Vehicle Charging Decision Process Using Game Theory. The 35th KKHTCNN Symposium on Civil Engineering (2024)
- Hyejin Lee, Hwasoo Yeo, Traffic Queue Length Estimation and Prediction in Signalized Intersection using Sparse Vehicle Trajectory, MTFS 2024 (2024)
- Yeeun Kim, Seongjin Choi, Sujae Jeon, Hwasoo Yeo, Multi-level Traffic Simulation with Dynamic Simulation Level Assignment for Urban Network, TRC30 (2024)
- Hyunsoo Kim, Hye-young Tak, Hwapyeong Yu, Hwasoo Yeo, Hierarchical Traffic Signal Coordination with Priority-based Optimization via Deep Reinforcement Learning, TRC30 (2024)
- Minerva Bonilla, Junseok Kim, Deirdre Edward, Hwasoo Yeo. Machine Learning Predictive Model: Prioritizing Expenditures in Public Transportation based on Transportation Emissions. Construction Research Congress (2024)
- Tengfeng Lin, Hwasoo Yeo, Inhi Kim. Overcoming Data Sparsity in Traffic Speed Prediction: A variational Autoencoder Approach on Large-Scale Road Networks. The Korean Society of Intelligent Transport Systems (International part) (2024)
- Robert Fonod, Haechan Cho, Hwasoo Yeo, Nikolas Geroliminis. High-Precision Trajectory Extraction Using Advanced Computer Vision From a Multi-Drone Experiment in South Korea. Transportation Research Board Annual Meeting (2024)
- Yeeun Kim, Seongjin Choi, Sujae Jeon, Hwasoo Yeo. MULTI-LEVEL TRAFFIC SIMULATION USING DYNAMIC SIMULATION LEVEL ASSIGNMENT FOR URBAN NETWORK. Transportation Research Board Annual Meeting (2024)
- Hwapyeong Yu, Hwasoo Yeo. IMPACT OF ADAPTIVE CRUISE CONTROL ON HIGHWAY TRAFFIC BREAKDOWN AND RAMP METERING. Transportation Research Board Annual Meeting (2024)

**2023**

- Jeongyun Kim, Sehyun Tak, Jinwoo Lee, Hwasoo Yeo, Integrated design framework for on-demand transit system based on spatiotemporal mobility patterns, Transportation Research Part C (2023) https://doi.org/10.1016/j.trc.2023.104087
- Hyejin Lee, Haechan Cho, Byeongjoon Noh, Hwasoo Yeo, NAVIBox: Real-Time Vehicle-Pedestrian Risk Prediction System in an Edge Vision Environment, Electronics 12(20), 4311 (2023) https://doi.org/10.3390/electronics12204311
- 이주희, 김지후, 여화수. 전염병 유행과 대전광역시의 시내버스 수요의 회복탄력성 패턴을 이용한 지역 대중교통 인프라 불균형 연구. 대한교통학회지. 제 41권 제 7호 p.835 (2023.12)
- 조해찬, 윤여환, 여화수, 차량 블랙박스 카메라를 이용한 도시부 교통상태 추정, 한국ITS학회논문지, 제 22권 제 2호 p, 133 (2023. 04)
- 노병준, 조해찬, 이혜진, 가동호, 여화수. 컴퓨터 비전 기반의 횡단보도 내 차량-보행자 간 잠재적 충돌 위험 인식 방법 및 분석에 관한 연구. 대한교통학회지. 제 41권 제 1호 p.1 (2023.02)
- Hye-young Tak, Yeeun Kim, Sunghoon Kim, Hwasoo Yeo, a Hybrid Model for Real-Time Traffic Prediction with Augmented Historical Data using Traffic Simulation, IEEE ITSC (2023)
- Hyunsoo Kim, Zhixiong Jin, Hye-young Tak, Hwapyeong Yu, Hwasoo Yeo, Prioritized Phase Split Optimization for Coordinated Traffic Signal Control in Urban Network using Deep Reinforcement Learning, IEEE ITSC (2023)
- Haechan Cho, Yeohwan Yoon, Jihu Kim, Hwasoo Yeo, Urban Traffic State Estimation from Moving Camera for Real-time Application, The 6th International Conference on Artificial Intelligence in Information and Communication (2023)

**2022**

- Yesuel Kim, Hwasoo Yeo, Youngchul Kim, Estimating urban spatial temperatures considering anthropogenic heat release factors focusing on the mobility characteristics, Sustainable Cities and Society Vol 85, October 2022, 104073,. https://doi.org/10.1016/j.scs.2022.104073
- Zhixiong Jin, Jiwon Kim, Hwasoo Yeo, Seongjin Choi, Transformer-based map-matching model with limited labeled data using transfer-learning approach, Transportation Research Part C (2022), https://doi.org/10.48550/arXiv.2108.00439 학술지 DOI: https://doi.org/10.1016/j.trc.2022.103668
- Byeongjoon Noh, Hwasoo Yeo, A novel method of predictive collision risk area estimation for proactive pedestrian accident prevention system in urban surveillance infrastructure, Transportation Research Part C (2022), https://doi.org/10.1016/j.trc.2022.103570
- Byeongjoon Noh, Hansaem Park, Hwasoo Yeo, Analyzing vehicle-pedestrian interactions: combining data cube structure and predictive collision risk estimation model, Accident Analysis and Prevention, vol.165, 106539 (2022) https://www.sciencedirect.com/science/article/pii/S0001457521005704?dgcid=author DOI: https://doi.org/10.1016/j.aap.2021.106539
- 김유진, 노병준, 여화수. 도시환경정보 기반의 데이터 큐브 모델을 이용한 이륜차 사고의 다차원 요인 분석. 대한교통학회지. 제 40권 제 3호 p.358 (2022.06)
- Jiyoung Hwang, Byeongjoon Noh, Zhixiong Jin, Hwasoo Yeo, Asymmetric Long-Term Graph Multi-Attention Network for Traffic Speed Prediction, IEEE ITSC (2022)
- Zhixiong Jin, Beyongjoon Noh, Haechan Cho, Hwasoo Yeo, Deep Learning-based Approach on Risk Estimation of Urban Traffic Accidents, IEEE ITSC (2022)
- Haechan Cho, Hwasoo Yeo, Deep Learning based multi-camera vehicle tracking, The Korea Institute of ITS International Conference (2022)
- Hyejin Lee, Haechan Cho, Hwasoo Yeo, Real-time Warning System based on Vehicle-Pedestrian Risk Prediction in Edge Computing Environment, The Korea Institute of ITS International Conference (2022)
- Yeeun Kim, Hye-young Tak, Sunghoon Kim, Hwasoo Yeo, Real-Time Traffic Prediction Approach Based on Simulation and Machine Learning Techniques, The Korea Institute of ITS International Conference (2022)
- Tengfeng Lin, Zhixiong Jin, Hwasoo Yeo, Evaluation of Vulnerable Pedestrian Potential Risk at Intersection Based on Arrival Time Prediction using Deep Learning, The Korea Institute of ITS International Conference (2022)
- Zhixiong Jin, Jiwon Kim, Hwasoo Yeo, Seongjin, Transformer-based Map-matching Model with Limited Labeled Data using Transfer-Learning Approach, The Korea Institute of ITS International Conference (2022)
- Zhixiong Jin, Seongjin Choi, Hwasoo Yeo, TMM: Transformer-based Map-matching Model with Transfer Learning Approach, Transportation Research Board Annual Meeting (2022)
- Jinwon Yoon, Kyuree Ahn, Kanghoon Lee, Jinkyoo Park, Hwasoo Yeo, Transferable Multi-agent Traffic Signal Control considering Spatial Correlation between State Variables in Reinforcement Learning, Transportation Research Board Annual Meeting (2022)
- Jeongyun Kim, Hwasoo Yeo, Data-Driven Methodology for Designing On-Demand Transit Services, Transportation Research Board Annual Meeting (2022)

**2021**

- 김예은, 김성훈, 여화수, 기계학습과 시뮬레이션 기법을 융합한교통 상태 예측 방법 개발 연구. 한국ITS학회논문지, 제 20권 제 5호, 100-112 (2021.10) DOI: https://doi.org/10.12815/kits.2021.20.5.100
- Seongjin Choi, Jiwon Kim, Minju Park, Hwasoo Yeo, TRAJGAIL: Generating Urban Vehicle Trajectories using Generative Adversarial Imitation Learning, Transportation Research Board Annual Meeting (2021)
- Byeongjoon Noh, Dongho Ka, David Lee, Hwasoo Yeo, Analysis of Vehicle-Pedestrian Interactive Behaviors near Unsignalized Crosswalk, Transportation Research Board Annual Meeting (2021)
- Jinwon Yoon, Kyree Ahn, Jinkyoo Park, Hwasoo Yeo, Restricted Exploration Problem of Reinforcement Learning-based Traffic Signal Control Model and Development of Transferable Policy using Graph Neural Networks, Transportation Research Board Annual Meeting (2021)
- Sunghoon Kim, Monica Menendez, Hwasoo Yeo, Methodology to Increase the Flexibility in Inter-region Flow Control for Urban Traffic, Transportation Research Board Annual Meeting (2021)

## 특허

연구실 Patents의 등록 특허 가운데 2021년 10월 13일–2026년 10월 13일에 등록된 2항목이다. 발명자·제목·번호·등록일은 연구실 표기다.[^patents]

- Hwasoo Yeo, Donghoun Lee, Sehyun Tak, Vehicle Driving Management System, Client and Server Device for Vehicle Driving Management, Patent no. 10-2587119 (2023.10.04), Republic of Korea (등록일 2023-10-04)
- Hwasoo Yeo, Yeeun Kim. Method for Traffic Simulation considering Driver's Behabior and Road Section Risk and Safety-vulnerable Region Prediction System. Patent No. 10-2843362 (2025.08.01), Republic of Korea (등록일 2025-08-01)

## 수상과 선정

2021년 10월 13일–2026년 10월 13일의 연구실 소식 중 수상·선정 안내 13글과 학술지 부편집장 선임 안내 1글이다. 날짜는 상세 글의 게시일이며, 수상일이 본문에 별도로 적힌 경우 함께 표시했다. 상 이름과 등급은 연구실 표기다.[^news-index]

- 2026-10-01 · Sujae Jeon이 한국과학기술단체총연합회의 제36회 과학기술우수논문상을 받았다고 알렸다. 시상일은 2026년 9월 30일이며, 대한교통학회 추천 논문은 「A Two-Dimensional Lane-Changing Model Reflecting Asymmetric Driving Behavior」이다.[^n322]
- 2026-08-24 · Sujae Jeon의 대한교통학회 추천·수여 제26회 「Science and Technology Best Paper Award」 선정을 알렸다.[^n361]
- 2026-07-02 · 여화수 교수의 Transportation Research Part C: Emerging Technologies 부편집장 선임을 알렸다.[^n315]
- 2026-03-13 · Sujae Jeon이 대한교통학회 제94회 학술대회의 「Academic Award」 수상자로 선정됐다고 알렸다.[^n349]
- 2026-03-03 · 여화수 교수의 「KAIST Strategic Leadership Award」 수상을 알렸다.[^n324]
- 2025-12-08 · Chaemin Na가 홍콩 KKHTCNN에서 「Best Presenter Award」를 받았다고 알렸다.[^n335]
- 2025-09-29 · Yeonwoo Yu가 대한교통학회 학술대회에서 「Excellence Paper Presentation Award」를 받았다고 알렸다.[^n302]
- 2024-11-26 · Peijia Pok이 제35회 KKHTCNN에서 「Best Presentation Award」를 받았다고 알렸다.[^n375]
- 2024-11-12 · Hyunsoo Kim이 대한교통학회 제91회 학술대회에서 「Priority-Based Hierarchical Traffic Signal Optimization Using Deep Reinforcement Learning」 발표로 「Best Paper Presentation Award」를 받았다고 알렸다.[^n355]
- 2024-03-22 · 여화수 교수가 KAIST 대학원생인권센터의 「KAIST Excellent Ethical Professor Award」 최우수상을 받았다고 알렸다.[^n350]
- 2023-10-16 · Tengfeng Lin이 대한교통학회와 Korea Planning Association의 공동 학술대회에서 신호등 없는 교차로의 보행자 위험 평가 논문으로 「Best Paper Award」를 받았다고 알렸다.[^n343]
- 2022-12-07 · 여화수 교수가 KAIST Q-Day에서 「Creative Lecture Award」를 받았다고 알렸다.[^n301]
- 2022-06-29 · 한국ITS학회 학술대회에서 Haechan Cho의 「Deep Learning-based multi-camera vehicle tracking」 포스터가 「outstanding posters」 가운데 하나로 선정됐다고 알렸다.[^n368]
- 2022-01-11 · Tengfeng Lin·Zhixiong Jin·Seongjin Choi·여화수 교수 팀이 「Transportation Forecasting Competition (TRANSFOR 22) Data Challenge」에서 3위를 기록했다고 알렸다.[^n339]

## 소식

같은 기간 연구실 소식 중 논문 게재, 연구 자료 공개, 기술 소개와 연구협약을 다룬 15글이다. 날짜는 상세 글의 게시일이다.[^news-index]

- 2025-12-05 · Hye-young Tak의 Transportation Research Part C: Emerging Technologies 논문 게재를 알렸다.[^n319]
- 2025-06-24 · Hwapyeong Yu의 Transportmetrica B: Transport Dynamics 논문 게재를 알렸다.[^n325]
- 2025-04-28 · 고속도로 교통 흐름과 차량 호출 서비스의 지역 간 차량 재배치를 다룬 논문들이 ANT 2025의 Procedia Computer Science에 게재됐다고 알렸다.[^n345]
- 2025-04-09 · Jinwon Yoon의 「Decentralized and Communication-Based Multi-Agent Traffic Signal Control Model Employing a Graph Representation for the State」가 IEEE Transactions on Intelligent Transportation Systems에 온라인 선공개됐다고 알렸다.[^n363]
- 2025-03-18 · EPFL LUTS Lab과 함께 만든 Songdo Traffic·Songdo Vision 자료의 공개를 알렸다. 드론 영상에서 지리 좌표가 붙은 차량 경로를 추출하는 영상 분석 알고리즘을 개발했으며, 약 70만 개 차량 경로와 차량 영역 표시 30만 개를 소개했다.[^n348]
- 2024-11-18 · Hwapyeong Yu의 Transportation Research Part C 논문 게재를 알렸다.[^n331]
- 2024-09-30 · Yujin Kim의 「Integrating visual and community environments in a motorcycle crash and casualty estimation」 논문이 Accident Analysis & Prevention에 게재됐다고 알렸다.[^n333]
- 2024-03-21 · Yeeun Kim의 Transportation Research Part C 논문 게재를 알렸다.[^n312]
- 2024-02-05 · Yeeun Kim과 Hye-young Tak의 Transportation Research Part C 논문 게재를 알렸다.[^n337]
- 2023-03-28 · Jeongyun Kim의 Transportation Research Part C 논문 게재를 알렸다.[^n366]
- 2023-03-15 · 여화수 교수가 KAIST와 TNO의 연구·과학기술 분야 학술협력을 위한 양해각서에 서명했다고 알렸다.[^n338]
- 2022-10-12 · 송도에서 여러 대의 드론을 활용한 도시 교통 자료 수집과 영상 기반 차량 경로 추출·자료 공개 계획을 소개했다.[^n328]
- 2022-04-28 · Zhixiong의 Transportation Research Part C 논문 게재를 알렸다.[^n364]
- 2022-02-14 · Byeongjoon Noh의 Transportation Research Part C 논문 게재를 알렸다.[^n310]
- 2022-01-18 · Byeongjoon Noh의 Accident Analysis & Prevention 논문 게재를 알렸다. 횡단보도 감시 영상 등 여러 자료로 실제 충돌 없이 도로 안전 수준을 평가하는 분석 틀을 소개했다.[^n305]

## 연락과 위치

- 교수 오피스: 학과 소개 W15동 411호, 연구실 About W16-408[^dept][^about]
- 주소: 34141 대전광역시 유성구 대학로 291, KAIST 건설및환경공학과[^about]
- 교수·연구실 전화: +82-42-350-3634, 팩스: +82-42-350-3610[^about]
- 교수 이메일: hwasoo@kaist.ac.kr[^about]
[^dept]: KAIST 건설및환경공학과, 여화수 교수 소개. <https://cee.kaist.ac.kr/boards/view/professor/43/sc_category/1> 관측 2026-11-06.
[^about]: KAIST AI x Mobility Lab, About: 교수·구성원·졸업생·연락처. <https://www.aimobility.kaist.ac.kr/about> 관측 2026-11-06.
[^research]: KAIST AI x Mobility Lab, Research: Mobility + AI, Smart Cities and Urban Informatics, Predictive Analytics. <https://www.aimobility.kaist.ac.kr/research> 관측 2026-11-06.
[^pubs]: KAIST AI x Mobility Lab, Publications: 국제·국내 학술지, 논설, 책 장과 교재 목록. <https://www.aimobility.kaist.ac.kr/publications> 관측 2026-11-06.
[^conference]: KAIST AI x Mobility Lab, Conference Papers: 국제학회 목록. <https://www.aimobility.kaist.ac.kr/conference-papers> 관측 2026-11-06.
[^patents]: KAIST AI x Mobility Lab, Patents: 출원·등록 목록. <https://www.aimobility.kaist.ac.kr/patents> 관측 2026-11-06.
[^news-index]: KAIST AI x Mobility Lab, AI x Mobility Lab News 소식 게시판. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news> 개별 글의 상세 주소는 각 항목 각주에 표시했다. 관측 2026-11-06.
[^bibliography]: OpenAlex, Hwasoo Yeo의 논문별 DOI·저자·발표처·출판일 기록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p1]: Y. Kim, S. Choi, S. JEON, H. Yeo, IEEE Transactions on Intelligent Transportation Systems (2026). <https://doi.org/10.1109/tits.2026.3671220> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p2]: T. Lin, Z. Jin, H. Yeo, I. Kim, IEEE Transactions on Intelligent Transportation Systems (2026). <https://doi.org/10.1109/tits.2026.3661062> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p3]: J. Kim, Y. Kim, H. Yeo, IET Intelligent Transport Systems (2025). <https://doi.org/10.1049/itr2.70134> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p4]: H. Yu, H. Yeo, Transportmetrica B Transport Dynamics (2025). <https://doi.org/10.1080/21680566.2025.2519630> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p5]: J. Yoon 외, H. Yeo, IEEE Transactions on Intelligent Transportation Systems (2025). <https://doi.org/10.1109/tits.2025.3548945> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p6]: Y. Kim, H. Yeo, L. Lim, Sustainable Cities and Society (2023). <https://doi.org/10.1016/j.scs.2023.105004> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p7]: P. Pok, S. Woo, H. Yeo, ACM Sustainability Week (2026). <https://doi.org/10.1145/3765611.3815391> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^p8]: H. Cho, Y. Yoon, J. Kim, H. Yeo, International Conference on Artificial Intelligence in Information and Communication (ICAIIC) (2023). <https://doi.org/10.1109/icaiic57133.2023.10066969> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5033786777,publication_year:2021-2026> 관측 2026-11-06.
[^n301]: KAIST AI x Mobility Lab, Prof. Yeo receives an award on KAIST Q-Day. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/009392be-a487-4ca8-99dc-f68f85f3f5dd> 게시 2022-12-07, 관측 2026-11-06.
[^n302]: KAIST AI x Mobility Lab, AixMobility at Korean Society of Transportation Conference 2025. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/025917c6-fc05-49c8-aa91-22e63e2256b5> 게시 2025-09-29, 관측 2026-11-06.
[^n305]: KAIST AI x Mobility Lab, New paper published in Accident Analysis & Prevention (AAP). <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/0fae2bfa-ec54-4d16-88f5-cc9cfc2698cb> 게시 2022-01-18, 관측 2026-11-06.
[^n310]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/2f5b4d21-bfe2-4528-9f50-a5fa4c02df18> 게시 2022-02-14, 관측 2026-11-06.
[^n312]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/3e383e9c-0351-45a5-b2df-933485d80fd0> 게시 2024-03-21, 관측 2026-11-06.
[^n315]: KAIST AI x Mobility Lab, Professional Achievement: Prof. Hwasoo Yeo appointed as Associate Editor of Transportation Research Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/41ad8bcc-4c90-4574-ad92-a1d0b28c7ffd> 게시 2026-07-02, 관측 2026-11-06.
[^n319]: KAIST AI x Mobility Lab, New paper published in Transportation Research Part C: Emerging Technologies. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/4a794acd-ad0c-4cb5-9f48-c62d69703b3a> 게시 2025-12-05, 관측 2026-11-06.
[^n322]: KAIST AI x Mobility Lab, [Award News] Ph.D. Candidate Sujae Jeon Receives the 36th Science and Technology Excellence Paper Award. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/4ec0632c-ed9b-4f47-9d54-6a815e8d3be1> 게시 2026-10-01, 관측 2026-11-06.
[^n324]: KAIST AI x Mobility Lab, Congratulations to our Professor on Receiving the KAIST Strategic Leadership Award. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/543c7ea6-5303-4275-839f-1b2f5cb5535e> 게시 2026-03-03, 관측 2026-11-06.
[^n325]: KAIST AI x Mobility Lab, New paper published in Transportmetrica B: Transport Dynamics. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/55c8f7b3-36b5-4180-915c-cd69f9dee736> 게시 2025-06-24, 관측 2026-11-06.
[^n328]: KAIST AI x Mobility Lab, Drones in Songdo. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/58db96f4-4750-40ce-ba14-e66364c9ee04> 게시 2022-10-12, 관측 2026-11-06.
[^n331]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/647a9a71-3df9-477d-bf79-c2782a530eec> 게시 2024-11-18, 관측 2026-11-06.
[^n333]: KAIST AI x Mobility Lab, New paper published in Accident Analysis & Prevention. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/69ff5112-e875-4b03-9f71-f3685a971fb7> 게시 2024-09-30, 관측 2026-11-06.
[^n335]: KAIST AI x Mobility Lab, AIxMobility @ KKHTCNN Hongkong. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/730fc740-3ea1-4cc9-b1bb-4bbca97b7c52> 게시 2025-12-08, 관측 2026-11-06.
[^n337]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/77a14c6e-0189-4af2-9e76-b5785978b419> 게시 2024-02-05, 관측 2026-11-06.
[^n338]: KAIST AI x Mobility Lab, KAIST & TNO MOU. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/77aceacb-4c7c-4383-b5cb-e5a540b639e1> 게시 2023-03-15, 관측 2026-11-06.
[^n339]: KAIST AI x Mobility Lab, 3rd Place in Transportation Forecasting Competition (TRANSFOR 22) Data Challenge. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/7f9847b0-e8bf-4af5-9092-0d0f7725aae0> 게시 2022-01-11, 관측 2026-11-06.
[^n343]: KAIST AI x Mobility Lab, Korean Society of Transportation & Korea Planning Association joint conference. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/90f148ca-a5cc-45e1-a992-c899cd7d624e> 게시 2023-10-16, 관측 2026-11-06.
[^n345]: KAIST AI x Mobility Lab, ANT 2025. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/92df1636-aec2-4075-b4ae-256c8288c1c0> 게시 2025-04-28, 관측 2026-11-06.
[^n348]: KAIST AI x Mobility Lab, Songdo Traffic and Songdo Vision datasets available online. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/9aabe36c-32d5-4644-a88b-cc143d229a04> 게시 2025-03-18, 관측 2026-11-06.
[^n349]: KAIST AI x Mobility Lab, Congratulations to Sujae Jeon on KST Academic Award. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/9cdd8dba-3b23-4ae6-851a-0a475935a446> 게시 2026-03-13, 관측 2026-11-06.
[^n350]: KAIST AI x Mobility Lab, Prof. Yeo receives KAIST Excellent Ethical Professor Award from the Graduate Student Human Rights Center. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/a055f24d-e7a4-49f0-9187-f3622a9030a9> 게시 2024-03-22, 관측 2026-11-06.
[^n355]: KAIST AI x Mobility Lab, the 91st KST Conference Best Paper Award (1). <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/a96c35a6-5a93-4ef7-bb51-b9a48fa185cd> 게시 2024-11-12, 관측 2026-11-06.
[^n361]: KAIST AI x Mobility Lab, Sujae Jeon Receives the 26th Science and Technology Best Paper Award!. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/b3023aa2-7c74-4d0f-8d7c-8e7913903bd6> 게시 2026-08-24, 관측 2026-11-06.
[^n363]: KAIST AI x Mobility Lab, Early Access of article in IEEE Transactions on ITS available. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/bb838ae3-bf0d-4c1a-a4e2-3a66730c6797> 게시 2025-04-09, 관측 2026-11-06.
[^n364]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/bcdf23b2-e2d1-411b-9f3d-e07b59e02f59> 게시 2022-04-28, 관측 2026-11-06.
[^n366]: KAIST AI x Mobility Lab, New paper published in TR Part C. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/d92a8004-52d8-4d60-8af0-771b4937bb00> 게시 2023-03-28, 관측 2026-11-06.
[^n368]: KAIST AI x Mobility Lab, ITS Conference. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/e480d706-e98b-43b3-8f95-2f5d9f881a57> 게시 2022-06-29, 관측 2026-11-06.
[^n375]: KAIST AI x Mobility Lab, Peijia Pok (Ph.D candidate) receives the Best Presentation Award at the 35th KKHTCNN. <https://www.aimobility.kaist.ac.kr/group/ai-x-mobility-lab-news/discussion/fbc8e029-85b7-43e7-b1d9-d0e34b95dff1> 게시 2024-11-26, 관측 2026-11-06.

# KAIST Transportation and Infrastructure Lab

**KAIST 건설및환경공학과 · 이진우 부교수**

- 분야: 교통 인프라 계획·운영, 공유·전기·다중수단 모빌리티, 도로 시설 관리와 재난 대응
- 대분야: 건설·도시·인프라, 컴퓨팅·AI
- 태그: 교통·도시 계획[^dept][^research], 강화학습[^research], 도심 항공 모빌리티(UAM)[^research]
- 홈페이지: <https://lee.kaist.ac.kr>
- 근거와 출처: [KAIST Transportation and Infrastructure Lab 근거 페이지](lee-sources.md)

> 사람과 차량의 이동을 분석해 충전소·차고지·도로 같은 기반 시설을 계획하고, 교통 서비스와 시설의 운영·유지·재난 대응을 함께 연구하는 연구실이다.[^dept][^research]

## 무엇을 연구하나

이진우 부교수가 이끄는 연구실은 모빌리티(사람과 물자의 이동 및 이를 제공하는 수단·서비스)와 교통 인프라(이동을 뒷받침하는 시설과 체계)를 함께 다룬다. 학과 소개는 전기·공유·자율·다중수단 모빌리티의 모형을 만들고 터미널·모빌리티 허브·역·차고지·주차장 등의 역할에 집중한다고 설명한다.[^dept][^research]

첫 갈래는 도시의 통행 수요에 맞춰 교통 서비스와 시설을 함께 정하는 연구다. 연구 소개는 수요응답형 교통(Demand-Responsive Transit, DRT: 이용자의 이동 요청에 맞춰 운행을 조정하는 교통 서비스)의 계획·운영과 대규모 운행용 강화학습 알고리즘을 연구 주제로 적는다.[^research] 강화학습은 행동의 결과로 받는 보상을 바탕으로 행동 선택 규칙을 배우는 방법이다. 대표 논문은 충전소까지 가는 시간과 대기시간을 함께 계산해 충전시설을 배치하고, 자율 호출형 차량을 구역 사이와 구역 안에서 재배치하는 방법을 다룬다.[^p1][^p3]

둘째 갈래는 이동 수단의 전동화와 도심 항공 교통이다. 전기버스의 차량 수·배터리 용량·충전시설을 함께 정해 비용과 온실가스 배출을 비교한다.[^p2] 도심 항공 모빌리티(Urban Air Mobility, UAM: 도시 안과 주변에서 사람·화물을 나르는 항공 교통)는 환경·사회적 영향과 여객·물류 서비스의 계획·운영을 연구한다.[^research] 대표 논문에서는 기체와 이착륙장 공간, 충전기 수를 운항·충전·대기·재배치 결정과 함께 정한다.[^p4]

셋째 갈래는 시설을 언제 점검·보수·재건할지와 재난이 일어났을 때 이동 체계를 어떻게 유지할지다. 연구 소개는 도로·교량·철도·공항의 상태 관찰과 관리 결정, 인공지능과 로봇을 이용한 도로 포장 보수, 해수면 상승과 산불 위험 아래의 시설 계획을 다룬다. 대표 논문은 과적 차량의 우회 행동을 반영한 계량시설(주행 중인 차량의 무게를 재는 시설) 배치와 산불로 도로가 닫힐 때의 대피 취약성을 분석한다.[^research][^p5][^p6]

## 주요 연구 주제

### 여러 교통수단과 공유 서비스의 계획

다중수단 교통(서로 다른 교통수단을 함께 이용하는 이동 체계)에서 통행의 연결 순서와 수단 사이의 관계를 분석한다. 공유 모빌리티와 대중교통의 공동 계획, 로보택시(자율주행으로 운행하는 호출형 택시)의 주차·충전시설 배치와 기존 교통 체계와의 연결이 연구 대상이다.[^research] 도시 특성과 교통수단별 이용 비율의 관계를 분석한 대표 논문은 도시를 승용차·대중교통·자전거 중심 집단으로 나누고 인구사회·환경·교통계획 요인의 영향을 살폈다.[^p7]

### 충전시설과 항공 교통의 계획·운영

전기버스와 공유 차량의 전동화, 전기 모빌리티 거점의 연결망을 계획한다.[^research] 공공 급속충전시설 연구는 충전소 밀도와 충전기 수, 지역별 통행·충전 수요가 이용자의 이동시간과 대기시간에 미치는 영향을 함께 다룬다.[^p1] 도심 항공 교통에서는 여객과 물류 서비스의 계획·운영 및 환경·사회적 영향을 주요 대상으로 든다.[^research]

### 시설의 상태 관찰과 보수 결정

자율주행 차량과 일반 차량이 섞인 도로의 전용차로·경로 계획, 자동화 트럭의 물류, 차량 센서 자료를 이용한 도로 포장·교량 관리를 연구한다. 또한 대규모 시설 연결망에서 상태 관찰·점검·유지보수·재건을 함께 정하는 강화학습과 자동 상태 관찰, 인공지능·로봇 기반 도로 포장 보수 체계를 연구 주제로 제시한다.[^research] 주행 중 계량시설의 배치는 도로 유지비와 운전자의 경로 선택이 서로 영향을 주는 문제로 다룬다.[^p5]

### 재난 대응과 교통 자료 분석

재난 전후의 시설 관리와 복구, 해수면 상승·산불 위험 아래의 시설 계획, 도로망의 취약성과 회복 능력을 연구한다. 게임 이론(여러 주체가 서로의 선택을 고려해 행동하는 상황을 분석하는 방법)과 도로 연결 관계의 분석을 활용하며, 산불 대피 연구에서는 도로 폐쇄에 따른 고립 차량과 대피시간을 살폈다. 교통 속도 예측에서는 도로 사이의 정체 전파를 신경망에 반영해 시간에 따라 바뀌는 관계를 다룬다.[^research][^p6][^p8]

## 대표 논문

KAIST 재직 시기의 논문에서 충전시설·전기버스, 공유·항공 모빌리티, 시설 관리·재난 대응, 도시 이동 분석·교통 예측을 고르게 골랐다. 연도는 연구실의 학술지 목록 표기다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Urban public charging infrastructure planning for electric vehicles: A continuum approximation approach](https://doi.org/10.1016/j.trd.2025.104605) · Transportation Research Part D Transport and Environment | 충전소까지 가는 시간과 충전 대기시간을 함께 계산해 도시 공공 급속충전시설의 배치를 정하는 방법을 제안했다. 지역별 충전 수요와 도로·교통 여건의 차이를 반영하고, 충전소 밀도·충전기 수·충전소 배정 규칙이 서비스 수준에 미치는 영향을 분석했다. 뉴욕시 사례에서는 기존 시설보다 서비스 수준을 개선할 수 있는 계획을 보였다.[^p1] | 1저자 Yichan An, 마지막 저자 Jinwoo Lee |
| 2 | 2023 | [Optimal battery electric bus planning and its economic and environmental impacts](https://doi.org/10.1016/j.trd.2023.103821) · Transportation Research Part D Transport and Environment | 전기버스의 차량 수, 배터리 용량, 충전시설을 함께 정하면서 전체 비용과 온실가스 배출을 줄이는 의사결정 틀을 제안했다. 운행의 불확실성을 고려하고 대기행렬 이론으로 계산 방법을 만들었다. 수치 사례에서 최적으로 계획한 전기버스 체계는 내연기관·자체 충전 하이브리드 버스 체계보다 비용이 높았지만 환경 편익도 가장 컸다.[^p2] | 1저자 Jinwoo Lee, 공저자 Seungmin Oh·Sanghoon Son |
| 3 | 2023 | [Real-Time Operations of Autonomous Mobility- on-Demand Services With Inter-and Intra-Zonal Relocation](https://doi.org/10.1109/tiv.2023.3299692) · IEEE Transactions on Intelligent Vehicles | 공유 자율주행 차량이 호출을 받지 않고 기다릴 때 어느 곳으로 이동시킬지 실시간으로 정하는 방법을 제안했다. 전체 구역 사이의 재배치와 각 구역 안의 재배치를 나눠 계산 부담을 줄였다. 기존 택시를 공유 자율주행 차량으로 바꾼다는 가정 아래 대전의 실제 택시 자료로 모의실험했고, 이용자와 운영기관의 비용을 함께 줄일 수 있음을 보였다.[^p3] | 1저자 Jiho Yeo, 마지막 저자 Jinwoo Lee |
| 4 | 2025 | [An optimization framework for urban air mobility (UAM) planning and operations](https://doi.org/10.1016/j.jairtraman.2024.102720) · Journal of Air Transport Management | 도심 항공 교통에 필요한 전기 수직이착륙 기체·이착륙장 공간·충전기 수와 운항·충전·대기·재배치 상태를 함께 정하는 의사결정 틀을 제안했다. 시공간별 수요와 비용 차이를 반영했으며, 수도권의 가상 이착륙장들을 대상으로 서비스 목표와 충전 속도가 계획에 미치는 영향을 분석했다. 수요와 전력 소비가 달라지는 모의실험으로 계획의 안정성도 살폈다.[^p4] | 1저자 Heeseung Shon, 마지막 저자 Jinwoo Lee |
| 5 | 2024 | [Optimal Weigh-in-Motion Planning for Multiple Stakeholders](https://doi.org/10.3390/systems12120557) · Systems | 과적 차량이 단속시설을 피해 다른 길을 고르는 행동까지 고려해 주행 중 차량 무게를 재는 시설의 위치를 정했다. 정부·도로 관리기관·운전자의 서로 다른 목표를 모형에 담고, 시설을 설치하는 쪽의 도로 유지비와 운전자의 통행비용을 함께 고려했다. 각 배치안에서 차량이 어떤 경로로 나뉘는지 계산하고 게임 이론으로 주체 사이의 상호작용을 표현했다.[^p5] | 1저자 Yunkyeong Jung, 마지막 저자 Jinwoo Lee |
| 6 | 2022 | [How to Measure the Network Vulnerability of Cities to Wildfires: Cases in California, U.S.A.](https://doi.org/10.1177/03611981221095516) · Transportation Research Record Journal of the Transportation Research Board | 도시의 도로 연결 상태와 산불 때의 대피 모의실험을 결합해 산불에 대한 도로망 취약성을 평가하는 틀을 제안했다. 캘리포니아 세 도시에서 도로 일부가 무작위로 닫히는 경우의 고립 차량 수와 대피시간을 살폈다. 비교 대상 가운데 Paradise는 도로 연결성이 가장 나빴고 도로 폐쇄에 가장 민감해, 두 분석에서 가장 취약한 도시로 나타났다.[^p6] | 1저자 Jeongin Yun, 마지막 저자 Jinwoo Lee |
| 7 | 2022 | [What cities have is how people travel: Conceptualizing a data-mining-driven modal split framework](https://doi.org/10.1016/j.cities.2022.103902) · Cities | 도시의 환경·인구사회·교통계획 특성이 교통수단별 이용 비율과 어떤 관계를 갖는지 분석하는 틀을 제안했다. 세계 도시들을 승용차·대중교통·자전거 중심 무리로 나누고 의사결정나무로 특성들의 결합 영향을 살폈다. 인구사회 요인의 영향이 가장 컸으며 인구밀도와 고용률, 연료세와 요금, 날씨가 이동수단 선택과 관련되는 양상을 제시했다.[^p7] | 1저자 Sujin Lee, 공저자 Jinwoo Lee, 마지막 저자 Euiyoung Kim |
| 8 | 2026 | [Incorporating traffic propagation impacts into dynamic graph diffusion convolutional network for traffic speed prediction](https://doi.org/10.1080/15472450.2026.2695352) · Journal of Intelligent Transportation Systems | 도로 사이의 거리와 연결 여부뿐 아니라 정체가 실제로 얼마나 전파되는지를 반영해 교통 속도를 예측하는 신경망을 제안했다. 시간에 따라 바뀌는 도로 사이 관계를 반영하고 관련이 적은 연결을 덜어 냈다. 서울의 실제 교통 자료로 평가한 결과 기준 모형들보다 예측 성능이 좋았으며, 특히 장기 예측에서 개선을 보였다.[^p8] | 1저자 Heeseung Shon, 마지막 저자 Jinwoo Lee |

## 교수와 전문 분야

이진우 부교수는 KAIST 건설및환경공학과 학사(2010), UC Berkeley 건설및환경공학 석사(2012)·박사(2015)를 받았다. New York University Abu Dhabi 박사후연구원(2015–2017)과 Hong Kong Polytechnic University 연구조교수(2017–2019)를 거쳐, KAIST 조천식모빌리티대학원 조교수(2019–2023)·부교수(2023–2024)를 지냈고 2024년부터 건설및환경공학과 부교수다. 연구실의 경력 소개에는 2023년부터 녹색성장지속가능대학원 Affiliated Professor도 적혀 있다.[^dept][^members]

학과 소개의 전문 분야는 교통 인프라, 전기·공유·자율·다중수단 모빌리티, 대중교통과 수요응답 모빌리티, 지속가능 교통과 교통공학이다. 최근 대표 논문에서는 충전시설·전기버스의 계획, 공유 차량·항공 교통의 운영, 이해관계자 행동을 반영한 시설 배치, 재난 때의 도로망 분석으로 이어진다.[^dept][^p1][^p2][^p3][^p4][^p5][^p6] 연구실은 2025년부터의 산업 경력으로 ROVOROAD의 Chief Technology Officer와 Studio Galilei의 Directory of Technology Innovation을 적는다.[^members]

## 응용 분야

공공 급속충전시설과 전기버스 도입 계획, 호출형 공유 차량의 재배치, 도심 항공 교통의 시설·운항 계획, 과적 단속시설 배치와 도로 유지보수, 재난 대피 계획이 응용 대상이다. 연구실은 Studio Galilei와의 수요응답형 교통 연구 및 Rovoroad와의 인공지능·로봇 기반 도로 포장 보수 연구를 소개한다.[^research][^p1][^p2][^p3][^p4][^p5][^p6]

## 구성원

연구실 Members 페이지의 교수 외 현재 구성원 12명으로, 박사후연구원 2명, 박사과정 3명, 석사과정 7명이다. 과정과 연구 주제는 연구실 표기다. 대표 논문의 전체 저자 목록과 이름이 일치하면 같은 이름의 저자를 같은 사람으로 보아 참여 번호를 표시했다. 기준은 2026-11-06이다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Linlin Zhang | 박사후연구원 | Mobility innovation adoption; Travel behavior and accessibility; Charging behavior; Travel satisfaction |  |
| Yichan An | 박사후연구원 | Charging infrastructure planning for electric vehicles; Continuum approximation modeling; Agent-based simulations; Modula vehicle systems | 1 |
| Jeongin Yun | 박사과정 | Dedicated lane and road planning for mixed traffic with autonomous vehicles; Agent-based simulations of mixed traffic; Disaster evacuation strategies | 6 |
| Yoojin Kim | 박사과정 | Mobility service and system design; Greenhouse gas emissions from robotaxis; Demand Responsive Transit (DRT) for sustainability |  |
| Yunkyeong Jung | 박사과정 | Interaction between ground logistics and pavement systems; Multi-criteria and multi-scale infrastructure decisions; Automated trucks | 5 |
| Benedict Uy Fabia | 석사과정 | Macroscopic Mobility Hierarchy (MMH) analysis of multimodal public transit systems; Robotaxi and UAM; Demand Responsive Transit (DRT) |  |
| Jaemin Shin | 석사과정 | Physical-AI–based transportation infrastructure asset management; Robotic pavement repair system |  |
| Kyunghoon Shin | 석사과정 | Analytical modeling of multi-stakeholder transportations systems; POMDP for infrastructure network management |  |
| Timofey Viktorovich Kim | 석사과정 | Walkability in urban mobility systems |  |
| Gyukang Kim | 석사과정 | Robotaxi planning and operations |  |
| Hahyun Cho | 석사과정 | Transit theories |  |
| Sangwook Park | 석사과정 | RL for optimal transit planning and operations |  |

## 졸업생과 이전 구성원

Members 페이지 Alumni의 8명과 Former Researchers의 3명이다. 학위·연도·진로는 연구실 표기이며, 이전 연구원 3명은 학위와 진로 칸이 비어 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaehoon Han | M.S. (2022) | Samsung Electronics |
| Sanggyu Kim | M.S. (2023) | Korea Institute of Science and Technology Information (KISTI) |
| Seungmin Oh | M.S. (2023) | Ph.D. Student at KAIST |
| Heeseung Shon | Ph.D. (2023) | Postdoctoral Researcher at Civil, Materials, and Environmental Engineering, University of Illinois at Chicago (UIC) |
| Myungkeun Jeong | M.S. (2023) | Hyundai Mobis |
| Eunji Lee | M.S. (2025) | LG Electronics |
| Sua Keum | M.S. (2025) |  |
| Bomi Kim | M.S. (2026) | Ph.D. Student at KAIST |
| Byul Kang |  |  |
| Aya Selmoune |  |  |
| Haebin Park |  |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 두 연구 갈래와 Members의 개인별 Research Papers에 게시된 학술지 논문 27편과 학회 항목 13편이다. 제목·저자·발표처와 연도는 연구실 표기다. 학술지 목록의 accepted는 「게재 승인」, 학회의 Accepted for presentation은 발표처 뒤 「채택」으로 표시했다. 게재 승인 항목은 누리집에 적힌 연도에 두었다.[^pubs][^members]

**2026**

- Fabia, B. and Lee, J., 2026. Macroscopic Equity Analysis Framework in Urban Multimodal Mobility Systems. Journal of Public Transportation, 게재 승인.
- An, Y., Jang, S., Park, H. and Lee, J., 2026. Influencing Factors in Personal Mobility Device Accident Severity in Korea. KSCE Journal of Civil Engineering, p.100732. DOI: 10.1016/j.kscej.2026.100732.
- Shon, H., Kim, S., Shin, Y., Yoon, Y. and Lee, J., 2026. Incorporating traffic propagation impacts into dynamic graph diffusion convolutional network for traffic speed prediction. Journal of Intelligent Transportation Systems, pp.1-17. DOI: 10.1080/15472450.2026.2695352.
- Yun, J., Oh, S. and Lee, J., 2026. Optimal dedicated lane management for mixed traffic with connected and autonomous vehicles accounting for heterogeneous headways and speeds. Transportation Research Part E: Logistics and Transportation Review, 207, p.104588.
- Baek, S., Moon, J., Yun, J., Shin, C., Lee, J. and Park, J., 2026. Estimating Capacity Adjustment Factors for Highway Basic Segments under Autonomous Vehicle Penetration. Journal of Korean Society of Transportation, 44(1), pp.86-98.
- An, Y., Lee, E. and Lee, J., 2026. An Optimisation Framework for Shared Autonomous Electric Vehicles as Mobile Energy Storage Systems. IET Intelligent Transport Systems, 20(1), e70215.
- Obonguta, F., Lee, J. and Mizutani, D., 2026. Simultaneous optimization of road intervention and overloading penalty policies for user cost minimization. Transportation Research Interdisciplinary Perspectives, 36, p.101849.
- An, Y., Keum, S., Lee, K, Sohn, H. and Lee, J., 2026. Impact Analysis of Non-Stop Trains on Passenger Travel Time and Optimal Planning. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- Kang, M., An, Y., Kim, H. and Lee, J., 2026. Joint Planning of Parking and Charging Infrastructure for Shared Autonomous Electric Vehicles. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- Lee, K.W., Kim, B., An, Y., Cho, H. and Lee, J., 2026. An Artificial Intelligence Approach for Automated Pavement Distress Detection Using Drone and Vehicle-Mounted Cameras. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- An, Y., Lee, E., Kim, H. and Lee, J., 2026. Optimal Operations of Shared Autonomous Electric Vehicles as Mobile Energy Storage Systems. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- Jung, Y. and Lee, J., 2026. Optimal Weigh-In-Motion Planning Using Game Theory. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- Jung, Y., Mizutani, D., and Lee, J., 2026. Optimal Route Planning for Autonomous Trucks in Pavement Management Systems. Transportation Research Board (TRB) 105th Annual Meeting (채택)
- Fabia, B. and Lee, J., 2026. Macroscopic Equity Analysis Framework in Urban Multimodal Mobility Systems. Transportation Research Board (TRB) 105th Annual Meeting (채택)

**2025**

- An, Y., Chow, J.Y.J., Woo, S. and Lee, J., 2025. Urban Public Charging Infrastructure Planning for Electric Vehicles: A Continuum Approximation Approach. Transportation Research Part D: Transport and Environment, 141, p.104605. DOI: 10.1016/j.trd.2025.104605.
- Shon, H. and Lee, J., 2025. An optimization framework for urban air mobility (UAM) planning and operations. Journal of Air Transport Management, 124, p.102720. DOI: 10.1016/j.jairtraman.2024.102720.
- An, Y., Papakonstantinou, I., Son, S. and Lee, J., 2025. Evaluating planning and operational policies for urban public electric vehicle charging infrastructure. International Journal of Sustainable Transportation, 19(8), pp. 730–748. DOI: 10.1080/15568318.2024.2390450.
- Jung, Y., Mizutani, D., and Lee, J., 2025. Weigh-In-Motion Placement for Overloaded Truck Enforcement Considering Traffic Loadings and Disruptions. Sustainability. 게재 승인. DOI: 10.3390/su17030826.
- An, Y., Chow, J.Y.J., Woo, S. and Lee, J., 2025. A Continuum Approximation Approach for Optimal Planning of Urban Public Charging Infrastructure for Electric Vehicles. Transportation Research Board (TRB) 104th Annual Meeting (채택)
- Yun, J., Kim, S., Kim, D. and Lee, J., 2025. Evaluation of Equivalent Property Damage Only (EPDO) Weight Sets for Hotspot Identification: A Case Study on Korean Expressways. Case Studies on Transport Policy, 101531. (presented at Transportation Research Board 104th Annual Meeting). DOI: 10.1016/j.cstp.2025.101531.
- Oh, S., Yun, J. and Lee, J., 2025. Optimal Management of Two Dedicated Lane Types for Mixed Highway Traffic with Connected and Autonomous Vehicles. Transportation Research Board (TRB) 104th Annual Meeting (채택)

**2024**

- Shon, H., Kim, S. and Lee, J., 2024. Optimal planning of urban air mobility systems accounting for ground access trips. International Journal of Sustainable Transportation, pp.1-23. DOI: 10.1080/15568318.2024.2311125.
- Jung, Y. and Lee, J., 2024. Optimal Weigh-in-Motion Planning for Multiple Stakeholders. Systems, 12(12), p.557. DOI: 10.3390/systems12120557.

**2023**

- Yeo, J., Lee, S., Jang, K. and Lee, J., 2023. Real-Time Operations of Autonomous Mobility-on-Demand Services with Inter- and Intra-Zonal Relocation. IEEE Transactions on Intelligent Vehicles, 8(10), pp.4357-4369. DOI: 10.1109/tiv.2023.3299692.
- Choi, S. and Lee, J., 2023. Optimal planning of parking infrastructure and fleet size for Shared Autonomous Vehicle. Transportation Research Part E: Logistics and Transportation Review, 176, p.103213. DOI: 10.1016/j.tre.2023.103213.
- Park, J., Lee., J., Kim, J., and Chung, J., 2023. An Optimization Model of On-Demand Mobility Services with Spatial Heterogeneity in Travel Demand. Transportation Research Part C: Emerging Technologies, 153, p.104229. DOI: 10.1016/j.trc.2023.104229.
- Lee., J., Oh, S., and Son, S., 2023. Optimal battery electric bus planning and its economic and environmental impacts. Transportation Research Part D: Transport and Environment, 122, p.103821. DOI: 10.1016/j.trd.2023.103821.
- Kim, J., Tak, S., Lee, J., and Yeo, H., 2023. Integrated Design Framework for On-Demand Transit System based on Spatiotemporal Mobility Patterns. Transportation Research Part C: Emerging Technologies, 150, p. 104087. DOI: 10.1016/j.trc.2023.104087.
- Yun, J., Selmoune, A., Chae, J., Seo, M., and Lee, J., 2023. A Before-And-After Study of a Collision Risk Detecting and Warning System on Local Roads. Journal of Advanced Transportation. DOI: 10.1155/2023/6894065.
- Selmoune, A., Yun, J., Seo, M., Kwon, H., Lee, C., and Lee, J., 2023. Development of a Residential Road Collision Warning Service Based on Risk Assessment. Journal of Advanced Transportation. DOI: 10.1155/2023/7496377.
- Roh, S., Lee, J., Urbino, I.J., Lin, W. and Cho, Y., 2023. Airport pavement maintenance decision-making system with condition cases optimization. Applied Sciences, 13(24), p.13167. DOI: 10.3390/app132413167.
- Zhang, L., Gu, W., Byon, Y., and Lee, J., 2023. Condition-Based Pavement Management Systems Accounting for Model Uncertainty and Facility Heterogeneity with Belief Updates. Transportation Research Part C: Emerging Technologies, 게재 승인. DOI: 10.1016/j.trc.2023.104054.
- An, Y. and Lee, J., 2023. Urban Public Charging Infrastructure Planning for Electric Vehicles: A Continuum Approximation Approach. 27th International Conference of Hong Kong Society for Transportation Studies (HKSTS) (채택)
- An, Y. and Lee, J., 2023. An Analytical Model to Evaluate City wide Waiting and Detour Time for Electric Vehicle Public Charging. International Symposium on Transportation Data and Modelling (ISTDM2023) (채택)

**2022**

- Lee, S., Lee, J., Hiemstra-van Mastrigt, S., and Kim, E., 2022. What cities have is how people travel: Conceptualizing a data-mining-driven modal split framework. Cities, 131, p. 103902. DOI: 10.1016/j.cities.2022.103902.
- Shon, H., Cho, C., Byon, Y. and Lee, J., 2022. Autonomous Condition Monitoring-based Pavement Management System. Automation in Construction, 138, p.104222. DOI: 10.1016/j.autcon.2022.104222.
- Yun, J., Lee, J., Park, J., Chung, K. and Lee, J., 2022. How to measure the network vulnerability of cities to wildfires: Cases in California. Transportation Research Record, 2676(12), pp.382~395. DOI: 10.1177/03611981221095516.
- An, Y., Papakonstantinou, I., Son, S. and Lee, J., 2022. Strategies to Improve the Level of Service of a Citywide Public Fast Charging Infrastructure for Electric Vehicles. Transportation Research Board (TRB) 101st Annual Meeting (채택)
- Yun, J., Selmoune, A., Seo, M., Kwon, H. and Lee, J., 2022. Development of A Risk Assessment-Based Collision Warning Service on Residential Roads. Transportation Research Board (TRB) 102nd Annual Meeting (채택)

**2021**

- Lee, J., Shon, H., Papakonstantinou, I. and Son, S., 2021. Optimal fleet, battery, and charging infrastructure planning for reliable electric bus operations. Transportation Research Part D: Transport and Environment, 100, p.103066.

## 수상과 선정

Members의 수상 항목 8건이다. 연도는 각 수상 항목에 적힌 연도이며, 개별 수상일은 게시되어 있지 않다. 2026년 대한교통학회 제94회 학술발표회는 홈페이지에 3월 12–13일로 적혀 있다. Best Paper Award와 Best TA Award의 명칭은 연구실 표기다.[^members][^home]

- 2025 · Yichan An · Best Paper Award, The 93rd Conference of Korean Society of Transportation, 2025 (Non-Stop Trains)
- 2025 · Yichan An · Best Paper Award, The 93rd Conference of Korean Society of Transportation, 2025 (Shared Autonomous Electric Vehicles)
- 2023 · Yichan An · Best Paper Award, The 88th Conference of Korean Society of Transportation, 2023
- 2022 · Yichan An · Best TA Award, Smart Mobility for Sustainable Society (CoE491), 2022
- 2026 · Jeongin Yun · Best Paper Award, The 94th Conference of Korean Society of Transportation, 2026
- 2025 · Jeongin Yun · Best Paper Award, The Korean Society of ITS Fall Conference, 2025
- 2023 · Jeongin Yun · Best Paper Award, The 89th Conference of Korean Society of Transportation, 2023
- 2024 · Yunkyeong Jung · Best Paper Award, The 91th Conference of Korean Society of Transportation, 2024

## 연락과 위치

- 교수 오피스: KAIST W15동 413호[^dept]
- 교수 기관 전화: 042-350-3614[^dept]
- 교수 이메일: jinwoo@kaist.ac.kr[^dept][^members]
- 기관 주소: (34141) 대전광역시 유성구 대학로 291 한국과학기술원 건설및환경공학과[^dept][^home]
[^home]: KAIST Transportation and Infrastructure Lab, Home. <https://lee.kaist.ac.kr> (관측일 2026-11-06).
[^research]: KAIST Transportation and Infrastructure Lab, Research. <https://lee.kaist.ac.kr/research> (관측일 2026-11-06).
[^members]: KAIST Transportation and Infrastructure Lab, Members. <https://lee.kaist.ac.kr/members> (관측일 2026-11-06).
[^pubs]: KAIST Transportation and Infrastructure Lab, Publications. <https://lee.kaist.ac.kr/publications> (관측일 2026-11-06).
[^dept]: KAIST 건설및환경공학과, 이진우 부교수 소개. <https://cee.kaist.ac.kr/boards/view/professor/97/sc_category/1> (관측일 2026-11-06).

[^p1]: Y. An, J. Y. Chow, S. Woo, J. Lee, Transportation Research Part D Transport and Environment (2025). <https://doi.org/10.1016/j.trd.2025.104605> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p2]: J. Lee, S. Oh, S. Son, Transportation Research Part D Transport and Environment (2023). <https://doi.org/10.1016/j.trd.2023.103821> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p3]: J. Yeo, S. Lee, K. Jang, J. Lee, IEEE Transactions on Intelligent Vehicles (2023). <https://doi.org/10.1109/tiv.2023.3299692> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p4]: H. Shon, J. Lee, Journal of Air Transport Management (2024). <https://doi.org/10.1016/j.jairtraman.2024.102720> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p5]: Y. Jung, J. Lee, Systems (2024). <https://doi.org/10.3390/systems12120557> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p6]: J. Yun 외, J. Lee, Transportation Research Record Journal of the Transportation Research Board (2022). <https://doi.org/10.1177/03611981221095516> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p7]: S. Lee, J. Lee, S. H.-v. Mastrigt, E. Kim, Cities (2022). <https://doi.org/10.1016/j.cities.2022.103902> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).
[^p8]: H. Shon 외, J. Lee, Journal of Intelligent Transportation Systems (2026). <https://doi.org/10.1080/15472450.2026.2695352> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5006964121> (관측일 2026-11-06).

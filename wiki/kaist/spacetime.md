# 시공간지능 연구실 (Spacetime Intelligence Laboratory)

**KAIST 건설및환경공학과 · 윤윤진 부교수**

- 분야: 도시 지역 표현 학습, 시계열·교통 예측, 도심 항공 교통과 공역 평가, 도시 접근성과 기후 회복력[^dept][^research]
- 대분야: 건설·도시·인프라, 컴퓨팅·AI
- 태그: 교통·도시 계획[^dept][^research], 그래프 기계학습·지식 그래프[^research], 시계열 분석·예측[^research], 도심 항공 모빌리티(UAM)[^research], 공간 분석·지리정보(GIS)[^research]
- 홈페이지: <https://spacetime.kaist.ac.kr/>
- 근거와 출처: [시공간지능 연구실 근거 페이지](spacetime-sources.md)

> 사람과 차량의 이동, 도시의 공간과 생활 자료를 함께 분석해 교통을 예측하고 도시와 항공 교통의 운영·접근성·안전을 연구하는 연구실이다.[^dept][^research]

## 무엇을 연구하나

시공간지능 연구실은 복합적으로 연결된 교통·도시·사회기반시설의 문제를 자료 분석, 통계 분석과 시뮬레이션(실제 현상이나 체계의 동작을 모형으로 재현해 결과를 살피는 방법)으로 다룬다. 학과 소개는 경제학과 운영공학의 이론을 바탕으로 지능적이고 지속 가능한 미래도시를 만드는 것을 목표로 적는다. 교수 소개는 도시 지능, 계산을 이용한 교통 연구, 지속 가능한 도시 이동을 주요 관심 분야로 든다.[^dept][^people]

한 축은 **도시와 이동 자료를 배우는 계산 방법**이다. 기계학습(자료에서 규칙을 배워 새 자료를 분류하거나 예측하는 계산 방법)으로 도시 지역의 특성을 나타내고 교통의 시간 변화를 예측한다. 그래프는 대상과 그 관계를 점과 선으로 나타낸 구조다. 연구실은 서로 다른 도시 자료의 관계를 그래프에 담아 지역의 표현을 배우는 모형을 개발하고, 그래프 신경망(점 사이의 연결을 따라 정보를 주고받으며 자료의 표현을 학습하는 계산 모형)으로 교통을 예측한다. 표현 학습은 자료의 특성을 계산에 쓸 수 있는 수치 형태로 나타내는 방법을 학습하는 것이다. 시계열은 시간 순서로 관측한 자료이며, 연구실은 그 시간적 관계와 변화 구조를 학습하는 방법도 제안한다.[^research] 대표 논문 2는 시간에 따른 양상과 자료의 구조적 성질을 함께 배우고, 대표 논문 3은 도시의 물리적 특성과 사람의 활동을 연결하며, 대표 논문 4는 예측 때 새로 들어오는 교통 자료에 맞춰 연결 관계를 조정한다.[^p2][^p3][^p4]

다른 축은 **도로·해상·도심 하늘의 이동과 운영**이다. 연구실은 도심 항공 모빌리티(Urban Air Mobility, UAM, 도시 안과 주변에서 항공기로 사람과 화물을 나르는 운항과 기반 체계)의 수요를 예측하고 이착륙장 입지를 평가한다. 건물과 인구의 위치를 함께 분석해 공역(항공기의 운항을 위해 다루는 하늘의 공간)의 사용 가능성과 위험을 살피며, 여러 항공기의 이동 경로를 계획하는 방법을 연구한다.[^research] 대표 논문 6은 거주 인구만으로 위험을 계산하는 대신 시간·장소에 따라 실제로 머무는 인구를 반영한다. 대표 논문 5는 선박의 위치·속도·진행 방향으로 이동 경로를 예측하고, 대표 논문 7은 여러 자율주행차가 혼잡한 환경에서 움직일 때의 운전 소프트웨어와 교통 분석을 다룬다.[^p5][^p6][^p7]

최근 연구는 **도시 정책을 탐색하는 도구와 생활 여건**으로도 이어진다. 연구실은 대형 언어 모델(Large Language Model, 많은 조절값을 가진 신경망으로 언어의 관계를 학습해 글을 이해하고 생성하는 모형)을 이용해 사용자의 말에서 교통 실험 조건을 정하고 실행하는 AgentSUMO를 소개한다. 이 도구는 SUMO(Simulation of Urban MObility, 도로 위 차량의 움직임을 모의하는 공개 소프트웨어)를 이용한다. 기후 자료와 지역별 매출을 결합해 기후 스트레스에 대한 상권의 회복력을 분석하는 연구도 수행한다.[^research][^events] 대표 논문 1은 식품을 구하기 어려운 지역을 단순한 거리로만 판단하기 어렵고, 가격·이동 여건·지역의 식품 환경을 함께 고려해야 한다고 정리한다.[^p1]

## 주요 연구 주제

### 1. 도시 지역 표현과 시계열 학습

이종 그래프(종류가 다른 점이나 관계를 함께 담는 그래프)에 도시의 공간 특성과 사람의 이동을 연결해 지역별 특성을 학습한다. 연구실은 서로 다른 자료의 관계와 여러 학습 목표를 함께 다루는 HUGAT(Heterogeneous Urban Graph Attention Network)를 제안한다. 그래프 기계학습에서는 그래프 자료에서 관계와 표현을 배우는 방법 자체를 개발한다.[^research] 위상 자료 분석(Topological Data Analysis, 자료의 연결성과 구멍 같은 구조적 성질을 분석하는 방법)도 연구한다. TopoCL은 시계열을 바꿔 학습 자료를 만들 때 시간적 의미가 손상될 수 있다는 문제에 대해, 변환 뒤에도 유지되는 구조적 특징을 함께 학습하도록 설계했다.[^research][^p2][^p3]

### 2. 교통 속도와 선박 경로 예측

교통 자료의 시간적 의존 관계와 도로 사이의 연결을 함께 학습하는 예측 방법을 개발한다. PGCN(Progressive Graph Convolutional Network)은 학습 단계뿐 아니라 실제 예측 단계의 입력에도 맞춰 그래프를 점진적으로 조정한다.[^research][^p4] 선박 쪽에서는 선박자동식별시스템(Automatic Identification System, AIS, 선박의 식별정보와 위치·운항 정보를 무선으로 주고받는 체계)의 자료를 이용하고, 경로 예측과 속도·방향 예측을 함께 학습하는 AIS-ACNet(Auxiliary tasks and Convolutional encoders를 쓰는 선박 경로 예측 모델)을 제안한다.[^research][^p5]

### 3. 항공 이동과 도시 공간의 안전·접근성

도심 항공 교통의 수요와 이착륙장 배치를 평가하고, 지상의 인구와 건물 때문에 생기는 공간적 제약을 분석한다. 연구실은 고속도로 환승 시설과 항공 교통을 잇는 이착륙장 후보를 이동 수요·시간·접근성으로 평가하는 방법을 소개한다. 또한 도시 공간을 이어진 영역으로 묶고, 지상 인구의 시간 변화를 반영해 운항 제한 공간을 평가한다. 건물의 장애물과 운항 요건을 반영한 공역 평가 틀, 공역의 수평·수직 연결성을 나타내는 공간 분석 방법도 제안한다.[^research]

### 4. 대화형 교통 실험과 도시 생활 환경

사용자의 자연어 요청으로 교통 시뮬레이션을 준비·실행하는 AgentSUMO, 거리 영상에 대한 인공지능의 공간 추론, 기후에 따른 지역 상권의 매출 변화와 회복력을 연구한다. 자료의 소리 변환은 수치를 높낮이·리듬·세기 등 소리의 속성에 대응시키는 표현 방법이다. 연구실은 기후와 매출의 관계를 입체 지도와 소리로 제시하는 전시도 수행했다.[^research][^events] 식품 접근성 연구는 각 지역의 경제적·공간적 여건에 따라 식품을 구하기 어려운 원인과 정책의 효과가 달라질 수 있음을 검토한다.[^p1]

## 대표 논문

KAIST 재직 시기의 논문 가운데 도시 지역 표현, 시계열·교통 예측, 항공 안전과 접근성, 자율주행을 고르게 보여 주는 7편을 골랐다. 「쉽게 말하면」은 각 논문의 초록을 근거로 했으며, 선박 경로 논문은 연구실 연구 소개의 게시 요약을 근거로 했다. 저자 역할은 저자 순서에 따른 표기다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Food deserts in context: How site-specific factors reshape food deserts discussion](https://doi.org/10.1038/s42949-026-00458-2) · npj Urban Sustainability | 식품을 구하기 어려운 지역을 다룬 세계의 문헌을 검토했다. 식품 가게까지의 거리뿐 아니라 가격을 감당할 수 있는지, 이동 여건과 지역 식품 환경이 어떤지를 함께 고려하는 방향으로 분석이 변하고 있음을 정리했다. 상점 투자나 온라인 서비스 같은 정책의 효과도 지역의 밀도와 사회적 여건에 따라 달라져, 지역 맥락을 반영한 통합 정책이 필요하다고 결론 내린다.[^p1] | 1저자 Young-Jun Park, 마지막 저자 윤윤진 |
| 2 | 2026 | [TopoCL: Topological Contrastive Learning for Time Series](https://doi.org/10.1109/tnnls.2026.3675422) · IEEE Transactions on Neural Networks and Learning Systems | 시계열을 변형해 학습시키면 반복되는 시간 양상이나 앞뒤 관계가 손상될 수 있다. TopoCL은 시간적 특성과 변환에도 유지되는 구조적 특성을 서로 다른 자료 형태로 취급하고 함께 학습한다. 분류·이상 탐지·예측·다른 과제로의 학습 이전을 시험해 제안한 방법의 성능을 평가했다.[^p2] | 1저자 Nam-Woo Kim, 마지막 저자 윤윤진 |
| 3 | 2025 | [Effective Urban Region Representation Learning Using Heterogeneous Urban Graph Attention Network (HUGAT)](https://doi.org/10.1109/access.2025.3577202) · IEEE Access | 도시의 물리적 공간과 사람의 활동을 함께 나타내는 학습 모형을 제안했다. 여러 종류의 도시 대상과 관계를 연결하고, 공간과 사람 활동의 변화를 동시에 학습한다. 뉴욕 자료에서 개인 평균 소득·빈곤 비율·지역 인기도 예측과 공간적 묶음 구분을 평가했으며, 사람의 이동 자료가 도시의 변화를 담는 데 중요함을 보였다.[^p3] | 1저자 Nam-Woo Kim, 마지막 저자 윤윤진 |
| 4 | 2024 | [PGCN: Progressive graph convolutional networks for spatial-temporal traffic forecasting](https://doi.org/10.1109/tits.2024.3349565) · IEEE Transactions on Intelligent Transportation Systems | 도로 사이의 관계를 학습 때만 정하면 예측 중 생기는 예상 밖 교통 변화에 대응하기 어렵다. PGCN은 학습과 예측 단계 모두에서 새 입력에 맞춰 그래프를 조정하고, 지점별 변화의 유사성을 학습해 연결 관계를 만든다. 서로 다른 실제 교통 자료에서 성능을 시험해 여러 지역에 적용할 수 있는지를 평가했다.[^p4] | 1저자 Yuyol Shin, 마지막 저자 윤윤진 |
| 5 | 2024 | [Deep learning framework for vessel trajectory prediction using auxiliary tasks and convolutional networks](https://doi.org/10.1016/j.engappai.2024.107936) · Engineering Applications of Artificial Intelligence | 선박의 위치·속도·진행 방향 기록에서 앞으로의 경로를 예측하는 AIS-ACNet을 제안했다. 여러 경로로 자료의 특징을 추출해 합치고, 속도와 진행 방향도 함께 예측하는 보조 학습을 둔다. 미국 휴스턴항의 실제 자료에서 기존 모형과 비교하고 구성 요소를 달리한 실험으로 효과를 평가했다.[^p5] | 1저자 Yuyol Shin, 마지막 저자 윤윤진 |
| 6 | 2022 | [Data-driven risk analysis of unmanned aircraft system operations considering spatiotemporal characteristics of population distribution](https://doi.org/10.1016/j.trip.2022.100732) · Transportation Research Interdisciplinary Perspectives | 무인항공기 운항이 지상 사람에게 주는 위험을 시간·장소별 인구 밀도로 평가한다. 거주 인구 대신 실제 체류 인구를 반영해 서울의 운항 제한 공간을 분석했다. 낮에는 상업 지역 주변의 제한 공간이 많고 주거 지역에서는 적게 나타나는 등, 인구의 시간 변화를 정확히 고려할 필요성을 보였다.[^p6] | 1저자 Soohwan Oh, 마지막 저자 윤윤진 |
| 7 | 2024 | [Design, Field Evaluation, and Traffic Analysis of a Competitive Autonomous Driving Model in a Congested Environment](https://doi.org/10.1109/tits.2024.3382680) · IEEE Transactions on Intelligent Transportation Systems | 여러 자율주행차가 동시에 움직이며 추월·교차로 통과·교통법규 준수를 수행하는 운전 소프트웨어를 제시했다. 실제 환경과 가상 환경에서 길 찾기·주변 인식·행동 계획을 평가했다. 여러 차량의 위치와 주행 기록의 공간적 분포를 비교하는 교통 분석 방법도 제안했다.[^p7] | 1저자 Daegyu Lee, 마지막 저자 윤윤진 |

## 교수와 전문 분야

윤윤진 부교수는 서울대학교 수학과 학사(1996), Stanford University 전산학 석사(2000)와 경영공학 석사(2002), UC Berkeley 토목공학 박사(2010)를 받았다. 2011–2018년 KAIST 건설및환경공학과 조교수로 재직했고, 학과 경력은 2018년부터 부교수로 적는다. 이전 경력에는 SRI International과 Stanford University의 연구 조교, Leigh Fisher Associates의 컨설턴트, 항공 운영 연구센터의 연구원이 있다.[^dept]

연구실 교수 소개는 수학·전산학·경영공학·토목공학 배경을 바탕으로 교통·도시·물류·공중보건처럼 여러 체계가 연결되는 문제를 연구한다고 밝힌다. 인공지능대학원과 데이터사이언스대학원 겸임도 적는다. 학과는 주요 연구 분야로 항공 교통 관리, 도시 교통 시스템, 안전 관리 시스템, 교통·도시 기반시설의 대규모 자료 분석을 든다.[^people][^dept]

최근 논문에서 드러나는 전문성은 도시 공간과 사람의 이동을 연결하는 표현 학습, 변화하는 교통망의 예측 방법, 도심 항공 운항을 위한 인구·공간 분석이다. 식품 접근성에 대한 지역별 차이를 정리하는 도시 정책 연구와 혼잡한 환경의 자율주행 구현·교통 분석도 함께 다룬다.[^p1][^p3][^p4][^p6][^p7]

## 응용 분야

도로의 교통 예측과 운영, 선박 경로 예측, 도심 항공 이착륙장 배치와 운항 제한 공간 평가, 대화형 교통 정책 실험이 주요 응용이다. 도시 쪽에서는 지역의 사회경제적 특성, 식품 접근성, 기후 변화에 따른 상권의 회복력을 다룬다.[^research][^p1][^p3][^p5][^p6] 과제에는 도시 표현 학습, 미래 도시 인공지능, 카이스트·버클리 미래 모빌리티 공동연구, 도시 항공 교통을 위한 공간 분석이 게시되어 있다.[^projects]

## 구성원

2026년 11월 6일 People 페이지의 연구교수 1명, 연구원 1명, 박사과정 3명, 석박사통합과정 2명, 석사과정 2명이다. 시작 칸은 누리집의 시작 연월과 계속 표기를 따른다.[^people] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Namwoo Kim | 연구교수 | 2023.09~ | ih736x@kaist.ac.kr |  |
| Sungmin Sohn | 박사과정 | 2023.09~ | smsohn1997@kaist.ac.kr |  |
| Donghyun Yoon | 박사과정 | 2024.03~ | tloveu49@kaist.ac.kr |  |
| Minwoo Jeong | 박사과정 | 2026.09~ | minwoo5003@kaist.ac.kr |  |
| Seungro Lee | 연구원 | 2026.09~ | roy.seungro.lee@kaist.ac.kr |  |
| Keonhee Jang | 석박사통합과정 | 2024.09~ | keoniverse@kaist.ac.kr | 1 |
| Jeeyun Chang | 석사과정 | 2025.03~ | jyc021@kaist.ac.kr |  |
| Jihyeon Ohk | 석박사통합과정 | 2025.09~ | jh.ohk@kaist.ac.kr |  |
| Youngwoo Kim | 석사과정 | 2026.03~ | kimyoungwoo44@kaist.ac.kr |  |

## 졸업생과 이전 구성원

People 페이지 Alumni의 박사 9명과 석사 15명이다. 학위·과정 기간과 진로는 누리집 표기다. Namwoo Kim, Minwoo Jeong, Seungro Lee는 학위 이력과 현재 구성원에 함께 나온다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Ohhoon Kwon | Ph.D. (박사 2010.03~2015.02) | Associate Professor, Dep. of Transportation Engineering, Keimyung Univ. |
| Sammer Ud Din | Ph.D. (박사 2014.03~2018.02) | Assistant Professor, Inst. of Civil Engineering, NUST |
| Yuna Noh | Ph.D. (박사 2012.09~2018.02) |  |
| Jungwoo Cho | Ph.D. (석사 2014.03~2015.08; 박사 2015.09~2020.02) | Assistant Professor, Dep. of Aerospace Engineering, Inha Univ. |
| Jiseon Lee | Ph.D. (박사 2013.09~2022.08) |  |
| Yuyol Shin | Ph.D. (박사 2016.09~2022.08) | Postdoctoral Associate, NYUAD |
| Soohwan Oh | Ph.D. (박사 2016.09~2023.02) | Assistant Professor, Dep. of Aerospace Industrial & Systems Engineering, Hanseo Univ. |
| Namwoo Kim | Ph.D. (석사 2015.09~2017.08; 박사 2017.09~2023.08) | Research Professor, Dep. of Civil and Environmental Engineering, KAIST. |
| Seyun Kim | Ph.D. (석사 2014.03~2016.02; 박사 2016.03~2021.02; 박사후연구원 2021.03~2025.07) | 한국교통연구원 부연구위원 |
| Kyowon Song | M.S. (석사 2010.09~2012.08) |  |
| Yingping Zhao | M.S. (석사 2010.09~2012.08) |  |
| Eunhye Kim | M.S. (석사 2012.03~2014.02) |  |
| Donghun Lee | M.S. (석사 2012.03~2014.02) |  |
| Eunseok Kim | M.S. (석사 2012.09~2014.08) |  |
| Qundeel Hussain | M.S. (석사 2013.03~2015.02) |  |
| Yoonjung Kang | M.S. (석사 2013.09~2016.08) |  |
| Yeonghwa Woo | M.S. (석사 2014.03~2016.02) |  |
| Minjae Kim | M.S. (석사 2016.03~2018.02) |  |
| Hyeyeong Lee | M.S. (석사 2021.03~2023.02) | Kakao Mobility |
| Gwanghwan Seong | M.S. (석사 2021.03~2023.02) |  |
| Junghee Kim | M.S. (석사 2022.09~2024.07) |  |
| Juneyoung Ro | M.S. (석사 2024.03~2026.02) | NAVER LABS Robotics & Autonomous Driving Group |
| Minwoo Jeong | M.S. (석사 2024.03~2026.02) | Ph.D. Candidate, Dept. of Data Science, KAIST |
| Seungro Lee | M.S. (석사 2024.09~2026.07) |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 학술지 12편, 국제 학회 12편, 국내 학회·학술지 5편으로, 합계 29편이다. 연도·제목·저자·발표처는 누리집 표기이며, DOI가 있는 항목은 함께 적었다. 학회명·연도만으로 실린 항목은 「연구실 기재」로 표시한다. 2021년 학회 항목의 연도는 누리집 표기다.[^pubs][^intl][^national]

**2026**

- Y Park, J Na, K Jang, D Lee, C Kwon, Y Yoon. "Food deserts in context: How site-specific factors reshape food deserts discussion". *npj Urban Sustainability; DOI 10.1038/s42949-026-00458-2*.
- H. Shon, S. Kim, Y. Shin, Y. Yoon, J. Lee. "Incorporating traffic propagation impacts into dynamic graph diffusion convolutional network for traffic speed prediction". *Journal of Intelligent Transportation Systems; DOI 10.1080/15472450.2026.2695352*.
- N. Kim, H. Baik, Y. Yoon. "TopoCL: Topological Contrastive Learning for Time Series". *IEEE Transactions on Neural Networks and Learning Systems; DOI 10.1109/tnnls.2026.3675422*.

**2025**

- N. Kim, Y. Yoon. "Effective Urban Region Representation Learning Using Heterogeneous Urban Graph Attention Network (HUGAT)". *IEEE Access, vol. 13, pp. 102602-102612.; DOI 10.1109/access.2025.3577202*.
- M. Jeong, J. Chang, Y. Yoon. "Speak to Simulate: An LLM-Guided Agentic Framework for Traffic Simulation in SUMO". *GeoSIM '25: 8th ACM SIGSPATIAL International Workshop on Geospatial Simulation (연구실 기재); DOI 10.1145/3764921.3770151*.
- D. Yoon, M. Jeong, J. Lee, S. Kim, Y. Yoon. "Integrating Urban Air Mobility with Highway Infrastructure: A Strategic Approach for Vertiport Location Selection in the Seoul Metropolitan Area". *104th TRB Annual Meeting (연구실 기재)*.
- J. Ro, N. Kim, Y. Yoon. "How Well Do Vision-Language Models Understand Cities? A Comparative Study on Spatial Reasoning from Street-View Images". *IEEE/CVF International Conference on Computer Vision (ICCV) Workshops (연구실 기재)*.
- S. Sohn, N. Kim, M. Hansen, Y. Yoon. "Unveiling Latent Factors of the Urban Dynamics for Vertiport Placement". *104th TRB Annual Meeting (연구실 기재)*.
- 김정희，이혜영，김세윤，윤윤진. "동적 시간 왜곡 기반 코로나 19 에 따른 서울 지하철 이용 패턴의 시계열 군집 분석". *대한교통학회지 제43권 제1호; DOI 10.7470/jkst.2025.43.1.015*.

**2024**

- D Lee, H Seong, G Kang, S Han, DH Shim, Y Yoon. "Design, Field Evaluation, and Traffic Analysis of a Competitive Autonomous Driving Model in a Congested Environment". *IEEE Transactions on Intelligent Transportation Systems 25 (8), 9482-9497.; DOI 10.1109/tits.2024.3382680*.
- S. Oh, Y. Yoon. "Urban drone operations: A data-centric and comprehensive assessment of urban airspace with a Pareto-based approach". *Transportation Research Part A: Policy and Practice, 182, 104034.; DOI 10.1016/j.tra.2024.104034*.
- Y. Shin, N. Kim, H. Lee, S. In, M. Hansen, Y. Yoon. "Deep learning framework for vessel trajectory prediction using auxiliary tasks and convolutional networks". *Engineering Applications of Artificial Intelligence, 132, 107936; DOI 10.1016/j.engappai.2024.107936*.
- Y. Shin, Y. Yoon. "PGCN: Progressive graph convolutional networks for spatial-temporal traffic forecasting". *IEEE Transactions on Intelligent Transportation Systems; DOI 10.1109/tits.2024.3349565*.
- 오수환, 윤윤진. "무인항공시스템 운영을 위한 데이터 기반 통합적 도심 공역 평가 프레임워크 연구". *대한교통학회 제90회 학술발표회*.

**2023**

- Y. Shin, Y. Yoon. "Performance Evaluation of Building Blocks of Spatial-Temporal Deep Learning Models for Traffic Forecasting". *IEEE Access, 11, 136478-136495; DOI 10.1109/access.2023.3338223*.
- Lee, H., Kim, N., Kim, S., & Yoon, Y. "Detecting socioeconomic changes of Chicago regions between 2013 and 2020 using urban region representation learning". *Procedia Computer Science, 220, 259-266.; DOI 10.1016/j.procs.2023.03.034*.
- Seong, G., Kim, N., Kim, S., & Yoon, Y. "Multi-modal Based Region Representation Learning Considering Mobility Data in Seoul". *Procedia Computer Science, 220, 251-258.; DOI 10.1016/j.procs.2023.03.153*.
- N. Kim, H. Lee, Y. Yoon. "A Heterogeneous Attention Network Model for Longitudinal Analysis of Socioeconomic and Racial Inequalities in Urban Regions: Evidence from Chicago, IL". *ACM SIGSPATIAL; DOI 10.1145/3589132.3625650*.
- Y. Shin, G. Seong, N. Kim, S. Kim, Y. Yoon. "Understanding Urban Economic Status through GNN-based Urban Representation Learning Using Mobility Data". *UrbanAI 2023 : The 1st ACM SIGSPATIAL International Workshop on Advances in Urban AI; DOI 10.1145/3615900.3628786*.

**2022**

- Oh, S., & Yoon, Y. "Data-driven risk analysis of unmanned aircraft system operations considering spatiotemporal characteristics of population distribution". *Transportation Research Interdisciplinary Perspectives, 16, 100732.; DOI 10.1016/j.trip.2022.100732*.
- S. Oh, Y. Yoon, S. Kim. "Risk analysis of unmanned aerial system operations in urban airspace considering spatiotemporal population dynamics". *2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC); DOI 10.1109/itsc55140.2022.9922030*.
- S. Kim, Y. Yoon. "Vertiport Location Selection for Urban Air Mobility Based on Urban Taxi Mobility Data". *INFORMS (Institute for Operation Research and the Management Sciences) (연구실 기재)*.
- N. Kim, Y. Yoon. "Graph Neural Network Applications for UAM Commute Flow Prediction". *INFORMS (Institute for Operation Research and the Management Sciences) (연구실 기재)*.
- S. Oh, Y. Yoon. "Data-driven Approach for Comprehensive Airspace Assessment of Small Unmanned Aircraft System Operations in Urban Environments". *INFORMS (Institute for Operation Research and the Management Sciences) (연구실 기재)*.
- J. Cho, H. Cho, S. Oh, S. Kim, Y. Yoon. "Can Urban Air Mobility Become a Public Transportation Option?: Understanding Sociodemographic Characteristics and Urban Air Mobility Adoption Readiness in Seoul, South Korea". *Transportation Research Board: 101st Annual Meeting (연구실 기재)*.
- 성광환, 신유열, 윤윤진. "지역별 장애인 콜택시의 접근 형평성 분석". *2022 춘계공동학술대회(한국경영과학회, 대한산업공학회)*.
- 이혜영, 김남우, 윤윤진. "Urban Region Representation Learning Reflecting Seoul Census Data". *2022 춘계공동학술대회(한국경영과학회, 대한산업공학회)*.
- 오수환, 김세윤, 윤윤진. "Population risk analysis of small unmanned aircraft system operations in urban environments". *2022 춘계공동학술대회(한국경영과학회, 대한산업공학회)*.

**2021**

- Y. Shin, Y. Yoon. "A Comparative Study on Basic Elements of Deep Learning Models for Spatial-Temporal Traffic Forecasting". *AAAI 2021 Workshop: AI for Transportation (연구실 기재)*.

## 연구 과제

Projects에 게시된 과제·연구 프로그램 가운데 수행 기간이 2021-10-13–2026-10-13 구간과 겹치는 12건이다. 큰 과제 아래 적힌 도시 항공 교통 과제 1건도 포함한다. 기간은 연도 단위의 누리집 표기로, 시작·종료 월일을 뜻하지 않는다. 지원과 연구비가 적힌 항목은 함께 옮겼다.[^projects]

- 도시 표현 학습을 위한 멀티 모달 인공지능 학습 모델 및 신뢰가능한 인공지능 기술 연구 (기간 2025 ~ 2030; 지원 National Research Foundation Mid-career Grant; 연구비 1,399,460,000 KRW)
- GS건설-KAIST 미래 도시 인공지능 핵심 기술 연구개발 (기간 2024 ~ 2028; 지원 GS E&C Industrial R&D Project; 연구비 4,400,000,000 KRW)
- UAM 운용을 위한 버티포트 위치 및 도심 3차원 공간 분석 (기간 2025 ~ 2028; 지원 GS E&C; 사업 GS E&C-KAIST Joint R&D on Urban AI Technologies for Future Cities)
- Brain Pool Global Hub for Urban AI (기간 2025 ~ 2027; 지원 National Research Foundation (NRF) - Brain Pool Program; 연구비 2,100,000,000 KRW)
- KAIST-NYU Center for Cities and Climate Change (기간 2023 ~ 2024)
- Urban@KAIST (기간 2023 ~)
- 인간중심 미래모빌리티를 위한 카이스트-버클리 국제공동연구 (기간 2022 ~ 2025)
- 탄소 대기 열 환경 정보 기반 지역경제 반응 예측 및 기후 반응 민감지도 개발 (기간 2025; 지원 Seoul AI Foundation (SAIF); 연구비 100,000,000 KRW)
- 서울시 녹지공간의 입체적 연결성 강화를 위한 Visual AI 기반 체감형 도시생태 네트워크 구축 연구 (기간 2025; 지원 Seoul AI Foundation (SAIF); 연구비 100,000,000 KRW)
- 어텐션 메커니즘과 그래프인공신경망에 기반한 대도심 모빌리티 네트워크 분석 및 예측모델 기술 개발 (기간 2021 ~ 2024; 지원 National Research Foundation (NRF) Basic Research Lab)
- 미래 모빌리티 운용을 위한 시멘틱 테셀레이션 기반 수요 분석 및 예측 기술 연구 (기간 2020 ~ 2024; 지원 National Research Foundation (NRF))
- 교통 빅데이터를 활용한 대도심 교통 네트워크의 위상학적 분석 및 응용 연구 (기간 2019 ~ 2023; 지원 National Research Foundation Mid-career Grant)

## 수상과 선정

Events의 수상·선정 기록 4건이다. 날짜는 해당 행사 기록의 날짜이고, 참가자로 적힌 사람을 수상자라고 따로 명시하지 않은 경우에는 참가자라고 표시한다.[^events]

- 2025-11-03–2025-11-06 · 「Speak to Simulate: An LLM-Guided Agentic Framework for Traffic Simulation in SUMO」가 Association for Computing Machinery(ACM)의 Kudos Showcase에 선정되었다.
- 2025-09-05 · Minwoo Jeong이 K-DS Conference에서 Best Paper Award를 받았다.
- 2024-11-11–2024-11-13 · K-DS Hackathon의 2nd Prize. 행사 참가자는 Donghyun Yoon, Sungmin Sohn, Juneyoung Ro, Seungro Lee로 적혀 있다.
- 2024-09-06 · 고속도로 비전 캠퍼스 논문 공모전 장려상 시상식. 행사 참가자는 Donghyun Yoon과 Minwoo Jeong으로 적혀 있다.

## 연구 소식

Events에 연구 내용과 함께 게시된 발표·전시 소식 3건이다. 날짜는 행사 기간이다.[^events] Smart Life Week의 도시 기후·상권 연구는 연구실 Press에도 소개되어 있다.[^press]

- 2026-04-24–2026-04-26 · 대한민국과학축제 경기 행사에서 「Urban Heat, Urban Sales」를 전시했다. 서울의 기후 자료와 지역별 카드 거래를 결합해 기온 변화에 따른 매출을 분석하고, 입체 지도·자료의 소리 변환·지역별 비교 도구로 제시했다.
- 2025-10-10–2025-10-23 · Juneyoung Ro가 ICCV 2025 워크숍에서 도시 거리 영상의 공간 추론 연구를 발표했다. 일반 비전-언어 모델의 도시 장면 이해와 해당 분야 자료를 이용한 추가 학습의 효과를 다뤘다.
- 2025-09-30–2025-10-02 · Smart Life Week 2025에서 MIT Senseable City Lab과 함께 「Urban Heat, Urban Sales」와 「Feeling Nature」를 전시했다. 기온·습도와 카드 거래 자료로 업종·지역별 매출과 기후 회복력을 분석했다.

## 연락과 위치

- 교수 이메일: yoonjin@kaist.ac.kr[^people][^dept]
- 교수 사무실: KAIST W16동 410호[^dept]
- 교수 전화: 042-350-3615[^dept]
- 주소: 대전광역시 유성구 대학로 291 한국과학기술원[^dept]
[^dept]: KAIST 건설및환경공학과 윤윤진 교수 소개. <https://cee.kaist.ac.kr/boards/view/professor/44/sc_category/1>. 관측일 2026-11-06.
[^people]: Spacetime Intelligence Laboratory, People. <https://spacetime.kaist.ac.kr/people>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/peopleData.json>. 관측일 2026-11-06.
[^research]: Spacetime Intelligence Laboratory, Research와 개별 연구 소개. <https://spacetime.kaist.ac.kr/research>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/researchData.json>. 관측일 2026-11-06.
[^pubs]: Spacetime Intelligence Laboratory, Publications의 Journal Publications. <https://spacetime.kaist.ac.kr/publications>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/publicationsData.json>. 관측일 2026-11-06.
[^intl]: Spacetime Intelligence Laboratory, Publications의 International Conference. <https://spacetime.kaist.ac.kr/publications>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/internationalData.json>. 관측일 2026-11-06.
[^national]: Spacetime Intelligence Laboratory, Publications의 National Conference. <https://spacetime.kaist.ac.kr/publications>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/nationalData.json>. 관측일 2026-11-06.
[^projects]: Spacetime Intelligence Laboratory, Projects. <https://spacetime.kaist.ac.kr/projects>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/projectsData.json>. 관측일 2026-11-06.
[^events]: Spacetime Intelligence Laboratory, Events의 대외 활동·성과 기록. <https://spacetime.kaist.ac.kr/events>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/outreachData.json>. 관측일 2026-11-06.
[^press]: Spacetime Intelligence Laboratory, Press. <https://spacetime.kaist.ac.kr/press>. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/pressData.json>. 관측일 2026-11-06.
[^p1]: Y.-J. Park 외, Y. Yoon, npj Urban Sustainability (2026). <https://doi.org/10.1038/s42949-026-00458-2> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.
[^p2]: N.-W. Kim, H. Baik, Y. Yoon, IEEE Transactions on Neural Networks and Learning Systems (2026). <https://doi.org/10.1109/tnnls.2026.3675422> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.
[^p3]: N.-W. Kim, Y. Yoon, IEEE Access 13, 102602-102612 (2025). <https://doi.org/10.1109/access.2025.3577202> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.
[^p4]: Y. Shin, Y. Yoon, IEEE Transactions on Intelligent Transportation Systems (2024). <https://doi.org/10.1109/tits.2024.3349565> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.
[^p5]: Y. Shin 외, Y. Yoon, Engineering Applications of Artificial Intelligence 132, 107936 (2024). <https://doi.org/10.1016/j.engappai.2024.107936> 연구실 연구 소개의 게시 요약 기준. 누리집이 불러오는 자료 파일 <https://spacetime.kaist.ac.kr/data/researchData.json>. 초록 원문 <https://spacetime.kaist.ac.kr/research/maritime>. 관측일 2026-11-06.
[^p6]: S. Oh, Y. Yoon, Transportation Research Interdisciplinary Perspectives 16, 100732 (2022). <https://doi.org/10.1016/j.trip.2022.100732> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.
[^p7]: D. Lee 외, Y. Yoon, IEEE Transactions on Intelligent Transportation Systems 25, 9482-9497 (2024). <https://doi.org/10.1109/tits.2024.3382680> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047381304,publication_year:2021-2026>. 관측일 2026-11-06.

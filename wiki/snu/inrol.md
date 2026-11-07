# INRoL (Interactive & Networked Robotics Laboratory)

**서울대학교 공과대학 기계공학부 · 이동준 교수**

- 분야: 로봇 역학과 제어, 원격 조작과 촉각, 공중 조작, 자율 이동과 산업 장비 제어[^prof][^pi]
- 대분야: 기계·로봇·제조
- 태그: 로봇 조작·파지[^mechanics][^aerial], 제어 이론·제어 공학[^mechanics][^industrial], 햅틱[^haptics], 가상·증강현실[^haptics], 로봇 항법·SLAM[^mobility], 드론·무인 항공기[^aerial]
- 홈페이지: <https://www.inrol.snu.ac.kr/>
- 근거와 출처: [INRoL 근거 페이지](inrol-sources.md)

> 사람의 손과 로봇을 연결하는 조작 장치, 접촉하는 물체의 움직임을 계산하는 방법, 공중 로봇과 산업 장비의 제어를 연구한다.[^pi][^haptics][^mechanics][^aerial][^industrial]

## 무엇을 연구하나

INRoL은 로봇이 사람의 명령을 따르면서 주변 물체와 접촉하고 움직이게 하는 방법을 연구한다. 중심에는 로봇 역학(힘과 운동 사이의 관계를 다루는 분야)과 제어(원하는 동작을 얻도록 장치에 주는 입력을 정하는 일)가 있다. 연구실은 원격 조작, 촉각 장치, 로봇 조작과 시뮬레이션(실제 대상의 작동을 모형으로 재현하는 일), 공중 로봇, 자율 이동, 산업 제어를 관심 분야로 든다.[^prof][^pi]

한 갈래는 **사람의 손동작과 촉감을 로봇·가상 공간에 연결하는 기술**이다. 햅틱(힘·진동·온도 등으로 촉각을 전하거나 촉각을 재는 기술) 장치로 손끝에 힘을 전달하고, 가상현실(Virtual Reality, VR: 컴퓨터가 만든 공간을 보고 조작하게 하는 기술)에서 물체를 만지는 상호작용을 연구한다.[^haptics] 카메라와 관성측정장치(Inertial Measurement Unit, IMU: 가속도와 각속도 등을 재는 장치)를 결합한 손 추적도 다룬다. 손가락에 닿는 힘의 방향과 크기를 함께 제어하고, 손 추적 오차를 사람이 어떻게 지각하는지 살핀다.[^haptics][^p2][^p8]

다른 갈래는 **여러 물체가 닿을 때의 운동 계산과 로봇 제어**다. 조립이나 물체 조작에서는 접촉 위치가 바뀌고 여러 접촉이 동시에 생긴다. 연구실은 이런 움직임을 계산하는 알고리즘(문제를 풀기 위한 계산 절차)을 개발하고, 계산을 여러 부분으로 나눠 동시에 처리하는 방법을 연구한다. 제어 이론에서는 수동성(외부에서 받은 양과 저장해 둔 양을 넘는 에너지를 내보내지 않는 성질)을 이용해 로봇 운동을 분리하고 안정성을 분석한다.[^mechanics] 유연한 받침대 위 양팔 로봇에서는 한 팔을 지지면에 대고 다른 팔이 작업하도록 제어한다.[^mechanics][^p3][^p4]

**자율 이동과 산업 제어**에서는 바퀴 달린 로봇이 갈 길을 정하고, 뒤집히거나 미끄러질 가능성을 판단하며, 굴착기의 움직임을 제어한다. 카메라와 다른 센서의 관측을 결합하는 센서 융합(여러 센서의 관측으로 대상의 상태를 함께 추정하는 방법)과 로봇의 위치 추정·경로 계획을 연구한다.[^mobility] 다리 로봇에서는 카메라가 달린 머리의 충격과 떨림을 줄이는 목 구조를 설계하고, 자율 이동 로봇에서는 매끄럽게 이어지는 경로를 계산한다. 유압은 액체에 가한 압력으로 힘을 전하는 방식이며, 압력은 면에 수직으로 작용하는 힘을 그 면의 넓이로 나눈 물리량이다. 산업용 유압 굴착기에서는 장비의 반응을 자료로 모형화해 목표 움직임을 따르게 한다.[^mobility][^industrial]

**공중 조작**은 사람이 타지 않는 비행체가 이동하면서 물체에 힘을 가하거나 도구를 쓰게 하는 연구다.[^aerial] 연구실은 회전날개로 각 부분을 구동하는 로봇 팔과 관절 잠금 구조를 설계하고, 물체를 운반하거나 조작할 경로를 계산한다.[^aerial] 관절을 잠그는 상태에 따라 움직일 수 있는 방향과 물체를 지탱하는 능력이 달라지므로, 기계 구조와 제어·경로 계획을 함께 다룬다.[^aerial]

## 주요 연구 주제

### 1. 원격 조작과 촉각 상호작용

원격 로봇의 움직임을 사람의 조작에 연결하고 접촉 힘을 사람에게 되돌려 주는 제어를 연구한다. 통신 지연이 있는 상황에서도 안정적인 양방향 조작을 다룬다.[^tele] 최근에는 사람의 손가락 조작으로 카메라 시점을 안내하고 삼차원 장면을 복원하는 방법, 촉각 피드백이 손 추적 오차의 지각에 주는 영향을 연구했다.[^p1][^p2]

### 2. 접촉 시뮬레이션과 조작 제어

물체가 맞닿는 위치·방향과 마찰에 관한 제약을 계산하고, 그 계산을 조립·물체 조작에 연결한다. 여러 접촉을 동시에 다루는 계산의 정확성과 속도를 연구하며, 유연한 받침대 위 로봇의 힘 제어도 다룬다.[^mechanics][^p3][^p4]

### 3. 이동 경로와 산업 장비 제어

최적화(정해진 조건을 지키면서 목표에 가장 잘 맞는 값을 찾는 계산)로 로봇의 경로와 동작을 정한다. 클로소이드(곡선을 따라간 거리에 비례해 곡률이 변하는 곡선)를 이용한 이동 경로 계산과 굴착 중 미끄러짐·전복을 막는 궤적(시간에 따른 위치와 방향의 변화) 조절이 대표 사례다.[^mobility][^p5][^p6]

### 4. 회전날개 구동 로봇 팔과 공중 작업

연결된 각 부분을 회전날개로 구동하는 로봇 팔, 여러 비행체가 연결된 구조, 도구를 단 비행체의 운동과 제어를 연구한다. 관절 잠금을 이용하는 로봇 팔에서는 잠금 선택과 이동 경로 계산을 함께 다룬다.[^aerial][^p7]

## 대표 논문

2021–2026년 서울대 재직 시기 논문 가운데 이동준 교수가 저자이고 초록을 읽을 수 있는 논문을 연구 갈래별로 골랐다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Human-in-the-Loop Gaussian Splatting for Robotic Teleoperation](https://doi.org/10.1109/lra.2025.3632755) · IEEE Robotics and Automation Letters | 원격 조작 중 카메라 영상만으로는 주변 물체와의 간격을 파악하기 어렵다는 문제를 다룬다. 센서 자료로 삼차원 장면을 복원하고, 가상현실 화면에 상황 정보를 표시하며, 사람이 손가락으로 로봇을 필요한 촬영 위치로 안내하는 방법을 결합했다. 모의실험과 실제 실험에서 장면 복원 품질, 사용성, 효율을 평가했다.[^p1] | 1저자 Yongseok Lee, 마지막 저자 이동준 |
| 2 | 2025 | [Enlarging Error Detection Threshold of IMU-Based Hand Tracking in VR with Haptic Feedback](https://doi.org/10.1080/10447318.2025.2586083) · International Journal of Human-Computer Interaction | 가상현실에서 손 추적에 오차가 있어도 사용자가 어느 정도까지 알아채지 못하는지 조사했다. 인위적으로 만든 위치 오차와 관성측정장치 기반 장치에서 생기는 오차를 구분하고, 손에 그럴듯한 접촉 감각을 함께 주면 허용되는 추적 오차가 커짐을 보였다. 손 추적 장치의 정확도를 정할 때 쓸 지침을 제시한다.[^p2] | 1저자 Yongseok Lee, 마지막 저자 이동준 |
| 3 | 2025 | [Variations of Augmented Lagrangian for Robotic Multicontact Simulation](https://doi.org/10.1109/tro.2025.3577410) · IEEE Transactions on Robotics | 로봇과 물체가 여러 곳에서 동시에 닿는 상황의 운동을 계산하는 방법을 제안했다. 접촉 조건을 계산하기 쉬운 문제로 바꿔 반복해서 풀고 관련 변수를 갱신한다. 정확성과 견고성에 초점을 둔 방식과, 시스템을 나눠 계산 속도·확장성·동시 처리를 높이는 방식을 제시하고 여러 로봇 조작 상황에서 평가했다.[^p3] | 1저자 Jeongmin Lee, 마지막 저자 이동준 |
| 4 | 2025 | [Wrench Control of Dual-Arm Robot on Flexible Base With Supporting Contact Surface](https://doi.org/10.1109/tro.2025.3554411) · IEEE Transactions on Robotics | 받침대가 휘는 양팔 로봇에서 한 팔은 지지면에 닿고 다른 팔은 작업하도록 제어했다. 관절의 각도·회전력(힘이 물체를 축 주위로 돌리려는 효과를 나타내는 양) 제한과 접촉 조건, 받침대의 휨을 함께 고려한다. 기본 자세와 힘을 정하는 제어, 변형에 대한 저항을 조절하는 제어, 실제 힘을 되먹임하는 제어를 결합했다. 이론 분석과 모의실험·실험으로 방법을 보였다.[^p4] | 1저자 Jeong-Seob Lee, 마지막 저자 이동준 |
| 5 | 2024 | [Efficient Clothoid Tree-Based Local Path Planning for Self-Driving Robots](https://doi.org/10.1109/icra57147.2024.10610306) · ICRA 2024 | 자율 이동 로봇의 경로를 클로소이드 곡선으로 계산하는 방법이다. 곡선을 정확하고 매끄럽게 근사하는 계산과, 곡선의 대칭·닮음을 이용해 연결 곡선을 표현하는 방법을 만들었다. 이를 경로 후보를 탐색하는 절차에 넣고 여러 주행 상황에서 평가했다.[^p5] | 1저자 Minhyeong Lee, 마지막 저자 이동준 |
| 6 | 2025 | [Real-Time Excavation Trajectory Modulation for Slip and Rollover Prevention](https://doi.org/10.1109/lra.2025.3540389) · IEEE Robotics and Automation Letters | 경사면에서 자율 굴착기가 미끄러지거나 뒤집히지 않게 굴착 움직임을 실시간으로 조절한다. 두 위험을 하나의 부등식 조건으로 표현하고, 다음 시점의 굴착 힘을 학습 모형으로 예측한다. 예측의 남은 오차도 고려해 동작을 정하며, 자체 제작한 축소 굴착기로 실험했다.[^p6] | 1저자 Changu Kim, 마지막 저자 이동준 |
| 7 | 2024 | [Sequential Trajectory Optimization for Externally-Actuated Modular Manipulators with Joint Locking](https://doi.org/10.1109/icra57147.2024.10611268) · ICRA 2024 | 회전날개로 구동하는 여러 부분이 연결되고 관절을 잠글 수 있는 로봇 팔의 경로 계획이다. 관절 잠금은 물체를 지탱하는 능력과 움직임의 자유를 조절하지만, 가능한 조합이 늘어 계산이 복잡해진다. 끝부분과 바로 연결된 부분을 잠그는 구조적 성질을 이용해 문제를 여러 부분으로 나누고 차례로 풀었다. 지면에 연결된 경우와 연결되지 않은 경우의 모의실험·실험으로 평가했다.[^p7] | 1저자 Jaeu Choe, 마지막 저자 이동준 |
| 8 | 2023 | [Symmetry-Based Modeling and Hybrid Orientation-Force Control of Wearable Cutaneous Haptic Device](https://doi.org/10.1109/iros55552.2023.10341859) · IROS 2023 | 손끝에 접촉 힘을 전달하는 착용형 촉각 장치에서 사람마다 다른 조건을 다룬다. 장치 구조의 대칭성을 이용해 위치와 방향을 추정하고, 원하는 접촉 힘의 방향과 크기를 함께 맞추는 제어를 만들었다. 케이블의 당기는 힘을 조절해 마찰의 영향도 줄였다. 장치 실험과 시연으로 추정·제어 방법을 평가했다.[^p8] | 1저자 Somang Lee, 마지막 저자 이동준 |

## 교수와 전문 분야

이동준 교수는 1995년 KAIST 기계공학 학사, 1997년 KAIST 자동화 및 설계 석사, 2004년 University of Minnesota 기계공학 박사를 받았다. 기아자동차 중앙연구소 연구원과 University of Illinois Urbana-Champaign 박사후연구원, University of Tennessee 조교수를 거쳐 2011년 8월 서울대학교에 조교수로 부임했다. 2013년 9월 부교수, 2018년 9월 교수가 됐다.[^prof][^pi]

전문 분야는 로봇 역학·제어를 바탕으로 한 물리적 상호작용이다. 접촉을 포함한 운동 계산, 사람이 조작하는 로봇과 촉각 장치, 공중 조작, 자율 이동과 산업 장비 제어를 연결한다. 최근 논문에서는 여러 접촉의 계산과 양팔 힘 제어, 이동 경로 계산, 굴착 안전 제어, 손가락 기반 원격 조작을 다룬다.[^pi][^p1][^p3][^p4][^p5][^p6]

교수 소개는 서울대학교 미래모빌리티기술센터장과 서울대학교·삼성전자 로보틱스 교육 트랙 책임자를 맡고 있다고 적는다. 강의 목록에는 기계 시스템 모델링(대상의 구조와 작동을 모형으로 표현하는 일)과 제어, 제어 시스템, 로봇 역학과 제어, 동역학이 있다.[^pi][^teaching]

## 응용 분야

원격 로봇 조작, 손가락으로 가상 물체를 다루는 장치, 로봇 조립을 위한 접촉 계산, 자율 이동 로봇, 공중에서 물체를 운반하거나 도구를 사용하는 로봇을 연구한다. 냉간 압연은 금속을 재결정이 일어나는 온도 아래에서 롤 사이로 눌러 두께를 줄이는 가공이며, 재결정은 변형된 재료 안에 새로운 결정들이 생기고 자라는 현상이다. 산업 제어에서는 유압 굴착기, 철강 냉간 압연 공정, 엔진의 상태 추정과 제어를 다룬다.[^tele][^haptics][^mechanics][^aerial][^industrial]

## 구성원

2026년 11월 7일 People의 학생 43명이다. 과정과 연구 주제는 게시 표기를 따랐다.[^people] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Bukun Son | 박사과정 | learning-based control of tight-tolerance assembly and bolting tasks | 6 |
| Jiseock Kang | 박사과정 | sensor fusion and SLAM of mobile and flying robots | 1 |
| Minhyeong Lee | 박사과정 | data-driven control theory for complex mechanical systems | 5, 6 |
| Seongwook Baik | 박사과정 | design, control and estimation theory of aerial manipulation |  |
| Taekyun Kim | 박사과정 | autonomous navigation with unconventional sensors |  |
| Somang Lee | 석박사통합과정 | design and perception of haptic/VR system | 8 |
| Jaeu Choe | 석박사통합과정 | trajectory optimization for aerial manipulation system | 7 |
| Hyunsu Kim | 석박사통합과정 |  | 1 |
| Seoki An | 석박사통합과정 |  |  |
| Hojun Cha | 석박사통합과정 |  | 4 |
| Junheon Yoon | 석박사통합과정 |  |  |
| Hyunreal Park | 석박사통합과정 |  |  |
| Sunkyung Park | 박사과정 |  | 3 |
| Geunsu Yoo | 석사과정 |  |  |
| Changyeon Rou | 석박사통합과정 |  |  |
| Yejun Song | 석박사통합과정 |  |  |
| Eunhak Lee | 석박사통합과정 |  |  |
| Joonseo Jang | 석사과정 |  |  |
| Daehyeok Yun | 석사과정 |  |  |
| Suhyeon Kim | 석박사통합과정 |  |  |
| Joseph Park | 석박사통합과정 |  |  |
| Hoyong Lee | 박사과정 | estimation and control of industrial  processes |  |
| Flin Höpflinger | 박사과정 | design and control of new aerial robotic platforms |  |
| Jinuk Heo | 박사과정 | sensing and estimation of human-interactive robots | 1 |
| Hyelim Choi | 박사과정 | control and analysis of robotic systems with complex interaction | 6 |
| Yonghyeok Kim | 박사과정 | design, estimation and control for aerial manipulation systems |  |
| Jaehwi Cho | 석박사통합과정 | perception and user-interface of hyper-redundant aerial robotic arm |  |
| Youngseon Lee | 석박사통합과정 | teleoperation of anthropomorphic robot hand | 1 |
| Heeseong Lee | 석박사통합과정 |  |  |
| Doyoon Kong | 석박사통합과정 |  | 4 |
| Harim Ji | 석박사통합과정 |  | 1 |
| Kihong Kim | 석박사통합과정 |  |  |
| Jongwan Lee | 박사과정 |  |  |
| Jinhee Yun | 석박사통합과정 |  | 3 |
| Jungeun Park | 석사과정 |  |  |
| Jiwon Kong | 석사과정 |  |  |
| Taegyun Choi | 석사과정 |  |  |
| Yunho Lee | 석박사통합과정 |  |  |
| Jiwon Yoon | 석사과정 |  |  |
| Kyungtack Lee | 박사과정 |  |  |
| Junha Kim | 석사과정 |  |  |
| Yongmin Im | 석사과정 |  |  |
| Junwhee Kim | 석박사통합과정 |  |  |

## 졸업생과 이전 방문 학생

Alumni에 게시된 50명이다. 학위·연도·진로는 연구실의 표기를 따랐고, 마지막 행은 이전 방문 박사과정 학생이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Changsu Ha | Ph.D. (2018) | Samsung Research |
| Myungsin Kim | Ph. D. (2019) | Samsung Research |
| Hyunsoo Yang | Ph.D. (2021) | Istituto Italiano di Tecnologia |
| Jaemin Yoon | Ph.D. (2021) | Samsung Research |
| Sangyun Jeon | Ph.D. (2023) | KATECH |
| Jeongmin Lee | Ph.D. (2024) | Holiday Robotics |
| Minji Lee | Ph.D. (2025) | Holiday Robotics |
| Hyunjun Cho | M.S. (2014) | Hanhwa Corp. |
| Inyeong Jang | M.S. (2016) | Tenergy |
| Donghun Lee | M.S. (2016) | Continental AG |
| Juhyeok Kim | M.S. (2017) | KIDA |
| Hackchan Kim | M.S. (2018) | Samsung Electronics |
| Sengjin Kwon | M.S. (2018) |  |
| Rakjoon Chung | M.S. (2019) | Samsung Research |
| Yonghan Lee | M.S. (2019) | NAVER Labs |
| Dongwon Son | M.S. (2020) | Samsung Research |
| Changmuk Kim | M.S. (2020) | Doosan Infracore |
| Seongjung Kim | M.S. (2021) | Hyundai Motors |
| Hasun Lee | M.S. (2021) | StradVision |
| Seungjoon Lee | M.S. (2023) | Hyundai Motors |
| Seokjin Jeong | M.S. (2023) | HD Hyundai XiteSolution |
| Seokhyun Hong | M.S. (2025) | HD Hyundai XiteSolution |
| Cheongkee Jung | M.S. (2025) |  |
| Sungpyo Sagong | M.S. (2025) | Samsung Research |
| Jaebeom Kwon | M.S. (2026) | Hyundai Motors |
| Hai-Nguyen Nguyen | Ph.D. (2018) | Imperial College London |
| Sangyul Park | Ph.D. (2020) | Samsung Electronics |
| Yongseok Lee | Ph.D. (2021) | DGIST |
| Kwangmin Kim | Ph.D. (2022) | Samsung Electronics |
| Jeongseob Lee | Ph.D. (2024) | Samsung Future Robotics |
| Changu Kim | Ph.D. (2025) | Samsung Future Robotics |
| Youngsun Nam | M.S. (2014) | Hyundai Motors |
| Francis B. Choi | M.S. (2015) | Hyundai Motors |
| Jongbeom Her | M.S. (2016) | Samsung Electronics |
| Kent Yee Lui | M.S. (2016) | ASML |
| Yongjun Lee | M.S. (2018) | Harnics |
| Junyoung Park | M.S. (2018) | Yujin Robot |
| Hyojoon Park | M.S. (2019) | KIST / University of Utah |
| Joonmo Ahn | M.S. (2019) | Samsung Research |
| Minji Kim | M.S. (2019) | Samsung Electronics |
| Hoochang Lee | M.S. (2020) | MandoHella |
| Wonha Lee | M.S. (2020) | Samsung Electronics |
| Ilkwon Hong | M.S. (2021) | KIST |
| Changho Song | M.S. (2023) |  |
| Minsung Kang | M.S. (2023) | HD Hyundai XiteSolution |
| Changhee Han | M.S. (2024) |  |
| Aleksandr Pustroem | M.S. (2025) | ing Robotics |
| Byoungkwon Yoon | M.S. (2025) | Purdue University |
| Soyoon Bae | M.S. (2025) |  |
| Nicolas Staub | Visiting Ph.D. Student | LAAS-CNRS |

## 최근 5년 논문·학회 발표 목록

연구실 Journal과 Conference에 게시된 2021–2026년 논문·학회 발표 가운데 2021년 10월 22일 이후 범위의 항목이다. 학술지 16행과 학회 24행을 연도별로 적었다. 같은 논문이 학술지와 학회에 각각 게시된 경우 발표처 표기를 구분해 두었다.[^journal][^conference]

**2026**

- J. Heo, H. Kim, E. Lee, Y. Lee, H. Park, S. Huh, S. Lee, Y. Lee, and D.J. Lee, Finger-based 3D Human-Swarm Interaction Interface: Design and Human-Subject Evaluation, Expert Systems With Applications, 2026
- J. Kang, J. Choe, D. Kong, B. Yoon, J. Cho, and D.J. Lee, Fast and Robust Online Initialization of Monocular Visual-Inertial Odometry via One-Dimensional Cost Approximation, IEEE Transactions on Robotics, 2026
- J. Lee and D.J. Lee, Real-Time Constraint-Aware Inverse Kinematics via Passivity-Based Dynamics Simulation, IEEE Robotics & Automation Letters, 2026
- H. Ji, Y. Lee, and D. J. Lee, TE-SDF: Tetra-Encoded Signed Distance Field for Memory-Efficient and Accurate Collision Detection, RSS 2026
- Y. Song, S. An, S. Lee, J. Lee, J. Lee, G. Yoo, and D. J. Lee, Differentiable Optimization-Based Modular Planning Framework for Pick-and-Place with Regrasp, ICRA 2026
- J. Yun, J. Lee, S. Park, and D. J. Lee, Amortized NeuralSDF-Mesh Collision Detection for Robotic Contact Simulation, ICRA 2026
- H. Choi, H. Park, H. Ji, S. Lee, Y. Lee, Y. Lee, and D. J. Lee, Robust Hand Tracking from Visual-Inertial Fusion, ICRA 2026

**2025**

- M. Lee, J. Lee and D. J. Lee, Narrow Passage Path Planning via Homotopy-Preserving Collision Constraint Interpolation, IEEE Transactions on Robotics, 2025
- Y. Lee, and D. J. Lee, Enlarging Error Detection Threshold of IMU-based Hand Tracking in VR with Haptic Feedback, International Journal of Human-Computer Interaction, 2025 DOI: 10.1080/10447318.2025.2586083.
- Y. Lee, H. Kim, H. Ji, J. Heo, Y. Lee, J. Kang, J. Lee and D. J. Lee, Human-in-the-Loop Gaussian Splatting for Robotic Teleoperation, IEEE Robotics & Automation Letters, 2025 DOI: 10.1109/lra.2025.3632755.
- J. Lee, M. Lee, S. Park, J. Yun and D. J. Lee, Variations of Augmented Lagrangian for Robotic Multi-Contact Simulation, IEEE Transactions on Robotics, 2025 DOI: 10.1109/tro.2025.3577410.
- J. Lee, D. Kong, H. Cha, J. Lee, D. Ryu, H. Shin and D. J. Lee, Wrench Control of Dual-Arm Robot on Flexible Base with Supporting Contact Surface, IEEE Transactions on Robotics, 2025 DOI: 10.1109/tro.2025.3554411.
- C. Kim, B. Son, M. Lee, H. Choi, S. Hong, M. Kang, J. Moon, D. Kim and D. J. Lee, Real-time Excavation Trajectory Modulation for Slip and Rollover Prevention, IEEE Robotics & Automation Letters, 2025 DOI: 10.1109/lra.2025.3540389.
- H. Lee, S. Sagong, M. Lee, J. Lee, and D. J. Lee, SAC(λ): Efficient Reinforcement Learning for Sparse-Reward Autonomous Car Racing using Imperfect Demonstrations, IROS 2025 DOI: 10.1109/iros60139.2025.11246186.
- S. Park, J. Lee, and D. J. Lee, Shape Abstraction via Marching Differentiable Support Functions, CVPR 2025 DOI: 10.1109/cvpr52734.2025.01575.
- J. Lee, S. Park, M. Lee, D. J. Lee, Efficient Gradient-Based Inference for Manipulation Planning in Contact Factor Graphs, ICRA 2025 DOI: 10.1109/icra55743.2025.11127769.
- M. Lee, J. Lee, D. J. Lee, Narrow Passage Path Planning using Collision Constraint Interpolation, ICRA 2025 DOI: 10.1109/icra55743.2025.11127444.
- M. Lee and D. J. Lee, Time-Correlated Model Predictive Path Integral: Smooth Action Generation for Sampling-Based Control, ICRA 2025 DOI: 10.1109/icra55743.2025.11128021.
- H. Ji, H. Kim, J. Lee, S. Lee, S. An, J. Heo, Y. Lee, Y. Lee, and D. J. Lee, GPU-Accelerated Subsystem-Based ADMM for Large-Scale Interactive Simulation, ICRA 2025 DOI: 10.1109/icra55743.2025.11128665.

**2024**

- B. Yoon, S. Hong and D. J. Lee, Directional Correspondence Based Cross-Source Point Cloud Registration for USV-UAV Cooperation in Lentic Environments, IEEE Robotics & Automation Letters, 10(2), pp. 1601-1608, 2024
- J. Heo, H. Choi, Y. Lee, H. Kim, H. Ji, H. Park, Y. Lee, C. Jung, H-N. Nguyen, and D. J. Lee, Hand Tracking: Survey, International Journal of Control, Automation, and Systems, v22, pp. 1761–1778, 2024 DOI: 10.1007/s12555-024-0298-1.
- T. Kim, B. Yoon and D. J. Lee, UWB-Based Localization System Considering Antenna Anisotropy and NLOS/Multipath Conditions, IROS 2024
- S. An, S. Lee, J. Lee, S. Park and D. J. Lee, Collision Detection between Smooth Convex Bodies via Riemannian Optimization Framework, IROS 2024 DOI: 10.1109/iros58592.2024.10802286.
- J. Choe, J. Lee, H. Yang, H-N. Nguyen and D. J. Lee, Sequential Trajectory Optimization for Externally-Actuated Modular Manipulators with Joint Locking, ICRA 2024 DOI: 10.1109/icra57147.2024.10611268.
- M. Lee and D. J. Lee, Efficient Clothoid Tree-Based Local Path Planning for Self-Driving Robots, ICRA 2024 DOI: 10.1109/icra57147.2024.10610306.
- S-Y. Jeon, R. Chung & D. J. Lee, Planned Trajectory Classification for Wheeled Mobile Robots to Prevent Rollover and Slip, ICRA 2024/IEEE-RAL DOI: 10.1109/lra.2023.3281936.
- H. Choi, M. Lee, J. Kang, and D. J. Lee, Online 3D Edge Reconstruction of Wiry Structures from Monocular Image Sequences, ICRA 2024/IEEE-RAL DOI: 10.1109/lra.2023.3320022.

**2023**

- H. Choi, M. Lee, J. Kang, and D. J. Lee, Online 3D Edge Reconstruction of Wiry Structures from Monocular Image Sequences, IEEE Robotics & Automation Letter, 8(11), pp. 7479-7486, 2023 DOI: 10.1109/lra.2023.3320022.
- S-Y. Jeon, R. Chung & D. J. Lee, Planned Trajectory Classification for Wheeled Mobile Robots to Prevent Rollover and Slip, IEEE Robotics & Automation Letters, 8(7), p.4227-4234, 2023 DOI: 10.1109/lra.2023.3281936.
- J. Lee, M. Lee and D. J. Lee, Large-Dimensional Multibody Dynamics Simulation Using Contact Nodalization and Diagonalization, IEEE Transactions on Robotics, 39(2), p.1419-1438, 2023 DOI: 10.1109/tro.2022.3226149.
- T. Kim, S. Kim and D. J. Lee, Tunable Impact and Vibration Absorbing Neck for Robust Visual-Inertial State Estimation for Dynamic Legged Robots, IEEE Robotics & Automation Letters, 8(3), p.1431-1438, 2023 DOI: 10.1109/lra.2023.3240369.
- Y. Kim, H. Lee, J. Lee and D. J. Lee, Wrench Estimation of Modular Manipulator with External Actuation and Joint Locking, IROS 2023 DOI: 10.1109/iros55552.2023.10341887.
- S. Lee, H. Kim and D. J. Lee, Symmetry-Based Modeling and Hybrid Orientation-Force Control of Wearable Cutaneous Haptic Device, IROS 2023 DOI: 10.1109/iros55552.2023.10341859.
- T. Kim, S. Kim and D. J. Lee, Tunable Impact and Vibration Absorbing Neck for Robust Visual-Inertial State Estimation for Dynamic Legged Robots, IROS 2023/IEEE-RAL DOI: 10.1109/lra.2023.3240369.
- J. Lee, M. Lee and D. J. Lee, Uncertain Pose Estimation during Contact Tasks using Differentiable Contact Features, RSS 2023 DOI: 10.15607/rss.2023.xix.043.
- J. Lee, M. Lee and D. J. Lee, Large-Dimensional Multibody Dynamics Simulation Using Contact Nodalization and Diagonalization, ICRA 2023/IEEE-TRO DOI: 10.1109/tro.2022.3226149.
- J. Lee, M. Lee and D. J. Lee, Modular and Parallelizable Multibody Physics Simulation via Subsystem-Based ADMM, ICRA 2023 DOI: 10.1109/icra48891.2023.10161052.
- M. Lee, J. Lee and D. J. Lee, Differentiable Dynamics Simulation Using Invariant Contact Mapping and Damped Contact Force, ICRA 2023 DOI: 10.1109/icra48891.2023.10161519.

**2022**

- M. Lee, H. Choi, C. Kim, J. H. Moon, D. Kim and D. J. Lee Precision Motion Control of Robotized Industrial Hydraulic Excavators via Data-Driven Model Inversion, IEEE Robotics & Automation Letters, 7(2), pp. 1912-1919, 2022 DOI: 10.1109/lra.2022.3142389.
- M. Lee, H. Choi, C. Kim, J. H. Moon, D. Kim and D. J. Lee Precision Motion Control of Robotized Industrial Hydraulic Excavators via Data-Driven Model Inversion, ICRA 2022/IEEE-RAL DOI: 10.1109/lra.2022.3142389.

## 수상과 선정

교수 소개와 연구실 소식에 게시된 수상·선정 11건이다. 날짜는 소식의 게시일이며 제목에 든 행사 연도와 구분한다. 교수 소개의 2022·2023년 두 항목은 연도 구역 표기이고 날짜는 게시되어 있지 않다. Finalist는 최종 후보, Runner-up은 차순위 수상 표기다.[^pi][^b131]

- 2026-08-19 · Hyelim Choi와 Hyunreal Park가 KHC 2026에서 Robust Hand Tracking System from Visual-Inertial Fusion 시연으로 Outstanding Demonstration Award를 받았다.[^b122]
- 2025-07-09 · Jaebeom Kwon이 ICROS 2025에서 차량 궤적 추종 성능 분석 연구로 Outstanding Paper Award를 받았다.[^b126]
- 2025-07-09 · Jeongmin Lee가 물리 시뮬레이터의 신뢰성과 확장성 연구로 RSS Pioneers 2025에 선정됐다.[^b129]
- 2024-05-28 · Jaeu Choe의 관절 잠금 모듈형 로봇 팔 경로 계획 논문이 ICRA 2024 Best Unmanned Aerial Vehicles Paper Award의 Finalist로 선정됐다.[^b131]
- 2024-05-09 · Yonghyeok Kim이 관절 잠금 로봇 팔의 외력 추정 연구로 KSME 2023 Outstanding Paper Award를 받았다.[^b132]
- 2023-08-02 · Jeongmin Lee와 Minji Lee가 ICRA 2023 워크숍 Embracing Contacts: Making robots physically interact with our world에서 불확실한 물체 자세 추정 연구로 Runner-up Award를 받았다.[^b134]
- 2023-08-02 · Youngsun Lee가 ICRA 2023 워크숍 Computer Vision for Wearable Robotics에서 착용형 로봇 손의 자세 감지·피드백 제어 연구로 Third Best Poster Award를 받았다.[^b134]
- 2023-08-02 · Taekyun Kim이 KROC 2023에서 다리 로봇의 충격·진동 흡수 목 구조 연구로 Outstanding Paper Award를 받았다.[^b136]
- 2023-08-02 · Bukun Son과 Hyelim Choi가 KROC 2022에서 정밀 볼트 조임 학습 방법 연구로 Outstanding Paper Award를 받았다.[^b136]
- 2023 · 이동준 교수가 SNU Excellence in Research Award를 받았다.[^pi]
- 2022 · 이동준 교수가 KROS Achievement Award를 받았다.[^pi]

## 소식

연구실 소식에 게시된 기술 시연 1건이다. 날짜는 소식의 게시일이다.

- 2022-02-14 · CES 2022에서 DYROS와 함께 손 추적·진동 촉각 장치·물체 조작 시뮬레이션을 결합한 자체 제작 촉각 장갑을 시연했다.[^b137]

## 연락과 위치

연구실 누리집은 서울대학교 관악캠퍼스의 사무 공간을 301동 211호·1203호·1204호와 314동 207호, 실험 공간을 312동 202호·203호·204호로 적는다. 주소는 서울특별시 관악구 관악로 1, 우편번호 08826이다. 연구실 전화는 +82-2-880-1690, 교수의 학과 전화는 02-880-1724다.[^home][^prof]

교수 업무 이메일: djlee@snu.ac.kr.[^home]

## 각주
[^home]: INRoL 첫 화면·연락과 위치. <https://www.inrol.snu.ac.kr/> (관측일 2026-11-07).
[^prof]: 서울대학교 기계공학부 이동준 교수 상세. <https://me.snu.ac.kr/snu__professor/%ec%9d%b4%eb%8f%99%ec%a4%80-lee-dongjun/> (관측일 2026-11-07).
[^pi]: INRoL Dongjun Lee 교수 소개. <https://www.inrol.snu.ac.kr/dongjun-lee> (관측일 2026-11-07).
[^people]: INRoL People. <https://www.inrol.snu.ac.kr/people> (관측일 2026-11-07).
[^alumni]: INRoL Alumni. <https://www.inrol.snu.ac.kr/alumni> (관측일 2026-11-07).
[^journal]: INRoL Journal. <https://www.inrol.snu.ac.kr/journal> (관측일 2026-11-07).
[^conference]: INRoL Conference. <https://www.inrol.snu.ac.kr/conference> (관측일 2026-11-07).
[^teaching]: INRoL Teaching. <https://www.inrol.snu.ac.kr/teaching> (관측일 2026-11-07).
[^tele]: INRoL Telerobotics. <https://www.inrol.snu.ac.kr/telerobotics> (관측일 2026-11-07).
[^haptics]: INRoL Haptics/VR. <https://www.inrol.snu.ac.kr/haptics-vr> (관측일 2026-11-07).
[^mechanics]: INRoL Mechanics/Control. <https://www.inrol.snu.ac.kr/mechanics-control> (관측일 2026-11-07).
[^mobility]: INRoL Autonomous Mobility. <https://www.inrol.snu.ac.kr/autonomous-mobility> (관측일 2026-11-07).
[^aerial]: INRoL Aerial Manipulation. <https://www.inrol.snu.ac.kr/aerial-manipulation> (관측일 2026-11-07).
[^industrial]: INRoL Industrial Control. <https://www.inrol.snu.ac.kr/industrial-control> (관측일 2026-11-07).
[^b137]: We participated in CES 2022 and also visited DASL@UNLV. <https://www.inrol.snu.ac.kr/single-post/we-participated-in-ces-2022-and-also-visited-dasl-unlv> (관측일 2026-11-07).
[^b122]: KHC 2026 in Seoul, Korea. <https://www.inrol.snu.ac.kr/single-post/khc-2026-in-seoul-korea> (관측일 2026-11-07).
[^b126]: ICROS 2025 Outstanding Paper Award. <https://www.inrol.snu.ac.kr/single-post/icros-2025-outstanding-paper-award> (관측일 2026-11-07).
[^b129]: RSS Pioneers 2025. <https://www.inrol.snu.ac.kr/single-post/rss-pioneers-2025> (관측일 2026-11-07).
[^b131]: ICRA 2024 at Yokohama, Japan. <https://www.inrol.snu.ac.kr/single-post/icra2024-at-yokohama-japan> (관측일 2026-11-07).
[^b132]: KSME 2023 Outstanding Paper Award. <https://www.inrol.snu.ac.kr/single-post/ksme-2023-outstanding-paper-award> (관측일 2026-11-07).
[^b134]: ICRA 2023 at London. <https://www.inrol.snu.ac.kr/single-post/icra2023-at-london> (관측일 2026-11-07).
[^b136]: KROC 2023/2022 Outstanding Paper Awards. <https://www.inrol.snu.ac.kr/single-post/kroc-2023-2022-outstanding-paper-awards> (관측일 2026-11-07).
[^p1]: Y. Lee 외, D. Lee, IEEE Robotics and Automation Letters (2025). <https://doi.org/10.1109/lra.2025.3632755> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p2]: Y. Lee, D. Lee, International Journal of Human-Computer Interaction (2025). <https://doi.org/10.1080/10447318.2025.2586083> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p3]: J. Lee 외, D. Lee, IEEE Transactions on Robotics (2025). <https://doi.org/10.1109/tro.2025.3577410> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p4]: J.-S. Lee 외, D. Lee, IEEE Transactions on Robotics (2025). <https://doi.org/10.1109/tro.2025.3554411> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p5]: M. Lee, D. Lee, Proceedings - IEEE International Conference on Robotics and Automation/Proceedings (2024). <https://doi.org/10.1109/icra57147.2024.10610306> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p6]: C. Kim 외, D. Lee, IEEE Robotics and Automation Letters (2025). <https://doi.org/10.1109/lra.2025.3540389> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p7]: J. Choe 외, D. Lee, Proceedings - IEEE International Conference on Robotics and Automation/Proceedings (2024). <https://doi.org/10.1109/icra57147.2024.10611268> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).
[^p8]: S. Lee, H.-S. Kim, D. Lee, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (2023). <https://doi.org/10.1109/iros55552.2023.10341859> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100626026,publication_year:2021-2026> (관측일 2026-11-07).

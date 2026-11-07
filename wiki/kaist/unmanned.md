# KAIST 무인시스템 및 제어 연구실 (Unmanned Systems Research Group, USRG)

**KAIST 전기및전자공학부 · 심현철 교수**

- 영문 이름: "David" Hyunchul Shim
- 분야: 무인항공기, 자율주행차, 이동 로봇, 인간형 조종사 로봇[^research]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 자율주행[^research], 드론·무인 항공기[^research], 로봇 항법·SLAM[^research], 보행·휴머노이드 로봇[^research], 강화학습[^learning], 제어 이론·제어 공학[^control]
- 홈페이지: <http://unmanned.kaist.ac.kr/>
- 근거와 출처: [KAIST 무인시스템 및 제어 연구실 근거 페이지](unmanned-sources.md)

> 드론과 자동차가 주변을 알아보고 스스로 이동하는 기술부터 사람용 조종석의 기기를 다루는 인간형 로봇까지, 실제 환경에서 작동하는 자율 시스템을 만드는 연구실이다.

## 무엇을 연구하나

연구실은 무인항공기, 자율주행차, 지상 로봇을 대상으로 주변 인식과 항법(자기 위치를 알아내고 목적지까지 이동하는 기술), 제어(측정한 상태를 바탕으로 원하는 움직임을 만들도록 입력을 정하는 기술)를 결합한다.[^research] 실험실 시연을 넘어 실제 현장에서 작동하는 로봇 시스템을 개발하는 것이 연구 목표다.[^research]

드론 연구에서는 자기 위치를 추정하면서 주변 지도를 함께 만드는 기술을 자체 개발한다.[^research] 라이다(LiDAR, Light Detection and Ranging, 빛을 보내 되돌아오는 정보를 이용해 거리와 입체 모양을 재는 기술)로 얻은 자료를 이용해 복잡한 공간을 탐사하는 드론과 지상 로봇을 연구한다.[^research] 고속 자율주행차에서는 주변 인식, 갈 길을 정하는 경로 계획, 주행 제어를 연결하고 실제 경주 차량으로 시험한다.[^research][^p3]

자료와 경험으로 계산 규칙을 익히는 기계학습 방법도 직접 개발한다. 강화학습(환경과의 상호작용에서 얻는 보상을 바탕으로 행동을 배우는 기계학습 방법)을 활용한 자율주행, 모방학습(시범으로 제시된 행동 자료에서 행동 방법을 배우는 방법)과 강화학습을 결합하는 기법, 여러 로봇의 행동을 함께 학습하는 모형을 연구한다.[^learning] 모의 환경에서 배운 행동을 실제 환경에 적용하는 문제도 다룬다.[^learning]

연구실은 휴머노이드(사람의 신체 형태를 본뜬 로봇)도 개발한다. PIBOT은 사람을 위해 만들어진 항공기 조종석에서 계기를 다루는 조종사 로봇이다.[^research] 연구실은 자연어로 적힌 조종 매뉴얼을 지식으로 정리하고 상황에 맞는 행동을 판단하는 시스템을 개발한다.[^projects] 이동 로봇에 팔을 결합한 모바일 매니퓰레이터는 배송과 원격 현장 체험에도 활용한다.[^projects]

## 주요 연구 주제

### 드론의 위치 추정과 탐사

복잡하고 처음 보는 공간에서 드론이 자기 위치를 추정하고 장애물을 피하며 탐사하게 한다. 대표 논문 1은 라이다와 관성 측정을 결합해 이동량을 추정하고 입체 지도를 생성하는 시스템을 다룬다. 관성 측정은 물체의 가속도(단위 시간당 속도의 변화)와 회전 속도를 재는 것이고, 이동량 추정은 연속한 관측에서 위치와 방향의 변화를 계산하는 것이다. 대표 논문 2는 카메라 영상에서 대응하는 지점을 찾는 방법을 개발해 카메라의 움직임을 추정한다.[^p1][^p2]

### 고속 자율주행의 인식과 제어

서로 다른 측정 장치의 정보를 결합하고, 위치 추정에 실패해도 차량이 경로를 따라갈 수 있게 하는 항법을 개발한다.[^p3] 또 차량의 수학 모형으로 앞으로의 움직임을 예측하면서 제어 입력을 정하는 모델 예측 제어를 이용해 공력 제어(공기의 흐름이 차량에 주는 힘을 조절하는 기술) 장치의 응답 지연을 보상하는 연구를 한다.[^control]

### 여러 층의 실내 이동과 행동 학습

배송 로봇이 여러 층의 지도와 이동 경로를 연결하고 엘리베이터를 이용하도록 시스템을 구성한다. 대표 논문 4는 지도 관리, 위치 추정, 경로 계획, 인식과 과제 계획을 통합한다. 대표 논문 5는 사전에 지도가 없는 환경에서 목적지로 가는 행동과 주변을 탐색하는 행동을 함께 배우고 선택하는 강화학습 방법을 개발한다.[^p4][^p5]

### 인간형 조종사와 원격 현장 체험

조종 매뉴얼의 절차를 해석해 로봇이 실행할 과제로 나누고, 이를 팔과 다리의 움직임으로 연결한다. 대형 언어 모델(LLM, Large Language Model, 많은 글을 학습해 언어를 이해하고 생성하는 인공지능 모형)을 이용해 명령과 상황에 맞는 행동 계획을 만드는 것이 대표 논문 6과 7의 연구다. 대표 논문 8은 원격의 현장을 가우시안 스플래팅(입체 공간의 점에 색과 퍼짐을 부여해 장면을 표현하는 기법)으로 재구성하고 로봇을 통해 시점을 움직이는 텔레프레즌스(멀리 있는 장소에 있는 것처럼 보고 조작하게 하는 기술) 시스템으로, 이동 로봇 팔의 시점 제어와 주변 물체와의 충돌 회피를 함께 다룬다.[^p6][^p7][^p8]

## 대표 논문

심현철 교수가 저자로 참여한 KAIST 재직 시기의 2021–2026년 논문 가운데 드론 항법, 고속 자율주행, 실내 로봇과 행동 학습, 인간형 로봇과 원격 조작을 고르게 골랐다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [An autonomous UAV system based on adaptive LiDAR inertial odometry for practical exploration in complex environments](https://doi.org/10.1002/rob.22284) · Journal of Field Robotics | 복잡하고 처음 보는 공간을 탐사하는 드론 시스템을 제안했다. 라이다와 관성 자료를 결합한 위치 추정으로 입체 지도를 만들고, 이를 탐사·장애물 회피·물체 검출과 위치 파악에 사용한다. 지시에 따르는 모드와 스스로 탐사하는 모드를 전환할 수 있다. 모의 환경과 실제 환경에서 위치 추정과 탐사 성능을 평가했다.[^p1] | 1저자 Boseong Kim, 마지막 저자 심현철 |
| 2 | 2025 | [DINO-VO: A Feature-Based Visual Odometry Leveraging a Visual Foundation Model](https://doi.org/10.1109/lra.2025.3592065) · IEEE Robotics and Automation Letters | 범용 시각 모형 DINOv2의 특징을 카메라 이동량 추정에 활용하는 방법을 제안했다. 눈에 띄는 지점을 검출하고 의미 정보와 세밀한 기하 정보를 결합한 뒤, 영상 사이에서 대응하는 지점을 학습해 카메라 움직임을 계산한다. 여러 공개 자료에서 정확도와 새 환경에 대한 적용 성능을 평가했고, SuperPoint 같은 기존 검출·기술 망보다 어려운 환경에서 강건하다고 평가했다.[^p2] | 1저자 Maulana Bisyir Azhari, 마지막 저자 심현철 |
| 3 | 2024 | [Enhancing State Estimator for Autonomous Racing : Leveraging Multi-Modal System and Managing Computing Resources](https://doi.org/10.1109/tiv.2024.3366153) · IEEE Transactions on Intelligent Vehicles | 고속 경주차에서 믿을 수 있는 측정값을 골라 위치를 추정하고, 위치 추정이 중단되면 직접 인식한 주변 정보를 이용해 경로를 계속 따라가게 했다. 라이다 계산에 필요한 컴퓨터 자원도 효율적으로 배분한다. 모의 시험과 실제 시험에서 실패 복구와 주행의 지속성을 검증했다.[^p3] | 1저자 Daegyu Lee, 마지막 저자 심현철 |
| 4 | 2024 | [Development of an Indoor Delivery Mobile Robot for a Multi-Floor Environment](https://doi.org/10.1109/access.2024.3381489) · IEEE Access | 여러 층에서 사람의 개입 없이 배송하는 이동 로봇을 만들었다. 층별 입체 지도와 지점 간 연결 관계를 나타내는 지도를 결합하고, 엘리베이터에 탈 수 있는 경로와 여러 배송지의 작업 순서를 계획한다. 일반 건물의 정규 업무 시간에 한 달 동안 현장 시험을 진행했다.[^p4] | 1저자 Taejin Kim, 마지막 저자 심현철 |
| 5 | 2024 | [Skill Q-Network: Learning Adaptive Skill Ensemble for Mapless Navigation in Unknown Environments](https://doi.org/10.1109/iros58592.2024.10801531) · IROS | 사전에 지도가 없는 공간에서 여러 이동 기술과 그중 무엇을 선택할지를 함께 배우는 강화학습 방법을 제안했다. 목적지로 향하는 행동과 막힌 상황에서 벗어나기 위한 탐색 행동을 스스로 조합한다. 학습 때 보지 못한 장애물과 불규칙한 지형이 있는 환경에도 추가 학습 없이 적용하는 성능을 보였다.[^p5] | 1저자 Hyunki Seong, 마지막 저자 심현철 |
| 6 | 2025 | [Toward Fully Autonomous Aviation: PIBOT, a Humanoid Robot Pilot for Human-Centric Aircraft Cockpits](https://doi.org/10.1109/mra.2024.3505774) · IEEE Robotics & Automation Magazine | 사람용 조종석을 개조하지 않고 계기를 직접 조작하는 인간형 조종사 로봇 PIBOT을 소개한다. 언어 명령을 행동 순서로 바꾸는 계획기와 이를 팔다리 움직임으로 나누는 판단 모듈(정해진 기능을 맡는 구성 단위)을 연결했다. 전원을 켜기 전 상태에서 출발해 이륙하고 착륙하는 과정을 모의 시험에서 수행해 자율 조종의 가능성을 보였다.[^p6] | 1저자 Sungjae Min·Gyuree Kang·Hyungjoo Kim(공동 기여), 마지막 저자 심현철 |
| 7 | 2024 | [Fly by Book: How to Train a Humanoid Robot to Fly an Airplane using Large Language Models](https://doi.org/10.1109/iros58592.2024.10802288) · IROS | 로봇이 조종 매뉴얼을 이해해 비행 절차를 계획하고 실행하게 하는 LLM-PIBOT 시스템을 제안했다. 명령과 상황에 맞는 절차를 문서에서 찾고 실행할 과제로 정리한다. 생성한 계획으로 실물 크기의 모의 조종 장치를 이용해 항공기를 조종하는 실험을 했다.[^p7] | 1저자 Hyungjoo Kim, 마지막 저자 심현철 |
| 8 | 2026 | [Low-Latency Telepresence via Gaussian Splatting With Safety-Aware Control for Mobile Manipulators](https://doi.org/10.1109/access.2026.3673834) · IEEE Access | 이동 로봇에 달린 팔로 사용자의 시점을 움직이고, 가우시안 스플래팅으로 현장을 재구성하는 원격 체험 시스템을 제안했다. 자연어로 이동을 지시하고 전시물 주변의 충돌도 피한다. 박물관과 유사한 실내 환경에서 시각 정보의 지연, 시점 제어와 충돌 회피 성능을 평가했다.[^p8] | 1저자 Gyuree Kang, 마지막 저자 심현철 |

## 교수와 전문 분야

심현철 교수는 서울대학교에서 1991년 학사와 1993년 석사를, University of California, Berkeley에서 2000년 박사를 받았다. 학위 분야는 기계공학이며, 박사 전공은 제어공학이다. 2007년 2월 KAIST 항공우주공학과 조교수로 부임했고, 2018년 6월 전기및전자공학부로 옮겼다. 현재 학부 교수 명단의 직위는 교수다.[^bio][^prof][^faculty]

연구실 소개와 최근 논문을 함께 보면 전문 분야는 실제 로봇의 인식·항법·제어를 통합하는 자율 시스템이다. 드론에서는 복잡한 환경의 위치 추정과 탐사를, 자동차에서는 고속 주행 중 측정 실패와 계산 자원 문제를, 실내 로봇에서는 여러 층의 경로와 작업 순서를 다룬다. 인간형 로봇 연구는 언어로 된 절차와 실제 기기 조작을 연결하는 방향이다.[^research][^p1][^p3][^p4][^p6][^p7]

## 응용 분야

연구실의 과제는 고속 자율주행, 실내외를 연속해서 이동하는 로봇, 드론과 지상 로봇을 연계한 배송, 사람이 들어가기 어려운 공간의 탐사, 인간형 조종사, 전시 공간의 원격 체험을 대상으로 한다. 로봇이 실제 환경에서 주변을 인식하고 안전하게 이동하며 필요한 기기를 조작하도록 만드는 기술이 여러 응용에 공통으로 연결된다.[^projects][^research]

## 구성원

2026년 11월 7일 연구실 첫 화면의 박사과정 14명과 석사과정 10명이다. 과정과 시작 시기는 게시 표기를 옮겼다.[^students] '대표 논문 참여'는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Ozan Günes | 박사과정 | Spring 2022~ |  |
| Maulana Bisyir Azhari | 박사과정 | Fall 2022~ | 1, 2 |
| 김희영 | 박사과정 | Fall 2022~ |  |
| 김형주 | 박사과정 | Spring 2023~ |  |
| 민성재 | 박사과정 | Spring 2023~ |  |
| 문성우 | 박사과정 | Spring 2024~ |  |
| 나성원 | 박사과정 | Spring 2024~ |  |
| 양정기 | 박사과정 | Fall 2024~ |  |
| 한동훈 | 박사과정 | Spring 2025~ |  |
| 노주형 | 박사과정 | Spring 2025~ |  |
| 강제훈 | 박사과정 | Spring 2026~ |  |
| 안호진 | 박사과정 | Spring 2026~ |  |
| 박성준 | 박사과정 | Fall 2026~ |  |
| 김연찬 | 박사과정 | Fall 2026~ |  |
| 황영준 | 석사과정 | Spring 2025~ |  |
| 이지민 | 석사과정 | Spring 2025~ |  |
| 김경환 | 석사과정 | Fall 2025~ |  |
| 전민규 | 석사과정 | Fall 2025~ |  |
| 김경재 | 석사과정 | Fall 2025~ |  |
| 박준규 | 석사과정 | Spring 2026~ |  |
| 김선강 | 석사과정 | Spring 2026~ |  |
| 양성원 | 석사과정 | Spring 2026~ |  |
| 조현준 | 석사과정 | Spring 2026~ |  |
| 유승현 | 석사과정 | Fall 2026~ |  |

## 졸업생 진로

연구실 첫 화면과 졸업생 페이지에 게시된 박사 23개 항목, 석사 54개 항목이다. 기간과 진로, 학위 논문 제목은 연구실 게시 표기다.[^students][^oldstudents]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 이승욱 | 박사 (2020~2026) | Hanwha Aerospace | Bearing-Only UAV Interception with Cooperative Visual Sensing: The Pursuit–Parallax Conflict, from Information Limits to Capture |
| 강규리 | 박사 (2022~2026) |  | Agentic Robot Planning and Execution with Open-Vocabulary Failure Recovery for Long-Horizon Tasks |
| 성현기 | 박사 (2021~2026) | Qualcomm | Vision-Centric Action Models for Generalizable End-to-End Driving: From Regression to Open-World Retrieval |
| 김태진 | 박사 (2017~2024) | Hyundai Motors Group Robotics Lab | Development of a Mobile Robot System for Delivery in an Indoor Multi-Floor Environment |
| 김보성 | 박사 (2019~2024) | NASA JPL-Field AI | Segmented Map-Based Topological Exploration with Adaptive LiDAR-Inertial Odometry |
| 이대규 | 박사 (2020~2024) | 전북대학교 | Scaleable and Learnable Autonomous Driving System: Design and Field Evaluation |
| 류상규 | 박사 (2018~2023) | ADD | Sensor prediction of missile flight tests |
| 오현찬 | 박사 (2015~2023) | KETI |  |
| 정찬영 | 박사 (2018~2022) | NASA JPL-Field AI | Towards fully autonomous racing : system design for the indy autonomous challenge and imitation learning approach using hierarchical policy abstractions |
| 이한섭 | 박사 (2017~2021) | ETRI | Development of an anti-drone system using a deep reinforcement learning algorithm |
| 정성구 | 박사 (2016~2020) | NASA JPL-Field AI | A Deep Reinforcement Learning based Motion Planner for the Exploration of Unknown Environments with an Aerial Robot |
| 이재현 | 박사 (2016~2020) | Cirrus-Hyundai Supernal | Detect-and-Avoid Technology Development and Flight Test for Unmanned Aircraft System Integration |
| 이다솔 | 박사 (2013~2019) | ADD | (A) Scalable Path Planning Algorithm for Drone Swarms using Density Control |
| 신희민 | 박사 (2013~2018) | KARI | Design of an Aerial Combat Algorithm Based on Basic Fighter Maneuvers and Reinforcement Learning |
| 이장호 | 박사 (Fall 2013~2017) | KARI | Research on the actuator fault tolerant adaptive control scheme to enhance safety of multicopter |
| 조성욱 | 박사 (2012~2017) | 청주대학교 | Research on the Image-based Visual Servoing Framework Considering the Aerial Manipulation |
| 이웅희 | 박사 (2011~2017) | NAVER LABS | Development of urban self-driving vehicle using lane detection on the road and localization in intersection with lane map |
| 양희돈 | 박사 (2008~2015) | Korea Polytechnics |  |
| 정연득 | 박사 (2010~2014) | KARI | A Multimodal Flight Control Design and Flight Test of a Tail-sitter UAV |
| 유동일 | 박사 (2010~2014) | ADD | Design of an Aerial Combat Guidance Law using Virtual Pursuit Point Concept |
| 허성식 | 박사 (2009~2014) | KARI | Vision and LIDAR-based Autonomous Navigation System for Indoor and Outdoor Flight of Unmanned Aerial Vehicles |
| 윤상열 | 박사 (Spring 2011~2013) | LG Electronics | Research on the UAV Model Based Design and Adaptive Control for Uncertain Dynamics |
| 최형식 | 박사 (Fall 2007~2011) | KARI | Research on the UAV Model Based Design and Adaptive Control for Uncertain Dynamics |
| 박성준 | 석사 (2024~2026) | Ph.D. Course |  |
| 김연찬 | 석사 (2024~2026) | Ph.D. Course |  |
| 왕정하 | 석사 (2024~2026) |  |  |
| 강제훈 | 석사 (2024~2026) | Ph.D. Course |  |
| 양승진 | 석사 (2024~2026) | HD Korea Shipbuilding & Offshore Engineering |  |
| 안호진 | 석사 (2024~2026) | Ph.D. Course |  |
| 유제인 | 석사 (2023~2025) |  |  |
| 김지혁 | 석사 (2023~2025) | LG Innotek |  |
| 한동훈 | 석사 (2023~2025) | Ph.D. Course |  |
| 노주형 | 석사 (2023~2025) | Ph.D. Course |  |
| 김도경 | 석사 (2023~2025) | LIG Defense & Aerospace |  |
| 류찬회 | 석사 (2022~2024) |  |  |
| 남현우 | 석사 (2022~2024) | Hyundai Motors Group |  |
| 문성우 | 석사 (2022~2024) | Ph.D. Course |  |
| 나성원 | 석사 (2022~2024) | Ph.D. Course |  |
| 박재용 | 석사 (2022 ~ 2024) | LIG Defense & Aerospace |  |
| Andrea Finazzi | 석사 (2020~2022) | Technology Innovation Institute, Abu Dhabi |  |
| 한승일 | 석사 (2020~2022) | Hyundai Motors Group |  |
| 강규리 | 석사 (2020~2022) | Ph.D Course |  |
| 유재웅 | 석사 (2020~2022) | KETI |  |
| Jedsadakorn Yonchorhor | 석사 (2019~2021) | Siam Commercial Bank |  |
| 김동휘 | 석사 (2019~2021) | KAI |  |
| 한동희 | 석사 (2019~2021) | 라이드 플럭스 |  |
| 김현지 | 석사 (2019~2021) | Samsung Electronics |  |
| 류현지 | 석사 (2019~2021) | Hyundai Motors Group |  |
| 성현기 | 석사 (2019~2021) | Ph.D Course |  |
| 이승현 | 석사 (2019~2021) |  |  |
| 이승욱 | 석사 (2018~2020) | Ph.D Course |  |
| 김태연 | 석사 (2018~2020) |  |  |
| 이대규 | 석사 (2018~2020) | Ph.D Course |  |
| 위인환 | 석사 (2018~2020) | KI Robotics |  |
| 황선유 | 석사 (2016~2018) | TU Delft, Ph.D. Course |  |
| 홍준 | 석사 (2015~2017) | MORAI |  |
| 정찬영 | 석사 (2016~2017) | Ph.D Course |  |
| 강재민 | 석사 (2016~2017) | Timax Soft |  |
| 김현기 | 석사 (2016~2017) | KAI |  |
| 정석우 | 석사 (2015~2017) | LG Electronics |  |
| 이한섭 | 석사 (2015~2016) | Ph. D Course |  |
| 유하람 | 석사 (2015~2016) | Timax Soft |  |
| 박성연 | 석사 (2014~2015) | LG Electronics |  |
| 송한준 | 석사 (2014~2015) | Intuitive Robots |  |
| 이석주 | 석사 (2013~2015) | Ph.D Course |  |
| 이다솔 | 석사 (2013~2014) | Ph.D Course |  |
| 김정운 | 석사 (2011~2012) | ADD |  |
| 정지원 | 석사 (2012~2013) | Ph.D Course |  |
| 신희민 | 석사 (2011~2012) | Ph.D Alumni |  |
| 이상협 | 석사 (2011~2012) | Hyundai Motors Group |  |
| 조성욱 | 석사 (2010~2011) | Ph.D Alumni |  |
| 오은미 | 석사 (2010~2011) | KARI |  |
| 문상우 | 석사 | 공군사관학교 교수요원 |  |
| 정연득 | 석사 (2008~2009) | Ph.D Alumni |  |
| 유동일 | 석사 (2008~2009) | Ph.D Alumni |  |
| 허성식 | 석사 (2007~2008) | Ph.D Alumni |  |
| 강민구 | 석사 (Fall 2014~2015) | Korean Air |  |

## 최근 5년 논문 목록

연구실의 International Journals, Domestic Journals, International Conference Papers, Domestic Conference Papers에 게시된 논문이다. 저자·제목·발표처는 연구실 표기이며, 날짜 없이 게재 승인으로 적힌 항목은 그 상태를 표시했다. 학회 이름·연도만 있는 항목의 연도는 연구실 기재 연도다.[^papers] 연도 표기가 없는 국내 학술지 항목의 연도는 학술지 발행 연도다.[^journal2023a][^journal2023b]

**2026**

- Maulana Bisyir Azhari, Donghun Han, Je In You, Sung Jun Park, and David Hyunchul Shim. "Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing". *Journal of Field Robotics, 2026 (게재 승인); DOI 10.1002/rob.70371*.
- Gyuree Kang, Yeonchan Kim, Juhyeong Roh and David Hyunchul Shim. "Low-Latency Telepresence via Gaussian Splatting with Safety-Aware Control for Mobile Manipulators". *IEEE Access, 2026; DOI 10.1109/access.2026.3673834*.
- 노주형, 강규리, 김연찬, 심현철. "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템". *한국로봇학회 논문지, 제 21권, 제 1호, pp. 48-57, 2026년*.
- Maulana Bisyir Azhari, Donghun Han, Sung Jun Park, and David Hyunchul Shim. "Robust Tightly-Coupled Filter-Based Monocular Visual-Inertial State Estimation and Graph-Based Evaluation for Autonomous Drone Racing". *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (연구실 기재)*.
- Seungwook Lee and David Hyunchul Shim. "Delay-Aware Active Triangulation with Uncertainty-Driven Multi-Agent Reinforcement Learning for Counter-UAS". *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (연구실 기재)*.
- Jehun Kang, Jungha Wang, Youngjun Hwang and David Hyunchul Shim. "DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction". *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (연구실 기재)*.
- Sungwon Nah, Seungjin Yang, Youngjun Hwang, Jungha Wang, Janghan Choi, JungSoo Lee, JungKi Son, and David Hyunchul Shim. "Development of an Active Aerodynamic System for Improving Circuit Driving Performance of High-Performance Electric Vehicles". *2026 IEEE Intelligent Vehicles Symposium (IV) (연구실 기재)*.

**2025**

- Maulana Bisyir Azhari and David Hyunchul Shim. "DINO-VO: A Feature-based Visual Odometry Leveraging a Visual Foundation Model". *IEEE Robotics and Automation Letters (RA-L), 2025; DOI 10.1109/lra.2025.3592065*.
- Sungjae Min \* , Gyuree Kang \* , Hyungjoo Kim \* , and David Hyunchul Shim. "Toward Fully Automated Aviation, PIBOT: a Humanoid Robot Pilot for Human-Centric Aircraft Cockpits". *IEEE Robotics & Automation Magazine (RAM), 2025. ( \* Equal contribution); DOI 10.1109/mra.2024.3505774*.
- Seongwoo Moon, Hyunki Seong, Jehun Kang, Hojin Ahn, and David Hyunchul Shim. "Pixel-to-Control: End-to-End Autonomous Driving via Spatio-Temporal BEV Architecture for Control Sequence Prediction". *2025 IEEE Intelligent Transportation Systems Conference (ITSC); DOI 10.1109/itsc60802.2025.11423111*.
- Juhyeong Roh, Jinwon Kim, Chanwoo Park, and David Hyunchul Shim. "Autonomous Multi-Floor and Narrow Indoor Exploration Using Multi-Criteria Decision-Making Approach". *2025 International Conference on Ubiquitous Robots (UR); DOI 10.1109/ur65550.2025.11078057*.
- Chanhoe Ryu, Hyunki Seong, Daegyu Lee, Seongwoo Moon, Sungjae Min, and David Hyunchul Shim. "Words to Wheels: Vision-Based Autonomous Driving Understanding Human Language Instructions Using Foundation Models". *2025 IEEE Intelligent Vehicles Symposium (IV); DOI 10.1109/iv64158.2025.11097533*.
- Jihyeok Kim, Seongwoo Moon, Sungwon Nah, and David Hyunchul Shim. "MonoDINO-DETR: Depth-Enhanced Monocular 3D Object Detection Using a Vision Foundation Model". *2025 IEEE Intelligent Vehicles Symposium (IV); DOI 10.1109/iv64158.2025.11097713*.
- Sungwon Nah, Seongwoo Moon, Hyunwoo Nam, Chanhoe Ryu, Dokyeong Kim, Jihyeok Kim, and David Hyunchul Shim. "Design and Validation of Autonomous Driving System for High Speed One-on-One Racing". *2025 IEEE Intelligent Vehicles Symposium (IV); DOI 10.1109/iv64158.2025.11097696*.
- Gyuree Kang, Ozan Günes, Seungwook Lee, Maulana Bisyir Azhari, and David Hyunchul Shim. "SPIBOT: A Drone-Tethered Mobile Gripper for Robust Aerial Object Retrieval in Dynamic Environments". *2025 International Conference on Robotics and Automation (ICRA); DOI 10.1109/icra55743.2025.11128830*.

**2024**

- Hyunki Seong and David Hyunchul Shim. "TempFuser: Learning Tactical and Agile Flight Maneuvers in Aerial Dogfights using a Long Short-Term Temporal Fusion Transformer". *IEEE Robotics and Automation Letters(RA-L), 2024*.
- Gyuree Kang, Hyunki Seong, Daegyu Lee, and David Hyunchul Shim. "A Versatile Door Opening System with Mobile Manipulator through Adaptive Position-Force Control and Reinforcement Learning". *Robotics and Autonomous Systems, 2024; DOI 10.1016/j.robot.2024.104760*.
- Taejin Kim, Gyuree Kang, Daegyu Lee, and D. Hyunchul Shim. "Development of an Indoor Delivery Mobile Robot for a Multi-Floor Environment". *IEEE Access, 2024; DOI 10.1109/access.2024.3381489*.
- Daegyu Lee\*, Hyunki Seong\*, Gyuree Kang, Seungil Han, D. Hyunchul Shim, Yoonjin Yoon. "Design, Field Evaluation, and Traffic Analysis of a Competitive Autonomous Driving Model in the a Congested Environment". *IEEE Transactions on Intelligent Transportation Systems (T-ITS), 2024. (\*equally contributed); DOI 10.1109/tits.2024.3382680*.
- Daegyu Lee, Hyunwoo Nam, Chanhoe Ryu, Sungwon Nah, Seongwoo Moon and David Hyunchul Shim. "Enhancing State Estimator for Autonomous Race Car: Leveraging Multi-modal System and Managing Computing Resources". *IEEE Transactions on Intelligent Vehicles (T-IV), 2024; DOI 10.1109/tiv.2024.3366153*.
- Calvin Chanyoung Jung, Andrea Finazzi, Hyunki Seong, Daegyu Lee, Seungwook Lee, Bosung Kim, Gyuri Gang, Seungil Han, and David Hyunchul Shim. "Autonomous System for Head-to-Head Race: Design, Implementation and Analysis; Team KAIST at the Indy Autonomous Challenge". *IEEE Transactions on Field Robotics (2024); DOI 10.1109/tfr.2024.3497922*.
- 노주형, 김보성, 김도경, 김지혁, 심현철. "다층 실내 환경에서 계단 극복이 가능한 궤도형 로봇의 신뢰성 있는 자율 주행 정찰 시스템". *한국로봇학회 논문지, 제 19권, 제 2호, pp. 149-158, 2024년 5월*.
- Hyungjoo Kim, Sungjae Min, Gyuree Kang, Jihyeok Kim, and David Hyunchul Shim. "Fly by Book: How to Train a Humanoid Robot to Fly an Airplane Using Large Language Models". *2024 International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/iros58592.2024.10802288*.
- Hyunki Seong and David Hyunchul Shim. "Skill Q-Network: Learning Adaptive Skill Ensemble for Mapless Navigation in Unknown Environments". *2024 International Conference on Intelligent Robots and Systems (IROS); DOI 10.1109/iros58592.2024.10801531*.
- Hyunki Seong and David Hyunchul Shim. "Self-Supervised Interpretable Sensorimotor Learning via Latent Functional Modularity". *2024 International Conference on Machine Learning (ICML) (연구실 기재)*.
- Sungwon Nah, Jihyeok Kim, Chanhoe Ryu and David Hyunchul Shim. "Interaction-aware Trajectory Prediction for Opponent Vehicle in High Speed Autonomous Racing". *2024 IEEE Intelligent Vehicles Symposium (IV); DOI 10.1109/iv55156.2024.10588727*.
- Boseong Kim, Hyunki Seong, and D. Hyunchul Shim. "Topological Exploration using Segmented Map with Keyframe Contribution in Subterranean Environments". *2024 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/icra57147.2024.10610605*.
- Hyunki Seong and David Hyunchul Shim. "Self-Supervised Interpretable Sensorimotor Learning via Latent Functional Modularity". *XAI4DRL@AAAI24 (연구실 기재)*.
- 노주형, 김보성, 김도경, 김지혁, 심현철. "다층 실내 환경에서 계단 극복이 가능한 궤도형 로봇의 신뢰성 있는 자율주행 시스템". *제19회 한국로봇종합학술대회, 2024.2 (연구실 기재)*.
- 나성원, 김지혁, 심현철. "고속 자율주행 레이싱에서의 장거리 객체 인식을 위한 센서 퓨전 알고리즘". *제19회 한국로봇종합학술대회, 2024.2 (연구실 기재)*.
- 강규리, 심현철. "엘리베이터 탑승을 위한 모바일 매니퓰레이터 시스템". *제19회 한국로봇종합학술대회, 2024.2 (연구실 기재)*.

**2023**

- Boseong Kim, Maulana Bisyir Azhari, Jaeyong Park, and David Hyunchul Shim. "An autonomous UAV system based on adaptive LiDAR inertial odometry for practical exploration in complex environments". *Journal of Field Robotics, 2023; DOI 10.1002/rob.22284*.
- Hyunki Seong, Chanyoung Chung, and David Hyunchul Shim. "Model parameter identification via a hyperparameter optimization scheme for autonomous racing systems". *IEEE Control Systems Letters (2023); DOI 10.1109/lcsys.2023.3267041*.
- 김보성, 이승욱, 박재용, 심현철. "복합적인 실내 환경 내 신뢰성 있는 자율 비행을 위한 3 차원 장애물 지도 생성 및 경로 계획 알고리즘". *로봇학회 논문지, 18(3), 337-345; DOI 10.7746/jkros.2023.18.3.337*.
- 박재용, 김보성, 이승욱, 심현철. "쿼드콥터의 곡률 기반 3 차원 경로 계획 알고리즘". *로봇학회 논문지, 18(3), 316-322; DOI 10.7746/jkros.2023.18.3.316*.
- 이대규, 강규리, 김태진, 심현철, 정훈, 김은혜. "다층 환경에서의 라스트 마일 배송 서비스를 위한 경로 계획 및 엘리베이터 탑승 알고리즘". *로봇학회 논문지 18, no. 1 (2023): 10-17*.
- 성현기，문성우，심현철，김우열，이택규. "비정형 환경의 모바일 로봇을 위한 보조 도착점 기반계층적 경로계획 프레임워크". *제어로봇시스템학회지, 제29권 제6호, 2023년 6월*.
- Daegyu Lee, Hyunwoo Nam, Chanhoe Ryu, Sungwon Nah, and David Hyunchul Shim. "Resilient Navigation Based on Multimodal Measurements and Degradation Identification for High-Speed Autonomous Race Cars". *2023 IEEE Intelligent Vehicles Symposium (IV); DOI 10.1109/iv55152.2023.10186537*.
- Boseong Kim, Chanyoung Jung, D. Hyunchul Shim and Ali-akbar Agha-mohammadi. "Adaptive Keyframe Generation based LiDAR Inertial Odometry for Complex Underground Environments". *2023 IEEE International Conference on Robotics and Automation (ICRA); DOI 10.1109/icra48891.2023.10161207*.
- 김보성, 이승욱, 박재용, 심현철. "복합적인 실내 환경 내 신뢰성 있는 자율 비행을 위한 3차원 장애물 지도 생성 및 경로 계획 알고리즘". *제18회 한국로봇종합학술대회, 2023.2 (연구실 기재)*.
- 이승욱, 조성욱，신희민，심현철. "영상 기반 공중 물체 탐지와 위치 추정을 통한 궤적 예측 방법". *2023 항공우주시스템공학회 학술행사 논문집, 2023.5 (연구실 기재)*.
- 조성욱，심현철，신희민. "딥러닝 기반 중장거리 불법 드론 인식 모델과 추적 알고리즘 운용 전략 연구". *2023 항공우주시스템공학회 학술행사 논문집, 2023.5 (연구실 기재)*.
- 박재용，이승욱，김보성，한동훈，심현철. "모델 예측 제어 기법을 활용한 쿼드롭터의 타겟 추적". *2023 항공우주시스템공학회 학술행사 논문집, 2023.5 (연구실 기재)*.
- 박재용, 김보성, 이승욱, 심현철. "유리에서 유발된 잡음의 효율적인 제거를 위한 라이다 센서 필터링 알고리즘". *제 18회 한국로봇종합학술대회, 2023.2 (연구실 기재)*.
- 민성재, 김형주, 심현철. "자율 항공 조종을 위한 인간형 조종사 로봇". *제 18회 한국로봇종합학술대회, 2023.2 (연구실 기재)*.
- 이대규, 심현철. "다층 환경에서의 라스트 마일 배송 서비스를 위한 경로 계획 알고리즘". *제18회 한국로봇종합학술대회, 2023.2 (연구실 기재)*.

**2022**

- Sang-Gyu Ryu, Jae Jin Jeong and David Hyunchul Shim. "Sensor data prediction in missile flight tests". *Sensors 22.23 (2022): 9410; DOI 10.3390/s22239410*.
- 강규리, 이대규,심현철. "실내 자율주행 로봇을 위한 3차원 다층 정밀 지도 구축 및 위치 추정 알고리즘". *로봇학회 논문지 17, no.1 (2022) : 025-031*.
- Jaewoong Yoo, Hyunki Seong, David Hyunchul Shim, Jung Ho Bae, Yong-Duk Kim. "Deep Reinforcement Learning-based Intelligent Agent for Autonomous Air Combat". *2022 IEEE/AIAA 41st Digital Avionics Systems Conference (DASC 2022) (pp. 1-9). IEEE; DOI 10.1109/dasc55683.2022.9925811*.
- 김태진, 심현철. "자율 주행 전동 스쿠터의 개념 연구 및 시스템 개발". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 성현기, 심현철. "비정형지형 탐색을 위한 주행 가능성 기반 경로 계획". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 강규리, 심현철. "도심 자율주행을 위한 차량 및 장애물 인식 알고리즘". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 장윤하, 성현기, 정명근, 심현철. "Deep reinforcement learning based End-to-End Autonomous Driving Network with Semantic map". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 이승욱, 김보성, 심현철. "영상 및 음성 데이터 수집을 위한 실내 드론 자율비행 알고리즘". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 김보성, 이승욱, 심현철. "다층 건물 재난 상황 대응을 위한 자율 비행 드론 시스템 개발". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.
- 이대규, 남현우, 심현철. "Wi-Fi 수신신호강도를 활용한 다층 환경에서의 항법에 관한 연구". *제17회 한국로봇종합학술대회, 2022.5 (연구실 기재)*.

**2021**

- Daegyu Lee, Gyuree Kang, Boseong Kim, and D. Hyunchul Shim. "Assistive Delivery Robot Application for Real-World Postal Services". *in IEEE Access, vol. 9, pp. 141981-141998, 2021, doi: 10.1109/ACCESS.2021.3120618; DOI 10.1109/access.2021.3120618*.
- Daegyu Lee, Hyungi Kim, and David Hyunchul Shim. "Framework for Deep Learning-enabled Building High-Definition Maps and Planning Routes for Autonomous Vehicles". *2021 21th International Conference on Control, Automation, and Systems (ICCAS 2021) (연구실 기재)*.

## 과제

연구실의 Project list와 Past researches에서 수행 기간을 적은 과제 가운데 2021년 10월 13일–2026년 10월 13일에 걸치는 연도 범위의 항목이다. 기간은 누리집의 연도 표기다.[^projects]

- 산업통상부: AI 기반 고속 자율주행을 위한 고성능 특화 플랫폼 및 한계 극복 드라이빙 기술 개발 (기간 2026-2029)
- 한화시스템: 지능형 원격제어 시스템 구현을 위한 인지-자율 협업제어 기술 연구 (기간 2026-2028)
- 티라로보틱스: 실내외 연속 자율주행(Seamless Navigation) 알고리즘 개발 (기간 2026)
- 산업통상부: 자율주행을 위한 합성 데이터 수집 및 시뮬레이션 고도화 기술 개발 (기간 2025-2027)
- KETI: 초실감 문화콘텐츠 체험을 위한 텔레프레즌스 Robo-VFX 서비스 플랫폼 기술 개발 (기간 2024-2026)
- ETRI: 드론-로봇 연계 도심지 최대중량 40kg 화물 멀티모달 배송 기술 개발 (기간 2023-2026)
- 무인이동체 보안을 위한 항재밍 및 무허가 무인이동체 탐지대응 기술 개발 (기간 2023-2026)
- 자연어 처리 지식베이스 기반 인간형 조종사 로봇 개발 (기간 2022-2027)
- 한화에어로스페이스: 초장사정 유무인 복합 자주포 및 지휘차량 사업 소프트웨어 설계 및 시험 (기간 2024-2026)
- LIG Nex1: 유무인 협업을 위한 자율화 소프트웨어 (기간 2023-2026)
- ADD: 유인 운용 내부제독 시스템 (기간 2024-2026)
- 현대자동차: 고성능EV 서킷 주행 성능 향상을 위한 액티브 에어로 벡터링 시스템 개발 (기간 2024-2025)
- 현대자동차: PnD (Plug and Drive) 모듈 다양화 및 표준화 개발 (기간 2024-2025)
- 현대자동차: 심층강화학습을 활용한 자율 주행 알고리즘 및 Sim2Real 기법 연구 (기간 2024)
- KRM: 건물 및 지하 공동 탐색을 위한 로봇 자율주행 기술 개발 (기간 2024)
- 다중로봇의 임무수행을 위한 end-to-end 강화학습 모델 프로토타입 연구 (기간 2023-2024)
- 배송로봇 경로계획 및 플랫폼 제어 모듈 개발 (기간 2022)
- 불법드론 지능형 대응기술개발사업 - 드론캅 기체/요소기술 및 운용시스템 개발 (기간 2021-2025)
- 무인전투기 자율 공중교전을 위한 강화학습 기반 알고리즘 개발 (기간 2021-2023)
- 비정형 실내 환경 자율주행을 위한 모바일 매니퓰레이터 시스템 개발 (기간 2021)
- 도심형 주소기반 자율주행 실증 배달로봇 (기간 2020-2021)
- Autonomous Drone Navigation based on Vision and AI (기간 2019-2022)
- ROS 기반 AGV 자율주행 알고리즘 개발 및 적용 (기간 2019-2021)
- SK hynix KAIST 차세대 인공지능 반도체 시스템 연구센터 산하 자율 주행 시스템 개발 (기간 2019-2021)
- Flight Safety Regulation Development and Integrated Operation Demonstration for Civil RPAS (기간 2015-2021)

## 특허

연구실 Patents 목록에서 2021년 10월 13일–2026년 10월 13일에 출원한 항목이다. 번호와 출원일은 연구실 게시 표기다.[^patents]

- 제어 명령을 생성하는 방법 및 이를 위한 전자 장치 (발명자 심현철, 김형주, 민성재, 이지민; 출원번호 10-2026-0039110; 출원일 2026.03.04; 국가 대한민국)
- 로봇 손가락 및 그의 설계 방법 (발명자 심현철, 민성재, 김형주; 출원번호 10-2026-0029774; 출원일 2026.02.13; 국가 대한민국)
- 장애물을 고려한 로봇의 이동 경로 결정을 위한 로봇 경로 제어 장치 및 방법 (발명자 심현철, 노주형, 김보성, 성현기, 박찬우, 김진원, 윤우성; 출원번호 10-2024-0182720; 출원일 2024.12.10; 국가 대한민국)
- 인간형 로봇 조종사 시스템 및 이를 이용한 자율 비행 방법 (발명자 심현철, 민성재, 김형주, 강규리; 출원번호 10-2023-0134388; 출원일 2023.10.10; 국가 대한민국)
- 보조 도착점에 기반한 경로를 생성하는 전자 장치 및 그 동작 방법 (발명자 심현철, 성현기, 문성우; 출원번호 10-2023-0121759; 출원일 2023.09.13; 국가 대한민국)
- 영상 및 음성 데이터 기반 실내 자율비행 드론 시스템 (발명자 심현철, 이승욱, 김보성, 박재용; 출원번호 10-2022-0164831; 출원일 2022.11.30; 국가 대한민국)
- Autonomous driving device (발명자 Hyunki Seong, Chanyoung Jung, Seungwook Lee, David Hyunchul Shim; 출원번호 17/937,733; 출원일 2023.05.18; 국가 United States)
- 다층 건물 환경에서의 그래프 기반 통합 경로 계획 방법 및 장치 (발명자 심현철, 이대규, 강규리; 출원번호 10-2022-0135857; 출원일 2022.10.20; 국가 대한민국)
- Method and system for building lane-level map by using 3D point cloud map (발명자 David Hyunchul Shim, Daegyu Lee, Hyungi Kim; 출원번호 17827844; 출원일 2022.05.30; 국가 United States)
- 자율 주행 장치 (발명자 심현철, 성현기, 이승욱, 정찬영; 출원번호 10-2021-0157644; 출원일 2021.11.16; 국가 대한민국)

## 수상과 선정

연구실 소식과 수상 목록의 수상 항목이다. 연도만 표시한 2022년·2023년 항목의 연도는 누리집 연도 표기이고 날짜는 게시되어 있지 않다.[^awards]

- 2026.06 · 나성원, 양승진, 황영준, 왕정하, 심현철 교수 외, IEEE Intelligent Vehicles Symposium (IV) 2026 Best Student Paper Award (1st Prize) 수상
- 2026.06 · 민성재, 강규리, 김형주, 심현철 교수, IEEE Robotics & Automation Magazine Best Paper Award 수상
- 2025.07 · Team USRG, Indy Autonomous Racing Laguna Seca 3위
- 2025.04 · Team USRG, UAE A2RL DCL 드론 레이싱 3위
- 2024.09 · KAIST-KRM 연합팀, 육군 드론봇챌린지 최우수상
- 2024.02 · KAIST 기계공학과 김진환 교수 연합팀, UAE MBZIRC Maritime Challenge 2위
- 2024.02 · 김보성, 노주형 외, 한국 로봇학회 우수논문상 2건
- 2023.11 · 이대규, 나성원, 남현우, 문성우, 류찬회, 김도경, 노주형, 김지혁, 심현철 교수(EureCar-R팀), 현대 자율주행 챌린지 2등
- 2023.08 · 김보성, 노주형, 김도경, 김지혁, 심현철, 국방부장관배 드론봇 챌린지 대회 건물내부정찰 종목 기술혁신상
- 2023 · 김보성, KRoC 한국로봇종합 학술 대회 우수논문상
- 2022.12 · 김보성, 이승욱, 인공지능 그랜드 챌린지(AGC) 공로상(KETI 연구원장상)
- 2022 · 김보성, 이승욱, 박재용, Maulana Bisyir Azhari, Ozan Günes, 심현철, 제5회 Army TIGER 드론봇 임무형 챌린지 대회 건물 내부 정찰 종목 우수상
- 2022.02 · 심현철 교수, KAIST 제51주년 국제협력상
- 2021.12 · 심현철 교수, 과기정통부 장관 표창(인공지능챌린지 발전 공로)
- 2021.11 · 이대규, 성현기, 한승일, 강규리, 심현철 교수, 현대자동차 자율주행 챌린지 우승 및 서울특별시장 표창

## 소식

연구실 소식의 연구 협력과 연구실 이전 항목이다.[^news]

- 2023.02 · Team USRG가 현대자동차(주)와 고속 자율주행기술 개발 파트너십을 체결했다.
- 2022.08 · USRG 연구실이 N1 314호로 이전했다.

## 연락과 위치

- 교수 업무 이메일: hcshim@kaist.ac.kr[^faculty]
- 연구실 이메일: usrglab@kaist.ac.kr[^oldstudents]
- 교수 전화: +82-42-350-7445[^oldstudents]
- 교수 사무실: IT융합빌딩(N1) 308호[^faculty]
- 연구실 위치: N1 314호. 2022년 8월 이전 소식의 표기다.[^news]
[^research]: 연구실 첫 화면의 연구 소개. 드론·자율주행차·지상 로봇·자체 SLAM·PIBOT 연구. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^learning]: 연구실 첫 화면의 Past researches 중 현대자동차 심층강화학습·모방학습 연구 및 다중 로봇 강화학습 모형 개발. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^control]: 연구실 첫 화면의 Past researches 중 차량 모형 기반 공력 제어와 모델 예측 제어의 응답 지연 보상 연구. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^projects]: 연구실 첫 화면의 Project list와 Past researches. 수행 기간과 연구 대상. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^students]: 연구실 첫 화면의 Students 및 Alumni. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^papers]: 연구실 첫 화면의 International Journals·Domestic Journals·International Conference Papers·Domestic Conference Papers. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^patents]: 연구실 첫 화면의 Patents. 출원번호·출원일·발명자. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^awards]: 연구실 첫 화면의 News Flash·Awards·News. 수상명과 시기. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^news]: 연구실 첫 화면의 News. 연구 협력·연구실 이전. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^prof]: 연구실 첫 화면의 Professor. 학위와 KAIST 부임·학부 이동 경력. <http://unmanned.kaist.ac.kr/> (관측일 2026-11-07).
[^faculty]: KAIST 전기및전자공학부 교수 목록 2쪽, 심현철 교수. <https://ee.kaist.ac.kr/professor-s1/?page=2> (관측일 2026-11-07).
[^bio]: 연구실 Professor 소개. 학위 분야와 경력. <http://unmanned.kaist.ac.kr/bio.html> (관측일 2026-11-07).
[^oldstudents]: 연구실 Students·Alumni 및 연락처. <http://unmanned.kaist.ac.kr/students.html> (관측일 2026-11-07).
[^journal2023a]: 김보성·이승욱·박재용·심현철, 「복합적인 실내 환경 내 신뢰성 있는 자율 비행을 위한 3차원 장애물 지도 생성 및 경로 계획 알고리즘」, The Journal of Korea Robotics Society 18(3), 337–345. 인쇄판 출판일 2023-08-31. DOI 10.7746/jkros.2023.18.3.337. <https://jkros.org/_common/do.php?a=full&aidx=37551&b=&bidx=3391> (관측일 2026-11-07).
[^journal2023b]: 박재용·김보성·이승욱·마울라나 비시르 아즈하리·심현철, 「쿼드콥터의 곡률 기반 3차원 경로 계획 알고리즘」, The Journal of Korea Robotics Society 18(3), 316–322. 인쇄판 출판일 2023-08-31. DOI 10.7746/jkros.2023.18.3.316. <https://jkros.org/_PR/view/?aidx=37548&bidx=3391> (관측일 2026-11-07).
[^p1]: B. Kim, M. B. Azhari, J.-Y. Park, D. H. Shim, Journal of Field Robotics (온라인 2024-01-19). <https://doi.org/10.1002/rob.22284> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p2]: M. B. Azhari, D. H. Shim, IEEE Robotics and Automation Letters (온라인 2025-07-23). <https://doi.org/10.1109/lra.2025.3592065> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p3]: D. Lee 외, D. H. Shim, IEEE Transactions on Intelligent Vehicles (2024). <https://doi.org/10.1109/tiv.2024.3366153> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p4]: T. Kim, G. Kang, D. Lee, D. H. Shim, IEEE Access (2024). <https://doi.org/10.1109/access.2024.3381489> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p5]: H. Seong, D. H. Shim, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (온라인 2024-10-14). <https://doi.org/10.1109/iros58592.2024.10801531> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p6]: S. Min, G. Kang, H. Kim, D. H. Shim, IEEE Robotics & Automation Magazine (온라인 2024-12-13). <https://doi.org/10.1109/mra.2024.3505774> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07). 공동 기여 표시는 연구실 논문 목록. <http://unmanned.kaist.ac.kr/>.
[^p7]: H. Kim 외, D. H. Shim, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (온라인 2024-10-14). <https://doi.org/10.1109/iros58592.2024.10802288> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).
[^p8]: G. Kang, Y. Kim, J. Roh, D. H. Shim, IEEE Access (2026). <https://doi.org/10.1109/access.2026.3673834> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5053591461,publication_year:2021-2026> (관측일 2026-11-07).

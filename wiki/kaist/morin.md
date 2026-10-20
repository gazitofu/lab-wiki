# 모바일 로보틱스·지능 연구실 (Mobile Robotics & Intelligence Laboratory, MORIN Lab)

**KAIST 기계공학과 · 김진환 교수**

- 분야: 무인 수상정·잠수정의 동역학·유도·제어, 자율운항선박(충돌 회피, 접안), GPS가 닿지 않는 곳의 항법과 SLAM(수중 해저지형 SLAM 포함), 다중 로봇 임무 계획과 작업 할당, 학습 기반 모델링·제어
- 홈페이지: <https://kaistmorin.github.io/>
- 근거와 출처: [MORIN Lab 근거 페이지](morin-sources.md)

> 사람이 타지 않는 배와 잠수정, 로봇이 복잡하고 불확실한 환경에서 스스로 길을 찾고 부딪히지 않게 움직이도록 만드는 연구실이다. 바다 위 자율운항선박과 바닷속 지도 만들기에 특히 힘을 쏟으며, 여기서 만든 방법은 땅과 하늘의 로봇에도 쓸 수 있다고 본다.[^home][^research]

## 무엇을 연구하나

연구실은 차량과 이동 로봇의 지능형 제어, 자율성, 의사결정을 연구하며, 동역학·유도·항법·제어·추정과 학습 기반 방법을 두루 다룬다. 특히 무인 수상정(사람 없이 물 위를 다니는 배)과 무인 잠수정 같은 해양 로봇과 자율 차량에 무게를 두지만, 여기서 만든 방법은 땅과 하늘의 이동 로봇에도 쓸 수 있다고 소개한다.[^home] 연구는 네 주제로 묶인다.[^research]

첫째는 **해양·야외 로봇의 동역학과 제어**다. 무인 수상정·잠수정의 움직임을 이론과 학습으로 모델링하고 제어한다.[^research] 대표 논문에서는 미지의 외란(밖에서 가해지는 예측하기 어려운 힘)이 있어도 배를 부두에 안전하게 대는 제어기를 만들었고,[^p6] 포항 운하에서 작은 유람선이 좁은 물길을 스스로 다니게 하는 실험을 했다.[^p7]

둘째는 **자율운항선박**이다. 해상 상황 인식과 자동 운항, 국제 해상충돌예방규칙(COLREGs, 배끼리 마주쳤을 때 피하는 방법을 정한 국제 규칙)을 지키는 충돌 회피, 도달 가능 영역에 기반한 안전 분석을 연구한다.[^research] 대표 논문에서는 좁은 수로에서 규칙을 지키며 피하는 방법과,[^p4] 규칙을 지키지 않는 배의 의도를 추론해 피하는 방법을 만들었고,[^p5] 자율운항 연구용 다중 센서 데이터셋을 공개했다.[^p3]

셋째는 **어려운 환경의 항법과 SLAM**이다. SLAM은 로봇이 움직이면서 자기 위치를 추정하는 동시에 주변 지도를 만드는 기술이다. 연구실은 GPS 신호가 닿지 않는 곳의 항법, 해저 지형을 이용한 수중 항법과 SLAM을 연구한다.[^research] 대표 논문에서는 여러 수중 로봇이 느린 음향 통신으로 해저 지도를 나눠 만들 수 있도록 지도 데이터를 압축하는 방법과,[^p1] 계단과 벽이 반복되는 여러 층 건물에서도 흔들리지 않는 라이다(레이저로 거리를 재는 센서) SLAM을 만들었다.[^p2]

넷째는 **다중 로봇 협업과 임무 계획**이다. 여러 로봇의 경로와 작업 할당·일정, 탐색·지도 작성 임무를 위한 정보 기반 경로 계획을 연구한다.[^research] 대표 논문에서는 여러 로봇이 일을 나눠 맡아 전체 임무를 가장 빨리 끝내도록 하는 강화학습 방법을 만들었다.[^p8]

## 주요 연구 주제

### 1. 항법과 SLAM

수중 협업 해저지형 SLAM, 다층 건물 라이다 SLAM.[^p1][^p2] 대표 논문 1, 2.

### 2. 자율운항선박

운하 데이터셋, 좁은 수로 충돌 회피, 규칙 위반 선박 대응.[^p3][^p4][^p5] 대표 논문 3–5.

### 3. 해양 로봇 동역학과 제어

안전 보장 접안 제어, 운하 자율 운항 제어.[^p6][^p7] 대표 논문 6, 7.

### 4. 다중 로봇 협업

다중 로봇 작업 할당.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 국제 학술지 논문 가운데 김진환 교수가 교신저자(랩 표기 *)인 것에서 네 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [ID(O): Mapping Data Quantization for Bathymetric Collaborative SLAM](https://doi.org/10.1109/tro.2025.3641755) · IEEE Transactions on Robotics | 수중 음향 통신은 대역폭이 좁고 느려, 여러 로봇이 해저 지형 지도를 함께 만들 때 데이터를 주고받기 어렵다. 지도를 번호 지도·깊이 지도·방향 지도로 나눠 압축하는 벡터 양자화(데이터를 대표값의 번호로 바꿔 줄이는 방법)를 만들고, 방향 정보는 빼고 보낸 뒤 복원할 때 추정하게 했다. 대규모 해상 시험 자료에서 기존 주성분 분석(데이터를 핵심 축 몇 개로 요약하는 방법) 방식보다 복원 정확도가 약 40% 높았고, 통신 데이터 묶음(패킷)의 40%가 사라져도 견뎠으며, 음향 모뎀 통신망에서 시험한 첫 협업 해저지형 SLAM이다.[^p1] | 1저자 Qianyi Zhang, 교신 김진환 |
| 2 | 2024 | [NV-LIOM: LiDAR-Inertial Odometry and Mapping Using Normal Vectors Towards Robust SLAM in Multifloor Environments](https://doi.org/10.1109/lra.2024.3457373) · IEEE Robotics and Automation Letters | 라이다·관성 센서 위치 추정은 실외에서는 잘 되지만 벽과 계단이 반복되는 여러 층 실내에서는 흔들린다. 라이다 점들에서 표면의 수직 방향(법선 벡터)을 뽑아 점 맞추기에 쓰고, 방향 분포로 맞추기가 불안정한 상황을 가려 불확실성을 조절하며, 벽 너머 잘못된 연결을 피하는 루프 닫기 모듈을 넣었다.[^p2] | 1저자 Dongha Chung, 교신 김진환 |
| 3 | 2023 | [Pohang Canal Dataset: A Multimodal Maritime Dataset for Autonomous Navigation in Restricted Waters](https://doi.org/10.1177/02783649231191145) · International Journal of Robotics Research | 좁은 물길에서의 자율 운항 연구를 위해 스테레오·적외선·전방위 카메라, 라이다 3대, 선박 레이더, GPS, 자세 센서로 포항의 좁은 운하, 내항·외항, 연안을 잇는 7.5 km 경로를 여러 날씨에서 기록한 데이터셋을 만들어 무료로 공개했다.[^p3] | 1저자 Dongha Chung, 교신 김진환 |
| 4 | 2023 | [Autonomous Ship Collision Avoidance in Restricted Waterways Considering Maritime Navigation Rules](https://doi.org/10.1109/joe.2023.3296836) · IEEE Journal of Oceanic Engineering | 수로는 모양이 제각각이라 하나의 충돌 회피 방법을 모두에 쓰기 어렵다. 수로를 따라가는 방향과 가로지르는 방향으로 좌표를 바꿔 모양과 관계없이 다루는 좌표계를 만들고, 그 위에서 해상 교통 규칙을 지키는 자동 충돌 회피 절차를 설계해 여러 수로에서 몬테카를로 모의실험(무작위 조건을 많이 돌려 보는 실험)으로 평가했다.[^p4] | 1저자 Yonghoon Cho, 교신 김진환 |
| 5 | 2022 | [Intent Inference-Based Ship Collision Avoidance in Encounters with Rule-Violating Vessels](https://doi.org/10.1109/lra.2021.3130386) · IEEE Robotics and Automation Letters | 모든 배가 국제 해상충돌예방규칙을 지키지는 않아 위험한 상황이 생긴다. 상대 배의 의도를 추론해 충돌하게 되는 속도를 확률적으로 피하는 방법을 만들고, 규칙 준수와 선제 회피 사이의 균형을 고려해 일대일·다중 선박 조우 상황을 모의실험으로 검증했다.[^p5] | 1저자 Yonghoon Cho, 교신 김진환 |
| 6 | 2024 | [Safety-Guaranteed Ship Berthing Using Cascade Tube-Based Model Predictive Control](https://doi.org/10.1109/tcst.2024.3374152) · IEEE Transactions on Control Systems Technology | 모르는 외란이 일정 범위 안에서 작용할 때 배를 안전하게 부두에 대기 위해, 저속 선박 모델을 앞뒤 방향과 옆·회전 방향 두 부분으로 나누고 각각에 튜브 기반 모델 예측 제어(앞날의 움직임을 예측해 매 순간 조종을 계산하되 외란 범위까지 감안하는 제어)를 계단식으로 적용했다. 배 주변 안전 거리를 고려해 안전 영역을 계산했고, 제어가 계속 가능하고 안정함을 보였다.[^p6] | 1저자 Changyu Lee, 교신 김진환 |
| 7 | 2024 | [Nonlinear Model Predictive Control with Obstacle Avoidance Constraints for Autonomous Navigation in a Canal Environment](https://doi.org/10.1109/tmech.2023.3312672) · IEEE/ASME Transactions on Mechatronics | 포항 운하에서 작은 유람선이 좁은 물길을 스스로 다니도록, 시험 운항 자료로 배의 움직임 모델을 구하고 라이다로 잡은 운하 벽을 선분으로 나타내 장애물 제약으로 넣은 비선형 모델 예측 제어 하나로 경로 계획과 추종을 함께 했다. 실제 운하 주행 실험으로 성능을 확인했다.[^p7] | 1저자 Changyu Lee, 교신 김진환 |
| 8 | 2026 | [Makespan Minimization for Multi-Robot Task Allocation with Balance-Aware Pointerformer](https://doi.org/10.1109/lra.2026.3728333) · IEEE Robotics and Automation Letters | 여러 로봇이 일을 나눠 전체 임무 완료 시간을 줄이는 문제를 트랜스포머 기반 강화학습으로 풀었다. 로봇에 일을 맡기는 순서에 따라 일이 한쪽에 몰리는 문제를 줄이려고 여러 순서를 탐색하고 전체·로봇별 진행 상황을 함께 보게 했다. 작은 문제에서는 시간 제한을 둔 최적화 풀이기와 견줄 만했고, 큰 문제에서는 기존 방법보다 완료 시간이 짧았다.[^p8] | 1저자 Hakmo Son, 교신 김진환 |

## 교수와 전문 분야

김진환 교수는 서울대 조선해양공학과 학사·석사, 미국 스탠퍼드대 항공우주공학 박사(전기공학 부전공)를 받았다. KAIST 기계공학과 교수이며 로봇공학 프로그램과 해양시스템대학원에도 소속돼 있다고 적는다.[^members] 안보과학기술대학원 교수 명단에도 기계공학과 소속으로 올라 있고, 세부 분야를 무인시스템, 이동로봇, 해양로봇, 자율화기술로 적는다.[^gst]

논문으로 보면 전문 분야는 세 갈래다.

- **자율운항선박의 충돌 회피·접안과 모델 예측 제어**.[^p4][^p5][^p6][^p7]
- **수중·실내 항법과 SLAM, 해양 데이터셋**.[^p1][^p2][^p3]
- **다중 로봇 작업 할당**.[^p8]

## 응용 분야

대표 논문으로 보면 자율운항선박과 무인 선박의 운항, 항만 접안 자동화, 수중 탐사·지도 작성, 실내 로봇 항법, 여러 로봇을 쓰는 탐색·지도 작성 임무에 닿아 있다.[^p1][^p2][^p3][^p6][^p8] 졸업생은 국방과학연구소, 선박해양플랜트연구소, 한국기계연구원, 삼성전자, 아비커스, 공주대·한국항공대·인하대·경상국립대·계명대·인천대 등으로 진출했다고 랩이 적는다.[^members]

## 구성원

2026년 10월 20일 랩 People 페이지 기준이다. 괄호의 "w/"는 랩이 이름 옆에 함께 적은 기관이고, 연구 주제와 이메일은 랩이 적은 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyungseo Kim | 박사후연구원 |  | chalseokim@kaist.ac.kr |  |
| Jinwook Park | 박사후연구원 |  | qkrwlsdnr10@kaist.ac.kr | 4 |
| Qianyi Zhang | 박사후연구원 |  | qianyizhang@kaist.ac.kr | 1 |
| Sol Han | 박사과정 | Computer Vision Sensor Fusion | dream4future@kaist.ac.kr |  |
| Kiyong Park | 박사과정 |  | qkrrldyd777@kaist.ac.kr |  |
| Donghyun Kim | 박사과정 |  | rlaehdgusqwe@kaist.ac.kr |  |
| Hakmo Son | 박사과정 |  | gkrah12@kaist.ac.kr | 8 |
| Jisu Jeon | 박사과정 |  | dun04047@kaist.ac.kr |  |
| Dongwook Lee | 박사과정 | Deep Learning UUV SLAM | dongwooklee1201@kaist.ac.kr |  |
| Jiyong Choi | 박사과정 |  | jiyongchoi0702@kaist.ac.kr |  |
| Minju Kang | 박사과정 (w/ KRISO) |  | mkang@kaist.ac.kr |  |
| Keunhwan Kim | 박사과정 (w/ KETI) |  | khgapa@kaist.ac.kr |  |
| Yeongha Shin | 박사과정 | Scene Underst. Decision Making | yeongha.shin@kaist.ac.kr |  |
| Wonseok Oh | 박사과정 (w/ Twinny) | SLAM VLA | ooww0123@kaist.ac.kr |  |
| Kyeongmo Kang | 박사과정 (w/ ROK Navy) |  | kmkang@kaist.ac.kr |  |
| Ju Hang Lee | 박사과정 |  | hangsul@kaist.ac.kr |  |
| Ji Soo Kim | 박사과정 (w/ HD KSOE) | Software-defined Vessel | kimjjs100@kaist.ac.kr |  |
| Tae Woo Lee | 석사과정 | Model Predictive Control | aimer1@kaist.ac.kr |  |
| Kyeonghun Lee | 석사과정 |  | rapael6696@kaist.ac.kr |  |
| Sang Won Park | 석사과정 |  | sangwon0730@kaist.ac.kr |  |
| Taeung Lee | 석사과정 |  | christy201@kaist.ac.kr |  |

## 졸업생

랩 People 페이지 Alumni 표의 이름, 졸업 연도·학위, 진로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyunkuen Cho | 박사 (2026) | Avikus Co. |
| Junwoo Park | 석사 (2026) | Twinny |
| Yonghoe Lee | 석사 (2026) | Samsung Electronics |
| Taekjoong Kwon | 석사 (2026) | Republic of Korea Navy |
| Haggi Do | 박사 (2025) | Korea Institute of Machinery & Materials |
| Changyu Lee | 박사 (2025) | Kongju National University |
| Hoon Chung | 석사 (2025) | MOBINN |
| Junhyung Kim | 석사 (2025) | LG Electronics Inc. |
| Kunchul Hwang | 박사 (2025) | Agency for Defense Development |
| Dongha Chung | 박사 (2024) | URobotics |
| Youngbum Kim | 박사 (2024) | HD Hyundai XiteSolution |
| Jonghwi Kim | 박사 (2024) | Korea Aerospace University |
| Eunghyun Kim | 석사 (2024) | Samsung Electronics |
| Uijong Kim | 석사 (2023) | Agency for Defense Development |
| Jungwoo Han | 석사 (2023) | Honda Research Institute |
| Junwoo Jang | 박사 (2023) | Inha University |
| Jinsik Kim | 석사 (2022) | GINT Co. |
| Wonseok Oh | 석사 (2022) | Twinny |
| Yonghoon Cho | 박사 (2021) | Agency for Defense Development |
| Jisung Park | 박사 (2021) | Gyeongsang National University |
| Seungjo Hong | 석사 (2021) | Republic of Korea Navy |
| David Munk Zino | 석사 (2020) | MAN Energy Solutions |
| Jeonghyeon Wang | 박사 (2020) | Samsung Electronics |
| Keunhwan Kim | 석사 (2020) | Korea Electronics Technology Institute |
| Sukmin Yoon | 박사 (2020) | Agency for Defense Development |
| Seonghun Hong | 박사 (2019) | Keimyung University |
| Jungwook Han | 박사 (2019) | Korea Research Institute of Ships and Ocean Engineering |
| Byunghyun Yoo | 박사 (2019) | Electronics and Telecommunications Research Institute |
| Taeyun Kim | 박사 (2019) | Agency for Defense Development |
| Thorsteinn Baldvin Jonsson | 석사 (2018) | Seoul Robotics |
| Youngshik Kim | 박사 (2018) | Korea Research Institute of Ships and Ocean Engineering |
| Sangwook Woo | 석사 (2017) | Hyundai Construction Equipment |
| Aleixo Cambeiro Barreiro | 석사 (2017) | Fraunhofer Heinrich-Hertz-Institute |
| Soohyun Nam | 박사 (2017) | Samsung Electronics |
| Jaeheon Choe | 박사 (2017) | Incheon National University |
| Yeonjoo Shim | 석사 (2016) | Hyundai Mobis |
| Donghwan Kim | 석사 (2016) | Moais |
| Minju Kang | 석사 (2016) | Korea Research Institute of Ships and Ocean Engineering |
| Jeonghong Park | 박사 (2016) | Korea Research Institute of Ships and Ocean Engineering |
| Sungchur Kwon | 석사 (2015) | EDGE Group |
| Hojang Lee | 석사 (2014) | Defence Agency for Technology and Quality |
| Hyungbae Lee | 석사 (2013) | Hyundai Heavy Industries |
| Younghyun Kim | 석사 (2012) | LIG D&A |
| Quoc Van Tran | 박사후연구원 | Hanoi University of Science and Technology |
| Mohan Santhakumar | 박사후연구원 | Indian Institute of Technology Palakkad |
| Armagan Elibol | 박사후연구원 | Forschungzentrum Jülich |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021년 이후 국제 학술지, 국제 학회([국제학회]), 국내 학술지([국내 학술지]) 논문이다. 저자 이름 뒤 *는 교신저자를 뜻하는 랩 표기다.[^papers]

**2026**

- Hakmo Son, Haggi Do and Jinwhan Kim\*. "Makespan Minimization for Multi-Robot Task Allocation with Balance-Aware Pointerformer". *IEEE Robotics and Automation Letters (RA-L), Early Access, 2026*.
- Sol Han and Jinwhan Kim\*. "CROCS: Camera-Radar Online Alignment via Conic-Section-Constrained Scalar Field Correlation". *IEEE Robotics and Automation Letters (RA-L), Early Access, 2026*.
- Qianyi Zhang and Jinwhan Kim\*. "Terrain-Based Global Tracking Without Prior Pose Information using Multibeam Echosounder Measurements". *IEEE Transactions on Instrumentation and Measurement, Vol. 75, pp. 7506113-7506113, 2026*.
- Yonghoon Cho, Jinwhan Kim and Jonghwi Kim\*. "Motion State Estimation of Maritime Objects with Image-Derived Uncertainty Using a Monocular Camera on Unmanned Surface Vehicles". *IEEE Sensors Journal, Early Access, 2026*.
- Changu Lee, Kiyong Park and Jinwhan Kim\*. "Turning Circle-Based Control Barrier Function for Efficient Collision Avoidance of Nonholonomic Vehicles". *IEEE Transactions on Control Systems Technology, Vol. 34, No. 5, pp. 2813-2820, 2026*.
- Sol Han, Dongwook Lee, Jonghwi Kim and Jinwhan Kim\*. "A Survey on Maritime Perception Datasets and Technologies for Autonomous Surface Vessels". *Intelligent Service Robotics, Vol. 19, No. 25, 2026*.
- Donghyun Kim and Jinwhan Kim\*. "Hierarchical Planning for Vehicle Routing and Scheduling in Marsupial Robotic Systems". *IEEE Robotics and Automation Letters (RA-L), Vol. 11, No. 1, pp. 362-369, 2026*.
- Jiyong Choi and Jinwhan Kim\*. "Data-Driven Modeling of Surface Vehicle Dynamics Using Deep Koopman Networks". *IFAC World Congress, Busan, Korea, Aug. 2026 [국제학회]*.
- Qianyi Zhang and Jinwhan Kim\*. "ID(O): Mapping Data Quantization for Bathymetric Collaborative SLAM". *IEEE International Conference on Robotics and Automation (ICRA), Vienna, Austria, Jun. 2026 (TRO-paper) [국제학회]*.
- Donghyun Kim and Jinwhan Kim\*. "Hierarchical Planning for Vehicle Routing and Scheduling in Marsupial Robotic Systems". *IEEE International Conference on Robotics and Automation (ICRA), Vienna, Austria, Jun. 2026 (RA-L paper) [국제학회]*.
- Taewoo Lee, Kiyong Park and Jinwhan Kim\*. "Physics-Informed Hybrid Dynamics Modeling of High-Speed Autonomous Surface Vehicles". *MTS/IEEE OCEANS, Sanya, China, May 2025 [국제학회]*.

**2025**

- Qianyi Zhang and Jinwhan Kim\*. "ID(O): Mapping Data Quantization for Bathymetric Collaborative SLAM". *IEEE Transactions on Robotics, Vol. 42, pp. 525-544, 2025*.
- Chenming Li, Chengtao Cai, Jinwhan Kim\*, Wentao Zhou\* and Renjie Qiao. "Dbanet: a Dual Branch Aggregation Network for Real-Time Semantic Segmentation of Omnidirectional Images in Maritime Environments". *The Journal of Supercomputing, Vol. 81, Art. 1363, 2025*.
- Jonghwi Kim, Sol Han and Jinwhan Kim\*. "Data Association Leveraging Extrinsic Parameter Consistency for Multi-Object Detection in Maritime Environment". *Mechatronics, Vol. 108, 2025*.
- Kyungseo Kim and Jinwhan Kim\*. "Coordinated Informative Path Planning for Multi-Robot Search in Open Fields". *Journal of Intelligent & Robotic Systems, Vol. 111, No. 2, Art. 65, 2025*.
- Kyungseo Kim, Junwoo Park and Jinwhan Kim\*. "Optimized Area Partitioning for Cooperative Underwater Search Using Multiple Autonomous Underwater Vehicles". *International Journal of Control, Automation, and Systems, Vol. 23, pp. 392-404, 2025*.
- Donghyun Kim and Jinwhan Kim\*. "Efficient Routing and Scheduling for Marsupial USV-AUV System". *IEEE International Symposium on Multi-Robot & Multi-Agent Systems (MRS), Singapore, Dec. 2025 [국제학회]*.
- Yeongha Shin and Jinwhan Kim\*. "Enhancing Navigational Scene Understanding Using Integrated Language Models in Maritime Environments". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, Oct. 2025 [국제학회]*.
- Kyungseo Kim and Jinwhan Kim\*. "Optimizing Coverage Path Planning for Underwater Surveys with Mother Ship-Deployed AUVs". *International Conference on Ubiquitous Robots (UR), College Station, USA, Jun. 2025 [국제학회]*.
- Junhyung Kim and Jinwhan Kim\*. "Semantic Loop Closure for Reducing False Matches in SLAM". *International Conference on Ubiquitous Robots (UR), College Station, USA, Jun. 2025 [국제학회]*.
- Kiyong Park, Changyu Lee and Jinwhan Kim\*. "Robust Trajectory Tracking for Surface Vehicles Via L1-Augmented Model Predictive Control". *MTS/IEEE OCEANS, Brest, France, Jun. 2025 [국제학회]*.
- Dongwook Lee and Jinwhan Kim\*. "Branch Augmented Neural Network for Marine Vessel Re-Identification Using LiDAR Point Cloud". *MTS/IEEE OCEANS, Brest, France, Jun. 2025 [국제학회]*.
- Dongha Chung and Jinwhan Kim\*. "NV-LIOM: LiDAR-Inertial Odometry and Mapping Using Normal Vectors Towards Robust SLAM in Multifloor Environments". *IEEE International Conference on Robotics and Automation (ICRA), Atlanta, USA, Jun. 2025 (RA-L paper) [국제학회]*.
- Qianyi Zhang and Jinwhan Kim\*. "Shape BoW: Generalized Bag of Words for Appearance-Based Loop Closure Detection in Bathymetric SLAM". *IEEE International Conference on Robotics and Automation (ICRA), Atlanta, USA, Jun. 2025 (RA-L paper) [국제학회]*.
- 박진욱, 이찬규, 최지용, 김진환\*. "국제해상규칙이 반영된 속도장애물 기반 제어장벽함수를 활용한 선박 충돌회피 알고리즘". *제어로봇시스템학회 논문지, Vol. 31, No. v, pp. 1271-1276, 2025 [국내 학술지]*.

**2024**

- Junwoo Jang, Haggi Do, Maani Ghaffari and Jinwhan Kim\*. "Efficient Data Collection Strategy for Modeling the Dynamics of Floating Robotic Vehicles Using Neural Networks". *Journal of Intelligent & Robotic Systems, Vol. 110, No. 152, 2024*.
- Dongha Chung and Jinwhan Kim\*. "NV-LIOM: LiDAR-Inertial Odometry and Mapping Using Normal Vectors Towards Robust SLAM in Multifloor Environments". *IEEE Robotics and Automation Letters (RA-L), Vol. 9, No. 11, pp. 9375-9382, 2024*.
- Qianyi Zhang and Jinwhan Kim\*. "Shape BoW: Generalized Bag of Words for Appearance-Based Loop Closure Detection in Bathymetric SLAM". *IEEE Robotics and Automation Letters (RA-L), Vol. 9, No. 9, pp. 7405-7412, 2024*.
- Changyu Lee, Quoc Van Tran and Jinwhan Kim\*. "Safety-Guaranteed Ship Berthing Using Cascade Tube-Based Model Predictive Control". *IEEE Transactions on Control Systems Technology, Vol. 32, No. 4, pp. 1504-1511, 2024*.
- Changyu Lee, Dongha Chung, Jonghwi Kim and Jinwhan Kim\*. "Nonlinear Model Predictive Control with Obstacle Avoidance Constraints for Autonomous Navigation in a Canal Environment". *IEEE/ASME Transactions on Mechatronics, Vol. 29, No. 3, pp. 1985-1996, 2024*.
- Qianyi Zhang and Jinwhan Kim\*. "TTT SLAM: A Feature-Based Bathymetric SLAM Framework". *Ocean Engineering, Vol. 294, 2024*.
- Hakmo Son, Haggi Do and Jinwhan Kim\*. "An Efficient Solution to the Multi-Depot Vehicle Routing Problem Using Reinforcement Learning". *Robot Intelligence Technology and Applications (RITA), Ulsan, Korea, Dec. 2024 [국제학회]*.
- Yeongha Shin, Hanguen Kim and Jinwhan Kim\*. "AnytimeFusion: Parameter-Free RGB Camera-Radar Sensor Fusion Algorithm in Complex Maritime Situations". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Abu Dhabi, UAE, Oct. 2024 [국제학회]*.
- Jinwook Park, Jiyong Choi, Jeonghong Park, Dongjin Yeo and Jinwhan Kim\*. "Experimental Validation of an Intent-Inference-based Ship Collision Avoidance Algorithm". *IFAC Conference on Control Applications in Marine Systems, Robotics, and Vehicles (CAMS), Blacksburg, USA, Sep. 2024 [국제학회]*.
- Haggi Do, Hakmo Son and Jinwhan Kim. "An Efficient Method for Solving Routing Problems with Energy Constraints Using Reinforcement Learning". *International Conference on Ubiquitous Robots (UR), New York, USA, Jun. 2024 [국제학회]*.
- Jonghwi Kim, Changyu Lee, Dongha Chung and Jinwhan Kim\*. "Navigable Area Detection and Perception-Guided Model Predictive Control for Autonomous Navigation in Narrow Waterways". *IEEE International Conference on Robotics and Automation (ICRA), Yokohama, Japan, May 2024 (RA-L paper) [국제학회]*.
- Qianyi Zhang and Jinwhan Kim\*. "Feature-Based Global Localization for Underwater Terrain Aided Navigation Using Bag of Words". *MTS/IEEE OCEANS, Singapore, Apr. 2024 [국제학회]*.
- 김종휘, 김진환\*. "자율운항선박을 위한 인식 및 센싱 기술". *제어로봇시스템학회 논문지, Vol. 30, No. v, pp. 383-393, 2024 [국내 학술지]*.

**2023**

- Jonghwi Kim, Changyu Lee, Dongha Chung, Yonghoon Cho, Jinwhan Kim\*, Wangseok Jang and Saeyong Park. "Field Experiment of Autonomous Ship Navigation in Canal and Surrounding Nearshore Environments". *Journal of Field Robotics, Vol. 41, No. 2, pp. 470-489, 2023*.
- Dongha Chung, Jonghwi Kim, Changyu Lee and Jinwhan Kim\*. "Pohang Canal Dataset: A Multimodal Maritime Dataset for Autonomous Navigation in Restricted Waters". *International Journal of Robotics Research, Vol. 42, No. 12, pp. 1104-1114, 2023*.
- Jonghwi Kim, Changyu Lee, Dongha Chung and Jinwhan Kim\*. "Navigable Area Detection and Perception-Guided Model Predictive Control for Autonomous Navigation in Narrow Waterways". *IEEE Robotics and Automation Letters (RA-L), Vol. 8, No. 9, pp. 5456-5463, 2023*.
- Yonghoon Cho, Jinwook Park, Jonghwi Kim and Jinwhan Kim\*. "Autonomous Ship Collision Avoidance in Restricted Waterways Considering Maritime Navigation Rules". *IEEE Journal of Oceanic Engineering, Vol. 48, No. 4, pp. 1009-1018, 2023*.
- Junwoo Jang, Changyu Lee and Jinwhan Kim\*. "A Learning-Based Approach to Surface Vehicle Dynamics Modeling for Robust Multistep Prediction". *Autonomous Robots, Vol. 47, No. 6, pp. 797-808, 2023*.
- Junwoo Jang, Jungwoo Han and Jinwhan Kim\*. "K-Mixup: Data Augmentation for Offline Reinforcement Learning Using Mixup in a Koopman Invariant Subspace". *Expert Systems with Applications, Vol. 225, 2023*.
- Changyu Lee and Jinwhan Kim\*. "Model Predictive Anti-Spin Thruster Control for Efficient Ship Propulsion in Irregular Waves". *Control Engineering Practice, Vol. 136, 2023*.
- Quoc Van Tran, Changyu Lee, Jinwhan Kim and H. Q. Nguyen. "Robust Bearing-Based Formation Tracking Control of Underactuated Surface Vessels: an Output Regulation Approach". *IEEE Transactions on Control of Network Systems, Vol. 10, No. 4, 2023*.
- Junwoo Jang and Jinwhan Kim\*. "Hydrodynamic Modeling of a Robotic Surface Vehicle Using Representation Learning for Long- Term Prediction". *Ocean Engineering, Vol. 270, 2023*.
- Jonghwi Kim, Yonghoon Cho and Jinwhan Kim\*. "Urban Localization Based on Aerial Imagery by Correcting Projection Distortion". *Autonomous Robots, Vol. 47, No. 3, pp. 299-312, 2023*.
- Seonghun Hong and Jinwhan Kim. "Three-Dimensional Visual Mapping of Underwater Ship Hull Surface Using Image Stitching Geometry". *Ocean Engineering, Vol. 269, 2023*.
- Dongha Chung and Jinwhan Kim\*. "Underwater Visual Mapping of Curved Ship Hull Surface Using Stereo Vision". *Autonomous Robots, Vol. 47, pp. 109-120, 2023*.
- Changyu Lee, Kiyong Park and Jinwhan Kim\*. "Parameter-Varying Koopman Operator for Nonlinear System Modeling and Control". *62nd IEEE Conference on Decision and Control (CDC), Singapore, Dec. 2023 [국제학회]*.
- Jinwook Park, Changyu Lee and Jinwhan Kim\*. "Robust Ship Berthing Control with Wind Disturbance Compensation Using Reachability Analysis". *IFAC World Congress, Yokohama, Japan, Jul. 2023 [국제학회]*.
- Kiyong Park, Changyu Lee and Jinwhan Kim\*. "Robust Path Tracking and Obstacle Avoidance of Autonomous Ship Using Stochastic Model Predictive Control". *International Conference on Ubiquitous Robots (UR), Hawaii, USA, Jun. 2023 [국제학회]*.
- Eunghyun Kim, Jonghwi Kim and Jinwhan Kim\*. "Multi-Target Tracking Considering the Uncertainty of Deep Learning-Based Object Detection of Marine Radar Images". *International Conference on Ubiquitous Robots (UR), Hawaii, USA, Jun. 2023 [국제학회]*.
- Hyunkeun Cho and Jinwhan Kim\*. "Marine Radar-Based Coastal SLAM with Occupancy Grid Mapping". *MTS/IEEE OCEANS, Limerick, Ireland, Jun. 2023 [국제학회]*.
- Donghyun Kim and Jinwhan Kim\*. "Mission Planning for Collaborative Operations of Autonomous Marine Systems". *MTS/IEEE OCEANS, Limerick, Ireland, Jun. 2023 [국제학회]*.
- Keunhwan Kim, Jonghwi Kim and Jinwhan Kim\*. "Robust Data Association for Multi-Object Detection in Maritime Environments Using Camera and Radar Measurements". *IEEE International Conference on Robotics and Automation (ICRA), London, UK, May 2024 (RA-L paper) [국제학회]*.
- 이찬규, 김진환\*. "Trajectory Optimization for Autonomous Berthing of a Twin-Propeller Twin-Rudder Ship". *한국해양공학회 논문지, Vol. 37, No. 3, pp. 122-128, 2023 [국내 학술지]*.

**2022**

- Jisung Park and Jinwhan Kim\*. "Robust Underwater Localization Using Acoustic Image Alignment for Autonomous Intervention Systems". *IEEE Access, Vol. 10, pp. 58447-58457, 2022*.
- Jisung Park and JInwhan Kim\*. "Underwater Localization Using an Optic and Acoustic Stereo Imaging System for Autonomous Intervention Robots". *Electronics Letters, Vol. 58, No. 15, 2022*.
- Sukmin Yoon, Haggi Do and Jinwhan Kim\*. "Robust Task Allocation for Multiple Cooperative Robotic Vehicles Considering Node Position Uncertainty". *Journal of Intelligent & Robotic Systems, Vol. 106, No. 23, 2022*.
- Junwoo Jang, Changyu Lee and Jinwhan Kim\*. "Ambiguity Resolution Between Constant Velocity and Coordinated Turn Models for Multimodel Target Tracking". *IEEE Sensors Letters, Vol. 6, No. 5, 2022*.
- Junwoo Jang and Jinwhan Kim\*. "Topographic SLAM Using a Single Terrain Altimeter in GNSS-Restricted Environment". *IEEE Access, Vol. 10, pp. 10806-10815, 2022*.
- Quoc Van Tran\* and Jinwhan Kim. "Bearing-Constrained Formation Tracking Control of Nonholonomic Agents without Inter-Agent Communication". *IEEE Control Systems Letters (L-CSS), Vol. 6, pp. 2401-2406, 2022*.
- Yonghoon Cho, Jonghwi Kim and Jinwhan Kim\*. "Intent Inference-Based Ship Collision Avoidance in Encounters with Rule-Violating Vessels". *IEEE Robotics and Automation Letters (RA-L), Vol. 7, No. 1, pp. 518-525, 2022*.
- Jungwoo Han and Jinwhan Kim\*. "Data Augmentation of Selective Subspace to Improve the Performance of Offline Reinforcement Learning". *22th International Conference on Control, Automation and Systems (ICCAS 2022), Busan, Korea, Nov. 2022 [국제학회]*.
- Changyu Lee, Quoc Van Tran and Jinwhan Kim\*. "Robust Path Tracking and Obstacle Avoidance Using Tube-Based Model Predictive Control for Surface Vehicles". *IFAC Conference on Control Applications in Marine Systems, Robotics, and Vehicles (CAMS), and Vehicles (CAMS), Copenhagen, Denmark, Sep. 2022 [국제학회]*.
- Junwoo Jang and Jinwhan Kim\*. "Hydrodynamics Modeling of a Surface Robotic Vehicle Using Computationally-Efficient Variations of Gaussian Processes". *IFAC Conference on Control Applications in Marine Systems, Robotics, and Vehicles (CAMS), and Vehicles (CAMS), Copenhagen, Denmark, Sep. 2022 [국제학회]*.
- Quoc Van Tran\*, Hyo-Sung Ahn and Jinwhan Kim. "Direction-Only Orientation Alignment of Leader-Follower Networks". *American Control Conference (ACC), Atlanta, USA, Jun. 2022 [국제학회]*.
- 박진욱, 김진식, 김진환\*, 김용명, 이문진. "HNS 광역 탐지 및 모니터링을 위한 부유식 무인시스템의 실험적 성능 검증". *해양환경안전학회지, Vol. 28, No. S, pp. 11-17, 2022 [국내 학술지]*.
- 김종휘, 조용훈, 한솔, 김진환\*. "딥러닝 기반 객체 탐지 결과의 불확실성을 고려한 자동 선박 탐지 및 추적". *제어로봇시스템학회 논문지, Vol. 28, No. 6, pp. 529-535, 2022 [국내 학술지]*.
- 장준우, 도학기, 김진환\*. "해양 무인 이동체 기반의 수중 탐사를 위한 임무 계획". *한국해양공학회 논문지, Vol. 36, pp. 41-49, 2022 [국내 학술지]*.

**2021**

- Keunhwan Kim, Jonghwi Kim and Jinwhan Kim\*. "Robust Data Association for Multi-Object Detection in Maritime Environments Using Camera and Radar Measurements". *IEEE Robotics and Automation Letters (RA-L), Vol. 6, No. 3, pp. 5865-5872, 2021*.
- Hangil Joe, Hyeonwoo Cho, Minsung Sung, Jinwhan Kim and Son-cheol Yu\*. "Sensor Fusion of Two Sonar Devices for Underwater 3D Mapping with an AUV". *Autonomous Robots, Vol. 45, pp. 543-569, 2021*.
- Young-Shik Kim and Jinwhan Kim\*. "Icevaning Control of an Arctic Offshore Vessel and Its Experimental Validation". *International Journal of Naval Architecture and Ocean Engineering, Vol. 13, pp. 208-222, 2021*.
- Jungwook Han\*, Sun-Young Kim and Jinwhan Kim. "Enhanced Target Ship Tracking with Geometric Parameter Estimation for Unmanned Surface Vehicles". *IEEE Access, Vol. 9, pp. 39864-39872, 2021*.
- Yonghoon Cho, Jonghwi Kim and Jinwhan Kim\*. "Intent Inference of Ship Collision Avoidance Behavior under Maritime Traffic Rules". *IEEE Access, Vol. 9, pp. 5598-5608, 2021*.
- Kyungseo Kim and Jinwhan Kim\*. "Path Optimization for Cooperative Mapping Using Multiple Robots with Limited Sensing Capabilities". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Prague, Czech Republic, Sep. 2021 [국제학회]*.
- Keunhwan Kim, Jonghwi Kim and Jinwhan Kim\*. "Robust Data Association for Multi-Object Detection in Maritime Environments Using Camera and Radar Measurements". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Prague, Czech Republic, Sep. 2021 [국제학회]*.
- Changyu Lee and Jinwhan Kim\*. "Energy Efficient Control for Electric Ship Propulsion Considering Thrust Fluctuation in Regular Waves". *IFAC Conference on Control Applications in Marine Systems, Robotics, and Vehicles (CAMS), and Vehicles (CAMS), Oldenburg, Germany, Sep. 2021 [국제학회]*.
- Yonghoon Cho, Jonghwi Kim and Jinwhan Kim\*. "COLREG-compliant Ship Collision Avoidance in Narrow Channels Using Curvilinear Coordinates". *IFAC Conference on Control Applications in Marine Systems, Robotics, and Vehicles (CAMS), and Vehicles (CAMS), Oldenburg, Germany, Sep. 2021 [국제학회]*.
- 최현택\*, 박정홍, 최진우, 강민주, 이영준, 정종대, 김종휘, 권혁준, 김진환, 윤국진, 김한근, 박상태. "인공지능 기술에 기반한 자율운항선박의 새로운 상황인식 시스템의 설계와 초기 결과". *제어로봇시스템학회 논문지, Vol. 27, No. 8, 2021 [국내 학술지]*.
- 조용훈, 김종휘, 김진환\*. "곡선좌표계 변환에 기반한 협수로에서 선박 자율 충돌회피". *대한조선학회 논문집, Vol. 58, No. 3, 2021 [국내 학술지]*.

## 연락과 위치

- 연구실: KAIST 실습동(N9) 4170호[^contact]
- 교수 이메일: jinwhan@kaist.ac.kr[^home]

[^home]: MORIN Lab 누리집 첫 화면 <https://kaistmorin.github.io/> (2026-10-20 열람)
[^research]: MORIN Lab Research 페이지 <https://kaistmorin.github.io/research/> (2026-10-20 열람)
[^members]: MORIN Lab People 페이지 <https://kaistmorin.github.io/people/> (2026-10-20 열람)
[^papers]: MORIN Lab Publications 페이지(페이지에 들어 있는 논문 데이터) <https://kaistmorin.github.io/publications/> (2026-10-20 열람)
[^contact]: MORIN Lab Contact 페이지 <https://kaistmorin.github.io/contact/> (2026-10-20 열람)
[^gst]: KAIST 안보과학기술대학원 교수 명단 1쪽 <https://gst.kaist.ac.kr/member/faculty/> (2026-10-20 열람)
[^p1]: Q. Zhang, J. Kim, IEEE Transactions on Robotics 42, 525-544 (2026). <https://doi.org/10.1109/tro.2025.3641755> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: D. Chung, J. Kim, IEEE Robotics and Automation Letters 9, 9375-9382 (2024). <https://doi.org/10.1109/lra.2024.3457373> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Chung, J. Kim, C. Lee, J. Kim, The International Journal of Robotics Research 42, 1104-1114 (온라인 2023-08-21). <https://doi.org/10.1177/02783649231191145> 초록 기준.
[^p4]: Y. Cho, J. Park, J. Kim, J. Kim, IEEE Journal of Oceanic Engineering 48, 1009-1018 (2023). <https://doi.org/10.1109/joe.2023.3296836> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Cho, J. Kim, J. Kim, IEEE Robotics and Automation Letters 7, 518-525 (2022). <https://doi.org/10.1109/lra.2021.3130386> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: C. Lee, Q. V. Tran, J. Kim, IEEE Transactions on Control Systems Technology 32, 1504-1511 (2024). <https://doi.org/10.1109/tcst.2024.3374152> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: C. Lee, D. Chung, J. Kim, J. Kim, IEEE/ASME Transactions on Mechatronics 29, 1985-1996 (2024). <https://doi.org/10.1109/tmech.2023.3312672> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Son, H. Do, J. Kim, IEEE Robotics and Automation Letters 11, 11944-11951 (2026). <https://doi.org/10.1109/lra.2026.3728333> 초록 기준(Semantic Scholar 등록 초록).

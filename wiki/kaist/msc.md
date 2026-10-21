# 메카트로닉스·시스템·제어 연구실 (Mechatronics, Systems and Control Laboratory, MSC Lab)

**KAIST 기계공학과 · 김경수 교수**

- 분야: 전기차 모터 제어, 배터리 관리 시스템(충전 상태 추정, 셀 밸런싱), 자율주행(인지·경로 계획·주행 안정성 제어), 다리 달린 로봇·휴머노이드 제어와 상태 추정, 힘·토크 센서, 의수
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 전기차[^research][^p1], 배터리 관리 시스템[^p2][^p3][^research], 자율주행[^p4][^p5][^research], 보행·휴머노이드 로봇[^research][^p6][^p7], 재활·보조·접근성 기술[^p8], 강화학습[^research], 로봇 구동기·센서[^p7]
- 홈페이지: <https://msc.kaist.ac.kr/>
- 근거와 출처: [MSC Lab 근거 페이지](msc-sources.md)

> 전기차를 움직이는 모터와 배터리를 똑똑하게 제어하고, 차와 로봇이 스스로 보고 판단해 안전하게 움직이도록 만드는 연구실이다. 네 발 로봇과 휴머노이드, 로봇 의수, 로봇용 힘 센서까지 기계와 전자·제어를 엮은 시스템을 직접 만든다.[^home][^research]

## 무엇을 연구하나

연구실은 통합 설계와 고급 제어, 스마트 자동화로 지능형 기계 시스템을 만든다고 소개하며, 연구 주제를 모터 제어, 배터리 관리 시스템, 모빌리티, 로봇의 네 가지로 든다.[^home] 연구는 전기 구동계 제어 그룹과 인지·제어 그룹으로 나뉜다.[^research]

**모터 제어**에서는 전기차에 쓰는 영구자석 동기 전동기(PMSM)를 효율 높게, 극한 조건에서도 안정적으로 돌리는 방법을 연구한다. 고효율 제어, 고속 영역 제어(약계자 제어), 최적 토크 제어, 외란 관측기를 쓴 강인한 전류 제어, 신경망으로 모터 특성 지도를 갱신하는 방법이 여기에 들며, 수소연료전지 트랙터 같은 응용 장비도 다룬다.[^research] 대표 논문에서는 계산량을 크게 줄이고 조정할 계수도 없앤 모델 예측 토크 제어(앞으로의 움직임을 예측해 매 순간 최적의 토크 명령을 계산하는 제어)를 만들었다.[^p1]

**배터리 관리 시스템**에서는 배터리에 남은 전기의 비율(충전 상태, SOC)과 온도·출력 가능 전력을 정확히 추정하고, 병렬로 이은 셀의 충전을 고르게 하며, 셀 밸런싱(직렬로 이은 셀들의 충전량을 맞추는 일)을 연구한다. 침지 냉각, 100kWh급 에너지 저장 차량, 저궤도 위성용 배터리 관리도 다룬다.[^research] 대표 논문에서는 배터리가 낡아도 정확한 충전 상태 추정 방법과,[^p2] 작은 신경망으로 셀 밸런싱을 규칙 기반 제어보다 빠르게 하는 방법을 만들었다.[^p3]

**모빌리티**에서는 자율주행차의 인지(위치 추정과 지도 작성, 센서 융합으로 물체 속도·위치 추정, 4D 레이더 데이터셋, 차선 인식), 경로 계획, 노면 마찰 추정·긴급 제동·차체 자세 제어를 연구한다.[^research] 대표 논문에서는 GPU로 여러 경로를 동시에 최적화해 복잡한 도심에서도 안전한 경로를 짜는 방법과,[^p4] 레이더와 카메라를 합쳐 주변 물체의 실제 속도를 추정하는 방법을 만들었다.[^p5]

**로봇**에서는 네 발 로봇, 휴머노이드, 자율이동로봇, 산업용 로봇팔과 로봇 손을 대상으로 불확실성 속 상태 추정, 제약과 외란을 고려한 동작 계획과 강인한 제어, 강화학습과 시각-언어-행동(VLA) 모델 같은 AI 방법을 연구한다.[^research] 대표 논문에서는 발이 미끄러질 때 생기는 위치 추정 오차를 신경망으로 보정하는 방법,[^p6] 충격에 강한 광학식 6축 힘·토크 센서,[^p7] 빠르고 힘센 로봇 의수를 만들었다.[^p8]

## 주요 연구 주제

### 1. 모터 제어

계산 효율 높은 모델 예측 토크 제어.[^p1] 대표 논문 1.

### 2. 배터리 관리 시스템

강인한 충전 상태 추정, 신경망 셀 밸런싱.[^p2][^p3] 대표 논문 2, 3.

### 3. 자율주행 모빌리티

병렬 경로 최적화, 레이더-카메라 속도 추정.[^p4][^p5] 대표 논문 4, 5.

### 4. 로봇

다리 달린 로봇 상태 추정, 힘·토크 센서, 로봇 의수.[^p6][^p7][^p8] 대표 논문 6–8.

## 대표 논문

랩 논문 게시판의 2021–2026년 논문 가운데 김경수 교수가 마지막 저자인 것에서 네 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2021 | [Computationally efficient model predictive torque control of permanent magnet synchronous machines using numerical techniques](https://doi.org/10.1109/tcst.2021.3113045) · IEEE Transactions on Control Systems Technology | 기존 모델 예측 토크 제어는 복잡한 최적화 문제를 반복해서 풀어야 해 계산이 무거웠다. 문제를 두 부분 문제로 나누고 토크 식과 전류 제약을 선형화해 답을 바로 구하는 방식으로 계산 부담을 크게 줄였고, 조정할 제어 계수나 가중치가 없어 튜닝이 필요 없다. 4 kW 모터 구동 장치 실험으로 기존 방법과 비교해 성능과 계산 효율을 확인했다.[^p1] | 1저자 K. Choi, 마지막 저자 김경수 |
| 2 | 2021 | [A robust state of charge estimation approach based on nonlinear battery cell model for lithium-ion batteries in electric vehicles](https://doi.org/10.1109/tvt.2021.3079934) · IEEE Transactions on Vehicular Technology | 순수 전기차와 하이브리드차의 리튬이온 배터리에서 모델의 불확실성과 특성 변화에도 흔들리지 않는 충전 상태 추정기를 설계하고 안정성을 분석했다. 노화 정도가 다른 원통형 셀 두 개로 두 운전 방식에서 실험해, 셀이 낡아도 정확하게 추정함을 보였다.[^p2] | 1저자 W. Kim, 마지막 저자 김경수 |
| 3 | 2026 | [Lightweight Neural Network-Based Cell Balancing Using Variable Effective Resistance](https://doi.org/10.1109/access.2026.3735378) · IEEE Access | 셀마다 붙은 방전 저항을 빠르게 켜고 끄는 방식(PWM)으로 실제 저항값을 바꾸고, 작은 신경망이 다섯 셀의 충전 상태를 보고 각 저항의 켜짐 비율을 정하게 했다. 모의실험에서 마지막 충전 상태 편차를 0.49%p에서 0.04%p로 줄이고 밸런싱 시간을 규칙 기반 제어보다 36.6% 줄였으며, 좁은 범위로 학습한 신경망을 마이크로컨트롤러 시제품에 넣어 감지부터 구동까지 전체 동작을 확인했다. 회로를 바꾸지 않는 소프트웨어 개선이다.[^p3] | 1저자 T. Lee, 마지막 저자 김경수 |
| 4 | 2024 | [Gpu-enabled parallel trajectory optimization framework for safe motion planning of autonomous vehicles](https://doi.org/10.1109/lra.2024.3471452) · IEEE Robotics and Automation Letters | 무작위로 여러 경로를 뽑는 방식과 기울기로 매끄러운 경로를 다듬는 방식을 합쳐, GPU로 많은 후보 경로를 동시에 최적화한 뒤 가장 좋은 것을 고르는 자율주행 경로 계획 틀을 만들었다. 안전 제약을 장벽 함수로 넣었고, 복잡한 도심 환경에서도 더 나은 경로와 더 정확한 제어를 보였다.[^p4] | 1저자 Y. Lee, 마지막 저자 김경수 |
| 5 | 2025 | [POW4R: POint-Wise full-velocity estimation using 4 d Radar-camera fusion beyond radial limitations](https://doi.org/10.1109/lra.2025.3606356) · IEEE Robotics and Automation Letters | 4D 레이더는 물체가 다가오거나 멀어지는 방향의 속도만 잰다. 이를 카메라 영상에서 뽑은 움직임 정보(광류, 영상 속 물체가 움직인 방향과 크기)와 합쳐 물체의 전체 속도 벡터를 추정하는 방법을 만들고 실제 차량에 탑재해 시험했다. 속도 추정 오차율이 기준 방법 81%에서 31%로 줄었다.[^p5] | 1저자 H. Y. Jeon, 마지막 저자 김경수 |
| 6 | 2026 | [Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation](https://doi.org/10.1109/lra.2026.3664311) · IEEE Robotics and Automation Letters | 다리 달린 로봇은 발이 미끄러지면 "발은 미끄러지지 않는다"는 가정이 깨져 위치 추정에 오차가 쌓인다. 센서와 모델을 섞어 상태를 추정하는 칼만 필터에, 미끄러짐 정도에 따른 오차를 어텐션 신경망(입력 중 중요한 부분에 가중치를 두는 신경망)으로 추정해 보정하는 모듈을 붙여 미끄러운 조건에서 기존 방법보다 나은 성능을 냈다.[^p6] | 1저자 S. Lee, 마지막 저자 김경수 |
| 7 | 2025 | [Compact and Optimized Optical Six-Axis Force/Torque Sensor for Legged Robots](https://doi.org/10.1109/tim.2025.3618428) · IEEE Transactions on Instrumentation and Measurement | 다리 달린 로봇의 힘 센서는 평소 지면 반력의 세 배가 넘는 충격을 견뎌야 한다. 변형 게이지 대신 빛 센서(포토커플러)로 닿지 않고 재는 작고 가벼운 6축 힘·토크 센서를 만들고, 감도는 높이고 오차는 줄이는 최적 설계 변수를 찾아 네 발 로봇에 달아 시험했다.[^p7] | 1저자 H. B. Kim, 마지막 저자 김경수 |
| 8 | 2022 | [The MSC prosthetic hand: Rapid, powerful, and intuitive](https://doi.org/10.1109/lra.2022.3140444) · IEEE Robotics and Automation Letters | 의수는 무겁고 힘이 약하며 조종이 불편하다. 줄을 꼬아 당기는 구동기로 0.8초 만에 쥐고 45 N의 집는 힘을 내면서 무게는 390 g인 의수를 만들고, 피부 근전도(근육이 움직일 때 나는 전기 신호)와 학습 모델로 손가락마다 의도를 추정해 여러 손가락을 동시에 조종하게 했다.[^p8] | 1저자 Y. Cho, 마지막 저자 김경수 |

## 교수와 전문 분야

김경수 교수는 KAIST 기계공학과에서 학사(1993)·석사(1995)·박사(1999)를 받았다. LG전자 디지털미디어연구소 책임연구원(1999–2003), ST마이크로일렉트로닉스 멀티미디어기술센터 그룹장(2003–2005), 한국산업기술대 기계공학과 교수(2005–2007)를 거쳐 2007년부터 KAIST 기계공학과 교수다. Cho Chun Shik Graduate School of Mobility 원장(2015–2021), Eco-Friendly Smart Vehicle Research Center 센터장(2017–2021), KAIST 기획처장(2021–2024)을 지냈고, 2022년부터 KAIST Mobility Research Center 센터장, 2024년부터 Next-Generation ESS Research Center 센터장을 맡고 있다. 2024년 3월부터 2026년 8월까지 KAIST 대외부총장(랩 영문 표기 Vice President for Planning and Budget)을 지냈다고 적는다.[^prof]

연구 관심사로는 강인 제어·가변구조 제어·외란 추정과 보상·모터 제어, 공압·유압 구동과 힘·토크 센서 설계, 로봇 손·보행 로봇·로봇팔, 전동식 조향·하이브리드 구동계·전기차·자율주행차를 든다. 수상으로는 2025년 대한민국 국회공로장 교육위원장상, International Conference on Advanced Intelligent Mechatronics Best Student Paper Award(2009, 2016), 제어로봇시스템학회(Institute of Control, Robotics and Systems) Best Paper Award(2008, 2009) 등을 적는다.[^prof]

논문으로 보면 전문 분야는 세 갈래다.

- **전기 구동계 제어와 배터리 상태 추정**.[^p1][^p2][^p3]
- **자율주행차의 경로 계획과 센서 융합 인지**.[^p4][^p5]
- **다리 달린 로봇·의수의 센서, 추정, 제어**.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 과제로 보면 전기차·전기버스의 모터와 배터리, 에너지 저장 장치, 자율주행차의 안전 기능, 자율이동로봇, 휴머노이드, 의수, 국방용 유무인 복합 체계 훈련 시뮬레이션에 닿아 있다.[^p1][^p3][^p4][^p8][^home] 연구실은 LS일렉트릭, 한국기계연구원, 농촌진흥청, 한국연구재단, 산업통상부 등의 과제와 특허 출원·등록을 적는다.[^home][^patents] 2021년 이후 졸업생은 현대자동차, LG에너지솔루션, 삼성전자, 삼성리서치, LS일렉트릭 등으로 진출했고, 한양대 ERICA와 경기대 교수가 된 졸업생도 있다고 랩이 적는다.[^alumni]

## 구성원

2026년 10월 20일 랩 Members 게시판 기준이다. 이름은 랩 표기(국문과 영문)를 따랐고, 연구 관심사는 랩이 적은 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| 김현빈 (Hyun-Bin Kim) | 박사후연구원 | Force/Torque sensors, Legged robot control, Robot design, Mechatronics systems | 7 |
| 이상민 (Sangmin Lee) | 박사과정 | Eco-friendly powertrain control |  |
| 김찬석 (Chanseok Kim) | 박사과정 | Language-driven Robotics, Embodied Task Planning |  |
| 오상윤 (Sangyoon Oh) | 박사과정 | Autonomous Driving, 3D perception | 5 |
| 이병욱 (Byungwook Lee) | 박사과정 | prosthetic hand |  |
| 최효서 | 박사과정 | Motor Control |  |
| 양승훈 (Seunghoon Yang) | 박사과정 | autonomous driving, semantic segmentation, SLAM | 5 |
| 권성진 (Seongjin Kwon) | 박사과정 | Fixed-wing UAV, Reinforcement Learning, Platoon Control |  |
| 이정태 (Jeongtae Lee) | 박사과정 | control, learning |  |
| 함병일 (Byeong-Il Ham) | 박사과정 | Legged robot, Optimal control, Motion planning | 7 |
| 박진호 (Jinho Park) | 박사과정 | Autonomous Mobile Robot, Optimal Control |  |
| 이석주 (Seokju Lee) | 박사과정 | legged robotics, learning, control | 6 |
| 권준수 (Junsu Kwon) | 박사과정 | Autonomous Driving, Collision Avoidance, Stability Control |  |
| 백현민 (Hyeonmin Baek) | 박사과정 | Battery Management System, State Estimation, Immersion Cooling | 3 |
| 김산 (San Kim) | 박사과정 | Motor Control, Permanent Magnetic Synchronous Motor, Fault Diagnosis |  |
| 이경호 (Gyungho Lee) | 석사과정 | Autonomous Driving, Reinforcement Learning |  |
| 전찬형 (Chanhyeong Jeon) | 석사과정 | Autonomous Driving, Path Planning |  |
| 강동윤 (Dongyun Kang) | 석사과정 | Autonomous Driving, Computer Vision |  |
| 정승호 (Seungho Jung) | 석사과정 | Motor Control, Electric Vehicle Control |  |
| 임정혁 (Jeonghyeok Lim) | 석사과정 | Humanoid |  |
| 김경수 (Kyoungsoo Kim) | 인턴 | Humanoid, Reinforcement Learning |  |
| 이시은 (Sieun Lee) | 인턴 | BMS Control |  |
| 전영호 (Yeongho Jeon) | 인턴 | Legged Robotics, Control |  |

## 졸업생

랩 Alumni 게시판의 2021년 이후 졸업생 이름, 학위·졸업 시기, 진로, 학위 논문 제목이다. 진로의 R.O.K.A.는 대한민국 육군을 뜻하는 랩 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 유재민 (Jaemin Yu) | Aug.2026 | LS Electric | Development of Electrical Arc Detection Algorithm Using Wavelet Transform |
| 전현용 | Feb. 2026 | R.O.K.A | 4D Radar-Camera Fusion Based Full-Velocity Estimation for Autonomous Driving Vehicles |
| 이태훈 (Taehun Lee) | M.S. Feb. 2026 | R.O.K.A. | Lightweight neural network-based cell balancing using variable effective resistance |
| 이영석 (Yeongseok Lee) | Ph.D. Aug. 2025 | DIDEN Robotics | Motion planning with batch trajectory optimization for autonomous driving in cluttered environment |
| 임세영 (Se-Yeong Im) | M.S. Feb. 2025 | Hyundai Motors | Methodology for estimating voltage source inverter nonlinearity and permanent magnet synchronous motor parameters using temperature sensor and current ripple dynamics |
| 장병관 (Byeonggwan Jang) | Ph.D. Feb. 2025 | LG Energy Solution | Novel charging control strategy for battery systems to minimize variations among parallel-connected batteries |
| 김현빈 (Hyun-Bin Kim) | Ph.D. Feb. 2025 | KAIST Researcher | Compact design of 6-axis force/torque sensor for legged robots using photo-couplers |
| 한승호 (Seungho Han) | Ph.D. Aug. 2024 | Hanyang University ERICA Professor | Collision avoidance of autonomous driving under object and environmental uncertainty |
| 김상현 (Sanghyun Kim) | Ph.D. Aug. 2024 | R.O.K.A. | Study of aerodynamics and energy efficiency characteristics of morphing-wing structure for small vertical take-off and landing unmanned aerial vehicles |
| 박수범 (Subeom Park) | M.S. Feb. 2024 | Clobot | Hybrid A-Star based nonlinear model predictive control for collision avoidance of autonomous vehicles |
| 허미라 (Mira Heo) | Ph.D. Feb. 2024 | R.O.K.A. | Study on machine learning based smartphone colorimetric analysis for concentration prediction of mixed heavy metals |
| 최민성 (Minseong Choi) | Ph.D. Feb. 2024 | Kyonggi University, Professor | Research on vector map SLAM for autonomous driving via camera and 4D radar |
| 조민수 (Minsu Cho) | Ph.D. Feb. 2024 | Samsung Electronics | Risk-aware motion planning with CVaR maps for collision avoidance in dynamic environments |
| 정유진 (Eugene Jeong) | Ph.D. Feb. 2024 | Samsung Electronics | A study on a novel fNIRS/EEG hybrid sensor system for brain cognition |
| 전영준 (Youngjun Jeon) | Ph.D. Feb. 2024 | Hyundai Motors | Study on real-time identification of plastic objects using visible light and near-infrared hyperspectral image |
| 강정욱 (Jeonguk Kang) | Ph.D. Feb. 2024 | Samsung Research | Robust locomotion control of legged robots via graph optimization-based disturbance estimation |
| Bangunharcana, Antyanta | Ph.D. Feb. 2024 | Motional | Long term visual localization via image graph feature matching and adaptive generalized depth-pose optimization |
| 오승수 | M.S. Feb. 2023 | R.O.K.A. | Study on the improvement of maneuverability, agility, and power consumption according to the flight environment to verify bio-inspired morphing wing unmanned aerial vehicle flight capability |
| 김한길 | M.S. Feb. 2023 |  | Estimation of finger flexion/extension intention for simultaneous and proportional control of multi-DOF prosthetic hand using sEMG |
| 김지우 | M.S. Feb. 2023 | Hyundai Motors | Path tracking and adaptive cruise control considering vehicle mass and road gradient |
| 엄상우 | Ph.D. 2023 | Samsung Electronics | Study of suction location decision and rapid manipulation trajectory generation algorithm for plastic waste sorting robot |
| 서민석 | Ph.D. 2023 | K-Lab | fNIRS Signal Classification Using Graph Representation for Brain-Computer Interface |
| 김장헌 | Ph.D. 2023 | Samsung Electronics | A study on the estimation of blood glucose level in the human body through diffuse reflectance spectroscopy using visible-near infrared band |
| 조진우 | M.S. 2022 |  | Data augmentation based on deep learning for infrared object detection in autonomous vehicle |
| 손동효 | M.S. 2022 | Hyundai Motors | Study on the feature map fusion module between image and point cloud for 3D object detection |
| 변성미 | M.S. 2022 | Samsung Research | Channel, spatial and temporal separated 3D convolution for deep 3D CNN |
| 조영걸 | Ph.D. 2022 | Imperial College London Post-Doc. | Development of a robust intention estimation algorithm and rehabilitation technique based on muscle activation for prosthetic hand control |
| 조시훈 | Ph.D. 2022 | Agency for Defense Development(ADD) | Study on novel index to assess health state of battery module considering cell inconsistency |
| 장유현 | Ph.D. 2022 |  | Study on the stable walking technique of a quadruped robot for moving in a nuclear power plant rough environment |
| 박지일 | Ph.D. 2022 | Incheon University Researcher | Development of autonomous driving sensing system capable of real-time weather condition recognition and object detection/tracking in snowy weather |
| 김동현 | Ph.D. 2022 | Samsung Electronics | Under-constrained walking algorithm for hybrid actuated biped robot |
| 강대원 | Ph.D. 2022 | K-Lab | Thermal degradation-resistant CNT saturable absorber for mode-locked fiber laser and basic application |
| Shyam, Pranjay | Ph.D. 2022 | Amazon | Robust holistic scene understanding via multi-task learning and sensor fusion |
| 부준호 | M.S. 2021 | Engel Robotics | Dynamic modeling and control of Mckibben actuator |
| 김하준 | M.S. 2021 | R.O.K.A | Real-time object tracking algorithm based on pixel and GPS coordinates for lightweight mobile surveillance platform |
| 고찬호 | M.S. 2021 | 42dot | Motion planning for collision avoidance and stabilization of autonomous vehicle based on model predictive control |
| 홍윤표 | Ph.D. 2021 | Samsung Electroncis | Bipedal robot with hybrid actuation using a novel pneumatic power pack |
| 한상훈 | Ph.D. 2021 | Samsung Electronics | Vision-based walking control of bipedal and quadrupedal transformable robot for nuclear power plant working |
| 이진우 | Ph.D. 2021 | Samsung Electronics. | Material parameter determination using terahertz time-domain spectroscopy in ambient air |
| 김병진 | Ph.D. 2021 | GIST Professor | Development of parallel type leg and walking control algorithm for nuclear power plant robot |

## 최근 논문 목록 (2021–2026)

랩 Papers 게시판의 2021년 이후 학술지·학회 논문이다.[^papers]

**2026**

- Choi, H., Kim, Y., Kim, K.S. "ANN-Model Based Adaptive Flux-Linkage Map". *IEEE Energy Conversion Congress & EXPO*.
- Lee, T., Baek, H, Jang, B., Choi, K.H., Kim, K.S. "Lightweight Neural Network-Based Cell Balancing Using Variable Effective Resistance". *IEEE Access, 14, 145548-145563*.
- Ham, B.I., Kim, H.B., Kang, J., Choi, K.H., Kim, K.S. "Dual-MPC Footstep Planning for Robust Quadruped Locomotion". *IEEE/ASME Transactions on Mechatronics*.
- Park, J.H., Lee, J., Lim, J.H., Choi, K.H., & Kim, K.S. "MSC: Multi-Stage Caster-aware Control Framework with Uncertainty-Aware NMPC and RL-based Execution Layer". *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems(IROS)*.
- Lee, B., Kang, J., Lee, S., Jeon, K.W., Kim, T.H., Chung, H.J., Hong, M.B., Park, J.S., & Kim, K.S. "Optimal Load Distribution Strategy via Knee-Hip Coordinated Control for Heavy Load Lifting Assistance in Wearable Robots". *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems(IROS)*.
- Lee, J., Park, J.H., Yang, S., Choi, K.H., & Kim, K.S. "Fully Distributed Real-Time MPC for Cooperative Mobile Manipulation Via Box-iLQR and ADMM with an Object-Centric Planar Projection". *2026 IEEE International Conference on Robotics & Automation(ICRA)*.
- Oh, S., Jeon, H.Y., Seo, J., Choi K.H., & Kim, K.S. "Field-Validated Navigation Framework for Orchard Weeding Robots Using Multimodal Sensor Fusion". *International Journal of Control, Automation, and Systems(IJCAS), 1-18*.
- Kim, H.B., & Kim, K.S. "A Compact PCB-Integrated Inductive Six-Axis Force/Torque Sensor". *IEEE Sensors Journal, 26*.
- Lee, K.S., Kim, K.S., & Kim, S. "Predicting Warhead Fragment Dispersion Using Stepwise Machine Learning Regression". *International Journal of Precision Engineering and Manufacturing, 27, 225-239*.
- Lee, S., & Kim, K. S. "Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation". *IEEE Robotics and Automation Letters(RA-L), 11(4), 4122 - 4129*.

**2025**

- Jeong, E., Seo, M., & Kim, K. S. "Broad-Spectrum Error Robust Wavelengths for fNIRS Systems". *International Journal of Precision Engineering and Manufacturing, 26, 3473–3484*.
- Kim, H. B., Ham, B. I., Choi, K. H., & Kim, K. S. "Compact and Optimized Optical Six-Axis Force/Torque Sensor for Legged Robots". *IEEE Transactions on Instrumentation and Measurement, 74*.
- Kim, H. B., Ham, B. I., & Kim, K. S. "A Miniature High-Resolution Tension Sensor Based on a Photo-Reflector for Robotic Hands and Grippers". *IEEE Sensors Journal, 25(10), 38916 - 38924*.
- Jeon, H. Y., Choi, M., Lee, Y., Oh, S., Yang, S., Choi, K. H., & Kim, K. S. "POW4R: POint-Wise full-velocity estimation using 4 d Radar-camera fusion beyond radial limitations". *IEEE Robotics and Automation Letters(RA-L), 10(10), 10934 - 10941*.
- Lee, M., Kim, M., Park, C., Cha, M., & Kim, K. S. "Vehicle Speed Estimation Using Modulated Motion Blur in Diverse Environments". *IEEE Access, 13, 159667 - 159684*.
- Kim, H. B., Lee, S., Ham, B. I., Choi, K. H., & Kim, K. S. "Temperature Compensation Method for a Six-Axis Force/Torque Sensor Using a Gated Recurrent Unit". *IEEE Sensors, 25, 26581 - 26590*.
- Ham, B. I., Kim, H. B., & Kim, K. S. "Ground-Aware Octree-A\* Hybrid Path Planning for Memory-Efficient 3D Navigation of Ground Vehicles". *2025 25th International Conference on Control, Automation and Systems (ICCAS), 768 - 773*.
- Park, J., Lee, J., Yang, S., Kim, K. S., & Choi, K. "Robust and Precise Autonomous Mobile Robot System for Misplaced Rack Center Navigation in Small to Medium-Sized Warehouses". *2025 22nd International Conference on Ubiquitous Robots (UR), 253-259*.
- Cho, Y., Hwang, J. S., Kim, K. S., & Gong, H. S. "Biomechanical modeling of finger flexion based on imaging data: Implications on trigger finger surgery". *Journal of Plastic, Reconstructive & Aesthetic Surgery, 104, 153-161*.
- Lee, S., Kim, H. B., & Kim, K. S. "Legged Robot State Estimation Using Invariant Neural-Augmented Kalman Filter with a Neural Compensator". *2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 15445-15452*.
- Kang, J., Ham, B. I., Han, S., Kim, H., & Kim, K. S. "Adaptive Gait Pattern Switching under External Disturbances Using Multi-Modal MPC". *2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), 134-140*.
- Kim, H. B., Kim, C., Ham, B. I., Kang, J., Choi, M., Choi, K. H., & Kim, K. S. "Development of Remote Piping Inspection System with Dual-Mode Locomotion Quadruped Robot". *International Conference on Robot Intelligence Technology and Applications (RiTA2024), 307-319*.

**2024**

- Han, S., Choi, M., Jang, B., Choi, K. H., & Kim, K. S. "Adaptive ROI for Collision Warning Mitigation Based on Road Geometry and Kinematics". *IEEE Sensors Journal, 25(3), 5499 - 5509*.
- Lee, B., Kim, K. S., & Cho, Y. "Real-time adaptive cancellation of TENS feedback artifact on sEMG for prosthesis closed-loop control". *Frontiers in Bioengineering and Biotechnology, 12*.
- Lee, H., Oh, S., Kim, K. S., Kim, Y., & Kim, S. K. "Model-Free Filter-Based Trajectory Tracking Controller for Two-Wheeled Vehicles Through Pole-Zero Cancellation Technique". *Vehicles, 6(4), 1902-1921*.
- Kang, J., Kim, H. B., Ham, B. I., & Kim, K. S. "External force adaptive control in legged robots through footstep optimization and disturbance feedback". *IEEE Access, 12, 157531 - 157539*.
- Lee, Y., Choi, K. H., & Kim, K. S. "Gpu-enabled parallel trajectory optimization framework for safe motion planning of autonomous vehicles". *IEEE Robotics and Automation Letters(RA-L), 9(11), 10407 - 10414*.
- Jeong, E., Seo, M., & Kim, K. S. "Design of an fNIRS–EEG hybrid terminal for wearable BCI systems". *Review of Scientific Instruments, 95(8)*.
- Kim, H. B., Choi, K. H., & Kim, K. S. "A compact six-axis force/torque sensor using photocouplers for impact robustness". *Review of Scientific Instruments, 95(4)*.
- Han, S\*., Kwon, J\*., & Kim, K. S. "Position uncertainty-integrated potential function for collision avoidance systems based on model predictive control". *IEEE Transactions on Intelligent Vehicles., 9(11), 7045 - 7058*.
- Han, S., Choi, K. H., & Kim, K. S. "Adaptive safety distance for collision avoidance based on a full braking activation parameter". *IEEE Transactions on Intelligent Transportation Systems, 25(9), 12657-12668*.
- Jang, B., Choi, K. H., Choi, H., Jung, Y., Choi, W., & Kim, K. S. "Prediction of Driving Range per Charge for e-Mobility using a Vehicle Dynamics Model". *IECON 2024-50th Annual Conference of the IEEE Industrial Electronics Society, 1-6*.

**2023**

- Yang, S., Choi, M., Han, S., Choi, K. H., & Kim, K. S. "4D radar-camera sensor fusion for robust vehicle pose estimation in foggy environments". *IEEE Access, 12, 16178-16188*.
- Seo, M., Jeong, E., & Kim, K. S. "Multi-class fnirs classification using an ensemble of gnn-based models". *IEEE Access, 11, 137606-137620*.
- Jang, B., Choi, H., Kim, W., & Kim, K. S. "Connection Loss Detection Algorithm of Parallel-connected Cells Based on Change of Battery SOC". *International Journal of Control, Automation and Systems, 21(11), 3551-3562*.
- Kang, J., Kim, H., & Kim, K. S. "View: Visual-inertial external wrench estimator for legged robot". *IEEE Robotics and Automation Letters(RA-L), 8, 8366 - 8373*.
- Han, S., Choi, M., Cho, M., Park, J. I., & Kim, K. S. "Dynamic control and simulation of leader-follower vehicle formation considering vehicle stability". *International Journal of Control, Automation and Systems, 21(9), 2995-3005*.
- Han, S., Yang, S., Lee, Y., Lee, M., Park, J. I., & Kim, K. S. "The leader-follower formation control of nonholonomic vehicle with follower-stabilizing strategy". *IEEE Robotics and Automation Letters, 9(1), 707-714*.
- Choi, M., Yang, S., Han, S., Lee, Y., Lee, M., Choi, K. H., & Kim, K. S. "Msc-rad4r: Ros-based automotive dataset with 4d radar". *IEEE Robotics and Automation Letters, 8(11), 7194-7201*.
- Choi, M., Choi, K., Cho, M., Lee, M., & Kim, K. S. "Chattering reduction of sliding mode control via nonlinear disturbance observer for anti-lock braking system and verification with carsim simulation". *International Journal of Automotive Technology, 24(4), 1141-1149*.
- Jeon, Y., Seol, W., Kim, S., & Kim, K. S. "Robust near-infrared-based plastic classification with relative spectral similarity pattern". *Waste Management, 166, 315-324*.
- Cho, Y., Lee, B., Lee, Y., & Kim, K. S. "Simultaneous sensory feedback strategy for force and position of gripper based on tens". *IEEE Robotics and Automation Letters, 8(9), 5291-5298*.
- Kang, J., Kim, D., Chung, H. J., Jeon, K. W., & Kim, K. S. "Whole-body control based lifting assistance simulation for exoskeletons". *International Journal of Control, Automation and Systems, 21(6), 1950-1958*.
- Um, S., Kim, K. S., & Kim, S. "Fast suction-grasp-difficulty estimation for high throughput plastic-waste sorting". *Journal of Mechanical Science and Technology, 37(2), 955-964*.
- Cho, M., Lee, Y., & Kim, K. S. "Model predictive control of autonomous vehicles with integrated barriers using occupancy grid maps". *IEEE Robotics and Automation Letters, 8(4), 2006-2013*.
- Kang, J., Kim, H. B., Choi, K. H., & Kim, K. S. "External force estimation of legged robots via a factor graph framework with a disturbance observer". *2023 IEEE International Conference on Robotics and Automation (ICRA), 12120-12126*.

**2022**

- Seo, H. T., Hong, Y. P., Park, J., & Kim, K. S. "Improving the response of an electrohydrostatic actuation (EHA) system using a high-pressure accumulator". *IEEE Access, 10, 93353-93361*.
- Jo, S., Kim, W., Kim, J., & Kim, K. S. "Study on actual Ah‐throughput‐based health indicator of battery module consisting of inconsistent cells for its second life". *Electronics Letters, 58(15), 588-590*.
- Jang, B., Lee, D., Kim, K., & Kim, K. S. "Road torque modeling for electric power steering systems". *International Journal of Automotive Technology, 23(3), 765-773*.
- Cho, M., Cho, Y., & Kim, K. S. "Training strategy and sEMG sensor positioning for finger force estimation at various elbow angles". *International Journal of Control, Automation and Systems, 20(5), 1621-1631*.
- Cho, Y., Lee, Y., Kim, P., Jeong, S., & Kim, K. S. "The MSC prosthetic hand: Rapid, powerful, and intuitive". *IEEE Robotics and Automation Letters(RA-L), 7(2), 3170-3177*.
- Jang, Y., Seol, W., Lee, K., Kim, K. S., & Kim, S. "Development of quadruped robot for inspection of underground pipelines in nuclear power plants". *Electronics Letters, 58(6), 234-236*.
- Kang, D., Sarkar, S., Kim, K. S., & Kim, S. "Highly damage-resistant thin film saturable absorber based on mechanically functionalized SWCNTs". *Nanoscale Research Letters, 17(1)*.
- Cho, M., Lee, Y., & Kim, K. S. "Iterative lqr with discrete barrier states for efficient collision avoidance of autonomous vehicle". *2022 22nd International Conference on Control, Automation and Systems (ICCAS), 1636-1641*.
- Jeong, E., Seo, M., & Kim, K. S. "Guide for wavelength selection of LEDs for fNIRS systems". *2022 22nd International Conference on Control, Automation and Systems (ICCAS), 1819-1822*.
- Seo, M., Jeong, E., & Kim, K. S. "Extracting spatial features of fNIRS signal using a graph representation". *2022 22nd International Conference on Control, Automation and Systems (ICCAS), 6-9*.
- Shyam, P., Yoon, K. J., & Kim, K. S. "Multi-source domain alignment for domain invariant segmentation in unknown targets". *2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 309-316*.
- Lee, Y., Cho, M., & Kim, K. S. "Gpu-parallelized iterative lqr with input constraints for fast collision avoidance of autonomous vehicles". *2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 4797-4804*.
- Park, J. I., Choi, M., Han, S., Lee, Y., Cho, J., Choi, H., Cho, M., Lee, M., & Kim, K. S. "Development of ROS-based small unmanned platform for acquiring autonomous driving dataset in various places and weather conditions". *2022 IEEE 46th Annual Computers, Software, and Applications Conference (COMPSAC), 24-31*.
- Shyam, P., Kim, K. S., & Yoon, K. J. "Giqe: Generic image quality enhancement via nth order iterative degradation". *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2077-2087*.
- Bangunharcana, A., Kim, S., & Kim, K. S. "Revisiting the receptive field of conv-gru in droid-slam". *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 1906-1916*.
- Shyam, P., Mishra, S., Yoon, K. J., & Kim, K. S. "Infra Sim-to-Real: An efficient baseline and dataset for infrastructure based online object detection and tracking using domain adaptation". *2022 IEEE Intelligent Vehicles Symposium (IV), 1393-1399*.
- Jang, B., Han, S., Kim, Y., & Kim, K. S. "Disturbance observer-based robust speed control of autonomous in-wheel driven electric vehicle". *2022 13th Asian Control Conference (ASCC), 744-749*.

**2021**

- Kim, D., Hong, Y. P., & Kim, K. S. "Bipedal walking and impact reduction algorithm for a robot with pneumatically driven knees". *International Journal of Control, Automation and Systems, 19(12), 3937-3946*.
- Choi, K., Kim, Y., Kim, S. K., & Kim, K. S. "Computationally efficient model predictive torque control of permanent magnet synchronous machines using numerical techniques". *IEEE Transactions on Control Systems Technology, 30(4), 1774-1781*.
- Lee, M., Cho, J. S., Kim, K. S., & Kim, S. "Modulated motion blur-based vehicle body velocity and pose estimation using an optical image modulator". *IEEE Transactions on Vehicular Technology, 70(9), 8744-8754*.
- Lee, H. J., Kim, K. S., & Kim, S. "Generalized control framework for exoskeleton robots by interaction force feedback control". *International Journal of Control, Automation and Systems, 19(10), 3419-3427*.
- Park, J. I., Lee, Y., Suh, E., Jeon, H., Yoon, K. J., & Kim, K. S. "Improvement of optical flow estimation by using the hampel filter for low-end embedded systems". *IEEE Robotics and Automation Letters, 6(4), 7233-7239*.
- Kim, W., Lee, P. Y., Kim, J., & Kim, K. S. "A robust state of charge estimation approach based on nonlinear battery cell model for lithium-ion batteries in electric vehicles". *IEEE Transactions on Vehicular Technology, 70(6), 5638-5647*.
- Lee, D., Jang, B., Han, M., & Kim, K. S. "A new controller design method for an electric power steering system based on a target steering torque feedback controller". *Control Engineering Practice, 106*.
- Shyam, P., Yoon, K. J., & Kim, K. S. "Weakly supervised approach for joint object and lane marking detection". *Proceedings of the IEEE/CVF international conference on computer vision, 2885-2895*.
- Cho, Y., Kim, P., & Kim, K. S. "Simultaneous and Proportional Wrist Force Intent Estimation Method using Constrained Autoencoder". *2021 21st International Conference on Control, Automation and Systems (ICCAS), 1917-1921*.
- Bangunharcana, A., Cho, J. W., Lee, S., Kweon, I. S., Kim, K. S., & Kim, S. "Correlate-and-excite: Real-time stereo matching via guided cost volume excitation". *2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 3542-3548*.
- Um, S., Kim, K. S., & Kim, S. "Suction point selection algorithm based on point cloud for plastic waste sorting". *IEEE 17th International Conference on Automation Science and Engineering (CASE), 60-65*.
- Jeong, S., Lee, Y., & Kim, K. S. "Applications: Twisted string actuation-based compact automatic transmission". *2021 IEEE International Conference on Robotics and Automation (ICRA), 10870-10876*.
- Shyam, P., Yoon, K. J., & Kim, K. S. "Adversarially-trained hierarchical feature extractor for vehicle re-identification". *2021 IEEE International Conference on Robotics and Automation (ICRA), 13400-13407*.
- Shyam, P., Yoon, K. J., & Kim, K. S. "Towards domain invariant single image dehazing". *Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 35, No. 11, 9657-9665*.

## 특허

랩 Patents 게시판의 2021년 이후 특허와 국가, 번호, 등록·출원 상태다.[^patents]

- 2025 · 6-AXIS FORCE TORQUE SENSOR BASED ON PHOTOCOUPLER AND METHOD OF SENSING 6-AXIS FORCE TORQUE BASED ON PHOTOCOUPLER MEASUREMENT (발명자 Kim, Kyung-Soo, Kim, Hyun-Bin, Choi, Keun Ha; 국가 United States; 번호 19/414543; 상태 출원)
- 2025 · 복합 신호에 대한 단일 측정 단자 모듈 (발명자 정유진, 서민석, 김경수, 조민수; 국가 대한민국; 번호 10-2890966-0000; 상태 등록)
- 2025 · METHOD AND APPARATUS FOR REMOVING LIDAR POINT CLOUD NOISE (발명자 Kim, Kyung-Soo, Park, Ji il, Choi, Min Seong, Jeon, Hyun Yong, Park, Jihyuk; 국가 United States; 번호 12/416709; 상태 등록)
- 2025 · 6-Axis force torque sensor based on inductance measurement and method of sensing 6-axis force torque based on inductance measurement (발명자 Kim, Kyung-Soo, Kim, Hyun-Bin; 국가 International; 번호 PCT/KR2025/008853; 상태 출원)
- 2025 · 최적 안전거리 제공을 위한 비상자동제동 방법 및 비상자동제동 시스템 (발명자 김경수, 한승호, 최근하; 국가 대한민국; 번호 10-2025-0042188; 상태 출원)
- 2025 · 전기 모빌리티의 주행 가능거리 예측 방법 (발명자 김경수, 장병관, 최근하, 최효서; 국가 대한민국; 번호 10-2025-0022826; 상태 출원)
- 2025 · 포토 커플러 기반의 6축 힘 토크 감지 장치 및 6축 힘 토크 감지 방법 (발명자 김경수, 김현빈, 최근하; 국가 대한민국; 번호 10-2025-0000095; 상태 출원)
- 2024 · 인덕턴스를 이용한 장력 센서를 구비한 의수의 로봇 핑거 (발명자 김경수, 김현빈; 국가 대한민국; 번호 10-2024-0141334; 상태 출원)
- 2024 · Method and apparatus for controlling power of hybrid vehicle considering driving environment (발명자 Kim, Kyung-Soo, Choi, Kyunghwan, Jang, In Gwun; 국가 United States; 번호 12/097840; 상태 등록)
- 2024 · 하이브리드 차량의 과도특성을 고려한 동력제어 방법 및 장치 (발명자 김경수, 최경환, 장인권; 국가 대한민국; 번호 10-2701529-0000; 상태 등록)
- 2024 · 인덕턴스 측정 기반의 6축 힘 토크 감지 장치 및 6축 힘 토크 감지 방법 (발명자 김경수, 김현빈; 국가 대한민국; 번호 10-2024-0101868; 상태 출원)
- 2024 · 이동 로봇 (발명자 김경수, 김현빈, 함병일, 최근하, 김찬석, 장유현, 송은혜, 설우진, 김현기; 국가 대한민국; 번호 10-2024-0095219; 상태 출원)
- 2024 · 6축 힘 토크 센서 (발명자 김경수, 김현빈; 국가 대한민국; 번호 10-2675600-0000; 상태 등록)
- 2024 · Method and device for controlling power through consideration of transient characteristics of hybrid vehicle (발명자 Kim, Kyung-Soo, Choi, Kyunghwan, Jang, In Gwun; 국가 Europe; 번호 22887650.4; 상태 출원)
- 2024 · Method and apparatus for controlling power of hybrid vehicle considering transient characteristics (발명자 Kim, Kyung-Soo, Choi, Kyunghwan, Jang, In Gwun; 국가 United States; 번호 18/648697; 상태 출원)
- 2024 · 배관 내부 점검을 위한 카메라 탐사장치 (발명자 김경수, 김현빈, 김건무, 최근하, 김찬석; 국가 대한민국; 번호 10-2024-0032731; 상태 출원)
- 2024 · 광학식 비접촉 토크 센서 (발명자 김경수, 김현빈; 국가 대한민국; 번호 10-2024-0021550; 상태 출원)
- 2023 · Method and apparatus for real-time estimation of full parameters of permanent magnet synchronous motor (발명자 Kim, Kyung-Soo, Choi, Kyunghwan, Kim, Seok Kyoon; 국가 United States; 번호 11/614488; 상태 등록)
- 2023 · Apparatus and method for operating accessories of vehicle during engine stop using one-way clutch pulley (발명자 Jang, In Gwun, Kum, Dongsuk, Kim, Kyung-Soo, Jang, Kitae, Lee, Changwoo, Kim, Jong Ho, Choi, Kyunghwan, Kim, Mingi; 국가 United States; 번호 11/607944; 상태 등록)
- 2023 · 하이브리드 차량의 주행환경을 고려한 동력제어 방법 및 장치 (발명자 김경수, 최경환, 장인권; 국가 대한민국; 번호 10-2508409-0000; 상태 등록)
- 2022 · 라이다 포인트 클라우드 노이즈 제거 방법 및 장치 (발명자 김경수, 박지일, 최민성, 전현용, 박지혁; 국가 대한민국; 번호 10-2482358-0000; 상태 등록)
- 2022 · 토크 제한 자기강화 클러치 및 이를 이용하는 하이브리드 자동차 (발명자 김경수, 윤용산, 장인권, 최민성, 고찬호; 국가 대한민국; 번호 10-2470215-0000; 상태 등록)
- 2022 · Method and apparatus for controlling power of hybrid vehicle considering transient characteristics (발명자 Kim, Kyung-Soo, Choi, Kyunghwan, Jang, In Gwun; 국가 International; 번호 PCT/KR2022/016588; 상태 출원)
- 2022 · 영구자석동기모터 전체 파라미터의 실시간 추정 방법 및 장치 (발명자 김경수, 최경환, 김석균; 국가 대한민국; 번호 10-2437244-0000; 상태 등록)
- 2022 · 조향 장치 및 그를 가지는 차량 (발명자 김경수, 이동욱; 국가 대한민국; 번호 10-2383533-0000; 상태 등록)
- 2022 · 뇌파 기반의 생체 통신이 가능한 방탄모 및 생체 통신 방법 (발명자 김경수, 강정욱, 정유진, 김광태; 국가 대한민국; 번호 10-2359390-0000; 상태 등록)
- 2021 · 하이브리드 차량의 과도특성을 고려한 동력제어 방법 및 장치 (발명자 김경수, 최경환, 장인권; 국가 대한민국; 번호 10-2021-0144773; 상태 출원)
- 2021 · 테라헤르츠 신호를 이용한 샘플의 두께 측정 방법 (발명자 김수현, 김경수, 이진우, 서민석, 전영민, 부준호, 정유진; 국가 대한민국; 번호 10-2314842-0000; 상태 등록)
- 2021 · 격발 보조 장치 및 격발 보조 장치의 제어 방법 (발명자 김경수, 차재준, 김수현, 정재원, 정유진, 서민석, 조영걸; 국가 대한민국; 번호 10-2299410-0000; 상태 등록)
- 2021 · Motor control system and method for compensating disturbance (발명자 김경수, 김용훈; 국가 China; 번호 106849770; 상태 등록)
- 2021 · 수동 변속기의 변속 레버 위치 검출 장치 및 운전자 변속의도 검출을 통한 실시간 변속 레버 위치 검출 방법 및 장치 (발명자 김경수, 김우용, 김용훈; 국가 대한민국; 번호 10-2292179-0000; 상태 등록)
- 2021 · System for compensating for disturbance of motor for motor driven power steering (발명자 김경수, 김용훈, 한민우, 성우제, 이종호, 김성준; 국가 China; 번호 106936345; 상태 등록)
- 2021 · 자동 용접 로봇 장치 (발명자 김수현, 김경수, 엄상우, 김찬석, 박찬배; 국가 대한민국; 번호 10-2021-0072952; 상태 출원)
- 2021 · Dual-mode transmission based on twisted string actuation (발명자 Kim, Kyung-Soo, Jeong, Seok Hwan, Lim, Jung Min, Kim, Soohyun; 국가 Europe; 번호 3376068; 상태 등록)
- 2021 · Dual-mode transmission based on twisted string actuation (발명자 Kim, Kyung-Soo, Jeong, Seok Hwan, Lim, Jung Min, Kim, Soohyun; 국가 Germany; 번호 602017038758.4; 상태 등록)
- 2021 · 교통 정체 상황을 고려한 지능형 ISG 제어를 위한 전자 장치 및 그의 동작 방법 (발명자 금동석, 김경수, 장기태, 장인권, 김경근; 국가 대한민국; 번호 10-2225748-0000; 상태 등록)
- 2021 · 자율주행을 위한 라이다 포인트 클라우드 노이즈 제거 방법 및 장치 (발명자 김경수, 박지일, 최민성, 전현용, 박지혁; 국가 대한민국; 번호 10-2021-0001372; 상태 출원)

## 연구 과제

랩 첫 화면의 진행 중 과제와 발주 기관, 기간이다.[^home]

- Arc Fault Detection Device Research (지원 LS Electric; 기간 Sep.2026-Dec.2026)
- Development of the ESV Vehicle at the KAIST Mobility Research Center (지원 KAIST Mobility Research Center; 기간 Jul.2026-)
- AI-Integrated High-Safety Battery Pack Development for Electric Buses Featuring Advanced Prognostics and Health Management (지원 Ministry of Trade, Industry and Energy (MOTIE, 산업통상부); 기간 Apr.2026–Dec.2030)
- Research on Humanoid Autonomous Walking and Loco-Manipulation Using a Vision-Based Integrated Learning Framework (지원 KIMM(한국기계연구원); 기간 Jan. 2026 - Dec.2030)
- Research on Controlling Multi-agent Indoor·Outdoor Ultra-compact Autonomous Mobility (지원 National Research Foundation of Korea (NRF, 한국연구재단); 기간 Mar. 01, 2025 - Feb. 28, 2029)
- Development of an AI-Based Training Simulation Environment to Enhance Tactical Performance of Small Units in Manned–Unmanned Teaming Systems (지원 MORAI Inc., Korea National Defense University(KNDU, 국방대학교); 기간 Dec. 01, 2025 - Nov. 30, 2028)
- DRB-KAIST SketchTheFuture Research Center (지원 DRB, KAIST SketchLab; 기간 Feb., 2024 -)
- Robotic Immersive Interaction Platform for Future Mobility Space Design (지원 DRB, KAIST SketchLab; 기간 July, 2025 -)
- Fully Distributed Real-Time MPC for Cooperative Mobile Manipulation via Box-iLQR and ADMM with an Object-Centric Planar Projection (기간 June 01, 2025 - Dec. 31, 2026)
- Development of the hydrogen fuel-cell tractor’s drive and PTO the motor drive units and motor control algorithms up to 110 kW (지원 Rural Development Administration(RDA, 농촌진흥청); 기간 Jan. 01, 2022 - Dec. 31, 2026)
- Development of Integrated Core Technology for Solar Battery in Low Earth Orbit Satellites for Ultra-Broadband Communication Network Establishment (지원 National Research Foundation of Korea (NRF, 한국연구재단); 기간 Sep. 01, 2023 - Dec. 31, 2027)

## 수상

교수 페이지 Awards 항목이다. 인명록(Who's Who) 등재도 랩이 이 항목에 함께 적었다.[^prof]

- 2025.12 · National Assembly Education Committee Chairman's Award (대한민국 국회공로장 교육위원장상)
- 2016.7 · Best Student Paper Award, International Conference on Advanced Intelligent Mechatronics
- 2010.2 · Excellence in Teaching Award (Founding Anniversary), KAIST
- 2009.12 · Best Paper Award, Institute of Control, Robotics and Systems
- 2009.7 · Best Student Paper Award, International Conference on Advanced Intelligent Mechatronics
- 2008.12 · Best Paper Award, Institute of Control, Robotics and Systems
- 2007.1 · Listed in Who’s Who in Science & Engineering
- 2006.1 · Listed in Who’s Who in Science & Engineering – Emerging Leaders in Asia
- 2005.1 · Listed in Who’s Who in the World
- 2003.1 · Best Paper Award, Digital Media Research Lab., LG Electronics

## 연락과 위치

- 연구실: KAIST 본원 N25(산업디자인학과/기계공학과 나래 실습동) 4층 3439–3445호, 문지캠퍼스 연구동 2층(KAIST 모빌리티센터)·3층 306–309호[^home]
- 교수실: KAIST N7 7112호[^prof]

[^home]: MSC Lab 누리집 첫 화면 <https://msc.kaist.ac.kr/> (2026-10-20 열람)
[^research]: MSC Lab Research Topics(Electric Powertrain Control, Perception and Control) 페이지 <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub2_1_a>, bo_table=sub2_2_a (2026-10-20 열람)
[^prof]: MSC Lab 김경수 교수 페이지 <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub1_1_a&wr_id=16> (2026-10-20 열람)
[^members]: MSC Lab Members 게시판(Post Doctoral Researchers, Graduate Students, Interns) <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub1_2_a>, bo_table=sub1_2_b, bo_table=sub1_2_c (2026-10-20 열람)
[^alumni]: MSC Lab Alumni 게시판 1–7쪽 <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub1_3> (2026-10-20 열람)
[^papers]: MSC Lab Papers 게시판 1–8쪽 <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub5_1> (2026-10-20 열람)
[^patents]: MSC Lab Patents 게시판 1–3쪽 <https://msc.kaist.ac.kr/bbs/board.php?bo_table=sub5_2> (2026-10-20 열람)
[^p1]: K. Choi, Y. Kim, S.-K. Kim, K.-S. Kim, IEEE Transactions on Control Systems Technology 30, 1774-1781 (2022). <https://doi.org/10.1109/tcst.2021.3113045> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: W. Kim, P.-Y. Lee, J. Kim, K.-S. Kim, IEEE Transactions on Vehicular Technology 70, 5638-5647 (2021). <https://doi.org/10.1109/tvt.2021.3079934> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: T. Lee 외, K.-S. Kim, IEEE Access 14, 145548-145563 (2026). <https://doi.org/10.1109/access.2026.3735378> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Lee, K. H. Choi, K.-S. Kim, IEEE Robotics and Automation Letters 9, 10407-10414 (2024). <https://doi.org/10.1109/lra.2024.3471452> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H.-Y. Jeon 외, K.-S. Kim, IEEE Robotics and Automation Letters 10, 10934-10941 (2025). <https://doi.org/10.1109/lra.2025.3606356> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: S. Lee, K.-S. Kim, IEEE Robotics and Automation Letters 11, 4122-4129 (2026). <https://doi.org/10.1109/lra.2026.3664311> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H.-B. Kim, B.-I. Ham, K. H. Choi, K.-S. Kim, IEEE Transactions on Instrumentation and Measurement 74, 1-12 (2025). <https://doi.org/10.1109/tim.2025.3618428> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: Y. Cho 외, K.-S. Kim, IEEE Robotics and Automation Letters 7, 3170-3177 (2022). <https://doi.org/10.1109/lra.2022.3140444> 초록 기준(Semantic Scholar 등록 초록).

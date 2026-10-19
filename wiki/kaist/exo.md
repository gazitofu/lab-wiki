# EXO 연구실 (Exoskeleton Laboratory, EXO-Lab)

**KAIST 기계공학과 · 공경철 교수**

- 분야: 착용형 로봇(외골격), 하지마비 장애인 보행 보조, 재활 로봇, 직렬 탄성 구동기, 보행 인식과 제어, 피지컬 AI
- 홈페이지: <https://robotics.kaist.ac.kr/>
- 근거와 출처: [EXO 연구실 근거 페이지](exo-sources.md)

> 사람이 입는 로봇(착용형 로봇)을 만드는 연구실이다. 다리를 전혀 움직이지 못하는 하지 완전마비 장애인이 걷도록 돕는 외골격 로봇 "워크온슈트(WalkON Suit)"로 국제 대회 사이배슬론에서 2020년과 2024년 금메달을 땄고, 교수는 착용형 로봇 기업 엔젤로보틱스를 공동 창업했다.[^background][^prof]

## 무엇을 연구하나

연구실은 사람의 삶을 낫게 하는 피지컬 AI(로봇 몸을 통해 현실 세계와 직접 힘을 주고받는 인공지능)와 메카트로닉스(기계·전자·제어를 합친 기술)·로봇 시스템 개발을 목표로 내건다. 제어, 동역학, 인공지능을 바탕으로 사람의 이동을 돕는 다리형 로봇을 설계하고 제어한다.[^home] 착용형 로봇은 사람형 로봇과 닮았지만 입은 사람의 의도와 정확히 맞물려 움직여야 하고, 기능과 무게 사이에서 균형을 잡아야 한다고 랩은 설명한다.[^background] 센서와 구동기 같은 부품부터 로봇 전체까지 직접 만든다.[^background]

첫 번째 갈래는 **하지 완전마비 장애인용 외골격 로봇**이다. 완전마비 환자는 다리 근육을 전혀 쓰지 못하므로 로봇의 제어 시스템이 걸음을 이끈다.[^background] 최신 모델 워크온슈트 F1은 구동 관절 12개를 가졌고, 휠체어에 앉은 사용자에게 스스로 걸어와 앞쪽에서 입을 수 있다.[^api] 미리 정한 보행 궤적이 사람마다 맞지 않는 문제를 풀기 위해, 발이 땅에 닿는 시점을 보고 보행 패턴을 사용자에게 맞게 반복 조정하는 방법을 내놓았고,[^p1] 보행 단계마다 달라지는 조건에서도 로봇이 정밀하게 움직이도록 제어기를 개선했다.[^p2] 지금은 대규모 시뮬레이션 속 강화학습(시행착오로 배우는 인공지능)으로 보행 제어를 다시 만들고 있다.[^api]

두 번째 갈래는 **재활과 일상을 돕는 부드러운 착용형 로봇**이다. 케이블로 엉덩이 관절을 돕는 부드러운 로봇을 만성 뇌졸중 환자 19명에게 시험해 걷는 데 드는 산소 소비를 14.9% 줄였다.[^p3] 걷는 속도가 바뀌어도 보행 단계를 추정하는 모듈,[^p5] 발목 근육의 힘을 피부 위에서 재는 공기압 센서도 만들었다.[^p6] 무거운 일을 하는 군인과 근로자의 근력을 보조하는 로봇도 주요 응용이다.[^background]

세 번째 갈래는 **로봇을 움직이는 구동기와 모델링**이다. 무거운 모터를 몸 가까이 두고 휘는 축으로 발목에 힘을 전달하는 직렬 탄성 구동기(모터와 관절 사이에 스프링을 넣어 힘을 부드럽고 정확하게 조절하는 장치, Flexi-SEA),[^p4] 온도가 변해도 모터가 같은 힘을 내도록 보정하는 기법,[^p7] 베어링까지 부품 단위로 모델링해 시뮬레이션 정확도를 높이는 방법을 연구한다.[^p8]

최근에는 사람을 이해하는 쪽으로 연구를 넓혔다. 사람과 로봇을 하나의 물리 시스템으로 보고 시뮬레이션하는 연구(Human–Robot Integrated Simulation), 몸에 단 몇 개의 센서만으로 온몸의 움직임과 몸이 받는 힘을 추정하는 "사람 동작 기반 모델(Human Motion Foundation Model)", 그리고 사람의 운동 제어 체계에서 착안한 피지컬 AI를 연구 목표로 든다.[^research][^hmfm][^hris]

## 주요 연구 주제

### 1. 완전마비 장애인용 외골격 로봇(WalkON Suit)

사용자 맞춤 보행 패턴, 정밀 동작 제어, 강화학습 기반 보행.[^p1][^p2][^api] 2024년 사이배슬론에서는 크게 개선한 워크온슈트로 목발 없이 균형을 잡고 걷는 과제까지 해내며 다른 팀보다 세 배 많은 과제를 마쳐 1위를 했다.[^background] 대표 논문 1, 2.

### 2. 재활·보조용 부드러운 착용형 로봇

뇌졸중 환자 보행 보조 임상 시험, 보행 단계 추정, 근력 측정 센서.[^p3][^p5][^p6] 대표 논문 3, 5, 6.

### 3. 구동기 설계와 로봇 모델링

직렬 탄성 구동기, 구동기 온도 보정, 베어링 모델링.[^p4][^p7][^p8] 대표 논문 4, 7, 8.

### 4. 사람 모델과 피지컬 AI

신경·근골격 시뮬레이션으로 파킨슨병의 보행 동결이나 뇌졸중 편마비 같은 걸음의 원인을 모델링하고, 로봇 보조에 사람이 어떻게 반응하는지 시뮬레이션한다.[^hris] 착용 센서와 실험실 측정 자료를 짝지어 학습한다.[^hmfm]

## 대표 논문

랩 논문 목록의 2021–2026년 논문 중 교수가 마지막 저자(연구 책임)인 것을 중심으로 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2022 | [Iterative Learning of Human Behavior for Adaptive Gait Pattern Adjustment of a Powered Exoskeleton](https://doi.org/10.1109/tro.2022.3144955) · IEEE Transactions on Robotics | 완전마비 장애인용 외골격 로봇의 정해진 보행 패턴이 사람마다 맞지 않는 문제를 풀었다. 발이 땅에 닿는 시점을 보고 상체 기울기 각도를 반복 계산해 보행 궤적을 맞춘다. 완전마비 사용자 2명에게 적용했고, 사이배슬론 2020 금·동메달로도 검증했다.[^p1] | 1저자 Kyeong-Won Park, 마지막 저자 공경철 |
| 2 | 2023 | [Hybrid Filtered Disturbance Observer for Precise Motion Generation of a Powered Exoskeleton](https://doi.org/10.1109/tie.2022.3152016) · IEEE Transactions on Industrial Electronics | 보행 단계마다 달라지는 조건과 사람·환경의 영향 속에서도 외골격 로봇이 정밀하게 움직이도록, 보행 단계에 맞춰 시스템 모델과 제어기를 바꿔 가며 외란(예상 밖의 힘)을 보상하는 방법이다. 완전마비 사용자 1명이 실험에 참여했다.[^p2] | 1저자 Kyeong-Won Park, 마지막 저자 공경철 |
| 3 | 2025 | [Efficacy of a Soft Wearable Robot for Hip Assistance in Chronic Stroke Patients: A Randomized Crossover Trial](https://doi.org/10.1109/tnsre.2025.3577600) · IEEE TNSRE | 케이블로 엉덩이 관절을 돕는 부드러운 착용형 로봇을 만성 뇌졸중 환자 19명에게 무작위 교차 시험했다. 걷는 데 드는 산소 소비가 14.9% 줄고, 보행 속도가 0.11 m/s, 6분 보행 거리가 20.7 m 늘었다.[^p3] | 1저자 Seung-Hyeon Han, 공경철은 다섯째 저자, 마지막 저자 Deog Young Kim |
| 4 | 2025 | [Flexi-SEA: Flexible-Shaft-Driven Series Elastic Actuator for Wearable Robots](https://doi.org/10.1109/tmech.2025.3537113) · IEEE/ASME Transactions on Mechatronics | 무거운 모터를 몸 가까이 두고 휘는 축으로 발목 쪽 스프링 장치에 힘을 전달해, 케이블 방식의 불편함 없이 발목 부분을 가볍게 만든 구동기. 휘는 축의 불규칙한 비틀림은 제어로 보정했다.[^p4] | 1저자 Sanguk Choi, 마지막 저자 공경철 |
| 5 | 2023 | [Walking-Speed-Adaptive Gait Phase Estimation for Wearable Robots](https://doi.org/10.3390/s23198276) · Sensors | 걷는 속도가 일정할 때도, 빨라지거나 느려질 때도 보행 단계를 매끄럽게 추정하는 모듈과 알고리즘. 기존 두 방법보다 보행 단계 편차를 약 48% 줄였다.[^p5] | 1저자 Sanguk Choi, 마지막 저자 공경철 |
| 6 | 2024 | [Plantar Flexion Muscle Force Estimation With a Soft Wearable Pneumatic Sensor System](https://doi.org/10.1109/tmech.2024.3398224) · IEEE/ASME Transactions on Mechatronics | 근육이 당겨질수록 옆으로 단단해지는 성질을 이용해, 종아리에 댄 공기주머니 센서의 압력으로 발목 근육의 힘을 몸에 상처 내지 않고 추정한다.[^p6] | 1저자 Taeyeon Kim, 마지막 저자 공경철 |
| 7 | 2024 | [Thermal Characteristic Modeling and Compensation for the Improvement of Actuator Homeostasis](https://doi.org/10.1109/tmech.2024.3400214) · IEEE/ASME Transactions on Mechatronics | 온도가 바뀌면 모터의 힘이 달라지는 문제를, 직접 잴 수 없는 회전 자석의 온도를 열 모델로 실시간 추정해 보정하는 방법으로 풀었다.[^p7] | 1저자 Jimin Youn, 마지막 저자 공경철 |
| 8 | 2026 | [Modeling of Ball Bearings for Accurate Force and Torque Transmission in Dynamic Robotic Systems](https://doi.org/10.1007/s12541-025-01423-2) · International Journal of Precision Engineering and Manufacturing | 로봇 관절의 베어링을 이상적인 관절로 두지 않고 내륜·외륜·볼로 나눠 모델링하면, 베어링 틈새·궤도 곡률·편심이 힘 전달을 크게 바꾼다는 것을 보이고 시뮬레이션 정확도를 높였다.[^p8] | 1저자 Jongwon Kim, 마지막 저자 공경철 |

## 교수와 전문 분야

공경철 교수는 서강대에서 기계공학·물리학 학사(2004, 최우등)와 기계공학 석사(2006)를, 미국 UC 버클리에서 기계공학 박사(2009)를 받았다. 박사 논문 주제는 사람을 보조하고 재활을 돕는 시스템의 메카트로닉스였고, 지도교수는 Masayoshi Tomizuka다.[^prof] UC 버클리 박사후연구원(2009–2011), 서강대 조교수·부교수(2011–2018)를 거쳐 2019년 KAIST 기계공학과 부교수가 됐고 2024년부터 교수다. 프랑스 파리이스트크레테유대(UPEC) 방문교수(2013–2015)도 지냈다.[^prof]

창업 경력도 있다. 2014년 SG메카트로닉스를 세웠고, 2017년 엔젤로보틱스(옛 SG로보틱스)를 공동 창업해 2017–2024년 대표이사(CEO), 2024년부터 회장(President)을 맡고 있다.[^prof] 사이배슬론 외골격 부문 금메달(2020·2024)과 동메달(2016·2020), 2018 평창 패럴림픽 착용형 로봇 성화 봉송,[^background] 산업통상자원부 10대 대표 성과(2023), 국가연구개발 우수성과 100선(2022), 평창 패럴림픽 기여 국무총리 표창(2019)이 랩에 적힌 주요 이력이다.[^prof]

논문으로 보면 전문 분야는 세 갈래다.

- **외골격 로봇의 보행 제어**: 완전마비 보행, 사용자 맞춤 보행 패턴, 정밀 제어.[^p1][^p2]
- **착용형 로봇의 메카트로닉스 설계**: 직렬 탄성 구동기, 구동기 온도 보정, 센서.[^p4][^p6][^p7]
- **재활 로봇의 임상 적용**: 뇌졸중 환자 대상 시험.[^p3]

## 응용 분야

대표 논문과 과제로 보면 하지마비 장애인의 일상 보행, 뇌졸중·노인성 보행 장애 재활, 군인·근로자의 근력 보조, AI 로봇용 구동 모듈에 닿아 있다.[^p1][^p3][^background][^projects] 랩의 분사 기업(Spin-off Company) 페이지는 엔젤로보틱스 누리집으로 연결된다.[^spinoff] 졸업생은 엔젤로보틱스·휴머닉스·삼성전자·현대자동차·국방과학연구소·한국기계연구원과 대학(상명대·영남대 등)으로 진출했다.[^alumni]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제와 이메일은 랩 표기를 옮겼다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Hyunho Jeong | 박사후연구원 | Wearable robot user's performance evaluation; Reinforcement learning for human application | hyunho.jeong@kaist.ac.kr |  |
| Jeongmin Kim | 박사후연구원 | Gait anslysis of wearable robot users; Usability evaluation of wearable and assitive robot systems | jeongmin.kim@kaist.ac.kr |  |
| Sanguk Choi | 박사과정 | Design and control of human assistive robots; Control of soft wearable robots for stroke patients; Control of series elastic actuators; Gait analysis for wearable robots | sangukchoi@kaist.ac.kr | 3, 4, 5 |
| Jongwon Kim | 박사과정 | Optimal control of wearable robot; Design and control of actuator | jongwon.kim@kaist.ac.kr | 4, 8 |
| Chanyoung Ko | 박사과정 | Design and control of human assistive wearable robots; Control of series elastic actuators | kkyle0927@kaist.ac.kr | 3, 4, 5 |
| Jimin Youn | 박사과정 | Design and control of human assistive wearable robots; Design of motor drivers and filters; Precise torque control in high temperature for wearable robots | yjm7845@kaist.ac.kr | 7 |
| Gunhee Lee | 박사과정 | Design and control of human assistive wearable robots; Design and control of actuators | gh003008@kaist.ac.kr |  |
| Hyojun An | 박사과정 | Design and control of human assistive wearable robots; Actuator force control | gywns99@kaist.ac.kr |  |
| Abhiraj Singh | 박사과정 | MPC-based control for powered exoskeletons; Learning-based control (RL) and sim-to-real transfer for robust assistance; RGB-D environment recognition and terrain-adaptive locomotion | abhirajsingh@kaist.ac.kr |  |
| Jinsu Park | 박사과정 | Effective human-robot interaction; RL-based robot control | jinsu.park@kaist.ac.kr |  |
| Jincheol Ha | 박사과정 | Design and control of wearable robots; RL-based control and robot simulation | jincheol.ha@kaist.ac.kr |  |
| Hendrik Herold | 석사과정 | Mechanical Design and Human Robot Interaction | hendrikm@kaist.ac.kr |  |
| Sungjune Shin | 석사과정 | Control of Exoskeletal Robot; Robot Simulation | sungjune.shin@kaist.ac.kr |  |
| Jaeyong Cho | 석사과정 | Design and control of wearable robots; Human Intention Recognition | jycho211@kaist.ac.kr |  |
| Mohammad Yousefi | 석사과정 | Machine Vision; Human Intention recognition | mohammad.yousefi@kaist.ac.kr |  |
| Wonil Kang | 석사과정 | Design and control of wearable robots; Control of Exoskeleton Robot | kangwonil1110@kaist.ac.kr |  |
| Rakyoung Kim | 석사과정 | Control and design of human assistive robot; Human intent recognition | kry5205@kaist.ac.kr |  |
| Dongryun Kang | 석사과정 | Design and control of wearable robots; Robot simulation and gait control | dongryun.kang@kaist.ac.kr |  |
| Miae Bae | 행정 직원 |  | miae_bae@kaist.ac.kr |  |
| Huitae Han | 학부 연구생 | Design and control of human assistive robots |  |  |
| Sunji Moon | 학부 연구생 | Sim-to-Real Control for Transparent Lower-limb Wearable Robots |  |  |

## 졸업생 진로

랩 졸업생 페이지의 목록이다. 연구교수·박사후연구원으로 있었던 사람도 함께 실려 있다. 진로는 랩이 적은 소속을 옮겼다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sehoon Oh | 연구교수 |  |
| Sungwon Shin | 연구교수 |  |
| Myunghyun Lee | 박사후연구원 | Researcher in Agency for Defense Development |
| JeongSu Park | Ph.D. (2026.07) | Senior Researcher in Angel Robotics |
| Taeyeon Kim | Ph.D. (2026.02) | Post-doctoral researcher in Yonsei Univ. College of Medicine |
| Hyeongjun Kim | Ph.D. (2025.08) | Angel Robotics |
| Mingoo Jeong | Ph.D. (2024.08) | Humanics |
| Gwangtae Kim | Ph.D. (2024.02) | Researcher in Agency for Defense Development |
| Jungsoo Cho | Ph.D. (2020.08) |  |
| Hanseung Woo | Ph.D. (2019.02) | Agency for Defense Development; ADD |
| Pyeong-gook Jung | Ph.D. (2019.02) | Samsung Electronics |
| Hyunjin Choi | Ph.D. (2019.02) | Sangmyung University |
| Byeonghun Na | Ph.D. (2019.02) | Angel Robotics |
| Jungsu Choi | Ph.D. (2018.08) | Yeungnam University |
| Seungwon Yun | M.S. (2026.02) | KAIST |
| Eunseok Song | M.S. (2024.08) | Samsung Electronics |
| Seongbin An | M.S. (2023.02) | Korea Institute of Machinery and Materials; KIMM |
| Minjun Kang | M.S. (2024.02) | Seoul National University |
| Hyeonseok Seo | M.S. (2023.08) | Samsung Electronics |
| Daeho Lee | M.S. (2022.08) | Agency for Defense Development; ADD |
| Sumin Lee | M.S. (2022.08) | Samsung Electronics |
| Dongha Nam | M.S. (2022.02) | Korea Advanced Institute of Science and Technology; KAIST |
| Youngsik Kim | M.S. (2021.08) | Hyundai Motor Company |
| Kyeongwon Park | M.S. (2021.02) | Stanford University |
| Hyunjune Song | M.S. (2020.02) |  |
| Heiseok Moon | M.S. (2019.02) | UPEC (Université Paris-Est Créteil) |
| Cheolmin Kwon | M.S. (2019.02) | Angel Robotics |
| Yooseok Kim | M.S. (2019.02) |  |
| Seungho Youn | M.S. (2019.02) |  |
| Minkyu Choi | M.S. (2018.02) |  |
| Kanghyun Kim | M.S. (2018.02) |  |
| Jangmok Lee | M.S. (2018.02) |  |
| Yeongsik Seo | M.S. (2017.08) |  |
| Joonyoung Jung | M.S. (2017.02) |  |
| Kyoungduk Park | M.S. (2016.02) |  |
| Myoungseok Lee | M.S. (2016.02) |  |
| Eunyoung Baek | M.S. (2015.02) |  |
| Seok-ki Song | M.S. (2015.02) |  |

## 최근 논문 목록 (2021–2026)

랩 학술지 논문 목록에 실린 2021–2026년 논문 15편이다. 서지는 랩 표기를 옮겼다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- J. Kim and K. Kong. "Modeling of Ball Bearings for Accurate Force and Torque Transmission in Dynamic Robotic Systems". *International Journal of Precision Engineering and Manufacturing, 2026*.

**2025**

- J. Kim, A. Singh, J. Youn, H. Kim, J. Park, J. Park and K. Kong. "Optimization of crutch-free walking for a powered exoskeleton considering human adaptation". *MECHATRONICS, vol.110, 2025*.
- S. Han, S. Choi, C. Ko, J. Lee, K. Kong and D. Rha. "Efficacy of a Soft Wearable Robot for Hip Assistance in Chronic Stroke Patients: A Randomized Crossover Trial". *IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol.33, pp.2251 - 2262, 2025*.
- J. Park, T. Kim and K. Kong. "Inertial Orientation Estimation Robust to Impact for Bipedal Robot Locomotion". *International Journal of Control, Automation and Systems, vol.23, no.4, pp.1139-1146, 2025*.
- S. Choi, J. Kim, C. Ko and K. Kong. "Flexi-SEA: Flexible-Shaft-Driven Series Elastic Actuator for Wearable Robots". *IEEE/ASME Transactions on Mechatronics, vol.29, no.4, pp.3019 - 3027, 2025*.

**2024**

- J. Youn, H. Kim, K. Shi and K. Kong. "Thermal Characteristic Modeling and Compensation for the Improvement of Actuator Homeostasis". *IEEE/ASME Transactions on Mechatronics, vol.29, pp.3019 - 3027, 2024*.
- T. Kim and K. Kong. "Plantar Flexion Muscle Force Estimation With a Soft Wearable Pneumatic Sensor System". *IEEE/ASME Transactions on Mechatronics, vol.29, pp.2920 - 2928, 2024*.

**2023**

- S. Choi, C. Ko, and K. Kong. "Walking-Speed-Adaptive Gait Phase Estimation for Wearable Robots". *Sensors, vol.23, no.19, 2023*.
- S. Lee, S. Choi, C. Ko, T. Kim and K. Kong. "Design and Control of the Compact Cable-driven Series Elastic Actuator Module in Soft Wearable Robot for Ankle Assistance". *International Journal of Control, Automation and Systems, vol.21, no.5, pp.1624-1633, 2023*.
- S. An, J. Feng, E. Song, K. Kong, J. Kim and H. Choi. "High-Accuracy Hand Gesture Recognition on the Wrist Tendon Group Using Pneumatic Mechanomyography (pMMG)". *IEEE Transactions on Industrial Informatics, 2023*.
- J. Park, D. Lee and K. Kong. "Shank Shock Absorption Mechanism and Associated Gait Pattern Design for Reduction of Ground Impact of a Powered Exoskeleton". *International Journal of Control, Automation and Systems, vol.21, pp.1959–1969, 2023*.
- G. Kim, M. Lee, Y. Kim and K. Kong. "Robust Gait Event Detection Based on the Kinematic Characteristics of a Single Lower Extremity". *International Journal of Precision Engineering and Manufacturing, pp.987–1000, 2023*.

**2022**

- K. Park, J. Choi, and K. Kong. "Hybrid Filtered Disturbance Observer for Precise Motion Generation of a Powered Exoskeleton". *IEEE Transactions on Industrial Electronics, pp.1-1, 2022*.
- K. Park, J. Choi, and K. Kong. "Iterative Learning of Human Behavior for Adaptive Gait Pattern Adjustment of a Powered Exoskeleton". *IEEE Transactions on Robotics, pp.1-15, 2022*.

**2021**

- H. Woo, K. Kong, and D. Rha. "Lower-Limb-Assisting Robotic Exoskeleton Reduces Energy Consumption in Healthy Young Persons during Stair Climbing". *Applied Bionics and Biomechanics, 2021*.

## 특허 (2021년 이후 출원)

랩 특허 목록에서 2021년 이후 출원한 8건이다.[^patents]

- 앞으로 착용하는 외골격 로봇 (발명자 공경철 박정수 시경수 이건희 안효준; 출원번호 10-2024-0045132)
- 착용형 로봇의 제어방법 (발명자 고찬영, 최상욱, 윤용탁, 공경철; 출원번호 10-2022-0144369; 등록번호 10-2711338)
- 케이블 견인 구동장치 및 이를 포함하는 착용형 슈트 (발명자 이수민, 조현태, 윤용탁, 공경철; 출원번호 10-2022-0041802; 등록번호 10-2649630)
- 동작의도 측정센서 및 동작의도 측정 시스템 (발명자 안성빈, 최현진, 공경철; 출원번호 10-2021-0064017; 등록번호 1028410800000)
- 하체 보조로봇 (발명자 박정수,나병훈,공경철; 출원번호 10-2021-0064403)
- 다족 로봇용 다리유닛 (발명자 조정수, 공경철; 출원번호 10-2021-0043249; 등록번호 1024453080000)
- 탄성 감속 구동기 및 이를 구비하는 착용형 보조장치 (발명자 김태연 시경수 정민구 공경철; 출원번호 10-2021-0003724; 등록번호 1024904410000)
- 착용형 보조장치 (발명자 정민구 김태연 우한승 김형준 공경철; 출원번호 10-2021-0000333; 등록번호 1026334700000)

## 연구 과제

랩 과제 페이지(Funded Projects)에 게시된 과제다. 끝난 과제도 함께 실려 있다.[^projects]

- 형상기억합금 코일 섬유형 인공근육기반 초경량·고출력 하이브리드 구동기를 적용한 고령자 및 하지마비 장애인 보조용 웨어러블 로봇 플랫폼 개발 (기간 2025-04-01~2029-12-31; 지원 한국연구재단 / 과학기술정보통신부)
- 인간친화형 로봇 스케일업 밸리 혁신 생태계 구축 (기간 2025-07-01 ~ 2028-12-31; 지원 한국연구재단 / 과학기술정보통신부)
- 노인성 보행장애 극복을 위한 관절 보호 및 근육 기능 회복 웨어러블 로봇 기술 연구 (기간 2024.09.01 ~ 2026.08.31; 지원 한국연구재단 / 교육부)
- AI 기반 로봇을 위한 Sim-to-real 수준의 고토크-무저항 구동모듈 개발 (기간 2024.07.01 ~ 2026.12.31.; 지원 한국산업기술기획평가원 / 산업통상자원부)
- 보행장애 완전극복 웨어러블 로봇기술을 위한 인간운동제어이론 연구 (기간 2022.06.01 ~ 2031.02.28; 지원 한국연구재단 / 과학기술정보통신부)
- 하지 완전마비 장애인의 일상생활 보조 및 재활을 위한 전동형 외골격 로봇 및 보행 제어 알고리즘 개발(KAIST-정착) (기간 2019-01-01 ~ 2021-12-30; 지원 KAIST)
- 통합성능 시험장치 및 통계적 성능 DB 획득 (기간 2021-03-01 ~ 2024.06.30; 지원 국방과학연구소(ADD))
- KAIST 산학 연계 PDAM(Power Door Assist Module) 연구 개발 (기간 2021-12-01 ~ 2022.06.30; 지원 평화정공(PHA))
- 착용형 로봇 고속동기 제어를 위한 생체신호 유연센서 기반의 동작의도 인식 시스템 개발 (기간 2020.07.01 ~ 2024.12.31; 지원 한국연구재단 / 한국과학기술원)
- 뇌졸중 환자의 일상생활 보조를 위한 유연한 동력전달구조를 갖는 로봇보조기기의 메카트로닉스 요소설계기술개발연구 (기간 2020.04.01 ~ 2023.12.31; 지원 한국보건산업진흥원 / 보건복지부)

## 연락과 위치

- 교수 이메일: kckong@kaist.ac.kr[^prof]
- 교수 전화: 042-350-3012[^prof]
- 연구실 전화: 042-350-5229[^home]
- 위치: KAIST 기계공학동(N7-3) 3206호 (대전 유성구 대학로 291)[^prof] 제작 공간과 시제품 제작실은 기계공학동 3층 3210호에 있다.[^infra]

[^home]: 랩 첫 화면 <https://robotics.kaist.ac.kr/> (2026-10-19 열람)
[^background]: 랩 소개 페이지(Background) <https://robotics.kaist.ac.kr/sub1_1> (2026-10-19 열람)
[^infra]: 랩 연구 시설 페이지(Research Infra) <https://robotics.kaist.ac.kr/sub1_3> (2026-10-19 열람)
[^projects]: 랩 과제 페이지(Funded Projects) <https://robotics.kaist.ac.kr/sub1_5> (2026-10-19 열람)
[^research]: 랩 연구 비전 페이지(Application Research) <https://robotics.kaist.ac.kr/sub3_3> (2026-10-19 열람)
[^api]: 랩 연구 페이지(Artificial Physical Intelligence) <https://robotics.kaist.ac.kr/sub3_6> (2026-10-19 열람)
[^hmfm]: 랩 연구 페이지(Human Motion Foundation Model) <https://robotics.kaist.ac.kr/sub3_7> (2026-10-19 열람)
[^hris]: 랩 연구 페이지(Human-Robot Integrated Simulation) <https://robotics.kaist.ac.kr/sub3_8> (2026-10-19 열람)
[^papers]: 랩 학술지 논문 목록(Journal Papers) <https://robotics.kaist.ac.kr/sub3_4_a> (2026-10-19 열람)
[^patents]: 랩 특허 목록 <https://robotics.kaist.ac.kr/sub3_5> (2026-10-19 열람)
[^prof]: 랩 교수 페이지(Director) <https://robotics.kaist.ac.kr/sub5_2> (2026-10-19 열람)
[^people]: 랩 구성원 페이지(Researchers) <https://robotics.kaist.ac.kr/sub5_3> (2026-10-19 열람)
[^alumni]: 랩 졸업생 페이지(Alumni) <https://robotics.kaist.ac.kr/sub5_4> (2026-10-19 열람)
[^spinoff]: 랩 분사 기업 페이지(Spin-off Company) <https://robotics.kaist.ac.kr/sub6_1> (2026-10-19 열람)
[^p1]: K.-W. Park, J. Choi, K. Kong, IEEE Transactions on Robotics 38, 1395-1409 (2022). <https://doi.org/10.1109/tro.2022.3144955> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K.-W. Park, J. Choi, K. Kong, IEEE Transactions on Industrial Electronics 70, 646-656 (2023). <https://doi.org/10.1109/tie.2022.3152016> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S.-H. Han 외, D. Y. Kim, IEEE Transactions on Neural Systems and Rehabilitation Engineering 33, 2251-2262 (2025). <https://doi.org/10.1109/tnsre.2025.3577600> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Choi, J. Kim, C. Ko, K. Kong, IEEE/ASME Transactions on Mechatronics 30, 6882-6892 (2025). <https://doi.org/10.1109/tmech.2025.3537113> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Choi, C. Ko, K. Kong, Sensors 23, 8276 (온라인 2023-10-06). <https://doi.org/10.3390/s23198276> 초록 기준.
[^p6]: T. Kim, K. Kong, IEEE/ASME Transactions on Mechatronics 29, 2920-2928 (2024). <https://doi.org/10.1109/tmech.2024.3398224> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Youn, H. Kim, K. Shi, K. Kong, IEEE/ASME Transactions on Mechatronics 29, 3019-3027 (2024). <https://doi.org/10.1109/tmech.2024.3400214> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Kim, K. Kong, International Journal of Precision Engineering and Manufacturing 27, 1485-1495 (온라인 2026-01-08). <https://doi.org/10.1007/s12541-025-01423-2> 초록 기준.

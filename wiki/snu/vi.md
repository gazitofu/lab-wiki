# 지능형자동차 연구실 (Vehicle Intelligence Lab, VI Lab)

**서울대학교 공과대학 전기·정보공학부 · 서승우 교수**

- 분야: 도심·비포장 지형의 자율주행, 카메라·라이다 인식, 지도 작성과 위치 추정, 안전을 고려한 경로·제어, 복합 과제의 행동 학습
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 자율주행[^r1][^r4][^r7], 로봇 항법·SLAM[^r3], 컴퓨터 비전[^r1][^r2][^p8], 강화학습[^r4][^r5][^p7]
- 홈페이지: <http://vi.snu.ac.kr>
- 근거와 출처: [지능형자동차 연구실 근거 페이지](vi-sources.md)

> 차량이 주변을 알아보고 자기 위치와 갈 길을 판단해 스스로 주행하도록, 센서와 차량 장치부터 인식·위치 추정·제어 프로그램까지 함께 개발하는 연구실이다.[^lab][^r7]

## 무엇을 연구하나

서울대학교 전기·정보공학부 서승우 교수가 이끄는 지능형자동차 연구실은 1996년 설립됐다. 도심뿐 아니라 도로가 정비되지 않은 곳과 지형이 험한 곳의 자율주행(차량이 주변을 인식하고 경로를 정해 스스로 움직이는 기술)을 목표로 한다. 차량과 센서 장치부터 차량 안의 프로그램까지 개발하고, 시스템의 동작을 모형으로 재현해 살펴보는 시뮬레이션과 실제 환경을 함께 활용한다.[^lab]

인식 연구는 카메라 영상과 라이다(빛을 보내 돌아오는 신호로 거리를 재는 장치)로 주변의 차량·사람·자전거 등을 찾는 일이다. 물체 검출(관측 자료에서 물체의 종류와 위치·크기를 찾는 기술)과 물체 추적(여러 시점에 관측된 같은 물체를 연결해 움직임을 파악하는 기술), 영상의 영역을 종류별로 구분하는 방법을 다룬다. 카메라 소개는 정답을 붙인 자료로 배우는 지도학습을 사용하며, 일부 자료에만 정답이 있는 반지도학습과 정답 표시 없이 자료의 구조를 배우는 비지도학습은 추가 연구 계획으로 적는다.[^r1][^r2] 지도 작성과 측위(자신의 위치를 알아내는 일) 연구에서는 센서 자료와 지도를 비교하고, 아직 지도가 없는 곳에서는 SLAM(Simultaneous Localization and Mapping, 자기 위치 추정과 지도 작성을 함께 수행하는 기술)을 사용한다.[^r3]

안전을 고려한 주행 판단은 다른 주체의 행동 시범을 보고 행동 방법을 배우는 모방학습과 강화학습을 활용한다. 연구실은 전문가의 주행 자료를 활용한다고 밝힌다.[^r4] 강화학습은 행동 결과의 평가값인 보상을 바탕으로 앞으로 받을 보상의 합을 크게 하는 행동 방법을 배우는 방식이다. 연구실은 학습한 주행 판단과 규칙에 따른 안전 확인 부분을 결합하고, 주행 상황에 맞는 안전 범위를 정하는 방법을 연구한다.[^r4][^r6] 자율주행 검증 환경 K-City에서는 라이다로 얻은 공간의 점 자료인 포인트클라우드를 이용한 물체 검출, 주변 차량의 미래 경로 예측, 전문가 운전 자료를 이용한 경로 생성, 여러 상황의 자료를 균형 있게 유지하는 학습 자료 관리 기술을 개발·검증한다고 소개한다.[^r7]

복합 과제의 행동 학습은 현재 상황에 맞는 하위 과제를 고르고, 다음 과제로의 전환을 예측하며, 서로 다른 과제에서 쓸 수 있는 행동 방법을 학습하는 연구다. 이미 배운 것을 잊는 문제와 새 과제로 지식을 옮기는 문제도 다룬다.[^r5] 최근 논문은 영상 정보를 주행 행동의 순서에 맞게 정리하는 방법,[^p1] 여러 중간 목표를 순서대로 구성하는 방법,[^p5] 바뀌는 환경에서 기존 행동을 유지하고 조합하는 방법을 제안했다.[^p6]

비포장 지형에서는 로봇이 해당 구간을 통과할 수 있는 정도인 주행 가능성을 추정하고 경로 계획에 반영한다. 지형과 로봇 내부 상태를 함께 고려하거나 로봇이 이미 지나간 경로로 학습하는 연구가 있다.[^p2][^p3] 첫 화면은 연구 그룹을 「Intelligent Vehicle Cooperative riving」(차량 협력 주행), 「Vehicular Image Processing」(차량 영상 처리), 「Energy Management System」(에너지 관리 시스템)으로 소개한다.[^home]

## 주요 연구 주제

### 1. 카메라·라이다 인식과 지도·위치 추정

차량 주변 물체의 종류·위치·크기와 움직임을 알아내고, 센서 자료로 지도를 만들며 위치를 추정한다.[^r1][^r2][^r3] 대표 논문은 영상에서 얻은 정보와 주행 행동의 관계를 학습하고, 종류별 자료 수가 치우친 영상 인식의 학습 목표를 설계한다.[^p1][^p8]

### 2. 비포장 지형의 주행 가능성 추정

주변 지형으로 판단한 주행 가능성과 로봇 내부 상태를 반영한 주행 가능성을 구분해 경로 계획과 제어(장치에 줄 입력을 정해 원하는 동작을 이끌어내는 일)에 넣고, 지형·영상과 로봇이 지나간 경로로 통과 가능한 구간을 학습한다.[^p2][^p3]

### 3. 안전을 고려한 주행 판단과 낯선 상황의 복귀

학습 기반 판단에 규칙 기반 안전 확인을 결합하고, 주행 상황별 안전 범위를 다룬다.[^r4][^r6] 주변 차량의 움직임 예측과 차량 제어를 함께 학습하는 연구와, 원래 학습한 상황을 벗어난 로봇이 복귀하도록 재학습하는 연구가 있다.[^p4][^p7]

### 4. 복합 과제를 다루는 행동 학습

복합 과제를 하위 과제로 나누고 과제 간 전환과 지식 이전을 학습한다.[^r5] 여러 중간 목표를 순서대로 만드는 방법과, 환경이 바뀌어도 이전 행동을 유지하며 새 행동을 조합하는 방법을 다룬다.[^p5][^p6]

## 대표 논문

Current 목록의 2021–2026년 논문 가운데 서승우 교수가 저자이고 서울대 재직 시기에 해당하며 초록을 확인한 8편을 네 연구 갈래에 나누어 골랐다. 2026년 논문 2편을 포함한다. 연도는 Current 목록의 표기이고, 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. arXiv 판을 읽은 논문은 각주에 그 판본을 표시했다. 제목의 RL은 Reinforcement Learning, 즉 강화학습의 줄임말이다.[^pubs]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Ordinal Neural Collapse as a Representation Prior for Visual Navigation](https://doi.org/10.1007/978-3-032-37356-4_24) · ECCV 2026, arXiv 판 | 영상에서 얻은 정보를 주행 행동의 순서와 연결하는 ORION(Ordinal Neural Collapse for Visual Navigation)을 제안했다. 왼쪽에서 오른쪽으로 이어지는 행동 방향의 순서에 맞게 영상 정보를 정리하고, 이를 로봇이 위치를 파악하고 길을 정해 이동하는 항법 학습에 사용했다. 시뮬레이션과 실제 환경에서 주행 성공과 목표 접근 정도를 평가했다.[^p1] | 1저자 E-In Son, 마지막 저자 Seung-Woo Seo |
| 2 | 2024 | [Traversability-aware Adaptive Optimization for Path Planning and Control in Mountainous Terrain](https://doi.org/10.1109/LRA.2024.3387042) · IEEE Robotics and Automation Letters | 산악 지형의 주행 가능성을 주변 지형의 모습뿐 아니라 로봇의 속도 같은 내부 상태까지 고려해 판단했다. 이를 경로 계획과 움직임 제어에 반영해 위험 구간과 갇히는 상황을 피하도록 했다. 시뮬레이션과 실제 환경에서 검증했다.[^p2] | 1저자 Se-Wook Yoo, 마지막 저자 Seung-Woo Seo |
| 3 | 2024 | [Follow the Footprints: Self-supervised Traversability Estimation for Off-road Vehicle Navigation based on Geometric and Visual Cues](https://arxiv.org/abs/2402.15363) · ICRA 2024, arXiv 판 | 비포장 지형에서 로봇이 통과할 수 있는 곳을 추정했다. 지형의 경사와 영상 속 대상의 의미를 함께 처리하고, 로봇이 실제 지나간 경로를 학습의 근거로 사용해 로봇 종류의 특성도 반영했다. 자동차와 무인 지상 차량을 포함한 여러 조건에서 적용을 평가했다.[^p3] | 1저자 Yurim Jeon, 마지막 저자 Seung-Woo Seo |
| 4 | 2022 | [GIN: Graph-based Interaction-aware Constraint Policy Optimization for Autonomous Driving](https://doi.org/10.1109/LRA.2022.3227862) · IEEE Robotics and Automation Letters | 주변 차량의 의도가 바뀌는 상황에 대응하도록, 차량 사이의 관계를 점과 선으로 나타낸 정보를 써 움직임 예측과 제어를 함께 학습했다. GIN(Graph-based Interaction-aware Constraint Policy Optimization)은 두 부분이 정보를 공유하고 서로 결과를 반영하게 하며, 도심 주행 시뮬레이션에서 평가됐다.[^p4] | 1저자 Se-Wook Yoo, 마지막 저자 Seung-Woo Seo |
| 5 | 2026 | [Chain-of-Goals Hierarchical Policy for Long-Horizon Offline Goal-Conditioned RL](https://arxiv.org/abs/2602.03389) · ICML 2026, arXiv 판 | 오랜 단계에 걸친 목표를 수행하도록 CoGHP(Chain-of-Goals Hierarchical Policy)를 제안했다. 현재 상태와 최종 목표를 받아 중간 목표들을 순서대로 만든 뒤 실제 행동을 정한다. 앞서 만든 목표가 뒤의 예측에 반영되는 하나의 구조를 사용하며, 이동과 물체를 다루는 과제에서 평가했다.[^p5] | 1저자 Jinwoo Choi, 마지막 저자 Seung-Woo Seo |
| 6 | 2023 | [Unsupervised Skill Discovery for Learning Shared Structures across Changing Environments](https://proceedings.mlr.press/v202/lee23r.html) · ICML 2023 | 환경이 바뀌어도 쓸 수 있는 행동 묶음을 학습하는 방법을 제안했다. 이전에 배운 행동들을 조합해 도달한 범위를 새 행동이 넓히도록 하고, 중복된 행동이 쌓이지 않도록 평가 과정을 넣었다. 미로 이동과 이동 동작 과제에서 시험했다.[^p6] | 1저자 Sang-Hyun Lee, 마지막 저자 Seung-Woo Seo |
| 7 | 2023 | [SeRO: Self-Supervised Reinforcement Learning for Recovery from Out-of-Distribution Situations](https://doi.org/10.24963/ijcai.2023/432) · IJCAI 2023 | 강화학습 로봇이 학습 때 경험한 상황의 범위를 벗어나면 믿기 어려운 행동을 할 수 있다. SeRO(Self-Supervised Reinforcement Learning for Recovery from Out-of-Distribution Situations)는 로봇이 이런 상황을 알아차리고, 이전에 학습한 상황으로 돌아가도록 스스로 학습 근거를 만드는 재학습 방법이다. 복귀 능력과 원래 과제의 성능 회복을 실험했다.[^p7] | 1저자 Chan Kim, 넷째 저자 Seung-Woo Seo, 마지막 저자 Seong-Woo Kim |
| 8 | 2023 | [Long-Tailed Recognition by Mutual Information Maximization between Latent Features and Ground-Truth Labels](https://proceedings.mlr.press/v202/suh23a.html) · ICML 2023 | 종류별 자료 수가 치우친 영상 인식에서 학습 목표를 설계했다. 입력 자료 자체 대신 학습된 특징(자료를 구별하고 설명하는 성질이나 정보)과 정답 종류 사이에 공유되는 정보를 키우도록 해, 자료 사이의 관계를 배우는 방식과 종류별 자료 수를 고려하는 보정 방식을 연결했다. 영상 분류와 영상의 영역을 종류별로 나누는 과제에서 평가했다.[^p8] | 1저자 Min-Kook Suh, 마지막 저자 Seung-Woo Seo |

## 교수와 전문 분야

서승우 교수는 서울대학교 전기공학 학사(1987)와 석사(1989), 미국 Pennsylvania State University 전기공학 박사(1993)를 받았다. 연구실 교수 소개는 Pennsylvania State University 컴퓨터공학과 조교수(1993년 8월–1994년 7월), Princeton University 전기공학과 및 POEM 연구소 연구원(1994년 8월–1996년 7월)을 거쳐 1996년 7월 서울대학교 교수로 부임했다고 적는다.[^faculty] 학과는 현재 소속을 전기·정보공학부로, 직위를 교수로 게시한다.[^prof]

학과 교수 소개의 전공은 무선과 차량제어 네트워크, 정보 보안이며, 연구 관심은 무인자동차·자동차 통신·통신 및 네트워크 보안이다. 2009년부터 지능형자동차IT연구센터 센터장, 2010년부터 만도이노베이션랩 운영책임교수, 2013년부터 LG전자 스마트카공동연구센터 운영책임교수로 게시되어 있다. Stanford University CARS 방문교수(2013–2014), 대한전자공학회 회장(2022–2023) 경력도 적혀 있다.[^prof]

최근 논문에서 확인되는 전문 분야는 영상 인식과 시각 정보를 이용한 로봇 항법,[^p1][^p8] 비포장 지형의 통과 가능성 추정과 경로·제어,[^p2][^p3] 주변 차량을 고려한 주행 판단과 낯선 상황에서의 복귀,[^p4][^p7] 복합 과제의 중간 목표·행동 학습이다.[^p5][^p6]

## 응용 분야

연구실은 도심 자율주행의 측위·인식·판단·제어·시스템 관리 기술을 K-City에서 개발·검증한다고 소개한다.[^r7] 학과 소개는 도로가 정비되지 않은 곳과 지형이 험한 곳의 자율주행까지 목표로 든다.[^lab] 대표 논문은 영상으로 길을 찾는 로봇, 산악·비포장 지형의 로봇과 자동차, 주변 차량이 있는 도심 주행을 다룬다.[^p1][^p2][^p3][^p4]

## 구성원

2026년 10월 27일 Ph.D Candidates 13명과 M.S Candidates 4명이다. 과정과 연구 관심은 해당 목록의 표기이며 Student Representative도 원문 표기다. 「대표 논문 참여」는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^phd][^ms]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Yunjae Jeong (정윤재) | 박사과정 | - Point cloud representation learning | yujs30@snu.ac.kr |  |
| Daeyoung Kim (김대영) | 박사과정 | Representation learning Semantic segmentation | ddykim@snu.ac.kr |  |
| Jinwoo Choi (최진우) | 박사과정 | Reinforcement learning Representation learning Path planning Decision making | wlsdn9350@snu.ac.kr | 4, 5 |
| Jisung Bae (배지성) | 박사과정 (Student Representative) | SLAM (Lidar SLAM) Lidar Odometry Specialized localization | trr0631@snu.ac.kr |  |
| Jinheock Choi (최진혁) | 박사과정 | Lidar odometry | jinheock@snu.ac.kr |  |
| Keonwoo Kim (김건우) | 박사과정 | Dual learning | dayclear94@snu.ac.kr |  |
| Dongwook Kim (김동욱) | 박사과정 | Visual Odometry, Structure from Motion Simultaneous Localization and Mapping Point cloud segmentation | sgr01086@snu.ac.kr |  |
| Ji-Hoon Hwang (황지훈) | 박사과정 | Semantic Segmentation Visual Navigation | hoons21@snu.ac.kr |  |
| E In Son (손이인) | 박사과정 | - Reinforcement Learning - Path Planning | pingpang@snu.ac.kr | 1, 2, 3 |
| Jiwon Lee (이지원) | 박사과정 |  | zzwon1212@snu.ac.kr |  |
| Kun Park (박건) | 박사과정 | SLAM 3D reconstruction Localization | gun615@snu.ac.kr |  |
| Jung-Taak Kim (김정탁) | 박사과정 | - Visual Navigation - Path Planning - Robot Learning | mychoco333@snu.ac.kr | 1 |
| Yeonkyu Lee(이연규) | 박사과정 |  | yeonkyu011@snu.ac.kr |  |
| Kangsun Lee (이강선) | 석사과정 | planning, reinforcement learning | calvin1225@snu.ac.kr |  |
| Heungchan Kwon (권흥찬) | 석사과정 | Visual Localization, 3D Gaussian Splatting | samkwon1122@snu.ac.kr |  |
| Hyeokjun Kwon (권혁준) | 석사과정 | Vision-Language-Action Model, Robot Learning, Edge AI | hyeokjun@snu.ac.kr |  |
| Myungshin Kang (강명신) | 석사과정 | Reinforcement Learning, Representation Learning | audtls225@snu.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 목록의 75명이다. 학위와 연도는 게시되어 있지 않아 시기를 구분하지 않은 목록이며 최근 5년 졸업자만을 뜻하지 않는다. 진로는 누리집에 게시된 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyungsuk Yoon (윤형석) |  | 삼성미래로봇추진단 |
| Mingu Jeon |  | Associate Professor, Pusan National University. |
| Chan Kim (김찬) |  | 삼성미래로봇추진단 |
| Hwichang Kim (김휘창) |  | 한화시스템 |
| Se-Wook Yoo (유세욱) |  | 삼성 MX |
| Dongwook Yang |  | Samsung Research (SR) |
| Minkook Suh |  | LG Electronics |
| Yurim Jeon |  | Boeing Korea |
| Myungwoo Woo |  |  |
| JaeKyung Cho |  | SKT |
| Younghwa Jung |  | Samsung Advanced Institute of Technology (SAIT) |
| Sihyeon Jo |  | Dunamu |
| Yeon-Jun Lee |  | Samsung Electronics |
| Soomok Lee |  | Assistant professor of Computer Science, Kennesaw State University |
| Han-Seul Lee |  | SK Hynix |
| In-Sub Yoo |  | Samsung Electronics |
| Myung-Ok Shin |  | Samsung Electronics |
| Gi-Poong Gwon |  | Phantom AI |
| Seung-Tak Choi |  | TmaxSoft |
| Bo-Kyung Seo |  | TmaxSoft |
| Mid-Eum Choi |  | Samsung Electronics, DMC |
| Xavier Jerald Punithan |  | LG Electronics |
| Junhwa Hur |  | Ph.D student, Technische Universität Darmstadt |
| Seung-Nam Kang |  |  |
| Seung-Ho Lee |  | Georgia Tech |
| Seung-Ho Yoo |  | SAP |
| Young-Hoon Park |  | Associate Professor, Sookmyung Women's University |
| Thomas Morris |  | Samsung Electronics |
| Dong-Hyun Je |  | Samsung Electronics |
| Moon-Young Chung |  | Samsung Electronics |
| Seong-Woo Kim |  | Associate Professor, Seoul National University |
| Jong-Ho Park |  | Samsung Electronics |
| Il-Hyung Park |  |  |
| Minho Park |  | Associate Professor, Soongsil University |
| Yang Ji |  | Samsung Electronics |
| Hyung-Jun Kim |  |  |
| Yoon-Ho Choi |  | Associate Professor, Pusan National University |
| Sang-Kon Kim |  | Assistant Professor, Korea University |
| Ju-Hyung Son |  | LG Electronics |
| Zhu Feng |  | Samsung Electronics |
| Dong-Wook Jung |  |  |
| Jun-Sik Lee |  | Korea Electric Testing Institute |
| Dong-Hwe Geum |  | High School Teacher |
| Song-Woo Lee |  |  |
| Veronika Kondratieva |  |  |
| Sergey Seleznev |  | Samsung Electronics |
| Chung-Keun Lee |  | Samsung Electronics |
| Ji-Hoon Yun |  | Associate Professor, Seoul National University of Science and Technology |
| Jae-Han Lim |  | Assistant Professor, Kwangwoon University |
| Il-Hwan Kim |  |  |
| Heng-Geol Choi |  | Apple CTL |
| Jung-Yeop Ji |  | KT |
| Seok-Jun Yeom |  | KT |
| Han-You Jeong |  | Professor, Pusan National University |
| Ji-Ho Yun |  | DMR |
| Ji-Wan Cho |  |  |
| Jae-Jun Song |  | Game Vil |
| Su-Jin Kim |  |  |
| Sung-Ho Ju |  | KEPCO |
| Hyung-Il Lee |  | Korean Intellectual Property Office |
| Zhao Hui |  |  |
| Do-Hyung Lim |  | LG Electronics |
| Chang-Woo Lee |  |  |
| Jae-Hyun Woo |  |  |
| Byung-Jun Min |  | Nexon |
| Won-Rock Doh |  | Samsung Electronics |
| Jae-Min An |  | Samsung Electronics |
| Jung-Hwan Seo |  |  |
| Sang-Wan Kim |  | Silicon Image, Inc. in San Jose, USA |
| Chang-Hyung Lee |  | Samsung Electronics |
| Hyun-Taek Oh |  | Samsung Networks |
| Kyung-Jung Ho |  | KT |
| Ji-Yun Yu |  |  |
| Dong-Gi Kim |  |  |
| SSang-Soo Lee |  | LG Display |

## 최근 논문 목록 (2021–2026)

Current (2015~)의 2021–2026년 항목 중 서승우 교수가 저자인 논문 31편과 학과 소개에만 있는 1편으로, 중복을 제외한 32편이다. 연도는 각 출처의 게시 연도를 따랐다. Current의 International Conference와 International Journal 두 구획을 합쳤으며, 학과 목록과 겹치는 7편은 한 번씩 실었다.[^pubs][^lab] ICML 2026의 Chain-of-Goals는 arXiv 판으로 확인했고, 다른 논문도 각주가 밝힌 판본을 기준으로 설명했다.[^p5]

**2026**

- E In Son, Jung-Taak Kim, Seung-Woo Seo. "Ordinal Neural Collapse as a Representation Prior for Visual Navigation". *European Conference on Computer Vision (ECCV)*.
- Jinwoo Choi;  Sang-Hyun Lee; Seung-Woo Seo. "Chain-of-Goals Hierarchical Policy for Long-Horizon Offline Goal-Conditioned RL". *International Conference on Machine Learning (ICML)*.

**2025**

- Jinwoo Choi, Seung-Woo Seo. "Dynamic Contrastive Skill Learning with State-Transition Based Skill Clustering and Dynamic Length Adjustment". *International Conference on Learning Representations (ICLR) , 2025*.
- Chan Kim\*, Keonwoo Kim\*, Mintaek Oh, Hanbi Baek, Jiyang Lee, Donghwi Jung, Soojin Woo, Younkyung Woo, John Tucker, Roya Firoozi, Seung-Woo Seo, Mac Schwager, Seong-Woo Kim. "E2Map: Experience-and-Emotion Map for Self-Reflective Robot Navigation with Language Models". *IEEE International Conference on Robotics and Automation (ICRA), 2025*.
- Kun Park, Seung-Woo Seo. "SAGA-SLAM: Scale-Adaptive 3D Gaussian Splatting for Visual SLAM". *IEEE Robotics and Automation Letters*.
- Ji-Hoon Hwang, Daeyoung Kim, Hyung-Suk Yoon, Dong-Wook Kim, and Seung-Woo Seo. "How to Relieve Distribution Shifts in Semantic Segmentation for Off-road Environments". *IEEE Robotics and Automation Letters (RA-L)*.

**2024**

- Yurim Jeon, E-In Son, and Seung-Woo Seo. "Follow the Footprints: Self-supervised Traversability Estimation for Off-road Vehicle Navigation based on Geometric and Visual Cues". *International Conference on Robotics and Automation (ICRA)*.
- Mingu Jeon, Jae-Kyung Cho, Hee-Yeun Kim, Byeonggyu Park, Seung-Woo Seo, Seong-Woo Kim. "Non-Line-of-Sight Vehicle Localization Based on Sound". *IEEE Transactions on Intelligent Transportation Systems*.
- Dong-Wook Kim, E-In Son, Chan Kim, Ji-Hoon Hwang, Seung-Woo Seo. "PTS-Map: Probabilistic Terrain State Map for Uncertainty-Aware Traversability Mapping in Unstructured Environments". *IEEE Robotics and Automation Letter*.
- Yoonjae Jung, Sang-Hyun Lee, and Seung-Woo Seo. "3D Directional Encoding for Point Cloud Analysis". *IEEE Access*.
- Mingu Jeon,In-Ho Choi,Seung-Woo Seo,Seong-Woo Kim. "Extremely Rare Anomaly Detection Pipeline in Semiconductor Bonding Process with Digital Twin-driven Data Augmentation Method". *IEEE Transactions on Components, Packaging and Manufacturing Technology (T-CPMT)*.
- Sang-Hyun Lee, Yoonjae Jung, Seung-Woo Seo. "Imagination-augmented Hierarchical Reinforcement Learning for Safe and Interactive Autonomous Driving in Urban Environments". *IEEE Transactions on Intelligent Transportation Systems (T-ITS)*.
- Gyumin Oh, Seung-Woo Seo. "Fast and Robust 6-DoF LiDAR-based Localization of an Autonomous Vehicle against Sensor Inaccuracy". *IEEE Robotics and Automation Letters (RA-L)*.
- Se-Wook Yoo\*, E-In Son\*, and Seung-Woo Seo. "Traversability-aware Adaptive Optimization for Path Planning and Control in Mountainous Terrain". *IEEE Robotics and Automation Letter (RA-L)*.
- Sang-Hyun Lee and Seung-Woo Seo. "Self-Supervised Curriculum Generation for Autonomous Reinforcement Learning without Task-Specific Knowledge". *IEEE Robotics and Automation Letters (RA-L)*.
- Hyung-Suk Yoon, Ji-Hoon Hwang, Chan Kim, E-In Son, Se-Wook Yoo, and Seung-Woo Seo. "Adaptive Robot Traversability Estimation Based on Self-Supervised Online Continual Learning in Unstructured Environments". *IEEE Robotics and Automation Letters (RA-L)*.

**2023**

- Sang-Hyun Lee and Seung-Woo Seo. "Unsupervised Skill Discovery for Learning Shared Structures across Changing Environments". *International Conference of Machine Learning (ICML)*.
- Min-Kook Suh and Seung-Woo Seo. "Long-Tailed Recognition by Mutual Information Maximization between Latent Features and Ground-Truth Labels". *International Conference on Machine Learning (ICML)*.
- Chan Kim, Jaekyung Cho, Christophe Bobda, Seung-Woo Seo, and Seong-Woo Kim. "SeRO: Self-Supervised Reinforcement Learning for Recovery from Out-of-Distribution Situations". *International Joint Conference on Artificial Intelligence(IJCAI), Macau*.
- Dongwook Yang and Seung-Woo Seo. "Discrete Wavelet Transform Meets Transformer: Unleashing the Full Potential of the Transformer for Visual Recognition". *IEEE Access*.
- Min-Kook Suh and Seung-Woo Seo. "Aggregation of Masked Outputs for Improving Accuracy–Cost Trade-off in Semantic Segmentation". *IEEE Access*.

**2022**

- Dongwook Yang and Seung-Woo Seo. "AFF-CAM: Adaptive Frequency Filtering based Channel Attention Module". *Asian Conference on Computer Vision (ACCV)*.
- Younghwa Jung, Seung-Woo Seo, and Seong-Woo Kim. "Fast Point Clouds Upsampling with Uncertainty Quantification for Autonomous Vehicles". *International Conference on Robotics and Automation (ICRA)*.
- Se-Wook Yoo and Seung-Woo Seo. "Learning Multi-Task Transferable Rewards via Variational Inverse Reinforcement Learning". *International Conference on Robotics and Automation (ICRA)*.
- Se-Wook Yoo, Chan Kim, Jinwoo Choi, Seong-Woo Kim, Seung-Woo Seo. "GIN: Graph-based Interaction-aware Constraint Policy Optimization for Autonomous Driving". *IEEE Robotics and Automation Letter (RA-L)*.
- Chan Kim, Jae-Kyung Cho, Hyung-Suk Yoon, Seung-Woo Seo and Seong-Woo Kim. "UNICON: Uncertainty-Conditioned Policy for Robust Behavior in Unfamiliar Scenarios". *IEEE Robotics and Automation Letters (RA-L)*.
- Yurim Jeon. Seung-Woo Seo. "EFGHNet: A Versatile Image-to-Point Cloud Registration Network for Extreme Outdoor Environment". *IEEE Robotics and Automation Letters (RA-L)*.
- Soomok Lee, Seung-Woo Seo. "Fail-Safe Multi-Modal Localization Framework Using Heterogeneous Map-Matching Sources". *IEEE Transactions on Intelligent Transportation Systems*.

**2021**

- Chan Kim, Hyung-Suk Yoon, Seung-Woo Seo, and Seong-Woo Kim. "STFP: Simultaneous Traffic scene Forecasting and Planning for Autonomous Driving". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Hyung-Suk Yoon, Chan Kim, Seong-Woo Kim, and Seung-Woo Seo. "Self-Balancing Online Dataset for Incremental Driving Intelligence". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Younghwa Jung, Mingu Jeon, Chan Kim, Seung-Woo Seo, and Seong-Woo Kim. "Uncertainty-Aware Fast Curb Detection Using Convolutional Networks in Point Clouds". *IEEE International Conference on Robotics and Automation (ICRA)*.
- Yurim Jeon, Hwichang Kim and Seung-Woo Seo. "ABCD: Attentive Bilateral Convolutional Network for Robust Depth Completion". *IEEE Robotics and Automation Letters*.

## 수상

2021년 10월 22일–2026년 10월 22일 범위의 Notice에 게시된 수상이다. 날짜는 게시일이다.[^notice1]

- 2024-10-24 · IROS 2024 Earth Rover Challenge 우승

## 소식

2021년 10월 22일–2026년 10월 22일 범위의 Notice 1·2쪽에 게시된 논문 게재 승인·학회 채택 소식 21건이다. 날짜는 게시일이다.[^notice1][^notice2]

- 2025-03-06 · 영상의 영역을 종류별로 나누는 연구 논문: IEEE Robotics and Automation Letters 게재 승인
- 2025-02-07 · 강화학습 논문: ICLR 2025 채택
- 2025-02-07 · 로봇 항법 논문: ICRA 2025 채택
- 2024-11-25 · 공간의 점 자료를 이용한 주행 가능성 추정 논문: IEEE Robotics and Automation Letters 게재 승인
- 2024-10-21 · 공간의 점 자료 분석 논문: IEEE Access 게재 승인
- 2024-09-10 · 계층적 강화학습 논문: IEEE Transactions on Intelligent Transportation Systems 게재 승인
- 2024-08-19 · 라이다를 이용한 위치 추정 논문: IEEE Robotics and Automation Letters 게재 승인
- 2024-03-26 · 주행 가능성을 고려한 경로 계획·제어 논문: IEEE Robotics and Automation Letters 게재 승인
- 2024-03-26 · 스스로 학습 근거를 만드는 주행 가능성 추정 논문: ICRA 2024 채택
- 2024-03-04 · 스스로 학습 근거를 만드는 강화학습 논문: IEEE Robotics and Automation Letters 게재 승인
- 2023-05-03 · 별도의 정답 행동 표시 없이 행동 묶음을 발견하는 연구 논문: ICML 2023 채택
- 2023-05-03 · 종류별 자료 수가 치우친 인식 과제 논문: ICML 2023 채택
- 2023-05-03 · 영상의 영역을 종류별로 나누는 연구 논문: IEEE Access 게재 승인
- 2023-04-20 · 강화학습 논문: IJCAI 2023 채택
- 2022-12-01 · 행동 방법 최적화 논문: IEEE Robotics and Automation Letters 게재 승인
- 2022-09-28 · 영상에서 주목할 정보를 고르는 계산 부분 논문: ACCV 2022 채택
- 2022-06-28 · 행동 계획 논문: IEEE Robotics and Automation Letters 게재 승인
- 2022-06-28 · 영상과 공간의 점 자료 사이의 대응 논문: IEEE Robotics and Automation Letters 게재 승인
- 2022-05-06 · 여러 종류의 정보를 이용한 위치 추정 논문: IEEE Transactions on Intelligent Transportation Systems 게재 승인
- 2022-02-03 · 공간의 점 자료를 늘리는 연구 논문: ICRA 2022 채택
- 2022-02-03 · 여러 단계의 행동을 시범에서 배우는 계층적 모방학습 논문: ICRA 2022 채택

## 연락과 위치

- 교수 사무실: 서울대학교 132동 405호[^faculty][^prof]
- 교수 전화: 02-880-8418[^prof]
- 교수 이메일: sseo@snu.ac.kr[^faculty]
- 학과 연구실 소개의 연구실 전화: 02-880-8438[^lab]
[^home]: Vehicle Intelligence Lab 첫 화면. <http://vi.snu.ac.kr> 2026-10-27 관측.
[^faculty]: 연구실 Faculty의 Prof. Seung-Woo Seo 소개. <http://svil.dsso.ai.kr/sub2_1.php> 2026-10-27 관측.
[^prof]: 서울대학교 전기·정보공학부, 서승우 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p022> 2026-10-27 관측.
[^lab]: 서울대학교 전기·정보공학부, 지능형자동차 연구실 소개. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=48&md=view> 2026-10-27 관측.
[^phd]: Ph.D Candidates. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub2_2> 2026-10-27 관측.
[^ms]: M.S Candidates. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub2_3> 2026-10-27 관측.
[^alumni]: Alumni. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub2_4> 2026-10-27 관측.
[^pubs]: Publications Current (2015~). <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub3_1> 2026-10-27 관측.
[^notice1]: Notice 1쪽. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub4_1> 2026-10-27 관측.
[^notice2]: Notice 2쪽. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub4_1&page=2> 2026-10-27 관측.
[^r1]: Camera Object Detection and Tracking for autonomous driving. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=1> 2026-10-27 관측.
[^r2]: LiDAR Object Detection and Tracking for autonomous driving. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=2> 2026-10-27 관측.
[^r3]: Mapping and Localization for autonomous driving. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=3> 2026-10-27 관측.
[^r4]: Safety-Guaranteed Autonomous Driving with Artificial Intelligence (AI). <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=4> 2026-10-27 관측.
[^r5]: Multi-Task Reinforcement Learning. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=5> 2026-10-27 관측.
[^r6]: Planning with safe Control. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=6> 2026-10-27 관측.
[^r7]: SNUVI experiment in K-CITY. <http://svil.dsso.ai.kr/bbs/board.php?bo_table=sub1_1&wr_id=7> 2026-10-27 관측.
[^p1]: E.-I. Son, J.-T. Kim, S.-W. Seo, Computer Vision ECCV 2026 17051, 433-450 (2026). <https://doi.org/10.1007/978-3-032-37356-4_24> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2606.26839>.
[^p2]: S.-W. Yoo, E. I. Son, S.-W. Seo, IEEE Robotics and Automation Letter (RA-L) (2024). <https://doi.org/10.1109/LRA.2024.3387042> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2404.03274>.
[^p3]: Y. Jeon, E. I. Son, S.-W. Seo, International Conference on Robotics and Automation (ICRA) (2024). <https://arxiv.org/abs/2402.15363> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2402.15363>.
[^p4]: S.-W. Yoo 외, S.-W. Seo, IEEE Robotics and Automation Letter (RA-L) (2022). <https://doi.org/10.1109/LRA.2022.3227862> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2206.01488>.
[^p5]: J. Choi, S.-H. Lee, S.-W. Seo, International Conference on Machine Learning (ICML) (2026). <https://arxiv.org/abs/2602.03389> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.03389>.
[^p6]: S.-H. Lee, S.-W. Seo, Proceedings of the 40th International Conference on Machine Learning 202, 19185-19199 (2023). <https://proceedings.mlr.press/v202/lee23r.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/lee23r.html>.
[^p7]: C. Kim 외, S.-W. Kim, International Joint Conference on Artificial Intelligence(IJCAI), Macau (2023). <https://doi.org/10.24963/ijcai.2023/432> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2311.03651>.
[^p8]: M.-K. Suh, S.-W. Seo, Proceedings of the 40th International Conference on Machine Learning 202, 32770-32782 (2023). <https://proceedings.mlr.press/v202/suh23a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v202/suh23a.html>.

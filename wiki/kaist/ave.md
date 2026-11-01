# AVE 연구실 (Autonomous Vehicles and Embedded systems)

**KAIST 조천식모빌리티대학원·안보과학기술대학원 · 공승현 부교수**

- 분야: 자율주행 인지, 학습 기반 주행 제어, 차량용 인공지능, 위치 추정[^prof][^e2e][^pos]
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 자율주행[^e2e][^p1], 3차원 복원·인식[^p1][^p2], 강화학습[^e2e], 멀티모달 AI[^p2][^e2e], 엣지 컴퓨팅·엣지 AI[^emb], 위성항법(GNSS)[^pos], 데이터 중심 AI·데이터 효율 학습[^p4][^p5]
- 홈페이지: <https://ave.kaist.ac.kr/>
- 근거와 출처: [AVE 연구실 근거](ave-sources.md)
- 자료 기준: 구성원 2026년 10월 31일, 누리집 2026년 10월 31일–11월 1일, 최근 성과 2021년 10월 13일–2026년 10월 13일[^members][^ij][^news]

> 레이더·라이다·카메라로 차량 주변을 알아보고, 경험에서 운전 방법을 배우며, 차량 안에서 동작할 인공지능과 정확한 위치 추정 기술을 연구하는 연구실이다.

## 무엇을 연구하나

AVE 연구실은 자율주행차가 주변을 인식하고 운전 행동을 정하는 데 필요한 인공지능을 개발한다. 레이더(전파로 대상의 위치와 움직임 등을 알아보는 장치), 라이다(LiDAR, Light Detection and Ranging, 빛으로 대상까지의 거리와 형태를 측정하는 장치), 카메라의 관측을 다루며, 센서 융합(여러 측정 자료를 결합해 대상이나 환경의 상태를 알아내는 방법)을 연구한다. 레이더 자료로 도로 위 물체를 찾는 것뿐 아니라 차가 갈 수 있는 영역과 공간의 점유 상태를 알아보는 것도 연구 대상이다.[^perception][^p1][^p2]

주요 기반 중 하나는 4D 레이더 자료다. 여기서 네 축은 거리, 수평 방향, 수직 방향과 상대 운동에 따른 신호 변화에 해당한다. K-Radar는 여러 도로와 안개·비·눈 환경에서 얻은 레이더 자료에 물체의 위치와 크기를 표시한 정답을 함께 제공한다. 레이더 자료를 여러 축으로 배열한 텐서 형태로 다루고, 라이다와 카메라의 관측도 함께 제공해 인식 방법을 비교할 수 있게 했다.[^p1]

운전 행동은 종단간 학습(입력에서 최종 출력까지 이어지는 처리를 함께 학습하는 방식)으로 다룬다. 연구실은 전문가의 시연을 따라 배우는 모방학습과, 행동 결과에 주어진 보상을 바탕으로 행동을 배우는 강화학습을 결합해 관측에서 차량 제어로 이어지는 주행 정책을 개발한다. 영상·언어·행동을 연결하는 모형으로 장면 이해, 원인에 관한 추론과 경로 생성을 함께 연구한다.[^e2e]

실제 기기에서 인식을 실행하는 방법도 연구한다. 임베디드 인공지능(기기 안에서 특정 기능을 수행하는 인공지능)의 계산량과 에너지 사용을 줄이고, 지식 증류(학습한 모형의 정보를 다른 모형의 학습에 전달하는 방법), 경량 신경망과 스파이킹 신경망(시간에 따른 불연속 신호로 정보를 주고받는 신경망)을 다룬다. SpikingRTNH는 레이더 물체 검출에 이러한 신경망을 적용한 사례다.[^emb][^p3]

또 다른 축은 위성항법과 실내외 위치 추정이다. GNSS(Global Navigation Satellite System, 위성 신호로 위치·속도·시각을 구하는 위성항법체계)의 신호 설계와 수신 처리를 연구하고, 신호가 여러 길로 도달하는 다중경로와 직접 도달 경로가 없는 비가시선 상황을 다룬다. 위성 신호를 쓰기 어려운 곳에서는 지도 대응, 여러 주체의 협력 측위와 서로 다른 센서·무선 측정을 결합한다.[^pos]

## 주요 연구 주제

### 1. 레이더 학습 자료와 자동 주석

물체 검출기(자료에서 물체의 종류와 위치를 찾는 모형)를 학습시키려면 센서 관측과 정답 표시가 필요하다. K-Radar는 레이더 학습·평가 자료를 제공하며, 자동 주석 연구는 라이다 관측으로 학습한 검출기가 레이더 학습 자료의 정답을 생성하도록 한다. 이렇게 만든 정답으로 학습한 레이더 검출기의 성능을 사람이 붙인 정답을 쓴 경우와 비교했다.[^p1][^p5]

### 2. 레이더 처리의 계산·에너지 효율

레이더 텐서에서 얼마만큼의 자료를 남길지에 따라 검출 결과와 메모리 사용이 달라진다. Enhanced K-Radar는 자료 밀도를 바꾸어 이 관계를 살피고, 밀도를 미리 줄인 희소 표현(대부분의 성분이 비어 있거나 영인 자료 표현)을 제시한다. SpikingRTNH는 밀도가 다른 포인트 클라우드(공간상의 점들로 대상을 나타낸 자료)를 순차적으로 처리하는 신경망을 제안하고 에너지 소비와 검출 성능을 평가했다.[^p4][^p3]

### 3. 센서 고장에 대응하는 융합과 차선 검출

카메라·라이다·레이더 가운데 일부 센서의 성능이 저하되거나 고장 나면 인식 방법도 이에 대응해야 한다. ASF(Availability-aware Sensor Fusion, 센서의 사용 가능 상태를 고려하는 융합)는 센서별 특징을 공통 공간으로 옮기고 서로의 정보를 참조하도록 해 이런 상황의 물체 검출을 다룬다. 라이다 차선 검출 연구는 먼저 차선 후보를 구한 뒤 주변 특징의 관계를 이용해 후보를 보정하며, 차선 일부가 가려진 상황도 평가한다.[^p2][^p6]

### 4. 학습 기반 운전과 위치·항법 신호

연구실은 모방학습과 강화학습을 이용해 관측에서 차량의 조작으로 이어지는 정책을 개발하며, 시뮬레이션(모형으로 대상이나 상황의 동작을 재현하는 계산)에서 주행을 반복해 평가한다. 위치 추정 쪽에서는 위성항법 신호의 획득·추적, 위성 신호의 보강·지원 체계와 실내외 연속 측위를 연구한다. 합성개구레이더(SAR, Synthetic Aperture Radar, 이동하면서 얻은 레이더 관측을 결합해 영상을 만드는 방식)의 전파 간섭 억제와 영상의 초점 보정도 연구 분야로 소개한다.[^e2e][^pos]

## 대표 논문

공승현이 저자로 참여한 최근 논문 중 데이터 구축, 인식 방법과 계산 효율을 보여 주는 6편이다. 「쉽게 말하면」은 각 논문의 초록을 근거로 썼다. arXiv 판은 해당 등록본의 서지로 표시했다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수 참여 |
|---|---|---|---|---|
| 1 | 2022 | [K-Radar: 4D Radar Object Detection for Autonomous Driving in Various Weather Conditions](https://proceedings.neurips.cc/paper_files/paper/2022/hash/185fdf627eaae2abab36205dcd19b817-Abstract-Datasets_and_Benchmarks.html) · NeurIPS 2022 | 안개·비·눈과 여러 도로 조건에서 얻은 4D 레이더 자료에 도로 위 물체의 입체 위치·크기 정답을 붙인 K-Radar를 공개했다. 라이다·카메라 등의 관측과 기준 검출 신경망도 제공하고, 높이 정보가 입체 물체 검출에 중요함을 보였다.[^p1] | 전체 저자 목록에 기재 |
| 2 | 2025 | [Availability-aware Sensor Fusion via Unified Canonical Space](https://proceedings.neurips.cc/paper_files/paper/2025/hash/80bd5c815cdb033ac23eb27605adaaba-Abstract-Conference.html) · NeurIPS 2025 | 카메라·라이다·레이더가 항상 정상 작동한다고 가정하지 않는 센서 융합 방법을 제안했다. 각 센서의 특징을 공통 공간으로 옮기고 센서 사이의 정보를 참조하게 해, 악천후와 센서 성능 저하·고장 조건에서 물체 검출을 평가했다.[^p2] | 전체 저자 목록에 기재 |
| 3 | 2025 | [SpikingRTNH: Spiking Neural Network for 4D Radar Object Detection](https://arxiv.org/abs/2502.00074) · arXiv 판 | 4D 레이더의 물체 검출에 스파이킹 신경망을 적용했다. 시간에 따라 신호를 내는 계산 단위를 사용하고, 밀도가 높은 점 자료에서 낮은 점 자료 순서로 처리하는 방법을 제안해 검출 성능과 에너지 소비를 평가했다.[^p3] | 전체 저자 목록에 기재 |
| 4 | 2023 | [Enhanced K-Radar: Optimal Density Reduction to Improve Detection Performance and Accessibility of 4D Radar Tensor-based Object Detection](https://arxiv.org/abs/2303.06342) · arXiv 판 | 레이더 텐서에서 남기는 자료의 비율을 바꾸어 물체 검출 성능과 메모리 소비의 관계를 조사했다. 자료 밀도를 미리 줄여 저장하는 표현과 학습용 도구도 제시해 자료 크기와 학습 시간을 다뤘다.[^p4] | 전체 저자 목록에 기재 |
| 5 | 2024 | [Efficient 4D Radar Data Auto-labeling Method using LiDAR-based Object Detection Network](https://arxiv.org/abs/2407.04709) · arXiv 판 | 레이더 자료에 사람이 직접 정답을 붙이는 작업을 줄이려고, 라이다로 학습한 검출기가 레이더 학습 자료의 정답을 자동 생성하게 했다. 자동 정답으로 학습한 레이더 검출기는 수작업 정답으로 학습한 경우와 비슷한 검출 성능을 보였다.[^p5] | 전체 저자 목록에 기재 |
| 6 | 2022 | [Row-wise LiDAR Lane Detection Network with Lane Correlation Refinement](https://arxiv.org/abs/2210.08745) · arXiv 판 | 라이다 자료에서 차선 후보를 찾은 뒤, 후보 주변 특징 사이의 관계를 이용해 결과를 보정하는 두 단계 모형을 제안했다. K-Lane 자료에서 차선 검출 성능과 계산량을 평가했고, 차선 일부가 가려진 상황에서의 성능도 확인했다.[^p6] | 전체 저자 목록에 기재 |

## 교수와 전문 분야

공승현 부교수는 서강대학교 전자공학 학사, Polytechnic University 전기공학 석사를 거쳐 Stanford University에서 항공우주공학 박사학위를 받았다. 연구실 교수 소개는 KAIST 경력을 2010년부터 현재까지로 적고, 그 전에는 삼성전자 연구원, Nexpilot의 창업자 겸 연구개발 최고기술책임자와 Qualcomm Research Center의 Staff Research Engineer로 근무했다고 적는다.[^prof]

현재 관심 분야는 자율주행을 위한 강화학습, 차량 센서의 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 배우는 기계학습 분야), 위치 추정과 인식을 위한 센서 융합, 도심의 협력 항법이다. 조천식모빌리티대학원은 전임교수 명단에 부교수로 올리고 있으며, 안보과학기술대학원 교수 명단은 소속학과를 조천식모빌리티대학원으로 적고 자율주행·객체인식·강화학습·센서퓨전을 세부 연구 분야로 소개한다.[^prof][^mo][^gst]

대표 논문에서 보이는 전문성은 센서 관측을 학습 자료로 구성하는 기술, 악천후와 센서 이상에 대응하는 입체 인식, 인식 모형의 계산과 에너지 효율이다. 연구 소개의 주행 정책과 위성항법 신호 처리도 이 전문 분야를 구성한다.[^p1][^p2][^p3][^p5][^e2e][^pos] 교수 소개는 IEEE Transactions on Intelligent Transportation Systems의 Associate Editor, IEEE Intelligent Vehicles Symposium 2024의 General Chair 및 Organization Chair 활동도 적는다.[^prof]

## 응용 분야

레이더와 센서 융합 연구는 악천후에서 주변 물체를 알아보는 자율주행을 목표로 한다. 운전 정책 연구는 도로 주행·밀집 교통·장애물 회피를 다루며, 기기 내부의 인공지능 연구는 차량 등에서 인식 처리를 실행하는 데 연결된다. 위치 연구는 위성 신호가 약하거나 닿지 않는 실내외 환경의 연속 측위와 위성 기반 위치·항법·시각 서비스의 지원 체계를 대상으로 한다.[^perception][^e2e][^emb][^pos]

## 구성원

2026년 10월 31일 연구실 Members 페이지의 21명이다. Doctoral Students 구획 8명에는 석박사통합과정 1명이 포함되며, Master’s Students 구획 9명과 Undergraduate Students 구획 4명이 있다. 과정과 연구 관심 분야는 게시 카드의 표기를 기준으로 한다. 「대표 논문 참여」는 위 표의 전체 저자 목록에서 같은 이름을 확인한 경우의 번호다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 이석준 (Seokjun Lee) | 박사과정 | Vehicle Dynamics and Control, Autonomous Driving on the Handling Limits, End-to-End Autonomous Driving | seokjunlee@kaist.ac.kr |  |
| 정우진 (Woo-Jin Jung) | 박사과정 | Radar Technology, Autonomous Vehicle Technology, Human Pose Estimation | woo-jin.jung@kaist.ac.kr |  |
| Sumit Mishra | 박사과정 | Urban Mobility and Smart Transportation, Computer Vision for Perception, Accident Prevention with ADAS | sumitmishra209@kaist.ac.kr |  |
| Neha Sengar | 박사과정 | Mechanistic Interpretability of Vision-Language Models, Vision-based Perception for Autonomous Robots | neha.sengar@kaist.ac.kr |  |
| 정희양 (Hee-Yang Jung) | 박사과정 | SAR Signal Processing, LPI Signal Processing, Simultaneous Localization and Mapping | heeyang@kaist.ac.kr |  |
| 송승현 (Seung-Hyun Song) | 박사과정 | Autonomous Vehicle Technology, Sensor Fusion, Deep Learning | shyun@kaist.ac.kr | 5 |
| 장현서 (Hyun-Seo Jang) | 박사과정 | Mobile Robotics, Vision-Language-Action Models, End-to-End Autonomous Driving |  |  |
| 한승민 (Seung-Min Han) | 석박사통합과정 | Computer Vision, Vision-Language-Action Models, End-to-End Autonomous Driving | seungmin.han@kaist.ac.kr |  |
| Christofel Rio Goenawan | 석사과정 | Autonomous Vehicle Technology, Reinforcement Learning, End-to-End Autonomous Driving |  |  |
| 변웅찬 (Woong-Chan Byun) | 석사과정 | Autonomous Vehicle Technology, Object Detection, Deep Learning | woongchan.byun@kaist.ac.kr |  |
| 김시우 (Siewoo Kim) | 석사과정 | Autonomous Vehicle Technology, Computer Vision, Deep Learning | siewoo.kim@kaist.ac.kr |  |
| Tung Tong | 석사과정 | Autonomous Vehicle Technology, Deep Learning, Sensor Fusion | tungtong@kaist.ac.kr |  |
| 김성준 (Seong-Jun Kim) | 석사과정 | Autonomous Vehicle Technology, Computer Vision & Deep Learning, Optimal Path Planning | sjun328@kaist.ac.kr |  |
| 장준혁 (Joon-Hyuk Jang) | 석사과정 | Vision-Language Models (VLM), Computer Vision, Multi-Object Tracking (MOT) | tnvjwnsgur2@kaist.ac.kr |  |
| 남소현 (So-Hyun Nam) | 석사과정 | Deep Learning, Sensor Fusion, Embedded IoT | sohyun126@kaist.ac.kr |  |
| 임찬빈 (Chan-Bin Lim) | 석사과정 | Autonomous Vehicle Technology, Sensor Fusion, Computer Vision & Deep Learning | chanbin.lim@kaist.ac.kr |  |
| 박주언 (Joo-eon Park) | 석사과정 | End-to-End Autonomous Driving, Vision-Language-Action Models, Diffusion-Based Trajectory | jooeonjohn@kaist.ac.kr |  |
| 강상구 (Sang Gu Kang) | 학부 연구생 | Computer Vision, End-to-End Autonomous Driving, Large Multimodal Models |  |  |
| Nattanan Chinworakij (Mos) | 학부 연구생 |  | nattananchin@kaist.ac.kr |  |
| Thiwat Chatkham (Mickey) | 학부 연구생 |  | thiwat.cha@kaist.ac.kr |  |
| Passavee Losripat (Nett) | 학부 연구생 |  | passavee.losripat@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 31일 Alumni 페이지에 학위별로 게시된 박사 6행과 석사 26행이다. 같은 사람이 두 학위로 나타날 수 있다. 박사 표의 마지막 칸은 학위 논문, 석사 표의 마지막 칸은 대표 논문이며, 진로와 연도는 게시 표기를 따랐다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문·대표 논문 |
|---|---|---|---|
| 최영수 (Youngsoo Choi) | Ph.D (2025) | National Forensic Service | Integrated Study Using Surveillance Cameras for Cross-Validation of ERecorder(EDR) Reliability |
| 백동희 (Donghee Paek) | Ph.D (2025) | Professor at Korea University (Sejong Campus) | 4D Radar-Centric Perception AI with LiDAR and Camera Sensor Fusion for Autonomous Driving in Adverse Weather Conditions |
| 조상재 (Sangjae Cho) | Ph.D (2024) | Agency for Defense Development (ADD) | GNSS and automotive 4D radar signal processing for autonomous vehicle localization |
| 윤석택 (Seok-Taek Yun) | Ph.D (2022) | Professor at Gyeongsang National University | Data-driven in-orbit current and voltage prediction for LEO satellite lithium-ion battery state estimation |
| 최유준 (Yoojune Choi) | Ph.D (2018) | Korea Automotive Technology Institute (KATECH) | Research on driver status monitoring system using ECG sensor based on dry electrode |
| 김빈희 (Binhee Kim) | Ph.D (2015) | Korea Aerospace Industries (KAI) | Fast two-dimensional compressed correlator based acquisition techniques for next-generation GNSS |
| 박수면 (Su-Myeon Park) | M.S. (2026) | Korea Railroad Corporation(KORAIL) |  |
| 이상영 (Sangyeong Lee) | M.S. (2026) |  |  |
| 송승현 (Seung-Hyun Song) | M.S. (2026) | Ph.D. Student at KAIST |  |
| 장해철 (Haecheul Chang) | M.S. (2026) | Hyundai Motor Company |  |
| Batyrbek Mukhatbekov | M.S. (2026) |  |  |
| Wang Jiachen | M.S. (2026) |  |  |
| 정희양 (Hee-Yang Jung) | M.S. (2025) | Ph.D. Student at KAIST |  |
| Adeeb Mohammed Islam | M.S. (2025) | 42dot |  |
| 김정훈 (Jeong-Hoon Kim) | M.S. (2024) | Turing Co., Ltd. | J.-H. Kim, S.-H. Kong, M.-H. Sun, “Vehicle Localization Network using Simultaneous Coarse and Fine Visual Map Matching” in IEEE Conference on Intelligent Transportation Systems (ITSC), 2023 |
| 김동인 (Dong-In Kim) | M.S. (2024) | Hyundai Motor Company | D.-I. Kim, D.-H. Paek, S.-H. Kong, “Bayesian Approximation-Based Trajectory Prediction and Tracking with 4D Radar” in IEEE Intelligent Vehicles Symposium, 2025 |
| 선민혁 (Min-Hyeok Sun) | M.S. (2024) | Hyundai Motor Company | M.-H. Sun, D.-H. Paek and S.-H. Kong, “A Survey of Lane Detection Networks using Various Sensors,” in IEEE Transactions on Intelligent Transportation Systems, 2024 |
| Kevin Tirta Wijaya | M.S. (2023) | Max Planck Institute for Informatics | K. T. Wijaya, D. Paek and S.-H. Kong, “Advanced feature learning on point clouds using multi-resolution features and learnable pooling”, in Remote Sensing, 2024 |
| 백동희 (Donghee Paek) | M.S. (2021) | Ph.D. from KAIST | D.-H. Paek\*, S.-H. Kong\*, and K. T. Wijaya, “K-Radar: 4D radar object detection for autonomous driving in various weather conditions,” Advances in Neural Information Processing Systems, 2022 |
| 정승환 (Seunghwan Chung) | M.S. (2021) | Naver Labs | S.-H. Chung, S.-H. Kong, S. Cho and I. M. A. Nahendra, “Segmented Encoding for Sim2Real of RL-based End-to-End Autonomous Driving,” IEEE Intelligent Vehicles Symposium, 2022 |
| 이남형 (Namhyoung Lee) | M.S. (2020) | Hyundai Motor Company |  |
| 조상재 (Sangjae Cho) | M.S. (2020) | Ph.D. from KAIST | S. Cho, D.-H. Paek, H.-W. Seok, and S.-H. Kong, “BOC-FPDNet: BOC First arrival Path Detection in Multipath Channel for GNSS Positioning” in IEEE Transactions on Intelligent Vehicles, 2024 |
| 김보성 (Boseong Kim) | M.S. (2019) |  |  |
| 고현우 (Hyunwoo Ko) | M.S. (2016) | Agency for Defense Development (ADD) | H. Ko, Y. Shim, and S.-H. Kong, “Realization and Demonstration of Enhanced Korean High-speed Train Navigation System with Noise Filtering Schemes,” International Journal of Control, Automation and Systems, 2018 |
| 백승호 (Seungho Paek) | M.S. (2019) | Hanwha Power Systems |  |
| Hoang Manh Linh | M.S. (2019) | Ph.D. |  |
| 김민준 (Minjun Kim) | M.S. (2019) | Korea Aerospace Research Institute (KARI) |  |
| 전상윤 (Sangyoon Jeon) | M.S. (2016) |  |  |
| 정길섭 (Gilseob Jung) | M.S. (2016) | Hyundai Mobis |  |
| 유경우 (Kyngwoo Yoo) | M.S. (2014) |  |  |
| 설상환 (Sanghwan Seol) | M.S. (2014) | Agency for Defense Development (ADD) |  |
| 한혜현 (Hyehyun Han) | M.S. |  |  |

## 최근 논문 목록 (2021–2026)

레이더·라이다 기반 인식, 학습 기반 주행과 궤적 예측, 위성항법·위성 전지 예측, 교통사고 분석을 다룬다. 국제 학술지 19편, 국제 학회 23편, 국내 학술지 15편, 국내 학회 17편으로 모두 74편이다. 제목·저자·발표처는 연구실 표기이며, 날짜가 적힌 2021년 항목은 10월 13일 이후만 포함한다. 연도와 발표처만 적힌 항목은 「연구실 기재」이고, 저자 뒤 별표와 단검 표시는 누리집 표시다.[^ij][^ic][^dj][^dc]

**2026**

- Seokjun Lee and Seung-Hyun Kong\*. "Learning-based Autonomous Oversteer Control and Collision Avoidance". *IEEE Transactions on Intelligent Vehicles*.
- Dong-Hee Paek and Seung-Hyun Kong\*. "AI for Perception using 4D Radar". *IEEE Intelligent Transportation Systems Magazine*.
- Seung-Hyun Kong\*, Hee-Yang Jung, Dong-Hee Paek, and Woo-Jin Jung. "Hybrid Frequency Estimator of Weak Signals Using Robust Frequency Estimator with SNR Estimation Network-based Selector". *IEEE Sensors Journal*.
- Youngsoo Choi, Jongjin Park, and Seung-Hyun Kong\*. "Integrated Validation Framework for EDR Data Reliability: Application to Korean Traffic Accident Cases". *Forensic Science International: Digital Investigation*.
- Youngsoo Choi, Yongmun Yun, Jongjin Park, Woo-Jeong Jeon, and Seung-Hyun Kong\*. "Robust Video-Based Vehicle Speed Estimation for Occluded Scenes for Forensic Analysis of Traffic Accidents". *Multimedia Tools and Applications*.
- Youngsoo Choi, Jongjin Park, Yongmun Yun, Woo-Jeong Jeon, and Seung-Hyun Kong\*. "Cross-Ratio and Vehicle Dynamics-Based Speed Estimation for Traffic Accident Analysis". *Forensic Science International, vol. 378, article 112675, February 2026*.
- Seung-Hyun Song, Dong-Hee Paek, Minh-Quan Dao, Ezio Malis, and Seung-Hyun Kong\*. "Enhanced 3D Object Detection via Diverse Feature Representations of 4D Radar Tensor". *IEEE Sensors journal, 2025*.
- Woo-Jin Jung, Dong-Hee Paek, and Seung-Hyun Kong\*. "LiDAR-to-4D Radar Synthesis for Building Large-Scale Tensor Datasets". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR-Findings), 2026*.
- Adeeb M. Islam, Dong-Hee Paek, and Seung-Hyun Kong\*. "Structural Knowledge Distillation for Aligning 4D Radar with Vision–Language Models". *IEEE Intelligent Vehicles Symposium (IV), 2026*.
- Batyrbek Mukhatbekov, Dong-Hee Paek, Woo-Jin Jung, and Seung-Hyun Kong\*. "SRF: Stereo-Radar Fusion for 3D Object Detection in Adverse Weather Conditions". *IEEE Intelligent Vehicles Symposium (IV), 2026*.
- Hee-Yang Jung, Dong-Hee Paek, and Seung-Hyun Kong\*. "Open-Source Autonomous Driving Software Platforms: Comparison of Autoware and Apollo". *IEEE Intelligent Vehicles Symposium (IV), 2026*.
- Haechul Chang, Siewoo Kim, Adeeb M. Islam, Seong-Jun Kim, and Seung-Hyun Kong\*. "Event-Aware Relabeling for Addressing Future Leakage in End-to-End Autonomous Driving". *International Conference on Artificial Intelligence in Information and Communication (ICAIIC), 2026*.
- Woong-Chan Byun, Seung-Hyun Song, Chan-Bin Lim, Dong-Hee Paek, and Seung-Hyun Kong\*. "Dashcam-Based Ego-Vehicle Speed Estimation via Lane-Aware Spatiotemporal Learning". *International Conference on Artificial Intelligence in Information and Communication (ICAIIC), 2026*.
- 김시우, 공승현. "Alpamayo의 국내 주행 환경 적응 및 추론 최적화를 통한 실차 적용". *한국자동차공학회 논문집, 2026*.
- 정우진, 백동희, 공승현. "정확도와 실시간성을 고려한 자율주행 인지 시스템용 4D 레이더 전처리 기법". *한국자동차공학회 논문집, 2026*.
- 김성준, 공승현. "EKF기반 다중 궤적 후보와 신경망 융합을 통한 차량 궤적 예측". *Journal of Institute of Control, Robotics and Systems, 2026*.
- 김대용, 공승현. "저조도 환경의 차선 검출 성능 향상을 위한 Task-aware ZeroDCE-CLRNet 프레임워크". *한국ITS학회 논문지, 2026*.
- 한승민, 공승현. "고속 주행 시나리오를 위한 장면-궤적-행동 정렬 기반 실시간 End-to-End 자율주행". *한국ITS학회 논문지, 2026*.
- 정희양, 백동희, 정우진, 공승현. "넓은 SNR 범위에서 SAFE 기반 주파수 추정". *Journal of Positioning, Navigation, and Timing (JPNT), 2026*.
- 변웅찬, 공승현. "DNC-IMM: 주행 맥락 정보 기반 신경망 보정을 통한 조기 차선변경 의도 인식". *한국ITS학회 논문지, 2026*.
- 김시우, 공승현. "SC-IMM 기반 교사 신호를 이용한 End-to-end 자율주행 궤적 출력 안정화". *Journal of Institute of Control, Robotics and Systems, 2026*.
- 임찬빈, 백동희, 공승현. "상태 예측 신경망을 활용한 IMM 기반 다중 객체 추적 기술". *한국자동차공학회 논문집, 2026*.
- 한승민, 공승현. "지식 증류와 경량 어텐션을 이용한 효율적인 자기 지도 기반 단안 깊이 추정". *Journal of Institute of Control, Robotics and Systems, 2026*.
- 임찬빈, 공승현(Seung-Hyun Kong). "시계열 학습을 통한 4D 레이더 기반 인간 자세 추정". *한국ITS학회 춘계학술대회, 2026*.
- 한승민, 공승현(Seung-Hyun Kong). "End-to-end 자율주행 모델의 효율적 비전 토큰 압축 방법". *한국ITS학회 춘계학술대회, 2026*.

**2025**

- Min-Hyeok Sun, Seung-Hyun Kong\*, and Dong-Hee Paek. "A Survey on Deep Learning-Based Lane Detection Algorithms for Camera and LiDAR". *IEEE Transactions on Intelligent Transportation Systems, vol. 26, no. 6, pp. 7319-7342, June 2025*.
- Seung-Hyun Kong. "The 2024 IEEE Intelligent Vehicles Symposium: A Landmark Event in Autonomous Driving and Intelligent Mobility". *IEEE Intelligent Transportation Systems Magazine, vol. 17, no. 4, pp. 122-126, July-August 2025*.
- Kevin Tirta Wijaya, Dong-Hee Paek, and Seung-Hyun Kong\*. "SwiftPCN: Fast, Implementation-Efficient, and Accurate Point Cloud Completion Network with Flexible Output Resolution". *Neurocomputing, vol. 624, article 129387, April 2025*.
- Kevin Tirta Wijaya, Christofel Rio Goenawan, and Seung-Hyun Kong\*. "Enhancing performance of 3D point completion network using consistency loss". *Neurocomputing, vol. 618, article 129037, February 2025*.
- Seung-Hyun Kong\*, Dong-Hee Paek, and Sangyeong Lee. "RTNH+: Enhanced 4D Radar Object Detection Network using Two-Level Preprocessing and Vertical Encoding". *IEEE Transactions on Intelligent Vehicles, vol.10, no.2, pp.1427-1440, February 2025*.
- Haechul Chang, Adeeb Mohammed Islam, Siewoo Kim, Dong-Hee Paek, and Seung-Hyun Kong\*. "Real-Time Closed-Loop E2E Driving: Dataset Refinement and Causal Reasoning in Digital-Twin Evaluation". *International Conference on Control, Automation, and Systems (ICCAS), 2025*.
- Dong-Hee Paek and Seung-Hyun Kong\*. "Availability-aware Sensor Fusion via Unified Canonical Space". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Woong-Chan Byun, Dong-Hee Paek, Seung-Hyun Song, and Seung-Hyun Kong\*. "Efficient On-Chip Implementation of 4D Radar-Based 3D Object Detection on Hailo-8L". *ITS ASIA PACIFIC FORUM, 2025*.
- Woo-Jin Jung, Dong-Hee Paek, and Seung-Hyun Kong\*. "4DR P2T: 4D Radar Tensor Synthesis with Point Clouds". *ITS ASIA PACIFIC FORUM, 2025*.
- Dong-In Kim, Dong-Hee Paek, Seung-Hyun Song, and Seung-Hyun Kong\*. "Bayesian Approximation-Based Trajectory Prediction and Tracking with 4D Radar". *IEEE Intelligent Vehicles Symposium (IV), 2025*.
- Dong-Hee Paek and Seung-Hyun Kong\*. "SpikingRTNH: Spiking Neural Network for 4D Radar Object Detection". *IEEE Intelligent Vehicles Symposium (IV), 2025*.
- 김시우, 장해철, Adeeb Mohammed Islam, 공승현(Seung-Hyun Kong). "데이터 중심 접근법을 통한 End-to-End 자율주행의 신뢰성 강화". *IPNT Conference, November, 2025*.
- 이상영, 백동희, 공승현(Seung-Hyun Kong). "거리–방위각–도플러 기반 적응형 4D 레이더 전처리 기법". *IPNT Conference, November, 2025*.

**2024**

- Christofel Rio Goenawan, Dong-Hee Paek, and Seung-Hyun Kong\*. "See the Unseen: Grid-Wise Drivable Area Detection Dataset and Network Using LiDAR". *Remote Sensing, vol. 16, no. 20, article 3777, October 2024*.
- Kevin Tirta Wijaya, Dong-Hee Paek, and Seung-Hyun Kong\*. "Advanced Feature Learning on Point Clouds using Multi-resolution Features and Learnable Pooling". *Remote Sensing, vol.16, no. 11, article 1835, May 2024*.
- Sangjae Cho, Dong-Hee Paek, Hong-Woo Seok, and Seung-Hyun Kong\*. "BOC-FPDNet: BOC First arrival Path Detection in Multipath Channel for GNSS Positioning". *IEEE Transactions on Intelligent Vehicles, vol. 9, no. 9, pp. 5581-5594, September 2024*.
- Min-Hyeok Sun, Dong-Hee Paek, Seung-Hyun Song, and Seung-Hyun Kong\*. "Efficient 4D Radar Data Auto-labeling Method using LiDAR-based Object Detection Network". *IEEE Intelligent Vehicles Symposium (IV), 2024*.
- 정우진, 백동희, 공승현(Seung-Hyun Kong). "IMM 필터를 활용한 4D 레이다와 라이다 센서 융합 기반 3D 객체 추적 기술". *IPNT Conference, November, 2024*.
- 정희양, 백동희, 공승현(Seung-Hyun Kong). "딥러닝 기반 4D 레이다 오도미트리 추정". *IPNT Conference, November, 2024*.
- Adeeb Mohammed Islam, Seung-Hyun Kong. "Integrating Control Barrier Function and Residual Learning for Safe High-Speed Obstacle Avoidance in Autonomous Vehicle". *KSAE Spring Conference, June, 2024*.
- 송승현, 백동희, 공승현(Seung-Hyun Kong). "Joint Detection and Tracking 기반 4D 레이다 3D 다중 객체 추적". *KSAE Spring Conference, June, 2024*.
- 장해철, 공승현(Seung-Hyun Kong). "다중 고속 차량 추월을 위한 MPC 기반 경로 계획 및 제어 알고리즘". *KSAE Spring Conference, June, 2024*.

**2023**

- Seung-Hyun Kong\*, Sangjae Cho, Taeseon Kim, and Sanguk Lee. "Stepped-Frequency Binary Offset Carrier Modulation for Global Navigation Satellite Systems". *IEEE Transactions on Aerospace and Electronic Systems, vol. 59, no. 3, pp. 2733-2751, June 2023*.
- Sangjae Cho, Hong-Woo Seok, and Seung-Hyun Kong\*. "Performance Analysis of GNSS Signal Based on SFBOC Modulation". *The Institute of Navigation Global Navigation Satellite System conference (ION GNSS+), 2023*.
- Youngsoo Choi, Yongmun Yun, Woo-Jeong Jeon, and Seung-Hyun Kong\*. "A Novel Approach for Estimating Vehicle Speed in Nighttime Traffic Accidents from Daytime Video Information". *IEEE Conference on Intelligent Transportation Systems (ITSC), 2023*.
- Jeong-Hoon Kim, Seung-Hyun Kong\*, and Min-Hyeok Sun. "Vehicle Localization Network using Simultaneous Coarse and Fine Visual Map Matching". *IEEE Conference on Intelligent Transportation Systems (ITSC), 2023*.
- Sangjae Cho, Hong-Woo Seok, and Seung-Hyun Kong\*. "MPCNet: GNSS Multipath Error Compensation Network via Multi-Task Learning". *IEEE Intelligent Vehicles Symposium (IV), 2023*.
- Dong-Hee Paek, Seung-Hyun Kong\*, and Kevin Tirta Wijaya. "Enhanced K-Radar: Optimal Density Reduction to Improve Detection Performance and Accessibility of 4D Radar Tensor-based Object Detection". *IEEE Intelligent Vehicles Symposium (IV), 2023*.
- Hong-Woo Seok, Sangjae Cho, and Seung-Hyun Kong. "A Survey on LEO-PNT Systems". *Journal of Positioning, Navigation, and Timing, vol. 12, no. 3, pp. 323-332, 2023*.
- 석홍우, 조상재, 공승현(Seung-Hyun Kong). "Factor Graph Optimization 기반 단일주파수 Code-PPP 에 관한 연구". *KICS Summer Conference, June, 2023*.

**2022**

- Seung-Hyun Kong†, Sangjae Cho†, and Euiho Kim\*. "GPS First Path Detection Network based on MLP-Mixers". *IEEE Transactions on Wireless Communications, vol. 21, no. 9, pp. 7764-7777, 2022*.
- Seok-Teak Yun and Seung-Hyun Kong\*. "Data-driven In-orbit Current and Voltage prediction using Bi-LSTM for LEO Satellite Lithium-ion Battery SOC estimation". *IEEE Transactions on Aerospace and Electronic Systems, vol. 58, no. 6, pp. 5292-5306, December 2022*.
- Dong-Hee Paek, Seung-Hyun Kong\*, and Kevin Tirta Wijaya. "K-Lane: Lidar Lane Dataset and Benchmark for Urban Roads and Highways". *IEEE/CVF Computer Vision and Pattern Recognition (CVPR) Workshop on Autonomous Driving, 2022*.
- Dong-Hee Paek, Seung-Hyun Kong\*, and Kevin Tirta Wijaya. "K-Radar: 4D Radar Object Detection for Urban Roads and Highways in Various Weather Conditions". *Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks, 2022*.
- Dong-Hee Paek, Kevin Tirta Wijaya, and Seung-Hyun Kong\*. "Row-wise Lidar Lane Detection Network with Lane Correlation Refinement". *IEEE Conference on Intelligent Transportation Systems (ITSC), 2022*.
- Seung-Hwan Chung, Seung-Hyun Kong\*, Sangjae Cho, and I Made Aswin Nahrendra. "Segmented Encoding for Sim2Real of RL-based End-to-End Autonomous Driving". *IEEE Intelligent Vehicles Symposium (IV), 2022*.
- Kevin Tirta Wijaya, Dong-Hee Paek, and Seung-Hyun Kong\*. "Multiview Attention for 3D Object Detection in Lidar Point Cloud". *IEEE International Conference on Artificial Intelligence in Information and Communication (ICAIIC), 2022*.
- Jeong-Hoon Kim, Binhee Kim, and Seung-Hyun Kong. "Low Computational FFT-based Fine Acquisition Technique for BOC Signals". *Journal of Positioning, Navigation, and Timing, v.11, no.1, pp.11-21, 2022*.
- 선민혁, 백동희, 공승현. "자율 주행을 위한 딥러닝 기반 라이다 객체 인식 신경망 연구 분석". *한국자동차공학회논문집 vol. 30, no. 9, pp. 635-647, 2022*.
- Sangjae Cho, Tae Seon Kim, and Seung-Hyun Kong\*. "Time-Division-Multiplexing Tertiary Offset Carrier Modulation for GNSS". *Journal of Positioning, Navigation, and Timing vol. 11, no. 3, pp. 147-156, 2022*.
- 최영수, 공승현. "주행 차량의 엔진음을 이용한 속력 분석". *한국자동차공학회논문집 vol. 30, no. 2, pp. 91-98, 2022*.
- 조상재, 공승현(Seung-Hyun Kong). "다양한 변조 파라미터에 따른 TDMTOC의 성능 평가". *IPNT conference, November 2022*.
- 선민혁, 백동희, 김동인, Kevin Tirta Wijaya, 공승현(Seung-Hyun Kong). "3D 레이더와 RTK를 활용한 주행 차량 Odometry 추정 인공지능 신경망에 관한 연구". *IPNT conference, November 2022*.
- 김정훈, 조상재, 공승현(Seung-Hyun Kong). "가우시안 라벨 스무딩을 활용한 딥러닝 기반 최초 도달 신호 탐지 기술". *IPNT conference, November 2022*.
- 김동인, 백동희, 선민혁, 공승현(Seung-Hyun Kong). "앵커 라인을 활용한 라이다 기반 차선 인식 네트워크". *3rd Korea Artificial Intelligence Conference, September 2022*.
- 김동인, 백동희, 선민혁, Ryan Gallagher, 공승현(Seung-Hyun Kong). "다양한 조도에 강인한 라이다-카메라 센서 융합 기반 차선 인식 네트워크". *3rd Korea Artificial Intelligence Conference, September 2022*.
- 김정훈, 조상재, 공승현(Seung-Hyun Kong). "S-BEV 이미지를 이용한 효율적인 자율 주행". *3rd Korea Artificial Intelligence Conference, September 2022*.

**2021**

- Seok-Teak Yun and Seung-Hyun Kong\*. "Forecasting Methods of Battery Charge and Discharge Current Profile for LEO Satellites". *Electronics, vol. 10, no. 23, article 2999, December 2021*.
- 한승태, 김보성, 조상재, 공승현(Seung-Hyun Kong). "CNN을 이용한 다중 경로 신호 중 최초 도달 신호 탐지 기술". *IPNT conference, November 2021*.

「Learning-based Autonomous Oversteer Control and Collision Avoidance」는 국제 학술지 목록에는 학술지 이름으로, 구성원 페이지에는 「Under Review」로 적혀 있다.[^ij][^members]

## 과제

연구실 Projects 1–3쪽에 게시된 과제 중 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 13건이다. 연도만 적힌 기간은 원래 표기를 따랐으며, 「B2B 마케팅 전문가 교육」의 기간은 「2020/2021」이다. 주관기관과 목표·내용은 연구실이 게시한 설명이다.[^projects][^projects2][^projects3]

- 대규모 융합연구소 (지원 KAIST; 기간 2026. 7. 1 ~ 2028. 12. 31; 랩 설명 본 사업은 GeoAI 기반 첨단 모빌리티 분야를 선도하는 교수진의 연구역량을 결집하여, 차세대 모빌리티 혁신을 위한 대규모 융합연구소를 운영하고 향후 관련 대형 국책과제 유치를 위한 기반을 구축하는 것을 목표로 한다. 본 연구소는 공간 이해 기반 주행, 실내·외 연속 이동, 동적 이동체 대상 효율 통신, 인프라-모빌리티 지능형 협력, 지속적 개선이 가능한 Fleet Learning 등 첨단 모빌리티 핵심 분야를 아우르는 융합 연구 허브로 기능하고자 한다. 이를 통해 분야별 선도 연구역량 간 연계를 강화하고, 국가 차원의 차세대 모빌리티 기술 경쟁력 강화와 후속 대형 국책과제 추진에 기여하고자 한다.)
- 산업혁신인재성장지원 첨단제조융합인재육성지원사업 (지원 산업통상부; 기간 2026.06 ~ 2031.02; 랩 설명 산업계 수요 기반의 산학 프로젝트 수행을 통해 첨단제조 분야의 고급 연구인재를 육성하는 것을 목표로 한다. 본 사업은 대학, 기업 및 관련 기관이 협력하여 산업 현장에서 요구되는 제조 공정 개선, 소재·부품 개발, 첨단 기술 융합 연구 등을 수행하며, 박사후연구원이 프로젝트에 주도적으로 참여하여 독립적인 연구역량과 산업 적용 역량을 강화할 수 있도록 지원한다. 이를 통해 첨단제조 분야의 기술 혁신과 산업계 수요에 부합하는 실무형 연구인재 양성에 기여하고자 한다.)
- 글로벌 C-ITS 시장 진출을 위한 Edge AI 기반 고해상도 4D 이미징 레이더-비전 융합 센서 (지원 중소벤처기업부; 기간 2025.09.01 ~ 2029.08.31; 랩 설명 센서 융합 AI 기반 4D 레이더-비전 인지 센서 및 지능형 교통 분석 플랫폼 개발을 목표로 한다. 이를 위해 ITS용 4D 이미징 레이더 개발 기반 비전, Egde AI 통합 제품화 개발, 데이터 셋 확보 기반 Early Fusion 레이더-비전 퓨전 AI 모델 개발, 그리고 융합 센서 데이터의 모니터링 및 시뮬레이션 SW 플랫폼 개발을 수행한다.)
- 대형트럭 특화 End-to-End AI 기반 무인 자율주행 화물운송 상용화 기술개발 (지원 산업통상부; 기간 2025.07.01 ~ 2027.12.31; 랩 설명 대형트럭의 고속·고중량 주행 특성에 최적화된 Vision 기반 End-to-End 자율주행 기술을 개발하여, 고속도로 구간의 무인 화물운송 상용화를 목표로 한다. 1억km 규모의 실주행 데이터를 활용해 End-to-End 자율주행 신경망과 비전-언어 모델을 고도화하고, 비정상 상황을 인지·판단할 수 있는 인공지능 알고리즘을 개발함으로써, 보다 안전하고 지능적인 대형트럭 자율주행 기술을 구현한다.)
- 레이더 단독 객체 인식 DNN 기술 개발 (지원 (주)현대엔지비; 기간 2024.07.29~2025.08.31; 랩 설명 4D 레이더는 악천후 환경에서도 안정적인 성능을 발휘하는 특성으로 인해, 자율주행자동차의 주요 센서로 주목받고 있다. 본 프로젝트는 자율주행차에 4D 레이더를 적용하기 위한 PoC(Proof of Concept)를 수행하고, 이에 적합한 데이터 전처리 과정과 인식 모델을 탐색·개발하는 것을 목표로 한다.)
- 실주행 4D 레이더 데이터셋 구축 및 전처리 기술 개발 (지원 (주)현대엔지비; 기간 2024.03.25~2025.03.24; 랩 설명 다양한 기상환경(악천후 포함)에서 도로 위 객체 탐지를 위한 대용량 4D 레이다 멀티 모달 데이터셋을 구축하고, 고해상도 4D 레이다 데이터를 위한 새로운 전처리 기술을 개발한다. 데이터셋 구축을 하는 과정에서 시간 및 비용 감축을 위해 Semi-오토라벨링 기술을 추가로 개발한다. (총 2.7억원))
- Global Innovation Network Programme (GINP) : Robotics and Artificial Intelligence (지원 Danish Agency for Higher Education and Science (덴마크 고등교육과학청); 기간 2024.01.01~2025.12.31; 랩 설명 본 프로젝트는 로봇, AI 및 자동화를 중심으로 한국과 덴마크의 연구자들이 교류하며, 새로운 연구 분야를 탐색하고, 사회에 기여할 수 있는 로보틱스 기술을 개발하는 것을 목표로 한다. 제조 산업, 의료 로봇공학, 노인 간호용 로봇 등의 주제를 포함하며, 로봇 시스템의 모델링, 계획 및 제어, 컴퓨터 비전, 인간-로봇 상호 작용, 인공지능을 중심으로 공동 연구를 수행한다.)
- 자율주행을 위한 인공지능 기반의 고급 인지 시스템 개발 (지원 INRIA (프랑스 국립 디지털 과학 기술 연구소); 기간 2023.04.01~2025.12.31; 랩 설명 본 프로젝트는 도심에서 자율주행차의 안전한 운행을 위해 변화하는 환경에서도 강건한 상황 인지 시스템을 개발하는 것을 목표로 한다. 이를 위해, 라이다, 카메라 등의 센서들을 활용하여 주변환경 데이터들을 획득하고 주변 객체의 정확한 상태(위치, 방향, 속도)를 추정하기 위한 센서 융합 연구를 수행한다. 그리고 데이터/인공지능 기반 종단간 인지 기술(AVE Lab 담당)과 모델 기반 인지 기술(수식 모델 기반의 휴리스틱한 알고리즘, INRIA 담당) 기술을 각각 개발하고, 각 기술의 장점을 극대화할 수 있는 하이브리드 인지 기술을 공동으로 연구 및 개발한다.)
- 예상 못한 상황에 빠르게 적응하는 메타-강화학습기반 End-to-end 자율주행 기술 연구 (지원 한국연구재단; 기간 2021.04.01~2026.12.31; 랩 설명 자율주행 자동차가 제어 이상이 발생하는 예상하지 못한 상황(UNS; Unexpected Novel Situation)을 스스로 대처하기 위해, UNS를 탐지하는 인공지능과 UNS에 적절한 주행 정책을 실시간으로 학습 및 주행제어하는 메타 강화학습기반 자율주행 인공지능을 개발한다. (총 20억원))
- 자율주행을 위한 인공지능 기반의 4D 레이다 객체 인식 기술 개발 (지원 과학기술정보통신부; 기간 2021.04.01~2022.12.31; 랩 설명 세계 최초로 4D 이미지 레이다(Radar) 센서에 적용되는 자율주행을 위한 인공지능(AI: Artificial Intelligence) 기반의 객체 인식 기술을 개발하는 것을 목표로 한다. 4륜차와 같이 RCS(Radar cross section; 레이다 반사 면적)가 큰 객체뿐만 아니라, 보행자 및 2륜차와 같이 RCS가 작은 객체를 포함한 도로상의 주요 객체를 모두 인식하는 레이다 인공지능을 개발한다. 또한 대용량 데이터를 확보하여 원활한 연구 진행이 가능하도록, Lidar 인공지능을 레이다 데이터와 연계하여 실시간 라벨링(labeling)된 레이다 데이터를 확보하는 레이다 Auto-Labeling 인공지능을 개발한다. (총 7억원))
- 현실 세계에서 변화하는 상황에 따라 지속적으로 자가 개선하는 인공지능 기술 개발 (지원 과학기술정보통신부; 기간 2020.04.01 ~2023.12.31; 랩 설명 자율주행 인공지능이 학습하지 않은 무경험∙비정상 상황에서도 신뢰도 있는 주행을 하기 위해, 운전자의 주행 방식을 모방하는 모방학습 기반 자율주행 인공지능을 개발하고, 모방학습 결과를 기반으로 학습하지 않은 무경험∙비정상 상황에서 적응하여 적절한 주행 정책을 학습하는 강화학습 기반 종단간 자율주행 인공지능을 개발한다. (총 7억원))
- Constant Envelope Modulation 기법을 위한 다중위성 항법신호 개발 (지원 ETRI 한국전자통신연구원; 기간 2021.06.17~2021.11.30; 랩 설명 한반도를 커버하는 정지궤도 및 지구 동기 경사궤도 위성으로 구성된 지역항법 시스템을 위해 측위 성능과 잡음 환경에서 신호의 성능을 향상시키고, 동시에 constant envelope을 만족하면서 다중신호를 송출할 수 있는 신호 변조 기법을 개발한다.)
- B2B 마케팅 전문가 교육 (자율주행 프로젝트) (지원 LG인화원; 기간 2020/2021; 랩 설명 자율주행 관련 B2B 시장 확대를 위해, B2B 마케팅 전문가들에게 최신 자율주행 트렌드와 실제 자율주행 핵심 요소기술(인지, 위치, 경로 계획, 제어 등)을 교육하고, 자율주행 경진대회를 열어 실제 자율주행 프로세스를 경험해보는 기회를 제공한다.)

## 특허

연구실 Patents 페이지에서 출원일 또는 등록일이 조사 기간에 들어가는 14건이다. 출원번호와 등록번호를 구별했으며, 제목·발명자와 날짜는 연구실 표기다.[^patents]

- (KR) 교통사고 원인 분석을 위한 멀티모달 데이터 기반 엔진 정지 판정 장치 (발명자 공승현, 최영수, 변웅찬; 출원번호 10-2025-0113526; 출원일 August 2025)
- (KR) 불완전한 시연을 이용한 강화 학습 방법 및 시스템 (발명자 이석준, 공승현; 출원번호 10-2025-0071564; 출원일 May 2025)
- (KR) 다중 센서 자동 보정 방법 및 시스템 (발명자 백동희, 공승현; 출원번호 10-2025-0071524; 출원일 May 2025)
- (KR) 센서 융합 시스템 및 방법 (발명자 백동희, 공승현, 정우진; 출원번호 10-2025-0068977; 출원일 May 2025)
- (KR) 레이더 데이터 합성 학습 시스템 및 방법 (발명자 공승현, 백동희, 정우진; 출원번호 10-2025-0012612; 출원일 January 2025)
- (KR) 이산적 시변 주파수를 가지는 가변 이진 오프셋 반송파 변조 방법 및 이를 이용하는 위성항법 신호 생성 장치 (발명자 이상욱, 공승현, 조상재, 김태선, 정승환; 등록번호 10-2696443-0000; 등록일 August 2024)
- (KR) 4차원 레이더의 포인트 클라우드 필터링 방법 및 데이터 처리 장치 (발명자 공승현, 백동희, 한승태; 등록번호 10-2655213-0000; 등록일 April 2024)
- (KR) 4D 레이다의 효과적인 전처리 방법 및 시스템 (발명자 공승현, 백동희; 출원번호 10-2023-0109069; 출원일 August 2023)
- (KR) 무선 주차 데이터베이스를 활용한 자율주차 시스템 및 방법 (발명자 공승현, 배홍상; 출원번호 10-2023-0109070; 출원일 August 2023)
- (US) METHOD FOR FILTERING POINT CLOUD OF FOUR-DIMENSIONAL RADAR AND DATA PROCESSING DEVICE (발명자 공승현, 백동희, 한승태; 출원번호 18574547; 출원일 December 2023)
- (KR) 위성항법 수신기의 초기위치결정 시간 단축 방법 및 이를 위한 항법메시지 구조 (발명자 공승현, 김태선, 이상욱; 출원번호 10-2022-0032303; 출원일 March 2022)
- (US) METHOD FOR MODULATING VARIABLE BINARY OFFSET CARRIER WITH DISCRETE TIME-VARIANT FREQUENCY, AND SATELLITE NAVIGATION SIGNAL GENERATOR USING THE SAME (발명자 공승현, 조상재, 이상욱; 출원번호 17695711; 출원일 March 2022)
- (KR) S-BEV 이미지를 이용한 효율적인 자율 주행 방법 (발명자 공승현, 조상재, 김정훈; 출원번호 10-2022-0148920; 출원일 November 2022)
- (KR) 인공지능에서의 레이더 포인트 클라우드 및 레이더 텐서 융합 방법 및 데이터 처리 방법 및 시스템 (발명자 공승현, 김동인, 선민혁, 백동희; 출원번호 10-2022-0180594; 출원일 December 2022)

## 수상과 선정

News 1–6쪽에 게시된 수상·선정·경진대회 본선 진출 11건이다. 날짜는 소식 목록의 게시일이며, 교수 소개에 대응하는 수상의 연도는 별도로 표시했다.[^news][^news2][^news3][^news4][^news5][^news6][^prof]

- 2026-06-18 · 임찬빈 연구원, ITS 2026에서 우수논문상 수상
- 2026-03-04 · 변웅찬 석사과정, ICAIIC 2026 에서 Excellent Paper Award 수상
- 2025-11-10 · 이상영 석사과정, IPNT 2025 에서 우수논문상 수상
- 2025-10-02 · 2025 현대자동차그룹 자율주행챌린지 2차대회 본선 준우승
- 2025-03-31 · 2025 현대자동차그룹 자율주행챌린지 1차대회 본선 준우승
- 2024-02-14 · 백동희 박사과정 글로벌 리더십 포상 (도전부문) 수상
- 2024-02-13 · AVE 연구실, 2024년도 KAIST Globalization Excellence Lab 선정
- 2024-02-13 · 이석준 석/박사통합과정 항법시스템학회 우수논문상 수상 (연도 2023 (교수 소개))
- 2022-11-15 · 2023 자율주행 자동차 경진대회(현대자동차 주최) 실차 트랙 본선 진출
- 2022-10-26 · 2023 자율주행 자동차 경진대회(현대자동차 주최) 가상 트랙 본선 진출
- 2021-11-18 · 한승태 연구원, 한국인공지능학술대회 2021년도 우수논문상 수상

## 소식

News 1–6쪽 전체에서 2021년 10월 13일–2026년 10월 13일에 게시된 연구 발표·학술 교류 소식 41건이다. 날짜는 목록에 적힌 게시일이다.[^news][^news2][^news3][^news4][^news5][^news6]

- 2026-10-09 · 공승현 교수·백동희 교수, EuMW 2026에서 4D Radar 및 센서 융합 AI 튜토리얼 진행
- 2026-09-02 · KAIST–UPenn–경상국립대학교 공동 세미나 개최
- 2026-09-02 · 공승현 교수, 국회 초청 ‘위치 기술의 오늘과 Geo-Physical AI’ 강연
- 2026-07-02 · AVE 연구실, IV 2026에서 자율주행 소프트웨어 플랫폼 및 센서 융합 AI 연구 발표
- 2026-06-11 · 정우진 박사과정, CVPR Findings 2026에서 포스터 발표
- 2026-04-09 · AVE 연구실, LG이노텍에서 강건한 자율주행 AI 기술 관련 세미나 진행
- 2025-12-13 · 백동희 박사, NeurIPS 2025에서 센서 융합 AI 발표
- 2025-10-17 · AVE 연구실의 KAT팀, 2025 현대자동차그룹 자율주행챌린지 전략 공유회에서 기술 발표
- 2025-10-17 · 공승현 교수, 2025 현대자동차그룹 자율주행챌린지에서 전문가 패널 토의
- 2025-09-22 · AVE 연구실, 한·아세안 국제군수포럼에서 4D 레이더 기반 국방 기술 전시
- 2025-09-16 · 장해철 석사과정, 한국전자기술연구원(KETI)에서 오토웨어(Autoware) 실차 적용 방안 관련 세미나 진행
- 2025-06-26 · 공승현 교수, IEEE IV 2025 에서 전문가 인터뷰
- 2025-06-24 · 공승현 교수, IEEE IV 2025의 IEEE ITS Society 25주년 기념 대담에 연사로 초청
- 2025-06-17 · 공승현 교수, 육군본부 군수참모부 주관 기술 세미나에서 ‘군 특화 군집 주행 기술’ 주제로 초청 강연
- 2025-05-28 · 백동희 박사과정, ICRA 2025 에서 4D 레이다 및 센서퓨전 AI 관련 튜토리얼 진행
- 2025-04-11 · 비트센싱·AVE 연구실·제타모빌리티, 업무협약 체결
- 2024-11-20 · AVE 연구실, 덴마크 로보틱스 연구자들 초청 랩투어 행사 진행
- 2024-09-26 · [보도] 한국 자율주행 오픈소스 플랫폼의 다음 달 출범
- 2024-07-21 · 공승현 교수, 한국오토웨어협회 창립총회에서 한국오토웨어협회 협회장으로 선출
- 2024-06-14 · 한국오토웨어협회, 오토웨어재단과 업무협약 체결
- 2024-06-13 · 백동희 박사과정, IEEE IV 2024에서 4D 레이다 관련 튜토리얼 진행
- 2024-06-13 · 공승현 교수, IEEE IV 2024 성황리에 개최
- 2024-04-22 · 서울로보틱스·AVE 연구실 산학협력연구 미팅 및 서울로보틱스 본사 방문
- 2024-03-05 · INRIA·AVE 연구실 협력연구 두 번째 미팅
- 2023-10-04 · INRIA·AVE 연구실 협력연구 착수 미팅
- 2023-08-29 · 공승현 교수 Autoware Foundation of Korea 설립위원장 선출
- 2023-07-25 · J.Christian Gerdes 교수 (Stanford University) 초청강의
- 2023-07-14 · 한국 Stanford 연구센터·AVE 연구실, 고속 자율주행을 위한 차량 동역학 초청 강의
- 2023-07-14 · 2023 여름방학 학부연구생 자율주행 세미나
- 2023-07-11 · 삼성전자·AVE 연구실 산학협력연구 미팅
- 2023-05-25 · Motional·AVE 연구실 산학협력연구 미팅
- 2023-02-03 · 겨울방학 학부연구생 딥러닝 세미나
- 2023-02-02 · NeurIPS 2022 논문 세미나
- 2022-11-01 · [보도] 카이스트 신문 제510호, 악천후에서도 자율주행을 가능하게 하는 4D 레이더 인공지능 기술
- 2022-10-26 · NeurIPS 2022에 4D 레이더 인공지능 개발 논문 게재
- 2022-08-24 · AVE 연구실, IEEE ITS Magazine 2022년 7·8월호에 소개
- 2022-06-13 · 공승현 교수가 대회장(General Chair)을 맡는 2024년 IEEE IVS 개최 확정
- 2022-04-18 · IEEE CVPR 2022에 라이다 차선 인식 인공지능 개발 논문 게재
- 2022-04-06 · 악천후 환경에서의 자율주행을 위한 4D 레이다 대용량 데이터셋 및 벤치마크 구축
- 2022-02-12 · 랩 고급 딥러닝 및 강화학습 세미나
- 2022-01-21 · 랩 신입생을 위한 기초 강화학습 스터디

## 연락과 위치

- 소속: KAIST 조천식모빌리티대학원, 대전광역시 유성구 문지로 193 문지캠퍼스[^prof]
- 교수 사무실: F412, 전화 +82-42-350-1265, 이메일 skong@kaist.ac.kr[^prof][^mo]
- 연구실 연락: +82-42-350-1285, avelab@kaist.ac.kr[^prof]
[^perception]: 연구실 Perception. <https://ave.kaist.ac.kr/perception/> 관측일 2026-10-31.
[^e2e]: 연구실 End-to-End Autonomous Driving. <https://ave.kaist.ac.kr/e2e/> 관측일 2026-11-01.
[^emb]: 연구실 Embedded System. <https://ave.kaist.ac.kr/embedded-system/> 관측일 2026-11-01.
[^pos]: 연구실 Localization & Geoscience and Remote Sensing. <https://ave.kaist.ac.kr/positioning-system/> 관측일 2026-11-01.
[^prof]: 연구실 Professor. <https://ave.kaist.ac.kr/professor/> 관측일 2026-10-31.
[^members]: 연구실 Members. <https://ave.kaist.ac.kr/members/> 관측일 2026-10-31.
[^alumni]: 연구실 Alumni. <https://ave.kaist.ac.kr/alumni/> 관측일 2026-10-31.
[^ij]: 연구실 International Journals. <https://ave.kaist.ac.kr/international-journals/> 관측일 2026-10-31.
[^ic]: 연구실 International Conferences. <https://ave.kaist.ac.kr/international-conferences/> 관측일 2026-10-31.
[^dj]: 연구실 Domestic Journals. <https://ave.kaist.ac.kr/domestic-journals/> 관측일 2026-10-31.
[^dc]: 연구실 Domestic Conferences. <https://ave.kaist.ac.kr/domestic-conferences/> 관측일 2026-11-01.
[^projects]: 연구실 Projects. <https://ave.kaist.ac.kr/projects/> 관측일 2026-10-31.
[^patents]: 연구실 Patents. <https://ave.kaist.ac.kr/patents/> 관측일 2026-10-31.
[^news]: 연구실 News. <https://ave.kaist.ac.kr/news/> 관측일 2026-10-31.
[^mo]: 조천식모빌리티대학원 교수 명단. <https://mo.kaist.ac.kr/professor/> 관측일 2026-11-01.
[^gst]: 안보과학기술대학원 교수 명단. <https://gst.kaist.ac.kr/member/faculty/> 관측일 2026-11-01.
[^projects2]: 연구실 Projects 2쪽. <https://ave.kaist.ac.kr/projects/page/2/> 관측일 2026-11-01.
[^projects3]: 연구실 Projects 3쪽. <https://ave.kaist.ac.kr/projects/page/3/> 관측일 2026-11-01.
[^news2]: 연구실 News 2쪽. <https://ave.kaist.ac.kr/news/page/2/> 관측일 2026-11-01.
[^news3]: 연구실 News 3쪽. <https://ave.kaist.ac.kr/news/page/3/> 관측일 2026-11-01.
[^news4]: 연구실 News 4쪽. <https://ave.kaist.ac.kr/news/page/4/> 관측일 2026-11-01.
[^news5]: 연구실 News 5쪽. <https://ave.kaist.ac.kr/news/page/5/> 관측일 2026-11-01.
[^news6]: 연구실 News 6쪽. <https://ave.kaist.ac.kr/news/page/6/> 관측일 2026-11-01.
[^p1]: D.-H. Paek, S.-H. KONG, K. T. Wijaya, Advances in Neural Information Processing Systems 35 (2022). <https://doi.org/10.52202/068431-0276> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper_files/paper/2022/hash/185fdf627eaae2abab36205dcd19b817-Abstract-Datasets_and_Benchmarks.html> 관측일 2026-11-01.
[^p2]: D.-H. Paek, S.-H. KONG, Advances in Neural Information Processing Systems 38 (2025). <https://doi.org/10.52202/085713-2986> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper_files/paper/2025/hash/80bd5c815cdb033ac23eb27605adaaba-Abstract-Conference.html> 관측일 2026-11-01.
[^p3]: D.-H. Paek, S.-H. Kong, arXiv (2025). <https://doi.org/10.48550/arXiv.2502.00074> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2502.00074> 관측일 2026-11-01.
[^p4]: D.-H. Paek, S.-H. Kong, K. T. Wijaya, arXiv (2023). <https://doi.org/10.48550/arXiv.2303.06342> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2303.06342> 관측일 2026-11-01.
[^p5]: M.-H. Sun, D.-H. Paek, S.-H. Song, S.-H. Kong, arXiv (2024). <https://doi.org/10.48550/arXiv.2407.04709> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2407.04709> 관측일 2026-11-01.
[^p6]: D.-H. Paek, K. T. Wijaya, S.-H. Kong, arXiv (2022). <https://doi.org/10.48550/arXiv.2210.08745> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2210.08745> 관측일 2026-11-01.

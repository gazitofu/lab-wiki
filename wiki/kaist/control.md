# 제어연구실 (Control Lab, Ctrl Lab)

**KAIST 전기및전자공학부 · 장동의 교수**

- 분야: 드론과 기계 시스템의 기하학적 제어, 다양체 위에서 움직이는 시스템의 상태 추정, 드론 자율 비행, 강화학습과 딥러닝 방법, 의료 시술 로봇·메모리 신호·화학 가스 탐지 응용
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^ee][^p1][^p4], 강화학습[^p4][^p6][^p7], 로봇 항법·SLAM[^p2], 수술·의료 로봇[^p6], 고속 유선 인터페이스[^p7], 과학·공학 AI[^p8], 드론·무인 항공기[^p3], 상태 추정·필터링(데이터 동화)[^p2]
- 홈페이지: <https://control.kaist.ac.kr>
- 근거와 출처: [제어연구실 근거 페이지](control-sources.md)

> 드론과 로봇 같은 기계 시스템이 원하는 대로 움직이고 자기 위치와 자세를 정확히 알도록 하는 제어·추정 이론을 세우고, 강화학습 같은 인공지능 방법을 더해 드론 비행, 혈관 시술용 가이드와이어 조종, 메모리 신호 보정, 화학 가스 분류에 쓰는 연구실이다.[^ee][^p1][^p2][^p4][^p6][^p7][^p8]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 장동의 교수가 이끄는 제어연구실이다. 누리집은 영문 이름을 Control Lab, 줄인 이름을 "Ctrl Lab"으로 적고, 연구실을 인공지능·로봇·드론의 혁신이 매일 만들어지는 곳으로 소개한다.[^home][^ee] 교수 소개는 연구 관심을 AI, 로봇공학, 드론, 제어로 적고,[^prof] 전기및전자공학부 교수 소개는 주요 연구를 제어·로보틱스·기계학습으로 적는다.[^ee] 제어(control)는 시스템이 원하는 대로 움직이도록 측정값을 바탕으로 입력을 정하는 방법을 설계하고 분석하는 분야다.

대표 논문과 최근 논문으로 보면 연구는 세 갈래로 모인다. 첫째는 드론이나 강체 같은 기계 시스템의 상태를 다양체(manifold, 좁은 범위에서는 평평한 공간처럼 다룰 수 있는 굽은 공간) 위에서 다루는 기하학적 제어와 상태 추정이다. 대표 논문 1은 드론의 운동 방정식을 새 주다발 구조로 다시 정리해 요(yaw, 위아래 축을 중심으로 도는 회전) 운동을 나머지 운동과 떼어 놓고, 동적 피드백으로 선형 시스템으로 바꿔 궤적과 제어를 설계하기 쉽게 했다.[^p1] 대표 논문 2는 카메라와 관성 측정 장치로 위치와 자세를 추정하는 시각-관성 주행 거리 측정(VIO)에서, 위치·자세를 다양체나 리 군(Lie group, 회전·이동 같은 연속적인 변환들의 모임)의 원소로 다룰 때 필요한 접다발·리 대수 계산을 안정 임베딩(stable embedding)이라는 수학 이론으로 없앴다.[^p2] 최근 논문 목록에도 다양체 위의 시스템을 유클리드 공간에서 다루는 확장 칼만 필터와 모델 예측 조절, 안정 임베딩을 쓴 무향 칼만 필터와 입자 필터, 강체와 행렬 리 군 위 시스템의 관측기, 피드백 적분기에 관한 논문이 이어진다.[^cr]

둘째는 드론과 로봇이 스스로 날고 움직이게 하는 연구다. 대표 논문 3은 쿼드로터 드론이 표지 없이 실외의 가는 막대에 스스로 내려앉는 시스템을, 대표 논문 4는 기존 조절기에 강화학습(시행착오로 보상을 가장 크게 하는 행동을 배우는 기계학습)의 보정을 더해 바람과 짐 같은 외란 속에서도 드론이 궤적을 견고하게 따라가게 하는 제어 틀을 만들었다.[^p3][^p4] 최근 논문 목록에는 멀티로터의 영상 기반 자율 착륙, 이동 로봇의 주행, 장면 그래프로 물체를 찾아가는 주행, 대형 언어 모델로 하는 작업 계획, 낮은 프레임률 영상의 다중 물체 추적에 관한 논문도 있다.[^cr]

셋째는 강화학습과 딥러닝 방법을 만들고 공학 문제에 쓰는 연구다. 대표 논문 5는 피드백 적분기에서 착안해, 심층 신경망을 직교성 조건 아래에서 효율적이고 안정적으로 학습시키는 최적화 방법을 냈다.[^p5] 응용으로는 심장 혈관 시술에서 가이드와이어를 영상으로 자율 조종하는 심층 강화학습(대표 논문 6), 고속 DRAM 인터페이스의 등화기 설정을 강화학습으로 찾는 방법(대표 논문 7), 적외선 스펙트럼으로 화학 가스를 분류하는 신경망(대표 논문 8)이 있다.[^p6][^p7][^p8] 최근 논문 목록에는 캡슐 내시경의 위치 추정, 레이더 신호원 분류, 리튬이온 전지의 충전 상태 추정에 관한 논문도 있다.[^cr]

## 주요 연구 주제

### 1. 다양체 위에서 움직이는 기계 시스템의 제어와 상태 추정

드론의 추력 방향은 흔히 구면 다양체 S²로 나타내고, VIO 연구들은 위치·자세를 다양체나 리 군의 원소로 나타낸다.[^p1][^p2] 연구실은 이런 구조를 직접 다루는 제어·추정 방법을 만든다.[^p1][^p2] 대표 논문 1은 원점을 뺀 벡터 공간 위에 원 모양의 올이 붙은 주다발을 새로 만들어 드론의 요 운동을 원 위에, 나머지 운동을 기준 공간 위에 두고, 다발 전체를 덮는 두 국소 좌표 표현마다 동적 피드백으로 드론 운동을 요 운동이 분리된 선형 가제어 시스템으로 바꿨다. 이 다발을 쓰면 추력 방향에 쓰던 S²가 필요 없다고 밝힌다.[^p1] 대표 논문 2는 안정 임베딩 이론을 VIO에 적용해, 소형 비행체의 실제 비행 데이터셋 두 개에서 비교한 VIO들보다 위치 궤적 오차와 계산 복잡도 모두 나은 결과를 냈다.[^p2] 대표 논문 5는 다양체 위의 수치 적분법인 피드백 적분기에서 착안해, 스티펠 다양체의 접다발 위에서 정의한 연속시간 동역학계를 오일러 이산화로 계산하는 Feedback Gradient Descent를 제안했다.[^p5] 전기및전자공학부 교수 소개는 교수의 대표업적으로 2016년 논문 「Feedback integrators」(Journal of Nonlinear Science)를 든다.[^ee] 대표 논문 1, 2, 5.

### 2. 드론의 자율 비행과 학습 기반 견고 제어

대표 논문 3은 오래 날아야 하는 무인 임무에서 제자리 비행에 드는 에너지를 줄이려고, 쿼드로터가 표지 없이 허들의 가로 막대에 내려앉는 퍼칭 시스템을 만들었다. 짐벌 카메라, 고도 라이다, ToF 센서를 쓰고, 작은 물체를 잘 잡도록 고친 영상 분할 모델과 상태 기계 제어기를 드론에 실은 컴퓨터(Jetson Orin NX)에서 돌려 실외 비행 시험 6번에서 모두 내려앉았다.[^p3] 대표 논문 4의 NST-RL은 비선형 시스템 툴박스(NST)로 계산한 근사 최적 조절기에 잔차 강화학습의 보정을 더하는 견고 제어 틀이다. 보정은 제어 입력이 양수로 유지되고 기본 조절의 안정성이 지켜지도록 동적 확장을 거쳐 들어가며, Crazyflie 2.1 드론의 궤적 추종 실험에서 바람과 짐 외란 아래 비교 방법들보다 추종이 견고하고 제어가 매끄러웠다.[^p4] 대표 논문 3, 4.

### 3. 강화학습·딥러닝의 공학 응용: 혈관 시술, 메모리 신호, 화학 가스

대표 논문 6은 경피적 관상동맥 중재술(PCI)에서 의사의 방사선 노출을 줄이려고 제안된 보조 로봇의 자율 조종을 다룬다. 영상 기반 가이드와이어 조종을 위한 심층 강화학습 틀에 하위 과제 전략과 도메인 무작위화를 넣어, 모의실험과 팬텀 환경에서 기존 방법보다 나은 성능을 보였다.[^p6] 대표 논문 7은 고속 DRAM 인터페이스에서 결정 궤환 등화기(DFE)의 탭 가중치를 채널 모델 없이 신호 데이터로 직접 최적화하는 심층 강화학습 방법이다.[^p7] 대표 논문 8은 화학작용제를 멀리서 탐지하는 푸리에 변환 적외선(FTIR) 분광의 스펙트럼으로 화학 가스를 분류하는 반지도 오토인코더 신경망을 제안했다.[^p8] 대표 논문 6–8.

## 대표 논문

출판사 등록 서지에서 장동의 교수가 저자로 오른 2021–2026년 논문 가운데 교수가 마지막 저자(대표 논문 1은 단독 저자)이고 초록을 구할 수 있는 논문을 연구 갈래마다 고르게 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [A New Bundle Picture for the Drone](https://doi.org/10.1109/tac.2022.3200982) · IEEE Transactions on Automatic Control | 드론의 운동 방정식을 새 수학 구조로 정리했다. 원점을 뺀 벡터 공간 위에 원(S¹) 모양의 올이 붙은 새 주다발(principal bundle, 기준 공간의 점마다 같은 모양의 공간이 하나씩 붙은 구조)을 만들어, 드론의 요 동역학은 원 위에서, 나머지 동역학은 기준 공간 위에서 움직이게 나타냈다. 다발 전체를 두 국소 자명화(다발의 한 부분을 기준 공간 조각과 원의 곱으로 나타낸 좌표 표현)로 덮고, 각각에서 동적 피드백으로 드론 동역학을 요 동역학이 나머지와 분리된 선형 가제어 시스템(입력을 골라 원하는 상태로 보낼 수 있는 선형 시스템)으로 바꿔 드론의 궤적과 제어를 설계하기 쉽게 했다. 추력 방향을 나타낼 때 흔히 쓰던 다양체 S²는 이 새 다발로 필요 없어졌다.[^p1] | 장동의 단독 저자 |
| 2 | 2024 | [A New Paradigm for Dealing With Manifold Structures in Visual Inertial Odometry by Using Stable Embedding](https://doi.org/10.1109/tcst.2024.3351074) · IEEE Transactions on Control Systems Technology | 시각-관성 주행 거리 측정(VIO)은 관성 측정 장치(IMU)와 카메라로 센서를 실은 기체의 위치와 자세를 추정해, GPS가 닿지 않는 곳에서도 길을 찾게 하는 로봇 기술이다. 최근 VIO는 상태 공간을 다양체나 리 군으로 나타내 정확도와 견고성을 높였고, 그 접다발이나 리 대수 위에서 확장 칼만 필터(EKF)나 무향 칼만 필터(UKF)를 쓴다. 이 논문은 안정 임베딩이라는 수학 이론으로 상태 공간의 다양체 구조를 다뤄 접다발이나 리 대수를 따로 고려할 필요를 없앴다. 소형 비행체(MAV)의 실제 비행 데이터셋 두 개에서 비교한 VIO들보다 위치 궤적 오차와 계산 복잡도가 나았다.[^p2] | 1저자 J.-H. Park, 마지막 저자 장동의 |
| 3 | 2026 | [An Onboard Integrated Perception and Control Framework for Autonomous Quadrotor UAV Perching on Markerless Hurdles](https://doi.org/10.3390/drones10040270) · Drones | 오래 걸리는 무인 임무에서 제자리 비행(호버링)에 드는 에너지를 줄이려고, 쿼드로터 드론이 표지(마커) 없이 스스로 내려앉는(퍼칭) 시스템을 만들고 실외 비행으로 검증했다. 기존 자율 착륙 연구는 주로 평평한 면, 시각 표지가 있는 환경, 특수 하드웨어를 전제해 협조 없는 실외에서 가는 막대 모양 표적에 앉는 경우로 넓히기 어려웠다. 이 시스템은 허들의 가로 막대에 앉도록 단축 짐벌 카메라, 고도 라이다, ToF 센서를 쓰고 인식·후처리·제어를 묶었다. 인식 쪽은 YOLOv12n 기반 분할 모델에 작은 물체를 잡는 고해상도 P2 경로를 더하고 모듈을 압축해 탑재 장치에서 실시간으로 돌게 했고, 허들 전체와 가로 막대를 함께 쓰며 부정 표본(찾는 대상이 아니라고 표시한 학습 예시)을 만들어 오검출을 줄였다. 제어 쪽은 상태 기계 제어기가 중심 좌표·방향·거리 측정값으로 먼 거리 접근과 가까운 거리 정렬을 해냈다. Jetson Orin NX 기반 시스템으로 한 실외 비행 시험 6번에서 모두 퍼칭에 성공했다.[^p3] | 1저자 D. Kim, 마지막 저자 장동의 |
| 4 | 2026 | [NST-RL: Residual Reinforcement Learning With Approximate Optimal Regulation for Robust Drone Control](https://doi.org/10.1109/lra.2026.3729483) · IEEE Robotics and Automation Letters | NST-RL은 잔차 강화학습(기존 제어기의 출력에 학습한 보정값을 더하는 강화학습)과, 비선형 시스템 툴박스(NST)로 계산한 근사 최적 조절기를 묶은 견고 제어 틀이다. 외란을 보상하는 보정은 동적 확장을 거쳐 들어가, 제어 입력이 양수로 유지되고 보정의 고주파 성분이 줄며, 보정이 유한하면 기본 조절이 국소적으로 입력-상태 안정(입력이 유한하면 상태도 유한한 범위에 머무는 성질)을 유지한다. BalancedBuffer는 조절기의 최적 비용을 써서, 잘 작동하는 기본 제어기 아래에서는 데이터에 드물게 담기는 제어 노력이 큰 상태에 학습을 집중시킨다. Crazyflie 2.1 드론의 궤적 추종 실험에서 바람과 짐 외란 아래 기하 제어·적응 제어·기존 잔차 강화학습보다 추종이 견고하고 제어가 매끄러웠다.[^p4] | 1저자 G. Pertin, 마지막 저자 장동의 |
| 5 | 2022 | [Feedback Gradient Descent: Efficient and Stable Optimization with Orthogonality for DNNs](https://doi.org/10.1609/aaai.v36i6.20558) · Proceedings of the AAAI Conference on Artificial Intelligence | 심층 신경망 학습에서 직교성(가중치 벡터들이 서로 수직인 성질)을 거는 최적화가 쓸모 있다고 알려져 있고, 여기에는 계산 효율과 안정성이 모두 중요하다. 기존 방법 가운데 리만 최적화나 엄격한 제약을 쓰는 방법은 안정성만, 느슨한 제약을 쓰는 방법은 효율만 챙길 수 있었다. 이 논문은 스티펠 다양체의 접다발 위 연속시간 동역학계를 단순한 오일러 이산화로 계산해 직교성을 끌어내는 Feedback Gradient Descent(FGD)를 제안했다. 다양체 위의 수치 적분법인 피드백 적분기(Feedback Integrators)에서 착안했다. 이미지 분류 실험에서 기존 최신 방법들보다 정확도·효율·안정성이 고루 나았다.[^p5] | 1저자 F. Bu, 마지막 저자 장동의 |
| 6 | 2025 | [A Robust Deep Reinforcement Learning Framework for Image-Based Autonomous Guidewire Navigation](https://doi.org/10.1109/icra55743.2025.11127741) · ICRA 2025 | 경피적 관상동맥 중재술(PCI)은 환자의 혈관에 카테터나 가이드와이어를 넣는 시술이라 시술 중 의사가 방사선에 노출된다. 이를 줄이려고 보조 로봇이 제안됐고, 최근에는 심층 강화학습으로 완전 자율 조종을 하려는 연구가 이어지지만, 기존 알고리즘은 실제 시술에 가까운 처음 보는 여러 환경에서 한계가 있었다. 이 논문은 영상 기반 가이드와이어 조종을 위한 견고한 심층 강화학습 틀을 제안했다. 복잡한 전체 과제를 국소 지도로 설계한 하위 과제로 나눠 한 에이전트가 풀게 하는 하위 과제 전략과, 혈관 모양·가이드와이어 변형·카메라 설정의 변화를 다루는 도메인 무작위화(학습 환경의 조건을 무작위로 바꿔 가며 학습시키는 기법)를 함께 썼다. 여러 모의실험과 팬텀(사람 몸을 본뜬 실험용 모형) 환경에서 기존 방법보다 나은 성능을 보였다.[^p6] | 1저자 S. Yoo, 마지막 저자 장동의 |
| 7 | 2026 | [Deep Reinforcement Learning-Based DFE Structure Optimization for High-Speed DRAM Signals](https://doi.org/10.1109/tcpmt.2025.3648009) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 고속 DRAM 인터페이스에서 결정 궤환 등화기(DFE, 이미 판정한 이전 신호를 되먹여 그 신호가 남긴 간섭을 빼는 수신 회로)의 탭 가중치를 채널을 따로 모델링하지 않고 데이터로 최적화하는 틀이다. 심층 강화학습과 오토인코더로 얻은 신호 표현을 결합해, Q-러닝 에이전트가 학습된 잠재 특징 위에서 신호 데이터로부터 탭 가중치를 직접 최적화한다. 보상 선택과 수렴 성질에 대한 이론적 보장도 제시했다. 대규모 DRAM 신호 데이터셋 실험에서 아이 다이어그램(신호 파형을 겹쳐 그려 신호 품질을 보는 그림)의 창 면적이 26.1% 넓어져, 베이즈 최적화(11.7%)·정책 최적화(15.5%)와 기존 방법들보다 나았다.[^p7] | 1저자 M. Usama, 마지막 저자 장동의 |
| 8 | 2024 | [Semi-Supervised Autoencoder for Chemical Gas Classification with FTIR Spectrum](https://doi.org/10.3390/s24113601) · Sensors | 화학작용제는 독성이 매우 강해 화학 가스를 빨리 식별하고 대응해야 한다. 푸리에 변환 적외선(FTIR) 분광은 멀리서 물질을 분석할 수 있어, 색과 냄새가 없는 화학작용제를 탐지하는 데 쓰인다. 이 논문은 FTIR 스펙트럼으로 화학 가스를 분류하는 반지도 오토인코더(SSAE) 심층 신경망을 제안했다. 기존 방법과 달리 오토인코더와, 그 잠재 벡터에 붙인 분류기를 함께 학습시켜 분류에 쓸 특징 추출을 강화했다. 실험실에서 모은 FTIR 스펙트럼에서 기존 방법보다 분류 성능이 높았고, 잠재 벡터의 군집 분포가 더 조밀해지는 것이 효과의 바탕이라고 밝혔다. 하이퍼파라미터 최적화를 위한 일관된 실험 환경도 마련했다.[^p8] | 1저자 H.-D. Jang, 마지막 저자 장동의 |

## 교수와 전문 분야

장동의 교수는 KAIST 전기및전자공학부 교수다. 학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Robotics & Control로, 주요 연구를 제어·로보틱스·기계학습으로, 디비전을 Signal division으로 적는다.[^ee] 반도체시스템공학과 교수 명단(연구분야 「컴퓨터, 인공지능 및 소프트웨어」)과 연구실 명단에도 올라 있다.[^sseprof][^sselab]

교수 소개 페이지에 따르면 서울대학교 제어계측공학과에서 학사(1994, 최우등 summa cum laude), 같은 대학 전기공학부에서 석사(1997, 지도교수 In-Joong Ha)를 받았고, 캘리포니아공과대학(Caltech)에서 Jerrold E. Marsden 교수의 지도로 Control & Dynamical Systems 박사학위(2002)를 받았다. 2018–2020년 SIAM Journal on Control and Optimization의 부편집장(Associate editor)을 지냈다.[^prof] 학부 교수 소개는 대표업적으로 2001–2016년 논문 6편을 든다. 제어된 라그랑지안(controlled Lagrangians) 방법 연구(IEEE Transactions on Automatic Control 2001, SIAM Journal on Control and Optimization 2010), 수동성 기반 제어로 기계 시스템을 안정화하는 연구(Regular and Chaotic Dynamics 2014), 피드백 적분기(Journal of Nonlinear Science 2016) 등이다.[^ee] 2018년에는 Anthony L. Caterini와 함께 책 「Deep Neural Networks in a Mathematical Framework」(SpringerBriefs in Computer Science)를 냈다.[^book][^home]

누리집 소식란은 교수가 대통령 경호처 과학경호 자문위원회 위원(드론 분야, 임기 2021.03.22–2022.03.21)과 도로교통공단 자문위원(AI 분야)을 맡았다고 적고, 2020년 한국인공지능학회 학술혁신상 수상과 ICCAS 2024 튜토리얼을 알린다.[^home] IEEE Control Systems 2026년 6월호의 「People in Control」 꼭지에는 「Dong Eui Chang」이라는 제목의 글이 실렸고, 서지는 저자를 교수 한 명으로 적는다.[^mcs]

논문으로 보면 전문 분야는 세 갈래다. 첫째, 다양체와 리 군 위에서 움직이는 기계 시스템의 기하학적 제어와 상태 추정이고, 그 생각을 딥러닝 최적화로 넓힌 연구다(대표 논문 1, 2, 5).[^p1][^p2][^p5] 둘째, 드론의 자율 비행과 강화학습을 더한 견고 제어다(대표 논문 3, 4).[^p3][^p4] 셋째, 강화학습과 딥러닝을 혈관 시술용 가이드와이어 조종, DRAM 신호 등화, 화학 가스 분류에 쓰는 응용 연구다(대표 논문 6–8).[^p6][^p7][^p8]

## 응용 분야

대표 논문들은 GPS가 닿지 않는 곳에서 비행체의 위치·자세 추정(대표 논문 2), 오래 날아야 하는 무인 임무에서 드론의 퍼칭(대표 논문 3), 바람과 짐이 있는 드론 궤적 추종(대표 논문 4), 경피적 관상동맥 중재술의 가이드와이어 자율 조종(대표 논문 6), 고속 DRAM 인터페이스의 신호 무결성(대표 논문 7), 화학작용제 가스 탐지(대표 논문 8)를 실험 대상으로 삼았다.[^p2][^p3][^p4][^p6][^p7][^p8] 누리집 소식란은 2020년 제1회 전장상황에서의 자율비행 기술경진대회에서 팀 K-Drone의 최우수상(방위사업청장상) 수상과, 2019년 Lockheed Martin이 연 AlphaPilot AI Drone Racing Challenge에 연구실 석사과정 학생 두 명이 본선에 나간 일도 적는다.[^home] 졸업생과 이전 구성원 표가 적은 진로에는 Samsung Display, Samsung Electronics, Samsung SDI, SK hynix, Samsung Electro-Mechanics, Hyundai Motors, Xpeng Motors, KakaoBrain, Alibaba, TWINNY, Tweeny, KITECH, KERI와 대학(University of Putra Malaysia, University of Tokyo, University of Oxford)이 있다.[^students]

## 구성원

연구실 누리집 Students & Postdocs 페이지의 현재 구성원 23명이다(박사과정 10, 석사과정 13). 페이지는 이름과 과정만 적는다.[^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. 누리집 소식란과 논문 저자 표기의 Muhammad Usama는 박사과정 Mohammad Usama와 같은 사람으로 보았다.[^home]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Xiaowei Xing | 박사과정 |  |
| Sunju Lee | 박사과정 |  |
| Whimin Kim | 박사과정 |  |
| Mohammad Usama | 박사과정 | 7 |
| Soham Shanbhag | 박사과정 |  |
| Beomjoon Pyun | 박사과정 |  |
| ByungChang Choi | 박사과정 |  |
| Sangbaek Yoo | 박사과정 | 2, 6 |
| Hee Deok Jang | 박사과정 | 7, 8 |
| Jiabao Wang | 박사과정 |  |
| Hojun Kwon | 석사과정 | 6 |
| Seokjoon Kwon | 석사과정 | 8 |
| Donghyun Kim | 석사과정 | 3 |
| Guining Pertin | 석사과정 | 4 |
| The Duong Tran | 석사과정 |  |
| Jihwan Mo | 석사과정 |  |
| Seok Ho Jeong | 석사과정 |  |
| Khairul Makirin | 석사과정 |  |
| Jae Kwon | 석사과정 |  |
| Kyeongdon Lee | 석사과정 |  |
| Geon Park | 석사과정 |  |
| Luong Tran Van | 석사과정 |  |
| Ihyun Park | 석사과정 |  |

## 졸업생과 이전 구성원

Students & Postdocs 페이지 「Past Members」에 실린 34줄이다(Past Post-docs 5줄, Past Graduate Students 29줄). 학위·연도·진로·학위 논문 제목은 페이지 표기 그대로이고, 같은 사람이 두 구역이나 여러 줄에 나오면 줄마다 적었다(JaeHyeon Park은 두 구역에, Hyeong-Geun Yu는 세 줄에 나오며 박사 졸업 연도가 2020과 2021 두 가지로 적혀 있다). University of Waterloo로 적힌 6줄(2010–2017)은 KAIST가 아닌 University of Waterloo에서 학위를 받은 졸업생이어서 현재 KAIST 연구실의 졸업생과 구분해 읽어야 한다. 연도가 없는 KAIST 졸업생 줄도 있다.[^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Nor Mohd Haziq Norsahperi | 박사후연구원 (2024) | professor at the University of Putra Malaysia (UPM) |  |
| JaeHyeon Park | 박사 (2022), 박사후연구원 (2023) | Samsumg Display |  |
| Karmvir S. Phogat | 박사후연구원 (August 2018 -- July 2019) | post-doc at the University of Tokyo |  |
| Fernando Jimenez Alburquerque | 박사후연구원 | Researcher at Oxford University |  |
| Hyeong-Geun Yu | 박사후연구원 (2021) | Samsung Electro-Mechanics |  |
| Assawayut Khunmaturod | 석사 (2024) |  |  |
| Jaehyeok Lee | 석사 (2023) | Samsung Electronics |  |
| Dong Hyun Park | 석사 (2023) | Samsung SDI |  |
| JaeHyeon Park | 박사 (2022), 박사후연구원 (2023) | Samsumg Display |  |
| Adil Aloufi | 석사 (2022) | Instructor at Jubail Industrial College, Saudi Arabia |  |
| Min Kyu Park | 석사 (2022) | SK hynix |  |
| Mengyi Gao | 석사 (2022) | Alibaba |  |
| Jiayao Jia | 석사 (2022) |  |  |
| Sangun Park | 박사 (2021) | Tweeny |  |
| Yong Jin Byeon | 박사 (2021) | Tweeny |  |
| Yongjun Cho | 석사 (2021) |  |  |
| Hyeong-Geun Yu | 박사 (2020) | Samsung Electro-Mechanics |  |
| Fanchen Bu | 석사 (2021) |  | A Novel Optimization Algorithm with Orthogonality for Deep Neural Networks Inspired by Feedback Integrators |
| Changsik Lee | 석사 (2021) | Researcher at KITECH | Model Predictive Control of Drone Systems via Stable Embedding Technique |
| Hyeong-Geun Yu | 박사 (2021) | Post-doc at KAIST | Design of a Normalized Matched Filter for Gas Detection with Hyperspectral Images |
| Xiaowei Xing | 석사 (KAIST, 2020) | PhD student at KAIST | Satellite Attitude Control by Adaptive Dynamic Programming and Stable Embedding Technique |
| Tianqi Wang | 석사 (KAIST, 2020) | Xpeng Motors | Robust Navigatoin for Racing Drones based on Imitation Learning |
| Jae Sung Kim | 박사 (KAIST) | TWINNY | Time-Optimal Cornering Trajectory Planning for Differential- Wheeled Mobile Robots Avoiding Lateral Slip |
| Si Jong Kim | 박사 (KAIST) | KERI | Online Multi-Object Tracking Using Deep Neural Network |
| Jae Hoon Lee | 박사 (KAIST) | TWINNY | Precoder Design for Sensing-Based Spectrum Sharing in Cognitive Radio Networks |
| Wonshick Ko | 석사 (KAIST) | Hyundai Motors | Stable Embedding Technique for Control of Satellite Attitude Represented in Unit Quaternions |
| Mohammad Usama | 석사 (KAIST) | PhD student at KAIST | Towards Robust Neural Networks and Efficient Exploration in Reinforcement Learning |
| Taehwan Kwon | 석사 (KAIST) | Engineer at KakaoBrain | Prioritized Stochastic Memory Management for Enhanced Reinforcement Learning |
| Anthony Caterini | 석사 (University of Waterloo, 2017) | PhD Student at the University of Oxford | A Novel Mathematical Framework for the Analysis Neural Networks |
| Shaun Sawyer | 석사 (University of Waterloo, 2015) |  | Gain-scheduled control of a quadcopter UAV |
| Krishan Rajaratnam | 석사 (University of Waterloo, 2014) (co-supservisioin with Ray McLenaghan) |  | Orthogonal separation of variables of the Hamilton-Jacobi equation on spaces of constant curvature |
| Zhao Jin | 석사 (University of Waterloo, 2012) |  | Application of repetitive control to the lateral motion in a roll-to-roll web system |
| Waiman Ng | 박사 (University of Waterloo, 2011) (co-supervision with George Labah) |  | Energy shaping for systems with two degrees of underactuation |
| Joshua Fletcher | 석사 (University of Waterloo, 2010) |  | Motion planning and observer synthesis for a two-span web roller machine |

## 최근 논문 목록 (2021–2026)

장동의 교수가 저자로 참여한 2021–2026년 학술지 논문 39편, 학회 논문 21편, 책 속 장 2편이다. 저자·제목·학술지·학회 표기는 출판사가 등록한 서지를 따랐다.[^cr]

**2026**

- Guining Pertin, Dong Eui Chang. "NST-RL: Residual Reinforcement Learning With Approximate Optimal Regulation for Robust Drone Control". *IEEE Robotics and Automation Letters*.
- Jihwan Mo, Sangbaek Yoo, Jaesoon Choi, Dong Eui Chang. "Anatomically Accurate 3D Vessel Generation via 3-Phase Chebyshev Curve Diffusion". *Lecture Notes in Computer Science*.
- Muhammad Usama, Dong Eui Chang. "Distributional Reinforcement Learning With Information Bottleneck for Uncertainty-Aware DRAM Equalization". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Donghyun Kim, Dong Eui Chang. "An Onboard Integrated Perception and Control Framework for Autonomous Quadrotor UAV Perching on Markerless Hurdles". *Drones*.
- Beom Joon Pyun, Seung Il Kim, Hyung Jeen Choi, Dong Eui Chang. "An Assessment Standard Research for Vehicle Dynamics Model Verification Based on the Coefficient of Determination". *Transaction of the Korean Society of Automotive Engineers*.
- Seokjoon Kwon, Hee-Deok Jang, Dong Eui Chang. "HSG-ON: Hierarchical Scene Graph-Based Object Navigation". *Sensors*.
- Muhammad Usama, Hee-Deok Jang, Dong Eui Chang. "Deep Reinforcement Learning-Based DFE Structure Optimization for High-Speed DRAM Signals". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Muhammad Usama, Dong Eui Chang. "Multi-Lane Joint DRAM Equalization via Cooperative Multi-Agent Distributional Reinforcement Learning". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Van Luong Tran, Xuan Mai Nguyen, Dong Eui Chang, Si Hong Hoang, Manh Cuong Hoang. "Residual Neural Network for Precise 6-DoF Capsule Endoscope Localization Using Electromagnetic Induction". *IEEE Transactions on Instrumentation and Measurement*.

**2025**

- Soham Shanbhag, Dong Eui Chang. "Angular Velocity and Linear Acceleration Measurement Bias Estimators for the Rigid Body System With Global Exponential Convergence". *International Journal of Robust and Nonlinear Control*.
- Nor Mohd Haziq Norsahperi, Salmiah Ahmad, Siti Fauziah Toha, Mohd Azri Abd Mutalib, Mohamad Ridzwan Ishak, Dong Eui Chang. "Dynamic Analysis on an Aerial Work Platform Using a Hybrid CAD Approach for Satellite Testing Applications". *IIUM Engineering Journal*.
- Soham Shanbhag, Dong Eui Chang. "Globally exponentially convergent observer for systems evolving on matrix Lie groups". *Mathematics and Computers in Simulation*.
- Sangbaek Yoo, Hojun Kwon, Jaesoon Choi, Dong Eui Chang. "A Robust Deep Reinforcement Learning Framework for Image-Based Autonomous Guidewire Navigation". *2025 IEEE International Conference on Robotics and Automation (ICRA)*.
- Seokjoon Kwon, Jae-Hyeon Park, Hee-Deok Jang, CheolLae Roh, Dong Eui Chang. "Large Language Model Based Autonomous Task Planning for Abstract Commands". *2025 IEEE International Conference on Robotics and Automation (ICRA)*.
- Jiabao Wang, Dong Eui Chang. "LoFSORT: Sample Online and Real-time Tracking in Low Frame Rate Scenarios". *2025 IEEE International Conference on Robotics and Automation (ICRA)*.
- Soham Shanbhag, Dong Eui Chang. "Machine learning based state observer for discrete time systems evolving on Lie groups". *Engineering Applications of Artificial Intelligence*.

**2024**

- Dong Hyun ParK, Dong-ho Seo, Jee-hyeon Baek, Won-jin Lee, Dong Eui Chang. "Repeated K-means Clustering Algorithm For Radar Sorting". *Journal of the Korea Institute of Military Science and Technology*.
- Sangbaek Yoo, Jae-Hyeon Park, Dong Eui Chang. "A Two-Step Controller for Vision-Based Autonomous Landing of a Multirotor with a Gimbal Camera". *Drones*.
- Assawayut Khunmaturod, Dong Eui Chang. "Development of a Lunar Rover Simulator with an Interface for Reinforcement Learning". *2024 9th International Conference on Automation, Control and Robotics Engineering (CACRE)*.
- Hee-Deok Jang, Seokjoon Kwon, Hyunwoo Nam, Dong Eui Chang. "Semi-Supervised Autoencoder for Chemical Gas Classification with FTIR Spectrum". *Sensors*.
- Hee-Deok Jang, Seokjoon Kwon, Hyunwoo Nam, Dong Eui Chang. "Chemical Gas Source Localization with Synthetic Time Series Diffusion Data Using Video Vision Transformer". *Applied Sciences*.
- Jae Hyeok Lee, Jae-Hyeon Park, Dong Eui Chang. "FocoTrack: Multi Object Tracking by Focusing On Overlap at Low Frame Rate". *2024 IEEE International Conference on Robotics and Automation (ICRA)*.
- Hee-Deok Jang, Jae-Hyeon Park, Dong Eui Chang. "Particle Filter with Stable Embedding for State Estimation of the Rigid Body Attitude System on the Set of Unit Quaternions". *2024 IEEE International Conference on Robotics and Automation (ICRA)*.
- Jae-Hyeon Park, Sangbaek Yoo, Dong Eui Chang. "A New Paradigm for Dealing With Manifold Structures in Visual Inertial Odometry by Using Stable Embedding". *IEEE Transactions on Control Systems Technology*.
- Seokjoon Kwon, Jae-Hyeon Park, Hee-Deok Jang, Hyunwoo Nam, Dong Eui Chang. "A Sensor Drift Compensation Method with a Masked Autoencoder Module". *Applied Sciences*.

**2023**

- Dong-Hyun Park, Jong-seo Kim, Jae-Hyeon Park, Dong-Eui Chang. "A Deep Learning-based Fault Recovery System for Safe Flight of UAV in the Position Sensor Freezing Situation". *Journal of Institute of Control, Robotics and Systems*.
- Dong Hyun Park, Dong-Ho Seo, Jee-Hyeon Baek, Won-Jin Lee, Dong Eui Chang. "A Novel Batch Streaming Pipeline for Radar Emitter Classification". *Applied Sciences*.
- Muhammad Usama, Dong Eui Chang. "PyEye: An Integrated Approach for Signal Integrity Assessment and Eye Diagram Generation". *2023 IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia)*.
- Hee-Deok Jang, Jae-Hyeon Park, Dong-Eui Chang, Hyun-Soo Seo, Hyunwoo Nam. "Deep Learning Algorithm With Residual Blocks for Chemical Gas Concentration Estimation". *Journal of Institute of Control, Robotics and Systems*.
- Dong Hyun Park, Hee-deok Jang, Dong Eui Chang. "Optimized Network Pruning Method for Li-ion Batteries State-of-charge Estimation on Robot Embedded System". *Journal of Korea Robotics Society*.

**2022**

- Chuanbeibei Shi, Yushu Yu, Yuwei Ma, Dong Eui Chang. "Constrained control for systems on matrix Lie groups with uncertainties". *International Journal of Robust and Nonlinear Control*.
- Soham Shanbhag, Dong Eui Chang. "Globally exponentially convergent observer for the rigid body system on SE(3)". *2022 IEEE 61st Conference on Decision and Control (CDC)*.
- Jae‐Hyeon Park, Dong Eui Chang. "Unscented Kalman filter with stable embedding for simple, accurate, and computationally efficient state estimation of systems on manifolds in Euclidean space". *International Journal of Robust and Nonlinear Control*.
- Mengyi Gaoi, Xiaowei Xing, Dong Eui Chang. "Autonomous Drone Surveillance in a Known Environment Using Reinforcement Learning". *2022 22nd International Conference on Control, Automation and Systems (ICCAS)*.
- Hee-Deok Jang, Jae-Hyeon Park, Hyunwoo Nam, Dong Eui Chang. "Deep neural networks for gas concentration estimation and the effect of hyperparameter optimization on the estimation performance". *2022 22nd International Conference on Control, Automation and Systems (ICCAS)*.
- Jiayao Jia, Xiaowei Xing, Dong Eui Chang. "GRU-Attention based TD3 Network for Mobile Robot Navigation". *2022 22nd International Conference on Control, Automation and Systems (ICCAS)*.
- Jae-Hyeon Park, Soham Shanbhag, Dong Eui Chang. "Model-Free Unsupervised Anomaly Detection of a General Robotic System Using a Stacked LSTM and Its Application to a Fixed-Wing Unmanned Aerial Vehicle". *2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Yongjun Cho, Jae-Hyeon Park, Jaesoon Choi, Dong Eui Chang. "Sim-to-Real Transfer of Image-Based Autonomous Guidewire Navigation Trained by Deep Deterministic Policy Gradient with Behavior Cloning for Fast Learning". *2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Dong Eui Chang, Matthew Perlmutter, Joris Vankerschaver. "Feedback Integrators for Mechanical Systems with Holonomic Constraints". *Sensors*.
- Karmvir Singh Phogat, Dong Eui Chang. "Model Predictive Regulation on Manifolds in Euclidean Space". *Sensors*.
- Fanchen Bu, Dong Eui Chang. "Feedback Gradient Descent: Efficient and Stable Optimization with Orthogonality for DNNs". *Proceedings of the AAAI Conference on Artificial Intelligence*.
- Dong Eui Chang. "A New Bundle Picture for the Drone". *IEEE Transactions on Automatic Control*.
- Yushu Yu, Chuanbeibei Shi, Yuwei Ma, Dong Eui Chang. "Constrained Control for Systems on Lie Groups with Uncertainties via Tube-Based Model Predictive Control on Euclidean Spaces". *Communications in Computer and Information Science*.
- Soham Shanbhag, Dong Eui Chang. "Globally Convergent Observer for the Rigid Body System on SE(3) in Presence of Intermittent Measurements". *IEEE Access*.
- Muhammad Usama, Dong Eui Chang. "Learning Flexible and Fair Data Representations". *IEEE Access*.

**2021**

- Hyeong Geun Yu, Dong Jo Park, Dong Eui Chang, Hyunwoo Nam. "An Effective Baseline Correction Algorithm Using Broad Gaussian Vectors for Chemical Agent Detection with Known Raman Signature Spectra". *Sensors*.
- Sangun Park, Dong Eui Chang. "Multipath Lightweight Deep Network Using Randomly Selected Dilated Convolution". *Sensors*.
- Yongjun Cho, Jae-Hyeon Park, Jaesoon Choi, Dong Eui Chang. "Image Processing Based Autonomous Guidewire Navigation in Percutaneous Coronary Intervention". *2021 IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia)*.
- Soham Shanbhag, Dong Eui Chang. "Real time pose detection of animals using HRNet". *2021 IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia)*.
- Mengyi Gao, Dong Eui Chang. "Autonomous Driving Based on Modified SAC Algorithm through Imitation Learning Pretraining". *2021 21st International Conference on Control, Automation and Systems (ICCAS)*.
- Jae-Hyeon Park, Dong Eui Chang. "Data-driven fault detection and isolation of system with only state measurements and control inputs using neural networks". *2021 21st International Conference on Control, Automation and Systems (ICCAS)*.
- Hyeong-Geun Yu, Whimin Kim, Dong-Jo Park, Dong Eui Chang, Hyunwoo Nam. "Design of a Cooperative Chemical Agent (CA) Detection Algorithm with the Hyperspectral Imaging System". *2021 21st International Conference on Control, Automation and Systems (ICCAS)*.
- Whimin Kim, Dong Eui Chang. "Image-Based Visual Servoing with Backstepping for the Drone". *2021 21st International Conference on Control, Automation and Systems (ICCAS)*.
- Muhammad Usama, Dong Eui Chang. "Learning-Driven Exploration for Reinforcement Learning". *2021 21st International Conference on Control, Automation and Systems (ICCAS)*.
- Xiaowei Xing, Dong Eui Chang. "The Adaptive Dynamic Programming Toolbox". *Sensors*.
- Chang Sik Lee, Hyeong-Geun Yu, Jae-Hyeon Park, Whimin Kim, Dong-Jo Park, Dong Eui Chang, Hyunwoo Nam. "Denoising Autoencoder based Noise Reduction Technique for Raman Spectrometers for Standoff Detection of Chemical Warfare Agents". *Journal of the Korea Institute of Military Science and Technology*.
- Dong Eui Chang. "Globally Exponentially Convergent Continuous Observers for Velocity Bias and State for Invariant Kinematic Systems on Matrix Lie Groups". *IEEE Transactions on Automatic Control*.
- Jae-Hyeon Park, Hyeong-Geun Yu, Chang Sik Lee, Dong Eui Chang, Dong-Jo Park, Hyunwoo Nam, Byeong Hwang Park. "CNN based Raman Spectroscopy Algorithm That is Robust to Noise and Spectral Shift". *Journal of the Korea Institute of Military Science and Technology*.
- Tianqi Wang, Dong Eui Chang. "Robust Navigation for Racing Drones based on Imitation Learning and Modularization". *2021 IEEE International Conference on Robotics and Automation (ICRA)*.
- Jae-Hyeon Park, Karmvir Singh Phogat, Whimin Kim, Dong Eui Chang. "Transversely Stable Extended Kalman Filters for Systems on Manifolds in Euclidean Spaces". *Journal of Dynamic Systems, Measurement, and Control*.
- Hyeong‐Geun Yu, Chang Sik Lee, Dong‐Jo Park, Dong Eui Chang, Hyunwoo Nam. "Design of cooperative matched filter for detection of chemical agents". *Electronics Letters*.
- Jae-Hyeon Park, Hyeong-Geun Yu, Dong-Jo Park, Hyunwoo Nam, Dong Eui Chang. "Dynamic one-shot target detection and classification using a pseudo-Siamese network and its application to Raman spectroscopy". *The Analyst*.

## 소식

누리집 첫 화면 「What's happening in CTRL lab」에서 2022년 이후 항목 7건이다. 항목마다 날짜는 적혀 있지 않고, 문장은 게시된 그대로다.[^home]

- ICRA2025 (3 papers accepted)
- ICCAS 2024 Tutorial by Prof. Dong Eui CHANG
- ICRA2024 (1 paper accepted)
- IEEE Transactions on Automatic Control "A new bundle picture for the drone" by Dong Eui Chang, 2023. In this paper, we study the geometry of the drone dynamics and make use of the celebrated Hopf fibration.
- CDC 2022 (1 paper accepted)
- IROS 2022 (2 papers accepted)
- AAAI 2022 (1 paper accepted)

## 연락과 위치

- 연구실: KAIST LG이노베이션홀(N24) 1109·1110호, (34141) 대전광역시 유성구 대학로 291[^home][^prof][^ee]
- 교수 연구실: 교수 소개 페이지와 반도체시스템공학과 명단은 전기및전자공학부동(E3-2) 6206호로, 전기및전자공학부 교수 소개는 LG이노베이션홀(N24) 1109호로 적는다.[^prof][^sseprof][^ee]
- 전화: 042-350-7440[^prof][^sseprof]
- 교수 이메일: dechang@kaist.ac.kr[^prof][^ee][^sseprof]
- 모집 안내: 누리집은 "Students from EE, ME, CE, and Math are all equally welcome!"이라고 적는다.[^home]
[^p1]: D. E. Chang, IEEE Transactions on Automatic Control, 1-8 (2022). <https://doi.org/10.1109/tac.2022.3200982> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J.-H. Park, S. Yoo, D. E. Chang, IEEE Transactions on Control Systems Technology 32, 1098-1104 (2024). <https://doi.org/10.1109/tcst.2024.3351074> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Kim, D. E. Chang, Drones 10, 270 (온라인 2026-04-08). <https://doi.org/10.3390/drones10040270> 초록 기준.
[^p4]: G. Pertin, D. E. Chang, IEEE Robotics and Automation Letters 11, 12200-12207 (2026). <https://doi.org/10.1109/lra.2026.3729483> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: F. Bu, D. E. Chang, Proceedings of the AAAI Conference on Artificial Intelligence 36, 6106-6114 (온라인 2022-06-28). <https://doi.org/10.1609/aaai.v36i6.20558> 초록 기준.
[^p6]: S. Yoo, H. Kwon, J. Choi, D. E. Chang, 2025 IEEE International Conference on Robotics and Automation (ICRA), 468-474 (2025). <https://doi.org/10.1109/icra55743.2025.11127741> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. Usama, H.-D. Jang, D. E. Chang, IEEE Transactions on Components, Packaging and Manufacturing Technology 16, 378-388 (2026). <https://doi.org/10.1109/tcpmt.2025.3648009> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H.-D. Jang, S. Kwon, H. Nam, D. E. Chang, Sensors 24, 3601 (온라인 2024-06-03). <https://doi.org/10.3390/s24113601> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://control.kaist.ac.kr/> (소개, What's happening in CTRL lab, 2026-10-22 열람)
[^prof]: 같은 누리집 Professor 페이지 <https://control.kaist.ac.kr/Professor> (직위, 연구실 위치, 연락처, 학력, 연구 관심, 부편집장 이력, 2026-10-22 열람)
[^students]: 같은 누리집 Students & Postdocs 페이지 <https://control.kaist.ac.kr/students> (Current Members, Past Members, 2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(장동의) <https://ee.kaist.ac.kr/professor/14315/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-22 열람)
[^sseprof]: KAIST 반도체시스템공학과 교수 명단 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 명단 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^cr]: 2021–2026년 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (저자 확인 기준은 근거 페이지, 2026-10-22 조회)
[^book]: A. L. Caterini, D. E. Chang, Deep Neural Networks in a Mathematical Framework, SpringerBriefs in Computer Science, Springer (2018) 서지(Crossref) <https://doi.org/10.1007/978-3-319-75304-1> (2026-10-22 조회)
[^mcs]: D. E. Chang, "Dong Eui Chang [People in Control]", IEEE Control Systems (2026년 6월호) 서지(Crossref) <https://doi.org/10.1109/mcs.2026.3677909> (2026-10-22 조회)

# 미래도시 로봇연구실 (Urban Robotics Lab, URL)

**KAIST 전기및전자공학부 · 명현 교수**

- 분야: 로봇 자율 이동(위치 추정·지도 작성·경로 계획), 라이다·카메라·관성 센서 융합 SLAM, 다리 로봇 보행 제어와 강화학습, 공간 인공지능·컴퓨터 비전, 벽을 오르는 드론 등 도시 환경 점검 로봇
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 로봇 항법·SLAM[^area][^nav][^p1], 보행·휴머노이드 로봇[^pai][^p6], 강화학습[^pai][^p6], 3차원 복원·인식[^pai][^p2], 컴퓨터 비전[^pai][^p8], 자율주행[^nav][^p8], 다중 로봇 협업·물류 자동화[^nav][^project], 드론·무인 항공기[^p7]
- 홈페이지: <https://urobot.kaist.ac.kr/>
- 근거와 출처: [미래도시 로봇연구실 근거 페이지](urobot-sources.md)

> 스마트 도시의 실제 환경에서 움직이는 로봇 기술을 연구하는 연구실이다. 로봇이 스스로 자기 위치를 알고 지도를 만들며 길을 찾는 자율 이동 기술, 센서 자료로 공간을 이해하는 공간 인공지능, 강화학습으로 배우는 다리 로봇의 보행, 벽을 오르는 드론처럼 도시 시설을 살피는 로봇을 만든다.[^home][^area]

## 무엇을 연구하나

연구실 누리집은 연구실을 스마트 도시를 위한 로봇 기술(Robotics for Smart Cities)을 연구·개발하는 곳으로 소개한다.[^home] Research Area 페이지에 따르면 연구 분야는 로봇의 자율 이동, 공간 인공지능(spatial AI, 센서 자료로 주변 공간의 구조와 그 안의 물체를 알아내는 인공지능), 기계학습, 그리고 점검·감시·제어를 위한 지능형 시스템이며, 복잡한 도시 환경을 알아보고 그 안에서 행동하는 로봇을 만드는 것을 목표로 한다.[^area] 같은 페이지는 연구 방향으로 남이 하지 않는 새로운 일, 한 주제에 10년 넘게 투자하는 깊이, 여러 분야와의 융합, 사회에 기여하고 산업화로 이어질 수 있는 연구를 든다.[^area]

연구는 누리집 Research Area의 세 갈래로 나뉜다. Navigation 갈래는 로봇이 자기 위치를 추정하며 지도를 만드는 SLAM(Simultaneous Localization and Mapping, 동시적 위치 추정 및 지도 작성)과 경로 계획을 다룬다. 라이다(LiDAR, 레이저를 쏘아 주변까지 거리를 재는 센서)·카메라·관성 센서(IMU, 가속도와 회전 속도를 재는 센서)를 함께 쓰는 오도메트리(odometry, 센서 값을 이어 붙여 로봇이 움직인 궤적을 추정하는 방법), 여러 번 나눠 만든 지도를 하나로 합치는 다중 세션 SLAM, 지도의 변화 탐지, 비정형 환경의 경로 계획이 여기에 든다.[^nav] Physical AI 갈래는 신경망으로 영상과 센서 자료에서 장면을 이해하는 연구와 강화학습(reinforcement learning, 시행착오로 보상을 키우는 행동을 배우는 기계학습)으로 다리 로봇의 보행 제어기를 만드는 연구를 묶는다.[^pai] Future Robotics 갈래는 벽을 오르는 드론, 화재에 견디는 드론, 교량 부재의 변위를 재는 구조물 점검 시스템처럼 도시 시설을 살피는 로봇을 다룬다.[^future]

연구는 사족 보행 로봇, 자율주행 자동차, 드론, 수상·수중 로봇 등 여러 로봇 플랫폼의 자율 이동으로 이어진다.[^nav] 누리집 첫 화면은 사족 보행 로봇 DreamWaQ와 벽을 오르는 드론 CAROS-H가 CNN에 소개됐다고 적는다.[^home]

대표 논문으로 보면 연구는 네 갈래다. 첫째, 라이다로 자기 위치를 추정하고 지도를 만들고 고치는 SLAM이다(대표 논문 1, 2, 3).[^p1][^p2][^p3] 둘째, 다닐 수 있는 땅을 가려내고 안전한 경로를 짜는 주행 판단이다(대표 논문 4, 5).[^p4][^p5] 셋째, 강화학습으로 배우는 사족 보행 로봇의 보행이다(대표 논문 6).[^p6] 넷째, 벽을 오르는 드론과 위성 사진으로 차량 위치를 찾는 공간 인공지능이다(대표 논문 7, 8).[^p7][^p8]

## 주요 연구 주제

### 1. 라이다·영상 SLAM과 위치 추정

라이다·관성 오도메트리가 측정이 듬성하거나 한쪽으로 쏠린 퇴화 환경에서도 무너지지 않게 하는 필터를 만들었고,[^p1] 두 시점의 3차원 점 구름 사이 자세를 처음부터 맞추는 전역 정합을 지면 분할로 강건하게 해 라이다 SLAM의 루프 클로징(loop closing, 예전에 지난 곳에 다시 왔음을 알아내 지도의 누적 오차를 바로잡는 단계)에 썼다.[^p2] 공사 현장처럼 구조가 자주 바뀌는 곳에서 지도의 변화를 알아내고 지도를 오래 유지하는 신경망도 내놓았다.[^p3] Navigation 페이지는 이 밖에 시각-관성 오도메트리(VIO, 카메라 영상과 관성 센서로 움직임을 추정하는 방법)의 움직이는 물체 대응, 소실점을 이용한 선 기반 SLAM, 단안 카메라용 파운데이션 모델 기반 키프레임 선택, 여러 로봇의 위치 추정, 지면 분할과 움직이는 물체 제거를 든다.[^nav] 대표 논문 1, 2, 3.

### 2. 주행 가능 영역 인식과 경로 계획

3차원 점 구름을 그래프로 나타내 바퀴로 다닐 수 있는 지면과 그 위의 물체를 함께 나누는 방법을 만들었고,[^p4] 지형의 안정성과 주행 위험을 담은 그래프로 비정형 환경에서 안전하면서 짧은 경로를 짜는 계획기를 내놓았다.[^p5] Navigation 페이지는 잠재 공간(latent space, 신경망이 입력을 압축해 표현한 공간)에서 하는 국소 주행, 제로샷 물체 목표 주행(따로 학습하지 않은 물체를 목표로 찾아가는 주행), 드론의 경로 계획·장애물 회피·움직이는 차량 위 착륙, 다층 커버리지 경로 계획을 든다.[^nav] 대표 논문 4, 5.

### 3. 다리 로봇 보행과 강화학습

로봇이 관절 각도처럼 제 몸에서 재는 고유 감각과 주변을 보는 외부 감각을 함께 써서 계단과 경사를 넘는 사족 보행 제어기를 강화학습으로 만들었다.[^p6] Navigation·Physical AI 페이지는 관성 센서와 관절 엔코더만으로 걷는 사족 보행, 고장 상황을 견디는 보행 제어, 다리 로봇에 단 팔로 관절형 물체를 여는 제어, 기울어지는 로터를 단 드론의 기본 제어기를 강화학습으로 보강하는 연구를 든다.[^nav][^pai] 과제 목록에는 휴머노이드 로봇의 전신 제어와 사족 보행 로봇의 이동 조작 과제가 있다.[^project] 대표 논문 6.

### 4. 도시 시설 점검 로봇과 공간 인공지능

공중에서 자세를 바꿔 벽에 붙고 벽을 오르는 드론을 설계하고 그 제어 방법을 내놓았고,[^p7] 위성 사진과 차량의 카메라·라이다 자료를 비교해 차량의 자세를 추정하는 신경망을 만들었다.[^p8] Future Robotics 페이지는 소형 비행체를 이용한 수직 구조물 점검, 영상으로 교량 부재의 변위를 재는 시스템, 화재에 견디는 드론 FAROS를 든다.[^future] Physical AI 페이지는 이벤트 카메라 영상으로 3차원 장면을 복원하는 가우시안 스플래팅(Gaussian splatting, 3차원 공간을 작은 가우시안 덩어리들의 모임으로 나타내 그리는 방법), 영상 특징점을 빠르게 짝짓는 방법, 화소 단위 장면 이해를 위한 대조 학습, 깊이 보완을 든다.[^pai] 대표 논문 7, 8.

## 대표 논문

명현 교수가 마지막 저자(교신저자 † 표시)인 2021–2026년 학술지·학회 논문 가운데 초록을 확인할 수 있는 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry with Adaptive Schmidt-Kalman Filter and Data Exploitation](https://doi.org/10.1109/lra.2025.3634906) · IEEE Robotics and Automation Letters | 라이다·관성 오도메트리(LIO)는 정확도가 높아 로봇에 널리 쓰이지만, 긴 복도나 높은 고도 비행처럼 라이다 측정이 한쪽으로 쏠리거나 듬성한 퇴화 환경에서는 상태 추정이 잘 정해지지 않아 성능이 떨어진다. 이 연구는 두 모듈로 이 문제를 다루는 LODESTAR를 내놓았다. 퇴화 인식 적응 슈미트-칼만 필터(DA-ASKF)는 슬라이딩 윈도로 과거 상태와 측정을 추가 제약으로 쓰면서, 상태마다 퇴화 정도에 따라 갱신할 상태와 고정할 상태를 나누고, 고정한 상태가 공분산을 통해 갱신할 상태의 기준점 구실을 하게 한다. 퇴화 인식 데이터 활용(DA-DE)은 위치 추정에 기여하는 정도와 야코비 행렬의 조건수를 기준으로 정보가 적은 측정을 덜어 내고 고정 상태의 측정을 골라 쓴다. 여러 퇴화 조건의 실험에서 기존 라이다 기반 오도메트리 방법과 퇴화 인식 모듈보다 정확도와 강건성이 좋았다.[^p1] | 1저자 E. M. Lee, 마지막 저자 명현 (3명) |
| 2 | 2024 | [Quatro++: Robust Global Registration Exploiting Ground Segmentation for Loop Closing in LiDAR SLAM](https://doi.org/10.1177/02783649231207654) · International Journal of Robotics Research | 전역 정합(global registration, 두 시점에서 얻은 3차원 점 구름 사이의 상대 자세를 추정하는 일)은 라이다 SLAM에서 두 문제로 성능이 떨어진다. 회전식 라이다가 얻는 점 구름이 듬성한 희소성 문제와, 이상치 제거 방법이 대응점을 너무 많이 버려 정상 대응점이 셋보다 적게 남는 퇴화 문제다. 두 시점의 자세 차이가 클수록 둘 다 심해진다. 이 연구는 지면 분할(ground segmentation, 점 구름에서 땅에 해당하는 점을 가려내는 일)을 이용하는 강건한 전역 정합 틀 Quatro++를 내놓고, 이를 라이다 SLAM의 루프 클로징 관점에서 다뤘다. 실험에서 최신 전역 정합 방법보다 성공률이 높았고, 지면 분할이 지상 차량에서 성공률을 크게 높였다. 라이다 SLAM의 루프 클로징 모듈에 적용해 루프 제약의 품질이 좋아지고 지도가 더 정밀해짐을 확인했다.[^p2] | 1저자 H. Lim, 마지막 저자 명현 (5명) |
| 3 | 2026 | [Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments](https://doi.org/10.1109/lra.2026.3665079) · IEEE Robotics and Automation Letters | 공사가 한창인 현장이나 배치가 자주 바뀌는 실내처럼 변화가 잦은 곳에서는 가림과 시공간 변화가 많아 이동 로봇이 변화를 알아내기 어렵고, 기존 방법은 변화를 놓치거나 관측이 바뀔 때 지도를 갱신하지 못한다. 이 연구는 온라인 변화 탐지와 장기 지도 유지를 함께 하는 이중 헤드 신경망을 내놓았다. 실제 데이터에서 시간에 따른 구조 차이를 손으로 맞추는 일은 품이 많이 들고 현실적이지 않아서, 다른 장면의 요소를 가져와 구조 변화를 합성하는 데이터 증강 방법으로 대량의 정답 표시 없이 모델을 학습시켰다. 실제 공사 현장과 실내 사무실 실험에서 여러 상황에 잘 일반화되고 지도를 효율적이고 정확하게 갱신했다.[^p3] | 1저자 S. Jang, 마지막 저자 명현 (4명) |
| 4 | 2022 | [TRAVEL: Traversable Ground and Above-Ground Object Segmentation Using Graph Representation of 3D LiDAR Scans](https://doi.org/10.1109/lra.2022.3182096) · IEEE Robotics and Automation Letters | 3차원 점 구름에서 다닐 수 있는 영역과 관심 물체를 알아보는 일은 자율 이동의 핵심 과제다. 지상 차량은 바퀴로 갈 수 있는 지형을 찾고, 안전한 판단을 위해 그 위의 물체를 나눠야 하는데, 지나치게 쪼개거나 덜 쪼개면 판단을 그르칠 수 있다. 이 연구는 점 구름을 그래프로 나타내 주행 가능한 지면 검출과 물체 묶기를 함께 하는 TRAVEL을 내놓았다. 지면은 점 구름을 삼각 격자 하나를 노드로 하는 그래프(tri-grid field)로 바꾼 뒤, 노드를 잇는 에지의 국소적인 볼록·오목을 따져 찾고 다시 정한다. 지면 위 물체는 구면 투영 공간에서 수평으로 이웃한 점 묶음을 노드로, 노드 사이의 수직·수평 관계를 에지로 삼아 실시간으로 나누며 지나친 쪼개짐을 줄인다. 모의실험·도시 장면·자체 데이터셋 실험에서 제안한 지면 분할이 기존 지표로 최신 방법보다 나았고, 새로 제안한 평가 지표가 지면 위 물체 분할을 평가하는 데 의미가 있음을 보였다.[^p4] | 1저자 M. Oh, 마지막 저자 명현 (10명) |
| 5 | 2025 | [TRG-planner: Traversal Risk Graph-Based Path Planning in Unstructured Environments for Safe and Efficient Navigation](https://doi.org/10.1109/lra.2024.3524912) · IEEE Robotics and Automation Letters | 산·동굴·공사 현장·재난 지역 같은 비정형 환경은 지형이 고르지 않아 자율 이동이 어렵고, 위험한 지형을 피하면서 목표에 빠르고 안전하게 가는 경로를 짜는 일이 중요하다. 이 연구는 지형의 기하학적 주행 가능성을 반영한 새 그래프 표현인 주행 위험 그래프(TRG)로 안전하고 거리 효율적인 경로를 짜는 방법을 내놓았다. 노드는 지형의 안정성과 도달 가능성을, 에지는 주행 위험으로 가중한 경로 후보를 나타낸다. TRG는 파면이 퍼지듯 넓혀 가며 만들고 계층적으로 관리해 넓은 환경에서도 실시간으로 계획할 수 있으며, 그래프 최적화 문제로 안전하면서 짧은 경로를 함께 우선한다. 기존 방법보다 안전성·거리 효율·처리 시간이 좋았고, 사족 보행 로봇의 실제 실험으로 검증했다. ICRA 2023의 사족 보행 로봇 챌린지(Quadruped Robot Challenge)에서 우승한 DreamSTEP 팀의 자율 이동 체계에서 전역 경로 계획기로 쓰였다.[^p5] | 1저자 D. Lee, 마지막 저자 명현 (5명) |
| 6 | 2026 | [DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning](https://doi.org/10.1109/tro.2026.3653774) · IEEE Transactions on Robotics | 사족 보행 로봇은 동물처럼 어수선한 환경을 다닐 잠재력이 있지만, 몸통이 땅에 고정되지 않은 구조라 현실의 불확실성에 취약해 보행 제어가 어렵다. 심층 강화학습이 강건한 보행 제어기를 만드는 대안으로 떠올랐지만, 고유 감각(proprioception, 관절 각도처럼 로봇이 제 몸에서 재는 정보)에만 기대는 방법은 앞발이 계단에 닿아야 계단을 알아채므로 충돌 없는 보행을 포기하게 되고, 외부 감각을 쓰려면 센서로 오랜 시간 관측해 정밀하게 만든 지도가 필요하다. 이 연구는 회복력 있는 다중 모달 강화학습 틀로 고유 감각과 외부 감각을 합치는 방법을 내놓았다. 이 제어기는 거친 지형·가파른 경사·높은 계단 등 다양한 실제 코스에서 사족 보행 로봇의 민첩한 보행을 보였고, 학습 때와 분포가 다른 상황에서도 강건성을 유지했다.[^p6] | 1저자 I M. A. Nahrendra, 마지막 저자 명현 (8명) |
| 7 | 2021 | [CAROS-Q: Climbing Aerial RObot System Adopting Rotor Offset With a Quasi-Decoupling Controller](https://doi.org/10.1109/lra.2021.3108489) · IEEE Robotics and Automation Letters | 무인 항공기(UAV)는 여러 분야에서 쓸모를 보여 왔지만 건물 점검·청소 같은 수직면 작업에 쓰기에는 아직 이르다. 이 연구는 공중에 떠 있는 동안 모양을 바꿔 비행 자세를 수평에서 수직으로, 또 그 반대로 바꿔 벽에 붙고(퍼칭) 벽을 오를 수 있는, 기울어지는 장치를 단 동축 6로터(Y6) 비행체를 설계했다. 기울어지는 로터를 기울임 축에서 일정 거리 떨어뜨리는 로터 오프셋 설계로 벽과 기체 사이 거리를 줄여 안정성을 높이고 전력 효율을 높일 여지를 넓혔다. 그러나 이 오프셋 때문에 서보 모터가 느려지고 기울기 각이 한쪽으로만 움직일 수 있어 기존 제어 방법에 큰 문제가 생기므로, 준분리 제어(quasi-decoupling control)라는 새 제어 방법을 제안해 서보 모터의 느린 동특성과 각도 제약을 극복했다.[^p7] | 1저자 H. Lee, 마지막 저자 명현 (7명) |
| 8 | 2025 | [PIDLoc: Cross-View Pose Optimization Network Inspired by PID Controllers](https://doi.org/10.1109/cvpr52734.2025.02047) · IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | 자율주행에는 정확한 위치 추정이 꼭 필요하지만, 위성 항법(GNSS) 기반 방법은 고층 건물이 늘어선 도심 같은 환경에서 어려움을 겪는다. 위성 사진으로 차량 자세를 바로 추정하는 교차 시점 자세 최적화가 효과적인 해법인데, 기존 방법은 주어진 자세에서의 교차 시점 특징에 주로 기대어 정밀도를 위한 세부 맥락과 큰 초기 자세 오차에 강한 전역 맥락을 놓친다. 이 연구는 비례-적분-미분(PID) 제어기에서 착안한 교차 시점 자세 최적화 방법 PIDLoc을 내놓았다. RGB 영상과 라이다 데이터를 써서 PID 갈래로 교차 시점 특징 관계를 모델링하는데, 특징 차이로 국소 맥락(P)을, 누적한 특징 차이로 전역 맥락(I)을, 특징 차이의 기울기로 세부 맥락(D)을 잡는다. 공간 인식 자세 추정기(SPE)가 이 특징들의 공간 관계를 잡아 자세를 추정한다. KITTI 데이터셋의 교차 시점 자세 추정에서 이전 최고 성능보다 위치 오차를 37.8% 줄였다.[^p8] | 1저자 W. Lee, 마지막 저자 명현 (7명) |

## 교수와 전문 분야

명현 교수는 KAIST 전기및전자공학부 교수다. 전기및전자공학부 교수 소개는 디비전을 Signal과 Computer로, 주요 연구분야를 AI & Machine Learning, Multimedia Signal Processing, Robotics & Control로, 주요 연구를 자율 로봇·드론·자동차 항법, SLAM, 딥러닝, 기계학습으로 적고, 소속연구실을 「미래도시로봇 연구실」로 적는다.[^eeprof]

연구실 교수 소개 페이지에 따르면 교수는 KAIST 전기공학에서 학사(1992), 석사(1994), 박사(1998)를 받았다. 한국전자통신연구원(ETRI)의 Senior Researcher(1998–2002), Emersys Corporation의 CTO 겸 Digital Contents Research Laboratory Director(2002–2003), 삼성종합기술원(SAIT)의 Principal Researcher(2003–2008)를 거쳐 2008년 KAIST 건설및환경공학과에 부임했고, 2019년 1월부터 전기및전자공학부 교수다. 건설및환경공학과, KAIST Robotics Program, KI for Robotics, KAIST Future Vehicle Program의 겸임교수(Adjunct Professor)이고, 5D AI Robotics Research Center(2026년 4월부터), USCRL(Unmanned Swarm CPS Research Lab Center, 2021년 2월부터), Hanwha Aerospace-KAIST Autonomy Hub Center(2023년 7월부터)의 Director를 맡고 있다.[^prof] 교수 소개는 교수가 해파리 제거 로봇 JEROS, 벽을 오르는 드론 CAROS, 굴착 로봇 Mole-bot, 보지 않고 걷는(blind-walking) 사족 보행 로봇 DreamWaQer의 개발을 이끌었고, 현재 연구 관심을 로봇 자율 이동, 공간 인공지능, SLAM, 구조물 건전성 모니터링(SHM), 군집 로봇으로 적는다.[^prof]

교수 소개 페이지의 학계 활동 가운데 현재 맡은 것으로는 IEEE RA-L(Robotics & Automation Letters)의 Senior Editor(2026년 7월부터), 제어·로봇·시스템학회(ICROS) 부회장(2024년부터)과 한국로봇학회(KROS) 부회장(2023년부터), IEEE VTS Distinguished Lecturer(2023–2027), ICRA 2027 Program Co-Chair가 있다.[^prof] 2021년 10월 이후 수상으로는 2022 IEEE RA-L Best Paper Award(2023), KAIST 연구상(2023)과 KAIST Research Day 연구대상(2026), 2023 한국로봇학회 학술상, ICRA 2023 사족 보행 로봇 챌린지 우승, CES 2023 혁신상(Hills Robotics와 함께) 등이 있으며, 전체 목록은 아래 「수상」에 있다.[^prof]

논문으로 보면 KAIST에서의 전문 분야는 라이다 기반 SLAM과 위치 추정(대표 논문 1, 2, 3),[^p1][^p2][^p3] 주행 가능 영역 인식과 경로 계획(대표 논문 4, 5),[^p4][^p5] 강화학습 기반 다리 로봇 보행(대표 논문 6),[^p6] 벽을 오르는 드론과 교차 시점 위치 추정(대표 논문 7, 8)이다.[^p7][^p8]

## 응용 분야

연구실은 연구를 스마트 도시의 실제 환경, 즉 도시를 짓고 유지하는 일에 쓰이는 로봇에 겨냥한다.[^area] 과제 게시판에서 기간이 2021년 10월 이후에 걸친 과제는 산불 대응 로봇(KIRO), 항공·해상·지상 플랫폼용 양자 항법 시스템, 자율주행 차량용 레이더·카메라·라이다 센서의 온라인 보정과 SLAM(LG Innotek), 휴머노이드 로봇의 학습 기반 전신 제어(KIMM), 굴착기용 3차원 지형 지도(HD XiteSolution), 송전선 점검 드론(KEPCO), 실내 시각 SLAM(Samsung Elec.), 넓은 실내에서 여러 로봇이 함께 하는 협업 SLAM과 항법, 초소형 군집 로봇의 항법과 제어 등을 다룬다.[^project] 누리집 Spin-off Company 페이지는 Seadronix와 URobotics를 들고 두 회사에 있는 연구실 출신 구성원을 적는다. 해파리 제거 로봇 JEROS의 기술은 RasTech에 이전됐다.[^spinoff][^first] 연구실은 HeLiMOS, X-MAS, KAIST VIO, ViViD++ 등의 데이터셋을 공개한다.[^dataset]

## 구성원

연구실 누리집 Current 페이지의 박사후연구원 1명, 박사과정 29명, 석사과정 16명, 연구원 1명이다.[^current] 과정과 이름 옆 표기(RL은 Research Leader, GL은 Group Leader)는 페이지 그대로이고, 「시작」 칸은 페이지가 적은 입학 학기 표기다(페이지는 이 목록을 입학 연도 순으로 정렬했다고 적는다). 페이지의 Group Leaders 절에 오른 6명은 박사과정 명단의 GL 표시와 같은 사람들이다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Kevin Christiansen MARSIM / RL | 박사후연구원 | '26F | Multi-robot System, Sensor Fusion, Swarm Planner |  | 1 |
| Kwang-yik JUNG | 박사과정 | '14F | VIO, SLAM, AGV |  |  |
| Seunghee LEE | 박사과정 | '17S | DL-based Human Pose / Behaviour Recognition, SNN |  |  |
| Changkyoon KIM | 박사과정 | '18F | Localization |  |  |
| Yunsoo KIM | 박사과정 | '21S | AI |  |  |
| Sungjae SHIN | 박사과정 | '22S | Sensor Fusion, Visual SLAM, Multi-Robot System, UGVs |  |  |
| Seongho NAM | 박사과정 | '22S |  |  |  |
| Hyeonwoo LEE / Former GL ('25.02-'26.09) | 박사과정 | '22F | Path Planning and Control, Deep Reinforcement Learning |  | 6 |
| Samyeul NOH | 박사과정 | '22F | Reinforcement Learning, Robot Learning |  |  |
| Jinwoo JEON / GL | 박사과정 | '23S | Visual SLAM, Deep Learning |  |  |
| Donguk SEO / Former GL ('24.08-'26.09) | 박사과정 | '23S | Multi-Map reconstruction, Visual SLAM for AR application |  |  |
| Youngwoo LEE | 박사과정 | '23S | Robot & automobile systems, software architecture, Deep Reinforcement Learning |  |  |
| Seungjae LEE / GL | 박사과정 | '23F | LiDAR SLAM, Deep Learning |  |  |
| Dongkyu LEE | 박사과정 | '23F | Path Planning, Decision Making, Legged Robot |  | 5, 6 |
| Jaesang SUN | 박사과정 | '23F | Deep Learning, Computer Vision, SLAM |  |  |
| Myeongwoo JEONG | 박사과정 | '24S | UAV, Multi-robot localization |  | 7 |
| Dasol HONG / GL | 박사과정 | '24S | Object Detection, Domain Generalization, VLM |  | 8 |
| Jun Seong LEE | 박사과정 | '24S | Deep learning, Computer Vision for Physiological Measurement |  |  |
| Taewan KIM / GL | 박사과정 | '24F | Mobile Robots, UAVs, Control |  |  |
| Seoyeon JANG | 박사과정 | '24F | Change detection, Long-term Map management |  | 3 |
| Seunghyun LEE | 박사과정 | '24F | Locomotion Controller, Deep Reinforcement Learning |  | 6 |
| Jeewon KIM | 박사과정 | '25S | Visual SLAM, UAVs |  |  |
| Gunhee SHIN | 박사과정 | '25S | SLAM, LiDAR, Sensor Fusion |  |  |
| Daebeom KIM | 박사과정 | '25S | LiDAR, SLAM |  | 2 |
| Juhye PARK | 박사과정 | '25F | Embodied AI, Cross-view geo-localization, VLN |  | 8 |
| Mincheol KIM / GL | 박사과정 | '25F | Robotics, Control, Legged robot, Humanoid |  |  |
| Geehoon LEE | 박사과정 | '26S | SLAM, Navigation | wlgns4123@kaist.ac.kr |  |
| Chanjoon PARK / GL | 박사과정 | '26F | Control, Planning, UAVs |  |  |
| Seonghyeon LIM | 박사과정 | '26F | Robot Learning, Control, Manipulation |  |  |
| Jungha WANG | 박사과정 | '26F | Visual SLAM, Deep Learning |  |  |
| Junwan CHOI | 석사과정 | '25S | Visual SLAM, Quadruped Robots |  |  |
| Jiwon PARK | 석사과정 | '25S | UGVs, Navigation, Robot Perception |  |  |
| Chanhyuk LEE | 석사과정 | '25S | Multi-Robot System, Deep Learning, Visual SLAM |  |  |
| Wanhee KIM | 석사과정 | '25S | Deep Learning, Computer Vision |  |  |
| Jei KONG | 석사과정 | '25S | LiDAR SLAM, VLM |  |  |
| Eunbin Carroll LEE | 석사과정 | '25F | UAVs, Control |  |  |
| Wonbin LEE | 석사과정 | '25F | LiDAR SLAM, Sensor Fusion |  |  |
| Sejin KWON | 석사과정 | '26S | Learning-based control, Reinforcement learning | sejink@kaist.ac.kr |  |
| Seunghun LEE | 석사과정 | '26S | Visual SLAM, Deep Learning | shleee@kaist.ac.kr |  |
| Taeji LEE | 석사과정 | '26S | Bio-inspired robotics, Robot designing, Future robotics | tjlee0512@kaist.ac.kr |  |
| Cheolmin PARK | 석사과정 | '26F | humanoid, controls, robot learning |  |  |
| Gyuhyeun SONG | 석사과정 | '26F | Humanoid, Learning-based Control, Robot Learning |  |  |
| Jihun NAM | 석사과정 | '26F | Visual SLAM, Sensor Fusion, Deep Learning |  |  |
| Minsang KONG | 석사과정 | '26F | Visual SLAM, Deep Learning |  |  |
| Dongjae KIM | 석사과정 | '26F | Visual SLAM, Sensor Fusion |  |  |
| Javier Dustin TAMBUNAN | 석사과정 | '26F | Control, UAVs, Object Detection |  |  |
| Sang-Mi HAN | 연구원 |  |  |  |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사후연구원 9명, 박사 34명, 석사 68명, 연구원 2명, 모두 113줄이다.[^alumni] 페이지는 이 목록을 졸업 연도 순으로 정렬했다고 적으며, 괄호 안 학기 표기(예: '25F)는 페이지 그대로다. 이름 옆 RL·GL 표시도 페이지 그대로다. 한 사람이 석사와 박사, 박사와 박사후연구원 절에 함께 오른 경우가 있고, 석사 졸업생 가운데 여러 명은 현재 박사과정 구성원으로도 올라 있다. 페이지에 진로 칸은 없다.

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Serin LEE | 박사후연구원 ('10F) |  |
| Seungmok LEE | 박사후연구원 ('14F) |  |
| Haemin JEON | 박사후연구원 ('14F) |  |
| Jongdae JUNG | 박사후연구원 ('15F) |  |
| Hyungtae LIM | 박사후연구원 ('23S) |  |
| I Made Aswin NAHRENDRA | 박사후연구원 ('24S) |  |
| Yeeun KIM | 박사후연구원 ('24F) |  |
| Changki SUNG / RL | 박사후연구원 ('25F) |  |
| Eungchang LEE / RL, Former GL ('21-'25.08) | 박사후연구원 ('25F) |  |
| Haemin JEON | 박사 ('14F) |  |
| Seungmok LEE | 박사 ('14F) |  |
| Donghwa LEE | 박사 ('14F) |  |
| Jongdae JUNG | 박사 ('15F) |  |
| Hanguen KIM | 박사 ('16S) |  |
| Byeolteo PARK | 박사 ('16F) |  |
| Dong-Hoon KIM | 박사 ('16F) |  |
| Jong-Heon KIM | 박사 ('18F) |  |
| Sungwook JUNG | 박사 ('19S) |  |
| Wanchoel MYEONG | 박사 ('19F) |  |
| Hyongjin KIM | 박사 ('19F) |  |
| Yu-Cheol LEE | 박사 ('20S) |  |
| Kyungbok SUNG | 박사 ('20F) |  |
| Wonkeun YOON | 박사 ('20F) |  |
| Hyungtae LIM | 박사 ('23S) |  |
| Alex Junho LEE | 박사 ('23S) |  |
| Seungwon SONG | 박사 ('23S) |  |
| I Made Aswin NAHRENDRA | 박사 ('24S) |  |
| Dongki NOH | 박사 ('24F) |  |
| Yeeun KIM | 박사 ('24F) |  |
| Hyunjun LIM | 박사 ('24F) |  |
| Jae-Uk SHIN | 박사 ('24F) |  |
| Taekjun OH | 박사 ('25S) |  |
| Byeongho YU | 박사 ('25S) |  |
| Eungchang LEE / RL, Former GL ('21-'25.08) | 박사 ('25F) |  |
| Changki SUNG / RL | 박사 ('25F) |  |
| Woojoo LEE / Former GL | 박사 ('25F) |  |
| Junho CHOI / Former GL | 박사 ('25F) |  |
| Wonho SONG | 박사 ('25F) |  |
| Junseok LEE / Former GL | 박사 ('25F) |  |
| Minho OH | 박사 ('26S) |  |
| Duckyu CHOI | 박사 ('26S) |  |
| Jieum HYUN | 박사 ('26S) |  |
| Kevin Christiansen MARSIM / RL | 박사 ('26F) |  |
| Yuseok BANG | 석사 ('10F) |  |
| Gon-Yop KIM | 석사 ('11S) |  |
| Iksu SHIN | 석사 ('11S) |  |
| Seong Han CHOI | 석사 ('11F) |  |
| Tae-Hwan LEE | 석사 ('11F) |  |
| Joomi PARK | 석사 ('12S) |  |
| Jongdae JUNG | 석사 ('12F) |  |
| Haemin JEON | 석사 ('12F) |  |
| Dong-Hoon KIM | 석사 ('13F) |  |
| Byeolteo PARK | 석사 ('13F) |  |
| Hanguen KIM | 석사 ('13F) |  |
| Jae-Uk SHIN | 석사 ('14S) |  |
| Jieun Park | 석사 ('14S) |  |
| Hyongjin KIM | 석사 ('14S) |  |
| Kwang-yik JUNG | 석사 ('14F) |  |
| Sang Won LEE | 석사 ('15S) |  |
| Youngjae KIM | 석사 ('15S) |  |
| Sungwook JUNG | 석사 ('16F) |  |
| Seunghee LEE | 석사 ('17S) |  |
| Jungmo KOO | 석사 ('17S) |  |
| Suyoung CHOI | 석사 ('17S) |  |
| Seungwon SONG | 석사 ('18S) |  |
| Pillip YOUN | 석사 ('18S) |  |
| Jinki KIM | 석사 ('18F) |  |
| Kyukwang KIM | 석사 ('18F) |  |
| Jieum HYUN | 석사 ('19S) |  |
| Jinkwang KIM | 석사 ('19F) |  |
| Christian TIRTAWARDHANA | 석사 ('19F) |  |
| Yeeun KIM | 석사 ('20S) |  |
| Hyunjun LIM | 석사 ('20S) |  |
| Hyungtae LIM | 석사 ('20S) |  |
| Junho CHOI / Former GL | 석사 ('20S) |  |
| Changgyu PARK | 석사 ('20F) |  |
| Joohyun PARK | 석사 ('20F) |  |
| Hyungyu LEE | 석사 ('21S) |  |
| Eungchang LEE / RL, Former GL ('21-'25.08) | 석사 ('21S) |  |
| Yunsoo KIM | 석사 ('21S) |  |
| Woojoo LEE / Former GL | 석사 ('21S) |  |
| Changki SUNG / RL | 석사 ('21S) |  |
| Seulgi JEON | 석사 ('21S) |  |
| Byeongho YU | 석사 ('21S) |  |
| Duckyu CHOI | 석사 ('21F) |  |
| Sungwon HWANG | 석사 ('22S) |  |
| Sumin HU | 석사 ('22S) |  |
| Euigon JUNG | 석사 ('22S) |  |
| Minho OH | 석사 ('22F) |  |
| Jinwoo JEON / GL | 석사 ('23S) |  |
| Donguk SEO / Former GL ('24.08-'26.09) | 석사 ('23S) |  |
| Dongkyu LEE | 석사 ('23F) |  |
| Seungjae LEE / GL | 석사 ('23F) |  |
| Taewan KIM / GL | 석사 ('24S) |  |
| Myeongwoo JEONG | 석사 ('24S) |  |
| Dasol HONG / GL | 석사 ('24S) |  |
| Seoyeon JANG | 석사 ('24F) |  |
| Seunghyun LEE | 석사 ('24F) |  |
| Ingyun LEE | 석사 ('24F) |  |
| Juhyun KIM | 석사 ('24F) |  |
| Jaewon PARK | 석사 ('25S) |  |
| Gunhee SHIN | 석사 ('25S) |  |
| Jeewon KIM | 석사 ('25S) |  |
| Daebeom KIM | 석사 ('25S) |  |
| Kihwan RYOO | 석사 ('25S) |  |
| Juhye PARK | 석사 ('25F) |  |
| Jun LEE | 석사 ('26F) |  |
| Chanjoon PARK / GL | 석사 ('26F) |  |
| Seunggyu SONG | 석사 ('26F) |  |
| Alvin Jinsung CHOI | 석사 ('26F) |  |
| Taeyun KIM | 석사 ('26F) |  |
| Yonghun JEONG | 연구원 |  |
| Youngbo SHIM | 연구원 |  |

## 최근 논문 목록 (2021–2026)

누리집 Papers 페이지 목록의 2021–2026년 항목 242건이다. 국제 학술지 41편, 국내 학술지 6편, 국제 학회 논문 138편, 국내 학회 논문 57편이고, 연도마다 학술지 다음 학회 순으로 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이며, 저자 이름 뒤 †는 누리집이 교신저자로 적은 표시, *는 공동 기여 표시다. 2026년 항목 가운데 26건은 누리집이 「(Accepted)」로 적은, 발표나 출판을 앞둔 채택 논문이다. IEEE RA-L 논문 8편은 같은 논문을 학회에서 발표한 줄로도 함께 실려 있고, 2021년 학술지 항목 1건은 다른 논문의 정정 공지(Corrections to …)다. 교수가 마지막 저자가 아닌 공동연구 논문도 목록대로 실었다.[^pubs]

**2026**

- Junseong Lee, Samyeul Noh, Changki Sung, and Hyun Myung†. "LQ-rPPG: A Label-Quantized Coarse-to-Fine Learning Framework for Remote Physiological Measurement". *ESWA (Expert Systems With Applications), vol.329, Nov. 2026*.
- Changki Sung, Hyungtae Lim, Wanhee Kim, Youngwoo Seo, and Hyun Myung†. "Contextrast++: Robust Multi-Scale Contextual Contrastive Learning for Semantic Segmentation". *IEEE TPAMI (Transactions on Pattern Analysis and Machine Intelligence), Jul. 2026. (Accepted)*.
- Kwangyik Jung, Eungchang Mason Lee, Taekjun Oh, and Hyun Myung†. "ASPIRE-VINS: Adaptive Spline-based Visual-inertial Navigation System With Robust 3D Measurement Residuals". *IEEE RA-L (Robotics and Automation Letters), Jun. 2026. (Accepted)*.
- Donguk Seo, Jinwoo Jeon, Eungchang Mason Lee, and Hyun Myung†. "GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow". *IEEE RA-L (Robotics and Automation Letters), vol.11, no.6, pp.7644-7651, Apr. 2026*.
- Seoyeon Jang, Alex Lee, I Made Aswin Nahrendra, and Hyun Myung†. "Chamelion : Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments". *IEEE RA-L (Robotics and Automation Letters), vol.11, no.4, pp.4361-4368, Feb. 2026*.
- Hyungtae Lim\*, Daebeom Kim\*, and Hyun Myung†. "Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles". *IEEE T-IV (Transactions on Intelligent Vehicles), vol.11, no.3, pp.338-351, Feb. 2026*.
- Juhyun Kim and Hyun Myung†. "Robust and Accurate 3D Point Cloud Registration Method for Close-range Docking of Spacecraft". *IEEE TAES (Transactions on Aerospace and Electronic Systems), vol.62, pp.4799-4812, Jan. 2026*.
- I Made Aswin Nahrendra, Byeongho Yu, Minho Oh, Dongkyu Lee, Seunghyun Lee, Hyeonwoo Lee, Hyungtae Lim, and Hyun Myung†. "DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning". *IEEE T-RO (Transactions on Robotics), vol.42, pp.819-836, Jan. 2026*.
- Eungchang Mason Lee, Kevin Christiansen Marsim, and Hyun Myung†. "LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry with Adaptive Schmidt-Kalman Filter and Data Exploitation". *IEEE RA-L (Robotics and Automation Letters), vol.11, no.1, pp.922-929, Jan. 2026*.
- Dongjae Kim, Sungjae Shin, and Hyun Myung†. "CARE: Calibration-Aware Ray-wise Evaluation of 3D Gaussian Splatting Maps". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Dec. 2026. (Accepted)*.
- Carroll Eunbin Lee, Seonghyeon Lim, Hyeonwoo Lee, and Hyun Myung†. "AIM: Attention as Implicit Masking for Whole-Body Legged Manipulation". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Dec. 2026. (Accepted)*.
- Mingyu Park\*, Samyeul Noh\*, Hyun Myung†, and Donghwan Lee†. "VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning". *in Proc. Conference on Neural Information Processing Systems (NeurIPS), Sydney, Australia, Dec. 2026. (Accepted)*.
- Seonghyeon Lim, Hyeonwoo Lee, Mincheol Kim, Kimin Lee†, and Hyun Myung†. "MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking". *in Proc. Conference on Robot Learning (CoRL), Texas, USA, Nov. 2026. (Accepted)*.
- Alvin Jinsung Choi, Wanhee Kim, Taeyun Kim, Dasol Hong, Wooju Lee, and Hyun Myung†. "NeuDonatello: Uncertainty-Aware Framework for Accurate Neural SDF Learning". *in Proc. The 37th British Machine Vision Conference (BMVC), Lancaster, UK, Nov. 2026. (Accepted)*.
- Gunhee Shin, Yunsoo Kim, Chanhyuk Lee, Wanhee Kim, Minwoo Lee, Sungwoo Han, Jeongwoo Woo, Hyuntai Chin, Minha Park, and Hyun Myung†. "Online Target-less Radar-LiDAR-Camera Extrinsic Calibration via Joint Optimization". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Chanhyuk Lee, Wonbin Lee, Dongjae Kim, and Hyun Myung†. "AdaM-VIO: Robust Adaptive Multi-Camera Visual-Inertial Odometry in Degenerate Indoor Environments". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Mincheol Kim, Gyuhyeun Song, Cheolmin Park, Hyeonwoo Lee, and Hyun Myung†. "LLM-Guided Automatic Reward Design for Humanoid Locomotion". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Jinwoo Jeon, Dong-Uk Seo, and Hyun Myung†. "DUET-SLAM: Dual-Flow Consistency for Dense Monocular SLAM in Dynamic Environments with Geometry-aware Foundation Model". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Sejin Kwon, Seungjae Lee, Carroll Eunbin Lee, and Hyun Myung†. "ALACER: Energy-Efficient Blind Locomotion via Dynamic Reward Modulation of Inferred Terrain Context". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Yunsoo Kim, Taeji Lee, and Hyun Myung†. "Depth-Supervised Event Gaussian Splatting for Accurate Surface Reconstruction". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Seoyeon Jang, Daebeom Kim, Seonghyeon Lim, and Hyun Myung†. "Conservative Visual-Geometric Fusion for Off-Road Traversability Estimation". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Chanjoon Park, Myeongwoo Jeong, and Hyun Myung†. "A Multi-Resolution Any-Angle Global Planner for Aerial–Ground Robots". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Haechang Kim, Eungchang Mason Lee, Chanjoon Park, and Hyun Myung†. "TDPF: Temporal Dynamic Prior Filter for Radar Ego Velocity Estimation in Highly Dynamic Environments". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Dasol Hong, Juhye Park, and Hyun Myung†. "Beyond closed-set place recognition: unknown-aware few-shot novel place mapping". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Dong-Uk Seo, Jiwon Park, Jei Kong, Jinwoo Jeon, and Hyun Myung†. "Leveraging Planar Regularity for Gaussian Splatting SLAM". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Seunghun Lee, Jihun Nam, and Hyun Myung†. "360DVIO: Deep Visual-Inertial Odometry Using a 360-Degree Camera". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Wanhee Kim, Chang Ki Sung, and Hyun Myung†. "UToM: Uncertainty-Aware Token Merging for Efficient Semantic Segmentatio". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Sungjae Shin, Dongjae Kim, Uihyun Hwang, and Hyun Myung†. "LACE: Loop-Constraint Augmentation with Reprojection-Guided Correspondence Verification and Edge Selection for Visual-Inertial Pose Graph Optimization in Sparse-Loop Indoor Environments". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Uihyun Hwang, Sungjae Shin, Dongjae Kim, and Hyun Myung†. "Reflection-Robust Stereo Visual-Inertial Odometry via Kalman-Filtered Ground-Height Estimation". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Jiyun Yang, Jeewon Kim, Dongha Chung, Byeongho Yu, and Hyun Myung†. "SPIN: Sketch-map-based Place Inference Using Signs for Long-horizon Robot Navigation". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Junwan Choi, Geehoon Lee, and Hyun Myung†. "Enhanced Learned Feature Tracking and Adaptive Weighting for Visual-Inertial Odometry in Structured Environments". *in Proc. International Conference on Control, Automation and System (ICCAS), Sapporo, Japan, Oct. 2026. (Accepted)*.
- Seunghun Lee, Jihun Nam, Dong-Uk Seo, and Hyun Myung†. "PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh, USA, Sep. 2026 (Accepted)*.
- Junwan Choi, Woongrae Jo, Dong-Uk Seo, Jinwoo Jeon, and Hyun Myung†. "Robust Structureless Monocular Visual-Inertial Initialization Exploiting Line Features and Vanishing Points". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh, USA, Sep. 2026 (Accepted)*.
- Jei Kong, Seungjae Lee, Jeewon Kim, and Hyun Myung†. "GORI: Image-Guided Selective 3D Object Re-Association for 3D Scene Graphs and Task Planning". *in Proc. The 23th International Conference on Ubiquitous Robots (UR), Osaka, Japan, Jul. 2026*.
- Hyeonwoo Lee, Mincheol Kim, and Hyun Myung†. "HIP: Hybrid Impedance and PD Control for Adaptive and Compliant Locomotion in Quadruped Robots". *in Proc. The 23th International Conference on Ubiquitous Robots (UR), Osaka, Japan, Jul. 2026*.
- Yunsoo Kim, Changki Sung, Dasol Hong, and Hyun Myung†. "E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction". *in Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 4922-4931, Denver, USA, Jun. 2026*.
- Juhye Park, Wooju Lee, Dasol Hong, Changki Sung, Youngwoo Seo, Dongwan Kang, and Hyun Myung†. "VIRD: View-Invariant Representation through Dual-Axis Transformation for Cross-View Pose Estimation". *in Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 33693-33702, Denver, USA, Jun. 2026*.
- Jiwon Park, Dongkyu Lee, I Made Aswin Nahrendra, Jaeyoung Lim, and Hyun Myung†. "DreamFlow: Local Navigation Beyond Observation via Conditional Flow Matching in the Latent Space". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 2242-2249, Vienna, Austria, Jun. 2026*.
- Seonghyeon Lim, Seunghyun Lee, Hyeonwoo Lee, I Made Aswin Nahrendra, and Hyun Myung†. "OpenHEART: Opening Heterogeneous Articulated Objects with a Legged Manipulator". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 7791-7798, Vienna, Austria, Jun. 2026*.
- Gunhee Shin, Seungjae Lee, Jei Kong, Young-Woo Seo, and Hyun Myung†. "Smooth IMU Propagation With Jointly Distributed Poses on SE(3) Manifold for Accurate and Robust LiDAR-Inertial Odometry". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 2290-2297, Vienna, Austria, Jun. 2026*.
- Jinwoo Jeon, Dong-Uk Seo, Eungchang Mason Lee, and Hyun Myung†. "AIM-SLAM: Dense Monocular SLAM via Adaptive and Informative Multi-View Keyframe Prioritization with Foundation Model". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 18530-18537, Vienna, Austria, Jun. 2026*.
- Taeyun Kim, Alvin Jinsung Choi, Dasol Hong, and Hyun Myung†. "CLUE: Adaptively Prioritized Contextual Cues by Leveraging a Unified Semantic Map for Effective Zero-Shot Object-Goal Navigation". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 18554-18561, Vienna, Austria, Jun. 2026*.
- 박시형, 김대범, 명현. "소방대원 추종을 위한 강인한 특정 객체 추적 모듈". *in Proc. 제 41회 제어로봇시스템학회 학술대회 (ICROS 2025), 대구 EXCO, Jul. 2026*.
- 이시원, 박찬준, 이응창, 명현. "의미적 장면 완성 기반 폐색 환경에서의 종단 간 학습 기반의 쿼드로터 자율비행". *in Proc. 제 41회 제어로봇시스템학회 학술대회 (ICROS 2025), 대구 EXCO, Jul. 2026*.
- 장서연, 박주혜, 신건희, 김대범, 서영우, 강동완, 명현. "비정형 환경에서의 강인한 절대·상대 위치 추정 기술". *in Proc. 한국로봇종합학술대회 (KRoC 2026) OS, 평창 알펜시아, Feb. 2026*.

**2025**

- Kevin Christiansen Marsim, Minho Oh, Byeongho Yu, Seungjae Lee, I Made Aswin Nahrendra, Hyungtae Lim, and Hyun Myung†. "LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization". *IEEE RA-L (Robotics and Automation Letters), vol.10, no.10, pp.10050-10057, Oct. 2025*.
- Samyeul Noh, Wooju Lee, and Hyun Myung†. "Sample-Efficient and Occlusion-Robust Reinforcement Learning for Robotic Manipulation via Multimodal Fusion Dualization and Representation Normalization". *Neural Networks, vol.185, Article 107202, May. 2025*.
- Jung-Woo Lee, See-On Park, Seong-Yun Yun, Yeeun Kim, Hyun Myung, Shinhyun Choi†, and Yang-Kyu Choi†. "Decoupling Strategy to Separate Training and Inference with Three-Dimensional Neuromorphic Hardware Composed of Neurons and Hybrid Synapses". *ACS Nano, vol.19, no. 13, pp. 13063-13072, Mar. 2025*.
- Dongkyu Lee, I Made Aswin Nahrendra, Minho Oh, Byeongho Yu, and Hyun Myung†. "TRG-planner: Traversal Risk Graph-Based Path Planning in Unstructured Environments for Safe and Efficient Navigation". *IEEE RA-L (Robotics and Automation Letters), vol.10, no.2, pp.1736-1743, Feb. 2025*.
- Daebeom Kim, Seungjae Lee, Seoyeon Jang, Kevin Christiansen Marsim, and Hyun Myung†. "Raymoval: Raycasting-based Dynamic Object Removal for Static 3D Mapping". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, Dec. 2025*.
- Taewan Kim, Mincheol Kim, Sitae Noh, Gyuhyeun Song, Cheolmin Park, and Hyun Myung†. "Bio-Inspired Flexible Spine Mechanism Design for Small Quadruped Robot". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, Dec. 2025*.
- Sejin Kwon, Seonghyeon Lim, Hyeonwoo Lee, and Hyun Myung†. "Reinforcement Learning-based Inverse Kinematics Compensation for Robust Manipulation under Payload Variation and Singularity". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 2187-2191, Songdo, Korea, Nov. 2025*.
- Sungjae Shin, Wanhee Kim, Alvin Jinsung Choi, and Hyun Myung†. "GSDB: A Lightweight Database for Gaussian Splatting Map-based Visual Localization Leveraging Edge-aware and Quality-guided View Filtering". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 831-838, Songdo, Korea, Nov. 2025. [The Best Paper Award]*.
- Eungchang Mason Lee, Chanjoon Park, and Hyun Myung†. "SSF-Exploration: Safe Segments Forwarding-Based Seamless Replanning and Tracking for Fast UAV Exploration". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 288-291, Songdo, Korea, Nov. 2025*.
- Junho Choi, Kihwan Ryoo, Jeewon Kim, Taeyun Kim, Eungchang Mason Lee, Myeongwoo Jeong, Kevin Christiansen Marsim, Hyungtae Lim, and Hyun Myung†. "SaWa-ML: Structure-Aware Pose Correction and Weight Adaptation-Based Robust Multi-Robot Localization". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9170-9177, Hangzhou, China, Oct. 2025*.
- Kevin Christiansen Marsim, Jinwoo Jeon, Myeongwoo Jeong, Yeeun Kim, and Hyun Myung†. "CHADET: Cross-Hierarchical-Attention for Depth-Completion Using Unsupervised Lightweight Transformer". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 4931-4938, Hangzhou, China, Oct. 2025*.
- Jeewon Kim, Minho Oh, and Hyun Myung†. "TACS-Graphs: Traversability-Aware Consistent Scene Graphs for Ground Robot Indoor". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 6008-6015, Hangzhou, China, Oct. 2025*.
- Seunghyun Lee, Dongkyu Lee, Byeongho Yu, I Made Aswin Nahrendra, and Hyun Myung†. "Learning Resilient Blind Locomotion Controller for Humanoid Robots using Deep Reinforcement Learning". *IEEE/RAS International Conference on Humanoid Robots Workshop on Sim-to-Real Transfer for Humanoid Robots, Seoul, Korea, Oct. 2025*.
- Dasol Hong, Juhye Park, and Hyun Myung†. "ActiveGrounder: 3D Visual Grounding with Object-Hull-Guided Active Observation". *IEEE/RAS International Conference on Humanoid Robots Workshop on Bridging Humanoid Robotics and Foundation Models: Embodied Intelligence and AI Integration, Seoul, Korea, Oct. 2025*.
- Seoyeon Jang, Alex Junho Lee, I Made Aswin Nahrendra, and Hyun Myung†. "Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments". *Conference on Robot Learning (CoRL) Workshop on Safe and Robust Robot Learning for Operation in the Real World, Seoul, Korea, Sep. 2025*.
- Dasol Hong, Wooju Lee, and Hyun Myung†. "CoCoA-Mix: Confusion-and-Confidence-Aware Mixture Model for Context Optimization". *in Proc. International Conference on Machine Learning (ICML 2025), pp. 23700-23721, Vancouver, Canada, Jul. 2025*.
- Junseok Lee, Taewan Kim, Jaewon Park, Jun Lee, and Hyun Myung†. "Insect-Like Wall Climbing Robot Capable of Flying and Walking". *in Proc. The 22th International Conference on Ubiquitous Robots (UR), Texas, USA, Jun. 2025*.
- Wonho Song, Dongwan Kang, and Hyun Myung†. "Automatic LiDAR-Camera Online Calibration Monitoring and Refinement for Ground Platforms". *in Proc. The 22th International Conference on Ubiquitous Robots (UR), pp. 75-79, Texas, USA, Jun. 2025*.
- Wooju Lee, Juhye Park, Dasol Hong, Changki Sung, Youngwoo Seo, DongWan Kang, and Hyun Myung†. "PIDLoc: Cross-View Pose Optimization Network Inspired by PID Controllers". *in Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 21981-21990, Nashville, USA, Jun. 2025*.
- Youngwoo Lee, Jungho Bae, Minkyu Lee, Myunggun Kim, Wonik Park, Tokson Choe, and Hyun Myung†. "A ROS2-Based Robot Software Architecture for Plug-and-Play of Modular Payload Kits". *IEEE International Conference on Robotics and Automation (ICRA) Workshop on Robot Software Architecture, Atlanta, USA, May 2025*.
- I Made Aswin Nahrendra, Seunghyun Lee, Dongkyu Lee, and Hyun Myung†. "Versatile Legged Locomotion Adaptation through Vision-Language Grounding". *IEEE International Conference on Robotics and Automation (ICRA) Workshop on Safely Leveraging Vision-Language Foundation Models in Robotics : Challenges and Opportunities , Atlanta, USA, May 2025*.
- Seunghyun Lee, I Made Aswin Nahrendra, Dongkyu Lee, Byeongho Yu, Minho Oh, Hyeonwoo Lee, and Hyun Myung†. "DreamFLEX: Learning Fault-Aware Quadrupedal Locomotion Controller for Anomaly Situation in Rough Terrains". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 16001-16007, Atlanta, USA, May 2025*.
- Kihwan Ryoo, Hyungtae Lim, and Hyun Myung†. "MambaGlue: Fast and Robust Local Feature Matching With Mamba". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 5758-5765, Atlanta, USA, May 2025*.
- Hyungtae Lim, Daebeom Kim, Gunhee Shin, Jingnan Shi, Ignacio Vizzo, Hyun Myung†, Jaesik Park†, and Luca Carlone. "KISS-Matcher: Fast and Robust Point Cloud Registration Revisited". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 11104-11111, Atlanta, USA, May 2025*.
- Joon Hyub Lee, Siripon Sutthiwanna, Sungjae Shin, Taegyu Jin, Hyun Myung†, Seok-Hyung Bae†. "Immersive Prototyping for Robot Design with 3D Sketching and VR Acting in Reconstructed Workspace". *in Proc. CHI: Conference on Human Factors in Computing Systems 2025, pp. 1-7, Yokohama, Japan, Apr. 2025*.
- 최진성, 명현. "입력 이미지 노이즈에 대한 Neural Radiance Fields의 강건성 평가". *in Proc. 제 40회 제어로봇시스템학회 학술대회 (ICROS 2025), 전남 전북대학교, Jun. 2025*.
- 송승규, 이승재, 명현. "정확한 루프 폐쇄를 위한 3차원 점군 정합 방법". *in Proc. 제 40회 제어로봇시스템학회 학술대회 (ICROS 2025), 전남 전북대학교, Jun. 2025*.
- 이응창, 명현. "위치 추정성 저하에 강건한 적응적 슈미트-칼만 필터를 사용한 라이다 관성 오도메트리". *in Proc. 제 40회 제어로봇시스템학회 학술대회 (ICROS 2025), 전남 전북대학교, Jun. 2025*.
- 이준석, 김태완, 박재원, 이준, 명현. "CAROS-H: Climbing Aerial Robot System Leveraging Hexapod Locomotion". *in Proc. 한국로봇종합학술대회 (KRoC 2025) RED Show, 평창 휘닉스, Feb. 2025*.
- 박주혜, 강동완, 명현. "기하학적투영과특성별선형변조를통한위성이미지기반지리적위치추정". *in Proc. 한국로봇종합학술대회 (KRoC 2025), 평창 휘닉스, Feb. 2025*.
- 서동욱, 홍다솔, 명현. "동적 환경에서의 위치추정을 위한 하이브리드 특징점 추적 기법". *in Proc. 한국로봇종합학술대회 (KRoC 2025), 평창 휘닉스, Feb. 2025*.
- 이응창, 이준, 박찬준, 이승현, 김태완, 명현. "무인 비행체를 위한 적응적 데이터 활용 기반의 강인한 다중 라이다 관성 위치 추정". *in Proc. 한국로봇종합학술대회 (KRoC 2025), 평창 휘닉스, Feb. 2025*.
- 이준, 이응창, 박찬준, 이승현, 김태완, 명현. "쿼드로터를 위한 적응형 비선형 모델 예측 제어기 개발". *in Proc. 한국로봇종합학술대회 (KRoC 2025), 평창 휘닉스, Feb. 2025*.

**2024**

- Seungwon Song, Hyungtae Lim, Alex Lee, Hyun Myung†. "DynaVINS++: Robust Visual-Inertial State Estimator in Dynamic Environments by Adaptive Truncated Least Squares and Stable State Recovery". *IEEE RA-L (Robotics and Automation Letters), vol.9, no.10, pp.9127-9134, Oct. 2024*.
- DongKi Noh, Hyungtae Lim, Gyuho Eoh, Duckyu Choi, Jeongsik Choi, Hyunjun Lim, SeungMin Baek, and Hyun Myung†. "CLOi-Mapper: Consistent,Lightweight, Robust, and Incremental Mapper With Embedded Systems for Commercial Robot Services". *IEEE RA-L (Robotics and Automation Letters), vol.9, no.9, pp.7541-7548, Sep. 2024*.
- Hyungtae Lim, Beomsoo Kim, Daebeom Kim, Eungchang Mason Lee, and Hyun Myung†. "Quatro++: Robust Global Registration Exploiting Ground Segmentation for Loop Closing in LiDAR SLAM". *International Journal of Robotics Research, vol.43, no.5, pp.685-715, Apr. 2024*.
- Hyungtae Lim, Minho Oh, Seungjae Lee, Seunguk Ahn, and Hyun Myung†. "Similar but Different: A Survey of Ground Segmentation and Traversability Estimation for Terrestrial Robots". *International Journal of Control, Automation and Systems, vol.22, no.2, pp.347-359, Feb. 2024*.
- Gunhee Shin, Seungjae Lee, Minho Oh, Dongkyu Lee, Jaeyoung Lee, Youngwoo Seo, and Hyun Myung†. "NM-LIO: Multiple LiDAR-Inertial Odometry Addressing LiDAR Measurement Noise Discrepancy". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, Dec. 2024*.
- Jeewon Kim, Minho Oh, and Hyun Myung†. "Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, Dec. 2024*.
- Kihwan Ryoo, Junho Choi, Hyunjun Lim, and Hyun Myung†. "SSG-VINS: A Semantic Segmentation-Guided Adaptive Visual-Inertial State Estimator". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1538-1543, Jeju, Korea, Oct. 2024*.
- Jaewon Park, Changki Sung, Seunghee Lee, Dongwan Kang, and Hyun Myung†. "Cross-View Geo-Localization via Effective Negative Sampling". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1078-1083, Jeju, Korea, Oct. 2024*.
- Seonghyeon Lim, Hyeonwoo Lee, Seunghyun Lee, and Hyun Myung†. "Learning Robust Whole-Body Control for Legged Manipulation via Learned Terrain Estimation". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1510-1515, Jeju, Korea, Oct. 2024*.
- Hyungtae Lim, Seoyeon Jang, Benedikt Mersch, Jens Behley, Hyun Myung†, and Cyrill Stachniss. "HeLiMOS: A Dataset for Moving Object Segmentation in 3D Point Clouds From Heterogeneous LiDAR Sensors". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 14087-14094, Abu Dhabi ,UAE, Oct. 2024*.
- Samyeul Noh and Hyun Myung†. "Learning Dexterous Object Manipulation with a Robotic Hand via Goal-Conditioned Visual Reinforcement Learning Using Limited Demonstrations". *European Conference on Computer Vision (ECCV) Workshop on Observing and Understanding Hands in Action, Milano, Italy, Sep. 2024*.
- Kevin Christiansen Marsim, Junho Choi, Myeongwoo Jeong, Kihwan Ryoo, Jeewon Kim, Taeyun Kim, and Hyun Myung†. "Multi-robot Cooperative Localization with Single UWB Error Correction". *in Proc. The 21th International Conference on Ubiquitous Robots (UR), pp. 539-544, New York, USA, Jun. 2024*.
- Seungjae Lee, Minho Oh, I Made Aswin Nahrendra, Wonho Song, Byeongho Yu, Kevin Christiansen Marsim, and Hyun Myung†. "3D LiDAR Map-Based Robust Localization System Leveraging Pose Divergence Detection and Relocalization". *in Proc. The 21th International Conference on Ubiquitous Robots (UR), pp. 1-4, New York, USA, Jun. 2024*.
- Minho Oh, Gunhee Shin, Seoyeon Jang, Seungjae Lee, Dongkyu Lee, Wonho Song, Byeongho Yu, Hyungtae Lim, Jaeyoung Lee, and Hyun Myung†. "B-TMS: Bayesian Traversable Terrain Modeling and Segmentation Across 3D LiDAR Scans and Maps for Enhanced Off-Road Navigation". *in Proc. IEEE Intelligent Vehicles Symposium (IV 2024) Workshop, pp. 200-205, Jeju, Korea, Jun. 2024*.
- Wonho Song, Minho Oh, Jaeyoung Lee, and Hyun Myung†. "Galibr: Targetless LiDAR-Camera Extrinsic Calibration Method via Ground Plane Initialization". *in Proc. IEEE Intelligent Vehicles Symposium (IV 2024) Workshop, pp. 217-223, Jeju, Korea, Jun. 2024*.
- Changki Sung, Wanhee Kim, Jungho An, WooJu Lee, Hyungtae Lim, and Hyun Myung†. "Contextrast: Contextual Contrastive Learning for Semantic Segmentation". *in Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3732-3742, Seattle, USA, Jun. 2024*.
- Ingyun Lee, Wooju Lee, and Hyun Myung†. "Domain Generalization with Vital Phase Augmentation". *in Proc. AAAI Conference on Artificial Intelligence (AAAI 2024), pp. 2892-2900, Vancouver, Canada, Feb. 2024*.
- Wooju Lee\*, Dasol Hong\*, Hyungtae Lim†, and Hyun Myung†. "Object-Aware Domain Generalization for Object Detection". *in Proc. AAAI Conference on Artificial Intelligence (AAAI 2024), pp. 2947-2955, Vancouver, Canada, Feb. 2024*.
- 김지원, 최준호, 명현. "정밀 시각-관성-거리 기반 위치 추정을 위한 다중 로봇 제어". *in Proc. 제 39회 제어로봇시스템학회 학술대회 (ICROS 2024), 대전 컨벤션센터, Jul. 2024*.
- 이승희, 성창기, 박재원, 명현. "대조 학습 기반 크로스뷰 지오이미지 검색". *in Proc. 제 39회 제어로봇시스템학회 학술대회 (ICROS 2024), 대전 컨벤션센터, Jul. 2024*.
- 현지음, 오택준, 명현. "비가시선 환경에서의 UWB 거리 측정 오차 보정 방법". *in Proc. 제 39회 제어로봇시스템학회 학술대회 (ICROS 2024), 대전 컨벤션센터, Jul. 2024*.
- 이승현, I Made Aswin Nahrendra, 이현우 ,이동규, 명현. "심층강화학습 기반 사족보행 로봇의 다양한 행동 제어 기술 개발". *in Proc. 한국로봇종합학술대회 (KRoC 2024) RED Show, 평창 휘닉스, Feb. 2024*.
- 이승현, I Made Aswin Nahrendra, 유병호, 명현. "심층 강화 학습을 이용한 4 족 로봇 블라인드 보행 제어". *in Proc. 한국로봇종합학술대회 (KRoC 2024) OS, 평창 휘닉스, Feb. 2024*.
- 홍다솔, 명현. "확장된 MEC 손실함수를 통한 객체 탐지에서의 도메인 일반화". *in Proc. 한국로봇종합학술대회 (KRoC 2024), 평창 휘닉스, Feb. 2024*.
- 이현우, I Made Aswin Nahrendra, 이승현, 이동규, 노승규, 명현. "보행 속도 적응적 보행 패턴이 가능한 심층강화학습 기반의 사족보행 로봇 제어기 개발". *in Proc. 한국로봇종합학술대회 (KRoC 2024), 평창 휘닉스, Feb. 2024*.

**2023**

- Joon-Kyu Han, Jung-Woo Lee, Yeeun Kim, Young Bin Kim, Seong-Yun Yun, Sang-Won Lee, Ji-Man Yu, Keon Jae Lee, Hyun Myung†, and Yang-Kyu Choi†. "3D Neuromorphic Hardware With Single Thin-Film Transistor Synapses Over Single Thin-Body Transistor Neurons by Monolithic Vertical Integration". *Advanced Science, pp.202302380, Sep. 2023*.
- Young-Min Kim, Yong-Ho Yoo, In-Ug Yoon, Hyun Myung, and Jong-Hwan Kim†. "Spatio-Temporal Deformable DETR for Weakly Supervised Defect Localization". *IEEE Sensors, vol.23, no.17, pp.19935-19945, Jul. 2023*.
- Alex Junho Lee, Seungwon Song, Hyungtae Lim, Wooju Lee, and Hyun Myung†. "(LC)2: LiDAR-Camera Loop Constraints For Cross-Modal Place Recognition". *IEEE RA-L (Robotics and Automation Letters), vol.8, no.6, pp.3589-3596, Jun. 2023*.
- DongKi Noh, Chang Ki Sung, Taeyoung Uhm, Wooju Lee, Hyungtae Lim, Jaeseok Choi, Kyuewang Lee, Dasol Hong, Daeho Um, Inseop Chung, Hochul Shin, Min-Jung Kim, Hyoung-Rock Kim, Seung-Min Baek, and Hyun Myung†. "X-MAS: Extremely Large-Scale Multi-Modal Sensor Dataset for Outdoor Surveillance in Real Environments". *IEEE RA-L (Robotics and Automation Letters), vol.8, no.2, pp.1093-1100, Feb. 2023*.
- Alex Junho Lee, Wonho Song, Byeongho Yu, Duckyu Choi, Christian Tirtawardhana, and Hyun Myung†. "Survey of robotics technologies for civil infrastructure inspection". *Journal of Infrastructure Intelligence and Resilience, vol. 2, no. 1, 100018, Mar. 2023*.
- Junho Choi, Kevin Christiansen Marsim, Myeongwoo Jeong, Kihwan Ryoo, Jeewon Kim, Hyun Myung†. "Multi-unmanned Aerial Vehicle Pose Estimation Based on Visual-inertial-range Sensor Fusion (영상-관성-거리 센서 융합 기반의 다중 무인기 위치 추정)". *Journal of Institute of Control, Robotics and Systems (in Korean), vol.29, no.11, pp.859-865, Nov. 2023*.
- Hyunjun Lim, Hyun Myung†. "소실점 정보의 Loss 함수를 이용한 특징선 기반 SLAM". *로봇학회 논문지, vol.18, no.3, pp.330-336, Aug. 2023*.
- Junseok Lee, Hyun Myung†. "극한 환경 탐사 로봇: 두더지 생체모방 굴진 로봇(Mole-Bot)". *로봇학회 논문지, vol.20, no.1, pp.4-10, Jan. 2023*.
- Samyeul Noh, Seonghyun Kim, Ingook Jang, and Hyun Myung†. "An Investigation into Value-Implicit Pre-Training for Task-Agnostic, Sample-Efficient Goal-Conditioned Reinforcement Learning". *in Proc. Conference on Neural Information Processing Systems (NeurIPS 2023) Workshop, New Orleans, USA, Dec. 2023*.
- Yeeun Kim, Junwan Choi, and Hyun Myung†. "Inertial-Joint Learning-aided Robust Pose Estimation for Legged Robots". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 251-257, Taicang, China, Dec. 2023*.
- Seoyeon Jang, Minho Oh, Byeongho Yu, I Made Aswin Nahrendra, Seungjae Lee, Hyungtae Lim, and Hyun Myung†. "TOSS: Real-time Tracking and Moving Object Segmentation for Static Scene Mapping". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 187-199, Taicang, China, Dec. 2023*.
- Samyeul Noh, and Hyun Myung†. "Coupling Vision and Proprioception for Sample-Efficient, Object-Occlusion-Robust Robotic Manipulation". *in Proc. International Conference on Computer Vision (ICCV 2023) Workshop, pp. 1-9, Paris, France, Oct. 2023*.
- Duckyu Choi, Donghyeon Youn, and Hyun Myung†. "AWP: Alpha Wrapping-Based Collision-Free Surface-Along Path Planner for UAV". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 909-913, Yeosu, Korea, Oct. 2023*.
- Jinwoo Jeon, Myungwoo Jeong, and Hyun Myung†. "Fuzzy Logic and Neural Network-Based Intelligent Control System for Quadruped Robot on Extreme Terrain". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1885-1889, Yeosu, Korea, Oct. 2023*.
- Seunggyu Song, Byeongho Yu, Minho Oh, and Hyun Myung†. "BIG-STEP: Better Initialized State Estimator for Legged Robots with Fast and Robust Ground Segmentation". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 184-188, Yeosu, Korea, Oct. 2023*.
- Sungjae Shin, Yeeun Kim, Byeongho Yu, Eungchang Mason Lee, Dong-Uk Seo, and Hyun Myung†. "PanoNetVLAD: Visual Loop Closure Detection in Continuous Space Represented With Panoramic View Using Multiple". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 172-177, Yeosu, Korea, Oct. 2023*.
- Dong-Uk Seo, Hyuntae Lim, Eungchang Mason Lee, Hyunjun Lim, and Hyun Myung†. "Enhancing Robustness of Line Tracking Through Semi-Dense Epipolar Search in Line-based SLAM". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 3483-3490, Detroit, USA, Oct. 2023*.
- I Made Aswin Nahrendra, Minho Oh, Byeongho Yu, Hyungtae Lim, and Hyun Myung†. "Robust Recovery Motion Control for Quadrupedal Robots via Learned Terrain Imagination". *in Proc. Robotics: Science and Systems (RSS 2023) Workshop, Daegu, Korea, Jul. 2023*.
- Hyungtae Lim, Lucas Nunes, Benedikt Mersch, Xieyuanli Chen, Jens Behley, Hyun Myung†, and Cyrill Stachniss. "ERASOR2: Instance-Aware Robust 3D Mapping of the Static World in Dynamic Scenes". *in Proc. Robotics: Science and Systems (RSS 2023), Daegu, Korea, Jul. 2023*.
- Eungchang Mason Lee, Donghyeon Youn, and Hyun Myung†. "THE-Planner: Topological and Hierarchical Exploration Path Planner for Fast 3D Mapping of Outdoor Structures with UAVs". *in Proc. The 20th International Conference on Ubiquitous Robots (UR), pp. 571-575, Honolulu, USA, Jun. 2023*.
- Junho Choi, Myeongwoo Jeong, Eungchang Mason Lee, Duckyu Choi, and Hyun Myung†. "NLOS-Avoiding and Obstacle-Adaptive Formation Control by Sharing Obstacle Information of a Leader UAV in Multi-UAV System". *in Proc. The 20th International Conference on Ubiquitous Robots (UR), pp. 566-570, Honolulu, USA, Jun. 2023*.
- Hyungtae Lim, Daebeom Kim, Beomsoo Kim, and Hyun Myung†. "AdaLIO: Robust Adaptive LiDAR-Inertial Odometry in Degenerate Indoor Environments". *in Proc. The 20th International Conference on Ubiquitous Robots (UR), pp. 48-53, Honolulu, USA, Jun. 2023*.
- Hyungtae Lim, Kawon Han, Gunhee Shin, Giseop Kim, Songcheol Hong, and Hyun Myung†. "ORORA: Outlier-Robust Radar Odometry". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 2046-2053, London, UK, May 2023*.
- I Made Aswin Nahrendra, Byeongho Yu, and Hyun Myung†. "DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 5078-5084, London, UK, May 2023*.
- 이승현, 최덕규, 박재헌, 명현. "쿼드로터를 위한 외란에 강인한 적응형 모델 예측 제어기 개발". *in Proc. 제어로봇시스템학회 대전충청지부 학술대회 (ICROS 2023), 대전 라미컨벤션웨딩, Dec. 2023*.
- 이현우, I Made Aswin Nahrendra, 이승현, 이동규, 노승규, 명현. "심층강화학습을 활용한 사족보행 로봇 제어기의 보행 속도 적응적 보행 패턴 개발". *in Proc. 제어로봇시스템학회 대전충청지부 학술대회 (ICROS 2023), 대전 라미컨벤션웨딩, Dec. 2023*.
- 유병호, 김예은, 전진우, 명현. "시각적 특징점을 지면 정보로 보정하는 보행 로봇 상태 추정기". *in Proc. 제 3회 국방로봇학회, 정부세종컨벤션센터, Dec. 2023*.
- 신성재, 명현. "멀티 카메라를 이용한 파노라마 영상 루프 탐지". *in Proc. 제 38회 제어로봇시스템학회 학술대회 (ICROS 2023), 삼척 쏠비치, Jun. 2023*.
- 성창기, 명현. "이미지 프로세싱 모폴로지 연산 및 딥러닝을 활용한 3차원 점군지도의동적 물체 제거 방법". *in Proc. 제 38회 제어로봇시스템학회 학술대회 (ICROS 2023), 삼척 쏠비치, Jun. 2023*.
- 김예은, 명현. "모바일 기기를 위한 특징점 및 특징선 기반의 SLAM 알고리즘 개발". *in Proc. 제 38회 제어로봇시스템학회 학술대회 (ICROS 2023), 삼척 쏠비치, Jun. 2023*.
- 이응창, I Made Aswin Nahrendra, 최준호, 이승현, 명현. "전장 상황에서의 무인 정찰을 위한 자율 비행 드론". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023) RED Show, 평창 휘닉스파크, Feb. 2023*.
- 김태완, 유병호, Christian Tirtawardhana, I Made Aswin Nahrendra, 명현. "고층 빌딩 페인팅을 위한 미래 드론형 벽면등반로봇 (CAROS-P)". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023) RED Show, 평창 휘닉스파크, Feb. 2023*.
- 이준, 이준석, 최덕규, 명현. "B2Bot: Biomimetic Beetle Robot Capable of Walking and Flying". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023) RED Show, 평창 휘닉스파크, Feb. 2023*.
- 성창기, 장서연, 명현. "3차원 점군 지도를 이용한 자율주행 자동차 위치 추정을 위한 정밀 지도 갱신 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 김예은, 유병호, 전진우, 명현. "보행로봇의 관절 및 관성 정보 학습 기반의 위치 추정 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 최준호, 정명우, 명현. "UWB-Odometry 융합을 통한 최적화 기반 다중 무인 비행체 상대 위치 추정 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 이승재, 임형태, 명현. "다양한 분포의 3 차원 포인트 클라우드를 위한 지면 추출 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 송원호, 오민호, 이현우, 김태완, 김재경, 박정희, 명현. "지상 야지환경에서의 센서융합 위치인식 및 위성지도 기반 통합 자율주행". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 이우주, 홍다솔, 이인균, 명현. "이미지를 강인하게 인식하는 보조 노이즈 전파 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 이응창, 명현. "3 차원 복원을 위한 2 단계 최적화 기반 에너지 효율적 커버리지 경로계획법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 임현준, 명현. "특징선 기반 SLAM을 위한 소실점 정보의 Loss 함수 개발". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 최덕규, 명현. "신뢰 거리 기반 공간 분할을 활용한 UAV 탐사 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 현지음, 명현. "NLOS 상황에서 UWB-VIO 융합을 통한 로봇의 위치 추정 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 서동욱, 신성재, 명현. "Surfel 기반 깊이 이미지 업데이트를 통한 동적물체 제거 맵 생성 기법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 이준호, 송승원, 명현. "Event-RGB 융합을 기반으로 한 강건한 장소 인식 방법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.
- 이동규, 이승현, 명현. "실시간 3차원 건물 모델링을 위한 frontier 기반 경로 계획법". *in Proc. 제 18회 한국로봇종합학술대회 (KRoC 2023), 평창 휘닉스파크, Feb. 2023*.

**2022**

- Seungwon Song, Hyungtae Lim, Alex Junho Lee, and Hyun Myung†. "DynaVINS: A Visual-Inertial SLAM for Dynamic Environments". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.4, pp.11523-11530, Oct. 2022*.
- I Made Aswin Nahrendra, Christian Tirtawardhana, Byeongho Yu, EungChang Lee, and Hyun Myung†. "Retro-RL: Reinforcing Nominal Controller with Deep Reinforcement Learning for Tilting-Rotor Drones". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.4, pp.9004-9011, Oct. 2022*.
- Minho Oh, Euigon Jung, Hyunhtae Lim, Wonho Song, Sumin Hu, EungChang Lee, JungHee Park, Jaekyung Kim, Jangwoo Lee, and Hyun Myung†. "TRAVEL: Traversable Ground and Above-Ground Object Segmentation Using Graph Representation of 3D LiDAR Scans". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.3, pp.7255-7262, Jul. 2022. (RA-L Best Paper Award)*.
- Jinwoo Jeon, Hyunjun Lim, Dong-Uk Seo, and Hyun Myung†. "Struct-MDC: Mesh-Refined Unsupervised Depth Completion Leveraging Structural Regularities from Visual SLAM". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.3, pp.6391-6398, Jul. 2022*.
- Alex Junho Lee, Younggun Cho, Young-Sik Shin, Ayoung Kim, and Hyun Myung†. "ViViD++: Vision for Visibility Dataset". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.3, pp.6282-6289, Jul. 2022*.
- Yeeun Kim\*, Byeongho Yu\*, Eungchang Mason Lee, Joon-ha Kim, Hae-won Park, and Hyun Myung†. "STEP: State Estimator for Legged Robots Using a Preintegrated Foot Velocity Factor". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.2, pp.4456 - 4463, Apr. 2022*.
- Hyunjun Lim, Jinwoo Jeon, and Hyun Myung†. "UV-SLAM: Unconstrained Line-based SLAM Using Vanishing Points for Structural Mapping". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.2, pp.1518 - 1525, Apr. 2022*.
- Changki Sung, Seulgi Jeon, Hyungtae Lim, and Hyun Myung†. "What If There Was No Revisit? Large-Scale Graph-based SLAM with Traffic Sign Detection in an HD Map Using LiDAR Inertial Odometry". *Journal of Intelligent Service Robotics, vol.15, no.2, pp.161–170, Apr. 2022*.
- Seungwon Song, Hyungtae Lim, Sungwook Jung, and Hyun Myung†. "G2P-SLAM: Generalized RGB-D SLAM Framework for Mobile Robots in Low-Dynamic Environments". *IEEE Access, vol.10, pp.21370 - 21383, Feb. 2022*.
- Hyungtae Lim, Han-seok Ryu, Matthew Rhudy, Dongjin Lee, Dongjin Jang, Changho Lee, Youngmin Park, Wonkeun Youn, and Hyun Myung†. "Deep Learning-aided Synthetic Airspeed Estimation of UAVs for Analytical Redundancy with a Temporal Convolutional Network". *IEEE RA-L (Robotics and Automation Letters), vol.7, no.1, pp. 17-24, Jan. 2022*.
- Alex Junho Lee, Wonho Song, Byeongho Yu, Duckyu Choi, and Hyun Myung†. "사회 기반 시설물 점검을 위한 로봇 기술 리뷰". *제어로봇시스템학회지 , vol.28, no.3, pp.37-46, Sep. 2022*.
- Junseok Lee, Christian Tirtawardhana, and Hyun Myung†. "Performance Verification of Biomimetic Mole Robot (Mole-bot) for Efficient Underground Exploration". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 321-330, Gold Coast, Australia, Dec. 2022*.
- Taewan Kim, Christian Tirtawardhana, Byeongho Yu, I Made Aswin Nahrendra, Seoktae Kim, and Hyun Myung†. "Development of Perching and Fail-safe Module for Wall Climbing Multi-copter". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 235-244, Gold Coast, Australia, Dec. 2022*.
- Dongkyu Lee, EungChang Mason Lee, Hyungtae Lim, Seungwon Song, and Hyun Myung†. "FARO-Tracker: Fast and Robust Target Tracking System for UAVs in Urban Environment". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 226-234, Gold Coast, Australia, Dec. 2022*.
- Myeongwoo Jeong, Junho Choi and Hyun Myung†. "Low-Cost UWB-Based Relative Position Estimation for Cyber Physical Multi-Robot System". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 99-106, Gold Coast, Australia, Dec. 2022*.
- Eungchang Mason Lee, Sungwook Jung, Seungwon Song, Duckyu Choi, Dongkyu Lee, Seunghyun Lee, Seoktae Kim, and Hyun Myung†. "CEO-MLCPP: Collision-Efficient and Obstacle-Aware Multi-Layer Coverage Path Planner for 3D Reconstruction with UAVs". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 27-36, Gold Coast, Australia, Dec. 2022*.
- Wooju Lee and Hyun Myung†. "Parametric Surround modulation improves the robustness of the deep neural networks". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 282-291, Gold Coast, Australia, Dec. 2022*.
- Samyeul Noh and Hyun Myung†. "Toward Effective Deep Reinforcement Learning for 3D Robotic Manipulation: Multimodal End-to-End Reinforcement Learning from Visual and Proprioceptive Feedback". *in Proc. 36th Conference on Neural Information Processing Systems (NeurIPS 2022) Workshop, New Orleans, USA, Dec. 2022*.
- Taewan Kim , Byeongho Yu , Christian Tirtawardhana , I Made Aswin Nahrendra , and Hyun Myung†. "Development of Cleaning Module for Wall Climbing Drone with Bio-inspired Watering Mechanism". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1432-1436, Busan, Korea, Nov. 2022*.
- Byeongho Yu , Yeeun Kim , Jinwoo Jeon , I Made Aswin Nahrendra , and Hyun Myung†. "A Robust State Estimator for Legged Robots using Visual-Inertial-Leg Kinematics in the Wild". *in Proc. International Conference on Control, Automation and System (ICCAS), Busan, Korea, Nov. 2022*.
- Jieum Hyun and Hyun Myung†. "Pose-Graph-Based UWB SLAM with NLOS Factor Estimation". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 120-122, Busan, Korea, Nov. 2022*.
- Duckyu Choi and Hyun Myung†. "Conversion of mesh map using surface parameterization for 3D coverage path planner". *in Proc. International Conference on Control, Automation and System (ICCAS), Busan, Korea, Nov. 2022*.
- Junho Choi, Eungchang Lee, Myeongwoo Jeong, Duckyu Choi, and Hyun Myung†. "Range-only Relative Position Estimation for Multi-UAV". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1984-1989, Busan, Korea, Nov. 2022*.
- Alex Junho Lee , Hyungtae Lim , Minho Oh , Wonho Song, and Hyun Myung†. "Volumetric Vegetation Monitioring from LiDAR Scans with Ground Estimation". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 1378-1379, Busan, Korea, Nov. 2022*.
- Sumin Hu, Yeeun Kim, Hyungtae Lim, Alex Junho Lee, and Hyun Myung†. "eCDT: Event Clustering for Simultaneous Feature Detection and Tracking". *in Proc. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 3808-3815, Kyoto, Japan, Oct. 2022*.
- I Made Aswin Nahrendra, Christian Tirtawardhana, Byeongho Yu, EungChang Lee, and Hyun Myung†. "Retro-RL: Reinforcing Nominal Controller with Deep Reinforcement Learning for Tilting-Rotor Drones". *in Proc. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9004-9011, Kyoto, Japan, Oct. 2022*.
- Jinwoo Jeon, Hyunjun Lim, Dong-Uk Seo, and Hyun Myung†. "Struct-MDC: Mesh-Refined Unsupervised Depth Completion Leveraging Structural Regularities from Visual SLAM". *in Proc. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 6391-6398, Kyoto, Japan, Oct. 2022*.
- Minho Oh, Euigon Jung, Hyungtae Lim, Wonho Song, Sumin Hu, EungChang Lee, JungHee Park, Jaekyung Kim, Jangwoo Lee, and Hyun Myung†. "TRAVEL: Traversable Ground and Above-Ground Object Segmentation using Graph Representation of 3D LiDAR Scans". *in Proc. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 7255-7262, Kyoto, Japan, Oct. 2022*.
- Seungjae Lee, Hyungtae Lim, and Hyun Myung†. "Patchwork++: Fast and Robust Ground Segmentation Solving Partial Under-Segmentation Using 3D Point Cloud". *in Proc. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 13276-13283, Kyoto, Japan, Oct. 2022*.
- Dongki Noh, JunHo Choi, Jeongsik Choi, Dasol Byun, Youngjae Kim, Hyoung-Rock Kim, Seungmin Baek, SeungHwan Lee, and Hyun Myung†. "MASS: Multi-Agent Scheduling System for Intelligent Surveillance". *in Proc. The 19th International Conference on Ubiquitous Robots (UR), pp. 252-257, Jeju, Korea, Jul. 2022*.
- Dongkyu Lee, EungChang Mason Lee, Duckyu Choi, Junho Choi, Christian Tirtawardhana, and Hyun Myung†. "M-BRIC: Design of Mass-driven Bi-Rotor with RL-based Intelligent Controller". *in Proc. The 19th International Conference on Ubiquitous Robots (UR), pp. 103-108, Jeju, Korea, Jul. 2022*.
- Dong-Uk Seo, Hyungtae Lim, Seungjae Lee, and Hyun Myung†. "PaGO-LOAM: Robust Ground-Optimized LiDAR Odometry". *in Proc. The 19th International Conference on Ubiquitous Robots (UR), pp. 1-7, Jeju, Korea, Jul. 2022*.
- Alex Junho Lee and Hyun Myung†. "Natural Language Representation as Features for Place Recognition". *in Proc. The 19th International Conference on Ubiquitous Robots (UR), pp. 284-287, Jeju, Korea, Jul. 2022*.
- Eungchang Mason Lee, Jinwoo Jeon, and Hyun Myung†. "TROT-Q: Traversability and Obstacle Aware Target Tracking System for Quadruped Robots". *in Proc. The 13th Asian Control Conference (ASCC 2022), pp. 2480-2484, Jeju, Korea, Jul. 2022*.
- Wooju Lee, and Hyun Myung†. "Adversarial Attack for Asynchronous Event-based Data". *in Proc. The 36th AAAI Conference on Artificial Intelligence (AAAI 2022), pp. 1237-1244, Virtual, Jun. 2022*.
- Alex Junho Lee, Younggun Cho, and Hyun Myung†. "Low-cost Thermal Mapping for Concrete Heat Monitoring". *in Proc. IEEE International Conference on Robotics and Automation (ICRA) Workshop, Philadelphia, USA, May 2022*.
- Yeeun Kim, Byeongho Yu, Eungchang Mason Lee, Joon-ha Kim, Hae-won Park, and Hyun Myung†. "STEP: State Estimator for Legged Robots Using a Preintegrated Foot Velocity Factor". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 4456-4463, Philadelphia, USA, May 2022*.
- Hyunjun Lim, Jinwoo Jeon, and Hyun Myung†. "UV-SLAM: Unconstrained Line-Based SLAM Using Vanishing Points for Structural Mapping". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 1518-1525, Philadelphia, USA, May 2022*.
- Hyungtae Lim, Suyong Yeon, Soohyun Ryu, Yonghan Lee, Youngji Kim, Jaeseong Yun, Euigon Jung, Donghwan Lee, and Hyun Myung†. "A Single Correspondence Is Enough: Robust Global Registration to Avoid Degeneracy in Urban Environments". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp. 8010-8017, Philadelphia, USA, May 2022*.
- Minho Oh, Hyungtae Lim, and Hyun Myung†. "Tri-Tzone: Tri-Grid Traversable Zone Segmentation based on Graph Searching Method using 3D LiDAR". *in Proc. The 13th Asian Control Conference (ASCC 2022) Poster, Jeju, Korea, May 2022*.
- 전진우, 임현준, 명현. "시각 SLAM 에서의 동적 특징점 검출을 통한 군집 로봇 내의 상대 위치 추정". *in Proc. 2022 한국군사과학기술학회 추계학술대회 Poster, 대전 컨벤션센터, Nov. 2022*.
- 신성재, 정광익, 임현준, 명현. "특징점이 부족한 실내 환경에서 영상 관성 초광대역 센서를 이용한 강인한 로봇 위치 추정". *in Proc. 제 2회 국방로봇학회, 대전 컨벤션센터, Sep. 2022*.
- 최덕규, 정성욱, 류서현, 명현. "유한 상태 기계를 활용한 점검 목적의 무인비행체 경로 추종 기법". *in Proc. 제 37회 제어로봇시스템학회 학술대회 (ICROS 2022), 거제 소노캄, Jun. 2022*.
- 송원호, 명현. "도로 객체의 특징선 기반 자율주행 차량 센서 자동 외부 보정". *in Proc. 제 37회 제어로봇시스템학회 학술대회 (ICROS 2022), 거제 소노캄, Jun. 2022*.
- 서동욱, 명현. "차선 기반의 슬라이딩 윈도우 후보군을 활용한 최적 경로 선택 시스템". *in Proc. 제 37회 제어로봇시스템학회 학술대회 (ICROS 2022), 거제 소노캄, Jun. 2022*.
- 임현준, 전진우, 명현. "시각 SLAM 을 이용한 군집 로봇의 상대 위치 추정". *in Proc. 2022 한국군사과학기술학회 종합학술대회 Poster, 제주 컨벤션센터, Jun. 2022*.
- 이준석, 임현준, Christian Tirtawardhana, 명현. "지하 탐사를 위한 생체모방형 두더지 로봇 (Mole-Bot)". *in Proc. 제 17회 한국로봇종합학술대회 (KRoC 2022) RED Show, 평창 휘닉스파크, May 2022*.
- 김예은, 유병호, 명현. "보행 로봇을 위한 다리기구학 기반 위치 인식". *in Proc. 제 17회 한국로봇종합학술대회 (KRoC 2022) Workshop, 평창 휘닉스파크, May 2022*.
- 이응창, 이동규, 임형태, 송승원, 명현. "무인 비행체를 위한 비균일 운동 목표물 추적 시스템". *in Proc. 제 17회 한국로봇종합학술대회 (KRoC 2022) Poster, 평창 휘닉스파크, May 2022*.

**2021**

- Jieum Hyun and Hyun Myung†. "NR-UIO: NLOS-Robust UWB-Inertial Odometry based on IMM and NLOS Factor Estimation". *Sensors, vol.21, no.23, pp. 7886 - 7902 , Nov. 2021*.
- Hyungyu Lee , Byeongho Yu, Christian Tirtawardhana, Chanyoung Kim, Myeongwoo Jeong, Sumin Hu, and Hyun Myung†. "CAROS-Q: Climbing Aerial RObot System Adopting Rotor Offset With a Quasi-Decoupling Controller". *IEEE RA-L (Robotics and Automation Letters), vol.6, no.4, pp.8490-8497, Oct. 2021*.
- Hyungtae Lim, Minho Oh, and Hyun Myung†. "Patchwork: Concentric Zone-based Region-wise Ground Segmentation with Ground Likelihood Estimation Using a 3D LiDAR Sensor". *IEEE RA-L (Robotics and Automation Letters), vol.6, no.4, pp.6458-6465, Oct. 2021*.
- Young-Min Kim, In-Ug Yoon, Hyun Myung, and Jong-Hwan Kim†. "Bi-Directional Convolutional Recurrent Reconstructive Network for Welding Defect Detection". *IEEE Access, vol.9, pp.135316 - 135325, Sep. 2021*.
- Wonkeun Youn, Hyungtae Lim, Hyoung Sik Choi, Matthew Rhudy, Hyeok Ryu, Sungyug Kim, and Hyun Myung†. "State Estimation of HALE UAV with Deep-learning-aided Virtual AOA/SSA Sensor for Analytical Redundancy". *IEEE RA-L (Robotics and Automation Letters), vol.6, no.3, pp.5276-5283, Jul. 2021*.
- Jinwoo Jeon\*, Sungwook Jung\*, Eungchang Lee, Duckyu Choi, and Hyun Myung†. "Corrections to “Run Your Visual-Inertial Odometry on NVIDIA Jetson: Benchmark Tests on a Micro Aerial Vehicle". *" IEEE RA-L (Robotics and Automation Letters), vol.6, no.3, pp.5840 - 5840, Jul. 2021*.
- Jinwoo Jeon\*, Sungwook Jung\*, Eungchang Lee, Duckyu Choi, and Hyun Myung†. "Run Your Visual-Inertial Odometry on NVIDIA Jetson: Benchmark Tests on a Micro Aerial Vehicle". *IEEE RA-L (Robotics and Automation Letters), vol.6, no.3, pp.5332-5339, Jul. 2021*.
- Hyun Myung† and Yang Wang. "Robotic Sensing and Systems for Smart Cities". *Sensors, vol.21, no.9, pp.2963, Apr. 2021*.
- Hyungtae Lim, Sungwon Hwang, and Hyun Myung†. "ERASOR: Egocentric Ratio of Pseudo Occupancy-based Dynamic Object Removal for Static 3D Point Cloud Map Building". *IEEE RA-L (Robotics and Automation Letters), vol.6, no.2, pp.2272-2279, Apr. 2021*.
- Sungwook Jung, Duckyu Choi, Seungwon Song, Hyun Myung†. "Autonomous Navigation System of an Unmanned Aerial Vehicle for Structural Inspection (무인 구조물 검사를 위한 자율 비행 시스템)". *Journal of Korea Robotics Society (in Korean), vol.16, no.3, pp.216-222, Jun. 2021*.
- Euigon Jung, Wonho Song, Hyun Myung†. "High-Definition Map-based Local Path Planning for Dynamic and Static Obstacle Avoidance (동적 및 정적 물체 회피를 위한 정밀 도로지도 기반 지역 경로 계획)". *Journal of Korea Robotics Society (in Korean), vol.16, no.2, pp.112-121, Jun. 2021*.
- Yeeun Kim, Hyunjun Lim, and Hyun Myung†. "Point and Line Feature-Based VIO for Mobile Devices". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 284-290, Virtual, KAIST, Korea, Dec. 2021. (Robot Intelligence Technology and Applications 6: Results from the 9th International Conference on Robot Intelligence Technology and Applications. Lecture Notes in Networks and Systems book series (LNNS, vol.429), pp. 284-290, Springer)*.
- KwangYik Jung, SungJae Shin, and Hyun Myung†. "U-VIO: Tightly Coupled UWB Visual Inertial Odometry for Robust Localization". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 272-283, Virtual, KAIST, Korea, Dec. 2021. (Robot Intelligence Technology and Applications 6: Results from the 9th International Conference on Robot Intelligence Technology and Applications. Lecture Notes in Networks and Systems book series (LNNS, vol.429), pp. 272-283, Springer)*.
- Seunghyun Lee, Sumin Chang, Eungchang Mason Lee, Junho Choi, Jinwoo Jeon, Seoktae Kim, and Hyun Myung†. "TPL: Trajectory Planner for Target Tracking in Low-Light Environments". *in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), pp. 12-23, Virtual, KAIST, Korea, Dec. 2021. (Robot Intelligence Technology and Applications 6: Results from the 9th International Conference on Robot Intelligence Technology and Applications. Lecture Notes in Networks and Systems book series (LNNS, vol.429), pp. 12-23, Springer)*.
- Sungwon Hwang, Hyungtae Lim, and Hyun Myung†. "Equivariance-bridged SO(2)-Invariant Representation Learning using Graph Convolutional Network". *in Proc. The 32nd British Machine Vision Conference (BMVC 2021), Virtual, Nov. 2021*.
- ChanYoung Kim, EungChang Mason Lee, JunHo Choi, Jinwoo Jeon, SeokTae Kim, and Hyun Myung†. "ROLAND: Robust Landing of UAV on Moving Platform using Object Detection and UWB based Extended Kalman Filter". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 249-254, Jeju, Korea, Oct. 2021*.
- Hyunjun Lim and Hyun Myung†. "Avoiding Degeneracy for Line-based Visual SLAM Using Vanishing Point Re-projection". *in Proc. International Conference on Control, Automation and System (ICCAS) Poster, Jeju, Korea, Oct. 2021*.
- EungChang Mason Lee, DongUk Seo, Jinwoo Jeon, and Hyun Myung†. "QR-SCAN: Traversable Region Scan for Quadruped Robot Exploration using Lightweight Precomputed Trajectory". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 957-961, Jeju, Korea, Oct. 2021*.
- Sungjae Shin, Eungchang Lee, Junho Choi, and Hyun Myung†. "MIR-VIO: Mutual Information Residual-based Visual Inertial Odometry with UWB Fusion for Robust Localization". *in Proc. International Conference on Control, Automation and System (ICCAS), pp. 91-96, Jeju, Korea, Oct. 2021. [The Best Poster Award]*.
- Euigon Jung and Hyun Myung†. "Efficient Trajectory Planning for Obstacle Avoidance in the Frenet Space based on High-Definition Map". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) Poster, Praque, Czech Republic, Sep. 2021*.
- Junseok Lee, Hyunjun Lim, Christian Tirtawardhana, and Hyun Myung†. "Experimental Validation of Compact Biomimetic Robot (Mole-Bot) for Subsurface Exploration". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) Poster, Praque, Czech Republic, Sep. 2021*.
- Seungwon Song and Hyun Myung†. "G2P-SLAM: Generalized Grouping and Pruning Method for RGB-D SLAM in Low-Dynamic Environments". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) Poster, Praque, Czech Republic, Sep. 2021*.
- Hyungyu Lee, Myeongwoo Jeong, Chanyoung Kim, Hyungtae Lim, Changgue Park, Sungwon Hwang, and Hyun Myung†. "Low-level Pose Control of Tilting Multirotor for Wall Perching Tasks Using Renforcement Learning". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9669-9676, Praque, Czech Republic, Sep. 2021*.
- Hyungtae Lim, Minho Oh, and Hyun Myung†. "Patchwork: Concentric Zone-based Region-wise Ground Segmentation with Ground Likelihood Estimation Using a 3D LiDAR Sensor". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 6458-6465, Praque, Czech Republic, Sep. 2021*.
- Eungchang Mason Lee, Junho Choi, Hyungtae Lim, and Hyun Myung†. "REAL: Rapid Exploration with Active Loop-Closing toward Large-Scale 3D Mapping using UAVs". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 4194-4198, Praque, Czech Republic, Sep. 2021*.
- Chanyoung Kim, Hyungyu Lee, Myeongwoo Jeong, and Hyun Myung†. "A Morphing Quadrotor that Can Optimize Morphology for Transportation". *in Proc. IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9683-9689, Praque, Czech Republic, Sep. 2021*.
- Wonho Song, Changki Sung, Euigon Jung, Minho Oh, and Hyun Myung†. "Extrinsic Calibration of LiDAR and Camera using Multiple Traffic Signs". *in Proc. 2021 World Congress on Advances in Nano, Bio, Robotics and Energy (ANBRE), Seoul, Korea, Aug. 2021*.
- Junho Choi, Eungchang Lee, Sungjae Shin, and Hyun Myung†. "Solving Geometric Constraints for Relative Position Estimation using UWB Sensors in Multi-Robot System". *in Proc. 2021 World Congress on Advances in Nano, Bio, Robotics and Energy (ANBRE), Seoul, Korea, Aug. 2021*.
- KwangYik Jung, YeEun Kim, HyunJun Lim, and Hyun Myung†. "ALVIO: Adaptive Line and Point Feature-based Visual Inertial Odometry for Robust Localization in Indoor Environments". *in Proc. The 8th International Conference on Robot Intelligence Technology and Applications (RiTA), Cardiff, UK (virtual), Aug. 2021. (Robot Intelligence Technology and Applications: Results from the 8th International Conference on Robot Intelligence Technology and Applications. Lecture Notes in Mechanical Engineering book series (LNME), pp.171-184, Springer)*.
- EungChang Mason Lee, Duckyu Choi, and Hyun Myung†. "Peacock Exploration: A Lightweight Exploration for UAV using Control-Efficient Trajectory". *in Proc. The 8th International Conference on Robot Intelligence Technology and Applications (RiTA), Cardiff, UK (virtual), Aug. 2021. [The Best Paper Award\](Robot Intelligence Technology and Applications: Results from the 8th International Conference on Robot Intelligence Technology and Applications. Lecture Notes in Mechanical Engineering book series (LNME), pp.136-146, Springer)*.
- Changki Sung, Seulgi Jeon, Hyungtae Lim, and Hyun Myung†. "What If There Were no Loops?: Large-Scale Graph-based SLAM with Traffic Sign Detection in an HD Map using LiDAR Inertial Odometry". *in Proc. International Conference on Ubiquitous Robots (UR), pp. 76-77, Gangneung, Gangwon-do, Korea, July 2021. [The Best Paper Award Finalist]*.
- Seungwon Song and Hyun Myung†. "Floorplan-based Localization and Map Update Using LiDAR Sensor". *in Proc. International Conference on Ubiquitous Robots (UR), pp. 30-34, Gangneung, Gangwon-do, Korea, July 2021*.
- Duckyu Choi, EungChang Mason Lee, and Hyun Myung†. "Online 3D Coverage Path Planning Using Surface Vector". *in Proc. International Conference on Ubiquitous Robots (UR), pp. 392-396, Gangneung, Gangwon-do, Korea, July 2021*.
- Jinwoo Jeon, Sungwook Jung, Eungchang Lee, Duckyu Choi, and Hyun Myung†. "Run Your Visual-Inertial Odometry on NVIDIA Jetson: Benchmark Tests on a Micro Aerial Vehicle". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp.14476-14483, Xi'an, China, May 2021*.
- Hyungtae Lim, Sungwon Hwang, and Hyun Myung†. "ERASOR: Egocentric Ratio of Pseudo Occupancy-based Dynamic Object Removal for Static 3D Point Cloud Map Building". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp.5446-5453, Xi'an, China, May 2021*.
- Hyunjun Lim, Yeeun Kim, Kwangik Jung, Sumin Hu, and Hyun Myung†. "Avoiding Degeneracy for Monocular Visual SLAM with Point and Line Features". *in Proc. IEEE International Conference on Robotics and Automation (ICRA), pp.11675-11681, Xi'an, China, May 2021*.
- 최준호, 이응창, 신성재, 명현. "GNSS 불가용 상황에서 UWB를 이용한 다중 로봇 간의 상대 위치 추정". *in Proc. 2021 한국군사과학기술학회 종합학술대회, 대전 컨벤션 센터, Nov. 2021*.
- 이준석, 임현준, Christian Tirtawardhana, 명현. "지하 및 우주 자원 탐사를 위한 두더지 생체모방 굴진 로봇(몰봇) 개발". *in Proc. 제 36회 제어로봇시스템학회 학술대회 (ICROS 2021), 여수 소노캄, June 2021*.
- 성창기, 명현. "3차원 라이다 센서를 이용한 표지판 추출 및 고정밀 지도 매칭". *in Proc. 제 36회 제어로봇시스템학회 학술대회 (ICROS 2021), 여수 소노캄, June 2021*.
- 현지음, 명현. "강결합 UWB-IMU 기반의 로봇 위치 인식". *in Proc. 제 36회 제어로봇시스템학회 학술대회 (ICROS 2021), 여수 소노캄, June 2021*.
- 이우주, 명현. "이미지를 강인하게 인식하는 중심주변 조절 기반 뉴럴 네트워크". *in Proc. 제 16회 한국로봇종합학술대회 (KRoC 2021), 평창 휘닉스파크, May 2021*.
- 현지음, 오택준, 명현. "NLOS 환경에서 강결합을 이용한 강인한 UWB-IMU 기반 위치 추정". *in Proc. 제 16회 한국로봇종합학술대회 (KRoC 2021), 평창 휘닉스파크, May 2021*.
- 신성재, 황성원, 명현. "Polar Histogram 매칭을 이용한 다중 로봇 상대 자세 추정 알고리즘". *in Proc. 제 16회 한국로봇종합학술대회 (KRoC 2021), 평창 휘닉스파크, May 2021*.
- 오택준, 정광익, 명현. "WiFi 와 자기장 신호를 이용한 대규모 공간에서의 그래프 기반 SLAM". *in Proc. 제 16회 한국로봇종합학술대회 (KRoC 2021), 평창 휘닉스파크, May 2021*.

## 특허

누리집 Patents 페이지의 네 구역에서 등록 특허는 등록일, 출원 특허는 출원일이 2021년 10월 13일 이후인 57건이다. Registered, Korea 12건, Registered, International 5건, Applied, Korea 32건, Applied, International 8건이고, 구역마다 날짜가 늦은 것부터 적었다. 각 줄 앞에 누리집의 구역 이름을 붙였고, 발명자·제목·번호·날짜 표기는 누리집 그대로다. 출원번호가 같은 12건은 출원 구역과 등록 구역에 함께 올라 있다.[^patents]

- 2026.06.30 · Registered, Korea: Hyun Myung, Marsim Kevin Christiansen, Minho Oh, Byeongho Yu, Seungjae Lee, "WALKING ROBOT AND POSITION ESTIMATION METHOD THEREOF (보행 로봇 및 보행 로봇의 위치추정 방법)," Korea, Application No.10-2024-0078852 (2024.06.18), Patent Reg. No.10-2986432 (2026.06.30)
- 2026.03.25 · Registered, Korea: Hyun Myung, Hyun Jun Lim, Yee Eun Kim, Byeong Ho Yu, Jinwoo Jeon, "Line-based SLAM using vanishing points for structural mapping (소실점을 이용한 특징선 기반 SLAM 시스템)," Korea, Application No.10-2022-0093369 (2022.07.27), Patent Reg. No.10-2945776 (2026.03.25)
- 2026.01.05 · Registered, Korea: Hyun Myung, Wonho Song, Changki Sung, Euigon Jung, Minho Oh, Sumin Hu, Jung-Hee Park, Jang-Woo Lee, Jea-Kyung Kim, "Sensor Calibration Apparatus using Multiple Traffic Signs and Method Thereof (다중 교통 표지를 사용한 센서 캘리브레이션 장치 및 방법)," Korea, Application No.10-2022-0073499 (2022.06.16), Patent Reg. No.10-2909781 (2026.01.05)
- 2025.10.24 · Registered, Korea: Hyun Myung, Sungwon Hwang, "Method and Apparatus for Learning Rotation Equivariant and Invariant Representation of Image using Graph Convolutional Network (그래프 합성곱 신경망 기반 이미지의 회전에 대한 등변 및 불변 표상 학습 방법 및 장치)," Korea, Application No.10-2022-0057319 (2021.12.29), Patent Reg. No.10-2878353 (2025.10.24)
- 2025.06.30 · Registered, Korea: Hyun Myung, Sungwon Hwang, Yun Soo Kim, Hyungtae Lim, "Visual Place Similarity Evaluation and Recognition Method and System with Convolutional Neural Network (합성곱 신경망 기반 장소 이미지 유사도 평가 및 장소 인식 방법 및 시스템)," Korea, Application No.10-2021-0191081 (2021.12.29), Patent Reg. No.10-2829355 (2025.06.30)
- 2025.04.15 · Registered, Korea: Hyun Myung, Yeeun Kim, Byeongho Yu, Jinwoo Jeon, "Robot State Estimation System and Method (로봇의 상태 추정 장치 및 방법)," Korea, Application No.10-2022-0168107 (2022.12.05), Patent Reg. No.10-2797722 (2025.04.15)
- 2024.12.18 · Registered, Korea: Hyun Myung, Hyungyu Lee, Myeongwoo Jeong, Chanyoung Kim, Hyungtae Lim, "Method and Apparatus for Controlling Low-level Pose of Tilting Multirotor for Wall Perching Tasks Using Reinforcement Learning (벽면 부착을 위한 틸팅 드론의 강화학습 기반 낮은 수준의 자세 제어 방법 및 장치)," Korea, Application No.10-2022-0054350 (2022.05.02), Patent Reg. No.10-2745541 (2024.12.18)
- 2024.12.18 · Registered, Korea: Hyun Myung, Byungho Yu, Hyungyu Lee, "Aerial Deformation Drone based on Quasi-Decoupling Controller for Wall-Perching and its Control Method (벽면 부착을 위한 준-탈동조화 제어기 기반의 공중 변형 드론 및 그 제어 방법)," Korea, Application No.10-2022-0099198 (2022.08.09), Patent Reg. No.10-2745542 (2024.12.18)
- 2024.08.19 · Registered, Korea: Hyun Myung, Jieum Hyun, Hwisung Park, "NLOS-Robust UWB-lnertial Odometry based on Interacting Multiple Model and NLOS Factor Estimation (UWB 및 관성 센서 기반의 로봇 위치 추정 장치 및 방법)," Korea, Application No.10-2022-0097492 (2022.08.04), Patent Reg. No.10-2697973 (2024.08.19)
- 2024.04.01 · Registered, Korea: Hyun Myung, Sungjae Shin, Kwangyik Jung, Eungchang Lee, Junho Choi, "Tightly Coupled UWB-Visual-Inertial Odometry for Robust Localization (이동 로봇 및 이의 위치 추정 방법)," Korea, Application No.10-2021-0154973 (2021.11.11), Patent Reg. No.10-2654852 (2024.04.01)
- 2023.11.07 · Registered, Korea: Hyun Myung, Hyongjin Kim, Seungwon Song, Jieum Hyun, Sunhyuk Hong, "Mobile robots and Localization method using fusion image sensor and multiple magnetic sensors (이미지 센서와 복수의 지자기 센서를 융합하여 위치 보정하는 이동 로봇 장치 및 제어 방법)," Korea, Application No.10-2019-0024283 (2019.02.28), Patent Reg. No.10-2601141 (2023.11.07)
- 2022.10.13 · Registered, Korea: Hyeon Myeong, Wan Cheol Myeong, "Wall-climbing Drone Using Auxiliary Arm and Method for Controlling Therefore (보조 암을 이용한 벽면 등반형 무인 항공기 및 그 제어 방법)," Korea, Application No.10-2020-0046129 (2020.04.16), Patent Reg. No.10-2456041 (2022.10.13)
- 2026.04.14 · Registered, International: Hyun Myung, Sungwon Hwang, "Method and Apparatus for Learning Rotation Equivariant and Invariant Representation of Image using Graph Convolutional Network (그래프 합성곱 신경망 기반 이미지의 회전에 대한 등변 및 불변 표상 학습 방법 및 장치)," US, Application No.17973408 (2022.10.25), Patent Reg. No.12602584 (2026.04.14)
- 2025.06.10 · Registered, International: Hyun Myung, Euigon Jung, Wonho Song, "High-Definition Map-Based Local Path Planning Method and Apparatus for Dynamic and Static Obstacle Avoidance (동적 및 정적 물체 회피를 위한 정밀 도로지도 기반 지역 경로 계획 방법 및 장치)," US, Application No.18101169 (2023.01.25), Patent Reg. No.12325445 (2025.06.10)
- 2024.09.03 · Registered, International: Hyun Myung, Hyongjin Kim, Seungwon Song, "Matching Method for Laser Scanner Considering Movement of Ground Robot and Apparatus Therefor (지상 로봇의 움직임을 고려한 강인한 레이저 스캐너 매칭 방법 및 그 장치)," US, Application No.17266520 (2021.02.05), Patent Reg. No.12080071 (2024.09.03)
- 2024.02.12 · Registered, International: Hyeon Myeong, Hyongjin Kim, Seungwon Song, Jieun Hyun, Soonhyuk Hong, "Mobile Robot Device for Correcting Position by Fusing Image Sensor and Plurality of Geomagnetic Sensors and Control Method (이미지 센서와 복수의 지자기 센서를 융합하여 위치 보정하는 이동 로봇 장치 및 제어 방법)," US, Application No.17055415 (2020.11.13), Patent Reg. No.12001218 (2024.02.12)
- 2023.11.08 · Registered, International: Hyeon Myung, Hyungjin Kim, Seung Won Song, "Strong Laser Scanner Matching Method And Apparatus Considering Movement of Ground Robot (지상 로봇의 움직임을 고려한 강인한 레이저 스캐너 매칭 방법 및 그 장치)," EU, Application No.19885755.9 (2021.02.09), Patent Reg. No.3882869 (2023.11.08)
- 2026.02.24 · Applied, Korea: Hyun Myung, WooJu Lee, Juhye Park, Youngwoo Seo, Seuguk Ahn, Dongwan Kang, "Global pose estimation system for autonomous vehicles and method thereof (자율주행 차량의 전역 포즈 추정 시스템 및 그 방법)," Application Number: 10-2026-0033863, Korea, 2026.02.24
- 2026.01.19 · Applied, Korea: Hyun Myung, I Made Aswin Nahrendra, Byeongho Yu, Minho Oh, Dongkyu Lee, Seunghyun Lee, Hyeonwoo Lee, Hyungtae Lim, "Obstacle-Aware Quadrupedal with Resilient Multi-Modal Reinforcement Learning (강건한 다중 모달 강화학습 기반의 장애물 인지형 사족보행 로봇 보행 제어)," Application Number: 10-2026-0010030, Korea, 2026.01.19
- 2025.12.24 · Applied, Korea: Hyun Myung, I Made Aswin Nahrendra, Seunghyun Lee, Dongkyu Lee, "Method And System For Versatile Legged Locomotion Adaptation of an Autonomous Mobile Entity Through Vision-Language Alignment (비전-언어 기반 정합을 통한 자율 이동체의 범용 다족 보행 적응 방법 및 시스템)," Application Number: 10-2025-0209045, Korea, 2025.12.24
- 2025.11.12 · Applied, Korea: Hyun Myung, Dasol Hong, Wooju Lee, "Method And Apparatus for Image Classification based on Vision-Language Model (시각-언어 모델 기반 영상 분류 방법 및 장치)," Application Number: 10-2025-0170761, Korea, 2025.11.12
- 2025.10.29 · Applied, Korea: Hyun Myung, Sungjae Shin, Wanhee Kim, Alvin Jinsung Choi, "Method And Apparatus for Constructing a Lightweight Database for Visual Localization Based on Gaussian Splatting (가우시안 스플래팅 기반 영상 위치 인식용 경량 데이터베이스 구축 방법 및 장치)," Application Number: 10-2025-0159588, Korea, 2025.10.29
- 2025.06.02 · Applied, Korea: Hyun Myung, Wonho Song, Minho Oh, Dongwan Kang, Seunguk Ahn, Youngwoo Seo, "Calibration method and computer program (캘리브레이션 방법 및 컴퓨터 프로그램)," Application Number: 10-2025-0072422, Korea, 2025.06.02
- 2025.05.29 · Applied, Korea: Hyun Myung, Minho Oh, Wonho Song, Dongkyu Lee, Seungjae Lee, Gunhee Shin, Jaeyoung Lee, Seunguk Ahn, Youngwoo Seo, "Terrain modeling method and computer program (지형 모델링 방법 및 컴퓨터 프로그램)," Application Number: 10-2025-0070563, Korea, 2025.05.29
- 2025.04.14 · Applied, Korea: Seok-Hyung Bae, Joon Hyub Lee, Siripon Sutthiwanna, Hyun Myung, Sungjae Shin, Taegyu Jin, "Immersive Prototyping for Robot Design with 3D Sketching and VR Acting in Reconstructed Workspace (복원된 작업공간 내 3D 스케칭 및 VR 액팅을 활용하는 로봇 디자인을 위한 몰입적 프로토타이핑)," Application Number: 10-2025-0048001, Korea, 2025.04.14
- 2025.04.02 · Applied, Korea: Hyun Myung, Dongkyu Lee, Byeongho Yu, Minho Oh, I Made Aswin Nahrendra, Jiwon Park, Taeyun Kim, "Traversal Risk Graph-based Robot Path Planning (이동 가능 위험도 그래프 기반의 로봇 경로 계획 방법)," Application Number: 10-2025-0042701, Korea, 2025.04.02
- 2025.01.21 · Applied, Korea: Hyun Myung, Junseok Lee, Taewan Kim, Jaewon Park, Jun Lee, "Robot Capable of Flying and Walking (비행 및 보행이 가능한 로봇)," Application Number: 10-2025-0008440, Korea, 2025.01.21
- 2024.06.18 · Applied, Korea: Hyun Myung, Marsim Kevin Christiansen, Minho Oh, Byeongho Yu, Seungjae Lee, "Walking Robot and Position Estimation Method Thereof (보행 로봇 및 보행 로봇의 위치추정 방법)," Application Number: 10-2024-0078852, Korea, 2024.06.18
- 2024.06.05 · Applied, Korea: Hyun Myung, Minho Oh, Byeongho Yu, Dongkyu Lee, Seoyeon Jang, I Made Aswin Nahrendra, "Method and Apparatus for Generating Terrain Map Considering Traversability of Robot (로봇의 이동 가능성을 고려한 지형 지도 생성 방법 및 장치)," Application Number: 10-2024-0073727, Korea, 2024.06.05
- 2023.12.04 · Applied, Korea: Hyun Myung, Marsim Kevin Christiansen, Minho Oh, Byeongho Yu, Seungjae Lee, "LiDAR-Visual-Inertial-Kinematic Tightly-coupled Odometry using Cross-Modality Feature Association for Legged Robots (상호 모듈의 특징점 연계성을 고려한 강 결합 방식의 3차원 라이다 센서, 이미지 센서, 관성 센서, 관절 역학기법 융합 기반의 보행 로봇의 자세 및 위치 추정 기술)," Application Number: 10-2023-0172956, Korea, 2023.12.04
- 2023.12.04 · Applied, Korea: Hyun Myung, Minho Oh, Byeongho Yu, Dongkyu Lee, Seoyeon Jang, I Made Aswin Nahrendra, "Traversability Terrain Mapping with Risk-Aware Prediction for Enhanced Online Quadruepd Robot Navigation (사족보행 로봇 항법의 향상을 위한 위험도 인식 기반의 이동 가능성을 고려한 지형 지도 생성)," Application Number: 10-2023-0173169, Korea, 2023.12.04
- 2023.08.23 · Applied, Korea: Hyun Myung, Seungwon Song, "Apparatus and method for estimating self-position robust to dynamic environment of camera system (카메라 시스템의 동적 환경에 강인한 자기 위치 추정 장치 및 그 방법)," Application Number: 10-2023-0110669, Korea, 2023.08.23
- 2023.07.28 · Applied, Korea: Hyun Myung, Seungwon Song, I Made Aswin Nahrendra, Junho Choi, Duckyu Choi, Seunghyun Lee, Eungchang Lee, "Drone unit for unmanned exploration and reconnaissance, autonomous flight system and the method thereof (무인 탐사 및 정찰을 위한 드론 유닛과, 드론 유닛의 자율 비행 시스템 및 그 방법)," Application Number: 10-2023-0099161, Korea, 2023.07.28
- 2023.07.10 · Applied, Korea: Hyun Myung, I Made Aswin Nahrendra, Byeongho Yu , "Learning Robust Legged Robot Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning (암시적 지형 정보 추론을 통한 심층 강화 학습 기반 보행로봇 보행 제어)," Application Number: 10-2023-0089039, Korea, 2023.07.10
- 2023.06.13 · Applied, Korea: Hyun Myung, Minho Oh, Wonho Song, Hyungtae Lim, Eungchang Lee, Euigon Jung, Sumin Hu, Jung-Hee Park, Chae Hyun Lee, Jae Kyung Kim, "Method and Apparatus for Recognizing a Moving Environment Based on Sensor Data (센서 데이터 기반의 이동 환경 인식 방법 및 그를 위한 장치)," Application Number: 10-2023-0075575, Korea, 2023.06.13
- 2023.04.27 · Applied, Korea: Hyun Myung, Euigon Jung, Wonho Song, "High-Definition Map-based Local Path Planning Method and Apparatus for Dynamic and Static Obstacle Avoidance (동적 및 정적 물체 회피를 위한 정밀 도로지도 기반 지역 경로 계획 방법 및 장치)," Application Number: 10-2023-0055277, Korea, 2023.04.27
- 2023.04.25 · Applied, Korea: Hyun Myung, Byeongho Yu, Christian Tirtawardhana, Eungchang Lee, I Made Aswin Nahrendra, "Method and apparatus for control of drone performing nominal control reinforcement based on deep reinforcement learning (심층 강화학습 기반의 공칭 제어 보강을 수행하는 드론 제어 방법 및 그 장치)," Application Number: 10-2023-0054096, Korea, 2023.04.25
- 2023.04.14 · Applied, Korea: Hyun Myung, Jinwoo Jeon, Hyunjun Lim, "Program for generating depth map based on neural network model using refined depth information of mesh (메쉬의 정제된 깊이 정보를 이용한 신경망 모델 기반의 깊이맵 생성 장치, 방법, 컴퓨터 판독 가능한 기록 매체 및 컴퓨터 프로그램)," Application Number: 10-2023-0049589, Korea, 2023.04.14
- 2022.12.05 · Applied, Korea: Hyun Myung, Yeeun Kim, Byeongho Yu, Jinwoo Jeon, "Robot State Estimation System and Method (로봇의 상태 추정 장치 및 방법)," Application Number: 10-2022-0168107, Korea, 2022.12.05
- 2022.11.17 · Applied, Korea: Hyun Myung, and Seungwon Song, "Method and Apparatus for Estimating Position of Mobile Robot and Generating Static Environment Map in Environment in Which High-Dynamic Object and Low-Dynamic Object Exist (고-동적 물체 및 저-동적 물체가 존재하는 환경에서의 이동 로봇의 위치 추정 및 정적 환경 지도 생성 방법 및 장치)," Application Number: 10-2022-0154103, Korea, 2022.11.17
- 2022.08.09 · Applied, Korea: Hyun Myung, Byungho Yu, Hyungyu Lee, "Aerial Deformation Drone based on Quasi-Decoupling Controller for Wall-Perching and its Control Method (벽면 부착을 위한 준-탈동조화 제어기 기반의 공중 변형 드론 및 그 제어 방법)," Application Number: 10-2022-0099198, Korea, 2022.08.09
- 2022.08.04 · Applied, Korea: Hyun Myung, Jieum Hyun, Hwisung Park, "Apparatus and Method for Estimating Robot Position based on UWB and Inertial Odometry (UWB 및 관성 센서 기반의 로봇 위치 추정 장치 및 방법)," Application Number: 10-2022-0097492, Korea, 2022.08.04
- 2022.07.27 · Applied, Korea: Hyun Myung, Hyun Jun Lim, Yee Eun Kim, Byeong Ho Yu, Jinwoo Jeon, "Line-feature-based SLAM System using Vanishing Points (소실점을 이용한 특징선 기반 SLAM 시스템)," Application Number: 10-2022-0093369, Korea, 2022.07.27
- 2022.06.16 · Applied, Korea: Hyun Myung, Wonho Song, Changki Sung, Euigon Jung, Minho Oh, Sumin Hu, Jung-Hee Park, Jang-Woo Lee, Jea-Kyung Kim, "Sensor Calibration Apparatus using Multiple Traffic Signs and Method Thereof (다중 교통 표지를 사용한 센서 캘리브레이션 장치 및 방법)," Application Number: 10-2022-0073499, Korea, 2022.06.16
- 2022.05.31 · Applied, Korea: Hyun Myung, Euigon Jung, Wonho Song, "High-Definition Map-based Local Path Planning Method and Apparatus for Dynamic and Static Obstacle Avoidance (동적 및 정적 물체 회피를 위한 정밀 도로지도 기반 지역 경로 계획 방법 및 장치)," Application Number: 10-2022-0067049, Korea, 2022.05.31
- 2022.05.10 · Applied, Korea: Hyun Myung, Sungwon Hwang, "Method and Apparatus for Learning Rotation Equivariant and Invariant Representation of Image using Graph Convolutional Network (그래프 합성곱 신경망 기반 이미지의 회전에 대한 등변 및 불변 표상 학습 방법 및 장치)," Application Number: 10-2022-0057319, Korea, 2022.05.10
- 2022.05.02 · Applied, Korea: Hyun Myung, Hyungyu Lee, Myeongwoo Jeong, Chanyoung Kim, Hyungtae Lim, "Method and Apparatus for Controlling Low-level Pose of Tilting Multirotor for Wall Perching Tasks Using Reinforcement Learning (벽면 부착을 위한 틸팅 드론의 강화학습 기반 낮은 수준의 자세 제어 방법 및 장치)," Application Number: 10-2022-0054350, Korea, 2022.05.02
- 2021.12.29 · Applied, Korea: Hyeon Myeong, Sungwon Hwang, Yun Soo Kim, Hyungtae Lim, "Visual Place Similarity Evaluation and Recognition Method and System with Convolutional Neural Network (합성곱 신경망 기반 장소 이미지 유사도 평가 및 장소 인식 방법 및 시스템)," Application Number: 10-2021-0191081, Korea, 2021.12.29
- 2021.11.11 · Applied, Korea: Hyun Myung, Eungchang Lee, Junho Choi, Sungjae Shin, Kwangyik Jung, "Tightly Coupled UWB-Visual-Inertial Odometry for Robust Localization (이동 로봇 및 이의 위치 추정 방법)," Application Number: 10-2021-0154973, Korea, 2021.11.11
- 2026.04.17 · Applied, International: Hyun Myung, Sungjae Shin, Wanhee Kim, Alvin Jinsung Choi, "Method And Apparatus for Constructing Lightweight Visual Localization Database (가우시안 스플래팅 기반 영상 위치 인식용 경량 데이터베이스 구축 방법 및 장치)," Application Number: 19/650,553, US, 2026.04.17
- 2025.08.19 · Applied, International: Hyun Myung, Dongkyu Lee, Byeongho Yu, Minho Oh, I Made Aswin Nahrendra, Jiwon Park, Taeyun Kim, "Traversal Risk Graph-based Robot Path Planning (이동 가능 위험도 그래프 기반의 로봇 경로 계획 방법)," Application Number: 19303759, US, 2025.08.19
- 2024.12.03 · Applied, International: Hyun Myung, Marsim Kevin Christiansen, Minho Oh, Byeongho Yu, Seungjae Lee, "Walking Robot and Position Estimation Method Thereof (보행 로봇 및 보행 로봇의 위치추정 방법)," Application Number: 18966623, US, 2024.12.03
- 2024.12.03 · Applied, International: Hyun Myung, Marsim Kevin Christiansen, Minho Oh, Byeongho Yu, Seungjae Lee, "Walking Robot and Position Estimation Method Thereof (보행 로봇 및 보행 로봇의 위치추정 방법)," Application Number: 242171932, EPO, 2024.12.03
- 2024.07.25 · Applied, International: Hyun Myung, Seungwon Song, I Made Aswin Nahrendra, Junho Choi, Duckyu Choi, Seunghyun Lee, Eungchang Lee, "Drone unit for unmanned exploration and reconnaissance, autonomous flight system and the method thereof (무인 탐사 및 정찰을 위한 드론 유닛과, 드론 유닛의 자율 비행 시스템 및 그 방법)," Application Number: 18783703, US, 2024.07.25
- 2024.03.20 · Applied, International: Hyun Myung, I Made Aswin Nahrendra, Byeongho Yu, "Learning Robust Legged Robot Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning (암시적 지형 정보 추론을 통한 심층 강화 학습 기반 보행로봇 보행 제어)," Application Number: 18610285, US, 2024.03.20
- 2023.01.25 · Applied, International: Hyun Myung, Euigon Jung, Wonho Song, "High-Definition Map-Based Local Path Planning Method and Apparatus for Dynamic and Static Obstacle Avoidance (동적 및 정적 물체 회피를 위한 정밀 도로지도 기반 지역 경로 계획 방법 및 장치)," Application Number: 18101169, US, 2023.01.25
- 2022.10.25 · Applied, International: Hyun Myung, Sungwon Hwang, "Method and Apparatus for Learning Rotation Equivariant and Invariant Representation of Image using Graph Convolutional Network (그래프 합성곱 신경망 기반 이미지의 회전에 대한 등변 및 불변 표상 학습 방법 및 장치)," Application Number: 17973408, US, 2022.10.25

## 과제

누리집 Project 게시판 66건 가운데 수행 기간이 2021년 10월 13일 이후에 걸친 16건이다. 과제명·지원 기관·기간은 게시판 표기 그대로다.[^project]

- Development of robot technology for forest fire response in irregular mountainous areas (지원 KIRO; 기간 2025-07-01–2029-12-31)
- Development of an ultra-precision quantum navigation system for air, marine, and land platforms (지원 KAIST; 기간 2025-07-01–2027-12-31)
- Online calibration and SCLAM technology for radar, camera, and LiDAR sensors for autonomous vehicles (지원 LG Innotek; 기간 2025-06-02–2027-06-01)
- (Global TOP) Learning-based whole-body control for humanoid robots (지원 KIMM; 기간 2025-05-01–2030-04-30)
- Efficient visual information processing SW technology for high-speed interaction (지원 ETRI (IITP); 기간 2025-04-01–2028-12-31)
- 3D terrain map generation and update for excavators (지원 HD XiteSolution; 기간 2025-03-01–2025-10-31)
- Hanwha Aerospace-KAIST Autonomy Hub Center (지원 Hanwha Aerospace; 기간 2023-07-01–2026-06-30)
- An autonomous quadrupedal mobile manipulation system for rapid exploration and collaboration missions in disaster and industrial environments (지원 NRF; 기간 2025-05-01–2028-04-30)
- Development of a dexterous and agile humanoid robot for industrial environments (지원 KEIT; 기간 2024-01-01–2027-12-31)
- Visual SLAM for indoor autonomous navigation (지원 Samsung Elec.; 기간 2024-06-01–2025-05-31)
- Cooperative SLAM and Navigation for Multi-Robots in Large Scale Indoor Environments (지원 KEIT; 기간 2023-04-01–2026-12-31)
- Navigation & Control for Micro Swarm Robots (지원 KRIT (국기연); 기간 2022-01-01–2027-12-31)
- Deep Reinforcement Learning-Based Velocity-Adaptive Locomotion Controller for Quadrupedal Robots (지원 HD Keffico; 기간 2023-01-01–2023-11-30)
- Intelligent Drone System for Power Line Inspection (지원 KEPCO; 기간 2023-01-31–2024-09-30)
- Spatial Intelligence SW for Autonomous Navigation of Legged Robots in Dynamic and Atypical Environments (지원 KEIT; 기간 2022-04-01–2026-12-31)
- [AI28] Self-Improving AI for Changing Situation in Real World (지원 IITP; 기간 2022-01-01–2023-12-31)

## 수상

연구실 교수 소개 페이지 Awards 칸 가운데 ICCAS 2021(2021년 10월 12–15일) 항목부터 그 뒤의 35건이다. 교수 개인의 수상과 연구실 팀·학생의 수상이 함께 있으며, 상 이름과 날짜는 페이지 표기 그대로다.[^prof]

- 1st Place, VLNVerse (Vision-Language Navigation) Challenge, EMR (Embodied Multimodal Reasoning) Workshop, ECCV (European Conference on Computer Vision) 2026, Malmö, Sweden, Sep. 9, 2026.
- 2nd place, NaviTrace Challenge, OWN (Open-World Navigation) Workshop, RSS (Robotics: Science and Systems) 2026, Sydney, Australia, July 17, 2026.
- 1st Place Overall, NSS (Nothing Stands Still) Challenge, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026), June, 2026.
- 1st Place Overall, SLAM Category, HILTI x Trimble SLAM Challenge, IEEE International Conference on Robotics and Automation (ICRA 2026), June, 2026.
- Research Grand Prize (연구대상), KAIST Research Day, Apr. 28, 2026.
- Best Paper Award, ICCAS (Int’l Conf. Control, Automation, and Systems), Songdo, Incheon, Nov. 6, 2025.
- Best Paper Award by KFMES, ICROS’25 Annual Conference, Jeonju, June 26, 2025.
- 1st Place Overall, NSS (Nothing Stands Still) Challenge, IEEE International Conference on Robotics and Automation (ICRA)’25, 2025.
- 2nd Place, The 3rd QRC (Quadruped Robot Challenge), IEEE International Conference on Robotics and Automation (ICRA)’25, Atlanta, USA, 2025.
- KAIST Proud Alumni Award (KAIST 자랑스러운 동문상), KAIST Alumni Association (KAIST 총동문회), Jan. 17, 2025.
- IJCAS Best Senior Editor Award 2024, IJCAS (Int’l Journal of Control, Automation, and Systems), Jan. 10, 2025.
- Grand Prize, 2024 Technology Innovation Awards of College of Engineering (기술혁신 대상), KAIST, Dec. 17, 2024.
- The Hanbit Awards (한빛대상), Oct. 24, 2024.
- 2nd Place in Autonomous at the 2nd QRC (Quadruped Robot Challenge), IEEE ICRA’24, Yokohama, Japan, May 14-16, 2024.
- RED Show Award (RED Show 일반 부문 우수상), KRoC 2024, Feb. 23, 2024.
- KAIST Breakthroughs『Readers’ Choice Award』, Feb. 21, 2024.
- 2023 KAISTian of the Year Award, KAIST, Feb. 14, 2024.
- Best Paper Award, RiTA 2023 (The 11th International Conference on Robot Intelligence Technology and Applications), Xi’an Jiaotong-Liverpool University, Taicang, China, Dec. 6-8, 2023.
- 2023 KROS Academic Award (한국로봇학회 학술상), 한국로봇학회 (KROS), Dec. 1, 2023.
- 2023 IEEE Academic Activity Award (IEEE 학술활동상), ICROS (제어·로봇·시스템학회), Oct. 19, 2023.
- Champion, IEEE International Conference on Robotics and Automation (ICRA) Autonomous Quadruped Robot Challenge (QRC), May 29 – June 2, 2023.
- 1st Place Overall, LiDAR Single Session Category, IEEE International Conference on Robotics and Automation (ICRA)’23 HILTI SLAM Challenge, 2023.
- 1st Place in Academia, Vision-Only Single Session Category, IEEE International Conference on Robotics and Automation (ICRA)’23 HILTI SLAM Challenge, 2023.
- Best Paper Award, IEEE RA-L (Robotics and Automation Letters) 2022, June 1, 2023.
- Best poster award (포스터 일반 부문 우수논문상), “특징선 기반 SLAM을 위한 소실점 정보의 Loss 함수 개발,” KRoC 2023, Feb. 17, 2023.
- RED show award (RED Show 일반 부문 우수상), “전장 상황에서의 무인정찰을 위한 자율비행 드론,” KRoC 2023, Feb. 17, 2023.
- RED show award (RED Show 학부생 부문 우수상), “B2Bot Biomimetic Beetle Robot Capable of Walking and Flying,” KRoC 2023, Feb. 17, 2023.
- KAIST Research Prize (개교 52주년 기념 연구상), Feb. 6, 2023.
- KAIST Technology Innovation Award (기술혁신상), Dec. 22, 2022.
- CES (Consumer Electronics Show) 2023 Innovation Award, Robotics Field (with Hills Robotics), Nov. 17, 2022.
- 2022 Future Challenge Defense Technology Contest (2022년 미래도전 국방기술 경진대회 장려금 수상), Nov. 6, 2022.
- People of the Year Award, AI One Team SUMMIT 2022, Sofitel Ambassador Seoul, Oct. 25, 2022.
- 2nd CASH Prize (USD 3,000) in Academia, HILTI SLAM Challenge, Future of Construction Workshop, IEEE Int’l Conference on Robotics and Automation (ICRA), Philadelphia, USA, May 23-27, 2022.
- Excellence Award for RED (Robot Engineering & Design) Show, KRoC (Korea Robotics Conference), Pyungchang, May 11-14, 2022.
- The Best Poster Award, ICCAS (Int’l Conf. Control, Automation, and Systems) 2021, Jeju, Korea, Oct. 12-15, 2021.

## 소식

누리집 Announcement 게시판과 Media Release 게시판에 2021년 10월 13일 이후 오른 글 91건이다(2021년 10월 25일–2026년 10월 3일). 날짜는 게시일이고 제목은 게시판 표기 그대로다.[^news]

- 2026-10-03 · 1st Place in COMFORT Localization Challenge @ IROS'26
- 2026-09-16 · 1st place in VLNVerse Challenge @ ECCV'26
- 2026-08-21 · 2nd place in NaviTrace Challenge @ RSS 2026
- 2026-07-28 · [SBS documentary] Life of AI
- 2026-06-25 · Challenge Championships at ICRA'26 and CVPR'26
- 2026-04-29 · Prof. Myung wins KAIST Research Grand Prize
- 2026-04-13 · DreamWaQ++
- 2026-03-15 · Prof. Myung Wins Deputy Prime Minister and Minister of Science and ICT Award
- 2026-02-20 · [국민일보] 시사 뉴스 (Feb. 04, 2026)
- 2025-11-17 · AI Summit Seoul @ EXPO
- 2025-11-14 · ICCAS 2025 Best Paper Award
- 2025-11-01 · [KMatriX] Multiway registration framework for spatiotemporal environments
- 2025-10-13 · [LG CNS AX Fair 2025] Keynote
- 2025-09-16 · [URobotics] KAIST, 로봇창업 산실 ‘주목’
- 2025-09-16 · '즐거움 강연' 시리즈 개최
- 2025-09-08 · [MK News] URobotics
- 2025-07-30 · [KAISTian Newsletter] 2025 Spring & Summer
- 2025-06-28 · [ICROS'25] Best Paper Award (KFMES)
- 2025-05-30 · URL Team Wins First Place at NSS Challenge, ICRA'25
- 2025-05-13 · [MBC radio] 손에 잡히는 경제 (May 11, 2025)
- 2025-04-21 · Dr. Alex Junho Lee appointed to Sookmyung Women's University
- 2025-04-21 · [로봇신문] URobotics 소개
- 2025-03-20 · [뉴스1] 건설부동산 포럼 특별강연 (Mar.19, 2025)
- 2025-03-05 · [디지털타임스] (주)유로보틱스 소개
- 2025-01-15 · [AI, 세상을 뒤바꾸다] AI로 현실화된 '휴머노이드'
- 2025-01-13 · Prof. Myung received KAIST Proud Alumni Award
- 2025-01-13 · Prof. Myung wins IJCAS Best Senior Editor Award 2024
- 2024-11-27 · [MBN] 보고대회 (Nov. 26, 2024)
- 2024-11-19 · CNN's Tech for Good (Nov. 2024)
- 2024-10-09 · Prof. Myung receives the Hanbit Awards 2024
- 2024-07-18 · [UWC 2024] Plenary Talk
- 2024-07-04 · [ICROS 2024] Plenary Talk
- 2024-07-04 · [ICROS 2024] Best Paper Award (Jeewon Kim)
- 2024-06-17 · Team DreamTRIP won the 2nd place in the 2nd QRC Challenge
- 2024-05-21 · Dr. Lim selected as RSS 2024 PIONEERS
- 2024-05-01 · [MIT Technology Review] Apr. 30, 2024
- 2024-03-18 · [한국경제] MIT 꺾은 KAIST 보행 로봇…"밤새 AI 알고리즘 짠 결과"
- 2024-03-07 · [KRoC'24] RED Show Award
- 2024-02-26 · Readers' Choice Award (Feb. 2024)
- 2024-02-15 · Prof. Myung received the 2023 KAISTian of the Year Award
- 2024-02-15 · DreamStep team received KAIST Challenge Award
- 2024-02-03 · [IEEE Spectrum] Video Friday featuring the DreamRiser
- 2024-01-11 · KAISTian Newsletter (Autumn & Winter, 2023)
- 2023-12-20 · Mr. Byeongho Yu received KI Excellent Researcher Award
- 2023-12-12 · Best Paper Award in RiTA 2023
- 2023-12-10 · KAIST Researchers Introduce Quatro++
- 2023-12-06 · Prof. Myung Receives Academic Awards from Korea Robotics Society and ICROS
- 2023-11-16 · 인간의 뇌를 모방한 3차원 집적 뉴로모픽 반도체 개발​
- 2023-11-07 · Open KAIST
- 2023-11-06 · [ICROS] IEEE Academic Activity Award
- 2023-11-06 · [AICON'23] Invited Talk
- 2023-10-22 · Leaflet for 대덕특구50주년 기념 성과전시회
- 2023-10-22 · DreamWaQer in 대덕특구50주년 기념 전시회
- 2023-10-04 · DreamSTEP in KAIST Breakthrough (Aug. 2023)
- 2023-08-30 · DreamWaQ in KAIST TechFair (Aug. 30, 2023)
- 2023-08-07 · DreamSTEP aired in KBS (Aug. 1, 2023)
- 2023-08-01 · KROS AI/Robotics Summer School (Aug. 1, 2023)
- 2023-08-01 · Hanwha Aerospace-KAIST Autonomy Hub
- 2023-07-12 · DreamWalker appeared in InnovateKorea 2023
- 2023-06-15 · DreamSTEP team won championship at Quadruped Robot Challenge (ICRA'23)
- 2023-06-15 · 2022 IEEE RA-L Best Paper Award
- 2023-06-15 · ICRA'23 HILTI SLAM Challenge double championship
- 2023-04-04 · DreamWaQ appears in IEEE Spectrum Video Friday (Apr. 4, 2023)
- 2023-03-31 · Prof. Myung appointed as Distinguished Lecturer of IEEE VTS (2023-2025)
- 2023-03-30 · DreamWaQ media coverage (Mar. 30, 2023) / 드림워크 언론보도
- 2023-02-28 · Future Mobility Technology Workshop (Feb. 28, 2023)
- 2023-02-25 · [KOSEN PICK] 국가 안보와 인공지능 로봇 기술
- 2023-02-22 · Prof. Myung receives Research Prize 2023, KAIST
- 2023-02-22 · [KRoC 2023] Best poster & RED show awards
- 2023-02-22 · KRoC 2023 (한국로봇종합학술대회)
- 2023-02-22 · KRoC 2023 (한국로봇종합학술대회)
- 2022-12-27 · Prof. Myung received KAIST Technology Innovation Award (Dec. 2022)
- 2022-11-17 · KAIST & Hills Robotics receives CES 2023 Innovation Awards
- 2022-11-10 · 2022년 미래도전 국방기술 경진대회 수상
- 2022-10-27 · AI One Team "People of the Year" 2022
- 2022-09-27 · DX Korea 2022
- 2022-08-24 · Dr. Jongdae Jung appointed as a professor at Chungnam National University
- 2022-08-24 · Dr. Yu-Cheol Lee appointed as a professor at Korea Aerospace University
- 2022-08-09 · KRoC 2022 RED Show Award
- 2022-08-05 · [YTN Science] DocuSPrime (July 28, 2022)
- 2022-06-02 · KAIST, '2022 ICRA'서 열린 'HILTI SLAM Challenge' 2위 차지
- 2022-05-31 · KAIST URL Team wins the 2nd Prize among Academia in IEEE ICRA 2022 SLAM Challenge
- 2022-04-22 · [News] KT & KAIST developed indoor robot spatial AI (Apr. 14, 2022)
- 2022-03-12 · Molebot in YTN Docu S Prime
- 2022-01-07 · [ICCAS 2021] Best poster paper award
- 2021-11-25 · Seoul Future Mobility Show 2021
- 2021-11-24 · CAROS-Q in IEEE Spectrum (Nov. 19, 2021)
- 2021-11-15 · KBS 중견만리 (Nov. 14, 2021)
- 2021-11-03 · [HelloDD] KAIST '신세계' 열었다···휴보·두더지봇이 선보인 '과학+예술'
- 2021-11-03 · 2021 과학자 소통 포럼 (KIRD 주최)
- 2021-10-25 · K-Science Mentoring & Speech at DSF (Daejeon Science Festival) 2021

## 연락과 위치

- 주소: Urban Robotics Lab. (Room No. 3243, E3-2 Bldg.), School of Electrical Engineering, KAIST, 291 Daehak-ro Yuseong-gu, Daejeon 34141. 실험실은 E3-2 3245호(Experimental Lab I)와 KI빌딩 C304호(Experimental Lab II)다.[^contact]
- 전화: +82-42-350-7551/7651 (Staff office), 팩스 +82-42-350-3410[^contact]
- 교수실: 전기및전자공학부동(E3-2) 3236호, 연락처 7451[^eeprof]
- 교수 이메일: hmyung@kaist.ac.kr[^eeprof]
- 누리집 Recruit 게시판은 2026년 겨울 학부 인턴(2026년 12월–2027년 8월, 1명)을 모집하며, 석사·박사과정 진학을 바라는 학생에게 인턴 활동을 먼저 권한다.[^recruit]
[^p1]: E. M. Lee, K. C. Marsim, H. Myung, IEEE Robotics and Automation Letters 11, 922-929 (2026). <https://doi.org/10.1109/lra.2025.3634906> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Lim 외, H. Myung, The International Journal of Robotics Research 43, 685-715 (온라인 2023-11-02). <https://doi.org/10.1177/02783649231207654> 초록 기준.
[^p3]: S. Jang, A. J. Lee, I. M. A. Nahrendra, H. Myung, IEEE Robotics and Automation Letters 11, 4361-4368 (2026). <https://doi.org/10.1109/lra.2026.3665079> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: M. Oh 외, H. Myung, IEEE Robotics and Automation Letters 7, 7255-7262 (2022). <https://doi.org/10.1109/lra.2022.3182096> 초록 기준(arXiv 판).
[^p5]: D. Lee 외, H. Myung, IEEE Robotics and Automation Letters 10, 1736-1743 (2025). <https://doi.org/10.1109/lra.2024.3524912> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: I. M. A. Nahrendra 외, H. Myung, IEEE Transactions on Robotics 42, 819-836 (2026). <https://doi.org/10.1109/tro.2026.3653774> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Lee 외, H. Myung, IEEE Robotics and Automation Letters 6, 8490-8497 (2021). <https://doi.org/10.1109/lra.2021.3108489> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: W. Lee 외, H. Myung, 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 21981-21990 (2025). <https://doi.org/10.1109/cvpr52734.2025.02047> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 미래도시 로봇연구실 누리집 첫 화면 <https://urobot.kaist.ac.kr/> (Welcome, 연구 소개 슬라이드, Recent Announcement, Recent Publications, 2026-10-23 열람)
[^area]: 미래도시 로봇연구실 누리집 Research Area 페이지 <https://urobot.kaist.ac.kr/research_area/> (Introduction, Research Directions, 2026-10-23 열람)
[^first]: 미래도시 로봇연구실 누리집 The First Research 페이지 <https://urobot.kaist.ac.kr/first_research/> (SLAM, Localization, Control, Artificial Intelligence 연구 이름과 로봇 소개, 2026-10-23 열람)
[^nav]: 미래도시 로봇연구실 누리집 Research Area의 Navigation 페이지 <https://urobot.kaist.ac.kr/navigation/> (2026-10-23 열람)
[^pai]: 미래도시 로봇연구실 누리집 Research Area의 Physical AI 페이지 <https://urobot.kaist.ac.kr/physical_ai/> (2026-10-23 열람)
[^future]: 미래도시 로봇연구실 누리집 Research Area의 Future Robotics 페이지 <https://urobot.kaist.ac.kr/future_robotics/> (2026-10-23 열람)
[^project]: 미래도시 로봇연구실 누리집 Project 게시판 <https://urobot.kaist.ac.kr/project/> (목록 1–7쪽: 과제명, Funding, Period, 2026-10-23 열람)
[^dataset]: 미래도시 로봇연구실 누리집 Dataset 페이지 <https://urobot.kaist.ac.kr/dataset/> (2026-10-23 열람)
[^spinoff]: 미래도시 로봇연구실 누리집 Spin-off Company 페이지 <https://urobot.kaist.ac.kr/spin-off-company/> (2026-10-23 열람)
[^prof]: 미래도시 로봇연구실 누리집 교수 소개 페이지 <https://urobot.kaist.ac.kr/url_teams/prof-hyunmyung/> (직위, Biography, Education, Employment History, Awards, Professional Activities, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(명현) <https://ee.kaist.ac.kr/professor/16491/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-23 열람)
[^current]: 미래도시 로봇연구실 누리집 Current 페이지 <https://urobot.kaist.ac.kr/current/> (2026-10-23 열람)
[^alumni]: 미래도시 로봇연구실 누리집 Alumni 페이지 <https://urobot.kaist.ac.kr/alumni/> (2026-10-23 열람)
[^pubs]: 미래도시 로봇연구실 누리집 Papers 페이지 <https://urobot.kaist.ac.kr/publications_papers/> (페이지가 불러오는 논문 목록 자료; 목록 범위는 근거 페이지, 2026-10-23 열람)
[^patents]: 미래도시 로봇연구실 누리집 Patents 페이지 <https://urobot.kaist.ac.kr/patents/> (Registered, Korea; Registered, International; Applied, Korea; Applied, International 네 구역, 2026-10-23 열람)
[^news]: 미래도시 로봇연구실 누리집 Announcement 게시판 <https://urobot.kaist.ac.kr/announcement/>과 Media Release 게시판 <https://urobot.kaist.ac.kr/media-release/> (각 목록 1–5쪽, 2026-10-23 열람)
[^contact]: 미래도시 로봇연구실 누리집 Contact & Map 페이지 <https://urobot.kaist.ac.kr/contact_map/> (Directions, Postal Address, TEL, FAX, 2026-10-23 열람)
[^recruit]: 미래도시 로봇연구실 누리집 Recruit 게시판 글 「[2026 Winter] Early Intern Recruiting」 <https://urobot.kaist.ac.kr/recruit/?mod=document&uid=657> (2026-10-23 열람)

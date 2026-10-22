# 로봇지능 연구실 (RaiLab)

**KAIST 기계공학과 · 황보제민 교수**

- 분야: 강화학습으로 배우는 사족 보행 로봇 제어, 다리 로봇의 자율 항법과 전신 조작, 보행 로봇의 기계·전자 하드웨어 설계
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 보행·휴머노이드 로봇[^research][^robots][^p6], 강화학습[^research][^p2], 로봇 구동기·센서[^research][^robots], 로봇 항법·SLAM[^research][^p3], 제어 이론·제어 공학[^mepop][^research]
- 홈페이지: <https://railab.kaist.ac.kr/>
- 근거와 출처: [로봇지능 연구실 근거 페이지](railab-sources.md)

> 네 다리로 걷는 로봇을 직접 설계해 만들고, 강화학습으로 거칠거나 미끄럽거나 무른 지형을 지나는 보행 제어기를 개발하는 연구실이다. 다리 로봇이 스스로 갈 길을 정해 움직이는 자율 항법과, 다리 로봇이 몸 전체로 크고 무거운 물체를 다루는 조작도 연구한다. 연구실이 만든 사족 보행 로봇 RAIBO2는 2024년 11월 마라톤 대회에서 풀코스를 배터리 한 번 충전으로 완주했다.[^research][^robots][^news]

## 무엇을 연구하나

로봇지능 연구실(RaiLab)은 KAIST 기계공학과 황보제민 교수가 이끄는 연구실이다.[^me][^home] 기계공학과 교수 소개는 교수의 연구분야를 Legged robotics(다리로 걷는 로봇의 공학)와 Learning-based control(학습 기반 제어)로 적는다.[^mepop] 누리집 Research 페이지는 연구실의 핵심 연구를 학습 기반 제어(Learning-based Control), 자율 항법(Autonomous Navigation), 하드웨어 플랫폼(Hardware Platform)의 세 주제로 나누고, 하드웨어 플랫폼을 다시 기계 설계와 전기 설계로 나눈다.[^research]

Research 페이지는 다리 로봇이 자유도가 높고 복잡한 환경을 정확히 모델링하기 어려워 강건하고 안정된 제어기를 만들기 어렵다고 보고, 강화학습(reinforcement learning, 시행착오로 보상을 가장 크게 하는 행동을 배우는 기계학습 방법)으로 사족 보행 로봇이 거칠고 미끄럽고 무른(deformable) 지형을 지나도록 하는 보행 제어기를 개발해 왔다고 적는다.[^research] 연구실은 학습 알고리즘을 적용한 제어기를 실험하려고 로봇의 부품을 모두 직접 만들며, 모터·감속기·엔코더·모터 드라이버로 이루어진 구동 유닛과 전원 회로, 모터 드라이버 회로도 직접 설계한다.[^research] Robots 페이지는 연구실이 만든 사족 보행 로봇 RAIBO와 RAIBO 2, 바퀴 둘을 단 다리 로봇 RAIWAY, 연구실 자체 바퀴 로봇 RAICART, 그리고 연구에 쓰는 소형 사족 보행 로봇 Mini Cheetah를 소개한다.[^robots]

Projects 페이지는 진행 중인 주요 과제(important ongoing initiatives)로 휴머노이드 로봇, 자율 에이전트 설계, 징검돌 지형의 사족 보행, 대형 언어 모델을 쓴 로봇 환경 설계, 고속 시각 자율 시스템, 전신 조작의 여섯 과제를 소개한다. 지원 기관으로는 산업통상자원부(MOTIE), DRB, Samsung Research Funding & Incubation Center of Samsung Electronics, NAVER Cloud, 싱가포르 DSO National Laboratories, 한국연구재단(NRF)을 적는다.[^projects]

News 페이지에 따르면 연구실의 사족 보행 로봇 RAIBO2는 2024년 11월 17일 Sangju Gotgam Marathon에서 풀코스(42.195 km)를 배터리 한 번 충전으로 4시간 19분 52초에 완주했다. 16s10p 리튬 이온 배터리를 달았고, 최대 10도의 경사를 지났으며, 조종자, 카메라 담당, 관중 지원으로 이루어진 운영팀이 함께 로봇을 관리했고 구성원마다 10 km 구간을 맡았다. 누리집은 RAIBO2가 풀코스 마라톤을 완주한 첫 사족 보행 로봇이 되었다고 적는다.[^news] 이 로봇의 설계와 에너지 효율 분석은 2026년 Nature 논문으로 실렸다(대표 논문 6).[^p6]

## 주요 연구 주제

### 1. 강화학습으로 배우는 보행 제어 (Learning-based Control)

Research 페이지는 학습 기반 접근이 제어기의 강건성과 안정성을 높이고, 정확하지만 계산량이 큰 모델에 대한 의존을 줄여, 동적이고 예측하기 어려운 환경에서 실제로 쓰기에 알맞다고 적는다.[^research] 같은 페이지가 드는 연구실 논문은 다음과 같다.[^research]

- 보상(reward)을 최대화하면서 제약 조건(constraint)을 만족하도록 학습하는 강화학습 틀을 제안하고, 다리 로봇이 험한 지형을 지나도록 훈련하는 데 적용했다(IEEE T-RO 2024, 대표 논문 2).[^research][^p2]
- 모델 예측 제어(MPC, model predictive control, 로봇의 동역학 모델로 앞으로의 움직임을 예측하며 매 순간 입력을 계산하는 제어 방식)와 학습 알고리즘을 묶은 IFM(Imitating and Finetuning Model Predictive Control) 틀을 내놓았다. 모방 학습으로 제어기를 훈련한 뒤 심층 강화학습으로 다듬는 방식으로, 페이지는 시뮬레이션과 하드웨어 실험에서 거칠고 미끄러운 지면의 발 디딤 조정, 걸음 대칭성, 에너지 효율이 기존 방법에 비해 크게 나아졌다고 적는다(IEEE Robotics and Automation Letters 2023).[^research]
- 무른 지형의 접촉 모델을 써서 사족 보행 로봇이 모래 같은 무른 지형에서 빠르게 달리도록 학습했다(Science Robotics 2023, 대표 논문 1).[^research][^p1] Robots 페이지는 이 연구에서 RAIBO가 언덕, 계단, 모래를 포함한 여러 지형에서 민첩하고 강건한 보행을 보였다고 적는다.[^robots]
- 제어 정책과 상태 추정기(state estimator, 센서 값으로 로봇 몸통의 속도·자세 같은 상태를 계산하는 부분)를 함께 훈련하는 방법을 내놓았다(IEEE Robotics and Automation Letters 2022).[^research] Robots 페이지는 강화학습으로 훈련한 Mini Cheetah가 이 방법으로 아스팔트, 미끄러운 지형, 경사로 같은 여러 지형에서 빠르게 걸었다고 적는다.[^robots]

진행 중인 연구로는 가파른 경사와 흩어진 잔해가 있는 자연 환경을 시각 정보 없이 걷는 보행(blind locomotion)과, 징검돌을 건너는 동적 보행을 든다.[^research] 징검돌 지형의 사족 보행 연구는 Samsung Research Funding & Incubation Center of Samsung Electronics가 지원한다.[^projects] 상태 추정에서는 신경망이 추정한 몸통 속도와 발 접촉 확률을 칼만 필터의 측정값으로 쓰는 고유 감각 상태 추정 방법도 연구했다(대표 논문 8).[^p8] 논문 목록에는 서로 다른 몸 구조의 로봇에 맞춰 적응하는 보행 정책 학습(PolyMorph, 게재 승인), 300 kg을 넘는 유압 사족 보행 로봇의 강화학습 보행(대표 논문 7), 로봇 팔을 꼬리처럼 써서 빠르게 돌고 공중에서 자세를 바꾸고 균형을 잡는 학습(CASE 2025)도 있다.[^pubs][^p7]

### 2. 다리 로봇의 자율 항법 (Autonomous Navigation)

Research 페이지는 다리 로봇이 도시뿐 아니라 숲과 산 같은 자연 환경도 탐사할 수 있지만, 그런 환경을 스스로 다니려면 경로 계획에서 지형의 의미(무엇인지)와 기하(모양)를 함께 따지고, 경로 추종에서 로봇의 물리적 제약과 제어기 특성을 고려해야 해서 어렵다고 적는다.[^research] 연구실은 학습 기반 방법과 고전적 방법을 묶어 자율 항법 틀을 만들고 있으며, 이 틀은 주행 가능성 추정(traversability estimation), 효율적인 경로·동작 계획, 정밀한 경로 추종 알고리즘으로 이루어진다. 최종 목표는 실내외 자율 점검 같은 여러 작업에 쓸 수 있는 항법 시스템이다.[^research]

같은 페이지가 드는 논문은 비포장 야외 지형에서 로봇 주변을 잘라 낸 영상 조각으로 로봇의 미래 위치와 방향을 예측하는 Crop-LSTM(IEEE Robotics and Automation Letters 2024, 대표 논문 4)과, 사족 보행 로봇이 안전하게 다니도록 순방향 동역학 모델과 궤적 표본 추출기를 학습한 연구(Robotics: Science and Systems 2022)다.[^research][^p4] 논문 목록에는 1인칭 시점 영상(egocentric video)과 자동 주석 전략으로 지형의 의미적 주행 가능성을 학습한 연구(IEEE Robotics and Automation Letters 2024)와, 띄엄띄엄 놓인 발판과 복잡한 지형에서 사족 보행 로봇의 고속 제어와 항법을 다룬 연구(Science Robotics 2025, 대표 논문 3)도 있다.[^pubs][^p3]

Crop-LSTM 실험에 쓴 RAICART는 연구실이 만든 야외 항법용 바퀴 로봇이다. Robots 페이지는 크기를 Zed2 카메라 거치대를 포함해 770mm x 500mm x 480mm, 무게를 14kg으로 적고, 애커먼 조향으로 방향을 바꿔 곡선 구간에서 바퀴가 옆으로 미끄러지지 않게 하며, 모든 계산과 자료 수집을 소형 임베디드 컴퓨터 NVIDIA Jetson AGX Xavier에서 했다고 적는다.[^robots] Projects 페이지의 고속 시각 자율 과제(High-Speed Vision Autonomy)는 빠른 영상 처리를 위한 고속 시각 모듈과 시선 계획기(Gaze Planner), 여러 센서를 융합한 항법, 무너지기 쉬운 지형에서의 고속 보행을 개발하며, 싱가포르 DSO National Laboratories가 지원한다.[^projects]

### 3. 다리 로봇의 전신 조작과 로봇 팔

Research 페이지는 사족 보행 로봇이 몸 전체로 크고 무거운 물체를 다루게 하는 학습 기반 시스템을 연구실 논문으로 든다. 물체를 명시적으로 모델링하지 않으며, 최적화 기반 방법에 비해 계산 효율이 크게 높다고 적는다(IEEE Robotics and Automation Letters 2024, 대표 논문 5).[^research][^p5] 한국연구재단이 지원하는 전신 조작 과제(Whole Body Manipulation)는 구조화되지 않은 상황에서 즉각 반응하는 궤적 계획과 환경 조작을 연구한다.[^projects]

논문 목록에는 다리 달린 이동 조작 로봇의 동적 집어 옮기기(pick-and-place) 학습(IEEE Robotics and Automation Letters 2026), 부분 기구학 임베딩으로 걸으면서 조작하는 전신 동작을 학습한 PAKE(게재 승인), 사람의 작업을 위한 힘 있고 민첩한 휴머노이드 팔 RAIPAL(게재 승인), 강화학습을 쓴 다리 로봇 이동 조작(2023)이 있다.[^pubs] Projects 페이지의 휴머노이드 과제(Robust Humanoid Robots)는 민첩하게 움직이고 장애물을 피하며 두 팔로 자율 조작하는 휴머노이드 로봇을 개발하는 과제로, KAIST의 URL/DRCD/CLVR, MIT의 Biomemetic Robotics Lab(누리집 표기), Rainbow Robotics와 협력하고 산업통상자원부가 지원한다.[^projects]

### 4. 로봇 하드웨어: 기계 설계와 전기 설계 (Hardware Platform)

기계 설계에서 연구실은 여러 조건의 충격을 견디고 환경과 관계없이 강건하게 동작하는 RAIBO의 하드웨어를 만들었고, 모터, 감속기(motor reducer), 엔코더(encoder), 모터 드라이버로 이루어진 구동 유닛을 직접 설계한다.[^research] Research 페이지는 이 구동 유닛의 고유한 형태(form factor)가 동작 중 높은 효율을 내는 데 큰 역할을 한다고 적고, 관련 연구로 케이블로 힘을 전달하는 구동 방식 논문(IROS 2018)을 든다.[^research]

전기 설계에서는 충격 때 생기는 돌입 전류와 회생 제동을 다루는 전원 회로부터 출력이 크고 대역폭이 넓은 모터 드라이버까지 설계하며, 회로 설계, 아트워크(artwork, 인쇄 회로 기판의 배선 도면 작업), SMT, 시험을 모두 연구실 안에서 한다.[^research] Research 페이지는 이런 전력 전자와 로봇 시스템 이해를 바탕으로 로봇이 모터 성능의 극한 영역까지 쓰게 하고, 시뮬레이션과 실제 로봇 사이의 차이(sim-to-real gap)를 좁히는 데에도 기여하며, 부품 특성을 고려해 작은 크기에 출력이 크고 잡음이 적은 모터 드라이버를 만든다고 적는다.[^research]

Robots 페이지는 RAIBO 2를 험한 환경에서 오래 쓰도록 설계한 강건하고 에너지 효율이 높은 사족 보행 로봇으로 소개한다. 무게는 42 kg이고, 최대 6 m/s로 달리며, 최대 8시간 연속으로 동작한다. 모듈형 중공축 구동기(속이 빈 축을 쓰는 모듈 단위 관절 구동 장치)를 쓰고, 정비와 제작이 쉽도록 설계해 내구성과 효율이 중요한 산업 응용에 실용적이고 비용 효율적인 해법이라고 적는다.[^robots] RAIBO는 산업 점검·탐사·순찰 같은 실제 작업에 알맞은 중형 사족 보행 로봇으로, 힘 있는 모터 12개와 높은 주파수로 모터를 제어하는 내장 소프트웨어를 갖췄다.[^robots] News 페이지는 2023 Innovate Korea 행사에서 RAIBO가 20cm 높이의 계단을 빠르게 오르내리고 2m/s로 빠르게 걷는 시연을 했다고 적는다.[^news] RAIWAY는 험한 지형을 빠르게 주행하도록 설계한 바퀴 둘 달린 다리 로봇으로, 오프로드 바퀴와 강화학습 기반 제어로 거친 지형을 빠르게 넘는다.[^robots] RAIWAY 논문은 2026년 구역에 게재 승인 논문으로 올라 있다.[^pubs]

### 5. 설계 도구, 시뮬레이터와 언어 모델 과제

Research 페이지는 복잡한 관절 부품을 가진 로봇의 설계를 돕는 RobotSketch(ACM SIGGRAPH 2024 Emerging Technologies)를 연구실 논문으로 든다. 3차원 스케치, 인공지능이 만드는 움직임, 가상현실 검토로 다리 로봇 설계의 초기 개발 과정을 간소화하는 도구다.[^research] Projects 페이지의 자율 설계 과제(Revolutionizing Autonomous Design)는 가상현실과 인공지능으로 자율 에이전트의 형태·구조·움직임·상호작용을 빠르게 설계하고, 그 설계를 가상현실에서 시뮬레이션·체험·평가한 뒤 하드웨어 시제품으로 만드는 통합 시스템을 목표로 하며 DRB가 지원한다.[^projects] 언어 기반 환경 설계 과제(Language Driven Environment Design)는 대형 언어 모델을 로봇 환경 설계와 계획에 쓰는 연구로, NAVER Cloud가 후원한다.[^projects]

Software 페이지는 RaiSim Tech Inc.가 만든 로봇 시뮬레이션용 물리 엔진 RaiSim을 소개한다. 페이지는 RaiSim이 강체(rigid body, 힘을 받아도 모양이 변하지 않는다고 보는 물체)를 효율적으로 시뮬레이션하고, C++ 라이브러리로 STL과 Eigen에만 의존한다고 적는다.[^software] News 페이지의 웨비나 목록에는 「Locomotion Controller Training with Reinforcement Learning & RaiSim」(2021.01.19)이 있다.[^news]

## 대표 논문

누리집 Publications 목록의 2021–2026년 논문 가운데 황보제민 교수가 마지막 저자이고 1저자가 Members 페이지의 구성원 또는 졸업생인 논문에서, Research 페이지의 연구 주제와 전신 조작·상태 추정 연구에 고르게 여덟 편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [Learning quadrupedal locomotion on deformable terrain](https://doi.org/10.1126/scirobotics.ade2256) · Science Robotics | 시뮬레이션 기반 강화학습으로 만든 다리 로봇 제어 정책은 무르고 변형되는 지형, 특히 빠른 속도에서는 아직 쓰기 어렵다. 경험하지 못한 환경에서는 잘 동작하지 못하기 때문이다. 연구진은 아주 무른 해변 모래부터 단단한 아스팔트까지 여러 지형을 나타낼 수 있고 계산 효율이 높은 알갱이 매질(granular media) 모델을 강화학습용으로 만들고, 로봇이 발로 지형을 느끼면서 지형의 성질을 암묵적으로 알아내는 적응형 제어 구조를 더했다. 연구실이 자체 개발한 사족 보행 로봇 Raibo에 적용한 결과, 디딤 구간에 발이 모래에 완전히 묻히는데도 무른 해변 모래 위를 초속 3.03 m로 달렸고, 비닐 타일 바닥, 육상 트랙, 잔디, 무른 에어 매트리스에서도 달렸다.[^p1] | 1저자 S. Choi(Suyoung Choi), 마지막 저자 황보제민 (7명) |
| 2 | 2024 | [Not Only Rewards but Also Constraints: Applications on Legged Robot Locomotion](https://doi.org/10.1109/tro.2024.3400935) · IEEE Transactions on Robotics | 신경망 제어기를 모델 없는 강화학습으로 훈련하면 복잡한 로봇에서 좋은 성능을 내지만, 수많은 보상 항목을 만들고 알맞은 보상 계수를 정하는 보상 설계(reward engineering)에 많은 시간과 노력이 든다. 이 논문은 보상과 제약 조건을 함께 쓰는 강화학습 틀을 제안하고, 엔지니어가 의도를 제약으로 반영하도록 두 가지 제약 유형과 계산 부담이 적은 정책 최적화 알고리즘을 내놓았다. 모양과 물리적 특성이 다른 여러 다리 로봇이 험한 지형을 지나도록 보행 제어기를 훈련했고, 시뮬레이션과 실제 실험에서 보상 계수 하나만 조정해, 보상 설계를 크게 줄이고도 성능 좋은 제어기를 얻었다. 제약 조건은 해석하기 쉽고 일반화되어 설계 과정도 단순하고 직관적이 된다.[^p2] | 1저자 Y. Kim(Yunho Kim), 마지막 저자 황보제민 (8명) |
| 3 | 2025 | [High-speed control and navigation for quadrupedal robots on complex and discrete terrain](https://doi.org/10.1126/scirobotics.ads6192) · Science Robotics | 다리 로봇이 발 디딜 곳이 띄엄띄엄 있고 모양이 복잡한 환경을 빠르게 지나가기는 어렵다. 자유도가 높은 동역학과, 긴 시간 범위를 내다봐야 하는 볼록하지 않은(nonconvex) 최적화 문제 때문이다. 연구진은 계획 모듈과 추종 모듈로 이루어진 위계적 항법 파이프라인을 제안했다. 계획 모듈은 발 디딤 계획 후보를 표본으로 뽑아 최적화하면서, 미리 정한 판단 기준(휴리스틱)과 신경망으로 후보를 차례로 빠르게 걸러 물리적으로 가능한 계획을 찾고, 물리 시뮬레이션으로 굴려 보아 가장 좋은 계획을 고른다. 추종 모듈은 목표 발 디딤 위치를 정확히 밟도록 훈련하며, 훈련 중 목표 위치의 분포는 추종 모듈과 경쟁하며 학습하는 생성 모델이 준다. 연구실의 사족 보행 로봇 Raibo는 수직 벽 위를 달리고, 1.3 m 틈을 뛰어넘고, 징검돌 위를 초속 4 m로 달리고, 30° 경사로와 계단, 여러 크기의 상자가 가득한 지형을 자율적으로 지났다.[^p3] | 1저자 H. Kim(Hyeongjun Kim), 마지막 저자 황보제민 (8명) |
| 4 | 2024 | [Learning Vehicle Dynamics From Cropped Image Patches for Robot Navigation in Unpaved Outdoor Terrains](https://doi.org/10.1109/lra.2024.3371910) · IEEE Robotics and Automation Letters | 자율 이동 로봇이 포장되지 않은 야외를 안전하게 다니려면 차원이 높은 센서 자료에서 필요한 정보를 뽑아야 한다. 이전 연구는 전체 영상에서 전역 특징을 뽑는 데 성과를 냈지만 중요한 국소 정보를 잡기 어려웠다. 연구진은 로봇의 현재 위치 주변을 잘라 낸 영상 조각을 반복해서 받아 미래의 위치, 방향, 울퉁불퉁함을 예측하는 Crop-LSTM을 제안했다. 예측한 로봇 경로를 따라 2차원 영상 평면에서 해당 영상 조각에 주의를 기울여 국소 특징을 뽑으며, 이렇게 해서 로봇의 미래 궤적을 더 정확히 예측한다. 연구실의 바퀴 이동 로봇 Raicart로 비포장 야외에서 목표 지점까지 가는 항법을 시험해, RGBD 영상(색 영상과 깊이 영상을 함께 담은 영상)을 써서 험한 비포장 지형을 안전하고 강건하게 다니게 했다.[^p4] | 1저자 J. H. Lee(Jeong Hyun Lee), 마지막 저자 황보제민 (6명) |
| 5 | 2023 | [Learning Whole-Body Manipulation for Quadrupedal Robot](https://doi.org/10.1109/lra.2023.3335777) · IEEE Robotics and Automation Letters | 사족 보행 로봇이 몸 전체로 크고 무거운 물체를 다루게 하는 학습 기반 시스템이다. 위계적 제어 전략을 쓰며, 상호작용, 고유 감각(로봇이 자기 관절과 몸의 상태를 재는 감각), 지난 행동 기록에서 조작에 필요한 정보를 뽑아 신경망 안의 내부 표현(잠재 변수)에 담고, 로봇은 이 표현으로 물체의 성질을 따로 계산하지 않고 암묵적으로 알아차린다. 시뮬레이션에서는 여러 물체를 0.03 m와 5° 허용 오차 안에서 옮기고 돌려 놓는 성공률이 93.6%였고, 실제 실험에서는 무게 27 kg인 로봇이 물을 채운 19.2 kg 드럼과 무거운 물건을 채운 15.3 kg 플라스틱 상자를 다뤘다. 작고 가벼운 물체를 쥐어서 다루던 이전 연구와 달리, 쥘 수 없는 크고 무거운 물체를 몸 전체로 다루는 데 사족 보행 로봇을 쓸 가능성을 보였다. 물체를 명시적으로 모델링할 필요가 없고, 최적화 기반 방법에 비해 계산 효율이 크게 높다.[^p5] | 1저자 S. Jeon(Seunghun Jeon), 마지막 저자 황보제민 (5명) |
| 6 | 2026 | [A quadruped robot designed to complete a marathon on a single battery charge](https://doi.org/10.1038/s41586-026-11102-5) · Nature | 다리 로봇 제어가 발전하면서 재난 지역과 산악 지대의 구조 작업 같은 실제 쓰임이 넓어졌지만, 배터리 한 번 충전으로 갈 수 있는 거리가 짧아 실제로 쓰기 어렵다. 바퀴 로봇과 달리 사족 보행 로봇은 몸무게를 버티느라 관절에서 계속 에너지를 쓰고, 발이 땅에 닿았다 떨어지는 동안 운동 에너지를 잃는다. 연구진은 로봇 전체의 에너지 손실 모델을 분석해 에너지 효율이 높은 사족 보행 로봇 RAIBO2를 만들었다. 힘을 그대로 전달하는(force-transparent) 가벼운 기계 하드웨어, 저항이 낮은 모터 구동 회로, 에너지 소모가 적은 보행 정책으로 효율을 높였다. RAIBO2는 배터리 한 번 충전으로 풀코스 마라톤을 4시간 19분 52초에 완주했고, 총 이동 비용(cost of transport, 이동에 쓴 에너지를 무게와 이동 거리로 나눈 값) 0.25를 기록해 사람의 기준값 0.37보다 낮았다. 기존 사족 보행 로봇에 견주면 충전 한 번에 가는 거리가 세 배를 넘는다.[^p6] | 1저자 C. Lee(Choongin Lee), 마지막 저자 황보제민 (18명). 누리집 목록은 앞의 세 저자 이름 뒤에 *를 붙인다. |
| 7 | 2025 | [Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model](https://doi.org/10.1109/lra.2025.3623024) · IEEE Robotics and Automation Letters | 대형 유압 로봇은 제어 응답이 느리고 유체 동역학이 복잡해, 시뮬레이션에서 배운 제어를 실제 로봇으로 옮기기(sim-to-real) 어렵다. 여러 실린더가 서로 이어진 구조와 실린더마다 다른 유량 때문에 모든 관절을 자세히 시뮬레이션하기 어려워 강화학습에 쓰기 알맞지 않다. 연구진은 유압 동역학으로 움직임을 계산하는 해석적 구동기 모델을 제안했다. 이 모델은 구동기 12개의 관절 토크를 1 μs 미만에 예측해 강화학습 환경에서 빠르게 처리할 수 있고, 자료가 적은 상황에서 신경망 기반 구동기 모델에 견준 장점을 보였다. 이 모델로 강화학습한 보행 정책을 무게 300 kg을 넘는 유압 사족 보행 로봇 BeTheX-Q에 적용했고, 논문은 이를 무거운 유압 사족 보행 로봇에서 강화학습으로 안정되고 강건한 명령 추종 보행을 옮겨 낸 첫 사례라고 적는다.[^p7] | 1저자 M. Lee(Minho Lee), 마지막 저자 황보제민 (7명) |
| 8 | 2025 | [Legged Robot State Estimation with Invariant Extended Kalman Filter Using Neural Measurement Network](https://doi.org/10.1109/icra55743.2025.11127971) · 2025 IEEE International Conference on Robotics and Automation (ICRA) | 카메라 같은 시각 장치를 믿기 어려운 환경에서는 로봇이 자기 몸의 감각만으로 상태를 추정하는 고유 감각 상태 추정기가 꼭 필요하다. 이런 추정기는 전통적으로 발 접촉의 기구학만 측정값으로 쓰는 모델 기반 방식이었다. 연구진은 신경 측정 네트워크(NMN)를 훈련해 몸통의 선속도와 발 접촉 확률을 추정하고, 이를 불변 확장 칼만 필터(invariant extended Kalman filter, 움직임 모델의 예측과 측정값을 결합해 상태를 추정하는 칼만 필터의 한 형태)의 측정값으로 쓰는 상태 추정 틀을 만들었다. 자료를 쉽게 많이 얻을 수 있는 시뮬레이션 자료만으로 훈련했고, 기존 학습 기법과 정규화를 적용해 시뮬레이션과 실제의 차이를 다뤘다. 평평한 땅, 잔해, 무른 땅, 미끄러운 땅의 네 지형에서 사족 보행 로봇으로 실험해, 모델 기반 상태 추정기에 비해 위치와 속도의 평균 절대 궤적 오차(ATE)를 줄였다.[^p8] | 1저자 D. Youm(Donghoon Youm), 마지막 저자 황보제민 (6명) |

## 교수와 전문 분야

황보제민 교수(Jemin Hwangbo)는 KAIST 기계공학과 교수다.[^mepop] Members 페이지에 따르면 University of Toronto에서 학사 학위를, ETH Zurich에서 석사와 박사 학위를 받았고, 기계공학과 교수 소개는 최종학위를 Ph.D., ETH Zurich(2019)로 적는다.[^members][^mepop] 기계공학과 교수 소개와 교수진 목록은 연구분야를 Legged robotics, Learning-based control로 적고, 기계공학과 연구분야 페이지는 교수를 로보틱스/제어/모빌리티 분야의 핵심교수로 싣는다.[^mepop][^me][^mer1]

Education 페이지는 두 강의를 소개한다. 봄 학기 Robot dynamics(로봇 동역학)는 여러 몸체와 관절로 이루어진 강체 다관절 시스템의 동역학, 특히 시뮬레이션을 위한 순방향 동역학을 다루며, 뉴턴 역학에 바탕을 둔 재귀 계산법인 ABA(Articulated Body Algorithm), CRBA(Composite Rigid Body Algorithm), RNE(Recursive Newton-Euler)를 주된 도구로 쓰고 라그랑주 역학과 접촉의 비매끄러운 동역학도 다룬다. 가을 학기 Learning-based control(학습 기반 제어)은 심층 강화학습을 중심으로 학습 기반 제어의 개념을 가르치며, 벨만 최적성 조건과 HJB 방정식(Hamilton-Jacobi-Bellman 방정식, 최적 제어 문제의 최적값이 만족하는 편미분 방정식) 같은 최적 제어의 기초에서 시작해 강화학습의 최근 연구 흐름까지 다룬다.[^edu]

누리집 Publications 목록은 2021년 이전 논문도 함께 싣는다. 그 가운데 교수가 1저자인 논문으로는 다리 로봇의 민첩하고 동적인 운동 기술 학습(Science Robotics, 2019년 구역), 접촉 동역학을 푸는 접촉점별 반복 계산법(IEEE Robotics and Automation Letters, 2018년 구역), 동적 로봇 시스템을 위한 케이블 구동(IROS, 2018년 구역), 강화학습을 쓴 쿼드로터(프로펠러 네 개로 나는 비행체) 제어(Older 구역)가 있다.[^pubs] 2021–2026년 대표 논문으로 보면 최근 전문 분야는 강화학습 기반 다리 로봇 보행 제어(대표 논문 1, 2, 7), 고속 항법과 야외 자율 항법(대표 논문 3, 4), 사족 보행 로봇의 전신 조작(대표 논문 5), 에너지 효율이 높은 보행 로봇 하드웨어 설계(대표 논문 6), 고유 감각 상태 추정(대표 논문 8)이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

기계공학과 연구분야 페이지는 교수 연구의 주요 응용 산업을 구조 로봇과 서비스 로봇으로 적는다.[^mer1] Robots 페이지는 RAIBO가 산업 점검·탐사·순찰 같은 실제 작업에 알맞은 크기이고, RAIBO 2가 내구성과 효율이 중요한 산업 응용에 실용적인 해법이라고 적는다.[^robots] Research 페이지는 자율 항법 연구의 최종 목표를 실내외 자율 점검 같은 여러 작업에 쓸 수 있는 항법 시스템으로 적는다.[^research]

## 구성원

누리집 Members 페이지의 학생 23명이다(박사과정 13명, 석사과정 10명). 과정은 Doctoral Students·Master Students 구역을 옮긴 것이고, 괄호 안은 카드에 적힌 이전 학위(BAS 학사, MAS 석사)와 학교를 누리집 표기 그대로 옮겼다. 카드는 시작 연도, 연구 주제, 이메일을 적지 않는다. 대표 논문 참여 칸은 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Yongjae Kim | 박사과정 (BAS, MAS at Tokyo Tech) |  |
| Donghoon Youm | 박사과정 (BAS, MAS at KAIST) | 2, 3, 6, 8 |
| Suyoung Choi | 박사과정 (BAS at Chung-Ang University; MAS at KAIST) | 1, 4, 5, 6, 8 |
| Hyeongjun Kim | 박사과정 (BAS, MAS at KAIST) | 1, 3, 6, 8 |
| Gwanghyeon Ji | 박사과정 (BAS at POSTECH; MAS at KAIST) | 1, 2, 6 |
| JuhyeokMun | 박사과정 (BAS at Seoul National University; MAS at KAIST) | 1, 6 |
| Jeongsoo Park | 박사과정 (BAS, MAS at KAIST) | 1, 3, 6 |
| Seunghun Jeon | 박사과정 (BAS, MAS at KAIST) | 5, 8 |
| Jeong Hyun Lee | 박사과정 (BAS, MAS at KAIST) | 1, 2, 4, 6, 7 |
| Hyunsik Oh | 박사과정 (BAS at Hanyang University; MAS at KAIST) | 2, 3, 4, 6, 8 |
| Moonkyu Jung | 박사과정 (BAS, MAS at KAIST) | 2, 3, 5, 6 |
| Kyungmin Nam | 박사과정 (BAS, MAS at KAIST) | 6 |
| Minho Lee | 박사과정 (BAS, MAS at KAIST) | 3, 6, 7 |
| Hyungho Choi | 석사과정 (BAS at KAIST) | 6 |
| Donghyuk Choi | 석사과정 (BAS at KAIST) | 6 |
| Donggeon Kim | 석사과정 (BAS at KAIST) | 6 |
| Woojin Kim | 석사과정 (BAS at POSTECH) |  |
| Jiseong Lee | 석사과정 (BAS at KAIST) |  |
| Jungwoo Hur | 석사과정 (BAS at Sogang University) | 6 |
| Eunchae Kim | 석사과정 (BAS at KAIST) |  |
| Insung Yang | 석사과정 (BAS at KAIST) |  |
| Donghee Kim | 석사과정 (BAS at KAIST) |  |
| Kyungseo Park | 석사과정 (BAS at Seoul National University) |  |

## 졸업생과 이전 구성원

누리집 Members 페이지 Alumni 구역의 5명 전부다. 카드는 이름과 학위·학교(BAS 학사, MAS 석사, PhD 박사 표기)만 적고, 졸업 연도와 진로는 적지 않는다. 학위 칸은 누리집 표기 그대로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Joowoong Byun | BAS at Yonsei University; MAS at KAIST |  |
| Seungyeon Hwang | BAS at Sungkyunkwan University; MAS at KAIST |  |
| Yunho Kim | BAS at Seoul National University; MAS at KAIST |  |
| Simo Ryu | BAS at Korea University; MAS at KAIST |  |
| Choongin Lee | BAS, MAS at Seoul National University; PhD at KAIST |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지는 International 구역에 2026–2017년 연도 구역과 Older 구역으로 모두 45편을, Domestic 구역에 국내 학회 논문 4편을 싣는다.[^pubs] 아래는 International 구역의 2021–2026년 27편(2026년 6편, 2025년 4편, 2024년 4편, 2023년 4편, 2022년 8편, 2021년 1편)과 Domestic 구역 4편(2023년 2편, 2021년 2편)이다. 이 목록은 2021년 이전 논문까지 담은 교수의 논문 목록이고, 2022년 구역의 5편(KAIST HOUND 설계, Monte carlo tree search 걸음새 계획, 야외 지각 보행, D-grasp, 유압 구동기 힘 제어)은 저자에 Members 페이지의 구성원·졸업생 이름이 없는 논문이다. 2026년 구역의 4편은 누리집이 권호 없이 (Accepted)로만 적은 학술지 논문이라 「게재 승인」으로 표시했다. 저자 순서와 이름 뒤 *, 제목·학술지·학회 표기는 누리집 그대로이며, Domestic 구역의 논문은 누리집의 한 줄 표기를 그대로 옮겼다(한 줄은 끝에 Best Paper Award를 적는다).[^pubs]

**2026**

- Jung, Moonkyu; Lee, Jiseong; He, Zhengmao; Youm, Donghoon; Mun, Juhyeok; Kim, HyeongJun; Oh, Hyunsik; Choi, Donghyuk; Hur, Jungwoo; Song, Jie; Hwangbo, Jemin. "Learning Dynamic Pick-and-Place for a Legged Manipulator". *IEEE Robotics and Automation Letters*.
- Kim, Donggeon\*; Choi, Hyungho Chris\*; Choi, Donghyuk\*; Park, Jeongsoo; Lee, Choongin; Park, Chan; Hwangbo, Jemin. "RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks". *IEEE Robotics and Automation Letters (게재 승인, 누리집 표기 Accepted)*.
- Lee, Choongin\*; Youm, Donghoon\*; Park, Jeongsoo\*; Lee, Jeonghyun; Choi, Suyoung; Ji, Gwanghyeon; Mun, Juhyeok; Jung, Moonkyu; Choi, Hyungho Chris; Kim, Hyeongjun; Oh, Hyunsik; Nam, Kyungmin; Lee, Minho; Hur, Jungwoo; Choi, Donghyuk; Kim, Donggeon; An, Yeonsu; Hwangbo, Jemin. "A Quadruped Robot Designed to Complete a Marathon on a Single Battery Charge". *Nature*.
- He, Zhengmao\*; Jung, Moonkyu\*; Kim, HyeongJun; Lee, Jiseong; Zhang, Hui; Hwangbo, Jemin; Song, Jie. "PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings". *IEEE Robotics and Automation Letters (게재 승인, 누리집 표기 Accepted)*.
- Oh, Hyunsik; Jeon, Seunghun; Youm, Donghoon; Hur, Jungwoo; Kim, HyeongJun; Lee, Jeong Hyun; Jung, Moonkyu; Hwangbo, Jemin. "PolyMorph: Learning Locomotion Policy for Cross-Embodiment Adaptation". *IEEE Robotics and Automation Letters (게재 승인, 누리집 표기 Accepted)*.
- Nam, Kyungmin; Lee, Jiseong; Choi, Donghyuk; Park, Jeongsoo; Kim, Woojin; Hwangbo, Jemin. "RAIWAY: A Large-Wheeled Bipedal Robot with Contact-Informed Blind Locomotion". *IEEE Robotics and Automation Letters (게재 승인, 누리집 표기 Accepted)*.

**2025**

- Youm, Donghoon; Oh, Hyunsik; Choi, Suyoung; Kim, Hyeongjun; Jeon, Seunghun; Hwangbo, Jemin. "Legged Robot State Estimation With Invariant Extended Kalman Filter Using Neural Measurement Network". *2025 International Conference on Robotics and Automation (ICRA)*.
- Kim, Hyeongjun; Oh, Hyunsik; Park, Jeongsoo; Kim, Yunho; Youm, Donghoon; Jung, Moonkyu; Lee, Minho; Hwangbo, Jemin. "High-speed control and navigation for quadrupedal robots on complex and discrete terrain". *Science Robotics*.
- Yang, Insung; Hwangbo, Jemin. "Learning rapid turning, aerial reorientation, and balancing using manipulator as a tail". *2025 International Conference on Automation Science and Engineering (CASE)*.
- Lee, Minho; Kim, Hyeonseok; Kim, Jin Tak; Park, Sangshin; Lee, Jeong Hyun; Cho, Jungsan; Hwangbo, Jemin. "Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model". *IEEE Robotics and Automation Letters*.

**2024**

- Kim, Yunho\*; Lee, Jeong Hyun\*; Lee, Choongin; Mun, Juhyeok; Youm, Donghoon; Park, Jeongsoo; Hwangbo, Jemin. "Learning Semantic Traversability with Egocentric Video and Automated Annotation Strategy". *IEEE Robotics and Automation Letters*.
- Lee, Jeong Hyun; Choi, Jinhyeok; Ryu, Simo; Oh, Hyunsik; Choi, Suyoung; Hwangbo, Jemin. "Learning Vehicle Dynamics from Cropped Image Patches for Robot Navigation in Unpaved Outdoor Terrains". *IEEE Robotics and Automation Letters*.
- Kim, Yunho; Oh, Hyunsik; Lee, Jeonghyun; Choi, Jinhyeok; Ji, Gwanghyeon; Jung, Moonkyu; Youm, Donghoon; Hwangbo, Jemin. "Not only rewards but also constraints: Applications on legged robot locomotion". *IEEE Transactions on Robotics*.
- Lee, Joonhyub; Oh, Hyunsik; Yoon, Junwoo; Lee, Seung-Jun; Jin, Taegyu; Hwangbo, Jemin; Bae, Seok-Hyung. "RobotSketch: An Interactive Showcase of Superfast Design of Legged Robots". *ACM SIGGRAPH 2024 Emerging Technologies*.

**2023**

- Lee, Seokju; Jeon, Seunghun; Hwangbo, Jemin. "Learning Legged Mobile Manipulation Using Reinforcement Learning". *Robot Intelligence Technology and Applications 7: Results from the 10th International Conference on Robot Intelligence Technology and Applications*.
- Choi, Suyoung; Ji, Gwanghyeon; Park, Jeongsoo; Kim, Hyeongjun; Mun, Juhyeok; Lee, Jeong Hyun; Hwangbo, Jemin. "Learning quadrupedal locomotion on deformable terrain". *Science Robotics*.
- Jeon, Seunghun; Jung, Moonkyu; Choi, Suyoung; Kim, Beomjoon; Hwangbo, Jemin. "Learning Whole-body Manipulation for Quadrupedal Robot". *IEEE Robotics and Automation Letters*.
- Youm, Donghoon; Jung, Hyunyoung; Kim, Hyeongjun; Hwangbo, Jemin; Park, Hae-Won; Ha, Sehoon. "Imitating and Finetuning Model Predictive Control for Robust and Symmetric Quadrupedal Locomotion". *IEEE Robotics and Automation Letters*.
- 이정현, 최진혁, 황보제민, 강화학습을 사용한 험지 자율주행 경로계획 알고리즘 연구, Research on Rough Terrain Autonomous Driving Path Planning Algorithm Using Reinforcement Learning, (한국로봇종합학술대회, 2023)
- 최진혁, 이정현, 황보제민, 비포장 야지 자율주행을 위한 애커먼 스티어링 차륜 플랫폼 개발, Development of Ackermann Steering Car Platform for Autonomous Driving in Rough terrain, (한국로봇종합학술대회, 2023)

**2022**

- Shin, Young-Ha; Hong, Seungwoo; Woo, Sangyoung; Choe, JongHun; Son, Harim; Kim, Gijeong; Kim, Joon-Ha; Lee, KangKyu; Hwangbo, Jemin; Park, Hae-Won. "Design of KAIST HOUND, a quadruped robot platform for fast and efficient locomotion with mixed-integer nonlinear optimization of a gear train". *2022 International Conference on Robotics and Automation (ICRA)*.
- Amatucci, Lorznzo; Kim, Joon-Ha; Hwangbo, Jemin; Park, Hae-Won. "Monte carlo tree search gait planner for non-gaited legged system control". *2022 International Conference on Robotics and Automation (ICRA)*.
- Kim, Yunho; Kim, Chanyoung; Hwangbo, Jemin. "Learning Forward Dynamics Model and Informed Trajectory Sampler for Safe Quadruped Navigation". *Robotics: Science and Systems (RSS) 2022*.
- Byun, Joo Woong; Youm, Donghoon; Jeon, Seunghoon; Hwangbo, Jemin; Park, Hae-Won. "Learning Footstep Planning for the Quadrupedal Locomotion with Model Predictive Control". *Robot Intelligence Technology and Applications 6: Results from the 9th International Conference on Robot Intelligence Technology and Applications*.
- Ji, Gwanghyeon; Mun, Juhyeok; Kim, Hyeongjun; Hwangbo, Jemin. "Concurrent training of a control policy and a state estimator for dynamic and robust legged locomotion". *IEEE Robotics and Automation Letters*.
- Miki, Takahiro; Lee, Joonho; Hwangbo, Jemin; Wellhausen, Lorenz; Koltun, Vladlen; Hutter, Marco. "Learning robust perceptive locomotion for quadrupedal robots in the wild". *Science Robotics*.
- Christen, Sammy; Kocabas, Muhammed; Aksan, Emre; Hwangbo, Jemin; Song, Jie; Hilliges, Otmar. "D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions". *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.
- Kim, Sung-Woo; Cho, Buyoun; Shin, Seunghoon; Oh, Jun-Ho; Hwangbo, Jemin; Park, Hae-Won. "Force control of a hydraulic actuator with a neural network inverse model". *IEEE Robotics and Automation Letters*.

**2021**

- Kim, Joon-Ha; Hong, Seungwoo; Ji, Gwanghyeon; Jeon, Seunghun; Hwangbo, Jemin; Oh, Jun-Ho; Park, Hae-Won. "Legged robot state estimation with dynamic contact event information". *IEEE Robotics and Automation Letters*.
- 전승훈, 황보제민, 학습 기반 4족 로봇 동적 행동 제어, Quadrupedal robot dynamic motion control based on learning, The Korea Robotics Society Annual Conference, 2021, (한국로봇종합학술대회, 2021)
- 전승훈, 황보제민, 학습 기반 4족 보행과 2족 보행간 전환식 제어, Learning based switchable multimodal locomotion control between quadrupedal and bipedal locomotion modes, The Korea Robotics Society Annual Conference, 2021, (한국로봇종합학술대회, 2021), Best Paper Award

## 연구 과제

누리집 Projects 페이지가 진행 중인 주요 과제(important ongoing initiatives)로 소개하는 6건 전부다. 페이지는 과제의 기간과 시작 연도를 적지 않는다. 과제 이름과 지원·협력 기관 표기는 누리집 그대로다.[^projects]

- Robust Humanoid Robots (지원 Republic Korea’s Ministry of Trade, Industry and Energy (MOTIE); 협력 기관 KAIST’s URL/DRCD/CLVR, MIT’s Biomemetic Robotics Lab, and Rainbow Robotics)
- Revolutionizing Autonomous Design (지원 DRB)
- Quadrupedal Locomotion (지원 Samsung Research Funding & Incubation Center of Samsung Electronics)
- Language Driven Environment Design (지원 NAVER Cloud)
- High-Speed Vision Autonomy (지원 Singapore’s DSO National Laboratories)
- Whole Body Manipulation (지원 National Research Foundation of Korea (NRF))

## 소식

누리집 News 페이지의 Highlights 2건, Spotlights 2건, Webinars 2건 가운데 2021년 10월 13일 이전 날짜의 웨비나 1건(2021.01.19)을 뺀 5건이다. 2024 Sangju Marathon 항목의 날짜는 본문에 적힌 대회 날짜이고, 2023 Innovate Korea 항목은 연도만 적혀 있으며, Spotlights 2건에는 날짜가 없다. 제목 문구는 누리집 그대로다.[^news]

- 2024-11-17 · 2024 Sangju Marathon: RAIBO2 became the first ever quadruped robot to complete a full marathon!
- 2023 · 2023 Innovate Korea
- 2023-06-22 · Webinar: Development and Related Research of RaiBo at KAIST
- Spotlights: Our work was spotlighted on the nature news article
- Spotlights: Our work was highlighted on numerous broadcast media

## 연락과 위치

- 교수실: (Office) 4150, Building N9, 291 Daehak St., Yuseong-gu, Deajeon, Korea(누리집 표기)[^open]
- 전화: 042-350-3244[^mepop]
- 교수 이메일: jhwangbo@kaist.ac.kr[^mepop]
- 대학원 지원: 석사과정은 KAIST 기계공학과 과정에 직접 지원하고, 박사과정은 교수에게 직접 연락하라고 안내한다.[^open]
[^home]: RaiLab 누리집 첫 화면 <https://railab.kaist.ac.kr/> (누리집 제목과 연구실 이름, 메뉴, 2026-10-23 열람)
[^research]: RaiLab 누리집 Research 페이지 <https://railab.kaist.ac.kr/sections/research.html> (학습 기반 제어, 자율 항법, 하드웨어 플랫폼(기계·전자 설계)의 소개와 연구실 논문, 2026-10-23 열람)
[^robots]: RaiLab 누리집 Robots 페이지 <https://railab.kaist.ac.kr/sections/robots.html> (RAIBO 2, RAIWAY, RAIBO, Mini Cheetah, RAICART 소개, 2026-10-23 열람)
[^members]: RaiLab 누리집 Members 페이지 <https://railab.kaist.ac.kr/sections/members.html> (교수 학력, 박사과정 13명, 석사과정 10명, 졸업생 5명, 2026-10-23 열람)
[^news]: RaiLab 누리집 News 페이지 <https://railab.kaist.ac.kr/sections/news.html> (Highlights 2건, Spotlights 2건, Webinars 2건, 2026-10-23 열람)
[^pubs]: RaiLab 누리집 Publications 페이지 <https://railab.kaist.ac.kr/sections/publication.html> (International 45편, Domestic 4편, 2026-10-23 열람)
[^projects]: RaiLab 누리집 Projects 페이지 <https://railab.kaist.ac.kr/sections/projects.html> (과제 6건의 내용과 지원·협력 기관, 2026-10-23 열람)
[^software]: RaiLab 누리집 Software 페이지 <https://railab.kaist.ac.kr/sections/software.html> (물리 엔진 RaiSim 소개, 2026-10-23 열람)
[^edu]: RaiLab 누리집 Education 페이지 <https://railab.kaist.ac.kr/sections/education.html> (강의 2개의 소개와 핵심어, 2026-10-23 열람)
[^open]: RaiLab 누리집 Open position 페이지 <https://railab.kaist.ac.kr/sections/openpositions.html> (석사·박사 과정 지원 안내, 교수실 주소, 2026-10-23 열람)
[^me]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (연구분야, 연구실, 최종학위, 2026-10-23 열람)
[^mepop]: KAIST 기계공학과 교수 소개(황보제민) <https://me.kaist.ac.kr/pop/team.html?uid=102&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 전화, 2026-10-23 열람)
[^mer1]: KAIST 기계공학과 연구분야 로보틱스/제어/모빌리티 페이지 <https://me.kaist.ac.kr/research/research_010100.html> (교수의 연구주제와 주요 응용 산업, 2026-10-23 열람)
[^p1]: S. Choi 외, J. Hwangbo, Science Robotics 8, eade2256 (2023). <https://doi.org/10.1126/scirobotics.ade2256> 초록 기준.
[^p2]: Y. Kim 외, J. Hwangbo, IEEE Transactions on Robotics 40, 2984-3003 (2024). <https://doi.org/10.1109/tro.2024.3400935> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: H. Kim 외, J. Hwangbo, Science Robotics 10, eads6192 (2025). <https://doi.org/10.1126/scirobotics.ads6192> 초록 기준.
[^p4]: J. H. Lee 외, J. Hwangbo, IEEE Robotics and Automation Letters 9, 4035-4042 (2024). <https://doi.org/10.1109/lra.2024.3371910> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Jeon 외, J. Hwangbo, IEEE Robotics and Automation Letters 9, 699-706 (2024). <https://doi.org/10.1109/lra.2023.3335777> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: C. Lee 외, J. Hwangbo, Nature 658, 372-379 (온라인 2026-09-23). <https://doi.org/10.1038/s41586-026-11102-5> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. Lee 외, J. Hwangbo, IEEE Robotics and Automation Letters 10, 12421-12428 (2025). <https://doi.org/10.1109/lra.2025.3623024> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: D. Youm 외, J. Hwangbo, 2025 IEEE International Conference on Robotics and Automation (ICRA), 670-676 (2025). <https://doi.org/10.1109/icra55743.2025.11127971> 초록 기준(Semantic Scholar 등록 초록).

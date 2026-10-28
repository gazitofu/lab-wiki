# 강인지능 및 로보틱스 연구실 (Robust Intelligence and Robotics Laboratory, RIRO Lab)

**KAIST 전산학부·AI Computing·Graduate School of AI·Robotics Program·Graduate School of Advanced Security Science and Technology · 박대형 부교수**

- 분야: 로봇 학습, 로봇의 물체 조작, 작업·경로 계획, 자연어 지시 해석, 인간과 로봇의 상호작용[^home][^topics][^faculty]
- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 로봇 조작·파지[^topics][^p2], 강화학습[^topics][^p3], 로봇 항법·SLAM[^topics][^p7], 인간–로봇 상호작용[^home][^p8], 보행·휴머노이드 로봇[^topics], 그래프 기계학습·지식 그래프[^p5][^p6]
- 홈페이지: <https://rirolab.kaist.ac.kr/>
- 근거와 출처: [RIRO Lab 근거 페이지](rirolab-sources.md)

> 사람의 말과 시연을 이해하고, 물체를 다루며, 작업 도중 상황이 바뀌어도 계획을 고쳐 실행하는 로봇의 지능을 연구한다.[^home][^topics][^p8]

## 무엇을 연구하나

RIRO Lab은 박대형 교수가 이끄는 KAIST 전산학부 연구실이다. 기계학습(자료와 경험으로부터 규칙이나 예측 방법을 배우는 계산 방법)과 로보틱스(로봇의 설계·인식·계획·제어를 다루는 분야)의 접점에서 협업·서비스 로봇을 연구한다. 이동하면서 물체도 다루는 모바일 매니퓰레이션을 중심으로, 사람이 전달한 의도를 이해하고 실제 행동으로 이어 가는 방법을 개발한다.[^home][^faculty]

사람이 보여 준 행동을 배우는 시연 학습과 행동 결과의 평가를 통해 행동 선택 방법을 배우는 강화학습을 다룬다. 학습 대상에는 목표에 이르는 동작뿐 아니라 행동 중 지켜야 할 제약 조건도 들어간다. 예를 들어 해야 할 일의 보상(행동의 결과를 평가하는 값)과 해서는 안 되는 행동에 관한 조건을 나누어 배우거나, 행동 순서에 관한 조건을 시연에서 찾아 새 과제에 적용하는 방법을 제안했다.[^topics][^p3][^p4]

환경을 해석하는 일과 행동을 계획하는 일도 연결한다. 언어 지시가 가리키는 위치를 하나로 단정하는 대신 확률 분포(가능한 값마다 어느 정도의 가능성이 있는지 나타내는 규칙)로 나타내고, 추가 지시로 그 범위를 갱신한다. 로봇과 장애물 사이의 거리를 예측하는 방법과, 사람이 물체를 옮기는 등 작업에 개입했을 때 계획을 고치는 방법도 연구한다.[^p5][^p6][^p7][^p8]

현재 연구 소개는 휴머노이드(사람 형태의 몸을 갖춘 로봇)의 전신 조작, 변형 가능한 물체의 손안 조작, 언어·영상 모델을 이용한 작업·동작 계획, 언어로 이끄는 이동·조작을 제시한다. 전신 조작은 팔·손과 몸의 움직임을 함께 사용해 물체를 다루는 것이다. 연구실은 모방·강화학습으로 행동을 배우고, 대형 언어 모델(많은 언어 자료를 학습해 언어를 처리·생성하는 인공지능 모델)과 시각·언어·행동 모델(Vision-Language-Action model, VLA: 시각 정보와 언어 지시를 받아 행동을 출력하는 모델)을 이용해 실제 환경의 여러 과제를 수행하는 계층적 학습 체계(여러 수준으로 나눈 의사결정을 연결해 배우는 체계)를 만드는 것을 목표로 한다.[^topics]

## 주요 연구 주제

### 시연에서 조작 배우기와 변형 물체 다루기

DiSPo는 시연으로 배운 동작의 세밀함을 바꾸는 정책 학습(상황에 따라 행동을 선택하는 규칙을 배우는 과정) 방법이다. 중요한 구간과 그렇지 않은 구간에서 움직임의 간격을 달리하는 방식을 다룬다. INR-DOM(Implicit Neural-Representation Learning for Elastic Deformable-Object Manipulations)은 일부만 보이는 탄성 물체의 전체 표면을 복원해 물체 상태를 나타내고, 그 표현을 조작 행동 학습에 사용한다. 연구실의 장기 방향에는 영상과 촉각을 함께 이용해 변형 물체를 손안에서 옮기고 방향을 바꾸는 방법도 들어 있다.[^p1][^p2][^topics]

### 시연에서 제약과 행동 순서 배우기

역제약 학습(Inverse Constraint Learning, ICL)은 시연으로부터 지켜야 할 조건을 거꾸로 알아내는 방법이다. 연구실은 과제의 목표와 과제에 매이지 않는 제약을 나누어 배워 새 상황에 옮기는 방법을 제안했다. ILCL(Inverse Logic-Constraint Learning)은 시간 논리(사건의 발생 순서와 시간에 따른 조건을 표현하는 논리)를 이용해 시연에 담긴 행동 순서의 제약을 배우고, 그 제약 아래에서 행동을 학습한다.[^p3][^p4]

### 충돌 거리 추정과 작업·동작 계획

그래프(대상과 그 사이의 관계를 점과 선으로 나타낸 구조)로 물체 형상 사이의 관계를 표현해 거리를 추정한다. GraphDistNet은 형상 사이의 거리와 그 거리의 변화 정보를 예측하며, 후속 연구 GDN-R은 그래프의 연결을 바꾸면서 입체 형상의 최소 거리를 추정한다. 작업·동작 계획(Task-and-Motion Planning, TAMP)은 무엇을 어떤 순서로 할지 정하는 계획과 몸을 어떻게 움직일지 정하는 계획을 함께 다룬다. 사람이 작업에 개입했을 때 앞서 만든 계획을 활용해 실행을 복구하는 방법도 연구했다.[^p5][^p6][^p8]

### 사람의 언어를 로봇의 위치·행동으로 연결하기

언어 접지(말의 의미를 실제 환경의 대상·위치·행동과 연결하는 과정)를 통해 사람이 전달한 이동·조작 지시를 해석한다. LINGO-Space는 공간을 가리키는 표현의 불명확함을 확률적으로 다루고, 후속 표현으로 공간의 범위를 갱신한다. 현재 연구 방향은 언어와 움직임을 짝지은 자료에서 상식적 지식을 배우고, 빠진 정보가 있는 지시를 상황에 맞게 해석하는 것이다. 사족 로봇을 포함한 이동 로봇에서 언어 지시를 이용한 학습 방법을 평가한다고 밝힌다.[^p7][^topics]

## 대표 논문

박대형 교수의 KAIST 부임 이후인 2021–2026년 연구 가운데 연구 갈래와 최근 연구를 고르게 보여 주는 8편이다. 아래 제목과 날짜는 각주에 표시한 arXiv 사전 공개본 기준이며, 날짜는 최초 제출일이다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.[^advisor]

| 번호 | 연도 | 논문·판본 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2024 | **DiSPo: Diffusion-SSM based Policy Learning for Coarse-to-Fine Action Discretization**. arXiv, 2024-09-23, 2026-02-24 개정판. ICRA 2026 채택 표기.[^p1] | 거친 동작을 보여 준 시연에서 배우고 동작의 세밀함을 바꿔 출력하는 방법을 제안했다. 제안한 학습 방식과 동작 간격 조절을 평가하고, 모의 환경과 실제 물체 조작에서 적용 가능성을 보였다. |
| 2 | 2025 | **Implicit Neural-Representation Learning for Elastic Deformable-Object Manipulations**. arXiv, 2025-05-01.[^p2] | 탄성 물체가 일부만 보여도 전체 표면을 나타내는 표현을 배우고, 이를 로봇의 조작 학습에 연결했다. 학습 중 표현을 조정하는 방법을 제안하고, 모의 환경과 실제 로봇 팔에서 분석했다. |
| 3 | 2025 | **ILCL: Inverse Logic-Constraint Learning from Temporally Constrained Demonstrations**. arXiv, 2025-07-15, 2025-11-08 개정판.[^p3] | 시연에 담긴 행동 순서의 조건을 찾는 과정과 그 조건 아래에서 행동을 배우는 과정을 결합했다. 조건을 배우고 다른 과제에 옮기는 성능을 평가했으며, 실제 삽입 작업으로의 이전도 보였다. |
| 4 | 2023 | **Inverse Constraint Learning and Generalization by Transferable Reward Decomposition**. arXiv, 2023-06-21.[^p4] | 시연에서 해야 할 일의 목표와 지켜야 할 조건을 나누어 배우는 방법을 제안했다. 새 상황에서 학습한 조건을 활용하는 성능을 모의 환경에서 비교하고 실제 로봇 과제에서도 평가했다. |
| 5 | 2022 | **GraphDistNet: A Graph-based Collision-distance Estimator for Gradient-based Trajectory Optimization**. arXiv, 2022-06-03. 페이지에 RA-L 2022 출판판 표기.[^p5] | 물체 형상 사이의 구조적 관계를 이용해 충돌 거리와 그 거리의 변화 정보를 예측한다. 학습 때 보지 못한 형상에서의 적용과 로봇의 움직임 계획을 모의 환경·실제 과제에서 평가했다. |
| 6 | 2023 | **Graph-based 3D Collision-distance Estimation Network with Probabilistic Graph Rewiring**. arXiv, 2023-10-06.[^p6] | 입체 물체 사이의 최소 거리를 추정하면서 형상을 나타내는 그래프의 연결을 확률적으로 바꾸는 방법을 제안했다. 처음 보는 물체 형태에 대한 예측과 움직임 계획에 필요한 계산 기능을 평가했다. |
| 7 | 2024 | **LINGO-Space: Language-Conditioned Incremental Grounding for Space**. arXiv, 2024-02-02. AAAI 2024 채택 표기.[^p7] | 말로 가리킨 공간을 확률로 나타내고, 이어지는 지시로 그 범위를 갱신하는 방법을 제안했다. 모의 물체 조작과 실제 사족 로봇 이동 과제에서 평가했다. |
| 8 | 2021 | **Reactive Task and Motion Planning under Temporal Logic Specifications**. arXiv, 2021-03-26. 페이지에 ICRA 2021 출판 표기.[^p8] | 사람이 작업에 협조하거나 방해해 계획이 어긋나는 상황에 대응한다. 앞서 만든 계획과 갱신한 탐색 결과를 활용해 실행을 복구하는 방법을 제안하고, 모의 환경과 실제 물체 조작에서 평가했다. |

## 교수와 전문 분야

박대형 교수는 2020년 9월 KAIST 전산학부 조교수로 부임했고 2024년 9월부터 부교수로 재직한다. 연구실 소개에는 AI Computing, Graduate School of AI, Robotics Program, Graduate School of Advanced Security Science and Technology 겸무가 적혀 있다.[^advisor] 학과 소개는 로봇학·기계학습·인공지능을 전공으로 적고, 모바일 매니퓰레이션, 작업·경로 계획, 인간과 로봇의 상호작용을 연구 분야로 소개한다.[^faculty]

2018년 Georgia Institute of Technology에서 로보틱스 박사학위를 받았으며, 이후 MIT 컴퓨터과학·인공지능연구소에서 박사후연구원으로 일했다. 그 이전에는 삼성전자에서 로봇 연구원으로 근무했다.[^advisor][^faculty] 최근 연구는 시연에서 행동과 제약을 배우는 방법, 변형 물체를 다루는 학습, 물체 간 거리 추정, 언어의 공간적 의미 해석을 연결한다. 대표 논문 1–7에서 마지막 저자로, 8에서 공동저자로 참여한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

협업·서비스 로봇, 이동하면서 물체를 다루는 로봇, 현장 작업 로봇과 자동화를 목표로 한다. 현재 연구 소개는 휴머노이드의 전신 조작, 변형 물체의 손안 조작, 사람의 언어 지시를 따르는 이동·조작을 구체적인 대상으로 든다.[^home][^topics]

## 구성원

People 페이지의 교수 이외 현재 구성원 23명이다. 박사후연구원 2명, 박사과정 5명, 석사과정 12명, 학부 연구생 4명이며, 괄호 안 소속·연도와 연구 주제는 랩 표기다. 연도는 소속·과정 옆 게시 연도이며 합류 시점으로 단정하지 않는다. 대표 논문 전체 저자 목록과 같은 이름의 저자를 같은 사람으로 보아 참여 번호를 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Sehee Jung | 박사후연구원 (5D AI Robotics Initiative) | Computer Vision, Planning |  |
| Linan Deng | 박사후연구원 (5D AI Robotics Initiative) | Manipulation, Tactile Sensing |  |
| Yeseung Kim | 박사과정 (School of Computing, 2023) | Motion Planning, Collision Detection | 5, 6 |
| Dohyun Kim | 박사과정 (School of Computing, 2024) | Robotic Natural Language Processing | 7 |
| Junhyeong Bang | 박사과정 (School of Computing, 2025) | Natural Language Grounding |  |
| Woosong Kang | 박사과정 (School of Computing, 2026) | Humanoid Whole-body Control |  |
| An Ning | 박사과정 (School of Computing, 2026) | Vision Language Action, Imitation Learning |  |
| Gyungjin Eo | 석사과정 (Robotics Program, 2024) | Perception, Task Planning |  |
| Minseok Song | 석사과정 (School of Computing, 2025) | Manipulation | 2 |
| Seungsup Lee | 석사과정 (School of Computing, 2025) | Perception, Manipulation, Planning |  |
| Jun Park | 석사과정 (Robotics Program, 2025) | Manipulation, Task Planning |  |
| Jaehyeong Jang | 석사과정 (School of Computing, 2025) | Imitation Learning, Reinforcement Learning | 1 |
| Hyungjin Kwon | 석사과정 (Robotics Program, 2025) | Planning, Navigation |  |
| Sungtai Jang | 석사과정 (Software Program (Hyundai Motor), 2025) | Engineering & HRI |  |
| Chankyu Lee | 석사과정 (School of Computing, 2026) | Manipulation |  |
| Sangyun Won | 석사과정 (School of Computing, 2026) | VLA, Imitation Learning |  |
| Geonwoo Kim | 석사과정 (Robotics Program, 2026) | Manipulation |  |
| Injin Choi | 석사과정 (Department of AI Computing, 2026) | Planning, Navigation |  |
| Seoyul Jeon | 석사과정 (School of Computing, 2026) | Physical AI, ML & DL |  |
| Joonwoo Hur | 학부 연구생 (School of Computing, 2022) | Manipulation |  |
| Taekgeun Nam | 학부 연구생 (Mechanical Engineering, 2023) | Humanoid Whole-body Control |  |
| Hyunseo Lee | 학부 연구생 (School of Computing, 2022) | Planning, Navigation |  |
| Yungeun Song | 학부 연구생 (School of Computing, 2020) | Reinforcement Learning |  |

## 졸업생과 이전 구성원

People 페이지 Alumni 11명과 Past RA & Visiting Scholars 4명이다. Alumni의 학위 연도는 2024–2026년, 이전 연구원·방문자의 게시 활동 연도는 2024–2025년이다. 후자의 기관은 해당 활동 소개에 적힌 소속이며 이후 진로를 뜻하지 않는다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Moonkyeong Jung | M.S. in Robotics Program (2026) | Samsung Electronics |
| Keonyoung Koh | M.S. in School of Computing (2026) |  |
| Nayoung Oh | M.S. in Artificial Intelligence (2026) |  |
| Deok-Min Hwang | M.S. in School of Computing (2026) |  |
| Minwoo Cho | M.S. in School of Computing (2025) |  |
| Jieun Choi | M.S. in School of Computing KT-AI  (2025) | KT |
| Minjae Song | M.S. in School of Computing (2024) | Vuno |
| Jaehwi Jang | M.S. in Artificial Intelligence (2024) | Georgia Tech Ph.D. Course |
| Chanyoung Ahn | M.S. in Robotics (2024) | KIST |
| Jinwoo Kim | M.S. in School of Computing (2024) | ROBOTIS |
| Ju-chul Shin | M.S. in Software Engineering (2024) | LIG Nex1 (LIG넥스원) |
| Seohee Choy | Visiting Scholar (2025) | University of Wisconsin–Madison |
| Teetat Thamronglak | Summer Internship (2025) | Chulalongkorn University CE Undergraduate |
| Jisang Park | Research Assistant (2024-2025) | Stanford CS MS |
| Gyeongwu Kim | Summer Internship (2024) | MIT CS Undergraduate |

## 최근 논문 목록 (2021–2026)

국제 학술지 6편, 국제 학회 15편, 국내 학회 9편으로 총 30편이다. 로봇 조작과 이동, 행동 학습, 언어 지시 해석, 작업·동작 계획을 다룬다. 제목·저자·발표처·연도는 랩 목록의 표기다. 학회 목록의 채택 표시는 유지했다.[^international][^domestic]

**2026**

- Nayoung Oh, Dohyun Kim, Junhyeong Bang, Rohan Paul, Daehyung Park. "C2F-SPACE: Coarse-to-Fine Space Grounding for Spatial Instructions using Vision-Language Models". *Intelligent Service Robotics (ISR), 2026*.
- Wonjae Kang\*, Geonwoo Kim\*, Minseok Song, Daehyung Park (\*- authors contributed equally). "Sling2Sim2Real: One-Shot Elastic System Identification for Non-Destructive Slingshot Policy Learning". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2026 (채택)*.
- Deokmin Hwang, Minseok Song, Daehyung Park. "ParCo-SDF: Learning Prior-Free Partial-to-Complete Signed Distance Fields of Deformable Objects". *International Conference on Ubiquitous Robots (UR), 2026*.
- Keonyoung Koh, Moonkyeong Jung, Samuel Seungsup Lee, Daehyung Park. "SuReNav: Superpixel Graph-based Constraint Relaxation for Navigation in Over-constrained Environments". *IEEE International Conference on Robotics and Automation (ICRA), 2026*.
- Nayoung Oh, Jaehyung Jang, Moonkyeong Jung, Daehyung Park. "DiSPo: Diffusion-SSM based Policy Learning for Coarse-to-Fine Action Discretization". *IEEE International Conference on Robotics and Automation (ICRA), 2026*.

**2025**

- Minwoo Cho, Jaehwi Jang, Daehyung Park. "ILCL: Inverse Logic-Constraint Learning from Temporally Constrained Demonstrations". *IEEE Robotics and Automation Letters (RA-L), 2025*.
- Yeseung Kim\*, Nayoung Oh\*, Jun Park\*, Teetat Thamronglak\*, Daehyung Park (\*- authors contributed equally). "A Visuo-Tactile Data Collection System with Haptic Feedback for Coarse-to-Fine Imitation Learning". *Conference on Robot Intelligence Technology and Applications (RiTA), 2025*.
- Minseok Song, JeongHo Ha, Bonggyeong Park, Daehyung Park. "Implicit Neural-Representation Learning for Elastic Deformable-Object Manipulation". *Robotics: Science and Systems (RSS), 2025*.
- Junhyeong Bang, Dohyun Kim, Ahyoung Seong, Daehyung Park. "A Training Dataset for Pixelwise Grounding of Object Placement from Natural Language Instructions". *Institute of Control, Robotics and Systems (ICROS), 2025*.
- Seunghyuk Hyun, Minwoo Cho, Daehyung Park. "Automated Reset System for Real-world Shallow Depth-Insertion Policy Learning". *Institute of Control, Robotics and Systems (ICROS), 2025*.

**2024**

- Yeseung Kim, Dohyun Kim, Jieun Choi, Jisang Park, Nayoung Oh, Daehyung Park. "A Survey on Integration of Large Language Models with Intelligent Robots". *Intelligent Service Robotics, 2024*.
- Jinwoo Kim\*, Keonyoung Koh\*, Samuel Seungsup Lee, Yohan Park, Daehyung Park (\*- authors contributed equally). "Reactive Constraint Relaxation for Urban Environment Navigation". *Conference on Robot Intelligence Technology and Applications (RiTA), 2024*.
- Minjae Song, Yeseung Kim, Minjun Kim, Daehyung Park. "Graph-based 3D Collision-distance Estimation Network with Probabilistic Graph Rewiring". *IEEE International Conference on Robotics and Automation (ICRA), 2024*.
- Dohyun Kim, Nayoung Oh, Deokmin Hwang, Daehyung Park. "LINGO-Space: Language-Conditioned Incremental Grounding for Space". *Association for the Advancement of Artificial Intelligence (AAAI), 2024*.
- Minseok Song, Bonggyeong Park, Daehyung Park. "Development of VR Teleoperation System and Collecting Demonstration for Deformable Object Manipulation". *Institute of Control, Robotics and Systems (ICROS), 2024*.

**2023**

- Jaehwi Jang, Minjae Song, Daehyung Park. "Inverse Constraint Learning and Generalization by Transferable Reward Decomposition". *IEEE Robotics and Automation Letters (RA-L), 2023*.
- Dohyun Kim\*, Yeseung Kim\*, Jaehwi Jang\*, Minjae Song\*, Woojin Choi, Daehyung Park (\*- authors contributed equally). "SGGNet2: Speech-Scene Graph Grounding Network for Speech-guided Navigation". *IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), 2023*.
- Kanghyun Kim, Daehyung Park, Min Jun Kim. "A Reachability Tree-Based Algorithm for Robot Task and Motion Planning". *IEEE International Conference on Robotics and Automation (ICRA), 2023*.
- Minsung Yoon, Mincheul Kang, Daehyung Park, and Sung-Eui Yoon. "Learning-Based Initialization of Trajectory Optimization for Path-Following Problems of Redundant Manipulators". *IEEE International Conference on Robotics and Automation (ICRA), 2023*.

**2022**

- Yeseung Kim, Jinwoo Kim, Daehyung Park. "GraphDistNet: A Graph-based Collision-distance Estimator for Gradient-based Trajectory". *IEEE Robotics and Automation Letters (RA-L), 2022*.
- Howard, T., Stump, E., Fink, J., Arkin, J., Paul, R., Park, D., Roy, S., Barber, D., Bendell, R., Schmeckpeper, K., Tian, J., Oh, J., Wigness, M., Quang, L., Rothrock, B., Nash, J., Walter, M., Jentsch, F., & Roy, N. "An Intelligence Architecture for Grounded Language Communication with Field Robots". *Field Robotics, 2(1), 2022*.
- Dohyun Kim\*, Jinwoo Kim\*, Minwoo Cho, Daehyung Park (\*- authors contributed equally). "Natural Language-Guided Navigation using Scene Graph". *Conference on Robot Intelligence Technology and Applications (RiTA), 2022*.
- Hyeongyeol Ryu, Minsung Yoon, Daehyung Park, Sung-eui Yoon. "Confidence-based Robot Navigation under Sensor Occlusion with Deep Reinforcement Learning". *IEEE International Conference on Robotics and Automation (ICRA), 2022*.
- Ulzhalgas Rakhman, Jaehoon Yoo, Yeseung Kim, Deokmin Hwang, Seunghoon Hong, Daehyung Park. "Reactive Task Planning using Scene Graph for Robust Robotic Manipulation". *Korea Robotics Society Annual Conference (KRoC), 2022*.
- Jaehwi Jang and Daehyung Park. "Transferable-Reward Decomposition for Inverse Reinforcement Learning". *Korea Robotics Society Annual Conference (KRoC), 2022*.
- Bonggyeong Park, Chanyoung Ahn, Daehyung Park. "A Telemanipulation Suite for Deformable Object Manipulation". *Korean Artificial intelligence Association (KAIA), 2022*.
- Jinwoo Kim, Dohyun Kim, Daehyung Park. "A Framework for Natural Language-guided Semantic Mapping and Mobile Navigation". *Korea Robotics Society Annual Conference (KRoC), 2022*.

**2021**

- Shen Li\*, Daehyung Park\*, Yoonchang Sung\*, Julie Shah, Nicholas Roy (\*- authors contributed equally). "Reactive Task and Motion Planning under Temporal Logic Specifications". *IEEE International Conference on Robotics and Automation (ICRA), 2021*.
- Minsung Yoon, Daehyung Park, Sung-Eui Yoon. "Bias tree expansion using reinforcement learning for efficient motion planning". *Korea Robotics Society Annual Conference (KRoC), 2021*.
- Hyeongyeol Ryu, Minsung Yoon, Daehyung Park, Sung-Eui Yoon. "Robust Robot Navigation against External Disturbance using Deep Reinforcement Learning". *Korea Robotics Society Annual Conference (KRoC), 2021*.

## 수상과 선정

Awards 페이지에 게시된 2022–2025년 수상·선정 9건이다. 연도만 적힌 항목은 해당 연도로 표시했으며, 최종 후보(finalist)는 수상과 구분해 원문대로 적는다.[^awards]

- 2024 · Jinwoo Kim, Keonyoung Koh, Samuel Seungsup Lee, Yohan Park, Daehyung Park, Best Student Paper Award , International Conference on Robot Intelligence Technology and Applications (RiTA)
- 2023 · Minsung Yoon, Mincheul Kang, Daehyung Park, and Sung-Eui Yoon, Outstanding Planning Paper Award , International Conference on Robotics and Automation (ICRA)
- 2022 · Dohyun Kim\*, Jinwoo Kim\*, Minwoo Cho, Daehyung Park, Best Student Paper Award , International Conference on Robot Intelligence Technology and Applications (RiTA)
- 2022 · Hyeongyeol Ryu, Minsung Yoon, Daehyung Park, Sung-eui Yoon, Outstanding Navigation paper finalist , International Conference on Robotics and Automation (ICRA)
- 2022 · Daehyung Park, Google Research Scholar Award , Google
- 2025 · Seunghyuk Hyun et al. 학부생논문상 , 제어로봇시스템학회
- 2024 · Minseok Song et al. 학부생우수논문상 , 제어로봇시스템학회
- 2022 · Ulzhalgas Rakhman et al., 우수논문상 , 한국로봇종합학술대회
- 2022 · Daehyung Park, 우수신진연구자상 , 제어로봇시스템학회

## 소식

2022–2026년 소식 30건이다. 날짜가 적힌 항목은 그 날짜를, 연도만 적힌 항목은 연도를 표시했다. 아래의 논문 채택·게재 승인 소식은 당시 공지 내용을 나타낸다.[^news]

- 2026-06-24 · DiSPo 연구가 연합뉴스 등 언론에 소개되었다.
- 2025 · Minwoo Cho와 Jaehwi Jang의 ILCL 논문이 RA-L에 게재 승인되었다.
- 2025 · Yeseung Kim, Nayoung Oh, Jun Park, Teetat Thamronglak의 논문이 RiTA에 채택되었다.
- 2025 · 박대형 교수가 George Washington University의 University Seminar Series에서 강연했다.
- 2025 · 박대형 교수가 International Robot Learning Symposium에서 강연했다.
- 2025-08-21 · INR-DOM 연구가 동아사이언스 등 언론에 소개되었다.
- 2025 · Seunghyuk Hyun과 Minwoo Cho가 제어로봇시스템학회 학부생논문상을 받았다.
- 2025-04-22 · INR-DOM 연구가 KI 소식지에 소개되었다.
- 2025 · Minseok Song과 JeongHo Ha의 논문이 RSS에 채택되었다.
- 2025-04-10 · 연구실이 K-Humanoid 연합에 참여했다.
- 2025 · 연구실이 인공지능산업융합사업단(AICA)을 통해 NVIDIA H100 GPU 8개를 지원받았다.
- 2025 · 현대자동차의 지원으로 Unitree G1 휴머노이드 로봇이 연구실에 도입되었다.
- 2025-01-15 · 연구실이 조선일보의 「사람 말 알아듣고 똑똑해진 로봇」 기사에 소개되었다.
- 2024 · 연구실이 RiTA Best Student Paper Award를 받았다.
- 2024 · 박대형 교수가 Humanoids에서 인간과의 상호작용을 통한 과제 학습을 주제로 워크숍을 조직한다는 소식을 알렸다.
- 2024 · 박대형 교수가 International Elite Robotics Summer School에서 기조강연을 했다.
- 2024 · Minseok Song이 제어로봇시스템학회 학생논문상을 받았다.
- 2024 · Minseok Song의 논문이 제어로봇시스템학회 학술대회에 채택되었다.
- 2024 · Yeseung Kim의 대형 언어 모델에 관한 종설 논문이 Intelligent Service Robotics에 게재 승인되었다.
- 2024 · Minjae Song의 논문이 IEEE ICRA에 채택되었다.
- 2024 · Dohyun Kim의 논문이 AAAI에 채택되었다.
- 2023 · Jaehwi Jang의 논문이 IEEE RA-L에 게재 승인되었다.
- 2023 · 박대형 교수가 ICRA Outstanding Planning Paper Award를 받았다.
- 2023 · 박대형 교수가 RSS에서 실험 중심 보행·조작 연구 워크숍을 조직한다는 소식을 알렸다.
- 2023 · 박대형 교수가 Ro-MAN에서 보건·의료 분야의 인간과 에이전트·로봇 상호작용 특별 세션을 조직한다는 소식을 알렸다.
- 2022 · 연구실이 RiTA Best Student Paper Award를 받았다.
- 2022 · 논문이 IEEE RA-L에 게재 승인되었다. 랩은 IROS도 함께 표기했다.
- 2022 · 박대형 교수가 제어로봇시스템학회 우수신진연구자상을 받았다.
- 2022 · 연구실이 한국로봇종합학술대회 우수논문상을 받았다.
- 2022 · 연구실이 ICRA Outstanding Navigation Award의 최종 후보로 선정되었다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST E3-1 건물 2429호, 우편번호 34141.[^home][^advisor]
- 교수연구실: E3-1 2429호.[^faculty]
- 전화: +82-42-350-3586.[^advisor]
[^home]: 연구실 첫 화면. <https://rirolab.kaist.ac.kr/> 소속, 협업·서비스 로봇, 학습·추론·계획·인간과 로봇의 상호작용 연구, 주소. 관측일 2026-10-28.
[^advisor]: Advisor. <https://rirolab.kaist.ac.kr/advisor> 부임·승진 시기, 겸무, 학력·경력, 전화·위치. 관측일 2026-10-28.
[^faculty]: 전산학부 교수 상세 소개. <https://cs.kaist.ac.kr/people/view?idx=613&kind=faculty&menu=160> 박대형 부교수, 전공과 연구 분야, 학력·경력, 교수연구실 2429호. 관측일 2026-10-28.
[^topics]: Current Topics. <https://rirolab.kaist.ac.kr/research/topics> 전신 조작, 시연·강화학습, 변형 물체 조작, 작업·동작 계획, 언어 기반 이동·조작. 관측일 2026-10-28.
[^people]: People. <https://rirolab.kaist.ac.kr/people> 교수, 박사후연구원·재학생, Alumni, Past RA & Visiting Scholars. 관측일 2026-10-28.
[^international]: International Publications. <https://rirolab.kaist.ac.kr/publication/international> 국제 학술지·학회 논문 목록. 관측일 2026-10-28.
[^domestic]: Domestic Publications. <https://rirolab.kaist.ac.kr/publication/domestic> 국내 학회 논문 목록. 관측일 2026-10-28.
[^awards]: Awards. <https://rirolab.kaist.ac.kr/news/awards> 수상·선정과 수상자, 연도. 관측일 2026-10-28.
[^news]: Newslist. <https://rirolab.kaist.ac.kr/news/newslist> 연구 성과, 논문 채택·게재 승인, 강연·워크숍·수상·언론 소개 소식. 관측일 2026-10-28.
[^p1]: N. Oh, J. Jang, M. Jung, D. Park, arXiv (사전 공개본) (온라인 2024-09-23). <https://doi.org/10.48550/arXiv.2409.14719> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.14719>. 관측일 2026-10-28.
[^p2]: M. Song, J. Ha, B. Park, D. Park, arXiv (사전 공개본) (온라인 2025-05-01). <https://doi.org/10.48550/arXiv.2505.00500> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2505.00500>. 관측일 2026-10-28.
[^p3]: M. Cho, J. Jang, D. Park, arXiv (사전 공개본) (온라인 2025-07-15). <https://doi.org/10.48550/arXiv.2507.11000> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2507.11000>. 관측일 2026-10-28.
[^p4]: J. Jang, M. Song, D. Park, arXiv (사전 공개본) (온라인 2023-06-21). <https://doi.org/10.48550/arXiv.2306.12357> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2306.12357>. 관측일 2026-10-28.
[^p5]: Y. Kim, J. Kim, D. Park, arXiv (사전 공개본) (온라인 2022-06-03). <https://doi.org/10.48550/arXiv.2206.01517> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2206.01517>. 관측일 2026-10-28.
[^p6]: M. Song, Y. Kim, M. J. Kim, D. Park, arXiv (사전 공개본) (온라인 2023-10-06). <https://doi.org/10.48550/arXiv.2310.04044> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2310.04044>. 관측일 2026-10-28.
[^p7]: D. Kim, N. Oh, D. Hwang, D. Park, arXiv (사전 공개본) (온라인 2024-02-02). <https://doi.org/10.48550/arXiv.2402.01183> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2402.01183>. 관측일 2026-10-28.
[^p8]: S. Li 외, N. Roy, arXiv (사전 공개본) (온라인 2021-03-26). <https://doi.org/10.48550/arXiv.2103.14464> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2103.14464>. 관측일 2026-10-28.

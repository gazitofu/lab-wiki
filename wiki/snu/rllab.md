# 로봇학습 연구실 (Robot Learning Laboratory, RLLAB)

**서울대학교 공과대학 전기·정보공학부 · 오성회 교수**

- 대분야: 컴퓨팅·AI, 기계·로봇·제조
- 태그: 강화학습[^research][^p1], 로봇 조작·파지[^research][^p4], 로봇 항법·SLAM[^p6][^p7], 컴퓨터 비전[^research], 자율주행[^research][^p8]
- 홈페이지: <https://rllab.snu.ac.kr/>

> 사람이 있는 환경에서 로봇이 안전하게 배우고, 주변을 보며 이동하고, 언어 지시에 따라 물체를 다루는 방법을 연구한다.

## 무엇을 연구하나

로봇학습 연구실은 로봇의 행동이 주변 환경을 바꾸고, 바뀐 환경에서 다시 관찰한 정보를 다음 행동에 사용하는 문제를 다룬다. 기계학습(자료에서 규칙을 배워 판단하거나 예측하는 방법)을 실제로 움직이는 로봇에 적용하는 것이 중심이다. 학과 소개는 로봇학습을 중심으로 로보틱스, 컴퓨터 비전(사진·영상에서 물체·사람·장면과 그 속성을 알아내는 기술), 기계학습을 연구한다고 설명한다.[^deptlab]

학습 방법에서는 강화학습(행동의 결과로 받은 보상을 바탕으로 누적 보상을 키우는 행동을 배우는 방법)과 모방학습(시범으로 주어진 행동을 바탕으로 수행 방법을 배우는 방법)을 다룬다. 보상은 행동 결과를 학습 목표에 맞춰 평가한 값이며, 정책은 관찰한 상황에 따라 행동을 정하는 규칙이다. 연구실은 적은 자료로 학습하면서 안전 조건을 지키고, 사람이 함께 지내기 알맞은 로봇 행동을 만드는 것을 목표로 둔다.[^research]

로봇이 어디로 가고 무엇을 움직일지도 연구한다. 시각 항법(카메라로 관찰한 정보를 이용해 위치나 이동 방향·경로를 정하는 방법)에서는 낯선 실내에서 목표를 찾고 충돌을 피하는 문제를 다룬다. 물체 조작에서는 사람이 말로 요청한 배치를 로봇 팔의 실행 계획으로 바꾼다. 휴머노이드(사람의 몸 구조를 본뜬 로봇)에서는 이동과 물체 조작을 이어서 수행하도록 학습한다.[^p4][^p5][^p6][^p7]

## 주요 연구 주제

### 효율적이고 안전한 로봇 학습

오프라인 강화학습(미리 모은 경험 자료로 행동 규칙을 배우는 강화학습)으로 여러 단계 뒤의 결과를 고려하는 의사결정을 연구한다. Universal Horizon Models는 원하는 시점의 미래 상태를 직접 예측하는 방법이다. 상태는 의사결정에 사용하는 환경과 수행 주체의 상황을 나타낸 정보다. 다른 연구는 과제 수행에 필요한 변화와 주변 상황을 나눠, 경험하지 못한 목표와 상황의 조합에도 행동을 적용하려 한다.[^p1][^p2] 안전성 연구에서는 여러 목표의 개선 방향이 충돌하지 않도록 조정하면서 안전 조건을 함께 반영한다.[^p3]

### 언어 지시와 로봇 조작

사람이 말로 정한 목표를 물체 사이의 관계와 실제 행동으로 연결한다. 장면 그래프(물체와 물체 사이의 관계를 점과 연결선으로 나타낸 구조)를 이용해 현재 배치에서 목표 배치로 가는 계획을 세우고, 로봇이 그 계획을 실행할 수 있는지 확인한다. 대규모 언어 모델(Large Language Model, 많은 언어 자료에서 학습해 문맥에 따른 언어 처리를 수행하는 모델)은 언어 목표를 장면 그래프로 바꾸는 데 쓰인다.[^p4] 시각·언어·행동 모델(Vision-Language-Action Model, 영상과 언어 정보를 로봇의 행동 출력으로 연결하는 모델)을 이용한 휴머노이드 연구에서는 나눠서 수집한 이동·조작 시범으로 두 행동의 전환을 학습한다.[^p5]

### 시각 기반 로봇 항법

실내 로봇이 낯선 공간에서 목표에 도달하는 과정을 연구한다. RVN-Bench(A Benchmark for Reactive Visual Navigation)는 미리 주어진 지도 없이 시각 관찰로 여러 목표 위치를 차례로 찾아가되 충돌을 피하도록 하는 평가 환경이다. 성공 여부와 함께 충돌을 고려하고, 학습용 이동 기록을 만드는 도구를 제공한다.[^p6] Meta-Explore는 언어 지시를 잘못 따라간 뒤, 관찰할 수 있지만 아직 방문하지 않은 지점 가운데 중간 목표를 골라 경로를 수정한다. 이를 위해 주변 물체의 배치를 수학적으로 나타낸 정보를 이용한다.[^p7]

### 도로 구조를 이용한 자율주행

자율주행(차량이 주변을 인식하고 이동 경로와 행동을 정해 스스로 주행하는 기술)에서는 도로의 연결 구조와 영상 속 물체의 관계를 함께 고려한다. RIANet(Road Graph and Image Attention Network)은 도로 구조 정보를 이용해 영상의 어떤 물체에 주의를 둘지 계산하고, 이를 차량 제어로 연결한다. 도시 주행을 재현한 가상 환경에서 학습과 평가를 수행했다.[^p8]

## 대표 논문

최근 논문 가운데 로봇 학습, 언어 지시와 물체 조작, 시각 항법, 자율주행을 함께 보여 주는 8편을 골랐다. 모든 논문에 오성회 교수가 저자로 참여하며, 논문 첫 쪽에 서울대학교 소속과 교신저자 표기가 있다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 연도·학회는 연구실 논문 목록의 표기다.[^pubs]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | Offline Reinforcement Learning with Universal Horizon Models · ICML | 미리 모은 자료에서 학습할 때 미래를 한 단계씩 반복 예측하면 오차가 누적될 수 있다. 원하는 단계 뒤의 상태를 직접 예측하는 Universal Horizon Models를 제안하고, 지나치게 먼 미래에 대한 예측 범위를 제한해 학습을 안정화했다. OGBench의 과제에서 기존 비교 방법보다 좋은 결과를 보였으며, 특히 질이 낮은 자료와 장기 추론이 필요한 과제를 다뤘다.[^p1] | 교신저자·마지막 저자 |
| 2 | 2026 | Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning · ICML | 과제에서 바뀌어야 할 것과 주변 상황을 구분해, 이미 배운 행동을 새로운 상황의 목표에 조합하는 방법을 제안했다. 과제 수행에 필요한 변화를 담는 표현(정보를 계산에 쓸 수 있게 나타낸 형태)을 만들고, 경험 자료에서 보지 못한 변화와 상황의 조합에도 계획을 적용하도록 했다. OGBench의 물체 조작 환경에서 효과를 확인했다.[^p2] | 교신저자·마지막 저자 |
| 3 | 2025 | Conflict-Averse Gradient Aggregation for Constrained Multi-Objective Reinforcement Learning · ICLR | 로봇이 여러 목표를 추구하면서 안전 조건도 지키도록 CoMOGA(Constrained Multi-Objective Gradient Aggregator)를 제안했다. 각 목표의 개선 방향이 충돌하는 문제와 안전 제약을 하나의 계산 문제로 다룬다. 상태와 행동을 표로 나타내는 조건에서 전체 최적의 답에 가까워짐을 보장했고, 실험 과제에서 제약 충족을 확인했다.[^p3] | 교신저자·마지막 저자 |
| 4 | 2025 | Language-Guided Hierarchical Planning with Scene Graphs for Tabletop Object Rearrangement · IROS | ‘물체를 정리하라’는 언어 목표를 물체 사이의 관계로 바꾼 뒤, 그 관계에 맞는 배치와 로봇 행동을 계획했다. 언어 목표를 장면 그래프로 바꾸고, 실제 로봇 조작으로 실행할 수 있는지 확인한다. 실험에서는 일반적인 언어 목표를 처리하고 사람이 선호하는 배치를 만들었으며, 가상 환경에서 실제 로봇으로 옮기기 위한 조정 없이 실물 적용을 보였다.[^p4] | 교신저자·마지막 저자 |
| 5 | 2026 | Learning Humanoid Loco-Manipulation with Responsibility-Induced Specialized Experts for Vision-Language-Action Models · IROS | 이동과 물체 조작의 시범을 따로 수집해도 두 행동을 이어 수행하도록 RISE(Responsibility-Induced Specialized Experts)를 제안했다. 행동 유형별로 전문화되는 여러 모델을 학습하고, 실행 중 각 모델의 비중을 조정해 전환 시점을 정한다. 가상 환경과 실제 휴머노이드에서 이동·조작을 여러 차례 전환하는 과제를 평가했다.[^p5] | 교신저자·마지막 저자 |
| 6 | 2026 | RVN-Bench: A Benchmark for Reactive Visual Navigation · IROS | 실내 이동 로봇이 시각 정보만으로 낯선 환경의 여러 목표를 차례로 찾아가면서 충돌을 피하는지 평가할 수 있도록 했다. 충돌을 고려한 과제와 평가 기준, 학습용 이동 기록 생성 도구를 제공한다. 학습된 행동이 새로운 가상 환경에도 적용됨을 보였고, 실제 이동 로봇의 초기 실험에서는 가상 환경에서 배운 행동을 실물에 옮길 가능성을 보였다.[^p6] | 교신저자·마지막 저자 |
| 7 | 2023 | Meta-Explore: Exploratory Hierarchical Vision-and-Language Navigation Using Scene Object Spectrum Grounding · CVPR | 로봇이 언어 지시와 다른 길로 간 뒤 경로를 바로잡는 방법이다. 아직 가 보지 않았지만 관찰할 수 있는 장소 가운데 중간 목표를 고르고, 주변 물체의 배치를 이용해 그 목표를 선택한다. 세 가지 평가 자료에서 시험했으며, 제안한 물체 배치 정보를 이용한 중간 목표 탐색이 목표 도달 성능을 높였다.[^p7] | 공동 교신저자·마지막 저자 |
| 8 | 2022 | RIANet: Road Graph and Image Attention Network for Urban Autonomous Driving · IROS | 도로의 연결 구조를 이용해 영상 속 물체의 중요도를 계산하는 차량 주행 방법이다. 도로·영상·장면 정보를 함께 처리해 차량 제어에 이용한다. 도시 주행을 재현한 CARLA 가상 환경에서 학습하고 평가해 기존 비교 방법보다 좋은 주행 결과를 보였다.[^p8] | 교신저자·마지막 저자 |

## 교수와 전문 분야

오성회 교수는 UC Berkeley에서 전기컴퓨터공학 학사(1995), 석사(2003), 박사(2006)를 받았다. Intel의 설계 엔지니어, Synopsys의 선임 소프트웨어 엔지니어를 거쳤고, 2007년 UC Berkeley 박사후연구원, 2007–2009년 UC Merced 조교수로 일했다. 현재 서울대학교 전기·정보공학부 교수다.[^prof][^deptprof]

교수 소개의 연구 관심은 로보틱스, 컴퓨터 비전, 기계학습, 사이버 물리 시스템(계산·통신과 실제 물리 과정이 서로 연결되는 시스템)이다.[^prof] 대표 논문으로 보면 전문 분야는 미래 결과를 고려하는 로봇 학습과 안전 제약 처리, 언어 목표를 행동으로 바꾸는 조작 계획, 시각 기반 이동과 자율주행이다.[^p1][^p3][^p4][^p6][^p8]

IEEE Robotics and Automation Letters 부편집장(2017–2022), IEEE Transactions on Robotics 부편집장(2019–2022)을 맡았으며, 교수 소개는 2026년부터 IEEE Transactions on Robot Learning 부편집장으로 적는다.[^prof]

## 응용 분야

연구실이 제시한 응용은 자율 배송 로봇과 가사 로봇이다. 영상과 언어 정보를 이용해 사람과 함께 지내는 로봇을 만들고, 주문 관리·연계 배송·자율 배송 차량·실시간 차량군 관리가 포함된 배송 플랫폼을 연구한다.[^research] 대표 논문은 탁상 물체 정리, 휴머노이드의 이동과 조작, 실내 이동 로봇의 충돌 회피, 도시 자율주행으로 이어진다.[^p4][^p5][^p6][^p8]

## 구성원

2026년 10월 28일 People의 Graduate Students 구획에 게시된 17명이다. 개인 소개에서 박사과정을 적은 8명은 그 표기를 반영했고, 나머지 9명은 대학원생으로 적었다. 연구 주제는 People의 Research Area 표기다.[^people][^memberdetail] ‘대표 논문 참여’는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Wooseok Oh | 대학원생 | Robotics, Machine Learning | 4, 5 |
| Hongjung Lee | 박사과정 | Representation Learning, Continual Learning, Machine Learning |  |
| Jeongwoo Oh | 대학원생 | Driving Automation, Robotics | 6, 8 |
| Jaeyeon Jeong | 대학원생 | Robotics, Human-Robot Interaction | 5, 7 |
| Hojun Chung | 박사과정 | Robotics, Reinforcement Learning | 1, 8 |
| Junseo Lee | 박사과정 | Reinforcement Learning, Robotics | 1 |
| Junseok Kim | 박사과정 | Reinforcement Learning, Robotics | 2 |
| Jaewon Lee | 박사과정 | Reinforcement Learning, Robotics | 6 |
| Hyeokjin Kwon | 박사과정 | Reinforcement Learning, Robotics |  |
| Geunje Cheon | 박사과정 | Robotics, Machine Learning |  |
| Yoseph Park | 대학원생 | Robotics, Machine Learning |  |
| Minsoo Kim | 대학원생 | Robotics, Computer Vision | 7 |
| Jooyoung Kim | 박사과정 | Robotics, Reinforcement Learning, World Models, 3D Computer Vision | 5 |
| Hosung Lee | 대학원생 | Robotics, Vision-Language-Action Models, Humanoid | 5 |
| Hyeondal Son | 대학원생 | Robotics, Machine Learning | 5 |
| Seoyoung Lim | 대학원생 | Autonomous Driving |  |
| Jaeseok Yang | 대학원생 | Robotics, Reinforcement Learning |  |

## 졸업생과 이전 구성원

Alumni의 박사 26명, 석사 8명, 이전 학부생 6명으로 총 40개 항목이다. 연도는 2010–2026년의 누리집 표기이고, 진로와 학위 논문 제목도 누리집이 적은 내용이다. 이전 학부생 가운데 학위가 적혀 있지 않은 사람은 그 구획명으로 표시했다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Minjae Kang | Ph.D. (2026) | at Samsung Advanced Institute of Technology (Suwon, KOREA) | Long-Horizon and Complex Robotic Task Learning Using Reusable and Adaptable Policies |
| Jeongho Park | Ph.D. (2026) | at Samsung Research (Seoul, KOREA) | Context-Aware Multi-Agent Decision Making and Learning for Cooperative Robot Systems |
| Howoong Jun | Ph.D. (2026) | at Samsung Robotics eXperience (Seoul, KOREA) | Efficient 3D Visual Representation for Robotic Spatial Intelligence: Localization, Navigation, and Semantic Mapping |
| Hogun Kee | Ph.D. (2026) | at NVIDIA (Seoul, KOREA) | Vision-Based Hierarchical Policy Learning for Robotic Object Rearrangement |
| Gunmin Lee | Ph.D. (2025) | at LG CNS (Seoul, KOREA) | Designing Robust Autonomous Driving Controller Using Mixed Quality Demonstrations |
| Mineui Hong | Ph.D. (2025) | at CMU (PA, USA) | Latent State Representation Learning for Long-Horizon Robot Tasks and Planning |
| Dohyeong Kim | Ph.D. (2025) |  | Spectral-Risk Multi-Objective Reinforcement Learning |
| Obin Kwon | Ph.D. (2024) | at Tesla (CA, USA) | Scene Representation Learning for Visual Navigation |
| Jaegu Choy | Ph.D. (2024) |  | Motion-Based Unsupervised 3D Part Segmentation of Articulated Objects via Visual Information |
| Hwiyeon Yoo | Ph.D. (2024) | at Naver Labs (Seongnam, KOREA) | Efficient and Effective Visual Context-Based Topological Representations for Embodied Agent Navigation |
| Yunho Choi | Ph.D. (2024) | at Samsung Robotics eXperience (Seoul, KOREA) | Efficient Decision-Making of Embodied Agents Using Local Interest Points |
| Nuri Kim | Ph.D. (2023) | a professor at Jeonbuk National University (Jeonju, KOREA) | Robust Semantic Visual Graphs for Navigation of Embodied Agents |
| Taeoh ha (Timothy Ha) | Ph.D. (2023) | at Samsung Advanced Institute of Technology (Suwon, KOREA) | Learning-Based Autonomous Vehicle Navigation Using Road Graph Networks |
| Seunggyu Chang | Ph.D. (2022) | at Naver (Seongnam, KOREA) | Modeling 3D Humans from Multiple Cues: 3D Data Acquisition, Reconstruction, and Motion Generation |
| Chanho Ahn | Ph.D. (2022) | at Samsung Advanced Institute of Technology (Suwon, KOREA) | Instance-Based Network Architecture Selection for Multi-Task and Incremental Learning |
| Kyungjae Lee | Ph.D. (2021) | a professor at Korea University (Seoul, KOREA) | Sample Efficient Robot Learning for Optimal Decision Making under Uncertain and Complex Environments |
| Kyunghoon Cho | Ph.D. (2020) |  | Learning-Assisted Rule-Based Vehicle Navigation under Complex Circumstances |
| Hyemin Ahn | Ph.D. (2020) | a professor at POSTECH (Pohang, KOREA) | Context-Aware Robot Behavior Learning for Practical Human-Robot Interaction |
| Geonho Cha | Ph.D. (2019) | at Naver (Seongnam, KOREA) | Non-Rigid 3D Structure Reconstruction Using Part-Based Models and Its Practical Extensions |
| Donghoon Lee | Ph.D. (2019) | at Tesla (CA, USA) | Structured Visual Understanding from Local Parts: Sparsity, Randomness, Correlation, and Deep Networks |
| Sungjoon Choi | Ph.D. (2018) | a professor at Korea University (Seoul, KOREA) | Robust Learning from Demonstration with Leverage Optimization |
| Yoonseon Oh | Ph.D. (2018) | a professor at Hanyang University (Seoul, KOREA) | Robust Target Tracking and Navigation for Mobile Robots with Guaranteed Performance |
| Inhwan Hwang | Ph.D. (2018) | at Samsung Research (Seoul, KOREA) | Situation Understanding Using Smart Devices and Its Applications |
| Eunwoo Kim | Ph.D. (2017) | a professor at Chung-Ang University (Seoul, KOREA) | Robust Subspace Learning and Clustering: Sparse and Low-Rank Representations |
| Jungchan Cho | Ph.D. (2016) | a professor at Gachon University (Seongnam, KOREA) | Probabilistic 3D Human Pose Recovery and Its Application to Action Recognition |
| Junghun Suh | Ph.D. (2016) | at Kakao Mobility (Seongnam, KOREA) | Robust Localization and Efficient Path Planning for Mobile Sensor Networks |
| Subin Shin | M.S. (2026) |  |  |
| Minyoung Hwang | M.S. (2023) |  |  |
| Kyungdo Kim | M.S. (2021) | at Seoul National University Hospital (Seoul, KOREA) |  |
| Hyunjun Kim | M.S. (2017) | at SuaLab (Seoul, KOREA) |  |
| Joonsig Gong | M.S. (2015) | at Lee & Ko IP (Seoul, KOREA) |  |
| HyeongSeok Oh | M.S. (2013) |  |  |
| Sangseok Yoon | M.S. (2012) |  |  |
| Junyoung Kim | M.S. (2011) | at ALTIBASE (Seoul, KOREA) |  |
| Eunjeong Park | B.S. (2015) |  |  |
| Kiwoo Shin | B.S. (2015) |  |  |
| Minsu Kang | B.S. (2012) |  |  |
| Juyong Kim | Former Undergraduate Students (2011) |  |  |
| Seungil You | B.S. (2011) |  |  |
| MoonSeung Baeg | Former Undergraduate Students (2010) |  |  |

## 최근 논문 목록 (2021–2026)

Publications와 Domestic Publications의 2021–2026년 항목 99행이다. 국제 학술지 19행, 국제 학회 64행, 기술보고 2행, 국내 학회 14행이며, 같은 학술지 논문을 학회 발표(RA-L option)로도 적은 8쌍을 포함한다. 연도는 누리집의 서지 표기다. ‘게재 승인’과 ‘채택’은 각각 학술지와 학회 항목의 Accepted 표기를 옮긴 것이다.[^pubs][^domestic]

**2026**

- Hongjung Lee, Jae Goo Choy, Howoong Jun, Jeongwoo Oh, and Songhwai Oh. "GAP3D: Geometry-Aware Adaptive Planar Representations for 3D Occupancy Prediction". *IEEE Robotics and Automation Letters, 2026. (게재 승인)*.
- Jeongho Park, Hyeondal Son, Hyeokjin Kwon, Geunje Cheon, Jooyoung Kim, Minjae Kang, and Songhwai Oh. "LF-Former: A Multi-Agent Policy with Ordered Decision Structures for Multi-Arm Manipulation". *IEEE Robotics and Automation Letters, vol. 11, no. 11, pp. 12432-12439, Nov. 2026. (게재 승인)*.
- Gunmin Lee, Jaeseok Heo, Dohyeong Kim, Geunje Cheon, Jeongwoo Oh, Minyoung Hwang, Chanwoo Park, and Songhwai Oh. "SafeIL: Safety Constrained Imitation Learning for Autonomous Systems". *Robotics and Autonomous Systems, vol. 199, May 2026, 105376. (게재 승인)*.
- Howoong Jun, Seongbo Ha, Jaewon Lee, Hyeonwoo Yu, and Songhwai Oh. "Memory-Efficient Voxelized Renderable Neural 3D Spatial Representation for Vision-Based Robotics". *IEEE Robotics and Automation Letters, vol. 11, no. 1, pp.113-120, Jan. 2026*.
- Junseo Lee, Hyeokjin Kwon, and Songhwai Oh. "AEGIS: Almost Surely Safe Offline Reinforcement Learning". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2026. (채택)*.
- Hogun Kee, Wooseok Oh, Jooyoung Kim, Jaeyeon Jeong, Hyewoo Jeong, Hyeondal Son, Ho Sung Lee, Minjae Kang, and Songhwai Oh. "Learning Humanoid Loco-Manipulation with Responsibility-Induced Specialized Experts for Vision-Language-Action Models". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Sep. 2026. (채택)*.
- Jaewon Lee, Jae Seok Heo, Gunmin Lee, Howoong Jun, Jeongwoo Oh, and Songhwai Oh. "RVN-Bench: A Benchmark for Reactive Visual Navigation". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Sep. 2026. (채택)*.
- Hojun Chung, Junseo Lee, and Songhwai Oh. "Offline Reinforcement Learning with Universal Horizon Models". *in Proc. of the International Conference on Machine Learning (ICML), Jul. 2026. (채택)*.
- Junseok Kim, Dohyeong Kim, Mineui Hong, and Songhwai Oh. "Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning". *in Proc. of the International Conference on Machine Learning (ICML), Jul. 2026. (채택)*.
- Hogun Kee, Wooseok Oh, Minjae Kang, Hyemin Ahn, and Songhwai Oh. "Tidiness Score-Guided Monte Carlo Tree Search for Visual Tabletop Rearrangement". *IEEE International Conference on Robotics and Automation (ICRA), Jun. 2026. (RA-L option)*.
- Minjae Kang, Mineui Hong, and Songhwai Oh. "Playbook: Scalable Discrete Skill Discovery from Unstructured Datasets for Long-Horizon Decision-Making Problems". *IEEE International Conference on Robotics and Automation (ICRA), Jun. 2026. (RA-L option)*.
- Howoong Jun, Seongbo Ha, Jaewon Lee, Hyeonwoo Yu, and Songhwai Oh. "Memory-Efficient Voxelized Renderable Neural 3D Spatial Representation for Vision-Based Robotics". *IEEE International Conference on Robotics and Automation (ICRA), Jun. 2026. (RA-L option)*.

**2025**

- Minjae Kang, Mineui Hong, and Songhwai Oh. "Playbook: Scalable Discrete Skill Discovery from Unstructured Datasets for Long-Horizon Decision-Making Problems". *IEEE Robotics and Automation Letters, vol. 10, no. 10, pp. 10162-10169, Oct. 2025*.
- Hogun Kee, Wooseok Oh, Minjae Kang, Hyemin Ahn, and Songhwai Oh. "Tidiness Score-Guided Monte Carlo Tree Search for Visual Tabletop Rearrangement". *IEEE Robotics and Automation Letters, vol. 10, no. 10, pp.10090-10097, Oct. 2025*.
- Geunje Cheon, Junseok Kim, Gunmin Lee, Subin Shin, Jeongho Park, Jaewon Lee, Hyeokjin Kwon, and Songhwai Oh. "Multi-Agent Tsallis Actor-Critic for Autonomous Vehicle Fleet Coordination on Road Graph Networks". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Nov. 2025*.
- Minjae Kang, Hogun Kee, Hosung Lee, and Songhwai Oh. "Automatic Real-to-Sim-to-Real System through Iterative Interactions for Robust Robot Manipulation Policy Learning with Unseen Objects". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2025*.
- Jeongho Park and Songhwai Oh. "Context-Aware Multi-Agent Trajectory Transformer". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2025*.
- Wooseok Oh, Hogun Kee and Songhwai Oh. "Language-Guided Hierarchical Planning with Scene Graphs for Tabletop Object Rearrangement". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2025*.
- Dohyeong Kim, Hyeokjin Kwon, Junseok Kim, Gunmin Lee, and Songhwai Oh. "Stage-Wise Reward Shaping for Acrobatic Robots: A Constrained Multi-Objective Reinforcement Learning Approach". *in Proc of the IEEE International Conference on Robotics and Automation (ICRA), May 2025*.
- Dohyeong Kim, Mineui Hong, Jeongho Park, and Songhwai Oh. "Conflict-Averse Gradient Aggregation for Constrained Multi-Objective Reinforcement Learning". *in Proc. of the International Conference on Learning Representations (ICLR), Apr. 2025*.

**2024**

- Nuri Kim, Jeongho Park, Mineui Hong, and Songhwai Oh. "Semantic Environment Atlas for Object-Goal Navigation". *Knowledge-Based Systems, vol. 304, article 112446, Nov. 2024*.
- Hwiyeon Yoo, Yunho Choi, Jeongho Park, and Songhwai Oh. "Commonsense-Aware Object Value Graph for Object Goal Navigation". *IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4423-4430, May 2024*.
- Hojun Chung, Junseo Lee, Minsoo Kim, Dohyeong Kim, and Songhwai Oh. "Adversarial Environment Design via Regret-Guided Diffusion Models". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2024. (Spotlight 발표)*.
- Dohyeong Kim, Taehyun Cho, Seungyub Han, Hojun Chung, Kyungjae Lee, and Songhwai Oh. "Spectral-Risk Safe Reinforcement Learning with Convergence Guarantees". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2024*.
- Hogun Kee and Songhwai Oh. "Scene Generation for Object Rearrangement with Latent Diffusion Models". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2024*.
- Jeongho Park, Obin Kwon and Songhwai Oh. "Spatially-Conditional 3D Furniture Generation Model for Indoor Scene Synthesis". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2024*.
- Jaeyeon Jeong, Jonghyun Park, and Songhwai Oh. "Effective Exploration Via Tsallis Actor-Critic on 6D Robot Grasping". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Nov. 2024*.
- Minsoo Kim, Obin Kwon, Howoong Jun, and Songhwai Oh. "RNR-Nav: A Real-World Visual Navigation System Using Renderable Neural Radiance Maps". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2024*.
- Jae Goo Choy, Geonho Cha, Hogun Kee, and Songhwai Oh. "Unsupervised 3D Part Decomposition via Leveraged Gaussian Splatting". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2024*.
- Minjae Kang, Hogun Kee, Yoseph Park, Junseok Kim, Jaeyeon Jeong, Geunje Cheon, Jaewon Lee, and Songhwai Oh. "Gradual Receptive Expansion Using Vision Transformer for Online 3D Bin Packing". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2024*.
- Howoong Jun, Hyeonwoo Yu, and Songhwai Oh. "Renderable Street View Map-Based Localization: Leveraging 3D Gaussian Splatting for Street-Level Positioning". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2024*.
- Hyeokjin Kwon, Gunmin Lee, Junseo Lee, and Songhwai Oh. "Safe CoR: A Dual-Expert Approach to Integrating Imitation Learning and Safe Reinforcement Learning Using Constraint Rewards". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2024*.
- Hwiyeon Yoo, Yunho Choi, Jeongho Park, and Songhwai Oh. "Commonsense-Aware Object Value Graph for Object Goal Navigation". *40th Anniversary of the IEEE Conference on Robotics and Automation (ICRA@40), Sep. 2024. (RA-L option)*.
- Obin Kwon, Dongki Jung, Youngji Kim, Soohyun Ryu, Suyong Yeon, Songhwai Oh, and Donghwan Lee. "WayIL: Image-based Indoor Localization with Wayfinding Maps". *in Proc of the IEEE International Conference on Robotics and Automation (ICRA), May 2024*.
- Hojun Chung, Jeongwoo Oh, Jaeseok Heo, Gunmin Lee, and Songhwai Oh. "MAC-ID: Multi-Agent Reinforcement Learning with Local Coordination for Individual Diversity". *in Proc of the IEEE International Conference on Robotics and Automation (ICRA), May 2024*.
- Dohyeong Kim, Mineui Hong, Jeongho Park, and Songhwai Oh. "Scale-Invariant Gradient Aggregation for Constrained Multi-Objective Reinforcement Learning". *arXiv preprint:2403.00282, 2024*.
- 박성제, 이건민, 오성회. "Serial Constrained Policy Optimization for Autonomous Driving". *한국인공지능학회 하계학술대회, Aug. 2024*.
- 오우석, 오성회. "Effective Ensemble Methods for Skeleton-Based Action Recognition Using Extended Hierarchically Decomposed Graphs". *한국인공지능학회 하계학술대회, Aug. 2024*.

**2023**

- Taeoh Ha, Jeongwoo Oh, Gunmin Lee, Jaeseok Heo, Do Hyung Kim, Byungkyu Park, Chang-Gun Lee, and Songhwai Oh. "RIANet++: Road Graph and Image Attention Networks for Robust Urban Autonomous Driving under Road Changes". *IEEE Robotics and Automation Letters, vol. 8, no. 11, pp. 7815-7822, Nov. 2023*.
- Wooseok Oh, Hwiyeon Yoo, Timothy Ha, and Songhwai Oh. "Local Selective Vision Transformer for Depth Estimation Using a Compound Eye Camera". *Pattern Recognition Letters, vol. 167, pp. 82-29, Mar. 2023*.
- Mineui Hong, Minjae Kang, and Songhwai Oh. "Diffused Task-Agnostic Milestone Planner". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2023*.
- Dohyeong Kim, Kyungjae Lee, and Songhwai Oh. "Trust Region-Based Safe Distributional Reinforcement Learning for Multiple Constraints". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2023*.
- Minyoung Hwang, Gunmin Lee, Hogun Kee, Chan Woo Park, Kyungjae Lee, and Songhwai Oh. "Sequential Preference Ranking for Efficient Reinforcement Learning from Human Feedback". *in Proc. of Neural Information Processing Systems (NeurIPS), Dec. 2023*.
- Minjae Kang, Junseok Kim, Hogun Kee, and Songhwai Oh. "Object Rearrangement Planning for Target Retrieval in a Confined Space with Lateral View". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2023*.
- Junseo Lee, Jaeseok Heo, Dohyeong Kim, Gunmin Lee, and Songhwai Oh. "Dual Variable Actor-Critic for Adaptive Safe Reinforcement Learning". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2023*.
- Jeongho Park, Obin Kwon and Songhwai Oh. "Attention-Based Randomized Ensemble Multi-Agent Q-Learning". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2023*.
- Obin Kwon, Jeongho Park, and Songhwai Oh. "Renderable Neural Radiance Map for Visual Navigation". *in Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Jun. 2023*.
- Minyoung Hwang, Jaeyeon Jeong, Minsoo Kim, Yoonseon Oh, and Songhwai Oh. "Meta-Explore: Exploratory Hierarchical Vision-and-Language Navigation Using Scene Object Spectrum Grounding". *in Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Jun. 2023*.
- Jeongwoo Oh, Jaeseok Heo, Junseo Lee, Gunmin Lee, Minjae Kang, Jeongho Park, and Songhwai Oh. "SCAN: Socially-Aware Navigation Using Monte Carlo Tree Search". *in Proc of the IEEE International Conference on Robotics and Automation (ICRA), May 2023*.
- Hogun Kee, Minjae Kang, Dohyeong Kim, Jaegoo Choy, and Songhwai Oh. "SDF-Based Graph Convolutional Q-Networks for Rearrangement of Multiple Objects". *in Proc of the IEEE International Conference on Robotics and Automation (ICRA), May 2023*.
- 기호건, 오성회. "Object Rearrangement with a Mixture of Coherent Point Drift". *정보 및 제어 학술대회, Oct. 2023*.
- 정재연, 오성회. "멀티태스크 강화학습을 위한 그래디언트 유사도 기반 파라미터 선택 네트워크". *정보 및 제어 학술대회, Oct. 2023*.

**2022**

- Dohyeong Kim and Songhwai Oh. "Efficient Off-Policy Safe Reinforcement Learning Using Trust Region Conditional Value at Risk". *IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 7644-7651, Jul. 2022*.
- JaeGoo Choy, Geonho Cha, and Songhwai Oh. "Unsupervised 3D Link Segmentation of Articulated Objects with a Mixture of Coherent Point Drift". *IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 7124-7131, Jul. 2022*.
- Chanho Ahn, Eunwoo Kim, and Songhwai Oh. "Incremental Learning with Adaptive Model Search and a Nominal Loss Model". *IEEE Access, vol. 10, pp. 16052-16062, 2022*.
- Mineui Hong, Kyungjae Lee, Minjae Kang, Wonsuhk Jung, and Songhwai Oh. "Dynamics-Aware Metric Embedding: Metric Learning in a Latent Space for Visual Planning". *IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 3388-3395, Apr. 2022*.
- Dohyeong Kim and Songhwai Oh. "TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning". *IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 2621-2628, Apr. 2022*.
- Minjae Kang and Songhwai Oh. "Deep Latent-Space Sequential Skill Chaining from Incomplete Demonstrations". *Intelligent Service Robotics, vol. 15, pp. 203–213, Apr. 2022*.
- Nuri Kim, Obin Kwon, Hwiyeon Yoo, Yunho Choi, Jeongho Park, and Songhwai Oh. "Topological Semantic Graph Memory for Image-Goal Navigation". *in Proc of the Conference on Robot Learning (CoRL), Dec. 2022*.
- Gunmin Lee, Wooseok Oh, Jeongwoo Oh, Seungyoun Shin, Dohyeong Kim, Jaeyeon Jeong, Sungjoon Choi, and Songhwai Oh. "Semi-Supervised Imitation Learning with Mixed Qualities of Demonstrations for Autonomous Driving". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Nov. 2022*.
- Howoong Jun, Sangil Lee, and Songhwai Oh. "EventPointNet: Robust Keypoint Detection with Neuromorphic Camera Data". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Nov. 2022*.
- Dohyeong Kim, Jaeseok Heo, and Songhwai Oh. "SafeTAC: Safe Tsallis Actor-Critic Reinforcement Learning for Safer Exploration". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022*.
- Jeongwoo Oh, Gunmin Lee, Jeongeun Park, Wooseok Oh, Jaeseok Heo, Hojun Chung, Do Hyung Kim, Byungkyu Park, Chang-Gun Lee, Sungjoon Choi, and Songhwai Oh. "Towards Defensive Autonomous Driving: Collecting and Probing Driving Demonstrations of Mixed Qualities". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022*.
- Dohyeong Kim, Yunho Kim, Kyungjae Lee, and Songhwai Oh. "Safety Guided Policy Optimization". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022*.
- Minjae Kang, Hogun Kee, Junseok Kim, and Songhwai Oh. "Grasp Planning for Occluded Objects in a Confined Space with Lateral View Using Monte Carlo Tree Search". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022*.
- Timothy Ha, Jeongwoo Oh, Hojun Chung, Gunmin Lee, and Songhwai Oh. "RIANet: Road Graph and Image Attention Network for Urban Autonomous Driving". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022*.
- Dohyeong Kim and Songhwai Oh. "Efficient Off-Policy Safe Reinforcement Learning Using Trust Region Conditional Value at Risk". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022. (RA-L option)*.
- JaeGoo Choy, Geonho Cha, and Songhwai Oh. "Unsupervised 3D Link Segmentation of Articulated Objects with a Mixture of Coherent Point Drift". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2022. (RA-L option)*.
- Hyemin Ahn, Obin Kwon, Kyungdo Kim, Jaeyeon Jeong, Howoong Jun, Hongjung Lee, Dongheui Lee, and Songhwai Oh. "Visually Grounding Language Instruction for History-Dependent Manipulation". *in Proc. of the IEEE International Conference on Robotics and Automation (ICRA), May 2022*.
- Mineui Hong, Kyungjae Lee, Minjae Kang, Wonsuhk Jung, and Songhwai Oh. "Dynamics-Aware Metric Embedding: Metric Learning in a Latent Space for Visual Planning". *IEEE International Conference on Robotics and Automation (ICRA), May 2022. (RA-L option)*.
- Dohyeong Kim and Songhwai Oh. "TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning". *IEEE International Conference on Robotics and Automation (ICRA), May 2022. (RA-L option)*.
- Seunggyu Chang, Jungchan Cho, and Songhwai Oh. "Texture Generation Using Dual-Domain Feature Flow with Multi-View Hallucinations". *in Proc. of the AAAI Conference on Artificial Intelligence (AAAI), Feb. 2022*.
- Mineui Hong, Kyungjae Lee, Minjae Kang, Wonsuhk Jung, and Songhwai Oh. "Supplementary Material for Dynamics-Aware Metric Embedding: Metric Learning in a Latent Space for Visual Planning". *ECE, Seoul National University, Technical Report, 2022*.
- 황민영, 오성회. "이미지 캡션 생성을 통한 시각-언어 기반 자율주행". *정보 및 제어 학술대회, Oct. 2022*.
- 기호건, 오성회. "Scene Segmentation Reasoning for Multi-object Manipulation". *인공지능 하계학술대회, Aug. 2022*.
- 최재구, 오성회. "Generation of a simple kinematic model of an articulated object by approximating a point set to a set of ellipsoids". *인공지능 하계학술대회, Aug. 2022*.
- 오우석, 오성회. "Does Vision-Language Transformers Learn Multimodal Representations for Object Detection?". *인공지능 하계학술대회, Aug. 2022*.

**2021**

- Yoonseon Oh, Kyunghoon Cho, Yunho Choi, and Songhwai Oh. "Chance-Constrained Multi-Layered Sampling-Based Path Planning for Temporal Logic-Based Missions". *IEEE Transactions on Automatic Control, vol. 66, no.12, pp. 5816-5829, Dec. 2021*.
- Eunwoo Kim, Chanho Ahn, and Songhwai Oh. "Auto-VirtualNet: Cost-Adaptive Dynamic Architecture Search for Multi-Task Learning". *Neurocomputing, vol. 442, pp. 116-124, Jun. 2021*.
- Geonho Cha, Minsik Lee, Jungchan Cho, and Songhwai Oh. "Reconstruct as Far as You Can: Consensus of Non-Rigid Reconstruction from Feasible Regions". *IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 43, no. 2, pp. 623-637, Feb. 2021*.
- Obin Kwon, Nuri Kim, Yunho Choi, Hwiyeon Yoo, Jeongho Park, and Songhwai Oh. "Visual Graph Memory with Unsupervised Representation for Visual Navigation". *in Proc. of the International Conference on Computer Vision (ICCV), Oct. 2021*.
- Hwiyeon Yoo, Jungho Yi, Jong Mo Seo, and Songhwai Oh. "Actualization of Deep Ego-motion Classification on Miniaturized Octagonal Compound Eye Camera". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021. (Best Poster Paper Award Winner)*.
- Wooseok Oh, Hwiyeon Yoo, Timothy Ha, and Songhwai Oh. "Vision-Based 3D Reconstruction Using a Compound Eye Camera". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Mineui Hong and Songhwai Oh. "Learning Latent Dynamics from Multi-View Observations for Image-Based Control". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Hogun Kee, Dohyeong Kim, and Songhwai Oh. "Decomposed Q-Learning for Non-Prehensile Rearrangement Problem". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Obin Kwon and Songhwai Oh. "Image-Goal Navigation Algorithm using Viewpoint Estimation". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Minyoung Hwang, Obin Kwon, and Songhwai Oh. "Geometric Understanding of Reward Function in Multi-Agent Visual Exploration". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Jae Seok Heo, Yunho Choi, and Songhwai Oh. "Image-Goal Navigation via MetricMapping and Keypoint based Reinforcement Learning". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Nuri Kim, Minjae Kang, and Songhwai Oh. "Semantic Descriptors into Representation for Robust Indoor Visual Place Recognition". *in Proc. of the International Conference on Control, Automation and Systems (ICCAS), Oct. 2021*.
- Timothy Ha, Gunmin Lee, Dohyeong Kim, and Songhwai Oh. "Road Graphical Neural Networks for Autonomous Roundabout Driving". *in Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Sep. 2021*.
- Minjae Kang and Songhwai Oh. "Deep Skill Chaining from Incomplete Demonstrations". *International Conference on Ubiquitous Robots, Jul. 2021. (Best Conference Paper Award Finalist)*.
- Yunho Choi and Songhwai Oh. "Image-Goal Navigation via Keypoint-Based Reinforcement Learning". *in Proc. of the International Conference on Ubiquitous Robots, Jul. 2021*.
- Hwiyeon Yoo and Songhwai Oh. "Localizability-based Topological Local Object Occupancy Map for Homing Navigation". *in Proc. of the International Conference on Ubiquitous Robots, Jul. 2021*.
- 이건민, 오성회. "q-Gaussian Mixture를 통한 자율주행 안정성 보장". *제 21회 정보 및 제어 학술대회, Oct. 2021*.
- 김도형, 오성회. "GPU 기반 비선형 계획법 솔버를 사용한 모델 기반 강화학습". *제 21회 정보 및 제어 학술대회, Oct. 2021*.
- 정재연, 오성회. "Agent의 효율적이고 안전한 Exploration을 위한 Tsallis Entropy의 분포 기반 강화학습에의 적용". *제 21회 정보 및 제어 학술대회, Oct. 2021*.
- 유휘연, 최윤호, 권오빈, 오성회. "모바일 로봇 네비게이션을 위한 실외환경 3차원 시뮬레이션 데이터셋". *제 21회 정보 및 제어 학술대회, Oct. 2021*.
- 전호웅, 오성회. "시각 정보 기반 네비게이션을 위한 국소 특징 추출법에 대한 고찰". *제 21회 정보 및 제어 학술대회, Oct. 2021*.
- 장승규, 오성회. "3차원 옵티컬 플로우 추정을 통한 비 강체 정합". *제33회 영상처리 및 이해에 관한 워크샵, Febuary, 2021*.

## 과제 참여

구성원 소개의 Research Experiences에 게시된 과제 3건이다. 기간은 해당 구성원이 게시한 참여 기간이며 과제 전체 사업 기간을 뜻하지 않는다.[^hongjung][^hojun]

- Development of Cloud Robot Intelligence Augmentation, Sharing, and Framework Technology to Integrate and Enhance the Intelligence of Multiple Robots (기간 Hongjung Lee 2021–2023; Hojun Chung 2022–2023 (구성원 참여 기간))
- Robot Learning: Efficient, Safe, and Socially-Acceptable Machine Learning (기간 Hongjung Lee 2022–2023 (구성원 참여 기간))
- General-Purpose Deep Reinforcement Learning Using Metaverse for Real World Applications (기간 Hojun Chung 2022–present (구성원 참여 기간))

## 수상

교수·구성원 개인 소개의 2022–2023년 수상 5건이다. 연도만 있는 항목은 누리집의 연도 표기이며 별도의 수상 날짜가 적혀 있지 않다. 구성원 개인 수상을 함께 담았다.[^prof][^jaewon][^hyeokjin]

- 2023 · 오성회: 한국로봇학회 오준호 학술상(Oh Jun-Ho Academic Award).
- 2023-09 · Jaewon Lee: Kakao Mobility Corp. NEMOTHON 1위.
- 2022-08 · Jaewon Lee: 대한조선학회 자율운항보트 경진대회 원격조종(Teleoperation) 부문 1위.
- 2022 · Hyeokjin Kwon: 서울대학교 공과대학 창의설계축전 3rd Prize(3등상).
- 2022 · Hyeokjin Kwon: Outstanding BS Thesis Presentation Award(학사학위 논문 발표 우수상).

## 소식

2021년 12월 2일–2026년 10월 14일의 논문 채택·게재 승인 소식 33건이다. 날짜는 각 소식 상세 본문 첫머리에 표시된 게시 날짜다.[^news]

- 2026-10-14 · 시각 정보 기반 3차원 공간 점유 예측 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n708]
- 2026-09-26 · 거의 확실한 안전성을 다루는 강화학습 논문이 NeurIPS 2026에 채택되었다.[^n70]
- 2026-08-12 · 여러 로봇 팔을 위한 다중 에이전트 학습 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n71]
- 2026-06-17 · 연구실 논문 2편이 IROS 2026에 채택되었다.[^n72]
- 2026-05-02 · 연구실 논문 2편이 ICML 2026에 채택되었다.[^n73]
- 2026-02-02 · 안전 제약을 둔 모방학습 논문이 Robotics and Autonomous Systems 게재 승인을 받았다.[^n74]
- 2026-02-01 · 연구실 논문 3편이 ICRA 2026에 채택되었다.[^n75]
- 2025-10-20 · 시각 기반 로봇을 위한 메모리 효율적인 3차원 공간 표현 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n76]
- 2025-07-23 · 장기 로봇 과제를 위한 행동 기술 발견 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n77]
- 2025-07-21 · 시각 기반 탁상 물체 재배치 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n78]
- 2025-06-16 · 연구실 논문 3편이 IROS 2025에 채택되었다.[^n79]
- 2025-01-30 · 곡예 동작 로봇을 위한 강화학습 논문이 ICRA 2025에 채택되었다.[^n80]
- 2025-01-23 · 제약이 있는 다목적 강화학습 논문이 ICLR 2025에 채택되었다.[^n81]
- 2024-09-25 · 연구실 논문 2편이 NeurIPS 2024에 채택되었다.[^n774]
- 2024-08-29 · 목표 물체를 찾아가는 시각 항법 논문이 Knowledge-Based Systems 게재 승인을 받았다.[^n754]
- 2024-07-18 · 목표 물체를 찾아가는 시각 항법 논문이 ICRA@40에 채택되었다.[^n728]
- 2024-07-01 · 연구실 논문 5편이 IROS 2024에 채택되었다.[^n712]
- 2024-03-08 · 목표 물체를 찾아가는 시각 항법 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n743]
- 2024-01-30 · 연구실 논문 2편이 ICRA 2024에 채택되었다.[^n772]
- 2023-09-22 · 연구실 논문 3편이 NeurIPS 2023에 채택되었다.[^n769]
- 2023-09-18 · 도로가 바뀐 상황의 도시 자율주행 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n761]
- 2023-06-22 · 연구실 논문 2편이 IROS 2023에 채택되었다.[^n773]
- 2023-02-28 · 연구실 논문 2편이 CVPR 2023에 채택되었다.[^n770]
- 2023-01-17 · 연구실 논문 2편이 ICRA 2023에 채택되었다.[^n771]
- 2022-09-11 · 목표 이미지에 해당하는 장소를 찾는 로봇 항법 논문이 CoRL 2022에 구두 발표로 채택되었다.[^n759]
- 2022-07-01 · 연구실 논문 7편이 IROS 2022에 채택되었다.[^n766]
- 2022-06-01 · 안전 강화학습 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n736]
- 2022-05-17 · 관절로 연결된 물체의 부분을 구분하는 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n760]
- 2022-02-01 · 연구실 논문 3편이 ICRA 2022에 채택되었다.[^n768]
- 2022-01-29 · 자료를 추가해 가며 배우는 학습 방법 논문이 IEEE Access 게재 승인을 받았다.[^n738]
- 2022-01-08 · 시각 정보를 이용한 계획 수립 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n735]
- 2021-12-21 · 안전 강화학습 논문이 IEEE Robotics and Automation Letters 게재 승인을 받았다.[^n753]
- 2021-12-02 · 물체 표면의 무늬를 생성하는 논문이 AAAI 2022에 채택되었다.[^n757]

## 연락과 위치

- 연구실 전화: +82-2-880-1512[^home]
- 연구실 A: 서울특별시 관악구 관악로 1 서울대학교 133동 610호, 우편번호 08826[^home]
- 연구실 B: 서울특별시 관악구 관악로 1 서울대학교 301동 751-4호, 우편번호 08826[^home]
- 교수 연구실: 301동 702호, 전화 +82-2-880-1511[^prof]
- 교수 이메일: songhwai@snu.ac.kr[^prof]

## 각주
[^p1]: H. Chung, J. Lee, S. Oh, Proceedings of the 43rd International Conference on Machine Learning 306 (2026). <https://rllab.snu.ac.kr/publications/papers/2026_icml_uhm.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2026_icml_uhm.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p2]: J. Kim, D. Kim, M. Hong, S. Oh, Proceedings of the 43rd International Conference on Machine Learning 306 (2026). <https://rllab.snu.ac.kr/publications/papers/2026_icml_cta.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2026_icml_cta.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p3]: D. Kim, M. Hong, J. Park, S. Oh, International Conference on Learning Representations (2025). <https://rllab.snu.ac.kr/publications/papers/2025_iclr_comoga.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2025_iclr_comoga.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p4]: W. Oh, H. Kee, S. Oh. <https://rllab.snu.ac.kr/publications/papers/2025_iros_llmrearrange.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2025_iros_llmrearrange.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p5]: H. Kee 외, S. Oh. <https://rllab.snu.ac.kr/publications/papers/2026_iros_rise.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2026_iros_rise.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p6]: J. Lee 외, S. Oh. <https://rllab.snu.ac.kr/publications/papers/2026_iros_rvnbench.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2026_iros_rvnbench.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p7]: M. Hwang 외, S. Oh. <https://rllab.snu.ac.kr/publications/papers/2023_cvpr_metaexplore.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2023_cvpr_metaexplore.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^p8]: T. Ha 외, S. Oh. <https://rllab.snu.ac.kr/publications/papers/2022_iros_rianet.pdf/@@display-file/file> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://rllab.snu.ac.kr/publications/papers/2022_iros_rianet.pdf/@@display-file/file> 연구실이 게시한 논문 PDF 첫 쪽의 초록.
[^home]: 연구실 첫 화면, 2026-10-28 열람. <https://rllab.snu.ac.kr/> 연락과 위치.
[^deptlab]: 전기·정보공학부 로봇학습 연구실 소개, 2026-10-28 열람. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=66&md=view> 연구실 이름, 지도교수, 로봇학습의 설명.
[^deptprof]: 전기·정보공학부 오성회 교수 소개, 2026-10-28 열람. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p070> 직위, 학력과 이전 경력.
[^prof]: 연구실 Songhwai Oh 소개, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/songhwai-oh> 현재 소속·직위, 학력·경력·관심 분야·학술 활동·수상, 기관 전화와 이메일.
[^research]: 연구실 Research, 2026-10-28 열람. <https://rllab.snu.ac.kr/research> SW Star Lab의 효율·안전·사회적 수용성, 언어 모델 기반 로봇 계획, 메타로보틱스, 자율 배송, 휴머노이드, 3차원 복원 연구.
[^people]: 연구실 People, 2026-10-28 열람. <https://rllab.snu.ac.kr/people> Graduate Students 17명과 Research Area.
[^alumni]: 연구실 Alumni, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/alumni> 박사·석사·이전 학부생 명단과 학위·연도·진로·학위논문.
[^pubs]: 연구실 Publications, 2026-10-28 열람. <https://rllab.snu.ac.kr/publications> 국제 학술지·학회·기술보고 목록과 대표 논문의 학회·연도.
[^domestic]: 연구실 Domestic Publications, 2026-10-28 열람. <https://rllab.snu.ac.kr/publications/domestic-publications> 국내 학술지·학회 목록.
[^news]: 연구실 News, 2026-10-28 열람. <https://rllab.snu.ac.kr/news> 첫 목록의 논문 채택 및 게재 승인 제목 대조.
[^hongjung]: Hongjung Lee 개인 소개, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/hongjung-lee> 박사과정, 과제 참여 기간.
[^hojun]: Hojun Chung 개인 소개, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/hojun-chung> 박사과정, 과제 참여 기간.
[^jaewon]: Jaewon Lee 개인 소개, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/jaewon-lee> Ph.D. candidate, 개인 수상.
[^hyeokjin]: Hyeokjin Kwon 개인 소개, 2026-10-28 열람. <https://rllab.snu.ac.kr/people/hyeokjin-kwon> 박사과정, 개인 수상.
[^memberdetail]: 박사과정 표기는 다음 개인 소개의 Ph.D. Student 또는 Ph.D. Candidate를 따른다. 2026-10-28 열람. <https://rllab.snu.ac.kr/people/hongjung-lee> <https://rllab.snu.ac.kr/people/hojun-chung> <https://rllab.snu.ac.kr/people/junseo-lee> <https://rllab.snu.ac.kr/people/junseok-kim> <https://rllab.snu.ac.kr/people/jaewon-lee> <https://rllab.snu.ac.kr/people/hyeokjin-kwon> <https://rllab.snu.ac.kr/people/geunje-cheon> <https://rllab.snu.ac.kr/people/jooyoungkim>
[^n708]: 연구실 소식 「Our paper on vision-based 3D occupancy prediction is accepted to IEEE RA-L」, 본문 게시 날짜 2026-10-14, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-vision-based-3d-occupancy-prediction-is-accepted-to-ieee-ra-l>
[^n70]: 연구실 소식 「Our paper on almost-sure safe reinforcement learning is accepted to NeurIPS 2026」, 본문 게시 날짜 2026-09-26, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-safe-reinforcement-learning-with-the-optimality-guarantee-is-accepted-to-neurips-2026>
[^n71]: 연구실 소식 「Our paper on multi-agent learning for multi-arm manipulation is accepted to IEEE RA-L」, 본문 게시 날짜 2026-08-12, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-multi-agent-learning-for-multi-arm-manipulation-is-accepted-to-ieee-ra-l>
[^n72]: 연구실 소식 「Two papers from RLLAB are accepted to IROS 2026」, 본문 게시 날짜 2026-06-17, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-iros-2026>
[^n73]: 연구실 소식 「Two papers from RLLAB are accepted to ICML 2026」, 본문 게시 날짜 2026-05-02, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-icml-2026>
[^n74]: 연구실 소식 「Our paper on safe imitation learning is accepted to Robotics and Autonomous Systems」, 본문 게시 날짜 2026-02-02, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-safe-imitation-learning-is-accepted-to-robotics-and-autonomous-systems>
[^n75]: 연구실 소식 「Three papers from RLLAB are accepted to ICRA 2026」, 본문 게시 날짜 2026-02-01, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/three-papers-from-rllab-are-accepted-to-icra-2026>
[^n76]: 연구실 소식 「Our paper on voxelized renderable neural 3D spatial representation is accepted to IEEE RA-L」, 본문 게시 날짜 2025-10-20, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-voxelized-renderable-neural-3d-spatial-representation-is-accepted-to-ieee-ra-l>
[^n77]: 연구실 소식 「Our paper on skill discovery for long-horizon robotic tasks is accepted to IEEE RA-L」, 본문 게시 날짜 2025-07-23, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-skill-discovery-for-long-horizon-robotic-tasks-is-accepted-to-ieee-ra-l>
[^n78]: 연구실 소식 「Our paper on visual tabletop rearrangement is accepted to IEEE RA-L」, 본문 게시 날짜 2025-07-21, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-visual-tabletop-rearrangement-is-accepted-to-ieee-ra-l>
[^n79]: 연구실 소식 「Three papers from RLLAB are accepted to IROS 2025」, 본문 게시 날짜 2025-06-16, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/three-papers-from-rllab-are-accepted-to-iros-2025>
[^n80]: 연구실 소식 「Our paper on reinforcement learning for acrobatic robots is accepted to ICRA 2025」, 본문 게시 날짜 2025-01-30, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-reinforcement-learning-for-acrobatic-robots-is-accepted-to-icra-2025>
[^n81]: 연구실 소식 「Our paper on constrained multi-objective reinforcement learning is accepted to ICLR 2025」, 본문 게시 날짜 2025-01-23, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-common-sense-object-goal-visual-navigation-is-accepted-to-iclr-2025>
[^n774]: 연구실 소식 「Two papers from RLLAB are accepted to NeurIPS 2024」, 본문 게시 날짜 2024-09-25, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-neurips-2024>
[^n754]: 연구실 소식 「Our paper on semantic atlas for visual navigation is accepted to Knowledge-Based Systems」, 본문 게시 날짜 2024-08-29, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-semantic-atlas-for-visual-navigation-is-accepted-to-knowledge-based-systems>
[^n728]: 연구실 소식 「Our paper on common-sense object-goal visual navigation is accepted to ICRA@40」, 본문 게시 날짜 2024-07-18, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-common-sense-object-goal-visual-navigation-is-accepted-to-icra-40>
[^n712]: 연구실 소식 「Five papers from RLLAB are accepted to IROS 2024」, 본문 게시 날짜 2024-07-01, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/five-papers-from-rllab-are-accepted-to-iros-2024>
[^n743]: 연구실 소식 「Our paper on object-goal visual navigation is accepted to IEEE RA-L」, 본문 게시 날짜 2024-03-08, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-object-goal-visual-navigation-is-accepted-to-ieee-ra-l>
[^n772]: 연구실 소식 「Two papers from RLLAB are accepted to ICRA 2024」, 본문 게시 날짜 2024-01-30, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-icra-2024>
[^n769]: 연구실 소식 「Three papers from RLLAB are accepted to NeurIPS 2023」, 본문 게시 날짜 2023-09-22, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/three-papers-from-rllab-are-accepted-to-neurips-2023>
[^n761]: 연구실 소식 「Our paper on urban autonomous driving is accepted to IEEE RA-L」, 본문 게시 날짜 2023-09-18, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-urban-autonomous-driving-is-accepted-to-ieee-ra-l>
[^n773]: 연구실 소식 「Two papers from RLLAB are accepted to IROS 2023」, 본문 게시 날짜 2023-06-22, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-iros-2023>
[^n770]: 연구실 소식 「Two papers from RLLAB are accepted to CVPR 2023」, 본문 게시 날짜 2023-02-28, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-cvpr-2023>
[^n771]: 연구실 소식 「Two papers from RLLAB are accepted to ICRA 2023」, 본문 게시 날짜 2023-01-17, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/two-papers-from-rllab-are-accepted-to-icra-2023>
[^n759]: 연구실 소식 「Our paper on topological semantic graph memory for visual navigation is accepted to CoRL 2022 as oral presentation」, 본문 게시 날짜 2022-09-11, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-topological-semantic-graph-memory-for-visual-navigation-is-accepted-to-corl-2022-as-oral-presentation>
[^n766]: 연구실 소식 「Seven papers from RLLAB are accepted to IROS 2022」, 본문 게시 날짜 2022-07-01, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/seven-papers-from-rllab-are-accepted-to-iros-2022>
[^n736]: 연구실 소식 「Our paper on efficient off-policy safe reinforcement learning is accepted to IEEE RA-L」, 본문 게시 날짜 2022-06-01, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-efficient-off-policy-safe-reinforcement-learning-is-accepted-to-ieee-ra-l>
[^n760]: 연구실 소식 「Our paper on unsupervised 3D segmentation of articulated objects is accepted to IEEE RA-L」, 본문 게시 날짜 2022-05-17, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-unsupervised-3d-segmentation-of-articulated-objects-is-accepted-to-ieee-ra-l>
[^n768]: 연구실 소식 「Three papers from RLLAB are accepted to ICRA 2022」, 본문 게시 날짜 2022-02-01, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/three-papers-from-rllab-are-accepted-to-icra-2022>
[^n738]: 연구실 소식 「Our paper on incremental learning with adaptive model search is accepted to IEEE Access」, 본문 게시 날짜 2022-01-29, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-incremental-learning-with-adaptive-model-search-is-accepted-to-ieee-access>
[^n735]: 연구실 소식 「Our paper on dynamic-aware metric learning is accepted to IEEE RA-L」, 본문 게시 날짜 2022-01-08, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-dynamic-aware-metric-learning-is-accepted-to-ieee-ra-l>
[^n753]: 연구실 소식 「Our paper on safe reinforcement learning is accepted to IEEE RA-L」, 본문 게시 날짜 2021-12-21, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-safe-reinforcement-learning-is-accepted-to-ieee-ra-l>
[^n757]: 연구실 소식 「Our paper on texture generation using dual-domain feature flow with multi-view hallucination is accepted to AAAI 2022」, 본문 게시 날짜 2021-12-02, 2026-10-28 열람. <https://rllab.snu.ac.kr/news/our-paper-on-texture-generation-using-dual-domain-flow-with-multi-view-hallucination-is-accepted-to-aaai-2022>

# 필드 인공지능 및 로보틱스 연구실 (Field AI and Robotics Laboratory, FAIR)

**KAIST 기계공학과 · 오현동 교수**

- 분야: 무인 이동체의 자율 판단, 라이다·영상·관성 센서 기반 인지와 SLAM, 비전 기반 드론 항법과 착륙, 정보 이론 기반 능동 탐색, 다중 무인기 군집·임무 할당·통신 중계, 완전 구동 드론
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 로봇 항법·SLAM[^slam][^path][^p1], 다중 로봇 협업·물류 자동화[^mac][^task][^p2], 강화학습[^mac][^p1], 제어 이론·제어 공학[^mac][^p3], 컴퓨터 비전[^slam], 3차원 복원·인식[^ap][^fad]
- 홈페이지: <https://fair.kaist.ac.kr/>
- 근거와 출처: [필드 인공지능 및 로보틱스 연구실 근거 페이지](fair-sources.md)

> 드론과 지상 로봇 같은 무인 이동체가 사람 없이 주변을 알아보고, 갈 길을 정하고, 여러 대가 함께 임무를 나눠 하도록 만드는 연구실이다. 센서 자료를 합쳐 위치를 추정하고 지도를 만드는 기술, 정보 이론으로 어디를 볼지 정하는 능동 인지, 학습 기반 인지·계획·제어를 함께 다룬다.[^prof][^research]

## 무엇을 연구하나

교수 소개는 연구 관심사를 무인 이동체의 자율성과 의사결정, 정보 이론 기반 능동 인지, 학습 기반 인지·계획·제어, 추정과 센서·정보 융합(여러 센서의 측정을 합쳐 더 정확한 추정을 얻는 일)으로 적는다.[^prof] 기계공학과 교수진 목록은 연구분야를 Unmanned Vehicles, Perception and Planning, Multi-Agent Systems로 적는다.[^melist] 기계공학과 연구분야 안내의 「ME + AX」 항목은 연구주제를 Mission planning and task assignment, Information-theoretic active perception, Learning-based perception, planning and control, Swarm and flocking control of multiple unmanned vehicles로, 주요 응용 산업을 모빌리티, 로보틱스, 국방무기체계로 적는다.[^meres]

연구 페이지는 연구를 여섯 갈래로 나눈다. 로봇이 주변을 알아보고 자기 위치와 지도를 함께 구하는 인지와 SLAM, 드론이 장애물을 피해 빠르게 날거나 움직이는 차량 위에 내려앉는 경로·궤적 계획, 센서를 어디로 옮겨야 가장 많은 정보를 얻을지 정하는 능동 인지, 여러 무인기가 무리를 지어 함께 움직이는 다중 에이전트 제어, 여러 로봇에게 일을 나눠 주는 임무 할당, 그리고 위치와 자세를 따로 제어할 수 있는 완전 구동 드론이다.[^research]

연구실이 다루는 무인 이동체는 주로 드론이다. 연구 페이지의 사례에는 드론 편대로 숲과 산에서 사람을 찾는 수색 구조, 실내 농장에서 작물을 세는 로봇 인지, 난류 속에서 보이지 않는 유해 가스의 누출원을 찾는 이동 센서, 통신이 닿지 않는 곳까지 연결을 넓히는 중계 무인기가 있다.[^slam][^ap][^mac]

## 주요 연구 주제

### 1. 인지와 SLAM

SLAM(Simultaneous Localization and Mapping, 위치 추정과 지도 작성을 동시에 하는 기술)은 위성 항법 신호를 쓸 수 없는 곳에서도 로봇이 자기 자세를 추적하면서 처음 보는 환경의 지도를 만드는 기술이다. 연구실은 카메라, 라이다(레이저를 쏘아 주변까지의 거리를 재는 센서), 레이더, IMU(Inertial Measurement Unit, 가속도와 회전 속도를 재는 관성 측정 장치)의 측정을 합쳐 이 문제를 푼다.[^slam]

- 영상–관성 주행 거리계(VIO, Visual-Inertial Odometry, 카메라 영상과 관성 측정을 합쳐 움직임을 추정하는 방법): 카메라는 가볍고 작으면서 풍부한 시각 정보를 주고, 관성 자료가 빠른 움직임에서 생기는 영상 흐림을 보완해 실내나 도심 협곡처럼 위성 항법이 안 되는 곳에서도 정밀하게 항법한다.[^slam]
- 라이다–관성 주행 거리계(LIO)와 레이더–관성 주행 거리계(RIO): 라이다는 조명과 관계없이 정밀한 3차원 점 구름을 주고, 레이더는 연기나 안개 속에서도 거리와 시선 방향 속도를 잰다. 각각을 관성 자료와 결합해 위치와 자세를 추정한다.[^slam]
- 다리 로봇의 운동학–관성 주행 거리계: 관절 인코더와 접촉 센서로 다리 로봇이 땅과 맞닿는 상태를 재고 관성 자료와 합쳐, 바깥 센서가 가려지거나 특징이 없는 환경에서도 움직임을 추정한다.[^slam]
- 가우시안 과정(Gaussian Process, 측정한 지점 사이의 값을 확률 분포로 예측하는 통계 모델) 기반 공간 모델링: 드문드문하고 잡음 섞인 측정에서 높이 지도나 가스 농도 분포 같은 연속된 면을 매끄럽게 복원하고, 예측의 불확실성도 함께 구한다.[^slam]
- 정밀 농업용 로봇 인지: 고해상도 카메라와 라이다를 결합해 실내 농장의 작물을 센티미터 이하 정밀도로 관찰하고, 열매 세기, 수확량 추정, 생육 분석을 자동화한다.[^slam]
- 신경망 압축: 가지치기, 양자화, 지식 증류로 신경망을 작게 만들어 계산 자원과 전력이 제한된 이동 로봇에서도 딥러닝 모델을 실시간으로 쓰게 한다.[^slam]
- 드론 편대 기반 사람 탐지: 가시광 카메라와 열화상 센서를 함께 써서 시야가 나쁘거나 수풀이 우거진 곳에서도 사람을 찾고, 장애물 회피와 편대 간 통신을 결합해 숲과 산에서 수색 구조 임무를 한다.[^slam]

최근 논문 목록에는 레이더–관성 주행 거리계, 도플러 속도로 점 구름을 맞추는 스캔 정합, 점 구름의 기하 구조를 학습하는 연구가 있다.[^pubs]

### 2. 경로·궤적 계획

드론이 카메라 영상으로 경로 위의 장애물을 실시간으로 찾아 피하며 빠르고 민첩하게 나는 비전 기반 항법과, 자동차나 배처럼 움직이는 차량 위에 사람의 개입 없이 내려앉는 자율 착륙을 연구한다.[^path] 대표 논문 1은 착륙장을 시야에 계속 두면서 움직이는 착륙장에 내려앉는 방법을 학습으로 다룬다.[^p1] 연구 페이지는 허가받지 않았거나 적대적인 드론에 요격 드론이 직접 접근해 공중에서 멈추게 하는 드론 요격, 시계 밖 공중전(BVR, Beyond-Visual-Range, 눈으로 보이지 않는 거리에서 벌어지는 공중 교전)도 이 갈래에 둔다.[^path] 무너진 건물, 터널, 산업 시설처럼 좁고 위험한 곳에서 로봇이 충돌 없이 길을 찾도록 하는 제어와 경로 계획도 연구한다.[^path]

### 3. 능동 인지와 정보 이론 기반 탐색

능동 인지(로봇이 얻을 정보를 따져 센서를 어디로 옮길지 스스로 정하는 일)의 대표 주제는 이동 센서로 보이지 않는 유해 가스의 누출원을 찾는 일이다. 베이즈 틀(새 측정이 들어올 때마다 확률 분포를 갱신하는 추론 방식)에서 누출원의 위치와 방출 세기 같은 소스 항(source term)을 추정하고, 그 추정의 불확실성을 최소화하도록 센서를 움직이는 정보 기반 탐색 전략을 만든다. 실외와 실내, 여러 에이전트와 여러 누출원에 대한 전략을 개발해 실제 실험으로 검증했다.[^ap] 최근 논문 목록에는 심층 강화학습(시행착오로 보상을 키우는 행동을 신경망으로 배우는 기계학습 방법)과 비전–언어 모델(영상과 글을 함께 다루는 인공지능 모델)을 쓴 가스 누출원 위치 추정 연구가 있다.[^pubs]

가우시안 과정으로 공간과 시간에 따라 바뀌는 현상을 모델링해 이동 센서망이 좋은 자료를 효율적으로 모으게 하는 능동·적응 표본 추출, 정보 이득과 최적화로 드론의 비행 경로를 정해 구조물을 적은 시간과 비용으로 정확하게 3차원 복원하는 전략도 이 갈래의 연구다.[^ap]

### 4. 다중 에이전트 제어와 임무 할당

여러 무인기가 무리를 지어 함께 움직이게 하는 군집 비행(flocking)과 편대 제어로 넓은 지역을 효과적으로 덮고 정보를 실시간으로 나누게 하며, 강화학습과 신경망으로 무인기들이 환경과 서로에게서 배우며 군집 비행 성능을 높이는 학습 기반 군집 비행을 연구한다.[^mac] 무인기나 무인 지상 차량을 중계기로 보내 장애물과 간섭이 바뀌는 환경에서도 통신을 이어 주는 자율 통신 중계도 이 갈래에 있다.[^mac] 대표 논문 2는 실내 임무에서 중계 로봇의 경로를 실시간으로 계획한다.[^p2]

임무 할당은 드론, 로봇, 자율주행차가 사람의 개입 없이 안전하게 임무를 마치도록 경로, 행동 일정, 환경과의 상호작용을 설계하는 일이다. 연구실은 여러 로봇이 여러 임무를 나눠 맡는 다중 로봇 다중 임무 계획을 연구한다.[^task]

무인기 제어 쪽에서는 외란이 있는 시스템을 다루는 슬라이딩 모드 제어(시스템 상태를 미리 정한 면으로 끌어와 그 면을 따라 움직이게 하는 강인 제어 방법) 연구도 이어 간다. 대표 논문 3은 측정되지 않는 상태와 외란이 있는 시스템의 출력을 유한 시간 안에 원하는 값으로 이끄는 제어기 설계를 다룬다.[^p3]

### 5. 완전 구동 드론

완전 구동 드론(위치와 자세를 서로 따로 제어할 수 있는 비행체)은 여러 방향으로 힘과 모멘트를 낼 수 있어, 원하는 방향을 바라본 채로 움직일 수 있다. 연구실은 여섯 로터를 고정된 각도로 기울여 단 기울어진 헥사로터, 로터 기울기를 한 방향으로 능동 조절하는 H자형 쿼드 틸트로터, 여섯 로터의 기울기를 모두 능동 조절하는 헥사로터를 만든다. 이런 비행체는 3차원 복원, 모든 방향에서의 물체 관찰, 좁은 통로 통과 같은 임무에 쓰인다.[^fad]

## 대표 논문

오현동 교수가 저자인 2021–2026년 논문 가운데, 교수가 KAIST 소속으로 적히고 교신저자(*)인 논문으로서 초록을 확인할 수 있는 세 편을 골랐다. 교수는 2025년 8월 KAIST에 부임했다. 표는 세 편뿐이며 인지·SLAM 갈래와 능동 탐색 갈래의 논문을 담지 않는다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Vision-Based Autonomous Drone Landing on Moving Platforms With Uncertain Motion via Deep Reinforcement Learning](https://doi.org/10.1109/lra.2026.3674011) · IEEE Robotics and Automation Letters | 쿼드로터 드론이 움직임을 미리 알 수 없는 이동 착륙장에 카메라로 내려앉는 문제를 다룬다. 카메라는 가볍고 싸며 전역 기준 좌표 없이 착륙장과의 상대 관측을 주지만, 기존 시각 착륙은 정확한 추정과 조정에 의존해 견고성이 떨어지고, 심층 강화학습은 움직임이 불확실하거나 좁은 시야 때문에 착륙장을 놓치면 성능이 떨어진다. 핵심 과제는 격한 기동 중에도 착륙장을 시야에 두는 능동 인지다. 저자들은 인지·추정·제어를 함께 배우는 비전 기반 심층 강화학습 틀을 만들고, 시야 유지와 제어 성능을 함께 따지는 보상으로 안정된 착지를 이끌었다. 시뮬레이션에서 시각 서보잉(카메라 영상의 특징을 직접 되먹임해 움직임을 제어하는 방법)과 기존 강화학습 기준 방법보다 견고했고, 시야가 제한된 상태에서 최대 8 m/s로 움직이는 착륙장에도 내려앉았으며, 실제 실험으로 실현 가능성과 안정성을 확인했다.[^p1] | 1저자 W. Shin, 마지막 저자 H. Oh* (6명) |
| 2 | 2026 | [Real-Time Communication Relay Planning With a Low-Complexity Network Quality Prediction Model in Dynamic Indoor Missions](https://doi.org/10.1109/lra.2025.3632056) · IEEE Robotics and Automation Letters | 중계 로봇은 다른 로봇이 먼 곳까지 임무를 나갈 때 통신이 끊기지 않게 이어 준다. 기존 망 품질 예측 모델과 중계 계획은 계산 비용이 크고 자주 바뀌는 임무에 맞추기 어려워 실시간으로 돌리기 힘들었다. 이 연구는 칼만 필터(측정이 들어올 때마다 상태 추정을 갱신하는 알고리즘) 기반 가우시안 과정 회귀로 갱신 시간이 일정한(약 0.02초) 망 품질 예측 모델을 만들고, 몬테카를로 트리 탐색(여러 행동 순서를 표본으로 시험해 유망한 쪽을 더 깊이 살피는 계획 방법)으로 정해진 단계마다 망 조건을 지키는 통신 인식 궤적을 만드는 계층적 중계 계획을 내놓았다. 실제 실험에서 채널 신뢰도 99.1%로 거의 끊김 없는 연결을 보였고, 패킷 전달률을 기준 방법의 44.7%에서 73.7%로 높였다.[^p2] | 1저자 J. Seo, 마지막 저자 H. Oh* (6명) |
| 3 | 2026 | [Observer-based output feedback nonsingular terminal sliding mode control for systems with mismatched disturbances: Theory and applications](https://doi.org/10.1109/access.2026.3679398) · IEEE Access | 제어 입력이 직접 상쇄할 수 없는 경로로 들어오는 외란(mismatched disturbance)이 있는 시스템을 위해, 관측기(측정값으로 측정되지 않는 상태를 추정하는 장치) 기반 출력 되먹임(측정한 출력만으로 제어 입력을 정하는 방식) 비특이 종단 슬라이딩 모드 제어를 제안했다. 측정되지 않는 출력의 미분과 쌓인 외란을 가변 이득 유한 시간 슬라이딩 모드 관측기로 복원하고, 비특이 종단 슬라이딩 면으로 슬라이딩 단계에서 출력을 0으로 보내며, 수정 슈퍼 트위스팅 도달 법칙으로 도달 단계에서 슬라이딩 변수를 0으로 만든다. 저자들은 이 방법이 유한 시간 안에 빠르고 정확하게 추정하고, 관측기 설계의 상수 경계 가정을 완화하며, 시스템 차수와 관계없이 관측기 하나만 쓰고, 모든 상태를 잴 수 있다는 가정을 없앤다고 적는다. 출력이 유한 시간 안에 수렴함을 엄밀히 보이고 여러 응용 예로 성능을 보였다.[^p3] | 1저자 N. P. Nguyen, 교신저자 H. Oh*·J. Moon* (5명 중 2번째·3번째) |

## 교수와 전문 분야

오현동 교수는 KAIST 기계공학과 교수로, 연구실 교수 소개는 2025년 8월부터의 직위를 Associate Professor with Tenure(종신 부교수)로 적는다.[^prof][^meprof] 겸임은 KAIST AI대학 AX학과와 조천식모빌리티대학원(GCS Graduate School of Mobility, 2026년 4월부터), Robotics Program과 KI for Disruptive Robotics(2025년 8월부터)다.[^prof]

학력은 KAIST Mechanical and Aerospace Engineering 학사(2004)와 석사(2010), 영국 Cranfield University 무인 자율 시스템(Unmanned Autonomous Systems) 박사(2013)이며, Loughborough University에서 Postgraduate Certificate in Academic Practice(2016)를 받았다. Republic of Korea Air Force Quality Control Officer(2004–2007), KAIST 연구조교(2008–2010), Cranfield University 연구조교(2010–2013), University of Surrey 박사후연구원(2013–2014), Loughborough University 강사(Lecturer, 2014–2016)를 거쳐 UNIST 기계공학과 조교수(2016–2019)와 부교수(2019–2025.08)를 지냈다. UNIST 재직 중 Cranfield University 방문교수(2023.08–2024.08)를 지냈고, Loughborough University 방문 연구원(Visiting Research Fellow, 2016–2020)을 겸했다.[^prof] UNIST에서 교수가 이끈 연구실은 자율 시스템 연구실(Autonomous Systems Lab)이다.[^home]

교수 소개에 적힌 수상은 다음과 같다(이름은 교수 소개 표기 그대로).[^prof]

- IEEE Robotics and Automation Letters Distinguished Service Award (As an Outstanding Reviewer) (2026)
- Best Paper Award (Commendation from the National Fire Agency), Institute of Control, Robotics, and Systems (ICROS) (2026)
- Best Paper Award, The Korea Robotics Society (KROS) (2026, 2025)
- Best Student Paper Award Finalist, Robotics: Science and Systems (RSS 2025)
- Best Student Paper Award, International Symposium on Swarm Behavior and Bioinspired Robotics (SWARM 2024)
- UAV Competition Winner, International Conference on Unmanned Aircraft Systems (ICUAS 2024)
- Best Paper Award, Institute of Control, Robotics, and Systems (ICROS) (2024, 2023)
- IJASS the Most Cited Article Award (2023), IJASS the Most Downloaded Article Award (2022)
- Kwon Wook-Hyun Young Researcher Award, Institute of Control, Robotics, and Systems (ICROS) (2022)
- Deputy Prime Minister and Minister of Education Award, Top 50 outstanding academic and research performances from the 'Academic and Research Support Program' of the Ministry of Education (2021)
- Excellence Award (2nd place), Autonomous Drone Competition organized by DAPA and ADD (2021)
- Best Intelligence Paper Award, 9th International Conference on Robot Intelligence Technology and Applications (RiTA) (2021)
- Excellence Award, KAI Aerospace Paper Award (2021)
- Outstanding Paper Presentation Award, The Korean Society for Aeronautical & Space Sciences (2021, 2019)
- Grand Prize, the 2019 AI Competition for Space Weather Disaster Prediction, National Radio Research Agency (2019)
- Early Career Scientist and Engineer Award, The Korean Scientists and Engineers Association in the UK (2013)
- Minister of Trade, Industry and Energy Award (Top Prize), International UAV paper competition, Korea Aerospace Industries Association (2013)

2025년 8월 KAIST 부임 전의 수상은 UNIST 등 이전 소속 시기의 것이다.[^prof]

학계 활동으로는 IEEE Transactions on Aerospace and Electronic Systems Senior Editor(2026년 10월 임명 소식), International Journal of Aeronautical and Space Sciences 편집위원, IEEE Robotics and Automation Letters Associate Editor를 맡고 있고, ICCAS 2027 Program Chair, RSS 2026 Area Chair, IFAC World Congress(2026) Competition Chair, RiTA 2024 General Chair, RSS 2023 Workshop Chair, RiTA 2022 Program Chair를 맡았거나 맡고 있다. IEEE Senior Member이자 AIAA Member다.[^prof][^news]

논문으로 보면 교수의 전문 분야는 무인기의 자율 항법과 인지(비전 기반 착륙·항법, 라이다·레이더·관성 융합 주행 거리계), 정보 이론 기반 능동 탐색(가스 누출원 위치 추정), 다중 무인기의 군집 비행·임무 할당·통신 중계, 그리고 슬라이딩 모드 제어 같은 강인 제어 이론이다.[^pubs] KAIST 소속으로 나온 대표 논문은 비전 기반 착륙(대표 논문 1), 통신 중계 계획(대표 논문 2), 슬라이딩 모드 제어(대표 논문 3)다.[^p1][^p2][^p3]

## 응용 분야

연구 페이지는 연구의 쓰임으로 숲과 산의 수색 구조, 실내 스마트 농장의 작물 감시, 보이지 않는 유해 가스의 누출원 탐색, 무너진 건물·터널·산업 시설의 수색과 점검, 감시와 환경 감시, 보호 구역에 들어온 드론의 요격을 든다.[^slam][^path][^ap][^mac] 과제 표의 진행 중 과제에는 달 착륙선용 라이다 기반 장애물 탐지·회피·항법 알고리즘 연구(KARI/KASA), 선박 블록 안 이동 로봇의 경로 생성(HD KSOE), 학습 기반 드론 대응 제어(Nearthlab), 실내 농장 자료 처리 자동화(Metafarmers), 스마트 농업 디지털 트윈용 완전 구동 드론 플랫폼(KAIST Institute) 과제가 있다. 괄호 안은 누리집이 적은 기관 표기다.[^projects] 소식에는 2026년 8월 Anduril Industries가 연 자율 드론 경주 대회의 가상 예선 1위가 있다.[^home]

## 구성원

연구실 누리집 Members 페이지의 Postdoctoral Researchers 1명, Ph.D. Students 16명, M.S. Students 6명, Researchers 칸 4명(연구원 2명, 입학 예정 석사과정 2명), 모두 27명이다.[^members] 과정은 각 카드의 표기이고, 시작은 카드 학력 칸에서 "present"로 끝나는 대학원 과정 줄의 시작 연월과 그 학교다. 학력 칸에 따르면 구성원 가운데 여러 명이 UNIST에서 과정을 시작했다. 연구 주제는 카드 앞면의 Research interests 표기이고, 이메일은 카드에 적힌 학교 주소만 실었다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Yeongho Song | 박사후연구원 | 2025.09 (KAIST) | Safe control for multi-agent systems | yh.song@kaist.ac.kr |  |
| Minjae Jung | 박사과정 | 2025.09 (KAIST) | Swarm robotics, Multi robot task allocation | starshirts@kaist.ac.kr |  |
| Geunsik Bae | 박사과정 | 2026.03 (KAIST) | Path planning for MAV | baegs.uav@kaist.ac.kr | 1 |
| Jaemin Seo | 박사과정 |  | Probabilistic Environmental Representation for Practical Applications With Robotic System | jam.seo@kaist.ac.kr | 2 |
| Heejung Shin | 박사과정 | 2025.09 (KAIST) | Robot perception with deep Learning | godhj93@kaist.ac.kr |  |
| Myeonggeun Gu | 박사과정 | 2021.03 (UNIST) | Multi-agent decision making | cvaudrms@unist.ac.kr |  |
| Seunghwan Kim | 박사과정 | 2021.03 (UNIST) | Information-theoretic active sensing and autonomus exploration | kevin6960@unist.ac.kr | 1, 2 |
| Taewook Park | 박사과정 | 2021.03 (UNIST) | Machine learning for unmmaned vehicles | wook@unist.ac.kr | 1 |
| Hongro Jang | 박사과정 | 2026.03 (KAIST) | Information-theoretic active perception for multiple agents, Probabilistic inference | hlomk35@kaist.ac.kr |  |
| Changseung Kim | 박사과정 | 2021.03 (UNIST) | Collaborative visual SLAM, LiDAR-visual-inertial sensor fusion SLAM | pon02124@unist.ac.kr | 2 |
| Hyeongseop Kim | 박사과정 | 2022.03 (UNIST) | Distributed decision making | kimhs8090@unist.ac.kr |  |
| Myong-Yol Choi | 박사과정 | 2022.03 (UNIST) | Flocking/swarming using deep reinforcement learning | mychoi@unist.ac.kr |  |
| Junhee Lee | 박사과정 | 2025.08 (KAIST) | Information-theoretic active sensing, Learning-based perception and planning | ljh0124@kaist.ac.kr |  |
| Woojae Shin | 박사과정 | 2025.08 (KAIST) | Vision-based navigation using deep reinforcement learning | oj7987@kaist.ac.kr | 1, 2 |
| Jiwoo Kim | 박사과정 | 2026.02 (KAIST) | Simultaneous localization and mapping | tars0523@kaist.ac.kr |  |
| Jinwoo Lee | 박사과정 | 2026.02 (KAIST) | autonomous robotic navigation | jinwoolee@kaist.ac.kr |  |
| Seobeom Lee | 박사과정 |  | Fully-actuated drone, optimal control, robust control | seobeomlee@postech.ac.kr |  |
| Gaeun Yim | 석사과정 | 2023.09 (UNIST) | Exploration and 3D reconstruction | gaeungraceyim@unist.ac.kr |  |
| Hyungjin Kim | 석사과정 | 2025.09 (KAIST) | Information-theoretic active perception for multi-agent control | gudwls124z@kaist.ac.kr |  |
| Minsung Kim | 석사과정 | 2026.02 (KAIST) | Simultaneous localization and mapping | hj05vv@kaist.ac.kr |  |
| Seunghoon Lee | 석사과정 |  | Autonomous navigation, Locomotion control for quadruped robots | lsh356812@kaist.ac.kr |  |
| Hankyoul Ko | 석사과정 |  | Embedded system, indoor positioning, controller design | kyoul@unist.ac.kr |  |
| Hieu Do Quang | 석사과정 |  | Decentralized Cooperative Swarm Navigation | hieudo@kaist.ac.kr |  |
| Hanse Cho | 연구원 | 2024.09 (UNIST) | Flocking/swarming system control, safe reinforcement learning | joahdzl@unist.ac.kr |  |
| Han-ryung Shin | 연구원 |  | Novel robotic hardware, learning-enhanced model-based control |  |  |
| Lee Jeong Min | 입학 예정 석사과정 |  | Exploration and 3D reconstruction | jmlee0221@kaist.ac.kr |  |
| Soobeom Kwak | 입학 예정 석사과정 |  | Autonomous Driving, Perception & SLAM | sbkwak@kaist.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 22명이다. 학위·과정과 시기, 진로는 각 줄의 표기다. 학위 논문은 Thesis/Dissertations 페이지에서 이름이 같은 항목을 이었고, 이름 철자가 다르거나 논문 항목이 없는 행은 비워 두었다. 누리집은 학위를 받은 학교를 적지 않는다. 학위 시기가 2025년 8월 이전인 행은 교수가 KAIST에 부임하기 전 시기다.[^alumni][^theses]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seungin Park | Master degree (2026.08) | LG CNS |  |
| Hyoungho Park | Master degree (2026.02) | RLWRLD | Semantic-GSL: a semantic-aware vision-language model framework for gas source localization in unknown indoor environments (Master thesis, 2026.02) |
| Meraj Mammadov | Master degree (2025.08) | Örebro University | Learning end-to-end perception-aware policies for UAV collision avoidance in dynamic environments (Master thesis, 2025.08) |
| Minwoo Kim | PhD degree (2025.02) | Samsung Research | Learning-based visual navigation for drones: generalization, sample-efficiency and sim-to-real gap (PhD thesis, 2025.02) |
| Seonguk Bae | Master degree (2025.02) | Hanwha Ocean | Efficient Direct Voxel-Based Viewpoint Planning in 3D Reconstruction for UAVs (Master thesis, 2025.02) |
| Phong Nguyễn Ngô | PhD degree (2022.02) | Lecturer Vietnamese German University | Continuous Sliding Mode Control: Theoretical Frameworks and Applications to Mechanical Systems (PhD thesis, 2022.02) |
| Pawel Ladosz | PhD degree (2018.02) | Lecturer in University of Manchester |  |
| Youngho Song | PhD degree (2023.06) | InnoCORE Postdoc in KAIST |  |
| Gangik Cho | PhD degree (2023.06) | Airbility | Autonomous landing of a UAV on a moving platform using image based visual servoing (PhD thesis, 2023.08) |
| Minkyu Park | PhD degree (2023.02) | Assistant Professor in Changwon National University | Autonomous Hazardous Gas Source Search and Estimation Strategies of Mobile Sensors (PhD thesis, 2023.02) |
| Heejung Shin | Master degree (2023.02) | PhD in KAIST | Fast Monocular Depth Estimation with Neural Network Compression for Collision Avoidance (Master thesis, 2023.02) |
| Geunsoo Kim | Master degree (2022.02) |  | Multi-Agent Deep Reinforcement Learning for Multi-Regional Coverage Path Planning (Master thesis, 2022.02) |
| Minjae Jung | Master degree (2022.02) | PhD in KAIST | Heterogeneous Mission Planning of UAVs with Attention-Based Deep Reinforcement Learning (Master thesis, 2022.02) |
| Joonwon Choi | Master degree (2021.08) | PhD in Purdue University |  |
| Hyerin Jeong | Studied for one semester | Korea Aerospace Industries (KAI) |  |
| Seul-bi An | Master degree (2021.02) | Hyundai Robotics | Information-Based Path Planning for Source Term Estimation Using an Unmanned Aerial Vehicle: Algorithms and Experiments (Master thesis, 2021.02) |
| Jinwoo Oh | Master degree (2021.02) | CONTEC | Communication-Aware Multi-Target Tracking Guidance for Cooperative UAVs with Gimbaled Vision Sensors in Urban Environments (Master thesis, 2021.02) |
| Seungho Back | Master degree (2020.02) | HD Korea Shipbuilding & Offshore Engineering | Autonomous Navigation of the UAV on the Trail with Obstacles Avoidance Using Deep Neural Networks (Master thesis, 2020.02) |
| Jongyun Kim | Master degree (2020.02) | Postdoc in University of Manchester | Optimal Communication Relay Approach for Mobile Multi-Node Networks in Complex Environment (Master thesis, 2020.02) |
| Dongmin Shin | Master degree (2019.08) | Pablo Air, 한국자동차연구원 (KATECH) | Nonlinear Disturbance Observer Based Path Following for a Small Fixed-Wing UAV (Master thesis, 2019.08) |
| Bumsu Park | Master degree (2019.02) | Assistant Professor in SEOULTECH | Autonomous Navigation for Mobile Robots: Machine Learning-Based Techniques for Obstacle Avoidance (Master thesis, 2019.02) |
| Xuan Toa Tran | Research associate (2017.04 ~ 2020.03) | Research Fellow in Queens University Belfast, UK |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 2021–2026년 연도 구역 143편이다. International Journals [J44]–[J91] 48편, International Conferences [C46]–[C93] 48편, Domestic Journals [J5]–[J10] 6편, Domestic Conferences [C52]–[C91] 40편, Book Chapters [B5] 1편이고, 연도마다 이 순서로 적었다. 국내 목록의 번호는 국제 목록의 번호와 겹치므로 줄 끝에 「(국내 학술지)」·「(국내 학회)」를, 책 속 장에는 「(책 속 장)」을 붙였다. Domestic Journals와 Book Chapters는 연도 구역 없이 적혀 있어 줄 끝의 연도를 따랐다. 각 줄은 누리집 표기 그대로이고, 학술지 목록의 *는 누리집이 적은 교신저자 표시다. 2026년 구역의 「in press」 5편([J88]–[J91], 국내 [J10])은 게재가 정해졌으나 권·쪽이 나오기 전인 논문이다. 국제 학회 [C92]는 첫 화면이 2026년 4월에 RSS 2026 발표 채택을 알린 논문이라 「RSS 2026 발표 채택」으로 표시했다. 교수 개인의 논문 목록이라 2025년 8월 KAIST 부임 전 UNIST 시기의 논문이 섞여 있어, 모두 현재 KAIST 연구실의 성과로 묶지 않는다.[^pubs]

**2026**

- [J91] H. Park, H. Jang, S. Kim, J. Lee, J. Kim and \*H. Oh. Semantic-GSL: Integrating visual semantic context into information-theoretic search for gas source localization, IEEE Robotics and Automation Letters, in press.
- [J90] T. Park, S. Lee, J. Lee, J. Cho, J. Shim, W. Yun, K. Lee and \*H. Oh, Optimizing indoor farm monitoring: drone-based efficient data acquisition and 3D multi-view fusion for instance-level strawberry monitoring, IEEE Transactions on Field Robotics, in press.
- [J89] J. Kim, M. Jung, H. Oh, A. Tsourdos and \*H.S. Shin. Energy-efficient and scalable UAV flocking by learning lazy behaviors using reinforcement learning, Scientific Reports, in press.
- [J88] Z. Dai, T. Fan, M. Amani, J. Seo, K. M. B. Lee, H. Oh and \*N. Atanasov. Kernel-SDF: An open-source library for real-time signed distance function estimation using kernel regression, IEEE Robotics and Automation Letters, in press.
- [J87] W. Shin, M. Kim, T. Park, G. Bae, S. Kim and \*H. Oh, Vision-based autonomous drone landing on moving platforms with uncertain motion via deep reinforcement learning, IEEE Robotics and Automation Letters, Vol. 11, No. 5, pp. 5542-5549, 2026.
- [J86] N.P. Nguyen, \*H. Oh, \*J. Moon, Y. Kim and J. Yang. Observer-based output feedback nonsingular terminal sliding mode control for systems with mismatched disturbances: Theory and experiments, IEEE Access, Vol. 14, pp. 55564-55578, 2026.
- [J85] M. Gu, Y. Song, C. Ra, J. Suk and \*H. Oh. Iterative task decomposition and allocation for fixed-wing multi-UAV coverage path planning, International Journal of Aeronautical and Space Sciences, Vol. 27, pp. 774-790, 2026
- [J84] M. Jung, \*D. Lee, \*H. Oh, J.W. An, J.W. Woo and G.R. Nam. A hybrid deep reinforcement learning approach for target allocation and routing of multiple nonholonomic vehicles, Engineering Applications of Artificial Intelligence, Vol. 164, Part B, 113308, 2026.
- [J83] J. Seo, J. Kim, S. Kim, C. Kim, W. Shin and \*H. Oh. Real-time communication relay planning with a low-complexity network quality prediction model in dynamic indoor missions, IEEE Robotics and Automation Letters, Vol. 11, No. 1, pp. 322-329, 2026.
- [J82] T. Park, G. Bae, W. Shin, M. Meraj, J. Seo, H. Shin and \*H. Oh. PACMAN: rapid identification of keypoint-based fiducial marker in occluded environments, Image and Vision Computing, Vol. 165, 105821, 2026.
- [C93] J. Kim, J. Lee, W. Shin, G. Kim and H. Oh. Self-supervised geometry reasoning for LiDAR simultaneous localization and mapping, From Perception to Action Workhop in Robotics: Science and Systems (RSS), Sydney, Australia, 2026.
- [C92] J. Lee, J. Kim, W. Shin, G. Kim and H. Oh. Learning the underlying geometry of point clouds:theory and practice, Robotics: Science and Systems (RSS), Sydney, Australia, 2026. (RSS 2026 발표 채택)
- [J10] S. Lee, T. Park, C. Kim and H. Oh. HG-LLIO: Hierarchical ground-reaction-force-aided learning leg-inertial odometry. Journal of Institute of Control, Robotics and Systems, in press, 2026. (국내 학술지)
- [C91] S. Lee, T. Park and H. Oh. Dynamics-informed pose estimation for accuracy enhancement in quadruped robots. The 21th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2026. (국내 학회)
- [C90] T. Park, S. Lee, J. Shim, W. Yun and H. Oh. Design of an operator-assisted UAV system for yield estimation in confined indoor strawberry farms. The 21th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2026. (국내 학회)
- [C89] M. Gu and H. Oh. Communication-efficient multi-agent task allocation via preference-based grouping. The 21th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2026. (국내 학회)
- [C88] S. Kim and H. Oh. Deep learning-based indoor hazardous gas source localization and pollution monitoring using mobile robot. The 21th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2026. (국내 학회)
- [C87] J. Seo, J. Kim, S. Kim, C. Kim, W. Shin and H. Oh. Real-time communication relay planning with a low-complexity network quality prediction model in dynamic indoor missions. The 21th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2026. (국내 학회)

**2025**

- [J81] Y. Song, N.P. Nguyen and \*H. Oh. Safety-critical optimal flocking control algorithm with feasibility enhancement of high-order control barrier functions, IEEE Transactions on Control of Network Systems, Vol. 12, No. 3, pp. 2052-2063, 2025.
- [J80] C. Kim, G. Bae, W. Shin, S. Wang and \*H. Oh. EKF-based Radar-inertial odometry with online temporal calibration, IEEE Robotics and Automation Letters, Vol. 10, No. 7, pp. 7230-7237, 2025.
- [J79] J. Lee, H. Jang, M. Park and \*H. Oh. Enhanced reward function design for source term estimation based on deep reinforcement learning, IEEE Access, Vol. 13, pp. 87777-87792, 2025.
- [J78] H. Shin, S. Bae, H. Kim, G. Bae, T. Park, G. Yim, J. Lee, D. Lee, S. Woo and \*H. Oh. Rapid and safe human detection in uninhabited terrains integrating formation flight and multispectral imaging, International Journal of Control, Automation, and Systems, Vol. 23, No. 5, pp. 1527-1541, 2025.
- [J77] J. Seo, G. Bae and \*H. Oh. Kalman filter-based distributed Gaussian process for unknown scalar field estimation in wireless sensor networks, Expert Systems With Applications, Vol. 285, pp. 1-11, 2025.
- [J76] N.P. Nguyen, \*H. Oh and \*J. Moon. Composite trajectory tracking control for under-actuated crane systems with matched and mismatched disturbances, Mechanical Systems and Signal Processing, Vol. 226, pp. 1-24, 2025.
- [J75] S. Kim, J. Seo, H. Jang, C. Kim, M. Kim, J. Pyo and \*H. Oh. Gas source localization in unknown indoor environments using dual-mode information-theoretic search, IEEE Robotics and Automation Letters, Vol. 10, No. 1, pp. 588-595, 2025.
- [C91] W. Shin, M. Kim, T. Park, G. Bae, S. Kim and H. Oh. Vision-based autonomous drone landing on fast-moving platforms via deep reinforcement learning, 13th International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, 2025 (presentation-only option).
- [C90] M.Y. Choi, H. Ko, H. Cho, C. Kim, S. Kim, J. Seo, and H. Oh. Communication-free collective navigation for a swarm of UAVs via LiDAR-based deep reinforcement learning, 13th International Conference on Robot Intelligence Technology and Applications (RiTA), London, UK, 2025 (presentation-only option).
- [C89] J. Lee, H. Jang and H. Oh. Autonomous hazardous gas source localization via disagreement-augmented reinforcement learning, Asia-Pacific International Symposium on Aerospace Technology (APISAT), Seoul, Korea, 2025 (presentation-only option).
- [C88] H. Park, H. Jang, S. Kim, J. Lee, J. Kim and H. Oh. Semantic-GSL: Semantically guided gas source localization with vision-language models, Active Perception Workshop in International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, 2025 (poster-only option).
- [C87] J. Lee, H. Jang, S. Kim, H. Park, H. Kim, C. Kim and H. Oh. Source term estimation using curiosity-driven information-guided reinforcement learning in turbulent environments, Active Perception Workshop in International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, 2025 (spotlight-presentation).
- [C86] H. Jeong, M. Joo, H. Shin, H. Song, H. Oh, J. Jeon, T. Kim and H. Ahn. Demonstrating artistic drawing on low-cost robot, 9th Annual Conference on Robot Learning (CoRL) Demos, Seoul, Korea, 2025.
- [C85] J. Kim, G. Bae, C. Kim, J. Lee, W. Shin and H. Oh. Doppler correspondence: Non-iterative scan matching with Doppler velocity-based correspondence, Robotics: Science and Systems (RSS), LA, USA, 2025.
- [C84] M. Kim, G. Bae, J. Lee, W. Shin, C. Kim, M.Y. Choi, H. Shin and H. Oh. RAPID: Robust and agile planner using inverse reinforcement learning for vision-based drone navigation, Robotics: Science and Systems (RSS), LA, USA, 2025.
- [C83] T. Park, J. Lee, H. Oh, W.J. Yun and K.W. Lee. Optimizing indoor farm monitoring efficiency using UAV: yield estimation in a GNSS-denied cherry tomato greenhouse, Field Robotics Workshop in International Conference on Robotics and Automation (ICRA), Atlanta, USA, 2025 (spotlight-presentation).
- [C82] S. Kim, J. Seo, H. Jang, C. Kim, M. Kim, J. Pyo and H. Oh. Gas source localization in unknown indoor environments using dual-mode information-theoretic search, International Conference on Robotics and Automation (ICRA), Atlanta, USA, 2025 (with IEEE RA-L option).
- [J9] H. Park, H. Jang, S. Kim, J. Kim and H. Oh. EV-infotaxis: extended vision-language model-based infotaxis for efficient gas source term estimation and search. Journal of Institute of Control, Robotics and Systems, 31(6):643-653, 2025. (국내 학술지)
- [C86] H. Cho, G. Bae, M.Y. Choi, J. Hur and H. Oh. Development of a JSBSim-based simulation environment and autonomous mission algorithms for manned-unmanned teaming. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Gangwon, Nov 2025. (국내 학회)
- [C85] C. Lee, T. Park, G. Lee, S. Won, J. Shim, D. Kim, H. Oh and W. Yun. Autonomous pollination robot system for indoor vertical strawberry farming: development and experimental evaluation. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C84] S. Lee, T. Park and H. Oh. Improving quadruped robot attitude estimation accuracy using geodesic loss. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C83] S. Park, M. Jung and H. Oh. Spatial and object semantics with large language models for multi robot task allocation. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C82] J. Kim, J. Lee, G. Bae, C. Kim, W. Shin and H. Oh. Efficient scan matching leveraging doppler velocity. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C81] T. Park, J. Lee, H. Oh, W. Yoon and K. Lee. Optimizing indoor farm monitoring efficiency using UAV: yield estimation in a GNSS-denied cherry tomato greenhouse. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C80] H. Shin, S. Kim, G. Yim and H. Oh. Robust and real-time occupancy grid map prediction via aleatoric uncertainty and neural network acceleration on embedded systems. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C79] M. Kim, G. Bae, J. Lee, W. Shin, C. Kim, M.Y. Choi, H. Shin and H. Oh. Vision-based drone navigation using inverse reinforcement learning. The 40th ICROS Annual Conference (ICROS 2025), Jeonju, June 2025. (국내 학회)
- [C78] J. Lee, T. Park, H. Ko, J. Kim, G. Bae, C. Bae and H. Oh. Drone-based cherry tomato yield estimation in greenhouse farms. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)
- [C77] W. Shin, M. Kim, T. Park and H. Oh. Vision-based autonomous landing on a fast-moving platform using deep reinforcement learning. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)
- [C76] J. Lee, H. Jang, H. Park and H. Oh. Autonomous hazardous gas source search using deep reinforcement learning. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)
- [C75] T. Park, H. Oh and Y. Yu. Realtime 3D multi-object tracking for cherry tomato counting and size estimation. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)
- [C74] S. Kim, H. Jang, C. Kim and H. Oh. Autonomous gas source localization algorithm in indoor environments using mobile robots. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)
- [C73] M. Jung, J. Kim, H. Shin and H. Oh. Improving efficiency of swarm flight by utilizing inactivity in nature. The 20th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2025. (국내 학회)

**2024**

- [J74] L. Xu, \*H. Lu, J. Wang, H. Oh, X. Guo and L. Guo. Oscillation suppression-enhanced cooperative control via refined cooperative disturbance estimation for aerial co-transportation system, IEEE Transactions on Automation Science and Engineering, Vol. 22, pp. 8371-8385, 2024.
- [J73] N. Nguyen, \*H. Oh and \*J. Moon. Continuous integral-type sliding mode tracking control of under-actuated cranes: theory and experiments, Nonlinear Dynamics, 112:16295–16313, 2024.
- [J72] L. Xu, \*H. Lu, J. Wang, H. Oh, X. Guo and L. Guo. Force-coordination control for aerial collaborative transportation based on lumped disturbance separation and estimation, IEEE Transactions on Aerospace and Electronic System, Vol. 60, No. 5, pp. 6037-6049, 2024.
- [J71] P. Ladosz, M. Mammadov, H. Shin, W. Shin, and \*H. Oh. Autonomous landing on a moving platform using vision-based deep reinforcement learning, IEEE Robotics and Automation Letters, Vol. 9, No. 5, pp. 4575-4582, 2024.
- [J70] N.P. Nguyen, \*H. Oh and \*J. Moon. Finite-time continuous nonsingular terminal modified adaptive-gain super-twisting control: application to a 2-DOF planar robot manipulator system, IEEE Transactions on Cybernetics, Vol. 54, No. 5, pp. 2838-2851, 2024.
- [J69] S. Bae, H. Shin, H. Kim, M. Park, M. Choi and \*H. Oh. Deep learning-based human detection using RGB/IR images from drones, International Journal of Aeronautical and Space Sciences, Vol. 25, pp. 164-175, 2024.
- [C81] J. Kim, W. Shin, H. Shin, M. Kim, J. Lee and H. Oh. ReDepth: rectified activations for robust depth estimation, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C80] H. Park, H. Jang, J. Seo and H. Oh. B-MCTS for information-theoretic source search in urban environments, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C79] G. Yim, H. Park, S. Bae, J. Seo and H. Oh. An efficient image filtering algorithm for UAV-based photogrammetry using ORB feature matching in large-scale outdoor environments, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C78] J. Lee, H. Jang, M. Park and H. Oh. GMM information gain-based deep reinforcement learning for source term estimation, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C77] H. Kim, I. Jang and H. Oh. Hedonic game for task allocation in heterogeneous multi-robot systems, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (presentation-only option).
- [C76] T. Park, S. Kim and H. Oh. Designing and identification of keypoint patches in unstructured environments, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C75] S. Kim, H. Shin, G. Yim and H. Oh. Enhancing exploration efficiency using uncertainty-aware information prediction, 12th International Conference on Robot Intelligence Technology and Applications (RiTA), Ulsan, Korea, 2024 (poster-only option).
- [C74] M. Kim, G. Bae, J. Lee, W. Shin, H. Shin, M.Y. Choi and H. Oh. RAPID: Robust and agile planner using inverse reinforcement learning for drones, 14th Workshop on Planning, Perception and Navigation for Intelligent Vehicles in International Conference on Intelligent Robots and Systems (IROS), Abu Dhabi, UAE, 2024.
- [C73] J. Kim, M. Jung, H. S. Shin, H. Oh and A. Tsourdos. Efficient flocking control for swarm robots using reinforcement learning-based lazy agents, International Symposium on Swarm Behavior and Bio-Inspired Robotics (SWARM), Kyoto, Japan, 2024 (presentation-only option).
- [C72] J. Kim, M. Jung, H. S. Shin, H. Oh and A. Tsourdos. Deep reinforcement learning-based neighbor selection of a cucker-smale flocking algorithm, International Conference on Control, Decision and Information Technologies (CoDIT), Vallette, Malta, 2024.
- [C71] C. Kim, G. Bae, W. Shin and H. Oh. Multi-state constraint radar-inertial odometry, International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 2024 (poster-only option).
- [C70] H. Jang, J. Seo and H. Oh. Information-driven search strategy for multiple hazardous gas sources in turbulent environments, International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 2024 (poster-only option).
- [C69] S. Kim, J. Seo, H. Jang and H. oh. Gas source localization in complex unknown indoor environments using a hierarchical planner, International Conference on Industrial Technology (ICIT), Bristol, UK, 2024 (presentation-only option).
- [C68] J. Seo, G. Yim and H. Oh. Routing formation control strategy for constructing a chain network system using unmanned vehicles, International Conference on Industrial Technology (ICIT), Bristol, UK, 2024 (presentation-only option).
- [J8] Y. Song, H. S. Park, Y. You, M. Lee and H. Oh. Swarm mode design and hybrid flocking control algorithm for swarm operation of small fixed-wing UAVs. Journal of Institute of Control, Robotics and Systems, 30(11):1277-1286, 2024. (국내 학술지)
- [J7] M. Y. Choi, W. Shin, M. Kim, H. S. Park, Y. You, M. Lee and H. Oh. Collective navigation through a narrow gap for a swarm of UAVs using curriculum-based deep reinforcement learning. The Journal of Korea Robotics Society, Feb 2024. (국내 학술지)
- [C72] G. Bae, J. Seo, T. Park, W. Shin, J. Lee, H. Ko, M. Jung, H. Jang, M. Gu and H. Oh. Real-time fruit tracking framework for autonomous drone-based crop monitoring systems. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Gangwon, Nov 2024. (국내 학회)
- [C71] M. Jung, J. Seo, Y. Song and H. Oh. Communication relay strategies for fixed-wing UAV Swarms. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Gangwon, Nov 2024. (국내 학회)
- [C70] C. Kim, J. Kim, J. Pyo, M. Kim and H. Oh. EKF-based radar-inertial odometry with temporal calibration. The 39th ICROS Annual Conference (ICROS 2024), Daejeon, July 2024. (국내 학회)
- [C69] M. Mammadov and H. Oh. End-to-end autonomous racing with reinforcement learning using 2D lidar. The 19th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2024. (국내 학회)
- [C68] H. Kim, S. Bae, H. Shin, T. Park, G. Bae and H. Oh. Safe survivor detection algorithm using multiple unmanned aerial vehicles. The 19th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2024. (국내 학회)
- [C67] G. Yim, J. Lee, S. Bae, H. Ko and H. Oh. 3D reconstruction strategy of UAV for enhancing quality of reconstructed surface area. The 19th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2024. (국내 학회)

**2023**

- [J68] N.P. Nguyen, \*H. Oh and \*J. Moon, Y. Kim. Multivariable disturbance observer-based finite-time sliding mode attitude control for fixed-wing UAVs under matched and mismatched disturbances, IEEE Control Systems Letters, Vol. 7, pp. 1999-2004, 2023.
- [J67] Y. Song, S. Lim, \*H. Oh, H. Myung, H. Lee, J. Jung, and H. Lim. Distributed swarm system with hybrid-flocking control for small fixed-wing UAVs: algorithms and flight experiments, Expert Systems With Applications, Vol. 229, 120457, 2023.
- [J66] H. Jang, M. Park and \*H. Oh. Improved Socialtaxis for information-theoretic source search using cooperative multiple agents in turbulent environments, Expert Systems With Applications, Vol. 225, 120033, 2023.
- [J65] Y. Song, H. Lee, C. Kwon, H. Shin and \*H. Oh. Distributed estimation of stochastic multi-agent systems for cooperative control with a virtual network, IEEE Transactions on Systems, Man and Cybernetics: Systems, Vol. 53, No. 4, pp. 2350-2362, 2023.
- [J64] M. Park, P. Ladosz, J. Kim and \*H. Oh. Receding horizon-based Infotaxis with random sampling for source search and estimation in complex environments, IEEE Transactions on Aerospace and Electronic Systems, Vol. 59, No. 1, pp. 591-609. 2023.
- [J63] H. Park, G. Bae, I. Kim, \*H. Oh and \*S. Kim. Development of flapping wing robot and vision-based obstacle avoidance strategy, PeerJ Computer Science, 9:e1201, pp. 1-35, 2023.
- [J62] J. Seo, G. Bae and \*H. Oh. Collision-free active sensing for maximum seeking of unknown environment fields with Gaussian processes, Expert Systems With Applications, Vol. 216, 119459, 2023.
- [C67] N. P. Nguyen, H. Oh, J. Moon and Y. Kim. Multivariable disturbance observer-based finite-time sliding mode attitude control for fixed-wing UAVs under matched and mismatched disturbances, 62nd IEEE Conference on Decision and Control (CDC), Marina Bay Sands, Singapore, 2023 (with IEEE L-CSS option).
- [C66] N. P. Nguyen, H. Oh and J. Moon. Integral sliding mode tracking control of under-actuated gantry cranes: theory and experiment, 11th International Conference on Robot Intelligence Technology and Applications (RiTA), Taicang, China, 2023 (presentation-only option).
- [C65] H. Jang, J. Lee and H. Oh. Efficient information-driven strategy for localizing and searching multiple gas sources in turbulent environments, Workshop in Robotics Science and Systems (RSS), Korea, 2023.
- [C64] M. Kim, G. Bae, P. Ladosz, H. Shin and H. Oh. Learning from the best: inverse imitation learning for agile drone flight, Workshop in Robotics Science and Systems (RSS), Korea, 2023.
- [C63] H. Shin, T. Park and H. Oh. Fast monocular depth estimation with neural network compression on embedded systems for drone collision avoidance, International Conference on Robotics and Automation (ICRA), UK, 2023 (poster-only option).
- [C62] J. Seo, G. Bae and H. Oh. Unknown scalar field estimation with robotic sensor networks utilizing Kalman filter-based distributed Gaussian process , International Conference on Robotics and Automation (ICRA), UK, 2023 (poster-only option).
- [C61] Y. Song, N.P. Nguyen and H. Oh. Safety-critical optimal control using control barrier function with selective relaxation method, International Conference on Control, Automation and Systems (ICCAS), Korea, 2023.
- [J6] T. Park, H. Shin and H. Oh. Detection of fiducial marker with neural network compression. Journal of Institute of Control, Robotics and Systems, 29(8):628-635, 2023. (국내 학술지)
- [C66] Y. Song and H. Oh. Optimal flocking control algorithm with guaranteed feasibility of control barrier function. The 38th ICROS Annual Conference (ICROS 2023), Samcheok, June 2023. (국내 학회)
- [C65] H. Jang, J. Lee, and H. Oh. Information-driven search strategy for multiple hazardous gas sources in turbulent environments. The 38th ICROS Annual Conference (ICROS 2023), Samcheok, June 2023. (국내 학회)
- [C64] J. Seo, G. Bae, and H. Oh. Kalman filter-based distributed Gaussian process approach for estimating unknown environments With Robotic Sensor Networks. The 38th ICROS Annual Conference (ICROS 2023), Samcheok, June 2023. (국내 학회)
- [C63] T. Park and H. Oh. A research on accelerated deep learning-based fiducial marker detection. The 18th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2023. (국내 학회)
- [C62] H. Shin and H. Oh. Monocular depth estimation with neural network compression for collision avoidance with deep reinforcement learning. The 18th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2023. (국내 학회)
- [C61] S. Bae, H. Shin, H. Kim, M. Park, M. Choi, and H. Oh. Accelerated RGB/IR-based object detection and formation flight for survivor detection. The 18th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2023. (국내 학회)
- [C60] S. Kim, C. Kim, and H. Oh. A study on the autonomous driving system of small unmanned ground robot in disaster environments. The 18th Korea Robotics Society Annual Conference, Pyeongchang, Feb 2023. (국내 학회)
- [B5] M. Park, S. An, H. Jang and H. Oh. Information-theoretic autonomous source search and estimation of mobile sensors. Control of Autonomous Aerial Vehicles, H. Shin, G. Inalhan and A. L’Afflitto (Eds), Springer, 2023. (책 속 장)

**2022**

- [J61] N.P. Nguyen, \*H. Oh and \*J. Moon. Continuous nonsingular terminal sliding mode control with integral-type sliding surface for disturbed systems: application to the attitude control for quadrotor UAVs under external disturbances, IEEE Transactions on Aerospace and Electronic Systems, Vol. 58, No. 6, pp. 5635-5660, 2022.
- [J60] J. Choi, M. Seo, H.S. Shin and \*H. Oh. Adversarial swarm defence using multiple fixed-wing Unmanned Aerial Vehicles, IEEE Transactions on Aerospace and Electronic Systems, Vol. 58, No. 6, pp. 5204-5219, 2022.
- [J59] G. Cho, J. Choi, G. Bae and \*H. Oh. Autonomous ship deck landing system of a quadrotor UAV using feed-forward image-based visual servoing, Aerospace Science and Technology, Vol. 130, 107869, 2022.
- [J58] M. Jung and \*H. Oh. Heterogeneous mission planning of a single UAV with attention-based deep reinforcement learning, PeerJ Computer Science, 8:e1119, pp. 1-17, 2022.
- [J57] M. Park, P. Ladosz, and \*H. Oh. Source term estimation using deep reinforcement learning with Gaussian mixture model feature extraction for mobile sensors, IEEE Robotics and Automation Letters, Vol. 7, No. 3, pp. 8323-8330, 2022.
- [J56] P. Ladosz, L. Weng (@OpenAI), M. Kim and \*H. Oh. Exploration in deep reinforcement learning: a survey, Information Fusion, Vol. 85, pp. 1-22, 2022.
- [J55] M. Kim, P. Ladosz and \*H. Oh. Monocular vision-based time-to-collision estimation for small drones by domain adaptation of simulated images, Expert Systems With Applications, Vol. 199, 116973, 2022.
- [J54] M. Kim, J. Kim, M. Jung and \*H. Oh. Towards monocular vision-based autonomous flight through deep reinforcement learning, Expert Systems With Applications, Vol. 198, 116742, 2022.
- [J53] S. An, M. Park and \*H. Oh. Receding-horizon RRT-Infotaxis for autonomous source search in urban environments, Aerospace Science and Technology, Vol. 120, 107276, 2022.
- [C60] M. Park, P. Ladosz and H. Oh. Source term estimation using deep reinforcement learning with Gaussian mixture model feature extraction for mobile sensors, International Conference on Intelligent Robots and Systems (IROS), Japan, 2022 (with IEEE RA-L option).
- [C59] G. Bae, J. Seo, H. Oh. Distributed Gaussian process regression for multi-agent active sensing with hyperparameter tuning. 10th International Conference on Robot Intelligence Technology and Applications (RiTA), Gold Coast, Australia, 2022 (presentation-only option).
- [C58] M. Jung and H. Oh. Decentralized multi-robot task allocation with attention-based deep reinforcement learning algorithm. 10th International Conference on Robot Intelligence Technology and Applications (RiTA), Gold Coast, Australia, 2022 (presentation-only option).
- [C57] Y. Song and H. Oh. Optimal flocking control algorithm with feasibility enhancement of control barrier function. 10th International Conference on Robot Intelligence Technology and Applications (RiTA), Gold Coast, Australia, 2022 (presentation-only option).
- [C56] N. P. Nguyen, H. Oh and J. Moon. Continuous sliding mode control for indoor under-actuated overhead crane systems. 22nd International Conference on Control, Automation and Systems (ICCAS), Pusan, Korea, 2022 (presentation-only option).
- [C55] M. Jung, H. Shin and H. Oh. Deep learning-based UAV trail following with the neural network model compression. Asian Control Conference, Jeju, Korea, 2022 (presentation-only option).
- [C54] M. Kim and H. Oh. Boustrophedon coverage path planning using deep reinforcement learning based traveling salesman problem. Asian Control Conference, Jeju, Korea, 2022 (presentation-only option).
- [J5] H. Shin and H. Oh. Neural network model compression algorithms for image classification in embedded systems. The Journal of Korea Robotics Society, Vol. 17, No. 2, pp. 133-141, 2022. (국내 학술지)
- [C59] M. Kim, G. Bae, H. Shin, and H. Oh. Vision-based highspeed collision-free trajectory generation using sample efficient inverse reinforcement learning. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Jeju, Nov 2022. (국내 학회)
- [C58] H. Shin and H. Oh. Research trends on fast information processing techniques for intelligent flight control. KIMST Conference, Jeju, June 2022. (국내 학회)
- [C57] T. Park, S. Kim, C. Kim, G. Bae, H. Shin, P. Ladosz, and H. Oh. Development of autonomous flight framework for exploration and object position estimation in an unknown indoor environment. The 37th ICROS Annual Conference, Geoje, June 2022. (국내 학회)
- [C56] T. Park, H. Shin, and H. Oh. A study on accuracy and computation performance of compressed deep neural network deployed on FPGA. The 37th ICROS Annual Conference, Geoje, June 2022. (국내 학회)

**2021**

- [J52] J. Prada, J. Im, H. Oh and \*C. Song, Enhanced location tracking in sensor fusion-assisted virtual reality micro-manipulation environments, PLoS ONE 16(12): e0261933, 2021.
- [J51] M. Park, S. An, J. Seo and \*H. Oh. Autonomous source search for UAVs using Gaussian mixture model-based Infotaxis: algorithm and flight experiments, IEEE Transactions on Aerospace and Electronic Systems, Vol. 57, No. 6, pp. 4238-4254, 2021.
- [J50] Y. Yan, \*C. Liu, W.H. Chen and H. Oh. Dual-layer optimization-based control allocation for a fixed-wing aircraft, Aerospace Science and Technology, Vol. 119, 107184, 2021.
- [J49] Y. Song, M. Gu, J. Choi, \*H. Oh, S. Lim, H. Shin and A. Tsourdos. Using lazy agents to improve the flocking efficiency of multiple UAVs, Journal of Intelligent and Robotic Systems, 103(53):1-17, 2021.
- [J48] N.P. Nguyen, \*H. Oh and Y. Kim, \*J. Moon, J. Yang and W.H. Chen. Finite-time disturbance observer-based modified super-twisting algorithm for systems with mismatched disturbances: application to fixed-wing UAVs under wind disturbances, International Journal of Robust and Nonlinear Control, 31(15):7317-7343, 2021.
- [J47] N.P. Nguyen, \*H. Oh, Y. Kim and \*J. Moon. A nonlinear hybrid controller for swinging-up and stabilizing the rotary inverted pendulum, Nonlinear Dynamics, 104(2):1117-1137, 2021.
- [J46] J. Kim, \*H. Oh, B. Yu and S. Kim. Optimal task assignment for UAV swarm operations in hostile environments, International Journal of Aeronautical and Space Sciences, 22(2), 456-467, 2021.
- [J45] X.T. Tran and \*H. Oh. A modified generic second order algorithm with fixed-time stability, ISA Transactions, Vol. 109, pp. 72-80, 2021.
- [J44] D. Shin, Y. Song, J. Oh and \*H. Oh. Nonlinear disturbance observer-based standoff target tracking for small fixed-wing UAVs, International Journal of Aeronautical and Space Sciences, 22(1), 108-119, 2021.
- [C53] M. Jung, H. Oh and H. Shin. Heterogeneous mission planning of UAVs with attention-based deep reinforcement learning. 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, 2021 (presentation-only option).
- [C52] J. Seo and H. Oh. Collision-free active sensing for maximum seeking of unknown environment fields with Gaussian processes. 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, 2021 (presentation-only option).
- [C51] M. Kim, P. Ladosz and H. Oh. Uncertainty-aware time-to-collision prediction using convolutional long-short-term memory networks. 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, 2021 (presentation-only option).
- [C50] H. Park, G. Bae, I. Kim, H. Oh and S. Kim. Development of CNUX-mini flapping wing MAV and vision-based obstacle avoidance strategy. 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, 2021 (presentation-only option).
- [C49] G. Cho, J. Choi, G. Bae and H. Oh. Autonomous ship deck landing of UAVs using feed-forward image-based visual servoing. 9th International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, 2021 (presentation-only option).
- [C48] H. Jang, M. Park and H. Oh. Improved socialtaxis for information-theoretic source search using cooperative multiple agents in turbulent environments. Asia-Pacific International Symposium on Aerospace Technology (APISAT), Jeju, Korea, 2021 (presentation-only option).
- [C47] J. Seo, G. Bae, Y. Song and H. Oh. Active sampling for maximum seeking and environment field reconstruction using cooperative mobile sensors. 21st International Conference on Control, Automation and Systems (ICCAS), Jeju, Korea, 2021 (presentation-only option).
- [C46] N. P. Nguyen, H. Oh and J. Moon. A simple finite-time position tracking controller for servo motor systems. 21st International Conference on Control, Automation and Systems (ICCAS), Jeju, Korea, 2021 (presentation-only option).
- [C55] G. Kim and H. Oh. Multi-agent deep reinforcement learning for multi-regional coverage path planning. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Jeju, Nov 2021. (국내 학회)
- [C54] Y. Song, M. Gu, and H. Oh. Coverage path planning using multiple fixed-wing UAVs and replanning through task allocation. In Autumn Conference of Korean Society for Aeronautical and Space Sciences, Jeju, Nov 2021. (국내 학회)
- [C53] M. Park, J. Seo, and H. Oh. Experimental verification for cognitive search strategy to estimate hazardous substance source using autonomous unmanned mobile vehicle. In Spring Conference of the Korea Society of Mechanical Engineers (KSME), Ulsan, June 2021. (국내 학회)
- [C52] G. Cho, J. Choi, G. Bae, and H. Oh. Autonomous ship deck landing using feed-forward image-based visual servoing. In Spring Conference of the Korea Society of Mechanical Engineers (KSME), Ulsan, June 2021. (국내 학회)

## 과제

누리집 Projects 페이지의 「KAIST: As a PI or Co-I」 표 가운데 기간이 2021년 10월 이후에 걸친 37건(진행 중 19건, 끝난 과제 18건)이다. 기간, 지원 기관, 역할(Principal Investigator·Researcher 등)은 표 그대로다. 누리집은 이 표를 「KAIST」 제목 아래 두지만, 2025년 8월 KAIST 부임 전에 시작한 과제가 섞여 있다.[^projects]

- Neuro-Symbolic Physical AI for Autonomous Robotic Teams: Physical AI Platform (기간 10.2026-08.2029; 지원 HANHWA AEROSPACE/ADD; 역할 Researcher; 상태 Ongoing)
- Development of Key AI Technologies for Autonomous Operation and Enhanced Survivability in Cooperative High-Speed Unmanned Aerial Vehicles (기간 10.2026-02.2029; 지원 KAI/ADD; 역할 Researcher; 상태 Ongoing)
- Development of Reliability Assurance Technology for Autonomous Missions to Ensure Aviation AI Safety (기간 10.2026-12.2029; 지원 KARI/KASA; 역할 Principal Investigator; 상태 Ongoing)
- Research on LiDAR-Based Obstacle Detection, Avoidance, and Navigation Algorithms for Lunar Landers (기간 04.2026-12.2027; 지원 KARI/KASA; 역할 Principal Investigator; 상태 Ongoing)
- Development of Path Generation Algorithms for Mobile Robots in Constrained Ship Block Environments (기간 04.2026-09.2026; 지원 HD KSOE; 역할 Principal Investigator; 상태 Ongoing)
- Learning-Based Anti-Drone Control System (기간 04.2026-09.2026; 지원 Nearthlab; 역할 Principal Investigator; 상태 Ongoing)
- Development of an Automated Indoor Farm Data Processing System for Robotic Perception (기간 04.2026-09.2026; 지원 Metafarmers; 역할 Principal Investigator; 상태 Ongoing)
- Development of Apple Growth Diagnosis Technology and AI Monitoring System (기간 04.2026-12.2030; 지원 MAFRA; 역할 Researcher; 상태 Ongoing)
- High-Performance Fully-Actuated Drone Platform: Enabling Ultra-Precise Digital Twin Framework for Smart Agriculture (기간 04.2026-12.2026; 지원 KAIST Institute; 역할 Principal Investigator; 상태 Ongoing)
- InnoCORE Research Group: AI-Transformed Aerospace (기간 07.2025-12.2029; 지원 MSIT; 역할 Researcher; 상태 Ongoing)
- Development and Demonstration of Intelligent Agricultural Robots and Control Systems for Fruit and Vegetable Crops (기간 04.2025-12.2027; 지원 MAFRA; 역할 Researcher; 상태 Ongoing)
- Technology Development for Bioinspired Avian-Type Unmanned Air Vehicle (기간 08.2025-09.2029; 지원 ADD; 역할 Researcher; 상태 Ongoing)
- Techonology Development of Atmospheric Environment UAV One-Stop Platform (기간 05.2025-12.2029; 지원 MCEE; 역할 Researcher; 상태 Ongoing)
- Development of Sensor Fusion and Mission Autonomy Algorithms for Manned-Unmanned Aerial Teaming (기간 05.2024-11.2028; 지원 KAI/ADD; 역할 Researcher; 상태 Ongoing)
- Vision-Based Fast, Highly Reliable, and Agile Autonomous Drone Flight Using Deep Learning Approaches (기간 03.2023-02.2027; 지원 NRF; 역할 Principal Investigator; 상태 Ongoing)
- Mission Planning and Autonomous Mission Replanning for Tactical UAV Swarm (기간 02.2023-11.2026; 지원 LIGNEX1/ADD; 역할 Researcher; 상태 Ongoing)
- Development of a Wireless Teleoperable Relief Robot for Detecting Searching and Responding in Narrow Space (기간 04.2022-12.2026; 지원 KEIT; 역할 Researcher; 상태 Ongoing)
- Theater Defence Research Center: High Speed Big Data Processing Technology for Intelligent Flight Control (기간 12.2020-02.2027; 지원 KAIST/ADD; 역할 Principal Investigator (세부책임); 상태 Ongoing)
- Advanced Vehicle Autonomy & Intelligence Technology Development for Unmanned Vehicles (기간 06.2020-03.2027; 지원 MSIT/KARI; 역할 Researcher; 상태 Ongoing)
- Development CAD-Based Real-Time Position Estimation System for Autonomous Mobile Robots Inside Ship Block (기간 08.2025-11.2025; 지원 HD KSOE; 역할 Principal Investigator; 상태 Completed)
- Development of Smart Environment Monitoring System Technology using Autonomous Unmanned Systems (기간 06.2020-07.2025; 지원 NRF; 역할 Researcher; 상태 Completed)
- Development of a Swarm Operation Simulator (기간 02.2023-12.2024; 지원 LIGNEX1/ADD; 역할 Researcher; 상태 Completed)
- Real-time Wide Area Airborne Detection System for Ground Explosives Using Drones (기간 06.2020-12.2024; 지원 DBrain/ADD; 역할 Researcher; 상태 Completed)
- Path Planning for Vision-Based 3-D Mapping Using Tilt-Rotor UAV (기간 02.2024-10.2024; 지원 NARMA; 역할 Principal Investigator; 상태 Completed)
- Integrated Simulation and UAV Operation Test of Mission Space Modelling Equipment (기간 06.2024-12.2024; 지원 KARI; 역할 Principal Investigator; 상태 Completed)
- Development of Vision-Based Safety Alarm System for Crane Workers (기간 01.2024-05.2024; 지원 HD Hyundai; 역할 Principal Investigator; 상태 Completed)
- HILS of Mission Space Modelling Equipment (기간 07.2023-12.2023; 지원 KARI; 역할 Principal Investigator; 상태 Completed)
- Improvement on Search and Human Detection Using Outdoor Ad-Hoc Network-Based Drone Formation Flight (기간 04.2023-11.2023; 지원 ETRI; 역할 Principal Investigator; 상태 Completed)
- State Estimation of a Moving Vehicle and Test Environment Development for Vision-Based Autonomous Landing of the UAV (기간 07.2021-10.2023; 지원 ADD; 역할 Principal Investigator; 상태 Completed)
- Autonomous Multi-Source Search and Estimation Using Multiple Heterogeneous Unmanned Vehicles (기간 06.2020-02.2023; 지원 NRF; 역할 Principal Investigator; 상태 Completed)
- Research on Search and Human Detection Using Outdoor Ad-Hoc Network-Based Drone Formation Flight (기간 05.2022-11.2022; 지원 ETRI; 역할 Principal Investigator; 상태 Completed)
- Design of Mission Space Modelling Equipment for Autonomous Operation of Multiple Heterogeneous Unmanned Vehicles (기간 04.2022-11.2022; 지원 KARI; 역할 Principal Investigator; 상태 Completed)
- Drone System Development for Navy Vessels and Marine Missions (기간 12.2018-03.2022; 지원 Defense Acquisition Program Administration/ADD; 역할 Researcher; 상태 Completed)
- Development of Ground Worker Detection Algorithm From Crane Operation Video (기간 01.2022-03.2022; 지원 KIMM; 역할 Principal Investigator; 상태 Completed)
- Conceptual Design of Mission Space Modelling Equipment for Autonomous Operation of Multiple Heterogeneous Unmanned Vehicles (기간 09.2021-11.2021; 지원 KARI; 역할 Principal Investigator; 상태 Completed)
- Development of Robust Adaptive Control System for a Compound Rotorcraft (기간 02.2020-12.2021; 지원 Loughborough University/ADD; 역할 Principal Investigator; 상태 Completed)
- Optimization for Deep Learning-Based Multiple High-Performance Missions (기간 06.2021-11.2021; 지원 ETRI; 역할 Principal Investigator; 상태 Completed)

## 소식

누리집 첫 화면 「FAIR Lab Updates」의 날짜 있는 소식 5건과 News 페이지의 글 3건, 모두 8건(2026년 4월–2026년 10월)이다. 날짜와 문장은 게시된 그대로다.[^home][^news]

- 2026.10 · Prof. Oh appointed as a Senior Editor for IEEE TAES
- 2026.08 · KAIST FAIR took 1st place in the virtual qualifier of the autonomous drone racing competition organized by Anduril Industries.
- 2026.08 · Prof. Oh received the Outstanding Reviewer Award from IEEE Robotics and Automation Letters
- 2026.07 · Members of KAIST FAIR had a joint-workshop with the Dr. Mohammad Deghat’s group at UNSW, Australia.
- 2026.07 · New members have joined our lab: Seunghoon Lee, Hankyoul Ko, Do Quang Hieu (M.S. student) and Seobeom Lee (Ph.D. student).
- 2026.07 · KAIST FAIR won the best paper award in ICROS 2026
- 2026.04 · ‘Research on LiDAR-based HDA and navigation algorithms for lunar landers’ supported by KARI/KASA has started.
- 2026.04 · Our paper ‘Learning the underlying geometry of point clouds: Theory and practice’ has been accepted for presentation at RSS 2026.

## 연락과 위치

- 연구실 교수실: Rm 6106, Building N7-4(기계공학동 N7 6106), KAIST[^prof][^meprof]
- 전화: 042-350-3028[^prof][^meprof]
- 교수 이메일: h.oh@kaist.ac.kr[^prof][^meprof]
[^p1]: W. Shin 외, H. Oh, IEEE Robotics and Automation Letters 11, 5542-5549 (2026). <https://doi.org/10.1109/lra.2026.3674011> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Seo 외, H. Oh, IEEE Robotics and Automation Letters 11, 322-329 (2026). <https://doi.org/10.1109/lra.2025.3632056> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: N. P. Nguyen 외, J. Yang, IEEE Access, 1-1 (2026). <https://doi.org/10.1109/access.2026.3679398> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://fair.kaist.ac.kr/> (FAIR Lab Updates, 연구실 소식 소개, 2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://fair.kaist.ac.kr/research/> (연구 갈래 여섯 개, 2026-10-23 열람)
[^slam]: 연구실 누리집 Research 「Perception & SLAM」 페이지 <https://fair.kaist.ac.kr/perception-and-slam/> (2026-10-23 열람)
[^path]: 연구실 누리집 Research 「Path/Trajectory Planning」 페이지 <https://fair.kaist.ac.kr/path-trajectory-planning/> (2026-10-23 열람)
[^ap]: 연구실 누리집 Research 「Active Perception」 페이지 <https://fair.kaist.ac.kr/active-perception/> (2026-10-23 열람)
[^mac]: 연구실 누리집 Research 「Multi-Agent Control」 페이지 <https://fair.kaist.ac.kr/multi-agent-control/> (2026-10-23 열람)
[^task]: 연구실 누리집 Research 「Task Assignment」 페이지 <https://fair.kaist.ac.kr/task-assignment/> (2026-10-23 열람)
[^fad]: 연구실 누리집 Research 「Fully-Actuated Drone」 페이지 <https://fair.kaist.ac.kr/fully-actuated-drone/> (2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://fair.kaist.ac.kr/people/instructor/> (Education, Experience, Research Interests, Honours and Awards, Professional Activities, 2026-10-23 열람)
[^members]: 연구실 누리집 Members 페이지 <https://fair.kaist.ac.kr/people/members/> (Postdoctoral Researchers, Ph.D. Students, M.S. Students, Researchers, 2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://fair.kaist.ac.kr/people/alumni/> (2026-10-23 열람)
[^theses]: 연구실 누리집 Thesis/Dissertations 페이지 <https://fair.kaist.ac.kr/thesisdissertations/> ([T01]–[T22], 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 메뉴: International Journals <https://fair.kaist.ac.kr/international-journals/>, International Conferences <https://fair.kaist.ac.kr/international-conferences/>, Domestic Journals <https://fair.kaist.ac.kr/domestic-journals/>, Domestic Conferences <https://fair.kaist.ac.kr/domestic-conferences/>, Book Chapters <https://fair.kaist.ac.kr/bookchapters-2-2/> (2026-10-23 열람)
[^projects]: 연구실 누리집 Projects 페이지 <https://fair.kaist.ac.kr/projects/> (KAIST: As a PI or Co-I, Ongoing·Completed, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://fair.kaist.ac.kr/news/> (2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(오현동) <https://me.kaist.ac.kr/pop/team.html?uid=143&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 사무실, 전화, 2026-10-23 열람)
[^melist]: KAIST 기계공학과 교수진 목록 2쪽 <https://me.kaist.ac.kr/team/team_010100.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1> (오현동 교수 항목, 2026-10-23 열람)
[^meres]: KAIST 기계공학과 연구분야 「ME + AX」 <https://me.kaist.ac.kr/research/research_010100.html> (오현동 교수 항목, 2026-10-23 열람)

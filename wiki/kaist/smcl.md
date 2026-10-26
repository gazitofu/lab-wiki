# 우주비행 임무 및 제어 연구실 (Spaceflight Mission and Control Lab, SMCL)

**KAIST 항공우주공학과 · 이동헌 교수**

- 분야: 달·행성 간 탐사 궤적과 임무 설계(저추력 추진, 중력 도움, 다체 모델), 인공위성 자세 유도·제어(spin-to-spin 경계 조건, 반작용 휠·CMG·추력기), 랑데부·도킹 궤도 유도 알고리즘과 지상 시험장치, 로봇 팔을 단 위성의 경로 계획
- 대분야: 기계·로봇·제조
- 태그: 제어 이론·제어 공학[^attitude][^rdv], 과학·공학 AI[^mission][^iccas], 유도·항법·제어(GNC)[^aelab], 궤도역학·우주 궤적 설계[^mission], 궤도상 서비싱·랑데부·우주 로봇[^rdv], 상태 추정·필터링(데이터 동화)[^aelab]
- 홈페이지: <https://smcl.kaist.ac.kr/>
- 근거와 출처: [우주비행 임무 및 제어 연구실 근거 페이지](smcl-sources.md)

> 우주선을 달과 다른 행성으로 보내는 궤적을 설계하고 최적화하는 일, 인공위성이 원하는 방향을 빠르고 안정적으로 가리키게 하는 자세 유도·제어, 두 우주선이 궤도에서 만나 결합하는 랑데부·도킹의 궤도 유도 알고리즘과 지상 시험장치를 연구하는 항공우주공학과 연구실이다.[^home][^mission][^attitude][^rdv] 학과 연구실 소개는 연구 대상을 행성 탐사를 위한 궤도선과 착륙선, 영상 촬영을 위한 인공위성, 랑데부·도킹이 필요한 우주 시스템으로 적는다.[^aelab]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 이동헌 교수의 연구실이다. 학과 연구실 소개는 연구실 이름을 「우주비행 임무 및 제어 연구실(Spaceflight Mission and Control Lab)」로 적고, 우주 공간을 비행하는 시스템의 임무를 분석해 임무 수행에 필요한 유도·항법·제어(GNC, 비행체가 갈 길과 자세를 정하고 자기 위치를 추정하며 그대로 움직이게 하는 기술)를 연구한다고 소개한다.[^aelab] 학과 교수진 목록은 교수의 연구분야를 Astrodynamics(천체역학), Trajectory Optimization(궤적 최적화), Spacecraft Guidance and Control(우주선 유도·제어), Interplanetary Exploration(행성 간 탐사)으로 적는다.[^aefac] 누리집은 연구를 Interplanetary Mission Design and Analysis, Spacecraft Attitude Guidance and Control, Guidance and Control Algorithms for Space Rendezvous and Docking System의 세 갈래로 나눈다.[^home]

학과 연구실 소개에 따르면 행성 탐사를 위한 궤도선 분야에서는 여러 탐사 궤적과 임무 궤도의 설계 기법을 다루고, 착륙선을 위해서는 정밀 착륙을 위한 유도·항법·제어 알고리즘을 연구한다. 영상 촬영을 위한 인공위성에서는 여러 제약 조건을 고려한 자세 유도 기법을 연구하는데, 최근에는 실시간 유도 기법 생성 알고리즘 개발에 초점을 맞춘다. 랑데부·도킹이 필요한 우주 시스템에서는 근접 운영 단계의 궤도와 기동을 설계하고, 영상 정보로 목표 물체의 상태 정보를 추정하는 기법을 연구한다.[^aelab]

누리집 Research Project 게시판은 진행 중인 과제로 「행성 간 탐사 임무를 위한 궤적설계 기술 연구」(기간 24-01-01~26-12-31, 지원 한국과학기술원)를 적는다.[^project] 누리집 Conference 게시판의 2024–2025년 학회 발표에는 지구-화성 전이 궤적과 발사 기회, 저추력 최적 천이 궤적, spin-to-spin 회전 기동의 최소 시간 분석, CMG 배치와 김발 궤적, 랑데부 근접 기동 궤적, 로봇 팔을 단 위성의 역학 시뮬레이션, 자세 명령 재구성 탑재 소프트웨어가 이어진다.[^conf]

## 주요 연구 주제

### 1. 달·행성 간 탐사 궤적과 임무 설계

연구 페이지에 따르면 연구실은 우주선을 지구 밖의 천체로 보내기 위한 궤적을 계획하고 최적화한다. 저추력 추진(low-thrust propulsion, 작은 추력을 오랫동안 내어 궤도를 바꾸는 추진 방식), 중력 도움(gravity assist, 천체 곁을 지나며 그 중력으로 우주선의 속도와 방향을 바꾸는 기법), 다체 모델(multi-body dynamics model, 여러 천체의 중력을 함께 고려하는 운동 모형) 등을 적용해 우주 탐사 임무를 효율적으로 설계하는 데 주력하고, 수치 시뮬레이션과 최적화 기법, 인공지능 기반 접근법 등으로 탐사 임무 계획을 세운다. 연구 페이지는 이 연구로 소행성과 외행성 탐사를 포함해 지구 중력의 영향 밖으로 나가는 임무를 지원하고 우주선 설계, 항법, 임무 운영 전략에 기여하는 것을 목표로 적는다.[^mission]

대표 논문 1은 달 궤도에 있는 모선 한 대에서 큐브샛(CubeSat, 정해진 규격 단위로 만드는 초소형 위성) 여러 대를 내보내 달 표면에 충돌시키는 임무의 궤도 설계를 다룬다. 섭동(perturbation, 주된 중력 외에 궤도를 조금씩 바꾸는 힘) 때문에 근점(periapsis, 궤도에서 천체에 가장 가까운 점) 방향이 저절로 바뀌는 큐브샛 방출 궤도를 찾아 활용했다.[^p1] 2021–2026년 논문 목록에는 실제 비행한 달 임무의 궤적과 궤도를 단계별로 정리한 Acta Astronautica 논문(2026)도 있다.[^cr] 2024–2025년 학회 발표에는 지구-화성 발사 기회 분석, 원자력 열추진을 이용한 화성 탐사 임무 분석, 지구-아포피스(소행성) 저추력 최소 연료 천이 궤적, 정지 천이 궤도(GTO)에서 정지 궤도(GEO)로 가는 저추력 최적 천이 궤적, 물리 정보 신경망(PINN, 물리 법칙을 담은 식을 학습에 함께 쓰는 신경망) 기반 램버트 문제(두 위치와 비행 시간이 주어질 때 그 사이를 잇는 궤도를 구하는 문제) 풀이, 베이지안 최적화를 이용한 중력 도움 지구-화성 전이 임무 설계가 있다.[^conf]

### 2. 인공위성 자세 유도·제어

연구 페이지에 따르면 궤도에서 위성의 안테나와 탑재체를 원하는 방향으로 가리키고 안정적으로 유지하려면 자세 유도 프로파일(시간에 따라 위성이 취할 자세와 회전 빠르기를 정한 계획)과 여러 구동기를 쓴 정밀 제어가 필요하다. 위성의 자세 기동에서는 하드웨어 제한, 지상국과 통신하기 위한 자세 조건, 관측 임무의 spin-to-spin 경계 조건(기동을 시작하고 끝낼 때 위성이 정지해 있지 않고 회전하고 있는 조건)을 함께 고려해야 하며, 연구실은 이런 제약을 지키면서 빠르고 안정적인 임무 수행이 가능한 최적 자세 유도 알고리즘을 연구한다. 설계한 프로파일을 위성에 효율적으로 올리는 탑재 소프트웨어를 개발하고, 반작용 휠(reaction wheel, 바퀴의 회전 속도를 바꿔 그 반작용으로 위성을 돌리는 장치), CMG(control moment gyroscope, 빠르게 도는 바퀴의 회전축을 기울여 회전력을 얻는 장치), 추력기를 활용한 자세 기동 성능 개선과 구동기 고장 대응 기법도 연구한다.[^attitude]

대표 논문 2는 spin-to-spin 경계 조건과 정해진 최종 시간 아래에서 한 축 회전 기동의 절대 노력 최소화 문제에 대한 닫힌 형태의 해(closed-form solution, 반복 계산 없이 식으로 바로 구하는 해)를 내놓았다.[^p2] 대표 논문 3은 지상에서 자세 유도 프로파일 전체를 보내는 대신 꼭 필요한 정보만 보내고 위성에서 자세 명령을 다시 만들어 내는 탑재 알고리즘이다.[^p3] 2021–2026년 논문 목록에는 각속도 제한이 있는 spin-to-spin 회전 기동의 시간 최적화를 다룬 AIAA SciTech 2026 학회 논문과, 일정한 라인 속도를 유지해야 하는 TDI(시간 지연 적분) 영상 촬영을 위한 자세 프로파일 설계를 다룬 Advances in Space Research 논문(2026)이 있다.[^cr] 누리집 소식에 따르면 비여분 CMG 클러스터(제어에 필요한 수보다 많은 CMG를 두지 않은 CMG 묶음)에서 목표 자세에 이르기 위한 중간 김발 각을 다층 퍼셉트론(MLP, 여러 층의 인공 신경망)으로 추정해 김발 각 궤적을 만드는 방법을 제안한 ICCAS 2025 논문이 Outstanding Student Paper Award를 받았다.[^iccas]

### 3. 랑데부·도킹 유도와 우주 로봇

연구 페이지에 따르면 연구실은 랑데부(궤도에서 두 우주선이 서로 접근해 만나는 일)와 도킹(만난 두 우주선이 결합하는 일) 과정에서 우주선의 궤도를 유도하는 알고리즘을 연구하며, 특히 고정된 크기의 연속 추력을 활용한 유도 알고리즘 개발에 집중한다. 해석적으로 구한 순간 추력 벡터를 고정된 크기의 연속 추력 형태로 바꾸는 방법을 탐색하고, 바꾼 유도 알고리즘의 성능을 최적화 문제와 비교해 검증한다.[^rdv] 또 랑데부·도킹 임무를 모사하는 지상 시험장치를 설계·제작한다. 두 대의 시뮬레이터가 각각 Chaser(다가가는 우주선)와 Target(목표 우주선)의 움직임을 모사해, 최적화 기법으로 설계한 궤적을 실제 임무에 적용하기 전에 지상에서 검증한다. 상대 물체의 위치와 자세를 추정하는 기법(pose estimation)을 연구하기 위해 여러 센서와 마커를 시험장치에 달아 센서와 알고리즘을 검증할 수 있고, 현재 추력기를 이용한 지상 시험장치를 설계·제작하고 있다고 연구 페이지는 적는다.[^rdv]

대표 논문 4는 로봇 팔 두 개를 단 자유 부유(free-floating, 위성 몸체의 위치와 자세를 따로 붙잡아 두지 않아 팔이 움직이면 몸체도 함께 움직이는 상태) 위성의 경로 계획을 입자 군집 최적화로 두 단계에 나눠 푸는 방법이다.[^p4] 2021–2026년 논문 목록에는 전방향 바퀴를 쓴 하드웨어 시뮬레이터 개발과, 자유 부유 이중 로봇 팔 위성의 역학 검증을 다룬 Journal of Aerospace System Engineering 논문 두 편(2026)도 있다.[^cr] 2024–2025년 학회 발표에는 가시선 제한 아래 연료 최소 V-bar 근접 기동 궤적, 도킹 단계 랑데부 접근을 위한 Teardrop Hovering 근접 기동, 자동 랑데부·도킹 유도 알고리즘을 위한 하드웨어 시뮬레이터 설계·제작, 임의의 도킹 축으로 접근하는 우주 쓰레기 제거 궤적 설계가 있다.[^conf]

### 4. 우주비행체 지상 시험 자료 관리

대표 논문 5는 우주선 지상 시험에서 쌓이는 시험 자료를 사람의 개입 없이 중앙 저장소로 옮기고, 엔지니어링 팀마다 맞춘 형식으로 자동 제공하며, 자료 검증도 자동으로 하는 시스템을 다룬다. 저자들은 이 시스템을 실제 우주선 개발과 지상 시험 운영에 적용해 검증했다고 적는다.[^p5]

## 대표 논문

이동헌 교수가 저자인 2021–2026년 논문 가운데 KAIST 부임(2024년 1월) 뒤 나왔고 초록을 확인할 수 있는 다섯 편을 네 연구 갈래(달·행성 간 탐사 궤적과 임무 설계, 인공위성 자세 유도·제어, 랑데부·도킹 유도와 우주 로봇, 지상 시험 자료 관리)에 나눠 골랐다. 2–5번은 교수가 마지막 저자이고, 1번은 교수가 세 저자 가운데 둘째다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^cr] |
|---|---|---|---|---|
| 1 | 2026 | [Orbit Design of Multiple Lunar CubeSat Impactors Deployed from a Single Mothership: A Practical Approach](https://doi.org/10.1007/s42405-025-01121-3) · International Journal of Aeronautical and Space Sciences | 달 궤도에 있는 모선 한 대에서 큐브샛 여러 대를 내보내 달 표면에 충돌시키는 임무의 실용적인 궤도 설계를 내놓았다. 임무 목표는 달의 자기장 이상, 특히 적도 근처의 달 소용돌이 무늬(lunar swirl)를 조사하는 것이다. 큐브샛은 목표 소용돌이 무늬 위를 낮은 고도로 지나며 과학 자료를 모은 뒤 달 표면에 충돌한다. 핵심은 섭동 때문에 근점 벡터가 저절로 바뀌는 큐브샛 방출 궤도(CubeSat Release Orbit, CRO)를 찾아 활용한 것으로, 추가 속도 변화(delta-V)를 많이 들이지 않고 큐브샛을 내보낼 수 있게 한다. Rima Sirsalis, Firsov, Dewar, Reiner Gamma 네 곳의 소용돌이 무늬를 사례로 CRO가 충분한 방출 기회를 준다는 것을 보였고, 큐브샛은 목표 위를 20 km 근처나 그 아래 고도로 지나갔다. 저자들은 이 방식이 모선과 큐브샛의 시스템 복잡성과 운영 위험을 줄이고, 여러 소용돌이 무늬에서 자기장을 측정할 가능성을 높인다고 적는다.[^p1] | 1저자 Y.-J. Song, 둘째 저자 이동헌 (3명) |
| 2 | 2025 | [Closed-Form Solution for the Absolute Effort Minimization Problem for Single-Axis, Spin-to-Spin Maneuvers](https://doi.org/10.1007/s42405-025-00942-6) · International Journal of Aeronautical and Space Sciences | 한 축으로 도는 회전 기동은 우주 임무를 비롯한 여러 분야에 쓰이고, 우주선 자세 제어에서는 연료 최적 제어가 중요한 연구 분야다. 이 논문은 spin-to-spin 경계 조건과 정해진 최종 시간 아래에서 한 축 회전 기동의 절대 노력 최소화 문제(제어 입력의 절댓값을 시간에 대해 적분한 값을 최소로 하는 문제)에 대한 닫힌 형태의 해를 내놓았다. 앞서 정의된 bang-off-bang 구조(최대 입력, 입력 없음, 반대 방향 최대 입력을 차례로 쓰는 구조)를 포함해 각가속도 프로파일 구조 여섯 가지를 도입하고, 상태 변수의 경계 조건을 분류해 문제를 풀었다. 특정 최종 시간에서는 최적해가 없는 경우도 다루었고, 제안한 해를 수치 예제로 검증했다.[^p2] | 1저자 J. Lee, 마지막 저자 이동헌 (2명) |
| 3 | 2026 | [Efficient Attitude Command Reconstruction Algorithm for Satellites Operations](https://doi.org/10.1007/s42405-026-01245-0) · International Journal of Aeronautical and Space Sciences | 지상에서 미리 만든 자세 유도 프로파일 전체를 보내는 대신 꼭 필요한 정보만 보내고, 위성에서 자세 명령을 다시 만들어 내는 탑재 알고리즘을 제안했다. 지구 관측 임무처럼 기동 구간과 임무 구간이 번갈아 오는 프로파일을 대상으로 한다. 기동 구간에서는 닫힌 형태의 각가속도 프로파일에서 각속도 명령을 해석적으로 다시 만들고, 쿼터니언(물체의 회전 상태를 나타내는 수학적 표현) 명령은 평균 각속도 벡터로 이산 전파해 얻는다. 닫힌 형태 식이 없는 임무 구간에서는 보낸 각속도 프로파일을 적분하거나 쿼터니언 프로파일을 미분하는 두 방법을 쓴다. 저자들은 이 알고리즘이 기존의 전체 프로파일 전송 방법에 비해 보내는 자료를 크게 줄이고, 재구성 방식마다 맞춘 자료 구조를 정의하며, 가볍고 수렴이 보장되어 실제 위성 운용에 실용적이라고 적는다. 지구 관측 시나리오의 수치 예제로 효율과 정확도를 검증했다.[^p3] | 1저자 S. Byeon, 마지막 저자 이동헌 (8명) |
| 4 | 2026 | [PSO-Based Two-Step Path Planning for a Dual-Arm Free-Floating Robotic Satellite](https://doi.org/10.1007/s42405-026-01187-7) · International Journal of Aeronautical and Space Sciences | 4자유도 로봇 팔 두 개를 단 자유 부유 위성 시스템의 경로 계획 알고리즘을 제안했다. 목표는 작업 전후 위성의 자세 유지, 로봇 팔과 위성 몸체의 충돌 방지, 완전한 3차원 작업 공간 안의 움직임 세 가지다. 목표가 여럿이어서 궤적 계획을 다목적 최적화 문제로 세우고 입자 군집 최적화(PSO, 여러 후보 해가 서로 정보를 나누며 움직여 해를 찾는 최적화 방법)로 푼다. 기존의 한 단계 PSO는 계산 시간이 길고 여러 제약을 다루기 어려워 두 단계 경로 계획을 제안했다. 첫 단계에서는 조작성(manipulability, 로봇 팔이 여러 방향으로 움직일 수 있는 정도를 나타내는 지표)을 최대로 해 작업이 끝날 때의 시스템 자세를 정하고, 둘째 단계에서는 충돌 회피, 자세 안정화, 관절 속도 제한 같은 제약 아래 PSO로 최적 궤적을 만든다. 수치 시뮬레이션으로 기존 한 단계 PSO와 비교해 효과를 검증했다.[^p4] | 1저자 B. Kim, 마지막 저자 이동헌 (8명) |
| 5 | 2025 | [Enhanced Test Data Management in Spacecraft Ground Testing: A Practical Approach for Centralized Storage and Automated Processing](https://doi.org/10.3390/aerospace12090813) · Aerospace | 우주선이 고속 통신 시스템과 여러 탑재체를 갖추게 되면서 자료가 많아지고 시스템이 복잡해졌다. 특히 지상 시험 단계에서는 방대한 시험 자료를 분류·배포·분석하는 데 시간과 자원이 많이 들어, 시험 효율을 높이고 비용을 줄이는 자료 관리가 중요해졌다. 이 연구는 실제 우주선 개발과 지상 시험 운영에 적용해 검증한, 시험 자료를 중앙에서 다루는 자율 시스템을 내놓았다. 사건이 생길 때 동작하는 구조(event-triggered architecture)로, 시험이 끝나기를 기다리거나 사람이 개입하지 않아도 시험 자료를 중앙 저장소로 빠르게 옮긴다. 옮긴 자료는 엔지니어링 팀마다 맞춘 여러 형식으로 자동 제공해 자료 비교와 분석을 돕고, 시험 자료 검증도 수동 입력 없이 자동으로 한다. 실제 우주선 지상 시험에서 자동 전송과 후처리 동안 생긴 기록을 빅데이터 분석해 성능을 평가했다.[^p5] | 1저자 J. Park, 마지막 저자 이동헌 (3명) |

## 교수와 전문 분야

이동헌 교수(Lee, Donghun)는 KAIST 항공우주공학과 조교수다. 학과 교수진 목록은 직위를 Assistant Professor로, 학력을 B.S. KAIST(2005), M.S. KAIST(2007), Ph.D. KAIST(2010)로, 연구분야를 Astrodynamics, Trajectory Optimization, Spacecraft Guidance and Control, Interplanetary Exploration으로 적는다.[^aefac] 누리집 교수 페이지에 따르면 KAIST 항공우주공학과에서 학사(2005), 석사(2007), 박사(2010)를 받았다. KAIST(2010.09–2011.03), U.S. Naval Postgraduate School(2011.03–2012.09), KAIST(2012.10–2013.11)에서 박사후연구원(Post-doctor)으로, 한국항공우주연구원(Korea Aerospace Research Institute)에서 Senior engineer(2013.12–2021.02)로, 한국항공대학교(Korea Aerospace University)에서 Assistant Professor(2021.03–2023.12)로 일했고, 2024년 1월부터 KAIST Assistant Professor다.[^prof]

2021–2026년 논문 목록에서 KAIST 부임 전 논문은 한국형 달 궤도선(Korea Pathfinder Lunar Orbiter) 임무의 비행 역학 서브시스템, 달 기준 좌표계 변환, 궤도 진입 성능 분석, 비상 궤적 운영 준비, 나로우주센터에서 태양-지구 라그랑주점 임무를 보내는 발사 기회 분석, 궤도 천이 궤적의 조향각 프로파일, 군집 비행체의 대형 전환, spin-to-spin 기동과 한 축 회전 기동의 자세 명령 닫힌 해를 다룬다.[^cr] 이 논문들과 부임 뒤 논문으로 보면 전문 분야는 궤도역학과 달·행성 탐사 궤적 설계, 우주선 자세 기동의 최적 유도, 랑데부·근접 운영과 우주 로봇의 궤적 계획이다.[^cr]

## 응용 분야

연구 페이지들은 응용을 소행성과 외행성 탐사를 포함한 지구 중력권 밖 임무와 우주선 설계·항법·임무 운영 전략[^mission], 관측 임무를 비롯한 여러 위성 임무의 성공률과 신뢰성[^attitude], 향후 우주 탐사와 여러 우주 임무의 궤도 유도 전략[^rdv]으로 적는다. 학과 연구실 소개는 행성 탐사용 궤도선과 착륙선, 영상 촬영용 인공위성, 랑데부·도킹이 필요한 우주 시스템을 다룬다고 적는다.[^aelab] 대표 논문 5는 우주선 개발 과정의 지상 시험 자료 관리에 적용한 시스템이다.[^p5]

## 구성원

누리집 Current Member 게시판 1·2쪽의 석사과정(Master Course) 11명, 박사과정(Ph.D Course) 13명, 모두 24명이다. 「시작」은 카드에 적힌 과정 시작 연월이고, 「연구 주제」는 카드의 Research interest 칸이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 이형석 | 석사과정 | 2026.09 |  |  |
| 이예진 | 석사과정 | 2026.09 |  |  |
| 류원우 | 석사과정 | 2026.03 |  |  |
| Yong Lin Yap | 석사과정 | 2026.03 |  |  |
| Jetniphat Boonyanuson | 석사과정 | 2025.09 |  |  |
| 한승민 | 석사과정 | 2025.09 | Low Earth Orbit Analysis / Constellation Design & Control |  |
| 장재형 | 석사과정 | 2025.09 | Spacecraft trajectory optimization |  |
| 김강면 | 석사과정 | 2025.03 | Orbital trajectory design / Proximity operation for rendezvous |  |
| 김정원 | 석사과정 | 2025.03 | Spacecraft Attitude Optimization / Control Moment Gyros |  |
| 이윤강 | 석사과정 | 2025.03 | Spacecraft task scheduling |  |
| 남윤호 | 석사과정 | 2025.03 | Spacecraft trajectory optimization |  |
| 이진 | 박사과정 | 2026.09 | Attitude profile optimization |  |
| 손보연 | 박사과정 | 2026.09 | Optimal trajectory design / Space mission design with deep learning |  |
| 장은진 | 박사과정 | 2026.03 |  |  |
| 이인구 | 박사과정 | 2026.03 | Optimal trajectory design |  |
| 정유진 | 박사과정 | 2026.03 | Optimal trajectory design / Space mission design with deep learning |  |
| 김윤중 | 박사과정 | 2026.03 | Deep Space Mission Design / Convex Optimization / Quantum Computing |  |
| 김병준 | 박사과정 | 2025.09 | Space robotics trajectory optimization |  |
| 변승현 | 박사과정 | 2025.09 |  |  |
| 이지원 | 박사과정 | 2025.03 | Satellite attitude optimization | 2, 3 |
| 임정우 | 박사과정 | 2025.03 | Space mission and trajectory optimization | 4 |
| 신영균 | 박사과정 | 2025.03 | Rendezvous & docking mission and trajectory guidance / Continuous thrust-based optimal trajectory design |  |
| 이윤일 | 박사과정 | 2024.09 | Spacecraft attitude control & optimization / Optimal landing trajectory design |  |
| 임경선 | 박사과정 | 2024.09 |  | 3, 4 |

## 최근 논문 목록 (2021–2026)

두 자료를 합친 목록이다. 하나는 출판사 등록 서지(Crossref)에 이동헌 교수가 저자로 오른 2021–2026년 학술지 논문 19편과 학회 논문 1편이고(저자·제목·학술지 표기와 연도는 출판사 서지 기준), 다른 하나는 누리집 Conference 게시판이 2022–2025년 국내·국제 학술대회 발표로 적은 60건이다(저자·제목·학술대회 표기는 게시판 그대로).[^cr][^conf] 누리집 Journal 게시판에는 학술지 논문 목록이 올라 있지 않다.[^journal] 교수는 2024년 1월 KAIST에 부임했으므로, 2021–2023년 항목은 교수가 한국항공우주연구원(2021년 2월까지)과 한국항공대학교(2021년 3월–2023년 12월)에 있던 시기의 논문과 학회 발표다.[^prof]

**2026**

- Yunkang Lee and Donghun Lee. "Attitude profile design for TDI imaging under constant line-rate constraint". *Advances in Space Research (doi:10.1016/j.asr.2026.08.006)*.
- Young-Joo Song, Donghun Lee, and Jooho Park. "Centralizing Korea's space governance: Institutional impacts and strategic implications one year after launching KASA". *Space Policy (doi:10.1016/j.spacepol.2026.101748)*.
- Seunghyeon Byeon, Kyeongsun Lim, and Donghun Lee. "Development of an Omnidirectional-Wheel-Based Hardware Simulator for Preliminary Integrated Verification of Autonomous Rendezvous and Proximity Operation Algorithms". *Journal of Aerospace System Engineering (doi:10.20910/jase.2026.20.7.24)*.
- Byungjun Kim, Kyeongsun Lim, Chungwon Kim, Seunghyeon Byeon, and Donghun Lee. "Dynamics Verification of a Free-Floating Dual-Arm Robotic Satellite". *Journal of Aerospace System Engineering (doi:10.20910/jase.2026.20.8.56)*.
- Seunghyeon Byeon, Byungjun Kim, Gunho Park, Jiwon Lee, Kyeongsun Lim, Taehun Kim, Yoonhyuk Choi, and Donghun Lee. "Efficient Attitude Command Reconstruction Algorithm for Satellites Operations". *International Journal of Aeronautical and Space Sciences (doi:10.1007/s42405-026-01245-0)*.
- Young-Joo Song, Donghun Lee, and Yoonhyuk Choi. "Lunar mission trajectories and orbits: A comprehensive phase-by-phase survey based on real-flight operations". *Acta Astronautica (doi:10.1016/j.actaastro.2026.02.047)*.
- Young-Joo Song, Donghun Lee, and Moon-Jin Jeon. "Orbit Design of Multiple Lunar CubeSat Impactors Deployed from a Single Mothership: A Practical Approach for Mission Feasibility". *International Journal of Aeronautical and Space Sciences (doi:10.1007/s42405-025-01121-3)*.
- Byungjun Kim, Jeongwoo Lim, Seunghyeon Byeon, Gunho Park, Taehun Kim, Yoonhyuk Choi, Kyeongsun Lim, and Donghun Lee. "PSO-Based Two-Step Path Planning for a Dual-Arm Free-Floating Robotic Satellite". *International Journal of Aeronautical and Space Sciences (doi:10.1007/s42405-026-01187-7)*.
- Jiwon Lee, Yoon Ill Lee, Yujin Jeong, and Donghun Lee. "Time-Optimal Spin-to-Spin Slew Maneuver With Angular Velocity Constraints via Sequential Convex Programming". *AIAA SCITECH 2026 Forum (doi:10.2514/6.2026-2536)*.

**2025**

- 남윤호, 임정우, 이동헌. "2041년~2046년 지구-화성 발사 기회 분석". *한국추진공학회 2025년도 춘계학술대회 (국내 학회 발표)*.
- 문신혜, 이동헌. "3축 Spin-to-Spin 기동 위성의 시간 최적화 해석적 자세명령 생성 기법". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이윤일, 이지원, 이진, 이동헌. "3축, Spin-to-spin 회전 기동의 근사적 최소 시간 분석". *한국항공우주학회 2025년도 우주학술대회 (국내 학회 발표)*.
- 남윤호, 임정우, 조남경, 이동헌. "GMAT을 활용한 원자력 열추진 화성 탐사 3차원 궤도 설계 및 분석". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이진, 이지원, 이윤일, 이동헌. "GPOPS를 사용한 초기 각속도 조건에 따른 3축 Spin-to-spin 기동 시간 분석". *한국항공우주학회 2025년도 우주학술대회 (국내 학회 발표)*.
- 임경선, 이동헌. "MLP를 이용한 비여분 CMG Cluster의 Gimbal 궤적 생성 기법". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이윤일, 이지원, 이진, 이동헌. "Spin-to-spin 경계조건을 고려한 작은 각 회전 기동의 기동 시간 근사화". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이윤강, 이동헌. "TDI 카메라의 일정 Line Rate 유지를 위한 Bezier 곡선 기반 자세 계획". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 임정우, 이동헌. "가시선 제한 하 최소 연료 V-bar 근접 기동 궤적의 기하학적 분석". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 김정원, 이동헌. "가위쌍 구조 적용 정육면체형 CMG 배치 활용 최소 시간 자세 기동 궤적". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이진, 이동헌. "각가속도의 박스 제한 조건을 고려한 위성의 최소 시간 기동 스위칭 타임 결정". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이인구, 남윤호, 정유진, 이동헌. "고충실도 역학 기반 GTO-GEO 저추력 최적 천이 궤적 설계". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 손보연, 정유진, 이동헌. "교대 최적화 스케줄링을 통한 물리 정보 신경망(PINN) 기반 램버트 솔버의 성능 향상". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이지원, 이윤일, 이동헌. "구형 각가속도 제한을 고려한 spin-to-spin 회전의 시간 최적 자세 프로파일 생성: Sequential convex programming 기반 접근". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 김강면, 신영균, 이동헌. "도킹 단계 랑데부 접근을 위한 Teardrop Hovering 근접 기동". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 김강면, 남윤호, 이동헌. "도킹 단계 랑데부 접근을 위한 근접 기동(Hovering)". *2025년 공군사관학교 미래 항공우주 학술대회 (국내 학회 발표)*.
- 정유진, 손보연, 이동헌. "램버트 문제 해결을 위한 TFC 보간 기반 물리 정보 신경망 프레임워크". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 김윤중, 이동헌. "베이지안 최적화를 이용한 Gravity-Assist 기반 지구-화성 전이 임무 설계". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 이윤일, 이동헌. "우주비행체의 자세 제어 추력기의 특성을 고려한 6DOF 추력 분배 시뮬레이션". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 남윤호, 임정우, 이동헌. "원자력 열추진을 이용한 화성탐사 임무분석". *한국추진공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 김정원, 이동헌. "정육면체형 SGCMG 배치에의 가위쌍 구조 적용 효과". *항공우주시스템공학회 2025년도 추계학술대회 (국내 학회 발표)*.
- 남윤호, 임정우, 이동헌. "해석적인 방법을 활용한 지구-화성 탐사 총 궤적 설계". *한국항공우주학회 2025년도 추계학술대회 (국내 학회 발표)*.
- Lee, Ingu, Jeong, Yujin, and Lee, Donghun. "Arctangent smoothing method for optimal bang-bang control problem". *2025 AAS/AIAA Space Flight Mechanics Meeting (국제 학회 발표)*.
- Lim, Kyeong-sun, and Lee, Donghun. "Deep Learning Based Approach to Preferred Gimbal Angle Set Prediction in Nonredundant CMG Clusters". *2025 Asia-Pacific International Symposium on Aerospace Technology (국제 학회 발표)*.
- Lim, Jeongwoo, and Lee, Donghun. "Linear programming for a fixed-time v-bar glideslope under los constraints". *2025 AAS/AIAA Astrodynamics Specialist Conference (국제 학회 발표)*.
- Lee, Yoon Ill, Lee, Jiwon, Lee, Jin, and Lee, Donghun. "Minimum Time Approximation Analysis of a 3-axis, Spin-to-spin Slew Maneuver". *2025 Asia-Pacific International Symposium on Aerospace Technolgy (국제 학회 발표)*.
- Lee, Yoon Ill, Lee, Jiwon, Lee, Jin, and Lee, Donghun. "Minimum Time Trade-off Study for a Spacecraft’s Three-axis Spin-to-spin Slew Maneuver". *The 25th International Conference on Control, Automation, and Systems (국제 학회 발표)*.
- Shin, Youngkyun, and Lee, Donghun. "Natural Motion Cirumnavigation-Based Trajectory Design for Active Debris Removal with Arbitrary Docking Axis Approach". *2025 Asia-Pacific International Symposium on Aerospace Technolgy (국제 학회 발표)*.
- Shin, Youngkyun, and Lee, Donghun. "Polynomial Regression Approach for Solving Coplanar Orbit Transfer Problems". *2025 Asia-Pacific International Symposium on Aerospace Technolgy (국제 학회 발표)*.
- Lim, Kyeong-sun, and Lee, Donghun. "Prediction and Evaluation of Preferred Gimbal Angle Using Multi-Layer Perceptron in Nonredundant CMG Cluster". *The 25th International Conference on Control, Automation, and Systems (국제 학회 발표)*.
- Jiwon Lee and Donghun Lee. "Closed-Form Solution for the Absolute Effort Minimization Problem for Single-Axis, Spin-to-Spin Slew Maneuvers". *International Journal of Aeronautical and Space Sciences (doi:10.1007/s42405-025-00942-6)*.
- Jooho Park, Young-Joo Song, and Donghun Lee. "Enhanced Test Data Management in Spacecraft Ground Testing: A Practical Approach for Centralized Storage and Automated Processing". *Aerospace (doi:10.3390/aerospace12090813)*.

**2024**

- 신영균, 임정우, 이동헌. "Hill’s Equation 기반 순간 추력의 연속 추력기를 이용한 접근 기동". *항공우주학회 2024년도 춘계학술대회 (국내 학회 발표)*.
- 이진, 이동헌. "각속도의 다항식 회귀를 사용한 최적 자세 프로파일 생성". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 변승현, 임경선, 이동헌. "두 종류의 전방향 모바일 로봇의 궤적 추종 및 자세 제어 실험". *항공우주학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 김병준, 임경선, 이윤일, 신영균, 이동헌. "로봇 팔 역학 시뮬레이션의 계산시간 비교". *항공우주시스템공학회 2024년도 춘계학술대회 (국내 학회 발표)*.
- 김은솔, 이동헌. "배틴의 램버트 알고리즘을 사용한 지구-화성 전이 궤적". *항공우주학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 임정우, 신영균, 이동헌. "상태 천이 행렬을 통한 순간 추력 기반의 근접기동 분석". *항공우주학회 2024년도 춘계학술대회 (국내 학회 발표)*.
- 이인구, 정유진, 이동헌. "슈팅 방법을 이용한 지구-아포피스 저추력 최소 연료 천이 궤적 설계". *항공우주학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 이윤일, 이동헌. "우주 비행체의 자세제어를 위한 2차원 추력 분배 시뮬레이션". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 문신혜, 김태석, 이동헌. "위성 자세 기동 명령의 효율적 업로드를 위한 재구성 알고리즘". *항공우주학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 김병준, 이동헌. "이중 로봇 팔 장착 위성 역학 시뮬레이션". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 임경선, 변승현, 이동헌. "자동 랑데부/도킹 유도 알고리즘을 위한 하드웨어 시뮬레이터 설계 및 제작". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 변승현, 박건호, 김병준, 이동헌. "자세 명령 프로파일 재구성 탑재 소프트웨어 개발". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 신영균, 이동헌. "장시간 J2 섭동 기동을 통한 궤도면 일치 임무 설계 분석". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 남윤호, 이인구, 이동헌. "저추력을 이용한 지구-화성 천이 에너지 및 연료 최적 궤도 설계". *항공우주학회 2024년도 추계학술대회 (국내 학회 발표)*.
- 정유진, 이인구, 이동헌. "좌표계 정의에 따른 저추력기를 이용한 지구-화성 최적 에너지 천이 궤적 비교". *항공우주시스템공학회 2024년도 추계학술대회 (국내 학회 발표)*.
- Lim, Jeongwoo, and Lee, Donghun. "Line-of-sight constrained fuel-optimal V-bar glideslope guidance algorithm for proximity operation". *APISAT 2024 (국제 학회 발표)*.

**2023**

- 이윤일, 이동헌. "GPOPS를 이용한 연료 최적의 궤적 설계 연구". *항공우주시스템공학회 2023년도 춘계학술대회 (국내 학회 발표)*.
- 변승현, 임경선, 이동헌. "메카넘휠을 장착한 모바일 로봇의 궤적 추종 제어 시뮬레이션". *항공우주시스템공학회 2023년도 춘계학술대회 (국내 학회 발표)*.
- 임경선, 박동연, 김귀만, 신영균, 이윤일, 임정우, 변승현, 우지연, 이현주, 이지수, 성상경, 이상철, 이동헌. "자동 랑데부/도킹 임무를 위한 유도항법제어 기술 조사". *항공우주학회 제1회 우주학술대회 (국내 학회 발표)*.
- 신영균, 이동헌. "최적화 파라미터 근사해를 이용한 궤도 천이 전략 연구". *항공우주시스템공학회 2023년도 춘계학술대회 (국내 학회 발표)*.
- 이지원, 이동헌. "최종시간 제한조건을 고려한 1축 회전 기동의 자세제어 프로파일 연구". *항공우주시스템공학회 2023년도 춘계학술대회 (국내 학회 발표)*.
- 임정우, 이동헌. "추력 최소화를 위한 램버트 문제 기반의 저궤도 위성 궤도 천이 연구". *항공우주시스템공학회 2023년도 춘계학술대회 (국내 학회 발표)*.
- Donghun Lee and Young-Joo Song. "Closed-Form Solutions for Single-Axis Slew Maneuvers Under a Fixed Final Time Constraint". *International Journal of Aeronautical and Space Sciences (doi:10.1007/s42405-023-00682-5)*.
- Sung-Hoon Mok, Hyochoong Bang, and Donghun Lee. "Closed-form solution of attitude command generation for spin-to-spin maneuver". *Advances in Space Research (doi:10.1016/j.asr.2022.07.053)*.
- Young-Joo Song, Jonghee Bae, SeungBum Hong, Jun Bang, and Donghun Lee. "Post Trajectory Insertion Performance Analysis of Korea Pathfinder Lunar Orbiter Using SpaceX Falcon 9". *Journal of Astronomy and Space Sciences (doi:10.5140/jass.2023.40.3.123)*.
- Jun Bang, SeungBum Hong, Jonghee Bae, Young-Joo Song, and Donghun Lee. "Preparation of Contingency Trajectory Operation for the Korea Pathfinder Lunar Orbiter". *Journal of Astronomy and Space Sciences (doi:10.5140/jass.2023.40.4.217)*.

**2022**

- 이지원, 변승현, 임정우. "1축 자세 제어 시스템 설계 및 파라미터 추정". *항공우주학회 2022년도 추계학술대회 (국내 학회 발표)*.
- 이지원, 이동헌. "각속도 제한을 고려한 일축-회전 기동". *항공우주시스템공학회 2022년도 춘계학술대회 (국내 학회 발표)*.
- 임경선, 이동헌. "구형 가속도 제한 조건을 고려한 최소 시간 자세 제어 문제". *항공우주시스템공학회 2022년도 춘계학술대회 (국내 학회 발표)*.
- 신영균, 이동헌. "궤도요소 변화에 따른 위성간 상대운동 분석". *항공우주학회 2022년도 추계학술대회 (국내 학회 발표)*.
- 이동헌, 신영균. "랑데부-도킹 임무 해석을 위한 궤도 전파기 설계". *항공우주시스템공학회 2022년 추계학술대회 (국내 학회 발표)*.
- 금준섭, 이동헌. "오픈 소스 최적화 프로그램을 이용한 2차원 착륙 궤적 최적화". *항공우주시스템공학회 2022년도 춘계학술대회 (국내 학회 발표)*.
- 이윤일, 이지원, 이동헌. "추력 분배 기법을 적용한 2차원 자세제어 시뮬레이션". *항공우주학회 2022년도 추계학술대회 (국내 학회 발표)*.
- 정민조, 이동헌. "혼합정수선형계획법을 이용한 군집 드론의 최적 경로 지정 연구". *항공우주시스템공학회 2022년도 춘계학술대회 (국내 학회 발표)*.

**2021**

- SungTae Moon, Donghun Lee, Dongoo Lee, Doyoon Kim, and Hyochoong Bang. "Energy-Efficient Swarming Flight Formation Transitions Using the Improved Fair Hungarian Algorithm". *Sensors (doi:10.3390/s21041260)*.
- Donghun Lee and Young-Joo Song. "Influence of Steering Angle Profiles on the Orbit Transfer Trajectory". *Mathematical Problems in Engineering (doi:10.1155/2021/2648585)*.
- Young-Joo Song, Young-Rok Kim, Jonghee Bae, Jae-ik Park, Seungbum Hong, Donghun Lee, and Dae-Kwan Kim. "Overview of the Flight Dynamics Subsystem for Korea Pathfinder Lunar Orbiter Mission". *Aerospace (doi:10.3390/aerospace8080222)*.
- Young-Joo Song, Donghun Lee, Young-Rok Kim, Jonghee Bae, Jae-ik Park, SeungBum Hong, Dae-Kwan Kim, and Sang-Ryool Lee. "Practical Algorithms on Lunar Reference Frame Transformations for Korea Pathfinder Lunar Orbiter Flight Operation". *Journal of Astronomy and Space Sciences (doi:10.5140/jass.2021.38.3.185)*.
- Young-Joo Song and Donghun Lee. "Preliminary Analysis on Launch Opportunities for Sun-Earth Lagrange Points Mission from NARO Space Center". *Journal of Astronomy and Space Sciences (doi:10.5140/jass.2021.38.2.145)*.

## 연구 과제

누리집 Research Project 게시판의 진행 중 과제(Current Project)다.[^project]

- 행성 간 탐사 임무를 위한 궤적설계 기술 연구 (기간 24-01-01~26-12-31; 지원 한국과학기술원; 상태 Current Project)

## 수상

누리집 News 게시판의 수상 글이다. 날짜는 글의 게시일이며, 2025-04-28 글은 항공우주시스템공학회 2024년도 추계학술대회의 수상을 알린다.[^news][^award13][^award12][^iccas][^award8]

- 2025-12-16 · 이지원 박사과정, 항공우주시스템공학회 2025년도 추계학술대회 우수발표논문상 수상
- 2025-12-05 · 김강면 석사과정, 2025년 미래 항공우주 학술대회 우수상 수상
- 2025-12-01 · 임경선 박사과정, ICCAS Outstanding Student Paper Award 수상
- 2025-04-28 · 이윤일 박사과정, 항공우주시스템공학회 2024년도 추계학술대회 우수발표논문상 수상

## 소식

누리집 News 게시판의 수상 글이 아닌 글이다. 2025년 7월 21일 University of Cincinnati 김동훈 교수를 초청해 「우주비행체 유도 및 제어 연구 동향」을 주제로 세미나를 열었고, 강연은 On-orbit Servicing(궤도상 서비스)과 궤도 제어 기법의 최신 연구 동향을 중심으로 진행됐다.[^seminar]

- 2025-07-23 · University of Cincinnati 김동훈 교수님 초청 세미나 개최

## 연락과 위치

- 교수 연구실: N7-2 #2307[^aefac][^home]
- 학생 연구실: N7-5 #509[^home]
- 교수 전화: 042-350-3717[^aefac][^aelab][^prof], 팩스 +82-42-350-3710[^prof]
- 교수 이메일: donghlee@kaist.ac.kr[^aefac][^aelab]
- 주소: 34141 대전광역시 유성구 대학로 291 KAIST 항공우주공학과[^home]
[^p1]: Y.-J. Song, D. Lee, M.-J. Jeon, International Journal of Aeronautical and Space Sciences 27, 3751-3765 (온라인 2026-01-13). <https://doi.org/10.1007/s42405-025-01121-3> 초록 기준.
[^p2]: J. Lee, D. Lee, International Journal of Aeronautical and Space Sciences 26, 2768-2784 (온라인 2025-04-10). <https://doi.org/10.1007/s42405-025-00942-6> 초록 기준(Springer 논문 페이지 게시 초록).
[^p3]: S. Byeon 외, D. Lee, International Journal of Aeronautical and Space Sciences (온라인 2026-07-29). <https://doi.org/10.1007/s42405-026-01245-0> 초록 기준.
[^p4]: B. Kim 외, D. Lee, International Journal of Aeronautical and Space Sciences (온라인 2026-05-19). <https://doi.org/10.1007/s42405-026-01187-7> 초록 기준(Springer 논문 페이지 게시 초록).
[^p5]: J. Park, Y.-J. Song, D. Lee, Aerospace 12, 813 (온라인 2025-09-09). <https://doi.org/10.3390/aerospace12090813> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://smcl.kaist.ac.kr/> (OUR RESEARCH, LATEST NEWS, CONTACT US, 바닥글 주소, 2026-10-23 열람)
[^mission]: 연구실 누리집 Research Topic 페이지 「Interplanetary Mission Design and Analysis」 <https://smcl.kaist.ac.kr/sub2_1_a.php> (2026-10-23 열람)
[^attitude]: 연구실 누리집 Research Topic 페이지 「Spacecraft Attitude Guidance and Control」 <https://smcl.kaist.ac.kr/sub2_1_b.php> (2026-10-23 열람)
[^rdv]: 연구실 누리집 Research Topic 페이지 「Guidance and Control Algorithms for Space Rendezvous and Docking System」 <https://smcl.kaist.ac.kr/sub2_1_c.php> (A. 랑데부 도킹 궤도 유도 알고리즘, B. 지상 시뮬레이터 장치 관련, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 게시판 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (전화, 이메일, 팩스, Experience, Education, 2026-10-23 열람)
[^members]: 연구실 누리집 Current Member 게시판 1·2쪽 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub1_2>, <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub1_2&page=2> (Total 24건, 2026-10-23 열람)
[^project]: 연구실 누리집 Research Project 게시판 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub2_2> (2026-10-23 열람)
[^journal]: 연구실 누리집 Publication > Journal 게시판 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_1> (2026-10-23 열람)
[^conf]: 연구실 누리집 Publication > Conference 게시판 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2>와 글 6건 「2025 국내 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=10>, 「2025 국제 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=7>, 「2024 국제 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=4>, 「2024 국내 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=3>, 「2023 국내 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=2>, 「2022 국내 학술 대회」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&wr_id=1> (2026-10-23 열람)
[^news]: 연구실 누리집 Board > News 게시판 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1> (Total 5건, 2026-10-23 열람)
[^award13]: 연구실 누리집 News 글 「이지원 박사과정, 항공우주시스템공학회 2025년도 추계학술대회 우수발표논문상 수상」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=13> (2025-12-16 게시, 2026-10-23 열람)
[^award12]: 연구실 누리집 News 글 「김강면 석사과정, 2025년 미래 항공우주 학술대회 우수상 수상」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=12> (2025-12-05 게시, 2026-10-23 열람)
[^iccas]: 연구실 누리집 News 글 「임경선 박사과정, ICCAS Outstanding Student Paper Award 수상」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=11> (2025-12-01 게시, 2026-10-23 열람)
[^award8]: 연구실 누리집 News 글 「이윤일 박사과정, 항공우주시스템공학회 2024년도 추계학술대회 우수발표논문상 수상」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=8> (2025-04-28 게시, 2026-10-23 열람)
[^seminar]: 연구실 누리집 News 글 「University of Cincinnati 김동훈 교수님 초청 세미나 개최」 <https://smcl.kaist.ac.kr/bbs/board.php?bo_table=sub4_1&wr_id=10> (2025-07-23 게시, 2026-10-23 열람)
[^aelab]: KAIST 항공우주공학과 연구실 소개 「Spaceflight Mission and Control Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/13329> (연구실명, 교수, 연구실 소개, 웹사이트, 이메일, Tel, Office, 연구분야, 2024-05-14 게시, 2026-10-23 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (이동헌 항목의 직위, Career, Tel, Website, E-mail, 연구분야, 연구실, 2026-10-23 열람)
[^cr]: 2021–2026년 논문과 대표 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (교수 확인 기준은 근거 페이지, 2026-10-23 조회)

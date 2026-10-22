# 로봇 제어 & 설계 연구실 (Dynamic Robot Control & Design Lab, DRCD Lab)

**KAIST 기계공학과 · 박해원 교수**

- 분야: 4족 보행 로봇과 휴머노이드의 동적 보행, 강화학습과 생성 모델을 쓴 보행 제어, 모델 예측 제어와 궤적 최적화, 로봇 구동기와 감속 기구·자석 발 설계, 다리 로봇의 상태 추정과 마찰 계수 식별
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 보행·휴머노이드 로봇[^home][^robots][^p1], 강화학습[^control][^p1][^p2], 제어 이론·제어 공학[^people][^control][^p4], 로봇 구동기·센서[^hw][^p6], 로봇 항법·SLAM[^est][^p7]
- 홈페이지: <https://www.dynamicrobot.kaist.ac.kr/>
- 근거와 출처: [로봇 제어 & 설계 연구실 근거 페이지](dynamicrobot-sources.md)

> 다리로 걷고 뛰는 로봇을 직접 설계해 만들고, 그 로봇이 험한 지형이나 벽과 천장 위에서도 빠르고 안정적으로 움직이도록 제어하는 기계공학과 연구실이다. 모델 예측 제어 같은 최적화 기반 제어와 강화학습을 함께 쓰고, 4족 보행 로봇 HOUND, 벽을 오르는 4족 로봇 MARVEL, 휴머노이드를 만든다.[^home][^people][^robots]

## 무엇을 연구하나

연구실 첫 화면은 연구실 이름을 "Dynamic Robot Control & Design Lab"으로 적고, 한계를 넘어서는 로봇을 만든다는 목표 아래 동적 하드웨어 설계, 민첩한 제어, 지능형 보행을 연구한다고 소개한다.[^home] 첫 화면은 이를 새로운 구동 방식, 동적 제어, 학습 기반 이동 능력을 하나로 묶는 일로 설명하고, 험한 자연 지형에서의 4족 보행(네 다리로 걷고 뛰는 이동), 강자성 표면에서 벽을 오르는 동적 제어, 구동 장치와 모델 기반 제어와 학습 기반 지능을 결합한 차세대 하드웨어를 대표 연구로 든다.[^home]

PEOPLE 페이지에 적힌 교수의 연구 관심은 다리 로봇의 최적화 기반 제어와 설계, 모델 예측 제어(MPC, Model Predictive Control, 로봇의 동역학 모형으로 가까운 미래의 움직임을 예측해 매 순간 가장 알맞은 입력을 계산하는 제어 방법), 생체모사 로봇(동물의 몸 구조나 움직임을 본떠 만든 로봇)이다.[^people] 기계공학과 교수 소개는 연구 분야를 동적 로봇 시스템의 제어와 설계, 다리로 이동하는 보행 로봇, 생체모사 로봇으로 적는다.[^meprof]

누리집 RESEARCH 메뉴는 연구를 제어(CONTROL), 하드웨어 설계(HARDWARE-DESIGN), 추정(ESTIMATION)의 세 갈래로 나누고, 제어 갈래를 다시 학습 기반 제어와 모델 기반 제어로 나눠 각 연구와 논문을 소개한다.[^control][^hw][^est] ROBOTS 페이지는 연구실이 만든 로봇으로 동적 보행용 실물 크기 휴머노이드 KAIST Humanoid, 4족 보행 로봇 HOUND 1과 HOUND 2, 벽을 오르는 4족 로봇 MARVEL을 소개한다.[^robots] 하드웨어 페이지는 연구실이 개발한 이론을 모두 실제 로봇으로 실험하며, 이를 위해 로봇 플랫폼을 처음부터 직접 만든다고 적는다.[^hw]

## 주요 연구 주제

### 1. 학습 기반 보행 제어

강화학습(시행착오를 거치며 보상이 커지는 행동을 스스로 배우는 기계학습 방법)과 생성 모델로 다리 로봇의 움직임을 배우게 한다. 제어 페이지는 미분 가능한 시뮬레이터(입력을 조금 바꿨을 때 결과가 얼마나 바뀌는지를 함께 계산할 수 있는 물리 시뮬레이터)를 흐름 정합(flow matching, 잡음에서 원하는 데이터로 옮겨 가는 경로를 배워 새 데이터를 만드는 생성 모델 학습 방법)에 넣어, 상태만 담긴 시연 자료에서 물리적으로 실현 가능한 동작 궤적을 만드는 DynaFlow(ICRA 2026)를 소개한다.[^control] 같은 페이지는 모델 기반 제어기에 학습한 잔차 모듈(모형이 실제와 어긋나 생기는 차이를 메우도록 따로 학습한 보정 부분)을 붙여 불확실성에 강하게 만든 틀(RA-L 2025), 장벽 함수(값이 허용 범위의 경계에 가까워질수록 커지도록 만든 함수) 형태의 보상으로 걸음새와 자세를 이끌어 한 로봇이 4족·3족·2족 걸음을 모두 하게 만든 강화학습 틀(ICRA 2025), 모터의 토크–속도 한계를 학습에 넣어 고속으로 달리게 한 연구(R-AM 2024)를 든다.[^control] 장벽 함수 보상 연구는 4족 모드에서 4.67 m/s로 달리고 높이 최대 58 cm의 장애물을 넘었으며, 2족 모드에서 3.6 m/s로 달리고 7.5 kg 물체를 나르며 계단을 올랐다고 적는다.[^control] 대표 논문 1은 단순화한 동역학 모형으로 만든 움직임 자료로 여러 보행 기술을 미리 배운 뒤 강화학습으로 다듬어, 4족 로봇이 탑재 센서만으로 지형에 맞게 걸음새를 골라 바꾸게 했다.[^p1] 대표 논문 2, 3.[^p2][^p3]

### 2. 모델 기반 제어와 최적화

로봇의 동역학 모형을 바탕으로 최적화 문제를 풀어 움직임과 발 디딤을 정한다. 제어 페이지는 접촉점마다 병진 동역학을 나눠 다루는 궤적 최적화(로봇이 따라갈 움직임 경로를 비용이 최소가 되도록 계산하는 방법) 연구(RA-L 2026), 접촉 순서나 궤적을 미리 정하지 않고 여러 접촉 동작을 실시간으로 찾아내는 접촉 암묵적 모델 예측 제어(IROS 2022, IJRR 2024), 회전군 SO(3)(3차원 공간의 회전을 모두 모은 수학적 집합) 위에서 정식화한 비선형·선형 모델 예측 제어, 장애물을 뛰어넘는 동작의 온라인 최적화, 희소 행렬(대부분의 원소가 0인 행렬)의 구조를 이용해 최적화 문제를 빠르게 푸는 풀이기를 소개한다.[^control] 이 가운데 SO(3) 위의 비선형 모델 예측 제어 논문은 IROS 2020에서 Best RoboCup Paper Award를 받았다고 적는다.[^control][^news] 대표 논문 4는 접촉 순간의 충격을 다루는 상보성 조건(두 물체가 닿아 있을 때만 접촉력이 생기도록 묶는 수학적 조건)을 완화해 매끄러운 기울기를 얻고, 45 kg의 4족 로봇 HOUND에서 접촉 순서를 미리 정하지 않은 앞다리 들기 같은 동작을 실험했다.[^p4] 대표 논문 4.

### 3. 로봇 하드웨어와 구동기 설계

다리 로봇의 몸체와 구동기(모터와 감속 기구처럼 관절을 움직이는 장치)를 최적화로 설계해 직접 만든다. 하드웨어 페이지는 전영구 자석(전류를 잠깐 흘려 자력을 켜고 끄며, 켠 뒤에는 전력 없이도 자력을 유지하는 자석) 발과 자기유변 탄성체(자기장에 따라 강성이 바뀌는 탄성 고분자 소재)로 강자성 벽과 천장을 오르는 4족 로봇 MARVEL(Science Robotics 2022 표지 논문), 멈춤쇠 기구로 유성 기어(가운데 기어 둘레를 여러 기어가 돌며 회전 속도를 줄이는 기어 장치)의 고정 부품을 바꿔 감속비 6.91과 44.93을 오가는 관절 구동기(IROS 2022), 기어 잇수까지 혼합 정수 최적화(정수 변수와 연속 변수를 함께 다루는 최적화)로 정해 3 m/s 속보에 맞춘 4족 로봇 KAIST HOUND의 설계(ICRA 2022), 토크 제어 구동기 설계(IROS 2017)를 소개한다.[^hw] HOUND 1 페이지는 45 kg의 이 로봇이 2023년 10월 정지 상태에서 출발해 100 m를 19.87초에 달려 가장 빠른 4족 로봇 기네스 세계 기록을 세웠고, 이때 강화학습으로만 학습한 제어기 하나를 썼다고 적는다.[^hound1] HOUND 2 페이지는 모터, 모터 구동기, 기어, 통신 모듈을 연구실이 직접 설계해 만들었다고 적는다.[^hound2] 대표 논문 5는 MARVEL을, 대표 논문 6은 기름 관을 몸체 속에 넣은 유압 4족 로봇 LIGHTDOG을 다룬다.[^p5][^p6] 대표 논문 5, 6.

### 4. 상태 추정과 파라미터 식별

다리 로봇이 자기 위치·속도·자세를 스스로 알아내고(상태 추정), 바닥의 마찰 같은 환경 값을 찾아낸다(파라미터 식별). 추정 페이지는 다리 관절의 기구학 정보와 관성 측정 장치(IMU, 가속도와 회전 속도를 재는 센서), 라이다(레이저로 주변까지의 거리를 재는 센서), GPS를 불변 확장 칼만 필터(InEKF, 로봇 운동의 대칭 구조를 이용해 센서 값으로 상태를 차례로 고쳐 나가는 추정 방법)와 불변 평활기(Invariant Smoother, 일정 시간 동안 모인 측정값을 한꺼번에 써서 상태를 추정하는 방법)로 합쳐 높이 방향으로 위치 추정이 점점 어긋나는 문제를 줄이는 연구(RA-L 2025), 발이 미끄러지는 동적 접촉 사건을 걸러내는 상태 추정(RA-L 2021, T-RO 2023), 미끄러운 지형에서 마찰 계수를 실시간으로 찾는 연구(RA-L 2025)를 소개한다.[^est] 대표 논문 7은 불변 평활기로 상태를 추정하고 발 미끄러짐을 걸러냈으며, 대표 논문 8은 접촉 충격의 매끄러운 기울기로 마찰 계수를 찾았다.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

박해원 교수가 마지막 저자인 2021–2026년 학술지 논문 가운데 초록을 확인할 수 있는 여덟 편을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 연도는 출판사 서지의 출판 연도다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Agile perceptive multiskill locomotion for quadrupedal robots in the wild](https://doi.org/10.1126/scirobotics.adz7397) · Science Robotics | 4족 로봇이 험한 실외와 도시 환경을 지나려면 여러 운동 기술을 이어 쓰고 걸음새를 부드럽게 바꾸며, 탑재 센서만으로 빠르게 움직여야 한다. 이 논문은 단순화한 동역학으로 궤적 최적화를 풀어 2차원 움직임 자료를 대량으로 만들고, 이 자료로 여러 보행 기술을 미리 배운 뒤 강화학습으로 다듬는 APT-RL을 제안했다. 실제 4족 로봇이 실내 장애물과 실외 자연 환경을 지났고, 아래로 뛰어내리는 동작에서 순간 최고 속도가 최대 6 m/s였다. 탑재된 정책 하나로 계단, 허들, 징검돌, 틈, 쓰러진 나뭇가지를 넘었다.[^p1] | 1저자 J.-G. Kang(Jun-Gill Kang), 마지막 저자 박해원 (6명) |
| 2 | 2025 | [Reinforcement Learning for High-Speed Quadrupedal Locomotion With Motor Operating Region Constraints](https://doi.org/10.1109/mra.2024.3487322) · IEEE Robotics & Automation Magazine | 4족 로봇을 빠르게 달리게 하려고 강화학습에 구동기의 토크–속도 작동 영역을 넣었다. 실제로는 모터 한계 때문에 불가능한 상태 변화를 학습에서 줄였고, 보상을 설계해 네 다리에 모터 토크를 고르게 나눠 한 모터만 한계에 걸리는 병목을 줄였다. 학습한 정책으로 45 kg의 KAIST Hound가 최대 6.5 m/s로 달렸고, 초록은 이를 전기 모터 구동 4족 로봇 가운데 가장 빠른 속도라고 적는다.[^p2] | 1저자 Y.-H. Shin(Young-Ha Shin), 마지막 저자 박해원 (4명) |
| 3 | 2025 | [A Modular Residual Learning Framework to Enhance Model-Based Approach for Robust Locomotion](https://doi.org/10.1109/lra.2025.3592067) · IEEE Robotics and Automation Letters | 경험적으로 설계한 발 디딤 계획기와 동역학 모형에 각각 학습한 잔차 모듈을 붙여, 모형과 실제의 차이로 생기는 성능 저하를 메웠다. 모듈마다 알맞은 학습 방법을 골라, 불확실성이 큰 환경에서 제어 성능이 좋아지고 비교 방법보다 학습 효율도 높았다. 기준 제어기가 파라미터 조정에 덜 민감해지는 이점도 관찰했다. 모델 예측 제어와 결합해 실제 4족 로봇에서 균형을 유지하며 명령 속도를 따라갔다.[^p3] | 1저자 M.-G. Kim(Min-Gyu Kim), 마지막 저자 박해원 (4명) |
| 4 | 2025 | [Contact-implicit Model Predictive Control: Controlling diverse quadruped motions without pre-planned contact modes or trajectories](https://doi.org/10.1177/02783649241273645) · The International Journal of Robotics Research | 접촉 순서나 발 디딤 위치를 미리 정하지 않고 여러 접촉 동작을 실시간으로 찾아내는 모델 예측 제어다. 딱딱한 접촉 모형과 선형 상보성 제약을 묶은 미분 동적 계획법(DDP, 움직임 경로를 시간 순서대로 나눠 거꾸로 따라가며 개선하는 최적화 방법)을 쓰고, 완화한 상보성 제약으로 접촉 충격의 해석적 기울기를 구해 다양한 접촉 방식을 탐색하게 했다. 실제로 쓸 수 있는 걸음을 만들도록 발 궤적을 이끄는 비용 항을 넣었고, 불안정한 초기 시뮬레이션 문제는 다중 슈팅(multiple shooting, 구간을 나눠 각각 계산한 뒤 이어 붙이는 방법)으로 풀었다. 45 kg의 HOUND로 속보와 앞다리 들기 동작을 실험했다.[^p4] | 1저자 G. Kim(Gijeong Kim), 마지막 저자 박해원 (5명) |
| 5 | 2022 | [Agile and versatile climbing on ferromagnetic surfaces with a quadrupedal robot](https://doi.org/10.1126/scirobotics.add1017) · Science Robotics | 바닥, 벽, 천장을 빠르게 오가는 등반 로봇은 일할 수 있는 공간이 넓지만, 그동안 등반 속도와 동작이 제한적이었다. 이 논문은 강자성 환경에서 줄 없이 움직이는 4족 등반 로봇 MARVEL을 만들었다. 전영구 자석과 자기유변 탄성체를 결합한 발로 큰 흡착력과 마찰력을 얻고, 토크 제어 구동기와 등반에 맞춘 모델 예측 제어를 썼다. 천장에서 최대 초속 0.5 m(몸길이의 1.51배), 수직 벽에서 최대 초속 0.7 m(몸길이의 2.12배)로 움직였고, 폭 10 cm 틈과 높이 5 cm 장애물을 넘으며 바닥·벽·천장 사이를 옮겨 다녔다. 두께 최대 0.3 mm의 페인트와 녹, 먼지가 덮인 저장 탱크의 굽은 면도 올랐다.[^p5] | 1저자 S. Hong(Seungwoo Hong), 마지막 저자 박해원 (4명) |
| 6 | 2025 | [Design of LIGHTDOG: A high payload-to-weight, hose-less hydraulic quadrupedal robot](https://doi.org/10.1177/02783649251349225) · The International Journal of Robotics Research | 무게에 비해 출력이 크고 짐을 많이 지는, 토크 제어 유압 4족 로봇 LIGHTDOG을 설계했다. 유압 장치의 복잡성·무게·열 문제를 풀려고 생물의 혈관 구조에서 착안해 기름 관을 모두 로봇 몸속에 넣었고, 관절 안에도 기름 관을 넣을 수 있는 이중 날개 회전 구동기를 설계했다. 이 기름 관은 몸체를 작고 가볍게 할 뿐 아니라 열을 몸체 전체로 퍼뜨려 바깥 방열기 없이 식힌다. 구동기의 내부 누설과 마찰 토크를 줄이는 구조를 넣고 크랭크 기구와 구동기 크기를 최적화했다. 45 kg의 LIGHTDOG은 쪼그리는 동작에서 130 kg의 짐을 들었다.[^p6] | 1저자 S. Shin(Seunghoon Shin), 마지막 저자 박해원 (5명) |
| 7 | 2024 | [Invariant Smoother for Legged Robot State Estimation With Dynamic Contact Event Information](https://doi.org/10.1109/tro.2023.3328202) · IEEE Transactions on Robotics | 관성 측정 장치와 다리 기구학 측정으로 다리 로봇의 상태를 추정하는 불변 평활기를 제안했다. 로봇 운동의 대칭 구조를 이용하는 형태(군 아핀 성질)로 잔차 함수를 세워 야코비 행렬(입력 변화가 출력에 주는 영향을 모은 행렬)이 현재 추정값에 기대지 않게 했고, 그 덕분에 발이 미끄러지는 동적 접촉 사건에서도 수렴이 좋아졌다. 동적 접촉 사건이 생기면 발이 땅에 붙어 있다는 가정의 불확실성을 키워 미끄러짐을 걸러내고, 안정적으로 디딘 동안 발 위치가 여러 시간 단계에 걸쳐 그대로라는 측정 모형도 더했다. 실내 실험과 160 m 실외 실험으로 최신 알고리즘들과 비교했다.[^p7] | 1저자 Z. Yoon(Ziwon Yoon), 마지막 저자 박해원 (3명) |
| 8 | 2025 | [Online Friction Coefficient Identification for Legged Robots on Slippery Terrain Using Smoothed Contact Gradients](https://doi.org/10.1109/lra.2025.3541428) · IEEE Robotics and Automation Letters | 미끄러운 지형에서 다리 로봇이 바닥의 마찰 계수를 실시간으로 찾는 방법이다. 마찰 계수에 따라 달라지는 예측 상태와 실제 상태의 차이를 최소화하도록 문제를 세우고, 쿨롱 마찰의 상보성 조건을 매끄럽게 만든 접촉 충격의 해석적 기울기로 매끄럽지 않은 접촉 동역학 때문에 기울기가 정보를 주지 못하는 문제를 풀었다. 발이 닿는 순간 수직 접촉 속도가 큰 자료는 걸러냈다. KAIST HOUND로 미끄러운 지형과 미끄럽지 않은 지형에서 실험해, 여러 초기 조건에서 빠르고 일관되게 마찰 계수를 찾았다.[^p8] | 1저자 H. Kim(Hajun Kim), 마지막 저자 박해원 (5명) |

## 교수와 전문 분야

박해원 교수는 KAIST 기계공학과 부교수다.[^people][^meprof] PEOPLE 페이지의 경력에 따르면 2019년 2월 KAIST 기계공학과 조교수로 부임했고 2022년 2월부터 부교수이며, 2020년 2월부터 KAIST 휴머노이드 로봇 연구센터(Humanoid Robot Research Center) 센터장이다.[^people] 기계공학과 교수 소개의 연구 분야는 동적 로봇 시스템의 제어와 설계, 다리로 이동하는 보행 로봇, 생체모사 로봇이다.[^meprof]

같은 페이지에 따르면 교수는 연세대학교에서 기계공학 학사(2005년 2월)와 석사(2007년 2월)를, University of Michigan, Ann Arbor에서 기계공학 박사(2012년 5월)를 받았다. 학사 논문은 전자석 구동기를 쓴 소형 6족 보행 로봇, 석사 논문은 돌고래 로봇, 박사 논문은 거친 지형을 걷는 2족 로봇의 제어를 다뤘다.[^people] 2012–2014년 Massachusetts Institute of Technology(MIT) 기계공학과 박사후 연구원, 2014–2015년 같은 곳 연구 과학자를 지냈고, 2015–2019년 University of Illinois at Urbana-Champaign(UIUC) 기계과학공학과 조교수(2017–2019년 Coordinated Science Laboratory 조교수 겸임)를 거쳐, KAIST 부임 뒤 2019–2022년 UIUC 겸임교수를 지냈다.[^people]

연구실 소식은 교수가 2021년 Robotics: Science and Systems(RSS)에서 Early-Career Spotlight Award를 받았고 아시아권 대학 교수로는 처음 받은 것이라고 적으며, 2020년 8월부터 IEEE/ASME Transactions on Mechatronics 편집위원이라고 적는다.[^news] 교수가 교신저자로 참여한 SO(3) 위 비선형 모델 예측 제어 논문은 IROS 2020 Best RoboCup Paper Award를 받았다.[^news] 논문 목록은 2025년 Humanoids 학회 논문에 Best Oral Paper, 2022년과 2026년 Science Robotics 논문에 표지 논문 표기를 적는다.[^pubs] 2017년 이전 논문 목록에는 MIT Cheetah 2의 고속 바운딩·장애물 뛰어넘기와 2족 보행 로봇 MABEL의 제어 논문이 있다.[^pubs]

논문으로 보면 KAIST에서의 전문 분야는 다리 로봇의 동적 보행을 위한 제어와 설계다. 학습 기반 보행 제어(대표 논문 1–3),[^p1][^p2][^p3] 접촉을 다루는 모델 예측 제어(대표 논문 4),[^p4] 등반 로봇과 유압 로봇의 하드웨어 설계(대표 논문 5, 6),[^p5][^p6] 상태 추정과 마찰 식별(대표 논문 7, 8)에 걸친다.[^p7][^p8]

## 응용 분야

대표 논문 5의 MARVEL은 페인트와 녹이 덮인 저장 탱크의 굽은 면을 올랐고, 강자성 환경에서 바닥·벽·천장을 오가는 등반 로봇으로 소개된다.[^p5] 대표 논문 1은 험한 실외와 도시 환경을 지나는 4족 로봇을, 대표 논문 6은 무거운 짐을 지는 유압 4족 로봇을 겨냥한다.[^p1][^p6] 연구실 소식은 2022년 10월 대전경찰청의 제77주년 경찰의 날 행사에서 Mini-Cheetah 로봇이 표창장 전달을 돕는 시연을 했다고 적는다.[^news]

PEOPLE 페이지의 Alumni 칸은 졸업생 16명 가운데 4명의 진로를 Diden Robotics로 적고, 그 밖에 Samsung Research, Samsung Electronics, Rainbow Robotics, INDEX Robotics 등을 적는다.[^people]

## 구성원

연구실 누리집 PEOPLE 페이지의 PhD Students 16명과 Master Students 9명, 모두 25명이다.[^people] 과정은 각 카드의 과정 줄이고, 연구 주제는 카드에 적힌 항목을 이었다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| KangKyu Lee | 박사과정 | Humanoid Robot / Designer of CYBO |  |
| Hajun Kim | 박사과정 | Sensor Fusion / Optimal Control / Learning based Control | 3, 8 |
| Sangyoung Woo | 박사과정 | Actuator Design |  |
| Jaehyun Park | 박사과정 | Quadruped Robot Control / Reinforcement Learning / Legged Robot Navigation | 1 |
| Tae-Gyu Song | 박사과정 | Quadruped Robot Design / Transmission Mechanism Design / Quadruped Robot Control | 1, 2 |
| Harim Son | 박사과정 |  |  |
| Soonpyo Kwon | 박사과정 | Elevation Mapping / GPU acceleration |  |
| Yong Um | 박사과정 (Integrated program) | Quadruped Robot Design / Magnetic Device Design | 5 |
| Yonghoon Lee | 박사과정 | Quadruped Robot Control / Imitation Learning / Agile Motion |  |
| Hyunseok Kim | 박사과정 | Quadruped Robot Design / Magnetic Device Design |  |
| Youngrang Seo | 박사과정 | State Estimation / Humanoid Robot Control |  |
| Min-Gyu Kim | 박사과정 | Quadraped Robot Control | 3, 8 |
| Gijeong Kim | 박사과정 | Quadruped Robot Control / Trajectory Optimization | 4, 8 |
| Dongyun Kang | 박사과정 | Legged Robot Control / Learning-based Control / Motion Generation | 3, 4, 8 |
| Sangmin Kim | 박사과정 | Quadruped Robot Control / Trajectory Optimization / Optimal Control |  |
| Yu Ho Jeong | 박사과정 | Quadruped Robot Control / Reinforcement Learning |  |
| Junbin Choi | 석사과정 | Mechanical Design Optimization / Transmission Mechanism Design |  |
| Hamza Dahioui | 석사과정 | Physics-Based Control / Learning-Based Control / Motion Generation |  |
| Junbeom Lim | 석사과정 | Reinforcement Learning / Actuator Design |  |
| Seungbin Oh | 석사과정 | Quadruped Robot Control / Trajectory Optimization |  |
| Jiwon Yoon | 석사과정 | Mechanical Design Optimization / Actuator Design |  |
| Jihyeok Kim | 석사과정 | Mechanical Design Optimization / Transmission Mechanism Design |  |
| Sowoo Lee | 석사과정 | Legged Robot Control / Generative Control |  |
| Kyungmo Choi | 석사과정 | Legged Robot Control / Reinforcement Learning |  |
| Yejun Joo | 석사과정 | Reinforcement Learning / Legged Robot Control |  |

## 졸업생과 이전 구성원

PEOPLE 페이지 Alumni 칸의 16명 전부다. 페이지는 이름과 현재 소속만 적고 학위·과정과 연도는 적지 않는다. 진로는 페이지 표기 그대로다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Youngha Shin |  | Diden Robotics |
| Joon-Ha Kim |  | Diden Robotics |
| Sung-Woo Kim |  | Samsung Research |
| Yunmo Yang |  | Samsung Electronics |
| Donghoon Youm |  | Ph.D. Candidate at RaiLab, KAIST |
| JongHun Choe |  | Diden Robotics |
| Trong Hieu Nguyen |  | VinMotion |
| Seungwoo Hong |  | Assistant Professor at Korea Univ. |
| Joowoong Byun |  | Xangle Product Owner |
| Sara Fragomeli |  | MS. student of Politecnico di Milano |
| Mingyu Lee |  | Diden Robotics |
| Aaron Kuba Jasiewicz |  | Tongji University |
| Seunghoon Shin |  | INDEX Robotics (인덱스 로보틱스) |
| Buyoun Cho |  | Rainbow Robotics |
| Yeseong Jee |  | Samsung Electronics |
| Ziwon Yoon |  | Ph.D. Candidate at Georgia Tech |

## 최근 논문 목록 (2021–2026)

누리집 PUBLICATIONS 페이지의 2021–2026년 연도 구역 34편이다. 학술지 표시 [J] 18편과 학회 표시 [C] 16편이며, 연도별로 2026년 3편, 2025년 10편, 2024년 2편, 2023년 3편, 2022년 9편, 2021년 7편이다. 연도는 누리집의 연도 구역이고, 각 줄은 누리집 표기 그대로다. 2021년 구역에는 2021년 10월 전에 나온 논문도 들어 있다. 줄 끝의 (cover paper)·(Best Oral Paper) 같은 표기는 누리집이 적은 것이다.[^pubs]

**2026**

- [J] JG Kang, J Park, TG Song, JH Kim, S Hong, HW Park Agile perceptive multiskill locomotion for quadrupedal robots in the wild Science Robotics 11 (116), eadz7397 (cover paper)
- [J] Kang, D., Kim, M. G., Song, T. G., Kim, H., Ha, S., & Park, H. W. Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model-Homotopy-Inspired Transfer. in IEEE Robotics and Automation Letters
- [C] Lee, S., Kang, D., Park, J., & Park, H. W. "DynaFlow: Dynamics-embedded Flow Matching for Physically Consistent Motion Generation from State-only Demonstrations." 2026 International Conference on Robotics and Automation (ICRA)

**2025**

- [J] Kim, S., Kim, H., Kim, G., Kim, M. G., & Park, H. W. (2025). "Dynamically-Consistent Trajectory Optimization for Legged Robots via Contact Point Decomposition." in IEEE Robotics and Automation Letters
- [C] J. Choe, G. Kim, H. Kim, D. Kang, M. -S. Kim and H. -W. Park, "Design of a 3-DOF Hopping Robot with an Optimized Gearbox: An Intermediate Platform Toward Bipedal Robots," 2025 IEEE-RAS 24th International Conference on Humanoid Robots (Humanoids), Seoul, Korea, Republic of, 2025, pp. 653-660, doi: 10.1109/Humanoids65713.2025.11203011. (Best Oral Paper)
- [C] Kang, D., Kim, G., Choe, J., Kim, H., & Park, H. W. (2025). "Learning Impact-Rich Rotational Maneuvers via Centroidal Velocity Rewards and Sim-to-Real Techniques: A One-Leg Hopper Flip Case Study." 2025 Conference on Robot Learning (CoRL)
- [J] M. -G. Kim, D. Kang, H. Kim and H. -W. Park, "A Modular Residual Learning Framework to Enhance Model-Based Approach for Robust Locomotion," in IEEE Robotics and Automation Letters, doi: 10.1109/LRA.2025.3592067.
- [C] Lee, Y. H., Kim, G., Song, T. G., & Park, H. W. (2025, July). Path Planning and Foothold Adaptation for Quadrupedal Locomotion on Challenging Terrain. In Robot Intelligence Technology and Applications 9: Results from the 12th International Conference on Robot Intelligence Technology and Applications (Vol. 1419, p. 194). Springer Nature.
- [J] Shin S, Hong S, Kim M-S, Oh J-H, Park H-W. Design of LIGHTDOG: A high payload-to-weight, hose-less hydraulic quadrupedal robot. The International Journal of Robotics Research. 2025;0(0). doi:10.1177/02783649251349225
- [C] Kim, G., Lee, Y. H., & Park, H. W., "A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards." 2025 International Conference on Robotics and Automation (ICRA), 2025
- [C] Lee, Y. H., Kim, K., Park, J., Park, C. H., & Park, H. W., "Soft Contact Model for Robust Locomotion of Legged Robots." 2025 International Conference on Robotics and Automation (ICRA) Workshop on Robot safety under uncertainty from “intangible” specifications, Atlanta, USA, May 2025
- [J] Y. Nisticò, H. Kim, J. C. V. Soares, G. Fink, H. -W. Park and C. Semini, "Multi-Sensor Fusion for Quadruped Robot State Estimation Using Invariant Filtering and Smoothing," in IEEE Robotics and Automation Letters, doi: 10.1109/LRA.2025.3564711.
- [J] H. Kim, D. Kang, M. -G. Kim, G. Kim and H. -W. Park, "Online Friction Coefficient Identification for Legged Robots on Slippery Terrain Using Smoothed Contact Gradients," in IEEE Robotics and Automation Letters, doi: 10.1109/LRA.2025.3541428.

**2024**

- [J] Y. -H. Shin, T. -G. Song, G. Ji and H. -W. Park, "Reinforcement Learning for High-Speed Quadrupedal Locomotion With Motor Operating Region Constraints: Mitigating Motor Model Discrepancies through Torque Clipping in Realistic Motor Operating Region," in IEEE Robotics & Automation Magazine, doi: 10.1109/MRA.2024.3487322.
- [J] Kim G, Kang D, Kim J-H, Hong S, Park H-W. Contact-implicit Model Predictive Control: Controlling diverse quadruped motions without pre-planned contact modes or trajectories. The International Journal of Robotics Research. 2024;44(3):486-510. doi:10.1177/02783649241273645

**2023**

- [J] Ziwon Yoon, Joon-Ha Kim, Hae-Won Park, “Invariant Smoother for Legged Robot State Estimation With Dynamic Contact Event Information”, IEEE Transactions on Robotics, 2023
- [J] D. Youm, H. Jung, H. Kim, J. Hwangbo, H. -W. Park and S. Ha, "Imitating and Finetuning Model Predictive Control for Robust and Symmetric Quadrupedal Locomotion," in IEEE Robotics and Automation Letters, doi: 10.1109/LRA.2023.3320827.
- [J] J. Choe, J. -H. Kim, S. Hong, J. Lee and H. -W. Park, "Seamless Reaction Strategy for Bipedal Locomotion Exploiting Real-Time Nonlinear Model Predictive Control," in IEEE Robotics and Automation Letters, vol. 8, no. 8, pp. 5031-5038, Aug. 2023, doi: 10.1109/LRA.2023.3291273.

**2022**

- [J] S Hong, Y Um, J Park, HW Park "Agile and versatile climbing on ferromagnetic surfaces with a quadrupedal robot." Science Robotics 7.73 (2022): eadd1017 (Cover Paper)
- [C] G. Kim, D. Kang, J. -H. Kim and H. -W. Park, "Contact-Implicit Differential Dynamic Programming for Model Predictive Control with Relaxed Complementarity Constraints," 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2022
- [C] T. -G. Song, Y. -H. Shin, S. Hong, H. C. Choi, J. -H. Kim and H. -W. Park, "DRPD, Dual Reduction Ratio Planetary Drive for Articulated Robot Actuators," 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2022
- [C] M.G. Kim et al., "Design of Foothold Decision Model in Convex Model Predictive Control for Legged Robots," in Robot Intelligence Technology and Applications 6. RiTA 2021. Lecture Notes in Networks and Systems, vol 429. Springer, Cham. https://doi.org/10.1007/978-3-030-97672-9_3
- [C] J.H. Choe et al., "2-DOF Rolling Joint with the Novel Interior Reinforcement Structures," in Robot Intelligence Technology and Applications 6. RiTA 2021. Lecture Notes in Networks and Systems, vol 429. Springer, Cham. https://doi.org/10.1007/978-3-030-97672-9_15
- [C] J.W. Byun et al., "Learning Footstep Planning for the Quadrupedal Locomotion with Model Predictive Control," in Robot Intelligence Technology and Applications 6. RiTA 2021. Lecture Notes in Networks and Systems, vol 429. Springer, Cham. https://doi.org/10.1007/978-3-030-97672-9_4
- [C] L. Amatucci et al., "Monte Carlo Tree Search Gait Planner for Non-Gaited Legged System Control," 2022 International Conference on Robotics and Automation (ICRA), 2022, pp. 4701-4707, doi: 10.1109/ICRA46639.2022.9812421.
- [C] Y.H. Shin et al., "Design of KAIST HOUND, a Quadruped Robot Platform for Fast and Efficient Locomotion with Mixed-Integer Nonlinear Optimization of a Gear Train," 2022 International Conference on Robotics and Automation (ICRA), 2022, pp. 6614-6620, doi: 10.1109/ICRA46639.2022.9811755.
- [J] B. Cho, S. -W. Kim, S. Shin, J. -H. Oh, H. -S. Park and H. -W. Park, "Energy-Efficient Hydraulic Pump Control for Legged Robots Using Model Predictive Control," in IEEE/ASME Transactions on Mechatronics, 2022, doi: 10.1109/TMECH.2022.3190506.

**2021**

- [J] J. H. Kim et al., "Legged Robot State Estimation With Dynamic Contact Event Information," in IEEE Robotics and Automation Letters, vol. 6, no. 4, pp. 6733-6740, Oct. 2021, doi: 10.1109/LRA.2021.3093876.
- [J] S. -W. Kim, B. Cho, S. Shin, J. -H. Oh, J. Hwangbo and H. -W. Park, "Force Control of a Hydraulic Actuator With a Neural Network Inverse Model," in IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 2814-2821, April 2021, doi: 10.1109/LRA.2021.3062353.
- [J] B. Cho et al., "Design of a Compact Embedded Hydraulic Power Unit for Bipedal Robots," in IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 3631-3638, April 2021, doi: 10.1109/LRA.2021.3061390.
- [J] Yaran Ding, Abhishek Pandala, Chuzheng Li, Young-ha Shin, Hae-Won Park, “Representation-Free Model Predictive Control for Dynamic Motions in Quadrupeds”, IEEE Transactions on Robotics, 2021,
- [C] Yeseong Jeong, Shin Seunghoon, Soonpyo Kwon, Buyoun Cho, Kim Sung Woo, Joon-Ha Kim, Jun-Ho Oh, Hae-Won Park, “Real-time Bilateral Teleoperation with Electric and Hydraulic Actuator,” The Korea Robotics Society Annual Conference, 2021
- [C] Soonpyo Kwon, Joon-Ha Kim, Juwoong Byun, Hae-Won Park, “GPU Acceleration of Probabilistic Local Height Map that Resolves Race Condition,” The Korea Robotics Society Annual Conference, 2021
- [C] Mingyu Kim, Seungwoo Hong, Joon-Ha Kim, Hae-Won Park, “Design of Foothold Optimization Model for Controlling Legged Robots,” The Korea Robotics Society Annual Conference, 2021

## 소식

누리집 NEWS 페이지 NEWS & UPDATES 칸의 글 가운데 날짜가 2021년 10월 13일 이후인 5건(2022년 10월–2026년 7월)과, 날짜가 함께 적히지 않은 YTN Science 소개 글 1건이다. 날짜는 글에 붙은 날짜이고 문구는 글 제목 그대로다.[^news]

- 2026-07-15 · Quadrupedal robot, HOUND, is published on the cover of July issue of Science Robotics
- 날짜 표기 없음 · KAIST Humanoid Featured on YTN Science
- 2024-11-21 · KAIST Hound 2 Robot Showcased on CNN's 'Tech for Good
- 2023-12-12 · HOUND robot has set a Guiness World Record by running "The fastest 100 metres by a quadrupedal robot"
- 2022-12-21 · Wall-climbing robot, MARVEL, is published on the cover of December issue of Science Robotics
- 2022-10-21 · 제77주년 경찰의 날 시연

## 연락과 위치

- 위치: 연구실 N9동 4150호, 교수실 기계동(N7) 6104호[^home][^meprof]
- 전화: 교수 042-350-3242[^meprof]
- 교수 이메일: haewonpark@kaist.ac.kr[^meprof]
[^p1]: J.-G. Kang 외, H.-W. Park, Science Robotics 11, eadz7397 (2026). <https://doi.org/10.1126/scirobotics.adz7397> 초록 기준.
[^p2]: Y.-H. Shin, T.-G. Song, G. Ji, H.-W. Park, IEEE Robotics & Automation Magazine 32, 49-59 (2025). <https://doi.org/10.1109/mra.2024.3487322> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: M.-G. Kim, D. Kang, H. Kim, H.-W. Park, IEEE Robotics and Automation Letters 10, 9072-9079 (2025). <https://doi.org/10.1109/lra.2025.3592067> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: G. Kim 외, H.-W. Park, The International Journal of Robotics Research 44, 486-510 (2025). <https://doi.org/10.1177/02783649241273645> 초록 기준.
[^p5]: S. Hong, Y. Um, J. Park, H.-W. Park, Science Robotics 7, eadd1017 (2022). <https://doi.org/10.1126/scirobotics.add1017> 초록 기준.
[^p6]: S. Shin 외, H.-W. Park, The International Journal of Robotics Research 45, 285-307 (온라인 2025-06-25). <https://doi.org/10.1177/02783649251349225> 초록 기준.
[^p7]: Z. Yoon, J.-H. Kim, H.-W. Park, IEEE Transactions on Robotics 40, 193-212 (2024). <https://doi.org/10.1109/tro.2023.3328202> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Kim 외, H.-W. Park, IEEE Robotics and Automation Letters 10, 3150-3157 (2025). <https://doi.org/10.1109/lra.2025.3541428> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 로봇 제어 & 설계 연구실 누리집 첫 화면 <https://www.dynamicrobot.kaist.ac.kr/> (연구실 소개, 대표 연구, 바닥 주소, 2026-10-23 열람)
[^people]: 연구실 누리집 PEOPLE 페이지 <https://www.dynamicrobot.kaist.ac.kr/contact> (교수 Research Interests·Education·Professional Experience, PhD Students, Master Students, Alumni, 2026-10-23 열람)
[^robots]: 연구실 누리집 ROBOTS 페이지 <https://www.dynamicrobot.kaist.ac.kr/new-page> (2026-10-23 열람)
[^hound1]: 연구실 누리집 ROBOTS 메뉴 KAIST HOUND 1 페이지 <https://www.dynamicrobot.kaist.ac.kr/kaist-hound-1> (Selected Works, Specifications, 2026-10-23 열람)
[^hound2]: 연구실 누리집 ROBOTS 메뉴 KAIST HOUND 2 페이지 <https://www.dynamicrobot.kaist.ac.kr/kaist-hound-2> (Specifications, 2026-10-23 열람)
[^control]: 연구실 누리집 RESEARCH 메뉴 CONTROL 페이지 <https://www.dynamicrobot.kaist.ac.kr/control> (Learning-Based Control, Model-Based Control, 2026-10-23 열람)
[^hw]: 연구실 누리집 RESEARCH 메뉴 HARDWARE-DESIGN 페이지 <https://www.dynamicrobot.kaist.ac.kr/control-1> (2026-10-23 열람)
[^est]: 연구실 누리집 RESEARCH 메뉴 ESTIMATION 페이지 <https://www.dynamicrobot.kaist.ac.kr/control-1-1> (Legged Robot State Estimation, Parameter Identification, 2026-10-23 열람)
[^pubs]: 연구실 누리집 PUBLICATIONS 페이지 <https://www.dynamicrobot.kaist.ac.kr/publications> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^news]: 연구실 누리집 NEWS 페이지 <https://www.dynamicrobot.kaist.ac.kr/news> (NEWS & UPDATES, 2026-10-23 열람)
[^meprof]: KAIST 기계공학과 교수 소개(박해원) <https://me.kaist.ac.kr/pop/team.html?uid=25&LANGUAGE_TYPE=kor> (최종학위, 연구분야, 연구실, 이메일, 사무실, 전화, 2026-10-23 열람)

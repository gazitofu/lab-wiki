# 비행 역학 및 제어 연구실 (Flight Dynamics and Control Laboratory, FDCL)

**KAIST 항공우주공학과 · 이창훈 교수**

- 분야: 미사일·무인항공기·우주발사체·우주비행기 등 항공우주 비행체의 유도·항법·제어, 실시간 최적화 기반 전산 유도제어와 궤적 최적화, 항공우주 응용 기계학습·빅데이터 분석, 표적 추적 필터
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 제어 이론·제어 공학[^research][^aelab], 과학·공학 AI[^research][^p5][^p6], 드론·무인 항공기[^p4], 유도·항법·제어(GNC)[^aelab], 발사체·로켓 추진[^p2]
- 홈페이지: <https://fdcl2.kaist.ac.kr/>
- 근거와 출처: [비행 역학 및 제어 연구실 근거 페이지](fdcl2-sources.md)

> 미사일, 무인항공기, 우주발사체, 우주비행기 같은 항공우주 비행체가 목표한 곳에 이르도록 갈 길을 정하고 그대로 움직이게 하는 유도·제어 기법을 연구하는 항공우주공학과 연구실이다.[^home][^aelab] 연구 페이지는 연구를 정밀 유도제어, 지능형 유도제어, 전산 유도제어의 세 기둥으로 나눈다.[^research]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 이창훈 교수의 연구실이다. 누리집 첫 화면에 따르면 FDCL은 1989년 탁민제(Min-Jea Tahk) 교수가 세웠고, 이창훈 교수가 2019년에 합류했다.[^home][^prof] 첫 화면은 FDCL이 1989년부터 비행 역학과 제어 분야의 학생, 엔지니어, 교수를 길러 왔고 국가 항공우주 연구개발 사업에서 핵심 역할을 해 왔다고 적는다.[^home] 학과 연구실 소개는 연구실이 다양한 비행체 시스템의 실제 유도(guidance, 비행체가 목표에 이르도록 갈 길과 명령을 정하는 일)와 제어(control, 그 명령대로 비행체가 움직이게 하는 일) 문제를 다루며, 미사일, 무인항공기, 우주발사체, 우주비행기 등 항공우주 비행체의 유도, 항법(navigation, 비행체가 자기 위치와 속도를 추정하는 일), 제어를 연구한다고 소개한다. 주된 연구 분야는 유도 미사일의 유도·제어, 무인항공기의 비행 제어 시스템, 항공우주 응용 분야의 빅데이터 분석과 기계학습이고, 전산 유도제어(computational guidance and control)와 궤적 최적화(trajectory optimization) 연구도 진행한다고 적는다.[^aelab] 학과 교수진 목록은 교수의 연구분야를 Guidance & Control and Optimization(유도·제어와 최적화)으로 적는다.[^aefac]

연구 페이지는 연구의 지향을 「Towards More Advanced Guidance and Control (All that G&C)」으로 적고, 고급 유도·제어(G&C) 기법으로 자율 시스템의 실제 유도·제어 문제를 다루며 특히 우주와 군사 응용에 초점을 둔다고 설명한다. 첫째 기둥인 정밀 유도제어(Precision Guidance and Control, PG&C)는 미사일 방어, 소행성 요격 등을 위한 정밀 유도·제어 기법 개발이다. 둘째 기둥인 지능형 유도제어(Intelligent Guidance and Control, IG&C)는 빅데이터 분석과 기계학습 같은 새 기술을 실제 유도·제어 문제 해결에 쓰는 연구다. 셋째 기둥인 전산 유도제어(Computational Guidance and Control, CG&C)는 실시간 최적화 기법, 최적화 풀이기, 검증 방법 같은 기본 틀을 만드는 연구다.[^research]

누리집 첫 화면의 연구 성과 소개는 한빛-나노(HANBIT-Nano)의 'SPACEWARD' 임무와 그 시험 비행체 한빛-TLV의 유도·제어 알고리즘 설계, 수직 이착륙 재사용 발사체(VTVL-RLV) 부스터의 회수 유도·제어와 자체 개발한 고충실도 6자유도 시뮬레이션, 볼록 최적화 기반 계획·추종 틀로 재사용 궤도 로켓을 착륙시키는 연료 최적 유도, 재사용 발사체 시험기(RLV-TD)의 계류 비행 시험·1차원 비행 시험용 유도·제어 알고리즘, 호버바이크의 자세 제어 알고리즘, 12개 회전 날개 비행체(dodecacopter)의 고장 허용 제어, 한국항공우주연구원과 함께한 재사용 발사체(KSLV-R) 6자유도 시뮬레이션을 든다.[^home] 누리집 과제 목록의 진행 중 과제에는 재사용 발사체의 연착륙 최적 유도제어, 우주비행기의 제어 통합 성능 분석, 극초음속 비행 환경의 비행제어 성능 해석, 무인 우주비행체의 귀환 비행 유도제어, 무인 이동체 자율 유도제어, 유도무기의 중기 유도와 성능 분석 도구 개발 등이 있다.[^projects]

## 주요 연구 주제

### 1. 전산 유도제어: 실시간 최적화와 발사체·재진입 비행체 유도

연구 페이지에 따르면 전산 유도제어 기둥은 실시간 최적화 기법, 최적화 풀이기, 검증 방법 같은 기본 틀을 만드는 연구다.[^research] 대표 논문 1은 유도·제어에서 자주 생기는 실시간 최적화 문제를 비행체에 실린 컴퓨터에서 풀기 위한 맞춤형 2차 원뿔 계획(second-order cone programming, SOCP) 풀이기와, 문제 구조에 맞춘 풀이기 코드를 만들어 주는 코드 생성 도구다.[^p1] 대표 논문 2는 재사용 발사체가 착륙할 때 연료 최적 착륙 궤적을 세우는 계획 문제와 실시간 추종 명령을 정하는 문제를 나눠 순차 볼록 계획으로 푸는 착륙 유도 기법이다.[^p2] 대표 논문 3은 대기권에 다시 들어오는 비행체의 재진입 유도 문제를 순차 볼록 계획으로 풀 때 제어 입력이 빠르게 흔들리는 문제를, 새 메시 세분화(mesh refinement, 계산에 쓰는 시간 격자를 필요한 곳에서 촘촘하게 다시 나누는 일) 전략으로 줄였다.[^p3] 2021–2026년 논문 목록에는 우주비행기의 볼록 최적화 기반 재진입 유도(2022), 재사용 궤도 로켓의 볼록 최적화 기반 착륙 유도·제어 알고리즘(2025), 다중 펄스 로켓 미사일의 추력 통합 궤적 최적화(2023), 지점 간 로켓 화물 수송 체계의 궤적 최적화 기반 임무 분석(2024)도 있다.[^pubs]

### 2. 지능형 유도제어: 기계학습과 무인기 제어

연구 페이지에 따르면 지능형 유도제어 기둥은 빅데이터 분석과 기계학습 같은 새 기술을 실제 유도·제어 문제 해결에 쓰는 연구다.[^research] 대표 논문 4는 쿼드로터(회전 날개가 네 개인 무인기)가 정해진 경로를 따라가도록, 표본을 뽑아 제어 입력을 고르는 모델 예측 경로 적분(MPPI) 제어에 몇 개의 유도 변수만 고르게 하는 정책을 넣은 방법이다.[^p4] 대표 논문 5는 물리 정보 신경망(physics-informed neural network, 운동 방정식 같은 물리 법칙을 학습에 함께 넣는 신경망)과 최적 제어 이론을 결합해 비행체의 최적 제어 입력을 계산하는 틀이고, 대표 논문 6은 물리 정보 신경망으로 비행체의 불확실한 매개변수를 추정하는 방법이다.[^p5][^p6] 2021–2026년 논문 목록에는 가우스 과정 회귀를 쓴 도심 항공 모빌리티의 외란 제거 제어(2024), 불확실성을 고려한 무인기 경로 추종 MPPI(2025), 동축 12개 회전 날개 비행체의 고장 허용 제어 할당(2025), 공력 제어 미사일의 비행 자료 집합과 그 활용(2022)도 있다.[^pubs]

### 3. 정밀 유도제어: 도달 시간·각도를 맞추는 유도 법칙

연구 페이지에 따르면 정밀 유도제어 기둥은 미사일 방어, 소행성 요격 등을 위한 정밀 유도·제어 기법 개발이다.[^research] 대표 논문 7은 정해진 시각에 목표에 도달하게 하는 도달 시간 제어 유도 법칙을 다항식으로 세우고 최적 제어 이론에서 얻은 성질을 넣은 연구이고, 대표 논문 8은 가상의 목표점을 향하는 비례 항법(proportional navigation, 목표를 바라보는 시선 방향이 도는 빠르기에 비례해 진로를 바꾸는 유도 방식) 명령으로 원하는 도달 방향을 맞추는 도달 각도 제어 유도 기법이다.[^p7][^p8] 2021–2026년 논문 목록에는 탐색기 시야 제한을 고려한 유도 법칙, 공기 저항을 고려한 도달 각도 제어 유도, 임의의 표적 기동과 요격체 전략을 위한 유도 설계 틀(2026, 게재 승인) 등 같은 주제의 논문이 이어진다.[^pubs]

## 대표 논문

이창훈 교수가 교신저자(누리집 목록의 밑줄)이자 마지막 저자인 2024–2026년 국제 학술지 논문 가운데 초록을 확인할 수 있는 여덟 편을 세 연구 기둥(전산 유도제어, 지능형 유도제어, 정밀 유도제어)에 나눠 골랐다. 교수는 2019년부터 KAIST에 있다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Customized Interior-Point Methods Solver for Embedded Real-Time Convex Optimization](https://doi.org/10.1109/taes.2026.3673639) · IEEE Transactions on Aerospace and Electronic Systems | 현대 유도·제어 응용에서 자주 생기는 임베디드 실시간 최적화를 위해 맞춤형 2차 원뿔 계획(SOCP) 풀이기를 만들었다. 풀이기는 예측-수정형 원-쌍대 내점법(PDIPM)을 쓰고, 해가 없는 문제를 알아내는 동차 임베딩 틀을 결합했다. 기존 동차 자기쌍대 임베딩과 달리 이차 비용 함수를 문제를 바꿔 쓰지 않고 바로 다룰 수 있어, 바꿔 쓰는 과정에서 희소성(행렬에 0인 원소가 많은 성질)을 잃어 성능이 떨어지는 일을 피한다. 풀 문제의 희소성 구조를 분석해 미리 정한 틀로 맞춤 풀이기 코드를 만들어 주는 코드 생성 도구도 개발했다. 생성된 코드는 표준 라이브러리 math.h 외에 외부 의존이 없는 C 코드이고 모든 자료를 정적으로 할당한다. 임베디드 플랫폼에서 한 벤치마크와 수치 실험에서, 유도·제어 응용에 흔한 문제 크기에서 기존 풀이기들보다 좋은 성능을 보였다.[^p1] | 1저자 J. I. Jang, 마지막 저자·교신 표시 이창훈 (2명) |
| 2 | 2025 | [Optimal Landing Guidance of Reusable Launch Vehicles with Dual-convex Optimization](https://doi.org/10.1007/s12555-024-0628-3) · International Journal of Control, Automation, and Systems | 순차 볼록 계획(SCP)에 바탕을 둔 모델 예측 방식으로 재사용 발사체(RLV)의 착륙 유도 전략을 내놓았다. 재사용 발사체에 맞는 실제 경로 제약을 담아 연료 최적 착륙 궤적을 계획하는 문제와, 실시간 최적 추종 명령을 정하는 문제의 두 최적 제어 문제를 따로 세운다. 이렇게 계획과 추종을 나누면 추종 단계의 예측 구간 길이를 조절해 계산 부담을 줄이면서 폐루프에 가까운 성능을 낼 수 있다. 추종 단계에는 다른 회전 운동 표현을 써서 최적 제어 문제를 수치적으로 더 안정되게 풀고 비행체의 과도 동역학을 반영했다. 추력 방향을 바꿔 제어하는 재사용 발사체에 맞춰 계획·추종 두 단계의 공력 모형도 고쳐, 계산을 늘리지 않고 모형 충실도의 차이를 줄였다. 여러 6자유도 시뮬레이션으로 유도 성능이 좋아진 것을 확인했다.[^p2] | 1저자 K. W. Jung, 마지막 저자·교신 표시 이창훈 (4명) |
| 3 | 2024 | [New Adaptive Mesh Refinement Strategy for Entry Guidance via Sequential Convex Programming](https://doi.org/10.2514/1.g006918) · Journal of Guidance, Control, and Dynamics | 대기권 재진입 경로를 계산할 때 제어 명령이 빠르게 흔들리는 문제를 줄이는 계산 방법이다. 계산 구간을 다시 나누는 기준을 제안했고, 수치 시뮬레이션에서 명령의 흔들림을 줄이고 계산 결과의 정확도를 높였다.[^p3] | 1저자 J. Bae, 마지막 저자·교신 표시 이창훈 (3명) |
| 4 | 2026 | [Adaptive Path-Following for Quadrotors via Parameterized-Policy MPPI Control](https://doi.org/10.1007/s42405-026-01183-x) · International Journal of Aeronautical and Space Sciences (게재 승인) | 쿼드로터의 경로 추종을 위해 매개변수화한 정책을 쓰는 모델 예측 경로 적분(MPPI) 제어 틀을 제안했다. MPPI 제어는 비선형·비볼록 문제에 쓰기 좋지만, 경로 추종에 바로 쓰면 제어 입력을 찾는 공간이 넓고 모형 오차에 민감하다는 문제가 있다. 제안한 방법은 가상 목표점을 두는 추적형 유도 법칙을 낮은 차원의 물리적으로 해석할 수 있는 정책으로 넣고, 세 축 가속도 전체 대신 유도 이득과 축 방향·전진 가속도 같은 몇 개의 유도 변수만 뽑아 조정해 표본 효율과 계산 부담을 개선한다. 모형 불확실성과 바람 외란을 다루기 위해 비선형 외란 관측기(NDO)를 넣어 외란을 실시간으로 보상한다. 바람이 없을 때와 있을 때의 꺾은선 기준 경로 수치 시뮬레이션에서 유도 법칙만 쓴 방법과 전체 차원 입력의 표준 MPPI 제어보다 경로 추종 오차가 일관되게 작고, 제어 입력이 매끄럽고, 표본 효율이 뚜렷이 높았다.[^p4] | 1저자 E. T. Jeong, 마지막 저자·교신 표시 이창훈 (3명) |
| 5 | 2026 | [Nonlinear Optimal Control for Flight Vehicles using Neural Operators and Physics-Informed Neural Networks](https://doi.org/10.1177/09544100261451532) · Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering (게재 승인) | 물리 정보 딥러닝과 고전 최적 제어 이론을 결합해 최적 제어 입력을 계산하는 틀을 내놓았다. 지배 미분방정식과 종단 제약을 오일러-라그랑주 틀로 세워 물리 정보 신경망에 넣어, 신경망이 동역학과 경계 조건을 따르게 한다. 또 주어진 제어 입력에 대응하는 종단 상태를 DeepONet 구조로 추정한다. 미사일 교전 상황의 최적 도달 시간·도달 각도 유도 문제에 공기 저항이 있을 때와 없을 때를 모두 적용해 검증했다. 넓은 범위의 초기·종단 조건에서 최적해를 안정적으로 찾았고, 최적해 공간의 구조에 대한 통찰과 시스템 설계에 쓸 가능성을 준다. 학습 손실을 충분히 줄이면 GPOPS로 계산한 해와 거의 같았다. 저자들은 이 방법을 항공우주 공학의 더 넓은 최적 제어 문제로 넓힐 수 있다고 적는다.[^p5] | 1저자 K. M. Na, 마지막 저자·교신 표시 이창훈 (2명) |
| 6 | 2024 | [Identification of Uncertain Parameter in Flight Vehicle Using Physics-Informed Deep Learning](https://doi.org/10.2514/1.i011269) · Journal of Aerospace Information Systems | 물리 정보 신경망을 이용해 비행체의 불확실한 매개변수를 추정하는 방법을 제안했다. 수치 시뮬레이션으로 추정 성능과 잡음이 있는 자료에 대한 적용 가능성을 살폈다.[^p6] | 1저자 K. M. Na, 마지막 저자·교신 표시 이창훈 (2명) |
| 7 | 2025 | [Polynomial Based Impact-Time-Control Guidance Law Integrating Optimal Characteristics](https://doi.org/10.1109/taes.2025.3605915) · IEEE Transactions on Aerospace and Electronic Systems | 표적 요격에서 어느 정도의 최적성을 유지하는 다항식 기반 도달 시간 제어 유도(ITCG) 법칙을 제안했다. 앞선 연구를 바탕으로, 선도각(lead angle)의 코사인이 남은 비행 시간(time-to-go)에 대한 다항식을 따르도록 유도 명령을 세워 도달 시간 제약을 지키게 한다. 최적성을 더 높이려고 최적 제어 이론에서 얻은 성질을 이 다항식에 넣었고, 그 최적해는 시간에 대한 야코비 타원 함수로 나타난다. 이 해는 직접 최적화 결과와 비교해 확인했다. 이 방법은 작은 각 가정 같은 흔한 근사를 쓰지 않고 수치 기법도 필요하지 않다. 수치 시뮬레이션에서 원하는 도달 시간에 표적을 요격하면서 어느 정도의 최적성을 유지했다.[^p7] | 1저자 J. Park, 마지막 저자·교신 표시 이창훈 (2명) |
| 8 | 2025 | [Proportional Navigation Guidance with Virtual Targeting for Impact-Angle-Control](https://doi.org/10.1109/taes.2024.3448393) · IEEE Transactions on Aerospace and Electronic Systems | 가상 표적 개념을 쓰는 도달 각도 제어 유도(IACG) 방법을 소개한다. 제안한 유도 법칙은 가상 표적을 요격하도록 하는 비례 항법 유도(PNG) 명령으로 짜여 있다. 먼저 비례 항법의 성질을 살펴 그것으로 유도 법칙을 만들고, 경계 조건을 지키는 가상 표적의 위치를 해석적으로 구한다. 그래서 비례 항법의 단순함을 살리면서, 기존 방법과 달리 남은 비행 시간을 추정하지 않고도 원하는 도달 방향으로 실제 표적을 요격할 수 있다. 속도가 변하는 비선형 교전 상황에도 맞출 수 있다. 여러 교전 조건에서 가상 표적 위치의 성질과 최적 유도 법칙과의 관계를 살폈고, 비례 항법의 성질 때문에 이 방법의 성능 지표가 제어 에너지 최소화와 밀접하다는 점을 보였다. 수치 시뮬레이션과 비교로 효과를 확인했다.[^p8] | 1저자 J. Park, 마지막 저자·교신 표시 이창훈 (4명) |

## 교수와 전문 분야

이창훈 교수(Lee, Chang-Hun)는 KAIST 항공우주공학과 부교수다. 학과 교수진 목록은 직위를 Associate Professor로, 학력을 B.S. KAIST('08), M.S. KAIST('10), Ph.D. KAIST('13)로, 연구분야를 Guidance & Control and Optimization으로 적는다.[^aefac] 누리집 교수 페이지에 따르면 KAIST에서 항공우주공학 학사(2008), 석사(2010), 박사(2013)를 받았고, 2013–2015년 국방과학연구소(Agency for Defense Development) 유도제어팀 선임연구원(Senior Researcher), 2016–2018년 영국 Cranfield University의 School of Aerospace, Transportation, and Manufacturing 연구원(Research Fellow)으로 일했다. 2019년부터 KAIST 항공우주공학과에 있으며 현재 (Tenured) Associate Professor다. 최근 연구 관심사는 고급 미사일 유도·제어, 무인항공기의 협동 제어, 표적 추적 필터, 딥러닝, 항공 자료 분석이고, International Journal of Aeronautical and Space Science와 IEEE Transactions on Aerospace and Electronic Systems의 부편집장(associate editor)을 맡고 있다.[^prof] 교수 페이지는 연구실을 세운 탁민제 교수를 명예교수(Founder, Professor Emeritus)로 함께 소개한다.[^prof]

누리집 논문 목록의 책 구역에는 교수가 공저한 「Optimal Guidance and Its Applications in Missiles and UAVs」(Springer Nature, 2020)와 「Rocket Engineering」(HongReung, 2025)이 있다.[^pubs] 누리집 강의 페이지에 따르면 교수는 2019–2025년 항공우주 동역학(AE250), 고등 선형안정 및 제어(AE552), 비행동역학 및 제어(AE450), 항법 및 유도(AE650), 기초항공우주 프로젝트(AE201) 등을 가르쳤다.[^lectures] 연구 기둥과 논문으로 보면 전문 분야는 미사일·발사체·재진입 비행체의 유도 법칙과 자동 조종 설계, 볼록 최적화 기반의 실시간 궤적 최적화와 전산 유도, 물리 정보 신경망 등 기계학습을 쓴 비행체 제어·추정이다.[^research][^pubs]

## 응용 분야

연구 페이지는 정밀 유도제어의 응용으로 미사일 방어와 소행성 요격 등을 들고, 연구 전체가 특히 우주와 군사 응용에 초점을 둔다고 적는다.[^research] 누리집 첫 화면의 연구 성과는 한빛-나노와 그 시험 비행체 한빛-TLV, 재사용 발사체 시험기(RLV-TD)와 재사용 발사체(KSLV-R), 호버바이크, 12개 회전 날개 비행체를 든다.[^home] 대표 논문 4와 2021–2026년 논문 목록은 쿼드로터와 도심 항공 모빌리티의 비행 제어도 다룬다.[^p4][^pubs]

## 구성원

누리집 Post Doctors 페이지의 박사후연구원 4명과 Students 페이지의 박사과정 7명, 파트타임 박사과정(Part-time) 7명, 석사과정 9명, 모두 27명이다. 「시작」은 이름 앞에 적힌 두 자리 연도와 S·F 표기를 그대로 옮겼다. 파트타임 박사과정은 누리집이 이름 옆에 적은 소속 기관을 과정 칸에 함께 적었다. 「연구 주제」는 카드의 Research Interest 칸이다.[^postdocs][^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 폴 노빈 (Nobin, Paul) | 박사후연구원 | 24F | Bio-inspired guidance, navigation, and control (GNC) strategies; Flight autonomy using AI/ML for aerospace vehicles; Simulator design for drones, missiles, launch vehicles, and space missions; Reinforcement learning for intelligent intercept and cooperative swarms; Guidance theory and its applications |  |
| 박준우 (Park, Jun-Woo) | 박사후연구원 | 25F | Robust navigation under GNSS-denied environments: TRN, VisNAV, MagNAV; Bayesian state estimation for aerospace systems: particle filter, EKF, UKF; Embedded real-time implementation: EGI, flight controller (FC); Information-theoretic flight autonomy and reinforcement learning applications |  |
| 에다타람 미둔 (Midhun, Edatharam Kunnath) | 박사후연구원 | 25F | Robotics and AI; Guidance and control; Path Planning; Unmanned Aircraft Systems Traffic Management; Computer Vision |  |
| 정철구 (Jung, Cheol-Goo) | 박사후연구원 | 26F | Missile guidance and control; Target tracking and guidance filter; Optimization | 2 |
| 박종찬 (Park, Jong-Chan) | 박사과정 | 24S | Guidance and control for missiles and launch vehicles; Nonlinear control | 7, 8 |
| 장재일 (Jang, Jae-Il) | 박사과정 | 25S | Convex Programming; Real-Time Embedded Optimization; Guidance and control for launch vehicles | 1 |
| 강오령 (Kang, Oh-Ryeung) | 박사과정 | 26S | Missile guidance and control; Target tracking and guidance filter |  |
| 안세환 (An, Se-Hwan) | 박사과정 | 26F | Hypersonic vehicle guidance and control; Reentry guidance and control; Cooperative guidance |  |
| 이유정 (Lee, You-Jeong) | 박사과정 | 26F | Nonlinear and adaptive control for aerospace system; Guidance and control of hypersonic vehicles and UAVs |  |
| 이흔재 (Lee, Heun-Jae) | 박사과정 | 26F | Trajectory optimization; Missile guidance and control |  |
| 심재욱 (Shim, Jae-Wook) | 박사과정 | 26F | Guidance and control for launch vehicles and missiles; Optimal guidance and control |  |
| 한유덕 (Han, Yoo-Deok) | 박사과정 (Part-time, 국방과학연구소 [ADD]) | 19F |  |  |
| 박종근 (Park, Jong-Geun) | 박사과정 (Part-time, 대한항공 [Korean Air]) | 20F |  |  |
| 오영재 (Oh, Young-Jae) | 박사과정 (Part-time, 한국항공우주연구원 [KARI]) | 23F |  |  |
| 최은주 (Choi, Eun-Ju) | 박사과정 (Part-time, 한국항공우주연구원 [KARI]) | 23F |  |  |
| 심주현 (Sim, Ju-Hyen) | 박사과정 (Part-time, 대한항공 [Korean Air]) | 25S |  |  |
| 김찬호 (Kim, Chan-Ho) | 박사과정 (Part-time, 한화에어로스페이스 [Hanwha Aerospace]) | 25F |  |  |
| 안세준 (Ahn, Se-Joon) | 박사과정 (Part-time, 국방과학연구소 [ADD]) | 26S |  |  |
| 정다인 (Jeong, Da-In) | 석사과정 | 25S | Interceptor guidance; Missile defense; Trajectory optimization |  |
| 한태희 (Han, Tae-Hee) | 석사과정 | 25S | Launch vehicle guidance and control; Missile guidance and control |  |
| 김수민 (Kim, Su-Min) | 석사과정 | 25S | Missile guidance and control |  |
| 박온유 (Park, On-Yu) | 석사과정 | 25F | Missile guidance and control; Optimization-based control |  |
| 김찬영 (Kim, Chan-Young) | 석사과정 | 26S | Guidance and control of reentry vehicle; Computational guidance; Optimization |  |
| 엄승준 (Eom, Seung-Joon) | 석사과정 | 26F | Missile guidance and control; Trajectory optimization |  |
| 김재환 (Kim, Jae-Hwan) | 석사과정 | 26F | Trajectory optimization; Guidance and control of UAVs |  |
| 황준혁 (Hwang, Joon-Hyuk) | 석사과정 | 25S | MUM-T (Mannded-Unmanned Teaming); Autonomous Control of UAVs |  |
| 천지원 (Cheon, Ji-Won) | 석사과정 | 25S | Missile guidance and control; Optimization-based control |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사(Ph.D.) 93줄, 석사(Master) 141줄, 박사후연구원(Postdoctoral Researcher) 1줄, 모두 235줄이다. 연구실은 1989년에 세워졌고 이창훈 교수는 2019년에 합류했으므로, 이 명단에는 교수 합류 전의 구성원이 함께 실려 있다. 같은 사람이 석사와 박사 양쪽에 오른 경우가 있다. 학위 칸의 괄호는 누리집이 이름 앞에 적은 연도 표기(두 자리 연도와 s·d 기호)를 그대로 옮긴 것이다. 진로는 누리집이 이름 뒤에 적은 기관이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 류동영 (Rew, Dong-Young) | Ph.D. (91/96) | 한국항공우주연구원 (KARI) |
| 진재현 (Jin, Jae-Hyun) | Ph.D. (92/97) | 순천대학교 (Suncheon National University) |
| 선병찬 (Sun, Byung-Chan) | Ph.D. (93/97s) | 한국항공우주연구원 (KARI) |
| 이훈구 (Lee, Hungu) | Ph.D. (94/99) | 세트렉아이 (Satrec-Initiative) |
| 류 혁 (Ryu, Hyeok) | Ph.D. (95/00) | 한국항공우주연구원 (KARI) |
| 송은정 (Song, Eun-Jung) | Ph.D. (97/00) | 한국항공우주연구원 (KARI) |
| 이호일 (Lee, Hoil) | Ph.D. (98/01s) | 국방과학연구소 (ADD) |
| 최경용 (Choi, Kyung-Ryong) | Ph.D. (97/02d) |  |
| 허 종 (Hur, Jong) | Ph.D. (96/04) | 한국항공우주산업 (Korea Aerospace Industry) |
| 박봉규 (Park, BongKyu) | Ph.D. (00/04s) | 국방과학연구소 (ADD) |
| 박연묵 (Park, Yonmook) | Ph.D. (00/04s) | 아남전자 (Anam Electronics) |
| 홍영석 (Hong, Young-Seok) | Ph.D. (94/05) | 국방과학연구소 (ADD) |
| 박창수 (Park, Chang-Su) | Ph.D. (98/05) | 한국항공우주연구원 (KARI) |
| 류창경 (Ryoo, Chang-Kyung) | Ph.D. (03/06) | 인하대학교 (Inha University) |
| 이진익 (Lee, Jin-Ik) | Ph.D. (02/06s) | 국방과학연구소 (ADD) |
| 우현욱 (Woo, Hyun-Wook) | Ph.D. (96/07) | 세트렉아이 (Satrec-Initiative) |
| 이현재 (Lee, Hyun-Jae) | Ph.D. (02/07) | 조선대학교 (Chosun University) |
| 전인수 (Jeon, In Soo) | Ph.D. (03/07) | 국방과학연구소 (ADD) |
| 황태원 (Hwang, Tae-Won) | Ph.D. (02/07) | 국방과학연구소 (ADD) |
| 오충석 (Oh, Choong-Seok) | Ph.D. (03/07s) | 한국항공우주연구원 (KARI) |
| 이상종 (Lee, Sang-Jong) | Ph.D. (04/08) | 인하공업전문대학 (Inha Technical College) |
| 서인호 (Seo, In-Ho) | Ph.D. (04s/08s) | 국방과학연구소 (ADD) |
| 김해동 (Kim, Hae-Dong) | Ph.D. (05/09) | 한국항공우주연구원 (KARI) |
| 윤호성 (Youn, Ho-Seong) | Ph.D. (06/09d) |  |
| 김윤환 (Kim, Youn-Hwan) | Ph.D. (04/09s) | LIG넥스원 (LIG Nex1) |
| 박문수 (Park, Moon-Su) | Ph.D. (04/09s) | 한국항공우주연구원 (KARI) |
| 임형철 (Lim, Hyung-Chul) | Ph.D. (03/09s) |  |
| 박영웅 (Park, Young-Woong) | Ph.D. (02/10) |  |
| 상대규 (Sang, Daekyu) | Ph.D. (06/10) | 국방과학연구소 (ADD) |
| 은연주 (Eun, Yeon-Ju) | Ph.D. (05s/10) | 한국항공우주연구원 (KARI) |
| 이광현 (Lee, Kwang-Hyun) | Ph.D. (03/10s) | 한국항공우주연구원 (KARI) |
| 최윤혁 (Choi, Yoon-Hyuk) | Ph.D. (06/10s) | 한국항공우주연구원 (KARI) |
| 이동헌 (Lee, Dong Heon) | Ph.D. (07/10s) | 한국항공우주연구원 (KARI) |
| 김응현 (Kim, Eung-Hyun) | Ph.D. (04/11) | 한국항공우주연구원 (KARI) |
| 명현삼 (Myung, Hyun-Sam) | Ph.D. (05s/11) | 국방과학연구소 (ADD) |
| 박익수 (Park, Ik-Soo) | Ph.D. (06/11) | 국방과학연구소 (ADD) |
| 윤선혜 (Yoon, Seon-Hye) | Ph.D. (08s/11d) |  |
| 신성식 (Shin, Sung-Sik) | Ph.D. (03/11s) | 특허청 (Korean Intellectual Property Office) |
| 최인호 (Choi, Inho) | Ph.D. (06s/11s) |  |
| 최형식 (Choi, Hyoung-Sik) | Ph.D. (07s/11s) | 한국항공우주연구원 (KARI) |
| 이원석 (Lee, Won-Seok) | Ph.D. (07/11s) | 국방과학연구소 (ADD) |
| 용기력 (Yong, Ki-Lyuk) | Ph.D. (05/12) |  |
| 조동현 (Cho, Dong-Hyun) | Ph.D. (07/12) | 한국항공우주연구원 (KARI) |
| 김태훈 (Kim, Tae-Hun) | Ph.D. (07s/12) | 한국항공대학교 (Korea Aerospace University) |
| 김승환 (Kim, Seung-Hwan) | Ph.D. (08s/12) | 국방과학연구소 (ADD) |
| 이용인 (Lee, Yong-In) | Ph.D. (08s/12) | 국방과학연구소 (ADD) |
| 원대연 (Won, Dae-Yeon) | Ph.D. (08/12s) | 국방과학연구소 (ADD) |
| 박정우 (Park, Jung-Woo) | Ph.D. (09/12s) | 국방과학연구소 (ADD) |
| 이일형 (Lee, Il-Hyung) | Ph.D. (05/12s) | 삼성전자 (Samsung Electronics) |
| 정연황 (Jung, Youn-Hwang) | Ph.D. (02/13d) |  |
| 김요섭 (Kim, Yo-Sup) | Ph.D. (04/13) | 국방과학연구소 (ADD) |
| 박봉균 (Park, Bong-Gyun) | Ph.D. (10/13) | 경상국립대학교 (Gyeongsang National University) |
| 이창훈 (Lee, Chang-Hun) | Ph.D. (10/13) | 한국과학기술원 (KAIST) |
| 윤상열 (Yoon, Sang Yol) | Ph.D. (09/13) |  |
| 민병문 (Min, Byoung-Mun) | Ph.D. (04/14) | 인하공업전문대학 (Inha Technical College) |
| 허성식 (Huh, Sung-Sik) | Ph.D. (09/14s) | 한국항공우주연구원 (KARI) |
| 유동일 (You, Dong-Il) | Ph.D. (10/14s) | 국방과학연구소 (ADD) |
| 정연득 (Jeong, Yeon-Deuk) | Ph.D. (10/14s) | 한국항공우주연구원 (KARI) |
| 유동완 (Yoo, Dong-Wan) | Ph.D. (11/14s) | 국방과학연구소 (ADD) |
| 강영신 (Kang, Young-Shin) | Ph.D. (11s/14s) | 한국항공우주연구원 (KARI) |
| 류무용 (Ryu, Moo-Yong) | Ph.D. (12/15s) | 국방과학연구소 (ADD) |
| 양희돈 (Yang, Hee-Don) | Ph.D. (08/15) |  |
| 신효상 (Shin, Hyo-Sang) | Ph.D. (06/16) | 크랜필드 대학교 (Cranfield University) |
| 김현중 (Kim, Hyun-Joong) | Ph.D. (12s/16s) | 국방과학연구소 (ADD) |
| 김상화 (Kim, Sang-Hwa) | Ph.D. (13s/16s) | 국방과학연구소 (ADD) |
| 서민국 (Seo, Min-Guk) | Ph.D. (14/17) | 크랜필드 대학교 박사 후 과정 (Cranfield University, PostDoc) |
| 이웅희 (Lee, Ung-Hui) | Ph.D. (11/17) | 네이버랩스 (Naverlabs) |
| 심상욱 (Shim, Sang-Wook) | Ph.D. (12/18) | 국방과학연구소 (ADD) |
| 조성욱 (Cho, Sung-Wook) | Ph.D. (12/17s) | 니어스랩 (Nearthlab) |
| 신희민 (Shin, Hee-Min) | Ph.D. (13/18) |  |
| 오현식 (Oh, Hyun-Shik) | Ph.D. (13/17s) | 국방과학연구소 (ADD) |
| 이병윤 (Lee, Byung-Yoon) | Ph.D. (13/18) | 니어스랩 (Nearthlab) |
| 이장호 (Lee, Jang-Ho) | Ph.D. (13/17) |  |
| 정지원 (Jeong, Ji-Won) | Ph.D. (14) |  |
| Yogaswara, Y.H. | Ph.D. (14/18) | 인도네시아 국방대학교 (Republic of Indonesia Ministry of Defences) |
| 문정호 (Moon, Jung-Ho) | Ph.D. (11s/19) | 청주대학교 (Cheongju University) |
| 문건희 (Moon, Gun-Hee) | Ph.D. (14/19) | 현대자동차 (Hyundai Motors) |
| 황동혁 (Hwang, Dong-Hyuk) | Ph.D. (14s/19) | 국방과학연구소 (ADD) |
| 안지연 (Ahn, Ji-Yeon) | Ph.D. (15/19) | 국방과학연구소 (ADD) |
| 정영숙 (Jung, Young-Sook) | Ph.D. (15s/19s) | 국방과학연구소 (ADD) |
| 김영삼 (Kim, Young-Sam) | Ph.D. (15s/19s) | 대한항공 (Korean Air) |
| 홍성민 (Hong, Seong-Min) | Ph.D. (15/20) | 국방과학연구소 (ADD) |
| 이동연 (Lee, Dong-Yeon) | Ph.D. (16/21) | 니어스랩 (Nearthlab) |
| 김영철 (Kim, Yeong-Cheol) | Ph.D. (11/21) | 국방과학연구소 (ADD) |
| 송경록 (Song, Kyung-Rok) | Ph.D. (12/21) | 국방과학연구소 (ADD) |
| 김기표 (Kim, Ki-Pyo) | Ph.D. (19/23) | 국방과학연구소 (ADD) |
| 김영원 (Kim, Young-Won) | Ph.D. (19/23) | 위플로 (weflo) |
| 정의택 (Jeong, Eui-Taek) | Ph.D. (21/24) | 국방과학연구소 (ADD) |
| 이상돈 (Lee, Sang-Don) | Ph.D. (21/25) | LIG넥스원 (LIG Nex1) |
| 김보석 (Kim, Boseok) | Ph.D. (22/26) | 한국과학기술원 박사 후 과정 (KAIST, PostDoc) |
| 윤다인 (Yoon, Dain) | Ph.D. (22/26) | 국방과학연구소 (ADD) |
| 정철구 (Jung, Cheol-Goo) | Ph.D. (23/26) | 국방과학연구소 (ADD) |
| 정기욱 (Jung, Ki-Wook) | Ph.D. (23/26) | 한국항공우주연구원 (KARI) |
| 류창경 (Ryoo, Chang-Kyung) | Master (89/91) | 인하대학교 (Inha University) |
| 류 혁 (Ryu, Hyeok) | Master (89/91) | 한국항공우주연구원 (KARI) |
| 유창선 (Yoo, Chang-Sun) | Master (89/91) | 한국항공우주연구원 (KARI) |
| 구훤준 (Koo, Hweon-Jun) | Master (90/92) | 국방과학연구소 (ADD) |
| 위관식 (Wie, Kwan-Sik) | Master (90/92) | 국방과학연구소 (ADD) |
| 진재현 (Jin, Jae-Hyun) | Master (90/92) | 순천대학교 (Suncheon National University) |
| 김영호 (Kim, Young-Ho) | Master (91/93) |  |
| 박봉규 (Park, BongKyu) | Master (91/93) | 국방과학연구소 (ADD) |
| 선병찬 (Sun, Byung-Chan) | Master (91/93) | 한국항공우주연구원 (KARI) |
| 최경용 (Choi, Kyung-Ryong) | Master (91/94) |  |
| 이호일 (Lee, Hoil) | Master (91/94) | 국방과학연구소 (ADD) |
| 김요섭 (Kim, Yo-Sup) | Master (92/94) | 국방과학연구소 (ADD) |
| 이훈구 (Lee, Hungu) | Master (92/94) | 세트렉아이 (Satrec-Initiative) |
| 황인석 (Hwang, In-Seok) | Master (92/94) | 퍼듀 대학교 (Purdue University) |
| 박영웅 (Park, Young-Woong) | Master (93/95) | 한국항공우주연구원 (KARI) |
| 이용인 (Lee, Yong-In) | Master (93/95) | 국방과학연구소 (ADD) |
| 우현욱 (Woo, Hyun-Wook) | Master (94/96) | 세트렉아이 (Satrec-Initiative) |
| 윤형주 (Yoon, Hyung-Joo) | Master (94/96) | 한국항공우주연구원 (KARI) |
| 황태원 (Hwang, Tae-Won) | Master (94/96) | 국방과학연구소 (ADD) |
| 류진훈 (Ryu, Jin-Hoon) | Master (95/97) | 한국항공산업 (KAI) |
| 송은정 (Song, Eun-Jung) | Master (95/97) | 한국항공우주연구원 (KARI) |
| 김선갑 (Kim, Seon-Gap) | Master (96/98) |  |
| 박창수 (Park, Chang-Su) | Master (96/98) | 한국항공우주연구원 (KARI) |
| 김제겸 (Kim, Je-Gyum) | Master (97/99) | Edu Expert |
| 황재원 (Hwang, Jae-Won) | Master (97/99) | 삼성전자 (Samsung Electronics) |
| 송인수 (Song, In-Soo) | Master (98/00) | 리얼리티 리블렉션 (Reality Reflection) |
| 심재완 (Shim, Jae-Wan) | Master (99s/00d) |  |
| 구근모 (Koo, Keun-Mo) | Master (98/01) | 더보스턴컨설팅그룹 (The Boston Consulting Group) |
| 김종한 (Kim, Jong-Han) | Master (99/01) | 경희대학교 (Kyunghee University) |
| 지효선 (Chi, Hyo-Seon) | Master (99/01) | 국방과학연구소 (ADD) |
| 최한림 (Choi, Han-Lim) | Master (00/02) | 한국과학기술원 (KAIST) |
| 명현삼 (Myung, Hyun-Sam) | Master (01/03) | 국방과학연구소 (ADD) |
| 오충석 (Oh, Choong-Seok) | Master (01/03) | 한국항공우주연구원 (KARI) |
| 이기훈 (Lee, Ki-Hoon) | Master (01/03) |  |
| 정재우 (Jung, Jae-Woo) | Master (01/03) | 삼성 SDS |
| 성호준 (Sung, Ho-Joon) | Master (03/03d) |  |
| 김근태 (Kim, Kun-Tae) | Master (02/04) |  |
| 김윤환 (Kim, Youn-Hwan) | Master (02/04) | LIG넥스원 (LIG Nex1) |
| 이수진 (Lee, Soo-Jin) | Master (02/04) | 국방과학연구소 (ADD) |
| 은연주 (Eun, Yeon-Ju) | Master (02/04s) | 한국항공우주연구원 (KARI) |
| 이정신 (Lee, Jung-Shin) | Master (02/05) | 국방과학연구소 (ADD) |
| 권혁훈 (Kwon, Hyuck Hoon) | Master (03/05) | LIG넥스원 (LIG Nex1) |
| 오세붕 (Oh, Se-Boung) | Master (03/05) |  |
| 이일형 (Lee, Il-Hyung) | Master (03/05) | 삼성전자 (Samsung Electronics) |
| 조성봉 (Cho, Sung-Bong) | Master (03/05) | 국방과학연구소 (ADD) |
| 한수철 (Han, Su-Cheol) | Master (03/05) |  |
| 나채진 (Na, Chae-Jin) | Master (03s/05s) |  |
| Kannan, Somasundar | Master (03s/05s) |  |
| 김부성 (Kim, Boo-Sung) | Master (04/06) |  |
| 신효상 (Shin, Hyo-Sang) | Master (04/06) | 크랜필드 대학교 (Cranfield University) |
| 장대수 (Jang, Dae-Su) | Master (04/06) | 대한항공 (Korean Air) |
| 조신제 (Cho, Shin-Je) | Master (04/06) | 대한항공 (Korean Air) |
| 최윤혁 (Choi, Yoon-Hyuk) | Master (04/06) | 국방과학연구소(ADD) |
| Farook, Shashi Khan | Master (04s/06s) |  |
| 조동현 (Cho, Dong-Hyun) | Master (04s/06s) | 한국항공우주연구원 (KARI) |
| 김영삼 (Kim, Young-Sam) | Master (05/07) | 대한항공 (Korean Air) |
| 이동헌 (Lee, Dong Heon) | Master (05/07) | 한국항공우주연구원 (KARI) |
| 이원석 (Lee, Won-Seok) | Master (05/07) | 국방과학연구소 (ADD) |
| 홍진성 (Hong, Jin-Sung) | Master (05/07) | 국방과학연구소 (ADD) |
| 김태훈 (Kim, Tae-Hun) | Master (05/07s) | 한국항공대학교 (Korea Aerospace University) |
| 김광연 (Kim, Kwang-Yeon) | Master (06/08) | 퍼듀 대학교 박사과정 (Purdue University, Ph.D. Course) |
| 백광열 (Baek, Kwang-Yul) | Master (06/08) | 한국항공우주연구원 (KARI) |
| 원대연 (Won, Dae-Yeon) | Master (06/08) | 국방과학연구소 (ADD) |
| 이동진 (Lee, Dong-Jin) | Master (06/08) | 한서대학교 (Hanseo University) |
| 이영구 (Lee, Young-Gu) | Master (06/08) |  |
| 노은정 (Roh, Eun-jung) | Master (06/08s) | 대한항공 (Korean Air) |
| 임승한 (Lim, Seung-Han) | Master (07/09) | 국방과학연구소 (ADD) |
| 박정우 (Park, Jung-Woo) | Master (07/09) | 국방과학연구소 (ADD) |
| 이지석 (Lee, Ji-Suk) | Master (07/09) | 모션디바이스 (Motion Device) |
| 최대형 (Choi, Dae-hyung) | Master (07/09) |  |
| 허성식 (Huh, Sung-Sik) | Master (07/09) | 한국항공우주연구원 (KARI) |
| 박봉균 (Park, Bong-Gyun) | Master (08/10) | 경상국립대학교 (Gyeongsang National University) |
| 오현동 (Oh, Hyon-Dong) | Master (08/10) | 울산과학기술대학교 (UNIST) |
| 유동일 (You, Dong-Il) | Master (08/10) | 국방과학연구소 (ADD) |
| 이창훈 (Lee, Chang-Hun) | Master (08/10) | 한국과학기술원 (KAIST) |
| 정연득 (Jeong, Yeon-Deuk) | Master (08/10) | 한국항공우주연구원 (KARI) |
| 장대성 (Jang, Dae-Sung) | Master (08/10d) | 한국항공대학교 (Korea Aerospace University) |
| 류선미 (Ryu, Sun-Mee) | Master (09/11) | LIG넥스원 (LIG Nex1) |
| 문상우 (Moon, Sang-Woo) | Master (09/11) | 마이크로소프트 (Microsoft Research) |
| 안종선 (Ahn, Jong-Sun) | Master (09/11) | KAIST 전산학부 |
| 유동완 (Yoo, Dong-Wan) | Master (09/11) | 국방과학연구소 (ADD) |
| 이동협 (Lee, Dong-Hyup) | Master (09/11) |  |
| 이웅희 (Lee, Ung-Hui) | Master (09/11) | 네이버랩스 (Naverlabs) |
| 김금성 (Kim, Keum-Seong) | Master (10/12) | 삼성전자DS (Samsung Electronics Device Solution) |
| 심상욱 (Shim, Sang-Wook) | Master (10/12) | 국방과학연구소 (ADD) |
| 오은미 (Oh, Eun-Mi) | Master (10/12) | 한국항공우주연구원 (KARI) |
| 조성욱 (Cho, Sung-Wook) | Master (10/12) | 니어스랩 (Nearthlab) |
| 신희민 (Shin, Hee-Min) | Master (11/13) |  |
| 이병윤 (Lee, Byung-Yoon) | Master (11/13) | 니어스랩 (Nearthlab) |
| 이상협 (Lee, Sang-Hyup) | Master (11/13) | 현대자동차 (Hyundai Motors) |
| 황연하 (Hwang, Yeonha) | Master (11/13s) | 미국 유학 |
| 김정운 (Kim, Jeong-Woon) | Master (12/14) | 국방과학연구소 (ADD) |
| 문건희 (Moon, Gun-Hee) | Master (12/14) | 현대자동차 (Hyundai Motors) |
| 서민국 (Seo, Min-Guk) | Master (12/14) | 크랜필드 대학교 박사 후 과정 (Cranfield University, PostDoc) |
| 전병주 (Jeon, Byoung-Joo) | Master (12/14) | 크랜필드 대학교 박사과정 (Cranfield University, Ph.D. Course) |
| 정지원 (Jeong, Ji-Won) | Master (12/14) |  |
| 이다솔 (Lee, Da-Sol) | Master (13/15) |  |
| 이수관 (Lee, Su-Gwan) | Master (13/15) |  |
| 이해인 (Lee, Hae-In) | Master (13/15) | 크랜필드 대학교 박사 후 과정(Cranfield University, PostDoc) |
| 홍성민 (Hong, Seong-Min) | Master (13/15) | 국방과학연구소 (ADD) |
| 박현주 (Park, Hyunju) | Master (13s/15s) | 국방과학연구소 (ADD) |
| 이석주 (Lee, SJ) | Master (13s/15s) |  |
| 김영원 (Kim, Young-won) | Master (14/16) | 위플로 (weflo) |
| 김윤영 (Kim, Yun-Young) | Master (14/16) | LIG넥스원 (LIG Nex1) |
| 박성연 (Park, SungYeon) | Master (14/16) |  |
| 백창훈 (Baek, Chang hun) | Master (14/16) |  |
| 송한준 (Song, Hanjun) | Master (14/16) |  |
| 이동연 (Lee, Dong-Yeon) | Master (14/16) | 니어스랩 (Nearthlab) |
| 이준용 (Lee, Jun-Yong) | Master (14/16) | 니어스랩 (Nearthlab) |
| 신인선 (Shin, Insun) | Master (14s/16s) | 한화시스템 (HanwhaSystem) |
| 유하람 (You, Haram) | Master (15/17) |  |
| 정석우 (Jung, Seokwoo) | Master (15/17) |  |
| 이한섭 (Lee, Hanseob) | Master (15/17) | 니어스랩 (Nearthlab) |
| 김민기 (Kim, Min-Ki) | Master (15/16s) | 공군사관학교 (Republic of Korea Air Force Academy) |
| 한승엽 (Han, Seungyeop) | Master (15/17) | 세트렉아이 (Satrec-Initiative) |
| 황민철 (Hwang, Minchul) | Master (15/17) | 한화종합연구소 (Hanwha) |
| 변세범 (Byun, Se-Beom) | Master (15s/18) | 풍산 (Poongsan) |
| 조민현 (Cho, Min-Hyun) | Master (16/18) | 퍼듀 대학교 박사과정 (Purdue University, Ph.D. Course) |
| 박재민 (Park, Jaemin) | Master (17/19) |  |
| 배지훈 (Bai, Ji Hoon) | Master (17/19) | 니어스랩 (Nearthlab) |
| 노희건 (Roh, Heekun) | Master (17/19) | 메사추세츠 공과대학교 박사과정 (MIT, Ph.D. Course) |
| 윤성진 (Yoon, Sung-Jin) | Master (17s/19s) | 한화종합연구소 (Hanwha) |
| 오영재 (Oh, Young-Jae) | Master (17s/19s) | 한국항공우주연구원 (KARI) |
| 이상돈 (Lee, Sang-Don) | Master (19/21) | LIG넥스원 (LIG Nex1) |
| 김보석 (Kim, Boseok) | Master (20/22) | 한국과학기술원 박사 후 과정 (KAIST, PostDoc) |
| 윤다인 (Yoon, Dain) | Master (20/22) | 국방과학연구소 (ADD) |
| 정철구 (Jung, Cheol-Goo) | Master (21/23) | 국방과학연구소 (ADD) |
| 정기욱 (Jung, Ki-Wook) | Master (21/23) | 한국항공우주연구원 (KARI) |
| 나경미 (Na, Kyung-Mi) | Master (21/23) | 조지아 공과대학교 박사과정 (Georgia Tech, Ph.D. Course) |
| 박종찬 (Park, Jong-Chan) | Master (22/24) | KAIST FDCL |
| 이선호 (Lee, Sun-Ho) | Master (20/24) | 국방과학연구소 (ADD) |
| 전광규 (Jeon, Koang-Kyu) | Master (22/24) | LIG넥스원 (LIG Nex1) |
| 김태영 (Kim, Tae-Young) | Master (23/25) |  |
| 김다휘 (Kim, Da-Hwi) | Master (23/25) | 델프트 공과대학교 박사과정 (TU Delft, Ph.D. Course) |
| 신민재 (Shin, Minjae) | Master (23/25) | 한국항공우주연구원 (KARI) |
| 김현재 (Kim, Hyeonjae) | Master (24/26) | 한화에어로스페이스 (Hanwha Aerospace) |
| 강승진 (Kang, Seung-Jin) | Master (24/26) |  |
| 안세환 (An, Se-Hwan) | Master (24/26) | KAIST FDCL |
| 이유정 (Lee, You-Jeong) | Master (24/26) | KAIST FDCL |
| 이흔재 (Lee, Heun-Jae) | Master (24/26) | KAIST FDCL |
| 강경태 (Kang, Kyeong-Tae) | Master (24/26) | 국방과학연구소 (ADD) |
| 王鹏宇 (Pengyu Wang) | Postdoctoral Researcher (22/25) | Harbin Institute of Technology (Associate Professor) |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지에서 연도가 2021–2026년인 항목 217건이다. 책 1권, 국제 학술지 논문 69편, 국제 학술대회 논문 50편, 국내 학술지 논문 17편, 국내 학술대회 논문 80편이고, 연도별로 2026년 13, 2025년 60, 2024년 38, 2023년 28, 2022년 43, 2021년 35건이다. 이 목록은 이창훈 교수의 논문 목록이어서 다른 기관 연구진이 이끈 공동 연구도 들어 있다. 누리집은 교신저자를 밑줄로 표시하며, 여기서는 그 이름 뒤에 *를 붙였다. 누리집이 권·쪽 없이 「Accepted for Publication」으로 적은 학술지 논문은 「게재 승인」으로 표시했고, 권·쪽이 함께 적힌 2021년 1편은 누리집 표기 그대로 두었다. 국내 학술지·학술대회 논문은 누리집이 한국어로 쓴 논문이라고 밝히며, 제목은 누리집 표기를 따랐다.[^pubs]

**2026**

- K. W. Jung, Y. W. Kim, S. W. Shim and C. H. Lee\*. "A Guidance Design Framework for Arbitrary Target Maneuvers and Interceptor Strategies". *IEEE Transactions on Aerospace and Electronic Systems, 2026 (게재 승인)*.
- J. Park, Y. J. Lee, S. H. An, C. H. Lee\*, H. S. Choi, and S. Shin. "Enhancing Autopilot Performance via Zero Augmentation in a Generalized Three-Loop Structure". *International Journal of Control Automation and Systems, 2026 (게재 승인)*.
- Q. Li, P. Wang\*, Y. Guo, N. Cho, and C. H. Lee. "Time-to-Go Inversion Guidance for Field-of-View Limited Impact Angle and Time Control". *IEEE Transactions on Aerospace and Electronic Systems, 2026 (게재 승인)*.
- K. K. Jeon, K. W. Jung, and C. H. Lee\*. "A Two-Gain Acceleration-Feedback Three-Loop Autopilot for Mitigating Guidance-Control Loop Divergence". *International Journal of Aeronautical and Space Sciences, 2026 (게재 승인)*.
- K. M. Na and C. H. Lee\*. "Nonlinear Optimal Control for Flight Vehicles using Neural Operators and Physics-Informed Neural Networks". *Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, 2026 (게재 승인)*.
- C. G. Jung, S. An, C. H. Lee\*, H. S. Choi, and S. Shin. "Real-Time Entry Guidance Framework via an Optimization Oriented Quadratic Programming Formulation". *Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, 2026 (게재 승인)*.
- E. T. Jeong, D. Yoon, and C. H. Lee\*. "Adaptive Path-Following for Quadrotors via Parameterized-Policy MPPI Control". *International Journal of Aeronautical and Space Sciences, 2026 (게재 승인)*.
- J. I. Jang and C. H. Lee\*. "Customized Interior-Point Methods Solver for Embedded Real-Time Convex Optimization". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 62, 2026, pp. 7896-7913*.
- M. J. Tahk, O. Kang, C. H. Lee\*, H. K. Kim, and S. H. Seo. "Guidance Techniques for Canard-Equipped Artillery Shells Based on Trajectory Prediction". *International Journal of Aeronautical and Space Sciences, Vol. 27, 2026, pp. 3502-3523*.
- N. Paul, K. W. Jung, and C. H. Lee\*. "Hawk-Inspired Variable-Speed Guidance Law with Integrated Collision Avoidance for Intelligent Inerceptors". *Journal of Guidance, Control, and Dynamics, Vol. 49, No. 6, 2026, pp. 1838-1850*.
- O. Kang, B. Kim, C. H. Lee\*, and S. W. Shim. "Time-to-Go Polynomial Guidance Laws under Off-Axis Seeker Constraints". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 62, 2026, pp. 3153-3167*.
- C. G. Jung and C. H. Lee\*. "Real-Time Feasible Optimal Deployment Strategy for Carrier-Type Missiles in Multi-Target Engagements". *International Journal of Aeronautical and Space Sciences, Vol. 27, 2026, pp. 3259-3272*.
- B. Kim, J. I. Jang, H. Lee, and C. H. Lee\*. "Receding-Horizon Midcourse Guidance for Variable-Flow Ducted Rocket Missiles". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 62, 2026, pp. 285-302*.

**2025**

- H. G. Sung, C. H. Lee, B. J. Lee, K. B. Ahn, H. J. Lee, K. H. Lee, and H. L. Kim, Rocket Engineering, HongReung, 2025
- D. Yoon, K. W. Jung, E. T. Jeong, and C. H. Lee\*. "Uncertainty-Aware Adaptive Sampling in MPPI for Robust UAV Path-Following". *Aerospace Science and Technology, Vol. 168, 111126, 2025, pp. 1-11*.
- C. G. Jung and C. H. Lee\*. "Semi-Analytical Guidance for Velocity Maximization of Gliding Vehicles Using Proportional Navigation and Sparse Waypoints". *Optimal Control Applications and Methods, Vol. 46, No. 6, 2025, pp. 2829-2842*.
- J. Park and C. H. Lee\*. "Polynomial Based Impact-Time-Control Guidance Law Integrating Optimal Characteristics". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 6, 2025, pp. 17703-17716*.
- K. W. Jung, S. D. Lee, C. G. Jung, and C. H. Lee\*. "Optimal Landing Guidance of Reusable Launch Vehicles with Dual-convex Optimization". *International Journal of Control, Automation, and Systems, Vol. 23, No. 8, 2025, pp. 2198-2218*.
- C. G. Jung, K. W. Jung, B. Kim, O. Kang, and C. H. Lee\*. "Look-angle-based Agile Turn Guidance for All-aspect Target Interception". *Aerospace Science and Technology, Vol. 166, 110572, 2025, pp. 1-13*.
- S. He\*, H. Luo, C. H. Lee, H. S. Shin, A. Tsourdos. "Review of Data-Driven Computational Guidance for Unmanned Aerospace Vehicles". *Progress in Aerospace Sciences, Vol. 157, 101129, 2025, pp. 1-17*.
- K. W. Jung, and C. H. Lee\*. "An Impact Point Guidance for a Launch Vehicle with Aerodynamics Control". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 5, 2025, pp. 13565-13579*.
- Z. Liu, Z. Wu, T. Tabuchi, H. T. Nguyen, C. H. Lee, and S. He\*. "A Data-Driven Learning Guidance Strategy for Target Interception with Terminal Time Constraint". *Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, Vol. 239, No. 13, 2025, pp. 1610-1626*.
- J. Bae, J. H. Bai, B. Y. Lee, J. Y. Lee, and C. H. Lee\*. "On the Reachability of 3-Dimensional Paths with a Prescribed Curvature Bound". *Automatica, Vol. 178, 112359, 2025, pp. 1-9*.
- H. Luo, C. H. Lee, C. Li, and S. He\*. "Generative Adversarial Imitation Learning-based Continuous Learning Computational Guidance". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 3, 2025, pp. 6809-6821*.
- D. Yoon, K. M. Na, D. W. Lee, C. H. Lee\*, and H. C. Bang. "Fault-Tolerant Control Allocation in Coaxial Dodecacopter Using Quadratic Programming-based on ACS Analysis". *Control Engineering Practice, Vol. 156, 106235, 2025, pp. 1-10*.
- S. D. Lee, K. W. Jung, and C. H. Lee\*. "Convex Optimization based Landing Guidance and Control Algorithms for Reusable Orbital Rockets". *International Journal of Aeronautical and Space Sciences, Vol. 26, 2025, pp. 1890-1911*.
- H. Luo, Z. Liu, T. Jin, C. H. Lee, and S. He\*. "Computational Predictor-Corrector Homing Guidance for Constrained Impact". *Journal of Guidance, Control, and Dynamics, Vol. 48, No. 6, 2025, pp. 1366-1380*.
- C. G. Jung, B. Kim, and C. H. Lee\*. "Non-iterative Convex Programming-based Optimal Guidance with Field-of-View and Acceleration Limits". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 2, 2025, pp. 5477-5487*.
- B. Kim, M. Shin, C. H. Lee\*, J. W. Kim, Y. K. Kim, and I. Y. Kang. "Guidance Scheme for Gun-Launched Gliding Guided Projectiles". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 2, 2025, pp. 1630-1647*.
- P. Wang, C. H. Lee\*, N. Cho, and B. Wie. "Generalized Time-to-Go Inversion Guidance with Impact Time and Angle Constraints". *Journal of Guidance, Control, and Dynamics, Vol. 48, No. 3, 2025, pp. 555-574*.
- J. Bae, B. Kim, and C. H. Lee\*. "A New Trust-Region Constraint Method for Sequential Convex Programming Framework for Entry Guidance". *International Journal of Aeronautical and Space Sciences, Vol. 26, 2025, pp. 1216-1233*.
- J. Park, E. T. Jeong, K. W. Jung, and C. H. Lee\*. "Proportional Navigation Guidance with Virtual Targeting for Impact-Angle-Control". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 61, No. 1, 2025, pp. 457-472*.
- Y. K. Lee, H. G. Sung\*, and C. H. Lee. "Performance Analysis of a Ducted Rocket under Various Flight Conditions". *International Journal of Aeronautical and Space Sciences, Vol. 26, 2025, pp. 674-687*.
- D. I. Jeong, K. W. Jung, S. H. An, C. H. Lee\*. "Multivariable Sensitivity Analysis and Real-Time Navigation Constant Updating for Missile Guidance Using Automatic Differentiation". *The 13th International Conference on Robot Intelligence Technology and Applications, RiTA2025, London, UK, 2025*.
- T. Han, K. W. Jung, K. M. Na, and C. H. Lee\*. "Aerodynamic Model Estimation using Dynamics-Embedded Neural ODE". *The 13th International Conference on Robot Intelligence Technology and Applications, RiTA2025, London, UK, 2025*.
- K. W. Jung, H. J. Kim, M. J. Tahk, and C. H. Lee\*. "Feedback Landing Guidance for Reusable Launch Vehicle in Atmosphere based on Homing Guidance". *76th International Astronautical Congress, Sydney, Australia, 2025*.
- H. J. Lee, B. Kim, C. H. Lee\*, M. J. Tahk, C. Lee, B. G. Kwon, and K. K. Jeon. "Mid-Course Trajectory Optimization for Variable-Flow Ducted Rocket Missile under Radar Detection Angle Constrain". *4th International Conference on High-Speed Vehicle Science & Technology, Tours, France, 2025*.
- Y. J. Lee, D. Yoon, S. H. An, C. H. Lee\*, H. S. Choi, and S. C. Shin. "KL-Divergence Model Predictive Control for On–Off Thrusters in Spaceplane". *4th International Conference on High-Speed Vehicle Science & Technology, Tours, France, 2025*.
- S. H. An, C. G. Jung, C. H. Lee\*, H. S. Choi, and, Y. D. Jeong. "Adaptive Multi-Command TAEM Guidance Using a Cascade Predictor-Corrector Scheme". *4th International Conference on High-Speed Vehicle Science & Technology, Tours, France, 2025*.
- M. J. Tahk\*, O. Kang, B. Kim, and C. H. Lee. "Trajectory Prediction for Spin-Stabilized Guided Shells with Canards". *11th European Conference for AeroSpace Sciences (EUCASS 2025), Rome, Italy, 2025*.
- M. J. Tahk\*, B. Kim, O. Kang, and C. H. Lee. "Tracking Algorithms for Optimal Trajectories Based on Augmented Pursuit Guidance". *11th European Conference for AeroSpace Sciences (EUCASS 2025), Rome, Italy, 2025*.
- J. Jang, D. H. Kim, and C. H. Lee\*. "Powered Descent Guidance via Sequential Convex Programming with Constraint Function Design". *2025 IEEE Aerospace Conference, Montana, USA, 2025*.
- D. H. Kim, J. Jang, and C. H. Lee\*. "Rocket Landing Guidance with Linearized Model Predictive Control via Second-order Cone Programming". *2025 IEEE Aerospace Conference, Montana, USA, 2025*.
- K. W. Jung, J. I. Jang, J. C. Park, C. H. Lee\*, T. S. Kuk, and J. W. Lee. "Computational Guidance and Control Algorithm for Powered-Descent Guidance of RLV-TD". *Journal of The Korean Society for Aeronautical and Space Sciences, Vol. 53, No. 11, 2025, pp. 1147-1157*.
- C. G. Jung, C. H. Lee\*, M. J. Tahk, J. H. Jeong, H. J. Jo, and H. K. Na. "A Study on Target/Non-target Identification and Projectile Classification Algorithms Using Counter-battery Radar Measurements". *Journal of Institute of Control, Robotics and Systems, Vol. 31, No. 9, 2025, pp. 1059-1072*.
- O. Kang, B. Kim, C. H. Lee\*, S. W. Park, Y. K. Lee, J. W. Kim, and H. J. Park. "Study on Guidance and Control Algorithms for Gun-Launched Gliding Guided Munition". *Journal of The Korean Society for Aeronautical and Space Sciences, Vol. 53, No. 9, 2025, pp. 907-918*.
- M. Shin, C. G. Jung, and C. H. Lee\*. "Stability and Robustness Analysis of Reference Drag-following Reentry Guidance". *Journal of Institute of Control, Robotics and Systems, Vol. 31, No. 6, 2025, pp. 701-703*.
- J. C. Park, K. W. Jung, C. H. Lee\*, and H. S. Choi. "Autopilot Design and Analysis for Hypersonic Vehicles Using Nonlinear Adaptive Control Approaches". *Journal of Institute of Control, Robotics and Systems, Vol. 30, No. 12, 2025, pp. 1329-1339*.
- S. M. Bang, M. Shin, T. H. Kim\*, C. H. Lee, H. S. Choi. "Entry Trajectory Generation Using Reference Drag Acceleration and Range-based Parameter Design Method". *Journal of Institute of Control, Robotics and Systems, Vol. 30, No. 12, 2025, pp. 1347-1359*.
- C. G. Jung, O. R. Kang, E. T. Jeong, C. H. Lee\*, I. H. Kim, C. S. Kim, and S. T. Lee. "Radar Cross Section Analysis of Long-Range Artillery Engagement Debris using Satellite Break-up Model". *Journal of Institute of Control, Robotics and Systems, Vol. 30, No. 10, 2025, pp. 1179-1190*.
- O. Kang, J. Park, and C. H. Lee. "Polynomial Guidance Laws with Off-Axis Seeker Field-of-View Constraints". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- S. H. An, Y. J. Lee, C. H. Lee\*, H. S. Choi, and S. C. Shin. "Predictive Guidance and Control for a Reentry Vehicles". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- T. Han, S. M. Kim, and C. H. L\*ee\*. "A Study on Autonomous Air Combat Maneuvering Policy Using Deep Reinforcement Learning". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- D. I. Jeong, K. W. Jung, S. H. An, and C. H. Lee\*. "Sensitivity Analysis and Navigation Constant Estimation for Missile Guidance Using Automatic Differentiation". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- H. J. Kim, K. W. Jung, and C. H. Lee\*. "Fault-Tolerant Control of Reusable Launch Vehicles Using Attainable Control Sets". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- J. W. Shim, J. Jang, C. H. Lee\*, and J. I. Baek. "Predictor-Corrector Based Optimal Guidance for Boost-back Burn Phase of Reusable Launch Vehicles". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- C. H. Lee\*, M. J. Tahk, H. J. Yoon, and J. H. Kim. "Requirement Analysis of Guidance and Control Algorithm for Trajectory Correction Fuze". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- S. M. Kim, K. W. Jung, and C. H. Lee\*. "Optimal ZEM based Midcourse Guidance Using Ballistic Trajectory Prediction". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- K. T. Kang and C. H. Lee\*. "Predictor-Corrector Entry Guidance of Capsule Vehicle with Rapid Trajectory Propagation". *The Korea Society for Aeronautical and Space Sciences 2025 Fall Conference, 2025*.
- J. W. Shim and C. H. Lee\*. "Optimization and Analysis of Reusable Launch Vehicle First Stage Recovery". *The Society for Aerospace System Engineering 2025 Fall Conference, 2025*.
- J. Park, C. H. Lee\*, and H. S. Choi. "Nonlinear Autopilot Design for Hypersonic Flight Vehicles". *The Society for Aerospace System Engineering 2025 Fall Conference, 2025*.
- J. Jang, D. W. Kim, K. W. Jung, and C. H. Lee\*. "Design and Analysis of Guidance Algorithm for Reusable Launch Vehicle’s 1st Stage Recovery". *The Korea Society for Aeronautical and Space Sciences 2025 Space Conference, 2025*.
- Y. J. Lee, S. H. An, C. H. Lee\*, and H. S. Choi. "Control Allocation Considering Quantization Error in Hybrid Actuation Systems". *The Korea Society for Aeronautical and Space Sciences 2025 Space Conference, 2025*.
- J. W. Shim and C. H. Lee\*. "Trajectory Optimization of Mid-Course Guidance for Reusable Launch Vehicles". *The Korea Society for Aeronautical and Space Sciences 2025 Space Conference, 2025*.
- K. T. Kim and C. H. Lee\*. "Development Trends of Chinese Commercial Reusable Launch Vehicles". *The Korea Society for Aeronautical and Space Sciences 2025 Space Conference, 2025*.
- J. Jang and C. H. Lee\*. "Powered Descent Guidance for a Reusable Launch Vehicle Demonstrator Using a Customized Convex Optimization Solver". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- S. H. An, C. G. Jung, and C. H. Lee\*. "TAEM Guidance for Unmanned Space Vehicle using Adaptive Heading Alignment Cone". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- S. J. Kang, K. W. Jung, C. G. Jung, and C. H. Lee\*. "Attitude Control of Reusable Launch Vehicle Using Finite-Time Control". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- H. J. Kim, K. W. Jung, and C. H. Lee\*. "Acceleration Control Algorithm for Reusable Launch Vehicle during Landing Burn". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- C. G. Jung and C. H. Lee\*. "Sensitivity Analysis of Disturbance in Terminal Homing Guidance Based on Navigation Gain". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- Y. J. Lee, D. Yoon, and C. H. Lee\*. "Analysis of Connections between Nonlinear Adaptive Control Laws". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- O. Kang, C. H. Lee\*, and M. J. Tahk. "Time-to-go polynomial guidance laws with Off-Axis seeker". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.
- H. J. Lee, B. Kim, C. H. Lee\*, C. Lee, B. G. Kwon, and K. K. Jeon. "Mid-Course Trajectory Optimization for Variable-Flow Ducted Rocket Missiles under Radar Detection Angle Constraint". *The Korea Society for Aeronautical and Space Sciences 2025 Spring Conference, 2025*.

**2024**

- C. G. Jung and C. H. Lee\*. "Optimal Impact Angle Control Guidance Law Considering Aerodynamic Drag". *Journal of Guidance, Control, and Dynamics, Vol. 47, No. 11, 2024, pp. 2435-2443*.
- C. G. Jung, P. Wang, and C. H. Lee\*. "Optimal Impact-angle Constrained Guidance with Barrier Constraint". *Proceedings of the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, Vol. 238, No. 11, 2024, 1055-1067*.
- B. Kim and C. H. Lee\*. "Firing Command Generation for Close-In-Weapon System to Intercept High-Speed Targets". *International Journal of Aeronautical and Space Sciences, Vol. 25, 2024, pp. 1524-1535*.
- J. Kim, C. H. Lee, and M. Y. Li\*. "A Study on the Weapon Target Assignment Problem Considering Heading Error". *International Journal of Aeronautical and Space Sciences, Vol. 25, No. 7, 2024, pp. 1105-1120*.
- D. Yoon and C. H. Lee\*. "A Disturbance Rejection Control for Urban Air Mobility using Artificial Sensor-based Gaussian Process Regression". *Aerospace Science and Technology, Vol. 147, 2024, pp. 1-11*.
- H. Kang, P. Wang\*, C. H. Lee, and S. Song. "Impact Time and Angle Guidance Considering Aerodynamic Drag". *Journal of the Franklin Institute, Vol. 361, No. 6, 2024, pp. 1-20*.
- E. T. Jeong, P. Wang, S. He, T. H. Kim, and C. H. Lee\*. "Heading Error Shaping Guidance Laws Using Generalized Finite-Time Convergence Error Dynamics". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 60, No. 3, 2024, pp. 3192-3208*.
- Y. Liu, P. Wang\*, C. H. Lee, and R. Toth. "Attitude Takeover Control for Noncooperative Space Targets Based on Gaussian Processes with Online Model Learning". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 60, No. 3, 2024, pp. 3050-3066*.
- M. J. Tahk, E. T. Jeong, C. H. Lee\*, and S. J. Yoon. "Attitude Hold Proportional Navigation Guidance for Interceptors with Off-axis Seeker". *Journal of Guidance, Control, and Dynamics, Vol. 47, No. 5, 2024, pp. 1015-1025*.
- J. Bae, B. Kim, and C. H. Lee\*. "New Adaptive Mesh Refinement Strategy for Entry Guidance via Sequential Convex Programming". *Journal of Guidance, Control, and Dynamics, Vol. 47, No. 4, 2024, pp. 711-727*.
- K. P. Kim and C. H. Lee\*. "Adaptive Weight Model Predictive Path Integral Control for Multi-constrained Missile Guidance". *Journal of Aerospace Information Systems, Vol. 21, No. 4, 2024, pp. 305-322*.
- P. Wang, C. H. Lee\*, Y. Liu, and M. J. Tahk. "Nonlinear Three-Dimensional Guidance for Impact Time and Angle Control with Field-of-View Constraint". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 60, No. 1, 2024, pp. 264-279*.
- K. M. Na and C. H. Lee\*. "Identification of Uncertain Parameter in Flight Vehicle Using Physics-Informed Deep Learning". *Journal of Aerospace Information Systems, Vol. 21, No. 2, 2024, pp. 152-167*.
- S. D. Lee, K. W. Jung, and C. H. Lee\*. "Mission Profile Analysis of Point-to-Point Rocket Cargo Transportation System using Trajectory Optimization". *Journal of Spacecraft and Rockets, Vol. 61, No. 1, 2024, pp. 263-273*.
- D. H. Kim, M. J. Tahk, M. Shin, J. Park, K. W. Jung, and C. H. Lee\*. "Attitude Estimation of Launch Vehicles Using GPS/INS and Periodic Yaw Maneuvers". *2024 Asia-Pacific International Symposium on Aerospace Technology (APISAT 2024), Adelade, Australia, 2024*.
- D. Yoon and C. H. Lee\*. "Disturbance Rejection Path-following Guidance Using Gaussian Process Regression via Kalman Filtering for Unmanned Aerial Vehicle". *2024 Asia-Pacific International Symposium on Aerospace Technology (APISAT 2024), Adelade, Australia, 2024*.
- J. Park, K. W. Jung, M. J. Tahk, D. H. Kim, H. S. Choi, Y. Jung, T. H. Kim, and C. H. Lee\*. "Enhanced Longitudinal Controller of Hypersonic Vehicles based on Nonlinear Dynamic Inversion with Nonlinear Disturbance Observer". *2024 Asia-Pacific International Symposium on Aerospace Technology (APISAT 2024), Adelade, Australia, 2024*.
- K. W. Jung and C. H. Lee\*. "Downrange Control Guidance for Reentry Burn of Reusable Launch Vehicle". *34th Congress of the International Council of the Aeronautical Sciences (ICAS 2024), Florence, Italy, 2024*.
- C. G. Jung, C. H. Lee\*, and M. J. Tahk. "Trajectory Optimization for Long-range Air-launched Gliding Vehicles Using Convex Programming". *34th Congress of the International Council of the Aeronautical Sciences (ICAS 2024), Florence, Italy, 2024*.
- J. Jang, C. H. Lee\*, and S. He. "Convex Programming Approach of Robust Powered Descent Guidance Through Dynamic Tube MPC". *34th Congress of the International Council of the Aeronautical Sciences (ICAS 2024), Florence, Italy, 2024*.
- M. Shin, M. J. Tahk, B. Kim, and C. H. Lee\*. "Pursuit-based Long-range Air-to-air Missile Midcourse Guidance Robust to Changes in the Predicted Impact Point". *34th Congress of the International Council of the Aeronautical Sciences (ICAS 2024), Florence, Italy, 2024*.
- P. Wang, H. Kang, and C. H. Lee\*. "Field-of-View Limited Guidance Law for Maneuvering Targets Using Relative Virtual Frame Formulation". *2024 CEAS EuroGNC Conference, Bristol, UK, 2024*.
- K. M. Na and C. H. Lee\*. "Physics-Informed Deep Learning Approach to Solve Optimal Control Problem". *AIAA SciTech Forum 2024, Orlando, USA, 2024*.
- C. H. Lee\*, M. J. Tahk, S. T. Park, S. J. Yoo, and Y. H. Song. "A Study on Homing Guidance Techniques for Guided Drone-Dropped Ammunitions". *Journal of Institute of Control, Robotics and Systems, Vol. 30, No. 3, 2024, pp. 276-287*.
- Y. J. Oh, Y. K. Park\*, and C. H. Lee. "Study of Launch Vehicle Applicability of Incremental Nonlinear Dynamic Inversion Attitude Controller". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- H. C. Kang, J. W. Cha, T. S. Kuk\*, S. H. Ryu, K. J. Woo, K. W Jung, and C. H. Lee. "Altitude Control/Tethered Flight Test Results of RLV Demonstrator Using Hybrid Rocket". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- S. D. Lee, K. W. Jung, and C. H. Lee\*. "Landing Guidance for Reusable Orbital Rockets using Model Predictive Control". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- H. J. Kim, J. Park, C. H. Lee\*, and H. S. Choi. "Advanced Longitudinal Controller of Hypersonic Vehicle Using Nonlinear Dynamic Inversion and Adaptive Estimator". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- C. H. Lee\*, M. J. Tahk, S. H. Seo, and H. K. Kim. "Design of Guidance and Control for Course Correction Fuze using Rapid Impact Point Prediction". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- O. Kang, B. Kim, C. H. Lee\*, M. J. Tahk, J. W. Kim, Y. K. Kim, and S. W. Park. "Guidance Strategy for Gun-Launched Gliding Guided Munitions". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- K. W. Jung, S. D. Lee, J. Park, J. Jang, C. H. Lee\*, H. C. Kang, and T. S. Kuk. "Study on the Landing Guidance and Control Algorithm for Test Vehicle of Reusable Launch Vehicle". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- D. W. Kim, J. Jang, and C. H. Lee\*. "Landing Guidance of Reusable Launch Vehicle with Linearized Model Predictive Control using Second-order Cone Programming". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- J. Jang and C. H. Lee\*. "Development of Customized Convex Optimization Solver for Onboard Real-Time Optimization". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- K. W. Jung and C. H. Lee\*. "Study on Landing Guidance for Reusable Launch Vehicle based on the Concept of Zero-Effort-Trajectory". *The Korea Society for Aeronautical and Space Sciences 2024 Fall Conference, 2024*.
- K. K. Jeon, C. H. Lee\*, K. W. Jung, C. G. Jung, and C. Lee. "A Study on the Three-loop Autopilot for Compensation for Autopilot Lag". *The Korea Institute of Military Science and Technology 2024 Spring Conference, 2024*.
- T. Kim, B. Kim, C. H. Lee\*, J. W. Kim, Y. K. Lee, and S. W. Park. "Longitudinal Guidance Considering Acceleration Limits for Gliding Guided Projectile". *The Korea Institute of Military Science and Technology 2024 Spring Conference, 2024*.
- D. H. Kim, J. Jang, and C. H. Lee\*. "Closed-Loop Landing Guidance for Reusable Launch Vehicle using Covariance Steering". *The Korea Society for Aeronautical and Space Sciences 2024 Spring Conference, 2024*.
- E. T. Jeong and C. H. Lee\*. "Analysis of Interception Geometry Conditions for the Long-range Artillery Interceptor Using High-explosive Fragmentation Warhead". *The Korea Society for Aeronautical and Space Sciences 2024 Spring Conference, 2024*.

**2023**

- B. Kim and C. H. Lee\*. "Optimal Midcourse Guidance for Dual-Pulse Rocket Using Pseudospectral Sequential Convex Programming". *Journal of Guidance, Control, and Dynamics, Vol. 46, No. 7, 2023, pp. 1425-1436*.
- C. G. Jung, B. Kim, K. W. Jung, and C. H. Lee\*. "Thrust Integrated Trajectory Optimization for Multi-pulse Rocket Missiles using Convex Programming". *Journal of Spacecraft and Rockets, Vol. 60, No. 3, 2023, pp. 957-971*.
- K. P. Kim and C. H. Lee\*. "MPPI-Based Computational Guidance for Impact Time Control with Practical Constraints". *International Journal of Aeronautical and Space Sciences, Vol. 24, No. 12, 2023, pp. 853-875*.
- K. P. Kim and C. H. Lee\*. "Fixed Range Horizon MPPI-based Missile Computational Guidance for Constrained Impact Angle". *International Journal of Control, Automation and Systems, Vol. 21, No. 6, 2023, pp. 1866-1884*.
- S. D. Lee and C. H. Lee\*. "Multi-phase and Dual Aero/Propulsive Rocket Landing Guidance using Successive Convex Programming". *Proceedings of the IMeche, Part G: Journal of Aerospace Engineering, Vol. 237, No. 8, 2023, pp. 1816-1834*.
- S. D. Lee and C. H. Lee\*. "An Analysis of the Point-to-Point Cargo Transportation System using Reusable Launch Vehicles". *74th International Astronautical Congress, Baku, Azerbaijan, 2023*.
- K. W. Jung and C. H. Lee\*. "Parameter Optimization-Based Automatic Design of Launch Vehicle's Attitude Controller". *74th International Astronautical Congress, Baku, Azerbaijan, 2023*.
- M. J. Tahk, J. Park, H. Rho, and C. H. Lee\*. "Suboptimal Guidance Based on Pursuit and Impact Angle Control for Long-Range Air-to-Air Missiles". *2023 14th International Conference on Mechanical and Aerospace Engineering, Porto, Portugal, 2023*.
- J. Park, H. Rho, C. H. Lee\*, M. J. Tahk, H. S. Choi, and S. Y. Kim. "Nonlinear Three-Loop Autopilot Design for Hypersonic Vehicles Considering Aerodynamic-Propulsion Dynamics Couplings". *2023 14th International Conference on Mechanical and Aerospace Engineering, Porto, Portugal, 2023*.
- C. G. Jung, C. H. Lee\*, T. H. Kim, and H. S. Choi. "Entry Vehicle Trajectory Optimization using Convex Programming and Post-correction Technique". *Joint 10th EUCASS - 9th CEAS Conference, Lausanne, Switzerland, 2023*.
- B. Kim, C. H. Lee\*, M. J. Tahk, Y. Lee, and H. G. Sung. "Mid-Course Trajectory Optimization of VFDR Missiles via Pseudospectral Sequential Convex Programming". *Joint 10th EUCASS - 9th CEAS Conference, Lausanne, Switzerland, 2023*.
- M. J. Tahk, J. C. Park, B. Kim, H. Rho, and C. H. Lee\*. "Augmented Pursuit Guidance for Flight Trajectory Shaping". *Joint 10th EUCASS - 9th CEAS Conference, Lausanne, Switzerland, 2023*.
- D. Yoon and C. H. Lee\*. "A Computationally Effective Multi-Output Recursive Gaussian Process-based Path-following Guidance for Unmanned Aerial Vehicle". *RSS2023 Workshop (Inference and Decision Making for Autonomous Vehicles), Daegu, Korea, 2023*.
- J. Jang, C. G. Jung, and C. H. Lee\*. "Technology Development Trends of Ultra-high-speed Target Wide Area Defense Systems". *Journal of Institute of Control, Robotics and Systems, Vol. 29, No. 3, 2023, pp. 20-29*.
- B. Kim, C. G. Jung, Y. Lee, H. G. Sung, and C. H. Lee\*. "Midcourse Trajectory Optimization for Variable-flow Ducted Rocket Missiles Based on Convex Optimization". *Journal of Institute of Control, Robotics and Systems, Vol. 29, No. 8, 2023, pp. 652-661*.
- J. Jin\*, C. H. Lee, H. Bang, Y. W. Kim, J. Park, and T. H. Kim. "Performance Analysis for Configuration Design Optimization of Hit-to-kill Interceptor Missile Against Ballistic Missiles". *Journal of Institute of Control, Robotics and Systems, Vol. 29, No. 8, 2023, pp. 662-670*.
- T. Kim, B. Kim, C. H. Lee\*, M. J. Tahk, J. W. Kim, Y. K. Lee, and I. Y. Kang. "Longitudinal Guidance for Maximizing the Range of a Gliding Guided Munition". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- D. H. Kim and C. H. Lee\*. "Powered Descent Guidance on Mars using Sequential Convex Programming with Linear Throttle Margin". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- K. M. Na and C. H. Lee\*. "Stochastic System Modeling Using Physics-Informed Deep Learning". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- C. G. Jung, M. Shin, and C. H. Lee\*. "Comparative Analysis Study on Re-entry Vehicle Guidance". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- J. Park, K. W. Jung, and C. H. Lee\*. "Hypersonic Vehicle Trajectory Tracking Guidance Algorithm through Following Reference Dynamic Pressure Profile". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- J. Jang and C. H. Lee\*. "Landing Guidance Algorithm of Reusable Launch Vehicles with State-Conditioned Constraint Function". *The Korea Society for Aeronautical and Space Sciences 2023 Fall Conference, 2023*.
- E. T. Jeong and C. H. Lee. "Improvement of Computational Efficiency of Path Following MPPI Algorithm for UAVs Using Pursuit Guidance Laws". *The Korea Institute of Military Science and Technology 2023 Fall Conference, 2023*.
- D. Yoon and C. H. Lee\*. "A Computationally Effective Gaussian Process Regression-based Path-following Guidance Law for Unmanned Vehicle". *The Korea Institute of Military Science and Technology 2023 Fall Conference, 2023*.
- K. W. Jung and C. H. Lee\*. "A Design Scheme for a Launch Vehicle’s Attitude Control Algorithm during Atmospheric Ascent via Parameter Optimization". *2023 Symposium on Space Launch Vehicle Technology, 2023*.
- S. D. Lee and C. H. Lee\*. "Landing Guidance for Orbital Rockets using Convex Optimization". *2023 Symposium on Space Launch Vehicle Technology, 2023*.
- K. W. Jung, H. K. Rho, C. H. Lee\*. "A Study on Landing Guidance for Reusable Launch Vehicle with Model Predictive Control". *The Korea Society for Aeronautical and Space Sciences 2023 Spring Conference, 2023*.
- C. G. Jung, C. H. Lee\*, and M. J. Tahk. "Midcourse Guidance for Dual-Pulse Rocket Missiles using Polynomial Trajectory". *The Korea Society for Aeronautical and Space Sciences 2023 Spring Conference, 2023*.

**2022**

- J. Li, Z. Ning, S. He, C. H. Lee, and S. Zhao\*. "Three-Dimensional Bearing-Only Target Following via Observability-Enhanced Helical Guidance". *IEEE Transactions on Robotics, Vol. 39, No. 2, 2022, pp. 1509-1526*.
- K. W. Jung, Y. W. Kim, and C. H. Lee\*. "Aerodynamically Controlled Missile Flight Datasets and its Applications". *International Journal of Aeronautical and Space Sciences, Vol. 24, 2022, pp. 248-260*.
- Y. W. Kim, M. G. Seo, and C. H. Lee\*. "Investigation on Energy-Effective Guidance-to-Collision Strategies for Exo-Atmospheric Interceptors". *Aerospace Science and Technology, Vol. 124, 2022, pp. 1-13*.
- J. Kim, C. H. Lee, M. Y. Yi\*. "New Weapon Target Assignment Algorithms for Multiple Targets Using Rotational Strategy and Clustering Approach". *IEEE Access, Vol. 10, 2022, pp. 43738-43750*.
- H. Li, S. He\*, J. Wang, and C. H. Lee. "Optimal Encirclement Guidance". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 58, No. 5, 2022, pp. 4327-4341*.
- H. Li, J. Wang, S. He\*, and C. H. Lee. "Nonlinear Optimal 3-D Impact-Angle-Control Guidance against Maneuvering Targets". *IEEE Transactions on Aerospace and Electronic Systems, Vol. 58, No. 3, 2022, pp. 2467-2481*.
- Y. Wang, S. He\*, J. Wang, C. H. Lee. "Dynamic Estimation and Compensation of Time Delay for Missiles with Strapdown Seeker". *Journal of Guidance, Control, and Dynamics, Vol. 45, No. 4, 2022, pp. 781-791*.
- J. Bae, S. D. Lee, Y. W. Kim, C. H. Lee\*, S. Y. Kim. "Convex Optimization-based Entry Guidance for Spaceplane". *International Journal of Control, Automation and Systems, Vol. 20, No. 5, 2022, pp. 1652-1670*.
- P. Wang\*, Y. Guo, G. Ma, C. H. Lee, B. Wie. "New Look-Angle Tracking Guidance Strategy for Impact Time and Angle Control". *Journal of Guidance, Control, and Dynamics, Vol. 35, No. 3, 2022, pp. 545-557*.
- Y. W. Kim, B. Kim, C. H. Lee\*, and S. He. "A Unified Formulation of Optimal Guidance-to-Collision Law for Accelerating and Decelerating Targets". *Chinese Journal of Aeronautics, Vol. 35, No. 7, 2022, pp. 40-54*.
- E. T. Jeong, S. D. Lee, K. M. Na, and C. H. Lee\*. "MPPI Control-based Adaptive Pursuit Guidance for Path-following Control of Quadrotors in the Presence of Wind Disturbance". *The 10th International Conference on Robot Intelligence Technology and Applications (RiTA 2022), Gold Coast, Australia, 2022*.
- K. M. Na, J. C. Park, K. W. Jung, and C. H. Lee\*. "Estimation of Aerodynamic Uncertainty in Missile System Using Physics-Informed Neural Networks Framework". *The 10th International Conference on Robot Intelligence Technology and Applications (RiTA 2022), Gold Coast, Australia, 2022*.
- D. Yoon, Y. W. Kim, B. Kim, and C. H. Lee\*. "Nonlinear Autoregressive with Gaussian Process Regression-based Path-following Guidance for UAV under Time-varying Disturbances". *The 10th International Conference on Robot Intelligence Technology and Applications (RiTA 2022), Gold Coast, Australia, 2022*.
- P. Wang, C. H. Lee\*, and B. Wie. "New Guidance Law for Impact Time and Angle Control Against Maneuvering Target". *The 22nd International Conference on Control, Automation and Systems (ICCAS 2022), Busan, Korea, 2022*.
- C. G. Jung, C. H. Lee\*, and M. J. Tahk. "Convex Programming-based Optimal Three-Dimensional Mid-course Guidance with Lossless Convexification". *33rd Congress of the International Council of the Aeronautical Sciences (ICAS 2022), Stockholm, Sweden, 2022*.
- Y. W. Kim and C. H. Lee\*. "A New Optimal Terminal Guidance Law for High-Speed Maneuvering Target". *The 13th Asian Control Conference (ASCC 2022), Jeju, Korea, 2022*.
- D. Yoon, E. T. Jeong, and C. H. Lee\*. "Gaussian Process Regression-based Disturbance Rejection Controller for Unmanned Aerial Vehicle". *The 13th Asian Control Conference (ASCC 2022), Jeju, Korea, 2022*.
- B. Kim, C. G. Jung, M. J. Tahk, and C. H. Lee\*. "Optimal Mid-Course Guidance of VFDR Missiles Based on Pseudospectral Convex Optimization". *The 13th Asian Control Conference (ASCC 2022), Jeju, Korea, 2022*.
- P. Wang and C. H. Lee\*. "Impact Time and Angle Guidance Against Maneuvering Targets". *The 13th Asian Control Conference (ASCC 2022), Jeju, Korea, 2022*.
- B. Kim, M. J. Tahk, and C. H. Lee\*. "Mid-Course Guidance for Dual-pulse Rocket Air-to-Air Missiles Using Pseudospectral Sequential Convex Programming". *The 6th CEAS Conference on Guidance, Navigation and Control, EuroGNC 2022, Berlin, Germany, 2022*.
- D. Yoon, C. H. Lee\*, and M. J. Tahk. "Gaussian Process Regression-based Disturbance Compensation Control for Urban Air Mobility". *The 6th CEAS Conference on Guidance, Navigation and Control, EuroGNC 2022, Berlin, Germany, 2022*.
- C. G. Jung, B. Kim, and C. H. Lee\*. "Midcourse Trajectory Optimization for Long-Range Missiles with Seeker Field-of-View Limit". *Journal of Institute of Control, Robotics and Systems, Vol. 28, No. 12, 2022, pp. 1206-1215*.
- C. G Jung, C. H. Lee\*, M. J. Tahk, D. G. Yoo, and S. H. Sohn. "Integrated Algorithm for Identification of Long Range Artillery Type and Impact Point Prediction With IMM Filter". *Journal of The Korean Society for Aeronautical and Space Sciences, Vol. 50, No. 8, 2022, pp. 531-540*.
- J. C. Park, K W. Jung, Y. W. Kim, and C. H. Lee\*. "Anomaly Detection Method for Missile Flight Data by Attention-CNN Architecture". *Journal of Institute of Control, Robotics and Systems, Vol. 28, No. 5, 2022, pp. 520-527*.
- E. T. Jeong and C. H. Lee\*. "A Study on Disturbance Classification of Unmanned Vehicle Data Using SVM". *Journal of Institute of Control, Robotics and Systems, Vol. 28, No. 4, 2022, pp. 304-312*.
- E. T. Jeong, J. C. Park, C. H. Lee\*, H. S. Choi, and S. Y. Kim. "Design of Nonlinear Flight-Path-Angle Controller for Hypersonic Vehicles via Three-loop Topology". *The Korea Society for Aeronautical and Space Sciences 2022 Fall Conference, 2022*.
- S. D. Lee, C. H. Kim, C. H. Lee\*, and H. L. Choi. "Study on Mission Profile Design for Reusable Rocket Cargo". *The Korea Society for Aeronautical and Space Sciences 2022 Fall Conference, 2022*.
- D. Yoon, K. M. Na, and C. H. Lee\*. "Design of Nonlinear Disturbance Observer-based Attitude Controller for Wake Effect of the Coaxial rotors". *The Korea Society for Aeronautical and Space Sciences 2022 Fall Conference, 2022*.
- J. C. Park and C. H. Lee\*. "Study on 3-Dimensional Guidance Law based on Collision Geometry". *The Korea Society for Aeronautical and Space Sciences 2022 Fall Conference, 2022*.
- K. M. Na, D. Yoon, and C. H. Lee\*. "Control Allocation Logic Validation in Simulation for Compensation of Performance Degradation in Dodeca-Hexacopter". *The Korea Society for Aeronautical and Space Sciences 2022 Fall Conference, 2022*.
- J. C. Park, C. H. Lee\*, H. S. Choi, and S. Y. Kim. "Guidance Law for Following Reference Dynamic Pressure Profile for Hypersonic Vehicles". *The Korea Institute of Military Science and Technology 2022 Fall Conference, 2022*.
- K. W. Jung and C. H. Lee\*. "Trajectory Tracking Guidance Based on Fuel-Optimal Trajectory for Powered-Descent of the Reusable Launch Vehicles". *The Korea Institute of Military Science and Technology 2022 Fall Conference, 2022*.
- C. G. Jung, B. Kim, C. H. Lee\*, M. J. Tahk, J. W. Kim, Y. K. Lee, I. Y. Kang. "Study on Attitude Stabilization for Gliding Guided Munition during Transition Phase". *The Korea Institute of Military Science and Technology 2022 Fall Conference, 2022*.
- C. G. Jung, C. H. Lee\*, and M. J. Tahk. "Performance Analysis of Trajectory Optimization-based Mid-Course Guidance". *The Korea Institute of Military Science and Technology 2022 Conference, 2022*.
- K. M. Na, K. W. Jung, and C. H. Lee\*. "Model Uncertainty Estimation Using Domain Knowledge and Neural Networks". *The Korea Institute of Military Science and Technology 2022 Conference, 2022*.
- K. M. Na, K. W. Jung, and C. H. Lee\*. "Error Estimation for Guided Missile Time-Series Data Based on Convolutional Neural Networks and Domain Knowledge". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- Y. W. Kim and C. H. Lee\*. "A Suboptimal Impact Time Control Guidance Law for DACS Type Kill Vehicle". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- D. Yoon, E. T. Jeong, and C. H. Lee\*. "Gaussian Process Regression-based Path-following Guidance Law for Unmanned Vehicle under Wind Disturbance". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- B. Kim and C. H. Lee\*. "Mid-Course Trajectory Optimization for Variable-Flow Ducted Rocket Missiles Using Pseudospectral Convex Programming". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- M. H. Cho, D. Yoon, and C. H. Lee\*. "A Design of Feedback Linearization Controller Using Gaussian Process Regression". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- E. T. Jeong and C. H. Lee\*. "Sample Efficient Model-Reference Reinforcement Learning Using MPPI and Path Following Guidance". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- K. W. Jung, S. D. Lee, and C. H. Lee\*. "Study on Computational Guidance and Control for Reusable Launch Vehicle’s Powered Descent". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.
- S. D. Lee, E. T. Jeong, and C. H. Lee\*. "Curved Path Following for Unmanned Vehicle via Reinforcement Learning". *The Korea Society for Aeronautical and Space Sciences 2022 Spring Conference, 2022*.

**2021**

- B. Kim, Y. W. Kim, N. Cho, and C. H. Lee\*. "Collision-geometry-based Optimal Guidance for High-speed Target". *Aerospace Science and Technology, Vol. 115, 2021, pp. 1-15*.
- C. Li, J. Wang, S. He\*, and C. H. Lee. "Nonlinear Optimal Impact-Angle-Constrained Guidance with Large Initial Heading Error". *Journal of Guidance, Control, and Dynamics, Vol. 44, No. 9, 2021, pp. 1663-1676*.
- M. G. Seo, C. H. Lee\*, and T. H. Kim. "Trajectory Shaping Guidance Law Design using Constraint-Combining Multiplier". *Proceedings for the Institution of Mechanical Engineers, Part G, Journal of Aerospace Engineering, Vol. 235, No. 13, 2021, pp. 1843-1853*.
- K. R. Song, T. H. Kim, C. H. Lee\*, and M. J. Tahk. "A New Guidance Algorithm against High-Speed Maneuvering Target". *International Journal of Aeronautical and Space Sciences, Vol. 22, No. 5, 2021, pp. 1170-1182*.
- H. S. Chi, Y. I. Lee, C. H. Lee, and H. L. Choi\*. "A Practical Optimal Guidance Scheme under Impact Angle and Terminal Acceleration Constraints". *International Journal of Aeronautical and Space Sciences, Vol. 22, No. 4, 2021, pp. 923-935*.
- Y. C. Kim, C. H. Lee, T. H. Kim, and M. J. Tahk\*. "A New Cooperative Homing Guidance of Anti-ship Missiles for Survivability Enhancement". *Accepted for Publication in International Journal of Aeronautical and Space Sciences, Vol. 22, No. 3, 2021, pp. 676-686*.
- D. Y. Lee, M. J. Tahk\*, and C. H. Lee. "Optimal Intermittent Maneuver of Homing Missiles for Target Observability Improvement". *Publication in International Journal of Aeronautical and Space Sciences, Vol. 22, No. 4, 2021, pp. 911-922*.
- S. He, C. H. Lee\*, H. S. Shin, and A. Tsourdos. "Optimal Three-Dimensional Impact Time Guidance with Seeker's Field-of-View Constraint". *Chinese Journal of Aeronautics, Vol. 34, No. 2, 2021, pp. 240-251*.
- S. Park, Y. Oh, S. J. Kim, Y. W. Kim, H. L. Choi\*, and C. H. Lee. "Trajectory-based Anomaly Classification of 6-DOF Guided Missile using Neural Networks". *The 9th International Conference on Robot Intelligence Technology and Applications (RiTA2021), Daejeon, Korea, 2021*.
- E. T. Jeong and C. H. Lee\*. "Learning-based Robust Flight Control under Center-of-Pressure Uncertainty". *The 9th International Conference on Robot Intelligence Technology and Applications (RiTA2021), Daejeon, Korea, 2021*.
- D. Yoon and C. H. Lee\*. "Gaussian Process-based Adaptive Path-Following Guidance for Unmanned Aerial Vehicles". *The 9th International Conference on Robot Intelligence Technology and Applications (RiTA2021), Daejeon, Korea, 2021*.
- C. G. Jung, C. H. Lee\*, and M. J. Tahk. "Legendre Pseudo-Spectral Method for Missile Trajectory Optimization with Free Final Time". *12th Asia-Pacific International Symposium on Aerospace Technology (APISAT 2021), Jeju, Korea, 2021*.
- K. W. Jung and C. H. Lee\*. "Anomaly Detection for Monte-Carlo Simulation Data of Missile Control System". *12th Asia-Pacific International Symposium on Aerospace Technology (APISAT 2021), Jeju, Korea, 2021*.
- E. T. Jeong and C. H. Lee\*. "Path-Following Guidance Using Model Predictive Path Integral Control". *12th Asia-Pacific International Symposium on Aerospace Technology (APISAT 2021), Jeju, Korea, 2021*.
- S. D. Lee, C. H. Lee\*, and S. Y. Kim. "Pseudospectral Convex Optimization for Reentry Vehicle Guidance with No-Fly Zone Constraints". *12th Asia-Pacific International Symposium on Aerospace Technology (APISAT 2021), Jeju, Korea, 2021*.
- D. Yoon and C. H. Lee\*. "Nonlinear Three-Loop Autopilot Design for Spaceplanes". *2021 The 21st International Conference on Control, Automation and Systems (ICCAS 2021), Jeju, Korea, 2021*.
- K. W. Jung, C. H. Lee\*, J. Lee, S. Im, K. Lee, M. Sagliano, and D. Seelbinder. "An Instantaneous Impact Point Guidance for Rocket with Aerodynamics Control". *2021 The 21st International Conference on Control, Automation and Systems (ICCAS 2021), Jeju, Korea, 2021*.
- D. Yoon, Y. W. Kim, T. Jeong, C. H. Lee\*, and M. J. Tahk. "A Nonlinear Disturbance Observer-Based Adaptive Controller Considering CG Variation of Urban Aerial Mobility". *29th Mediterranean Conference on Control and Automation (MED 2021), Bari, Italy, 2021*.
- D. Y. Lee, Y. W. Kim, C. H. Lee\*, and M. J. Tahk. "Impact Angle Control Guidance Laws using Finite-Time-Convergence Control Methods". *29th Mediterranean Conference on Control and Automation (MED 2021), Bari, Italy, 2021*.
- S. He\*, X. Zhang, D. Lin, and C. H. Lee. "A New Proportional-Integral Guidance Law". *33rd Chinese Control and Decision Conference, Kunming, China, 2021*.
- D. Yoon, Y. W. Kim, C. H. Lee\*, H. L. Choi, and H. Ryu. "Reentry Guidance for Korean Spaceplane Based on Reference Drag Following". *Journal of The Korean Society for Aeronautical and Space Sciences, Vol. 49, No. 8, 2021, pp. 637-648*.
- B. Kim, C. H. Lee\*, M. J. Tahk, D. S. Kim, S. H. Kim, and H. S. Lee. "Optimal Weapon-Target Assignment Algorithm for Closed-In Weapon Systems Considering Variable Burst Time". *Journal of The Korean Society for Aeronautical and Space Sciences, Vol. 49, No. 5, 2021, pp. 365-372*.
- S. D. Lee, J. S. Hwang, H. Y. Jeon, C. H. Lee\*, J. M. Ahn, and J. H. Kim. "A Study on Attitude Control for Reusable Launch Vehicle". *The Korea Society for Propulsion Engineers 2021 Fall Conference, 2021*.
- J. H. Cho, Y. W. Kim, C. H. Lee\*, and J. H. Kim. "Flight Anomaly Detection Using Support Vector Machines". *The Korea Society for Aeronautical and Space Sciences 2021 Fall Conference, 2021*.
- K. W. Jung, J. C. Park, and C. H. Lee\*. "Anomaly Detection for Simulation Data". *The Korea Society for Aeronautical and Space Sciences 2021 Fall Conference, 2021*.
- C. G. Jung, K. W. Jung, and C. H. Lee\*. "hp Pseudo-Spectral Convex Programming for Mid-course Trajectory Optimization for Surface-to-Air Missiles". *The Korea Society for Aeronautical and Space Sciences 2021 Fall Conference, 2021*.
- E. T. Jeong and C. H. Lee\*. "Disturbance and Uncertainty Classification for Quadrotor 6DOF Flight Simulation Data Using SVM". *The Korea Society for Aeronautical and Space Sciences 2021 Fall Conference, 2021*.
- S. D. Lee and C. H. Lee\*. "Trajectory Tracking Control for 3-DOF Unmanned Vehicle via Reinforcement Learning". *The Korea Society for Aeronautical and Space Sciences 2021 Fall Conference, 2021*.
- C. G. Jung, C. H. Lee\*, M. J. Tahk. "A Midcourse Guidance for Air-to-Air Missiles using Convex Optimization". *The Korea Institute of Military Science and Technology 2021 Conference, 2021*.
- K. W. Jung, Y. W. Kim, C. H. Lee\*. "Anomaly Detection Algorithm for Flight Pattern Analysis using Machine Learning". *The Korea Institute of Military Science and Technology 2021 Conference, 2021*.
- S. H. Lee and C. H. Lee\*. "Trajectory Following Guidance for Unmanned Vehicle using Convex Optimization". *The Korea Society for Aeronautical and Space Sciences 2021 Spring Conference, 2021*.
- S. D. Lee, Y. W. Kim, C. H. Lee\*. "Entry Guidance Algorithm for Reentry Vehicles via Convex Programming". *The Korea Society for Aeronautical and Space Sciences 2021 Spring Conference, 2021*.
- C. Moon, U. Choi, D. Lee, D. Yoon, C. H. Lee, J. Ahn\*. "A Study on the Path Generation and Waypoint Guidance for Autonomous Hoverbike". *The Korea Society for Aeronautical and Space Sciences 2021 Spring Conference, 2021*.
- D. Yoon and C. H. Lee\*. "Guidance and Control Algorithm using Nonlinear Disturbance Observer for Unmanned Vehicle". *The Korea Society for Aeronautical and Space Sciences 2021 Spring Conference, 2021*.
- B. Kim, C. H. Lee\*, M. J. Tahk, D. S. Kim, S. H. Kim. "Impact Point Correction of CIWS for High-Speed Target Interception". *The Korea Society for Aeronautical and Space Sciences 2021 Spring Conference, 2021*.

## 연구 과제

누리집 Projects 페이지의 Current Research Projects 20건과, Previous Research Projects 가운데 2021년 10월 이후에 끝난 21건이다. 상태는 누리집이 나눈 구역 이름이며, Current 구역에도 종료 연월이 2025년인 과제가 있다. 지원 칸은 누리집이 적은 지원·주관 기관이고, 역할은 교수의 역할(연구책임자·공동연구원)이다.[^projects]

- 탄도수정신관 롤각 추정기법 및 성능분석 프로그램 연구 (기간 2025.01 ~ 2025.12; 지원 풍산; 역할 연구책임자; 상태 Current Research Projects)
- 재사용발사체 임무-비용 연계분석을 통한 경제성 분석연구 (기간 2024.10 ~ 2025.09; 지원 우주항공청/KAIST; 역할 공동연구원; 상태 Current Research Projects)
- AESA레이다 연동능력을 고려한 장거리공대공유도탄 운용개념 연구 (기간 2024.10 ~ 2026.09; 지원 LIG 넥스원; 역할 연구책임자; 상태 Current Research Projects)
- 대공 유도무기의 성능분석도구 개발 및 교전통제 알고리즘 연구 (기간 2024.07 ~ 2026.06; 지원 LIG 넥스원; 역할 연구책임자; 상태 Current Research Projects)
- 국방 지능형 군집체계 연구 및 인력양성 (기간 2024.07 ~ 2025.12; 지원 정보통신기획평가원/KAIST; 역할 공동연구원; 상태 Current Research Projects)
- 대지 표적 요격을 위한 중기유도 및 급속 호밍 유도기술 개발 (기간 2024.05 ~ 2025.12; 지원 LIG 넥스원/한국항공대학교; 역할 공동연구원; 상태 Current Research Projects)
- 환경 영향성에 대한 표적 동특성 분석 (기간 2024.04 ~ 2025.09; 지원 LIG 넥스원; 역할 연구책임자; 상태 Current Research Projects)
- 우주발사체 시스템 기술동향 분석 연구 (기간 2023.02 ~ 2026.12; 지원 한국항공우주연구원/KAIST; 역할 공동연구원; 상태 Current Research Projects)
- 재사용발사체 동력하강 비행구간 탑재(on-board) 유도제어 기술 개발 및 성능 검증 연구 (기간 2023.02 ~ 2027.12; 지원 한국항공우주연구원/인하대학교; 역할 공동연구원; 상태 Current Research Projects)
- 재사용발사체 유도제어 시뮬레이션 프로그램 개발 (기간 2023.08 ~ 2026.04; 지원 한화 에어로스페이스; 역할 연구책임자; 상태 Current Research Projects)
- 우주비행기 제어 통합 성능 분석 프로그램 개발 (기간 2023.01 ~ 2028.12; 지원 한국항공우주연구원; 역할 연구책임자; 상태 Current Research Projects)
- 무인우주비행체의 귀환 비행을 위한 유도제어 기술 연구 (기간 2022.11 ~ 2028.10; 지원 국방기술진흥연구소; 역할 연구책임자; 상태 Current Research Projects)
- 소형발사체 상단용 전기펌프를 적용한 하이브리드 로켓 엔진 개발 (기간 2022.05 ~ 2027.12; 지원 한국연구재단/이노스페이스; 역할 공동연구원; 상태 Current Research Projects)
- 재사용발사체 연착륙을 위한 최적 유도제어 알고리즘 개발 (기간 2022.04 ~ 2025.12; 지원 한국연구재단; 역할 연구책임자; 상태 Current Research Projects)
- 도심항공모빌리티(UAM) 특화 전문인력양성사업 (기간 2022.03 ~ 2025.02; 지원 한국산업기술진흥원/KAIST; 역할 공동연구원; 상태 Current Research Projects)
- 극초음속 비행환경을 고려한 비행제어 성능해석 연구 (기간 2022.01 ~ 2026.12; 지원 한국항공우주연구원; 역할 연구책임자; 상태 Current Research Projects)
- 다양한 표적 대응을 위한 장거리 공대공 유도탄의 중기유도기법 연구 (기간 2020.12 ~ 2026.12; 지원 국방과학연구소; 역할 연구책임자; 상태 Current Research Projects)
- 직격비행체 성능분석 도구 개발을 통한 최적 설계 연구 (기간 2020.12 ~ 2026.12; 지원 국방과학연구소/KAIST; 역할 공동연구원; 상태 Current Research Projects)
- 비행성능 판단을 위한 학습 기반 추정 및 기법 연구 (기간 2020.12 ~ 2026.03; 지원 국방과학연구소; 역할 연구책임자; 상태 Current Research Projects)
- 무인이동체 자율 유도제어 기술 개발 (기간 2020.06 ~ 2027.05; 지원 한국연구재단/인하대학교; 역할 공동연구원; 상태 Current Research Projects)
- 소형위성발사체 항법유도조종 알고리즘 및 성능분석 도구 개발 (기간 2024.01 ~ 2025.01; 지원 이노스페이스; 역할 연구책임자; 상태 Previous Research Projects)
- 범용 우주발사체 임무설계 및 성능해석 통합 SW 개발 (기간 2023.04 ~ 2024.12; 지원 정보통신기획평가원/제이마플; 역할 공동연구원; 상태 Previous Research Projects)
- 교육용 조립식 모델로켓의 제작과 궤적 예측 (기간 2024.03 ~ 2024.12; 지원 한국영재학교; 역할 연구책임자; 상태 Previous Research Projects)
- 포발사 탄약용 유도조종 알고리즘 개발 (기간 2024.01 ~ 2024.12; 지원 풍산; 역할 연구책임자; 상태 Previous Research Projects)
- 미래 전장 응용을 위한 고신뢰성의 다목적 호버바이크 개발 (기간 2019.11 ~ 2024.10; 지원 국방과학연구소/KAIST; 역할 공동연구원; 상태 Previous Research Projects)
- 반영구적 임무 수행이 가능한 환경 감시 드론 기반 기술 개발 (기간 2024.05 ~ 2024.12; 지원 KAIST 로보틱스 연구소; 역할 공동연구원; 상태 Previous Research Projects)
- 드론 투하탄 공격정확도 예측 장비 개발 (기간 2023.11 ~ 2024.02; 지원 OBP ENG/청주대학교; 역할 공동연구원; 상태 Previous Research Projects)
- 지능탄 비행성능예측 용역 (기간 2023.07 ~ 2024.02; 지원 국방과학연구소/순천대학교; 역할 공동연구원; 상태 Previous Research Projects)
- 장사정포요격체계 요격성능분석을 위한 교전모의 연구 (기간 2023.05 ~ 2024.04; 지원 LIG 넥스원; 역할 연구책임자; 상태 Previous Research Projects)
- 유도형 비행체 임무계획 및 종말유도기법 연구 (기간 2023.01 ~ 2023.12; 지원 풍산; 역할 연구책임자; 상태 Previous Research Projects)
- 재사용 로켓 수송 시스템 핵심 기술 연구 (기간 2022.06 ~ 2023.12; 지원 KAIST; 역할 연구책임자; 상태 Previous Research Projects)
- 재사용 가능한 우주발사체 효용성 연구 용역 (기간 2022.05 ~ 2022.11; 지원 대한민국 육군; 역할 연구책임자; 상태 Previous Research Projects)
- 유도형 탄약의 회전 중 자세 안정화 기법 연구 (기간 2022.01 ~ 2022.12; 지원 풍산; 역할 연구책임자; 상태 Previous Research Projects)
- 발사체의 탑재체 궤도 진입을 위한 비행 자세 제어 (기간 2021.12 ~ 2023.12; 지원 한화 에어로스페이스; 역할 연구책임자; 상태 Previous Research Projects)
- 소형위성발사체 비행제어 알고리즘 및 성능분석 도구 개발 (II) (기간 2021.09 ~ 2022.09; 지원 이노스페이스; 역할 연구책임자; 상태 Previous Research Projects)
- 유사 스펙트럴 에르미트 보간법을 사용한 보다 빠르고 정확한 재진입 비행체 궤적 최적화 (기간 2021.07 ~ 2021.12; 지원 KAIST(URP Program); 역할 연구책임자; 상태 Previous Research Projects)
- 장사정포 탐지/추적 필터 및 동시표적 추적 알고리즘 개발 (기간 2021.04 ~ 2022.03; 지원 LIG 넥스원; 역할 연구책임자; 상태 Previous Research Projects)
- 발사체 재사용을 위한 재진입 및 착륙 연구 (기간 2019.03 ~ 2021.12; 지원 한국항공우주연구원; 역할 연구책임자; 상태 Previous Research Projects)
- 복합재 항공기의 위험감지 및 경고를 위한 기계학습 기반 인공지능 구조건전성 모니터링 시스템 개발 (기간 2019.03 ~ 2021.12; 지원 한국산업기술평가관리원; 역할 연구책임자; 상태 Previous Research Projects)
- 재진입 비행체 항법유도제어 시스템 최적화 설계 프레임 개발을 위한 기초 기술 연구 (기간 2019.03 ~ 2021.12; 지원 한국항공우주연구원; 역할 연구책임자; 상태 Previous Research Projects)
- 항공우주시스템을 위한 전산유도제어 프레임워크 개발에 대한 기초 연구 (기간 2019.01 ~ 2022.12; 지원 KAIST; 역할 연구책임자; 상태 Previous Research Projects)

## 연락과 위치

- 교수 연구실: N7-2 #2306[^aefac] (학과 연구실 소개는 N7-2동 #2312로 적는다[^aelab])
- 교수 전화: 042-350-3711[^aefac][^home] (학과 연구실 소개는 042-350-3758로 적는다[^aelab]), 팩스 +82-42-350-3710[^home]
- 교수 이메일: lckdgns@kaist.ac.kr[^home][^aelab][^aefac]
- 주소: Bldg. N7-2, Department of Aerospace Engineering, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
[^p1]: J.-I. Jang, C.-H. Lee, IEEE Transactions on Aerospace and Electronic Systems 62, 7896-7913 (2026). <https://doi.org/10.1109/taes.2026.3673639> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K.-W. Jung, S.-D. Lee, C.-G. Jung, C.-H. Lee, International Journal of Control, Automation and Systems 23, 2198-2218 (온라인 2025-08-13). <https://doi.org/10.1007/s12555-024-0628-3> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Bae, B. Kim, C.-H. Lee, Journal of Guidance, Control, and Dynamics 47, 711-727 (2024). <https://doi.org/10.2514/1.g006918> 초록 기준.
[^p4]: E.-T. Jeong, D. Yoon, C.-H. Lee, International Journal of Aeronautical and Space Sciences (온라인 2026-03-26; 누리집 표기는 게재 승인). <https://doi.org/10.1007/s42405-026-01183-x> 초록 기준(출판사 논문 페이지).
[^p5]: K.-M. Na, C.-H. Lee, Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering (온라인 2026-05-26; 누리집 표기는 게재 승인). <https://doi.org/10.1177/09544100261451532> 초록 기준.
[^p6]: K.-M. Na, C.-H. Lee, Journal of Aerospace Information Systems 21, 152-167 (2024). <https://doi.org/10.2514/1.i011269> 초록 기준.
[^p7]: J. Park, C.-H. Lee, IEEE Transactions on Aerospace and Electronic Systems 61, 17703-17716 (2025). <https://doi.org/10.1109/taes.2025.3605915> 초록 기준(OpenAlex 등록 초록).
[^p8]: J. Park, E.-T. Jeong, K.-W. Jung, C.-H. Lee, IEEE Transactions on Aerospace and Electronic Systems 61, 457-472 (2025). <https://doi.org/10.1109/taes.2024.3448393> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://fdcl2.kaist.ac.kr/> (연구실 소개, Research Areas, Contact Information, Research Achievements, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professors 페이지 <https://fdcl2.kaist.ac.kr/people/professors> (2026-10-23 열람)
[^students]: 연구실 누리집 Students 페이지 <https://fdcl2.kaist.ac.kr/people/students> (2026-10-23 열람)
[^postdocs]: 연구실 누리집 Post Doctors 페이지 <https://fdcl2.kaist.ac.kr/people/post-doctors> (2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://fdcl2.kaist.ac.kr/people/alumni> (2026-10-23 열람)
[^research]: 연구실 누리집 Research 페이지 <https://fdcl2.kaist.ac.kr/research> (Research Vision과 Research Pillar #1–#3, 2026-10-23 열람)
[^projects]: 연구실 누리집 Projects 페이지 <https://fdcl2.kaist.ac.kr/projects> (Current Research Projects, Previous Research Projects, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://fdcl2.kaist.ac.kr/publications> (Book, International Journal, International Conference, Domestic Journal, Domestic Conference, 2026-10-23 열람)
[^lectures]: 연구실 누리집 Lectures 페이지 <https://fdcl2.kaist.ac.kr/lectures> (2026-10-23 열람)
[^aelab]: KAIST 항공우주공학과 연구실 소개 「Flight Dynamics and Control Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/88> (연구실명, 교수, 연구실 소개, 웹사이트, 이메일, Tel, Office, 연구분야, 2021-08-16 게시, 2026-10-23 열람)
[^aefac]: KAIST 항공우주공학과 교수진 목록 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (이창훈 항목의 직위, Career, Tel, Website, E-mail, 연구분야, 연구실, 2026-10-23 열람)

# 반도체 패키지 모듈 연구실 (SMEET Lab)

**서울대학교 공과대학 전기·정보공학부 · 윤상원 교수**

- 분야: 반도체 패키지 설계, 냉각과 내구성 평가, 이동 수단의 전자부품과 센서 신호(정보를 나타내거나 전달하는 물리량의 변화) 처리
- 대분야: 전기전자·반도체·광학, 기계·로봇·제조
- 태그: 첨단 반도체 패키징[^p2][^p3], 열전달·열관리[^p1][^p5], 착용형 생체 센서[^p6]
- 홈페이지: <https://sites.google.com/view/smeetsnu>
- 근거와 출처: [SMEET 근거 페이지](smeet-sources.md)

> 반도체 칩을 연결하고 보호하는 패키지를 설계해 열을 빼고 고장을 평가하며, 이동 수단과 착용 기기의 센서 신호를 해석하는 연구실이다.[^objective][^packaging]

## 무엇을 연구하나

반도체 패키징은 칩을 기판(소자나 재료를 놓거나 만드는 바탕)이나 다른 칩과 연결하고 보호하는 기술이다. SMEET 연구실은 전기에너지의 흐름을 조절하는 전력반도체의 패키지와, 인공지능 연산용 칩·메모리의 이종집적(서로 다른 종류의 소자나 칩을 묶는 기술)을 연구한다. 메모리는 자료를 저장하는 장치이고, 소자는 전기적 기능을 수행하는 부품이다. 연구 범위는 설계에서 평가까지이며, 전기·열 특성과 패키지의 휨, 접합(재료나 부품을 맞붙이는 일)과 파손을 함께 다룬다.[^objective][^packaging]

메모리 패키지에서는 칩을 쌓은 구조의 열 흐름을 다룬다. NAND형 플래시 메모리(블록 단위로 지우고 다시 쓰며 전원이 꺼져도 자료를 유지하는 반도체 메모리)의 패키지 연구는 실험과 유한요소법(대상을 여러 부분으로 나누어 물리 현상을 계산하는 방법), 열 흐름을 연결망으로 나타낸 모형을 결합했다. 칩에서 나온 열이 위쪽의 보호 재료와 아래쪽의 납땜(녹인 접합용 금속으로 부품을 붙이는 작업) 연결부를 통해 흐르는 경로를 확인하고, 내부에 금속 구조를 넣어 열을 배출하는 설계를 제안했다.[^p1] 연구실의 연구 목표에는 인공지능 연산용 칩과 메모리의 패키징도 명시되어 있다.[^objective]

전력반도체 패키지에서는 전기 연결과 냉각, 반복 가열에 따른 손상을 함께 다룬다. 질화갈륨(Gallium Nitride, GaN) 소자를 구리 구조로 연결해 전기·열 성능을 평가했고,[^p2] 탄화규소(Silicon Carbide, SiC) 모듈에서는 위아래로 열을 빼는 양면 냉각 구조와 열팽창(온도 변화에 따라 재료의 치수가 변하는 현상)을 함께 고려했다.[^p3] 열로 인한 반복 변형이 납땜층에 만드는 균열(재료 안이나 표면의 갈라진 틈)을 계산하고 실험의 균열 성장과 비교하는 연구도 있다.[^p4] 냉각 장치 쪽에서는 열을 내보내는 방열판의 핀(방열판에서 돌출된 열 방출 구조) 형상과 기울기를 바꾸어 모듈의 온도를 낮추는 설계를 제작·측정했다.[^p5]

또 다른 갈래는 모빌리티(사람과 물건의 이동 수단과 체계)에 쓰는 센서의 모형과 신호 처리, 부품 신뢰성(정해진 조건과 기간에 요구한 기능을 유지하는 성질)이다.[^objective] 센서 융합(여러 센서의 정보를 함께 이용하는 방법)과 딥러닝(여러 처리 단계로 이어진 인공신경망으로 자료의 특징을 학습하는 방법)을 활용한다. 인공신경망은 연결된 계산 요소의 관계를 자료로 학습하는 모형이다. 귓불 착용 센서의 맥박·가속도(속도가 시간에 따라 변하는 정도) 신호를 함께 이용해 활동과 자세를 분류했고,[^p6] 광용적맥파(Photoplethysmography, PPG, 빛으로 혈액량 변화를 읽는 측정)의 신호에 섞인 움직임 잡음을 검출하는 알고리즘(계산이나 판단을 수행하는 절차)을 제안했다.[^p7]

## 주요 연구 주제

### 1. 메모리와 연산용 칩의 패키지 열관리

칩 패키지의 내부 열 흐름을 실험과 계산으로 연결하고, 금속 구조를 넣는 설계가 열 배출에 주는 영향을 연구한다. 인공지능 연산용 칩과 메모리를 묶는 이종집적도 연구 목표다.[^p1][^objective]

### 2. 전력반도체의 연결·냉각·수명 평가

구리 연결 구조, 양면 냉각 모듈의 수직 배치, 납땜층 균열과 수명 평가, 방열판의 형상 설계를 다룬다. 전기·열 성능과 반복 가열로 생기는 손상을 함께 고려하는 것이 이 갈래의 공통점이다.[^p2][^p3][^p4][^p5]

### 3. 센서 신호 융합과 움직임 잡음 처리

착용 센서의 맥박·가속도 신호로 활동과 자세를 분류하고, 정상 신호를 학습해 움직임으로 생긴 잡음을 검출하는 방법을 다룬다. 연구 목표는 센서 모형, 가상환경에서의 동작 계산, 신호 처리와 모빌리티 부품의 신뢰성을 포함한다.[^p6][^p7][^objective]

## 대표 논문

2021–2026년 논문 가운데 윤상원 교수의 서울대 부임(2023년 9월) 뒤에 출판된 논문 7편을 골랐다. 메모리 열관리, 전력반도체 패키징과 신뢰성, 센서 신호 처리를 함께 보여 주는 구성이다. 연도는 연구실 국제 학술지 목록의 출판 연도이고, '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.[^faculty][^journals]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Modeling and Improvement of Heat-Flow Paths Inside 3D-NAND First-Level Packages With Internal Metal Structures](https://doi.org/10.1109/TED.2026.3667123) · IEEE Transactions on Electron Devices | 메모리 패키지의 열 흐름을 실험·계산·연결망 모형으로 분석했다. 위쪽 수지와 아래쪽 기판이 열 배출을 제한하는 지점을 확인하고, 패키지 안에 금속을 넣는 설계를 비교해 온도를 낮추는 방법을 제안했다.[^p1] | 마지막 저자 |
| 2 | 2026 | [Improving Electrical and Thermal Performance of 650-V GaN E-HEMT Modules Using a Cover-All Meandered Thick-Copper (CAMT) Interconnection](https://doi.org/10.1109/ACCESS.2026.3658650) · IEEE Access | 기존 연결선을 대신하는 구리 연결 구조 CAMT(Cover-All Meandered Thick-Copper)를 제안하고 계산과 실험으로 평가했다. 전류 변화에 따라 연결부가 전압을 유도하는 성질인 기생 인덕턴스와, 스위칭(전기 흐름을 켜고 끄는 동작) 때의 전압 초과 상승 및 열 저항(열 흐름을 방해하는 정도)이 줄었다고 보고했다.[^p2] | 마지막 저자 |
| 3 | 2026 | [Balanced Vertical Structures for Thermal Expansion Matching and Reduced Thermomechanical Stress in Silicon Carbide Double-Sided Cooling Power Modules](https://doi.org/10.1109/TCPMT.2025.3641249) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 양면 냉각 모듈의 칩 아래에 간격을 두는 부품을 추가하고 수직 배치와 재료를 바꾸어 분석했다. 위아래의 열 배출과 열팽창을 함께 고려한 설계를 제안하고, 시제품의 반복 구동 시험으로 열에 따른 기계적 손상을 평가했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [Advanced Reliability Assessment Approach of Power Modules Under Low-Cycle Thermal Fatigue Through Redefined 3-D J-Integral](https://doi.org/10.1109/TCPMT.2024.3522123) · IEEE Transactions on Components, Packaging and Manufacturing Technology | 반복 가열 때문에 생기는 납땜 균열을 평가하기 위해 재정의한 J 적분(균열 주변의 에너지 상태를 나타내는 계산량)을 적용했다. 계산 결과를 실험에서 얻은 균열 성장률과 비교해 모듈의 수명을 평가하는 방법을 제안했다.[^p4] | 마지막 저자 |
| 5 | 2024 | [Analysis and Design Optimization of Tilted Rounded-Rectangular Pin-Fin Heat Sinks for xEV Double-Sided Cooling Power Module](https://doi.org/10.1109/JESTPE.2024.3354772) · IEEE Journal of Emerging and Selected Topics in Power Electronics | 양면 냉각 모듈의 방열 핀을 둥근 사각형으로 바꾸고 기울기를 조절했다. 계산으로 설계를 고른 뒤 실제로 제작·측정해 칩의 온도와 열 저항을 낮추는 효과를 확인했다.[^p5] | 마지막 저자 |
| 6 | 2024 | [Human Activity and Correlated Posture Monitoring Using Earlobe-Worn Wearable Sensor System and Deep Learning Algorithm](https://doi.org/10.1109/JSEN.2023.3332897) · IEEE Sensors Journal | 귓불에 착용하는 센서의 맥박과 가속도 신호를 함께 이용해 활동·자세를 분류하는 방법을 제안했다. 여러 학습 모형을 비교하고, 두 종류의 신호를 결합한 분류 결과를 평가했다.[^p6] | 마지막 저자 |
| 7 | 2024 | [Anomaly Detection of Motion Artifact in Photoplethysmography (PPG) Sensors Using Unsupervised Learning](https://doi.org/10.1109/JSEN.2024.3404558) · IEEE Sensors Journal | 정상 맥박 신호를 학습해 움직임으로 생긴 잡음을 검출하는 알고리즘을 제안했다. 신호를 압축했다 복원하도록 학습하는 오토인코더, 센서 종류에 맞춘 오차 계산과 보조 확인 절차를 결합했다.[^p7] | 마지막 저자 |

## 교수와 전문 분야

윤상원 교수는 서울대학교 전기공학부 학사(2000), University of Michigan 전기·컴퓨터과학 석사(2003)와 박사(2009)를 받았다. Toyota Research Institute of North America에서 연구원과 Senior Scientist로 일한 뒤, 2013년 9월부터 2023년 8월까지 한양대학교 미래자동차공학과에 재직했다. 서울대학교 전기·정보공학부에는 2023년 9월 부교수로 부임했고, 2026년 3월부터 교수로 재직한다.[^faculty]

학부는 전문 분야를 반도체 패키지와 모빌리티 전자부품으로 소개한다.[^faculty] 최근 논문에서 구체적으로 확인되는 분야는 패키지의 열 흐름과 냉각 설계,[^p1][^p5] 전력반도체의 연결·수직 구조와 균열 수명 평가,[^p2][^p3][^p4] 착용 센서의 정보 결합과 잡음 검출이다.[^p6][^p7] 누리집은 반도체공동연구소 차세대반도체패키지센터 센터장, 서울대-퍼듀대반도체공동연구센터 센터장(각 2026년 4월부터), 반도체공동연구소 연구부장(2026년 6월부터)으로도 적는다.[^pi]

## 응용 분야

연구 목표는 전력반도체용 모듈과 인공지능 연산용 칩·메모리의 패키징, 모빌리티 전자부품의 신뢰성 평가다.[^objective] 대표 논문은 전기 구동 차량에 쓰는 전력모듈의 냉각과 연결 구조,[^p3][^p5] 메모리 패키지의 내부 방열 구조,[^p1] 몸에 착용하는 센서의 활동·자세 인식과 움직임 잡음 처리를 다룬다.[^p6][^p7]

## 구성원

2026년 10월 26일 Team 페이지의 박사후연구원 1명과 재학생 12명이다. 학생은 석박사통합과정 7명, 박사과정 1명, 석사과정 4명이다. 과정과 시작 학기는 누리집 표기를 따랐다. '대표 논문 참여'는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Hobeom Han (한호범) | 박사후연구원 |  | 1, 6 |
| Jaejin Jeon (전재진) | 석박사통합과정 | Spring 2024 | 2, 4 |
| Se ung hyun Won (원승현) | 박사과정 | Spring 2024 | 3 |
| Junghoon Song (송정훈) | 석박사통합과정 | Spring 2024 |  |
| Jiyong So (소지용) | 석박사통합과정 | Spring 2024 |  |
| Eunpyo Hong (홍은표) | 석사과정 | Fall 2024 | 1 |
| Ayeong Choi (최아영) | 석박사통합과정 | Fall 2024 | 2 |
| Sunseong Kwon (권순성) | 석사과정 | Spring 2025 |  |
| Bonghak Lee (이봉학) | 석사과정 | Spring 2025 |  |
| Sejun Yang (양세준) | 석박사통합과정 | Spring 2026 |  |
| Heechan You (유희찬) | 석사과정 | Spring 2026 |  |
| Seungwan Jeung (정승완) | 석박사통합과정 | Spring 2026 |  |
| Seungyun Ha (하승윤) | 석박사통합과정 | Fall 2026 |  |

## 졸업생과 이전 구성원

Alumni 페이지의 박사 5명(2022–2024)과 석사 26명(2016–2026), 총 31개 학위 기록이다. 윤상원 교수의 2023년 9월 서울대 부임 이전에 한양대에서 배출한 졸업생이 포함되어 있다. 학위·연도·진로·학위 논문 제목은 누리집 표기다.[^alumni][^faculty]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 조성무 | Ph.D (2024) | 현대자동차 | Thermal Performance Enhancement of Indirect Double-Sided Cooling Power Modules Used in High Power Density xEV Inverters |
| 임장묵 | Ph.D (2022) | 현대모비스 | Characterization process of junction temperature and thermal impedance in GaN e-mode and d-mode HEMT power modules under cycling |
| 성지환 | Ph.D (2022) | 현대자동차 | Design and Evaluation of Automotive Power Module: 650V Gan E-HEMT with Meandered Interconnection and Integrated Motor-inverter Power Module |
| 김민기 | Ph.D (2022) | 현대모비스 | Maximum Junction Temperature Estimation and Thermal Impedance Characterization of Multichip SiC MOSFET Power Modules |
| 한호범 | Ph.D (2022) | 서울대학교 반도체공동연구소 | Driver Posture and Hand Gesture Recognition based on Artificial Intelligence and Sensor Fusion |
| 이유나 | M.S. (2026) | 삼성전자 |  |
| 조현습 | M.S. (2025) | LIG 넥스원 | 차량 위치 및 방향 추정을 위한 시각 및 관성 센서 융합 기반 시각적 관성 주행 거리계 연구 |
| 김진민 | M.S. (2024) | 라이드플럭스 | LSTM 기반 차량 모델 불확실성 변수 예측을 통한 차량 Torque Vectoring에서의 Sliding Mode Control 적용 가능성 연구 |
| 민경태 | M.S. (2024) | 삼성전자 | Case Type 및 Transfer Molded Type Sic 파워 모듈의 Stray Inductance 저감 기법 분석 |
| 원승현 | M.S. (2024) | 서울대 박사과정 진학 | 양방향 냉각 파워모듈 내 열분산 비율 불균형을 고려한 수직 적층 구조의 열응력 저감 비교 연구 |
| 권태림 | M.S. (2023) | 현대모비스 | PPG 센서 기반 운전자 생체 신호 이상탐지 및 신호처리 연구 |
| 신석진 | M.S (2023) | LG 마그나 | 전압 오버슈트와 스위칭 효율 향상을 위한 RC 스너버 회로 통합형 SiC 파워모듈의 설계 연구 |
| 오세찬 | M.S (2023) | HL 클레무브 | 긴급차량 발생 시나리오에서 가상 환경 차량 내외부 센서 데이터 융합을 통한 효율적 차량 유도 연구 |
| 윤성준 | M.S (2023) | HL 클레무브 | 실측 데이터 기반 라이다 노이즈 모델 개발과 가상환경 자율주행 객체인지 상황에서의 유용성 연구 |
| 최수형 | M.S (2023) | 라이드플럭스 | 자율주행 가상환경에서 빗방울 역산라 노이즈를 반영한 포인트 클라우드 연구 |
| 편성현 | M.S (2023) | 현대자동차 | SiC 파워모듈 히트싱크 냉각 성능 향상을 위한 Performed Pin 설계 |
| 권하연 | M.S (2022) | 현대자동차 | 저가 GPS/IMU 센서 기반 차량 위치 추정의 강건성 향상을 위한 딥 앙상블 알고리즘 성능 연구 |
| 김건희 | M.S (2022) | 만도 | 저비용 IMU 센서와 딥러닝 기반 적응형 칼만필터 알고리즘을 이용한 자세추정 연구 |
| 조용식 | M.S (2022) | 세미파워렉스 | 1200V 100A 급 SiC MOSFET, SiC-JFET/Si-MOSFET cascode 하프브리지 파워 모듈 슬루율 연구 |
| 조재현 | M.S. (2022) | 세미파워렉스 | Epoxy Molding Compound 특성값 및 몰딩 조건에 기반한 파워모듈 몰딩 해석 연구 |
| 김종한 | M.S. (2021) | 현대자동차 | 심층 신경망 기반 적응 필터를 이용한 차량의 종 방향 절대 속도 추정 알고리즘 연구 |
| 황승택 | M.S. (2021) | 현 대자동차 | 적층형 Cascode GaN 파워 모듈 내 보이드 위치에 따른 방열특성 연구 |
| 김태양 | M.S. (2020) | 현대 모비스 | 하프 브릿지 회로 구성에서 SiC MOSFET의 비선형성을 반영한 스위칭 과도 모델링 |
| 변미정 | M.S. (2020) | 현대자동차 | Study of ADAS Sensor Modeling and Performance considering Rainfall Disturbance |
| 장형규 | M.S. (2020) | 대학원진학 | 자석 기반 웨어러블 센서와 딥러닝 알고리즘을 이용한 거북목, 굽은어깨, 비대칭어깨 종합 검사 및 장거리 운전자 피로 분석에의 응용 |
| 이태희 | M.S. (2019) | Ansys | Estimation of Vehicle Roll Angle and Road Bank Angle Using Deep Neural Network |
| 오예균 | M.S. (2018) | Continental AG | 할박 배열에 의한 외란저감 연구 및 홀 자기센서의 적용 |
| 차현준 | M.S. (2018) | 현대자동차 | 선형 홀센서를 이용한 On-axis 조향각 센서 개발과 센서 융합을 통한 자기외란 보정 알고리즘 연구 |
| 이상유 | M.S. (2018) | 현대자동차 | 실리콘 카바이드 파워모듈 내 소자 배치와 상태특성을 반영한 전용 냉각구조 연구 |
| 이 덕희 | M.S. (2017) | 삼성전자 | 에너지 효율 향상과 시스템 안정성 확보를 위한 보조배터리 제어 연구 |
| 이 상헌 | M.S. (2016) | 현대자동차 | 센서 융합기반 yaw각 추정 알고리즘 및 평행 자동 주차시스템에서의 응용 |

## 최근 논문과 학회 발표 목록 (2021–2026)

국제 학술지 25편, 국내 학술지 2편, 국제 학회 발표·초청강연 37건, 국내 학회 발표·초청강연 24건이다. 학회 목록은 논문집 출판 여부를 구분하지 않는 발표 목록이며, 제목이 없는 초청강연도 행사명으로 기재되어 있다. 연도는 누리집 표기이고, 윤상원 교수의 2023년 9월 서울대 부임 이전 한양대 재직 시기 항목이 섞여 있다.[^journals][^jdom][^confint][^confdom][^faculty]

**2026**

- Yuna Lee, Jeong Hun Song, and Sang Won Yoon\*. "Stack-Height-Aware Thermal Management of HBM Packages via Selective NCF Thermal Conductivity Strategy". *국제 학술지 · Microelectronics Reliability, Vol. 185, 116286, October 2026*.
- Hobeom Han, Jung Su Yoon, Eun Pyo Hong, Suk-Kang Sung, Sang Won Yoon\*. "Modeling and Improvement of Heat-Flow Paths inside 3D-NAND First-Level Packages with Internal Metal Structures". *국제 학술지 · IEEE Transactions on Electron Devices, vol. 73, no. 4, pp. 2130-2136, April 2026*.
- Eun Pyo Hong and Sang Won Yoon\*. "Heat Dissipation Improvement Using Plugged Sidewall for Three-Dimensional (3D) Package of High-Stacked High Bandwidth Memory (HBM)". *국제 학술지 · Journal of Semiconductor Technology and Science, vol. 26, no. 2, pp. 97-105, A pr 2026*.
- A Yeong Choi, Jaejin Jeon, Jae Hyuk Lim, and Sang Won Yoon\*. "Embedded PCB and DBC-integrated design of 650 V GaN power modules with enhanced thermal and electrical performance". *국제 학술지 · Microelectronics Reliability, Vol. 179, 116053, 2026*.
- Jihwan Seong, A Yeong Choi, Jaejin Jeon, Jang Kwon Lim, Sang Won Yoon\*. "Imp roving Electrical and Thermal Performance of 650V GaN E-HEMT Modules Using a Cover-All Meandered Thick-Copper(CAMT) Interconnection". *국제 학술지 · IEEE Access, vol. 14, pp. 15883-15893, 2026*.
- S eung Hyun Won, Kyoung Kook Hong, Sang Won Yoon\*. "Balanced Vertical Structures for Thermal Expansion Matching and Reduced Thermomechanical Stress in Silicon Carbide Double-Sided Cooling Power Modules". *국제 학술지 · IEEE Transactions on Components, Packaging and Manufacturing Technology (vol. 16, no. 6, pp. 1303-1311, June. 2026)*.
- Sungtaek Hwang, Eun Pyo Hong, Min-Ki Kim, Dong Keun Jang and Sang Won Yoon\*. "Thermal Behavior in Vertically Stacked Cascode GaN HEMT Power Modules including Mutual Heating, Dissipation Disturbance, and Solder Voids". *국제 학술지 · IEEE Transactions on Components, Packaging and Manufacturing Technology, vol. 16, no. 2, pp. 276-284, Feb. 2026*.
- 국제 학회 · Sang Won Yoon, 12th Asia-Pacific Conference on Transducers and Micro-Nano Technology (APCOT 2026), Taichung, Taiwan, June 2026
- Seung Wan Jeung and Sang Won Yoon. "Simulation Analysis of Triple-Point Electric-Field Concentration and Mitigation via Localized Coating in High-Voltage SiC Power Modules". *국제 학회 · 2026 Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2026), Busan, Korea, July, 2026. (Oral Presentation)*.
- Hee Chan You and Sang Won Yoon. "Design Process for Balancing Electro-Thermal-Mechanical Trade-offs in Multi-Chip Power Modules via DBC Copper Thickness Selection". *국제 학회 · 2026 Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2026), Busan, Korea, July, 2026*.
- Se Jun Yang and Sang Won Yoon. "Cohesive Zone Modeling of Bonding Formation and Cooling Retention in Cu-Cu Hybrid Bonding with Cu Dishing". *국제 학회 · 2026 Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2026), Busan, Korea, July, 2026. (Oral Presentation)*.
- Jaejin Jeon, Sang Won Yoon. "Advanced Reliability Assessment of Power Modules Under Low Cycle Thermal Fatigue Through Redefined 3-D J-Integral". *국제 학회 · The Power Conversion and Intelligent Motion (PCIM Europe), Nuremberg, Germany, June 2026*.
- Seung Hyun Won, Dong Keun Jang, Sang Won Yoon. "Warpage Relaxation of Pre-Bent Cu Baseplates with Grooves During Reflow in Power Modules". *국제 학회 · The Power Conversion and Intelligent Motion (PCIM Europe), Nuremberg, Germany, June 2026*.
- A Yeong Choi, Sang Won Yoon. "DBC-Integrated PCB-Embedded GaN Power Module with Double-Sided Cooling for". *국제 학회 · Improved Electrical and Thermal Performance", The Power Conversion and Intelligent Motion (PCIM Europe), Nuremberg, Germany, June 2026*.
- Bonghak Lee, Sang Won Yoon. "Metal-Enhanced Waffle Wafer Design for Thermomechanical Warpage Reduction in Fan-Out Wafer-Level Packaging". *국제 학회 · IEEE 76th Electronic Components and Technology Conference (ECTC 2026),Orlando, USA, M ay. 2026 (Oral Presentation)*.
- Eun Pyo Hong and Sang Won Yoon. "Enhancing In-Package Thermal Management of 3D V-NAND Flash Memory Using Under-Periphery Thermal Pins (UPTPs) and Materials-and-Structure Co-Design". *국제 학회 · IEEE 76th Electronic Components and Technology Conference (ECTC 2026),Orlando, USA, May. 2026*.

**2025**

- Jaejin Jeon, Jeonghoon Song, Jun Young Oh, Seok Hwan Lee, Younghun Kim, Yun Ho Kim, Sam-Jong Choi and Sang Won Yoon\*. "Residual stress and deformation analysis considering adhesive material properties to enhance manufacturing of HBM". *국제 학술지 · Journal of Materials Research and Technology, September-October 2025*.
- J aejin Jeon and Sang Won Yoon\*. "Advanced Reliability Assessment Approach of Power Modules under Low-Cycle Thermal Fatigue through Redefined 3-D J-Integral". *국제 학술지 · IEEE Transactions on Components, Packaging and Manufacturing Technology, vol. 15, no. 5, pp.982-990, May 2025*.
- Jung Su Yoon and Sang Won Yoon\*. "Warpage Analysis and Improvement Approach of Transfer-Molded Power Semiconductor Modules Considering EMC Properties and Module Structure". *국제 학술지 · Journal of Semiconductor Technology and Science, vol. 25, no. 2, pp.154-159, April 2025*.
- Jeong Hun Song and Sang Won Yoon\*. "Comparative Study of Thermal Dissipation in increasing DRAM Layers of HBM using 3D FEA Simulations". *국제 학술지 · Journal of Semiconductor Technology and Science, vol. 25, no. 2, pp.142-147, April 2025*.
- J i Yong So, Young-Doo Yoon and Sang Won Yoon\*. "Thermal Analysis of Indirect Double-Sided Cooling Power Modules Considering the Impact of Thermal Interface Material Characteristics". *국제 학술지 · Journal of Semiconductor Technology and Science, vol. 25, no. 2, pp.148-153, April 2025*.
- 국제 학회 · Sang Won Yoon, International Symposium on Advanced Power Packaging (ISAPP 2025), Fukuoka, Japan, 2025
- Yuna Lee and Sang Won Yoon. "Thermal Conductivity-Aware Design Approach of Non-Conductive Film Layers for Enhanced Vertical Heat Dissipation in 3D HBM Package". *국제 학회 · 14th IEEE CPMT Symposium Japan (ICSJ2025), Nov. 2025*.
- Jaejin Jeon, Kyung Tae Min, SangWon Yoon. "Reducing Parasitic Inductance Through Power Terminal Grouping in SiC Power Modules for EV Applications". *국제 학회 · 2025 ICSCRM, Busan, Korea, Sep 2025*.
- Bonghak Lee, Seokjin Shin, SangWon Yoon. "RC Snubber Co-Design of SiC Power Modules considering Impact on Transient Switching Characteristics". *국제 학회 · 2025 ICSCRM, Busan, Korea, Sep 2025*.
- A Yeong Choi and SangWon Yoon. "Electrical and Thermo-Mechanical Analysis of 650V GaN Power Modules with Symmetric and Unsymmetric Lateral Layout using Power Cycling FEA Simulation". *국제 학회 · 2025 A sia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2025), Nara, Japan, July, 2025 (Oral Presentation)*.
- Bong Hak Lee and SangWon Yoon. "Prelimiary Study on Simulation Challenges in Warpage Analysis from Wafer- to Panel Level Packaging Using the Equivalent CTE model". *국제 학회 · 2025 A sia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2025), Nara, Japan, July, 2025*.
- Eun Pyo Hong and SangWon Yoon. "Heat Dissipation Improvement Using Plugged Sidewall for 3-Dimensional (3D) Package of High-Stacked High Bandwidth Memory (HBM)". *국제 학회 · 2025 A sia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2025), Nara, Japan, July, 2025*.
- Sun Seong Kwon and SangWon Yoon. "Comparative Estimation for the transition from Thermocompression Bonding to Direct Metal Bonding of High Bandwidth Memory(HBM) based on 3D Finite Element Analysis Simulations". *국제 학회 · 2025 A sia-Pacific Workshop on Advanced Semiconductor Devices (AWAD2025), Nara, Japan, July, 2025*.
- Sang Won Yoon, Jihwan Seong, Min-Ki Kim. "Experimental Validation of Parasitic Inductance Reduction by Me ander-shaped Cover-all Interconnection Design for 650V GaN e HEMT Power Modules". *국제 학회 · The Power Conversion and Intelligent Motion (PCIM Europe), Nuremberg, Germany, May 2025*.

**2024**

- Taerim Kwon and Sang Won Yoon\*. "Anomaly Detection of Motion Artifact in Photoplethysmography (PPG) Sensors using Unsupervised Learning". *국제 학술지 · IEEE Sensors Journal, vol. 24, no. 14, July 2024*.
- Jangmuk Lim, D. K. Jang and Sang Won Yoon\*. "Novel Temperature Calibration Method of E-mode and D-mode GaN Power Modules Considering Dynamic on-resistance". *국제 학술지 · IEEE Transactions on Industrial Electronics, vol. 71, no. 5, pp. 5245 - 5252, May 2024*.
- Seongmoo Cho, Sunghyun Pyun and Sang Won Yoon\*. "Analysis and Design Optimization of Tilted Rounded-Rectangular Pin-Fin Heat Sinks for xEV Double-Sided Cooling Power Module". *국제 학술지 · IEEE Journal of Emerging and Selected Topics in Power Electronics, vol 12, no. 2, pp.1803-1812, Apr 2024*.
- Hobeom Han , Gunhee Kim , Soohyung Choi , Amar Basu , and Sang Won Yoon\*. "Human Activity and Correlated Posture Monitoring using Earlobe-worn Wearable Sensor System and Deep Learning Algorithm". *국제 학술지 · IEEE Sensor Journal, vol. 24, no. 1, pp. 533-542, Jan 2024*.
- Sang Won Yoon. "Considerations for Packaging Solutions for Current Automotive Power Modules". *국제 학회 · 22nd International Symposium on Microelectronics and Packaging joined with the 18th International Conference Reliability and Stress-Related Phenomena in Nanoelectronics (ISMP-IRSP 2024), Nov. 2024*.
- Sang Won Yoon. "Packaging Approaches for Wide Bandgap Power Semiconductors: Challenges and Efforts". *국제 학회 · 11th Asia-Pacific Workshop on Widegap Semiconductors (APWS 2024), Oct. 2024 (Invited Talk)*.
- Sang Won Yoon. "Packaging Solutions for Power Semiconductors: Power Modules and Their Applications". *국제 학회 · SiC Power Semiconductor Summit, Semicon Korea, Feb. 2024 (Invited Talk)*.
- Hyunseup Jo and Sang Won Yoon. "Visual and Inertial Sensor Fusion Approach for Visual Inertial Odometry Used in Vehicle Localization". *국제 학회 · IEEE Sensors, 2024 (Oral Presentation)*.
- Jung Su Yoon and SangWon Yoon. "Dependency Analysis of Wargapge in Semiconductor Package by Epoxy Molding Compound Property with simulatnous consideration of Shrinkage and CTE Mismatch". *국제 학회 · 2024 A sia-Pacific Workshop on Advanced Semiconductor Devices (A W AD2024), July, 2024*.
- Jeong Hun Song and SangWon Yoon. "Thermal Dissipation Analysis of High Bandwidth Memory(HBM) using 3D Finite Element Analysis(FEA) simulations". *국제 학회 · 2024 Asia-Pacific Workshop on Advanced Semiconductor Devices (A W AD2024), July, 2024*.
- Ji Yong So and SangWon Yoon. "Heat Dissipation Performance Dependency on Thermal Interface Material used in Indirect Double-Sided Cooling Power Modules". *국제 학회 · 2024 Asia-Pacific Workshop on Advanced Semiconductor Devices (A W AD2024), July, 2024 (Oral Presentation)*.
- Kyung Tae Min and SangWon Yoon. "Approach to Reduce Parasitic Inductance in Automotive Power Modules Considering Selected Parallelization of Power Terminals". *국제 학회 · International Electric Vehicle Symposium and Exhibition (EVS37), April, 2024 (Oral Presentation)*.
- 윤상원. "반도체 패키징의 다중물리적 특성 파악을 위한 해석 기법". *국내 학회 · 한국반도체디스플레이기술학회 (KCSDT 2024 GUMI), May 2024*.
- 윤중수, 윤상원. "반도체 패키지의 휨 특성에 대한 에폭시 몰딩 컴파운드(Epoxy Molding Compound)의 열전도율 및 열팽창 계수 영향 연구". *국내 학회 · 대한전자공학회 2024년도 하계종합학술대회, June, 2024*.
- 소지용, 윤상원. "간접 양면 냉각 파워 모듈의 열 인터페이스 재료에 따른 냉각 성능 비교". *국내 학회 · 대한전자공학회 2024년도 하계종합학술대회, June, 2024*.
- 송정훈, 윤상원. "고대역폭 메모리 적층구조에서의 발열상황 및 방열특성 사전 점검을 위한 유한 요소법 적용 연구". *국내 학회 · 대한전자공학회 2024년도 하계종합학술대회, June, 2024*.
- 김진민, 윤상원. "LSTM 기반 차량 모델 불확실성 변수 예측에 Sliding Mode Control 적용 가능성 연구". *국내 학회 · 제 34회 통신정보 합동학술대회, Apr. 2024*.
- 전재진, 신석진, 민경태, 윤상원. "리드프레임 구조 변형 및 스너버 회로를 통한 자동차용 SiC 파워모듈의 기생인덕턴스 감소와 스위칭 손실 분석". *국내 학술지 · J. Microelectron. Packag. Soc., 31(3), 99-104 (2024)*.
- 조현습, 김진민, 윤상원\*. "가상환경 내 자율주행 차량 데이터 취득을 위한 CARLA 기반 테스트 시나리오 제안". *국내 학술지 · 한국 자동차 공학회 국문 논문집, Vol.3, Mar. 2024*.

**2023**

- Min-Ki Kim, Y oung-Doo Yoon and Sang Won Yoon\*. "Actual Maximum Junction Temperature Estimation Process of Multichip SiC MOSFET Power Modules with New Calibration Method and Deep Learning". *국제 학술지 · IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 11, no. 6, pp. 5602-5612, Dec 2023*.
- Seongmoo Cho and Sang Won Yoon\*. "Analysis Model for Thermal Resistance of Double-sided Cooling Power Module with Pin-Fin Heat Sink used in xEVs". *국제 학술지 · Journal of Power Electronics, vol. 23, pp. 1880-1887, Dec 2023*.
- Sunghyun Pyun, Seongmoo Cho, and Sang Won Yoon\*. "Analysis of Perforated Pin Design use in Automotive SiC Power Module Heatsink". *국제 학술지 · Journal of Power Electronics, vol. 23, pp. 1888–1895, Dec 2023*.
- Hobeom Han, Sang Won Yoon. "Comprehensive LiDAR Sensor Noise Model and Application to Texture and Object Classification Using Custom Deep Learning". *국제 학회 · IEEE Sensors Conference, Oct.-Nov. 2023*.
- Hyunjun Cha, Yegyun Oh, Hobeom Han, Sang Won Yoon. "Plural Kalman Filter-Based Algorithm for Suppressing Strong Magnetic Disturbance in Automotive Steering Angle Sensors". *국제 학회 · IEEE Sensors Conference, Oct.-Nov. 2023*.
- Jaemyung Lim and Sang Won Yoon. "Thermal Modeling for Chiplet Package". *국제 학회 · International Symposium on Microelectronics and Packaging (ISMP), Nov. 2023 (Oral presentation)*.
- Sang Won Yoon, J. Lim, J. Jeon, J. Seong, H. Han, S. M. Cho. "Multi-Physics Analysis considering Electrical and Thermal Properties of Power Module used in Automotive and Industrial Applications". *국제 학회 · International Symposium on Microelectronics and Packaging (ISMP), Nov. 2023 (Oral presentation)*.
- Seokjin Shin and Sang Won Yoon. "Simulation and Experiment Investigation of Overshoot Voltage and Settling Time in RC Snubber Integrated Silicon Carbide Power Module". *국제 학회 · Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD 2023), Yokohama, Japan, July, 2023*.
- SeungHyun Won and Sang Won Yoon. "Thermal Performance Analysis of Vertically Stacked Structure in Double-Sided Cooling SiC MOSFET Power Modules". *국제 학회 · Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD 2023), Yokohama, Japan, July, 2023*.
- Jaehyun Cho and Sang Won Yoon. "Comparative Analysis of Epoxy Molding Compound (EMC) Material Properties Used in Double-sided Cooling Power Module". *국제 학회 · 11th International Conference on Power Electronics (ICPE 2023-ECCE Asia), Jeju, Korea, May 2023 (Oral presentation)*.
- 윤상원. "SiC의 응용분야: 파워모듈 패키지와 xEV에의 응용 관점에서". *국내 학회 · 2023 SiC 반도체 컨퍼런스, 한국전기전자재료학회 하계학술대회, 2023*.
- 한호범, 김진민, 조현습, 윤상원. "텍스처에 의한 라이다 센서 노이즈 분석과 딥러닝을 활용한 객체분류 가능성 연구". *국내 학회 · 대한전자공학회 2023년도 추계학술대회, Nov. 2023*.
- 민경태, 윤상원. "파워모듈의 Heatsink 재료와 접합방에 따른 연구 효율". *국내 학회 · 2023 한국 자동차공학회 추계학술대회 및 전시회, Oct, 2023*.
- 민경태, 원승현, 윤상원. "Lead Frame 단자의 병렬성을 활용한 파워 모듈 기생 인덕턴스 저감 가능성 연구". *국내 학회 · 대한전자공학회 2023년도 하계종합학술대회, June, 2023*.
- 염원준, 김진민, 조현습, 윤상원. "Generative 모델을 활용한 SiC 파워모듈의 과도응답 주파수 추정 가능성 연구". *국내 학회 · 대한전자공학회 2023년도 하계종합학술대회, June, 2023*.
- 윤상원. "자동차 ADAS 센서 동작특성과 기상환경변수를 고려한 가상환경 시뮬레이 션용 센서모델링". *국내 학회 · April, 2023*.

**2022**

- J. Heo, H. Lee, Sang Won Yoon and K. Kim. "Responses to Take-Over Request in Autonomous Vehicles: Effects of Environmental Conditions and Cues". *국제 학술지 · IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 12, pp. 23573-23582, Dec 2022*.
- H. -J. Lee, Sang Won Yoon and Y. -D. Yoon. "Hybrid Distribution Transformer Based on an Existing Distribution Transformer and a Series-Connected Power Converter". *국제 학술지 · IEEE Transactions on Power Delivery, vol. 37, no. 5, pp. 4202-4211, Oct 2022*.
- Sang Won Yoon. "Design and Analysis Approaches of Power Modules used in Various Automotive Applications". *국제 학회 · International Welding & Joining Conference-Korea 2022 (IWJC-Korea 2022), Oct. 2022 (Invited Talk)*.
- 편성현, 신석진, 윤상원. "xEV 파워모듈을 위한 나사산 형성 방열핀의 냉각 성능 분석". *국내 학회 · 2022 한국자동차공학회 추계학술대회 및 전시회, Nov, 2022*.
- 최수형, 윤상원. "우천시 역산란 현상을 반영한 라이다 포인트 클라우드 분석기법". *국내 학회 · 2022 한국자동차공학회 추계학술대회 및 전시회, Nov, 2022*.
- 민경태, 원승현, 윤상원. "xEV용 인버터 파워모듈 최대온도와 시스템 레벨 동작점의 상관성 분석". *국내 학회 · 2022 한국자동차공학회 추계학술대회 및 전시회, Nov, 2022*.
- 윤성준, 오세찬, 김진민, 윤상원. "실측 기반 라이다 노이즈 모델 분석과 CARLA 시뮬레이터 기반 검증". *국내 학회 · 2022 한국자동차공학회 추계학술대회 및 전시회, Nov, 2022*.
- 염원준, 윤상원. "Formula Student 레이스카의 선회능력 향상을 위한 All Wheel Steering 제어 설계". *국내 학회 · 2022 한국자동차공학회 추계학술대회 및 전시회, Nov, 2022*.
- 신석진, 윤상원. "전력변환 안정성과 효율 향상을 위한 RC-스너버 통합형 SiC 파워모듈 설계". *국내 학회 · 대한전자공학회 2022년도 하계종합학술대회, Jun, 2022*.
- 오세찬, 윤성준, 최수형, 윤상원. "CARLA 시뮬레이터 내 차량 센서를 이용한 응급 차량 주행 시나리오 개선". *국내 학회 · 대한전자공학회 2022년도 하계종합학술대회, Jun, 2022*.
- 국내 학회 · 오세찬, 윤성준, 최수형, 한호범, 김경진, 최기한, 김도은, 윤상원, 강수용 "자율주행 시뮬레이터와 엣지 컴퓨팅을 활용한 교차로 꼬리물기 방지 기법"﻿, 대한전자공학회 2022년도 하계종합학술대회, Jun, 2022

**2021**

- J. Lim, J. Jeon, J.-h. Seong, J. Cho, S. M. Cho, K. S.Kim, Sang Won Yoon\*. "Iterative Electrical–Thermal Coupled Simulation Method of Automotive Power Module used in Electric Power Steering System". *국제 학술지 · IEEE Access vol. 9, pp. 164712-164719, Dec 2021*.
- J. Lim, J. Seong, J. Jeon, Y.S. Kim, H.-C. Im, W.S. Hong, Sang Won Yoon\*. "Design and Experimental Evaluation of Transfer-Molded 650 V Super-Junction mosfet Power Module for Industrial Applications". *국제 학술지 · IEEE Transactions on Industry Applications, vol. 57, no. 6, pp. 6295-6305, Nov.-Dec 2021*.
- J. -Y. Ryu, S. -W. Hwang, J. -W. Chin, Y. -S. Hwang, Sang Won Yoon and M. -S. Lim. "Mathematical Modeling of Fast and Accurate Coupled Electromagnetic-Thermal Analysis". *국제 학술지 · IEEE Transactions on Industry Applications, vol. 57, no. 5, pp. 4636-4645, Sept.-Oct. 2021*.
- J. Jeon, J.-H. Seong, J. Lim, M. K. Kim, T. Kim, Sang Won Yoon\*. "Finite Element and Experimental Analysis of Spacer Designs for Reducing Thermomechanical Stress in Double-Sided Cooling Power Modules". *국제 학술지 · IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 9, no. 4, August 2021*.
- Sang Won Yoon. "Power semiconductor packaging approaches - A way to a reliable power module system". *국제 학회 · 19th International Symposium on Microelectronics and Packaging (ISMP), Nov. 2021 (Invited Talk)*.
- Sang Won Yoon. "Approaches of Highly Reliable Package for High Power Electronic Devices". *국제 학회 · Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices (AWAD), Aug. 2021 (Invited Talk)*.
- Min-Ki Kim, Sang Won Yoon. "Thermal Impedance Measurement Utilizing Optical Measurement and Thermal Impedance Model for Multichip SiC MOSFET Module with Anti-Parallel Diodes". *국제 학회 · The Power Conversion and Intelligent Motion (PCIM Europe), May 2021 (Oral presentation)*.
- 조용식, 윤상원. "1200V 100A 급 SiC MOSFET과 Cascode SiC FET 하프 브리지 파워 모듈 슬루율 제어 기법 연구". *국내 학회 · 제4회 반도체공학회 종합학술대회 및 정기총회, Dec, 2021*.
- 김경진, 최기한, 김도은, 오세찬, 윤성준, 최수형, 한호범, 윤상원, 강수용. "엣지 컴퓨팅을 이용한 교차로 꼬리물기 방지 시스템". *국내 학회 · 2021 한국자동차공학회 추계학술대회 및 전시회, Nov, 2021*.
- 신석진, 윤상원. "xEV SiC 멀티칩 파워 모듈의 커넥터 위치 변경을 통한 전류 불균형 저감 연구". *국내 학회 · 2021 한국자동차공학회 추계학술대회 및 전시회, Nov, 2021*.
- 편성현, 윤상원. "Perforated 방열 Pin을 이용한 xEV용 SiC 파워 모듈의 냉각 성능 향상". *국내 학회 · 2021 한국자동차공학회 추계학술대회 및 전시회, Nov, 2021*.
- 권하연, 윤상원. "저가 IMU 센서와 딥 앙상블을 활용한 차량 오일러 각 추정 연구". *국내 학회 · 2021 한국자동차공학회 추계학술대회 및 전시회, Nov, 2021*.

## 과제

정부과제와 산학과제 31건이다. 시작·종료 또는 참여기간의 날짜가 2021년 10월 22일–2026년 10월 22일 범위에 드는 28건과, 기간을 적지 않은 3건을 함께 보인다. 기간 없는 항목은 최근 과제로 시기를 특정하지 않는다. 윤상원 교수의 2023년 9월 서울대 부임 이전 한양대 재직 시기 과제도 포함된다. 역할·기관·전체 기간과 별도 참여기간은 누리집 표기이며, On-going은 진행 중이라는 게시 표기다.[^projects][^faculty]

- [서울대-공동] 송배전용 3.3kV급 SiC 전력반도체 모듈 국산화 기술 개발(산업통상부) - 2026.04.~2029.12. (On-going)
- [서울대-공동] 차세대 소재 적용 고출력 전력반도체 개발 - 2026.04. ~ 2026.12. (On-going)
- [서울대-공동] 전기자동차용 구동회로 내장형 파워모듈 기술개발(산업통상부) - 2026.04. ~2029.12. (On-going)
- [서울대-책임] SiC/GaN-on-Si 기반 차세대 수직적층형 파워-연산 Co-Packaging 핵심 기술 연구(과학기술 정보통신부) - 2026.03. ~2031.02. (On-going)
- [서울대-책임] 화합물 전력 반도체 전문 인력 양성 (산업통상자원부) - 2025.03.~2030.02. (On-going)
- [서울대-공동] GaN·SiC 전력모듈 국산화 기반 서버용 초고밀도 전원공급모듈 수요연계 기술 개발 (산업통상자원부) - 2025.04.~2028.12. (On-going)
- [서울대-공동] 전기자동차용 고전압 GaN 전력모듈 기술개발 (산업통상자원부) - 2024.04.~2028.12. (On-going)
- [참여] 서울대학교 반도체특성화대학사업단 (On-going) (기간 표기 없음)
- [참여] 서울대학교 정보기술 미래인재 교육연구단 (BK21 Four, 교육부) - 2024.03. ~ (On-going)
- [단독] 친환경 자동차용 차세대 전력반도체 신뢰성 평가 및 계측 기술 개발을 통한 한국형 반도체 수명예측모델 연구 - 과학기술정보통신부 (연구재단, 중견연구) - 2023.03. ~ 2026.02.
- [참여] 전기동력 수직이착륙 도심 항공 모빌리티의 전기추진시스템 기초연구실 - 과학기술정보통신부 (기초연구실지원사업 후속과제) - 2023.03. ~ 2026.02.
- [책임] 고신뢰성 차량용 반도체 전주기 지원을 위한 성능평가 인증지원 - 산업통상자원부 (한국산업기술진흥원) - 2022.04. ~ 2024.12.
- [책임] 다중 통신기술 네트워크 로드밸런싱 기술개발 - 과학기술정보통신부 (정보통신기획평가원, 자율주행기술개발혁신사업) - 2022.04. ~ 2024.12.
- [책임 -> 참여] AI 반도체 이종집적 패키지의 발열 모델링과 방열 아키텍처 기술 개발 - 과학기술정보통신부 (정보통신기획평가원, ICT융합산업혁신기술개발) - 2023.04. ~2027.12. (참여기간 : 2023.04~2023.12.)
- [참여] 미래형자동차(자율주행, 커넥티드) 핵심인력양성 - 산업통상자원부 - 2022.03. ~ 2027.02. (참여기간: 2022.03~2023.08)
- [참여] 친환경자동차(xEV) 부품개발 R&D 전문인력 양성 - 산업통상자원부 - 2021.01. ~ 2026.02. (참여기간: 2021.01~2023.08)
- [참여] 미래자동차-소프트웨어 융복합 혁신인재 양성 교육연구단 - BK21 Four - (참여기간: 2020.09~2023.08)
- [참여] 근적외선 광자 기반 e-파워트레인 능동 에너지관리 기초연구실 - 과학기술정보통신부 - 2020.07. ~ 2023.02.
- [단독] 자율주행 전기자동차용 조향각 센서의 EMI 외란 강건성 확보를 위한 센서융합 및 머신러닝 기법, 기본연구 - 과학기술정보통신부 - 2020.06. ~ 2023.02.
- [참여] 스마트 센서의 독립전원을 위한 에너지 하베스팅 소재 및 모듈 개발 - 산업통산자원부 (에너지기술평가원) - 2018.05. ~ 2022.04.
- [참여] 미래형자동차 부품 및 서비스 R&D 인력양성 및 산학연계형 생태계 구축, 산업기술혁신사업 - 산업통상자원부 (한국산업기술진흥원) - 2017.03. ~ 2022.02.
- [주관] 반도체 패키지 공동연구 (삼성전자) (기간 표기 없음)
- [참여] 고전력 WBG 전력변환 시스템용 재료 적용 연구 (기간 표기 없음)
- [단독] Wafer-level 첨단 반도체 패키징 (삼성전자) 2024.05~ (3차년도) (On-going)
- [단독] 파워반도체 모듈 과제 (삼성전자) - 2024.06 ~ (3차년도) (On-going)
- [참여] NAND 반도체 클러스터 과제 - 삼성전자 - 2024.03 ~ (3차년도) (On-going)
- [단독] 오픈소스 시뮬레이션 기반 제어기 평가환경 구축 - iVH - 2023.04. ~ 2023.11.
- [단독] 전기차 인버터용 SiC MOSFET 모듈 개발 설계 및 해석 - LX세미콘 - 2022.05-2023.04
- [단독] GaN EVDC 모듈개발과제 응력해석 - 아모센스 - 2022
- [단독] 전력변환 효율 및 안정성 향상을 위한 스너버 통합형 파워모듈 회로 해석 및 개발 - 현대자동차 - 2021.03. ~ 2022.02.
- [책임] ADAS/자율주행환경을 고려한 BLRTC 해석 방법론 및 기능 안전 Process (FSM) 개선 아이템 개발 - SK하이닉스 - 2020. 03. ~ 2022.02.

## 특허

국내 등록 8건(2022년 2월–2025년 6월)과 국내 출원 11건(2024년 6월–2026년 9월)이다. 윤상원 교수의 서울대 부임 이전 한양대 재직 시기 연구가 포함된 개인 특허 목록이다. 제목을 적지 않은 출원은 출원번호·게시된 발명자·날짜만 보인다. 번호·상태·날짜는 누리집 표기다.[^patents][^faculty]

- 윤상원, 권태림, “맥파 신호에서 이상 신호를 탐지하는 방법”, Korea Patent, (10-28266580000, 2025.06.24)
- 윤상원, 임장묵, "HEMT 파워 모듈의 온도 추정을 위한 캘리브레이션 방법 및 온도 추정 방법”, Korean Patent (10-27886700000, 2025.03.26)
- 윤상원, 편성현, "파워 모듈을 위한 히트싱크", Korean Patent (10-27811420000, 2025.03.10)
- 윤영두, 이현준, 주제억, 윤상원, "전동기 제정수 추정 장치 및 그 방법", Korean Patent, (10-27274020000 , 2024.11.04.)
- 윤상원, 조성무, "파워 모듈을 위한 히트싱크", Korean Patent, (10-27091380000, 2024.9.19)
- 박성준, 김재균, 이태희, 윤상원 , "방진 커넥터 및 이를 포함하는 차량", Korean Patent, (10-26556910000, 2024.04.03.)
- 윤상원, 권하연, “파워케이블 홀더”, Korea Patent, (10-26106860000, 2023.12.01)
- Sang Won Yoon, M. Byeon, “라이다 센서의 임계값을 조절하는 방법”, Korean Patent, (10-2367601, Feb. 2022)
- 홍은표, 한호범, 윤상원, Korea Patent Application, 10-2026-0176566 (Filed Sept. 2026)
- 권순성, 송정훈, 윤상원, 홍은표, Korea Patent Application, 10-2026-0165582 (Filed Sept. 2026)
- Korea Patent Application, 10-2026-0003142 (Filed Jan. 2026)
- Korea Patent Application, 10-2025-0168026 (Filed Nov. 2025)
- Korea Patent Application, 10-2025-0160822 (Filed Oct. 2025)
- 윤상원, 김진민, 조현습, Korea Patent Application, 10-2025-0061372 (Filed May. 2025)
- 윤상원, 윤중수, 홍은 표, Korea Patent Application, 10-2025-0050591 (Filed April. 2025)
- 윤상원, 홍은표, 윤중수, Korea Patent Application, 10-2025-0052880 (Filed April. 2025)
- 윤상원, 김진민, 조현습, "스테레오 카메라 융합 칼만필터 기반 측정법," Korean Patent, 10-2024-0136841 (Filed Oct. 2024)
- 윤상원, 한호범, Korea Patent Application, 10-2024-0082562 (Filed June. 2024)
- 윤상원, 한호범, Korea Patent Application, 10-2024-0082556 (Filed June. 2024)

## 수상과 선정

Awards 페이지 가운데 2021년 11월–2026년 7월의 8건이다. 윤상원 교수의 2023년 9월 서울대 부임 이전 한양대 재직 시기 수상도 포함한다. 학회 발표상, 학생 논문상, 우수학생과 학회 참가 지원 선정을 구분해 적었다.[^awards][^faculty]

- 2026.07 · 송정훈, 화합물전력반도체 전문인력 양성사업 우수학생 수상
- 2026.07 · 정승완, AWAD 2026 Outstanding Presentation Award 수상
- 2026.05 · 이봉학, ECTC 2026 Student Travel Grant 선정
- 2025.07 · 최아영, AWAD 2025 Certificate of Young Researcher Award 수상
- 2022.12 · 윤성준, IEEE Seoul Section Student Paper Contest Best Student Paper Award - Gold 수상
- 2022.12 · 권태림, IEEE Seoul Section Student Paper Contest Best Student Paper Award - Bronze 수상
- 2022.12 · 편성현, IEEE Seoul Section Student Paper Contest Best Student Paper Award - Bronze 수상
- 2021.11 · 윤상원, 제14회 반도체의 날 한국반도체산업협회장 상 수상

## 소식

첫 화면이 2024년 8월–2025년 9월 날짜로 게시한 과제 시작·학술 강연·위원 위촉 소식이다.[^home]

- 2025.09 · 윤상원 교수, PCIM Europe 자문위원 위촉
- 2025.09 · 윤상원 교수, International Conference on Silicon Carbide and Related Materials 2025에서 튜토리얼 강연
- 2024.08 · 현대자동차·삼성전자·세미파워렉스와 새 과제 시작

## 연락

- 홈페이지: <https://sites.google.com/view/smeetsnu>
- 교수 전화: 02-880-1759[^faculty]
[^home]: 첫 화면. <https://sites.google.com/view/smeetsnu> 2026-10-26 열람.
[^pi]: PI. <https://sites.google.com/view/smeetsnu/people/pi> 2026-10-26 열람.
[^team]: Team. <https://sites.google.com/view/smeetsnu/people/team> 2026-10-26 열람.
[^alumni]: Alumni. <https://sites.google.com/view/smeetsnu/people/alumni> 2026-10-26 열람.
[^objective]: Research Objectives. <https://sites.google.com/view/smeetsnu/research/objective> 2026-10-26 열람.
[^packaging]: Semiconductor Packaging. <https://sites.google.com/view/smeetsnu/research/semiconductor-packaging> 2026-10-26 열람.
[^projects]: Projects. <https://sites.google.com/view/smeetsnu/research/projects> 2026-10-26 열람.
[^journals]: Journals (International). <https://sites.google.com/view/smeetsnu/publication/journalsinternational> 2026-10-26 열람.
[^jdom]: Journals (Domestic). <https://sites.google.com/view/smeetsnu/publication/journalsdomestic> 2026-10-26 열람.
[^confint]: Conferences (International). <https://sites.google.com/view/smeetsnu/publication/conferencesinternational> 2026-10-26 열람.
[^confdom]: Conferences (Domestic). <https://sites.google.com/view/smeetsnu/publication/conferencesdomestic> 2026-10-26 열람.
[^patents]: Patents. <https://sites.google.com/view/smeetsnu/publication/patents> 2026-10-26 열람.
[^awards]: Awards. <https://sites.google.com/view/smeetsnu/awards> 2026-10-26 열람.
[^faculty]: 서울대학교 전기·정보공학부 윤상원 교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p893> 2026-10-26 열람.
[^p1]: H. Han 외, S. W. Yoon, IEEE Transactions on Electron Devices 73, 2130-2136 (2026). <https://doi.org/10.1109/TED.2026.3667123> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/401531184_Modeling_and_Improvement_of_Heat-Flow_Paths_Inside_3D-nand_First-Level_Packages_With_Internal_Metal_Structures> 2026-10-26 열람.
[^p2]: J. Seong 외, S. W. Yoon, IEEE Access 14, 15883-15893 (2026). <https://doi.org/10.1109/ACCESS.2026.3658650> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/400200303_Improving_Electrical_and_Thermal_Performance_of_650-V_GaN_E-HEMT_Modules_Using_a_Cover-All_Meandered_Thick-Copper_CAMT_Interconnection> 2026-10-26 열람.
[^p3]: S. H. Won, K. K. Hong, S. W. Yoon, IEEE Transactions on Components, Packaging and Manufacturing Technology. <https://doi.org/10.1109/TCPMT.2025.3641249> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/398468923_Balanced_Vertical_Structures_for_Thermal_Expansion_Matching_and_Reduced_Thermomechanical_Stress_in_Silicon_Carbide_Double-Sided_Cooling_Power_Modules> 2026-10-26 열람.
[^p4]: J. Jeon, S. W. Yoon, IEEE Transactions on Components, Packaging and Manufacturing Technology. <https://doi.org/10.1109/TCPMT.2024.3522123> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/387393399_Advanced_Reliability_Assessment_Approach_of_Power_Modules_under_Low-Cycle_Thermal_Fatigue_through_Redefined_Three-Dimensional_J-Integral> 2026-10-26 열람.
[^p5]: S. Cho, S. Pyun, S. W. Yoon, IEEE Journal of Emerging and Selected Topics in Power Electronics 12, 1803-1812 (2024). <https://doi.org/10.1109/JESTPE.2024.3354772> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/377459538_Analysis_and_Design_Optimization_of_Tilted_Rounded-Rectangular_Pin-Fins_Heat_Sink_for_xEV_Double-Sided_Cooling_Power_Module> 2026-10-26 열람.
[^p6]: H. Han 외, S. W. Yoon, IEEE Sensors Journal 24, 533-542 (2024). <https://doi.org/10.1109/JSEN.2023.3332897> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/375806401_Human_Activity_and_Correlated_Posture_Monitoring_using_Earlobe-worn_Wearable_Sensor_System_and_Deep_Learning_Algorithm> 2026-10-26 열람.
[^p7]: T. Kwon, S. W. Yoon, IEEE Sensors Journal 24, 23163-23172 (2024). <https://doi.org/10.1109/JSEN.2024.3404558> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/381021704_Anomaly_Detection_of_Motion_Artifact_in_Photoplethysmography_PPG_Sensors_using_Unsupervised_Learning> 2026-10-26 열람.

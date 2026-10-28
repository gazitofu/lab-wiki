# 전자파융합 연구실 (Wave Fusion Laboratory, WAVE FUSION LAB)

**서울대학교 공과대학 전기·정보공학부 · 오정석 교수**

- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 메타물질·메타광학[^meta], 집적회로 설계[^ic], 무선·이동통신[^wireless], 무선 전력 전송[^wpt], 과학·공학 AI[^ai]
- 홈페이지: <http://wfl.snu.ac.kr>

> 안테나·메타표면과 고주파 회로를 함께 설계하고, 전파 전달 계산과 생성형 인공지능으로 통신·전력 전달·전자파 해석 문제를 푸는 연구실이다.

## 무엇을 연구하나

전자파융합 연구실은 **무선 연결에 쓰는 안테나·표면·회로와 전파 해석 소프트웨어**를 함께 연구한다. 안테나(전기 신호를 전파로 내보내거나 전파를 전기 신호로 바꾸는 장치), 인공 구조로 전파를 조절하는 메타표면, 고주파 집적회로, 시스템 시뮬레이터가 네 연구 갈래다. 신호는 정보를 전달하거나 어떤 상태를 나타내는 물리량의 변화이며, 시뮬레이터는 대상의 동작을 모형으로 계산하는 도구다.[^research]

첫째는 **스마트폰과 패키지에 통합하는 안테나**다. 패키지는 반도체 칩을 보호하고 외부 회로와 연결하는 구조다. Antenna-in-Package는 패키지 안에 안테나를 통합하는 기술을 뜻한다. 안테나·메타표면·스마트폰 덮개를 처음부터 함께 설계해 전파가 도달하는 방향 범위를 개선하고, 화면의 금속 구조에 직접 결합하는 안테나도 연구한다. 이때 화면의 가시성과 터치 감도를 개선할 수 있을 것으로 기대한다고 설명한다. 움직임 감지용 패키지 안테나와 여러 층의 인쇄회로기판으로 만드는 배열 안테나도 소개한다. 배열 안테나는 여러 안테나를 배치해 전파의 모양과 방향을 조절하는 장치다.[^aip]

둘째는 **편광과 전파의 방향을 조절하는 메타표면**이다. 메타표면은 표면에 배치한 인공 구조로 파동의 진행과 성질을 조절하는 구조이고, 편광은 파동을 이루는 전기장의 진동 방향과 시간에 따른 변화 양상이다. 들어오는 전파의 편광에 따라 빔(특정 방향으로 집중된 파동)의 모양을 바꾸는 구조와, 단위 구조의 배치로 방향을 조절하는 표면을 설계한다. 액정(액체의 흐름성과 분자 배열의 방향성을 함께 지닌 물질)의 전기적 성질을 전압으로 바꾸어 원하는 파면(파동의 진동 상태가 같은 위치를 이은 면)을 만드는 능동 표면도 개발했다. 전압은 전하가 두 지점 사이를 이동할 때 전하량당 바뀌는 에너지다. 위상은 반복되는 파동의 한 주기 안에서의 위치다. 이를 이용해 별도의 위상 변환기(신호의 위상을 원하는 만큼 바꾸는 회로) 없이 전파의 형태를 바꾸는 연구다.[^meta]

셋째는 **이동통신과 무선 전력 전송용 집적회로**다. 집적회로는 전자 부품과 연결을 한 칩에 모아 놓은 회로다. 고주파는 진동이나 반복이 빠르게 일어나는 주파수 영역을 가리키며, 주파수는 일정 시간에 진동이나 반복이 일어나는 횟수다. MMIC(모놀리식 마이크로파 집적회로, Monolithic Microwave Integrated Circuits) 갈래에서 전력증폭기(입력 신호의 전력을 키우는 회로), 위상 변환기, 발진기(주기적으로 변하는 전기 신호를 만드는 회로)를 설계한다. CMOS(상보형 금속 산화물 반도체, Complementary Metal-Oxide-Semiconductor. 성질이 상보적인 두 종류의 트랜지스터를 조합하는 기술), 갈륨비소·질화갈륨 공정으로 전력증폭 회로를 연구한다. RIS(재구성 지능형 표면, Reconfigurable Intelligent Surface. 전기적 제어로 전파에 대한 반응을 바꾸는 인공 표면)와 CMOS 회로를 결합해 수신 신호를 증폭하려는 목표도 있다. 무선 전력 전송(전선 없이 자기장이나 전자기파로 전력을 보내는 기술)을 위한 증폭 회로와, 생체조직에 자극 신호를 전달하는 회로·탐침의 설계도 다룬다.[^ic][^wpt]

넷째는 **전파 전달 계산과 인공지능 기반 전자파 설계**다. 광선 추적(파동의 진행을 경로로 나타내고 주변 물체와의 상호작용을 따라 계산하는 방법)으로 실내외 무선 채널(송신기와 수신기 사이에서 신호가 전달되는 경로와 특성)을 모형화한다. 선박의 전자파 간섭과 차폐를 계산하고, 휴대기기의 전력증폭기에서 생길 신호 왜곡을 미리 보정하는 디지털 사전 왜곡(Digital Pre-Distortion) 시뮬레이터도 개발한다. 생성형 인공지능(자료의 패턴을 배워 새 자료를 만드는 인공지능) 연구에서는 위상 정보 없는 근거리 측정으로 멀리서의 전파를 예측하는 모형과, 원하는 성능에서 설계 조건을 구하는 역설계 방법을 개발하고 있다. 설계 과정에 물리적 제약과 관계를 직접 넣는 것이 목표다.[^sim][^ai]

## 주요 연구 주제

### 1. 스마트폰·패키지 안테나의 통합 설계

스마트폰 덮개와 안테나·메타표면을 함께 설계하고, 화면 통합 안테나와 여러 층의 패키지 안테나를 연구한다. 대표 논문은 하나의 세라믹 공정으로 안테나와 회로·표면을 함께 만든 연구와 스마트폰 세라믹 덮개에 맞춘 메타표면 연구다.[^aip][^p1][^p2]

### 2. 액정 메타표면과 전파 제어

편광에 반응하는 메타표면과 전압으로 성질을 바꾸는 액정 표면으로 전파의 진행 방향과 모양을 조절한다. 대표 논문은 편광과 방향을 함께 바꾸는 표면, 전압으로 방향 전환 응답을 조절하는 액정 반사 배열을 다룬다.[^meta][^p3][^p4]

### 3. 고주파 회로와 전력 전달

이동통신용 전력증폭기·위상 변환기·발진기, 무선 전력 전송용 증폭 회로, 생체 자극용 신호 발생·전달 회로를 연구한다. 대표 논문은 양방향 위상 변환기와 여러 주파수 구간에서 동작하는 발진기다.[^ic][^wpt][^p5][^p6]

### 4. 전파 전달 계산과 인공지능 역설계

실내외 전파의 경로를 계산하는 광선 추적, 신호 왜곡 보정, 생성형 인공지능을 이용한 전파 예측과 역설계를 다룬다. 대표 논문은 도시 실외의 전파를 계산하는 방법과 실외에서 실내로 이어지는 경로를 포함한 계산 방법이다.[^sim][^ai][^p7][^p8]

## 대표 논문

Journal의 2021–2026년 구역에서 오정석 교수가 마지막 저자인 서울대 재직 시기 논문을 네 연구 갈래에 두 편씩 골랐다. "쉽게 말하면" 칸은 각 논문의 등록 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Sub-THz Polarization-Dependent Beam-Steerable Metasurface Antenna-in-Package for 6G Communication Constructed Using an LTCC Process](https://doi.org/10.26866/jees.2026.1.r.342) · Journal of Electromagnetic Engineering and Science | 발진기와 안테나, 전파를 조절하는 표면을 하나의 LTCC 공정으로 함께 설계했다. LTCC는 저온 동시 소성 세라믹(Low-Temperature Co-Fired Ceramic)으로, 세라믹과 금속 배선을 함께 가열해 만드는 기술이다. 편광에 반응하는 메타표면 렌즈를 결합해 전파가 집중되는 방향을 바꾸는 구조를 제안하고 측정했다.[^p1] | 1저자 Seongwoog Oh, 마지막 저자 오정석 |
| 2 | 2024 | [Heterogeneous Metasurface Empowering Proximate High-Permittivity Ceramic Cover For a 5G Dual-Band Millimeter-Wave Smartphone](https://doi.org/10.1109/tap.2024.3383725) · IEEE Transactions on Antennas and Propagation | 스마트폰의 세라믹 뒤 덮개가 전파를 반사해 생기는 문제를 다루었다. 안테나 가까이에 서로 다른 단위 구조를 조합한 메타표면을 넣고, 두 주파수 구간의 동작을 조절했다. 여러 안테나 배열의 계산과 실제 통화 시험으로 안테나 성능과 전파가 도달하는 방향 범위의 개선을 확인했다.[^p2] | 1저자 Byeongjin Kim, 마지막 저자 오정석 |
| 3 | 2025 | [Design and Experimental Validation of a Through-Quartz Via-Based LC RIS for Dual-Polarization Beam Steering in Sub-Terahertz Bands](https://doi.org/10.1109/ojap.2025.3606889) · IEEE Open Journal of Antennas and Propagation | 전파를 반사할 때 편광과 진행 방향을 함께 바꾸는 액정 기반 표면을 제안했다. 석영을 관통하는 연결로 제어선을 금속 구조에 이어 편광 변환 성능의 저하를 막는 설계를 사용했다. 전자파 계산과 제작한 표면의 측정으로 편광 변환과 방향 조절을 검증했다.[^p3] | 1저자 Byeongju Moon, 마지막 저자 오정석 |
| 4 | 2024 | [Low Voltage Controlled Fast Switchable Liquid Crystal-Based Reflectarray With Transverse Rubbing Layer](https://doi.org/10.1109/lawp.2024.3438367) · IEEE Antennas and Wireless Propagation Letters | 액정 기반 반사 배열에서 빔을 바꾸는 데 걸리는 시간을 다루었다. 띠 형태의 접지 구조와 액정 표면 처리층을 도입해 전압으로 액정의 되돌아가는 응답을 조절했다. 안테나 성능과 방향 전환 속도를 측정해 제안 구조를 평가했다.[^p4] | 1저자 Hogyeom Kim, 마지막 저자 오정석 |
| 5 | 2025 | [A Novel Switch-Less Active Bi-Directional Phase Shifter With In–Out Impedance Equalization via Staggered Structure for Ku-Band Applications](https://doi.org/10.1109/tmtt.2024.3476692) · IEEE Transactions on Microwave Theory and Techniques | 신호가 양방향으로 지나는 위상 변환 회로를 제안했다. 입력과 출력 연결점의 전기적 특성을 같게 맞추는 구조로, 별도로 그 특성을 조절하는 가변 회로를 쓰지 않도록 했다. 신호를 증폭하는 정도인 이득과 위상의 오차, 전력 소비를 평가했다.[^p5] | 1저자 Uichan Park, 마지막 저자 오정석 |
| 6 | 2023 | [Miniaturized mmWave Tri-Band VCO Using Self-and Mutual-Mode-Controlled Inductor](https://doi.org/10.1109/tmtt.2023.3263590) · IEEE Transactions on Microwave Theory and Techniques | 전압으로 동작 주파수를 조절하는 CMOS 발진기를 제안했다. 코일의 연결 상태를 바꾸어 서로 다른 주파수 구간에서 동작하도록 하고, 짝지은 스위치와 여러 발진 핵심 회로를 사용해 스위치 때문에 생기는 위상 잡음 저하를 없애는 구성을 제시했다. 위상 잡음은 반복 신호의 위상이 불규칙하게 흔들리는 현상이다.[^p6] | 1저자 Seongwoog Oh, 마지막 저자 오정석 |
| 7 | 2025 | [Transmission-Integrated HAIT Ray Tracing for Massive O2I Propagation Modeling with MTN Preprocessing and Anxel Beam Transformation](https://doi.org/10.1109/tap.2025.3595956) · IEEE Transactions on Antennas and Propagation | 기존 실외 전파 계산 방법에 건물을 통과하는 경로의 모형을 더했다. 통과 횟수를 미리 계산하는 절차와 경로를 표현하는 방식을 도입하고, 중앙처리장치와 그래픽처리장치가 함께 계산하도록 구성해 실외에서 실내로 전달되는 전파를 계산했다.[^p7] | 1저자 Yongwan Kim, 마지막 저자 오정석 |
| 8 | 2024 | [Anxel Beam Shrinkage Method and Heterogeneous Computing Accelerated Full Image Theory Method Ray Tracing Enabling Massive Outdoor Propagation Modeling](https://doi.org/10.1109/tap.2024.3411793) · IEEE Transactions on Antennas and Propagation | 도시 규모의 실외 전파를 계산하기 위해 경로를 미리 거르고 경로의 연결 구조를 만드는 방법을 제안했다. 중앙처리장치와 그래픽처리장치의 병렬 계산을 결합하고, 기존 소프트웨어와 계산 시간을 비교해 많은 관측 지점과 여러 번 반사되는 경로를 다룰 수 있음을 보였다.[^p8] | 1저자 Yongwan Kim, 마지막 저자 오정석 |

## 교수와 전문 분야

오정석(Jungsuek Oh) 교수는 서울대학교에서 전기공학 학사와 석사, 미시간대학교에서 박사 학위를 받았다. 랩 교수 소개에 따르면 2015년 3월부터 2018년 2월까지 인하대학교 조교수로 재직했고, 2018년 3월 서울대학교 부교수로 부임해 2025년 3월 교수가 되었다. 그 전에는 Samsung Research America Dallas에서 근무했다.[^prof]

학과 교수 소개는 전문 분야를 능동·수동 메타표면, 안테나 시스템, 고주파 회로와 시스템, 실내외 전파 전달 모형으로 적는다. 대표 논문에서도 패키지·스마트폰 안테나, 액정 기반 표면, 위상 변환·발진 회로, 도시 전파 계산을 확인할 수 있다.[^dept][^p1][^p3][^p5][^p6][^p7]

## 응용 분야

스마트폰의 5G·6G 이동통신, 전파의 방향을 바꾸는 통신 표면, 무선 전력 전송, 생체 자극용 전자회로, 실내외 무선 채널 예측과 전자파 간섭 해석이 직접적인 응용 대상이다.[^aip][^ic][^sim] 2025년 삼성미래기술육성사업 선정 소식은 생성형 인공지능으로 안테나 역설계와 신호 왜곡 보정을 함께 다루는 연구를 제시한다.[^news]

## 구성원

2026년 10월 28일 Researchers 페이지의 28명이다. 이름과 시작 시점은 카드 표기이며, 과정은 원문 영문명을 함께 적었다. PhD는 박사, MS는 석사이며, Integrated는 석박사통합과정이다. Candidate와 Student 구분도 원문대로 유지했다.[^members] "대표 논문 참여"는 전체 저자 이름이 완전히 일치하는 경우에만 표시한 표의 번호다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Euiho Shin | 석박사통합과정 (Integrated PhD Candidate) | 20.03~ | euiho20@snu.ac.kr |  |
| Jeongtaek Oh | 석박사통합과정 (Integrated PhD Candidate) | 20.03~ | iwalife@snu.ac.kr |  |
| Byeongjin Kim | 석박사통합과정 (Integrated PhD Candidate) | 20.03~ | anjelcruso@snu.ac.kr | 2 |
| Dongyeon Seo | 석박사통합과정 (Integrated PhD Candidate) | 20.09~ | skaty15@snu.ac.kr |  |
| Jaecheol Oh | 박사과정 (PhD Candidate) | 22.09~ | oyes252@snu.ac.kr |  |
| Hyunjun Yang | 석박사통합과정 (Integrated PhD Candidate) | 21.03~ | guswns6217@snu.ac.kr | 8 |
| Uichan Park | 석박사통합과정 (Integrated PhD Candidate) | 21.03~ | marine522@snu.ac.kr | 5 |
| Taeyeong Yoon | 박사과정 (PhD Candidate) | 23.03~ | taeyeong.yoon@snu.ac.kr | 5 |
| Maengchang Kang | 박사과정 (PhD Candidate) | 23.03~ |  |  |
| Seongbu Hwang | 석박사통합과정 (Integrated PhD Candidate) | 21.03~ | sbhwang95@snu.ac.kr |  |
| Taewook Park | 박사과정 (PhD Candidate) | 23.03~ | demetrio@snu.ac.kr |  |
| Byeongjoo Moon | 석박사통합과정 (Integrated PhD Candidate) | 21.09~ | bjmoon5843@snu.ac.kr |  |
| Young-Seok Lee | 박사과정 (PhD Candidate) | 23.09~ | ryanlee@snu.ac.kr |  |
| Seungwoo Bang | 석박사통합과정 (Integrated PhD Candidate) | 22.03~ | littlebang97@snu.ac.kr | 3, 4 |
| Sungyeong Park | 박사과정 (PhD Candidate) | 24.03~ | clover200@snu.ac.kr |  |
| Minje Kim | 석박사통합과정 (Integrated PhD Candidate) | 23.03~ | sbi06035@snu.ac.kr |  |
| Joonbo Hyun | 박사과정 (PhD Student) | 25.03~ | hjckrck15@snu.ac.kr |  |
| Hooyoung Kim | 석박사통합과정 (Integrated PhD Student) | 24.03~ | kimhy3010@snu.ac.kr | 7, 8 |
| Junpyo Jo | 석박사통합과정 (Integrated PhD Student) | 24.03~ | junpyo99@snu.ac.kr | 8 |
| Seokyeon Hong | 박사과정 (PhD Student) | 26.03~ | syhong@snu.ac.kr |  |
| Minkyu Park | 석박사통합과정 (Integrated MS Student) | 25.03~ | kyyusnu@snu.ac.kr |  |
| Donghun Kang | 석박사통합과정 (Integrated MS Student) | 25.03~ | ehdgns4013@snu.ac.kr |  |
| Semin Lee | 석박사통합과정 (Integrated MS Student) | 25.03~ | leesm0719@snu.ac.kr |  |
| Kanghyun Ryoo | 석사과정 (MS Student) | 25.03~ | k.ryoo@snu.ac.kr |  |
| Gihyeun Moon | 석사과정 (MS Student) | 25.03~ | mgh2936@snu.ac.kr |  |
| Ghunho Min | 석박사통합과정 (Integrated MS Student) | 26.03~ | goongo@snu.ac.kr |  |
| Hoseok Kang | 석박사통합과정 (Integrated MS Student) | 26.09~ | khs2001120@snu.ac.kr |  |
| Suyong Moon | 석사과정 (MS Student) | 26.09~ | volvosanta@snu.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 22개 게시 항목 중 2022–2025년으로 적힌 9명이다. 연도는 누리집의 학위·과정 연도 표기이며, 구체적인 날짜는 게시되어 있지 않다. 진로와 학위 논문은 랩 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Jaebaek Jung | Ph.D (2025) | MX division, Samsung Electronics | RF Metasurface and Antenna Fusion Technologies for Optimizing Radiation Performance and Bandwidth of 5G/6G Smartphone Integrated AiP |
| Jaehoon Kim | Ph.D (2025) | MX division, Samsung Electronics | Advancements in Antenna Block Design for Future Wireless Communications: Reconfigurable Beamforming and Spatial Functionalities in Radiating Aperture |
| Jeongwoo Heo | M.S (2025) | Broadcom Corporation | A Study on System-Efficient Millimeter Wave RF Passive Components for Wireless Communication : Tetra-Plexing Antenna, Balanced Balun and Space-Coupled Sub-Array Antenna |
| Suk Hwangbo | M.S (2025) | Broadcom Corporation | RF Customized Semiconductor Fabrication of Reconfigurable Intelligent Surfaces : Embedded PIN Varactors for Beamforming |
| Sanghun Lee | M.S (2025) | MX division, Samsung Electronics | Study on RF-DC Efficiency Optimization based on Receiver Localization Techniques |
| Hyoseop Lee | M.S (2024) |  | Detecting Targets Located in N-LOS conditions Using a Beam Steerable Broadband Metasurface |
| Seongwoog Oh | Ph.D (2023) | Professor at University of Seoul | Reconfigurable Intelligent Surface Assisted Beamforming in Hyper-Connected Metasurface Antenna-RFIC Packaging Systems for 6G Networks |
| Woojun Lee | M.S (2023) | Virginia Tech | A Study on Compact Array Antennas Based on Novel Excitation Techniques |
| Taeyeong Yoon | M.S (2023) | WFL in SNU | Study on the Highly Isolated TRx Dual-Polarized Array Antennas for In-Band Full-Duplex Communications |

## 최근 논문 목록 (2021–2026)

Journal의 81편과 Conference의 41편, 합계 122개 게시 항목이다. 연도는 누리집의 연도 구역 표기이며, 2021년 구역은 월에 관계없이 포함했다. 학술지와 학회 목록을 나누고, 같은 제목도 서로 다른 학술지·학회 기록이면 각각 적었다. Early Access는 목록의 온라인 선공개 표기다. 학회명과 연도만 적힌 항목도 있어, 이 목록의 모든 항목을 논문집 출판 완료로 뜻하지는 않는다.[^journals][^conferences] 생체 자극 응용의 학술지 논문 두 편은 초록이 회로·탐침 또는 무선 전력 전송 코일·시스템의 개발을 기여로 제시한다.[^bio]

### 학술지 논문 (81편)

**2026**

- Young-Seok Lee, Sihyun Kim, Taeyeong Yoon, Sangwook Nam, and Jungsuek Oh. "Virtual-Beacon Depth Refocusing for Improved Received-Power Uniformity in Near-Field Time-Reversal Wireless Power Transfer". *IEEE Antennas and Wireless Propagation Letters, EArly Access*.
- Uichan Park, Donghun Kang, and Jungsuek Oh. "A System-Level Solution for Dual-Polarized-Array Digital Predistortion: Joint Load-Impedance Alignment and Cross-Polarization Cancellation". *IEEE Transactions on Microwave Theory and Techniques, Early Access*.
- Taeyeong Yoon, Young-Seok Lee, Uichan Park, Minje Kim, Sanghun Lee, Sangwook Nam, and Jungsuek Oh. "Hardware-Aware MILP for Optimal End-to-End Efficiency in MISO WPT: Joint Optimization of Power Modes and Fault Tolerance". *IEEE Transactions on Microwave Theory and Techniques, Early Access*.
- Young-Seok Lee, Taeyeong Yoon, and Jungsuek Oh. "An End-to-End DC-to-DC Efficiency Optimization and Design Analysis for MIMO Wireless Power Transfer Systems". *IEEE Transactions on Microwave Theory and Techniques ,vol. 74 ,no. 9 ,pp. 8545-8562*.
- Hyunjun Yang, Hooyoung Kim, and Jungsuek Oh. "Accelerated 3-D Multi-Diffraction Image-Theory Ray Tracing for 6G Propagation with an Urban-Scale Sionna RT Benchmark". *IEEE Transactions on Antennas and Propagation, Early Access*.
- Minje Kim, Euiho Shin, Hooyoung Kim, Taeyeong Yoon, Semin Lee, and Jungsuek Oh. "MR2P: Diffusion Model-Driven Pixelated-Antenna Inverse Design Framework Generalizable Across Extensible Electromagnetic Figures of Merit". *IEEE Journal on Multiscale and Multiphysics Computational Techniques, Early Access*.
- Je-Heon Lee, Hyeon-Chang Seong, Jungsuek Oh, and Jae Hee Kim. "Array Antenna Radiation Pattern Synthesis Using Mixture Density Networks With Iterative Retraining". *IET Microwaves Antennas & Propagation ,vol. 20 ,no. 1*.
- Jinhyun Kim, Byeongjin Kim, Minkyu Park, Jeongtaek Oh, and Jungsuek Oh. "STARE: a semiconductor-integrated transmit-array architecture for 6G beamforming". *Nature Communications*.
- Hyunjun Yang, Hooyoung Kim, Uichan Park, Seungwoo Bang, and Jungsuek Oh. "6G Upper Mid-band Channels at 7.5 GHz with Diverse Urban Campaigns and Coverage Analysis via Image-Theory Full-3D Ray-Tracing". *IEEE Transactions on Communications, Early Access*.
- Yongwan Kim, Hooyoung Kim, Seungwoo Bang, and Jungsuek Oh. "Realistic Outdoor-to-Indoor Path Loss Modeling for Upper Mid-Band in Urban Microcell Environments Using Semi-Deterministic Ray Tracing". *IEEE Transactions on Antennas and Propagation, Early Access*.
- Byeongjin Kim, Seungwoo Bang, Sumin Yun, Maengchang Kang, Hosaeng Kim, and Jungsuek Oh. "Ultra-Thin Unidirectional Holographic Metasurface Antenna Excited by TE-Mode Surface Wave". *IEEE Antennas and Wireless Propagation Letters ,vol. 25 ,no. 4 ,pp. 1697-1701*.
- Yongwan Kim, and Jungsuek Oh. "Ray-Tracing-Based 6G Air-to-Indoor Path Loss Modeling in Urban Environments". *IEEE Antennas and Wireless Propagation Letters ,vol. 25 ,no. 4 ,pp. 1457-1461*.
- Uichan Park, Taeyeong Yoon, Donghun Kang, and Jungsuek Oh. "An Ultracompact Active Bidirectional Phase Shifter With an Intrinsic Reciprocal Phase-Inverting Core". *IEEE Microwave and Wireless Technology Letters, Early Access*.
- Jinhyun Kim, Seongwoog Oh, and Jungsuek Oh. "A 2.5-Bit Polarization-Rotating Ultrawideband Transmit Array for 6G Communications". *IEEE Transactions on Antennas and Propagation ,vol. 74 ,no. 3 ,pp. 2869 - 2874*.
- Jaecheol Oh, Maengchang Kang, Junpyo Jo, Seungwoo Bang, Hyeon-Seok Choe, Sung-Hun Ha, Seokyoung Park, Jinbong Kim, Sangkeun Kim, Jungsuek Oh, and Hong-Kyu Jang. "A Compact Broadband Omnidirectional Top-Loaded UHF Antenna with Integrated Ground Wall and GFRP Radome for Conformal Airborne Applications". *Aerospace ,vol. 13 ,no. 3 ,pp. 227*.
- Jinhyun Kim, Seongwoog Oh, and Jungsuek Oh. "A Concurrent dual band Power Amplifier with diplexer based on Asymmetric Load Coupler". *IEEE Access ,vol. 14 ,pp. 39821-39829*.
- Seungwoo Bang, Jaehoon Kim, Jungi Jeong, Junhwa Oh, Byeongjin Kim, and Jungsuek Oh. "Varactor-Integrated Single-Port Antenna Array With Element-Wise Coupling Optimization for Scalable Beamforming in 6G Massive MIMO Systems". *IEEE Transactions on Antennas and Propagation ,vol. 74 ,no. 3 ,pp. 2342-2351*.
- Byeongjin Kim, Jeongtaek Oh, Kiseo Kim, and Jungsuek Oh. "Impedance-Modulating Patch Integration for Gain and Bandwidth Control of Antenna-in-Display in Millimeter-Wave Smartphones". *Journal of Electromagnetic Engineering and Science ,vol. 26 ,no. 1 ,pp. 39-48*.
- Seongwoog Oh, Yeongmyeong Park, and Jungsuek Oh. "Sub-THz Polarization-Dependent Beam-Steerable Metasurface Antenna-in-Package for 6G Communication Constructed Using an LTCC Process". *Journal of Electromagnetic Engineering and Science ,vol. 26 ,no. 1 ,pp. 88-102*.
- Hogyeom Kim, Seongwoog Oh, Manseok Kim, Byeongju Moon, Jeongtaek Oh, Seungwoo Bang, and Jungsuek Oh. "Low-Power Consumption and Beam-Sustainable Reconfigurable Intelligent Surface for Fixed Wireless Communication at Millimeter-Wave 5G Band". *IEEE Transactions on Microwave Theory and Techniques ,vol. 74 ,no. 1 ,pp. 524-535*.

**2025**

- Byeongju Moon, Seungwoo Bang, Seongwoog Oh, and Jungsuek Oh. "Design and Experimental Validation of a Through-Quartz Via-Based LC RIS for Dual-Polarization Beam Steering in Sub-Terahertz Bands". *IEEE Open Journal of Antennas and Propagation ,vol. 6 ,no. 6 ,pp. 1881-1894*.
- Byeongjin Kim, Suk Hwangbo, and Jungsuek OH. "Optically Transparent Holographic Display Antenna: High Gain, Beam Steering, and Lossless Bonding for 5G Millimeter-Wave n261 Band". *IEEE Open Journal of Antennas and Propagation ,vol. 6 ,no. 6 ,pp. 1799-1814*.
- Taeyeong Yoon, Uichan Park, Minje Kim, Sanghun Lee, Young-Seok Lee, Sangwook Nam, and Jungsuek Oh. "A Topology-based Array Compensation Empowered by Equivalent Current Modeling of TM10 Patch Antennas for Cross-Polarization Reduction". *IEEE Open Journal of Antennas and Propagation ,vol. 6 ,no. 6 ,pp. 1696-1707*.
- Uichan Park, Taeyeong Yoon, and Jungsuek Oh. "A Compact Active Bidirectional Phase Shifter Employing a Highly Isolated Single Gilbert Cell". *IEEE Microwave and Wireless Technology Letters ,vol. 32 ,no. 3 ,pp. 2109 - 2112*.
- Yongwan Kim, Hooyoung Kim, Jonghyup Lee, Hyunho Cho, and Jungsuek Oh. "Transmission-Integrated HAIT Ray Tracing for Massive O2I Propagation Modeling with MTN Preprocessing and Anxel Beam Transformation". *IEEE Transactions on Antennas and Propagation ,vol. 73 ,no. 11 ,pp. 9255-9270*.
- Byeongjin Kim, Seungwoo Bang, Sumin Yun, Hosaeng Kim, Jungsuek Oh. "Broadband Holographic Mode Synthesis Between Adjacent Resonances for a Low-Profile Thin-Microstrip Antenna-Fed Metasurface". *IEEE Transactions on Antennas and Propagation ,vol. 73 ,no. 11 ,pp. 9577-9582*.
- Jeongtaek Oh, Hyunjin Kim, Sucheoul Kim, Jaehyun Choi, Jihun Ha, and Jungsuek Oh. "M-shaped Under-Bridge Feeding Method For A Low-Profile Dual-Band Dual-Polarized Antenna-on-Package In The 6G Upper-mid Band". *IEEE Antennas and Wireless Propagation Letters ,vol. 24 ,no. 9 ,pp. 3164-3168*.
- Byeongjin Kim, and Jungsuek Oh. "Dual-Wideband Low-Profile Three-Notch Patch Antenna With Indirect Differential Feeding for 5G Millimeter-Wave Applications". *IEEE Antennas and Wireless Propagation Letters ,vol. 24 ,no. 9 ,pp. 2734-2738*.
- Jinhyun Kim, Uichan Park, Haeseung Lee, Kyungho Yoo, and Jungsuek Oh. "Compact MIMO Antenna OTA Measurement System with Utilization of Metasurface for Wavefront Manipulator". *IEEE Transactions on Instrumentation and Measurement ,vol. 74 ,pp. 1-8*.
- Hogyeom Kim, Byeongju Moon, Seungwoo Bang, Seongwoog Oh, Jungsuek Oh. "PCB-Based Dual-Polarized Liquid Crystal Reflectarray with High Aperture Efficiency and Bridge-Shaped Biasing Topology for 2D Scanning". *IEEE Access ,vol. 13 ,pp. 2169-3536*.
- Young-Seok Lee, Taeyeong Yoon, Young Jin Song, Sun K. Hong, Jungsuek Oh, Sangwook Nam. "Transmission-Conversion Efficiency Maximization Technique for MIMO Wireless Power Transfer Systems in ISAC Applications". *IEEE Antennas and Wireless Propagation Letters ,vol. 24 ,no. 11 ,pp. 4492 - 4496*.
- Young-Seok Lee, Taeyeong Yoon, Minje Kim, Sanghun Lee, Byungwook Jung, and Jungsuek Oh. "A Design and Characterization Method of a Scalable Large Transmitting Array for Wireless Power Transfer". *IEEE Transactions on Microwave Theory and Techniques ,vol. 73 ,no. 6 ,pp. 3346-3358*.
- Jeongwoo Heo,  Byeongjin Kim, Maengchang Kang, Heeyoung Kim, Youngju Lee, and Jungsuek Oh. "Tetra-Plexing Dual-Broadband/Dual-Polarized Antenna for 5G/6G Millimeter-Wave Systems". *IEEE Transactions on Antennas and Propagation, Early Access*.
- Uichan Park, Suk Hwangbo, Jinhyun Kim, Taeyeong Yoon, and Jungsuek Oh. "A Novel Switch-Less Active Bi-Directional Phase Shifter With In–Out Impedance Equalization via Staggered Structure for Ku-Band Applications". *IEEE Transactions on Microwave Theory and Techniques ,vol. 73 ,no. 5 ,pp. 2653-2667*.
- Byeongjin Kim, Seungwoo Bang, Sunghyun Kim, Doyle Kwon, Seongkwan Kim, and Jungsuek Oh. "Locally Optimal Periods in Periodic Optically Transparent Two-Metal-Layered Refractive Metasurfaces for Outdoor-to-Indoor Communication". *IEEE Antennas and Wireless Propagation Letters ,vol. 24 ,no. 5 ,pp. 1253-1257*.
- Taeyoung Kim, Sangmin Lee, Seongwoog Oh, Jinhyun Kim, Jungsuek Oh, and Sangjo Choi. "Pre-phased 1-bit Reflective Passive Metasurface with Optimum Number of Pre-phasing for Low QLL and SLL at 140 GHz". *IEEE Transactions on Antennas and Propagation ,vol. 73 ,no. 2 ,pp. 975-985*.
- Seungwoo Bang, Hogyeom Kim and Jungsuek Oh. "Enhancing 2-D Beam Scanning Capability through Extended Transmission Paths in a Liquid Crystal-Based Transmitarray Antenna for mmWave Communications". *Journal of Electromagnetic Engineering and Science ,vol. 25 ,no. 1 ,pp. 85-91*.
- Jeongtaek Oh, Kiseo Kim, Jaeuk Choi, and Jungsuek Oh. "Tightly Embedded Modular Antenna-in-Display (MAiD) into The Panel Edge of Display with Dual-Polarization for 5G Smartphones". *IEEE Transactions on Antennas and Propagation ,vol. 73 ,no. 2 ,pp. 1209-1214*.

**2024**

- Uichan Park, Jinhyun Kim, Taeyeong Yoon, Haeseung Lee, Kyungho Yoo, and Jungsuek Oh. "A Low-Profile High-Efficiency Transmitarray Antenna Reflecting Effective Phase Discontinuity With TE/TM Superimpose Analysis". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 12 ,pp. 9208-9220*.
- Hyunjin Kim and Jungsuek Oh. "D-Band Scalable Phased Array Antenna-in-Package Using Stripline Power Divider-Based Sub-Array". *IEEE Access ,vol. 12 ,pp. 185618-185629*.
- Hogyeom Kim, Jae-Won Lee, Seungwoo Bang, Junkai Wang, Min-Seok Kim, Hak-Rin Kim, and Jungsuek Oh. "Low Voltage Controlled Fast Switchable Liquid Crystal-Based Reflectarray With Transverse Rubbing Layer". *IEEE Antennas and Wireless Propagation Letters ,vol. 23 ,no. 12 ,pp. 4194-4197*.
- Hyunjun Yang, Sunghyun Kim, Hogyeom Kim, Seungwoo Bang, Yongwan Kim, Seongkwan Kim, Kyujin Park, Doyle Kwon, and Jungsuek Oh. "Beyond Limitations of 5G with RIS: Field Trial in a Commercial Network, Recent Advances, and Future Directions". *IEEE Communications Magazine ,vol. 62 ,no. 10 ,pp. 132-138*.
- Jaehoon Kim, Seungwoo Bang, Jungi Jeong, Sang-Hyuk Wi, and Jungsuek Oh. "Enhancing Selectivity in 5G/6G Ultra-Narrowband Applications: Plug-and-Play Frequency Selective Surfaces with Field-Manipulating Vias". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 8 ,pp. 6783-6788*.
- Hogyeom Kim, Jae-Won Lee, Junkai Wang, Min-Seok Kim, Hak-Rin Kim, and Jungsuek Oh. "Waveguide-Thru Closed-Form Characterization of Anisotropic Polymer Network Liquid-Crystal for mmWave Reconfigurable RF Devices". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 7 ,pp. 5447-5457*.
- Yongwan Kim, Hyunjun Yang, Hooyoung Kim, Junpyo Jo, and Jungsuek Oh. "Anxel Beam Shrinkage Method and Heterogeneous Computing Accelerated Full Image Theory Method Ray Tracing Enabling Massive Outdoor Propagation Modeling". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 7 ,pp. 5935-5949*.
- Seungwoo Bang, Taeyeong Yoon, Byeongjin Kim, Jaecheol Oh, Hogyeom Kim, and Jungsuek Oh. "Extremely Miniaturized Free-Space Measurement System for RF Metamaterial Composite Based on Beam Focusing Transmitarray". *IEEE Antennas and Wireless Propagation Letters ,vol. 23 ,no. 6 ,pp. 1705-1709*.
- Byeongjin Kim, Jaebaek Jung, Sumin Yun, Hosaeng Kim, and Jungsuek Oh. "Heterogeneous Metasurface Empowering Proximate High-Permittivity Ceramic Cover For a 5G Dual-Band Millimeter-Wave Smartphone". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 5 ,pp. 4086-4094*.
- Seongwoog Oh and Jungsuek Oh. "Asymmetric Capacitor-Loaded Marchand Balun-Based Four-Stacked Power Amplifier Utilized C -Band Stimulus Source in SOI CMOS". *IEEE Microwave and Wireless Technology Letters ,vol. 34 ,no. 3 ,pp. 302-305*.
- Jaehoon Kim, Junhwa Oh, Sanghyuk Wi, Jungsuek Oh. "Asymmetrically Layered Unit Cell Topology to Reduce Cell Gap of Liquid Crystals for 5G Millimeter-Wave Transmissive Reconfigurable Intelligent Surface Applications". *IEEE Transactions on Antennas and Propagation ,vol. 72 ,no. 3 ,pp. 2950-2955*.
- Taeyeong Yoon, Uichan Park, and Jungsuek Oh. "Band-Stop Behavior Vertically Extended Ground Isolator Based on Transmission Line Theory for IBFD TRx Decoupling Applications". *IEEE Transactions on Microwave Theory and Techniques ,vol. 72 ,no. 2 ,pp. 1405-1415*.
- Hyunjin Kim, Sangwook Nam, and Jungsuek Oh. "A Compact 1:3 Power Divider Incorporating 180° Shifted Path for Polarization Purity Enhanced Base Station Subarray". *Journal of Electromagnetic Engineering and Science ,vol. 24 ,no. 1 ,pp. 9-17*.

**2023**

- Hyunjin Kim, Jaebaek Jung, Woojun Lee, Sangwook Nam, and Jungsuek Oh. "D-Band 4 × 4 Multi-Feed Array Antenna-in-Package for High-Power Combining and Polarization Synthesis". *IEEE Access ,vol. 11 ,pp. 144006-144016*.
- Jaehoon Kim, Woojun Lee, and Jungsuek Oh. "Liquid-Crystal-Tuned Resonant Series Patch Array with Unique Element Spacing Emulating Simplified Operating Construe of Traveling-wave Antenna". *IEEE Antennas and Wireless Propagation Letters ,vol. 22 ,no. 12 ,pp. 3087-3091*.
- Byeongju Moon and Jungsuek Oh. "FSS-Enhanced Quasi-Optical Dielectric Measurement Method for Liquid Crystals in Sub-THz Band". *IEEE Antennas and Wireless Propagation Letters ,vol. 22 ,no. 12 ,pp. 3062-3306*.
- Seongwoog Oh and Jungsuek Oh. "140-GHz Affordable Miniaturized Array Antenna-on-Package for Sub-THz Transceiver". *IEEE Access ,vol. 11 ,pp. 132780-132791*.
- Byeongjin Kim and Jungsuek Oh. "Single-Glass Layer Optically Transparent Transmitarray With High Aperture Efficiency And Low Profile At 5G Millimeter-Wave Band". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 11 ,pp. 9036-9041*.
- Taeyeong Yoon and Jungsuek Oh. "Metal Rods-Based Field Concentrated Common and Differential Modes Theory Enabling Design of Dual-Polarized Antennas". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 10 ,pp. 7782-7791*.
- Seongwoog Oh and Jungsuek Oh. "Miniaturized mmWave Tri-Band VCO Using Self-and Mutual-Mode-Controlled Inductor". *IEEE Transactions on Microwave Theory and Techniques ,vol. 71 ,no. 10 ,pp. 4404-4415*.
- Jaebaek Jung, Woojun Lee, Gyuha Lee, Songcheol Hong, and Jungsuek Oh. "Ultra-thinned Metasurface-embedded Smartphone Antenna-in-package for Millimeter Wave 5G/6G Coverage Enhancement". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 10 ,pp. 7766-7781*.
- Hyunjin Kim and Jungsuek Oh. "D-band Stripline Interconnection Using Capped Cavity via Transition". *IEEE Microwave and Wireless Technology Letters ,vol. 33 ,no. 9 ,pp. 1262-1265*.
- Hogyeom Kim, Seongwoog Oh, Seungwoo Bang, Hyunjun Yang, Byeongjin Kim, and Jungsuek Oh. "Independently Polarization Manipulable Liquid-Crystal-Based Reflective Metasurface for 5G Reflectarray and Reconfigurable Intelligent Surface". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 8 ,pp. 6606-6616*.
- Jinhyun Kim, Seongwoog Oh, and Jungsuek Oh. "A Low Phase Error Vector Modulator Using Tunable I/Q Generator for mmWave Communication". *IEEE Microwave and Wireless Technology Letters ,vol. 33 ,no. 7 ,pp. 1055-1058*.
- Euiho Shin, Young-seek Chung, Cheolsun Park, Seonkyo Kim, and Jungsuek Oh. "Broadband Beamforming Using the Least Square Method Improved via Adaptive Diagonal Loading". *Journal of Electromagnetic Engineering and Science*.
- Jaehoon Kim, Jinhyun Kim, Junhwa Oh, Sanghyuk Wi, and Jungsuek Oh. "Rotated Feed-Combined Reconfigurable Transmit RIS with Disparate Deployment of 1-Bit Hybrid Units for B5G/6G". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 6 ,pp. 5457-5462*.
- Seongwoog Oh, Jinhyun Kim, and Jungsuek Oh. "W-Band Switch-Less Reconfigurable-Push Dual-Band VCO Using Clover-Shaped Inductor and Robust Triple Cores for 6G Communications". *IEEE Transactions on Microwave Theory and Techniques ,vol. 71 ,no. 5 ,pp. 1890-1898*.
- Jinhyun Kim, Sanggeon Park, Seongwoog Oh, Yeowool Huh, Jeiwon Cho, and Jungsuek Oh. "Cage-Embedded Crown-type Dual Coil Wireless Power Transfer Based Microwave Brain Stimulation System for Untethered and Moving Mice". *IEEE Transactions on Biomedical Circuits and System ,vol. 17 ,no. 2 ,pp. 362-374*.
- Hyunjin Kim and Jungsuek Oh. "140-GHz Wideband Array Antenna-in-Package Using Multimode Resonance". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 3 ,pp. 2136-2144*.
- Yongwan Kim, Hyunjun Yang, and Jungsuek Oh. "Critical Angle Formulation of Nonuniform Plane Waves for Determining Correct Refraction Angles at Planar Interface". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 3 ,pp. 2861-2866*.
- Jinhyong Kim, Cheolung Cha, Kwonhong Lee, Jungsuek Oh and Yongtaek Hong. "E-textile based Wavy Surface WPT Flexible Antenna with Frequency Self-reconfiguration Function for Battery-less Sensor Platform". *IEEE Sensors Journal ,vol. 23 ,no. 5 ,pp. 4392-4404*.
- Jeongtaek Oh, Byeongjin Kim, Sangrock Yoon, Kiseo Kim, Eunjin Sung, and Jungsuek Oh. "High-Gain Millimeter-Wave Antenna-in-Display Using Non-Optical Space for 5G Smartphones". *IEEE Transactions on Antennas and Propagation ,vol. 71 ,no. 2 ,pp. 1458-1468*.
- Euiho Shin and Jungsuek Oh. "Broadband DOA Estimation by Exploiting DFT Extrapolation". *Applied Sciences ,vol. 13 ,no. 1 ,pp. 660*.

**2022**

- Hogyeom Kim, Jongyeong Kim and Jungsuek Oh. "A Novel Systematic Design of High-Aperture-Efficiency 2D Beam-Scanning Liquid-Crystal Embedded Reflectarray Antenna For 6G FR3 And Radar Applications". *IEEE Transactions on Antennas and Propagation ,vol. 70 ,no. 11 ,pp. 11194-11198*.
- Dongyeon Seo, Hogyeom Kim, Seongwoog Oh, Jinhyun Kim and Jungsuek Oh. "Ultra-thin High Gain D-band Transmitarray Based on a Spatial Filter Topology Utilizing Bonding Layer Effect". *IEEE Antennas and Wireless Propagation Letters ,vol. 21 ,no. 10 ,pp. 1945-1949*.
- Seokyeon Hong, Yongwan Kim and Jungsuek Oh. "Automobile Laminated Glass Window Embedded Transmitarray and Ray Tracing Validation for Enhanced 5G Connectivity". *IEEE Transactions on Antennas and Propagation ,vol. 70 ,no. 8 ,pp. 6671-6682*.
- Jaehyun Lee, Hogyeom Kim and Jungsuek Oh. "Large-Aperture Metamaterial Lens Antenna for Multi-Layer MIMO Transmission for 6G". *IEEE Access ,vol. 10 ,pp. 20486-20495*.
- Jinhyong Kim, Cheolung Cha, Jungsuek Oh and Yongtaek Hong. "New Design Topology of High-Q Factor Printed Antenna having Unequal Width and Pitch used for Near-field Wireless Power Transmission". *IEEE Journal of Emerging and Selected Topics in Power Electronics ,vol. 10 ,no. 1 ,pp. 984-996*.

**2021**

- Jungwoo Seo, Inseop Yoon, Jaebaek Jung, Jeongki Ryoo, Juhyoung Park, Woncheol Lee, Dongok Ko and Jungsuek Oh. "Miniaturized Dual-band Broadside/Endfire Antenna-in-Package for 5G Smartphone". *IEEE Transactions on Antennas and Propagation ,vol. 69 ,no. 12 ,pp. 8100-8114*.
- Hogyeom Kim, Jongyeong Kim and Jungsuek Oh. "Liquid-Crystal-based X-band Reactively Loaded Reflectarray Unit Cell to Reduce Reflection Loss". *IEEE Antennas and Wireless Propagation Letters ,vol. 20 ,no. 10 ,pp. 1898-1902*.
- Seongwoog Oh, Dahee Jung, Taeyoon Seo, Yeowool Huh, Jeiwon Cho and Jungsuek Oh. "6.5-GHz Brain Stimulation System Using Enhanced Probe Focusing and Switch-Driven Modulation". *IEEE Transactions on Microwave Theory and Techniques ,vol. 69 ,no. 9 ,pp. 4107-4117*.
- Seongwoog Oh, Kwang-Seok Seo and Jungsuek Oh. "Low Phase Noise Concurrent Dual-Band (5/7 GHz) CMOS VCO Using Gate Feedback on Nonuniformly Wound Transformer". *IEEE Microwave and Wireless Components Letters ,vol. 31 ,no. 2 ,pp. 177-180*.
- Euiho Shin and Jungsuek Oh. "Beam-Steerable Passive Transmitarray Optimized Based on an Adjacent Algorithm". *IEEE Access ,vol. 9 ,pp. 28797-28804*.

### 학회 논문 (41편)

**2026**

- Young-Seok Lee, Taeyeong Yoon, Sangwook Nam, and Jungsuek Oh. "DC-to-DC Efficiency Maximization in Wireless Power Transfer with PA and Rectifier Nonlinearities via Semidefinite Relaxation". *IEEE Wireless Power Technology Conference and Expo (WPTCE) 2026*.
- Minje Kim and Jungsuek Oh. "Inference-Time Physics-Guided Inverse Design of Pixelated Patch Antennas via EM-Video Diffusion". *2026 IEEE International Symposium on Antennas and Propagation and USNC-URSI Radio Science Meeting (AP-S), Detroit, MI, USA, 2026*.
- Dongyeon Seo, Dongyeol Yang, Sungho Lee, and Jungsuek Oh. "High-Gain Beamforming-Capable Bi-Directional D-Band Transmitarray for FMCW Radar via Integrated Packaging-Aware Multi-Channel AoP". *2026 IEEE International Symposium on Antennas and Propagation and USNC-URSI Radio Science Meeting (AP-S), Detroit, MI, USA, 2026*.
- Seungwoo Bang and Jungsuek Oh. "Liquid-Crystal-Based RIS with M+N Bias Lines Enabling Diagonal Beamforming via Polarity-Independent Optimization". *2026 IEEE International Symposium on Antennas and Propagation and USNC-URSI Radio Science Meeting (AP-S), Detroit, MI, USA, 2026*.
- Donghun Kang, Uichan Park, and Jungsuek Oh. "Joint Optimization of Peak Reduction and DPD  for Boosting PA Average Output Power". *2026 IEEE/MTT-S International Microwave Symposium (IMS), Boston, MA, USA, 2026*.
- Uichan Park, Taeyeong Yoon, Donghun Kang, and Jungsuek Oh. "An Ultracompact Active Bidirectional Phase Shifter With an Intrinsic Reciprocal Phase-Inverting Core". *2026 IEEE/MTT-S International Microwave Symposium (IMS), Boston, MA, USA, 2026*.
- Seungwoo Bang, Hogyeom Kim, Byeongjin Kim, Hooyoung Kim, Byeongjoo Moon, Uichan Park, Dongyeon Seo, Min-Seok Kim, Hak-Rin Kim, and Jungsuek Oh. "System-Power-Efficient Reconfigurable Intelligent Surface with M+N Control: Achieving Full-Space Steering Including Diagonal Plane". *2026 IEEE/MTT-S International Microwave Symposium (IMS), Boston, MA, USA, 2026*.
- Hogyeom Kim, Seongwoog Oh, Seungwoo Bang, Hyunjun Yang, and Jungsuek Oh. "Polarization-Multiplexed Massive Reconfigurable Intelligent Surface for LEO Satellite Networks". *2026 IEEE International Conference on Communications (ICC 2026) - Wireless Communications Symposium*.
- Kanghyun Ryoo, Byengjin Kim, Minkyu Park, and Jungsuek Oh. "Dual-Circularly Polarized Bent-Patch Antenna for Foldable Smartphones: Leveraging an FPCB and Its Through-Aperture". *2026 European Conference on Antennas and Propagation (EuCAP), Dublin, Ireland*.

**2025**

- Seungwoo Bang, Jaehoon Kim, Jungi Jeong, Junhwa Oh, Byeongjin Kim and Jungsuek Oh. "Realization of Constant Amplitude Standing Wave Excitation Through Multi-Level Coupling Control in a Reconfigurable Series-Fed Antenna". *2025 International Symposium on Antennas and Propagation (ISAP)*.
- Jaecheol Oh, Hyeon-Seok Choe, Sung-Hun Ha, Heeduck Chae, Maengchang Kang, Jungsuek Oh, and Hong-kyu Jang. "Antenna Aperture-Shared Low-Pass Radar Absorbing Metasurface for Stealth Applications". *2025 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Maengchang Kang, Heeduck Chae, Youngwan Kim, Chang-Hyun Lee, and Jungsuek Oh. "High-Precision (1-Degree) Beam-Steerable Transmissive Metasurface Antenna Integrating Discrete and Continuous Tunability". *2025 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Hogyoem Kim and Jungsuek Oh. "2-Bit Dual Polarization Controllable RIS-Assisted 6G ISAC System Demonstrating Enhanced Operation(Comm/Sensing)-Mode Isolation". *2025 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Hogyeom and Jungsuek Oh. "Electronically Reconfigurable Low-Profile Folded Reflectarray Antenna at 28 GHz". *2025 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Taeyeong Yoon, Young-Seok Lee, Minje Kim, Sanghun Lee, Jaesup Lee, Sangwook Nam, and Jungsuek Oh. "Overcoming Efficiency Degradation in Wireless Power Transfer Systems: A Supply Voltage Modulation Method Empowered by 5.64-GHz 256-Element Antenna Array Receiving 10.6-Watt". *2025 IEEE MTT-S International Microwave Symposium (IMS 2025)*.
- Uichan Park, and Jungsuek Oh. "Reference Phase Adjustment Technique with Cross-Polarization Cancellation for Enhanced Digital Predistortion in Mobile Dual-Polarized Arrays". *2025 IEEE MTT-S International Microwave Symposium (IMS 2025)*.
- Hogyeom Kim, Hyunjun Yang, Hooyoung Kim, and Jungsuek Oh. "Integrated Sensing and Communication Using Reconfigurable  Intelligent Surface: Hardware, Ray-Tracing Demonstration, and  Channel Measurement in the 6G Mid Band". *2025 IEEE MTT-S International Microwave Symposium (IMS 2025)*.
- Hogyeom Kim, Seongwoog Oh, Jeongtaek Oh, and Jungsuek Oh. "Low Power Consumption and Beam-Sustainable Reconfigurable Intelligent Surface for Fixed Wireless Communication at Millimeter- Wave 5G Band". *2025 IEEE MTT-S International Microwave Symposium (IMS 2025)*.
- Hyunjun Yang, Seungwoo Bang, Hooyoung Kim, Sunghyun Kim, Yusuk Sung,  Kyujin Park, Seongkwan Kim, and Jungsuek Oh. "Channel Measurement in Urban, Dense Urban Scenario and Massive Ray-Tracing-Based Coverage Analysis at 7.5 GHz". *2025 IEEE International Conference on Communications (ICC 2025) - Wireless Communications Symposium*.
- Young-Seok Lee, Jungsuek Oh, and Sangwook Nam. "Sequential Feedback-Based Phase Optimization Using Hadamard Basis for Wireless Power Transfer". *2025 IEEE Wireless Power Technology Conference and EXPO (WPTCE 2025)*.

**2024**

- Young-Seok Lee, Jungsuek Oh, and Sangwook Nam. "An Effect of Time Reversal Based Multiple Beacon Selection on Wireless Power Transfer Performance". *2024 IEEE International Symposium on Antennas and Propagation (ISAP 2024)*.
- Hogyeom Kim and Jungsuek Oh. "Proof of Concept for Massive Reconfigurable Intelligent Surface Enabling Beam Sustainability at Sub-THz Band". *2024 IEEE International Symposium on Antennas and Propagation (ISAP 2024)*.
- Yongwan Kim, Hooyoung Kim, and Jungsuek Oh. "Revolutionizing Full Image Theory Method EM Ray Tracing for Massive Propagation Analysis with Enhanced Computational Efficiency". *2024 IEEE International Symposium on Antennas and Propagation (ISAP 2024)*.
- Taeyeong Yoon, Uichan Park, and Jungsuek Oh. "Unlocking Operation Principle of Corner Truncated Antenna Enabling to Squeeze-out Axial Ratio Bandwidth with Thick Substrate Effect". *2024 IEEE International Symposium on Antennas and Propagation (ISAP 2024)*.
- Young-Seok Lee, Taeyeong Yoon, Sanghun Lee, Minje Kim, Jaesup Lee, Jungsuek Oh, and Sangwook Nam. "LUT-Based Transmit Mode Calibration Complexity Reduction Method for Wireless Power Transfer". *2024 IEEE Wireless Power Technology Conference and Expo (WPTCE 2024)*.
- Uichan Park, Suk Hwangbo, Jinhyun Kim, Taeyeong Yoon, and Jungsuek Oh. "Design of Ku-Band Bi-directional Active Phase Shifter Enabling a Low RMS Error Utilizing Switch-less Staggered Core with the Identical  In-out Matching". *2024 IEEE MTT-S International Microwave Symposium (IMS 2024)*.

**2023**

- Uichan Park, Jungsuek Oh. "A New Class of Method With TE/TM Wave Decomposition and Superposition Enabling High-Efficiency Transmitarray Antenna". *2023 IEEE International Symposium on Antennas and Propagation (ISAP 2023)*.
- Hyunjin Kim and Jungsuek Oh. "140 GHz Wideband Array Antenna-in-package and Sub-array Structures for Scalable Phased Array". *2023 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Jaehoon Kim and Jungsuek Oh. "Slimmed 6G Transmit Reconfigurable Intelligent Surface (RIS) Unit Cells Electromagnetically Tailoring Effective Cell Gap of Liquid Crystal". *2023 European Conference on Antennas and Propagation (EuCAP)*.
- Yongwan Kim, Hyunjun Yang, and Jungsuek Oh. "Heterogeneous Computing and Visibility Preprocessor Accelerated Full-3D Ray Tracing for Large Scale Outdoor Propagation Modeling". *2023 European Conference on Antennas and Propagation (EuCAP)*.
- Hogyeom Kim and Jungsuek Oh. "5G/6G Reconfigurable Intelligent Surface Supporting Multiple Pairs of Polarization and Scattering Modes". *2023 European Conference on Antennas and Propagation (EuCAP)*.

**2022**

- Jaebaek Jung and Jungsuek Oh. "3D Tempered Glass-Covered Metasurface Antenna-in-Package Enabling Reliable 5G/6G Smartphone Beam Coverage". *2022 International Symposium on Antennas and Propagation (ISAP)*.
- Jinhyun Kim and Jungsuek Oh. "A High Gain Vector-Sum Phase Shifter in 28nm CMOS for 5G Communication". *2022 IEEE International Symposium on Radio-Frequency Integration Technology (RFIT)*.
- Seongwoog Oh and Jungsuek Oh. "Triple-Push VCO With Robust Start-Up Tri-Core in CMOS for 6G Communication". *2022 IEEE International Symposium on Radio-Frequency Integration Technology (RFIT)*.
- Hogyeom Kim and Jungsuek Oh. "Polarization-Convertible/Orthogonality-Preserved Reconfigurable Intelligent Surface Using LC-PCB". *2022 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Seongwoog Oh and Jungsuek Oh. "First‑of‑a‑kind 6G Metasurface Links Exceeding Both LOS and NLOS Limits". *2022 IEEE International Symposium on Antennas and Propagation & USNC-URSI Radio Science Meeting (APS-URSI)*.
- Seongwoog Oh, Jinhyun Kim and Jungsuek Oh. "Sub‑THz Switch‑less Reconfigurable Triple‑/Push‑push Dual‑band VCO for 6G Communication". *2022 IEEE Radio Frequency Integrated Circuits Symposium (RFIC)*.

**2021**

- Seongwoog Oh and Jungsuek Oh. "Sub-THz Metasurfacing Antenna-in-Package/ Antenna-on-Package for 6G Communications". *2021 IEEE International Symposium on Antennas and Propagation and North American Radio Science Meeting (APS-URSI)*.
- Euiho Shin and Jungsuek Oh. "Improved and Agile Metasurface Beamforming Using Hybrid Intelligent Algorithms". *2021 IEEE International Symposium on Antennas and Propagation and North American Radio Science Meeting (APS-URSI)*.
- Seongwoog Oh and Jungsuek Oh. "D-band Affordable Phased-Array Antenna-on-Package for 6G Transceivers". *2021 International Symposium on Antennas and Propagation (ISAP)*.
- Seongwoog Oh and Jungsuek Oh. "A Novel Miniaturized Tri-band VCO Utilizing a Three-mode Reconfigurable Inductor". *2021 IEEE Radio Frequency Integrated Circuits Symposium (RFIC)*.

## 특허

Patent의 51개 게시 항목 중 2021년 12월과 2022–2025년에 해당하는 18건이다. 날짜는 목록의 날짜 표기이며 대부분 연월만 있다. 특허번호·등록 상태·발명자 이름은 랩 표기다. 출원과 등록을 같은 건으로 합치지 않았다.[^patents]

- May. 2025 · Array antenna system capable of beam steering and impedance control using active radiation layer (번호 US11990680B2; 상태 등록; 발명자 Jungsuek Oh, Jaehoon Kim)
- May. 2025 · ELECTRONIC DEVICE (번호 US12295232B2; 상태 등록; 발명자 Jungsuek Oh, Jae-Kyoung Kim, Seongryong Lee, Byeongjin Kim, Jeongtaek Oh)
- Aug. 2025 · METASURFACE FOR SMARTPHONE ANTENNA, AND SMARTPHONE DEVICE COMPRISING SAME (번호 US12394904B2; 상태 등록; 발명자 Jungsuek Oh, Jaebaek Jung)
- Aug. 2025 · DISPLAY DEVICE INCLUDING A SENSING ELECTRODE (번호 US12402510B2; 상태 등록; 발명자 Eunjin Sung, Jungsuek Oh, Kiseo Kim, Byeongjin Kim, Jeongtaek Oh, Sangrock YOON)
- Nov. 2025 · LIQUID CRYSTAL POLARIZATION ANTENNA (번호 US12469980B2; 상태 등록; 발명자 Jungsuek Oh, Byeongju Moon)
- Dec. 2025 · ELECTRONIC DEVICE (번호 US12489838B2; 상태 등록; 발명자 Eunjin Sung, Jungsuek Oh, Kiseo Kim, Sangrock Yoon, Byeongjin Kim, Jeongtaek Oh)
- Dec. 2025 · TRANSMISSION LINE FOR MILLIMETER WAVE BAND USING VERTICAL TYPE PIN DIODE (번호 US12489182B2; 상태 등록; 발명자 Jungsuek Oh, Jinhyun Kim)
- May. 2023 · Electronic device (번호 US11662782B2; 상태 등록; 발명자 Jungsuek Oh, Sangrock Yoon, Kiseo Kim, Byeongjin Kim, Jeongtaek Oh)
- Oct. 2023 · Display device including a sensing electrode (번호 US11793052B2; 상태 등록; 발명자 Eunjin Sung, Jungsuek Oh, Kiseo Kim, Byeongjin Kim, Jeongtaek Oh, Sangrock Yoon)
- Nov. 2023 · Electronic device (번호 US11831069B2; 상태 등록; 발명자 Sangrock Yoon, Kiseo Kim, Eunjin Sung, Byeongjin Kim, Jungsuek Oh, Jeongtaek Oh, Seungwook Chun)
- Dec. 2023 · Antenna apparatus (번호 US11855355B2; 상태 등록; 발명자 Juhyoung Park, Jungwoo Seo, Jungsuek OH, Jeongki Ryoo, Kyubum Han)
- Feb. 2022 · Antenna apparatus (번호 US11245201B2; 상태 등록; 발명자 Juhyoung Park, Jungwoo Seo, Jungsuek Oh, Jeongki Ryoo, Kyubum Han)
- Apr. 2022 · Antenna apparatus (번호 US11316272B2; 상태 등록; 발명자 Juhyoung Park, Inseop Yoon, Jungsuek Oh, Jeongki Ryoo, Kyubum Han)
- Sep. 2022 · Antenna apparatus (번호 US11437723B2; 상태 등록; 발명자 Juhyoung Park, Woncheol Lee, Inseop Yoon, Jungwoo Seo, Jungsuek OH)
- Nov. 2022 · Display device including a sensing electrode (번호 US20220375997A1; 발명자 Eunjin Sung, Jungsuek Oh, Kiseo Kim, Byeongjin Kim, Jeongtaek Oh, Sangrock Yoon)
- Mar. 2022 · Array antenna system capable of beam steering and impedance control using active radiation layer (번호 1020220033726; 발명자 Jaehoon Kim and Jungsuek Oh)
- Mar. 11, 2022 · Liquid crystal-based reflective metasurface, and reflective array antenna and antenna device comprising the same (번호 Korea Patent #1023741530000; 발명자 Jongwan Yook, Jungsuek Oh, Hogyeom Kim, and Taehyung Kim)
- Dec. 2021 · Inductor device with improved Q factor using periodic metal pattern structure (번호 Korea Patent #10-2342732; 발명자 Jungsuek Oh and Seongwoog Oh)

## 연구과제

2025년 11월 11일 News의 삼성미래기술육성사업 선정 소식에 적힌 과제 1건이다. 기간은 선정 당시의 표현이다.[^news] AI는 인공지능(Artificial Intelligence), MIMO는 여러 송수신 안테나로 통신하는 다중입출력(Multiple-Input Multiple-Output), DPD는 디지털 사전 왜곡(Digital Predistortion)을 뜻한다.

- 2025-11-11 · 확률론적 역설계 AI 모델 수립 기반 초고밀도 6G MIMO 안테나-DPD 통합 시스템 구현 및 성능 검증 (지원 삼성미래기술육성사업; 기간 향후 4년간)

## 수상과 선정

News의 수상·선정 소식 32건과 교수 소개의 2024년 여름 수상 표기 1건이다. News 날짜는 게시일이고, 교수 소개의 연도·계절 표기는 구체적인 수상일이 게시되어 있지 않다. 서로 다른 게시 항목 수이며, 고유한 수상 사건의 총수를 뜻하지 않는다.[^news][^prof]

- 2026-08-20 · Byeongjin Kim, 한국전자파학회 하계학술대회 IEEE AP-S 서울지부장상 수상
- 2026-08-03 · Seungwoo Bang, IEEE AP-S 학생논문상 3위 수상
- 2026-07-13 · Young-Seok Lee, IEEE WPTCE 학생논문상 1위 수상
- 2026-06-23 · Seungwoo Bang, IEEE AWAP 학생논문상 수상
- 2026-06-23 · Byeongjin Kim, IEEE AP-S C. J. Reddy Travel Grant 선정
- 2026-03-20 · ByeongjinKim, 한국전자파학회 전자파측정 논문 경진대회 최우수상 수상
- 2026-02-26 · Jeongtaek Oh, 한국전자파학회 동계학술대회 우수논문상 수상; Taeyeong Yoon, IEEE MTT-S 서울지부장상 수상
- 2025-11-24 · 삼성전자와 공동 개발한 생성형 인공지능 기반 하드웨어 측정 결과 예측 연구, 삼성전자 Innovation Awards 최우수상 수상
- 2025-11-21 · Seungwoo Bang, 한국전자파학회 Student Paper Competition in Propagation 우수학생논문상 수상
- 2025-11-19 · 김민제, 서울장학재단 AI 서울테크 대학원 장학생 선정
- 2025-09-02 · Hogyeom Kim, 우수학위논문상 수상
- 2025-08-21 · Joonbo Hyun·Uichan Park·Jinhyun Kim, 한국전자파학회 하계학술대회 우수논문상 수상
- 2025-03-24 · Hyunjun Yang·Hooyoung Kim·Seungwoo Bang, 전자파측정 논문 경진대회 Excellence Award 수상
- 2025-02-13 · Young-Seok Lee, 한국전자파학회 동계학술대회 우수논문상 1위; Hogyeom Kim, IEEE AP-S 서울지부장상; Hooyoung Kim, 우수논문상 수상
- 2025-02-07 · Jaehoon Kim, 우수학위논문상 수상
- 2024-12-27 · 오정석 교수, 한국전자파학회 우수연구자상 수상
- 2024-11-21 · Taeyeong Yoon·Young-Seok Lee, 한국전자파학회 Student Paper Competition in Propagation 우수학생논문상 수상
- 2024-11-07 · Young-seok Lee, IEEE ISAP 논문상 2위 수상
- 2024-08-22 · Hogyeom Kim, 한국전자파학회 하계학술대회 우수논문상 수상
- 2024-07-11 · Minje Kim, 한국전자파학회 EMC 장학금 선정
- 2024-03-22 · Young-seok Lee·Taeyeong Yoon·Sanghun Lee·Minje Kim·Jungsuek Oh·Sangwook Nam, 한국전자파학회 전자파측정 논문 경진대회 Excellence Award 수상
- 2024-02-22 · Minje Kim, 한국전자파학회 동계학술대회 우수논문상 수상
- 2024-01-29 · 오정석 교수, 과학기술혁신 유공자 과학기술정보통신부 장관 표창
- 2023-11-24 · Hogyeom Kim·Seungwoo Bang, 한국전자파학회 Student Paper Competition in Propagation 우수학생논문상 수상
- 2023-11-13 · Uichan Park, IEEE ISAP 우수학생논문상 1위 수상
- 2023-10-22 · Jeongtaek Oh, 삼성디스플레이 논문상 수상
- 2023-08-24 · Seungwoo Bang, 한국전자파학회 하계학술대회 우수논문상 1위 수상
- 2022-10-20 · Seongwoog Oh, IEEE AP-S Fellowship 선정
- 2022-10-17 · Jeongtaek Oh·Byeongjin Kim, 삼성디스플레이 기술논문대회 논문상 수상
- 2022-08-18 · Jinhyun Kim, 한국전자파학회 하계학술대회 우수논문상 1위(LIG Nex1); Hogyeom Kim, Excellent Paper Award; Hyunjun Yang, 우수논문상 수상
- 2022-07-15 · Seongwoog Oh, IEEE AP-S/URSI Honorable Mention(입선)
- 2022-02-10 · Taeyeong Yoon, 한국전자파학회 동계학술대회 우수논문상 수상
- 2024 Summer · IEEE AP-S Seoul Chapter Chair Prize (교수 소개 표기)

## 소식

News 1–5쪽에서 2021년 10월 22일–2026년 10월 22일에 해당하는 120건 가운데 논문 게재 66건과 과제 선정 1건, 합계 67건이다. 수상·선정 32건은 「수상과 선정」 절에 두었다. 아래 날짜는 게시일이다.[^news]

- 2026-10-16 · 근거리 무선 전력 전송의 수신 전력 균일성에 관한 논문 게재 승인
- 2026-10-16 · 이중 편파 안테나 배열의 디지털 사전 왜곡에 관한 논문 게재 승인
- 2026-09-22 · 무선 전력 전송의 전력 모드와 고장 허용 최적화에 관한 논문 게재 승인
- 2026-08-12 · 다중 안테나 무선 전력 전송의 효율 최적화에 관한 논문 게재 승인
- 2026-08-11 · 도시 전파 예측을 위한 삼차원 광선 추적에 관한 논문 게재 승인
- 2026-08-06 · 생성형 인공지능을 이용한 안테나 역설계에 관한 논문 게재 승인
- 2026-08-03 · 반도체를 집적한 통과형 안테나 배열에 관한 논문 게재 승인
- 2026-06-03 · 도시 이동통신 채널과 통신 가능 영역 분석에 관한 논문 게재 승인
- 2026-04-08 · 능동 양방향 위상 변환 회로에 관한 논문 게재 승인
- 2026-03-17 · 항공기 표면에 맞추는 전방향 안테나에 관한 논문 게재 승인
- 2026-03-17 · 동시에 두 주파수 대역을 다루는 전력증폭기에 관한 논문 게재 승인
- 2026-02-10 · 표면을 따라 진행하는 파동으로 동작하는 메타표면 안테나에 관한 논문 게재 승인
- 2026-02-03 · 스마트폰 화면에 통합하는 안테나의 성능 제어에 관한 논문 출판
- 2026-01-24 · 도시 실외에서 실내로 전달되는 전파의 손실 모형에 관한 논문 게재 승인
- 2025-12-24 · 안테나 사이 결합을 조절하는 배열 안테나에 관한 논문 게재 승인
- 2025-11-18 · 능동 양방향 위상 변환 회로에 관한 논문 게재 승인
- 2025-11-18 · 고정 무선 통신용 재구성 지능형 표면에 관한 논문 게재 승인
- 2025-11-11 · 오정석 교수, 확률론적 역설계 인공지능을 이용한 안테나 통합 시스템 연구로 삼성미래기술육성사업 선정
- 2025-10-29 · 안테나 설계 연구 논문 게재 승인 (IEEE Open Journal of Antennas and Propagation)
- 2025-08-28 · 화면 통합 안테나 연구 논문 게재 승인 (IEEE Open Journal of Antennas and Propagation)
- 2025-08-14 · 전파 전달 계산 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2025-07-31 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2025-07-29 · 안테나 설계 연구 논문 게재 승인 (IEEE Open Journal of Antennas and Propagation)
- 2025-07-03 · 안테나 설계 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2025-06-25 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Access)
- 2025-06-25 · 무선 전력 전송 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2025-05-28 · 안테나 설계 연구 논문 게재 승인
- 2025-05-28 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2025-03-10 · 메타표면·안테나 연구 논문 출판 소식 (IEEE Transactions on Instrumentation and Measurement)
- 2025-02-10 · 액정 기반 전파 제어 연구 논문 출판 소식 (Journal of Electromagnetic Engineering and Science)
- 2025-01-23 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2024-11-29 · 안테나 설계 연구 논문 게재 승인 (IEEE Access)
- 2024-11-27 · 화면 통합 안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-11-13 · 무선 전력 전송 연구 논문 게재 승인 (IEEE Transactions on Microwave Theory and Techniques)
- 2024-10-23 · 위상 변환 회로 연구 논문 게재 승인 (IEEE Transactions on Microwave Theory and Techniques)
- 2024-10-23 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-10-16 · 고주파 시스템 연구 논문 출판 소식 (IEEE Communications Magazine)
- 2024-08-06 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2024-06-17 · 전파 전달 계산 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-05-30 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-04-15 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-04-06 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2024-02-21 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2024-02-04 · 전력증폭 회로 연구 논문 게재 승인 (IEEE Microwave and Wireless Technology Letters)
- 2023-12-26 · 고주파 시스템 연구 논문 게재 승인 (IEEE Communications Magazine)
- 2023-12-12 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-11-23 · 안테나 설계 연구 논문 게재 승인 (IEEE Access)
- 2023-09-01 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2023-08-31 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2023-08-22 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-08-10 · 고주파 시스템 연구 논문 게재 승인 (IEEE Transactions on Microwave Theory and Techniques)
- 2023-08-10 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-08-02 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-07-14 · 고주파 연결 구조 연구 논문 게재 승인 (IEEE Microwave and Wireless Technology Letters)
- 2023-06-12 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-05-10 · 신호 변조 회로 연구 논문 게재 승인 (IEEE Microwave and Wireless Technology Letters)
- 2023-04-13 · 발진 회로 연구 논문 게재 승인 (IEEE Transactions on Microwave Theory and Techniques)
- 2023-04-04 · 뇌 자극용 회로·무선 전력 전송 시스템 연구 논문 게재 승인 (IEEE Transactions on Biomedical Circuits and Systems)
- 2023-03-22 · 발진 회로 연구 논문 게재 승인 (IEEE Transactions on Microwave Theory and Techniques)
- 2023-03-06 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-01-26 · 전파 도착 방향 추정 연구 논문 게재 승인 (Applied Sciences)
- 2023-01-25 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2023-01-10 · 안테나 설계 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2022-12-19 · 화면 통합 안테나 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2022-09-30 · 액정 기반 전파 제어 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)
- 2022-06-28 · 메타표면·안테나 연구 논문 게재 승인 (IEEE Antennas and Wireless Propagation Letters)
- 2022-03-28 · 전파 전달 계산 연구 논문 게재 승인 (IEEE Transactions on Antennas and Propagation)

## 연락과 위치

- 주소: 서울특별시 관악구 관악로 1 서울대학교[^prof]
- 교수 연구실: 301동 804호, 132동 213호[^prof]
- 교수 전화: +82-2-880-1815(301동), +82-2-880-8216(132동)[^prof]
- 교수 업무 이메일: jungsuek@snu.ac.kr[^prof]
- 연구실 전화: 02-880-1764(학과 연구실 소개 표기)[^lab]
[^research]: Research 개요의 네 연구 갈래. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_0> (2026-10-28).
[^aip]: Antenna-in-Package의 네 연구 소개: 스마트폰 안테나와 메타표면·덮개 공동 설계, 움직임 감지, 화면 통합 안테나, 여러 층의 패키지 안테나. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_1> (2026-10-28).
[^meta]: Metasurface의 다섯 연구 소개는 재료·구조의 배열 설계, 편광에 따른 빔 형상 제어, 액정에 전압을 가해 전자파의 형태를 바꾸는 능동 메타표면 개발을 설명한다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_2> (2026-10-28).
[^ic]: MMIC의 네 연구 소개는 이동통신용 전력증폭기·위상 변환기·발진기, CMOS·갈륨비소·질화갈륨 공정, 재구성 지능형 표면과 회로 결합, 생체 자극용 회로·탐침 개발을 설명한다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_3> (2026-10-28).
[^wireless]: Antenna-in-Package는 5G·6G 스마트폰 안테나 개발을, Metasurface는 이동통신의 전파 도달 범위와 방향을 조절하는 표면을 연구 대상으로 적는다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_1>, <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_2> (2026-10-28).
[^wpt]: MMIC의 「Millimeter-Wave CMOS Power Amplifier for Wireless Power Transfer Systems」는 무선 전력 전송을 위해 전력증폭기의 구조를 설계하고, 회로와 안테나 배열을 함께 검증한다고 적는다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_3> (2026-10-28).
[^sim]: System Simulator의 네 연구 소개: 실내외 광선 추적, 선박 전자파 해석, 휴대기기용 디지털 사전 왜곡 시뮬레이터, 생성형 인공지능 기반 전자파 설계. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_4> (2026-10-28).
[^ai]: System Simulator의 「Generative AI Frameworks for Advanced Electromagnetic Engineering」은 위상 없는 근거리 자료로 원거리 파동을 예측하는 확산 모형과, 물리적 제약·관계를 생성 과정에 넣는 역설계 전략을 개발한다고 적는다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub1_4> (2026-10-28).
[^prof]: 랩 Professor의 학력·경력·수상·업무 연락처. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub2_1> (2026-10-28).
[^dept]: 전기·정보공학부 오정석 교수 소개의 직위·소속·연구 관심과 주요 경력. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p823> (2026-10-28).
[^lab]: 전기·정보공학부 전자파융합 연구실 상세의 이름·홈페이지·연구 소개·전화. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=68&md=view> (2026-10-28).
[^members]: Researchers 전체 카드 28명의 이름·과정·시작 시점·학교 이메일. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub2_2> (2026-10-28).
[^alumni]: Alumni 1–2쪽의 이름·학위·연도·논문·진로. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub2_4>, <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub2_4&page=2> (2026-10-28).
[^journals]: Journal 1–7쪽의 제목·저자·학술지·연도·권호·쪽수·Early Access 표기. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub4_1> (2026-10-28).
[^conferences]: Conference 1–5쪽의 제목·저자·학회·연도 표기. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub4_2> (2026-10-28).
[^patents]: Patent 1–4쪽의 제목·번호·날짜·상태·발명자. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub4_3> (2026-10-28).
[^news]: News 1–5쪽의 고유 항목 147개 중 기간 안 120개는 논문 게재 66개, 수상·선정 32개, 과제 선정 1개 등으로 구분된다. 「소식」에는 논문 게재·과제 선정 67개를, 「수상과 선정」에는 수상·선정 32개를 두었다. <http://wfl.snu.ac.kr/bbs/board.php?bo_table=sub3_1> (2026-10-28).
[^p1]: S. Oh, Y. Park, J. Oh, Journal of Electromagnetic Engineering and Science 26, 88-102 (2026). <https://doi.org/10.26866/jees.2026.1.r.342> 초록 기준(Crossref 등록 초록). 초록 원문 [Crossref 등록 초록](https://api.crossref.org/works?rows=3&query.bibliographic=Sub-THz%20Polarization-Dependent%20Beam-Steerable%20Metasurface%20Antenna-in-Package%20for%206G%20Communication%20Constructed%20Using%20an%20LTCC%20Process)
[^p2]: B. Kim 외, J. Oh, IEEE Transactions on Antennas and Propagation 72, 4086-4094 (2024). <https://doi.org/10.1109/tap.2024.3383725> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p3]: B. Moon, S. Bang, S. Oh, J. Oh, IEEE Open Journal of Antennas and Propagation 6, 1881-1894 (2025). <https://doi.org/10.1109/ojap.2025.3606889> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p4]: H. Kim 외, J. Oh, IEEE Antennas and Wireless Propagation Letters 23, 4194-4197 (2024). <https://doi.org/10.1109/lawp.2024.3438367> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p5]: U. Park 외, J. Oh, IEEE Transactions on Microwave Theory and Techniques 73, 2653-2667 (2025). <https://doi.org/10.1109/tmtt.2024.3476692> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p6]: S. Oh, J. Oh, IEEE Transactions on Microwave Theory and Techniques 71, 4404-4415 (2023). <https://doi.org/10.1109/tmtt.2023.3263590> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p7]: Y. Kim 외, J. Oh, IEEE Transactions on Antennas and Propagation 73, 9255-9270 (2025). <https://doi.org/10.1109/tap.2025.3595956> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^p8]: Y. Kim 외, J. Oh, IEEE Transactions on Antennas and Propagation 72, 5935-5949 (2024). <https://doi.org/10.1109/tap.2024.3411793> 초록 기준(OpenAlex 등록 초록). 초록 원문 [OpenAlex 등록 초록](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660)
[^bio]: Journal 24번은 뇌 자극용 회로와 탐침의 설계·제작·측정을, 37번은 위치·방향 변화에 대응하는 무선 전력 전송 코일과 자극 시스템의 개발을 제시한다. [OpenAlex 등록 초록 10.1109/tmtt.2021.3075726](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660), [OpenAlex 등록 초록 10.1109/tbcas.2023.3255248](https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-74911-2%7C10.1049/mia2.70124%7C10.1109/access.2021.3058647%7C10.1109/access.2022.3150037%7C10.1109/access.2023.3334433%7C10.1109/access.2023.3344093%7C10.1109/access.2024.3506722%7C10.1109/access.2025.3581322%7C10.1109/access.2026.3671652%7C10.1109/ims40360.2025.11103801%7C10.1109/jestpe.2021.3101477%7C10.1109/jmmct.2026.3719661%7C10.1109/jsen.2022.3203847%7C10.1109/lawp.2021.3099818%7C10.1109/lawp.2022.3186686%7C10.1109/lawp.2023.3309990%7C10.1109/lawp.2023.3310496%7C10.1109/lawp.2024.3367497%7C10.1109/lawp.2024.3438367%7C10.1109/lawp.2025.3532301%7C10.1109/lawp.2025.3572958%7C10.1109/lawp.2025.3578089%7C10.1109/lawp.2025.3585144%7C10.1109/lawp.2026.3656909%7C10.1109/lawp.2026.3661970%7C10.1109/lawp.2026.3743501%7C10.1109/lmwc.2020.3045192%7C10.1109/lmwt.2023.3270660%7C10.1109/lmwt.2023.3285883%7C10.1109/lmwt.2023.3348162%7C10.1109/lmwt.2025.3629107%7C10.1109/lmwt.2026.3677742%7C10.1109/mcom.024.2300440%7C10.1109/ojap.2025.3592198%7C10.1109/ojap.2025.3601621%7C10.1109/ojap.2025.3606889%7C10.1109/tap.2022.3161432%7C10.1109/tap.2022.3228912%7C10.1109/tap.2022.3233489%7C10.1109/tap.2023.3248374%7C10.1109/tap.2023.3299008%7C10.1109/tap.2023.3338863%7C10.1109/tap.2024.3383725%7C10.1109/tap.2024.3385101%7C10.1109/tap.2024.3403939%7C10.1109/tap.2024.3411793%7C10.1109/tap.2024.3481661%7C10.1109/tap.2024.3501415%7C10.1109/tap.2024.3510861%7C10.1109/tap.2025.3570006%7C10.1109/tap.2025.3590571%7C10.1109/tap.2025.3595956%7C10.1109/tap.2025.3639500%7C10.1109/tap.2025.3644651%7C10.1109/tap.2026.3681752%7C10.1109/tap.2026.3720777%7C10.1109/tbcas.2023.3255248%7C10.1109/tcomm.2026.3698902%7C10.1109/tim.2025.3548763%7C10.1109/tmtt.2021.3075726%7C10.1109/tmtt.2023.3253545%7C10.1109/tmtt.2023.3263590%7C10.1109/tmtt.2023.3300192%7C10.1109/tmtt.2024.3476692%7C10.1109/tmtt.2024.3487911%7C10.1109/tmtt.2026.3714844%7C10.1109/tmtt.2026.3732370%7C10.1109/tmtt.2026.3734488%7C10.26866/jees.2023.4.l.14%7C10.26866/jees.2024.1.r.199%7C10.26866/jees.2025.1.r.281%7C10.26866/jees.2026.1.r.338%7C10.26866/jees.2026.1.r.342%7C10.3390/aerospace13030227%7C10.3390/app13010660) (2026-10-28).

# 전자파 적합성 연구실 (EMC Lab, Electromagnetic Compatibility Lab)

**KAIST 조천식모빌리티대학원 · 안승영 교수**

- 분야: 전자파 적합성(EMC)과 전자파 인체 노출, 반도체 패키지의 신호·전력 무결성, 전기차·철도 무선전력전송, AI 기반 전자 설계
- 대분야: 전기전자·반도체·광학
- 태그: 전자파 적합성·신호 무결성[^emc][^sipi][^p8], 무선 전력 전송[^p2][^p1][^wpt], 첨단 반도체 패키징[^p6][^p7][^p8], 강화학습[^p6][^p7], 이식형·생체 전자 기기[^p4]
- 홈페이지: <https://emc.kaist.ac.kr/>
- 근거와 출처: [EMC Lab 근거 페이지](emc-sources.md)

> 전자기기가 서로 전자파로 방해하지 않게 하고, 칩 안의 고속 신호와 전력이 깨끗하게 전달되게 하며, 전기차를 선 없이 안전하게 충전하는 기술을 연구한다.[^research][^emc][^sipi][^wpt]

## 무엇을 연구하나

전자파 적합성(EMC)은 전자기기가 주변에 전자파 간섭(EMI)을 일으키지 않고, 바깥 전자파에 흔들리지도 않으면서 제대로 동작하는 능력이다.[^emc] 이 연구실은 전자파 적합성, 신호·전력 무결성, 무선전력전송 세 분야를 연구한다.[^research]

첫 번째 갈래는 **전자파 적합성과 인체 노출**이다. 잡음의 원인과 전달 경로를 측정·분석하고, 커패시터·EMI 필터 같은 부품을 정밀하게 모델링해 제품을 만들기 전에 문제를 예측한다.[^emc] 휴대기기 안테나나 전기차 무선충전에서 나오는 전자기장이 사람 몸에 미치는 영향도 평가하며, 고출력 전자기 펄스(EMP)로부터 장비를 보호하는 연구와 AI 기반 EMC 설계도 한다.[^emc]

두 번째 갈래는 **반도체 패키지의 신호·전력 무결성**이다. 신호 무결성은 고속 신호가 모양과 타이밍을 잃지 않고 전달되는 성질이고, 전력 무결성은 칩에 흔들림 없는 전압과 전류를 공급하는 성질이다.[^sipi] 연구실은 고대역폭 메모리(HBM)의 실리콘 관통 전극(TSV)을 설계하고,[^p8] 3차원 칩 패키지의 전원 배선 배치를 강화학습(시행착오를 거치며 더 나은 선택을 배우는 인공지능)으로 최적화한다.[^p6][^p7]

세 번째 갈래는 **무선전력전송**이다. 여러 송신 코일로 다양한 수신기를 효율적으로 충전하는 시스템을 설계하고, 충전할 때 새어 나오는 자기장을 줄여 사람에 대한 노출과 다른 기기 간섭을 줄인다.[^wpt] 전기차 무선충전의 고조파 간섭을 최대 21.66 dB 줄이는 회로 설계를 내놓았고,[^p2] 충전 영역의 이물질을 감지하거나 무선전력으로 철도 차량 위치를 추적하는 연구도 한다.[^wpt]

## 주요 연구 주제

### 1. 전기차 무선충전의 전자파 저감

효율을 거의 잃지 않으면서 전자파 간섭과 누설 자기장을 줄이는 공진 회로 설계.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 전자파 인체 노출과 생체 무선 소자

체내 이식 기기용 무선충전에서 인체 노출을 줄이는 설계,[^p4] 저주파 무선 바이오 센서.[^p5] 대표 논문 4, 5.

### 3. 반도체 패키지 신호·전력 무결성

HBM용 TSV 설계,[^p8] 3차원 칩 패키지의 강화학습 기반 전원 배선 최적화.[^p6][^p7] 대표 논문 6, 7, 8.

## 대표 논문

최근 5년 논문 중 교수가 마지막 저자(연구 책임)인 것을 중심으로 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2026 | [Magnetically Coupled Resonant Circuit Design for Low Power Loss EMI Suppression in EV Wireless Power Transfer System](https://doi.org/10.1109/tpel.2026.3661024) · IEEE Transactions on Power Electronics | 전력 경로에 필터를 직접 넣지 않고 자기적으로 결합한 보조 공진기로 전기차 무선충전의 전자파 간섭을 줄였다. 전선을 타고 나가는 공통모드 잡음(여러 선에 같은 방향으로 실리는 잡음)을 최대 17 dB 줄이면서 효율은 82.5%로 기존(82.9%)과 거의 같았다.[^p1] | 1저자 Changmin Lee, 마지막 저자 안승영 |
| 2 | 2026 | [An Efficient EMI Reduction Method Through Harmonic Magnetic Field Balancing in Electric Vehicle Wireless Power Transfer System](https://doi.org/10.1109/temc.2025.3632869) · IEEE Transactions on Electromagnetic Compatibility | 고조파(기본 주파수의 정수배로 생기는 원치 않는 성분) 전류의 크기와 위상을 맞추는 공진 회로 설계로, 규격을 넘던 3·5·7차 고조파를 각각 21.66·15.58·18.38 dB 줄였다.[^p2] | 1저자 Hyunsoo Lee, 마지막 저자 안승영 |
| 3 | 2025 | [Design of Resonant Circuit Components to Suppress Both EMF and EMI in Wireless Power Transfer Systems for Electric Vehicles](https://doi.org/10.1109/jestpe.2025.3540010) · IEEE JESTPE | 전기차 무선충전의 공진 회로 부품을 설계해 사람에게 미치는 전자기장(EMF)을 최대 50%, 기기 간섭(EMI)을 최대 14 dB 줄였다.[^p3] | 1저자 Seongho Woo, 마지막 저자 안승영 |
| 4 | 2022 | [An Out-of-Phase Wireless Power Transfer System for Implantable Medical Devices to Reduce Human Exposure to Electromagnetic Field and Increase Power Transfer Efficiency](https://doi.org/10.1109/tbcas.2022.3222011) · IEEE Transactions on Biomedical Circuits and Systems | 몸속 이식 기기를 무선충전할 때 두 코일 사이 인체 조직에 가장 강한 전자기장이 생기는 문제를, 위상을 어긋나게 한 설계로 풀어 전자기장을 41.05% 줄이고 효율을 9.62% 높였다.[^p4] | 1저자 Jangyong Ahn, 마지막 저자 안승영 |
| 5 | 2026 | [Low-frequency ionic-electronic coupling for energy-efficient noise-resilient wireless bioelectronics](https://doi.org/10.1038/s41467-026-70331-4) · Nature Communications | 이온 젤과 작은 LC 안테나를 결합해 1 MHz 아래의 낮은 주파수에서 동작하는 무선 생체 센서 플랫폼(WiLECS). 높은 주파수에서 생기는 간섭과 조직 발열 문제를 피했다.[^p5] | 1저자 Ji Hong Kim, 공동 1저자 김해림(랩 소식 표기), 공동 교신 안승영(랩 소식 표기), 마지막 저자 Do Hwan Kim |
| 6 | 2026 | [Optimization of Power/Ground Microvia Placement in Multiple Power Domain 3D-IC Package Substrates Using Deep Reinforcement Learning](https://doi.org/10.1109/tsipi.2026.3714430) · IEEE Transactions on Signal and Power Integrity | 여러 전원 영역이 섞인 3차원 칩 패키지 기판에서 전원·접지 미세 비아(층을 잇는 작은 구멍)의 위치를 심층 강화학습으로 정해 전력 무결성 설계를 최적화하는 방법. 무작위 탐색·유전 알고리즘보다 실행 시간과 해의 품질이 모두 나았다.[^p6] | 1저자 Seunghun Ryu, 마지막 저자 안승영 |
| 7 | 2024 | [Optimization of the Power/Ground Ball Map in 3-D-IC BGA Packages With Multiple Power Domains Using Deep Reinforcement Learning](https://doi.org/10.1109/tcpmt.2024.3487577) · IEEE TCPMT | 3차원 칩 패키지 바닥의 전원·접지 볼 배치를 강화학습(U-net)으로 최적화해 동시 스위칭 잡음을 줄이고, 다른 배치에도 재사용할 수 있게 했다.[^p7] | 1저자 Seunghun Ryu, 마지막 저자 안승영 |
| 8 | 2023 | [Signal Integrity Analysis of Through-Silicon Via (TSV) With a Silicon Dioxide Well to Reduce Leakage Current for High-Bandwidth Memory Interface](https://doi.org/10.1109/tcpmt.2023.3276862) · IEEE TCPMT | 고대역폭 메모리(HBM)의 실리콘 관통 전극 사이에 산화막 우물을 넣어 누설 전류를 줄였다. 4 GHz에서 삽입 손실(신호가 지나가며 약해지는 정도)을 최대 0.079 dB 개선하고 신호 간 간섭도 줄였다.[^p8] | 1저자 Hyunwoong Kim, 마지막 저자 안승영 |

## 교수와 전문 분야

안승영 교수는 KAIST 전기전자공학과에서 학사(1998)·석사(2000)·박사(2005)를 받았다.[^prof] 삼성전자 Senior Engineer(2005–2009)과 KAIST 연구교수(2009–2011)를 거쳐 조천식모빌리티대학원 조교수·부교수를 지나 교수로 있으며, 전기및전자공학부 겸임교수다.[^prof] IEEE EMC 학회 저명 강연자(2019–2020), IEEE TCPMT 부편집장(2019–)을 맡았다.[^prof] 2026년 7월 국토교통부장관 표창을 받았다.[^news]

논문으로 보면 전문 분야는 세 갈래다.

- **무선전력전송 시스템과 전자파 저감 설계**.[^p1][^p2][^p3][^p4]
- **반도체 패키지 신호·전력 무결성과 AI 기반 설계**.[^p6][^p7][^p8]
- **EMC 측정·모델링과 전자파 인체 노출 평가**.[^emc][^p4]

## 응용 분야

대표 논문과 과제로 보면 전기차·철도·이동 로봇의 무선충전, HBM과 칩렛 같은 첨단 반도체 패키지, 전기차 전력 부품의 전자파 적합성, 5G·6G 기지국의 전자파 인체 노출 예측에 닿아 있다.[^p1][^p6][^p8][^projects] 삼성전자·SK하이닉스·LG이노텍과의 산학 과제가 진행 중이다.[^projects] 졸업생 허성렬 박사는 무선충전 모빌리티 솔루션 기업 코일즈(COILS)를 세웠고,[^news][^alumni] 다수가 삼성전자로, 일부는 충북대·계명대·경국대·한국공학대·순천향대 교수와 ETRI로 진출했다.[^alumni]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제와 이메일은 랩 표기를 옮겼다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Yangbae Chun | 연구원 | Wireless Power Transfer; Development of Absorber for Electromagnetic Anechoic | ybchun@kaist.ac.kr |  |
| Hongseok Kim | 연구원 | Power electronics EMC | kimhongseok@kaist.ac.kr |  |
| Sungryul Huh | 연구원 | Wireless Power Transfer | tjdfuf2397@kaist.ac.kr | 2, 3, 4 |
| Sanguk Lee | 박사과정 | Modeling and Measurement of EMC component; Behaviour modeling of VRM | sang960326@kaist.ac.kr | 2, 6, 7 |
| Hyunwoo Kim | 박사과정 | Signal and Power Integrity | kimhyunwoo@kaist.ac.kr | 6, 7 |
| Hyunsoo Lee | 박사과정 | Wireless Power Transfer System Design; EMF Effects on the Human Body of the 5G/6G Antenna for Mobile Devices | hyunsoolee@kaist.ac.kr | 2 |
| Jinwook Lee | 박사과정 | Signal and Power Integrity | jwlee98@kaist.ac.kr | 6 |
| Kangmin Choi | 박사과정 | Wireless Power Transfer System Design; Design for Electromagnetic Compatibility | kangminchoi@kaist.ac.kr |  |
| Yuchul Jung | 박사과정 | Signal and Power Integrity | rightoil_fe@kaist.ac.kr |  |
| Youbin Jun | 석사과정 | Wireless Power Transfer System Design; Energy Harvesting | youbinjun@kaist.ac.kr |  |
| Junhyeok Park | 석사과정 | Signal and Power Integrity; AI-Based 5G Base Station EMF Prediction | junhyeokpark@kaist.ac.kr |  |
| Youseop Lee | 석사과정 |  | youseoplee@kaist.ac.kr |  |
| Beomgyu Kim | 석사과정 |  | beomgyukim@kaist.ac.kr |  |
| Minji Kim | 석사과정 |  | minji.kim2319@kaist.ac.kr |  |
| Jimin Jeong | 석사과정 |  | stopmean@kaist.ac.kr |  |
| 김영주 | 행정 직원 |  | dudwno@kaist.ac.kr |  |

## 졸업생 진로

랩 졸업생 페이지의 목록(박사 21명, 석사 20명, 명예 동문 3명)이다. 진로는 랩이 적은 소속을 옮겼다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seonghi Lee | Ph.D (2026) | Samsung Electronics |
| Changmin Lee | Ph.D (2026) | Samsung Electronics |
| Seunghun Ryu | Ph.D (2026) | Samsung Electronics |
| Jaewon Rhee | Ph.D (2025) | Prof. at Chungbuk National University |
| Dongryul Park | Ph.D (2025) | Post Doc. at Missouri S&T |
| Seongho Woo | Ph.D (2025) | Prof. at Keimyung University |
| Sungryul Huh | Ph.D (2024) | CEO at COILS |
| Hyunwoong Kim | Ph.D (2024) | Samsung Electronics |
| Haerim Kim | Ph.D (2023) | Samsung Electronics |
| Yujun Shin | Ph.D (2022) | Prof. at Keimyung University |
| Jangyong Ahn | Ph.D (2022) | ETRI |
| Kyunghwan Song | Ph.D (2022) | Samsung Electronics |
| Bumjin Park | Ph.D (2022) | Prof. at Gyeongkuk National University |
| Jedok Kim | Ph.D (2022) | Samsung Electronics |
| Jongwook Kim | Ph.D (2021) | SK Hynix |
| Suna Choi | Ph.D (2020) | ETRI |
| Jaehyoung Park | Ph.D (2020) | Samsung Electronics |
| Dongwook Kim | Ph.D (2019) | Prof. at Tech University of Korea |
| Jaeyong Cho | Ph.D (2019) | CTO at Huwin |
| Kibeom Kim | Ph.D (2019) | Prof. at Soonchunhyang University |
| Karam Hwang | Ph.D (2018) | Samsung Electronics |
| Eunyoung Mun | MS (2026) | KORAIL 철도표준모빌리티프로그램 |
| Pilhoo Jeong | MS (2026) | KORAIL 철도표준모빌리티프로그램 |
| Dongkyun Kim | MS (2026) |  |
| Seungmin Ha | MS (2026) | Hyundai Motors |
| Gagyeong Park | MS (2023) | Ph.D at KAIST (Department of. Aerospace Engineering) |
| Semin Choi | MS (2022) | Samsung Electronics |
| Andrés S. Brito Calderón | MS (2020) | Ph.D at SUTD (Electrical Engineering) |
| Seokhyeon Son | MS (2022) | Hyundai Motors |
| Nguyen Minh Nghiem (Neil) | MS (2021) | Vinfast |
| Dawon Jeong | MS (2021) | Samsung Electronics |
| Kiwon Hwang | MS (2013) | ASML |
| Sunghwan Kim | MS (2014) | Hyundai Motors Group |
| Sungkyu Kim | MS (2014) | LG Electronics, CTO |
| Hwansoo Moon | MS (2015) | Hyundai Motors Group |
| Minho Kim | MS (2015) | Mando, Global R&D Center |
| Jesung Yoo | MS (2015) | LG Chemical, R&D Center |
| Hongkyun Kim | MS (2018) | Synopsys, Portugal |
| Chungjae Choe | MS (2020) | KETI |
| Chanjun Park | MS (2020) | Samsung Electronics |
| Kiback Jung | MS (2020) | Deepscent |
| Junsung Choi | Postdoctoral researcher / Research professor (2023) | Prof. at Chungbuk National University |
| Amirhossein Hajiaghajani | Research Intern (2018) | Apple |
| Ki-Cheol Yoon | Postdoctoral researcher (2018) | Gacheon University Gil Medical Center |

## 논문 목록

랩 국제 학술지 목록 전체(157편, 랩 번호순)다. 랩 목록에 게재 연도가 빠진 항목이 많아 연도별로 나누지 않았다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

- Hyunwoo Kim, Seunghun Ryu, Sanguk Lee, Seonghi Lee, Jinwook Lee, Junhyeok Park, Seungyoung Ahn. "An Integrated Framework for Channel Optimization and Routing-Aware Bump Map Design in High-Speed Chiplet Interconnects". *IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Seunghun Ryu, Seonghi Lee, Sanguk Lee, Hyunwoo Kim, Seongho Woo, Dongryul Park, Jinwook Lee, Dongkyun Kim, Seokbeom Yong, Sangsub Song, Seungyoung Ahn. "Optimization of Power/Ground Microvia Placement in Multiple Power Domain 3D-IC Package Substrates using Deep Reinforcement Learning". *IEEE Transactions on Signal and Power Integrity*.
- Seonghi Lee, Sanguk Lee, Hyunwoo Kim, Dongryul Park, Seunghun Ryu, Jinwook Lee, Hyunsik Kim, Duksoo Kim, Seungyoung Ahn. "VCVS-Based Reflection Wave Decomposition Method for Analysis of Multiloading Transmission-Line Channels". *IEEE Transactions on Microwave Theory and Techniques (2026)*.
- Seonghi Lee, Sanguk Lee, Zhiping Yang, Seungyoung Ahn, Chulsoon Hwang. "A Transformer-based IBIS-AMI Modeling Method for High-Speed Nonlinear Buffers". *in IEEE Transactions on Signal and Power Integrity*.
- Seonghi Lee, Sanguk Lee, Seunghun Ryu, Hyunwoo Kim, Seongho Woo, Jinwook Lee, Jiseong Kim and Seungyoung Ahn. "Design of Termination Resistance-Adjusted Passive Equalizer for Low-Power and High-Speed Signaling". *in IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Hyunwoo Kim, Seunghun Ryu, Sanguk Lee, Seonghi Lee, Dongryul Park, Jinwook Lee, and Seungyoung Ahn. "Perforated Ground Plane Design for Mitigating Mode Conversion in the High-speed Differential Channels of a Die-to-Die Interface". *in IEEE Transactions on Signal and Power Integrity*.
- Pilhoo Jeong, Hyunsoo Lee, Youbin Jun, Sungryul Huh, and Seungyoung Ahn. "Optimized Parallel-Resonant Impedance Matching for Railway Magnetic Field Energy Harvesting". *in IEEE Transactions on Magnetics, 2026*.
- Hyunwoo Kim, Seunghun Ryu, Sanguk Lee, Seonghi Lee, Dongryul Park, Jinwook Lee, Jongwook Kim, and Seungyoung Ahn. "A Signal Integrity (SI)-driven Comprehensive Framework for High-speed Interconnect Designs and Evaluations in Advanced System-in-Package (SiP) Systems". *in IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Seungmin Ha, Jaewon Rhee, Sanguk Lee, Jiseong Kim, and Seungyoung Ahn. "Design and Analysis of a Gate Driver Power Supply Architecture for Common-Mode Current Reduction". *in IEEE Access*.
- Akimasa Hirata, Teruo Onishi, Naoki Shinohara, Valerio De Santis, Yinliang Diao, Mauro Feliziani, Takashi Hikage, Junging Lan, Francesca Maradei, Keishi Miwa, Alexander Prokop, Yujun Shin, Seungyoung Ahn. "Electromagnetic Field Exposure Assessment and Mitigation Strategies for Wireless Power Transfer Systems: A Review and Future Perspectives". *in IEEE Journal on Wireless Power Technologies*.
- . "Yujun shin, Seungyoung Ahn, Hyunsoo Lee, Seongho Woo, "A Multi-Frequency Harmonic Suppression Approach for Eliminating Radiated Emissions in LCC-LCC WPT System for Electric Vehicles“, in IEEE Transactions on Industrial Electronics". **.
- Changmin Lee, Jaewon Rhee, Seongho Woo, Seungmin Ha and Seungyoung Ahn. "Magnetically Coupled Resonant Circuit Design for Low Power Loss EMI Suppression in EV Wireless Power Transfer System". *in IEEE Transactions on Power Electronics, doi: 10.1109/TPEL.2026.3661024*.
- Ji Hong Kim, Haerim Kim, Jaewon Rhee, Joo Sung Kim, Hanbin Choi, Won Hyuk Choi, Seungyoung Ahn, and Do Hwan Kim. "Low-frequency ionic-electronic coupling for energy-efficient noise-resilient wireless bioelectronics". *Nature Communications*.
- Doeon Kim, Dongryul Park, Jinbae Seo, Hyungchan Cho, Seungyoung Ahn, Namwoo Kang, Seongsin Kim. "Estimation of Electromagnetic Field Strength: Experiments Using Vision Transformers". *in IEEE Access, vol. 13, pp. 195735-195748, 2025*.
- Hyunsoo Lee, Seongho Woo, Sungryul Huh, Sanguk Lee, Jaewon Rhee, Changmin Lee, Minseok Kang, and Seungyoung Ahn. "An Efficient EMI Reduction Method through Harmonic Magnetic Field Balancing in Electric Vehicle Wireless Power Transfer System". *in IEEE Transactions on Electromagnetic Compatibility*.
- Sanguk Lee, Jaewon Rhee, Seunghun Ryu, Seonghi Lee, Hyunwoo Kim, Hongseok Kim, seungyoung Ahn. "A Method for Estimating Impedance of Floating Electrode Multi-layered Ceramic Capacitor". *IEEE Microwave and Wireless Technology Letters*.
- Jaewon Rhee, Sanguk Lee, Seungmin Ha, Changmin Lee, Seongho Woo, Yujun Shin, Hongseok Kim, Jiseong Kim, Seungyoung Ahn. "An Efficient Capacitance Extraction Method for Multi-chip Power Modules for EMI analysis". *IEEE Transactions on Power Electronics*.
- Jaewon Rhee, Seungmin Ha, Jiseong Kim, Seungyoung Ahn. "A Practical Method for Module-Level Capacitance Estimation in Automotive Power Module Using Datasheet-Based Modeling". *IEEE Access*.
- Jaewon Rhee, Seongho Woo, Yujun Shin, Jiseong Kim and Seungyoung Ahn. "A 3-port Network-based Capacitance Measurement Method for Asymmetric Half-Bridge Power Modules". *IEEE Access*.
- Jaewon Rhee, Changmin Lee, Sanguk Lee, Seongho Woo, Yujun Shin, Seungyoung Ahn. "A Dual Current Probes Method with Enhanced Low-Frequency Sensitivity for High-Voltage Dynamic Capacitance Measurement". *IEEE Transactions on Instrumentation & Measurement*.
- Yujun Shin, Jaewon Rhee and Seongho Woo. "Resonance Circuit Design Eliminating RX-Side Series Capacitor in LCC-LCC WPT Systems Using an RX Shield Coil". *Electronics 2025*.
- Dongryul Park, Seonghi Lee, Seunghun Ryu, Hyunwoo Kim, Duksoo Kim, Hyunsik Kim, Jongwook Kim, and Seungyoung Ahn. "Scalable and Fast Electrical Modeling Method for Bonding-Wire Memory Packages". *IEEE Access*.
- Seonghi Lee, Seunghun Ryu, Sanguk Lee, Hyunwoong Kim, Seongho Woo, Dongryul Park, Hyunwoo Kim, Jiyoung Park, Yongho Lee, Seungki Nam, Sungwook Moon, Jiseong Kim and Seungyoung Ahn. "A Fast SerDes Equalizer Effect-Included Worst Eye Diagram Estimation Method for High-Speed Serial Links". *in IEEE Transactions on Components, Packaging and Manufacturing Technology*.
- Seongho Woo, Yujun Shin, Jaewon Rhee, Sungryul Huh and Seungyoung Ahn. "Design of Resonant Circuit Components to Suppress both EMF and EMI in Wireless Power Transfer Systems for Electric Vehicles". *in IEEE Journal of Emerging and Selected Topics in Power Electronics, doi: 10.1109/JESTPE.2025.3540010*.
- Francesca Maradei, Seungyoung Ahn, Tommaso Campi, Grant Covic, Silvano Cruciani, Akimasa Hirata, Shuo Wang, and Mauro Feliziani. "EMC and EMF Safety Aspects of Wireless Power Transfer Systems for e-Mobility". *in IEEE Electromagnetic Compatibility Magazine, vol. 13, no. 3, pp. 74-92, 3rd Quarter 2024, doi: 10.1109/MEMC.2024.10834399*.
- Seongho Woo , Yujun Shin, Jaewon Rhee, Hyunsoo Lee, Hongseok Kim and Seungyoung Ahn. "Frequency Selective Suppression Method of Harmonic Magnetic Field for Double-Sided LCC Wireless Power Transfer Systems". *IEEE Transactions on Power Electronics, vol. 40, no. 4, pp. 4701-4705, April 2025, doi: 10.1109/TPEL.2024.3507874*.
- Seunghun Ryu, Dongryul Park, Hyunwoong Kim, Seonghi Lee, Sanguk Lee, Hyunwoo Kim, Seongho Woo, Seokbeom Yong, Sangsub Song, and Seungyoung Ahn. "Optimization of the Power/Ground Ball Map in 3D-IC BGA Packages with Multiple Power Domains using Deep Reinforcement Learning". *IEEE Transactions on Components, Packaging and Manufacturing Technology, vol. 14, no. 11, pp. 1943-1958, Nov. 2024*.
- Yujun Shin, Jaewon Rhee and Seongho Woo. "Resonance Capacitance Selection Method for Minimizing Leakage Magnetic Fields and Achieving Zero Phase Angles in Wireless Power Transfer Systems". *Electronics, Vol. 13, No. 21, p. 4188, October 25, 2024*.
- Yujun Shin and Seongho Woo. "Method for Determining the Compensation Circuit Values to Minimize the Leakage Magnetic Field of Wireless Power Transfer System with Double-sided LCC Topology". *Journal of Electromagnetic Engineering and Science (JEES)*.
- Jaewon Rhee, Sanguk Lee, Changmin Lee, Seongho Woo, Hongseok Kim, Jiseong Kim and Seungyoung Ahn. "One-step Method of Dynamic Capacitances Extraction from a SiC Power MOSFET in a Half-Bridge Package for EMI Analysis". *IEEE Transactions on Power Electronics , Vol. 40, No. 1, pp. 969-983, October 8, 2024*.
- Changmin Lee, Jaewon Rhee, Hyukchoon Kwon, Yongho Park and Seungyoung Ahn. "A Reduction Method of Phantom Shell Effects for APD Extraction Using Negative Permittivity Material". *IEEE Access, Vol. 12, pp. 134862-134873, September 16, 2024*.
- Jaewon Rhee, Sanguk Lee, Hongseok Kim, Jiseong Kim and Seungyoung Ahn. "A Simple Characterization Method for Parasitic Capacitances Extraction of SiC Power MOSFETs Integrated Half-bridge Configuration". *IEEE Journal of Emerging and Selected Topics in Power Electronics , vol. 12, no. 6, pp. 5638-5647, Dec. 2024*.
- Jaewon Rhee, Seongho Woo, Changmin Lee and Seungyoung Ahn. "Selection of Ferrite Depending on Permeability and Weight to Enhance Power Transfer Efficiency in Low-Power Wireless Power Transfer Systems". *Energies , Vol. 17, No. 15, p. 3816, August 2, 2024*.
- Sanguk Lee, Hyunwoong Kim, Jangyong Ahn, Jaewon Rhee, Jaeyong Cho, Hongseok Kim and Seungyoung Ahn. "A Method for De-embedding the Mounting Pad and Via-Hole Effect in a Test Fixture for Accurate Impedance Measurement of the Surface Mount Device Component". *IEEE Transactions on Instrumentation and Measurement, Vol. 73, April 29, 2024*.
- Yujun Shin and Seongho Woo. "Reactive Shield for Reducing the Magnetic Field of a Wireless Power Transfer System with Dipole Coil Structure". *Electronics, Vol. 13, No. 9, p. 1712, April 29, 2024*.
- . "Seongho Woo , Yujun Shin, Changmin Lee, Jungick Moon, Hyunwoong Kim, Hongseok Kim, Sungryul Huh and Seungyoung Ahn, "Design and Analysis of LCC-S Wireless Power". **.
- Jaewon Rhee, Hyunwoong Kim, Kwanguk Chu, and Seungyoung Ahn. "Methodology for Extracting Low-frequency Input Impedance of Personal Computer (PC) during Operation using Dual Current Probes Method". *IEEE Transactions on Electromagnetic Compatibility , Vol. 66, No. 2, pp. 584 - 598, January 17, 2024*.
- Sungryul Huh, Ja-il Koo, Okhyun Jeong, and Seungyoung Ahn. "Maximizing Output Power Using a Magnetic Energy Harvesting System Considering the Relationship between Harvesting Time and Induced Voltage due to a Change of Airgap". *IEEE Access , Vol. 12, pp. 5947-5959, December 22, 2023*.
- Hyunwoong Kim, Jongchoel Park, Sanguk Lee, Jongwook Kim, and Seungyoung Ahn. "Signal Integrity Analysis of Through-Silicon-Via (TSV) with Passive Equalizer to Separate Return Path and Mitigate the Inter-Symbol Interference (ISI) for Next Generation High Bandwidth Memory". *IEEE Transactions on Components, Packaging and Manufacturing Technology , Vol. 13, No. 12, pp. 1973-1988, November 20, 2023*.
- Jungsung Choi and Seungyoung Ahn. "A 5.9 GHz Channel Characterization at Railroad Crossings for Train-to-Infrastructure (T2I) Communications". *Electronics, 12(11), 2400, 2023*.
- Hyunwoong Kim, Seonghi Lee, Jongcheol Park, Yujun Shin, Seongho Woo, Jongwook Kim, Jaeyong Cho, and Seungyoung Ahn. "Signal Integrity Analysis of Through-Silicon Via (TSV) with a Silicon Dioxide Well to Reduce Leakage Current for High-Bandwidth Memory Interface". *IEEE Transactions on Components, Packaging and Manufacturing Technology , Vol. 13, No. 5, pp. 700 - 714, May 16, 2023*.
- Haerim Kim, Jongwook Kim, Jangyong Ahn, Yujun Shin, Bumjin Park, Sungryul Huh, Semin Choi, Jaehyoung Park, and Seungyoung Ahn. "Determination of Compensation Capacitor Considering the Dead-time Characteristics for ZVS in Wireless Power Transfer System". *IEEE Journal of Emerging and Selected Topics in Power Electronics , Vol. 11, No. 3, pp. 2501 - 2513, January 19, 2023*.
- Jangyong Ahn, Seongho Woo, Haerim Kim, Kyunghwan Song, Sungryul Huh, Seon-Eui Hong, Jedok Kim, Hyung-Do Choi and Seungyoung Ahn. "An Out-of-Phase Wireless Power Transfer System for Implantable Medical Devices to Reduce Human Exposure to Electromagnetic Field and Increase Power Transfer Efficiency". *IEEE Transactions on Biomedical Circuits and Systems , Vol. 16, No. 6, pp. 1166 - 1180, November 17, 2022*.
- Seongho Woo, Yujun Shin, Changmin Lee, Jaewon Rhee, Jangyong Ahn, Jungick Moon, Seokhyeon Son, Sanguk Lee, Hongseok Kim and Seungyoung Ahn. "Minimizing Leakage Magnetic Field of Wireless Power Transfer Systems Using Phase Difference Control". *Energies 2022, 15, 8202. https://doi.org/10.3390/en15218202*.
- Sungryul Huh, Bumjin Park, Semin Choi, Yujun Shin, Haerim Kim, Jongwook Kim, Jaehyoung Park, Dongryul Park, and Seungyoung Ahn. "Transmitter Coils Selection Method for Wireless Power Transfer System with Multiple Transmitter Coils and Single Receiver Coil". *IEEE Transactions on Power Electronics , Vol. 38, No. 3, pp. 4092 - 4109, October 25, 2022*.
- Myunghoi Kim  and Seungyoung Ahn. "Analytical Approaches for Effects of Edge-Located EBG Structure With Defected Ground Structure on Cavity-Mode Resonances of Power/Ground Planes". *IEEE Transactions on Microwave Theory and Techniques , Vol. 70, No. 12, pp. 5405-5417, October 13, 2022*.
- Changmin Lee, Seongho Woo, Yujun Shin, Jaewon Rhee, Jungick Moon and Seungyoung Ahn. "EMI Reduction Method for Wireless Power Transfer Systems With High Power Transfer Efficiency Using Frequency Split Phenomena". *in IEEE Transactions on Electromagnetic Compatibility, 2022, doi: 10.1109/TEMC.2022.3198753*.
- Dongwook Kim and Seungyoung Ahn. "Wireless Power Transfer-Based Microrobot with Magnetic Force Propulsion Considering Power Transfer Efficiency". *Journal of Electromagnetic Engineering and Science (JEES), Vol. 22, No. 4, pp. 488-495, January 31, 2022*.
- Hyunwoong Kim, Seonghi Lee, Kyunghwan Song, Yujun Shin, Dongyrul Park, Jongcheol Park, Jaeyong Cho, and Seungyoung Ahn. "A Novel Interposer Channel Structure with Vertical Tabbed Vias to Reduce Far-End Crosstalk for Next-Generation High-Bandwidth Memory". *Micromachines, Micromachines 13, no. 7: 1070. https://doi.org/10.3390/mi13071070*.
- Yujun Shin, Seongho Woo, Changmin Lee, Jaiwoong Jeong, Gyumin Kwak, Seungyoung Ahn. "Design of a Wireless Power Transfer System with Two Inputs with Large Voltage Differences for Missiles Mounted on Maritime Vessels". *in IEEE Access, 2022, vol. 10, pp. 70825 - 70839, June, 2022, 10.1109/ACCESS.2022.3187184*.
- Seunghun Ryu, Kibeom Kim, Jang-Yeol Kim, In-Kui Cho, Haerim Kim, Jangyong Ahn, Junsung Choi and Seungyoung Ahn. "Design and Analysis of a Magnetic Field Communication System using a Giant Magneto-Impedance Sensor". *IEEE Access, vol. 10, pp. 56961-56973, May, 2022, doi: 10.1109/ACCESS.2022.3171581*.
- Yujun Shin, Seongho Woo, Jaewon Rhee, Changmin Lee, Haerim Kim, Sungryul Huh, Bumjin Park and Seungyoung Ahn. "Accurate Method for Extracting the Coupling Coefficient of an LCC-Series Wireless Power Transfer System". *in IEEE Transactions on Power Electronics, vol. 37, no. 9, pp. 11406-11422, Sept. 2022, doi: 10.1109/TPEL.2022.3168087*.
- Seokhyeon Son, Seongho Woo, Haerim Kim, Jangyong Ahn, Sungryul Huh, Sanguk Lee, Seungyoung Ahn. "Shielding Sensor Coil to Reduce the Leakage Magnetic Field and Detect the Receiver Position in Wireless Power Transfer System for Electric Vehicle". *Energies, Vol. 15, No. 7, Mar. 2022*.
- Junsung Choi, V. Marojevic, C. B. Dietrich and Seungyoung Ahn. "DSRC-Enabled Train Safety Communication System at Unmanned Crossings". *in IEEE Transactions on Intelligent Transportation Systems, doi: 10.1109/TITS.2022.3159778*.
- Junsung Choi, Dongryul Park, Suil Kim and Seungyoung Ahn. "Implementation of a Noise-Shaped Signaling System through Software-Defined Radio". *Applied Science, 2022*.
- Jangyong Ahn, Seon-Eui Hong, Haerim Kim, Kyunghwan Song, Hyung-Do Choi, and Seungyoung Ahn. "Improved Calculation Method of Coupling Factors for Low-Frequency Wireless Power Transfer Systems". *International Journal of Environmental Research and Public Health, Vol. 44, No. 44, Dec. 2021*.
- Jaewon Rhee, Yujun Shin, Seongho Woo, Changmin Lee, Dongwook Kim, Jangyong Ahn, Haerim Kim, and Seungyoung Ahn. "Wireless Torque and Power Transfer Using Multiple Coils with LCC‐S Topology for Implantable Medical Drug Pump". *Sensors, Vol. 21, No. 8150, Nov. 2021*.
- A. Hirata et al.. "Assessment of Human Exposure to Electromagnetic Fields: Review and Future Directions". *in IEEE Transactions on Electromagnetic Compatibility, vol. 63, no. 5, pp. 1619-1630, Oct. 2021*.
- Seokhyeon Son, Yujun Shin, Seongho Woo, and Seungyoung Ahn. "Sensor Coil System for Misalignment Detection and Information Transfer in Dynamic Wireless Power Transfer of Electric Vehicle". *Journal of Electromagnetic Engineering and Science (JEES)*.
- Jedok Kim and Seungyoung Ahn. "Dual Loop Reactive Shield Application of Wireless Power Transfer System for Leakage Magnetic Field Reduction and Efficiency Enhancement". *IEEE Access, Vol. 9, pp. 118307-118323, August 20, 2021*.
- Dongwook Kim, Jangyong Ahn, and Seungyoung Ahn. "Propulsion of a Magnetic Material-Applied Microrobot in a Tube Based on a Wireless Power Transfer System". *Journal of Electromagnetic Engineering and Science (JEES)*.
- Jangyong Ahn, Jedok Kim, Dongryul Park, Haerim Kim, and Seungyoung Ahn. "An Active Shielding Control Method for a Wireless Power Transfer System Under Misalignment Condition". *Journal of Electromagnetic Engineering and Science (JEES)*.
- Kyunghwan Song, Jongwook Kim , Hyunwoong Kim, Seonghi Lee, Jangyong Ahn, Andres Brito, Hyunsik Kim, Minho Park and Seungyoung Ahn. "Modeling, Verification, and Signal Integrity Analysis of High-Speed Signaling Channel with Tabbed Routing in High Performance Computing Server Board". *Electronics 10, no. 13: 1590., July. 2021*.
- Kibeom Kim, Seunghun Ryu, Jang-Yeol Kim, In-Kui Cho, Hyun-Joon Lee, Jaewoo Lee, and Seungyoung Ahn. "Giant Magnetoimpedance Receiver with A Double-Superheterodyne Topology for Magnetic Communication". *in IEEE Access*.
- Bumjin. Park, Sungryul Huh, Jongwook Kim, Haerim Kim, Yujun Shin, Seongho Woo, Jaehyoung Park, Andres Brito, Dongwook Kim, Hyun Ho Park, Okhyun Jeong, Ja-Il Koo and Seungyoung Ahn. "The Magnetic Energy Harvester with Improved Power Density Using Saturable Magnetizing Inductance Model for Maintenance Applications Near High Voltage Power Line". *in IEEE Access*.
- Dongryul Park, Jangyong Ahn, Chungjae Choe, Seongho Woo, Seungyoung Ahn and Junsung Choi. "A Noise-Shaped Signaling Method for Vehicle-to-Everything Security". *in IEEE Access, vol. 9, pp. 75385-75397, 2021*.
- Yujun Shin, Jaehyoung Park, Haerim Kim, Seongho Woo, Bumjin Park, Sungryul Huh, Changmin Lee, and Seungyoung Ahn. "Design Considerations for Adding Series Inductors to Reduce Electromagnetic Field Interference in an Over-Coupled WPT System". *Energies 14, no. 10: 2791., May, 2021*.
- SangWook Park and Seungyoung Ahn. "Novel Resonance-Based Wireless Power Transfer Using Mixed Coupling". *MDPI Sensors, 20, 7277, Dec. 2020*.
- Jang-yeol Kim, In-Kui Cho, Hyun Joon Lee, Jaewoo Lee, Jung-ick Moon, Seong-Min Kim, Sang-Won Kim, Seungyoung Ahn, and Kibeom Kim. "A Novel Experimental Approach to the Applicability of High-Sensitivity Giant Magneto-Impedance Sensors in Magnetic Field Communication". *IEEE Access, Oct. 2020*.
- Jaeyong Cho, Jangyong Ahn, Jongwook Kim, Jaehyoung Park, Yujun Shin, Kibeom Kim, Junsung Choi, and Seungyoung Ahn. "Low- and High-Frequency Extrapolation of Band-Limited Frequency Responses to Extract Delay Causal Time Responses". *IEEE Transactions on Electromagnetic Compatibility, Oct, 2020*.
- Jedok Kim, Jangyong Ahn, Sungryul Huh, Kibeom Kim, and Seungyoung Ahn. "A coil design and control method of independent active shielding system for leakage magnetic field reduction of wireless UAV charger". *IEICE Transactions on Communications, In Publication, Jul. 2020*.
- Junsung Choi, Vuk Marojevic, Carl B. Dietrich, Jeffrey H. Reed, and Seungyoung Ahn. "Survey of Spectrum Regulation for Intelligent Transportation Systems". *IEEE Access. 29 July, 2020*.
- Chungjae Choe, Jangyong Ahn, Junsung Choi, Dongryul Park, Minjun Kim, and Seungyoung Ahn. "A Robust Channel Access using Cooperative Reinforcement Learning for Congested Vehicular Networks". *IEEE Access, 23 July, 2020*.
- Junho Kim, Hyeok Kim, Dongwook Kim, Hun-Jun Park, Kiwon Ban, Seungyoung Ahn, and Sung-Min Park. "A Wireless Power Transfer based Implantable ECG Monitoring Device". *Energies, 1 February, 2020*.
- . "Dongwook Kim, Dawon Jeong, Jongwook Kim, Haerim Kim, Junho Kim, Sung-Min Park, and Seungyoung Ahn, "Design and implementation of a wireless charging based cardiac monitoring". **.
- Chanjun Park, Jaehyoung Park, Yujun Shin, Jongwook Kim, Sungryul Huh, Dongwook Kim, and Seungyoung Ahn. "Separated Circular Capacitive Coupler for Reducing Cross-Coupling Capacitance in Drone Wireless Power Transfer System". *IEEE Transactions on Microwave Theory and Techniques, May, 2020*.
- Suna Choi, Seungkeun Park, Kyu-Min Kang, and Seungyoung Ahn. "Analysis of Spectrum Requirements for Autonomous Driving Using SINR Probability Distributions". *IEEE Communications Letters, vol. 24, no. 1, pp. 202-206, Jan. 2020*.
- Jangyong Ahn, Sun-Eui Hong, Haerim Kim, Yangbae Chun, Hyung-Do Choi, Kibeom Kim, Brito Andres, Junsung Choi, and Seungyoung Ahn. "Compliance Testing for Human Body Model Exposure to Electromagnetic Fields from a High-power Wireless Charging System for Drones". *Radiation Protection Dosimetry, February 24. 2020*.
- Dongwook Kim, Hongseok Kim, Anfeng Huang, Qiusen He, Hanyu Zhang, Seungyoung Ahn, Yuyu Zhu, Youkuan Kang, and Jun Fan. "Analysis and Introduction of Effective Permeability with Additional Air-Gaps on Wireless Power Transfer Coils for Electric Vehicle Based on SAE J2954 Recommended Practice". *MDPI Energies, December. 2019*.
- Dongwook Kim, Jaehyoung Park, Bumjin Park, Yujun Shin, Kibeom Kim, Hyun Ho Park, and Seungyoung Ahn. "Propulsion and Rotation of Microrobot Based on a Force on a Magnetic Material in a Time-Varying Magnetic Field Using Wireless Power Transfer System". *IEEE Transactions on Magnetics, Accepted, Sep. 2019*.
- Amirhossein Hajiaghajani, Dongwook Kim, and Seungyoung Ahn. "Patterned Magnetic Fields for Remote Steering and Wireless Powering to a Swimming Microrobot". *IEEE Transactions on Mechatronics, Accepted, 2019*.
- Seokwoo Hong, Youngwoo Kim, Seongsoo Lee, Seungtaek Jeong, Boogyo Sim, Hongseok Kim, Jinwook Song, Seungyoung Ahn, and Joungho Kim. "A Frequency-Selective EMI Reduction Method for Tightly Coupled Wireless Power Transfer Systems Using Resonant Frequency Control of a Shielding Coil in Smartphone Application". *IEEE Transactions on Electromagnetic Compatibility, vol. 61, no. 6, pp. 2031-2039, Dec. 2019*.
- Jongwook Kim, Kibeom Kim, Haerim Kim, Dongwook Kim, Jaehyoung Park, and Seungyoung Ahn. "An Efficient Modeling for Underwater Wireless Power Transfer Using Z-parameter". *IEEE Transactions on Electromagnetic Compatibility, vol. 61, no. 6, pp. 2006-2014, Dec. 2019*.
- Jaeyong Cho, Karam Hwang, Seungil Jeung, and Seungyoung Ahn. "An Efficient Extrapolation Method of Band-limited S-parameters for Extracting Causal Impulse Responses". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, November. 2019*.
- Kibeom Kim, Junsung Choi, Seongho Woo, Jaeyong Cho, and Seungyoung Ahn. "E-field Induced Keep-Out Zone Determination Method of Through-Silicon Vias for 3-D ICs". *Microelectronics reliability, July. 2019*.
- Seongsoo Lee, Donghyun Kim, Yeonje Cho, Hongseok Kim, Chiuk Song, Seungtaek Jeong, Jinwook Song, Gyeyoung Park, Seokwoo Hong, Junyong Park, Kyungjun Cho, Hyunsuk Lee, Chulhun Seo, Seungyoung Ahn, and Joungho Kim. "Low Leakage Electromagnetic Field level and High Efficiency using a Novel Hybrid Loop-array Design for Wireless High Power Transfer System". *IEEE Transactions on Industrial Electronics, vol. 66, no. 6, pp. 4356-4367, Jun. 2019*.
- Hyun Ho Park and Seungyoung Ahn. "Millimeter-Wave Scattering and Transmission of Misaligned Dual Metallic Grating Screens". *IEICE Transactions on Communications, E102B, no. 6, pp. 1180-1187, Jun. 2019*.
- Jaehyoung Park, Chanjun Park, Yujun Shin, Dongwook Kim, Bumjin Park, Jaeyong Cho, Junsung Choi, and Seungyoung Ahn. "Planar multi resonance reactive shield for reducing electromagnetic interference in portable wireless power charging application". *Applied Physics Letters, 114, 203902, 2019*.
- Amirhossein Hajiaghajani and Seungyoung Ahn. "Single-Sided Near-Field Wireless Power Transfer by A Three-Dimensional Coil Array". *Micromachines, Vol. 10, No. 3, March 21, 2019*.
- Yujun Shin, Karam Hwang, Jaehyoung Park, Dongwook Kim, and Seungyoung Ahn. "Precise Vehicle Location Detection Method Using a Wireless Power Transfer (WPT) System". *IEEE Transactions on Vehicular Technology, vol. 68, no. 2, pp. 1167-1177, Feb. 2019*.
- Karam Hwang, Jaeyong Cho, Jaehyoung Park, Dongsoo Har, Seungyoung Ahn. "Ferrite Position Identification System Operating with Wireless Power Transfer for Intelligent Train Position Detection". *IEEE Transactions on ITS, vol. 20, no. 1, pp. 374-382, Jan. 2019*.
- Jaehyoung Park, Jonghoon Kim, Yujun Shin, Bumjin Park, Won-Seok Kim, Seok-Jong Cheong, and Seunyoung Ahn. "Toroidal Shaped Coils for a Wireless Power Transfer System for Unmanned Aerial Vehicle". *JOURNAL OF ELECTROMAGNETIC ENGINEERING AND SCIENCE, vol. 19, no. 1, pp. 48-55, Jan. 2019*.
- Ki-Cheol Yoon, Seungyoung Ahn, and Jong-Chul Lee. "A Compact Low Phase Noise Oscillator Using Network and Complimentary MNZ Metamaterial Resonator". *Microwave and Optical Technique Letters, Jan. 2019. https://doi.org/10.1002/mop.31500*.
- Ki-Cheol Yoon, Seungyoung Ahn, and Jong-Chul Lee. "Elliptic Function Compact-size of the Band-pass Filter Using Complimentary MNZ metamaterial Resonator". *Microwave and Optical Technique Letters, Oct. 2018. https://doi.org/10.1002/mop.31406*.
- Ki Jin Han and Seungyoung Ahn. "Foreword: Special Section on Recent Progress in the Electrical Design of Advanced Package and Systems (Part 2)". *IEEE Transactions on Components Packaging and Manufacturing Technology, vol. 8, no. 4, pp. 509-510, Apr. 2018*.
- Ki-Cheol Yoon, Seungyoung Ahn, and Jong-Chul Lee. "Wide Band Compact Coplanar Waveguide with IDC Using Left-handed Metamaterial". *Microwave and Optical Technique Letters, vol.60, pp. 2030-2033, 2018. https://doi.org/10.1002/mop.31301*.
- Kibeom Kim, Jangyong Ahn, and Seungyoung Ahn. "Detection of the Interface Trap Charge Density and Lateral Nonuniformity of Through-Silicon Vias". *IEEE Microwave and Wireless Components Letters, vol. 28, no. 5, pp. 422-424, May. 2018*.
- Kibeom Kim, Jedok Kim, Hongkyun Kim, and Seungyoung Ahn. "Rigorous Mathematical Model of Through-Silicon Via (TSV) Capacitance". *IET Circuits, Devices & Systems, Article in IET Circuits Devices & Systems, https://doi.org/10.1049/iet-cds.2017.0157 Mar. 2018*.
- Hyun-Ho Park and Seungyoung Ahn. "Steerable Electromagnetic Transmission of Metal Gratings on a Magnetized Ferrite Slab". *IEEE Trans. on Magnetics, vol. 54, no. 3, Mar. 2018*.
- Chiuk Song, Hongseok Kim, Daniel H. Jung, Jonghoon J. Kim, Sunkyu Kong, Jiseong Kim, Seungyoung Ahn, Jonghoon Kim, and Joungho Kim. "EMI Reduction Methods in Wireless Power Transfer System for Drone Electrical Charger using Tightly-coupled Three-phase Resonant Magnetic Field". *IEEE Transactions on Industrial Electronics, vol. 65, no. 9, pp. 6839-6849, Jan. 2018*.
- Bumjin Park, Dongwook Kim, Jaehyoung Park, Kibeom Kim, Jay Koo, Hyun Ho Park, and Seungyoung Ahn. "Optimization design of toroidal core for magnetic energy harvesting near power line by considering saturation effect". *AIP Advances, vol. 8, 056728, Jan. 2018*.
- Dongwook Kim, Bumjin Park, Jaehyoung Park, Hyun Ho Park, and Seungyoung Ahn. "Magnetic field concentration using ferromagnetic material to propel a wireless power transfer based micro-robot". *AIP Advances 8, 056823, 2018*.
- Ki Jin Han and Seungyoung Ahn. "Foreword: Special Section on Recent Progress in the Electrical Design of Advanced Package and Systems". *IEEE Transactions on Components Packaging and Manufacturing Technology, vol. 8, no. 4, pp. 509-510, Jan. 2018*.
- Seungyoung Ahn. "2017 Asia-Pacific International Symposium on EMC (APEMC), Seoul, Korea". *IEEE Electromagnetic Compatibility Magazine, vol. 6, no. 3, pp. 98-103, Nov. 2017*.
- Karam Hwang, Dongwook, Kim, Dongsoo Har, Seungyoung Ahn. "Pickup Coil Counter for Detecting Presence of Trains Operated by Wireless Power Transfer". *IEEE Sensors, vol. 17, no. 22, pp. 7526-7532 Nov. 2017*.
- Jaeyong Cho, Byung-Sung Kim, Jonghyuck Jung, Joonsung Kim, Kibeom Kim, Karam Hwang, Hwiseob Lee, Seungil Jeung and Seungyoung Ahn. "A Two-line Time-domain Gating Method for Characterization of Test Fixture with Via-hole Discontinuity". *IEEE Microwave and Wireless Components Letters, Vol. No. 10, pp. 936-938, Oct. 2017*.
- Bumjin Park, Jaehyoung Park, Yujun Shin, Chanjun Park, Jonghyeon Jeong, Kyung Sub Lee, Seungyoung Ahn, and Il Song Han. "Wireless Charging System Using Soft Magnetic Composite for Unmanned Aerial Vehicle". *International Journal of Communications, vol. 2, Oct. 2017*.
- Dongwook Kim, Karam Hwang, Jaehyoung Park, Hyun Ho Park, and Seungyoung Ahn. "Miniaturization of Implantable Micro-robot Propulsion Using Wireless Power Transfer System". *Micromachines, vol. 8, no. 9, Sep. 2017*.
- Myunghoi Kim and Seungyoung Ahn. "A Compact and Multi-Stack Electromagnetic Bandgap Structure for Gigahertz Noise Suppression in Multilayer Printed Circuit Boards". *Applied Sciences, vol. 7, no. 8, 804, Aug. 2017*.
- Hyun Ho Park, Jong Hwa Kwon, and Seungyoung Ahn. "A Simple Equivalent Circuit Model for Shielding Analysis of Magnetic Sheets Based on Microstrip Line Measurement". *IEEE Transactions on Magnetics, vol. 53, no. 6, pp. 1-4, Jun. 2017*.
- Dongwook Kim, Karam Hwang, Jaehyoung Park, Hyun Ho Park, and Seungyoung Ahn. "High Efficiency Wireless Power and Force Transfer for a Micro-robot using a Multi-axis AC/DC Magnetic Coil". *IEEE Trans. on Magnetics, vol. 53, no. 6, Jun. 2017*.
- Karam Hwang, Jaeyong Cho, Dongwook Kim, Jaehyoung Park, Jong Hwa Kwon, Sang Il Kwak, Hyun Ho Park, Seungyoung Ahn. "Autonomous Coil Alignment System(ACAS) for the Dynamic Wireless Charging of Electric Vehicles to Minimize Lateral Misalignment". *Energies 2017, 10, 315*.
- Seung Beop Lee, Seungyoung Ahn, and In Gwun Jang. "Simulation-Based Feasibility Study on the Wireless Charging Railway System with a Ferriteless Primary Module". *IEEE Transactions on Vehicular Technology, Vol. 66, no. 2, pp. 1004-1010, Feb, 2017*.
- Jaehyoung Park, Dongwook Kim, Hyun Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "A Resonant Reactive Shielding for Planar Wireless Power Transfer System in Smart Phone Application". *IEEE Transactions on Electromagnetic Compatibility, vol. 59, no. 2, pp. 695-703, Jan. 2017*.
- Hyun Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Electromagnetic Shielding Analysis of Multiple Slits on a Metal Plate Coated with a Ferrite Sheet". *IEEE Transactions on Electromagnetic Compatibility, vol. 58, no. 5, pp. 1448-1455, Oct. 2016*.
- Chiuk Song, Hongseok Kim, Daniel H. Jung, Jonghoon J. Kim, Sunkyu Kong, Jiseong Kim, Seungyoung Ahn, Jonghoon Kim, and Joungho Kim. "Low EMF and EMI Design of Tightly-coupled Handheld Resonant Magnetic Field (HH-RMF) Charger for Automotive Battery Charging". *IEEE Transactions on Electromagnetic Compatibility, vol. 58, no. 4, pp. 1194-1209, Aug. 2016*.
- Kibeom Kim, Karam Hwang, and Seungyoung Ahn. "An Improved 100 GHz Equivalent Circuit Model of a Through Silicon Via with Substrate Current Loop". *IEEE Microwave and Wireless Components Letters, vol. 26, no. 6, pp. 425-427, Jun. 2016*.
- Suna Choi, Seungkeun Park, and Seungyoung Ahn. "Impact of Discovery Reference Signals in LTE Small Cell eNB on Audio Devices". *Electronics letters, 2pp, Mar. 2016*.
- Hongseok Kim, Chiuk Song, Daniel H. Jung, Dong-Hyun Kim, Jonghoon Kim, Seungyoung Ahn, and Joungho Kim. "Coil Design and Measurements of Automotive Magnetic Field Resonant Wireless Power Transfer System for High Efficiency and Low EMF/EMI". *IEEE Transactions on Microwave Theory and Techniques, vol. 64, no. 2, pp. 383-400, Feb. 2016*.
- Yeonje Cho, Jonghoon J. Kim, Dong-Hyun Kim, Seongsoo Lee, Hongseok Kim, Chiuk Song, Sunkyu Kong, Hyoungjun Kim, Seungyoung Ahn, and Joungho Kim. "Thin PCB-Type Metamaterials for Improved Efficiency and Reduced EMF Leakage in Wireless Power Transfer Systems". *IEEE Transactions on Microwave Theory and Techniques, vol. 64, no. 2, pp. 353-364, Feb. 2016*.
- Karam Hwang, Jaehyoung Park, Dongwook Kim, Hyun Ho Park, Jong Hwa Kwon, Sang Il Kwak, Seungyoung Ahn. "Autonomous Coil Alignment System Using Fuzzy Steering Control for Electric Vehicles with Dynamic Wireless Charging". *Mathematical Problems in Engineering, vol. 2015, Article ID 205285, 14 pages, 2015*.
- Park Jae-Hyoung, and Seung-Young Ahn.. "Leakage magnetic field reduction for wireless power transfer system using shielding coil for railway". *IJAR 3.4 (2015): 265-269*.
- Minho Kim, Hongseok Kim, Dongwook kim, Yongmin Jeong , Hyun-ho Park, Seungyoung Ahn. "A Three-Phase Wireless Power Transfer System for On-line Electric Vehicles with Reduction of Leakage Magnetic Fields". *IEEE Transactions on Microwave Theory and Techniques, Vol. 63, No. 11, Nov. 2015*.
- Hyun Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Effect of Air-Gap Between a Ferrite Plate and Metal Strips on Magnetic Shielding". *IEEE Transactions on Magnetics, Vol. 51, No. 11, Nov. 2015*.
- Dongwook Kim, Jaehyoung Park, Hyun Ho Park, and Seungyoung Ahn. "Generation of Magnetic Propulsion Force and Torque for Microrobot Using Wireless Power Transfer Coil". *IEEE Transactions on Magnetics, Vol. 51, No. 11, 8600104, Nov. 2015*.
- Karam Hwang, Jaehyoung Park, Dongwook Kim, Hyun Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Autonomous Steering using Coil Alignment System for Electric Vehicles with Dynamic Wireless Charging". *Mathematical Problems in Engineering, Vol. 2015, 205285, Sep. 2015*.
- Hyun-Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Magnetic Shielding Analysis of a Ferrite Plate with a Periodic Metal Strip". *IEEE Transactions on Magnetics, Vol. 51, No. 8, Article Number 7002408, Aug. 2015*.
- Sukjin Kim, Daniel Hyunsuk Jung, Jonghoon J. Kim, Bumhee Bae, Sunkyu Kong, Seungyoung Ahn, Jonghoon Kim, Joungho Kim. "High-Efficiency PCB- and Package-Level Wireless Power Transfer Interconnection Scheme Using Magnetic Field Resonance Coupling". *IEEE Transactions on Components Packaging and Manufacturing Technology, Vol. 5, No. 7, pp. 863-878, Jul. 2015*.
- Hyun-Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Magnetic Shielding Analysis of a Multiply-Slotted Metal Plate Coated with a Ferrite Sheet in a Periodic Line Current Source". *Journal of Magnetism and Magnetic Materials, Vol. 385, pp. 250-256, Jul. 2015*.
- Seung Beop Lee, Seungyoung Ahn, and In Gwun Jang. "Development of the Optimization Framework for Wireless Power Transfer Systems". *IEEE Transactions on Microwave Theory and Techniques, Vol. 63, No. 3, Apr. 2015*.
- Hwansoo Moon, Sungkyu Kim, Hyun Ho Park, and Seungyoung Ahn. "Design of a Resonant Reactive Shield with Double Coils and a Phase Shifter for Wireless Charging of Electric Vehicles". *IEEE Transactions on Magnetics, vol. 51, no. 3, Apr. 2015*.
- Hyun-Ho Park, Jong Hwa Kwon, Sang Il Kwak, and Seungyoung Ahn. "Analysis of Quasistatic Magnetic Field Penetration into Multiple Slits in a Conducting Plane Loaded with a Ferrite Sheet". *IEEE Transactions on Electromagnetic Compatibility, vol. 57, no. 2, Apr. 2015*.
- Joungho Kim and Seungyoung Ahn. "Guest Editorial: Mini-special Issue on 2014 IEEE Wireless Power Transfer Conference (WPTC 2014)". *IEEE Transactions on Microwave Theory and Techniques, vol. 63. No. 3. pp, 778-779, Mar. 2015*.
- Dongwook Kim, Minho Kim, Jesung Yoo, Hyun-Ho Park, and Seungyoung Ahn. "Magnetic Resonant Wireless Power Transfer for Propulsion of Implantable Micro-robot". *Journal of Applied Physics, 117(17), 17E712, Jan. 2015*.
- Tushar Batra, Erik Schaltz, and Seungyoung Ahn. "Effect of Ferrite Addition above the Base Ferrite on the Coupling Factor of Wireless Power Transfer for Vehicle Applications". *Journal of Applied Physics, 117(17), 17D517-1, Jan. 2015*.
- Jingook Kim, Jongjoo Lee, Seungyoung Ahn, and Jun Fan. "Closed-Form Expressions for the Noise Voltage caused by a Burst Train of IC Switching Currents on a Power Distribution Network". *IEEE Transactions on Electromagnetic Compatibility, vol. 10, no. 4, pp. 1585-1597, Dec. 2014*.
- Hyun Ho Park, Jong Hwa Kwon, and Seungyoung Ahn. "Magnetic Shielding Analysis of a Slit on a Conducting Plate Coated with a Ferrite Sheet: Transverse Incidence". *IEEE Transactions on Magnetics, Vol. 50, No. 9, Sep. 2014*.
- Seonghwan Kim, Hyun Ho Park, Jonghoon Kim, Jiseong Kim, and Seungyoung Ahn. "Design and Analysis of a Resonant Reactive Shield for a Wireless Power Electric Vehicle". *IEEE Transactions on Microwave Theory and Techniques, Vol. 62, No. 4, pp.1057-1066, Apr. 2014*.
- Myunghoi Kim, Kyoungchoul Koo, Yujeong Shim, Chulsoon Hwang, Jun So Pak, Seungyoung Ahn, and Joungho Kim. "Vertical Stepped Impedance EBG (VSI-EBG) Structure for Wideband Suppression of Simultaneous Switching Noise in Multilayer PCBs". *IEEE Transactions on Electromagnetic Compatibility, Vol. 55, No. 2, pp. 307-314, Apr. 2014*.
- Jaegue Shin, Seungyong Shin, Yangsu Kim, Seungyoung Ahn, Seokhwan Lee, Guho Jung, Boyune Song, Seongjeub Jeon, and Dong Ho Cho. "Design and Implementation of a Shaped Magnetic Resonance Based Wireless Power Transfer System for Roadway-Powered Moving Electric Vehicles". *IEEE Transactions on Industrial Electronics, Vol. 61, No. 3, pp. 1179-1192, Mar. 2014*.
- Seungyoung Ahn, Chulsoon Hwang, and Hyun Ho Park. "Optimized Shield Design for Reduction of EMF from Wireless Power Transfer Systems". *IEICE Electronics Express, Vol. 11, No. 2, pp. 1-9, Feb. 2014*.
- . "Yangbae Chun, Seongwook Park, Jonghoon Kim, Jiseong Kim, Hongseok Kim, Joungho Kim, Nam Kim, and Seungyoung Ahn, "Electromagnetic Compatibility of Resonance Coupling Wireless Power Transfer in On-Line Electric Vehicle System, IEICE Transactions on Communications, Vol. E97-B, No. 2, pp. 416-423, Feb. 2014". **.
- Minchul Shin, Myunghoi Kim, Jiseong Kim, Joungho Kim, and Seungyoung Ahn. "Small-size, Low-cost, Wideband, Continuous-time Linear Passive Equalizer with an Embedded Cavity Structure on a High-Speed Digital Channel". *IEEE Transactions on Advanced Packaging, Vol. 4, No. 1, pp. 94-99, Jan. 2014*.
- Jiseong Kim, Jonghoon Kim, Sunkyu Kong, Hongseok Kim, In-Soo Suh, Nam Pyo Suh, Dong-Ho Cho, Joungho Kim, and Seungyoung Ahn. "Coil Design and Shielding Methods for a Magnetic Resonant Wireless Power Transfer System". *Proceedings of the IEEE, Vol. 101, No. 6, pp. 1332-1342, Jun. 2013*.
- Seungyoung Ahn, Nam Pyo Suh, and Dong-Ho Cho. "Charging Up the Road". *IEEE Spectrum, pp. 48-54, Apr. 2013*.
- Yang-bae Chun, Ki-won Hwang, Nam Kim, and Seung-young Ahn. "Multi-Sectional Coil Design for Wireless Power Transfer". *International Journal of Advanced Railway, Vol. 1, No. 2, pp. 41-44, Oct. 2013*.
- Kiwon Hwang,Seonghwan Kim, Seongkyu Kim, Yangbae Chun, and Seungyoung Ahn. "Design of Wireless Power Transfer System for Railway Application". *IJAR 5.4 (2012): 167-174*.
- Seungyoung Ahn, Yangbae Chun, Dong-Ho Cho, and Joungho Kim. "Wireless Power Transfer Technology in On-Line Electric Vehicle". *Journal of Electromagnetic Engineering and Science, vol. 11, no. 3, pp. 174-182, Sep. 2011*.
- Jonghoon Kim, Hongseok Kim, In-Myoung Kim, Young-Il Kim, Seungyoung Ahn, Jiseong Kim, and Joungho Kim. "Reduction of Electromagnetic Field from Wireless Power Transfer Using a Series-Parallel Resonance Circuit Topology". *Journal of Electromagnetic Engineering and Science, vol. 11, no. 3, pp. 166-173, Sep. 2011*.
- Jeonghyeon Cho, Eakhwan Song, Heegon Kim, Seungyoung Ahn, Jun So Pak, Jiseong Kim, and Joungho Kim. "Mixed-mode ABCD Parameters: Theory and Application to Signal Integrity Analysis of PCB-level Differential Interconnects". *IEEE Transactions on Electromagnetic Compatibility, vol.53, no.3, pp. 814-822, Aug. 2011*.
- Hyun Ho Park and Seungyoung Ahn. "Mitigation of noise coupling on RF cable using electromagnetic bandgap structures". *Electronics Letters, Vol. 47, No. 15, pp. 849-850, Jul. 2011*.
- Jun So Park, Joohee Kim, Jonghyun Cho, Kiyeong Kim, Taigon Song, Seungyoung Ahn, Junho Lee, Hyungdong Lee, Kunwoo Park, and Joungho Kim. "PDN Impedance Modeling and Analysis of 3D TSV IC by Using Proposed P/G TSV Array Model Based on Separated P/G TSV and Chip-PDN Models". *IEEE Transactions on CPMT, vol. 1 no. 2, pp. 208-219, Feb. 2011*.
- Junho Lee, Seungyoung Ahn, Woon-Seong Kwon, Kyung-Wook Paik, and Joungho Kim. "Microwave Frequency Model of FPBGA Solder Ball Extracted from S-Parameter Measurement". *Transactions on IEICE, Vol. E87-C, No. 9, September 2004*.
- Seungyoung Ahn, Junho Lee, Junwoo Lee, Jonghoon Kim, Woonghwan Ryu, Young-Soo Kim, Byung-Hun Kum, Hyun-Seok Choi, Chong K. Yoon, and Joungho Kim. "Over GHz Electrical Circuit Model of a High-Density Multiple Line Grid Array (MLGA) Package". *IEEE Transactions On Advanced Packaging, Volume 26, Issue 1, February 2003, pp. 90-98*.
- Woonghwan Ryu, Myung-Jin Yim, Seungyoung Ahn, Junho Lee, Woopoung Kim, Kyung-Wook Paik, and Joungho Kim. "High-Frequency SPICE Model of Anisotropic Conductive Film Flip-Chip Interconnections Based on a Genetic Algorithm". *IEEE Transaction on Components and Packaging Technologies, Vol. 23, Issue.3, pp. 542-545, Sep. 2000*.
- Woonghwan Ryu, Junwoo Lee, Hyungsoo Kim, Seungyoung Ahn, Namhoon Kim, Baekkyu Choi, Donggun Kam, and Joungho Kim. "RF Interconnect for Multi-Gbit/sec Board-Level Clocck Distribution". *IEEE Transactions on Advanced Packaging, Vol. 23, Issue. 3, pp. 398-407, Aug. 2000*.
- Myung Jin Yim, Woonghwan Ryu, Young-Doo Jeon, Junho Lee, Seungyoung Ahn, Joungho Kim, and Kyung-Wook Paik. "Microwave Model of ACF Flip-Chip Interconnections for High-Frequency Application". *IEEE Transactions on CPT, Vol. 22, Issue 4, pp.575-581, Dec. 1999*.

## 특허 (2021년 이후 출원)

랩 특허 목록에서 2021년 이후 출원한 20건이다. 상태는 랩 표기다.[^patents]

- WIRELESS POWER TRANSMISSION APPARATUS, WIRELESS POWER RECEPTION APPARATUS, AND WIRELESS POWER TRANSMISSION SYSTEM USING AUXILIARY COIL (발명자 안승영, 김제독, 안장용; 국가 US; 출원번호 10/313,432; 출원일 2023.05.08; 상태 등록)
- 멀티 드롭에 의한 심볼간 간섭 및 크로스톡 감소 효과를 위한 고대역폭 메모리용 실리콘 관통 비아의 패시브 이퀄라이저를 포함하는 메모리 모듈 (발명자 안승영, 김현웅, 류승훈, 박종철; 국가 KR; 출원번호 10-2023-0188193; 출원일 2023.12.21; 등록번호 10-2928693; 등록일 2026.02.12; 상태 등록)
- 패드 및 비아-홀 디임베딩 기법이 적용된 임피던스 측정장치 (발명자 안승영, 이상욱, 안장용, 김현웅, 김홍석; 국가 KR; 출원번호 10-2023-0182765; 출원일 2023.12.15; 등록번호 10-2911631; 등록일 2026.01.08; 상태 등록)
- 반도체 장치 (발명자 안승영, 김현웅, 이성희, 송경환, 박동렬, 박종철; 국가 KR; 출원번호 10-2022-0128010; 출원일 2022.10.06; 등록번호 10-2781360; 등록일 2025.03.18; 상태 등록)
- WIRELESS POWER TRANSMISSION SYSTEM (발명자 안승영, 이창민, 우성호, 신유준, 이재원, 박동렬, 이범선; 국가 US; 출원번호 18/411178; 출원일 2024.01.12; 등록번호 12362602; 등록일 2025.07.15; 상태 등록)
- 반도체 소자의 기생 커패시턴스를 측정하는 시스템 및 방법 (발명자 안승영, 이재원, 이상욱, 김지성, 김홍석; 국가 KR; 출원번호 10-2024006817; 출원일 2024.05.24; 등록번호 10-2843842; 등록일 2025.08.04; 상태 등록)
- 전력선 전류의 크기에 따라 2차 측 권선수를 조정하는 에너지 하베스팅 시스템, 및 이의 구동 방법 (발명자 안승영, 이범선, 박범진, 허성렬, 신유준, 우성호, 박동렬; 국가 KR; 출원번호 10-20240112567; 출원일 2023.01.12; 등록번호 10-2814280; 등록일 2025.05.26; 상태 등록)
- UUV의 수중 충전/통신 시스템 및 방법 (발명자 은희현, 최석민, 곽규민, 이철, 안승영, 신유준, 우성호; 국가 KR; 출원번호 10-20220001518; 출원일 2022.01.05; 등록번호 10-2752676; 등록일 2025.01.06; 상태 등록)
- 금속 이물질 감지가 가능한 송신코일, 금속 이물질 감지시스템 및 금속 이물질 감지방법 (발명자 조요한, 박일호, 안승영, 우성호, 허성렬, 이현수; 국가 KR; 출원번호 10-20240020838; 출원일 2024.02.14; 등록번호 10-2743175; 등록일 2024.12.11; 상태 등록)
- 무선 전력 전송 시스템의 결합 계수 추출 방법 및 그를 위한 장치 (발명자 권병기, 은희현, 곽규민, 안승영, 신유준, 우성호, 이창민; 국가 KR; 출원번호 10-20230012953; 출원일 2023.01.31; 등록번호 10-2731604; 등록일 2024.11.13; 상태 등록)
- 이중모드 멀티코일 무선전력전송 시스템 (발명자 안승영, 최세민, 허성렬, 김해림, 우성호; 국가 KR; 출원번호 10-20220172961; 출원일 2022.12.12; 등록번호 10-2730654; 등록일 2024.11.12; 상태 등록)
- 무선 전력 전송 시스템 (발명자 안승영, 이범선, 신유준, 우성호, 이창민, 이재원, 손석현, 박범진; 국가 KR; 출원번호 10-20210180100; 출원일 2021.12.15; 등록번호 10-2730197; 등록일 2024.11.11; 상태 등록)
- 무선전력 전송을 이용한 마이크로 로봇 추진 시스템 (발명자 안승영, 이재원, 안장용, 박동렬, 김동욱; 국가 KR; 출원번호 10-20220005216; 출원일 2022.01.13; 등록번호 10-2716161; 등록일 2024.10.07; 상태 등록)
- 자성체 포화현상을 이용하여 누설 자기장의 고조파 성분을 상쇄하는 무선 전력 전송 시스템, 및 그 동작 방법 (발명자 안승영, 이범선, 박범진, 허성렬, 신유준, 우성호, 손석현, 이상욱, 김해림, 박동렬; 국가 KR; 출원번호 10-20210179207; 출원일 2021.12.14; 등록번호 10-2657215; 등록일 2024.04.09; 상태 등록)
- 무선전력전송 시스템의 송수신코일 간 결합계수 산출 장치 및 방법 (발명자 은희현, 최석민, 곽규민, 이철, 안승영, 신유준, 우성호, 손석현, 이창민; 국가 KR; 출원번호 10-20220001569; 출원일 2022.01.05; 등록번호 10-2651047; 등록일 2024.03.20; 상태 등록)
- Wireless power transfer system for selectively driving at least one transmitting coil among transmitting coils and operation method thereof (발명자 안승영, 이범선, 김종욱, 박범진, 박동렬, 허성렬; 국가 US; 출원번호 17643919; 출원일 2021.12.13; 등록번호 11750039; 등록일 2023.09.05; 상태 등록)
- Radio frequency weak magnetic field detection sensor and method of manufacturing the same (발명자 김장열, 조인귀, 이현준, 김성원, 김성민, 문정익, 박우천, 윤제훈, 이재우, 이호진, 장동원, 김기범, 안승영; 국가 US; 출원번호 17189788; 출원일 2021.03.02; 등록번호 11699549; 등록일 2023.07.11; 상태 등록)
- 더미 구조물을 포함하는 반도체 장치 및 그 제조 방법 (발명자 안승영, 김현웅, 이성희, 박종철, 박주성, 김민창, 송경환; 국가 KR; 출원번호 10-20210139684; 출원일 2021.10.19; 등록번호 10-2558916호; 등록일 2023.07.19; 상태 등록)
- 커패시티브 커플링에 기반하는 비접촉 통신 시스템 (발명자 안승영, 류승훈, 김지성, 이범선, 안장용, 김해림, 박동렬; 국가 KR; 출원번호 10-20210177992; 출원일 2021.12.13; 등록번호 10-2558913호; 등록일 2023.07.19; 상태 등록)
- 디지털 신호의 잡음 통신 방법 및 시스템 (발명자 안승영, 최준성, 박동렬, 김수일; 국가 KR; 출원번호 10-2022-0005933; 출원일 2022.01.14; 등록번호 10-2411498호; 등록일 2022.06.16; 상태 등록)

## 연구 과제 (진행 중)

랩 과제 페이지에 게시된 진행 과제다.[^projects]

- 다중 코일 기반 충전 영역 조절 기술을 적용한 이동형 로봇용 고성능·고호환성 무선충전 스테이션 사업화 (지원 중소기업벤처부; 기간 2026-04-01~2027-03-31)
- 누설 전자파 저감형 공동기 기반 송수신기 이격 대응 무선전력전송기술 개발 (지원 정보통신기획평가원 (IITP); 기간 2026-04-01~2030-12-31)
- Next Gen. Memory Module 개발을 위한 효율적인 SI/PI 검증 방법론 연구 (지원 SK 하이닉스; 기간 2026.01.01~2028.12.31)
- 1kW급 HPC향 SoC 구현시 multi-power domain간 power noise coupling 최소화를 위한 system-level PI 분석 방법론 및 설계 가이드 개발 (지원 삼성전자; 기간 2025.07.01~2028.06.30)
- 산업수요연계 칩렛 패키지용 ML 기반 설계 최적화, 고밀도 배선 공정 및 신호 무결성 검증 솔루션 개발 (지원 한국산업기술기획평가원 (KEIT); 기간 2025.04.01~2028.12.31)
- AI 기반 주파수 간섭 분석 및 전파 예측 기술 개발 (지원 정보통신기획평가원 (IITP); 기간 2025-04-01~2029-12-31)
- 2.xD 첨단 패키지용 폴리머 인터포저 소재 및 공정 핵심기술 개발 (지원 LG 이노텍; 기간 2024.04.01~2028.12.31)
- 22kW급 전기차 무선전력전송 경량 소재 및 전자파 저감 기술 개발 (지원 정보통신기획평가원 (IITP); 기간 2024.04.08~2027.12.31)
- 드로그를 이용한 무인잠수정 진회수 도킹 시스템 개발 (지원 국방과학연구소(ADD); 기간 2022.11.01~2027.10.31)
- 인공지능 기반 기지국 전자파 인체노출량 예측 알고리즘 개발 (지원 정보통신기획평가원(IITP); 기간 2022.04.01~2026.12.31)
- 초연결 E-Vehicle 전력 및 신호 EMC 고도화 기술 개발 (지원 정보통신기획평가원(IITP); 기간 2020.04.01~2027.12.31)

## 수상과 소식

랩 소식 게시판의 최근 항목이다.[^news]

- 2026-10-06 · 최강민 박사과정 조천식모빌리티대학원 공로상 수상
- 2026-09-03 · 황가람 박사, 세계적인 반도체 학회 '핫칩스 2026'에서 삼성전자 대표로 LPDDR5X-PIM 세부 사양 발표
- 2026-08-24 · 박준혁 석사과정, IEEE EMC-S Daejeon-Seoul Joint Chapter Chair Award 수상
- 2026-07-27 · 김현우 박사과정, 2026년도 EMC 장학금 수상
- 2026-07-27 · 이상욱 박사과정, 2026년도 EMC 장학금 수상
- 2026-07-21 · 안승영 교수님, 국토교통부장관 표창장 수상
- 2026-06-18 · 정필후 석사과정, 최우수학생연구상 수상
- 2026-05-13 · 안승영 교수님, KAIST 연구비 기관흡수액 준우수 기여상 수상
- 2026-04-08 · 김해림 박사 (공동 1저자), 이재원 박사(공동저자), 안승영 교수님(공동 교신저자), Nature Communications 논문 출판
- 2026-04-03 · 이상욱 박사과정, 최우수 학생연구상 수상
- 2026-03-17 · 전유빈 석사과정, 대학생 창의설계 경진대회 우수 논문상 수상
- 2026-03-03 · 이현수 박사과정, IEEE EMC-S Daejeon-Seoul Joint Chapter Chair Award 수상
- 2026-02-19 · 이재원 박사, 박사학위 최우수 논문상 수상
- 2026-01-05 · 전유빈 석사과정, 국가우수(이공계)장학생 선발
- 2025-11-11 · 김현우 박사과정, 2025 IEEE Workshop on Advanced Interconnects (WAI), Best Paper Award 수상
- 2025-10-26 · 허성렬 박사, 무선충전 모빌리티 솔루션 기업 '코일즈' 설립 및 기술 상용화 본격화
- 2025-09-19 · 이현수 박사과정 조천식모빌리티대학원 공로상 수상
- 2025-09-19 · 이재원 연구교수 조천식모빌리티대학원 최우수 학생연구상 수상
- 2025-07-13 · 이재원 박사과정, 2025년도 EMC 장학금 수상
- 2025-05-23 · 이현수 박사과정, EVTeC 2025 Young Investigators Award 수상

## 연락과 위치

- 이메일: sahn@kaist.ac.kr[^prof]
- 전화: 042-350-1263[^prof]
- 위치: KAIST 문지캠퍼스 Faculty Wing 3층 316호 (대전 유성구 문지로 193)[^prof]

[^research]: 랩 연구 개요 페이지 <https://emc.kaist.ac.kr/index.php?mid=research_01> (2026-10-19 열람)
[^emc]: 랩 연구 페이지(Electromagnetic Compatibility) <https://emc.kaist.ac.kr/index.php?mid=research_02> (2026-10-19 열람)
[^sipi]: 랩 연구 페이지(Signal and Power Integrity) <https://emc.kaist.ac.kr/index.php?mid=research_03> (2026-10-19 열람)
[^wpt]: 랩 연구 페이지(Wireless Power Transfer) <https://emc.kaist.ac.kr/index.php?mid=research_04> (2026-10-19 열람)
[^prof]: 랩 교수 페이지 <https://emc.kaist.ac.kr/index.php?mid=Professor> (2026-10-19 열람)
[^members]: 랩 구성원 페이지 <https://emc.kaist.ac.kr/index.php?mid=member_01> (연구원), member_02(박사과정), member_03(석사과정), member_05(직원) (2026-10-19 열람)
[^alumni]: 랩 졸업생 페이지 <https://emc.kaist.ac.kr/index.php?mid=member_04> (2026-10-19 열람)
[^papers]: 랩 국제 학술지 목록 <https://emc.kaist.ac.kr/index.php?mid=publication_01> (2026-10-19 열람)
[^patents]: 랩 특허 목록 <https://emc.kaist.ac.kr/index.php?mid=publication_03> (2026-10-19 열람)
[^projects]: 랩 진행 과제 페이지 <https://emc.kaist.ac.kr/index.php?mid=project_01> (2026-10-19 열람)
[^news]: 랩 소식 게시판 <https://emc.kaist.ac.kr/index.php?mid=news> (2026-10-19 열람)
[^p1]: C. Lee 외, S. Ahn, IEEE Transactions on Power Electronics (2026, 조기 공개). <https://doi.org/10.1109/tpel.2026.3661024> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Lee 외, S. Ahn, IEEE Transactions on Electromagnetic Compatibility 68, 246-258 (2026). <https://doi.org/10.1109/temc.2025.3632869> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Woo 외, S. Ahn, IEEE Journal of Emerging and Selected Topics in Power Electronics 13, 4358-4368 (2025). <https://doi.org/10.1109/jestpe.2025.3540010> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Ahn 외, S. Ahn, IEEE Transactions on Biomedical Circuits and Systems 16, 1166-1180 (2022). <https://doi.org/10.1109/tbcas.2022.3222011> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. H. Kim 외, D. H. Kim, Nature Communications 17, 3800 (온라인 2026-03-11). <https://doi.org/10.1038/s41467-026-70331-4> 초록 기준.
[^p6]: S. Ryu 외, S. Ahn, IEEE Transactions on Signal and Power Integrity 5, 154-170 (2026). <https://doi.org/10.1109/tsipi.2026.3714430> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Ryu 외, S. Ahn, IEEE Transactions on Components, Packaging and Manufacturing Technology 14, 1943-1958 (2024). <https://doi.org/10.1109/tcpmt.2024.3487577> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Kim 외, S. Ahn, IEEE Transactions on Components, Packaging and Manufacturing Technology 13, 700-714 (2023). <https://doi.org/10.1109/tcpmt.2023.3276862> 초록 기준(Semantic Scholar 등록 초록).

# 권경하 연구그룹 (Kwon Research Group)

**KAIST 전기및전자공학부 · 권경하 교수**

- 분야: 전기차 배터리 관리 반도체(BMS IC)와 임피던스 측정 회로, 고속 직렬 통신 송수신 회로(메모리·칩렛 인터페이스, 광통신), 피부 부착형·이식형 무선 생체 센서
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^prof][^p1][^p4], 배터리 관리 시스템[^bms][^p1][^p2], 착용형 생체 센서[^health][^p6][^p7], 에너지 하베스팅[^p8][^p7], 이식형·생체 전자 기기[^health], 광통신[^serdes], 고속 유선 인터페이스[^serdes][^p4][^p5]
- 홈페이지: <https://krg.kaist.ac.kr/>
- 근거와 출처: [권경하 연구그룹 근거 페이지](kwon-group-sources.md)

> 아날로그와 디지털이 섞인 반도체 회로를 설계해, 전기차 배터리 상태를 정밀하게 재는 칩, 인공지능 반도체의 메모리를 빠르게 잇는 통신 칩, 피부에 붙이거나 몸에 넣는 무선 건강 측정 장치를 만드는 연구실이다.[^prof][^home]

## 무엇을 연구하나

교수 소개는 연구실이 혼성 아날로그·디지털 회로와 특정 용도용 집적회로(ASIC)를 설계하며, 디지털 의료·헬스케어와 더 믿을 만하고 빠른 통신 서비스를 만들어 왔다고 적는다.[^prof] 첫 화면은 연구 분야로 회로·시스템 설계, 배터리 관리 IC, 고속 직렬 링크(SerDes), 디지털 헬스케어, 바이오메디컬 시스템, AI를 든다.[^home]

첫 번째 갈래는 **배터리 관리 IC**다. 전기차·에너지 저장 장치의 배터리 관리 시스템(BMS)에 들어가는 칩으로, 직렬로 이어진 수많은 배터리 셀의 전압을 정밀하게 재는 배터리 모니터링 IC(BMIC), 배터리 내부 상태를 주파수별 저항(임피던스)으로 진단하는 EIS 회로, 전원 관리 IC(PMIC)를 설계한다.[^bms] 연구실 설명에 따르면 충전 상태를 1% 오차 안으로 추정하려면 셀 전압을 1 mV 안으로 재야 하는데, 연구실이 2023년 국제고체회로학회(ISSCC)에서 발표한 2 mV가 당시 세계 최고 성능이라고 밝힌다.[^bms] 자동차 기능 안전 최고 등급(ASIL-D)과 차량용 부품 온도 규격(AEC-Q100)을 맞추는 설계가 특징이다.[^p1][^p3]

두 번째 갈래는 **고속 직렬 통신 회로**(데이터를 한 줄로 차례차례 빠르게 보내는 통신)다. 생성형 AI는 거대 모델을 메모리에서 읽고 쓰는 일이 병목이라, 고대역폭 메모리(HBM), 칩렛(여러 칩을 한 패키지에 잇는 방식), 메모리 내 연산(PIM)을 잇는 고속 인터페이스가 중요해졌다. 연구실은 메모리 핀 사이 간섭 보상, 저전력 칩렛용 신호 방식(한 번에 네 단계 전압으로 2비트를 보내는 PAM-4, 세 단계 전압을 쓰는 듀오바이너리), 전원 잡음 억제 기술과, 데이터센터 광통신의 신호 왜곡을 전자적으로 보정하는 기술(EDC)을 연구한다.[^serdes][^p4][^p5]

세 번째 갈래는 **디지털 헬스케어**다. 딱딱한 회로 기판 대신 피부 굴곡에 맞는 유연한 저전력 전자 장치와 블루투스 저전력 통신, 무선 전력 전송으로, 땀·심장·상처 회복·호흡 같은 생체 지표를 실시간으로 재는 피부 부착형·이식형 장치를 만든다.[^health] 피부 아래 혈관 깊이까지 함께 재는 혈류 측정 패치,[^p6] 빛으로 전력을 얻어 배터리 부담을 줄이는 착용형 센서 플랫폼,[^p7] 배관의 미세 진동으로 스스로 전기를 만들어 실내 이산화탄소를 재는 장치가 예다.[^p8]

## 주요 연구 주제

### 1. 전기차 배터리 관리 반도체

배터리 전압 측정 IC, 임피던스 측정(EIS), 자동차용 발진기.[^p1][^p2][^p3][^bms] 대표 논문 1, 2, 3.

### 2. 메모리·칩렛용 고속 인터페이스

PAM-4 송수신기, 온칩 링크.[^p4][^p5][^serdes] 대표 논문 4, 5.

### 3. 무선 생체 센서와 에너지 수확

혈류 측정, 빛 에너지 수확 센서, 진동 발전 이산화탄소 모니터.[^p6][^p7][^p8][^health] 대표 논문 6, 7, 8.

## 대표 논문

랩 논문 목록의 2023–2026년 국제 학술지·학술대회 논문 가운데 교수가 교신저자(†)인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2023 | [ASIL-D Compliant Battery Monitoring IC with High Measurement Accuracy and Robust Communication](https://doi.org/10.1109/isscc42615.2023.10067607) · IEEE ISSCC 2023 | 전기차는 수많은 리튬이온 셀로 수백 볼트 배터리 팩을 만들고, 각 셀의 충전·건강 상태를 추정하려면 셀 전압과 온도를 정밀하게 재야 한다. 자동차 기능 안전 최고 등급(ASIL-D)을 만족하면서 측정 정확도와 통신 견고성을 높인 배터리 모니터링 IC를 발표했다.[^p1] | 1저자 Jong-Kyoung Lee, 교신 권경하 |
| 2 | 2025 | [Small-Perturbation Electrochemical Impedance Spectroscopy System With High Accuracy for High-Capacity Batteries in Electric Vehicles](https://doi.org/10.1109/tie.2024.3436676) · IEEE Transactions on Industrial Electronics | 대용량 전기차 배터리의 임피던스를 작은 전류만 흘려 정확하게 재는 측정 시스템. 필터 구성을 맞춰 측정 시간을 줄였고, 70 Ah 배터리에서 오차를 마이크로옴 수준으로 낮췄다.[^p2] | 1저자 Young-Nam Lee, 교신 권경하 |
| 3 | 2026 | [Digitally Self-Calibrated RC Oscillator Utilizing Farey Search Algorithm Under ASIL-D Conditions Within AEC-Q100 Grade 0 Temperature Range](https://doi.org/10.1109/tcsi.2025.3604256) · IEEE Transactions on Circuits and Systems I | 자동차 칩의 기준 신호를 만드는 RC 발진기(저항과 축전기로 일정한 주기의 신호를 만드는 회로)를 사람이 일일이 보정하지 않아도 되도록, 패리 수열 탐색 알고리즘으로 스스로 보정하게 했다. 180 nm 공정 시제품이 영하 40도에서 영상 150도까지 오차 0.56% 안에 들었다.[^p3] | 1저자 Jeongwon Han, 교신 권경하 |
| 4 | 2026 | [A 32-Gb/s 0.89-pJ/b Ground-Referenced PAM-4/NRZ Transceiver with Unidirectional Current Summation and Double Sampling](https://doi.org/10.1109/cicc65509.2026.11509464) · IEEE CICC 2026 | 짧은 거리 칩 간 연결용 단일 선 송수신기로, 접지 기준 신호 방식(GRS)에서 네 단계 신호(PAM-4)를 처음 구현해 실험으로 검증했다. 28 nm 공정에서 초당 32 Gb를 비트당 0.89 pJ로 보냈다.[^p4] | 공동 1저자 Wonbin Lee·Jae-Seung Jeong, 교신 권경하 |
| 5 | 2025 | [A 23.5-fJ/b/dB 15.2-Gb/s/pin Switched-Capacitor-Driven On-Chip Link with Half-VDD DC Biasing and ISI Mitigation](https://doi.org/10.1109/esserc66193.2025.11214071) · IEEE ESSERC 2025 | 칩 안의 긴 배선(6 mm)으로 신호를 보내는 축전기 구동 인터페이스(축전기에 모은 전하로 선을 구동하는 송신 회로). 축전기 두 개를 번갈아 충전·공유해 작은 용량으로도 신호 크기를 유지하고 대역폭을 높여, 초당 15.2 Gb를 보냈다.[^p5] | 1저자 Wonbin Lee, 교신 권경하 |
| 6 | 2026 | [Deep learning–integrated multilayer thermal gradient sensing platform for real-time blood flow monitoring](https://doi.org/10.1126/sciadv.aea8902) · Science Advances | 높이가 다른 층에 온도 센서를 배치한 부드러운 무선 패치로 피부 위 온도 기울기를 재고, 딥러닝으로 혈류 속도와 혈관 깊이를 함께 실시간 추정했다. 광혈류 측정과 결합해 연속 혈압 측정 정확도도 높였다.[^p6] | 1저자 Youngmin Sim, 마지막·교신 권경하 |
| 7 | 2025 | [Adaptive electronics for photovoltaic, photoluminescent and photometric methods in power harvesting for wireless wearable sensors](https://doi.org/10.1038/s41467-025-60911-1) · Nature Communications | 빛을 쓰는 착용형 센서의 배터리 부담을 줄이려고, 주변 빛을 측정에 직접 쓰는 방법, 다중 접합 태양전지, 빛을 받아 발광하는 포장재를 함께 쓰는 적응형 전자 플랫폼을 만들었다. 센서 안 계산으로 무선 전송량도 줄였다.[^p7] | 공동 1저자 Chanho Park 등, 공동 교신 권경하·John A. Rogers 등 |
| 8 | 2025 | [Highly compact inertia-driven triboelectric nanogenerator for self-powered wireless CO2 monitoring via fine-vibration harvesting](https://doi.org/10.1016/j.nanoen.2025.110872) · Nano Energy | 건물 배관의 미세한 진동을 공진 구조와 여러 겹 마찰 전기 발전기로 키워 전기를 만들고(13 Hz에서 0.5 mW), 블루투스 저전력 칩으로 실내 이산화탄소 농도를 배터리 없이 주기적으로 보내는 장치.[^p8] | 공동 1저자 Daniel Manaye Tiruneh·Gyurim Jang, 공동 교신 권경하·Hanjun Ryu |

## 교수와 전문 분야

권경하 교수는 KAIST 전기전자공학 학사(2011, 최우등(Summa Cum Laude) 졸업), 석사(2013), 박사(2018)를 받고 미국 노스웨스턴대 생체통합전자센터 박사후연구원(2018–2020)을 거쳤다. 지금은 KAIST 전기및전자공학부 부교수이며 반도체시스템공학과와 AI반도체대학원 겸임교수다.[^prof] 국제고체회로학회(ISSCC) 기술 프로그램 위원회에서 한국 대표(2024)와 아시아·태평양 부간사(2025)를 맡았고, KAIST 임팩트 연구상(2025), KAIST 10대 연구성과상(2025), IDEC 우수 신진연구자상(2022) 등을 받았다.[^prof]

논문으로 보면 전문 분야는 세 갈래다.

- **자동차용 고정밀 아날로그·혼성 회로**: 배터리 측정, 임피던스, 자가 보정 발진기.[^p1][^p2][^p3]
- **고속 유선 송수신 회로**: PAM-4, 온칩 링크.[^p4][^p5]
- **무선 생체 전자 시스템**: 혈류·환경 센서, 에너지 수확.[^p6][^p7][^p8]

## 응용 분야

대표 논문과 연구 설명으로 보면 전기차·에너지 저장 장치 배터리 안전 진단, AI 반도체와 데이터센터 인터커넥트, 원격 건강 관리, 건물 환경 감시에 닿아 있다.[^bms][^serdes][^p6][^p8]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다. 연구실 대표(Lab Representative)는 석박사통합과정 Uikyoung Lee와 석사과정 Changhyoung Lee다.[^graduate] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Wonbin Lee | 박사과정 | On-Chip Link; Advanced Modulation Schemes; Chiplet Interface | 4, 5 |
| Jaeseung Jeong | 박사과정 | Memory Interface | 4, 5 |
| Byeongho Hwang | 박사과정 | Integrated Solution IC for BMS |  |
| Suhwan Kim | 박사과정 | Wireless Cardiac Monitoring System; WPT System for Biomedical Applications |  |
| Sara Kim | 박사과정 | EDC for Optical Communication | 5 |
| Namhoon Kim | 박사과정 | SI/PI in Memory Interface | 4 |
| Jeongwon Han | 박사과정 | High-Voltage Analog Front Ends for BMS | 3 |
| Doyun Park | 박사과정 | Wireless Capnograph System; Embedded System for Biomedical Applications | 7 |
| Jung Hoo Kim | 박사과정 | Power Management IC |  |
| Yoojin Kang | 박사과정 | Wireless Biomedical System Design |  |
| Gyu Rim Jang | 박사과정 | Wireless Multi-Modal Health Monitoring System | 8 |
| Hyunmin Shin | 박사과정 | EDC for Optical Communication | 4 |
| In-Woo Jang | 박사과정 | HBM Interface | 4, 5 |
| Young Min Sim | 석박사통합과정 | Wireless, Skin-Interfaced Biosensors and Electronics; Blood Flow Monitoring System | 6, 7 |
| Uikyoung Lee | 석박사통합과정 | State of Charge (SoC) Estimation |  |
| Ian Kim | 석박사통합과정 | High Precision ADC for Battery Estimation |  |
| Yusun Cheong | 석사과정 | Biomedical System |  |
| Heesang Kim | 석사과정 | SI/PI in Memory Interface |  |
| Changhyoung Lee | 석사과정 | Wireless real-time health monitoring systems; Flexible bio-sensors for biomarker extraction |  |
| Bokyung Lee | 석사과정 | D2D Interface |  |
| Yoonjung Lee | 석사과정 | Low-Dropout Regulator |  |
| Burmgie Sone | 석사과정 | Memory Interface |  |
| Yosep Park | 석사과정 | Wireless biosensors; On-device AI sensors | 6 |
| Wonyeong Choi | 석사과정 | Power Management IC |  |
| Bobyung Kim | 석사과정 | Battery Management IC |  |
| Jisoo Kim | 석사과정 | Battery Cell Balancing, Power Management IC |  |
| Minsang Yu | 석사과정 | Memory Interface |  |
| Sungbin Yun | 석사과정 | Memory Interface |  |

## 졸업생

랩 졸업생 페이지는 이름과 연구 분야만 적고 진로는 적지 않는다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jong-Kyoung Lee | Ph.D. (연구 분야 Battery Management IC) |  |
| Nanum Sung | M.S. (연구 분야 High-Speed Serial Links) |  |
| Yunchae Lee | M.S. (연구 분야 Electrochemical Impedance Spectroscopy (EIS) IC) |  |
| Chulyoon Jung | M.S. (연구 분야 Power Management IC (PMIC)) |  |
| Jihan Shin | M.S. (연구 분야 Battery Cell Balancing) |  |
| Ayoung Jin | M.S. (연구 분야 D2D Interface) |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021–2026년 국제 학술지·국제 학술대회 논문 43편과 게재가 승인된 논문 1편이다. 저자를 줄여 적은 항목은 랩 표기 그대로 옮겼다.[^papers]

**2026**

- J. Han, K.-S. Oh, D. Kim, W.-J. Choi, S. Han, K. Park, J. Choi, J. Lee, J.-Y. Jeon, Y.-S. Son, S.-G. Lee, K. Kwon†. "A 24-Channel Synchronous Battery Monitoring IC With Bipolar-Sampling ADCs and Calibration Engines for Sub-1-mV Accuracy". *IEEE Journal of Solid-State Circuits (Early Access)*.
- Y.-N. Lee, G. Rahim, S.-W. Jo, J. Han, W. Jeong, Y.-S. Jang, Y.-S. Son, K. Kwon, S.-G. Lee, K.-S. Choi. "Fast and Accurate Lithium-ion Battery Impedance Measurement Using Multi-rate Quadrature Demodulation with Band-pass Filtering". *IEEE Transactions on Instrumentation and Measurement, Apr. 10, 2026*.
- Y. Sim, Y. Park, K. Kwon†. "Deep learning-integrated multilayer thermal gradient sensing platform for real-time blood flow monitoring". *Science Advances, Feb. 6, 2026*.
- N. Kim, H. Kim, W. Lee, J. Kim, S. Kim, J.-S Jeong  and K. Kwon†. "A 26 Gb/s/pin Single-Ended Transceiver With Adaptive Switched-Capacitor-Based Simultaneous Switching Noise Compensation". *IEEE International Symposium on Circuits and Systems (ISCAS), May 2026*.
- W. Lee\*, J.-S. Jeong\*, H. Shin, I.-W. Jang, N. Kim and K. Kwon†. "A 32-Gb/s 0.89-pJ/b Ground-Referenced PAM-4/NRZ Transceiver with Unidirectional Current Summation and Double Sampling". *IEEE Custom Integrated Circuits Conference (CICC), April 2026*.
- J. Han, S. Woo, K-S. Oh, D. Kim, Y. Ko, W-J. Choi, S. Han, K. Park,  J. Choi, J. Lee, J-Y. Jeon, Y-S. Son, S-G. Lee,  K. Kwon†. "Sub-1mV-Accuracy, 24-CH Synchronous Battery Monitoring IC with Bipolar-Sampling ADCs and Calibration Engines". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2026 (Selected as Session Highlight)*.

**2025**

- S. Yoo, Z. Lv, N. Fadell, J.-Y. Yoo, S. Oh, K.-H. Ha, W. M. Moritz, J. Cha, H. Wu, J. Park, S. S. Kwak, K. Kwon, Y. Park, D. Cho, H.-Y. Ahn, C. Park, S. Kim, T. W. Park, W.-y. Maeng, H. C. Ko, A. M. Westman, M. MacEwan, Y. Huang, J. Saks, J. A. Rogers†. "A wireless, skin-integrated, continuous pressure distribution monitoring system to prevent ulcers across various healthcare environments". *nature partner journal (npj) Flexible Electronics, Dec. 2025*.
- J. Han, W.-J. Choi, S.-G. Lee, K. Kwon†. "Digitally Self-Calibrated RC Oscillator Utilizing Farey Search Algorithm under ASIL-D Conditions within AEC-Q100 Grade 0 Temperature Range". *IEEE Transactions on Circuits and Systems I, Sept. 2025*.
- N.-E. Oyunbaatar, J. Wei, L. Wang, S.-H. Kim, H. Lee, K. Kwon, Y. Won, D.-W. Lee†. "3D-Printed CNT-Reinforced Bioresorbable Vascular Scaffold with Enhanced Mechanical Stability and Integrated Wireless Pressure Sensor for Continuous Hemodynamic Monitoring". *ACS Sensors, Aug. 2025*.
- D. S. Yang, M. Zhou, S. Li, S. Cho, Y. Wu, Y. Sekine, E. E. Kanatzidis, Z. Lv, K. Yamagishi, J. Kim, C. Park, S. Yoo, H. Hua, J. Park, J. Kang, J. U. Kim, J. Feng, E. Pniushkova, K. Kwon, J.-H. Kim, S. G. Seo, J. Y. Kwak, R. Avila, T. Senzaki, A. J. Aranyosi, R. Ghaffari, Y. Huang†, J. Rogers†. "Soft, Skin-Interfaced 3D Microfluidic Systems for High Performance Assessment of Sweat Rate, Cumulative Loss and Biochemical Content". *Advanced Functional Materials, July 16, 2025*.
- C. Park\*, D. Y. Park\*, H. Zhang\*, D. Yang\*, C. R. Redden, S. Yoo, T. Park, M. Zhou, J.-Y. Yoo, Y. Sim, A. Vázquez-Guardado, R. Avila, J. Kim, H.-Y. Ahn, Y. Kim, S. Oh, J.-H. Kim, A. Banks, A. F. Shaaban, Y. Huang†, K. Kwon†, J. A. Rogers†. "Adaptive Electronics for Photovoltaic, Photoluminescent and Photometric Methods in Power Harvesting for Wireless Wearable Sensors". *Nature Communication, July 1, 2025*.
- D. Y. Park\*, H.-M. Lee\*, S.-H. Kim, Y. Sim., Y. Kang, G. Jang, S. Kim, K. Kwon†, H. Ryu†. "Recent Advances in Bioresorbable Biomedical Applications: From Materials to Devices". *Advanced Electronic Materials, June 27, 2025*.
- M. Park, S. Li, K.M. Song, K. Kwon, J.-H. Yun, R. Avila, R.C. Webb, H.M. Arafa, S. Cho, G. Lee, C. Correira, B. Kim, Y.B. Kim, H.J. Ha, W.-Y. Maeng, J.-Y. Yoo, H. Jeong, H. Ryu, S.M. Won, Y.H. Jung, Y. Park, S.J. Kang, Y. Huang, J.A. Rogers. "Evaporative cooling for low-cost monitoring of flow of cerebrospinal fluid through shunts in patients with hydrocephalus". *Biosensors and Bioelectronics, June. 15 2025*.
- D. M. Tiruneh\*, G. Jang\*, K. Kwon†, H. Ryu†. "Highly compact inertia-driven triboelectric nanogenerator for self-powered wireless CO2 monitoring via fine-vibration harvesting". *Nano Energy, June. 1 2025*.
- B. Hwang\*, Y. Lee\*, J. Shin, J. Park, U. Lee, and K. Kwon†. "Advanced Voltage Measurement Unit with On-Chip High-Pass Filters for Battery EIS System". *IEEE Asia Pacific Conference on Circuits and Systems (APCCAS), Oct. 2025*.
- W. Lee, S. Kwon, I.-W. Jang, J.-S. Jeong, S. Kim, and K. Kwon†. "A 23.5-fJ/b/dB 15.2-Gb/s/pin Switched-Capacitor-Driven On-Chip Link with Half-VDD DC Biasing and ISI Mitigation". *IEEE European Solid-State Electronics Research Conference (ESSERC), Sept. 2025*.
- L. Wang , N.-E. Oyunbaatar , D.-S. Kim , J. Wei , Y.-J. Jeong , H. Lee , S.-H. Kim , Y. Won , K. Kwon , I.-S. Jeong , and D.-W. Lee†. "Ultra-Sensitive Wireless Pressure Sensor for Real-Time Cardiovascular Restenosis Monitoring in Smart Stents". *IEEE International Conference on Micro Electro Mechanical Systems (MEMS), Jan. 2025*.

**2024**

- J. Wei, N.-E. Oyunbaatar, Y.-J. Jeong, J. Park, S.-H. Kim, K. Kwon, H. Lee, Y. Won, D.-S. Kim, D.-W. Lee. "Enhancing Flexibility of Smart Bioresorbable Vascular Scaffolds through 3D Printing using Polycaprolactone and Polylactic Acid". *Sensors and Actuators B: Chemical, Sept. 2024*.
- Y.-N. Lee, S.-W. Jo, G. Rahim, S.-G. Lee, and K. Kwon†. "Small-perturbation Electrochemical Impedance Spectroscopy System with High Accuracy for High-capacity Batteries in Electric Vehicles". *IEEE Transactions on Industrial Electronics, Sept. 5 2024*.
- J. Kim\*, M. I. Bury\*, K. Kwon\*, J.-Y. Yoo, N. V. Halstead, H.-S. Shin, S. Li, S. M. Won, M.-H. Seo, Y. Wu, D. Y. Park, M. Kini, J. W. Kwak, S. R. madhvapathy, J. L. Ciatti, J. H. Lee, S. Kim, H. Ryu, K. Yamagishi, H.-J. Yoon, S. S. Kwak, B. Kim, Y. Huang, L. C. Halliday, E. Y. Cheng , G. A. Ameer, A. K. Sharma, J. A. Rogers. "A Wireless, Implantable Bioelectronic System for Monitoring Urinary Bladder Function Following Surgical Recovery". *Proceedings of the National Academy of Sciences of the United States of America (PNAS), Apr. 2 2024*.
- G. G. Yang, H. J. Choi, S. Li, J. H. Kim, K. Kwon, H. M. Jin, B. H. Kim, S. O. Kim. "Intelligent block copolymer self-assembly towards IoT hardware components". *Nature Reviews Electrical Engineering, Feb. 5 2024*.
- Y. Park\*, H. Luan\*, K. Kwon\*, T. S. Chung, S. Oh, J.-Y. Yoo, G. Chung, J. Kim, S. Kim, S. S. Kwak, J. Choi, H.-P. Phan, S. Yoo, H. Jeong, J. Shin, S. M. Won, H.-J. Yoon, Y. Jung, J. A. Rogers. "Soft, full Weatstone bridge 3D pressure sensors for cardiovascular monitoring". *nature partner journal (npj) Flexible Electronics, Jan. 29 2024*.
- H. Ryu\*, J. W. Song\*, H. Luan\*, Y. Sim\*, S. S. Kwak, H. Jang, Y. Jo, H. Jeong, J. Shin, D. Y. Park, K. Kwon†, G. A. Ameer†, J. A. Rogers†. "Materials and Device Designs for Wireless Monitoring of Temperature and Thermal Transport Properties of Wound Beds during Healing". *Advanced Healthcare Materials, Feb. 19 2024*.
- J. Han\*, W.-J. Choi\*, Y.-S. Son, S.-G. Lee, and K. Kwon†. "ASIL-D and AEC-Q100 Grade 0 Compliant Automotive RC Oscillator with Farey Sequence-based Calibration". *IEEE Custom Integrated Circuits Conference (CICC), April 2024*.

**2023**

- N.-E. Oyunbaatar, D.-S. Kim, A. Shanmugasundaram, S.-H. Kim, Y.-J. Jeong, K. Kwon, E. Choi, D.-W. Lee. "Implantable self-reporting stent for detecting in-stent restenosis and cardiac functional dynamics". *ACS Sensors, Dec. 2023*.
- N.-E. Oyunbaatar, A. Shanmugasundaram, K. Kwon, D.-W. Lee. "Continuous Monitoring of Cardiovascular Function with a Smart Stent Incorporating a Flexible and Stretchable Wireless Pressure Sensor". *Journal of Micromechanics and Microengineering, vol. 33, Sept. 2023*.
- K. Munirathinam, K. Kwon, J. Park, D.-W. Lee. "Liquid dielectric layer-based microfluidic capacitive sensor for wireless pressure monitoring". *Sensors & Actuators: A. Physical, vol. 357, August 1 2023*.
- W. Ouyang, W. Lu, Y. Zhang, Y. Liu, J.U. Kim, H. Shen, Y. Wu, H. Luan, K. Kilner, S. P. Lee, Y. Lu, Y. Yang, J. Wang, Y. Yu, A. J. Wegener, J. A. Moreno, Z. Xie, Y. Wu, S. M. Won,  K. Kwon, C. Wu, W. Bai, H. Guo, T. Liu, H. Bai, G. Monti, J. Zhu, S. R. Madhvapathy, J. Trueb, M. Stanslaski, E. M. Higbee-Dempsey, I. Stepien, N. Ghoreishi-Haack, C. R. Haney, T. Kim, Y. Huang, R. Ghaffari, A. R. Banks, T. C. Jhou, C. H. Good, and J. A. Rogers. "A wireless, battery-free, fully implantable system for closed-loop neurorecording and neuromodulation in small animals". *Nature Biomedical Engineering, April 27 2023*.
- K. Kwon\*†, J. U. Kim\*, S. M. Won\*, J. Zhao\*, R. Avila , H. Wang , K. S. Chun , H. Jang , K. H. Lee , J.-H. Kim , S. Yoo , Y. Kang , J. Kim , J. Lim , Y. Park , W. Lu , T. Kim , A. Banks , Y. Huang , J. A. Rogers†. "A battery-less wireless implant for the continuous monitoring of vascular pressure, flow rate and temperature". *Nature Biomedical Engineering, April 10 2023*.
- J. W. Song\*, H. Ryu\*, W. Bai\*, Z. Xie\*, A. Vázquez-Guardado, K. Nandoliya, R. Avila, G. Lee, Z. Song, J. Kim, M.-K. Lee, Y. Liu, M. Kim, H. Wang, Y. Wu, H.-J. Yoon, S. S. Kwak, J. Shin, K. Kwon, W. Lu, X. Chen, Y. Huang, G. A. Ameer† and J. A. Rogers†. "Bioresorbable, wireless, and battery-free system for electrotherapy and impedance sensing at wound sites". *Science Advances, vol. 9, no. 8, Feb. 22 2023*.
- J. Shin\*, H. Wang\*, K. Kwon\*, D. Ostojich, Z. Christiansen, J. Berkovich, Y. Park, Z. Li, G. Lee, R. Nasif, T. S. Chung, C.-J. Su, J. Lim, Y. Ishida, A. Ikoma, Y.-A. Lu, D. H. Lin, S. Xu, A. Banks, J.-K. Chang†, J. A. Rogers†. "Wireless, Soft Sensors of Skin Hydration With Designs Optimized for Rapid, Accurate Diagnostics of Dermatological Health". *Advanced Healthcare Materials, vol. 12, no. 4, Feb. 6 2023*.
- Y.-N. Lee, K.-S. Choi, S.-W. Jo, G. Rahim, K. Kwon, and S.-G. Lee†. "Fast-settling Onboard Electrochemical Impedance Spectroscopy System Adopting Quasi-linear-phase Band-pass Filter". *IEEE International Instrumentation and Measurement Technology Conference (I2MTC), July 2023*.
- J. Lee, S. Woo, W. Jeong, K.-S. Oh, D. Kim, Y. Ko, J.-Y. Jeon, J. Lee, Y.-S. Son, S.-G. Lee, and K. Kwon†. "ASIL-D compliant Battery Monitoring IC with High Measurement Accuracy and Robust Communication". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2023*.

**2022**

- Y. J. Kang, H. M. Arafa, J. Yoo, C. Kantarcigil, J.-T. Kim, H. Jeong, S. Yoo, S. Oh, J. Kim, A. Tzavelis, Y. Wu, K. Kwon, J. Winograd, S. Xu, B. Martin-Harris†, J. A. Rogers†. "Soft, wireless skin-interfaced mechano-acoustic sensors for real-time monitoring and patient feedback on respiratory and swallowing biomechanics". *nature partner journal (npj) Digital Medicine, vol. 5, no. 147, Sept. 20 2022*.
- S. Li, Y. Park, H. Luan, H. Wang, K. Kwon, J. A. Rogers, Y. Huang. "Measurement of Blood Pressure via a Skin-Mounted, Non-Invasive Pressure Sensor". *Journal of Applied Mechanics, vol. 88, no. 10, June 8 2022*.

**2021**

- S. Y. Heo\*, K. Kwon\*, M. Chan, P. Gutruf, A. Burton, T. Banks, C. Duan, H. Jang, J. Kim, D. Franklin, J. B. Park, J. A. Rogers. "Wireless, Accumulation Dosimeters Monitor Pulsed and Non-pulsed Germicidal Lamps". *IEEE Sensors Journal, vol. 21, no. 17, June 23 2021*.
- H. Jeong, J. Y. Lee, K. H. Lee, Y. J. Kang, J.-T. Kim, R. Avila, A. Tzavelis, J. Kim, H. Ryu, S. S. Kwak, J. U. Kim, A. Banks, H. Jang, J.-K. Chang, S. Li, C. K. Mummidisetty, Y. Park, S. Nappi, K. S. Chun, Y. J. Lee, K. Kwon, X. Ni, H. U. Chung, H. Luan, J.-H. Kim, C. Wu, S. Xu, A. Banks, A. Jayaraman, Y. Huang, J. A. Rogers. "Differential cardiopulmonary monitoring system for artifact-canceled physiological tracking of athletes, workers, and COVID-19 patients". *Science Advances, vol. 7, no. 20, May 12 2021*.
- J. K. Robinson, S. Patel, S. Y. Heo, E. Gray, J. Lim, K. Kwon,  Z. Christiansen, J. Model, J. Trueb, A. Banks, M. Kwasny, J. A. Rogers. "Real Time UV Measurement with a Sun Protection System Warning Young Adults of Sunburn: Prospective Cohort Stud". *JMIR mHealth and uHealth, May 6 2021*.
- K. Kwon\*, J. U. Kim\*, Y. Deng\*, S. R. Krishnan, J. Choi, H. Jang, K. Lee, C.-J. Su, I. Yoo, Y. Wu, L. Lipschultz, J.-H. Kim, T. S. Chung, D. Wu, Y. Park, T. Kim, R. Ghaffari, S. Lee, Y. Huang, J. A. Rogers. "An on-skin platform for wireless monitoring of flow rate, cumulative loss and temperature of sweat in real time". *Nature Electronics, Mar. 2021*.
- Y. Park, C. K. Franz, H. Ryu1, H. Luan, K. Y. Cotton, J. U. Kim, T. S. Chung, S. Zhao, A. V. Guardado, D. S. Yang , K. Li, R. Avila, J. K. Phillips, M. J. Quezada, H. Jang, S. S. Kwak, S. M. Won, K. Kwon, H. Jeong, A. J. Bandodkar, M. Han, H. Zhao, G. R. Osher, H. Wang, K. Lee, Y. Zhang , Y. Huang, J. D. Finan, J. A. Rogers. "Three dimensional, multifunctional neural interfaces for cortical spheroids and engineered 3 assembloids". *Science Advances, vol. 7, no. 12, Mar. 2021*.
- W. Lu, W. Bai, H. Zhang, C. Xu, A. M. Chiarelli, A. Vázquez-Guardado, Z. Xie, H. Shen, K. Nandoliya, H. Zhao, K.H. Lee, Y. Wu, D. Franklin, R. Avila, S. Xu, A. Rwei M. Han, K. Kwon, Y. Deng, X. Yu, E. B. Thorp, X. Feng, Y. Huang, J. Forbess, Z.-D. Ge, J. A. Rogers. "Wireless, Implantable Catheter-type Oximeter Designed for Cardiac Oxygen Saturation". *Science Advances, vol. 7, no. 7, Feb. 10 2021*.
- K. Kwon\*, H. Wang\*, J. Lim, K. S. Chun, H. Jang, I. Yoo, D. Wu, A. J. Chen, C. G. Gu, L. Lipschultz, J. U. Kim, J. Kim, H. Jeong, H. Luan, Y. Park, C.-J. Su, Y. Ishida, S. R. Madhvapathy, A. Ikoma, J. W. Kwak, D. S. Yang, A. Banks, S. Xu, Y. Huang, J.-K. Chang, J. A. Rogers. "Wireless, Soft Electronics for Rapid, Multi-sensor Measurements of Hydration Levels in Healthy and Diseased Skin". *Proceedings of the National Academy of Sciences of the United States of America, vol. 118, no. 5, Jan. 2021*.
- Y.S. Oh, JH. Kim, Z. Xie, ... K. Kwon ... et al. "Battery-free, wireless soft sensors for continuous multi-site measurements of pressure and temperature from patients at risk for pressure injuries". *Nature Communication, 12, 5008, Aug. 24 2021*.

**연도 표기 없음**

- T. W. Park, H. Zhang, C. Park, S. D. Goldstein, L. Wade, A. J. McLuckie, Y. Kulahci, R. Janarthanan, T. Y. Kim, M.-S. Jo, B. Sazoglu, Z. Demir, O. Diricanli, W.-Y. Maeng, S. Yoo, K. Zhang, H.-Y. Ahn, J. U. Kim, J. Lee, A. Banks, S. Oh, K. Kwon, V. S. Gorantla, A. Nugent, A. Pelech, Y. Huang, J. A. Rogers†. "A compact, wireless fluorimeter system for continuous, real-time monitoring of in vivo fluorescence signals". *Science Advances (게재 승인)*.

## 교수 수상과 활동

- Impact Research Award, KAIST, 2025
- KAIST Top 10 Research Achievements Award, KAIST, 2025
- Asia Pacific (APAC) Associate Secretary, IEEE ISSCC TPC, 2025
- Convergence Research Award, KI, 2024
- Excellent Paper Award, KAIST, 2024
- Country Representative of Korea, IEEE ISSCC TPC, 2024
- Kwon Oh-Hyun Endowed Professor, KAIST, 2023–2026
- Excellent Young Researchers Award, IDEC, 2022
- Technology Innovation Award, KAIST, 2021

## 연락과 위치

- 교수 이메일: kyeongha@kaist.ac.kr(랩 표기 "kyeongha at kaist.ac.kr")[^prof]
- 교수실: KAIST 나노종합기술원(E19) 207호[^prof]
- 연구실: KAIST 나노종합기술원(E19) 204호, 내선 7567·7667 (대전 유성구 대학로 291)[^home]

[^home]: 권경하 연구그룹 누리집 첫 화면 <https://krg.kaist.ac.kr/> (2026-10-19 열람)
[^prof]: 권경하 연구그룹 교수 소개 <https://krg.kaist.ac.kr/members/professor> (2026-10-19 열람)
[^graduate]: 권경하 연구그룹 대학원생 페이지 <https://krg.kaist.ac.kr/members/graduate> (2026-10-19 열람)
[^alumni]: 권경하 연구그룹 졸업생 페이지 <https://krg.kaist.ac.kr/members/alumni> (2026-10-19 열람)
[^bms]: 연구 페이지(Battery Management IC) <https://krg.kaist.ac.kr/research/battery-management-ic> (2026-10-19 열람)
[^serdes]: 연구 페이지(High-Speed Serial Links) <https://krg.kaist.ac.kr/research/high-speed-serial-links> (2026-10-19 열람)
[^health]: 연구 페이지(Digital Healthcare) <https://krg.kaist.ac.kr/research/digital-healthcare> (2026-10-19 열람)
[^papers]: 권경하 연구그룹 논문 목록 <https://krg.kaist.ac.kr/publications/papers> (2026-10-19 열람)
[^p1]: J.-K. Lee 외, K. Kwon, 2023 IEEE International Solid-State Circuits Conference (ISSCC), 322-324 (2023). <https://doi.org/10.1109/isscc42615.2023.10067607> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y.-N. Lee 외, K. Kwon, IEEE Transactions on Industrial Electronics 72, 3202-3212 (2025). <https://doi.org/10.1109/tie.2024.3436676> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Han, W.-J. Choi, S.-G. Lee, K. Kwon, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 1721-1730 (2026). <https://doi.org/10.1109/tcsi.2025.3604256> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: W. Lee 외, K. Kwon, 2026 IEEE Custom Integrated Circuits Conference (CICC), 1-4 (2026). <https://doi.org/10.1109/cicc65509.2026.11509464> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: W. Lee 외, K. Kwon, 2025 IEEE European Solid-State Electronics Research Conference (ESSERC), 361-364 (2025). <https://doi.org/10.1109/esserc66193.2025.11214071> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. Sim, Y. Park, K. Kwon, Science Advances 12, eaea8902 (2026). <https://doi.org/10.1126/sciadv.aea8902> 초록 기준.
[^p7]: C. Park 외, J. A. Rogers, Nature Communications 16, 5808 (온라인 2025-07-01). <https://doi.org/10.1038/s41467-025-60911-1> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: D. M. Tiruneh, G. Jang, K. Kwon, H. Ryu, Nano Energy 138, 110872 (2025). <https://doi.org/10.1016/j.nanoen.2025.110872> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).

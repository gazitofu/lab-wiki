# 전력전자시스템연구실 (Power Electronics Systems Lab)

**서울대학교 공과대학 전기·정보공학부 · 신종원 부교수**

- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 제어 이론·제어 공학[^p1][^p3], 첨단 반도체 패키징[^p5][^p6], 전력전자 변환기·전력 변환 시스템[^p3], 전자파 적합성·신호 무결성[^p5], 반도체 계측·검사[^p2]
- 홈페이지: <https://pesl.snu.ac.kr/>

> 전기를 필요한 형태로 바꾸는 회로와 제어 방법을 설계하고, 차량 전력 시스템과 전력 모듈의 잡음·신뢰성을 연구한다.[^home][^p5]

## 무엇을 연구하나

전력전자시스템연구실은 전력변환(전압·전류 등 전력의 형태를 용도에 맞게 바꾸는 일)을 연구한다. 직류(DC, Direct Current, 흐르는 방향이 일정한 전류)를 다른 전압의 직류로 바꾸는 DC-DC 변환과, 교류(AC, Alternating Current, 흐르는 방향이 주기적으로 바뀌는 전류)를 직류로 바꾸는 AC-DC 변환이 중심이다. 회로 구성, 수학 모형, 아날로그·디지털 제어, 모의실험과 실제 장치 시험을 함께 다룬다.[^home][^lab]

회로가 전기를 공급하는 대상인 부하가 갑자기 달라지면 출력 전압도 변한다. 이 랩은 측정한 출력 전압으로 제어 신호를 조절하는 방법, 입력 측에서 얻은 정보로 출력 전압을 맞추는 방법을 개발한다. 제어기(측정값을 바탕으로 장치에 줄 입력을 정하는 부분)의 수학 모형을 세우고 실제 전력변환 회로에서 작동을 확인한다.[^p1][^p3]

고주파(문맥에서 다루는 주파수 범위의 높은 쪽)에서 작동하는 회로의 부품 구조도 다룬다. 평면 변압기(평평한 도체 층을 감은 선 대신 사용하고 자기장의 변화로 전기 에너지를 전달하는 부품)의 층 두께와 배치를 바꾸어 기생 정전용량(설계 목적과 별개로 생기는 전하 저장 능력)을 줄이는 연구가 한 예다. 두 회로 사이에서 전력을 전달하는 변환기의 인덕턴스(전류가 변할 때 자기장 변화로 전압이 생기는 성질)를 정하는 방법도 분석한다.[^p4][^p8]

전력 모듈(전력을 다루는 반도체와 연결·보호 구조를 묶은 부품)에서는 패키징(반도체를 연결하고 보호하는 구조와 제작 기술)을 연구한다. 직접접합구리 기판(세라믹에 구리층을 붙인 기판)의 일부 구조를 바꾸고 에폭시나 실리콘 겔을 적용해 공통모드 잡음(여러 전선에서 기준점에 대해 같은 방향으로 나타나는 원치 않는 전기 신호)을 줄인다. 모듈의 열 전달과 반복되는 온도 변화에 대한 기계적 신뢰성도 함께 확인한다.[^p5][^p6][^p7]

## 주요 연구 주제

### 전력변환 회로의 제어와 상태 측정

부하 변화 때 출력 전압이 목표보다 올라가거나 내려가는 현상을 줄이도록 제어 신호의 기울기를 조절한다. 또 반도체가 켜져 있을 때의 저항 변화를 회로의 전류와 입력·출력 전압으로 측정하여, 소자의 남은 사용 수명을 추정하는 데 활용하는 방법을 제안한다.[^p2][^p3]

### 자기 부품과 양방향 변환기

평면 변압기에서 원치 않는 전하 저장 효과를 분석하고 기판 두께와 감은 선의 구성을 바꾸는 방법을 제안한다. 양방향 변환기(전력을 양쪽 방향으로 전달할 수 있는 변환 회로)에서는 입력 전압이 달라질 때 전류와 손실이 어떻게 바뀌는지 분석해 직렬 인덕턴스를 선택한다.[^p4][^p8]

### 전력 모듈의 잡음과 신뢰성

전력 모듈 아래쪽 구리층의 일부를 없애거나 다른 재료로 대체해 원치 않는 전류의 경로를 바꾼다. 에폭시를 이용한 지지 구조, 실리콘 겔을 이용한 보호 구조를 제안하고 잡음 측정과 온도 반복 시험으로 전기적·기계적 특성을 확인한다.[^p5][^p6][^p7]

## 대표 논문

서울대 소속이 확인되거나 서울대 부임 이후 연도로 게시된 연구 중 제어, 상태 측정, 자기 부품, 패키징을 보여 주는 8편을 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 연도는 확인한 서지의 표기이며, 온라인 출판일을 확인한 논문은 그 날짜를 각주에 적었다.[^prof]

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2025 | [Primary-Side Regulated Active-Clamp Forward Converter by Controlling Clamp Capacitor Voltage](https://doi.org/10.1109/TPEL.2025.3578643) | 입력 전력과 전압으로 계산한 기준값을 이용해 회로 안 축전기의 전압을 조절하고 출력 전압을 맞추는 방법을 제안했다.[^p1] |
| 2 | 2024 | [Noise-Robust Online Measurement of the On-State Resistance of the Power Semiconductor Devices in PWM Converters](https://doi.org/10.1109/ACCESS.2024.3396575) | 스위치를 켜고 끌 때 생기는 잡음의 영향을 피하도록, 회로 전류와 직류 전압에서 소자의 켜진 상태 저항 변화를 구했다.[^p2] |
| 3 | 2024 | [Digital Linear Slope Control for Boost Converter to Improve Load Transient](https://doi.org/10.1109/ACCESS.2024.3407102) | 전류를 따로 측정하지 않고 출력 전압만으로 제어 신호의 기울기를 조절해, 부하 변화 때 전압의 오르내림을 줄였다.[^p3] |
| 4 | 2024 | [Analyzing and mitigating parasitic capacitances in planar transformers for high-frequency operation](https://doi.org/10.1007/s43236-024-00804-6) | 평면 변압기의 원치 않는 전하 저장 효과를 분석하고 기판 두께와 감은 선 배치를 바꾸는 방법을 시험했다.[^p4] |
| 5 | 2024 | [Power Module With Low Common-Mode Noise and High Reliability](https://doi.org/10.1109/ACCESS.2024.3420393) | 모듈의 구리층 일부를 없애고 에폭시로 지지해 잡음을 줄였으며, 열 전달과 반복 온도 변화에 대한 신뢰성을 확인했다.[^p5] |
| 6 | 2024 | [Improved Packaging of Power Module With Low-Permittivity Material for Low Common-Mode Noise and High Reliability](https://doi.org/10.1109/TPEL.2024.3438831) | 구리층 일부를 전하를 저장하는 성질이 작은 에폭시로 대체해 잡음을 줄이고 열적·기계적 특성을 확인했다.[^p6] |
| 7 | 2025 | [Utilizing Silicone Gel Encapsulation in Power Semiconductor Module to Improve Manufacturability While Reducing Common-Mode Noise](https://doi.org/10.1109/TPEL.2025.3617463) | 구리층 일부를 없앤 모듈을 실리콘 겔로 감싸 제조와 잡음 특성을 개선하고 반복 온도 변화에 대한 안정성을 확인했다.[^p7] |
| 8 | 2024 | [Optimizing inductance for minimizing reactive power in single-phase-shift modulated dual active bridge converters under variable input voltage](https://doi.org/10.1007/s43236-024-00961-8) | 입력 전압에 따라 달라지는 전류를 분석해, 양방향 변환기의 불필요한 전력 왕복과 전도 손실을 줄일 직렬 인덕턴스를 제안했다.[^p8] |

## 교수와 전문 분야

신종원은 서울대학교 전기·정보공학부 부교수다. 서울대에서 2006년 학사, 2013년 박사 학위를 받았다. 버지니아텍과 토요타 북미 연구 조직을 거쳐 2018년부터 중앙대학교 에너지시스템공학부에서 근무했으며, 2024년 3월 서울대에 조교수로 부임하고 2026년 3월 부교수가 되었다. 나고야대학교 방문부교수 경력도 게시되어 있다.[^prof][^faculty]

전문 분야는 전력변환 회로의 구성과 제어, 변환기의 수학 모형, 전력 모듈 패키징이다. 최근 논문에서는 출력 전압 제어와 소자 저항 측정, 평면 변압기의 구조 분석, 모듈의 잡음과 신뢰성을 다룬다.[^faculty][^p1][^p2][^p4][^p5]

## 응용 분야

차량 전력 시스템 구조, 재생에너지용 전력전자, AC-DC 및 DC-DC 전력변환 회로가 랩의 응용 분야다. 게시 과제에는 전동화 차량용 전력변환, 데이터센터 전원용 변환기, 모바일 충전기, 변환기의 고장 사전 진단을 위한 상태 측정이 포함되어 있다.[^home][^projects]

## 구성원

누리집 Students의 박사과정 3명, 석사과정 9명, 학부생 6명이다. 과정은 랩의 구획을 따랐다. 대표 논문 참여는 같은 영문 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| 백종운 (Jongun Baek) | 박사과정 |  |
| 신준호 (Junho Shin) | 박사과정 | 1, 2 |
| 조영훈 (Younghoon Cho) | 박사과정 |  |
| 서동한 (Donghan Seo) | 석사과정 | 3, 8 |
| 정범순 (Beomsoon Chung) | 석사과정 |  |
| 박민석 (Minseok Park) | 석사과정 |  |
| 최민국 (Minguk Choi) | 석사과정 |  |
| 안영록 (Youngrok An) | 석사과정 |  |
| 김지환 (jihwan Kim) | 석사과정 |  |
| 설윤제 (YunJe Seol) | 석사과정 |  |
| 조원준 (Wonjun Cho) | 석사과정 |  |
| 정석준 (Sukjoon Chung) | 석사과정 |  |
| 오대룡 (Daeryong Oh) | 학부 연구생 |  |
| 김인창 (Inchang Kim) | 학부 연구생 |  |
| 김진서 (Jinseo Kim) | 학부 연구생 |  |
| 오윤주 (Yunjoo Oh) | 학부 연구생 |  |
| 유영욱 (Youngwook Yu) | 학부 연구생 |  |
| 안태욱 (Taewook An) | 학부 연구생 |  |

## 졸업생과 이전 구성원

Alumni에 게시된 11명과 랩이 적은 진로다. 신종원 교수의 중앙대 재직 시기를 포함한 명단이다.[^alumni][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 양동혁 (Donghyuk Yang) |  | Hyundai Mobis Co., Ltd. |
| 김석원 (Seokwon Kim) |  | Korea Electronics Technology Institute (KETI) |
| 성한힘 (Hanhim Sung) |  | Samsung Electronics Co., Ltd. (Global Technology Research, Manufacturing Robot Team) |
| 이수정 (Sujeong Lee) |  | Hyundai Rotem Defense Solution Electronic system team |
| 용승욱 (Seung-uk Yong) |  | Doosan Enerbility. (Plant engineering center) |
| 최시훈 (Sihoon Choi) |  | Nagoya University Assistant Professor |
| 홍명재 (MyeongJae Hong) |  | Samsung Electronics Co., Ltd. (Circuit Design (Set & Board) Applicative Product R&D Team) |
| 고동희 (Donghee Ko) |  | Samsung Electronics Co., Ltd. System LSI |
| 정혜린 (Hyelin Jung) |  | Hyundai Mo tor Co., Ltd. (Charging System Engineering Design Team) |
| 김도윤 (Doyun Kim) |  | LG Electronics. |
| 김성환 (Seonghwan Kim) |  | Hyundai Mobis Co., Ltd. |

## 최근 논문 목록 (2021–2026)

2021–2026년으로 표기된 논문 19편이다. 신종원 교수의 2024년 3월 서울대 부임 전 논문을 포함한다. 연도와 서지는 각 목록·개별 등록 기록의 표기를 따른다.[^prof][^bibliography]

**2026**

- Beomsoon Chung, Jongun Baek, Jong-Won Shin. "Two-Port Network Design for a Double-Sided LC-Compensated Capacitive Wireless Power Transfer with Robustness to Coupling Variation". *Conference Paper; May 2026*.
- Junho Shin, Jung-Ik Ha, Jong-Won Shin. "Single Input Multi Output Converter Design by Three-Port Network Analysis". *Conference Paper; May 2026*.
- Minseok Park, Jong-Won Shin. "A New DC-DC Converter with Enhanced CM Noise Characteristics and Capacitive Isolation". *Conference Paper; May 2026*.
- Younghoon Cho, Paul Jang, Jong-Won Shin. "Multi-mode Control for an Asymmetric Half-bridge Flyback Converter". *Conference Paper; May 2026*.
- Youngrok An, Junho Shin, Donghan Seo, Jong-Won Shin. "Design of Active-Clamp Push-Pull Converter with Decoupled Transformer for Low Conduction Loss". *Conference Paper; May 2026*.
- Jongun Baek, Donghan Seo, Jong-Won Shin. "Novel Approach of Mobile Charger Utilizing Resonant Switched-Capacitor Converter". *Conference Paper; March 2026*.
- Younghoon Cho, Paul Jang, Jong-Won Shin. "Cross Regulation Characteristics by Current Dip in Fly-buck Converter". *Conference Paper; March 2026*.
- Jongun Baek, Donghan Seo, Jong-Won Shin. "Implementation of Resonant Switched-Capacitor Converter in Discontinuous Conduction Mode". *Conference Paper; March 2026*.
- Junho Shin, Yuqi Wei, Jong-Won Shin. "The Primary-Side Regulation of Active-Clamp Forward Converter with On-the-Fly Output Voltage Variation". *IEEE Journal of Emerging and Selected Topics in Power Electronics; Article; January 2026*.

**2025**

- Junho Shin, Jong-Won Shin. "Primary-Side Regulated Active-Clamp Forward Converter by Controlling Clamp Capacitor Voltage". *IEEE Transactions on Power Electronics PP: 1-11*.
- Sihoon Choi, Jiyoon Choi, Thiyu Warnakulasooriya, Jong-Won Shin, Jun Imaoka, Masayoshi Yamamoto. "Utilizing Silicone Gel Encapsulation in Power Semiconductor Module to Improve Manufacturability While Reducing Common-Mode Noise". *IEEE Transactions on Power Electronics 41: 3308-3318*.

**2024**

- Junho Shin, Jong-Won Shin, Wonhee Kim. "Noise-Robust Online Measurement of the On-State Resistance of the Power Semiconductor Devices in PWM Converters". *IEEE Access 12: 63669-63682 (2024)*.
- Seokwon Kim, Donghan Seo, Seonghwan Kim, Seung-Uk Yong, Jong-Won Shin. "Digital Linear Slope Control for Boost Converter to Improve Load Transient". *IEEE Access 12: 76826-76836 (2024)*.
- Sihoon Choi, Jiyoon Choi, Thiyu Warnakulasooriya, Jong-Won Shin, Jun Imaoka, Masayoshi Yamamoto. "Power Module With Low Common-Mode Noise and High Reliability". *IEEE Access 12: 90929-90939 (2024)*.
- Sujeong Lee, Seokwon Kim, Jong-Won Shin, Wonhee Kim. "Analyzing and mitigating parasitic capacitances in planar transformers for high-frequency operation". *Journal of Power Electronics 24: 946-954*.
- Sihoon Choi, Jiyoon Choi, Thiyu Warnakulasooriya, Jong-Won Shin, Jun Imaoka, Masayoshi Yamamoto. "Improved Packaging of Power Module With Low-Permittivity Material for Low Common-Mode Noise and High Reliability". *IEEE Transactions on Power Electronics 39: 14261-14270*.
- Seung-Uk Yong, Donghan Seo, Seokwon Kim, Jong-Won Shin, Wonhee Kim. "Optimizing inductance for minimizing reactive power in single-phase-shift modulated dual active bridge converters under variable input voltage". *Journal of Power Electronics 25: 1-11*.

**2023**

- Sihoon Choi, Jong-Won Shin, Jun Imaoka, Masayoshi Yamamoto. "Voltage-Controlled Variable Inductor for Fixed-Frequency Critical Conduction Mode Operation". *IEEE Trans. Ind. Electron. 70(6): 5707-5716 (2023)*.

**2021**

- Dongwook Kim, Jongun Baek, Jisu Lee, Joonho Shin, Jong-Won Shin. "Implementation of Soft-Switching Auxiliary Current Control for Faster Load Transient Response". *IEEE Access 9: 7092-7106 (2021)*.

## 과제

게시 과제 18건 가운데 기간이 2021년 10월 22일–2026년 10월 22일에 걸치는 전력변환·상태 측정 과제 15건이다. 서울대 부임 이전에 시작하거나 종료된 과제를 포함하며, 지원기관과 기간은 랩 표기다.[^projects][^prof]

- High-density power conversion for electrified vehicles by high-frequency GaN FET and three-dimensional cooling (지원 the Ministry of Science and ICT, South Korea; 기간 March 2022- February 2026)
- Development of Nano Grid Gateway Using High-Efficiency Micro-SST (지원 the Ministry of Science and ICT, South Korea; 기간 May 2021-Februrary 2024)
- Fault-detection and prognostics of power conditioning system (지원 the Ministry of Science and ICT, South Korea; 기간 May 2021-Februrary 2024)
- Development of Energy Router Using SST for Energy Network (2nd stage) (지원 the Ministry of Science and ICT, South Korea; 기간 January 2021-December 2023)
- Component-level RUL (remaining useful life) estimation of power semiconductor module (지원 Korea Institute of Energy Research; 기간 January 2021-December 2024)
- Unified power conversion system for plug-in hybrid electric vehicle (PHEV) with high efficiency and high power density (지원 the Ministry of Education, South Korea; 기간 June 2018-May 2022)
- Development of a High-Performance LLC Converter for Data Center Power Systems (지원 Samsung; 기간 July 2025-April 2026)
- Development of Real-time Health Index Measurement Method for Fault-Prediagnosis of Converter (지원 Hyundai Motor Company; 기간 September 2024-September 2026)
- Development of 65W GaN Charger for M obile A pplication (지원 Lucidmicrosystems; 기간 March 2024-December 2025)
- Development of a Control Algorithm for High-Frequency Switching PFC (지원 LG Electronics; 기간 February 2025-September 2025)
- Bidirectional 48 V-12 V isolated GaN FET converters (지원 LG Innotek; 기간 June 2023-June 2024)
- Bidirectional 22-kW on-board battery charger compatible for both single- and three-phase AC mains (지원 EGtronics; 기간 July 2022-June 2023)
- Reliable synchronous rectifier for high-efficiency power conversion (지원 Hyundai Motor Company; 기간 June 2022-May 2023)
- Synchronous driving technique of 3-kW bidirectional low-voltage DC-DC converter for HEV application (지원 Hyundai Motor Company; 기간 November 2021-July 2023)
- 4-kW bidirectional low-voltage dc-dc converter for vehicular application (지원 Hyundai MOBIS; 기간 March 2020-October 2022)

## 연락과 위치

- 교수 연구실: 서울특별시 관악구 관악로 1, 서울대학교 301동 607호, 우편번호 08826[^contact][^faculty]
- 전화: 02-880-1821[^contact]

## 각주
[^home]: PESL 첫 화면, 차량 전력 시스템 구조·재생에너지·전력변환 회로와 설계·제어·시험 소개. <https://pesl.snu.ac.kr/> (관측일 2026-10-26).
[^lab]: 서울대학교 전기·정보공학부, 전력전자시스템연구실 소개. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=140> (관측일 2026-10-26).
[^prof]: PESL Professor, 학력·직위·재직 기간. <https://pesl.snu.ac.kr/member/professor> (관측일 2026-10-26).
[^faculty]: 서울대학교 전기·정보공학부 신종원 교수 소개, 직위·학력·경력·연구 분야·위치. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p899> (관측일 2026-10-26).
[^students]: PESL Students. <https://pesl.snu.ac.kr/member/students> (관측일 2026-10-26).
[^alumni]: PESL Alumni. <https://pesl.snu.ac.kr/member/alumni> (관측일 2026-10-26).
[^projects]: PESL Research Projects, 정부·산업체 지원 과제의 제목·지원기관·기간. <https://pesl.snu.ac.kr/research-projects> (관측일 2026-10-26).
[^contact]: PESL Contact Us. <https://pesl.snu.ac.kr/contact-us> (관측일 2026-10-26).
[^bibliography]: dblp의 Jong-Won Shin 서지 5편, ResearchGate 자동 생성 저자 목록 첫 쪽의 저자를 확인할 수 있는 9편, 개별 논문 등록 기록 5편을 합친 목록이다. <https://dblp.org/pid/283/2839.html>, <https://www.researchgate.net/scientific-contributions/Jong-Won-Shin-2184717854>. 중복 제목은 한 번만 실었다. 개별 등록 기록의 주소와 연도 표기 차이는 [근거 페이지](./pesl-sources.md)에 적었다 (관측일 2026-10-26).
[^p1]: J. Shin, J.-W. Shin, IEEE Transactions on Power Electronics PP, 1-11 (2025, 등록 연도). <https://doi.org/10.1109/TPEL.2025.3578643> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/392577905_Primary-Side_Regulated_Active-Clamp_Forward_Converter_by_Controlling_Clamp_Capacitor_Voltage>
[^p2]: J. Shin, J.-W. Shin, W. Kim, IEEE Access 12, 63669-63682 (2024, 등록 연도). <https://doi.org/10.1109/ACCESS.2024.3396575> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/380337334_Noise-robust_online_measurement_of_the_on-state_resistance_of_the_power_semiconductor_devices_in_PWM_converters>
[^p3]: S. Kim 외, J.-W. Shin, IEEE Access 12, 76826-76836 (온라인 2024-05-30). <https://doi.org/10.1109/ACCESS.2024.3407102> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/381013003_Digital_Linear_Slope_Control_for_Boost_Converter_to_Improve_Load_Transient>
[^p4]: S. Lee, S. Kim, J.-W. Shin, W. Kim, Journal of Power Electronics 24, 946-954 (온라인 2024-04-16). <https://doi.org/10.1007/s43236-024-00804-6> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/379890131_Analyzing_and_mitigating_parasitic_capacitances_in_planar_transformers_for_high-frequency_operation>
[^p5]: S. Choi 외, M. Yamamoto, IEEE Access 12, 90929-90939 (온라인 2024-06-28). <https://doi.org/10.1109/ACCESS.2024.3420393> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/381818769_Power_Module_with_Low_Common-Mode_Noise_and_High_Reliability>
[^p6]: S. Choi 외, M. Yamamoto, IEEE Transactions on Power Electronics 39, 14261-14270 (2024). <https://doi.org/10.1109/TPEL.2024.3438831> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/382926423_Improved_Packaging_of_Power_Module_with_Low-Permittivity_Material_for_Low_Common-Mode_Noise_and_High_Reliability>
[^p7]: S. Choi 외, M. Yamamoto, IEEE Transactions on Power Electronics 41, 3308-3318 (2025, 등록 연도). <https://doi.org/10.1109/TPEL.2025.3617463> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/396188201_Utilizing_Silicone_Gel_Encapsulation_in_Power_Semiconductor_Module_to_Improve_Manufacturability_while_Reducing_Common-Mode_Noise>
[^p8]: S.-U. Yong 외, W. Kim, Journal of Power Electronics 25, 1-11 (2024, 등록 연도). <https://doi.org/10.1007/s43236-024-00961-8> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/386571386_Optimizing_inductance_for_minimizing_reactive_power_in_single-phase-shift_modulated_dual_active_bridge_converters_under_variable_input_voltage>

# 반도체 집적회로 및 시스템 설계 연구실 (Analog & Power Circuits and Systems Lab, APCS Lab)

**서울대학교 첨단융합학부 차세대지능형반도체전공, 공과대학 전기·정보공학부(겸임) · 홍성완 부교수**

- 분야: 아날로그·전력 관리 집적회로와 시스템, 전력 변환, 무선 전력 전송, 에너지 하베스팅, 통신용 전원 제어
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^ece-lab][^research], 무선 전력 전송[^home][^research], 에너지 하베스팅[^home][^research]
- 홈페이지: <https://sites.google.com/view/apcs-lab>
- 근거와 출처: [APCS 근거 페이지](apcs-sources.md)

> 전자 기기에 필요한 전원을 만드는 회로를 설계하고, 전선 없는 전력 전달과 주변 에너지 수확, 통신 신호에 맞춘 전원 공급을 연구하는 연구실이다.[^home][^ece-lab]

## 무엇을 연구하나

APCS는 홍성완 부교수가 이끄는 아날로그(연속적으로 변하는 신호를 다루는 방식)·전력(시간당 전달되거나 소비되는 전기 에너지) 관리 연구실이다. 집적회로는 전자 부품과 그 연결을 반도체 칩에 모은 회로다. 연구실은 전기를 기기가 요구하는 형태로 바꾸는 전력 변환 회로, 무선 전력 전송, 에너지 하베스팅(주변의 움직임·열·빛·전파에서 전기 에너지를 얻는 기술), 통신용 전원 회로를 연구 분야로 든다.[^ece-lab][^home]

전력 변환 쪽에서는 데이터센터, 사람 형태의 로봇, 화면, 휴대 기기와 배터리에 전원을 공급하는 회로를 다룬다. 전압(단위 전하가 두 지점 사이를 이동할 때의 에너지 차)과 전류(단위 시간에 흐르는 전하량)를 제어하는 것이 공통 대상이다. 연구 소개는 데이터센터의 전력 변환 단계를 부하(전원을 공급받는 회로나 장치) 가까이에 두는 수직 전력 공급, 로봇 관절의 모터 구동기, 양·음 전압을 함께 내는 전원, 휴대 기기의 온도를 고려한 전원 관리를 설명한다.[^research]

다른 갈래는 전선 없이 전력을 전달하거나 주변 에너지를 모으는 회로, 그리고 통신 신호의 변화에 맞춰 전원을 조절하는 회로다. 연구실은 여러 주변 에너지원을 함께 이용하는 시스템과 진동에서 전기를 얻는 회로를 소개한다. 이식형 기기의 전원도 연구 대상이며, 관련 논문은 다중 출력 전압 변환기와 무선 전력 수신용 정류기(교류 전기를 한 방향으로 흐르는 직류 전기로 바꾸는 회로)를 제안한다. 이 두 논문은 서울대 부임 전 연구다.[^research][^bio-simo][^bio-rectifier]

## 주요 연구 주제

### 전력 변환과 공급

서로 다른 변환 방식을 결합하는 하이브리드 회로와, 입력·출력 사이의 전압 차가 작은 조건에서도 출력을 조절하는 LDO(Low-Dropout Regulator)를 설계한다. 화면용 양극성 전원, 배터리 충전과 상태 관리도 다룬다. 2026년 논문은 중간 커패시터(전기장에 에너지를 저장하는 부품)를 없애는 2단 변환 회로를 제안했다.[^research][^p1]

다른 대표 논문은 두 출력 전압을 만드는 전압 상승 회로,[^p2] 여러 곳에 배치한 디지털(불연속적인 값으로 정보를 표현하는 방식) 전압 조절 회로,[^p3] 여러 칩을 병렬(전류가 흐르는 여러 경로가 같은 두 지점을 잇도록 연결하는 방식)로 연결해 확장하는 전압 하강 회로를 다룬다.[^p4]

### 무선 전력 전송과 주변 에너지 수확

전선 없이 전력을 전달하는 회로와, 여러 주변 에너지원에서 전력을 얻는 회로를 연구한다. 연구 소개에는 진동·빛·열·전파를 함께 이용하는 시스템과 압전(힘을 받으면 전하가 나타나고 전압을 가하면 변형되는 성질)을 이용한 진동 에너지 수확이 나온다. 이식형 기기 전원 논문은 새로운 전력 변환 회로와 정류 회로를 제안한다.[^research][^bio-simo][^bio-rectifier]

### 통신 신호에 맞춘 전원 제어

포락선 추적(Envelope Tracking)은 진동하는 신호의 진폭 변화 경계를 따라 전원 전압을 조절하는 기법이다. 연구실은 통신 송신 회로가 필요로 하는 전력을 공급하도록 출력 전압을 실시간으로 조절하는 전원 회로를 연구한다.[^research]

## 대표 논문

2021–2026년 목록에서 서울대 재직 시기의 논문 4편을 골랐다. 아래의 쉬운 설명은 ResearchGate 등록 초록(1번)과 OpenAlex 등록 초록(2–4번)만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | A Middle-Capacitor-free Two-Stage 48V to 1-1.2V Converter using Fixed 0.5 Duty-Cycle Switched-Capacitor · IEEE Transactions on Power Electronics[^p1] | 높은 입력 전압을 두 단계로 낮추는 회로다. 첫 단계의 스위치가 켜져 있는 시간 비율을 고정해 전류에 따른 손실을 줄이고, 둘째 단계의 연속적인 커패시터 전류 경로를 이용해 중간 커패시터를 없애면서 전원 변화에 대한 응답을 개선했다. | 마지막 저자 |
| 2 | 2026 | A Dual-Output Hybrid-Boost (DOHB) Converter for 37.5 V/150 V with Continuous Current Delivery and Switching Charge-Recycling · IEEE Transactions on Power Electronics[^p2] | 서로 다른 두 출력 전압을 만드는 전압 상승 회로다. 둘째 단계에서 전류를 연속적으로 공급하고, 스위치를 켜고 끌 때의 전하를 재사용해 회로 접속점에서 생기는 해당 손실을 절반으로 줄였다. | 마지막 저자 |
| 3 | 2026 | A Scalable Distributed Digital LDO Achieving Fast and Accurate Current Balancing · VLSI 2026[^p3] | 여러 곳에 배치한 전압 조절 회로의 규모를 늘리면서 전류를 고르게 나누도록 설계했다. 회로를 그룹으로 묶어 전류 균형을 맞추는 보정(기준에 맞도록 오차를 조절하는 일) 단계를 줄이고, 아날로그 전류 측정 회로를 이용한다. | 마지막 저자 |
| 4 | 2026 | A 12V-to-1V Scalable 2N-Phase Buck Converter using 0V-Stress Balancer with Shortest IL Balancing Path for Parallel IC Expansion in xPU Systems · VLSI 2026[^p4] | 전류 균형을 맞추는 경로를 짧게 둔 회로를 이용해 여러 칩의 병렬 연결로 확장하는 전압 하강 회로다. 칩 하나부터 네 개까지 연결한 시제품을 시험했다. | 마지막 저자 |

## 교수와 전문 분야

홍성완 부교수는 고려대학교에서 학사(2009), KAIST에서 석사(2011)와 박사(2014)를 받았다. 삼성전자 DMC 연구소 책임연구원(2014년 3월–2017년 2월), 숙명여자대학교 전자공학전공 조교수(2017년 3월–2021년 2월), 서강대학교 전자공학과 조·부교수(2021년 3월–2026년 2월)를 거쳐 2026년 3월 서울대학교에 부임했다. 첨단융합학부 교수 소개는 전기·정보공학부를 겸무 소속으로 적는다.[^ece-prof][^snuti]

교수의 전문 분야는 아날로그·전력 관리 집적회로와 시스템 설계다. 연구실이 현재 소개하는 전력 변환, 무선 전력 전송, 에너지 수확, 통신용 전원 공급을 연결하는 분야다. 논문 목록에는 전압을 낮추거나 높이는 회로와 전압 조절기, 증폭기(신호의 크기를 키우는 회로)가 반복해서 등장하며, 대표 논문은 전력 변환 단계의 구성과 전류 경로를 설계하는 연구를 보여 준다.[^ece-prof][^journals][^conferences][^p1]

공개 학술 활동으로는 2026년 ISSCC 한국 대표·세션 좌장, 2025년 VLSI 기술프로그램위원·세션 좌장, 2025년 PwrSoC Workshop 조직위원·기술프로그램위원이 적혀 있다. 국내에서는 2026년 반도체공학회 ISSCC 리뷰워크숍과 대한전자공학회 아날로그·파워 워크숍의 조직위원을 맡았다.[^prof]

## 응용 분야

연구실은 데이터센터의 전력 공급, 사람 형태 로봇의 관절 구동, 화면용 전원, 휴대 기기 전원 관리, 배터리 충전·관리, 주변 에너지로 동작하는 기기, 이식형 기기용 전원, 무선 통신 송신용 전원을 응용 대상으로 든다. 이식형 기기 관련 논문에서 다루는 것은 전력을 만들고 전달하는 회로다.[^home][^bio-simo][^bio-rectifier]

## 구성원

2026년 10월 26일 Students 페이지의 대학원생 13명이다. 과정과 시작 시점은 누리집 카드 표기다. 이전 소속 시절에 시작한 과정도 함께 실려 있다. 전영준은 대표(Representative)로 표시되어 있다. "대표 논문 참여"는 위 표의 번호이며 같은 영문 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Joo-Mi Cho (조주미) | 석박사통합과정 | Mar. 2021 ~ | joomicho@sogang.ac.kr |  |
| Hyeon-Ji Choi (최현지) | 박사과정 | Sep. 2026 ~ | choihj0202@snu.ac.kr |  |
| Chan-Ho Lee (이찬호) | 석박사통합과정 | Mar. 2022 ~ | chlee9695@sogang.ac.kr | 1, 4 |
| Young-Ju Oh (오영주) | 박사과정 | Sep. 2026 ~ | youngjuoh@snu.ac.kr |  |
| Young-Jun Jeon (전영준) | 박사과정 | Sep. 2026 ~ | youngjun_jeon@snu.ac.kr | 4 |
| Sang-Yun Nam (남상윤) | 박사과정 | Sep. 2026 ~ | okjd123@snu.ac.kr | 3 |
| Jeong-Hun Kim (김정헌) | 석박사통합과정 | Mar. 2023 ~ | jh1705k@sogang.ac.kr | 2 |
| Hyeonho Park (박현호) | 석박사통합과정 | Mar. 2023 ~ | juid0122s@sogang.ac.kr | 2 |
| Hyun-Woo Jeong (정현우) | 박사과정 | Sep. 2026 ~ |  | 1 |
| Won-Gyu Kim (김원규) | 박사과정 | Sep. 2026 ~ |  | 3 |
| Yong-Chan Lee (이용찬) | 석사과정 | Mar. 2025 ~ | lean1223@sogang.ac.kr |  |
| Seoborn Chung (정서본) | 석박사통합과정 | Sep. 2026 ~ | colaffio@snu.ac.kr |  |
| Bo-Geun Lim (임보근) | 석사과정 | Sep. 2026 ~ | mymy2u2@snu.ac.kr |  |

## 졸업생과 진로

2026년 10월 26일 Alumni 페이지의 박사 1명·석사 10명이다. 2020년 2월–2026년 8월 표기를 모두 실었으며, 서울대 부임 전 숙명여대·서강대 재직 시기 졸업생이 포함된 목록이다. 학위·과정 표현과 진로는 누리집 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyo-Jin Park (박효진) | PhD Course (Aug. 2026) | SK Hynix |
| Dowon Jeong (정도원) | MS Course (Feb. 2026) | SK Hynix |
| Kenneth Minseop Kim (김민섭) | MS Course (Feb. 2026) | Samsung Electronics |
| Jongwoo Jang (장종우) | MS Course (Feb. 2026) | Samsung Electronics |
| Seok-Jun Lee (이석준) | MS Course (Aug. 2025) | Samsung Electronics |
| Jun-Seok Oh (오준석) | MS degree (Feb. 2025) | Samsung Electronics |
| Ho-Chan Ahn (안호찬) | MS degree (Feb. 2024) | Samsung Electronics |
| Esun Baik (백이선) | MS degree (Feb. 2024) | Silicon Mitus |
| Chan Kyu Lee (이찬규) | MS degree (Feb. 2024) | Samsung Electronics |
| Su-Min Park (박수민) | MS degree (Aug. 2023) | Samsung Electronics |
| Ji-Eun Park (박지은) | MS degree (Feb. 2020) | Magna Chip |

## 최근 논문 목록 (2021–2026)

Conferences의 19–38번 20편과 Journals의 20–39번 20편, 합계 40편이다. 연도는 각 페이지의 연도 구역을 따르며 2021년 구역의 10월 22일 이전 논문도 포함한다. 서울대 부임(2026년 3월) 전 숙명여대·서강대 재직 시기 논문이 섞여 있다. 제목에는 전력 변환·전압 조절·증폭 회로와 이식형 기기용 전원 회로가 나온다.[^conferences][^journals][^prof]

Journals 39번은 2026년 구역의 날짜 없는 게재 승인 항목으로, 첫 화면이 2026년 8월 승인을 알린다. 37·38번은 누리집 권호가 2026년 11월이므로 출판 완료로 보지 않고 2026년 6월 소식에 따른 게재 승인으로 표시했다. 나머지 제목·저자·서지는 랩 표기를 따른다. Journals의 별표는 교신저자 표시다.[^journals][^home]

**2026**

- Sang-Yun Nam, Won-Gyu Kim, Ja eseung Lee, Jun-Hyeok Yang, and Sung-Wan Hong. "A Scalable Distributed Digital LDO Achieving Fast and Accurate Current Balancing". *in IEEE Symp. VLSI Circuits (VLSI), June. 2026*.
- Young-Jun Jeon, Chan-Ho Lee, Jong-Woo Jang, and Sung-Wan Hong. "A 12V-to-1V Scalable 2N-Phase Buck Converter using 0V-Stress Balancer with Shortest IL Balancing Path for Parallel IC Expansion in xPU Systems". *in IEEE Symp. VLSI Circuits (VLSI), June. 202 6*.
- Hyun-Woo Jeong, Chan-Ho Lee, Hyeon-Ji Choi, and Sung-Wan Hong. "A 92.4%-Peak-Efficiency 48V to 0.8-to-1.6V Hybrid Converter with Inductor-Interleaved Fibonacci Switched-Capacitor". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 202 6*.
- Hyeon-Ji Choi, Joo-Mi Cho, Sang-Yun Nam, and Sung-Wan Hong. "A 94.8%-Peak-Efficiency Double Step-Up SIBO Converter Achieving 88% Output Ripple Reduction for AMOLED Display". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2026*.
- Joo-Mi Cho, Jeong-Hun Kim, Yong-Chan Lee, and Sung-Wan Hong. "A Hybrid Bipolar-Output Isolated Converter with +15V/–5V Outputs for SiC Gate Drivers". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2026*.
- Joo-Mi Cho, Jeong-Hun Kim, Yong-Chan Lee, and Sung-Wan Hong\*. "A Hybrid Bipolar-Output Isolated Gate Driver Power Supply With Primary-Side Regulation and Switched-Capacitor for SiC Power Devices". *IEEE Journal of Solid-State Circuits (JSSC), 게재 승인*.
- Yong-Chan Lee, Young-Jun Jeon, Hyun-Woo Jeong, Yang Jiang, and Sung-Wan Hong\*. "A Dummy-Free Low-Power LDO with Sub-1-μA Quiescent Current for Fast Wake-Up in Long-Term Standby Applications". *게재 승인(첫 화면 2026-06); 누리집 권호: IEEE Transactions on Power Electronics (TPEL), vol. 41, no. 11, pp. 18906-18910, Nov. 2026*.
- Jeong-Hun Kim, Hyo-Jin Park, Hyeonho Park, Jeeyoung Shin, Woong Choi, Junwon Jeong, and Sung-Wan Hong\*. "A Dual-Output Hybrid-Boost (DOHB) Converter for 37.5 V/150 V with Continuous Current Delivery and Switching Charge-Recycling". *게재 승인(첫 화면 2026-06); 누리집 권호: IEEE Transactions on Power Electronics (TPEL), vol. 41, no. 11, pp. 18828-18832, Nov. 2026*.
- Chan-Ho Lee, Hyun-Woo Jeong, Jeeyoung Shin, Woong Choi, Junwon Jeong, and Sung-Wan Hong\*. "A Middle-Capacitor-free Two-Stage 48V to 1-1.2V Converter using Fixed 0.5 Duty-Cycle Switched-Capacitor". *IEEE Transactions on Power Electronics (TPEL), vol. 41, no. 9, pp. 14329-14333, Sept. 2026*.

**2025**

- Sang-Yun Nam, Hyeonho Park, Won-Gyu Kim, and Sung-Wan Hong. "A 0.087 fs FOM Current-mirror-based Analog-assisted Digital LDO with VO Ripple Optimization". *in IEEE Symp. VLSI Circuits (VLSI), June. 2025*.
- Joo-Mi Cho, Hyeon-Ji Choi, Hyo-Jin Park, Jaeho Han, Kwang-Seok Yun, Jong-Pil Im, and Sung-Wan Hong. "2,771% Power Improvement Triple-source Ground-symmetric Pile-up Resonant Energy Harvester". *in IEEE Symp. VLSI Circuits (VLSI), June. 2025*.
- Hyun-Woo Jeong, Chan-Ho Lee, Sang-Yun Nam, and Sung-Wan Hon g. "A Gm-Boosted 3-stage Amplifier with Gain-Enhancing Feedforward Path for CL of 40-160nF". *in IEEE Symp. VLSI Circuits (VLSI), June. 2025*.
- Jeong-Hun Kim, Young-Jun Jeon, Won-Gyu Kim, Jaeseung Lee, Jun-Hyeok Yang, and Sung-Wan Hong. "A 2A Fully Analog Distribution LDO with Noise Immunity for a SoC". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Young-Jun Jeon, Jeong-Hun Kim, Won-Gyu Kim, and Sung-Wan Hong. "A Sub-1V, 50mV Dropout LDO using Pseudo-Impedance Buffer with Phase-Margin Improvement Design". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Hyeon-Ji Choi, Joo-Mi Cho, Hyo-Jin Park, Seok-Jun Lee, and Sung-Wan Hong\*. "A 0-to-10uF Off-chip Output Capacitor-Scalable Boost Converter Achieving 96.68% Peak Efficiency". *IEEE Solid-State Circuits Letters (SSCL), vol. 8, pp. 233 - 236, Aug. 2025*.
- Young-Ju Oh, Chan-Ho Lee, Jeong-Hun Kim, Hyeonho Park, Dowon Jeong, and Sung-Wan Hong\*. "A 91.7% Peak-Efficiency 48V-to-1V Pseudo Two-Stage Two-Phase Hybrid Buck Converter". *IEEE Transactions on Circuits and Systems II (TCAS-II) , vol. 72, no. 9, pp. 1 318-1 322, Jul. 2025*.
- Won-Gyu Kim, Sang-Yun Nam, Young-Jun Jeon, and Sung-Wan Hong\*. "A 1.8V-5.5V LDO-BGR System with LACM Buffer for High PSRR in Camera Applications". *IEEE Transactions on Circuits and Systems II (TCAS-II) , vol. 72, no. 8, pp. 1108-1112, Aug. 2025*.
- Chan-Ho Lee, Hyeon-Woo Jeong, Young-Ju Oh, Dowon Jeong, Eunju Jeong, Woosung Park and Sung-Wan Hong\*. "A Scalable N-level Dickson Charge Pump Based 12V to 1-1.8V Hybrid Buck Converter". *IEEE Transactions on Power Electronics (TPEL) , vol. 40, no. 9, pp. 12021-12025, Sept. 2025*.
- Hyo-Jin Park, Hyeonho Park, Dowon Jeong, and Sung-Wan Hong\*. "Achieving Wide Voltage-Conversion-Ratio and Reduced Power Losses for High Efficiency with EVCR Buck Converter for a 1.8 V Power Rail". *IEEE Transactions on Power Electronics (TPEL) , vol. 40, no. 9, pp. 12011-12014 ,Sept 2025*.
- Ho-Chan Ahn, Chan-Ho Lee, Sang-Yun Nam, Jeong-Hun Kim, HyeonHo Park, Hyun-Woo Jeong, Jeeyoung Shin, Woong Choi, Junwon Jeong, and Sung-Wan Hong\*. "A 2 A Dual Loop LDO with Dynamic Negative Feedback Loop and G m Boosting Error Amplifier for Off-Chip and Cap-less Applications". *IEEE Transactions on Circuits and Systems I (TCAS-I), vol. 72, no. 5, pp. 2444 - 2455, May 2025*.
- Young-Ju Oh, Hyun-Woo Jeong, Hyeonho Park, Jeeyoung Shin, Junwon Jeong, Woong Choi, and Sung-Wan Hong\*. "Compact Single-Stage Input and Output Rail-to-Rail Class AB Buffer Amplifier with an Asymmetric Output Structure". *IEEE Solid-State Circuits Letters (SSCL), vol. 8, pp. 73 - 76, Mar. 2025*.
- Young-Ju Oh, Chan-Ho Lee, Sang-Yun Nam, Jun-Seok Oh, Seok-Jun Lee, Jun-Hyeok Yang, Jaeseung Lee, Sung-Wan Hong\*. "A Robust High On-duty Buck Converter Achieving a Peak Effective On-Duty of 0.976 with EMI Suppression". *IEEE Transactions on Industrial Electronics (TIE), vol. 72, no. 3, pp. 3223 - 3227, Mar. 2025*.
- Chan-Ho Lee, Jeong-Hun Kim, Hyun-Woo Jeong, Hyeonho Park, Jeeyoung Shin, Junwon Jeong, Woong Choi, and Sung-Wan Hong\*. "A 12V Input 0.3V-to-0.6V Output Imbalanced Inductor-Currents Converter that Achieves a Peak Efficiency of 90.7%". *IEEE Transactions on Circuits and Systems II (TCAS-II), vol. 72, no. 1, pp. 338 - 342, Jan. 2025*.

**2024**

- Hyeon-Ji Choi, Chan-Ho Lee, Young-Jun Jeon, Hyeonho Park, Jeong-Hun Kim, Young-Jin Woo, Ju-Pyo Hong, Haifeng Jin, Sung-Wan Hong. "A 92.7% Peak Efficiency 12V-to-60V Input to 1.2V Output Hybrid DC-DC Converter based on a Series-Parallel-Connected Switched Capacitor". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2024*.
- Hyo-Jin Park, Joo-Mi Cho, Chan-Ho Lee, Young-Ju Oh, Hyunwoo Jeong, Jun-Hyeok Yang, Jaeseung Lee, and Sung-Wan Hong. "A 97.18% Peak-Efficiency Asymmetrically Implemented Dual-phase (AID) Converter with a full Voltage-Conversion Ratio (VCR) between 0-and-1". *in IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2024*.
- Young-Jun Jeon, Hyun-Woo Jeong, Hyeonho Park, Jeeyoung Shin, Junwon Jeong, Woong Choi, and Sung-Wan Hong\*. "A 600mA Multi-Feedback Loops Capacitor-less Low-dropout Regulator with a -40dB Power Supply Rejection at 1MHz with 27.5μA Quiescent Current Consumption". *IEEE Transactions on Power Electronics (TPEL), vol. 39, no. 10, pp. 11969 - 11973, Oct. 2024*.
- Chan-Kyu Lee, Chan-Ho Lee, Young-Jun Jeon, Young-Ju Oh, Byunghun Lee, and Sung-Wan Hong\*. "A 92 ns Settling-Time Fast-Transient Capacitor-less LDO with a Stable Class B Bandwidth-boosting Error Amplifier and an Improved Buffer for Mobile Applications". *IEEE Transactions on Industrial Electronics (TIE), vol. 71, no. 9, pp. 11696 - 11700, Sep. 2024*.
- Hyo-Jin Park, Joo-Mi Choi, Hyeon-Ji Choi, Chan-Ho Lee, Young-Jun Jeon, Jeeyoung Shin, Woong Choi, Junwon Jeong, and Sung-Wan Hong\*. "A Simultaneous Energy Transferring SIBO Converter Achieving Low Ripple and High Efficiency for AMOLED Applications". *IEEE J. Solid-State Circuits (JSSC), vol. 59, no. 5, pp. 1497 – 1508, May. 2024*.

**2023**

- Ho-Chan Ahn, Joo-Mi Cho, Hyeon-Ji Choi, Chan-Ho Lee, Chan-Kyu Lee, and Sung-Wan Hong. "A 2 A Maximum Load Current Capable 0-to-1 μF Off-chip Capacitor N-type LDO using Dual Dynamic Negative Feedback Loop and an Improved Error Amplifier". *in IEEE European Solid-State Circuits Conference (ESSCIRC), Sep. 2023*.
- Hyo-Jin Park, Joo-Mi Cho, Hyeon-Ji Choi, Chan-Ho Lee, and Sung-Wan Hong. "96.48% Peak-Efficiency Continuous-Current Step-Up Battery Charger (CC-SUBC) with Dual Energy-Harvesting Sources for Automotive Application". *in IEEE Symp. VLSI Circuits (VLSI), Jun. 2023*.
- Chan-Ho Lee, Hyo-Jin Park, Joo-Mi Choi, Hyeon-Ji Choi, Young-Jun Jeon, and Sung-Wan Hong. "A 1V 20.7uW Four-Stage Amplifier Capable of Driving a 4-to-12nF Capacitive Load with 1.07MHz GBW with an Improved Active Zero". *in IEEE Symp. VLSI Circuits (VLSI), Jun. 2023*.
- Hyeon-Ji Choi, Chisung Bae, Yeunhee Huh, Sang Joon Kim, Seungchul Jung, Kye-Seok Yoon, Joo-Mi Cho, Hyo-Jin Park, Chan-Ho Lee, Su-Min Park Esun Baik, Young-Ju Oh, Ho-Chan Ahn, Chan-Kyu Lee, and Sung-Wan Hong\*. "An Ultra-Low Power Soft-Switching Self-Oscillating SIMO Converter for Implantable Stimulation Systems". *IEEE Transactions on Industrial Electronics (TIE), vol. 70, no. 8, pp. 8603 - 8608, Aug. 2023*.

**2022**

- Young-Ju Oh, Hyo-Jin Park, Joo-Mi Cho, Hyeon-Ji Choi, Su-Min Park, Chan-Ho Lee, Esun Baik, Chan-Kyu Lee, Ho-Chan Lee, and Sung-Wan Hong. "A High Slew-rate Wide-range Capacitive Load Driving Buffer Amplifier with Correlated Dual Positive Feedback Loops". *in IEEE International SoC Design Conference (ISOCC), Oct. 2022*.
- Chan-Ho Lee, Hyo-Jin Park, Joo-Mo Cho, Hyeon-Ji Choi, Su-Min Park, Esun Baik, Young-Ju Oh, Ho-Chan Ahn, Chan-Kyu Lee, Jeeyoung Shin, Se-Un Shin, and Sung-Wan Hong\*. "An Input-Independent Loop Type-III Buck Converter with PSRR Improvement and EMI Suppression for Enhancing the Security of Edge Devices". *IEEE Transactions on Power Electronics (TPEL), vol. 37, no. 9 pp. 10070 - 10074, Sep. 2022*.

**2021**

- Hyeon-Ji Choi, Joo-Mi Cho, Hyo-Jin Park, and Sung-Wan Hong. "An Output Capacitor-less Low-dropout Regulator using a Wide-range Single-Stage Gain-Boosted Error Amplifier and a Frequency-dependent Buffer with a Total Compensation Capacitance of 2.5 pF in 0.5 um CMOS". *in IEEE Asian Solid-State Circuits conference (ASSCC), Nov. 2021*.
- Hyo-Jin Park, Joo-Mi Cho, Hyunji Choi, Esun Baik, Jeeyoung Shin, and Sung-Wan Hong. "A 18 uA Rail-to-Rail Class-AB Operational Amplifier with a High-Slew Miller Compensation (HSMC) Technique with 240% Settling Time Reduction in 0.18 um". *in IEEE European Solid-State Circuits conference (ESSCIRC), Sep. 2021*.
- Joo-Mi Cho, Hyo-Jin Park, Hyunji Choi, Esun Baik, Jeeyoung Shin, and Sung-Wan Hong. "A 100-MHz 81.2% All-Paths Inductor-Connected Buck-Converter with Balanced Conduction-Losses and Continuous Path-Currents". *in IEEE European Solid-State Circuits conference (ESSCIRC), Sep. 2021*.
- Joo-Mi Cho, Hyo-Jin Park, and Sung-Wan Hong. "A 0.93-uW Single-Stage Rail-to-Rail Class AB Buffer Amplifier Improving DC gain and Slew-Rate with Different-Ratio Current-Mirrors and Positive-Feedback Loops". *in IEEE Symp. VLSI Circuits (VLSI), Jun. 2021*.
- Najam ul Hassan, Sung-Wan Hong\*, and Byunghun Lee. "A Robust Multi-Output Self-Regulated Rectifier for Wirelessly-Powered Biomedical Applications". *IEEE Transactions on Industrial Electronics (TIE), vol. 68, no. 6, pp. 5466 - 5472, Jun. 2021*.
- Woojoong Jung, Se-Un Shin, Sung-Wan Hong, Sung-Min Yoo, Tae-Hwang Kong, Jun-Hyeok Yang, Sang-Ho Kim, Michal Choi, Jongshin Shin, and Hyung-Min Lee. "Dual-Path Three-Level Buck Converter with Loop-Free Auto-Calibration for Flying Capacitor Self-Balancing". *IEEE Transactions on Power Electronics (TPEL), vol. 36, no. 10, pp. 51– 55, Jan. 2021*.

## 수상

교수 소개의 Awards 가운데 2022–2026년 7건이다. 서울대 부임 전 서강대 재직 시기 수상이 포함되어 있다. 연도만 게시한 항목은 연도만 적었고, 삼성 휴먼테크논문대상 2건의 월은 News 게시 표기를 함께 따랐다. 등급은 교수 소개가 적은 표기다.[^prof][^news]

- 2026-02 · 삼성 휴먼테크논문대상 동상
- 2025 · 제 2 6 회 대한민국 반도체설계대전 은상
- 2025 · 제 26회 대한민국 반도체설계대전 기업특별 상
- 2025-02 · 삼성 휴먼테크논문대상 동상
- 2024 · 제 25회 대한민국 반도체설계대전 기업특별상
- 2023 · 제 24회 대한민국 반도체설계대전 은상
- 2022 · 제 23회 대한민국 반도체설계대전 동상

## 소식

2021년 10월 22일–2026년 10월 22일 범위에 드는 날짜의 논문 승인·채택 33건과 교수 임명 1건이다. 첫 화면과 News에 같은 논문을 알린 항목은 한 번씩 실었다. 서울대 부임 전 서강대 재직 시기 소식이 포함되어 있다.[^home][^news][^prof]

- 2026-08 · 조주미의 SiC 전력 소자용 양극성 절연 전원 회로 논문, IEEE Journal of Solid-State Circuits 게재 승인
- 2026-06 · 이용찬의 장기 대기 기기용 저전력 전압 조절 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2026-06 · 김정헌의 이중 출력 전압 상승 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2026-03 · 남상윤의 분산형 디지털 전압 조절 회로 논문, VLSI 2026 채택
- 2026-03 · 전영준의 병렬 확장이 가능한 다상 전압 하강 회로 논문, VLSI 2026 채택
- 2026-03 · 이찬호의 중간 커패시터 없는 2단 전압 변환 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2025-10 · 정현우의 피보나치 스위치드 커패시터를 이용한 하이브리드 전압 변환 회로 논문, ISSCC 2026 채택
- 2025-10 · 최현지의 AMOLED 화면용 이중 승압 회로 논문, ISSCC 2026 채택
- 2025-10 · 조주미의 SiC 게이트 구동기용 양극성 절연 전압 변환 회로 논문, ISSCC 2026 채택
- 2025-07 · 최현지의 외부 출력 커패시터 용량에 대응하는 전압 상승 회로 논문, IEEE Solid-State Circuits Letters 게재 승인
- 2025-07 · 오영주의 2상 하이브리드 전압 하강 회로 논문, IEEE Transactions on Circuits and Systems II 게재 승인
- 2025-06 · 김원규의 카메라용 전압 조절·기준 전압 회로 논문, IEEE Transactions on Circuits and Systems II 게재 승인
- 2025-05 · 이찬호의 Dickson 전하 펌프 기반 하이브리드 전압 하강 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2025-05 · 박효진의 전압 변환비 범위를 다루는 전압 하강 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2025-04 · 홍성완 교수, ISSCC 기술프로그램위원회 한국 대표로 임명
- 2025-03 · 남상윤의 전류 미러 기반 디지털 전압 조절 회로 논문, VLSI 2025 채택
- 2025-03 · 조주미의 세 에너지원에서 전력을 얻는 에너지 수확 회로 논문, VLSI 2025 채택
- 2025-03 · 정현우의 3단 증폭기 논문, VLSI 2025 채택
- 2025-03 · 오영주의 비대칭 출력 구조를 이용한 버퍼 증폭기 논문, IEEE Solid-State Circuits Letters 게재 승인
- 2024-10 · 이찬호의 인덕터 전류를 불균등하게 배분하는 전압 변환 회로 논문, IEEE Transactions on Circuits and Systems II 게재 승인
- 2024-10 · 김정헌의 분산형 아날로그 전압 조절 회로 논문, ISSCC 2025 채택
- 2024-10 · 전영준의 전압 조절 회로 안정성 설계 논문, ISSCC 2025 채택
- 2024-09 · 안호찬의 이중 제어 경로를 갖춘 전압 조절 회로 논문, IEEE Transactions on Circuits and Systems I 게재 승인
- 2024-07 · 오영주의 전자파 간섭 억제 기능을 갖춘 전압 하강 회로 논문, IEEE Transactions on Industrial Electronics 게재 승인
- 2024-06 · 전영준의 여러 제어 경로를 이용한 전압 조절 회로 논문, IEEE Transactions on Power Electronics 게재 승인
- 2023-11 · 이찬규의 전원 변화 응답을 다루는 전압 조절 회로 논문, IEEE Transactions on Industrial Electronics 게재 승인
- 2023-10 · 최현지의 직렬·병렬 연결 커패시터 기반 하이브리드 전압 변환 회로 논문, ISSCC 2024 채택
- 2023-10 · 박효진의 비대칭 2상 전압 변환 회로 논문, ISSCC 2024 채택
- 2023-09 · 박효진의 AMOLED 화면용 양극성 전원 회로 논문, IEEE Journal of Solid-State Circuits 게재 승인
- 2023-05 · 안호찬의 외부 커패시터 범위에 대응하는 전압 조절 회로 논문, ESSCIRC 2023 채택
- 2023-04 · 박효진의 두 에너지원을 이용한 차량용 배터리 충전 회로 논문, VLSI 2023 채택
- 2023-04 · 이찬호의 용량성 부하 구동용 4단 증폭기 논문, VLSI 2023 채택
- 2022-12 · 최현지의 이식형 자극 시스템용 다중 출력 전압 변환 회로 논문, IEEE Transactions on Industrial Electronics 게재 승인
- 2022-03 · 이찬호의 전자파 간섭과 전원 잡음을 다루는 전압 하강 회로 논문, IEEE Transactions on Power Electronics 게재 승인

## 연락과 위치

- 교수 사무실: 서울특별시 관악구 관악로 1, 서울대학교 18동 419호.[^contact][^ece-prof]
- 연구실: 서울대학교 반도체공동연구소 인재양성관.[^contact]
- 전화: 02-880-8474.[^contact]
- 교수 이메일: swhong@snu.ac.kr.[^contact]

## 각주
[^home]: 첫 화면. 연구 분야, 2026년 8월까지의 논문 승인 소식. <https://sites.google.com/view/apcs-lab> 열람 2026-10-26.

[^research]: Research. 전력 변환, 무선 전력 전송·에너지 수확, 통신용 전원 회로의 연구 설명. <https://sites.google.com/view/apcs-lab/research> 열람 2026-10-26.

[^prof]: Professor. 학력·경력, 학술 활동과 Awards. <https://sites.google.com/view/apcs-lab/members/professor> 열람 2026-10-26.

[^students]: Students. 대학원생 이름·과정·시작 시점과 학교 이메일. 관측 2026-10-26. <https://sites.google.com/view/apcs-lab/members/students> 열람 2026-10-26.

[^alumni]: Alumni. 박사·석사 졸업생과 게시 진로. 관측 2026-10-26. <https://sites.google.com/view/apcs-lab/members/alumni> 열람 2026-10-26.

[^conferences]: Conferences. 국제 학회 논문 1–38번, 최근 목록은 19–38번. <https://sites.google.com/view/apcs-lab/publication/conferences> 열람 2026-10-26.

[^journals]: Journals. 학술지 논문 1–39번, 최근 목록은 20–39번. 별표는 교신저자. <https://sites.google.com/view/apcs-lab/publication/journals> 열람 2026-10-26.

[^news]: News. Featured News와 Latest News. 날짜·성과는 각 구획의 게시 표기. <https://sites.google.com/view/apcs-lab/news> 열람 2026-10-26.

[^contact]: Contact. 교수 사무실, 연구실 위치와 연락처. <https://sites.google.com/view/apcs-lab/contact> 열람 2026-10-26.

[^ece-lab]: 전기·정보공학부 연구실 소개. 국·영문 연구실명과 지도교수, 연구 분야. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=152&md=view> 열람 2026-10-26.

[^ece-prof]: 전기·정보공학부 교수 상세. 직위·학력·2026년 3월 서울대 부임과 이전 경력. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p918> 열람 2026-10-26.

[^snuti]: 첨단융합학부 교수 상세. 차세대지능형반도체전공 부교수, 2026년 3월부터 전기·정보공학부 겸무. <https://snuti.snu.ac.kr/snu__professor/%ED%99%8D%EC%84%B1%EC%99%84/> 열람 2026-10-26.

[^bio-simo]: ResearchGate 등록 초록. 이식형 자극 시스템용 저전력 다중 출력 변환기 자체의 개발을 확인했다. DOI 10.1109/TIE.2022.3231256. <https://www.researchgate.net/publication/366993829_An_Ultra-Low_Power_Soft-Switching_Self-Oscillating_SIMO_Converter_for_Implantable_Stimulation_Systems> 열람 2026-10-26.

[^bio-rectifier]: ResearchGate 등록 초록. 무선 전력 수신용 다중 출력 자기 조절 정류기를 제안한 기여를 확인했다. DOI 10.1109/TIE.2020.2988226. <https://www.researchgate.net/publication/340820445_A_Robust_Multi-Output_Self-Regulated_Rectifier_for_Wirelessly-Powered_Biomedical_Applications> 열람 2026-10-26.

[^p1]: C.-H. Lee 외, S.-W. Hong, IEEE Transactions on Power Electronics 41, 14329-14333 (2026). <https://doi.org/10.1109/tpel.2026.3676469> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/scientific-contributions/Sung-Wan-Hong-2162673947>. 저자 순서는 Crossref 등록 서지, 권호는 Journals 기준. 열람 2026-10-26.

[^p2]: J.-H. Kim 외, S.-W. Hong, IEEE Transactions on Power Electronics 41, 18828-18832 (2026). <https://doi.org/10.1109/tpel.2026.3701068> 초록 기준(OpenAlex 등록 초록). 저자 순서는 Crossref 등록 서지 기준. 열람 2026-10-26.

[^p3]: S.-Y. Nam 외, S.-W. Hong, 2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) (2026). <https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577442> 초록 기준(OpenAlex 등록 초록). 저자 순서는 Crossref 등록 서지 기준. 열람 2026-10-26.

[^p4]: Y.-J. Jeon, C.-H. Lee, J.-W. Jang, S.-W. Hong, 2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) (2026). <https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577414> 초록 기준(OpenAlex 등록 초록). 저자 순서는 Crossref 등록 서지 기준. 열람 2026-10-26.

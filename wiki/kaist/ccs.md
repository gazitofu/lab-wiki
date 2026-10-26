# Cho's Circuits & Systems Lab (CCS)

**KAIST 전기및전자공학부·반도체시스템공학과 · 조성환 교수**

- 분야: 아날로그·혼성 신호 집적회로 설계, 유선·무선 통신용 고속 아날로그 회로(메모리 인터페이스, 유선 송수신기, RF·밀리미터파 주파수 합성기), 센서·생체 신호용 초저전력 아날로그 회로, 기계학습·메모리용 집적회로, 전원 회로
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^home][^ee][^p1], 고속 유선 인터페이스[^hs][^p3], 착용형 생체 센서[^lp], AI 반도체·가속기[^ml][^p6][^p7], 배터리 관리 시스템[^home], 전력 관리 집적회로[^p8], 주파수 합성·클럭 생성 회로[^hs], 센서 인터페이스·판독 집적회로[^lp]
- 홈페이지: <https://ccs.kaist.ac.kr/>
- 근거와 출처: [CCS 근거 페이지](ccs-sources.md)

> 알고리즘과 시스템 구조부터 회로 기법까지 여러 단계를 함께 고려해 아날로그 집적회로를 설계하는 연구실로, 유선·무선 통신용 고속 회로, 센서용 저전력 회로, 기계학습·메모리 회로를 칩으로 만든다.[^home]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 조성환 교수가 이끄는 연구실이다.[^home][^ee] 누리집은 이름을 Cho's Circuits & Systems Lab으로 적고, 반도체시스템공학과와 전기및전자공학부의 교수 소개는 Cho's Circuits & System Laboratory로 적는다.[^home][^sse][^ee] 연구실은 아날로그 집적회로(전압·전류처럼 연속으로 변하는 신호를 다루는 회로를 칩 하나에 모은 것)를 설계하되, 알고리즘과 시스템 구조부터 회로 기법까지 여러 단계의 시스템 추상화를 함께 염두에 둔다고 소개한다.[^home] 주된 연구 분야로는 유선·무선 통신을 위한 고속 아날로그 회로, 배터리 관리와 생체 의료를 포함한 센서 응용을 위한 저전력 아날로그 회로, 기계학습과 메모리 회로 셋을 든다.[^home] 전기및전자공학부 교수 소개는 교수의 주요 연구를 메모리, 인터페이스, 인공지능, 전원, 센서를 위한 집적회로로 적는다.[^ee]

첫째 갈래는 **통신과 메모리 인터페이스를 위한 고속 회로**다. 연구 페이지는 이 갈래를 네 묶음으로 나눈다. 메모리 인터페이스에서는 DRAM(컴퓨터의 주 메모리로 쓰는 반도체 메모리) 인터페이스용 직교 신호 보정 회로와 저전력 DRAM에서 전원 잡음에 흔들리지 않는 클럭 분배를, 전기 연결을 위한 유선 송수신기에서는 DRAM 인터페이스용 저전력·고대역폭 송수신기, 잡음과 전력 효율을 위한 변조·선로 부호화 기법(balanced-coded PAM-4, QAM), 송신기·수신기·클럭 경로 블록의 고속 회로 설계를 든다.[^hs] RF 주파수 합성기 설계에서는 여러 방식의 PLL(위상 고정 루프, 기준 신호에 맞춰 원하는 주파수의 신호를 만드는 회로)을, 밀리미터파 주파수 합성기 설계에서는 레이더 응용을 위한 W 대역·V 대역 주파수 합성기와 FMCW(주파수를 시간에 따라 연속으로 바꾸는 신호 방식) 주파수 합성기를 든다.[^hs] 대표 논문에서는 낮은 주파수의 기준 신호를 주입해 7.5GHz 클럭을 만드는 클럭 곱셈기(기준 신호의 배수 주파수로 클럭을 만드는 회로)에서 지터(클럭 신호의 시점이 흔들리는 정도)와 기준 스퍼(기준 주파수 때문에 생기는 원치 않는 주파수 성분)를 함께 줄였고,[^p1] 주파수를 빠르게 바꾸고 1ns가 안 되는 시간에 안정되는 60GHz 국부 발진기(송수신 회로가 주파수를 옮길 때 쓰는 기준 신호를 만드는 회로)를 만들었으며,[^p2] 이웃 선에서 새어 드는 신호인 누화를 동작 중에 스스로 맞춰 지우는 12Gb/s PAM-4(전압을 네 단계로 나눠 한 번에 두 비트를 보내는 방식) 송수신기를 만들었다.[^p3] 최근 논문 목록에는 여러 장치가 한 버스에 함께 연결되는 멀티드롭 버스용 송신기(VLSI 2025), 3D DRAM용 감지 증폭기(A-SSCC 2025), LPDDR5 모바일 DRAM에서 전원 잡음으로 생기는 지터를 지우는 적응 필터(IEEE Journal of Solid-State Circuits, 2023)도 있다.[^journals][^confs]

둘째 갈래는 **센서와 생체 신호를 위한 저전력 회로**다. 연구 페이지는 착용형 건강관리 시스템 설계로 착용형 심전도 측정 회로, 저전력 광혈류 측정(PPG, 빛으로 혈관의 혈류 변화를 재는 방법) 센서, 맥파 전달 속도(PWV) 측정 칩을 들고, 표준 CMOS 공정으로 만드는 칩 위 센서로 사물인터넷용 저전력·저비용 센서 SoC(여러 기능을 칩 하나에 모은 시스템), 압력 센서 같은 정전 용량 감지 소자, 고해상도·저전력 정전 용량 센서 인터페이스를 든다.[^lp] 온도 센서에서는 칩 위 온도 감시 시스템의 정확도를 높이고 감지 소자 면적을 줄이며 온도에 영향받지 않게 읽어 내는 보정 논리를 다룬다.[^lp] 대표 논문에서는 전극의 접촉 임피던스가 서로 달라도 공통 모드 간섭(두 입력에 똑같이 들어오는 잡음)을 잘 걸러 내는 심전도 증폭기를 만들었고,[^p4] 표준 CMOS 공정으로 만드는 센서를 위해 정전 용량(두 도체 사이에 전하를 담는 능력)을 높은 해상도로 디지털 값으로 바꾸는 변환기를 만들었다.[^p5] 최근 논문 목록에는 리튬이온 전지의 전기화학 임피던스를 재는 아날로그 프런트엔드 칩(A-SSCC 2026), 여러 파장의 PPG로 움직임 잡음을 지우는 심박 추정 기법(IEEE Transactions on Biomedical Circuits and Systems, 2023), 수면 무호흡 감시 칩(A-SSCC 2022)도 있다.[^journals][^confs]

셋째 갈래는 **기계학습과 메모리를 위한 회로**다. 연구 페이지는 저전력 곱셈-누산(MAC) 회로 설계, 아날로그 센서를 품은 상시 동작 기계학습 시스템, 고속·저전력 분류, 아날로그 센서 데이터를 기계학습 회로에 바로 넣는 방식을 들고, 비휘발성 메모리인 낸드 플래시에서는 셀 문턱 전압 분포를 좁혀 읽기·쓰기·지우기 시간을 줄이는 일과 저전력 아날로그 회로·논리 설계를 든다.[^ml] 대표 논문에서는 35개 음성 명령어를 알아듣고 사용자 억양에 맞춰 칩 안에서 직접 학습하는 키워드 인식 칩을 만들었고,[^p6] 층 사이의 데이터 변환 없이 아날로그 메모리와 아날로그 계산으로 합성곱 신경망(CNN, 이미지 인식 등에 쓰는 신경망의 한 종류)을 돌리면서 공정·전압·온도 변화에도 분류 정확도를 지키는 프로세서를 만들었다.[^p7] 최근 논문 목록에는 낸드 플래시 기반 메모리 내 연산 칩(AICAS 2026)도 있다.[^confs]

넷째로, 전기및전자공학부 교수 소개가 드는 **전원 회로**도 다룬다.[^ee] 대표 논문에서는 전자기적으로 결합한 발진기로 전력을 옮기는 4:1 직류-직류 변환기(직류 전압을 다른 크기의 직류 전압으로 바꾸는 회로)를 칩 안에 모두 넣어 만들었다.[^p8] 최근 논문 목록에는 공정·전압·온도 변화에 둔감한 전류 기준 회로(IEEE Journal of Solid-State Circuits, 2024), 출력 커패시터 없이 동작하는 LDO 레귤레이터(입력과 출력의 전압 차가 작아도 일정한 전압을 내는 전원 회로, IEEE Transactions on Circuits and Systems I, 2023), 전압 기준과 전류 기준을 한 회로에서 내는 기준 회로(IEEE Transactions on Circuits and Systems II, Early Access)도 있다.[^journals] 연구실은 해외 연구 기관과도 협력한다. 국제 협력 페이지는 University of Columbia(기계학습), ETH Zürich(저전력 센서), University of Michigan(초저전력 회로), IMEC(생체 의료 시스템)에 학생을 보낸 파견 연구를 적는다.[^intl]

## 주요 연구 주제

### 1. 고속 통신·메모리 인터페이스와 클럭 회로

클럭 곱셈기와 PLL, 밀리미터파 국부 발진기, DRAM 인터페이스와 칩 사이 유선 송수신기(PAM-4).[^hs][^p1][^p2][^p3] 대표 논문 1–3.

### 2. 센서·생체 신호용 저전력 회로

착용형 심전도 증폭기, PPG 센서, 정전 용량 센서 인터페이스, 칩 위 온도 센서.[^lp][^p4][^p5] 대표 논문 4, 5.

### 3. 인공지능 계산과 메모리 회로

음성 키워드 인식 칩, 아날로그 계산 신경망 프로세서, 낸드 플래시 회로.[^ml][^p6][^p7] 대표 논문 6, 7.

### 4. 전원 공급과 기준 회로

칩 안 직류-직류 변환기, LDO 레귤레이터, 기준 전압·전류 회로.[^ee][^p8][^journals] 대표 논문 8.

## 대표 논문

랩 Publication 페이지의 Journals 칸에 실린 2021–2026년 학술지 논문 가운데 조성환 교수가 마지막 저자인 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^journals] |
|---|---|---|---|---|
| 1 | 2024 | [A 7.5-GHz Subharmonic Injection-Locked Clock Multiplier Featuring a 120× Multiplying Factor and 92.3-fs RMS Jitter Including Reference Spur](https://doi.org/10.1109/jssc.2024.3465436) · IEEE Journal of Solid-State Circuits | 기준 신호를 주입해 발진기를 붙잡는 방식의 클럭 곱셈기(낮은 주파수의 기준 신호로 그 배수 주파수의 클럭을 만드는 회로)에서, 지터(클럭 신호의 시점이 흔들리는 정도)를 줄이면서 기준 스퍼(기준 주파수 때문에 생기는 원치 않는 주파수 성분)도 억제하는 회로를 제안했다. 기준 신호를 넣는 일을 리셋과 회복 두 동작으로 나눠, 리셋 때는 전압 제어 발진기(VCO, 걸린 전압에 따라 주파수가 바뀌는 신호 발생 회로)의 출력끼리 이어 쌓인 지터를 없애고, 회복 때는 리셋으로 일그러진 파형을 되돌린다. 기준 스퍼를 줄이려고 발진기 주파수, 회복 크기, 회복 시점을 보정 루프로 맞추고 보정 회로 자체의 오프셋도 없앴다. 28nm CMOS 공정으로 만든 칩은 62.5MHz 기준 신호로 7.5GHz 클럭을 만들면서 rms 지터 67.7fs와 기준 스퍼 −56.6dBc를 얻었고 전력은 2.33mW를 썼다.[^p1] | 1저자 H. Choi, 마지막 저자 조성환 |
| 2 | 2026 | [A Fast-Settling mm-Wave LO With I/Q-Calibrated SSB Mixer and Frequency-Tuned ILO Filter Achieving Sub-ns Settling Time and −56 dBc Spur](https://doi.org/10.1109/jssc.2025.3634591) · IEEE Journal of Solid-State Circuits | 반송파 주파수를 차례로 바꿔 가며 쓰는 OFDM(여러 주파수에 데이터를 나눠 싣는 통신 방식)을 위해, 주파수를 빠르게 바꾸고 곧바로 안정되는 60GHz 국부 발진기(LO, 송수신 회로가 주파수를 옮길 때 쓰는 기준 신호를 만드는 회로)를 만들었다. 단측파대(SSB) 믹서로 주파수를 즉시 건너뛰게 하고, 주입 고정 발진기(ILO)를 좁은 대역만 통과시키는 필터로 써서 믹서가 만드는 스퍼를 줄였다. 주입 고정이 잘 되고 스퍼가 최대한 줄도록 ILO의 고유 공진 주파수를 동작 중에 도는 주파수 조정 루프로 목표 주파수에 맞추고, 믹서 입력의 I/Q 신호도 동작 중에 보정해 스퍼를 더 줄였다. 밀리미터파 전압 제어 발진기에서 신호 크기 변화가 주파수 변화로 바뀌는 현상은 커패시턴스를 상쇄한 버퍼로 줄여 위상 잡음을 개선했다. 28nm CMOS로 만든 시제품은 1ns보다 짧은 정착 시간, 최악 조건 −56dBc의 스퍼, rms 지터 60.3fs를 얻었고 전력은 73.1mW를 썼다.[^p2] | 1저자 J. Oh, 마지막 저자 조성환 |
| 3 | 2026 | [A 12-Gb/s Source-Synchronous Single-Ended PAM-4 Transceiver With Background Adaptive Crosstalk Equalization in 28-nm CMOS](https://doi.org/10.1109/jssc.2026.3712021) · IEEE Journal of Solid-State Circuits | 선 하나로 신호를 보내는 단일 종단 PAM-4(전압을 네 단계로 나눠 한 번에 두 비트를 보내는 방식) 인터페이스에서, 이웃 선의 신호가 새어 드는 누화(크로스토크)를 환경이 바뀌어도 정확히 지우도록 동작 중에 스스로 맞춰지는 누화 등화 기법을 제시했다. 최소 평균 제곱(LMS) 적응 루프가 누화 등화기를 조정하는데, 데이터와 함께 보내는 클럭(소스 동기 클럭)을 데이터 신호와 상관없는 간섭원 기준으로 쓴다. 수신부 앞단에는 동작 중에 보정되는 트랜스임피던스 증폭기(전류를 전압으로 바꾸는 증폭기)를 두어 입력과 출력의 직류 전압 차이를 없애고 PAM-4 신호의 선형성을 높였다. 28nm CMOS로 만든 12Gb/s 송수신기는 누화를 지운 뒤 비트 오류율 10⁻¹²에서 0.11UI(UI는 신호 심벌 하나가 차지하는 시간)의 눈 열림(받은 신호에서 값을 구별할 수 있는 여유)을 얻었고, −25°C부터 125°C까지 눈 가운데 열림의 변화를 0.02UI와 2.38mV 안으로 묶었다.[^p3] | 1저자 D. Shin, 마지막 저자 조성환 |
| 4 | 2023 | [A 43.3-μW Biopotential Amplifier With Tolerance to Common-Mode Interference of 18 Vpp and T-CMRR of 105 dB in 180-nm CMOS](https://doi.org/10.1109/jssc.2022.3185988) · IEEE Journal of Solid-State Circuits | 전극의 접촉 임피던스(전극과 몸이 맞닿은 곳의 전기 저항 성분)가 서로 달라도 총 공통 모드 제거비(TCMRR, 두 입력에 똑같이 들어오는 잡음을 얼마나 걸러 내는지 나타내는 값)가 크고, 큰 공통 모드 간섭을 견디는 심전도 증폭기를 제안했다. 전하 펌프로 공통 모드를 누르는 루프와 나란히 TCMRR을 높이는 적응 루프를 두어, 각 접촉 임피던스로 흐르는 간섭 전류를 조절해 공통 모드 간섭이 심전도 신호 성분(차동 모드)으로 바뀌는 것을 최소로 했다. 접촉 임피던스가 바뀌어도 빠르게 따라가 심전도를 안정적으로 얻도록 적응 루프를 빨리 정착시키는 기법도 제안했다. 180nm CMOS로 만든 시제품 칩은 접촉 임피던스가 최대 30% 달라도 105dB가 넘는 TCMRR을 얻었고, 60Hz에서 18Vpp의 공통 모드 간섭을 견뎠으며, 입력 환산 잡음(회로 안의 잡음을 입력 신호 크기로 환산한 값) 1.90µVrms에 전력 43.3µW를 썼다.[^p4] | 1저자 N. Koo, 마지막 저자 조성환 |
| 5 | 2023 | [A 3.68 aFrms Resolution Continuous-Time Bandpass ΔΣ Capacitance-to-Digital Converter for Full-CMOS Sensors in 0.18 μm CMOS](https://doi.org/10.1109/jssc.2022.3222229) · IEEE Journal of Solid-State Circuits | 표준 CMOS 공정만으로 만드는 센서를 위해, 정전 용량(두 도체 사이에 전하를 담는 능력)을 아주 높은 해상도와 에너지 효율로 디지털 값으로 바꾸는 4차 연속 시간 대역 통과 델타-시그마 변환기(CDC)를 만들었다. 해상도를 높이려고 신호를 일정 간격으로 끊어 처리하는 이산 시간 방식 대신 연속 시간 방식을 써서 열잡음 한계를 넘었고, 저역·고역 통과형 대신 대역 통과형 델타-시그마 변조기를 써서 전력을 아꼈다. 변조기 입력단에는 열잡음이 적고 구조가 단순한 전하 영역 디지털-아날로그 변환기를 제안했고, 인버터 기반 증폭기로 전력을 줄이면서 이득 증폭 회로를 더해 직류 이득을 높였다. 0.18µm CMOS로 구현한 변환기는 3.68aFrms의 해상도와 183dB의 Schreier 성능 지수를 얻어, 최근 비교 대상 변환기들보다 성능 지수를 3.3dB 높였다고 보고했다.[^p5] | 1저자 S. Park, 마지막 저자 조성환 |
| 6 | 2026 | [A 7.5-μW 35-Keyword End-to-End Keyword Spotting System With Random Augmented On-Chip Training](https://doi.org/10.1109/jssc.2026.3660634) · IEEE Journal of Solid-State Circuits | 저전력으로 동작하는 키워드 인식(정해진 음성 명령어를 알아듣는 기능) 칩에는 두 어려움이 있다. 알아들을 키워드가 늘면 회로가 복잡해지고 전력이 크게 늘며, 대부분 영어 원어민 자료로 학습해 원어민이 아닌 사용자의 말에서는 정확도가 떨어진다. 35개 키워드를 단순한 구조로 알아듣고, 사용자의 억양에 맞추도록 칩 안에서 직접 학습하는 저전력 키워드 인식 시스템을 만들었다. 무작위 데이터 증강을 써서 키워드마다 녹음 하나만으로 학습한다. 28nm CMOS로 만든 시제품은 9개 나라 화자 20명의 음성이 담긴 억양 음성 명령 데이터셋(ASCD)에서 평균 정확도 91.2%를 얻었고, 인식할 때 5.31µW, 학습할 때 7.49µW를 썼다.[^p6] | 1저자 H.-J. Lee, 마지막 저자 조성환 |
| 7 | 2024 | [A 44.2-TOPS/W CNN Processor With Variation-Tolerant Analog Datapath and Variation Compensating Circuit](https://doi.org/10.1109/jssc.2023.3321643) · IEEE Journal of Solid-State Circuits | 에너지 효율을 높이려고 아날로그 계산을 쓰는 합성곱 신경망(CNN) 프로세서에는 두 문제가 있다. 층과 층 사이에서 데이터 변환을 자주 해 효율이 떨어지고, 아날로그 회로가 공정·전압·온도(PVT) 변화에 약해 계산 오류가 생긴다. 아날로그 메모리를 넣은 아날로그 데이터 경로로 층 사이 데이터 변환이 필요 없게 한 CNN 프로세서를 제안했다. 계산 오류를 줄이려고 아날로그 메모리와 아날로그 계산 회로를 PVT 변화에 성능이 흔들리지 않게 설계했고, 변화를 보상하는 회로도 더했다. 28nm CMOS로 만든 시제품은 아날로그 데이터 경로에서 437.9TOPS/W, 시스템 전체에서 44.2TOPS/W(전력 1와트로 1초에 하는 연산 수를 조 단위로 센 값)의 에너지 효율을 냈고, 공급 전압 ±10%와 −20°C–85°C의 온도 변화에서도 분류 정확도 변화를 0.5%포인트 안으로 유지했다.[^p7] | 1저자 J.-O. Seo, 마지막 저자 조성환 |
| 8 | 2025 | [A Fully Integrated 4:1 DC–DC Converter With Series Transmission and Parallel Reception Through Electromagnetically Coupled Class-D LC Oscillators](https://doi.org/10.1109/jssc.2025.3566479) · IEEE Journal of Solid-State Circuits | 직류 전압을 다른 크기의 직류 전압으로 바꾸는 4:1 직류-직류 변환기를, 전자기적으로 결합한 D급 LC 발진기(코일과 커패시터로 된 발진 회로)로 칩 안에 모두 넣어 만들었다. 직렬로 보내고 병렬로 받는(STPR) 구조로 효율을 크게 잃지 않고 변환 비율을 늘릴 수 있게 했다. 전력을 보내는 발진기 셋과 받는 발진기 하나를 칩 위의 4단 적층 변압기 하나로 한꺼번에 결합해 배치를 작게 하고 면적과 복잡도를 줄였다. 28nm CMOS로 만든 시제품은 4:1 변환에서 피크 효율 74.5%를 내고 3.6V까지의 입력을 받으며, 피크 전력 밀도 0.78W/mm²를 내면서도 그때 효율을 67% 넘게 유지했다. 1:4 승압과 4:3 강압 변환도 지원해 피크 효율 74.3%와 90.3%, 피크 전력 밀도 0.68W/mm²와 3.27W/mm²를 냈다.[^p8] | 1저자 D. Cho, 마지막 저자 조성환 |

## 교수와 전문 분야

조성환 교수는 KAIST에서 전기공학 학사(1995)를, 미국 MIT에서 전기공학·컴퓨터과학 석사(1997)와 박사(2002)를 받았다.[^prof] 1999년 여름에는 IBM T.J. Watson Research Center에서 일했고, 2002년 Engim Inc.에 들어가 IEEE 802.11(a)(b)(g) 무선 랜용 데이터 변환기, PLL, 전압 제어 발진기 설계에 참여했으며, 2003–2004년에는 공익근무요원으로 병역을 이행했다.[^prof] 2004년 11월부터 KAIST 전기및전자공학부에 있으며 조교수(2004–), 부교수(2009–), 교수(2014–)를 거쳤다.[^prof] 미국 Santa Clara의 Marvell에서 방문 연구원으로 와이파이용 고효율 RF 전력 증폭기를 연구했고, 2016–2017년 영국 런던의 Google에서 방문 연구원으로 기계학습과 착용형 기기를 쓴 심혈관 건강 관리를 탐구했다.[^prof] 전기및전자공학부 부학부장(2020–2021)과 회로 디비전 의장(2018–2020)을 지냈고, 2022년부터 반도체시스템공학과장을 맡고 있다.[^prof] 전기및전자공학부 교수 목록은 직위를 교수로 적고 IEEE 석학회원, KEPCO 석좌교수, 반도체시스템공학과장을 함께 적는다.[^eelist]

학술 활동으로는 IEEE Journal of Solid-State Circuits 부편집장(2016–2017)과 객원 편집자(2009년 11월), IEEE Transactions on Circuits and Systems I 부편집장(2010–2011, 2014–2015)을 지냈다. ISSCC(국제 고체 회로 학회)의 학생 연구 미리보기(SRP) 의장(2017–2018)과 공동 의장(2012–2016), 집행위원회 간사(2016–2018), A-SSCC의 기술 프로그램 위원장(2022)과 공동 위원장(2021), 데이터 변환기 분과 위원장(2012–2016), 기술 프로그램 부위원장(2008)을 맡았고, ISSCC·Symposium on VLSI Circuits·A-SSCC·ISLPED·ASPDAC의 기술 프로그램 위원을 지냈다.[^prof] 수상과 영예로는 KEPCO 석좌교수(한전석좌교수), Institute of Semiconductor Engineers의 해동학술상(2023), IEEE Fellow, IEEE Solid-State Circuits Society Distinguished Lecturer(2015–2016), ISSCC Takuo Sugano Award for Outstanding Far-East Paper(2012), IEEE Transactions on Circuits and Systems Guillemin-Cauer Best Paper Award(2009), 대전시 이달의 과학기술인(2010년 7월), KAIST Outstanding Lecturer Award(2008)와 전기및전자공학부 Outstanding Lecturer Award(2005, 2014, 2019, 2021)를 적는다.[^prof] People 첫 페이지에 실린 교수 소개는 2012년과 2009년 논문상을 공동 수상(Co-recipient)으로 적고, 두 페이지의 학생 수상 칸에도 이 두 상이 학생 이름과 함께 실려 있다.[^people][^prof] 랩 소식은 2023년 12월 Solid-State Circuits Society에서 IEEE Fellow로 선임되고 같은 달 해동학술상을 받았으며, 2024년 2월 KEPCO 석좌교수로 임명됐다고 적는다.[^home]

교수 소개는 연구 관심을 통신, 센서, 메모리를 위한 아날로그·혼성 신호 회로로 요약한다.[^prof] 전기및전자공학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Integrated Circuits & Semiconductor Systems, Photonics로, 디비전을 Circuit로 적고,[^ee] 반도체시스템공학과 교수 소개는 연구분야를 반도체 시스템 및 집적회로로, 연구를 통신·생체 응용·신기술을 위한 아날로그·혼성 신호 집적회로 설계로 적는다.[^sse] 랩 Journals 목록에서 2021년 이전 논문은 시간-디지털 변환기, 전압 제어 발진기 기반 아날로그-디지털 변환기, 주파수 합성기와 PLL, 생체 임피던스를 쓴 맥파 전달 속도·호흡 센서, 칩 위 온도 감시 같은 주제를 다룬다.[^journals]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 클럭 곱셈기·국부 발진기·유선 송수신기 같은 고속 통신·인터페이스 회로다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 심전도 증폭기와 정전 용량 변환기 같은 센서용 저전력 측정 회로다(대표 논문 4, 5).[^p4][^p5] 셋째, 키워드 인식과 신경망 계산을 낮은 전력으로 하는 인공지능 칩이다(대표 논문 6, 7).[^p6][^p7] 넷째, 칩 안에 모두 넣은 직류-직류 변환기 같은 전원 회로다(대표 논문 8).[^p8]

## 응용 분야

연구실은 고속 아날로그 회로가 유선·무선 통신을, 저전력 아날로그 회로가 배터리 관리와 생체 의료를 포함한 센서 응용을 향한다고 적는다.[^home] 연구 페이지는 DRAM 인터페이스, 레이더용 밀리미터파 주파수 합성기,[^hs] 착용형 건강관리 시스템과 사물인터넷용 센서 SoC, 압력 센서 같은 정전 용량 감지 소자,[^lp] 상시 동작하는 센서 내장 기계학습 시스템과 낸드 플래시 메모리[^ml]를 응용 대상으로 든다. 대표 논문은 반송파를 차례로 바꾸는 OFDM 통신,[^p2] 심전도 측정,[^p4] 원어민이 아닌 사용자의 억양에 맞춘 음성 명령 인식[^p6]을 대상으로 한다. 졸업생의 진로로는 Samsung Electronics, SK Hynix, Marvell, Broadcom, Qualcomm, Apple, SAIT, Rebellions, ETRI, KARI, MIT와 DGIST·단국대학교·ETH Zurich·KAIST·NYU Abu Dhabi의 교원 등이 있다.[^alumni]

## 구성원

2026년 10월 22일 랩 People 페이지 기준이다. Ph.D. Students 칸의 10명과 M.S. Students 칸의 7명이며, 과정은 칸 이름을 옮겼다. Ph.D. Students 칸 첫 줄의 Donghyeok Cho는 이름 앞에 (Post-doc)이 붙어 있어 박사후연구원으로 적었고, Changmin Jeon의 괄호 안 Student Representative(학생 대표)는 페이지 표기다.[^phd][^ms] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Donghyeok Cho | 박사후연구원 | 8 |
| Giwoo Lee | 박사과정 |  |
| Dabin Hong | 박사과정 |  |
| Kuy Youn Chung | 박사과정 | 3 |
| Seoyeong Yang | 박사과정 |  |
| Kyunghoon Pyo | 박사과정 | 6 |
| Jongseok Jung | 박사과정 |  |
| Hangyul Yoon | 박사과정 |  |
| Woohyun Hwang | 박사과정 |  |
| Changmin Jeon | 박사과정 (Student Representative) |  |
| Sujeong Yoon | 석사과정 |  |
| Jaejun Lee | 석사과정 |  |
| Ahryung Kim | 석사과정 |  |
| Woojae Sung | 석사과정 |  |
| Tae Gyu Yang | 석사과정 |  |
| Woong Bee Kim | 석사과정 |  |
| Jinseok Kim | 석사과정 |  |

## 졸업생과 이전 구성원

랩 People 페이지 Alumni 칸의 박사 27명(2008–2026년)과 석사 41명(2006–2026년)이다. 학위와 연도는 랩 표기이고, 진로는 랩이 적은 Affiliation이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yeonwoo Ku | Ph.D. (2008) | Samsung Electronics |
| Joonhee Lee | Ph.D. (2010) | Samsung Electronics |
| Jaewook Kim | Ph.D. (2011) | KIST |
| Junghyup Lee | Ph.D. (2011) | DGIST, Professor |
| Dongmin Park | Ph.D. (2011) | Qualcomm, USA |
| Jaewon Lee | Ph.D. (2012) | SK Hynix, USA |
| Pyoungwon Park | Ph.D. (2012) | Apple, USA |
| Kwangseok Kim | Ph.D. (2013) | Broadcom, USA |
| Woojae Lee | Ph.D. (2014) | Samsung Electronics |
| Wonsik Yu | Ph.D. (2015) | Quorvo, Ireland |
| Younghwa Kim | Ph.D. (2016) | Samsung Electronics |
| Youngwoo Jo | Ph.D. (2018) | Samsung Electronics |
| Hyojun Kim | Ph.D. (2020) | KARI |
| Dongin Kim | Ph.D. (2020) | Samsung Electronics |
| Yongjo Kim | Ph.D. (2021) | Broadcom |
| Seongseop Lee | Ph.D. (2021) | SK Hynix |
| Nahmil Koo | Ph.D. (2021) | Univ. of Dankuk, Assistant Professor |
| Myungjun Kim | Ph.D. (2022) | Samsung Electronics |
| Sujin Park | Ph.D. (2022) | ETRI |
| Hyunsik Jeong | Ph.D. (2022) | SK Hynix |
| Jin-O Seo | Ph.D. (2023) | Rebellions |
| DongArm Shin | Ph.D. (2025) | Marvell |
| Han Gil Choi | Ph.D. (2025) | Samsung Electronics |
| Hyuk Jin Lee | Ph.D. (2025) | Samsung Electronics |
| Donghwan Kim | Ph.D. (2026) | Marvell |
| Jaewon Oh | Ph.D. (2026) | SAIT |
| Pangi Park | Ph.D. (2026) | MIT |
| Somyung Ha | M.S. (2006) | NYU @ Abu Dhabi, Associate Professor |
| Taekwang Jang | M.S. (2008) | ETH Zurich, Associate Professor |
| Sungjun Kim | M.S. (2008) | Samsung Electronics |
| Younggyu Yoon | M.S. (2008) | KAIST, Associate Professor |
| Sehyung Jeon | M.S. (2009) | Cirrus Logic |
| Wookon Son | M.S. (2009) | 경북대학교 의과대학 |
| Minchang Cho | M.S. (2010) | Apple |
| Sungjin Kim | M.S. (2010) | Ayar Labs |
| Jaehyun Han | M.S. (2010) | Kim & Chang Law Firm |
| Sungpah Lee | M.S. (2011) | Ringle |
| Kangyeop Choo | M.S. (2011) | Qualcomm |
| Hyoungtaek Choi | M.S. (2012) | Hyundai Mobis |
| Jinwoo Sang | M.S. (2012) | Agency for Defense Development |
| Jungho Kim | M.S. (2014) | Samsung Electronics |
| Gyusik Kim | M.S. (2014) | Samsung Electronics |
| Zilong Han | M.S. (2015) | Tyndall National Institute |
| Minyoung Kang | M.S. (2015) | Samsung Electronics |
| John Kang | M.S. (2015) | Northrop Grumman, Washington, D.C. |
| SungRok Jeon | M.S. (2015) | Pusan National University School of Medicine |
| Hyunik Kim | M.S. (2015) | Samsung Electronics |
| Seonggyu Lee | M.S. (2016) | SK Hynix |
| Jinsoo Choi | M.S. (2016) | Samsung Research |
| Jonghwa Lee | M.S. (2016) | Broadcom Inc |
| Jusung Lee | M.S. (2017) | Samsung Electronics |
| GeonHwi Lee | M.S. (2017) | SK Hynix |
| Jinseok Lee | M.S. (2017) | Encharge AI |
| Jihwan Kim | M.S. (2018) | Samsung Electronics |
| Dohun Jang | M.S. (2018) | Samsung Electronics |
| Dong Hee Kim | M.S. (2019) | Pusan National University, School of Medicine |
| Dongkyun Jung | M.S. (2019) | Samsung Electronics |
| Yeonwook Jung | M.S. (2021) | Samsung Electronics |
| Kyunghyun Kim | M.S. (2022) | Samsung Electronics |
| JunSeok Hong | M.S. (2022) | Samsung Electronics |
| Yubin Kim | M.S. (2022) | SK Hynix |
| Hyein Yoon | M.S. (2022) | Samsung Electronics |
| Youngjae Son | M.S. (2024) | Samsung Electronics |
| Kiwon Lee | M.S. (2025) | Samsung Electronics |
| Sihoon Yang | M.S. (2025) | SK Hynix |
| Woojin Lee | M.S. (2026) | SK Hynix |
| Juhwan Lee | M.S. (2026) | Samsung Electronics |
| Seonghoon Jeong | M.S. (2026) | SK Hynix |

## 최근 논문 목록 (2021–2026)

랩 Publication 페이지 Journals 칸의 2021–2026년 학술지 논문 18편과 연도 없이 Early Access(정식 호 수록 전 온라인 공개)로 적힌 학술지 논문 2편, Conferences 칸의 2021–2026년 학회 논문 21편이다. 연도는 각 줄 끝의 연도이고, Early Access 2편은 연도가 적혀 있지 않아 맨 끝에 따로 두었다. 각 줄은 랩 목록 표기 그대로이며, 줄 끝 괄호 안의 말(중견연구, PIM 등)도 랩이 적은 것이다.[^journals][^confs]

**2026**

- H.-J. Lee, K. Pyo, T. Jang, M. Seok, S.H. Cho, "A 7.5-μW 35-Keyword End-to-End Keyword Spotting System With Random Augmented On-Chip Training,"  IEEE Journal of Solid-State Circuits, vol. 61, no. 8, 2026. (명령어 인식)
- J. Oh, C. So, H. Kim, S. Hong, S.H. Cho, "A Fast-Settling mm-Wave LO With I/Q-Calibrated SSB Mixer and Frequency-Tuned ILO Filter Achieving Sub-ns Settling Time and -56 dBc Spur",  IEEE Journal of Solid-State Circuits, vol. 61, no. 7, 2026. (중견연구&글로벌공동연구)
- D. Hong, K. Lee, P. Park, S.H. Cho, "An Analog Front-End IC for Electrochemical Impedance Spectroscopy of Li-Ion Batteries Achieving 371-μΩ/0.4° RMSE in 180-nm CMOS," IEEE Asian Solid-State Circuits Conference (A-SSCC), 2026.
- H.-J. Lee, K. Pyo, S.H. Cho, "A 15.7TOPS/W NAND Flash-Based Process-In-Memory Featuring a Time-Domain Computation Unit,"  IEEE Int’l Conference on Artifical Intelligence Circuits and Systems (AICAS), 2026. (IITP 디지털글로벌연구지원)

**2025**

- D. Shin, Y. Ji, S.H. Cho and T. Jang, “Energy-Efficient Data Transmitters Achieving Energy Per Bit Beyond CV2 Limitation”, IEEE Transactions on Circuits and Systems - I, vol. 72, no. 12, 2025. (IITP글로벌&글로벌 공동연구)
- D. Cho, T. Jang and S.H. Cho, “A Fully Integrated 4:1 DC–DC Converter With Series Transmission and Parallel Reception Through Electromagnetically Coupled Class-D LC Oscillators”, IEEE Journal of Solid-State Circuits, vol. 60, no. 10, 2025. (중견연구&IITP글로벌)
- D. Shin, K. Chung, S. Yang, S.H. Cho, "A 12-Gb/s Source-Synchronous Single-Ended PAM-4 Transceiver with Background Adaptive Crosstalk Equalizer," IEEE Asian Solid-State Circuits Conference (A-SSCC), 2025. (Samsung Memory Division)
- G. Lee†, D. Kim†, S.H. Cho, "A Dual-Mode Sense Amplifier with Switched-Capacitor Amplification for Bitline Crosstalk Immunity in 3D DRAM," IEEE Asian Solid-State Circuits Conference (A-SSCC), 2025. (Samsung Memory Division)
- D. Kim, G. Lee, S.H. Cho, "A 3-Bit Offset-Canceled Sense Amplifier Using a Single-Capacitor SAR ADC for 3D DRAM," IEEE Asian Solid-State Circuits Conference (A-SSCC), 2025. (중견연구)
- K. Chung, Y. Kim, D. Shin, S.H. Cho, "A 12-Gb/s Single-Ended Transmitter with Echo-Canceling FFE for Multi-drop Bus in 28nm CMOS,"  IEEE Symposium on VLSI Circuits, 2025. (IITP 디지털글로벌연구지원)
- J. Oh, C. So, H. Kim, S. Hong, S.H. Cho, "A 60GHz I/Q-Calibrated SSB-Mixer-Based LO with Sub-ns Settling Time and -56dBc Worst-Case Spur Using ILO Filter in 28nm CMOS,"  IEEE Int’l Solid-State Circuits Conference (ISSCC), 2025. (중견연구)
- H.-J. Lee, K. Pyo, T. Jang, M. Seok, S.H. Cho, "A 13.5μW 35-Keyword End-to-End Keyword Spotting System Featuring Personalized On-Chip Training in 28nm CMOS,"  IEEE Int’l Solid-State Circuits Conference (ISSCC), 2025. (명령어 인식)

**2024**

- H. Choi, and S.H. Cho, “A 7.5GHz Subharmonic Injection-Locked Clock Multiplier Featuring a 120x Multiplying Factor and 92.3fs RMS Jitter Including Reference Spur”, IEEE Journal of Solid-State Circuits, vol. 59, no. 12, 2024. (IITP글로벌&글로벌 공동연구)
- P. Park, J. Lee and S.H. Cho, “A PVT-Insensitive Sub-ranging Current Reference Achieving 11.4-ppm/°C from −20 °C to 125 °C”, IEEE  Journal of Solid-State Circuits, vol. 59, no. 12, 2024. (PIM)
- J. Oh, and S.H. Cho, “A 0.001-mm2, 1.15-11 GHz Background Quadrature Phase and Duty-Cycle Error Corrector Using a NAND-based Phase Detector in 28-nm CMOS”, IEEE Solid-State Circuits Letters, vol. 7, pp. 247-250, 2024. (PIM)
- Y. Kim, T. Jang, S.H. Cho, "A Jitter Programmable Digital Bang-Bang PLL Using PVT-Invariant Stochastic Jitter Monitor" IEEE J. Solid-State Circuits, vol. 59, no. 10, 2024. (글로벌 공동연구&IITP글로벌)
- J. Seo, M. Seok, S.H. Cho, "A 44.2-TOPS/W CNN Process With Variation-Tolerant Analog Datapath and Variation Compensating Circuit", IEEE J. Solid-State Circuits, vol. 59, no. 5, 2024. (PIM & 글로벌 공동연구)
- D. Cho, T. Jang, S.H. Cho, "A Fully Integrated 4:1 DC-DC Converter Using Electromagnetically Coupled Class-D LC Oscillators Achieving 74.5% Peak Efficiency and 0.78W/mm2 Peak Power Density,"   IEEE Asian Solid-State Circuits Conference (A-SSCC), 2024. (명령어 인식)
- H. Choi, S.H. Cho, “A 7.5GHz Subharmonic Injection-Locked Clock Multiplier with a 62.5MHz Reference, -259.7dB FoMJ, and -56.6dBc Reference Spur,” IEEE Int’l Solid-State Circuits Conference (ISSCC), 2024. (명령어 인식, DRAM PIM)
- P. Park, J. Lee, S.H. Cho, “A PVT-Insensitive Sub-Ranging Current Reference Achieving 11.4ppm/°C from -20°C to 125°C,” IEEE Int’l Solid-State Circuits Conference (ISSCC), 2024. (명령어 인식, 중견연구)

**2023**

- P. Park, W. Lee, S.H. Cho, "An Adaptive Filter Based Motion Artifact Cancellation Technique Using Multi-wavelength PPG for Accurate HR Estimation" IEEE Trans. on Biomedical Circuits and Systems, vol. 17, no. 5, 2023.(IITP RADAR & 포공 바이오센터)
- M. Kim, S.H. Cho, "An Output-Capacitorless Analog LDO Featuring Frequency Compensation of Four-Stage Amplifier" IEEE Transactions on Circuits and Systems - I, vol. 70, no. 2, 2023. (이어달리기 & PIM)
- S. Park, H. Chae, S.H. Cho, "A 3.68aFrms Resolution Continuous-Time Bandpass ΔΣ Capacitance-to-Digital Converter for Full-CMOS Sensors in 0.18μm CMOS", IEEE J. Solid-State Circuits, vol. 58, no. 6, 2023. (중견연구, IITP RADAR)
- Y. Jung, S. Lee, H. Kim, S.H. Cho, "A Supply Noise Induced Jitter Canceling Adaptive Filter for LPDDR5 Mobile DRAM" IEEE J. Solid-State Circuits, vol. 58, no. 1, 2023. (이어달리기 & PIM)
- N. Koo, H. Kim, S.H. Cho, "43.3µW Biopotential Amplifier with Tolerance to Common-Mode Interference of 18Vpp and T-CMRR of 105dB in 180nm CMOS" IEEE J. Solid-State Circuits, vol. 58, no. 2, 2023. (이어달리기 & 중견연구)
- Y. Kim, T. Jang, S.H. Cho, “A Jitter-Programmable Bang-Bang Phase-Locked Loop using PVT Invariant Stochastic Jitter Monitor,” IEEE Asian Solid-State Circuits Conference (A-SSCC), 2023.
- W. Choi†, Y. Chen†, D. Kim†, S. Weaver, T. Schlotter, C. Livanelioglu, J. Liao, R. Incandela, P. Davami, S. Arjmandpour, S.H. Cho, T. Jang, "A 1,024-Channel, 64-Interconnect, Capacitive Neural Interfaces Using a Cross-Coupled Microelectrode Array and 2-Dimensional Code-Division Multiplexing" IEEE Symposium on VLSI Circuits, 2023. (DRAM PIM)

**2022**

- S. Park, J-H. Seol, L. Xu, S.H. Cho, D. Sylvester, and D. Blaauw, "A 43 nW, 32 kHz, A 43 nW, 32 kHz, ±4.2 ppm Piecewise Linear Temperature-Compensated Crystal Oscillator With ΔΣ-Modulated Load Capacitance", IEEE J. Solid-State Circuits, vol. 57, no. 4, 2022. (중견연구)
- D. Kim, and S.H. Cho, “Adaptive Clocking Using Supply Tracking Clock Modulator With Background-Calibrated Supply Sensitivity”,  IEEE Solid-State Circuits Letters, vol. 5, 2022. (중견연구, IITP RADAR)
- P. Park, D. Cho, S.H. Cho, "A Low-power Sleep Apnea Monitoring IC with a Duty-Recovered Body Channel Communication Receiver" IEEE Asian Solid-State Circuits Conference (A-SSCC), 2022. (DRAM PIM)
- J.-O. Seo, M. Seok, S.H. Cho, "ARCHON: A 332.7TOPS/W 5b Variation-Tolerant Analog CNN Processor Featuring Analog Neuronal Computation Unit and Analog Memory" IEEE International Solid-State Circuits Conference (ISSCC), 2022. (이어달리기, 글로벌인재양성)
- Y. Jung†, S. Lee†, H. Kim, S.H. Cho, "A Supply-Noise-Induced Jitter-Cancelling Clock Distribution Network for LPDDR5 Mobile DRAM featuring a 2nd-order Adaptive Filter" IEEE International Solid-State Circuits Conference (ISSCC), 2022. (이어달리기)

**2021**

- M. Kim, and S.H. Cho, “A Single BJT Bandgap Reference with Frequency Compensation Exploiting Mirror Pole”,  IEEE J. Solid-State Circuits, vol. 56, no. 10, 2021. (중견연구, IITP 이어달리기)
- N. Koo and S.H. Cho, "A 24.8µW Biopotential Amplifier Tolerant to 15-VPP Common-Mode Interference for Two-Electrode ECG Recording in 180nm CMOS," IEEE J. Solid-State Circuits, vol. 56, no. 2, 2021. (중견연구, IITP 이어달리기)
- D. Kim, S.H. Cho, "An Adaptive Clocking System Using Supply Tracking Clock Modulator with Background Calibrated Supply-Sensitivity in 28nm CMOS" IEEE Asian Solid-State Circuits Conference (A-SSCC), 2021. (-)
- D. Cho, N. Koo, T.K. Jang, S.H. Cho, "An Offset Charge Compensating Biphasic Neurostimulation for Faradaic DC-current Reduction" IEEE International Symposium on Circuit and Systems (ISCAS), 2021. (글로벌 인재양성)
- H. Jeong, S.H. Cho, "An Energy-Efficient Voltage Step-up System for 3D NAND Flash using Charge-Compensating Regulator" IEEE  Symposium on VLSI Circuits, 2021. (이어달리기)
- S. Park, H. Chae, S.H. Cho, "A 3.68aFrms Resolution 183dB FoMS 4th-order Continuous-Time Bandpass ΔΣ Capacitance-to-Digital Converter in 0.18μm CMOS," IEEE  Symposium on VLSI Circuits, 2021. (중견후속연구)
- N. Koo, H. Kim, S.H. Cho, "A 22.6μW Biopotential Amplifier with Adaptive Common-Mode interference Cancellation Achieving Total-CMRR of 104dB and CMI Tolerance of 15VPP in 180nm CMOS," IEEE Int’l Solid-State Circuits Conference (ISSCC), 2021. (중견연구 이어달리기)

**연도 표기 없음**

- P. Park, K. Lee and S. Cho, "A Sub-Ranging All-in-One Reference Achieving 8.8 ppm/°C in Voltage and 26.7 ppm/°C in Current from -40 °C to 125 °C," IEEE Trans. on Circuits and Systems - II: Express Briefs (Early Access). (중견연구)
- D. Shin, K. Y. Chung, S. Yang and S. Cho, "A 12-Gb/s Source-Synchronous Single-Ended PAM-4 Transceiver With Background Adaptive Crosstalk Equalization in 28-nm CMOS," IEEE Journal of Solid-State Circuits, (Early Access). (인공지능반도체대학원)

## 수상

랩 Professor 페이지의 학생 수상 칸(Awards and Fellowships received by students)에서 연도가 2021년 이후인 4건이다. 표기는 랩 그대로다.[^prof]

- 이혁진: KAIST 전기 및 전자공학부 우수 박사학위 논문상 (2025)
- 오재원: 삼성전자 휴먼테크 은상 (2024년)
- 이재준, 황우현: 반도체공학회 회로설계 경진대회 (2024년)
- 박수진: IEEE SSCS Predoctoral Achievement Award (2022년)

## 소식

랩 첫 화면 CCS NEWS 칸과 NEWS 페이지에 실린 2022년 1월–2026년 10월 소식 41건이다. 날짜와 글은 랩 표기 그대로다.[^home][^news]

- OCT 2026 · Pangi's work was accepted to TCAS-II (A Sub-Ranging All-in-One Reference with low TC)
- AUG 2026 · Dabin's work was accepted to ASSCC 2026 (AFE IC for electrochemical impedance spectroscopy of Li-ion batteries)
- JUL 2026 · DongArm's work was accepted to JSSC (12-Gb/s PAM4 transceiver w/ adaptive crosstalk equalizer)
- JUN 2026 · Hyukjin's work was accepted to AICAS (NAND flash PIM with time-domain computation unit)
- FEB 2026 · Hyukjin's work was accepted to JSSC (Keyword Spotting System with On-Chip Training)
- NOV 2025 · Jaewon's work was accepted to JSSC (Low-noise Fast-settling mm-Wave LO)
- AUG 2025 · DongArm's work was accepted to ASSCC 2025 (12-Gb/s PAM4 transceiver w/ adaptive crosstalk equalizer)
- AUG 2025 · Giwoo's work was accepted to ASSCC 2025 (Crosstalk-imune DRAM sense amplifier)
- AUG 2025 · Donghwan's work was accepted to ASSCC 2025 (Multi-bit DRAM sense amplifier)
- JUN 2025 · DongArm's work was accepted to TCAS-I (Energy-efficient data transmitters)
- MAY 2025 · Donghyeok's work was accepted to JSSC (DC-DC converter based on EMLC oscillators)
- APR 2025 · Kuyyoun's work was accepted to VLSI 2025 (12-Gb/s echo-canceling transmitter for multi-drop bus)
- FEB 2025 · Jaewon received Silver Prize in 31st Samsung HumanTech Paper Award.
- DEC 2024 · DongArm passed his Ph.D. defense.
- OCT 2024 · Jaewon's work on mm-wave LO was accepted to ISSCC 2025.
- OCT 2024 · Hyukjin's work on AI chip was accepted to ISSCC 2025.
- SEP 2024 · Pangi received Minister's Award in 25th Korea Semiconductor Design Competition.
- SEP 2024 · Hangil's work was accepted to JSSC (Injection locked clock multiplier)
- AUG 2024 · Pangi's work was accepted to JSSC (Current Reference)
- AUG 2024 · Jaewon's work was accepted to SSC-L (Quadrature and duty-cycle error corrector)
- AUG 2024 · Donghyeok's work on DC-DC converter was accepted to ASSCC 2024.
- MAY 2024 · Yong-Jo's work was accepted to JSSC (Jitter programmable PLL)
- FEB 2024 · Prof. SeongHwan Cho has been appointed as the KEPCO Chair Professor.
- DEC 2023 · Prof. SeongHwan Cho received the Haedong Award from the Institute of Semiconductor Engineers.
- DEC 2023 · Prof. SeongHwan Cho has been elevated to IEEE Fellow from the Solid-State Circuits Society.
- NOV 2023 · Kuy Youn attended MEDICA/COMPAMED at Dusseldorf, Germany.
- OCT 2023 · Pangi's work on current reference was accepted to ISSCC 2024.
- OCT 2023 · Hangil's work on low-jitter PLL was accepted to ISSCC 2024.
- SEP 2023 · Jin-O's work was accepted to JSSC (analog machine learning processor)
- AUG 2023 · Dr. Nahmil Koo has been appointed as an assistant professor at Dankook University for his work in biomedical circuit research.
- AUG 2023 · Pangi's work was accepted to TBioCAS (Motion artifact cancellation using multi-wavelength PPG)
- JUL 2023 · 4 students attended VLSI 2023
- APR 2023 · Donghwan's work was accepted to VLSI 2023 (1024-channel, 64-interconnect neural recording IC)
- NOV 2022 · Jin-O Seo passed his Ph.D. defense
- NOV 2022 · Myungjun's work was accepted to TCAS-I (Output capacitorless LDO using four-stage amplifier)
- NOV 2022 · Sujin's work was accepted to JSSC (High resolution capacitance to digital converter)
- AUG 2022 · Yeonwook's work was accepted to JSSC (Supply noise reduction in clock distribution network of LPDDR5 DRAM)
- AUG 2022 · Pangi's work was accepted to ASSCC 2022 (Sleep Apnea Monitoring IC)
- JUN 2022 · Nahmil's work was accepted to JSSC (ECG sensor with adaptive CMI cancellation)
- JAN 2022 · Sujin's work was accepted to JSSC (32kHz temperature-compensated crystal oscillator)
- JAN 2022 · Sujin Park received IEEE SSCS Predoctoral Achievement Award

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) 나노종합기술원 304호 (우)34141[^home][^contact]
- 교수 사무실: 나노종합기술원(E19) 308호[^ee][^sse]
- 연구실 전화: +82-42-350-5480[^home]
- 교수 전화와 이메일: 042-350-3480, chosta@kaist.ac.kr[^sse][^ee]
[^home]: 연구실 누리집 첫 화면 <https://ccs.kaist.ac.kr/> (연구실 소개, Research Interest, CCS NEWS, 주소·이메일·전화, 2026-10-22 열람)
[^hs]: Research 페이지 「High-speed analog, mixed-signal and RF circuits」 <https://ccs.kaist.ac.kr/research/high-speed-analog-mixed-signal-and-rf-circuits> (2026-10-22 열람)
[^lp]: Research 페이지 「Low-power circuits for sensors」 <https://ccs.kaist.ac.kr/research/low-power-circuits-for-sensors> (2026-10-22 열람)
[^ml]: Research 페이지 「Machine learning and memory」 <https://ccs.kaist.ac.kr/research/machine-learning-and-memory> (2026-10-22 열람)
[^intl]: Research 페이지 「International Collaboration」 <https://ccs.kaist.ac.kr/research/international-collaboration> (2026-10-22 열람)
[^prof]: People 페이지 「Professor」 <https://ccs.kaist.ac.kr/people/professor> (Education, Experience, Brief Bio, Technical Activity, Awards and Honors, 학생 수상, 2026-10-22 열람)
[^people]: People 첫 페이지 <https://ccs.kaist.ac.kr/people> (교수 소개와 학생 수상, 2026-10-22 열람)
[^phd]: People 페이지 「Ph.D.」 <https://ccs.kaist.ac.kr/people/students/ph-d> (2026-10-22 열람)
[^ms]: People 페이지 「M.S.」 <https://ccs.kaist.ac.kr/people/students/m-s> (2026-10-22 열람)
[^alumni]: People 페이지 「Alumni」 <https://ccs.kaist.ac.kr/people/alumni> (Alumni (Ph.D.)·Alumni (M.S.) 칸, 2026-10-22 열람)
[^journals]: Publication 페이지 「Journals」 <https://ccs.kaist.ac.kr/publication/journals> (Journal Papers, 2026-10-22 열람)
[^confs]: Publication 페이지 「Conferences」 <https://ccs.kaist.ac.kr/publication/conferences> (Conference Papers, 2026-10-22 열람)
[^news]: NEWS 페이지 <https://ccs.kaist.ac.kr/news> (CCS NEWS, 2026-10-22 열람)
[^contact]: Contact 페이지 <https://ccs.kaist.ac.kr/contact> (2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(조성환) <https://ee.kaist.ac.kr/professor/12286/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 디비전, 학위, 2026-10-22 열람)
[^eelist]: KAIST 전기및전자공학부 교수(전임교수) 목록 3쪽 <https://ee.kaist.ac.kr/professor-s1/?page=3> (2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 교수 목록 <https://sse.kaist.ac.kr/professor/> (연구분야, 연구실, 위치, 전화, 이메일, 2026-10-22 열람)
[^p1]: H. Choi, S. Cho, IEEE Journal of Solid-State Circuits 59, 3928-3937 (2024). <https://doi.org/10.1109/jssc.2024.3465436> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Oh 외, S. Cho, IEEE Journal of Solid-State Circuits 61, 3435-3448 (2026). <https://doi.org/10.1109/jssc.2025.3634591> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Shin, K. Y. Chung, S. Yang, S. Cho, IEEE Journal of Solid-State Circuits 61, 5409-5420 (2026). <https://doi.org/10.1109/jssc.2026.3712021> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: N. Koo, H. Kim, S. Cho, IEEE Journal of Solid-State Circuits 58, 508-519 (2023). <https://doi.org/10.1109/jssc.2022.3185988> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: S. Park, H. Chae, S. Cho, IEEE Journal of Solid-State Circuits 58, 1657-1666 (2023). <https://doi.org/10.1109/jssc.2022.3222229> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H.-J. Lee 외, S. Cho, IEEE Journal of Solid-State Circuits 61, 4321-4330 (2026). <https://doi.org/10.1109/jssc.2026.3660634> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J.-O. Seo, M. Seok, S. Cho, IEEE Journal of Solid-State Circuits 59, 1603-1611 (2024). <https://doi.org/10.1109/jssc.2023.3321643> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: D. Cho, T. Jang, S. Cho, IEEE Journal of Solid-State Circuits 60, 3464-3473 (2025). <https://doi.org/10.1109/jssc.2025.3566479> 초록 기준(Semantic Scholar 등록 초록).

# 혼합신호IC 및 시스템 연구실 (Mixed-Signal IC and System Group, MICS)

**서울대학교 공과대학 전기·정보공학부 · 김재하 교수**

- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^kor][^prof], 고속 유선 인터페이스[^p6][^p7], 반도체 계측·검사[^p1], 회로·설계 자동화(EDA)[^kor], FPGA·재구성형 하드웨어[^kor]
- 홈페이지: <https://mics.snu.ac.kr/>

> 아날로그·디지털 회로를 함께 설계하고, 회로의 동작을 모델로 표현해 검증하며, 미리 만든 회로 블록을 조합하거나 프로그램으로 기능을 바꾸는 설계 방법을 연구하는 연구실이다.[^kor]

## 무엇을 연구하나

김재하 교수가 이끄는 MICS는 집적회로(IC, Integrated Circuit, 여러 전자 소자를 한 칩에 연결한 회로)의 성능과 설계·검증 방법을 함께 연구한다.[^home][^prof] 중심 대상은 혼성신호 회로(연속값을 다루는 아날로그 회로와 구분된 값을 다루는 디지털 회로를 함께 쓰는 회로)다. 디지털 회로의 설계 자동화에 쓰이던 기술을 아날로그 회로로 확장하는 것이 연구 방향이다.[^kor]

첫째는 **회로를 모델로 표현하고 검증하는 방법**이다. 실제 회로의 동작을 계산 가능한 표현으로 만들고, 그 모델을 실행해 회로의 반응을 구하는 시뮬레이션으로 설계를 살핀다. 연구실에서 개발한 XMODEL은 이 방향의 결과물이다.[^home] 최근 논문에서는 초기 조건이 하나의 값이 아니라 범위로 주어질 때 회로가 도달할 수 있는 상태들을 계산하는 방법을 다뤘다.[^p2][^p3]

둘째는 **셀을 조합하는 아날로그 설계**다. 셀(미리 기능과 성능을 정해 둔 회로 블록)을 연결해 회로를 구성하고, 이를 위한 아날로그 셀 라이브러리 ACL을 IDEC을 통해 배포한다고 소개한다.[^kor] 시간 영역 회로의 예로는 전압 정보를 펄스 사이의 시간 차이로 바꾸고, 그 차이를 단계적으로 처리하는 아날로그-디지털 변환기(ADC, Analog-to-Digital Converter, 연속적인 입력을 디지털 값으로 바꾸는 회로)를 개발했다.[^p4]

셋째는 **프로그래밍으로 기능을 바꾸는 아날로그 회로**다. 연구실은 칩을 새로 제작하지 않고 설정을 바꾸어 다른 아날로그 회로를 구현하는 아날로그 FPGA(Field-Programmable Gate Array, 제작 후 논리 기능과 연결을 설정하는 집적회로의 개념을 아날로그 회로로 확장한 것)를 연구한다. 누리집은 이 구조와 뉴로모픽 회로(신경계의 정보 처리 방식을 본뜬 회로)의 유사성도 설명한다.[^kor]

최근 논문은 이런 설계 방법뿐 아니라 실제 회로의 성능을 분석하고 재는 작업도 보여 준다. 고속 유선 수신기에서는 데이터가 들어오는 시각을 추적하는 동기화와 신호 왜곡을 보정하는 등화를 함께 분석하며,[^p5] 메모리 연결에서는 이웃 배선의 신호가 서로 간섭하는 누화를 줄이는 부호화를 다룬다.[^p8] 또 트랜지스터(전류를 제어하거나 신호를 증폭하는 소자)의 전류 차이를 칩 안에서 측정하는 회로를 만들었다.[^p1]

## 주요 연구 주제

### 1. 회로 모델링과 동작 범위 검증

개별 입력으로 회로를 실행해 보는 데서 나아가, 주어진 초기 상태 범위에서 가능한 동작의 경계를 계산한다. 2021년 논문은 비선형 회로를 구간별 선형 시스템(영역마다 선형 관계로 동작을 나타내는 모델)으로 표현하고, 라플라스 변환(시간 함수를 복소 주파수의 함수로 바꾸는 연산)을 써서 상태 영역의 궤적을 계산했다.[^p3] 2023년 논문은 여러 상태 집합이 같은 경계를 통과할 때 묶어서 처리해 집합 수와 계산 비용이 계속 늘어나는 문제를 다뤘다.[^p2]

### 2. 셀 기반 설계와 시간 영역 신호 처리

미리 정의한 회로 블록을 조합하는 설계와 프로그램으로 바꾸는 아날로그 회로가 연구실의 두 축이다.[^kor] 대표 논문의 ADC는 입력 전압을 시간 차이로 바꾸고 펄스 폭의 차를 이용해 다음 단계에서 처리할 정보를 만든다. 적분·발화 회로(입력을 누적하다가 기준값에 도달하면 펄스를 내는 회로)를 사용하며, 별도의 증폭기 없이 동작하는 구조를 제시했다.[^p4]

### 3. 고속 유선 수신기와 메모리 연결

등화기는 전송 중 생긴 신호 왜곡을 보정한다. 분수 간격 등화기(FSE, Fractionally-Spaced Equalizer, 데이터 기호 간격보다 짧은 간격의 표본을 쓰는 등화기)를 클록·데이터 복구(CDR, Clock and Data Recovery, 수신 신호에서 데이터와 판독 시각을 찾아내는 기능)와 같은 관점에서 분석했다.[^p5] 다른 논문은 수신 신호에 맞춰 등화기의 계수를 학습하고 가능한 데이터열을 평가하는 계산을 줄였다.[^p6] PCIe(Peripheral Component Interconnect Express, 컴퓨터 부품 사이의 고속 직렬 연결 규격) 수신기에서는 여러 전송 속도에 맞춘 동작과 전력 절약을 다뤘다.[^p7] 고대역폭 메모리(HBM, High Bandwidth Memory) 연결에서는 배선 위치에 따라 다른 가중치를 주는 부호화로 누화를 줄였다.[^p8]

### 4. 트랜지스터 특성의 칩 내부 측정

공정 변동(제조 과정에서 문턱전압 등 소자 특성이 달라지는 현상)을 정량화하기 위해, 트랜지스터 배열에서 측정할 소자를 골라 발진 회로(주기적인 전기 신호를 만드는 회로)에 연결하고 주기 변화를 읽는 측정 회로를 제안했다. 같은 트랜지스터의 전압 조건을 바꾸거나 서로 다른 트랜지스터를 비교하며, 주변 회로가 만드는 체계적 오차는 통계 분석으로 보정한다.[^p1]

## 대표 논문

2021–2026년 논문 가운데 김재하 교수가 저자이고 실제 초록을 확인한 8편이다. 회로 검증·시간 영역 회로·고속 유선 수신기·트랜지스터 측정을 나누어 골랐다. 아래 연도는 학술지 권호 또는 학회 연도이며, “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 김재하 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2025 | [An On-Chip Circuit With Digital Output for Characterizing Transistor Current Mismatch Across Multiple Bias Conditions](https://doi.org/10.1109/ACCESS.2025.3628656) · IEEE Access | 트랜지스터마다 전류가 달라지는 정도를 칩 안에서 재고 디지털 값으로 내보내는 회로다. 배열에서 선택한 트랜지스터를 공통 발진 회로에 연결하고, 전압 조건을 조금 바꿨을 때 주기가 변하는 양으로 전류의 상대 차이를 구한다. 주변 회로의 체계적 오차를 통계적으로 보정하며 시험 칩의 측정값을 직접 전류 측정과 비교했다.[^p1] | 교신·마지막 저자 |
| 2 | 2023 | [Reachability Analysis for Nonlinear Analog/Mixed-Signal Circuits With Trajectory-Based Reachable Sets](https://doi.org/10.1109/ACCESS.2023.3295825) · IEEE Access | 비선형 아날로그·혼성신호 회로가 시간에 따라 도달할 수 있는 상태 범위를 계산한다. 상태 집합의 궤적을 수식으로 표현하고, 여러 집합이 같은 경계를 통과할 때 묶어서 처리한다. 집합이 끝없이 갈라져 계산량이 늘어나는 문제를 줄였으며 직류 전압 변환기 예제로 기존 알고리즘과 비교했다.[^p2] | 교신·마지막 저자 |
| 3 | 2021 | [Safety Verification of AMS Circuits with Piecewise-Linear System Reachability Analysis](https://doi.org/10.1109/ISOCC53507.2021.9614029) · ISOCC | 회로가 여러 초기 조건에서 시작할 때 가능한 상태의 경계를 계산해 안전한 동작 범위를 검증하는 방법이다. 비선형 회로를 구간별 선형 모델로 나타내고 상태 영역이 움직이는 궤적을 계산했다. 직류 전압을 낮추는 변환기 예제로 방법을 시험했다.[^p3] | 마지막 저자 (3명 중 3번째) |
| 4 | 2021 | [A Time-Based Pipelined ADC Using Integrate-and-Fire Multiplying-DAC](https://doi.org/10.1109/TCSI.2021.3079338) · IEEE Trans. Circuits Syst. I Regul. Pap. | 전압을 시간 차이가 담긴 두 펄스로 바꾼 뒤 단계적으로 디지털 값으로 변환한다. 각 단계는 펄스 폭의 차를 계산해 남은 변환 오차를 다음 단계로 전달한다. 회로의 비이상성이 이득 오차 대신 오프셋 오차로 나타나는 구조여서 보정을 단순화하며, 증폭기가 없는 시제품 회로를 제작해 측정했다.[^p4] | 마지막 저자 (5명 중 5번째) |
| 5 | 2024 | [Fractionally-Spaced Equalizers as Clock and Data Recovery Loops](https://doi.org/10.1109/TCSI.2024.3392842) · IEEE Trans. Circuits Syst. I Regul. Pap. | 신호 왜곡을 보정하는 분수 간격 등화기가 수신 시각을 추적하는 능력을 분석했다. 등화기를 클록·데이터 복구 회로에 대응시키는 모델을 만들고, 표본을 읽는 위상(주기적인 신호에서 진동이 진행된 상태를 나타내는 양)에 따라 달라지는 대역폭과 오차를 계산했다. 시뮬레이션으로 모델을 검증하고, 수신 속도가 조금 다른 상황에서 등화기 전환 판단을 개선했다.[^p5] | 공저자 (3명 중 2번째) |
| 6 | 2025 | [Implementing FFE-MLSD With Improved BER and Reduced Complexity for Long-Reach PAM4 Wireline Receivers](https://doi.org/10.1109/ACCESS.2025.3572568) · IEEE Access | 네 가지 신호 레벨을 쓰는 유선 수신기에서 오류를 줄이면서 계산 하드웨어를 줄이는 방법이다. 등화기의 계수를 두 단계로 학습하고, 데이터열 판정에서 계산할 후보를 미리 정한 표로 골라낸다. 기존 계수 학습보다 오류율을 개선했고, 전체 후보를 계산하는 방식에 비해 오류율을 유지하며 면적과 소비 전력을 줄였다. 회로 합성·평가와 FPGA 보드 구현을 함께 했다.[^p6] | 공저자 (5명 중 4번째) |
| 7 | 2022 | [A 2.5-32 Gb/s Gen 5-PCIe Receiver With Multi-Rate CDR Engine and Hybrid DFE](https://doi.org/10.1109/TCSII.2022.3153396) · IEEE Trans. Circuits Syst. II Express Briefs | 여러 세대의 PCIe 전송 속도에 맞춰 동작하는 수신기다. 데이터 속도에 따라 클록 방식을 바꾸어 넓은 속도 범위를 처리하고, 혼합 구조의 판정 궤환 등화기로 지연 조건과 전력 소비를 다룬다. 낮은 전송 속도에서는 일부 클록 동작을 멈춰 전력을 아낀다. 시제품 칩을 제작해 여러 PCIe 채널에서 오류율과 타이밍 허용 범위를 측정했다.[^p7] | 공저자 (10명 중 9번째) |
| 8 | 2026 | [Weighted Coding Scheme for Noise Reduction in Silicon Interposer of HBM](https://doi.org/10.1109/TVLSI.2025.3629742) · IEEE Trans. Very Large Scale Integr. Syst. | 고대역폭 메모리와 다른 칩을 잇는 촘촘한 배선에서 신호 간섭을 줄이는 부호화다. 배선 위치에 따라 서로 다른 가중치를 주고, 차폐를 추가하는 확장 방식도 제안했다. 채널 모델 시뮬레이션으로 신호 품질을 비교하고, 실제 시스템에 넣을 하드웨어의 면적·지연과 동시 출력 전환 잡음을 줄이는 방법도 다뤘다.[^p8] | 공저자 (9명 중 8번째) |

## 교수와 전문 분야

김재하 교수는 서울대학교 전기공학 학사(1997), Stanford University 전기공학 석사(1999)·박사(2003)를 받았고, 2010년 서울대학교에 부임했다. 그 전에는 True Circuits의 회로 설계자, 서울대 반도체공동연구소 박사후연구원, Rambus의 Principal Engineer, Stanford University의 대우조교수로 일했다.[^people][^prof]

학부 교수 소개는 전공을 집적회로·설계자동화, 분야를 집적회로 설계·검증으로 적는다. 현재 연구 관심으로 고성능·저전력 아날로그 및 혼성신호 집적회로와 그 설계 자동화·검증 방법을 든다.[^prof] 최근 논문으로 보면 전문 분야는 회로의 상태 범위를 수학적으로 계산하는 검증,[^p2][^p3] 시간 정보를 이용하는 변환 회로,[^p4] 고속 수신기의 등화·동기화,[^p5][^p6] 칩 내부의 트랜지스터 특성 측정이다.[^p1] 2015년에는 아날로그·혼성신호 검증 소프트웨어 회사 Scientific Analog를 창업했다.[^people]

## 응용 분야

회로 설계·검증 방법과 아날로그 셀 라이브러리는 집적회로를 개발하는 데 쓰이며, 프로그래밍 가능한 아날로그 회로는 칩을 다시 제작하지 않고 기능을 구성하는 제품을 목표로 한다.[^kor] 대표 논문은 컴퓨터 부품 사이의 PCIe 연결,[^p7] 장거리 유선 데이터 수신,[^p6] 고대역폭 메모리 연결의 신호 간섭 억제,[^p8] 트랜지스터 전류 특성 측정을 다룬다.[^p1]

## 구성원

2026년 10월 25일 People 페이지의 박사과정 4명과 석사과정 5명이다. 과정과 이메일은 게시 표기를 기준으로 했다. “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Seungho Yu | 박사과정 | seungho@mics.snu.ac.kr | 1 |
| Byoungkyu Kim | 박사과정 | bkkim@mics.snu.ac.kr |  |
| Piljun Jeong | 박사과정 | piljun@mics.snu.ac.kr | 6 |
| Dongho Hwang | 박사과정 |  |  |
| Duhyeon Kim | 석사과정 | dhkim@mics.snu.ac.kr |  |
| Donghun Chung | 석사과정 | dhchung@mics.snu.ac.kr | 1 |
| Seungyun Lee | 석사과정 | seungyun@mics.snu.ac.kr |  |
| Hyungyu Shim | 석사과정 | hyungyu@mics.snu.ac.kr | 1 |
| Yunjin Park | 석사과정 | yunjin@mics.snu.ac.kr |  |

## 졸업생과 이전 구성원

People 페이지의 Alumni 25명이다. 학위·연도는 해당 페이지에 적힌 최종 서울대학교 학위이며, 진로는 게시 이력의 첫 줄 기준이다. 학위 연도는 2012–2023년이며 진로 이력은 연도가 붙은 원문 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| MyeongJae Park | Ph.D. in E.E.C.S. (2014) | 2014- SK Hynix, Korea | A Study on Ditherless CDR with Optimal Phase Detection |
| Kyunghoon Kim (William K. Kim) | Ph.D. in E.E.C.S. (2018) | 2002- SK Hynix, Korea |  |
| Hanseok Kim | M.S. in E.E.C.S. (2012) | 2015- Samsung Electronics, Korea | A 3.2mW 10Gb/s Low-Power Decision Feedback Equalizer |
| Minbok Lee | Ph.D. in E.E.C.S (2017) | 2021- Cirrus Logic, USA | A Study on Energy-Efficient Inductor Current Controls for Maximum Energy Delivery in Battery-free Buck Converter |
| Sangho Youn | Ph.D. in E.E.C.S. (2014) | 2024- AMD, USA | Probabilistic Validation and Computer-Aided Debugging in Analog/Mixed-Signal Systems: Pre-Silicon Global Convergence Property Checking and Post-Silicon Bug Localization |
| Sigang Ryu | Ph.D. in E.E.C.S. (2019) | 2024- Assistant Professor, Korea Aerospace University, Korea | Design of Digital PLL/CDR with Advanced Digital Controller |
| Yunju Choi | Ph.D. in E.E.C.S. (2017) | 2018- Samsung Electronics, Korea | Design of Field-Programmable Mixed-Signal IC with Time-Domain Configurable Analog Block |
| Taewook Kang | M.S. in E.E.C.S. (2013) | 2024- Assistant Professor, Sungkyunkwan University, Korea | Designing an Optimum On-chip Inductor using Magnetic Core |
| Jieun Jang | Ph.D. in E.E.C.S. (2015) | 2015- Oracle, USA | Event-Driven Simulation Methodology for Analog/Mixed-Signal Systems |
| Seobin Jung | M.S. in E.E.C.S. (2013) | 2018- Google, USA | Variability-Aware Discrete Optimization for Analog Circuits |
| Hwanseok Yeo | Ph.D. in E.E.C.S. (2017) | 2005- Samsung Electronics, Korea | A Design of Calibration-Free Phase-Locked Loops (PLLs) |
| Sung-Youb Jung | Ph.D. in E.E.C.S (2019) | 2019- Samsung Electronics, Korea |  |
| Seuk Son | Ph.D. in E.E.C.S (2019) | 2022- Qualcomm, USA |  |
| Jiho Lee | Ph.D. in E.E.C.S (2019) | 2019- Samsung Electronics, Korea |  |
| Joonseok Yang | M.S. in E.C.E. (2016) | 2024- Apple, USA | Design of an Efficient CapacitorFree Piezoelectric Energy Harvesting PMIC |
| Juyun Lee | M.S. in E.C.E. (2016) | 2023- Synopsys, USA | A Modeling Methodology for Verification of High-Voltage Wordline Generator in NAND Flash Memory |
| Hyunseung Lee | M.S. in E.C.E. (2017) | 2021- Ph.D. candidate in Seoul National University |  |
| Se-won Kim | M.S. in E.E. (2021) | 2021- SK Hynix, Korea |  |
| Jiyeon Lee | M.S. in E.E. (2021) | 2021- Samsung Electronics, Korea |  |
| Nayoung Choi | M.S. in E.E. (2021) | 2011- Samsung Electronics, Korea |  |
| Chan Young Park | M.S. in E.E. (2021) | 2024- Samsung Electronics, Korea |  |
| Seoyeong Jo | M.S. in E.C.E. (2022) | 2022- Shinhan Bank, Korea |  |
| Seung Heon Baek | Ph.D. in E.C.E. (2022) | 2022- SK Hynix, Korea |  |
| Seyoung Kim | Ph.D. in E.C.E. (2022) | 2005- Samsung Electronics, Korea |  |
| Jeongwoo Min | M.S. in E.C.E. (2023) | 2023- Samsung Electronics, Korea |  |

## 최근 논문 목록 (2021–2026)

DBLP의 교수 개인 이름 목록에서 저자 식별 정보와 공저자 연결을 대조한 15편이다. 학술지 논문과 학회·워크숍 논문을 포함한다. 연도는 서지의 권호·학회 연도이며 2021년 구역의 논문은 해당 연도 전체를 실었다. 김재하 교수는 2010년 서울대에 부임했다.[^pubs][^people]

**2026**

- Sangouk Jeon, Seoyoon Jang, Kwanghyun Shin, Dongkwon Lee, Hankyu Chi, Wookjin Shin, Changhyun Pyo, Jaeha Kim, Dongsuk Jeon. "Weighted Coding Scheme for Noise Reduction in Silicon Interposer of HBM". *IEEE Trans. Very Large Scale Integr. Syst. 34(2): 466-479 (2026)*.
- Jeong-Hoon Min, Ashwin Bhat, Adou Sangbone Assoa, Seoyeong Jo, Jaeha Kim, Sigang Ryu. "XEDGE-SIM: Fast NPU-Level Simulator Unifying RRAM-Based CIM and Firmware-Aware Digital Subsystems for Mixed-Signal Verification". *SMACD 2026: 1-4*.

**2025**

- Hanseok Kim, Sihyun Lee, Piljun Jeong, Jaeha Kim, Woo-Seok Choi. "Implementing FFE-MLSD With Improved BER and Reduced Complexity for Long-Reach PAM4 Wireline Receivers". *IEEE Access 13: 90726-90740 (2025)*.
- Donghun Chung, Hyungyu Shim, Seungho Yu, Jaeha Kim. "An On-Chip Circuit With Digital Output for Characterizing Transistor Current Mismatch Across Multiple Bias Conditions". *IEEE Access 13: 192306-192314 (2025)*.
- Jaeha Kim. "Invited paper: Modeling and Simulation of Silicon Photonics Systems in SystemVerilog/XMODEL". *ASP-DAC 2025: 141-146*.
- Seoyoon Jang, Sangouk Jeon, Kwanghyun Shin, Dongkwon Lee, Hankyu Chi, Wookjin Shin, Changhyun Pyo, Jaeha Kim, Dongsuk Jeon. "WITCH: WeIghTed Coding Scheme for Crosstalk Reduction in High Bandwidth Memory". *ASP-DAC 2025: 945-951*.

**2024**

- Sigang Ryu, Jaeha Kim, Arijit Raychowdhury. "Fractionally-Spaced Equalizers as Clock and Data Recovery Loops". *IEEE Trans. Circuits Syst. I Regul. Pap. 71(7): 3002-3015 (2024)*.

**2023**

- Seyoung Kim, Seungho Yang, Hyein Lim, Hyein Lee, Jongwook Jeon, Jung Yun Choi, Jaeha Kim. "Accurate Layout-Dependent Effect Model in 10 nm-Class DRAM Process Using Area-Efficient Array Test Circuits". *IEEE Access 11: 70691-70697 (2023)*.
- Seyoung Kim, Jaeha Kim. "Reachability Analysis for Nonlinear Analog/Mixed-Signal Circuits With Trajectory-Based Reachable Sets". *IEEE Access 11: 74602-74613 (2023)*.

**2022**

- Moon-Chul Choi, Sanghee Lee, Seungha Roh, Kwangho Lee, Jonghyun Oh, Sungwoo Kim, Kwandong Kim, Woo-Seok Choi, Jaeha Kim, Deog-Kyoon Jeong. "A 2.5-32 Gb/s Gen 5-PCIe Receiver With Multi-Rate CDR Engine and Hybrid DFE". *IEEE Trans. Circuits Syst. II Express Briefs 69(6): 2677-2681 (2022)*.
- Seung-Heon Baek, Jaeha Kim. "A Gradient-Descent Calibration Method to Mitigate Process Variations in Analog Synapse Arrays". *ICEIC 2022: 1-4*.
- Jeong Woo Min, Jaeha Kim. "XSNN: a System-Level Simulator for Spiking Neural Network with Neuron Circuits and Synapse Devices". *ISOCC 2022: 390-391*.

**2021**

- Sigang Ryu, Chan Young Park, Wooryeol Kim, Seuk Son, Jaeha Kim. "A Time-Based Pipelined ADC Using Integrate-and-Fire Multiplying-DAC". *IEEE Trans. Circuits Syst. I Regul. Pap. 68(7): 2876-2889 (2021)*.
- Seyoung Kim, Heechun Park, Jaeha Kim. "Safety Verification of AMS Circuits with Piecewise-Linear System Reachability Analysis". *ISOCC 2021: 203-206*.
- Jiwoo Hong, Sunghoon Kim, Jaeha Kim, Dongsuk Jeon. "Fast Automatic Circuit Optimization Using Deep Learning". *ISOCC 2021: 207-210*.

## 연락과 위치

- 연구실 주소: 서울특별시 관악구 관악로 1 서울대학교 104-1동 314호[^home]
- 교수실: 104-1동 314호(주 사무실), 301동 507호(보조 사무실)[^people]
- 교수 전화: 02-880-1671, 보조 번호 02-880-1672[^people][^prof]
- 연구실 전화: 02-871-3285[^lab]
[^home]: MICS, Introduction. <https://mics.snu.ac.kr/> 관측일 2026-10-25.
[^kor]: MICS, 국문 Introduction. <https://mics.snu.ac.kr/kor.html> 관측일 2026-10-25.
[^people]: MICS, People(교수·박사과정·석사과정·Alumni). <https://mics.snu.ac.kr/people.html> 관측일 2026-10-25.
[^prof]: 서울대학교 전기·정보공학부, 김재하 전임교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p071> 관측일 2026-10-25.
[^lab]: 서울대학교 전기·정보공학부, 혼합신호IC 및 시스템 연구실. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=24> 관측일 2026-10-25.
[^pubs]: DBLP, Jaeha Kim 이름 목록의 2021–2026년 구역. <https://dblp.org/pid/24/4851.html> ORCID 0000-0003-2237-3134와 공저자 연결을 기준으로 구분했다. 관측일 2026-10-25.
[^p1]: D. Chung, H. Shim, S. Yu, J. Kim, IEEE Access 13, 192306-192314 (2025). <https://doi.org/10.1109/ACCESS.2025.3628656> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/397278121_An_On-Chip_Circuit_with_Digital_Output_for_Characterizing_Transistor_Current_Mismatch_Across_Multiple_Bias_Conditions> 관측일 2026-10-25.
[^p2]: S. Kim, J. Kim, IEEE Access 11, 74602-74613 (온라인 2023-07-17). <https://doi.org/10.1109/ACCESS.2023.3295825> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/372432318_Reachability_Analysis_for_Nonlinear_AnalogMixed-Signal_Circuits_with_Trajectory-Based_Reachable_Sets> 관측일 2026-10-25.
[^p3]: S. Kim, H. Park, J. Kim, ISOCC, 203-206 (2021). <https://doi.org/10.1109/ISOCC53507.2021.9614029> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/355113445_Safety_Verification_of_AMS_Circuits_with_Piecewise-Linear_System_Reachability_Analysis> 관측일 2026-10-25.
[^p4]: S. Ryu 외, J. Kim, IEEE Trans. Circuits Syst. I Regul. Pap. 68, 2876-2889 (2021). <https://doi.org/10.1109/TCSI.2021.3079338> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/351792671_A_Time-Based_Pipelined_ADC_Using_Integrate-and-Fire_Multiplying-DAC> 관측일 2026-10-25.
[^p5]: S. Ryu, J. Kim, A. Raychowdhury, IEEE Trans. Circuits Syst. I Regul. Pap. 71, 3002-3015 (2024). <https://doi.org/10.1109/TCSI.2024.3392842> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/380406039_Fractionally-Spaced_Equalizers_as_Clock_and_Data_Recovery_Loops> 관측일 2026-10-25.
[^p6]: H. Kim 외, W.-S. Choi, IEEE Access 13, 90726-90740 (2025). <https://doi.org/10.1109/ACCESS.2025.3572568> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/392008367_Implementing_FFE-MLSD_With_Improved_BER_and_Reduced_Complexity_for_Long-Reach_PAM4_Wireline_Receivers> 관측일 2026-10-25.
[^p7]: M.-C. Choi 외, D.-K. Jeong, IEEE Trans. Circuits Syst. II Express Briefs 69, 2677-2681 (2022). <https://doi.org/10.1109/TCSII.2022.3153396> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/358820561_A_25_-32_Gbs_Gen_5-PCIe_Receiver_with_Multi-Rate_CDR_Engine_and_Hybrid_DFE> 관측일 2026-10-25.
[^p8]: S. Jeon 외, D. Jeon, IEEE Trans. Very Large Scale Integr. Syst. 34, 466-479 (2026). <https://doi.org/10.1109/TVLSI.2025.3629742> 초록 기준(ResearchGate 등록 초록). ResearchGate 논문 페이지에 게시된 초록: <https://www.researchgate.net/publication/398804297_Weighted_Coding_Scheme_for_Noise_Reduction_in_Silicon_Interposer_of_HBM> 관측일 2026-10-25.

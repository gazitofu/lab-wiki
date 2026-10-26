# IPC Lab (Integrated Power Circuit Laboratory)

**KAIST 전기및전자공학부 · 백재일 교수**

- 분야: 전력전자, 집적 전력 회로(전력 칩), 결합·패키지 내장 자성 소자, 전력 전달망과 전력 무결성, 패키징·냉각, 인공지능 반도체·수송·로봇용 전원
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^research], 전자파 적합성·신호 무결성[^ee][^research], 첨단 반도체 패키징[^research][^p1], 열전달·열관리[^research], 무선 전력 전송[^home], 로봇 구동기·센서[^home], 디지털 트윈[^home], 전력전자 변환기·전력 변환 시스템[^p2]
- 홈페이지: <https://ipc.kaist.ac.kr/>
- 근거와 출처: [IPC Lab 근거 페이지](ipc-sources.md)

> 새로 떠오르는 응용과 앞으로의 응용에 쓸, 더 작고 더 큰 전력을 다루는 집적 전력전자(전력 칩)를 만드는 방법을 연구하는 연구실이다. 자성 소자 설계, 회로 구조, 패키징·냉각, 전력 전달망 분석을 함께 다루며 인공지능 반도체, 수송·항공우주, 로봇·미래 모빌리티를 응용 분야로 든다.[^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 백재일 조교수의 연구실로, 누리집 이름은 Integrated Power Circuit Laboratory(IPC Lab)다.[^home] 교수는 2024년 10월 KAIST 전기및전자공학부에 조교수로 부임했다.[^home] 전기및전자공학부 교수 소개는 소속 연구실을 Integrated Power (IP) Lab으로, 주요 연구를 Power Electronics & Power Integrity for future and emerging applications로 적고,[^ee] 반도체시스템공학과 교수진 목록은 Integrated Power Circuit (IPC) Lab으로 적는다.[^ssep]

연구의 바탕은 전력전자(power electronics, 반도체 스위치를 켜고 끄는 방식으로 전기의 전압·전류를 바꾸고 조절하는 공학)다. 연구 페이지는 연구실의 주된 연구를 새로 떠오르는 응용과 앞으로의 응용을 위해 더 똑똑하고, 더 친환경적이고, 더 작고, 더 큰 전력을 다루는 집적 전력전자, 곧 전력 칩(power chips)을 만드는 방법이라고 적는다.[^research] 교수 소개가 함께 드는 전력 무결성(power integrity, 칩에 들어가는 전원 전압이 흔들리지 않고 고르게 유지되도록 하는 설계)도 주된 연구 축이다.[^ee]

연구 페이지가 드는 연구 영역은 네 가지다. 자성 소자(magnetics, 코일과 변압기 등 자기장에 에너지를 담거나 전달하는 부품) 영역에서는 결합 인덕터와 패키지 내장 자성 소자를 설계하고 이론·시뮬레이션·측정으로 분석하며 결합 자성 소자의 제어를 다룬다.[^research] 회로 영역에서는 회로 구성 요소(building block)와 구조(architecture)를, 패키징·냉각 영역에서는 첨단 패키징 분석과 열 분석을, 전력 전달(power delivery) 영역에서는 분산된 전력 전달망의 분석과 응용별 전력 전달 방식의 최적화를 다룬다.[^research] 응용 분야로는 인공지능 반도체, 수송·항공우주, 로봇·미래 모빌리티를 든다.[^research]

부임 뒤 첫 화면 소식에는 기업·연구기관과의 공동 과제가 이어진다. 삼성전자 LSI와 고성능 가속기 전력 전달(누리집 표기 MBVR+IVR, 2025년 10월–2028년 9월), 삼성전자 네트워크와 네트워크 전원 장치의 디지털 트윈 개발, Samsung Research와 고성능 RF·임피던스 정합 시스템, 현대자동차와 전기차 충전 구조 개선, VODA와 스마트 공장용 다중 출력 무선 전력 전송, 한국기계연구원(KIMM)과 휴머노이드 로봇 과제를 시작했다고 적는다.[^home] 교수는 한국항공우주연구원(KARI)의 이온 추력기용 전력 처리 장치 핵심 기술 과제에 공동 연구책임자로 선정됐고, 인공지능 반도체용 전력전자 연구로 한국연구재단 우수신진연구 지원을 받았다.[^home]

## 주요 연구 주제

### 1. 결합·패키지 내장 자성 소자

전원 회로의 인덕터와 변압기 같은 자성 소자를 설계한다. 연구 페이지는 결합 인덕터(coupled inductor, 여러 권선을 한 자성 코어에 감아 서로의 자기장이 영향을 주고받게 만든 인덕터)와 패키지 내장 자성 소자(package integrated magnetics, 칩을 담는 패키지 안에 함께 만든 인덕터)의 설계, 이론·시뮬레이션·측정에 의한 분석, 결합 자성 소자의 제어를 든다.[^research] 대표 논문 1은 패키지 안에 만드는 동축형 인덕터에 상(phase) 사이 결합을 더해 인덕터 크기를 줄였다.[^p1] 구성원 가운데 세 명이 연구 주제를 Magnetics로 적고,[^researchers] 2026년 6월에는 기업이 이끄는 공동 제안이 선정되어 전기차용 차세대 자성 부품을 개발한다고 첫 화면이 적는다.[^home]

### 2. 프로세서·인공지능 반도체의 전력 전달

큰 전류를 쓰는 마이크로프로세서와 인공지능 가속기에 전원을 공급하는 방법을 연구한다. 연구 페이지는 분산 전력 전달망(power delivery network, 전원에서 칩까지 전류를 나르는 배선과 부품의 연결) 분석과 응용별 전력 전달 방식 최적화를 들고,[^research] 첫 화면 소식은 고성능 마이크로프로세서용 완전 집적 전압 레귤레이터(FIVR, 칩이나 패키지 안에 넣어 칩이 쓸 전압을 만드는 회로) 발표(APEC 2025), 삼성전자 LSI와의 가속기 전력 전달 과제, 큰 전류를 쓰는 인공지능 가속기용 전압 레귤레이터 모듈 연구의 APEC 2027 발표 채택을 알린다.[^home] 구성원 다섯 명이 연구 주제를 Data Center & AI Semiconductors로 적는다.[^researchers] 대표 논문 1.

### 3. 패키징·냉각과 열 분석

전원 부품을 칩 패키지 가까이 넣을 때의 구조와 열을 분석한다. 연구 페이지는 이 영역을 Packaging & Cooling Solutions로 묶고 첨단 패키징 분석(Analysis of Advanced Packaging)과 열 분석(Thermal analysis)을 든다.[^research] 대표 논문 1의 인덕터는 패키지 안에 만든 인덕터다.[^p1]

### 4. 전기차·우주·로봇·무선 전력용 전력 변환

연구 페이지가 드는 수송·항공우주, 로봇·미래 모빌리티 응용을 위해 전원 회로와 시스템을 만든다.[^research] 첫 화면 소식 기준으로 현대자동차와 전기차 충전 구조를, VODA와 스마트 공장용 다중 출력(Multi-Output) 무선 전력 전송을, 한국기계연구원과 휴머노이드 로봇 과제를 진행하며, 휴머노이드 로봇용 모터·SMA(형상 기억 합금, 가열하면 정해 둔 모양으로 돌아가는 합금) 혼합 구동기(actuator, 로봇 관절을 움직이는 장치) 연구가 2026 IEEE-RAS Humanoids 학회 발표로 채택됐다.[^home] 이온 추력기(ion thruster, 이온을 전기장으로 가속해 내뿜어 위성을 미는 장치)용 전력 처리 장치(PPU, 위성 전원의 전력을 추력기가 쓰는 전압·전류로 바꿔 주는 장치) 과제에도 참여한다.[^home] 구성원 연구 주제에는 Electric Vehicles, Wireless Power Transfer, Humanoid가 있다.[^researchers] 대표 논문 2–5는 교수가 공저자로 참여한 2025–2026년 전력 변환·충전 논문이다.

### 5. 고출력 RF 임피던스 정합과 전원 장치 디지털 트윈

Samsung Research와 고성능 RF·임피던스 정합(impedance matching, 전원과 부하 사이에서 전력이 되돌아오지 않고 잘 전달되도록 회로의 전기적 특성을 맞추는 일) 시스템을 연구한다.[^home] 구성원이 RF 임피던스 정합 시스템용 직렬 적층 공진형 전기 가변 커패시터(전기 신호로 용량을 바꾸는 커패시터) 연구를 ECCE 2026에서 발표했고, 공진형 직렬 전기 가변 커패시터(S-EVC) 구조 연구로 2026 KIPE Conference에서 Best Paper Award를 받았다.[^home] 삼성전자 네트워크와는 네트워크 전원 장치의 디지털 트윈(실제 장치를 컴퓨터 안에 똑같이 재현해 시험하고 예측하는 모형)을 개발한다.[^home] 구성원 연구 주제에는 High Power RF System과 Digital Twin이 있다.[^researchers]

## 대표 논문

백재일 교수가 KAIST에 부임한 2024년 10월 뒤 출판된 논문 가운데 교수가 저자이고 초록을 확인할 수 있는 다섯 편을 담았다. 1번은 누리집 논문 목록에 있는 교수 1저자 논문이고 나머지 저자 일곱 명은 Intel Corporation 소속이다. 2–5번은 누리집 목록에는 없고 출판사 등록 서지(Crossref)에 교수가 공저자로 오른 논문으로, 교수는 네 번째 저자이고 마지막 저자는 Gun-Woo Moon이다.[^pubs][^cr] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^cr] |
|---|---|---|---|---|
| 1 | 2025 | [Fully Integrated Voltage Regulators (FIVRs) with Package In-situ Coupled CoaxMIL Inductor for High Power Density Microprocessor Applications](https://doi.org/10.1109/apec48143.2025.10977257) · IEEE APEC 2025 | CoaxMIL 인덕터는 완전 집적 전압 레귤레이터(FIVR)용으로 패키지 안에 만드는 최신 인덕터로, 저항에 견준 인덕턴스가 크다. 그러나 결합하지 않은 인덕터의 근본적인 성능 상충 때문에 효율과 밀도를 함께 높이기 어렵다. 이 논문은 CoaxMIL 구조에 상 사이 결합을 더한 결합형 패키지 내장 동축 자성 인덕터(CoaxMIL-C)를 내놓아, 기존 CoaxMIL 인덕터의 효율을 유지하면서 인덕터 크기를 33% 줄이고 부하가 바뀔 때의 응답 성능을 높였다. 실험실 측정과 외부 인덕터 패드를 단 FIVR 시험 장치로 성능을 확인했고, CoaxMIL-C는 최대 24 A/mm²의 밀도를 내며 FIVR이 1.75 V를 0.75 V로 바꿀 때 최고 효율 89%를 내게 했다.[^p1] | 1저자 백재일 (8명) |
| 2 | 2026 | [Zero Voltage Switching Technique Using Synchronous Rectifier Control of PWM LLC Resonant Converter for Light Load Efficiency](https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11596680) · IPEC-Nagasaki 2026 (ECCE Asia) | LLC 공진 변환기(코일과 커패시터의 공진을 이용해 직류 전압을 바꾸는 변환기)는 부하가 가벼울 때 출력 전압 조절이 나쁘고 효율이 낮다. 해법 가운데 펄스 폭 변조(PWM) 제어가 유망하게 여겨져 왔고, 기존 제어는 PWM에 밸리 스위칭을 결합해 1차 측 스위치가 드레인-소스 전압의 첫 골에서 켜지게 해 스위칭 손실을 줄인다. 그러나 부품이 더 필요하고, 스위칭 주파수가 높아 스위칭 손실이 크다. 이 논문은 PWM으로 제어하는 LLC 공진 변환기의 새 동기 정류기 제어를 제안해, 드레인-소스 전압과 상관없이 영전압 스위칭(ZVS, 스위치 양단 전압이 0일 때 켜서 손실을 줄이는 방식)을 이루었다. 밸리 시점에 매이지 않아 스위칭 주파수를 자유롭게 고르고 추가 부품을 없앴으며, 입력 340–420 V 직류와 출력 48 V·1000 W의 시제품 변환기로 검증했다.[^p2] | 1저자 Yeonghun Jeong, 백재일 4번째, 마지막 저자 Gun-Woo Moon (5명) |
| 3 | 2026 | [A New Full-Bridge Buck-Boost Converter with Coupled-Inductor for EV Solar Roof Application](https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597223) · IPEC-Nagasaki 2026 (ECCE Asia) | 기존 전류형 풀브리지 변환기(CFFB)는 전압을 크게 높일 수 있어 태양광에 널리 쓰이지만, 1차 측 스위치가 하드 스위칭으로 동작하고 전압 스트레스가 높다. 이 논문은 전기차 태양광 지붕용으로, 기존 승압 인덕터를 인버터 쪽 결합 인덕터로 바꾼 결합 인덕터 인버터(CII) 방식의 전류형 풀브리지 강압·승압 변환기를 제안했다. 왼쪽 레그 스위치의 전압이 입력 전압으로 묶이고, 강압·승압 두 모드 모두에서 왼쪽 레그 스위치가 전 범위 영전압 스위칭을 하며, 48 V 입력에서 200–800 V에 해당하는 강압·승압 사이의 연속 전압 이득을 낸다. 200 W 시제품 실험에서 전부하 최고 효율 97.38%를 확인했고, 기존 CFFB보다 효율이 꾸준히 높았다.[^p3] | 1저자 Kahee Kim, 백재일 4번째, 마지막 저자 Gun-Woo Moon (5명) |
| 4 | 2026 | [A Half-Bridge Converter with Coupled Inductor for Electrical Power Systems in Satellites](https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597462) · IPEC-Nagasaki 2026 (ECCE Asia) | 위성 전기 추진 시스템의 전력 처리 장치(PPU) 안에 있는 양극 전원 변환기(APC)를 효율과 전력 밀도를 높게 만들기 위해 결합 인덕터를 넣은 새 하프브리지 변환기를 제안했다. 브리지 구조에 결합 인덕터를 넣어 승압형 동작 특성을 얻고, 스위치 전압 스트레스를 기존 전류형 하프브리지(CFHB) 변환기의 절반으로 줄였다. 스위치가 켜질 때의 하드 스위칭 손실을 줄이고 낮은 온저항의 저전압 스위치를 써서 전도 손실을 낮췄으며, 인덕터 전류의 출렁임이 줄어 인덕터를 작게 설계해 전력 밀도와 코어 손실을 함께 최적화했다. 입력 100 V, 출력 300 V·500 W 조건에서 누설 인덕턴스 때문에 생기는 서지 전압을 무손실 스너버로 억제했고, 실험으로 전 부하 범위의 효율과 전력 밀도를 확인했다.[^p4] | 1저자 Seongjun Kim, 백재일 4번째, 마지막 저자 Gun-Woo Moon (5명) |
| 5 | 2025 | [Reverse-Pulse Charging Method of Lithium Batteries for Stable Charging at Low Temperatures](https://doi.org/10.33961/jecst.2024.00969) · Journal of Electrochemical Science and Technology | 상온에서 안정적이고 빠른 리튬이온 배터리 충전법도 저온에서는 배터리의 임피던스가 바뀌어 성능을 보장하지 못한다. 기존 저온 충전법은 대부분 리튬 석출을 감지하려고 배터리 단자를 더 달거나, 평균 전류를 점점 낮춰 충전 시간이 길다. 이 논문은 역펄스 전류 충전법을 제안해, 리튬 석출 감지가 필요 없고 평균 전류를 정전류(CC) 충전과 같게 맞춰 저온에서 기존보다 빠르고 안전하게 충전한다. 시뮬레이션과 실험으로 효과를 확인했고, 충전 속도를 유지하면서 정전류 충전의 용량 감소율을 61% 개선했다.[^p5] | 1저자 Jaein Lee, 백재일 4번째, 마지막 저자 Gun-Woo Moon (6명) |

## 교수와 전문 분야

백재일 교수(Jaeil Baek)는 KAIST 전기및전자공학부 조교수이고 디비전은 Signal이다.[^ee] 연구실 누리집 교수 페이지는 반도체시스템공학과(Department of Semiconductor System Engineering), KAIST Space Institute, Department of AI Systems를 함께 적는다.[^pi] 전기및전자공학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Robotics & Control, Software Systems & Networking, Integrated Circuits & Semiconductor Systems로, 주요 연구를 Power Electronics & Power Integrity for future and emerging applications로 적고, 학위를 Ph.D. (2018) KAIST로 적는다.[^ee] 반도체시스템공학과 교수진 목록은 연구분야를 '반도체 시스템 및 집적회로'로 적는다.[^ssep]

교수는 2024년 10월 KAIST 전기및전자공학부 조교수로 부임했고, 같은 달 IEEE Senior Member가 되었다.[^home] 출판사 등록 서지에 적힌 교수의 소속은 2021–2023년 논문에서 Princeton University, 2023–2024년 논문에서 Intel Corporation이다.[^cr] 이 시기 논문은 KAIST 부임 전의 것이라 현재 KAIST 연구실의 성과로 묶지 않는다.

부임 전 논문으로 보면 전문 분야는 대전류 마이크로프로세서(CPU)용 전압 레귤레이터와 그 자성 소자다. 48 V 입력을 1 V로 바꾸는(제목 표기 48V-1V) 수직 적층형 LEGO-PoL CPU 전압 레귤레이터(PoL은 point-of-load, 부하 가까이에서 최종 전압을 만드는 변환기), 다상 결합 인덕터의 모형과 설계, 초박형 전압 레귤레이터 모듈용 다상 평면 대칭 결합 인덕터(MIPS), PWM 전력 변환용 행렬 결합 일체형 자성 소자, 수직 전력 전달용으로 높이 8.4 mm인 Mini-LEGO CPU 전압 레귤레이터, 완전 집적 전압 레귤레이터용 패키지 내장 동축 자성 인덕터(CoaxMIL 2.0)를 다뤘다.[^pubs] 목록에는 어댑터와 넓은 출력 전압 범위용 LLC 공진 변환기, 토템폴 역률 보정(PFC, 전원에서 끌어오는 전류의 모양을 전압에 맞춰 전력 낭비를 줄이는 회로) 정류기(이상 2021년), 저온 리튬이온 배터리의 공진 자기 가열 기법(2022년)도 있다.[^pubs] 전기및전자공학부 교수 소개는 대표업적으로 Vertical Stacked LEGO-PoL CPU Voltage Regulator(IEEE TPEL, 2022), MIPS(IEEE TPEL, 2023), CoaxMIL 2.0(IEEE ECTC, 2024)을 든다.[^ee]

수상과 활동은 다음과 같다. Vertical Stacked LEGO-PoL CPU Voltage Regulator 논문은 전기및전자공학부 교수 소개가 '2022 IEEE TPEL (1st prize paper)'로 적고, 누리집 논문 목록은 그 아래 줄에 '1st place - IEEE TPEL Prize Paper Award (2022), Highlighted Paper'를 적는다.[^ee][^pubs] 부임 뒤에는 2025년 3월 한국연구재단 우수신진연구(NRF of Korea Award - Outstanding Young Scientist Grant)에 선정됐고, 2025년 9월 Outstanding Teaching Award(EE30094: Power Electronics Control)를 받았으며, 2026년 2월 Kwon Oh-Hyun Endowed Chair Professor로 임명됐다.[^home] Power Supply on Chip(PwrSoC) 2025 기술 프로그램 위원과 APEC 2025 기술 세션 38 좌장을 맡았다.[^home]

## 응용 분야

연구 페이지가 드는 응용은 인공지능 반도체, 수송·항공우주, 로봇·미래 모빌리티 세 가지다.[^research] 첫 화면 소식에 오른 공동 과제는 이 응용과 이어진다. 인공지능 반도체 쪽은 삼성전자 LSI와의 고성능 가속기 전력 전달 과제와 인공지능 가속기용 전압 레귤레이터 모듈 연구, 수송 쪽은 현대자동차와의 전기차 충전 구조 과제와 전기차용 차세대 자성 부품 과제, 항공우주 쪽은 한국항공우주연구원의 이온 추력기 전력 처리 장치 과제, 로봇 쪽은 한국기계연구원과의 휴머노이드 로봇 과제다.[^home] 이 밖에 스마트 공장용 다중 출력 무선 전력 전송(VODA), 고성능 RF·임피던스 정합 시스템(Samsung Research), 네트워크 전원 장치의 디지털 트윈(삼성전자 네트워크) 과제가 있다.[^home]

대표 논문 3은 전기차 태양광 지붕용 변환기를, 대표 논문 4는 위성 전기 추진 시스템의 전력 처리 장치 안 양극 전원 변환기를 다룬다.[^p3][^p4]

## 구성원

누리집 Researchers 페이지(연구실 누리집에 삽입된 구성원 페이지)의 박사과정 4명, 석사과정 9명, 학부 연구생 5명이다. 과정·연구 주제·이메일은 페이지 표기이고, 과정 칸 괄호의 Student Leader와 SK Hynix도 페이지 표기다. "시작"은 첫 화면 News가 그 구성원의 합류를 알린 달이다.[^researchers][^home] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Doyeon Eom | 박사과정 (Student Leader) | 2025-07 | Electric Vehicles | doyeon.eom@kaist.ac.kr |  |
| Youngjoon Song | 박사과정 | 2025-07 | Digital Twin | yjsong98@kaist.ac.kr |  |
| Yunsu Kang | 박사과정 | 2025-01 | Humanoid | yunsu.k@kaist.ac.kr |  |
| Hoonjoon Lee | 박사과정 | 2025-01 | Magnetics | hoonjoon.lee@kaist.ac.kr |  |
| Chaeyoung Moon | 석사과정 | 2025-01 | High Power RF System | swc50101@kaist.ac.kr |  |
| Dongjin Chae | 석사과정 | 2025-02 | Data Center & AI Semiconductors | chaedongjin20@kaist.ac.kr |  |
| Daehyung Lim | 석사과정 | 2025-01 | Wireless Power Transfer | limdh@kaist.ac.kr |  |
| Hyeonseo Kim | 석사과정 | 2025-05 | Data Center & AI Semiconductors | pcpoptv@kaist.ac.kr |  |
| Chaewon Yoon | 석사과정 | 2025-06 | Data Center & AI Semiconductors | success259@kaist.ac.kr |  |
| Junseo Yang | 석사과정 | 2025-06 | Magnetics | junseo.yang@kaist.ac.kr |  |
| Kidae Park | 석사과정 (SK Hynix) | 2025-12 | Data Center & AI Semiconductors | kidae.park@kaist.ac.kr |  |
| Donghyun Lee | 석사과정 | 2025-10 | Data Center & AI Semiconductors | triplethriled@kaist.ac.kr |  |
| Sangeun Jeon | 석사과정 | 2026-01 | Magnetics | sejeon@kaist.ac.kr |  |
| Jaeyun Lee | 학부 연구생 | 2025-02 | Humanoid | jylee13@kaist.ac.kr |  |
| Nayeon Kim | 학부 연구생 | 2025-05 | Wireless Power Transfer | rlaskdus2045@kaist.ac.kr |  |
| Junwoo Kim | 학부 연구생 | 2025-08 | Digital Twin | woojunkim1228@kaist.ac.kr |  |
| Jinwook Kim | 학부 연구생 | 2026-02 | Digital Twin | kjinwook@kaist.ac.kr |  |
| Doyun Gu | 학부 연구생 | 2026-09 | Digital Twin & Humanoid | doyun.gu@kaist.ac.kr |  |

## 이전 구성원

Researchers 페이지 Alumni 칸의 1명이다. 진로는 페이지 표기이고, 페이지는 이 사람의 과정이나 연도를 적지 않는다. 첫 화면 News는 2025년 5월에 이 사람의 합류를 알렸다.[^researchers][^home]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Leo Choung |  | University of Toronto |

## 최근 논문 목록 (2021–2026)

누리집 Publication 페이지의 선별 목록(Selected Journal Publication, Selected Conference Proceedings) 가운데 2021–2026년 논문 20편(학술지 10편, 학회 10편)과, 누리집 목록에는 없고 출판사 등록 서지(Crossref)에 교수가 저자로 오른 2025–2026년 논문 4편(학술지 1편, 학회 3편, 끝에 doi를 적은 항목)이다. 누리집 목록의 2024년까지 논문은 교수가 KAIST에 부임한 2024년 10월 전에 낸 것이라 현재 KAIST 연구실의 성과로 묶지 않는다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, doi를 적은 4편은 출판사 등록 서지의 표기다. 누리집 목록은 몇몇 항목 바로 아래 줄에 수상·발표 선정 표기를 따로 두는데, 그 표기는 바로 위 항목 끝에 「누리집 목록에서 이 항목 아래 줄」로 붙였다.[^pubs][^cr]

**2026**

- Yeonghun Jeong, Dongmin Choi, Taewoo Kim, Jaeil Baek, Gun-Woo Moon. "Zero Voltage Switching Technique Using Synchronous Rectifier Control of PWM LLC Resonant Converter for Light Load Efficiency". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia) (doi:10.23919/ipec-nagasaki2026-ec64663.2026.11596680)*.
- Kahee Kim, Dongmin Choi, Seongjun Kim, Jaeil Baek, Gun-Woo Moon. "A New Full-Bridge Buck-Boost Converter with Coupled-Inductor for EV Solar Roof Application". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia) (doi:10.23919/ipec-nagasaki2026-ec64663.2026.11597223)*.
- Seongjun Kim, Dongmin Choi, Kahee Kim, Jaeil Baek, Gun-Woo Moon. "A Half-Bridge Converter with Coupled Inductor for Electrical Power Systems in Satellites". *2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia) (doi:10.23919/ipec-nagasaki2026-ec64663.2026.11597462)*.

**2025**

- J. Baek, B. Choi, S. Kulasekaran, H. Do, B. Marin, J. Chavarria, L. Wojewoda, and K. Radhakrishnan. "Fully Integrated Voltage Regulators (FIVRs) with Package In-situ Coupled CoaxMIL Inductor for High Power Density Microprocessor Applications". *IEEE Applied Power Electronics Conference and Exposition (APEC), Atlanta, GA, USA, 2025*.
- Jaein Lee, Sang-Hyeon Ha, Hyunki Yoon, Jaeil Baek, Jae-Sang Kim, Gun-Woo Moon. "Reverse-Pulse Charging Method of Lithium Batteries for Stable Charging at Low Temperatures". *Journal of Electrochemical Science and Technology (doi:10.33961/jecst.2024.00969)*.

**2024**

- Y. Elasser, J. Baek, K. Radhakrishnan, H. Gan, J. Douglas, H. K. Krishnamurthy, X. Li, S. Jiang, V. De, C. R. Sullivan, and M. Chen. "Mini-LEGO CPU Voltage Regulator". *IEEE Transactions on Power Electronics, vol 39, no. 3, pp. 3391 - 3410, March 2024*.
- B. Choi, J. Baek, B. C. Marin, S. Qu, S. Kulasekaran, J. I. Chavarria, L. E. Wojewoda, and K. Radhakrishnan. "CoaxMIL 2.0 – Next Generation Coaxial Magnetic Integrated Inductors for Higher Efficiency Fully Integrated Voltage Regulator". *IEEE Electronic Components and Technology Conference (ECTC), Denver, CO, USA, 2024*.

**2023**

- Y. Elasser, H. Li, P. Wang, J. Baek, K. Radhakrishnan, S. Jiang, H. Gan, X. Zhang, D. Giuliano, and M. Chen. "Circuits and Magnetics co-Design for Ultra-thin Vertical Power Delivery: A Snapshot Review". *MRS Advances, December 2023*.
- J. Baek, Y. Elasser, and M. Chen. "MIPS: Multiphase Integrated Planar Symmetric Coupled Inductor for Ultrathin VRM". *IEEE Transactions on Power Electronics, vol 38, no. 5, pp. 5609-5614, May 2023*.
- Y. Elasser, J. Baek, K. Radhakrishnan, H. Gan, J. Douglas, V. De, S. Jiang, H. Krishnamurthy, X. Li, C. R. Sullivan, and M. Chen. "Mini-LEGO: A 1.5-MHz 240-A 48-V-to-1-V CPU VRM with 8.4mm Height for Vertical Power Delivery". *IEEE Applied Power Electronics Conference (APEC), Orlando, FL, USA, 2023 · 누리집 목록에서 이 항목 아래 줄: Outstanding Presentation Award*.
- S. Thurber, X. Zhang; Y. Jeon, and J. Baek. "An Auxiliary Circuit with a Flexible LC Resonant Tank for High-Efficiency and Low-Cost Totem-pole Boost Bridgeless Power-Factor Correction Converter". *IEEE Applied Power Electronics Conference (APEC), Orlando, FL, USA, 2023*.
- H. Cheng, Z. Zheng, P. Kumar, Y. Chen, J. Baek, B. Kim, S. Wagner, N. Verma, J. C. Sturm, and M. Chen. "A Flexible Lightweight 7.4 V Input 300 V to 1500 V Output Power Converter for an Untethered Modular Piezoelectric Soft Robot". *IEEE Workshop on Control and Modeling of Power Electronics (COMPEL). Arbor, MI, USA, 2023*.

**2022**

- P. Wang, D. Zhou, Y. Elasser, J. Baek, and M. Chen. "Matrix Coupled All-in-One Magnetics for PWM Power Conversion". *IEEE Transactions on Power Electronics, vol 37, no. 12, pp. 15035-15050, December 2022 · 누리집 목록에서 이 항목 아래 줄: Highlighted Paper*.
- J. Baek, Y. Elasser, K. Radhakrishnan, H. Gan, J. Douglas, H. K. Krishnamurthy, X. Li, S. Jiang, C. R. Sullivan, and M. Chen. "Vertical Stacked LEGO-PoL CPU Voltage Regulator". *IEEE Transactions on Power Electronics, vol 37, no. 6, pp. 6305-6322, June 2022 · 누리집 목록에서 이 항목 아래 줄: 1st place - IEEE TPEL Prize Paper Award (2022), Highlighted Paper*.
- S. H. Ha, J. Lee, H. Yoon, T. R. Park, J. Baek, J. S. Kim, and G. W. Moon. "Frequency-Variable Resonant Self-Heating Technique for Lithium-Ion Batteries at Low Temperature". *IEEE Transactions on Aerospace and Electronic Systems, vol. 58, no. 4, pp. 3399-3410, August 2022*.
- Z. Daniel, E. Youssef, J. Baek, and M. Chen. "Reluctance-Based Dynamic Models for Multiphase Coupled Inductor Buck Converters". *IEEE Transactions on Power Electronics, vol. 37, no. 2, pp. 1334-1351, February 2022*.
- Y. Elasser, J. Baek, K. Radhakrishnan, H. Gan, J. Douglas, H. Krishnamurthy, X. Li, S. Jiang, C. R. Sullivan, and M. Chen. "Vertical Stacked 48V-1V LEGO-PoL CPU Voltage Regulator with 1A/mm2 Current Density". *IEEE Applied Power Electronics Conference (APEC), Houston, TX, USA, 2022*.

**2021**

- J. Baek, K. W Kim, H. S. Youn, and C. E. Kim. "High-Efficiency LLC Resonant Converter with Reconfigurable Voltage Multiplying Rectifier (RVMR) for Wide Output Voltage Applications". *IEEE Transactions on Power Electronics, vol. 36, no. 7, pp. 7641-7651, July 2021*.
- Y. D. Lee, G. W. Moon, J. Baek, and C. E. Kim. "A Reconfigurable Totem-pole PFC Rectifier With Light Load Optimization Control Strategy And Soft-switching Capability". *IEEE Transactions on Power Electronics, vol. 36, no. 4, pp. 4371-4382, April 2021*.
- C. E. Kim, J. Baek, and J. B. Lee. "Three-Switch LLC Resonant Converter for High-Efficiency Adapter with Universal Input Voltage". *IEEE Transactions on Power Electronics, vol. 36, no. 1, pp. 630-638, January 2021*.
- J. Baek, Y. Elasser, and M. Chen. "Vertical Stacked 48V-1V Voltage Regulator for Ultra High Current Microprocessors". *Open Compute Project (OCP) Annual Symposium 2021, San Jose, CA, USA, 2021 · 누리집 목록에서 이 항목 아래 줄: Best Paper Award and Selected Paper for the Oral Presentation Session*.
- Tanuj Sen, J. Baek, and M. Chen. "Current Balancing of Paralleled Switches in Resonant Converters with Multiphase Coupled Inductor". *IEEE Workshop on Control and Modelling of Power Electronics (COMPEL), Cartagena, Colombia, 2021*.
- J. Baek, Y. Elasser, and M. Chen. "3D LEGO-PoL: A 93.3\% Efficient 48V-1.5V 450A Merged-Two-Stage Hybrid Switched-Capacitor Converter with 3D Vertical Coupled Inductors". *IEEE Applied Power Electronics Conference and Exposition (APEC), Phoenix, AZ, USA, 2021*.
- Y. Elasser, J. Baek, C. R. Sullivan, and M. Chen. "Modeling and Design of Vertical Multiphase Coupled Inductors with Inductance Dual Model". *IEEE Applied Power Electronics Conference and Exposition (APEC), Phoenix, AZ, USA, 2021*.

## 소식

누리집 첫 화면 News의 2024년 10월–2026년 10월 글 44건이다. 날짜는 게시된 달 머리글이고, 문장은 게시된 그대로다.[^home]

- 2026-10 · Our work on Voltage Regulator Modules for High-Current AI Accelerators has been accepted for presentation at the 2027 IEEE APEC, March 07-11, 2027, in New Orleans, LA. Congrats, Dongjin!! More exciting research on AI Accelerators is coming!
- 2026-10 · Chaeyoung successfully presented his research on "A Series-Stacked Resonant Electrical Variable Capacitor for RF Impedance Matching Systems " at ECCE 2026, held in Vancouver , CA, Canada! Congrats, Chaeyoung!
- 2026-10 · Our work on Motor-SMA Hybrid Actuator for Humanoid Robots has been accepted for presentation at the 2026 IEEE-RAS 25th International Conference on Humanoid Robots, December 06-09, 2026, in Santa Clara, CA. Congrats, Yunsu!! More exciting research on humanoid robotics is coming!
- 2026-09 · Doyun Gu joins Integrated Power Circuit (IPC) Lab. Welcome, Doyun!
- 2026-07 · Chaeyoung received the Best Paper Award at the 2026 KIPE Conference for “Architecture of a Resonant Series Electrically Variable Capacitor (S-EVC) for RF Impedance Matching System.” Congrats, Chaeyoung!
- 2026-06 · A collaborative proposal (led by Chang Sung Corportaion) has been selected! IPC Lab will develop next-generation magnetic components for electric vehicles (EVs) in collaboration with leading research institutes and Hyundai Motor Company.
- 2026-05 · Our work on a Impedance Matching Network has been accepted for presentation at the IEEE ECCE (Energy Conversion Conference and Expo) 2026 , October 04-08, 2026, in Vancouver, Canada! Congrats, Chaeyung and Doyeon!!
- 2026-04 · IPC Lab has renewed and expanded its collaboration with Samsung Research to further advance High-performance RF + Impedance Matching Systems for future applications!
- 2026-03 · IPC Lab launched a collaboration project with Hyundai Motor Company to improve Electric Vehicles Charging Architectures!
- 2026-02 · Prof. Baek appointed as Kwon Oh-Hyun Endowed Chair Professor!
- 2026-02 · Jinwook joined Integrated Power Circuit (IPC) Lab. Welcome, Jinwook!
- 2026-01 · Sangeun joined Integrated Power Circuit (IPC) Lab. Welcome, Sangeun!
- 2025-12 · Nayeon & Hoonjoon's research proposal for the KAIST URP program was awarded (IPC's 3rd URP program award)!. Congrats, Nayeon & Hoonjoon!
- 2025-12 · Kidae joined Integrated Power Circuit (IPC) Lab. Welcome, Kidae!
- 2025-10 · Donghyun joined Integrated Power Circuit (IPC) Lab. Welcome, Donghyun!
- 2025-10 · IPC Lab launched a collaboration project with Samsung Electronics (LSI) for MBVR+IVR High Performance Accelerator Power Delivery from 2025. 10 to 2028.09!
- 2025-09 · Prof. Baek received the Outstanding Teaching Award (EE30094: Power Electronics Control)!
- 2025-09 · IPC Lab launched a collaboration project with Samsung Electronics (Network) for Digital Twin Development of Network Power Supplies!
- 2025-08 · Junwoo Kim joins Integrated Power Circuit (IPC) Lab. Welcome, Junwoo!
- 2025-07 · Doyeon Eom joins Integrated Power Circuit (IPC) Lab. Welcome, Doyeon!
- 2025-07 · Youngjoon Song joins Integrated Power Circuit (IPC) Lab. Welcome, Youngjoon!
- 2025-06 · Chaewon Yoon joins Integrated Power Circuit (IPC) Lab. Welcome, Chaewon!
- 2025-06 · Junseo Yang joins Integrated Power Circuit (IPC) Lab. Welcome, Junseo!
- 2025-06 · Jaeyun & Yunsu's research proposal for the KAIST URP program has been awarded! Congrats, Jaeyun & Yunsu!
- 2025-06 · Daehyung & Chaeyoung's research proposal for the KAIST URP program has been awarded! Congrats, Daehyung & Chaeyoung!
- 2025-05 · Leo Choung joins Integrated Power Circuit (IPC) Lab. Welcome, Leo!
- 2025-05 · Nayeon Kim joins Integrated Power Circuit (IPC) Lab. Welcome, Nayeon!
- 2025-05 · Hyeonseo Kim joins Integrated Power Circuit (IPC) Lab. Welcome, Hyeonseo!
- 2025-04 · IPC Lab launched a collaboration project with VODA for Multi-Output Wireless Power Transfer for FutureSmart Factory!
- 2025-04 · IPC Lab launched a collaboration project with KIMM for Humanoid Robots! More exciting research topics are coming!
- 2025-04 · IPC Lab launched a collaboration project with Samsung Research for High-performance RF + Impedance Matching Systems for future applications!
- 2025-03 · Prof. Baek will serve as a Technical Program Committee (TPC) member for Power Supply on Chip (PwrSoC) 2025.
- 2025-03 · Prof. Baek received the NRF of Korea Award - Outstanding Young Scientist Grant (우수신진) for his proposal "Research on Sophisticated Power Electronics for High Performance AI Semiconductor: Component, Circuit, Architecture, and System". More exciting research is coming!
- 2025-03 · Proposal as a Co-PI "Research on Core Technologies of Power Processing Unit (PPU) for Ion Thruster" was selected for funding by Korea Aerospace Research Institute (KARI). More exciting research is coming!
- 2025-03 · Prof. Baek will chair the Technical Session 38 at APEC 2025, held in Atlanta, GA.
- 2025-03 · Prof. Baek will present his research on "High Power Density Fully Integrated Voltage Regulator (FIVR) for High Power Density Microprocessors (GPU, CPU, and XPU) " at APEC 2025, held in Atlanta, GA.
- 2025-02 · Jaeyun Lee joins Integrated Power Circuit (IPC) Lab. Welcome, Jaeyun!
- 2025-02 · Dongjin Chae joins Integrated Power Circuit (IPC) Lab. Welcome, Dongjin!
- 2025-01 · Chaeyoung Moon joins Integrated Power Circuit (IPC) Lab. Welcome, Chaeyoung!
- 2025-01 · Yunsu Kang joins Integrated Power Circuit (IPC) Lab. Welcome, Yunsu!
- 2025-01 · Daehyung Lim joins Integrated Power Circuit (IPC) Lab. Welcome, Daehyung!
- 2025-01 · Hoonjoon Lee joins Integrated Power Circuit (IPC) Lab. Welcome, Hoonjoon!
- 2024-10 · Prof. Baek became a Senior Member of IEEE.
- 2024-10 · Jaeil Baek joins KAIST School of Electrical Engineering as an Assistant Professor.

## 연락과 위치

- 주소: Integrated Power Circuit Lab, School of Electrical Engineering, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 교수 연구실: 전기및전자공학부동(E3-2) 5224호[^ee]
- 연락처: 042-350-7478[^ee]
- 교수 이메일: jaeil.baek@kaist.ac.kr[^ee]
[^p1]: J. Baek 외, K. Radhakrishnan, 2025 IEEE Applied Power Electronics Conference and Exposition (APEC), 491-497 (2025). <https://doi.org/10.1109/apec48143.2025.10977257> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y. Jeong 외, G.-W. Moon, 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), 1-8 (2026). <https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11596680> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: K. Kim 외, G.-W. Moon, 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), 1-8 (2026). <https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597223> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Kim 외, G.-W. Moon, 2026 International Power Electronics Conference (IPEC-Nagasaki 2026 - ECCE Asia), 1-8 (2026). <https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597462> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Lee 외, G.-W. Moon, Journal of Electrochemical Science and Technology 16, 113-128 (2025). <https://doi.org/10.33961/jecst.2024.00969> 초록 기준.
[^home]: IPC Lab 누리집 첫 화면 <https://ipc.kaist.ac.kr/> (연구실 이름, 모집 안내, News, 주소, 2026-10-23 열람)
[^pi]: IPC Lab 누리집 Principal Investigator 페이지 <https://ipc.kaist.ac.kr/members/principal-investigator> (직위, 소속, 2026-10-23 열람)
[^researchers]: IPC Lab 누리집 Researchers 페이지 <https://ipc.kaist.ac.kr/members/researchers> (삽입된 구성원 페이지 <https://hoonjoon0501.github.io/IPC_Lab/members/researchers/>, 2026-10-23 열람)
[^research]: IPC Lab 누리집 Research Area 페이지 <https://ipc.kaist.ac.kr/research-area> (연구 영역과 응용, 2026-10-23 열람)
[^pubs]: IPC Lab 누리집 Publication 페이지 <https://ipc.kaist.ac.kr/publication> (Selected Journal Publication, Selected Conference Proceedings, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(백재일) <https://ee.kaist.ac.kr/professor/%eb%b0%b1%ec%9e%ac%ec%9d%bc/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (백재일 교수 항목, 2026-10-23 열람)
[^cr]: 출판사 등록 서지(Crossref) 저자 검색 <https://api.crossref.org/works?query.author=Jaeil+Baek> (저자 순서·소속, 2026-10-23 조회)

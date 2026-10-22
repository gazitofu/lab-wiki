# 지능형전력효율설계연구실 (SEED Lab, Smart Energy-Efficient Design Lab)

**KAIST 전기및전자공학부·AI시스템학과 · 정완영 교수**

- 분야: 저전력 집적회로, 전력 관리 회로(LDO·DC-DC 변환기), 아날로그·혼성 신호 회로(데이터 변환기·센서), 회로 설계 자동화(CAD·EDA), 디지털 기본 회로, AI·엣지 가속기
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^prof][^eeprof][^p1], 메모리 내 연산[^research][^p5], AI 반도체·가속기[^research][^prof][^p5], 컴퓨터 구조·운영체제[^research][^p7][^p8], 과학·공학 AI[^research][^prof]
- 홈페이지: <https://seed.kaist.ac.kr/>
- 근거와 출처: [지능형전력효율설계연구실 근거 페이지](seed-sources.md)

> 작고 스스로 움직이는 시스템에 들어갈 저전력 집적회로를 만드는 연구실이다. 전력 관리 회로와 데이터 변환기·센서 회로, 메모리 안에서 계산하는 회로를 설계하고, 인공지능으로 회로 설계를 자동화하는 도구와 이런 회로를 쓰는 프로세서 구조까지 함께 연구한다.[^prof][^research]

## 무엇을 연구하나

연구실 Professor 페이지는 연구실이 작은 자율 시스템을 위한 저전력 집적회로, 전력 관리, 인공지능의 도움을 받는 설계 자동화에 집중한다고 소개하고, 연구 분야로 전력 관리 IC, 아날로그·혼성 신호 회로, 데이터 변환기와 센서, 회로 CAD·EDA(컴퓨터로 회로를 설계·검증하는 도구), 디지털 기본 회로, AI·엣지 가속기를 꼽는다.[^prof] 첫 화면은 연구실의 방향을 "회로부터 AI까지, 저전력·고효율 시스템을 설계한다"는 문장으로 적는다.[^home] 전기및전자공학부 교수 소개는 주요 연구를 초저전력 아날로그·디지털 회로와 IoT(사물인터넷) 시스템으로, 반도체시스템공학과 교수진은 연구분야를 반도체 시스템 및 집적회로로 적는다.[^eeprof][^ssep]

Research 페이지는 연구를 응용, AI 모델, 시스템 소프트웨어, 컴퓨터 구조, 컴퓨터 지원 설계(CAD), 회로, 소자, 물리의 여덟 층으로 된 설계 계층으로 나누고, 이 가운데 회로, CAD, 컴퓨터 구조, AI 모델의 네 층을 연구실의 집중 분야로 표시한다.[^research] 회로 층은 전력 관리와 데이터 변환을 위한 아날로그·디지털·혼성 신호 회로로, LDO 레귤레이터(입력과 출력의 전압 차이가 작아도 동작하는 선형 전압 조절 회로)와 DC-DC 변환기(직류 전압을 다른 직류 전압으로 바꾸는 회로)를 포함한 전력 관리 IC, ADC·DAC(아날로그 신호와 디지털 숫자를 서로 바꾸는 회로) 같은 데이터 변환기, 에너지 효율이 높은 온도 센서, 센서 신호를 받아 다듬는 혼성 신호 인터페이스, 메모리 안에서 곱셈-누산을 하는 메모리 내 연산(CIM), 플립플롭 같은 디지털 기본 회로를 연구 주제로 둔다.[^research]

CAD 층은 컴퓨터 구조와 회로를 함께 최적화하기 위한 설계 도구를 다루며, 회로 구조(토폴로지)를 자동으로 만들어 내는 합성, 컴퓨터 구조 탐색과 구조에서 회로까지 이어지는 최적화, 제약을 고려한 설계 공간 탐색, 배치를 고려한 자동화와 PPA(성능·전력·면적) 최적화, 기계학습으로 회로를 시뮬레이션하고 성능을 예측하는 모델을 주제로 둔다.[^research] 컴퓨터 구조 층은 AI 가속기, 데이터 경로, 마이크로아키텍처, 명령어 집합(ISA) 확장, 메모리 시스템을 주제로 둔다. AI 모델 층은 하드웨어를 중심에 두고 AI 모델과 알고리즘을 다듬어 학습·추론 효율을 함께 높이는 연구로, 양자화·압축·저비트 추론, 가지치기, 가속기에 맞춘 하드웨어·소프트웨어 공동 설계, 계산 효율이 높은 신경망 구조를 주제로 든다.[^research]

대표 논문으로 보면 연구는 네 갈래다. 첫째, 전원 회로인 LDO 레귤레이터와 하이브리드 DC-DC 변환기의 회로 구조 자동 생성이다(대표 논문 1, 2).[^p1][^p2] 둘째, 아날로그 신호를 디지털로 바꾸는 ADC와 온도 센서다(대표 논문 3, 4).[^p3][^p4] 셋째, DRAM 셀로 신경망 계산을 하는 메모리 내 연산 회로와 저전력 플립플롭이다(대표 논문 5, 6).[^p5][^p6] 넷째, 전압을 쌓아 공급하는 벡터 프로세서와 엣지 컴퓨팅용 프로세서 구조다(대표 논문 7, 8).[^p7][^p8] 2021–2026년 논문 목록에는 이 밖에 플립플롭 회로 구조를 자동으로 만들고 탐색하는 연구(ICCAD 2024, DAC 2026), 누리집이 기계학습 기반 회로 시뮬레이터(ML-based Circuit Simulator)로 분류한 그래프 신경망 회로 모델(DAC 2026), DRAM 메모리 내 연산 매크로(IEEE JSSC 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 전력 관리 회로와 회로 구조 자동 생성

아날로그 LDO와 디지털 LDO의 장점을 함께 살린 소프트 스위칭 LDO를 만들어, 입력 전압 0.6–1 V에서 높은 전류 밀도와 전류 효율, 빠른 부하 응답을 보였다.[^p1] 인덕터 하나와 커패시터 둘을 쓰는 하이브리드 DC-DC 변환기의 회로 구조를 빠짐없이 자동으로 만들고 분석하는 틀 ConverGenT를 내놓았다.[^p2] 논문 목록에는 출력이 하나 또는 둘인 스위치드 커패시터 DC-DC 변환기(A-SSCC 2024), 빠른 동적 전압 조절(DVS)을 하는 시스템에서 용량성 DC-DC 변환기의 전압 변환 비율이 바뀔 때 생기는 손실을 분석하고 줄이는 기법(IEEE TPEL 2021), 회로 구조 자동 생성 틀 FACTGen(ISOCC 2022)도 있다.[^pubs] 대표 논문 1, 2.

### 2. 데이터 변환기와 온도 센서

플로팅 인버터 증폭기를 개선한 CC-FIA를 잔차 증폭기로 넣은 고해상도 파이프라인 SAR ADC를 만들었다.[^p3] MOS 트랜지스터로 온도를 재면서 변환부와 판독 회로를 하나로 합치고 비교 단계를 줄인 에너지 효율 온도 센서도 만들었다.[^p4] 논문 목록에는 온도와 전압을 직접 비교하는 SAR 온도 센서(A-SSCC 2022, IEEE SSC-L 2023)와 디지털 지연 사슬로 만든 작고 전력이 적은 열(column) 판독 회로(ISCAS 2024)도 있다.[^pubs] 대표 논문 3, 4.

### 3. 메모리 내 연산과 디지털 기본 회로

DRAM 셀 두 개로 여러 비트의 곱셈-누산을 한 번에 하는 아날로그 가속기 MAC-DO를 설계했다.[^p5] 클럭에 연결된 내부 노드의 불필요한 전환과 경합 경로를 없앤 저전력 플립플롭 C2SFF도 내놓았다.[^p6] 논문 목록에는 1T1C DRAM 메모리 내 연산 매크로 DRAMP(IEEE JSSC 2026), 플립플롭 회로 구조를 자동으로 만들고 넓게 탐색하는 SeGen(ICCAD 2024)과 B-Flex(DAC 2026)도 있다.[^pubs] 대표 논문 5, 6.

### 4. 프로세서 구조와 전력 전달

전원을 직렬로 쌓아 공급하는 벡터 프로세서에서 회로 사이 전류 불균형을 데이터 경로 회로로 줄인 TickTockStack을,[^p7] 엣지 컴퓨팅용으로 수직 인덱싱 명령을 더한 SIMD 프로세서 VVIP를 만들었다.[^p8] 논문 목록은 TickTockStack에 ICCAD 2025 「Best Paper Award Nominations」 표시를 붙였다.[^pubs] 대표 논문 7, 8.

## 대표 논문

랩 Publications 목록의 2021–2026년 논문 가운데 정완영 교수가 마지막 저자인 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [A 0.6-1 V VIN Soft-Switching Low Dropout Regulator with 31.3 A/mm2 Current Density, 99.99% Current Efficiency, and 2.04 fs FoM](https://doi.org/10.1109/vlsitechnologyandcir46783.2024.10631485) · IEEE Symposium on VLSI Technology and Circuits (VLSI-C) 2024 | 아날로그 LDO와 디지털 LDO의 장점을 함께 살린 소프트 스위칭 LDO다. 소프트 양자화기가 아날로그 LDO처럼 전력 트랜지스터를 부드럽게 켜고 끄게 하고, 인버터로 만든 버퍼는 디지털 LDO처럼 전원의 양 끝까지 이르는 출력 전압을 전력 트랜지스터에 준다. 이 버퍼는 밀고 당기는(push-pull) 구조라 입력·출력 전압 차이(드롭아웃 전압)가 50 mV로 작을 때도 부하 변화에 빨리 반응한다. 65 nm CMOS 공정으로 만든 시험 칩은 입력 1 V에서 전류 밀도 31.3 A/mm², 입력 0.6 V에서 전류 효율 99.99%를 얻었고, 입력 0.6 V에서 부하 전류가 4 ns 동안 90 mA 바뀔 때 출력 전압이 102 mV 떨어지는 빠른 응답을 보였다.[^p1] | 1저자 J. Kim(Jeongmyeong Kim), 마지막 저자 정완영 (3명) |
| 2 | 2023 | [ConverGenT: Automated Topology Generation and Analysis of Hybrid DC–DC Converters](https://doi.org/10.1109/tpel.2023.3285548) · IEEE Transactions on Power Electronics (TPEL) | 인덕터와 커패시터를 함께 쓰는 하이브리드 DC-DC 변환기는 효율과 전력 밀도가 높아 주목받지만, 인덕터와 커패시터 개수가 다른 새 회로 구조(토폴로지)를 만드는 체계적인 절차가 없었다. ConverGenT는 인덕터 하나와 커패시터 둘(플라잉 커패시터 하나, 출력 커패시터 하나)을 쓰는 2위상 하이브리드 변환기의 회로 구조를 자동으로 만들고 분석하는 틀로, 이런 종류의 회로 구조를 모두 찾아낸다. 직관에 기대던 기존 방법보다 시간이 덜 들고 가능한 구조를 빠뜨리지 않으며, 만든 구조는 손이나 자동으로 분석·검증해 응용에 맞는 것을 고를 수 있다. ConverGenT는 기존 변환기보다 어떤 면에서 나은 변환기 계열 62개(계열마다 구조 최대 6개)를 찾았고, 그 가운데 적어도 8개 구조는 최근 5년 안에 발표된 것이었다.[^p2] | 1저자 H. Nguyen(Huan Nguyen), 마지막 저자 정완영 (2명) |
| 3 | 2024 | [A High-Resolution Pipelined-SAR ADC Using Cyclically Charged Floating Inverter Amplifier](https://doi.org/10.1109/jssc.2024.3419759) · IEEE Journal of Solid-State Circuits (JSSC) | 에너지 효율이 높고 조정하기 쉬운 플로팅 인버터 증폭기(FIA)인 CC-FIA를 내놓았다. 여러 스위치드 커패시터를 다시 써서 증폭기의 동작점을 안정한 영역으로 맞출 수 있어, 동작점을 문턱 전압 근처나 그 아래에 두고 전류 효율(gm/ID)을 높인다. 동작점을 쉽게 바꿀 수 있어 샘플링 주파수가 달라지는 이벤트 구동 ADC에서도 증폭기 에너지 효율을 최대로 맞출 수 있다. 개방 루프 이득이 안정하고 조정하기 쉬워 닫힌 루프에서 생기는 안정성 문제가 없고, 저장 커패시터마다 증폭기에 전하를 여러 번 퍼 주므로 기존 FIA보다 면적이 크게 작다. CC-FIA를 파이프라인 SAR ADC의 개방 루프 잔차 증폭기로 넣고 65 nm CMOS 공정으로 만든 시제품은 샘플링 주파수 2 MS/s에서 SNDR 74.0 dB, SFDR 85.5 dB를 얻었고, 1.2 V 전원에서 72.3 μW를 써 Schreier 성능 지수 175.4 dB를 보였다.[^p3] | 1저자 C. Park(Changjoo Park), 마지막 저자 정완영 (7명) |
| 4 | 2025 | [A MOS-Based Temperature Sensor With Energy-Efficient Techniques](https://doi.org/10.1109/lssc.2025.3559900) · IEEE Solid-State Circuits Letters (SSC-L) | MOS 트랜지스터로 온도를 재는 에너지 효율이 높은 온도 센서다. 온도를 전기 신호로 바꾸는 변환부와 판독 회로를 하나로 합쳐 잡음을 줄였고, 온도에 따라 오프셋 전압이 바뀌는 비교기를 가장 낮은 비트부터 값을 정하는 LSB-first SAR 방식과 묶어 에너지 효율을 최적화했다. LSB-first SAR는 변환 단계 수와 에너지 소비를 줄인다. 비동기 클럭으로 회로를 제어해 시간 기준 신호가 필요 없고, 온도에 맞춰 속도가 바뀌어 측정이 더 견고해진다. 65 nm CMOS 공정으로 만든 센서는 −60 °C부터 145 °C까지 재며, 2차 다항식으로 두 점 보정한 뒤 오차는 전체 범위에서 −1.93/+1.44 °C, −43 °C부터 137 °C까지에서 −0.96/+0.94 °C였다. 상온에서 해상도 71.8 mK, 변환 한 번에 41.9 pJ를 써 해상도 성능 지수 216 fJ·K²를 얻었다.[^p4] | 1저자 J. Kim(Jooeun Kim), 마지막 저자 정완영 (5명) |
| 5 | 2024 | [MAC-DO: DRAM-Based Multi-Bit Analog Accelerator Using Output Stationary](https://doi.org/10.1109/iscas58744.2024.10558271) · IEEE International Symposium on Circuits and Systems (ISCAS) 2024 | DRAM 기반 가속기는 기존 폰 노이만 구조의 메모리 벽(프로세서와 메모리 사이 데이터 이동이 성능을 묶는 문제)을 풀 가능성을 보였지만, 전하 공유나 논리 회로로 단순한 논리 연산만 해서 여러 비트의 곱셈-누산(MAC) 연산에는 많은 사이클이 들고 데이터 접근·이동이 늘어 전력 효율이 나빠질 수 있다. MAC-DO는 1T1C DRAM 셀 두 개로 된 셀 하나가 여러 비트 MAC 연산을 한 사이클에 해내, 기존 1T1C DRAM 셀·배열 구조와 호환되고 선형성을 좋게 유지하면서 전력 효율을 크게 높인다. 이는 전하 조향(charge steering)을 쓴 새 아날로그 계산 방식 덕분이며, 출력 고정(output stationary) 배치로 심층 신경망 계산의 대부분을 차지하는 합성곱을 가속한다. 트랜지스터 수준 시뮬레이션으로 평가한 16×16 셀 시험 배열은 120.96 TOPS/W를 얻었고, 재학습 없이 MNIST 데이터셋에서 Top-1 정확도 97.07%를 보였다.[^p5] | 1저자 M. Jeong(MinKi Jeong), 마지막 저자 정완영 (2명) |
| 6 | 2024 | [A Redundant-Transition-Free and Contention-Free Change-Sensing Flip-Flop](https://doi.org/10.1109/tcsii.2024.3377714) · IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II) | 불필요한 신호 전환이 없는 저전력 플립플롭 C2SFF다. 데이터 입력의 변화가 클럭 신호와 상관없이 일어나는 시험 조건에서 기존 변화 감지 회로가 불안정해지는 문제를 찾아냈다. 이를 풀어 C2SFF는 늘 경합이 없고 누설 전류가 적으며, 클럭에 연결된 내부 노드의 불필요한 전환을 없애 동적 전력도 낮게 유지한다. 경합 경로를 모두 없애 트랜지스터 크기를 따로 조정하지 않고도 0.32 V까지 안정하게 동작한다. 65 nm CMOS 공정 설계 자료로 한 배치 후 시뮬레이션에서 전송 게이트 플립플롭(TGFF)보다 전력 소비가 1 V에서 활동률 10%·20%일 때 각각 62.1%·52.8%, 0.4 V에서 56.9%·49.0% 줄었다. 셋업·홀드 창은 시험한 플립플롭 가운데 두 번째로 좋았다.[^p6] | 1저자 K. Kang(Kyounghun Kang), 마지막 저자 정완영 (2명) |
| 7 | 2025 | [TickTockStack: In-Datapath Current Imbalance Elimination Using Clocked Differential Logic in a Voltage Stacked Vector Processor](https://doi.org/10.1109/iccad66269.2025.11240897) · IEEE/ACM International Conference On Computer Aided Design (ICCAD) 2025 | 전력 밀도가 높은 최신 디지털 칩에서는 전력 전달망(PDN)에서 에너지가 많이 낭비되어 열과 전압 강하가 생기고 시스템 신뢰성이 떨어진다. 전압 적층은 전류 양상이 비슷한 회로들의 전원 단자를 직렬로 이어 전하를 다시 써서 PDN 손실을 줄이지만, 적층된 회로 사이 전류 불균형 때문에 전압 출렁임과 전력 전달 손실이 남는다. TickTockStack은 구조와 회로를 함께 최적화해 설계한 전압 적층 벡터 프로세서다. 여러 레인이 같은 명령을 함께 실행하는 벡터 프로세서를 골라 제어에서 생기는 차이를 줄였고, 데이터에 따라 생기는 나머지 불균형은 활동률이 일정한 클럭 이중 레일 도미노(DRD) 논리로 만든 데이터 경로와 대칭 멀티플렉서를 갖춘 완전 차동 래치 기반 레지스터 파일로 줄였다. 표준 벤치마크에서 적층 CMOS 기준 설계보다 적층 전압 출렁임이 6.2배 줄고 전력 전달 손실이 평균 33.5% 낮았다. 면적 증가 18.4%는 같은 출렁임 감소를 위한 스위치드 커패시터 레귤레이터보다 4.9배 작았고, 문턱 전압 아래 균형 방식과 달리 최대 동작 주파수에 제한을 두지 않는다.[^p7] | 1저자 M. A. Gorywoda(Michał Andrzej Gorywoda), 마지막 저자 정완영 (2명) |
| 8 | 2024 | [VVIP: Versatile Vertical Indexing Processor for Edge Computing](https://doi.org/10.1145/3649329.3655676) · ACM/IEEE Design Automation Conference (DAC) 2024 | 단일 명령 다중 데이터(SIMD) 구조를 바탕으로 한 엣지 컴퓨팅용 다목적 수직 인덱싱 프로세서 VVIP다. 면적 효율이 높은 계산을 위해 수직 방향의 원본·목적지 인덱싱 명령을 맞춤으로 만들었고, 레지스터와 데이터 조향 논리를 더 써서 처리 모듈 안의 데이터 순서를 다시 배열한다. 레지스터 파일을 조회표나 누산기로 써서, 여러 비트를 차례로 처리하는 곱셈과 희소 데이터 연산을 지원한다. 벡터 프로세서에서 검증한 VVIP는 면적 증가가 2.8% 미만이고, 선형대수 벤치마크에서 1비트씩 차례로 곱하는 방식보다 평균 10.1배 빠르게 계산했으며, 구조가 정해지지 않은 희소 점별 합성곱에서 기존 제어 방식보다 평균 1.2배 성능이 좋았다.[^p8] | 1저자 H. Bae(Hyungjoon Bae), 마지막 저자 정완영 (3명) |

## 교수와 전문 분야

정완영 교수는 KAIST 전기및전자공학부 부교수이고 Circuit 디비전에 속하며, 전기및전자공학부 교수진 목록은 겸임학과를 AI시스템학과로 적는다.[^eeprof][^eelist] 연구실 Professor 페이지는 직함을 전기및전자공학부와 AI시스템학과의 Associate Professor로 적는다.[^prof] 반도체시스템공학과 교수진에도 연구분야 「반도체 시스템 및 집적회로」, 연구실 「Smart Energy-Efficient Design Lab」으로 올라 있다.[^ssep] 전기및전자공학부 교수 소개의 주요 연구분야는 AI & Machine Learning, Robotics & Control, Computer Architecture, Software Systems & Networking, Integrated Circuits & Semiconductor Systems, Quantum Science & Engineering, Semiconductor Devices & Nanotechnology이다.[^eeprof]

연구실 Professor 페이지에 따르면 교수는 서울대학교에서 전기공학 학사(2012)를, 미국 University of Michigan(Ann Arbor)에서 전기공학 박사(2017)를 받았고, 2017년 8월부터 2019년 8월까지 MIT Microsystems Technology Laboratories에서 박사후연구원으로 일했다.[^prof] 같은 페이지는 교수의 주된 연구 관심을 아날로그·디지털 회로 전반으로 적고, 그 가운데 원격 센서 기기와 IoT 응용 같은 자율 저전력 시스템과 CAD로 이끄는 회로 설계 자동화에 무게를 둔다고 적는다.[^prof] 박사 연구는 칩 위 에너지 하베스팅, 전력 관리, 센싱, 데이터 변환을 아우르는 저전력 아날로그 회로 기법이었고, MIT에서는 에너지 효율이 높은 추론 가속기와 보안 IoT 시스템 같은 디지털 회로로 연구를 넓혔다.[^prof] KAIST에서는 이런 기본 회로를 개선하고, 회로 구조를 자동으로 탐색·최적화하는 인공지능 기반 자동화 도구를 만드는 데 집중한다고 적는다.[^prof] 전기및전자공학부 교수 소개가 대표업적으로 드는 다섯 편은 2014–2017년의 에너지 하베스터, 전력 관리 장치, 스위치드 커패시터 DC-DC 변환기, 정전용량-디지털 변환기, SAR ADC용 비교기 논문으로, KAIST 부임 전 시기의 연구다.[^eeprof]

논문으로 보면 KAIST에서의 전문 분야는 네 갈래다. 전력 관리 회로와 그 회로 구조 자동 생성(대표 논문 1, 2),[^p1][^p2] 데이터 변환기와 온도 센서(대표 논문 3, 4),[^p3][^p4] 메모리 내 연산과 디지털 기본 회로(대표 논문 5, 6),[^p5][^p6] 프로세서 구조와 전력 전달(대표 논문 7, 8)이다.[^p7][^p8]

## 응용 분야

Professor 페이지는 연구실의 회로가 겨냥하는 대상을 작은 자율 시스템, 원격 센서 기기, IoT 응용으로 적는다.[^prof] 대표 논문 가운데 MAC-DO는 심층 신경망의 합성곱 계산을 가속하고(대표 논문 5), VVIP는 엣지 컴퓨팅용 프로세서다(대표 논문 8).[^p5][^p8] TickTockStack은 전력 밀도가 높은 디지털 칩의 전력 전달 손실 문제를 다룬다(대표 논문 7).[^p7] 구성원의 연구 주제에는 선형 광학 양자 컴퓨팅용 아날로그 전단 회로, 에너지 하베스팅 시스템, RF 회로도 있다.[^members]

## 구성원

연구실 누리집 Current Members 페이지의 26명이다(박사후연구원 2, 석사 후 연구원 1, 박사과정 11, 석사과정 12).[^members] 과정과 연구 주제는 각 카드의 표기이고, 「시작」은 각자 소개의 학력·경력 칸에서 현재 과정이나 직책이 시작된 연월이다. 박사과정 한 명의 카드에는 Lab Representative(랩 대표)가, 석사과정 한 명의 카드에는 Young-Ik Sohn 교수와 함께 지도받는 학생(Jointly Advised Student)이라는 표기가 있다. 박사후연구원 두 명은 이 연구실 박사 졸업생이기도 하다.[^members][^alumni] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Huan Van Nguyen | 박사후연구원 | 2025.2 | DC-to-DC Converter | 2 |
| Jooeun Kim | 박사후연구원 | 2026.8 | Analog Temperature Sensor | 4 |
| Minkyu Yang | 박사과정 | 2022.8 | Analog-to-Digital Converter (ADC) | 3, 4 |
| Dalta Imam Maulana | 박사과정 | 2022.8 | AI Accelerator |  |
| Michał Gorywoda | 박사과정 | 2022.8 | Power Delivery Network | 7 |
| Kyounghun Kang | 박사과정 | 2023.2 | Flip-Flop | 3, 4, 6 |
| Jihwan Cho | 박사과정 | 2023.2 | Compute-in-Memory (CIM) |  |
| Hyungjoon Bae | 박사과정 | 2023.2 | Central Processing Unit (CPU) | 8 |
| Seokhyun Jung | 박사과정 | 2024.9 | Digital Temperature Sensor |  |
| Minyoung Choi | 박사과정 | 2025.2 | Optimizer |  |
| Xinyu Chen | 박사과정 | 2026.3 | ML-based Circuit Generator |  |
| Huiseop Kim | 박사과정 (Lab Representative) | 2026.3 | Analog-to-Digital Converter (ADC) |  |
| JeongSeop Park | 박사과정 | 2025.2 | Transformer Optimization |  |
| Vu Thanh Tung | 연구원 | 2026.8 | DC-to-DC Converter |  |
| Quanghuy Le | 석사과정 | 2025.2 | Energy Harvesting Systems |  |
| Perapat Prugsamas | 석사과정 | 2025.9 | DC-to-DC Converter |  |
| Seoyeong Jang | 석사과정 | 2025.9 | Digital Temperature Sensor |  |
| Hao Wen Lau | 석사과정 | 2025.9 | ML-based Circuit Generator |  |
| Daegyeom Kim | 석사과정 | 2025.9 | Analog Front-end for Linear Optic Quantum Computing (Jointly Advised Student with Young-Ik Sohn) |  |
| Doyoung Park | 석사과정 | 2026.3 | Analog Front-end for Linear Optic Quantum Computing |  |
| Jeongwoo Park | 석사과정 | 2026.3 | Analog Front-end for Linear Optic Quantum Computing |  |
| Andrew James Lim | 석사과정 | 2026.3 | Compute-in-Memory (CIM) |  |
| Jimin Hwang | 석사과정 | 2026.3 | AI-Driven EDA |  |
| Junyeong Kim | 석사과정 | 2026.8 | RF Circuit |  |
| Sunkyu Chang | 석사과정 | 2026.8 | Flip-Flop |  |
| Yunju Kim | 석사과정 | 2026.8 | TBD |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사 5명과 석사 14명이다. 학위 연월과 진로는 누리집 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Doojin Jang | Ph.D. (2021.08) | Professor @ Chungju University |
| Huan Van Nguyen | Ph.D. (2025.02) | Post-Doctoral Researcher @ SEED |
| Changjoo Park | Ph.D. (2025.02) | Professor @ Incheon National University |
| Jeongmyeong Kim | Ph.D. (2026.08) | SK Hynix |
| Jooeun Kim | Ph.D. (2026.08) | Post-Doctoral Researcher @ SEED |
| Minki Jeong | M.S. (2022.02) | SK Hynix |
| Byeongmin Moon | M.S. (2022.02) | LX Semicon |
| Da Won Kim | M.S. (2023.02) | ScaleFlux (California, USA) |
| Sangwon Yoon | M.S. (2024.02) | Skaichips |
| Siheon Lee | M.S. (2024.02) | Samsung Electronics, Memory |
| Donghee Ko | M.S. (2024.02) | Samsung Electronics, System LSI |
| Jaehwan Jung | M.S. (2024.08) | SK Hynix |
| Gyubeom Hwang | M.S. (2025.02) | SK Hynix |
| Seungjun Lee | M.S. (2025.02) | SK Hynix |
| Youngin Park | M.S. (2025.02) | Samsung Electronics, Memory |
| Kwangwoo Lee | M.S. (2025.08) | Samsung Electronics, Mobile eXperience |
| Joohyung Yeon | M.S. (2026.02) | Samsung Electronics, Memory |
| Tung Thanh Vu | M.S. (2026.08) | Post-Master Researcher @ SEED |
| Zamri Fairuz Binti Nadhirah | M.S. (2026.08) | Samsung Electronics, System LSI |

## 최근 논문 목록 (2021–2026)

누리집 Publications 메뉴의 2021–2026년 논문 27편이다. International Journals 페이지의 학술지 7편과 International Conferences 페이지의 학회 논문 20편이며, 연도마다 학술지 논문을 먼저 적었다. 저자 순서와 제목·학술지·학회 표기는 누리집 그대로이고, 저자 이름 뒤 °는 누리집이 적은 공동 기여 표시다. 학술지 논문 뒤 괄호의 Invited와 학회 이름, 학회 논문 뒤 괄호의 Best Paper Award Nominations는 누리집이 그 논문에 붙인 표시다.[^pubs]

**2026**

- Jihwan Cho, Dalta Imam Maulana, Minkyu Yang, Changjoo Park, and Wanyeong Jung. "DRAMP: A Fully Parallel 1T1C DRAM Compute-in-Memory Macro With Mismatch-Robust Word-Line Ramp-Charging Operation". *IEEE Journal of Solid-State Circuits (JSSC), 2026*.
- Hyunsung Jeong°, Kyounghun Kang°, Jongeun Lee, and Wanyeong Jung. "B-Flex: Exploration of Broader Flip-Flop Design Space Based on FSM Exhaustive Search". *Proceedings of the 63rd ACM/IEEE Design Automation Conference (DAC), Jul 2026*.
- Xinyu Chen and Wanyeong Jung. "UNCHARTED: A Universal Circuit Design Hierarchical Model based on Auto-Regressive Spatio-Temporal Graph Neural Network with Exogenous Driving Inputs". *Proceedings of the 63rd ACM/IEEE Design Automation Conference (DAC), Jul 2026*.

**2025**

- Jooeun Kim, Jeongmyeong Kim, Minkyu Yang, Kyounghun Kang, and Wanyeong Jung. "A MOS-Based Temperature Sensor With Energy-Efficient Techniques". *IEEE Solid-State Circuits Letters (SSC-L), 2025 (Invited, A-SSCC 2024)*.
- Michał Andrzej Gorywoda and Wanyeong Jung. "TickTockStack: In-Datapath Current Imbalance Elimination Using Clocked Differential Logic in a Voltage Stacked Vector Processor". *IEEE/ACM International Conference On Computer Aided Design (ICCAD), 2025 (Best Paper Award Nominations)*.

**2024**

- Changjoo Park, Jeongmyeong Kim, Kyounghun Kang, Minkyu Yang, Byeongmin Moon, Siheon Lee, and Wanyeong Jung. "A High-Resolution Pipelined-SAR ADC Using Cyclically Charged Floating Inverter Amplifier". *IEEE Journal of Solid-State Circuits (JSSC), 2024 (Invited, A-SSCC 2023)*.
- Kyounghun Kang and Wanyeong Jung. "A Redundant-Transition-Free and Contention-Free Change-Sensing Flip-Flop". *IEEE Transactions on Circuits and Systems II: Express Briefs (TCAS-II), 2024 (Invited, ISCAS 2024)*.
- Donghee Ko°, Doojin Jang°, Da Won Kim, Jeongmyeong Kim, Byeongmin Moon, and Wanyeong Jung. "A Single/Dual-Output Switched-Capacitor DC-DC Converter with Geometrically Arranged Soft VCR Transitions". *2024 IEEE Asian Solid-State Circuits Conference (A-SSCC), 2024*.
- Jooeun Kim, Jeongmyeong Kim, Minkyu Yang, Kyounghun Kang, and Wanyeong Jung. "A -60 to 145° C, 216 fJ·K2 Energy-Efficient MOS-Based Temperature Sensor Achieving 71.8 mK Resolution". *IEEE Asian Solid-State Circuits Conference (A-SSCC), 2024*.
- Kyounghun Kang and Wanyeong Jung. "SeGen: Automatic Topology Generator for Sequencing Elements". *Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2024*.
- Jeongmyeong Kim, Changjoo Park, and Wanyeong Jung. "A 0.6-1 V VIN Soft-Switching Low Dropout Regulator with 31.3 A/mm2 Current Density, 99.99% Current Efficiency, and 2.04 fs FoM". *2024 IEEE Symposium on VLSI Technology and Circuits (VLSI-C), 2024*.
- Hyungjoon Bae, Da Won Kim, and Wanyeong Jung. "VVIP: Versatile Vertical Indexing Processor for Edge Computing". *Proceedings of the 61st ACM/IEEE Design Automation Conference (DAC), 2024*.
- MinKi Jeong and Wanyeong Jung. "MAC-DO: DRAM-Based Multi-Bit Analog Accelerator Using Output Stationary". *2024 IEEE International Symposium on Circuits and Systems (ISCAS), 2024*.
- Minkyu Yang, Changjoo Park, and Wanyeong Jung. "A Compact and Low-Power Column Readout Circuit based on Digital Delay Chain". *2024 IEEE International Symposium on Circuits and Systems (ISCAS), 2024*.
- Kyounghun Kang and Wanyeon Jung. "A Contention-Free and Redundant-Transition-Free Change-Sensing Flip-Flop". *2024 IEEE International Symposium on Circuits and Systems (ISCAS), 2024*.

**2023**

- Huan Nguyen and Wanyeong Jung. "ConverGenT: Automated Topology Generation and Analysis of Hybrid DC–DC Converters". *IEEE Transactions on Power Electronics (TPEL), 2023*.
- Jooeun Kim, Jeongmyeong Kim, Changjoo Park, Minkyu Yang, and Wanyeong Jung. "A Wide Range, Energy-Efficient Temperature Sensor Based on Direct Temperature–Voltage Comparison". *IEEE Solid-State Circuits Letters (SSC-L), 2023 (Invited, A-SSCC 2022)*.
- Changjoo Park, Jeongmyeong Kim, Kyounghun Kang, Minkyu Yang, Byeongmin Moon, Siheon Lee, and Wanyeong Jung. "A 74.0 dB-SNDR 175.4 dB-FoM Pipelined-SAR ADC Using a Cyclically Charged Floating Inverter Amplifier". *2023 IEEE Asian Solid-State Circuits Conference (A-SSCC), 2023*.
- Kyounghun Kang and Wanyeong Jung. "26TSPC: A Low Hold Time, Low Power Flip-Flop With Clock Path Optimization". *2023 IEEE International Symposium on Circuits and Systems (ISCAS), 2023*.
- Dalta Imam Maulana and Wanyeong Jung. "An Energy-Efficient Delay Insensitive Asynchronous Interface for Globally Asynchronous Locally Synchronous (GALS) System". *2023 IEEE International Symposium on Circuits and Systems (ISCAS), 2023*.

**2022**

- Jooeun Kim, Jeongmyeong Kim, Changjoo Park, Minkyu Yang, and Wanyeong Jung. "A-50 to 130° C, 38.69 pJ/conv Fully Integrated SAR Temperature Sensor Based on Direct Temperature-Voltage Comparison". *2022 IEEE Asian Solid-State Circuits Conference (A-SSCC), 2022*.
- Da Won Kim, Dalta Imam Maulana, and Wanyeong Jung. "Kyber Accelerator on FPGA Using Energy-Efficient LUT-Based Barrett Reduction". *2022 19th International SoC Design Conference (ISOCC), 2022*.
- Jangwon Suh and Wanyeong Jung. "FACTGen: Framework for Automated Circuit Topology Generator". *2022 19th International SoC Design Conference (ISOCC), 2022*.
- Jihwan Cho, Dalta Imam Maulana, and Wanyeong Jung. "A Near-Memory Radix Sort Accelerator with Parallel 1-bit Sorter". *2022 IEEE 30th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM), 2022*.

**2021**

- Doojin Jang, Jeongmyeong Kim, Unbong Lee, Jangwon Suh, and Wanyeong Jung. "Techniques for Analyzing and Reducing Voltage Conversion Ratio Transition Losses of Capacitive DC–DC Converters for Fast-DVS-Enabled Systems". *IEEE Transactions on Power Electronics (TPEL), 2021*.
- Joonhyuk Cho and Wanyeong Jung. "RectBoost: Start-Up Boosting for Rectenna Using an Adaptive Matching Network". *2021 IEEE International Symposium on Circuits and Systems (ISCAS), 2021*.
- Doojin Jang, Unbong Lee, Jeongmyeong Kim, Jangwon Suh, and Wanyeong Jung. "An On-Chip Dual-Output Switched-Capacitor DC- DC Converter with Fine-Grained Output Control". *2021 IEEE International Symposium on Circuits and Systems (ISCAS), 2021*.

## 수상과 장학

누리집 Current Members 페이지의 구성원 소개에 적힌 2021년 10월 이후 수상·장학 2건과, International Conferences 페이지가 논문에 붙인 Best Paper Award Nominations 표시 1건이다. 날짜는 페이지가 적은 연·월이고, 상 이름과 이름 표기는 페이지 그대로다.[^members][^pubs]

- 2025.2 · Best Design Award of Chip Design Contest, The 32nd Korean Conference on Semiconductors (KCS) (Minkyu Yang)
- 2025.12 · STEM Master's Excellence Scholarship, Korea Student Aid Foundation (Seoyeong Jang)
- 2025 · Best Paper Award Nominations, IEEE/ACM International Conference On Computer Aided Design (ICCAD) 2025: TickTockStack (Michał Andrzej Gorywoda, Wanyeong Jung)

## 연락과 위치

- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 교수 연구실: E3-2동 4201호, 전화 +82-42-350-7459[^home][^prof]
- 학생실: E3-2동 4207호(+82-42-350-7559), E4동 A304호(+82-42-350-4296)[^home]
- 교수 이메일: wanyeong@kaist.ac.kr[^prof][^eeprof]
[^p1]: J. Kim, C. Park, W. Jung, 2024 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), 1-2 (2024). <https://doi.org/10.1109/vlsitechnologyandcir46783.2024.10631485> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Nguyen, W. Jung, IEEE Transactions on Power Electronics 38, 11193-11220 (2023). <https://doi.org/10.1109/tpel.2023.3285548> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: C. Park 외, W. Jung, IEEE Journal of Solid-State Circuits 59, 3242-3252 (2024). <https://doi.org/10.1109/jssc.2024.3419759> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Kim 외, W. Jung, IEEE Solid-State Circuits Letters 8, 109-112 (2025). <https://doi.org/10.1109/lssc.2025.3559900> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: M. Jeong, W. Jung, 2024 IEEE International Symposium on Circuits and Systems (ISCAS), 1-5 (2024). <https://doi.org/10.1109/iscas58744.2024.10558271> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: K. Kang, W. Jung, IEEE Transactions on Circuits and Systems II: Express Briefs 71, 2559-2563 (2024). <https://doi.org/10.1109/tcsii.2024.3377714> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. A. Gorywoda, W. Jung, 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD), 1-9 (2025). <https://doi.org/10.1109/iccad66269.2025.11240897> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Bae, D. W. Kim, W. Jung, Proceedings of the 61st ACM/IEEE Design Automation Conference, 1-6 (온라인 2024-11-07). <https://doi.org/10.1145/3649329.3655676> 초록 기준(Semantic Scholar 등록 초록).
[^home]: SEED Lab 누리집 첫 화면 <https://seed.kaist.ac.kr/> (연구실 소개 문장, 연락처, 2026-10-23 열람)
[^research]: SEED Lab 누리집 Research 페이지 <https://seed.kaist.ac.kr/research/> (설계 계층과 층별 연구 주제, 2026-10-23 열람)
[^prof]: SEED Lab 누리집 Professor 페이지 <https://seed.kaist.ac.kr/people/professor/> (직함, 연구실 소개, 연구 분야, 연락처, Education, Biography, 2026-10-23 열람)
[^members]: SEED Lab 누리집 Current Members 페이지 <https://seed.kaist.ac.kr/people/current/> (구성원 카드와 소개, 2026-10-23 열람)
[^alumni]: SEED Lab 누리집 Alumni 페이지 <https://seed.kaist.ac.kr/people/alumni/> (Ph.D. Alumni, M.S. Alumni, 2026-10-23 열람)
[^pubs]: SEED Lab 누리집 Publications 메뉴: International Journals <https://seed.kaist.ac.kr/publications/journals/>, International Conferences <https://seed.kaist.ac.kr/publications/conferences/> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(정완영) <https://ee.kaist.ac.kr/professor/16846/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^eelist]: KAIST 전기및전자공학부 교수(전임교수) 목록 3쪽 <https://ee.kaist.ac.kr/professor-s1/?page=3> (정완영 항목의 직위·디비전·겸임학과, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (정완영 교수 항목, 2026-10-23 열람)

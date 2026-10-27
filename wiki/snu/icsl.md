# 반도체회로 및 시스템 설계 연구실 (Integrated Circuits & Systems Lab, ICSL)

**서울대학교 공과대학 전기·정보공학부 · 최재혁 교수**

- 분야: 아날로그·혼성 신호·RF 집적회로 설계, 저잡음 분수 분주 PLL과 주파수 합성기, D 대역·W 대역 주파수 합성과 국부 발진 신호 생성, 고속 메모리 인터페이스(DRAM·HBM)의 클럭 생성·분배와 클럭 데이터 복원, 메모리 인터페이스용 LDO와 전원 유발 지터 억제
- 대분야: 전기전자·반도체·광학
- 태그: 집적회로 설계[^home][^eceprof][^p1], 고속 유선 인터페이스[^home][^eceprof][^p4], 무선·이동통신[^home][^eceprof][^prof], 전자파 적합성·신호 무결성[^p6][^p7], 전력 관리 집적회로[^p6], 주파수 합성·클럭 생성 회로[^p3]
- 홈페이지: <https://www.icsl.snu.ac.kr/>
- 근거와 출처: [ICSL 근거 페이지](icsl-sources.md)

> 새로운 무선·유선 통신 표준을 위한 고속 혼성 신호·RF 집적회로를 설계하는 연구실이다. 다중 표준 무선 송수신기, 고속 인터커넥션과 클럭 생성기, 전원 관리 IC를 연구 주제로 들고, 지터가 낮은 PLL과 메모리 인터페이스의 클럭·전원 회로를 칩으로 만들어 왔다.[^prof][^home][^p1][^p4][^p6]

## 무엇을 연구하나

연구실은 서울대학교 공과대학 전기·정보공학부 최재혁 교수가 이끄는 반도체회로 및 시스템 설계 연구실(Integrated Circuits & Systems Lab, ICSL)이다.[^ecelabd][^home] 학과 연구실 소개는 연구 분야를 「반도체회로 및 시스템 설계」로 적고,[^ecelabd] 학과 연구실 목록은 이 연구실을 집적회로, 차세대 컴퓨팅, 통신 시스템, 회로 및 시스템의 네 연구그룹에 올린다.[^ecelab] 누리집 첫 화면은 연구 주제로 다중 표준 무선 송수신기 설계(Multi-standard wireless transceiver design), 고속 인터커넥션과 클럭 생성기(High-speed interconnection & clock generators), 전원 관리 IC(Power management IC)의 셋을 든다.[^home] 송수신기는 신호를 보내는 송신기와 받는 수신기를 한데 묶은 장치이고, 인터커넥션은 칩과 칩, 칩 안의 회로 사이를 잇는 신호 연결이며, 클럭은 회로들이 동작 시점을 맞추는 데 쓰는 일정한 주기의 반복 신호다.

누리집 교수 소개는 교수의 연구 관심을 새로 나오는 무선·유선 통신 표준을 위한 고속 혼성 신호(아날로그 신호와 디지털 신호를 함께 다루는 방식) 집적회로와 RF(Radio Frequency, 전파로 쓰이는 주파수 대역의 전기 신호) 집적회로로 적는다.[^prof] 학과 교수 소개는 전공을 「집적회로 및 시스템 설계」로 적고, Research Interest로 아날로그/혼성신호/RF 회로 설계, 초고속/저전력 메모리 인터페이스와 칩 인터커넥트 회로 설계, 차세대 무선통신 반도체 회로 및 시스템 설계를 든다.[^eceprof] 최근 논문 목록 42편 가운데 26편이 제목에 PLL(Phase-Locked Loop, 위상 고정 루프: 출력 신호의 위상을 기준 신호의 위상에 맞추도록 되먹임으로 조절해, 기준 신호에 고정된 주파수의 신호를 만드는 회로)을 달고, 35편이 제목에 지터(jitter, 신호가 바뀌는 시점이 이상적인 시점에서 벗어나 흔들리는 정도)를 적는다.[^pubs]

대표 논문으로 보면 연구는 네 갈래로 모인다. 첫째, 출력 주파수를 기준 주파수의 정수배가 아닌 분수배로도 맞출 수 있는 분수 분주(fractional-N) 디지털 PLL(위상 비교와 루프 조절을 디지털 회로로 처리하는 PLL)에서 지터를 낮추는 회로와 디지털 보정 방법이다. 대표 논문 1은 여러 보정 값을 함께 빠르게 맞추는 보정 알고리즘을 넣었고, 대표 논문 2는 양자화 오차(값을 정해진 단계로 끊어 나타낼 때 생기는 오차)를 보상하는 위상 검출기와 빠른 보정 방법을 제안했다.[^p1][^p2] 둘째, 서브테라헤르츠(sub-THz, 테라헤르츠 바로 아래의 주파수 범위) 대역에 드는 D 대역의 신호를 낮은 지터로 넓은 주파수 범위에서 만드는 주파수 합성기다. 대표 논문 3은 50GHz 대역 서브샘플링 PLL(출력 신호를 기준 신호로 직접 표본화해 위상 오차를 재는 PLL)과, 고조파(기본 주파수의 정수배 주파수 성분)를 키우는 주파수 체배기(입력 주파수의 정수배 주파수 신호를 내는 회로)를 두 단계로 엮었다.[^p3] 셋째, DRAM(Dynamic Random Access Memory, 저장한 내용을 주기적으로 다시 써 주어야 유지되는 반도체 메모리)·HBM(High Bandwidth Memory, DRAM 칩 여러 개를 쌓아 많은 신호선으로 연결해 한꺼번에 많은 데이터를 주고받는 메모리) 같은 고속 메모리 인터페이스에서 클럭을 적은 전력으로 나르고 만드는 회로와, 칩 안에서 클럭의 지터를 재는 회로다. 대표 논문 4는 낮은 주파수의 클럭 하나만 보내고 데이터 핀 바로 앞에서 직교 클럭(위상이 한 주기의 4분의 1씩 어긋난 클럭 신호들)을 만드는 클럭 분배 방식을, 대표 논문 5는 주파수와 지터 크기가 제각각인 클럭을 재는 온칩(칩 안에 함께 넣은) 지터 측정 회로를 내놓았다.[^p4][^p5] 넷째, HBM 인터페이스의 클럭 버퍼에 전원을 대는 LDO(Low-Dropout regulator, 입력 전압과 출력 전압의 차이가 작아도 일정한 출력 전압을 유지하는 선형 전압 조정기)와 레귤레이터 묶음으로, 전원 공급망의 잡음과 전압 강하가 일으키는 지터를 줄이는 연구다.[^p6][^p7]

최근 논문 목록에는 이 밖에도 5G FR1 대역(5G 이동통신 표준이 정한 주파수 범위 가운데 하나)을 위한 넓은 범위의 국부 발진 신호(LO, Local Oscillator: 송수신기 안에서 만들어, 주고받는 신호의 주파수를 다른 주파수로 옮기는 데 쓰는 신호) 생성기(JSSC 2023), 103.5GHz PLL(ISSCC 2023, SSC-L 2023), 264−287GHz CMOS(Complementary Metal-Oxide-Semiconductor, n형·p형 트랜지스터를 짝지어 만드는 반도체 회로 방식) 신호원(ISSCC 2023), W 대역(파장이 밀리미터 단위인 밀리미터파 가운데 한 주파수 대역) 직교 국부 발진 신호 생성기(RFIC 2026)가 있다.[^pubs] 클럭 쪽에는 링 발진기 기반 주입 고정(injection locking, 외부 신호를 발진기에 넣어 발진기의 위상과 주파수를 그 신호에 맞추는 방식) 클럭 곱셈기(JSSC 2023), MDLL(Multiplying Delay-Locked Loop, 링 발진기의 전환 시점을 기준 클럭의 전환 시점으로 주기적으로 바꿔 넣어 기준 주파수의 정수배 클럭을 만드는 회로, JSSC 2025), HBM 인터페이스용 주입 고정 직교 클럭 생성기(ISSCC 2025), 레인(lane, 데이터를 나르는 병렬 신호 경로 하나)마다 데이터 속도가 달라지는 상황을 다루는 디지털 CDR(Clock and Data Recovery, 받은 데이터 신호에서 타이밍 정보를 뽑아 클럭을 되살리고 그 클럭으로 데이터를 읽어 내는 회로, VLSI 2026)이 있다.[^pubs] 전원 쪽에는 외부 클럭 없이 동작하는 디지털 LDO(ESSCIRC 2021)가, 데이터 변환 쪽에는 플래시 방식과 VCO(Voltage-Controlled Oscillator, 입력 전압으로 출력 주파수를 바꾸는 발진기) 방식을 함께 쓰는 ADC(Analog-to-Digital Converter, 아날로그 신호를 디지털 값으로 바꾸는 회로, CICC 2023·SSC-L 2025)가 있다.[^pubs]

## 주요 연구 주제

### 1. 저잡음 분수 분주 PLL

대표 논문 1과 2는 분수 분주 디지털 PLL에서 델타-시그마 변조기(ΔΣM, 입력 값을 적은 단계의 값으로 끊어 나타내되 그 오차를 되먹여 오차 잡음을 높은 주파수 쪽으로 옮기는 변조 회로)가 남기는 양자화 오차를 없애 대역 안 잡음을 줄이고, 그 효과가 기대는 디지털 보정을 빠르게 하는 방법을 다룬다. 대표 논문 1은 면적을 아끼려고 작은 인덕터를 쓴 발진기의 나쁜 위상 잡음(신호 위상의 무작위 흔들림)을 넓은 PLL 대역폭으로 억누르고, 디지털-시간 변환기(DTC, 디지털 값에 따라 신호의 지연 시간을 바꾸는 회로)와 위상 선택기로 양자화 잡음과 DTC의 열잡음(도체 안 전자의 열운동 때문에 생기는 잡음)을 줄였다. 오차 제곱의 평균이 줄어드는 방향으로 계수를 조금씩 고쳐 가는 LMS(Least Mean Squares) 알고리즘을 쓰는 기존 보정기는 수렴이 느려, 새 측정값이 들어올 때마다 지금까지의 오차 제곱합을 가장 작게 하는 계수를 다시 계산하는 RLS(Recursive Least Squares) 알고리즘 기반 다변수 보정기로 보정 시간을 7.2μs 미만으로 줄였다.[^p1] 대표 논문 2는 양자화 오차 보상 뱅뱅 위상 검출기(QEC-BBPD, 뱅뱅 위상 검출기는 두 신호 가운데 어느 쪽이 앞서는지만 판정하는 위상 검출기)로 보상 과정의 열잡음을 줄여 대역 안 위상 잡음과 rms 지터를 낮추고, 그 비선형성(입력과 출력이 비례하지 않는 성질)을 없애는 보정을 직교 다항식 기반 LMS로 빠르게 했다.[^p2] 최근 논문 목록에는 비선형성 복제 기법을 쓰는 분수 분주 샘플링 PLL(ISSCC 2024, JSSC 2026)과 전압 영역 양자화 오차 상쇄를 쓰는 서브샘플링 PLL(ISSCC 2021, JSSC 2024), DTC의 2·3차 비선형성 상쇄를 쓰는 링 DCO(Digitally Controlled Oscillator, 디지털 값으로 주파수를 바꾸는 발진기) 기반 디지털 PLL(ISSCC 2021, JSSC 2022)도 있다.[^pubs]

### 2. D 대역·W 대역 주파수 합성과 국부 발진 신호

대표 논문 3은 기존 서브테라헤르츠 주파수 합성기의 구조적 한계를 넘어 낮은 지터와 넓은 주파수 조정 범위를 함께 얻으려고, 3차 고조파(기본 주파수의 세 배 주파수 성분)가 풍부한 발진기를 쓴 50GHz 대역 서브샘플링 PLL 뒤에 고조파를 키우는 주파수 체배기를 붙인 두 단계 구조를 설계했다. 40nm CMOS 공정으로 설계한 합성기는 144–162GHz의 주파수 조정 범위를 보였다.[^p3] 최근 논문 목록에는 상보형 전원 차단(power-gating) 주입 고정 주파수 체배기 기반 위상 검출기를 쓰는 D 대역 PLL(ASSCC 2024, SSC-L 2025), 빠른 직교 보정을 갖춘 85.5–94.5GHz W 대역 직교 국부 발진 신호 생성기(RFIC 2026), 확장한 루프 대역폭의 103.5GHz PLL(ISSCC 2023, SSC-L 2023), 102GHz W 대역 PLL(ISSCC 2021, JSSC 2022), 0.6−7.7GHz 국부 발진 신호 생성기(ISSCC 2023)와 5G FR1 대역용 넓은 범위 국부 발진 신호 생성기(JSSC 2023)가 있다.[^pubs]

### 3. 고속 인터페이스 클럭의 생성·분배와 측정

대표 논문 4는 고속 DRAM 인터페이스에서 높은 주파수의 직교 클럭 네 개를 긴 배선으로 많은 데이터 핀까지 나르는 기존 방식 대신, 낮은 주파수의 단일 위상 클럭 하나만 보내고 데이터 핀 바로 앞에서 디지털 PLL 기반 직교 클럭 생성기로 직교 클럭을 만드는 방식을 제시했다. 이 생성기는 입력 클럭의 지터를 거를 수 있으면서 1mW 미만의 전력을 쓴다.[^p4] 대표 논문 5는 지터 크기에 따라 양자화기(입력 값을 정해진 단계의 값으로 바꾸는 회로)의 분해능(구별할 수 있는 가장 작은 차이)을 바꾸는 기법으로, 주파수와 지터 크기가 제각각인 임의의 클럭에 대해 칩 안에서 지터 분포를 재는 회로를 만들었다.[^p5] 최근 논문 목록에는 HBM 인터페이스의 저전력 클럭 분배를 위한 850μW 주입 고정 직교 클럭 생성기(ISSCC 2025), 전원 차단 기법을 쓰는 12.24GHz MDLL(VLSI 2023, JSSC 2025), 레인마다 데이터 속도가 달라지고 SSC(Spread-Spectrum Clocking, 클럭 주파수를 일정 범위에서 계속 바꿔 방사 에너지를 여러 주파수로 퍼뜨리는 방식)가 깊게 걸린 상황을 다루는 16.8–33.6Gb/s 디지털 CDR(VLSI 2026)도 있다.[^pubs]

### 4. 메모리 인터페이스의 전원 잡음 억제

HBM 인터페이스의 쓰기 데이터 스트로브(WDQS, 쓰기 데이터의 시점을 알려 주는 기준 신호) 버퍼는 부하 전류가 갑자기 바뀌어, 복잡한 전원 공급망(PDN, Power Delivery Network)에서 큰 전압 강하가 생기고 전원 유발 지터(PSIJ, Power-Supply-Induced Jitter)가 커진다. 대표 논문 6은 부하 전류의 크기와 시점이 호스트가 보내는 명령에 따라 정해진다는 메모리 시스템의 성질을 이용해, 그 전류가 생기는 때에 맞춰 같은 크기의 전류를 미리 공급하는 명령 인식 하이브리드 LDO(CA-HLDO)를 만들었다.[^p6] 대표 논문 7은 WDQS 클럭 분배망을 따라 있는 모든 PSIJ 원인을 줄이려고, WDQS 버퍼용 스트로브 촉발 디지털 LDO와 뒤따르는 중계기용 국소 복제 레귤레이터를 묶은 종합 방식을 제시했다.[^p7] 최근 논문 목록에는 명령 인식 하이브리드 LDO를 다룬 학회 논문(ISSCC 2025)과, 외부 클럭 없이 넓은 범위에서 표본화 주파수를 바꾸는 디지털 LDO(ESSCIRC 2021)도 있다.[^pubs]

## 대표 논문

랩 PUBLICATIONS 페이지의 2021–2026년 논문 가운데 최재혁 교수가 서울대에 온 뒤 서울대 소속으로 낸 2024–2026년 학술지·학회 논문을 연구 갈래마다 골랐다. 일곱 편 모두 최재혁 교수가 마지막 저자이고, 랩 목록은 교수 이름에 \*를 붙인다. 주요 저자 칸의 =는 랩이 Equally-Credited Authors로 표시한 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [A Low-Jitter and Compact-Area Fractional-N Digital PLL With Fast Multi-Variable Calibration Using the Recursive Least-Squares Algorithm](https://doi.org/10.1109/jssc.2024.3456105) · IEEE Journal of Solid-State Circuits | 지터가 낮고 면적이 작으며 여러 보정 값을 빠르게 맞추는 분수 분주 디지털 PLL(DPLL)을 제시했다. 실리콘 면적을 아끼려고 LC 전압 제어 발진기(LC VCO, 인덕터와 커패시터의 공진으로 발진하며 입력 전압으로 주파수를 바꾸는 발진기)에 세 바퀴 감은 작은 인덕터를 넣었고, 그래도 지터를 낮게 하려고 PLL의 대역폭을 넓게 설계해 이 VCO의 나쁜 위상 잡음(신호 위상의 무작위 흔들림)을 억눌렀다. 대역 안 잡음을 줄이려고 디지털-시간 변환기(DTC, 디지털 값에 따라 신호의 지연 시간을 바꾸는 회로)로 델타-시그마 변조기(ΔΣM)의 양자화 잡음을 없앴고, 위상 선택기(PSEL)로 DTC의 열잡음을 줄였다. 이런 지터 저감 기법의 효과는 디지털 백그라운드 보정(회로를 멈추지 않고 동작 중에 계속하는 보정)에 달려 있는데, 최소 평균 제곱(LMS) 알고리즘을 쓰는 기존 다변수 보정기(MVC)는 수렴 시간이 길다. 이를 극복하려고 이분 좌표 하강(DCD) 알고리즘을 써서 적당한 구현 비용으로 빠르게 보정할 수 있는 재귀 최소 제곱(RLS) 기반 MVC를 도입했다. 제안한 DCD-RLS MVC의 보정 시간은 7.2μs 미만으로 LMS MVC보다 40배 빨랐다. 이 DPLL은 정수 분주에 가까운 채널에서 88fsrms 지터와 68dBc 분수 스퍼(원하는 출력 주파수 밖에 생기는 원치 않는 주파수 성분)를 보였고, 40nm CMOS 공정으로 만들어 능동 면적 0.12mm²만 차지하며 15.7mW를 썼다.[^p1] | 1저자 Seheon Jang·Munjae Chae(랩 표시 =), 마지막 저자 최재혁 |
| 2 | 2025 | [A Low-Jitter Fractional-N Digital PLL Using a Quantization-Error-Compensating BBPD and an Orthogonal-Polynomial-Based LMS Calibration](https://doi.org/10.1109/jssc.2025.3611417) · IEEE Journal of Solid-State Circuits | 10.0–11.5GHz 분수 분주 디지털 PLL을 제시했다. 핵심인 양자화 오차 보상 뱅뱅 위상 검출기(QEC-BBPD, 뱅뱅 위상 검출기는 두 신호 가운데 어느 쪽이 앞서는지만 판정하는 위상 검출기)는 델타-시그마 변조기의 양자화 오차를 없애는 데 필요한 정적 지연과 동적 지연을 함께 최소로 줄인다. 양자화 오차를 보상하는 과정에서 더해지는 열잡음도 줄이므로 DPLL이 낮은 대역 안 위상 잡음과 낮은 rms 지터를 얻을 수 있다. 이와 함께 QEC-BBPD의 비선형성을 없애는 보정을 적은 하드웨어 부담으로 빠르게 하려고 직교 다항식 기반 최소 평균 제곱 다변수 보정(OP-LMS MVC)을 제안했다. 40nm CMOS 공정으로 만든 DPLL은 실리콘 0.12mm²를 차지하고 14.4mW를 썼으며, 10.9GHz 근처의 분수 분주 주파수에서 rms 지터는 64fs, 가장 나쁜 분수 스퍼는 −62.8dBc였다. 최신 분수 분주 PLL들 가운데 가장 낮은 대역 안 위상 잡음과, 곱셈 배수 N으로 정규화한 지터-전력 성능 지수(FoMjitter,N) −272.2dB로 가장 좋은 값을 얻었다.[^p2] | 1저자 Munjae Chae·Seheon Jang(랩 표시 =), 마지막 저자 최재혁 |
| 3 | 2025 | [A Low-Jitter and Wide-Frequency-Range D-Band Frequency Synthesizer With a Subsampling PLL and a Harmonic-Boosting Frequency Multiplier](https://doi.org/10.1109/jssc.2024.3523474) · IEEE Journal of Solid-State Circuits | 넓은 주파수 조정 범위(FTR)에서 지터가 매우 낮은 출력 신호를 만들 수 있는 D 대역 주파수 합성기를 제시했다. 기존 서브테라헤르츠(sub-THz) 주파수 합성기의 구조적 한계를 넘어 낮은 지터와 넓은 FTR을 함께 얻으려고 두 단계 구조를 설계했다. 첫 단계는 3차 고조파가 풍부한 class-F 전압 제어 발진기(VCO)를 쓴 50GHz 대역 서브샘플링 PLL(SSPLL, 출력 신호를 기준 신호로 직접 표본화해 위상 오차를 재는 PLL)이고, 둘째 단계의 고조파 강화 주파수 체배기(FM)와 함께 동작한다. 40nm CMOS 공정으로 설계한 이 합성기는 11.8%, 곧 144–162GHz의 넓은 FTR을 보였다. 대역 안 위상 잡음을 억누르는 높은 이득의 서브샘플링 위상 검출기와 대역 밖 위상 잡음을 낮추는 class-F VCO 덕분에 가장 낮은 rms 지터(39fsrms)를 얻었다. 3차 고조파가 풍부한 class-F VCO와 고조파 강화 FM의 조합이 D 대역 출력 신호를 전력 효율적으로 만들어, FTR이 5%를 넘는 최신 W/D 대역 주파수 합성기 가운데 가장 좋은 지터 성능 지수(FOM)도 얻었다.[^p3] | 1저자 Seohee Jung, 마지막 저자 최재혁(랩 목록은 Heein Yoon과 최재혁에게 \*를 붙인다) |
| 4 | 2025 | [A Digital-PLL-Based Quadrature Clock Generator for a Low-Power and Jitter-Filtering-Capable Clock Distribution Scheme in High-Speed DRAM Interfaces](https://doi.org/10.1109/jssc.2024.3433026) · IEEE Journal of Solid-State Circuits | 고속 DRAM 인터페이스를 위해, 디지털 PLL 기반 직교 클럭 생성기(QCG)를 쓰는 전력이 적고 지터를 걸러 낼 수 있는 클럭 분배 방식을 제시했다. 기존 클럭 분배는 높은 주파수 f_CLK의 직교 클럭 신호 네 개를 긴 채널로 많은 DQ(데이터 입출력 핀)에 보내 전력을 많이 쓴다. 제안한 방식은 훨씬 낮은 주파수(f_CLK의 8분의 1)의 단일 위상 클럭 하나만 보내므로 클럭 분배 전력을 32분의 1로 크게 줄일 수 있다. 그런 다음 QCG가 DQ 바로 앞에서 듀티 사이클(한 주기 가운데 신호가 켜져 있는 시간의 비율) 25%의 정밀한 직교 클럭을 만든다. QCG는 f_CLK의 8분의 1에서 동작하는 PLL을 바탕으로 해 입력 클럭의 지터를 거를 수 있으면서 1mW 미만의 전력을 쓴다. 주파수와 상관없는 방법으로 직교 오차를 바로잡아 동작 주파수 범위를 크게 넓힐 수 있고, IDLE 모드와 ACTIVE 모드 사이를 바로 전환하게 하는 동기식 모드 전환 분주기(SMS-DIV)도 제시했다. 40nm CMOS로 만든 QCG는 2GHz 직교 출력 신호를 만드는 데 900μW를 썼고, 1–4GHz 범위에서 0.5° 미만의 매우 작은 직교 오차를 꾸준히 보였다.[^p4] | 1저자 Yuhwan Shin, 마지막 저자 최재혁 |
| 5 | 2026 | [A Versatile On-Chip Jitter Measurement Circuit with Dynamic Quantizer-Resolution Adaptation for Arbitrary Clocks Across 1–8GHz and 20–130pspp Jitter](https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577405) · VLSI Technology and Circuits 2026 | 여러 용도로 쓸 수 있는 온칩 지터 측정(OCJM) 회로를 제시했다. 지터 크기에 따라 양자화기(입력 값을 정해진 단계의 값으로 바꾸는 회로)의 분해능을 최적으로 맞추는 동적 양자화기 분해능 적응(DQRA) 기법으로, 주파수와 지터가 크게 달라지는 임의의 클럭에 대해서도 지터 히스토그램(값의 분포를 구간별 개수로 나타낸 그림)을 정확히 만든다. 28nm CMOS로 구현한 시제품은 양자화기 15개만으로 1–8GHz 주파수에서 20–130ps_pp(pp는 가장 큰 값과 가장 작은 값의 차이) 크기의 클럭 지터를 쟀다.[^p5] | 1저자 Junseok Lee·Chanwoong Hwang(랩 표시 =), 마지막 저자 최재혁 |
| 6 | 2026 | [A Command-Aware Hybrid LDO With Ultra-Small Voltage Droop and Fast Settling Time for Power-Supply-Induced Jitter Mitigation in HBM Interfaces](https://doi.org/10.1109/jssc.2025.3602459) · IEEE Journal of Solid-State Circuits | 고대역폭 메모리(HBM) 인터페이스의 쓰기 데이터 스트로브(WDQS) 버퍼에서 생기는 전압 강하와 전원 유발 지터(PSIJ)를 줄이는 명령 인식 하이브리드 LDO(CA-HLDO)를 제시했다. HBM 표준에서 WDQS 버퍼는 부하 전류가 갑자기 바뀌어, 복잡한 전원 공급망(PDN) 환경에서 큰 전압 강하를 겪는다. 기존 아날로그 LDO와 사건 구동 LDO는 루프 대역폭이 제한되어 큰 전압 강하와 PSIJ 악화를 막기 어렵다. CA-HLDO는 부하 전류의 크기와 시점이 호스트가 보내는 명령에 따라 정해진다는 메모리 시스템의 고유한 성질을 이용해, 부하 전류가 생기는 바로 그때 그에 맞는 전류를 미리 공급해 전압 강하를 최소로 줄이고 안정 시간을 줄인다. 구조에는 공급 전류의 크기를 동적으로 맞추는 적응기와 공급 시점을 보정하는 제어 신호 생성기(CSG)가 들어 있다. 40nm CMOS로 만든 CA-HLDO는 작은 출력 커패시터와 최소한의 대기 전류로 10mV 미만의 전압 강하와 400ps 안정 시간을 얻었고, 모든 주파수에서 10dB를 넘는 전원 잡음 제거비(PSR)를 제공해 잡음이 많고 복잡한 PDN이 일으키는 PSIJ를 효과적으로 줄였다.[^p6] | 1저자 Jaeho Kim·Myeongho Han(랩 표시 =), 마지막 저자 최재혁(랩 목록은 Younghyun Lim과 최재혁에게 \*를 붙인다) |
| 7 | 2026 | [A Comprehensive Power-Supply-Induced Jitter Mitigation Scheme for HBM Interfaces Using a Strobe-Triggered Digital LDO and Local Replica Regulators Achieving 10.7mV Voltage Droop and 1.4ns Settling Time](https://doi.org/10.1109/cicc65509.2026.11509607) · CICC 2026 | HBM 인터페이스의 쓰기 데이터 스트로브(WDQS) 클럭 분배망(CDN)을 따라 있는 모든 PSIJ 원인을 줄이는 종합 방식을 제시했다. 이 방식은 WDQS 버퍼용 스트로브 촉발 디지털 LDO(ST-DLDO)와, 그 뒤를 잇는 중계기(repeater)용 국소 복제 레귤레이터(LRR)로 이루어진다. 레귤레이터마다 10pF 출력 커패시터와 IDLE 모드 대기 전류 3.2μA만으로 전압 강하를 줄여 PSIJ를 크게 억누르고, 드롭아웃 전압 100mV와 전체 주파수 범위에서 적어도 -10dB의 전원 잡음 제거비(PSR)를 유지한다. WDQS/2 주파수 0.4–3.5GHz의 넓은 범위를 지원한다. 28nm CMOS 공정으로 만든 구조는 0.005mm²의 ST-DLDO와 각각 0.003mm²인 여러 LRR을 담아, 전압 강하가 작은 최신 LDO들 가운데 가장 좋은 성능 지수(FoM)를 얻었다.[^p7] | 1저자 Myeongho Han·Jaeho Kim(랩 표시 =), 마지막 저자 최재혁 |

## 교수와 전문 분야

최재혁 교수는 서울대학교 공과대학 전기·정보공학부 교수다.[^eceprof] 학과 교수 소개는 학위를 공학박사, 전공을 「집적회로 및 시스템 설계」, 분야를 「반도체회로 및 시스템 설계」로 적는다.[^eceprof] 누리집 교수 소개 Biography는 교수를 IEEE Senior Member로 소개한다.[^prof]

누리집 Biography에 따르면 교수는 2003년 서울대학교에서 전기공학 학사(summa cum laude)를, 2008년과 2010년 미국 Georgia Institute of Technology에서 전기컴퓨터공학 석사와 박사를 받았다.[^prof] 2010–2011년 미국 샌디에이고의 Qualcomm에서 다중 표준 셀룰러 송수신기 설계에 참여했고(경력 칸 표기 Senior Engineer), UNIST 조교수·부교수와 KAIST 부교수(2019–2023)를 거쳐 2023년부터 서울대학교에 있다.[^prof][^eceprof] UNIST 재직 시작은 Biography가 2012년, 누리집 경력 칸과 학과 교수 소개가 2011년으로 적고, 서울대 직위는 학과 교수 소개가 2023년부터 교수로, 누리집 경력 칸이 2023–2025년 부교수, 2026년부터 교수로 적는다.[^prof][^eceprof]

누리집 Biography와 Professional Activities and Awards 칸에 따르면 교수는 2017–2025년 ISSCC(IEEE International Solid-State Circuits Conference)의 기술 프로그램 위원회(TPC, Technical Program Committee) 위원(RF 분과)이었고, ISSCC 극동 지역 기술 프로그램 위원회(Far-East Regional TPC)의 간사(Secretary, 2021–2023)와 부위원장(Vice Chair)·위원장(Chair)을 지냈으며, Biography는 지금 ISSCC 2027 RF 분과의 부위원장(Vice Chair)을 맡고 있다고 적는다. 2021년부터 A-SSCC(IEEE Asian Solid-State Circuits Conference) TPC 위원(RF & Wireless 분과)이고, ESSCIRC(IEEE European Solid-State Circuits Conference, 활동 칸 표기는 IEEE European Solid-State Electronic Research Conference(ESSERC))의 TPC 위원도 지냈다. 2020–2021년 IEEE 고체회로 학회(Solid-State Circuits Society, SSCS)의 Distinguished Lecturer였고, 2022년부터 학술지 IEEE Journal of Solid-State Circuits(JSSC)의 Associate Editor이며, 2016년부터 IEEE Circuits and Systems for Communication 기술 위원회 위원이다.[^prof] 수상으로는 IEEE–IEIE Joint Award: Young Engineer of the Year(2020)와 IEEE 2025 Takuo Sugano Award for Outstanding APAC Paper를 적고, 2021년과 2025년 Korea Semiconductor Design Contest의 President's Award를 받았다고 적는다.[^prof] 랩 AWARDS & HONORS 페이지는 2023년 KAIST-Samsung Electronics Cooperation Center의 Best Patent Award를 교수의 수상으로 올린다.[^awards]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 양자화 오차 상쇄와 빠른 디지털 보정으로 지터를 낮춘 분수 분주 디지털 PLL이다(대표 논문 1, 2).[^p1][^p2] 둘째, 서브테라헤르츠 D 대역에서 지터가 낮고 주파수 범위가 넓은 주파수 합성기다(대표 논문 3).[^p3] 셋째, 고속 메모리 인터페이스의 저전력 클럭 분배와 직교 클럭 생성, 칩 안의 지터 측정이다(대표 논문 4, 5).[^p4][^p5] 넷째, HBM 인터페이스의 전압 강하와 전원 유발 지터를 줄이는 LDO와 레귤레이터 구성이다(대표 논문 6, 7).[^p6][^p7]

## 응용 분야

누리집 교수 소개는 연구 대상을 새로 나오는 무선·유선 통신 표준을 위한 집적회로로 적고,[^prof] 학과 교수 소개는 차세대 무선통신 반도체 회로와 초고속·저전력 메모리 인터페이스를 Research Interest로 든다.[^eceprof] 대표 논문은 고속 DRAM 인터페이스의 클럭 분배,[^p4] HBM 인터페이스의 클럭 버퍼 전원[^p6][^p7]을 대상으로 하고, 최근 논문 목록에는 5G FR1 대역용 국부 발진 신호 생성기가 있다.[^pubs] 구성원 개인 페이지의 특허 목록에는 5G 통신의 넓은 주파수 대역을 덮는 국부 발진 신호 생성기, 여러 레인의 고속 통신 장치에 쓰는 CDR 회로, 의사 차동 위상차 변조를 쓰는 송신기·수신기와 이를 포함한 메모리 시스템 특허가 있다.[^mpages] 졸업생의 진로로는 Samsung Electronics, Samsung(미국 San Jose), Qualcomm(미국 San Diego), Apple Inc., Neuralink와 UNIST·Kyung Hee University의 Assistant Professor가 있다.[^alumni]

## 구성원

2026년 10월 25일 랩 MEMBERS 페이지 기준이다. 박사후연구원(Postdoctoral Researcher) 1명, 박사과정(Ph.D.) 6명, 석박사통합과정(Integrated Master's & Ph.D.) 14명, 학부 연구생(Undergraduate Student) 2명이다. 과정 칸은 카드의 과정 표기를 옮긴 것이고, 박사후연구원 신유환의 카드는 소속을 Inter-university Semiconductor Research Center, Seoul National University로 적는다. 시작 칸은 카드의 「YYYY ~ Present」 연도이고, 이메일은 카드에 적힌 학교 이메일이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 신유환 (Yuhwan Shin) | 박사후연구원 (Inter-university Semiconductor Research Center) | 2026 | yuhwan.shin@snu.ac.kr | 4 |
| 한명호 (Myeongho Han) | 박사과정 | 2024 | myeongho@snu.ac.kr | 6, 7 |
| 장세헌 (Seheon Jang) | 박사과정 | 2024 | s.jang@snu.ac.kr | 1, 2 |
| 김재호 (Jaeho Kim) | 박사과정 | 2024 | jaehokim@snu.ac.kr | 3, 6, 7 |
| 채문재 (Munjae Chae) | 박사과정 | 2024 | munjaechae@snu.ac.kr | 1, 2 |
| 정서희 (Seohee Jung) | 박사과정 | 2024 | seoheejung@snu.ac.kr | 3 |
| 서정범 (Jeongbeom Seo) | 박사과정 | 2024 | jeongbeom1@snu.ac.kr | 5 |
| 김종화 (Jongwha Kim) | 석박사통합과정 | 2024 | jongwha.00@snu.ac.kr | 4 |
| 이준석 (Junseok Lee) | 석박사통합과정 | 2024 | junseok.lee@snu.ac.kr | 4, 5 |
| 이사랑 (Sarang Lee) | 석박사통합과정 | 2024 | sarang2@snu.ac.kr | 3 |
| 이주한 (Joohan Lee) | 석박사통합과정 | 2024 | juhanlee@snu.ac.kr |  |
| 송현준 (Hyunjun Song) | 석박사통합과정 | 2024 | hyunjun.song@snu.ac.kr | 6, 7 |
| 곽서현 (Seohyeon Kwak) | 석박사통합과정 | 2024 | seohyeon6977@snu.ac.kr |  |
| 이승재 (Seungjae Lee) | 석박사통합과정 | 2025 | seungjae.lee@snu.ac.kr | 2 |
| 전민호 (Minho Jeon) | 석박사통합과정 | 2025 | minhojeon@snu.ac.kr |  |
| 전호준 (Hojun Jeon) | 석박사통합과정 | 2025 | hojunjeon@snu.ac.kr |  |
| 이건호 (Gunho Lee) | 석박사통합과정 | 2026 | gunholee@snu.ac.kr |  |
| 이후정 (Hoojung Lee) | 석박사통합과정 | 2026 | hoojung@snu.ac.kr |  |
| 이시진 (Sijin Lee) | 석박사통합과정 | 2026 | sijinlee@snu.ac.kr |  |
| 이주상 (Joosang Lee) | 석박사통합과정 | 2026 | joosanglee@snu.ac.kr |  |
| 이서현 (Seohyun Lee) | 석박사통합과정 | 2026 | shlee24@snu.ac.kr |  |
| 남기현 (Gihyun Nam) | 학부 연구생 | 2026 | nick0418@snu.ac.kr |  |
| 황정운 (Jungwoon Hwang) | 학부 연구생 | 2026 | hwang5866@snu.ac.kr |  |

## 졸업생과 이전 구성원

랩 ALUMNI 페이지의 15명이다. 학위 칸은 카드의 학력 줄에 적힌 학위·학교와 그 과정의 끝 연도이고, 카드가 Combined M.S. - Ph.D 또는 Integrated Master's & Ph.D.로 적은 과정은 「석박사통합과정」으로 적었다. 진로 칸은 카드 이름 아래 줄의 표기다. 학위 학교는 카드 표기대로 UNIST 또는 KAIST다. 김민아의 카드는 UNIST 석사(2013 - 2016) 위에 MIT 박사(2017 - 2022)도 적는다. 황찬웅과 박한기의 개인 페이지는 두 사람을 2025년부터 서울대 박사후연구원(Postdoctoral researcher)으로 적어, ALUMNI 카드의 진로와 다르다.[^alumni][^mpages]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 김민아 (Mina Kim) | 석사 (UNIST) (2016) | Apple Inc., USA |
| 윤희인 (Heein Yoon) | 박사 (UNIST, 석박사통합과정) (2019) | UNIST, Ulsan, South Korea, Assistant Professor |
| 이용선 (Yongsun Lee) | 박사 (UNIST, 석박사통합과정) (2020) | Samsung Electronics, Hwaseong, South Korea |
| 최서진 (Seojin Choi) | 박사 (UNIST, 석박사통합과정) (2020) | Qualcomm, San Diego, USA |
| 유세연 (Seyeon Yoo) | 박사 (UNIST, 석박사통합과정) (2020) | Qualcomm, San Diego, USA |
| 임영현 (Younghyun Lim) | 박사 (UNIST, 석박사통합과정) (2020) | Kyung Hee University, Seoul, South Korea, Assistant Professor |
| 성태호 (Taeho Seong) | 박사 (UNIST, 석박사통합과정) (2021) | Qualcomm, San Diego, USA |
| 박선의 (Suneui Park) | 박사 (KAIST) (2023) | Samsung Electronics, Hwaseong, South Korea |
| 이정현 (Jeonghyun Lee) | 박사 (KAIST) (2024) | Samsung Electronics, Hwaseong, South Korea |
| 김주엽 (Juyeop Kim) | 박사 (KAIST) (2023) | Samsung, San Jose, USA |
| 방주은 (Jooeun Bang) | 박사 (KAIST) (2025) | Neuralink, San Jose, USA |
| 조윤서 (Yoonseo Cho) | 박사 (KAIST, 석박사통합과정) (2025) | Samsung Electronics, Hwaseong, South Korea |
| 조용우 (Yongwoo Jo) | 박사 (KAIST) (2025) | Samsung, San Jose, USA |
| 황찬웅 (Changwoong Hwang) | 박사 (KAIST, 석박사통합과정) (2025) | Samsung Electronics, Hwaseong, South Korea |
| 박한기 (Hangi Park) | 박사 (KAIST, 석박사통합과정) (2025) | Samsung, San Jose, USA |

## 최근 논문 목록 (2021–2026)

랩 PUBLICATIONS 페이지 2021–2026년 연도 구역의 42편(2026년 7, 2025년 9, 2024년 6, 2023년 9, 2022년 6, 2021년 5)이다. 연도는 페이지의 연도 구역이고, 저자·제목·학회와 학술지 이름·연월은 랩 표기 그대로다. 저자 이름 뒤의 =는 랩이 Equally-Credited Authors로 표시한 저자이고, \*는 누리집 표시 \*다. 2026년 구역의 JSTS 논문 1편은 날짜 없이 「Accepted」로만 적혀 있어 「게재 승인」으로 표시했다. 교수는 2019–2023년 KAIST에 있다가 2023년 서울대로 옮겼으므로, 2021–2023년 구역에는 KAIST 재직 시기의 논문이 들어 있다.[^pubs][^prof][^eceprof]

**2026**

- J. Hwang, J. Kim, and J. Choi\*. "A Dual-Mode C²MOS Multi-Modulus Divider for Wide Frequency Operation". *Journal of Semiconductor Technology and Science (JSTS), Accepted (게재 승인)*.
- Y. Shin, J. Kim, J. Lee, Y. Jo, and J. Choi\*. "A Low-Jitter Fractional-N Sampling PLL with Voltage-Domain Quantization-Error Cancellation Using a Nonlinearity-Replication Technique". *IEEE Journal of Solid-State Circuits (JSSC), Sep. 2026*.
- J. Kim, Y. Jo, S. Min, J. Chun, Y. Shin, H. Song, S. Kwak, K. Park\*, and J. Choi\*. "A 16.8–33.6Gb/s, 0.93pJ/b Direct-Frequency-Tracking Digital CDR with an SSC Profile Replicator for Per-Lane Data-Rate Variation and High Jitter Tolerance under Deep SSC". *IEEE Symp. VLSI Circuits Dig., Jun. 2026*.
- J. Lee=, C. Hwang=, J. Seo, and J. Choi\*. "A Versatile On-Chip Jitter Measurement Circuit with Dynamic Quantizer-Resolution Adaptation for Arbitrary Clocks across 1–8GHz and 20–130pspp Jitter". *IEEE Symp. VLSI Circuits Dig., Jun. 2026*.
- S. Lee=, S. Jung=, S. Kwak, S. Lee, H. Lee, and J. Choi\*. "An 85.5-to-94.5-GHz W-Band Fully-Symmetric Quadrature LO Generator with a Fast Quadrature Calibration Technique, Achieving Closely Matched 61-fs RMS Jitter and 41-dB IRR". *IEEE RFIC Symposium, Jun. 2026*.
- M. Han=, J. Kim=, H. Song, and J. Choi\*. "A Comprehensive Power-Supply-Induced Jitter Mitigation Scheme for HBM Interfaces Using a Strobe-Triggered Digital LDO and Local Replica Regulators Achieving 10.7mV Voltage Droop and 1.4ns Settling Time". *IEEE Custom Integrated Circuits Conference (CICC), Apr. 2026*.
- J. Kim=, M. Han=, H. Song, J. Bang, Y. Lim\*, and J. Choi\*. "A Command-Aware Hybrid LDO with Ultra-Small Voltage Droop and Fast Settling Time for Power-Supply-Induced Jitter Mitigation in HBM Interfaces". *IEEE Journal of Solid-State Circuits (JSSC), Jan. 2026*.

**2025**

- M. Chae=, S. Jang=, S. Lee, and J. Choi\*. "A Low-Jitter Fractional-N Digital PLL Using a Quantization-Error-Compensating BBPD and an Orthogonal-Polynomial-based LMS Calibration". *IEEE Journal of Solid-State Circuits (JSSC), Dec. 2025*.
- S. Kim=, J. Lee=, Y. Cho, J. Kim, J. Choi\*, and H. Yoon\*. "A 6.2b-ENOB 2.5GS/s Flash-and-VCO Based Subranging ADC Using a Residue Shifting Technique". *IEEE Solid-State Circuits Letters (SSC-L), Aug, 2025*.
- J. Kim, J. Bang, S. Jung, M. Han, and J. Choi\*. "A Low-Reference-Spur and Low-Jitter D-Band PLL with Complementary Power-Gating Injection-Locked Frequency-Multiplier-Based Phase Detector". *IEEE Solid-State Circuits Letters (SSC-L), Aug. 2025, invited from IEEE Asian Solid-State Circuits Conference (ASSCC)*.
- S. Jung, J. Kim, J. Bang, S. Lee, H. Yoon\*, and J. Choi\*. "A Low-Jitter and Wide-Frequency-Range D-Band Frequency Synthesizer with a Subsampling PLL and a Harmonic Boosting Frequency Multiplier". *IEEE Journal of Solid-State Circuits (JSSC), May 2025*.
- J. Kim=, M. Han=, J. Bang, Y. Lim, and J. Choi\*. "A Command-Aware Hybrid LDO for Advanced HBM Interfaces with 150μA-Quiescent Current and 20pF-On-Chip Capacitor, Achieving Sub-10mV-Voltage Droop in 400ps-Settling Time". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- J. Seo=, Y. Cho=, Y. Shin, and J. Choi\*. "An 850μW, 2-to-5GHz Jitter-Filtering and Instant-Toggling Injection-Locked Quadrature-Clock Generator for Low-Power Clock Distribution in HBM Interfaces". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- M. Chae=, S. Jang=, C. Hwang, H. Park, and J. Choi\*. "A 65fsrms-Jitter and −272dB-FoMjitter,N 10.1GHz Fractional-N Digital PLL with a Quantization-Error-Compensating BBPD and an Orthogonal-Polynomial LMS Calibration". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2025*.
- Y. Shin, Y. Jo, J. Kim, J. Lee, J. Kim, and J. Choi\*. "A Digital-PLL-Based Quadrature Clock Generator for a Low-Power and Jitter-Filtering-Capable Clock Distribution Scheme in High-Speed DRAM Interfaces". *IEEE Journal of Solid-State Circuits (JSSC), Feb. 2025*.
- Y. Cho=, J. Lee=, S. Park, S. Yoo, and J. Choi\*. "A 12.24-GHz MDLL with a 102-Multiplication Factor Using a Power-Gating-Based Ring-Oscillator". *IEEE Journal of Solid-State Circuits (JSSC), Feb. 2025*.

**2024**

- S. Jang=, M. Chae=, H. Park, C. Hwang, and J. Choi\*. "A Low-Jitter and Compact-Area Fractional-N Digital PLL with Fast Multi-Variable Calibration Using the Recursive Least Squares Algorithm". *IEEE Journal of Solid-State Circuits (JSSC), Dec. 2024*.
- J. Kim=, J. Bang=, S. Jung, M. Han and J. Choi\*. "A –51dBc-Reference-Spur and 66fsrms-Jitter D-Band PLL with Complementary Power-Gating Injection-Locked Frequency-Multiplier-Based Phase Detector". *IEEE Asian Solid-State Circuits Conference (ASSCC), Nov. 2024*.
- S. Jung, J. Kim, J. Bang, and J. Choi\*. "A 45-fsrms-Jitter, 144-to-162-GHz D-Band Frequency Synthesizer Using a Subsampling PLL and a Harmonic-Boosting Frequency Multiplier". *IEEE RFIC Symposium, June 2024*.
- S. Jang=, M. Chae=, H. Park=, C. Hwang, and J. Choi\*. "A 5.5μs-Calibration-Time, Low-Jitter and Compact-Area Fractional-N Digital PLL Using the Recursive Least Squares (RLS) Algorithm". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2024*.
- Y. Shin=, J. Lee=, J. Kim=, Y. Jo, and J. Choi\*. "A 76fsrms-Jitter and −65dBc-Fractional-Spur Fractional-N Sampling PLL Using a Nonlinearity-Replication Technique". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2024*.
- J. Kim, Y. Jo, T. Seong, H. Park, Y. Lim\*, and J. Choi\*. "A 12.8–15.0-GHz Low-Jitter Fractional-N Subsampling PLL Using a Voltage-Domain Quantization-Error Cancellation". *IEEE Journal of Solid-State Circuits (JSSC), Feb. 2024*.

**2023**

- Y. Jo, J. Kim, Y. Shin, H. Park, C. Hwang, Y. Lim, and J. Choi\*. "A Wideband LO Generator for 5G FR1 Bands Using a Single LC-VCO-Based Subsampling PLL and a Ring-VCO-Based Fractional-Resolution Frequency Multiplier". *IEEE Journal of Solid-State Circuits (JSSC), Dec. 2023*.
- J. Bang, S. Jung, J. Kim, S. Park, and J. Choi\*. "A Sub-50-fs RMS jitter, 103.5-GHz Fundamental-Sampling PLL with an Extended Loop Bandwidth". *IEEE Solid-State Circuits Letters (SSC-L), Aug. 2023*.
- Y. Cho=, J. Lee=, S. Park, S. Yoo, and J. Choi. "A 122fsrms-Jitter and -60dBc-Reference-Spur 12.24GHz MDLL with a 102-Multiplication Factor Using a Power-Gating Technique". *IEEE Symp. VLSI Circuits Dig., Jun. 2023*.
- J. Lee=, Y. Cho=, J. Kim\*, and J. Choi\*. "A 0.009mm2, 6.5mW, 6.2b-ENOB 2.5GS/s Flash-and-VCO-Based Subranging ADC Using a Resistor-Ladder-Based Residue Shifter". *IEEE Custom Integrated Circuits Conference (CICC), Apr. 2023*.
- B. Moon, S. Lee\*, and J. Choi\*. "A 264−287GHz, −2.5dBm Output Power, and −92dBc/Hz 1MHz-Phase Noise CMOS Signal Source Adopting a 75fsrms Jitter D-Band Cascaded Sub-Sampling PLL". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2023*.
- Y. Shin=, Y. Jo=, J. Kim, J. Lee, J. Kim, and J. Choi\*. "A 900μW, 1–4GHz Input-Jitter-Filtering Digital-PLL-Based 25%-Duty-Cycle Quadrature-Clock Generator for Ultra-Low-Power Clock Distribution in High-Speed DRAM Interfaces". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2023*.
- Y. Jo=, J. Kim=, Y. Shin, C. Hwang, H. Park, and J. Choi\*. "A 135fsrms-Jitter 0.6−7.7GHz LO Generator Using a Single LC-VCO-Based Subsampling PLL and a Ring-Oscillator-Based Sub-Integer-N Frequency Multiplier". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2023*.
- J. Bang, J. Kim, S. Jung, S. Park, and J. Choi\*. "A 47fsrms-Jitter and 26.6mW 103.5GHz PLL with Power-Gating Injection-Locked Frequency Multiplier-Based Phase Detector and Extended Loop Bandwidth". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2023*.
- S. Park, S. Yoo, Y. Shin, J. Lee, and J. Choi\*. "A Sub-100 fs-Jitter 8.16-GHz Ring-Oscillator-Based Power-Gating Injection-Locked Clock Multiplier With the Multiplication Factor of 68". *IEEE Journal of Solid-State Circuits (JSSC), Jan. 2023*.

**2022**

- H. Park=, C. Hwang=, T. Seong, J. Choi\*. "A Low-Jitter Ring-DCO-Based Fractional-N Digital PLL with a 1/8 DTC-Range-Reduction Technique Using a Quadruple-Timing-Margin Phase Selector". *IEEE Journal of Solid-State Circuits (JSSC), Dec. 2022*.
- C. Hwang=, H. Park=, Y. Lee, T. Seong, J. Choi\*. "A Low-Jitter and Low-Fractional Spur Ring-DCO-Based Fractional-N Digital PLL Using a DTC’s Second/Third-Order Nonlinearity Cancellation and a Probability-Density-Shaping ΔΣM". *IEEE Journal of Solid-State Circuits (JSSC), Sep. 2022*.
- S. Park=, S. Choi=, S. Yoo\*, Y. Cho, and J. Choi\*. "An Ultra-Low Jitter, Low-Power, 102-GHz PLL Using a Power-Gating Injection-Locked Frequency Multiplier-Based Phase Detector". *IEEE Journal of Solid-State Circuits (JSSC), Sep. 2022*.
- S. Park=, S. Yoo=, Y. Shin, J. Lee, J. Choi\*. "A 97fsrms-Jitter and 68-Multiplication Factor, 8.16GHz Ring-Oscillator Injection-Locked ClockMultiplier with Power-Gating Injection-Locking and Background Multi-Functional Digital Calibrator". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2022*.
- C. Hwang=, H. Park=, T. Seong, J. Choi\*. "A 188fsrms-Jitter and –243dB-FoMjitter 5.2GHz-Ring-DCO-Based Fractional-N Digital PLL with a 1/8 DTC-Range Reduction Technique Using a Quadruple-Timing-Margin Phase Selector". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2022*.
- Y. Lim, J. Kim, Y. Jo, J. Bang, and J. Choi\*. "A Wide-Lock-In-Range and Low-Jitter 12–14.5 GHz SSPLL Using a Low-Power Frequency-Disturbance-Detecting and Correcting Loop". *IEEE Journal of Solid-State Circuits (JSSC), Feb. 2022*.

**2021**

- J. Bang, S. Choi, S. Yoo, J. Lee, J. Kim, and J. Choi\*. "A 0.0084-mV-FOM, Fast-Transient and Low-Power External-Clock-Less Digital LDO Using a Gear-Shifting Comparator for the Wide-Range Adaptive Sampling Frequency". *IEEE European Solid-State Circuits Conference (ESSCIRC), Sep. 2021*.
- H. Park=, C. Hwang=, T. Seong=, Y. Lee, J. Choi\*. "A 365fsRMS Jitter and −63dBc-Fractional Spur, 5.3GHz-Ring-DCO-Based Fractional-N DPLL Using a DTC’s Second/Third-Order Nonlinearity Cancellation and a Probability-Density-Shaping ΔΣM". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2021*.
- S. Yoo=, S. Park=, S. Choi=, Y. Cho, H. Yoon, C. Hwang, J. Choi\*. "An 82fsRMS-Jitter and 22.5mW-Power, 102GHz W-Band PLL Using a Power-Gating Injection-Locked Frequency Multiplier-Based Phase Detector in 65nm CMOS". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2021*.
- J. Kim=, Y. Jo=, Y. Lim=, T. Seong, H. Park, S. Yoo, Y. Lee, S. Choi, J. Choi\*. "A 104fsRMS-Jitter and −61dBc-Fractional Spur 15GHz Fractional-N Subsampling PLL Using a Voltage-Domain Quantization-Error Cancellation Technique". *IEEE International Solid-State Circuits Conference (ISSCC), Feb. 2021*.
- S. Yoo, S. Choi, Y. Lee, T. Seong, Y. Lim and J. Choi\*. "A Low-Jitter and Low-Reference-Spur Ring-VCO-Based Injection-Locked Clock Multiplier Using a Triple-Point Background Calibrator". *IEEE Journal of Solid-State Circuits (JSSC), Jan. 2021*.

## 특허

구성원·졸업생 개인 페이지의 Patents 칸에 적힌 특허 가운데 페이지에 적힌 날짜(출원일 또는 등록일)가 2021-10-22–2026-10-22인 6건이다. 제목·번호·발명자와 괄호 안 구분(Domestic·U.S., Filed·Granted)은 페이지 표기 그대로다. 2022-12-28 출원 1건은 교수가 KAIST에 있던 시기의 출원이다.[^mpages][^prof]

- 2026-08-13 · TRANSMITTER AND RECEIVER USING PSEUDO-DIFFERENTIAL PHASE-DIFFERENCE MODULATION, AND MEMORY SYSTEM INCLUDING THE SAME (번호 10-2026-0152266; 국가 Domestic; 상태 Filed; 발명자 J. Choi, S. Bae, Y. Shin, H. Park, J. Lee, K. Kim and Y. Lee)
- 2026-02-09 · Clock data recovery circuit used in multi-lane high-speed communication devices (번호 10-2026-0025346; 국가 Domestic; 상태 Filed; 발명자 J. Choi, J. Kim and Y. Shin)
- 2025-12-30 · INTEGRATED CIRCUIT DEVICES HAVING ENHANCED CLOCK GENERATORS THEREIN (번호 12,510,921; 국가 U.S.; 상태 Granted; 발명자 J. Choi, Y. Shin, Y. Jo and J. Kim)
- 2025-06-25 · Apparatus and methods for offsetting nonlinearity in fractional-N phase-locked loop circuits (번호 10-2025-0083987; 국가 Domestic; 상태 Filed; 발명자 J. Choi, Y. Shin, J. Lee, J. Kim and Y. Jo)
- 2023-09-07 · LO Generator for Wideband Frequency Band Cover for 5G Communication and its Operation Method (번호 10-2023-0119112; 국가 Domestic; 상태 Filed; 발명자 J. Choi, Y. Jo, J. Kim and Y. Shin)
- 2022-12-28 · Clock generator and semiconductor device including the same (번호 10-2022-0186648; 국가 Domestic; 상태 Filed; 발명자 J. Choi, Y. Shin, Y. Jo and J. Kim)

## 수상

랩 AWARDS & HONORS 페이지의 항목 가운데 수상 날짜가 2021-10-22–2026-10-22인 34건이다. 날짜는 수상자 개인 페이지가 적은 연월(일)이고, 개인 페이지에 없으면 NEWS 페이지의 연월, 둘 다 없으면 AWARDS & HONORS 페이지의 연도 구역이다. 대괄호 안 대회·행사 이름과 상 이름, 수상자 표기는 AWARDS & HONORS 페이지 그대로이고, Honorable Mention Award에는 「(입선)」을 붙였다. 목록에는 교수의 KAIST 재직 시기(2019–2023)의 수상이 들어 있다(KAIST-Samsung Electronics Cooperation Center 상 등).[^awards][^mpages][^news]

- 2026-02 · [2026 IEEE International Solid-State Circuits Conference] ISSCC 2025 Takuo Sugano Award - 서정범, 조윤서, 신유환
- 2026-02 · [IEEE SSCS Predoctoral Achievement Award] - 신유환
- 2026-02 · [32nd Samsung Humantech Paper Award] Honorable Mention Award(입선) (Dept. circuit design) - 이준석, 서정범
- 2026-01 · [2026 KCS Chip Design Contest] Best Design Award - 서정범
- 2025-11 · [2025 SNU-Samsung DS Cooperation Center Outstanding Paper Award] Honorable Mention Award(입선) - 서정범
- 2025-10 · [26th Korea Semiconductor Design Competition] Presidential Award - 서정범, 신유환, 이준석, 이주한
- 2025-10 · [26th Korea Semiconductor Design Competition] Corporate Special Award - 채문재, 장세헌, 이승재, 이사랑
- 2025-10 · [26th Korea Semiconductor Design Competition] Corporate Special Award - 김재호, 한명호, 송현준, 곽서현
- 2025-02 · [31st Samsung Humantech Paper Award] Gold Award (Dept. circuit design) - 김재호, 한명호, 방주은
- 2025-02 · [31st Samsung Humantech Paper Award] Silver Award (Dept. circuit design) - 채문재, 장세헌, 황찬웅, 박한기
- 2025 · [2025 AI Semiconductor Insight Day] Minister of Science and ICT Award - 한명호
- 2025 · [2025 IDEC Congress Chip Design Contest] Best Poster Award - 정서희, 김재호, 방주은
- 2025 · [2025 KCS Chip Design Contest] SSCS Seoul Chapter Special Award - 방주은
- 2024-11 · [16th Electronic Times ICT Paper Contest] 대한전자공학회 학회장상 - 김재호, 한명호, 방주은
- 2024-11 · [25th Korea Semiconductor Design Competition] Minister Award - 장세헌, 채문재, 박한기, 황찬웅
- 2024-10 · [25th Korea Semiconductor Design Competition] Corporate Special Award - 신유환, 조용우, 이준석
- 2024-08 · [2024 SNU-Samsung DS Cooperation Center Outstanding Paper Award] Honorable Mention Award(입선) - 장세헌
- 2024-02 · [30th Samsung Humantech Paper Award] Silver Award (Dept. circuit design) - 신유환, 이준석, 조용우
- 2024-02 · [30th Samsung Humantech Paper Award] Bronze Award (Dept. circuit design) - 장세헌, 채문재, 박한기, 황찬웅
- 2024-02 · [IEEE SSCS Predoctoral Achievement Award] - 황찬웅
- 2024-02 · [IEEE SSCS Predoctoral Achievement Award] - 방주은
- 2023-11-07 · [24th Korea Semiconductor Design Competition] Minister Award - 조윤서, 장세헌, 정서희
- 2023-11-07 · [24th Korea Semiconductor Design Competition] Minister Award - 신유환, 조용우, 이준석, 김종화
- 2023-10-26 · [2023 IDEC Congress Chip Design Contest] Best Poster Award - 이정현, 조윤서
- 2023-07 · [2023 ISE Summer Annual Conference] Excellent Paper Award - 신유환, 조용우, 김주엽
- 2023-07 · [2023 IDEC Congress Chip Design Contest] Excellent Design Award - 신유환, 조용우, 김주엽
- 2023-06-29 · [2023 IEIE Summer Annual Conference] Best Paper Award - 조윤서, 이정현
- 2023-02 · [IEEE SSCS Predoctoral Achievement Award] - 박선의
- 2023 · [2023 KAIST-Samsung Electronics Cooperation Center] Best Patent Award - 최재혁 교수님
- 2022-10-21 · [2022 ISOCC Chip Design Contest] Best Design Award - 박선의, 신유환, 이정현
- 2022-09 · [2022 KAIST-Samsung Electronics Cooperation Center] Best Paper Award - 박선의
- 2022-02 · [28th Samsung Humantech Paper Award] Silver Award (Dept. circuit design) - 박선의, 신유환, 이정현
- 2022-02 · [IEEE SSCS Predoctoral Achievement Award] - 김주엽
- 2021-10-26 · [22nd Korea Semiconductor Design Competition] Presidential Award - 박선의, 조윤서, 방주은

## 소식

랩 NEWS 페이지 글 가운데 연월이 2021년 11월–2026년 9월인 연구·수상 소식 28건이다. 날짜는 페이지에 적힌 연월이고, 문구는 게시된 그대로이며 여러 줄로 된 글은 줄 사이를 「/」로 이었다. 교수의 KAIST 재직 시기(2019–2023)의 소식이 들어 있다.[^news][^prof]

- 2026-03 · Congratulations! ICSL's papers are accepted for presentation at 2026 IEEE symposium on VLSI circuits held in Honolulu, Hawaii
- 2026-02 · Congratulations! ICSL’s Papers Won Prizes in 32nd Samsung Human-Tech Paper Award
- 2026-02 · Congratulations! ICSL's paper is accepted for presentation at the Symposium on RFIC 2026 held in Boston
- 2026-02 · Congratulations! ICSL's paper won 2025 Takuo Sugano Award at 2026 IEEE International Solid-State Circuits (ISSCC) held in San Francisco, CA
- 2026-01 · Congratulations! ICSL's paper has been accepted for presentation at 2026 IEEE Custom Integrated Circuit Conference (CICC) held in Seattle, Washington
- 2025-10 · Three ICSL's papers won prizes in 26th Korea Semiconductor Design Competition / Presidential Award - Jeongbeom Seo, Yuhwan Shin, Junseok Lee, Joohan Lee / Corporate Special Award - Munjae Chae, Seheon Jang, Seungjae Lee, Sarang Lee / Corporate Special Award - Jaeho Kim, Myeongho Han, Hyunjun Song, Seohyeon Kwak
- 2025-02 · Congratulations! Two ICSL’s Papers Won Prizes in 31st Samsung Human-Tech Paper Award
- 2024-12 · [16th Electronic Times ICT Paper Contest] / 우수상-대한전자공학회 학회장상 / Jaeho Kim, Myeongho Han, Jooeun Bang
- 2024-10 · Two ICSL's papers won prizes in 25th Korea Semiconductor Design Competition / Minister Award - Seheon Jang, Munjae Chae, Hangi Park, Chanwoong Hwang / Corporate Special Award - Yuhwan Shin, Yongwoo Jo, Junseok Lee
- 2024-10 · Congratulations! Three ICSL's papers have been accepted for presentation at 2025 IEEE ISSCC held in San Francisco
- 2024-08 · Congratulations! ICSL's paper is accepted for presentation at the Asian Solid-State Circuits Conference 2024 held in Hiroshima
- 2024-02 · Congratulations! ICSL's paper is accepted for presentation at the Symposium on RFIC 2024 held in Washington, DC
- 2024-02 · Chanwoong Hwang and Jooeun Bang were honored at ISSCC as a winner of "2024 IEEE Predoctoral Achievement Award"
- 2024-02 · Congratulations! Two ICSL’s Papers Won Prizes in 30th Samsung Human-Tech Paper Award
- 2023-11 · [24th Korea Semiconductor Design Competition] / ICSL's papers won 2 Minister Awards / Minister Award - YoonSeo Cho, Seheon Jang, Seohee Jung / Minister Award - Yuhwan Shin, Yongwoo Jo, Junseok Lee, Jongwha Kim
- 2023-10 · Congratulations! Two ICSL's papers have been accepted for presentation at 2024 IEEE ISSCC held in San Francisco
- 2023-07 · [ISE Summer Annual Conference] / Excellent Paper Award - Yuhwan Shin, Yongwoo Jo, Juyeop Kim
- 2023-07 · [IDEC Congress Chip Design Contest] / Excellent Design Award - Yuhwan Shin, Yongwoo Jo, Juyeop Kim
- 2023-06 · [IEIE Summer Annual Conference] / Best Paper Award(1st place) - Yoonseo Cho, Jeonghyun Lee
- 2023-03 · Congratulations! ICSL's paper is accepted for presentation at the Symposium on VLSI Circuits 2023 held in Kyoto
- 2023-02 · Suneui Park was honored at ISSCC as a winner of “2023 IEEE Predoctoral Achievement Award”
- 2023-01 · Congratulations! ICSL's paper has been accepted for presentation at 2023 IEEE Custom Integrated Circuit Conference (CICC) held in San Antonio, Texas
- 2022-11 · Congratulations! Prof. Choi is selected as an Associate Editor of IEEE Journal of Solid-State Circuits (JSSC)
- 2022-10 · Congratulations! Three ICSL's papers have been accepted for presentation at 2023 IEEE ISSCC held in San Francisco
- 2022-09 · [KAIST-Samsung Electronics Cooperation Center] Best Paper Award - 박선의
- 2022-02 · Juyeop Kim was honored at ISSCC as a winner of “2022 IEEE Predoctoral Achievement Award”
- 2022-02 · Congratulations! ICSL’s Papers Won Prizes in 28th Samsung Human-Tech Paper Award
- 2021-11 · [22nd Korea Semiconductor Design Competition] Presidential Award - SunEui Park, YoonSeo Cho, JooEun Bang

## 연락과 위치

- 연구실: 서울대학교 302동 510-3호(누리집 표기 Bldg. 302, Rm. 510-3, 1, Gwanak-ro, Gwanak-gu, Seoul, 08826, Republic of Korea), 전화 02-880-1763, 02-871-3986(누리집 표기 +82-02-880-1763, +82-02-871-3986)[^home][^ecelabd]
- 교수 연구실: 301동 803호(누리집 표기 Rm. 803, Bldg. 301), 전화 02-880-1762[^prof][^eceprof]
- 교수 이메일: jaehyouk@snu.ac.kr[^prof]
- 학과 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^eceprof]
[^p1]: S. Jang 외, J. Choi, IEEE Journal of Solid-State Circuits 59, 3884-3897 (2024). <https://doi.org/10.1109/jssc.2024.3456105> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: M. Chae, S. Jang, S. Lee, J. Choi, IEEE Journal of Solid-State Circuits 60, 4587-4599 (2025). <https://doi.org/10.1109/jssc.2025.3611417> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Jung 외, J. Choi, IEEE Journal of Solid-State Circuits 60, 1632-1643 (2025). <https://doi.org/10.1109/jssc.2024.3523474> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Shin 외, J. Choi, IEEE Journal of Solid-State Circuits 60, 509-518 (2025). <https://doi.org/10.1109/jssc.2024.3433026> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Lee, C. Hwang, J. Seo, J. Choi, 2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), 1-3 (2026). <https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577405> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: J. Kim 외, J. Choi, IEEE Journal of Solid-State Circuits 61, 116-128 (2026). <https://doi.org/10.1109/jssc.2025.3602459> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. Han, J. Kim, H. Song, J. Choi, 2026 IEEE Custom Integrated Circuits Conference (CICC), 1-4 (2026). <https://doi.org/10.1109/cicc65509.2026.11509607> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://www.icsl.snu.ac.kr/> (RESEARCH 세 주제, CONTACT의 주소·전화, 2026-10-25 열람)
[^prof]: 누리집 PROFESSOR 페이지 <https://www.icsl.snu.ac.kr/professor-cav0> (Biography, Contact info., Education, Professional Experience, Professional Activities and Awards, 2026-10-25 열람)
[^members]: 누리집 MEMBERS 페이지 <https://www.icsl.snu.ac.kr/student> (구성원 카드 23장, 2026-10-25 열람)
[^alumni]: 누리집 ALUMNI 페이지 <https://www.icsl.snu.ac.kr/alumni> (졸업생 카드 15장, 2026-10-25 열람)
[^mpages]: 구성원·졸업생 개인 페이지(MEMBERS·ALUMNI 카드의 More 링크) 38쪽, 예: <https://www.icsl.snu.ac.kr/syh> (Publications, Awards, Patents 칸, 주소 목록은 근거 페이지, 2026-10-25 열람)
[^pubs]: 누리집 PUBLICATIONS 페이지 <https://www.icsl.snu.ac.kr/publications> (2009–2026년 연도 구역과 U.S. Patents, 2026-10-25 열람)
[^awards]: 누리집 AWARDS & HONORS 페이지 <https://www.icsl.snu.ac.kr/awards-honors> (2014–2026년 연도 구역, 2026-10-25 열람)
[^news]: 누리집 NEWS 페이지 <https://www.icsl.snu.ac.kr/news> (연월별 소식 78건, 2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-25 열람)
[^ecelabd]: 서울대학교 전기·정보공학부 연구실 소개(반도체회로 및 시스템 설계 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=133> (연구실 국·영문 이름, 지도교수, 연구, TEL, WEBSITE, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 소개(최재혁) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p894> (직위, TEL, OFFICE, 학위, 전공, 분야, 학력, 주요경력, Research Interest, 학과 주소, 2026-10-25 열람)

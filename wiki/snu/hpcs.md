# 고성능 컴퓨터 시스템 연구실 (High Performance Computer System Lab, HPCS)

**서울대학교 공과대학 전기·정보공학부 · 김장우 교수**

- 분야: 컴퓨터 구조와 시스템 설계, 장치 중심 서버 구조와 FPGA 기반 네트워크·저장장치 가속(DPU, Data Processing Unit), 초저온 CMOS·초전도 SFQ(Single Flux Quantum) 프로세서·결함 허용 양자 컴퓨터 시스템, AI·딥러닝 가속 시스템과 3차원 낸드 플래시 메모리 안 연산, 뇌 시뮬레이션용 뉴로모픽 컴퓨팅과 뇌-컴퓨터 인터페이스 시스템, 컴퓨터 시스템 모델링·시뮬레이션·성능 분석
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 구조·운영체제[^home][^ecelabd][^p3], AI 반도체·가속기[^research][^ai][^p5], 메모리 내 연산[^ai][^p5], 양자 컴퓨팅[^cryo][^p4], 컴퓨터 네트워크[^server][^p1][^p2], 신경 인터페이스·뇌-컴퓨터 인터페이스[^neuro][^p7], AI 시스템·인프라[^research][^ai], 저장 시스템·SSD[^p2]
- 홈페이지: <https://hpcs.snu.ac.kr/> (교수 개인 페이지 <https://hpcs.snu.ac.kr/~jangwoo/>)
- 근거와 출처: [HPCS 연구실 근거 페이지](hpcs-sources.md)

> 차세대 컴퓨터 구조와 시스템을 설계하고 모델링하고 시제품으로 만들어 평가하는 연구실이다. 장치 중심 서버와 FPGA 가속, 초저온·초전도·양자 컴퓨터 시스템, AI·딥러닝 가속 시스템, 뉴로모픽 컴퓨팅과 뇌-컴퓨터 인터페이스 시스템, 컴퓨터 시스템 모델링과 분석을 연구 과제로 둔다.[^home][^ecelabd][^research]

## 무엇을 연구하나

연구실은 서울대학교 공과대학 전기·정보공학부 김장우 교수가 이끄는 고성능 컴퓨터 시스템 연구실(High Performance Computer System Lab, HPCS)이다.[^ecelabd][^eceprof] 누리집 첫 화면은 차세대 컴퓨터 구조(프로세서·메모리 같은 컴퓨터 하드웨어를 어떻게 짜고 잇는지에 관한 설계)와 시스템에 관한 여러 연구 주제를 탐구하는 연구실로 소개하고,[^home] 학과 연구실 소개는 연구 분야를 "컴퓨터 및 VLSI 시스템"으로 적는다.[^ecelabd] 학과 연구실 소개 글에 따르면 연구실 연구원들은 컴퓨터 시스템 설계자로서 차세대 컴퓨터 시스템을 설계하고 모델링하고 시제품으로 만들어 평가하며, 이를 위해 컴퓨터 구조, 시스템 모델링과 시뮬레이션, VLSI(Very Large Scale Integration, 트랜지스터를 대규모로 한 칩에 집적하는 기술) 설계와 시제작, 시스템 소프트웨어, 사용자 응용까지 핵심 분야를 모두 훈련받는다. 이를 바탕으로 빠르고 규모를 키울 수 있는 CPU(Central Processing Unit)와 서버, 뇌 시뮬레이션 시스템, 딥러닝 가속기, 초저전력 슈퍼컴퓨터 같은 차세대 응용용 컴퓨터 시스템을 만든다고 적는다.[^ecelabd] 학과 연구실 목록은 이 연구실을 인공지능 및 머신러닝, 차세대 컴퓨팅, 통신 네트워크, 회로 및 시스템, 빅데이터 및 인공지능 플랫폼의 다섯 연구그룹에 올린다.[^ecelab]

Research 페이지는 연구를 다섯 과제로 나눈다.[^research] 첫째, 장치 중심 서버 구조(Device-Centric Server Architecture)는 데이터 분석, 기계 학습, 가상 머신(한 컴퓨터 안에서 소프트웨어로 만든 독립된 컴퓨터) 같은 새 서버 응용의 필요를 채우는 서버 구조를 설계하고 시제품으로 만든다. 응용의 계산·메모리·저장 요구를 맞추려고 FPGA(Field-Programmable Gate Array, 만든 뒤에도 회로 구성을 바꿔 쓸 수 있는 반도체 칩)로 여러 장치를 조율하고 가속하는 방법을 적극 써서, 전체 시스템 수준에서 서버 한 대의 성능을 키우는(scale-up) 해법과 서버 여러 대로 늘리는(scale-out) 해법을 낸다. 둘째, 초저온·초전도·양자 컴퓨터 시스템 과제는 여러 초저온 컴퓨터 장치와 시스템을 설계해 만든다. 초저온 컴퓨터는 극저온(예: 4K, 77K. K는 절대온도 단위인 켈빈)에서 동작해 배선 지연과 누설 전류(의도하지 않은 경로로 새어 흐르는 전류)를 크게 줄이며, 연구실은 초저온 컴퓨터 모델링 도구를 개발하고 초저온 프로세서·캐시·메모리·서버 설계를 내놓는다. 셋째, AI·딥러닝 가속 시스템 과제는 CNN·RNN·MANN 같은 신경망 응용의 필요를 분석해 이를 효율적으로 가속하는 구조·시스템 해법을 내며, FPGA, ASIC(Application-Specific Integrated Circuit, 특정 용도에 맞춰 설계한 집적회로), GPU, SSD 같은 서로 다른 하드웨어를 함께 써서 규모를 키울 수 있고 유연한 AI 가속 시스템을 만드는 데 관심을 둔다. 넷째, 뉴로모픽 컴퓨팅과 뇌-컴퓨터 인터페이스 시스템 과제는 뇌를 이해하고 뇌와 상호작용하기 위한 두 갈래를 함께 간다. 사람 규모의 신경 회로를 충실히 시뮬레이션하고 스파이크(신경세포가 내는 짧은 전기 신호) 기반 신경망이 어떻게 인지를 가능하게 하는지 밝히는 뉴로모픽 컴퓨팅 시스템을 만들고, 실제 응용에서 뇌와 믿을 만하게 상호작용하는 뇌-컴퓨터 인터페이스(BCI, Brain-Computer Interface) 시스템을 개발한다. 다섯째, 컴퓨터 시스템 모델링과 분석 과제는 성능·전력 소비를 다루는 효율적인 컴퓨터 구조 시뮬레이션 방법과, 내부 동작이 공개되지 않은 상용 프로세서·저장장치·데이터센터를 이해하는 성능 분석 방법을 개발해 공개한다.[^research]

누리집 첫 화면의 Computer Architecture and System 목록은 CPU·서버·데이터센터 구조, 시스템 모델링·시뮬레이션·분석, 클라우드·빅데이터 컴퓨팅 시스템, 뇌에서 착안한 뉴로모픽 컴퓨터 시스템, 가속기 시스템과 프로그래밍 지원을 들고,[^home] 교수 개인 페이지는 지금의 연구 과제를 CPU·서버·데이터센터 구조, 시스템 모델링·시뮬레이션·분석, AI·뉴로모픽 컴퓨터 시스템, 초저온·양자 컴퓨터 시스템, 시스템 소프트웨어 지원을 갖춘 가속 시스템으로 적는다.[^pihome] 교수 개인 페이지는 교수를 MangoBoost Inc의 "CEO and founder"로 소개하고, MangoBoost를 서울대에서 한 「10+ years」의 장치 중심 서버 가속 연구와 여러 AI 시스템 가속 연구를 바탕으로 차세대 서버 기반 시설 가속 장치(DPU 등)를 내놓는 한국·미국 기반 스타트업으로 적는다. DPU(Data Processing Unit)는 서버의 네트워크·저장 같은 데이터 처리 작업을 CPU 대신 맡는 처리 장치다.[^pihome]

대표 논문으로 보면 연구는 다섯 갈래로 모인다. 첫째, FPGA로 TCP(Transmission Control Protocol, 인터넷에서 데이터를 빠짐없이 순서대로 전달하는 통신 규약) 처리 전체를 가속하는 틀과, 네트워크 너머의 저장장치에 접근하는 NVMe/TCP(저장장치 접속 규약 NVMe를 TCP 통신 위에서 쓰는 방식) 처리를 하드웨어로 옮긴 DPU다(대표 논문 1, 2).[^p1][^p2] 둘째, 초전도 소자로 만드는 매우 빠른 프로세서와, 결함 허용(일부 부품에 오류가 생겨도 올바른 계산 결과를 내도록 설계한) 양자 컴퓨터가 실행 중에 큐비트(qubit, 양자 정보의 기본 단위)의 오류율이 높아져도 양자 상태를 잃지 않고 보정하며 오래 돌게 하는 방법이다(대표 논문 3, 4).[^p3][^p4] 셋째, 3차원 낸드 플래시 메모리 안에서 신경망 계산을 하는 딥러닝 가속 시스템이다(대표 논문 5).[^p5] 넷째, 추측 실행으로 뇌 시뮬레이션을 빠르게 하는 하드웨어 가속기와, 뇌에 심는 BCI 시스템에서 계속 학습할 때의 메모리 쓰기를 줄이는 시스템이다(대표 논문 6, 7).[^p6][^p7] 다섯째, 대표적인 작업 배치 시나리오를 뽑아 데이터센터 성능을 빠르게 평가하는 방법이다(대표 논문 8).[^p8]

## 주요 연구 주제

### 1. 장치 중심 서버 구조와 FPGA 가속

요즘 고성능 서버는 NVMe SSD, 100GbE(초당 100기가비트 이더넷) 네트워크 카드, GPU, AI 가속기 같은 빠른 장치를 한 서버에 많이 꽂아 성능을 얻지만, 이 많은 장치를 동시에 조율하려면 호스트 CPU의 대역폭 부담과 장치 제어 지연이 커진다. 연구실의 DCS 구조는 FPGA 기반 장치 조율 장치 DCS-Engine을 두어 호스트 CPU와 운영체제 대신 장치 사이의 데이터·제어 경로를 하드웨어 수준에서 관리하고, DCS-Engine에 장치 가까이에서 계산하는 처리 장치(NDP, near-device processing)를 더해 성능과 확장성을 높인다.[^server] 같은 생각을 저장 서버(CIDR, FIDR), AI 학습 서버(TrainBox), 가상 머신 에뮬레이션(FVM)으로 넓혔고, 네트워크 가속 연구 F4T는 상태가 있는 TCP 처리를 멈춤 없이 연달아 처리하고 여러 메모리 모듈에 걸친 TCP 상태를 효율적으로 관리하며, 응용을 고치지 않고 쓸 수 있는 소프트웨어·하드웨어 전체 스택을 갖췄다. 지금은 장치 사이와 서버 사이를 잇는 새 연결 방식을 활용해 서버 해법의 규모 확장 능력을 높이는 연구를 한다고 적는다.[^server] 최근 논문 목록에는 NVMe/TCP 저장장치 가속(BoostX-NTI), 새 연결 방식을 위한 스위칭 시스템(FS2), FPGA로 가속하는 DPU 해법(MangoBoost Alice), AI용 네트워크 장치(BoostX-RNIC, MICRO 2026 채택)가 있다.[^pubs] 대표 논문 1, 2.

### 2. 초저온·초전도·양자 컴퓨터 시스템

고성능 컴퓨팅과 데이터센터 산업은 늘 가장 빠르고 전력 효율이 높은 컴퓨터를 원하지만, 단일 스레드·다중 스레드 성능 향상이 끝나 가면서 상온 컴퓨팅으로는 성능과 전력 효율을 더 높이기 어려워졌다. 그래서 연구실은 아주 낮은 온도에서 컴퓨터를 설계하고 운용하는 초저온·초전도·양자 컴퓨팅에 집중하며, 기존 컴퓨터의 성능을 최대로 끌어올리고(초저온·초전도 컴퓨팅) 고성능 초전도 컴퓨터와 규모를 키울 수 있는 양자 컴퓨터 같은 차세대 컴퓨터를 실현하는 것을 목표로 둔다. 주요 성과는 77K CMOS 기반 초저온 컴퓨팅, 4K 초전도체 기반 컴퓨팅, mK(밀리켈빈) 결함 허용 양자 컴퓨팅의 셋으로 요약한다.[^cryo] 77K(섭씨 영하 196도)는 액체 질소로 싸게 만들 수 있고 CMOS(Complementary Metal-Oxide-Semiconductor, n형·p형 트랜지스터를 짝지어 만드는 반도체 회로 방식) 소자가 이 온도에서도 믿을 만하게 동작하므로, 77K에서 도는 메모리·캐시·프로세서의 성능·전력 시뮬레이션 방법을 직접 만들고 CryoRAM, CryoGuard, CryoCache, CryoCore, CryoWire 같은 온도 최적화 설계를 내놓았으며, 검증한 성능 모델링 틀 CryoModel을 공개했다.[^cryo] 4K(섭씨 영하 269도)보다 낮은 온도에서는 초전도 소자를 써야 하는데 그 구조 설계 원칙이 아직 많이 탐구되지 않았기에, 4K 아래용 컴퓨터 구조 모델링 도구를 만들고 규슈대·나고야대와 함께 초전도 소자로 분야별 가속기(SuperNPU)와 범용 프로세서(SuperCore)를 설계했으며, 되먹임 고리에서 동작 주파수를 제한하는 요인을 찾아 클록 방식·회로·구조를 함께 설계하는 방법으로 풀었다.[^cryo] 실용적인 양자 컴퓨팅에는 큐비트 100만 개 규모의 결함 허용 양자 컴퓨터가 필요하지만 제어 시스템의 확장성 병목을 찾을 믿을 만한 도구가 없었다. 연구실은 공개 양자 제어 시스템 시뮬레이터 XQsim과 QIsim을 만들어 큐비트 1만 개 규모의 제어 시스템을 제안했고, 이 모델링 도구로 100만 큐비트까지 늘리는 분산 결함 허용 양자 컴퓨터 구조를 제안했다. 나아가 큐비트 오류율을 낮게 유지하는 정확하고 비파괴적인 보정 방법(LANCER)과, 양자 LDPC 부호(오류 정정 부호의 한 종류)를 써서 실용 응용에 필요한 자원을 줄이는 컴파일러·구조 공동 설계로 넓히고 있다.[^cryo] 대표 논문 3, 4.

### 3. AI·딥러닝 가속 시스템

연구실은 최신 자연어 처리·추천 응용을 분석해 한 AI 응용을 여러 작은 작업으로 나누고 서로 다른 하드웨어에 최적화해 나눠 맡기는 단일 AI 가속, 여러 사용자의 서로 다른 AI 응용을 함께 배치하기 좋은 작은 작업으로 나눠 동적으로 일정을 짜서 가속기 한 대의 활용도를 최대로 유지하는 다중 AI 가속, CPU·GPU·ASIC·FPGA로 이뤄진 여러 장치에서 AI 추론과 학습을 병렬화하는 다중 장치 AI 처리를 연구한다.[^ai] 지금은 서로 매우 다른 응용을 돌리면서 대상 응용에 맞게 구조를 동적으로 바꾸는 유연한 AI 가속 시스템을 설계하고 있다고 적는다. 또 AI 서비스의 계산은 메모리에서 오는 에너지 소비가 크다는 문제를 다루려고, 계산을 메모리 배열에 맡기는 메모리 안 연산(PIM, Processing-In-Memory)을 3차원 낸드 플래시로 구현하는 구조와 전용 재학습 틀, 컴파일러를 설계했다.[^ai] NLP-Fast와 3D-FPIM을 공개 소프트웨어로 내놓았다.[^ai] 대표 논문 5.

### 4. 뉴로모픽 컴퓨팅과 뇌-컴퓨터 인터페이스 시스템

사람 규모의 뇌는 시냅스로 이어진 수십억 개의 서로 다른 뉴런으로 이뤄지고 복잡한 스파이크 전달로 소통하므로, 기존 컴퓨터로는 뇌를 충실히 시뮬레이션하기에 너무 느리거나 비싸고 맞춤 설계한 뇌 시뮬레이션 시스템은 다룰 수 있는 모델이 좁다.[^neuro] 연구실은 서로 다른 생물 뉴런 모델과 학습 규칙을 동적으로 구성하는 ASIC 기반 구조 Flexon과 FlexLearn을 내놓았고, 이를 담은 전체 스택 뇌 시뮬레이션 시스템 FlexBrain을 개발하고 있으며, 사건이 생길 때만 계산하는 사건 구동 시뮬레이션 방식을 단일 코어 구조에 들인 NeuroEngine도 설계했다.[^neuro] 뇌의 스파이킹 신경망(SNN, 스파이크로 정보를 주고받는 인공 신경망) 방식을 AI 가속기의 전력 효율을 높이는 데 쓰려는 SNN 기반 AI·딥러닝 실행 방식과 가속 시스템도 연구한다.[^neuro] BCI 시스템은 신경 신호를 받아 처리해 뇌와 바깥 장치를 직접 잇는데, 전극이 늘고 과제가 복잡해지면서 유연하고 에너지 효율적인 신호 처리와 시간에 따라 바뀌는 신경 신호 패턴에 대한 적응이 필요해졌다. 연구실은 스파이크 기반 BCI 작업용 사건 구동 뉴로모픽 프로세서 NeuroLobe와, 신경 신호의 비정상성에 대응하는 연속 학습을 지원하며 비휘발성 메모리 쓰기를 줄여 장치 수명을 늘리는 InfiniMind를 내놓았고, 여러 계산 계층에 처리를 나누는 다계층 BCI 시스템 설계를 위한 시뮬레이션 틀 TierX를 공개했다.[^neuro] 최근 논문 목록에는 안전하게 심을 수 있는 BCI를 위한 배터리 없는 처리 시스템(SafeMind, MICRO 2026 채택)도 있다.[^pubs] 대표 논문 6, 7.

### 5. 컴퓨터 시스템 모델링과 분석

컴퓨터 구조 연구·개발의 큰 과제는 시스템의 성능과 에너지 효율을 분석해 병목을 찾고 이를 풀 가장 좋은 구조 설계를 빨리 찾는 것이므로, 연구실은 빠르고 정확한 시스템 모델링·분석 도구를 개발해 내놓는다.[^model] CPU 쪽에서는 해석적 모델링, 지정 성능 시험, 기계 학습, 시뮬레이터 병렬화를 엮은 방법을 만들었고, 상용 프로세서의 세부 타이밍 동작을 특정 동작 하나를 재도록 만든 시험 프로그램(마이크로벤치마크)으로 뽑아내는 DiagSim과 해석적 모델링과 시뮬레이터 병렬화를 결합해 프로세서 설계 공간 탐색을 빠르게 하는 RpStacks가 그 예다. 내부 동작이 공개되지 않고 제조사마다 다른 SSD 같은 주변 장치의 내부 구조와 타이밍을 뽑아내는 도구 SSDcheck는 앞으로 올 접근의 지연 시간을 예측해 입출력 일정 관리기의 효율을 높인다.[^model] 데이터센터 쪽에서는 전체 데이터센터를 정확히 대표하는 소수의 서버와 작업 부하를 뽑아 성능을 모델링하는 WSMeter를 만들었고, 누리집은 WSMeter가 Google에서 검증·적용되었다고 적는다.[^model] UC-Check, RpStacks, SSDcheck를 공개했다.[^model] 대표 논문 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 출판된 학회·학술지 논문을 연구 갈래마다 고르게 골랐다. 여덟 편 모두 김장우 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회·학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [F4T: A Fast and Flexible FPGA-based Full-stack TCP Acceleration Framework](https://doi.org/10.1145/3579371.3589090) · ISCA 2023 | 여러 서버에서 도는 복잡한 작업 부하가 더 높은 네트워크 처리량을 요구하면서 TCP 스택(TCP 통신을 처리하는 소프트웨어 계층)을 돌리는 데 드는 CPU 계산이 늘어났다. 계산이 많은 TCP 처리의 CPU 부담을 덜려고 앞선 연구들은 TCP 처리를 네트워크 장치 안의 내장 프로세서, ASIC, FPGA로 넘겼지만, 높은 성능·많은 연결·높은 유연성이라는 TCP의 핵심 요구를 한꺼번에 채운 방법은 없었다. 내장 프로세서는 TCP 스택을 모두 넘겨받기에 성능이 모자라고, ASIC은 유연성이 모자라며, 기존 FPGA 기반 TCP 가속기는 처리 구조가 비효율적이어서 높은 성능을 내지 못하거나 높은 성능을 위해 핵심 기능과 요구 일부를 포기했다. 이 논문은 높은 성능, 많은 연결 지원, 높은 유연성을 함께 갖춰 CPU 계산을 아끼는 FPGA 기반 전체 스택 TCP 가속 틀 F4T를 제안했다. 기존 FPGA 기반 TCP 가속기를 분석해, 핵심 병목이 상태를 다루는 연산을 비효율적으로 처리해 생기는 멈춤과 여러 메모리 모듈을 쓰는 데 필요한 TCP 상태 관리의 부재라는 두 요인에서 온다는 것을 밝혔고, 상태를 다루는 연산을 멈춤 없이 연달아 처리하며 여러 메모리 모듈에 걸쳐 TCP 상태를 효율적으로 관리하도록 F4T를 설계했다. 응용을 전혀 고치지 않고 F4T를 쓸 수 있도록 소프트웨어·하드웨어 전체 스택도 제공했다. 평가에서 F4T는 CPU 코어 두 개만으로 100Gbps 연결 대역폭을 가득 채우면서 많은 연결과 높은 유연성을 지원했고, Nginx 웹 서버를 돌릴 때 리눅스 TCP 스택과 비교해 CPU 계산을 64% 아끼고 응용에 2.8배의 CPU 계산을 내주었다.[^p1] | 1저자 Junehyuk Boo, 마지막 저자 김장우 |
| 2 | 2026 | [BoostX™-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration](https://doi.org/10.1109/isca66397.2026.00081) · ISCA 2026 | 데이터센터에서 계산 자원과 저장 자원을 떼어 놓는 저장장치 분리(storage disaggregation)가 중요한 흐름이 되었고, 전송 방식 가운데 NVMe/TCP(저장장치 접근 규약 NVMe를 이더넷의 TCP 통신 위에서 쓰는 방식)는 상용 이더넷 기반 시설과 호환되어 널리 쓰이게 되었다. 그러나 성능 요구가 커지면 회선 속도(line rate)를 유지하는 일이 호스트 CPU에 지나친 부담을 준다. 장치 안의 보조 코어(sidecore)로 이 부담을 덜려는 방법은 계산 능력과 메모리 대역폭이 모자라 확장성과 성능이 묶인다. 이 논문은 FPGA 기반 하드웨어 가속으로 NVMe/TCP를 처리하는 DPU 해법 MangoBoost BoostX-NTI(NTI)를 내놓았다. 저장장치 분리 스택 전체를 DPU 카드로 넘겨 호스트 CPU 부담을 없애고, 입출력 경로 전체를 하드웨어에서 바로 실행해 보조 코어를 거치지 않고 칩 밖 메모리도 오가지 않게 해 회선 속도 성능을 냈다. 또 크기와 전력 제약을 맞추고 규약 표준을 따르며, 하드웨어와 소프트웨어 사이를 동적으로 전환·복구할 수 있게 해 실제 데이터센터에 배치할 수 있게 했다. 평가에서 보조 코어 기반 방법보다 처리량이 최대 9.17배, 소프트웨어 방법보다 코어 효율이 16.7배 높았고, AI·클라우드·데이터베이스 작업 부하에서 꾸준히 앞섰다.[^p2] | 1저자 Hamin Jang·Jinha Jeong(랩 표시 공동 1저자 ¹), 마지막 저자 김장우 |
| 3 | 2024 | [SuperCore: An Ultra-Fast Superconducting Processor for Cryogenic Applications](https://doi.org/10.1109/micro61859.2024.00112) · MICRO 2024 | 초전도 단일 자속 양자(SFQ, Single Flux Quantum) 논리 소자군은 매우 빠르고 에너지를 적게 써서 양자 컴퓨팅·천문학·계측 같은 초저온 응용에 유망한 기술로 꼽혀 왔고, 최근 SFQ 기반 컴퓨팅 연구는 초저온 응용을 위한 빠르고 전력을 적게 쓰는 SFQ 프로세서 개발에 힘을 모았다. 그러나 파이프라인(명령 처리를 여러 단계로 나눠 겹쳐 진행하는 구조)이 극도로 깊어서 생기는 성능 문제 때문에 설득력 있는 SFQ 프로세서 설계는 아직 나오지 못했다. 이 논문은 깊은 파이프라인 문제를 풀어 매우 빠르고 전력을 적게 쓰는 순차 실행(in-order) SFQ 프로세서를 제안했다. 먼저 구조 수준의 새 아이디어로 깊이를 최소로 줄인 SFQ 프로세서 파이프라인을 만들고, 깊은 파이프라인을 가진 SFQ 프로세서의 실제 성능 병목 세 가지(멈춤·비우기 논리, 앞 명령이 쓴 값을 뒤 명령이 읽으려고 기다리는 RAW(Read After Write) 멈춤, 명령 인출 장치)를 찾아냈다. 이를 푸는 SFQ에 맞춘 해법 세 가지를 담은 SuperCore는 기준 SFQ 프로세서보다 11배 빨랐고, 4K에서 도는 순차 실행 CMOS 프로세서와 비교하면 6배 빠르면서 전력은 최대 193배 적게 썼다.[^p3] | 1저자 Junhyuk Choi·Ilkwon Byun(랩 표시 공동 1저자 ¹), 마지막 저자 김장우 |
| 4 | 2025 | [LANCER: Low-Overhead, Accurate, and Non-Destructive Calibration for Real-World Fault-Tolerant Quantum Applications](https://doi.org/10.1145/3725843.3756026) · MICRO 2025 | 결함 허용 양자 컴퓨팅(FTQC, Fault-Tolerant Quantum Computing)의 궁극 목표는 실용 응용을 돌리는 것이다. 실용 작업은 실행 시간이 길어서, FTQC 시스템은 잡음이 있는 큐비트의 오류를 바로잡으면서 여러 날 동안 믿을 만하게 동작해야 한다. 그러나 실행 중에 오류를 일으키는 요인이 변해 큐비트 오류율이 높아지는 오류 표류(error drift)가 믿을 만한 실행 시간을 제한하고, 기존의 오류 표류 대처 방법은 큐비트 상태를 무너뜨리거나 오류를 억제하지 못해 오래 걸리는 작업을 실행할 수 없다. 이 논문은 오류 표류 아래에서도 믿을 만하게 실행하도록 정확하고 비파괴적인 보정(calibration, 큐비트를 다루는 제어 값을 재어 다시 맞추는 일) 방법 LANCER를 제안했다. 실행 중 양자 상태를 담고 있는 큐비트는 일부뿐이라는 관찰에서 출발해, 프로그램을 주기적으로 멈추고 양자 상태를 쉬고 있는 큐비트로 잠시 옮겨 상태를 잃지 않고 정확히 보정한다. 이때 생기는 두 문제, 곧 실행 중인 큐비트와 보정 중인 큐비트 사이의 간섭(crosstalk)과 양자 상태를 옮기려고 멈출 때 생기는 큰 지연 부담을 세 가지 해법으로 풀었다. 실행 중인 큐비트의 주파수를 바꿔 보정 중인 큐비트의 주파수와 떼어 놓아 간섭을 줄였고, 결함 허용 양자 게이트(큐비트 상태를 바꾸는 기본 연산)에 원래 있는 쉬는 시간을 활용해 지연 부담을 줄였으며, 양자 상태를 쉬는 큐비트로 옮긴 동안에도 실행할 수 있도록 큐비트 배치를 다시 설계해 지연 부담을 더 줄였다. 평가에서 LANCER는 기준 방법보다 95배 큰 프로그램(곧 게이트 수가 더 많은 프로그램)을 실행할 수 있게 했고, 지연 부담과 큐비트 부담은 각각 4.3%, 4.0%로 무시할 만했다.[^p4] | 1저자 Junpyo Kim, 마지막 저자 김장우 |
| 5 | 2022 | [3D-FPIM: An Extreme Energy-Efficient DNN Acceleration System Using 3D NAND Flash-Based In-Situ PIM Unit](https://doi.org/10.1109/micro56248.2022.00093) · MICRO 2022 | 비휘발성 메모리(전원이 꺼져도 저장한 값이 남는 메모리)의 크로스바 구조(가로 배선과 세로 배선이 엇갈리는 점마다 메모리 소자를 둔 배열)는 아날로그 방식의 행렬-벡터 곱셈을 병렬로, 에너지 효율 높게 할 수 있다. 이를 살리려고 기존 연구는 낮은 정밀도의 곱셈을 메모리 배열에 맡기는 혼합 신호 심층 신경망(DNN, Deep Neural Network) 가속기를 설계했지만, 단순한 아날로그-디지털 변환기(ADC) 설계 때문에 낮은 정밀도 신경망을 정확하고 효율적으로 지원하지 못했고, 아직 성숙하지 않은 RRAM(Resistive RAM, 저항 변화 메모리) 기반 메모리 배열이라 최신 공정 세대에 적용할 수 없었다. 이 논문은 3차원 낸드 플래시 기반의 전체 스택 구조로 낮은 정밀도 신경망을 정확히 배치하는, 에너지 효율적이고 견고한 혼합 신호 DNN 가속 시스템 3D-FPIM을 내놓았다. 특화한 아날로그-디지털 변환 방법을 설계하고 3차원 구조를 활용해 정확도·에너지 효율·견고성을 얻었고, 신경망을 정확하고 효율적으로 배치하도록 DNN 재학습 틀과 맞춤 컴파일러를 함께 제공했다. 산업계에서 검증한 회로 수준 시뮬레이터로 평가한 결과, 기준인 2차원 RRAM 기반 가속기보다 면적당 성능이 평균 2.09배, 에너지 효율이 13.18배 높았다.[^p5] | 1저자 Hunjun Lee·Minseop Kim(랩 표시 공동 1저자 ¹), 마지막 저자 김장우 |
| 6 | 2022 | [NeuroSync: A Scalable and Accurate Brain Simulator Using Safe and Efficient Speculation](https://doi.org/10.1109/hpca53966.2022.00053) · HPCA 2022 | 뇌의 작동 방식을 이해하고 흉내 내려고 신경과학자들은 시간 순서에 따라 진행하는 뇌 시뮬레이션을 쓴다. 시뮬레이션은 뉴런 상태가 시간에 따라 어떻게 바뀌는지 계산하고, 시냅스를 거쳐 연결된 뉴런에 스파이크를 전달하며, 뉴런의 스파이크 활동에 따라 시냅스 가중치가 바뀌는 학습도 모사한다. 기존 시뮬레이터는 정확성을 위해 모든 뉴런·시냅스 상태 변화를 시간 순서대로 계산하는 시간 정밀 방식을 쓰지만, 규모가 커지면 자원이 크게 놀고 에너지 효율이 떨어진다. 이 논문은 추측 실행(결과를 미리 가정해 먼저 계산하고 틀리면 되돌리는 방식) 시뮬레이션을 최소한의 부담으로 쓰고 이를 구조로 뒷받침하는, 빠르고 에너지 효율적이며 규모를 키울 수 있는 하드웨어 가속기 NeuroSync를 내놓았다. 추측 시뮬레이션에 최적인 데이터 흐름으로 효율을 높이고, 추측이 틀렸을 때를 처리하는 되돌림·복구 방식을 설계해 시뮬레이션 정확도를 지켰으며, 추측 실행에 맞춘 학습 시뮬레이션 방법도 제안했다. 평가에서 칩 64개로 이뤄진 NeuroSync는 면적 부담 10.96%만으로 3.37배 빨라지고 에너지 효율이 3.81배 높아졌으며, 시스템 규모가 커질수록 속도 향상도 커졌다.[^p6] | 1저자 Hunjun Lee·Chanmyeong Kim(랩 표시 공동 1저자 ¹), 마지막 저자 김장우 |
| 7 | 2025 | [InfiniMind: A Learning-Optimized Large-Scale Brain-Computer Interface](https://doi.org/10.1145/3695053.3731067) · ISCA 2025 | BCI는 뇌와 컴퓨터를 서로 주고받는 닫힌 고리로 잇고, 뇌 안에 심은 신호 처리기로 신경과학과 의학 여러 분야의 혁신을 이끌고 있다. 최근 연구들은 대규모 응용을 위해 심는 시스템에 비휘발성 메모리(NVM, Non-Volatile Memory)를 넣어야 하고, 기록한 신호의 비정상성(시간에 따라 통계적 성질이 바뀌는 성질)에 대응하려면 시스템 안에서 계속 학습해야 한다고 강조한다. 이 논문은 NVM을 쓰는 BCI 시스템에 학습을 넣을 때 생기는 성능·수명 문제를 처음으로 다뤘다. 학습 때문에 늘어나는 쓰기 부담을 줄이려고 BCI 작업에 맞춘 최적화 네 가지를 제안했다. 갱신 거르기(update filtering)는 BCI 신호가 드문드문 나타나고 되풀이되는 성질을 이용해 불필요한 쓰기를 줄이고, 변화분 버퍼링(delta buffering)은 신호의 시간 지역성을 이용해 NVM 쓰기를 줄이며, 제자리 밖 비우기(out-of-place flushing)는 페이지보다 작은 여러 갱신을 페이지 한 번 쓰기로 묶어 쓰기 증폭을 줄이고, 파형 압축은 신경 신호의 구조적 특징을 이용해 쓰는 데이터 양을 줄인다. 이 최적화들을 메모리 컨트롤러에 구현해 최신 NVM 기반 BCI 시스템에 넣어 학습에 최적화한 시스템 전체를 만들었고, 대표적인 연속 학습 알고리즘에서 성능을 5.39배, 수명을 23.52배 늘렸다.[^p7] | 1저자 Yeongwoo Jang·Daye Jung(랩 표시 공동 1저자 ¹), 마지막 저자 김장우 |
| 8 | 2023 | [Fast, Light-Weight, and Accurate Performance Evaluation using Representative Datacenter Behaviors](https://doi.org/10.1145/3590140.3629117) · Middleware 2023 | 데이터센터는 새 하드웨어 배치와 소프트웨어 패치 같은 새 기능을 들이며 빠르게 바뀌고, 새 기능을 들이려면 수백만 달러 규모 컴퓨팅 기반 시설의 위험을 줄이도록 그 영향을 정확히 평가해야 한다. 그러나 비용과 여러 사용자가 함께 쓰는 성질 때문에 데이터센터 전체 성능 분석은 매우 어렵다. 운영 중인 데이터센터에서 평가하면 정확하지만 실제 서비스에 피해를 줄 수 있어 하기 어렵고, 소규모 시험 환경에서 일반 부하 시험 벤치마크를 돌리면 함께 돌아가는 다른 작업의 영향을 고려하지 못해 부정확하다. 이 논문은 대표적인 데이터센터 동작으로 빠르고 가볍고 정확하게 성능을 평가하는 방법 FLARE를 제안했다. 핵심은 대상 데이터센터에서 가능한 모든 작업 동시 배치(colocation) 가운데 대표적인 소수 시나리오를 뽑는 것이다. 작업 동시 배치를 성능·자원 지표에 따라 체계적으로 특성화하고 묶어 데이터센터 동작에 대한 높은 수준의 통찰을 주고, 이를 시험 환경에서 재구성해 부하 시험 벤치마크로 기능을 정확히 평가하게 한다. 사내 데이터센터와 캐시 크기 조정, DVFS(동작 중에 전압과 주파수를 바꾸는 기법), SMT(코어 하나가 여러 스레드를 동시에 실행하는 기술) 설정의 세 기능으로 평가한 결과, 기능의 영향을 1% 미만의 오차로 추정하면서 평가 비용은 데이터센터 전체 평가보다 50배, 표본 추출 기반 평가보다 10배 낮았다.[^p8] | 1저자 Jaewon Lee, 마지막 저자 김장우 |

## 교수와 전문 분야

김장우 교수는 서울대학교 공과대학 전기·정보공학부 교수다.[^eceprof] 학과 교수 소개는 전공을 「컴퓨터 아키텍처, 모바일/서버 시스템」, 분야를 「컴퓨터 구조, 시스템 설계」로 적고, Research Interest로 CPU·서버 및 데이터센터 설계, 시스템 모델링 및 시뮬레이션, 데이터센터/클라우드 컴퓨터 시스템, 뉴로모픽 컴퓨터 시스템, 초저온 컴퓨터 시스템을 든다.[^eceprof] 교수 개인 페이지 첫머리는 교수를 MangoBoost Inc.의 CEO and Founder이자 서울대 교수로 소개하고, 경력 칸에 MangoBoost Inc의 CEO/Founder(2022 - Current)를 적는다.[^pihome] 학과 교수 소개의 주요경력도 2022년부터 MangoBoost Inc CEO로 적는다.[^eceprof]

학과 교수 소개에 따르면 미국 코넬대학교에서 전기공학 학사(1997)와 컴퓨터과학 석사(2001)를, 카네기멜론대학교에서 전기컴퓨터공학 박사(2008)를 받았다.[^eceprof] 교수 개인 페이지는 박사 지도교수가 Babak Falsafi 교수였고 James C. Hoe, Ken Mai, Anastassia Ailamaki 교수와도 가깝게 연구했으며, 카네기멜론에서는 주로 결함·고장을 견디는 컴퓨터 시스템 구조를 연구했다고 적는다.[^pihome] 학계에 오기 전에는 미국 실리콘밸리의 Sun Microsystems와 Oracle에서 CPU·시스템 설계자로 일하며 다중 코어·다중 스레드 SPARC T4 CPU의 성능 모델링과 검증, 가상 머신 기술을 쓰는 확장성 높은 클라우드 컴퓨팅 서버 개발을 맡았다.[^pihome] 학과 교수 소개의 주요경력은 2008–2009년 Sun Microsystems, 2009–2010년 Oracle Corporation의 CPU/System 아키텍트, 2010–2017년 포항공과대학교 컴퓨터공학과 조교수·부교수, 2017–2019년 서울대학교 전기정보공학부 부교수, 2019년부터 같은 학부 교수다.[^eceprof] 교수 개인 페이지는 POSTECH 재직을 2010–2016년으로, 서울대 재직을 2017년부터로 적는다.[^pihome]

교수 개인 페이지의 Academic Service 칸은 2012–2027년 연도별로 ASPLOS, HPCA, ISCA, MICRO, Top Picks 등의 이름에 (PC)나 (ERC) 표기를 붙여 적고, Academic Awards 칸에는 ASPLOS Hall of Fame(2026), ISCA Hall of Fame(2020), MICRO Hall of Fame(2019)을 적는다.[^pihome]

논문으로 보면 전문 분야는 다섯 갈래다. 첫째, FPGA로 서버의 통신·저장 처리를 하드웨어로 가속하는 장치 중심 서버와 DPU다(대표 논문 1, 2).[^p1][^p2] 둘째, 초전도 SFQ 프로세서 설계와 결함 허용 양자 컴퓨터의 실행 중 보정처럼 극저온에서 도는 컴퓨터의 구조·시스템 설계다(대표 논문 3, 4).[^p3][^p4] 셋째, 3차원 낸드 플래시 메모리 안 연산을 쓰는 딥러닝 가속이다(대표 논문 5).[^p5] 넷째, 뇌 시뮬레이션 가속기와 뇌에 심는 BCI 시스템의 메모리 구조다(대표 논문 6, 7).[^p6][^p7] 다섯째, 데이터센터 성능을 빠르고 정확하게 평가하는 모델링 방법이다(대표 논문 8).[^p8]

## 응용 분야

Research 페이지와 세부 페이지는 응용 대상으로 데이터 분석·기계 학습·가상 머신 같은 서버 응용, 데이터센터 서버, SSD를 여러 개 꽂은 저장 시스템, 가속기를 여러 개 꽂은 AI 학습 서버를 들고,[^research][^server] 여러 AI 응용을 함께 돌리는 예로 여러 사용자가 함께 쓰는 클라우드 서버, 자율 주행, 모바일 시스템을 든다.[^ai] 초저온·초전도·양자 컴퓨팅은 고성능 컴퓨팅과 데이터센터 산업의 요구에서 출발하고,[^cryo] 대표 논문 3은 SFQ 프로세서가 쓰일 초저온 응용으로 양자 컴퓨팅, 천문학, 계측을 든다.[^p3] BCI 시스템 과제는 신경 활동 연구와 함께 발작 탐지, 떨림 억제, 시각 보철 같은 임상 응용을 예로 든다.[^neuro] 대표 논문 2는 AI·클라우드·데이터베이스 작업 부하에서 평가했고,[^p2] 모델링 과제의 WSMeter는 Google에서 검증·적용되었다고 적는다.[^model] 교수 개인 페이지는 MangoBoost가 서울대의 장치 중심 서버 가속 연구와 AI 시스템 가속 연구를 바탕으로 서버 기반 시설 가속 장치를 내놓는다고 적고, 대표 논문 2와 최근 논문 목록의 MangoBoost Alice는 MangoBoost 이름을 붙인 DPU 해법을 다룬다.[^pihome][^p2][^pubs]

## 구성원

2026년 10월 25일 랩 Members 페이지 기준이다. 교수 외 Post Doctoral Researchers 1명, PhD Students 27명, Undergraduate Students 3명이다.[^members] 과정 칸 괄호 안의 MS/PhD·PhD는 교수 개인 페이지 학생 명단의 표기이고, Members 페이지의 PhD Students 가운데 김해원(Haewon Kim)은 개인 페이지 명단에 없다. 개인 페이지 명단은 이 가운데 18명 옆에 "currently @ MangoBoost"를 적는다.[^pimembers] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| 부준혁 (Junehyuk Boo) | 박사후연구원 | 1 |
| 최강현 (Kanghyun Choi) | 박사과정 (MS/PhD) |  |
| 이은복 (Eunbok Lee) | 박사과정 (MS/PhD) |  |
| 김동령 (Dongryeong Kim) | 박사과정 (MS/PhD) |  |
| 정유진 (Yujin Chung) | 박사과정 (MS/PhD) | 1, 6 |
| 김준표 (Junpyo Kim) | 박사과정 (MS/PhD) | 3, 4 |
| 김민섭 (Minseop Kim) | 박사과정 (MS/PhD) | 5, 6 |
| 박보경 (Bogyeong Park) | 박사과정 (MS/PhD) |  |
| 정진하 (Jinha Jeong) | 박사과정 (MS/PhD) | 2 |
| 이원석 (Wonseok Lee) | 박사과정 (MS/PhD) | 2 |
| 최준혁 (Junhyuk Choi) | 박사과정 (MS/PhD) | 3, 4 |
| 조정민 (Jungmin Cho) | 박사과정 (MS/PhD) | 3, 4 |
| 장영우 (Yeongwoo Jang) | 박사과정 (MS/PhD) | 7 |
| 이기환 (Gihwan Lee) | 박사과정 (MS/PhD) |  |
| 정다예 (Daye Jung) | 박사과정 (MS/PhD) | 7 |
| 홍주원 (Juwon Hong) | 박사과정 (MS/PhD) | 3, 4 |
| 정현성 (Hyeonseong Jeong) | 박사과정 (MS/PhD) | 3, 4 |
| 박형주 (Hyungjoo Park) | 박사과정 (MS/PhD) |  |
| 김현석 (Hyeonseok Kim) | 박사과정 (MS/PhD) |  |
| 송승현 (Seunghyun Song) | 박사과정 (MS/PhD) | 7 |
| 윤경수 (Kyeongsu Yun) | 박사과정 (MS/PhD) |  |
| 김세진 (Sejin Kim) | 박사과정 (PhD) |  |
| 추현재 (Hyunjae Chu) | 박사과정 (MS/PhD) | 2 |
| 최종현 (Jonghyun Choi) | 박사과정 (MS/PhD) |  |
| 김한민 (Hanmin Kim) | 박사과정 (MS/PhD) |  |
| 김남규 (Namkyu Kim) | 박사과정 (MS/PhD) |  |
| 김나연 (Nayeon Kim) | 박사과정 (MS/PhD) |  |
| 김해원 (Haewon Kim) | 박사과정 |  |
| 이도규 (Dogyu Lee) | 학부 연구생 |  |
| 윤채원 (Chaewon Yun) | 학부 연구생 |  |
| 조원우 (Wonoo Cho) | 학부 연구생 |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 PhD Alumni 20명과 MS Alumni 6명에, 교수 개인 페이지 학생 명단의 박사 졸업생 칸에만 있는 1명(Jihun Kim)을 더한 27명이다.[^alumni][^pimembers] 학위 칸의 박사·석사는 Alumni 페이지의 구분이고, 괄호 안 학교(POSTECH, SNU)는 교수 개인 페이지 명단의 학위 표기다. 진로 칸 앞부분은 Alumni 페이지 표기이고, 「교수 개인 페이지:」 뒤는 개인 페이지 명단이 같은 사람에게 적은 직위·기관이다. 김창수(Changsu Kim)는 개인 페이지 명단에서 박사후연구원 졸업생 칸에 Changsoo Kim으로, 김찬명(Chanmyeong Kim)과 장하민(Hamin Jang)은 현재 학생 칸에 올라 있다. 학위 학교가 POSTECH으로 적힌 졸업생도 함께 들어 있다(교수는 2010–2016년 POSTECH에 있었다).[^pimembers][^pihome]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 김영석 (Youngsok Kim) | 박사 (POSTECH) | Professor @ Yonsei Uni. / 교수 개인 페이지: Associate Professor @ Yonsei University |
| 이재원 (Jaewon Lee) | 박사 (POSTECH) | Meta (USA) / 교수 개인 페이지: Researcher @ Meta (USA) |
| 채동주 (Dongju Chae) | 박사 (POSTECH) | MangoBoost / 교수 개인 페이지: SW architect @ MangoBoost |
| 장한휘 (Hanhwi Jang) | 박사 (POSTECH) | Google (USA) / 교수 개인 페이지: Researcher @ Google (USA) |
| 안재형 (Jaehyung Ahn) | 박사 (POSTECH) | Samsung SAIT / 교수 개인 페이지: Researcher @ Samsung SAIT |
| Mohammadamin Ajdari | 박사 (POSTECH) | Professor @ Tsinghua Uni. / 교수 개인 페이지: Assistant Professor @ Tsinghua University (China) |
| 조재언 (Jae-Eon Jo) | 박사 (POSTECH) | Samsung SAIT / 교수 개인 페이지: Researcher @ Samsung SAIT |
| 김준성 (Joonsung Kim) | 박사 (SNU) | Professor @ Sungkyunkwan Uni. / 교수 개인 페이지: Assistant Professor @ Sungkyunkwan University |
| 권동업 (Dongup Kwon) | 박사 (SNU) | MangoBoost / 교수 개인 페이지: CTO @ MangoBoost |
| 김창수 (Changsu Kim) | 박사 (교수 개인 페이지 표기 PostDoc (SNU)/PhD (POSTECH)) | MangoBoost / 교수 개인 페이지: SW architect @ MangoBoost |
| 이규현 (Gyuhyeon Lee) | 박사 (SNU) | MangoBoost / 교수 개인 페이지: SW architect @ MangoBoost |
| 박평수 (Pyeongsu Park) | 박사 (SNU) | Meta (USA) / 교수 개인 페이지: Researcher @ Meta (USA) |
| 백은진 (Eunjin Baek) | 박사 (SNU) | MangoBoost / 교수 개인 페이지: HW architect @ MangoBoost |
| 이헌준 (Hunjun Lee) | 박사 (SNU) | Professor @ Hanyang Uni. / 교수 개인 페이지: Assistant Professor @ Hanyang University |
| 민동문 (Dongmoon Min) | 박사 (SNU) | Professor @ Sungkyunkwan Uni. / 교수 개인 페이지: Assistant Professor @ Sungkyunkwan University |
| 변일권 (Ilkwon Byun) | 박사 (SNU) | Professor @ Kyushu Uni. / 교수 개인 페이지: Associate Professor @ Kyushu University (Japan) |
| 정희택 (Heetaek Jeong) | 박사 (SNU) | Mangoboost / 교수 개인 페이지: HW architect @ MangoBoost |
| 이원식 (Wonsik Lee) | 박사 (SNU) | Mangoboost / 교수 개인 페이지: HW architect @ MangoBoost |
| 김찬명 (Chanmyeong Kim) | 박사 (교수 개인 페이지 명단은 현재 학생 MS/PhD로 적음) | Mangoboost |
| 장하민 (Hamin Jang) | 박사 (교수 개인 페이지 명단은 현재 학생 MS/PhD로 적음) | Mangoboost |
| 이다열 (Dayeol Lee) | 석사 (POSTECH) | 1st position: UC Berkeley Graduate School / 교수 개인 페이지: Researcher @ TikTok |
| 이성화 (Sunghwa Lee) | 석사 (SNU) | 1st position: SNU Law School / 교수 개인 페이지: JD student @ SNU Law School |
| 이승호 (Seungho Lee) | 석사 (SNU) | 1st position: SNU GSCST / 교수 개인 페이지: PhD student @ SNU GSCST |
| 허수연 (Suyeon Hur) | 석사 (SNU) | 1st position: Naver / 교수 개인 페이지: Researcher @ Naver |
| 나성민 (Seongmin Na) | 석사 졸업생 칸 (교수 개인 페이지 표기 BS (SNU)) |  |
| 강태헌 (Taehun Kang) | 석사 졸업생 칸 (교수 개인 페이지 표기 BS (SNU)) |  |
| Jihun Kim | 박사 (POSTECH, 교수 개인 페이지 학생 명단에만 있음) | 교수 개인 페이지: Researcher @ Financial Security Institute |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지 2021–2026년 연도 구역의 38편(2026년 7, 2025년 5, 2024년 4, 2023년 5, 2022년 7, 2021년 10)이다. 연도는 페이지의 연도 구역이고, 저자·제목·학회와 학술지 이름·연월은 랩 표기 그대로다. 저자 이름 뒤의 ¹은 랩이 공동 1저자(The co-first authorship)로 표시한 저자다. 「Oct. 2026 (to appear)」로 적힌 MICRO 2026 두 편(BoostX-RNIC, SafeMind)은 랩 첫 화면 소식이 채택을 알린 논문이라 「채택」으로 표시했다. 교수는 2017년부터 서울대에 있어 목록의 논문은 모두 서울대 시기 논문이다.[^pubs][^home][^pihome]

**2026**

- Kanghyun Choi¹, Bogyeong Park¹, Gihwan Lee, Hanmin Kim, Nayeon Kim, Chanmyeong Kim, Hyeonseong Choi, Dongjoo Lee, Jaehyun Lee, Eunjin Baek, Changsu Kim, Changyeon Jo, Minho Chu, and Jangwoo Kim. "BoostX-RNIC: Fast, Scalable and Flexible AI RNIC". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Oct. 2026 (to appear), 채택*.
- Daye Jung¹, Yeongwoo Jang¹, Seunghyun Song, and Jangwoo Kim. "SafeMind: A Battery-Free Processing System for Safely Implantable Brain-Computer Interfaces". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Oct. 2026 (to appear), 채택*.
- Hamin Jang¹, Jinha Jeong¹, Wonseok Lee, Jun Heo, Jongcheon Lee, Hyunjae Chu, Taehyun Kim, Youngwoo Jeong, Dongu Kim, Heetaek Jeong, Changsu Kim, Dongup Kwon and Jangwoo Kim. "BoostX-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Acceleration". *ACM/IEEE International Symposium on Computer Architecture (ISCA), Jun. 2026*.
- Jungmin Cho¹, Hyeonseong Jeong¹, Junpyo Kim, Junhyuk Choi, Juwon Hong, and Jangwoo Kim. "Accelerating Computation in Quantum LDPC Code". *31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Mar. 2026*.
- Seunghyun Song, Yeongwoo Jang, Daye Jung, Kyungsoo Park, Donghan Kim, Gwangjin Kim, Hunjun Lee, Jerald Yoo, and Jangwoo Kim. "TierX: A Simulation Framework for Multi-tier BCI System Design Evaluation and Exploration". *31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Mar. 2026*.
- Jangwoo Kim, Junpyo Kim, Junhyuk Choi, Jungmin Cho, Juwon Hong, Hyeonseong Jeong, Dongmoon Min, Ilkwon Byun, Masamitsu Tanaka, and Koji Inoue. "Architecting a Full-Stack Superconducting Fault-Tolerant Quantum Computer". *IEEE Micro, Feb. 2026*.
- Koji Inoue, Ilkwon Byun, Masamitsu Tanaka, Yosuke Ueno, Naoki Takeuchi, Satoshi Kawakami, Olivia Chen, Dongmoon Min, Teruo Tanimoto, Takatsugu Ono, Hiroshi Nakamura, and Jangwoo Kim. "Toward Ultra-High-Speed, Ultra-Low-Power Cryogenic Superconductor Computing". *IEEE Computer, Feb. 2026*.

**2025**

- Heetaek Jeong¹, Wonsik Lee¹, Eunjin Baek, Changsu Kim, Dongju Chae, Kanghyun Choi, Hamin Jang, Mohamed Elgammal, Sungmin Hong, Eriko Nurvitadhi, Dongup Kwon, and Jangwoo Kim. "MangoBoost Alice: Extremely Fast, Seamless, and Versatile FPGA-accelerated DPU Solutions". *IEEE Micro, 2025*.
- Heetaek Jeong¹, Kanghyun Choi¹, Hamin Jang, Dongup Kwon, Eunjin Baek, Pyeongsu Park, and Jangwoo Kim. "FS2: A Fast, Scalable and Flexible Switching System for Emerging Interconnects". *IEEE Micro, 2025*.
- Junhyuk Choi, Juwon Hong, Junpyo Kim, Jungmin Cho, Hyeonseong Jeong, Dongmoon Min, Masamitsu Tanaka, Koji Inoue, and Jangwoo Kim. "SuperSFQ: A Hardware Design to Realize High-Frequency Superconducting Processors". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Oct. 2025*.
- Junpyo Kim, Jungmin Cho, Hyeonseong Jeong, Dongmoon Min, Junhyuk Choi, Juwon Hong, and Jangwoo Kim. "LANCER: Low-Overhead, Accurate, and Non-Destructive Calibration for Real-World Fault-Tolerant Quantum Applications". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Oct. 2025*.
- Yeongwoo Jang¹, Daye Jung¹, Seunghyun Song, Hunjun Lee, and Jangwoo Kim. "InfiniMind: A Learning-Optimized Large-Scale Brain-Computer Interface". *ACM/IEEE International Symposium on Computer Architecture (ISCA), Jun. 2025*.

**2024**

- Junhyuk Choi¹, Ilkwon Byun¹, Juwon Hong, Dongmoon Min, Junpyo Kim, Jungmin Cho, Hyeonseong Jeong, Masamitsu Tanaka, Koji Inoue, and Jangwoo Kim. "SuperCore: An Ultra-Fast Superconducting Processor For Cryogenic Applications". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Nov. 2024*.
- Hunjun Lee, Yeongwoo Jang, Daye Jung, Seunghyun Song, and Jangwoo Kim. "Rearchitecting a Neuromorphic Processor for Spike-Driven Brain-Computer Interfacing". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Nov. 2024*.
- Dongmoon Min, Ilkwon Byun, Gyu-Hyeon Lee, and Jangwoo Kim. "CoolDC: A Cost-Effective Immersion-Cooled Datacenter with Workload-Aware Temperature Scaling". *ACM Transactions on Architecture and Code Optimization (TACO), May. 2024*.
- Junpyo Kim, Dongmoon Min, Jungmin Cho, Hyeonseong Jeong, Ilkwon Byun, Junhyuk Choi, Juwon Hong, and Jangwoo Kim. "A Fault-Tolerant Million Qubit-Scale Distributed Quantum Computer". *29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Apr. 2024*.

**2023**

- Jaewon Lee, Dongmoon Min, Ilkwon Byun, Hanhwi Jang, and Jangwoo Kim. "Fast, Light-Weight, and Accurate Performance Evaluation using Representative Datacenter Behaviors". *2023 ACM/IFIP/USENIX International Middleware Conference (MIDDLEWARE), Dec. 2023*.
- Junehyuk Boo, Yujin Chung, Eunjin Baek, Seongmin Na, Changsu Kim, and Jangwoo Kim. "F4T: A Fast and Flexible FPGA-based Full-stack TCP Acceleration Framework". *50th ACM/IEEE International Symposium on Computer Architecture (ISCA), Jun. 2023*.
- Dongmoon Min, Junpyo Kim, Junhyuk Choi, Ilkwon Byun, Masamitsu Tanaka, Koji Inoue, and Jangwoo Kim. "QIsim: Architecting 10+K Qubit QC Interfaces Toward Quantum Supremacy". *50th ACM/IEEE International Symposium on Computer Architecture (ISCA), Jun. 2023*.
- Eunjin Baek, Eunbok Lee, Taehun Kang, and Jangwoo Kim. "STfusion: Fast and Flexible Multi-NN Execution using Spatio-Temporal Block Fusion and Memory Management". *IEEE Transactions on Computers (TC), Apr. 2023*.
- Suyeon Hur, Seongmin Na, Dongup Kwon, Joonsung Kim, Andrew Boutros, Eriko Nurvitadhi, and Jangwoo Kim. "A Fast and Flexible FPGA-based Accelerator for Natural Language Processing Neural Networks". *ACM Transactions on Architecture and Code Optimization (TACO), vol. 20, Feb. 2023*.

**2022**

- Hunjun Lee¹, Minseop Kim¹, Dongmoon Min, Joonsung Kim, Jongwon Back, Honam Yoo, Jongho Lee, and Jangwoo Kim. "3D-FPIM: An Extreme Energy-Efficient DNN Acceleration System Using 3D NAND Flash-Based In-Situ PIM Unit". *55th IEEE/ACM International Symposium on Microarchitecture (MICRO), Oct. 2022*.
- Ilkwon Byun, Junpyo Kim, Dongmoon Min, Ikki Nagaoka, Kosuke Fukumitsu, Iori Ishikawa, Teruo Tanimoto, Masamitsu Tanaka, Koji Inoue, and Jangwoo Kim. "XQsim: Modeling Cross-Technology Control Processors for 10+K Qubit Quantum Computers". *49th ACM/IEEE International Symposium on Computer Architecture (ISCA), Jun. 2022*.
- Hamin Jang¹, Taehun Kang¹, Joonsung Kim, Jaeyong Cho, Jae-Eon Jo, Seungwook Lee, Wooseok Chang, Jangwoo Kim, and Hanhwi Jang. "LSim: Fine-Grained Simulation Framework for Large-Scale Performance Evaluation". *IEEE Computer Architecture Letters (CAL), Apr. 2022*.
- Hunjun Lee¹, Chanmyeong Kim¹, Minseop Kim, Yujin Chung, and Jangwoo Kim. "NeuroSync: A Scalable and Accurate Brain Simulation System using Safe and Efficient Speculation". *28th IEEE International Symposium on High-Performance Computer Architecture (HPCA), Apr. 2022*.
- Dongup Kwon¹, Wonsik Lee¹, Dongryeong Kim, Junehyuk Boo, and Jangwoo Kim. "SmartFVM: A Fast, Flexible, and Scalable Hardware-based Virtualization for Commodity Storage Devices". *ACM Transactions on Storage (TOS), 2022*.
- Dongmoon Min¹, Yujin Chung¹, Ilkwon Byun, Junpyo Kim, and Jangwoo Kim. "CryoWire: Wire-Driven Microarchitecture Designs for Cryogenic Computing". *27th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Feb. 2022*.
- Pyeongsu Park, Jaewon Lee, Heetaek Jeong, and Jangwoo Kim. "DLS: A Fast and Flexible Neural Network Training System with Fine-grained Heterogeneous Device Orchestration". *IEEE Transactions on Parallel and Distributed Systems (TPDS), Jan. 2022*.

**2021**

- Joonsung Kim¹, Hamin Jang¹, Hunjun Lee, Seungho Lee, and Jangwoo Kim. "UC-Check: Characterizing Micro-operation Caches in x86 Processors and Implications in Security and Performance". *ACM/IEEE International Symposium on Microarchitecture (MICRO), Oct. 2021*.
- Joonsung Kim, Suyeon Hur, Eunbok Lee, Seungho Lee, and Jangwoo Kim. "NLP-Fast: A Fast, Scalable, and Flexible System to Accelerate Large-Scale Heterogeneous NLP Models". *IEEE International Conference on Parallel Architecture and Compilation Techniques (PACT), Sep 2021*.
- Hunjun Lee, Chanmyeong Kim, Seungho Lee, Eunjin Baek, and Jangwoo Kim. "An Accurate and Fair Evaluation Methodology for SNN-Based Inferencing with Full-Stack Hardware Design Space Explorations". *Neurocomputing, Sep 2021*.
- Dongup Kwon, Dongryeong Kim, Junehyuk Boo, Wonsik Lee, and Jangwoo Kim. "A Fast and Flexible Hardware-based Virtualization Mechanism for Computational Storage Devices". *USENIX Annual Technical Conference (ATC), July. 2021*.
- Joonsung Kim, Kanghyun Choi, Wonsik Lee, and Jangwoo Kim. "Performance Modeling and Practical Use Cases for Black-Box SSDs". *ACM Transactions on Storage (TOS), Jun. 2021*.
- Gyuhyeon Lee, Seongmin Na, Ilkwon Byun, Dongmoon Min, and Jangwoo Kim. "CryoGuard: A Near Refresh-Free Robust DRAM Design for Cryogenic Computing". *48th ACM/IEEE International Symposium on Computer Architecture (ISCA), June. 2021*.
- Ilkwon Byun¹, Dongmoon Min¹, Gyu-Hyeon Lee, Seongmin Na, and Jangwoo Kim. "A Next-Generation Cryogenic Processor Architecture". *IEEE Micro Special Issue: Top Picks from Computer Architecture Conferences (IEEE’s Micro Top Picks), May/June. 2021*.
- Koki Ishida¹, Ilkwon Byun¹, Ikki Nagaoka, Kosuke Fukumitsu, Masamitsu Tanaka, Satoshi Kawakami, Teruo Tanimoto, Takatsugu Ono, Jangwoo Kim, and Koji Inoue. "Superconductor Computing for Neural Networks". *IEEE Micro Special Issue: Top Picks from Computer Architecture Conferences (IEEE’s Micro Top Picks), May/June. 2021*.
- Jaewon Hur, Suhwan Song, Dongup Kwon, Eunjin Baek, Jangwoo Kim, and Byoungyoung Lee. "DiFuzzRTL: Differential Fuzz Testing to Find CPU Bugs". *IEEE Symposium on Security and Privacy (S&P), May 2021*.
- Hunjun Lee¹, Chanmyeong Kim¹, Yujin Chung, and Jangwoo Kim. "NeuroEngine: A Hardware-Based Event-Driven Simulation System for Advanced Brain-Inspired Computing". *26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Apr. 2021*.

## 소식

랩 누리집 소식 글 가운데 2021-10-22–2026-10-22에 게시된 글 23건이다. 날짜는 글에 표시된 게시일이고, 제목과 내용은 게시된 문장 그대로다. 같은 논문(NeuroSync, HPCA 2022)의 채택 소식이 2021-11-26과 2022-07-22 두 번 올라 있다.[^news]

- 2026-09-08 · Two papers are accepted to MICRO 2026: K. Choi, B. Park et al., “BoostX-RNIC: Fast, Scalable and Flexible AI RNIC”, MICRO 2026 (to appear); D. Jung, Y. Jang et al., “SafeMind: A Battery-Free Processing System for Safely Implantable Brain-Computer Interfaces”, MICRO 2026 (to appear)
- 2026-05-13 · One paper is accepted to ISCA 2026: H. Jang, J. Jeong et al., “BoostX-NTI: Fast, Scalable, and Flexible Storage Architecture with NVMe/TCP Acceleration”, ISCA 2026
- 2026-01-27 · Two papers are accepted to ASPLOS 2026: S. Song et al., “TierX: A Simulation Framework for Multi-tier BCI System Design Evaluation and Exploration”, ASPLOS 2026; J. Cho, H. Jeong et al, “Accelerating Computation in Quantum LDPC Code”, ASPLOS 2026
- 2026-01-03 · One paper is accepted to IEEE Micro 2026: J. Kim et al., “Architecting a Full-Stack Superconducting Fault-Tolerant Quantum computer”, IEEE Micro 2026
- 2026-01-02 · One paper is accepted to IEEE Computer 2026: K. Inoue et al., “Toward Ultra-High-Speed, Ultra-Low-Power Cryogenic Superconductor Computing”, IEEE Computer 2026
- 2025-07-21 · Two papers are accepted to IEEE Micro: H. Jeong, K. Choi et al., “FS2: A Fast, Scalable and Flexible Switching System for Emerging Interconnects”, IEEE Micro; H. Jeong, W. Lee et al., “MangoBoost Alice: Extremely Fast, Seamless, and Versatile FPGA-accelerated DPU Solutions”, IEEE Micro
- 2025-07-21 · Two papers are accepted to MICRO 2025: J. Choi et al., “SuperSFQ: A Hardware Design to Realize High-Frequency Superconducting Processors”, MICRO 2025; J. Kim et al., “LANCER: Low-Overhead, Accurate, and Non-Destructive Calibration for Real-World Fault-Tolerant Quantum Applications”, MICRO 2025
- 2025-05-29 · One paper is accepted to ISCA 2025: Y. Jang, D. Jung et al., “InfiniMind: A Learning-Optimized Large-Scale Brain-Computer Interface”, ISCA 2025
- 2024-07-18 · Two papers are accepted to MICRO 2024: J. Choi, I. Byun et al., “SuperCore: An Ultra-Fast Superconducting Processor For Cryogenic Applications”, MICRO 2024; H. Lee et al., “Rearchitecting a Neuromorphic Processor for Spike-Driven Brain-Computer Interfacing”, MICRO 2024
- 2024-07-18 · One paper is accepted to TACO 2024: D.min, et al., “CoolDC: A Cost-Effective Immersion-Cooled Datacenter with Workload-Aware Temperature Scaling”, TACO 2024
- 2024-01-10 · One paper is accepted to ASPLOS 2024: J. Kim, et al., “A Fault-Tolerant Million Qubit-Scale Distributed Quantum Computer”, ASPLOS 2024
- 2024-01-10 · One paper is accepted to MIDDLEWARE 2023: J. Lee, et al., “Fast, Light-Weight, and Accurate Performance Evaluation using Representative Datacenter Behaviors”, MIDDLEWARE 2023
- 2023-04-12 · Two papers are accepted to ISCA 2023: D. Min, et al., “QIsim: Architecting 10+K Qubit QC Interfaces Toward Quantum Supremacy”, ISCA 2023; J. Boo, et al., “F4T: A Fast and Flexible FPGA-based Full-stack TCP Acceleration Framework”, ISCA 2023
- 2022-10-05 · One paper is accepted to TACO 2022: S. Hur, et al., “A Fast and Flexible FPGA-based Accelerator for Natural Language Processing Neural Networks”, TACO 2022
- 2022-09-25 · One paper is accepted to TC 2022: E. Baek, et al., “STfusion: Fast and Flexible Multi-NN Execution using Spatio-Temporal Block Fusion and Memory Management”, TC 2022
- 2022-07-22 · One paper is accepted to MICRO 2022: H. Lee, M. Kim et al., “3D-FPIM: An Extreme Energy-Efficient DNN Acceleration System Using 3D NAND Flash-Based In-Situ PIM Unit”, MICRO 2022
- 2022-07-22 · One paper is accepted to CAL 2022: H. Jang, T. Kang et al., “LSim: Fine-Grained Simulation Framework for Large-Scale Performance Evaluation”, CAL 2022
- 2022-07-22 · One paper is accepted to HPCA 2022: H. Lee, C. Kim et al., “NeuroSync: A Scalable and Accurate Brain Simulation System using Safe and Efficient Speculation”, HPCA 2022
- 2022-03-20 · One paper is accepted to ISCA 2022: I. Byun et al., “XQsim: Modeling Cross-Technology Control Processors for 10+K Qubit Quantum Computers”, ISCA 2022
- 2022-01-12 · One paper is accepted to TOS 2022: D. Kwon, W. Lee et al., “SmartFVM: A Fast, Flexible, and Scalable Hardware-based Virtualization for Commodity Storage Devices”, TOS 2022
- 2022-01-10 · One paper is accepted to TPDS 2022: P. Park et.al., “DLS: A Fast and Flexible Neural Network Training System with Fine-grained Heterogeneous Device Orchestration”, TPDS 2022
- 2021-11-26 · One paper is accepted to ASPLOS 2022: D. Min, Y. Chung et.al., “CryoWire: Wire-Driven Microarchitecture Designs for Cryogenic Computing”, ASPLOS 2022
- 2021-11-26 · One paper is accepted to HPCA 2022: H. Lee, C. Kim, et.al., “NeuroSync: A Scalable and Accurate Brain Simulation System using Safe and Efficient Speculation”, HPCA 2022

## 연락과 위치

- 연구실: 서울대학교 133동 413호(누리집 표기 413, Bldg 133, Seoul National University, 1 Gwanak-ro, Gwanak-gu, Seoul, KOREA), 전화 02-880-7298[^home][^ecelabd]
- 교수 연구실: 301동 902호, 전화 02-880-1868[^eceprof][^pihome]
- 학과 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^eceprof]
[^p1]: J. Boo 외, J. Kim, Proceedings of the 50th Annual International Symposium on Computer Architecture, 1-13 (온라인 2023-06-17). <https://doi.org/10.1145/3579371.3589090> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Jang 외, J. Kim, 2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA), 1029-1043 (2026). <https://doi.org/10.1109/isca66397.2026.00081> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Choi 외, J. Kim, 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO), 1532-1547 (2024). <https://doi.org/10.1109/micro61859.2024.00112> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Kim 외, J. Kim, Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture, 547-563 (온라인 2025-10-17). <https://doi.org/10.1145/3725843.3756026> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Lee 외, J. Kim, 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO), 1359-1376 (2022). <https://doi.org/10.1109/micro56248.2022.00093> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. Lee 외, J. Kim, 2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA), 633-647 (2022). <https://doi.org/10.1109/hpca53966.2022.00053> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y. Jang 외, J. Kim, Proceedings of the 52nd Annual International Symposium on Computer Architecture, 1969-1985 (온라인 2025-06-20). <https://doi.org/10.1145/3695053.3731067> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Lee 외, J. Kim, Proceedings of the 24th International Middleware Conference, 220-233 (온라인 2023-11-27). <https://doi.org/10.1145/3590140.3629117> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면 <https://hpcs.snu.ac.kr/> (연구실 소개, Latest News, Computer Architecture and System 목록, Contact Info, 2026-10-25 열람)
[^research]: Research 페이지 <https://hpcs.snu.ac.kr/research/> (다섯 연구 과제 소개, 2026-10-25 열람)
[^server]: Research 세부 페이지 Server Architecture <https://hpcs.snu.ac.kr/research/server-architecture/> (Motivation, Research, Software release, Publications, 2026-10-25 열람)
[^cryo]: Research 세부 페이지 Cryogenic/Superconducting/Quantum Computing <https://hpcs.snu.ac.kr/research/cryogenic-and-quantum-computing/> (Motivation, Research, Software release, Publications, 2026-10-25 열람)
[^ai]: Research 세부 페이지 AI Acceleration System <https://hpcs.snu.ac.kr/research/ai-acceleration-system/> (Motivation, Research, Software release, Publications, 2026-10-25 열람)
[^neuro]: Research 세부 페이지 Neuromorphic Computing <https://hpcs.snu.ac.kr/research/neuromorphic-computing/> (Motivation, Research, Software release, Publications, 2026-10-25 열람)
[^model]: Research 세부 페이지 Computer System Modeling and Analysis <https://hpcs.snu.ac.kr/research/system-modeling-and-simulation-methodology/> (Motivation, Research, Software release, Publications, 2026-10-25 열람)
[^members]: Members 페이지 <https://hpcs.snu.ac.kr/members/> (Professors, Post Doctoral Researchers, PhD Students, Undergraduate Students, 2026-10-25 열람)
[^alumni]: Alumni 페이지 <https://hpcs.snu.ac.kr/members/alumni/> (PhD Alumni, MS Alumni, 2026-10-25 열람)
[^pubs]: Publications 페이지 <https://hpcs.snu.ac.kr/publications/> (2013–2026년 연도 구역, 2026-10-25 열람)
[^news]: 누리집 소식 글 모음(작성자 hpcs의 글 목록) <https://hpcs.snu.ac.kr/author/hpcs/> 1–3쪽 (주소 목록은 근거 페이지, 2026-10-25 열람)
[^pihome]: 김장우 교수 개인 페이지 <https://hpcs.snu.ac.kr/~jangwoo/> (Biography, Research, Education, Employment, Academic Service, Academic Awards, Publications, 연락처, 2026-10-25 열람)
[^pimembers]: 교수 개인 페이지 학생 명단 <https://hpcs.snu.ac.kr/~jangwoo/members.html> (Postdoc researchers, Current students, Alumni, 2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-25 열람)
[^ecelabd]: 서울대학교 전기·정보공학부 연구실 소개(고성능 컴퓨터 시스템 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=22> (연구실 이름, 지도교수, 연구, TEL, 연구실 소개 및 연구분야, 최근 관심분야 및 주요 연구과제, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 소개(김장우) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p817> (직위, TEL, OFFICE, 학위, 전공, 분야, 학력, 주요경력, Research Interest, 학과 주소, 2026-10-25 열람)

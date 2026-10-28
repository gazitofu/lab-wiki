# 차세대 박막소자 및 회로 연구실 (Advanced TFTs and Smart Electronics Laboratory, ACELAB)

**서울대학교 공과대학 전기·정보공학부 · 이수연 부교수**

- 분야: 산화물 박막 소자, 디스플레이 화소·보상 회로, 뉴로모픽 소자·시스템, 광집적회로
- 대분야: 전기전자·반도체·광학
- 태그: 산화물 반도체[^oxide], 뉴로모픽 소자[^oxide][^neuro], 광집적회로[^photonics], 유연·신축 전자[^oxide], 디스플레이 구동·보상 회로[^pixel][^p1][^p3]
- 홈페이지: <https://sites.google.com/view/snu-acelab/home>
- 근거와 출처: [ACELAB 근거 페이지](acelab-sources.md)

> 산화물 박막 소자를 만들고 분석하며, 이를 디스플레이를 구동하는 회로와 신경계의 정보 처리를 본뜬 하드웨어, 빛을 다루는 집적회로로 연결하는 연구실이다.[^home][^research]

## 무엇을 연구하나

이수연 교수가 이끄는 연구실은 박막(두께가 얇은 재료층)으로 만든 소자(전기·광학 등의 기능을 수행하는 부품)를 연구한다. 중심 재료는 산화물 반도체(산소와 다른 원소가 결합한 반도체)다. 재료로 소자를 제작하는 일, 그 동작을 분석하고 모델링(대상의 성질과 동작을 수식이나 계산 모형으로 나타내는 일)하는 일, 회로와 구동 방법으로 성능을 보완하는 일을 함께 다룬다.[^home][^department]

첫 갈래는 화면의 밝기를 제어하는 회로다. TFT(Thin-Film Transistor, 박막 반도체에 흐르는 전하를 전압으로 제어하는 소자)를 이용해 화소(화면을 구성하는 개별 표시 단위)를 구동한다. 특히 a-IGZO(amorphous indium-gallium-zinc oxide, 원자 배열이 장거리 규칙성을 갖지 않는 인듐·갈륨·아연 산화물)를 쓴다. OLED(Organic Light-Emitting Diode, 유기물에서 전기에너지를 빛으로 바꾸는 소자) 화소에서는 소자마다 다른 문턱전압(트랜지스터가 켜지는 경계를 정하는 전압), 이동도(전기장에 반응해 전하가 움직이는 정도), 문턱전압 이하 스윙(전류가 열 배 변하는 데 필요한 문턱전압 이하 영역의 게이트 전압 변화량)을 보상하는 회로를 개발한다. 마이크로 LED(Light-Emitting Diode, 전류가 흐를 때 빛을 내는 반도체 소자를 미세화한 것)에서는 빛을 내는 시간을 조절하는 PWM(Pulse Width Modulation, 일정 시간 동안 나타나는 신호의 지속 시간을 바꾸는 방식) 회로를 연구한다.[^pixel]

둘째 갈래는 산화물 소자 자체의 구조와 안정성이다. 플라스마(기체에서 분리된 전자와 전하를 띤 원자·분자들이 전기장과 자기장에 집단적으로 반응하는 상태) 처리와 재료가 맞닿는 계면 분석으로 소자의 동작이 시간과 사용 조건에 따라 달라지는 원인을 살핀다. 소자가 줄어들 때 생기는 문제를 분석하고, 접촉 부분에 중간층을 넣거나 구조를 바꾸는 방법도 개발한다. 늘어나는 전자소자에서는 단단한 섬 구조와 금속 연결부를 설계하고, 반복 변형에 따른 성능 변화를 조사한다.[^oxide]

셋째 갈래는 뉴로모픽(신경세포와 그 연결의 정보 처리 방식을 본뜨는 계산) 하드웨어다. 시냅스(신경세포 사이에서 신호 전달을 조절하는 연결)를 본뜬 트랜지스터에 정보를 저장하고, 신경세포 역할을 하는 회로와 연결한다. 연구 범위는 소자에 흐르는 전류 조절에서 회로 배열과 신경망(연결된 계산 단위들의 결합으로 정보를 처리하는 모형)의 계산까지 이어진다. 신경망의 연결 강도를 저장하는 비휘발성(전원을 꺼도 정보가 유지되는 성질) 소자와 그 배열, 실제 소자에 근거한 회로 모형을 함께 개발한다.[^oxide][^neuro][^p4][^p6]

넷째 갈래는 광집적회로(빛을 보내고 나누고 바꾸는 부품을 한 칩에 모은 회로)다. 도파관(빛이나 전자기파가 정해진 경로를 따라 전파되도록 하는 구조)에 산화물 광검출기를 결합하고, 레이저 디스플레이와 빛을 이용한 뉴로모픽 계산을 연구한다. 광트랜지스터(입사한 빛에 따라 전류가 달라지는 트랜지스터)에서는 재료 조합을 바꾸어 빛에 대한 응답과 잔류 전류를 조절한다. 대표 논문 8은 전압을 없앤 뒤에도 남는 광학 상태 변화를 재료의 결정 구조와 연결한다.[^photonics][^p8]

## 주요 연구 주제

### 1. 화소 회로와 밝기 보상

어두운 밝기 단계에서 화소마다 같은 밝기를 내도록 회로·구동 신호·보상 알고리즘을 설계한다. 산화물 TFT 회로와 실리콘 회로를 모두 다루며, 화면 측정 결과를 이용한 보상도 연구한다. 대표 논문 1–3은 각각 마이크로 LED 구동 신호, 소자 구조를 통한 전류 조절 특성, 화면의 밝기 불균일 보상을 다룬다.[^pixel][^p1][^p2][^p3]

### 2. 소자 구조·신뢰성과 신축 전자

산화물 TFT의 결함과 접촉 구조, 소자 크기에 따른 동작 변화, 늘어나는 구조에서의 기계적 변형을 분석한다. 컴퓨터 계산과 실제 소자 제작·측정을 연결하고, 유한요소해석(대상을 유한한 부분들로 나누어 해를 근사하는 수치해석 방법)으로 변형에 취약한 곳과 구조 설계의 영향을 살핀다.[^oxide]

### 3. 정보를 저장하며 계산하는 소자와 회로

전하를 저장하는 층을 설계하고 전류를 조절해 시냅스의 연결 강도를 구현한다. 강유전체(외부 전기장이 없어도 전기적 분극이 남고 그 방향을 전기장으로 바꿀 수 있는 물질)를 이용한 기억 소자도 개발한다. 소자 제작 결과를 회로 배열과 스파이킹 신경망(시간에 따라 발생하는 펄스로 정보를 전달하는 신경망) 계산으로 잇는 것이 대표 논문 4–6의 공통 주제다. 대표 논문 7은 저장된 내용과 입력을 비교하는 메모리(정보를 저장하는 장치)를 심전도 이상 탐지 연산에 이용한다.[^oxide][^neuro][^p4][^p5][^p6][^p7]

### 4. 빛을 검출하고 광학 상태를 저장하는 회로

빛의 전달 경로와 검출 소자를 결합해 레이저 디스플레이와 뉴로모픽 계산에 쓰는 광학 플랫폼을 연구한다. 대표 논문 8은 하프늄·지르코늄 산화물의 결정 구조와 변형 상태가 굴절률에 미치는 영향을 분석해, 전압으로 설정한 광학 상태가 남는 이유를 설명한다.[^photonics][^p8]

## 대표 논문

교수가 서울대학교 소속 교신저자로 확인되는 논문 가운데 화소·보상 회로, 뉴로모픽 소자·시스템, 광집적회로를 고르게 골랐다. 연도는 출판사의 온라인 공개 연도이며, 아래의 '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2025 | [Oxide TFT-Based Micro-LED Pixel Circuit With Piecewise Linear Sweep Slope Signal for Improved Low Gray-Level Expression](https://doi.org/10.1002/jsid.2110) | 밝기 구간에 따라 기울기가 다른 구동 신호를 사용하고 발광 시간을 구간별로 나누는 화소 회로를 제안했다. 어두운 밝기의 표현을 개선하고 신호 전환으로 생기는 왜곡을 막는 동작을 회로 계산으로 검증했다.[^p1] |
| 2 | 2026 | [Subthreshold Swing Control in IGZO TFTs Using Floating-Gate Engineering for AMOLED Displays](https://doi.org/10.1002/jsid.70054) | 주변과 전기적으로 절연된 저장 전극의 폭과 겹침 구조를 바꾸어 전류 조절 특성을 조정했다. 실험과 소자 계산으로 구조 설계와 전류 특성의 관계를 확인하고, 어두운 화면의 밝기를 균일하게 제어하는 소자 구조를 제안했다.[^p2] |
| 3 | 2024 | [A Mura model-based optical compensation for organic light-emitting diode display luminance nonuniformity utilizing two image capturing](https://doi.org/10.1002/jsid.2017) | 화소 제작 편차로 생기는 화면 밝기의 불균일을 수학 모형으로 나타내고, 두 번의 촬영으로 여러 밝기 단계의 보상값을 구하는 알고리즘을 제안했다. 계산과 실험으로 보상 효과를 검증했다.[^p3] |
| 4 | 2023 | [Synaptic Transistor Based on In-Ga-Zn-O Channel and Trap Layers with Highly Linear Conductance Modulation for Neuromorphic Computing](https://doi.org/10.1002/aelm.202201306) | 전류가 흐르는 층과 전하를 저장하는 층에 IGZO를 사용했다. 저장층의 상태를 조절해 전하를 빼내는 효율과 시냅스 연결 강도 조절을 개선하고, 신경망 계산에서의 가능성을 보였다.[^p4] |
| 5 | 2026 | [Low-Voltage Operation of IGZO Memtransistors Enabled by Coupling Enhancement Through 2T Drain-Driven Operation for Neuromorphic Computing](https://doi.org/10.1002/aisy.70508) | 두 단자로 구동하는 메모리형 IGZO 트랜지스터를 제안하고, 전극 사이 전기적 결합을 강화해 동작 전압을 낮췄다. 소자 배열을 제작했으며 실제 소자의 이상적이지 않은 특성을 반영한 신경망 계산으로 영상 분류를 평가했다.[^p5] |
| 6 | 2026 | [A Neuromorphic Simulation Framework for Indium-Gallium-Zinc-Oxide Charge-Trap Synaptic Transistors: From Device Modeling to System Simulation](https://doi.org/10.1002/aisy.70374) | 제작한 시냅스 소자의 동작을 회로 모형으로 만든 뒤, 배열 안의 저항과 정전용량(전압에 따라 저장되는 전하의 양을 나타내는 값)에 의한 영향을 반영하고 신경망 계산까지 연결했다. 소자만 따로 평가할 때와 시스템 수준 평가 사이의 간격을 다루는 연구다.[^p6] |
| 7 | 2026 | [Ultralow-Power Floating-Gate InGaZnO Content-Addressable Memory for Wearable Electrocardiogram Anomaly Detection](https://doi.org/10.1002/aisy.70474) | 심장의 전기 활동을 기록한 심전도에서 이상을 찾는 메모리 연산 하드웨어를 제안했다. 전극 면적의 설계로 소자 특성을 조절하고, 정보를 계속 옮기는 대신 저장 장치 안에서 비교 연산을 수행해 에너지 사용을 줄이는 방식을 평가했다.[^p7] |
| 8 | 2026 | [Crystallographic Analysis of a Nonvolatile HZO Phase Shifter Integrated on a Si3N4 Waveguide](https://doi.org/10.1002/aelm.202500765) | 질화규소 도파관에 하프늄·지르코늄 산화물을 결합했다. 전압을 없앤 뒤에도 남는 결정 구조의 비중과 변형을 측정하고 계산해, 광학 응답이 바뀐 상태로 유지되는 이유를 설명했다.[^p8] |

## 교수와 전문 분야

이수연 교수는 서울대학교에서 전기공학 학사(2004–2009)와 박사(2009–2013)를 마쳤고, 2013–2019년 삼성디스플레이 책임연구원으로 일했다. 2019년 서울대학교에 부임했으며, 연구실 소개는 2019–2023년 조교수, 2023년부터 부교수로 적는다. 2025–2026년에는 도쿄대학교 첨단과학기술연구센터 방문연구원으로도 적혀 있다.[^people][^professor]

전문 분야는 산화물 소자의 동작과 구조를 이해하고, 이를 실제 회로와 시스템 설계에 연결하는 일이다. 학부 소개는 산화물 박막 소자와 디스플레이 보상회로를 관심 분야로 적는다. 최근 연구는 소자의 구조를 이용한 전류 제어, 신경망 연결 강도를 저장하는 소자와 연산 하드웨어, 광학 상태를 저장하는 부품으로 이어진다.[^professor][^p2][^p4][^p6][^p7][^p8]

## 응용 분야

OLED·마이크로 LED 화면과 실리콘 기반 초소형 디스플레이, 산화물 기반 영상 센서, 신경계의 정보 처리를 본뜬 계산 시스템, 레이저를 이용하는 디스플레이와 스마트 안경이 연구 소개의 응용 대상이다.[^pixel][^oxide][^photonics] 대표 논문 7은 웨어러블 심전도 감시를 위한 이상 탐지 연산을 대상으로 한다.[^p7]

## 구성원

2026년 10월 26일 People 페이지의 교수 외 구성원 26명이다. 과정과 연구 주제는 게시 표기를 옮겼다. '대표 논문 참여'는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 안수빈 (Soobin An) | 박사후연구원 | Device modeling & simulation | soobin.an@snu.ac.kr | 4 |
| 공민식 (Minsik Kong) | 박사후연구원 | Waveguide photonics, Device physics | mskong.kong@snu.ac.kr | 8 |
| 박찬진 (Chanjin Park) | 박사과정 | Pixel circuit design & simulation | chanjinpark97@snu.ac.kr | 1, 3 |
| 신승윤 (Seung Yoon Shin) | 박사과정 | Neuromorphic, Ferroelectric | ssy071700@snu.ac.kr |  |
| 이지호 (Ji-Ho Lee) | 박사과정 | In-sensor computing, Device physics, Neuromorphic | jiholee1229@snu.ac.kr |  |
| 김재범 (Jaybum Kim) | 박사과정 | Pixel circuit design & simulation | jaybum@snu.ac.kr | 1, 2 |
| 양기영 (Key-Young Yang) | 박사과정 | Pixel/GIP circuit design & simulation | young924@snu.ac.kr |  |
| 윤유민 (Yumin Yun) | 박사과정 (Lab Manager) | Neuron circuit design & simulation, Synaptic transistor, Device physics | dbals2822@snu.ac.kr | 2, 5, 6, 7 |
| 김민지 (Minji Kim) | 박사과정 (Lab Manager) | Pixel circuit design & simulation | spongelove2000@snu.ac.kr | 1 |
| 김성은 (Seong Eun Kim) | 박사과정 | Stretchable electronics, Sensor Systems, Waveguide Photonics | kimseongeun@snu.ac.kr |  |
| 배선열 (Sunyeol Bae) | 박사과정 | Oxide Semiconductor Memory Devices, Neuromorphic Hardware, Pixel Circuits | sun010421@snu.ac.kr | 2, 5, 6, 7 |
| 강민 (Min Kang) | 박사과정 | Waveguide photonics, Device physics | km1785@snu.ac.kr | 8 |
| 박채환 (Chae-Hwan Park) | 박사과정 | Neuromorphic system, Synaptic transistor | ordlike@snu.ac.kr | 2, 5, 6 |
| 천새루 (Saeru Cheon) | 박사과정 | Pixel circuit design & simulation | tofn0924@snu.ac.kr |  |
| 고진원 (Jinwon Go) | 박사과정 | Device physics | gojinwon@snu.ac.kr |  |
| 정문석 (Moon Seok Jung) | 박사과정 | Pixel/GIP circuit design & simulation | ms_jung@snu.ac.kr |  |
| 정찬우 (Chan Woo Jeong) | 박사과정 | Device physics | ads0704@snu.ac.kr | 8 |
| 이동현 (Dong Hyeon Lee) | 석사과정 | Device physics | geronimo6@snu.ac.kr | 5, 6 |
| 김수빈 (Subin Kim) | 석사과정 | Pixel/GIP Circuit design & simulation | subinkim7@snu.ac.kr |  |
| 이주수 (Jusu Lee) | 석사과정 | Stretchable electronics, Device physics | jusu.lee@snu.ac.kr |  |
| 공병업 (Byeongup Gong) | 석사과정 | Device physics | byeongup.gong@snu.ac.kr |  |
| 백준영 (Junyoung Baek) | 석사과정 | Device physics | bjy8692@snu.ac.kr |  |
| 이홍 (Hong lee) | 석사과정 | Pixel circuit design & simulation | hongcode@snu.ac.kr |  |
| 김재진 (Jaejin Kim) | 석사과정 | Device physics | kimjaejin524@snu.ac.kr |  |
| 이지수 (Jisoo Lee) | 석사과정 | Pixel circuit design & simulation | pixelcraft@snu.ac.kr |  |
| 김나영 (Nayoung Kim) | 석사과정 | Pixel circuit design & simulation | nkim1678@snu.ac.kr |  |

## 졸업생과 이전 구성원

People 페이지 Alumni의 11명이다. 학위·과정과 연도는 랩의 게시 표기이고, 일부 재적 기간은 교수의 2019년 서울대 부임 전부터 시작한다. 박사후연구원 이력을 포함한 목록이다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 노형준 (Hyungjun Noh) | Ph.D. (20 25-2026) | Samsung Electronics |
| 박준형 (Junhyeong Park) | Integrated M.S/Ph.D. and Post-Doc Researchers (2020-2026) | Samsung Electronics |
| 박지환 (Ji-Hwan Park) | Integrated M.S/Ph.D. (20 20-202 6) | Samsung Electronics |
| 강경수 (Kyeong-Soo Kang) | Integrated M.S/Ph.D. and Post-Doc Researchers (2018-2026) |  |
| 최현진 (Hyunjin Choi) | M.S. (2023-2026) | SK hynix |
| 강현구 (Hyeon Gu Kang) | M.S. (2024-2026) | SK hynix |
| 이진규 (Jinkyu Lee) | Integrated M.S/Ph.D. (2019-2025) | Samsung Electronics |
| 조성인 (Seong-In Cho) | Post-Doc Researchers (2024-2025) | Samsung Electronics |
| 장유성 (Yuseong Jang) | Ph.D. (2020-2025) | Samsung Electronics |
| 목진성 (Ji nsung Mok) | M.S. (2 022-202 4) | Ph.D. in Seoul National University |
| 강 지민 (Jimin Kang) | M.S. (2021-2023) | Ph.D. in Stanford University |

## 최근 논문·학회 발표 목록 (2021–2026)

학술지 논문 44편과 학회 발표 87건이다. 연도는 랩 목록의 연도 구역이며, 학회 발표는 개최지·월·발표 방식까지 랩 표기를 따른다. 2021년은 해당 연도 구역 전체를 포함한다. 학술지 논문 목록에는 산화물 소자·화소 회로·뉴로모픽 계산·광학 소자의 연구가, 학회 목록에는 신축성 표시장치와 소자·회로의 설계·분석 발표가 함께 실려 있다.[^journals][^conference]

**2026**

- Jaybum Kim, Chanjin Park, Minji Kim, Saeru Cheon, Subin Kim, and Soo-Yeon Lee. "A Micro-LED PWM Pixel Circuit Achieving Stable Ultra-Low-Gray Expression Through Drain-Reservoir Feedback". *Journal of Information Display, vol. 27, no. 4, pp. 24, 2026*.
- Minsik Kong, Seong Eun Kim, Kyuho Kim, Namkyoo Park, Sunkyu Yu, and Soo-Yeon Lee. "Monolithically Integrated IGZO Synaptic Transistors on a Silicon Nitride Waveguide for Optoelectronic Neuromorphic Computing". *ACS Photonics, vol. 13, no. 18, pp.5358-5369, 2026*.
- Minsik Kong, Min Kang, Byeongup Gong, and Soo-Yeon Lee. "Color-Selective IGZO/ZnON Phototransistors Enabled by Glass-Integrated Inorganic Fabry-Pérot Filters". *Optical Materials Express, vol. 16, 8, pp. 2441-2452, 2026*.
- Junhyeong Park, Sunyeol Bae, Yumin Yun, Chae-Hwan Park, Donghyeon Lee, and Soo-Yeon Lee. "Low-Voltage Operation of IGZO Memtransistors Enabled by Coupling Enhancement through 2T Drain-Driven Operation for Neuromorphic Computing". *Advanced Intelligent Systems, e70508, 2026*.
- Sunyeol Bae, Hyung-Jun Noh, Yumin Yun, Chae-Hwan Park, Junhyeong Park, and Soo-Yeon Lee. "Floating-Gate IGZO Thin-Film Transistor Employing Split-Gate to Enable Tunable Subthreshold Swing for AMOLED Pixel Circuits". *IEEE Transactions on Electron Devices, vol. 73, no.9, pp. 5715-5721, 2026*.
- Hyung-jun Noh, Sunyeol Bae, Yumin Yun, Junhyeong Park, and Soo-Yeon Lee. "Ultra-Low-Power Floating-Gate InGaZnO Content-Addressable Memory for Wearable Electrocardiogram Anomaly Detection". *Advanced Intelligent Systems, e70474, 2026*.
- Minsik Kong, Min Kang, Chanwoo Jeong, Kyuho Kim, Sunkyu Yu, and Soo-Yeon Lee. "Crystallographic Analysis of a Nonvolatile HZO Phase Shifter Integrated on a Si3N4 Waveguide". *Advanced Electronic Materials, vol. 12, no. 11, 2026*.
- Moonseok Jung, Key Young Yang, Ji-Hwan Park, SangHee Yu, Heung-Lyul Cho, Youngseok Choi, Soo-Yeon Lee. "A PWM Scan Driver Supporting RegionSelective Masking for Depletion-Mode a-IGZO TFTs". *IEEE Electron Device Letters, vol. 47, 7, pp.1418-1421, 2026*.
- Sunyeol Bae, Junhyeong Park, Hyung-Jun Noh, Jaybum Kim, Yumin Yun, Chae-Hwan Park, and Soo-Yeon Lee. "Subthreshold Swing Control in IGZO TFTs Using Floating-Gate Engineering for AMOLED Displays". *Journal of the Society for Information Display, vol. 34, no. 5, pp. 214-223, 2026*.
- Yumin Yun, Junh.yeong Park, Sunyeol Bae, Chae-Hwan Park, Dong Hyeon Lee, and Soo-Yeon Lee. "A Neuromorphic Simulation Framework for IGZO Charge-Trap Synaptic Transistors: From Device Modeling to System Simulation". *Advanced Intelligent Systems, vol. 8, no.7, 2026*.
- Hyeon-Gu Kang, Minji Kim, Key Young Yang, Kyeong-Soo Kang, and Soo-Yeon Lee. "A Stable Pixel Circuit with Constant Current Compensation for Threshold Voltage, Mobility, and Subthreshold Swing Variations". *Journal of Information Display, vol. 27, 2, pp.1-11, 2026*.
- Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, Key Young Yang, Moonseok Jung, and Soo-Yeon Lee. "An a-IGZO TFT-Based AMOLED Pixel Circuit for Highly Stable Driving Current under Pico-Ampere-Range Current Region". *Journal of Information Display, vol. 27, 5, pp.1-8, 2026*.
- Yumin Yun, Junhyeong Park, Minsik Kong, Ji-Ho Lee, Sunyeol Bae, Chanjin Park, and Soo-Yeon Lee. "Optoelectronic Neuromorphic System Based on Amorphous Indium-Gallium-Zinc-Oxide Thin-Film Transistor for Spiking Neural Networks". *Advanced Intelligent Systems, vol. 8, 1, 202 6*.
- Heejae Roh, Saeru Cheon, Siyuan Liu, Yuanyuan Zhou, Soo-yeon Lee, Naoji Matsuhisa. "A stretchable OLED Display with Touch Sensing Function". *The 16th International Conference on Flexible and Printed Electronics (ICPFE 2026), Korea, Jeju, August 2026 (Poster)*.
- Jaybum Kim, Ji-Hwan Park, Chanjin Park, Saeru Cheon, Subin Kim, and Soo-Yeon Lee. "Oxide TFT-Based Micro-LED Pixel Circuit with a Double-Sweep Signal for Improved Low Gray Expression". *The 26th International Meeting on Information Display 2026 (IMID 2026), Busan, Korea, August 2026 (Oral)*.
- Hyung-Jun Noh, Sunyeol Bae, Jaybum Kim, and Soo-Yeon Lee. "Area-Engineered IGZO Floating-Gate TFTs with Enhanced Subthreshold Swing for High-Resolution AMOLED Displays". *The 26th International Meeting on Information Display 2026 (IMID 2026), Busan, Korea, August 2026 (Poster)*.
- Ji-Ho Lee, Junhyeong Park, Seungyoon Shin, Min Kang, Chan Woo Jeong, Byeongup Gong, Minsik Kong, Soobin An and Soo-Yeon Lee. "Visible-Light Photoresponse of an a-IGZO-based MISM Photodiode". *The 26th International Meeting on Information Display 2026 (IMID 2026), Busan, Korea, August 2026 (Poster)*.
- Sunyeol Bae, Junhyeong Park, Chae-Hwan Park, Seong Eun Kim, Yumin Yun, Jusu Lee, Minji Kim, Donghyeon Lee, and Soo-Yeon Lee. "Effect of Source Voltage Variation on Source-Overlapped Floating-Gate IGZO TFTs for AMOLED Pixel Circuits". *The 26th International Meeting on Information Display 2026 (IMID 2026), Busan, Korea, August 2026 (Oral)*.
- Sunyeol Bae, Junhyeong Park, Hyung-Jun Noh, Yumin Yun, Chae-Hwan Park,  and Soo-Yeon Lee. "Subthreshold Swing Control in IGZO TFTs Using Floating-Gate Engineering for AMOLED Displays". *SID Display Week 2026, Los Angeles, USA, May 2026 (Oral)*.
- Subin Kim, Jaybum Kim, Kyeong-Soo Kang, Chanjin Park, and Soo-Yeon Lee. "Oxide-based Micro-LED Pixel Circuit Employing a Nonlinear Ramp Sweep Generator for Enhanced Low Gray-Level Resolution". *SID Display Week 2026, Los Angeles, USA, May 2026 (Oral)*.
- Jaybum Kim, Ji-Hwan Park, Chanjin Park, Saeru Cheon, Subin Kim, and Soo-Yeon Lee. "LTPO TFT-Based Micro-LED PWM Pixel Circuit with Compact Feedback and VTH Compensation for Enhanced Low-Gray Expression". *SID Display Week 2026, Los Angeles, USA, May 2026 (Oral)*.
- Yumin Yun, Junhyeong Park, Sunyeol Bae, Chanjin Park, and Soo-Yeon Lee. "Hybrid a-IGZO/Si Current Mirror: Heterogeneous Integration and Electrical Performance". *SID Display Week 202 6, Los Angeles, USA, May 202 6 (Oral)*.
- Soobin An, Seong Eun Kim, Minji Kim, Hyunjin Choi, and Soo-Yeon Lee. "Design Strategies for Stretchable Displays Based on the Island-Bridge Architecture". *Materials Research Society (MRS 2026 Spring), Honolulu, Hawaii, April 2026 (Invited)*.
- Seungyoon Shin, Jinkyu Lee, Sunyeol Bae, Hyunjin Choi, Yumin Yun, and Soo-Yeon Lee. "Functional Al2O3 Interfaces for Contact Improvement and Plasma Damage Protection in IGZO TFTs". *International Conference on Display Technology (ICDT 2026), Chongqing, China, April 2026 (Invited)*.
- Sunyeol Bae, Junhyeong Park, Yumin Yun, Donghyeon Lee, Ji-Ho Lee, and Soo-Yeon Lee. "Minimizing Device-to-Device Variation in IGZO Floating-Gate Synaptic Transistors via Source/Drain Contact Structure Modification". *The 33rd Korean Conference on Semiconductors (KCS 2026), Jeongseon, Korea, January 2026 (Poster)*.
- Chae-Hwan Park, Seung Yoon Shin, Seong Eun Kim, Min Kang, and Soo-Yeon Lee. "A Schmitt-Trigger Comperator-Based Noise-Robust Reconfigurable Leaky Integrate-and-Fire Neuron Circuit for Spiking Neural Networks". *The 33rd Korean Conference on Semiconductors (KCS 2026), Jeongseon, Korea, January 2026 (Poster)*.
- Chanjin Park, and Soo-Yeon Lee. "Gate- and Body-driven OLEDoS Pixel Circuit for a Wide Data Range". *The 33rd Korean Conference on Semiconductors (KCS 2026), Jeongseon, Korea, January 2026 (Poster)*.
- Seong Eun Kim, Ji-Ho Lee, Donghyeon Lee, Soobin An, and Soo-Yeon Lee. "Stress Analysis of a IGZO TFTs with Various Device Architectures for Stretchable Backplanes Using Rigid-Island Structures". *The 3 3r d Korean Conference on Semiconductors (KCS 202 6), Jeongseon, Korea, January 202 6 (Poster)*.
- Donghyeon Lee, Chanji n Park, Chan Woo Jeong, and Soo-Yeon Lee. "Analysis of Driving TFT Degradation Behavior under AC Stress Emulating Circuit Operating Conditions". *The 2nd Korean Meeting on Information Display (KMiD 2026), Gangneung, Korea, January 2026 (Poster)*.
- Chan Woo Jeong, Dong hyeon Lee, and Soo-Yeon Lee. "Stretched Exponential 함수 기반 a-IGZO TFT의 AC 스트레스 열화 모델링". *The 2nd Korean Meeting on Information Display (KMiD 2026), Gangneung, Korea, January 2026 (Oral)*.
- Seong Eun Kim, Soobin An, Chan Woo Jeong, and Soo-Yeon Lee. "A Simulation Study on the Effect of PI-Island Thickness and Mesh-type Electrodes on Mechanical Robustness of Stretchable Devices". *The 2nd Korean Meeting on Information Display (KMiD 202 6), Gangneung, Korea, January 202 6 (Oral)*.

**2025**

- Seungyoon Shin, Jinkyu Lee, Hyunjin Choi, Seong-In Cho, Sunyeol Bae, and Soo-Yeon Lee. "Suppression of Interface Damage in IGZO TFTs Using Al 2 O 3 Protective Layer During N 2 O Plasma Treatment". *Applied Surface Science, 718, 164912, 2025*.
- Yuseong Jang, Junhyeong Park, Seungyoon Shin, Soobin An, and Soo-Yeon Lee. "Multilevel Non−volatile Ferroelectric Diode Employing HfZrOx and Metal Oxynitride Semiconductor for Neuromorphic Computing". *ACS Materials Letters, 7, 3800−3807, 2025*.
- Jaybum Kim, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, Minji Kim and Soo-Yeon Lee. "Oxide TFT-Based Micro-LED Pixel Circuit with Piecewise Linear Sweep Slope Signal for Improved Low Gray-Level Expression". *Journal of the Society for Information Display, pp. 1-8, 2025*.
- Chanjin Park, Kyeong-Soo Kang, Ji-Hwan Park, Minji Kim and Soo-Yeon Lee. "High Resolution a-IGZO TFT-based AMOLED Pixel Circuit Enabling Multiple OLED Driving via Field Sequential Color Method". *Journal of Information Display, pp.1-9, 2025*.
- JinKyu Lee, Sunyeol Bae, Seungyoon Shin, and Soo-Yeon Lee. "Mitigating Electrical Degradation in Ultra-Thin IGZO TFTs through Contact Engineering with Al 2 O 3 Interlayer". *Applied Surface Science Advances, 29, 100827, 2025*.
- Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, Hee-Ok Kim, Jong-Heon Yang, Jae-Eun Pi, Yong-Duck Kim, Chun-Won Byun, and Soo-Yeon Lee. "Oxide TFT-Based Micro Light-Emitting Diode Pixel Circuit for Improving Low Gray-Level Expression by Employing Sweep Generators". *IEEE Transactions on Electron Devices, vol. 72, no. 7, pp. 3707-3711, 2025*.
- Kyeong-Soo Kang, Ji-Hwan Park, Chan j in Park, Ji-Ho Lee, and Soo-Yeon Lee. "Inverter-Based MicroLED Pixel Circuit Using LTPO TFTs Achieving Submicrosecond Pulse-Width Modulation With Low Power Consumption Through Dynamic SWEEP Generation". *IEEE Access, vol. 13, pp. 65348-65355, 2025*.
- Junhyeong Park, Yumin Yun, Sunyeol Bae, Yuseong Jang, Seungyoon Shin, and Soo-Yeon Lee. "High-Performance Synapse Arrays for Neuromorphic Computing via Floating Gate-Engineered IGZO Synaptic Transistors". *Advanced Science, 12, 2500568, 2025*.
- Soobin An, Junhyeong Park, Jin Kyu Lee, Kyeong-Soo Kang, Ji-Hwan Park, Yuseong Jang, and Soo-Yeon Lee. "Extraction of Subgap Density of States in Amorphous In–Ga–Zn–O Thin-Film Transistors by Measuring Capacitor-on-Gate Structure". *IEEE Transactions on Electron Devices, vol.72, no.4, 2025*.
- Seong-In Cho, Soobin An, and Soo-Yeon Lee. "Analysis of Channel Length-Dependent Degradation of IGZO TFTs under Positive Bias Stress through TCAD Simulation". *Journal of Information Display, pp.1-9, 2025*.
- Junhyeong Park, Yumin Yun, Sunyeol Bae, Chae-Hwan Park and Soo-Yeon Lee. "High-Performance IGZO Synaptic Transistors via Floating-Gate Engineering for Neouromorphic Applications". *The 32nd International Display Workshops (IDW 2025), Hiroshima, Japan, December 2025 (Invited)*.
- Junhyeong Park, Yumin Yun, Sunyeol Bae, Chae-Hwan Park and Soo-Yeon Lee. "High-Performance IGZO Synaptic Transistors Using Metal Oxide Floating Gates for Neuromorphic Applications". *32nd International Conference on Neural Information Processing (ICONIP 2025), Okinawa, Japan, November 2025 (Invited)*.
- Min Kang, Minsik Kong and Soo-Yeon Lee. "Indium Tin Oxide-based Transparent Electrode Memristor for Integrated Photonic Phase Modulation on Silicon Nitride Platforms". *The 86th Japan Society of Applied Physics(JSAP) Autumn Meeting 2025, Nagoya, Japan, September 2025 (Oral)*.
- Hyunjin Choi, Soobin An, Seong Eun Kim, and Soo-Yeon Lee. "Fully Transparent and Stretchable a-IGZO Thin-Film Transistor With Polyimide Island Structure for Deformable Electronics". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Poster)*.
- Jaebeen Lee, Soobin An, Ji-Ho Lee, Chanjin Park, Jaybum Kim and Soo-Yeon Lee. "Suppression of Photo Leakage Current Using Anode Extension in OLEDoS". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Poster)*.
- Moonseok Jung and Soo-Yeon Lee. "a-IGZO TFT-Based Region-Selective Masking Scan Driver for Long Pulse Width". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Poster)*.
- Saeru Cheon, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "Diode-connected TFTs for Suppressing Crosstalk Effect in SWEEP Generation Circuit for MicroLED Displays". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Poster)*.
- Minji Kim, Chanjin Park, and Soo-Yeon Lee. "A Robust a-IGZO TFT based AMOLED Pixel Circuit under VTH, Subthreshold Swing and Mobility Variations". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Oral)*.
- Ji-Hwan Park, Kyeong-Soo Kang, Saeru Cheon, and Soo-Yeon Lee. "A New Amorphous Indium-Gallium Zinc Oxide Thin-Film Transistor MicroLED Pixel Circuit for Constant and Uniform Driving Current". *The 25th International Meeting on Information Display 2025 (IMID 2025), Busan, Korea, August 2025 (Poster)*.
- Yumin Yun, Chanjin Park, Junhyeong Park, and Soo-Yeon Lee. "A Low Power Integrate-and-Fire Neuron Circuit Using an a-IGZO-Based Thin-Film Transistor with an Inverter Transition Point Programming Method". *IEEE International Symposium on Circuits and Systems (IEEE ISCAS 2025), London, UK, May 2025 (Poster)*.
- Chae-Hwan Park, Jaybum Kim, Kyeong-Soo Kang, Hyeon-Gu Kang, and Soo-Yeon Lee. "Micro-LED Pixel Circuit with A Novel NMOS-Oxide TFT Inverter for Reducing Falling Time and Enhancing Gray-Level Expression". *SID Display Week 2025, San Jose, USA, May 2025 (Poster)*.
- Chanjin Park, Kyeong-Soo Kang, Yumin Yun, Saeru Cheon, and Soo-Yeon Lee. "4105-PPI LEDoS Pixel Circuit With an Analog Pulse-Width-Modulation Driving Method Employing a Dual-Sweep Signal for Wider Data Range". *SID Display Week 2025, San Jose, USA, May 2025 (Oral)*.
- Junhyeong Park, Yumin Yun, Sunyeol Bae, Chae-Hwan Park, and Soo-Yeon Lee. "IGZO-Based Synaptic Transistors for Neuromorphic Applications". *SID Display Week 2025, San Jose, USA, May 2025 (Invited)*.
- Seongyoon Shin, Jin Kyu Lee, Hyunjin Choi, Seong-In Cho, and Soo-Yeon Lee. "Insertion of Protective Layer for Enhancing Effect of N2O Plasma Treatment on NBS Stability in IGZO TFTs". *The 32nd Korean Conference on Semiconductors (KCS 2025), Jeongseon, Korea, February 2025 (Oral)*.
- Sunyeol Bae, Junhyeong Park, Yumin Yun, and Soo-Yeon Lee. "Design Strategy of IGZO Flash Memory Device for Low Voltage Operation". *The 32nd Korean Conference on Semiconductors (KCS 2025), Jeongseon, Korea, February 2025 (Poster)*.
- Seong-In Cho, Soobin An, and Soo-Yeon Lee. "Study of Positive Bias Stress Stability in Short Channel Oxide Thin-Film Transistors based on TCAD Simulation". *The 32nd Korean Conference on Semiconductors (KCS 2025), Jeongseon, Korea, February 2025 (Poster)*.
- Chae-Hwan Park, Soobin An, Seungyoon Shin, Ji-Ho Lee, Hyeonjun Choi, and Soo-Yeon Lee. "고성능 디스플레이 화소 회로 설계를 위한 TFT 인버터 특성 비교". *The 1st Korean Meeting on Information Display (KMiD 2025), Gangneung, Korea, January 2025 (Poster)*.
- Min Kang, Minsik Kong, Seong Eun Kim, Seong-In Cho, Jin Kyu Lee, Sunyeol Bae, and Soo-Yeon Lee. "Optimization of Optical Properties of Indium Tin Oxide Thin Films Depending on Annealing Temperature and Their Application in Waveguides". *The 1st Korean Meeting on Information Display (KMiD 2025), Gangneung, Korea, January 2025 (Poster)*.
- Chanjin Park, Yumin Yun, Saeru Cheon, Junhyeong Park, Yuseong Jang, and Soo-Yeon Lee. "Analog Pulse-Width-Modulation 방식의 CMOS 기반 µLED 화소 회로". *The 1st Korean Meeting on Information Display (KMiD 2025), Gangneung, Korea, January 2025 (Oral)*.
- Minji Kim, Kyeong-Soo Kang, Ji-Hwan Park, Hyeon-Gu Kang, and Soo-Yeon Lee. "구동 트랜지스터의 문턱전압이하스윙 및 문턱전압 산포 보상이 가능한 a-IGZO TFT 기반의 AMOLED 화소회로". *The 1st Korean Meeting on Information Display (KMiD 2025), Gangneung, Korea, January 2025 (Oral)*.

**2024**

- Hyuckwon Kwon, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "A Mura model-based optical compensation for organic light-emitting diode display luminance nonuniformity utilizing two image capturing". *Journal of the Society for Information Display, vol.33, pp.24-33, 2024*.
- Kyeong-Soo Kang, Hee-Ok Kim, Jong-Heon Yang, Jae-Eun Pi, Yong-Duck Kim, Chun-Won Byun, Ji-Hwan Park, Chanjin Park, Minji Kim, Yumin Yun, and Soo-Yeon Lee. "Depletion-Mode Oxide TFT-Based MicroLED Pixel Circuit for High-Current Pulsewidth Modulation With Low Driving Voltage". *IEEE Transactions on Electron Devices, vol.71, no. 11, pp.6820-6825, 2024*.
- Chanjin Park, Hee-Ok Kim, Jong-Heon Yang, Jae-Eun Pi, Yong-Duck Kim, Chun-Won Byun, Kyeong-Soo Kang, J i-Hwan Park, Minji Kim, Hyoungsik Nam, and Soo-Yeon Lee. "Highly Uniform Low Gray AMOLED Pixel using Stable Circuit and Duty Ratio Modulation Driving". *IEEE Journal of the Electron Devices Society, vol. 12, pp.668-676, 2024*.
- Kyeongwoo Jang, Yuseong Jang, Soobin An, and Soo-Yeon Lee. "In-situ IGZO/ITON Heterostructure Phototransistor to Enhance Visible Light Detection". *IEEE Electron Device Letters, vol.45, no. 10, pp.1839-1842, 2024*.
- Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, and Soo-Yeon Lee. "A New 13T4C LTPO MicroLED Pixel Circuit Producing Highly Stable Driving Current by Minimizing Effect of Parasitic Capacitors and Stabilizing Capacitor Nodes". *IEEE Journal of the Electron Devices Society, vol. 12, pp. 472-478, 2024*.
- Geun Woo Baek, Yeon Jun Kim, Jaekwon Kim, Jun Hyuk Chang, Uhjin Kim, Soobin An, Junhyeong Park, Sunkyu Yu, Wan Ki Bae, Jaehoon Lim, Soo-Yeon Lee, and Jeonghun Kwak. "Memristive Switching Mechanism in Colloidal InP/ZnSe/ZnS Quantum Dot-Based Synaptic Devices for Neuromorphic Computing". *Nano Letters, vol. 24, no. 19, pp. 5855-5861, 2024*.
- Junhyeong Park, Yumin Yun, Minji Kim, and Soo-Yeon Lee. "Simulation and Optimization of IGZO-Based Neuromorphic System for Spiking Neural Networks". *IEEE Journal of the Electron Devices Society, vol. 12, pp.228-235, 2024*.
- Jaybum Kim, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, Minji Kim and Soo-Yeon Lee. "Oxide TFT-Based Micro-LED Pixel Circuit Enhancing Low Gray Expression Through Continuous Piecewise Linear Sweep Signal". *The 31st International Display Workshops (IDW 2024), Sapporo, Japan, December 2024 (Oral)*.
- Yuseong Jang and Soo-Yeon Lee. "Metal Oxynitride Semiconductor Prepared by Reactive Sputtering of Metal Oxide Target for Thin Film Devices". *The 31th International Display Workshops (IDW 2024), Sapporo, Japan, December 2024 (Invited)*.
- Minsik Kong and Soo-Yeon Lee. "Influence of Wet and Dry Etching on IGZO TFTs Focusing on Sidewall Conductance and Hump phenomenon". *The 31th International Display Workshops (IDW 2024), Sapporo, Japan, December 2024 (Poster)*.
- Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, and Soo-Yeon Lee. "LTPO MicroLED Pixel Circuit for Highly Stable Driving Current with 6T1C Pulse Width Control Circuit Structure". *The 31st International Display Workshops (IDW 2024), Sapporo, Japan, December 2024 (Oral)*.
- Hyeon-Gu Kang, Chanjin Park, Ji-Hwan Park, and Soo-Yeon Lee. "AMOLED Compensation Pixel Circuit with Consecutive VTH Sensing Method". *Electro-physics & Applications Society Fall Conference (KIEE 2024), Gangneung, Korea, October 2024 (Oral)*.
- Seong Eun Kim, Hyunjin Choi, Soobin An, and Soo-Yeon Lee. "Optimization of PDMS/PI Island Structure for Enhancing Durability in Stretchable TFT". *Electro-physics & Applications Society Fall Conference (KIEE 2024), Gangneung, Korea, October 2024 (Oral)*.
- Saeru Cheon, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "Compensation Algorithm for Crosstalk Effect in a Sweep Generation Circuit Using Load Capacitance Charging". *Electro-physics & Applications Society Fall Conference (KIEE 2024), Gangneung, Korea, October 2024 (Oral)*.
- Jinkyu Lee, Junhyeong Park, and Soo-Yeon Lee. "Optimization of Metal Capping Layer Design for Enhancing Mobility in IGZO TFTs". *the Pacific Rim international meeting of The Electrochemical Society (ECS PRiME 2024), Honolulu, HI, USA, October 2024 (Poster)*.
- Yumin Yun, Junhyeong Park, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "Design and Verification of an a-IGZO TFTs-based Neuron Circuit with Threshold Voltage Variation Compensation". *the Pacific Rim international meeting of The Electrochemical Society (ECS PRiME 2024), Honolulu, HI, USA, October 2024 (Oral)*.
- Ji-Ho Lee, Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, and Soo-Yeon Lee. "An a-IGZO TFT Based Pixel Circuit Suitable for Stable Operation Under AMOLED Impulsive Driving Dimming Scheme". *the Pacific Rim international meeting of The Electrochemical Society (ECS PRiME 2024), Honolulu, HI, USA, October 2024 (Oral)*.
- Junhyeong Park, Yumin Yun, Sunyeol Bae, and Soo-Yeon Lee. "IGZO-Based Neuromorphic Devices and Their Application in Spiking Neural Networks". *the Pacific Rim international meeting of The Electrochemical Society (ECS PRiME 2024), Honolulu, HI, October 2024 (Invited)*.
- Keyyoung Yang and Soo-Yeon Lee. "a-IGZO TFT Pixel Circuit Enhancing Low Gray Expression for Active-Matrix OLED Displays". *The 24th International Meeting on Information Display 2024 (IMID 2024), Jeju, Korea, August 2024 (Poster)*.
- Ji-Hwan Park, Kyeong-Soo Kang, and Soo-Yeon Lee. "Amorphous Indium-Gallium Zinc Oxide Thin-Film Transistor MicroLED Pixel Circuit with Zero-V GS Inverter for Short Falling Time". *The 24th International Meeting on Information Display 2024 (IMID 2024), Jeju, Korea, August 2024 (Poster)*.
- Sunyeol Bae, Jinkyu Lee, and Soo-Yeon Lee. "Effect of Active Layer Thickness on Contact Properties of Ultra-Thin Channel Amorphous InGaZnO Thin Film Transistor with Ti Source/Drain Electrodes". *The 24th International Meeting on Information Display 2024 (IMID 2024), Jeju, Korea, August 2024 (Oral)*.
- Chanjin Park, Kyeong-Soo Kang, Ji-Hwan Park, and Soo-Yeon Lee. "a-IGZO TFT μLED Pixel Circuit for PWM Driving and Its Color Shift with Different Duty Ratios and Current Amplitudes". *The 31th International Workshop on Active-Matrix Flatpanel Displays and Devices (AM-FPD 24), Kyoto, Japan, July 2024 (Oral)*.
- Hyeon-Gu Kang, Chanjin Park, Kyeong-Soo Kang, and Soo-Yeon Lee. "Enhancing Low Gray Level Performance in OLED Displays Using Pre-Charging Structures". *International Conference on Electro-physics & Information Technology Applications 2024 (ICEP-ITA 2024), Tashkent, Uzbekistan, June 2024 (Oral)*.
- Chae-H wan Park, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "μLED pixel circuit based on Low-Temperature Polysilicon and Oxide Thin Film Transistors for pulse width modulation with extremely short falling time". *International Conference on Electro-physics & Information Technology Applications 2024 (ICEP-ITA 2024), Tashkent, Uzbekistan, June 2024 (Oral)*.
- Sae r u Cheon, Chanjin Park, Kyeong-Soo Kang and Soo-Yeon Lee. "A Compact μLED Pixel Circuit for p-type only Low-Temperature Poly-Silicon Thin Film Transistor Backplane". *International Conference on Electro-physics & Information Technology Applications 2024 (ICEP-ITA 2024), Tashkent, Uzbekistan, June 2024 (Oral)*.
- Minji Kim, Kyeong-Soo Knag, Ji-Hwan Park, Chanjin Park and Soo-Yeon Lee. "Compact AMOLED Pixel Circuit Employing Double-Gate TFT Achieving High Threshold Voltage Compensation Accuracy". *SID Display Week, 2024, San Jose, USA, May 2024 (Poster)*.
- Seungyoon Shin, Yuseong Jang, Junhyeong Park, and Soo-Yeon Lee. "Memory Window and Endurance Improvement of In-Ga-Zn-O-Based Ferroelectric Thin Film Transistors by Inserting In-Ga-Zn-O Floating Gate". *SID Display Week, 2024, San Jose, USA, May 2024 (Poster)*.
- Soobin An, Junhyeong Park, Jinkyu Lee, Yumin Yun, and Soo-Yeon Lee. "High Subthreshold Swing a-IGZO Driving TFTs Without Mobility Degradation for Low-Gray Level Image Quality Improvement in Active-Matrix OLED". *SID Display Week 2024, San Jose, USA, May 2024 (Oral)*.

**2023**

- Kyeong-Soo Kang, Ji-Hwan Park, ChanJin Park, Ji-Ho Lee, and Soo-Yeon Lee. "A New PWM Operational Scheme for MicroLED Displays Using Inverter and Dynamic SWEEP Signal Slope for Low Gray Level Expression". *IEEE Access, vol. 11, 2023*.
- Junhyeong Park, Yuseong Jang, and Soo-Yeon Lee. "Optimization of post-annealing temperature for high-performance synaptic transistors based on In-Ga-Zn-O channel and trap layers". *AIP Advances, vol. 13, no. 12, 125314, 2023*.
- Kyeong-Soo Kang, Ji-Hwan Park, Chan J in Park, Ji-Ho Lee, and Soo-Yeon Lee. "An a-IGZO TFT Based AMOLED Pixel Circuit Employing Stable Mobility Compensation Suppressing Degradation of Detected VTH". *IEEE Journal of the Electron Devices Society, vol. 1 2, pp. 7-13, 2023*.
- Yuseong Jang, Jin Kyu Lee, Jinsung Mok, Junhyeong Park, Seung Yoon Shin, and Soo-Yeon Lee. "Suppression of redox reaction between IGZO surface and reducing agent TMA using oxidizing agent fluorine treatment". *RSC Advances, vol. 13, pp. 33269-33275, 2023*.
- Jin Kyu Lee, Soobin An and Soo-Yeon Lee. "Self-Aligned Top-Gate IGZO TFT with Stepped Structure for Suppressing Short Channel Effect". *IEEE Electron Device Letters, vol. 44, pp. 1845-1848, 2023*.
- Kyeong-Soo Kang, Ji-Hwan Park, Jimin Kang, Chanjin Park, Changwon Jeong, and Soo-Yeon Lee. "A Compact Amorphous In-Ga-Zn-Oxide Thin Film Transistor Pixel Circuit with Two Capacitors for Active Matrix Micro Light Emitting Diode Displays". *IEEE Journal of the Electron Devices Society, vol. 11, pp. 204-209, 2023*.
- Junhyeong Park, Yuseong Jang, Jin Kyu Lee, Soobin An, Jinsung Mok, and Soo-Yeon Lee. "Synaptic Transistor Based on In-Ga-Zn-O Channel and Trap Layers with Highly Linear Conductance Modulation for Neuromorphic Computing". *Advanced Electronic Materials, vol. 9, no. 6, 2201306, 2023*.
- Ji-Hwan Park, Kyeong-Soo Kang, Junhyeong Park, and Soo-Yeon Lee. "산화물 박막소자의 단기 열화 특성 분석 및 예측식 모델링". *The Transactions of the Korean Institute of Electrical Engineers, vol. 72, no. 3, pp. 402-405, 2023*.
- Yuseong Jang, and Soo-Yeon Lee. "In Situ IGZO/ZnON Phototransistor Free of Persistent Photoconductivity with Enlarged Spectral Responses". *ACS Applied Electronic Materials, vol. 5, no. 1, pp. 509-519, 2023*.
- Yuseong Jang, Seong Yoon Shin, and Soo-Yeon Lee. "Metal Oxynitride Semiconductor for Ferroelectric HfZrOx Thin Film Devices". *The 30th International Display Workshops (IDW 23), Niigata, Japan, December 2023 (Oral)*.
- Kyeong-Soo Kang, and Soo-Yeon Lee. "Oxide TFT Pixel Circuits and Various Operation Methods for PWM MicroLED Displays". *The 30th International Display Workshops (IDW 23), Niigata, Japan, December 2023 (Invited)*.
- Yumin Yun, Junhyeong Park, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "An a-IGZO TFTs Based Neuron Circuit with Threshold Voltage Variation Compensation for Artificial Neural Network". *The 30th International Display Workshops (IDW 23), Niigata, Japan, December 2023 (Oral)*.
- Minsik Kong, Jiyong Shim, and Soo-Yeon Lee. "The Effect of the In2O3 Insertion Layer on HfO2/AlOX-Based Resistive Memory Characteristics". *The 30th International Display Workshops (IDW 23), Niigata, Japan, December 2023 (Poster)*.
- Jinsung Mok, Jin Kyu Lee, Yuseong Jang, Ji Ho Lee, and Soo-Yeon Lee. "Effect of Fluorine Plasma Treatment on IGZO TFT Stability According to the Channel Oxygen Vacancy Concentration". *The 30th International Display Workshops (IDW 23), Niigata, Japan, December 2023 (Poster)*.
- Soobin An, Yumin Yun, Ji-Hwan Park, Ji-Ho Lee, Minji Kim, Seungyoon Shin, and Soo-Yeon Lee. "A Study on High Subthreshold Swing a-IGZO Driving TFTs to Enhance Low-Gray Level Image Quality in Active-Matrix OLED". *International Conference on Electrical Engineering & Computing Convergence and Applications 2023 (ICEE-CCA 2023), Tashkent, Uzbekistan, August 2023 (Poster)*.
- Chanjin Park, Kyeong-Soo Kang, Ji-Hwan Park and Soo-Yeon Lee. "Just-Noticeable-Difference applicable for wide viewing distance range and extremely low luminance". *The 23rd International Meeting on Information Display 2023 (IMID 2023), Busan, Korea, August 2023 (Poster)*.
- Junhyeong Park, Yuseong Jang, and Soo-Yeon Lee. "Effect of Annealing Temperature on In-Ga-Zn-O Charge Trap-Based Synaptic Transistor". *The 23rd International Meeting on Information Display 2023 (IMID 2023), Busan, Korea, August 2023 (Poster)*.
- Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "A New Compact Progressive Emission MicroLED Pixel Circuit with Only Three Scan Signals". *The 23rd International Meeting on Information Display 2023 (IMID 2023), Busan, Korea, August 2023 (Poster)*.
- Ji-Hwan Park, Kyeong-Soo Kang, Chanjin Park, and Soo-Yeon Lee. "A Compact a-IGZO TFT Pixel Circuit for Micro-LED Displays with Clamped-Inverter Structure". *The 2 3rd International Meeting on Information Display 202 3 (IMID 202 3), Busan, Korea, August 202 3 (Poster)*.
- Ji-Ho Lee, Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "Multiple-Threshold-Voltage-Compensation During the Dimming Period to Stabilize the OLED Luminance at Low Gray Levels". *The 30th International Workshop on Active-Matrix Flatpanel Displays and Devices (AM-FPD 23), Kyoto, Japan, July 2023 (Oral)*.
- Soobin An, Chanjin Park, Yumin Yun, Ji-Hwan Park, Tae-Hyoung Moon, Jiyong Noh, Kwon-Shik Park, Yong-Sang Kim, and Soo-Yeon Lee. "High Subthreshold Swing a-IGZO Driving TFTs for Low-Gray Level Uniformity in Active-Matrix OLED". *The 30th International Workshop on Active-Matrix Flatpanel Displays and Devices (AM-FPD 23), Kyoto, Japan, July 2023 (Poster)*.
- Ji-Hwan Park, Kyeong-Soo Kang, Jiho Lee, and Soo-Yeon Lee. "New a-IGZO TFT Pixel Circuit for High-Resolution Mobile AMOLED Display for Good Optical Uniformity at Low Gray Levels". *SID Display Week 2023, Los Angeles, USA, May 2023 (Oral)*.
- Chanjin Park, Kyeong-Soo Kang, Ji-Hwan Park, and Soo-Yeon Lee. "Novel a-IGZO TFT Micro-LED Circuit with Improved Stability and Area Efficiency". *SID Display Week 2023, Los Angeles, USA, May 2023 (Oral)*.
- Kyeong-Soo Kang, Ji-Hwan Park, Chanjin Park, and Soo-Yeon Lee. "A New Line-by-Line SWEEP Signal Generation Method for PWM Driving MicroLED TFT Pixel Circuit". *SID Display Week 2023, Los Angeles, USA, May 2023 (Oral)*.
- Junhyeong Park, Yuseong Jang, Jinkyu Lee, and Soo-Yeon Lee. "In-Ga-Zn-O Synaptic Transistor with 1 μm Channel Length for Neuromorphic Computing". *SID Display Week 202 3, Los Angeles, USA, May 2023 (Oral)*.

**2022**

- Yuseong Jang, Junhyeong Park, Jimin Kang, and Soo-Yeon Lee. "Amorphous InGaZnO (a-IGZO) Synaptic Transistor for Neuromorphic Computing". *ACS Applied Electronic Materials, vol. 4, no. 4, pp. 1427-1448, 2022*.
- Changwon Jeong, Jimin Kang, Kyeong-Soo Kang, Ji-Hwan Park, Soobin An, Chanjin Park, and Soo-Yeon Lee. "Oxide-Based Pixel Circuit for PWM Driving Micro-LED Displays Employing Double-Gate Structure TFT". *The 29th International Display Workshops (IDW 22), Fukuoka, Japan, Dec 2022 (Poster)*.
- Minsik Kong, Soobin An, Chanjin Park, and Soo-Yeon Lee. "Enhancement of Field Effect Mobility of RF-sputtered In 2 O 3 Thin Film Transistor by Titanium Floating Metal". *The 29th International Display Workshops (IDW 22), Fukuoka, Japan, Dec 2022 (Poster)*.
- Jinkyu Lee, Yuseong Jang, and Soo-Yeon Lee. "Ar Plasma Treatment for Highly Stable n+ Region of Self-Aligned Coplanar IGZO TFT". *The 29th International Display Workshops (IDW 22), Fukuoka, Japan, Dec 2022 (Poster)*.
- Jimin Kang, and Soo-Yeon Lee. "The Pixel Circuit Compensating for Strain Effect and Threshold Voltage Variation in Stretchable Display". *The 29th International Display Workshops (IDW 22), Fukuoka, Japan, Dec 2022 (Invited)*.
- Yuseong Jang, Kyeong-Soo Kang, and Soo-Yeon Lee. "ZnON Thin Film and Its Impact on the IGZO Phototransistor". *The 29th International Display Workshops (IDW 22), Fukuoka, Japan, Dec 2022 (Oral)*.
- Ji-Hwan Park, Kyeong-Soo Kang and Soo-Yeon Lee. "Effect of Mobility Compensation on Active-Matrix OLED Pixel Circuit". *The 2 2nd International Meeting on Information Display 202 2 (IMID 202 2), Busan/Online, Korea, August 202 2 (Oral)*.
- Minsik Kong, Jimin Kang, and Soo-Yeon Lee. "Subthreshold Swing Engineering in a-IGZO TFT by Manipulating Oxygen Partial pressure during RF-Magnetron Sputtering". *The 22nd International Meeting on Information Display 2022 (IMID 2022), Busan/Online, Korea, August 2022 (Poster)*.
- Jimin Kang, Kyeong-Soo Kang, Ji-Hwan Park, Minsik Kong, and Soo-Yeon Lee. "Stretchable AMOLED Display Pixel Circuit Compensating for Vth Variation and Strain Effect". *The 29th International Workshop on Active-Matrix Flatpanel Displays and Devices (AM-FPD 22), Kyoto, Japan, July 2022 (Oral)*.
- Junhyeong Park, Yuseong Jang, Jinkyu Lee, and Soo-Yeon Lee. "Charge Trap-Based Synaptic Transistor Employing In-Ga-Zn-O as Channel and Trap Layers for Bio-Inspired Neuromorphic Computing". *SID Display Week 2022, San Jose, USA, May 2022 (Poster)*.
- Ji-Hwan Park, Kyeong-Soo Kang, Jimin Kang, and Soo-Yeon Lee. "A New Active-Matrix OLED Pixel Circuit Compensating for Depletion-mode Threshold Voltage and Mobility of a-IGZO TFT with Source Follower Method". *SID Display Week 2022, San Jose, USA, May 2022 (Poster)*.
- Jimin Kang, Kyeong-Soo Kang, Ji-Hwan Park, and Soo-Yeon Lee. "AMOLED Pixel Circuit for Strain Compensation in Stretchable Display". *SID Display Week 2022, San Jose, USA, May 2022 (Poster)*.

**2021**

- Jimin Kang, Kyeong Soo Kang, Ji-Hwan Park, Kee Chan Park, and Soo-Yeon Lee. "A New Pixel Circuit Compensating for Strain-induced Luminance Reduction in Stretchable Active-Matrix Organic Light Emitting Diode Displays". *IEEE Electron Device Letters, Vol. 42, no.9, pp.1350-1353, Sept. 2021*.
- Jaihyun Koh, Kyeongsoo Kang, Chaehun Shin, Soo-Yeon Lee and Sungroh Yoon. "Compensating Nonuniform OLED Pixel Brightness in a Vertical Blanking Interval by Learning TFT Characteristics". *IEEE Transactions on Electron Devices, vol. 68, no. 7, pp. 3396-3402, July 2021*.
- Kyeongsoo Kang, Jin Kyu Lee, Jimin Kang, and Soo-Yeon Lee. "A Novel Real-Time TFT Threshold Voltage Compensation Method for AM-OLED Using Double Sampling of Source Node Voltage". *IEEE Journal of the Electron Devices Society, vol. 9, pp. 311-317, Feb. 2021*.
- Jungwoo Lee, Jongsu oh, Eunkyo Jung, Keechan Park, Jae-Hong Jeon, Soo-Yeon Lee, Yong-Sang Kim. "High-reliability gate driver circuit to prevent ripple voltage". *Journal of the Society for Information Display 29.1, 2021*.
- Ji-Min Kang , Kyeong-Soo Kang , Ji-Hwan Park and Soo-Yeon Lee. "Double-gate AM-OLED Pixel Circuit Independent on TFT and OLED Vth Variation". *The 21st International Meeting on Information Display 2021 (IMID 2021), Seoul/Online, Korea, August 2021 (Oral)*.

## 특허

Patents 페이지의 2022–2025년 구역 27건이다. 연도는 누리집의 연도 구역 표기이고, 출원일·등록일 자체는 게시되어 있지 않다. 제목·발명자·출원 또는 등록 번호 표기는 게시 내용이다.[^patents]

- 2025 · Yumin YUN, Junhyeong PARK, Soo-Yeon LEE, "문턱전압 변동의 보상 기능을 갖는 인공신경망 뉴런 회로", KR-Patent No. 10-2877890
- 2025 · Jimin KANG, Soo-Yeon LEE, "스트레처블 마이크로 LED 디스플레이 보상 방법", KR-Patent No. 10-2860311
- 2025 · Jimin KANG, Soo-Yeon LEE, "스트레처블 표시장치의 보상 회로 및 그를 포함하는 스트레처블 표시장치", KR-Patent No. 10-283 6865
- 2025 · Jimin KANG, Soo-Yeon LEE, "스트레처블 표시장치의 보상 회로 및 그를 포함하는 스트레처블 표시장치", KR-Paten t No. 10-28 36871
- 2025 · Ji-Ho LEE, Soo-Yeon LEE, "유기 발광 소자 화소 회로의 디밍 구간을 활용한 보상 방법", KR-patent No. 10-2784881
- 2025 · Kyeong-Soo KANG, Sangik LEE, Joon-Chul GOH, Soo-Yeon LEE, "표시 장치 및 문턱 전압 센싱 방법", KR-Patent No. 10-2864250
- 2025 · Kyeong-Soo KANG, Soo-Yeon LEE, "마이크로 엘이디 화소 회로 및 그를 포함하는 구동 방법", KR-Patent No. 10-2827882
- 2025 · Kyeong-Soo KANG, Soo-Yeon LEE, "표시 장치 및 표시 장치의 문턱 전압 센싱 방법", KR-Patent No. 10-2806491
- 2025 · Kyeong-Soo KANG, Soo-Yeon LEE, "PWM 방식으로 구동되는 마이크로 LED 화소회로", KR-Patent No. 10-2799912
- 2025 · Kyeong-Soo KANG, Chanjin P ARK, Soo-Yeon LEE, "마이크로 LED 구동 회로", KR-Patent No. 10-2852164
- 2025 · Soobin An, Soo-Yeon LEE, "박막 트랜지스터 및 이의 제조방법", KR-Patent No. 10-2851490
- 2025 · Kyeong-Soo KANG, Soo-Yeon LEE, "PWM 구동을 위한 SWEEP 신호 생성 방식", KR-Patent No.  10-2768970
- 2025 · Chanjin PARK, Soo-Yeon Lee, "유기 발광 다이오드용 화소 회로 및 그의 동작 방법", KR-Patent No. 10-2833132
- 2025 · Kyeong-Soo KANG, Jin Kyu LEE, Soo-Yeon LEE, "유기 발광 표시 장치, 및 구동 특성 센싱 방법", KR-Patent No. 10-2773893
- 2025 · Minsik KONG, Soo-Yeon LEE, "어레이 내부로 연장되는 도파관을 포함하는 뉴로모픽 시스템", KR-Patent No. 10-2827842
- 2025 · Minsik KONG, Soo-Yeon LEE, "발광소자가 내장된 뉴로모픽 소자 및 이를 이용한 뉴로모픽 시스템", KR-Patent No. 10-2809128
- 2025 · J in Kyu LEE, Soo-Yeon LEE, "고이동도 박막 트랜지스터 구동 소자 및 이의 제조방법", KR-Patent No. 10-2787271
- 2025 · Jin Kyu L EE, Soo-Yeon LEE, "박막 트랜지스터 구동 소자 및 이의 제조방법", KR-Patent No. 10-2792725
- 2025 · Jimin KANG, Soo-Yeon LEE, "더블게이트 트랜지스터를 포함하는 마이크로 LED 구동 회로 및 이를 포함하는 마이크로 LED 표시장치", KR-Patent No. 10-2 768968
- 2024 · Ji-Hwan PARK, Soo-Yeon LEE, "유기 발광 다이오드를 포함하는 화소 회로 및 그를 포함하는 표시장치", KR-Patent No. 10-2706105
- 2024 · Kyeong-Soo KANG, Jin Kyu LEE, Jeonkyoo KIM, Manseung CHO, Junhee MOON, Bonghyun YOU, Soo-Yeon LEE, "DISPLAY DEVICE, AND METHOD OF SENSING A DRIVING CHARACTERISTIC", US-Application No. US 11,955,092 B2
- 2024 · Jimin KANG, Soo-Yeon LEE, "COMPENSATION CIRCUIT FOR STRETCHABLE DISPLAY AND STRETCHABLE DISPLAY INCLUDING SAME", KR-Patent No. 10-2657518
- 2023 · Jimin KANG, Soo-Yeon LEE, "STRAIN SENSOR CIRCUIT NETWORK, METHOD FOR DETERMINING STRAIN POINT AND STRAIN DEGREE OF STRETCHABLE DISPLAY AND SYSTEM FOR COMPENSATING A CURRENT OF STRETCHABLE DISPLAY USING THE SAME", KR-Application No. 1025947550000
- 2023 · Kyeong-Soo KANG, Jin Kyu LEE, Jeonkyoo KIM, Manseung CHO, Junhee MOON, Bonghyun YOU, Soo-Yeon LEE, "DISPLAY DEVICE, AND METHOD OF SENSING A DRIVING CHARACTERISTIC", US-Application No. US 11,631,374 B2
- 2023 · Kyeong-Soo KANG, Sangik LEE, Joon-Chul GOH, Soo-Yeon LEE, "DISPLAY DEVICE AND METHOD OF SENSING A THRESHOLD VOLTAGE", US-Application No. US 11,610,551 B2
- 2023 · Kyeong-Soo KANG, Soo-Yeon LEE, "Pixel circuit, light emitting display apparatus including pixel circuit, and operating methods thereof ", KR-Application No. 10-2496448-00-00
- 2022 · Kyeong-Soo KANG, Jin Kyu LEE, Jeonkyoo KIM, Manseung CHO, Junhee MOON, Bonghyun YOU, Soo-Yeon LEE, "DISPLAY DEVICE, AND METHOD OF SENSING A DRIVING CHARACTERISTIC", US-Application No. US 11,430,394 B2

## 수상

2026년 학회 목록과 학부 소식에 게시된 수상 3건이다. 날짜는 발표·행사 기간 또는 게시일을 구분해 적었다.[^conference][^sidaward][^merck]

- 2026년 8월 · Heejae Roh·Saeru Cheon·Siyuan Liu·Yuanyuan Zhou·Soo-Yeon Lee·Naoji Matsuhisa의 터치 감지 기능을 갖춘 신축성 OLED 디스플레이 발표, ICPFE 2026 Best Poster Award 수상
- 2026년 5월 3–8일 · 배선열 박사과정을 포함한 연구팀, SID Display Week 2026 Distinguished Student Paper Award 수상
- 2026년 9월 1일 게시 · 이수연 교수, 머크 젊은 과학자상 수상

## 연락과 위치

- 교수 이메일: sooyeon.lee@snu.ac.kr[^people][^contact]
- 교수 연구실: 서울대학교 301동 1109호[^professor]
- 전화: 02-880-7273[^professor]
[^home]: ACELAB, Home. <https://sites.google.com/view/snu-acelab/home> (열람 2026-10-26).
[^research]: ACELAB, Research. <https://sites.google.com/view/snu-acelab/research> (열람 2026-10-26).
[^department]: 서울대학교 전기·정보공학부, 차세대 박막소자 및 회로 연구실. <https://ece.snu.ac.kr/research-faculty/research/lab?labidx=84&md=view> (열람 2026-10-26).
[^pixel]: ACELAB, Display Pixel Circuit / Sensor Circuit and Board Design. <https://sites.google.com/view/snu-acelab/research/pixel-sensor-circuit%EC%9D%98-%EB%B3%B5%EC%82%AC%EB%B3%B8> (열람 2026-10-26).
[^oxide]: ACELAB, Oxide Based Devices. <https://sites.google.com/view/snu-acelab/research/oxide-based-devices> (열람 2026-10-26).
[^neuro]: ACELAB, Neuromorphic Circuit. <https://sites.google.com/view/snu-acelab/research/neuromorphic-circuit%EC%9D%98-%EB%B3%B5%EC%82%AC%EB%B3%B8> (열람 2026-10-26).
[^photonics]: ACELAB, Photonics. <https://sites.google.com/view/snu-acelab/research/photonics> (열람 2026-10-26).
[^people]: ACELAB, People. <https://sites.google.com/view/snu-acelab/people> (열람 2026-10-26).
[^professor]: 서울대학교 전기·정보공학부, 이수연 부교수. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p835> (열람 2026-10-26).
[^journals]: ACELAB, Journals. <https://sites.google.com/view/snu-acelab/publications/journals> (열람 2026-10-26).
[^conference]: ACELAB, Conference. <https://sites.google.com/view/snu-acelab/publications/conference> (열람 2026-10-26).
[^patents]: ACELAB, Patents. <https://sites.google.com/view/snu-acelab/publications/patents> (열람 2026-10-26).
[^contact]: ACELAB, Contact. <https://sites.google.com/view/snu-acelab/contact> (열람 2026-10-26).
[^sidaward]: 서울대학교 전기·정보공학부, 이수연 교수 연구팀 SID Display Week 2026 Distinguished Student Paper Award 수상. <https://ece.snu.ac.kr/ece/news?bbsidx=57767&md=v> (열람 2026-10-26).
[^merck]: 서울대학교 전기·정보공학부, 이수연 교수 2026년 머크 어워드 머크 젊은 과학자상 수상. <https://ece.snu.ac.kr/ece/news?bbsidx=58010&md=v> (열람 2026-10-26).
[^p1]: J. Kim 외, S.-Y. Lee, Journal of the Society for Information Display 34, 25-32 (온라인 2025-11-24). <https://doi.org/10.1002/jsid.2110> 초록 기준(출판사 논문 페이지). 초록 원문 <https://sid.onlinelibrary.wiley.com/doi/10.1002/jsid.2110>.
[^p2]: S. Bae 외, S.-Y. Lee, Journal of the Society for Information Display 34, 214-223 (온라인 2026-04-03). <https://doi.org/10.1002/jsid.70054> 초록 기준(출판사 논문 페이지). 초록 원문 <https://sid.onlinelibrary.wiley.com/doi/10.1002/jsid.70054>.
[^p3]: H. Kwon 외, S.-Y. Lee, Journal of the Society for Information Display 33, 24-33 (온라인 2024-11-07). <https://doi.org/10.1002/jsid.2017> 초록 기준(출판사 논문 페이지). 초록 원문 <https://sid.onlinelibrary.wiley.com/doi/10.1002/jsid.2017>.
[^p4]: J. Park 외, S.-Y. Lee, Advanced Electronic Materials 9, 2201306 (온라인 2023-04-14). <https://doi.org/10.1002/aelm.202201306> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/aelm.202201306>.
[^p5]: J. Park 외, S.-Y. Lee, Advanced Intelligent Systems, e70508 (온라인 2026-08-17). <https://doi.org/10.1002/aisy.70508> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.70508>.
[^p6]: Y. Yun 외, S.-Y. Lee, Advanced Intelligent Systems 8, e70374 (온라인 2026-04-01). <https://doi.org/10.1002/aisy.70374> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.70374>.
[^p7]: H.-J. Noh 외, S.-Y. Lee, Advanced Intelligent Systems, e70474 (온라인 2026-07-11). <https://doi.org/10.1002/aisy.70474> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.70474>.
[^p8]: M. Kong 외, S.-Y. Lee, Advanced Electronic Materials 12, e00765 (온라인 2026-05-27). <https://doi.org/10.1002/aelm.202500765> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202500765>.

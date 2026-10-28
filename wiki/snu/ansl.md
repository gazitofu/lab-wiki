# Advanced Next-generation Semiconductor Lab (ANSL)

**서울대학교 공과대학 재료공학부 · 한준규 조교수**

- 영문 이름: Advanced Next-generation Semiconductor Lab (ANSL)[^home]
- 대분야: 전기전자·반도체·광학
- 태그: 뉴로모픽 소자[^research], 메모리 반도체 소자[^research][^p1], 3차원 집적[^research], 산화물 반도체[^p1][^p2], 확률 컴퓨팅[^research][^p5][^p6], 이징 머신·물리 기반 계산[^research], 강유전체[^p8]
- 홈페이지: <https://ansl.snu.ac.kr/>

> 반도체 소자를 위로 쌓고, 신경세포의 동작과 확률적 변화를 계산에 활용하는 차세대 반도체 연구실이다.[^dept][^research]

## 무엇을 연구하나

ANSL은 정보를 저장하고 계산하는 반도체 소자와 그 제작 방법을 연구한다. 소자는 특정한 기능을 수행하는 전자 장치의 구성 단위다. 소재·소자·시스템을 함께 살피며, 전자 장치에 넣는 소자의 수와 에너지 효율을 높이는 것이 목표다.[^dept]

한 축은 3차원 집적(소자 층을 한 칩 안에서 위로 쌓는 기술)이다. 트랜지스터(전기 신호로 전류를 조절하는 반도체 소자)를 쌓아 논리 기능과 메모리 기능을 구현한다. 전류는 전기를 띤 입자의 흐름을 단위 시간에 지나가는 전기의 양으로 나타낸 물리량이다. 산화물 반도체와 실리콘을 함께 쓰는 수직 적층 메모리도 개발한다.[^research][^p2]

다른 축은 뇌의 정보 처리에서 착안한 뉴로모픽 계산과 확률 계산이다. 뉴로모픽 계산은 신경세포와 그 사이 연결의 기능을 모사한 계산이다. 랩은 인공 뉴런과 시냅스 소자, 감지와 계산을 함께 하는 센서를 개발한다. 인공 뉴런은 신경세포의 정보 처리 기능을 모사한 소자이며, 시냅스는 신경세포 사이에서 정보를 전달하는 연결부다. 확률 계산에서는 상태가 확률적으로 바뀌는 소자를 이용해 여러 선택지의 조합에서 목적에 맞는 답을 찾는다.[^research][^p3][^p4][^p5][^p6]

소자의 신뢰성(의도한 기능을 정해진 조건과 기간 동안 유지하는 성질)도 연구한다. 전기적 특성이 열이나 사용 이력에 따라 바뀌는 원인을 밝히고, 그 변화를 억제하는 구조와 동작 방법을 설계한다. 연구 대상에는 실리콘과 산화물 반도체를 쓰는 논리·메모리 소자 등이 포함된다.[^research] 대표 논문은 메모리의 정보 유지와 저장 상태를 지우는 동작을 개선한다.[^p7][^p8]

## 주요 연구 주제

### 3차원 집적과 메모리

아래 소자를 만든 뒤 위 소자를 순서대로 제작하는 모놀리식 3차원 집적과 웨이퍼 접합을 연구한다. 웨이퍼는 반도체 소자를 제작하는 판이다. 후공정과 양립하는 제작 방법으로 소자를 쌓으며, 메모리 셀과 배열의 동작을 함께 살핀다. 셀은 정보를 저장하는 기본 단위이고, 배열은 여러 셀을 배치해 연결한 구조다.[^research][^p1][^p2]

### 생체 모사 계산 소자

신경세포를 모사하는 소자와 그 사이 연결 기능을 담당하는 소자를 함께 제작한다. 대표 논문에서는 CMOS(Complementary Metal-Oxide-Semiconductor, 상보적인 두 종류의 트랜지스터를 함께 쓰는 반도체 기술) 공정을 이용해, 같은 구조의 트랜지스터를 인공 뉴런과 시냅스로 각각 동작시킨다. 센서가 감지한 정보를 센서 자체에서 처리하는 인-센서 계산도 연구한다.[^research][^p3] 가스 센서와 전기를 켜고 끄는 소자를 연결해 가스를 감지하고 스파이크(짧게 발생하는 전기 신호)를 만드는 인공 후각 모듈도 개발한다. 모듈은 일정한 기능을 묶은 구성 단위다.[^p4]

### 양자에서 착안한 확률 계산

확률 비트인 p-bit(probabilistic bit)는 0과 1 사이에서 상태가 확률적으로 바뀌는 계산 단위다. 랩은 이를 이용한 확률 계산과 이징 머신(서로 반대인 상태 중 하나를 갖는 계산 단위들의 상호작용 에너지를 이용해, 에너지를 낮추는 상태에서 조합 문제의 답을 찾는 계산기)을 연구한다. 대표 논문은 여러 상태를 다루는 포츠 모형 기반 계산, 한 소자를 확률 비트와 시냅스로 바꿔 동작시키는 집적 하드웨어를 다룬다.[^research][^p5][^p6]

### 소자 열화의 원인과 억제

부유 몸체 효과는 트랜지스터 몸체의 전기적 상태가 외부에서 고정되지 않아 동작 특성에 영향을 주는 현상이며, 자체 발열 효과는 동작 중 발생한 열이 소자에 영향을 주는 현상이다. 랩은 이 현상들과 유전체·계면의 열화를 전기적으로 분석하고, 소자의 수명을 예측하며 신뢰성을 높이는 구조와 동작 방법을 연구한다.[^research]

정보 유지에 관한 대표 논문은 게이트(트랜지스터에서 전기의 흐름을 조절하는 부분)의 서로 다른 층을 양끝과 중앙에 배치해, 저장한 0과 1 모두에서 부유 몸체 효과를 억제하는 구조를 설계하고 모의실험으로 평가했다.[^p7] 지움 동작에 관한 논문은 정공(전자 빈자리로 나타나는 양의 전기 운반자)의 생성과 축적을 분석하고, 지움을 돕는 펄스(제한된 시간 동안 나타나는 신호)를 조절해 저장 상태를 되돌리는 동작을 개선한다.[^p8]

## 대표 논문

2025–2026년에 출판되었고 한준규 교수의 서울대학교 저자 소속을 확인한 논문 가운데, 3차원 집적·생체 모사 계산·확률 계산·소자 신뢰성을 두 편씩 보여 주는 8편을 골랐다. 연도는 온라인 출판 연도를 우선하며, 온라인 날짜가 별도로 등록되지 않은 논문은 등록 발행일을 따른다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 · 학술지 | 쉽게 말하면 | 교수의 역할 |
|---|---|---|---|---|
| 1 | 2025 | [A Vertically Stackable Split-Gate Amorphous Oxide Semiconductor 2T0C DRAM for Reducing Capacitive Coupling and Sneak-Path Current](https://doi.org/10.1002/admt.202502404) · Advanced Materials Technologies | 별도의 저장용 커패시터(전하를 모아 저장하는 소자) 없이 두 트랜지스터로 정보를 저장하는 DRAM(Dynamic Random Access Memory, 저장한 정보를 유지하려면 주기적인 갱신이 필요한 반도체 메모리)을 개발했다. 읽기 트랜지스터의 게이트를 나눠 저장 상태에 영향을 주는 전기적 결합과 원치 않는 경로의 전류를 줄였다. 쓰기 트랜지스터의 산화물 반도체 부분을 정보 저장에도 사용해 수직 적층 구조의 제작을 단순화했다.[^p1] | 마지막 저자 |
| 2 | 2025 | [Heterogeneous Capacitor-less Two-transistor Dynamic Random Access Memory Cell with Long Retention Time and High Sensing Current Supporting 5-Bit Multilevel Operation](https://doi.org/10.1002/pssr.202500131) · physica status solidi (RRL) – Rapid Research Letters | 쓰기 트랜지스터에는 비정질 인듐·갈륨·아연 산화물을, 읽기 트랜지스터에는 단결정 실리콘을 사용하고 두 소자를 수직으로 집적했다. 정보 유지 시간과 정보를 읽을 때의 전류를 함께 확보해, 한 셀에 여러 수준의 정보를 저장하는 동작을 보였다.[^p2] | 공동 교신저자 |
| 3 | 2026 | [Array of Cointegrated Transistor-Based Artificial Neurons and Synapses for Neuromorphic Computing](https://doi.org/10.1002/smll.74638) · Small | 동일한 구조의 트랜지스터들을 서로 다른 기능의 인공 뉴런과 시냅스로 함께 제작했다. 뉴런 하나에 시냅스 16개를 연결한 구조로 문자와 무늬를 인식했다. CMOS 공정 안에서 뉴런·시냅스와 주변 회로를 함께 구성할 수 있는 하드웨어 방식이다.[^p3] | 공동 1저자(누리집 표시) |
| 4 | 2025 | [Neuromorphic olfaction with ultralow-power gas sensors and ovonic threshold switch](https://doi.org/10.1126/sciadv.adv9222) · Science Advances | 가스 센서와 전기를 켜고 끄는 소자를 직렬(부품을 하나의 전류 경로에 이어 붙이는 연결)로 연결한 저전력 인공 후각 모듈을 만들었다. 모듈은 가스를 감지해 스파이크를 내며, 이 신호를 사용하는 스파이크 신경망(SNN, Spiking Neural Network, 스파이크의 발생과 시간을 이용해 정보를 처리하는 계산 모형)으로 가스 종류를 구분했다. 습도가 변하는 조건에서 서로 다른 성분을 구분하는 하드웨어 동작도 보였다.[^p4] | 공동 1저자(누리집 표시), 저자 순서상 두 번째 |
| 5 | 2026 | [CMOS compatible probabilistic computing hardware with cointegrated reconfigurable p-bits and synapse arrays](https://doi.org/10.1038/s41467-026-71906-x) · Nature Communications | 전자를 포획하는 위치의 에너지를 조절해 하나의 트랜지스터를 확률 비트 또는 시냅스로 바꿔 동작시켰다. CMOS 공정으로 확률 비트와 시냅스 배열을 같은 웨이퍼에 집적했다. 음의 가중치를 포함하는 조합 최적화 문제를 다뤘으며, 4개 지점으로 이루어진 문제는 실험으로, 20개 지점으로 이루어진 문제는 모의실험으로 풀었다. 가중치는 각 관계가 계산에 미치는 영향을 나타내는 값이다.[^p5] | 마지막 저자 |
| 6 | 2026 | [Multi-State Probabilistic Computing Using Floating-Body MOSFETs Based on the Potts Model for Solving Complex Combinatorial Optimization Problems](https://doi.org/10.1002/adma.202516797) · Advanced Materials | 몸체가 전기적으로 고정되지 않은 트랜지스터의 확률적인 스위칭을 여러 상태의 확률 비트로 사용했다. 여러 상태를 다루는 포츠 모형과 전압을 나누어 쓰는 회로·상태 선택 방법을 결합했다. 실험에서 조절 가능한 확률 분포를 만들고 조합 최적화 문제를 풀었다.[^p6] | 공동 교신저자(누리집 표시), 마지막 저자 |
| 7 | 2026 | [Three-layer work-function gate for suppressing floating-body effects on vertical-channel DRAM access transistors](https://doi.org/10.1063/5.0320207) · Applied Physics Letters | 수직 방향으로 전기가 흐르는 DRAM 트랜지스터에서, 몸체가 전기적으로 고정되지 않아 정보 유지 시간이 줄어드는 문제를 다뤘다. 게이트의 양끝과 중앙에 서로 다른 일함수를 갖는 층을 배치했다. 일함수는 물질 표면에서 전자를 진공으로 꺼내는 데 필요한 최소 에너지다. 모의실험에서 0과 1 모두의 정보 유지 저하를 억제하는 설계를 보였다.[^p7] | 공동 교신저자(누리집 표시), 마지막 저자 |
| 8 | 2026 | [Role of Hole Dynamics in Polarization Reset and Switching-Assist Pulse-Based Erase Optimization of Floating Body Ferroelectric Field-Effect Transistors](https://doi.org/10.1021/acsaelm.6c01430) · ACS Applied Electronic Materials | 강유전 트랜지스터에서 정보를 지울 때 정공의 생성과 축적이 분극 초기화에 미치는 영향을 분석했다. 분극은 물질 안에서 양·음의 전기가 치우친 상태다. 강유전체는 전기장을 없애도 분극이 남고 그 방향을 전기장으로 뒤집을 수 있는 물질이며, 전기장은 전기를 띤 입자에 힘이 작용하는 공간의 상태다. 지움을 돕는 펄스를 조절해, 지움 전압을 줄인 조건에서도 초기화 속도와 초기화 정도를 개선했다. 전압은 두 위치 사이의 전기적 위치 에너지 차이를 전하량으로 나눈 값이고, 전하량은 물체나 입자가 띤 전기의 양이다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

한준규 교수는 KAIST 전기및전자공학부에서 2017년 학사, 2019년 석사, 2023년 박사 학위를 받았다. 2023–2024년 서울대학교 반도체공동연구소 박사후연구원과 Harvard University 방문연구원을 지냈고, 2024–2025년 서강대학교 시스템반도체공학과 조교수를 거쳐 2025년부터 서울대학교 재료공학부 조교수로 재직한다.[^dept][^prof]

학부 교수 소개의 연구 관심은 3차원 집적, 차세대 계산용 반도체 소자, 반도체 공정·소자 설계에 인공지능을 활용하는 연구다.[^dept] 최근 논문에서는 산화물 반도체와 실리콘의 집적 메모리, 뉴런·시냅스 소자의 공동 제작과 인공 후각, 확률 비트를 활용한 계산이 전문 분야로 드러난다.[^p1][^p2][^p3][^p4][^p5][^p6] 정보 유지와 지움 동작을 개선하는 소자 신뢰성도 연구한다.[^p7][^p8]

## 응용 분야

연구실이 제시한 응용은 논리·메모리 반도체, 감지와 계산을 함께 하는 센서, 생체 모사 계산과 확률 계산 하드웨어다.[^research] 대표 논문에서는 문자·무늬 인식, 가스 구분, 조합 최적화와 메모리의 정보 유지·지움 동작을 다룬다.[^p3][^p4][^p5][^p6][^p7][^p8]

## 구성원

2026년 10월 28일 Researchers 페이지 기준으로 박사후연구원 2명, 박사과정 4명, 석박사통합과정 8명, 석사과정 1명, 학부 구성원 2명이다. 시작 연월과 연구 주제는 카드 표기를 따른다. Jihyeon Yun의 KIST 공동지도 표기를 함께 둔다.[^members] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Pyeongkang Hur | 박사후연구원 |  | Neuromorphic computing |  |
| Hyun-Jung Kim | 박사후연구원 |  | Device reliability |  |
| Hyun-Jun Kang | 박사과정 | 2025.09– | Neuromorphic computing with ferroelectric devices | 8 |
| Seonjae Park | 박사과정 | 2026.03– | Neuromorphic computing |  |
| Hyunjun Lee | 박사과정 | 2026.09– | Probabilistic computing / 3D Integration |  |
| Jae-Hyun Lee | 석박사통합과정 | 2025.03– | Neuromorphic computing | 5, 8 |
| Jeong-Min Lee | 석박사통합과정 | 2025.03– | 3D DRAM with oxide semiconductor | 1, 5, 8 |
| Jun-Young Park | 석박사통합과정 | 2025.09– | Probabilistic computing | 5, 6, 8 |
| Seon-Jin Yoo | 석박사통합과정 | 2025.09– | 3D integration | 8 |
| Seung-Bum Yim | 석박사통합과정 | 2026.03– | 3D DRAM / 3D integration |  |
| Min-Hyeok Jo | 석박사통합과정 | 2026.03– | Neuromorphic computing |  |
| Ki-Nam Park | 석박사통합과정 | 2026.03– | 3D DRAM / 3D integration | 5, 7, 8 |
| Hyeong-Jin Lee | 석박사통합과정 | 2026.03– | 3D DRAM / 3D integration |  |
| Seong-Jun Byun | 석사과정 | 2026.03– | 3D DRAM / 3D integration | 1 |
| Jihyeon Yun | 박사과정 (KIST co-advising) | 2026.09– | Advanced metal interconnect |  |
| Young-Min Park | Undergraduate |  | Probabilistic computing |  |
| Yuri Ha | Undergraduate |  |  |  |

## 최근 논문과 게재 승인 목록 (2021–2026)

한준규 교수의 2025년 서울대학교 부임 전 논문이 함께 들어 있는 개인 저자 목록이다. 랩 Journal Articles의 Lead author·Co-author 구획에서 2021–2026년으로 적힌 100편과 날짜 없는 게재 승인 7편, Conference Presentations의 국제 12건·국내 13건을 함께 실었다. 학회 목록에는 초청 발표가 포함된다. 연도와 월, 저자·제목·학술지·학회는 누리집 표기이며, 2021년 항목은 해당 연도 전체를 포함한다.[^journal][^conference]

게재 승인 7편은 출판 연도가 없어 “연도 표기 없음”으로 구분한다. IEDM 항목의 2026년 12월은 누리집 기재 날짜이며 발표 전 항목이다.[^journal][^conference]

**2026**

- Jae-Hyun Lee, Jun-Young Park, Jeong-Min Lee, Hyun-Jun Kang, Seon-Jin Yoo, Ki-Nam Park, Yoon Ho Jang\*, and Joon-Kyu Han\*. "Hardware-Efficient Locality-Preserving Graph Processing via Ferroelectric Fowler–Nordheim Tunneling Crossbar Array". *Small, Sep. 2026. (\*co-corresponding)*.
- Hyun-Jun Kang, Ki-Nam Park, Jun-Young Park, Jae-Hyun Lee, Jeong-Min Lee, Seon-Jin Yoo, and Joon-Kyu Han. "Role of Hole Dynamics in Polarization Reset and Switching-Assist Pulse-Based Erase Optimization of Floating Body Ferroelectric Field-Effect Transistors". *ACS Applied Electronic Materials, Sep. 2026*.
- †Jaehong Min, †Hyun-Jun Kang, †Jaehong Park, Youngchan Cho, Min Wook Kang, Jueun Lee, Sangwan Kim, David Radermacher, Saeroonter Oh\*, Joon-Kyu Han\*, and Wonjun Shin\*. "Reconfigurable Noise-Spectroscopy Physical Unclonable Function in Floating-Body Charge-Trap-Flash Transistors". *Advanced Functional Materials, Sep. 2026. (†co-first, \*co-corresponding)*.
- †Sang-Won Lee, †Seokho Seo, †Hakcheon Jeong, †Joon-Kyu Han, Yujin Kim, Dongeun Yoo, Joon-Ha Son, Ji-Man Yu, Shinhyun Choi, and Yang–Kyu Choi. "Array of Cointegrated Transistor-based Artificial Neurons and Synapses for Neuromorphic Computing". *Small, Jul. 2026. (†co-first)*.
- Dokyoung Lee, Jun-Young Park, Joon-Kyu Han\*, and Sungho Kim\*. "Physics-Grounded Probabilistic Bits for Hardware-Efficient Intelligent Inference and Optimization". *Advanced Intelligent Systems, Jun. 2026. (\*co-corresponding)*.
- †Juhyung Seo, †Taehyun Park, †Jun-Young Park, Han-Koo Lee, Jae Yeon Park, Wonjun Shin, Joon-Kyu Han\*, and Hocheon Yoo\*. "Sub-mV tunable photonic p-bits for probabilistic computing". *Science Advances, May 2026. (†co-first, \*co-corresponding)*.
- Jun-Young Park, Jae-Hyun Lee, Jeong-Min Lee, Ki-Nam Park, Sungho Kim, and Joon-Kyu Han. "CMOS Compatible Probabilistic Computing Hardware with Cointegrated Reconfigurable P-Bits and Synapse Arrays". *Nature Communications, Apr. 2026*.
- Sunwoo Cheong, Soo Hyung Lee, Janguk Han, Jun-Young Park, Dong Hoon Shin, Yoon Ho Jang, Sung Keun Shim, Sungho Kim, Cheol Seong Hwang\*, and Joon-Kyu Han\*. "Multi‐State Probabilistic Computing Using Floating‐Body MOSFETs Based on the Potts Model for Solving Complex Combinatorial Optimization Problems". *Advanced Materials, Mar. 2026. (\*co-corresponding)*.
- †Seung-Yoon Lee, †Ki-Nam Park, Sihyun Kim\*, and Joon-Kyu Han\*. "Three-Layer Work-Function Gate for Suppressing Floating-Body Effects on Vertical-Channel DRAM Access Transistors". *Applied Physics Letters, Apr. 2026. (†co-first, \*co-corresponding)*.
- Hyun-Jun Kang, Jeong-Min Lee, Jun-Young Park, and Joon-Kyu Han. "Demonstration of Gateless 1T Array Structure for High-Density DRAM Applications". *IEEE Electron Device Letters, Jan. 2026*.
- Seong-Yun Yun, Joon-Kyu Han, and Yang-Kyu Choi. "Uncovering a Third Function of the Transistor Beyond Switching and Amplification: Coupled Photo-Responsive Oscillators for In-Sensor Computing". *Materials Horizons, Apr. 2026*.
- †Hyun-Jun Kang, †Soo Hyung Lee, Jae-Hyun Lee, Seon-Jin Yoo, Jiabao Ye, Soohyeon Kim, Wei D. Lu\*, and Joon-Kyu Han\*. "Experimental Demonstration of a 2-Tier Monolithic 3D FeTFT Array with 3-b/cell Analog MAC and Full-Stack Evaluation for CNN and MoE-LLM Inference". *International Electron Devices Meeting (IEDM), Dec. 2026. (†co-first, \*co-corresponding) (발표 전; 누리집 기재 날짜 2026-12)*.
- Joon-Kyu Han. "Capacitorless DRAM Technologies to Overcome Capacitor Scaling". *Global Conference of Innovation Materials (GCIM), Jun. 2026. (Invited)*.
- Joon-Kyu Han. "Silicon Transistors for Unconventional Computing". *MRS Spring Meeting & Exhibit, Apr. 2026. (Invited)*.
- Hyun-Jun Kang, Jun-Young Park, Jae-Hyun Lee, and Joon-Kyu Han. "Cell-Level and Array-Level Analysis of Gateless Polycrystalline-Silicon Channel-Based 1T-DRAM Cell for Cost-Effective Vertical Stacking". *Korean Conference on Semiconductors (KCS), Jan. 2026*.
- Jun-Young Park, Seong-Hun Kim and Joon-Kyu Han. "Random Telegraph Noise-Driven Probabilistic Bit in Polycrystalline Silicon Thin-film Transistor". *Korean Conference on Semiconductors (KCS), Jan. 2026*.
- Jae-Hyun Lee, Jun-Young Park, and Joon-Kyu Han. "Self-Rectifying Ferroelectric Diode-Based Crossbar Array to Map Non-Euclidean Graph Data". *Korean Conference on Semiconductors (KCS), Jan. 2026*.
- Jeong-Min Lee, Seung-Yoon Lee, Seong-Jun Byun, and Joon-Kyu Han. "A Split-Gate 2T0C Gain Cell Suppressing Cell-Level and Array-Level Issues". *Korean Conference on Semiconductors (KCS), Jan. 2026*.
- Seong-Jun Byun, Jeong-min Lee, and Joon-Kyu Han. "Single-Ended 3T Sense Amplifiers for Amorphous Oxide Semiconductor 2T0C DRAM". *Korean Conference on Semiconductors (KCS), Jan. 2026*.
- Hyun Wook Kim, Jin Hong Kim, Dong Hoon Shin, Min Chung Jung, Tae Won Park, Hyung Jun Park, Joon-Kyu Han, and Cheol Seong Hwang. "Neuromorphic Visual Receptive Field Hardware with Vertically Integrated Indium-Gallium-ZincOxide Optoelectronic Memristors over Silicon Neuron Transistors". *Korean Conference on Semiconductors (KCS), Jan. 2026*.

**2025**

- Jeong-Min Lee, Seung-Yoon Lee, Seong-Jun Byun, and Joon-Kyu Han. "A Vertically Stackable Split-Gate Amorphous Oxide Semiconductor 2T0C DRAM for Reducing Capacitive Coupling and Sneak-Path Current". *Advanced Materials Technologies, Dec. 2025*.
- Jae-Hyun Lee, Seong-Yun Yun, Joon-Kyu Han\*, and Yang-Kyu Choi\*. "A Review of Single Transistor-based Neuron for Highly Scalable Neuromorphic Hardware". *IEEE Electron Devices Reviews, Nov. 2025. (\*co-corresponding)*.
- †Seong-Jun Byun, †Jeong-Min Lee, and Joon-Kyu Han. "Single-Ended 3T Sense Amplifiers for Amorphous Oxide Semiconductor 2T0C DRAM". *IEEE Transactions on Electron Devices, Nov. 2025. (†co-first)*.
- Hyun-Jun Kang, Jun-Young Park, Jae-Hyun Lee, and Joon-Kyu Han. "Gateless 1T-DRAM Cell with a Polycrystalline-Silicon Channel for Cost-Effective Vertical Stacking". *IEEE Electron Device Letters, Nov. 2025*.
- Hyun Wook Kim, Jin Hong Kim, Dong Hoon Shin, Min Chung Jung, Tae Won Park, Hyung Jun Park, Joon-Kyu Han\*, and Cheol Seong Hwang\*. "Neuromorphic Visual Receptive Field Hardware with Vertically Integrated Indium-Gallium-Zinc-Oxide Optoelectronic Memristors Over Silicon Neuron Transistors". *Advanced Materials, Sep. 2025. (\*co-corresponding)*.
- †Mingu Kang, †Joon-Kyu Han, †Kicheol Lee, Jaeseok Jeong, Chanyoung Yoo, Jeong Woo Jeon, Byongwoo Park, Wonho Choi, Junseong Ahn, Kuk-Jin Yoon, Cheol Seong Hwang, and Inkyu Park. "Neuromorphic Olfaction with Ultra Low Power Gas Sensors and Ovonic Threshold Switch". *Science Advances, Sep. 2025. (†co-first)*.
- Jae-Hyun Lee, Yena Lee, Jun-Young Park, and Joon-Kyu Han. "Frequency Adaptive Single Transistor Neuron based on Temporal Charge Trapping". *IEEE Transactions on Electron Devices, Aug. 2025*.
- Jeong-Min Lee, Seung-Yoon Lee, and Joon-Kyu Han. "Split-gate 2T Gain Cell Memory for Reducing Capacitive Coupling and Sneak Current". *IEEE Transactions on Electron Devices, Jul. 2025*.
- †Jae-Hyun Lee, †Se-Hyun Hwang, Wonbin Jo, Kang-Uk Byeon, and Joon-Kyu Han. "Time-to-first-spike Coding in Sensory Neuron for Energy-Efficient Spiking Neural Networks". *IEEE Electron Device Letters, Jun. 2025. (†co-first)*.
- †Jun-Young Park, †Yeon-Woo Cho, and Joon-Kyu Han. "Highly Endurable Single Transistor Latch Operation Using Band-to-band Tunneling". *IEEE Electron Device Letters, May. 2025. (†co-first)*.
- †Yonghee Lee, †Seung-Yoon Lee, Jinheon Choi, Néstor Ghenzi, Joon-Kyu Han\*, and Cheol Seong Hwang\*. "Heterogeneous 2T0C DRAM Cell with Long Retention Time and High Sensing Current Supporting 5-bit Multilevel Operation". *Physica Status Solidi (RRL), May 2025. (†co-first, \*co-corresponding)*.
- Joon-Kyu Han, Jun-Young Park, Shania Rehman, Muhammad Farooq Khan, Moon-Seok Kim, and Sungho Kim. "Highly Durable and Energy-efficient Probabilistic Bits based on h-BN/SnS2 Interface for Integer Factorization". *InfoMat, Mar. 2025*.
- Taehyun Park, Minseo Kim, Juhyung Seo, Young-Joon Kim, Amit Ranjan Trivedi\*, Joon-Kyu Han\*, and Hocheon Yoo\*. "Advancing Device-Based Computing: Simplifying Circuit Complexity". *Device, Apr. 2025. (\*co-corresponding)*.
- †Ho-Young Maeng, †Joon-Kyu Han, Janguk Han, Soo Hyung Lee, Sunwoo Cheong, Cheol Seong Hwang, and Yang-Kyu Choi. "Homeothermic P-bit Computing Hardware with Stochastic Operations Beyond Limit of Non-stochastic Materials". *Advanced Functional Materials, Mar. 2025. (†co-first)*.
- Joon-Kyu Han. "Reliable Oscillatory Neural Network Utilizing a Thermally Stable Single Transistor-based Oscillator". *Journal of Semiconductor Technology and Science, Feb. 2025*.
- †Jung-Woo Lee, †Joon-Kyu Han, Seung-Il Kim, Ho-Young Maeng, Seong-Yun Yun, Joon-Ha Son, Sang-Won Lee, and Yang-Kyu Choi. "Vertically Integrated Security Devices with Physically Unclonable Function and Random Number Generation". *Nano Research, Jan. 2025. (†co-first)*.
- Sung Keun Shim, Joon-Kyu Han, Janguk Han, Soo Hyung Lee, Dong Hoon Shin, Sunwoo Cheong, Sungho Kim, Hanyong Jeong, Yoon Ho Jang, Cheol Seong Hwang. "Advanced Time Series Data Processing Using Various Memristor-Integrated Devices". *Advanced Materials Technologies, Jun. 2025*.
- Ye-Seong Chung, Seong-Yun Yun, Joon-Kyu Han, and Yang-Kyu Choi. "Oscillatory Neural Network with Tunable Frequency for Brain-Inspired Neuromorphic Computing". *Nano Letters, Apr. 2025*.
- Janguk Han, Yoon Ho Jang, Ji Won Moon, Sung Keun Shim, Sunwoo Cheong, Soo Hyung Lee, Tae Won Park, Joon-Kyu Han, and Cheol Seong Hwang. "Vertical Memristive Crossbar Array for Multi-Layer Graph Embedding and Analysis". *Advanced Materials, Mar. 2025*.
- Hyungjun Park, Joon-Kyu Han, Seongpil Yim, Dong Hoon Shin, Tae Won Park, Kyung Seok Woo, Soo Hyung Lee, Jae Min Cho, Hyun Wook Kim, Taegyun Park, and Cheol Seong Hwang. "An Analysis of Components and Enhancement Strategies for Advancing Memristive Neural Networks". *Advanced Materials, Feb. 2025*.
- Hyun-Jun Kang, Jun-Young Park, Jae-Hyun Lee, and Joon-Kyu Han. "Demonstration of Polycrystalline-silicon Channel-based Gateless 1T-DRAM Cell for Cost-effective 3D Stacking". *International Conference on Advanced Materials and Devices (ICAMD), Dec. 2025*.
- Jeong-Min Lee, Seung-Yoon Lee, Seong-Jun Byeon, and Joon-Kyu Han. "A Cost-Effective 3D Stackable Split-Gate 2T0C DRAM Addressing Cell-Level and Array-Level Reliability Challenges". *International Conference on Advanced Materials and Devices (ICAMD), Dec. 2025*.
- Jun-Young Park, Jae-Hyun Lee, Jeong-Min Lee, Ki-Nam Park, and Joon-Kyu Han. "Co-integrated Probabilistic Computing Hardware with Reconfigurable P-bits and Synapse Arrays through Trap Energy Control in Charge-trap Field-effect Transistor". *International Conference on Advanced Materials and Devices (ICAMD), Dec. 2025*.
- Joon-Kyu Han. "Fully CMOS Compatible Probabilistic Computing Hardware based on Silicon Field-effect Transistors". *International Conference on Advanced Materials and Devices (ICAMD), Dec. 2025. (Invited)*.
- Joon-Kyu Han. "Artificial Sensory Neuron for In-sensor Spiking Neural Network". *Fall Conference of the Korean Sensors Society, Oct. 2025. (Invited)*.
- Seung-Yoon Lee, Jaehyun On, and Joon-Kyu Han. "Bidirectional Machine Learning Technology to Predict the Electrical Characteristics and Structural Parameters of a Stacked Nanosheet FET". *Korean Conference on Semiconductors (KCS), Feb. 2025*.
- Jae-Hyun Lee and Joon-Kyu Han. "SPICE Modeling of a Resistive Memory Crossbar Array to Solve the Shortest Pathfinding Problem". *Korean Conference on Semiconductors (KCS), Feb. 2025*.
- Min-Ho Kim and Joon-Kyu Han. "Exploring the Influence of Various Structural Parameters on Fork-sheet FET Characteristics". *Korean Conference on Semiconductors (KCS), Feb. 2025*.
- Jun-Young Park and Joon-Kyu Han. "Probabilistic-Bits Utilizing Stochastic Charge Trapping in Field-effect Transistor". *Korean Conference on Semiconductors (KCS), Feb. 2025*.
- Se-Hyun Hwang, Wonbin Jo, Kang-Uk Byeon, and Joon-Kyu Han. "Inhibitive Sensory Neuron for Energy Efficient Spiking Neural Network with Time-to-first-spike Coding". *Korean Conference on Semiconductors (KCS), Feb. 2025*.
- Jin Hong Kim, Hyun Wook Kim, Min Jung Chung, Dong Hoon Shin, Yeong Rok Kim, Joon-Kyu Han, and Cheol Seong Hwang. "A Stochastic Photo-responsive Memristive Neuron for an In-sensor Visual System Based on a Restricted Boltzmann Machine". *Korean Conference on Semiconductors (KCS), Feb. 2025*.

**2024**

- Jin Hong Kim, Hyun Wook Kim, Min Jung Chung, Dong Hoon Shin, Yeong Rok Kim, Jae Hyun Kim, Yoon Ho Jang, Sun Woo Cheong, Soo Hyung Lee, Janguk Han, Hyung Jun Park, Joon-Kyu Han\*, and Cheol Seong Hwang\*. "A Stochastic Photo-responsive Memristive Neuron for an In-sensor Visual System based on Restricted Boltzmann Machine". *Nanoscale Horizons, Oct. 2024. (\*co-corresponding)*.
- Sahngik Mun, Yoon Ho Jang, Janguk Han, Sung Keun Shim, Sukin Kang, Yonghee Lee, Jinheon Choi, Sunwoo Cheong, Soo Hyung Lee, Seung Kyu Ryoo, Joon-Kyu Han\*, and Cheol Seong Hwang\*. "High-Dimensional Physical Reservoir with Back-end-of-line-compatible Tin Monoxide Thin-Film Transistor". *ACS Applied Materials & Interfaces, Aug. 2024. (\*co-corresponding)*.
- †Yoon Ho Jang, †Joon-Kyu Han, and Cheol Seong Hwang. "A Review of Memristive Reservoir Computing for Temporal Data Processing and Sensing". *InfoScience, Dec. 2024. (†co-first)*.
- Jeong Woo Jeon, Byongwoo Park, Yoon Ho Jang, Soo Hyung Lee, Sangmin Jeon, Janguk Han, Seung Kyu Ryoo, Kyung Do Kim, Sung Keun Shim, Sunwoo Cheong, Wonho Choi, Gwangsik Jeon, Sungjin Kim, Chanyoung Yoo, Joon-Kyu Han\*, and Cheol Seong Hwang\*. "Vertically Stackable Ovonic Threshold Switch Oscillator Using Atomic Layer Deposited Ge0.6Se0.4 Film for High-density Artificial Neural Networks". *ACS Applied Materials & Interfaces, Mar. 2024. (\*co-corresponding)*.
- †Jung-Woo Lee, †Joon-Kyu Han, Dong-Hyun Wang, Seong-Yun Yun, Jeong-Seob Oh, Byeong-Chan Bang, Won-Hyo Cha, Jun-Young Park, and Yang-Kyu Choi. "High-pressure Deuterium Annealing for Trap Passivation for a 3D Integrated Structure". *IEEE Transactions on Electron Devices, Apr. 2024. (†co-first)*.
- †Jae Hyeon Kim, †Joon-Kyu Han, Ho-Young Maeng, Janguk Han, Jeong Woo Jeon, Yoon Ho Jang, Kyung Seok Woo, Yang-Kyu Choi, and Cheol Seong Hwang. "Fully CMOS-based p-bits with a Bistable Resistor for Probabilistic Computing". *Advanced Functional Materials, May. 2024. (†co-first)*.
- †Seong-Yun Yun, †Joon-Kyu Han, and Yang-Kyu Choi. "A Nanoscale Bistable Resistor for an Oscillatory Neural Network". *Nano Letters, Jan. 2024. (†co-first)*.
- †Yoon Ho Jang, †Joon-Kyu Han, Sangik Moon, Sung Keun Shim, Janguk Han, Sunwoo Cheong, Soo Hyung Lee, and Cheol Seong Hwang. "High-dimensional In-sensor Reservoir Computing with Optoelectronic Memristors for High-performance Neuromorphic Machine Vision". *Materials Horizons, Aug. 2024. (†co-first)*.
- Jeong-A Han, Jung-Woo Lee, Joon-Kyu Han, Do-Wan Kim, Do-Hoon Lee, and Yang-Kyu Choi. "P-type Ternary Logic MOSFET with Tunable Middle State Using Bidirectional Threshold Switching". *IEEE Electron Device Letters, Nov. 2024*.
- Seong-Yun Yun, Ye-Seong Chung, Joon-Kyu Han, Sang-Won Lee, and Yang-Kyu Choi. "Resistive Coupling of Bistable Resistor-Based Oscillators for Oscillatory Neural Network". *IEEE Transactions on Electron Devices, Nov. 2024*.
- Seong-Yun Yun, Joon-Ha Son, Jin-Ki Kim, Joon-Kyu Han, and Yang-Kyu Choi. "Spike-based Rotation Detection Using a Self-powered Triboelectric Sensor with Mimicry of a Vestibular System". *Nano Energy, Dec. 2024*.
- Sunwoo Cheong, Dong Hoon Shin, Soo Hyung Lee, Yoon Ho Jang, Janguk Han, Sung Keun Shim, Joon-Kyu Han, Néstor Ghenzi, and Cheol Seong Hwang. "Hyperplane Tree-based Data Mining with Multi-functional Memristive Crossbar Array". *Materials Horizons, Oct. 2024*.
- Sang-Won Lee, Seung-Il Kim, Seong-Yun Yun, Joon-Kyu Han, Ji-Man Yu, Joon-Ha Son, and Yang-Kyu Choi. "Single Transistor Latch Near 1 V with Asymmetric Biasing in a MOSFET". *IEEE Transactions on Electron Devices, Oct. 2024*.
- Soo Hyung Lee, Sunwoo Cheong, Jea Min Cho, Néstor Ghenzi, Dong Hoon Shin, Yoon Ho Jang, Janguk Han, Tae Won Park, Dong Yun Kim, Sung Keun Shim, Joon-Kyu Han, Seung Soo Kim, and Cheol Seong Hwang. "In-materia Annealing and Combinatorial Optimization Based on Vertical Memristive Array". *Advanced Materials, Oct. 2024*.
- Yoon Ho Jang, Soo Hyung Lee, Janguk Han, Sunwoo Cheong, Joon-Kyu Han, Seung Kyu Ryoo, and Cheol Seong Hwang. "Memristive Crossbar Array-based Probabilistic Graph Modeling". *Advanced Materials, Sep. 2024*.
- Sang-Won Lee, Seong-Yun Yun, Joon-Kyu Han, Young-Hoon Nho, Seung-Bae Jeon, and Yang-Kyu Choi. "Spike-Based Neuromorphic Hardware for Dynamic Tactile Perception with a Self-Powered Mechanoreceptor Array". *Advanced Science, Sep. 2024*.
- Dong Hoon Shin, Sun Woo Cheong, Soo Hyung Lee, Yoon Ho Jang, Taegyun Park, Janguk Han, Sung Keun Shim, Yeong Rok Kim, Joon-Kyu Han, In Kyung Baek, Néstor Ghenzi, and Cheol Seong Hwang. "Heterogeneous Density-based Clustering with Dual-functional Memristive Array". *Materials Horizons, Jul. 2024*.
- In Kyung Baek, Soo Hyung Lee, Yoon Ho Jang, Hyungjun Park, Jaehyun Kim, Sunwoo Cheong, Sung Keun Shim, Janguk Han, Joon-Kyu Han, Gwang Sik Jeon, Kyung Seok Woo, and Cheol Seong Hwang. "Implementation of Bayesian Network and Bayesian Inference using Cu0.1Te0.9/HfO2/Pt Threshold Switching Memristor". *Nanoscale Advances, Apr. 2024*.
- Kyung Seok Woo, Yonghee Lee, Joon-Kyu Han, Tae Won Park, Yoon Ho Jang, and Cheol Seong Hwang. "A Ternary Gate-Connected Threshold Switching Thin-Film Transistor". *Applied Physics Letters, Apr. 2024*.
- Ji-Man Yu, Youson Kim, Changhyeon Lee, Booseok Jeong, Jin-Ki Kim, Joon-Kyu Han, Junyeong Yang, Seong-Yun Yun, Sung Gap Im, and Yang-Kyu Choi. "Bio-Inspired Organic Synaptor with in-situ ion-Doped Ultrathin Polyelectrolyte Containing Acetylcholine-like Cation". *Small, Feb. 2024*.
- Ji-Man Yu, Gyeongdo Ham, Seong-Yeon Kim, Jin-Ki Kim, Joon-Kyu Han, Seong-Yun Yun, Seonghak Kim, Sang-Won Lee, Seung-Bae Jeon, Dae-Shik Kim, and Yang-Kyu Choi. "Self-Curable Synaptor with Tri-node Charge-Trap FinFET for Semi-Supervised Learning". *IEEE Electron Device Letters, Jan. 2024*.
- Sung Keun Shim, Yoon Ho Jang, Janguk Han, Jeong Woo Jeon, Dong Hoon Shin, Yeong Rok Kim, Joon-Kyu Han, Gyung Seok Woo, Soohyung Lee, Sunwoo Cheong, Jaehyun Kim, Haengha Seo, Jonghoon Shin, and Cheol Seong Hwang. "2Memristor-1Capacitor Integrated Temporal Kernel for High-Dimensional Data Mapping". *Small, Jan. 2024*.
- Sun Woo Cheong, Dong Hoon Shin, Soo Hyung Lee, Yoon Ho Jang, Taegyun Park, Janguk Han, Sung Keun Shim, Yeong Rok Kim, Joon-Kyu Han, Néstor Ghenzi, and Cheol Seong Hwang. "Parallel Density-based Spatial Clustering with Dual-functional Memristive Crossbar Array". *Advanced Functional Materials, Feb. 2024*.
- Yoon Ho Jang, Soo Hyung Lee, Janguk Han, Sung Keun Shim, Kyung Seok Woo, Joon-Kyu Han, and Cheol Seong Hwang. "Spatiotemporal Data Processing with Memristor Crossbar Array-based Graph Reservoir". *Advanced Materials, Feb. 2024*.
- Joon-Kyu Han. "Single Transistor Latch in Floating Body Transistors and its Application in Next-Generation Computing". *International Conference on Electronic Materials and Nanotechnology for Green Environment (ENGE), Nov. 2024. (Invited)*.
- Joon-Kyu Han. "Next-Generation Computing Using Threshold Switching in Floating Body Transistors". *MEMRISYS, Nov. 2024. (Invited)*.
- Joon-Kyu Han. "Artificial Neuron Devices Fully Compatible with CMOS Technology for Neural Processing and Sensing in Neuromorphic Hardware". *International Symposium on the Physics of Semiconductors and Applications (ISPSA), Jun. 2024. (Invited)*.
- Jae Hoon Lee, Yong Hee Lee, Joon-Kyu Han\* and Cheol Seong Hwang\*. "Load Line Analysis of the Memory Window in Amorphous Indium-Gallium-Zinc Oxide-Based Ferroelectric Thin-Film Transistor". *MRS Spring Meeting & Exhibit, Apr. 2024. (\*co-corresponding)*.

**2023**

- †Joon-Kyu Han, †Jung-Woo Lee, Young Bin Kim, Seong-Yun Yun, Ji-Man Yu, Keon Jae Lee, and Yang-Kyu Choi. "Vertically Integrated CMOS Ternary Logic Device with Low Static Power Consumption and High Packing Density". *ACS Applied Materials & Interfaces, Oct. 2023. (†co-first)*.
- †Joon-Kyu Han, †Jung-Woo Lee, †Yeeun Kim, †Young Bin Kim, Seong-Yun Yun, Sang-Won Lee, Ji-Man Yu, Keon Jae Lee, Hyun Myung, and Yang-Kyu Choi. "3-dimensional Neuromorphic Hardware with Single Thin-film Transistor Synapses over Single Thin-body Transistor Neurons by Monolithic Vertical Integration". *Advanced Science, Oct 2023. (†co-first)*.
- Joon-Kyu Han, Seong-Yun Yun, Ji-Man Yu, and Yang-Kyu Choi. "Leaky FinFET for Reservoir Computing with Temporal Signal Processing". *ACS Applied Materials & Interfaces, May 2023*.
- Joon-Kyu Han, Seong-Yun Yun, Ji-Man Yu, Seung-Bae Jeon, and Yang-Kyu Choi. "Artificial Multisensory Neuron with a Single Transistor for Multimodal Perception through Hybrid Visual and Thermal Sensing". *ACS Applied Materials & Interfaces, Jan. 2023*.
- Yoon Ho Jang, Janguk Han, Sung Keun Shim, Sunwoo Cheong, Soo Hyung Lee, Joon-Kyu Han, and Cheol Seong Hwang. "Cross-wired Memristive Crossbar Array for Effective Graph Data Analysis". *Advanced Materials, Dec. 2023*.
- Dae-Han Jung, Ji-Man Yu, Ja-Yun Ku, Sung-Su Yoon, Jae-Hun Kim, Joon-Kyu Han, Tae-Hyun Kil, Dong-Hyun Wang, Ju-Won Yeon, Yang-Kyu Choi, and Jun-Young Park. "Physically Unclonable Function with a Rough Silicon Channel MOSFET". *IEEE Transactions on Electron Devices, Dec. 2023*.
- Hae-Yeon Kim, Seung-Il Kim, Joon-Kyu Han, Jin-Woo Jung, and Yang-Kyu Choi. "A Single MOSFET-Based Oscillator on a Bulk-Silicon Wafer". *IEEE Electron Device Letters, Nov. 2023*.
- Hery Shin, Ji-Man Yu, Joon-Kyu Han, and Yang-Kyu Choi. "Co-integrated Neuromorphic Devices for Bio-inspired Compliance Control". *IEEE Transactions on Nanotechnology, Oct. 2023*.
- Sang-Won Lee, Mingu Kang, Joon-Kyu Han, Seong-Yun Yun, Inkyu Park, and Yang-Kyu Choi. "Two-in-One Type of Olfactory Neuron with Gas Classification for In-sensor Computing". *Device, Sep. 2023*.
- Ji-Man Yu, Dong-Hyun Wang, Joon-Kyu Han, Seong-Yun Yun, Jun-Young Park, and Yang-Kyu Choi. "Lowering of Schottky Barrier Height in a MOSFET by Deuterium Annealing". *IEEE Electron Device Letters, Jul. 2023*.
- Ja-Yun Ku, Ji-Man Yu, Dong-Hyun Wang, Dae-Han Jung, Joon-Kyu Han, Yang-Kyu Choi, and Jun-Young Park. "Improved SOI FinFETs Performance with Low-Temperature Deuterium Annealing". *IEEE Transactions on Electron Devices, Jul. 2023*.
- Seong-Yun Yun, Joon-Kyu Han, Sang-Won Lee, Ji-Man Yu, Seung-Bae Jeon, and Yang-Kyu Choi. "Self-aware Artificial Auditory Neuron with a Triboelectric Sensor for Spike-based Neuromorphic Hardware". *Nano Energy, May 2023*.
- Ji-Man Yu, Seong-Yeon Kim, Jin-Ki Kim, Joon-Kyu Han, Seung-Bae Jeon, and Yang-Kyu Choi. "Triple-Node FinFET with Non-Ohmic Schottky Junctions for Synaptic Devices". *IEEE Electron Device Letters, Jan. 2023*.

**2022**

- Joon-Kyu Han, Ji-Man Yu, Do-Wan Kim, and Yang-Kyu Choi. "An Artificial Neuron with a Leaky FinFET for a Highly Scalable Capacitive Neural Network". *Advanced Intelligent Systems, Dec. 2022*.
- †Young-Woo Chung, †Joon-Kyu Han, Jin-Woo Jung, Seong-Yun Yun, Ji-Man Yu, Mun-Woo Lee, and Yang-Kyu Choi. "Thermally Stable Single-Transistor Neuron for Reliable Neuromorphic System". *IEEE Electron Device Letters, Nov. 2022. (†co-first)*.
- †Joon-Kyu Han, †Sang-Chan Park, Ji-Man Yu, Jae-Hyuk Ahn, and Yang-Kyu Choi. "A Bio-inspired Artificial Gustatory Neuron for a Neuromorphic based Electronic-tongue". *Nano Letters, Jun. 2022. (†co-first)*.
- Joon-Kyu Han, Seong-Yun Yun, Sang-Won Lee, Ji-Man Yu and Yang-Kyu Choi. "A Review of Artificial Spiking Neuron Devices for Neural Processing and Sensing". *Advanced Functional Materials, Aug. 2022*.
- Joon-Kyu Han, Ji-Man Yu, and Yang-Kyu Choi. "CMOS Ternary Logic with a Biristor Threshold Switch for Low Static Power Consumption". *IEEE Electron Device Letters, Jul. 2022*.
- Joon-Kyu Han, Ji-Man Yu, and Yang-Kyu Choi. "A Junctionless Single Transistor Neuron with Vertically Stacked Multiple Nanowires for Highly Scalable Neuromorphic Hardware". *IEEE Transactions on Electron Devices, Jun. 2022*.
- †Joon-Kyu Han, †Mingu Kang, Jaeseok Jeong, Incheol Cho, Ji-Man Yu, Kuk-Jin Yoon, Inkyu Park, and Yang-Kyu Choi. "Artificial Olfactory Neuron for an In-sensor Neuromorphic Nose". *Advanced Science, Jun. 2022. (†co-first)*.
- †Joon-Kyu Han, †Il-Woong Tcho, Seung-Bae Jeon, Ji-Man Yu, Weon-Guk Kim, and Yang-Kyu Choi. "Self-powered Artificial Mechanoreceptor based on Triboelectrification for a Neuromorphic Tactile System". *Advanced Science, Mar. 2022. (†co-first)*.
- †Joon-Kyu Han, †Young-Woo Chung, Jaeho Sim, Ji-Man Yu, Geon-Beom Lee, Sang-Hyeon Kim, and Yang-Kyu Choi. "Mnemonic-Opto-Synaptic Transistor for In-sensor Vision System". *Scientific Reports, Feb. 2022. (†co-first)*.
- †Seong-Joo Han, †Joon-Kyu Han, Gyeong-Jun Yun, Mun-Woo Lee, Ji-Man Yu, and Yang-Kyu Choi. "Ultra-fast Data Sanitization of SRAM by Back-biasing to Resist a Cold Boot Attack". *Scientific Reports, Jan. 2022. (†co-first)*.
- Jung-Woo Lee, Joon-Kyu Han, Myung-Su Kim, Ji-Man Yu, Jin-Woo Jung, Seong-Yun Yun, and Yang-Kyu Choi. "Reliability Improvement of Gate-All-Around Junctionless SONOS Memory by Joule Heat from Inherent Nanowire Current". *IEEE Transactions on Electron Devices, Nov. 2022*.
- Myung-Su Kim, Jin-Ki Kim, Gyeong-Jun Yun, Ji-Man Yu, Joon-Kyu Han, Jong-Woo Lee, Seokho Seo, Shinhyun Choi, and Yang-Kyu Choi. "An Overturned Charge Injection Synaptic Transistor with a Floating-gate for Neuromorphic Hardware Computing". *IEEE Electron Device Letters, Sep. 2022*.
- Ji-Man Yu, Dong-Hyun Wang, Ja-Yun Ku, Joon-Kyu Han, Jun-Young Park, and Yang-Kyu Choi. "Low-Temperature Deuterium Annealing to Improve Performance and Reliability in a MOSFET". *Solid State Electronics, Nov. 2022*.
- Seong-Yeon Kim, Ji-Man Yu, Gi Sung Lee, Dae-Hwan Yun, Moon-Seok Kim, Da-Jin Kim, Geon-Beom Lee, Myung-Su Kim, Joon-Kyu Han, Myungsoo Seo, and Yang-Kyu Choi. "A Synaptic Segmented Transistor with Improved Linearity by Schottky Junctions and Accelerated Speed by Double-Layered Nitride". *ACS Applied Materials & Interfaces, Jul. 2022*.
- Ji-Man Yu, Joon-Kyu Han, and Yang-Kyu Choi. "Mimicry of Biological Synaptic Plasticity with Leaky Charge-Trap FinFET". *Journal of Materials Chemistry C, Jul. 2022*.
- Jin-Woo Jung, Joon-Kyu Han, Ji-Man Yu, Mun-Woo Lee, Moon-Seok Kim, Geon-Beom Lee, Il-Woong Tcho, Seong-Yun Yun, and Yang-Kyu Choi. "Concealable Oscillation-Based Physically Unclonable Function with a Single-Transistor Latch". *IEEE Electron Device Letters, Aug. 2022*.
- Ji-Man Yu, Chungryoel Lee, Joon-Kyu Han, Sang-Won Lee, Moon-Seok Kim, Sung Gap Im, and Yang-Kyu Choi. "Tunable and Reconfigurable Logic Gates with Electrolyte Gate Transistor Array for Neuromorphic Computing". *IEEE Transactions on Electron Devices, Aug. 2022*.
- Ji-Man Yu, Gyeongdo Ham, Chungryeol Lee, Jae-Hyeok Lee, Joon-Kyu Han, Jin-Ki Kim, Donggon Jang, Nahyun Kim, Moon-Seok Kim, Sung Gap Im, Dae-Shik Kim, and Yang-Kyu Choi. "A Multiple-State Ion Synaptic Transistor Applicable to Abnormal Car Detection with Transfer Learning". *Advanced Intelligent Systems, Jun. 2022*.
- Myung-Su Kim, Gyeong-Jun Yun, Wu-Kang Kim, Myungsoo Seo, Da-Jin Kim, Ji-Man Yu, Joon-Kyu Han, Jae Hur, Geon-Beom Lee, Seong-Yeon Kim, Dae-Hwan Yun, and Yang-Kyu Choi. "A Steep-Slope Phenomenon by Gate Charge Pumping in a MOSFET". *IEEE Electron Device Letters, Apr. 2022*.
- Hyun-Jung Kim, Geon-Beom Lee, Joon-Kyu Han, Seong-Joo Han, Da-Jin Kim, Ji-Man Yu, Myung-Su Kim and Yang-Kyu Choi. "Curing of 1-Transistor DRAM by Joule Heat from Punch-through Current". *IEEE Electron Device Letters, Mar. 2022*.
- Jung-Woo Lee, Joon-Kyu Han, Ji-Man Yu, Geon-Beom Lee, Il-Woong Tcho and Yang-Kyu Choi. "Reliability Improvement of Gate-All-Around SONOS Memory by Joule Heat from Gate Induced Drain Leakage Current". *IEEE Transactions on Electron Devices, Jan. 2022*.

**2021**

- Joon-Kyu Han, Jungyeop Oh, Ji-Man Yu, Sung-Yool Choi and Yang-Kyu Choi. "A Vertical Silicon Nanowire Based Single Transistor Neuron with Excitatory, Inhibitory, and Myelination Functions for Highly Scalable Neuromorphic Hardware". *Small, Dec. 2021*.
- Joon-Kyu Han, Myung-Su Kim, Seung-Il Kim, Mun-Woo Lee, Sang-Won Lee, Ji-Man Yu, and Yang-Kyu Choi. "Investigation of Leaky Characteristic in a Single Transistor Based Leaky Integrate-and-fire Neuron". *IEEE Transactions on Electron Devices, Nov. 2021*.
- Joon-Kyu Han, Jungyeop Oh, Gyeong-Jun Yun, Dongeun Yoo, Myung-Su Kim, Ji-Man Yu, Sung-Yool Choi, and Yang-Kyu Choi. "Co-integration of single transistor neurons and synapses by nanoscale CMOS fabrication for highly scalable neuromorphic hardware". *Science Advances, Aug. 2021*.
- Joon-Kyu Han, Seong-Joo Han, Ji-Man Yu, and Yang-Kyu Choi. "Data Sanitization of SRAM by Thermal Distortion". *IEEE Transactions on Electron Devices, Jul. 2021*.
- Joon-Kyu Han, Mun-Woo Lee, Ji-Man Yu, and Yang-Kyu Choi. "A Single Transistor-Based Threshold Switch for a Bio-inspired Reconfigurable Threshold Logic". *Advanced Electronic Materials, May 2021*.
- Mun-Woo Lee, Joon-Kyu Han, Gyeong-Jun Yun, Ji-Man Yu, Geon-Beom Lee, Seong-Joo Han, and Yang-Kyu Choi. "A Temperature Sensor with a Termillator". *IEEE Electron Device Letters, Nov. 2021*.
- Seong-Joo Han, Joon-kyu Han, Myung-Su Kim, Gyeong-Jun Yun, Ji-Man Yu, Il-Woong Tcho, Myungsoo Seo, Geon-Beom Lee, and Yang-Kyu Choi. "Ternary Logic Decoder Using Independently Controlled Double-gate Si-NW MOSFETs". *Scientific Reports, Jun. 2021*.
- Ji-Man Yu, Chungryeol Lee, Joon-Kyu Han, Seong-Joo Han, Geon-Beom Lee, Sung Gap Im and Yang-Kyu Choi. "Multi-functional Logic Circuits Composed of Ultra-thin Electrolyte Gated Transistor with Wafer-scale Integration". *Journal of Materials Chemistry C, May 2021*.
- Wu-Kang Kim, Pavlo Bidenko, Jong Min Kim, Jaeho Shim, Joon-Kyu Han, Seongkwang Kim, Dae-Myeong Geum, Sanghyeon Kim, and Yang-Kyu Choi. "Vertical InGaAs Biristor for sub-1 V Operation". *IEEE Electron Device Letters, May. 2021*.
- Ji-Man Yu, Chungryeol Lee, Da-Jin Kim, Hongkeun Park, Joon-Kyu Han, Jae Hur, Jin-Ki Kim, Myung-Su Kim, Myeongsoo Seo, Sung Gap Im, and Yang-Kyu Choi. "All-solid-state Ion Synaptic Transistor for Wafer-scale Integration with Electrolyte of a Nanoscale Thickness". *Advanced Functional Materials, Jun. 2021*.
- Ji-Man Yu, Gyeong-Jun Yun, Moon-Seok Kim, Joon-Kyu Han, Da-Jin Kim, and Yang-Kyu Choi. "A Poly-Crystalline Silicon Nanowire Transistor with Independently Controlled Double-Gate for Physically Unclonable Function by Multi-States and Self-Destruction". *Advanced Electronic Materials, Apr. 2021*.
- †Joon-Kyu Han, †Jaeho Sim, Dae-Myeong Geum, Seong Kwang Kim, Ji-Man Yu, Jongmin Kim, Sanghyeon Kim, and Yang-Kyu Choi. "3D Stackable Broadband Photoresponsive InGaAs Biristor Neuron for a Neuromorphic Visual System with Near 1 V Operation". *International Electron Devices Meeting (IEDM), Dec. 2021. (†co-first author)*.

**연도 표기 없음**

- †Min Wook Kang, †Seonjae Park, Youngchan Cho, Seo Hui Beak, David Radermacher, Joon-Kyu Han\*, and Wonjun Shin\*. "Synapse-Integrated Noise-Spectroscopy Physical Unclonable Functions". *Advanced Functional Materials, 게재 승인(날짜 표기 없음) (†co-first, \*co-corresponding)*.
- Dokyoung Lee, Jun-Young Park, Joon-Kyu Han\*, and Sungho Kim\*. "Resolving hidden interface-trap capture times through stochastic current transients in multitrap nanoscale transistors". *Scientific Reports, 게재 승인(날짜 표기 없음) (\*co-corresponding author)*.
- Ki-Nam Park, Hyun-Jun Kang, Jeong-Min Lee, Jae-Hyun Lee, Seon-Jin Yoo, Eui-Cheol Yun, Jun-Young Park and Joon-Kyu Han. "Back-Gate Pulse-Controlled Scheme for Retention Enhancement in Double-Gate Nanosheet DRAM". *Applied Physics Letters, 게재 승인(날짜 표기 없음)*.
- Ki-Nam Park, Hyun-Jun Kang, Seon-Jin Yoo, Hyeong-Jin Lee, and Joon-Kyu Han. "In-Depth Analysis of Floating Body Effects in 3D DRAM Access Transistor: Scaling and Material Perspectives". *IEEE Transactions on Device and Materials Reliability, 게재 승인(날짜 표기 없음)*.
- †Seung-Bum Yim, †Ki-Nam Park, Hyun-Jun Kang, Jun-Young Park, Sihyun Kim, Jaeyong Jeong, and Joon-Kyu Han. "Gateless 1T-DRAM for Cryogenic Memory Applications". *Applied Physics Letters, 게재 승인(날짜 표기 없음) (†co-first)*.
- Hyungjun Park, Jin Hong Kim, Hyun Wook Kim, Néstor Ghenzi, Sung Keun Shim, Joon-Kyu Han, Min Chung Jung, Dong Hoon Shin, Kyung Seok Woo, and Cheol Seong Hwang. "Memristive Motion-Streak Neuron for Spatiotemporal Multiple Object Detection". *Advanced Materials, 게재 승인(날짜 표기 없음)*.
- Jae Hoon Lee, Yonghee Lee, Joon-Kyu Han, Kyung Do Kim, Seung Ryong Byun, Hyeon Woo Park, and Cheol Seong Hwang. "Gate Engineering Effect in Ferroelectric Field-Effect Transistors with Al-Doped HfO2 Thin Film and Amorphous Indium-Gallium-Zinc-Oxide Channel". *Advanced Electronic Materials, 게재 승인(날짜 표기 없음)*.

## 과제

한준규 교수의 서울대학교 부임 전인 2024년에 시작한 과제도 포함된 목록이다. 누리집 Projects의 15건 가운데 2024년 또는 2025년에 시작한 것으로 적힌 11건이다. 기간과 진행·완료 분류는 누리집 표기이고, 시작 연도가 기준 기간 안에 든 항목을 실었다.[^research]

- DS부문 신진산학과제 삼성전자 (기간 2025–2028; 상태 진행 중(누리집 분류))
- DRAM 미래기술협의회 삼성전자 (기간 2025–2026; 상태 진행 중(누리집 분류))
- 6종 센싱이 가능한 3차원 집적 구조의 멀티모달 인-센서 뉴로모픽 칩 플랫폼 개발 한국산업기술기획평가원 (기간 2025–2027; 상태 진행 중(누리집 분류))
- 확률론적 컴퓨팅용 실리콘 소자 및 어레이 기술 개발 한국과학기술연구원 (기간 2025–2026; 상태 진행 중(누리집 분류))
- 뉴런과 시냅스가 3차원 집적된 구조의 고집적 뉴로모픽 하드웨어 개발 서울대학교 (기간 2025–2026; 상태 진행 중(누리집 분류))
- 상용 파운드리 Si CMOS 플랫폼과 통합 설계·제작된 고성능 IGZO TFT 시냅스 소자 정보통신기획평가원 (기간 2024–2027; 상태 진행 중(누리집 분류))
- 실리콘 기반 확률적 비트 소자를 이용한 대용량 확률 컴퓨팅 하드웨어 한국연구재단 (기간 2024–2027; 상태 진행 중(누리집 분류))
- 실리콘 채널-MIEC 프로그래밍 터미널을 이용한 인공 시냅스 메모리 신개념 소자 개발 한국연구재단 (기간 2025–2027; 상태 완료(누리집 분류))
- AI 기반 PCB 자동 설계 DB 구축 럭스로보 (기간 2025–2026; 상태 완료(누리집 분류))
- IoT 산업 혁신을 위한 전자회로 설계 AI 기술 개발 서울경제진흥원 (기간 2024–2025; 상태 완료(누리집 분류))
- 대규모 확률 컴퓨팅 하드웨어 제작 국가나노인프라협의체 (기간 2024–2025; 상태 완료(누리집 분류))

## 수상과 선정

2025년 서울대학교 부임 전 수상도 포함한 한준규 교수의 개인 이력이다. 연도만 게시되어 있으며, 그 해 전체가 기준 기간에 드는 2022–2025년의 6건을 실었다.[^prof]

- 2025 · ICAMD2025 신진연구자상(Young Researcher Award)
- 2023 · KAIST 공과대학 박사학위 우수논문상(Excellent Ph.D. Dissertation Award)
- 2022 · KAIST·삼성전자 협력 우수논문상(Excellent Paper Award)
- 2022 · KAIST·삼성전자 협력 우수특허상(Excellent Patent Award)
- 2022 · Young-Han Kim Global Leader 장학금
- 2022 · 제28회 Samsung HumanTech Award 장려상(Encouragement Prize)

## 연락과 위치

- 교수 업무 이메일: joonkyuhan@snu.ac.kr[^prof]
- 위치: 서울대학교 재료공학부, Mailstop 33-308[^dept]
[^home]: ANSL, 첫 화면의 연구실 이름과 소속. <https://ansl.snu.ac.kr/>
[^dept]: 서울대학교 재료공학부, 한준규 교수 소개. 직위·소속·학력·경력·연구 관심·Lab Overview·Mailstop. <https://mse.snu.ac.kr/joon-kyu-han/>
[^research]: ANSL, Research Topics와 Projects. 3차원 논리·메모리 소자, 인공 뉴런·시냅스와 센서, 확률 비트·이징 머신, 소자 신뢰성을 연구한다고 설명한다. <https://ansl.snu.ac.kr/research>
[^prof]: ANSL, Professor. 학력·경력·수상과 업무 이메일. <https://ansl.snu.ac.kr/members-professor>
[^members]: ANSL, Researchers. 과정·시작 연월·연구 주제. <https://ansl.snu.ac.kr/members-researchers>
[^journal]: ANSL, Journal Articles. Lead author·Co-author 구획의 저자·제목·학술지·게재 시기·게재 승인 표시. <https://ansl.snu.ac.kr/publications-journal>
[^conference]: ANSL, Conference Presentations. International·Domestic 구획의 발표 목록. <https://ansl.snu.ac.kr/publications-conference>
[^p1]: J.-M. Lee, S.-Y. Lee, S.-J. Byun, J.-K. Han, Advanced Materials Technologies 11, e02404 (온라인 2025-12-27). <https://doi.org/10.1002/admt.202502404> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202502404>.
[^p2]: Y. Lee 외, C. S. Hwang, physica status solidi (RRL) – Rapid Research Letters 19, 2500131 (온라인 2025-05-25). <https://doi.org/10.1002/pssr.202500131> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/abs/10.1002/pssr.202500131>.
[^p3]: S.-W. Lee 외, Y.-K. Choi, Small 22, e74638 (온라인 2026-07-21). <https://doi.org/10.1002/smll.74638> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/abs/10.1002/smll.74638>.
[^p4]: M. Kang 외, I. Park, Science Advances 11, eadv9222 (2025). <https://doi.org/10.1126/sciadv.adv9222> 초록 기준(Crossref 등록 초록). 등록 발행일 2025-09-26.
[^p5]: J.-Y. Park 외, J.-K. Han, Nature Communications 17, 5110 (온라인 2026-04-11). <https://doi.org/10.1038/s41467-026-71906-x> 초록 기준(OpenAlex 등록 초록).
[^p6]: S. Cheong 외, J.-K. Han, Advanced Materials 38, e16797 (온라인 2026-02-17). <https://doi.org/10.1002/adma.202516797> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/41700537/>.
[^p7]: S.-Y. Lee, K.-N. Park, S. Kim, J.-K. Han, Applied Physics Letters 128, 123304 (온라인 2026-03-24). <https://doi.org/10.1063/5.0320207> 초록 기준(Crossref 등록 초록).
[^p8]: H.-J. Kang 외, J.-K. Han, ACS Applied Electronic Materials 8, 8023-8030 (온라인 2026-09-04). <https://doi.org/10.1021/acsaelm.6c01430> 초록 기준(Crossref 등록 초록).

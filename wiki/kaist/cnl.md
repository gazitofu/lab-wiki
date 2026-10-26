# 계산나노기술공학 연구실 (Computational Nanoelectronics Laboratory, CNL)

**KAIST 전기및전자공학부·반도체공학대학원 · 신민철 교수**

- 분야: 반도체 소자의 양자 수송 모형과 시뮬레이션, 차세대 트랜지스터, 강유전체·자성 메모리, 기계학습을 이용한 소자 계산과 최적화
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 소자 설계 시뮬레이션[^method], 차세대 트랜지스터·논리 소자[^mosfet], 메모리 반도체 소자[^memory], 강유전체[^memory], 스핀트로닉스[^memory], 산화물 반도체[^mosfet], 제1원리 계산[^method]
- 홈페이지: <https://cnl.kaist.ac.kr/home>
- 근거와 출처: [CNL 근거 페이지](cnl-sources.md)

> 반도체 안에서 전자가 어떻게 흐르고 정보가 어떻게 저장되는지를 컴퓨터로 계산하며, 그 계산 도구도 직접 만드는 연구실이다.[^home][^method][^memory]

## 무엇을 연구하나

신민철 교수가 이끄는 CNL은 반도체 소자(전기적 기능을 수행하는 반도체 부품)를 컴퓨터 모형으로 연구한다. 중심 대상은 트랜지스터(전류의 흐름을 조절하는 소자)와 메모리(정보를 저장하는 장치)다. 구조와 재료를 바꾸어 계산하고, 원자 수준의 변화가 소자의 작동에 어떤 영향을 주는지 조사한다. 누리집은 이를 계산을 통한 과학 연구로 소개하며, 소자를 계산하는 도구의 자체 개발과 소자 특성 분석을 함께 내세운다.[^home][^mosfet][^method]

소자가 나노미터(길이 단위) 영역으로 줄어들면 전자의 움직임을 양자역학(물질과 빛의 상태·변화를 설명하는 물리 이론)으로 다루는 일이 중요해진다. 연구실은 양자 수송(quantum transport)을 계산해 재료의 경계, 결함, 표면이 전자의 흐름을 어떻게 바꾸는지 살핀다. 채널(channel)을 둘러싼 구조와 접촉 부위까지 포함한 소자를 모형으로 만들고, 비평형 그린 함수(NEGF, Non-equilibrium Green's function) 방법으로 전자가 드나드는 상태를 계산한다.[^mosfet][^method]

메모리 연구에서는 강유전체(외부 전기장을 없애도 전기 분극이 남고 그 방향을 전기장으로 바꿀 수 있는 물질)와 자성체(자기적 성질을 띠는 물질)의 상태를 정보 저장에 이용한다. 전기장은 전하에 전기력이 작용하는 공간의 성질이며, 전하는 물체가 전기적 힘을 주고받는 성질이다. 강유전체의 전기 분극(양·음 전하가 치우친 상태)과 자성체의 자화(물질이 띠는 자석 성질)가 바뀌는 과정을 전자의 흐름과 함께 계산한다. 이를 위해 서로 영향을 주는 여러 물리 현상을 함께 푸는 다중물리 시뮬레이션을 개발한다.[^memory]

또 다른 축은 계산 방법이다. 원자 수준 모형에 필요한 전자 구조(물질 안 전자의 에너지와 배치)를 구하고, 계산에 쓰는 행렬(수를 행과 열로 배열한 것)의 크기를 줄이거나, 기계학습(자료에서 규칙을 배워 예측하는 계산 방법)으로 다음 설계 후보를 고른다. 목표는 소자의 물리 현상을 다루면서 설계 탐색과 계산에 드는 일을 줄이는 것이다.[^method]

## 주요 연구 주제

### 차세대 트랜지스터의 구조와 재료

연구 소개의 Advanced MOSFET는 금속·산화물·반도체 전계효과 트랜지스터(Metal-Oxide-Semiconductor Field-Effect Transistor)를 다룬다. 게이트(gate)가 전기장으로 채널을 제어하는 구조를 바꾸어 소자 특성을 조사한다. 나노시트(나노미터 영역의 두께를 지닌 판상 구조)와 나노와이어(나노미터 영역의 단면 크기를 지닌 선상 구조), 산화물 반도체(산화물로 이루어져 반도체 성질을 보이는 물질), 원자층 재료를 채널로 쓰는 소자가 대상이다. 소자 크기와 구조 때문에 게이트 제어가 약해지는 단채널 효과(short-channel effects), 재료 경계의 영향, 터널링(tunneling)을 계산한다. 연구실은 자체 양자 수송 계산기를 개발해 이들 구조의 성능을 분석한다고 밝힌다.[^mosfet]

### 강유전체와 자성을 이용하는 메모리

Novel Memory Devices는 전원을 꺼도 정보가 남는 비휘발성 메모리를 다룬다. 강유전체의 분극을 저장 상태로 쓰는 FeRAM(Ferroelectric Random-Access Memory), 강유전체를 트랜지스터에 넣는 FeFET(Ferroelectric Field-Effect Transistor), 강유전체 층을 통과하는 전자의 흐름을 읽는 FTJ(Ferroelectric Tunnel Junction)를 연구한다. 분극이 공간 안에서 어떤 무늬를 이루는지와 그 무늬가 바뀌는 과정을 계산해 여러 저장 상태를 만드는 방법을 조사한다.[^memory]

자성 메모리에서는 전자의 스핀(spin)을 이용해 자화 방향을 바꾸는 STT-MRAM(Spin-Transfer Torque Magnetoresistive Random-Access Memory)과 SOT-MRAM(Spin-Orbit Torque Magnetoresistive Random-Access Memory)을 연구한다. 자화의 시간 변화를 계산하는 모형과 전자 수송 모형을 이용해 쓰기 동작, 재료와 구조의 영향을 살핀다.[^memory]

### 소자 계산 도구와 기계학습

Methodology에서는 소자 안 전자의 에너지를 표현하는 해밀토니안(Hamiltonian)을 구성하고, 전자의 흐름과 전기적 상태가 서로 맞아떨어지도록 반복 계산하는 도구를 개발한다. 밀도 범함수 이론(DFT, Density Functional Theory)을 비롯한 방법으로 재료의 전자 구조를 구하며, 재료가 바뀌는 경계나 결함도 다룬다. 모드 공간(mode space) 방법은 계산 모형의 크기를 줄이는 데 쓰이고, 포논(phonon)과 전자의 상호작용도 전자 수송 계산에 반영한다.[^method]

설계 최적화에서는 TCAD(Technology Computer-Aided Design)가 후보 소자의 특성을 계산하면 기계학습 모형이 다음 후보를 고르는 과정을 반복한다. 계산 방법을 다룬 2021년 논문에는 베이지안 최적화(Bayesian optimization)를 언제 멈출지 정하는 조건과, 여러 재료가 이어진 소자의 모형을 줄이는 방법이 있다.[^method][^p3][^p4]

## 대표 논문

트랜지스터의 결함 분석, 강유전체 메모리, 계산 도구와 기계학습을 다룬 2021–2026년 논문 8편이다. 아래 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 세 번째는 학술지 서지와 연결된 arXiv 판, 네 번째는 KAIST 전기및전자공학부 게시 초록이다. 다섯 번째부터 여덟 번째는 OpenAlex·Crossref 등록 초록이다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 교수 참여 |
|---|---|---|---|---|
| 1 | 2025 | [Middle Interlayer Engineered Ferroelectric NAND Flash Overcoming Reliability and Stability Bottlenecks for Next-Generation High-Density Storage Systems](https://doi.org/10.1002/advs.202510155) · Advanced Science | 강유전체 재료 안에 중간층을 넣어 분극 변화와 전하가 붙잡히는 작용을 조절했다. 이를 통해 적층형 저장 소자의 안정성과 신뢰성을 개선하고, 저장 상태가 유지되는 특성과 소자별 동작 차이를 분석했다.[^p1] | 공동저자 |
| 2 | 2023 | [Ferroelectric Nanopillar Field-Effect Transistors: Quantum Transport Simulations Based on a Three-Dimensional Phase Field](https://doi.org/10.1103/PhysRevApplied.19.054061) · Physical Review Applied | 트랜지스터 안에 강유전체 기둥을 넣고 분극 상태를 바꾸는 저장 소자를 제안했다. 분극과 전자 흐름을 함께 푸는 모형으로 6개 상태의 동작을 이론적으로 보였으며, 소자가 짧아질 때의 변화도 조사했다.[^p2] | 마지막 저자·교신저자 |
| 3 | 2021 | [Hetero-structure Mode Space Method for Efficient Device Simulations](https://doi.org/10.1063/5.0064314) · Journal of Applied Physics | 서로 다른 재료가 이어지거나 결함과 표면 변화가 있는 소자를 계산하는 모형을 줄이는 방법이다. 네 종류의 소자로 계산의 정확성과 모형 축소 효과를 보였고, 여러 종류의 재료 경계에 적용할 가능성을 제시했다.[^p3] | 단독저자 |
| 4 | 2021 | [Bayesian Optimization of MOSFET Devices Using Effective Stopping Condition](https://ee.kaist.ac.kr/ai-in-device/bayesian-optimization-of-mosfet-devices-using-effective-stopping-condition/) · IEEE Access | 소자 설계를 탐색할 때 반복 횟수를 미리 고정하는 대신, 다음 계산에서 기대되는 개선량으로 중단 시점을 정했다. 이 조건이 설계 최적화에 필요한 학습 자료를 줄이는 효과를 조사했다.[^p4] | 마지막 저자 |
| 5 | 2026 | [Multilevel/Layer FeFET With Polar Topological States: Four-Coupled Multiphysics Simulations](https://doi.org/10.1109/ted.2026.3680378) · IEEE Transactions on Electron Devices | 강유전체의 분극 무늬로 여러 저장 상태를 만드는 단일층·다층 트랜지스터의 가능성을 계산했다. 전자 흐름, 분극 변화, 전기적 상태, 탄성 변형을 함께 풀었으며, 재료 사이 층과 입출력 쪽 구조를 바꾸어 만들 수 있는 상태의 범위를 조사했다.[^p5] | 마지막 저자 |
| 6 | 2024 | [SemiH: DFT Hamiltonian neural network training with semi-supervised learning](https://doi.org/10.1088/2632-2153/ad7227) · Machine Learning: Science and Technology | 물질의 전자 에너지 모형을 예측하는 신경망(연결된 계산 단위들의 관계를 학습하는 모형)을 학습시켰다. 정답이 있는 자료뿐 아니라 모형이 만든 임시 정답을 붙인 자료도 이용해, 학습 자료가 제한된 상황과 학습 때 다루지 않은 원자 수·온도 범위에서의 예측 성능을 조사했다.[^p6] | 공동저자 |
| 7 | 2023 | [A Novel Neural-Network Device Modeling Based on Physics-Informed Machine Learning](https://doi.org/10.1109/ted.2023.3316635) · IEEE Transactions on Electron Devices | 물리 관계를 반영한 기계학습으로 소자의 성능과 위치별 물리량을 예측했다. 일부 전압 조건으로 학습한 뒤, 학습한 조건 사이와 그 바깥에서의 예측 정확성을 조사하고 소자 설계 계산과 실시간 물리 분석에 활용할 방법을 제안했다.[^p7] | 마지막 저자 |
| 8 | 2021 | [First-Principles-Based Quantum Transport Simulations of Interfacial Point Defect Effects on InAs Nanowire Tunnel FETs](https://doi.org/10.1109/ted.2021.3112395) · IEEE Transactions on Electron Devices | 인듐비소 나노와이어 트랜지스터에서 재료 경계의 원자 결함 두 종류가 전자 흐름에 미치는 영향을 계산했다. 결함이 전하를 붙잡거나 전자의 터널링을 돕는 작용을 함께 다뤘으며, 결함 종류에 따른 차이와 소자가 짧아질 때의 영향을 조사했다.[^p8] | 마지막 저자 |

## 교수와 전문 분야

신민철 교수는 서울대학교에서 물리학 학사(1984–1988), Northwestern University에서 물리학 박사(1988–1992) 과정을 밟았다. 누리집은 경력을 한국전자통신연구원 선임연구원(1992–2001), ICU 부교수(2002–2009), KAIST 교수(2009–현재)로 적는다.[^prof] 전기및전자공학부 교수 소개는 현재 직위를 교수로, 주요 연구를 계산나노기술과 나노 소자 시뮬레이션으로 소개한다.[^ee]

교수 소개의 전문 분야는 양자선과 양자점에서의 수송, 단일전자 터널링 등 물질의 양자적 전자 흐름과 나노 소자 계산 도구 개발이다. 최근 연구에서는 트랜지스터의 구조·재료를 원자 수준으로 계산하는 일, 강유전체의 분극 상태와 전자의 흐름을 결합하는 일, 계산 모형을 줄이고 설계를 최적화하는 일이 이어진다.[^prof][^mosfet][^memory][^method]

## 응용 분야

연구실은 차세대 트랜지스터와 적층형 메모리의 구조·재료 설계를 다룬다. 연구 소개는 산화물 반도체를 적층 메모리의 채널 후보로, 강유전체와 자성 메모리를 내장형 저장 장치와 새로운 저장 방식의 후보로 설명한다. 대표 논문에는 강유전체를 이용한 적층형 저장 소자의 신뢰성 개선과 여러 상태를 저장하는 소자의 계산이 포함된다.[^mosfet][^memory][^p1][^p2]

## 구성원

Research Staff와 Students에 게시된 연구원 1명, 박사과정 2명, 석사과정 8명이다. 시작은 개별 쪽에 적힌 해당 과정·직위의 기간이며, 학위 취득으로 해석하지 않는다. 대표 논문 참여는 게시 이름과 저자 이름을 대조했다.[^staff][^students]

| 이름 | 과정·직위 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Phil-Hun Ahn[^a112] | 연구원 | 2025.9 ~ | Quantum transport simulation | k951131h@kaist.ac.kr |  |
| Geunseok choi[^a114] | 박사과정 | 2022.2 ~ | Quantum transport simulation using machine learning; Density functional theory simulation using machine learning | ieggiegg@kaist.ac.kr | 6 |
| Yangjin Jung[^a115] | 박사과정 | 2025.9 ~ |  | yangjj@kaist.ac.kr | 1, 5 |
| Ilhan Yu[^a116] | 석사과정 | 2025.3 ~ |  | ilhan.yu@kaist.ac.kr |  |
| Heonseok Oh[^a117] | 석사과정 | 2025.3 ~ |  | vinc178888@kaist.ac.kr |  |
| Joo Seok Kim[^a118] | 석사과정 | 2025.3 ~ |  | wntjr1024@kaist.ac.kr |  |
| Gyeongwon Roh[^a119] | 석사과정 | 2025.3 ~ |  | gyeongwon7016@kaist.ac.kr |  |
| Seungjin Lee[^a120] | 석사과정 | 2025.9 ~ |  | sjin10.lee@kaist.ac.kr |  |
| Soyeon Park[^a121] | 석사과정 | 2025.9 ~ |  | sy.park@kaist.ac.kr |  |
| Youngmin Wee[^a122] | 석사과정 | 2026.3 ~ |  | dnlherry@kaist.ac.kr |  |
| Namgung Yunkyeong[^a123] | 석사과정 | 2026.9 ~ |  | ngyk203@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni에 게시된 이름과 개별 소개의 학위·과정, 기간, 진로다. 과정 재학·후보 표기가 있는 항목은 그 표기를 그대로 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyun Whan Choi[^a125] | 2008~2014: KAIST Ph.D; 2004~2006: Information and Communication University, MS, ECE | 2014~ : Samsung Display |
| Chi-yui Ahn[^a126] | 2008~2015: Ph.D. in Electrical Engineering, Stanford University; 2005~2007: M.S. in Electrical Engineering, KAIST | 2016~present: Assistant Professor, Univ. of Texas at San Antonio |
| Tran Le Anh Tuan[^a127] | 2006~2011: KAIST, Ph.D; 2003~2005: Hanoi University of Technology, MS, ECE | 2012~present : Samsung Electronics |
| Ju Young Jung[^a156] | 2011~present: KAIST, Ph.D candidate; 2006~2009: Seoul National University, MS, Chemical Biological Engineering |  |
| Won Chul Choi[^a128] | 2011~2015: KAIST, Ph.D, EE; 2009~2011: KAIST, MS, EE | 2015~ : Samsumg Electronics |
| Kihoon Park[^a129] | 2015-2020: Univ. of Illinois at Urbana-Champaign, EE, PhD.; 2011~2013 : KAIST, MS, EE | 2020 - Present: Device Engineer, Intel, Hilsboro, USA; 2013~2014 : SK hynix |
| Yo Lum Lee[^a130] | 2012~2014: KAIST, MS, EE | 2016~ : Synopsys; 2014~2016 : Samsung Electronics |
| Ho-Won Choi[^a131] | 2012~2014 : KAIST, MS, EE | 2018~present : SK hynix; 2014~2018 : ABOV semiconductor |
| Jaehyun Lee[^a132] | 2012~2016: KAIST Ph. D, EE; 2006~2008: Information and Communication University, MS, ECE | 2023 ~ :Professor, Pusan National University, Pusan, S. Korea; 2016 ~ 2023 : Postdoctoral researcher, University of Glasgow, UK. |
| Sangchun Park[^a133] | 2015~2017: KAIST, Master | 2017~ : Samsung Electronics |
| Seung Heon Baek[^a134] | 2013~2017 : KAIST Ph. D , EE; 2011~2013 : KAIST, MS, EE | 2017~ : SK hynix |
| Hyo-Eun Jung[^a135] | 2013~2018 : KAIST Ph. D; 2011~2013 : KAIST, MS, EE | 2018~ : Samsung Electronics |
| Sungwoo Jung[^a136] | 2016~2018 : KAIST, Master | 2018~ present : Samsung Electronics |
| Moonhoi Kim[^a137] | 2017 ~ 2019 : KAIST, MS, Electrical Engineering | 2019 ~ present : SK hynix |
| Yongsoo Ahn[^a138] | 2014. 09 ~ 2019. 08 : KAIST, Ph. D, Electrical Engineering; 2012. 02 ~ 2014. 08 : KAIST, MS, Electrical Engineering | 2019. 09 ~ present : Samsung Electronics |
| Woojin Jeong[^a139] | 2014~ 2020: KAIST Ph. D, EE; 2012~2014 : KAIST, MS, EE | 2020 ~ present : Samsung Electronics |
| Yucheol Cho[^a140] | 2021~2025 : KAIST, Ph.D candidate, Electrical Engineering; 2018~2020: KAIST, MS, Electrical Engineering | 2025~ : Professor, Hanbat National University, Daejeon, S. Korea; 2020~2021: Samsung Electronics |
| Jihun Byun[^a141] | 2019 ~ 2021 : KAIST, MS, Electrical Engineering | 2021 ~ present : Samsung Electronics |
| Junbeom Seo[^a142] | 2017.3. ~ 2021.2 : Ph. D, Electrical Engineering, KAIST; 2014.3. ~ 2016.8. : MS, Electrical Engineering, KAIST | 2021.3 ~ present : Samsung Electronics |
| Seongcheol Noh[^a143] | 2016~2021: KAIST, Ph.D candidate, EE; 2014~2016: KAIST, MS, EE | 2021~ : Samsung Electronics |
| Chan-Hyeong Lee[^a144] | 2021 ~ 2023 : KAIST, MS, Electrical Engineering | 2023 ~ present : Samsung Electronics |
| Kang-Hyun Joo[^a145] | 2021 ~ 2023 : KAIST, MS, Electrical Engineering | 2024 ~ present : Samsung Electronics |
| Seong Hyeok Jeon[^a146] | 2016~2023 : KAIST, Integrated Master's & Ph. D Program Candidate, Electrical Engineering; 2014~2016 : KAIST, MS, Physics | 2023~ : Samsung Electronics |
| Hyeongu Lee[^a147] | 2019.9 ~ 2024.2 : KAIST, Ph.D, Electrical Engineering; 2017.3 ~ 2019.2 : KAIST, MS, Electrical Engineering | 2024.3 ~ present: Samsung Electronics |
| Bokyeom Kim[^a148] | 2018.3~2024.2: KAIST, Ms-Ph.D combined student, Electrical Engineering | 2024.3~Present: Samsung Electronics |
| Jeong-Hwan Jang[^a149] | 2021.3 ~ : KAIST, MS-Ph.d Integrated, Electrical Engineering | 2024 ~ : Samsung Electronics |
| Jeong-Ho Oh[^a150] | 2021.3 ~ 2024.2 : KAIST, MS student (V-KEPSI, SK hynix), Electrical Engineering | 2024 ~ : SK hynix |
| Seung-Hyo Han[^a151] | 2022.9 ~ 2024.8 : KAIST, MS, Electrical Engineering | 2025 ~ : Samsung Electronics |
| Gyutae Park[^a152] | 2023.3 ~ : KAIST, MS, Electrical Engineering |  |
| Yeongjun Lim[^a153] | 2025. 9 ~ 2026. 8 : KAIST, Ph.D candidate, Electrical Engineering; 2022. 3 ~ 2025. 8 : KAIST, Ph.D candidate, Electrical Engineering; 2020. 3 ~ 2022. 2 : KAIST, MS, Electrical Engineering | 2026. 9 ~ present : SK hynix |
| Deokhwa Seo[^a154] | 2023 ~ 2025 : KAIST, MS, Electrical Engineering |  |
| Seokwon Lee[^a155] | 2024.9 ~ 2026.6 : KAIST, MS, Electrical Engineering | 2026.7 ~ present : SK hynix |

## 최근 논문 목록 (2021–2026)

트랜지스터의 전자 수송, 강유전체·자성 메모리, 원자 수준 계산과 기계학습을 이용한 소자 설계를 다룬 목록이다. 아래 85건은 학술지 26건, 국제 학회 36건, 국내 학회 23건이다. 논문 목록은 2021–2026년 연도 범위이며 2021년 10월 13일 이전 논문도 포함한다. 「게재 승인」 항목은 승인 날짜 없이 누리집에 적힌 2026년을 따랐다. 학회 항목은 랩 게시 발표 목록이며, 정식 출판 논문과 구분해 학회 이름·연도를 적었다.[^journal][^conference]

**2026**

- "Electrical injection of meron-antimeron pairs into a magnetic domain wall", Jiseok Yang, Taekhyeon Lee, San Ko, Soogil Lee, Mincheol Shin, Kyoung-Woong Moon, Sanghoon Kim, SeKwon Kim, Kab-Jin Kim, npj Spintronics, 게재 승인 (누리집 2026년 표기, 승인 날짜 없음)
- "Oxide Interlayer Engineering in Self-Rectifying Ferroelectric Tunnel Junctions: Oxygen Reservoir Effect on Interface Passivation and Memory Reliability", Paul Gallegos, Sohyeon An, Seungyeon Chang, Jae-hyeon Cho, Hunbeom Shin; Seokwon Lee, Sang-hee Ko Park, Mincheol Shin, Jinho Ahn, and Sanghun Jeon, ACS Applied Electronic Materials, September. 2026
- "Multilevel/Layer FeFET With Polar Topological States: Four-Coupled Multiphysics Simulations", Yangjin Jung, Hyeongu Lee, and Mincheol Shin, IEEE Transactions on Electron Devices, April. 2026.
- "Antiferroelectric-Expanded, Strain-Coupled Multiphysics Phase-Field Model and its applications", Yangjin Jung and Mincheol Shin, Conference on Computational Physics (CCP), Seoul, Korea, 2026
- "Analysis of Gate Leakage Current in AlGaN/AlN/GaN HEMTs Using a Three-Terminal NEGF Approach ",Heonseok Oh, Jooseok Kim, Phil-Hun Ahn and Mincheol Shin, Conference on Computational Physics (CCP), Seoul, Korea, 2026
- "Neural-Network-Based Quantum Transport Simulations of Cation-Disordered c-IGZO ",Jooseok Kim\*, Guenseok Choi\*, and Mincheol Shin (\* Equal Contribution), Conference on Computational Physics (CCP), Seoul, Korea, 2026
- "Quasi-Bound State Tunneling in GaN Devices using 2D NEGF with Supercell Mode-Space Method", Heonseok Oh, Phil-Hun Ahn, Jooseok Kim and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Kumamoto, Japan, 2026
- "Alloy-scattering-limited Hole Mobility in SiGe: First-principles-based Multi-scale Approach", Gyeongwon Roh, Yeongjun Lim, and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Kumamoto, Japan, 2026
- "Three-Dimensional Quantum Transport in Nanosheet FETs: Effects of Contacts, Geometry, and Multi-Stacks", Seungjin Lee, Soyeon Park, Seunghyun Song, and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Kumamoto, Japan, 2026
- "Neural-Network-Based Effective-Mass Hamiltonian for Quantum Transport Simulations of Disordered Devices", Guenseok Choi\*, Jooseok Kim\*, Gyeongwon Roh, and Mincheol Shin (\* Equal Contribution), International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Kumamoto, Japan, 2026
- "Antiferroelectric-Expanded, Strain-Coupled Multiphysics Phase-Field Model and Its Applications", 정양진, 신민철, 제 2회 계산전자공학 학술대회, 서울, 2026.
- "QBS-Assisted Gate Leakage Analysis in GaN Devices Using Three-Terminal 2D NEGF", 오헌석, 신민철, 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Neural-Network Tight-Binding Molecular Dynamics for Large-Scale Atomistic Simulations", 최근석, 신민철, 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Large-Scale Three-Dimensional Quantum Transport Simulations of Nanosheet FETs", 이승진, 박소연, 송승현, 신민철, 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Alloy-Scattering-Limited Hole Mobility in SiGe Based on First-Principles Multi-Scale Simulation", 노경원, 신민철 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Oxide semiconductor Grain boundary limited resistivity and mobility calculation based on Density Functional Theory," 유일한, 임영준, 이주희, 김록연, 조영미, 김현득, 신민철 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Efficient Quantum Transport Simulation of Cation-Disordered c-IGZO Using Neural-Network," 김주석, 최근석, 신민철, 제 2회 계산전자공학 학술대회, 서울, 2026.
- "Beyond the Perfect-Metal Assumption: A 3D Phase Field Simulation Framework with Thomas–Fermi Electrode Screening for FTJs." 이석원, 신민철, 제 33회 한국반도체학술대회, 정선, 2026.

**2025**

- "Engineering Negative Capacitance in Hf0.5Zr0.5O2 for Low-Power and Reliable Charge Trap Flash Memory" Yunseok Nam, Sangho Lee, Yangjin Jung, Kang Kim, Jihye Ok, Jinwook Ha, Heemiin Yoon, Mincheol Shin Sanghee Park, and Sanghun Jeon, ACS Applied Materials & Interfaces, 2025
- "Stabilized negative capacitance for near-theoretical efficiency and high reliability in charge trap flash memory" Lee Sangho, Kim Giuk, Nam Yunseok, Jeong Yangjin, Kang Hyunjun, Kim Woongjin, Shin Hunbeom, Shin Mincheol, Park Sanghyun, Seo Kwangyou, Kim Kwangsoo, Kim Wanki, Ha Daewon, Ahn Jinho, and Jeon Sanghun, Materials Today Physics, August. 2025
- "Middle Interlayer Engineered Ferroelectric NAND Flash Overcoming Reliability and Stability Bottlenecks for Next-Generation High-Density Storage Systems", Giuk Kim, Sangho Lee, Hyojun Choi, Yangjin Jung, Woongjin Kim, Sanghyun Park, Kwangyou Seo, Kwangsoo Kim, Wanki Kim, Daewon Ha, Mincheol Shin, Jinho Ahn, Sanghun Jeon, ADVANCED SCIENCE, e10155, August. 2025.
- "Effects of Gate Offset on Negative Capacitance Field-Effect Transistors With Self-Heating Effect", Yangjin Jung, Hyeongu Lee, and Mincheol Shin, IEEE Transactions on Electron Devices, vol 72, no. 6, June. 2025.
- "Nonvolatile Capacitive Synapse Utilizing Polar Topological States for Computing In-Memory", Hyeongu Lee and Mincheol Shin, IEEE Transactions on Electron Devices, vol 72, no. 5, May. 2025.
- "Improvement of Switching Performance of RRAM Through Protruding Top Electrode and Utilizing Surface Roughness: Multiphysics Simulations", Jeongwhan Jang and Mincheol Shin, IEEE Transactions on Electron Devices, vol 72, pp. 253-258, Jan. 2025.
- "Large-scale Quantum Simulations Enabled By Real-space-equivalent SuperMS Method", Mincheol Shin, 71th IEEE International Electron Devices Meeting (IEDM), SF, USA, 2025
- "Advancing Atomistic Simulations of Realistically Sized Devices: SuperMS, Full-Charge Treatment, and Disorder Modeling", Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Grenoble, France, 2025 (invited)
- "Efficient Quantum-Mechanics-Based Molecular Dynamics Through Machine Learning-Driven Density Functional Theory Hamiltonian", Guenseok Choi and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Grenoble, France, 2025
- "Optimizing Grain Boundary Doping in Molybdenum Interconnects: A Frist-Principle Study," Yeongjun Lim and Mincheol Shin, International Interconnect Technology Conference (IITC), Busan, Korea, 2025
- "Robust Mode Space Method for Heterostructure Transport Enabled by Machine Learning Approach," Yeongjun Lim and Mincheol Shin, International Workshop on Computational Nanotechnology (IWCN), UT, USA, 2025
- "Site-specific analysis of grain boundary doping in Mo interconnects for resistivity reduction," 오헌석, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Amorphous IGZO Mobility Calculation Based on Density Functional Theroy," 유일한, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Efficient Quantum-Mechanics-Based Molecular Dynamics Through Machine Learning-Driven Density Functional Theory Hamiltonian," 최근석, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Analysis of Electrical Characteristics in AlGaN/GaN HEMTs Using First-Principles and Transport Simulations," 김주석, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Amorphous IGZO Mobility Calculation Based on Model Hamiltonian and Cation Potential," 노경원, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Multiscale Investigation of Metal–Ferroelectric Interfaces: From First-Principles to 3D Phase-Field Simulation," 이석원, 신민철, 제 1회 계산전자공학 학술대회, 대전, 2025.
- "Four-coupled Multi-physics Simulations of Multi-layer Ferroelectric Field Effect Transistors with Polar Topological States," 정양진, 이석원, 신민철, 제 32회 한국반도체학술대회, 정선, 2025.

**2024**

- "SemiH: DFT Hamiltonian Neural Network Training with Semi-supervised Learning", Guenseok Choi, Yucheol Cho, Gyeongdo Ham, Mincheol Shin, and Daeshik Kim, Machine Learning: Science and Technology, vol. 5, p. 035060, Sep. 2024.
- "Multi-level storage in cleaved-gate ferroelectric FETs investigated by 3D phase-field-based quantum transport simulation", Jeonghwan Jang, Hyeongu Lee, and Mincheol Shin, Solid-State Electronics, vol. 216, p. 108928, Mar. 2024.
- "Transport Properties of Crystalline IGZO Channel Devices: Effects of Cation Disorders, Composition and Dimensions", Deokhwa Seo, Seung Hyo Han, Jun-Hwe Cha, Seiyon Kim and Mincheol Shin, 70th IEEE International Electron Devices Meeting (IEDM), SF, USA, 2024
- "Unveiling the Origin of Disturbance in FeFET and the Potential of Multifunctional TiO2 as a Breakthrough for Disturb-Free 3D NAND Cell: Experimental and Modeling", Giuk Kim, Hyunjun Kang, Sangho Lee, Hyojun Choi, Yangjin Jung, Mincheol Shin, Kwangsoo Kim, Suhwan Lim, Mintae Ryu, Jongho Woo, Wanki Kim, Daewon Ha, Jinho Ahn, and Sanghun Jeon, 70th IEEE International Electron Devices Meeting (IEDM), SF, USA, 2024
- "Design Methodology for Low-Voltage Operational (≤1 V) FRAM Cell Capacitors and Approaches for Overcoming Disturb Issues in 1T-nC Arrays: Experimental & Modeling", Sangho Lee, Giuk Kim, Chaeheon Kim, Yangjin Jung, Yunseok Nam, Jeonghyun Hwang, Mincheol Shin, Youngin Goh, Mintae Ryu, Jihye Suh, Kilho Lee, Wanki Kim, Daewon Ha, Jinho Ahn, and Sanghun Jeon, 70th IEEE International Electron Devices Meeting (IEDM), SF, USA, 2024
- "Cation Disorder Limited IGZO Mobility Calculation Based on the Density Functional Theory", Seung Hyo Han, Deokhwa Seo, Jun-Hwe Cha, Seiyon Kim and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), San Jose, USA, 2024
- "Doping Effects in Grain Boundaries of Tungsten: Insights from First-Principle Study," Yeongjun Lim and Mincheol Shin, International Interconnect Technology Conference (IITC), San Jose, USA, 2024
- "Effects of the Gate Offset on Gate-all-around Negative Capacitance Field Effect Transistors with Self-heating Effect", 정양진, 이현구, 신민철, 제 31회 한국반도체학술대회, 경주, 2024.
- "Cation Disorder Limited IGZO Mobility Calculation based on Density Functional Theory", 한승효, 서덕화, 신민철, 제 31회 한국반도체학술대회, 경주, 2024.
- "Switching Performance Improvements of RRAM by Applying Protruding Top Electrode and Utilizing Surface Roughness: Multi-physics Simulations", 장정환, 신민철, 제 31회 한국반도체학술대회, 경주, 2024.

**2023**

- "A Novel Neural-Network Device Modeling based on Physics-informed Machine Learning", Bokyeom Kim and Mincheol Shin, IEEE Transactions on Electron Devices, vol. 70, no.11, 6021 - 6025, Nov. 2023.
- "Circuit-Level Memory Cell Simulation of Magnetic Bloch Line Racetrack Memory," Chanhyeong Lee, Kabjin Kim, and Mincheol Shin, IEEE Transactions on Magnetics, Jun. 2023.
- "Efficient device simulations using density functional theory Hamiltonian and non-equilibrium Green’s function: heterostructure mode space method and core charge approximation," Seonghyeok Jeon and Mincheol Shin, Journal of Computational Electronics, May 2023.
- "Performance Boost of Si TFETs by Insertion of III-V Dipole Formation Layer: A First Principle Study," Yeongjun Lim, Junbeom Seo, and Mincheol Shin, IEEE Transactions on Electron Devices, vol. 70, no. 6, June 2023.
- "Ferroelectric nanopillar field-effect transistors: Quantum transport simulations based on a three-dimensional phase-field", Hyeongu Lee, Yoon-suk Kim, and Mincheol Shin, Physical Review Applied, vol. 19, p. 054061, May. 2023
- "A Novel Ferroelectric Nanopillar Multi-level Cell Memory", Hyeongu Lee and Mincheol Shin, Solid-State Electronics, vol. 200, p. 108535, Feb. 2023
- "DFT Hamiltonian Neural Network Training with Semi-supervised Learning," Guenseok Choi, Yucheol Cho, Gyeongdo Ham, Mincheol Shin, and Dae-Shik Kim, Machine Learning and the Physical Sciences Workshop, NeurIPS, New Orleans, USA, December, 15, 2023
- "Three-dimensional phase-field based quantum transport simulations of polar topological states," Hyeongu Lee and Mincheol Shin, 69th IEEE International Electron Devices Meeting (IEDM), SF, USA, 2023
- "Highly Efficient Atomistic Simulations of Laterally Inhomogeneous Devices Using the Non-equilibrium Green’s Function Method," Mincheol Shin and Seonghyeok Jeon, IEEE NMDC 2023, Paestum, Italy, 2023.10.22. - 10.25. (invited)
- "A Novel Machine-Learning Based Mode Space Method for Efficient Device Simulations," Yeongjun Lim and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Kobe, Japan, 2023
- "Coupled Multiple Physics-informed Deep Operator Networks for Boltzmann Transport Simulations of Nanowire Field Effect Transistors," Bokyeom Kim, and Mincheol Shin, 7th IEEE Electron Devices Technology and Manufacuring (EDTM) Conference 2023, Coex, Seoul, Korea, 2023
- "Semiconductor Device Modeling By Utilizing Physics-informed Machine Learning," Bokyeom Kim, and Mincheol Shin, 2023 KSIAM Spring Conference, Alpensia, Pyeong Chang, Korea, 2023.
- "Multi-physics Boltzmann Transport Simulation in Nanowire by coupling multiple Physics-informed Deep Operator Networks_Bokyeom Kim," 김보겸,신민철, 제 30회 한국반도체학술대회, 정선, 2023.
- "Multi-Level Storage in Cleaved-Gate Ferroelectric FETs Investigated by 3D Phase-Field Based Quantum Transport Simulation," 장정환, 이현구, 신민철, 제 30회 한국반도체학술대회, 정선, 2023.
- "Reduction of Device Hamiltonian with Automatic Differentiation," 임영준, 신민철, 제 30회 한국반도체학술대회, 정선, 2023.

**2022**

- ”Efficient Atomistic Simulations of Lateral Heterostructure Devices with Metal Contacts,” Mincheol Shin, Seonghyeok Jeon, and Kanghyun Joo, Solid-State Electronics, vol. 198, 108456, Dec. 2022
- "DFT-NEGF Simulation Study of Co 2 FeAl-MgO-Co 2 FeAl Magnetic Tunnel Junctions Under Biaxial Strain", Seongcheol Noh, Stefano Sanvito, and Mincheol Shin, IEEE Transactions on Magnetics, Vol. 58, No.5 , 2022.
- "Tight-binding based Hamiltonian generation simulator for crystal structure using machine learning", Geunseok Choi and Mincheol Shin, Nano Korea 2022, Kintex, Ilsan, Korea, 2022
- "Electron Transport Properties of Monatomic Phase-change Memory: A First-Principles Study", Kanghyun Joo and Mincheol Shin, Nano Korea 2022, Kintex, Ilsan, Korea, 2022
- "Data-free Physics-informed Neural Networks for Boltzmann Transport Equation," Bokyeom Kim, and Mincheol Shin, Nano Korea 2022, Kintex, Ilsan, Korea, 2022
- "Efficient Atomistic Simulations of Lateral Heterostructure Devices with Metal Contacts", Mincheol Shin and Kanghyun Joo, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Granada, Spain, 2022.
- "A novel ferroelectric nanopillar multi-level cell memory", Hyeongu Lee and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Granada, Spain, 2022.
- "Short Channel Effects Induced by Multi-domain in Negative Capacitance Field-Effect Transistors: A Phase-field based Quantum Transport Study," 이현구, 신민철, 제29회 한국반도체학술대회, 정선, 2022

**2021**

- "Critical switching current density of magnetic tunnel junction with shape perpendicular magnetic anisotropy through the combination of spin-transfer and spin-orbit torques", Doo Hyung Kang and Mincheol Shin, Sci. Rep., Nov., 2021.
- "First-Principles-based Quantum Transport Simulations of Interfacial Point Defect Effects on InAs Nanowire Tunnel Field-Effect Transistors", Hyeongu Lee, Yucheol Cho, Seonghyeok Jeon, and Mincheol Shin, IEEE Transctions on Electron Devices, vol. 68, no. 11, pp. 5901 - 5907, Nov. 2021.
- "Racetrack memory based on current-induced motion of topological Bloch lines," Jiseok Yang, Kyoung-Woong Moon, Albert Park, Soogil Lee, Doo Hyung Kang, Mincheol Shin, Sanghoon Kim and Kab-Jin Kim, Applied Physics Express, vol. 11, no. 10, Sept. 2021.
- "Hetero-structure Mode Space Method for Eﬃcient Device Simulations," Mincheol Shin, J. Appl. Phys., vol. 130, 104303, Sep. 2021.
- "Bayesian Optimization of MOSFET Devices Using Effective Stopping Condition", Bokyeom Kim and Mincheol Shin, IEEE Access, vol. 9, 108480-108494, Aug. 2021.
- "Critical switching current of a perpendicular magnetic tunnel junction owing to the interplay of spin-transfer and spin-orbit torque." Doo Hyung kang, Ji-Hun Byun, and Mincheol Shin, Journal of Physics D: Applied Physics, vol 54, 435001, Aug. 2021.
- "Switching performance comparison between conventional SOT and STT-SOT write schemes with effect of shape deformation," Jihun Byun, Doo Hyung Kang, and Mincheol Shin, AIP Advances, vol. 11, 015035, Jan. 2021.
- "Quantum Transport Simulations of Short Channel Effects Induced by Domain Interfactions in Ferroelectric FETs", Hyeongu Lee and Mincheol Shin, International Conference on Simulation of Semiconductor Process and Devices (SISPAD), Dallas, TX, USA, 2021.
- "Band-Engineering of Silicon Tunnel Field Effect Transistor: A First Principle Study", Yeongjun Lim, Junbeom Seo, and Mincheol Shin, Nano Korea 2021, Kintex, Ilsan, Korea, 2021
- "Effects of the Temperature on the Performance of Double-Gate Negative Capacitance Field-Effect Transistors", Hyeongu Lee and Mincheol Shin, Nano Korea 2021, Korea, 2021
- "Comparative study of excess charge approach and electron only approach: DFT based NEGF simulation," Seonghyeok Jeon and Mincheol Shin, Nano Korea 2021, Ilsan, Korea, 2021
- "Bayesian optimization of 3-nm node nanosheet FETs," Bokyeom Kim, and Mincheol Shin, Nano Korea 2021, Kintex, Ilsan, Korea, 2021
- "DFT-NEGF study of biaxial strain effects on Co2FeAl-based magnetic tunnel junctions", Seongcheol Noh and Mincheol Shin, IWCN2021, Daejeon, Korea, Virtual conference, 2021
- "Interfacial trap effects in InAs gate-all-around nanowire tunnel field-effect transistors: first-principles-based approach", Hyeongu Lee, Yucheol Cho, Seonghyeok Jeon, and Mincheol Shin, IWCN2021, Daejeon, Korea, Virtual conference, 2021
- "Effects of Thin Dipole Layer in Silicon Tunnel Field Effect Transistors", Yeongjun Lim, Junbeom Seo, and Mincheol Shin, IWCN2021, Daejeon, Korea, Virtual conference, 2021
- "Efficient machine-learning-based optimization of 3-nm node nanosheet FETs," Bokyeom Kim, and Mincheol Shin, IWCN2021, Daejeon, Korea, 2021

## 특허

임영준 개별 소개에 출원일이 2021-10-13–2026-10-13에 드는 것으로 게시된 2건이다. 번호와 출원일은 랩 표기다.[^a153]

- Tunneling Field Effect Transistor and Semiconductor Device Including the Same (국가 미국; 등록번호 11990533; 출원일 2022.03.22; 발명자 신민철, 임영준, 서준범)
- 효율적인 반도체 소자의 특성 시뮬레이션 방법 (국가 대한민국; 출원번호 10-2024-0120508; 출원일 2024.09.05; 발명자 신민철, 임영준)

## 소식

첫 화면 Latest News에 게시된 연구 성과·행사 소식이다. 날짜는 원문에 적힌 연·월이다.[^home]

- 2026-09 · 노경원의 연구가 IEEE 국제전자소자학회(IEDM)에 채택됐다.
- 2026-07 · CNL 논문 4편이 반도체 공정·소자 시뮬레이션 국제학회(SISPAD)에 채택됐다.
- 2026-07 · 제2회 계산전자공학 워크숍(KWCE)을 개최했다.
- 2025-12 · 신민철 교수의 논문이 IEEE 국제전자소자학회(IEDM)에 채택됐다.
- 2025-09 · 신민철 교수가 SISPAD 워크숍에서 초청 강연을 했다.
- 2025-07 · 제1회 계산전자공학 워크숍(KWCE)을 개최했다.
- 2024-12 · 삼성미래기술육성재단의 연구비 지원에 선정됐다.
- 2024-12 · 서덕화의 연구가 IEEE 국제전자소자학회(IEDM)에 채택됐다.
- 2024-12 · 정양진의 연구가 IEEE 국제전자소자학회(IEDM)에 채택됐다.
- 2023-09 · 이현구의 연구가 IEEE 국제전자소자학회(IEDM)에 채택됐다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 전기및전자공학부동 E3-2, 5216호[^home]
- 연구실 전화: +82-42-350-7619[^home]
- 교수 이메일: mshin@kaist.ac.kr[^prof]
- 학과 교수 소개의 위치: 전기및전자공학부동 E3-2, 서 6204호, 내선 7418[^ee]
[^home]: CNL, Home, 연구 소개·Latest News·연락처. <https://cnl.kaist.ac.kr/home> 관측 2026-10-26.
[^mosfet]: CNL, Advanced MOSFET, 구조·재료와 자체 양자 수송 계산 연구. <https://cnl.kaist.ac.kr/research/adv_mosfet> 관측 2026-10-26.
[^memory]: CNL, Novel Memory Devices, 강유전체·자성 메모리와 자체 다중물리 계산 연구. <https://cnl.kaist.ac.kr/research/spin> 관측 2026-10-26.
[^method]: CNL, Methodology, 원자 수준 전자 구조·양자 수송 계산 도구와 기계학습 기반 최적화. <https://cnl.kaist.ac.kr/research/method> 관측 2026-10-26.
[^prof]: CNL, Mincheol Shin, 학력·경력·연구 분야. <https://cnl.kaist.ac.kr/members/professor/mincheol-shin> 관측 2026-10-26.
[^ee]: KAIST 전기및전자공학부, 신민철 교수 소개. <https://ee.kaist.ac.kr/professor/12212/> 관측 2026-10-26.
[^staff]: CNL, Research Staff와 Phil-Hun Ahn 소개. <https://cnl.kaist.ac.kr/members/research_staff> <https://cnl.kaist.ac.kr/members/research_staff/philhun-ahn> 관측 2026-10-26.
[^students]: CNL, Students, 박사과정·석사과정 명단. <https://cnl.kaist.ac.kr/members/students> 관측 2026-10-26.
[^alumni]: CNL, Alumni. <https://cnl.kaist.ac.kr/members/alumni> 관측 2026-10-26.
[^journal]: CNL, Journal, 학술지와 그 밖의 학술지 목록. <https://cnl.kaist.ac.kr/publication/Journal> 관측 2026-10-26.
[^conference]: CNL, Conference, 국제·국내 학회 목록. <https://cnl.kaist.ac.kr/publication/Conference> 관측 2026-10-26.
[^a112]: CNL, Phil-Hun Ahn 개별 소개. <https://cnl.kaist.ac.kr/members/research_staff/philhun-ahn> 관측 2026-10-26.
[^a114]: CNL, Geunseok choi 개별 소개. <https://cnl.kaist.ac.kr/members/students/geun-seok-choi> 관측 2026-10-26.
[^a115]: CNL, Yangjin Jung 개별 소개. <https://cnl.kaist.ac.kr/members/students/yangjin-jung> 관측 2026-10-26.
[^a116]: CNL, Ilhan Yu 개별 소개. <https://cnl.kaist.ac.kr/members/students/ilhan-yu> 관측 2026-10-26.
[^a117]: CNL, Heonseok Oh 개별 소개. <https://cnl.kaist.ac.kr/members/students/heonseok-oh> 관측 2026-10-26.
[^a118]: CNL, Joo Seok Kim 개별 소개. <https://cnl.kaist.ac.kr/members/students/joo-seok-kim> 관측 2026-10-26.
[^a119]: CNL, Gyeongwon Roh 개별 소개. <https://cnl.kaist.ac.kr/members/students/gyeongwon-roh> 관측 2026-10-26.
[^a120]: CNL, Seungjin Lee 개별 소개. <https://cnl.kaist.ac.kr/members/students/seungjin-lee> 관측 2026-10-26.
[^a121]: CNL, Soyeon Park 개별 소개. <https://cnl.kaist.ac.kr/members/students/soyeon-park> 관측 2026-10-26.
[^a122]: CNL, Youngmin Wee 개별 소개. <https://cnl.kaist.ac.kr/members/students/youngmin-wee> 관측 2026-10-26.
[^a123]: CNL, Namgung Yunkyeong 개별 소개. <https://cnl.kaist.ac.kr/members/students/namgung-yunkyeong> 관측 2026-10-26.
[^a125]: CNL, Hyun Whan Choi 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/hyunwhan-choi> 관측 2026-10-26.
[^a126]: CNL, Chi-yui Ahn 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/chi-yui-ahn> 관측 2026-10-26.
[^a127]: CNL, Tran Le Anh Tuan 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/tran-le-anh-tuan> 관측 2026-10-26.
[^a156]: CNL, Ju Young Jung 개별 소개. <http://cnl.kaist.ac.kr/members/alumni/juyoung-jung> 관측 2026-10-26.
[^a128]: CNL, Won Chul Choi 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/wonchul-choi> 관측 2026-10-26.
[^a129]: CNL, Kihoon Park 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/kihoon-park> 관측 2026-10-26.
[^a130]: CNL, Yo Lum Lee 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/yolum-lee> 관측 2026-10-26.
[^a131]: CNL, Ho-Won Choi 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/howon-choi> 관측 2026-10-26.
[^a132]: CNL, Jaehyun Lee 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/jaehyun-lee> 관측 2026-10-26.
[^a133]: CNL, Sangchun Park 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/sangchun-park> 관측 2026-10-26.
[^a134]: CNL, Seung Heon Baek 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seunghun-baek> 관측 2026-10-26.
[^a135]: CNL, Hyo-Eun Jung 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/hyoeun-jung> 관측 2026-10-26.
[^a136]: CNL, Sungwoo Jung 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seongwoo-jung> 관측 2026-10-26.
[^a137]: CNL, Moonhoi Kim 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/moonhoi-kim> 관측 2026-10-26.
[^a138]: CNL, Yongsoo Ahn 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/yongsoo-ahn> 관측 2026-10-26.
[^a139]: CNL, Woojin Jeong 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/woojin-jeong> 관측 2026-10-26.
[^a140]: CNL, Yucheol Cho 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/yucheol-cho> 관측 2026-10-26.
[^a141]: CNL, Jihun Byun 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/jihun_byun> 관측 2026-10-26.
[^a142]: CNL, Junbeom Seo 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/junbeom-seo> 관측 2026-10-26.
[^a143]: CNL, Seongcheol Noh 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seongcheol-noh> 관측 2026-10-26.
[^a144]: CNL, Chan-Hyeong Lee 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/chan-hyeong-lee> 관측 2026-10-26.
[^a145]: CNL, Kang-Hyun Joo 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/kang-hyun-joo> 관측 2026-10-26.
[^a146]: CNL, Seong Hyeok Jeon 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seonghyeok-jeon> 관측 2026-10-26.
[^a147]: CNL, Hyeongu Lee 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/hyeongu-lee> 관측 2026-10-26.
[^a148]: CNL, Bokyeom Kim 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/bokyeom_kim> 관측 2026-10-26.
[^a149]: CNL, Jeong-Hwan Jang 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/jeong-hwan-jang> 관측 2026-10-26.
[^a150]: CNL, Jeong-Ho Oh 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/jeong-ho-oh> 관측 2026-10-26.
[^a151]: CNL, Seung-Hyo Han 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seung-hyo-han> 관측 2026-10-26.
[^a152]: CNL, Gyutae Park 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/gyutae-park> 관측 2026-10-26.
[^a153]: CNL, Yeongjun Lim 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/yeongjun-lim> 관측 2026-10-26.
[^a154]: CNL, Deokhwa Seo 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/deokhwa-seo> 관측 2026-10-26.
[^a155]: CNL, Seokwon Lee 개별 소개. <https://cnl.kaist.ac.kr/members/alumni/seokwon-lee> 관측 2026-10-26.
[^p1]: G. Kim 외, S. Jeon, Advanced Science 12, e10155 (온라인 2025-08-23). <https://doi.org/10.1002/advs.202510155> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202510155> 관측 2026-10-26.
[^p2]: H. Lee, Y.-S. Kim, M. Shin, Physical Review Applied 19, 054061 (온라인 2023-05-18). <https://doi.org/10.1103/PhysRevApplied.19.054061> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.19.054061> 관측 2026-10-26.
[^p3]: M. Shin, Journal of Applied Physics 130, 104303 (2021). <https://doi.org/10.1063/5.0064314> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2107.10511> 관측 2026-10-26.
[^p4]: B. Kim, M. Shin, IEEE Access (2021). <https://ee.kaist.ac.kr/ai-in-device/bayesian-optimization-of-mosfet-devices-using-effective-stopping-condition/> 초록 기준(KAIST 전기및전자공학부 게시 초록). 초록 원문 <https://ee.kaist.ac.kr/ai-in-device/bayesian-optimization-of-mosfet-devices-using-effective-stopping-condition/> 관측 2026-10-26.
[^p5]: Y. Jung, H. Lee, M. Shin, IEEE Transactions on Electron Devices (2026). <https://doi.org/10.1109/ted.2026.3680378> 초록 기준(OpenAlex 등록 초록). 관측 2026-10-26.
[^p6]: Y. Cho 외, D. Kim, Machine Learning: Science and Technology (2024). <https://doi.org/10.1088/2632-2153/ad7227> 초록 기준(Crossref 등록 초록). 관측 2026-10-26.
[^p7]: B. Kim, M. Shin, IEEE Transactions on Electron Devices (2023). <https://doi.org/10.1109/ted.2023.3316635> 초록 기준(OpenAlex 등록 초록). 관측 2026-10-26.
[^p8]: H. Lee, Y. Cho, S. Jeon, M. Shin, IEEE Transactions on Electron Devices (2021). <https://doi.org/10.1109/ted.2021.3112395> 초록 기준(OpenAlex 등록 초록). 관측 2026-10-26.

# 미래반도체기술 연구실 (Future Semiconductor Technology Laboratory, FuST Lab)

**KAIST 신소재공학과 · 김경민 교수**

- 분야: 멤리스터(저항 변화 소자)의 물리와 소재·공정, 모트 전이 소자 기반 뉴로모픽 뉴런과 확률 컴퓨팅, 멤리스터 교차 배열 연산과 엣지 AI 하드웨어, 하드웨어 보안(진성 난수, 암호), 첨단 패키징과 배선 소재(하이브리드 본딩)
- 홈페이지: <https://semi.kaist.ac.kr/>
- 근거와 출처: [FuST Lab 근거 페이지](semi-sources.md)

> 전압을 걸면 저항이 바뀌고 그 상태를 기억하는 "멤리스터"라는 새로운 반도체 소자로, 뇌처럼 계산하는 AI 반도체와 무작위성을 이용하는 보안 칩, 확률 컴퓨터를 만드는 연구실이다. 소자가 내는 열이나 잡음처럼 보통은 없애려는 현상까지 계산에 쓰고, 칩을 쌓아 잇는 첨단 패키징 소재도 연구한다.[^home][^r3][^p1]

## 무엇을 연구하나

연구실의 연구는 네 갈래로 소개된다.[^home] 첫째는 **멤리스터 물리**다. 멤리스터의 저항 변화는 이온이 움직여 전도성 필라멘트가 생기고 끊기는 방식과, 전하가 갇혔다 풀리는 방식으로 나뉘는데, 연구실은 그 기전을 밝혀 물리 모델을 세우고 목적에 맞는 멤리스터를 만든다.[^r1] 둘째는 **멤리스터 소재와 공정**으로, TiOx·TaOx·NbOx·HfOx 같은 산화물 멤리스터의 속도·유지·내구·균일성을 높이고, 원자층 증착 같은 박막 공정과 교차 배열(가로세로로 엇갈린 전극의 교차점마다 소자를 둔 배열)에서 새는 전류를 막는 선택 소자를 연구한다.[^r2]

셋째는 **새로운 멤리스터 소자**다. 트랜지스터 미세화가 한계에 가까워지면서, 연구실은 멤리스터로 차세대 비휘발성 메모리(전원이 꺼져도 데이터가 남는 메모리)인 RRAM(저항 변화 메모리), 메모리 안에서 논리 연산을 하는 소자, 뇌를 닮은 뉴로모픽 소자를 개발한다.[^r3] 대표 논문에서는 모트 전이(온도에 따라 절연체와 금속 사이를 오가는 현상)를 일으키는 NbOx 소자가 내는 열의 시간 변화로 신경세포의 여러 행동을 흉내 내고 열만으로 소자끼리 소통하게 했으며,[^p1] 같은 소자의 잡음 섞인 진동으로 0과 1을 확률적으로 내는 확률 비트와,[^p2] 빠르고 환경 변화에 강한 진성 난수(소자의 타고난 무작위성으로 만든 예측할 수 없는 난수) 발생기를 만들었다.[^p3] 또 무작위 스위칭과 아날로그 저장을 함께 하는 멤리스터로 암호화된 채 계산하는 동형 암호 하드웨어를,[^p4] 휘는 기판 위 멤리스터 교차 배열로 심전도를 실시간 진단하는 엣지 AI를,[^p5] 두 가지 상태를 따로 조절하는 산화물 트랜지스터로 시간 기반 암호를 보였고,[^p6] 생체 지표 농도가 기준값을 넘는지 소자 안에서 바로 판단하는 바이오센서 변환기도 만들었다.[^p8]

넷째는 **첨단 패키징과 배선 소재**다. 웨이퍼 단계 접착 필름, 3차원 적층용 미세 범프 접합, 팬아웃 패키지 몰딩 소재를 개발하고, 미세화로 저항과 신뢰성 문제가 커지는 구리 배선을 대신할 새 배선 소재와 원자층 증착 공정을 찾는다.[^r4] 대표 논문에서는 고분자 절연막을 아르곤 플라즈마로 처리해 구리/고분자 하이브리드 본딩 면을 정밀하게 평탄화했다.[^p7]

## 주요 연구 주제

### 1. 모트 소자와 확률 컴퓨팅

열 동역학 모트 뉴런, 자가 진동 확률 비트, 진성 난수 발생기.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 멤리스터 연산과 보안 하드웨어

동형 암호 하드웨어, 휘는 교차 배열 심전도 진단, 시간 기반 암호 트랜지스터, 문턱 판단 바이오센서.[^p4][^p5][^p6][^p8] 대표 논문 4–6, 8.

### 3. 첨단 패키징

구리/고분자 하이브리드 본딩 평탄화.[^p7] 대표 논문 7.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 김경민 교수가 교신저자(랩 표기 *)인 것에서 연구 갈래를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [Mott neurons with dual thermal dynamics for spatiotemporal computing](https://doi.org/10.1038/s41563-024-01913-0) · Nature Materials | 전자 소자의 열은 보통 냉각으로 없앤다. 소자 안에서 생기는 열의 시간 변화를 설계해 정보를 담고 처리하게 만들었다. 휘는 유기 기판 위 NbOx 모트 뉴런 하나가 모트 전이의 열 동역학과 기판과의 열 상호작용으로 18가지 신경세포 행동을 흉내 냈고, 여러 뉴런이 열만으로 소통하며 그래프 최적화 문제를 최고 수준 디지털 프로세서보다 100만 배 넘게 적은 에너지로 풀었다.[^p1] | 공동 1저자 Gwangmin Kim·Jae Hyun In 등, 교신 Suhas Kumar·김경민 |
| 2 | 2023 | [Probabilistic computing with NbOx metal-insulator transition-based self-oscillatory pbit](https://doi.org/10.1038/s41467-023-43085-6) · Nature Communications | 물류·AI·암호처럼 풀기 어려운(NP-난해) 문제에 확률 비트를 쓰는 확률 컴퓨팅이 주목받는다. NbOx 휘발성 멤리스터 발진기로 스스로 박자를 맞춰 확률 비트를 내는 소자를 만들고, 금속-절연체 전이 부근의 잡음이 확률성을 만든다는 모델을 세웠으며, 이 소자로 만든 볼츠만 머신(확률 비트들이 에너지가 낮은 답을 찾아가게 하는 계산 구조)으로 NP-난해 문제를 풀었다.[^p2] | 1저자 Hakseung Rhee, 교신 김경민 |
| 3 | 2021 | [Self-clocking fast and variation tolerant true random number generator based on a stochastic mott memristor](https://doi.org/10.1038/s41467-021-23184-y) · Nature Communications | 멤리스터의 타고난 무작위성은 해독할 수 없는 하드웨어 보안에 필요한 진성 난수를 만들 수 있다. NbOx 모트 멤리스터의 무작위 진동으로 스스로 박자를 맞추는 난수 발생기를 만들어, 휘발성 멤리스터 방식 가운데 가장 빠른 초당 40 kb 이상을 냈고, 주변 온도와 소자 편차에도 강했다.[^p3] | 공동 1저자 Gwangmin Kim·Jae Hyun In, 교신 김경민 |
| 4 | 2024 | [Stochastic switching and analog-state programmable memristor and its utilization for homomorphic encryption hardware](https://doi.org/10.1038/s41467-024-50592-7) · Nature Communications | 동형 암호는 데이터를 풀지 않고 암호화된 채 계산해 클라우드와 기기 사이의 보안 문제를 없앤다. 몰리브데넘이 움직이는 Pt/Ta2O5/Mo 멤리스터가 무작위로 켜지는 성질로 암호 키를 만들고, 켜진 뒤에는 아날로그 값을 정확히 저장하게 해, 한 소자 안에서 키 생성·암호화·복호화를 메모리 내 연산 방식으로 했다.[^p4] | 1저자 Woon Hyung Cheong, 교신 김경민 |
| 5 | 2025 | [Flexible self-rectifying synapse array for energy-efficient edge multiplication in electrocardiogram diagnosis](https://doi.org/10.1038/s41467-025-59589-2) · Nature Communications | 착용형 전자기기용 엣지 AI는 작고 전력이 적어야 하며 부드러운 기판 위에 만들어야 한다. 폴리이미드 기판 위에 저온 공정의 전하 포획형 멤리스터로 32×32 교차 배열을 만들어 5 mm로 휘어도 안정하게 했고, 실시간 심전도 진단에서 93.5% 정확도를 디지털 방식의 0.3% 에너지로 얻었다.[^p5] | 공동 1저자 Younghyun Lee·Hakseung Rhee·Geunyoung Kim, 교신 Jongwon Lee·김경민 |
| 6 | 2026 | [Dual-State Programmable Oxide Transistor for Time-Based Cryptography](https://doi.org/10.1002/adma.74951) · Advanced Materials | 문턱 전압과 포화 전류를 따로 조절할 수 있고, 하나는 오래 기억하고 다른 하나는 잠깐만 기억하는 산화물 트랜지스터를 만들었다. 이 두 상태의 시간 동역학을 이용해 정해진 시간이 지나야 풀리거나 정해진 시간 안에만 풀리는 시간 기반 암호를 배열 수준에서 보였다.[^p6] | 1저자 Huisu Noh, 교신 김경민 |
| 7 | 2025 | [Chemical Mechanical Polishing of Plasma-Modified Cu/Polymer Interfaces for Advanced Hybrid Bonding](https://doi.org/10.1002/advs.202512611) · Advanced Science | 금속과 절연막을 함께 직접 붙이는 하이브리드 본딩은 차세대 반도체 패키징의 핵심이지만, 고분자 절연막(BCB)은 말랑해서 화학적 기계 연마가 어렵다. 반경화 BCB를 아르곤 플라즈마로 처리해 표면을 단단하게 만들자 연마 속도가 5배 넘게 빨라졌고 구리 표면 거칠기가 51.4 nm에서 3.0 nm로 줄어, 빈틈 없는 본딩을 가능하게 했다.[^p7] | 공동 1저자 Sukkyung Kang·Chansu Jeon, 교신 김경민·Sanha Kim |
| 8 | 2025 | [Demonstration of CMOS-compatible memristor-based electrochemical biosensor transducer with threshold-sensing functionality](https://doi.org/10.1038/s41467-025-66372-w) · Nature Communications | 많은 전기화학 바이오센서는 생체 지표 농도가 정해진 기준을 넘는지로 질병을 판단하는데, 이 판단에 전력을 많이 쓰는 처리 장치가 필요하다. 기준을 넘으면 바로 저항이 바뀌는 TaOx/Ta2O5 멤리스터 변환기로 판단을 소자 안에서 하게 했고, pH 센서와 연결한 바이오센서 시스템을 만들었다.[^p8] | 1저자 Young Joon Kim, 교신 Shinhyun Choi·김경민·Jongwon Lee |

## 교수와 전문 분야

김경민 교수는 서울대 재료공학 학사(2003)와 서울대 나노과학기술 협동과정 석박사통합과정(2008)을 마쳤다. 서울대 반도체공동연구소 박사후연구원(2008–2011), 삼성종합기술원과 삼성전자 반도체연구소 Senior Engineer(2011–2013), 미국 Hewlett Packard Labs Research Scientist(2014–2017)를 거쳐 2017년 11월 KAIST 신소재공학과 부교수로 부임했고, 2026년 3월부터 교수이며 KAIST Chair Professor(2026.03–2029.02)를 맡고 있다. 박사 논문은 TiO2 박막의 단극·양극 저항 변화 모델을 다뤘다.[^prof]

교수 페이지에 적힌 수상으로는 대한민국 과학기술 포장(2026), 2025년 국가연구개발 우수성과 100선 재료/기계 분야 최우수(2025), 과학의 날 과학기술진흥 유공 장관 표창(2025), KAIST 대표 연구성과 10선(2022) 등이 있다.[^prof] 랩 특허 페이지에는 2021년 이후 특허 출원 15건(국내 14건, 미국 1건)과 그 이전 등록 특허 11건(2009–2018년, 미국 10건·국내 1건)이 있다.[^patents]

논문으로 보면 전문 분야는 세 갈래다.

- **모트 전이 소자의 열·잡음 동역학을 이용한 뉴로모픽·확률 컴퓨팅**.[^p1][^p2][^p3]
- **멤리스터 기반 하드웨어 보안과 엣지 AI**.[^p4][^p5][^p6][^p8]
- **첨단 패키징 공정**.[^p7]

## 응용 분야

대표 논문으로 보면 저전력 AI 반도체와 조합 최적화 문제 풀이, 하드웨어 보안 칩과 클라우드 암호, 착용형 의료 기기와 현장 진단 바이오센서, 차세대 반도체 패키징(이종 집적)에 닿아 있다.[^p1][^p2][^p4][^p5][^p7][^p8] 박사 졸업생은 ETRI, IMEC, 율리히 연구소(Forschungszentrum Jülich), 퍼듀대, SK하이닉스, 삼성전자 등으로 진출했다.[^alumni]

## 구성원

2026년 10월 20일 랩 Researchers 페이지 기준이다. 연구 주제는 랩이 적은 태그이고, 이메일은 랩이 적은 학교 주소다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Do Hoon Kim | 박사후연구원 | Neuromorphic, Memristor, Noise | starmr1053@kaist.ac.kr | 2, 5 |
| Min Gu Lee | 박사후연구원 | Neuromorphic, Memristor, TFT | dlalsrn546@kaist.ac.kr | 6 |
| Myeongchan Ko | 박사과정 | Ferroelectric, ALD, Dielectric | rhaudcks7@kaist.ac.kr | 6 |
| Sooyeon Narie Kay | 박사과정 | Memristor, CTM, In-Memory Computing | kay0122@kaist.ac.kr | 5 |
| Yongjun Cho | 박사과정 | Ferroelectric, Memcapacitor | yongjun.cho@kaist.ac.kr |  |
| Eun Young Kim | 박사과정 | Memristor, Memcapacitor | seaut_k17@kaist.ac.kr |  |
| Moongu Choi | 박사과정 | In-Memory Computing | cmgu0708@kaist.ac.kr |  |
| Junho Byun | 박사과정 | Neuromorphic, Thermal Computing | jhbyun@kaist.ac.kr |  |
| Chansu Jeon | 박사과정 | Advanced Packaging, Direct bonding, Hybrid bonding | ddanddu23@kaist.ac.kr | 7 |
| Daehee Kim | 박사과정 | PUF, a-C/a-BN PEALD | daehee0219@kaist.ac.kr |  |
| Junmo Kang | 박사과정 | Neuromorphic, Memristor, Oscillator | csmmy1211@kaist.ac.kr |  |
| Jingyao Yu | 박사과정 | TFT, RRAM, M3D Integration | gyeongwoo0421@kaist.ac.kr | 6 |
| Junyong Lee | 박사과정 | TFT, Heterostructure, Dielectric, 2D Flash | junyong.lee@kaist.ac.kr |  |
| Sumin Lee | 박사과정 | Ferroelectric, Memcapacitor | sumin2409@kaist.ac.kr |  |
| Dongkeon An | 박사과정 | Advanced Packaging, Cu/polymer hybrid bonding | dongkeon17@kaist.ac.kr |  |
| Huisu Noh | 박사과정 | Neuromorphic, CTM, TFT | shgmltn@kaist.ac.kr | 6 |
| Jeehyuk Kim | 박사과정 | Thermal Computing, Non-linear Devices | jeehyuk0819@kaist.ac.kr |  |
| Tae Wook Go | 박사과정 | Memristor, RRAM | dhrkawkas@kaist.ac.kr | 6 |
| Seoeun Jang | 박사과정 | Probabilistic Computing, Oscillator | seoeun@kaist.ac.kr |  |
| Taeha Suh | 박사과정 | Advanced Packaging | taeha.suh@kaist.ac.kr |  |
| Hangyu Cho | 석사과정 | Advanced Packaging, ACF | hangyu.cho@kaist.ac.kr |  |
| Jeong Hyun Jung | 석사과정 | CTM, TFT, ALD, IGZO | jh.jung@kaist.ac.kr |  |
| Hyein Lee | 석사과정 | Advanced Packaging | sj092237@kaist.ac.kr |  |
| Jaeuk Lee | 석사과정 | ALD, Dielectric, RF | jaeuk0302@kaist.ac.kr |  |
| Jeongwoo Lee | 석사과정 | Advanced Packaging, Direct Metal Bonding | jwoolee0513@kaist.ac.kr |  |
| Seungju Lee | 석사과정 | Advanced Packaging | dan05192@kaist.ac.kr |  |
| Gyuseok Jung | 석사과정 | ALD | rbtjr9359@kaist.ac.kr |  |
| Jaehyung Hwang | 석사과정 | Thermal Computing, Oscillator | hjo5812@kaist.ac.kr |  |
| Jinyoung Lee | 석사과정 | ALD, V-NAND HARC Process PE-ALD | leejy2324@kaist.ac.kr |  |
| Juntae Cheong | 석사과정 | Ferroelectric, Memcapacitor | olive0217@kaist.ac.kr |  |
| Junyeong Jeong | 석사과정 | Oscillator, Probabilistic Computing | bluedong0910@kaist.ac.kr |  |
| Yujin Lee | 석사과정 | Neuromorphic, Memristor, RRAM | yujinleee@kaist.ac.kr |  |
| Donghui Bae | 석사과정 | Ferroelectric, Stateful logics | dh.bae@kaist.ac.kr |  |
| Soohyun Hwang | 석사과정 | ALD | hsh010403@kaist.ac.kr |  |
| Seojin Cho | 인턴 | Neuromorphic, Memristor, NbO2-based TS device | seojin5982@kaist.ac.kr |  |
| Jisu Park | 인턴 | Advanced Packaging | jsprk97@kaist.ac.kr |  |
| Jihwan Hwang | TUBE | Thermal Computing | hwangjihwan05@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 이름, 과정, 졸업 연도, 랩이 적은 진로다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 이학승 / Hakseung Rhee | Ph. D. Graduate (2026) | ETRI (Researcher) |
| Alba Martinez | Ph. D. Graduate (2025) | IMEC (Researcher) |
| 박우준 / Woojoon Park | Ph. D. Graduate (2025) | Forschungszentrum Jülich (Post doc.) |
| 장민구 / Min Gu Jang | Ph. D. Graduate (2025) | SK Hynix |
| 이영현 / Younghyun Lee | Ph. D. Graduate (2024) | Purdue University (Post doc.) |
| 김광민 / Gwangmin Kim | Ph. D. Graduate (2024) | Forschungszentrum Jülich (Post doc.) |
| 김근영 / Geunyoung Kim | Ph. D. Graduate (2024) | SK Hynix |
| 송한찬 / Hanchan Song | Ph. D. Graduate (2024) | ETRI (Researcher) |
| 인재현 / Jae Hyun In | Ph. D. Graduate (2024) | Samsung Electronics |
| 박주성 / Juseong Park | Ph. D. Graduate (2024) | Samsung Electronics |
| 정운형 / Woon Hyung Cheong | Ph. D. Graduate (2023) | Samsung Electronics |
| 전재범 / Jae Bum Jeon | Ph. D. Graduate (2023) | Samsung Electronics |
| 노정완 / Jungwan Noh | M. S. Graduate (2026) | Samsung Electronics |
| 황동휘 / DongHwi Hwang | M. S. Graduate (2026) | Samsung Electronics |
| 강병찬 / Byeongchan Kang | M. S. Graduate (2026) | Samsung Electronics |
| 김영재 / Yeongjae Kim | M. S. Graduate (2026) | Samsung Electronics |
| 정정은 / Jungeun Jung | M. S. Graduate (2026) | SK Hynix |
| 박지열 / Jiyul Park | M. S. Graduate (2025) | SK Hynix |
| 주수민 / Su Min Ju | M. S. Graduate (2025) | SK Hynix |
| 김남준 / Nam Jun Kim | M. S. Graduate (2024) | KAIST, MSE (Ph. D. Course) |
| 김명은 / Myeong Eun Kim | M. S. Graduate (2024) | SK Hynix |
| 김정균 / Jungkyun Kim | M. S. Graduate (2023) | Samsung Advanced Institute of Technology (SAIT) |
| 이지윤 / Jiyun Lee | M. S. Graduate (2022) | Samsung Electronics |
| 신형석 / Hyung Seok Shin | M. S. Graduate (2022) | SK Hynix |
| 손명원 / Myeong Won Son | M. S. Graduate (2021) | Samsung Electronics |
| 남현수 / Hyun Soo Nam | M. S. Graduate (2021) | SK Hynix |
| 손서일 / Seoil Son | M. S. Graduate (2021) | Samsung Electronics |
| 안장호 / Jangho An | M. S. Graduate (2020) | Samsung Advanced Institute of Technology (SAIT) |
| 김영석 / Young Seok Kim | M. S. Graduate (2020) |  |

## 최근 논문 목록 (2021–2026)

랩 Journal Papers 페이지의 2021년 이후 논문이다. 저자 이름 뒤 *는 교신저자, †는 공동 1저자를 뜻하는 랩 표기다.[^papers]

**2026**

- Huisu Noh, Min Gu Lee, Hwayoung Kim, Myeongchan Ko, Jungwan Noh, Taewook Go, Jingyao Yu, Sang-Hee Ko Park, Himchan Cho, and Kyung Min Kim\*. "Dual-State Programmable Oxide Transistor for Time-Based Cryptography". *Advanced Materials, Early View, e74951 (2026)*.
- Do Hoon Kim, Seoeun Jang, Hakseung Rhee, Min Gu Lee, Daehee Kim, Taewook Go, Woon Hyung Cheong, Hanchan Song and Kyung Min Kim\*. "Noise-Tunable Memristor Enabling Programmable Probabilistic Neurons for Frequency-Selective Time-Series Signal Encoding". *Advanced Materials, Early View, e74529 (2026)*.
- Hakseung Rhee†, Seoeun Jang†, Tae Wook Go, Woojoon Park, Do Hoon Kim, Gwangmin Kim, Hanchan Song, Younghyun Lee, Junmo Kang, and Kyung Min Kim\*. "NbOx-Based Oscillatory P-trit for Probabilistic Ternary Potts Machine". *Advanced Science, Early View, e76754 (2026)*.
- Min Gu Lee, Geunyoung Kim, Hwa Young Kim, Do Hoon Kim, Hanchan Song, Huisu Noh, Jungwan Noh, Seungwoo Lee, Sang-Hee Ko Park, Himchan Cho\* and Kyung Min Kim\*. "Multimode Oxide-Based Optoelectronic Memtransistor for In-Sensor Vision Processing". *Advanced Functional Materials, Early View, e77205 (2026)*.
- Mingxin Deng, Yinan Wang, Hui Xu, Likang Sun, Lun Lu, Ao Xu, Nuo Xu, Zhiwei Li, Qingjiang Li\* and Kyung Min Kim\*. "Memristive Crossbar Array-based Hardware Framework for Compressed Sensing and Event-Driven Neuromorphic Processing". *Nature Communications, 17, 5717 (2026)*.
- Eun Young Kim, Juseong Park, Sumin Ju, Taeyoung Jeong, Dohyun Kim, Woojoon Park, Myeongchan Ko, Woon Hyung Cheong, Jung-Hae Choi\*, and Kyung Min Kim\*. "Memristive Baffle Systems: Design, Simulation, and Applications". *Advanced Science, 13(23), e23273 (2026)*.

**2025**

- Young Joon Kim, Youna Kwon, Youngwoo Yoo, Kandaswamy Theyagarajan, Sairaman Saikrithika, Aryeong Lee, Nam Ho Bae, Won Chul Lee, Gapseop Sim, Younghyun Lee, See On Park, Hyijae Cho, Min Ho Kang, Youngjoo Kim, Yumin Park, Kyoung G. Lee, Choul Young Kim, Hyoungho Ko, Woo Suk Sul, Seok Jae Lee, Jae Hyuk Ahn, Shinhyun Choi\*, Kyung Min Kim\*, and Jongwon Lee\*. "Demonstration of CMOS-compatible memristor-based electrochemical biosensor transducer with threshold-sensing functionality". *Nature Communications, 16, 10851 (2025)*.
- Batzorig Buyantogtokh†, Eun Young Kim, Sheung Hun Kim, Seongmun Eom, Byung Jin Cho, Kyung Min Kim, and Seungbum Hong\*. "Visualization of grain boundary-mediated domain nucleation and growth in polycrystalline Pb(Zr52Ti48)O3 ferroelectric capacitor". *APL Mater, 13, 111111 (2025)*.
- Sukkyung Kang†, Chansu Jeon†, Juseong Park, Seulah Park, Kyung Min Kim\* and Sanha Kim\*. "Chemical Mechanical Polishing of Plasma-Modified Cu/Polymer Interfaces for Advanced Hybrid Bonding". *Advanced Science, 13, e12611 (2025)*.
- Geunyoung Kim†, Jiyul Park†, Woojoon Park, Myeongchan Ko, Min Gu Lee, Hangyu Cho, and Kyung Min Kim\*. "Band and Field Coengineered Charge Trap Memristor via Au Nanoparticle Layer for Programming Speed Enhancement". *Small Science, 5, e202500309 (2025)*.
- Kyung Seok Woo†, Gwangmin Kim†, Kyung Min Kim\*, Suhas Kumar\*. "Role of heat in post-silicon electronics". *Applied Physics Reviews, 12, 031323 (2025)*.
- Kyung Min Kim, Young-Gyu Yoon, Shinhyun Choi, Sung-Yool Choi, Seunghyup Yoo. "Semiconductor-related research and education at KAIST". *Nature reviews electrical engineering, 2, 592–597 (2025)*.
- Woojoon Park†, Hanchan Song†, Eun Young Kim, Moon Gu Choi, Min Gu Lee, Hakseung Rhee, Gwangmin Kim, Taewook Go, Alba Martinez, Daehee Kim, Junmo Kang, Jae Hyun In, and Kyung Min Kim\*. "Frequency Switching Neuristor for Realizing Intrinsic Plasticity and Enabling Robust Neuromorphic Computing". *Advanced Materials, 37, e02255 (2025)*.
- Alba Martinez†, Younghyun Lee†, Geunyoung Kim, Woojoon Park, Jingyao Yu, Sooyeon Narie Kay, Eun Young Kim, Hakseung Rhee, Do Hoon Kim, and Kyung Min Kim\*. "Higher-Order Temporal Dynamics in Complementary Charge Trap Memristor for High-Dimensional Reservoir Computing". *Advanced Functional Materials, 36, e11469 (2025)*.
- Junyoung Kwon†, Jae Bum Jeon, Min Gu Lee, Serin Jeong, Wonjin Choi, Kyung Min Kim, and Jihyeon Yeom\*. "Enantioselective Se lattices for stable chiroptoelectronic processing media". *Nature Communications, 16(1), 4134 (2025)*.
- Gwangmin Kim†, Jae Hyun In, Hakseung Rhee, Woojoon Park, Hanchan Song, and Kyung Min Kim\*. "Enhancing Johnson-Nyquist Noise for High-Performance Mott memristor-based Oscillatory TRNG". *npj Unconventional Computing, 2(1), 12 (2025)*.
- Younghyun Lee†, Hakseung Rhee†, Geunyoung Kim†, Woon Hyung Cheong, Do Hoon Kim, Hanchan Song, Sooyeon Narie Kay, Jongwon Lee\*, Kyung Min Kim\*. "Flexible Self-rectifying Synapse Array for Energy-efficient Edge Multiplication in Electrocardiogram Diagnosis". *Nature Communications, 16(1), 4312 (2025)*.
- Woon Hyung Cheong†, Geunyoung Kim†, Younghyun Lee, Eun Young Kim, Jae Bum Jeon, Do Hoon Kim, and Kyung Min Kim\*. "A Neuransistor with Excitatory and Inhibitory Neuronal Behaviors for Liquid State Machine". *Advanced Materials, 37, 2419122 (2025)*.
- Junyoung Kwon†, Jae Bum Jeon†, Walber Goncalves Guimaraes Junior, Min Gu Lee, Changhyeon Lee, Geunyoung Kim, Hanchan Song, Woon Hyung Cheong, Sung Gap Im, Andre F. de Moura, Kyung Min Kim\*, Jihyeon Yeom\*. "Chiroferromagnetic Quantum Dots for Chiroptical Synapse (ChiropS)". *Advanced Materials, 37(20), 2415366 (2025)*.
- Mingu Jang†, Hanchan Song, Hae Jin Kim, Jung Ho Yoon, and Kyung Min Kim\*. "Multielement Filament Memristor Enabling Multifunctional Neuromorphic Device". *Advanced Functional Materials, 35, 2423273 (2025)*.
- Myeongchan Ko†, Ji Su Park, Soyun Joo, Seungbum Hong, Jong Min Yuk, and Kyung Min Kim\*. "Direct Growth of Ferroelectric Orthorhombic ZrO2 on Ru by Atomic Layer Deposition at 300 ℃". *Materials Horizons, 12, 565-574 (2025)*.
- [Back Cover] Moon Gu Choi†, Jae Hyun In, Hanchan Song, Gwangmin Kim, Hakseung Rhee, Woojoon Park, and Kyung Min Kim\*. "Demonstration of a novel majority logic in a memristive crossbar array for in-memory parallel computing". *Materials Horizons, 12, 131-140 (2025)*.

**2024**

- Chansu Jeon†, Sukkyung Kang†, Myeong Eun Kim†, Juseong Park, Daehee Kim, Sanha Kim\*, and Kyung Min Kim\*. "Ru passivation layer enables Cu-Cu Direct Bonding at Low Temperatures with Oxidation Inhibition". *ACS Applied Materials & Interfaces, 16 (36), 48481-48487 (2024)*.
- In-Kook Hwang†, Min Gu Lee†, Jae Bum Jeon, Sang Hyun Nam, Daseul Lee, Changhyeon Lee, Junyoung Kwon, Sung-Gap Im, Young-Hoon Kim\*, Kyung Min Kim\*, and Byong-Guk Park\*. "Visible‐Light Chiral Photonic Synapses Based on Hybrid Organic‐Inorganic 2D Perovskites". *Advanced Electronic Materials, 11 (3), 2400525 (2024)*.
- Woon Hyung Cheong†, Jae Hyun In, Jae Bum Jeon, Geunyoung Kim, and Kyung Min Kim\*. "Stochastic Switching and Analog-state Programmable Memristor and its Utilization for Homomorphic Encryption Hardware". *Nature Communications, 15, 6318 (2024)*.
- Do Hoon Kim†, Woon Hyung Cheong†, Hanchan Song, Jae Bum Jeon, Geunyoung Kim, and Kyung Min Kim\*. "Memristive Monte Carlo DropConnect crossbar array enabled by device and algorithm co-design". *Materials Horizons, 11 (17), 4094-4103 (2024)*.
- Gwangmin Kim†, Jae Hyun In†, Younghyun Lee†, Hakseung Rhee, Woojoon Park, Hanchan Song, Juseong Park, Jae Bum Jeon, Thimothy D. Brown, A. Alec Talin, Suhas Kumar\*, and Kyung Min Kim\*. "Mott Neurons with Dual Thermal Dynamics for Spatiotemporal Computing". *Nature Materials, 23, 1237-1244 (2024)*.
- Hanchan Song†, Woojoon Park†, Gwangmin Kim, Moon Gu Choi, Jae Hyun In, Hakseung Rhee, and Kyung Min Kim\*. "Memristive Explainable Artificial Intelligence Hardware". *Advanced Materials, 36 (25), 2400977 (2024)*.
- Hanchan Song†, Min Gu Lee†, Gwangmin Kim, Do Hoon Kim, Geunyoung Kim, Woojoon Park, Hakseung Rhee, Jae Hyun In, and Kyung Min Kim\*. "Fully Memristive Elementary Motion Detectors for a Maneuver Prediction". *Advanced Materials, 36 (18), 2309708 (2024)*.

**2023**

- Hye-In Yeom†, Jingyu Kim, Guk-Jin Jeon, Jeongwoo Park, Dong Uk Han, Joohyeong Kim, Kyung Min Kim, Bonggeun Shong, and Sang-Hee Ko Park\*. "High-performance oxide thin-film diode and its conduction mechanism based on ALD-assisted interface engineering". *Journal of Materials Chemistry C, 11 (4), 1336-1345 (2023)*.
- Hakseung Rhee†, Gwangmin Kim, Hanchan Song, Woojoon Park, Do Hoon Kim, Jae Hyun In, Younghyun Lee, and Kyung Min Kim\*. "Probabilistic computing with NbOx metal-insulator transition-based self-oscillatory pbit". *Nature Communications, 14, 7199 (2023)*.
- Geunyoung Kim†, Younghyun Lee, Jae Bum Jeon, Woon Hyung Cheong, Woojoon Park, Hanchan Song, and Kyung Min Kim\*. "Threshold Modulative Artificial GABAergic Nociceptor". *Advanced Materials, 35 (47), 2304148 (2023)*.
- Jungkyun Kim†, Hakseung Rhee†, Myeong Won Son, Juseong Park, Gwangmin Kim, Jae Bum Jeon, Hanchan Song, Geunwoo Kim, Byong-Guk Park, Jeong Hwan Han\*, and Kyung Min Kim\*. "Electromigration Reliability of Barrierless Ruthenium and Molybdenum for Sub-10 nm Interconnection". *ACS Applied Electronic Materials, 5 (5), 2447–2453 (2023)*.
- Gisu Doo†, Juseong Park, Jeesoo Park, Jiyun Heo, Jinkwan Jung, Dong Wook Lee, Hanmin Bae, Jonghyun Hyun, Euntaek Oh, Jiyun Kwen, Kyung Min Kim, and Hee-Tak Kim\*. "Contact Problems of IrOx Anodes in Polymer Electrolyte Membrane Water Electrolysis". *ACS Energy Letters, 8 (5), 2214–2220 (2023)*.
- Juseong Park†, Sukkyung Kang†, Myeong Eun Kim, Nam Jun Kim, Jungkyun Kim, Sanha Kim\*, and Kyung Min Kim\*. "Advanced Cu/Polymer Hybrid Bonding System for Fine-Pitch 3D Stacking Devices". *Advanced Materials Technologies, 8 (20), 2202134 (2023)*.
- [Cover] Woojoon Park†, Gwangmin Kim, Jae Hyun In, Hakseung Rhee, Hanchan Song, Juseong Park, Alba Martinez, and Kyung Min Kim\*. "High Amplitude Spike Generator in Au Nanodot-Incorporated NbOx Mott Memristor". *Nano Letters, 23 (11), 5399−5407 (2023)*.
- Eun Chong Ko†, Jae Yeon Kim, Hakseung Rhee, Kyung Min Kim, and Jeong Hwan Han\*. "Low-resistivity ruthenium metal thin films grown via atomic layer deposition using dicarbonyl-bis(5-methyl-2,4-hexanediketonato)ruthenium (II) and oxygen". *Materials Science in Semiconductor Processing, 156, 107258 (2023)*.

**2022**

- Geunyoung Kim†, Seoil Son†, Hanchan Song, Jae Bum Jeon, Jiyun Lee, Woon Hyung Cheong, Shinhyun Choi, and Kyung Min Kim\*. "Retention secured nonlinear and self-rectifying analog charge trap memristor for energy-efficient neuromorphic hardware". *Advanced Science, 10 (3), 2205654 (2022)*.
- Juseong Park†, Jungwoo Choi, Gwangmin Kim, Geunyoung Kim, Gil Seop Kim, Hanchan Song, Yeong Seok Kim, Younghyun Lee, Hakseung Rhee, Hyuck Mo Lee, Cheol Seong Hwang, and Kyung Min Kim\*. "Modified dynamic physical model of valence change mechanism memristors". *ACS Applied Materials & Interfaces, 14 (31), 35949-35958 (2022)*.
- Jang Hwan Kim†, Suwan Jeon, Jae Hyun In, Seonho Nam, Hyeong Min Jin, Kyu Hyo Han, Geon Gug Yang, Hee Jae Choi, Kyung Min Kim, Jonghwa Shin, Seung-Woo Son, Seok Joon Kwon\*, Bong Hoon Kim\*, and Sang Ouk KIm\*. "Nanoscale physical unclonable function labels based on block co-polymer self-assembly". *Nature Electronics, 5, 433-442 (2022)*.
- Do Hoon Kim†, Young Seok Kim, Woon Hyung Cheong, Hanchan Song, Hakseung Rhee, Sooyeon Narie Kay, Jin-Woo Han, and Kyung Min Kim\*. "Evolutionary Learning of Binary Neural Network Using a TaOx Memristor via Stochastic Stateful Logic". *Advanced Intelligent Systems, 4 (9), 2200058 (2022)*.
- [Front Cover] Hyung Seok Shin†, Hanchan Song†, Do Hoon Kim, Alba Martinez, Woon Hyung Cheong, and Kyung Min Kim\*. "Multimode Synaptic Operation of a HfAlOx-Based Memristor as a Metaplastic Device for Neuromorphic Applications". *ACS Applied Electronic Materials, 4 (8), 3786–3793 (2022)*.
- [Back Cover] Woon Hyung Cheong†, Jae Bum Jeon†, Jae Hyun In, Geunyoung Kim, Hanchan Song, Jangho An, Juseong Park, Young Seok Kim, Cheol Seong Hwang\*, and Kyung Min Kim\*. "Demonstration of Neuromodulation-inspired Stashing System for Energy-efficient Learning of Spiking Neural Network using a Self-Rectifying Memristor Array". *Advanced Functional Materials, 32 (29), 2200337 (2022)*.

**2021**

- Young Seok Kim†, Jangho An, Jae Bum Jeon, Myeong Won Son, Seoil Son, Woojoon Park, Younghyun Lee, Juseong Park, Geun Young Kim, Gwangmin Kim, Hanchan Song, and Kyung Min Kim\*. "Ternary logic with Stateful Neural Networks using a bilayered TaOx-based memristor exhibiting ternary states". *Advanced Science, 9 (5), 2104107 (2021)*.
- Seong-In Cho†, Jae Bum Jeon, Joo Hyung Kim, Seung Hee Lee, Wooseok Jeong, Jingyu Kim, Geunyoung Kim, Kyung Min Kim\*, and Sang-Hee Ko Park\*. "Synaptic transistors with human brain-like fJ energy consumption via double oxide semiconductor engineering for neuromorphic electronics". *Journal of Materials Chemistry C, 9, 10243-10253 (2021)*.
- Wonkyu Kang†, Kyoungmin Woo, Hyon Bin Na, Chi Jung Kang, Tae-Sik Yoon, Kyung Min Kim, and Hyun Ho Lee\*. "Analog Memristive Characteristics of Square Shaped Lanthanum Oxide Nanoplates Layered Device". *Nanomaterials, 11 (2), 441 (2021)*.
- Gwangmin Kim†, Jae Hyun In†, Young Seok Kim, Hakseung Rhee, Woojoon Park, Hanchan Song, Juseong Park, and Kyung Min Kim\*. "Self-clocking fast and variation tolerant true random number generator based on a stochastic mott memristor". *Nature Communications, 12, 2906 (2021)*.
- Young Seok Kim†, Myeong Won Son, and Kyung Min Kim\*. "Memristive Stateful Logic for Edge Boolean Computer". *Advanced Intelligent Systems, 3(7), 2000278 (2021)*.

## 특허

랩 Patent 페이지의 특허 26건 전체다. 페이지는 2021년 이후 항목을 연도별로, 그 이전 등록분 11건을 "~ 2018" 구역에 따로 싣는다. 이 구역 항목의 연도는 적힌 등록일의 연도다.[^patents]

- 2026 · 출력 보정 장치, 출력 보정 시스템, 및 출력 보정 방법 (발명자 김경민, 장서은; 번호 한국특허출원 2026년 09월 03일 / 10-2026-0167590)
- 2026 · 담금질 기법 연산 장치 및 이의 동작 방법 (발명자 김경민, 김광민, 김대희; 번호 한국특허출원 2026년 07월 22일 / 10-2026-0135136)
- 2026 · 비정질 보론 질화막 형성용 보론 전구체, 비정질 보론 질화막, 및 이의 제조 방법 (발명자 최지유, 김경민, 김대희, 김영재, 황선혜, 박규희; 번호 한국특허출원 2026년 07월 15일 / 10-2026-0130805)
- 2026 · 물리적 복제 방지 기능 연산 장치, 이의 동작 방법, 및 보안 시스템 (발명자 김경민, 김광민, 김대희; 번호 한국특허출원 2026년 07월 13일 / 10-2026-0128513)
- 2026 · 비정질 탄소 박막의 제조 방법 및 비정질 탄소 박막 (발명자 최지유, 김경민, 황선혜, 박규희, 김대희, 김영재; 번호 한국특허출원 2026년 02월 09일 / 10-2026-0025904)
- 2025 · 암호화 소자, 이를 포함하는 암호화 장치, 및 암호화 시스템 (발명자 김경민, 노희수, 이민구, 조힘찬; 번호 한국특허출원 2025년 12월 26일 / 10-2025-0211300)
- 2025 · 수직형 메모리 장치, 그 구동 방법 및 이를 포함하는 전자 장치 (발명자 김유민, 계수연, 김경민, 현승담; 번호 한국특허출원 2025년 09월 05일 / 10-2025-0126883)
- 2025 · 뉴로모픽 회로 유닛 (발명자 김경민, 박우준; 번호 한국특허출원 2025년 02월 24일 / 10-2025-0023309)
- 2024 · 반도체 소자, 이를 포함하는 이미지 처리 장치, 및 이미지 처리 장치의 동작 방법 (발명자 조힘찬, 이재환, 이승우, 김경민, 연성범, 이민구, 김근영; 번호 한국특허출원 2024년 07월 31일 / 10-2024-0101667)
- 2024 · 연마 가공방법 및 연마 가공장치 (발명자 김산하, 김경민, 강석경, 박주성, 전찬수; 번호 한국특허출원 2024년 05월 02일 / 10-2024-0058665)
- 2023 · 반도체 회로 제조방법 (발명자 김산하, 김경민, 강석경, 박주성; 번호 한국특허출원 2023년 10월 18일 / 10-2023-139596)
- 2023 · 저온공정이 가능한 ZrO2 강유전 커패시터 (발명자 김경민, 고명찬; 번호 한국특허출원 2023년 03월 24일 / 10-2023-0038897)
- 2022 · SEMICONDUCTOR MEMORY DEVICE (발명자 김경민, 인재현, 김광민, 이영현; 번호 해외특허출원 (미국) 2022년 10월 28일 / US20230134585A1)
- 2022 · 모트 멤리스터 기반 진성난수생성기 및 진성난수생성방법 (발명자 김경민, 김광민, 인재현; 번호 한국특허출원 2022년 05월 17일 / 10-2022-0060216)
- 2021 · 반도체 메모리 소자 (발명자 김경민, 인재현, 김광민, 이영현; 번호 한국특허출원 2021년 10월 29일 / 10-2021-0146697)
- 2018 · Multilayered memristors (발명자 Warren Jackson, Jianhua Yang, Kyung Min Kim, Zhiyong Li; 번호 해외특허등록 (미국) 2018년 07월 17일 / US10026896B2)
- 2018 · Sensing an output signal in a crossbar array based on a time delay between arrival of a target output and a sneak output (발명자 Kyung Min Kim, Ning Ge, Jianhua Yang; 번호 해외특허등록 (미국) 2018년 04월 03일 / US9934852B2)
- 2017 · Apparatus having first and second switching materials (발명자 Ning Ge, Jianhua Yang, Stanley Williams, Kyung Min Kim; 번호 해외특허등록 (미국) 2017년 10월 17일 / US9793322B2)
- 2016 · Multi-bit memory elements, memory devices including the same, and methods of manufacturing the same (발명자 Chang-Bum Lee, Chang-Jung Kim, Young-Bae Kim, Myoung-Jae Lee, Dong-Soo Lee, Man Chang, Seung-Ryul Lee, Kyung-min Kim; 번호 해외특허등록 (미국) 2016년 11월 01일 / US9484087B2)
- 2015 · Resistive switching devices and memory devices including the same (발명자 Kyung-min Kim, Young-Bae Kim, Chang-Jung Kim, Seung-Ryul Lee, Man Chang, Sung-Ho Kim, Eun-ju CHO; 번호 해외특허등록 (미국) 2015년 10월 6일 / US9153778B2)
- 2015 · Resistive memory devices and methods of operating the same (발명자 Ingyu Baek, Yeong-Taek Lee, Kyungmin Kim; 번호 해외특허등록 (미국) 2015년 09월 08일 / US9129675B2)
- 2015 · Resistance switching material element and device employing the same (발명자 Kyung-min Kim, Young-Bae Kim, Chang-Jung Kim, Sung-Ho Kim, Sae-jin KIM, Seung-Ryul Lee, Man Chang, Eun-ju CHO; 번호 해외특허등록 (미국) 2015년 08월 04일 / US9099639B2)
- 2015 · 2-terminal switching device (발명자 Kyung-min Kim, Young-Bae Kim, Eun-ju CHO; 번호 해외특허등록 (미국) 2015년 06월 02일 / US9048839B2)
- 2015 · Semiconductor devices including variable resistance elements and methods of operating semiconductor devices (발명자 Man Chang, Young-Bae Kim, Dong-Soo Lee, Chang-Bum Lee, Seung-Ryul Lee, Chang-Jung Kim, Myoung-Jae Lee, Kyung-min Kim; 번호 해외특허등록 (미국) 2015년 04월 07일 / US9001551B2)
- 2015 · Nonvolatile memory devices and methods of driving the same (발명자 Man Chang, Young-Bae Kim, Dong-Soo Lee, Chang-Bum Lee, Seung-Ryul Lee, Chang-Jung Kim, Myoung-Jae Lee, Kyung-min Kim; 번호 해외특허등록 (미국) 2015년 02월 03일 / US8947905B2)
- 2009 · 저항변화기록소자, 그 제조방법, 정보기록방법 및정보판독방법 (발명자 황철성, 최병준, 김경민; 번호 한국특허등록 2009년 06월 24일 / 10-0905420-0000)

## 수상

교수 페이지에 적힌 수상이다.[^prof]

- 2026.04 · 대한민국 과학기술 포장
- 2025.12 · 2025년 국가연구개발 우수성과 100선 (재료/기계 분야 – 최우수)
- 2025.11 · 제 15회 에쓰-오일 화학공학/재료공학 부문 우수학위논문상 (지도학생: 김광민 박사)
- 2025.04 · 제 58회 ‘과학의 날’ 과학기술진흥 유공 장관 표창장
- 2024.05 · KAIST Research Day (리서치데이) 14대 미래선도기술: 반도체/디스플레이 분야 선정
- 2022.05 · KAIST’s Top 10 Research Achievements (KAIST 대표 연구성과 10선) [Title: 모트 전이 소재 기반 초고석, 저전력, 변이 내성 진성 난수 발생기 개발]
- 2022.02 · 제 28회 삼성휴먼테크논문대상 장려상
- 2018.10 · SK하이닉스 혁신 아이디어 공모전 우수상

## 연락과 위치

- 교수실: KAIST W1-1동 2403호[^prof]

[^home]: 연구실 누리집 첫 화면 <https://semi.kaist.ac.kr/> (2026-10-20 열람)
[^prof]: Professor 페이지 <https://semi.kaist.ac.kr/member/professor/> (2026-10-20 열람)
[^members]: Researchers 페이지 <https://semi.kaist.ac.kr/students/> (2026-10-20 열람)
[^alumni]: Alumni 페이지 <https://semi.kaist.ac.kr/member/alumni/> (2026-10-20 열람)
[^r1]: Memristive Physics 페이지 <https://semi.kaist.ac.kr/research/physics-in-new-semiconductor-materials/> (2026-10-20 열람)
[^r2]: Memristor Materials & Process 페이지 <https://semi.kaist.ac.kr/research/semiconductor-process-for-memristor/> (2026-10-20 열람)
[^r3]: Emerging Memristive Devices 페이지 <https://semi.kaist.ac.kr/research/emerging-semiconductor-devices/> (2026-10-20 열람)
[^r4]: Materials for Advanced Packaging & Interconnection 페이지 <https://semi.kaist.ac.kr/research/materials-for-advanced-packaging-and-interconnection/> (2026-10-20 열람)
[^papers]: Journal Papers 페이지 <https://semi.kaist.ac.kr/publication_journal/> (2026-10-20 열람)
[^patents]: Patent 페이지 <https://semi.kaist.ac.kr/publication_journal/patent/> (2026-10-20 열람)
[^p1]: G. Kim 외, K. M. Kim, Nature Materials 23, 1237-1244 (온라인 2024-06-18). <https://doi.org/10.1038/s41563-024-01913-0> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Rhee 외, K. M. Kim, Nature Communications 14, 7199 (온라인 2023-11-08). <https://doi.org/10.1038/s41467-023-43085-6> 초록 기준.
[^p3]: G. Kim 외, K. M. Kim, Nature Communications 12, 2906 (온라인 2021-05-18). <https://doi.org/10.1038/s41467-021-23184-y> 초록 기준.
[^p4]: W. H. Cheong 외, K. M. Kim, Nature Communications 15, 6318 (온라인 2024-07-26). <https://doi.org/10.1038/s41467-024-50592-7> 초록 기준.
[^p5]: Y. Lee 외, K. M. Kim, Nature Communications 16, 4312 (온라인 2025-05-09). <https://doi.org/10.1038/s41467-025-59589-2> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: H. Noh 외, K. M. Kim, Advanced Materials, e74951 (온라인 2026-09-10). <https://doi.org/10.1002/adma.74951> 초록 기준.
[^p7]: S. Kang 외, S. Kim, Advanced Science 13, e12611 (온라인 2025-10-29). <https://doi.org/10.1002/advs.202512611> 초록 기준.
[^p8]: Y.-J. Kim 외, J. Lee, Nature Communications 16, 10851 (온라인 2025-12-03). <https://doi.org/10.1038/s41467-025-66372-w> 초록 기준.

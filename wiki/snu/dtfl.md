# 유전박막연구실 (Dielectric Thin Film Laboratory, DTFL)

**서울대학교 공과대학 재료공학부 · 황철성 SNU Special Distinguished Professor (특임석좌교수)**

- 분야: 반도체 메모리, 박막, 산화물 반도체, 메모리 내 연산, 확률 계산
- 대분야: 전기전자·반도체·광학, 소재
- 태그: 메모리 반도체 소자[^prof], 뉴로모픽 소자[^research], 메모리 내 연산[^research], 강유전체[^ferro], 산화물 반도체[^tft], 원자층 증착[^capacitor][^pcm], 유전체 커패시터 소재[^capacitor]
- 홈페이지: <http://dtfl.snu.ac.kr/>
- 근거와 출처: [유전박막연구실 근거 페이지](dtfl-sources.md)

> 정보를 저장하는 반도체 박막과 소자를 만들고, 그 소자 자체로 신경계의 정보 처리와 확률 계산을 구현하는 연구실이다.[^prof][^research]

## 무엇을 연구하나

정보를 저장하는 반도체 메모리와, 저장 소자를 이용한 계산 기술을 함께 연구한다. 소자는 전자 장치에서 특정 기능을 맡는 부품이며, 박막은 두께가 얇은 층 형태의 재료다. 연구실은 재료 선택, 박막을 쌓는 공정, 소자의 동작 원리를 함께 다룬다. 저장과 계산을 담당하는 소자의 재료·구조를 바꾸는 것이 연구의 공통 출발점이다.[^memory]

저장 방식은 전하를 이용하는 방식과 저항을 이용하는 방식으로 나누어 살핀다. 저항은 전류의 흐름을 방해하는 정도를 나타내는 물리량이다. 전원을 끈 뒤에도 정보를 유지하는 비휘발성 메모리에서는 강유전체(외부 전기장을 없애도 전기 분극이 남고, 그 방향을 전기장으로 뒤집을 수 있는 물질), 상변화 재료, 저항 변화 재료를 다룬다. 상변화는 물질의 구조나 상태가 다른 상태로 바뀌는 현상이다.[^prof][^memory]

뉴로모픽 연구는 신경세포와 시냅스의 동작을 본뜬 소자로 정보를 처리하려는 연구다. 연구실은 비휘발성 메모리와 멤리스터(전기적 자극의 이력에 따라 저항 상태가 달라지는 소자)를 이용해 이런 하드웨어를 구현한다. 신경망(서로 연결된 계산 단위들이 정보를 주고받는 계산 모형)을 위한 소자와 시간 정보 처리, 여러 물체의 움직임을 소자의 반응으로 구별하는 기술을 연구한다.[^research][^p2]

메모리 내 연산은 정보를 저장하는 곳 안이나 그 가까이에서 계산하는 방식이다. 연구실은 저항 변화 소자로 논리 계산을 구현하고, 배선의 저항과 전극(전자 소자에 전기를 공급하거나 받아들이는 도체) 구조, 시스템 구성과 신뢰성을 함께 연구한다. 도체는 전하가 자유롭게 이동하여 전류가 흐르는 물질이다. 소자의 확률적인 동작을 이용해 정수의 인수분해 같은 문제를 다루는 확률 계산으로도 연구를 넓히고 있다.[^research][^rram]

## 주요 연구 주제

### DRAM의 저장 구조와 박막 공정

DRAM(Dynamic Random Access Memory)은 저장된 정보를 유지하기 위해 전하를 주기적으로 보충하는 반도체 메모리다. 연구실은 소자를 평면에서 줄이는 방식의 한계를 다루기 위해, 저장 단위를 입체적으로 쌓는 DRAM 구조와 그 제조 공정을 연구한다. 저장 단위의 커패시터(전하를 저장하는 전자 부품), 트랜지스터(전압으로 전류를 조절하는 반도체 소자), 소자 사이 배선을 함께 다룬다.[^dram]

커패시터에서는 전극 사이의 유전체(전기장에 반응해 내부의 전하 분포가 달라지는 절연 재료)와 전극 박막을 연구한다. 루테늄과 산화루테늄 전극, 이산화타이타늄·타이타늄산스트론튬·산화지르코늄 등의 유전체가 대상이다. 도핑(다른 원소를 첨가해 재료의 성질을 조절하는 것), 서로 다른 재료 사이의 계면(맞닿는 경계), 막이 결정화되는 양상을 조절해 누설 전류(의도한 경로 밖으로 흐르는 전류)와 전하 저장 성질을 연구한다.[^capacitor]

입체 구조에 막을 형성하기 위해 원자층 증착(Atomic Layer Deposition, ALD; 원료 기체를 번갈아 공급하고 표면 반응이 일정 수준에서 멈추는 성질을 이용해 막을 쌓는 방법)과 화학 기상 증착(Chemical Vapor Deposition, CVD; 기체 원료의 화학 반응으로 고체 막을 만드는 방법)을 다룬다. 원료를 공급하는 순서와 나누어 공급하는 방식, 막이 처음 자라는 과정, 재료 조성에 따른 전기적 성질을 함께 연구한다.[^capacitor]

### 산화물 반도체 트랜지스터

산화물 반도체는 산소와 다른 원소가 결합한 화합물로 만든 반도체다. 연구실은 인듐·갈륨·아연 산화물과 아연·주석 산화물, 산화주석의 박막 트랜지스터를 연구한다. 비정질(원자들이 전체에 걸쳐 규칙적으로 배열되어 있지 않은 상태) 산화물에서도 전류를 조절할 수 있는 성질을 이용해 디스플레이와 메모리 소자로 연결한다.[^tft]

빛과 전압을 가했을 때 동작이 달라지는 원인, 재료의 조성과 결함(원자 배열이나 조성이 이상적인 상태에서 벗어난 부분), 다른 재료와 맞닿는 층의 영향을 살핀다. 전하를 가두는 플래시 메모리와 DRAM에 사용할 트랜지스터를 연구하며, 산화물 반도체 쓰기 소자와 실리콘 읽기 소자를 위아래로 결합한 커패시터 없는 메모리도 구현했다. 플래시 메모리는 블록 단위로 지우고 다시 쓸 수 있는 비휘발성 반도체 메모리다.[^tft][^p1]

### 강유전체·상변화·저항 변화 메모리

강유전체 연구에서는 산화하프늄과 산화지르코늄을 포함한 박막의 두께, 결정 상태, 계면과 전기장 반복 인가에 따른 성질 변화를 다룬다. 강유전체를 쓰는 트랜지스터와 커패시터의 동작을 해석하고, 물질 안에서 같은 방향으로 전기 분극한 영역들의 변화도 모의실험으로 연구한다.[^ferro]

상변화 메모리는 원자 배열이 규칙적인 결정 상태와 비정질 상태 사이의 전기 저항 차이를 이용해 정보를 저장한다. 연구실은 게르마늄·안티모니·텔루륨 계열 박막의 원자층 증착, 수직형 메모리 구조, 서로 다른 물질층을 반복해 쌓은 구조를 연구한다. 또 특정 전압에서 전류가 흐르는 상태로 바뀌는 선택 소자를 연구해, 배열에서 선택하지 않은 저장 소자로 흐르는 전류를 다룬다. 이 선택 소자의 동작은 상변화 메모리와 달리 결정·비정질 사이의 상변화를 이용하지 않는다.[^pcm]

저항 변화 메모리에서는 전압을 가했을 때 저항이 바뀌는 원리와 이를 조절하는 구조를 연구한다. 구리 공급원의 모양과 소자 내부 구조를 바꾸거나, 전자가 재료 안에 갇히고 빠져나오는 과정을 이용한다. 수직으로 쌓는 메모리, 선택 트랜지스터와 결합한 구조, 소자 안에서 논리 계산을 수행하는 회로도 연구 범위다.[^rram]

### 뉴로모픽 정보 처리와 확률 계산

빛에 반응하는 멤리스터와 자극이 끝난 뒤 반응이 시간에 따라 사라지는 멤리스터를 결합해 물체의 움직임을 처리한다. 소자의 출력이 줄어드는 양상으로 물체가 머문 시간을 나타내고 방향과 속도를 판별한다.[^p2]

리저버 컴퓨팅은 입력에 반응하는 동적 시스템의 상태를 이용해 정보를 처리하고 그 상태를 읽는 부분을 학습하는 계산 방식이다. 그래프(대상과 대상 사이의 연결을 점과 선으로 나타낸 것) 형태의 리저버를 멤리스터로 구현해 입력들의 공간적·시간적 관계를 계산에 쓴다. 크로스바 배열(서로 교차하는 배선 사이에 소자를 놓은 구조)로 그래프의 연결 관계를 표현하고, 소자의 확률적 동작과 배열의 연결 구조를 이용해 그래프 분석과 경로 찾기를 수행한다.[^p3][^p4][^p5]

조합 최적화는 가능한 여러 조합 가운데 목적과 제약에 맞는 답을 찾는 문제다. 확률 계산에서는 계산 단위의 상태가 확률에 따라 달라지는 성질을 이용한다. 연구실은 여러 상태를 갖는 확률 계산 단위를 트랜지스터로 구성하고, 계산 단위 사이의 상호작용을 여러 상태의 변수로 나타내는 포츠 모형(Potts model)을 이용해 조합 최적화 문제를 푸는 시스템을 제안했다.[^p6]

## 대표 논문

서울대 재직 시기의 메모리 소자, 뉴로모픽 정보 처리, 그래프 분석, 확률 계산을 보여 주는 6편이다. 연도는 출판사의 권호 연도이며, 온라인 출판일은 각주에 적었다. ‘쉽게 말하면’은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2025 | [Heterogeneous Capacitor-less Two-transistor Dynamic Random Access Memory Cell with Long Retention Time and High Sensing Current Supporting 5-Bit Multilevel Operation](https://doi.org/10.1002/pssr.202500131) · physica status solidi (RRL) | 쓰기용 산화물 반도체 트랜지스터와 읽기용 실리콘 트랜지스터를 수직으로 결합했다. 두 종류 소자의 특성을 함께 이용해 정보를 유지하고 여러 상태로 읽는 메모리를 만들었다.[^p1] |
| 2 | 2026 | [Memristive Motion-Streak Neuron for Spatiotemporal Multiple Object Detection](https://doi.org/10.1002/adma.74793) · Advanced Materials | 빛에 반응하는 소자와 시간이 지나며 반응이 줄어드는 소자를 결합했다. 물체가 머문 시간을 소자의 출력에 담아 여러 물체의 이동 방향과 속도를 구별했다.[^p2] |
| 3 | 2024 | [Spatiotemporal Data Processing with Memristor Crossbar-Array-Based Graph Reservoir](https://doi.org/10.1002/adma.202309314) · Advanced Materials | 멤리스터에 여러 입력 사이의 관계를 저장하는 그래프 리저버를 제안했다. 시간과 공간에 걸쳐 변하는 입력의 관계를 계산에 이용하고, 시간에 따른 값의 예측과 영상 분류 등에 적용했다.[^p3] |
| 4 | 2024 | [Memristive Crossbar Array-Based Probabilistic Graph Modeling](https://doi.org/10.1002/adma.202403904) · Advanced Materials | 소자마다 동작이 달라지는 특성을 이용해 확률을 갖는 그래프를 표현했다. 실제 소자로 그래프와 확률 계산을 구현하고, 확장한 모형의 모의실험으로 그래프 분석을 수행했다.[^p4] |
| 5 | 2024 | [Cross-Wired Memristive Crossbar Array for Effective Graph Data Analysis](https://doi.org/10.1002/adma.202311040) · Advanced Materials | 소자 배열의 대각선 부분과 나머지 부분을 교차 연결해 그래프를 물리적으로 표현했다. 연결 상태가 변하는 그래프에서 경로를 찾고, 단백질 사이의 연결 관계를 분석하는 데 적용했다.[^p5] |
| 6 | 2026 | [Multi-State Probabilistic Computing Using Floating-Body MOSFETs Based on the Potts Model for Solving Complex Combinatorial Optimization Problems](https://doi.org/10.1002/adma.202516797) · Advanced Materials | 여러 상태를 갖는 확률 계산 단위를 트랜지스터로 만들고 포츠 모형을 이용하는 시스템을 제안했다. 계산 단위의 상태가 나올 확률을 제어하고 조합 최적화 문제에 적용했다.[^p6] |

대표 논문 6에는 에너지 비교 표의 단위와 수치를 바로잡는 정정 공지가 있다.[^correction]

## 교수와 전문 분야

황철성 교수는 서울대학교에서 무기재료공학 학사(1987), 석사(1989), 박사(1993) 학위를 받았다. 1993년 2월–1994년 5월 미국 국립표준기술연구소의 박사후연구원, 1994년 5월–1997년 12월 삼성전자 반도체 연구개발 조직의 Principal Engineer로 일했다. 1998년 1월 서울대학교 조교수로 부임했고, 2002년 4월 부교수, 2008년 3월 교수로 이어졌으며, 2020년 9월부터 SNU Distinguished Professor로 기재되어 있다.[^prof]

전문 분야는 차세대 메모리 재료와 박막, 메모리·논리 소자, 뉴로모픽 하드웨어다. 연구 관심에는 강유전체와 저항 변화·상변화 재료, 전하를 가두는 방식의 플래시 메모리, 금속 전극, 산화물 반도체, 신경망과 확률 계산용 소자가 포함된다. 플래시 메모리는 블록 단위로 지우고 다시 쓸 수 있는 비휘발성 반도체 메모리다.[^prof]

누리집은 한국공학한림원 회원(2019년부터), 한국과학기술한림원 정회원(2015년부터), 영국 왕립화학회 Fellow(2014년부터), 서울대 반도체공동연구소 소장(2014–2016)을 기재한다. 학술 활동에는 Physica Status Solidi (RRL) 편집위원, Advanced Electronic Materials·Journal of Materials Chemistry C 국제자문위원, Scientific Reports 편집위원이 있다.[^prof]

## 응용 분야

- 반도체 정보 저장: DRAM, 비휘발성 메모리, 메모리와 논리 소자를 위한 박막과 전극.[^prof]
- 감각 정보 처리: 신경계의 기능을 본뜬 하드웨어와 여러 물체의 움직임을 처리하는 시각 소자.[^research][^p2]
- 계산 하드웨어: 메모리 내 논리 계산, 그래프 분석, 확률 계산과 조합 최적화.[^research][^p4][^p6]

## 구성원

박사후연구원 5명, 박사과정 48명, 석사과정 15명의 메뉴별 명단과, 별도 Member 쪽의 Postdoctoral Fellowship 표기 1명이다. 과정·연구 분야·학교 이메일은 누리집 표기다. 별도 Member 쪽에는 재직 기간이 적혀 있지 않다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 최원호 | 박사후연구원 | PRAM | choiwh@snu.ac.kr |  |
| 정태영 | 박사후연구원 | Neuromorphic |  |  |
| 한장욱 | 박사후연구원 | RRAM | bandooria@snu.ac.kr |  |
| 문상익 | 박사후연구원 | Oxide TFT | aaronmun@snu.ac.kr |  |
| 박형준 | 박사후연구원 | ReRAM | stormy123@snu.ac.kr |  |
| 김혜령 | 박사과정 | PRAM |  |  |
| 이인수 | 박사과정 | FRAM | insoo8840@snu.ac.kr |  |
| 변승용 | 박사과정 | FRAM | byunsimon@snu.ac.kr |  |
| 김도현 | 박사과정 | RRAM | dohyun317@snu.ac.kr |  |
| 윤승재 | 박사과정 | DFT | pingpong0828@snu.ac.kr |  |
| 이정규 | 박사과정 | ReRAM | andynine@snu.ac.kr |  |
| 정민정 | 박사과정 | RRAM | cindy44@snu.ac.kr |  |
| 전상민 | 박사과정 | PRAM | sjeon121@snu.ac.kr |  |
| 조재민 | 박사과정 | RRAM | jmjo200@snu.ac.kr |  |
| 남현우 | 박사과정 | FRAM | hyunwoonam@snu.ac.kr |  |
| 신성재 | 박사과정 | FRAM | s.seongjae@snu.ac.kr |  |
| 함재원 | 박사과정 | TFT | hungrylion@snu.ac.kr |  |
| 김진홍 | 박사과정 | RRAM | smaser@snu.ac.kr |  |
| 최준성 | 박사과정 | TFT | wnstjd4014@snu.ac.kr |  |
| 김병수 | 박사과정 | RRAM | plutokbs@snu.ac.kr |  |
| 임성필 | 박사과정 | RRAM | seongpil.yim@snu.ac.kr |  |
| 김민섭 | 박사과정 | FRAM, Negative Capacitance | kimkan7@snu.ac.kr |  |
| 김승진 | 박사과정 | PRAM | rkatndwks@snu.ac.kr |  |
| 곽찬수 | 박사과정 | DRAM | westham@snu.ac.kr |  |
| 김동연 | 박사과정 | VRRAM | kim.dongyun@snu.ac.kr |  |
| 최승헌 | 박사과정 | FRAM, Negative Capacitance | lugia0916@snu.ac.kr |  |
| 박한솔 | 박사과정 | FRAM | slagk12@snu.ac.kr |  |
| 이수형 | 박사과정 | RRAM | soohyung99@snu.ac.kr |  |
| 박서룡 | 박사과정 | Oxide TFT | sr51.park@snu.ac.kr |  |
| 김현욱 | 박사과정 | RRAM | hyunwk@snu.ac.kr |  |
| 피길화 | 박사과정 | FRAM | khpi1@snu.ac.kr |  |
| 윤한섭 | 박사과정 | DRAM | hansub.yoon@snu.ac.kr |  |
| 염민규 | 박사과정 | FRAM | yminkyu97@snu.ac.kr |  |
| 김형증 | 박사과정 | TFT | hyungjeung77@snu.ac.kr |  |
| 김성현 | 박사과정 | DRAM | tjdgus5432@snu.ac.kr |  |
| 김시현 | 박사과정 | TFT | polhyuncx@snu.ac.kr |  |
| 강준영 | 박사과정 | FRAM | joony.kang@snu.ac.kr |  |
| 김성은 | 박사과정 | FRAM | sekkim@snu.ac.kr |  |
| 성여현 | 박사과정 | FRAM | ssungyeo@snu.ac.kr |  |
| 엄민섭 | 박사과정 | TFT | ums8138@snu.ac.kr |  |
| 표현곤 | 박사과정 | FEFET | hyungon92@snu.ac.kr |  |
| 손건희 | 박사과정 | RRAM | kingof21@snu.ac.kr |  |
| 김현민 | 박사과정 | FRAM | ggoomnara@snu.ac.kr |  |
| 김호진 | 박사과정 | FRAM | rlaghwls92@snu.ac.kr |  |
| 정한용 | 박사과정 | RRAM | dinthesky@snu.ac.kr |  |
| 이상협 | 박사과정 | FRAM |  |  |
| 정수빈 | 박사과정 | FRAM | jungddub@snu.ac.kr |  |
| 박진우 | 박사과정 | ReRAM | phsvevo@snu.ac.kr |  |
| 김원 | 박사과정 | FRAM | acme10@snu.ac.kr |  |
| 김성호 | 박사과정 | ReRAM | lionpeter@snu.ac.kr |  |
| 윤광현 | 박사과정 | VRRAM | ykhyun@snu.ac.kr |  |
| 문수빈 | 박사과정 | TFT | anstnqlsvv@snu.ac.kr |  |
| 김윤재 | 박사과정 | FRAM, DFT | kyjss1375@snu.ac.kr |  |
| 최재욱 | 석사과정 | TFT | jaewook.choi@snu.ac.kr |  |
| 박준우 | 석사과정 | PRAM | jwpark345@snu.ac.kr |  |
| 차승범 | 석사과정 | FRAM | csb4189@snu.ac.kr |  |
| 김동재 | 석사과정 | FRAM | kdjmse@snu.ac.kr |  |
| 이정윤 | 석사과정 | TFT | yoonli@snu.ac.kr |  |
| 강민재 | 석사과정 | FRAM | mj.kang@snu.ac.kr |  |
| 김영우 | 석사과정 | DRAM | iankyw@snu.ac.kr |  |
| 박보람 | 석사과정 | FRAM | vbcs51110@snu.ac.kr |  |
| 박상민 | 석사과정 | FRAM | psmurphy@snu.ac.kr |  |
| 김선엽 | 석사과정 | TFT | kimsy007@snu.ac.kr |  |
| 김도윤 | 석사과정 | DRAM | ben3539@snu.ac.kr |  |
| 박미소 | 석사과정 | TFT | miso8652@snu.ac.kr |  |
| 박지훈 | 석사과정 | DRAM | jihoon2.park@snu.ac.kr |  |
| 최제강 | 석사과정 | PRAM | jk.choi@snu.ac.kr |  |
| 문지원 | 석사과정 | TFT | moonjw@snu.ac.kr |  |
| Dong Ryeol Whang | 박사후연구원 (별도 Member 쪽 표기) | Phosphorescent Ir(III) Complexes |  |  |

## 졸업생과 이전 구성원

Alumni의 2001–2026년 구역에 게시된 195행이다. 같은 이름이라도 학위·연도·진로가 다르게 게시된 행은 각각 표시한다. 학위 칸이 ‘전체’로 적힌 행은 학위를 추정하지 않고 비워 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 신종훈 | Ph. D. (2026) | SK 하이닉스 |
| 심성근 | Ph. D. (2026) | SK 하이닉스 |
| 정태영 | Ph. D. (2026) | Post-doc |
| 송해원 | Ph. D. (2026) | SK 하이닉스 |
| 강한솔 | Master (2026) | SK 하이닉스 |
| 문상익 | Ph. D. (2026) | Post-doc |
| 백인경 | Ph. D. (2026) | SK 하이닉스 |
| 조유린 | Ph. D. (2026) | Peking University |
| 정선우 | Ph. D. (2026) | SAIT |
| 박형준 | Ph. D. (2026) | Post-doc |
| 전광식 | Ph. D. (2026) | 삼성전자 |
| 박병우 | Ph. D. (2026) | SK 하이닉스 |
| 김현영 | Ph. D. (2026) | SK 하이닉스 |
| 김영록 | Ph. D. (2026) | SK 하이닉스 |
| 백희원 | Ph. D. (2026) | 삼성전자 |
| 최진헌 | Ph. D. (2026) | 삼성전자 |
| 김태균 | Ph. D. (2026) | 삼성전자 |
| 신종훈 | Ph. D. (2026) | Postdoc |
| 송재희 | Ph. D. (2026) | SK 하이닉스 |
| 김연재 | Master (2026) | SK 하이닉스 |
| 정문수 | Master (2026) | SK 하이닉스 |
| 김승범 | Master (2026) | SK 하이닉스 |
| 김민종 | Master (2026) | SK 하이닉스 |
| 최원호 | Ph. D. (2026) | SAIT |
| 이석현 | Ph. D. (2025) | 삼성전자 |
| 박태원 | Ph. D. (2025) | 삼성전자 |
| 김병윤 | Master (2025) | SK 하이닉스 |
| 신동훈 | Ph. D. (2025) | SK 하이닉스 |
| 김경도 | Ph. D. (2025) | SK 하이닉스 |
| 신중찬 | Master (2025) | 삼성전자 |
| 박태민 | Master (2025) | 삼성전자 |
| 이동형 | Master (2025) | 삼성전자 |
| 박효빈 | Master (2025) | 삼성전자 |
| 오길중 | Master (2025) | SK 하이닉스 |
| 백창훈 | Master (2025) | SK 하이닉스 |
| 이수형 | Master (2025) | University of Michigan |
| 이재훈 | Ph. D. (2025) | SK 하이닉스 |
| 한장욱 | Ph. D. (2025) | Postdoc |
| 강석인 | Ph. D. (2025) | 삼성전자 |
| 한준규 | Postdoctoral (2024) | 서울대학교 |
| 김진홍 | Master (2024) | 박사 과정 진학 |
| 임성필 | Master (2024) | 박사 과정 진학 |
| 류승규 | Ph. D. (2024) | Stanford University |
| 서행하 | Ph. D. (2024) | imec |
| 이용희 | Ph. D. (2024) | Lawrence Berkeley National Laboratory |
| 예건희 | Ph. D. (2024) | SK 하이닉스 |
| 마은경 | Master (2024) | SK 하이닉스 |
| 이한철 | Master (2024) | SK 하이닉스 |
| 장서영 | Master (2024) | SK 하이닉스 |
| 봉슬기 | Master (2024) | SK 하이닉스 |
| 이용빈 | Ph. D. (2024) | 삼성전자 |
| 남현우 | Master (2024) | 박사 과정 진학 |
| 이건욱 | Master (2024) | 삼성전자 |
| 김영신 | Master (2024) | 삼성전자 |
| 박유경 | Master (2024) | 삼성전자 |
| 문지원 | Master (2024) | 삼성전자 |
| 전정우 | Ph. D. (2024) | Stanford University |
| 김재현 | Ph. D. (2024) | 삼성전자 |
| 임준일 | Ph. D. (2024) | 삼성전자 |
| 우효천 | Ph. D. (2024) | SK 하이닉스 |
| 이향원 | Ph. D. (2023) |  |
| 이용빈 | Ph. D. (2023) | 삼성전자 |
| 김승수 | Ph. D. (2023) |  |
| 장윤호 | Ph. D. (2023) | 연세대학교 |
| 이선진 | Master (2023) | SK 하이닉스 |
| 김하니 | Master (2023) | SK 하이닉스 |
| 이별준 | Master (2023) |  |
| 용수겸 | Master (2023) | 삼성전자 |
| 이선우 | Master (2023) | 서울대학교 치의학과 |
| 왕보웬 | Ph. D. (2022) |  |
| 박태균 | Ph. D. (2022) | SK 하이닉스 |
| 이진원 | Master (2022) | SK 하이닉스 |
| 심두섭 | Master (2022) | SK 하이닉스 |
| 우경석 | Ph. D. (2022) | 울산과학기술원(UNIST) |
| 김우현 | Ph. D. (2022) | 삼성전자 |
| 김지훈 | Ph. D. (2022) | SK 하이닉스 |
| 김범용 | Ph. D. (2022) | SK 하이닉스 |
| 김길섭 | Ph. D. (2022) | SK 하이닉스 |
| 최진우 | Master (2022) | 데이터사이언스 |
| 최진명 | Master (2022) | 삼성전자 |
| 오민식 | Master (2022) | MIT |
| 김도헌 | Ph. D. (2021) | 삼성전자 |
| 권대선 | Ph. D. (2021) | 숙명여자대학교 |
| 유찬영 | Ph. D. (2021) | 홍익대학교 |
| 박현우 | Ph. D. (2021) | Georgia Institute of Technology |
| 백인환 | Ph. D. (2021) | 인하대학교 |
| 한규승 | Ph. D. (2021) | 삼성전자 |
| 김화영 | Master (2021) | SK 하이닉스 |
| 김광민 | Master (2021) | 삼성디스플레이 |
| 현승담 | Ph. D. (2021) | 삼성종합기술원 |
| 이현재 | Ph. D. (2021) | Georgia Institute of Technology |
| 장윤진 | Ph. D. (2021) | 삼성종합기술원 |
| 김동건 | Ph. D. (2021) | 삼성전자 |
| 김준식 | Ph. D. (2021) | 삼성전자 |
| 이윤경 | Postdoctoral (2020) | 전북대학교 |
| 여인원 | Ph. D. (2020) | Postdoc |
| 권대은 | Ph. D. (2020) | SK 하이닉스 |
| 권영재 | Ph. D. (2020) | SK 하이닉스 |
| 김구현 | Ph. D. (2020) | Postdoc |
| 박의상 | Ph. D. (2020) | SK 하이닉스 |
| 이영환 | Ph. D. (2020) | 삼성전자 |
| 이우철 | Ph. D. (2020) | 삼성종합기술원 |
| 차재춘 | Master (2020) | SK 하이닉스 |
| 마성습 | Master (2020) | SK 하이닉스 |
| 이호인 | Master (2020) | 삼성전자 |
| 하만익 | Master (2020) | 삼성전자 |
| 김호현 | Master (2020) | SK 하이닉스 |
| 김유민 | Ph. D. (2019) | 삼성종합기술원 |
| 김금도 | Ph. D. (2019) | 삼성전자 |
| 노장호 | Master (2019) | 삼성전자 |
| 루카이 | Ph. D. (2019) | Qingdao university |
| 박재홍 | Ph. D. (2019) | 삼성전자 |
| 안철현 | Ph. D. (2019) | 삼성전자 |
| 왕용민 | Master (2019) |  |
| 김혜진 | Ph. D. (2019) | 명지대학교 |
| 차순형 | Master (2019) | 삼성전자 |
| 조철진 | Ph. D. (2019) | 삼성전자 |
| 김백수 | Master (2019) | SK 하이닉스 |
| 문태환 | Ph. D. (2019) | 아주대학교 |
| 김상현 | Ph. D. (2019) | 삼성전자 |
| 조성탁 | Master (2019) | 삼성전자 |
| 전석민 | Master (2018) | SK 하이닉스 |
| 황은석 | Ph. D. (2018) | 주성엔지니어링 |
| 이승준 | Ph. D. (2018) | 삼성디스플레이 |
| 박태형 | Ph. D. (2018) | SK 하이닉스 |
| 김한준 | Ph. D. (2018) | SK 하이닉스 |
| 유시정 | Ph. D. (2017) | 삼성종합기술원 |
| 송호주 | Master (2017) | 삼성전자 |
| 김상균 | Master (2017) |  |
| 권태홍 | Ph. D. (2017) | SK 하이닉스 |
| 정민정 | Master (2016) | 삼성전자 |
| 윤경진 | Ph. D. (2016) | Intel |
| 김유진 | Ph. D. (2016) | SK 하이닉스 |
| 이재호 | Ph. D. (2016) | 삼성전자 |
| 임형광 | Ph. D. (2016) |  |
| 석준영 | Ph. D. (2015) | 삼성전자 |
| 조영진 | Ph. D. (2015) | 삼성종합기술원 |
| 윤정호 | Ph. D. (2015) | 성균관대학교 |
| 전우진 | Ph. D. (2015) | 경희대학교 |
| 김언기 | Ph. D. (2015) | 삼성전자 |
| 유연우 | Master (2014) | KIMS |
| 이웅규 | Ph. D. (2014) | 숭실대학교 |
| 송슬지 | Ph. D. (2014) | 삼성전자 |
| 박민혁 | Ph. D. (2014) | 서울대학교 |
| 엄태용 | Ph. D. (2014) | 세종대학교 |
| 이상영 | Ph. D. (2014) | SK 하이닉스 |
| 유일혁 | Master (2013) | 주성 엔지니어링 |
| 정윤수 | Master (2013) | LG 화학 |
| 최선희 | Ph. D. (2013) | KIST |
| 이주휘 | Ph. D. (2013) | Toyota Central R&D Laboratories Inc. |
| 라상호 | Ph. D. (2013) | 삼성전자 |
| 김효겸 | Ph. D. (2013) | 삼성전자 |
| 정윤장 | Master (2012) | Princeton Univ. |
| 이종호 | Postdoctoral (2012) | SK 하이닉스 |
| 김건환 | Ph. D. (2012) | 연세대학교 |
| 정형석 | Ph. D. (2012) | 삼성전자 |
| 이종호 | (2012) | U Penn. |
| 한소라 | Master (2011) | LG CNS |
| 한정환 | Ph. D. (2011) | 서울과학기술대학교 |
| 최설 | Ph. D. (2011) | 삼성전자 |
| 김정환 | Ph. D. (2011) | 한밭대학교 |
| 이현주 | Ph. D. (2011) | 삼성전자 |
| 이민환 | Postdoctoral (2011) | University of California, Merced |
| 오힘찬 | Master (2010) | 한국전자통신연구원 |
| 서민하 | Ph. D. (2010) | LG CNS |
| 최규진 | Master (2009) | 서울대학교 치의학과 |
| 나광덕 | Master (2009) | POSCO |
| 이상운 | Ph. D. (2009) | 아주대학교 |
| 박우영 | Ph. D. (2009) | SK 하이닉스 |
| 최병준 | Ph. D. (2009) | 서울과학기술대학교 |
| 조덕용 | Postdoctoral (2009) | 전북대학교 |
| 신용철 | Master (2008) | 삼성글로벌리서치 |
| 김경민 | Ph. D. (2008) | 한국과학기술원 |
| 박태주 | Ph. D. (2008) | 한양대학교 |
| 송재원 | Ph. D. (2008) | 한화첨단소재 |
| 이근 | Master (2007) | 삼성전자 |
| 김성근 | Ph. D. (2007) | KIST |
| 조문주 | Ph. D. (2007) | IMEC, Bel |
| 민요셉 | Ph. D. (2007) | 건국대학교 |
| 홍석훈 | Master (2006) | Applied Materials |
| 조금석 | Ph. D. (2006) | Tianjin University |
| 황규원 | Master (2006) | KIST |
| 심준섭 | Master (2006) | SK 하이닉스 |
| 전충배 | Master (2006) | 삼성 LED |
| 권오성 | Ph. D. (2006) | 삼성전자 |
| 정두석 | Master (2005) | 한양대학교 |
| 김완돈 | Master (2005) | 삼성전자 |
| 이석우 | Master (2005) | 삼성전자 |
| 박재후 | Ph. D. (2005) | 삼성전자 |
| 박홍배 | Master (2004) | 삼성전자 |
| 임지은 | Master (2003) | 삼성전자 |
| 박병건 | Master (2002) |  |
| 정시화 | Master (2002) | LG-Phillips |
| 김지훈 | Master (2002) | 삼성전자 |
| 김혜령 | Master (2001) | KIST |

## 최근 논문 목록 (2021–2026)

누리집 Paper의 2021–2026년 연도 구역에 실린 166편이다. 구역별로 2026년 21편, 2025년 41편, 2024년 34편, 2023년 23편, 2022년 23편, 2021년 24편이다. 아래 연도는 누리집의 구역 표기이며, 실제 서지의 권호 연도와 다를 수 있다. 저자·제목·학술지·서지는 게시된 한 줄을 따른다.[^pubs]

**2026**

- Jonghoon Shin, Haengha Seo, Tae Kyun Kim, Sung Keun Shim, Hyun Wook Kim, Heewon Paik, Haewon Song, Seong Jae Shin, Sanghyup Lee, Han Sol Park, Seungheon Choi, Sungho Kim, Kunhee Son, Janguk Han, Dae Seon Kwon, and Cheol Seong Hwang\* Dopant Engineered Y‑Doped Hafnia-Zirconia Nanolaminates with 0.26 nm Equivalent Oxide Thickness for Dynamic Random Access Memory Capacitors ACS Nano (2026) DOI: https://doi.org/10.1021/acsnano.6c11877
- Joon Young Kang, Jinheon Choi, Jonghoon Shin, Haewon Song, Tae Won Park, Jin-Woo Han, Daewon Ha, Jae Joon Kim, and Cheol Seong Hwang\* Three-dimensional dynamic random-access memory beyond two-dimensional scaling limits Nature Reviews Electrical Engineering (2026) DOI: https://doi.org/10.1038/s44287-026-00347-x
- Han Sol Park, Seungheon Choi, Min Kyu Yeom, Sanghyup Lee, Sahngik A. Mun, and Cheol Seong Hwang\* Achieving Robust Ferroelectric Properties of Hf₀.₆Zr₀.₄O₂ Thin Films through the Pseudofield-Inducing Effect of Al₀.₈₅Sc₀.₁₅N Bottom Electrode ACS Nano (2026) DOI: https://doi.org/10.1021/acsnano.6c13488
- Sung Keun Shim†, Wonho Choi†, Sunwoo Cheong, Dong Hoon Shin, Jonghoon Shin, Janguk Han, Jiseong Im, Sungho Kim, Kunhee Son, Hyun Wook Kim, Jin Hong Kim, Jea Min Cho, Junwoo Park, Byongwoo Park, Yoon Ho Jang and Cheol Seong Hwang Monolithic three-dimensionally integrated memristor-thin-film transistor for electrically programmable multimode reservoir computing Nature Communications (2026)
- Hyungjun Park‡, Han Yong Jeong‡, Kyung Seok Woo, Hyun Wook Kim, Janguk Han, Jong Hoon Shin, and Cheol Seong Hwang\* Fast Electronic Memristors with Improved Retention and Synaptic Functionality Enabled by Tri-TaOₓ Engineering ACS Applied Materials & Interfaces (2026) DOI : https://doi.org/10.1021/acsami.6c14083
- In Kyung Baek†, Sunwoo Cheong†, Hyun Wook Kim†, Jea Min Cho, Kunhee Son, Yeong Rok Kim, Kyung Seok Woo, Hyungjun Park, Byeong Su Kim, and Cheol Seong Hwang\* In-Memory Bayesian Machine Using Vertical Cu0.33Te0.67/HfO2/TiN Memristive Crossbar Arrays ACS Nano (2026) DOI : https://doi.org/10.1021/acsnano.6c07852
- Wen-Xiong Song†, Guangjie Shi†, Qi Hu†, Fan Zhu, Tianjiao Xin, Ying Chen, Sergiu Clima, Gilberto Teobaldi, Yuhao Wang, Wenjian Huang, Sannian Song\*, Cheol Seong Hwang, Li-Min Liu, Yan Cheng\*, Zhitang Song\* Non-Arrhenius threshold switching by field-driven dipolar ordering Nature Communications (2026) DOI : https://doi.org/10.1038/s41467-026-72970-z
- Hyungjun Park†, Jin Hong Kim†, Hyun Wook Kim†, Néstor Ghenzi, Sung Keun Shim, Joon-Kyu Han, Min Jung Chung, Dong Hoon Shin, Kyung Seok Woo, Cheol Seong Hwang\* Memristive Motion-Streak Neuron for Spatiotemporal Multiple Object Detection Advanced Materials (2026) DOI : https://doi.org/10.1002/adma.74793
- Seung Ryong Byun, Seungheon Choi, Han Sol Park, Seong Jae Shin, Jaehee Song, Minseob Kim, Yeohyun Sung, Subin Jung, Hyeonwoo Park,\* and Cheol Seong Hwang\* Stochastic Preisach Modeling of Ferroelectric Switching Kinetics ACS Appl. Electron. Mater. (2026) DOI : 10.1021/acsaelm.6c00889
- Haewon Song, Yu Kyung Park, Jonghoon Shin, Tae Kyun Kim, Heewon Paik, and Cheol Seong Hwang\* Efficient leakage suppression in TiO₂ dielectric films for dynamic random access memory capacitors via Mg doping. Journal of Materials Chemistry C (2026) DOI: 10.1039/D6TC01369D
- Sungjin Kim, Jeong Woo Jeon, Byongwoo Park, Wonho Choi, Gwangsik Jeon, Sangmin Jeon, Junwoo Park, Woohyun Kim, Junyoung Lim, David Ahn, Chanyoung Yoo, and Cheol Seong Hwang\*\* Atomic Layer Deposition of High-Density GeSe Films for Stable Vertical Ovonic Threshold Switching and Selector-Only Memory Chem. Mater. DOI: 10.1021/acs.chemmater.6c01199 (2026).
- June-Chul Shin†, Taegyun Park†, Dong Hoon Shin†, Hyun-Young Choi†, Kyungmin Yang, Jiwoo Kim, Oh Yeong Gong, Hee Jae Hwang, Kenji Watanabe, Takashi Taniguchi, Yeonwoong Jung, Cheol Seong Hwang, and Gwan-Hyoung Lee\*\* Reconfigurable 2D Floating-Gate Field-Effect Transistors with Graphene-Induced Interfacial Polarization for Unified Memory-Logic Integration ACS Nano (2026) DOI: https://doi.org/10.1021/acsnano.6c05072
- Juneseong Choi†, Minsub Um†, Hyobin Park, Jinheon Choi, Sahngik Aaron Mun, Jaewon Ham, Seoryong Park, Hyungjeung Kim, Shihyun Kim, Subin Moon, Jong hoon shin, and Cheol Seong Hwang\* Mechanistic Evaluation of Amorphous InGaZnO-Based One Transistor-One Capacitor Memory Cell via Fast Current-Voltage Measurements and Modeling Nanoscale (2026) DOI : https://doi.org/10.1039/d6nr00995f
- Dong Hoon Shin, Wonho Choi, Sunwoo Cheong, Néstor Ghenzi, Sung Keun Shim, Sung Ho Kim, Kunhee Son, Soo Hyung Lee, Byongwoo Park, Jonghoon Shin, and Cheol Seong Hwang\* Adaptive spatial hashing with dual-domain memristive hardware. Nature Communications., DOI: 10.1038/s41467-026-72743-8 (2026)
- Haewon Song, Jonghoon Shin, Tae Kyun Kim, Heewon Paik, Dae Seon Kwon, and Cheol Seong Hwang\* Electrode-dependent interfacial reactions and Ru loss suppression during ozone-based atomic layer deposition of TiO2 on Ru- and RuO2-based electrodes. J. Mater. Chem. C, 14, 14546-14557 (2026)
- Hyeon Woo Park, Yunseok Kim, Won-Tae Koo, Dong Ik Suh, Junseong Seo , Seungyong Byun, Youngmo Kim, Ja-Yong Kim, SeungWook Ryu, Heeyoung Jeon, KiVin Im, Gwangyeob Lee, Taeone Youn, Seho Lee, Jaeyun Yi, Seon Yong Cha & Cheol Seong Hwang The cylindrical devices with tunable positive, infinite, and negative capacitance for dynamic random access memory. Nat Commun 17, 5184
- Dae Seon Kwon, Kun Hee Ye, In Soo Lee, Jonghoon Shin, Junil Lim, Tae Kyun Kim, Haengha Seo, Heewon Paik, Haewon Song, Seungheon Choi, Jung-Hae Choi\*, and Cheol Seong Hwang\* Heterogeneous Local-Epitaxial Growth Behavior of Ultrathin HfO2/Al-Doped TiO2 Bilayer Dielectrics for Dynamic Random-Access Memory Capacitor Applications ACS Appl. Mater. Interfaces, DOI: 10.1021/acsami.6c04008 (2026)
- Shuang Wang, Zhiyuan Li, Mengjiao Pei, Qinqi Ren, Ming Deng, Kah-Wee Ang, Alon Ascoli, Sarbajit Banerjee, Michele Bonnin, Yoeri van de Burgt, Bojun Cheng, Leon Chua, Pier Paolo Civalleri, Fernando Corinto, Tie Jun Cui, Saptarshi Das, Ahmet Samil Demirkol, Sebastiaan van Dijken, Yijia Fan, Lu Fang, Matteo Farronato, Zi Rui Feng, Emanuele Gemo, Marco Gilli, Sreetosh Goswami, Yuhui He, Chaoran Huang, Qianqian Huang, Cheol Seong Hwang, Daniele Ielmini, Yoon Ho Jang, Zdenka Kuncic, Max Christian Lemme, Can Li, Shi-Jun Liang, Keqin Liu, Shaojie Liu, Jin Luo, Qian Ma, Wolfgang Maass, Piergiulio Mannocci, Ioannis Messaris, Feng Miao, Thomas Mikolajick, Vasilis Ntinas, John Ponis, Themis Prodromakis, Dimitris Prousalis, Qiming Shao, Stefan Slesazeck, John Paul Strachan, Hongwei Tan, Jianshi Tang, Ronald Tetzlaff, Le Phuong Lan Tran, Ilia Valov, Anthony Vorias, Benshan Wang, Jiangjing Wang, Shengbo Wang, Xiaozhe Wang, Yasai Wang, Huaqiang Wu, Qiangfei Xia, Kai Xiao, Zhihua Xiao, Zheshun Xiong, Tengji Xu, Ming-Jay Yang, Yuchao Yang, Yuekun Yang, Wei Zhang, Yang Chai\* Technology Roadmap of Bioinspired Computing Hardware ACS Nano (2026) DOI : https://doi.org/10.1021/acsnano.5c17087
- Sunwoo Cheong†, Soo Hyung Lee†, Janguk Han†, Jun-Young Park, Dong Hoon Shin, Yoon Ho Jang, Sung Keun Shim, Sungho Kim, Cheol Seong Hwang\*, Joon-Kyu Han\* Multi-State Probabilistic Computing Using Floating-Body MOSFETs Based on the Potts Model for Solving Complex Combinatorial Optimization Problems AdvancedMaterials,2026;0:e16797 DOI : https://doi.org/10.1002/adma.202516797
- Suk Yeop Chun†, Yoon Ho Jang†, Ji Eun Kim, Keunho Soh, Min Su Nam, Na Kyung Yu, Janguk Han, Soo Hyung Lee, Chong-Yun Kang\*, Cheol Seong Hwang\*, Jung Ho Yoon\* Hydrogen-Assisted Asymmetric and Nonlinear Memristor Array for Reconfigurable Olfactory Graph Networks Small Methods , 2026; 0:e02405 DOI : https://doi.org/10.1002/smtd.202502405
- Tae Kyun Kim, Heewon Paik, Jonghoon Shin, Haewon Song, Dae Seon Kwon, and Cheol Seong Hwang Al-Doped Rutile TiO2 with Y2O3−ZrO2 Stacks Achieving Thin Thickness and Low Leakage for Dynamic Random-Access Memory Capacitors ACS Applied Electronic Materials (2026)

**2025**

- Taeyoung Jeong, Kun Hee Ye, Seungjae Yoon, Dohyun Kim, Yunjae Kim, Cheol Seong Hwang and Jung-Hae Choi VacHopPy: A Python module for vacancy hopping analysis based on molecular dynamics simulations Computer Physics Communications, 320, 110010 (2026)
- Yu Lin Zou†, Sunwoo Cheong†, Jea Min Cho, Néstor Ghenzi, Mingxin Deng, Seongjae Shin, Donghoon Shin, Xiangyuan Li, Tae Won Park, Jiseong Im\* and Cheol Seong Hwang\* Algorithm-Compatible Single-Transistor Neuron and Al/ZrO2/TiO2/AlOx Memristor Synapse Kernel for Spiking Neural Networks ACS Applied Materials & Interfaces Article ASAP (2025) https://doi.org/10.1021/acsami.5c19107
- Kyung Do Kim, Seung Kyu Ryoo, Min Kyu Yeom, Dong Jae Kim and Cheol Seong Hwang Influence of Bottom Electrodes on the Ferroelectric Stability of AlScN Film at High Temperatures Advanced Electronic Materials, (2025)
- Gwangsik Jeon†, Sangmin Jeon†, Seunghwan Lee, Jeong Woo Jeon, Wonho Choi, Byongwoo Park, Sungjin Kim, Chanyoung Yoo, Hyejin Jang, and Cheol Seong Hwang\* Ultrathin Monatomic Antimony Films by Sacrificial Atomic Layer Deposition for Phase Change Memory Advanced Materials, 38, e19924 (2026)
- Soo Hyung Lee†, Sungho Kim†, Janguk Han, Sung Keun Shim, Kunhee Son, Dong Hoon Shin, Hanyong Jeong, Jinwoo Park, Seong Jae Shin, Yoon Ho Jang\* and Cheol Seong Hwang\* Electrically tunable physical reservoir computing on two-terminal devices npj Unconv. Comput. 2, 27 (2025) DOI: https://doi.org/10.1038/s44335-025-00043-3
- Kunhee Son†, Jea Min Cho†, Dong Hoon Shin†, Yeong Rok Kim, Néstor Ghenzi, Sunwoo Cheong, Byeong Su Kim, Jung Kyu Lee, Sungho Kim, Wonho Choi, Soo Hyung Lee, Janguk Han and Cheol Seong Hwang Vertical Self-Rectifying Memristive Arrays for Page-Wise Parallel Logic and Arithmetic Processing Adv. Mater., 38, e14099 (2026) DOI: 10.1002/adma.202514099
- Jonghoon Shin, Haengha Seo, Janguk Han, Tae Kyun Kim, Heewon Paik, Haewon Song, Hansub Yoon, Han Sol Park, Kyung Do Kim, Seong Jae Shin, Jae Hee Song, Sanghyup Lee, Seungheon Choi, Dong Hoon Shin, Juneseong Choi and Cheol Seong Hwang High-performance dynamic random access memory capacitor with an equivalent oxide thickness of 0.31 nm via stepwise cycling in Y-doped Hf0.5Zr0.5O2 thin films Material Horizons, 13, 1739-1756 (2026) DOI: 10.1039/D5MH01563D
- Seo Young Jang†, Jaewon Ham†, Yonghee Lee, Sukin Kang, Sahngik Aaron Mun, Jinheon Choi, Juneseong Choi, Seoryong Park, Hyungjeung Kim and Cheol Seong Hwang\* Wet etching of atomic-layer-deposited amorphous zinc-tin-oxide thin film using oxalic acid Journal of Materials Chemistry C, (2025) DOI: 10.1039/D5TC03481G
- Janguk Han†, Hyungjun Park†, Yoon Ho Jang, Dong Hoon Shin, Hyun Wook Kim, Wonho Choi, Kyung Seok Woo\*, and Cheol Seong Hwang\*, Cyclic Plasma Treatment for Enhancing the Synaptic Performance of Bulk-Conductive Resistive Switching Memory ACS Appl. Mater. Interfaces 2025 https://doi.org/10.1021/acsami.5c15918
- Mingu Kang†, Joon-Kyu Han†, Kichul Lee†, Jaeseok Jeong, Chanyoung Yoo, Jeong Woo Jeon, Byongwoo Park, Wonho Choi, Cheol Seong Hwang\*, and Inkyu Park\* Neuromorphic olfaction with ultralow-power gas sensors and ovonic threshold switch Sci. Adv. 2025, Vol 11, Issue 39 DOI: 10.1126/sciadv.adv9222
- Jinheon Choi, Juneseong Choi, Hyungjeung Kim, Shihyun Kim, Sahngik Aaron Mun, Jaewon Ham, Seoryong Park, Minsub Um, Subin Moon and Cheol Seong Hwang\* Effect of Al2O3 passivation layer and optimization of atomic-layer-deposited Zn–Sn–O and Al–Zn–Sn–O thin-film transistors Journal of Materials Chemistry C, (2025) DOI: 10.1039/D5TC02175H
- Heewon Paik, Dohyun Kim, Junil Lim, Haengha Seo, Tae Kyun Kim, Jong Hoon Shin, Haewon Song, Hansub Yoon, Dae Seon Kwon, Dong Gun Kim, Jung-Hae Choi, and Cheol Seong Hwang\* The leakage current suppression mechanism in a RuO2/SrTiO3/Ru capacitor induced by introduction of an ultra-thin GeO2 interfacial layer at the bottom interface Journal of Materials Chemistry C, 2025, 13, 21233-21676
- Shihyun Kim, Hyungjeung Kim, Jinheon Choi, Sahngik Aaron Mun, Yonghee Lee, Sukin Kang, Juneseong Choi, Jaewon Ham, Seoryong Park, Subin Moon, Minsub Um, and Cheol Seong Hwang\* Contact resistance reduction in Amorphous In-Ga-Zn-O thin film transistors by interposing an atomic-layer-deposited amorphous Zn-Sn-O interlayer Journal of Materials Chemistry C, (2025) DOI: 10.1039/d5tc02972d
- Sungho Kim, Dong Hoon Shin, Wonho Choi, Sunwoo Cheong, Sung Keun Shim, Soo Hyung Lee, Janguk Han, Yoon Ho Jang, Kunhee Son, Néstor Ghenzi\* and Cheol Seong Hwang\* Spatiotemporal Reservoir Computing with a Reconfigurable Multifunctional Memristor Array Adv. Mater, e10635, (2025), https://doi.org/10.1002/adma.202510635
- Hyun Wook Kim†, Jin Hong Kim†, Dong Hoon Shin, Min Chung Jung, Tae Won Park, Hyung Jun Park, Joon-Kyu Han, and Cheol Seong Hwang Neuromorphic Visual Receptive Field Hardware with Vertically Integrated Indium-Gallium-Zinc-Oxide Optoelectronic Memristors over Silicon Neuron Transistor Advanced Materials (2025) DOI: https://doi.org/10.1002/adma.202513907
- Jong-Cheol Lee, Jinheon Choi, Tackhwi Lee, Minsik Kim, Seongmin Ahn, Junghan Lee, Sungho Lee, Jihyun Kho, Yongsoon Choi, Kwangmin Park, and Cheol Seong Hwang\* Identifying the Chemical Structure of Indium-Gallium-Zinc Oxide Thin Films with Oxygen Vacancy Variation ACS Applied Electronic Materials, (2025), DOI: 10.1021/acsaelm.5c01023
- Yoon Ho Jang†, Janguk Han†, Soo Hyung Lee†, and Cheol Seong Hwang\* Next-generation graph computing with electric current-based and quantum-inspired approaches Nature Communications, 16, 8029 (2025)
- Han Sol Park, Joong Chan Shin, Kyung Do Kim, Seong Jae Shin, Jae Hee Song, Seung Kyu Ryoo, In Soo Lee, Suk Hyun Lee, Hyunwoo Nam, Cheol Seong Hwang\* Enhancing ferroelectric properties of Hf0.5Zr0.5O2 thin films using the HfN/TiN and W/TiN bi-layer bottom electrodes Journal of Materiomics, 11, 101109 (2025)
- Seong Jae Shin, Hani Kim, Seungyong Byun, Jonghoon Shin, Jinwoo Choi, Suk Hyun Lee, Kyung Do Kim, Jae Hee Song, Dong Hoon Shin, Soo Hyung Lee, In Soo Lee, Hyunwoo Nam, Cheol Seong Hwang\* Influence of deposition temperature and precursor chemistry on the properties of atomic layer deposited Hf0.5Zr0.5O2 thin films Journal of Materiomics, 11, 101101 (2025)
- Kyung Do Kim+, Min Kyu Yeom+, Han Sol Park, Gwangsik Jeon and Cheol Seong Hwang Proximity-Induced Ferroelectric Switching in Wurtzite/Fluorite Bilayers for High-Performance Ferroelectric Field-Effect Transistor Advanced Materials (2025) DOI: https://doi.org/10.1002/adma.202509088
- Jong-Ho Lee, Jae-Joon Kim & Cheol Seong Hwang Semiconductor-related research and education at Seoul National University Nature Reviews Electrical Engineering, (2025), https://doi.org/10.1038/s44287-025-00194-2
- Hyun Young Kim, Néstor Ghenzi, Hyungjun Park, Dong Hoon Shin, Dong Yun Kim,Tae Won Park, Jea Min Cho, Taegyun Park \* and Cheol Seong Hwang \* Dual-mode switching of a bidirectional self-rectifying Ti/HfO2/Ti device for bipolar and electronic complementary resistive switching Nanoscale Horizons (2025) DOI: 10.1039/d5nh00256g
- Yu Lin Zou†, Xiang Yuan Li†, Néstor Ghenzi, Taegyun Park, Dong Hoon Shin, Seong Jae Shin, Jea Min Cho, Tae Won Park, Sunwoo Cheong, Sahngik Aaron Mun, and Cheol Seong Hwang A Study on the Synaptic Behavior of Al/ZrO2/TiO2/Al Electronic Bipolar Resistance Switching Memristor ACS Applied Materials & Interfaces (2025) doi:10.1021/acsami.5c09911
- Kyung Do Kim, Seung Kyu Ryoo, Min Kyu Yeom, Suk Hyun Lee, Wonho Choi, Yunjae Kim, Jung-Hae Choi, Tianjiao Xin, Yan Cheng and Cheol Seong Hwang\* Decoupling polarization and coercive field in AlScN/AlN/AlScN stack for enhanced performance in ferroelectric thin-film transistors Nature Communications, 2025, 16, 7425, DOI: https://doi.org/10.1038/s41467-025-62904-6
- Tae Kyun Kim, Haengha Seo, Junil Lim, Heewon Paik, Jonghoon Shin, Haewon Song, Dae Seon Kwon\* and Cheol Seong Hwang\* Effect of yttrium feeding time on the electrical and structural properties of atomic layer deposited Y-doped TiO2 films for dynamic random-access memory capacitors Journal of Materials Chemistry C (2025)
- Jae Hee Song, Kyung Do Kim, Jonghoon Shin, Seong Jae Shin, Suk Hyun Lee, Seung Yong Byun, In Soo Lee, Han Sol Park, Yeon Jae Kim , Hyun Woo Nam and Cheol Seong Hwang\* Ferroelectric and field-induced ferroelectric phase formation in atomic-layer-deposited ZrO2 thin films with TiN electrodes Journal of Materials Chemistry C, 2025, 13, 14751 - 14766, DOI: 10.1039/D5TC01449B
- Soon Joo Yoon, Jeong Woo Jeon, Junho Lee, Jin Tae Park, Chanwoo Lee, Ki Jun Yu, Hagyoul Bae, Kihyun Kim, Keun Heo, Cheol Seong Hwang, Deok-Yong Cho, Taehun Lee\*, Yoon Kyeung Lee\* Defect Formation and Electrical Transformation in SiO2 Thin Films via Ti-Induced Interdiffusion Acta Materialia (2025)
- Heewon Paik, Junil Lim, Haengha Seo, Tae Kyun Kim, Jonghoon Shin, Haewon Song, Dong Gun Kim, Woongkyu Lee, Dae Seon Kwon\* and Cheol Seong Hwang\* Enhanced Crystallization and Dielectric Properties of Atomic Layer Deposited SrTiO3 Thin Films on Ru Electrode by Inserting GeO2 Interfacial Layer Materials Horizons, 2025,12, 7305-7317
- Dohyun Kim, Kun Hee Ye, Taeyoung Jeong, Seungjae Yoon, Yunjae Kim, Cheol Seong Hwang\* and Jung-Hae Choi\* Polytype family representations of octahedrally coordinated adaptive structures in Ta2O5: energetic and dynamic stability from first principles Phys. Chem. Chem. Phys., 27, 14082 - 14094 (2025), DOI: 10.1039/d5cp01821h
- Sung Keun Shim, Joon-Kyu Han, Janguk Han, Soo Hyung Lee, Dong Hoon Shin, Sunwoo Cheong, Sungho Kim, Hanyoung Jeong, Yoon Ho Jang\*, and Cheol Seong Hwang\* Advanced Time Series Data Processing Using Various Memristor-Integrated Devices Advanced Materials Technologies, (2025), DOI: 10.1002/admt.202500838
- Yonghee Lee, Seung-Yoon Lee, Jinheon Choi, Néstor Ghenzi, Joon-Kyu Han\*, and Cheol Seong Hwang\* Heterogeneous Capacitor-less Two-transistor Dynamic Random Access Memory Cell with Long Retention Time and High Sensing Current Supporting 5-Bit Multilevel Operation Phys. Status Solidi RRL, (2025), DOI: 10.1002/pssr.202500131
- Jinheon Choi†, Juneseong Choi†, Yonghee Lee, Sukin Kang, Sahngik Aaron Mun, Jaewon Ham, Hyungjeung Kim, Shihyun Kim, Subin Moon, and Cheol Seong Hwang\* Optimization of Atomic-Layer-Deposited Zinc-Tin-Oxide Thin-Film- Transistors via Controlled Aluminum Doping ACS Applied Electronic Materials, (2025), DOI: 10.1021/acsaelm.5c00575
- Jonghoon Shin, Dong Hoon Shin, Haengha Seo, Kyung Do Kim, Seungheon Choi, Tae Kyun Kim, Heewon Paik, Haewon Song, Seungyong Byun, In Soo Lee, and Cheol Seong Hwang Ultra-High Energy Storage Performance of Field-induced Ferroelectric Al2O3-inserted Hf0.5Zr0.5O2 Thin Films for Electrostatic Supercapacitors Energy Storage Materials, 79, 104306 (2025)
- Kun Hee Ye, Taeyoung Jeong, Seungjae Yoon, Dohyun Kim, Yunjae Kim, Cheol Seong Hwang\*, Jung-Hae Choi\* Ab Initio Study on 3D Anisotropic Ferroelectric Switching Mechanism and Coercive Field in HfO2 and ZrO2 Advanced Functional Materials. 2025, 2500390
- Hyun Woo Nam, Jae Hoon Lee, Seung Kyu Ryoo, Seong Jae Shin, Kun Hee Ye, Kyung Do Kim, Seung yong Byun, In Soo Lee, Suk Hyun Lee, Jae Hee Song, Jung hae Choi and Cheol Seong Hwang\* Improving the memory window of a ferroelectric thin film transistor using an atomic layer deposited HfNx interfacial layer Journal of Materials Chemistry C, (2025), DOI: 10.1039/d5tc00453e
- Sahngik A. Mun, Seoryong Park, Min-Hyun Lee, Yonghee Lee, Sukin Kang, Jinheon Choi, Jaewon Ham, Juneseong Choi, and Cheol Seong Hwang\* Analysis of the Ambipolar Conduction of Tin Monoxide Thin-Film Transistors with Indium Tin Oxide Electrodes ACS Applied Materials & Interfaces, (2025), DOI: 10.1021/acsami.5c01274
- Gwangsik Jeon, Jeongwoo Jeon, Woohyun Kim, Daehyeon Kim, Wontae Noh, Wonho Choi, Byongwoo Park, Sangmin Jeon, Sungjin Kim, Chanyoung Yoo\* and Cheol Seong Hwang\* Low-temperature atomic layer deposition of metastable MnTe films for phase change memory devices Journal of Materials Chemistry C, 2025, 13, 6762 - 6771
- Haengha Seo, Jonghoon Shin, Han Sol Park, Tae Kyun Kim, Heewon Paik, Haewon Song and Cheol Seong Hwang Non-diffusive behavior of aluminum and yttrium dopants in ZrO2/Al2O3 and ZrO2/Y2O3 bilayer thin films Journal of Materials Chemistry C, Advance Article (2025)
- Janguk Han†, Yoon Ho Jang†, Ji Won Moon, Sung Keun Shim, Sunwoo Cheong, Soo Hyung Lee, Tae Won Park, Joon-Kyu Han, Cheol Seong Hwang\* Vertical Memristive Crossbar Array for Multilayer Graph Embedding and Analysis Advanced Materials, (2025), DOI: 10.1002/adma.202416988
- Hyungjun Park, Joon-Kyu Han, Seongpil Yim, Dong Hoon Shin, Tae Won Park, Kyung Seok Woo, Soo Hyung Lee, Jae Min Cho, Hyun Wook Kim, Taegyun Park\*, and Cheol Seong Hwang\* An Analysis of Components and Enhancement Strategies for Advancing Memristive Neural Networks Advanced Materials, (2025), 2412549, DOI: 10.1002/adma.202412549
- Jinheon Choi†, Juneseong Choi†, Tae Kyun Kim, Yonghee Lee, Sukin Kang, Sahngik Aaron Mun, Jaewon Ham, Hyungjeung Kim, and Cheol Seong Hwang\* Enhanced Performance and Gate Bias Stress Stability of Atomic-Layer-Deposited Amorphous Zn-Sn-O Thin-Film Transistors with HfO2 and Al-Doped TiO2 Interlayers on SiO2 Gate Oxide ACS Applied Electronic Materials, (2025), DOI: 10.1021/acsaelm.4c01690

**2024**

- Yeong Rok Kim†, Dong Hoon Shin†, Néstor Ghenzi, Sunwoo Cheong, Jea Min Cho, Sung Keun Shim, Jung Kyu Lee, Byeong Su Kim, Seongpil Yim, Taegyun Park, and Cheol Seong Hwang Fully Resistive In-Memory Cryptographic Engine with Dual-Polarity Memristive Crossbar Array Advanced Functional Materials, 35, 4, 2414332 (2024)
- Byongwoo Park†, Jeong Woo Jeon†, Woohyun Kim, Wonho Choi, Gwang Sik Jeon, Sangmin Jeon, Sungjin Kim, Chanyoung Yoo, Junyoung Lim, Yonghun Sung, David Ahn, and Cheol Seong Hwang Atomic layer deposition of Sn-doped germanium diselenide for an As-free Ovonic threshold switch with low off-current Dalton Transactions, 2025, 54, 492-502
- Kun Hee Ye, Taeyoung Jeong, Seungjae Yoon, Dohyun Kim, Cheol Seong Hwang\* and Jung-Hae Choi\* Theoretical understanding of the in-plane tensile strain effects on enhancing the ferroelectric performance of Hf0.5Zr0.5O2 and ZrO2 thin films Nanoscale, Advance Article (2024)
- Seung Kyu Ryoo, Kyung Do Kim, Wonho Choi, Panithan Sriboriboon, Seungjae Heo, Haengha Seo, Yoon Ho Jang, Jeong Woo Jeon, Min Kyu Yeom, Suk Hyun Lee, Han Sol Park, Yunseok Kim and Cheol Seong Hwang\* Fabrication of Ultrathin Ferroelectric Al0.7Sc0.3N Films under Complementary-Metal-Oxide-Semiconductor Compatible Conditions by using HfN0.4 Electrode Advanced Materials, 2413295 (2024)
- Jea Min Cho, Seung Soo Kim, Tae Won Park, Dong Hoon Shin, Yeong Rok Kim, Hyung Jun Park, Dong Yun Kim, Soo Hyung Lee, Taegyun Park\* and Cheol Seong Hwang\* Concealable physical unclonable function and an in-memory encryption machine using vertical self-rectifying memristors Nanoscale Horizons (2024)
- Tae Won Park†, Jiwon Moon†, Dong Hoon Shin, Hae Jin Kim, Seung Soo Kim, Jea Min Cho, Hyungjun Park, Kyung Seok Woo, Dong Yun Kim, Sunwoo Cheong, Haewon Song, Jong Hoon Shin, Soo Hyung Lee, Néstor Ghenzi\* and Cheol Seong Hwang\* Enhancing Uniformity, Read Voltage Margin,and Retention in Three-Dimensional and Self-Rectifying Vertical Pt/Ta2O5/Al2O3/TiN Memristors ACS Appl. Mater. Interfaces (2024) DOI : 10.1021/acsami.4c15598
- Suk Hyun Lee, Han Sol Park, Seong Jae Shin, In Soo Lee, Seung Kyu Ryoo, Seungyong Byun, Kyung Do Kim, Taehwan Moon\*, and Cheol Seong Hwang\* Investigation of Ferro-resistive Switching Mechanisms in TiN/Hf0.5Zr0.5O2/WOx/W Ferroelectric Tunnel Junctions with Interface Layer Effect Applied Physics Reviews, 11, 041404 (2024)
- Sunwoo Cheong†, Dong Hoon Shin†, Soo Hyung Lee, Yoon Ho Jang, Janguk Han, Sung Keun Shim, Joon-Kyu Han, Nestor Ghenzi\* and Cheol Seong Hwang \* Hyperplane tree-based data mining with a multi-functional memristive crossbar array Materials Horizons (2024) DOI : 10.1039/d4mh00942h
- Jin Hong Kim†, Hyun Wook Kim†, Min Jung Chung, Dong Hoon Shin, Yeong Rok Kim, Jaehyun Kim, Yoon Ho Jang, Sun Woo Cheong, Soo Hyung Lee, Janguk Han, Hyung Jun Park, Joon-Kyu Han\*, and Cheol Seong Hwang\* Stochastic photo-responsive Memristive Neuron for an In-sensor Visual System based on Restricted Boltzmann Machine Nanoscale Horizons (2024) DOI : 10.1039/D4NH00421C
- Sung Keun Shim†, Keonuk Lee†, Janguk Han, Dong Hoon Shin, Soo Hyung Lee, Sunwoo Cheong, Yoon Ho Jang\*, and Cheol Seong Hwang\* Thresholding Computing with Heterogeneous Integration of Memristive Kernel with Metal-Oxide-Semiconductor Capacitor for Temporal Data Analysis Advanced Material, 2410432 (2024)
- Taegyun Park†, Jihun Kim†, Young Jae Kwon, Han Joon Kim, Seong Pil Yim, Dong Hoon Shin, Yeong Rok Kim, Hae Jin Kim\*, and Cheol Seong Hwang\* Au-Nanodots Embedded Self-Rectifying Analog Charge Trap Memristor with Modified Bias Voltage Application Method for Stable Multi-Bit Hardware-Based Neural Network Advanced Materials Technologies (2024)
- Han Sol Park, Seungheon Choi, Kyung Do Kim, Min Kyu Yeom, Suk Hyun Lee, Seung Kyu Ryoo and Cheol Seong Hwang Optimization of the 4 nm-Thick Hf1-xZrxO2 Film with Low Operating Voltage and High Endurance for Ferroelectric Random Access MemoryACS Applied Electronic Materials (2024)
- Jonghoon Shin, Dong Hoon Shin, Kyung Do Kim, Haengha Seo, Kun Hee Ye, Jeong Woo Jeon, Tae Kyun Kim, Heewon Paik, Haewon Song, Suk Hyun Lee, Jung-Hae Choi and Cheol Seong Hwang Reversible Modulation of Critical Electric Fields for Field-Induced Ferroelectric Effect with Field-Cycling in ZrO2 Thin Films Journal of Materials Chemistry C, 2024, 12, 15423 - 15434
- Jae Hoon Lee, Yonghee Lee, Joon-Kyu Han, Kyung Do Kim, Seung Ryong Byun, Hyeon Woo Park\* and Cheol Seong Hwang\* Gate Engineering Effect in Ferroelectric Field-Effect Transistors with Al-Doped HfO2 Thin Film and Amorphous Indium-Gallium-Zinc-Oxide Channel Advanced Electronic Materials, 240516 (2024)
- Soo Hyung Lee†, Sunwoo Cheong†, Jea Min Cho†, Nestor Genzi, Dong Hoon Shin, Yoon Ho Jang, Janguk Han, Tae Won Park, Dong Yun Kim, Sung Keun Shim, Joon-Kyu Han, Seung Soo Kim,\* and Cheol Seong Hwang\* In-Materia Annealing and Combinatorial Optimization Based on Vertical Memristive Array Advanced Materials (2024)
- Yoon Ho Jang†, Joon-Kyu Han†, and Cheol Seong Hwang\* A review of memristive reservoir computing for temporal data processing and sensing Infoscience (2024) DOI:10.1002/inc2.12013
- Sahngik A. Mun†, Yoon Ho Jang†, Janguk Han, Sung Keun Shim, Sukin Kang, Yonghee Lee, Jinheon Choi, Sunwoo Cheong, Soo Hyung Lee, Seung Kyu Ryoo, Joon-Kyu Han\*, and Cheol Seong Hwang\* High-Dimensional Physical reservoir with Back-End-of-Line-Compatible Tin Monoxide Thin-Film Transistor ACS Applied Materials and Interfaces (2024) DOI: 10.1021/acsami.4c07747
- Jinheon Choi, Yonghee Lee, Sukin Kang, Sahngik Aaron Mun. and Cheol Seong Hwang Optimizing the Performance of the Atomic-Layer-Deposited Zinc-Tin-Oxide Thin Film Transistor by Ozone Treatment and Thermal Annealing ACS applied electronic material, (2024), 6, 8, 5961-5972 DOI: 10/1021/acsaelm.4c00916
- Yoon Ho Jang†, Soo Hyung Lee†, Janguk Han, Sunwoo Cheong, Sung Keun Shim, Joon-Kyu Han, Seung Kyu Ryoo, and Cheol Seong Hwang\* Memristive Crossbar Array-Based Probabilistic Graph Modeling Advanced Materials, 2403904, (2024)
- Dong Hoon Shin†, Sunwoo Cheong†, Soo Hyung Lee, Yoon Ho Jang, Taegyun Park, Janguk Han, Sung Keun Shim, Yeong Rok Kim, Joon-Kyu Han, In Kyung Baek, Néstor Ghenzi\* and Cheol Seong Hwang\* Heterogeneous density-based clustering with a dual-functional memristive array Materials Horizons, 11, 4493 (2024) DOI : 10.1039/D4MH00300D
- Kyung Do Kim, Seung Kyu Ryoo, Han Sol Park, Seungheon Choi, Tae Won Park, Min Kyu Yeom and Cheol Seong Hwang Comparative study on the stability of ferroelectric polarization of HfZrO2 and AlScN thin films over the depolarization effect Journal of Applied Physics, 136, 024101 (2024)
- Haengha Seo, Han Sol Park, Seong Tak Cho, Jonghoon Shin, Junil Lim, Tae Kyun Kim, Heewon Paik, Haewon Song and Cheol Seong Hwang Internal strain identification of seed-layered ZrO2, aluminum-, and yttrium-doped ZrO2 thin films via grazing incidence x-ray diffraction Journal of Applied Physics, 136, 1, 015301 (2024)
- Kyung Seok Woo†, Hyungjun Park†, Nestor Ghenzi, A. Alec Talin, Taeyoung Jeong, Jung-Hae Choi, Sangheon Oh, Yoon Ho Jang, Janguk Han, R. Stanley Williams, Suhas Kumar\*, and Cheol Seong Hwang\* Memristors with Tunable Volatility for Reconfigurable Neuromorphic Computing ACS Nano (2024)
- In Kyung Baek†, Soo Hyung Lee†, Yoon Ho Jang, Hyungjun Park, Jaehyun Kim, Sunwoo Cheong, Sung Keun Shim, Janguk Han, Joon-Kyu Han, Gwang Sik Jeon, Dong Hoon Shin, Kyung Seok Woo\* and Cheol Seong Hwang\* Implementation of Bayesian networks and Bayesian inference using a Cu0.1Te0.9/HfO2/Pt threshold switching memristor Nanoscale Adv, Advance Article (2024)
- Kyung Seok Woo†, Janguk Han†, Su-in Yi, Luke Thomas, Hyunjun Park, Suhas Kumar\* and Cheol Seong Hwang\* Tunable stochastic memristors for energy-efficient encryption and computing Nature Communications, 15, 3245 (2024)
- Kyung Seok Woo†, Yonghee Lee†, Joon-Kyu Han, Tae Won Park, Yoon Ho Jang and Cheol Seong Hwang A ternary gate-connected threshold switching thin-film transistor Appl. Phys. Lett. 124, 153503 (2024)
- Dong Hoon Shin, Hyungjun Park, Néstor Ghenzi, Yeong Rok Kim, Sunwoo Cheong, Sung Keun Shim, Seongpil Yim, Tae Won Park, Haewon Song, Jung Kyu Lee, Byeong Su Kim, Taegyun Park\*, and Cheol Seong Hwang\*Multiphase Reset Induced Reliable Dual-Mode Resistance Switching of the Ta/HfO2/RuO2 memrister ACS Appl. Mater. Interfaces (2024) DOI: 10.1021/acsami.3c19523
- Taeyoung Jeong, In Won Yeu, Kun Hee Ye, Seungjae Yoon, Dohyun Kim, Cheol Seong Hwang\* and Jung-Hae Choi\* Study of a charge transition-driven resistive switching mechanism in TiO2-based random accress memory via density functional theory Nanoscale, Advance Article (2024) DOI: 10.1039/D3NR06614B
- Jeong Woo Jeon,† Byongwoo Park,† Yoon Ho Jang, Soo Hyung Lee, Sangmin Jeon, Janguk Han, Seung Kyu Ryoo, Kyung Do Kim, Sung Keun Shim, Sunwoo Cheong, Wonho Choi, Gwangsik Jeon, Sungjin Kim, Chanyoung Yoo, Joon-Kyu Han,\* and Cheol Seong Hwang\* Vertically Stackable Ovonic Threshold Switch Oscillator Using Atomic Layer Deposited Ge0.6Se0.4 Film for High-Density Artificial Neural Networks ACS Appl. Mater. Interfaces 16, 12, 15032–15042 (2024) DOI: 10.1021/acsami.3c18625
- Jonghoon Shin, Haengha Seo, Kun Hee Ye, Yoon Ho Jang, Dae Seon Kwon, Junil Lim, Tae Kyun Kim, Heewon Paik, Haewon Song, Ha Ni Kim, Seungyong Byun, Seong Jae Shin, Kyung Do Kim, Yong Bin Lee, In Soo Lee, Jung-Hae Choi and Cheol Seong Hwang\* Understanding phase evolution of ferroelectric Hf0.5Zr0.5O2 thin films with Al2O3 and Y2O3 inserted layers Journal of Materials Chemistry C, 12, 5035 - 5046 (2024)
- Haewon Song, Bowen Wang, Jonghoon Shin, Yu-kyung Park, Heewon Paik, Haengha Seo, Junil Lim, Daeson Kwon, Keonuk Lee, Young Sin Kim, Doon Hoon Shin, and Cheol Seong Hwang\* Improved electrical performance of ultra-thin BexMg1-xO films using super-cycle atomic layer deposition Journal of Materials Chemistry C (2024) DOI: 10.1039/d3tc04338j
- Jaehyun Kim†, Joon-Kyu Han†, Ho-Young Maeng, Janguk Han, Jeong Woo Jeon, Yoon Ho Jang, Kyung Seok Woo, Yang-Kyu Choi\*, and Cheol Seong Hwang\* Fully CMOS-Based p-Bits with a Bistable Resistor for Probabilistic Computing Advanced Functional Materials, 2307935, (2024)
- Sung Keun Shim†, Yoon Ho Jang†, Janguk Han, Jeong Woo Jeon, Dong Hoon Shin, Yeong Rok Kim, Joon-Kyu Han, Kyung Seok Woo, Soo Hyung Lee, Sunwoo Cheong, Jaehyun Kim, Haengha Seo, Jonghoon Shin, Cheol Seong Hwang\* 2Memristor-1Capacitor Integrated Temporal Kernel for High-Dimensional Data Mapping SMALL, 2306585, (2024)
- Yoon Ho Jang†, Janguk Han†, Sung Keun Shim, Sunwoo Cheong, Soo Hyung Lee, Joon-Kyu Han, and Cheol Seong Hwang\* Cross-Wired Memristive Crossbar Array for Effective Graph Data Analysis Advanced Materials, 2311040, (2024)

**2023**

- Nestor Ghenzi†, Tae Won Park†, Seung Soo Kim, Hae Jin Kim, Yoon Ho Jang, Kyung Seok Woo\* and Cheol Seong Hwang\* Heterogeneous reservoir computing in second-order Ta2O5/HfO2 memristors Nanoscale Horizons, (2024) DOI: 10.1039/D3NH00493G
- Yoon Ho Jang†, Soo Hyung Lee†, Janguk Han, Woohyun Kim, Sung Keun Shim, Sunwoo Cheong, Kyung Seok Woo, Joon-Kyu Han, and Cheol Seong Hwang\* Spatiotemporal Data Processing with Memristor Crossbar-Array-Based Graph Reservoir Advanced Materials, 2309314, (2023), DOI: 10.1039/D3MH01584J
- Sunjin Lee†, Yonghee Lee†, Sukin Kang, Sahngik Mun, Jinheon Choi, and Cheol Seong Hwang \* Thickness-Dependent Growth Behaviors of Sputtered Amorphous InGaZnO Films Depending on the Substrates and Sputtering Conditions ACS Applied Electronic Materials, (2023), DOI: 10.1021/acsaelm.3c01190
- Yoon Ho Jang†, Joon-Kyu Han†, Sangik Moon, Sung Keun Shim, Janguk Han, Sunwoo Cheong, Soo Hyung Lee and Cheol Seong Hwang \* A high-dimensional in-sensor reservoir computing system with optoelectronic memristors for high performance neuromorphic machine vision Materials Horizons, (2023), DOI: 10.1039/D3MH01584J
- Sunwoo Cheong†, Dong Hoon Shin†, Soo Hyung Lee, Yoon Ho Jang, Taegyun Park, Janguk Han, Sung Keun Shim, Yeong Rok Kim, Joon-Kyu Han, Néstor Ghenzi,\* and Cheol Seong Hwang\* Parallel Density-Based Spatial Clustering with Dual-Functional Memristive Crossbar Array Advanced Functional Materials, 2309108, (2023)
- Chanyoung Yoo†, Jeong Woo Jeon†, Byongwoo Park, Wonho Choi, Gwangsik Jeon, Sangmin Jeon, Sungjin Kim, and Cheol Seong Hwang\* A Review of Advances in Deposition Methods and Material Properties of Superlattice Phase-Change Memory ACS Applied Electronic Materials (2023)
- Kyung Do Kim, Yong Bin Lee, Suk Hyun Lee, In Soo Lee, Seung Kyu Ryoo, Seung Yong Byun, Jae Hoon Lee and Cheol Seong Hwang Impact of operation voltage and NH3 annealing on the fatigue characteristics of ferroelectric AlScN thin films grown by sputtering Nanoscale, 15, 16390 - 16402 (2023)
- Kun Hee Ye, In Won Yeu, Gyuseung Han, Taeyoung Jeong, Seungjae Yoon, Dohyun Kim, Cheol Seong Hwang\*, and Jung-Hae Choi\* Comprehensive interpretations of thermodynamic and kinetic effects on the phase fractions in Hf1-xZrxO2 by first principle calculations Appl. Phys. Rev. 10, 031419 (2023)
- José P. B. Silva, Ruben Alcala, Uygar E. Avci, Nick Barrett, Laura Bégon-Lours, Mattias Borg, Seungyong Byun, Sou-Chi Chang, Sang-Wook Cheong, Duk-Hyun Choe, Jean Coignus, Veeresh Deshpande, Athanasios Dimoulas, Catherine Dubourdieu, Ignasi Fina, Hiroshi Funakubo, Laurent Grenouillet, Alexei Gruverman, Jinseong Heo, Michael Hoffmann, H. Alex Hsain, Fei-Ting Huang, Cheol Seong Hwang, Jorge Íñiguez, Jacob L. Jones , Ilya V. Karpov, Alfred Kersch, Taegyu Kwon, Suzanne Lancaster, Maximilian Lederer, Younghwan Lee, Patrick D. Lomenzo, Lane W. Martin, Simon Martin, Shinji Migita, Thomas Mikolajick, Beatriz Noheda, Min Hyuk Park, Karin M. Rabe, Sayeef Salahuddin, Florencio Sánchez, Konrad Seidel, Takao Shimizu, Takahisa Shiraishi, Stefan Slesazeck, Akira Toriumi, Hiroshi Uchida, Bertrand Vilquin, Xianghan Xu, Kun Hee Ye, Uwe Schroeder Roadmap on ferroelectric hafnia- and zirconia-based materials and devices APL materials, 11, 8, 089901 (2023)
- Chanyoung Yoo†, Wonho Choi†, Sangmin Jeon, Jeong Woo Jeon, Byongwoo Park, Gwangsik Jeon, In-Hwan Baek, and Cheol Seong Hwang\* Top-to-Bottom Local Epitaxial Growth of the Two-Dimensional Antimony Telluride Film by Atomic Layer Deposition Using Sacrificial Germanium Telluride Chemistry of Materials, 35, 17, 7311-7321 (2023)
- Hyeon Woo Park†, Seungyong Byun†, Kyung Do Kim, Seung Kyu Ryoo, In Soo Lee,Yong Bin Lee, Suk Hyun Lee, Hyun Woo Nam, Jae Hoon Lee, Jae Hee Song,Sung Jae Shin, and Cheol Seong Hwang\* Exploring the Physical Origin of the Negative CapacitanceEffect in a Metal–Ferroelectric–Metal–Dielectric Structure Advanced Functional Materials, 2304754 (2023)
- Seungjae Yoon, Gyuseung Han, Kun Hee Ye, Taeyoung Jeong, Cheol Seong Hwang, and Jung-Hae Choi A first principles study of the in-plane strain effects on the dielectric constant of high-κ Be0.25Mg0.75O superlattice Journal of Applied Physics, 134, 054102 (2023)
- Junil Lim†, Kun Hee Ye†, Dae Seon Kwon, Haengha Seo, Tae Kyun Kim, Heewon Paik, Jonghoon Shin, Haewon Song, Yoon Ho Jang, Jung-Hae Choi\*, and Cheol Seong Hwang\* Enhancing the Crystallization and Properties of the SrRuO3 Electrode Film Grown by Atomic-Layer-Deposited SrO and Pulsed-Chemical Vapor-Deposited RuO2 through Al Substitution ACS Appl. Electron. Mater. (2023)
- Junil Lim, Dae Seon Kwon, Haengha Seo, Tae Kyun Kim, Heewon Paik, Jonghoon Shin, Haewon Song, Yoon Ho Jang, Yu-kyung Park, Keonuk Lee, Young Sin Kim, Jung-Hae Choi\*, and Cheol Seong Hwang\* Improving the Properties of SrRuO3 Electrode Films Grown by Atomic Layer-Deposited SrO and Pulsed Chemical Vapor-Deposited RuO2 Using Al2O3 Capping Layers ACS Appl. Electron. Mater. (2023)
- Kyung Do Kim, Yong Bin Lee, Suk Hyun Lee, In Soo Lee, Seung Kyu Ryoo, Seungyong Byun, Jae Hoon Lee, Hani Kim, Hyeon Woo Park\*, and Cheol Seong Hwang\* Influences of the inhomogeneity of the ferroelectric thin films on switching current MRS Communications, 13, 5 (2023)
- Whayoung Kim†, Sukin Kang†, Yonghee Lee, Sahngik Mun, Jinheon Choi, Sunjin Lee and Cheol Seong Hwang Electrical properties of amorphous Zn–Sn–O thin films depending on composition and post-deposition annealing temperature near crystallization temperature Journal of Materials Chemistry C, 11, 8254-8262 (2023)
- Beom Yong Kim†, In Soo Lee†, Hyeon Woo Park, Yong Bin Lee, Suk Hyun Lee, Minsik Oh, Seung Kyu Ryoo, Seung Ryong Byun, Kyung Do Kim, Jae Hoon Lee, Deok Yong Cho, Min Hyuk Park, and Cheol Seong Hwang Top Electrode Engineering for High-Performance Ferroelectric Hf0.5Zr0.5O2 Capacitors Advanced Materials Technologies, 2300146 (2023)
- Taegyun Park†, Seung Soo Kim†, Byeol Jun Lee, Tae Won Park, Hae Jin Kim\* and Cheol Seong Hwang\* Highly Parallel Stateful Boolean Logic Gates based on Aluminum-doped Self-Rectifying Memristors in a Vertical Crossbar Array Structure Nanoscale, 15, 6387-6395 (2023).
- Wonho choi, Gilseop Kim, Hyun Young Kim, Chanyoung Yoo, Jeong Woo Jeon, Byongwoo Park, Gwangsik Jeon, Sangmin Jeon, Sukin Kang, Yonghee Lee, and Cheol Seong Hwang\* Parallel integration of Nanoscale Atomic Layer Deposited Ge2Sb2Te5 Phase-Change Memory with an Indium Gallium Zinc Oxide Thin-Film Transistor ACS Applied Electronic Materials, 5, 1721-1729 (2023)
- Kyung Do Kim, Yong Bin Lee, Suk Hyun Lee, In Soo Lee, Seung Kyu Ryoo, Seungyong Byun, Jae Hoon Lee, Hani Kim, Hyeon Woo Park\* and Cheol Seong Hwang\* Evolution of the Ferroelectric Properties of AlScN Film by Electrical Cycling with an Inhomogeneous Field Distribution Advanced Electronic Materials, 2201142, (2023)
- Sangmin Jeon, Jeong Woo Jeon, Wonho Choi, Byongwoo Park, Gwangsik Jeon, Chanyoung Yoo\* and Cheol Seong Hwang\* Enhanced pseudo-atomic layer deposition of antimony telluride thin films by co-injecting NH3 gas with both precursors J. Mater. Chem. C, 11, 3726-3735 (2023) 2023 HOT Journal of Materials Chemistry C article
- Yoon Ho Jang†, Janguk Han†, Jihun Kim, Woohyun Kim, Kyung Seok Woo, Jaehyun Kim, and Cheol Seong Hwang\* Graph Analysis with Multifunctional Self-Rectifying Memristive Crossbar Array Advanced Materials, 2209503 (2022).
- Taegyun Park†, Yeong Rok Kim†, Dong Hoon Shin, Byeol Jun Lee, and Cheol Seong Hwang\* Efficient Method for Error Detection and Correction in In-Memory Computing Based on Reliable Ex-Logic Gates Advanced Intelligent Systems, 2200341 (2023).

**2022**

- Hyeon Woo Park, Minsik Oh, In Soo Lee, Seungyong Byun, Yoon Ho Jang, Yong Bin Lee, Beom Yong Kim, Suk Hyun Lee, Seung Kyu Ryoo, Doosup Shim, Jae Hoon Lee, Hani Kim, Kyung Do Kim, and Cheol Seong Hwang\* Double S-Shaped Polarization – Voltage Curve and Negative Capacitance from Al2O3-Hf0.5Zr0.5O2-Al2O3 Triple-Layer Structure Adv. Funct. Mater. 2206637, (2022)
- Seung Soo Kim†, Soo Kyeom Yong†, Jin Myung Choi, Tae Won Park, Hyun Young Kim, Hae Jin Kim\*, and Cheol Seong Hwang\* Fabrication of a Hole-Type Vertical Resistive-Switching Random-Access Array and Intercell Interference Induced by Lateral Charge Spreading Advanced Electronic Materials, 2022
- Seung Kyu Ryoo†, Beom Yong Kim†, Yong Bin Lee, Hyeon Woo Park, Suk Hyun Lee, Minsik Oh, In Soo Lee, Seung Yong Byun, Doo Sup Shim, Jae Hoon Lee, Ha Ni Kim, Kyung Do Kim, and Cheol Seong Hwang\* Atomic layer deposition of HfNx films and improving the film performance by annealing under NH3 atmosphere Journal of Materials Chemistry C (2023)
- Xiang yuan li, Tae Hyung Park, Seung Dam Hyun, and Cheol Seong Hwang\* Performance Improvement of an Al/TiO2/Al Electronic Bipolar Resistive Switching Memory Cell via Inserting an Ultrathin ZrO2 Layer ACS Appl. Electron. Mater., 2022, 4, 5351−5360
- Chanyoung Yoo, Jeong Woo Jeon, Seungjae Yoon, Yan Cheng, Gyuseung Han, Wonho Choi, Byongwoo Park, Gwangsik Jeon, Sangmin Jeon, Woohyun Kim, Yonghui Zheng, Jongho Lee, Junku Ahn, Sunglae Cho, Scott B. Clendenning, Ilya V. Karpov, Yoon Kyung Lee, Jung-Hae Choi, and Cheol Seong Hwang\* Atomic Layer Deposition of Sb2Te3/GeTe Superlattice Film and Its Melt-Quenching-Free Phase-Transition Mechanism for Phase-Change Memory Advanced Materials, 2207143 (2022)
- Kyung Seok Woo†, Jaehyun Kim†, Janguk Han, Woohyun Kim, Yoon Ho Jang & Cheol Seong Hwang Probabilistic computing using Cu0.1Te0.9/HfO2/Pt diffusive memristors Nature Communications, 13, 5762 (2022)
- Hyo Cheon Woo, Jihun Kim, Sunwoo Lee, Hae Jin Kim, and Cheol Seong Hwang\* Stacked One-Selector-One-Resistive Memory Crossbar Array With High Nonlinearity and On-Current Density for the Neuromorphic Applications Adv. Electron. Mater. 2022, 2200656
- Seung Kyu Ryoo†, Kyung Do Kim†, Hyeon Woo Park, Yong Bin Lee, Suk Hyun Lee, In Soo Lee, Seungyong Byun, Doosup Shim, Jae Hoon Lee, Hani Kim, Yoon Ho Jang, Min Hyuk Park, and Cheol Seong Hwang\* Investigation of Optimum Deposition Conditions of Radio Frequency Reactive Magnetron Sputtering of Al0.7Sc0.3N Film with Thickness down to 20 nm Adv. Electron. Mater., 2200726 (2022)
- Juseong Park, Jungwoo Choi, Gwangmin Kim, Geunyoung Kim, Gil Seop Kim, Hanchan Song, Yeong Seok Kim, Younghyun Lee, Hakseung Rhee, Hyuck Mo Lee, Cheol Seong Hwang\* and Kyung Min Kim\* Modified Dynamic Physical Model of Valence Change Mechanism Memristors ACS Appl. Mater. Interfaces (2022)
- Gyuseung Han, In Won Yeu, Kun Hee Ye, Seungjae Yoon, Taeyoung Jeong, Seung-Cheol Lee, Cheol Seong Hwang and Jung-Hae Choi\* Temperature-dependent bandgap of (In,Ga)As via P5Grand: A Python Package for Property Prediction of Pseudobinary systems using Grand canonical ensemble Chemical Physics Letters, 804, 139887 (2022)
- Yong Bin Lee, Beom Yong Kim, Hyeon Woo Park, Suk Hyun Lee, Minsik Oh, Seung Kyu Ryoo, In Soo Lee, Seungyong Byun, Doosup Shim, Jae Hoon Lee, Hani Kim, Kyung Do Kim, Min Hyuk Park, Cheol Seong Hwang\* Oxygen-Scavenging Effects of Added Ti Layer in the TiN Gate of Metal-Ferroelectric-Insulator-Semiconductor Capacitor with Al-doped HfO2 Ferroelectric Film Advanced Electronic Materials, 2200310 (2022)
- Seung Soo Kim, Soo Kyeom Yong, Whayoung Kim, Sukin Kang, Hyeon Woo Park, Kyung Jean Yoon, Dong Sun Sheen, Seho Lee, and Cheol Seong Hwang\* Review of Semiconductor Flash Memory Devices for Material and Process Issues Advanced Materials, 2200659 (2022) DOI:10.1002/adma.202200659
- Dae Seon Kwon, Tae Kyun Kim, Junil Lim, Haengha Seo, Heewon Paik, and Cheol Seong Hwang\* Enhanced Electrical Properties of an Al-Doped TiO2 Dielectric Film on a TiN Electrode by Adopting an Atomic Layer Deposited Ru Interlayer ACS Applied Electronic Materials, 4, 4, 2005-2014 (2022)
- Bo Wen Wang, Seungsoo Kim, Haewon Song, Haengha Seo, Xiangyuan Li, Jin Myung Choi, Jinwoo Choi, Jonghoon Shin and Cheol Seong Hwang Improving the water-resistance of MgO-based metal–insulator–metal capacitors by inserting a BeO thin film grown via atomic layer deposition J. Mater. Chem. C, 2022, Advance Article (2022) DOI: 10.1039/d2tc00595f
- Haengha Seo, In Won Yeu, Dae Seon Kwon, Dong Gun Kim, Junil Lim, Tae Kyun Kim, Heewon Paik, Jung-Hae Choi and Cheol Seong Hwang The Contrasting Impacts of the Al2O3 and Y2O3 Insertion Layers on the Crystallization of ZrO2 Films for Dynamic Random Access Memory Capacitors Advanced Electronic Materials, 8, 7 (2022)
- Woon Hyung Cheong, Jae Bum Jeon, Jae Hyun In, Geunyoung Kim, Hanchan Song, Janho An, Juseong Park, Young Seok Kim, Cheol Seong Hwang,\* and Kyung Min Kim\* Demonstration of Neuromodulation-inspired Stashing System for Energy-efficient Learning of Spiking Neural Network using a Self-Rectifying Memristor Array Adv. Funct. Mater. 2022, 2200337
- Uwe Schroeder, Min Hyuk Park, Thomas Mikolajick & Cheol Seong Hwang The fundamentals and applications of ferroelectric HfO2 Nature Review Materials, doi: 10.1038/s41578-022-00431-2 (2022)
- Gyuseung Han, In Won Yeu, Kun Hee Ye, Cheol Seong Hwang, and Jung-Hae Choi\* Atomistic prediction on the composition- and configuration-dependent bandgap of Ga(As,Sb) using cluster expansion and ab initio thermodynamics Materials Science and Engineering B, 280 115713 (2022)
- Taegyun Park, Yeong Rok Kim, Jihun Kim, Jinwon Lee, and Cheol Seong Hwang\* Reliable Domain-Specific Exclusive Logic Gates Using Reconfigurable Sequential Logic Based on Antiparallel Bipolar Memristors Advanced Intelligent Systems, 2100267 (2022)
- Jihun Kim, Hyo Cheon Woo, Sunwoo Lee, Byeol Jun Lee, Taegyun Park, and Cheol Seong Hwang\* Training method for accurate Off-Chip training of one-selector-one-resistor crossbar array with nonlinearity and wire resistance Advanced Intelligent Systems, 2100256 (2022)
- Young Geun Song†, In-Hwan Baek†, Jae-Gyun Yim, Taeyong Eom, Teak-Mo Chung, Chul-Ho Lee, Cheol Seong Hwang, Chong-Yun Kang\*, and Seong Keun Kim\* Cross-linked structure of self-aligned p-type SnS nanoplates for highly sensitive NO2 detection at room temperature Journal of Materials Chemistry A, DOI: 10.1039/d1ta11014d
- Hyeon Woo Park, Minsik Oh, and Cheol Seong Hwang\* Negative Capacitance from the Inhomogenous Stray Field in a Ferroelectric–Dielectric Structure Adv. Funct. Mater. 2022, 2200389
- Yan Cheng, Zhaomeng Gao, Kun Hee Ye, Hyeon Woo Park, Yonghui Zheng, Yunzhe Zheng, Jianfeng Gao, Min Hyuk Park, Jung-Hae Choi, Kan-Hao Xue, Cheol Seong Hwang\* and Hangbing Lyu\* Reversible transition between the polar and antipolar phases and its implications for wake-up and fatigue in HfO2-based ferroelectric thin film Nature Communications volume 13, Article number: 645 (2022)

**2021**

- Jeong Woo Jeon, Chanyoung Yoo, Woohyun Kim, Wonho Choi, Byongwoo Park, Yoon Kyeung Lee\* and Cheol Seong Hwang\* Atomic layer deposition of SnSex thin films using Sn(N(CH3)2)4 and Se(Si(CH3)3)2 with NH3 coinjection Dalton Trans., 2022, 51, 594-601
- Jihun Kim, Hyo Cheon Woo, Taeyoung Jeong, Jung-Hae Choi, and and Cheol Seong Hwang In-Depth Analysis of One Selector–One Resistor Crossbar Array for Its Writing and Reading Operations for Hardware Neural Network with Finite Wire Resistance Advanced Intelligent Systems, 2100174 (2021)
- In Hwan Baek, Ah Jin Cho, Ga Yeon Lee, Heenang Choi, Sung Ok Won, Taeyong Eom, Taek Mo Chung, Cheol Seong Hwang and Seong Keun Kim\* Enhancement of electrical performance of atomic layer deposited SnO films via substrate surface engineering Journal of Materials Chemistry C, 2021, 9, 12314-12321
- Bo Wen Wang, Jinwoo Choi, Hyoung Gyun Kim, Seung Dam Hyun, Chanyoung Yoo, Seungsoo Kim, Hoin Lee and Cheol Seong Hwang\* Influences of oxygen source and substrate temperature on the unusual growth mechanism of atomic layer deposited magnesium oxide using bis(cyclopentadienyl)magnesium precursor Journal of Materials Chemistry C, 2021, 9, 15359-15374
- Yoon Ho Jang, Woohyun Kim, Jihun Kim, Kyung Seok Woo, Hyun Jae Lee, Jeong Woo Jeon, Sung Keun Shim, Janguk Han, and Cheol Seong Hwang\* Time-varying data processing with nonvolatile memristor-based temporal kernel Nature Communications, 12, 5727 (2021)
- Beom Yong Kim, Se Hyun Kim, Hyeon Woo Park, Yong Bin Lee, Suk Hyun Lee, Minsik Oh, Seung Kyu Ryoo, In Soo Lee, Seungyong Byun, Doosup Shim, Min Hyuk Park\*, Cheol Seong Hwang\* Improved ferroelectricity in Hf0.5Zr0.5O2 by inserting an upper HfOxNy interfacial layer Appl. Phys. Lett. 119, 122902 (2021)
- Yu Yan, Jia Cheng Li, Yu Ting Chen, Xiang Yu Wang, Gang Ri Cai, Hyeon Woo Park, Ji Hun Kim, Jin Shi Zhao,\* and Cheol Seong Hwang\* Area-Type Electronic Bipolar Switching Al/TiO1.7/TiO2/Al Memory with Linear Potentiation and Depression Characteristics ACS Applied Materials & Interface （2021）
- Nuo Xu‡, Taegyun Park‡, Kyung Jean Yoon\*, Cheol Seong Hwang\* In-Memory Stateful Logic Computing Using Memristors: Gate, Calculation, and Application Physica Status Solidi RRL, 2100208 (2021)
- In Won Yeu, Gyuseung Han, Kun Hee Ye, Cheol Seong Hwang, Jung-Hae Choi InterPhon: Ab initio interface phonon calculations within a 3D electronic structure framework Computer Physics Communications, 268, 108089 (2021)
- Kyung Seok Woo, Jaehyun Kim, Janguk Han, Jin Myung Choi, Woohyun Kim, and Cheol Seong Hwang\* A High-Speed True Random Number Generator Based on a CuxTe1-x Diffusive Memristor Advanced Intelligent Systems, 2100062 (2021)
- Hae Jin Kim, Jihun Kim, Tae Gyun Park, Jung Ho Yoon\*, and Cheol Seong Hwang\* Multi-Level Control of Conductive Filament Evolution and Enhanced Resistance Controllability of the Cu-Cone Structure Embedded Conductive Bridge Random Access Memory Advanced Electronic Materials, 2100209 (2021)
- Hyun Jae Lee, Taehwan Moon, Sukin Kang, Woohyun Kim, and Cheol Seong Hwang\* Threshold Voltage Modulation in a Transistor with a Two-Dimensional Electron Gas Channel at the Interface between Al2O3 and Sub-5 nm ZnO Films ACS Applied Electronic Materials, Article ASAP, DOI: 10.1021/acsaelm.1c00410
- Dae Seon Kwon, Woojin Jeon, Dong Gun Kim, Tae Kyun Kim, Haengha Seo, Junil Lim, and Cheol Seong Hwang\* Improved Properties of the Atomic Layer Deposited Ru Electrode for Dynamic Random-Access Memory Capacitor Using Discrete Feeding Method ACS Applied Materials & Interfaces, 13, 23915-23927 (2021)
- Beom Yong Kim, Hyeon Woo Park, Seung Dam Hyun, Yong Bin Lee, Suk Hyun Lee, Minsik Oh, Seung Kyu Ryoo, In Soo Lee, Seungyong Byun, Doosup Shim, Deok-Yong Cho, Min Hyuk Park\*, and Cheol Seong Hwang\* Enhanced Ferroelectric Properties in Hf0.5Zr0.5O2 Films Using a HfO0.61N0.72 Interfacial Layer Adv. Electron. Mater. 2021, 2100042
- Yoon Kyeung Lee, Chanyoung Yoo, Woohyun Kim, Jeong Woo Jeon and Cheol Seong Hwang\* Atomic layer deposition of chalcogenides for next-generation phase change memory J. Mater. Chem. C, 9, 3708 - 3725 (2021)
- Dohun Kim, Guhyun Kim, Cheol Seong Hwang, Doo Seok Jeong\* eWB: Event-based weight binarization algorithm for spiking neural networks IEEE Access (2021)
- Kun Hee Ye, Gyuseung Han, In Won Yeu, Cheol Seong Hwang,\* and Jung-Hae Choi\* Atomistic Understanding of the Ferroelectric Properties of a Wurtzite-Structure (AlN)n/(ScN)m Superlattice Phys. Status Solidi (RRL)-Rapid Research Letters, 2100009 (2021)
- Dong Gun Kim, Hae-Ryoung Kim, Dae Seon Kwon, Junil Lim, Haengha Seo, Tae Kyun Kim, Heewon Paik, Woongkyu Lee and Cheol Seong Hwang Comparison of high-k Y2O3/TiO2 bilayer and Y-doped TiO2 thin films on Ge substrate J. Phys. D: Appl. Phys., 54, 185110 (2021)
- Hyeon Woo Park, Seung Dam Hyun, In Soo Lee, Suk Hyun Lee, Yong Bin Lee, Minsik Oh, Beom Yong Kim, Seung Gyu Ryoo, and Cheol Seong Hwang\* Polarizing and depolarizing charge injection through a thin dielectric layer in a ferroelectric-dielectric bilayer Nanoscale, 2021, 13, 2556-2572
- Gyuseung Han, In Won Yeu, Kun Hee Ye, Seung-Cheol Lee, Cheol Seong Hwang\* and Jung-Hae Choi\* Atomistic prediction on the configuration- and temperature-dependent dielectric constant of Be0.25Mg0.75O superlattice as a high-κ dielectric layer Journal of Materials Chemistry C, 9, 851-859 (2021)
- Jun Shik Kim, Sukin Kang, Younjin Jang, Yonghee Lee, Kwangmin Kim, Whayoung Kim, Woongkyu Lee, and Cheol Seong Hwang Investigating the Reasons for the Difficult Erase Operation of a Charge-Trap Flash Memory Device with Amorphous Oxide Semiconductor Thin-Film Channel Layers physica status solidi (RRL)–Rapid Research Letters, DOI: 10.1002/pssr.202000549
- Hyeon Woo Park, Jae-Gil Lee, and Cheol Seong Hwang\* Review of ferroelectric field-effect transistor for three-dimensional storage applications Nano Select, (2021), DOI:10.1002/nano.20200281.
- Dong Gun Kim, Dae Seon Kwon, Junil Lim, Haengha Seo, Tae Kyun Kim, Woongkyu Lee and Cheol Seong Hwang Trap Reduction through O3 Post‐Deposition Treatment of Y2O3 Thin Films Grown by Atomic Layer Deposition on Ge Substrates Advanced Electronic Materials, 202000819 (2021)
- Dong Gun Kim, Cheol Hyun An, Sanghyeon Kim, Dae Seon Kwon, Junil Lim, Woojin Jeon and Cheol Seong Hwang Optimized Al-doped TiO2 gate insulator for metal-oxide-semiconductor capacitor on Ge substrate Journal of Materials Chemistry C, 9, 1572-1583 (2021)

## 학회 발표 (2021–2026)

Conference의 연도 구역별 발표 항목 200건이다. 연도별 건수로 정리했으며 같은 논문의 다른 학회 발표는 각각의 게시 항목이다.[^conference]

| 연도 구역 | 발표 항목 수 |
|---|---|
| 2026 | 69 |
| 2025 | 22 |
| 2024 | 26 |
| 2023 | 30 |
| 2022 | 28 |
| 2021 | 25 |

## 특허

누리집 Patent의 2021–2026년 구역 가운데 기재일이 2021년 10월 22일–2026년 10월 22일에 드는 42건이다. 날짜는 누리집에 특허 번호와 함께 적힌 날짜이며 출원일·등록일의 구분은 별도로 표시되어 있지 않다.[^patents]

- 2026-09-15 · 메모리 소자 및 그 제조 방법 (발명자 황철성, 신중찬; 국가 미국; 번호 12740073)
- 2026-09-15 · 커패시터리스 3차원 적층형 DRAM 소자 및 그 제조 방법 (발명자 황철성, 장서영, 이한철; 국가 미국; 번호 12740040)
- 2026-09-09 · 강유전체 재료 구조, 이를 포함하는 강유전체 메모리 소자 및 이의 제조 방법 (발명자 황철성, 김경도; 국가 대한민국; 번호 10-3019004-00-00)
- 2026-09-09 · 강유전체 소자, 이를 포함하는 강유전체 메모리 소자 및 이의 제조 방법 (발명자 황철성, 류승규; 국가 대한민국; 번호 10-3018988)
- 2026-08-12 · 메모리 소자 및 그 제조 방법 (발명자 황철성, 이한철; 국가 대한민국; 번호 10-3006068)
- 2026-07-14 · 커패시터리스 3차원 DRAM 소자 및 그 제조 방법 (발명자 황철성, 이선진, 장서영; 국가 미국; 번호 12684754)
- 2026-07-08 · 메모리 소자 및 그 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2990310)
- 2026-07-08 · 임계 컴퓨팅에 활용되는 시간 커널 소자, 시간 커널 컴퓨팅 시스템 및 이들의 동작 방법 (발명자 황철성, 심성근, 장윤호; 국가 대한민국; 번호 10-2990309)
- 2026-06-16 · 시간 커널 소자, 시간 커널 컴퓨팅 시스템 및 그들의 동작 방법 (발명자 황철성, 장윤호; 국가 미국; 번호 12660205)
- 2026-03-31 · 소스 전극 구조체 및 드레인 전극 구조체를 포함하는 반도체 장치 (발명자 황철성; 국가 미국; 번호 12593436)
- 2026-03-26 · 커패시터, 커패시터의 제조 방법, 커패시터를 포함하는 전자 소자 및 전자 소자의 제조 방법 (발명자 황철성, 송해원; 국가 대한민국; 번호 10-2946266)
- 2026-03-17 · 그래프 데이터 분석에 적용 가능한 크로스바 어레이 소자, 이를 포함하는 뉴로모픽 소자, 크로스바 어레이 소자의 동작 방법 및 크로스바 어레이 소자를 이용한 그래프 데이터 분석 방법 (발명자 황철성, 장윤호, 한장욱; 국가 미국; 번호 12581661)
- 2026-02-26 · 양극성 2차원 반도체를 이용한 재구성 가능한 전자 소자, 그 제조 방법 및 이를 이용한 논리 소자 (발명자 이관형, 신준철, 황철성, 신동훈, 최현영, 박태균; 국가 대한민국; 번호 10-2933349)
- 2025-12-24 · 커패시터와 그 제조 방법 및 커패시터를 포함하는 소자 (발명자 황철성; 국가 대한민국; 번호 10-2905840)
- 2025-08-08 · 메모리 소자 및 그 제조 방법 (발명자 황철성, 신중찬; 국가 대한민국; 번호 10-2845920)
- 2025-08-08 · 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2845845)
- 2025-07-08 · 원자층 증착 공정을 이용한 칼코게나이드계 박막의 형성 방법, 이를 적용한 스위칭 소자의 형성 방법 및 메모리 소자의 제조 방법 (발명자 황철성, 하만익; 국가 미국; 번호 12356873)
- 2025-06-10 · 시간 커널 소자, 시간 커널 컴퓨팅 시스템 및 이들의 동작 방법 (발명자 황철성, 심성근, 장윤호; 국가 대한민국; 번호 10-2820396)
- 2025-02-18 · 캐패시터를 갖는 반도체 소자 및 그 형성 방법 (발명자 황철성, 강상열, 조규호, 임한진; 국가 미국; 번호 12230667)
- 2024-12-06 · 커패시터리스 3차원 DRAM 소자 및 그 제조 방법 (발명자 황철성, 장서영, 이선진; 국가 대한민국; 번호 10-2741447)
- 2024-12-06 · 커패시터리스 3차원 DRAM 소자 및 그 제조 방법 (발명자 황철성, 장서영, 이선진; 국가 대한민국; 번호 10-2741443)
- 2024-11-11 · 원자층 증착 공정을 이용한 칼코게나이드계 물질층의 형성 방법, 이를 적용한 상변화 메모리 소자의 제조 방법 및 상변화 메모리 소자 (발명자 황철성, 유찬영; 국가 대한민국; 번호 10-2730369)
- 2024-10-04 · 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2715695)
- 2024-09-23 · 수직 적층형 메모리 소자 및 그 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2710383)
- 2024-09-12 · 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2707894)
- 2024-09-10 · 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2706834)
- 2024-09-03 · 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2704016)
- 2024-08-26 · 그래프 데이터 분석에 적용 가능한 크로스바 어레이 소자, 이를 포함하는 뉴로모픽 소자, 크로스바 어레이 소자의 동작 방법 및 크로스바 어레이 소자를 이용한 그래프 데이터 분석 방법 (발명자 황철성, 장윤호, 한장욱; 국가 대한민국; 번호 10-2700708)
- 2024-08-13 · 그래프 데이터 분석에 적용 가능한 크로스바 어레이 소자, 이를 포함하는 뉴로모픽 소자, 크로스바 어레이 소자의 동작 방법 및 크로스바 어레이 소자를 이용한 그래프 데이터 분석 방법 (발명자 황철성, 장윤호, 한장욱; 국가 대한민국; 번호 10-2696326)
- 2024-05-28 · 시간 커널 소자, 시간 커널 컴퓨팅 시스템 및 그들의 동작 방법 (발명자 황철성, 장윤호; 국가 일본; 번호 7495992)
- 2024-03-18 · 커패시터리스 3차원 적층형 DRAM 소자 및 그 제조 방법 (발명자 황철성, 장서영, 이한철; 국가 대한민국; 번호 10-2649968)
- 2024-02-02 · 수직형 반도체 소자 및 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2634963)
- 2023-12-26 · 캐패시터를 갖는 반도체 소자 및 그 형성 방법 (발명자 황철성, 강상열, 조규호, 임한진; 국가 중국; 번호 ZL201810971335.6)
- 2023-10-25 · 시간 커널 소자, 시간 커널 컴퓨팅 시스템 및 그들의 동작 방법 (발명자 황철성, 장윤호; 국가 대한민국; 번호 10-2595529)
- 2023-09-11 · 저항성 메모리 소자 및 이의 제조 방법 (발명자 이재연, 황철성; 국가 대한민국; 번호 10-2578854)
- 2023-04-28 · 원자층 증착 공정을 이용한 칼코게나이드계 박막의 형성 방법, 이를 이용한 스위칭 소자의 형성 방법 및 메모리 소자의 제조 방법 (발명자 황철성, 하만익; 국가 대한민국; 번호 10-2529144)
- 2023-04-28 · 원자층 증착 공정을 이용한 칼코게나이드계 박막의 형성 방법, 이를 적용한 상변화 물질층의 형성 방법 및 상변화 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2529139)
- 2023-02-07 · 비휘발성 메모리 장치 및 이의 동작 방법 (발명자 황철성, 윤정호, 미즈사키소이치로, 조영진; 국가 미국; 번호 11574677)
- 2022-09-13 · 원자층 증착 공정을 이용한 칼코게나이드계 박막의 형성 방법, 이를 이용한 스위칭 소자의 형성 방법 및 메모리 소자의 제조 방법 (발명자 황철성, 하만익; 국가 대한민국; 번호 10-2444272)
- 2022-09-13 · 원자층 증착 공정을 이용한 칼코게나이드계 박막의 형성 방법, 이를 적용한 상변화 물질층의 형성 방법 및 상변화 메모리 소자의 제조 방법 (발명자 황철성; 국가 대한민국; 번호 10-2444266)
- 2022-08-09 · 캐패시터를 갖는 반도체 소자 및 그 형성 방법 (발명자 황철성, 임한진, 조규호, 강상열; 국가 미국; 번호 11411069)
- 2022-05-26 · 캐패시터를 갖는 반도체 소자 및 그 형성 방법 (발명자 황철성, 조규호, 임한진, 강상열; 국가 대한민국; 번호 10-2404060)

## 수상과 선정

교수 소개 수상 3건과 기간 안의 DTFL News 수상·선정 글 6건을 함께 정리한 7개 항목이다. 교수 소개와 소식에 함께 있는 근정훈장과 ALD 관련 수상은 각각 한 항목으로 묶었으며, 서로 다른 이름과 날짜 표기는 함께 적었다. 소식 날짜는 게시일, 교수 소개 날짜는 연월 표기다. 우경석 수상 글은 누리집이 UNIST 교수의 성과로 소개한 것이다.[^prof][^news]

- 2026-06-12 (게시일) · 손건희 박사과정 학생, GCIM 2026 Best Oral Award 수상
- 2026-04-07 (게시일) · 연구실의 제33회 한국반도체학술대회 수상
- 2025-11-27 (게시일) · UNIST 우경석 교수, MRS Bulletin postdoc prize 수상
- 2025-07 · 황철성 교수, 대한민국최고과학기술인상 수상 (Korea Best Scientist and Technologist Award)
- 2025-04 · 황철성 교수, 황조 근정훈장 수훈 (교수 소개: Yellow Stripes Order of Service Merit; 소식 게시일 2025-04-21)
- 2025-01-10 (게시일) · 황철성 교수, Materials Horizons와 Nanoscale Horizons themed collection의 guest editor 선정
- 2022-06 · 황철성 교수, ALD 관련 수상 (교수 소개: ALD Innovation Award, Americal Vacuum Society, USA, 2022-06; 소식: Innovator Award, 게시일 2022-07-03)

## 연락과 위치

- 주소: 서울특별시 관악구 관악로 1 서울대학교 공과대학 재료공학부, 08826.[^prof]
- 교수 사무실: 33동 111호. 기관 전화 +82-2-880-7535, 팩스 +82-2-884-1413.[^prof]
- 교수 업무 이메일: cheolsh@snu.ac.kr.[^prof]
- 누리집 하단 연구실 전화: +82-2-880-8923 (7988, 8643), +82-2-889-6440. 팩스 +82-2-874-6414.[^home]
[^home]: 유전박막연구실 누리집 첫 화면. <http://dtfl.snu.ac.kr/> 열람 2026-10-30.
[^prof]: DTFL, Member > Professor. 연구실 이름, 소속, 상단 직함, 학력·경력·수상·연구 관심, 사무실·전화·이메일. <http://dtfl.snu.ac.kr/sub02/sub01.php> 열람 2026-10-30.
[^research]: DTFL, Research > New computing and Neuromorphic Research, Overview. 연구실의 비휘발성 메모리 응용, 뉴로모픽·신경망·메모리 내 연산·확률 계산 연구. <http://dtfl.snu.ac.kr/sub01/sub01_n8.php> 열람 2026-10-30.
[^pubs]: DTFL, Publication > Paper, 2021–2026년 연도 구역과 각 구역의 모든 쪽. <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2026> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2025> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2024> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2023> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2022> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&category=2021> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2025&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2025&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2024&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2023&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2022&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2021&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=paper&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> 열람 2026-10-30.
[^news]: DTFL, Board > DTFL News, 1–3쪽. <http://dtfl.snu.ac.kr/bbs/board.php?tbl=bbs02> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=bbs02&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=bbs02&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> 열람 2026-10-30.
[^correction]: Advanced Materials, Correction to “Multi-State Probabilistic Computing Using Floating-Body MOSFETs Based on the Potts Model for Solving Complex Combinatorial Optimization Problems”, 38(45), e73915, 온라인 2026-07-07. <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.73915> 에너지 비교 표의 단위와 수치 정정.
[^memory]: DTFL, Research > Memory & Logic Research. <http://dtfl.snu.ac.kr/sub01/sub01_n.php> 열람 2026-10-30.
[^dram]: DTFL, Research > 3D DRAM. <http://dtfl.snu.ac.kr/sub01/sub01_n2.php> 열람 2026-10-30.
[^capacitor]: DTFL, Research > DRAM Capacitor. <http://dtfl.snu.ac.kr/sub01/sub01_n3.php> 열람 2026-10-30.
[^tft]: DTFL, Research > Thin Film Transistor. <http://dtfl.snu.ac.kr/sub01/sub01_n4.php> 열람 2026-10-30.
[^ferro]: DTFL, Research > Ferroelectric. <http://dtfl.snu.ac.kr/sub01/sub01_n5.php> 열람 2026-10-30.
[^pcm]: DTFL, Research > Phase Change Memory. <http://dtfl.snu.ac.kr/sub01/sub01_n6.php> 열람 2026-10-30.
[^rram]: DTFL, Research > Resistive Switching Memory. <http://dtfl.snu.ac.kr/sub01/sub01_n7.php> 열람 2026-10-30.
[^members]: DTFL, Postdoctoral Fellowship·Ph. D. Student·M. S. Student 및 별도 Member 쪽. <http://dtfl.snu.ac.kr/sub02/sub02.php> <http://dtfl.snu.ac.kr/sub02/pos.php?type=pos> <http://dtfl.snu.ac.kr/sub02/pos.php?type=phd> <http://dtfl.snu.ac.kr/sub02/pos.php?type=mas> 열람 2026-10-30.
[^alumni]: DTFL, Alumni, 1–7쪽. <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=4> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=5> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=6> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=alumni&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=7> 열람 2026-10-30.
[^conference]: DTFL, Conference, 2021–2026년 연도 구역의 모든 쪽. <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2026> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2025> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2024> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2023> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2022> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&category=2021> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=4> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=5> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=6> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=7> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2025&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2025&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2024&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2024&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2023&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2023&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2022&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2022&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2021&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=conference&&category=2021&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=3> 열람 2026-10-30.
[^patents]: DTFL, Patent, 2021–2026년 연도 구역의 모든 쪽. <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2026> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2025> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2024> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2023> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2022> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&category=2021> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&&category=2026&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> <http://dtfl.snu.ac.kr/bbs/board.php?tbl=patent&&category=2024&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=2> 열람 2026-10-30.
[^p1]: Y. Lee 외, C. S. Hwang, physica status solidi (RRL) – Rapid Research Letters 19, 2500131 (온라인 2025-05-25). <https://doi.org/10.1002/pssr.202500131> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/full/10.1002/pssr.202500131> 열람 2026-10-30.
[^p2]: H. Park 외, C. S. Hwang, Advanced Materials 38, e74793 (온라인 2026-08-22). <https://doi.org/10.1002/adma.74793> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.74793> 열람 2026-10-30.
[^p3]: Y. H. Jang 외, C. S. Hwang, Advanced Materials 36, 2309314 (온라인 2023-10-25). <https://doi.org/10.1002/adma.202309314> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202309314> 열람 2026-10-30.
[^p4]: Y. H. Jang 외, C. S. Hwang, Advanced Materials 36, 2403904 (온라인 2024-07-19). <https://doi.org/10.1002/adma.202403904> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202403904> 열람 2026-10-30.
[^p5]: Y. H. Jang 외, C. S. Hwang, Advanced Materials 36, 2311040 (온라인 2023-12-25). <https://doi.org/10.1002/adma.202311040> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202311040> 열람 2026-10-30.
[^p6]: S. Cheong 외, J.-K. Han, Advanced Materials 38, e16797 (온라인 2026-02-17). <https://doi.org/10.1002/adma.202516797> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202516797> 열람 2026-10-30.

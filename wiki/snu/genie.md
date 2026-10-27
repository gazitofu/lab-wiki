# 반도체 재료 및 소자연구실 (Semiconductor Materials and Devices Laboratory, SMDL)

**서울대학교 공과대학 전기·정보공학부 · 이종호 교수**

- 분야: 3차원 낸드 플래시 메모리의 동작·신뢰성과 전하 포획층 물리, 플래시·강유전체 기반 시냅스 소자와 뉴런 회로, 메모리 내 연산과 뉴로모픽 하드웨어, FET형 가스 센서와 인공 후각 시스템, 하프니아 강유전체 소자와 저주파 잡음, 메모리 소자를 이용한 물리적 복제 방지 기능(PUF)
- 대분야: 전기전자·반도체·광학
- 태그: 메모리 반도체 소자[^nvm][^ecelabv][^p4], 뉴로모픽 소자[^neuro][^ecelabv][^p5], 메모리 내 연산[^p2][^p5][^p6], 강유전체[^ecelabv][^p7][^p8], 하드웨어 보안[^p3][^iedm], AI 반도체·가속기[^p5][^p7], 가스 센서[^p1], 센서 인터페이스·판독 집적회로[^p2]
- 홈페이지: <https://genie.snu.ac.kr/>
- 근거와 출처: [SMDL 근거 페이지](genie-sources.md)

> 반도체 소자를 직접 만들고 재고 모델링하는 연구실로, 3차원 낸드 플래시 메모리, 플래시와 강유전체 소자로 만드는 뉴로모픽 하드웨어와 메모리 내 연산, CMOS 기술과 함께 만드는 FET형 가스 센서를 중심으로 연구한다.[^home][^ecelabv]

## 무엇을 연구하나

연구실은 서울대학교 공과대학 전기·정보공학부 이종호 교수가 이끄는 연구실이다.[^eceprof][^ecelab] 학부 연구실 목록은 이름을 「반도체 재료 및 소자연구실」로 적고 반도체 물리 및 소자 연구그룹에 올리며, 누리집은 Semiconductor Materials and Devices Laboratory(SMDL)로 적는다.[^ecelab][^home] 첫 화면 소개에 따르면 연구 분야는 비휘발성 메모리(전원을 꺼도 저장한 정보가 남는 메모리), 유연 전자 소자, 가스 센서와 바이오 센서, 박막 트랜지스터(TFT, thin-film transistor. 기판 위에 입힌 얇은 반도체 막으로 만든 트랜지스터), 재구성 가능 소자·회로(동작 방식을 바꿔 쓸 수 있는 소자와 회로), 뉴로모픽 소자·회로(신경세포와 시냅스의 동작을 흉내 내 정보를 처리하는 소자와 회로)에 걸쳐 있다.[^home] 소자와 회로는 주로 캠퍼스 안의 ISRC(Inter-University Semiconductor Research Center)에서 만들고, 연구실 학생 대부분이 반도체 소자와 회로를 직접 만들어 본 경험이 있으며, 일부 소자와 회로는 반도체 회사와의 협력 과제로 받는다고 적는다. 연구 범위는 소자 제작, 측정, 특성 분석, 모델링이다.[^home] 측정 장비로는 프로브 스테이션(소자에 탐침을 대어 전기 특성을 재는 장치) 다섯 대, 반도체 파라미터 분석기 네 대, 오실로스코프, 스펙트럼 분석기, 저잡음 전류·전압 증폭기, 록인 증폭기, 레이저 광원, 잉크젯 프린터, 전사 프린터 등을 든다.[^home]

학부 연구실 상세는 연구실의 nano-scale device group이 가스 센서, 비휘발성 메모리(NVM, non-volatile memory), 강유전체(전기장을 걸지 않아도 전기 분극이 남고 그 방향을 전기장으로 뒤집을 수 있는 물질) 기반 메모리와 시냅스 소자, 신경모방(neuromorphic) 시스템을 연구한다고 소개한다.[^ecelabv] 고집적 비휘발성 메모리를 위해 여러 3차원 적층 구조의 SONOS(silicon-oxide-nitride-oxide-silicon. 실리콘·산화막·질화막·산화막·실리콘을 차례로 쌓고 질화막에 전하를 가두어 정보를 저장하는 메모리 셀 구조) 플래시 메모리와 강유전체 물질·소자를 연구하고, 산화물 반도체를 감지 물질로 쓰는 FET형 가스 센서(FET는 field-effect transistor의 줄임말로, 전계효과 트랜지스터의 전류 변화로 가스를 감지하는 센서)를 만들어 CMOS(complementary metal-oxide-semiconductor. n형과 p형 MOS 트랜지스터를 짝지어 쓰는 반도체 회로 기술)와 집적하는 연구를 한다. 최근에는 가스 센서 기술과 뉴로모픽 시스템을 집적해 에너지 효율과 신뢰성을 높이는 연구를 하고 있다고 적는다.[^ecelabv] 같은 페이지는 주요 연구과제로 「대형 언어 모델 (LLM)을 위한 3차원 낸드 플래시 기반 트랜스포머 구현」(SK하이닉스)을 든다. LLM은 large language model의 줄임말이다.[^ecelabv] 학부 교수 상세의 Research Interest 칸은 3D Bulk FinFET, 3D NAND Flash Memory, Neuromorphic Technology, Gas Sensor, Thin Film Transistors다.[^eceprof]

첫째 갈래는 **3차원 낸드 플래시 메모리의 동작과 신뢰성**이다. 낸드 플래시는 메모리 셀을 직렬로 이어 스트링으로 묶은 플래시 메모리이고, 3차원 낸드는 이 셀들을 수직으로 쌓은 구조다. Nonvolatile Memory 페이지는 3차원 적층 낸드 플래시 메모리 연구로 동작 특성 향상, 데이터 보존(retention, 저장한 정보를 시간이 지나도 유지하는 성질) 특성 개선, 동작 과정 최적화, 낸드 플래시를 이용한 뉴로모픽 배열 구현을 들고,[^nvm] 첫 화면은 3차원 적층 낸드 플래시의 제작, 모델링, 특성 분석, 시뮬레이션과 설계, 트랩(전하를 붙잡는 자리) 분석을 소개한다.[^home] 대표 논문에서는 플래시 메모리에 데이터를 쓸 때 전자가 질화규소(Si3N4) 전하 포획층 안에서 옆으로 옮겨 가는 이유를 실험과 모델로 밝혔고,[^p4] 제조 과정에서 생기는 낸드 스트링 사이의 차이를 이용해 칩마다 다른 보안 응답을 만들고 쓰지 않을 때는 숨길 수 있는 물리적 복제 방지 기능(PUF, 제조 과정에서 생기는 차이로 칩마다 고유한 응답을 만드는 보안 기능)을 수직 낸드 플래시로 구현했다.[^p3] IEEE IEDM 2025에 채택된 연구팀 논문에는 상용 자기터널접합(MTJ, 얇은 절연막을 사이에 둔 두 자성층의 자화 방향 관계에 따라 저항이 달라지는 소자) 소자의 붕괴를 이용한 PUF도 있다.[^iedm] 최근 논문 목록에는 블록 단위 소프트 지우기로 데이터 보존을 개선한 연구(Applied Physics Letters, 2026), 수직 낸드 플래시로 만든 이징 문제(서로 영향을 주고받는 이진 변수들의 에너지가 가장 낮아지는 배치를 찾는 최적화 문제) 해법기(Advanced Intelligence System, 2026), 수직 낸드 플래시 기반 베이즈 신경망(가중치를 확률 분포로 다루는 신경망, Advanced Intelligent Systems, 2026)도 있다.[^journal]

둘째 갈래는 **뉴로모픽 소자·회로와 메모리 내 연산**이다. 메모리 내 연산(in-memory computing)은 데이터를 메모리와 처리 장치 사이로 옮기지 않고 메모리 안에서 계산하는 방식이다. Neuromorphic Device & Processor 페이지는 시냅스 소자로 낸드형(수직), AND형(수평·수직), NOR형 플래시를, 뉴런 회로로 Integrate-&-fire 뉴런 회로(입력을 쌓아 문턱에 이르면 신호를 내보내는 회로), AN 뉴런 회로, PF(Positive-feedback, 양성 되먹임) 뉴런 회로를 든다. 주변 회로로는 PF 소자와 플래시 메모리를 쓴 아날로그-디지털 변환기와 펄스 폭 변조기 기반 뉴로모픽 시스템을, 마지막으로 아날로그 스파이킹 신경망(뉴런들이 스파이크라 부르는 펄스 신호를 주고받으며 정보를 처리하는 인공 신경망) 시스템용 뉴로모픽 시뮬레이터를 든다.[^neuro] 대표 논문에서는 메모리 내 연산을 위해 신경망의 양자화, 비선형 활성화, 최대 풀링을 한 모듈에 담아 면적이 작고 에너지를 적게 쓰는 플래시 게이트 사이리스터 기반 뉴로모픽 모듈을 제안하고 플래시 메모리·CMOS 트랜지스터와 한 웨이퍼에 함께 집적할 가능성을 보였으며,[^p5] 수직으로 쌓은 3차원 플래시 메모리의 구성을 이용해 합성곱 연산과 강화학습을 하는 메모리 내 연산 구조를 만들어 자율주행 경로 계획을 시연했다.[^p6] 가스 센서와 증폭 회로의 신호를 AND형 비휘발성 메모리 배열에서 바로 계산하는 인공 후각 시스템은 이 갈래와 가스 센서 갈래가 만나는 연구다.[^p2] 최근 논문 목록에는 수직 낸드 플래시로 어텐션 점수를 계산하는 행렬 곱셈 방식(Neurocomputing, 2025), 수직 AND형 플래시 메모리의 메모리 내 연산 분석(Nano Convergence, 2026), 대규모 아날로그 스파이킹 신경망 시뮬레이터 SNNSim(Advanced Intelligent Systems, 2024)도 있다.[^journal]

셋째 갈래는 **FET형 가스 센서와 센서 안의 계산**이다. Gas Sensor 페이지는 수평 플로팅 게이트(다른 전극과 전기적으로 이어지지 않은 게이트 전극)를 가진 MOSFET(금속-산화막-반도체 전계효과 트랜지스터)형 가스 센서를 첫 주제로 들고, 이 센서가 CMOS와 호환되고 여러 가스를 감지하며 이전 FET 가스 센서보다 감도가 높다고 적는다. 이어 CMOS 호환 기압 FET형 센서, 여러 온도에서의 FET형 센서 전류-전압 곡선과 마이크로 히터 전류-전압 곡선을 다루는 소자 모델링, 에너지 밴드 그림을 통한 가스 감지 특성 분석, 열 방출을 높이려고 비대칭 공기 틈을 둔 마이크로 히터 설계 최적화, 센서-증폭기 병합 배열과 메모리 내 연산을 이용한 새 가스 식별 방법을 든다.[^gas] 첫 화면은 Si MOSFET형 센서로 가스·습도·기압 센서를 소개한다.[^home] 대표 논문에서는 센서에 넣은 마이크로 히터로 이웃 센서들의 감지 물질을 칩 위에서 서로 다르게 열처리하고 차동 증폭 회로로 환원성 가스와 습도의 영향을 상쇄해 산화성 가스를 골라 감지했고,[^p1] 산화아연 막을 쓴 FET형 가스 센서와 비휘발성 메모리 배열을 묶은 인공 후각 시스템으로 닭고기가 상해 가는 과정을 추적했다.[^p2] IEDM 2025 채택 논문 가운데 하나는 FET형 가스 센서 두 개와 감산 회로를 한 칩에 통합해 교란 가스의 영향을 칩 안에서 상쇄하는 혼합 가스 판별 시스템으로, 계란이 상할 때 나오는 황화수소를 감지해 신선도 모니터링을 시연했다.[^iedm]

넷째 갈래는 **하프니아 강유전체 소자와 저주파 잡음**이다. 대표 논문에서는 생성 인공지능을 칩 위에서 돌리는 하드웨어로, CMOS·VLSI 공정과 호환되는 하프늄 산화물 강유전 터널 접합(FTJ, 얇은 강유전체 막을 사이에 둔 두 전극 사이의 터널 전류가 분극 방향에 따라 달라지는 소자) 배열 하나에서 무작위 잡음을 이용한 표본 추출과 여러 단계 전도도를 이용한 벡터-행렬 곱셈을 모두 해 이미지를 생성했고,[^p7] 프로그램·지우기 직후 반대 부호의 펄스를 걸어 약하게 분극된 영역을 없애는 분극 가지치기로 하프니아 강유전체 소자의 데이터 보존, 읽기 잡음, 문턱 전압 편차, 선형성을 개선했다.[^p8] IEDM 2025 채택 논문 가운데 하나는 HfO2-TiO2-HfO2 삼중 interlayer 구조를 넣은 HfZrO2 강유전 커패시터다.[^iedm] 학부 연구실 상세도 강유전체 기반 물질·소자와 시냅스 소자 연구를 든다.[^ecelabv] 최근 논문 목록에는 하프니아 강유전체에서 분극과 결함이 이끄는 스위칭을 저주파 잡음(낮은 주파수 대역에 나타나는 전류·전압의 요동)으로 재는 연구(Advanced Science, 2026), 환원성 금속 산화물의 저주파 잡음 분광을 메모리 내 연산으로 처리해 가스를 골라 감지하는 연구(Advanced Science, 2023), 「Low-frequency noise in CMOS-integrated gas sensors: From a reliability constraint to a selective sensing feature」(Sensors and Actuators B: Chemical, 2026)처럼 저주파 잡음을 강유전체 소자와 가스 센서 양쪽에서 다루는 논문이 있다.[^journal]

## 주요 연구 주제

### 1. 3차원 낸드 플래시 메모리의 동작·신뢰성과 낸드 기반 계산

수직 낸드 플래시의 동작·데이터 보존 개선과 트랩 분석, 전하 포획층 안 전자 이동의 물리 모델, 숨길 수 있는 낸드 PUF, 낸드 플래시 기반 신경망 연산(대표 논문 3, 4).[^nvm][^home][^p3][^p4][^journal]

### 2. 뉴로모픽 소자·회로와 메모리 내 연산

낸드·AND·NOR형 플래시 시냅스 소자, 뉴런 회로와 주변 회로, 플래시 게이트 사이리스터 뉴로모픽 모듈, 3차원 플래시 합성곱 블록(대표 논문 5, 6).[^neuro][^p5][^p6]

### 3. FET형 가스 센서와 센서 안의 계산

수평 플로팅 게이트 MOSFET형 가스 센서, 내장 마이크로 히터와 칩 위 열처리, 가스 센서와 메모리 배열을 묶은 인공 후각 시스템(대표 논문 1, 2).[^gas][^p1][^p2]

### 4. 하프니아 강유전체 메모리 소자와 저주파 잡음

하프늄 산화물 강유전 터널 접합으로 하는 이미지 생성, 분극 가지치기로 높인 강유전체 소자 신뢰성, 저주파 잡음 분석(대표 논문 7, 8).[^p7][^p8][^journal]

## 대표 논문

랩 Journal 페이지의 2021–2026년 논문 가운데 이종호 교수가 마지막 저자인 학술지 논문을 네 연구 갈래에 두 편씩 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^journal] |
|---|---|---|---|---|
| 1 | 2024 | [On-Chip Annealing Using Embedded Micro-Heater for Highly Sensitive and Selective Gas Detection](https://doi.org/10.1002/advs.202401821) · Advanced Science | 가스를 빠르고 정확하게 알아보는 가스 감지 시스템의 수요가 빠르게 늘고 있지만, 센서 배열을 만드는 공정이 복잡하고, 외부 처리 장치로 데이터를 보내는 데 시간이 걸리며, 여러 단계의 데이터 처리에 에너지가 많이 든다. 가스 센서 안에 넣은 마이크로 히터로 감지 물질을 칩 위에서 열처리(온칩 어닐링)하는, 빠르고 전력을 아끼는 가스 감지 시스템을 제안했다. 이 방법으로 같은 기판에 있는 이웃 센서들의 감지 물질을 공정을 더하지 않고 서로 다르게 만들 수 있다. 금속 산화물(MOX) 감지 물질은 결정 알갱이(그레인)가 작으면, 가스와 반응할 때 알갱이 안의 공핍 폭(전하 운반자가 빠져나간 영역의 폭)이 알갱이 크기보다 넓어지지 못해 산화성 가스에 대한 응답이 제한된다. 반면 공핍 폭을 줄이는 환원성 가스와 습도에 대한 응답은 알갱이 크기의 영향을 덜 받는다. 차동 증폭기와 FET형 가스 센서 두 개를 합친 읽기 회로는 환원성 가스와 습도에 대한 응답을 상쇄해 산화성 가스에 대한 응답을 두드러지게 한다. 이 선택적 온칩 어닐링 방법은 여러 금속 산화물 감지 물질에 쓸 수 있고, 단순하고 확장하기 쉬워 상용 분야에 응용할 가능성을 보였다.[^p1] | 1저자 J. Park, 마지막 저자 이종호 |
| 2 | 2023 | [Energy Efficient Artificial Olfactory System with Integrated Sensing and Computing Capabilities for Food Spoilage Detection](https://doi.org/10.1002/advs.202302506) · Advanced Science | 생물의 후각을 흉내 내는 인공 후각 시스템(AOS)에 관심이 크지만, 기존 시스템 대부분은 데이터 변환과 전송 때문에 에너지를 많이 쓰고 지연이 생긴다. 센서 가까이에서 계산하는 근접 센서 컴퓨팅을 바탕으로 에너지와 면적을 아끼는 인공 후각 시스템을 제안했다. FET형 가스 센서와 증폭 회로를 합친 감지 단위의 배열과 AND형 비휘발성 메모리 배열을 하나로 묶었다. 감지 단위의 신호가 메모리 배열에 바로 이어져 메모리 안에서 계산되고, 신호들의 의미 있는 선형 결합이 비트 라인 전류로 나온다. 얇은 산화아연 막을 가스 감지 물질로 써서 음식 부패를 감지하도록 설계했고, 단백질이 많은 음식의 부패 표지인 황화수소(H2S)와 암모니아(NH3)의 검출 한계가 0.01 ppm으로 낮았다. 개념 증명으로 닭 안심이 상해 가는 전 과정을 지켜보며 신선도 점수와 음식 상태를 계속 추적했다. 감지 온도를 바꿀 수 있고 메모리 셀을 프로그래밍할 수 있어 여러 응용에 쓸 수 있다.[^p2] | 1저자 G. Jung, 마지막 저자 이종호 |
| 3 | 2025 | [Concealable physical unclonable functions using vertical NAND flash memory](https://doi.org/10.1038/s41467-025-60415-y) · Nature Communications | 물리적 복제 방지 기능(PUF)은 강화된 하드웨어 보안 요구에 답할 수 있다. 수직 낸드(V-NAND) 플래시 메모리는 상용화된 비휘발성 메모리지만, 데이터를 안정적으로 저장하려고 셀 사이의 편차를 줄이도록 최적화되어 있어, 바로 그런 편차에 기대는 PUF로 쓰기 어렵다. 약한 GIDL(게이트 유도 드레인 누설) 지우기로 PUF 데이터를 만드는, 숨길 수 있는 V-NAND PUF를 제안했다. 제조 과정에서 생기는 낸드 스트링 사이의 도핑 깊이 차이가 GIDL 지우기 성능의 차이를 낳는다. 이렇게 만든 V-NAND PUF는 이상적인 보안 특성을 보였고, 읽기 횟수와 온도가 바뀌어도 100% 정확도를 유지했다. PUF 데이터 위에 다른 데이터를 덮어써서 숨기며, 숨기고 다시 드러내는 동작을 되풀이해도 그 특성이 완벽하게 유지되었다. 이 PUF는 쓰지 않을 때 공격을 막고, 메모리를 저장 장치로도 쓸 수 있게 한다.[^p3] | 1저자 S.-H. Park, 마지막 저자 이종호 |
| 4 | 2025 | [Nearly Temperature-Independent Gate-Electric-Field-Driven Lateral Migration of Electrons in Si3N4 Charge Trap Layer of Flash Memory Devices](https://doi.org/10.1103/lj4r-dcb7) · Physical Review Letters | 플래시 메모리 소자에 데이터를 쓰는(프로그램하는) 동안 전자가 질화규소(Si3N4) 전하 포획층 안에서 옆으로 옮겨 가는 이유를 실험과 새로 제안한 모델로 밝혔다. 제안한 열 보조 트랩-밴드 터널링 방출 모델(붙잡혀 있던 전자가 열의 도움을 받아 에너지 장벽을 뚫고 빠져나온다고 보는 모델)은 측정한 전기장과 온도가 전자의 옆 이동에 주는 영향을 잘 설명했다. 이 모델을 상용 소자 설계 시뮬레이션 도구(TCAD)에 사용자 인터페이스로 넣어 정확한 물리 분석을 할 수 있게 했다. 이 모델은 전자의 옆 이동을 이용하는 소자를 설계하거나, 수직 낸드 플래시 메모리의 space program, Z 간섭 같은 여러 현상을 분석하는 데 쓸 수 있다.[^p4] | 1저자 J. Hwang, 마지막 저자 이종호 |
| 5 | 2025 | [CMOS-compatible flash-gated thyristor–based neuromorphic module with small area and low energy consumption for in-memory computing](https://doi.org/10.1126/sciadv.adt8227) · Science Advances | 메모리 내 연산(IMC)은 아날로그 방식의 벡터-행렬 곱셈(VMM)을 효율적으로 하는 기술로, 처리 장치와 메모리를 나눈 기존 폰 노이만 구조의 성능 병목을 넘으려고 널리 연구되어 왔다. 아날로그 곱셈 말고도 더 많은 연산을 메모리 안에서 하려면 효율적인 뉴로모픽 모듈을 메모리와 결합해야 한다. 신경망의 양자화, 비선형 활성화, 최대 풀링 같은 여러 기능을 한 모듈에 담은, CMOS 공정과 호환되는 플래시 게이트 사이리스터 기반 뉴로모픽 모듈(FGTNM)을 제안했다. 이 모듈의 면적은 53제곱마이크로미터, 에너지 소비는 연산당 9.1펨토줄로 이전의 CMOS 기반 모듈보다 낫다. 이 모듈을 쓴 시스템 수준의 메모리 내 연산은 CIFAR-10 이미지 분류에서 89.97%의 정확도를 보였다. 플래시 메모리, 플래시 게이트 사이리스터, n형·p형 MOS 트랜지스터를 한 웨이퍼에 함께 집적할 가능성을 보여, 메모리 내 연산의 응용을 아날로그 곱셈 너머로 넓혔다.[^p5] | 1저자 J. Ko, 마지막 저자 이종호 |
| 6 | 2025 | [Hybrid functional 3D artificial synapses for convolution and reinforcement learning](https://doi.org/10.1126/sciadv.adw7498) · Science Advances | 메모리 내 연산(CIM) 기술은 컴퓨팅 방식의 유망한 전환으로 큰 관심을 받고 있다. 2차원 크로스바 배열을 쓰는 기존 CIM 시스템은 완전 연결 신경망에서는 면적과 에너지 효율이 뛰어나지만, 합성곱 신경망에서는 효율이 떨어진다. 수직으로 쌓은 3차원 플래시 메모리의 독특한 구성을 활용해 합성곱 연산과 강화학습을 할 수 있는 구조를 제안했다. 제안한 3차원 합성곱 블록(3D CB)은 면적 부담을 크게 줄이고 합성곱 연산의 신뢰성과 에너지 효율을 높인다. 3D CB와 3차원 완전 연결 블록(3D FCB)은 구조를 조금만 바꿔 서로 다른 기능을 하며, 둘이 호환되어 한 웨이퍼에 함께 집적할 수 있다. 이렇게 완전히 집적한 시스템은 면적·에너지 효율이 높으면서 자율주행 경로 계획을 정확하고 일관되게 해냈다.[^p6] | 1저자 J. Im, 마지막 저자 이종호 |
| 7 | 2026 | [CMOS-compatible ferroelectric tunnel junctions integrate stochastic sampling and deterministic computing for image generation](https://doi.org/10.1038/s41467-026-72969-6) · Nature Communications | 생성 모델이 발전하면서 작고 에너지 효율적인 하드웨어가 더 필요해졌지만, 이미지 생성을 하드웨어에서 바로 하려면 잠재 공간에서 무작위로 표본을 뽑는 일과 정해진 대로 복원(디코딩)하는 일이라는 서로 맞서는 요구를 함께 채워야 한다. 하프늄 산화물 강유전 터널 접합(FTJ) 배열 하나가 두 기능을 모두 하는 통합 하드웨어 틀을 보였다. CMOS·VLSI 공정과 호환되는 하프니아 강유전체 제조를 이용해, random telegraph noise(소자 전류가 정해진 값들 사이를 무작위로 오가는 잡음)를 만들어 조절 가능한 무작위 표본 추출에 쓰는 모드와, 여러 단계의 비휘발성 전도도 상태로 정밀한 벡터-행렬 곱셈을 하는 모드를 함께 구현했다. 전압과 표본 추출 시간을 조절해 무작위성과 신뢰성을 세밀하게 조정했고, 손글씨 숫자 합성(MNIST)과 고해상도 얼굴 이미지 생성(CelebA)에서 높은 품질의 이미지를 만들었다. 회로 수준 시연에서 10만 회가 넘는 사이클 동안 안정적으로 동작해 이전 하드웨어 기반 방법보다 나았고, 규모를 키울 수 있는 칩 위 생성 인공지능 가속기로 가는 길을 보였다.[^p7] | 1저자 R.-H. Koo, 마지막 저자 이종호 |
| 8 | 2024 | [Polarization Pruning: Reliability Enhancement of Hafnia-Based Ferroelectric Devices for Memory and Neuromorphic Computing](https://doi.org/10.1002/advs.202407729) · Advanced Science | 강유전체 물질은 비휘발성이고 상태를 빠르게 바꿀 수 있으며 에너지를 적게 써서 전자 소자 발전의 열쇠가 되고, 강유전체 소자는 논리 회로, 메모리 저장 장치, 센서, 메모리 내 연산에 쓰인다. 그러나 강유전체 메모리를 실제로 쓰는 데 주된 과제는 신뢰성이다. 이를 풀려고 프로그램이나 지우기 동작 바로 뒤에 반대 부호의 펄스를 걸어 약하게 분극된 영역(도메인)을 없애는 분극 가지치기(PP) 방법을 제안했다. 약하게 분극된 도메인 때문에 생기는 탈분극을 줄이고 강유전 쌍극자의 요동을 누그러뜨려 강유전체 소자의 신뢰성을 크게 높였다. 데이터 보존이 25% 나아지고, 읽기 잡음이 50% 줄고, 문턱 전압 편차가 45% 줄고, 선형성이 72% 나아졌다. 이 방법은 메모리 저장 효율과 뉴로모픽 시스템의 성능을 크게 높인다.[^p8] | 1저자 R.-H. Koo, 마지막 저자 이종호 |

## 교수와 전문 분야

이종호 교수는 경북대학교에서 학사(1987)를, 서울대학교에서 석사(1989)와 박사(1993)를 받았고 세 학위 모두 전자공학이다.[^intro][^eceprof] 1993년 서울대 ISRC에서 엔지니어로 BiCMOS 공정 개발을 맡았고, 1994년 원광대학교 전기공학부, 2002년 경북대학교 전자전기컴퓨터공학부 교수를 거쳐 2009년 9월부터 서울대학교 전기·정보공학부 교수다.[^intro][^eceprof] 1994–1998년에는 ETRI의 초빙 연구원(invited member of technical staff)으로 deep submicron MOS 소자와 소자 격리를, 1998년 8월–1999년 7월에는 MIT 박사후연구원으로 100 nm 미만 이중 게이트 CMOS 소자를 연구했다.[^intro] 교수 개인 페이지의 이력은 2022–2024년을 Minister of Science and ICT(과학기술정보통신부 장관)로, 2024년부터를 서울대 전기·정보공학부 교수로 적고,[^profcv] 2024–2026년 소식 글들은 교수를 「전 과학기술정보통신부 장관」으로 소개한다.[^news]

교수 소개에 따르면 교수는 Institute of Electronics Engineers of Korea(IEEK) 평생회원이자 IEEE Fellow이고, IEDM 분과위원, ITRS ERD 위원, IPFA2011 general chair, IEEE EDS Korea chapter chair를 지냈다. 교수는 bulk FinFET, DRAM 셀 트랜지스터용 Saddle FinFET(bCAT), 가상 소스/드레인을 쓰는 낸드 플래시 셀 스트링을 발명했고, 교수 소개는 이 세 발명이 산업계 양산에 적용되어 온 핵심 기술이라고 적는다.[^intro] 개인 페이지의 수상 목록은 1994–2018년의 21건이다. 2006년 This Month’s Scientist Award(Ministry of Science of Korea), 2007년 Doyeon Creative Research Award(ISRC), 2011년 Men of National Merit in Semiconductor Technology Development(Prime minister of Korea), 2012년 Samsung Humantech Award, 2013년 한국공학한림원(NAEK)의 미래 기술 선정, 2014년 SK hynix cooperative patent Award, 2015년 Okawa Prize와 19th Young Engineer Award(NAEK), 녹조근정훈장(National Medal), 2016년 IEEE Fellow Member와 SK hynix Industry-University Research Award, 2018년 Kyung-Am Award(공학 부문)가 들어 있다.[^profcv] 2025년 11월에는 경암상위원회 위원장으로 제21회 경암상 시상식에 참석했다.[^news]

학부 교수 상세는 교수의 전공을 반도체 소자, 분야를 반도체 재료 및 소자로 적는다.[^eceprof] 논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 3차원 낸드 플래시 메모리의 전하 포획 물리와 동작, 그리고 낸드를 보안에 쓰는 방법이다(대표 논문 3, 4).[^p3][^p4] 둘째, 플래시 기반 시냅스 소자와 뉴로모픽 모듈로 메모리 내 연산 하드웨어를 만드는 일이다(대표 논문 5, 6).[^p5][^p6] 셋째, CMOS와 함께 만드는 FET형 가스 센서와 센서 신호를 메모리에서 바로 계산하는 시스템이다(대표 논문 1, 2).[^p1][^p2] 넷째, 하프니아 강유전체 소자의 신뢰성과 그 소자로 하는 생성 인공지능 연산이다(대표 논문 7, 8).[^p7][^p8] 2024–2026년 교수의 기조·초청 강연 제목은 저전력 AI 반도체, AI 반도체 정책, 플래시 메모리 기반 신경망을 다룬다.[^conf][^news]

## 응용 분야

대표 논문은 음식 부패 감지(닭고기 신선도 추적),[^p2] 쓰지 않을 때 공격을 막으면서 메모리를 저장 장치로도 쓰는 하드웨어 보안,[^p3] 자율주행 경로 계획,[^p6] 규모를 키울 수 있는 칩 위 생성 인공지능 가속기[^p7]를 응용 대상으로 들고, 칩 위 열처리 가스 감지 방법은 단순하고 확장하기 쉬워 상용 분야에 쓸 가능성이 있다고 적는다.[^p1] 분극 가지치기는 메모리 저장 효율과 뉴로모픽 시스템의 성능을 높인다.[^p8] IEDM 2025 소식은 세 논문의 응용으로 초저전력·뉴로모픽 하드웨어, 차세대 하드웨어 보안, 계란 부패 때 나오는 황화수소를 감지하는 실시간 신선도 모니터링을 든다.[^iedm] 학부 연구실 상세는 주요 연구과제로 「대형 언어 모델 (LLM)을 위한 3차원 낸드 플래시 기반 트랜스포머 구현」(SK하이닉스)을 적고,[^ecelabv] 교수 소개는 교수의 bulk FinFET, Saddle FinFET, 낸드 플래시 셀 스트링 발명이 산업계 양산에 적용되어 왔다고 적는다.[^intro] 졸업생 개인 페이지의 경력 줄에는 Samsung Electronics, SK Hynix, Samsung Display, LG Display, TmaxSoft와 University of California, Santa Barbara, Georgia Institute of Technology, Shenyang University of Technology의 박사후 과정이 있다.[^members]

## 구성원

2026년 10월 25일 열람한 Members 페이지(교수를 포함한 76명, 8쪽) 기준이다. Post Doc. 칸 5명, Ph.D. Candidates 칸 8명, M.S. Candidates 칸 8명이며, 과정은 칸 이름을 옮긴 것이다. 괄호 안은 개인 페이지 Academic Experiences의 현재 과정 줄 표기와 카드의 「연구실 대표」 표기다. 시작은 그 과정 줄(박사후연구원은 박사후연구원 줄)의 시작 연도나 연월이고, 연구 주제는 개인 페이지에 Research Topics 칸을 둔 1명의 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 심성근(Sung Keun Shim) | 박사후연구원 | 2025.09 |  |  |
| 박성호(Sungho Park) | 박사후연구원 | 2026 |  | 3, 5, 7, 8 |
| 구륜한(Ryun-Han Koo) | 박사후연구원 | 2025.08 | CMOS-based neuromorphic systems, Ferroelectric memory devices, Low-frequency noise in semiconductor devices | 3, 5, 6, 7, 8 |
| 임지성(Jiseong Im) | 박사후연구원 | 2025 |  | 3, 5, 6, 7, 8 |
| 황준(Joon Hwang) | 박사후연구원 | 2025 |  | 1, 4, 7 |
| 정진혁(Jinhyeok Jung) | 박사과정 (PhD Degree Course) | 2025 |  |  |
| 지종호(Jongho Ji) | 박사과정 (PhD Degree Course) | 2025 |  |  |
| 신훈희(Hunhee Shin) | 박사과정 (MS&PhD Degree Course) | 2022 |  | 1, 2 |
| 이인석(InSeok Lee) | 박사과정 (MS&PhD Degree Course) | 2022 |  |  |
| 고종현(Jonghyun Ko) | 박사과정 (MS&PhD Degree Course) | 2022 |  | 3, 5, 6, 7, 8 |
| 최강욱(Kangwook Choi) | 박사과정 (연구실 대표, MS&PhD Degree Course) | 2021 |  |  |
| 김승환(Seungwhan Kim) | 박사과정 (MS&PhD Degree Course) | 2021 |  |  |
| 김정현(Jeonghyun Kim) | 박사과정 (MS&PhD Degree Course) | 2021 |  | 6 |
| 김우재(Woojae Kim) | 석사과정 (MS&PhD Degree Course) | 2026 |  |  |
| 조성빈(Sungbin Jo) | 석사과정 (MS&PhD Degree Course) | 2026 |  |  |
| 조성윤(Sungyun Cho) | 석사과정 (MS&PhD Degree Course) | 2026 |  |  |
| 장건(Geon Jang) | 석사과정 (MS&PhD Degree Course) | 2026 |  |  |
| 임상현(Sanghyun Leem) | 석사과정 (MS&PhD Degree Course) | 2026 |  |  |
| 이태호(Taeho Lee) | 석사과정 (MS&PhD Degree Course) | 2025 |  |  |
| 오민균(Mingyun Oh) | 석사과정 (MS&PhD Degree Course) | 2025 |  |  |
| 박수영(Suyoung Park) | 석사과정 (MS&PhD Degree Course) | 2025 |  |  |

## 졸업생과 이전 구성원

Members 페이지 ALUMNI(Alumni) 칸의 54명이다. 학위·과정 칸은 개인 페이지 Academic Experiences의 서울대 학위 줄과 학위 과정 줄(학사 줄 제외)을, 진로 칸은 그 과정이 시작된 뒤의 경력 줄과 끝나는 해가 적히지 않은 경력 줄을 누리집 표기 그대로 적은 것이다. 학위 과정 줄에 학교 이름이 없는 경우도 누리집 표기대로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 권동석(Dongseok Kwon) | 2017~2023 MS & PhD Degree Course | 2023~ University of California, Santa Barbara, Postdoc. |
| 이차영(Chayoung Lee) | 2020~2024 PhD Degree Course | 2010~ SKHynix |
| 백종원(Jong-Won Back) | 2018~2024 MS & PhD Degree Course |  |
| 오성빈(Seongbin Oh) | 2017~2023 MS & PhD Degree Course |  |
| 정규원(Gyuweon Jung) | 2018~2023 MS & PhD Degree Course | 2023~2024 Post Doc. |
| 유호남(Honam Yoo) | 2004~2008 Seoul National University, MS; 2019~2023 PhD Degree Course | 2009~ SkHynix |
| 정유정(Yujeong Jeong) | 2017~2019 Seoul National University, MS; 2019~ 2023 Ph. D Degree Course |  |
| 홍성빈(Seongbin Hong) | 2016~2018 Master Degree Course; 2018~2022 Ph. D. Degree Course |  |
| 이수창(Soochang Lee) | 2016~2018 Master Degree Course; 2018~2022 Ph. D. Degree Course |  |
| 이정규(Jung-Kyu Lee) | 2010~2012 Seoul National University, MS; 2012 ~ 2017 Ph. D Degree Course; 2018 ~ 2022 Ph. D Degree Course |  |
| 유건(Keon Yoo) | 2013~2015 Seoul National University, MS; 2015~2020 Ph. D Degree Cours | 2005~ SK Hynix Inc. |
| 서영탁(Youngtak Seo) | 2016~2018 Seoul National University, MS; 2018~2021 Seoul National University, Ph.D |  |
| 강원묵(Won-Mook Kang) | 2015~2017 Seoul National University, MS; 2017~ 2021 Seoul National University, Ph.D |  |
| 이성태(Sung-Tae Lee) | 2016~2018 Seoul National University, MS; 2018~2021 Seoul National University, Ph.D | 2021~ Georgia Institute of Technology, POST Ph.D |
| 우성윤(Sung Yun Woo) | 2014~2016 Master Degree Course; 2016~2021 Ph. D Degree Course |  |
| 장동규(Dongkyu Jang) | 2016~2020 Ph. D Degree Course | 2010~ Samsung Electronics Co.,Ltd |
| 최낙용(Nagyong Choi) | 2014~2016 Master Degree Course; 2016~2020 Ph. D Degree Course | 2020~ SK Hynix Inc. |
| 노유현(Yoohyun Noh) | 2017~2019 Seoul National University, MS | 2019~ SK Hynix Inc. |
| 서재화(Jae Hwa Seo) | 2018~2019 Seoul National University, Post Ph.D | 2019~ Samsung Electronics, Co., Ltd. |
| 임수환(Suhwan Lim) | 2015~2019 Seoul National University, Ph.D | 2019~ Samsung Electronics, Co., Ltd. |
| 홍윤기(Yoonki Hong) | 2013~2015 Seoul National University, MS; 2015~2019 Seoul National University, Ph. D | 2019~ Samsung Electronics, Co., Ltd. |
| 배종호(Jong-Ho Bae) | 2011~2013 Seoul National University, MS; 2013~2018 Seoul National University, Ph.D | 2018~ Postdoctoral Researcher / Assistant Researcher |
| 김철흥(Chul-Heung Kim) | 2013~2015 Seoul National University, MS; 2015~2019 Seoul National University, Ph. D | 2019~ Samsung Electronics, Co., Ltd. |
| Meile Wu | 2015~2019 Seoul National University, Ph. D | 2019~ Shenyang University of Technology, Postdoc |
| 최규봉(Kyu Bong Choi) | 2012~2014 Seoul National University, MS; 2014~2018 Seoul National University, Ph. D | 2018~ Samsung Electronics, Co., Ltd. |
| 강호중(Ho Jung Kang) | 2012~2014 Seoul National University, MS; 2014~2018 Seoul National University, Ph. D | 2018~ SK Hynix Inc |
| 엄재호(Jai-Ho Eum) | 2015~2018 Seoul National University, MS | 2018~ TmaxSoft |
| 신종민(Jongmin Shin) | 2012~2014 Seoul National University, MS; 2014~2018 Seoul National University, Ph. D | 2018~ Samsung Electronics, Co., Ltd. |
| 김재성(Jae Sung Kim) | 2014~2018 Seoul National University, MS/Ph.D course (completion) |  |
| Shuang Zhao | 2015~2017 Seoul National University, MS |  |
| 김종인 | 2004~2006 Seoul National University, MS; 2013~2017 Seoul National University, Ph.D | 2006~2012 Samsung Electronics, Co., Ltd.; 2012~ Samsung Display, Co., Ltd. |
| 박준모(Jun-Mo Park) | 2010~2012 Seoul National University, MS; 2012~2016 Seoul National University, PhD | 2016~ Samsung Electronics, Co., Ltd. |
| 이명선(Myoung-Sun Lee) | 2009~2011 Seoul National University, MS; 2011~2016 Seoul National University, PhD | 2016~ Samsung Electronics, Co., Ltd. |
| 조인탁(In Tak Cho) | 2011~2016 Seoul National University, PhD | 2016~ LG Display Co., Ltd. |
| 김창희(Chang-Hee Kim) | 2010~2012 Seoul National University, MS; 2012~2015 Seoul National University, PhD | 2015~ Samsung Electronics, Co., Ltd. |
| 김경도(Kyung Do Kim) | 1998~2000 Seoul National University, MS; 2011~2015 Seoul National University, PhD | 2000~ Hynix Semiconductor Inc.; 2015~ SK Hynix Inc |
| 조성민(Sung-Min Joe) | 2010~2015 Seoul National University, PhD | 2015~ Samsung Electronics, Co., Ltd |
| 최병인(Byeong-In Choe) | 2012~2014 Seoul National University, MS | 2004~ Samsung Electronics, Co., Ltd.; 2014~ Samsung Electronics, Co., Ltd. |
| 이주완(Ju-Wan Lee) | 2009~2014 Seoul National University, PhD | 2014~ Samsung Electronics, Co., Ltd. |
| 정민규(Min-Kyu Jeong) | 2009~2014 Seoul National University, PhD | 2014~ SK Hynix Inc |
| 남동우(Dong-Woo Nam) | 2011~2013 Seoul National University, MS |  |
| 조봉수(Bong-Su Jo) | 2011~2013 Seoul National University, MS | 2013~ SK Hynix Inc |
| 김남훈(Nam-Hoon Kim) | 2010~2012 Seoul National University, MS | 2012~ SK Hynix Inc |
| 신원준(Wonjun Shin) | 2018~2023 MS&PhD Degree Course | 2023~ Seoul National University, Post. Doc |
| 박민규(Min Kyu Park) | 2019~2024 MS&PhD Degree Course | 2024~ Post Doc. |
| 김장생(Jangsaeng Kim) | 2018~ 2024 MS&PhD Degree Course | 2024~ Post.Doc |
| 조준형(Joonhyung Cho) | 2022~2026 Ph.D Degree Course | 2015~ SK Hynix |
| 유상우(Sang-Woo Ryu) | 2022~2026 PhD Degree course | 2017~ SK hynix |
| 이경민(Kyung Min Lee) | 2022~2026 PhD Degree Course | 2015~ Samsung electronics |
| 김재현(Jaehyeon Kim) | 2020~2025 MS&PhD Degree Course | 2025~2026 Post-doctoral Researcher; 2026~ Samsung electronics |
| 김동희(Donghee Kim) | 2020~2026 MS&PhD Degree Course | 2026~ Samsung electronics |
| 이규호(Kyuho Lee) | 2020~2026 MS&PhD Degree Course |  |
| 염규호(Gyuho Yeom) | 2019~ MS&PhD Degree Course |  |
| 박진우(Jinwoo Park) | 2019~ 2025 MS&PhD Degree Course |  |

## 최근 학술지 논문 (2021–2026)

랩 Journal 페이지(쪽당 20편, 27쪽, 연도 내림차순)의 2021–2026년 항목 169편이다(2026년 22, 2025년 16, 2024년 36, 2023년 32, 2022년 18, 2021년 45). 누리집은 저자를 1저자 이름과 et al.로만 적고, 제목·학술지 이름·연도는 누리집 표기 그대로다. 같은 해 안에서는 누리집 순서다.[^journal]

**2026**

- Chayoung Lee et al. "Low-frequency noise in CMOS-integrated gas sensors: From a reliability constraint to a selective sensing feature". *Sensors and Actuators B: Chemical*.
- Jonghyun Ko et al. "Charge Trap Flash-Gated Inverter-Based In-Memory Analog-to-Digital Converter for Compute-in-Memory". *IEEE Electron Device Letters*.
- Joon Hwang et al. "Gate insulator stack engineering for fully CMOS-compatible reservoir computing". *Nano Convergence*.
- Chayoung Lee et al. "Low-frequency noise in CMOS-integrated gas sensors: From a reliability constraint to a selective sensing feature". *Sensors and Actuators: B. Chemical*.
- Hunhee Shin et al. "Design optimization of embedded micro-heater for reliable gas sensing and on-chip annealing". *Sensors and Actuators: B. Chemical*.
- Jonghyun Ko et al. "Low-power NO2 Gas Alarm Platform Using In-memory Latched Comparator". *Sensors and Actuators B: Chemical*.
- Jonghyun Ko et al. "Activation-Integrated and Memory-Assisted Dynamic-Latch Quantizer for Variation-Tolerant and Low-Energy Neuromorphic Computing". *Advanced Intelligent Science*.
- Joon Hwang et al. "Direct observation of lateral hole migration in the charge trap layer of an inhomogeneous flash memory device". *Applied Physics Reviews*.
- Sung-Ho Park et al. "Model-Inversion-Resistant Physical Unclonable Neural Network Using Vertical NAND Flash Memory". *Advanced Science*.
- Jong-Won Back et al. "A back-pattern-dependency-free synaptic string architecture using vertical NAND flash memory". *Nano Energy*.
- Sung-Ho Park et al. "Retention improvement in vertical NAND flash memory using block soft erase scheme". *Applied Physics Letters*.
- Jonghyun Ko et al. "2T-Embedded Flash Memory using Standard 28nm Logic CMOS Technology". *IEEE Electron Device Letters*.
- Jonghyun Ko et al. "Analysis of Vertical AND Flash Memory for Energy-Efficient, Scalable, and Fast CIM Beyond Vertical NAND Flash Memory". *Nano Convergence*.
- Jonghyun Ko et al. "SenroSim: System-level Simulator for Accuracy, Area, Latency, and Energy Consumption of Gas-sensing-based In-sensor Neuromorphic Computing". *IEEE Sensors Journal*.
- Joon Hwang et al. "Flash synaptic arrays with improved endurance-retention trade-off and backpropagation capability for efficient on-chip training". *Nano Energy*.
- Ryun Han Koo et al. "CMOS-compatible ferroelectric tunnel junctions integrate stochastic sampling and deterministic computing for image generation". *nature communications*.
- Ryun Han Koo et al. "Noise Fingerprints as a Quantitative Order Parameter for Polarization- and Defect-Mediated Switching in Hafnia Ferroelectrics". *Advanced Science*.
- Sung Ho Park et al. "Triple-Level Content-Addressable Vertical NAND Flash Memory". *Advanced Science*.
- Sung Ho Park et al. "Ising Solver Using Vertical NAND Flash Memory". *Advanced Intelligence System*.
- Sung Ho Park et al. "Hardware-Bound Binary Neural Network Using Concealable Magnetic Tunnel Junctions". *IEEE Electron Device Letters*.
- Sungho Park et al. "Hybrid approximate-accurate neural network using vertical NAND flash memory". *Nano Energy*.
- Sungho Park et al. "Vertical NAND Flash Memory-Based Bayesian Neural Networks With Intrinsic Gaussian Weight Sampling". *Advanced Intelligent Systems*.

**2025**

- Jonghyun Ko et al. "Vertical NAND flash memory-based matrix-matrix multiplication scheme for energy-efficient attention score computation". *Neurocomputing*.
- Hunhee Shin et al. "Optimization of co-sputtered zinc indium tin oxide-based MOSFET-type sensor for effective NO2 gas detection". *Sensors and Actuators B: Chemical*.
- Kangwook Choi et al. "Novel Gas Sensor Signal Acquisition Method: Amplifying Sensor Signals and Enabling Efficient Gas Identification". *Advanced science*.
- Sung-Ho Park et al. "Concealable physical unclonable functions using vertical NAND flash memory". *Nature communications*.
- Jonghyun Ko et al. "CMOS-compatible flash-gated thyristor–based neuromorphic module with small area and low energy consumption for in-memory computing". *Science Advances*.
- Ryun-Han Koo et al. "A universal re-annealing method for enhancing endurance in hafnia ferroelectric memories: Insights from stochastic noise analysis". *Chaos, Solitons & Fractals*.
- Ryun-Han Koo et al. "Interface percolation and random trap generation in ferroelectric memory: A two-step degradation mechanism explored through low-frequency noise spectroscopy". *Chaos, Solitons & Fractals*.
- Sangwoo Ryu et al. "Comparative analysis of ferroelectric domain wall motion under cycling stress of HfZrO2 fabricated by thermal and plasma-enhanced atomic layer depositions". *The Journal of Chemical Physics*.
- Ryun-Han Koo et al. "Stochastic behavior of random telegraph noise in ferroelectric devices: Impact of downscaling and mitigation strategies for neuromorphic applications". *Chaos, Solitons & Fractals*.
- Jonghyun Ko et al. "NeuroTorch: DRAM-free nonvolatile memory-based hybrid training compute-in-memory system simulator". *Neurocomputing*.
- Ryun-Han Koo et al. "Physical correlation between stochasticity and process-induced damage in ferroelectric memory devices". *Nano Convergence*.
- Sung-Ho Park et al. "Dynamic pass bias control for temperature-resilient neural networks using vertical NAND flash memory". *Nano Convergence*.
- Ryun-Han Koo et al. "From commercial to emerging memory: Device and circuit perspectives for neuromorphic computing". *Device*.
- Joon Hwang et al. "Nearly Temperature-Independent Gate-Electric-Field-Driven Lateral Migration of Electrons in Si3⁢N4 Charge Trap Layer of Flash Memory Devices". *Physical Review Letters*.
- Jiseong Im et al. "Hybrid functional 3D artificial synapses for convolution and reinforcement learning". *Science Advances*.
- Ryun-Han Koo et al. "Low-Frequency Noise Spectroscopy for Navigating Geometrically Varying Strain Effects in HfO2 Ferroelectric FETs". *Advanced Science*.

**2024**

- Min-Kyu Park et al. "Lateral Migration-based Flash-like Synaptic Device for Hybrid Off-chip/On-chip Training". *Advanced Electronic Materials*.
- Wonjun Shin et al. "Proposition of optimal self-curing method in horizontal-floating gate FET-type gas sensors for reliability improvement". *Sensors and Actuators B: Chemical*.
- Yoonki Hong et al. "Improved Performance of FET-Type Humidity Sensor With Low-Power Embedded Micro-Heater". *IEEE Electron Device Letters*.
- Jiseong Im et al. "Vertical AND-type Flash TFT Array Capable of Accurate Vector-Matrix Multiplication Operations for Hardware Neural Networks". *IEEE Electron Device Letters*.
- Sung-Ho Park et al. "On-Chip Learning in Vertical NAND Flash Memory Using Forward–Forward Algorithm". *IEEE Transactions on Electron Devices*.
- Ryun-Han Koo et al. "Stochasticity in ferroelectric memory devices with different bottom electrode crystallinity". *Chaos, Solitons & Fractals*.
- Sung-Ho Park et al. "Reliability Improvement in Vertical NAND Flash Cells Using Adaptive Incremental Step Pulse Programming (A-ISPP) and Incremental Step Pulse Erasing (ISPE)". *IEEE Transactions on Electron Devices*.
- Kangwook Choi et al. "NO2 gas response improvement method by adopting oxygen vacancy controlled In2O3 double sensing layers". *Solid-State Electronics*.
- Jinwoo Park et al. "On-Chip Annealing Using Embedded Micro-Heater for Highly Sensitive and Selective Gas Detection". *Advanced Science*.
- Jangsaeng Kim et al. "Demonstration of In-Memory Biosignal Analysis: Novel High-Density and Low-Power 3D Flash Memory Array for Arrhythmia Detection". *Advanced Science*.
- Ryun-Han Koo. "Examination of Ferroelectric Domain Dynamics in HZO Under Endurance Cycling Stress". *IEEE Electron Device Letters*.
- Jangsaeng Kim et al. "Vertical AND-Type Flash Synaptic Cell Stack for High-Density and Reliable Binary Neural Networks". *IEEE Electron Device Letters*.
- Jangsaeng Kim et al. "Toward Optimized In-Memory Reinforcement Learning: Leveraging 1/f Noise of Synaptic Ferroelectric Field-Effect-Transistors for Efficient Exploration". *Advanced Intelligent Systems*.
- Joon Hwang et al. "NOR-Type Flash Array Based on Four-Terminal TFT Synaptic Devices Capable of Selective Program/Erase Exploiting Fowler-Nordheim Tunneling". *EEE Electron Device Letters*.
- Wonjun Shin et al. "Robust 1/f Noise Unaffected by Program/Erase Cycling-Induced Damage in Ferroelectric Schottky Barrier FETs". *IEEE Electron Device Letters*.
- Jangsaeng Kim et al. "Vertical AND-Type Flash Synaptic Cell Stack for High-Density and Reliable Binary Neural Networks". *IEEE Electron Device Letters*.
- Jiseong Im et al. "Vertical AND-Type Flash TFT Array Capable of Accurate Vector-Matrix Multiplication Operations for Hardware Neural Networks". *IEEE Electron Device Letters*.
- Gyuweon Jung et al. "Chemisorption Manipulation by Adjusting the Carrier Concentration of the Adsorbent and Its Application to Adsorbate Identification". *ACS Materials Letters*.
- Jinwoo Park et al. "Reliability of FET-type gas sensor with asymmetric air-gap micro-heater structure considering thermoelectric effect". *Sensors and Actuators B: Chemical*.
- Chayoung Lee et al. "CMOS-Compatible Barometric Pressure Field-Effect Transistor-Type Sensor". *IEEE Electron Device Letters*.
- Jonghyun Ko et al. "SNNSim: Investigation and Optimization of Large-Scale Analog Spiking Neural Networks Based on Flash Memory Devices". *Advanced Intelligent Systems*.
- Meile Wu et al. "Hydrogen Sensing Properties of FET-Type Sensors with Pt-In2O3 at Room Temperature". *Chemosensors*.
- Kyu-Ho Lee et al. "Si-Based Dual-Gate Field-Effect Transistor Array for Low-Power On-Chip Trainable Hardware Neural Networks". *Advanced Intelligent Systems*.
- Jangsaeng Kim et al. "Performance Optimization in 3D Flash Memory Cell Stack via Process Variable Engineering". *IEEE Electron Device Letters*.
- Min-Kyu Park et al. "Analysis Method of Dynamic Read Variation in a TFT-Type Synaptic Devices With Poly-Si Channel Structure". *IEEE Transactions on Electron Devices*.
- Jangsaeng Kim et al. "Thermal Instability Compensation of Synaptic 3D Flash Memory-Based Hardware Neural Networks With Adaptive Read Bias". *IEEE Electron Device Letters*.
- Min-Kyu Park et al. "Highly Reliable Lateral Migration-Based TFT-Type Neuron Device for Spiking Neural Networks". *IEEE Electron Device Letters*.
- Jangsaeng Kim et al. "All-Ferroelectric Spiking Neural Networks via Morphotropic Phase Boundary Neurons". *Advanced Science*.
- Ryun-Han Koo et al. "Polarization Pruning: Reliability Enhancement of Hafnia-Based Ferroelectric Devices for Memory and Neuromorphic Computing". *Advanced Science*.
- Min-Kyu Park et al. "Analysis of Leaky Integrate-and-Fire Neuron Using Al2O3/Si3N4 Gate Insulator Stack for Spiking Neural Network". *ACS Applied Electronic Materials*.
- Ryun-Han Koo et al. "Strain–Stress Impact on Ferroelectric Devices: A Multilayer Analysis and Optimization Strategy for Neural Networks". *ACS Materials Letters*.
- Sang Woo Kim et al. "A New Back-End-Of-Line Ferroelectric Field-Effect Transistor Platform via Laser Processing". *Small*.
- Sung-Ho Park et al. "Optimization of Programming Pulse Shape for Vertical NAND Flash Memory Using Neural Networks". *IEEE Electron Device Letters*.
- Min-Kyu Park et al. "Charge-trap synaptic device with polycrystalline silicon channel for low power in-memory computing". *Scientific Reports*.
- Jiseong Im et al. "Multifunctional In-Memory Analog-to-Digital Converter for Next-Gen Compute-in-Memory Systems". *Advanced Intelligent Systems*.
- Sung-Ho Park et al. "Retention Improvement in Vertical NAND Flash Memory Using Electron Back-Tunneling". *IEEE Electron Device Letters*.

**2023**

- In-Seok Lee et al. "Power and Area-Efficient XNOR-AND Hybrid Binary Neural Networks Using TFT-Type Synaptic Device". *IEEE Electron Device Letters*.
- Wonjun Shin et al. "Unveiling Resistance Switching Mechanisms in Undoped HfOx Ferroelectric Tunnel Junction Using Low-Frequency Noise Spectroscopy". *IEEE Electron Device Letters*.
- Ryun-Han Koo et al. "Effect of Carrier Transport Process on Tunneling Electroresistance in Ferroelectric Tunnel Junction". *IEEE Electron Device Letters*.
- Sung Yun Woo et al. "Demonstration of Pulse Width Modulation Function Using Single Positive Feedback Device for Neuron". *IEEE Electron Device Letters*.
- Min-Kyu Park et al. "Cointegration of the TFT-Type AND Flash Synaptic Array and CMOS Circuits for a Hardware-Based Neural Network". *IEEE Transactions on Electron Devices*.
- Kyu-Ho Lee et al. "Si-Based Dual-Gate Field-Effect Transistor Array for Low-Power On-Chip Trainable Hardware Neural Networks". *Advanced Intelligent Systems*.
- Dongseok Kwon et al. "Efficient Hybrid Training Method for Neuromorphic Hardware Using Analog Nonvolatile Memory". *IEEE Transactions on Neural Networks and Learning Systems*.
- Dongseok Kwon et al. "Analog Synaptic Devices Based on IGZO Thin-Film Transistors with a Metal–Ferroelectric–Metal–Insulator–Semiconductor Structure for High-Performance Neuromorphic Systems". *Advanced Intelligent Systems*.
- Ryun-Han Koo et al. "Comparative Analysis of n- and p-Type Ferroelectric Tunnel Junctions Through Understanding of Non-FE Resistance Switching". *IEEE Electron Device Letters*.
- Gyuweon Jung et al. "Reconfigurable Manipulation of Oxygen Content on Metal Oxide Surfaces and Applications to Gas Sensing". *ACS Nano*.
- Dongseok Kwon et al. "Reconfigurable neuromorphic computing block through integration of flash synapse arrays and super-steep neurons". *Science Advances*.
- Wonjun Shin et al. "Unraveling Threshold Voltage Instability in Ferroelectric Junctionless FETs Using Low-Frequency Noise Measurement With Base Bias". *IEEE Electron Device Letters*.
- Gyuweon Jung et al. "Energy Efficient Artificial Olfactory System with Integrated Sensing and Computing Capabilities for Food Spoilage Detection". *Advanced Science*.
- Wonjun Shin et al. "Annealing Ambient and Film Thickness Dependent NO2 Response and 1/ f Noise Characteristics of IGZO Resistor-Type Gas Sensors". *IEEE Transactions on Electron Devices*.
- Wonjun Shin et al. "Channel-Length-Dependent Low-Frequency Noise Characteristics of Ferroelectric Junctionless Poly-Si Thin-Film Transistors". *IEEE Electron Device Letters*.
- Wonjun Shin et al. "Self-Curable Synaptic Ferroelectric FET Arrays for Neuromorphic Convolutional Neural Network". *Advanced Science*.
- Jaehyeon Kim et al. "A novel pathway to construct gas concentration prediction model in real-world applications: Data augmentation; fast prediction; and interpolation and extrapolation". *Sensors and Actuators B: Chemical*.
- Ryun-Han Koo et al. "Optimizing Post-Metal Annealing Temperature Considering Different Resistive Switching Mechanisms in Ferroelectric Tunnel Junction". *IEEE Electron Device Letters*.
- Dongseok Kwon et al. "Super-steep synapses based on positive feedback devices for reliable binary neural networks". *Applied Physics Letters*.
- Wonjun Shin et al. "Effects of temperature and DC cycling stress on resistive switching mechanisms in hafnia-based ferroelectric tunnel junction". *Applied Physics Letters*.
- Wonjun Shin et al. "Low-frequency noise characteristics of indium–gallium–zinc oxide ferroelectric thin-film transistors with metal–ferroelectric–metal–insulator–semiconductor structure". *Applied Physics Letters*.
- Dongseok Kwon et al. "Hardware-Based Ternary Neural Network Using AND-Type Poly-Si TFT Array and Its Optimization Guideline". *IEEE Transactions on Electron Devices*.
- Wonjun Shin et al. "Low-frequency noise in gas sensors: A review". *Sensors and Actuators B: Chemical*.
- Ho-Nam Yoo et al. "Effect of layer-specific synaptic retention characteristics on the accuracy of deep neural networks". *Solid-State Electronics*.
- Jinwoo Park et al. "H2S gas sensing properties in polysilicon control-gate FET-type gas sensor". *Solid-State Electronics*.
- Yujeong Jeong et al. "Effects of oxygen gas in the sputtering process of the WO3 sensing layer on NO2 sensing characteristics of the FET-type gas sensor". *Solid-State Electronics*.
- Wonjun Shin et al. "Recovery of off-state stress-induced damage in FET-type gas sensor using self-curing method". *Discovery Nano*.
- Seongbin Hong et al. "Macroscopic analysis and design of Si HFGFET gas sensor for sensitive gas detection". *Solid-State Electronics*.
- Wonjun Shin et al. "In-Memory-Computed Low-Frequency Noise Spectroscopy for Selective Gas Detection Using a Reducible Metal Oxide". *Advanced Science*.
- Wonjun Shin et al. "1/f Noise in Synaptic Ferroelectric Tunnel Junction: Impact on Convolutional Neural Network". *Advanced Intelligent Systems*.
- Ryun-Han Koo et al. "Proposition of Adaptive Read Bias: A Solution to Overcome Power and Scaling Limitations in Ferroelectric-Based Neuromorphic System". *Advanced Science*.
- Sung-Ho Park et al. "Voltage scheme for string-select transistors to improve inhibition characteristics during 1-bit erase in vertical NAND flash". *Applied Physics Letters*.

**2022**

- Sung Yun Woo et al. "Demonstration of integrate-and-fire neuron circuit for spiking neural networks". *Solid-State Electronics*.
- Wonjun Shin et al. "Variability analysis of ferroelectric FETs in program operation using low-frequency noise spectroscopy". *Applied Physics Letters*.
- Gyuweon Jung et al. "Design optimization of FET-type gas sensor considering device characteristics, sensitivity, power, noise, and SNR". *Sensors and Actuators B: Chemical*.
- Wonjun Shin et al. "Highly Efficient Self-Curing Method in MOSFET Using Parasitic Bipolar Junction Transistor". *IEEE Electron Device Letters*.
- Meile Wu et al. "Characterization and Modeling of a Pt-In2O3 Resistive Sensor for Hydrogen Detection at Room Temperature". *Sensors*.
- Wonjun Shin et al. "Synergistic improvement of sensing performance in ferroelectric transistor gas sensors using remnant polarization". *Material Horizons*.
- Jinwoo Park et al. "Analysis of Cr/Au contact reliability in embedded poly-Si micro-heater for FET-type gas sensor". *Sensors and Actuators B: Chemical*.
- Wonjun Shin et al. "Investigation of Low-Frequency Noise Characteristics of Ferroelectric Tunnel Junction: From Conduction Mechanism and Scaling Perspectives". *IEEE Electron Device Letters*.
- Wonjun Shin et al. "Fully integrated FET-type gas sensor with optimized signal-to-noise ratio for H2S gas detection". *Sensors and Actuators B: Chemical*.
- Wonjun Shin et al. "Optimization of channel structure and bias condition for signal-to-noise ratio improvement in Si-based FET-type gas sensor with horizontal floating-gate". *Sensors and Actuators B: Chemical*.
- Gyuweon Jung et al. "Highly Selective and Low-Power Carbon Monoxide Gas Sensor Based on the Chain Reaction of Oxygen and Carbon Monoxide to WO3". *ACS Applied Materials & Interfaces*.
- Wonjun Shin et al. "Effects of Postdeposition Annealing Ambience on NO2 Gas Sensing Performance in Si-Based FET-Type Gas Sensor". *IEEE Transactions on Electron Devices*.
- Donghee Kim et al. "Effects of Electrode Structure on H2S Sensing and Low-frequency Noise Characteristics in In2O3-based Resistor-type Gas Sensors". *IEEE Sensors Journal*.
- Seongbin Oh et al. "Neuron Circuits for Low-Power Spiking Neural Networks Using Time-To-First-Spike Encoding". *IEEE Access*.
- Soyoun Kim et al. "Investigation of Device Performance for Fin Angle Optimization in FinFET and Gate-All-Around FETs for 3 nm-Node and Beyond". *IEEE Transactions on Electron Devices*.
- Sung Yun Woo et al. "Demonstration of integrate-and-fire neuron circuit for spiking neural networks". *Solid-State Electronics*.
- Wonjun Shin et al. "Comprehensive and accurate analysis of the working principle in ferroelectric tunnel junctions using low-frequency noise spectroscopy". *Nanoscale*.
- Wonjun Shin et al. "Effects of Channel Length Scaling on the Signal-to-Noise Ratio in FET-Type Gas Sensor With Horizontal Floating-Gate". *IEEE Electron Device Letters*.

**2021**

- Wonjun Shin et al. "Effects of IGZO film thickness on H2S gas sensing performance: Response, excessive recovery, low-frequency noise, and signal-to-noise ratio". *Sensors and Actuators B: Chemical*.
- Yujeong Jeong et al. "Highly stable Si MOSFET-type humidity sensor with ink-jet printed graphene quantum dots sensing layer". *Sensors and Actuators B: Chemical*.
- Sugn-Tae Lee et al. "Novel Method Enabling Forward and Backward Propagations in NAND Flash Memory for On-Chip Learning". *IEEE Transactions on Electron Devices*.
- Hyungyo Kim et al. "Direct Gradient Calculation: Simple and Variation-Tolerant On-Chip Training Method for Neural Networks". *Advanced Intelligent Systems*.
- Ho-Nam Yoo et al. "Effect of Lateral Charge Diffusion on Retention Characteristics of 3D NAND Flash Cells". *IEEE Electron Device Letters*.
- Young-Tak Seo et al. "3-D and-Type Flash Memory Architecture With High-κ Gate Dielectric for High-Density Synaptic Devices". *IEEE Transactions on Electron Devices*.
- Wonjun Shin et al. "Effect of charge storage engineering on the NO2 gas sensing properties of a WO3 FET-type gas sensor with a horizontal floating-gate". *Nanoscale*.
- Won-Mook Kang et al. "Hardware-Based Spiking Neural Network Using a TFT-Type AND Flash Memory Array Architecture Based on Direct Feedback Alignment". *IEEE Access*.
- Gyuweon Jung et al. "A low-power embedded poly-Si micro-heater for gas sensor platform based on a FET transducer and its application for NO2 sensing". *Sensors and Actuators B: Chemical*.
- Huaping Wang et al. "Gas Sensing Materials Roadmap". *Journal of Physics: Condensed Matter*.
- Gyuweon Jung et al. "Comparison of the characteristics of semiconductor gas sensors with different transducers fabricated on the same substrate". *Sensors and Actuators B: Chemical*.
- Seongbin Oh et al. "Spiking Neural Networks with Time-to-First-Spike Coding Using TFT-type Synaptic Device Model". *IEEE Access*.
- Wonjun Shin et al. "Impacts of Program/Erase Cycling on the Low-Frequency Noise Characteristics of Reconfigurable Gated Schottky Diodes". *IEEE Electron Device Letters*.
- Dongseok Kwon et al. "Low-power and reliable gas sensing system based on recurrent neural networks". *Sensors and Actuators B: Chemical*.
- Seongbin Hong et al. "FET-type gas sensors: A review". *Sensors and Actuators B: Chemical*.
- Dongseok Kwon et al. "Investigation of Low-Frequency Noise Characteristics in Gated Schottky Diodes". *IEEE Electron Device Letters*.
- Jong-Won Back et al. "Variability of DRAM Peripheral Transistor at Liquid Nitrogen Temperature". *IEEE Transactions on Electron Devices*.
- Wonjun Shin et al. "Optimization of post-deposition annealing temperature for improved signal-to-noise ratio in In2O3 gas sensor". *Semiconductor Science and Technology*.
- Jangsaeng Kim et al. "On-chip trainable hardware-based deep Q-networks approximating a backpropagation algorithm". *Neural Computing and Applications*.
- Sungmin Hwang et al. "Low-Latency Spiking Neural Networks Using Pre-Charged Membrane Potential and Delayed Evaluation". *Frontiers in Neuroscience*.
- Jangsaeng Kim et al. "Hardware-based spiking neural network architecture using simplified backpropagation algorithm and homeostasis functionality". *Neurocomputing*.
- Wonjun Shin et al. "Improved signal-to-noise-ratio of FET-type gas sensors using body bias control and embedded micro-heater". *Sensors and Actuators B: Chemical*.
- Kitae Lee et al. "Effects of Process-Induced Defects on Polarization Switching in Ferroelectric Tunneling Junction Memory". *IEEE Electron Device Letters*.
- Xiaoshi Jin et al. "A Study on the Efect of the Structural Parameters and Internal Mechanism of a Bilateral Gate-Controlled S/D Symmetric and Interchangeable Bidirectional Tunnel Field Efect Transistor". *Nanoscale Research Letters*.
- Min-Kyu Park et al. "CMOS-Compatible Low-Power Gated Diode Synaptic Device for Hardware-Based Neural Network". *IEEE Transactions on Electron Devices*.
- Soochang Lee et al. "SiO2 Fin-Based Flash Synaptic Cells in AND Array Architecture for Binary Neural Networks". *IEEE Electron Device Letters*.
- Wonjun Shin et al. "Effects of High-Pressure Annealing on the Low-Frequency Noise Characteristics in Ferroelectric FET". *IEEE Electron Device Letters*.
- Sung-Tae Lee et al. "Utilization of Unsigned Inputs for NAND Flash Based Parallel and High-Density Synaptic Architecture in Binary Neural Networks". *IEEE Journal of the Electron Devices Society*.
- Meile Wu et al. "Branched Polyethylenimine Based Field Effect Transistor for Low Humidity Detection at Room Temperature". *IEEE Sensors Journal*.
- Dongseok Kwon et al. "Efficient fusion of spiking neural networks and FET-type gas sensors for a fast and reliable artificial olfactory system". *Sensors and Actuators B: Chemical*.
- Kitae Lee et al. "Ferroelectric-Metal Field-Effect Transistor with Recessed Channel for 1T-DRAM Application". *IEEE Journal of the Electron Devices Society*.
- Munhyeon Kim et al. "Suppression of Statistical Variability in Stacked Nanosheet Using Floating Fin Structure". *IEEE Electron Device Letters*.
- Munhyeon Kim et al. "Double-Gated Ferroelectric-Gate Field-Effect-Transistor for Processing in Memory". *IEEE Electron Device Letters*.
- Ryoongbin Lee et al. "Vertically-Stacked Si0.2Ge0.8 Nanosheet Tunnel FET With 70 mV/Dec Average Subthreshold Swing". *IEEE Electron Device Letters*.
- Kyung Kyu Min et al. "Interlayer engineering for enhanced ferroelectric tunnel junction operations in HfOx-based metal-ferroelectric-insulator-semiconductor stack". *Nanotechnology*.
- Seunghwan Song et al. "Integrate-and-Fire Neuron Circuit With Synaptic Off-Current Blocking Operation". *IEEE Access*.
- Gyuweon Jung et al. "Response Comparison of Resistor- and Si FET-Type Gas Sensors on the Same Substrate". *IEEE Transactions on Electron Devices*.
- Sihyun Kim et al. "Gate-First Negative Capacitance Field-Effect Transistor With Self-Aligned Nickel-Silicide Source and Drain". *IEEE Transactions on Electron Devices*.
- Md. Hasan Raza Ansari et al. "Core-Shell Dual-Gate Nanowire Memory as a Synaptic Device for Neuromorphic Application". *IEEE Journal of the Electron Devices Society*.
- Sihyun Kim et al. "Physical Unclonable Functions Using Ferroelectric Tunnel Junctions". *IEEE Electron Device Letters*.
- Young Suh Song et al. "Improvement of self-heating effect in Ge vertically stacked GAA nanowire pMOSFET by utilizing Al2O3 for high-performance logic device and electrical/thermal co-design". *Japanese Journal of Applied Physics*.
- Jeesoo Chang et al. "A Systematic Compact Model Parameter Calibration with Adaptive Pattern Search Algorithm". *Applied Sciences*.
- Sung Yun Woo et al. "Pulse-Width Modulation Neuron Implemented by Single Positive-Feedback Device". **.
- Dongseok Kwon et al. "Hardware-Based Spiking Neural Networks Using Capacitor-Less Positive Feedback Neuron Devices". *IEEE Transactions on Electron Devices*.
- Sung-Tae Lee et al. "Pruning for Hardware-Based Deep Spiking Neural Networks Using Gated Schottky Diode as Synaptic Devices". *Journal of Nanoscience and Nanotechnology*.

## 국제 학회 발표 (2021–2026)

랩 Conference 페이지(571건, 연도 내림차순)의 2021–2026년 항목 가운데 International 분류 32건이다. 누리집은 학회 항목마다 제목, 대회명, 기간(연도), 참가자만 적으며, 줄 앞의 이름은 참가자 칸이고 기울인 글씨는 대회명이다. 교수의 기조 강연(Plenary talk)도 이 페이지에 실려 있다.[^conf]

**2026**

- Jong-Ho Lee. "Looking Back on Semiconductor Research in My Life(Plenary talk)". *Institute of Science Tokyo*.
- Jong-Ho Lee. "AI Semiconductors in Korea(Plenary talk)". *Symposium on System Device Roadmap in Japan*.
- Joon-Hwang. "Monolithic Integration of Low-Voltage Flash Synaptic Arrays with CMOS Circuits for Neuromorphic Systems". *The 22nd International Symposium on the Physics of Semiconductors and Applications (ISPSA)*.

**2025**

- Jong-Ho Lee. "AI Semiconductor Policy and Flash Memory-Based Neural Networks (Plenary Talk)". *International Conference on Electronics, Information, and Communication (ICEIC) 2025*.
- Kyu-Ho Lee. "Nor-type Gated Diode Synapse Array with Selective Program/Erase Operation Capabilities". *EuroSOI Workshop and International Conference on Ultimate Integration on Silicon*.
- In-Seok Lee. "Low-Power Hierarchical Similarity Search Using Analog CAM Based on Dual-Gate FET". *2025 International Conference on Solid State Devices and Materials*.
- Sung-Ho Park. "Approximate Neural Network Using Vertical NAND Flash Memory". *2025 International Conference on Solid State Devices and Materials*.
- Kyung Min Lee, Ryun-Han Koo. "Concealable and Bit Error-Free Breakdown-Based Physical Unclonable Functions Using Magnetic Tunnel Junctions". *IEEE International Electron Devices Meeting*.
- Sangwoo Ryu, Ryun-Han Koo. "HZO FeCap with Ultra-High 2Pr = 133 μC/cm², PZT-Level Ec (1.17MV/cm @ 6 nm), and CMWε = 9.6 @ 0 V by Adopting HfO2-TiO2-HfO2 Pseudomorphic Interlayer". *IEEE International Electron Devices Meeting*.
- Hunhee Shin, Jinwoo Park. "Innovative Mixed Gas Discrimination System Using Integrated Self-Cancellation Circuit". *IEEE International Electron Devices Meeting*.

**2024**

- Jeonghyun Kim. "Comparative Analysis of TFT-Type Synaptic Device Characteristics with P-Type Doped Body Structures". *International Conference on Electronics, Information, and Communication (ICEIC) 2024*.
- Donghee Kim. "Humidity-Tolerant Neuromorphic Olfactory Systems Based on Hardware-Deployable Spiking Neural Networks and SnOx Resistor-Type Gas Sensors". *Solid-State Devices and Materials*.
- Sangwoo Ryu. "Comparative Analysis of Ferroelectric Domain Wall Motion Under Cycling Stress of HfZrO2 Fabricated by Thermal and Plasma-Enhanced Atomic Layer Depositions". *Solid-State Devices and Materials*.
- Jong-Ho Lee. "AI Semiconductor Policy and Flash Memory-Based Neural Networks (Plenary Talk)". *The 7th International Conference on Memristive Materials, Devices & Systems (MERISIS) 2024*.

**2023**

- Jangsaeng Kim, Jiseong Im. "First Demonstration of Innovative 3D AND-Type Fully-Parallel Convolution Block with Ultra-High Area-and Energy-Efficiency". *2023 International Electron Devices Meeting (IEDM)*.
- Chayoung Lee. "Temperature Measurement Method Using FET Type Gas Sensor". *2023 7th IEEE Electron Devices Technology & Manufacturing Conference (EDTM)*.
- Gyuweon Jung. "New Gas Identification Method Using Gas Sensor-Amplifier Merged Array and In-Memory Computing-Based Preprocessing". *2023 International Electron Devices Meeting (IEDM)*.

**2022**

- Sung-Ho Park. "Retention Improvement in Vertical NAND Flash Memory Using 1-bit Soft Erase Scheme and its Effects on Neural Networks". *2022 International Electron Devices Meeting (IEDM)*.
- Gyuweon Jung. "Innovative Gas Sensing Method Using Transient Behavior of FET-type Sensors with Gate Pulse Input". *2022 International Electron Devices Meeting (IEDM)*.
- Yujeong Jeong. "H2S Sensing Characteristics of the Amplifier Circuit Consisting of pFET-type and Resistor-type Gas Sensors". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Jiseong Im, Donghee Kim. "A Neuromorphic Olfactory System Using Temporal Encoded Spiking Neural Networks". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Seongbin Oh. "Synaptic Devices Based on 3D-Semicircular NAND Flash Memory". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Gyuweon Jung. "Comparison of the H2S gas response characteristics of semiconductor gas sensors (HFGFET-, TFT-, and resistor-type) fabricated on the same wafer". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Dongseok Kwon. "Effects of Static Current in AND-Type TFT Synaptic Devices on Supervised On-Chip Training". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Jangsaeng Kim. "Implementation of Homeostasis Functionality in Hardware-Based Spiking Neural Networks Using an STDP Learning Rule". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Hyeongsu Kim. "Variation-robust Binary Matrix-vector Multiplication Method". *International Conference on Solid State Devices and Materials (SSDM 2022) *.
- Ho-Nam Yoo. "First demonstration of 1-bit erase in vertical NAND flash memory". *2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*.
- Kangwook Choi. "Response Analysis of Resistor-type Gas Sensor with Bias Voltage Condition". *2022 IEEE International Symposium on Olfaction and Electronic Nose (ISOEN)*.
- Gyuweon Jung. "Optimal Bias Conditions for FET-type Gas Sensors to Minimize Current Fluctuations". *2022 IEEE International Symposium on Olfaction and Electronic Nose (ISOEN)*.

**2021**

- Yujeong Jeong. "Amplifier Circuit Consisting of the FET-type Gas Sensors with Tunable FET Load". *2021 International Conference on Solid State Devices and Materials*.
- Seongbin Hong. "Gas Sensing Performance of a Gated Lateral pnp-Bipolar Junction Transistor Gas sensor Having a Horizontal Floating-Gate Structure". *2021 International Conference on Solid State Devices and Materials*.
- Wonjun Shin. "Sub-ppm Detection of NO2 gas using IGZO TFT-type Gas Sensor with Optimal Signal-to-Noise Ratio". *2021 International Conference on Solid State Devices and Materials*.

## 국내 학회 발표 (2021–2026)

같은 Conference 페이지의 2021–2026년 항목 가운데 Domestic 분류 83건이다. 줄의 형식은 국제 학회 발표와 같다.[^conf]

**2026**

- Taeho Lee. "Latch-up Voltage Modulation by Applying Adaptive Pulse on Charge-Trap Based Floating-Body Transistor". *제 33회 한국반도체학술대회*.
- Jongho Ji. "Effect of Hf:Zr Ratio on Phase Transition and Cycling Behavior in Hf1₋xZrxO2 Thin Films". *제 33회 한국반도체 학술대회*.
- Jeonghyun Kim. "New Weight Modulation Method for Charge Trap Flash-Based Synaptic Devices". *제 33회 한국반도체 학술대회*.
- Sanghyun Leem. "Double-Gate Synaptic Device for Fowler-Nordheim-Tunneling-Based Selective Program/Erase in NOR Arrays". *대한전자공학회 하계종합학술대회*.
- Sungyun Cho. "NO2 Gas Sensing Properties of NiO-Based FET-type Gas Sensors". *대한전자공학회 하계종합학술대회*.
- Jong-Ho Lee. "Low-power AI Semiconductors(Plenary talk)". *KIEEME Annual Summer Conference 2026*.
- Jong-Ho Lee. "AI Semiconductors(plenary talk)". *Korea IT Fund*.
- Jong-Ho Lee. "Physical AI 시대의 반도체(plenary talk)". *Hankyung, Strong Korea*.
- Jong-Ho Lee. "Low Power Neural Networks Using Flash Memory(Plenary talk)". *Samsung Electronics*.

**2025**

- Suyoung Park. "Mechanisms and Effects of Deep Traps in Charge Trap Devices". *하계종합 학술대회*.
- Seungwhan Kim. "HfZrO2 기반 강유전성 터널 접합의 동작 특성에 대한 상부 금속 증착 방법 비교 분석". *하계종합 학술대회*.
- Jeonghyun Kim. "A Novel True Random Number Generator based on FET-type device with Al2O3/Si3N4 as a Gate Insulator Stack". *제32회 한국반도체학술대회*.
- Donghee Kim. "Humidity-independent NO2 Gas Identification Using a Neuromorphic Olfactory System Based on p-type and n-type SnOx Gas Sensors". *제32회 한국반도체학술대회*.
- Hunhee Shin. "Effect of Asymmetric Air-gap on Dual FET-type Gas Sensor Considering Thermoelectric Effect". *한국반도체학술대회*.
- Jaehyeon Kim. "Enhancing Robustness to Weight Variance in Neuromorphic Systems with Lipschitz Regularization". *제32회 한국반도체학술대회*.
- In-Seok Lee. "Batch Training Optimization Method on Neuromorphic Hardware". *제 32회 한국반도체학술대회*.
- Joon Hwang. "Analysis of Bias-Dependent Retention Characteristics of the Flash Memory Device without Tunneling Oxide". *한국반도체학술대회*.

**2024**

- InSeok Lee. "A CNN Accelarator Based on 3D NAND Flash Memory with Input Reuse". *제 31회 한국반도체학술대회*.
- Kyuho Lee. "Operation Principle of Reconfigurable Integrate-and-Fire Neuron Circuit". *제 31회 한국반도체학술대회*.
- Kangwook Choi. "Enhancement of Gas Sensing Performance in CuO Resistor-type Gas Sensors via Pre-Bias Voltage". *제 31회 한국반도체학술대회*.
- Jonghyun Ko. "Compute-in-Memory for Vision Transformer Using Thin Film Transistor Memory". *제 31회 한국반도체학술대회*.
- Jinwoo Park. "Effect of Forming Gas Annealing on Reliability of Embedded Poly-silicon Micro-heater". *제 30회 한국반도체학술대회*.
- Seungwhan Kim. "Effects of Nonlinear Conductance Update of Synaptic Devices on On-Chip Learning in Hardware Neural Network". *제 31회 한국반도체학술대회*.
- Jong-Ho Lee. "과학기술정보통신부 주요정책: AI/반도체 중심 (Plenary Talk)". *한국센서학회 추계학술대회 2024*.
- Donghee Kim. "NO2 Gas Sensing Characteristics of Resistor-Type Tin-Oxide-Based Gas Sensors with Different Post-Deposition Annealing Conditions". *나노코리아 2024*.

**2023**

- Hunhee Shin. "Effects of Annealing Conditions on NO2 Gas Response and Optimal Operating Temperature in Resistor-Type Gas Sensors". *제 30회 한국반도체학술대회*.
- Jiseong Im. "Efficient Gas Detection with Spiking Neural Networks using Temporal Gas-Detecting Neuron". *NANO KOREA 2023*.
- Jeonghyun Kim. "Novel Weight Update Scheme in Charge Trap Flash Based Synaptic Device". *NANO KOREA 2023*.
- Seungwhan Kim. "Effects of Current Fluctuation of Synapse Devices on On-Chip Learning in Hardware Neural Networks". *제 30회 한국반도체학술대회*.
- InSeok Lee. "Weight mapping scheme using gate voltage of NOR flash memory array". *제 30회 한국반도체학술대회*.
- Joon Hwang. "Effects of Inverter Circuit Size on Analog Pulse-Width Modulation Circuit". *제 30회 한국반도체학술대회*.
- Jinwoo Park. "NO2 Gas Sensing Properties of FET-type Gas Sensor with Poly-Si Used as an Embedded Micro-heater and Control-gate". *제 30회 한국반도체학술대회*.
- Jonghyun Ko. "Energy-efficient Neuron Circuit with Minimized Shoot-through Current". *제 30회 한국반도체학술대회*.
- Seongbin Oh. "Synaptic Devices Based on 3D-Semicircular NAND Flash Memory". *제 30회 한국반도체학술대회*.
- Gyuho Yeom. "Effect of Cell Position in Cell Strings on the Performance of Neural Networks Using NAND Flash Memory". *제 30회 한국반도체학술대회*.
- Donghee Kim. "A Hardware-Deployable SNN-based Approach to Data Encoding and Gas Identification Using Resistor-type Gas Sensors". *NANO KOREA 2023*.

**2022**

- Seongbin Oh. "Analysis of The Effect of Line Resistance in 3D Synaptic Array on The Accuracy of Spiking Neural Networks". *제 29회 한국반도체학술대회*.
- Hunhee Shin. "Investigation of H2S gas response in resistor- and FET-type gas sensors". *대한전자공학회 2022 하계종합학술대회*.
- Kangwook Choi. "NO2 gas Response Improvement of Gas Sensors by Adopting Oxygen Vacancy Controlled In2O3 Bilayer Sensing Films". *제 30회 한국반도체학술대회*.
- Wonjun Shin. "Low-Frequency Noise Characteristics of Hafnium Zirconium Oxide Ferroelectric Field-Effect_Transistors". *대한전자공학회 2022년도 추계학술대회*.
- Wonjun Shin. "Effects of Bias Conditions on Low Frequency Noise characteristics in Ferroelectric Based Memories". *대한전자공학회 2022 하계종합학술대회*.
- Joon Hwang. "Synaptic Error-Tolerant Off-Chip Training Method for All-Analog Neuromorphic Systems". *대한전자공학회 2022 하계종합학술대회*.
- Jonghyun Ko. "Analysis of energy consumption of integrate-and-fire neuron circuit". *대한전자공학회 2022 하계종합학술대회*.
- Wonjun Shin. "Highly improved NO2 gas sensing performances using charge storage engineering in FET-type gas sensor with embedded micro-heater". *2022년 한국센서학회 춘계학술대회*.
- Yujeong Jeong. "Comparison of the H2S Sensing Characteristics of the Amplifier Circuits Consisting of the FET-type Gas Sensors with different load". *2022 한국센서학회 춘계학술대회*.
- Wonjun Shin. "Low-frequency noise characteristics of ferroelectric tunnel junction". *NANO KOREA 2022*.
- Jeonghyun Kim. "Awareness Training of Neuron Device with Al2O3/Si3N4 as a Gate Insulator Stack". *대한전자공학회 2022 하계종합학술대회*.
- Kyuho Lee. "Neuron-Aware Training for IF neurons with non-linearity in Spiking Neural Networks". *대한전자공학회 2022 하계종합학술대회*.
- Ryunhan Koo. "Power efficient read bias scheme of the synaptic devices for neuromorphic applications". *대한전자공학회 2022 하계종합학술대회*.
- Sungho Park. "Improvement of Retention Characteristics of Charge Trap Flash Memory Cells by Soft Erase after Programming". *대한전자공학회 2022 하계종합학술대회*.
- InSeok Lee. "Thin Film Transistor-based Low-Power Gated Diode Synaptic Device Using Gated Induced Drain Leakage Current". *대한전자공학회 2022 하계종합학술대회*.

**2021**

- Dongseok Kwon. "Vth effect of TFT Type Flash Devices on Accuracy in Neuromorphic System Capable of On-chip Training". *제 28회 한국반도체학술대회*.
- Sung-Tae Lee. "Hardware based deep spiking neural networks using gated Schottky diode as synaptic devices". *NANO KOREA 2021*.
- Jaehyeon Kim. "Hardware-Friendly Temporal Backpropation Algorithm for Spiking Neural Networks". *대한전자공학회 2021년도 하계종합학술대회*.
- Wonjun Shin. "Effects of oxygen flow rate on the NO2 gas sensing and low-frequency noise characteristics in IGZO gas sensors". *NANO KOREA 2021*.
- Kyuho Lee. "Area-efficient hardware design for neural network using TFT-type synaptic devices". *NANO KOREA 2021*.
- Joon Hwang. "Mitigating the effect of quantization error in synaptic conductance of off-chip learning neuromorphic systems". *NANO KOREA 2021*.
- Dongseok Kwon. "Analog Memory Device with an Al2O3/Si3N4 Gate Stack for On-Chip Trainable Hardware-Based Neural Networks". *NANO KOREA 2021*.
- Jangsaeng Kim. "Hardware Implementation of Reinforcement Learning with Analog Synaptic Devices". *제 28회 한국반도체학술대회*.
- Hyeongsu Kim. "Effect of Conductance Variation in Synaptic Devices on Classification Accuracy with three Classification Methods". *제 28회 한국반도체학술대회*.
- Donghee Kim. "Effect of Sensing Layer Length on H2S Gas Sensing and Low-frequency Noise in Resistor-type Gas Sensor". *제 28회 한국반도체학술대회*.
- Seongbin Oh. "Inference of the single spike temporal-coded data in spiking neural networks". *제 28회 한국반도체학술대회*.
- Wonjun Shin. "Effect of post deposition annealing atmosphere on NO2 gas sensing and low-frequency noise in IGZO thin-film chemresistor gas sensor". *제 28회 한국반도체학술대회*.
- Jinwoo Park. "H2S Gas Sensing Properties in Polysilicon Control-Gate FET Gas Sensor". *제 28회 한국반도체학술대회*.
- Seongbin Hong. "Macroscopic Analysis and Design of Si HFGFET Gas Sensor for Sensitive Gas Detection". *제 28회 한국반도체학술대회*.
- Soochang Lee. "Multi-level Synaptic Array Based on AND-type Flash Memory for Hardware-based Neural Network". *제 28회 한국반도체학술대회*.
- Honam Yoo. "Effect of Layer-specific Synaptic Retention Characteristics on the Accuracy of Deep Neural Networks". *제 28회 한국반도체학술대회*.
- Gyuweon Jung. "H2S Gas Sensing Characteristics of Si FET-type Gas Sensor with Localized Micro-heater". *제 28회 한국반도체학술대회*.
- Sung Yun Woo. "Demonstration of Integrate-and-fire Neuron Circuit for Spiking Neural Networks". *제 28회 한국반도체학술대회*.
- Yujeong Jeong. "Effects of Oxygen Gas Flow on the Response of FET-type Gas Sensor with Sputtered WO3 Sensing Layer". *제 28회 한국반도체학술대회*.
- Hyeongsu Kim. "Comparison of Batch-Normalization and Layer-Normalization for Hardware-based Binary Neural Network Implementation". *제 29회 한국반도체학술대회*.
- Seungwhan Kim. "Solution to Solve Inference Accuracy Degradation Due to Stuck-at-Faults". *제 29회 한국반도체학술대회*.
- Kangwook Choi. "Response analysis of resistor-type gas sensor with read bias condition". *제 29회 한국반도체학술대회*.
- Jinwoo Park. "Effects of Annealing Temperature on Stability of FET-type Gas Sensor". *제 29회 한국반도체학술대회*.
- Yujeong Jeong. "NO2 Sensing Characteristics of the Amplifier Circuit Consisting of the FET-type Gas Sensors with FET Load". *2021 한국센서학회 추계학술대회*.
- Seongbin Hong. "SPICE Modeling of Field Effect Transistor-Type Neuron Device with Al2O3/Si3N4 as a Gate Insulator Stack for Neuromorphic System". *제 29회 한국반도체학술대회*.
- Seongbin Hong. "Capacitor-Based Gas Sensor with a ZnO Sensing Layer". *제29 회 한국반도체학술대회*.
- Seongbin Hong. "Long-term degradation characteristics of gas response depending on deposition atmosphere of sensing layer in FET-type gas sensors". *2021 한국센서학회 추계학술대회*.
- Ryunhan Koo. "Analysis of Cycling Endurance Characteristics in Field Effect Transistor-type Synaptic Device for Neuromorphic Applications". *대한전자공학회 2021년도 하계종합학술대회*.
- Min Kyu Park. "CMOS-Compatible Gated Diode-type Gas Sensor for H2S Gas Detection". *대한전자공학회 2021년도 하계종합학술대회*.
- Donghee Kim. "A Spiking Neural Network for Time-Efficient Gas Concentration Level Estimation in Resistor-Type Gas Sensors". *대한전자공학회 2021년도 하계종합학술대회*.
- Gyuho Yeom. "Effect of String Select Gate Bias in NAND Flash Memory Cell Strings for Hardware-based Neural Networks". *대한전자공학회 2021년도 하계종합학술대회*.
- Jiseong Im. "Implementing Error Generating Circuit for Temporal Spiking Neural Networks". *대한전자공학회 2021년도 하계종합학술대회*.

## 특허

랩 Patent 게시판 135건 가운데 글에 적힌 출원일이나 등록일이 2021년 10월 22일 이후인 20건(게시판 번호 116–135)이다. 줄 앞의 날짜는 등록일(등록 기록이 없으면 출원일)이고, 분류(Domestic·International)와 상태(Registration·Application)는 게시판 분류, 출원·등록 번호와 날짜, 발명자는 각 글의 표기 그대로다. 발명자를 적지 않은 글도 있다.[^patents]

- 2026-09-29 · 3차원 시냅스 소자 스택 및 이를 이용한 3차원 적층형 시냅스 어레이 및 3차원 시냅스 소자 스택의 제조 방법 (분류 Domestic; 상태 Registration; 출원 17/888770(2022.08.16); 등록 12751008(2026.09.29); 발명자 김장생, 서영탁, 오성빈, 이수창, 이종호)
- 2026-07-30 · 선택된 하나의 플래시 메모리 셀 지우기가 가능한 낸드 플래시 메모리 장치 및 그 동작 방법 (분류 Domestic; 상태 Registration; 출원 1020210182231(2021.12.17); 등록 10-2999490(2026.07.30); 발명자 유남호, 이종호)
- 2026-03-03 · 단위 시냅스를 위한 커패시터 소자, 단위 시냅스 및 커패시터 기반의 시냅스 어레이 (분류 International; 상태 Registration; 출원 미국(US) 17/967,373호 (2022-10-17); 등록 미국(US) 12566964 (2026-03-03); 발명자 이종호, 김형수)
- 2026-02-25 · 강유전체 기반의 시냅스 소자 및 시냅스 소자의 동작 방법, 상기 시냅스 소자를 기반으로 한 3D 시냅스 소자 스택 (분류 Domestic; 상태 Registration; 출원 10-2023-0027789(2023.03.02); 등록 2932656(2026.02.25); 발명자 김정현, 박민규, 이종호, 황준)
- 2025-12-30 · NAND flash memory device with enhanced data retention characteristics and operating method thereof (분류 International; 상태 Registration; 출원 18/340,473(2023.06.23); 등록 12,512,161(2025.12.30); 발명자 박성호)
- 2025-12-09 · 3차원 시냅스 소자 스택 및 이를 이용한 3차원 적층형 시냅스 어레이 및 3차원 시냅스 소자 스택의 제조 방법 (분류 Domestic; 출원 17/888,772(2022.08.16); 등록 12,495,553(2025.12.09); 발명자 김장생, 서영탁, 오성빈, 이수창, 이종호)
- 2025-11-18 · 아날로그-디지털 컨버터 (분류 Domestic; 출원 10-2024-0074636 (2024-06-08); 등록 10-2889488-00-00 ( 2025-11-18 ); 발명자 이종호, 임지성, 고종현)
- 2025-10-14 · 선택적 1셀 지우기를 이용한 낸드 플래시 메모리 저장 방법 (분류 Domestic; 상태 Registration; 출원 17/715809(2022.04.07); 등록 12444469(2025.10.14); 발명자 유호남, 이종호)
- 2025-05-20 · 3차원 커패시터 스택 및 3차원 커패시터 스택의 제조 방법 (분류 International; 상태 Registration; 출원 17/888.778(2022.08.16); 등록 12310022(2025.05.20); 발명자 김장생, 서영탁, 오성빈, 이수창, 이종호)
- 2025-04-04 · CMOS 집적 기술을 기반으로 한 시냅스 어레이 구조 및 그 제조 방법 (분류 Domestic; 상태 Registration; 등록 10-2793498 (2025.04.04))
- 2025-03-17 · 마이크로 히터를 갖는 가스 센서 (분류 Domestic; 상태 Registration; 등록 10-2784778 (2025.03.17))
- 2025-02-11 · Ferroelectric-based synaptic device and method of operating the synaptic device, and 3d synaptic device stack using the synaptic devices (분류 International; 상태 Registration; 출원 18/117,108(2023.03.03); 등록 12,224,003(2025.02.11); 발명자 이종호, 김정현)
- 2024-09-24 · On-chip training neuromorphic architecture (분류 International; 상태 Registration; 등록 12099919 (2024.9.24))
- 2024-04-03 · 상보형 센서 일체형 인터페이스 회로 및 상보형 센서 일체형 차동 인터페이스 회로 (분류 Domestic; 상태 Registration; 출원 10-0128292 (2021.09.28); 등록 10-2655502 (2024.04.03); 발명자 이종호, 정유정)
- 2023-12-26 · 단위 시냅스를 위한 커패시터 소자, 단위 시냅스 및 커패시터 기반의 시냅스 어레이 (분류 Domestic; 상태 Registration; 출원 10-0142489 (2021.10.25); 등록 10-2619356 (2023.12.26); 발명자 김형수, 이종호)
- 2022-08-23 · Neuromorphic system (분류 International; 상태 Registration; 등록 11423293 (2022.08.23))
- 2022-08-16 · 3d capacitor stack and method of fabricating the stack (분류 International; 상태 Application; 출원 17/888,770 (2022.8.16))
- 2022-08-16 · 시냅스 스트링 어레이를 이용한 신경망 (Neural network with a synapse string array) (분류 Domestic; 상태 Registration; 등록 1024341190000 (2022.08.16))
- 2022-01-18 · Nonvolatile memory device having stacked cell transistors and operating method thereof (분류 International; 상태 Registration; 등록 11227896 (2022.01.18))
- 2022-01-18 · 신경망을 위한 시냅스 스트링 및 시냅스 스트링 어레이 (Synapse string and synapse string array for neural networks) (분류 Domestic; 상태 Registration; 등록 1023542860000 (2022.01.18))

## 수상

랩 News(일반 게시판) 68건 가운데 2024년 6월–2026년 5월에 작성된 글의 수상 7건이다. 날짜는 게시판 작성일이고, 상 이름과 수상자 표기는 글 제목과 본문을 따랐다.[^news]

- 2026-02-27 · 구륜한 박사 도연 논문상 수상
- 2026-02-27 · Sung-Ho Park, Jonghyun Ko, Ryun-Han Koo, Jongho Ji: presidental science scholarship (PhD)
- 2026-01-08 · Jonghyun Ko: 제17회 전자신문 ICT 논문 공모 대제전 excellence prize
- 2025-05-02 · 신훈희 박사과정: 이종흔 논문상(논문 「On-chip Annealing Using Embedded Micro-Heater for Highly Sensitive Gas Detection」)
- 2025-04-10 · 구륜한 박사과정: 한국공학한림원 제3회 원익 차세대 공학도상 우수상
- 2025-03-04 · Jong-Ho Lee: 31st Humantech Paper Contest(삼성전자) special prize(학생 지도)
- 2025-03-04 · 31st Humantech Paper Contest(삼성전자) Physical Devices 부문: Jonghyun Ko silver prize, Jiseong Im bronze prize, Joon Hwang bronze and encouragement prizes

## 소식

같은 게시판의 2024년 6월–2026년 5월 글 가운데 교수의 기조 강연·초청 연설·행사 참석과 연구팀 학회 논문 소식 10건이다. 날짜는 게시판 작성일이고, 강연 날짜를 글에 따로 적은 소식은 그 날짜를 본문에 함께 적었다.[^news][^iedm]

- 2026-05-07 · 2026-03-26–27 경북대학교 MIT GSW(Global Startup Workshop)에서 「한국의 인공지능 및 반도체」 주제 keynote 강연과 패널토의
- 2025-11-18 · 경암상위원회 위원장으로 제21회 경암상 시상식 참석
- 2025-11-17 · 2025 대한임베디드공학회 추계학술대회 기조강연 「저전력 인공지능 (AI) 반도체 및 그 응용」
- 2025-11-17 · 2025 첨단군사과학융합기술 공동학술대회 기조강연 「국방반도체 추진방향」
- 2025-11-07 · IEEE IEDM 2025에 연구팀 논문 3편 채택(HfO2-TiO2-HfO2 삼중 interlayer 구조의 HfZrO2 강유전 캐패시터, 상용 자기터널접합 소자를 쓴 붕괴 기반 물리 복제 방지 기능, 자기상쇄 회로를 센서와 한 칩에 집적한 혼합가스 판별 시스템)
- 2025-09-15 · 2025-09-08–09 UAE 아부다비 Hili 포럼 「Geotech Disruption: Future Normal」 세미나 연사
- 2025-07-28 · 2025-04-22–26 UAE 두바이 AI Festival 기조연설 「Korea’s AI Policy & Low-Power AI Semiconductor」
- 2025-05-09 · 2025 국제장애고용포럼(IFDE) 기조 강연
- 2025-01-20 · ICEIC 2025 기조강연 「AI Semiconductor Policy and Non-volatile Memory-based Neural Networks」
- 2024-09-04 · 2024 한국센서학회 추계학술대회 기조강연 「과학기술정보통신부 주요정책: AI/반도체 중심」

## 연락과 위치

- 연구실: (우) 08826 서울특별시 관악구 관악로 1 서울대학교 301동[^contact]
- 전화와 팩스: +82-2-880-7285 / +82-2-882-4658[^contact]
- 교수 전화: 02-880-1727[^profcv][^eceprof]
- 학생 모집: 첫 화면은 「27년 2학기 전기정보공학부 석박통합과정 학생」을 모집 중이라고 적고, research fellow, 박사후연구원, 대학원생, 학부생 지원도 받는다고 적는다.[^home]
[^home]: 연구실 누리집 첫 화면 <https://genie.snu.ac.kr/> (ABOUT, Recruiting, 연구 소개 슬라이드, 2026-10-25 열람)
[^intro]: Intro 페이지 <https://genie.snu.ac.kr/intro/> (교수 소개, 2026-10-25 열람)
[^nvm]: Research 메뉴 Nonvolatile Memory 페이지 <https://genie.snu.ac.kr/nonvolatile-memory/> (2026-10-25 열람)
[^neuro]: Research 메뉴 Neuromorphic Device & Processor 페이지 <https://genie.snu.ac.kr/neuromorphic-device-processor/> (2026-10-25 열람)
[^gas]: Research 메뉴 Gas Sensor 페이지 <https://genie.snu.ac.kr/gas-sensor/> (2026-10-25 열람)
[^members]: Members 페이지 <https://genie.snu.ac.kr/members/> (8쪽)와 구성원 개인 페이지(Academic Experiences, Research Topics, 2026-10-25 열람)
[^profcv]: Members 메뉴의 교수 개인 페이지 <https://genie.snu.ac.kr/member/%ec%9d%b4%ec%a2%85%ed%98%b8/> (이력과 수상 목록, 전화, 2026-10-25 열람)
[^journal]: Journal 페이지 <https://genie.snu.ac.kr/journal/> (연도 내림차순 목록 27쪽 가운데 1–11쪽, 2026-10-25 열람)
[^conf]: Conference 페이지 <https://genie.snu.ac.kr/conference/> (화면 표기 총 571개, 연도 내림차순 목록 96쪽 가운데 1–35쪽, 2026-10-25 열람)
[^patents]: Patent 게시판 <https://genie.snu.ac.kr/patent/> (목록 14쪽과 각 글, 2026-10-25 열람)
[^news]: News(일반 게시판) <https://genie.snu.ac.kr/%ec%9d%bc%eb%b0%98-%ea%b2%8c%ec%8b%9c%ed%8c%90/> (목록 6쪽과 각 글, 2026-10-25 열람)
[^iedm]: News 글 「이종호 교수님 연구팀, IEEE IEDM 2025 논문 3편 게재 쾌거」 <https://genie.snu.ac.kr/%ec%9d%bc%eb%b0%98-%ea%b2%8c%ec%8b%9c%ed%8c%90/document/229/> (2025-11-07 작성, 2026-10-25 열람)
[^contact]: Contact 페이지 <https://genie.snu.ac.kr/contact/> (2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (2026-10-25 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 상세(반도체 재료 및 소자연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=40> (연구실 소개 및 연구분야, 주요 연구과제, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 상세(이종호 (S)) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p069> (학위, 전공·분야, 학력, 주요경력, Research Interest, 2026-10-25 열람)
[^p1]: J. Park 외, J.-H. Lee, Advanced Science 11, 2401821 (온라인 2024-05-13). <https://doi.org/10.1002/advs.202401821> 초록 기준.
[^p2]: G. Jung 외, J.-H. Lee, Advanced Science 10, 2302506 (온라인 2023-08-31). <https://doi.org/10.1002/advs.202302506> 초록 기준.
[^p3]: S.-H. Park 외, J.-H. Lee, Nature Communications 16, 5155 (온라인 2025-06-03). <https://doi.org/10.1038/s41467-025-60415-y> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Hwang 외, J.-H. Lee, Physical Review Letters 135, 157001 (온라인 2025-10-06). <https://doi.org/10.1103/lj4r-dcb7> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Ko 외, J.-H. Lee, Science Advances 11, eadt8227 (2025). <https://doi.org/10.1126/sciadv.adt8227> 초록 기준.
[^p6]: J. Im 외, J.-H. Lee, Science Advances 11, eadw7498 (2025). <https://doi.org/10.1126/sciadv.adw7498> 초록 기준.
[^p7]: R.-H. Koo 외, J.-H. Lee, Nature Communications 17, 6236 (온라인 2026-05-08). <https://doi.org/10.1038/s41467-026-72969-6> 초록 기준.
[^p8]: R.-H. Koo 외, J.-H. Lee, Advanced Science 11, 2407729 (온라인 2024-09-26). <https://doi.org/10.1002/advs.202407729> 초록 기준.

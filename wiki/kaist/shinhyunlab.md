# 신경망 모사 소자 및 회로 개발 연구실 (Emerging Nanoelectronic Technology and Integrated Systems Laboratory, ENTIS)

**KAIST 전기및전자공학부 · 최신현 교수**

- 분야: 멤리스터·상변화 메모리 같은 차세대 메모리·연산 소자, 트랜지스터형 시냅스 소자와 멤트랜지스터, 뉴로모픽 컴퓨팅 하드웨어, 멤리스터 배열로 만드는 인공지능 계산 시스템과 그 응용(영상·시계열 데이터 처리, 보안, 로봇 감각)
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 멤리스터[^emerging][^p2][^p3], 뉴로모픽 소자[^prof][^p3][^p5], 메모리 반도체 소자[^prof][^p1], 메모리 내 연산[^emerging][^p7], AI 반도체·가속기[^integrated][^applications], 하드웨어 보안[^applications][^p8]
- 홈페이지: <https://shinhyunlab.kaist.ac.kr>
- 근거와 출처: [ENTIS 근거 페이지](shinhyunlab-sources.md)

> 전기 신호의 이력을 기억하는 멤리스터 같은 새 반도체 소자를 직접 설계·제작하고, 이 소자로 뇌의 신경세포와 시냅스를 흉내 내 적은 에너지로 인공지능 계산을 하는 칩과 시스템을 만드는 연구실이다.[^emerging][^integrated]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 최신현 교수가 이끄는 연구실이다.[^prof][^home] 누리집은 이름을 Emerging Nanoelectronic Technology and Integrated Systems Laboratory(ENTIS)로 적고, 반도체공학대학원과 반도체시스템공학과의 연구실 목록은 국문 이름을 「신경망 모사 소자 및 회로 개발 연구실」로 적는다.[^home][^semicon][^sse] 반도체공학대학원 목록은 연구 분야를 "차세대 메모리/지능형 컴퓨팅 소자 및 통합 시스템 개발"로, 반도체시스템공학과 목록은 "차세대 뉴로모픽 컴퓨팅 디바이스 소자 및 회로"로 적는다.[^semicon][^sse] 연구실 소식은 ENTIS가 2018년 12월 KAIST 전기및전자공학부에서 시작했다고 적는다.[^news]

Research Areas 페이지는 연구를 세 영역으로 나눈다. Emerging Devices에는 생체 모방 멤리스터 소자, 상변화 메모리(물질의 상태가 바뀌며 저항이 달라지는 것으로 정보를 저장하는 메모리) 소자, 계면형 멤리스터, FET(전계효과 트랜지스터, 게이트 전압으로 전류의 흐름을 조절하는 트랜지스터) 기반 계산 소자, 신뢰성 높은 멤리스터를, Integrated Systems에는 멤리스터 기반 시스템 통합, 멤리스터 배열의 병렬 계산 시스템, 설계와 하드웨어 구현, 멤리스터와 CMOS(n형과 p형 두 종류의 트랜지스터를 짝지어 회로를 만드는 기술로, 오늘날 반도체 칩의 기본이 되는 소자 기술)의 공동 집적을, Applications에는 신경망, 뉴로모픽 컴퓨팅, 하드웨어 보안을 올린다.[^areas] 연구실은 새로운 나노전자 소자를 설계하고 만들고 평가한다. 대상은 단자가 둘인 소자(멤리스터, 곧 저항 변화 소자로 RRAM(저항 변화 메모리)·PCM(상변화 메모리)·계면형 소자 등), 단자가 셋인 전계효과 트랜지스터(FET) 기반 소자, 그리고 이 소자들을 빽빽하게 모아 병렬로 동작시키는 배열 집적이다.[^emerging] 멤리스터는 걸린 전압의 이력에 따라 저항이 바뀌고 그 상태를 기억하는 소자다. 연구실은 무어의 법칙(반도체 칩에 넣는 트랜지스터 수가 꾸준히 늘어 왔다는 경험칙)이 한계에 다가가 새로운 계산 소자가 필요해졌고, 인공지능이 빠르게 커지며 막대한 변수와 계산 능력을 쓰게 되어 폰 노이만 구조(계산 장치와 기억 장치가 나뉘어 데이터를 주고받는 기존 컴퓨터 구조) 이후의 구조로 옮겨 가고 있다고 설명한다. 새 소자로 만든 뉴로모픽 컴퓨팅(뇌의 신경세포와 시냅스 동작을 흉내 내 계산하는 방식) 시스템은 훨씬 적은 에너지와 적은 데이터 이동으로 인공지능 계산을 할 수 있어 유력한 후보로 주목받는다고 적는다.[^emerging]

연구실이 짚는 문제는 신뢰성이다. 기존의 새 소자들은 동작 원리가 제어되지 않고 확률적이어서 소자마다, 그리고 동작할 때마다 특성이 달라지고, 일부 소자는 칩 위에 배선층을 쌓는 후공정(BEOL)에 맞추기 어려워 높은 밀도로 세로로 쌓기 힘들다. 연구실은 CMOS와 호환되는 소재와 공정으로 고르고 믿을 수 있게 저항이 바뀌는 소자를 만드는 전략을 개발하고 있으며, 스파이킹 신경망(신경세포처럼 짧은 전기 신호로 정보를 주고받는 인공 신경망)과 확률 컴퓨팅(무작위성을 계산에 이용하는 방식) 같은 다음 세대 인공지능을 위한 소자도 설계한다. 연구는 새 소자 제작, 통합 시스템 개발, 소자와 시스템을 쓰는 응용 개발의 세 갈래에 초점을 둔다고 적는다.[^emerging]

통합 시스템 쪽에서 연구실은 CMOS로 만든 인공지능 전용 칩(ASIC)에도 통신 병목, 에너지 소비, 온라인 학습(기기를 쓰는 중에 계속 배우는 일) 능력의 한계가 남아 있다고 보고, 연구실이 개발한 인공 시냅스(주로 멤리스터)로 대규모 뉴로모픽 인공지능 하드웨어를 만드는 것을 목표로 든다. 입력 센서에서 계산 장치까지 지능형 시스템을 통합하고, 인공 뉴런에서 인공 시냅스까지 모두 갖춘 시스템을 시연하며, 디지털·아날로그 주변 회로와 제어기 같은 하드웨어와 인공지능 소프트웨어까지 함께 설계하는 새 소자 기반 도메인 특화 구조(DSA, 특정 종류의 계산에 맞춰 설계한 칩 구조)를 연구한다.[^integrated] 응용 쪽에서는 이 구조를 여러 인공지능 응용의 가속기나 처리 장치로 쓰고, 영상 처리, 순서가 있는 데이터 분석, 보안, 의료 진단 같은 응용에 맞춰 소자의 정확도·발열·전력을 실험과 시뮬레이션으로 분석한다.[^applications]

대표 논문으로 보면 연구는 네 갈래로 모인다. 첫째, 정보를 지울 때의 전류를 크게 줄인 상변화 메모리와 도핑으로 균일성을 높인 멤리스터처럼 믿을 수 있는 소자를 만든다(대표 논문 1, 2).[^p1][^p2] 둘째, 멤리스터로 신경세포와 감각 신경의 동작을 흉내 내고, 로봇 팔이 익숙한 자극은 무시하고 위협적인 자극에는 민감하게 반응하게 한다(대표 논문 3, 4).[^p3][^p4] 셋째, 단자가 셋인 트랜지스터형 시냅스와 시간 반응을 조절할 수 있는 멤트랜지스터 배열을 만든다(대표 논문 5, 6).[^p5][^p6] 넷째, 멤리스터 배열과 주변 회로로 실시간 영상 처리를 하는 아날로그 계산 플랫폼과 칩 인증용 보안 기술을 만든다(대표 논문 7, 8).[^p7][^p8] 최근 논문 목록에는 문턱값 감지 기능을 지닌 멤리스터 기반 전기화학 바이오센서 신호 변환 소자, 하드웨어로 가속하는 인공지능 모델 학습·추론을 위한 새 메모리·소자 기술, KAIST의 반도체 연구와 교육을 소개한 글도 있다.[^pubs]

## 주요 연구 주제

### 1. 균일하고 믿을 수 있는 멤리스터·상변화 메모리 소자

상변화가 가능한 나노 필라멘트로 리셋 전류를 줄인 상변화 메모리, 플루오린 도핑으로 편차를 줄이고 스위칭을 빠르게 한 산화타이타늄 멤리스터.[^p1][^p2] 대표 논문 1, 2.

### 2. 뉴런·감각 신경을 흉내 내는 동적 소자

트랜지스터 없이 멤리스터만으로 엮은 배열의 인공 뉴런과 순차 데이터 처리, 습관화·민감화 성질을 지닌 3차 멤리스터로 만든 로봇의 인공 감각 신경계.[^p3][^p4] 대표 논문 3, 4.

### 3. 트랜지스터형 시냅스와 멤트랜지스터 배열

열전자 방출로 가중치를 고르게 바꾸는 게이트 주입 방식 시냅스 트랜지스터, 시간 반응을 프로그래밍할 수 있는 멤트랜지스터로 만든 저수지 컴퓨팅.[^p5][^p6] 대표 논문 5, 6.

### 4. 멤리스터 배열로 만드는 계산 시스템과 응용

선택 소자 없는 아날로그 멤리스터 배열로 스스로 보정하며 실시간 영상을 처리하는 플랫폼, 멤리스터 배열과 딥러닝을 결합한 물리적 복제 방지 기능(PUF).[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 최신현 교수가 마지막 저자이고 랩 목록이 교수 이름에 ** 표시를 붙인 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Phase-change memory via a phase-changeable self-confined nano-filament](https://doi.org/10.1038/s41586-024-07230-5) · Nature | 상변화 메모리(PCM, 물질이 결정 상태와 비정질 상태 사이를 오가며 저항이 달라지는 것으로 정보를 저장하는 메모리)는 지연이 짧고 전원이 꺼져도 정보가 남으며 집적도가 높아, 계산 장치와 메모리 사이의 병목(폰 노이만 병목)을 풀 후보로 여겨져 왔다. 그러나 정보를 지우는 리셋 과정에서 상변화 물질을 녹여 비정질로 만들어야 해 큰 전류가 들고 에너지 효율이 떨어진다. 소자 크기를 줄여 동작 전류를 낮추려는 연구는 제작비를 올리면서도 리셋 전류를 줄이는 데 한계가 있었다. 상변화가 가능한 SiTeₓ 나노 필라멘트(나노미터 단위 굵기의 실 모양 구조)를 만들어 리셋 전류를 줄인 소자를 보였다. 제작비를 늘리지 않고도 리셋 전류가 약 10 μA로, 크기를 크게 줄인 기존 PCM보다 약 한두 자릿수 작았다. 켜짐·꺼짐 저항비가 크고 빠르며 편차가 작고 여러 단계의 값을 저장하는 성질도 유지했다. 뉴로모픽 컴퓨팅, 엣지 프로세서(데이터가 생기는 기기 가까이에서 계산하는 처리 장치), 메모리 내 연산, 기존 메모리 응용으로 가는 중요한 걸음이라고 보았다.[^p1] | 공동 1저자 S.-O. Park·S. Hong, 마지막 저자 최신현(**) |
| 2 | 2024 | [Tunable ion energy barrier modulation through aliovalent halide doping for reliable and dynamic memristive neuromorphic systems](https://doi.org/10.1126/sciadv.adm7221) · Science Advances | 멤리스터로 하는 뉴로모픽 컴퓨팅은 전력을 적게 쓰고 빠른 계산 방식으로 떠올랐지만, 이온이 무작위로 움직여 생기는 신뢰성 문제 때문에 상용화가 어렵다. 원자가가 다른 할로젠 원소를 넣는 도핑(소재에 다른 원소를 조금 섞어 성질을 바꾸는 일)으로 멤리스터의 균일성과 성능을 높이는 방법을 제안했다. 동적 TiO₂₋ₓ 멤리스터에 플루오린을 넣자 소자 사이의 편차가 줄고, 저항이 바뀌는 스위칭 속도가 빨라지며 스위칭 폭이 넓어졌다. 비정질 TiO₂₋ₓ의 원자 단위 시뮬레이션에서는 플루오린 이온이 산소 빈자리(산소 원자가 빠진 자리)를 끌어당겨, 빈자리가 되돌릴 수 있게 다시 배치되고 고르게 퍼지게 했다. 여러 번의 이동 장벽 계산은 플루오린 이온이 가까운 산소 빈자리의 이동 에너지도 낮춰 이온 확산과 빠른 스위칭을 돕는다는 것을 통계적으로 보여 주었다. 보로노이 부피 분석(원자마다 차지하는 공간을 나눠 재는 분석)은 움직이는 이온 사이의 정전기적 반발과 이동 장벽의 관점에서 설계 원리를 제시했다.[^p2] | 공동 1저자 J. Bae·C. Kwon, ** 표시 S. Kim·최신현(마지막 저자) |
| 3 | 2022 | [Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing](https://doi.org/10.1038/s41467-022-30539-6) · Nature Communications | 뉴로모픽 컴퓨팅은 뇌의 신경세포(뉴런) 동작을 그대로 흉내 내 정보를 처리한다. 멤리스터로 만든 인공 뉴런은 구조가 단순하고 에너지 효율이 높으며 작게 만들기 좋지만, 멤리스터의 신뢰성 문제가 큰 걸림돌이었다. 소자마다 트랜지스터를 달지 않고 멤리스터만으로 엮은 1R 크로스바 배열(가로세로 전선이 만나는 자리마다 소자를 둔 격자형 배열)을 만들었는데, 편차가 작고 수율이 100%이며 동적 범위가 넓고 빨랐다. 이 멤리스터로 입력을 쌓다가 일정 수준을 넘으면 신호를 내보내고 쌓인 값이 시간이 지나며 새어 나가는 성질(leaky-integrate-and-fire)을 가진 뉴런을 신뢰성 있게 구현했다. 또 이 멤리스터의 단기 기억 효과로 순서가 있는 데이터를 효율적으로 처리하는 계산 시스템을 만들어, 적은 수의 학습 변수로 생의학 순차 데이터인 항균 펩타이드(세균을 죽이는 짧은 단백질 조각) 서열을 학습하고 생성했다. 에너지 효율이 높은 엣지 컴퓨팅 기기에 필요한 멤리스터 인공 뉴런과 뉴로모픽 시스템의 가능성을 열었다고 보았다.[^p3] | 공동 1저자 S.-O. Park·H. Jeong·J. Park, 마지막 저자 최신현(**) |
| 4 | 2025 | [Experimental demonstration of third-order memristor-based artificial sensory nervous system for neuro-inspired robotics](https://doi.org/10.1038/s41467-025-60818-x) · Nature Communications | 동물의 감각 신경계는 바깥 자극을 알아차리게 한다. 자극에 효율적으로 반응하는 신경 모방 로봇을 만들려고 인공 감각 신경계가 많이 연구됐지만, 덩치 큰 주변 회로 없이 습관화(익숙한 자극에 점점 덜 반응하는 성질)와 민감화(중요한 자극에 더 크게 반응하는 성질) 같은 정교한 생물 기능을 갖추기는 어려웠다. 스위칭 복잡도가 3차인 멤리스터로, 습관화와 민감화 성질을 스스로 지닌 인공 시냅스를 흉내 냈다. HfO₂ 멤리스터에 저항이 바뀌는 TiOₓ 층을 하나 더 넣자 3차 스위칭 복잡도와 전원이 꺼져도 남는 습관화 특성이 나타났다. 이 멤리스터로 만든 인공 감각 신경계를 단 로봇 시스템을 제안해, 프로세서의 도움 없이 바깥 자극에 대한 로봇 팔의 반응을 최적화했다. 실험에서 이 로봇 팔은 안전하고 익숙한 자극의 약 71%를 무시하면서 위협적이고 중요한 자극에는 민감하게 반응해, 생물 감각 신경계의 습관화·민감화와 비슷하게 움직였다. 하드웨어 부담을 줄인 에너지 효율적이고 지능적인 로봇 시스템의 디딤돌이 될 수 있다고 보았다.[^p4] | 1저자 S.-O. Park, ** 표시 J. Lee·최신현(마지막 저자) |
| 5 | 2022 | [The gate injection-based field-effect synapse transistor with linear conductance update for online training](https://doi.org/10.1038/s41467-022-34178-9) · Nature Communications | 폰 노이만 구조를 대신할 뉴로모픽 컴퓨팅에는 데이터를 같은 자리에서 저장하고 계산하는 시냅스 소자가 필요하다. 단자가 셋인 시냅스 소자는 안정적이고 조절하기 쉬워 주목받지만, 가중치(시냅스 연결의 세기)를 바꿀 때 변화가 고르지 않고 동적 범위가 좁으며 기존 CMOS 시스템과 맞지 않아 큰 크로스바 배열로 키우기 어렵다고 알려져 왔다. 열전자 방출(열에너지를 얻은 전자가 에너지 장벽을 넘어가는 현상)을 이용해 전도도가 고르게(선형으로) 바뀌도록 한, CMOS와 호환되는 게이트 주입 방식 전계효과 트랜지스터를 제안했다. 게이트 층 사이에 계면층을 넣어 선형성이 전도 원리에 따라 어떻게 달라지는지 살폈고, 전도 원리를 확인하려고 온도를 바꿔 가며 게이트 전류를 쟀다. 열전자 방출에 바탕한 소자는 뛰어난 시냅스 특성을 보였고, 인공 신경망 시뮬레이션에서 MNIST(손글씨 숫자 그림 데이터셋) 인식 정확도 93.17%를 얻었다.[^p5] | 공동 1저자 S. Seo·B. Kim·D. Kim·S. Park, 마지막 저자 최신현(**) |
| 6 | 2026 | [Programmable memtransistor array with temporal dynamics modulation for efficient time-series data processing](https://doi.org/10.1038/s41467-026-75211-5) · Nature Communications | 하드웨어로 만든 저수지 컴퓨팅(입력을 시간에 따라 반응이 변하는 물리 시스템에 넣고 그 반응만 학습해 시계열을 처리하는 방식)은 시계열 데이터를 에너지 효율적으로 처리할 수 있다. 그러나 하드웨어 수준에서 시간 반응을 조절할 수 없어 여러 시간 규모의 특징을 뽑고 계산 용량을 키우는 데 한계가 있었다. 게이트 층이 두 가지 기능을 하는 프로그래밍 가능한 동적 멤트랜지스터(기억 성질을 지닌 트랜지스터)를 만들어, 계속 전압을 걸거나 입력을 미리 손보지 않고도 하드웨어 수준에서 동작을 조절했다. 이 소자는 시간에 따른 처리를 맡는 휘발성 전하 저장층과, 띠 구조(전자가 가질 수 있는 에너지 범위의 배치)를 비휘발성으로 바꾸는 전하 포획층을 함께 담아 이완 시간 상수(자극이 멈춘 뒤 상태가 원래대로 돌아가는 빠르기를 나타내는 값)를 5배 범위에서 조절했다. 서로 다른 시간 반응을 가진 멤트랜지스터를 나란히 묶어 여러 시간 규모의 신호를 처리하는 넓은 저수지 컴퓨팅 시스템을 구현했다. 여러 진동이 겹친 신호의 예측 과제에서 저수지 하나만 쓴 기준보다 오차를 40분의 1로 줄였고, 혼돈 운동을 보이는 로렌츠 끌개의 예측에서 소프트웨어에 견줄 만한 정확도를 얻었다.[^p6] | 1저자 D.-w. Kim, 마지막 저자 최신현(**) |
| 7 | 2025 | [Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array](https://doi.org/10.1038/s41928-024-01318-6) · Nature Electronics | 멤리스터 기반 플랫폼은 아날로그 영역에서 병렬로 계산할 수 있어 작고 에너지 효율적인 인공지능 엣지 컴퓨팅 시스템을 만드는 데 쓰일 수 있다. 그러나 멤리스터 배열 시스템은 낮은 수율, 나쁜 균일성, 내구성 같은 신뢰성 문제 때문에 학습까지 기기 안에서 모두 하는 실시간 인공지능 알고리즘을 구현하기 어렵다. 선택 소자(배열에서 원하는 소자만 고르도록 따로 붙이는 소자) 없이 멤리스터만으로 이뤄진 아날로그 멤리스터 배열에 바탕한 아날로그 계산 플랫폼을 보고했다. 산소 분포가 점진적인 계면형 산화타이타늄 멤리스터를 썼는데, 신뢰성과 선형성이 높고, 처음 쓰기 전의 형성 과정(높은 전압으로 전도 통로를 처음 만드는 과정)이 필요 없으며, 스스로 한쪽 방향으로만 전류를 잘 흘리는(자기 정류) 성질을 보였다. 1K(32×32) 크로스바 배열, 주변 회로, 디지털 제어기로 이뤄진 플랫폼은 보상 동작이나 사전 학습 없이 스스로 보정하며 아날로그 영역에서 인공지능 알고리즘을 돌린다. 실시간 영상에서 전경과 배경을 나누는 작업에서 평균 최대 신호 대 잡음비 30.49 dB와 구조적 유사도 지수 0.81을 얻었고, 이는 이상적인 경우의 시뮬레이션 값과 비슷했다.[^p7] | 공동 1저자 H. Jeong·S. Han, ** 표시 Y. Yoon·최신현(마지막 저자) |
| 8 | 2021 | [Neural Network Physically Unclonable Function: A Trainable Physically Unclonable Function System with Unassailability against Deep Learning Attacks Using Memristor Array](https://doi.org/10.1002/aisy.202100111) · Advanced Intelligent Systems | 엣지 기기가 널리 퍼지면서 개인정보 보호와 칩 인증을 위한 보안 기본 요소가 새로 필요해졌다. 멤리스터는 본래 지닌 무작위성과 확률적 성질 때문에 하드웨어 기반 보안 요소의 엔트로피(예측할 수 없는 무작위성) 원천으로 유망하다. 딥러닝 알고리즘을 활용하는 새로운 물리적 복제 방지 기능(PUF, 칩마다 제조 과정의 미세한 차이로 생기는 고유한 응답을 지문처럼 쓰는 보안 기술) 설계인 신경망 PUF(NNPUF)를 제안했다. 멤리스터 배열과 결합한 이 설계는 쓰기 동작의 정확도에 의존하지 않아 쉽게 만들 수 있다. 학습에서 미분할 수 없는 모듈을 다루려고 'PUF 손실'이라는 새 손실 개념을 고안했고, 이 손실로 가중치를 되풀이해 갱신하면 NNPUF가 최적 성능에 이른다. 균일성, 확산성, 고유성 같은 보안 지표에서 이상값에 가까운 평균 50%를 얻어 보안 요소의 실용 품질 기준을 충족했고, 딥러닝 기반 모델링 공격에 대해 예측 모델의 정확도가 50% 가까이에 머물러 공격을 견딘다는 것을 보였다.[^p8] | 1저자 J. Park, 마지막 저자 최신현(**) |

## 교수와 전문 분야

최신현 교수는 KAIST 전기및전자공학부 부교수(Associate Professor)이고, 누리집 교수 소개는 KAIST Endowed Chair Professor라는 직함도 함께 적는다.[^prof] 교수 소개에 따르면 교수의 연구는 (1) 저항 변화 소자를 이용한 새로운 메모리·계산 소자 개발, (2) 이를 엣지 컴퓨팅·뉴로모픽 컴퓨팅·메모리 기능 같은 통합 시스템에 적용하는 일, (3) 단자가 셋인 기존 트랜지스터형 메모리 소자의 새로운 동작 원리 개발에 초점을 둔다.[^prof] 반도체공학대학원 연구 페이지는 교수의 연구실을 「차세대 반도체 소자」 칸에, 반도체시스템공학과 연구실 목록은 「반도체 소자 및 공정」 칸에 올린다.[^semicon][^sse]

교수는 2009년 서울대학교에서 전기공학 학사를 최우등(Summa Cum Laude)으로 받았고, 미국 미시간대학교 앤아버(University of Michigan, Ann Arbor)에서 전기공학 석사(2011)와 박사(2015)를 받았다. 2015–2018년 MIT(Massachusetts Institute of Technology)에서 Postdoctoral Associate로 일했다.[^prof] 교수 소개는 교수가 저항 변화 소자의 기초 원리 이해와 뉴로모픽 응용을 연구해 왔고, Nature, Nature Electronics, Nature Materials, Nature Communications, Science Advances, Nano Letters, ACS Nano 등에 논문을 냈으며, 연구가 Nature 표지에 실리고 Nature News & Views, Nature Materials News & Views, Nature Nanotechnology Research Highlights에 소개됐다고 적는다.[^prof] 랩 Publications 페이지의 2019년 이전 목록(2012–2018년, 교수가 KAIST에 오기 전의 논문)에는 멤리스터 네트워크로 데이터를 군집화하거나 특징을 뽑은 실험(Scientific Reports 2015, Nano Letters 2017), 산화물 멤리스터의 동적 저항 변화 모델(ACS Nano 2014)과 금속 산화물 저항 변화 메모리의 정보 유지 실패 분석(Applied Physics Letters 2014), SiGe 에피택시(결정 위에 같은 방향으로 결정층을 키우는 성장) 층으로 만든 뉴로모픽 메모리(Nature Materials 2018)가 있다.[^pubs]

교수 소개는 교수의 연구가 2022년 KAIST 공과대학의 breakthrough research로 뽑혔고, 교수가 2020년 Hae-Dong Young Engineer Award를 받았으며, 2024년 KAIST Endowed Chair Professor로 임명되고 KAIST Q-day Faculty Excellence Award(연구 부문)를 받았고, 연구가 14th KAIST Leading-edge Technology Achievements의 하나로 선정됐다고 적는다.[^prof] 랩 Awards 페이지에 따르면 교수는 2025년 현우 KAIST 학술상을 받았고, 교수 연구진의 나노 필라멘트 상변화 메모리 연구(대표 논문 1)는 2025 대한민국 우수성과 100선(Top 100 National R&D Achievements 2025)에 선정됐다.[^awards]

논문으로 보면 전문 분야는 네 갈래다. 첫째, 상변화 메모리와 멤리스터의 동작 전류·균일성·신뢰성을 소재와 구조로 개선하는 소자 연구다(대표 논문 1, 2).[^p1][^p2] 둘째, 멤리스터의 시간에 따른 동작으로 신경세포와 감각 신경을 흉내 내는 연구다(대표 논문 3, 4).[^p3][^p4] 셋째, 단자가 셋인 트랜지스터형 시냅스와 멤트랜지스터의 동작 원리 연구다(대표 논문 5, 6).[^p5][^p6] 넷째, 멤리스터 배열을 주변 회로·알고리즘과 묶은 계산 시스템과 보안 응용이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

연구실은 개발한 소자를 계산 장치로 쓰는 범위를 넓히고 있으며, 새 소자 기반 도메인 특화 구조를 인공지능이 필요한 여러 응용의 가속기나 처리 장치로 쓸 수 있다고 적는다. 응용 분야로는 영상 처리, 순서가 있는 데이터 분석, 보안, 의료 진단을 든다.[^applications] 연구실의 새 소자는 뉴로모픽 컴퓨팅 하드웨어, 차세대 메모리 셀, 논리 회로, 보안 응용의 후보로 주목받았고, 소자의 기억 성질은 많은 데이터를 효율적으로 저장하고 병렬로 쓰고 읽는 시스템을 가능하게 하며, 높은 밀도, 낮은 전력 소비, 긴 반복 수명, 1나노초보다 짧은 스위칭 속도도 보였다고 설명한다.[^emerging]

대표 논문들은 나노 필라멘트 상변화 메모리가 뉴로모픽 컴퓨팅, 엣지 프로세서, 메모리 내 연산과 기존 메모리 응용으로 가는 걸음이고,[^p1] 멤리스터 인공 감각 신경계가 하드웨어 부담을 줄인 지능형 로봇 시스템의 디딤돌이 될 수 있으며,[^p4] 멤리스터 배열 기반 PUF가 엣지 기기의 개인정보 보호와 칩 인증에 쓰일 보안 요소의 품질 기준을 충족한다고 보았다.[^p8] 연구실 소식은 대표 논문 1–5와 7이 여러 언론에 소개됐다고 적는다.[^news]

## 구성원

연구실 누리집 Members 메뉴의 Postdocs·Ph.D. Students·M.S. Students·Undergraduates 페이지에 실린 25명이다.[^members] 과정과 괄호 안의 표기는 각 페이지의 표기를 따랐고, 연구 주제 칸은 각자의 Research Interest 칸이다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 박시온(See-On Park) | 박사후연구원 (25, Fall) | Highly Reliable and Linear Memristor Device; Bio-Inspired Learning with Memristor Device; Memristor-Based AI Chip for Edge Computing | 526zion3@kaist.ac.kr | 1, 2, 3, 4, 5, 6, 7 |
| 정학천(Hakcheon Jeong) | 박사후연구원 (26, Spring) | Neuromorphic Computing Using Memristor Devices; Hardware Implementation of Memristor-based System; Memristor-based System Design; Next Generation Memristor Devices | jhch0818@kaist.ac.kr | 1, 2, 3, 4, 5, 7, 8 |
| Seokho Seo | 박사과정 (23, Spring) | Next-generation Neuromorphic Devices; Advanced Three-terminal Memory; Reliability Engineering of RRAM & PCM; CMOS-Memristor Co-integration for Computing-in-Memory | ssho6941@kaist.ac.kr | 1, 4, 5, 6, 7 |
| Dae-won Kim (Lab Chief) | 박사과정 (23, Fall) | Next Generation Memristor Devices; In memory computing based on New memory | dwk1996@kaist.ac.kr | 6 |
| Chaebin Park | 박사과정 (23, Fall) | Chalcogenide-based Selector Devices; Novel Computing with Emerging Devices | coqlswkd@kaist.ac.kr | 6 |
| Taehwan Jang | 박사과정 (24, Spring) | Next Generation Memristor Devices; Integrated system development | noel358@kaist.ac.kr | 2, 6, 7 |
| 조윤호(Yoonho Cho) | 박사과정 (24, Spring) | Next Generation Memristor Devices; Integrated system development | chyn1808@kaist.ac.kr | 2, 6, 7 |
| 김유진(Yujin Kim) | 박사과정 (24, Fall, KEPSI) | Next Generation Memristor Devices; Integrated system development | yujindenny@kaist.ac.kr | 6 |
| 배종민(Jongmin Bae) | 박사과정 (24, Fall) | Novel Memristor Devices and Mechanisms; Memristive Integrated Systems; Computing-in-memory based on Conventional Memories | tombssts@kaist.ac.kr | 2, 3, 7 |
| Da-Won Kim | 석박사통합과정 (25, Spring) | Novel Memristor Devices; Memristor-based Artificial Neural Network System; Resistive Switching Mechanism | dafish@kaist.ac.kr | 1 |
| Jung-Heum Na | 박사과정 (26, Spring) | RRAM-Based Neuromorphic Computing | kmi8316@kaist.ac.kr |  |
| Hyowoong Yi | 박사과정 (26, Fall) | Memristor-based Probabilistic Computing; Analog Memory for Compute-in-Memory | gydnd001220@kaist.ac.kr |  |
| Jihun Kang | 석사과정 (24, Spring, V-KEPSI) | RRAM-Based Neuromorphic Computing |  |  |
| Jeonghong Lee | 석사과정 (25, Spring) | Next Generation Memristor Devices; Memristor-based System Design | byj04097@kaist.ac.kr |  |
| Taeho Yun | 석사과정 (25, Spring) | Next Generation Memristor Devices; Chalcogenide-based Memory Devices | yth09041@kaist.ac.kr |  |
| Yu-Won Jeong | 석사과정 (25, Spring, 군학 프로그램) | Application of Neuromorphic Devices in the Military Operations | therightroad@kaist.ac.kr |  |
| Min-Hyeok Kim | 석사과정 (25, Fall) | Next Generation Memristor Devices | rbam01@kaist.ac.kr |  |
| Dong-Yeop Lee | 석사과정 (25, Fall) | Next Generation Memristor Devices | yy07121212@kaist.ac.kr |  |
| Won-Gyun Park | 석사과정 (26, Spring) | Next Generation Memristor Devices; RRAM-Based Neuromorphic Computing | wongyun@kaist.ac.kr |  |
| Dong-Yun Jung | 석사과정 (26, Spring) | Next Generation Memristor Devices; RRAM-Based Neuromorphic Computing | dongyun@kaist.ac.kr |  |
| Chang-Min Hong | 석사과정 (26, Spring) | Next Generation Memristor Devices; RRAM-Based Neuromorphic Computing | changmin2000@kaist.ac.kr |  |
| Seong-Woo Kim | 석사과정 (26, Fall) | Next Generation Memristor Devices; RRAM-Based Neuromorphic Computing | kimsw6224@kaist.ac.kr |  |
| Woobeen Oh | 학부 연구생 | Next Generation Memristor Devices | paul3399@kaist.ac.kr |  |
| Yubin Yun | 학부 연구생 | Next Generation Memristor Devices | yb_yun@kaist.ac.kr |  |
| Dongcheol Shin | 학부 연구생 | Next Generation Memristor Devices | shindong0216@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지에 실린 10명(박사 1, 석사 9)이다. 학위와 진로는 누리집 표기 그대로이고, 학위 옆의 EPSS도 누리집 표기다. Ju-Yeon Kim은 진로 칸이 없다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Taehoon Park | 박사 (Ph.D.) | KIST |
| Tae-Ryong Kim | 석사 (M.S.) | Purdue University |
| Beom-Jin Kim | 석사 (M.S.) | Samsung Electronics |
| Sang-Hyun Choi | 석사 (M.S.) | Samsung Electronics |
| Yoon-Ji Lee | 석사 (M.S.) | Samsung Electronics |
| Jong-Yong Park | 석사 (M.S. EPSS) | Samsung Electronics |
| Dong-Hoon Kim | 석사 (M.S. EPSS) | Samsung Electronics |
| Seung-Woo Park | 석사 (M.S. EPSS) | Samsung Electronics |
| Hyun-Jun Jeong | 석사 (M.S.) | Samsung Electronics |
| Ju-Yeon Kim | 석사 (M.S.) |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021–2026년 논문 25편이다. 제목·저자·학술지 표기는 랩 표기 그대로이고, 저자 이름 뒤의 *는 누리집이 같은 기여(Equally contributed)로 설명한 표시다.[^pubs]

**2026**

- S.-W. Lee\*, S. Seo\*, H. Jeong\*, J.-K. Han\*, Y. Kim, D. Yoo, J.-H. Son, J.-M Yu, S. Choi\*\*, and Y.-K. Choi\*\*. "Array of Cointegrated Transistor-Based Artificial Neurons and Synapses for Neuromorphic Computing". *Small, e74638 (2026)*.
- D.-w. Kim\*, Y. Cho, S. Seo, Y. Kim, S. Park, T. Jang, C. Park, Y. Oh, J. Lee, and S. Choi\*\*. "Programmable memtransistor array with temporal dynamics modulation for efficient time-series data processing". *Nature Communications 17, 8311 (2026)*.
- Y. Cho\*, D. Kim, J. Lee, D.-w. Kim, S. Park, J. Bae, T. Jang, and S. Choi\*\*. "Tunable dynamics via dual-ion modulation for event-based data processing using a highly uniform and self-rectifying memristor array". *Advanced Science 13, e75594 (2026)*.
- Y. Cho\*, D.-w. Kim\*, Y. Kim\*, J. Na, Y. Jeong, D. Lee, and S. Choi\*\*. "Emerging memory and device technologies for hardware-accelerated model training and inference". *Advanced Electronic Materials, e00796 (2026)*.

**2025**

- Y. Kim\*, Y. Kwon\*, Y. Yoo\*, K. Theyagarajan, S. Saikrithika, A. Lee, N. Bae, W. Lee, G. Sim, Y. Lee, S. Park, H. Cho, M. Kang, Y. Kim, Y. Park, K. Lee, C. Kim, H. Ko, W. Sul, S. Lee, J. Ahn, S. Choi\*\*, K. Kim\*\*  & J. Lee\*\*. "Demonstration of CMOS-compatible memristor-based electrochemical biosensor transducer with threshold-sensing functionality". *Nature Communications 16, 10851 (2025)*.
- K. Kim\*\*, Y. Yoon\*\*, S. Choi\*\*, S. Choi\*\*, and S. Yoo\*\*. "Semiconductor-related research and education at KAIST". *Nature Reviews Electrical Engineering (2025)*.
- S. Park, H. Jeong, S. Seo, Y. Kwon, J. Lee\*\*, and S. Choi\*\*. "Experimental demonstration of third-order memristor-based artificial sensory nervous system for neuro-inspired robotics". *Nature Communications 16, 5754 (2025)*.
- J. Lee\* , S. Park\* , S. Yun\* , Y. Kim, H. Myung, S. Choi\*\*, and Y. Choi\*\*. "Decoupling strategy to separate training and inference with three-dimensional neuromorphic hardware composed of neurons and hybrid synapses". *ACS Nano 19, 13063–13072 (2025)*.
- H. Jeong\*, S. Han\*, S. Park, T. Kim, J. Bae, T. Jang, Y. Cho, S. Seo, H. Jeong, S. Park, T. Park, J. Oh, J. Park, K. Koh, K. Kim, D. Jeon, I. Kwon, Y. Yoon\*\*, S. Choi\*\*. "Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array". *Nature Electronics 8, 168–178 (2025)*.

**2024**

- J. Bae\*, C. Kwon\*, S. Park, H. Jeong, T. Park, T. Jang, Y. Cho, S. Kim\*\*, S. Choi\*\*. "Tunable ion energy barrier modulation through aliovalent halide doping for reliable and dynamic memristive neuromorphic systems". *Science Advances 10, eadm7221 (2024)*.
- T. Park\*, S. Seo, Y. Kim, S. Park, S. Choi, S. Hong, H. Jeong, S. Choi\*\*. "Ultra-Low Power and Reliable Dynamic Memtransistor Based on Charge Storage Junction FET with Step-Wise Potential Barrier for Energy-Efficient Edge Computing Framework". *Advanced Electronic Materials 10, e202300904 (2024)*.
- S. Park\*, S. Hong\*, S. Sung, D. Kim, S. Seo, H. Jeong, T. Park, W. Cho, J. Kim, S. Choi\*\*. "Phase-change memory via a phase-changeable self-confined nano-filament". *Nature 628, 293–298 (2024)*.
- S. Hong\*, S. Park, H. Jeong, T. Park, Y. Cho, T. Jang, S. Sung, H. Ahn, J. Lee, S. Choi\*\*. "Realization of Selector-Memory Bi-Functionality with Self-Current Regulation Utilizing Poly-Crystalline Based GST Electrolyte for Memristor Hardware Development". *Advanced Materials Interfaces 11, 2300975 (2024)*.

**2023**

- S. Park\*, T. Park, H.Jeong, S. Hong, S. Seo, Y. Kwon, J. Lee, S. Choi\*\*. "Linear Conductance Update Improvement of CMOS-Compatible Second-Order Memristors for Fast and Energy-Efficient Training of Neural Network Using a Memristor Crossbar Array". *Nanoscale Horizons 8, 1366–1376 (2023)*.
- M. Song\*, J. Kang\*, X. Zhang, W. Ji, A. Ascoli, I. Messaris, A. S. Demirkol, B. Dong, S. Aggarwal, W. Wan, S. Hong, S. G. Cardwell, I. Boybat,J. Seo, J. Lee, M. Lanza, H. Yeon, M. Onen, J. Li, B. Yildiz, J. del Alamo, S. Kim, S. Choi, G. Milano, C. Ricciardi, L. Alff, Y. Chai, Z. Wang,H. Bhaskaran, M. C. Hersam, D. Strukov, H.-S. P. Wong, I. Valov, B. Gao, H. Wu, R. Tetzlaff, A. Sebastian, W. Lu, L. Chua, J. Joshua Yang, J. Kim\*\*. "Recent Advances and Future Prospects for Memristive Materials, Devices and Systems". *ACS Nano 17, 11994–12039 (2023)*.
- T. Park\*, H.Jeong, S. Park, S. Hong, S. Seo, S. Park, S. Choi\*\*. "The Effect of Schottky Barrier Modulation on Conduction and Failure Mechanisms of an Ag/WOx/p-Si Based Memristor". *Journal of Applied Physics 133, 075701 (2023)*.
- G. Kim, S. Son, H. Song, J. Jeon, J. Lee, W. Cheong, S. Choi, K. Kim\*\*. "Retention Secured Nonlinear and Self-Rectifying Analog Charge Trap Memristor for Energy Efficient Neuromorphic Hardware". *Advanced Science 10, 2205654 (2023)*.

**2022**

- S. Seo\*, B.Kim\*, D. Kim\*, S. Park\*, T.R. Kim, J.Park, H.Jeong, S. Park, T. Park, H.Shin, M.Kim, Y. Choi, S. Choi\*\*. "The gate injection-based field-effect synapse transistor with linear conductance update for online training". *Nature Communications 13, 6431 (2022)*.
- S. Park\*, H. Jeong\*, J. Park\*, J.Bae, S. Choi\*\*. "Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing". *Nature Communications 13, 2888 (2022)*.
- S. Choi\*, S. Park\*, S. Seo, S. Choi\*\*. "Reliable multilevel memristive neuromorphic devices based on amorphous matrix via quasi-1D filament confinement and buffer layer". *Science Advances 8, eabj7866 (2022)*.
- M. Kim, J. Kim, G. Yun, J. Yu, J. Han, J. Lee, S, Seo, S. Choi, Y. Choi\*\*. "An Overturned Charge Injection Synaptic Transistor With a Floating-Gate for Neuromorphic Hardware Computing". *IEEE Electron Device Letters 43, 1489–1492 (2022)*.
- S. Hu, J. Kang, T. Kim, S. Lee, J. Park, I. Kim, J. Kim, J. Kwak, J. Park, G. Kim. S. Choi†, Y. Jeong†. "SPICE study of STDP characteristics in a drift and diffusive memristor-based synapse for neuromorphic". *IEEE Access 10, 6381–6392 (2022)*.
- Y. Jeong, H. Lee, J. Park, S. Lee, H. Jin, S. Park, H. Cho, S. Hong, T. Kim, K. Kim, S. Choi, S. Im\*\*. "Engineering MoSe2/MoS2 Heterojunction Traps in 2D Transistors for Multilevel Memory, Multiscale Display, and Synaptic Functions". *NPJ 2D Materials and Applications 6, 24 (2022)*.
- J. Jeong, S. Kim, J. Kim, D. Geum, D. Kim, E. Jo, H. Jeong, J. Park, J. Jang, S. Choi, I. Kwon\*\*, S. Kim\*\*. "Heterogeneous and Monolithic 3D Integration of III–V-Based Radio Frequency Devices on Si CMOS Circuits". *ACS Nano 16, 9031–9040 (2022)*.

**2021**

- J. Park, Y. Lee, H. Jeong, S. Choi\*\*. "Neural Network Physically Unclonable Function: A Trainable Physically Unclonable Function System with Unassailability against Deep Learning Attacks Using Memristor Array". *Advanced Intelligent Systems 3, 2100111 (2021)*.

## 수상

랩 Awards 페이지에 실린 24건 가운데 2022–2026년의 20건이다. 상 이름 뒤는 누리집의 국문 설명이고, 국문 설명이 없는 글은 받은 사람과 영문 설명을 적었다.[^awards]

- 2026-02-27 · Sejong Science Fellowship: 정학천 박사, 세종 과학 펠로우십 선정 (전국 200여명 선발)
- 2026-02-20 · Outstanding Paper Awards: 박시온 박사, KAIST 우수 논문상 수상
- 2026-02-11 · CoE PhD Dissertation Award: 정학천 박사, 박사학위 우수논문상 수상 (공과대학 25명 선정)
- 2026-01-30 · Outstanding Poster Awards: 김유진 & 조윤호 연구원, 한국반도체학술대회 현장우수포스터상 수상
- 2026-01-30 · Top 100 National R&D Achievements 2025: 최신현 교수님, 2025 대한민국 우수성과 100선 선정 (전국 100선 선정)
- 2025-12-12 · Best Poster Award: 정학천 연구원, 2025 ICAMD 우수 포스터상 수상
- 2025-07-16 · Kwanjeong Educational Foundation Scholarship: 배종민 연구원, 관정 국내장학생 선발
- 2025-04-30 · Hyeon-Woo KAIST Scholastic Award: 최신현 교수님, 현우 KAIST 학술상 수상 (연간 1인 선정)
- 2025-03-31 · Outstanding Research Award: 박시온 연구원, 전자과 연구실적 우수상 수상 (소자 디비전 1인 선정)
- 2025-03-12 · WONIK Next-generation Engineer Award: 박시온 연구원, 원익 차세대 공학도상 최우수상 수상
- 2025-02-25 · Jang Young Sil Fellow Excellence Track: 박시온 연구원, 장영실 펠로우 프로그램 선정 (전국 10여명 선정)
- 2024-12-30 · IPESK Next-Generation Engineering Researcher: 박시온 연구원, 정학천 연구원, IPESK 차세대 공학 연구자 선정
- 2024-12-05 · Q-Day Research Award: 최신현 교수님, KAIST Q-day 리서치 어워드 수상
- 2024-11-10 · Best Poster Award (Su-Jin Sung): She received the Best Poster Award from Memrisys 2024!
- 2024-07-23 · Young-Han Kim Global Leader Scholarship (See-On Park): He received Young-Han Kim Global Leader Scholarship!
- 2023-02-26 · The Top Honors (Jongmin Bae): He received the B.S. degree with top honors in the School of Materials Science and Engineering & Electrical Engineering from KAIST!
- 2023-02-21 · Grand Prix (Da-Won Kim): She received the Grand Prix for the Undergraduate Research Participation (URP) Program!
- 2023-02-17 · The Top Honors (1st place) (Soo-Bin Choi): She received the B.S. degree with top honors in the School of Organic & Nano Engineering from Hanyang University!
- 2022-08-25 · The Top Honors (1st place) (Hyun-Jun Jeong): He received the B.S. degree with top honors in the School of Electronic and Electrical Engineering from Sungkyunkwan University!
- 2022-08-25 · The Top Honors (1st place) (Su-Jin Sung): She received the B.S. degree with top honors in the School of Advanced Materials Science & Engineering from Sungkyunkwan University!

## 소식

랩 ENTIS News 게시판의 글 23건 전부다. 날짜는 게시판의 게시일이고, 제목 뒤는 글의 내용을 담은 첫 문장이다. 2024-09-30에는 2021–2022년 논문과 연구실 시작(2018년 12월)을 알리는 글을 포함해 10건이 한꺼번에 게시됐다.[^news]

- 2026-08-28 · Selected as Inside Front Cover: The paper "Tunable Dynamics via Dual-Ion Modulation for Event-based Data Processing Using a Highly Uniform and Self-Rectifying Memristor Array, Advanced Science" is selected as an inside front cover image!
- 2026-02-04 · Selected as Top 100 National R&D Achievements 2025: The paper "Phase-change memory via a phase-changeable self-confined nano-filament, Nature" was selected as Top 100 National R&D Achievements 2025 in Korea.
- 2025-08-19 · New Publication: The paper titled 〈Semiconductor-related research and education at KAIST〉 has been published in Nature Reviews Electrical Engineering.
- 2025-08-19 · Introduced to the media: The paper "Experimental demonstration of third-order memristor-based artificial sensory nervous system for neuro-inspired robotics, Nature Communications" has been introduced to various media.
- 2025-08-19 · Selected as KAIST Breakthroughs: The paper "Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array, Nature Electronics" is selected as KAIST Breakthroughs
- 2025-08-19 · Introduced to the media: The paper "Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array, Nature Electronics" has been introduced to various media.
- 2025-07-22 · New publication: The paper titled 〈Experimental demonstration of third-order memristor-based artificial sensory nervous system for neuro-inspired robotics 〉 has been published in Nature Communications!
- 2025-05-01 · Introduced to media: He was awarded "Hyeon-Woo KAIST Scholastic Award" and introduced to various media.
- 2025-01-16 · Introduced to the media: The paper "Phase-Change Memory via a Phase-Changeable Self-Confined Nano-Filament , Nature" has been introduced to various media.
- 2025-01-16 · Introduced to the media: The paper "Tunable ion energy barrier modulation through aliovalent halide doping for reliable and dynamic memristive neuromorphic systems, Science Advances" has been introduced to various media.
- 2025-01-08 · New Publication: The paper titled 〈Self-supervised video processing with self-calibration on an analogue computing platform based on a selector-less memristor array〉 has been published in Nature Electronics.
- 2024-12-15 · New publication: The paper titled 〈Tunable ion energy barrier modulation through aliovalent halide doping for reliable and dynamic memristive neuromorphic systems〉 has been published in Science Advances.
- 2024-10-07 · New Publication: The paper 〈Phase-change memory via a phasechangeable self-confined nano-filament, Nature〉 they engaged in published.
- 2024-09-30 · New Publication: The paper 〈Realization of Selector-Memory Bi-Functionality with Self-Current Regulation Utilizing Poly-Crystalline Based GST Electrolyte for Memristor Hardware Development, Advanced Materials Interfaces〉 He engaged in published.
- 2024-09-30 · Selected as featured image of Nature Communications: The paper "Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing, Nature Communications" is selected as featured image of Nature Communications
- 2024-09-30 · Featured in Nature Communications collection of Neuromorphic Hardware and Computing: The papers "The gate injection-based field-effect synapse transistor with linear conductance update for online training" and "Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing" are featured in Nature Communications collection of Neuromorphic Hardware and Computing. (https://www.nature.com/collections/jaidjgeceb)
- 2024-09-30 · Introduced to the media: The paper "The gate injection-based field-effect synapse transistor with linear conductance update for online training, Nature Communications" is introduced to various media
- 2024-09-30 · New Publication: The paper 〈The gate injection-based field-effect synapse transistor with linear conductance update for online training, Nature Communications〉 they engaged in published.
- 2024-09-30 · Selected as KAIST Breakthroughs: The paper "Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing, Nature Communications" is selected as KAIST Breakthroughs
- 2024-09-30 · Introduced to the media: The paper "Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing, Nature Communications" is introduced to various media
- 2024-09-30 · Introduced to the media: The paper "Reliable multilevel memristive neuromorphic devices based on amorphous matrix via quasi-1D filament confinement and buffer layer, Science Advances" is introduced to various media
- 2024-09-30 · Selected as the front cover: The paper "Neural Network Physically Unclonable Function: A Trainable Physically Unclonable Function System with Unassailability against Deep Learning Attacks Using Memristor Array" is selected as the front cover of Advanced Intelligent Systems
- 2024-09-30 · ENTIS Lab Starts: ENTIS starts at KAIST EE (Dec. 2018).

## 연락과 위치

- 연구실: (34141) 대전광역시 유성구 대학로 291 한국과학기술원(KAIST) 정보전자공학동 E3-2, 5214호[^contact]
- 교수 연구실: E3-2동 5209호[^prof]
- 전화: 042-350-7450(교수), 042-350-7550(연구실)[^contact]
- 교수 이메일: shinhyun@kaist.ac.kr[^prof]
- 연구실은 학부생, 석사·박사과정, 박사후연구원을 모집하며, 관심 있는 사람은 교수에게 직접 이메일을 보내라고 안내한다.[^contact]
[^home]: 연구실 누리집 첫 화면 <https://shinhyunlab.kaist.ac.kr/> (2026-10-22 열람)
[^areas]: Research 메뉴 Research Areas 페이지 <https://shinhyunlab.kaist.ac.kr/researchareas> (2026-10-22 열람)
[^emerging]: Research 메뉴 Emerging Devices 페이지 <https://shinhyunlab.kaist.ac.kr/emergingdevices> (2026-10-22 열람)
[^integrated]: Research 메뉴 Integrated Systems 페이지 <https://shinhyunlab.kaist.ac.kr/integratedsystems> (2026-10-22 열람)
[^applications]: Research 메뉴 Applications 페이지 <https://shinhyunlab.kaist.ac.kr/applications> (2026-10-22 열람)
[^prof]: Members 메뉴 Professor 페이지 <https://shinhyunlab.kaist.ac.kr/professor> (직함, 이메일, 연구실 위치, 소개문, 2026-10-22 열람)
[^members]: Members 메뉴 Postdocs <https://shinhyunlab.kaist.ac.kr/48>, Ph.D. Students <https://shinhyunlab.kaist.ac.kr/phdstudents>, M.S. Students <https://shinhyunlab.kaist.ac.kr/msstudents>, Undergraduates <https://shinhyunlab.kaist.ac.kr/undergraduates> 페이지 (2026-10-22 열람)
[^alumni]: Members 메뉴 Alumni 페이지 <https://shinhyunlab.kaist.ac.kr/alumni> (2026-10-22 열람)
[^pubs]: Publications 페이지 <https://shinhyunlab.kaist.ac.kr/47> (2021–2026년 논문과 "~2019" 아래 목록, 2026-10-22 열람)
[^awards]: News 메뉴 Awards 페이지 <https://shinhyunlab.kaist.ac.kr/awards> (2026-10-22 열람)
[^news]: News 메뉴 ENTIS News 게시판 <https://shinhyunlab.kaist.ac.kr/entisnews> (글 23건, 글별 주소는 근거 페이지, 2026-10-22 열람)
[^contact]: Contact 페이지 <https://shinhyunlab.kaist.ac.kr/contact> (주소, 전화, 모집 안내, 2026-10-22 열람)
[^semicon]: KAIST 반도체공학대학원 연구 페이지 <https://semicon.kaist.ac.kr/sub02/view> (「차세대 반도체 소자」 칸, 2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (「반도체 소자 및 공정」 칸, 2026-10-22 열람)
[^p1]: S.-O. Park 외, S. Choi, Nature 628, 293-298 (온라인 2024-04-03). <https://doi.org/10.1038/s41586-024-07230-5> 초록 기준(논문 페이지 게시 초록).
[^p2]: J. Bae 외, S. Choi, Science Advances 10, eadm7221 (2024). <https://doi.org/10.1126/sciadv.adm7221> 초록 기준.
[^p3]: S.-O. Park 외, S. Choi, Nature Communications 13, 2888 (온라인 2022-06-03). <https://doi.org/10.1038/s41467-022-30539-6> 초록 기준.
[^p4]: S.-O. Park 외, S. Choi, Nature Communications 16, 5754 (온라인 2025-07-01). <https://doi.org/10.1038/s41467-025-60818-x> 초록 기준.
[^p5]: S. Seo 외, S. Choi, Nature Communications 13, 6431 (온라인 2022-10-28). <https://doi.org/10.1038/s41467-022-34178-9> 초록 기준.
[^p6]: D.-w. Kim 외, S. Choi, Nature Communications 17, 8311 (온라인 2026-07-04). <https://doi.org/10.1038/s41467-026-75211-5> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Jeong 외, S. Choi, Nature Electronics (온라인 2025-01-08). <https://doi.org/10.1038/s41928-024-01318-6> 초록 기준(논문 페이지 게시 초록).
[^p8]: J. Park, Y. Lee, H. Jeong, S. Choi, Advanced Intelligent Systems 3, 2100111 (온라인 2021-10-07). <https://doi.org/10.1002/aisy.202100111> 초록 기준.

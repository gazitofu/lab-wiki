# Device-to-System Integration Lab (DSIL)

**KAIST 전기및전자공학부·AI시스템학과 · 권지민 교수**

- 분야: 저차원 소재(2차원 전이금속 칼코겐화물·탄소나노튜브) 논리 트랜지스터, 산화물 반도체 수직 채널 트랜지스터와 3차원 DRAM, 단일 3차원 집적(M3D)과 설계·기술 공동 최적화(DTCO), 첨단 반도체 패키징(3D 프린팅 기판, RF·양자 패키징, 칩렛), 멀티칩 시스템 설계·평가(STCO)
- 대분야: 전기전자·반도체·광학, 소재
- 태그: 첨단 반도체 패키징[^contact][^research][^p5], 3차원 집적[^contact][^research][^p4], 차세대 트랜지스터·논리 소자[^research][^p1], 2차원 소재[^research][^p1][^p2], 산화물 반도체[^research][^p3], 메모리 반도체 소자[^research][^p3], 3D 프린팅[^research][^p6][^p7], 열전달·열관리[^research][^p7][^p8]
- 홈페이지: <https://dsil.kaist.ac.kr/>
- 근거와 출처: [Device-to-System Integration Lab 근거 페이지](dsil-sources.md)

> 차세대 AI 하드웨어에 쓸 반도체 기술을 소자에서 패키징, 시스템까지 이어서 연구하는 연구실이다. 새 소재로 만든 논리·메모리 트랜지스터, 소자 층을 칩 위에 차례로 쌓는 3차원 집적, 여러 칩을 묶는 첨단 패키징과 그 시스템 평가를 함께 다룬다.[^home][^contact]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 권지민 조교수가 이끈다.[^ee] 누리집은 연구실이 KAIST 전기및전자공학부와 AI시스템학과 소속이라고 밝힌다.[^contact] 교수는 2026년 4월 KAIST에 부임했고, 그 전에는 UNIST Department of Electrical Engineering의 조교수(2022년 8월–2026년 3월)였다.[^pi] 누리집 Alumni 페이지는 UNIST 시기의 구성원을 UNIST Nanoelectronics and Advanced Packaging Lab(UNL) 소속으로 적고, 2026년 인턴부터 KAIST Device-to-System Integration Lab(DSIL) 소속으로 적는다.[^alumni]

누리집은 연구 목표를 차세대 AI 하드웨어 시스템을 위한 핵심 반도체 기술 개발로 적는다. 전기전자공학을 중심으로 기계공학·재료공학·화학공학을 묶은 다학제적 방식으로 소자, 패키징, 시스템을 잇는 통합 반도체 기술을 연구한다는 것이다.[^home] 연구는 두 방향으로 나뉜다. 첫째는 단일(monolithic)·이종(heterogeneous) 3차원 집적회로(3D IC, 소자 층이나 칩을 위로 쌓아 만든 집적회로) 기술로, 3D IC용 논리·메모리 소자를 만들고 고성능·저전력 컴퓨팅을 위한 3D IC 설계 방법론인 설계·기술 공동 최적화(DTCO, 소자 공정과 회로 설계를 함께 맞춰 가며 최적화하는 방법)를 연구한다. 둘째는 첨단 반도체 패키징(칩을 기판·다른 칩과 연결하고 보호하는 기술) 공정과 여러 칩으로 된 시스템의 설계·평가 기술인 시스템·기술 공동 최적화(STCO)로, 여러 반도체 칩을 묶어 데이터를 아주 많이 주고받는 고성능 컴퓨팅 시스템을 만들 수 있는 확장 가능한 플랫폼을 개발한다.[^contact]

누리집이 드는 연구 분야는 네 가지다. 논리·메모리 트랜지스터(논리용 2차원 전이금속 칼코겐화물과 탄소나노튜브, DRAM용 산화물 반도체), 단일 3차원(M3D) 시스템(3D IC 설계와 전력·성능·면적 평가), 첨단 반도체 패키징, 이종 멀티칩 시스템(패키지 수준의 디지털 구조와 시스템 평가)이다.[^home] Research 페이지는 이를 세 팀으로 나눠 소개한다. 기술 개발(TD) 팀은 논리 소자와 메모리 소자를, 설계·평가(DB) 팀은 3차원 표준 셀(논리 회로를 만드는 기본 단위 회로) 구조와 단일 3차원 집적의 블록·시스템 수준 설계와 평가를, 부품·패키징(CP) 팀은 고속 연결을 위한 첨단 패키징, 3D 프린팅 기판, RF(무선 주파수) 패키징과 양자 컴퓨터용 극저온 패키징을 맡는다.[^research] 전기및전자공학부 교수 소개는 주요 연구를 3D IC와 첨단 패키징, 1·2차원 논리 소자와 DTCO, DRAM용 산화물 반도체 수직 채널 트랜지스터, 2.5·3차원 패키징, RF·양자 패키징, 칩렛(하나의 칩이 할 기능을 나눠 맡도록 따로 만든 칩 조각) 시스템 구조로 적는다.[^ee]

KAIST 부임 뒤 출판된 논문(대표 논문 1–8)을 보면 연구는 이렇게 모인다. 강유전성이 없는 새 결정상의 인듐 셀레나이드 박막을 4인치 웨이퍼 전체에 고르게 만들어 논리 트랜지스터로 썼고,[^p1] 광학 현미경 영상으로 이황화몰리브덴 조각의 두께를 가려 트랜지스터 1,615개의 특성을 통계로 분석했다.[^p2] 산화물 반도체 수직 채널 트랜지스터에 산소가 지나는 길을 조절하는 층을 넣어 축전기 없는 메모리 셀의 전류와 신뢰성을 높였고,[^p3] 탄소나노튜브 트랜지스터 두 층을 쌓아 시간에 따라 바뀌는 신호를 분류하는 소자를 보였다.[^p4] 패키징에서는 메모리 칩을 세워 붙이는 수직 다이(V-die) 메모리 구조를 고대역폭 메모리와 비교 평가했고,[^p5] 3D 프린팅으로 안테나와 신호선을 품은 패키지 기판과 액체 냉각 채널을 품은 세라믹 기판을 만들었으며,[^p6][^p7] 방열판 설계용 열 시뮬레이션을 신경망으로 대신하는 모델을 만들었다.[^p8] 교수는 연구 과정에서 나오는 여러 데이터를 함께 다루는 에이전트형 AI 연구 보조 시스템에 관심이 있다고 적고, AI와 사람이 함께 소자·패키징을 연구하는 환경을 만들 연구자를 찾는다.[^contact]

## 주요 연구 주제

### 1. 저차원 소재 논리 트랜지스터

실리콘 전계효과 트랜지스터(FET, 게이트 전압으로 전류를 켜고 끄는 트랜지스터)가 크기를 줄이는 한계에 다가가자 게이트가 채널을 사방에서 감싸는 GAA FET, n형과 p형 트랜지스터를 위아래로 쌓는 CFET, FlipFET 같은 새 구조와 저차원 채널 소재가 논리 소자로 연구되고 있다.[^research] 2차원 전이금속 칼코겐화물(TMD, 원자 몇 층 두께의 판 모양 반도체)과 1차원 탄소나노튜브(CNT)는 크기를 줄여도 전기적 성질이 좋고, 칩 배선층을 만드는 후반 공정(BEOL)과 맞는 낮은 온도에서 만들 수 있어 소자를 차례로 쌓는 단일 3차원 집적에 알맞다고 누리집은 적는다.[^research] 2차원 반도체에서는 단일 결정 조각(플레이크) 트랜지스터로 두께와 균일도가 특성에 주는 영향을 통계로 분석하고, 위쪽에 게이트를 둔 소자의 접촉 저항을 줄이고 고른 게이트 절연막을 입히는 공정을 거쳐 웨이퍼 크기 박막 소자로 넓힌다.[^research][^p2] 탄소나노튜브에서는 반도체성 나노튜브만 고순도로 골라내 기판 위에 촘촘하고 고르게 줄 세우는 공정과, 꺼진 상태의 누설 전류를 줄이는 도핑 구조, 이를 쌓은 CFET 구조를 연구한다.[^research] 새 소재로는 강유전성이 없는 κ상 인듐 셀레나이드(In2Se3) 트랜지스터를 4인치 웨이퍼에서 만들고 p형 산화물 트랜지스터와 묶어 인버터를 보였다(대표 논문 1).[^p1]

### 2. 산화물 반도체 수직 채널 트랜지스터와 3차원 DRAM

산화물 반도체(금속 산화물로 된 반도체)로 채널을 세로로 세운 수직 채널 트랜지스터(VCT)를 만들어 칩 위에 쌓을 수 있는 고밀도 메모리를 연구한다.[^research] 원자층 증착(ALD, 원자 한 층씩 막을 쌓는 공정)으로 산화물 박막의 성분비·두께·도핑을 맞추고, 소자 시뮬레이션(TCAD)으로 공정 변수가 특성에 주는 영향을 수치로 따진다.[^research] 소자 단위의 스트레스 시험과 메모리 단위의 보존 시간·동작 속도·내구성을 함께 평가하고, 이 트랜지스터로 된 DRAM 배열의 주변 회로를 설계해 메모리 안에서 계산하는 구조(PIM·CIM)로 넓힌다.[^research] 대표 논문 3은 인듐 주석 산화물(ITO) 채널 옆에 산소의 이동을 조절하는 층을 넣어 축전기 없는 게인 셀(gain cell) 메모리의 전류와 신뢰성을 함께 높였다.[^p3]

### 3. 단일 3차원 집적과 설계·기술 공동 최적화

표준 셀의 높이를 줄여 밀도를 높이는 방식이 배선 혼잡과 배선 기생 성분 때문에 한계에 다가가자, 셀을 3차원으로 쌓는 구조(CFET, 3DS-FET)나 전원 배선을 웨이퍼 뒷면으로 옮기는 방식이 연구되고 있다.[^research] 연구실은 소자·표준 셀·시스템 수준의 평가로 단일 3차원 집적 시스템의 블록·시스템 수준 설계와 성능 비교를 하고, CMOS 미세화의 한계를 넘어 3차원 집적을 적용할 방향과 로드맵을 제안하려 한다.[^research] 누리집은 그 예로 IEDM 2025 발표 「Active BSCDN benchmark framework with backside-compatible CNFET logic technology」(웨이퍼 뒷면 공정과 맞는 탄소나노튜브 트랜지스터 논리 기술을 쓴 평가 틀)를 든다.[^research][^pubs] 대표 논문 4는 이온의 움직임을 조절한 탄소나노튜브 트랜지스터 두 층을 단일 3차원 집적으로 쌓아 시간 척도가 다른 신호를 처리하는 소자를 만들었다.[^p4]

### 4. 첨단 패키징: 3D 프린팅 기판, RF·양자 패키징, 수직 다이

칩렛 기반 이종 집적에서 신호를 빠르고 믿을 수 있게 전하려고 전기·기계·열 특성을 함께 다루는 패키징을 개발한다.[^research] 전기·열 시뮬레이션으로 신호 간섭, 임피던스 불일치, 열이 몰리는 곳(핫스폿)을 미리 예측해 설계하고, 비아 채움·범프 형성·재배선층(RDL) 제작·칩 접합 같은 부품 기술을 만든다.[^research] 3D 프린팅으로 휜 관통 구멍이 있는 팬아웃 인터포저(칩들을 이어 주는 중간 기판)와, 동축 형태 관통 구멍과 28 GHz 패치 안테나를 한 번에 만든 덮개 기판을 연구하고,[^research][^p6] 저손실 유리 기판에 칩을 묻는 RF 패키징과 유리 관통 비아(TGV)로 열을 빼는 전기·열 공동 설계, 양자 컴퓨터의 큐비트를 극저온에서 읽고 제어하는 회로를 위한 인터포저 패키징을 다룬다.[^research] 열 관리에서는 3D 프린팅 세라믹 기판 안에 액체 냉각 채널을 넣은 전력 모듈 패키지와,[^p7] 방열판 설계용 열 시뮬레이션을 대신하는 신경망 모델을 만들었다.[^p8] 메모리 칩을 세워 붙이는 3.5D 수직 다이(V-die) 메모리 구조를 고대역폭 메모리와 비교 평가했고(대표 논문 5),[^p5] 누리집 소식은 초고대역폭 AI 가속기를 위한 V-die 집적 패키징 기술 개발 과제로 삼성미래기술육성사업(2025년 12월–2030년 12월)에 선정됐다고 알렸다.[^news]

## 대표 논문

권지민 교수가 KAIST에 부임한 2026년 4월 뒤 출판된 논문 가운데 교수가 교신저자(*)이고 초록을 구할 수 있는 논문 여덟 편을 연구 갈래에 걸쳐 골랐다. 여덟 편 모두 저자에 UNIST 시기의 구성원(Alumni 페이지의 UNL 소속이거나 People 페이지에 UNIST 대학원 과정으로 적힌 사람)이 있다.[^alumni][^members] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Wafer-scale uniform non-ferroelectric κ-phase In2Se3 transistors](https://doi.org/10.1038/s41467-026-72553-y) · Nature Communications | 2차원 반도체 인듐 셀레나이드(In2Se3)는 전하가 잘 움직이고 강유전성(전기장을 걸지 않아도 전기 분극이 남는 성질)이 강해 메모리 안 연산용으로 주목받았지만, 웨이퍼 크기로 배선 후반 공정(BEOL)과 맞게 기르기 어렵고 분극 때문에 생기는 이력 현상(같은 전압에서도 앞선 상태에 따라 전류가 달라지는 현상)이 논리 회로에 쓰기 어렵게 했다. 연구진은 열 증착으로 강유전성이 없는 κ상 In2Se3 막을 450 °C보다 낮은 온도에서 4인치 웨이퍼 전체에 고르게 만들었다. 이 상은 간접 띠간격(전자가 전류를 나르려면 넘어야 하는 에너지 간격) 1.45 eV의 n형 반도체이고, 원자 배열 때문에 저절로 생기는 분극이 억제되어 트랜지스터의 이력 현상이 없어졌다. 트랜지스터는 게이트 전압을 걸어야 켜지는 증가형으로 동작했고, 전계효과 이동도(전기장을 받은 전하가 움직이는 빠르기) 39.3 cm²/V·s와 1,000번 넘는 안정된 스위칭을 보였으며, 이는 전하를 붙잡는 결함 상태와 접촉 저항이 줄어든 덕분이다. p형 셀레늄 합금 텔루륨 산화물 트랜지스터와 묶어 출력이 끝까지 오가고 전압 이득이 큰 상보형 인버터(입력 신호를 뒤집어 내보내는 기본 논리 회로)를 보였다.[^p1] | 공동 1저자 Jaeyun Lee·Yongwoo Lee, 교신저자 Ao Liu·권지민·Yong-Young Noh |
| 2 | 2026 | [Statistically resolving thickness-dependent electrical characteristics in multilayer-MoS2 transistors](https://doi.org/10.1002/adfm.202532204) · Advanced Functional Materials | 원자 몇 층 두께의 2차원 반도체는 게이트 길이가 몇 나노미터인 트랜지스터에서도 전류를 잘 조절하지만, 층수에 따라 특성이 크게 달라지고 그 변화를 통계로 밝힌 연구는 없었다. 두께가 정해진 단결정 조각을 많이 얻어 소자로 만들기 어려웠기 때문이다. 연구진은 광학 현미경 영상의 밝기를 단층 수의 지표로 삼고, 가장자리가 흐리거나 밝기가 고르지 않은 조각을 알고리즘으로 걸러 질 좋은 이황화몰리브덴(MoS2) 조각만 골라 밝기 분포에 따라 두께 무리로 나눴다. 원자힘 현미경으로 확인한 두께는 3–8층이었다. 소자 배치 설계를 자동으로 만들어 12만 개가 넘는 조각에서 고른 트랜지스터 1,615개의 전기 특성을 재, 두께에 따라 전하가 들어가고 움직이는 방식을 살폈다. 쉽게 쓸 수 있는 광학 현미경으로 2차원 반도체 소자 연구를 빠르게 할 수 있음을 보였다.[^p2] | 1저자 Sanghyun Lee, 교신저자 Yongwoo Lee·Haksoon Jung·권지민 |
| 3 | 2026 | [Oxygen-tunnel indium tin oxide vertical channel transistors with enhanced current density and reliability for monolithic 3D compute-in-memory systems](https://doi.org/10.1002/adfm.202531989) · Advanced Functional Materials | 단일 3차원 집적에는 배선 공정이 견딜 수 있는 온도 안에서 밀도를 크게 높일 수 있는 내장 메모리가 필요하다. 원자층 증착으로 기른 비정질 산화물 반도체는 수직 구조에도 고르게 입혀지고 꺼진 상태의 누설 전류가 낮아, 축전기 없이 데이터를 담는 게인 셀 메모리용 수직 채널 트랜지스터에 알맞다. 그러나 수직 구조에서는 산소가 모자란 채널과 산소가 많은 절연막 옆벽이 맞닿아, 산소 빈자리 때문에 특성이 불안정해지고 전극 계면이 산화된다. 누설과 이동도의 균형이 좋은 인듐 주석 산화물(ITO)은 이런 산소 이동에 특히 약하다. 연구진은 SiN/SiO2/SiN 층으로 산소가 지나는 길을 공간적으로 조절하는 '산소 터널' 구조를 넣어 채널의 산소 빈자리를 안정시키고 전극 산화를 막았다. 그 결과 논문이 기록적으로 높다고 밝힌 436 µA/µm의 전류 밀도와, 10⁷번의 바이어스 스트레스 반복 뒤 50 mV보다 작은 문턱 전압 변화를 얻었다. 게인 셀 메모리는 꺼짐 전류가 2.6×10⁻¹⁹ A/µm로 낮아 648초가 넘는 보존 시간과 1,200번이 넘는 내구성을 보였다. 실리콘과 ITO 트랜지스터를 함께 쓰는 게인 셀 집적 틀을 만들어, 실리콘 기반 내장 메모리와 메모리 내 연산 구조에 넣을 때의 이점을 평가했다.[^p3] | 1저자 Hyeonho Gu, 교신저자 Haksoon Jung·Yongwoo Lee·권지민 |
| 4 | 2026 | [Monolithic 3D-integrated all-solid ion-gated carbon nanotube transistors with tunable ionic conductance for multi-timescale reservoir computing](https://doi.org/10.1002/adma.202523703) · Advanced Materials | 이온 게이트 트랜지스터(이온이 움직여 게이트 쪽에 전하층을 만드는 트랜지스터)는 이온이 움직이는 시간 때문에 시간에 따라 바뀌는 동작을 보이지만, 이온의 움직임을 조절하기 어렵고 웨이퍼 단위 박막 공정과 맞추기 힘들었다. 연구진은 탄소나노튜브 채널에 고체 이온 막을 게이트로 쓴 트랜지스터(sIGT)를 만들고, 막 속 이온 함량과 1마이크로미터 아래로 줄인 막 두께로 이온 전도도를 조절해 이온 시간 상수를 마이크로초에서 밀리초까지 바꿨다. 이온 함량이 낮을 때도 고분자 바탕을 최적화해 직류 동작이 안정적이었고, 유연 기판 위에서 웨이퍼 단위로 만들었다. 전기 임피던스 분광과 소신호 분석으로 이온 전도도와 주파수에 따른 응답의 관계를 살폈고, 두 단자와 세 단자 소자에서 같은 경향을 보였다. 응답 속도가 다르게 설계된 두 층의 소자를 단일 3차원 집적으로 쌓아, 읽기 층 하나로 시간에 따라 바뀌는 입력을 분류하는 두 시간 척도의 물리 저수지(입력을 소자의 시간 응답으로 바꾸고 마지막 읽기 층만 학습하는 계산 방식)를 뉴로모픽 계산용으로 보였다.[^p4] | 1저자 Haksoon Jung, 교신저자 Yong-Young Noh·권지민 |
| 5 | 2026 | [Vertical-die (v-die) 3.5D integration for cool ultrahigh-bandwidth memory systems](https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577552) · IEEE Symposium on VLSI Technology and Circuits 2026 | 보통 방식으로 만든 DRAM 다이(웨이퍼에서 잘라 낸 칩 한 조각)를 세워 시스템 수준에서 3차원 공간을 쓰는 3.5D 수직 다이(V-die) 메모리 구조를 새 집적 방식으로 살폈다. 얻을 수 있는 대역폭, 용량 확장성, 열 특성을 최신 고대역폭 메모리(HBM, 메모리 칩을 쌓아 한 번에 많은 데이터를 주고받게 만든 메모리)와 비교해 실현 가능성을 평가했다. 다이를 세우면 드러나는 표면이 넓어지고 이웃 다이 사이를 액체로 바로 식힐 수 있어, 훨씬 큰 열 설계 전력을 감당하면서 기존 HBM을 넘는 입출력 밀도와 용량으로 키울 수 있다.[^p5] | 공동 1저자 Heesoo Yang·Hyeongjun Kim, 교신저자 권지민 |
| 6 | 2026 | [3D-printed coaxial-fed patch-antenna-embedded substrates for 5G antenna-in-package applications](https://doi.org/10.1109/ectc51846.2026.00298) · IEEE Electronic Components and Technology Conference (ECTC) 2026 | 안테나를 칩 패키지 안에 넣는 안테나 인 패키지(AiP)에 흔히 쓰는 수직 급전선은 접지로 감싸지 않으면 전파가 새어 손실이 생긴다. 연구진은 3D 프린팅으로 만든 기판 안에 동일 평면 도파관(CPW, 신호선 양옆에 접지를 둔 평면 전송선)·동축선·패치 안테나를 함께 넣은 28 GHz용 AiP 기판을 내놓았다. 동축 구조가 CPW와 동축선을 기판 면에 수직 방향으로 잇고, 바깥 도체를 신호선과 일정 간격 떼어 절연하면서도 임피던스 정합을 유지해 24–32 GHz에서 반사 손실이 −20 dB보다 작았다. 28 GHz에서 CPW 선과 CPW–동축선–CPW 경로의 삽입 손실은 각각 cm당 −2.05 dB와 −2.25 dB였다. 이 경로로 급전한 패치 안테나는 28 GHz에서 공진해 S11 −16.2 dB, 지향성 6.74 dBi, 실현 이득 4.03 dBi와 안정된 정면 방사를 보였다. 모양을 자유롭게 만드는 적층 제조로 작은 5G AiP를 만들 수 있음을 보였다.[^p6] | 1저자 Kyungsun Kim, 교신저자 Haksoon Jung·권지민 |
| 7 | 2026 | [Microchannel-embedded 3D-printed ceramic substrates for liquid-cooled power module packaging](https://doi.org/10.1109/ectc51846.2026.00240) · IEEE Electronic Components and Technology Conference (ECTC) 2026 | 전기차·데이터센터·재생에너지 설비의 전력 밀도 요구가 커지면서 전력 전자 패키징의 열·전기 관리가 중요해졌다. 와이어 본딩과 한쪽 면 냉각 구조는 여러 층의 열 계면과 좁은 방열 경로 때문에 기생 성분으로 스위칭 특성이 나빠지고 온도가 오른다. 연구진은 관통 구멍과 미세 유체 냉각 채널을 함께 넣은 3D 프린팅 세라믹 기판으로 양면을 식히는 플립칩(칩을 뒤집어 범프로 기판에 붙이는 방식) 전력 모듈 패키지를 제안했다. 자외선 노광량을 기능별 세 구역으로 나눠 세라믹을 정밀하게 프린팅해, 종횡비 1:10의 관통 구멍과 지름 500 μm까지의 가로 미세 채널을 패키지 전체에 만들었다. 기판은 상용 질화갈륨 전력 트랜지스터의 범프 설계에 맞췄고 최종 두께는 0.8 mm였다. 열 시뮬레이션에서 관통 구멍 배열 사이의 미세 유체 채널은 최고 온도를 84.0% 낮췄다.[^p7] | 1저자 Haksoon Jung, 교신저자 권지민 |
| 8 | 2026 | [Machine learning-based surrogate model of thermal simulation for heat sink design](https://doi.org/10.23919/icep-hbs69241.2026.11550638) · International Conference on Electronics Packaging and Hybrid Bonding Symposium (ICEP-HBS) 2026 | 방열판 설계를 최적화할 때 열 시뮬레이션에 드는 계산 시간을 크게 줄이려고 합성곱 신경망(CNN, 영상처럼 격자로 놓인 입력을 다루는 신경망) 기반 대리 모델(시간이 많이 드는 시뮬레이션 결과를 빠르게 흉내 내 예측하는 모델)을 만들었다. 대상은 GPU 1개와 HBM 6개로 된 AI 가속기에 붙는 방열판으로, 기둥 모양 핀이 43×28로 늘어선 구조이고 핀 하나는 폭 0.75 mm, 깊이 0.2 mm, 높이 1 mm다(대칭 가정). 핀의 방향 각도를 바꿔 가며 열 시뮬레이션 데이터를 만들고, 핀 각각의 각도를 픽셀 입력으로 받아 시스템 최고 온도를 예측하는 43×28 CNN 구조를 만들었다. 이 모델은 예측 정확도가 높으면서 계산 효율이 크게 좋다.[^p8] | Seongju Kim, 교신저자 권지민 |

## 교수와 전문 분야

권지민 교수(Jimin Kwon)는 KAIST 전기및전자공학부 조교수이고, 교수 소개의 디비전은 Device다.[^ee] 누리집 PI 페이지는 2026년 4월부터 KAIST 전기및전자공학부와 AI시스템학과(Department of AI Systems)의 조교수라고 적고,[^pi] Contact 페이지는 교수가 KAIST 반도체공학대학원 참여교수와 신소재공학과 겸임교수를 함께 맡는다고 적는다.[^contact] 반도체시스템공학과 교수 명단에도 연구분야 「반도체 소자 및 공정」으로 올라 있다.[^ssep] 전기및전자공학부 교수 소개는 주요 연구분야를 AI·기계학습, 집적회로·반도체 시스템, 양자 과학·공학, 반도체 소자·나노기술, RF·밀리미터파 소자·시스템으로 적는다.[^ee]

포항공과대학교(POSTECH)에서 학사(Department of Electrical Engineering, 2012), 석사(Division of IT Convergence Engineering, 2014), 박사(Department of Convergence IT Engineering, 2018)를 받았다.[^pi][^ee] 이어 POSTECH Future IT Innovation Lab·Department of Chemical Engineering 박사후연구원(2018년 10월–2020년 8월), 미국 스탠퍼드대학교 Department of Electrical Engineering 박사후연구원(2020년 10월–2022년 8월), UNIST Department of Electrical Engineering 조교수(2022년 8월–2026년 3월)를 지냈다.[^pi] PI 페이지의 수상 목록은 Korea Flexible & Printed Electronics (KFPE) Emerging Scholar Award(2024), POSTECH Alumni Association President’s Award(2019), Best Doctoral Dissertation Award, Department of Creative IT Engineering, POSTECH(2019), Winner, Graduation Design Award, Department of Electrical Engineering, POSTECH(2011)이다.[^pi] 2024년 수상은 누리집 국문 소식이 한국유연인쇄전자학회 신진학술상으로 적는다.[^news] 학계 활동으로는 IEEE 전자소자학회(EDS) Flexible Electronics and Displays Committee의 Member와 한국마이크로전자 및 패키징학회(The Microelectronics and Packaging Society of Korea)의 Academic Director(2024)를 적는다.[^pi]

논문 목록으로 보면 전문 분야는 시기에 따라 넓어졌다. 2016–2020년 논문은 잉크젯으로 찍어 만든 유기 트랜지스터를 위아래로 쌓은 3차원 회로, 인쇄형 유기 메모리와 센서가 중심이다.[^pubs] 2021–2023년 목록에는 인듐 주석 산화물 트랜지스터, 8층 3차원 수직 저항 메모리(RRAM, 전압으로 저항 상태를 바꿔 정보를 저장하는 메모리), 3차원 집적 컴퓨팅 하드웨어를 다룬 공저 논문(교신저자 E. Pop, H.-S. P. Wong, S. Mitra 등)이 있다.[^pubs] 2023–2025년 목록에서 교수가 교신저자(*)인 논문은 인쇄형 탄소나노튜브 트랜지스터, 이황화몰리브덴 트랜지스터의 결함 보정, 유기 전기화학 트랜지스터, 인듐 주석 산화물 수직 채널 트랜지스터, 3D 프린팅 패키징 기판 등을 다룬다.[^pubs] 누리집 특허 목록은 2018–2020년 구역에 3차원으로 쌓은 이중 게이트 박막 트랜지스터 논리 회로와 3차원 SRAM 셀 등 등록 특허 6건을 적는다.[^patents]

## 응용 분야

누리집은 연구의 목표를 차세대 AI 하드웨어와 이종 집적 컴퓨팅 시스템으로 적는다.[^contact] 대표 논문이 직접 든 쓰임은 다음과 같다. 배선 공정과 맞는 2차원 반도체 논리 회로,[^p1] 실리콘 위에 쌓는 내장 메모리와 메모리 내 연산 구조,[^p3] 시간에 따라 바뀌는 신호를 분류하는 뉴로모픽 계산,[^p4] 고대역폭 메모리를 넘는 대역폭·용량의 메모리 시스템,[^p5] 5G 안테나 인 패키지,[^p6] 전기차·데이터센터·재생에너지 설비의 전력 모듈 패키징,[^p7] AI 가속기의 방열판 설계다.[^p8] 누리집 Research 페이지는 큐비트를 읽고 제어하는 극저온 회로의 패키징을 양자 컴퓨팅 시스템용으로 연구한다고 적고,[^research] 누리집 소식은 양자시스템 제어를 위한 마이크로파 신호 생성·처리 장치 개발 과제로 양자공통기반기술개발사업(과학기술정보통신부·한국연구재단, 2025년 7월–2027년 12월)에 선정됐다고 알렸다.[^news]

Contact 페이지의 모집 분야에는 3차원 집적회로용 표준 셀을 AI 에이전트로 자동 설계하고 반도체 측정을 자동화하는 일, RF 패키징 환경을 고려한 전력 증폭기·임피던스 정합 회로를 AI로 설계하는 일, 수직 채널 DRAM 읽기 회로를 위한 신경망 소자 모델, 칩렛 시스템의 성능 예측 시뮬레이터가 있다.[^roles]

## 구성원

누리집 People 페이지가 처음 열 때 보여 주는 2026년 여름 학기(2026 Summer) 명단의 23명이다(교수 제외). 과정 칸은 각 구성원 소개의 학력·경력 가운데 지금(present)까지 이어지는 줄의 과정이고, 괄호 안은 그 줄이 적은 학교와 학과다. 시작 칸은 그 줄의 시작 시점이고, 연구 주제 칸은 소속 팀과 연구 분야(괄호 안은 세부 주제) 표기다.[^members] Hyeonho Gu는 소개에 지금까지 이어지는 줄이 없어 Alumni 페이지의 현재 표기(Post MS Researcher, KAIST)를 적었다.[^alumni] 2026년 봄 학기(2026 Spring) 명단에는 Sanghyun Lee(TD Team, UNIST Graduate School of Semiconductor Materials and Devices Engineering 석사과정)도 있다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Yongwoo Lee | 박사후연구원 (KAIST, School of Electrical Engineering) | Apr 2026 | Components and Packaging (CP) Team: Advanced semiconductor packaging (RF packaging for heterogeneous wireless systems; Panel-level packaging with additive manufacturing for high-speed I/O systems) / Scaling-Up Printed Electronics (Ion-gated FET RF varactors; Intelligent reflective surface (IRS) for 5G/6G) | ywlee96@kaist.ac.kr | 1, 2, 3, 4, 5, 6 |
| Haksoon Jung | 박사후연구원 (KAIST, School of Electrical Engineering) | Apr 2026 | CP Team: Advanced Packaging with 3D Printing (3DP fanout and chiplet interposers; New material engineering for packaging substrates) / Low-Dimensional Semiconductors for M3D (High-purity semi-CNT dispersion and alignment; Defect engineering of 2D TMD materials) | hsjung71@kaist.ac.kr | 1, 2, 3, 4, 5, 6, 7 |
| Youngmin Jo | 박사후연구원 (KAIST, Department of Electrical Engineering) | Apr 2026 | Technology Development (TD) Team: Vertical-Channel OS FET for M3D Memory (Gate-all-around VC OS FET; Channel-all-around VC OS FET) | ymjo@kaist.ac.kr | 3 |
| Hyeonho Gu | 연구원 (Post MS Researcher, KAIST) |  | TD Team: Vertical-Channel OS FET for M3D Memory (Channel-all-around VC OS FET; M3D eDRAM array fabrication) | hyeonho97@unist.ac.kr | 1, 3 |
| Sungmin Eum | 석박사통합과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Mar 2024 | CP Team: High-Speed CNFETs (CNFET RF fabrication and modeling; CNT-based MMIC/RFPA design; 3D CNFET benchmark circuit design and fabrication) | esm98@unist.ac.kr |  |
| Minho Park | 석박사통합과정 (UNIST, Department of Electrical Engineering) | Mar 2024 | Design and Benchmark (DB) Team: M3D Technology, Design and Benchmark Framework (Vertical-channel OS eDRAM design rules; Physical modeling of novel FETs; 1D/2D FET logic benchmark in modern processor building blocks) | mhpark@unist.ac.kr | 2, 3 |
| Hyeonjin Lee | 석박사통합과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Sep 2024 | TD Team: Vertical-Channel OS FET for M3D Memory (Gate-all-around VC OS FET; Reliability analysis VC OS FET for DRAM) | hjlee0706@unist.ac.kr | 1, 3 |
| Seunghun Baek | 석박사통합과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Mar 2025 | TD Team: Å-node CNFET Logic (Highly scaled CNFETs; TCAD-based CNFET logic design; 3D CNFET standard cell logic library and benchmark circuit fabrication) | sh.baek@unist.ac.kr | 3, 4 |
| Heesoo Yang | 석박사통합과정 (UNIST, Department of Electrical Engineering) | Mar 2025 | DB Team: Autonomous Design of Systems (Digital IP design and verification; System-level modeling and simulation; Agentic AI for design automation) | kristron@unist.ac.kr | 3, 5 |
| Hyeongjun Kim | 석박사통합과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Mar 2025 | CP Team: Large-Area RF Electronics (Ion-gated FET RF varactors; Intelligent reflective surface (IRS) for 5G/6G; Panel-level-packaging with EHD inkjet printing) | hjkim00@unist.ac.kr | 4, 5 |
| Kyungsun Kim | 석사과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Sep 2025 | CP Team: Large-Area RF Electronics (Intelligent reflective surface (IRS) for 5G/6G; Glass interposer and Chiplet; EMC/EMI design for chiplet interposer substrates) | kskim99@unist.ac.kr | 6 |
| Dongjin Wi | 석사과정 (UNIST, Graduate School of Semiconductor Materials and Devices Engineering) | Mar 2026 | TD Team: Oxide Semiconductor FET for M3D Memory (Vertical-Channel OS FET; M3D eDRAM array fabrication) / Electronic Design Automation for M3D Logic (FET parameterized cell (PCell); Standard cell logic library generation) | djwi@unist.ac.kr |  |
| Seoyon Choe | 석사과정 (KAIST, The Kim Jaechul Graduate School of AI) | Mar 2025 | DB Team: AI-Driven Design Automation for Device to System Integration (Generative AI for Power Amplifier Design; Design Automation with agentic AI) | starlight345@kaist.ac.kr |  |
| Kyungbin Lee | 석사과정 (KAIST, Graduate School of Semiconductor Technology) | Aug 2026 | DB Team: Design Technology Co-Optimization (DTCO), Design Automation (Physical design automation (Open-source PDK, PnR flow); 3D-stacked logic architectures (CFET, FlipFET); Novel-material logic devices (2D TMD, CNT)) | kblee@kaist.ac.kr |  |
| Gihwan Han | 석사과정 (KAIST, The School of Electrical Engineering) | Aug 2026 | CP Team: System-Technology Co-Optimization (Thermal & Power Integrity co-analysis and design for HBM-GPU Architecture) | ghhan01@kaist.ac.kr |  |
| Jinsoo Yun | 석사과정 (KAIST, Graduate School of Semiconductor Technology) | Aug 2026 | TD Team: 3D-Stacked Logic Devices (Carbon nanotube and 2D-material transistors; Beyond-CFET 3D integration) / Design Enablement for Stacked CMOS (Compact modeling and standard cell design; Circuit design and benchmarking) | jsyun@kaist.ac.kr |  |
| Woomin Jeon | 석박사통합과정 (KAIST, Department of AI Systems) | Aug 2026 | CP Team: Advanced Packaging (Quantum Packaging for Cryogenic Quantum Computing Systems) | wmjeon@kaist.ac.kr |  |
| Siwon Jang | 학사과정 (Sungkyunkwan University, Department of Material Science and Engineering) | Mar 2020 | CP Team: Vertical Die Packaging (Packaging process(bump, bonding, RDL etc.); Underfill materials for bonding process) |  |  |
| Hanjo Choo | 학사과정 (Korea University, Department of Physics (major) and Next Generation Semiconductor Engineering (second major)) | Mar 2024 | TD Team: Vertical-Channel OS FET for M3D Memory | choo1596@korea.ac.kr |  |
| Woojun Choi | 학사과정 (KAIST, The School of Electrical Engineering) | Feb 2022 | TD Team: Advanced Logic Devices | woojun001@kaist.ac.kr |  |
| Jonghyeon Lee | 박사과정 (KAIST, Department of AI Systems) | Aug 2026 | CP Team: Signal and Power Integrity Design for High-Speed Interconnects (Signal and power integrity analysis for chiplet and HBM interfaces) | jhlee990724@kaist.ac.kr |  |
| Dongol Cho |  |  | DB Team: Standard Cell Layout Synthesis and DTCO for Advanced Devices | dongol.cho@kaist.ac.kr |  |
| Yujin In | 학사과정 (Sookmyung Women's University, Department of Electronic Engineering) | Mar 2022 | DB Team: Analog/mixed-signal I/O circuit design (High-Speed Interface PHY Circuit Design) | inyj03@sookmyung.ac.kr |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 Alumni 칸 6명과 Intern 칸 5명이다. 학위·과정 칸은 페이지가 적은 연구실·역할·팀과 기간이고, 진로 칸은 페이지의 「Current」 표기다. UNIST Nanoelectronics and Advanced Packaging Lab(UNL)으로 적힌 7명은 교수가 UNIST에 있던 때의 구성원이고, KAIST Device-to-System Integration Lab(DSIL)로 적힌 4명은 2026년 여름 인턴이다. Hyeonho Gu는 위 구성원 표에도 있다.[^alumni][^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seongju Kim | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) Postdoctoral Researcher, CP Team (Mar 2025 - Aug 2025) | Assistant Professor, Department of Creative Convergence Engineering, Hanbat National University |
| Hyeonho Gu | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) MS Student, TD Team (July 2023 - Current) | Post MS Researcher, KAIST |
| Yurim Choi | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) MS Student, CP Team (January 2024 – July 2026) | Samsung SDI |
| Nahyeon Kim | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) MS Student, CP Team (January 2024 – Aug 2026) | KAIST Ph.D. student |
| Sumin Hong | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) MS Student, TD Team (January 2024 – Aug 2026) |  |
| Yehyun Shin | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) MS Student, TD Team (January 2024 – Aug 2026) |  |
| Seungmin Lee | UNIST Nanoelectronics and Advanced Packaging Lab (UNL) Intern, Design and Benchmark (DB) Team (Aug 2025 - Jan 2026) | BS Student, Department of Computer Science and Engineering, UNIST |
| Eunchae Choi | KAIST Device-to-System Integration Lab (DSIL) Intern, Technology Development (TD) Team (May 2026 - Aug 2026) | BS Student, The School of Electrical Engineering, KAIST |
| Seojun Ban | KAIST Device-to-System Integration Lab (DSIL) Intern, Technology Development (TD) Team (May 2026 - Aug 2026) | BS Student, The School of Electrical Engineering, KAIST |
| Minjae Cho | KAIST Device-to-System Integration Lab (DSIL) Intern, Technology Development (TD) Team (June 2026 - Aug 2026) | BS Student, The School of Electrical Engineering, KAIST |
| Dongkyu Lee | KAIST Device-to-System Integration Lab (DSIL) Intern, Technology Development (TD) Team (June 2026 - Aug 2026) | BS Student, Department of Electronic & Electrical Engineering, Hongik University |

## 최근 논문 목록 (2021–2026)

누리집 Publications 절의 International Journals 49편 가운데 2021–2026년 연도 구역 27편([023]–[049]), Domestic Journals 3편 전부, Conference Proceedings 20편 가운데 2021–2026년 연도 구역 16편([005]–[020])이다. 제목·저자·학술지·학회 이름은 누리집 표기 그대로이고, 저자 이름 뒤 *는 교신저자, †는 공동 기여 표시다. 국내 학술지는 이름 뒤에 (국내)를 붙였다. 교수 개인의 논문 목록이어서 2026년 4월 KAIST 부임 전 스탠퍼드대학교(2020년 10월–2022년 8월)·UNIST(2022년 8월–2026년 3월) 시기의 논문이 대부분이며, 모두 현재 KAIST 연구실의 성과로 묶지 않는다.[^pubs][^pi]

**2026**

- Haksoon Jung, Hanbin Cho, Yongwoo Lee, Seunghun Baek, Hyeongjun Kim, Yun Goo Ro, Hyunhyub Ko, Joonki Suh, Yong-Young Noh\*, Jimin Kwon\*. "Monolithic 3D-integrated all-solid ion-gated carbon nanotube transistors with tunable ionic conductance for multi-timescale reservoir computing". *Advanced Materials (2026)*.
- Hyeonho Gu, Haksoon Jung\*, Yongwoo Lee\*, Hoichang Jeong, Yanfeng Zhao, Heesoo Yang, Minho Park, Hyeonjin Lee, Seunghun Baek, Minju Song, Junghwan Kim, Youngmin Jo, Hyunjin Park, Munhyeon Kim, Jae-Joon Kim, Kyuho Jason Lee, Byungjo Kim, Jimin Kwon\*. "Oxygen-tunnel indium tin oxide vertical channel transistors with enhanced current density and reliability for monolithic 3D compute-in-memory systems". *Advanced Functional Materials e31989 (2026)*.
- Jaeyun Lee†, Yongwoo Lee†, Haksoon Jung, Taoyu Zou, Mingyu Kim, Hyeonho Gu, Hyeonjin Lee, Tae Hyeon Park, David ChangMo Yang, Chang Woo Myung, Ao Liu\*, Jimin Kwon\*, Yong-Young Noh\*. "Wafer-scale uniform non-ferroelectric κ-phase In2Se3 transistors". *Nature Communications 17, 5901 (2026)*.
- Sanghyun Lee, Sumin Hong, Minho Park, Seongju Kim, Sanghoon Baek, Seonguk Yang, Chang-Soo Lee, Sang-Hoon Bae, Joonki Suh, Yongwoo Lee\*, Haksoon Jung\*, Jimin Kwon\*. "Statistically resolving thickness-dependent electrical characteristics in multilayer-MoS2 transistors". *Advanced Functional Materials 36, e32204 (2026)*.
- Haksoon Jung†, Joonghoon Choi†, Seunghun Baek, Bong Gyu Shin, Young Jae Song\*, Hanggyo Jung, JoHyeon Kim, Jongwook Jeon\*, Gyumin Kim, Heechun Park\*, Yeonjoo Lee, Jinkyoung Yoo\*, Jae-Hyun Lee, Hyungwoo Kim, Kibum Kang\*, Jaeyong Jeong, Sang Hyeon Kim\*, Joohan Bae, Chang Soo Kim, Won Kwang Yang, Sungjoo Lee, Jiwook Kwon\*, Byung-Sung Kim, Jae-Hoon Han\*, Hyung-Jun Kim, Hoon Hahn Yoon\*, Jimin Kwon\*, Young Joon Hong\*. "Advances and future challenges in monolithic 3D integrated logic, power, and optoelectronics technologies for tightly interconnected intelligent systems". *ACS Nano 20, 6407-6445 (2026)*.
- Hyeonho Gu†, Haksoon Jung†, Minho Park, Hyeonjin Lee, Ae Rim Choi, Il-Kwon Oh, Yanfeng Zhao, Byungjo Kim, Jungsik Kim, Byung Chul Jang, Yongwoo Lee, Jimin Kwon\*. "Indium tin oxide vertical channel transistors for scaled 4F2 2T0C gain cell memory with etched sidewall cleaning". *IEEE Electron Device Letters 47, 836-839 (2026)*.
- 이용우, 음성민, 김경선, 박윤식, 권지민\*. "IC 내장형 유리기판 RF 패키징 기술 동향". *J. Microelectron. Packag. Soc. 33, 22-35 (2026) (국내)*.
- 정학순, 권지민\*. "AI 하드웨어를 위한 3D 패키징 고대역폭/대용량 메모리 기술 발전과 연구 동향". *J. Microelectron. Packag. Soc. 33, 36-47 (2026) (국내)*.
- Seongju Kim, Jimin Kwon\*. "Machine learning-based surrogate model of thermal simulation for heat sink design". *2026 International Conference on Electronics Packaging joined with Hybrid Bonding Symposium (ICEP-HBS 2026)*.
- Haksoon Jung, Yurim Choi, Kyungsun Kim, Nahyeon Kim, Jimin Kwon\*. "Analysis of shrinkage-induced dimensional mismatch in 3D-printed packaging substrates for flip-chip bonding". *2026 International Conference on Electronics Packaging joined with Hybrid Bonding Symposium (ICEP-HBS 2026)*.
- Heesoo Yang† (Presenter), Hyeongjun Kim†, Yurim Choi, Seungmin Lee, Dongyun Kam, Haksoon Jung, Yongwoo Lee, Seongju Kim, Jimin Kwon\*. "Vertical-die (v-die) 3.5D integration for cool ultrahigh-bandwidth memory systems". *2026 IEEE Symposium on VLSI Technology and Circuits (VLSI)*.
- Haksoon Jung (Presenter), Seongju Kim, Nahyeon Kim, Seungjun Chung, Jimin Kwon\*. "Microchannel-embedded 3D-printed ceramic substrates for liquid-cooled power module packaging". *2026 76th IEEE Electronic Components and Technology Conference (ECTC)*.
- Kyungsun Kim (Presenter), Haksoon Jung\*, Nahyeon Kim, Yongwoo Lee, Yunsik Park, Jimin Kwon\*. "3D-printed coaxial-fed patch-antenna-embedded substrates for 5G antenna-in-package applications". *2026 76th IEEE Electronic Components and Technology Conference (ECTC)*.

**2025**

- Yongwoo Lee†, Seong Jun Park†, Jimin Kwon\*, Kang-Il Song\*, Sungjune Jung\*. "Addressing transconductance-bandwidth trade-off by three-dimensional electrolyte-surrounded organic electrochemical transistors". *Science Advances 11, eady0279 (2025)*.
- Haksoon Jung†, Mingyu Kim†, Yongwoo Lee, Gi Beom Sim, Hyeonho Gu, Sumin Hong, Sanghyun Lee, Jaehyun, Donghyeop Lee, Taoyu Zou, Kibum Kang, Chang Woo Myung, Yong-Young Noh\*, Jimin Kwon\*. "Back-end-of-line-compatible passivation of sulfur vacancies in MoS2 transistors using electron-withdrawing benzenethiol". *ACS Nano 19, 6069-6078 (2025)*.
- Youngmin Jo, Youngoh Lee, Jimin Kwon, Seongju Kim, Gyungin Ryu, Soyoung Yun, Sanghoon Baek\*, Hyunhyub Ko\*, Sungjune Jung\*. "3D active-matrix multimodal sensors arrays for independent detection of pressure and temperature". *Science Advances 11, eads4516 (2025)*.
- Yehyun Shin†, Ikkyum Kim†, Minho Park† (Presenter), Junghyun Yoon, Seunghun Baek, Seongmin Eum, Heesoo Yang, Yurim Choi, Jaeyong Jeong, Sanghyeon Kim, Haksoon Jung, Seongju Kim\*, Heechun Park\*, Jimin Kwon\*. "Active BSCDN benchmark framework with backside-compatible CNFET logic technology". *2025 71th IEEE International Electron Devices Meeting (IEDM)*.
- Jaeyong Jeong†, Yurim Choi†, Seongju Kim, Hyeongjun Kim, Jimin Kwon\*, Sanghyeon Kim\*. "Monolithic 3D integration of III-V HEMTs on glass using ultra-thin dielectric bonding layer: a high-frequency and low-loss active glass platform for sub-THz applications". *2025 71th IEEE International Electron Devices Meeting (IEDM)*.
- Young Suh Song†, Jimin Kang†, Hyeonho Gu†, Haotian Su, Yuan-Mau Lee, Shan X. Wang, Jimin Kwon\*, H.-S. Philip Wong\*, Eric Pop\*. "Thermal evaluation and comparison of CAA and GAA indium tin oxide vertical channel transistors". *2025 71th IEEE International Electron Devices Meeting (IEDM)*.
- Nahyeon Kim (Presenter), Haksoon Jung\*, Yurim Choi, Hyeongjun Kim, Seongju Kim, Yongwoo Lee, Yunsik Park, Seungyeon Koh, Hyeok Kim, Jimin Kwon\*. "Quasi-coaxial through-hole integrated additively manufactured antenna-in-package lid substrates". *2025 75th IEEE Electronic Components and Technology Conference (ECTC)*.
- Haksoon Jung (Presenter), Nahyeon Kim, Yurim Choi, Seongju Kim, Hyunjin Park, Yunsik Park, Seungjun Chung, Jiheong Kang, Jimin Kwon\*. "3D printed fanout interposer substrates with curved through-holes for rapid prototyping of advanced packaging". *2025 75th IEEE Electronic Components and Technology Conference (ECTC)*.

**2024**

- Sanghoon Baek\*, Youngmin Jo, Yongwoo Lee, Jimin Kwon\*, Sungjune Jung\*. "Design and integration of organic printed thin-film transistor-based soft biosensors for wearable applications". *ACS Applied Electronic Materials 6, 7657-7678 (2024)*.
- Minsik Kong†, Man Hou Vong†, Mingyu Kwak, Ighyun Lim, Younghyun Lee, Seong-hun Lee, Insang You, Omar Awartani, Jimin Kwon, Tae Joo Shin, Unyong Jeong\*, Michael D Dickey\*. "Ambient printing of native oxides for ultrathin transparent flexible circuit boards". *Science 385, 731-737 (2024)*.
- Yongwoo Lee†, Haksoon Jung†, Youngmin Jo, Sanghoon Baek, Hyunjin Park, Seong Jun Park, Sungjune Jung, Yong-Young Noh\*, Jimin Kwon\*. "Dual-gate carbon nanotube thin-film transistors with printed channel and passivation interlayer on plastic foil". *IEEE Electron Device Letters 45, 2036-2039 (2024)*.
- Yongwoo Lee, Boseok Kang, Sungjune Jung\*, Jimin Kwon\*. "Stabilizing schottky junction in conjugated polymer diodes enables long-term reliable radio-frequency energy harvesting on plastic". *npj Flexible Electronics 8, 41 (2024)*.
- Woojo Kim, Gyungin Ryu, Youhyun Nam, Hyeonmin Choi, Meng Wang, Jimin Kwon, Christian B Nielsen\*, Keehoon Kang\*, Sungjune Jung\*. "High mobility amorphous polymer-based 3D stacked pseudo logic circuits through precision printing". *Advanced Functional Materials 34, 2312922 (2024)*.
- Sangmoon Han†, Justin S. Kim†, Eugene Park†, Yuan Meng, Zhihao Xu, Alexandre C Foucher, Gwan Yeong Jung, Ilpyo Roh, Sangho Lee, Sun Ok Kim, Ji-Yun Moon, Seung-Il Kim, Sanggeun Bae, Xinyuan Zhang, Bo-In Park, Seunghwan Seo, Yimeng Li, Heechang Shin, Kate Reidy, Anh Tuan Hoang, Suresh Sundaram, Phuong Vuong, Chansoo Kim, Junyi Zhao, Jinyeon Hwang, Chuan Wang, Hyungil Choi, Dong-Hwan Kim, Jimin Kwon, Jin-Hong Park, Abdallah Ougazzaden, Jae-Hyun Lee, Jong-Hyun Ahn, Jeehwan Kim, Rohan Mishra, Hyung-Seok Kim, Frances M Ross\*, Sang-Hoon Bae\*. "High energy density in artificial heterostructures through relaxation time modulation". *Science 384, 312-317 (2024)*.
- Hyunjin Park\*, Jimin Kwon, Jihyung Seo, Kiho Kim, Yun Ho Kim, Sungjune Jung\*. "Flexible field-effect transistors with high-quality and uniform single-layer graphene for high mobility". *Semiconductor Science and Technology 39, 04LT01 (2024)*.
- Shuhan Liu, Robert M. Radway, Xinxin Wang, Jimin Kwon, Caroline Trippel, Philip Livis, Subhasish Mitra, H.-S. Philip Wong. "Future of memory: massive, diverse, tightly integrated with compute ― from device to software". *2024 70th IEEE International Electron Devices Meeting (IEDM)*.
- Nahyeon Kim (Presenter), Haksoon Jung, Yongwoo Lee, Sungmin Eum, Yechan Han, Hyunjin Park, Yunsik Park, Jimin Kwon\*. "Micro-3D-printed packaging substrates with embedded through holes for organic interposers". *2024 74th IEEE Electronic Components and Technology Conference (ECTC)*.

**2023**

- Alwin Daus, Lauren Hoang, Carlo Gilardi, Sumaiya Wahid, Jimin Kwon, Shengjun Qin, Jung-Soo Ko, Mahnaz Islam, Aravindh Kumar, Kathryn M Neilson, Krishna C Saraswat, Subhasish Mitra, H-S Philip Wong, Eric Pop\*. "Effect of back-gate dielectric on indium tin oxide (ITO) transistor performance and stability". *IEEE Transactions on Electron Devices 70, 5685-5689 (2023)*.
- Young-Shin Kim, Hoimin Kim, Taewoong Yoon, Min-Jae Kim, Jiyun Lee, Hansol Lee, Dongki Lee, Young Jae Song, Jimin Kwon, Sae Byeok Jo, Jeong Ho Cho, Seung Goo Lee, Boseok Kang\*. "Latent and controllable doping of stimuli-activated molecular dopants for flexible and printable organic thermoelectric generators". *Chemical Engineering Journal 470, 144129 (2023)*.
- Sumaiya Wahid, Alwin Daus, Jimin Kwon, Shengjun Qin, Jung-Soo Ko, H-S Philip Wong, Eric Pop\*. "Effect of top-gate dielectric deposition on the performance of indium tin oxide transistors". *IEEE Electron Device Letters 44, 951-954 (2023)*.
- Sanghoon Baek, Hiroyuki Matsui, Taisei Mano, Ju An Park, Youngmin Jo, Yongwoo Lee, Shizuo Tokito, Jimin Kwon\*, Sungjune Jung\*. "Dual-gate thin film transistor lactate sensors operating in the subthreshold regime". *Biosensors and Bioelectronics 222, 114958 (2023)*.
- Seongmin Heo†, Jimin Kwon†, Mingi Sung, Seunglok Lee, Yongjoon Cho, Haksoon Jung, Insang You, Changduk Yang\*, Junghoon Lee\*, Yong-Young Noh\*. "Large transconductance of electrochemical transistors based on fluorinated donor-acceptor conjugated polymers". *ACS Applied Materials & Interfaces 15, 1629-1638 (2023)*.
- Woojo Kim, Jimin Kwon\*, Sungjune Jung\*. "3D integration of flexible and printed electronics: integrated circuits, memories, and sensors". *Journal of Flexible and Printed Electronics 2, 199-210 (2023) (국내)*.

**2022**

- Noh-Hwal Park, Eun Sol Shin, Gi-Seong Ryu, Jimin Kwon, Dongseob Ji, Hyunjin Park, Yun Ho Kim, Yong-Young Noh\*. "High performance carbon nanotubes thin film transistors by selective ferric chloride doping". *Journal of Information Display 24, 109-118 (2022)*.
- Sanghoon Baek†, Youngoh Lee†, JinHyeok Baek, Jimin Kwon, Seongju Kim, Seungjae Lee, Karl-Philipp Strunk, Sebastian Stehlin, Christian Melzer, Sung-Min Park\*, Hyunhyub Ko\*, Sungjune Jung\*. "Spatiotemporal measurement of arterial pulse waves enabled by wearable active-matrix pressure sensor arrays". *ACS Nano 16, 368-377 (2022)*.
- Lauren Hoang, Alwin Daus, Sumaiya Wahid, Jimin Kwon, Jung-Soo Ko, Shengjun Qin, Mahnaz Islam, Krishna C Saraswat, H-S Philip Wong, Eric Pop\*. "Bias stress stability of ITO transistors and its dependence on dielectric properties". *2022 Device Research Conference (DRC)*.
- Sumaiya Wahid, Alwin Daus, Jimin Kwon, Shengjun Qin, Jung-Soo Ko, Krishna C Saraswat, H-S Philip Wong, Eric Pop\*. "First demonstration of top-gated ITO transistors: effect of channel passivation". *2022 Device Research Conference (DRC)*.
- Shengjun Qin, Maryann Tung, Emma Belliveau, Shuhan Liu, Jimin Kwon, Wei-Chen Chen, Zizhen Jiang, S Simon Wong, H-S Philip Wong\*. "8-layer 3D vertical Ru/AlOxNy/TiN RRAM with mega-ohm level LRS for low power and ultrahigh-density memory". *2022 IEEE Symposium on VLSI Technology and Circuits (VLSI)*.

**2021**

- Jimin Kwon\*, Sanghoon Baek, Yongwoo Lee, Shizuo Tokito, Sungjune Jung\*. "Layout-to-bitmap conversion and design rules for inkjet-printed large-scale integrated circuits". *Langmuir 37, 10692-10701 (2021)*.
- Byullee Park, Seunghyun Lee, Jimin Kwon, Woojo Kim, Sungjune Jung\*, Chulhong Kim\*. "Dual-pulse photoactivated atomic force microscopy". *Scientific Reports 11, 17097 (2021)*.
- Woojo Kim, Jimin Kwon, Yasunori Takeda, Tomohito Sekine, Shizuo Tokito, Sungjune Jung\*. "Flexible and printed organic nonvolatile memory transistor with bilayer polymer dielectrics". *Advanced Materials Technologies 6, 2100141 (2021)*.
- Youngmin Jo, Jimin Kwon, Jan-Laurens van der Steen, Auke Jisk Kronemeijer, Sungjune Jung\*. "Programmable a-InGaZnO gate array with laser-induced forward transfer". *Flexible and Printed Electronics 6, 015014 (2021)*.
- RM Radway, K Sethi, W-C Chen, Jimin Kwon, S Liu, TF Wu, E Beigne, MM Shulaker, H-SP Wong, S Mitra\*. "The future of hardware technologies for computing: N3XT 3D MOSAIC, illusion scaleup, co-design". *2021 IEEE International Electron Devices Meeting (IEDM)*.

## 학회 발표와 초청 강연

누리집 Presentations & Talks 절의 초청 강연·튜토리얼 11건 전부(2023–2026년), International Conferences 28건 가운데 2021–2026년 24건에서 위 학회 논문집 목록과 제목이 같은 16건을 뺀 8건, Domestic Conferences 38건 전부(2024–2026년)다. 제목·발표자·학회 이름은 누리집 표기 그대로다. 2026년 4월 KAIST 부임 전 UNIST 시기의 발표가 섞여 있다.[^talks][^pi]

**초청 강연·튜토리얼**

- 2026 · Signal integrity challenges and opportunities in high-density chiplet I/O on glass substrates · Jimin Kwon, Yurim Choi · 2026 International Conference on Electronics Packaging joined with Hybrid Bonding Symposium (ICEP-HBS 2026)
- 2026 · Ultrahigh-bandwidth, and ultrahigh-capacity memory system using high-cooling-efficiency 3.5D vertical-die packaging · Jimin Kwon · 한국마이크로전자패키징학회 (KMEPS 2026 정기학술대회)
- 2026 · High-bandwidth interconnects enabled by EHD printing on glass substrates · Jimin Kwon · 한국유연인쇄전자학회 (KFPE 2026 춘계)
- 2025 · High-speed mixed ionic-electronic active devices for bio- and RF signal processing · 이용우, 정성준, 권지민 · 한국유연인쇄전자학회 (KFPE 2025 추계)
- 2025 · (Tutorial) Glass chiplet interposer packaging: from material innovation to system integration · Jimin Kwon · 대한전자공학회 (IEIE 2025 하계)
- 2025 · Novel through-hole interconnect technologies for 3D printed fanout interposer substrates · 정학순, 김나현, 권지민 · 한국유연인쇄전자학회 (KFPE 2025 춘계)
- 2024 · (Invited Talk) Direct-printing more components onto large-area and 3D electronics · Jimin Kwon · The 21th International Symposium on the Physics of Semiconductors and Applications (ISPSA 2024)
- 2024 · (Invited Talk) Heterogeneous integration technology development: monolithic 3D integration and advanced packaging · Jimin Kwon · 2024 Asia-Pacific Workshop on Advanced Semiconductor Devices (AWAD 2024)
- 2024 · (Invited Talk) Additively manufactured packaging substrates for fan-out interposers · Jimin Kwon · The 21th International SoC Design Conference (ISOCC 2024)
- 2024 · (Tutorial) Advanced packaging and new opportunities for additive manufacturing · Jimin Kwon · International Conference On Consumer Electronics Asia 2024 (ICCE-Asia 2024)
- 2023 · (Invited Talk) 단일3차원집적, 이종집적을 위한 반도체소자·패키지 제작 · Jimin Kwon · 한국세라믹학회 추계학술대회 (2023 Fall Meeting of the Korean Ceramic Society)

**국제 학회 발표(학회 논문집 목록에 없는 것)**

- 2025 · Sulfur vacancy repair in MoS2 using electron-withdrawing benzenethiol · Haksoon Jung, Mingyu Kim, Yongwoo Lee, Gi Beom Sim, Hyeonho Gu, Sumin Hong, Sanghyun Lee, Jaehyun Lee, Donghyeop Lee, Taoyu Zou, Kibum Kang, Chang Woo Myung, Yong-Young Noh, Jimin Kwon\* · 2025 MRS Fall Meeting
- 2025 · Radio-frequency signal transmission in organic mixed ionic-electronic conductors · Yongwoo Lee, Hyeongjun Kim, Kyungsun Kim, Haksoon Jung, Seongju Kim, Yurim Choi, Sungmin Eum, Jimin Kwon\* · 2025 MRS Fall Meeting
- 2025 · 3D-printed organic interposer with embedded fan-out interconnects enabled by additive manufacturing · 정학순, 권지민 · Korean International Semiconductor Conference on Manufacturing Technology 2025 (KISM 2025)
- 2025 · Development of silver EHD jet printing design rules for reliable RF component fabrication · Hyeongjun Kim, Yongwoo Lee, Seongju Kim, Jimin Kwon · International Symposium on Microelectronics and Packaging 2025 (ISMP 2025)
- 2025 · Radio-frequency carbon nanotube field-effect transistors on glass substrates · Sungmin Eum, Yehyun Shin, Seunghun Baek, Yurim Choi, Kyungsun Kim, Haksoon Jung, Yongwoo Lee, Jimin Kwon · International Symposium on Microelectronics and Packaging 2025 (ISMP 2025)
- 2025 · Continuous-time linear equalization based on organic mixed ionic-electronic conductors · Yongwoo Lee, Hyeongjun Kim, Yurim Choi, Kyungsun Kim, Haksoon Jung, Sungmin Eum, Seongju Kim, Jimin Kwon\* · International Symposium on Microelectronics and Packaging 2025 (ISMP 2025)
- 2025 · Reinforcement learning-driven custom liquid micro-channel design for direct liquid cooling in advanced packaging · Seongju Kim, Jimin Kwon\* · International Symposium on Microelectronics and Packaging 2025 (ISMP 2025)
- 2025 · Advanced interconnect design in 3D-printed fan-out interposers · Haksoon Jung, Jimin Kwon\* · International Symposium on Microelectronics and Packaging 2025 (ISMP 2025)

**국내 학회 발표**

- 2026 · Robust CPW-coaxial transition structures for 3D-printed AiP substrate embedding RF components · 김경선, 김나현, 정학순, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2026)
- 2026 · High-resolution ceramic 3D printing using multidose strategies for liquid cooled flip-chip power packaging · 정학순, 김성주, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2026)
- 2026 · Adaptive RF signal control using mixed ionic-electronic devices for antenna tuning and channel equalization · 이용우, 김형준, 김경선, 정학순, 음성민, 최유림, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2026)
- 2026 · Electrohydrodynamic jet-printed coplanar waveguide transmission lines for UCIe-based high-speed heterogeneous systems · 김형준, 이용우, 김성주, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2026)
- 2026 · Automated optical detection and thickness estimation of 2D flakes for large-scale FET data acquisition · 이상현, 정학순, 홍수민, 박민호, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Effect of seed-layer morphology on dielectric and device performance in MoS2 field-effect transistors · 홍수민, 정학순, 이상현, 박민호, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Study of substrate-dependent signal integrity in chiplet systems · 최유림, 이용우, 정학순, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Optimized FlipFET standard cell design for reduced gate delay and improved routability · 위동진, 박민호, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · 3D-printed 28-GHz antenna-in-package lid substrate featuring 50-ohm quasi-coaxial through-vias · 김나현, 정학순, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Buried electrostatic doping using nonstoichiometric silicon nitride for scaled n-type MOSFET-like CNFETs enabling high on/off ratio · 백승훈, 정학순, 신예현, 음성민, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · T-shaped gate high frequency carbon nanotube field-effect transistors on glass substrates · 음성민, 신예현, 백승훈, 이용우, 정학순, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Understanding the interfaces in dimension-limited self-alignment for highly ordered carbon nanotube monolayers · 신예현, 음성민, 정학순, 백승훈, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Design rule development of electrohydrodynamic jet printing for UCIe based high-speed interconnections · 김형준, 이용우, 김성주, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Scaling characteristics of oxide-based vertical channel transistors for gain-cell memory · 구현호, 정학순, 박민호, 이현진, 이용우, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Fan-out 3D-printed packages with embedded curved through-hole interconnections · 정학순, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · Mixed ionic-electronic conductors-based radio-frequency switches with interdigitated channel · 이용우, 김형준, 김경선, 정학순, 최유림, 음성민, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2026 · 3D-printed AiP lid substrates with coaxial through-via feeds for improved high-frequency signal integrity · 김경선, 김나현, 정학순, 이용우, 권지민 · 한국반도체학술대회 (KCS 2026)
- 2025 · 균일한 Cu pillar 범프 형성을 위한 잉크젯 프린팅 포토레지스트 도포 공정 개발 · 최유림, 김성주, 이용우, 정예린, 권지민 · 2025 한국전기전자재료학회 하계학술대회
- 2025 · 강화학습을 통한 첨단 반도체 패키징에서의 냉각 채널 최적 설계 · 김성주, 권지민 · 2025 한국전기전자재료학회 하계학술대회
- 2025 · 마이크로스트립 구조를 이용한 유리 기판의 복소 유전율 측정 · 김경선, 최유림, 정학순, 권지민 · 2025 한국전기전자재료학회 하계학술대회
- 2025 · 고정밀 마이크로 스케일 RF 부품 제작에서 전기 수력학 프린팅 기술의 디자인 룰 개발 · 김형준, 이용우, 김성주, 권지민 · 2025 한국전기전자재료학회 하계학술대회
- 2025 · 첨단 반도체 패키징을 위한 3D 프린팅 유기 팬아웃 기판 · 정학순, 김나현, 권지민 · 2025 한국전기전자재료학회 하계학술대회
- 2025 · Fabrication of quasi-coaxial through-hole embedded substrate for antenna-in-package using 3D printing · 김나현, 정학순, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2025)
- 2025 · Curved through-holes in 3D-printed fanout organic interposer substrate · 정학순, 김나현, 권지민 · 한국마이크로전자 및 패키징학회 (KMEPS 2025)
- 2025 · Fabrication of RF transmission lines and antenna using EHD inkjet printing · 김형준, 이용우, 권지민 · 한국유연인쇄전자학회 (KFPE 2025 춘계)
- 2025 · 3D-printed quasi-coaxial through-hole embedded substrate for antenna-in-package applications · 김나현, 정학순, 권지민 · 한국유연인쇄전자학회 (KFPE 2025 춘계)
- 2025 · 3D-printed antenna-in-package substrates with quasi-coaxial through-vias for 5G-advanced applications · 김나현, 정학순, 최유림, 이용우, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Inkjet-printed photoresist films for panel-level packaging using glass interposers · 최유림, 이용우, 정학순, 김나현, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Atomic layer deposition for high-mobility and reliable ITZO thin film transistors · 이현진, 구현호, 박민호, 이용우, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Top-gate carbon nanotubes field-effect transistors with buried extension gates for electrostatic doping · 음성민, 신예현, 백승훈, 정학순, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Bundle-free aligned semiconductor carbon nanotubes for field-effect transistors · 신예현, 음성민, 정학순, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Achieving low leakage current in carbon nanotube field-effect transistors using an extension doping layer · 백승훈, 음성민, 신예현, 정학순, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Top-gate oxide semiconductor FETs for reliable 2T0C read/write operation with reduced capacitive coupling · 박민호, 구현호, 이현진, 이용우, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · Interlayer dielectric engineering in vertical-channel ITO field-effect transistors for bias-reliable operation · 구현호, 박민호, 이현진, 이용우, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2025 · 3D-printed organic substrates for low-cost, re-distribution-layer-less fanout interposers · 정학순, 김나현, 권지민 · 한국반도체학술대회 (KCS 2025)
- 2024 · 게이트 절연막 시드층 최적화를 통한 상부 게이트 MoS2 전계효과트랜지스터 제작 · 홍수민, 구현호, 박민호, 정학순, 권지민 · 한국유연인쇄전자학회 (KFPE 2024 추계)
- 2024 · 정렬 탄소나노튜브 채널 전계효과트랜지스터를 위한 탄소나노튜브 번들 제거 공정 · 신예현, 음성민, 정학순, 권지민 · 한국유연인쇄전자학회 (KFPE 2024 추계)
- 2024 · 패널패키징을 위한 잉크젯 포토레지스트 Cu Bump 공정 개발 · 최유림, 이용우, 권지민 · 한국유연인쇄전자학회 (KFPE 2024 추계)

## 특허

누리집 Patents 절 56건 가운데 2021–2026년 연도 구역의 50건([007]–[056], 2023–2026년)이다. 제목·발명자·출원번호·등록번호·상태(filed는 출원, registered는 등록)는 누리집 표기 그대로이고, 상태가 비어 있는 항목은 누리집에 상태 표기가 없는 것이다. 교수 개인의 특허 목록이어서 2026년 4월 KAIST 부임 전 출원이 섞여 있으며, 모두 현재 KAIST 연구실의 성과로 묶지 않는다.[^patents][^pi]

- 2026 · 수직 다이 패키징 기술 개발 (발명자 권지민, 정학순; 출원번호 10-2026-0082967 (가출원); 상태 filed)
- 2026 · 나노 물질 광학 특성 분석을 이용한 반도체 소자 레이아웃 자동 생성 방법 및 장치 (발명자 권지민, 이상현, 정학순, 이용우; 출원번호 10-2026-0052953; 상태 filed)
- 2026 · 반도체소자 및 반도체소자의 패터닝방법 (발명자 권지민, 정학순; 출원번호 10-2026-0058387; 상태 filed)
- 2026 · 반도체소자 및 반도체소자의 패터닝방법 (발명자 권지민, 정학순; 출원번호 10-2026-0058388; 상태 filed)
- 2025 · Stretchable thin film transistor, stretchable panel, and electronic device (발명자 G. H. Lee, …, H. Jung; 출원번호 202510819824.X(CN); 상태 filed)
- 2025 · 게이트 절연층을 포함하는 수직 구조의 트랜지스터 및 그 제조 방법 (발명자 권지민, 이현진, 정학순, 박민호, 이용우; 출원번호 2025-183947(JP); 상태 filed)
- 2025 · 인공 지능 모델에 기반한 반도체 구조물의 방열 구조를 최적화하기 위한 전자 장치, 및 그 동작 방법 (발명자 권지민, 정학순, 김성주; 출원번호 2025-187821(JP); 상태 filed)
- 2025 · Apparatus for customized semiconductor packaging, server, system and operation method of the same (발명자 J. Kwon, H. Jung; 출원번호 24216097.6(EU); 상태 filed)
- 2025 · Material for a substrate for electrical connection and substrate for electrical connection between electronic components (발명자 J. Kwon, H. Jung; 출원번호 24218377.0(EU); 상태 filed)
- 2025 · Apparatus for forming interconnect structures inside a substrate formed based on 3D printing, and process method of the same (발명자 J. Kwon, H. Jung; 출원번호 24218381.2(EU); 상태 filed)
- 2025 · Structure combined with a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 24218382.0(EU))
- 2025 · Chip-let package including a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 24218385.3(EU); 상태 filed)
- 2025 · Antenna package including a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 24218387.9(EU))
- 2025 · Vertical transistor including gate insulating layer and manufacturing method thereof (발명자 J. Kwon, H. Lee, H. Jung, M. Park, Y. Lee; 출원번호 25212389.8(EU); 상태 filed)
- 2025 · Electronic device for optimizing heat dissipation structure of semiconductor structure based on artificial intelligence model, and operating method thereof (발명자 J. Kwon, H. Jung, S. Kim; 출원번호 25213729.4(EU); 상태 filed)
- 2025 · Apparatus for customized semiconductor packaging, server, system and operation method of the same (발명자 J. Kwon, H. Jung; 출원번호 18; 상태 filed)
- 2025 · Material for producing a semiconductor packaging structure based on 3D printing (발명자 J. Kwon, H. Jung; 출원번호 18; 상태 filed)
- 2025 · Apparatus for forming interconnect structures inside a substrate formed based on 3D printing, and process method of the same (발명자 J. Kwon, H. Jung; 출원번호 18; 상태 filed)
- 2025 · Structure combined with a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 18)
- 2025 · Chip-let package including a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 18; 상태 filed)
- 2025 · Antenna package including a substrate for semiconductor packaging formed based on 3DP, and an electronic device including the same (발명자 J. Kwon, H. Jung; 출원번호 18)
- 2025 · Stretchable thin film transistor, stretchable panel, and electronic device (발명자 G. H. Lee, …, H. Jung; 출원번호 19; 상태 filed)
- 2025 · Vertical transistor including gate insulating layer and manufacturing method thereof (발명자 J. Kwon, H. Lee, H. Jung, M. Park, Y. Lee; 출원번호 19; 상태 filed)
- 2025 · Electronic device for optimizing heat dissipation structure of semiconductor structure based on artificial intelligence model, and operating method thereof (발명자 J. Kwon, H. Jung, S. Kim; 출원번호 19; 상태 filed)
- 2025 · 수직채널 반도체 소자 및 그 제조 방법 (발명자 권지민, 구현호, 박민호, 이용우; 출원번호 10-2025-0002761; 상태 registered)
- 2025 · 게이트 절연층을 포함하는 수직 구조의 트랜지스터 및 그 제조 방법 (발명자 권지민, 이현진, 정학순, 박민호, 이용우; 출원번호 10-2025-0002764; 상태 registered)
- 2025 · 이온 게이트 박막 트랜지스터를 포함하는 반사 부재 전자 장치 및 그 동작 방법 (발명자 권지민, 이용우, 정학순; 출원번호 10-2025-0005699; 상태 registered)
- 2025 · 이온 박막 트랜지스터에 기반한 RF 신호의 반사 조절을 위한 전자 장치 및 그 동작 방법 (발명자 권지민, 이용우, 정학순; 출원번호 10-2025-0005702; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 반도체 패키징 구조물을 제조하기 위한 소재 (발명자 권지민, 정학순; 출원번호 10-2025-0071064; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 고객 맞춤형 반도체 패키징 용 구조물을 제공하는 서버, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 10-2025-0071066; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 패턴 형성을 위한 전자 장치, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 10-2025-0071068; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 생성된 기판 내부에 인터커넥트 구조를 형성하기 위한 장치, 및 그 제조 방법 (발명자 권지민, 정학순; 출원번호 10-2025-0071073; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판과 결합된 구조물, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 10-2025-0071074)
- 2025 · 3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판을 포함하는 칩-렛 패키지, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 10-2025-0071080; 상태 registered)
- 2025 · 3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판을 포함하는 안테나 패키지, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 10-2025-0071081; 상태 filed)
- 2025 · 3D 프린팅 기반 반도체 패키징을 위한 설계 기능을 제공하는 서버, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 10-2025-0071085; 상태 registered)
- 2025 · 도면 파일에 기반하여 반도체 패키징 용 구조물을 생성하기 위한 인쇄 파일을 생성하기 위한 서버, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 10-2025-0071086; 상태 filed)
- 2025 · 인공 지능 모델에 기반한 반도체 구조물의 방열 구조를 최적화하기 위한 전자 장치, 및 그 동작 방법 (발명자 권지민, 정학순, 김성주; 출원번호 10-2025-0162475; 상태 filed)
- 2025 · 칼코젠 결함 회복을 위한 처리제 및 이를 이용한 칼코젠 결함 회복 방법 (발명자 권지민, 정학순, 이철호; 출원번호 10-2025-0181227; 상태 filed)
- 2025 · 기상 증착 장치 및 이를 이용한 칼코젠 결함 회복 방법 (발명자 권지민, 정학순, 이철호; 출원번호 10-2025-0181247; 상태 filed)
- 2025 · 클록 분배망의 독립적 배선 구조를 이용한 클록 신호 및 로직 신호의 완전 분리형 반도체 장치 및 시스템 (발명자 권지민, 박희천, 박민호, 신예현, 김익겸; 출원번호 10-2025-0194458; 상태 filed)
- 2024 · 3D 프린팅 기반 소비자 맞춤형 반도체 패키징을 위한 장치, 서버, 시스템, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 2024-207709(JP); 상태 filed)
- 2024 · 3D 프린팅에 기반하여 반도체 패키징 구조물을 생성하기 위한 소재 (발명자 권지민, 정학순; 출원번호 2024-221471(JP); 상태 filed)
- 2024 · 3D 프린팅에 기반하여 형성된 기판 내부의 인터커넥트 구조를 형성하기 위한 장치, 및 공정 방법 (발명자 권지민, 정학순; 출원번호 2024-221476(JP); 상태 filed)
- 2024 · 3DP에 기반하여 형성된 반도체 패키징 용 기판을 포함하는 칩-렛 패키지, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 2024-221477(JP); 상태 filed)
- 2024 · 3DP에 기반하여 형성된 반도체 패키징 용 기판과 결합되는 구조물, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 2024-221492(JP); 상태 filed)
- 2024 · 3DP에 기반하여 형성된 반도체 패키징 용 기판을 포함하는 안테나 패키지, 및 이를 포함하는 전자 장치 (발명자 권지민, 정학순; 출원번호 2024-221495(JP); 상태 filed)
- 2024 · 연신 박막 트랜지스터, 연신 패널 및 전자 장치 (발명자 이계황, 권지민, 노용영, 강현범, 김형준, 김민규, 정학순; 출원번호 10-2024-0080521; 상태 filed)
- 2024 · 고해상도 유기 발광 소자 픽셀 패턴의 제조방법 및 그에 의해 제조된 고해상도 유기 발광 소자 픽셀 패턴 (발명자 권지민, 정학순; 출원번호 10-2024-0202220; 상태 registered)
- 2023 · 3D 프린팅 기반 소비자 맞춤형 반도체 패키징을 위한 장치, 서버, 시스템, 및 그 동작 방법 (발명자 권지민, 정학순; 출원번호 10-2023-0170852; 상태 registered)

## 소식

누리집 News 페이지의 글 38건 전부(2023년 9월–2026년 9월)다. 날짜와 제목은 누리집 영문 표기 그대로다. 2026년 2월까지의 글 24건은 교수가 UNIST에 있던 때의 글이다.[^news][^pi]

- Sep 03, 2026 · [Media Coverage] Turning a Memory Material into a Logic Device: Nature Communications Paper in the News
- Sep 02, 2026 · Dongjin Wi Selected for the NRF Master's Research Fellowship (2026)
- Aug 21, 2026 · Dr. Youngmin Jo Selected for the NRF Basic Research Program B (Inclusive Type)
- Aug 21, 2026 · Dr. Yongwoo Lee Receives Best Poster Award at IMID 2026
- Aug 20, 2026 · [Media Coverage] KAIST Solves 3D Memory Challenges to Boost AI Semiconductor Efficiency
- Aug 18, 2026 · [Front Cover] Oxygen-Tunnel ITO Vertical-Channel Transistors Featured in Advanced Functional Materials
- Jul 24, 2026 · Dr. Yongwoo Lee Selected for the NRF Postdoctoral Researcher Growth Support Program
- Jul 09, 2026 · [Media Coverage] KAIST Develops Automated Sorting Technology for 2D Semiconductors
- Jun 20, 2026 · Dr. Haksoon Jung Published in Advanced Materials 2026
- May 20, 2026 · Hyeonho Gu Published in Advanced Functional Materials
- Apr 20, 2026 · Dr. Yongwoo Lee's Paper Published in Nature Communications
- Apr 06, 2026 · Paper Co-First-Authored by Heesoo Yang and Hyeongjun Kim (Integrated M.S./Ph.D., 2nd year) Accepted to IEEE VLSI Symposium 2026
- Apr 06, 2026 · Sanghyeon Lee Published in Advanced Functional Materials
- Apr 03, 2026 · Hyeongjun Kim Received a Best Presentation Award at KMEPS 2026
- Feb 24, 2026 · Guhyun Ho Received the Graduate School Outstanding Thesis Award
- Feb 24, 2026 · Dr. Haksoon Jung Published in ACS Nano
- Feb 09, 2026 · Guhyun Ho Published in IEEE Electron Device Letters
- Nov 07, 2025 · Hyeongjun Kim Won Best Poster Award at ISMP 2025
- Oct 02, 2025 · Selected for the Samsung Future Technology Program
- Sep 27, 2025 · Dr. Yongwoo Lee Published in Science Advances
- Sep 13, 2025 · Three Papers Accepted to IEEE IEDM 2025
- Aug 28, 2025 · Three Students Selected for the NRF Master's Research Fellowship (2025)
- Aug 06, 2025 · Dr. Seongju Kim Appointed Assistant Professor at Hanbat National University
- Jul 31, 2025 · Selected for the Quantum Core Technology Development Program
- Jul 07, 2025 · Dr. Haksoon Jung Selected for NRF Postdoctoral Growth Program
- Jun 19, 2025 · Dr. Seongju Kim and Dr. Haksoon Jung Received Top Awards at KIEEM 2025
- May 09, 2025 · Minho Park Won a Best Paper Award at KCS 2025
- Mar 21, 2025 · Nahyeon Kim and Hyeongjun Kim Won Best Presentation Awards at KFPE 2025
- Mar 06, 2025 · Nahyeon Kim Won an On-site Best Poster Award at KCS 2025
- Feb 03, 2025 · Dr. Haksoon Jung Published in ACS Nano
- Oct 18, 2024 · Sumin Hong Won a Best Presentation Award at KFPE 2024
- Oct 16, 2024 · Prof. Jimin Kwon Received the KFPE Young Scholar Award
- Aug 29, 2024 · Dr. Yongwoo Lee Selected for the NRF Domestic Postdoctoral Fellowship
- Aug 29, 2024 · Three Students Selected for the NRF Master's Research Fellowship
- Aug 10, 2024 · Dr. Yongwoo Lee and Haksoon Jung Published in IEEE Electron Device Letters
- Jul 18, 2024 · Dr. Yongwoo Lee Published in npj Flexible Electronics
- May 30, 2024 · Nahyeon Kim Presented at ECTC 2024
- Sep 22, 2023 · Selected for the National Semiconductor Laboratory Core Technology Program

## 연락과 위치

- 연구실: KAIST 미래융합소자동(E3-3, Device Innovation Facility) 2302호, 291 Daehak-ro, Yuseong-gu, Daejeon 34141[^contact][^ee]
- 교수 연구실: 미래융합소자동(E3-3) 2304호, 전화 042-350-7485[^ee][^ssep]
- 교수 이메일: jmkwon@kaist.ac.kr[^pi][^ee]
- 누리집 Contact 페이지는 박사과정·석박사통합과정 지원자를 우선 뽑는다고 적고, 기술 개발(TD)·설계·평가(DB)·부품·패키징(CP) 팀의 모집 분야 7개와 학부 개별연구 모집 분야 1개를 안내한다.[^contact][^roles]
[^p1]: J. Lee 외, Y.-Y. Noh, Nature Communications 17, 5901 (온라인 2026-04-30). <https://doi.org/10.1038/s41467-026-72553-y> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: S. Lee 외, J. Kwon, Advanced Functional Materials 36, e32204 (온라인 2026-04-03). <https://doi.org/10.1002/adfm.202532204> 초록 기준.
[^p3]: H. Gu 외, J. Kwon, Advanced Functional Materials 36, e31989 (온라인 2026-05-20). <https://doi.org/10.1002/adfm.202531989> 초록 기준.
[^p4]: H. Jung 외, J. Kwon, Advanced Materials 38, e23703 (온라인 2026-06-30). <https://doi.org/10.1002/adma.202523703> 초록 기준.
[^p5]: H. Yang 외, J. Kwon, 2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), 1-3 (2026). <https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577552> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: K. Kim 외, J. Kwon, 2026 IEEE 76th Electronic Components and Technology Conference (ECTC), 1821-1825 (2026). <https://doi.org/10.1109/ectc51846.2026.00298> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Jung 외, J. Kwon, 2026 IEEE 76th Electronic Components and Technology Conference (ECTC), 1462-1466 (2026). <https://doi.org/10.1109/ectc51846.2026.00240> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: S. Kim, J. Kwon, 2026 International Conference on Electronics Packaging and Hybrid Bonding Symposium (ICEP-HBS), 389-390 (2026). <https://doi.org/10.23919/icep-hbs69241.2026.11550638> 초록 기준(Semantic Scholar 등록 초록).
[^home]: 연구실 누리집 첫 화면(영문·국문) <https://dsil.kaist.ac.kr/> , <https://dsil.kaist.ac.kr/ko/> (연구실 소개, 연구 분야 네 갈래, 2026-10-22 열람)
[^research]: 연구실 누리집 Research 페이지 <https://dsil.kaist.ac.kr/research/> (TD·DB·CP 팀별 연구 주제 소개, 2026-10-22 열람)
[^contact]: 연구실 누리집 Contact 페이지(영문·국문) <https://dsil.kaist.ac.kr/contact/> , <https://dsil.kaist.ac.kr/ko/contact/> (Join Our Lab 소개문, 연구 두 방향, 소속 안내, 모집 분야 목록, 2026-10-22 열람)
[^roles]: 연구실 누리집 Contact 페이지의 모집 분야(Open Roles) 세부 페이지 8쪽 <https://dsil.kaist.ac.kr/contact/positions/vct-based-oxide-dram/> , <https://dsil.kaist.ac.kr/contact/positions/high-performance-logic-devices/> , <https://dsil.kaist.ac.kr/contact/positions/cell-design/> , <https://dsil.kaist.ac.kr/contact/positions/system-level-benchmarking/> , <https://dsil.kaist.ac.kr/contact/positions/advanced-packaging/> , <https://dsil.kaist.ac.kr/contact/positions/rf/> , <https://dsil.kaist.ac.kr/contact/positions/io-circuits/> , <https://dsil.kaist.ac.kr/contact/positions/agent-ai-for-semiconductor-system/> (2026-10-22 열람)
[^pi]: 연구실 누리집 PI 페이지 <https://dsil.kaist.ac.kr/people/pi/> (경력, 학계 활동, 수상, 학력, 이메일, 2026-10-22 열람)
[^members]: 연구실 누리집 People 페이지 <https://dsil.kaist.ac.kr/people/> (2026 Summer·2026 Spring 학기 명단과 구성원 소개, 2026-10-22 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://dsil.kaist.ac.kr/people/alumni/> (Alumni·Intern 칸, 2026-10-22 열람)
[^pubs]: 연구실 누리집 Publications 절 International Journals·Domestic Journals·Conference Proceedings 페이지 <https://dsil.kaist.ac.kr/publications/journal-articles/international-journals/> , <https://dsil.kaist.ac.kr/publications/journal-articles/domestic-journals/> , <https://dsil.kaist.ac.kr/publications/conference-proceedings/> (2026-10-22 열람)
[^patents]: 연구실 누리집 Patents 페이지 <https://dsil.kaist.ac.kr/publications/patents/> (특허 56건, 2026-10-22 열람)
[^talks]: 연구실 누리집 Presentations & Talks 절 Invited Talks·International Conferences·Domestic Conferences 페이지 <https://dsil.kaist.ac.kr/publications/presentations-talks/invited-talks/> , <https://dsil.kaist.ac.kr/publications/presentations-talks/international-conferences/> , <https://dsil.kaist.ac.kr/publications/presentations-talks/domestic-conferences/> (2026-10-22 열람)
[^news]: 연구실 누리집 News 페이지(영문·국문) <https://dsil.kaist.ac.kr/news/> , <https://dsil.kaist.ac.kr/ko/news/> (2023-09–2026-09 글 38건, 2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(권지민) <https://ee.kaist.ac.kr/professor/%ea%b6%8c%ec%a7%80%eb%af%bc/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 디비전, 학위, 2026-10-22 열람)
[^ssep]: KAIST 반도체시스템공학과 교수 명단 <https://sse.kaist.ac.kr/professor/> (연구분야, 연구실, 전화, 2026-10-22 열람)

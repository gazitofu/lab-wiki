# 차세대 패키징 및 박막 연구실 (Advanced Packaging and Thin Films Lab, APTF)

**KAIST 기계공학과·반도체공학대학원·전기및전자공학부(겸임) · 김택수 교수**

- 분야: 반도체 패키지와 박막의 접착·변형·파괴·피로, 기계적 신뢰성, 물성 측정과 수치 해석, 유연 전자소자용 소재·전사 공정
- 대분야: 기계·로봇·제조, 소재
- 태그: 첨단 반도체 패키징[^packaging][^p2], 고체역학·소성[^mechanical][^p1], 전산역학·수치 해석[^fem][^p2], 유연·신축 전자[^p1][^p5], 나노 패터닝·전사[^manufacturing][^p5], 연성 소재·고분자[^p1][^p7], 연료전지[^home][^p6]
- 홈페이지: <https://aptf.kaist.ac.kr/>
- 근거와 출처: [APTF 근거 페이지](aptf-sources.md)

> 반도체 패키지와 얇은 기능성 막이 힘·열·습기를 받을 때 어떻게 변형되고 떨어지거나 부서지는지 측정하고 예측해, 반도체와 유연 전자소자의 신뢰성을 연구하는 연구실이다.[^home][^packaging][^mechanical]

## 무엇을 연구하나

김택수 교수가 이끄는 연구실은 반도체 패키징(칩을 다른 부품이나 칩과 연결하고 보호하는 기술)과 박막(두께가 얇은 물질층)의 역학적 거동을 연구한다. 고분자는 반복 단위가 여러 번 연결된 분자로 이루어진 물질을 뜻한다. 힘을 받는 동안의 변형, 서로 붙어 있는 재료의 접착, 균열과 파괴, 반복 하중으로 손상이 쌓이는 피로를 다룬다. 관심은 기계적 신뢰성(주어진 조건과 기간에 요구된 기능을 유지하는 성질)에 있다. 응용 대상으로 반도체 패키지, 휘어지는 디스플레이, 연료전지(연료와 산화제의 반응으로 화학에너지를 직접 전기에너지로 바꾸는 장치), 태양전지와 배터리, 유연 전자소자를 든다.[^home]

첫째는 **반도체 패키지의 휨과 접합면의 손상**이다. 다른 재료를 함께 쓴 패키지는 제조 과정에서 복잡하게 휘고 내부에 응력(물체 내부에서 단위 면적을 통해 전달되는 힘)이 생길 수 있다. 연구실은 고대역폭 메모리(HBM, High Bandwidth Memory)와 팬아웃 웨이퍼 레벨 패키징(FOWLP, Fan-Out Wafer-Level Packaging: 칩 바깥까지 연결 배선을 펼치는 패키징)의 제조 과정에 나타나는 비선형 휨(변형과 원인의 관계가 단순한 비례식으로 표현되지 않는 휨)을 모형으로 설명한다. 패키지 재료의 힘·온도·습기에 따른 성질과 재료 사이 접착도 측정한다.[^packaging] 대표 논문에서는 여러 층으로 만든 인쇄회로기판(PCB, Printed Circuit Board)이 대각선으로 휘는 문제를 다뤘다. 프리프레그(보강재에 수지를 미리 스며들게 해 둔 중간 재료)의 점탄성(시간에 따라 변형 응답이 달라지는 성질)과 방향별 물성을 측정하고, 이 성질들이 대각선 휨의 주된 원인임을 수치 해석으로 보였다.[^p2] 유한요소법(FEM, Finite Element Method)은 해석 대상을 유한한 수의 요소로 나누고 물리 관계를 근사해 계산하는 방법이다. 연구실은 이를 굽힘, 습기 흡수에 따른 변형, 구리와 그래핀(탄소 원자가 벌집 모양으로 연결된 원자층 물질)의 접착 연구에도 쓴다.[^fem]

둘째는 **박막 자체의 성질과 유연 소자의 내구성**이다. 인장 시험(잡아당기는 힘에 따른 변형과 파괴를 재는 시험), 굽힘 시험, 열팽창 계수(온도 변화당 길이나 부피의 상대적 변화율) 측정을 다룬다. 디지털 영상 상관법(DIC, Digital Image Correlation)은 영상에서 표면 무늬의 움직임을 비교해 변형을 재는 방법이다.[^property] 가열한 액체 위에 박막을 놓는 FOHL(Film on Heated Liquid) 방법으로 고온 인장 시험을 제안했고, 다른 논문에서는 고체 지지체의 영향을 받지 않는 열팽창 계수와 유리전이 온도(분자 운동의 변화로 재료 거동이 바뀌는 전이의 온도)를 함께 측정했다.[^p3][^p4] 유리전이는 결정의 녹음과 구별되는 재료 상태 변화다. 최근에는 공액 고분자(분자 사슬을 따라 전자가 퍼질 수 있는 구조를 가진 고분자) 박막의 분자량(분자 질량의 상대적인 크기)에 따른 신축 소자의 열기계적 신뢰성을 연구했다. 열을 가하는 시험에서 기준 분자량 아래의 막은 균열이 생겼고, 기준을 넘는 막은 소성 변형(힘을 없애도 남는 변형)에 따른 주름을 형성하며 전기가 흐르는 길을 유지했다.[^p1] 반복 굽힘에 따른 전극 파괴, 재료 사이의 들뜸과 기판(막이나 부품을 받치는 바탕)의 파열도 연구한다.[^mechanical]

셋째는 **박막을 옮기고 조립하는 제조 방법**이다. 전사(만들어진 막이나 무늬를 다른 지지체로 옮기는 공정) 과정에서 막을 떼어 내는 속도와 표면의 물 접촉 성질을 조절해 그래핀과 금 박막을 여러 무늬로 옮긴다. 물 표면에서 막을 말아 층별로 조립하는 방법도 개발했다.[^manufacturing] 대표 논문은 진공 압력으로 반도체 미세칩을 선택적으로 떼고 놓는 방법을 제시했다. 여러 진공 통로의 압력을 따로 제어해 서로 다른 반도체 칩을 같은 평면에 조립했으며, 이 전사 방법으로 휘어지는 마이크로 발광다이오드(마이크로 LED, Micro Light-Emitting Diode)와 트랜지스터(전기 신호로 전류 흐름을 조절하는 반도체 소자)를 제작했다.[^p5]

넷째는 **에너지 소자와 부드러운 전자재료의 신뢰성**이다. 이오노머(분자 사슬에 전기를 띤 부분을 일부 포함하는 고분자)가 탄소를 묶어 놓은 전극에서 물이 얼 때 생기는 손상을 연구했다. 열처리로 이오노머의 내부 구조를 바꾸어 물 흡수와 결빙 손상을 줄였고, 연료전지와 물을 전기로 분해하는 장치 등의 저온 내구성을 개선할 전략으로 제시했다.[^p6] 하이드로젤(물을 머금은 분자 그물망 재료) 전자재료에 관한 리뷰에서는 재료 설계와 미세가공(소재에 미세한 구조나 무늬를 만드는 가공), 물성(물질이 지닌 물리적 성질)의 정밀 측정 방법을 함께 다룬다.[^p7]

## 주요 연구 주제

### 1. 반도체 패키지의 휨과 신뢰성

반도체 패키징 공정의 휨과 접합면 손상을 측정하고 해석한다. 다층 인쇄회로기판에서는 재료의 시간 의존적·방향별 성질을 측정해 대각선 휨을 설명했다.[^packaging][^p2]

### 2. 박막의 기계·열 물성과 유연 전자재료

박막을 당기거나 구부릴 때의 반응, 온도에 따른 크기 변화와 상태 변화, 공액 고분자의 분자량에 따른 신축 소자의 내구성을 연구한다. 가열한 액체 위에서 박막을 직접 측정하는 방법과 하이드로젤 전자재료의 설계·가공·측정을 다룬다.[^p1][^p3][^p4][^p7]

### 3. 박막의 선택적 전사와 조립

접착과 진공 압력을 조절해 막과 반도체 미세칩을 원하는 위치로 옮기는 공정을 연구한다. 물 표면에서 막을 말아 층별로 조립하는 방법도 다룬다.[^manufacturing][^p5]

### 4. 에너지 소자용 박막 전극의 내구성

전극 안의 물과 이오노머 구조가 결빙 손상에 미치는 영향을 밝히고, 열처리에 따른 내부 구조 변화로 저온에서의 기계적 내구성을 개선한다.[^p6]

## 대표 논문

김택수 교수가 저자로 참여한 최근 논문 가운데 반도체 패키징, 박막 물성 측정, 나노 전사, 유연·신축 전자재료와 에너지 전극 연구를 고르게 담았다. 연도는 연구실의 논문 구역이며 등록 출판일은 각주에 적었다. 「쉽게 말하면」은 각 논문 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Importance of Molecular Weight of Conjugated Polymer Thin Films on Thermo-mechanical Reliability of Stretchable Organic Semiconductors](https://doi.org/10.1021/acs.chemmater.6c00701) · Chemistry of Materials | 신축성 소자에 쓰는 고분자 박막이 열을 받을 때 분자량에 따라 어떻게 손상되는지 연구했다. 분자량을 달리한 막으로 열을 가하는 시험과 인장 시험, 변형 계산을 수행했다. 기준 분자량 아래의 막은 균열이 나며 전기적 성질이 나빠졌고, 기준을 넘는 막은 힘을 없애도 남는 변형으로 주름을 만들어 전기가 흐르는 길을 유지했다.[^p1] | 첫 저자 Dong Jun Kim, 마지막 저자 Taek-Soo Kim |
| 2 | 2025 | [Effects of Viscoelastic-anisotropic Properties of Prepreg on Diagonal Warpage of Multilayer PCB Substrates](https://doi.org/10.1109/tmat.2025.3572834) · IEEE Transactions on Materials for Electron Devices | 열을 받는 다층 회로기판이 대각선으로 휘는 원인을 재료의 성질에서 찾았다. 기판 재료가 시간에 따라 힘에 반응하는 방식과 방향별 굽힘·열팽창 성질을 측정했다. 이 값을 사용한 유한요소 해석에서 재료의 점탄성과 방향별 물성이 대각선 휨의 주된 원인으로 나타났다.[^p2] | 첫 저자 Chang-Yeon Gu, 마지막 저자 Taek-Soo Kim |
| 3 | 2024 | [Direct Tensile Testing of Free-standing Ultrathin Polymer Films on Liquid Surface at High Temperature](https://doi.org/10.1002/smtd.202401291) · Small Methods | 얇고 잘 깨지는 고분자막을 고체 지지체 없이 높은 온도에서 직접 당겨 성질을 재는 방법을 제안했다. 열에 안정적인 액체 표면을 이용하고, 가열한 액체 위에서 시편의 기존 결함을 없애는 과정을 마련했다. 폴리스타이렌(스타이렌 분자들이 사슬로 이어진 고분자)막 시험에서 온도와 두께에 따른 인장 물성의 변화를 측정했다.[^p3] | Tae-Ik Lee, Ji Hun Kim, Eun Sung Oh, 마지막 저자 Taek-Soo Kim |
| 4 | 2024 | [Evaluating Free Thermal Expansion and Glass Transition of Ultrathin Polymer Films on Heated Liquid](https://doi.org/10.1021/acsami.4c02279) · ACS Applied Materials & Interfaces | 박막을 가열한 액체 위에 띄워 고체 지지체의 간섭 없이 열팽창 계수와 유리전이 온도를 함께 재는 방법을 제안했다. 열에 안정적인 액체 표면으로 막을 옮기고 입체 영상의 표면 무늬 움직임으로 열에 따른 변형을 측정했다. 여러 두께의 폴리스타이렌막을 사용해 방법을 검증했다.[^p4] | Tae-Ik Lee, Ji Hun Kim, Dong Jun Kim, 마지막 저자 Taek-Soo Kim |
| 5 | 2023 | [Universal Selective Transfer Printing via Micro-vacuum Force](https://doi.org/10.1038/s41467-023-43342-8) · Nature Communications | 진공의 흡입력을 선택적으로 조절해 반도체 미세칩을 옮기는 방법을 제시했다. 유리에 만든 구멍과 진공 통로의 압력을 제어해 별도 접착제 없이 칩을 떼고 놓았다. 서로 다른 반도체 칩을 같은 평면에 조립하고, 여러 통로를 따로 제어해 선택적 전사를 수행했다. 이 방법으로 휘어지는 마이크로 LED와 트랜지스터를 만들었다.[^p5] | 첫 저자 Sang Hyun Park, 김택수는 전체 14명 중 13번째, 마지막 저자 Keon Jae Lee |
| 6 | 2025 | [Prevention of Frost-Driven Self-Fracture of Ionomer-Bound Carbon Films by Controlling Freezable Water Domain Size](https://doi.org/10.1002/cey2.70098) · Carbon Energy | 탄소 전극이 얼면서 스스로 갈라지는 손상이 주로 전극을 묶는 이오노머 부분의 물에서 비롯됨을 제시했다. 열처리로 이오노머 구조를 바꾸어 물 흡수를 줄이고, 물이 얼 때 내부 힘이 쌓이는 것을 제한했다. 그 결과 결빙 후에도 전극이 늘어나는 성질을 유지했으며 연료전지 등의 저온 내구성 개선 전략으로 제안했다.[^p6] | Jae-Bum Pyo, Ji Hun Kim, 마지막 저자 Taek-Soo Kim |
| 7 | 2025 | [Hydrogel electronic materials and microfabrication processes for soft electronic applications](https://doi.org/10.1063/5.0261387) · Applied Physics Reviews | 물을 머금고 부드러운 성질을 갖는 하이드로젤을 전자재료로 쓰기 위한 설계와 가공 방법을 정리한 리뷰다. 전도성·반도체성 고분자 재료의 발전, 정밀한 무늬를 만드는 가공, 물리적 성질과 측정 방법을 다룬다. 몸속에 넣는 전자소자와 부드러운 로봇 등의 잠재적 응용을 소개하고 향후 연구 방향을 논의한다.[^p7] | Daeyeon Won, HyeongJun Kim, Taek-Soo Kim, Seung Hwan Ko. 김택수는 교신저자 |

## 교수와 전문 분야

김택수 교수는 연세대학교에서 기계공학 학사(2001), Stanford University에서 기계공학 석사(2006)와 박사(2010)를 받았다. 박사학위 논문은 「Fracture and Diffusion in Nanoporous Thin Films」이다. 2010년 12월 KAIST 기계공학과 조교수로 부임했고, 2015년 3월부터 부교수, 2022년 3월부터 Full Professor로 재직한다고 소개한다.[^people]

반도체공학대학원은 김택수 교수를 기계공학과 소속 교수로 올리고, 전기및전자공학부는 겸임교수로 소개한다.[^semicon][^ee] 연구실이 밝힌 전문 분야는 첨단 패키징과 박막의 접착·변형·파괴·피로와 신뢰성이다.[^home] 최근 논문에서는 패키지 재료의 물성과 휨 해석,[^p2] 액체 위 박막의 직접 측정과 신축 소자의 손상,[^p1][^p3][^p4] 선택적 전사 공정[^p5]을 다룬다. 탄소 전극의 결빙 손상과 하이드로젤 전자재료의 설계·가공·측정에도 참여한다.[^p6][^p7]

## 응용 분야

연구실은 반도체 패키지와 휘거나 접히는 디스플레이, 유연·신축 전자소자, 연료전지와 태양전지, 배터리를 응용 대상으로 적는다.[^home] 대표 논문은 다층 회로기판의 휨, 신축성 반도체의 열에 따른 손상, 휘어지는 반도체 소자 제작과 에너지 전극의 저온 내구성을 다룬다.[^p1][^p2][^p5][^p6] 의생명 응용의 공저에는 조직 표면에 맞춰 변형되는 삽입형 광소자, 얼굴 형태에 맞는 마이크로 LED 마스크, 하이드로젤 기반 삽입형 센서 개발이 있다.[^b09][^b10][^b13]

## 구성원

2026년 10월 31일 연구실 Members의 Student & Postdoc 구획 기준 25명이다. 박사후연구원 3명, 박사과정 12명, 석박사통합과정 2명, 석사과정 8명이다. 시작 시기는 카드의 현 과정 또는 현 직위 시작 표기다. 「대표 논문 참여」는 위 표의 논문 전체 저자 목록에서 같은 이름을 확인한 경우의 번호다.[^people]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 김동준 (Dong Jun Kim) | 박사후연구원 (KAIST InnoCORE PRIMS-AI Center) | 2026. 3 | djkim1@kaist.ac.kr | 1, 4 |
| 양찬희 (Chanhee Yang) | 박사후연구원 (Mechanical Engineering, KAIST) | 2026. 3 | yangch0428@kaist.ac.kr | 2 |
| 송명 (Myoung Song) | 박사후연구원 (KAIST InnoCORE SMI-PAI Center) | 2026. 9 | myoung2506@kaist.ac.kr | 5 |
| 김용휘 (Yonghwi Kim) | 박사과정 | 2022. 9 | yh_kim92@kaist.ac.kr |  |
| 구창연 (Chang-Yeon Gu) | 박사과정 | 2023. 3 | changyeon.gu@kaist.ac.kr | 2 |
| 이선우 (Sun-Woo Lee) | 박사과정 | 2023. 3 | swlee1@kaist.ac.kr |  |
| 오은성 (Eun Sung Oh) | 박사과정 | 2023. 9 | oes0218@kaist.ac.kr | 3 |
| 최원 (Won Choi) | 박사과정 | 2024. 3 | wonchoi1@kaist.ac.kr |  |
| 김도훈 (Dohun Kim) | 박사과정 | 2024. 9 | kdh95@kaist.ac.kr |  |
| 주민상 (Min Sang Ju) | 박사과정 | 2024. 9 | minsang.ju@kaist.ac.kr | 2 |
| 함영석 (Yeong Seok Ham) | 박사과정 | 2024. 9 | ham0531@kaist.ac.kr |  |
| 강원중 (Won Jung Kang) | 박사과정 | 2025. 3 | wonjungk0604@kaist.ac.kr |  |
| 오민호 (Minho Oh) | 석박사통합과정 | 2024. 3 | mhoh2249@kaist.ac.kr | 2 |
| 최민혁 (Min Hyeok Choi) | 박사과정 | 2025. 9 | pushed@kaist.ac.kr |  |
| 성시혁 (Sihyuk Sung) | 박사과정 | 2025. 9 | enature@kaist.ac.kr |  |
| 전태준 (Tae Jun Jeon) | 박사과정 | 2025.9 | taejun.jeon@kaist.ac.kr |  |
| 임동재 (Dongjae Lim) | 석박사통합과정 | 2025. 3 | limdj0512@kaist.ac.kr |  |
| 박민규 (Minkyu Park) | 석사과정 | 2025. 3 | hipaul2@kaist.ac.kr |  |
| 이호진 (Hojin Lee) | 석사과정 | 2025. 3 | hojin1772@kaist.ac.kr |  |
| 전원빈 (Wonbin Jeon) | 석사과정 | 2025. 3 | wonbin54@kaist.ac.kr |  |
| 조규호 (Kyuho Cho) | 석사과정 | 2025. 3 | 99kyuho@kaist.ac.kr |  |
| 정우석 (Woo Seok Jeong) | 석사과정 | 2025.9 | useok20@kaist.ac.kr |  |
| 박찬욱 (Chan Wook Park) | 석사과정 | 2025.9 | chanwook@kaist.ac.kr |  |
| 장호준 (Ho Jun Chang) | 석사과정 | 2026.3 | hojun.chang@kaist.ac.kr |  |
| 김다빈 (Dabin Kim) | 석사과정 | 2026.9 | daqls11@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 31일 연구실 Alumni의 Ph.D. 구획 22명과 M.S. 구획 9명, 모두 31명이다. 학위·기간과 진로는 카드 표기다. Ph.D. 구획의 송형귀는 KAIST 석사와 University of Illinois at Urbana-Champaign 박사로 소개되어 있다. M.S. 구획의 Florian Erdmann은 Dual degree M.S. student로 적혀 있고 학력 기간은 「2011. 4 ~ current」이다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 서정민 (Jeongmin Seo) | Ph.D. in Mechanical Engineering, KAIST, 2012. 2 ~ 2017. 2; M.S. in Mechanical Engineering, KAIST, 2001.3 ~ 2003. 2 | Principal Engineer, Samsung Display, 2018. 3 ~ present | 박사 논문: A Research on Interfacial Adhesion Energy and Transfer Process of Synthesized Graphene; 석사 논문: A study on the intensity-modulated multiplexing technique of fiber bragg grating sensors |
| 고용호 (Yong-Ho Ko) | Ph.D. in Mechanical Engineering, KAIST, 2012. 2 ~ 2017. 2; M.S. in Material Science and Engineering, KAIST, 2004. 3 ~ 2006. 2 | Principal Researcher, Korea Institute of Industrial Technology, 2010. 2 ~ present | 박사 논문: Interfacial Characteristics of Solder Joint in Electronic Packaging: Applications of Graphene and Flexible Substrate; 석사 논문: A Study on Correlation between Interfacial Reaction and Mechanical Reliability of Pb-free Solder Joint |
| 윤태식 (Taeshik Yoon) | Ph.D. in Mechanical Engineering, KAIST, 2013. 3 ~ 2017. 2; M.S. in Mechanical Engineering, KAIST, 2011. 2 ~ 2013. 2 | Senior Researcher, Standard Energy, 2020. 8 ~ present | 박사 논문: Evaluation and Healing of Graphene Defects; 석사 논문: Adhesion Energy Measurement and Interfacial Reliability Evaluation of Synthesized Graphene |
| 김재한 (Jae-Han Kim) | Ph.D. in Mechanical Engineering, KAIST, 2013. 9 ~ 2017. 2; M.S. in Mechanical Engineering, KAIST, 2011. 9 ~ 2013. 8 | Senior Researcher, Korea Atomic Energy Research Institute, 2017. 3 ~ present | 박사 논문: Mechanical Properties and Reliability of Advanced Energy/Electronics Materials; 석사 논문: Tensile testing of ultra-thin films on water surface |
| 이인화 (Inhwa Lee) | Ph.D. in Mechanical Engineering, KAIST, 2013. 9 ~ 2017. 2; M.S. in Mechanical Engineering, KAIST, 2011. 2 ~ 2013. 2 | Principal Engineer, Samsung Electronics, 2019. 8 ~ present | 박사 논문: Mechanical Properties and Interfacial Reliability of Organic Electronic Materials; 석사 논문: Improving reliability of silver nanoparticle thin films |
| 김산위 (Sanwi Kim) | Ph.D. in Mechanical Engineering, KAIST, 2013. 9 ~ 2017. 8; M.S. in Mechanical Engineering, KAIST, 2011. 9 ~ 2013. 8 | Senior Engineer, SK hynix, 2026.05 ~ present | 박사 논문: Research on Mechanical Behavior and Adhesion of Fuel Cells; 석사 논문: Research on Thin Film Characteristics and Adhesion of Fuel Cell |
| 김철규 (Choelgyu Kim) | Ph.D. in Mechanical Engineering, KAIST, 2014. 3 ~ 2018. 2; M.S. in Mechanical Engineering, KAIST, 2012. 2 ~ 2014. 2 | Senior Engineer, SK hynix, 2026. 05 ~ present | 박사 논문: Analysis and Application of Bending Deformation using Flexible and Soft Substrates; 석사 논문: Methodology Development of Packaging Substrate Warpage Analysis |
| 이태익 (Tae-Ik Lee) | Ph.D. in Mechanical Engineering, KAIST, 2015. 3 ~ 2019. 2; M.S. in Mechanical Engineering, KAIST, 2013. 2 ~ 2015. 2 | Senior Researcher, Korea Institute of Industrial Technology, 2019. 10 ~ present | 박사 논문: Thermo-Mechanical Properties and Bending Reliability of Polymeric Materials for Flexible Electronics; 석사 논문: Mechanical Property Measurement of Thin Polymer Composite Laminates for Warpage Analysis of Packaging Substrates |
| 김완선 (Wansun Kim) | Ph.D. in Mechanical Engineering, KAIST, 2016. 9 ~ 2020. 2; M.S. in Mechanical Engineering, KAIST, 2014. 9 ~ 2016. 8 | Senior Engineer, Samsung Electronics, 2022. 3 ~ present | 박사 논문: Toughening of Semiconducting Polymers for Mechanically-robust, Flexible Electroactive Thin Films; 석사 논문: Study on Mechanical Reliability of Flexible Display Structure Considering Multiple Neutral Planes |
| 장경림 (Kyung-Lim Jang) | Ph.D. in Mechanical Engineering, KAIST, 2016. 3 ~ 2020. 2; M.S. in Mechanical Engineering, KAIST,2014. 3 ~ 2016. 2 | Senior Engineer, Samsung Electronics, 2020. 7 ~ present | 박사 논문: Multi-length Scale Thermo-mechanical Behaviors of Ionomer for Proton Exchange Membrane Fuel Cell; 석사 논문: Quantitative analysis for fracture behavior of fuel cells |
| 표재범 (Jae-Bum Pyo) | Ph.D. in Mechanical Engineering, KAIST, 2016. 3 ~ 2020. 2; M.S. in Mechanical Engineering, KAIST, 2014. 3 ~ 2016. 2 | Associate Professor, Kongju National University, 2026. 3 ~ present | 박사 논문: Hygro-Thermal and Mechanical Behavior of Carbon Based Thin Film Materials for Advanced Energy and Actuator Application; 석사 논문: Research on the measurement of hygroscopic properties and prediction of deformation for flexible polymer substrates |
| 강수민 (Sumin Kang) | Ph.D. in Mechanical Engineering, KAIST, 2017. 3 ~ 2021. 2; M.S. in Mechanical Engineering, KAIST, 2015. 3 ~ 2017. 2 | Assistant Professor, Seoul National University of Science and Technology, 2023. 8 ~ present | 박사 논문: Fracture Behavior and Advanced Transfer Methods of Nanofilms; 석사 논문: Integration of Graphene Electrode on Cylindrical Substrates by Thin Film Rolling Method |
| 이상민 (Sangmin Lee) | Ph.D. in Mechanical Engineering, KAIST, 2017. 3 ~ 2021. 2; M.S. in Mechanical Engineering, KAIST, 2015. 3 ~ 2017. 2 | Senior Engineer, Samsung Electronics, 2021. 10 ~ present | 박사 논문: Research on Mechanical Properties and Fracture Behavior of ALD Thin Films for Flexible Electronics; 석사 논문: Mechanical Property Evaluation and Fracture Behavior Analysis of Brittle Thin Films |
| 조우성 (Woosung Jo) | Ph.D. in Mechanical Engineering, KAIST, 2016. 3 ~ 2021. 8; M.S. in Mechanical Engineering, KAIST, 2014. 3 ~ 2016. 2 | Senior Engineer, Samsung Electronics, 2021. 9 ~ present | 박사 논문: Design of Mechanically and Thermally Robust Foldable Electronics; 석사 논문: Metal Interconnection on Polymer for Steerable Microcatheters |
| 강태엽 (Tae Yeob Kang) | Ph.D. in Mechanical Engineering, KAIST, 2016. 3 ~ 2022. 2; M.S. in Mechanical Engineering, KAIST, 2009. 2 ~ 2011.2 | Assistant Professor, Ajou University, 2026. 3 ~ present | 박사 논문: Reliability assessment on electronic interconnects by S-parameter pattern analysis; 석사 논문: The Effect of Inclination on Impinging Jets at Small Nozzle-to-plate Spacing |
| 마부수 (Boo Soo Ma) | Ph.D. in Mechanical Engineering, KAIST, 2018. 3 ~ 2022. 2; M.S. in Mechanical Engineering, KAIST, 2016. 3 ~ 2018. 2 | Assistant Professor, Suwon University, 2025. 4 ~ present | 박사 논문: Thermo-mechanical behavior of conjugated polymer films for flexible and stretchable organic semiconductors; 석사 논문: A Study on Preotection of Brittle Layers in Rollable Display Structures |
| 송형귀 (Hyunggwi Song) | Ph.D. in Mechanical Engineering, University of Illinois at Urbana-Champaign (UIUC), 2015. 8 ~ 2020. 5; M.S. in Mechanical Engineering, KAIST, 2013. 3 ~ 2015. 2 | Assistant Professor, Chungbuk National University, 2025. 3 ~ present | 박사 논문: The Effect of Mechanical Loading on Bone During Growth; 석사 논문: Modeling dynamics and control mechanism of the swing leg in human walking for motion planning |
| 김준모 (Junmo Kim) | Ph.D. in Mechanical Engineering, KAIST, 2019. 3 ~ 2023. 8; M.S. in Mechanical Engineering, KAIST, 2017. 3 ~ 2019. 2 | Senior Engineer, Samsung Electronics, 2023. 12 ~ present | 박사 논문: Strategy for Reducing Warpage of Electronic Packages by Analyzing Thermo-Mechanical Behavior of Epoxy Molding Compound; 석사 논문: Warpage Prediction of Chip Package Using Simplified Model of PCB Substrate |
| 오승진 (Seung Jin Oh) | Ph.D. in Mechanical Engineering, KAIST, 2020. 3 ~ 2024. 2; M.S. in Mechanical Engineering, KAIST, 2018. 3 ~ 2020. 2 | Senior Researcher, Korea Institute of Machinery & Materials, 2024. 2 ~ present | 박사 논문: Mechanical Behavior of Brittle Thin Film Materials for Advanced Semiconductor and Electronic Applications; 석사 논문: Effects of Post-annealing on Tensile Properties of Indium Tin Oxide Thin Films |
| 김형준 (HyeongJun Kim) | Ph.D. in Mechanical Engineering, KAIST, 2016. 9 ~ 2023. 8; M.S. in Mechanical Engineering, KAIST, 2014. 3 ~ 2016.8 | Senior Engineer, Samsung Electronics, 2024. 6 ~ present | 박사 논문: Adhesion and Mechanical Properties of Wet Conducting Polymer; 석사 논문: ptimal Measuring Points Decision and Welding Process Diagnosis Considering Welding Distortion |
| 안광호 (Kwang Ho Ahn) | Ph.D. in Mechanical Engineering, KAIST, 2019. 3 ~ 2024. 8; M.S. in Mechanical Engineering, KAIST, 2017. 3 ~ 2019. 2 | Senior Engineer, Samsung Electronics, 2024. 9 ~ present | 박사 논문: Hygro-thermal and Mechanical Properties of Electrode for Proton Exchange Membrane Fuel Cell; 석사 논문: Thermal and Mechanical Behaviors of Nafion Thin Film in Hydrated State |
| 김지훈 (Ji Hun Kim) | Ph.D. in Mechanical Engineering, KAIST, 2021. 3 ~ 2024. 8; M.S. in Mechanical Engineering, KAIST, 2018. 3 ~ 2020. 8 | Assistant Professor, Chungbuk National University, 2026. 9 ~ present | 박사 논문: Enhancement of Mechanical Reliability of Nanocarbon Composite Electrode Films through Thermal Reconfiguration; 석사 논문: Highly Mobile Multi-Responsive Soft Actuator Using Diamagnetic Levitation |
| 안건식 (Kunsik Ahn) | Ph.D. in Electrical and Computer Engineering, Seoul National University, 2014. ~ 2018.; M.S. in Mechanical Engineering, KAIST, 2012. 2 ~ 2014.2 | Assistant Professor, Sejong University, 2024. ~ present | 석사 논문: Study on the metal nanoparticles sintering for maskless fabrication of electrode pattern using digital micromirror device |
| Adeel Nizami | M.S. in Mechanical Engineering, KAIST, 2010. 2 ~ 2012. 2 | Professor at the Department of Mechanical Engineering, The University of Lahore | 석사 논문: Development of ultrathin gold film tensile testing by floating specimen on water |
| 박아영 (Ah-Young Park) | Ph.D. in Mechanical Engineering, State University of New York at Binghamton, 2012. 1 ~ 2017. 5; M.S. in Mechanical Engineering, KAIST, 2009. 3 ~ 2011. 2 | Assistant Professor, University of Seoul, 2025. 2 ~ present | 석사 논문: A study on inclined conductive bump for electronic packaging |
| Florian Erdmann | M.S. in Mechanical Engineering, TU Berlin/KAIST, 2011. 4 ~ current |  |  |
| 최혜선 (Hye Sun Choi) | M.S. in Mechanical Engineering, KAIST, 2015. 9 ~ 2017. 8 | Engineer, LG Electronics, 2018. 2 ~ present | 석사 논문: A Research on Mechanical Reliability of Ag Ion Ink Films on Flexible Substrates |
| 조민선 (Min Sun Cho) | M.S. in Mechanical Engineering, KAIST, 2017. 3 ~ 2019.2 | Engineer, SK hynix, 2025.06 ~ present | 석사 논문: Defect Healing of CVD Graphene by Selective Electroplating for Mechanically Robust and Transparent Electrodes |
| 이선우 (Sun Woo Lee) | M.S. in Mechanical Engineering, KAIST, 2020. 3 ~ ~ 2022.2 | Engineer, Samsung Electronics, 2022.3 ~ present | 석사 논문: Effects of W nucleation processes on interfacial reliability of W/TiN/SiO2/Si multilayer structure |
| 정지원 (Jiwon Jeong) | M.S. in Mechanical Engineering, KAIST, 2024. 3 ~ 2026. 2 | Engineer, Samsung Display, 2026.3 ~ present | 석사 논문: Effects of Chemical Strengthening Treatment on Flexural Properties and Young’s Modulus Profile of Ultra Thin Glass (UTG) |
| 김보연 (Boyeon Kim) | M.S. in Mechanical Engineering, KAIST, 2024. 9 ~ 2026. 8 |  |  |

## 최근 논문·발표 목록 (2021–2026)

반도체 패키지의 휨과 접합면, 박막의 기계적 성질과 전사, 늘어나는 태양전지와 디스플레이 소재를 다룬다. 연구실 Publications의 학술지 논문 150편, 국제학회 50건, 국내학회 58건, 모두 258건이다. 제목·저자·발표처·권호는 연구실 표기다. 연도만 적힌 학술지 목록에는 해당 연도 구역을 적용했고, 정확한 출판일이나 학회 날짜가 있는 2021년 항목은 10월 13일 이후를 실었다. 학술지의 Accepted는 「게재 승인」으로 표시했다. 저자 뒤의 별표와 더하기표는 누리집 기호다.[^publications]

**2026**

- B. Oh+, S. Kim+, Y.-S. Lim, C. Gong, S. H. Hong, C. Yang, D. J. Kim, M. Kang, S. Lee, K. S. Nam, J.-W. Jeong, T.-S. Kim, S. Kang, S. Park, S. Hong, S.-M. Park, and S. Park\*. "Vacuum-Processable Hydrogel for Zero-Gauge Factor Stretchable Gold Electronics". *Nature Materials, 게재 승인*.
- E. S. Oh+, D. J. Kim+, W. Choi, and T.-S. Kim\*. "Unveiling the Creep Recovery Behavior of Pseudo Free-Standing Polymer Thin Films for Wearable Electronics". *Nano Letters, Published online*.
- J. H. Kim+, K. Kim+, J. Kim+, E. Kim, M. Park, M. Lee, M. Kim, J. Park, J. Ryu, H. Lee, D. J. Kim, J. C. Yang, J. Pyo, H. T. Hong, T.-S. Kim, H. Kim, H. Lee, S. Kim\*, S. K. Seol\*, and S. Park\*. "Stretchable free-form 3D electronics via on-demand direct conformal printing of liquid metal particles". *Nature Communications, 게재 승인*.
- M.-H. Lee+, S.-J. Hong+, S. Lee+, M. S. Kim, H. Lee, M. Song, D. Kim, D.-H. Kim, T.-S. Kim, J. Kim, J. Seo, J.-Y Lee\*. "Modulus-gradient shear-lag design for robust, high-efficiency intrinsically stretchable perovskite solar cells". *Energy Environ. Sci., 19 (19): 6540–6549*.
- M. Oh+, C. Yang+, C.-Y. Gu, M. S. Ju, D. M. Jang, G.-J. Park, T.-I. Lee\*, and T.-S. Kim\*. "Warpage and Stress Evolution in Double-Sided DRAM During Sequential Reflow". *Journal of Materials Research and Technology, 45, 1343-1355*.
- Y. Kim+, J.-B. Pyo, T. Y. Kang\*, and T.-S. Kim\*. "Radio Frequency Response as a Non-Destructive Readout Associated with Tensile-Strength Degradation in Nanoporous Carbon Electrodes". *Scientific Reports, 게재 승인*.
- J. Yoo, K. Lee+, J. S. Kim+, Y. Kim, C. Park, J. Lee, J. Kim, S.-W. Lee, E. Ahn, S. Jung, J. D. Seo, S. Lee, Y. Kim, G. H. Lee, K. Kim, S. I. Park, D. Yoon, J. Bae, C. Choi, H. Ahn, T.-S. Kim, D. C. Kim\*, D.-H. Kim\*, J. Yang\*, M. K. Choi\*. "High-Resolution Intrinsically Stretchable Quantum-Dot Displays Through Thermally Assisted Intaglio Transfer Printing". *Nature Nanotechnology, 게재 승인*.
- T. Kim, S.-B.Kim, D. Lee, Y. C. Park, W. Lee, S. J. Oh, S. Kim, T.-S.Kim, S. G. Im, J. H. Sim,\* S. yoo\*. "Scalable fabrication of high-EQE stretchable OLEDs enabled by residue controlled laser patterning". *npj Flexible Electronics, 10, 102*.
- J. Lee, S.-W. Lee, T.-S. Kim, D. Kwon\*. "AI-assisted Full-field Warpage Prediction and Optimization for Advanced Packaging". *IEEE Transactions on Components, Packaging and Manufacturing Technology, 게재 승인*.
- S.-B. Kim+, J. Kim+, S. Kim, D. Choi, C.-Y. Gu, T.-S. Kim, H. Moon\*, S. Yoo\*. "Hybrid auxetic metamaterial platforms enabling multiscale isotropic expansion for distortion-free stretchable displays". *Nature Communications, 17, 7389*.
- D. J. Kim, J.-W.Lee, K.Bae, T. Y. Kang, B. S. Ma, B. J. Kim, T.-S. Kim. "Importance of Molecular Weight of Conjugated Polymer Thin Films on Thermo-mechanical Reliability of Stretchable Organic Semiconductors". *Chemistry of Materials, 38(15), 7687-7699*. <https://doi.org/10.1021/acs.chemmater.6c00701>
- C. Yang, M. Oh, M. G. Park, W. Choi, M. S. Ju, H. Song\*, S. K. Lim\*, T.-S. Kim\*. "Deep Learning-Enabled Multiscale Strategy for Rapid and Accurate Warpage Prediction of Interposer Routing Interconnects". *International Journal of Precision Engineering and Manufacturing-Green Technology, 1-14*.
- M. Song, S. J. Oh, S. Suh, T. Y. Kang\*, and T.-S. Kim\*. "Knowledge-guided strain-damage image correlation for diagnosing nonlinear mechanical behavior of freely stretched ultra-thin polymer films on water surface". *Polymer Testing, 109154*.
- S. W. Lee+, D. J. Kim+, J. Jeon, T.-S. Kim\*. "Effect of W nucleation process on the adhesion of W/TiN/SiO2 structures for BEOL interconnects". *Applied Surface Science, 736, 166754*.
- D. Kim, G. Kim, H. Jeong, S. M. Hossain, S. Bhattacharjee, M. J. Kwon, Y. Lee, C. Yang, Y. S. Ham, T.-S. Kim, H. Moon, I. Park, S.-C. Lee, J. Kim, J. Kim, J. Park\*. "Direct Growth of Transparent Boron Nitride Neutron Shielding Layer for Space Window". *Advanced Science, e16390*.
- H. Jeon, J. Oh, J.-W. Lee, H. J. Eun, W. J. Kang, D. H. Ryu, C. E. Song, C. Wang, H. Kang, T.-S. Kim, J. H. Kim, S. Lee\*, B. J. Kim\*. "Strain-Induced Detectivity Enhancement in Intrinsically Stretchable Organic Photodetectors". *Advanced Materials, e14951*.
- C.-Y. Gu, M. H. Choi, M. S. Ju, D. Kim, S. Ma, T.-I. Lee\*, and T.-S. Kim\*. "Nonlinear Warpage Modeling of Dielectric-Controlled Carrier Wafers". *International Journal of Mechanical Sciences, 314(15), 111361*.
- S. H. Kwon, H. Jo, J. Han, Y. S. Ham, T.-S. Kim, M. J. Lee, H.-H. Cho, J. Park\*, and B. J. Kim\*. "Fluorinated Elastomeric Protective Layers with Controlled Solvophobic Properties for Stable Operation of Lithium Metal Batteries". *ACS Energy Letters, 11 (2): 2290–2300*.
- Y. Sim, J. Maeng, M. Oh, W. Choi, T.-S. Kim, E. Hur, Y. Sohn\*. "Study on the interfacial reactions between In-Ag alloys and electroless nickel-immersion gold metallization". *Soldering & Surface Mount Technology, 1-9*.
- E. S. Oh, D. J. Kim, and T.-S. Kim. "Thermomechanical Properties of Free-Standing Polymer Thin Films on an Ionic Liquid Surface at Low Temperatures via a Novel Direct Testing Method". *IUPAC-PSK50, Busan, Korea, Sep. 28 ~ Oct. 1, 2026. (Oral)*.
- D. J. Kim, D. Kim, S. Kang, and T.-S. Kim. "Phase Angle-Induced Transition of Interfacial Delamination in Cu/SiCN Interfaces". *The 4th Global conference of Innovation Materials & MRS-K Spring Meeting, Jeju, Korea, May 31-June 4, 2026. (Poster)*.
- H. J. Chang, D. J. Kim, H. Lee, and T.-S. Kim. "Enhanced Mechanical Properties of PEALD SiO2 Compared to PECVD TEOS-SiO2 for Advanced Electronic Application". *The 4th Global conference of Innovation Materials & MRS-K Spring Meeting, Jeju, Korea, May 31-June 4, 2026. (Poster)*.
- W. J. Kang, and T.-S. Kim. "Substrate Design for Conformal Contact on Non-developable Surfaces". *The 4th Global conference of Innovation Materials & MRS-K Spring Meeting, Jeju, Korea, May 31-June 4, 2026. (Poster)*.
- D. J. Lim, E. S. Oh, H. J. Kim, D. Won, S. H. Ko, and T.-S. Kim. "Enhancement of Thermal Stability through Ethylene Glycol Treatment in Graphene Oxide/PEDOT:PSS Composite Films". *The 4th Global conference of Innovation Materials & MRS-K Spring Meeting, Jeju, Korea, May 31-June 4, 2026. (Poster)*.
- C.-Y. Gu, M. H. Choi, M. S. Ju, D. Kim, S. W. Ma, T.-I. Lee, and T.-S. Kim. "Pre-Bow Strategy for Warpage Control Based on a Nonlinear Warpage Model". *The 4th Global conference of Innovation Materials & MRS-K Spring Meeting, Jeju, Korea, May 31-June 4, 2026. (Poster)*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays and More". *UK-Korea Bilateral International Meeting 2026, London, UK, Mar. 4-5, 2026. (Invited)*.
- 김택수. "차세대 반도체 패키징을 위한 워피지 측정 및 제어 기술". *PHM Korea 2026 정기학술대회, 부산, 2026/06/24-27. (Invited)*.
- 김용휘, 정원용, 표재범, 김택수. "전극 표면 비대칭성과 막 접촉 전극 표면이 연료전지 성능에 미치는 영향". *2026 대한기계학회 신뢰성부문 20주년 기념 학술대회, 제주, 2026/04/08-10. (Oral)*.
- 오은성, 김동준, 김택수. "저온에서의 고분자 박막의 열기계적 물성 직접 측정". *2026 대한기계학회 신뢰성부문 20주년 기념 학술대회, 제주, 2026/04/08-10. (Oral) (우수 논문 발표상)*.
- 김동준, 이선우, 이호진, 김택수. "SiH4및 B2H6환원 가스를 활용한 CVD-W 박막에서 잔류응력과 계면 접합력 간의 상층 관계". *2026 대한기계학회 신뢰성부문 20주년 기념 학술대회, 제주, 2026/04/08-10. (Oral)*.
- 소경현, 김동준, 배기현, 이호진, 장호준, 김범준, 김택수, 마부수. "물리 기반 신경망과 이중외팔보 실험 데이터를 활용한 고분자 박막 파괴 인성 역추정". *2026 대한기계학회 IT지능융합부문, 제주, 2026/04/08-10 (Oral)*.
- 김택수. "차세대 반도체 패키징을 위한 워피지 측정 및 제어 기술". *2026 대한기계학회 신뢰성부문 20주년 기념 학술대회, 제주, 2026/4/8-10 (Invited)*.
- 구창연, 최민혁, 주민상, 김도훈, 마성우, 이태익, 김택수. "비선형 휨 모델 기반 실리콘 웨이퍼의 다이싱 후 휨 예측". *한국마이크로전자 및 패키징학회 2026년 정기학술대회, 인천, 2026/04/01-03 (Oral) (우수 논문 발표상)*.
- 최민혁, 안현성, 배은정, 박영욱, 권정현, 김택수. "두께에 따른 인듐-아연-산화물의 기계적 물성". *한국마이크로전자 및 패키징학회 2026년 정기학술대회, 인천, 2026/04/01-03 (Oral)*.
- 조규호, 김동준, 함영석, 윤지현, 김택수. "가스 방출에 의한 ALD Mo의 구조적 열화 및 접합력 저하: 메커니즘과 Barrier-less 배선 공정 최적화". *한국마이크로전자 및 패키징학회 2026년 정기학술대회, 인천, 2026/04/01-03 (Oral)*.

**2025**

- J. Lee+, C. S. Moon+, Y. Kim, Y. Y. Kim, E. Y. Park, J. J. Yoo, G. Kim, E. S. Oh, T.-S. Kim, S. Song, T. J. Shin, J. H. Noh, N. J. Jeon\*, and J. Seo\*. "Tailored n-Value Engineering of Dion-Jacobson 2D Layers Enables Efficient and Stable Perovskite Solar Cells". *Joule, 10, 3*.
- J. Park, C.-Y Gu, J. Lee, M. Kim, S. Park, T.-S. Kim\*, and K. C. Choi\*. "Stabilization of Electrical Instabilities in Flexible Textile-Based 2T1C Pixel Circuits with a Bottom Shield Metal Structure". *ACS Applied Materials & Interfaces, 17, 52, 70690–70702*.
- D. J. Kim, S. W. Lee, H. Lee, and T.-S. Kim\*. "Effect of Nucleation-Stage Reducing Agents on Residual Stress in CVD Tungsten Thin Films". *IEEE Transactions on Materials for Electron Devices, vol. 3, pp. 1-7*.
- Y. Na, S. Y. Jeong, S. J. Oh, H.-E. Cho, S. Choi, K. S. Kang, Y. Jeon, T.-S. Kim, and K. C. Choi\*. "Truly Wearable OLEDs with Moisture Impermeable and Flexible Textile Substrate Based on Mechanical Analysis of Textile Directionality: Toward Real Cloth-Type Display". *Applied Electronics Materials, 7, 9329−9338*.
- J.-W. Lee†, K. Bae†, D. J. Kim, S. Lee, S. Lee, J.-Y. Lee, T.-S. Kim, and B. J. Kim\*. "Dual-Percolative Planar-Heterojunction Photoactive System for High-Performance Stretchable Organic Photovoltaics Enhancing Power Output Under Strain". *Advanced Functional Materials, e23048*.
- S.Y. Rhee, D.T. Nguyen, S.Y. Han, K. Klementiev, W. Youn, G. Yun, Y. Kwon, S.W. Han, J.H. Kim, T.-S. Kim, V.G. Kessler, H. Lee, G.A. Seisenbaeva and I.S. Choi. "Boric acid-mediated sol–gel construction of transparent, photoactive TiO2 films". *Chemical Communications, 61 (91): 17938–17941*.
- J.-B. Pyo+\*, J. H. Kim+, and T.-S. Kim\*. "Prevention of Frost-Driven Self-Fracture of Ionomer-Bound Carbon Films by Controlling Freezable Water Domain Size". *Carbon Energy, e70098*. <https://doi.org/10.1002/cey2.70098>
- C.-Y. Gu, M. Oh, W. Choi, Y. S. Ham, G.-H. Ju, Y.-H. Yi, J.-H. Lee, and T.-S. Kim\*. "Simultaneous Quantitative Analysis of Large-Area Warpage and Local In-Plane Strain Using 3D-DIC and Stitching Techniques". *J. Microelectron. Packag. Soc., 32(2), pp93-99*.
- D. Won+, H. J. Kim+, T.-S. Kim\*, and S. H. Ko\*. "Hydrogel electronic materials and microfabrication processes for soft electronic applications". *Appl. Phys. Rev., 12, 031302*. <https://doi.org/10.1063/5.0261387>
- J.W. Lee+, J. Oh+, W. J. Kang+, E. S. Oh, S. Lee, I. Lee, J. Park, J. Y. Lee, T.-S. Kim\*, and B. J. Kim\*. "Dual-layered percolative networks of photoactive materials and elastomers for highly-stretchable, efficient organic photovoltaics with strain-induced power enhancement up to 60% strain". *Energy & Environmental Science, 18 (14): 7089–7102*.
- C.-Y. Gu, C. Yang, M. S. Ju, M. Oh, D. M. Jang, J. S. Jang, J. W. Jang, J. K. Kim, and T.-S. Kim\*. "Effects of Viscoelastic-anisotropic Properties of Prepreg on Diagonal Warpage of Multilayer PCB Substrates". *IEEE Transactions on Materials for Electron Devices, vol. 2, pp. 64-71*. <https://doi.org/10.1109/tmat.2025.3572834>
- S.-W. Lee+, M. S. Ju+ and T.-S. Kim\*. "Warpage in Advanced Packaging: Challenges, Measurement Techniques, and Mitigation Strategies for Heterogeneous Integration". *J. Microelectron. Packag. Soc., 32, no.1, pp47-60*.
- D. J. Kim, S. W. Lee, W. Choi, H. J. Chang, I. Lee, S. Park, J. Lee, J. J. Kim, S. Kang\*, and T.-S. Kim\*. "Identifying the weakest interface in BEOL structures". *Applied Surface Science, 701, 163228*.
- J.-W. Lee+, T. H.-Q. Nguyen+, W. J. Kang, S. Seo, S. Lee, S. Lee, J. Choi, J. Park, T.-S. Kim, and B. J. Kim\*. "Simultaneous integration of poly(dimethylsiloxane) elastomer in polymer donor and dimer acceptor enables strain-induced power enhancement in intrinsically-stretchable organic photovoltaics". *Energy & Environmental Science, 18, 7, 3325-3340*.
- H. S. Kang, S. Kim, H. Song, Y. Lee, J. Jang, W. G. Chung, C.-Y. Gu, J. Kim, T.-S. Kim, S. Ryu, J.-U. Park\* and B.-S. Bae\*. "Skin-Tailored Adhesive Bio-Electrode with Tunable Poisson's Ratio for Stable Electrophysiological Communication". *Advanced Healthcare Materials, 14, 10, 2404882*.
- O. Gul, M. Song, C.-Y. Gu, J. Ahn, K. Lee, T.-S. Kim, J. Ahn\*, H. J. Kim\* and I. Park\*. "Bioinspired Omnidirectional Interface Engineered Flexible Island for Highly Stretchable Electronics". *Small, 2410247*.
- O. Gul, M. Song, C.-Y. Gu, J. Ahn, K. Lee, J. Ahn, H. J. Kim\*, T.-S. Kim\* and I. Park\*. "Bioinspired Interfacial Engineering for Highly Stretchable Electronics". *Nature Communications, 게재 승인*.
- D. J. Kim, S. W. Lee, S. Sung, I. Lee, S. Park, J. Lee, J. J. Kim, S. Kang\* and T.-S. Kim\*. "Role of loading mode on crack propagation behavior and adhesion at Cu–SiCN interface". *Applied Surface Science, 688, 162461*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays, and More". *2025 Materials Research Society (MRS) Fall Meeting, Boston, USA, Nov. 30 - Dec. 5, 2025. (Invited)*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays, and More". *6th International Conference on Nanojoining and Microjoining, Yeongju, Korea, Nov. 17-21, 2025. (Invited)*.
- M. S. Ju, C.-Y. Gu, S.-W. Lee, and T.-S. Kim. "Effect of Chip Layout on Warpage-Induced Delamination in Copper/FR4 Substrates under Mechanical Loading". *ISMP 2025, Daegu, Korea, November 04-07, 2025. (Poster)*.
- C.-Y. Gu, M. S. Ju, S. W. Ma, J. H. Lee, C. Jeong, C. Kim, J. Choi and T.-S. Kim. "Prediction of Long-term Warpage in Semiconductor Packages Considering Thermal Aging of Epoxy Molding Compound". *ISMP 2025, Daegu, Korea, November 04-07, 2025. (Oral)*.
- J. Nam, D.-M. Kim, D. J. Kim, T.-S. Kim and B. J. Lee. "Tuning substrate permittivity for enhanced plasmon thermal conductivity". *The 11th JEMS-KSME Thermal and Fluids Engineering Conference (J-K TFEC11), Okinawa, Japan, Oct. 22-25, 2025*.
- Y. S. Ham, M. S. Ju, S. H. Sung, M. Song, S. Bark, J. Kim, J. Heo, H. Seo, J. Baek, K. S. Yim and T. -S. Kim\*. "Mechanical Reliability of SiCN - Ultra Low k Dielectrics in BEOL Interconnect Depending on Fracture Mode". *International Microsystems, Packaging, Assembly and Circuits Technology conference 2025 (IMPACT 2025), Taipei, Taiwan Oct. 21-23, 2025. (Oral)*.
- D. J. Kim, S. W. Lee, W. Choi, H. J. Chang, I. Lee, S. Park, J. Lee, J. J. Kim, S. Kang\* and T.-S. Kim\*. "Comprehensive Interface Adhesion Characterization for Advanced Semiconductor Packaging". *International Microsystems, Packaging, Assembly and Circuits Technology conference 2025 (IMPACT 2025), Taipei, Taiwan Oct. 21-23, 2025. (Oral)*.
- D. J. Kim, S. W. Lee, W. Choi, H. J. Chang, S. Kang and T.-S. Kim. "Interfacial adhesion mapping in BEOL structures". *GCIM 2025 & MRS-K Spring Meeting, Jeju, Korea, June 15-19, 2025*.
- E. S. Oh, J. Jeong, and T.-S. Kim. "Adhesion reliability between Poly(3,4-ethylenedioxythiophene):poly(styrene sulfonate) hydrogel treated with polar organic solvents and Polyimide substrate". *GCIM 2025 & MRS-K Spring Meeting, Jeju, Korea, June 15-19, 2025. (Poster)*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays, and More". *GCIM 2025 & MRS-K Spring Meeting, Jeju, Korea, June 15-19, 2025. (Invited)*.
- M. Song, S. J. Oh, S. Suh, T. Y. Kang, and T.-S. Kim. "Computer Vision-Based Investigation for Quantitative Characterization of Craze Phenomenon in Freely Stretched Ultra-Thin Polymer Films". *GCIM 2025 & MRS-K Spring Meeting, Jeju, Korea, June 15-19, 2025. (Poster)*.
- C.-Y. Gu, M. H. Choi, M. S. Ju, D. Kim, S. W. Ma, J. H. Lee, C. Jeong, C. Kim, J. Choi and T.-S. Kim. "Prediction of Warpage Changes in Silicon Wafers Induced by Dielectric Layer Deposition". *GCIM 2025 & MRS-K Spring Meeting, Jeju, Korea, June 15-19, 2025. (Poster)*.
- S.-W. Lee, Y. H. Son, S. Lee, S. J. Oh , Y. Jeon, H. Kim, J. H. Kwon and T.-S. Kim. "Highly Reliable and Ultra-flexible Wearable OLEDs Enabled by Environmentally and Mechanically Robust Hybrid Multibarrier Encapsulation Layers". *2025 MRS Spring Meeting & Exhibit, Seattle, Washington, USA, April 7-11. (Poster)*.
- 김보연, 송명, 김택수. "고분자 초박막의 파괴인성 평가를 위한 물 표면 위 이중 노치 인장 시험". *대한기계학회 재료및파괴부문 2025년도 춘계학술대회, 제주, 2025/06/25-27. (Poster)*.
- 송명, 김택수. "물 표면 플랫폼을 활용한 금속 초박막의 혼합 모드 파괴 시험법 개발". *대한기계학회 재료및파괴부문 2025년도 춘계학술대회, 제주, 2025/06/25-27. (Oral)*.
- 김도훈, 김택수. "화학적 가교가 폴리디메틸실록산의 준정적 및 시간-의존적 기계적 거동에 미치는 영향". *대한기계학회 재료 및 파괴부문 2026년도 춘계학술대회, 제주, 2025/06/24-27. (Oral)*.
- 송명, 오승진, 서승호, 강태엽, 김택수. "차세대 생체 융합 전자소자의 기계적 신뢰성 확보를 위한 신축된 폴리머 초박막의 이미지 이진화 기반 손상 정량화". *대한전자공학회 2025년도 하계학술대회, 제주, 2025/06/24-27. (Poster)*.
- 주민상, 김준모, 구창연, 송명, 마성우,이진희, 정찬우, 김창현, 최준기, 김택수. "차세대 패키징용 몰디드 언더필의 신뢰성 평가: 휨 및 박리 현상". *대한기계학회 신뢰성부문 2025년도 춘계학술대회, 경주, 2025/04/09-11. (Oral)*.
- 구창연, 주민상, 마성우,이진희, 정찬우, 김창현, 최준기, 김택수. "에폭시 몰딩 컴파운드의 열 노화에 따른 흡탈습 거동 평가". *대한기계학회 신뢰성부문 2025년도 춘계학술대회, 경주, 2025/04/09-11. (Oral)*.
- 오민호, 양찬희, 구창연, 주민상, 장동민, 장진우, 박근제, 김정규, 문수영, 김택수. "유한요소법을 활용한 DRAM의 리플로우 공정 중 Warpage 분석". *한국마이크로전자 및 패키징학회 2025년 정기학술대회, 인천, 2025/04/01-03. (Poster)*.
- 최민혁, 배은정, 박영욱, 권정현, 김택수. "두께에 따른 인듐-아연-산화물의 기계적 물성". *한국마이크로전자 및 패키징학회 2025년 정기학술대회, 인천, 2025/04/01-03. (Poster)*.
- 송명, 김보연, 함영석, 주민상, 성시혁, 이서영, 장원영, 박경범, 정덕영, 백종민, 임강섭, 김택수. "응력 보상을 통한 고 종횡비 반도체 식각 공정 내 위글링 불량 저감". *한국마이크로전자 및 패키징학회 2025년 정기학술대회, 인천, 2025/04/01-03. (Oral) (우수 논문 발표상)*.
- 김택수. "Mechanically Reliable of Thin Film Materials for Semiconductors, Displays, and More". *한국광학회 2025년 동계학술대회, 부산, 2025/02/11-14. (Invited)*.

**2024**

- Byungkook Oh†, Seunghyeok Baek†, Kum Seok Nam†, Changhoon Sung, , Congqi Yang, Young-Soo Lim, Min Sang Ju, Soomin Kim, Taek-Soo Kim, Sung-Min Park, Seongjun Park\*, Steve Park\*. "3D printable and biocompatible PEDOT:PSS-ionic liquid colloids with high conductivity for rapid on-demand fabrication of 3D bioelectronics". *Nature Communications, 15, 5839*.
- J. H. Lee+, C. G. Lee+, M. S. Kim+, S. Kim, M. Song, H. Zhang, E. Yang, Y. H. Kwon, Y. H. Jung, D. Y. Hyeon, Y. J. Choi, S. Oh, D. J. Joe, T.-S. Kim, S. Jeon, Y. Huang, T.-H. Kwon\* and K.J. Lee\*. "Deeply Implantable, Shape-Morphing, 3D MicroLEDs for Pancreatic Cancer Therapy". *Advanced Materials, Early View, 2411494*. <https://doi.org/10.1002/adma.202411494>[^b09]
- T.-I. Lee+,\*, J. H. Kim+, E. S. Oh, and T.-S. Kim\*. "Direct Tensile Testing of Free-standing Ultrathin Polymer Films on Liquid Surface at High Temperature". *Small Methods, 2401291*. <https://doi.org/10.1002/smtd.202401291>
- J.-W. Lee, E. S. Oh, S. Lee, T.N.-L. Phan, T.-S. Kim , J.-Y. Lee, J. R. Reynolds, and B. J. Kim\*. "Strain-induced Power Output Enhancement in Intrinsically Stretchable Organic Solar Cells". *Joule, 101792*.
- J. Lee+, C.-Y. Gu+, J. Chang, E. H. Cho, T.-S. Kim\*, and K. C. Choi\*. "Analytic Modeling and Validation of Strain in Textile-Based OLEDs for Advanced Textile Display Technologies". *npj Flexible Electronics, 8, 1, 73*.
- M. S. Kim+, J. An+, S. H. Lee, S. Min, Y. B. Kim, M. Song, S. H. Park, K. Y. Nam, H. J. Park, K. S. Kim, S. H. Oh, D. Hahn, J. Moon, J. W. Park, T.-S. Kim, B. J. Kim, and K. J. Lee\*. "Clinical Validation of Face-Fit Surface-Lighting Micro Light-Emitting Diode Mask for Skin Anti-Aging Treatment". *Advanced Materials, 2411651*. <https://doi.org/10.1002/adma.202411651>[^b10]
- E. C. Chae, Y.-H. Seo, B. J. Kang, J. H. Oh, Y. Jung, J. Jang, T. Kim, Y.-R. Jo, D. J. Kim, T.-S. Kim, S. H. Im, S. J. Sung, S. S. Shin\*, S. Hong\*, J. J. Nam\*. "PTAA-Infiltrated Thin-Walled Carbon Nanotube Electrode with Hidden Encapsulation for Perovskite Solar Cells". *EcoMat, e12495*.
- S. Lee+, S. Oh+, S. Han+, D. Lee, J. Lee, Y. Kim , H.-Y. Jeong, J.-W. Lee, M.-H. Lee, W. B. Ying, S. Jeong, S. Lee, J. Kim, Y. H. Kim, B. J. Kim, E.-C. Jeon, T.-S. Kim, S. Cho, J.-Y. Lee\*. "Advancing high-efficiency, stretchable organic solar cells: novel liquid metal electrode architecture". *Energy & Environmental Science, 17, 8915*.
- C. Lim+, J.-W. Lee+, D. J. Kim , D. Han, T. N.-L. Phan, S. Lee, T.-S. Kim, B. J. Kim\*. "Tetramerized Small‐Molecule Acceptor for Organic Solar Cells with Enhanced Efficiency, Stability, and Mechanical Robustness: Impact of Chain Length and Dispersity Effects". *Advanced Functional Materials, 51, 34*.
- S.-W. Lee+, Y. H. Son+, S. Lee, S. J. Oh , Y. Jeon, H. Kim, T.-S. Kim\*, and J. H. Kwon\*. "Highly Reliable and Ultra-Flexible Wearable OLEDs Enabled by Environmentally and Mechanically Robust Hybrid Multibarrier Encapsulation Layers". *Advanced Functional Materials, 35, 10, 2411802*.
- S. Kang+, J. Chang, J. Lim, D. J. Kim , T.-S. Kim , K. C. Choi, J, H. Lee, S. Kim\*. "Graphene-enabled laser lift-off for ultrathin displays". *Nature Communications, 15, 8288*.
- K. H. Ahn+ , J.-B. Pyo, H. Song, T.-S. Kim\*. "Evaluation of stress distribution in carbon-based nanoporous electrode by three-dimensional nanostructural reconstruction". *Sustainable Materials and Technologies, 41, e01112*.
- E.-Y. Shin+, J. Park, D. J. Kim , S. H. Park, K. Kim, E. Go, K. Kim, H. Jin, J. S. Kim, J. H. Noh, S.-W. Baek, B. Chae, T.-S. Kim ,E. Lee, S. Chung, Y. H. Jang, H. J. Son\*. "Highly mechanically stable and intrinsically stretchable large-area organic photovoltaics using nanoporous bulk-heterojunction". *Chemical Engineering Journal, 499, 156116*.
- S.-B. Kim+, D. Lee, J. Kim, T. Kim, J. H. Sim, J.-H. Yang, S. J. Oh , S. Hahn, D. Choi, T.-S. Kim , H. Moon, S. Yoo\*. "3D height-alternant island arrays for stretchable OLEDs with high active area ratio and maximum strain". *Nature Communications, 15, 7802*.
- K. H. Ahn+ , K.-L. Jang+ , J.-H. Kim, T.-S. Kim\*. "Unraveling the Intrinsic Thermal Behavior of Freestanding Ionomer Films Depending on Thickness from Commercial Membrane to Nanofilm". *Langmuir, 40, 35*.
- Y. Lee+, B. Jang, H. Song , S. Kim, Y. W. Kwon, H. S. Kang, M. S. Kim, I. Park, T.-S. Kim , J. Jang, J.-H. Kim, J.-U. Jang, B.-S. Bae\*. "A seamless auxetic substrate with a negative Poisson’s ratio of −1". *Nature Communications, 15, 7146*.
- C. Yang , C.-Y. Gu , M.S. Ju , J. Kim , D. M. Jang, J. S. Jang, J. K. Kim T.-S. Kim\*. "Time-Dependent Warpage Analysis for PCB Considering Viscoelastic Properties of Prepreg". *J. Microelectron. Packag. Soc., 31, no.2, pp23-27*.
- S. Seo+, Q. Wan+, E. S. Oh+ , S. M. Sheppard, J.-W. Lee, C. Lim, T.-S. Kim\* , B. C. Thompson\*, B. J. Kim\*. "Investigating the Effects of Hydrogen Bonding on Mechanical and Electrical Properties of n-Type Semicrystalline Polymers". *Chemistry of Materials, 36, 15*.
- D. J. Kim+, S. Kang+, S. W. Lee, I, Lee, S. Park, J. Lee, J. J. Kim, and T.-S. Kim\*. "Effects of Surface Treatments for the Adhesion Improvement between Cu and SiCN in BEOL Interconnect". *Surfaces and Interfaces, 51, 104734*.
- HJ. Kim+, D. J. Kim+, J. P. Baek, W. J. Kim, S. Kim, and T.-S. Kim\*. "Intrinsic Thermo-Mechanical Properties of Freestanding TEOS-SiO2 Thin Films Depending on Thickness". *ACS Applied Electronic Materials, 6, 5293-5300*.
- E. Qiao+, J. Baek+, C. Fulmore, M. Song, T.-S. Kim, S. Kumar, and D.V. Schaffer\*. "Spectrin Mediates 3D-Specific Matrix Stress-relaxation Response in Neural Stem Cell Lineage Commitment". *Science Advances, 10(31), eadk8232*. <https://doi.org/10.1126/sciadv.adk8232>[^b11]
- J. Jo+, M. Park+, S. Kang+, H. Lee+, C.-Y. Gu, T.-S. Kim, and S. Ryu\*. "Data-driven prediction of strain fields in auxetic structures and non-contact validation with Mechanoluminescence for structural health monitoring". *International Journal of AI for Materials and Design*.
- H.-G. Lee+, J.-W. Lee+, E. S. Oh+, M. J. Lee, T.-S. Kim\*, C. Lee\*, and B. J. Kim\*. "Effect of Rigid-Block Length in Elastomer-Containing Photoactive Block Copolymers on Photovoltaic and Mechanical Properties of Polymer Solar Cells". *Journal of Materials Chemistry A*.
- S. J. Oh+, S.-W. Lee+, H. Lee+, H. Kim, T.-S. Kim\* and J. H. Kwon\*. "Nanolaminate-Induced Mechanically and Environmentally Robust Al2O3/TiO2 Thin Film Encapsulation by Low-Temperature Atomic Layer Deposition: Toward Flexible and Wearable OLEDs". *Advanced Materials Technologies, 2400381*.
- T.-I. Lee+, J. H. Kim+, D. J. Kim, and T.-S. Kim\*. "Evaluating Free Thermal Expansion and Glass Transition of Ultrathin Polymer Films on Heated Liquid". *ACS Applied Materials & Interfaces, 16(23), 30336-30343*. <https://doi.org/10.1021/acsami.4c02279>
- J.-W. Lee+, T. H.-Q. Nguyen+, E. S. Oh, S. Lee, J. Choi, H. S. Kwon, C. Wang, S. Lee, J.-Y. Lee, T.-S. Kim, B. J. Kim\*. "Establishing Co-Continuous Network of Conjugated Polymers and Elastomers for High-Performance Polymer Solar Cells with Extreme Stretchability". *Advanced Energy Materials, ", 2401191*.
- D. Won+, HJ. Kim+, J. Kim, H. Kim, M. W. Kim, J. Ahn, K. Min, Y. Lee, S. Hong, J. Choi, C.-Y. Kim, T.-S. Kim\*, and S. H. Ko\*. "Laser-induced wet stability and adhesion of pure conducting polymer hydrogels". *Nature Electronics, 1-10*.
- F. Arshad+, M. Haris+, E. S. Oh+, Z. Ullah+, D. H. Ryu, S. Lee, H. K. Lee, S. K. Lee, T.-S. Kim\*, H.-W. Kwon\*, C. E. Song\*, and W. S. Shin\*. "Hydrogen-Bonding Interactions Between Terpolymers Enable Excellent Device Efficiency and Operational Stability of Non-Halogenated Solvent-Processed Polymer Solar Cells". *Advanced Functional Materials, 2402045*.
- J.-W. Lee+, C. Sun+, S. Lee, D. J. Kim, E. S. Oh, T. N.-L. Phan, T. H.-Q. Nguyen, S. Seo, Z. Tan, M. J. Lee, J.-Y. Lee, X. Bao, T.-S. Kim, C. Lee\*, Y.-H. Kim\*, and B. J. Kim\*. "High-Performance Intrinsically Stretchable Organic Solar Cells Based on Flexible Spacer Incorporated Dimerized Small-Molecule Acceptors". *Nano Energy, 109541*.
- S. Seo+, H. Jeon+, E. S. Oh, J.-W. Lee, C. Lim, T. H.-Q. Nguyen, T. N.-L. Phan, D. Jeong, M. J. Lee, T.-S. Kim, and B. J. Kim\*. "Benzobisthiazole-Substituted Terpolymers for Non-Halogenated Solvent-Processed Polymer Solar Cells with Enhanced Efficiency, Thermal Stability and Mechanical Robustness". *Journal of Materials Chemistry A, 12, 8205-8215*.
- D. S. Lee, K. W. Kim, Y.-H. Seo, M. H. Ann, W. Lee, J. Nam, J. Chung, G. Seo, S. Nam, B. S. Ma, T.-S. Kim, Y. Kang, N. J. Jeon\*, J. Seo\*, and S. S. Shin\*. "Overcoming stability limitations of efficient, flexible perovskite solar modules". *Joule, Online published*.
- M. Song, B. S. Ma, S. J. Oh, and T.-S. Kim\*. "Plane Stress Fracture Toughness Testing of Freestanding Ultra-Thin Nanocrystalline Gold Films on Water Surface". *Small Methods, 2301220*.
- J. Lee+, D. Park+, K. Park, H. Song, T.-S. Kim and S. Ryu\*. "Optimization of grid composite configuration to maximize toughness using integrated hierarchical deep neural network and genetic algorithm". *Materials & Design, 112700*.
- J.-W. Lee†, C. Sun†, J. Lee, D. J. Kim, W. J. Kang, S. Lee, D. Kim, J. Park, T. N.-L. Phan, Z. Tan, F. S. Kim, J.-Y. Lee, X. Bao, T.-S. Kim, Y.-H. Kim\* and B. J. Kim\*. "Design of Star-Shaped Trimer Acceptors for High-Performance, Photostable, and Mechanically-Robust Organic Solar Cells". *Advanced Energy Materials, 14(8), 2303872*.
- K. Jeong+, D. Kim+, D. Ahn, C. Yang, J. Kim, C. Lee, Y. Kim, C. Lee, Y.-S. Park , S.-H. Lee , T.-S. Kim\*, and S. G. Im\*. "A Hyperelastic Adhesive Forming Multiple Neutral Planes Even at Extreme Temperatures". *Chemical Engineering Journal, 480, 148151*.
- Y. H. Kim, T. Y. Kang and T.-S. Kim. "Non-Destructive Monitoring of Mechanical Degradation of Nanostructured Carbon-Based Films under Freeze-Thaw Cycles by S-Parameter Analysis". *The 7th International Conference on Materials and Reliability (ICMR 2024), Busan, Korea, Dec. 3-6, 2024. (Oral) (Best Paper Award)*.
- M. Song, H. Lee, S. Suh, S. J. Oh, W. Choi, T. Y. Kang and T.-S. Kim. "Crazing-Image-Assisted Neural Network (CIANN) for Predicting Nonlinear Mechanical Behaviors of Freestanding Ultra-Thin Polymer Films". *The 7th International Conference on Materials and Reliability (ICMR 2024), Busan, Korea, Dec. 3-6, 2024. (Oral) (Best Paper Award)*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays and More". *The 7th International Conference on Materials and Reliability (ICMR 2024), Busan, Korea, Dec. 3-6, 2024. (Plenary Lecture)*.
- C.-Y. Gu, C. Yang, M. S. Ju, D. M. Jang, J. S. Jang, J. W. Jang, J. K. Kim and T.-S. Kim. "Effect of Viscoelastic-anisotropic Properties of Prepreg on Diagonal Warpage of Multilayer PCB Substrates". *The 22nd International Symposium on Microelectronics and Packaging joined with the 18th International Conference Reliability and Stress-Related Phenomena in Nanoelectronics (ISMP-IRSP 2024), Busan, Korea, Nov. 5-8, 2024. (Poster) (Best Poster Award)*.
- Y. S. Ham, M. S. Ju, S. H. Sung, M. Song, S. Bark, J. Kim, J. Heo, H. Seo, J. Baek, K. S. Yim and T. -S. Kim. "Mechanical Reliability of SiCN - SiOC:H in BEOL (Back-end-of-line) Interconnect According to Fracture Mode". *The 22nd International Symposium on Microelectronics and Packaging joined with the 18th International Conference Reliability and Stress-Related Phenomena in Nanoelectronics (ISMP-IRSP 2024), Busan, Korea, Nov. 5-8, 2024. (Oral)*.
- M. S. Ju, J. Kim, C.-Y. Gu, M. Song, S. W. Ma, K. Han, J. H. Lee, W.-S. Lee and T.-S. Kim. "Warpage and Delamination Behavior on Sub-100µm Thickness Epoxy Molding Compound : An Investigation for Molded Underfill in Advanced 3D Packaging". *The 22nd International Symposium on Microelectronics and Packaging joined with the 18th International Conference Reliability and Stress-Related Phenomena in Nanoelectronics (ISMP-IRSP 2024), Busan, Korea, Nov. 5-8, 2024. (Oral) (Young Scientist Award)*.
- D. J. Kim, H. J. Kim and T.-S. Kim. "Study on the Intrinsic Thermo-mechanical Properties of TEOS-SiO2 Thin Films through Etching of Naturally Formed Copper Oxide". *The 22nd International Symposium on Microelectronics and Packaging joined with the 18th International Conference Reliability and Stress-Related Phenomena in Nanoelectronics (ISMP-IRSP 2024), Busan, Korea, Nov. 5-8, 2024. (Oral)*.
- T.-S. Kim. "Mechanical Reliability of Thin Film Materials for Semiconductors, Displays and More". *International Microsystems, Packaging, Assembly and Circuits Technology Conference (IMPACT), Taipei, Taiwan, Oct. 23-25, 2024. (Invited)*.
- 송명, 최원, 김택수. "이미지 기반 신경망 이론을 활용한 파티클 프리 스트레인 맵핑". *대한기계학회 충청지회 & 한국기계연구원 DX전략연구단 2024년 공동학술대회, 대전, 2024/11/21. (Poster) (최우수상)*.
- 오은성, 이다혜, 박현정, 김범준, 김택수. "Measurement of the Thermal Expansion Properties of Poly(3-hexylthiophene) Thin Films as a Function of Molecular Weight". *한국세라믹학회 2024 추계학술대회, 서울, 2024/10/16. (Poster)*.
- 강원중, 김형준, 김택수. "Mechanical Properties of PEDOT:PSS Hydrogel Treated with Polar Organic Solvents". *한국세라믹학회 2024 추계학술대회, 서울, 2024/10/16. (Poster) (양송포스터상 우수상)*.
- 김동준, 김형준, 김택수. "Intrinsic Thermo-Mechanical Properties Measurements of Freestanding TEOS-SiO2 Thin Films via Copper Oxide Etching". *한국세라믹학회 2024 추계학술대회, 서울, 2024/10/16. (Poster)*.
- 이선우, 오승진, 권정현, 김택수. "Robust Al2O3/TiO2 Nanolaminate Thin Films via Low-Temperature Atomic Layer Deposition: Enhancing Flexibility and Environmental Resistance for Wearable OLEDs". *한국세라믹학회 2024 추계학술대회, 서울, 2024/10/16. (Poster)*.
- 송명, 오승진, 최원, 서승호, 이해봄, 강태엽, 김택수. "생성형 예측 모델을 활용한 박막의 인장 시험법 표준화를 위한 물 표면 플랫폼에서의 데이터 추출 시스템 개발". *대한기계학회 충청지회 2024년 춘계학술대회, 대전, 2024/06/20. (Poster) (우수논문상)*.
- 이선우, 김지훈, 김택수. "유한요소해석을 이용한 이종집적 실리콘 패키지의 휨 분석 및 기계적 물성 시스템 구축". *대한기계학회 충청지회 2024년 춘계학술대회, 대전, 2024/06/20. (Poster)*.
- 성시혁, 김동준, 성동철, 김택수, 홍영준, 홍석륜. "낮은 일함수 차이 금속 증착을 통한 Graphene/SiO2의 계면접합력 조정". *대한기계학회 충청지회 2024년 춘계학술대회, 대전, 2024/06/20. (Poster)*.
- 송명, 오승진, 최원, 서승호, 이해봄, 강태엽, 김택수. "생성형 예측 모델을 적용한 박막의 신뢰성 평가를 위한 물 표면 플랫폼에서의 데이터 추출 시스템 개발". *한국마이크로전자 및 패키징 학회 2024년 정기학술대회, 광주, 2024/04/03-04. (Poster)*.
- 강원중, 김형준, 김택수. "극성 유기용매가 PEDOT:PSS 하이드로겔의 기계적 물성에 미치는 영향". *한국마이크로전자 및 패키징 학회 2024년 정기학술대회, 광주, 2024/04/03-04. (Poster)*.
- 김도훈, 정기훈, 안다혜, 양찬희, 김준모, 임성갑, 김택수. "새로운 샌드위치 구조의 광학적으로 투명한 접착제를 위한 폴리디메틸실록산의 기계적 물성". *한국마이크로전자 및 패키징 학회 2024년 정기학술대회, 광주, 2024/04/03-04. (Poster)*.
- 구창연, 주민상, 김준모, 송명, 마성우, 이진희, 한권환, 이웅선, 김택수. "에폭시 몰딩 컴파운드의 내부 구조에 따른 흡탈습 거동 평가". *한국마이크로전자 및 패키징 학회 2024년 정기학술대회, 광주, 2024/04/03-04. (Oral)(Young Scientist Award)*.
- 오은성, 오승진, 이선우, 전승민, 김택수. "The Effect of Protective Layer on Ultra-thin Glass through Finite Element Analysis Modeling of Pen Drop Test". *대한기계학회 신뢰성부문 2024년 춘계학술대회, 여수, 2024/03/20-22. (Oral)*.
- 최원, 김택수. "신뢰성을 위한 두께에 따른 나노결정질 알루미늄 박막의 기계적 물성". *대한기계학회 신뢰성부문 2024년 춘계학술대회, 여수, 2024/03/20-22. (Oral)*.
- 주민상, 김준모, 구창연, 송명, 마성우, 이진희, 한권환, 이웅선, 김택수. "차세대 3D 패키징용 얇은 몰디드 언더필의 기계적 물성". *대한기계학회 신뢰성부문 2024년 춘계학술대회, 여수, 2024/03/20-22. (Oral)*.
- 함영석, 주민상, 성시혁, 송명, 박수현, 김주한, 허자영, 서훈석, 백종민, 임강섭, 김택수. "플라즈마 처리에 의한 BEOL 연결배선 구조 내 SiCN-SiOC:H의 계면 신뢰성 향상". *대한기계학회 신뢰성부문 2024 춘계학술대회, 여수, 2024/03/20-22 (Oral)*.
- 김택수. "Flexible & Stretchable 평가기술: Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *제20회 OLED School, 서울, 2024/02/05 (Invited)*.

**2023**

- Y. Jeon+, T.-Y. Lee+, M. Nam+, H. Lee, H. Kim, S.-W. Lee, S. J. Oh, S. Choi, J.-Y. Yang, S. Jung, S. Lee, E.-Y. Byeon, T.-S. Kim, H. Jeon\*, and J. H. Kwon\*. "Highly Efficient and Reliable Organic Light–Emitting Diodes Enabled by a Multifunctional Hazy Substrate for Extreme Environments". *Advanced Functional Materials, 2310268*.
- J. Bae, J. Lee, W. -T. Hwang, D. -Y. Youn, H. Song, J. Ahn, J. -S. Nam, J. -S. Jang, D. -W. Kim, W. Jo, T.-S. Kim, H. -J. Suk, P. -K. Bae, and I.-D. Kim\*. "Advancing Breathability of Respiratory Nanofilter by Optimizing Pore Structure and Alignment in Nanofiber Networks". *ACS Nano, 18(2), 1371-1380*.
- M. K. Kim, Y. S. Choi, D. Kim, K. Heo, S. J. Oh, S. Lee, J. An, H. Yoo, S. H. Kim, T.-S. Kim, and B. Shin\*. "Integration of Large-Area Halide Perovskite Single Crystals and Substrates via Chemical Welding Using an Ionic Liquid for Applications in X-ray Detection". *ACS Applied Materials & Interfaces, 15(49), 57404-57414*.
- Q. Wan+, H. Jeon+, S. Seo+, E. S. Oh, J.-W. Lee, C. Wang, T.-S. Kim, B. J. Kim\*, and B. C. Thompson\*. "Polymer Acceptor with Hydrogen Bonding Functionality for Efficient and Mechanically Robust Ternary Organic Solar Cells". *Chemistry of Materials, 35(24), 10476-10486*.
- S. H. Park, T. J. Kim, H. E. Lee, B. S. Ma, M. Song, M. S. Kim, J. H. Shin, S. H. Lee, J. H. Lee, Y. B. Kim, K. Y. Nam, H.-J. Park, T.-S. Kim, and K. J. Lee\*. "Universal Selective Transfer Printing via Micro-vacuum Force". *Nature Communications*. <https://doi.org/10.1038/s41467-023-43342-8>
- J.-W. Lee+, H.-G. Lee+, E. S. Oh, S.-W. Lee, T.N.-L. Phan, S. Li, T.-S. Kim, and B. J. Kim\*. "Rigid and Soft Block-Copolymerized Conjugated Polymers Enable High-Performance Intrinsically-Stretchable Organic Solar Cells with Record Efficiency". *Joule, 8(1), 204-223*.
- JE. Kim+, S. Lee, C. -Y. Gu, T.-S Kim, H. Kong, D. Jang\*. "Mechanical Characterization of Collagen Hydrogels by Quasi-static Uniaxial Tensile Experiments". *Advanced Engineering Materials*.
- C. Lim+, S. Park+, D. J. Kim+, J.-W Lee, J. Su. Park, S. Seo, D. Kim, F. S. Kim\*, T.-S. Kim\*, and B. J. Kim \*. "Design of Mechanically-Robust Naphthalenediimide-based Polymer Additives for High-Performance, Intrinsically-Stretchable Polymer Solar Cells". *Journal of Materials Chemistry A, 11(37), 20031-20042*.
- G.-U. Kim+, C. Choi+, D. Jeong+, D. J. Kim, T. N.-L. Phan, S. Song, J. Park, T.-S. Kim, Y.-H. Kim\*, and B. J. Kim \*. "Highly Efficient and Robust Ternary All-Polymer Solar Cells Achieved by Electro-Active Polymer Compatibilizers". *Advanced Energy Materials, 13(39), 2302125*.
- H. Jin, K. Kim, S. Park, J. Rhee, H. Ahn, D. J. Kim, K. Kim, J. H. Noh, T.-S. Kim, E.-Y. Shin, and H. J. Son\*. "Chemically Recyclable Conjugated Polymer and One-Shot Preparation of Thermally Stable and Efficient Bulk-Heterojunction from Recycled Monomer". *Advanced Functional Materials, 33(47), 2304930 (게재 승인)*.
- S. Y. Park, S. Y. On, J. Kim, J. Lee, T.-S. Kim, B. L. Wardle\*, and S. S. Kim\*. "Reducing Bonding Temperature and Energy Consumption in Electronic Packaging Using Flash Electro-Thermal Carbon Fiber Heating". *ACS Applied Materials & Interfaces, 15(32), 38750-38758*.
- S. Lee+, Y. Jeon+, S. J. Oh, S.-W. Lee, K. C. Choi\*, T.-S. Kim\*, and J. H. Kwon\*. "Study of Mechanical Degradation of Freestanding ALD Al2O3 by Hygrothermal Environment and Facile Protective Method for Environmentally Stable Al2O3: Toward Highly Reliable Wearable OLEDs". *Materials Horizons, 10, 4488-4500*.
- J.-W. Lee+, T. N.-L. Phan+, E. S. Oh+, H.-G. Lee, T.-S. Kim\*, and B. J. Kim\*. "Carboxylate-Containing Poly(thiophene vinylene) Derivative with Controlled Molecular Weights for High-Performance IntrinsicallyStretchable Organic Solar Cells". *Advanced Functional Materials, 2305851*.
- J. Kim, M. Song, C.-Y. Gu, S. Ma, J. H. Lee, W.-S. Lee, and T.-S. Kim\*. "Enhancing Predictability of Thermal Warpage by Applying Temperature-Dependent Poisson's Ratio of Epoxy Molding Compound". *Polymer Testing, 125, 108140*.
- H.-Y. Jung, E. S. Oh, D. J. Kim, H. Shim, W. Lee, S.-G. Yoon, J. Lim, J. S. Yun, T.-S. Kim, and T.-Y. Yang\*. "Adjusted Bulk and Interfacial Properties in Highly Stable Semitransparent Perovskite Solar Cells Fabricated by Thermocompression Bonding between Perovskite Layers". *ACS Applied Materials & Interfaces, 15(26), 31344-31353*.
- C. Kim, I. Kozakci, S. Y. Lee, B. Kim, J. Kim, J. Lee, B. S. Ma, E. S. Oh, T.-S. Kim, and J.-Y. Lee\*. "Quantum Dot-Siloxane Anchoring on Colloidal Quantum Dot Film for Flexible Photovoltaic Cell". *Small, 2302195*.
- H. Song+, E. Park+, H.J. Kim, C.I. Park, T.-S. Kim, Y.Y. Kim\*, and S. Ryu\*. "Free-Form Optimization of Pattern Shape for Improving Mechanical Characteristics of a Concentric Tube". *Materials and Design (연구실 기재)*.
- J. Lee+, J.-W. Lee+, H. Song, M. Song, J. Park, G.-U. Kim, D. Jeong, T.-S. Kim, and B. J. Kim\*. "Interdiffused thermoplastic urethane-PEDOT:PSS bilayers with superior adhesion properties for high-performance and intrinsically-stretchable organic solar cells". *Journal of Materials Chemistry A*.
- S. Lee, Y. Jeon, S. Y. Lee, B. S. Ma, M. Song, D. Jeong, J. Jo, G.-U. Kim, J. Lee, T.-S. Kim, B. J. Kim\*, and J.-Y. Lee\*. "Intrinsically Stretchable Organic Solar Cells without Cracks under 40% Strain". *Advanced Energy Materials*.
- S. J. Oh, S. Lee, K. C. Choi, J. H. Kwon\*, and T.-S. Kim\*. "Elucidating the Effect of Ag Interlayer Formation on the Intrinsic Mechanical Properties of Free-standing ITO/Ag/ITO Thin Films". *Journal of Materials Chemistry C, 11, 7262-7271*.
- K. Kim, H. Kim, S.-W. Lee, M. Y. Lee, G. Lee, Y. Park, H. Kim, Y. H. Lee, M. Kim, K. Y. Ma and M. J. Kim, T.-S. Kim, Hyeon S. S\*, B. J. Cho\*. "Ultralow- k Amorphous Boron Nitride Film for Copper Interconnect Capping Layer". *IEEE Transactions on Electron Devices*.
- S. Seo+, J.-W. Lee+, D. J. Kim, T. N.-L. Phan, J. Park, T.-S. Kim, and B. J. Kim\*. "Poly(dimethylsiloxane)-block-PM6 Polymer Donors for High-Performance and Mechanically-Robust Polymer Solar Cells". *Advanced Materials, 35(24), 2300230*.
- S. Y. Park, S. Y. On, J. Kim, J. Lee, T.-S. Kim, B. L. Wardle\*, and S. S. Kim\*. "Electronic Packaging Enhancement Engineered by Reducing the Bonding Temperature via Modified Cure Cycles". *ACS Applied Materials & Interfaces, 15(8), 11024-11032*.
- J. Kim+, G.-U. Kim+, D. J. Kim+, S. Lee, D. Jeong, S. Seo, S.-J. Ko\*, S. C. Yoon\*, T.-S.Kim\*, and B. J. Kim\*. "Development of rigidity-controlled terpolymer donors for high-performance and mechanically robust organic solar cells". *Journal of Materials Chemistry A, 11, 4808*.
- H. Park+, B. S. Ma+, Y. Kim, D. Lee, S. Li, H. J. Kim\*, T.-S. Kim\*, and B. J. Kim\*. "Direct Measurement of the Thermomechanical Properties of Poly(3-hexylthiophene) Thin Films on Ionic Liquid Surfaces". *Macromolecules, 56(4), 1633-1642*.
- B. Oh+, Y.-S. Lim+, K. W. Ko, H. Seo, D. J. Kim, D. Kong, J. M. You, H. Kim, T.-S. Kim, S. Park, D.-S. Kwon, J. C. Na, W. K. Han, S.-M, Park\*, and S. Park\*. "Ultra-soft and highly stretchable tissue-adhesvie hydrogel based multifunctional implantable sensor for monitoring of overactive bladder". *Biosensors and Bioelectronics, 115060*. <https://doi.org/10.1016/j.bios.2023.115060>[^b13]
- S. Kang, T.-S Kim\*. "Controlled Surface Topography of Nanofilm by Local Strain Modulation in Mechanical Transfer Process". *Applied Surface Science, 608, 155113*.
- W. Jo+, K. Jeong+, Y.-S. Park , J.-I. Lee , S. G. Im\*, T.-S Kim\*. "Thermally Stable and Soft Pressure-sensitive Adhesive for Foldable Electronics". *Chemical Engineering Journal, 452(1), 139050*.
- S. J. Oh, S.-W. Lee, Y. S. Ham, J. H. Kwon, and T.-S. Kim. "Enhancing Mechanical Reliability in Thin Film Encapsulation Using Low-Temperature Atomic Layer Deposition". *The 14th International Symposium on NDT in Aerospace (AeroNDT2023), Busan, Korea, Nov. 5-8, 2023. (Oral)*.
- S. J. Oh, K. C. Choi, J. H. Kwon, and T.-S. Kim. "Elucidating the Mechanical Properties of Transparent Conductive Thin Films for Mechanically Reliable Microelectronics". *The 21st International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Oct. 25-27, 2023. (Oral)*.
- M. S. Ju, J. Kim, C.-Y. Gu, M. Song, S. Ma, J. H. Lee, W.-S. Lee and T.-S. Kim. "Thermo-Mechanical Behavior of Molded Underfill Filling the Sub-100μm Die Gap for Advanced Packaging". *The 21st International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Oct. 25-27, 2023. (Oral)*.
- M. Song, K.-L. Jang, N. Jung, S. Kim, D. S. Kim, and T.-S. Kim. "Prediction of Wiggling Phenomenon in High Aspect Ratio Thin Film Structure During Etching Process through Buckling-Based Dimensional Analysis". *The 21st International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Oct. 25-27, 2023. (Oral) (Young Scientist Award)*.
- D. J. Kim, Y. H. Kim, and T.-S. Kim. "Fabrication of Robust Freestanding Gold Membrane by Heat Treatment". *Advanced Epitaxy for Freestanding Membranes and 2D Materials (AEFM) Conference 2023, Seoul, Korea, Jul. 10-12, 2023. (Poster)*.
- T.-S. Kim. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *Advanced Epitaxy for Freestanding Membranes and 2D Materials (AEFM) Conference 2023, Seoul, Korea, Jul. 10-12, 2023. (Invited)*.
- S. J. Oh, J. H. Kwon, S. Lee, and T.-S. Kim. "Mechanical Behavior of Transparent Conducting Oxide Thin Films for Advanced Electronic Applications". *ICEM20 - 20th International Conference on Experimental Mechanics, Porto, Portugal, July 2-7, 2023. (Oral)*.
- H. J. Kim, D. J. Kim, and T.-S. Kim. "Mechanical Properties of TEOS Thin Film". *ICEM20 - 20th International Conference on Experimental Mechanics, Porto, Portugal, July 2-7, 2023. (Oral)*.
- M. Song, B. S. Ma, S. J. Oh, and T.-S. Kim. "Elucidating Thickness-Dependent Plane Stress Fracture Toughness of Ultra-Thin Nanocrystalline Gold Films". *ICEM20 - 20th International Conference on Experimental Mechanics, Porto, Portugal, July 2-7, 2023. (Oral)*.
- D. J. Kim, S. W. Lee, S. Kang, I. Lee, S. Park, J. S. Lee, J. Lee, J. J. Kim, T.-S. Kim. "Optimization of Cu Interconnects - SiCN Interfacial Adhesion by Surface Treatments". *2023 IEEE 73rd Electronic Components and Technology Conference, Orlando, USA, May 30 - June 2, 2023. (Oral) (2023 ECTC Student Travel Award Winner)*.
- J. Kim, M. Song, C.-Y. Gu, M. S. Ju, S. W. Ma, J. H. Lee, W.-S. Lee, T.-S. Kim. "Effect of High-Temperature Exposure on the Thermo-Mechanical Behavior of Epoxy Molding Compound and Warpage of Molded Wafers". *2023 IEEE 73rd Electronic Components and Technology Conference, Orlando, USA, May 30 - June 2, 2023. (Oral)*.
- T.-S. Kim. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *International Conference on Electronics Packaging (ICEP), Kumamoto, Japan, April 19-20, 2023. (Invited)*.
- T.-S. Kim. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *The 7th IEEE Electron Devices Technology and Manufacturing (EDTM) Conference 2023, Seoul, Korea, Mar. 7-10, 2023. (Invited)*.
- T. Y. Kang, D. Seo, T.-S. Kim. "On-Chip Canary Circuit Design for Electronic Interconnects by Utilizing RF Resonance Peak Movement as a Prognostic Factor". *The 7th IEEE Electron Devices Technology and Manufacturing (EDTM) Conference 2023, Seoul, Korea, Mar. 7-10, 2023. (Oral)*.
- J. Kim, M. Song, C.-Y. Gu, S. W. Ma, M.-H .Jeong, J. H. Lee, W.-S. Lee, T.-S. Kim. "Enhancing Predictability of Thermal Warpage of Molded Wafer by Applying Accurate Thermo-Mechanical Properties of Epoxy Molding Compound". *The 7th IEEE Electron Devices Technology and Manufacturing (EDTM) Conference 2023, Seoul, Korea, Mar. 7-10, 2023. (Oral) (Best Student Paper Award)*.
- 김준모, 김택수. "얇은 유리 섬유 강화 기판의 유리 섬유 층 수에 따른 고온 인장 탄성 계수 변화 양상". *MPC 2023 추계 컨퍼런스, 서울, 2023/09/22. (Poster)*.
- 최원, 백수연, 오승진, 최경철, 김택수. "유연 소자의 기계적 신뢰성을 위한 알루미늄 박막의 기계적 물성 측정". *한국정밀공학회 2023 춘계학술대회, 제주도, 2023/05/10-12. (Poster)*.
- 송명, 장경림, 정나래, 김성진, 김대신, 김택수. "좌굴 기반 차원 분석을 통한 식각 공정 중 발생하는 고종횡비 박막 구조의 위글링 현상 예측". *한국정밀공학회 2023 춘계학술대회, 제주도, 2023/05/10-12. (Oral)*.
- 김준모, 구창연, 송명, 마성우, 이진희, 이웅선, 김택수. "Temperature-Dependent Elastic Properties of Thin Molded Underfill". *한국마이크로전자 및 패키징 학회 2023년도 춘계 정기학술대회, 수원, 2023/04/05-06. (Oral)*.
- 주민상, 김준모, 구창연, 송명, 마성우, 이진희, 이웅선, 김택수. "100μm 이하의 다이 갭을 충진하는 웨이퍼 레벨 패키징용 몰디드 언더필의 흡습 및 열-기계적 거동". *한국마이크로전자 및 패키징 학회 2023년도 춘계 정기학술대회, 수원, 2023/04/05-06. (Poster) 우수 포스터 발표상*.
- 이선우, 오승진, 오은성, 김택수. "기구학적 비선형성을 고려한 Ball-on-Ring 시험에의한 초박형 유리의 파괴 강도 평가". *대한기계학회 신뢰성부문 2023년 춘계학술대회, 제주도, 2023/03/22-24. (Oral) 우수 논문상*.
- 김용휘, 안광호, 채준수, 최시영, 김택수. "초음파 파쇄를 활용한 PEMFC 전극의 공극률 제어". *대한기계학회 신뢰성부문 2023년 춘계학술대회, 제주도, 2023/03/22-24. (Oral) 우수 논문상*.
- 안광호,김용휘,김택수. "구동환경에 따른 고분자 전해질막 연료전지 전극의 기계적 특성 평가". *대한기계학회 신뢰성부문 2023년 춘계학술대회, 제주도, 2023/03/22-24. (Oral)*.
- 김택수. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *한국광학회 2023년 동계학술대회, 부산, 2023/02/15-17. (Invited)*.

**2022**

- S. Kwon+, G. Park+, H. Jin, C. Gu, S. J. Oh, J. Y. Sim, W. Youm, T.-S. Kim, H. J. Kim, and S. Park\*. "On-skin and tele-haptic application of mechanically decoupled taxel array on dynamically moving and soft surfaces". *npj Flexible Electronics, 6, 98*.
- T. N.-L. Phan+, J.-W. Lee+, E. S. Oh, S. Lee, C. Lee, T.-S. Kim, S. Li\* B. J. Kim\*. "Efficient and Non-Halogenated Solvent-Processed Organic Solar Cells Enabled by Conjugated Donor-Acceptor Block Copolymers Containing the Same Benzodithiophene Unit". *ACS Applied Materials & Interfaces, 14(51), 57070–57081*.
- J.-W. Lee+, S. Seo+, S.-W. Lee, G.-U. Kim, S. Han, T. N.-L. Phan, S. Lee, S. Li, T.-S. Kim, J.-Y. Lee, B. J. Kim\*. "Intrinsically Stretchable, Highly Efficient Organic Solar Cells Enabled by Polymer Donors Featuring Hydrogen-Bonding Spacers". *Advanced Materials, 2207544*.
- J.-W. Lee+, C. Lim+, S.-W. Lee, Y. Jeon, S. Lee, T.-S. Kim, J.-Y. Lee, B. J. Kim\*. "Intrinsically Stretchable and Non-Halogenated Solvent Processed Polymer Solar Cells Enabled by Hydrophilic Spacer-Incorporated Polymers". *Advanced Energy Materials, 202202224*.
- J.-Y. Oh\*, C.-S. Hwang, Y. S. Yang, M. Song, J. Kim, T.-S. Kim, S. Kim. H. Oh, S. Y. Kang, J.-E. Pi, J. B. Koo, C. W. Park, H. Lee\*. "Dual-Functional Self-Attachable and Stretchable Interface for Universal Three-Dimensional Modular Electronics". *ACS Applied Materials & Interfaces, 14(43), 49303-49312*.
- J. Kim, B. Kim, C.-H Jung, G.-S. Kim, T.-S. Kim\*. "Thermal Stress Induced Spalling of Metal Pad on Silicon Interposer". *Journal of the Microelectronics and Packaging Society, 29(3), 25-29*.
- E. S. Oh, S. J. Oh, S.-W. Lee, S.-M. Jeon, T.-S. Kim\*. "Mechanical Modeling of Pen Drop Test for Protection of Ultra-Thin Glass Layer". *Journal of the Microelectronics and Packaging Society, 29(3), 49-53*.
- Y. Lee+, H. Lee+, H.-G Im, W. Jo, G.-M Choi, T.-S. Kim, J. Jang\*, B.-S. Bae\*. "Transparent and Flexible Hybrid Cover Window Film: Hard Coating/Substrate All-in-One Composite Film for Reliable Foldable Display". *Composites Part B: Engineering, 247, 110336*.
- J.-W. Lee+, C. Sun+, S.-W. Lee, G.-U. Kim, S. Li, C. Wang, T.-S Kim, Y.-H. Kim\*, B. J. Kim\*. "Sequentially-Regular Polymer Acceptors Featuring Flexible Spacers for High-Performance and Mechanically-Robust All-Polymer Solar Cells". *Energy & Environmental Science*.
- J.-W. Lee+, S.-W. Lee+, J. Kim+, Y. H. Ha, C. Sun, T. N.-L. Phan, S. Lee, C. Wang, T.-S Kim\*, Y.-H. Kim\*, B. J. Kim\*. "Mechanically Robust All-polymer Solar Cells Enabled by Polymerized Small Molecule Acceptors Featuring Flexible Siloxane-spacers". *Journal of Materials Chemistry A, 10, 20312-20322*.
- S. J. Sung, J. Im, G. Kim, C. S. Moon, J. J. Yoo, S. S. Shin, N. J. Jeon, B. S. Ma, D. J. Kim, T.-S. Kim, J. Seo\*. "Molecular Engineering for Function-Tailored Interface Modifier in High-Performance Perovskite Solar Cells". *Advanced Energy Materials, 12(27), 2200758*.
- S. J. Oh, B. S. Ma, C. Yang, T.-S. Kim\*. "Intrinsic Mechanical Properties of Free-Standing SiNx Thin Films depending on PECVD Conditions for Controlling Residual Stress". *ACS Applied Electronic Materials, 4(8), 3980-3987*.
- H. Song, S. Timilsina, J. Jung, T.-S. Kim\*, S. Ryu\*. "Improving the Sensitivity of the Mechanoluminescence Composite through Functionalization for Structural Health Monitoring". *ACS Applied Materials & Interfaces, 14(26), 30205-30215*.
- D. Won+, J. Kim+, J. Choi, H.J. Kim, S. Han, I. Ha, J. Bang, K. K. Kim, Y. Lee, T.-S. Kim, J.-H. Park, C-Y. Kim\*, S. H. Ko\*. "Digital selective transformation and patterning of highly conductive hydrogel bioelectronics by laser-induced phase separation". *Science Advances, 8(23), eabo3209*.
- H. E. Lee+, D. Lee+, T.-I. Lee, J. Jang, J. Jang, Y.-W. Lim, J. H. Shin, S.-M. Kang, G.-M. Choi, D. J. Joe, J. H. Kim, S. H. Lee, S. H. Park, C. B. Park, T.-S. Kim, K. J. Lee\*, B.-S. Bae\*. "Siloxane Hybrid Material-Encapsulated Highly Robust Flexible μLEDs for Biocompatible Lighting Applications". *ACS Applied Materials & Interfaces, 14, 24, 28258–28269*.
- Q. Chen+, Y. H. Han+, L. R. Franco, C. F. N. Marchiori, Z. Genene, C. M. Araujo, J.-W. Lee, T. N.-L. Phan, J. Wu, D. Yu, D. J. Kim, T.-S. Kim, L. Hou\*, B. J. Kim\*, E. Wang\*. "Effects of Flexible Conjugation-Break Spacers of Non-Conjugated Polymer Acceptors on Photovoltaic and Mechanical Properties of All-Polymer Solar Cells". *Nano-Micro Letters, 14, 164*.
- B. S. Ma+, J.-W. Lee+, H. Park, B. J. Kim\*, T.-S. Kim\*. "Thermo-mechanical Behavior of Poly(3-hexylthiophene) Thin Film on Water Surface". *ACS Omega, 7, 23, 19706–19713*.
- J.-W. Lee+, G.-U. Kim+, D. J. Kim+, Y. Jeon, S. Li, T.-S. Kim\*, J.-Y. Lee\*, B. J. Kim\*. "Intrinsically-Stretchable Organic Solar Cells Achieved by High-Molecular-Weight, Electro-Active Polymer Acceptor Additives". *Advanced Energy Materials, 2200887*.
- J. C. Yang+, S. Lee+, B. S. Ma, J. Kim, M. Song, S. Y. Kim, D. W. Kim, T.-S. Kim\*, S. Park\*. "Geometrically engineered rigid island array for stretchable electronics capable of withstanding various deformation modes". *Science Advances, 8, eabn3863*.
- J. Baek, P. A. Lopez, S. Lee, T.-S. Kim, S. Kumar,\* and D. V. Schaffer\*. "Egr1 is a 3D matrix-specific mediator of mechanosensitive stem cell lineage commitment". *Science Advances, 8, eabm4646*. <https://doi.org/10.1126/sciadv.abm4646>[^b14]
- H. Park+, D.-H. Kim+, B. S. Ma, E. Shin, Y. Kim, T.-S. Kim, F. S. Kim, I.-D. Kim\*, B. J. Kim\*. "High-Performance, Flexible NO2 Chemiresistors Achieved by Design of Imine-Incorporated n-Type Conjugated Polymers". *Advanced Science, 9, 2200270*.
- W. Jo, T.-I. Lee, T.-S. Kim\*. "Enlarged tensile strain at edge of flexible substrate due to anticlastic curvature". *Microelectronics Reliability, 130, 114485*.
- M. Song, B. S. Ma, S. J. Oh, and T.-S. Kim. "Liquid Surface Platform for Quantitatively Evaluating Fracture Toughness of Ultra-Thin Gold Films". *The 20th International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Nov. 9-11, 2022. (Oral)*.
- J. Kim, C.-Y. Gu, M. Song, S. Ma, J. H. Lee, W.-S. Lee and T.-S. Kim. "Effect of Span-to-Depth Ratio on Bending Behavior of Thin Molded Underfill". *The 20th International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Nov. 9-11, 2022. (Oral) (Young Scientist Award)*.
- E. S. Oh, D. J. Kim, T.-I. Lee, D. Lee, H. Park, J.-W. Lee, B. J. Kim and T.-S. Kim. "Thermo-mechanical behavior of poly(3-hexylthiophene-2,5-diyl) thin films for flexible and stretchable electronics". *The 20th International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Nov. 9-11, 2022. (Oral)*.
- T.-S. Kim. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *12th International Conference on Flexible and Printed Electronics (ICFPE), Jeju, Korea, Oct. 11-14, 2022. (Invited)*.
- J. H. Kim, J.-B. Pyo, K. Kim, and T.-S. Kim. "Improvements of Mechanical Properties and Electrical Resistance of PEMFC Catalyst Layer Through Thermal Reconfiguration". *The Electrochemical Society Meeting (ECS), Atlanta, USA, Oct. 9-13, 2022. (Oral)*.
- 양찬희, 김택수. "고온 환경 하에서 롤러블 디스플레이의 열-기계적 신뢰성". *대한기계학회 2022년 학술대회, 제주도, 2022/11/09-12. (Oral)*.
- 김택수. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *대한기계학회 2022년 학술대회, 제주도, 2022/11/09-12. (Invited)*.
- 오은성, 김동준, 이태익, 이다혜, 박현정, 이진우, 김범준, 김택수. "Thermo-mechanical Properties of Conjugated Polymer Thin Films for Flexible and Stretchable Devices". *한국고분자학회 2022년도 추계 정기학술대회, 대구, 2022/10/05-07. (Oral) 최우수 논문 발표상*.
- 김택수. "Strategies for Mechanically Reliable Thin-Film Flexible Electronics". *2022 한국고분자학회 분자전자부문위원회 심층토론회, 제주도, 2022/06/22-24. (Invited)*.
- 오승진, 마부수, 양찬희, 김택수. "PECVD 증착 조건에 따른 실리콘 질화물 박막의 기계적 특성 연구". *대한기계학회 재료 및 파괴부문 2022년도 춘계학술대회, 제주도, 2022/06/22-24. (Oral)*.
- 김준모, 송명, 구창연, 마성우, 이웅선, 이진희, 김택수. "Effect of Curing Conditions on Thermo-mechanical Properties of Epoxy Molding Compound". *대한기계학회 재료 및 파괴부문 2022년도 춘계학술대회, 제주도, 2022/06/22-24. (Oral)*.
- 김동준, 강수민, 이인화, 박승주, 이지현, 김중정, 김택수. "표면처리와 하중 모드에 따른 Cu 도선과 SiCN 캡핑층 간의 접합 신뢰성". *한국마이크로전자 및 패키징 학회 2022년도 춘계 정기학술대회, 수원, 2022/04/06-07. (Oral) 우수 논문 발표상*.
- 구창연, 김택수. "두께와 결정학적 방향이 얇은 실리콘 웨이퍼의 굽힘 물성에 끼치는 영향". *한국마이크로전자 및 패키징 학회 2022년도 춘계 정기학술대회, 수원, 2022/04/06-07. (Oral)*.
- 송명, 마부수, 김택수. "물 표면 플랫폼을 활용한 금속 초박막의 두께에 따른 파괴인성 평가". *한국마이크로전자 및 패키징 학회 2022년도 춘계 정기학술대회, 수원, 2022/04/06-07. (Oral) =*.
- 구창연, 김택수. "두께와 결정학적 방향이 얇은 실리콘 웨이퍼의 굽힘 물성에 끼치는 영향". *대한기계학회 신뢰성부문 2022년도 춘계학술대회, 제주도, 2022/03/23-25. (Oral)*.
- 송명, 마부수, 김택수. "물 표면 위에서의 단일 노치 인장 시험을 통한 초박막의 파괴인성 평가". *대한기계학회 신뢰성부문 2022년도 춘계학술대회, 제주도, 2022/03/23-25. (Oral)*.
- 김동준, 강수민, 이선우, 이인화, 박승주, 이지현, 김중정, 김택수. "표면 처리를 통한 Cu 도선과 SiCN 캡핑층 간의 접합 신뢰성 최적화". *대한기계학회 신뢰성부문 2022년도 춘계학술대회, 제주도, 2022/03/23-25. (Oral)*.

**2021**

- Y. Kim, J. Kim, C. Y. Kim, T. Kim, C. Lee, K. Jeong, W. Jo, S. Yoo, T.-S. Kim, K. C. Choi, S. G. Im\*. "A modulus-engineered multi-layer polymer film with mechanical robustness for the application to highly deformable substrate platform in stretchable electronics". *Chemical Engineering Journal, 431(2), 134074*.
- Z. Genene+, J.-W. Lee+, S.-W. Lee, Q. Chen, Z. Tan, B. A. Abdulahi, D. Yu, T.-S. Kim\*, B. J. Kim\*, and E. Wang\*. "Polymer Acceptors with Flexible Spacers Afford Efficient and Mechanically Robust All-Polymer Solar Cells". *Advanced Materials, 2107361*.
- J.-W. Lee+, C. Sun+, D. J. Kim, M. Y. Ha, D. Han, J. S. Park, C. Wang, W. B. Lee\*, S.-K. Kwon\*, T.-S. Kim\*, Y.-H. Kim\* and B. J. Kim\*. "Donor–Acceptor Alternating Copolymer Compatibilizers for Thermally Stable, Mechanically Robust, and High-Performance Organic Solar Cells". *ACS Nano, 15(12), 19970-19980*.
- S.-M. Kang, H. E. Lee, H. S. Wang, J. H. Shin, W. Jo, Y. Lee, H. Lee, D. Lee, Y. H. Kim, T.-S. Kim, K. J. Lee\*, B.-S. Bae\*. "Self-Powered Flexible Full-Color Display via Dielectric-Tuned Hybrimer Triboelectric Nanogenerators". *ACS Energy Letters, 6(11), 4097-4107*.
- S. J. Oh, B. S. Ma, C. Yang, M. Song, and T.-S. Kim\*. "Mechanical Property Evaluation of Dielectric Thin Films for Flexible Displays using Organic Nano-Support-Layer". *Journal of the Microelectronics and Packaging Society, 28(3), 33-38*.
- H. Lee, Y. Lee, S. W. Lee, S.-M. Kang, Y. H. Kim, W. Jo, T.-S. Kim, J. Jang\*, B.-S. Bae\*. "Elongation improvement of transparent and flexible surface protective coating using polydimethylsiloxane-anchored epoxy-functionalized siloxane hybrid composite for reliable out-foldable displays". *Composite Part B: Engineering, 225(15), 109313*.
- R. You+, S. Kang+, C. Lee, J. Jeon, J. Wie\*, T.-S. Kim\*, D. K. Yoon\*. "Programmable liquid crystal defect arrays via electric field modulation for mechanically functional liquid crystal networks". *ACS Applied Materials & Interfaces, 13(30), 36253-36261*.
- M. Lyu+, S. Park+, H. Lee, B. S. Ma, S. H. Park, K.-H. Hong, H. Kim, T.-S. Kim, J. H. Noh, H. J. Son\*, N.-G. Park\*. "Simultaneous Enhanced Efficiency and Stability of Perovskite Solar Cells Using Adhesive Fluorinated Polymer Interfacial Material". *ACS Applied Materials & Interfaces, 13(30), 35595-35605*.
- J. B. Ko, S. Lee, T.-I. Lee, S. Lee, J. Kim, H. Kim, T.-S. Kim, S.-H. K. Park\*. "Ultrathin, Flexible, and Transparent Oxide Thin-Film Transistors by Delamination and Transfer Methods for Deformable Displays". *Advanced Materials Technologies, 2100431*.
- J. Noh+, G.-U Kim+, S. Han, S. J. Oh, Y. Jeon, D. Jeong, S. W. Kim, T.-S. Kim, B. J. Kim\* and J.-Y. Lee\*. "Intrinsically Stretchable Organic Solar Cells with Efficiencies of over 11%". *ACS Energy Letters, 6(7), 2512–2518*.
- K.-S. Lee+, J.-B. Pyo+, T.-S. Kim\*, and H.-S. Park\*. "Tubular Hygromechanical Polymeric Brake for Soft and Compact Wearable Robots". *ACS Applied Polymer Materials, 3, 3206-3213*.
- J.-B. Pyo, S. Lee, and T.-S. Kim\*. "Intrinsic Swelling Behavior of Free-Standing Nanoporous Ionomer-Bound Carbon Films". *Polymer Testing, 100, 107241*.
- T. Y. Kang, D. Seo, J. Min, and T.-S. Kim\*. "Quantification of Performance Variation and Crack Evolution of Bond-Wire Interconnects Under Harsh Temperature Environments by S-Parameter Analysis". *IEEE Trans. Compon., Packag., Manuf. Technol., 11(6), 990-998*.
- D. K. Choi, D. H. Kim, C. M .Lee, H. Hafeez, S. Sarker, J. S. Yang, H. J. Chae, G.-W. Jeong, D. H. Choi, T. W. Kim, S. Yoo, J. Song, B. S. Ma, T.-S. Kim, C. H. Kim, H. J. Lee, J. W. Lee, D. Kim, T.-S. Bae, S. M. Yu, Y.-C. Kang, J. Park, K.-H. Kim, M. Sujak, M. Song, C.-S. Kim\*, and S. Y. Ryu\*. "Highly Efficient, Heat Dissipating, Stretchable Organic Light-Emitting Diodes Based on a MoO3/Au/MoO3 Electrode with Encapsulation". *Nature Communications, 12, 2864*.
- J.-W. Lee+, D. Jeong+, D. J. Kim, T. N-L. Phan, J. S. Park, T.-S. Kim and B. J. Kim\*. "Flexible-Spacer Incorporated Polymer Donors Enable Superior Blend Miscibility for High-Performance and Mechanically-Robust Polymer Solar Cells". *Energy & Environmental Science, 14, 4067-4076*.
- J.-B. Pyo+, J. H. Kim+, K. Kim, and T.-S. Kim\*. "Electrical Resistance Change in Thermally Reconfigured Nanoporous Ionomer-Bound Carbon Films". *Journal of Materials Chemistry A, 9, 13019*.
- T. I. Kim, I.-J. Park, S. Kang, T.-S. Kim, and S.-Y. Choi\*. "Enhanced Triboelectric Nanogenerator Based on Tungsten Disulfide via Thiolated Ligand Conjugation". *ACS Applied Materials & Interfaces, 13(18), 21299–21309*.
- J.-W. Lee+, B. S. Ma+, H. J. Kim, T.-S. Kim\* and B. J. Kim\*. "High-Molecular-Weight Electroactive Polymer Additives for Simultaneous Enhancement of Photovoltaic Efficiency and Mechanical Robustness in High-Performance Polymer Solar Cells". *JACS Au, 1(5), 612-622*.
- S. J. Oh+, J. H. Kwon+, S. Lee, K. C. Choi\* and T.-S. Kim\*. "Unveiling the Annealing-Dependent Mechanical Properties of Freestanding Indium Tin Oxide Thin Films". *ACS Applied Materials & Interfaces, 13(14), 16650–16659*.
- W. Jo+, H. Lee+, Y. Lee, B.-S. Bae\* and T.-S. Kim\*. "Controlling neutral plane of flexible substrates by asymmetric impregnation of glass fabric for protecting brittle films on foldable electronics". *Advanced Engineering Materials, 2001280*.
- J. Shin, J. Park, J. Seo, T. Im, J. Kim, H. Lee, D. Kim, K. Woo, H. Jeong, Y. Cho, T.-S. Kim, I. Kang and K. Lee\*. "A Flash-Induced Robust Cu Electrode on Glass Substrates and its Application for Thin-Film μLED". *Advanced Materials, 2007186*.
- S. Kang, T. Yoon, B. S. Ma, M. S. Cho and T.-S. Kim\*. "Liquid-assisted adhesion control of graphene–copper interface for damage-free mechanical transfer". *Applied Surface Science, 551, 149229*.
- Y. U. Kim+, B. S. Ma+, Y. Kim+, S. H. Park, H. Kang, H. J. Yoon, M. J. Cho\*, T.-S. Kim\*, J. H. Kim\* and D. H. Choi\*. "Comparison of the Mechanical Properties of Polymer Blend and Main-Chain Conjugated Copolymer Films with Donor–Acceptor Heterojunctions". *Chemical Engineering Journal, 415, 128952*.
- S. Han, K.-W. Seo, W. Kim, T.-S. Kim and J.-Y. Lee\*. "Enhanced stretchability of metal/interlayer/metal hybrid electrode". *Nanoscale, 13, 4543-4550*.
- S. Song, E. Y. Park, B. S. Ma, D. J. Kim, H. H. Park, Y. Y. Kim, S. S. Shin, N. J. Jeon, T.-S. Kim and J. Seo\*. "Selective Defect Passivation and Topographical Control of 4‐Dimethylaminopyridine at Grain Boundary for Efficient and Stable Planar Perovskite Solar Cells". *Advanced Energy Materials, 11, 2003382*.
- J.-W. Lee, N. Choi, D. J. Kim, T. N-L. Phan, H. Kang, T.-S. Kim and B. J. Kim\*. "Side Chain Engineered Naphthalene Diimide-Based Terpolymer for Efficient and Mechanically Robust All-Polymer Solar Cells". *Chemistry of Materials, 33(3), 1070-1081*.
- S. Kang and T.-S. Kim\*. "Capillary-Force-Driven Switchable Delamination of Nanofilms and Its Applications to Green Selective Transfer". *Advanced Materials Technologies, 6, 2001082*.
- H. You, A. L. Jones, B. S. Ma, G.-U. Kim, S. Lee, J.-W. Lee, H. Kang, T.-S. Kim, J. R. Reynolds\* and B. J. Kim\*. "Ester-Functionalized, Wide-Bandgap Derivatives of PM7 for Simultaneous Enhancement of Photovoltaic Performance and Mechanical Robustness of All-Polymer Solar Cells". *Journal of Materials Chemistry A, Advanced Article*.
- S. W. Lee, D. J. Kim, J. Jeon, W.J. Yun, T.-S. Kim, and T.-S. Kim. "Investigation on the Mechanical Reliability of TiN/SiO2 for W Nucleation Processes". *The 19th International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Nov. 3-5, 2021. (Oral)*.
- D. J. Kim, S. Kang, S. W. Lee, I. Lee, S. Park, J. S. Lee, J. Lee, J. J. Kim, and T.-S. Kim. "Optimization of Cu Interconnects-SiCN Interfacial Adhesion by Surface Treatments". *The 19th International Symposium on Microelectronics and Packaging (ISMP), Busan, Korea, Nov. 3-5, 2021. (Oral) (Young Scientist Award)*.
- 강수민, 김택수. "물 표면장력을 이용한 나노박막의 선택적 전사". *2021 한국정밀공학회 추계학술대회, 부산, 2021/11/24-26. (Oral)*.

## 특허

등록일이 2021년 10월 13일–2026년 10월 13일에 드는 연구실 게시 특허 6건이다. 국내 4건과 미국 2건이며, 제목·발명자·번호·등록일은 연구실 표기다.[^publications]

- 프리 스탠딩 멤브레인 제작 방법 및 프리 스탠딩 멤브레인을 이용한 전기도금층 형성 방법 (등록일 2026-08-06; 출원번호 10-2025-0016907; 등록번호 10-3003372; 발명자 김택수, 김동준, 김용휘; 국가 국내)
- 원격 제어가 가능한 반자기 부상 로터 및 이를 이용한 소프트 액츄에이터 (등록일 2024-12-26; 출원번호 10-2022-0110216; 등록번호 10-2748563; 발명자 김택수, 김지훈, 표재범; 국가 국내)
- 신축성 전자소자용 기판 및 이를 포함하는 아일랜드 형상 전자소자 (등록일 2023-07-26; 출원번호 10-2022-0056990; 등록번호 10-2561540; 발명자 스티브 박, 양준창, 이승규, 김택수; 국가 국내)
- 연료전지용 전극의 전기저항 측정 장치 및 방법 (등록일 2022-11-01; 출원번호 10-2017-0174755; 등록번호 10-2463432; 발명자 김택수, 오종길, 홍보기, 표재범, 김준모, 안광호, 이상민, 장경림, 김재한; 국가 국내)
- Soft robot using diamagnetic levitation (등록일 2023-12-05; 출원번호 17898668; 등록번호 11837972; 발명자 T.-S. Kim, J. H. Kim, J.-B. Pyo; 국가 US)
- Method for selective delamination and transfer of thin film using liquid platform (등록일 2022-07-26; 출원번호 16736983; 등록번호 11397382; 발명자 T.-S. Kim, S. Kang; 국가 US)

## 수상과 장학금

2021년 10월 13일–2026년 10월 13일의 교수 소개와 연구실 소식에 게시된 수상·장학금 18건이다.[^people][^news]

- 2026.04.21 · 김택수 교수, 2026년 과학·정보통신의 날 기념식 국무총리표창
- 2026.04.09 · 김동준 박사, 대한기계학회 우수학위논문상. 논문: 프리스탠딩 나노필름 제작 및 차세대 전사
- 2025.11.13 · 김동준, 우덕재단 장학금
- 2025.02.12 · 김택수 교수, KAIST 학술대상
- 2024.12.06 · 오은성, 기계공학과 석사과정 우수상. 논문: 이온성 액체 표면 플랫폼 위에서의 Poly(3-hexylthiophene) 박막의 열기계적 물성
- 2024.08.23 · 김동준, KAIST Humanity Scholarship Award (Achievement Category)
- 2023.10.27 · Myoung Song, ISMP-2023 Young Scientist Award
- 2023.04.10 · Dong Jun Kim, 2023 ECTC Student Travel Grant
- 2023.03.10 · Junmo Kim, IEEE EDTM 2023 Best Student Paper Award
- 2022.12.02 · Seung Jin Oh, 우덕재단 장학금
- 2022.11.25 · 김동준, 기계공학과 석사과정 우수상. 논문: Mechanical Reliability of Cu Interconnects - SiCN Capping Layer Interface by Surface Treatments
- 2022.11.11 · Junmo Kim, ISMP-2022 Young Scientist Award
- 2022.11.10 · 김택수 교수, 제13회 해동젊은공학인상 학술부문
- 2022.10.07 · 오은성, 한국고분자학회 최우수 논문 발표상
- 2022.08.03 · Dong Jun Kim, 김영한 글로벌리더 장학금
- 2022.04.19 · Eun Sung Oh, 관정장학재단 장학금
- 2022.04.07 · 김동준, 마이크로전자 및 패키징 학회 우수 논문 발표상
- 2021.11.05 · Dong Jun Kim, ISMP-2021 Young Scientist Award

## 소식

같은 기간에 게시된 연구 발표·보도 소식 3건이다.[^news]

- 2025.11.05 · 연구실의 수소 전극 동파 해결 연구가 언론에 보도되었다.
- 2024.09.23 · 김동준이 삼성전자 세미나에서 BEOL향 Cu-SiCN 계면 접합력과 TEOS 나노 박막 인장 물성 측정·분석에 관한 최신 논문 리뷰를 발표했다.
- 2024.06.01 · 연구실 연구가 TechXplore 기사와 Nature Reviews Electrical Engineering 연구 하이라이트, Nature Electronics 소식에 소개되었다.

## 연락과 위치

- 교수 연구실: Bldg. N7-4, Rm. 7103[^people]
- 학생 사무실: N7-4, 6126·5121호. 실험실: 6125호[^contact]
- 주소: 34141 대전광역시 유성구 대학로 291 KAIST 기계공학과 N7-4[^contact]
- 교수 이메일: tskim1@kaist.ac.kr[^people]
- 전화: 042-350-3238[^people]
- 학생 사무실 전화: 5층 042-350-5238, 6층 042-350-3278[^contact]
- 팩스: 042-350-3210[^people]

## 각주
[^home]: APTF Lab, Home. 첨단 패키징과 박막의 역학·신뢰성, 응용 분야 소개. <https://aptf.kaist.ac.kr/> 관측 2026-10-31.
[^people]: APTF Lab, Members. 교수의 학력·경력·직위·소속·수상·연락처와 Student & Postdoc·Alumni 목록. <https://aptf.kaist.ac.kr/members> 관측 2026-10-31.
[^packaging]: APTF Lab, Research, Semiconductor Packaging. 반도체 패키지의 기계적 신뢰성, HBM·FOWLP 제조의 비선형 휨, 패키징 재료의 열·습기·힘에 따른 성질과 접합면 에너지를 연구한다고 설명한다. <https://aptf.kaist.ac.kr/research/01> 관측 2026-10-31.
[^mechanical]: APTF Lab, Research, Mechanical Reliability. 접착 에너지와 박리, 잔류 응력·열·흡습 변형에 의한 휨, 유연 전자소자의 반복 하중과 피로 파괴를 연구한다고 설명한다. <https://aptf.kaist.ac.kr/research/03> 관측 2026-10-31.
[^property]: APTF Lab, Research, Mechanical Property. 박막의 인장·굽힘 물성 및 열팽창 계수 측정, 디지털 영상 상관법과 액체 표면의 박막 측정법을 소개한다. <https://aptf.kaist.ac.kr/research/04> 관측 2026-10-31.
[^manufacturing]: APTF Lab, Research, Manufacturing Method. 떼어 내는 속도와 표면 성질을 조절해 그래핀과 금 박막의 여러 무늬를 전사하고, 물 표면과 말기 동작을 이용해 막을 층별로 조립하는 방법을 개발했다고 설명한다. <https://aptf.kaist.ac.kr/research/06> 관측 2026-10-31.
[^fem]: APTF Lab, Research, Finite Element Method. 굽힘·흡습 변형·접착의 수치 해석과 계산된 응력·변형률을 이용한 신뢰성 연구를 소개한다. <https://aptf.kaist.ac.kr/research/05> 관측 2026-10-31.
[^publications]: APTF Lab, Publications. Journal·International Conference·Domestic Conference·Domestic Patent·International Patent·Book 게시 목록. <https://aptf.kaist.ac.kr/publications> 관측 2026-10-31.
[^news]: APTF Lab, News. 날짜별 연구 발표·보도·수상·장학금 소식. <https://aptf.kaist.ac.kr/news> 관측 2026-10-31.
[^semicon]: KAIST 반도체공학대학원, 구성원, 기계공학과. 김택수 교수·기계공학과 소속, 연구 분야와 APTF 누리집 링크. <https://semicon.kaist.ac.kr/sub0302> 관측 2026-10-31.
[^ee]: KAIST 전기및전자공학부, 김택수. 겸임교수, 차세대 패키징 및 박막 연구실, N7 7103과 연락처 표기. <https://ee.kaist.ac.kr/professor/%EA%B9%80%ED%83%9D%EC%88%98/> 관측 2026-10-31.
[^contact]: APTF Lab, Contact. N7-4 건물 주소, 교수·학생 사무실과 실험실, 전화·이메일 표기. <https://aptf.kaist.ac.kr/contact> 관측 2026-10-31.
[^p1]: D. J. Kim 외, T.-S. Kim, Chemistry of Materials 38, 7687-7699 (온라인 2026-07-21). <https://doi.org/10.1021/acs.chemmater.6c00701> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1021/acs.chemmater.6c00701> 관측 2026-10-31–2026-11-01.
[^p2]: C.-Y. Gu 외, T.-S. Kim, IEEE Transactions on Materials for Electron Devices 2, 64-71 (2025). <https://doi.org/10.1109/tmat.2025.3572834> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/adma.202411494|10.1002/adma.202411651|10.1002/cey2.70098|10.1002/smtd.202401291|10.1016/j.bios.2023.115060|10.1016/j.nanoen.2026.112288|10.1021/acs.chemmater.6c00701|10.1021/acsami.4c02279|10.1038/s41467-023-43342-8|10.1109/tmat.2025.3572834|10.1111/acel.13805|10.1126/sciadv.abg8459|10.1126/sciadv.abm4646|10.1126/sciadv.adk8232|10.2139/ssrn.4836133> 관측 2026-10-31–2026-11-01.
[^p3]: T.-I. Lee, J. H. Kim, E. S. Oh, T.-S. Kim, Small Methods 9, 2401291 (온라인 2024-12-19). <https://doi.org/10.1002/smtd.202401291> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/smtd.202401291> 관측 2026-10-31–2026-11-01.
[^p4]: T.-I. Lee, J. H. Kim, D. J. Kim, T.-S. Kim, ACS Applied Materials & Interfaces 16, 30336-30343 (온라인 2024-05-23). <https://doi.org/10.1021/acsami.4c02279> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/adma.202411494|10.1002/adma.202411651|10.1002/cey2.70098|10.1002/smtd.202401291|10.1016/j.bios.2023.115060|10.1016/j.nanoen.2026.112288|10.1021/acs.chemmater.6c00701|10.1021/acsami.4c02279|10.1038/s41467-023-43342-8|10.1109/tmat.2025.3572834|10.1111/acel.13805|10.1126/sciadv.abg8459|10.1126/sciadv.abm4646|10.1126/sciadv.adk8232|10.2139/ssrn.4836133> 관측 2026-10-31–2026-11-01.
[^p5]: S. H. Park 외, K. J. Lee, Nature Communications 14, 7744 (온라인 2023-11-26). <https://doi.org/10.1038/s41467-023-43342-8> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=Universal%20Selective%20Transfer%20Printing%20via%20Micro-vacuum%20Force> 관측 2026-10-31–2026-11-01.
[^p6]: J.-B. Pyo, J. H. Kim, T.-S. Kim, Carbon Energy 7, e70098 (온라인 2025-10-31). <https://doi.org/10.1002/cey2.70098> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/cey2.70098> 관측 2026-10-31–2026-11-01.
[^p7]: D. Won, H. Kim, T.-S. Kim, S. H. Ko, Applied Physics Reviews 12, 031302 (2025). <https://doi.org/10.1063/5.0261387> 초록 기준(출판사 논문 페이지). 초록 원문 <https://aipp.silverchair-cdn.com/article-minimal/3351268> 관측 2026-10-31.
[^b09]: J. H. Lee 외, K. J. Lee, Advanced Materials 37, 2411494 (온라인 2024-12-16). <https://doi.org/10.1002/adma.202411494> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/adma.202411494> 관측 2026-10-31–2026-11-01.
[^b10]: M. S. Kim 외, K. J. Lee, Advanced Materials 36, 2411651 (온라인 2024-10-22). <https://doi.org/10.1002/adma.202411651> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/adma.202411651> 관측 2026-10-31–2026-11-01.
[^b11]: E. Qiao 외, D. V. Schaffer, Science Advances 10, eadk8232 (2024). <https://doi.org/10.1126/sciadv.adk8232> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1126/sciadv.adk8232> 관측 2026-10-31–2026-11-01.
[^b13]: B. Oh 외, S. Park, Biosensors and Bioelectronics 225, 115060 (2023). <https://doi.org/10.1016/j.bios.2023.115060> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/adma.202411494|10.1002/adma.202411651|10.1002/cey2.70098|10.1002/smtd.202401291|10.1016/j.bios.2023.115060|10.1016/j.nanoen.2026.112288|10.1021/acs.chemmater.6c00701|10.1021/acsami.4c02279|10.1038/s41467-023-43342-8|10.1109/tmat.2025.3572834|10.1111/acel.13805|10.1126/sciadv.abg8459|10.1126/sciadv.abm4646|10.1126/sciadv.adk8232|10.2139/ssrn.4836133> 관측 2026-10-31–2026-11-01.
[^b14]: J. Baek 외, D. V. Schaffer, Science Advances 8, eabm4646 (2022). <https://doi.org/10.1126/sciadv.abm4646> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1126/sciadv.abm4646> 관측 2026-10-31–2026-11-01.

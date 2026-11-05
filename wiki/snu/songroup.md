# 전산 에너지/바이오 소재 연구실 (Son Research Lab)

**서울대학교 자연과학대학 화학부 · 손창윤 부교수**

- 분야: 계산화학, 전하 계면과 분극, 고분자 전해질의 이온 이동, 물 정제용 분리막, 생체 분자 안에서 물의 역할[^faculty][^research]
- 대분야: 화학, 소재
- 태그: 분자 동역학 시뮬레이션[^faculty][^profile], 연성 소재·고분자[^research][^profile], 과학·공학 AI[^research][^profile], 이차전지 소재[^research], 분리막[^research], 수처리[^research]
- 홈페이지: <https://songroup.github.io/sonlab-website/>
- 근거와 출처: [전산 에너지/바이오 소재 연구실 근거 페이지](songroup-sources.md)

> 분자 모의와 계산 방법 개발로 에너지·바이오 소재의 구조·움직임·반응을 설명하고 소재 설계를 돕는 계산화학 연구실이다.[^faculty][^profile]

## 무엇을 연구하나

손창윤 교수가 이끄는 연구실로, 계산화학(물질의 구조와 반응을 계산 모형으로 연구하는 분야)을 통해 소재의 작동 원리를 밝히고 기능성 소재 설계를 돕는다. 원자는 화학 원소의 성질을 지닌 물질의 기본 입자이며, 분자는 원자들이 화학적으로 결합한 물질 입자다. 연구실은 분자 수준의 계산을 에너지(일을 하거나 물리적 변화를 일으킬 수 있는 능력을 나타내는 양)와 생체 현상에 관한 문제에 연결한다고 소개한다.[^faculty][^profile]

계산 방법도 연구 대상이다. 통계역학(입자들의 상태를 통계적으로 다루어 물질 전체의 성질을 설명하는 이론), 분자 동역학(원자·분자에 작용하는 힘으로 운동 방정식을 시간에 따라 풀어 움직임을 계산하는 방법), 조대 입자 모형(원자들을 묶은 유효 입자로 분자를 나타내는 모형), 기계학습(자료에서 관계와 규칙을 학습하는 계산 방법)을 사용하고 개발한다. 서로 다른 시간·공간 범위의 계산을 연결하는 다중 스케일 모의로, 전하(입자나 물체의 전기적 상호작용을 결정하는 성질)를 띤 소재의 구조와 움직임을 다룬다. 연구실은 분자 모의에 쓰는 소프트웨어 OpenMM을 활용한다고 밝힌다.[^faculty][^profile][^resources]

첫 관심은 서로 다른 물질이 맞닿는 경계인 계면이다. 전하가 있거나 전기적 성질이 다른 계면에서, 전하 사이의 정전기적 상호작용과 분극(전기장 등에 의해 물질 안 전하 분포가 치우치는 현상)이 구조와 움직임에 어떻게 관여하는지 연구한다. 공기와 물의 경계, 이온(전기를 띤 원자나 원자 무리)이 녹은 용액, 고분자(많은 구성 단위가 반복해서 연결된 큰 분자) 전해질과 생체막(세포와 세포 내부 공간을 구분하는 지질 기반 막) 등을 아우르는 계산 틀을 만들어 기능성 막 소재 설계를 돕는 것이 목표다.[^research][^profile]

고분자 전해질에서는 이온이 이동하고 전하가 저장되는 과정을 연구한다. 전해질은 이온의 이동으로 전류가 흐르는 물질이며, 전류는 단위 시간에 지나가는 전기의 양으로 나타낸 전하의 흐름이다. 연구 소개는 고분자에 전해질 용액이나 이온성 액체(양이온과 음이온으로 이루어진 액체)를 결합한 고분자 젤 전해질을 대상으로 든다. 힘장(분자 모의에서 입자 사이의 상호작용 에너지를 계산하는 수학 모형)을 기계학습으로 보정하고 다중 스케일 계산에 활용해, 에너지 저장 장치와 착용형 장치에 쓰일 전해질의 이동·충전 원리를 살핀다.[^research]

물의 이동은 분리막과 생체 분자 양쪽에서 다룬다. 그래핀은 탄소 원자들이 육각형 그물로 연결된 층이며, 산화 그래핀은 산소를 포함한 원자 무리가 결합한 그래핀이다. 연구실은 이 막의 표면과 전해질의 분극이 물·이온의 이동과 선택적 통과에 미치는 영향을 계산해 물 정제용 분리 성질을 조절하려 한다. 생체 쪽에서는 단백질(아미노산들이 사슬로 연결된 생체 분자) 안 물의 이동 경로를 계산해 생명 유지에 필요한 반응 조절을 이해하려 한다.[^research]

## 주요 연구 주제

### 1. 전하 계면과 분극을 반영한 분자 모형

공기·물, 용액·막처럼 성질이 다른 물질의 경계에서 구조와 이동을 계산하고, 기능성 에너지·바이오 소재를 설계할 분자 모형과 힘장을 개발한다. 대표 논문 6은 이온성 액체 속 리튬 이온에 대해 분극을 명시적으로 반영한 힘장을 만들고 이온들의 집단 이동을 분석한다.[^research][^profile][^p6]

### 2. 고분자 전해질과 이온 이동

기계학습으로 보정한 힘장으로 고분자 젤 전해질의 이온 이동과 충전 원리를 연구한다. 대표 논문 1은 공유 결합 유기 골격(유기 분자들이 공유 결합으로 이어진 규칙적인 다공성 구조) 안의 이온 이동 경로 설계를 다룬다. 공유 결합은 원자들이 전자를 공유하여 이루는 결합이고, 전자는 음의 전기를 띤 기본 입자다.[^research][^p1]

### 3. 산화 그래핀 분리막과 물 정제

산화 그래핀 표면과 전해질의 분극을 함께 다루어, 막 안에 제한된 물·이온이 이동하는 원리와 분리 성질을 연구한다. 분리막은 성분에 따라 통과 정도를 달리하여 물질을 나누는 막이다.[^research]

### 4. 물과 생체 분자의 상호작용

생체막과 단백질 안의 물이 생명 유지 반응에 어떤 역할을 하는지 다중 스케일 모의로 살핀다. 계면에서 생체 분자끼리 상호작용하는 다른 사례로, 대표 논문 3은 액정(흐르는 성질과 구성 분자 배열의 방향 질서를 함께 지닌 물질 상태)의 배열 변화로 아미노산과 세균 유래 분자 사이의 상호작용을 빛의 변화로 읽는다. 대표 논문 7은 액정 계면의 분자 상호작용을 바탕으로 화학적 선택성을 설계하는 원리를 다룬다.[^research][^p3][^p7]

## 대표 논문

게시 논문 가운데 초록을 확인하고 손창윤 교수의 서울대 소속이 저자 소속에 등록되어 있는 7편이다. 전해질의 이온 이동, 이온성 액체의 계산 모형, 에너지 변환 소재, 액정·분자 인식 계면과 전자 소재 설계를 담았다. 누리집은 손창윤 교수를 1–3·6·7에서 교신저자로 표시하고, 4·5에서는 공동 저자로 적는다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.[^pubs][^p1][^p2][^p3][^p4][^p5][^p6][^p7]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Room-Temperature Single Li+ Ion Conducting Organic Solid-State Electrolyte with 10⁻⁴ S cm⁻¹ Conductivity for Lithium-Metal Batteries](https://doi.org/10.1002/aenm.202504143) · Advanced Energy Materials | 유기 분자들이 규칙적으로 연결된 골격으로 리튬 금속 전지용 고체 전해질 막을 만들었다. 막에 고정된 음이온(음의 전기를 띤 이온)과 카보닐기(탄소와 산소가 이중 결합한 원자 무리)를 배치해 리튬 이온이 통로 사이를 이동하도록 설계했다. 분자 동역학 모의로 이 이동 경로를 확인했고, 용액에서 합성한 막을 쓴 전지의 반복 충·방전 성능도 평가했다.[^p1] | 1저자 Rak Hyeon Choi·Akshay Gurumoorthi(공동 기여), 교신저자 손창윤·Hye Ryung Byon |
| 2 | 2026 | [Dual Impact of Long-Lived Localized Carriers Induced by Restricted Hole Transfer in Organic Photovoltaics and Photocatalytic Hydrogen Evolution](https://doi.org/10.1002/aenm.70952) · Advanced Energy Materials | 유기 태양전지에서 전하를 꺼내는 데 맞춘 소재가 물속에서 수소를 만드는 광촉매(빛을 받아 반응을 촉진하는 물질)로 쓰일 때는 다르게 작동함을 비교했다. 소재 조합을 바꾸어 빛을 받은 뒤 생긴 전하의 이동을 살폈고, 한곳에 머물며 오래 유지되는 전하가 수소 생성에 유리함을 보였다. 전자 구조 계산과 분자 동역학 모의로 이런 차이를 분자의 전기적 성질과 분자 사이 상호작용에 연결했다.[^p2] | 1저자 Gayoung Ham, 교신저자 손창윤 외 |
| 3 | 2026 | [Design of Optical Transducer for Recognition of Biomolecular Interactions between Bacterial Lipopolysaccharides and Amino Acids](https://doi.org/10.1002/advs.202523658) · Advanced Science | 글루탐산과 아스파르트산이라는 아미노산이 액정과 물의 경계에서 서로 다른 흡착·탈착(표면에 모이거나 표면에서 떨어지는 현상)을 보이는 원리를 실험과 전자 구조 계산으로 살폈다. 아미노산의 전기적 상태와 다른 생체 분자와의 결합이 액정의 광학 반응을 바꾸었다. 이 원리를 이용해 살모넬라의 존재를 스스로 인식하고 빛의 변화로 알리는 액정 장치를 보였다.[^p3] | 1저자 Yena Choi·Sangmin Lee(공동 기여), 교신저자 손창윤 외 |
| 4 | 2026 | [Perfluoroarene-Based Interlayers Unlock High External Quantum Efficiency in Planar Heterojunction OPDs](https://doi.org/10.1002/adfm.202517827) · Advanced Functional Materials | 유기 광다이오드(OPD, Organic Photodiode, 유기 물질이 빛을 전기 신호로 바꾸는 소자)에서 빛이 없을 때의 전류를 억제하면서 빛을 받을 때의 전류를 높이는 문제를 다뤘다. 과불소 방향족 분자로 만든 중간 층을 넣어 계면에서 전하가 분리되는 과정을 조절했다. 여러 전자 공여체(전자를 다른 물질에 주는 물질)에서 적용 가능성을 살폈고, 신호를 읽는 회로에 통합한 장치도 평가했다.[^p4] | 1저자 Seyeon Baek, 공동 저자 손창윤 |
| 5 | 2024 | [Molecular Engineering of Coordination Ligand for Multifunctional Sol–Gel Oxides](https://doi.org/10.1002/adma.202409906) · Advanced Materials | 금속과 결합하는 분자인 리간드를 바꾸어, 용액에서 만드는 산화물에 빛으로 무늬를 만드는 기능과 전기적 성질을 함께 부여했다. 여러 종류의 절연체와 반도체 산화물에 적용할 리간드를 합성했고, 이를 이용한 트랜지스터(전기 신호로 전류를 조절하는 소자)를 만들었다. 이런 리간드 교환이 여러 기능을 갖춘 산화물 전자 소재를 만드는 방법이 될 가능성을 제시했다.[^p5] | 1저자 Juhyeok Lee·Syed Zahid Hassan(랩 공동 기여 표기), 공동 저자 손창윤 |
| 6 | 2026 | [From Clustered Motion to Percolation: Unveiling Correlated Lithium Ion Dynamics in Ionic Liquid Mixtures via an Ab Initio Force Field](https://doi.org/10.1021/acs.jctc.5c01679) · Journal of Chemical Theory and Computation | 리튬염과 이온성 액체가 섞인 전해질에서 전자 분극을 명시적으로 반영하는 힘장을 개발했다. 리튬 이온 농도가 낮은 조건에서 이온의 이동과 전류 흐름을 예측하고, 주변 이온의 배열이 힘장에 따라 달라짐을 보였다. 리튬염 농도가 높아지면서 이온들이 함께 움직이는 방식이 바뀌었고, 전체 이온 전류에서 리튬 이온이 담당하는 비율은 처음 줄었다가 연결된 이온 망이 형성되면서 다시 늘어났다.[^p6] | 1저자 Seungwon Jeong, 교신저자·마지막 저자 손창윤 |
| 7 | 2025 | [Tailoring of Selective Chemo-Responsiveness in Liquid Crystals via Organic Ionic Plastic Crystals](https://doi.org/10.1002/smll.202410079) · Small | 액정 경계에 유기 이온성 유연결정(이온의 위치 배열 질서를 유지하면서 회전 방향의 질서는 흐트러진 결정)을 두고, 분자 사이의 상호작용을 계산과 실험으로 살폈다. 이온성 분자의 머리 부분과 사슬, 반대 전하 이온이 액정 배열과 화학 자극에 대한 반응을 어떻게 바꾸는지 밝혔다. 이 원리로 아세트산과 프로피온산에 대한 분자 결합을 구분하는 소재 설계 방향을 제시했다.[^p7] | 1저자 Jin-Kang Choi·Kyeong-Jun Jeong(공동 기여), 교신저자 손창윤 외 |

## 교수와 전문 분야

손창윤 교수는 서울대학교에서 화학 학사(2005)와 석사(2011)를, University of Wisconsin-Madison에서 화학 박사(2017)를 받았다. California Institute of Technology 박사후연구원(2017–2020), POSTECH 화학과 조교수(2020–2024)를 거쳐 2024년 서울대 화학부에 부임했다. 연구실 교수 소개는 2024년 여름 연구그룹을 서울대로 옮겼다고 밝힌다. 학과 교수 소개의 현재 직급은 부교수다.[^faculty][^profile]

전문 분야의 중심은 전하를 띤 고분자·액체·생체 분자를 설명하는 분자 모형과 계산 방법의 개발이다. 교수 소개는 예측 가능한 힘장, 다중 스케일 모의, 기계학습과 계산 자료 분석을 연구 접근으로 든다.[^profile] 서울대 소속의 논문에서는 고체 전해질의 이온 이동, 이온성 액체를 설명하는 분극 힘장, 유기 에너지 소재의 전하 거동, 액정 계면의 분자 인식과 화학적 선택성, 전자 소자용 분자·계면 설계로 그 접근을 확장하고 있다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7]

## 응용 분야

연구실이 직접 목표로 드는 응용은 차세대 전지와 착용형 장치의 전해질, 산화 그래핀 막을 이용한 물 정제, 기능성 생체막·단백질에서 일어나는 분자 과정의 이해다.[^research] 대표 논문은 리튬 금속 전지용 고체 전해질, 태양전지·광촉매용 유기 소재, 세균을 광학적으로 인식하는 액정 장치, 광검출 소자와 산화물 트랜지스터를 다룬다.[^p1][^p2][^p3][^p4][^p5]

## 구성원

2026년 11월 5일 Team의 Researchers 구획에 게시된 18명으로, 박사후연구원 2명·박사과정 14명·석사과정 2명이다. 과정과 현재 구성원 여부는 Team의 표기이며, 연구 관심·경험과 학력은 각 개인 소개 시점의 내용이다. 학력 칸의 연도는 해당 입학·학위 표기다.[^team] “대표 논문 참여”는 위 표의 번호이며, 저자 이름이 완전히 일치할 때 같은 이름의 저자를 같은 사람으로 보아 표시했다. 몬테카를로(Monte Carlo)는 무작위로 뽑은 표본으로 값을 계산하는 방법이고, pH는 용액의 산성·염기성 정도를 나타내는 값이다.

| 이름 | 과정 | 학력(개인 소개) | 연구 관심·경험(개인 소개) | 대표 논문 참여 |
|---|---|---|---|---|
| Seungwon Jeong[^member-seungwon] | 박사후연구원 | POSTECH Convergence IT Engineering 학사(2020), POSTECH 화학 박사(2026) | 분자 동역학·기계학습을 이용한 고분자 전해질의 이온 동역학 | 6 |
| Yein Lim[^member-yein] | 박사후연구원 |  |  |  |
| Chaemin Jeong[^member-chaemin] | 박사과정 | POSTECH 화학 학사·석사 | 분자 동역학으로 연구하는 제한된 공간의 물 |  |
| Juhwa Lee[^member-juhwa] | 박사과정 | PNU 화학 학사(2022) | 분자 동역학으로 연구하는 생체 분자 |  |
| Sangmin Lee[^member-sangmin] | 박사과정 | POSTECH 화학·수학 복수전공 학사, POSTECH 화학 석사 | 반응성 분자 동역학과 핵생성 과정의 계산 모형 | 3 |
| Seonghyeon Kang[^member-seonghyeon] | 박사과정 | DGIST Integrated B.S.(주전공 화학, 부전공 물리학) | 분자 동역학으로 연구하는 전도성 고분자 | 2, 4 |
| Seungbin Hong[^member-seungbin] | 박사과정 | CNU 화학공학 학사 | 이온성 액체와 고분자 흡착의 분자 동역학 |  |
| Donguk Shin[^member-donguk] | 박사과정 | CBNU 화학·화학공학 복수전공 학사 | 고분자 전해질(polyelectrolyte)의 분자 동역학 | 6 |
| Inyong Ji[^member-inyong] | 박사과정 | POSTECH 화학 학사 | 나노클러스터의 분자 동역학 |  |
| Ayodele Faleti[^member-ayodele] | 석사과정 | Federal University of Technology, Akure, Nigeria 산업화학 학사(2021) | 일정한 pH에서의 분자 동역학으로 연구하는 단백질·리간드 상호작용 |  |
| Jeongsik Lee[^member-jeongsik] | 석사과정 | POSTECH 화학 학사(2023) | 도킹 모의(분자들이 결합할 배치를 예측하는 계산) |  |
| Ho-hyeon Ann[^ann] | 박사과정 | 서울대학교 화학·수학 복수전공 학사(2025) | 몬테카를로·분자 동역학 모의의 계산 모형 결합 |  |
| Jaehyuk Lee[^jae] | 박사과정 |  | 분자 동역학 모의 | 2 |
| Jiseok Kang[^member-jiseok] | 박사과정 | POSTECH 화학 학사 | 전도성 고분자 결정 구조에서 액체 방울의 젖음과 리튬 이온 전해질(연구한 주제) |  |
| Sangwon Bae[^member-sangwon] | 박사과정 | POSTECH 화학 학사 | 여러 입자의 상호작용을 함께 반영한 제1원리 힘장 개발 | 1 |
| Yun Shin[^member-shinyun] | 박사과정 | 고려대학교 생명과학 학사, 서울대학교 의생명과학 석사 | 인지질 이중층에서 막단백질 구조 변화의 분자 동역학 |  |
| HyunJu Song[^member-hyunju] | 박사과정 | DGIST 학사(주전공 Computer Science, 부전공 Chemistry) |  |  |
| Sanghak Kim[^member-sanghak] | 박사과정 | POSTECH 화학·수학 복수전공 학사(2026) | 분자 동역학 모의 |  |

## 졸업생과 이전 구성원

Team의 Alumni에 게시된 4명이다. 손창윤 교수의 POSTECH(2020–2024)과 서울대(2024–) 시기에 걸친 연구실의 이전 구성원 목록이며, 개인별 기간은 게시된 경우에만 적었다. 진로는 Team 표기이고, 이전 과정·연구 관심·학력은 개인 소개 시점의 내용이다. 학력 칸의 연도와 연구실 활동 기간은 구분한다.[^team]

| 이름 | 이전 과정·활동 기간 | Team의 진로 | 학력(개인 소개) | 연구 관심·경험(개인 소개) |
|---|---|---|---|---|
| Kyeong-jun Jeong[^kjeong] | 박사후연구원(2025년 여름까지) | Assistant Professor at KGU | KAIST 화학 학사(2014), University of Wisconsin-Madison 박사(2020) | 분자 동역학으로 연구하는 연성 소재의 자기조립·상거동과 분자 설계 원리 |
| Akshay Gurumoorthi[^member-akshay] | 석사과정(이전 POSTECH 소개) | PhD student at UIUC | IIT Delhi Engineering Physics B.Tech.(2021); UIUC 화학공학 박사과정(2024년 8월부터) | 분자 모의의 유기 골격 구조 응용 |
| Minhye Kim[^member-minhye] | 박사과정(개인 소개 표기) | Former Student | EWHA W.U. 화학 학사·석사 | 조대 입자 분자 동역학으로 연구하는 막단백질·핵산 |
| Junho Lim[^member-junho] | 학부생(이전 POSTECH 소개) | PhD student at UC Berkeley | POSTECH 화학·물리학 복수전공(2020년부터라는 개인 소개 표기) | 유연한 지질이 지질방울로 함께 이동하는 과정의 분자 동역학; 비평형 조건의 확률 과정(관심) |

## 최근 논문 목록 (2021–2026)

Publications의 2021–2026년 구역 27편 가운데 최초 출판일이 2021년 10월 22일 전인 2021년 논문 3편을 제외한 출판 논문 24편(2022–2026년), 별도 Accepted 구획의 게재 승인 1편, Submitted 4편 중 심사 중 3편이다. 출판 논문의 연도는 누리집 연도 구역 표기다. 손창윤 교수의 서울대 부임 전인 POSTECH 시기 논문을 포함한다. Accepted와 Submitted에는 연도가 없으므로 아래 “연도 표기 없음” 구획에 두고 상태를 표시했다. 누리집은 *를 교신저자, †를 공동 기여로 설명하며, ‡는 뜻을 풀지 않은 누리집 표시다.[^pubs][^dates]

**2026**

- Dohyun Kim†, Sungryong Kim†, Seungbin Hong† , Jeongsu Kim, Giwon Shin, Minjun Kim, Hong Chul Moon\*, Chang Yun Son\* , Taiho Park‡. "Architecting Percolating Ionic Networks in Spiro-OMeTAD via Radical-Dopant Cooperation for Enhanced Hole Transport and Stability". *ACS Energy Letters , 2026*. <https://doi.org/10.1021/acsenergylett.6c01191>.
- Won Jun Pyo, Kyeong-Jun Jeong , Jordan Shanahan, Justin Neu, Junseo Kim, Xiaowei Zhong, Chang Yun Son\* , Wei You\*, Dae Sung Chung\*. "Ion–backbone accessibility enables unity doping efficiency in organic electrochemical transistors". *Nature Communications , 2026 , 17 , 8644*. <https://doi.org/10.1038/s41467-026-75568-7>.
- Gayoung Ham, Sanghyeok An, Wooteak Jung, Hyun Min Kwon, Seonghyeon Kang , Jaehyuk Lee , Sowon Kim, Changwoo Park, Damin Lee, Young Yong Kim, Sungjin Jo, Chang Yun Son\* , Sae Byeok Jo\*, Dae Sung Chung\*, Hyojung Cha\*. "Dual Impact of Long‐Lived Localized Carriers Induced by Restricted Hole Transfer in Organic Photovoltaics and Photocatalytic Hydrogen Evolution". *Advanced Energy Materials , 2026 , Early View*. <https://doi.org/10.1002/aenm.70952>.
- Seyeon Baek, Sangjun Lee, Jubin Kang, Seonghyeon Kang , Syed Zahid Hassan, Jungmin Oh, Sanghyeok An, Kyo Bin Park, Hye Ryun Sim, Chang Yun Son , Seong-Jin Kim, Dae Sung Chung\*. "Perfluoroarene‐Based Interlayers Unlock High External Quantum Efficiency in Planar Heterojunction OPDs". *Advanced Functional Materials , 2026 , 36 (46), e17827*. <https://doi.org/10.1002/adfm.202517827>.
- Jieun Kwon†, Syed Zahid Hassan†, Gayoung Ham, Seonghyeon Kang , Geoneop Choi, Sanghyeok An, Hye Ryun Sim, Suryeon Jang, Chang Yun Son\* , Hyojung Cha\*, Dae Sung Chung\*. "Visible‐Light Photoprogrammable Transistors Enabled by an All‐Organic Triplet‐Sensitized Diarylethene Channel Layer". *Advanced Optical Materials , 2026 , 14 (13), e03525*. <https://doi.org/10.1002/adom.202503525>.
- Yena Choi†, Sangmin Lee† , Jin-Kang Choi, Hyunsoo Han, Yeongseon Choi, Jun-Hyung Im, Hyein Kim, Sangmin Jeon, Minjae Lee\*, Chang Yun Son\* , Young-Ki Kim\*. "Design of Optical Transducer for Recognition of Biomolecular Interactions between Bacterial Lipopolysaccharides and Amino Acids". *Advanced Science , 2026 , 13 (29), e23658*. <https://doi.org/10.1002/advs.202523658>.
- Seungwon Jeong , Donguk Shin , Chang Yun Son\* . "From Clustered Motion to Percolation: Unveiling Correlated Lithium Ion Dynamics in Ionic Liquid Mixtures via an Ab Initio Force Field". *Journal of Chemical Theory and Computation , 2026 , 22 (1), 575-587*. <https://doi.org/10.1021/acs.jctc.5c01679>.

**2025**

- Minkyung Kim, Jungyeon Kim, Hee Myeong Wang, Hyemin Kim, Dohee Ahn, Jeongsik Lee , Chang Yun Son\* , Sang Jeon Chung\*, Min Hyeon Shin\*, Hyun-Suk Lim\*. "In Situ Click Chemistry Screen Facilitated by an On‐Nanoparticle DNA‐Encoded Library Identifies Highly Selective and Potent Peptoid Ligands for a Phosphatase". *Angewandte Chemie International Edition , 2025 , 64 (41), e202511606*. <https://doi.org/10.1002/anie.202511606>.
- Rak Hyeon Choi†, Akshay Gurumoorthi† , Sangwon Bae , Chang Yun Son\* , Hye Ryung Byon\*. "Room‐Temperature Single Li⁺ Ion Conducting Organic Solid‐State Electrolyte with 10⁻⁴ S cm⁻¹ Conductivity for Lithium‐Metal Batteries". *Advanced Energy Materials , 2025 , 15 (47), e04143*. <https://doi.org/10.1002/aenm.202504143>.
- Seong Hyeon Kim, Seonghyeon Kang , Minyoung Jeong, Jisang Park, Seungwon Jeong , Hyunji Lee, Chang Yun Son , Kilwon Cho\*. "Energetic Disorder in Doped P3HT: A Crucial Factor in Overcoming Coulomb Binding for Free Charge Generation". *ACS Nano , 2025 , 19 (32), 29265-29275*. <https://doi.org/10.1021/acsnano.5c04666>.
- Daegun Kim†, Jiwoo Min†, Kyeong-Jun Jeong† , Eunsol Ok, Jaemin Im, Hyun Ho Choi, Giwon Lee, Chang Yun Son\* , Kilwon Cho\*. "Stoichiometric anion exchange by a low-dielectric-constant solvent for highly-doped conjugated polymers with enhanced environmental stability". *Journal of Materials Chemistry A , 2025 , 13 , 18966-18977*. <https://doi.org/10.1039/d5ta01703c>.
- Hyesung Jo, Seonmin Ju, Minhye Kim , Jiyun Beon, Se-Young Jang, Seung Pil Pack, Chang Yun Son , Jong-Seo Kim, Seung Soo Oh \* . "Aptamer-Guided, Hydrolysis-Resistant Deoxyoxanosine Enables Epitope- and Moiety-Selective Conjugation to Nonengineered Proteins Even in Complex Environments". *Journal of the American Chemical Society , 2025 , 147 (11), 9328–9340*. <https://doi.org/10.1021/jacs.4c15674>.
- Jin-Kang Choi†, Kyeong-Jun Jeong† , Yena Choi, Won-Sik Kim, Jong Chan Shin, Jun-Hyung Im, Hyein Kim, Minjae Lee \* , Chang Yun Son \* , Young-Ki Kim \* . "Tailoring of Selective Chemo‐Responsiveness in Liquid Crystals via Organic Ionic Plastic Crystals". *Small , 2025 , 2410079*. <https://doi.org/10.1002/smll.202410079>.

**2024**

- Juhyeok Lee†, Syed Zahid Hassan†, Hye Ryun Sim, Sangjun Lee, Kyeong-Jun Jeong , Jieun Kwon, Chang Yun Son , Dae Sung Chung \* . "Molecular Engineering of Coordination Ligand for Multifunctional Sol-gel Oxides". *Advanced Materials , 2024 , 36 (46), 2409906*. <https://doi.org/10.1002/adma.202409906>.
- Sanghyeok An†, Kyeong-Jun Jeong †, Syed Zahid Hassan, Gayoung Ham, Seonghyeon Kang , Juhyeok Lee, Hyeonjong Ma, Jieun Kwon, Sang Young Jeong, Jiwoong Yang, Han Young Woo, Han-Hee Cho, Hyojung Cha \* , Chang Yun Son \* , Dae Sung Chung \*. "Hydrophilic Photocrosslinkers as a Universal Solution to Endow Water Affinity to a Polymer Photocatalyst for an Enhanced Hydrogen Evolution Rate". *Advanced Science , 2024 , 11 (28), 2309786*. <https://doi.org/10.1002/advs.202309786>.

**2023**

- Hyebin Yoo, Hyun-Ro Lee, Soon-Bo Kang, Juhwa Lee , Kunwoong Park, Hyunjae Yoo, Jinmin Kim, Taek Dong Chung, Kyung-Mi Lee, Hyun-Ho Lim \* , Chang Yun Son \* , Jeong-Yun Sun \* , Seung Soo Oh \*. "G‐Quadruplex‐Filtered Selective Ion‐to‐Ion Current Amplification for Non‐Invasive Ion Monitoring in Real Time". *Advanced Materials , 2023 , 35 (42), 2303655*. <https://doi.org/10.1002/adma.202303655>.
- Soumen Dutta, Akshay Gurumoorthi , Shinbi Lee, Sun Woo Jang, Nitee Kumari, Yu-Rim Hong, Wonyong Choi, Chang Yun Son \* , In Su Lee \* . "Sculpting In‐plane Fractal Porous Patterns in Two‐Dimensional MOF Nanocrystals for Photoelectrocatalytic CO 2 Reduction". *Angewandte Chemie , 2023 , 62 (28), e202303890*. <https://doi.org/10.1002/ange.202303890>.
- Seong Hyeon Kim†, Seungwon Jeong †, Daegun Kim, Chang Yun Son \* , Kilwon Cho \* . "Effects of Connecting Polymer Structure and Morphology at Inter‐Tube Junctions on the Thermoelectric Properties of Conjugated Polymer/Carbon Nanotube Composites". *Advanced Electronic Materials , 2023 , 9 (7), 2201293*. <https://doi.org/10.1002/aelm.202201293>.

**2022**

- Kyeong-jun Jeong †, Seungwon Jeong †, Sangmin Lee †, Chang Yun Son \* . "Predictive Molecular Models for Charged Materials Systems: From Energy Materials to Biomacromolecules". *Advanced Materials , 2022 , 35 (4), 2204272*. <https://doi.org/10.1002/adma.202204272>.
- Minjong Lee, Byunghwa Kang, Juhwa Lee , Jisun Lee, Sang Taek Jung, Chang Yun Son, Seung Soo Oh \* . "De novo selected hACE2 mimics that integrate hotspot peptides with aptameric scaffolds for binding tolerance of SARS-CoV-2 variants". *Science Advances , 2022 , 8 (43), eabq6207*. <https://doi.org/10.1126/sciadv.abq6207>.
- Rui-Yang Wang, Seungwon Jeong , Hyeonseong Ham, Jihoon Kim, Hojun Lee, Chang Yun Son \* , Moon Jeong Park \* . "Superionic Bifunctional Polymer Electrolytes for Solid‐State Energy Storage and Conversion". *Advanced Materials , 2022 , 35 (4), 2203413*. <https://doi.org/10.1002/adma.202203413>.
- So-Hee Son, Gyuri Park, Junho Lim , Chang Yun Son \* , Seung Soo Oh \* , Ju Young Lee \* . "Chain flexibility of medicinal lipids determines their selective partitioning into lipid droplets". *Nature Communications , 2022 , 13 (1), 3612*. <https://doi.org/10.1038/s41467-022-31400-6>.
- Jaeyoung Hong, Jee-Hwan Bae, Hyesung Jo, Hee-Young Park, Sehyun Lee, Sung Jun Hong, Hoje Chun, Min Kyung Cho, Juyoung Kim, Joodeok Kim, Yongju Son, Haneul Jin, Jin-Yoo Suh, Sung-Chul Kim, Ha-Kyung Roh, Kyu Hyoung Lee, Hyung-Seok Kim, Kyung Yoon Chung, Chang Won Yoon, Kiryeong Lee, Seo Hee Kim, Jae-Pyoung Ahn, Hionsuck Baik, Gyeung Ho Kim, Byungchan Han, Sungho Jin, Taeghwan Hyeon, Jungwon Park, Chang Yun Son \* , Yongsoo Yang \* , Young-Su Lee \* , Sung Jong Yoo \* , Dong Won Chun \*. "Metastable hexagonal close-packed palladium hydride in liquid cell TEM". *Nature , 2022 , 603 , 631-636*. <https://doi.org/10.1038/s41586-021-04391-5>.
- Jihoon Kim, Kyeong-Jun Jeong , Kyoungwook Kim, Chang Yun Son , Moon Jeong Park \* . "Enhanced Electrochemical Properties of Block Copolymer Electrolytes with Blended End-Functionalized Homopolymers". *Macromolecules , 2022 , 55 (6), 2028-2040*. <https://doi.org/10.1021/acs.macromol.1c02461>.

**연도 표기 없음**

- Son, S.-H.†; Bae S.† ; Moon, S.Y.; Kim, M. ; Oh, S.S.\*; Son, C.Y.\* ; Lee, J.Y.\*. "Spatial Control of Enzyme Orientation at Lipid Droplet Interfaces Enables Regio- and Chemo-selective Metabolic Flux". *Science Advances, 게재 승인*.
- Jeong, K.-J. ; Son, C.Y\* . "Importance of Collective Ion Transport in Molecular Weight Dependence of Conductivity in Block Copolymer Electrolytes". *심사 중*.
- Kang, T.†; Park, C. B.†; Lim, Y.† ; Son, C. Y.\* ; Kang, J.\*. "Chiral Chain Rotation Amplifies Fracture Resistance and Induces Mechanical Anisotropy in Supramolecular Elastomers". *심사 중*.
- Lee, M.; Kang, T.; Lee, J. ; Kang, S. ; Son, C. Y. ; Kang, J.\*. "On-Demand Self-Healing via Molecular Photoswitching". *심사 중*.

## 수상과 선정

2021년 10월 22일–2026년 10월 22일 범위에 드는 수상 글 8건이다. 손창윤 교수의 서울대 부임 전 POSTECH 시기 수상을 포함한다. 날짜는 소식 글의 게시 날짜이며, 수상자의 이름·줄임말은 누리집 표기다.[^awards]

- 2026-04-16 · 손창윤 교수, TCI 고분자화학 신진학술상 수상
- 2026-04-10 · Sangwon(누리집 표기), 한국고분자학회 춘계학술대회 포스터 발표상 수상
- 2025-07-05 · Sangwon(누리집 표기), 대한화학회 물리화학분과 하계 심포지엄 포스터상 수상
- 2025-07-04 · KJ(누리집 표기), Nano Korea 2025 Young Scientist Award 수상
- 2024-10-17 · 손창윤 교수, KCS-ACES Early Career Award 수상
- 2024-07-05 · Seonghyeon(누리집 표기), Nano Korea 2024 포스터 발표 은상 수상
- 2024-06-26 · Seungwon·Seonghyeon(누리집 표기), 한일 분자과학 심포지엄·대한화학회 물리화학분과 제143회 하계 심포지엄 최우수 포스터상 수상
- 2023-07-10 · 손창윤 교수, Asian Chemical Congress 2023 Distinguished Young Chemist Award 수상

## 연락과 위치

- 교수 연구실: 서울대학교 화학부 502동 221호, 02-880-6652[^faculty][^contact]
- 학생 연구실: 서울대학교 화학부 502동 208호, 02-880-6656[^faculty][^contact]
- 교수 이메일: changyunson@snu.ac.kr[^contact]
[^faculty]: 서울대학교 자연과학대학 화학부, 손창윤 교수 소개 <https://chem.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=95&sc=y> (2026-11-05 열람).
[^research]: Son Research Lab, Research <https://songroup.github.io/sonlab-website/research/> (2026-11-05 열람).
[^profile]: Son Research Lab, Chang Yun Son <https://songroup.github.io/sonlab-website/members/changyunson.html> (2026-11-05 열람).
[^resources]: Son Research Lab, Resources <https://songroup.github.io/sonlab-website/resources/> (2026-11-05 열람).
[^team]: Son Research Lab, Team <https://songroup.github.io/sonlab-website/team/> (2026-11-05 열람).
[^ann]: Son Research Lab, Ho-hyeon Ann <https://songroup.github.io/sonlab-website/members/hohyeon.html> (2026-11-05 열람).
[^jae]: Son Research Lab, Jaehyuk Lee <https://songroup.github.io/sonlab-website/members/jaehyuk.html> (2026-11-05 열람).
[^kjeong]: Son Research Lab, Kyeong-jun Jeong <https://songroup.github.io/sonlab-website/members/kjeong.html> (2026-11-05 열람).
[^pubs]: Son Research Lab, Publications <https://songroup.github.io/sonlab-website/publications/> (2026-11-05 열람).
[^awards]: Son Research Lab, Awards <https://songroup.github.io/sonlab-website/awards/> (2026-11-05 열람).
[^contact]: Son Research Lab, Contact <https://songroup.github.io/sonlab-website/contact/> (2026-11-05 열람).
[^member-seungwon]: Son Research Lab, Seungwon Jeong <https://songroup.github.io/sonlab-website/members/seungwon.html> (2026-11-05 열람).
[^member-yein]: Son Research Lab, Yein Lim <https://songroup.github.io/sonlab-website/members/yein.html> (2026-11-05 열람).
[^member-chaemin]: Son Research Lab, Chaemin Jeong <https://songroup.github.io/sonlab-website/members/chaemin.html> (2026-11-05 열람).
[^member-juhwa]: Son Research Lab, Juhwa Lee <https://songroup.github.io/sonlab-website/members/juhwa.html> (2026-11-05 열람).
[^member-sangmin]: Son Research Lab, Sangmin Lee <https://songroup.github.io/sonlab-website/members/sangmin.html> (2026-11-05 열람).
[^member-seonghyeon]: Son Research Lab, Seonghyeon Kang <https://songroup.github.io/sonlab-website/members/seonghyeon.html> (2026-11-05 열람).
[^member-seungbin]: Son Research Lab, Seungbin Hong <https://songroup.github.io/sonlab-website/members/seungbin.html> (2026-11-05 열람).
[^member-donguk]: Son Research Lab, Donguk Shin <https://songroup.github.io/sonlab-website/members/donguk.html> (2026-11-05 열람).
[^member-inyong]: Son Research Lab, Inyong Ji <https://songroup.github.io/sonlab-website/members/inyong.html> (2026-11-05 열람).
[^member-ayodele]: Son Research Lab, Ayodele Faleti <https://songroup.github.io/sonlab-website/members/ayodele.html> (2026-11-05 열람).
[^member-jeongsik]: Son Research Lab, Jeongsik Lee <https://songroup.github.io/sonlab-website/members/jeongsik.html> (2026-11-05 열람).
[^member-jiseok]: Son Research Lab, Jiseok Kang <https://songroup.github.io/sonlab-website/members/jiseok.html> (2026-11-05 열람).
[^member-sangwon]: Son Research Lab, Sangwon Bae <https://songroup.github.io/sonlab-website/members/sangwon.html> (2026-11-05 열람).
[^member-shinyun]: Son Research Lab, Yun Shin <https://songroup.github.io/sonlab-website/members/shinyun.html> (2026-11-05 열람).
[^member-hyunju]: Son Research Lab, HyunJu Song <https://songroup.github.io/sonlab-website/members/hyunju.html> (2026-11-05 열람).
[^member-sanghak]: Son Research Lab, Sanghak Kim <https://songroup.github.io/sonlab-website/members/sanghak.html> (2026-11-05 열람).
[^member-akshay]: Son Research Lab, Akshay Gurumoorthi <https://songroup.github.io/sonlab-website/members/akshay.html> (2026-11-05 열람).
[^member-minhye]: Son Research Lab, Minhye Kim <https://songroup.github.io/sonlab-website/members/minhye.html> (2026-11-05 열람).
[^member-junho]: Son Research Lab, Junho Lim <https://songroup.github.io/sonlab-website/members/junho.html> (2026-11-05 열람).
[^dates]: Crossref 등록 출판 날짜, PNAS <https://api.crossref.org/works/10.1073/pnas.2107987118>, <https://api.crossref.org/works/10.1073/pnas.2020615118>, Angewandte Chemie International Edition <https://api.crossref.org/works/10.1002/anie.202103827> (2026-11-05 열람).
[^p1]: R. H. Choi 외, H. R. Byon, Advanced Energy Materials 15, e04143 (온라인 2025-10-05). <https://doi.org/10.1002/aenm.202504143> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202504143> (2026-11-05 열람).
[^p2]: G. Ham 외, H. Cha, Advanced Energy Materials 16, e70952 (온라인 2026-04-16). <https://doi.org/10.1002/aenm.70952> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.70952> (2026-11-05 열람).
[^p3]: Y. Choi 외, Y.-K. Kim, Advanced Science 13, e23658 (온라인 2026-03-12). <https://doi.org/10.1002/advs.202523658> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202523658> (2026-11-05 열람).
[^p4]: S. Baek 외, D. S. Chung, Advanced Functional Materials 36, e17827 (온라인 2026-04-13). <https://doi.org/10.1002/adfm.202517827> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202517827> (2026-11-05 열람).
[^p5]: J. Lee 외, D. S. Chung, Advanced Materials 36, 2409906 (온라인 2024-09-27). <https://doi.org/10.1002/adma.202409906> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202409906> (2026-11-05 열람).
[^p6]: S. Jeong, D. Shin, C. Y. Son, Journal of Chemical Theory and Computation 22, 575-587 (2026). <https://doi.org/10.1021/acs.jctc.5c01679> 초록 기준(OpenAlex 등록 초록). 등록 발행일 2025-12-29(Semantic Scholar 표기). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index,authorships&filter=doi:10.1002/adfm.202517827|10.1002/adma.202409906|10.1002/advs.202523658|10.1002/aenm.202504143|10.1002/aenm.70952|10.1002/anie.202103827|10.1002/smll.202410079|10.1021/acs.jctc.5c01679|10.1038/s41467-022-31400-6|10.1039/d5ta01703c|10.1126/sciadv.abq6207> (2026-11-05 열람).
[^p7]: J.-K. Choi 외, Y.-K. Kim, Small, 2410079 (2025). <https://doi.org/10.1002/smll.202410079> 초록 기준. 초록 원문 <https://api.crossref.org/works/10.1002/smll.202410079> (2026-11-05 열람).

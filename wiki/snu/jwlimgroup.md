# 에너지 및 재료 분석화학 연구실 (Battery and Energy Research Group)

**서울대학교 자연과학대학 화학부 · 임종우 부교수**

- 분야: 전지 소재의 분석화학·물리화학, 작동 중 관찰, 계산과 자동 실험, 전기화학 촉매[^dept][^overview]
- 대분야: 화학
- 태그: 이차전지 소재[^cathode][^metal], 전고체 전지[^solid], 전기화학 촉매[^catalyst], 이산화탄소 전환[^catalyst], 자율 실험실·AI 실험 설계[^sdl], 제1원리 계산[^computation], 과학·공학 AI[^ai][^computation], X선 영상·회절[^cathode][^p2]
- 누리집: <https://jwlimgroup.imweb.me/>
- 근거와 출처: [에너지 및 재료 분석화학 연구실 근거 페이지](jwlimgroup-sources.md)

> 전지 안에서 리튬이 이동하고 재료가 변하는 과정을 관찰하며, 그 원리로 전지 소재·제조 방법과 전기화학 촉매를 설계하는 연구실이다.

## 무엇을 연구하나

연구실의 중심은 에너지(일을 하거나 변화를 일으킬 수 있는 능력)를 저장·변환하는 재료다. 분석화학(물질의 종류·양·구조 등을 알아내는 화학 분야)과 물리화학(물질의 성질과 화학 변화의 원리를 물리 법칙으로 설명하는 분야)을 바탕으로, 충전해 다시 쓰는 이차전지의 재료가 만들어지고 작동하고 열화되는 과정을 연구한다. 열화는 사용이나 시간의 경과로 재료·장치의 성질과 성능이 변해 나빠지는 현상이다.[^dept][^overview]

특히 전지 속 리튬의 이동이 고르지 않을 때 생기는 국소 변화와 재료 손상을 다룬다. 작동 중인 전지를 직접 관찰하는 오페란도(장치가 실제 기능을 수행하는 동안 상태를 측정하는 방식) 엑스선 현미경 기법도 개발한다. 엑스선은 파장이 짧은 전자기파이며, 파장은 파동이 반복되는 공간 간격이고 전자기파는 전기장과 자기장의 변화가 공간으로 전파되는 파동이다. 전기장은 전기를 띤 물체에 전기력이 작용하는 공간의 상태이고, 자기장은 자기력이 작용하는 공간의 상태다. 개별 입자의 내부와 여러 입자가 모인 전극을 함께 살펴보는 것이 특징이다. 전극은 외부 회로와 물질 사이에서 전기를 주고받는 부분이다.[^cathode][^p2]

관찰과 함께 계산·기계학습·자동 실험을 연결한다. 기계학습은 자료에서 규칙을 학습해 예측이나 판단에 사용하는 계산 방법이다. 전지의 용량(저장하고 꺼낼 수 있는 전기의 양)과 수명을 예측하고, 전해질(이온을 이동시켜 전기를 전달하는 물질)의 조합을 찾는다. 이온은 전기를 띤 원자나 원자 무리이며, 원자는 화학 원소의 성질을 유지하는 물질의 기본 단위다. 다른 축에서는 전극에서 일어나는 반응을 촉진하는 전기화학 촉매를 설계해 이산화탄소와 질산 이온을 유용한 물질로 전환한다.[^ai][^computation][^sdl][^catalyst]

## 주요 연구 주제

### 리튬이온 전지 양극의 반응과 변화

리튬이온 전지는 리튬 이온이 전극 사이를 이동하며 충전·방전하는 전지다. 양극재는 방전할 때 전자를 받아들이는 전극의 재료이며, 전자는 음의 전기를 띤 기본 입자다. 연구실은 인산철계와 니켈·망간·코발트계 양극재에서 리튬이 들어가고 나오는 속도와 위치를 연구한다. 전류(단위 시간에 지나가는 전기의 양으로 나타낸 전기를 띤 입자의 흐름)와 리튬 농도의 국소 차이가 재료 내부 응력과 수명에 미치는 영향을 살핀다. 농도는 혼합물의 일정한 양에서 특정 성분이 차지하는 양이며, 응력은 물체 내부의 단위 면적에 작용하는 힘이다.[^cathode]

작동 중 관찰뿐 아니라 가열해 양극재를 만드는 소성(재료를 가열하여 필요한 화학 반응이나 구조 변화를 일으키는 처리) 과정도 분석한다. 대표 논문은 합성 중 입자 안의 조성이 달라지는 원인, 전극의 충전 상태 차이를 측정하는 현미경, 입자 간 배치에 따른 가스 발생을 다룬다. 조성은 물질을 이루는 성분의 종류와 비율이다. 사용 전후 전지에서 열폭주(발열 반응과 온도 상승이 서로를 강화해 온도가 급격히 오르는 현상)가 달라지는 이유도 연구한다.[^p1][^p2][^p3][^p4][^p5]

### 리튬 금속 전지의 전해질과 표면

리튬 금속 전지는 금속 리튬을 음극으로 쓰는 전지다. 음극은 방전할 때 전자를 내놓는 전극이다. 반복 충방전 중 표면 보호층의 균열, 전해질 소모, 반응에 참여하지 못하는 리튬의 축적과 수지상 성장(가지가 갈라지는 형태로 물질이 자라는 현상)을 분석한다. 주사 투과 엑스선 현미경은 엑스선을 위치별로 통과시켜 내부 구조와 화학 상태를 영상으로 얻는 장치다. 이를 써서 고체 전해질 계면층(전극과 전해질 사이에서 생기는 반응 생성물 층)의 화학 조성과 리튬 형상 변화를 살핀다.[^metal]

액체 전해질에서는 불소를 포함하지 않는 희석제(다른 성분의 농도를 낮추기 위해 섞는 물질)를 찾는다. 분자(원자들이 화학 결합으로 묶여 독립된 단위를 이루는 것) 사이의 상호작용을 계산하고, 후보 물질의 성질과 예측의 불확실성을 함께 내는 기계학습 모형을 만든다. 불확실성은 결과나 값이 얼마나 확정되어 있지 않은지를 나타내는 정도다. 고분자(반복되는 기본 단위가 이어져 이루어진 분자)를 쓰는 전해질도 연구하며, 전기적 안정성·부식·전극과의 접촉을 함께 다룬다.[^metal]

### 전고체 전지의 접촉과 제조

전고체 전지는 액체 전해질 대신 고체 전해질을 쓰는 이차전지다. 고체 전극과 전해질의 접촉이 충방전 중 변하고 내부 응력이 생기는 문제를 다룬다. 황화물·할로젠화물 고체 전해질의 안정성과 수분에 의한 열화, 재료를 누르는 압력을 낮추는 제조·작동 방법을 연구한다. 황화물 고체 전해질은 황을 주요 음이온 성분으로 하는 고체 전해질이고, 할로젠화물 고체 전해질은 할로젠 원소를 주요 음이온 성분으로 하는 고체 전해질이다. 음이온은 음의 전기를 띤 원자나 원자 무리다. 할로젠은 불소·염소 등 주기율표의 같은 원소 무리를 가리킨다.[^solid]

실리콘계 음극에서는 충방전에 따른 부피 변화와 고체 사이 접촉 손실을 제어한다. 은·탄소 중간층을 쓰는 무음극 전지는 조립할 때 음극 활물질을 넣지 않고 양극에서 나온 리튬을 충전 중 집전체에 쌓는 방식이다. 활물질은 전극의 전기화학 반응에 참여해 전기를 저장하거나 내놓는 물질이며, 집전체는 전극 안에서 전자를 모아 외부 회로로 전달하는 부분이다. 또 고분자 전해질과 전극 재료를 직접 인쇄해 모양을 설계하는 전지 제조법을 연구한다.[^solid][^p6][^p7]

### 기계학습·원자 수준 계산·자율 실험

전기화학 신호(전기적·화학적 상태에 관한 정보를 전달하는 변화)에서 용량과 수명 예측에 필요한 특징을 추출한다. 분자 구조와 성질을 나타내는 기술자(계산 모형에 넣을 수 있게 대상의 특징을 수치화한 값)를 찾아 전해질 후보를 탐색한다. 물질을 이루는 원자 수준의 계산부터 전지 전체의 예측까지 연결하는 접근이다.[^ai][^computation]

밀도범함수이론은 전자의 밀도로 물질의 전자 상태와 에너지를 계산하는 방법이다. 제일원리 분자동역학은 기본 물리 법칙으로 원자에 작용하는 힘을 구해 그 움직임을 계산하는 방법이며, 기계학습 원자간 퍼텐셜은 원자들의 배치와 에너지·힘 사이의 관계를 자료로 학습한 모형이다. 연구실은 이 방법들을 써서 양극과 전해질의 구조 안정성, 리튬 이동, 시간에 따른 구조 변화를 분석한다. 퍼텐셜은 물체나 입자의 위치·배치에 따라 정해지는 위치에너지 또는 그와 관련된 함수를 뜻한다.[^computation]

자율 실험실(Self-Driving Laboratory)은 계산으로 후보를 고르고, 장비로 전지를 만들고 평가하며, 기계학습이 다음 실험 조성을 제안하는 순환 연구 시스템이다. 연구실은 전해질 성분 선별, 원통형 전지의 자동 혼합·주입·봉합·시험, 다음 실험 제안의 세 부분을 연결해 각 전지 체계에 맞는 전해질을 탐색한다.[^sdl]

### 전기화학 촉매와 반응기

이산화탄소 환원(전자를 받아들이는 화학 변화)에서는 구리계 촉매가 작동 중 어떤 상태로 바뀌는지, 그 변화가 촉매 활성과 선택성에 어떻게 연결되는지 연구한다. 활성은 화학 반응을 일으키는 정도이며, 선택성은 여러 반응이나 생성물 가운데 특정 반응·생성물이 나타나는 비중이다. 구리 산화물에 다른 금속을 첨가해 일산화탄소 전환 효율과 안정성을 조절하고, 질산 이온을 암모니아로 바꾸는 촉매도 개발한다.[^catalyst]

촉매 물질에서 끝나지 않고 반응기(화학 반응을 진행시키는 장치) 구조를 연구한다. 흐르는 전해질을 쓰는 장치, 전극과 이온 교환막을 결합한 장치, 구멍이 있는 고체 전해질 층을 추가하는 장치를 최적화한다. 이온 교환막은 특정 이온을 선택적으로 통과시키는 막이다. 대표 리뷰는 단일 원자 촉매(금속 원자가 서로 떨어져 지지체에 결합한 촉매)를 이용해 이산화탄소를 탄화수소(탄소와 수소로 이루어진 화합물)와 산소를 포함하는 화합물로 바꾸는 연구를 정리한다. 지지체는 촉매 성분을 받쳐 분산시키는 바탕 물질이다.[^catalyst][^p8]

## 대표 논문

양극의 합성·측정·안전, 전고체 전지의 소재·제조, 이산화탄소 전환 촉매를 고르게 보여 주는 8편이다. 연도는 출판사 페이지의 온라인 최초 발행 연도다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자의 역할은 출판사 저자 순서와 교신저자 표시를 따른다.

| 번호 | 연도 | 논문 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2022 | [Solid-State Reaction Heterogeneity During Calcination of Lithium-Ion Battery Cathode](https://doi.org/10.1002/adma.202207076) · Advanced Materials | 양극재를 가열해 만드는 동안 온도에 따른 반응 속도, 리튬 공급원의 이동성, 주변 산소가 입자 내부의 화학 조성을 결정함을 밝혔다. 금속이 다른 물질을 환원시키는 능력의 차이는 국소 구조를 결정했다.[^p1] | 1저자 Sugeun Jo, 교신저자 Jongwoo Lim·Keeyoung Jung |
| 2 | 2024 | [Nanoscale Projection Hard X-ray Microscope for Operando Statistical Analysis of Chemical Heterogeneity in Lithium-Ion Battery Cathodes](https://doi.org/10.1002/smtd.202401087) · Small Methods | 엑스선 영상으로 개별 입자와 전극 범위의 충전 상태 불균일성을 함께 측정하는 현미경을 제시했다. 열화된 전극의 입자별 차이와 가열 합성 중 입자 안팎의 반응 차이를 관찰했다.[^p2] | 1저자 Sugeun Jo, 교신저자 Jongwoo Lim·Jun Lim |
| 3 | 2024 | [Gas Evolution Kinetics in Overlithiated Positive Electrodes and its Impact on Electrode Design](https://doi.org/10.1002/advs.202400568) · Advanced Science | 양극 재료에서 나온 산소의 양이 같아도 재료를 넣은 밀도와 입자 사이 간격에 따라 가스 발생 속도와 양이 달라짐을 보였다. 가스 발생을 관리하려면 개별 입자의 성질과 전극 내부 배치를 함께 고려해야 한다는 결과다.[^p3] | 1저자 Munsoo Song, 교신저자 Jongwoo Lim |
| 4 | 2024 | [Thermal Runaway Mechanism in Ni-Rich Cathode Full Cells of Lithium-Ion Batteries: The Role of Multidirectional Crosstalk](https://doi.org/10.1002/adma.202402024) · Advanced Materials | 음극에서 나온 에틸렌이 양극의 산소 발생을 촉진하고, 그 산소가 음극으로 돌아가 에틸렌 생성을 늘리는 순환을 밝혔다. 이산화탄소도 음극 리튬과 반응해 열폭주에 관여했으며, 에틸렌과 산소 생성을 막는 음극 코팅을 개발했다.[^p4] | 1저자 Sugeun Jo, 교신저자 Jongwoo Lim |
| 5 | 2025 | [Electrochemical Abuse-Driven Thermal Runaway in Lithium-Ion Batteries: Evolution From Beginning-of-Life to End-of-Life](https://doi.org/10.1002/adfm.202521009) · Advanced Functional Materials | 새 전지와 수명을 다한 전지의 열폭주를 비교하고 열화 요인을 나누어 분석했다. 음극 표면에 쌓인 리튬은 열폭주 시작 온도를 낮췄고, 활성 리튬량의 변화는 전체 방출 열량을 대체로 줄였다. 전해질 소모는 총열량에는 큰 영향을 주지 않으면서 발열 반응을 높은 온도로 미뤘다.[^p5] | 1저자 San Hwang·Sungjae Seo(공동 기여), 교신저자 Jongwoo Lim |
| 6 | 2025 | [Comprehensive Si Anode Design for Sulfide-Based all-Solid-State Batteries: Insights into Si-Electrolyte Synergy for Mitigating Contact Loss](https://doi.org/10.1002/adfm.202504739) · Advanced Functional Materials | 알루미늄·실리콘 음극을 도입해 처음 팽창한 뒤 부피 변화를 안정시키고 고체 전해질과의 접촉을 유지했다. 탄성 회복이 가능한 전해질과의 조합으로 접촉 손실을 억제하고, 충방전을 되풀이할 때 원래 상태로 돌아오는 성질을 높였다.[^p6] | 1저자 Youngjin Song·Sungjin Cho·Suhwan Kim(공동 기여), 공저자 Jongwoo Lim, 교신저자 Yong Min Lee·Soojin Park |
| 7 | 2025 | [Direct-ink-writing of all-solid-state batteries with solvent-free, non-flammable electrolytes toward wearable electronics](https://doi.org/10.1002/inf2.70033) · InfoMat | 용매가 없고 불이 붙지 않는 고분자 전해질을 설계해 전고체 전지를 직접 인쇄했다. 인쇄 뒤 가열 처리 없이 만들 수 있고, 전해질 조성과 고분자 분자량을 조절해 인쇄성과 이온 이동을 함께 맞췄다. 착용형 전자기기에 맞춘 전지 제조를 제안했다.[^p7] | 1저자 Sumin Oh, 교신저자 Jongwoo Lim·Seungjun Chung |
| 8 | 2023 | [Single-atom catalysts for the electrochemical reduction of carbon dioxide into hydrocarbons and oxygenates](https://doi.org/10.1002/cey2.410) · Carbon Energy | 이산화탄소를 일산화탄소보다 더 환원된 탄화수소·산소 함유 화합물로 바꾸는 단일 원자 촉매 연구를 정리한 리뷰다. 기존 연구의 결과와 촉매 작동 원리를 분석하고 이 전환에서 남은 과제를 논의한다.[^p8] | 1저자 Karl Adrian Gandionco, 교신저자 Jongwoo Lim |

## 교수와 전문 분야

임종우 부교수는 포항공과대학교 화학 학사(2008), University of California, Berkeley 화학 박사(2013)를 받았다. Berkeley 화학과 박사후연구원(2014), Stanford University 재료과학공학 박사후연구원(2014–2017)을 거쳐 서울대학교 화학부 조교수(2017–2022), 부교수(2022–현재)로 재직한다.[^prof][^dept]

현재 전문 분야는 전지 재료의 변화와 이동 현상을 분석화학·물리화학으로 밝히고 그 결과를 소재 설계로 연결하는 연구다. 양극 합성과 리튬 이동, 전극 사이 반응과 열폭주, 전고체 전지의 접촉 문제, 작동 중 엑스선 측정이 대표 논문에 이어진다. 현재 연구 소개는 계산·기계학습·자동 실험을 결합한 전해질 탐색과 이산화탄소·질산 이온 전환 촉매까지 포함한다.[^overview][^p1][^p2][^p4][^p6][^sdl][^catalyst]

## 응용 분야

리튬이온 전지 양극 연구는 전기차용 전지의 에너지 저장 성능과 수명, 전지 안전에 연결된다. 전고체 전지는 전해질·음극의 접촉과 압력·제조 문제를, 직접 인쇄 전지는 착용형 전자기기에 맞는 모양과 공간 활용을 다룬다. 전기화학 촉매는 이산화탄소를 연료·화학 원료로 전환하고 질산 이온을 암모니아로 바꾸는 것을 목표로 한다. 자동 실험은 이런 전지 체계에 맞는 전해질 조합의 탐색에 쓰인다.[^cathode][^solid][^p7][^catalyst][^sdl]

## 구성원

2026년 11월 1일 Members 페이지 기준 35명이다. 박사후연구원 5명, 박사과정 20명(Ph.D. Candidate 15명·Ph.D. Course 5명), 석사과정 2명, 방문 학생 8명이다. 연구 주제와 학교 이메일은 랩 게시 표기를 따른다. LIBs(Lithium-Ion Batteries) Cathodes·LIBs Anodes는 각각 리튬이온 전지 양극·음극, ASSBs(All-Solid-State Batteries)는 전고체 전지, Computing은 계산, Electrocatalysis는 전기화학 촉매, Micro-device는 미세 장치를 뜻한다. 「대표 논문 참여」는 위 표의 번호이며, 전체 영문 이름이 일치하는 저자만 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Qing Ni | 박사후연구원 | ASSBs, Computing |  |  |
| Zhiyuan Zhang | 박사후연구원 | Electrocatalysis | zzyatsnu@snu.ac.kr |  |
| Donghoon Lee | 박사후연구원 | ASSBs | donghoonlee@snu.ac.kr |  |
| Munsoo Song | 박사후연구원 | LIBs Cathodes | loccomotiv@snu.ac.kr | 3, 4, 5 |
| Benediktus Madika | 박사후연구원 | Computing |  |  |
| Karl Adrian Gandionco | 박사과정 | Electrocatalysis |  | 8 |
| Jeongho Cho | 박사과정 | Micro-device, ASSBs | jhbest212@snu.ac.kr |  |
| Ikcheon Na | 박사과정 | LIBs Anodes, ASSBs | naich0505@snu.ac.kr | 3, 4, 6 |
| Sumin Oh | 박사과정 | ASSBs | dhtnals99@snu.ac.kr | 7 |
| Yujeong Hwang | 박사과정 | ASSBs | hwang4086@snu.ac.kr | 5 |
| Gibeom Kim | 박사과정 | ASSBs, Computing | gbkim@snu.ac.kr |  |
| Songha Seo | 박사과정 | LIBs Anodes | thdgk5089@snu.ac.kr | 5 |
| Seyeon Shin | 박사과정 | Computing | tpdus0331@snu.ac.kr |  |
| Sooseong Hwang | 박사과정 | LIBs Cathodes, Computing | gogreat@snu.ac.kr |  |
| Eunbyeol Ko | 박사과정 | LIBs Cathodes | kounbyol@snu.ac.kr |  |
| Jiseok Kim | 박사과정 | LIBs Cathodes | ddol1215@snu.ac.kr |  |
| Jongbeom Lim | 박사과정 | LIBs Cathodes | jblim971@snu.ac.kr |  |
| Eunki Hong | 박사과정 | ASSBs | kindelphinos@snu.ac.kr |  |
| Younghye Kang | 박사과정 | LIBs Cathodes | yh0925.kang@snu.ac.kr |  |
| Hyunji You | 박사과정 | Electrocatalysis |  |  |
| Junho Kim | 석사과정 | LIBs Cathodes | gabriel97@snu.ac.kr |  |
| Hyeonseok Oh | 박사과정 | ASSBs | greenhso@snu.ac.kr |  |
| Minho Kim | 박사과정 | ASSBs |  |  |
| Hyunmin Lee | 박사과정 | LIBs Anodes | lee.h.m@snu.ac.kr |  |
| Eunsoo Nam | 박사과정 | LIBs Cathodes | ds1sfw@snu.ac.kr |  |
| Junyoung Han | 박사과정 | Computing | hanjy0705@snu.ac.kr |  |
| Woojin Chong | 석사과정 | LIBs Anodes | sujinbrother@snu.ac.kr |  |
| Seohyun Kim | 방문 학생 |  | sean_kim2004@snu.ac.kr |  |
| Byungwook Nam | 방문 학생 |  | nbwook0314@snu.ac.kr |  |
| Yejin Lee | 방문 학생 |  | yejin0603@snu.ac.kr |  |
| Hoyu Kim | 방문 학생 |  | rlaghdb9008@cau.ac.kr |  |
| Seungjun Lee | 방문 학생 |  | leesj2001@snu.ac.kr |  |
| Yumin Chung | 방문 학생 |  | min10v04@ewha.ac.kr |  |
| Elias Barth | 방문 학생 |  | j.eliasbarth@snu.ac.kr |  |
| Jaehyeon Park | 방문 학생 |  |  |  |

## 졸업생과 이전 구성원

2026년 11월 1일 Alumni 페이지의 80개 게시 행이다. 이전 박사후연구원 4명, Ph.D. 구획 11명, Ph.D. Candidate 구획 2명, Masters 구획 8명, Visiting Students 구획 55행이다. 날짜와 학위 수여 연도는 게시되어 있지 않으며, Ph.D. Candidate 구획을 박사 학위 취득으로 해석하지 않는다. 방문 학생 구획의 Yewon Kim은 같은 이름이 두 번 적혀 있다. 진로는 랩이 적은 기관·과정 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jian Wang | Postdocs | Assistant Professor at City University of Hong Kong |
| Cong-Xue Liu | Postdocs | Postdoc at Beijing University |
| Jaejung Song | Postdocs | Future Quantum Convergence Institute |
| Sebastian Kunze | Postdocs | Nearfield Instruments (NFI) |
| Sugeun Jo | Ph.D. | Pohang Accelerator Laboratory |
| Hyejeong Hyun | Ph.D. | Samsung Electronics |
| Bonho Koo | Ph.D. | Postdoc at Leiden University |
| Danwon Lee | Ph.D. | Samsung SDI |
| Junho Bae | Ph.D. | Samsung SDI |
| Subin Choi | Ph.D. | Postdoc at KIST |
| Jinkyu Chung | Ph.D. | LG Chemistry |
| Juwon Kim | Ph.D. | RIST |
| Hwiho Kim | Ph.D. | LG Energy Solution |
| Sungjae Seo | Ph.D. | Samsung SDI |
| Chihyun Nam | Ph.D. | Postdoc at MIT |
| Yumin Heo | Ph.D. Candidate |  |
| Aleksandr Riabin | Ph.D. Candidate |  |
| Donghyuk Go | Masters | Samsung SDI |
| Yongjoon Kim | Masters | Samsung Electronics |
| Jeongwoo Han | Masters | LG Energy Solution |
| Junyeob Moon | Masters | Ph.D. at Harvard University |
| Hanbi Choi | Masters | Samsung SDI |
| Yuntaek Oh | Masters | Samsung SDI |
| San Hwang | Masters | Samsung SDI |
| Myeongjun Kim | Masters | Samsung SDI |
| Midam Lee | Visiting Students |  |
| Nakyung Kwon | Visiting Students |  |
| Sangyeon Won | Visiting Students |  |
| Seonghyeon Park | Visiting Students |  |
| Siyeong Park | Visiting Students |  |
| Seungjun Lee | Visiting Students |  |
| Jihye Choi | Visiting Students |  |
| Gyubin Hwang | Visiting Students |  |
| Geonho Lee | Visiting Students |  |
| Hyejin Yu | Visiting Students |  |
| Daeun Kim | Visiting Students |  |
| Johyun Park | Visiting Students |  |
| Junyeong Han | Visiting Students |  |
| Nahyeon Ji | Visiting Students |  |
| Suhyeong Lee | Visiting Students |  |
| Dongok Kim | Visiting Students |  |
| Seungcheol Na | Visiting Students |  |
| Taeyeon Cho | Visiting Students |  |
| Junghyun Park | Visiting Students |  |
| Mingi Jung | Visiting Students |  |
| Yewon Kim | Visiting Students |  |
| Omayma Jbarl | Visiting Students |  |
| Chaeeun Lee | Visiting Students |  |
| Yewon Kim | Visiting Students |  |
| Yejoon Yi | Visiting Students |  |
| Jiwon Lee | Visiting Students |  |
| Seongho Maeng | Visiting Students |  |
| Jaewon Lee | Visiting Students |  |
| Juan Baek | Visiting Students |  |
| Yongjune Choi | Visiting Students |  |
| Seoyeon Jeong | Visiting Students |  |
| Hanbin Yoon | Visiting Students |  |
| Ilmyeong Lim | Visiting Students |  |
| Seungwoo Yang | Visiting Students |  |
| Kyungwoon Kim | Visiting Students |  |
| Jiyoon Park | Visiting Students |  |
| Jisu Im | Visiting Students |  |
| Seungwon Chung | Visiting Students |  |
| Taehyun Kim | Visiting Students |  |
| Gimin Han | Visiting Students |  |
| Doyoung Kim | Visiting Students |  |
| Jiwon Hyun | Visiting Students |  |
| Mingeun Song | Visiting Students |  |
| Yeonjun Lee | Visiting Students |  |
| Jaehyun Kang | Visiting Students |  |
| Sungjun Bae | Visiting Students |  |
| Seungsoo Kim | Visiting Students |  |
| Inho Choi | Visiting Students |  |
| Jan Ostendarp | Visiting Students |  |
| Fabian Pfeiffer | Visiting Students |  |
| Sunghyun Park | Visiting Students |  |
| Hyuna Lee | Visiting Students |  |
| Daehyun Kim | Visiting Students |  |
| Jinseob Shin | Visiting Students |  |
| Jungyoon Mok | Visiting Students |  |

## 최근 논문 목록 (2021–2026)

Publications의 2021–2026년 연도 구역에 게시된 학술 논문·리뷰·논평 69편이다. 연도별로 2026년 12편, 2025년 14편, 2024년 10편, 2023년 15편, 2022년 6편, 2021년 12편이다. 연도는 누리집 구역 표기이므로 온라인 발행 연도·학술지 권호 연도와 다를 수 있다. 2026년 구역의 「Low temperature operation of Ag-C based anodeless all-solid-state pouch cells」는 날짜 없이 게재 승인으로 적힌 항목이다. 저자·제목·서지는 랩 표기이며, †·#는 누리집 표시다.[^publications]

**2026**

- Jiseok Kim†, Munsoo Song†, Sooseong Hwang, Hwiho Kim, Danwon Lee, Yujeong Hwang, Junhyuk Song, Suhyun Lee, Hyunyoung Park, Byongyong Yu, Sungjae Seo, Suguen Jo, Hyunji You, Chihyun Nam, Juwon Kim, and Jongwoo Lim\*. "Resolving the Structural Origin of Lattice Oxygen Release across Scales in Practical Lithium-Manganese-Rich Electrodes". *Advanced Energy Materials, 2026*.
- Myeongjun Kim†, Chihyun Nam†, Hyunmin Lee†, Seyeon Shin, Songha Seo, Woojin Chung, Yejin Lee, Munsoo Song, and Jongwoo Lim\*. "Physically Grounded Descriptors for Machine-Learning-Guided Diluent Design in Lithium Metal Batteries". *Journal of the American Chemical Society, 2026*.
- Hwiho Kim†, Dalyu Kim†, Chihyun Nam, Jun Tae Kim, Yujeong Hwang, Sooseong Hwang, Sugeun Jo, Sungjae Seo, Hyunji Yoo, Hun-Gi Jung\*, Mingyuan Ge\*, Yun Seog Lee\*, and Jongwoo Lim\*. "Stress-coupled lithium transport in all-solid-state batteries". *Joule, 2026, 10, 9, 102680*.
- Woojin Lee,† Jason Kim,† Hyunji Lee, Yujeong Hwang, Jiseong Park, Seunghoon Lee, Jongwoo Lim, Seung Youn Hong\*. "Harnessing Through-Space Orbital Interactions for Multicentred Organosulfur Catalysis". *Nature Catalysis, 2026, 9, 8*.
- Sungjae Seo, Sugeun Jo, Hwiho Kim, Juwon Kim, Munsoo Song, Chihyun Nam, Sung Pil Woo, and Jongwoo Lim\*. "Non-Monotonic Phase Evolution and Size-Dependent Lithium Accessibility in Degraded High-Nickel Cathodes". *ACS Energy Letters, 2026, 11, 8*.
- Hwiho Kim†, Sebastian Kunze†, Kyungho Yoon†, Sooseong Hwang, Jiseok Kim, Yujeong Hwang, Dongil Kang, Ikcheon Na, Chih-Wen Pao, Wei-Hsiang Huang, Yong-Gun Lee, Jun Hwan Ku\*, and Jongwoo Lim\*. "Low temperature operation of Ag-C based anodeless all-solid-state pouch cells". *Nature Communications, 2026, accepted*.
- Huiju Kim†, Hongjun Chang†, Sebastian Kunze†, Yoon Jeong Yoo, Yeji Lim, Jongwoo Lim\*, Janghyuk Moon\* and Won-Hee Ryu\*. "Rational Fe–4d Dual-Atom Pairing for Stabilizing Redox Mediators in Lithium–Oxygen Batteries". *Chemical Engineering Journal, 2026, 546, 179606*.
- Inseo Choi, Jaehee Lee, Kyohyun Hwang, Sebastian Kunze, Jae Wan Park, Seung Jun Hwang, Jongwoo Lim, Seunghoon Lee\*, Woon Ju Song\*. "Protein-Enforced Ligand Environments Reshape Classical Coordination Preferences in Copper Polypyridyl Complexes". *Journal of the American Chemical Society, 2026, 148, 28, 30460-30417*.
- Munsoo Song†, Danwon Lee†, Bonho Koo, Hyunjun Choi, Daesoo Kim, Juwon Kim, Chihyun Nam, Sungjae Seo, Jiseok Kim, Donghoon Lee, Yojin Kim, and Jongwoo Lim\*. "Enhancing the Longevity of Lithium-Manganese-Rich Layered Oxides by Promoting Oxygen Redox Reversibility". *Nature Communications, 2026, 17, 1*.
- Karl Adrian Gandionco, Juwon Kim, Alexander Ryabin, Hyunji You, Sebastian Kunze, Subin Choi, Jeongho Cho, Gibeom Kim, Jiseok Kim, Hwiho Kim, and Jongwoo Lim\*. "Stable and Active p-block Metal-doped Cu2O Catalysts for the Electrochemical Reduction of CO2 into CO". *ACS Applied Materials & Interfaces, 2026, 18, 16, 23062-23071*.
- Yujeong Hwang, Hwiho Kim, Sungjae seo, Mingyuan Ge, Yongjun Jang, and Jongwoo Lim\*. "Investigation of Moisture-Induced Degradation Mechanisms and a Reviving Strategy for Sulfide-Based Solid Electrolytes in All-Solid-State Composite Cathode". *Advanced Energy Materials, 2026, 16, 9*.
- Karl Adrian Gandionco, Zhiyuan Zhang, and Jongwoo Lim\*. "Sulfur enhances electrochemical CO2 reduction over porphyrin catalysts". *Nature Synthesis, 2026, 5, 2, 156-157*.

**2025**

- Yue Wen†, Jeongho Cho†, Linfeng Yu, Yi-Ming Zhao, Jingxuan Wang, Lei Shen, Guangzhao Qin, Seok Min Yoon\*, Jongwoo Lim\*, and Sunmi Shin\*. "Thermal conductivity of individual single-crystalline F16CuPc nano ribbons". *Nanoscale, 2025, 17, 36, 20982-20988*.
- San Hwang†, Sungjae Seo†, Munsoo Song, Chihyun Nam, Juwon Kim, Yujeong Hwang, Songha Seo, Jaejung Song, Sugeun Jo, Hongjin Lim, Sung Pil Woo, SoHee Kim, and Jongwoo Lim\*. "Electrochemical Abuse-Driven Thermal Runaway in Lithium-ion Batteries: Evolution from Beginning-of-Life to End-of-Life". *Advanced Functional Materials, 2025, 36, 18*.
- Zhiyuan Zhang and Jongwoo Lim\*. "Origin of copper catalyst reconstruction". *Chem Catalysis, 2025, 5, 8, 101494*.
- Prof. Dr. Zhiqi Zhang, Prof. Dr. Jiapeng Liu, Prof. Dr. Shangqian Zhu, Dr. Yuhao Wang, Prof. Dr. Jian Wang, Minhong Xu, Dr. Jie Zhao, Prof. Dr. Zheng Wang, Prof. Dr. Dewang Zeng, Prof. Dr. Jianrong Zeng, Dr. Yufei Song, Dr. Chih-Wen Pao, Prof. Dr. Zhiwei Hu, Prof. Dr. Jongwoo Lim, Prof. Dr. Rui Xiao, Prof. Dr. Minhua Shao, Prof. Dr. Francesco Ciucci\*. "Dizygotic Atomic Platinum and Palladium on Carbon for High-Performance Ethanol and Methanol Electro-Oxidation". *Angewandte Chemie International Edition, 2025, 137, 37*.
- Danwon Lee†, Chihyun Nam†, Juwon Kim, Sooseong Hwang, Bonho Koo, Hyejeong Hyun, Jinkyu Chung, Sungjae Seo, Munsoo Song, Jaejung Song, Myeongjun Kim, Daan Hein Alsem, Norman J. Salmon, Suyong Lee, Yeonchoo Cho, Namdong Kim, David A. Shapiro, and Jongwoo Lim\*. "Strain-Associated Nanoscale Fluctuating Lithium Transport within Single-Crystalline NMC Cathode Particles". *Nature Communications, 2025, 16, 1*.
- Intizar Abbas, Chan-Woo Park, Hoon-Hwe Cho, Jaekook Kim, Huyen Tran Tran, Sung-Bong Yu, Jongwoo Lim, Tran Thi Ngoc Tran, Thuy Linh Pham, Eui-Chol Shin, Oh Jeong Lee, An-Giang Nguyen, Daeho Jeong, Bok Hyun Ka, Namsoo Shin, Miran Gaberšcˇek, Su-Mi Hur, Chan-Jin Park, and Jong-Sook Lee\*. "GITT Limitations and EIS Insights into Kinetics of NMC622". *Batteries, 2025, 11, 6, 234*.
- Youngjin Song, Sungjin Cho, Suhwan Kim, Youyeong Shin, Ikcheon Na, Jongwoo Lim, Yong Min Lee\*, Soojin Park\*. "Comprehensive Si Anode Design for Sulfide-Based All-Solid-State Batteries: Insights into Si-Electrolyte Synergy for Mitigating Contact Loss". *Advanced Functional Materials, 2025, 35, 43*.
- Sumin Oh, Junho Bae, Yumin Heo, Hyeji Park, Seyun Chang, Jongwoo Lim\*, Seungjun Chung\*. "Direct-Ink-Writing of All-Solid-State Batteries with Solvent-Free, Non-Flammable Electrolytes toward Wearable Electronics". *InfoMat, 2025, 7, 8*.
- Youngwoo Choi, Gumin Kang, Seonghyun Kim, Yoonhan Cho, Jaewhan Oh, Dongho Kim, Jacob Choe, Jong Min Yuk, Pyuck-Pa Choi, Yongsoo Yang, Sung-Yoon Chung, Chi Won Ahn, Jongwoo Lim, Seungbum Hong\*. "Multiscale Materials Imaging and Spectroscopy for Battery Materials". *EcoMat, 2025, 7, 5*.
- Yuntaek Oh†, Hwiho Kim†, Jongbeom Lim, Yujeong Hwang, Sugeun Jo, Jihyun Seog, and Jongwoo Lim\*. "Enhanced Electrical Connectivity in High Energy Density Single-Crystal NCA Electrodes via Polycrystalline Blending Design". *ACS Applied Materials & Interfaces, 2025, 17, 19, 28094-28102*.
- Sebastian Kunze, Chihyun Nam, Hwiho Kim, Jinkyu Chung, Eunki Hong, Jaejung Song, Hanbi Choi, and Jongwoo Lim\*. "X-Ray Imaging Methods for Multiscale Characterization of Batteries". *Bulletin of the Korean Chemical Society, 2025, 46, 4, 360-380*.
- Kun-Hee Ko†, Hyeokjun Park†, Jaesang Yoon†, Seok Hyun Song, Eugene Choi, Sungjae Seo, Jaesub Kwon, Sunyoung Lee, Jaehoon Heo, Sangwook Han, Jooha Park, Wonju Kim, Yong-Tae Kim, Jongwoo Lim, Yun Seog Lee, Hyungsub Kim, and Kisuk Kang\*. "Multiscale Defect Regulation of Cobalt-Free Layered Oxides for High-Energy and Long-Lasting Cathodes". *ACS Energy Letters, 2025, 10, 4, 1605-1614*.
- Chihyun Nam†, Bonho Koo†, Juwon Kim†, Jinkyu Chung, Jaejung Song, Danwon Lee, Sungjae Seo, Munsoo Song, Seyeon Shin, Namdong Kim, Markus Weigand, Jian Wang, and Jongwoo Lim\*. "Dynamic Lithium Transport Pathway via Crack Formation in Phase-Separating Battery Particles". *ACS Nano, 2025, 19, 10, 9936-9945*.
- Junho Bae, Myeongjun Kim, Sumin Oh, Munsoo Song, Cong-Xue Liu, Seungjun Chung\*, and Jongwoo Lim\*. "Enhanced Corrosion Stability and Cycling Performance of Dual-Salts Polymer Electrolytes for Li-metal Polymer Batteries". *Energy Storage Materials, 2025, 76, 104089*.

**2024**

- Sugeun Jo, Hwiho Kim, Sangwoo Kim, Chihyun Nam, Jongwoo Lim\*, Jun Lim\*. "Nanoscale Projection Hard X-ray Microscope for Operando Statistical Analysis of Chemical Heterogeneity in Lithium-Ion Battery Cathodes". *Small Methods, 2024, 9, 3*.
- Jinkyu Chung†, Chihyun Nam†, Jae Young Kim†, Tae Hyung Lee, Juwon Kim, Danwon Lee, Bonho Koo, Sugeun Jo, Jeongho Cho, Sebastian Kunze, Yong Seok Choi, Jaejung Song, Hanbi Choi, Jiseok Kim, Sung Hyuk Park, Hyeon Ji Lee, Byung Hee Hong, Namdong Kim, David A. Shapiroe, Ho Won Jang\*, and Jongwoo Lim\*. "Elucidating Heterogeneous Li insertion using Single Crystalline and Freestanding Layered Oxide Thin Film". *Nano Letters, 2024, 24, 46, 14766–14773*.
- Subin Choi, Se-Jun Kim, Sunghoon Han, Jian Wang, Juwon Kim, Bonho Koo, Alexander A. Ryabin, Sebastian Kunze, Hyejeong Hyun, Jeongwoo Han, Shu-Chih Haw, Keun Hwa Chae, Changhyuck Choi, Hyungjun Kim, and Jongwoo Lim\*. "Enhancing Oxygen Evolution Reaction via Surface reconstruction-Induced Lattice Oxygen Mechanism". *ACS Catalysis, 2024, 14, 20, 15096-15107*.
- Juwon Kim†, Si Young Lee†, Se-Jun Kim†, Bonho Koo, Jinkyu Chung, Danwon Lee, Subin Choi, Ji Min Kim, Sungjae Seo, Karl Adrian Gandionco, Sugeun Jo, Namdong Kim, Hyun-Joon Shin, Keun Hwa Chae, Da Hye Won, Matthew A. Marcus, David A. Shapiro, Shu-Chih Haw, Daan Hein Alsem, Norman J. Salmon, Byoung Koun Min, Hyungjun Kim\*, Yun Jeong Hwang\*, and Jongwoo Lim\*. "Spatiotemporal active phase evolution for CO2 electrocatalysis". *Joule, 2024, 8, 12, 3373-3385*.
- Alexander A. Ryabin†, Subin Choi†, Yumin Heo†, Sebastian Kunze, Dmitry V. Pelegov\*, and Jongwoo Lim\*. "Potential-driven restructuring of lithium cobalt oxide yields an enhanced active phase for the oxygen evolution reaction". *Journal of Material Chemistry A, 2024, 12, 29, 18071-18081*.
- Ruije Yang, Liang Mei, Zhaoyang Lin, Yingying Fan, Jongwoo Lim, Jinghua Guo, Yijin Liu, Hyeon Suk Shin, Damien Voiry, Qingye Lu\*, Ju Li\*, and Zhiyuan Zeng\*. "Intercalation in 2D materials and in situ studies". *Nature Reviews Chemistry, 2024, 8, 6, 410-432*.
- Sugeun Jo#, Sungjae Seo#, Song Kyu Kang, Ikcheon Na, Sebastian Kunze, Munsoo Song, Hwang San, Sung Pil Woo, SoHee Kim, Won Bae Kim, and Jongwoo Lim\*. "Thermal runaway mechanism in Ni-rich cathode full-cells of lithium-ion batteries: The role of multidirectional crosstalk". *Advanced Materials, 2024, 36, 31*.
- Yunseok Shin, Seong Chan Cho, Gilsoo Park, Jae Hun Seol, Dongwook Lim, Subin Choi, Changbum Jo, Sung Hyeon Baeck, Jongwoo Lim, Sang Uck Lee\*, Sungjin Park\*. "Atomic-level insights into bioinspired Fe/Ni bimetallic active sites on carbon nitrides for electrocatalytic O2 evolution". *Chemical Engineering Journal, 2024, 485, 149799*.
- Munsoo Song, Danwon Lee, Juwon Kim, Subin Choi, Ikcheon Na, Sungjae Seo, Sugeun Jo, Chiho Jo, Jongwoo Lim\*. "Gas Evolution Kinetics in Overlithiated Positive Electrodes and its Impact on Electrode Design". *Advanced Science, 2024, 11, 22*.
- Ho-Young Jang#, Donggun Eum#, Jiung Cho, Jun Lim, Yeji Lee, Jun-Hyuk Song, Hyeokjun Park, Byunghoon Kim, Do-Hoon Kim, Sung-Pyo Cho, Sugeun Jo, Jae Hoon Heo, Sunyoung Lee, Jongwoo Lim, Kisuk Kang\*. "Structurally Robust Lithium-rich Layered Oxides for High-energy and Long-lasting Cathodes". *Nature Communications, 2024, 15, 1*.

**2023**

- Hongbo Zhao, Haitao Dean Deng, Alexander E. Cohen, Jongwoo Lim, Yiyang Li, Dimitrios Fraggedakis, Benben Jiang, Brian D. Storey, William C. Chueh, Richard D. Braatz, and Martain Z. Bazant\*. "Learning heterogeneous reaction kinetics from X-ray videos pixel by pixel". *Nature, 2023, 621, 289-294*.
- Hyejeong Hyun#, Hyojung Yoon#, Subin Choi, Juri Kim, So Young Kim, Tom Regier, Zachary Arthur, SeokKoo Kim, Jongwoo Lim\*. "Paradoxical role of structural degradation of nickel-rich layered oxides in capacity retention upon storage of lithium-ion batteries". *Energy & Environmental Science, 2023, 16, 3968-3983*.
- Hyejeong Hyun, Daseul Ham, Su Yong Lee, Jongwoo Lim\*. "Annealing-Induced Dynamic Strain Evolution in Cycled High-Ni Layered Oxides Revealing Latent Lattice Imperfections". *Advanced Energy Materials, 2023, 13, 2301647*.
- Jian Wang#\*, Hyejoeng Hyun#, Sungjae Seo#, Kyeongjae Jeong, Jeongwoo Han, Sugeun Jo, Hwiho Kim, Bonho Koo, Donggun Eum, Juwon Kim, Jinkyu Chung, Hoon-Hwe Cho,Heung Nam Han, Tae Joo Shin, Meng Ni, Kisuk Kang\*, Jongwoo Lim\*. "A Kinetic Indicator of Ultrafast Nickel-rich Layered Oxide Cathodes". *ACS Energy Letters, 2023, 8, 7, 2986-2995*.
- Juwon Kim, Danwon Lee, Chihyun Nam, Jinkyu Chung, Bonho Koo, Namdong Kim\*, Jongwoo Lim\*. "Energy material analysis via in-situ/operando scanning transmission x-ray microscopy". *Journal of Electron Spectroscopy and Related Phenomena, 2023, 266, 147337*.
- Bonho Koo#, Jinkyu Chung#, Juwon Kim#, Dimitrios Fraggedakis, Sungjae Seo, Chihyun Nam, Danwon Lee, Jeongwoo Han, Sugeun Jo, Hongbo Zhao, Neel Nadkarni, Jian Wang, Namdong Kim, Markus Weigand, Martin Z. Bazant\*, Jongwoo Lim\*. "Dynamic surface phases controlling asymmetry of high-rate lithiation and delithiation in phase-separating electrodes". *Energy & Environmental Science, 2023, 16, 3302-3313*.
- Karl A. Gandionco, Juwon Kim, Lieven Bekaert, Annick Hubin, Jongwoo Lim\*. "Single-Atom Catalysts for the Electrochemical Reduction of Carbon Dioxide into Hydrocarbons and Oxygenates". *Carbon Energy, 2023, e410*.
- Hyejeong Hyun, Jongwoo Lim\*. "Elucidating degradation mechanisms of Co-free high-Ni layered oxide cathodes for Li-ion batteries via advanced X-ray-based characterization methods". *Ceramist, 2023, 26, 138-157*.
- Donggun Eum, Ho-Young Jang, Byunghoon Kim, Jinkyu Chung, Dokyung Kim, Sung-Pyo Cho, Seok Hyun Song, Seongmin Kang, Seungju Yu, Sung-O Park, Jun-Hyuk Song, Hyungsub Kim , Orapa Tamwattana, Do-Hoon Kim, Jongwoo Lim, Kisuk Kang\*. "Effects of cation superstructure ordering on oxygen redox stability in O2-type lithium-rich layered oxides". *Energy & Environmental Science, 2023, 16, 673-686*.
- Munjeong Jang#, Subin Choi#, Yoondo Kim, Junyoung Cha, Ah-Reum Kim, Hyangsoo Jeong, Yongmin Kim, Sun Hee Choi, Suk Woo Nam, Jongwoo Lim\*, Chang Won Yoon\*, Hyuntae Sohn\*. "Effect of CeO2 redox properties on the catalytic activity of Pt-CeOx over irreducible SiO2 support for methylcyclohexane (MCH) dehydrogenation". *Applied Surface Science, 2023, 627, 157134*.
- Ikcheon Na, Hwiho Kim, Sebastian Kunze, Chihyun Nam, Sugeun Jo, Hanbi Choi, Sumin Oh, Eugene Choi, Yong Bae Song, Yoon Seok Jung, Yun Seong Lee, Jongwoo Lim\*. "Monolithic 100% silicon anode for all-solid-state batteries achieving high areal capacity at room temperature". *ACS Energy Letters, 2023, 8, 4, 1936-1943*.
- Junho Bae, Sumin Oh, Byeongmoon Lee, Cheolhoon Lee, Jinkyu Chung, Juwon Kim, Sugeun Jo, Jongwoo Lim\*, Seungjun Chung\*. "High-performance, printable quasi-solid-state electrolytes toward all 3D direct ink writing of shape-versatile Li-ion batteries". *Energy Storage Materials, 2023, 57, 277-288*.
- Munsoo Song#, Danwon Lee#, Juwon Kim, Yumin Heo, Chihyun Nam, Donghyuk Ko, Jongwoo Lim\*. "Chemical decomposition pathway of residual lithium carbonate of Li-ion battery cathodes". *Journal of Power Sources, 2023, 560, 232699*.
- Sugeun Jo, Jeongwoo Han, Sungjae Seo, Oh-Sung Kwon, Subin Choi, Jin Zhang, Hyefeong Hyun, Juhyun Oh, Juwon Kim, Jinkyu Chung, Hwiho Kim, Jian Wang, Junho Bae, Junyeob Moon, Yoon-Cheol Park, Moon-Hi Hong, Miyoung Kim, Yijin Liu, Il Sohn, Keeyoung Jung\*, Jongwoo Lim\*. "Solid-state reaction heterogeneity during calcination of lithium-ion battery cathode". *Advanced Materials, 2023, 35, 2207076*.
- Jong Seok Kim, Seungwon Jung, Hiram Kwak, Yoonjae Han, Suhwan Kim, Jongwoo Lim, Yong Min Lee\*, Yoon Seok Jung\*. "Synergistic halide-sulfide hybrid solid electrolytes for Ni-rich cathodes design guided by digital twin for all-solid-State Li batteries". *Energy Storage Materials, 2023, 55, 193-204*.

**2022**

- Hyunjoon Lee, Da Gil Ryu, Giho Lee, Min-Kyu Song, Hyungjin Moon, Jaehyeong Lee, Jongchan Ryu, Ji-Hoon Kang, Junmin Suh, Sangbum Kim, Jongwoo Lim, Dongsuk Jeon, Seyoung Kim\*, Jeehwan Kim\*, Yun Seog Lee\*. "Vertical Metal-Oxide Electrochemical Memory for High-Density Synaptic Array Based High-Performance Neuromorphic Computing". *Advanced Electronic Materials, 2022*.
- Zheng Wang, Yuhao Wang, Jian Wang, Yufei Song, Matthew J. Robson, Arim Seong, Meiting Yang, Zhiqi Zhang, Alessio Belotti, Jiapeng Liu, Guntae Kim, Jongwoo Lim, Zongping Shao, Francesco Ciucci\*. "Rational design of perovskite ferrites as high-performance proton-conducting fuel cell cathodes". *Nature Catalysis, 2022, 5, 777-787*.
- Kyungho Yoon#, Hwiho Kim#, Sangwook Han, Ting-Shan Chan, Kun-Hee Ko, Sugeun Jo, Jooha Park, Sewon Kim, Sunyoung Lee, Joohyeon Noh, Wonju Kim, Jongwoo Lim\*, and Kisuk Kang \*. "Detrimental effect of high-temperature storage on sulfide-based all-solid-state batteries". *Applied Physics Reviews, 2022, 9, 031403*.
- Junyeob Moon#, Dong Ok Kim#, Lieven Bekaert, Munsoo Song, Jinkyu Chung, Danwon Lee, Annick Hubin\*, Jongwoo Lim\*. "Non-fluorinated non-solvating cosolvent enabling superior performance of lithium metal negative electrode battery". *Nature Communications, 2022, 13, 4538*.
- Youngjoon Kim, Takashi Kodama, Yoonjin Kim, Brian S. Y. Kim, Changhyun Ko, Jongwoo Lim\*, Woosung Park\*. "Suppressed phonon conduction by geometrically induced evolution of transport characteristics from Brownian motion into Lévy flight". *NPG Asia Materials, 2022, 14, 33*.
- Jeongeun Song, Subin Choi, Jongwoo Lim\*, Kyoung Taek Kim\*. "Templated synthesis of microparticles with carbonaceous skeletal structures using polymer cubosomes as templates". *RSC Advances, 2022, 12, 14, 8429-8434*.

**2021**

- Jeongwoo Han, Sugeun Jo, Ikcheon Na, Seung-min Oh, Young-min Jeon, Jeong-gyu Park, Bonho Koo, Hyejeong Hyun, Sungjae Seo, Danwon Lee, Hwiho Kim, Juwon Kim, Jong-chan Lim, Jongwoo Lim\*. "Homogenizing silicon domains in SiOx anode during cycling and enhancing battery performance via magnesium doping". *ACS Applied Materials and Interfaces, 2021, 13, 52202*.
- Hyejeong Hyun, Kyeongjae Jeong, Hyukhun Hong, Sungjae Seo, Bonho Koo, Danwon Lee, Subin Choi, Sugeun Jo, Keeyoung Jung, Hoon-Hwe Cho, Heung Nam Han ,Tae Joo Shin\*, Jongwoo Lim\*. "Suppressing High-Current-Induced Phase Separation in Ni-Rich Layered Oxides by Electrochemically Manipulating Dynamic Lithium Distribution". *Advanced Materials, 2021, 2105337*.
- Zhiqi Zhang, Jiapeng Liu, Jian Wang, Qi Wang, Yuhao Wang, Kai Wang, Zheng Wang, Meng Gu, Zhenghua Tang, Jongwoo Lim, Tianshou Zhao & Francesco Ciucci\*. "Single-atom catalyst for high-performance methanol oxidation". *Nature Communications, 2021, 12, 5235*.
- Zheng-Long Xu, Jooha Park, Jian Wang, Hyunseok Moon, Gabin Yoon, Jongwoo Lim, Yoon-Joo Ko, Sung-Pyo Cho, Sang-Young Lee, Kisuk Kang\*. "A new high-voltage calcium intercalation host for ultra-stable and high-power calcium rechargeable batteries". *Nature Communications, 2021, 12, 3369*.
- Ruijie Gao#, Jian Wang#, Zhen-Feng Huang, Rongrong Zhang, Wei Wang, Lun Pan\*, Junfeng Zhang, Weikang Zhu, Xiangwen Zhang, Chengxiang Shi, Jongwoo Lim\*, Ji-Jun Zou\*. "Pt/Fe2O3 with Pt–Fe pair sites as a catalyst for oxygen reduction with ultralow Pt loading". *Nature Energy, 2021, 6, 614-623*.
- Shuqi Hua, Jian Wang, Jun Zhang, Jongwoo Lim, Yang Gao\*, Shiguo Zhan\*g. "Engineering the electronic structure of perovskite oxide surface with ionic liquid for enhanced oxygen reduction reaction". *Applied Catalysis B: Environmental, 2021, 282, 119593*.
- Solomon Ansah, Hyejeong Hyun,Namsoo Shin, Jong-Sook Lee, Jongwoo Lim\*, Hoon-Hwe Cho\*. "A modeling approach to study the performance of Ni-rich layered oxide cathode for lithium-ion battery". *Computational Materials Science, 2021, 196, 110559*.
- Jongseong Park, Tae HyungLee, Changyeon Kim, Sol A Lee, Min-Ju Choi, Hwiho Kim, Jin Wook Yang, Jongwoo Lim\*, Ho Won Jang\*. "Hydrothermally obtained type-II heterojunction nanostructures of In2S3 / TiO2 for remarkably enhanced photoelectrochemical water splitting". *Applied Catalysis B: Environmental, 2021, 295, 120276*.
- Jian Wang\*, Se-Jun Kim, Jiapeng Liu, Yang Gao, Subin Choi, Jeongwoo Han, Hyeyoung Shin, Sugeun Jo, Juwon Kim, Francesco Ciucci, Hwiho Kim, Qingtian Li, Wanli Yang, Xia Long, Shihe Yang\*, Sung-Pyo Cho, Keun Hwa Chae, Min Gyu Kim, Hyungjun Kim\*, Jongwoo Lim\*. "Redirecting Dynamic Surface Restructuring of a Layered Transition Metal Oxide Catalyst for Superior Water Oxidation". *Nature Catalysis, 2021, 4, 212-222*.
- Jun Yu, Jian Wang, Xia Long, Lei Chen, Qi Cao, Jian Wang, Chen Qiu, Jongwoo Lim, Shihe Yang\*. "Formation of FeOOH Nanosheets Induces Substitutional Doping of CeO2−x with High‐Valence Ni for Efficient Water Oxidation". *Advanced Energy Materials, 2021, 11, 2002731*.
- Mouhong Lin#, Jian Wang#, Gyeong-Hwan Kim#, Jianan Liu, Limin Pan, Yeonhee Lee, Jeong-Wook Oh, Yoonjae Jung, Sungjae Seo, Youngju Son, Jongwoo Lim, Jungwon Park, Taeghwan Hyeon, Jwa-Min Nam\*. "One-Pot Heterointerfacial Metamorphosis for Synthesis and Control of Widely Varying Heterostructured Nanoparticles". *Journal of American Chemical Society, 2021, 143, 9, 3383*.
- Antonino Curcio, Jian Wang, Zheng Wang, Zhiqi Zhang, Alessio Belotti, Simona Pepe, Mohammed B. Effat, Zongping Shao, Jongwoo Lim, Francesco Ciucci\*. "Unlocking the Potential of Mechanochemical Coupling: Boosting the Oxygen Evolution Reaction by Mating Proton Acceptors with Electron Donors". *Advanced Functional Materials, 2021, 31, 4, 2008077*.

## 수상과 선정

2021년 10월 22일–2026년 10월 22일 범위 안에 드는 월별 News의 41개 게시 항목이다. 수상·장학금·연구비·회원 및 직무 선정을 포함하며, 날짜는 게시 연월이다. 두 사람이 한 항목에 적힌 경우도 한 건으로 센다.[^news]

- 2026-09 · Ikcheon이 ShanghaiTech-Korea Symposium on Electrocatalysis and Energy Materials에서 포스터상을 받았다.
- 2026-08 · Chihyun이 서울대학교 자연과학대학의 최우수 박사학위논문상을 받았다.
- 2026-07 · 임종우 교수가 Materials Chemistry Frontiers 부편집장으로 임명되었다.
- 2026-06 · Woojin이 서울대·삼성SDI 배터리 트랙 장학금을 받았다.
- 2026-05 · Qing이 SNU Frontier Fellowship에 선정되었다.
- 2026-04 · Donghoon·Chihyun이 세종과학펠로우십에 선정되었다.
- 2025-12 · Myeongjun이 한국전기화학회 추계 학술대회에서 대상을 받았다.
- 2025-12 · Munsoo·Chihyun이 International Conference on Advanced Materials and Devices에서 최우수 포스터상을 받았다.
- 2025-11 · Chihyun이 방사광이용자협회의 대학원생 우수논문상을 받았다.
- 2025-04 · Seyeon이 미국재료학회 최우수 포스터상 후보로 선정되었다.
- 2025-04 · Qing이 Young Investigator Grant에 선정되었다.
- 2025-02 · Jinkyu가 서울대학교 자연과학대학 최우수박사학위논문상을 받았다.
- 2025-02 · Myeongjun·Seyeon·Chihyun·Jaejung이 서울대·삼성SDI 배터리 트랙 배터리 경진대회 대상을 받았다.
- 2025-01 · Chihyun이 삼성휴먼테크논문대상을 받았다.
- 2025-01 · Hyunseok이 우산육영회 장학금을 받았다.
- 2024-11 · Seohyeon이 서울대학교 화학부 학부생 우수연구상을 받았다.
- 2024-11 · Karl이 한국화학공학회 최우수 구두발표상을 받았다.
- 2024-11 · Sugeun이 한국방사광이용자협회 신진학술상을 받았다.
- 2024-11 · Namdong Kim이 포항가속기연구소 Best Manager Award를 받았다.
- 2024-11 · Eunbyeol이 글로벌 여성 리더십 장학금을 받았다.
- 2024-09 · Sugeun이 대한화학회 우수박사학위논문상을 받았다.
- 2024-08 · Sungjae가 Nano Korea Young Scientist Award를 받았다.
- 2024-08 · Chihyun이 ECS prime grant에 선정되었다.
- 2024-07 · Munsoo가 LG E&S 산학 학술행사에서 최우수 포스터상을 받았다.
- 2024-07 · 임종우 교수가 도쿄대학교 화학과 Zasshikai Lectureship을 받았다.
- 2024-06 · Chihyun이 한국연구재단 박사과정생연구장려금에 선정되었다.
- 2024-06 · Chihyun이 International Meeting on Lithium Batteries에서 최우수 포스터상을 받았다.
- 2024-06 · Munsoo가 BK21 우수 대학원생으로 선정되었다.
- 2024-05 · Bonho가 한국연구재단 국외 박사후연구 장학금에 선정되었다.
- 2024-04 · 임종우 교수가 한국전기화학회 춘계 학술대회에서 박수문학술상을 받았다.
- 2024-04 · Sungjae·Yumin이 한국전기화학회 춘계 학술대회에서 각각 대상·우수상을 받았다.
- 2024-04 · Hyunji가 한국연구재단 석사과정생연구장려금에 선정되었다.
- 2023-12 · 임종우 교수가 한국차세대과학기술한림원 회원으로 선출되었다.
- 2023-11 · Hyejeong이 포항 방사광 연구소의 신진학술상을 받았다.
- 2023-11 · 임종우 교수가 대한민국 대통령·한국연구재단 젊은과학자상을 받았다.
- 2023-10 · 임종우 교수가 대한화학회 KCS-Wiley 신진화학자상을 받았다.
- 2023-08 · Jinkyu가 Samsung Global Technology Symposium에서 포스터상을 받았다.
- 2023-07 · Danwon이 LG에너지솔루션 산학 학술행사에서 최우수 포스터상을 받았다.
- 2023-07 · Juwon이 대한화학회 하계 학술대회에서 우수발표상을 받았다.
- 2023-04 · Bonho·Sugeun이 한국전기화학회 춘계 학술대회에서 각각 우수발표상을 받았다.
- 2023-03 · 임종우 교수가 서울대학교 자연과학대학 연구상을 받았다.

## 소식

같은 기간 범위의 월별 News 가운데 논문 게재·게재 승인·출판 절차에 관한 36건이다. 아래 날짜는 게시 연월이며 논문의 발행일과 구분된다.[^news]

- 2026-09 · Myeongjun·Chihyun·Hyunmin의 리튬 금속 전지 희석제 설계 논문이 Journal of the American Chemical Society 게재 승인을 받았다.
- 2026-08 · Hwiho의 전고체 전지 내부 응력과 리튬 이동 연구가 Joule 게재 승인을 받았다.
- 2026-07 · Sungjae의 열화된 고니켈 양극 내부 변화와 리튬 접근성 연구가 ACS Energy Letters 게재 승인을 받았다.
- 2026-07 · Hwiho·Sebastian의 은·탄소 기반 무음극 전고체 파우치 전지 저온 작동 연구가 Nature Communications 게재 승인을 받았다.
- 2026-07 · Sebastian이 공동 제일저자로 참여한 리튬·산소 전지 산화환원 매개체 연구가 Chemical Engineering Journal 게재 승인을 받았다.
- 2026-05 · Munsoo·Danwon의 산소 산화환원 가역성을 통한 리튬·망간 풍부 양극 수명 연구가 Nature Communications 게재 승인을 받았다.
- 2026-04 · Karl의 구리 산화물 촉매를 이용한 이산화탄소의 일산화탄소 전환 연구가 ACS Applied Materials & Interfaces 게재 승인을 받았다.
- 2026-03 · Yujeong의 황화물 고체 전해질 수분 열화와 회복 전략 연구가 Advanced Energy Materials 게재 승인을 받았다.
- 2026-01 · Karl의 황과 포르피린 촉매를 이용한 이산화탄소 전환 논문이 Nature Synthesis에서 출판 절차에 들어갔다.
- 2025-10 · Jeongho가 참여한 단결정 유기 물질의 열전도도 논문이 Nanoscale에서 출판 절차에 들어갔다.
- 2025-10 · San·Sungjae의 전기화학적 열화에 따른 전지 열폭주 연구가 Advanced Functional Materials 게재 승인을 받았다.
- 2025-08 · Zhiyuan의 구리 촉매 재구성 논문이 Chem Catalysis에서 출판 절차에 들어갔다.
- 2025-08 · Danwon·Chihyun의 단결정 양극 내부 변형과 리튬 이동 연구가 Nature Communications 게재 승인을 받았다.
- 2025-05 · Sumin의 용매 없는 비가연성 전해질을 이용한 전고체 전지 직접 인쇄 연구가 InfoMat 게재 승인을 받았다.
- 2025-03 · Yuntaek·Hwiho의 양극 혼합 설계를 통한 전기적 연결성 개선 연구가 ACS Applied Materials & Interfaces 게재 승인을 받았다.
- 2025-03 · Sebastian의 전지 다중 규모 분석용 엑스선 영상 방법 논문이 Bulletin of the Korean Chemical Society 게재 승인을 받았다.
- 2025-02 · Chihyun·Bonho·Juwon의 입자 균열과 리튬 이동 경로 연구가 ACS Nano 게재 승인을 받았다.
- 2025-02 · Junho의 이중 염 고분자 전해질 부식 안정성·충방전 연구가 Energy Storage Materials 게재 승인을 받았다.
- 2024-12 · Sugeun의 전지 양극 불균일성 분석용 엑스선 현미경 논문이 Small Methods에서 출판 절차에 들어갔다.
- 2024-09 · Jinkyu·Chihyun의 독립형 단결정 산화물 막을 이용한 리튬 삽입 불균일성 연구가 Nano Letters 게재 승인을 받았다.
- 2024-09 · Subin의 촉매 표면 재구성과 산소 발생 반응 연구가 ACS Catalysis 게재 승인을 받았다.
- 2024-08 · Juwon의 이산화탄소 전환 중 촉매 활성 상태 변화 연구가 Joule 게재 승인을 받았다.
- 2024-07 · Alexander·Subin·Yumin의 전위에 따른 리튬 코발트 산화물 재구성과 산소 발생 연구가 Journal of Materials Chemistry A 게재 승인을 받았다.
- 2023-07 · Hyejeong의 리튬이온 전지 저장 중 열화와 용량 유지 연구가 Energy & Environmental Science 게재 승인을 받았다.
- 2023-07 · Hyejeong의 사용한 고니켈 양극 열처리 중 변형 연구가 Advanced Energy Materials에서 출판 절차에 들어갔다.
- 2023-05 · Jian·Hyejeong·Sungjae 등이 참여한 고니켈 양극의 반응 속도 지표 연구가 ACS Energy Letters에 출판되었다.
- 2023-05 · Bonho·Jinkyu·Juwon 등이 참여한 인산철 양극의 표면 변화 연구가 Energy & Environmental Science에 출판되었다.
- 2023-05 · Karl의 단일 원자 촉매와 이산화탄소 환원 논문이 Carbon Energy 게재 승인을 받았다.
- 2023-03 · Subin이 참여한 산화세륨 산화환원 성질과 촉매 활성 연구가 Applied Surface Science에 출판되었다.
- 2023-03 · Ikcheon의 일체형 실리콘 웨이퍼 음극 전고체 전지 연구가 ACS Energy Letters에 출판되었다.
- 2023-03 · Junho의 준고체 전해질을 이용한 전지 직접 인쇄 연구가 Energy Storage Materials에 출판되었다.
- 2023-01 · Munsoo·Danwon의 양극 잔류 탄산리튬 분해 연구가 Journal of Power Sources에 출판되었다.
- 2022-12 · Sugeun의 양극 재료 가열 합성 중 고체 반응 불균일성 연구가 Advanced Materials에 출판되었다.
- 2022-08 · Hwiho의 전고체 전지 고온 저장 연구가 Applied Physics Reviews에 출판되었다.
- 2022-08 · Junyeob·Dongok의 국소 고농도 전해질 연구가 Nature Communications에 출판되었다.
- 2022-04 · Yongjoon이 숙명여자대학교와 수행한 실리콘 구조의 열 전달 연구가 NPG Asia Materials에 출판되었다.

## 연락과 위치

- 교수: jwlim@snu.ac.kr, 02-880-2236[^prof]
- 교수 연구실: 서울대학교 자연과학대학 503동 521호[^prof][^dept]
- 연구실 위치·전화: 503동 506호·529호, 02-880-2237[^dept]
- 주소: 서울특별시 관악구 관악로 1 서울대학교, 우편번호 08826[^prof]
[^dept]: 서울대학교 화학부 교수 상세: 임종우. 부교수·연구실 이름·연구 소개·학력·주요 경력·연구실 위치와 전화. <https://chem.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=71&sc=y> 관측 2026-11-01.
[^prof]: 연구실 Jongwoo. 서울대학교 조교수 2017–2022, 부교수 2022–현재, 학력·경력·연락. <https://jwlimgroup.imweb.me/21> 관측 2026-11-01.
[^overview]: 연구실 Research Overview. 충전식 전지, 계산·자동 실험, 전기화학 촉매의 연구 목표와 세부 갈래. <https://jwlimgroup.imweb.me/33> 관측 2026-11-01.
[^cathode]: 연구실 Li-ion Battery Cathodes. 여러 양극재에서 리튬 삽입 속도를 연구하고, 국소 전류·리튬 농도와 응력·수명 관계를 분석하며 엑스선 현미경 기법을 개발한다. <https://jwlimgroup.imweb.me/28> 관측 2026-11-01.
[^metal]: 연구실 Li Metal Batteries. 리튬 금속 계면의 열화, 액체·고분자 전해질, 비불소 희석제 설계와 기계학습 모형을 연구한다. <https://jwlimgroup.imweb.me/45> 관측 2026-11-01.
[^solid]: 연구실 All-Solid-State Batteries. 황화물·할로젠화물 고체 전해질, 실리콘 음극, 은·탄소 무음극 전지의 접촉·안정성·저압 작동과 제조를 연구한다. <https://jwlimgroup.imweb.me/46> 관측 2026-11-01.
[^ai]: 연구실 AI-driven battery research. 전기화학 신호로 용량·수명을 예측하고 분자 기술자로 전해질 후보를 탐색한다. <https://jwlimgroup.imweb.me/47> 관측 2026-11-01.
[^computation]: 연구실 Computation. 밀도범함수이론·제일원리 분자동역학·기계학습 원자간 퍼텐셜을 연결해 전지 소재를 계산하고 자동 실험으로 이어 간다. <https://jwlimgroup.imweb.me/48> 관측 2026-11-01.
[^sdl]: 연구실 Self-driving laboratory. 계산으로 전해질 후보를 선별하고 장비로 전지를 자동 제작·시험하며 기계학습이 다음 실험 조성을 제안하는 순환 연구 시스템을 운영한다. <https://jwlimgroup.imweb.me/49> 관측 2026-11-01.
[^catalyst]: 연구실 Electrocatalyst. 구리계 촉매의 작동 중 상태 변화와 반응 선택성을 연구하고, 이산화탄소의 일산화탄소 전환과 질산 이온의 암모니아 전환 촉매 및 반응기를 개발한다. <https://jwlimgroup.imweb.me/50> 관측 2026-11-01.
[^members]: 연구실 Members. 박사후연구원·대학원생·방문 학생의 이름·과정·연구 주제·학교 이메일. <https://jwlimgroup.imweb.me/39> 관측 2026-11-01.
[^alumni]: 연구실 Alumni. 이전 박사후연구원·박사·박사학위 후보·석사·방문 학생 구획과 게시 진로. <https://jwlimgroup.imweb.me/22> 관측 2026-11-01.
[^publications]: 연구실 Publications. 심사 중 원고 구획과 2026–2019년·Before SNU 목록. 본문은 2021–2026년 구역의 학술 논문·리뷰·논평을 따른다. <https://jwlimgroup.imweb.me/37> 관측 2026-11-01.
[^news]: 연구실 Media/News의 월별 News. 본문의 날짜는 게시 연월이며 첫 화면에 겹친 글은 한 번만 센다. <https://jwlimgroup.imweb.me/16> 관측 2026-11-01.
[^p1]: S. Jo 외, J. Lim, Advanced Materials 35, 2207076 (온라인 2022-12-30). <https://doi.org/10.1002/adma.202207076> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202207076> 관측 2026-11-01.
[^p2]: S. Jo 외, J. Lim, Small Methods 9, 2401087 (온라인 2024-12-10). <https://doi.org/10.1002/smtd.202401087> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/10.1002/smtd.202401087> 관측 2026-11-01.
[^p3]: M. Song 외, J. Lim, Advanced Science 11, 2400568 (온라인 2024-04-06). <https://doi.org/10.1002/advs.202400568> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202400568> 관측 2026-11-01.
[^p4]: S. Jo 외, J. Lim, Advanced Materials 36, 2402024 (온라인 2024-05-21). <https://doi.org/10.1002/adma.202402024> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202402024> 관측 2026-11-01.
[^p5]: S. Hwang 외, J. Lim, Advanced Functional Materials 36, e21009 (온라인 2025-10-20). <https://doi.org/10.1002/adfm.202521009> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202521009> 관측 2026-11-01.
[^p6]: Y. Song 외, S. Park, Advanced Functional Materials 35, 2504739 (온라인 2025-05-09). <https://doi.org/10.1002/adfm.202504739> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202504739> 관측 2026-11-01.
[^p7]: S. Oh 외, S. Chung, InfoMat 7, e70033 (온라인 2025-05-29). <https://doi.org/10.1002/inf2.70033> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/10.1002/inf2.70033> 관측 2026-11-01.
[^p8]: K. A. Gandionco 외, J. Lim, Carbon Energy 6, e410 (온라인 2023-09-06). <https://doi.org/10.1002/cey2.410> 초록 기준(출판사 논문 페이지). 초록 원문 <https://onlinelibrary.wiley.com/doi/10.1002/cey2.410> 관측 2026-11-01.

# M-design Laboratory

**KAIST 화학과 · 김형준 교수**

- 분야: 물질 계면의 이론·계산 화학, 다중 규모 모의 계산 방법, 전기화학 촉매, 광활성 소재 설계
- 대분야: 화학, 소재
- 태그: 제1원리 계산[^dft][^umbd], 분자 동역학 시뮬레이션[^dft], 전기화학 촉매[^catalysts], 단일 원자 촉매[^catalysts], 연료전지[^catalysts], 광촉매·광전기화학[^photo], 태양전지[^photo], 할라이드 페로브스카이트[^photo]
- 홈페이지: <https://www.m-design-lab.net>
- 근거와 출처: [M-design Laboratory 근거 페이지](m-design-lab-sources.md)

> 물질이 맞닿는 곳에서 일어나는 반응을 원자·분자 수준의 계산으로 설명하고, 그 계산 방법과 에너지 소재를 함께 설계한다.[^research][^home]

## 무엇을 연구하나

김형준 교수가 이끄는 M-design Laboratory는 서로 다른 물질이나 상태가 맞닿는 계면을 연구한다. 특히 고체와 액체가 맞닿는 곳에서는 에너지 변환, 전자 전달, 여러 단계의 촉매 반응이 함께 일어난다. 촉매는 화학 반응에 참여해 반응 속도를 바꾸고 반응 과정에서 재생되는 물질이다. 연구실은 이러한 계면의 구조와 시간에 따른 변화를 계산해 새로운 촉매와 재료를 설계한다.[^faculty][^research]

중심 방법은 멀티스케일 시뮬레이션(서로 다른 공간·시간 규모의 계산을 연결해 대상을 모의하는 방법)이다. 액체에는 분자 동역학(Molecular Dynamics, MD), 즉 원자·분자에 작용하는 힘으로 시간에 따른 운동을 계산하는 방법을 쓴다. 고체의 전자 구조(전자들의 상태와 에너지 분포)는 밀도 범함수 이론(Density Functional Theory, DFT)으로 다룬다. DFT는 전자의 밀도를 바탕으로 물질의 전자 상태와 성질을 구하는 양자역학 계산법이다. 양자역학은 원자와 전자 등의 상태와 변화를 설명하는 물리 이론이다.[^research][^dft]

연구실은 계산법 자체도 개발한다. 고체와 액체를 함께 다루는 방법과, 원자 사이의 반데르발스 힘을 보정하는 방법이 그 예다. 반데르발스 힘은 원자·분자의 전기적 성질에서 생기며 공유결합·이온결합과 구별되는 상호작용이다. 평균장(주변의 영향을 평균적인 작용으로 나타내는 근사)을 통해 고체와 액체의 계산을 연결하고, 금속·이온성 물질·분자성 물질의 결합을 함께 다루려 한다.[^dft][^umbd]

이 방법들을 쓰는 대상은 전기화학 촉매와 빛에 반응하는 소재다. 이산화탄소와 질소 포함 분자의 전기화학적 변환, 연료전지(연료와 산소의 화학 반응에서 전기를 얻는 장치) 촉매의 반응과 성능 저하, 태양전지와 광촉매(빛을 흡수해 화학 반응을 촉진하는 물질) 소재의 설계를 연구한다. 전기화학은 전자의 이동을 수반하는 물질 변화와 전기 에너지의 관계를 다루는 분야다. 연구실은 소재가 어떤 반응을 거쳐 기능을 내는지 이해하고, 그 설명을 소재 선택과 설계로 연결한다.[^catalysts][^photo]

최근 논문에서는 주변 환경의 열적 영향을 반영해 전자의 상태 변화를 계산하는 방법과, 결정 구조를 바탕으로 물성을 예측하는 딥러닝 모형도 개발했다. 딥러닝은 여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 방법이다. 전자의 시간에 따른 변화는 양자 상태를 수학적으로 나타내는 파동함수로 기술하고, 소재 물성 예측에서는 결정 속 원소의 성질과 전자 배치 정보를 학습에 반영한다.[^p5][^p6]

## 주요 연구 주제

### 1. 고체·액체 계면을 연결하는 계산 방법

DFT-CES(Density Functional Theory in Classical Explicit Solvent)는 고체를 양자역학으로, 액체를 분자 동역학으로 계산해 연결하는 방법이다. 연구실은 이를 평균장 QM/MM(Quantum Mechanics/Molecular Mechanics, 양자역학과 분자역학 계산을 결합하는 방법)으로 소개한다. 전극과 전해질(이온의 이동으로 전류를 전달하는 물질)의 계면에 전압이 걸렸을 때의 현상을 원자 수준에서 이해하고, 전기화학 촉매 설계에 활용한다.[^dft] DFT-CES2에서는 계면의 상호작용을 서로 밀어내는 작용, 전하 사이의 작용, 분산력으로 나눠 표현하는 방법을 개발했다.[^p1] 기체와 고체의 계면에서는 분자가 표면에 모이는 흡착과 표면에서 떨어져 나오는 탈착을 유체 운동과 함께 계산하는 모형도 연구했다.[^p7]

### 2. 재료의 결합과 물성 예측

연구실은 DFT가 반데르발스 힘을 기술할 때 필요한 보정법을 개발한다. 연구실이 uMBD라고 부르는 보정법은 금속성 결합과 이온성 결합, 반데르발스 상호작용을 함께 다룬다. 분자 쌍, 분자 결정, 금속, 이온성 고체, 산화물, 금속 표면의 분자 흡착을 대상으로 평가했으며, 리튬 이온 배터리의 양극 소재와 불균일 촉매에도 적용한다. 불균일 촉매는 반응물과 서로 다른 상태에 있는 촉매를 뜻한다.[^umbd]

물성 예측에는 PROFiT-Net(PRoperty-networking Orbital Field maTrix-convolutional neural Network)이라는 딥러닝 모형을 개발했다. 결정의 표현에 원소의 성질과 최외곽 전자 배치를 반영해, 결정 속 원소 특성 사이의 관계를 학습한다. 유전상수(물질의 유전율을 진공의 유전율로 나눈 값)와 실험 밴드갭(전자가 가질 수 없는 에너지 구간의 폭) 등을 예측하고 물리적 경향도 포착했다.[^p6]

### 3. 전기화학 촉매의 반응과 안정성

이산화탄소를 연료나 화학물질로 바꾸는 촉매의 반응 경로를 계산하고, 촉매 표면과 반응물의 결합 성질을 조절하는 설계 기준을 연구한다. 질소를 포함한 분자들의 전기화학적 전환도 다룬다. 연료전지에서는 질소가 도입된 탄소 기반 촉매의 산소 환원 반응과 성능 저하 원리를 연구한다. 환원은 화학종(구별되는 원자·분자·이온 등의 종류)이 전자를 얻는 변화다. 금속 원자가 각각 떨어져 분산된 단일 원자 촉매의 전기화학 반응도 연구 대상이다.[^catalysts]

전극과 전해질의 경계에서 전하가 나뉘어 배열되는 전기 이중층의 구조도 연구한다. 농축 수용액에서 물 분자의 방향 변화와 음이온(음전하를 띤 이온)의 표면 응축이 어떻게 나타나는지 원자 수준의 모의 계산과 분광 측정으로 설명했다.[^p2] 산소 환원 반응에서는 알칼리 금속 양이온이 반응 중간체와 결합해 촉매로 작용한다는 결과도 제시했다. 양이온은 양전하를 띤 이온이며, 반응 중간체는 반응 도중 생겼다가 다른 물질로 바뀌는 화학종이다.[^p3]

### 4. 광활성 소재와 양자 동역학

태양전지와 광촉매에 쓸 물질을 이론적으로 설계하고, 빛을 받은 뒤 전자 상태와 원자 배열이 시간에 따라 어떻게 변하는지 연구한다. 납을 포함하지 않는 태양전지 후보 물질과 납 할라이드 페로브스카이트(납과 할로젠 원소를 포함하며 페로브스카이트 결정 구조를 갖는 물질)의 안정성과 광 동역학을 다룬다. 구리 단일 원자가 도입된 이산화타이타늄 광촉매에서는 빛을 받았을 때의 전자 상태 변화와 구조 변형을 계산한다. 용액 속 광촉매의 밴드 위치(전자가 가질 수 있는 에너지 구간의 경계)를 예측하는 방법도 개발한다.[^photo]

용액 속 소재의 빛에 대한 성질을 계산하는 방법을 만들고, 용매가 달라질 때 그 성질이 어떻게 바뀌는지 예측했다.[^p4] 전자의 동역학에는 열 효과를 반영한 가우스 파동묶음(Thermalized Gaussian Wavepacket, TGW)을 도입했다. 이는 모형화한 주변 열적 환경의 파동함수를 고전적 운동 경로를 따라 시간에 맞춰 계산하는 방법이다. 주변 환경의 열 효과와 결맞음 소실(양자 상태 사이의 위상 관계가 흐트러지는 현상)을 함께 다룬다.[^p5]

## 대표 논문

김형준 교수가 KAIST 재직 중 공저한 2021–2026년 논문에서 계산 방법, 전기화학 계면·촉매, 광활성 소재·양자 동역학, 기계학습 물성 예측을 고르게 담도록 7편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 마지막 저자 표시는 전체 저자 순서를 뜻한다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [DFT-CES2: Quantum Mechanics Based Embedding for Mean-Field QM/MM of Solid–Liquid Interfaces](https://doi.org/10.1021/jacsau.5c00176) · JACS Au | 고체와 액체의 경계에서 일어나는 현상을 원자 수준으로 계산하는 방법을 만들었다. 서로 밀어내는 작용, 전하 사이의 작용, 분산력을 나눠 표현하고 원자에 따른 매개값을 사용했다. 정밀한 양자역학 계산과 비교해 계면 상호작용을 기술하는 정확도를 검증했다. 여러 성분이 섞인 고체·액체 계면의 원자 수준 구조를 밝히는 데 널리 적용할 수 있을 것으로 기대했다.[^p1] | 첫 저자 Taehwan Jang, 마지막 저자 Hyungjun Kim |
| 2 | 2026 | [Electric Double Layer Structure in Concentrated Aqueous Solution](https://doi.org/10.1038/s41467-026-70322-5) · Nature Communications | 농도가 높은 수용액에서 전극 주변의 이온과 물 분자가 어떻게 배열되고 그 구조가 바뀌는지 모든 원자를 고려한 모의 계산으로 설명했다. 음극 쪽 전위(단위 전하당 전기적 위치 에너지) 영역에서 물 분자들의 방향이 집단적으로 바뀌고, 양극 쪽 전위 영역에서는 음이온이 표면에 응축됨을 관측했으며 분광 측정으로도 뒷받침했다. 계산한 구조 변화 전위는 실험에서 전기용량(전압 변화에 따른 저장 전하량 변화의 비) 곡선의 극대점이 나타나는 전위와 일치했다. 전기 이중층의 구조 상태도를 구성했다.[^p2] | 첫 저자 Minho M. Kim, 마지막 저자 Hyungjun Kim |
| 3 | 2024 | [Alkali Metal Cations Act as Homogeneous Cocatalysts for the Oxygen Reduction Reaction in Aqueous Electrolytes](https://doi.org/10.1038/s41929-024-01241-1) · Nature Catalysis | 반응에 직접 관여하지 않는다고 여겨지던 알칼리 금속 양이온이 물속에서 반응 중간체와 결합하고 반응 속도를 결정하는 촉매로 작용할 수 있음을 보였다. 탄소에서 일어나는 알칼리성 산소 환원 반응 중 나트륨 이온의 전자 구조가 물에 둘러싸였을 때와 달라짐을 측정했다. 물에서 불안정한 나트륨·산소 중간체의 형성을 확인하고 이론 계산과 함께 촉매 역할을 설명했다.[^p3] | 첫 저자 Sang Gu Ji, 공저자 Hyungjun Kim(11/12), 마지막 저자 Chang Hyuck Choi |
| 4 | 2024 | [Elucidating Solvatochromic Shifts in Two-Dimensional Photocatalysts by Solving the Bethe–Salpeter Equation Coupled with Implicit Solvation Method](https://doi.org/10.1021/acs.jpclett.4c00752) · The Journal of Physical Chemistry Letters | 용매를 연속적인 환경으로 나타내는 방법과 물질이 빛에 반응하는 성질을 계산하는 방정식을 결합했다. 이황화몰리브데넘, 포스포렌(인으로 이루어진 층상 물질), 질화탄소에 적용해 용매의 영향을 살폈다. 앞의 두 물질에서는 빛에 대한 반응을 나타내는 피크의 위치가 거의 바뀌지 않았지만, 질화탄소에서는 용매의 유전율이 달라지면 광학 성질이 크게 달라질 것으로 예측했다. 광촉매와 빛·전기를 함께 쓰는 화학 반응의 소재 설계에 도움을 줄 것으로 기대했다.[^p4] | 첫 저자 Se-Jun Kim, 마지막 저자 Hyungjun Kim |
| 5 | 2025 | [Semiclassical Multistate Quantum Dynamics Using Thermalized Gaussian Wavepacket](https://doi.org/10.1021/acs.jctc.5c01001) · Journal of Chemical Theory and Computation | 주변 환경의 열 효과와 결맞음 소실을 반영하면서 전자의 상태 변화를 계산하는 방법을 제안했다. 열 효과를 반영한 가우스 파동묶음으로 주변 열적 환경을 나타내고, 이를 고전적인 운동 경로에 따라 시간에 맞춰 계산하도록 했다. 두 상태 모형에서 약한 결합일 때의 이론적 전이 속도를 재현했고, 두 상태와 세 상태 모형에서 정밀한 양자 계산의 시간 변화를 재현했다.[^p5] | 첫 저자 Yoosang Son, 마지막 저자 Hyungjun Kim |
| 6 | 2024 | [PROFiT-Net: Property-Networking Deep Learning Model for Materials](https://doi.org/10.1021/jacs.4c05159) · Journal of the American Chemical Society | 결정 속 원소의 성질과 최외곽 전자 배치를 반영한 구조 표현으로 물성을 예측하는 딥러닝 모형을 만들었다. 유전상수와 실험 밴드갭 등을 예측하는 정확도가 비교한 다른 선도 모형들보다 높았다. 평가에서는 물리적으로 불가능한 음의 밴드갭 예측을 피하고 물리 모형과 닮은 경향을 나타냈다. 기능성 재료의 개발을 앞당길 것으로 기대했다.[^p6] | 첫 저자 Se-Jun Kim, 마지막 저자 Hyungjun Kim |
| 7 | 2026 | [Thermodynamically Consistent Incorporation of the Langmuir Adsorption Model into Compressible Fluctuating Hydrodynamics](https://doi.org/10.1063/5.0306932) · Journal of Chemical Physics | 기체 분자가 고체 표면에 붙었다 떨어지는 현상과 기체의 흐름을 함께 계산하는 방법을 만들었다. 분자가 이동할 때 기체와 표면의 질량·에너지를 어떻게 바꿔야 하는지 정하고, 그 방법이 열역학적 평형을 나타냄을 수학적으로 확인했다. 표면에 충돌하는 기체 분자의 평균 운동 에너지가 일반적인 기체 분포에서 구한 값과 달라 내부 에너지 보정이 필요함을 밝혔다. 일산화탄소와 아르곤의 혼합 기체를 모의해 계산 방법을 검증했다.[^p7] | 첫 저자 Hyun Tae Jung, 공저자 Hyungjun Kim, 마지막 저자 Changho Kim |

## 교수와 전문 분야

김형준 교수는 KAIST에서 화학 학사(2004), Caltech에서 화학 박사(물리 부전공, 2009)를 받았다. KAIST 응용과학연구소 선임연구원(2009.07–2012.12)을 거쳐 EEWS 대학원 조교수(2013.01–2016.02), 같은 대학원 부교수(2016.03–2020.02), 화학과 부교수(2017.09–2023.08)를 지냈으며 2023.09부터 화학과 교수로 적혀 있다. Caltech 화학과 방문교수 경력은 2022.08부터다.[^professor]

전문 분야는 계면의 물리화학을 설명하는 이론·계산 방법과 에너지 소재 설계다. 고체와 액체를 연결하는 계산법, 다양한 재료의 결합을 다루는 DFT 보정법을 직접 개발하고, 전기화학 촉매와 광활성 소재의 반응 원리에 적용한다.[^research][^dft][^umbd][^catalysts][^photo]

최근 논문에는 용액 속 광촉매의 광학 성질을 예측하는 계산법, 열적 환경을 반영하는 전자 동역학, 결정의 물성을 예측하는 딥러닝 모형이 포함된다. 분자·소재의 원리를 계산으로 설명하는 연구와 그 계산 도구를 만드는 연구를 함께 수행한다.[^p4][^p5][^p6]

## 응용 분야

연구실은 이산화탄소의 화학적 전환, 질소 포함 분자의 전기화학적 전환, 연료전지 촉매, 리튬 이온 배터리 양극, 태양전지와 광촉매 소재를 응용 대상으로 든다.[^catalysts][^umbd][^photo] 연구 도구로는 DFT-CES를 위한 Quantum-espresso와 Lammps 연결 코드, uMBD의 에너지 계산 코드를 소개한다.[^software]

## 구성원

2026년 11월 1일 Members 쪽의 교수 외 구성원 15명이다. Researcher 5명과 PhD candidate 10명이며, 학력은 각 카드의 표기다. 구성원 과정과 이전에 받은 학위는 구분했다.[^members] 「대표 논문 참여」는 위 표의 번호이며, 전체 저자 목록에서 이름 순서와 철자가 같은 경우에 표시했다.

| 이름 | 직위·과정 | 게시 학력 | 대표 논문 참여 |
|---|---|---|---|
| 이한결 (Hankyul Lee) | 연구원 (Researcher) | PhD in Chemistry, KAIST |  |
| 김지후 (Jihoo Kim) | 연구원 (Researcher) | PhD in Chemistry, KAIST |  |
| 정재우 (Jaewoo Jeong) | 연구원 (Researcher) | PhD in Chemistry, KAIST |  |
| 김민호 (Minho M. Kim) | 박사과정 (PhD candidate) | BS in Chemistry (Double major: Physics), KAIST | 2, 3 |
| 이준수 (Junsoo Lee) | 박사과정 (PhD candidate) | BS in Chemistry (Minor: Computer Science), KAIST |  |
| 최예성 (Yeseong Choi) | 박사과정 (PhD candidate) | BS in Chemistry, SNU | 5 |
| 손지훈 (Jihoon Son) | 박사과정 (PhD candidate) | MS in Energy Science and Technology, CNU |  |
| 왕도영 (Doyoung Wang) | 박사과정 (PhD candidate) | BS in Chemistry (Minors: Computer Science, Data Science), Michigan State U |  |
| 조아라 (Ara Cho) | 연구원 (Researcher) | PhD in Chemical Engineering, POSTECH |  |
| 백두암 (Dooam Baik) | 연구원 (Researcher) | PhD in Chemistry, KAIST |  |
| 정현태 (Hyuntae Jung) | 박사과정 (PhD candidate) | BS in Chemistry (Double major: Mathematics), KAIST |  |
| 손유상 (Yoosang Son) | 박사과정 (PhD candidate) | BS in Chemistry, SNU | 3, 5 |
| 박재원 (Jaewon Park) | 박사과정 (PhD candidate) | BS in Chemistry (Minor: Mathematics), KAIST |  |
| 승우정 (Woojung Seung) | 박사과정 (PhD candidate) | BS in Chemistry (Double major: Mathematics), KAIST |  |
| 권양희 (Yanghui Kwon) | 박사과정 (PhD candidate) | MS in Materials Science and Engineering, POSTECH |  |

## 졸업생·이전 구성원과 명예 구성원

2026년 11월 5일 Alumni 쪽 기준이다. 박사 20명, 석사 2명, 이전 박사후연구원 3명, 「Honorary Members (not official, but very special)」 5명을 게시한다. 학위 연도는 2015–2026년이고, 박사후연구원의 기간은 각 재직 기간이다. 명예 구성원은 학부 연구 참여·공동지도 관계로 소개되어 있다. 이한결·백두암·정재우는 현재 구성원 쪽에도 이름이 있다.[^alumni][^members]

### 박사

| 이름 | 학위·관계와 연도·기간 | 게시 진로 | 학위 논문 |
|---|---|---|---|
| 전지원 (Jiwon Jeon) | 박사 (2015) | Researcher, Chungnam National University | Multiscale modeling of electron transfer reactions in solutions for the photovoltaic applications |
| 임형규 (Hyung-Kyu Lim) | 박사 (2017) | Professor, Kangwon National University (강원대학교 화학공학과) | Multi-Scale Simulation Framework for Solid-Liquid Interface: Applications in Energy and Environmental Systems |
| 이한결 (Hankyul Lee) | 박사 (2018) | Researcher, KAIST | Atomistic Investigation on Non-Covalent Binding Interaction in Biomolecular Systems: from Aromatic Interaction to Protein-DNA Interaction |
| 김수지 (Suji Gim) | 박사 (2019) | Samsung Electronics (삼성전자) | Multiscale Simulation for Accurate Prediction of Physicochemical Properties of Solid-Liquid Interface |
| 김성민 (Sungmin Kim) | 박사 (2020) | Samsung Advanced Institute of Technology (삼성 종합기술원) | First Principles Modeling on Stability of Perovskite Solar Cell Materials |
| 신승재 (Seung-Jae Shin) | 박사 (2022) | Assistant Professor, UNIST (에너지화학공학과) | Development of Mean-field QM/MM method for Atom-scale Investigation of Electrochemical Interfaces |
| 신동엽 (Dongyup Shin) | 박사 (2022) | Assistant Professor, Kangwon National University (강원대학교 화학과) | Density Functional Study of Electrochemical Small-Molecule Conversion on Single-Atom Catalysts |
| 김세준 (Se-Jun Kim) | 박사 (2024) | Post Doc, Caltech | Development of a Many-Body Perturbation Theory for Solvated Materials and an Artificial Intelligence Model for Materials |
| 장태환 (Taehwan Jang) | 박사 (2024) | Post Doc, Caltech | Quantum Mechanics Based Embedding Mean-Field QM/MM for Solvated Systems |
| 박지혜 (Jihye Park) | 박사 (2025) | Post Doc, Lawrence Berkeley National Lab | Macromolecular Materials Modeling: Efficient Ensemble Sampling and Applications to Bio-inspired and Energy Storage Systems |
| 신혜영 (Hyeyoung Shin) | 박사 (2016) | Associate Professor, Kyung Hee University (경희대학교 화학과) | Multiscale Materials Modelling and Design for Heterogeneous Catalysts Applications |
| 엄태대형 (Taedaehyeong Eom) | 박사 (2018) | Samsung Electro Mechanics (삼성전기) | First Principles Based Multiscale Model of The Configuration Dependent Materials Properties |
| 김민호 (Minho Kim) | 박사 (2019) | Assistant Professor, Kyung Hee University (경희대학교 응용화학과) | First-Principles Simulations on the Interfacial Interactions: from Method Development to Applications |
| 한명훈 (Myung Hoon Han) | 박사 (2019) | Samsung Electronics (삼성전자) | Density-Functional Theory Studies of the Calculation method for Catalyst and the Material’s Energy Barrier |
| 조강진 (Kangjin Cho) | 박사 (2020) | Secretary, Korea Government | Molecular Dynamics Simulation Studies on Fluid Transport Properties at Solid-Liquid Interfaces |
| 하윤후 (Yoonhoo Ha) | 박사 (2022) | Samsung Advanced Institute of Technology (삼성 종합기술원) | First-Principles Time-Domain Study on Enhanced Luminescence of Nanostructured Halide Perovskites |
| 백두암 (Dooam Paik) | 박사 (2024) | Post Doc, KAIST | Understanding Pi-Pi Interaction in Water Using Mean-field QM/MM Method |
| 이현주 (Hyeonju Lee) | 박사 (2024) | Post Doc, Caltech | Understanding of Polymer Nanocomposite Material using Molecular Dynamic Simulation |
| 안지훈 (Jihun An) | 박사 (2025) | Samsung Electronics | Multiscale Modeling of Electronic Polarization of Metal at Liquid Interfaces |
| 정재우 (Jaewoo Jeong) | 박사 (2026) | Post Doc, KAIST | Theoretical mechanistic understanding of oxygen evolution: effect of solvent, spin, doping, and support structure |

### 석사

| 이름 | 학위·관계와 연도·기간 | 게시 진로 | 학위 논문 |
|---|---|---|---|
| 전경희 (Kyeonghee Jeon) | 석사 (2015) | Samsung SDI (삼성 SDI) | Material Simulation for Environmental Applications towards Water Treatment and Carbon Dioxide Separations |
| 하예슬 (Ye-Seol Ha) | 석사 (2018) | LG Innotek (LG 이노텍) | Atomistic Modeling on the Microstructure of Organic Functional Materials for the Energy Applications |

### 이전 박사후연구원

| 이름 | 학위·관계와 연도·기간 | 게시 진로 | 학위 논문 |
|---|---|---|---|
| 람제드 드비치 (Lamjed Debbichi) | 박사후연구원 (2015–2018) | Data Scientist at Faurecia, France |  |
| 알레코스 세갈리나 (Alekos Segalina) | 박사후연구원 (2021–2022) | Senior Researcher, Center for Advanced Reaction Dynamics (CARD), IBS |  |
| 스테판 링에 (Stefan Ringe) | 박사후연구원 (2019–2020) | Associate Professor, Korea University (고려대 화학과) |  |

### 명예 구성원

| 이름 | 학위·관계와 연도·기간 | 게시 진로 | 학위 논문 |
|---|---|---|---|
| 최정모 (Jeong-Mo Choi) | 학부 연구 참여 | Associate Professor, Pusan National University (부산대학교 화학과) |  |
| 강경원 (Gyeongwon Kang) | 학부 연구 참여 | Assistant Professor, Kangwon National University (강원대학교 화학과) |  |
| 오지석 (Jisuk Oh) | 학부 연구 참여 | Graduate student, Seoul National University |  |
| 김원준 (Won June Kim) | 공동지도 관계 | Associate Professor, Changwon National University (창원대학교 화학과) |  |
| 권민재 (Minjae Kwen) | 학부 연구 참여 | Graduate student, Harvard University |  |

## 최근 5년 논문 목록

계면 계산법, 촉매 반응, 배터리 전해질, 태양전지·광활성 소재와 분자·고분자 구조, 생체 분자 상호작용과 형광 소재를 다룬 논문들이다. 연구실 Journals의 2021–2026년 구역에 기재된 논문 중 91편을 연도별로 싣는다. 월·일이 따로 확인되는 논문은 출판일을 기준으로 하고, 연도만 적힌 2021년 항목은 해당 연도 구역을 따른다. 2026년 구역의 in press 2편은 「출판 중」으로 구분했다. 저자 이름 뒤의 별표는 누리집 표시이며, 더하기 기호는 누리집이 equal contribution으로 밝힌 공동 기여 표시다.[^pubs]

**2026**

- S Kim+, H Jun+, J Park+, S Kim+, S Noh, S-J Shin, B Kim, K-S Lee, J Kim, J Byeon, M Ban, D Choi, H Kim, JH Jang, W Kim, J Moon\*, JY Lee\*, H Kim\*, J Lee\*. "Stabilizing Ruthenium Atom Layer Neighbors through Molecular and Metal Support Interactions for Water Electrolyzers". *Nature Communications, in press (출판 중, 연구실 2026년 구역)*.
- DH Oh+, J Jeong+, S Lee, Y Park, S Chi, Y Baik, H Kim, H Shin\*, M Choi\*. "Hole-Activated Lattice Oxygen Enables Pt-Free Propane Dehydrogenation by Eliminating the Hydrogen Recombination Bottleneck". *Angewandte Chemie, in press (출판 중, 연구실 2026년 구역)*.
- T Jang+, MM. Kim+, H Ryu\*, WA Goddard, III\*, H Kim\*. "Polarizable Split-Charge Equilibration for Accurate Modeling of Nonbonded Interactions". *Journal of Chemical Theory and Computation, 22, 17, 9109–9119*.
- J Oh, Y Son\*, H Kim\*. "Dynamic Mirror Image Charge Method for First-Principles-Based Modeling of Surface Polarization at the Electrode–Electrolyte Interface". *Journal of Chemical Theory and Computation, 22, 17, 9109–9119*.
- J Jeong, H Kim\*, H Shin\*. "Water-mediated Stabilization of Oxyl Radicals as a Driving Force for the Oxygen Evolution Reaction". *Chemical Engineering Jounral, 546, 180201*.
- Y Baik, S Chi, D Oh, S Lee, K Lee, C Oh, MM Kim, D Paik, M Chung, H Kim, M Choi\*. "Beyond Geometric Effects: Particle Size-Dependent Electronic Promotion in Ru Catalysts for Ammonia Synthesis". *Journal of the American Chemical Society, 148, 29, 31079–31087*.
- T Jones, MM Kim, SM Sibug-Torres, E Wyatt, N Spiesshofer, JW Beattie, J Bar-David, R Arul, B de Nijs, H Kim\*, JJ Baumberg\*. "How the Electrochemical Double Layer Manipulates Molecule–Metal Interactions". *ACS Nano, 20, 25, 18284–18292*.
- MM Kim+, DH Kim+, J Cho+, S-J Shin\*, CH Choi\*, H Kim\*. "Electric Double Layer Structure in Concentrated Aqueous Solution". *Nature Communications, 17, 3645*.
- S Hong+, J Jeong+, E Yoo+, D Shin, S Yoo, E Lee, H Kim, H Shin\*, YJ Hwang\*. "Operando Cu Aggregation-Induced Spin State Modulation in Fe–Cu Single Atom Catalyst for Enhanced Tandem Electrochemical Nitrate Reduction Reaction". *Journal of the American Chemical Society, 148, 14, 15114-15124*.
- HT Jung, H Kim, AL Garcia, AJ Nonaka, JB Bell, I Srivastava, C Kim\*. "Thermodynamically Consistent Incorporation of the Langmuir Adsorption Model into Compressible Fluctuating Hydrodynamics". *Journal of Chemical Physics, 164, 094103*.
- MM Kim, WA Goddard, S-J Shin\*, H Kim\*. "Understanding the Hydrated Proton at the Electrode–Electrolyte Interface". *Electrochimica Acta, 588, 148475*.
- MM Kim, CH Choi\*, H Kim\*. "Electric Double Layer Charging, a New Framework for Optimizing Electrocatalyst Design and Performance". *ACS Energy Letters (Perspective), 11, 3, 2499-2507*.
- G Wu. J Park, W-G Liu, Y Jiao, L Zhang, H Han, C Tang, T Jang, MM Kim, B Song, X Li, R Zhang, E Liu, H Wu, Y Wu, X Zhao, Y Feng, Q Li, H Kim, RD Astumian\*, WA Goddard III\*, JF Stoddart\*. "Precise Synthesis of Non-Equilibrium Rotaxanes via Pumping in Water". *Chem, 12, 4, 102878*.

**2025**

- E Lee, J Lee, DH Kang, JC Hyun, CY Kim, J Kim, S Ha, MM Kim, BS Youn, J Yoon, G Bae, KH Shin, SM Lee, HS Park, CH Choi, H-J Jin, H-K Lim\*, H Kim\*, YS Yun\*. "Electrowetting-Driven Capacitance Enhancement Dependent on Charge Carrier and Nanopore Size". *eScience Energy, 1, 100006*.
- J Park, WA Goddard III\*, H Kim\*. "Molecular Dynamics-Based Optimization of Glyme Electrolytes". *Journal of Physical Chemistry B, 129, 47, 12285-12293*.
- A Segalina, T Jang, MM Kim, H Ihee, JW Park\*, WA Goddard III\*, H Kim\*. "Deciphering Charge Transfer and Hydrogen Bonding Characteristics from Liquid Water XAS Spectra". *Journal of Chemical Theory and Computation, 21, 22, 11679-11686*.
- Y Son, Y Choi, OV Prezhdo\*, H Kim\*. "Semiclassical Multistate Quantum Dynamics Using Thermalized Gaussian Wavepacket". *Journal of Chemical Theory and Computation, 21, 19, 9772-9783*.
- J Park, WJ Kim, WA Goddard III\*, EK Lee\*, H Kim\*. "Ion Speciation and Mobility in Solid Polymer Electrolytes: Insights from Molecular Dynamics Simulations". *Journal of Physical Chemistry Letters, 16, 28, 7242-7248*.
- H Lee, A Hazari, JA Raskatov, H Kim, WA Goddard III\*. "Design Guidelines to Control Rippled β-Sheets versus Pleated β-Sheets in Mixed-Chirality Peptides". *Journal of the American Chemical Society, 147, 21, 17642-17650*.
- S Kim, D-E Hwang, H Kim, J-M Choi\*. "Investigating the Nature of PRM:SH3 Interactions Using Artificial Intelligence and Molecular Dynamics". *Journal of Chemical Information and Modeling, 65, 11, 5662-5671*.
- H Choi+, S-J Shin+, G Bae+, J Cho, MH Han, MT Sougrati, F Jaouen, K-S Lee, H-S Oh, H Kim\*, CH Choi\*. "Space Charge, Modulating the Catalytic Activity of Single-Atom Metal Catalysts". *Journal of the American Chemical Society, 147, 16, 13320-13228*.
- T Jang, S-J Shin, H-K Lim, WA Goddard III, H Kim\*. "DFT-CES2: Quantum Mechanics Based Embedding for Mean-Field QM/MM of Solid–Liquid Interfaces". *JACS Au, 5, 4, 2047-2058*.
- J An, H-K Lim, H Kim\*. "Kernel-Based Modeling of Electron-Density Polarization at Metal–Liquid Interfaces". *Journal of Chemical Theory and Computation, 21, 8, 4134-4141*.
- A Hazari, MR Sawaya, H Lee, M Sajimon, H Kim, WA Goddard III, D Eisenberg, JA Raskatov\*. "Formation of Rippled β-sheets from Mixed Chirality Linear and Cyclic Peptides-New Structural Motifs based on the Pauling-Corey Rippled β-sheet". *Chemical Science, 16, 5907-5917*.
- S-M Jung, S Kim, J An, K-S Kim, M Kim, J Kwon, H Kim\*, Y-T Kim\*, SS Park\*. "Synergistic Effects of Co–N4 and Ni–N4 Sites in 2D Conductive Metal–Organic Framework Electrocatalysts for Enhanced Oxygen Reduction Reaction Performance". *ACS Catalysis, 15, 5568-5576*.
- S Kim+, S-J Shin+, H Kim+, B Kim, N Noh, K-S Lee, J Park, H Jun, J Kim, J Byeon, S Lee, H Huang, S Noh, HB Jeong, JH Jang, JM Yuk, W Kim, H Kim\*, J Lee\*. "Self-assembly-assisted Dynamic Placement of Noble Metals Selectively on Multifunctional Carbide Supports for Alkaline Hydrogen Electrocatalysis". *Energy Environmental Science, 18, 659-673*.
- N Nurlan, J Jeong, M Nurmyrza, H Kim, H Shin\*, W Lee\*. "The Effect of Two Critical Operating Factors on the Enhanced Catalytic Conversion of Aqueous NO3– to NH4+ by Pt-Co@NC and Theoretical Verification of its Surface Reaction Mechanism". *Chemical Engineering Journal, 506, 159874*.
- J-Y Jung, J Lee, Y Kim, D Shin, J Park, S Kim, HR Byon\*, H Kim\*, H Song\*. "Switching Methane Selectivity in Carbon Dioxide Electroreduction via Confining Copper(I) Oxide Nanocubes by Polyimine Shells". *ACS Catalysis, 15, 3, 2642-2653*.
- H Kim+, MM Kim+, J Cho+, S Lee, DH Kim, S-J Shin, T Utsunomiya, WA Goddard III, Y Katayama\*, H Kim\*, CH Choi\*. "Cation Effect on the Electrochemical Platinum Dissolution". *Journal of the American Chemical Society, 147, 5, 4667-4674*.

**2024**

- SG Ji+, MM Kim+, MH Han+, J Cho, Y Son, YY Kim, J Jeong, ZH Kim, KH Chae, H-S Oh\*, H Kim\*, CH Choi\*. "Alkali Metal Cations Act as Homogeneous Cocatalysts for the Oxygen Reduction Reaction in Aqueous Electrolytes". *Nature Catalysis, 7, 1330-1338*.
- NH Kwon+, S-J Kim+, T-H Gu, JM Lee, MH Kim, D Paik, X Jin, H Kim\*, S-J Hwang\*. "Surface Optimization of Noble-Metal-Free Conductive [Mn1/4Co1/2Ni1/4]O2 Nanosheets for Boosting Their Efficacy as Hybridization Matrices". *Advanced Science, 11, 44, 2408948*.
- S Yang, J Chu, J Park, H Kim\*, B Shin\*. "Enhancement of Lithium-Mediated Nitrogen Reduction by Modifying Center Atom of Tetraalkyl-Type Ionic Liquids". *Angewandte Chemie, 63, 50, e202411909*.
- S Lee+, H Kim+, MM Kim+, TK Ko, HM Chi\*, H Kim\*, CH Choi\*. "Elucidating the Pivotal Role of Acid-Catalyzed Hydration in Electrochemical Carbon Corrosion". *ACS Catalysis, 14, 23, 17293-17302*.
- J Kim+, SY Lee+, S-J Kim+, B Koo, J Chung, D Lee, S Choi, J Kim, S Seo, C Nam, KA Gandionco, G Bak, S Jo, N Kim, H-J Shin, KH Chae, DH Won, MA Marcus, DA Shapiro, S-C Haw, DH Alsem, NJ Salmon, BK Min, H Kim\*, YJ Hwang\*, J Lim\*. "Spatiotemporal Active Phase Evolution for CO2 Electrocatalysis". *Joule, 8, 12, 3373-3385*.
- S-J Kim, WJ Kim, C Kim, EK Lee\*, H Kim\*. "PROFiT-Net: Property-Networking Deep Learning Model for Materials". *Journal of the American Chemical Society, 146, 38, 26000-26007*.
- L Zhang, S Jeong, J Lee, J Kim, JS Lee, J Park, J Hong, J-H Eom, H Kim, YM Rhee, H Lee\*, H-S Lee\*. "Red Fluorescence from Organic Microdots: Leveraging Foldamer-Linked Azobenzene for Enhanced Stability and Intensity in Bioimaging Applications". *Small, 20(46), 2401480*.
- S Choi, S-J Kim, S Han, J Wang, J Kim, B Koo, AA Ryabin, S Kunze, H Hyun, J Han, S-C Haw, KH Chae, CH Choi, H Kim, J Lim\*. "Enhancing Oxygen Evolution Reaction via a Surface Reconstruction-Induced Lattice Oxygen Mechanism". *ACS Catalysis, 14(20), 15096–15107*.
- J Heo, A Segalina, D Kim, D-S Ahn, KY Oang, S Park, H Kim, H Ihee\*. "Ultrafast Interfacial Charge Transfer Initiates Mechanical Stress and Heat Transport at the Au-TiO2 Interface". *Advanced Science, 11(34), 2400919*.
- C Zhang, Y Son, H Kim, S-H Lee, X Liang, G Fu, S-U Lee, D-A Park, Q Jiang, K Zhu, N-G Park\*. "Work Function Tuning of a Weak Adhesion Homojunction for Stable Perovskite Solar Cells". *Joule, 8(5), 1394-1411*.
- M Kim, J Jeong, DH Kim, G Park, J Yi, S Kim, H Kim, CH Choi, H Shin\*, SS Park\*. "Tailoring Electrochemical Water Oxidation Activity from the Isostructural Series of Alkaline-Stable Bimetallic Fe,Ni-Azolate Metal–Organic Frameworks". *Advanced Energy Materials, 14(31), 2401198*.
- G Kang, H Kim\*, H-K Lim\*. "Atomic-Level Insights into Defect-Driven Nitrogen Doping of Reduced Graphene Oxide". *Catalysts, 14(4), 242*.
- S-J Kim, S Lebègue\*, S Ringe\*, H Kim\*. "Elucidating Solvatochromic Shifts in Two-Dimensional Photocatalysts by Solving the Bethe–Salpeter Equation Coupled with Implicit Solvation Method". *Journal of Physical Chemistry Letters, 15(17), 4575-4580*.
- H Lee, MY Yang, JA Raskatov, H Kim, WA Goddard III\*. "Molecular Dynamics Studies of Atomistically Determined Fibrillar Assemblies: Comparison of the Rippled β-Sheet, Pleated β-Sheet, and Herringbone Structures". *Journal of Physical Chemistry Letters, 15(17), 4568-4574*.
- J Park, WJ Kim, YJ Kim\*, EK Lee\*, H Kim\*. "Threading Subunits for Polymers to Predict the Equilibrium Ensemble of Solid Polymer Electrolytes". *Journal of Physical Chemistry Letters, 15(5), 1227-1233*.
- J Koh, D Kim, SW Park,H Kim, K-H Hong\*, B Shin\*. "Selective Reactivity-Assisted Sacrificial Additive Coating for Surface Passivation of Wide Bandgap Perovskite Solar Cells with Cesium Tetrafluoroborate". *Journal of Materials Chemistry A, 12, 4290-4298*.
- J Lee, J Lee, X Jin, H Kim\*, S-J Hwang\*. "Atomically-Thin Holey 2D Nanosheets of Defect-Engineered MoN–Mo5N6 Composites as Effective Hybridization Matrices". *Small, 20(9), 2306781*.

**2023**

- S Park+, T Jang+, S Choi+, YH Lee, KH Cho, MY Lee, H Seo, HK Lim, Y Kim, J Ryu, SW Im, MG Kim, J-S Park, M Kim, K Jin, SH Kim, G-S Park, H Kim\*, KT Nam\*. "Iridium-Cooperated, Symmetry-Broken Manganese Oxide Nanocatalyst for Water Oxidation". *Journal of the American Chemical Society, 145, 49, 26632-26644*.
- L Zhuang, Y Xia, Q Zhang\*, H Kim. "Chemical Physics of Electrochemical Energy Materials". *Journal of Chemical Physics, 159, 190401 (Editorial)*.
- SW Park, JH Heo, HJ Lee, H Kim, SH Im\*, K-H Hong\*. "Compositional Design for High-Efficiency All-Inorganic Tin Halide Perovskite Solar Cells". *ACS Energy Letters, 8, 12, 5061-5069*.
- NH Kwon, J Park, X Jin, S-J Kim, H Kim\*, S-J Hwang\*. "Defect-Regulated Two-Dimensional Superlattice of Holey g-C3N4–TiO2 Nanohybrids: Contrasting Influence of Vacancy Content on Hybridization Impact and Photocatalyst Performance". *ACS Nano, 17, 23, 23732-23745*.
- G Bae, MM Kim, MH Han, J Cho, DH Kim, M-T Sougrati, J Kim, K-S Lee, SH Joo, WA Goddard III, H-S Oh\*, H Kim\*, F Jaouen\*, CH Choi\*. "Unravelling the Complex Causality Behind Fe–N–C Degradation in Fuel Cells". *Nature Catalysis, 6, 1140-1150*.
- H Lee, WA Goddard, JH Cha, WJ Choi\*, SH Noh\*, H Shin\*, H Kim\*. "Functional Group-Dependent Proton Conductivity of Phosphoric Acid-Doped Ion-Pair Coordinated Polymer Electrolytes: A Molecular Dynamics Study". *Journal of Physical Chemistry B, 127(41) 8993–8999*.
- C Zhang\*, J Cheng\*, Y Chen, M Chan, Q Cai, RP Carvalho, CFN Marchiori, D Brandell, CM Araujo, M Chen, X Ji, G Feng, K Goloviznina, A Serva, M Salanne, T Mandai, T Hosaka, M Alhanash, P Johansson, Y Qiu, H Xiao, MH Eikerling, R Jinnouchi, MM Melander, G Kastlunger, A Bouzid, A Pasquarello, S-J Shin, MM Kim, H Kim, K Schwarz, R Sundararaman. "2023 Roadmap on Molecular Modelling of Electrochemical Energy Materials / Chapter 13: Density functional theory in classical explicit solvents (DFT-CES): efforts towards understanding the unseen, buried electric double layer". *Journal of Physics: Energy, 5, 041501 (invited perspective)*.
- Y Baik+, M Kwen+, K Lee, S Chi, S Lee, K Cho, H Kim\*, M Choi\*. "Splitting of Hydrogen Atoms into Proton–Electron Pairs at BaO–Ru Interfaces for Promoting Ammonia Synthesis under Mild Conditions". *Journal of the American Chemical Society, 145(20), 11364–11374144*.
- DH Ryu, N Khan, J-G Park, D Paik, BJ Kang, NJ Jeon, S Lee, HK Lee, SK Lee, WS Shin, J-C Lee, H Kim\*, K-H Hong\*, SH Im\*, CE Song\*. "Morphology and Performance Enhancement through the Strong Passivation Effect of Amphoteric Ions in Tin-based Perovskite Solar Cells". *Small, 19(39), 2302418*.
- Y Ha, Y Son, D Paik, K-H Hong\*, H Kim\*. "Effect of Surface Termination on Carrier Dynamics of Metal Halide Perovskites: Ab Initio Quantum Dynamics Study". *Electronic Materials Letters, 19, 588-597*.
- H Oh+, S-J Shin+, E Choi, H Yamagishi, T Ohta, N Yabuuchi, H-G Jung, H Kim\*, HR Byon\*. "Anion-Induced Interfacial Liquid Layers on LiCoO2 in Salt-in-Water Lithium-Ion Batteries". *JACS Au, 3(5), 1392-1402*.
- S Chi, SG Ji, M Kim, H Kim, CH Choi\*, M Choi\*. "Structural Heterogeneity of Single-Atom Catalysts and True Active Site Generation via Ligand Exchange during Electrochemical H2O2 Production". *Journal of Catalysis, 419, 49-57*.
- J Park, H-S Lee, H Kim\*, J-M Choi\*. "Conformational Landscapes of Artificial Peptides Predicted by Various Force Fields: Are We Ready to Simulate β-Amino Acids?". *Physical Chemistry Chemical Physics, 25, 7466-7476*.
- J-H Yu, KP Singh, S-J Kim, T-H Kang, K-S Lee, H Kim, S Ringe\*, J-S Yu\*. "Active and Stable PtP2-based Electrocatalyst Solves the Phosphate Poisoning Issue of High Temperature Fuel Cell". *Journal of Materials Chemistry A, 11, 6413-6427*.

**2022**

- K Ahn, GH Kim, S-J Kim, J Kim, G-S Ryu, P Lee, B Ryu, JY Cho, Y-H Kim, J Kang, H Kim, Y-Y Noh\*, M-G Kim\*. "Highly Conductive p-Type Transparent Conducting Electrode with Sulfur-Doped Copper Iodide". *Chemistry of Materials, 34, 23, 10517–10527*.
- H Ahn, H Ahn, J An, H Kim\*, JW Hong\*, SW Han\*. "Role of Surface Strain at Nanocrystalline Pt{110} Facets in Oxygen Reduction Catalysis". *Nano Letters, 22, 22, 9115-9121*.
- D Shin, H Choi, J An, CH Sohn, CH Choi, H Shin\*, H Kim\*. "Enhanced Electroreduction of CO2 by Ni−N−C Catalysts from the Interplay Between Valency and Local Coordination Symmetry". *Journal of Materials Chemistry A, 10, 22523-22530*.
- M Kim, S-J Shin, J Lee, Y Park, Y Kim, H Kim\*, JW Choi\*. "Cationic Additive with a Rigid Solvation Shell for High-Performance Zinc Ion Batteries". *Angewandte Chemie, 61, 47, e202211589*.
- S-J Shin, H Choi, S Ringe, DH Won, H-S Oh, DH Kim, T Lee, D-H Nam, H Kim\*, CH Choi\*. "A Unifying Mechanism for Cation Effect Modulating C1 and C2 Productions from CO2 Electroreduction". *Nature Communications, 13, 5482*.
- J Park, E Park, SQ Choi, J Wu, J Park, H Lee, H Kim, Haeshin Lee\*, Myungeun Seo\*. "Biodegradable Block Copolymer–Tannic Acid Glue". *JACS Au, 2, 9, 1978-1988*.
- D Paik, H Lee, H Kim\*, J-M Choi\*. "Thermodynamics of π–π Interactions of Benzene and Phenol in Water". *International Journal of Molecular Science, 23, 17, 9811*.
- S-J Kim, S Lebègue, S Ringe\*, H Kim\*. "GW Quasiparticle Energies and Bandgaps of Two-Dimensional Materials Immersed in Water". *Journal of Physical Chemistry Letters, 13, 32, 7574-7582*.
- S Lee, H Kim, R Ryoo, JY Park, M Choi\*. "Hydrogen Spillover in Nonreducible Oxides: Mechanism and Catalytic Utilization". *Nano Research, 15, 10357-10365*.
- JH Cho, Y Ha, A Cho, J Park, J Choi, Y Won, H Kim\*, BM Kim\*. "A Bimetallic PdCu–Fe3O4 Catalyst with an Optimal d-band Centre for Selective N-methylation of Aromatic Amines with Methanol". *Catalysis Science and Technology, 12, 3524-3533*.
- S Sultan+, H Lee+, S Park+, MM Kim+, A Yoon, H Choi, T-H Kong, Y-J Koe, H-S Oh, Z Lee\*, H Kim\*, W Kim\*, Y Kwon\*. "Interface Rich CuO/Al2CuO4 Surface for Selective Ethylene Production from Electrochemical CO2 conversion". *Energy Environmental Science, 15, 2397-2409*.
- K-H Kim, S-J Kim, WH Choi, H Lee, BC Moon, GH Kim, JW Choi, DG Park, JH Choi, H Kim\*, JK Kang\*. "Triphasic Metal Oxide Photocatalyst for Reaction Site-Specific Production of Hydrogen Peroxide from Oxygen Reduction and Water Oxidation". *Advanced Energy Materials, 12, 18, 2104052*.
- T Jang+, D Paik+, S-J Shin, H Kim\*. "Density Functional Theory in Classical Explicit Solvents: Mean-field QM/MM Method for Simulating Solid–liquid Interfaces". *Bulletin of the Korean Chemical Society, 43, 4, 476-483*.
- B-H Lee+, E Gong+, M Kim+, S Park, HR Kim, J Lee, E Jung, CW Lee, J Bok, Y Jung, YS Kim, K-S Lee, S-P Cho, J-W Jung, C-H Cho, S Lebègue, KT Nam, H Kim\*, S-I In\*, T Hyeon\*. "Electronic Interaction Between Transition Metal Single-atoms and Anatase TiO2 Boosts CO2 Photoreduction with H2O". *Energy Environmental Science, 15, 601-609*.
- S-J Shin+, DH Kim+, G Bae+, S Ringe, H Choi, H-K Lim, CH Choi\*, H Kim\*. "On the Importance of the Electric Double Layer Structure in Aqueous Electrocatalysis". *Nature Communications, 13, 174*.
- Y Ha, J-G Park, K-H Hong\*, H Kim\*. "Enhanced Light Emission through Symmetry Engineering of Halide Perovskites". *Journal of the American Chemical Society, 144, 1, 297-305*.
- NH Kwon, X Jin, S-J Kim, H Kim\*, S-J Hwang\*. "Multilayer Conductive Hybrid Nanosheets as Versatile Hybridization Matrices for Optimizing the Defect Structure, Structural Ordering, and Energy-Functionality of Nanostructured Materials". *Advanced Science, 9, 2, 213042*.

**2021**

- SR Shin, HS Cho, Y Lee, S Gim, YM Jung, H Kim, O Terasaki, JK Kang\*. "In Situ Mapping and Local Negative Uptake Behavior of Adsorbates in Individual Pores of Metal–Organic Frameworks". *Journal of the American Chemical Society, 143, 49, 20747–20757*.
- AC Kathalikkattil, Y Gu, JF Kurisingal, H Lee, H Kim, Y Choe, D-W Park\*. "A Catalytic Approach of Blending CO2-activating MOF Struts for Cycloaddition Reaction in a Helically Interlaced Cu(II) Amino Acid Imidazolate Framework: DFT-corroborated Investigation". *Research on Chemical Intermediates, 47, 3979-3997*.
- JH Kim+, D Shin+, J Kim+, JS Lim, VK Paidi, TJ Shin, HY Jeong, K-S Lee\*, H Kim\*, SH Joo\*. "Reversible Ligand Exchange in Atomically Dispersed Catalysts for Modulating the Activity and Selectivity of Oxygen Reduction Reaction". *Angewandte Chemie, 60, 37, 20528-20534*.
- M Lyu, S Park, H Lee, BS Ma, SH Park, K-H Hong, H Kim, T-S Kim, JH Noh, HJ Son\*, N-G Park\*. "Simultaneous Enhanced Efficiency and Stability of Perovskite Solar Cells Using Adhesive Fluorinated Polymer Interfacial Material". *ACS Applied Materials & Interfaces, 13(30), 35595-35605*.
- S-J Kim, S Lebègue, H Kim\*, WJ Kim\*. "Assessment and Prediction of Band Edge Locations of Nitrides using a Self-Consistent Hybrid Functional". *Journal of Chemical Physics, 155, 024120*.
- HS Cho,\* H Tanaka, Y Lee, Y-B Zhang, J Jiang, M Kim, H Kim, JK Kang, O Terasaki. "Physicochemical Understanding of the Impact of Pore Environment and Species of Adsorbates on Adsorption Behaviour". *Angewandte Chemie, 60, 37, 20504-20510*.
- AC Kathalikkattil, Y Gu, JF Kurisingal, H Lee, H Kim, Y Choe, D-W Park\*. "Three-dimensional Amino Acid Backbone Cu-aspartate Metal–Organic Framework as a Catalyst for the Cycloaddition of Propylene Oxide and CO2". *Reaction Kinetics, Mechanisms and Catalysis, 133, 425-439*.
- N Kim+, T-H Gu+, D Shin+, X Jin, H Shin, MG Kim, H Kim\*, S-J Hwang\*. "Lattice Engineering to Simultaneously Control the Defect/Stacking Structures of Layered Double Hydroxide Nanosheets to Optimize Their Energy Functionalities". *ACS Nano, 15(5), 8306-8318*.
- Y Lee, H Kim, K-H Hong\*, K Cho\*. "Femtosecond Quantum Dynamics of Excited-State Evolution of Halide Perovskites: Quantum Chaos of Molecular Cations". *Journal of Physical Chemistry C, 125(19), 10676-10684*.
- K Hyun, Y Park, S Lee, J Lee, Y Choi, S-J Shin, H Kim, M Choi\*. "Tailoring Dynamic Metal‐Polymer Interaction to Improve Catalyst Selectivity and Longevity in Hydrogenation". *Angewandte Chemie, 60(22), 12482-12489*.
- DH Kim+, S Ringe+, H Kim, S Kim, B Kim, G Bae, H-S Oh, F Jaouen, W Kim\*, H Kim\*, CH Choi\*. "Selective Electrochemical Reduction of Nitric Oxide to Hydroxylamine by Atomically Dispersed Iron Catalyst". *Nature Communications, 12, 1856*.
- J Wang\*, S-J Kim, J Liu, Y Gao, S Choi, J Han, H Shin, S Jo, J Kim, F Ciucci, H Kim, Q Li, W Yang, X Long, S Yang,\* S-P Cho, KH Chae, MG Kim, H Kim\*, J Lim\*. "Redirecting Dynamic Surface Restructuring of a Layered Transition Metal Oxide Catalyst for Superior Water Oxidation". *Nature Catalysis, 4, 212-222*.
- JS Oh+, KY Kim+, J Park, H Lee, Y Park, J Cho, SS Lee, H Kim\*, SH Jung\*, JH Jung\*. "Dynamic Transformation of a Ag+-Coordinated Supramolecular Nanostructure from a 1D Needle to a 1D Helical Tube via a 2D Ribbon Accompanying the Conversion of Complex Structures". *Journal of the American Chemical Society, 143(8), 3113-3123*.
- H Kim+, D Shin+, W Yang+, DH Won+, H-S Oh, MW Chung, D Jeong, SH Kim, KH Chae, JY Ryu, J Lee, SJ Cho, J Seo\*, H Kim\*, CH Choi\*. "Identification of Single-Atom Ni Site Active toward Electrochemical CO2 Conversion to CO". *Journal of the American Chemical Society, 143 (2), 925-933*.

## 수상

2021년 10월 13일–2026년 10월 13일 범위의 교수 수상이다.[^professor]

- 2024 · 김형준 · Pople medal, Asia-Pacific Association of Theoretical and Computational Chemistry

## 연락과 위치

연구실 안내 주소는 KAIST 화학과 N5-2146, 대전광역시 유성구 대학로 291이며 전화는 042-350-2876이다.[^home] 교수 소개 쪽은 연구실과 별도로 Office를 기초과학동 E6-6 #203, 전화는 042-350-2836으로 적는다.[^professor]

## 각주
[^home]: M-design Laboratory, Home. <https://www.m-design-lab.net> (관측 2026-11-01).
[^faculty]: KAIST 화학과 교수진 목록, 김형준(Kim, Hyungjun), 교수, m-Design-Lab. <https://chem.kaist.ac.kr/faculty> (관측 2026-11-01).
[^research]: M-design Laboratory, Research. <https://www.m-design-lab.net/research> (관측 2026-11-01).
[^dft]: M-design Laboratory, DFT-CES. <https://www.m-design-lab.net/dft-ces> (관측 2026-11-01).
[^umbd]: M-design Laboratory, uMBD. <https://www.m-design-lab.net/umbd> (관측 2026-11-01).
[^catalysts]: M-design Laboratory, Catalysts. <https://www.m-design-lab.net/catalysts> (관측 2026-11-01).
[^photo]: M-design Laboratory, Photoactive. <https://www.m-design-lab.net/photoactive> (관측 2026-11-01).
[^software]: M-design Laboratory, Softwares. <https://www.m-design-lab.net/softwares> (관측 2026-11-01).
[^members]: M-design Laboratory, Members. <https://www.m-design-lab.net/members> (관측 2026-11-01).
[^alumni]: M-design Laboratory, Alumni. <https://www.m-design-lab.net/alumni> (관측 2026-11-05).
[^pubs]: M-design Laboratory, Publications, Journals. <https://www.m-design-lab.net/publications> (관측 2026-11-01).
[^professor]: M-design Laboratory, Principal Investigator, Hyungjun Kim. <https://www.m-design-lab.net/professor> (관측 2026-11-05).
[^p1]: T. Jang 외, H. Kim, JACS Au 5, 2047-2058 (온라인 2025-04-12). <https://doi.org/10.1021/jacsau.5c00176> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p2]: M. M. Kim 외, H. Kim, Nature Communications 17, 3645 (온라인 2026-03-07). <https://doi.org/10.1038/s41467-026-70322-5> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p3]: S. G. Ji 외, C. H. Choi, Nature Catalysis 7, 1330-1338 (온라인 2024-12-20). <https://doi.org/10.1038/s41929-024-01241-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p4]: S.-J. Kim, S. Lebègue, S. Ringe, H. Kim, The Journal of Physical Chemistry Letters 15, 4575-4580 (온라인 2024-04-19). <https://doi.org/10.1021/acs.jpclett.4c00752> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p5]: Y. Son, Y. Choi, O. V. Prezhdo, H. Kim, Journal of Chemical Theory and Computation 21, 9772-9783 (온라인 2025-10-02). <https://doi.org/10.1021/acs.jctc.5c01001> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p6]: S.-J. Kim 외, H. Kim, Journal of the American Chemical Society 146, 26000-26007 (온라인 2024-09-12). <https://doi.org/10.1021/jacs.4c05159> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/smll.202401480|10.1007/s13391-023-00428-1|10.1021/acs.jcim.5c00342|10.1021/acs.jctc.5c01001|10.1021/acs.jpclett.4c00752|10.1021/acssynbio.1c00074|10.1021/jacs.4c05159|10.1021/jacsau.5c00176|10.1038/s41467-026-70322-5|10.1038/s41929-024-01241-1> (관측 2026-11-05).
[^p7]: H. T. Jung 외, C. Kim, Journal of Chemical Physics 164, 094103 (2026). <https://doi.org/10.1063/5.0306932> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.15329> (관측 2026-11-05).

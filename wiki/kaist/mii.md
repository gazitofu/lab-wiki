# Materials Imaging & Integration Lab (MII Lab)

**KAIST 신소재공학과 · 홍승범 교수**

- 분야: 원자간력 현미경(AFM) 기반 나노 영상과 물성 분석, AI·기계학습 소재 정보학, 이차전지 전극·계면의 이온·전자 거동 영상, 강유전체·압전 소재의 분극 영상, 생체 소재
- 대분야: 소재, 컴퓨팅·AI
- 태그: 강유전체[^pol][^p6][^p8], 이차전지 소재[^ionics][^p4][^p5], 과학·공학 AI[^ai][^p1][^p3], 생체재료·조직 공학[^pol][^home][^mse], 압전 소재·소자[^pol], 원자간력 현미경·주사 탐침 계측[^p7]
- 홈페이지: <https://mii.kaist.ac.kr/>
- 근거와 출처: [MII Lab 근거 페이지](mii-sources.md)

> 소재 영상(materials imaging)으로 「구조–물성 관계」를 밝히고 소재 통합(materials integration)으로 「소재 설계」를 한다고 소개하는 신소재공학과 연구실이다.[^home] 원자간력 현미경 기반 나노 영상·물성 분석과 AI·기계학습 기반 소재 정보학, 합성·공정 최적화를 묶어 배터리, 강유전·압전 메모리, 바이오 소재의 구조–물성 관계를 연구한다.[^mse]

## 무엇을 연구하나

연구실은 KAIST 신소재공학과 홍승범 교수의 연구실이다. 누리집 제목은 「KAIST MII LAB」이고, Contact 페이지는 연구실을 Materials Imaging and Integration Lab으로, 신소재공학과 연구실 소개 페이지는 영문 연구실 명칭을 Materials Imaging & Integration (MII) Lab.으로 적는다.[^home][^contact][^mse]

누리집 첫 화면은 연구실을 소재 영상으로 「구조–물성 관계(structure-property relationship, 소재의 원자·미세 구조와 그 소재가 보이는 성질 사이의 관계)」를 다루고 소재 통합으로 「소재 설계(materials design)」를 하는 곳으로 소개한다.[^home] 첫 화면은 응용(APPLICATIONS)으로 배터리(Battery, 전기·기계적 분석과 특성 평가), 메모리(Memory, 압전체와 강유전체), 바이오(Bio, 구조·기능성 생체 소재)를, 도구(TOOLS)로 AI/ML(소재 정보학), AFM(영상과 물성 분석), 합성(Synthesis, 공정과 최적화)을 든다.[^home]

신소재공학과 연구실 소개 페이지는 연구실을 원자간력현미경 기반 나노이미징·물성 분석과 AI/ML 기반 소재정보학, 합성·공정 최적화를 통합해 배터리, 강유전·압전 메모리, 바이오 소재의 구조–물성 관계를 규명하고 기능성 소재 설계를 하는 연구실로 소개한다.[^mse] 핵심어로는 원자현미경(AFM), 강유전체, 압전소재, 배터리 이미징, AI/ML을 단다.[^mse] 원자간력 현미경(atomic force microscope, AFM)은 끝이 뾰족한 탐침으로 시료 표면을 훑으며 탐침과 표면 사이에 작용하는 힘을 재어 표면의 높낮이와 성질을 영상으로 얻는 현미경이다. 강유전체(ferroelectric)는 전기장을 걸지 않아도 전기 분극이 남아 있고 그 방향을 전기장으로 뒤집을 수 있는 물질이고, 압전 소재(piezoelectric material)는 힘을 받으면 전기 분극이 생기고 전기장을 걸면 모양이 바뀌는 소재다.

누리집 Research 메뉴는 연구를 AI Materials Informatics, Ionics, Polarization의 세 갈래와 Research Projects로 나눈다.[^ai][^ionics][^pol][^projects]

## 주요 연구 주제

### 1. AI 소재 정보학

AI Materials Informatics 페이지는 기계학습(machine learning, ML) 모델로 리튬이온 전지 양극재(cathode material, 전지의 양극을 이루는 소재) 합성을 최적화해 방전 용량을 높이고 리튬이온 전지의 조성과 충방전 상태를 예측하는 것, 그리고 계산으로 만든 자료를 분석하도록 학습한 합성곱 신경망(convolutional neural network, CNN, 영상처럼 격자 모양으로 놓인 자료에서 작은 필터를 옮겨 가며 특징을 뽑아내는 신경망)이 실험 소재 자료를 예측할 수 있음을 보이는 것을 목표로 적는다.[^ai] 방법으로는 역설계(inverse design, 원하는 성질을 먼저 정하고 그 성질을 내는 소재나 조건을 거꾸로 찾는 설계)와 기계학습 모델을 묶어 양극재의 최적 합성 조건을 예측하고, 상장 모사(phase field simulation, 서로 다른 상의 경계를 연속적으로 변하는 변수로 나타내 미세 구조의 변화를 계산하는 방법)로 만든 영상으로 CNN을 학습시켜 실험으로 얻은 미세 구조 영상을 분할(segmentation, 영상의 각 화소가 어느 영역에 속하는지 나누는 처리)하며, 주사 전자 현미경(scanning electron microscope, SEM, 전자빔으로 시료 표면을 훑어 표면 영상을 얻는 현미경) 영상으로 학습한 CNN으로 양극재의 조성과 충방전 상태를 분류한다고 적는다.[^ai] 기대 효과로는 기존 시행착오 방식에 대한 의존을 줄인 고에너지 밀도 양극재의 발견과 최적화, 손으로 하는 분할 작업에 대한 의존 감소, 사람에 기대는 분석을 줄인 전지 생산·개발 효율 향상을 들고, 관련 코드는 GitHub 저장소에 정리해 두었다고 밝힌다.[^ai] 같은 페이지는 다중 규모의 「구조–물성」 관계와 「공정–물성」 관계를 하나로 잇는 것을 목표로 하는 M3I3(Materials and Molecular Modeling, Imaging, Informatics, and Integration) 프로젝트도 소개한다.[^ai]

대표 논문 1은 SEM 영상으로 학습한 CNN으로 리튬이온 전지 NCM 양극재의 주요 조성과 충방전 상태를 분류했다.[^p1] 대표 논문 2는 문헌 자료의 빈칸을 대체값 추정(imputation, 비어 있는 자료 값을 다른 값들로부터 추정해 채우는 방법)으로 채운 뒤, 리튬 과잉 NCM 양극재의 1차 입자 크기를 불확실성과 함께 예측하는 모델을 만들었다.[^p2] 대표 논문 3은 밀도범함수 이론(density functional theory, DFT, 전자의 밀도로 물질의 에너지와 성질을 계산하는 양자역학 계산법)으로 계산한 생성 에너지를 써서 화합물이 녹을 때 같은 조성의 액체가 되는지(조화 용융, congruent melting)를 예측하는 기계학습 모델을 만들었다.[^p3] 누리집 Journals 목록에는 이 밖에도 기계학습을 이용한 리튬이온 전지 양극재 합성(Nano Energy 2022), 상장 모사로 학습한 CNN의 실험 자료 분할(Acta Materialia 2021), 3차원 CNN을 이용한 단층 촬영 자료 분할(Computational Materials Science 2023), 소재·분자 모델링, 영상, 정보학, 통합으로 발견 시간을 줄이는 방법을 다룬 ACS Nano 2021 논문, 소재의 발견·개발·최적화를 위한 인공지능을 다룬 ACS Nano 2025 논문, 그래프 신경망을 이용한 NASICON형 전극의 자료 기반 설계(Batteries & Supercaps 2024)를 제목에 단 논문이 있다.[^pubs] 누리집 News 페이지는 2025년 4월 이차전지 기계학습 데이터셋의 공개와 2025년 10월 연구실의 「AI for Material Discovery」 기술의 리튬 금속 전지 기업 이전을 알린다.[^news]

### 2. 이온·배터리 소재 영상

Ionics 페이지는 이온·전자 성질을 이해하고 그 기전을 밝히는 것, 그리고 배터리 소재에서 일어나는 전기화학 현상을 나노·마이크로미터 규모에서 관찰하고 시각화해 전극 전체 규모의 분석 결과와 잇는 것을 목표로 적는다.[^ionics] 방법으로는 충방전 동안 전극 표면의 변화를 현장 전기화학 원자간력 현미경(in-situ EC-AFM, 전해질 속에서 전기화학 반응이 일어나는 동안 전극 표면을 원자간력 현미경으로 관찰하는 방법)으로 시각화하고, 여러 환경 조건에서 만든 고체 전해질 계면(solid electrolyte interphase, SEI, 충방전 중 전해질이 분해되어 전극 표면에 생기는 막)의 성질을 원자간력 현미경으로 평가하며, 깊이 분석(depth profiling, 표면에서 안쪽으로 들어가며 깊이에 따른 성분이나 성질을 재는 분석)으로 배터리 소재를 표면에서 구분하고 3차원으로 영상화한다고 적는다.[^ionics] 이차전지 계에 여러 원자간력 현미경 측정 방식을 적용한 독창적인 분석 방법과 전극·전해질 조합의 발전을 기대 효과로 든다.[^ionics] 페이지의 연구 사례는 켈빈 탐침 힘 현미경(Kelvin probe force microscopy, KPFM, 탐침과 시료 사이의 접촉 전위차를 재어 표면 전위나 일함수의 분포를 영상으로 얻는 방법)으로 SiO·흑연 복합 음극의 리튬화 자리를 시각화한 사례, 원자간력 현미경의 나노 압입 방식으로 확인한 SEI의 다층 구조, 전기화학 변형 현미경(electrochemical strain microscopy, ESM, 탐침으로 교류 전압을 걸 때 이온 이동에 따라 생기는 표면 변형을 재어 이온의 움직임을 영상으로 얻는 방법) 신호와 마찰력 신호의 상관, ESM 영상과 전도성 원자간력 현미경(conductive AFM, C-AFM, 전압을 건 탐침으로 표면을 훑으며 흐르는 전류를 재어 전기 전도의 분포를 영상으로 얻는 방법) 영상의 비교다.[^ionics]

대표 논문 4는 표면 모양이 C-AFM 영상에 만드는 허상(artifact, 측정 대상이 아닌 원인으로 생긴 거짓 신호)의 원인을 통계 방법으로 밝히고 시료 표면을 연마해 이를 줄인 뒤, 실리콘 산화물(SiO)·흑연 복합 음극에서 전자가 흐르는 길을 관찰했다.[^p4] 대표 논문 5는 ESM의 한 방식(DART-ESM)에서 되먹임 회로의 지연이 접촉 강성을 바꿔 생기는 표면 모양 혼신(topographic crosstalk, 표면의 높낮이가 측정 신호에 섞여 드는 현상)을 이온이 움직이지 않는 단결정 실리콘을 기준 시료로 정량 분석했다.[^p5] 누리집 Journals 목록에는 이 밖에도 단일벽 탄소나노튜브로 얻는 고른 리튬화(ACS Energy Letters 2023), 리튬 금속 음극의 선택적 리튬 도금과 탈리(ACS Energy Letters 2026), 광학 현미경 실시간 관찰과 현장 전기화학 원자간력 현미경을 묶은 리튬 금속 음극 표면 변화의 다중 규모 영상법(Advanced Materials Interfaces 2026), 고체 전해질의 리튬 이온 농도와 확산 계수의 정량 측정(ACS Applied Energy Materials 2021), 배터리 소재의 다중 규모 영상과 분광을 다룬 EcoMat 2025 논문이 있다.[^pubs] Research Projects 페이지의 과제에는 소듐 이온 배터리 소재 분석 기법, 리튬 이차전지 설계 인공지능 플랫폼, 원자간력 현미경 영상 기반 전극 표면의 젖음성과 표면 에너지 분석, 반도체–이차전지 인터페이싱 분석·평가 플랫폼이 있다.[^projects]

### 3. 분극·강유전체 영상과 압전 소재

Polarization 페이지는 강유전·압전 성질을 이해하고 그 기전을 밝히는 것, 그리고 원자간력 현미경 기법으로 강유전·압전 도메인(domain, 분극 방향이 같은 영역)과 구조, 성질을 시각화하고 평가하는 것을 목표로 적는다.[^pol] 방법으로는 현장 압전 응답 힘 현미경(piezoresponse force microscopy, PFM, 탐침으로 교류 전압을 걸 때 압전 효과로 생기는 표면 변형을 재어 분극 방향과 도메인을 영상으로 얻는 방법), 각도 분해 PFM, 전하 구배 현미경(charge gradient microscopy, CGM, 탐침이 표면을 훑을 때 표면 전하에서 흘러나오는 전류를 재어 도메인을 영상으로 얻는 방법)으로 분극이 뒤집히는 과정을 시각화해 그 기전을 연구하고, 혼성 구조와 새로운 제작 기법, 최적화 전략으로 압전 소재의 에너지 성능을 높이며, 세라믹(PZT, BaTiO3, ZnO, KNN)과 고분자(PVDF, PVDF-TrFE, PVDF-TrFE-CFE)를 아우르는 여러 압전 소재를 다룬다고 적는다.[^pol] 기대 효과로는 고성능 센서, 구동기, 에너지 하베스터, 생체 의료 기기 개발과 다강체(multiferroics, 강유전성·강자성처럼 외부 장으로 방향을 바꿀 수 있는 질서를 둘 이상 함께 가진 물질) 연구의 발전을 든다.[^pol] 페이지의 연구 사례는 단일 주파수 수직 PFM의 측정 원리, 비대칭 마찰을 이용한 새 패터닝 기술(분극 유도 리소그래피로 만든 3차원 나노 구조), 3차원 ZnO 나노 트러스 구조의 제작, 하이드록시아파타이트를 넣은 생체 모사 지지체로 뼈 재생을 높이는 지지체 설계다.[^pol]

대표 논문 6은 강유전체의 위아래 두 방향 도메인이 마찰과 마모에서 서로 다르게 반응함을 보이고, 이를 마스크로 써서 3차원 나노 구조를 만들었다.[^p6] 대표 논문 7은 탐침과 강유전체 표면 사이의 유전 간극(dielectric gap)이 PFM으로 잰 항전압(coercive voltage, 분극을 뒤집는 데 필요한 전압)에 미치는 영향을 밝혔다.[^p7] 대표 논문 8은 하부 전극과 열처리가 10 nm 두께 하프늄·지르코늄 산화물(Hf0.5Zr0.5O2) 축전기의 분극 반전을 어떻게 바꾸는지를 결정립 규모에서 밝혔다.[^p8] 누리집 Journals 목록에는 이 밖에도 강유전체 도메인의 나노 규모 마찰 영상(Science Advances 2026), 전도성 원자간력 현미경 단층 촬영으로 본 이산화타이타늄(TiO2) 속 전도 필라멘트의 3차원 시각화(Nano Letters 2026), 다결정 PZT 박막에서 결정립계가 매개하는 도메인 생성과 성장의 시각화(APL Materials 2025), P(VDF-TrFE)와 그 복합재의 압전 응답을 높이는 상(phase) 공학(Advanced Materials Interfaces 2025), 단일 주파수 수직 PFM(Journal of Applied Physics 2021), 측면 PFM의 대비 원리 재검토(Journal of Applied Physics 2023), 강유전체 연구와 여러 분야의 소재 연구를 위한 원자간력 현미경을 다룬 논문(Journal of Materials Chemistry C 2026, Small Methods 2025)이 있다.[^pubs] 생체 소재 쪽으로는 압전성과 표면 형상을 설계한 뼈 재생 지지체(ACS Applied Materials & Interfaces 2024), PFM으로 본 소결 하이드록시아파타이트의 표면 전하 효과(Journal of Applied Physics 2021), 알츠하이머병 관련 아밀로이드 베타(Aβ) 응집체의 측면 압전성(Advanced Science 2024)을 제목에 단 논문이 있다.[^pubs]

## 대표 논문

홍승범 교수가 저자인 2021–2026년 논문 가운데 세 연구 갈래(AI 소재 정보학, 이온·배터리 소재 영상, 분극·강유전체 영상)에서 초록을 확인할 수 있는 여덟 편을 골랐다. 여덟 편 모두 교수가 마지막 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [Composition and state prediction of lithium-ion cathode via convolutional neural network trained on scanning electron microscopy images](https://doi.org/10.1038/s41524-024-01279-6) · npj Computational Materials 10 | 전기차와 에너지 저장 장치에 쓸 안전하고 에너지 밀도가 높은 리튬이온 전지를 빨리 개발하려면 많은 소재를 빠르게 다루는 연구가 필요하다. 이 논문은 주사 전자 현미경 영상으로 학습한 CNN으로 여러 Li(Ni, Co, Mn)O2(NCM) 양극재의 주요 조성(333, 523, 622, 811)과 상태(처음 상태, 사전 충방전 상태, 100회 충방전 상태)를 분류하는 예측 모델을 만들었다. 학습한 모델은 시험 자료 3840개에서 99.6%의 정확도를 보였고, 기능성 전해질 첨가제를 쓴 NCM 양극재처럼 학습하지 않은 영상 자료에도 적용할 수 있었다.[^p1] | 1저자 Jimin Oh, 마지막 저자 홍승범 (7명) |
| 2 | 2025 | [Uncertainty-Quantified Primary Particle Size Prediction in Li-Rich NCM Materials via Machine Learning and Chemistry-Aware Imputation](https://doi.org/10.1002/advs.202515694) · Advanced Science 13 | 리튬 과잉 NCM 양극재는 1차 입자 크기에 따라 전기화학 성능이 달라지는데, 문헌 자료에 빈칸이 많아 기계학습으로 입자 크기를 예측하기 어려웠다. 이 논문은 MatImpute, K-최근접 이웃, 연쇄 방정식 다중 대체, 평균 대체로 자료의 빈칸을 채운 뒤 NGBoost(예측값과 함께 그 불확실성을 내는 부스팅 모델)로 1차 입자 크기를 불확실성과 함께 예측했다. MatImpute 기반 NGBoost 모델이 시험 자료에서 결정계수(R2) 0.866, 보정 오차 0.133으로 가장 정확했다. 특성 분석에서는 2차 소결 온도와 1차 소결 시간이 주된 요인이고 조성의 영향은 미미했다. 실험 검증에서 대부분의 예측이 측정값과 0.13 µm 안에서 맞았고, 정규화한 불확실성은 1.5 가까이였다. 리튬 과잉 NCM 소재의 미세 구조 변화는 화학량론 조성이 아니라 소결 조건이 좌우함을 확인했다.[^p2] | 1저자 Benediktus Madika, 마지막 저자 홍승범 (7명) |
| 3 | 2025 | [Machine learning-based melting congruency prediction of binary compounds using density functional theory-calculated formation energy](https://doi.org/10.1063/5.0247514) · APL Machine Learning 3 | 밀도범함수 이론으로 계산한 생성 에너지와 실험으로 얻은 용융 반응 자료를 함께 써서, 화합물이 녹을 때 같은 조성의 액체가 되는지를 예측하는 기계학습 모델을 만들었다. 시험한 여러 모델 가운데 XGBoost 모델이 가장 알맞아, 표지를 단 화합물 자료로 이 모델을 학습시켰다. 학습한 모델에서 뽑은 특성 중요도를 비교한 결과, 화합물 조성에서 DFT 볼록 껍질(convex hull, 조성별로 가장 안정한 상의 에너지를 이은 선)의 기울기 변화인 「볼록 껍질 날카로움」이 다른 특성보다 크게 중요했다. 이 방법은 합금 공정 설계에 쓰일 수 있고 더 복잡한 다원계 합금에도 적용할 수 있다.[^p3] | 1저자 Youngwoo Choi, 마지막 저자 홍승범 (3명) |
| 4 | 2022 | [Nanoscale Visualization of the Electron Conduction Channel in the SiO/Graphite Composite Anode](https://doi.org/10.1021/acsami.2c01460) · ACS Applied Materials & Interfaces 14 | C-AFM은 시료 표면의 전자 전도도를 나노미터 공간 해상도로 재는 데 널리 쓰이지만, 허상이 생기는 원인은 많이 연구되지 않아 영상 결과를 정확하게 해석하기 어려웠다. 이 논문은 허상 없는 C-AFM으로 실리콘 기반 복합 음극의 전자 전도 통로를 관찰했다. 표면 모양 때문에 생기는 대표적인 허상의 원인을, 영상마다 허상의 기여를 시각화하는 통계 방법으로 조사했다. 냉각 단면 연마기로 시료 표면을 연마해 허상을 줄였고, 피어슨 상관 분석으로 이를 확인했다. 허상 없는 영상으로 도전재로 단일벽 탄소나노튜브를 쓴 복합 음극과 카본 블랙을 쓴 복합 음극의 충방전 전후 전류 신호를 비교했고, 도전재에 따른 활물질의 전기적 열화와 형태 변화의 관계로 단일벽 탄소나노튜브를 넣은 전극의 전기적·전기화학적 성질 개선을 설명했다.[^p4] | 1저자 Gun Park, 마지막 저자 홍승범 (5명) |
| 5 | 2026 | [Quantitative Analysis of Topographic Crosstalk in DART-ESM Arising from Feedback-Loop-Delay-Induced Contact Stiffness Variations in Battery Materials](https://doi.org/10.1002/smtd.70763) · Small Methods 10 | ESM은 배터리 소재, 특히 이온 수송이 국소적으로 일어난다고 여겨지는 결정립계에서 나노 규모 이온 움직임을 재는 데 널리 쓰이지만, 표면 모양 때문에 측정 응답이 부풀려질 수 있어 신호 해석이 어렵다. 이 논문은 이중 교류 공진 추적(DART) 방식 ESM에서 되먹임 회로의 지연이 접촉 강성을 바꿔 생기는 표면 모양 혼신을, 이온이 움직이지 않는 단결정 실리콘을 기준 시료로 정량 분석했다. 배터리 전극과 고체 전해질에서 흔히 보는 결정립계 같은 모양을 흉내 내도록 인공 홈 구조를 만들었고, 접촉 공진을 단순 조화 진동자로 분석해 ESM 진폭의 증가가 이온 움직임과 관계없이 접촉 강성의 변화에서 생길 수 있음을 보였다. 여러 실리콘 보정 시료에서 재현성을 확인하고 흑연 음극과 Na2Zn2TeO6(NZTO) 고체 전해질에서도 검증해, 이런 허상이 실제 측정 조건의 DART-ESM에 본래 따른다는 것을 보였다. 냉각 단면 연마로 표면 거칠기를 줄이고 접촉 공진을 안정시켜 허상을 효과적으로 줄였다.[^p5] | 1저자 Dongyan Chen, 마지막 저자 홍승범 (10명) |
| 6 | 2024 | [Switchable tribology of ferroelectrics](https://doi.org/10.1038/s41467-023-44346-0) · Nature Communications 15 | 강유전체의 마찰학적 성질(마찰과 마모의 성질)을 바꿀 수 있다면 강유전체 도메인을 시각화하고 제어하는 다른 길이 된다. 이 논문은 나노 규모 주사 탐침으로 강유전체의 마찰과 마모가 분극 방향에 따라 바뀌는 것을 관찰했다. 아래 방향 도메인은 위 방향 도메인보다 마찰 계수가 낮고 마모가 느려 스마트 마스크로 쓸 수 있다. 이 비대칭은 충분히 큰 접촉력에서 휨 전기 효과(flexoelectricity, 위치에 따라 달라지는 변형의 기울기에 따라 분극이 생기는 효과)로 결합된 분극에서 생기며, 화학 조성과 결정 대칭이 다른 여러 강유전체에 널리 나타났다. 도메인을 움직이는 스마트 마스크로 여러 차례 패터닝해 위아래 도메인의 마모 속도 차이를 이용한 3차원 나노 구조를 만들었고, 이 방법은 기술적으로 쓸 만한 mm–cm 크기로 넓힐 수 있다고 제시했다. 강유전체가 나노 규모에서 전기로 조절할 수 있는 마찰학적 소재임을 보였다.[^p6] | 1저자 Seongwoo Cho, 마지막 저자 홍승범 (14명) |
| 7 | 2024 | [Unveiling the Nanoscale Dielectric Gap and Its Influence on Ferroelectric Polarization Switching in Scanning Probe Microscopy](https://doi.org/10.1002/adfm.202406944) · Advanced Functional Materials 35 | 주사 탐침 현미경의 탐침과 강유전체 표면 사이에 있는 유전 간극을 C-AFM과 PFM으로 조사했다. 이 간극은 유전체 층으로 작용하지만, 반지름 25 nm 탐침에 0.5 V를 걸고 10–20 µN 사이의 임계 하중을 주면 터널링 전류가 흘러 강유전체에 전하를 넣을 수 있었다. 압전 응답 이력 곡선으로 잰 항전압은 유전 간극의 유전율이 정했다. 공기 중에서 잰 항전압은 같은 물질을 축전기로 잰 값보다 훨씬 크게 나오곤 하는데, 물(εr = 79)이나 실리콘 오일(εr = 2.1–2.8) 같은 유전율이 높은 매질을 쓰면 기존 축전기 기반 분극 이력 측정값에 더 가까운 항전기장이 나왔다. 물을 매질로 쓴 PFM 영상은 주기적으로 분극된 니오브산리튬 결정에서 진폭과 위상 자료를 더 정확하게 얻게 했다. 탐침이 일으키는 분극 반전의 나노 규모 현상을 이해하고 더 정량적인 연구로 가는 길을 보였다.[^p7] | 1저자 Seongmun Eom, 마지막 저자 홍승범 (6명) |
| 8 | 2026 | [Nucleation to propagation switching modes in Ferroelectric Hf0.5Zr0.5O2 capacitors](https://doi.org/10.1021/acs.nanolett.6c01580) · Nano Letters 26 | 하프니아 기반 강유전체의 분극 반전은 나노 규모 도메인의 생성(핵 생성)과 도메인 벽의 이동이 정하지만, 전극 계면과 열처리가 결정립 규모에서 이 과정을 어떻게 정하는지는 알려지지 않았다. 이 논문은 바이어스에 따른 PFM과 펄스 반전 측정으로 하부 전극과 열처리가 10 nm 두께 Hf0.5Zr0.5O2(HZO) 축전기의 분극 반전을 어떻게 조절하는지 밝혔다. TiN 전극은 빠른 핵 생성과 결정립을 넘는 전파를, NbN 전극은 결정립 안의 점진적 반전을 낳고, MoO2 전극은 강유전 반전을 크게 억제했다. 가장 빠른 반전은 600 °C에서 열처리한 TiN/HZO/TiN에서 얻었고, 이는 고운 결정립 미세 구조와 협동적 전파를 돕는 결정립계와 맞는다. 수정한 KAI(Kolmogorov–Avrami–Ishibashi) 모형으로 펄스 반전 속도를 정량 분석한 결과 핵 생성과 성장의 시간 상수가 비슷해 두 과정이 함께 진행됨을 보였다.[^p8] | 1저자 Batzorig Buyantogtokh, 마지막 저자 홍승범 (6명) |

## 교수와 전문 분야

홍승범 교수(Seungbum Hong)는 KAIST 신소재공학과 정교수(Full Professor)다. 누리집 교수 페이지에 따르면 교수는 2021년 9월부터 신소재공학과 정교수이고, 2024년 3월부터 KAIST 교무처장(Vice President, Office of Academic Affairs), 2022년 11월부터 KAIST 글로벌경쟁력보좌역(처장급)을 맡고 있다. 2021년 6월–2026년 6월 신소재공학과 학과장, 2024년 4–11월 KAIST Global Institute of Talented Education 원장을 지냈다.[^prof]

교수 페이지에 따르면 교수는 KAIST에서 1994년 Ceramic Science and Engineering 학사(summa cum laude), 1996년 Materials Science and Engineering 석사, 2000년 Materials Science and Engineering 박사 학위를 받았다. 박사 학위 논문은 원자간력 현미경을 이용한 Pb(Zr,Ti)O3 박막의 강유전 도메인 영상 연구다.[^prof] 1996–1997년 한국전자통신연구원(ETRI) Research Associate, 2000–2001년 스위스 로잔 연방공과대학교(Swiss Federal Institute of Technology) 박사후연구원으로 압전 힘 현미경(Piezoelectric Force Microscopy)을 이용한 강유전 박막의 피로와 분극 반전을 연구했다.[^prof] 2000년 3월–2007년 9월 삼성종합기술원에서 탐침 저장 장치용 강유전 매체와 저항성 탐침 저장 장치, 강유전 하드디스크를 연구개발했고, 2007년 10월–2017년 1월 미국 아르곤 국립연구소(Argonne National Laboratory)에서 Materials Scientist와 Nanoscience Scientist(tenured staff scientist)로 페로익(ferroic) 나노 구조의 창발 현상과 나노 규모 기능성 이종 구조의 3차원 시각화를 연구했다.[^prof] 2012년 7월–2017년 1월 KAIST 신소재공학과 겸임교수, 2017년 1월–2021년 8월 신소재공학과 부교수를 거쳤다.[^prof]

교수 페이지는 수상으로 2008년 International Symposium on Integrated Ferroelectrics의 Young Investigator Outstanding Achievement Award, 2014년 한국과학기술한림원의 Frontier Scientist, 2020년 KAIST 이수영 교수학습혁신대상(Grand Prize for Learning & Teaching Innovation Awards) 등을 적고, 2017년 3월부터 Scientific Reports 편집위원(Editorial Board)으로 활동한다고 적는다.[^prof] 누리집 News 페이지는 2025년 10월 교수가 APAM 2024 Academician으로 선출됐고, 2026년 5월 IEEE Senior Member가 됐다고 알린다.[^news] 박사 학위 연구부터 이어진 원자간력 현미경 기반 강유전체 도메인 영상, Research 페이지의 세 갈래와 2021–2026년 논문 목록을 함께 보면, 교수의 전문 분야는 원자간력 현미경을 이용한 강유전·압전 소재와 배터리 소재의 나노 규모 영상과 물성 분석, 그리고 기계학습을 이용한 소재 정보학이다.[^prof][^ai][^ionics][^pol][^pubs]

## 응용 분야

누리집 첫 화면은 응용으로 배터리, 메모리(압전체와 강유전체), 바이오(구조·기능성 생체 소재)를 든다.[^home] AI Materials Informatics 페이지는 고에너지 밀도 리튬이온 전지 양극재의 발견과 최적화를 앞당기고 전지 생산·개발의 효율을 높이는 것을, Polarization 페이지는 고성능 센서·구동기·에너지 하베스터·생체 의료 기기 개발을 기대 효과로 적는다.[^ai][^pol] 누리집 News 페이지는 2025년 10월 연구실의 「AI for Material Discovery」 기술이 리튬 금속 전지 기업 BEI에 이전됐다고 알린다.[^news] 대표 논문 3은 그 방법이 합금 공정 설계에 쓰일 수 있다고, 대표 논문 6은 강유전체의 마찰 비대칭을 이용한 3차원 나노 구조 가공을 mm–cm 크기로 넓힐 수 있다고 적는다.[^p3][^p6]

## 구성원

누리집 Current members 페이지의 연구 구성원 25명이다(Post-doc 3명, Ph.D. candidate 13명, M.S. candidate 9명).[^members] 과정은 카드의 분류 표기이며, Ph.D. candidate 분류에는 상세 페이지가 석박사 통합과정(Integrated M.S. and Ph.D. Program)으로 적은 5명이 들어 있다. 시작은 각 구성원 상세 페이지의 학력·경력 줄 가운데 현재(present)로 끝나는 줄의 시작 연도이고, 연구 주제는 상세 페이지의 Research Interest 표기다.[^members] M.S. candidate 가운데 이름이 Ajin Kim인 사람이 두 명이다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Batzorig Buyantogtokh | 박사후연구원 | 2026 | Ferroelectric materials, Negative Capacitance, Ferroelectric materials imagining analysis with AFM | batzo0301@kaist.ac.kr | 8 |
| Yoonhan Cho | 박사후연구원 | 2026 | In-situ AFM, SEI analysis, Lithium metal anode, AFLMB | choyh1219@kaist.ac.kr |  |
| Sungbin Yang | 박사후연구원 | 2025 | next-generation battery | ssangvi0421@kaist.ac.kr |  |
| Seonggon Han | 박사과정 | 2023 | AFM, PFM, Battery Material, Machine Learning | skhan1015@kaist.ac.kr |  |
| Yeongyu Kim | 박사과정 | 2022 | Ferroelectrics, Negative capacitors | yeon-gyu@kaist.ac.kr | 7 |
| Seonghyun Kim | 박사과정 | 2023 | Materials imaging analysis with AFM, Battery materials | gimsh97@kaist.ac.kr |  |
| Gumin Kang | 박사과정 | 2024 | Materials Imaging Analysis with AFM, ESM | gm612@kaist.ac.kr |  |
| Chaewon Gong | 박사과정 | 2024 | Semiconductor Materials & Devices, Machine learning | g.chaewon@kaist.ac.kr | 5 |
| Seunghwan Ryu | 박사과정 | 2024 | AFM Imaging & Analysis , Battery Materials | victoryhwan@kaist.ac.kr |  |
| Dongyan Chen | 박사과정 | 2024 | AFM, machine learning, battery materials | dongyan.chen@kaist.ac.kr | 5 |
| Kunwoo Park | 박사과정 | 2024 | AFM imaging & analysis, Semiconductor materials, ferroelectric materials | kw1031@kaist.ac.kr |  |
| Chaeyul Kang | 박사과정 | 2026 | Semiconductor devices, Battery materials, and Machine learning | braveyul0416@kaist.ac.kr | 2 |
| Donghun Kim | 박사과정 | 2024 | AFM, Battery materials | ehdgns928@kaist.ac.kr |  |
| Yoonah Ko | 박사과정 | 2025 | Ferroelectric Materials, Semiconductor Materials & Devices | yoon2814@kaist.ac.kr |  |
| Sanggil Park | 박사과정 | 2025 | Materials imaging analysis with AFM, Battery materials | sanggil201@kaist.ac.kr |  |
| Tangsulu Adil | 박사과정 | 2025 | AFM Imaging, semiconductor devices, ferroelectric materials |  |  |
| Jinho Choi | 석사과정 | 2024 | Ferroelectric materials, Materials imaging analysis with AFM, Surface Chemistry, Machine learning | jinhoci@kaist.ac.kr |  |
| Junho Yang | 석사과정 | 2025 | Materials imaging analysis with AFM, machine learning | ddid904@kaist.ac.kr |  |
| Jihui Won | 석사과정 | 2025 | AFM Imaging & analysis, AI/ML for materials informatics, Semiconductor materials | wjh530@kaist.ac.kr |  |
| Jaehyun Yun | 석사과정 | 2025 | AFM, ferroelectrics, semiconductor materials | jaehyun628@kaist.ac.kr |  |
| Ajin Kim | 석사과정 | 2026 | Battery materials, AFM imaging analysis, Machine learning | ajinkim@kaist.ac.kr |  |
| Jae-eon Yeo | 석사과정 | 2026 | AFM imaging, ferroelectrics based synaptic devices, semiconductor materials | yju0703@kaist.ac.kr |  |
| Changseob Lee | 석사과정 | 2026 | AI for Materials Science, Energy Materials, Biomaterials | cseoblee@kaist.ac.kr |  |
| Ajin Kim | 석사과정 | 2026 | Ferroelectric Materials, AFM imaging analysis | kajin10@kaist.ac.kr |  |
| Lagyeong Jeong | 석사과정 | 2026 | Semiconductor materials, Biomaterials | lgjeong@kaist.ac.kr |  |

## 졸업생

누리집 Alumni 페이지의 37명이다(Post-doc 9명, Doctor 11명, Master 14명, Researcher 3명).[^alumni] 학위·과정은 카드의 분류 표기이고, 이름은 누리집 표기에서 Dr.·Mr.·Ms. 같은 호칭을 뗀 것이다. 괄호 연도는 각 졸업생 상세 페이지의 학력·경력 줄 가운데 KAIST에서 그 분류에 해당하는 줄(Doctor는 박사과정, Master는 석사과정, Post-doc은 박사후연구원이나 Research Fellow, Researcher는 연구원 줄)이 끝난 연도이고, 진로는 현재(present)로 끝나는 줄의 표기다. 세 줄은 현재 줄이 없어 진로 칸이 비어 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Youngwoo Choi | Post-doc (2026) | SK Hynix |
| Seongmun Eom | Post-doc (2025) | Post-doc, Materials Science and NanoEngineering, Rice University, Huston, TX, United States |
| Chee Sien, Wong | Post-doc (2022) | RnD Engineer, Zhejiang Casnovo Materials Co. Ltd. Zhoushan, Zhejiang, China |
| Chi Hao Liow | Post-doc (2021) | Huawei |
| Chungik Oh | Post-doc (2020) | Samsung Electronics |
| Hongjun Kim | Post-doc (2020) | Samsung Electronics |
| Jeongjae Ryu | Post-doc (2020) | Samsung Electronics |
| Panpan Li | Post-doc (2019) | Palamedrix, San Diego, USA |
| Yooun Heo | Post-doc (2017) | Assistant Professor, Physics, Inha Univerisity, Incheon, Korea |
| Benediktus Madika | Doctor (2026) | Post-doc, SNU Postdoctoral Fellow |
| Uichang Jeong | Doctor (2026) | Samsung Electronics |
| Aditi Saha | Doctor (2025) |  |
| Soyun Joo | Doctor (2025) | Deputy Editor, Advanced Materials, Wiley |
| Jimin Oh | Doctor (2023) | Assistant Professor, Smart Mobility Engineering, Kyungpook National Univerisity, Daegu, Korea |
| Seongwoo Cho | Doctor (2023) | Post-doc, University of Geneva, Switzerland |
| Gun Park | Doctor (2023) | Analysis Team at LG Energy Solution |
| Jiwon Yeom | Doctor (2023) | Artificial Intelligence Team, Samsung Advanced Institute of Technology |
| Jaegyu Kim | Doctor (2021) | Post-doc, Materials Science and Engineering, University of California, Berkeley, CA, United States |
| Hoon Kim | Doctor (2021) | Samsung Electronics |
| Seokjung Yun | Doctor (2021) | Samsung Electronics |
| Wei-Hsuan Chen | Master (2026) | TSMC |
| WonJeong Yu | Master (2024) | Ph.D. candidate, Materials Science and Engineering, KAIST, Daejeon, Korea |
| Dahyun Lee | Master (2024) | Samsung Electronics |
| James Philips | Master (2023) | Ph.D candidate, Materials Science and Engineering, University of Virginia, Virginia, USA |
| Jingshu Zhang | Master (2022) | Huawei |
| Eunnuri Cho | Master (2022) | SK Hynix |
| Soyeon Kim | Master (2022) | Samsung Electronics |
| Kyungmin Kwon | Master (2024) | Samsung Electronics |
| Jaewoon Kim | Master (2021) | Balance Hero |
| HyunJi Kim | Master (2021) | Samsung Electronics |
| Youngjoon Han | Master (2020) | Ph.D., Physics, California Institute of Technology, Pasadena, CA, United States |
| Hyoungkyu Kim | Master (2020) | Samsung Electronics |
| Albina Jetybayeva | Master (2019) | Ph.D., Materials Science and Engineering, University of Tennessee, Knoxville, Tennessee, United States |
| Melodie Glasser | Master (2019) | Ph.D., Materials Science and Engineering, Colorado School of Mines, Golden, CO |
| Šárka Kučerová | Researcher (2022) |  |
| Matthew Ryan | Researcher (2021) |  |
| Hojoon Lee | Researcher (2020) | M.S., Materials Science and Engineering, GIST, Gwangju, Korea |

## 최근 논문 목록 (2021–2026)

누리집 Journals 페이지의 2026–2021년 연도 구역에서 옮긴 88편이다(2026년 18편, 2025년 19편, 2024년 17편, 2023년 11편, 2022년 10편, 2021년 13편).[^pubs] 저자·제목·학술지 표기는 누리집 그대로이고, 연도는 누리집 연도 구역의 연도다. 목록에는 누리집의 저자·제목·학술지명을 옮겼으며, 원문 일부 항목에 적힌 권·호·쪽은 이 목록에서 생략했다. 일부 항목의 저자 이름 뒤 *는 누리집이 뜻을 적지 않은 표시다. 2022년 구역의 한 편은 누리집에 학술지 표기가 없어 학술지 칸에 확인한 판본(Research Square 사전 공개본)을 적었다. 목록 구성 기준은 근거 페이지에 적었다.

**2026**

- Mohammad Moein Seyfouri, Peiran Tong, Yoonah Ko, Menghui Xia, Qi Zhang, Zijian Hong, Bin Xu, Seungbum Hong, He Tian, Nagarajan Valanoor, Daniel Sando. "A Polar Topology Network Induces Elastic Stiffening in Ferroelectric Oxide Superlattices". *Small*.
- Kunwoo Park, Chaewon Gong, Sunghwan Park, Sang-Hee Ko Park, Seungbum Hong. "Three-Dimensional Visualization of Conductive Filaments in TiO2 via Conductive Atomic Force Microscopy Tomography". *Nano Letters*.
- Sheung Hun Kim, Youngkeun Park, Batzorig Buyantogtokh, Jaejoong Jeong, Chanmi Yu, Seungbum Hong, Byung Jin Cho. "Enhanced Disturbance Immunity in Ferroelectric FETs Using La-Doped HfO2 Film". *IEEE EDL*.
- Pijush Kanti Aich, Rajarshi Chakraborty, Akhilesh Kumar Yadav, Utkarsh Pandey, Chandra Bhal Singh, Priyanka Chetri, Seongmun Eom, Pranjit Barman, Seungbum Hong, Bhola Nath Pal. "Low-operating voltage ferroelectric multistate memory transistor with a capability of self-bias memory retention". *Materials Science in Semiconductor Processing*.
- Seongwoo Cho, Hyeonbin Moon, Iaroslav Gaponenko, Eunnuri Cho, Céline Lichtensteiger, Ruben Skjelstad Dragland, Ji Hye Lee, Jan Schultheiss, Dennis Meier, Seunghwa Ryu, Seungbum Hong, Patrycja Paruch. "Nanoscale frictional imaging of ferroelectric domains". *Science Advances*.
- Batzorig Buyantogtokh, Sheung Hun Kim, Hoon Kim, Byung Jin Cho, Uwe Schroeder, Seungbum Hong. "Nucleation to propagation switching modes in Ferroelectric Hf0.5Zr0.5O2 capacitors". *Nano Letters*.
- Yeongyu Kim, Minseung Gyeon, Ji Hoon Hong, Seongmun Eom, Kunwoo Park, Hongsik Park, Hae Yeon Lee, Sung Beom Cho, Kibum Kang, Seungbum Hong. "Nanoscale imaging of charge transport across the semimetal-semiconductor interface in monolithic platinum diselenide". *Matter*.
- Dongyan Chen, Junki Lee, Chaeeun Song, Seung Hee Han, Youngwoo Choi, Chaewon Gong, Aditi Saha, Nam-Soon Choi, Jong Min Yuk, Seungbum Hong. "Quantitative Analysis of Topographic Crosstalk in DART-ESM Arising from Feedback-Loop-Delay-Induced Contact Stiffness Variations in Battery Materials". *Small methods*.
- Jinseo Kim, Chaeyul Kang, Eunbin Noh, Junhwan Yu, Ateeq Ahmed, Wei-Hsuan Chen, Seungbum Hong, Jimin Oh. "Synergistic effects of calendering and laser structured electrode for high performance lithium batteries". *Chemical Engineering Journal*.
- Kil-dong Sung, Min-Su Kim, Jinhyuk Jang, Gi-Yeop Kim, Kyung Song, Si-Young Choi, Seungbum Hong. "Selective a-domain switching by sub-coercive field in PbTiO3 thin films". *Microstructures*.
- Jun-Seo Lee, Seungjae Lee, Hyojun Kim, WonJeong Yu, Hyungdoh Lee, Jaedong Jang, Seungwoo Lee, Eunha Park, Hyungju Ahn, Seungbum Hong, Jung-Yong Lee, Himchan Cho. "Highly Bright Deep-Blue Perovskite Light-Emitting Diodes via Dual-Passivating Additive-Based Synergetic Solid-State Halide Exchange". *Advanced Optical Materials*.
- Yoonhan Cho, Jeong-A Lee, Seonghyun Kim, Youngwoo Choi, Nam-Soon Choi, Seungbum Hong. "Multiscale Imaging Methodology for Surface Morphological Changes in Lithium Metal Anode Using Coupled Operando OM and In Situ EC-AFM". *Advanced Materials Interface*.
- Yujang Cho, Seongcheol Ahn, Yeji Han, Yonghan Jo, Min Soo Kim, ,Yoonah Ko, Dogyeong Jeon, Seungbum Hong, Chan Beum Park, Il-Doo Kim. "Scalable Hygroscopic Moisture-Electric Generator With Long-Term Stability for Self-Powered Wound-Healing Stimulation". *Advanced Materials*.
- Jeong-A. Lee, Haneul Kang, Yoonhan Cho, Seong Hyeon Kweon, Seonghyun Kim, Syed Azkar UI Hasan, Minju Song, Saehun Kim, Eunji Kwon, Samuel Seo, Kyoung Han Ryu, Rama K. Vasudevan, Sang Kyu Kwak, Seungbum Hong, Nam-Soon Choi. "Conjugation-mediated and polarity-switchable interfacial layers for fast cycling of lithium-metal batteries". *InfoMat*.
- Seonghyun Kim, Yoonhan Cho, Youngwoo Choi, Seungbum Hong. "Spatially Selective Lithium Plating and Stripping in Lithium Metal Anodes". *ACS Energy Letters*.
- Junki Lee, Dongyan Chen, Aditi Saha, Jacob Choe, Seungbum Hong, Jong Min Yuk. "Enabling Facile Synthesis and High Sodium Ionic Conductivity in NZTO Solid Electrolyte by Substituting Fe3+". *ChemSusChem*.
- Seongju Park, Seongheon Kim, Yeongyu Kim, Seungbum Hong, Jinwoo Chu, Hyun Woo Jeong, Min Hyuk Park, Yun Seog Lee, Byungha Shin. "Heterodimensional Interface for Improved Photovoltage and Stability in Narrow Bandgap Sn–Pb Perovskite Solar Cells via Vacancy-Ordered Double Perovskite". *Small*.
- Yeongyu Kim, Kunwoo Park, Seonggon Han, Dongyan Chen, Donghun Kim, Gumin Kang , Seungbum Hong. "Atomic Force Microscopy for Ferroelectric Materials Research". *Journal of Materials Chemistry C*.

**2025**

- Wonbeom Lee, Wei Liu, Cheng Zhang, Seungmin Shin, Jaejun Lee, Jaedong Jang, Sanggil Park , Seungbum Hong , Sihong Wang, Himchan Cho. "Hybrid Liquid Metal Cathode Enables High-Performance Intrinsically Stretchable OLEDs". *Advanced materials*.
- Batzorig Buyantogtokh , Eun Young Kim , Sheung Hun Kim , Seongmun Eom , Byung Jin Cho, Kyung Min Kim , Seungbum Hong. "Visualization of grain boundary-mediated domain nucleation and growth in polycrystalline Pb(Zr52Ti48)O3 ferroelectric capacitor". *APL Materials*.
- Uichang Jeong, Seunghwan Ryu, Chaewon Gong, Youngwoo Choi, Juwon Kim, Jongwoo Lim, Seungbum Hong. "Nanoscale Visualization and Contact Angle Analysis of Water Droplets on Ferroelectric Materials". *ACS Applied Materials & Interfaces*.
- Benediktus Madika, Chaeyul Kang, JooSung Shim, Taemin Park, Jung Hyeon Moon, EunAe Cho, Seungbum Hong. "Uncertainty-Quantified Primary Particle Size Prediction in Li-Rich NCM Materials via Machine Learning and Chemistry-Aware Imputation". *Advanced Science*.
- Tae Yeon Kim, Gopinathan Anoop, Hyeon Jun Lee, Sanjith Unithrattil, JeOh Choi, Wooseon Choi, Jaegyu Kim, Jacob A. Zorn, Jiwon Yeom, Seong Min Park, HyunJin Joh, Su Yong Lee, Yasuhiko Imai, Seungbum Hong, Young-Min Kim, Long-Qing Chen. "Electric field-induced anomalous structural dynamics of nanodomains in BaTiO3-based relaxor ferroelectric thin films". *Materials Today*.
- Boris N. Slautin, Yongtao Liu, Kamyar Barakati, Yu Liu, Reece Emery, Seungbum Hong, Astita Dubey, Vladimir V. Shvartsman, Doru C. Lupascu, Sheryl L. Sanchez, Mahshid Ahmadi, Yunseok Kim, Evgheni Strelcov, Keith A. Brown, Philip D. Rack, Sergei V. K. "Materials Discovery in Combinatorial and High-throughput Synthesis and Processing: A New Frontier for SPM". *Applied Physics Reviews*.
- Benediktus Madika, Aditi Saha, Chaeyul Kang, Batzorig Buyantogtokh, Joshua Agar, Chris M. Wolverton, Peter Voorhees, Peter Littlewood, Sergei Kalinin, Seungbum Hong. "Artificial Intelligence for Materials Discovery, Development, and Optimization". *ACS Nano*.
- Chaewon Gong, Sunghwan Park, ,Seongmun Eom, Youngwoo Choi, Sang-Hee Ko Park, Seungbum Hong. "Spatially Correlated Oxygen Vacancies, Electrons and Conducting Paths in TiO2 Thin Films". *ACS Applied Materials & Interfaces*.
- Jaegyu Kim, Youngki Yeo, Yong-Jun Kwon, Juhyun Lee, Jeongdae Seo, Seungbum Hong, Chan-Ho Yang. "Dynamic mechanical writing of skyrmion-like polar nanodomains". *npj Quantum Materials*.
- Soyun Joo, Seongmun Eom, Youngwoo Choi, Uichang Jeong, Yoonhan Cho, WonJeong Yu, Kunwoo Park, Seungbum Hong. "Atomic Force Microscopy for Cross-Disciplinary Materials Research". *Small Methods*.
- Jinhyuk Jang, Yeongrok Jin, Yeon-Seo Nam, Heung-Sik Park, Jaegyu Kim, Kyeong Tae Kang, Yerin So, Jiwoung Choi, Youngchang Choi, Jaechan Shim, Panithan Sriboriboon, Dong Kyu Lee, Kyoung-June Go, Gi-Yeop Kim, Seungbum Hong, Jun Hee Lee, Daesu. "Sub-unit-cell-segmented ferroelectricity in brownmillerite oxides by phonon decoupling". *Nature Materials*.
- Soyun Joo, Yoonah Ko, Rama K. Vasudevan, Seungbum Hong. "Phase Engineering for Enhanced Piezoresponse in P(VDF-TrFE) and Its Composites". *Advanced Materials Interfaces*.
- Youngwoo Choi, Gumin Kang, Seonghyun Kim, Yoonhan Cho, Jaewhan Oh, Dongho Kim, Jacob Choe, Jong Min Yuk, Pyuck-Pa Choi, Yongsoo Yang, Sung-Yoon Chung, Chi Won Ahn, Jongwoo Lim, Seungbum Hong. "Multiscale Materials Imaging and Spectroscopy for Battery Materials". *EcoMat*.
- Youngwoo Choi, Chris M. Wolverton, Seungbum Hong. "Machine learning-based melting congruency prediction of binary compounds using density functional theory-calculated formation energy". *APL Machine Learning*.
- Dong Won You, Jeongbin Yoon, Seonghyun Kim, Geon Gug Yang, Chan Woo Lee, Jonghwa Shin, Seungbum Hong, Jang Hwan Kim, Sang Ouk Kim. "Bioinspired Deformable Antireflective Materials by Block Copolymer Self-Assembly". *ACS Applied Materials & Interfaces*.
- Chang Jae Yoon, Gopinathan Anoop, Seong Min Park, Yeong Jun Son, Tae Yeon Kim, Sanjith Unithrattil, Gyeongtak Han, Young-Min Kim, Gi-Yeop Kim, Si Young Choi, Seongwoo Cho, Seungbum Hong, Ji Young Jo. "Defect induced polar distortion in SrMnO3 thin films". *Applied Surface Science*.
- Minjee Kim, Hyeongyu Moon, Seonghyun Kim, Yoonhan Cho, Taekyung Lee, Sewon Park, Hyunchul Kim, Yo Han Kwon, Seungbum Hong, Nam-Soon Choi. "Tunable solvation structures for fast charging of micron-Si anodes in energy-dense lithium-ion batteries". *Chemical Engineering Journal*.
- Chaeeun Song, Seung Hee Han, Youngwoo Choi, Hong Rim Shin, Min Kyu Kim, Chaewon Gong, Dongyan Chen, Jong‐Won Lee, Seungbum Hong, Nam‐Soon Choi. "Geometric Design of Interface Structures and Electrolyte Solvation Chemistry for Fast Charging Lithium‐Ion Batteries". *Advanced Materials*.
- Kwongyo Shin, Hyeongyu Moon, Gumin Kang, Donggyun Shin, Seonggon Han, Seungbum Hong, and Nam-Soon Choi. "Interfacial Engineering Using a Thiophene-based Electrolyte Additive for High-Voltage Lithium-Ion Batteries". *Energy & Fuels*.

**2024**

- Soyun Joo, Uichang Jeong, Chaewon Gong, and Seungbum Hong\*. "Bridging Mechanical and Electrical Analyses in AFM: Advances, Techniques, and Applications". *Accounts of Materials Research*.
- Seungwon Kim, Sewon Park, Minjee Kim, Yoonhan Cho, Gumin Kang, Sunghyun Ko, Daebong Yoon, Seungbum Hong, Nam-Soon Choi. "Improving Fast-Charging Performance of Lithium-Ion Batteries through Electrode-Electrolyte Interfacial Engineering". *Advanced Science*.
- Myeongchan Ko, Ji Su Park, Soyun Joo, Seungbum Hong, Jong Min Yuk and Kyung Min Kim. "Direct growth of ferroelectric orthorhombic ZrO2 on Ru by atomic layer deposition at 300 °C". *Materials Horizon*.
- Jinhyeong Jang, Soyun Joo, Jiwon Yeom, Yonghan Jo, Jingshu Zhang, Seungbum Hong, Chan Beum Park. "Lateral Piezoelectricity of Alzheimer's Aβ Aggregates". *Advanced Science*.
- Megala Moorthy, Ranjith Thangavel, Bala Krishnan Ganesan, Aditi Saha, Seungbum Hong, Yun-Sung Lee. "Ultra-high areal capacity, ultra-long life, dendrite-free sodium metal anode enabled by antimony-based Na-ion conducting artificial SEI layers". *Chemical Engineering Journal*.
- Seongmun Eom, Pravin Kavle, Deokyoung Kang, Yeongyu Kim, Lane W. Martin, Seungbum Hong. "Unveiling the Nanoscale Dielectric Gap and Its Influence on Ferroelectric Polarization Switching in Scanning Probe Microscopy". *Advanced Functional Materials*.
- Swathi Ippili, Gobbilla Sai Kumar, Arti Sharma, Yoonah Ko, Seungbum Hong, Mahendra Goddati, Haneesh Saini, Jaebeom Lee, Tae-Youl Yang, Soumik Siddhanta, Venkatraju Jella, Soon-Gil Yoon, Kolleboyina Jayaramulu. "Advancing Charge Density in Temperature‐Dependent Amphiphile Metal–Organic Polyhedra‐Based Triboelectric Nanogenerators". *Advanced Energy Materials*.
- Seongwoo Cho, Iaroslav Gaponenko, Kumara Cordero-Edwards, Jordi Barceló-Mercader, Irene Arias, Daeho Kim, Céline Lichtensteiger, Jiwon Yeom, Loïc Musy, Hyunji Kim, Seung Min Han, Gustau Catalan, Patrycja Paruch & Seungbum Hong. "Switchable tribology of ferroelectrics". *Nature Communications*.
- Jeong-A Lee, Saehun Kim, Yoonhan Cho, Seong Hyeon Kweon, Haneul Kang, Jeong Hwan Byun, Eunji Kwon, Samuel Seo, Wonkeun Kim, Kyoung Han Ryu, Sang Kyu Kwak, Seungbum Hong, Nam-Soon Choi. "Compositionally Sequenced Interfacial Layers for High-Energy Li-Metal Batteries". *Advanced Science*.
- Soyun Joo, Yonghyun Gwon, Soyeon Kim, Sunho Park, Jangho Kim\*, and Seungbum Hong\*. "Piezoelectrically and Topographically Engineered Scaffolds for Accelerating Bone Regeneration". *ACS Applied Materials & Interfaces*.
- Kyungmin Kwon, Seunghwan Ryu, Soyun Joo, Youngjoon Han, Donghyeon Baek, Moonsoo Park, Dongwon Kim, and Seungbum Hong. "Effect of resonant acoustic powder mixing on delay time of W–KClO4–BaCrO4 mixtures". *APL Materials*.
- Seokjung Yun, Hoon Kim, Myungsoo Seo, Min-Ho Kang, Taeho Kim, Seongwoo Cho, Min Hyuk Park, Sanghun Jeon, Yang-Kyu Choi, and Seungbum Hong\*. "Effect of Annealing Temperature on Minimum Domain Size of Ferroelectric Hafnia". *ACS Applied Electronic Materials*.
- Hyeonghun Park, WooJun Seol, Geumyong Park, Gopinathan Anoop, Jihun Kim, Tomas Tamulevičius, Sigitas Tamulevičius, Soyun Joo, Seungbum Hong, Ji Young Jo, Hyeong-Jin Kim. "Zn anode with hydrophobic and ferroelectric P(VDF-TrFE) layers for dendrite-free aqueous Zn-ion batteries". *Applied Surface Science*.
- Yoonsu Shim, Incheol Jeong, Junpyo Hur, Hyoungjeen Jeen, Seung-Taek Myung, Kang Taek Lee, Seungbum Hong, Jong Min Yuk\*, and Chan-Woo Lee\*. "Data-driven design of NASICON-type electrodes using graph-based neural networks". *Batteries & Supercaps*.
- Jimin Oh, Jiwon Yeom, Benediktus Madika, Kwang Man Kim, Chi Hao Liow, Joshua C. Agar & Seungbum Hong. "Composition and state prediction of lithium-ion cathode via convolutional neural network trained on scanning electron microscopy images". *npj Computational Materials*.
- Hyeongyu Moon, Donguk Kim, Gun Park, Kwongyo Shin, Yoonhan Cho, Chaewon Gong, Yoon-Sung Lee, Huibeom Nam, Seungbum Hong, Nam-Soon Choi. "Balancing Ionic and Electronic Conduction at the LiFePO4 Cathode–Electrolyte Interface and Regulating Solid Electrolyte Interphase in Lithium-Ion Batteries". *Advanced Functional Materials*.
- Venkatraju Jella, Subhashree Behera, Swathi Ippili, Soyun Joo, Kyungmin Kwon, Seungbum Hong, Hyun‐Suk Kim, Soon‐Gil Yoon. "Self-Charging Power System Empowered by Bismuth Halide Perovskite-Based Hybrid Nanogenerator and Lithium-ion Battery". *Small*.

**2023**

- Sung Su Han, Athira Thacharon, Jun Kim, Kyungwha Chung, Xinghui Liu, Woo-Sung Jang, Albina Jetybayeva, Seungbum Hong, Kyu Hyoung Lee, Young-Min Kim, Eun Jin Cho, Sung Wng Kim. "Boosted Heterogeneous Catalysis by Surface-Accumulated Excess Electrons of Non-Oxidized Bare Copper Nanoparticles on Electride Support". *Advanced Science*.
- Jim James, Nathan Pruyne, Tiberiu Stan, Marcus Schwarting, Jiwon Yeom, Seungbum Hong, Peter Voorhees, Ben Blaiszik, Ian Foster. "Segmentation of tomography datasets using 3D convolutional neural networks". *Computational Materials Science*.
- Seyeon Park, SungHyun Jeon, Honghui Kim, James Philips, DongHwan Oh, Jaewan Ahn, Minhyun Kim, Chungseong Park, Seungbum Hong, Jihan Kim, WooChul Jung, Il-Doo Kim. "Imparting Metal Oxides with High Sensitivity Toward Light-Activated NO2 Detection Via Tailored Interfacial Chemisty". *Advanced Functional Materials*.
- Jimin Oh, Gun Park, Hongjun Kim, Sujung Kim, Dong Ok Shin, Kwang Man Kim, Hye Ryung Byon, Young-Gi Lee, Seungbum Hong\*. "Correlating Nanoscale Structures with Electrochemical Properties of Solid Electrolyte Interphases in Solid-State Battery Electrodes". *ACS Applied Materials & Interfaces*.
- Jimin Oh, Dong Ok Shin, Myeong Ju Lee, Yong Min Lee, Young-Gi Lee, Seungbum Hong, Kwang Man Kim. "Enhancing Performance of All-Solid-State Battery by Establishment of Interconnected Li7La3Zr2O12 Network in Graphite Composite Anode". *Journal of Energy Storage*.
- Megala Moorthy, Brindha Moorthy, Bala Krishnan Ganesan, Aditi Saha, Seungju Yu, Do-Hoon Kim, Seungbum Hong, Sangho Park, Kisuk Kang, Ranjith Thangavel, Yun-Sung Lee. "A Series of Hybrid Multifunctional Interfaces as Artificial SEI layer for Realizing Dendrite Free, and Long-life Sodium Metal Anodes". *Advanced Functional Materials*.
- Gun Park, Hyeongyu Moon, Sunyoung Shin, Sumin Lee, Yongju Lee, Nam-Soon Choi, Seungbum Hong\*. "Spatially Uniform Lithiation Enabled by Single-Walled Carbon Nanotubes". *ACS Energy Letters*.
- Erbing Hua, Seunggun Choi, Siyuan Ren, Sungjun Kim, Ghulam Ali, Seon Je Kim, Woo-Sung Jang, Soyun Joo, Jingshu Zhang, Seulgi Ji, Yun Seong Cho, Joohoon Kang, Taeseup Song, Seungbum Hong, Heechae Choi, Young-Min Kim, Hyuksu Han, Sung W. "Negatively charged platinum nanoparticles on dititanium oxide electride for ultra-durable electrocatalytic oxygen reduction". *Energy & Environmental Science*.
- Chongsei Yoon, Swathi Ippili, Alphi Maria Thomas, Batzorig Buyantogtokh, Seungbum Hong\*, Venkatraju Jella\*, Van-Dang Tran, Soon-Gil Yoon\*. "Harnessing Flexoelectric and Piezoelectric Effects for Self-Charging Power Systems". *ACS Energy Letters*.
- Jaegyu Kim, Seongwoo Cho, Jiwon Yeom, Seongmun Eom, Seungbum Hong. "Revisiting contrast mechanism of lateral piezoresponse force microscopy". *Journal of Applied Physics*.
- Dae-Young Jeon\*, Soyun Joo, Dahyun Lee, Seungbum Hong\*. "Channel Thickness-Dependent Degradation of Field-Effect Mobility in Multilayer MoS2 Transistors". *ACS Applied Electronic Materials*.

**2022**

- Albina Jetybayeva, Nino Schön, Jimin Oh, Jaegyu Kim, Hongjun Kim, Gun Park, Young-Gi Lee, Rüdiger-A. Eichel, Karin Kleiner\*, Florian Hausen\*, Seungbum Hong\*. "Unraveling the State of Charge-Dependent Electronic and Ionic Structure-Property Relationships in NCM622 Cells by Multiscale Characterization". *ACS Applied Energy Materials*.
- Yun-Ho Kang, Sangbong Lee, Youngwoo Choi, Won Kyung Seong, Kyu Hyo Han, Jang Hwan Kim, Hyun-Mi Kim, Seungbum Hong, Sun Hwa Lee, Rodney S. Ruoff, Ki-Bum Kim, Sang Ouk Kim. "Large-area Uniform 1-nm-level Amorphous Carbon Layers from 3D Conformal Polymer Brushes. A 'Next-generation' Cu Diffusion Barrier?". *Advanced Materials*.
- K. Chung, J. Bang, A. Thacharon, H.Y. Song, S.H. Kang, W.-S. Jang, N. Dhull, D. Thapa, C.M. Ajmal, B. Song, S.-G. Lee, Z. Wang, A. Jetybayeva, S. Hong, K.H. Lee, E.J. Cho, S. Baik, S.H. Oh, Y.-M. Kim, Y.H. Lee, S.-G. Kim & S.W. Kim. "Non-oxidized bare copper nanoparticles with surface excess electrons in air". *Nature Nanotechnology*.
- Chi Hao Liow, Youngwoo Choi, Jiwon Yeom, Young Yim Doh, Seungbum Hong. "A Flexible Semi-Synthetic Data Generator for Risky Drinking Behavior". *학술지 표기 없음(확인한 판본: Research Square 사전 공개본)*.
- Shibnath Samanta, Gopinathan Anoop, WooJun Seol, Seong Min Park, HyunJin Joh, Je Oh Choi, Dante Ahn, Sanjith Unithrattil, Hoon Kim, Jiwon Yeom, Seungbum Hong, and Ji Young Jo. "Large electrocaloric effect with high thermal and electric field cycling stability in solution-processed Y:HfO2 thin films". *Journal of Materials Chemistry A*.
- Gun Park, Youngwoo Choi, Sunyoung Shin, Yongju Lee, and Seungbum Hong\*. "Nanoscale Visualization of the Electron Conduction Channel in the SiO/Graphite Composite Anode". *ACS Applied Materials & Interfaces*.
- C.H. Liow, H. Kang, S. Kim, M. Na, Y. Lee, A. Baucour, K. Bang, Y. Shim, J. Choe, G. Hwang, S. Cho, G. Park, J. Yeom, J.C. Agar, J.M. Yuk, J. Shin, H.M. Lee, H.R. Byon, E.A. Cho, S. Hong. "Machine learning assisted synthesis of lithium-ion batteries cathode materials". *Nano Energy*.
- Suchithra Padmajan Sasikala, Sung Hyun Kim, Cheolmin Park, Dong-Ha Kim, Hong Ju Jung, Juhyung Jung, Hojin Lee, Panpan Li, Hongjun Kim, Seungbum Hong, Sung-Yool Choi, Il-Doo Kim, Prem Prabhakaran, Kwang-Sup Lee, Sang Ouk Kim. "Spontaneous heteroassembly of 2D semiconducting van der Waals materials in random solution phase". *Materials Today*.
- Yong Cheon Park, Taehyun Kim, Hye Rin Shim, YoungWoo Choi, Seungbum Hong, Seunghyup Yoo, Sung Gap Im. "A highly bendable thin film encapsulation by the modulation of thermally induced interfacial residual stress". *Applied Surface Science*.
- Swathi Ippili, Venkatraju Jella, Jaegyu Kim, Seungbum Hong, Hyun-Suk Kim, Soon-Gil Yoon. "High-power nanogenerator of 2D-layered perovskite in a polymer matrix for self-charging battery-powered electronics". *Nano Energy*.

**2021**

- Gun Park, Hongjun Kim, Jimin Oh, Youngwoo Choi, Olga S. Ovchinnikova, Seokhwan Min, Young-Gi Lee, Seungbum Hong\*. "Quantitative Measurement of Li-Ion Concentration and Diffusivity in Solid-State Electrolyte". *ACS Applied Energy Materials*.
- DoSung Lee, Seokjung Yun, Jang-Woo Han, MinYoung Song, YoungGeun Kim, JongKweon Lee, Joonmyung Choi, Seongmin Chang, Seungbum Hong, JaeHwang Kim. "Microstructural evolution and mechanical properties of atmospheric plasma sprayed Y2O3 coating with state of in-flight particle". *Ceramics International*.
- S. Hong\*. "Single frequency vertical piezoresponse force microscopy". *Journal of Applied Physics*.
- S. Hong\*, C.H. Liow, H.R. Byon, Y. Yang, E.A. Cho, J. Yeom, G. Park, H. Kang, S. Kim, Y. Shim, M. Na, C. Jeong, G. Hwang, H. Kim, H. Kim, S. Eom, S. Cho, H. Jun, Y. Lee, A. Baucour, K. Bang, M. Kim. "Reducing Time to Discovery: Materials and Molecular Modeling, Imaging, Informatics, and Integration". *ACS Nano*.
- Colin Campbell, Yong Min Lee, Kuk Young Cho, Young-Gi Lee, Seungbum Hong and Charudatta Phatak. "Understanding the Selective Deposition of Li Metal on Nonuniform Electrode Surfaces Using Atomic Force Microscopy". *Journal of the Electrochemical Society*.
- Linh Thi Truc Nguyen, Nhu Thi Quynh Le, Vu Ba Duong, Chien Minh Tran, Seungbum Hong, Kwangsoo No & Sunghwan Lee. "Pseudo wastewater treatment by combining adsorption and phytoaccumulation on the Acrostichum aureum Linn. plant/activated carbon system". *International Journal of Phytoremediation*.
- Hyunjin Joh, Gopinathan Anoop, Won-June Lee, Dipjyoti Das, Jun Young Lee, Tae Yeon Kim, Hoon Kim, WooJun Seol, Jiwon Yeom, Sanghun Jeon, Seungbum Hong, Myung-Han Yoon\*, Ji Young Jo\*. "Low-Temperature Growth of Ferroelectric Hf0.5Zr0.5O2 Thin Films Assisted by Deep Ultraviolet Light Irradiation". *ACS Applied Electronic Materials*.
- Youngjoon Han, Jeongjae Ryu, Chungik Oh, Soyeon Kim, Andreas Schiffer, Jason P. Killgore, Seungbum Hong. "Deciphering osteoconductive surface charge effects in sintered hydroxyapatite via piezoresponse force microscopy". *Journal of Applied Physics*.
- Hyoungkyu Kim, Seokjung Yun, Tae Ho Kim, Hoon Kim, Changdeuck Bae, Sanghun Jeon, Seungbum Hong. "Effect of Hydrogen on Hafnium Zirconium Oxide Fabricated by Atomic Layer Deposition Using H2O2 Oxidant". *Physica Status Solidi - Rapid Research Letters*.
- J Yeom, T Stan , S Hong\*, P W. Voorhees. "Segmentation of Experimental Datasets via Convolutional Neural Networks Trained on Phase Field Simulations". *Acta Materialia*.
- Tae Yeon Kim, Je Oh Choi, Gopinathan Anoop, Jaegyu Kim, Seong Min Park, Shibnath Samanta, Wooseon Choi, Young-Min Kim, Seungbum Hong, Ji Young Jo. "(111)-oriented Sn-doped BaTiO3 epitaxial thin films for ultrahigh energy density capacitors". *Ceramics International*.
- Jae-Hyeon Cho, Seongwoo Cho, Jun Han Lee, Haribabu Palneedi, Ju-Hyeon Lee, Hwang-Pill Kim, Nyun Jong Lee, Siriporn Tigunta, Soodkhet Pojprapai, Sanghoon Kim, Jungho Ryu, Yoon Seok Oh, Seungbum Hong, Wook Jo. "Room-temperature multiferroicity in NiFe2O4 and its magnetoelectric coupling intensified through defect engineering". *Journal of the American Ceramic Society*.
- Shibnath Samanta, Gopinathan Anoop, HyunJin Joh, WooJun Seol, Seong Min Park, Sanjith Unithrattil, Jun Young Lee, Tae Yeon Kim, Hoon Kim, Jiwon Yeom, Seungbum Hong, Ji Young Jo. "Multi-Step Chemical Solution Deposition-Annealing Process Toward Wake-Up Free Ferroelectricity in Y:HfO2 Films". *Advanced Materials Interfaces*.

## 특허

누리집 Patents 페이지 79건 가운데 2021년 이후 연도가 적힌 1건이다. 발명자와 번호 표기는 누리집 그대로다.[^patents]

- Flexible Piezoelectric and Ferroelectric Haloimidazole Crystals (발명자 M.Owczarek, K. A.Hujsak, D. P.Ferris, A.Prokofjevs, D. P.Vinayak, J. F.Stoddart, S. Hong; 번호 US 11,091,443 B2(2021))

## 연구 과제

누리집 Research Projects 페이지의 5건이다. 누리집은 다섯 과제를 모두 On-going 분류에 두며, 기간과 지원 기관은 각 과제의 표기다.[^projects]

- 일자리 창출을 위한 뉴제너레이션 지역특화형 산학연협력 모형 개발 및 확산에 관한 연구 : 공공기술 기반 기술사업화와 창업을 중심으로 (기간 2021.09.01–2024.12.31; 지원 한국연구재단)
- 차세대 배터리(Na-ion 배터리) 개발을 위한 초민감소재 분석기법 고도화 (기간 2024.03.01–2025.02.28; 지원 한국연구재단)
- 다각도-멀티스케일 데이터 융합형 리튬이차전지 설계 인공지능 플랫폼 개발 (기간 2023.04.01–2027.12.31; 지원 한국연구재단)
- 다중모드 원자간력 현미경 이미징 기반 반응 맞춤형 전극 표면의 젖음성 및 표면 에너지 분석 기술 개발 (기간 2023.07.29–2024.07.28; 지원 한국연구재단)
- 반도체-이차전지 인터페이싱 분석 및 평가 플랫폼 기술개발 (기간 2023.01.01–2027.12.31; 지원 나노종합기술원)

## 수상

누리집 교수 페이지 HONORS and AWARDS의 2021년 10월 이후 항목 4건과 News 페이지의 2021-10-13 이후 수상 소식 22건, 모두 26건이다. 교수 페이지 항목은 연월, News 항목은 게시일이며, 문장은 각 표기를 따른다.[^prof][^news]

- 2026-07-10 · Batzo received first place poster award at IEEE ISAF-PFM 2026
- 2026-06-21 · Chaewon and Yoonah received best poster award at EEFS 2026
- 2026-05-19 · Prof. Hong received professor learning innovation award
- 2026-04-28 · Prof. Hong received KAIST Top 10 Research Achievement Award
- 2026-03-09 · MII Lab received award for excellence in safety management!
- 2025-09-10 · Ben and Chaeyul won the Grand Prize in Climate Tech Ideathon at KAIST
- 2025-07-17 · Yoonhan received an award at LG Energy Solution Industry-Academia cooperation conference
- 2025-02-11 · MII Lab has been selected as one of the '2024 Outstanding Safety Management Laboratory'.
- 2025-02-11 · Chaewon won Poster Award in Korean Dielectric Society Symposium 2025
- 2024-12-23 · Soyun Joo and Uichang Jeong won Poster Award in JKC-FE14
- 2024-12-23 · Chaewon Gong won Best Poster Award in ENGE 2024
- 2024-09-13 · Soyun Joo and Yeongyu Kim have been selected to receive a UFFC-JS 2024 travel grant.
- 2024-05-21 · Yoonhan Cho won Excellent Poster Award in KECS 2024.
- 2024-02-27 · Soyun Joo and Yoonah Ko won best poster awards at the 19th Dielectrics Symposium.
- 2024-02-27 · Aditi Saha received a safety guardian award from the DMSE at KAIST.
- 2024-02 · 개교기념표창 국제협력상 (KAIST)
- 2024-01-02 · Yoonhan Cho got best poster award in AMF-AMEC 2023.
- 2023-09-08 · Benediktus Madika won 3rd prize for the research presentation in Nano Research Campus Award held by Tsinghua University.
- 2023-02-10 · MII Lab has been selected as one of the Safety Lab by National Research Foundation of Korea.
- 2023-02 · KAIST Globalization Excellence Lab (KAIST)
- 2022-12 · Healthy Lab Award (National Research Foundation / Minister of Science and ICT)
- 2022-10-25 · Ben is awarded Excellence Prize for his essay from ASEAN-Korea Centre
- 2022-09-15 · Seongwoo is awarded a student travel grant for the upcoming MS&T 22 Technical Meeting and Conference
- 2022-03-29 · Benediktus Madika was awarded the Global Scholarship from Hyundai Motor Chung Mong-Koo Foundation
- 2022-02 · KAIST Global Lab (KAIST)
- 2021-11-12 · AI Lab Solution won the 4th ranking prize in E\*5 Lab Startup evaluation

## 소식

누리집 News 페이지의 2021-10-13 이후 글 가운데 언론 보도 13건, 강연·학술 활동 20건, 논문·자료 공개 소식 5건, 기술 이전·선정 같은 연구실과 교수 소식 5건, 모두 43건이다. 날짜는 게시일이고 문장은 글 제목 표기를 따른다. 수상 소식은 「수상」 절에 실었다.[^news]

- 2026-10-11 · Batzo and Prof. Hong appeared in the news
- 2026-09-21 · Batzo gave an invited talk for Electrical Engineering Department at University of Philippines
- 2026-09-07 · Dongyan and Prof. Hong appeared in the news
- 2026-07-13 · Yeongyu and Prof. Hong appeared in the news
- 2026-06-04 · Prof. Hong delivered a plenary lecture at EEFS 2026
- 2026-05-11 · Seonghyun, Youngwoo and Yoonhan appeared in the news
- 2026-05-06 · Prof. Hong was selected as IEEE Senior Member
- 2026-02-27 · Yoonhan was featured in the science news
- 2026-02-13 · Ben and Chaeyul appeared in the domestic news
- 2026-02-13 · MII Lab has been certified as a "security consulting lab".
- 2026-02-13 · Tsinghua University Academic Exchange
- 2026-02-02 · Prof. Hong has become one of the Plenary Speakers of EEFS 2026
- 2025-12-31 · Prof. Hong will give a talk at the 2026 Spring Global Leadership Lecture.
- 2025-11-02 · Ben, Batzo, Chaeyul and Aditi appeared in the news
- 2025-10-24 · Professor has been listed on the World Top 2% Researcher!
- 2025-10-14 · MII Lab's 'AI for Material Discovery' Technology was transferred to Lithium-Metal Battery Company BEI
- 2025-10-14 · Professor was elected as an Academician of APAM 2024
- 2025-09-15 · Professor gave a lecture at AI transformation workshop in KAIST
- 2025-09-13 · Chaewon appeared in the news
- 2025-04-29 · Machine learning dataset for secondary batteries has been officially published
- 2025-02-26 · Prof. Seungbum Hong, Plenary Speaker at PacRim 2025
- 2024-11-18 · Seongmun, Yeongyu, and Professor appeared in the news.
- 2024-08-19 · Soyun Joo appeared in the news.
- 2024-01-02 · Prof. Hong will give a talk at the 2024 Spring Global Leadership Lecture.
- 2024-01-02 · Prof. Hong, Uichang Jeong and Seunghwan Lyu appeared in KAIST News.
- 2023-08-16 · The M3I3 workshop will be held on August 22.
- 2023-07-13 · Prof. Hong will give an invited seminar at Argonne National Laboratory.
- 2023-04-02 · Prof. Hong has become one of the Plenary Speakers of AMF-AMEC 2023
- 2022-12-12 · Prof. Hong gave an invited talk at University Ranking Forum of Korea at POSTECH
- 2022-12-12 · Prof. Hanjong Paik gave an invited talk about "New Materials Discovery by Oxide Molecular-beam Epitaxy"
- 2022-12-02 · Prof. Seungbum Hong will give an invited talk in UFRK at POSTECH
- 2022-11-09 · Gun's research about Nanoscale Visualization of the Electron Conduction Channel is on KAIST news
- 2022-11-03 · Prof. Hong will give a lecture in Workshop held in Korea University
- 2022-10-24 · The article 'Segmentation of Tomography Datasets Using 3D Convolutional Neural Networks' is published in Computational Materials Science
- 2022-09-15 · MII Lab is holding M3I3 workshop
- 2022-06-23 · Paper covering 'Visualization of electron conduction channel' is published in ACS applied materials & interfaces
- 2022-06-20 · Prof. Hong will give an Invited Talk in IWSPM 2022
- 2022-04-09 · ML based cathode synthesis paper is published on Nano Energy.
- 2022-04-01 · Prof. Hong's lecture (AI materials) on KOOC launched
- 2022-03-30 · Prof. Hong will give a seminar on melting pot on April 1, 2022.
- 2022-03-11 · MII Lab appeared in Arirang TV
- 2022-02-24 · Youngwoo's work is included in Advanced Materials led by Prof. Sang Ouk Kim's Lab.
- 2021-11-01 · Prof. Hong presented "AI Materials" at STKri (CNU)

## 연락과 위치

- 위치: Dept. of Material Science and Engineering(W1-1), KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon. 교수실 #4403, 학생 연구실 #3316/#3317/#3415(Contact 페이지 표기)[^contact]
- 교수 이메일: seungbum@kaist.ac.kr[^contact][^prof]
[^p1]: J. Oh 외, S. Hong, npj Computational Materials 10, 88 (온라인 2024-05-04). <https://doi.org/10.1038/s41524-024-01279-6> 초록 기준.
[^p2]: B. Madika 외, S. Hong, Advanced Science 13, e15694 (온라인 2025-10-08). <https://doi.org/10.1002/advs.202515694> 초록 기준.
[^p3]: Y. Choi, C. M. Wolverton, S. Hong, APL Machine Learning 3, 026112 (온라인 2025-05-05). <https://doi.org/10.1063/5.0247514> 초록 기준.
[^p4]: G. Park 외, S. Hong, ACS Applied Materials & Interfaces 14, 30639-30648 (온라인 2022-06-22). <https://doi.org/10.1021/acsami.2c01460> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: D. Chen 외, S. Hong, Small Methods 10, e70763 (온라인 2026-06-11). <https://doi.org/10.1002/smtd.70763> 초록 기준.
[^p6]: S. Cho 외, S. Hong, Nature Communications 15, 387 (온라인 2024-01-09). <https://doi.org/10.1038/s41467-023-44346-0> 초록 기준.
[^p7]: S. Eom 외, S. Hong, Advanced Functional Materials 35, 2406944 (온라인 2024-09-02). <https://doi.org/10.1002/adfm.202406944> 초록 기준.
[^p8]: B. Buyantogtokh 외, S. Hong, Nano Letters 26, 10971-10979 (온라인 2026-06-15). <https://doi.org/10.1021/acs.nanolett.6c01580> 초록 기준.
[^home]: 연구실 누리집 첫 화면 <https://mii.kaist.ac.kr/> (소개 문구, APPLICATIONS·TOOLS, Project, Selected Publications, 2026-10-23 열람)
[^ai]: 연구실 누리집 Research 메뉴 AI Materials Informatics 페이지 <https://mii.kaist.ac.kr/sub2_1.php> (Goal, Approach, Impact, Code Repository, 연구 사례 그림 설명, 2026-10-23 열람)
[^ionics]: 연구실 누리집 Research 메뉴 Ionics 페이지 <https://mii.kaist.ac.kr/sub2_2.php> (Goal, Approach, Impact, 연구 사례 그림 설명, 2026-10-23 열람)
[^pol]: 연구실 누리집 Research 메뉴 Polarization 페이지 <https://mii.kaist.ac.kr/sub2_3.php> (Goal, Approach, Impact, 연구 사례 그림 설명, 2026-10-23 열람)
[^projects]: 연구실 누리집 Research Projects 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub2_4> (과제 5건의 이름, Period, Sponsor, 2026-10-23 열람)
[^prof]: 연구실 누리집 Professor 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (EDUCATION, PROFESSIONAL EXPERIENCE, HONORS and AWARDS, PROFESSIONAL ACTIVITIES, 이메일, 2026-10-23 열람)
[^members]: 연구실 누리집 Current members 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub1_2>와 구성원 25명의 상세 페이지 (분류, Research Interest, 이메일, Education and Position, 2026-10-23 열람)
[^alumni]: 연구실 누리집 Alumni 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub1_3>와 졸업생 37명의 상세 페이지 (분류, Education and Position, 2026-10-23 열람)
[^pubs]: 연구실 누리집 Journals 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (1–7쪽의 2026–2021년 연도 구역, 250–160번, 2026-10-23 열람)
[^patents]: 연구실 누리집 Patents 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub3_3> (1–6쪽, 79–1번, 2026-10-23 열람)
[^news]: 연구실 누리집 News 페이지 <https://mii.kaist.ac.kr/bbs/board.php?bo_table=sub4_1> (1–13쪽의 2021-09-30–2026-10-11 글 목록과 언론 보도 글 본문, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://mii.kaist.ac.kr/sub5_1.php> (주소, Professor Office, Student Office, 이메일, 2026-10-23 열람)
[^mse]: KAIST 신소재공학과 연구실 소개 페이지 「FIND YOUR LAB」 <https://mse.kaist.ac.kr/lab2026/lab01.html> (홍승범 항목의 영문 연구실 명칭, Academic·Plain Language 한 줄 소개, 핵심어, 연구실 홈페이지, 2026-10-23 열람)

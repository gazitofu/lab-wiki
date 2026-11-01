# Intelligent Chemistry Lab

**KAIST 화학과 · 김우연 교수**

- 분야: 계산화학, 화학반응 예측과 합성 경로 계획, 약물 설계 인공지능, 유기 발광 소재 설계
- 대분야: 화학, 컴퓨팅·AI
- 태그: 과학·공학 AI[^home], AI 신약 개발[^drug], 디스플레이·발광 소자[^materials], 설명 가능한 AI(XAI)[^drug], 다중 에이전트 시스템·분산 의사결정[^bioagent]
- 홈페이지: <https://wooyoun.kaist.ac.kr/>
- 근거와 출처: [Intelligent Chemistry Lab 근거 페이지](wooyoun-sources.md)

> 물리 법칙에 따른 계산과 인공지능을 결합해 화학반응을 예측하고, 약물과 발광 소재가 될 분자를 설계하는 연구실이다.[^home][^reaction][^drug][^materials]

## 무엇을 연구하나

김우연 교수가 이끄는 연구실은 원하는 성질의 분자(원자들이 화학적 결합으로 이루는 독립된 입자)를 설계하고 합성하는 문제를 다룬다. 계산화학(물질의 구조·성질·반응을 컴퓨터로 계산하는 분야)에 인공지능을 결합하는 것이 공통 방향이다. 물리 법칙에 따른 계산은 고전역학·양자역학·통계열역학을 바탕으로 화학 현상을 다루며, 연구실은 여기에 자료에서 규칙을 배우는 기계학습을 결합한다. 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 배우는 기계학습 분야)을 이용한 분자 설계와 반응 예측 도구를 개발한다.[^home]

첫 갈래는 화학반응 예측과 합성 계획이다. 반응물(반응에 들어가는 물질)과 생성물(반응으로 만들어지는 물질)이 주어지면, 그 사이에서 가능한 반응 기작(물질이 바뀌는 세부 단계와 그 과정)을 찾는다. 연구실의 ACE-Reaction(ACE: Advanced Computational Engine)은 화학 지식에 따른 규칙과 양자 계산을 결합해 가능한 기작을 탐색하는 소프트웨어다. 연구실은 전이 상태(반응 경로에서 에너지 장벽의 꼭대기에 해당하는 상태)를 자동으로 찾는 기능과 화학적 반응성을 예측하는 인공지능을 더하는 방향을 제시한다.[^reaction] 최근에는 분자의 에너지 변화를 반영해 구조를 조정하는 방법과, 반응물·생성물·전이 상태의 구조를 모은 Reaction-QM 자료집을 발표했다.[^p1][^p2]

둘째는 약물 후보를 찾고 설계하는 계산 방법이다. 단백질(아미노산이 연결되어 이루는 생체 분자)과 후보 물질의 입체 구조를 바탕으로, 결합 친화도(서로 결합하려는 정도)를 예측하는 딥러닝 모형을 만든다. 새로운 표적에 대한 자료가 적고 모형의 판단 근거가 드러나지 않는 문제를 다루기 위해, 모형의 구조에 화학 지식을 반영하는 접근을 내세운다.[^drug] 원하는 성질에 맞춰 분자의 일부를 교체하는 생성 모형과, 분자 구조 및 표적과의 상호작용을 함께 생성하는 방법을 발표했다.[^p4][^p5]

셋째는 유기 발광 소재 설계다. 계산화학과 기계학습으로 새로운 물질의 성질을 이해하고, 원하는 성질을 갖춘 분자를 컴퓨터로 설계하는 방법을 개발한다. 구체적인 대상으로 OLED(Organic Light-Emitting Diode, 유기 물질이 전류를 받아 빛을 내는 소자)에 쓰이는 분자를 든다.[^materials] 분자 조각에 기반한 생성 인공지능과 계산을 결합해 자료가 적은 조건에서 발광 소재를 설계하고, 녹색 발광체를 실험으로 검증한 연구가 이 갈래에 해당한다.[^p3] 효소(생체 반응을 촉진하는 촉매)와 반응 대상 물질 사이의 상호작용 예측, 단백질 구조 예측을 위한 표현 학습(자료의 특징을 계산에 쓸 형태로 배우는 방법)도 연구했다.[^p6][^p7]

## 주요 연구 주제

### 반응 경로 예측과 자동 합성 계획

반응 예측은 가능한 반응 기작을 찾고 계산으로 검토하는 일이고, 합성 계획은 원하는 분자를 만들기 위한 반응의 순서를 정하는 일이다. 연구실은 역합성(목표 분자에서 출발해 이를 만들 재료와 반응을 거꾸로 찾아가는 분석)에 기계학습을 적용한다. CASP(Computer-Aided Synthesis Planning, 컴퓨터를 이용한 합성 계획) 도구를 개발하며, 보고된 반응 자료에서 화학 지식을 배운 신경망으로 합성 경로를 탐색한다.[^reaction]

### 약물과 표적의 상호작용 예측 및 분자 생성

연구실은 약물 후보와 표적 단백질 사이의 원자 쌍 에너지를 물리 법칙을 반영한 식으로 예측한다. 이를 결합 친화도 점수에 연결해 가상 스크리닝(후보 물질들을 계산으로 평가해 추리는 과정)에 쓰려 한다. 분자 생성 모형은 목표로 하는 분자들의 범위에서 다양한 후보를 만들고, 원하는 성질을 조절하면서 유지할 특징을 보존하는 문제를 다룬다.[^drug]

### 계산과 기계학습을 이용한 발광 소재 설계

재료 연구 갈래는 넓은 화학 공간(가능한 분자 구조와 그 성질을 함께 다루는 범위)을 탐색해 새로운 물질을 설계한다. OLED 분자의 성질을 계산화학과 기계학습으로 이해하고, 원하는 물성을 갖추도록 컴퓨터를 이용한 설계 방법을 개발하는 것이 목표다.[^materials]

## 대표 논문

교수의 KAIST 재직 시기인 2025–2026년 논문과 사전 공개본에서 반응·구조 계산, 유기 발광 소재, 약물·생체 분자 인공지능을 다룬 7편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 사전 공개본은 발표처 칸에 표시했다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Riemannian denoising model for molecular structure optimization with chemical accuracy](https://doi.org/10.1038/s43588-025-00919-1) · Nature Computational Science[^p1] | 물리적인 에너지 성질을 반영한 좌표와 거리 기준으로 분자 구조를 조정하는 방법을 제안했다. 분자의 구조와 에너지 오차를 평가한 결과, 비교한 기존 방법보다 정확도가 나아졌다. 분자 에너지 변화에 맞는 좌표를 쓰는 계산 방법의 가능성을 제시한다. | 전체 4명 중 마지막 |
| 2 | 2026 | [A Comprehensive Dataset of Chemical Reactions Covering Second and Third Row Elements with Million-Scale Quantum Chemical Calculations](https://doi.org/10.1038/s41597-026-07325-w) · Scientific Data[^p2] | 반응물·생성물·전이 상태의 구조와 반응이 진행되는 동안의 분자 배치를 모은 Reaction-QM 자료집을 제시했다. 전이 상태와 반응 경로를 계산으로 검증했다. 기계학습 모형의 전이 상태 예측, 반응의 에너지 장벽 추정 등을 개발하고 평가할 자료로 제안한다. | 전체 7명 중 마지막 |
| 3 | 2026 | [Harnessing generative AI for efficient organic materials discovery in low-data regimes](https://doi.org/10.1039/D5DD00463B) · Digital Discovery[^p3] | 분자 조각에 기반한 생성 인공지능과 전자 구조 계산(물질 안 전자의 상태와 배치를 구하는 계산)을 결합해, 자료가 적은 조건에서 발광 소재를 찾는 방법을 제시했다. 설계한 녹색 발광체를 실험으로 검증했다. | 전체 8명 중 마지막 |
| 4 | 2026 | [Autonomous bioisosteric replacement for multi-property optimization in drug design](https://doi.org/10.1038/s41467-026-75512-9) · Nature Communications[^p4] | 분자의 생물학적 활성을 유지하면서 여러 성질을 조절하기 위해, 바꿀 분자 조각과 새로 넣을 조각을 스스로 선택하는 DeepBioisostere 모형을 제안했다. 실험에서 얻은 생물학적 활성 자료를 학습해 조각의 교체를 제안하며, 계산으로 후보 물질을 다듬는 사례에서 방법을 평가했다. | 전체 6명 중 마지막 |
| 5 | 2025 | [BInD: Bond and Interaction-Generating Diffusion Model for Multi-Objective Structure-Based Drug Design](https://doi.org/10.1002/advs.202502702) · Advanced Science[^p5] | BInD(Bond and Interaction-Generating Diffusion Model)는 분자와 표적 단백질 사이의 상호작용을 함께 생성하는 모형이다. 분자 각 부분의 원자 배치, 분자의 성질, 표적에 대한 상호작용을 함께 고려한다. 여러 목표를 평가했을 때 기존 방법과 비슷하거나 앞서는 성능을 보였다. 상호작용의 형태를 바탕으로 분자를 설계하고 다듬는 방법도 제안했다. | 마지막 저자·교신저자 |
| 6 | 2026 | [Elucidating enzyme–substrate specificity through co-folding foundation model](https://doi.org/10.64898/2026.07.30.741672) · bioRxiv, 사전 공개본[^p6] | 생체 분자 모형이 배운 구조 정보를 이용해 효소(생체 반응을 촉진하는 촉매)와 기질(효소 반응의 대상 물질)의 상호작용을 예측하는 Boltz2ESI 체계를 제안했다. 미리 결합 부위를 지정하지 않고도 구조 변화를 반영하며, 구조·진화·분자 모양 정보를 결합한다. 생물이 화합물을 만드는 경로에 관여할 효소 후보를 추리는 용도로도 평가했다. | 전체 9명 중 8번째 |
| 7 | 2026 | [Atom-level Protein Representation Learning Improves Protein Structure Prediction](https://doi.org/10.48550/arXiv.2605.22133) · arXiv:2605.22133v3, 사전 공개본[^p7] | 단백질의 아미노산 종류, 주된 연결 구조의 모양, 주변 원자 전체의 배치를 함께 배우는 TriProRep을 제안했다. 일부가 바뀐 자료에서 원래의 표현을 복원하도록 미리 학습시킨다. 단백질 표현을 구조 예측에 쓰는 평가 자료 RepSP도 제안했고, 복합체 구조와 상호작용 성질 등을 예측하는 과제에서 기존 표현 모형보다 나은 결과를 보였다. | 전체 9명 중 8번째 |

## 교수와 전문 분야

김우연(Woo Youn Kim)은 KAIST 화학과 교수다. 연구실 이력은 2011년부터 KAIST 화학과의 조교수·부교수·교수로 재직했다고 적는다. POSTECH에서 1997–2004년 화학 학사 과정을 마쳤으며 물리학을 복수전공했고, 2004–2009년 화학 박사 과정을 밟았다. 연구실 이력은 2009–2010년 Max-Planck-Institute of Microstructure Physics에서 박사후연구원으로 일했다고 적는다.[^faculty][^members]

연구실이 게시한 대외 경력은 2020년부터 HITS의 CEO·공동창업자, 2022년 3월–2024년 1월 한국제약바이오협회(KPBMA)의 Korea AI Center for Drug Discovery and Development 센터장, 2024년 1–3월 Convergence AI Institute for Drug Discovery 부원장이다.[^members]

전문 분야의 공통 축은 화학 지식과 계산을 인공지능 모형에 반영하는 방법이다. 반응 기작·합성 경로의 자동 탐색, 약물 후보와 단백질의 상호작용 예측, 발광 소재의 성질을 조절하는 설계가 연구실이 밝힌 세 갈래다.[^reaction][^drug][^materials] 최근 논문은 분자 구조 최적화와 반응 계산 자료, 발광 소재 설계, 약물 분자 생성 및 단백질의 구조 정보를 배우는 방법을 다룬다.[^p1][^p2][^p3][^p4][^p5][^p7] 여러 인공지능 행위자가 유전자 반응을 함께 추론하는 방법에도 참여했다.[^bioagent]

## 응용 분야

연구실이 직접 든 활용 대상은 화학반응의 예측과 합성 계획 자동화, 초기 신약 개발을 위한 후보 물질의 설계와 가상 평가, OLED 분자의 설계다.[^reaction][^drug][^materials]

## 구성원

2026년 11월 1일 연구실 Future & Present 쪽에 게시된 교수 외 구성원 14명이다. 시작 시기는 각 카드가 맨 앞에 적은 현재 과정·직위의 기간이다. 「대표 논문 참여」는 위 표의 번호이며, 이름 순서와 철자가 같은 전체 이름만 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정·직위 | 시작 | 연구 주제 | 게시 이력 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Kyunghoon Lee (이경훈) | 박사후연구원 | 2024 Mar. – | Automated reaction prediction method | 2024 Mar. –: Postdoc in KAIST, ICL; 2018 Sep. – 2024 Feb.: Ph.D. student in Chemistry, KAIST; 2014 – 2018 Aug.: B.S. in Mathematics (Chemistry, double major), KAIST | 2, 3 |
| Hyeong Woo Kim (김형우) | 박사후연구원 | 2026 | Reaction prediction method with AI | 2026: Postdoc in KAIST, ICL; 2020 Sept. –: Ph.D. student in Chemistry, KAIST; 2016 – 2020 Aug.: B.S. in Chemistry(Physics, minor), KAIST |  |
| Seokhyun Moon (문석현) | 박사후연구원 | 2026 Sept. – | Drug discovery with AI | 2026 Sept. –: Post Doc, Innocore AI; 2020 Sept. – 2026 Aug.: Ph.D. in Chemistry, KAIST; 2017 – 2020 Aug.: B.S. in Chemistry (Computer Science, minor), KAIST | 4 |
| Jun Hyeong Kim (김준형) | 박사과정 | 2021 – | Material design using deep learning | 2021 –: Ph.D. student in Chemistry, KAIST; 2016 – 2020: B.S. in Chemistry, KAIST | 1, 3 |
| Joongwon Lee (이중원) | 박사과정 | 2022 Sept. – | Drug discovery with AI | 2022 Sept. –: Ph.D. student in Chemistry, KAIST; 2017 – 2022 Aug.: B.S. in Chemistry (Chemical and Biomolecular Engineering, double major), KAIST | 5 |
| Seonghwan Seo (서성환) | 박사과정 | 2022 Sept. – | Drug discovery with AI | 2022 Sept. –: Ph.D. student in Chemistry, KAIST; 2018 – 2022 Aug.: B.S. in Chemistry (Computer Science, double major), KAIST | 6, 7 |
| Songmi Kim (김성미) | 박사후연구원 | 2023 Sept. – present | Computer-aided drug discovery | 2023 Sept. – present: Postdoc in KAIST, ICL; 2022 May – 2023 Aug.: Technician in KISTI Republic of Korea, VR/AR visualization team; 2017 Feb. – 2017 Sept.: Researcher, in BMDRC, Drug Discovery team, Yonsei University; 2014 – 2016: Research fellow (Postdoc) in KIAS, School of Computational Sciences, Seoul,; 2009 – 2014: Ph.D (Integrated M.S/Ph.D), Applied Life Science, Gyeongsang National University (Computational biology and Bioinformatics Lab, Supervisor: KW Lee; 2004 – 2008: B.S in Biochemistry, Gyeongsang National University |  |
| Shinwoo Kim (김신우) | 석박사통합과정 | 2024 Mar. – | Drug discovery with AI | 2024 Mar. –: M.S.-Ph.D Student in Chemistry, KAIST; 2019 Mar. – 2024 Feb.: B.S. in Chemistry(Computer Science, double major; Chemical and Biomolecular Engineering, minor), KAIST | 4 |
| Jisu Seo (서지수) | 석박사통합과정 | 2024 Mar. – | Molecule generation for drug design with AI | 2024 Mar. –: M.S.-Ph.D Student in Chemistry, KAIST; 2019 Mar. – 2024 Feb.: B.S. in Chemistry(Computer Science, minor), KAIST | 5 |
| Minha Park (박민하) | 박사과정 | 2025~ | Biomolecular representations, AI-driven molecular generation | 2025~: Ph.D. Student in Chemistry, KAIST Mar. – 2024 Feb.; 2019~2025: B.S. in Chemistry (Computer Science, minor; AI, Special Designated Major), KAIST |  |
| Minseong Park (박민성) | 박사과정 | 2025~ | Automated reaction-pathway exploration representations, AI-driven molecular generation | 2025~: Ph.D. Student in Chemistry, KAIST Mar. – 2024 Feb.; 2022~2025~2025: B.S. in Chemistry (Computer Science, double major), KAIST |  |
| Gyuho Jeon (전규호) | 석박사통합과정 | 2026~ | Drug discovery with AI | 2026~: M.S.-Ph.D. Student in Chemistry, KAIST; 2021~2025: B.S. in Chemistry (Computer Science, minor), SKKU |  |
| Eunyoung Cho (조은영) | 석사과정 | 2026~ | AI4Science | 2026~: M.S. Student in AX Department, KAIST; 2022~2026: B.S. in Biotechnology (Computer Science, double major), KU |  |
| Minkyung Shin (신민경) | 석사과정 | 2026. Sept. – | AI reasoning for therapeutic discovery | 2026. Sept. –: M.S. Student in AX; 2021. Mar. – 2026. Aug.: B.S. in Environmental Horticulture (Artificial Intelligence, double major), University of Seoul |  |

## 졸업생과 이전 구성원

2026년 11월 1일 Past 쪽의 21명이다. 박사후연구원·연구원·다른 연구실로 옮긴 학생도 포함한다. 학위·과정과 기간은 연구실 게시 표기다.[^alumni]

| 이름 | 학위·과정·연구 이력 | 랩이 적은 진로 | 연구 주제 | 게시 이력 |
|---|---|---|---|---|
| Jiyu Park (박지유) | 2022 – 2024 Feb.: Ph.D. student in Chemistry, ICL Team, KAIST; 2017 – 2021: B.S. in Chemistry (Chemical and Biomolecular Engineering, double major), KAIST | 2024 Mar.: Ph.D. student in Chemistry, BIOMIMETIC ORGANIC LAB, KAIST | Automated retrosynthetic analysis | 2024 Mar.: Ph.D. student in Chemistry, BIOMIMETIC ORGANIC LAB, KAIST; 2022 – 2024 Feb.: Ph.D. student in Chemistry, ICL Team, KAIST; 2017 – 2021: B.S. in Chemistry (Chemical and Biomolecular Engineering, double major), KAIST |
| Jin Woo Kim (김진우) | 2015 – 2020: Ph.D. student in Chemistry, KAIST; 2010 – 2014: B.S. in Chemistry (Mathematics, double major), KAIST | Present: Samsung, SAIT (Samsung Advanced Institute of Technology) | Automated reaction prediction method, machine learning | Present: Samsung, SAIT (Samsung Advanced Institute of Technology); 2015 – 2020: Ph.D. student in Chemistry, KAIST; 2010 – 2014: B.S. in Chemistry (Mathematics, double major), KAIST |
| Jaechang Lim (임재창) | 2020 Mar – 2020 July: Postdoc, Departement of Chemistry, Chemistry, KAIST; 2015 – 2020 Feb: Ph.D. student in Chemistry, KAIST; 2012 – 2015: B.S. Chemistry, KAIST | Present: Co-founder, HITS Inc. |  | Present: Co-founder, HITS Inc.; 2020 Mar – 2020 July: Postdoc, Departement of Chemistry, Chemistry, KAIST; 2019 Jan – 2019 Feb: Visiting researcher, Kakao Brain; 2016 Nov – 2017 Apr: Visiting student, Supercomputing Service Center, KISTI; 2015 – 2020 Feb: Ph.D. student in Chemistry, KAIST; 2012 – 2015: B.S. Chemistry, KAIST |
| Seongok Ryu (류성옥) | 2014 – 2020: Ph.D. in Chemistry, KAIST; 2009 – 2014: B.S. Chemistry (Physics, double major), KAIST | Present: Galux | Development of algorithms for geometry optimization of molecules, Machine learning | Present: Galux; 2020-2022: Research Scientist, AITRICS; 2014 – 2020: Ph.D. in Chemistry, KAIST; 2009 – 2014: B.S. Chemistry (Physics, double major), KAIST |
| Sang-Yeon Hwang (황상연) | 2014 – 2020: Ph.D. in Chemistry, KAIST; 2010 – 2014: B.S. Chemistry, Korea University | Present: HITS Inc. | Charge transfer theory; Machine learning | Present: HITS Inc.; 2020 – 2022: Staff Researcher, Samsung Advanced Institute of Technology; 2014 – 2020: Ph.D. in Chemistry, KAIST; 2010 – 2014: B.S. Chemistry, Korea University |
| Jeongeun Park (박정은) | 2019 – 2020: Ph.D student in Chemistry, KAIST; 2012 – 2016: Doctor of Pharmacy, Seoul National University; 2009 – 2011: Undergraduate in Chemistry, KAIST (2-year completion) | Present: BMS Korea | Drug discovery using deep learning | Present: BMS Korea; 2019 – 2020: Ph.D student in Chemistry, KAIST; 2012 – 2016: Doctor of Pharmacy, Seoul National University; 2009 – 2011: Undergraduate in Chemistry, KAIST (2-year completion) |
| Seung Hwan Hong (홍승환) | 2018 – 2019: Postdoc, Chemistry, KAIST; 2014 – 2017: Postdoc, Computational Sciences, Korea Institute for Advanced Study (advisor: Prof. Jooyoung Lee); 2009 – 2014: Ph.D. Physics, SungKyunKwan University (advisor: Prof. Han-Yong Choi); 2007 – 2009: M.S. Physics, SungKyunKwan University (advisor: Prof. Han-Yong Choi); 2003 – 2007: B.S. Physics, SungKyunKwan University | Present: Research Scientist, AItrics | Machine learning, Bioinformatics, Protein-ligand binding affinity | Present: Research Scientist, AItrics; 2019 – 2020: Senior Researcher, Arontier; 2018 – 2019: Postdoc, Chemistry, KAIST; 2014 – 2017: Postdoc, Computational Sciences, Korea Institute for Advanced Study (advisor: Prof. Jooyoung Lee); 2009 – 2014: Ph.D. Physics, SungKyunKwan University (advisor: Prof. Han-Yong Choi); 2007 – 2009: M.S. Physics, SungKyunKwan University (advisor: Prof. Han-Yong Choi); 2003 – 2007: B.S. Physics, SungKyunKwan University |
| Kyung Yup Baek (백경엽) | 2015 – 2019: Postdoc, Chemistry, KAIST; 2014 – 2015: Postdoc, Chemistry, Sungkyunkwan Univ. (advisor: Prof. Jin Young Lee); 2004 – 2014: Ph.D. Chemistry, Seoul National Univ. (advisor: Prof. Seong Keun Kim); 2000 – 2002: M.Sc. Chemistry, Seoul National Univ. (advisor: Prof. Do Yeung Yoon); 1993 – 1999: B.S. Chemistry, Korea Univ. | Present: Postdoc, Chemistry, Chung-Ang Univ. (advisor: Prof. Hye Ran Kho) | Theoretical investigation on CO2 conversion for highly valuable chemical feedstocks, Reaction dynamics of hydrated biomolecules using MM/QM calculations | Present: Postdoc, Chemistry, Chung-Ang Univ. (advisor: Prof. Hye Ran Kho); 2015 – 2019: Postdoc, Chemistry, KAIST; 2014 – 2015: Postdoc, Chemistry, Sungkyunkwan Univ. (advisor: Prof. Jin Young Lee); 2004 – 2014: Ph.D. Chemistry, Seoul National Univ. (advisor: Prof. Seong Keun Kim); 2006 – 2010: Visiting Researcher, National Taiwan Univ. (advisor: Prof. S. H. Lin and Prof. Y. Fujimura); 2000 – 2002: M.Sc. Chemistry, Seoul National Univ. (advisor: Prof. Do Yeung Yoon); 1993 – 1999: B.S. Chemistry, Korea Univ. |
| Yeonjoon Kim (김연준) | 2018 Jun. – 2023 Aug: Postdoc, National Renewable Energy Lab (NREL), CO, US; 2018 Feb. – 2018 Jun.: Postdoc, KAIST; 2008 Feb. – 2012 Feb.: B.S. Chemistry, KAIST | Present: Assistant Professor, Chemistry, Pukyung National University | Automated prediction of reaction paths, Cheminformatics, Chemical graph theory | Present: Assistant Professor, Chemistry, Pukyung National University; 2018 Jun. – 2023 Aug: Postdoc, National Renewable Energy Lab (NREL), CO, US; 2018 Feb. – 2018 Jun.: Postdoc, KAIST; 2008 Feb. – 2012 Feb.: B.S. Chemistry, KAIST |
| Zeehyo Kim (김지효) | 2016 Mar. – 2018 Feb.: M.Sc. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2011 – 2016: B.S. Computer (Chemistry, double major), Korea Univ. | Present: M.Sc. student, GSCT, KAIST (Motion computing laboratory) |  | Present: M.Sc. student, GSCT, KAIST (Motion computing laboratory); 2016 Mar. – 2018 Feb.: M.Sc. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2011 – 2016: B.S. Computer (Chemistry, double major), Korea Univ. |
| Sunghwan Choi (최성환) | 2012 Feb. – 2017 Aug.: Ph.D. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2009 – 2012: B.S. Chemistry, KAIST | 2024 Mar. –: Assistant Professor, Dept. of Chemistry, Inha University |  | 2024 Mar. –: Assistant Professor, Dept. of Chemistry, Inha University; 2017 Sep. – 2024 Feb.: Senior Researcher, Supercomputing Service Center, KISTI; 2012 Feb. – 2017 Aug.: Ph.D. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2016 Jun.- 2016 Aug.: Visiting student, MANA, NIMS (advisor: Dr. T. Miyajaki); 2015 Apr. – 2016 Mar.: Visiting student, Supercomputing Service Center, KISTI; 2009 – 2012: B.S. Chemistry, KAIST |
| Kwangwoo Hong (홍광우) | 2011 – 2016: Ph.D. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2007 – 2011: B.S. Chemistry, KAIST | Present: Samsung Display |  | Present: Samsung Display; 2016 – 2022: IPS Patent Corporation; 2011 – 2016: Ph.D. Chemistry, KAIST (advisor: Prof. Woo Youn Kim); 2007 – 2011: B.S. Chemistry, KAIST |
| Seihwan Ahn (안세환) | 2015 – 2019: Ph.D. student at Mookie Baik’s group, Department of Chemistry, KAIST; 2012 – 2015: Ph.D. student, Department of Chemistry, KAIST; 2006 – 2012: B.S. Chemistry, KNU | Present: Samsung display |  | Present: Samsung display; 2015 – 2019: Ph.D. student at Mookie Baik’s group, Department of Chemistry, KAIST; 2012 – 2015: Ph.D. student, Department of Chemistry, KAIST; 2006 – 2012: B.S. Chemistry, KNU |
| Wonho Zhung (정원호) | 2020 Sept. –: Ph.D. student in Chemistry, KAIST; 2016 – 2020 Aug.: B.S. in Chemistry(Biology, double major), KAIST | 2026: Researcher, HITS | Predicting drug-target interaction using deep learning | 2026: Researcher, HITS; 2020 Sept. –: Ph.D. student in Chemistry, KAIST; 2016 – 2020 Aug.: B.S. in Chemistry(Biology, double major), KAIST |
| Yoonsoo Jung (정윤수) | 2019 – 2022: Research associate, KAIST; 2011 – 2013: M.Sc. in Material Science & Engineering, Seoul National Univ. (advisor : Prof. Cheol Seong Hwang); 2005 – 2011: B.S. in Material Science & Engineering, Seoul National Univ. | 2023-: Hyosung |  | 2023-: Hyosung; 2019 – 2022: Research associate, KAIST; 2013 – 2019: Researcher, LG Chem.; 2011 – 2013: M.Sc. in Material Science & Engineering, Seoul National Univ. (advisor : Prof. Cheol Seong Hwang); 2005 – 2011: B.S. in Material Science & Engineering, Seoul National Univ. |
| Seonghwan Kim (김성환) | 2019 Sept. –: Ph.D. student in Chemistry, KAIST; 2013 – 2019: B.S. in Chemical and Biomolecular Engineering (Mathematics, double major), KAIST | 2025: Postdoc. AI-CRED | Algorithms and Machine learning for elucidating reaction network | 2025: Postdoc. AI-CRED; 2019 Sept. –: Ph.D. student in Chemistry, KAIST; 2013 – 2019: B.S. in Chemical and Biomolecular Engineering (Mathematics, double major), KAIST |
| Jeheon Woo (우제헌) | 2019 – 2025: Ph.D. in Chemistry, KAIST; 2015 – 2019: B.S. Chemistry (Physics, double major), HYU | 2025-: Postdoc., KISTI | Density functional theory, AI for science | 2025-: Postdoc., KISTI; 2019 – 2025: Ph.D. in Chemistry, KAIST; 2015 – 2019: B.S. Chemistry (Physics, double major), HYU |
| YongJun Kim (김용준) | 2025: Ph.D. in Chemistry, KAIST; 2019 –: Ph.D. student in Chemistry, KAIST; 2014 – 2019: B.S. in Chemistry, KAIST |  | Catalyst design, Development of Computer Software for DFT. | 2025: Ph.D. in Chemistry, KAIST; 2019 –: Ph.D. student in Chemistry, KAIST; 2014 – 2019: B.S. in Chemistry, KAIST |
| Hyeonsu Kim (김현수) | 2018 – 2024 03.: Ph.D. student in Chemistry, KAIST; 2013 – 2018: B.S. in Chemistry, KAIST | 2024 03. –: Senior research scientist, Samsung SDI | Catalyst design, Development of Computer Software for DFT. | 2024 03. –: Senior research scientist, Samsung SDI; 2018 – 2024 03.: Ph.D. student in Chemistry, KAIST; 2013 – 2018: B.S. in Chemistry, KAIST |
| Sungwoo Kang (강성우) | 2020 Sept. – 2022 Oct.: Postdoc, Departement of Chemistry, Chemistry, KAIST; 2015 – 2020 Aug.: Ph.D. student in Chemistry, KAIST; 2010 – 2015: B.S. Chemistry (Physics, double major), KAIST | Present: Samsung Electronics | Quantum Embedding Theory | Present: Samsung Electronics; 2020 Sept. – 2022 Oct.: Postdoc, Departement of Chemistry, Chemistry, KAIST; 2015 – 2020 Aug.: Ph.D. student in Chemistry, KAIST; 2010 – 2015: B.S. Chemistry (Physics, double major), KAIST |
| Jaewook Kim (김재욱) | 2019 – 2023.Aug: Present Postdoc, Departement of Chemistry, Chemistry, KAIST; 2013 – 2019: Ph.D. in Chemistry, KAIST (Advisor: Woo Youn Kim); 2009 – 2013: B.S. Chemistry (Physics, double major), KAIST | 2023 – Present: Senior Researcher, KISTI | Self-interaction correction, Excited-state calculation, Organic electronic material design. | 2023 – Present: Senior Researcher, KISTI; 2019 – 2023.Aug: Present Postdoc, Departement of Chemistry, Chemistry, KAIST; 2018: Visiting student, Departement of Chemistry, Duke University (Advisor: Weitao Yang); 2013 – 2019: Ph.D. in Chemistry, KAIST (Advisor: Woo Youn Kim); 2009 – 2013: B.S. Chemistry (Physics, double major), KAIST |

## 최근 논문 목록 (2021–2026)과 연도 표기 없는 항목

화학반응 계산과 합성 경로, 유기 소재와 분자 생성, 전자 구조 계산, 약물·생체 분자 인공지능을 다룬 논문과 원고다. 연구실 전체 논문 목록의 Published·Preprints 항목 중 2021–2026년 47편과 발표 연도를 확정하지 않은 TacoGFN 1편을 나누어 실었다. TacoGFN의 발표처는 「연구실 기재」로 표시했다. 연도만 적힌 2021년 항목은 해당 연도에 두고, 정확한 출판일이 기준 기간 전인 항목은 포함하지 않는다. BInD의 연도는 출판사 날짜, GeoTMI의 연도는 연구실의 NeurIPS 2023 소식에 따른다. 등록 서지로 연도를 확인한 항목은 온라인 출판일을 기준으로 두었다. 사전 공개본은 발표처 뒤에 표시했다. 제목·저자·발표처와 저자 뒤의 기호는 연구실 게시 표기다. PIGNet의 +는 원문이 equal contribution이라고 설명한다.[^papers][^bind][^news][^bibdates]

**2026**

- Yinhua Piao, Hyomin Kim, Seonghwan Kim, Yunhak Oh, Junhyeok Jeon, Sang-Yeon Hwang, Jaechang Lim, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn · "Learning Adaptive Perturbation-Conditioned Contexts for Robust Transcriptional Response Prediction" · *ICML 2026, PMLR 306:98696–98729*
- Hyeongwoo Kim+, Seokhyun Moon+, Wonho Zhung, Shinwoo Kim, Jaechang Lim, Woo Youn Kim\* · "Autonomous bioisosteric replacement for multi-property optimization in drug design" · *Nature Communications (2026)* DOI: <https://doi.org/10.1038/s41467-026-75512-9>.
- Minha Park, Shinwoo Kim, Seokhyun Moon, Hyeongwoo Kim, Gyuho Jeon, Woo Youn Kim · "How Do Co-folding Models Organize Structural Information?" · *GenBio 2026 (ICML 2026) Poster*
- Kyunghoon Lee+, Sungwoo Kang+, Beomgyu Kang+, Won-Joon Son, Seungmin Lee, Dae Sin Kim, Woo Youn Kim\* · "A Comprehensive Dataset of Chemical Reactions Covering Second and Third Row Elements with Million-Scale Quantum Chemical Calculations" · *Scientific Data 13(1), 983 (2026)* DOI: <https://doi.org/10.1038/s41597-026-07325-w>.
- Jun Hyeong Kim+, Kyunghoon Lee+, Hyeonsu Kim, MinSoo Kang, Suk-Ku Chang, Yinglan Jin, Dongwook Kim\*, Woo Youn Kim\* · "Harnessing generative AI for efficient organic materials discovery in low-data regimes" · *Digital Discovery (2026)* DOI: <https://doi.org/10.1039/D5DD00463B>.
- Seongrok Heo+, Minhae Cha+, Wonho Zhung+, JiMin Kim, Sirisuk Keereewan, Illhwan Cho, MinSeol Park, Wonbin Seo, Heewon Shin, Soljee Yoon, Suhyun Ye, Jae-Kyung Heo, Hayoung Hwang, Woo Youn Kim\*, YoungSoo Kim\*, Sunkyu Han\* · "Synthesis of 3-desoxycollinoketone B and its ability to reduce Alzheimer-associated misfolded proteins" · *Nature Communications (2026)* DOI: <https://doi.org/10.1038/s41467-026-69662-z>.
- Joongwon Lee, Seonghwan Kim, Seokhyun Moon, Hyunwoo Kim, Woo Youn Kim · "FragFM: Hierarchical Framework for Efficient Molecule Generation via Fragment-Level Discrete Flow Matching" · *ICLR 2026 Poster*
- Jeheon Woo+, Seonghwan Kim+, Jun Hyeong Kim, Woo Youn Kim\* · "Riemannian denoising model for molecular structure optimization with chemical accuracy" · *Nature Computational Science 6(2), 134-144 (2026)* DOI: <https://doi.org/10.1038/s43588-025-00919-1>.
- Hyomin Kim, Sang-Yeon Hwang, Jaechang Lim, Yinhua Piao, Yunhak Oh, Woo Youn Kim, Chanyoung Park, Sungsoo Ahn, Junhyeok Jeon · "Progressive Multi-Agent Reasoning for Biological Perturbation Prediction" · *arXiv:2602.07408 (2026) (사전 공개본)*
- Xiwei Cheng, Seonghwan Seo, Charlie Huh, Jihang Chen, Songlin Jiang, Pengkang Guo, Jing-Ke Weng, Woo Youn Kim\*, Wengong Jin · "Elucidating enzyme–substrate specificity through co-folding foundation model" · *bioRxiv, 2026.07.30.741672 (사전 공개본)* DOI: <https://doi.org/10.64898/2026.07.30.741672>.
- Taewon Kim+, Hyosoon Jang+, Hyunjin Seo, Seonghwan Seo, Hyeongwoo Kim, Wonho Zhung, Mingyeong Shin, Wooyoun Kim\*, Sungsoo Ahn · "Atom-level Protein Representation Learning Improves Protein Structure Prediction" · *arXiv:2605.22133 (사전 공개본)*

**2025**

- Yongjun Kim, Jaewook Kim\*, Woo Youn Kim\* · "Engineering Excited States of Pt-Based Deep-Blue Phosphors to Enhance OLED Stability" · *ACS Omega 10(46), 56753-56762 (2025)* DOI: <https://doi.org/10.1021/acsomega.5c09501>.
- Kyunghoon Lee, Shinyoung Park, Minseong Park, Woo Youn Kim\* · "MetalloGen: Automated 3D Conformer Generation for Diverse Coordination Complexes" · *Journal of Chemical Information and Modeling 65(21), 11878-11891 (2025)* DOI: <https://doi.org/10.1021/acs.jcim.5c02074>.
- Joongwon Lee+, Wonho Zhung+, Jisu Seo, Woo Youn Kim\* · "BInD: Bond and Interaction-Generating Diffusion Model for Multi-Objective Structure-Based Drug Design" · *Advanced Science* DOI: <https://doi.org/10.1002/advs.202502702>.
- Tony Shen+, Seonghwan Seo+, Ross Irwin , Kieran Didi, Simon Olsson, Woo Youn Kim, Martin Ester\* · "Compositional Flows for 3D Molecule and Synthesis Pathway Co-design" · *ICML 2025*
- Yongjun Kim+, Yeonjoon Kim+, Hyeonsu Kim, Sungwoo Kang, Jaewook Kim, Kyunghoon Lee, Wook Jeong, Won Jong Lee, Ho Ryu, Kyungwoo Kim, Woo Youn Kim\* · "Machine-Learning-Based Design of Metallocene Catalysts for Controlled Olefin Copolymerization" · *Chem. Eur. J. 2025, 0, e202500316* DOI: <https://doi.org/10.1002/chem.202500316>.
- Jiyeon Han, Wonho Zhung, Insoo Jang, Joongwon Lee, Min Ji Kang, Timothy Dain Lee, Seung Jun Kwack, Kyu-Bong Kim, Daehee Hwang, Byungwook Lee, Hyung Sik Kim, Woo Youn Kim\* & Sanghyuk Lee · "HepatoToxicity Portal (HTP): an integrated database of drug-induced hepatotoxicity knowledgebase and graph neural network-based prediction model" · *J Cheminform 17, 48 2025* DOI: <https://doi.org/10.1186/s13321-025-00992-8>.
- Kyunghoon Lee+, Jinwon Lee+, Shinyoung Park+, and Woo Youn Kim\* · "Facilitating Transition State Search with Minimal Conformational Sampling Using Reaction Graph" · *J. Chem. Theory Comput. 2025, 21, 5, 2487–2500* DOI: <https://doi.org/10.1021/acs.jctc.4c01692>.
- Kiyoung Seong, Seonghyun Park, Seonghwan Kim, Woo Youn Kim\*, and Sungsoo Ahn\* · "Transition Path Sampling with Improved Off-Policy Training of Diffusion Path Samplers" · *ICLR 2025*
- Jun Hyeong Kim+, Seonghwan Kim+, Seokhyun Moon+, Hyeongwoo Kim+, Jeheon Woo+, and Woo Youn Kim\* · "Discrete Diffusion Schrödinger Bridge Matching for Graph Transformation" · *ICLR 2025*
- Seonghwan Seo\*, Minsu Kim, Tony Shen, Martin Ester, Jinkyoo Park, Sungsoo Ahn, and Woo Youn Kim\* · "Generative Flows on Synthetic Pathway for Drug Design" · *ICLR 2025*

**2024**

- Seonghwan Seo and Woo Youn Kim\* · "PharmacoNet: deep learning-guided pharmacophore modeling for ultra-large-scale virtual screening" · *Chem. Sci., 2024,15, 19473-19487*
- Jeheon Woo, Woo Youn Kim\*, and Sunghwan Choi\* · "Efficient Shift-and-Invert Preconditioning for Multi-GPU Accelerated Density Functional Calculations" · *J. Chem. Theory Comput. 2024, 20, 17, 7443–7452* DOI: <https://doi.org/10.1021/acs.jctc.4c00721>.
- Kiyoung Seong\*, Seonghyun Park\*, Seonghwan Kim\*, Woo Youn Kim\*, and Sungsoo Ahn\* · "Collective Variable Free Transition Path Sampling with Generative Flow Network" · *ICML2024 Workshop Structured Probabilistic Inference & Generative Modeling*
- Joongwon Lee+, Wonho Zhung+, and Woo Youn Kim\* · "NCIDiff: Non-covalent Interaction-generative Diffusion Model for Improving Reliability of 3D Molecule Generation Inside Protein Pocket" · *ICML2024 Workshop AI4Science*
- Hyeonsu Kim+, Kyunghoon Lee+, Jun Hyeong Kim, and Woo Youn Kim\* · "Deep Learning-Based Chemical Similarity for Accelerated Organic Light-Emitting Diode Materials Discovery" · *J. Chem. Inf. Model. 2024, 64, 3, 677–689* DOI: <https://doi.org/10.1021/acs.jcim.3c01747>.
- Wonho Zhung+, Hyeongwoo Kim+ & Woo Youn Kim\* · "3D molecular generative framework for interaction-guided drug design" · *Nature Communications 15.1 (2024): 2688.*
- Seokhyun Moon+, Wonho Zhung+ & Woo Youn Kim \* · "Toward generalizable structure-based deep learning models for protein–ligand interaction prediction: Challenges and strategies" · *WIREs Comput Mol Sci.2024;14:e1705.* DOI: <https://doi.org/10.1002/wcms.1705>.
- Seonghwan Kim+, Jeheon Woo+, & Woo Youn Kim\* · "Diffusion-based Generative AI for Exploring Transition States from 2D Molecular Graphs" · *Nature Communications 15.1 (2024): 341.*
- Seoin Back, Alan Aspuru-Guzik, Michele Ceriotti, Ganna Gryn’ova, Bartosz Andrzej Grzybowski, Geun Ho Gu, Jason E Hein, Kedar Hippalgaonkar, Rodrigo Hormazabal, Yousung Jung, Seonah Kim, Woo Youn Kim, Mohamed Moosavi, Juhwan Noh, Changyoung Park, Joshua Schrier, Philipp Schwaller, Koji Tsuda, Tejs Vegge, Anatole von Lilienfeld, Aron Walsh · "Accelerated Chemical Science with AI" · *Digital Discovery* DOI: <https://doi.org/10.1039/d3dd00213f>.
- Seokhyun Moon, Sang-Yeon Hwang, Jaechang Lim, Woo Youn Kim · "PIGNet2: a versatile deep learning-based protein–ligand interaction prediction model for binding affinity scoring and virtual screening" · *Digital Discovery, 2024, 3, 287-299*

**2023**

- Jaewook Kim, Joonghyuk Kim, Yongjun Kim, Youngmok Son, Youngsik Shin, Hye Jin Bae, Ji Whan Kim, Sungho Nam, Yongsik Jung, Hyeonsu Kim, Sungwoo Kang, Yoonsoo Jung, Kyunghoon Lee, Hyeonho Choi, Woo Youn Kim\* · "Critical role of electrons in the short lifetime of blue OLEDs" · *Nature Communications 14, 7508 (2023).*
- Seonghwan Seo, Woo Youn Kim\* · "PharmacoNet: Accelerating Large-Scale Virtual Screening by Deep Pharmacophore Modeling" · *NeurIPS 2023 Workshop on New Frontiers of AI for Drug Discovery and Development*
- Hyeonsu Kim+, Jeheon Woo+, SEONGHWAN KIM+, Seokhyun Moon+, Jun Hyeong Kim+, Woo Youn Kim\* · "GeoTMI: Predicting Quantum Chemical Property with Easy-to-Obtain Geometry via Positional Denoising" · *Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS)*
- Hyeongwoo Kim+, Kyunghoon Lee+, Chansu Kim, Jaechang Lim, and Woo Youn Kim\* · "DFRscore: Deep Learning-Based Scoring of Synthetic Complexity with Drug-Focused Retrosynthetic Analysis for High-Throughput Virtual Screening" · *Journal of Chemical Information and Modeling* DOI: <https://doi.org/10.1021/acs.jcim.3c01134>.
- Kyunghoon Lee, Jun Hyeong Kim, Woo Youn Kim\* · "pyMCD: Python package for searching transition states via the multicoordinate driven method" · *Computer Physics Communications, Volume 291, October 2023, 108831* DOI: <https://doi.org/10.1016/j.cpc.2023.108831>.
- Jeheon Woo, Seonghwan Kim, and Woo Youn Kim\* · "Gaussian-Approximated Poisson Preconditioner for Iterative Diagonalization in Real-Space Density Functional Theory" · *J. Phys. Chem. A 2023, 127, 17, 3883–3893* DOI: <https://doi.org/10.1021/acs.jpca.2c09111>.
- Jeheon Woo, Seonghwan Kim, and Woo Youn Kim\* · "Dynamic Precision Approach for Accelerating Large-Scale Eigenvalue Solvers in Electronic Structure Calculations on Graphics Processing Units" · *J. Chem. Theory Comput. 2023, 19, 5, 1457–1465* DOI: <https://doi.org/10.1021/acs.jctc.2c00983>.
- Seonghwan Seo, Jaechang Lim\*, Woo Youn Kim\* · "Molecular Generative Model via Retrosynthetically Prepared Chemical Building Block Assembly" · *Advanced Science, 10.1002/advs.202206674* DOI: <https://doi.org/10.1002/advs.202206674>.

**2022**

- Jun Hyeong Kim, Hyeonsu Kim, Woo Youn Kim · "Effect of molecular representation on deep learning performance for prediction of molecular electronic properties" · *Volume43, Issue5 May 2022 Pages 645-649* DOI: <https://doi.org/10.1002/bkcs.12516>.
- Jeheon Woo, Hyeonsu Kim, and Woo Youn Kim · "Neural network-based pseudopotential: development of a transferable local pseudopotential" · *Phys. Chem. Chem. Phys., 2022, Advance Article*
- SUNGHO JEON, SANG-YEONHWANG, JIMCISTON, KAREN C.BUSTILLO, BRYAN W.REED, SUKJOONHONG, ALEXZETTL, WOOYOUN KIM, PETERERCIUS, JUNGWONPARK, AND WON CHULLEE · "Response to Comment on “Reversible disorder-order transitions in atomic crystal nucleation”" · *SCIENCE, 25 Mar 2022, Vol 375, Issue 6587, DOI: 10.1126/science.abj3683* DOI: <https://doi.org/10.1126/science.abj3683>.
- Woo, Jeheon; Kim, Woo Youn\*; Choi, Sunghwan\* · "System-Specific Separable Basis based on Tucker Decomposition: Application to Density Functional Calculations" · *J. Chem. Theory Comput. 2022, 18, 5, 2875–2884* DOI: <https://doi.org/10.1021/acs.jctc.1c01263>.
- Seokhyun Moon,+ Wonho Zhung,+ Soojung Yang,+ Jaechang Lim and Woo Youn Kim∗ +equal contribution · "PIGNet: A physics-informed deep learning model toward generalized drug-target interaction predictions" · *Chem. Sci., 2022,13, 3661-3673* DOI: <https://doi.org/10.1039/D1SC06946B>.
- Kyunghoon Lee, Jinho Jang, Seonghwan Seo, Jaechang Lim, and Woo Youn Kim · "Drug-likeness scoring based on unsupervised learning" · *Chem. Sci., 2022,13, 554-565*
- Jun Su Kang, Sungwoo Kang, Jong-Min Suh, Soon Mo Park, Dong Ki Yoon, Mi Hee Lim, Woo Youn Kim, and Myungeun Seo\* · "Circularly Polarized Light can Override and Amplify Molecular Chirality in Supramolecular Helices" · *J. Am. Chem. Soc. 2022, 144, 6, 2657–2666* DOI: <https://doi.org/10.1021/jacs.1c11306>.

**2021**

- Byung-Chang Oh, Eunyoung Yoon, Jintaek Gong, Jaewook Kim, Russell W. Driver, Yongjun Kim, Woo Youn Kim, and Hee-Seung Lee\* · "Morphology Transformation of Foldamer Assemblies Triggered by Single Oxygen Atom on Critical Residue Switch" · *small 2021, 2102525, Doi: 10.1002/smll.202102525* DOI: <https://doi.org/10.1002/smll.202102525>.

**연도 표기 없음**

- Tony Shen\*, Seonghwan Seo, Grayson Lee, Mohit Pandey, Jason R Smith, Artem Cherkasov, Woo Youn Kim, and Martin Ester\* · "TacoGFN: Target-conditioned GFlowNet for Structure-based Drug Design" · *TMLR* (연구실 기재)

## 수상과 선정

2022년 4월 대한화학회 학술발표회와 11월 8일 Samsung AI Challenge 시상식에서 알린 성과 2건이다. 대한화학회 수상의 날짜는 글에 적힌 학술발표회 기간이다.[^news][^news2]

- 2022-11-08 · 김현수·김성환·김준형 팀이 Samsung AI Challenge 2022의 Materials Discovery 주제에서 2등을 차지했다.
- 2022-04-13–2022-04-15 · 김형우가 대한화학회 제129회 학술발표회에서 합성 단계 수 예측을 주제로 포스터를 발표하고 우수 포스터상을 받았다.

## 소식

2023년 2월–2025년 12월의 학회 활동 소식 7건이다. 날짜는 글에 적힌 행사 기간이다.[^news]

- 2025-12-02–2025-12-07 · 김준형·문석현·김성환·서지수가 샌디에고 NeurIPS 2025에서 포스터 발표로 참석했다.
- 2025-04-24–2025-04-28 · 김준형·김성환·문석현·김형우·서성환이 싱가포르 ICLR 2025에서 포스터 발표로 참석했다.
- 2025-04-21–2025-04-25 · 문석현·정원호와 이경훈이 고베 APATCC 2025에서 포스터 발표로 참석했다.
- 2024-12-11–2024-12-17 · 김준형·김성환·문석현·우제헌·서성환이 밴쿠버 NeurIPS 2024에 참석했다. 연구실은 AI for new drug modalities 워크숍에서 포스터를 발표했다.
- 2023-12-10–2023-12-15 · 김우연과 문석현·김준형·김현수·김성환·우제헌·서성환이 뉴올리언스 NeurIPS 2023에 참석했다. 연구실은 본 학회와 신약 개발 AI 워크숍에서 포스터를 발표했다.
- 2023-08-21–2023-08-25 · 문석현·서성환·이중원이 토론토 Accelerate Conference 2023의 재료 주제에 포스터 발표로 참석했다.
- 2023-02-19–2023-02-23 · 김우연·정원호·문석현이 APATCC-10의 기계학습 세션에 참석했다. 김우연·정원호는 구두 발표를, 문석현은 포스터 발표를 했다.

## 연락과 위치

- 주소: Department of Chemistry, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 전화: +82-42-350-2815[^home]
- 연구실 전화: +82-42-350-2855[^home]
- 팩스: +82-42-350-2810[^home]

## 각주
[^home]: 연구실 첫 화면. <https://wooyoun.kaist.ac.kr/> 물리 법칙을 바탕으로 하는 계산화학과 인공지능을 결합하며, 약물·OLED 분자 설계와 반응 예측 도구를 개발한다고 소개한다. 관측일 2026-11-01.
[^faculty]: KAIST 화학과 교수 소개 쪽. <https://chem.kaist.ac.kr/faculty/view/id/13> 김우연 교수, Intelligent Chemistry Lab. 연구 분야는 반응·약물·소재 발견이다. 관측일 2026-11-01.
[^members]: 연구실 Future & Present. <https://wooyoun.kaist.ac.kr/our-family-future/> 교수의 학력·경력, 현재 구성원의 과정·기간·연구 주제. 관측일 2026-11-01.
[^alumni]: 연구실 Past. <https://wooyoun.kaist.ac.kr/our-family-past/> 이전 구성원의 과정·기간·연구 주제와 진로. 관측일 2026-11-01.
[^papers]: 연구실 Our Research paper. <https://wooyoun.kaist.ac.kr/our-research-paper/> Published·Preprints·Books & Chapters·Patents 목록. 관측일 2026-11-01.
[^reaction]: 연구실 Intelligent Reaction Discovery. <https://wooyoun.kaist.ac.kr/intelligent-reaction-discovery/> ACE-Reaction의 반응 기작 탐색, 전이 상태 탐색의 자동화와 반응성 예측, 기계학습을 통한 합성 계획 도구의 개발. 관측일 2026-11-01.
[^drug]: 연구실 Intelligent Drug Discovery. <https://wooyoun.kaist.ac.kr/intelligent-drug-discovery/> 입체 구조를 이용하는 약물 후보 설계용 딥러닝 모형을 개발하며, 화학 지식을 모형 구조에 넣어 일반화와 해석 가능성을 얻는 것을 목표로 한다. 단백질과 후보 물질의 원자 쌍 에너지로 상호작용을 예측하고 분자 생성 모형을 연구한다. 관측일 2026-11-01.
[^materials]: 연구실 Intelligent Materials Discovery. <https://wooyoun.kaist.ac.kr/intelligent-materials-discovery/> 계산화학과 기계학습으로 새로운 소재의 성질을 이해하고, OLED 분자가 원하는 성질을 갖도록 컴퓨터를 이용한 설계 방법을 개발한다. 관측일 2026-11-01.
[^news]: 연구실 News & Event. <https://wooyoun.kaist.ac.kr/news-event/> 학회 활동과 Samsung AI Challenge 2022 수상 소식. 관측일 2026-11-01.
[^news2]: 연구실 News & Event 2쪽. <https://wooyoun.kaist.ac.kr/news-event/2/> 김형우의 대한화학회 우수 포스터상과 이전 소식. 관측일 2026-11-01.
[^bind]: BInD 출판사 논문 쪽. <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202502702> First published: 11 July 2025. 전체 저자·KAIST 소속·Woo Youn Kim의 Corresponding Author 표기와 초록. 관측일 2026-11-01.
[^bibdates]: Crossref 등록 서지. <https://api.crossref.org/works/10.1039/d3dd00213f> 온라인 출판 기준으로 Accelerated Chemical Science with AI는 2024년이다. DFRscore는 2023-08-31(인쇄 2024-04-08), Molecular Generative Model via Retrosynthetically Prepared Chemical Building Block Assembly는 2023-01-03(인쇄 2023-03)이다. <https://api.crossref.org/works/10.1021/acs.jcim.3c01134> <https://api.crossref.org/works/10.1002/advs.202206674> 관측일 2026-11-01.
[^p1]: J. Woo, S. Kim, J. H. Kim, W. Y. Kim, Nature Computational Science 6, 134–144 (2026). <https://doi.org/10.1038/s43588-025-00919-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-69662-z%7C10.1038/s41467-026-75512-9%7C10.1038/s41597-026-07325-w%7C10.1038/s43588-025-00919-1%7C10.1039/d5dd00463b%7C10.64898/2026.07.30.741672>. 관측일 2026-11-01.
[^p2]: K. Lee 외, W. Y. Kim, Scientific Data 13, 983 (2026). <https://doi.org/10.1038/s41597-026-07325-w> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1038/s41467-026-69662-z%7C10.1038/s41467-026-75512-9%7C10.1038/s41597-026-07325-w%7C10.1038/s43588-025-00919-1%7C10.1039/d5dd00463b%7C10.64898/2026.07.30.741672>. 관측일 2026-11-01.
[^p3]: J. H. Kim 외, W. Y. Kim, Digital Discovery (2026). <https://doi.org/10.1039/D5DD00463B> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1039/D5DD00463B>. 관측일 2026-11-01.
[^p4]: H. Kim 외, W. Y. Kim, Nature Communications (2026). <https://doi.org/10.1038/s41467-026-75512-9> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1038/s41467-026-75512-9>. 관측일 2026-11-01.
[^p5]: J. Lee, W. Zhung, J. Seo, W. Y. Kim, Advanced Science 12, e02702 (온라인 2025-07-11). <https://doi.org/10.1002/advs.202502702> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202502702>. 관측일 2026-11-01.
[^p6]: X. Cheng 외, W. Jin, bioRxiv (Cold Spring Harbor Laboratory) (2026). <https://doi.org/10.64898/2026.07.30.741672> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.64898/2026.07.30.741672>. 관측일 2026-11-01.
[^p7]: T. Kim 외, S. Ahn, arXiv:2605.22133v3 (사전 공개본) (온라인 2026-05-21). <https://doi.org/10.48550/arXiv.2605.22133> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.22133>. 관측일 2026-11-01.
[^bioagent]: H. Kim 외, J. Jeon, arXiv:2602.07408v2 (사전 공개본) (온라인 2026-02-07). <https://doi.org/10.48550/arXiv.2602.07408> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.07408>. 관측일 2026-11-01.

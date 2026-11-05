# 계산생물학 연구실 (SNU Compbio Lab)

**서울대학교 자연과학대학 화학부 · 석차옥 교수**

- 분야: 계산생물학, 단백질 구조와 분자 결합 예측[^research][^faculty]
- 대분야: 화학, 컴퓨팅·AI
- 태그: 구조생물학[^research], 바이오정보학·계산생물학[^research], AI 신약 개발[^research]
- 홈페이지: <https://seoklab.org/>
- 근거와 출처: [계산생물학 연구실 근거 페이지](seoklab-sources.md)

> 생체 물질의 모양과 결합을 계산으로 예측하고, 이를 분자 설계에 연결하는 방법을 개발한다.

## 무엇을 연구하나

계산생물학 연구실은 단백질(아미노산이 사슬로 이어져 이루는 생체 물질)의 구조와 기능을 이론과 계산으로 이해하는 연구실이다. 생체 분자가 어떤 모양을 취하고 서로 어떻게 결합하는지 원자 수준에서 예측하는 것이 목표다. 학과 소개는 생체 분자의 모양과 움직임을 계산하는 수학적 방법을 만들고, 이를 새로운 약물과 단백질의 설계로 확장한다고 설명한다.[^research][^faculty]

연구의 중심에는 GALAXY(생체 분자의 구조와 결합을 계산하는 소프트웨어 묶음)가 있다. 단백질 구조 예측, 단백질과 리간드(단백질 등 결합 상대에 붙는 이온이나 분자)의 결합 예측, 단백질끼리의 결합 예측을 담당하는 프로그램을 함께 개발한다. 이런 결합 상태의 구조를 계산하는 일을 도킹이라 한다. 결합할 위치를 찾는 프로그램과 같은 종류의 단백질 사슬들이 이루는 조립체의 구조를 예측하는 프로그램도 포함한다. 연구실은 개발한 방법을 웹에서 사용할 수 있도록 GalaxyWeb이라는 계산 서비스를 제공한다.[^research]

특히 단백질 고리 구조(규칙적인 나선이나 판 구조에 속하지 않는 사슬 구간)의 예측과 구조 보정에 집중한다. 구조 보정은 계산으로 얻은 모양을 다시 조정하는 과정이다. 연구 소개는 고리의 양 끝 연결 조건을 만족시키는 계산 방법을 바탕으로 가능한 모양을 탐색하고, 단백질 전체 모형에서 부정확한 부분을 고치는 방법으로 이어 간다고 설명한다. 결합 예측에서도 단백질의 모양이 고정되어 있다고 가정하는 데서 나아가, 결합할 때 모양이 변하는 경우를 다룬다.[^research]

최근 연구에서는 신경망(연결된 계산 단위들의 연결 세기를 자료로 학습하는 모형)의 계산 구조를 새로 제안했다. 이 연구는 딥러닝(계산 단위를 여러 층으로 연결한 신경망을 학습하는 방법)을 이용하며, 단백질의 여러 구조 후보가 서로 정보를 주고받도록 한다. 항체(특정 물질을 인식해 결합하는 면역 단백질)의 고리 구조 예측에 적용해 가능한 구조를 찾는 과정을 개선했다.[^p2] 또 단백질의 기능과 관련된 여러 구조 상태를 예측 모델이 얼마나 잘 재현하는지 평가하는 자료와 기준을 개발했다. 리간드나 다른 단백질의 결합 때문에 생기는 구조 변화와, 그런 결합 없이 나타나는 구조 변화를 함께 다룬다.[^p1]

분자 설계에서는 강화학습(행동의 결과로 받은 보상을 바탕으로 행동을 배우는 기계학습 방법)을 이용해 합성 가능한 분자를 생성하고 결합 관련 성질을 함께 고려한다.[^p7] 면역원성(물질이 면역 반응을 일으키는 능력)을 예측하는 계산 방법도 개발한다. 여러 종류의 면역 관련 자료를 함께 학습해 예측하는 방법으로, 단백질 치료제와 백신의 개발에 도움을 줄 가능성을 제시했다.[^p8]

## 주요 연구 주제

### 1. 단백질 구조와 상태 변화 예측

단백질 사슬의 고리, 단백질들이 결합한 조립체, 기능에 따라 달라지는 구조 상태를 계산한다. 기존 구조 정보를 참고해 모형을 만들고 부정확한 구간을 고치는 방법과, 구조 후보들 사이의 정보 교환으로 새 모양을 탐색하는 방법을 연구한다. ProMiSE(단백질의 여러 구조 상태 예측을 평가하는 자료와 평가 체계)는 구조 예측 모델의 평가를, ComMat(구조 후보 집단의 정보 교환으로 단백질 고리를 예측하는 신경망 구조)는 고리 구조 계산을 다룬다.[^research][^p1][^p2]

GalaxyDomDock(단백질 도메인의 상대적 방향을 예측하는 도킹 프로그램)은 도메인(단백질 안에서 구조적으로 구분되는 접힘 단위)의 개별 구조가 주어졌을 때 이들이 어떤 방향으로 조립될 수 있는지 계산한다. 도메인들을 이어 주는 사슬 구간의 조건을 고려해 가능한 방향을 찾고 연결 구간의 모양도 예측한다.[^p6]

### 2. 단백질과 분자의 결합 예측

단백질과 리간드가 결합하는 자세와 결합 친화도(서로 결합하려는 경향의 세기)를 예측한다. GalaxyDock(단백질과 리간드의 결합 구조를 예측하는 프로그램)은 결합 상대 단백질의 유연성을 고려하는 방향으로 개발한다. GalaxySite(단백질에서 리간드가 결합할 위치를 예측하는 프로그램)는 도킹과 유사한 단백질의 정보를 결합한다. 단백질끼리 결합하는 구조와 같은 종류의 단백질들이 이루는 조립체의 구조도 연구한다.[^research]

최근에는 PrOMet(단백질 구조에서 금속이 결합할 위치와 종류를 예측하는 계산 방법), G-screen(단백질의 구조 정보를 반영해 후보 분자를 추리는 계산 체계), GalaxyCDock(공유 결합 리간드의 결합 구조를 예측하는 웹 서비스)를 제안했다. 공유 결합은 원자들이 전자를 공유해 이루는 화학 결합이다. G-screen은 가상 스크리닝(컴퓨터 계산으로 후보 분자를 추리는 방법)을, GalaxyCDock은 리간드의 자세 탐색과 채점 함수(후보 구조에 점수를 매기는 계산식)를 결합한 도킹을 다룬다.[^p3][^p4][^p5]

### 3. 실험 정보와 계산의 결합, 분자 설계

실험에서 얻은 불완전한 구조 정보와 계산 예측을 결합해 단백질 모형을 만드는 방법을 연구한다. 연구 소개는 항체와 세포 표면 수용체(세포가 특정 물질을 인식하도록 결합하는 단백질)를 대상으로, 고리 구조와 결합 상태를 계산하는 방법을 개발한다고 설명한다. 학과 소개는 이런 계산 방법을 약물과 단백질의 설계에 연결하는 것을 연구 방향으로 든다.[^research][^faculty]

SHARP(Synthesizable Hierarchical Action-space Reinforcement learning for Pareto optimization)는 분자 조각을 추가·삭제·치환하는 행동을 학습해 분자를 생성하는 방법이다. 합성 가능성을 추정하는 모형으로 허용할 행동을 정하고, 결합 관련 평가 등을 보상에 반영한다.[^p7]

### 4. 면역원성 예측

T-SCAPE(T cell immunogenicity scoring via cross-domain aided predictive engine)는 서로 다른 면역 관련 자료를 통합하는 딥러닝 체계다. 면역세포의 활성화와 치료용 항체가 항체 생성을 유도할 가능성을 예측했다. 예측 방법의 개발과 평가가 연구의 중심이며, 백신과 단백질 치료제 개발에 기여할 가능성을 제시한다.[^p8]

## 대표 논문

최근 논문 가운데 석차옥 교수가 저자이고 서울대 재직 시기에 발표한 여덟 편을 골랐다. 단백질 구조·고리 예측, 분자 결합과 도킹, 도메인 조립, 분자 설계, 면역원성 예측을 함께 담았다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다. 별표는 누리집 표시다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [ProMiSE: Protein Multi-State Evaluation Benchmark in Biological Contexts](https://proceedings.mlr.press/v306/ku26a.html) · International Conference on Machine Learning | 단백질은 기능을 수행하면서 여러 모양 사이를 오간다. 이 연구는 단백질 조립체를 바탕으로 자체 구조 변화와 결합에 따른 구조 변화를 함께 담은 자료와 평가 체계를 제안했다. 기존 구조 예측 모델들을 평가한 결과, 여러 상태를 생성하는 능력과 결합 상황을 반영하는 능력에 한계가 있음을 보였다.[^p1] | Bonjae Ku(1저자), Seeun Kim, Yubeen Kim, Hahnbeom Park(누리집 \*), Chaok Seok(누리집 \*, 마지막 저자)[^p1] |
| 2 | 2024 | [Protein loop structure prediction by community-based deep learning and its application to antibody CDR H3 loop modeling](https://doi.org/10.1371/journal.pcbi.1012239) · PLOS Computational Biology | 단백질 구조 정보가 부족할 때의 예측 문제를 다룬다. 구조 후보 하나를 추적하는 대신 여러 후보가 집단을 이루고 서로 정보를 교환하는 신경망 구조를 제안했다. 항체가 결합 상대를 인식하는 CDR(Complementarity-Determining Region, 상보성 결정 영역)의 H3 고리에 적용해 구조 탐색을 개선했다. 다른 구조 예측과 설계 문제에도 적용할 가능성을 제시했다.[^p2] | Hyeonuk Woo(공동 기여, 1저자), Yubeen Kim(공동 기여, 1저자), Chaok Seok(누리집 \*, 마지막 저자)[^p2] |
| 3 | 2026 | [PrOMet: Accurate and Robust Metal-Binding Site and Type Prediction](https://doi.org/10.1002/advs.78003) · Advanced Science | 단백질에서 금속이 결합할 위치와 금속 종류를 예측하는 방법이다. 후보를 추리는 과정과 최적화를 결합하는 전략을 제안했다. 실험으로 얻은 단백질 구조와 예측 구조 등에서 평가했으며, 불확실한 금속 위치와 종류를 정하는 데 활용할 가능성을 제시했다.[^p3] | Gangeun Park(1저자), Chaok Seok(누리집 \*), Hahnbeom Park(누리집 \*, 마지막 저자)[^p3] |
| 4 | 2026 | [G-screen: scalable protein-aware virtual screening through flexible ligand alignment](https://doi.org/10.1186/s13321-026-01297-0) · Journal of Cheminformatics | 기준이 될 단백질·리간드 복합체의 구조가 있을 때 대규모 분자 후보를 추리는 방법이다. 후보 분자를 기준 리간드에 유연하게 겹쳐 맞춘 뒤 단백질과의 상호작용을 평가한다. 분자 정렬에 기초한 탐색과 본격적인 도킹 사이에 놓이는 계산 절차로 제시했다.[^p4] | Nuri Jung(1저자), Hahnbeom Park, Jinsol Yang(누리집 \*), Chaok Seok(누리집 \*, 마지막 저자)[^p4] |
| 5 | 2026 | [GalaxyCDock: Webserver for Covalent Protein–Ligand Binding Mode Prediction](https://doi.org/10.1016/j.jmb.2026.169807) · Journal of Molecular Biology | 공유 결합 리간드의 결합 구조를 예측하는 웹 서비스를 개발했다. 리간드 자세 탐색과 딥러닝 기반 채점 함수를 결합했으며, 기존 도구들과 평가 자료에서 성능을 비교했다. 결합 상대 단백질의 구조를 알고 있을 때 활용할 수 있는 계산 방법으로 제시했다.[^p5] | Sumin Lee(1저자), Nuri Jung, Hyeonuk Woo, Jinsol Yang, Chaok Seok(누리집 \*, 마지막 저자)[^p5] |
| 6 | 2022 | [GalaxyDomDock: An Ab Initio Domain–domain Docking Web Server for Multi-domain Protein Structure Prediction](https://doi.org/10.1016/j.jmb.2022.167508) · Journal of Molecular Biology | 개별 도메인의 구조는 알지만 서로의 방향은 모를 때 단백질의 조립 구조를 예측한다. 도킹으로 방향 후보를 만들고, 도메인 사이의 연결부가 허용하지 않는 방향을 걸러 낸다. 연결부의 구조도 예측하며 기존 도메인 도킹 방법들과 비교했다.[^p6] | Jayun Choi(1저자), Taeyong Park, Seung Yul Lee, Jinsol Yang, Chaok Seok(누리집 \*, 마지막 저자)[^p6] |
| 7 | 2025 | [SHARP: Generating Synthesizable Molecules via Fragment-Based Hierarchical Action-Space Reinforcement Learning for Pareto Optimization](https://doi.org/10.1021/acs.jcim.5c01699) · Journal of Chemical Information and Modeling | 결합 친화도와 합성 가능성 등 여러 목표를 함께 고려해 분자를 만드는 방법이다. 분자 조각을 편집하는 행동을 강화학습으로 배우고, 합성 가능성 추정 모형을 이용해 허용할 행동을 정한다. 여러 분자 최적화 과제에서 평가해 분자 설계에 활용할 수 있는 계산 체계를 제시했다.[^p7] | Jeonghyeon Kim(1저자), Seongok Ryu, Woohyeong Lee, Ansoo Lee, Hahnbeom Park(누리집 \*), Chaok Seok(누리집 \*, 마지막 저자)[^p7] |
| 8 | 2025 | [T-SCAPE: T cell immunogenicity scoring via cross-domain aided predictive engine](https://doi.org/10.1126/sciadv.adz8759) · Science Advances | 면역원성 자료가 부족한 문제를 다루기 위해 서로 다른 면역 관련 자료를 함께 학습하는 새 딥러닝 체계를 제안했다. 면역세포의 활성화와 치료용 항체가 항체 생성을 유도할 가능성을 예측하는 평가를 수행했다. 백신과 단백질 치료제 개발에 도움을 줄 가능성을 제시했다.[^p8] | Jeonghyeon Kim(1저자), Nuri Jung, Jayyoon Lee, Nam-Hyuk Cho, Jinsung Noh(누리집 \*), Chaok Seok(누리집 \*, 마지막 저자)[^p8] |

## 교수와 전문 분야

석차옥 교수는 서울대학교 화학 학사(1993), University of Chicago 화학 석사(1995)와 박사(1998) 학위를 받았다. University of Chicago(1999), Massachusetts Institute of Technology(2000), University of California, San Francisco(2000–2004)에서 Research Associate로 근무했다.[^faculty] 연구실 이력은 2004년부터 서울대학교 화학부에서 조교수·부교수·교수로 재직했다고 적는다.[^members]

공개 연구 소개에 나타난 전문 분야는 생체 분자 구조의 계산 예측, 단백질 고리 구조의 모델링과 보정, 단백질과 리간드 및 단백질 사이의 결합 예측이다.[^research][^faculty] 대표 논문은 구조 예측 모델의 평가와 신경망 설계, 금속·리간드 결합 예측, 도메인 조립, 분자 생성과 면역원성 예측으로 이어지는 계산 방법 연구를 보여 준다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구 소개는 계산 방법을 단백질 기능의 이해와 분자 설계에 연결한다. 약물 후보가 될 분자와 단백질의 결합 구조, 항체 고리 구조, 세포 표면 수용체의 구조 변화가 응용 대상이다. 실험에서 얻은 구조 정보를 계산 모형과 결합하는 방법도 개발한다.[^research][^faculty]

## 구성원

2026년 11월 5일 연구실 Members 게시 명단의 대학원생 14명과 인턴 8명이다. 과정·역할은 Graduate Students와 Internship Members 구획 표기이며, 학력과 소속도 게시 표기다. “대표 논문 참여”는 위 표의 저자 이름과 완전히 일치하는 경우만 표시했다.[^members]

| 이름 | 과정·역할 | 게시 학력 또는 소속 | 대표 논문 참여 |
|---|---|---|---|
| Sumin Lee | 대학원생 | M.S. in Artificial Intelligence, SNU B.S. in Biological Sciences, SNU | 5 |
| Jayun Choi | 대학원생 | B.S. in Chemistry, SNU | 6 |
| Seho Lee | 대학원생 | B.S. in Chemistry, SNU |  |
| Seeun Kim | 대학원생 | B.S. in Chemistry, SNU | 1 |
| Wooyeop Jeong | 대학원생 | B.S. in Chemistry Education, SNU |  |
| Sujin Park | 대학원생 | B.S. in Chemistry, SNU |  |
| Yubeen Kim | 대학원생 | M.S. in Chemistry, SNU B.S. in Chemistry, SNU | 1, 2 |
| Byunghyun Bae | 대학원생 | M.S. in Chemistry, SNU B.S. in Pharmacy, CAU |  |
| Byungwook Kim | 대학원생 | B.S. in Chemistry, SNU |  |
| Hongsuk Kim | 대학원생 | B.S. in Chemistry, SNU |  |
| Hyeonsung Byeon | 대학원생 | B.S. in Applied Biology and Chemistry & Chemistry, SNU |  |
| Yooshin Kim | 대학원생 | B.S. in Biological Science, SNU |  |
| Hyemi Park | 대학원생 | M.S in Chemistry, SGU B.S in Chemistry, SGU |  |
| Jaehyeong Kong | 대학원생 | B.S. in Chemistry, SNU |  |
| Jeongmoo Jun | 인턴 | College of Medicine, SNU |  |
| Bonjae Ku | 인턴 | College of Liberal Studies, SNU | 1 |
| Junsang Park | 인턴 | Department of Chemical and Biological Engineering, SNU |  |
| Jaekyun Park | 인턴 | Department of Chemistry, SNU |  |
| Dongha Ham | 인턴 | Department of Animal Science and Biotechnology, SNU |  |
| Wonbin Lee | 인턴 | Department of Chemistry, SNU |  |
| Jinyi Hong | 인턴 | Department of Chemistry, SNU |  |
| Junwon Lee | 인턴 | Department of Chemistry, SNU |  |

## 졸업생과 이전 구성원

연구실 Members의 Alumni 표에 적힌 38명이다. 학위와 연도뿐 아니라 방문 학생·방문 교수·학부생 등 당시 역할도 원문대로 적었고, 진로는 연구실의 게시 표기다. 2006–2026년 항목이 함께 있으며 최근 5년으로 제한한 목록은 아니다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Nuri Jung | Ph.D. (2026) | Professional, Galux Inc. |
| Jiho Sim | Ph.D. (2026) | Professional, Galux Inc. |
| Gangeun Park | M.S. (2026) | Ph.D. student, Department of Biological Sciences, KAIST |
| Changsoo Lee | Ph.D. (2025) | Professional, Galux Inc. |
| Jeonghyeon Kim | M.S. (2025) | Ph.D. student, Department of Bioengineering and Biomedical Engineering, Duke University |
| Hakjean Kim | M.S. (2024) | ROKA |
| Jihyeon Lee | M.S. (2023) | Ph.D. student, Department of Pharmaceutical Sciences, University of Maryland |
| Hyeonuk Woo | Ph.D. (2023) | Professional, Galux Inc. |
| Katsuhito Inui | M.S. (2022) | Researcher, Ohsong Pharm |
| Sohee Kwon | Ph.D. (2022) | Professional, Galux Inc. |
| Sangwoo Park | Ph.D. (2022) | Staff Engineer, Samsung Semiconductor Lab |
| Beomchang Kang | Ph.D. (2022) | Professional, LG Energy Solution |
| Jinsol Yang | Ph.D. (2022) | Vice President & Co-founder, Galux Inc. |
| Taeyong Park | Ph.D. (2021) | CEO & Co-founder, Galux Inc. |
| Jonghun Won | M.S. and Ph.D. (2021) | Vice President & Co-founder, Galux Inc. |
| Minkyung Baek | Ph.D. (2018) | Associate Professor, Department of Biological Sciences, Seoul National University |
| Martin Steinegger | Visiting Student from Max Planck Institute (2014, 2016-2018) | Associate Professor, Department of Biological Sciences, Seoul National University |
| Gyu Rie Lee | Ph.D. (2017) | Assistant Professor, Department of Biological Sciences, KAIST |
| Matthias Buck | Visiting Professor (2017) | Professor, Case Western Reserve University |
| Andrew H. Beaven | Visiting Student from University of Kansas (2015-2016) | Postdoctoral Researcher, University of Minnesota |
| Lim Heo | Ph.D. (2015) | Sr. Principal Scientist, Bristol Myers Squibb |
| Hasup Lee | Ph.D. (2016) | Research Staff Member, Samsung Advanced Institute of Technology |
| Kyuhong Choe | M.S. (2015) | Researcher, LG Chemistry |
| Jaeju Ko | Visiting Professor (2014-2015) | Associate Professor, Indiana University of Pennsylvania |
| Woong-Hee Shin | Ph.D. (2014) | Associate Professor, College of Medicine, Korea University |
| Dongseon Lee | Ph.D. (2013) | Research Staff Member, Samsung Advanced Institute of Technology |
| Chiwook Park | Visiting professor (2013) | Professor, Purdue University |
| Hahnbeom Park | Ph.D. (2012) | Senior Researcher, Brain Science Institute, KIST |
| Junsu Ko | Ph.D. (2012) | CEO & Co-founder, Arontier |
| Junghyun Choi | M.S. (2011) | Researcher, LG Chemistry |
| Juyong Lee | M.S. and Ph.D. (2011) | Associate Professor, College of Pharmacy, Seoul National University |
| Younkyoung Lee | M.S. (2010) | Associate Professor, Electronic Materials Engineering, Jeonbuk National University |
| Jungho Lee | Research Assistant (2008) | Associate Professor, Department of Chemistry, Seoul National University |
| Jungki Yoon | Undergraduate Student (2008) | Clinical Assistant Professor, Seoul National University Hospital |
| Sukki Kang | Graduate Course (2007) | Science Writer |
| Sangwoo Shim | M.S. (2007) | Founder & Chief Data Scientist, MakinaRocks |
| Changho Sohn | Undergraduate Student (2006) | Assistant Professor, Nano Biomedical Engineering, Y-IBS Institute, Yonsei University |
| Heesun Han | Undergraduate Student (2006) | Associate Professor, Department of Chemistry, University of Illinois, Urbana-Champaign |

## 최근 논문 목록 (2021–2026)

연구실 Publications 14쪽의 전체 132편 가운데 2021–2026년 구역은 47편이며, 아래 목록은 그중 33편이다. 기간은 2021년 10월 22일부터 2026년 10월 22일까지를 기준으로 삼았다. 2021년 논문은 온라인 출판일이 있으면 그 날짜로 구분했다.[^dates] 제목·저자·학술지·학회와 연도 구역은 연구실 게시 표기를 따르며, 일부 공동 연구의 저자 칸은 전체 저자가 아닌 대표 저자와 랩 참여자의 표기다. 별표는 누리집 표시를 그대로 두었다. ProMiSE의 연구실 게시월은 6월이고 학회 논문집은 7월이다.[^pubs1][^pubs2][^pubs3][^pubs4][^pubs5][^p1]

**2026**

- Gangeun Park, Chaok Seok\* and Hahnbeom Park\*. "PrOMet: Accurate and Robust Metal-binding site and Type Prediction". *Advanced Science*. <https://doi.org/10.1002/advs.78003>.[^p3]
- Nuri Jung, Hahnbeom Park, Jinsol Yang\* and Chaok Seok\*. "G-screen: Scalable Protein-Aware Virtual Screening through Flexible Ligand Alignment". *Journal of Cheminformatics*. <https://doi.org/10.1186/s13321-026-01297-0>.[^p4]
- Bonjae Ku, Seeun Kim, Yubeen Kim, Hahnbeom Park\* and Chaok Seok\*. "ProMiSE: Protein Multi-State Evaluation Benchmark in Biological Contexts". *International Conference on Machine Learning*.
- Chulwon Choi, Hyeonsung Byeon, Juho Lee, Hong Geun Lee, Chaok Seok and Hee-Jung Choi\*. "Structural basis of the sweat odorant HMHA recognition by the human odorant receptor OR52E8". *Communications Biology*.
- Nawoon Kim, Byunghyun Bae, Nuri Jung, Chaok Seok and Hahnbeom Park\*. "MotifLeadDB: A Hierarchical Structural Data Set for Congeneric Ligand Binding Activity Change". *Journal of Chemical Information and Modeling*.
- Sumin Lee, Nuri Jung, Hyeonuk Woo, Jinsol Yang and Chaok Seok\*. "GalaxyCDock: Webserver for Covalent Protein–Ligand Binding Mode Prediction". *Journal of Molecular Biology*. <https://doi.org/10.1016/j.jmb.2026.169807>.[^p5]

**2025**

- Jeonghyeon Kim, Nuri Jung, Jayyoon Lee, Nam-Hyuk Cho, Jinsung Noh\*, Chaok Seok\*. "T-SCAPE: T-cell Immunogenicity Scoring via Cross-domain Aided Predictive Engine". *Science Advances*. <https://doi.org/10.1126/sciadv.adz8759>.[^p8]
- Chaok Seok\* and Pratyush Tiwary. "Editorial overview: Artificial intelligence methodologies in structural biology". *Current Opinion in Structural Biology*.
- Jeonghyeon Kim, Seongok Ryu, Woohyeong Lee, Ansoo Lee, Hahnbeom Park\* and Chaok Seok\*. "SHARP: Generating Synthesizable Molecules via Fragment-based Hierarchical Action-space Reinforcement Learning for Pareto Optimization". *Journal of Chemical Information and Modeling*. <https://doi.org/10.1021/acs.jcim.5c01699>.[^p7]
- Sujin Park, Wooyeop Jeong, Yubeen Kim, Chang-Han Lee and Chaok Seok\*. "Artificial Intelligence in Therapeutic Antibody Design: Advances and Future Prospects". *Current Opinion in Structural Biology*. <https://doi.org/10.1016/j.sbi.2025.103084>.[^s-b1]
- Seeun Kim, Simaek Oh, Hyeonuk Woo, Jiho Sim, Chaok Seok\* and Hahnbeom Park\*. "Deep learning molecular interaction motifs from Receptor structure alone". *Journal of Cheminformatics*.
- Jinuk Kim et al. (Hyeonsung Byeon and Chaok Seok). "Structural insights into small-molecule agonist recognition and activation of complement receptor C3aR". *EMBO Journal*. <https://doi.org/10.1038/s44318-025-00429-w>.[^s-b2]
- Byung-hyun Bae, Jungyoon Choi, Chaok Seok and Hahnbeom Park\*. "Physics-Inspired Accuracy Estimator for Model-Docked Ligand Complexes". *Journal of Chemical Theory and Computation*.
- Hyunuk Eom, Sukhwan Park, Kye Soo Cho, Jihyeon Lee, Hyunbin Kim, Stephanie Kim, Jinsol Yang, Young-Hyun Han, Juyong Lee, Chaok Seok, Myeong Sup Lee\*, Woon Ju Song\*, Martin Steinegger\*. "Discovery of highly active kynureninases for cancer immunotherapy through protein language model". *Nucleic Acids Research*. <https://doi.org/10.1093/nar/gkae1245>.[^s-b3]

**2024**

- Hakjean Kim, Seongok Ryu, Nuri Jung, Jinsol Yang\* and Chaok Seok\*. "CSearch: chemical space search via virtual synthesis and global optimization". *Journal of Cheminformatics*. <https://doi.org/10.1186/s13321-024-00936-8>.[^s-c7]
- Sohee Kwon, Nuri Jung, Jinsol Yang\* and Chaok Seok\*. "GalaxySagittarius-AF: Predicting Targets for Drug-Like Compounds in the Extended Human 3D Proteome". *Journal of Molecular Biology*.
- Changsoo Lee, Jonghun Won, Seongok Ryu, Jinsol Yang, Nuri Jung, Hahnbeom Park, and Chaok Seok\*. "GalaxyDock-DL: Protein-Ligand Docking by Global Optimization and Neural Network Energy". *Journal of Chemical Theory and Computation*. <https://doi.org/10.1021/acs.jctc.4c00385>.[^s-c5]
- Hyeonuk Woo, Yubeen Kim, and Chaok Seok\*. "Protein Loop Structure Prediction by Community-based Deep Learning and its Application to Antibody CDR H3 Loop Modeling". *PLoS Computational Biology*. <https://doi.org/10.1371/journal.pcbi.1012239>.[^p2]
- Shantanu Jain et al. (Chaok Seok). "CAGI, the Critical Assessment of Genome Interpretation, establishes progress and prospects for computational genetic variant interpretation methods". *Genome Biology*.

**2023**

- Sumin Lee, Seeun Kim, Gyu Rie Lee, Sohee Kwon, Hyeonuk Woo, Chaok Seok\* and Hahnbeom Park\*. "Evaluating GPCR modeling and docking strategies in the era of deep learning-based protein structure prediction". *Computational and Structural Biotechnology Journal*.
- Sohee Kwon and Chaok Seok\*. "CSAlign and CSAlign-Dock: Structure alignment of ligands considering full flexibility and application to protein-ligand docking". *Computational and Structural Biotechnology Journal*.
- Chulwon Choi et al. (Seho Lee, Chaok Seok and Hahnbeom Park). "Understanding the molecular mechanisms of odorant binding and activation of the human OR52 family". *Nature Communications*.
- Won Hoon Choi et al. (Seho Lee, Jiho Sim and Chaok Seok). "ECPAS/Ecm29-mediated 26S proteasome disassembly is an adaptive response to glucose starvation". *Cell Reports*.
- Changsoo Lee, Jinsol Yang, Sohee Kwon and Chaok Seok\*. "GalaxyDock2-HEME: protein-ligand docking for heme proteins". *Journal of Computational Chemistry*.
- Seho Lee, Chaok Seok\* and Hahnbeom Park\*. "Benchmarking applicability of medium-resolution cryo-EM protein structures for structure-based drug design". *Journal of Computational Chemistry*.
- Jihyeon Lee, Chaok Seok, Sihyun Ham and Song-Ho Chong\*. "Atomic-level thermodynamics analysis of the binding free energy of SARS-CoV-2 neutralizing antibodies". *Proteins*. <https://doi.org/10.1002/prot.26458>.[^s-b4]
- Jiho Sim, Sohee Kwon and Chaok Seok\*. "HProteome-BSite: predicted binding sites and ligands in human 3D proteome". *Nucleic Acids Research*.
- Hyunook Kang et al. (Sohee Kwon and Chaok Seok). "Structural basis for Y2 receptor-mediated neuropeptide Y and peptide YY signaling". *Structure*.

**2022**

- Sangwoo Park and Chaok Seok\*. "GalaxyWater-CNN: Prediction of Water Positions on the Protein Structure by a 3D-Convolutional Neural Network". *Journal of Chemical Information and Modeling*.
- Jayun Choi, Taeyong Park, Seung Yul Lee, Jinsol Yang and Chaok Seok\*. "GalaxyDomDock: An ab initio domain–domain docking web server for multi-domain protein structure prediction". *Journal of Molecular Biology*. <https://doi.org/10.1016/j.jmb.2022.167508>.[^p6]
- Kyoo Heo et al. (Sohee Kwon and Chaok Seok). "A pGpG-specific phosphodiesterase regulates cyclic di-GMP signaling in Vibrio cholerae". *Journal of Biological Chemistry*.
- Chaehee Park et al. (Hyeonuk Woo and Chaok Seok). "Structural basis of neuropeptide Y signaling through Y1 receptor". *Nature Communications*.
- Beomchang Kang, Chaok Seok\* and Juyong Lee\*. "A benchmark study of machine learning methods for molecular electronic transition: Tree-based ensemble learning versus graph neural network". *Bulletin of the Korean Chemical Society*.

## 연락과 위치

- 연구실: 서울대학교 자연과학대학 화학부 502동 203호, 서울 08826[^members]
- 교수 연구실: 502동 223호[^members][^faculty]
- 기관 전화: 교수 연구실 02-880-9197, 연구실 02-880-4355[^members][^faculty]
- 교수 업무 이메일: chaok@snu.ac.kr[^p2]
## 각주

[^research]: 연구실 Research. <https://seoklab.org/research> (열람일 2026-11-05).
[^faculty]: 서울대학교 자연과학대학 화학부, 석차옥 교수 상세. <https://chem.snu.ac.kr/research-faculty/faculty/fulltime?mode=view&profidx=57&sc=y> (열람일 2026-11-05).
[^members]: 연구실 Members, 교수 이력·구성원·Alumni·연락처. <https://seoklab.org/members> (열람일 2026-11-05).
[^pubs1]: 연구실 Publications 1쪽. <https://seoklab.org/publications/> (열람일 2026-11-05).
[^pubs2]: 연구실 Publications 2쪽. <https://seoklab.org/publications/page2/> (열람일 2026-11-05).
[^pubs3]: 연구실 Publications 3쪽. <https://seoklab.org/publications/page3/> (열람일 2026-11-05).
[^pubs4]: 연구실 Publications 4쪽. <https://seoklab.org/publications/page4/> (열람일 2026-11-05).
[^pubs5]: 연구실 Publications 5쪽. <https://seoklab.org/publications/page5/> (열람일 2026-11-05).
[^p1]: B. Ku 외, C. Seok, Proceedings of the 43rd International Conference on Machine Learning 306, 61215–61235 (2026). <https://proceedings.mlr.press/v306/ku26a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v306/ku26a.html> (열람일 2026-11-05).
[^p2]: H. Woo, Y. Kim, C. Seok, PLOS Computational Biology 20, e1012239 (온라인 2024-06-24). <https://doi.org/10.1371/journal.pcbi.1012239> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012239> (열람일 2026-11-05).
[^p3]: G. Park, C. Seok, H. Park, Advanced Science, e78003 (온라인 2026-10-11). <https://doi.org/10.1002/advs.78003> 초록 기준. 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=PrOMet%3A%20Accurate%20and%20Robust%20Metal-binding%20site%20and%20Type%20Prediction> (열람일 2026-11-05).
[^p4]: N. Jung, H. Park, J. Yang, C. Seok, Journal of Cheminformatics (온라인 2026-09-16). <https://doi.org/10.1186/s13321-026-01297-0> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index,authorships&filter=doi:10.1002/advs.78003|10.1002/prot.26231|10.1002/prot.26458|10.1007/s00018-023-04760-5|10.1016/j.jmb.2022.167508|10.1016/j.jmb.2026.169807|10.1016/j.sbi.2025.103084|10.1021/acs.jcim.5c01699|10.1021/acs.jctc.4c00385|10.1038/s44318-025-00429-w|10.1093/nar/gkae1245|10.1126/sciadv.adz8759|10.1186/s13321-024-00936-8|10.1186/s13321-026-01297-0|10.15252/emmm.202013790|10.2210/pdb7wj5/pdb> (열람일 2026-11-05).
[^p5]: S. Lee 외, C. Seok, Journal of Molecular Biology 438, 169807 (2026). <https://doi.org/10.1016/j.jmb.2026.169807> 초록 기준(Semantic Scholar 등록 초록). 초록 원문 <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jmb.2026.169807?fields=title,abstract,externalIds,publicationDate,venue> (열람일 2026-11-05).
[^p6]: J. Choi 외, C. Seok, Journal of Molecular Biology 434, 167508 (2022). <https://doi.org/10.1016/j.jmb.2022.167508> 초록 기준(Semantic Scholar 등록 초록). 초록 원문 <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jmb.2022.167508?fields=title,abstract,externalIds,publicationDate,venue> (열람일 2026-11-05).
[^p7]: J. Kim 외, C. Seok, Journal of Chemical Information and Modeling 65, 11601-11619 (온라인 2025-10-24). <https://doi.org/10.1021/acs.jcim.5c01699> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index,authorships&filter=doi:10.1002/advs.78003|10.1002/prot.26231|10.1002/prot.26458|10.1007/s00018-023-04760-5|10.1016/j.jmb.2022.167508|10.1016/j.jmb.2026.169807|10.1016/j.sbi.2025.103084|10.1021/acs.jcim.5c01699|10.1021/acs.jctc.4c00385|10.1038/s44318-025-00429-w|10.1093/nar/gkae1245|10.1126/sciadv.adz8759|10.1186/s13321-024-00936-8|10.1186/s13321-026-01297-0|10.15252/emmm.202013790|10.2210/pdb7wj5/pdb> (열람일 2026-11-05).
[^p8]: J. Kim 외, C. Seok, Science Advances 11, eadz8759 (2025). <https://doi.org/10.1126/sciadv.adz8759> 초록 기준. 초록 원문 <https://api.crossref.org/works?rows=3&query.bibliographic=T-SCAPE%3A%20T-cell%20Immunogenicity%20Scoring%20via%20Cross-domain%20Aided%20Predictive%20Engine> (열람일 2026-11-05).
[^s-b1]: Crossref 등록 서지·저자, Artificial intelligence in therapeutic antibody design: Advances and future prospects. <https://api.crossref.org/works/10.1016/j.sbi.2025.103084> (열람일 2026-11-05).
[^s-b2]: Crossref 등록 서지·저자, Structural insights into small-molecule agonist recognition and activation of complement receptor C3aR. <https://api.crossref.org/works/10.1038/s44318-025-00429-w> (열람일 2026-11-05).
[^s-b3]: Crossref 등록 서지·저자, Discovery of highly active kynureninases for cancer immunotherapy through protein language model. <https://api.crossref.org/works/10.1093/nar/gkae1245> (열람일 2026-11-05).
[^s-c7]: Crossref 등록 서지·저자, CSearch: chemical space search via virtual synthesis and global optimization. <https://api.crossref.org/works/10.1186/s13321-024-00936-8> (열람일 2026-11-05).
[^s-c5]: Crossref 등록 서지·저자, GalaxyDock-DL: Protein–Ligand Docking by Global Optimization and Neural Network Energy. <https://api.crossref.org/works/10.1021/acs.jctc.4c00385> (열람일 2026-11-05).
[^s-b4]: Crossref 등록 서지·저자, Atomic‐level thermodynamics analysis of the binding free energy of SARS‐CoV ‐2 neutralizing antibodies. <https://api.crossref.org/works/10.1002/prot.26458> (열람일 2026-11-05).
[^dates]: Crossref 등록 출판일. <https://api.crossref.org/works/10.1002/prot.26203> <https://api.crossref.org/works/10.1002/prot.26222> <https://api.crossref.org/works/10.1002/prot.26192> <https://api.crossref.org/works/10.1002/prot.26231> <https://api.crossref.org/works/10.15252/emmm.202013790> (열람일 2026-11-05).

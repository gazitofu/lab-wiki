# Insung S. Choi's Lab (The CHOI Group)

**KAIST 화학과 · 최인성 교수**

- 분야: 단일 세포 피포화, 세포와 합성 재료의 결합, 오염 방지 표면 화학, 분자 그래프 학습, 코돈 설계 계산 방법, 신경세포 배양
- 대분야: 화학, 컴퓨팅·AI
- 태그: 생체재료·조직 공학[^p1][^p3][^p5], 바이오정보학·계산생물학[^p6], 그래프 기계학습·지식 그래프[^p4], 과학·공학 AI[^p4]
- 홈페이지: <http://cisgroup.kaist.ac.kr/>
- 근거와 출처: [Insung S. Choi's Lab 근거 페이지](cisgroup-sources.md)

> 세포에 합성 재료로 기능을 더하고 신경세포의 배양 환경을 만들며, 분자 구조와 단백질 생산을 다루는 계산 방법을 개발하는 화학 연구실이다.[^p1][^p4][^p5][^p6]

## 무엇을 연구하나

최인성 교수의 연구실은 화학·생물학·계산 도구를 함께 사용한다. 누리집은 연구를 단일 세포 피포화, 신경과학, 기계학습으로 나눈다.[^people][^research] 단일 세포 피포화(Single-Cell Nanoencapsulation, SCNE)는 살아 있는 세포 하나를 나노미터 규모의 합성 껍질로 감싸는 방법이다. 연구실은 껍질에 촉매(화학 반응의 속도를 높이며 반응 전체에서 소모되지 않는 물질) 기능이나 환경에 반응하는 성질을 넣어 세포에 외래 기능을 부여한다.[^p1][^p2]

세포와 껍질의 결합에서는 재료의 형성과 기능 변화를 함께 다룬다. 한 연구는 효모가 발효하며 내놓는 에탄올과 효소(생물에서 화학 반응을 촉진하는 물질)의 연쇄 반응을 연결해 껍질을 형성하고, 세포 증식과 함께 비대칭 구조를 얻어 효소로 움직이는 세포 미세 로봇을 만들었다.[^p1] 다른 연구는 껍질의 조성을 바꾸면서 안에 담긴 기능성 물질을 방출하고 세포 보호 기능을 유지하는 방법을 제시했다.[^p2]

표면 화학에서는 단백질이나 세균 등이 표면에 달라붙는 생물 오염을 줄이는 재료를 만든다. AZ-DOPA라는 합성 분자를 코팅에 사용하고 클릭 화학(정해진 작용기 사이의 선택적 결합을 이용해 분자를 연결하는 화학적 접근)으로 표면에 기능성 분자를 붙였다. 기능화한 표면에서 세균 부착이 감소하는 것을 확인했다.[^p3]

계산 연구는 화학과 생물의 구조를 모델 설계에 반영한다. MolNet은 그래프 신경망(대상과 관계를 점과 선으로 나타낸 자료를 처리하는 신경망)에 분자의 결합 세기와 직접 결합하지 않은 원자 사이의 공간 관계를 넣는다.[^p4] MOSAIC는 코돈(단백질의 구성 단위나 합성 종료를 지정하는 세 염기로 이루어진 단위)을 하나씩 고르는 대신 연결된 집합으로 다루는 코돈 조화 알고리즘이다. 외래 단백질 생산을 위해 원래의 코돈 사용 패턴을 재현하려는 계산 방법이다.[^p6]

신경과학에서는 세포가 놓이는 배양 환경과 정상 발달을 다룬다. 뇌 유래 세포외기질(세포 바깥에서 세포를 지지하고 주변 환경을 이루는 물질)을 이용한 입체 배양에서 별아교세포(신경세포의 기능과 주변 환경을 조절하는 신경계 세포)가 별 모양으로 뻗는 형태와 성숙한 상태의 유전자 발현 특성을 보이도록 했다.[^p5] 정상 초기 신경세포에서 칸나비디올이 돌기 성장과 축삭(신경세포가 신호를 다른 세포로 보내는 돌기) 분화에 주는 영향도 정량적으로 살폈다.[^development]

## 주요 연구 주제

### 단일 세포 피포화와 기능성 껍질

세포의 발효와 재료 형성 반응을 결합하거나 껍질의 조성을 바꾸어, 세포에 운동·물질 방출 기능을 부여하는 방법을 연구한다. 자율 형성 연구에서는 세포 증식과 껍질 생성의 결합으로 비대칭 구조를 만들었고,[^p1] 조성 변환 연구에서는 껍질에 담긴 물질의 활성과 인식 기능을 보존하면서 방출하도록 했다.[^p2]

### 오염 방지 표면 화학

새 분자를 합성하고 표면에 기능성 성분을 연결하는 화학 방법을 개발한다. AZ-DOPA 기반 코팅은 여러 종류의 바탕 재료에 형성되며, 여기에 양쪽성 이온(한 분자 안에 양전하와 음전하를 함께 가지며 전체 전하는 중성인 화학종) 성분을 붙여 오염 방지 표면으로 만들었다.[^p3]

### 분자 그래프 학습과 코돈 설계

MolNet은 분자 내부의 비결합 공간 관계와 결합 세기를 학습 모델에 담아 분자 성질을 예측한다.[^p4] MOSAIC는 Monte Carlo-based Simulated Annealing for Linked Codons의 약자로, 무작위 표본을 이용하는 계산과 모의 담금질(목적값이 악화되는 후보도 확률적으로 선택하되 조절값을 낮추며 탐색하는 최적화 방법)을 결합해 연결된 코돈 집합의 사용 패턴을 조화시킨다.[^p6]

### 신경세포의 배양 환경과 발달

세포외기질을 이용한 입체 배양은 신경계 세포가 주변과 상호작용할 환경을 제공하는 방법이다. 별아교세포의 형태, 유전자 발현과 다른 신경세포를 지지하는 특성을 함께 살핀다.[^p5] 정상 신경세포 발달 연구에서는 돌기 길이와 가지 수, 축삭이 정해진 세포의 비율처럼 형태와 발달을 나타내는 값을 분석했다.[^development]

## 대표 논문

세포와 껍질의 복합체, 오염 방지 표면, 분자 그래프 학습, 신경세포 배양, 코돈 설계 방법을 보여 주는 6편이다. 사전 공개본은 발표처에 판본을 표시했다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 최인성의 역할 |
|---|---|---|---|---|
| 1 | 2025 | [Autonomous Chemo-Metabolic Construction of Anisotropic Cell-in-Shell Nanobiohybrids in Enzyme-Powered Cell Microrobots](https://doi.org/10.1126/sciadv.adu5451) · Science Advances | 효모의 발효와 효소 연쇄 반응을 연결해 폴리도파민 껍질이 자율적으로 형성되게 했다. 세포 증식과 결합해 비대칭 구조를 얻었고, 요소분해효소를 연결해 움직이는 세포 미세 로봇을 만들었다.[^p1] | 마지막 저자 |
| 2 | 2024 | [A Micrometric Transformer: Compositional Nanoshell Transformation of Fe3+-Trimesic-Acid Complex with Concomitant Payload Release in Cell-in-Catalytic-Shell Nanobiohybrids](https://doi.org/10.1002/advs.202306450) · Advanced Science | 효소를 담은 철 이온·트리메스산 껍질을 인산철 껍질로 바꾸면서 기능성 물질을 방출했다. 이 과정에서 담긴 물질의 활성과 인식 기능, 껍질의 세포 보호 성질을 유지했다.[^p2] | 마지막 저자 |
| 3 | 2026 | [Synthesis of an Azide-Bearing L-DOPA for Click-Based Antifouling Surface Functionalization](https://doi.org/10.1055/a-2839-6271) · Synthesis | AZ-DOPA를 합성해 여러 바탕 재료에 코팅하고, 클릭 반응으로 양쪽성 이온 성분을 붙였다. 기능화한 표면에서 세균 부착이 감소해 오염 방지 표면을 만드는 방법으로 제시했다.[^p3] | 공저자, 7명 중 6번째 |
| 4 | 2022 | [MolNet: A Chemically Intuitive Graph Neural Network for Prediction of Molecular Properties](https://doi.org/10.48550/arXiv.2203.09456) · arXiv 사전 공개본 v1 | 분자에서 직접 결합하지 않은 원자 사이의 공간 관계와 결합 세기를 함께 담은 모델을 제안했다. 분자 성질의 분류와 값 예측에서 여러 기준 모델보다 나은 성능을 보고했다.[^p4] | 마지막 저자 |
| 5 | 2023 | [In Vitro Induction of In Vivo-Relevant Stellate Astrocytes in 3D Brain-Derived, Decellularized Extracellular Matrices](https://doi.org/10.1016/j.actbio.2023.09.046) · Acta Biomaterialia | 뇌 유래 세포외기질로 입체 배양 환경을 만들었다. 그 안의 별아교세포는 별 모양으로 뻗고 성숙한 상태와 관련된 유전자 발현을 보였으며, 배양액은 신경 돌기 성장을 지원하는 특성을 보였다.[^p5] | 마지막 저자 |
| 6 | 2026 | [MOSAIC: Codon Harmonization of Monte Carlo-Based Simulated Annealing for Linked Codons in Heterologous Protein Expression](https://doi.org/10.1021/acssynbio.5c00844) · ACS Synthetic Biology | 코돈 하나가 아닌 연결된 집합을 대상으로 조화 알고리즘을 개발했다. 모델 단백질의 계산 평가와 생산 실험을 통해 민감한 단백질의 발현과 기능을 개선할 가능성을 제시했다.[^p6] | 마지막 저자 |

## 교수와 전문 분야

최인성 교수는 서울대학교에서 학사와 석사를, Harvard University에서 화학 박사를 받았다. MIT에서 박사후 연구를 수행한 뒤 2002년 KAIST에 부임했다. 누리집은 화학 박사와 컴퓨터과학 석사 학력을 함께 적고, 화학을 중심으로 생물학·계산 도구를 사용하는 연구자로 소개한다.[^people]

최근 논문으로 보면 전문 분야는 세포에 합성 재료와 기능을 더하는 표면 화학,[^p1][^p2][^p3] 신경계 세포의 배양 환경 설계,[^p5] 화학·생물 구조를 반영하는 계산 모델과 알고리즘으로 정리할 수 있다.[^p4][^p6]

## 응용 분야

세포와 껍질의 복합체는 세포를 보호하면서 외래 기능을 부여하는 화학적 도구이며, 세포 미세 로봇과 환경에 반응하는 재료 체계로 연결된다.[^p1][^p2] 오염 방지 표면은 세균 부착을 줄이는 재료 방법이다.[^p3] 입체 배양 기법은 별아교세포와 다른 신경계 세포의 연구 환경을 만드는 플랫폼이고,[^p5] 계산 모델은 분자 성질 예측과 외래 단백질 생산을 위한 설계를 지원한다.[^p4][^p6]

## 구성원

2026년 10월 30일 누리집 People 페이지 기준으로 연구원 4명과 학생 6명이다. 연구원의 괄호는 게시 학위이며 학생의 세부 학위과정은 구분하지 않는다. 연구 주제는 게시 표기다. 「대표 논문 참여」는 대표 표의 전체 저자 목록에 이름이 대응하는 사람에게 붙인 번호다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Seok-Pyo Hong | 연구원 (M.S.) | Organic Synthesis |  |
| Sang Yeong Han | 연구원 (Ph.D.) | Surface Chemistry | 1, 2, 3 |
| Hyunwoo Choi | 연구원 (Ph.D.) | In vitro Neuronal Network |  |
| HyeongBin Rheem | 연구원 (Ph.D.) | Surface Chemistry | 1, 3 |
| Ji Yoon Lee | 학생 | Supramolecular Chemistry |  |
| Yoonho Jeong | 학생 | Deep Learning | 4, 6 |
| Su Yeon Rhee | 학생 | Surface Chemistry | 2 |
| Duc Tai Nguyen | 학생 | Biomaterials Chemistry | 2 |
| Jayeong Kim | 학생 | Cell-Surface Interaction |  |
| Le Minh Nguyen | 학생 |  |  |

## 졸업생과 이전 구성원

People 페이지의 박사후 연구원·연구교수 6명, 박사 졸업생 34명, 석사 졸업생 17명이다. 구획 이름과 진로는 게시 표기이며 연도는 따로 적지 않는다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kuk-Ro Yoon | Postdoctoral Researchers and Research Professors | Professor, Department of Chemistry, Hannam University, Daejeon, Korea. |
| Wan-Joong Kim | Postdoctoral Researchers and Research Professors | Researcher, KRISS, Daejeon, Korea. |
| Young Hwan Jung | Postdoctoral Researchers and Research Professors | Professor, Korea Bio Polytechnic, Nonsan, Korea. |
| Sungjin Park | Postdoctoral Researchers and Research Professors | Professor, Department of Chemistry and Physics, Inha University, Incheon, Korea. |
| Sunghoon Joo | Postdoctoral Researchers and Research Professors | Researcher, Samsung SDS, Suwon, Korea. |
| Gyeongwon Yun | Postdoctoral Researchers and Research Professors | Patent Examiner, Korean Intellectual Property Office (KIPO), Daejeon, Korea. |
| Kyung-Bok Lee | Ph.D. Students | Researcher, KBSI, Daejeon, Korea. |
| Dong Jin Kim | Ph.D. Students | Researcher, HAESUNG DS, Changwon, Korea. |
| Joon Sung Lee | Ph.D. Students | Professor, Department of Applied Physics, Korea University, Sejong, Korea. |
| Young Shik Chi | Ph.D. Students | Researcher, Samsung Electro-Mechanics, Suwon, Korea. |
| Woo Kyung Cho | Ph.D. Students | Professor, Department of Chemistry, Chungnam National University, Daejeon, Korea. |
| Bong Soo Lee | Ph.D. Students | Researcher, S&G Biotech, Inc., Yongin, Korea. |
| Hyung Ju Park | Ph.D. Students | Researcher, ETRI, Daejeon, Korea. |
| Bokyung Kong | Ph.D. Students | Researcher, Corning, Korea. |
| Sung Min Kang | Ph.D. Students | Professor, Department of Chemistry, Chungbuk National University, Chungbuk, Korea. |
| Sung Ho Yang | Ph.D. Students | Professor, Department of Chemistry Education, Korea National University of Education, Chungbuk, Korea. |
| Kyungtae Kang | Ph.D. Students | Professor, Department of Applied Chemistry, Kyung Hee University, Yongin, Korea. |
| Daewha Hong | Ph.D. Students | Professor, Pusan National University, Busan, Korea. |
| Ji Hun Park | Ph.D. Students | Professor, Ewha Womans University, Seoul, Korea. |
| Juno Lee | Ph.D. Students | Researcher, Agency for Defense Development, Daejeon, Korea. |
| Eun Hyea Ko | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Beom Jin Kim | Ph.D. Students | Professor, Department of Chemistry, Dongguk University, Seoul, Korea. |
| Mi-Hee Kim | Ph.D. Students | USA. |
| Matthew Park | Ph.D. Students | Researcher, Amgen, Inc., Los Angeles, USA. |
| Taegyun Park | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Ji Yu Choi | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Hyunsuk Kim | Ph.D. Students | Researcher, Agency for Defense Development, Daejeon, Korea. |
| Ji Yup Kim | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Hojae Lee | Ph.D. Students | Professor, Department of Chemistry, Hallym University, Chuncheon, Korea. |
| Hee Chul Moon | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Hyeoncheol Cho | Ph.D. Students | Researcher, Samsung SDS, Seoul, Korea. |
| Jeongyeon Seo | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Wongu Youn | Ph.D. Students | Researcher, Center for Cognition and Sociality, Institute for Basic Science, Daejeon, Korea. |
| Sol Han | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Jungnam Kim | Ph.D. Students | Researcher, Samsung Electronics, Hwaseong, Korea. |
| Joohyouck Park | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Inae Han | Ph.D. Students | Researcher, The Armed Force CBR Defense Command, Seoul, Korea. |
| Seoin Yang | Ph.D. Students | Researcher, Samsung Electronics, Suwon, Korea. |
| Jihoo Kim | Ph.D. Students | Postdoctoral Researcher, M-Design Lab, KAIST, Daejeon, Korea. |
| Nayoung Kim | Ph.D. Students | Postdoctoral Researcher, Chemistry, Materials Science & Engineering and Biomedical Engineering, Northwestern University, USA. |
| Nam-Jung Kang | M.S. Students | Researcher, Samsung Electronics. |
| Jungkyu K. Lee | M.S. Students | Professor, Department of Chemistry, Kyungpook National University, Daegu, Korea. |
| Yong-Won Lee | M.S. Students | College of Law, Korea University. |
| Ganghyuk Jung | M.S. Students | School of Medicine, Kyung Hee University. |
| Sang-min Cho | M.S. Students | Researcher, STX Corporation. |
| Jae Young Park | M.S. Students | Researcher, SK Innovation. |
| Seung Pyo Jeong | M.S. Students | Ph.D., University of Massachusetts Amherst, USA. |
| Mi Rae Kim | M.S. Students | School of Medicine. |
| Jin Kyu Kim | M.S. Students | Researcher, Cheil Industries. |
| Baekhap Choi | M.S. Students | Researcher, SK Hynix. |
| HwaJin Yun | M.S. Students | Researcher, LG Display. |
| Ki Eun Bae | M.S. Students | Researcher, SK Hynix. |
| Hyelin Seo | M.S. Students | Researcher, SK Hynix. |
| Juan Kim | M.S. Students | Researcher, Samsung Electronics. |
| Sohee Choi | M.S. Students | Researcher, LG Innotek. |
| Won Il Kim | M.S. Students | Researcher, SK Innovation. |
| Yeji Kim | M.S. Students | Researcher, Samsung Electronics. |

## 최근 논문 목록 (2021–2026)

세포 피포화와 표면 재료, 신경세포 배양·발달, 분자 예측과 코돈 설계 방법을 다룬 논문이다. 제목·저자·발표처는 랩 게시 표기를 따랐다. arXiv Preprint는 사전 공개본이다. 날짜 없이 2026년 구역에 있는 「Iron Gall Ink Revisited: Visible Light-Induced Supramolecular Assembly…」는 랩 표기에 따라 게재 승인으로 구분했다.[^pubs]

**2026**

- Choi, H.; Han, S. Y.; Kim, N.; Lee, S.-H.; Lee, K.-B.; Choi, I. S. "Iron Gall Ink Revisited: Visible Light-Induced Supramolecular Assembly of Fe3+-Tannic Acid Complex in Asymmetric Single-Cell Nanoencapsulation". *Chem. Commun. 게재 승인*.
- Kamaraj, S.; Chen, D.; Zhang, B.; Jabeen, N.; Hegazy, M.; Choi, I. S.; Huang, X. "Engineering Abiotic–Biotic Interfaces for Solar-Driven Nitrogen Fixation: Challenges and Opportunities". *Mater. Today Energy 2026, 62, 102424*.
- Park, M. J.; Han, S. Y.; Hong, S. E.; Choi, I. S.; Yoon, K. R. "Single-Cell Nanoencapsulation of Probiotics within Fe3+-Trimesic Acid Nanoshells for Effective Cytoprotection against Gastrointestinal Insults". *ACS Biomater. Sci. Eng. 2026, 12(10), 5443-5449*.
- Kozłowski, F.; Kim, N.; Choi, H.; Daniel, G.; Seisenbaeva, G. A.; Choi, I. S.; Kessler, V. G. "Synthesis and Characterization of Biocompatible Manganese-Doped Titania Nanoparticles and Its Application to Single-Cell Nanoencapsulation". *Adv. Mater. Interfaces 2026, 13(18), e70649*.
- Rheem, H.; Han, I.; Kim, S.; Han, S. Y.; Hong, D.; Choi, I. S.; Cho, W. K. "Synthesis of an Azide-Bearing L-DOPA for Click-Based Antifouling Surface Functionalization". *Synthesis 2026, 58(15), 1761-1769*.
- Jeong, Y.; Choi, H.; Hariri, R. F. M.; Lee, E. K.; Lee, S. S.; Choi, I. S. "Smooth %MinMax: A Differentiable Relaxation for Codon Harmonization". *arXiv Preprint 2026, arXiv:2607.03881*.
- Jeong, Y.; Yang, C.; Hariri, R. F. M.; Kim, J.; Lee, E. K.; Lee, Y.; Kim, W. J.; Lee, S. S.; Choi, I. S. "MOSAIC: Codon Harmonization of Monte Carlo-Based Simulated Annealing for Linked Codons in Heterologous Protein Expression". *ACS Synth. Biol. 2026, 15(6), 2293-2301*.
- Nguyen, D. T.; Kim, N.; Han, S. Y.; Choi, H.; Choi, I. S. "Cell-in-Shell Metacells in Single-Cell Nanoencapsulation". *ChemPlusChem 2026, 91(4), e202500586*.
- Han, I.; Rheem, H.; Han, S. Y.; Kim, J.; Choi, I. S. "Surface-Initiated ARGET ATRP of Zwitterionic Carboxybetaine Methacryloyl Ethylenediamine in Formation of Ultralow-Biofouling Films". *Bull. Korean Chem. Soc. 2026, 47(3), 240-244*.
- Kim, S.; Park, J.; Kim, N.; Hong, S.-P.; Rheem, H. B.; Choi, I. S.; Cho, W. K.; Lee, H. "Material-Independent Film Formation of Zr4+-Trimesic Acid Metal-Organic Complexes and Their Antifouling Applications". *ACS Appl. Mater. Interfaces 2026, 18(3), 6026-6035*.

**2025**

- Rhee, S. Y.; Nguyen, D. T.; Han, S. Y.; Klementiev, K.; Youn, W.; Yun, G.; Kwon, Y.; Han, S. W.; Kim, J. H.; Kim, T.-S.; Lee, H.; Seisenbaeva, G. A.; Kessler, V. G.; Choi, I. S. "Boric Acid-Mediated Sol-Gel Construction of Transparent, Photoactive TiO2 Films". *Chem. Commun. 2025, 61(91), 17938-17941*.
- Hwang, J. M.; Shin, Y.-C.; Amasanaa, E.; Kim, N.; Hong. S.-P.; Choi, I. S.; Kim, Y. H.; Seong, H.-A.; Myung, K.; Lee, Z.-W.; Lee, K.-B. "Live-Cell Imaging of the Binding between a Chemical Drug and Its Target Proteins Based on Intracellular Redistribution of the Target Proteins". *Bioconjugate Chem. 2025, 36(11), 2330-2335*.
- Han, S. Y.; Jeong, Y.; Lee, H.; Choi, I. S. "Single-Cell Nanoencapsulation of Saccharomyces cerevisiae with Metal-Organic Complex Nanoshells of Fe3+ and Benzenehexacarboxylic Acid". *Bull. Korean Chem. Soc. 2025, 46(11), 1088-1092*.
- Rheem, H. B.; Kim, N.; Nguyen, D. T.; Baskoro, G. A.; Roh, J. H.; Lee, J. K.; Kim, B. J.; Choi, I. S. "Single-Cell Nanoencapsulation: Chemical Synthesis of Artificial Cell-in-Shell Spores". *Chem. Rev. 2025, 125(13), 6366-6396*.
- Kim, N.; Han, S. Y.; Rheem, H. B.; Lee, H.; Choi, I. S. "Autonomous Chemo-Metabolic Construction of Anisotropic Cell-in-Shell Nanobiohybrids in Enzyme-Powered Cell Microrobots". *Sci. Adv. 2025, 11(26), eadu5451*.
- Nguyen, D. T.; Han, S. Y.; Choi, H.; Kim, N.; Seisenbaeva, G. A.; Kessler, V. G.; Choi, I. S. "Ultrafast, Cytocompatible Mineralization of Calcium Phosphate in the Formation of Stratified Nanoshells of Artificial Spores". *Chem. Commun. 2025, 61(37), 6771-6774*.
- Han, S. Y.; Kim, N.; Nguyen, D. T.; Yang, S.; Kang, E. K.; Baskoro, G. A.; Lee, S.-H.; Lee, K.-B.; Kim, B. J.; Choi, I. S. "Cytoprotective Nanoencapsulation of Probiotic Cells within Fe3+-Phytic Acid Nanoshells". *Langmuir 2025, 41(16), 10625-10631*.
- Rheem, H. B.; Nguyen, D. T.; Choi, I. S. "Material-Independent Film Formation and Autonomous Degradation of Cu2+-Tetrahydroxy-1,4-Benzoquinone Metal-Organic Complexes". *Nanoscale 2025, 17(3), 1652-1658*.
- Yang, S.; Youn, W.; Rheem, H. B.; Han, S. Y.; Kim, N.; Han, S.; Schattling, P.; Stadler, B.; Choi, I. S. "Construction of Liposome-Based Extracellular Artificial Organelles on Individual Living Cells". *Angew. Chem. Int. Ed. 2025, 64(3), e202415823*.
- Jung, Y. J.; Choi, H.; Choi, I. S.; Lee, J. K. "Biocompatible Hydrogel Coating on Single Living Cells through Visible Light-Induced Polymerization". *Chem. Commun. 2025, 61(2), 322-325*.

**2024**

- Choi, H.; Rheem, H. B.; Nguyen, D. T.; Han, S. Y.; Lee, H.; Choi, I. S. "Iron Gall Ink Revisited: Visible Light-Induced, Eosin-Mediated Acceleration of Fe2+ Oxidation in Pattern Nanoarchitectonics of Fe3+-Tannic Acid Films". *Langmuir 2024, 40(43), 23033-23040*.
- Vardanyan, A.; Zhou, G.; Kim, N.; Budnyak, T. M.; Kessler, V.; Choi, I. S.; Huang, Z.; Seisenbaeva, G. A. "Transformation of Europium Metal-Organic Framework from 3D via 2D into Exfoliating 3D for Enzyme Immobilization". *Commun. Mater. 2024, 5(1), 187*.
- Nguyen, D. T.; Han, S. Y.; Kozlowski, F.; Seisenbaeva, G. A.; Kessler, V. G.; Kim, B. J.; Choi I. S. "Biphasic Water-Oil Systems for Functional Augmentation of Probiotic Lactobacillus acidophilus Nanoencapsulated in Luteolin-Fe3+ Shells". *Chem. Commun. 2024, 60(40), 5330-5333*.
- Kim, J.; Choi, H.; Yang, S.; Choi, I. S. "Promoting Effects of Cannabidiol on Neurite Growth and Neuronal Development in Neuron-Astrocyte Sandwich Coculture". *Bull. Korean Chem. Soc. 2024, 45(1), 55-59*.
- Park, J.; Kim, N.; Han, S. Y.; Rhee, S. Y.; Nguyen, D. T.; Lee, H.; Choi, I. S. "A Micrometric Transformer: Compositional Nanoshell Transformation of Fe3+-Trimesic-Acid Complex with Concomitant Payload Release in Cell-in-Catalytic-Shell Nanobiohybrids". *Adv. Sci. 2024, 11(1), 2306450*.
- Kim, J.; Jeong, Y.; Kim, W. J.; Lee, E. K.; Choi, I. S. "MolNet_Equi: A Chemically Intuitive, Rotation-Equivariant Graph Neural Network". *Chem. Asian J. 2024, 19(1), e202300684*.

**2023**

- Han, S.; Kim, J.; Kim, S. H.; Youn, W.; Kim, J.; Ji, G. Y.; Yang, S.; Park, J.; Lee, G. M.; Kim, Y.; Choi, I. S. "In Vitro Induction of In Vivo-Relevant Stellate Astrocytes in 3D Brain-Derived, Decellularized Extracellular Matrices". *Acta Biomater. 2023, 172, 218-233*.
- Han, S. Y.; Kim, N.; Yun, G.; Lee, H.; Choi, I. S. "Tandem-Biocatalysis Reactors Constructed by Topological Evolution of CaCO3 Particles into Hollow Metal Hydroxide Spheres". *Nat. Commun. 2023, 14(1), 6828*.
- Kim, J.; Yang, S.; Choi, I. S. "Neutralization of Cannabidiol Neurotoxicity in Neuron-Astrocyte Sandwich Coculture". *Adv. Biol. 2023, 7(1), 202300090*.
- Rheem, H. B.; Choi, H.; Yang, S.; Han, S.; Rhee, S. Y.; Jeong, H.; Lee, K.-B.; Lee, Y.; Kim, I.-S.; Lee, H.; Choi, I. S. "Fugetaxis of Cell-in-Catalytic-Coat Nanobiohybrids in Glucose Gradients". *Small 2023, 19(41), 2301431*.
- Nguyen, D. T.; Han, S. Y.; Yun, G.; Lee, H.; Choi, I. S. "Vortex-Assisted, Nanoarchitectonic Manipulation of Microparticles with Flavonoid-Fe3+ Complex in Biphasic Water-Oil Systems". *Chem. Commun. 2023, 59(31), 4612-4615*.
- Yang, S.; Choi, H.; Nguyen, D. T.; Kim, N.; Rhee, S. Y.; Han, S. Y.; Lee, H.; Choi, I. S. "Bioempowerment of Therapeutic Living Cells by Single-Cell Surface Engineering". *Adv. Therap. 2023, 6(7), 2300037*.
- Han, S. Y.; Yun, G.; Cha, H.-M.; Lee, M. K.; Lee, H.; Kang, E. K.; Hong, S.-P.; Teahan, K. A.; Park, M.; Hwang, H.; Lee, S. S.; Kim, M.; Choi, I. S. "A Natural Virucidal and Microbicidal Spray Based on Polyphenol-Iron Sols". *ACS Appl. Bio Mater. 2023, 6(5), 1981-1991*.
- Han, S. Y.; Nguyen, D. T.; Kim, B. J.; Kim, N.; Kang, E. K.; Park, J. H.; Choi, I. S. "Cytoprotection of Probiotic Lactobacillus acidophilus with Artificial Nanoshells of Nature-Derived Eggshell Membrane Hydrolysates and Coffee Melanoidins in Single-Cell Nanoencapsulation". *Polymers 2023, 15(5), 1104*.

**2022**

- Kim, Y.; Jeong, Y.; Kim, J.; Lee, E. K.; Kim, W. J.; Choi, I. S. "MolNet: A Chemically Intuitive Graph Neural Network for Prediction of Molecular Properties". *Chem. Asian J. 2022, 17(16), e202200269*.
- Lee, H.; Park, J.; Kim, N.; Youn, W.; Yun, G.; Han, S. Y.; Nguyen, D. T.; Choi, I. S. "Cell-in-Catalytic-Shell Nanoarchitectonics: Catalytic Empowerment of Individual Living Cells by Single-Cell Nanoencapsulation". *Adv. Mater. 2022, 34(30), 2201247*.
- Jeong, Y.; Kim, J.; Kim, Y.; Choi, I. S. "Development of A Chemically Intuitive Filter for Chemical Graph Convolutional Network". *Bull. Korean Chem. Soc. 2022, 43(7), 934-936*.
- Han, S. Y.; Yun, G.; Nguyen, D. T.; Kang, E. K.; Lee, H.; Kim, S.; Park, J. H.; Kim, B. J.; Choi, I. S. "Hydrogen Bonding-Based Layer-by-Layer Assembly of Nature-Derived Eggshell Membrane Hydrolysates and Coffee Melanoidins in Single-Cell Nanoencapsulation". *ChemNanoMat 2022, 8(5), e202100535*.

**2021**

- Lee, H.; Nguyen, D. T.; Kim, N.; Han, S. Y.; Hong, Y. J.; Yun, G.; Kim, B. J.; Choi, I. S. "Enzyme-Mediated Kinetic Control of Fe3+-Tannic Acid Complexation for Interface Engineering". *ACS Appl. Mater. Interfaces 2021, 13(44), 52385-52394*.

## 수상

2021년 10월 13일부터 2026년 10월 13일까지의 누리집 소식에 실린 수상이다.[^news]

- 2024-11-20 · HyeongBin Rheem, KAIST Department Seminar 2024의 Excellent Thesis Award 수상

## 소식

2021년 10월 13일부터 2026년 10월 13일까지의 게시 날짜를 기준으로 적었다.[^news]

- 2026-07-29 · AZ-DOPA를 이용한 오염 방지 표면 기능화 논문이 Synthesis에 게재됐다.
- 2026-06-19 · 연결된 코돈 집합을 다루는 코돈 조화 알고리즘 MOSAIC 논문이 ACS Synthetic Biology에 게재됐다.
- 2026-04-18 · 메타셀 개념 논문이 ChemPlusChem에 게재됐다.
- 2026-03-20 · 표면 개시 중합으로 오염 방지 고분자 막을 형성하는 논문이 Bulletin of the Korean Chemical Society에 게재됐다.
- 2026-02-23 · HyeongBin Rheem이 Schmidt Science Fellows 2026의 Finalist로 선정됐다.
- 2025-11-25 · 붕산을 이용한 산화타이타늄 막 형성 논문이 Chemical Communications에 게재됐다.
- 2025-07-09 · 인공 포자의 재료와 합성 방법을 정리한 총설이 Chemical Reviews에 게재됐다.
- 2025-06-27 · 세포 대사와 껍질 형성을 결합한 세포 미세 로봇 논문이 Science Advances에 게재됐다.
- 2025-05-07 · 인산칼슘 다층 껍질 형성 논문이 Chemical Communications에 게재됐다.
- 2025-04-29 · 철 이온·피트산 껍질로 생균을 피포화하는 논문이 Langmuir에 게재됐다.
- 2025-01-21 · 구리 이온과 유기 분자의 복합체로 막을 만들고 분해하는 논문이 Nanoscale에 게재됐다.
- 2025-01-15 · 리포솜 기반 세포 외 인공 소기관 논문이 Angewandte Chemie International Edition에 게재됐다.
- 2025-01-07 · 가시광 중합으로 살아 있는 세포에 하이드로겔을 코팅하는 논문이 Chemical Communications에 게재됐다.
- 2024-10-17 · 빛과 에오신을 이용해 철 이온의 산화를 촉진하고 막 무늬를 만드는 논문이 Langmuir에 게재됐다.
- 2024-06-07 · 물·기름 계에서 세포 껍질로 생균에 기능을 더하는 논문이 Chemical Communications에 게재됐다.
- 2024-01-29 · 초기 신경세포 발달에서 칸나비디올의 작용을 다룬 논문이 Bulletin of the Korean Chemical Society에 게재됐다.
- 2024-01-02 · 껍질 조성을 바꾸면서 물질을 방출하는 논문이 Advanced Science에 게재됐다.
- 2024-01-02 · MolNet_Equi 논문이 Chemistry – An Asian Journal에 게재됐다.
- 2023-12-01 · 뇌 유래 세포외기질을 이용한 별아교세포 입체 배양 논문이 Acta Biomaterialia에 게재됐다.
- 2023-10-26 · 연속 생촉매 반응기 논문이 Nature Communications에 게재됐으며 Nature Catalysis에 소개됐다.
- 2023-10-22 · 신경세포·별아교세포 공동배양 플랫폼 논문이 Advanced Biology에 게재됐다.
- 2023-10-11 · 세포의 촉매 코팅으로 이동 방향을 조절하는 논문이 Small에 게재됐다.
- 2023-07-28 · 물과 기름이 나뉜 계에서 미세 입자를 조절하는 논문이 Chemical Communications에 게재됐다.
- 2023-07-13 · 단일 세포 표면 공학의 화학적 기능화 전략을 정리한 총설이 Advanced Therapeutics에 게재됐다.
- 2023-04-21 · 폴리페놀·철 이온 졸을 이용한 분무 제형 논문이 ACS Applied Bio Materials에 게재됐다.
- 2023-02-22 · 난각막 가수분해물과 커피 멜라노이딘 껍질로 생균을 보호하는 논문이 Polymers에 게재됐다.
- 2022-08-15 · MolNet 논문이 Chemistry – An Asian Journal에 게재됐다.
- 2022-07-27 · 촉매 기능을 가진 껍질로 개별 세포에 기능을 더하는 논문이 Advanced Materials에 게재됐다.
- 2022-07-19 · 화학 그래프 합성곱 신경망의 필터 개발 논문이 Bulletin of the Korean Chemical Society에 게재됐다.
- 2022-05-01 · 자연 유래 재료의 층별 조립을 이용한 단일 세포 피포화 논문이 ChemNanoMat에 게재됐다.
- 2021-11-01 · 효소로 철 이온과 탄닌산의 결합 반응 속도를 조절하는 논문이 ACS Applied Materials & Interfaces에 게재됐다.

## 연락과 위치

- 소속과 주소: Department of Chemistry, KAIST, 291 College Road, Yuseong-gu, Daejeon 34141, Korea.[^home]
- 홈페이지: <http://cisgroup.kaist.ac.kr/>

## 각주
[^home]: 연구실 첫 화면. <http://cisgroup.kaist.ac.kr/> 관측일 2026-10-30.
[^people]: 연구실 People, Principal Investigator·Researchers·Students·Alumni. <http://cisgroup.kaist.ac.kr/people.html> 관측일 2026-10-30.
[^research]: 연구실 Research. <http://cisgroup.kaist.ac.kr/research.html> 관측일 2026-10-30.
[^pubs]: 연구실 Publications, 2021–2026년 구역. <http://cisgroup.kaist.ac.kr/publications.html> 관측일 2026-10-30.
[^news]: 연구실 News. <http://cisgroup.kaist.ac.kr/news.html> 관측일 2026-10-30.
[^p1]: N. Kim 외, I. S. Choi, Science Advances 11, eadu5451 (2025). <https://doi.org/10.1126/sciadv.adu5451> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1126/sciadv.adu5451> 관측일 2026-10-31.
[^p2]: J. Park 외, I. S. Choi, Advanced Science 11, 2306450 (온라인 2023-10-31). <https://doi.org/10.1002/advs.202306450> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/advs.202306450> 관측일 2026-10-31.
[^p3]: H. Rheem 외, W. K. Cho, Synthesis 58, 1761-1769 (온라인 2026-05-20). <https://doi.org/10.1055/a-2839-6271> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1055/a-2839-6271> 관측일 2026-10-31.
[^p4]: Y. Kim 외, I. S. Choi, arXiv 사전 공개본 v1, 2203.09456 (온라인 2022-02-01). <https://doi.org/10.48550/arXiv.2203.09456> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2203.09456> 관측일 2026-10-31.
[^p5]: S. Han 외, I. S. Choi, Acta Biomaterialia 172, 218-233 (2023). <https://doi.org/10.1016/j.actbio.2023.09.046> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.actbio.2023.09.046%22> 관측일 2026-10-31.
[^p6]: Y. Jeong 외, I. S. Choi, ACS Synthetic Biology 15, 2293-2301 (온라인 2026-05-14). <https://doi.org/10.1021/acssynbio.5c00844> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4416339362> 관측일 2026-10-31.
[^development]: J. Kim 외, I. S. Choi, Bulletin of the Korean Chemical Society 45(1), 55–59 (온라인 2023-10-30). <https://doi.org/10.1002/bkcs.12795> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/bkcs.12795> 관측일 2026-10-31.

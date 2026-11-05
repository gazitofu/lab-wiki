# KAIST 분자 모사 연구실 (Molecular Simulation Group)

**KAIST 생명화학공학과 · 김지한 교수**

- 분야: 계산화학, 분자 모사, 소재 역설계, 연구 자동화, 양자 계산, 기체 분리·저장
- 대분야: 소재, 컴퓨팅·AI
- 태그: 다공성 골격 소재(MOF·COF)[^research], 복합재료[^research], 과학·공학 AI[^research], 대형 언어 모델[^research], 양자 컴퓨팅[^research], 탄소 포집·저장[^home][^p7], 이산화탄소 전환[^research]
- 홈페이지: <https://molsim.kaist.ac.kr/>
- 근거와 출처: [KAIST 분자 모사 연구실 근거 페이지](molsim-sources.md)

> 컴퓨터 계산과 인공지능으로 원하는 성질의 재료를 설계하고, 탄소 포집·기체 저장·전지에 쓸 소재를 찾으며 계산화학 연구 자체를 자동화하는 연구실이다.[^home][^research]

## 무엇을 연구하나

김지한 교수가 이끄는 계산화학 연구실이다.[^faculty][^people] 계산화학은 물질의 구조와 성질, 반응을 컴퓨터로 계산하는 분야다. 원자(화학 원소의 성질을 유지하는 기본 단위)와 분자(원자들이 화학 결합으로 연결된 독립된 입자)의 거동을 계산으로 재현하는 분자 모사를 바탕으로, 에너지(일을 할 수 있는 능력을 나타내는 물리량)·환경 문제에 쓸 재료를 찾는다. 연구실은 탄소 포집(공기나 배출 기체 등에서 이산화탄소를 붙잡아 모으는 기술), 메탄·수소 저장, 전지를 목표 응용으로 들고, 이를 위해 정확하고 효율적인 계산 모형을 개발한다고 소개한다.[^home]

한 갈래는 원하는 성질을 먼저 정한 뒤 그 성질을 낼 재료를 찾는 역설계다. 금속유기골격체(Metal-Organic Framework, MOF; 금속과 유기 연결체가 결합해 규칙적인 구멍을 이루는 결정성 물질) 등 여러 소재를 대상으로, 분자 모사 기법과 기계학습(자료에서 규칙을 학습해 예측이나 결정을 수행하는 계산 방법) 모델을 개발한다.[^research] 기체를 담거나 분리하는 재료에서는 구멍의 구조가 달라질 때 성질이 어떻게 바뀌는지가 연구 대상이다. 예를 들어 유연한 골격을 설계한 논문은 기체를 넣고 빼는 동안 활용할 수 있는 저장량이 클 가능성이 있는 메탄·수소 저장 후보를 제안했다.[^p5]

다른 갈래는 연구 과정의 자동화다. 글·이미지·영상 자료를 자동으로 모으고, 대형 언어 모델(Large Language Model, LLM; 많은 글을 학습해 글을 이해하고 생성하는 인공지능 모델)을 연구 수행에 맞게 조정한다. 물이나 열에 대한 소재의 안정성처럼 기존 분자 모사만으로 쉽게 얻기 어려운 성질도 다룬다.[^research] ChatMOF는 사람이 일상적인 문장으로 요청하면 자료 검색, 성질 예측, 구조 생성을 수행하는 시스템이다.[^p4] 문헌의 표와 본문에서 실험 자료를 추출해 정리하고, 이를 합성 조건 추천에 연결하는 방법도 개발했다.[^p3] 최근에는 같은 MOF 이름을 가진 시료(분석이나 실험에 쓰는 물질의 일부)라도 실제 구조 상태가 다를 수 있다는 점을 반영해, 실험 측정 자료와 소재의 식별 정보를 함께 사용하는 예측 모델을 제안했다.[^p1]

양자 컴퓨팅(입자의 상태가 겹치고 서로 연결되는 양자 현상을 계산에 이용하는 방식)을 소재 설계에 연결하는 연구도 한다. 목표 성질을 갖는 소재를 생성하는 양자 기계학습 모델과, 소재의 구조·조성 제약을 반영해 구성을 최적화하는 계산 모형을 개발한다.[^research] 여러 종류의 연결체가 섞인 다공성 소재를 다룬 대표 논문에서는 구성 비율과 구조, 균형 조건을 모형에 함께 넣어 안정한 배치를 찾았고, 모의 계산과 실제 양자 장치에서 방법을 검증했다.[^p2]

복합재료(성질이 다른 재료를 구분되는 영역으로 합쳐 만든 재료)에서는 MOF와 다른 MOF, 또는 고분자(반복되는 구성 단위가 화학 결합으로 이어진 큰 분자로 이루어진 물질)를 조합하고, 구성 재료 사이의 상호작용이 합쳐진 성질을 만드는 원인을 연구한다. 또한 기체 분리·저장과 이산화탄소를 다른 물질로 바꾸는 전환을 목표로, 많은 후보를 계산으로 가려내고 소재 자료집을 구축한다.[^research] 두 차원의 MOF와 세 차원의 MOF를 연결할 조합을 찾는 계산 방법,[^p6] 규칙적인 배열이 사라진 MOF의 자료집을 만들고 대기 중 이산화탄소 포집에 유리한 후보를 찾는 방법이 그 예다.[^p7]

## 주요 연구 주제

### 1. 소재 예측과 계산화학 연구의 자동화

언어 모델이 문헌 자료를 정리하고 계산 도구를 연결하도록 만드는 연구다. 실험 자료와 계산 자료의 차이를 분석하는 연구와, 같은 골격이라도 시료 상태가 다르면 성질을 다르게 예측하는 모델 연구가 이 갈래에 속한다.[^research][^p1][^p3][^p4]

### 2. 역설계와 양자 계산

목표 성질을 입력으로 받아 재료를 생성하고, 구성 요소의 배치를 결정한다. 양자 계산 모형에 구조와 조성의 제약을 함께 반영하는 방법을 개발한다.[^research][^p2]

### 3. 복합재료의 연결과 상호작용

서로 다른 MOF나 고분자를 결합할 조합을 찾고, 합성 가능성과 구성 재료 사이의 상호작용을 살핀다. 서로 다른 차원의 골격을 연결하는 계산 알고리즘(문제를 풀기 위해 정한 계산 절차)도 연구한다.[^research][^p6]

### 4. 탄소 포집과 기체 분리·저장 소재

기체를 넣고 뺄 수 있는 유연한 골격을 설계하고, 대기 중 이산화탄소를 붙잡을 후보를 찾는다. 계산으로 가려낸 소재를 실험 연구자와의 공동 연구에 연결하는 것을 목표로 한다.[^home][^research][^p5][^p7]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 김지한 교수가 교신저자이고 마지막 저자인 논문을 연구 갈래별로 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸의 공동 1저자 표시는 연구실 목록의 범례를 따른다.[^pubs]

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Multimodal Transformer for Sample-Aware Prediction of Metal–Organic Framework Properties](https://doi.org/10.1021/acscentsci.6c01049) · ACS Central Science | 같은 MOF라도 시료의 결정 상태나 결함에 따라 성질이 달라지는 문제를 다뤘다. 소재 식별 정보와 X선 회절(물질에 X선을 쬐었을 때 원자 배열 때문에 방향이 바뀐 X선이 만드는 무늬로 구조를 알아보는 방법) 자료를 함께 쓰는 EXIT(Experimental X-ray Diffraction Integrated Transformer) 모델을 제안했다. 가상 MOF 100만 개로 먼저 학습한 뒤 실험 자료에 맞춰 학습했으며, 같은 골격이라도 회절 무늬가 다르면 서로 다른 예측값을 내는 것을 사례 분석으로 보였다.[^p1] | 공동 1저자 Seunghee Han·Jaewoong Lee, 교신저자 김지한 |
| 2 | 2025 | [Quantum Computing Based Design of Multivariate Porous Materials](https://doi.org/10.1021/acscentsci.5c00918) · ACS Central Science | 여러 연결체가 섞인 다공성 소재의 안정한 배치를 찾기 위해, 조성·구조·균형 제약을 함께 담은 양자 계산 모형을 제안했다. 알려진 소재의 안정한 배치를 모의 계산으로 재현했고, 실제 IBM 양자 장치에서도 검증 계산을 수행했다.[^p2] | 공동 1저자 Shinyoung Kang·Young-Hun Kim, 교신저자 김지한 |
| 3 | 2025 | [Harnessing Large Language Models to Collect and Analyze Metal–Organic Framework Property Data Set](https://doi.org/10.1021/jacs.4c11085) · Journal of the American Chemical Society | 여러 대형 언어 모델을 이어 문헌의 표와 글에서 MOF의 합성 조건과 성질을 추출해 정리했다. 실험과 계산 자료 사이의 차이를 분석하고, 주어진 출발 물질에 맞는 합성 조건을 제안하는 추천 시스템도 개발했다.[^p3] | 공동 1저자 Yeonghun Kang·Wonseok Lee·Taeun Bae, 교신저자 김지한 |
| 4 | 2024 | [ChatMOF: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models](https://doi.org/10.1038/s41467-024-48998-4) · Nature Communications | 사람이 일상적인 문장으로 묻거나 원하는 성질을 말하면, 언어 모델이 요청을 해석해 자료 검색·성질 예측·구조 생성을 수행하는 시스템을 만들었다. 작업을 수행하는 부분, 도구 모음, 결과를 평가하는 부분을 연결했고, 사용자가 원하는 성질을 갖는 소재를 생성했다.[^p4] | 1저자 Yeonghun Kang, 교신저자 김지한 |
| 5 | 2024 | [Data-Driven Design of Flexible Metal–Organic Frameworks for Gas Storage](https://doi.org/10.1021/acs.chemmater.4c00398) · Chemistry of Materials | 구조가 유연하게 변할 가능성이 있는 MOF 자료집을 만들고, 메탄과 수소를 저장할 후보를 분자 모사로 가려냈다. 기체를 넣고 빼는 조건 사이에서 활용할 수 있는 저장량이 클 가능성이 있는 후보를 제안했다. 결과는 계산에 바탕을 둔 합성 후보 제안이다.[^p5] | 공동 1저자 Yunsung Lim·Baekjun Kim, 교신저자 김지한 |
| 6 | 2023 | [Computational Discovery for Crafting Multi-Dimensional and Multi-Functional Metal–Organic Framework Composites](https://doi.org/10.1021/acs.jpcc.3c03814) · The Journal of Physical Chemistry C | 각 골격의 기하 정보를 이용해 두 차원 MOF와 세 차원 MOF를 연결할 조합을 찾는 방법을 개발했다. 합성 가능성을 우선해 후보를 골랐고, 이미 합성된 조합도 후보에 포함됐다. 방법을 통과한 후보는 구조가 맞지 않는 조합보다 높은 기계적 강도를 보였다.[^p6] | 1저자 Mingyu Jeon, 교신저자 김지한 |
| 7 | 2025 | [Amorphous Metal–Organic Framework Database for Amorphization Prediction and CO2 Direct Air Capture Screening](https://doi.org/10.1021/acsami.5c14534) · ACS Applied Materials & Interfaces | 비정질(구성 입자가 장거리에 걸쳐 규칙적으로 반복 배열되지 않은 고체 상태) MOF를 탐색하기 위해, 녹인 뒤 빠르게 식히는 과정을 모사해 구조 자료집을 만들었다. 이 자료로 열에 의해 비정질로 바뀌기 쉬운 소재를 예측하는 모델을 학습하고, 대기 중 이산화탄소 포집에 유리한 특징을 갖는 후보를 계산으로 찾았다.[^p7] | 1저자 Young-Hun Kim, 교신저자 김지한 |

## 교수와 전문 분야

김지한 교수는 KAIST 생명화학공학과 교수다. 2001년 University of California, Berkeley에서 전기공학·컴퓨터과학 학사, 2004년과 2009년 University of Illinois at Urbana-Champaign에서 전기·컴퓨터공학 석사와 박사 학위를 받았다. 이후 Lawrence Berkeley National Laboratories의 Computational Sciences Division과 Materials Sciences Division에서 박사후연구원으로 일했다.[^faculty][^people]

교수 소개는 분자 모사와 계산화학, 기계학습, 다공성 소재, 두 차원 소재를 전문 분야로 들고, 기체 저장·분리, 촉매, 센서, 물 포집을 연구 관심으로 적는다. 학과 소개는 계산화학, 나노소재 모사, 기계학습과 인공지능, 소재 설계, 소프트웨어 개발을 연구 분야로 제시한다.[^people][^faculty]

## 응용 분야

연구실이 내건 응용은 탄소 포집, 메탄·수소 저장, 전지다.[^home] 연구 소개에는 기체 분리와 이산화탄소 전환, 실험 합성에 적합한 소재 후보 발굴이 있고,[^research] 교수 소개에는 촉매·센서·물 포집도 있다.[^people] 대표 논문에서는 기체 저장 소재 후보 제안,[^p5] 대기 중 이산화탄소 포집 후보 탐색,[^p7] 소재 검색과 설계를 자동으로 수행하는 시스템이 구체적인 적용 사례다.[^p4]

## 구성원

2026년 11월 5일 People 페이지의 박사과정 11명과 석사과정 4명이다. 연구 주제와 학교 이메일은 해당 페이지의 표기이며, 시작 연월은 첫 화면의 합류 소식에 적힌 경우에만 표시한다.[^people][^home] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| 김준혁 (Junehyeok Kim) | 박사과정 |  | Machine Learning, Molecular Simulations | ghfkddl1998@kaist.ac.kr |  |
| 강신영 (Shinyoung Kang) | 박사과정 |  | Quantum Computing, Machine Learning, Molecular Simulations | shinyoung33@kaist.ac.kr | 2 |
| 김영훈 (Younghun Kim) | 박사과정 |  | Data-driven Materials Modeling | andy1220@kaist.ac.kr |  |
| 김도훈 (Dohoon Kim) | 박사과정 |  | Molecular Simulations | dhoonkim97@kaist.ac.kr |  |
| 금화연 (Hwayeon Kum) | 박사과정 |  | Machine Learning | flowerkite@kaist.ac.kr |  |
| 배태언 (Taeun Bae) | 박사과정 |  | Machine Learning | taeun8991@kaist.ac.kr | 3 |
| 황연희 (Yeun Hee Hwang) | 박사과정 |  | Molecular Simulation | hyh7689@kaist.ac.kr |  |
| 김준호 (Junho Kim) | 박사과정 |  | Machine Learning | kimjuneho4@kaist.ac.kr |  |
| 남경민 (Kyungmin Nam) | 박사과정 | 2026-03 | LLM Agent, Machine Learning | skarudals31@kaist.ac.kr |  |
| 이정우 (Jungwoo Lee) | 박사과정 |  | Molecular simulation | jwlee99@kaist.ac.kr |  |
| 강다연 (Dayeon Kang) | 박사과정 | 2026-08 | Molecular simulation | kdyeon@kaist.ac.kr |  |
| 김승우 (Seungwoo Kim) | 석사과정 | 2025-03 | Molecular simulation | tmddn998@kaist.ac.kr |  |
| 백유진 (Eugene Paek) | 석사과정 | 2025-03 | LLM Agent | lukie100@kaist.ac.kr |  |
| 고현정 (Hyunjung Kho) | 석사과정 | 2026-03 | Molecular simulation | khohj37@kaist.ac.kr |  |
| 채지훈 (Jihoon Chae) | 석사과정 | 2026-03 | Molecular simulation, Machine Learning | hoon8590@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 11월 5일 People 페이지 Alumni 구획의 28명이다. 학위·과정, 재학·재직 연도와 진로는 연구실 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Wooseok Jeong (정우석) | Ph.D. (2014-2018) | Korea Institute of Energy Research (한국에너지기술연구원) |
| Dooam Paik (백두암) | M.S. (2015-2017) | Postdoctoral researcher at KAIST (Prof. Hyungjun Kim) |
| Hoeyeon Kim (김희연) | M.S. (2017-2019) | Samsung SDI (삼성 SDI) |
| Bong Lim Suh (서봉임) | Ph.D./Postdoc (2015-2020) | Samsung Electronics (삼성 전자) |
| Youhan Lee (이유한) | M.S./Ph.D. (2014-2020) | NVIDIA (San Jose, USA) |
| Seunghee Lee (이승희) | M.S. (2018-2020) | Samsung Electronics Mechatronics R&D Center (삼성 전자 생산기술 연구소) |
| Seokwon Hyeon (현석원) | M.S./Ph.D. (2015-2021) | Samsung Electronics Memory Materials Technology Group (삼성 전자 소재기술 그룹) |
| Ohmin Kwon (권오민) | M.S./Ph.D./Postdoc (2014-2021) | Postdoctoral researcher at KAIST (Prof. Donghun Kim) |
| Sangwon Lee (이상원) | Ph.D./Postdoc (2016-2021) | LG Chem (LG 화학) |
| Sanghoon Park (박상훈) | M.S./Ph.D. (2015-2021) | Samsung Electronics (삼성 전자 메모리 사업부 Defect 제어 그룹) |
| Saad Aldin M. Ali Mohamed | Ph.D. (2018-2021) | Postdoctoral researcher at National University of Singapore (Prof. Jiang Jianwen) |
| Sanggyu Chong (정상규) | M.S./Ph.D. (2016-2022) | Senior R&T Scientist at Luxembourg Institute of Science and Technology (LIST) |
| Baekjun Kim (김백준) | M.S./Ph.D. (2016-2022) | Samsung Electronics (삼성전자) |
| Kyeongrim Kim (김경림) | M.S. (2021-2023) | Samsung Electronics (삼성전자) |
| Dayoung Ryu (류다영) | M.S. (2021-2023) | Samsung Electronics (삼성전자) |
| Hyunsoo Park (박현수) | M.S./Ph.D. (2017-2023) | Lila Sciences (Cambridge, USA) |
| Yoonseo Park (박윤서) | M.S. (2022-2024) | SK HYNIX (기반기술센터) |
| Wonseok Lee (이원석) | M.S./Ph.D. (2018-2024) | Samsung Electronics (삼성전자) |
| Junkil Park (박준길) | M.S./Ph.D. (2019-2024) | Postdoctoral researcher at Imperial College London (Prof. Aron Walsh) |
| Mingyu Jeon (전민규) | M.S./Ph.D. (2019-2024) | Assistant professor at the School of Chemical Engineering and Applied Chemistry of Kyungpook National University |
| Geonho Lee (이건호) | M.S. (2023-2024) | Student at Seoul National University |
| Yeonghun Kang (강영훈) | M.S./Ph.D. (2019-2025) | Assistant professor at the Department of Chemistry of Sungkyunkwan University |
| Yunsung Lim (임윤성) | M.S./Ph.D. (2020-2025) | Postdoctoral researcher at Seoul National University (Prof. Seungwu Han) |
| Honghui Kim (김홍희) | M.S./Ph.D. (2020-2026) | Postdoctoral researcher at KAIST (Prof. Sungsoo Ahn) |
| Huiwon Jang (장희원) | M.S./Ph.D. (2020-2026) | Postdoctoral researcher at MIT (Prof. Heather Kulik) |
| Jun Hee Woo (우준희) | M.S./Ph.D. (2020-2026) | 한국화학연구원 선임연구원 |
| Jaewoong Lee (이재웅) | M.S./Ph.D. (2020-2026) | Postdoctoral researcher at KAIST (Prof. Dong-Hwa Seo) |
| Seunghee Han (한승희) | M.S./Ph.D. (2021-2026) | Samsung Advanced Institute of Technology (SAIT) |

## 최근 논문 목록 (2021–2026)

연구실 Publications 페이지의 2021–2026년 연도 구역에서 KAIST 재직 시기의 논문 115편을 담았다. 연도 구역과 저자·제목·발표처는 연구실 표기이며, 등록 서지가 밝힌 날짜가 2021년 10월 13일–2026년 10월 13일인 항목을 대상으로 한다. 개별 날짜가 없는 항목은 연구실의 연도 구역을 따른다. 「게재 승인」은 출판 논문과 구분한 상태 표시이고, arXiv·ChemRxiv 발표처는 「연구실 기재」로 표시한다. #는 연구실이 밝힌 공동 1저자, *는 교신저자다.[^pubs]

**2026**

- J. Lee#, T. Bae#, J. Kim\*. "SimMOF: AI agent for Automated MOF Simulations". *Nature Communications (게재 승인), 2026*. [연구실 게시 링크](https://arxiv.org/abs/2603.29152).
- J. Park#, M. Lee#, S. Lee, H. Kum, Z. Ullah, H. Cho, J. Lee, S. Y. Kim, J. Kim, C. Boo, M. Son, C. Lee\*, J. Jang\*, J. Byun\*. "Decoupling wetting and transport in a photothermal-hydrovoltaic membrane for cascade conversion of wastewater ammonia". *Energy & Environmental Science, 2026*. DOI: <https://doi.org/10.1039/d6ee05465j>.
- Y. Ryu, J. Lee, J.-W. An, S. Y. Kim, H. Kum, J. Kim, H. Kwon\*, J. Jang\*. "Room-Temperature Selectivity Switching via Nanoporous Au Film-Integrated SnO2 Hybrid Sensors". *Small, e76126, 2026*. DOI: <https://doi.org/10.1002/smll.76126>.
- J. Kim. "Phenomenon-first problem formulation with language models in metal-organic frameworks". *arXiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.48550/arxiv.2610.04866>.
- J. Kim. "Reinterpreting Simulation Results for New Materials Applications with a Large Language Model". *ChemRxiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.26434/chemrxiv.15009527/v1>.
- J. Kim. "Divergent strategies and convergent outcomes in autonomous materials discovery". *arXiv, 2026 (연구실 기재)*. [연구실 게시 링크](https://arxiv.org/abs/2609.23957).
- J. Kim. "Editorial routing shapes how computational results are qualified in AI-assisted scientific writing". *arXiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.48550/arxiv.2609.14288>.
- J. Lee#, Y. Kim#, G.Lee, J. Kim\*. "PORMAKE2: Topology-Based Generation of Hypothetical Metal-Organic Frameworks through Single-Metal Nodes and Symmetry-Aware Linker Rotation". *ChemRxiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.26434/chemrxiv.15008555/v1>.
- J. Kim. "An Amdahl Framework for Agentic Computational Science". *ChemRxiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.26434/chemrxiv.15008151/v1>.
- J. Kim. "Workflow design as a research variable in computational materials discovery". *ChemRxiv, 2026 (연구실 기재)*. DOI: <https://doi.org/10.26434/chemrxiv.15008076/v1>.
- K. Nam#, S. Han#, J. Kim\*. "Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents". *arXiv, 2026 (연구실 기재)*. [연구실 게시 링크](https://arxiv.org/abs/2606.29459).
- S. Han, Y. Kang, T. Bae, J. Kim, Y. Kim, V. Bernales, A. Guzik\*, J. Kim\*. "EGMOF: Efficient Generation of Metal-Organic Frameworks Using a Hybrid Diffusion-Transformer Architecture". *Nature Communications (게재 승인), 2026*. [연구실 게시 링크](https://doi.org/10.48550/arXiv.2511.03122).
- S. Jang, Y. Kim, I. Jeong, M. Kim, J. Lee, J. Kim, K. Roh, K. Lee, S. Kim\*, Y. Lee\*, C. Ahn\*, H. Jung\*. "Chloride Ions: Essential Agents for Achieving Spontaneous Delamination of MXene". *Advanced Materials, 2026*. DOI: <https://doi.org/10.1002/adma.74422>.
- H. Kim, D. Kim, J. Kim\*. "LitMOF: An LLM Multi–Agent for Literature–Validated Metal–Organic Frameworks Database Correction and Expansion". *Nature Communications (게재 승인), 2026*. [연구실 게시 링크](https://doi.org/10.48550/arXiv.2512.01693).
- S. Han#, J. Lee#, J. Kim\*. "Multimodal Transformer for Sample-Aware Prediction of Metal-Organic Framework Properties". *ACS Central Science, 2026*. DOI: <https://doi.org/10.1021/acscentsci.6c01049>.
- Y. Jo#, M. Jeon#, D. Kim, J. Kim\*, M. Dincă\*. "Methanol-Ethanol Discrimination and Selective Sensing Enabled by Molecular Sieving in Conductive MOFs". *Advanced Materials, 2026*. DOI: <https://doi.org/10.1002/adma.73406>.
- Y. Kim#, D. Kim#, S. Kim, Y. Lim, J. Kim\*. "Framework-templated gas lattices in metal-organic frameworks". *Nature Communications, 2026*. DOI: <https://doi.org/10.1038/s41467-026-74776-5>.
- Y. Chiang, T. Kreiman, C. Zhang, M. Kuner, E. Weaver, I. Amin, H. Park, Y. Lim, J. Kim, D. Chrzan, A. Walsh, S. Blau, M. Asta, A. Krishnapriyan\*. "MLIP Arena: Advancing Fairness and Transparency in Machine Learning Interatomic Potentials via an Open, Accessible Benchmark Platform". *Advances in Neural Information Processing Systems, 2026*. DOI: <https://doi.org/10.52202/085713-4410>.
- W. Lee, Y. Choi, S.S. Jeon, H. Jeon, J. Nam, E. Lee, H. Kum, J. Kim, Y. J. Hwang, H. Lee\*. "Distinct durability of NiMo, PtNi/C, and Pt/C under various intermittent conditions in anion exchange membrane water electrolyzers". *Applied Catalysis B: Environment and Energy, vol.394, 126803, 2026*. DOI: <https://doi.org/10.1016/j.apcatb.2026.126803>.
- S. Han, T. Bae, J. Kim, Y. Kim, J. Kim\*. "Large Language Models for Porous Materials: From Text Mining to Autonomous Laboratory". *Digital Discovery, 2026*. DOI: <https://doi.org/10.1039/d5dd00578g>.
- L. Lim#, C. Lee#, J. Lee#, M. Lee, Y. Kim, T. K. Lee, G. Lee, J. Kim, S. Y. Oh, J. Kim, J. Park\*. "Bioelectronic synthesis of hydrogen sulfide enables spatiotemporal regulation of protein modification and cellular redox". *Science Advances, 2026*. DOI: <https://doi.org/10.1126/sciadv.aeb3401>.
- J. Lee#, J. Woo#, Y. Kim, S. Kim, C. Paulina, H. Park, H. T. Kim\*, S. Park\*, J. Kim\*. "LLMB: AI Agent for Lithium Metal Battery Research Using Large Language Model". *ACS Central Science, 2026*. DOI: <https://doi.org/10.1021/acscentsci.5c02433>.
- D. Lee, S. Lee, M. Park, J. Kim, H. Jin, S. Kim, D. Lee, Y. Lim, J. Yang, T. Lee, B. Oh, S. Sun, D. Kim, S. Wang, S. Im, H. Kim, S. Park, J. Kim, Y. Choi\*, S. Park\*. "Universal cryogenic transfer of liquid metal particles in polymers for wafer-scale stretchable integrated electronics". *Nature Communications, 2026*. DOI: <https://doi.org/10.1038/s41467-026-70101-2>.
- C. Paulina, D. Son, H. Jang, H. Park, J. Woo, S. Y. Kim, D. Kim, J. Kim\*, J. Lee\*, S. Park\*. "Addressing Low E/S and N/P Ratio Challenges in Li–S Batteries with a Multifunctional Interlayer". *Small, e08573, 2026*. DOI: <https://doi.org/10.1002/smll.202508573>.

**2025**

- H. Park, J.W. Baek, H. Jang, C. Park, M. Sagong, Y. Cho, H. Shin, J. Kim, I.D. Kim\*. "Defect-Mediated In Situ CNT Growth in Hollow Porous Carbon From ZIF-8/ZIF-67 Bilayers for Efficient and Stable ORR Catalysis". *Small, e09739, 2025*. DOI: <https://doi.org/10.1002/smll.202509739>.
- K. Lee, Y.M. Jo\*, M.S. Sohn, M. Jeon, C. Kim, O. Gul, S.J. Park, K.B. Kim, K.S. Chang, C.B. Jeong, J. Kim, Y.C. Kang\*, I. Park\*. "Photoactivated conductive MOF thin film arrays on micro-LEDs for chemiresistive gas sensing". *Nature Communications, 16, 9612, 2025*. DOI: <https://doi.org/10.1038/s41467-025-64602-9>.
- H. Kum, J. Kim\*. "High-Throughput Screening of Ru-Based MOF-Supported Single-Atom Catalysts for Hydrogen Evolution Reaction Via Machine Learning Interatomic Potential". *ACS Catalysis, 2025*. DOI: <https://doi.org/10.1021/acscatal.5c06272>.
- K. Lee, M. Kim, Y. Kwon, S. Park, Y. Lim, D. Kwak, J. Jeong, B. Kim, J. Ahn, J. Kim, Y.H. Cho, I.D. Kim\*, I. Park\*. "Enabling Weather-Independent Gas Detection through Deep Learning on Light-Activated Sensors". *ACS Nano, 2025*. DOI: <https://doi.org/10.1021/acsnano.5c10308>.
- Y. Lim, W. Jeong, H. Jung, H.L. Choi, T.H. Bae, J.H. Lee\*, J. Kim\*. "Tuning Pore Chemistry of Metal–Organic Frameworks Using Anionic Pillars for Humid-Tolerant CO2 Capture". *Chemistry of Materials, 2025*. DOI: <https://doi.org/10.1021/acs.chemmater.5c01848>.
- S. Kang, J. Kim\*. "Property-guided inverse design of metal-organic frameworks using quantum natural language processing". *Npj Computational Materials, 11, 321, 2025*. DOI: <https://doi.org/10.1038/s41524-025-01806-z>.
- S. Lee, J. Park, S. Han, E. Yu, J. Kim, C. S. H. Hwang\*, D.S. Lee\*, K.H. Jeong\*. "Superhydrophilic Silica-Coated Au Nanoislands for Efficient Capture and Enhanced SERS Detection of Airborne Biomarkers". *ACS Applied Materials & Interfaces, 2025*. DOI: <https://doi.org/10.1021/acsami.5c16035>.
- D. Jeon, H. Shin, J.H. Cha, H. Kim, S. Park, J. Ahn, S.H. Cho, C. Park, D.H. Kim, E. Shin, H. Baik,  J. Kim, S.Y. Choi,\* I.D. Kim\*. "Photothermal Annealing-Enabled Millisecond Synthesis of Carbon Nanoonions and Simultaneous Single-Atom Functionalization". *ACS Nano, 19, 34235-34247, 2025*. DOI: <https://doi.org/10.1021/acsnano.5c11229>.
- J. Kim, J. Kim\*. "Design Strategy for Metal−Organic Frameworks-Based Mixed Matrix Membranes Incorporating Polymer Infiltration". *The Journal of Physical Chemistry C, vol. 129, 40, 18303-18310, 2025*. DOI: <https://doi.org/10.1021/acs.jpcc.5c04714>.
- Y. Jeong, Y. Kim, W. Jeong, H.L. Choi, J. Kim, T.H. Bae\*. "Nitrogen-enriched porous organic polymers for high-performance CO2/N2 separation in mixed-matrix membranes". *Journal of Membrane Science, vol. 738, Part A, 124749, 2025*. DOI: <https://doi.org/10.1016/j.memsci.2025.124749>.
- S. Kim#, J. Lee#, S. Choi, S. Woo, S. Hong, H. Kim, J. Kim\*, and D. Lee\*. "Regulating Solvation Dynamics and Lithium Plating viaTi 3 C2 Tx -Engineered PVDF-HFP Separators". *Advanced Energy Materials, e03091, 2025*. DOI: <https://doi.org/10.1002/aenm.202503091>.
- H. Jang, J. Kim\*. "Computational screening and analysis of compatibility in mixed matrix membranes for enhanced gas separation". *Separation and Purification Technology, vol. 379, Part 1, 134852, 2025*. DOI: <https://doi.org/10.1016/j.seppur.2025.134852>.
- J. Lee#, M. Kim#, S. Park, J. Lee, Q. Chen, J. Kim, T. Defferriere, H. Park, S. Jeon\*, and I.D. Kim\*. "Bandgap-Engineered Graphene Quantum Dot Photosensitizers for Tunable Light SpectrumActivated NO2 Sensors". *ACS Nano, vol. 19, 36, 32732-32743, 2025*. DOI: <https://doi.org/10.1021/acsnano.5c10578>.
- J. Bae, B.L. Suh, H. Shin, J. Kim, I.D. Kim. "Discovery of a liquid crystal phase of sodium halides via a nonclassical nucleation pathway". *Advanced Powder Materials, vol. 4, 6, 100336, 2025*. DOI: <https://doi.org/10.1016/j.apmate.2025.100336>.
- S. Kang#, Y. Kim#, J. Kim\*. "Quantum Computing Based Design of Multivariate Porous Materials". *ACS Central Science, 2025*. DOI: <https://doi.org/10.1021/acscentsci.5c00918>.
- Y. Kim, W. Lee, J. Kim\*. "Amorphous Metal–Organic Framework Database for Amorphization Prediction and CO2 Direct Air Capture Screening". *ACS Applied Materials & Interfaces, vol. 17, 35, 49647-49659, 2025*. DOI: <https://doi.org/10.1021/acsami.5c14534>.
- J. Kim#, J. Lee, C. Cho, J. Nam, B. Ji, H. Cho, H. T. Shin, D. Sivanesan, Sarah S. Park, J. Kim, W. Choe\*. "Isoreticular moiré metal-organic frameworks with quasiperiodicity". *Nature Communications, 16, 7384, 2025*. DOI: <https://doi.org/10.1038/s41467-025-62247-2>.
- S. Maeng#, J. Kim#, T. Kim#, S. Lee, S. Han, S. J. Park, C. Kim, J. Kim, J. Y. Lee\*, H.Cho\*. "Dual-Strategy Direct Photocatalytic Patterning for Efficient Perovskite Nanocrystal LED Displays". *Advanced Materials, e08217, 2025*. DOI: <https://doi.org/10.1002/adma.202508217>.
- G. S. Kim#, H. Kum#, J. W. An#, H. Kwon, Y. J. Ryu, H. W. Jang, K. Lee\*, J. Kim\*, J. S. Jang\*. "Ultrafast Photothermal-Shock-Driven Multimetallic Exsolution for Artiﬁcial Olfaction of Sulfur Compounds Detection". *Small Structures, vol. 6, 10, 2500292, 2025*. DOI: <https://doi.org/10.1002/sstr.202500292>.
- M. Lee#, J. Lee#, Y. Kim, C. Lee, S. Y. Oh, J. Kim, J.Park\*. "Bioelectrosynthesis of Signaling Molecules for Selective Modulation of Cell Signaling". *Angewandte Chemie International Edition, vol. 64, e202508192, 2025*. DOI: <https://doi.org/10.1002/anie.202508192>.
- Y. Lim#, H. Park#, A. Walsh\*, J. Kim\*. "Accelerating CO₂ Direct Air Capture Screening for Metal-Organic Frameworks with a Transferable Machine Learning Force Field". *Matter, 8, 102203, 2025*. DOI: <https://doi.org/10.1016/j.matt.2025.102203>.
- T. H. Kim#, J. H. Moon#, J. Shin, S. A. Mohamed, J. Kim, H. Kang, Y. J. Lee, H. Kang, E. A. Cho\*. "Prevention of Surface and Bulk Degradation of Co-free Ni-rich Layered Cathodes by Primary-Particle-Level Li2SO4 Coating". *Journal of Power Sources, 649, 237390, 2025*. DOI: <https://doi.org/10.1016/j.jpowsour.2025.237390>.
- D. Kim, Y. Lim, J. Kim\*. "Refining a Generic Force Field for Predicting Phase Transitions in Wine-Rack Metal−Organic Frameworks". *Journal of Chemical Theory and Computation, vol. 21, 5599-5607, 2025*. DOI: <https://doi.org/10.1021/acs.jctc.5c00641>.
- D. W. Kim#, H. Mun#, Y. Kang, W. G. Kim, D. Ahn, S. Y. Yun, J. A. Han,  D. H. Lee, T. Lee, K. Jeong, J. Kim, S. G. Im\*, Y. K. Choi\*. "Synthesis of Stretchable Triboelectric Material with Strain-Compensating Ability Using Gradient Interpenetrating Polymer Networks". *Energy & Environmental Science, vol. 18, 4080-4096, 2025*. DOI: <https://doi.org/10.1039/d4ee03110e>.
- J. Guo#, J. W. Baek#, Y. Kang#, D. Kim#, C. Park, J. Woo, T. Zou, E. Shin, Q. Wang, Y. Noh, S. Park,  J. Kim\*, Yun. Li\*, I. D. Kim\*, K. Kang\*. "Molecular Sensitizer-Loaded Monolayer Organic Semiconductors for High-Performance H2S Sensors". *ACS Nano, vol. 19, 16175-16187, 2025*. DOI: <https://doi.org/10.1021/acsnano.5c04783>.
- C. Park#, J. Woo#, M. Jeon#, J. W. Baek, E. Shin, J. Kim\*, S. Park\*, I. D. Kim\*. "Dual-MOF-Layered Films via Solution Shearing Approach: A Versatile Platform for Tunable Chemiresistive Sensors". *ACS Nano, vol. 19, 11, 11230–11240, 2025*. DOI: <https://doi.org/10.1021/acsnano.4c18848>.
- J. Park#, K. H. Oh#, S. Kang, J. Ha, S. Lee, J. Kim, Y.S. Bae\*, H. R. Moon\*. "Rational Pore Design in Multivariate Metal-Organic Frameworks for C2H6/C2H4 Separation". *Small, vol. 21, 11, 2025*. DOI: <https://doi.org/10.1002/smll.202500937>.
- Y. Kang#, W. Lee#, T. Bae#, S. Han, H. Jang, J. Kim\*. "Harnessing Large Language Model to Collect and Analyze Metal-Organic Framework Property Data Set". *JACS, vol. 147, 5, 3943-3958, 2025*. DOI: <https://doi.org/10.1021/jacs.4c11085>.
- J. Park#, Y. Lee#, J. Kim\*. "Multi-modal conditional diffusion model using signed distance functions for metal-organic frameworks generation". *Nature Communications, vol. 16, 34, 2025*. DOI: <https://doi.org/10.1038/s41467-024-55390-9>.

**2024**

- S. Han#, B. G. Lee, D. W. Lim, J. Kim\*. "Machine Learning-Based Prediction of Proton Conductivity in Metal-Organic Frameworks". *Chemistry of Materials, vol. 36, 22, 2024*. DOI: <https://doi.org/10.1021/acs.chemmater.4c02368>.
- M. Jeon#, J. S. Lee#, M. Kim#, J. W. Seo, H. Kim, H. R. Moon\*, S. J. Choi\*, J. Kim\*. "Triphenylene-Based 2D cMOFs: Unraveling the H2S Sensing Mechanism and Applications for a Real-Time Wireless Chemiresistive Sensor". *ACS Applied Materials & Interfaces, vol. 16, 45, 62382-62391, 2024*. DOI: <https://doi.org/10.1021/acsami.4c13269>.
- J. Park, W. Lee, J. Kim\*. "Large-Scale Construction and Analysis of Amorphous Porous Polymer Network Materials". *ACS Applied Materials & Interfaces, vol. 16, 42, 57190-57199, 2024*. DOI: <https://doi.org/10.1021/acsami.4c13221>.
- J. Park, H. Kim, Y. Kang, Y. Lim, J. Kim\*. "From Data to Discovery: Recent Trends of Machine Learning in Metal-Organic Frameworks". *JACS Au, vol. 4, 10, 3727-3743, 2024*. DOI: <https://doi.org/10.1021/jacsau.4c00618>.
- J. Kim#, D. Nam#, H. J. Cho#, E. Cho, D. Sivanesan, C. Cho, J. Lee, J. Kim, W. Choe\*. "Up-down approach for expanding the chemical space of metal-organic frameworks". *Nature Synthesis, vol. 3, 1518-1528, 2024*. DOI: <https://doi.org/10.1038/s44160-024-00638-x>.
- C. Park#, H. Shin#, M. Jeon#, S. H. Cho, J. Kim\*, I. D. Kim\*. "Single-Atom Catalysts in Conductive Metal-Organic Frameworks: Enabling Reversible Gas Sensing at Room Temperature". *ACS Nano, vol. 18, 38, 26066-26075, 2024*. DOI: <https://doi.org/10.1021/acsnano.4c05815>.
- J. W. Baek, S. Han, S. E. Lee, J. Ahn, C. Park, J. S. Nam, Y. H. Kim, E. Shin, M. Kim, J. S. Jang, J. Kim, H. J. Park\*, I. D. Kim\*. "Cobalt-Doped Ceria Sensitizer Effects on Metal Oxide Nanofibers: Heightened Surface Reactivity for High-Performing Chemiresistive Sensors". *ACS Nano, vol. 18, 30, 19568-19580, 2024*. DOI: <https://doi.org/10.1021/acsnano.4c03168>.
- J. Wang#, T. Chen#, M. Jeon, J. J. Oppenheim, B. Tan, J. Kim, M. Dincă\*. "Superior Charge Transport in Ni-Diamine Conductive MOFs". *JACS, vol. 146, 29, 20500-20507, 2024*. DOI: <https://doi.org/10.1021/jacs.4c06935>.
- C. Song#, S. Kim#, S. Park#, S.Y. Park, J. Lee, M. H. Woo, A. A. Yu, J. Kim, N. S. Choi\*. "Safer lithium-ion batteries realized by electrolyte with thermoresponsive poly(vinylidene fluoride-co-trifluoroethylene)". *Chemical Engineering Journal, vol. 494, 152995, 2024*. DOI: <https://doi.org/10.1016/j.cej.2024.152995>.
- Y. Sung#, W. Lee#, H. Lee, J. W. Lee, B. Kim, S. Yoo, S. Jeong\* J. Kim\*, J. Y. Lee\*. "Nanostructured Molecular Packing of Polymer Films Formed on Water Surfaces". *Nano Letters, vol. 24, 24, 7474-7482, 2024*. DOI: <https://doi.org/10.1021/acs.nanolett.4c01675>.
- Y. Kang, J. Kim\*. "ChatMOF: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models". *Nature Communications, vol. 15, 4705, 2024*. DOI: <https://doi.org/10.1038/s41467-024-48998-4>.
- S. Park#, S. Woo#, J. Kim#, J. Lee, H. Lee, K. M. Kim, J. Ahn, H. T. Kim, Y. J. Kim, J. Kim, I. D. Kim\*, S. J. Kim\*. "A Joule-Heating-Derived multiphase porous TiO2 support for reinforcing High-Entropy alloy catalysts". *Chemical Engineering Journal, vol. 493, 152551, 2024*. DOI: <https://doi.org/10.1016/j.cej.2024.152551>.
- Y. Lim#, B. Kim#, J. Kim\*. "Data-Driven Design of Flexible Metal-Organic Frameworks for Gas Storage". *Chemistry of Materials, vol. 36, 11, 5465-5473, 2024*. DOI: <https://doi.org/10.1021/acs.chemmater.4c00398>.
- S. Y. Lee#, E. Cho#, B. L. Suh#, J. W. Choi, S. Lee, J. Kim, C. Lee\*, K. W. Jung\*. "Unveiling interfacial interaction between antimony oxyanions and boehmite nanorods: Spectroscopic evidence and density functional theory analysis". *Journal of Hazardous Materials, vol. 469, 133902, 2024*. DOI: <https://doi.org/10.1016/j.jhazmat.2024.133902>.
- W. Lee, S. Lee, J. Kim\*. "In Silico Generation of Chromium-Based MOFs with Abundant Active Sites for N2/CH4 Separation". *The Journal of Physical Chemistry C, vol.128, 18, 7690-7697, 2024*. DOI: <https://doi.org/10.1021/acs.jpcc.4c00401>.
- S. Han, Y. Kang, H. Park, J. Yi, G. Park, J. Kim\*. "Multimodal Transformer for Property Prediction in Polymers". *ACS Applied Materials & Interfaces, vol.16, 13, 16853-16860, 2024*. DOI: <https://doi.org/10.1021/acsami.4c01207>.
- S. Park#, M. Kim#, Y. Lim, D. H. Oh, J. Ahn, C. Park, S. Woo, W. C. Jung, J. Kim, I. D. Kim\*. "Dual-Photosensitizer Synergy Empowers Ambient Light Photoactivation of Indium Oxide for High-Performance NO2 Sensing". *Advanced Materials, vol. 36, 24, 2313731, 2024*. DOI: <https://doi.org/10.1002/adma.202313731>.
- Y. Ko, J. Park, X. Zhang, L. Kang, T. H. M. Pham, V. Boureau, C. Pham-Huu, J. Kim, L. Zhong\*, A. Züttel. "All Platinum Group Metal-Free and Curable Catalysts for Direct Borohydride Fuel Cells". *ACS Applied Energy Materials, vol. 7, 2, 639-648, 2024*. DOI: <https://doi.org/10.1021/acsaem.3c02578>.
- Y. Lee#, S. Chong#, C. Lee, J. Kim, S. Q. Choi\*. "Structural Determinants of Chirally Selective Transport of Amino Acids through the α-Hemolysin Protein Nanopores of Free-Standing Planar Lipid Membranes". *Nano Letters, vol. 24, 2, 681-687, 2024*. DOI: <https://doi.org/10.1021/acs.nanolett.3c03976>.
- T. Hyun#, J. Park#, J. So, J. Kim\*, D. Y. Koh\*. "Unexpected Molecular Sieving of Xylene Isomer Using Tethered Ligand in Polymer-Metal-Organic Frameworks (polyMOFs)". *Advanced Science, vol. 11, 34, 2402980, 2024*. DOI: <https://doi.org/10.1002/advs.202402980>.
- H. Jang, D. Ryu, W. Lee, G. Park, J. Kim\*. "Machine learning-based epoxy resin property prediction". *Molecular Systems Design & Engineering, 9, 959-968, 2024*. DOI: <https://doi.org/10.1039/d4me00060a>.
- J. Park#, H. Kim#, S. Kim, S. Y. Yi, H. Min, D. Choi, S. Lee,  J. Kim\*, J. Lee\*. "Boosting Alkaline Hydrogen Oxidation Activity of Ru Single-Atom Through Promoting Hydroxyl Adsorption on Ru/WC1-x Interfaces". *Advanced Materials, vol. 36, 4, 2308899, 2024*. DOI: <https://doi.org/10.1002/adma.202308899>.
- H. K. Lee#, Y. Oruganti#, J. Lee#, S. Han, J. Kim, D. Moon\*, M. Kim\*, D. W. Lim\*, H. R. Moon\*. "Moisture-triggered proton conductivity switching in metal-organic frameworks: role of coordinating solvents". *Journal of Materials Chemistry A, vol. 12, 2, 795-801, 2024*. DOI: <https://doi.org/10.1039/d3ta06197c>.
- J. Park, A. P. S. Gill, S. M. Moosavi, J. Kim\*. "Inverse design of porous materials: a diffusion model approach". *Journal of Materials Chemistry A, vol. 12, 11, 6507-6514, 2024*. DOI: <https://doi.org/10.1039/d3ta06274k>.
- H. Park#, S. Majumdar#, X. Zhang, J. Kim\*, B. Smit\*. "Inverse design of metal-organic frameworks for direct air capture of CO2 via deep reinforcement learning". *Digital Discovery, vol. 3, 4, 728-741, 2024*. [연구실 게시 링크](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d4dd00010b).

**2023**

- J. Lee#, W. Lee#, J. Kim\*. "MatGD: Materials Graph Digitizer". *ACS Applied Materials & Interfaces, vol. 16, 1, 723-730, 2023*. DOI: <https://doi.org/10.1021/acsami.3c14781>.
- H. Park#, Y. Kang#, J. Kim\*. "Enhancing Structure–Property Relationships in Porous Materials through Transfer Learning and Cross-Material Few-Shot Learning". *ACS Applied Materials & Interfaces, vol. 15, 56375, 2023*. DOI: <https://doi.org/10.1021/acsami.3c10323>.
- K. Kim, J. Kim\*. "Development of a Transferable Force Field between Metal–Organic Framework and Its Polymorph". *ACS Omega, vol. 8, 44328, 2023*. DOI: <https://doi.org/10.1021/acsomega.3c06937>.
- J. Kim#, T. H. Ha#, J. Kim#, G. H. Jeong, S. O. Kim, W. Chung, K. Roh, J. H. Lee, J. Oh. "Design principles for selective and economical CO2 electrolysis in acids". *Applied Catalysis B: Environmental, vol. 339, 123160, 2023*. [연구실 게시 링크](https://www.sciencedirect.com/science/article/pii/S0926337323008032?via%3Dihub).
- J. Shin, G. Lee, M. Choi, H. Jang, Y. Lim, G. S. Kim, S. H. Nam, S. H.  Baek, H. C. Song, J. Kim, C. Y. Kang, J. O. Lee, S. Jeon, D. Cho, J. S. Jang\*. "Atomically mixed catalysts on a 3D thin-shell TiO2 for dual-modal chemical detection and neutralization". *Journal of Materials Chemistry A, vol. 11, 18195, 2023*. DOI: <https://doi.org/10.1039/d3ta02160b>.
- D.H. Kim, J.H. Cha, S. Chong, S.H. Cho, H. Shin, J. Ahn, D. Jeon, J. Kim, S.Y. Choi\*, I.D. Kim\*. "Flash-Thermal Shock Synthesis of Single Atoms in Ambient Air". *ACS Nano, 2023*. DOI: <https://doi.org/10.1021/acsnano.3c02968>.
- S. Kim, H. Shin, J. Lee, C. Park, Y. Ahn, H.J. Cho, S. Yuk, J.Kim\*, D. Lee\*, I.D. Kim\*. "Three-Dimensional MoS2/MXene Heterostructure Aerogel for Chemical Gas Sensors with Superior Sensitivity and Stability". *ACS Nano, vol. 17, 19387, 2023*. DOI: <https://doi.org/10.1021/acsnano.3c07074>.
- S. Han, J. Lee, S. Han, S. M. Moosavi, J. Kim, C. Park\*. "Design of New Inorganic Crystals with the Desired Composition Using Deep Learning". *Journal of Chemical Information and Modeling, vol. 63, 5755, 2023*. DOI: <https://doi.org/10.1021/acs.jcim.3c00935>.
- M. Jeon, O. Kwon, J. Kim\*. "Computational Discovery for Crafting Multi-Dimensional and Multi-Functional Metal–Organic Framework Composites". *The Journal of Physical Chemistry C, vol. 127, 18089, 2023*. DOI: <https://doi.org/10.1021/acs.jpcc.3c03814>.
- S. Kang, M. Jeon, J. Kim\*. "Density Functional Theory Study of Synergistic Gas Sensing Using an Electrically Conductive Mixed Ligand Two-Dimensional Metal–Organic Framework". *ACS Sensors, vol. 8, 3448, 2023*. DOI: <https://doi.org/10.1021/acssensors.3c00965>.
- M. Jeon, M. Kim, J. Lee, H. Kim, S. Choi, H. Moon, J. Kim\*. "Computational Prediction of Stacking Mode in Conductive Two-Dimensional Metal–Organic Frameworks: An Exploration of Chemical and Electrical Property Changes". *ACS Sensors, vol. 8, 3068, 2023*. DOI: <https://doi.org/10.1021/acssensors.3c00715>.
- J. Lee, W. Lee, S. chong, J. Kim\*. "In Silico Design of Metal–Organic Frameworks Using Cooperative Binding of Two Metal Catecholates". *The Journal of Physical Chemistry C, vol. 127, 14389, 2023*. DOI: <https://doi.org/10.1021/acs.jpcc.3c02012>.
- J. Ahn, S. Park, D.H. Oh, Y. Lim, J. S. Nam, J. Kim, W.C. Jung, I.D. Kim\*. "Rapid Joule Heating Synthesis of Oxide-Socketed High-Entropy Alloy Nanoparticles as CO2 Conversion Catalysts". *ACS Nano, vol. 17, 12188, 2023*. DOI: <https://doi.org/10.1021/acsnano.3c00443>.
- D. Ryu, J. Kim\*. "Database Design for Double-Linker Metal–Organic Frameworks". *The Journal of Physical Chemistry C, vol. 127, 10384, 2023*. DOI: <https://doi.org/10.1021/acs.jpcc.3c02142>.
- G.S. Kim#, Y. Lim#, J. Shin, J. Yim, S. Hur, H.C. Song, S.H. Baek, S.K. Kim, J. Kim\*,  C.Y. Kang\*, J.S. Jang\*. "Breathable MOFs Layer on Atomically Grown 2D SnS2 for Stable and Selective Surface Activation". *Advanced Science, vol. 10, 2301002, 2023*. DOI: <https://doi.org/10.1002/advs.202301002>.
- J. Lee#, H. Lim#, J. Park#, M.S. Kim, J.W. Jung\*, J. Kim\*, I.D. Kim\*. "Fluorine-Rich Covalent Organic Framework to Boost Electrochemical Kinetics and Storages of K+ Ions for Potassium-Ion Battery". *Advanced Energy Materials, vol. 23, 2300442, 2023*. DOI: <https://doi.org/10.1002/aenm.202300442>.
- N.H. Kwon, S. Han, J. Kim, E.S. Cho\*. "Super Proton Conductivity Through Control of Hydrogen-Bonding Networks in Flexible Metal–Organic Frameworks". *Small, vol.19, 2301122, 2023*. DOI: <https://doi.org/10.1002/smll.202301122>.
- S. Han, Y. Lee, J. Kim, S.Y. Cho\*. "Physicochemical Profiling of Macrophage Heterogeneity Using Deep Learning Integrated Nanosensor Cytometry". *ACS Sensors, vol. 8, 1676, 2023*. DOI: <https://doi.org/10.1021/acssensors.2c02813>.
- J. Ha#, M. Jeon#, J. Park, J. Kim\*, H.R. Moon\*. "Effect of Steric Hindrance on the Interfacial Connection of MOF-on-MOF Architecture". *Nanoscale Advances, vol. 5, 2111, 2023*. [연구실 게시 링크](https://pubs.rsc.org/en/content/articlehtml/2023/na/d2na00790h).
- Y.T. Nam, H. Kang, S. Chong, Y.J. Kim, W. Lee, Y. Lee, J. Kim, S.Y. Cho\*, H.T. Jung\*. "Rapid and Reversible Sensing Performance of Hydrogen-Substituted Graphdiyne". *ACS Sensors, vol. 8, 1151, 2023*. DOI: <https://doi.org/10.1021/acssensors.2c02449>.
- J.S. Jang\*, Y. Lim, H. Shin, J. Kim, T.G. Yun\*. "Bidirectional Water-Stream Behavior on a Multifunctional Membrane for Simultaneous Energy Generation and Water Purification". *Advanced Materials, vol. 35, 2209076, 2023*. DOI: <https://doi.org/10.1002/adma.202209076>.
- S. Han, J. Kim\*. "Design and Screening of Metal–Organic Frameworks for Ethane/Ethylene Separation". *ACS Omega, vol. 8, 4278, 2023*. DOI: <https://doi.org/10.1021/acsomega.2c07517>.
- S. Park, S.H. Jeon, H. Kim, J. Philips, D.H. Oh, J. Ahn, M. Kim, C. Park, S. Hong, J. Kim, W.C. Jung, I.D. Kim\*. "Imparting Metal Oxides with High Sensitivity Toward Light-Activated NO2 Detection Via Tailored Interfacial Chemistry". *Advanced Functional Materials, vol. 33, 2214008, 2023*. DOI: <https://doi.org/10.1002/adfm.202214008>.
- Y. Kang#, H. Park#, B. Smit, J. Kim\*. "A Multi-modal Pre-training Transformer for Universal Transfer Learning in Metal-Organic Frameworks". *Nature Machine Intelligence, vol. 5, 309, 2023*. DOI: <https://doi.org/10.1038/s42256-023-00628-2>.
- J. Park, Y. Lim, S. Lee, J. Kim\*. "Computational Design of Metal–Organic Frameworks with Unprecedented High Hydrogen Working Capacity and High Synthesizability". *Chemistry of Materials, vol. 35, 9, 2023*. DOI: <https://doi.org/10.1021/acs.chemmater.2c01822>.

**2022**

- S. Cho#, C. Park#, M. Jeon#, J.H. Lee, O. Kwon, S. Seong, J. Kim\*, I.D. Kim\*, H.R. Moon\*. "Interface-Sensitized Chemiresistor: Integrated Conductive and Porous Metal-Organic Frameworks". *Chemical Engineering Journal, vol. 449, 137780, 2022*. DOI: <https://doi.org/10.1016/j.cej.2022.137780>.
- S.R. Cho#, D.H. Kim#, M. Jeon#, R. Pragya#, M. Gyeon, Y. Kim, M. Jo, S. Song, J. Park\*, J. Kim\*, I.D. Kim\*, K. Kang\*. "Overlaying Monolayer Metal-Organic Framework on PtSe2‐Based Gas Sensor for Tuning Selectivity". *Advanced Functional Materials, vol. 32, 2207265, 2022*. DOI: <https://doi.org/10.1002/adfm.202207265>.
- H. Kim, J. Kim\*. "Theoretical study of induced selective N2 binding under an electric field in MOF-74: application for N2/CH4 separations". *RSC Advances, vol. 12, 23396, 2022*. DOI: <https://doi.org/10.1039/d2ra04216a>.
- K. Choi, W. Jang, W. Lee, J.S. Choi, M. Kang, J. Kim, K. Char, J. Lim\*, S.G. Im\*. "Systematic Control of Sulfur Chain Length of High Refractive Index, Transparent Sulfur-Containing Polymers with Enhanced Thermal Stability". *Macromolecules, vol. 16, 7222, 2022*. DOI: <https://doi.org/10.1021/acs.macromol.2c00537>.
- R. A. Dodson, J. Park, J. Kim, M. J. Cliffe, S. M. Cohen\*. "Tethering Effects in Oligomer-Based Metal-Organic Frameworks". *Inorganic Chemistry, vol. 31, 12284, 2022*. DOI: <https://doi.org/10.1021/acs.inorgchem.2c01567>.
- J. Choi, B. Chacon, H. Park, K. Hantanasirisakul, T. Kim, K. Shevchuk, J. Lee, H. Kang, S.Y. Cho, J. Kim, Y. Gogotsi\*, S.J. Kim\*, H.T. Jung\*. "N-p-Conductor Transition of Gas Sensing Behaviors in Mo2CTXMXene". *ACS Sensors, vol. 8, 2225, 2022*. DOI: <https://doi.org/10.1021/acssensors.2c00658>.
- Y. Lim, J. Kim\*. "Application of transfer learning to predict diffusion properties in metal-organic frameworks". *Molecular Systems Design & Engineering, vol. 7, 1056, 2022*. DOI: <https://doi.org/10.1039/d2me00082b>.
- S. A. Mohamed, Y. Kim, J. Lee, W. Choe, J. Kim\*. "Understanding the Structural Collapse during Activation of Metal-Organic Frameworks with Copper Paddlewheels". *Inorganic Chemistry, vol. 25, 9702, 2022*. DOI: <https://doi.org/10.1021/acs.inorgchem.2c01171>.
- H. Park#, Y. Kang#, W. Choe, J. Kim\*. "Mining Insights on Metal-Organic Framework Synthesis from Scientific Literature Texts". *Journal of Chemical Information and Modeling, vol. 5, 1190, 2022*. DOI: <https://doi.org/10.1021/acs.jcim.1c01297>.
- D.H. Kim#, S. Chong#, C. Park, J. Ahn, J.S. Jang, J. Kim\*, I.D. Kim\*. "Oxide/ZIF-8 Hybrid Nanofiber Yarns: Heightened Surface Activity for Exceptional Chemiresistive Sensing". *Advanced Materials, 2105869, 2022*. DOI: <https://doi.org/10.1002/adma.202105869>.
- S. Chong, S. M. J. Rogge, J. Kim\*. "Tunable Electrical Conductivity of Flexible Metal-Organic Frameworks". *Chemistry of Materials, vol. 1, 254, 2022*. DOI: <https://doi.org/10.1021/acs.chemmater.1c03236>.

**2021**

- C.K. Chang, H.J. Yu, H. Jang, T.H. Hung, C.K. Chang, J. Kim\*, J.S. Lee\*, D.Y. Kang\*. "Conformational-change-induced selectivity enhancement of CAU-10-PDC membrane for H2/CH4 and CO2/CH4 separation". *Journal of Membrane Science Letters, vol. 1, 10005, 2021*. DOI: <https://doi.org/10.1016/j.memlet.2021.100005>.

## 수상과 선정

연구실 첫 화면의 2025년 수상 소식 3건이다. 날짜는 누리집에 적힌 연월이다.[^home]

- 2025-07 · 강신영이 제21회 KIAS Electronic Structure Calculation Workshop에서 Best Poster Award를 받았다.
- 2025-06 · 강신영이 2025 KSIEC Spring Meeting and International Conference에서 Excellent Paper Presentation Award를 받았다.
- 2025-01 · 이재웅과 우준희가 Samsung HumanTech Paper Award의 Energy & Environment 부문 Bronze Award를 받았다.

## 연락과 위치

- 교수 이메일: jihankim@kaist.ac.kr[^people][^home]
- 교수 연구실: LOTTE-KAIST R&D Center, W14, 402호. 전화 +82-42-350-7311.[^people][^faculty]
- 학생 연구실: LOTTE-KAIST R&D Center, W14, 601호. 연구실 대표 전화 +82-42-350-7351.[^people][^home]
- 주소: 대전광역시 유성구 대학로 291, KAIST.[^home]
[^home]: KAIST 분자 모사 연구실, 첫 화면의 Molecular Simulation Group·연구실 소개·Recent News·연락처. <https://molsim.kaist.ac.kr/> (관측 2026-11-05).
[^people]: KAIST 분자 모사 연구실, People의 교수 소개·Ph.D. program·Master program·Alumni. <https://molsim.kaist.ac.kr/people> (관측 2026-11-05).
[^research]: KAIST 분자 모사 연구실, Research의 양자 계산·자동 연구·역설계·복합재료·기체 분리와 저장 및 이산화탄소 전환 소개. <https://molsim.kaist.ac.kr/research> (관측 2026-11-05).
[^pubs]: KAIST 분자 모사 연구실, Publications의 연도별 논문 목록과 저자 기호 범례. <https://molsim.kaist.ac.kr/publications> (관측 2026-11-05).
[^faculty]: KAIST 생명화학공학과, Jihan Kim (김지한) 교수 소개. <https://cbe.kaist.ac.kr/boards/view/faculty/5/1/> (관측 2026-11-05).
[^p1]: S. Han, J. Lee, J. Kim, ACS Central Science (등록 출판일 2026-09-01). <https://doi.org/10.1021/acscentsci.6c01049> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p2]: S. Kang, Y.-H. Kim, J. Kim, ACS Central Science (등록 출판일 2025-08-22). <https://doi.org/10.1021/acscentsci.5c00918> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p3]: Y. Kang 외, J. Kim, Journal of the American Chemical Society (등록 출판일 2025-01-21). <https://doi.org/10.1021/jacs.4c11085> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p4]: Y. Kang, J. Kim, Nature Communications (등록 출판일 2024-06-03). <https://doi.org/10.1038/s41467-024-48998-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p5]: Y. Lim, B. Kim, J. Kim, Chemistry of Materials (등록 출판일 2024-05-22). <https://doi.org/10.1021/acs.chemmater.4c00398> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p6]: M. Jeon, O. Kwon, J. Kim, The Journal of Physical Chemistry C (등록 출판일 2023-09-01). <https://doi.org/10.1021/acs.jpcc.3c03814> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).
[^p7]: Y.-H. Kim, W. Lee, J. Kim, ACS Applied Materials & Interfaces (등록 출판일 2025-08-22). <https://doi.org/10.1021/acsami.5c14534> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5018605846,publication_year:2021-2026> (관측 2026-11-05).

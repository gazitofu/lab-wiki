# SNU Transformative ARchitecture Laboratory (STAR Laboratory)

**서울대학교 공과대학 기계공학부 · 양진규 교수**

- 영문 이름: Seoul National University Transformative ARchitecture Laboratory
- 분야: 경량·전개 구조물, 종이접기 구조 설계, 기계적 파동과 진동 제어[^prof][^research]
- 대분야: 기계·로봇·제조, 소재
- 태그: 전개형 구조물·종이접기 공학[^p1][^p4][^p5], 메타물질·메타광학[^p2][^p6], 구조 설계 소재(architected materials)[^p2][^p4][^p5]
- 홈페이지: <https://starlab.snu.ac.kr/>
- 근거와 출처: [STAR Laboratory 근거 페이지](snu-starlab-sources.md)

> 접힘과 연결 구조를 설계해 모양과 단단함을 바꾸고, 구조물 안에서 떨림과 충격이 전달되는 방식을 조절하는 연구실이다.

## 무엇을 연구하나

STAR Laboratory는 종이접기 원리를 이용한 구조물과 내부 배열을 설계한 소재를 연구한다. 접어 보관한 뒤 펼쳐 쓰는 전개 구조물을 항공우주 구조물과 로봇 같은 공학 대상에 연결하는 것이 한 축이다. 연구실은 역학과 물리학, 로봇공학, 자료 분석, 예술·디자인의 지식을 함께 써서 공학용 구조 시스템을 설계하고 개발한다고 소개한다.[^home][^research]

구조를 설계할 때는 접힘선과 판의 연결이 어떤 움직임을 허용하는지를 계산한다. 대표 논문 1은 단단한 판으로 된 여러 종류의 접이식 구조를 같은 방식으로 다루며, 판과 연결부의 기하 자료(모양·크기·배치에 관한 자료)에서 움직임의 제약을 자동으로 구성한다. 대표 논문 4는 서로 반대로 접히는 두 층을 결합해, 축 방향으로 굽힐 때 단면(물체를 잘랐을 때 나타나는 면) 안의 반대 움직임이 맞물리도록 했다. 이를 통해 굽힘 강성(굽히는 힘을 받을 때 변형에 저항하는 정도)을 높이고, 평평한 상태에서 하중(구조물에 가해지는 힘)을 지지하는 모양으로 바뀌는 팔 지지 장치·가구·쉼터를 만들었다.[^p1][^p4]

원하는 모양뿐 아니라 펼쳐지는 순서도 설계 대상으로 삼는다. 대표 논문 5는 물리 법칙을 학습 과정에 넣은 신경망(연결된 계산 요소의 연결 강도를 학습으로 조정해 입력과 출력의 관계를 표현하는 계산 모형)을 사용한다. 구조가 힘의 균형을 이루는 조건을 학습에 반영해 에너지(일을 할 수 있는 능력을 나타내는 물리량) 곡선을 예측하고, 목표한 안정 상태의 높이와 상태 사이의 장벽을 먼저 정해 설계를 찾는다. 여러 층으로 연결한 구조에서는 장벽의 크기를 조절해 층별 전개 순서를 만들었으며, 계산과 실제 시제품 실험으로 확인했다.[^p5]

또 다른 축은 메타물질(재료 자체의 성분뿐 아니라 인공적으로 설계한 구조 배열로 물리적 성질을 정하는 물질) 안의 파동(공간을 따라 변화나 교란이 전달되는 현상)과 진동(물체나 물리량이 기준 상태 주위에서 되풀이해 변하는 현상)이다. 대표 논문 2는 내부 막대가 진동하는 질량(물체의 운동 상태 변화에 저항하는 정도를 나타내는 물리량)을 관통하게 만들어 유효 질량과 강성(힘을 받을 때 변형에 저항하는 정도)을 따로 조절한다. 대표 논문 3은 격자에서 희박 고립파(압축 정도가 줄어든 교란이 모양을 유지하며 이동하는 파동)의 충돌을 실험하고 계산과 비교한다. 대표 논문 6은 종이접기 구조의 회전각과 연결을 조절해 파동을 한 가장자리 상태에서 다른 가장자리 상태로 옮기는 방법을 제시한다.[^p2][^p3][^p6]

## 주요 연구 주제

### 접었다 펼치는 구조와 자체 잠금

판과 연결부의 배치로 접힘 경로를 정하고, 펼친 뒤의 구조가 힘을 지지하도록 설계한다. 연구 소개에는 매끄러운 곡면을 이루는 전개 구조, 우주 거주 공간을 위한 접이식 구조, 모듈을 다시 연결하는 구조가 제시되어 있다. 대표 논문에서는 접이식 구조의 운동 계산 방법과 반대 방향으로 움직이는 두 겹 구조의 맞물림을 구체적으로 다뤘다.[^research][^p1][^p4]

### 목표한 전개 순서를 만드는 설계

접이식 구조의 역설계는 원하는 결과를 먼저 정하고 그 결과를 만드는 구조를 찾는 일이다. 대표 논문 5는 원뿔 형태의 접이식 구조에서 안정 상태와 그 사이를 넘는 데 필요한 에너지 장벽을 함께 지정했다. 연구실은 이처럼 내부 기하 구조를 설계해 변형과 힘에 대한 반응을 정하는 소재를 연구한다.[^p5][^p2]

### 파동의 전달·차단과 충돌

연구 소개는 구조 안의 에너지 전달, 진동 격리, 접힌 구조의 파동 전파를 주요 갈래로 제시한다. 대표 논문 2에서는 파동이 통과하지 못하는 주파수(단위 시간 동안 되풀이되는 변화의 횟수) 구간을 조절했고, 대표 논문 3에서는 변형이 커질수록 강성이 줄어드는 격자에서 희박 고립파의 충돌을 관찰했다. 충돌 결과는 진폭(반복되는 변화가 기준값에서 벗어나는 최대 크기)에 따른 위치 변화로 나타났고, 대표 논문 6에서는 접힘과 연결에 따른 파동의 이동을 다뤘다.[^research][^p2][^p3][^p6]

## 대표 논문

서울대 재직 시기에 발표한 논문 가운데 접이식 구조 설계·계산, 구조 배열을 이용한 소재 설계, 파동 제어를 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 주요 저자·PI 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [A Unified Framework for Kinematic Simulation of Rigid-Foldable Structures](https://doi.org/10.1093/jcde/qwag053) · Journal of Computational Design and Engineering | 1저자 Dongwook Kwak, 마지막 저자 Jinkyu Yang | 판과 연결부의 기하 자료에서 움직임을 제한하는 조건을 자동으로 구성해, 여러 종류의 접이식 구조가 접히고 펼쳐지는 운동을 계산하고 보여 주는 방법이다.[^p1] |
| 2 | 2026 | [Mechanical metamaterials with penetrating struts for tunable low-frequency bandgaps](https://doi.org/10.1038/s44455-026-00031-y) · npj Metamaterials | 1저자 Woosuk Kim, 공동 교신저자 Jinkyu Yang·Howon Lee | 내부 막대가 진동하는 질량을 관통하게 해 질량과 강성을 분리한다. 파동을 차단하는 구간을 조절하고, 서로 다른 구간을 가진 구조를 이어 여러 주파수 입력을 분리하는 필터를 보였다.[^p2] |
| 3 | 2026 | [Unveiling solitonic collisions in mechanical metamaterials](https://doi.org/10.1126/sciadv.aeb0489) · Science Advances | 1저자 Yasuhiro Miyazawa, 마지막 저자 Jinkyu Yang | 희박 고립파가 충돌하는 실험 장치를 만들었다. 대칭·비대칭 충돌에서 탄성적인 상호작용과 진폭에 따른 위치 변화를 관찰했고, 이동 속도와 위치 변화가 수치·해석 예측과 잘 맞았다.[^p3] |
| 4 | 2025 | [Double-Layer Self-Locking Origami Based on Opposite Folding Motion](https://doi.org/10.1177/21695172251401337) · Soft Robotics | 1저자 Jae-Kyeong Kim, 참여저자 Jinkyu Yang | 서로 반대로 접히는 두 층이 굽힘 중 맞물리도록 설계했다. 평평하게 둘 수 있으면서 필요할 때 힘을 지지하는 형태가 되는 팔 지지 장치·가구·쉼터를 만들었다.[^p4] |
| 5 | 2025 | [Physics-informed neural networks for programmable origami metamaterials with controlled deployment](https://doi.org/10.1039/D5MH01607J) · Materials Horizons | 1저자 Sukheon Kang, 참여저자 Jinkyu Yang | 미리 모은 학습 자료 없이 힘의 균형 조건으로 구조의 에너지 곡선을 예측한다. 목표한 안정 상태와 에너지 장벽을 정해 설계하고, 여러 층의 구조가 순서대로 펼쳐지게 했다.[^p5] |
| 6 | 2024 | [Topological pumping in origami metamaterials](https://doi.org/10.1103/PhysRevB.110.075123) · Physical Review B | 1저자 Shuaifeng Li, 교신저자 Jinkyu Yang | 공간에 따라 접힘의 회전각을 바꾸고 구조들을 연결해 파동을 서로 다른 가장자리 상태 사이로 옮겼다. 입력의 크기에 따라 상태 사이의 전달 확률이 달라지는 성질도 다뤘다.[^p6] |

## 교수와 전문 분야

양진규 교수는 2022년 9월부터 서울대학교 기계공학부에 재직하고 있다. 2013년 8월부터 2022년 9월까지 워싱턴대학교 시애틀 항공우주공학부에서 조교수·부교수·정교수로 근무했고, 그 전에는 사우스캐롤라이나대학교 조교수와 캘리포니아공과대학교 박사후연구원을 지냈다. Stanford University에서 항공우주공학 석사와 박사 학위를, KAIST에서 항공우주공학 학사 학위를 받았다.[^dept][^prof]

누리집에 제시한 전문 분야는 경량·전개 구조물, 메타물질과 복합재료(성질이 다른 재료를 구분되는 부분으로 함께 구성한 재료) 시스템 설계, 구조물의 비선형 동역학(변화의 크기에 대한 반응이 단순한 비례 관계를 따르지 않는 운동의 원리를 다루는 분야), 비파괴 평가와 구조물 상태 감시다. 최근 대표 논문에서는 판의 연결과 접힘을 계산하는 방법, 형태 변화로 소재의 성질을 바꾸는 설계, 구조 안의 파동 제어가 이어진다.[^prof][^p1][^p2][^p6]

## 응용 분야

연구실은 항공우주 구조물, 로봇, 에너지·환경 분야의 구조 시스템을 응용 대상으로 소개한다. 구체적인 대표 논문에서는 펼친 뒤 힘을 지지하는 가구·쉼터·팔 지지 장치, 저주파 진동 격리와 파동 필터, 전개 순서를 설계한 구조의 항공우주 시스템·형상 변화 구조물·부드러운 로봇 구동 장치로의 활용 가능성을 제시한다.[^home][^p2][^p4][^p5]

## 구성원

2026년 11월 11일 Members에 게시된 박사후연구원 3명, 대학원생 19명, 방문 연구원 3명, 학부 연구 인턴 3명이다. 대학원생은 석박사통합과정 14명, 박사과정 4명, 석사과정 1명이다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Jae-Kyeong KIM | 박사후연구원 |  | - Origami self-locking mechanism | 4 |
| Somya Ranjan PATRO | 박사후연구원 |  | - Wave dynamics of Negative Extensibility Metastructures. |  |
| Yasuhiro MIYAZAWA | 박사후연구원 |  | - Nonlinear wave dynamics in metamaterial - Dynamic behavior of origami-based metamaterials | 3 |
| Byoung-Gyu KIM | 석박사통합과정 |  | - Origami-based design of deployable curved surfaces and their engineering applications - Graph-theoretic and Euclidean/non-Euclidean geometric approaches to inverse design of flat-foldable thick origami structures with a smooth curved surface - Aerospace application, e.g. deployable .. |  |
| Changwoo HA | 석박사통합과정 |  | - Simulation and design methods of origami mechanics with multiple DOF - Origami robotics ​Intenational Collaborative Experience - Visiting Scholar at Princeton University (2025-26) |  |
| Dahun LEE | 석박사통합과정 |  | - Dynamics (wave, vibration) of structures - Analyzing dynamic response of origami structure ​Intenational Collaborative Experience - Visiting Scholar at Princeton University (2025-26) |  |
| Dongwook Kwak | 석박사통합과정 |  | - Dynamic modelling and controlling of rigid foldable structures - Topological wave propagation analysis of origami - Muscle-in-the-loop optimization of human walking | 1 |
| Geonhee Cho | 석박사통합과정 |  | - Configuration Space of Rigid Foldable Structure - Classification of Basic Structures - Composition of Basic Structures | 1 |
| Jemoon KIM | 석박사통합과정 |  | - Design lockable metamaterial in multi directions | 4 |
| Joohyoung LEE | 박사과정 |  | - Passive wave manipulation via nonlinear structure |  |
| Junseo KIM | 석박사통합과정 |  | - Origami-based deployable structrue - Structure (or mechanism) design |  |
| Myeonggyun JOO | 석박사통합과정 |  | - Wave Dynamics, Topological Metamaterials - Deployable Structure Design & Fabrication ​Intenational Collaborative Experience - Short-term visit at Princeton University (December, 2025) |  |
| Sehyeok Park | 석사과정 |  | - Predictive Modeling of Mechanical Properties in Kirigami-inspired Structures |  |
| Seojun CHOI | 석박사통합과정 |  | - Mechanical Coupling Effects in Kirigami-Inspired Metamaterials - Deformation modes in Origami/Kirigami structures - Single-DoF-based thick origami structures ​Intenational Collaborative Experience - Short-term visit at Tokyo University.. |  |
| Seokgyu YANG | 석박사통합과정 |  | - Mechanical analysis of origami inspired structures - Vibration control using in-situ stiffness tuning metamaterials (funded by R.O.K. Defense Acquisition Program Administration) |  |
| Seokhyeon Hong | 석박사통합과정 |  | - lightweight/deployable structure - Rigid Foldability, Energy Analysis |  |
| Seong Hyun KIM | 석박사통합과정 |  | - Lightweight & deployable structures - Helicoidal Metallic Waveguide Prototyping and Testing - Adaptive impact mitigation via origami structure |  |
| Seong Jae CHOI | 박사과정 |  | - Frequency - switchable topological edge states of Miura - folded metamaterials - Rigidity/Floppiness control of origami structures |  |
| Seungah CHOE | 박사과정 |  | - Metamaterials for acoustic impedance matching, anti-reflection, and absorption - Universal Acoustic Impedance Matching, Deployable Sound Absorber |  |
| Youngkwon KIM | 석박사통합과정 |  | - Metamorphic Structures - Reconfigurable Modular Structures - Robotics - Wave dynamics ​Intenational Collaborative Experience - Short-term visit at Princeton University (December, 2025) | 5 |
| Yu Bin OH | 박사과정 |  | - Wave analysis on origami structures |  |
| Zihe WANG | 석박사통합과정 |  | - A Generalized Micropolar Homogenization Framework - Hollow Metamaterials - Constitutive Model |  |
| Jaehyung Joshua Ju | 방문 연구원 (Associate Professor in Shanghai Jiao Tong University) |  | - Mechanical metamaterials - Meta-statics - Meta-dynamics - Meta-design - Meta-wheels |  |
| Panayotis G. Kevrekidis | 방문 연구원 (Distinguished Professor in UMass Amhest) |  | - Mathematical Physics - Nonlinear PDEs and DDEs - Dynamical Systems - Nonlinear Waves - Mathematical Biology | 6 |
| Sang-gyun Ahn | 방문 연구원 (Associate Professor in University of Washington) |  | - Industrial Design |  |
| Chaewon Baek | 학부 인턴 | 09/2023 - | - Miura-Ori Locking configuration |  |
| Jiwook Jeong | 학부 인턴 | 03/2024 - | -Simulation of Rigid Foldable Structures |  |
| Sang-uk Ahn | 학부 인턴 | 01/2025 - | - Actuation of Thick Origami for Solar Panel |  |

## 졸업생과 과거 구성원

Alumni에 게시된 25명의 과정·기간·진로다. 박사후연구원·석사과정·학부 인턴·방문 연구원 출신 4명과, 워싱턴대학교 시절로 따로 묶인 박사후연구원 5명·박사과정 7명·석사과정 9명이 함께 있다. 연월과 진로는 누리집 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hemant SHARMA | Postdoctoral Scholars: Ph.D. in Aeronautics and Astronautics (8/2025) | Assistant Professor, Birla Institute of Technology And Science, Pilani (BITS Pilani) |
| Rémy CHHO | Masters Degree Students (09/2024 - 11/2025) | Intern, Airbus, Paris |
| Suyeon Jeong | Undergraduate Research Interns (01/2024 - 08/2025) | Stanford University, Ph.D. program |
| Xiaolei WANG | Visiting Scholars (09/2025) | From Beijing Jiaotong University |
| Rui Zhu | Postdoctoral Scholars (05/2016 – 04/2017) | Professor, Beijing Institute of Technology, China |
| Gil-Yong Lee | Postdoctoral Scholars (01/2014 – 11/2016) | Professor, Kumoh National Institute of Technology, Korea |
| Eunho Kim | Postdoctoral Scholars (10/2012 – 02/2016) | Professor, Jeonbuk National University, Korea |
| Feng Li | Postdoctoral Scholars (4/2012 – 8/2013) | Professor, Beijing Institute of Technology, China |
| Amit Shelke | Postdoctoral Scholars (10/2012 – 06/2013) | Professor, Indian Institute of Technology, Guwahati (from University of South Carolina) |
| Shuaifeng Li | Ph.D. students: Ph.D. in Aeronautics and Astronautics (6/2023) | Assistant Professor, Huazhong University of Science and Technology (HUST), China |
| Xiaotian Shi | Ph.D. students: Ph.D. in Aeronautics and Astronautics (12/2022) | Research Engineer, Huawei, China |
| Seunghyun Ko | Ph.D. students: Ph.D. in Aeronautics and Astronautics (12/2021, co-advised with Prof. Marco Salviato) | Research Engineer, Pacific Northwest National Laboratory, USA |
| Chun-Wei Chen | Ph.D. students: Ph.D. in Aeronautics and Astronautics (4/2021) | Research Engineer, Metamaterial Inc., USA |
| Hyunryung Kim | Ph.D. students: Ph.D. in Aeronautics and Astronautics (12/2018) | Research Engineer, Microsoft, USA |
| Rajesh Chaunsali | Ph.D. students: Ph.D. in Aeronautics and Astronautics (08/2018) | Assistant Professor in Aerospace Engineering, Indian Institute of Science, Bangalore |
| Hiromi Yasuda | Ph.D. students: Ph.D. in Aeronautics and Astronautics (03/2018) | Assistant Professor, ISAS/JAXA, Japan |
| Qingqian Li | Masters Degree Students: M.S. in Aeronautics and Astronautics (06/2019) | Research Engineer, Comac, China |
| Balakumaran Gopalarethinam | Masters Degree Students: M.S. in Mechanical Engineering (06/2018) | Research Engineer, Black and Decker in Portland, OR, USA |
| Reed Hawkins | Masters Degree Students: M.S. in Aeronautics and Astronautics (06/2018, co-advised with Prof. Marco Salviato) | Research Engineer, Boeing, WA, USA |
| Reda El Mamoune | Masters Degree Students: Applied Master Program in Material Science & Engineering (08/2017, co-advised with Prof. Marco Salviato) | Research Engineer, Boeing, WA, USA |
| Aman Thakkar | Masters Degree Students: M.S. in Aeronautics and Astronautics (06/2017) | Ph.D. Candidate, Purdue University, USA |
| Jingmeng Tian | Masters Degree Students: Ph.D. in Aeronautics and Astronautics (08/2016) | Researcher, Seattle Pacific Trading LLC., USA |
| Noel Kimber | Masters Degree Students: M.S. in Aeronautics and Astronautics (06/2016) | Research Engineer, Stereo Display Inc., USA |
| Joshua Rivey | Masters Degree Students: M.S. in Aeronautics and Astronautics (03/2016) | F-22 Combined Test Force Assistant Director of Operations, U.S. Air Force |
| Taru Singhal | Masters Degree Students: M.S. in Aeronautics and Astronautics (06/2015) | Research Engineer, Acellent Technologies, USA |

## 최근 5년 논문 목록

Journal에 게시된 2021–2026년 논문 37편이다. 양진규 교수의 2022년 9월 서울대 부임 전 워싱턴대학교 시절 연구와 이후 서울대 소속 연구가 함께 있는 목록이다. 연도·저자·발표처는 연구실 표기를 따랐다. 연도 없이 「in print」로 적힌 세 편은 등록 출판 연도로 묶고 원래 상태를 병기했다. 별표는 누리집의 교신저자 표시이며, DOI는 각 논문 주소다.[^journals][^oa]

**2026**

- D. Kwak , G. Cho , J. Chung , J. Yang. "A unified framework for kinematic simulation of rigid foldable structures". *Journal of Computational Design and Engineering (in print) (누리집 표기 in print, 등록 출판 연도 2026)*. DOI <https://doi.org/10.1093/jcde/qwag053>.
- W. Kim, Y. Choi, S. Kim, K. Park, J. Yang\* , H. Lee\*. "Mechanical metamaterials with penetrating struts for tunable low-frequency bandgaps". *npj Metamaterials (in print) (누리집 표기 in print, 등록 출판 연도 2026)*. DOI <https://doi.org/10.1038/s44455-026-00031-y>.
- Y. Miyazawa , C. Chong, P. Kevrekidis, J. Yang. "Unveiling solitonic collisions in mechanical metamaterials". *Science Advances (in print) (누리집 표기 in print, 등록 출판 연도 2026)*. DOI <https://doi.org/10.1126/sciadv.aeb0489>.
- S. Li, D. Zhou, F. Li, P. Kevrekidis, J. Yang. "Topological edge states and amplitude-dependent delocalization in quasiperiodic elliptically geared lattices". *Physical Review Applied, 25, 024052*. DOI <https://doi.org/10.1103/z7hy-sgwj>.

**2025**

- J. Kim , S. Ahn, S. Jung, J. Kim , D. Hwang, H. Kim, S. Kim, D. Lee, J. Yang , K. Cho. "Double-Layer Self-Locking Origami Based on Opposite Folding Motion". *Soft Robotics, 21695172251401337*. DOI <https://doi.org/10.1177/21695172251401337>.
- S. Kang, Y. Kim , J. Yang , S. Ryu\*. "Physics-informed neural networks for programmable origami metamaterials with controlled deployment". *Materials Horizons 12, 24, 10641*. DOI <https://doi.org/10.1039/D5MH01607J>.
- K. Yamaguch, S. Jeong, Y. Miyazawai , Y. Oh , R. Dai, M. Mesbahi, J. Yang\*. "Controllability analysis of origami dynamics via state-space modeling". *Materials & Design, 259, 114771*. DOI <https://doi.org/10.1016/j.matdes.2025.114771>.
- S. Patro , H. Sharma , S. Yang , J. Yang\*. "Passive vibration isolation characteristics of negative extensibility metamaterials". *Extreme Mechanics Letter, 80, 102404*. DOI <https://doi.org/10.1016/j.eml.2025.102404>.
- T. Hong, J. Yang , Y. Park. "Model-based control of proprioceptive origami actuators for pneumatic manipulation". *The International Journal of Robotics Research, 02783649251366323*. DOI <https://doi.org/10.1177/02783649251366323>.
- X. Wang , Y. Wang, H. Qu, H. Wang, W. Liu, J. Yao, Z. Zhou, S. Guo, J. Yang\*. "Coupled leaf-like and Kresling patterns for origami-inspired soft continuum robots". *International Journal of Mechanical Sciences, 303, 110620*. DOI <https://doi.org/10.1016/j.ijmecsci.2025.110620>.
- S. Choi , S. Li , Y. Oh , J. Yang\*. "Frequency-switchable edge modes in Miura-folded checkerboard metamaterials". *International Journal of Mechanical Sciences, 303, 110589*. DOI <https://doi.org/10.1016/j.ijmecsci.2025.110589>.
- T. Nakagawa, S. Ko , J. Yang , M. Salviato. "Computational and experimental investigation into the effects of platelet size and flow on the tensile properties of discontinuous fiber composites". *Composites Part A, 199, 109170*. DOI <https://doi.org/10.1016/j.compositesa.2025.109170>.
- S. Li , Y. Oh , S. Choi , P. Kevrekidis, J. Yang\*. "On-demand manipulation of topological states using Miura-folded metamaterials". *Extreme Mechanics Letter, 102294*. DOI <https://doi.org/10.1016/j.eml.2025.102294>.
- J. O’Neil , M. Salviato, E. Kim , J. Yang\*. "Geometric effects on the crashworthiness of composite Kresling origami tubes". *International Journal of Solids and Structures, 309, 113199*. DOI <https://doi.org/10.1016/j.ijsolstr.2024.113199>.
- Y. Jang, E. Kim, J. Yang , J. Rho. "Sculpt wave propagation in 3D woodpile architecture through vibrational mode coupling". *Mechanical Systems and Signal Processing, 224, 112112*. DOI <https://doi.org/10.1016/j.ymssp.2024.112112>.
- Y. Jang, E. Kim \*, J. Yang\* , J. Rho. "Physics-informed discrete element modeling for the bandgap engineering of cylinder chains". *Applied Mathematical Modeling, 125, 571*. DOI <https://doi.org/10.1016/j.apm.2023.09.011>.

**2024**

- S. Li, P. Kevrekidis, X. Mao, J. Yang\*. "Topological pumping in origami metamaterials". *Physical Review B, 110, 075123*. DOI <https://doi.org/10.1103/physrevb.110.075123>.
- S. Li, P. Kevrekidis, J. Yang\*. "Emergence of elastic chiral Landau level and snake states in origami metamaterials". *Physical Review B, 109, 184109*. DOI <https://doi.org/10.1103/physrevb.109.184109>.
- T. Nakagawa, S. Ko, J. Yang , G. Houser, M. Salviato. "Repurposed discontinuous fiber composites for industrial applications: effects of platelet size, thickness, and continuous fiber plies on flexure properties". *Composites Part A, 108046*. DOI <https://doi.org/10.1016/j.compositesa.2024.108046>.
- S. Ko , T. Nakagawa, Z. Chen, W. Avery, E. Adams, M. Soja, M. Larson, C. Park, J. Yang , M. Salviato. "Effects of average number of platelets through the thickness and platelet width on the mechanical properties of discontinuous fiber composites". *Composites Part A, 107945*. DOI <https://doi.org/10.1016/j.compositesa.2023.107945>.

**2023**

- S. Li , Y. Miyazawa , K. Yamaguchi, P. Kevrekidis, J. Yang\*. "Geometry-informed dynamic mode decomposition in Kresling origami dynamics". *Extreme Mechanics Letters, 64, 102082*. DOI <https://doi.org/10.1016/j.eml.2023.102082>.
- X. Shi , R. Chaunsali , G. Theocharis, H. Huang, R. Zhu , J. Yang\*. "Topological phase transition in disordered elastic quantum spin Hall system". *Physical Review B, 108, 054205*. DOI <https://doi.org/10.1103/physrevb.108.054205>.
- K. Yamaguchi , Y. Miyazawa , H. Yasuda , Y. Song, U. Gandhi, J. Yang\*. "Post-fabrication tuning of mechanical metamaterials based on Tachi-Miura Polyhedron". *Materials and Design, 233: 112170*. DOI <https://doi.org/10.1016/j.matdes.2023.112170>.
- F. Li , Y. Wu , X. Shi , J. Yang , D. Zhou, Y. Yao. "Nonlinear topology in elliptically geared isostatic metamaterials". *Physical Review Letters, 131, 046101*. DOI <https://doi.org/10.1103/physrevlett.131.046101>.
- S. Li , P. Kevrekidis, J. Yang\*. "Characterization of elastic topological states using dynamic mode decomposition". *Physical Review B, 107, 184308*. DOI <https://doi.org/10.1103/physrevb.107.184308>.
- Y. Miyazawa , H. Yasuda , J. Yang\*. "Designs of compliant mechanisms for origami metamaterials". *Acta Mechanica Sinica, 39, 723169*. DOI <https://doi.org/10.1007/s10409-023-23169-x>.
- S. Li , L. M. Roger, L. Kumar, N. Lewinski, J. Klein, H. Putnam, J. Yang\*. "High-frequency imagery to capture coral tissue (Montipora capricornis) response to environmental stress, a pilot study". *PLoS ONE, 18(3): e0283042*. DOI <https://doi.org/10.1371/journal.pone.0283042>.
- S. Li , L. M. Roger, J. Klein, L. Cowen, N. Lewinski, J. Yang\*. "Data-driven discovery of spatiotemporal coherent patterns in pulsating soft coral tentacle motion with dynamic mode decomposition". *Physical Review Research, 5, 013175*. DOI <https://doi.org/10.1103/physrevresearch.5.013175>.
- J. O’Neil , M. Salviato, J. Yang\*. "Energy absorption behavior of filament wound CFRP origami tubes pre-folded in Kresling pattern". *Composite Structures, 116376*. DOI <https://doi.org/10.1016/j.compstruct.2022.116376>.
- L. Kumar, N. Brenner, S. Sledieski, M. Olaosebikan, M. Lynn-Goin, H. Putnam, J. Yang , N. Lewinski, R. Singh, N. M. Daniels, L. Cowen, J. Klein-Seetharaman\*. "Transfer of knowledge from model organisms to evolutionarily distant non-model organisms: the coral Pocillopora damicornis membrane signaling receptome". *PLoS Computational Biology, 18(2):e0270965*. DOI <https://doi.org/10.1371/journal.pone.0270965>.

**2022**

- S. Li , L. M. Roger, J. Klein, N. Lewinski, J. Yang\*. "Spatiotemporal dynamics of coral polyps in fluidic platform". *Physical Review Applied, 18, 024078*. DOI <https://doi.org/10.1103/physrevapplied.18.024078>.
- Y. Miyazawa , C. Chen , T. S. Gormley , G. Yin , R. Chaunsali , G. Theocharis, J. Yang\*. "Topological state transfer in Kresling origami". *Communications Materials, 3, 62*. DOI <https://doi.org/10.1038/s43246-022-00280-0>.
- J. Suh , Y. Miyazawa , J. Yang\* , J. Han\*. "Self-reconfiguring and stiffening origami tube". *Advanced Engineering Materials, 24, 2101202*. DOI <https://doi.org/10.1002/adem.202101202>.
- H. Yasuda , K. Johnson , V. Arroyos , K. Yamaguchi , J. Raney, J. Yang\*. "Leaf-like origami with bistability for self-adaptive grasping motions". *Soft Robotics, 9(5), 938-947*. DOI <https://doi.org/10.1089/soro.2021.0008>.
- Y. Miyazawa , C. Chong, P.G. Kevrekidis, J. Yang\*. "Rogue and solitary waves in coupled phononic crystals". *Physical Review E, 105, 034202*. DOI <https://doi.org/10.1103/physreve.105.034202>.
- K. Yamaguchi , H. Yasuda , K. Tsujikawa , T. Kunimine, J. Yang\*. "Graph-theoretic estimation of reconfigurability in origami-based metamaterials". *Materials and Design, 213, 110343*. DOI <https://doi.org/10.1016/j.matdes.2021.110343>.

**2021**

- Y. Miyazawa , H. Yasuda , H. Kim , K. Tsujikawa , T. Kunimine, J. Raney, J. Yang\*. "Heterogeneous origami architected materials with variable stiffness". *Communications Materials, 2:110*. DOI <https://doi.org/10.1038/s43246-021-00212-4>.

## 수상과 선정

2021년 10월 22일부터 2026년 10월 22일까지의 Board 수상·선정 글에 적힌 7건이다. 날짜는 본문이 밝힌 수상일을 우선하고, 그 밖에는 게시일이다. 수상자 이름과 상의 등급은 해당 글의 표기다.[^aw1][^aw2][^aw3][^aw4][^aw5]

- 2025-06-13 · Yubin이 Phononics 2025 Poster Presentation Award 1st Prize를 받았다.
- 2025-06-13 · Somya가 Phononics 2025 Poster Presentation Award 3rd Prize를 받았다.
- 2025-06-13 · Dongwook이 Phononics 2025 Poster Presentation Award를 받았다.
- 2024-06-19 · Junseo Kim이 BK21 Level 4 Outstanding Graduate Students에 선정되었다.
- 2024-03-19 · Jemoon Kim이 서울대학교 BK21 우수대학원생 펠로우십 장학생으로 선정되었다. 시상식은 3월 14일에 열렸다.
- 2024-02-27 · Junseo Kim이 공과대학 Excellent Teaching Assistant Award를 받았다.
- 2024-01-17 · Seonghyun Kim이 학과 Outstanding Major Course Teaching Assistant에 선정되었다.

## 연락과 위치

- 연구실: 서울시 관악구 관악로 1 서울대학교 301동 1217호, 우편번호 08826.[^contact]
- 교수 사무실: 서울대학교 301동 1424호.[^prof][^dept]
- 기관 전화: +82-2-880-1676.[^contact]
- 교수 이메일: jkyang11@snu.ac.kr.[^prof][^contact]
- 연구실 대표 이메일: iyk147@snu.ac.kr.[^contact]

## 각주
[^home]: STAR Laboratory, About STAR Laboratory. <https://starlab.snu.ac.kr/> 관측일 2026-11-11.
[^dept]: 서울대학교 기계공학부, 양진규 교수 소개. <https://me.snu.ac.kr/snu__professor/%ec%96%91%ec%a7%84%ea%b7%9c-yang-jinkyu/> 관측일 2026-11-11.
[^prof]: STAR Laboratory, Professor. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub1_1> 관측일 2026-11-11.
[^research]: STAR Laboratory, Lightweight & deployable structures, Energy transfer in advanced structures, Engineering applications. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub2_1> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub2_2> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub2_3> 관측일 2026-11-11.
[^members]: STAR Laboratory, Members. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub1_2> 관측일 2026-11-11.
[^alumni]: STAR Laboratory, Alumni. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub1_3> 관측일 2026-11-11.
[^journals]: STAR Laboratory, Journal 전체 다섯 쪽. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub3_1> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub3_1&page=2> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub3_1&page=3> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub3_1&page=4> <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub3_1&page=5> 관측일 2026-11-11.
[^oa]: OpenAlex, Jinkyu Yang(ORCID 0000-0003-1547-0219)의 2021–2026년 논문 등록 서지·초록·저자 소속. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771702,publication_year:2021-2026> 관측일 2026-11-11.
[^contact]: STAR Laboratory, Contact. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_3> 관측일 2026-11-11.
[^aw1]: STAR Laboratory, Board 수상·선정 글. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_4&wr_id=27> 관측일 2026-11-11.
[^aw2]: STAR Laboratory, Board 수상·선정 글. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_4&wr_id=24> 관측일 2026-11-11.
[^aw3]: STAR Laboratory, Board 수상·선정 글. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_4&wr_id=10> 관측일 2026-11-11.
[^aw4]: STAR Laboratory, Board 수상·선정 글. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_4&wr_id=9> 관측일 2026-11-11.
[^aw5]: STAR Laboratory, Board 수상·선정 글. <https://starlab.snu.ac.kr/bbs/board.php?bo_table=sub5_4&wr_id=7> 관측일 2026-11-11.
[^p1]: D. Kwak, G. Cho, J. Chung, J. Yang, Journal of Computational Design and Engineering (온라인 2026-06-19). <https://doi.org/10.1093/jcde/qwag053> 초록 기준(출판사 논문 페이지). 초록 원문 <https://academic.oup.com/jcde/advance-article/doi/10.1093/jcde/qwag053/8711990> 관측일 2026-11-11.
[^p2]: W. Kim 외, H. Lee, npj Metamaterials (2026). <https://doi.org/10.1038/s44455-026-00031-y> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771702,publication_year:2021-2026> 관측일 2026-11-11.
[^p3]: Y. Miyazawa, C. Chong, P. G. Kevrekidis, J. Yang, Science Advances (2026). <https://doi.org/10.1126/sciadv.aeb0489> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771702,publication_year:2021-2026> 관측일 2026-11-11.
[^p4]: J.-K. Kim 외, K.-J. Cho, Soft Robotics (2025). <https://doi.org/10.1177/21695172251401337> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771702,publication_year:2021-2026> 관측일 2026-11-11.
[^p5]: S. Kang, Y. Kim, J. Yang, S. Ryu, Materials Horizons (2025). <https://doi.org/10.1039/d5mh01607j> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5084771702,publication_year:2021-2026> 관측일 2026-11-11.
[^p6]: S. Li, P. G. Kevrekidis, X. Mao, J. Yang, Physical Review B 110, 075123 (온라인 2024-08-12). <https://doi.org/10.1103/physrevb.110.075123> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.110.075123> 관측일 2026-11-11.

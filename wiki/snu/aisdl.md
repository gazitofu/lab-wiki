# AI주도 시뮬레이션 및 설계 연구실

**서울대학교 공과대학 기계공학부 · 김도년 교수**

- 영문 이름: AI-driven Simulation and Design Lab
- 분야: 핵산 나노구조 설계, 전산역학, 과학·공학 인공지능, 반도체 계측·검사, 역학 메타물질
- 대분야: 기계·로봇·제조, 소재
- 태그: 전산역학·수치 해석[^mechanics], 과학·공학 AI[^mechanics][^industrial], 설계 최적화(위상·형상 최적화)[^mechanics], 구조 설계 소재(architected materials)[^meta], 메타물질·메타광학[^meta], 컴퓨터 비전[^industrial], 반도체 계측·검사[^industrial], 약물·유전자 전달체[^dna][^carrier]
- 홈페이지: <http://aisdl.snu.ac.kr/>
- 근거와 출처: [AI주도 시뮬레이션 및 설계 연구실 근거 페이지](aisdl-sources.md)

> 분자로 만든 구조부터 기계 부품까지 힘을 받을 때의 모양과 움직임을 계산하고, 인공지능으로 설계·제조·검사를 돕는 방법을 개발하는 연구실이다.[^about][^mechanics][^industrial]

## 무엇을 연구하나

김도년 교수가 이끄는 연구실은 **구조의 모양과 재료의 성질을 계산으로 예측하고 원하는 기능에 맞춰 설계하는 일**을 연구한다. 분자는 원자가 화학적으로 결합해 이루는 입자이며, 원자는 화학 원소의 성질을 지닌 기본 단위다. 인공지능(Artificial Intelligence, AI, 학습·추론 등 지능적 작업을 수행하는 계산 기술)을 역학 해석과 연결해 분자 수준 구조, 기계 부품, 제조 공정을 다룬다. 계산 방법 개발과 함께 자연 구조의 작동 원리를 밝히고 새로운 기계적 성질을 갖는 구조·재료를 만드는 것이 목표다.[^about]

한 갈래는 **핵산으로 모양과 움직임을 설계하는 연구**다. 핵산은 염기 배열을 통해 정보를 담거나 분자 기능을 수행하는 물질이며, DNA(Deoxyribonucleic Acid, 디옥시리보핵산)와 RNA(Ribonucleic Acid, 리보핵산)가 여기에 속한다. DNA 오리가미는 DNA 가닥을 설계한 결합 위치에 따라 접어 정해진 모양의 나노구조를 만드는 기술이다. 나노구조는 나노미터 단위의 치수나 구성 요소를 가진 구조이며, 나노미터는 십억분의 일 미터다. 연구실은 핵산이 스스로 조립되는 원리와 형상 전환을 분석하고, 외부 조건에 반응하는 분자 기계·로봇의 설계 원리를 개발한다. 또한 핵산 구조를 세포 내 물질·약물 전달과 세포 동결 보호에 이용하는 방향을 연구한다.[^dna]

다른 갈래는 **계산 방법과 설계 방법 자체를 개선하는 일**이다. 전산역학은 힘과 움직임을 나타내는 관계식을 컴퓨터로 풀어 구조의 거동을 예측하는 분야다. 연구실은 유한요소법(Finite Element Method, FEM, 구조를 유한한 수의 작은 영역으로 나누어 각 영역의 관계식을 연결해 푸는 계산 방법)을 개선하고, 기계학습(자료에서 규칙을 학습해 예측이나 판단을 수행하는 계산 방법)과 결합한다. 물리 법칙을 반영한 신경망(연결된 계산 단위들의 신호 전달을 통해 입력과 출력의 관계를 학습하는 모형)으로 여러 물리 현상이 연결된 문제를 풀고, 위상 최적화(주어진 설계 영역에서 목적과 제약을 만족하도록 재료의 배치를 정하는 설계 방법)의 반복 계산을 줄이는 방법도 개발한다.[^mechanics]

이 방법들은 **제조 현장과 구조 설계**로 이어진다. 반도체 분야에서는 영상에서 무늬와 결함을 알아보는 인공지능 기반 계측·검사 방법과, 실제 제조될 무늬를 예측하는 계산 방법을 개발한다.[^industrial] 재료 분야에서는 내부 기하 구조를 설계해 강성(변형에 저항하는 정도), 파동 전달, 열에 따른 변형을 조절하는 구조 설계 소재와 역학 메타물질을 만든다. 파동은 물리량의 변화가 공간을 따라 전달되는 현상이다. 메타물질은 인공 구조 배열을 설계해 자연 물질에 없는 광학·역학 성질을 내도록 만든 소재이며, 이 연구실은 늘어날 때 옆 방향으로도 늘어나는 오그제틱 구조를 주요 대상으로 삼는다.[^meta]

## 주요 연구 주제

### 핵산 구조의 계산·설계와 분자 기계

핵산 가닥의 배열과 결합이 입체 형상과 기계적 성질을 어떻게 바꾸는지 계산한다. 원자·분자의 움직임을 계산하는 분자 동역학과 구조 전체를 다루는 유한요소 모형을 연결하고, 축적한 구조·해석 자료를 학습해 목표 형상을 설계하는 방법을 개발한다.[^dna] 대표 논문 1은 물리 모의로 얻은 구조 자료로 확산 모형(자료에 잡음을 더하는 과정과 그 역과정을 학습해 새 자료를 생성하는 모형)을 학습해 목표 형상의 DNA 오리가미를 설계했다. 일부 설계의 접힘과 구조 전환은 실험으로 확인했다.[^p1] 대표 논문 2는 설계 파일에서 구조의 평형상태와 주요 변형·열에 따른 움직임을 계산하는 SNUPI라는 분석 프로그램을 제시했고, 대표 논문 3은 이온 농도가 달라질 때 구조가 닫혔다 열리고 다시 닫히는 동역학을 모의했다. 이온은 전자를 잃거나 얻어 전하를 띤 원자·분자이며, 전하는 전기적 상호작용을 일으키는 성질이다.[^p2][^p3]

약물·유전물질을 원하는 곳까지 옮기고 내놓는 운반체도 연구한다.[^dna] DNA 하이드로젤은 DNA 가닥이 연결된 그물 구조가 물을 머금은 재료다. 연구실의 분자 운반체 연구는 이 재료의 응축·팽창을 조절해 담은 물질을 보호하고 내놓는 방법을 개발했다. 응축된 상태에서는 분해 효소(물질을 분해하는 반응의 속도를 높이는 생체 분자)에 대한 저항성이 커지고, 다시 팽창하면 분해될 수 있게 하는 방식이다.[^carrier]

### 학습을 이용한 역학 해석과 최적 설계

전기와 변형이 함께 작용하는 문제의 계산, 압축하기 어려운 재료의 계산 안정성, 시간에 따라 퍼지는 파동의 해석을 위한 유한요소 방법을 개발한다. 위상 최적화에서는 낮은 해상도의 계산 결과를 신경망으로 높은 해상도로 바꾼 뒤 그 구조에서 최적화를 이어 가는 절차를 연구한다. 해상도는 공간이나 영상의 세부를 구분하는 정도다.[^mechanics]

계산 비용을 줄이기 위한 대리 모형(비용이 큰 계산의 입력과 출력 관계를 근사하는 모형)도 다룬다. 대표 논문 7은 섬유로 강화한 적층 플라스틱의 잔류응력을 추정하는 신경망에서 어떤 적층 구성을 학습 자료로 고를지 제안했다. 잔류응력은 외부 힘을 없앤 뒤에도 물체 내부에 남는 응력이며, 응력은 물체 내부의 단위 면적에 작용하는 힘이다.[^p7] 대표 논문 8은 균열 성장의 확률분포를 계산하는 과정에서 서로 다른 대리 모형을 중첩해, 낮은 확률 영역의 특성을 반영하는 계산을 빠르게 했다.[^p8]

### 반도체 영상 계측·검사와 제조 무늬 예측

반도체 제조에서 회로 무늬의 치수를 재고 의도하지 않은 결함을 찾는 영상 처리 방법을 개발한다. 리소그래피는 빛 등의 수단으로 재료에 정해진 무늬를 형성하는 공정이다. 연구실은 제조 자료와 물리 모형을 함께 이용해 리소그래피의 무늬 형성·검사·설계를 계산하고, 신경망 기반 계측·검사 방법을 개발한다.[^industrial] 대표 논문 6은 회로의 설계 배치를 입력받아 주사전자현미경(전자빔을 표면에 주사하고 발생 신호로 영상을 얻는 현미경)의 영상을 생성하며 결함이 생길 수 있는 영역을 예측했다. 영상의 영역을 구분하는 신경망과 영상을 변환하는 신경망을 병렬로 결합하고, 실제 산업 자료로 성능을 평가했다.[^p6]

### 기하 구조로 성질을 조절하는 역학 메타물질

오그제틱 무늬의 회전·접힘·변형을 이용해 형상, 굽힘과 비틀림, 파동·진동, 열팽창을 조절하는 재료를 설계한다. 진동은 물리량이나 물체의 상태가 기준 상태 주위에서 되풀이해 변하는 현상이다. 변형률은 원래 길이에 대한 길이 변화의 비율이다. 포아송비는 늘어나거나 줄어드는 방향의 변형률에 대한 수직 방향 변형률의 비에 음의 부호를 붙인 값이며, 열팽창계수는 온도 변화에 대한 상대적인 길이 변화율이다.[^meta] 대표 논문 4는 서로 다른 재료를 이은 보와 회전하는 사각 단위를 이용해 포아송비와 열팽창계수를 독립적으로 조절하는 판을 제시하고 계산·실험으로 확인했다.[^p4] 대표 논문 5는 절개한 평면을 입체로 펼치는 키리가미 구조의 연결부를 위치에 따라 다르게 설계해, 펼친 형상을 유지하면서 강성을 바꾸는 방법을 보였다. 같은 외부 조건에서 두 안정 상태를 가질 수 있는 성질이 쌍안정성이며, 이 논문은 그 성질을 이용한 입체 표면을 다룬다.[^p5]

## 대표 논문

서울대 재직 시기의 논문 중 핵산 구조의 설계·해석, 역학 메타물질, 반도체 검사, 학습 기반 계산을 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 저자 역할은 연구실의 공동 기여·교신저자 표기를 따른다.

| 번호 | 연도 | 논문 | 주요 저자·김도년 역할 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [De novo design of DNA origami with a generative diffusion model](https://doi.org/10.1038/s41467-026-73578-z)[^p1] | 1저자 Chien Truong-Quoc·Kyounghwa Jeon(공동 기여), 김도년 교신저자 | 물리 모의로 만든 구조 자료를 학습해 목표 형상에 맞는 DNA 오리가미를 생성한다. 일부 후보가 실제로 접히며 구조 전환과 조립 기능을 보이는지 실험했다. |
| 2 | 2025 | [SNUPI: A Computational Framework for Rapid Mechanical Analysis of Structured DNA Assemblies](https://doi.org/10.1021/jacsau.5c01110)[^p2] | 1저자 Jun Hyeong Park, 김도년·Jae Young Lee 교신저자 | DNA 설계 파일로부터 구조의 모양, 변형 방식, 열에 따른 움직임, 결합 분자의 영향을 계산하는 프로그램을 제시했다. |
| 3 | 2023 | [A computational model for structural dynamics and reconfiguration of DNA assemblies](https://doi.org/10.1038/s41467-023-42873-4)[^p3] | 1저자 Jae Young Lee, 김도년 교신저자 | DNA 구조의 평형·비평형 움직임을 함께 계산한다. 이온 농도 변화에 따라 구조가 닫혔다 열리고 다시 닫히는 과정을 모의했다. |
| 4 | 2024 | [Mechanical meta-sheets with independently tunable Poisson’s ratio and coefficient of thermal expansion](https://doi.org/10.1016/j.matdes.2024.113187)[^p4] | 1저자 Duhwan Kang·Jeong Min Hur(공동 기여), 김도년 교신저자 | 당기거나 누를 때의 가로 방향 변형과 온도에 따른 팽창을 서로 독립적으로 설계하는 판을 만들고 계산·실험으로 확인했다. |
| 5 | 2023 | [Controlling the stiffness of bistable kirigami surfaces via spatially varying hinges](https://doi.org/10.1016/j.matdes.2023.112053)[^p5] | 1저자 Hyeonho Cho, 김도년 교신저자 | 절개한 판을 펼쳐 만드는 입체 표면에서 연결부를 위치별로 다르게 설계한다. 펼친 모양과 안정성을 바꾸지 않으면서 변형에 저항하는 정도를 조절했다. |
| 6 | 2024 | [Hotspot Prediction: SEM Image Generation With Potential Lithography Hotspots](https://doi.org/10.1109/tsm.2023.3327784)[^p6] | 1저자 Jaehoon Kim·Jaekyung Lim(공동 기여), 김도년 교신저자 | 회로 설계 배치에서 현미경 영상을 생성해 결함이 생길 수 있는 위치를 보여 준다. 실제 산업 자료에서 기존 비교 모형보다 나은 예측 성능을 보였다. |
| 7 | 2026 | [Selecting Laminate Configurations for Training a DeepONet to Predict Incremental Hole-Drilling Calibration Constants in Fiber-Reinforced Plastic Laminates](https://doi.org/10.1115/1.4071199)[^p7] | 1저자 Seung-Woo Lee, 김도년 공저자 | 적층 플라스틱에 구멍을 조금씩 뚫어 잔류응력을 추정할 때 필요한 계산 상수를 신경망으로 예측한다. 적층 구성의 학습 자료를 선택하는 전략으로 예측 오차를 줄였다. |
| 8 | 2025 | [Nested surrogate model for discrete parameter optimization of structural reliability analysis](https://doi.org/10.1177/1748006x241307103)[^p8] | 1저자 Hongseok Kim, 김도년 교신저자 | 균열 성장의 확률 계산에서 유한요소 계산을 대신하는 모형과 그 결과를 학습하는 신경망을 연결해 최적의 계산 매개변수를 찾는 시간을 줄였다. |

## 교수와 전문 분야

김도년 교수는 서울대학교 기계항공공학부 학사(2000)·석사(2002), 매사추세츠공과대학교 기계공학 박사(2009)를 받았다. 박사 논문은 방향에 따라 성질이 다른 얇은 곡면 구조의 탄성·소성 해석을 다뤘다. 탄성은 힘을 없애면 원래 상태로 돌아가는 변형 성질이고, 소성은 힘을 없애도 변형이 남는 성질이다. 공군사관학교 항공우주공학과 전임강사, 매사추세츠공과대학교 생명공학과 박사후연구원을 거쳐 2013년 3월 서울대학교 조교수로 부임했다. 2017년 3월 부교수, 2022년 3월 교수가 되었다.[^pi][^department]

교수 소개는 구조 DNA·RNA 나노기술, 전산역학과 과학 기계학습, 산업 인공지능, 역학 메타물질 설계를 연구 분야로 든다. 2020년 1월부터 2025년 6월까지 기계공학부 부학부장을 맡았으며, 2026년 3월부터 POSCO Holdings의 POSCO Chair Professor로도 적혀 있다.[^pi] 최근 논문에서는 핵산 구조의 동역학을 계산하는 모형, 학습을 통한 설계·검사, 기하 구조의 변형 특성 제어를 전문 분야로 볼 수 있다.[^p1][^p3][^p4][^p6]

## 응용 분야

핵산 구조는 분자 수준의 감지·운반·구동과 세포 내 물질 전달·동결 보호를 목표로 한다.[^dna][^carrier] 산업 응용은 반도체 제조 무늬의 계측·검사와 결함 예측, 균열 성장과 부품 수명의 추정이다.[^industrial] 역학 메타물질은 형상 전환, 파동·진동 조절, 열과 힘에 따른 변형 제어를 위한 구조 설계에 연결한다.[^meta]

## 구성원

2026년 11월 6일 Current Members에 게시된 37명이다. 연구교수 1명, 박사후연구원 4명, 석박사통합과정 19명, 박사과정 6명, 석사과정 7명이다. 시작 시기·연구 주제·학교 이메일은 연구실 게시 표기를 따랐다. ‘대표 논문 참여’는 위 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Giseok Yun (윤기석) | 연구교수 | 2025.04.01 – present | Enriched Finite Element Analysis for Multiphysics Problems | kstoys@snu.ac.kr |  |
| Jozsef Adam Sebestyen (아담) | 박사후연구원 | 2025.03.01 - present | Graph Neural Networks for Scientific Machine Learning |  |  |
| Minh-Ngoc Nguyen (민-응옥 응우옌) | 박사후연구원 | 2025.10.01 - present | Topology Optimization |  |  |
| Sehyeon Kang (강세현) | 박사후연구원 | 2026.03.01 - present | Isogeometric Analysis and Design Optimization for Computational Lithography | gider@snu.ac.kr |  |
| Hyun-Suk Lee (이현석) | 박사후연구원 | 2026.09.01 - present | Physics-informed Neural Networks for Electrostatic Analysis | lhs0816@snu.ac.kr |  |
| Kwangseok Lee (이광석) | 석박사통합과정 | 2020.03.01 - present | Finite Element Analysis | ritde25@snu.ac.kr |  |
| Duhwan Kang (강두환) | 석박사통합과정 | 2021.09.01 - present | Thermo-mechanical Metastructures | flykdh20901@snu.ac.kr | 4 |
| Taeyoung Ryu (류태영) | 석박사통합과정 | 2023.03.01 – present | Multiscale Analysis of DNA/RNA Origami | rtaeyoung@snu.ac.kr |  |
| Seung-Woo Lee (이승우) | 석박사통합과정 | 2023.03.01 – present | AI-powered Computational Lithography | pl7073@snu.ac.kr | 7 |
| Eugene Jung (정유진) | 석박사통합과정 | 2024.03.01 - present | DNA Origami for Biological and Therapeutic Applications | eugene1011@snu.ac.kr |  |
| Seohyun Kwon (권서현) | 석박사통합과정 | 2024.03.01 - present | Reconfigurable DNA Origami Structures | kwonseo98@snu.ac.kr |  |
| Hongchang Lee (이홍창) | 석박사통합과정 | 2024.03.01 - present | AI-powered Virtual Inspection and Metrology | hz0128@snu.ac.kr |  |
| Jinho Kim (김진호) | 석박사통합과정 | 2024.09.01 - present | AI-powered Multibody Dynamic Analysis of DNA Origami |  | 1 |
| ChangHyun Rho (노창현) | 석박사통합과정 | 2024.09.01 - present | Vision AI for Metrology and Inspection |  |  |
| Jihoon Kim (김지훈) | 석박사통합과정 | 2025.03.01 - present | Multiscale Analysis of Supramolecular DNA Origami | rlawlgns159@snu.ac.kr |  |
| Yaejin Lee (이예진) | 석박사통합과정 | 2025.03.01 - present | AI-powered Computational Lithography | yaejin07.lee@snu.ac.kr |  |
| Donghyun Hwangbo (황보동현) | 석박사통합과정 | 2025.09.01 - present | AI-powered Characterization and 3D Reconstruction of DNA Origami | hbdh021107@snu.ac.kr |  |
| Seoeon Choi (최서언) | 석박사통합과정 | 2026.03.01 - present | AI-powered Computational Lithography | newsun0808@snu.ac.kr |  |
| Junwoo Park (박준우) | 석박사통합과정 | 2026.03.01 - present | Graph Neural Networks for Particle Simulation | junu.p@snu.ac.kr |  |
| Taehyeon Yoon (윤태현) | 석박사통합과정 | 2026.03.01 - present | Agentic AI for Metrology and Inspection | yth050105@snu.ac.kr |  |
| Siwon Chu (추시원) | 석박사통합과정 | 2026.03.01 - present | Agentic DNA Origami Design | wonny0513@snu.ac.kr |  |
| Dongha Lee (이동하) | 석박사통합과정 | 2026.03.01 - present | Agentic Metastructure Design | ehdgk888@snu.ac.kr |  |
| Seunghyuk Huh (허승혁) | 석박사통합과정 | 2026.03.01 - present | DNA Robotics | baileyh@snu.ac.kr |  |
| DongGwang Kim (김동광) | 석박사통합과정 | 2026.09.01 - present | Vision AI for Metrology and Inspection | kiimdg0815@snu.ac.kr |  |
| Dongsik Seo (서동식) | 박사과정 | 2021.09.01 - present | Information Processing with DNA Origami |  |  |
| Jun Mo Kim (김준모) | 박사과정 | 2023.03.01 – present | Reconfigurable DNA Nanostructures |  |  |
| Huisik Kim (김희식) | 박사과정 | 2024.03.01 - present | Mechanical Meta-materials | huisik.kim@snu.ac.kr |  |
| Hyewon Cho (조혜원) | 박사과정 | 2025.03.01 - present | Hierarchical DNA Origami Assemblies | gpdnjs3653@snu.ac.kr |  |
| Jeonghyun Kim (김정현) | 박사과정 | 2025.03.01 - present | Alternative Lithography with DNA Origami | jeonghyunkim@snu.ac.kr |  |
| Guhnwoo Lee (이건우) | 박사과정 | 2026.09.01 - present | Deployable Structures, Mechanical Metamaterials | thealchemist@snu.ac.kr |  |
| Jehong Lee (이제홍) | 석사과정 | 2025.03.01 - present | Graph Neural Networks for Particle Simulation | wpghd715@snu.ac.kr |  |
| Woosun Lim (임우선) | 석사과정 | 2025.03.01 - present | Crack Propagation Analysis for Structural Life Estimation | wsl061894@snu.ac.kr |  |
| Dahyun Joo (주다현) | 석사과정 | 2025.03.01 - present | Bistable Metastructures | clairda@snu.ac.kr |  |
| Dongyoub Shin (신동엽) | 석사과정 | 2025.03.01 - present | Physics-informed Inverse Analysis | dysin90@snu.ac.kr |  |
| Long Do-Pham-The (롱) | 석사과정 | 2025.11.01 - present | Generative DNA Origami Design | longdpt1002@snu.ac.kr |  |
| Yeongmin Kim (김영민) | 석사과정 | 2026.09.01 - present | Physics-informed Neural Networks for Stress Prediction | kim030912@snu.ac.kr |  |
| Hareen Kim (김하린) | 석사과정 | 2026.09.01 - present | Crack Propagation Analysis for Structural Life Estimation | haleen2002@snu.ac.kr |  |

## 졸업생과 이전 구성원

Alumni에 게시된 연구교수·박사후연구원·학위과정·인턴의 59개 항목이다. 이름이 같은 사람이 여러 과정으로 나오는 경우 각 과정의 기간과 진로를 따로 두었다. 괄호 안 기간은 해당 과정·직위의 재실 기간이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Jae Young Lee (이재영) | Research Professor (2022.09 - 2024.08) | Assistant Professor, Ajou University |  |
| Manoj Kumar Dhadwa (마노즈) | Research Professor (2019.04.01 - 2022.07.14) | Assistant Professor, San Diego State University |  |
| Jeehwan Lee (이지환) | Post Doc. (2025.08.01 - 2026.04.30) | SEMES |  |
| Yun Hyoung Nam (남윤형) | Post Doc. (2022.09 – 2025.08) | NEXTMI |  |
| Jaehoon Kim (김재훈) | Post Doc. (2022.09 – 2025.08) | NEXTMI |  |
| Giseok Yun (윤기석) | Post Doc. (2022.03 – 2025.03) | Research Professor, AISDL |  |
| Heeyuen Koh (고희연) | Post Doc. (2019.12 - 2024.06) |  |  |
| Chanseok Lee (이찬석) | Post Doc. (2019.09 - 2024.02) | Assistant Professor, Hanyang University (Erica) |  |
| Youngkyung Do (도영경) | Post Doc. (2023.02 - 2023.11) | Samsung Electronics |  |
| Jae Young Lee (이재영) | Post Doc. (2020.09 - 2022.08) | Assistant Professor, Ajou University |  |
| Kyungho Yoon (윤경호) | Post Doc. (2015.01 – 2017.01) | Associate Professor, Yonsei University |  |
| Hyun-Suk Lee (이현석) | Ph.D. (2020.03 - 2026.08) | AISDL for Postdoctoral Training | Scalable electrostatic simulation using physics-aware deep energy learning and graph neural network assembly |
| Kyounghwa Jeon (전경화) | Ph.D. (2020.09 - 2026.08) | Yale University for Postdoctoral Training | Ion-programmable state transitions in DNA hydrogels for biochemical regulation |
| Kyusoon Jung (정규순) | Ph.D. (2019.03 - 2026.02) | Samsung Electronics | Density-based topology optimization on a deformable unstructured mesh |
| Jinho Lee (이진호) | Ph.D. (2021.09 - 2025.08) | Samsung Electronics | High-performance lithography simulation using physics-informed neural networks |
| Seong Woo Lee (이성우) | Ph.D. (2017.03 – 2025.08) | LG Energy Solution | Developing a boundary graph neural network for simulating particle systems under confined environment |
| Hongseok Kim (김홍석) | Ph.D. (2021.03 - 2025.02) |  | Maintenance decision-making model for gas turbine engine component deteriorating due to fatigue cracking considering the inspection threshold and partial repair |
| Tae Yeon Kim (김태연) | Ph.D. (2018.09 - 2025.02) | Samsung Electronics | Toward accurate extraction of lithography pattern contours using deep learning models |
| Chien Truong-Quoc (트렁콕치엔) | Ph.D. (2021.09 - 2025.02) | Lecturer, Hanoi University of Science and Technology | Designing DNA origami nanostructures using Graph Neural Networks under data scarcity |
| Jozsef Adam Sebestyen (아담) | Ph.D. (2019.09 - 2025.02) | AISDL for Postdoctoral Training | Developing the Interpolation Mesh-Graph Network for physical simulations using higher-order element based meshes |
| KwangJe Lee (이광제) | Ph.D. (2017.09 - 2025.02) | Samsung Electronics | Design of bucklling induced meta-tire with circular hole array |
| Jeehwan Lee (이지환) | Ph.D. (2016.03 - 2025.02) | SEMES | Adaptive interpolation cover-based finite element method for transient wave propagation |
| Taehwi Kim (김태휘) | Ph.D. (2018.03 - 2024.08) | Samsung Electronics | Controlling torsional deformation in DNA-Gold nanoassemblies using DNA intercalators |
| Seungkwan Lee (이승관) | Ph.D. (2017.03 - 2024.08) | CarbonSix Robotics | Development of reduced analysis model for elastic shell structures with multi-stability |
| Kyung Soo Kim (김경수) | Ph.D. (2016.03 - 2024.08) | Samsung Electronics | Regulating mechanical properties and shape morphing of structured DNA assemblies using single-stranded DNA defect design approach |
| Heonyong Lee (이헌용) | Ph.D. (2014.03. - 2024.08) | Samsung Electronics | Reconstruction-based anomaly detection in multi-class dataset using domain transform data and location information in manifold |
| Jaekyung Lim (임재경) | Ph.D. (2018.09 - 2024.02) | Samsung Electronics | Efficient topology optimization using deep learning-based image super-resolution |
| Iksu Jeong (정익수) | Ph.D. (2016.09 - 2024.02) | Samsung Electronics | Data-driven identification of the mechanical behavior of materials using physics-informed neural networks and full-field displacements data |
| Jeong Min Hur (허정민) | Ph.D. (2015.09 – 2023.08) | Samsung Electronics | Designing structural stiffness using deformation modes of auxetic patterns |
| Hyeonho Cho (조현호) | Ph.D. (2016.09 – 2023.08) | Samsung Electronics | Computational design of bistable kirigami surfaces with controllable stiffness |
| Jae Gyung Lee (이재경) | Ph.D. (2016.09 – 2023.08) | SK Hynix | Computational procedure for structural analysis of DNA nanostructures |
| Youngkyung Do (도영경) | Ph.D. (2014.03 – 2023.02) | Samsung Electronics | A study on reducing the deflection of circular tubes under transverse impact through slits |
| Jaehoon Kim (김재훈) | Ph.D. (2016.09 - 2022.08) | NEXTMI | Deep-learning-based detection and prediction of lithography pattern hotspots |
| Yun Hyoung Nam (남윤형) | Ph.D. (2017.03 - 2022.08) | NEXTMI | Deep-learning-based lithography pattern classification and characterization |
| Giseok Yun (윤기석) | Ph.D. (2014.09 – 2022.02) | AISDL for Postdoctoral Training | Development of an enhanced mixed finite element method considering the stability in an incompressible analysis |
| Namkyu Kim (김남규) | Ph.D. (2018.03 – 2022.02) | Agency for Defense Development (ADD) | Overlapping finite element analysis for structures under thermal loads with spatially varying gradients |
| Jae Young Lee (이재영) | Ph.D. (2014.03 – 2020.08) | Assistant Professor, Ajou University | A multiscale modeling approach to predict the sequence-dependent shape and mechanical properties |
| Jaehyun Kim (김재현) | Ph.D. (2016.09 – 2020.02) | POSCO Global R&D Center | Experimental and numerical investigation for the fluting defect and bake hardening of metallic sheet materials originated from the yield-point phenomenon |
| Youngjoo Kim (김영주) | Ph.D. (2013.09 – 2020.02) | Samsung Electronics | Mechanical stress engineering for the shape design of DNA origami structures |
| Chanseok Lee (이찬석) | Ph.D. (2014.03 – 2019.08) | Assistant Professor, Hanyang University (Erica) | Study on the stiffness control method of DNA origami nanostructures |
| Gyeongho Kim (김경호) | M.S. (2024.05 - 2026.02) | LG Electronics | Topology optimization-based light weight design of plastic parts |
| Yoonkyung Cho (조윤경) | M.S. (2024.03 - 2026.02) | Samsung Electronics | Stress and lifetime analysis of dovetail attachment with varied geometric parameters |
| Jeong Min Lee (이정민) | M.S. (2024.03 - 2026.02) | Samsung SDI | ALOHA: anomaly-generating latent operator with hierarchical attention for fine-grained defect synthesis |
| Shreya Anirudh Tripathi (쉬레야) | M.S. (2023.09 – 2025.08) | LG Innotek | Programmable logic gate implementation using dynamic folding in DNA origami for structural computing |
| Sam Francis Ed Baumli (샘) | M.S. (2023.09 - 2025.08) |  | Physics-informed graph neural networks for mechanical modeling of lattice structures in low-data regimes |
| Yanggyun Kim (김양균) | M.S. (2022.03 - 2024.02) | Hanwha Aerospace | Improving electrostatic modeling for precise DNA structure shape prediction |
| Donghyeon Lee (이동현) | M.S. (2022.03 - 2024.02) | Samsung Electronics | Study on inverse design of mechanical structure using physics-guided neural networks and generative models |
| Jiwon Kang (강지원) | M.S. (2021.03 - 2023.02) | Makinarocks | Self-supervised denoising of SEM images for enhanced metrology and inspection |
| Sunjae Park (박선재) | M.S. (2021.03 - 2023.02) | Samsung Electronics | Identifying defects on unclean wafer surface through anomaly detection |
| Nohong Kwak (곽노홍) | M.S. (2021.03 - 2023.02) | Samsung Electronics | Effective data selection for robust training of generative adversarial network |
| Junho Park (박준호) | M.S. (2019.09 - 2023.02) |  |  |
| Myoung Seok Kim (김명석) | M.S. (2020.03 - 2022.02) | UC Berkeley for Ph.D. | Development of programmable nanoscale origami through self-assembled DNA wireframe structures |
| Jinu Jeong (정진우) | M.S. (2017.09 – 2019.06) | UIUC for Ph.D. | An accelerated framework for Brownian dynamics simulation of proteins |
| Sungho Joo (주성호) | M.S. (2017.09 – 2019.06) | Kakao | GAN based multimodal image registration for semiconductor manufacturing |
| Dongsik Seo (서동식) | M.S. (2015.03 – 2018.02) | AISDL for Ph.D | Controlling mechanical properties of tubular structures using auxetic slit pattern |
| Miyoung Lee (이미영) | M.S. (2015.03 – 2017.02) | LG Electronics | Force identification for nonlinear problems using the dynamic response sensitivity |
| Yun Hyoung Nam (남윤형) | M.S. (2015.03 - 2017.02) | NEXTMI | A numerical study on the effect of ski vibration on friction |
| Jaehoon Kim (김재훈) | M.S. (2013.03 - 2016.02) | NEXTMI | ​Dynamic analysis of biomolecular structures using the finite element method |
| Changyeob Back (백창엽) | Intern (2013.11 – 2015.04) | Apple Inc. |  |

## 최근 논문 목록 (2021–2026)

Journals의 2021–2026년 구역에 해당하는 논문 53편이다. 제목·저자·발표처는 연구실 게시 표기를 따르고, 인쇄 중인 논문은 별도로 표시했다. 별표는 연구실이 밝힌 공동 기여 표시다.[^journals]

**2026**

- Hongchang Lee, Seung-Woo Lee, and Do-Nyun Kim. "PADE: Process-adaptive denormalization for focus–dose conditioned SEM image generation". *Journal of Micro/Nanopatterning, Materials, and Metrology (인쇄 중)*.
- Teubes Christiaan Smit, Seung-Woo Lee, Do-Nyun Kim, and Robert Grant Reid. "Experimental validation of calibration constants determined by a deep operator network for IHD in laminated composite materials". *Experimental Mechanics (인쇄 중)*.
- \*Jeongmin Lee, \*Yunhyoung Nam, Young-joo Kim, Jihye Lee, and Do-Nyun Kim. "High-fidelity synthesis of slender defects via single-image-based latent blending for data-driven defect inspection". *IEEE Transactions on Semiconductor Manufacturing (인쇄 중) · <https://doi.org/10.1109/tsm.2026.3720410>*.
- Minh-Ngoc Nguyen and Do-Nyun Kim. "Coupled thermo-mechanical design optimization of multi-materials under material-specific stress constraints". *Finite Elements in Analysis and Design, 262: 104661 · <https://doi.org/10.1016/j.finel.2026.104661>*.
- Kyusoon Jung, Giseok Yun, and Do-Nyun Kim. "Density-based topology optimization on a deformable unstructured mesh with enriched finite elements". *Computers & Structures, 331: 108403 · <https://doi.org/10.1016/j.compstruc.2026.108403>*.
- \*Chien Truong-Quoc, \*Kyounghwa Jeon, Jinho Kim, Seo Hyun Kwon, Dongsik Seo, Chanseok Lee , and Do-Nyun Kim. "De novo design of DNA origami with a generative diffusion model". *Nature Communications, 17: 6792 · <https://doi.org/10.1038/s41467-026-73578-z>*.
- Seung-Woo Lee, Teubes Christiaan Smit, Do-Nyun Kim, and Robert Grant Reid. "Selecting laminate configurations for training a DeepONet to predict IHD calibration constants in FRP laminates". *Journal of Engineering Materials and Technology, 148: 031004 · <https://doi.org/10.1115/1.4071199>*.
- Hongchang Lee, Seo Hyun Kwon, and Do-Nyun Kim. "Classifying multi-state DNA origami: an automated approach with minimal labeling and confidence-based filtering". *Journal of Chemical Information and Modeling, 10: 5801–5810 · <https://doi.org/10.1021/acs.jcim.6c00780>*.
- \*Jack Y. Wang, \*Jared Huzar, \*Myoungseok Kim, Taeyoung Ryu, Nahtalee R. Lomeli, Derfogail Delcassian, Do-Nyun Kim, and Grigory Tikhomirov. "Uncovering design and assembly rules for mRNA–DNA origami". *Nano Letters, 26: 2538-2547 · <https://doi.org/10.1021/acs.nanolett.5c05607>*.

**2025**

- \*Yedam Lee, \*Woo Hyuk Jung, \*Kyounghwa Jeon, Eui Bum Choi, Taeyoung Ryu, Chanseok Lee , Do-Nyun Kim , and Dong June Ahn. "Membrane-targeted DNA frameworks with biodegradability recover cellular function and morphology from frozen cells". *Trends in Biotechnology, 43: 3196-3216 · <https://doi.org/10.1016/j.tibtech.2025.07.028>[^b1]*.
- Jun Hyeong Park, Do-Nyun Kim , and Jae Young Lee. "SNUPI: A computational framework for rapid mechanical analysis of structured DNA assemblies". *JACS Au, 5: 5813-5820 · <https://doi.org/10.1021/jacsau.5c01110>*.
- Jozsef Adam Sebestyen and Do-Nyun Kim. "Interpolation Mesh-Graph Net using disconnected spatial graphs of higher order element based meshes". *Engineering Applications of Artificial Intelligence, 159, Part C: 111535 · <https://doi.org/10.1016/j.engappai.2025.111535>*.
- Seungkwan Lee, Ju Yeon Park, Sinwoo Park, Jungju Kim, Il-Seok Jang, Ju-Dong Song, and Do-Nyun Kim. "A computational framework for investigating the mechanical stresses on breast implants under dynamic loading conditions". *Annals of Biomedical Engineering, 53: 3096-3108 · <https://doi.org/10.1007/s10439-025-03815-x>*.
- Chanseok Lee , Yanggyun Kim, Kyounghwa Jeon, Taeyoung Ryu, and Do-Nyun Kim. "Long-staple design approach towards the scalable production of scaffolded DNA origami". *Nanoscale Horizons, 10: 2584-2592 · <https://doi.org/10.1039/d5nh00357a>*.
- Jeehwan Lee, Giseok Yun , and Do-Nyun Kim. "An adaptive procedure for the analysis of transient wave propagation using interpolation covers". *Computer Methods in Applied Mechanics and Engineering, 445: 118167 · <https://doi.org/10.1016/j.cma.2025.118167>*.
- Hongseok Kim, Dooyoul Lee , and Do-Nyun Kim. "Nested surrogate model for discrete parameter optimization of structural reliability analysis". *Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability, 239: 984–999 · <https://doi.org/10.1177/1748006x241307103>*.
- Kyusoon Jung and Do-Nyun Kim. "Density-based topology optimization using a deformable mesh". *Computers & Structures, 316: 107879 · <https://doi.org/10.1016/j.compstruc.2025.107879>*.
- Hongseok Kim, Do-Nyun Kim , and Dooyoul Lee. "Maintenance decision-making model for gas turbine engine component considering the inspection threshold and partial repair". *Engineering Applications of Artificial Intelligence, 156: 111269 · <https://doi.org/10.1016/j.engappai.2025.111269>*.
- Seung-Woo Lee, Teubes Christiaan Smit, Kyusoon Jung, Robert Grant Reid, and Do-Nyun Kim. "Rapid estimation of residual stress in composite laminates using a deep operator network". *Composites Part B: Engineering, 299: 112409 · <https://doi.org/10.1016/j.compositesb.2025.112409>*.
- Giseok Yun and Do-Nyun Kim. "Accelerating continuum-based protein dynamics simulation using three-dimensional mixed overlapping element". *Computers in Biology and Medicine, 190: 110114 · <https://doi.org/10.1016/j.compbiomed.2025.110114>[^b2]*.
- Seunghyok Rho, Heeyuen Koh, Ji Woong Yu, Hye Been Koo, Sebin Kim, Je-Yeon Jung, EunYeong Jung, Chongyong Nam, Jae Young Lee, Kyounghwa Jeon, Jae-Byum Chang , Do-Nyun Kim , and Won Bo Lee. "Elasticity of swollen and folded polyacrylamide hydrogel using MARTINI coarse-grained model". *ACS Applied Materials & Interfaces, 17: 5340-5351 · <https://doi.org/10.1021/acsami.4c18162>*.
- Taehwi Kim, Seo Hyun Kwon, and Do-Nyun Kim. "A DNA origami pivot hinge driven by DNA intercalators". *ACS Nano, 19: 470-478 · <https://doi.org/10.1021/acsnano.4c09654>*.

**2024**

- Hyun Suk Lee, Giseok Yun , Ju-Hwan Song, and Do-Nyun Kim. "Two-step sub-modeling framework for thermomechanical fatigue analysis of solder joints in DRAM module". *Microelectronics Reliability, 160: 115469 · <https://doi.org/10.1016/j.microrel.2024.115469>*.
- \*Duhwan Kang, \*Jeong Min Hur, and Do-Nyun Kim. "Mechanical meta-sheets with independently tunable Poisson’s ratio and coefficient of thermal expansion". *Materials & Design, 244: 113187 · <https://doi.org/10.1016/j.matdes.2024.113187>*.
- Jae Young Lee, Yanggyun Kim, and Do-Nyun Kim. "Predicting the effect of binding molecules on the shape and mechanical properties of structured DNA assemblies". *Nature Communications, 15: 6446 · <https://doi.org/10.1038/s41467-024-50871-3>*.
- \*Chien Truong-Quoc, \*Jae Young Lee, Kyung Soo Kim, and Do-Nyun Kim. "Prediction of DNA origami shape using graph neural network". *Nature Materials, 23: 984-992 · <https://doi.org/10.1038/s41563-024-01846-8>*.
- \*Jaekyung Lim, \*Kyusoon Jung, Youngsuk Jung, and Do-Nyun Kim. "Accelerating topology optimization using deep learning-based image super-resolution". *Engineering Applications of Artificial Intelligence, 133: 108370 · <https://doi.org/10.1016/j.engappai.2024.108370>*.
- Kyounghwa Jeon, Chanseok Lee, Jae Young Lee, and Do-Nyun Kim. "DNA hydrogels with programmable condensation, expansion, and degradation for molecular carriers". *ACS Applied Materials & Interfaces, 16: 24162–24171 · <https://doi.org/10.1021/acsami.3c17633>*.
- \*Seung-Woo Lee, \*Chien Truong-Quoc, Youngmin Ro, and Do-Nyun Kim. "Adversarial deep energy method for solving saddle point problems involving dielectric elastomers". *Computer Methods in Applied Mechanics and Engineering, 421: 116825 · <https://doi.org/10.1016/j.cma.2024.116825>*.
- Tae-Yeon Kim, Sunjae Park, Chang-Kue Lim, Jae-Hyuk Choi, Chang-Hyun An, Lak-Hyun Song, and Do-Nyun Kim. "Deep learning-based detection of defects in wafer buffer zone during semiconductor packaging process". *Multiscale Science and Engineering, 6: 25-32 · <https://doi.org/10.1007/s42493-024-00103-z>*.
- \*Jaehoon Kim, \*Jaekyung Lim, Jinho Lee, Tae-Yeon Kim, Yunhyoung Nam, Kihyun Kim, and Do-Nyun Kim. "Hotspot prediction: SEM image generation with potential lithography hotspots". *IEEE Transactions on Semiconductor Manufacturing, 37: 103-114 · <https://doi.org/10.1109/tsm.2023.3327784>*.
- Taehwi Kim, Chanseok Lee, Jae Young Lee, and Do-Nyun Kim. "Controlling chiroptical responses via chemo-mechanical deformation of DNA origami structures". *ACS Nano, 18: 3414-3423 · <https://doi.org/10.1021/acsnano.3c10386>*.
- Iksu Jeong, Maenghyo Cho, Hayoung Chung , and Do-Nyun Kim. "Data-driven nonparametric identification of material behavior based on physics-informed neural network with full-field data". *Computer Methods in Applied Mechanics and Engineering, 418: 116569 · <https://doi.org/10.1016/j.cma.2023.116569>*.

**2023**

- Jae Young Lee, Heeyuen Koh, and Do-Nyun Kim. "A computational model for structural dynamics and reconfiguration of DNA assemblies". *Nature Communications, 14: 7079 · <https://doi.org/10.1038/s41467-023-42873-4>*.
- Eunseok Heo, Wooseop Hwang, Hye Been Koo, Steve Park, Do-Nyun Kim, Ho-Young Kim, YongJoo Kim, and Jae-Byum Chang. "Precise and selective macroscopic assembly of dual lock-and-key structured hydrogel". *Materials Horizons, 11: 428-441 · <https://doi.org/10.1039/d3mh00995e>*.
- ​Myoungseok Kim, Chanseok Lee, Kyounghwa Jeon, Jae Young Lee, Young-Joo Kim, Jae Gyung Lee, Hyunsu Kim, Maenghyo Cho and Do-Nyun Kim. "Harnessing a paper-folding mechanism for reconfigurable DNA origami". *Nature, 619: 78-86 · <https://doi.org/10.1038/s41586-023-06181-7>*.
- Hyeonho Cho and Do-Nyun Kim. "Controlling the stiffness of bistable kirigami surfaces via spatially varying hinges". *Materials & Design, 231: 112053 · <https://doi.org/10.1016/j.matdes.2023.112053>*.
- Giseok Yun, Jeehwan Lee, and Do-Nyun Kim. "Stability of mixed overlapping element in incompressible analysis". *Computer Methods in Applied Mechanics and Engineering, 412: 116104 · <https://doi.org/10.1016/j.cma.2023.116104>*.
- Jeong Min Hur and Do-Nyun Kim. "Auxetic meta-disk for independent control of flexural and torsional waves". *International Journal of Mechanical Sciences, 243: 108050 · <https://doi.org/10.1016/j.ijmecsci.2022.108050>*.
- \*Yunhyoung Nam, \*Youngkyung Do, Jaehoon Kim, Heonyoung Lee, and Do-Nyun Kim. "A hybrid framework to predict ski jumping forces by combining data-driven pose estimation and model-based force calculation". *European Journal of Sport Science, 23: 221-230 · <https://doi.org/10.1080/17461391.2022.2028013>*.

**2022**

- Youngkyung Do and Do-Nyun Kim. "Investigating the effect of slit patterns on the deformation of thin-walled tubes under side impact". *Journal of Mechanical Science and Technology, 36: 5649-5655 · <https://doi.org/10.1007/s12206-022-1027-4>*.
- \*Chanseok Lee, \*Yedam Lee, Woo Hyuk Jung, Tae-Yeon Kim, Taehwi Kim, Do-Nyun Kim , and Dong June Ahn. "Peptide-DNA origami as a cryoprotectant for cell preservation". *Science Advances, 8: eadd0185 · <https://doi.org/10.1126/sciadv.add0185>*.
- \*Sungho Do, \*Chanseok Lee, Taehyun Lee, Do-Nyun Kim , and Yongdae Shin. "Engineering DNA-based synthetic condensates with defined material properties, compositions and functionalities". *Science Advances, 8: eabj1771 · <https://doi.org/10.1126/sciadv.abj1771>*.
- \*Yunhyoung Nam, \*Sungho Joo, Nohong Kwak, Kihyun Kim, and Do-Nyun Kim. "Precise pattern alignment for die-to-database inspection based on the generative adversarial network". *IEEE Transactions on Semiconductor Manufacturing, 35: 532-539 · <https://doi.org/10.1109/tsm.2022.3171788>*.
- \*Heng Ni, \*Galio Guo, \*Feng Zhou, Jae Young Lee, Ned Seeman, Do-Nyun Kim, Nan Yao , Paul Chaikin , and Yimo Han. "Direct visualization of floppy 2D DNA origami using cryo-EM". *iScience, 25: 104373 · <https://doi.org/10.1016/j.isci.2022.104373>*.
- \*Chanseok Lee, \*Sungho Do, Jae Young Lee, Minju Kim, Sang Moon Kim, Yongdae Shin , and Do-Nyun Kim. "Formation of non-base-pairing DNA microgels using directed phase transition of amphiphilic monomers". *Nucleic Acids Research, 50: 4187-4196 · <https://doi.org/10.1093/nar/gkac232>*.
- Jae Gyung Lee, Kyung Soo Kim, Jae Young Lee, and Do-Nyun Kim. "Predicting the free-form shape of structured DNA assemblies from their lattice-based design blueprint". *ACS Nano, 16: 4289–4297 · <https://doi.org/10.1021/acsnano.1c10347>*.
- Namkyu Kim, Giseok Yun, and Do-Nyun Kim. "Overlapping finite element analysis for structures under thermal loads with spatially varying gradients". *Journal of Mechanical Science and Technology, 36: 1379-1390 · <https://doi.org/10.1007/s12206-022-0226-3>*.
- Young-Joo Kim, Jaekyung Lim, and Do-Nyun Kim. "Accelerated AFM characterization via deep-learning-based image super-resolution". *Small, 18: 2103779 · <https://doi.org/10.1002/smll.202103779>*.

**2021**

- \*Jae Young Lee, \*Myoungseok Kim, Chanseok Lee, and Do-Nyun Kim. "Characterizing and harnessing the mechanical properties of short single-stranded DNA in structured assemblies". *ACS Nano, 15: 20430-20441 · <https://doi.org/10.1021/acsnano.1c08861>*.
- Chanseok Lee\*, Young-Joo Kim\*, Kyung Soo Kim, Jae Young Lee and Do-Nyun Kim. "Modulating the chemo-mechanical response of structured DNA assemblies through binding molecules". *Nucleic Acids Research, 49: 12591–12599 · <https://doi.org/10.1093/nar/gkab1119>*.
- Jaehyun Kim, Hongwoo Lee, Kyungseok Oh, Dong-Yoon Seok, Sungsoo Park, Yeonsik Kang and Do-Nyun Kim. "Experimental and numerical investigation on the dent resistance of a dual phase steel originated from the yield-point phenomenon". *Journal of Materials Processing Technology, 289: 116929*.
- Jeong Min Hur\*, Dong-Sik Seo\*, Kiyean Kim, Jun Kyu Lee, Kwang Je Lee, Yoon Young Kim and Do-Nyun Kim. "Harnessing distinct deformation modes of auxetic patterns for stiffness design of tubular structures". *Materials & Design, 198: 109376*.

## 특허

2021년 10월 22일부터 2026년 10월 22일 사이 날짜가 적힌 4건이다. 발명자·번호·날짜는 누리집의 출원번호·출원일 칸 표기를 따른다.[^patents]

- 패턴의 결함 분류 방법 (발명자 김도년, 김기현, 곽노홍; 출원번호 10-2022-0027842; 출원일 2022년 03월 04일)
- 비공기입 타이어 및 그 제조 방법 (발명자 김도년, 이광제; 출원번호 10-2371395; 출원일 2022년 03월 02일)
- 얼음 결정의 형성 또는 성장 억제용 조성물 (발명자 김도년, 이찬석, 안동준, 이예담, 우상욱, 박수현; 출원번호 10-2368783; 출원일 2022년 02월 24일)
- 핵산 구조체의 제조 방법 (발명자 김도년,김명석; 출원번호 10-2021-0167625; 출원일 2021년 11월 29일)

## 수상과 선정

수상 게시판, 교수 소개, 연구실 소식에 적힌 2021년 12월부터 2026년 7월까지의 수상·선정 41건이다. 날짜는 글 제목의 수상일 또는 교수 소개의 수상 연월이며, 게시일을 사용한 항목은 ‘게시’로 표시했다. 연도만 쓴 항목은 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^awards][^pi][^news]

- 2026-07-30 게시 · Jehong Lee, LG에너지솔루션 산학협력 컨퍼런스 포스터 발표 Grand Prize 수상[^awards][^award-54]
- 2026-05-07 · Kyusoon Jung, 대한기계학회 outstanding thesis award 수상[^awards][^award-51]
- 2026-05-07 · Huisik Kim, 대한기계학회 best paper award 수상[^awards][^award-50]
- 2026-05-07 · Duhwan Kang, 대한기계학회 best paper award 수상[^awards][^award-49]
- 2026-05 · 김도년, Springer Nature Editor of Distinction Awards의 Editorial Contribution Award 수상(Journal of Mechanical Science and Technology 기여)[^pi][^award-52]
- 2026-02-25 · Jeongmin Lee, 서울대학교 공과대학 기계공학부 outstanding master’s thesis award 수상[^awards][^award-48]
- 2025-11 · 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상[^pi][^award-45]
- 2025-05 · 김도년, Springer Nature Editor of Distinction Awards의 Editorial Contribution Award 수상(Journal of Mechanical Science and Technology 기여)[^pi][^award-44]
- 2025-05 · 김도년, Springer Nature Editor of Distinction Awards의 Author Service Award 수상(Journal of Mechanical Science and Technology 기여)[^pi][^award-43]
- 2025-04-30 · Kyounghwa Jeon, International Society for Nanoscale Science, Computation and Engineering의 Seeman Student Travel Award 수상[^awards][^award-42]
- 2025-04-30 · Kyounghwa Jeon, International Society for Nanoscale Science, Computation and Engineering의 Excellent Student or Postdoc Poster Award 수상[^awards][^award-41]
- 2025-04-17 · Chien Truong-Quoc, 대한기계학회 outstanding thesis award 수상[^awards][^award-40]
- 2025-04-03 · 김도년, 한국전산구조공학회 학술상 수상[^awards][^award-39]
- 2025-02-25 · Jaehoon Kim, IEEE Transactions on Semiconductor Manufacturing의 2024 T-SM Best Paper Award 수상[^awards][^award-38]
- 2025 · 김도년, Journal of Mechanical Science and Technology의 Outstanding Service Award 수상[^awards][^award-47]
- 2024-12-06 · Yoonkyung Cho, 한국유체기계학회 Best Presentation Award 수상[^awards][^award-37]
- 2024-12 · DNA 종이접기 기술, 과학기술정보통신부 국가연구개발 우수성과 선정(기계소재 분야 최우수 성과)[^pi][^news][^news-47]
- 2024-11 · DNA 종이접기 기술, 한국기계기술단체총연합회 대한민국 올해의 기계기술 선정[^pi][^award-36]
- 2024-09 · 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상[^pi][^award-35]
- 2024-09 · 김도년, 한국공학교육학회 이기준 공학혁신상 수상[^pi][^award-34]
- 2024-07-12 · Seung-Woo Lee, 한국멀티스케일역학회 심포지엄 outstanding poster award 수상[^awards][^award-33]
- 2024-07 · 김도년, 한국멀티스케일역학회 학술상 수상[^pi][^award-32]
- 2024-05-02 · Jeong Min Hur, 대한기계학회 outstanding thesis award 수상[^awards][^award-31]
- 2024-03 · 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상[^pi][^award-30]
- 2024-02-26 · Donghyeon Lee, 서울대학교 공과대학 기계공학부 outstanding master’s dissertation award 수상[^awards][^award-29]
- 2023-10 · 김도년, 서울대학교 공과대학 신양공학학술상 수상[^pi]
- 2023-10 · 김도년, 서울대학교 공과대학 이병호 우수강의상 수상[^pi]
- 2023-08-24 · Seoungwoo Lee, 율촌 AI 연구 펠로십 선정[^news][^news-38]
- 2023-07 · 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상[^pi][^award-28]
- 2023-05-18 · Myoung Seok Kim, 대한기계학회 best paper award 수상[^awards][^award-27]
- 2023-05-18 · Yun Hyoung Nam, 대한기계학회 best paper award 수상[^awards][^award-26]
- 2022-12-16 · 김도년, 과학기술정보통신부 장관표창 수상[^awards][^award-25]
- 2022-11-06 · Hyeonho Cho, International Conference on Electronic Materials and Nanotechnology for Green Environment의 best presentation award 수상[^awards][^award-24]
- 2022-08-29 · Jaehoon Kim, 서울대학교 공과대학 기계공학부 outstanding doctoral dissertation award 수상[^awards][^award-23]
- 2022-06 · 김도년, 한국전산역학회 젊은연구자상 수상[^pi][^award-22]
- 2022-05-19 · Yun Giseok, 대한기계학회 outstanding thesis award 수상[^awards][^award-21]
- 2022-03 · Jaehoon Kim·Yun Hyoung Nam·김도년의 논문, IEEE Transactions on Semiconductor Manufacturing의 2021 T-SM Best Paper Award Honorable Mention(입선)[^pi][^award-18]
- 2022-02-25 · Myoung Seok Kim, 서울대학교 공과대학 기계공학부 outstanding master’s dissertation award 수상[^awards][^award-20]
- 2022-02-09 · Myoung Seok Kim, excellent graduate student award 수상[^awards][^award-19]
- 2021-12-22 · Seungkwan Lee·Kyusoon Jung, 한국멀티스케일역학회 심포지엄 best poster award 수상[^awards][^award-17]
- 2021-12-22 · 김도년, 한국멀티스케일역학회 젊은연구자상 수상[^awards][^award-16]

## 연락과 위치

- 교수 이메일: dnkim@snu.ac.kr[^contact]
- 연구실 공용 이메일: snussdl@gmail.com[^about]
- 교수 연락처: 02-880-1647[^contact][^department]
- 연구실 구성원 연락처: 02-880-7145[^members]
- 교수실·연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 1516호[^contact][^department]
- 연구실 추가 위치: 서울대학교 314동 304호[^about]

## 각주
[^about]: 연구실 About Us. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub1_1> 관측 2026-11-06.
[^contact]: 연구실 Contact. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub1_2> 관측 2026-11-06.
[^pi]: 연구실 Principal Investigator. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub2_1> 관측 2026-11-06.
[^members]: 연구실 Current Members. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub2_2> 관측 2026-11-06.
[^alumni]: 연구실 Alumni. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub2_3> 관측 2026-11-06.
[^dna]: 연구실 Structural DNA/RNA Nanotechnology. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub3_1_a> 관측 2026-11-06.
[^mechanics]: 연구실 Computational Mechanics & Scientific Machine Learning. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub3_1_b> 관측 2026-11-06.
[^industrial]: 연구실 Industrial Artificial Intelligence. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub3_1_c> 관측 2026-11-06.
[^meta]: 연구실 Mechanical Metamaterials. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub3_1_d> 관측 2026-11-06.
[^department]: 서울대학교 기계공학부 김도년 교수 상세. <https://me.snu.ac.kr/snu__professor/%ea%b9%80%eb%8f%84%eb%85%84-kim-do-nyun/> 관측 2026-11-06.
[^journals]: 연구실 Journals 1–8쪽. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=3> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=4> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=5> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=6> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=7> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_1&page=8> 관측 2026-11-06.
[^patents]: 연구실 Patents 1–3쪽. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_2&page=2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub4_2&page=3> 관측 2026-11-06.
[^awards]: 연구실 Awards 1–4쪽. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&page=2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&page=3> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&page=4> 관측 2026-11-06.
[^news]: 연구실 News 1–4쪽. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=2> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=3> <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1&page=4> 관측 2026-11-06.
[^p1]: C. Truong-Quoc 외, D.-N. Kim, Nature Communications (2026). <https://doi.org/10.1038/s41467-026-73578-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p2]: J. H. Park, D.-N. Kim, J. Y. Lee, JACS Au (2025). <https://doi.org/10.1021/jacsau.5c01110> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p3]: J. Y. Lee, H. Koh, D.-N. Kim, Nature Communications (2023). <https://doi.org/10.1038/s41467-023-42873-4> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p4]: D. Kang, J. M. Hur, D.-N. Kim, Materials & Design (2024). <https://doi.org/10.1016/j.matdes.2024.113187> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p5]: H. Cho, D.-N. Kim, Materials & Design (2023). <https://doi.org/10.1016/j.matdes.2023.112053> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p6]: J. Kim 외, D.-N. Kim, IEEE Transactions on Semiconductor Manufacturing (2023). <https://doi.org/10.1109/tsm.2023.3327784> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p7]: S.-W. Lee, T. C. Smit, D.-N. Kim, R. Reid, Journal of Engineering Materials and Technology (2026). <https://doi.org/10.1115/1.4071199> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^p8]: H. S. Kim, D. Lee, D.-N. Kim, Proceedings of the Institution of Mechanical Engineers Part O Journal of Risk and Reliability (2025). <https://doi.org/10.1177/1748006x241307103> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^carrier]: Kyounghwa Jeon, Chanseok Lee, Jae Young Lee, Do‐Nyun Kim, “DNA Hydrogels with Programmable Condensation, Expansion, and Degradation for Molecular Carriers”, ACS Applied Materials & Interfaces (2024). <https://doi.org/10.1021/acsami.3c17633> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5043035019,publication_year:2021-2026> 관측 2026-11-06.
[^b1]: Yedam Lee, Woo Hyuk Jung, Kyounghwa Jeon, Eui Bum Choi, Taeyoung Ryu, Chanseok Lee, Do‐Nyun Kim, Dong June Ahn, “Membrane-targeted DNA frameworks with biodegradability recover cellular function and morphology from frozen cells”, Trends in biotechnology (2025). <https://doi.org/10.1016/j.tibtech.2025.07.028> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.tibtech.2025.07.028%22> 관측 2026-11-06.
[^b2]: Giseok Yun, Do‐Nyun Kim, “Accelerating continuum-based protein dynamics simulation using three-dimensional mixed overlapping element”, Computers in Biology and Medicine (2025). <https://doi.org/10.1016/j.compbiomed.2025.110114> 초록 기준(Europe PMC 등록 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.compbiomed.2025.110114%22> 관측 2026-11-06.
[^award-54]: 연구실 수상 상세: Jehong Lee, LG에너지솔루션 산학협력 컨퍼런스 포스터 발표 Grand Prize 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=54> 관측 2026-11-06.
[^award-52]: 연구실 수상 상세: 김도년, Springer Nature Editor of Distinction Awards의 Editorial Contribution Award 수상(Journal of Mechanical Science and Technology 기여). <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=52> 관측 2026-11-06.
[^award-51]: 연구실 수상 상세: Kyusoon Jung, 대한기계학회 outstanding thesis award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=51> 관측 2026-11-06.
[^award-50]: 연구실 수상 상세: Huisik Kim, 대한기계학회 best paper award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=50> 관측 2026-11-06.
[^award-49]: 연구실 수상 상세: Duhwan Kang, 대한기계학회 best paper award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=49> 관측 2026-11-06.
[^award-48]: 연구실 수상 상세: Jeongmin Lee, 서울대학교 공과대학 기계공학부 outstanding master’s thesis award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=48> 관측 2026-11-06.
[^award-47]: 연구실 수상 상세: 김도년, Journal of Mechanical Science and Technology의 Outstanding Service Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=47> 관측 2026-11-06.
[^award-45]: 연구실 수상 상세: 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=45> 관측 2026-11-06.
[^award-44]: 연구실 수상 상세: 김도년, Springer Nature Editor of Distinction Awards의 Editorial Contribution Award 수상(Journal of Mechanical Science and Technology 기여). <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=44> 관측 2026-11-06.
[^award-43]: 연구실 수상 상세: 김도년, Springer Nature Editor of Distinction Awards의 Author Service Award 수상(Journal of Mechanical Science and Technology 기여). <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=43> 관측 2026-11-06.
[^award-42]: 연구실 수상 상세: Kyounghwa Jeon, International Society for Nanoscale Science, Computation and Engineering의 Seeman Student Travel Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=42> 관측 2026-11-06.
[^award-41]: 연구실 수상 상세: Kyounghwa Jeon, International Society for Nanoscale Science, Computation and Engineering의 Excellent Student or Postdoc Poster Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=41> 관측 2026-11-06.
[^award-40]: 연구실 수상 상세: Chien Truong-Quoc, 대한기계학회 outstanding thesis award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=40> 관측 2026-11-06.
[^award-39]: 연구실 수상 상세: 김도년, 한국전산구조공학회 학술상 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=39> 관측 2026-11-06.
[^award-38]: 연구실 수상 상세: Jaehoon Kim, IEEE Transactions on Semiconductor Manufacturing의 2024 T-SM Best Paper Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=38> 관측 2026-11-06.
[^award-37]: 연구실 수상 상세: Yoonkyung Cho, 한국유체기계학회 Best Presentation Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=37&page=2> 관측 2026-11-06.
[^award-36]: 연구실 수상 상세: DNA 종이접기 기술, 한국기계기술단체총연합회 대한민국 올해의 기계기술 선정. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=36&page=2> 관측 2026-11-06.
[^award-35]: 연구실 수상 상세: 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=35&page=2> 관측 2026-11-06.
[^award-34]: 연구실 수상 상세: 김도년, 한국공학교육학회 이기준 공학혁신상 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=34&page=2> 관측 2026-11-06.
[^award-33]: 연구실 수상 상세: Seung-Woo Lee, 한국멀티스케일역학회 심포지엄 outstanding poster award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=33&page=2> 관측 2026-11-06.
[^award-32]: 연구실 수상 상세: 김도년, 한국멀티스케일역학회 학술상 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=32&page=2> 관측 2026-11-06.
[^award-31]: 연구실 수상 상세: Jeong Min Hur, 대한기계학회 outstanding thesis award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=31&page=2> 관측 2026-11-06.
[^award-30]: 연구실 수상 상세: 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=30&page=2> 관측 2026-11-06.
[^award-29]: 연구실 수상 상세: Donghyeon Lee, 서울대학교 공과대학 기계공학부 outstanding master’s dissertation award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=29&page=2> 관측 2026-11-06.
[^award-28]: 연구실 수상 상세: 김도년, Journal of Mechanical Science and Technology의 Outstanding Contribution Award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=28&page=2> 관측 2026-11-06.
[^award-27]: 연구실 수상 상세: Myoung Seok Kim, 대한기계학회 best paper award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=27&page=2> 관측 2026-11-06.
[^award-26]: 연구실 수상 상세: Yun Hyoung Nam, 대한기계학회 best paper award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=26&page=2> 관측 2026-11-06.
[^award-25]: 연구실 수상 상세: 김도년, 과학기술정보통신부 장관표창 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=25&page=2> 관측 2026-11-06.
[^award-24]: 연구실 수상 상세: Hyeonho Cho, International Conference on Electronic Materials and Nanotechnology for Green Environment의 best presentation award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=24&page=2> 관측 2026-11-06.
[^award-23]: 연구실 수상 상세: Jaehoon Kim, 서울대학교 공과대학 기계공학부 outstanding doctoral dissertation award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=23&page=2> 관측 2026-11-06.
[^award-22]: 연구실 수상 상세: 김도년, 한국전산역학회 젊은연구자상 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=22&page=3> 관측 2026-11-06.
[^award-21]: 연구실 수상 상세: Yun Giseok, 대한기계학회 outstanding thesis award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=21&page=3> 관측 2026-11-06.
[^award-20]: 연구실 수상 상세: Myoung Seok Kim, 서울대학교 공과대학 기계공학부 outstanding master’s dissertation award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=20&page=3> 관측 2026-11-06.
[^award-19]: 연구실 수상 상세: Myoung Seok Kim, excellent graduate student award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=19&page=3> 관측 2026-11-06.
[^award-18]: 연구실 수상 상세: Jaehoon Kim·Yun Hyoung Nam·김도년의 논문, IEEE Transactions on Semiconductor Manufacturing의 2021 T-SM Best Paper Award Honorable Mention(입선). <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=18&page=3> 관측 2026-11-06.
[^award-17]: 연구실 수상 상세: Seungkwan Lee·Kyusoon Jung, 한국멀티스케일역학회 심포지엄 best poster award 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=17&page=3> 관측 2026-11-06.
[^award-16]: 연구실 수상 상세: 김도년, 한국멀티스케일역학회 젊은연구자상 수상. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_2&wr_id=16&page=3> 관측 2026-11-06.
[^news-47]: 연구실 소식 상세: DNA 종이접기 기술, 과학기술정보통신부 국가연구개발 우수성과 선정(기계소재 분야 최우수 성과). <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=47> 관측 2026-11-06.
[^news-38]: 연구실 소식 상세: Seoungwoo Lee, 율촌 AI 연구 펠로십 선정. <http://aisdl.snu.ac.kr/bbs/board.php?bo_table=sub5_1&wr_id=38&page=2> 관측 2026-11-06.

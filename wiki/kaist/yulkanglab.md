# 계산뇌인지과학 연구실 (Computational Cognitive Neuroscience Lab, CoCo Lab)

**KAIST 바이오및뇌공학과 · 강형률 교수**

- 분야: 불확실한 상황에서 뇌와 인공지능 시스템이 길을 찾고 결정을 내리는 방식(계산 인지신경과학), 베이즈 모형과 신경망 모형을 함께 쓰는 모델링, 공간 항법과 인지 지도, 불확실성 아래 의사결정과 기억, 계산정신과학
- 대분야: 기초생명·생물물리, 컴퓨팅·AI
- 태그: 계산신경과학[^home][^deptprof][^p1], 인지과학·의사결정[^home][^interview], 과학·공학 AI[^interview][^p1][^p2]
- 홈페이지: <https://yulkanglab.org>
- 근거와 출처: [계산뇌인지과학 연구실 근거 페이지](yulkanglab-sources.md)

> 뇌와 인공지능 시스템이 불확실한 상황에서 어떻게 길을 찾고 결정을 내리는지를, 베이즈 모형과 신경망 모형을 함께 써서 연구하는 바이오및뇌공학과 연구실이다. 모형은 연구실이 직접 하는 행동 실험과 공동 연구자의 신경 자료로 시험하며, 계산 인지신경과학의 기초 이해와 불면증·기분 장애 같은 뇌 질환의 이해를 목표로 든다.[^home][^interview]

## 무엇을 연구하나

누리집 첫 화면의 Mission 칸은 연구실이 뇌와 인공지능 시스템이 불확실성을 헤쳐 나가는 방식을 연구한다고 소개한다. 접근 방법으로는 지금까지 대체로 따로 발전해 온 두 전통, 곧 베이즈 모형(관측한 증거로 가능한 상태들에 대한 믿음을 확률로 고쳐 나가는 모형)과 신경망 모형을 결합한다고 적는다. 모형은 연구실이 직접 하는 행동 실험과 공동 연구자의 신경 자료로 시험하며, 계산 인지신경과학의 기초 이해와 불면증·기분 장애를 포함한 뇌 질환의 이해를 넓히는 것을 목표로 든다.[^home]

Team 페이지의 교수 소개는 교수가 뇌의 한계, 곧 한정된 시간, 기억, 정보로 뇌가 어떻게 배우고 결정하는지를 연구하며, 인공지능 시스템에서 이 한계를 조작한 결과를 뇌와 비교하는 방식으로 탐구한다고 적는다.[^team] 바이오및뇌공학과 교수진 목록과 교수 소개는 연구분야를 인공지능과 뇌의 작동 메커니즘 비교, 불확실성 하의 의사결정, 시각 기반 자율주행 등, 인지계산뇌과학, 계산정신과학으로 적는다.[^deptlist][^deptprof]

학과 소식지의 교수 인터뷰(2023년 9월 1일 게시)에서 교수는 뇌가 불확실한 상황에서 의사결정을 내리는 방식을 연구하며, 그 가운데 여러 단계에 걸쳐 정보를 모으고 합쳐 내리는 순차적 의사결정에 집중한다고 설명했다. 연구실은 먼저 주어진 문제를 최적으로 해결하는 방법을 인공지능 알고리듬으로 알아낸 뒤, 문제 해결의 각 단계에 생물학적·환경적 요인으로 들어가는 잡음과 편향을 바꿔 가며 결과를 시뮬레이션해 사람이나 동물의 행동, 뇌 활동 패턴과 비교한다. 이렇게 어느 단계에 어떤 잡음과 편향이 들어가는지와 그 이유를 분석한다고 했다. 교수는 연구실이 이론 연구에 집중하며, 불확실성이 있는 상황을 모형으로 나타내는 확률적 모델링을 주력 기법으로 든다고 말했다.[^interview]

## 주요 연구 주제

### 1. 공간 항법과 확률적 인지 지도

길을 찾는 동물과 사람은 자기 위치를 직접 보지 못하고, 잡음이 섞인 감각 입력에서 추론해야 한다. 연구실은 이 위치 추론의 불확실성이 뇌의 공간 표상과 길찾기 행동을 어떻게 만드는지 연구한다.[^home][^cosyne]

KAIST에서 낸 대표 논문 2는 잡음 섞인 자기 중심 시각 신호와 자기 운동 신호로 길을 찾는 에이전트 모형을 만들고, 앞으로 볼 시각 자극을 예측하도록 학습시키면 그 은닉 표상이 베이즈 이상 관찰자의 자세에 대한 사후 믿음과 장소 세포 활동을 닮는다는 것을 보였다.[^p2] 대표 논문 1은 이를 넓혀, 지각 추론을 넣은 베이즈 관찰자의 위치 믿음이 장소 세포 활동의 장소장 폭, 넓이, 밀도를 재현하고 다음 감각 입력을 예측하도록 학습한 순환 신경망이 베이즈 믿음과 닮은 표상을 배운다는 것을 보였다.[^p1] 같은 주제의 Cosyne 2024 포스터 발표는, 다음 시각 자극을 예측하도록 학습한 오토인코더 변형의 은닉 상태가 직접 설계한 이상 관찰자의 위치 믿음과 그 불확실성을 나타낸다고 보고했다.[^cosyne]

누리집 Research 칸은 공동 연구자와 함께 밝힌 결과로, 환경의 기하 구조에 따라 「변형」된다고 여겨지던 격자장(격자 세포가 활동하는 자리들이 이루는 무늬)이 실은 동물이 자기 위치에 대해 갖는 불확실성을 나타낸다는 것을 든다. 이를 위해 신경 표상의 변형과 귀소 행동의 편향·변동을 함께 예측하는 규범 이론, 그리고 1인칭 시점 영상과 자기 중심 움직임을 입력으로 받아 바깥 기준 위치에 대한 사후 믿음을 내는 이상 관찰자 모형을 만들었다고 적는다.[^home] 이 연구는 Daniel M. Wolpert, Máté Lengyel과 함께 한 bioRxiv 사전 공개본(2023년 2월 게시)으로 나와 있다.[^home][^pubs]

Team 페이지의 구성원 소개는 현재 과제로 예측 학습이 뇌의 확률적 표상 학습을 돕는 방식, 뇌에서 착안한 이상 관찰자를 쓴 공간 항법 모형, 감각 단서가 불확실하거나 서로 어긋날 때의 길찾기, 사람이 여러 단계의 불확실성을 합치는 방식을 든다.[^team]

### 2. 불확실성 아래 의사결정과 기억

누리집 Research 칸은 의사결정과 기억에 관한 결과로 두 가지를 든다. 일화 기억 연구에서는 단 한 번 겪은 일에 대한 기억이 정도를 가진 불확실성과 함께 남으며, 이 불확실성이 명시적 선택에 나타나는 인과 추론에 쓰일 뿐 아니라 명시적 선택을 고려한 뒤에도 시선에 드러난다는 것을 보였다(CCN 2023). 두 과제 연구에서는 한 물체에 대한 두 결정이 동시에 내려지지 못하고 하나씩 내려지며, 각 결정의 증거가 번갈아 쌓인다는 것을 새 행동 과제와 선택·반응 시간의 결합 분포를 맞추는 효율적인 표류-확산 모형으로 보였다(eLife 2021).[^home] 출판사 등록 서지는 eLife 2021 논문의 교수 소속을 Columbia University와 University of Cambridge로, CCN 2023 논문의 교수 소속을 Queen Mary University of London으로 적는다.[^pubs]

Team 페이지의 구성원 소개는 현재 과제로 여러 과제를 두고 내리는 의사결정의 모형화, 뇌파(EEG) 자료의 모형화와 결정할 때 뇌가 기대를 쓰는 방식, 시선을 예측하는 능동 감지 모형을 든다.[^team]

### 3. 계산정신과학과 수면

바이오및뇌공학과 교수 소개는 연구분야에 계산정신과학을 적는다.[^deptprof] 교수는 학과 인터뷰에서 불확실성 아래 의사결정 능력이 떨어지는 것이 여러 정신 질환으로 나타날 수 있다는 계산정신과학의 관점에서 연구를 계획하고 있다고 말했다.[^interview] Team 페이지의 구성원 소개는 수면·스트레스 예측(Sleep & Stress Prediction) 과제에서 뇌 영상을 분석하는 일과, 수면 과제에서 설치류의 수면 주기를 다루는 일을 현재 과제로 든다.[^team]

## 대표 논문

강형률 교수가 KAIST에 부임한 2023년 5월 뒤에 게시되거나 발표된 논문 가운데, 교수가 저자이고 초록을 확인할 수 있는 두 편을 골랐다. 두 편 모두 구성원 Yeowon Kim이 첫 저자, 교수가 마지막 저자이며 같은 주제를 다룬다. 대표 논문 1은 bioRxiv 사전 공개본이고, 대표 논문 2는 NeurIPS 2024 워크숍 포스터 논문이며, 학과 교수 소개의 수상 칸은 이 논문이 받은 NeurIPS NeuroAI Top 3 Student Paper Award에 교수를 「교신 저자」로 적는다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Predictive learning induces Bayesian cognitive maps in the hippocampus](https://doi.org/10.64898/2026.06.03.729991) · bioRxiv 사전 공개본 | 길을 찾으려면 지각이 필요하다. 눈으로 거리를 가늠할 때처럼, 위치는 잡음이 섞이고 모호한 자기 중심(자기 몸을 기준으로 한) 감각 입력에서 추론해야 한다. 그런데 공간 표상의 고전 모형 상당수는 바깥 기준 위치를 바로 관측할 수 있다고 암묵적으로 가정해 지각의 불확실성을 무시한다. 이 논문은 그런 모형과, 지각 추론을 명시적으로 넣은 베이즈 이상 관찰자(주어진 정보로 할 수 있는 최선의 확률적 추론을 하는 가상의 관찰자)를 비교했다. 베이즈 관찰자가 위치에 대해 갖는 믿음은 장소 세포(동물이 특정 장소에 있을 때 활동하는 해마 신경세포) 활동의 주요 성질인 장소장의 폭, 넓이, 밀도를 한 환경 안과 여러 환경 사이에서 더 정확하게 재현했다. 해석적 논증과 수치 시뮬레이션으로, 다음 자기 중심 감각 입력을 예측하도록 학습한 순환 신경망(이전 상태를 다음 계산에 다시 넣는 신경망)이 베이즈 믿음과 닮은 표상을 배우고 익숙한 환경과 낯선 환경 모두에서 장소 세포 같은 활동을 내며, 지금의 입력을 재현하도록 학습한 오토인코더(입력을 압축했다가 다시 복원하도록 학습하는 신경망)보다 낫다는 것을 보였다. 이 결과는 해마 회로가 예측적 지각 학습으로 경험에서 베이즈 인지 지도를 만들 수 있음을 시사한다.[^p1] | 1저자 Y. Kim(Yeowon Kim), 마지막 저자 강형률 (2명) |
| 2 | 2024 | [Predictive Learning Induces Probabilistic Cognitive Maps](https://neurips.cc/virtual/2024/99484) · NeurIPS 2024 Workshop NeuroAI (워크숍 포스터 논문) | 길을 찾으려면 잡음이 섞이고 모호한 자기 중심 감각 입력으로 환경 안에서 자기 자세(위치와 향하는 방향)를 추론해야 한다. 뇌의 장소 세포는 동물의 바깥 기준 위치와 그 불확실성을 나타낸다고 여겨지지만, 이런 확률적 표상이 어떻게 학습되는지는 분명하지 않다. 이 논문은 잡음 섞인 자기 중심 시각 신호와 자기 운동 신호로 길을 찾는 에이전트 모형을 만들었다. 에이전트가 앞으로 볼 시각 자극을 예측하도록 학습하면, 그 은닉 표상(신경망 안쪽 층의 활동)이 베이즈 이상 관찰자가 계산한 자세에 대한 사후 믿음(관측을 반영한 뒤의 확률적 믿음)과 가깝게 닮았다. 이 은닉 표상은 이상 관찰자의 사후 믿음처럼 익숙한 환경과 낯선 환경 모두에서 장소 세포 활동과도 닮았다. 지금의 시각 입력을 재현하도록 오토인코더로 학습한 에이전트에서는 이 닮음이 유의하게 약했다. 결과는 잡음 섞인 감각 입력을 예측하도록 배우면 확률적 인지 지도, 곧 자세 같은 숨은 상태를 확률로 나타낸 표상이 생길 수 있고, 이 표상이 뇌의 베이즈 추론에 꼭 필요하다는 것을 시사한다.[^p2] | 1저자 Y. Kim(Yeowon Kim), 마지막 저자 강형률 (2명) |

## 교수와 전문 분야

강형률(Yul HR Kang) 교수는 KAIST 바이오및뇌공학과 조교수다. 학과 인터뷰에서 교수는 2023년 5월부터 바이오및뇌공학과에 부임했다고 말했고, 연구실은 2023년부터 운영해 왔다.[^interview] 학과 교수 소개의 경력 칸은 2025년부터 New York University Affiliated Faculty Member, 2024년부터 KAIST 데이터사이언스대학원(Graduate School of Data Science) Adjunct Professor, 2023년부터 KAIST 바이오및뇌공학과 Assistant Professor, 2022–2023년 Queen Mary University of London 생물·실험심리학과(Department of Biological and Experimental Psychology) Lecturer(= Assistant Professor), 2019–2022년 University of Cambridge Wolfson College Junior Research Fellow, 2018–2022년 University of Cambridge 공학과 Computational and Biological Learning Lab Research Associate를 적는다. 최종 학위는 2018년 Columbia University 뇌과학 박사다.[^deptprof] 누리집 PI 칸은 이 밖에 2026년부터 KAIST Department of AX(AI Transformation) Adjunct Professor를 적고, Columbia University 박사 과정을 Michael Shadlen 연구실에서, Cambridge 박사후 연구를 Máté Lengyel 연구진에서 했으며 서울대학교에서 의학 학위(MD)를 받았다고 적는다.[^home]

학과 교수 소개는 수상으로 우수윤리교수상(2025), 교수학습혁신상(2025), NeurIPS NeuroAI Top 3 Student Paper Award(교신 저자, 2024), KAIST Q-Day 창의교육상(2024), Cosyne Presenters Travel Grant(2020), Excellent Poster, Korean Society for Computational Neuroscience(2014)를 적는다.[^deptprof] 누리집 Teaching 칸은 교수가 맡은 강의로 AI Models of the Brain(2025년 가을부터), Computational Neuroscience(2025년 봄부터), AI in Psychiatry(2025년 봄·가을부터), Computational Psychiatry(2024년 가을)를 적는다.[^home]

전문 분야는 베이즈 모형과 신경망 모형으로 불확실성 아래의 의사결정, 기억, 공간 항법을 설명하는 계산 인지신경과학이다.[^home][^deptprof] 교수는 Columbia University에서 계산 뇌과학과 의사결정을, Cambridge에서 불확실성 속의 길찾기, 학습, 기억을 연구했다고 인터뷰에서 설명했다.[^interview] 학과 교수 소개의 대표 연구실적은 KAIST에서 낸 NeurIPS 2024 워크숍 논문(대표 논문 2)과 함께, 부임 전 연구로 Bernstein Conference 2021 구두 발표(공간 불확실성과 환경 기하 구조), eLife 2021 논문(한 물체에 대한 여러 결정), Current Biology 2017 논문(Piercing of consciousness as a threshold crossing operation)을 든다.[^deptprof] 누리집은 공동 연구자로 Máté Lengyel(University of Cambridge), Daniel Wolpert·Michael Shadlen(Columbia University), Gergely Csibra(Central European University), Guifen Chen(QMUL), Hugo Spiers(UCL)를 적는다.[^home]

## 응용 분야

교수는 학과 인터뷰에서 연구가 두 갈래로 응용될 수 있다고 말했다. 첫째는 인공지능 알고리듬의 발전이고, 둘째는 뇌가 최적으로 작동하지 못하는 경우, 곧 질병에 대한 이해다.[^interview] 둘째 갈래의 예로 교수는 길찾기 능력을 재는 뇌과학 방법을 발전시켜 미세한 손상까지 감지하고 치매의 조기 진단과 예방에 기여하려는 협력 연구를 진행하고 있다고 했고, 우울증, 충동 조절 장애, 주의력 결핍 과잉행동장애(ADHD)처럼 의사결정의 장애로 볼 수 있는 정신 질환을 계산정신과학의 관점에서 이해해 진단과 치료법 개발에 기여하고 싶다고 했다.[^interview] 누리집 Mission 칸은 불면증과 기분 장애를 포함한 뇌 질환의 이해를 목표로 든다.[^home] 교수는 또 자율주행 알고리듬이 쓰는, 불확실성을 고려하는 의사결정 알고리듬을 응용해 사람과 동물이 불확실한 환경에서 행동하고 결정하는 방식을 모형으로 나타낸다고 설명했다.[^interview]

## 구성원

Team 페이지 Current 칸의 대학원생 10명과 Co-supervised 칸의 박사과정 1명이다. 과정 칸은 카드의 과정 표기를 옮겼고, 바이오및뇌공학과가 아닌 학과·프로그램(뇌인지공학프로그램, 데이터사이언스대학원)은 괄호에 함께 적었다. 연구 주제는 카드 소개 가운데 관심 분야와 현재 과제를 적은 문장 그대로다. Prakriti Nayak은 Queen Mary University of London의 Intelligent Games and Game Intelligence 박사 양성 과정(Centre for Doctoral Training)에서 함께 지도하는 박사과정 학생이며, 시작 칸은 페이지 표기 그대로다. 페이지는 구성원 이메일을 적지 않는다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team]

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Kyungmi Noh (노경미) | 박사과정 |  | She is interested in exploring the modeling of various psychological mechanisms and their impact on human decision-making. Also, her interest extends to applying this knowledge to more advanced artificial intelligence models, such as strong AI and super intelligent AI, to understand and enhance their capabilities. Her current work is on modeling the decision making process upon multiple tasks. |  |
| Yeowon Kim (김여원) | 석박사통합과정 |  | She is interested in understanding the neural processes involved in spatial navigation, employing AI models as tools. Her current project aims to examine how predictive objective can help in learning probabilistic representations in the brain. | 1, 2 |
| Donghyun Lee (이동현) | 박사과정 (brain and cognitive engineering program) |  | He is interested in determinism and brain-inspired aritifical intelligence. He is currently focusing on making active sensing model for predicting gaze. |  |
| Jisoo Yang (양지수) | 박사과정 |  | They are interested in psychiatry, especially mood disorders such as bipolar disorder. They are currently participating in a project on Sleep & Stress Prediction. |  |
| Jeongjae Park (박정재) | 석사과정 (Brain and Cognitive Engineering program) |  | He is studying navigation and problem solving in the human brain, and is currently working on how humans combine multi-step uncertainty. He is also interested in consciousness and hopes to understand it one day. |  |
| Jihoo Park (박지후) | 석사과정 |  | She is interested in understanding the neural mechanisms underlying high-level cognition in the human brain, using AI models. She is also fascinated by techniques for transforming and analyzing brain activation patterns observed during cognitive processes. Currently, Jihoo is participating in the sleep and stress prediction project, focusing on analyzing brain images. |  |
| Jovanka Alvira Wijaya | 석사과정 (Graduate School of Data Science) |  | She is interested in the intersection of neuroscience and statistics, and how the brain handles uncertainty through AI and statistical-inspired modeling. Her current work is on spatial navigation model using brain-inspired ideal observer. |  |
| Fatimah Kayla Kameela | 석사과정 |  | She is interested in the intersection field between consciousness, decision-making, and mental health. Particularly, she is interested in how the brain subconsciously reaches certain decisions and the particular moment of coming into consciousness. She is currently participating in the Sleep project, focusing on rodents’ sleep cycles. |  |
| Sara Hadavi | 석사과정 |  | Her background spans biology and computer science, and she is interested in understanding how the human brain supports navigation through the lens of AI models. She views navigation as a natural meeting point of high-level cognitive processes, including learning, memory, and the handling of uncertainty. Currently, she is studying navigation when sensory cues are uncertain or in conflict. |  |
| Seoah Yoon | 석사과정 |  | She is interested in understanding how people make decisions under uncertainty through computational modeling. Her current projects involve modeling EEG data and investigating how the brain uses expectation when making decisions. |  |
| Prakriti Nayak | 박사과정 (co-supervised at QMUL Intelligent Games and Game Intelligence Centre for Doctoral Training) | Fall 2023– |  |  |

## 졸업생과 이전 구성원

Team 페이지 Alumni 칸의 4명 전부다. KAIST 학부 연구생 1명(2024–2026)과, University of Cambridge 정보공학부(Information Engineering Division)에서 교수가 함께 지도한 석사과정 학생 3명(2021–2022, 2022–2023, 2023–2024)이다. 학위·과정 칸은 페이지 표기 그대로이고, 진로 칸은 페이지가 적은 다음 행선지다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| JaeHeon Lee | undergraduate researcher at KAIST (2024–2026) | Psychological and Brain Sciences PhD program at Dartmouth |
| Oskar Stone | co-supervised master’s student at Cambridge University, Information Engineering Division (2023–2024) | Gatsby Computational Neuroscience Unit as an intern |
| Tom Durrant | co-supervised master’s student at Cambridge University, Information Engineering Division (2022–2023) | Wood Mackenzie Power and Renewables research |
| Jeroen Olieslagers | co-supervised master’s student at Cambridge University, Information Engineering Division (2021–2022) | Neural Science Doctoral Program at NYU |

## 최근 논문 목록 (2021–2026)

2021–2026년 8건이다(2026년 1, 2024년 2, 2023년 2, 2021년 3). 학술지 논문 2편, 학회 논문 1편(CCN 2023), 워크숍 논문 1편(NeurIPS 2024), bioRxiv 사전 공개본 2편, 학회 발표 2건(Cosyne 2024 포스터, Bernstein Conference 2021 구두 발표)이다. 누리집은 논문 목록 페이지를 두지 않으므로, 논문은 교수의 출판사 등록 서지에서 저자·제목·학술지 표기를 옮겼고[^pubs], NeurIPS 2024 워크숍 논문은 NeurIPS 논문 페이지[^p2], Cosyne 2024 포스터는 연구실 소식 글[^cosyne], Bernstein Conference 2021 발표는 학과 교수 소개의 대표 연구실적[^deptprof] 표기를 따랐다.

- 목록은 교수 개인의 기록이라 KAIST 부임(2023년 5월) 전 연구가 함께 있다. 2021년 3건은 Columbia University·University of Cambridge 시기 연구이고, CCN 2023 논문은 교수 소속을 Queen Mary University of London으로 적는다. 2023년 사전 공개본은 2023년 2월에 게시되었고, 출판사 등록 서지는 교수 소속으로 KAIST 바이오및뇌공학과·데이터사이언스대학원과 University of Cambridge를 함께 적는다.[^pubs]
- 사전 공개본은 「bioRxiv 사전 공개본」으로, 학회 발표는 발표 형식으로 표시했다.

**2026**

- Yeowon Kim, Yul H. R. Kang. "Predictive learning induces Bayesian cognitive maps in the hippocampus". *bioRxiv 사전 공개본, 2026*.

**2024**

- Yeowon Kim, Yul HR Kang. "Predictive Learning Induces Probabilistic Cognitive Maps". *NeurIPS 2024 Workshop NeuroAI: Fusing Neuroscience and AI for Intelligent Solutions (워크숍 포스터 논문)*.
- Yeowon Kim, Yul HR Kang. "Uncertainty encoded in a recurrent neural network trained to predict visual input during navigation". *Cosyne 2024 포스터 발표(Poster 2-019)*.

**2023**

- Yul Kang, Johannes Mahr, Márton Nagy, Krisztina Andrási, Gergely Csibra, Máté Lengyel. "Forgone, but not forgotten: separate episodic memories underlie explicit reports and eye movements". *2023 Conference on Cognitive Computational Neuroscience (CCN 2023)*.
- Yul HR Kang, Daniel M Wolpert, Máté Lengyel. "Uncertainty underlies geometric effects on navigation and grid-cell tuning". *bioRxiv 사전 공개본, 2023*.

**2021**

- D. Susie Lee, Yul H. R. Kang, Angelina V. Ruiz‐Lambides, James P. Higham. "The observed pattern and hidden process of female reproductive trajectories across the life span in a non‐human primate". *Journal of Animal Ecology, 2021*.
- Yul HR Kang, Anne Löffler, Danique Jeurissen, Ariel Zylberberg, Daniel M Wolpert, Michael N Shadlen. "Multiple decisions about one object involve parallel sensory acquisition but time-multiplexed evidence incorporation". *eLife, 2021, 10, e63721*.
- Kang YHR, Wolpert DM, Lengyel M. "Spatial uncertainty and environmental geometry in navigation". *Bernstein Conference 2021 구두 발표(Oral Presentation)*.

## 수상

누리집 첫 화면 News 칸의 수상 소식 5건과 Teaching 칸의 수상 1건이다. 문구는 페이지 표기 그대로이고, 날짜는 News 칸의 연·월이다(Teaching 칸의 수상은 연도만 적혀 있다).[^home]

- 2025-08 · Our presentation received a Poster Presentation Award from KSBNS for “Predictive Learning Induces Bayesian Cognitive Maps in the Hippocampus.”
- 2025-06 · Yul received a Best Human Rights Professor Award from the KAIST Graduate Student Council.
- 2024-12 · Computational Neuroscience was recognized with a KAIST Q-Day Education Award.
- 2024-10 · Our submission to the NeurIPS NeuroAI workshop, “Predictive Learning Induces Probabilistic Cognitive Maps,” received a Top 3 Student Paper Award.
- 2024-03 · Our very first Cosyne submission, “Uncertainty encoded in a recurrent neural network trained to predict visual input during navigation,” won a Cosyne Presenters Travel Grant.
- 2025 · 2025 KAIST Education Innovation Award

## 소식

누리집 첫 화면 News 칸의 글 가운데 수상 소식을 뺀 2건이다. 문구는 페이지 표기 그대로다.[^home]

- 2026-06 · Our preprint “Predictive learning induces Bayesian cognitive maps in the hippocampus” is now available.
- 2025-04 · Our research was presented as a talk at Cosyne Workshop “Navigation Under Uncertainty.”

## 연락과 위치

- 위치: E16-1, 507호(학과 교수 소개), E16-1 Room 507, Daehak-ro 291, Daejeon Yuseong-gu 34141 South Korea(누리집 Contact)[^deptprof][^contact]
- 전화: +82-42-350-4335(학과 교수 소개), +82 42 350 4335(누리집 Contact)[^deptprof][^contact]
- 교수 이메일: yulkang@kaist.ac.kr[^deptlist][^deptprof]
[^p1]: Y. Kim, Y. H. R. Kang, bioRxiv 사전 공개본 (게시 2026-06-05). <https://doi.org/10.64898/2026.06.03.729991> 초록 기준.
[^p2]: Y. Kim, Y. H. R. Kang, NeurIPS 2024 Workshop NeuroAI: Fusing Neuroscience and AI for Intelligent Solutions 포스터 논문 (2024). <https://neurips.cc/virtual/2024/99484> 초록 기준(NeurIPS 논문 페이지 게시 초록).
[^home]: 연구실 누리집 첫 화면 <https://yulkanglab.org> (News, Mission, Research, PI, Collaborators, Teaching 칸, 2026-10-23 열람)
[^team]: 연구실 누리집 Team 페이지 <https://yulkanglab.org/team/> (Current, Co-supervised, Alumni 칸, 2026-10-23 열람)
[^contact]: 연구실 누리집 Contact 페이지 <https://yulkanglab.org/contact/> (주소와 전화, 2026-10-23 열람)
[^cosyne]: 연구실 누리집 소식 글 「Uncertainty encoded in a recurrent neural network trained to predict visual input during navigation」 <https://yulkanglab.org/uncertainty-encoded-in-a-recurrent-neural-network-trained-to-predict-visual-input-during-navigation/> (Cosyne 2024 포스터 발표의 저자와 초록, 2026-10-23 열람)
[^pubs]: 교수 ORCID(0000-0002-8846-5296)로 찾은 출판사 등록 서지(Crossref) <https://api.crossref.org/works?filter=orcid:0000-0002-8846-5296> 와 CCN 2023 논문의 서지 <https://doi.org/10.32470/ccn.2023.1472-0> (저자 순서와 소속, 게시·출판일, 2026-10-23 조회)
[^deptlist]: KAIST 바이오및뇌공학과 교수진 목록 <https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01> (강형률 교수 항목: 직위, 박사 학위, 연구분야, 연구실, 2026-10-23 열람)
[^deptprof]: KAIST 바이오및뇌공학과 교수 소개(강형률) <https://bioeng.kaist.ac.kr/index.php?document_srl=17391&mid=bio_03_01> (직위, 연구실명, 최종학위, 연구분야, 경력, 대외활동 수상 실적, 대표 연구실적, 2026-10-23 열람)
[^interview]: KAIST 바이오및뇌공학과 소식지 바빛사 「[학과 교수 취재] 강형률 교수」 <https://bioeng.kaist.ac.kr/index.php?document_srl=17895> (2023-09-01 게시, 2026-10-23 열람)

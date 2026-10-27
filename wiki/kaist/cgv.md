# 컴퓨터 그래픽스 및 가시화 연구실 (Computer Graphics and Visualization Lab, CGV)

**KAIST 전산학부·메타버스대학원 · 박진아 교수**

- 분야: 의료 영상 분석과 형태 모델링, 컴퓨터 햅틱스, 가상 훈련, 물리 시뮬레이션, 데이터 시각화
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 그래픽스·기하 처리[^research][^p1], 햅틱[^research][^p7][^p8], 가상·증강현실[^research], 의료 AI[^p2][^p3], 생성 인공지능[^p3], 신경영상 분석·뇌 연결망[^p2][^p4], 3차원 복원·인식[^p6]
- 홈페이지: <https://cgv.kaist.ac.kr>
- 근거와 출처: [컴퓨터 그래픽스 및 가시화 연구실 근거 페이지](cgv-sources.md)

> 몸속 구조를 영상에서 수치 모형으로 만들고, 가상 물체를 보고 만지는 상호작용과 물리 현상을 계산하는 방법을 연구한다. 의료 영상·컴퓨터 그래픽스·햅틱·시각화를 연결하는 연구실이다.[^research][^professor]

## 무엇을 연구하나

박진아 교수가 KAIST 전산학부에서 이끄는 연구실로, 메타버스대학원의 참여 연구실이기도 하다.[^professor][^metalab] 연구의 공통 질문은 영상과 자료 속 대상을 어떤 수치 모형으로 나타내고, 사람이 그 모형을 어떻게 이해하고 조작하게 할 것인가이다. 누리집은 의료 영상 분석·모델링, 컴퓨터 햅틱스와 가상현실, 시뮬레이션과 데이터 시각화를 세 갈래로 소개한다.[^research]

첫째는 의료 영상에서 장기와 뇌 구조를 표현하는 방법이다. 컴퓨터 비전(사진과 영상에서 대상과 장면의 정보를 알아내는 기술), 컴퓨터 그래픽스(컴퓨터로 모양과 장면을 표현하고 만드는 기술), 기계학습(자료에서 규칙을 배우는 계산 방법)을 함께 사용한다. 연구실은 장기의 모양뿐 아니라 구조 사이의 관계와 상호작용을 수치로 나타내고, 삼차원 의료 영상의 획득 방법도 개발하고 최적화(정해진 목표에 맞는 선택을 찾는 일)한다고 설명한다.[^research] 뇌의 형태가 시간에 따라 변하는 과정을 배우는 BrainODE와, 측뇌실(뇌 안에서 뇌척수액을 담는 공간의 일부)을 주변 뇌 영역과 함께 분석하는 방법이 이 갈래의 사례다.[^p2][^p4]

둘째는 가상 공간의 물체를 보고 조작하며 촉감을 받는 방법이다. 컴퓨터 햅틱스(컴퓨터와 장치를 이용해 촉감이나 힘의 감각을 전달하는 기술)를 실시간 물리 시뮬레이션(물리 현상을 계산해 사용자의 조작에 맞춰 재현하는 방법)과 결합한다. 연구실은 가상현실 기반 훈련과 수술 시뮬레이터를 연구 목표로 든다.[^research] 손과 물체의 접촉을 고려해 삼차원 모형을 조정하는 논문은 가상 상호작용에 필요한 공간 표현을 다룬다.[^p6]

최근 햅틱 연구는 촉각 피드백의 연속성과 정서적 표현을 다룬다. 부드러운 질감을 나타내기 위해 피드백 지점이 연속해서 이동하는 길이를 연속 길이(Continuity Length, CL)로 정의하고, 손의 움직임에 맞춰 피드백 위치를 조정하는 방법을 제안했다.[^p7] 다른 논문은 진동으로 느끼는 감정과 연상하는 색의 대응을 조사했다. 정서적 활성과 색의 속성에 관한 결과를 보고하지만, 일부 색 연상의 변화는 통계적으로 뚜렷하지 않아 대응 관계를 부분적인 결과로 설명한다.[^p8]

셋째는 자료와 물리 현상을 계산 가능한 형태로 표현하는 방법이다. 입자마다 위치와 내부 상태를 두고 공통 학습 규칙을 적용하는 신경 입자 자동자(Neural Particle Automata, NPA)를 제안했으며,[^p1] 점성(유체가 변형될 때 그 변형을 거스르는 힘이 생기는 성질)으로 인한 속도 변화를 학습하는 유체 계산 방법도 연구했다.[^p5] 데이터 시각화는 자료의 패턴과 관계를 시각적인 형태로 나타내는 일이며, 연구실은 생체·의료 자료를 주된 대상으로 소개한다.[^research]

## 주요 연구 주제

### 1. 의료 영상의 형태 분석과 생성

뇌 구조의 시간 변화를 예측하고, 주변 구조와의 대응 관계로 형태를 분석한다.[^p2][^p4] 의료 영상 분할(영상에서 장기나 조직에 해당하는 영역을 구별하는 일)과 생성도 연구한다. 미리 학습한 모델에 조건을 전달하는 VCM(Volumetric Conditioning Module)은 확산 모델(자료에 잡음을 더하는 과정과 그 역과정을 이용해 새 자료를 만드는 생성 모형)에 삼차원 정보를 전달해 의료 영상을 합성한다.[^medical][^p3]

### 2. 가상환경의 촉각과 삼차원 상호작용

가상 물체의 물리적 성질을 촉감과 힘으로 전달하고, 가상환경에서의 훈련을 연구한다.[^research] 손과 물체를 그래프(대상과 그 사이의 관계를 점과 연결선으로 표현한 구조)로 나타내고, 접촉 관계를 고려해 모양과 자세를 조정하는 방법도 다룬다.[^p6]

촉각 피드백 지점의 연속적인 이동으로 부드러움을 표현하고 손 움직임에 맞춰 그 피드백을 조절한다.[^p7] 진동과 감정·색 연상의 관계를 연구해 정서적 촉각 설계에 필요한 기초를 탐색한다.[^p8]

### 3. 입자·유체 시뮬레이션과 시각화

입자의 자기 조직화(개별 요소 사이의 상호작용으로 전체 구조나 행동이 형성되는 현상)를 학습하고, 점성으로 변하는 유체의 속도를 예측한다.[^p1][^p5] 뇌 형태 예측에는 신경망(서로 연결된 계산 요소의 매개변수를 자료로 학습하는 모형)으로 시간 변화 규칙을 나타내는 상미분방정식(한 독립변수에 대한 변화율을 포함한 방정식)을 활용한다.[^p2] 이런 계산 방법과 함께 생체·의료 자료를 시각적으로 탐색하는 방법을 연구한다.[^research]

## 대표 논문

연구 갈래, 방법의 차이, 최근 연구를 함께 보여 주는 논문 8편을 골랐다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다. arXiv로 연결한 네 편은 해당 공개 판본을 읽었으며, 페이지가 밝힌 학회와의 관계를 함께 적었다.[^p3][^p4][^p5][^p6] 햅틱 논문 두 편은 OpenAlex에 등록된 초록을 읽었다.[^p7][^p8]

| 번호 | 연도 | 논문과 발표처 | 쉽게 말하면 | 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Neural Particle Automata: Learning Self-Organizing Particle Dynamics](https://cgv.kaist.ac.kr/research/neural_particle_automata/) · SIGGRAPH 2026 (채택) | 고정된 격자(공간을 점이나 선으로 나눈 구조) 대신 위치와 내부 상태를 가진 입자에 학습 규칙을 적용하는 NPA를 제안한다. 입자 사이의 상호작용을 계산하는 방법을 구성하고, 형태 형성·점 자료 분류·표면 무늬 합성에서 자기 조직화와 재생 행동을 보였다.[^p1] | 마지막 저자 Jinah Park |
| 2 | 2025 | [BrainODE: Neural Shape Dynamics for Age- and Disease-aware Brain Trajectories](https://papers.nips.cc/paper_files/paper/2025/hash/abdc8c031aa6c6917c3b593166e5e340-Abstract-Conference.html) · Advances in Neural Information Processing Systems | 나이와 인지 상태를 조건으로 뇌의 형태 변화를 연속적으로 예측하는 BrainODE를 제안한다. 한 번의 관측에서 출발해 중간 시점의 인지 상태와 뇌 형태를 차례로 예측하며, 관측 간격이 일정한 자료와 불규칙한 자료에서 방법을 평가했다.[^p2] | 마지막 저자 Jinah Park |
| 3 | 2025 | [Volumetric Conditioning Module to Control Pretrained Diffusion Models for 3D Medical Images](https://arxiv.org/abs/2410.21826) · arXiv:2410.21826 (WACV 2025 관련 판) | 미리 학습한 확산 모델에 삼차원 의료 영상의 조건 정보를 전달하는 VCM을 제안한다. 복잡한 공간 조건을 전달하는 모듈을 덧붙이고, 서로 다른 종류의 입력과 자료 규모에서 조건에 맞는 영상 생성 성능을 평가했다. 영상의 축 방향 해상도(구별할 수 있는 세부 정보의 정도)를 높이는 응용 가능성도 살폈다.[^p3] | 마지막 저자 Jinah Park |
| 4 | 2024 | [Lateral Ventricle Shape Modeling using Peripheral Area Projection for Longitudinal Analysis](https://arxiv.org/abs/2410.07148) · arXiv:2410.07148 (MIUA 2024 관련 판) | 측뇌실 표면의 변화를 주변 뇌 영역과 연결해 분석하는 방법을 제안한다. 서로 다른 시점의 측뇌실 모형을 맞추면서 주변 영역과의 대응점을 함께 최적화한다. 제안한 표현으로 정상군과 치매군의 주변 영역별 형태 변화 차이를 분석했다.[^p4] | 마지막 저자 Jinah Park |
| 5 | 2024 | [Data-driven Viscosity Solver for Fluid Simulation](https://arxiv.org/abs/2409.14653) · arXiv:2409.14653 (GRAPP 2024 관련 판) | 유체의 점성 때문에 생기는 속도 변화를 예측하는 신경망을 제안한다. 축마다 크기가 같은 대칭 격자를 구성하고, 점성의 물리 관계를 반영하는 학습 기준을 사용했다. 평면과 입체의 유체·고체 상호작용 장면에서 결과를 보였다.[^p5] | 마지막 저자 Jinah Park |
| 6 | 2024 | [Hand-object reconstruction via interaction-aware graph attention mechanism](https://arxiv.org/abs/2409.17629) · arXiv:2409.17629 (ICIP 2024 채택 판) | 손과 물체를 각각 점과 연결 관계로 표현하고 서로의 상호작용을 반영해 추정 모형을 조정한다. 같은 모형 안과 서로 다른 모형 사이에서 관련성이 높은 점을 연결하는 그래프 어텐션(점 사이 관계의 중요도를 반영하는 계산) 기법을 제안했다. 실험에서 손과 물체의 접촉이 물리적으로 그럴듯하게 표현되는지를 평가했다.[^p6] | 마지막 저자 Jinah Park |
| 7 | 2025 | [Enhancing Smoothness Perception in Mid-Air Haptic Systems: Introducing Continuity Length and Movement-Adaptive Feedback for Active Touch](https://doi.org/10.1109/WHC64065.2025.11123390) · 2025 IEEE World Haptics Conference (WHC) | 가상 표면의 부드러운 촉감을 나타내기 위해 촉각 피드백 지점이 연속적으로 움직이는 길이를 매개변수로 제안한다. 손의 움직임에 맞춰 피드백 위치를 조정하는 방법을 개발했고, 사용자 평가에서 옷감과 털 같은 질감의 부드러움을 전달하는 효과를 보였다.[^p7] | 마지막 저자 Jinah Park |
| 8 | 2026 | [Vibration–Color–Emotion Correspondences for Affective Haptic Feedback](https://doi.org/10.1109/HAPTICS66823.2026.11495492) · 2026 IEEE Haptics Symposium (HAPTICS) | 진동에서 느끼는 감정과 연상하는 색 사이에 일관된 대응이 있는지 조사했다. 진동의 특성이 정서적 활성 정도와 색의 속성에 연관되는 결과를 보였다. 다만 일부 색 연상의 변화는 통계적으로 뚜렷하지 않아, 촉각과 감정·색 사이 대응을 부분적인 결과로 설명한다.[^p8] | 마지막 저자 Jinah Park |

## 교수와 전문 분야

박진아(Jinah Park) 교수는 전산학부 교수·석좌교수이며, 연구실 소개는 KAIST ICT Endowed Chair Professor로 적는다. 메타버스대학원 교수진에도 올라 있다.[^faculty][^professor][^metaprof] 컬럼비아대학교에서 전기공학 학사(1988), 펜실베이니아대학교에서 석사(1991)와 박사(1996)를 받았다. 학과 소개는 석사를 컴퓨터 비전, 박사를 컴퓨터 그래픽스 전공으로 설명한다.[^faculty]

학과와 연구실이 밝히는 전문 분야는 의료 영상, 변형 가능한 물체의 모델링, 컴퓨터 햅틱스, 데이터 시각화다. 초기 연구에는 자기공명영상(MRI, 자기장과 전파를 이용해 몸속을 영상으로 나타내는 기법)에서 심장 운동을 정량화하는 가변형 모형(모양을 바꿀 수 있는 수치 모형) 개발이 있다.[^faculty][^professor] 대표 논문에서는 이 관심이 뇌 형태의 시간 변화, 의료 영상 생성, 입자·유체 계산, 손과 물체의 상호작용으로 이어진다.[^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

누리집이 직접 제시하는 응용은 의료 영상의 구조 분석, 가상 훈련과 수술 시뮬레이션, 생체·의료 자료의 시각화다.[^research] 대표 논문의 방법은 뇌 형태의 종단 예측(같은 대상의 시간에 따른 변화를 예측하는 일), 조건을 지정한 의료 영상 생성, 유체와 물체의 움직임 계산, 손과 물체의 접촉 표현으로 이어진다.[^p2][^p3][^p5][^p6]

## 구성원

2026년 10월 26일 구성원 목록의 학생 9명과 10월 27일 개별 소개 기준이다. Ph.D Candidate는 박사과정, Master Student·Master Program은 석사과정으로 옮겼다. 연구 주제는 개별 소개가 적은 표현이다.[^members][^students] '대표 논문 참여'는 위 표의 번호이며, 전체 저자 목록에서 같은 이름을 확인한 경우에만 표시했다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Suhyun Ahn | 박사과정 (Lab Representative) | Computer Vision in 3D Medical Image Analysis | 2, 3, 4 |
| Hyunsoo Kim | 박사과정 | Physical Simulation Computer Vision Computer Haptics | 1, 5 |
| Chanhyeok Lee | 박사과정 | Machine Learning Computer Vision Augmented Reality | 8 |
| Jihwan Park | 박사과정 | Computer Graphics Biomedical Image Analysis |  |
| Eunhye Choi | 석사과정 | Computer Graphics Biomedical Image Generation |  |
| Jewoo Shin | 석사과정 | Computer Graphics Physical Simulation |  |
| Woojin Na | 석사과정 | Medical Image Analysis Computer Vision |  |
| Hyunjun Park | 석사과정 | Medical Image Analysis Computer Vision |  |
| HyeokJae Cho | 석사과정 | Computer Graphics VR/XR Visualization |  |

## 졸업생 진로

2026년 10월 26일 Alumni 페이지의 46명이다. 박사 졸업생 구획 13명과 석사 졸업생 구획 33명이며, 학위와 진로는 페이지 표기를 따른다. 진로는 졸업 당시 또는 게시 당시 표기일 수 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Wonjung Park | Ph.D. (February 2026) | KAIST |
| Jihoon Cho | Ph.D. (August 2024); M.S. (2019) | Samsung Research |
| Taeho Kim | Ph.D. (February 2024); M.S. (February 2013) | Tomocube |
| Soonchan Park | Ph.D. (February 2024); M.S. (August 2012) | Jeonbuk National Unversity |
| Jaehyun Jang | Ph.D. (February 2022); M.S. (KAIST, August 2016) | Samsung Research |
| Joong-Youn Lee | Ph.D. (August 2021) | KISTI |
| Seokyeol Kim | Ph.D. (February 2018) | Naver Z |
| Sekil Park | Ph.D. (February 2018); M.S.E. (June 2006) | Korea Institute of Ocean Science and Technology (KIOST) |
| Kimin Kim | Ph.D. (August 2016); M.S. (August 2009) | Wenzhou University |
| Jaeil Kim | Ph.D. (February 2015) | Kyungpook National University & BeamWorks (CEO & CTO) |
| Yongwan Kim | Ph.D. (August 2014) | Electronics and Telecommunications Research Institute (ETRI) |
| Jinah Kim | Ph.D. (February 2014); M.S.E. (February 2005) | Korea Institute of Ocean Science and Technology (KIOST) |
| Sang-Youn Kim | Ph.D. (in Mechanical Engineering, 2004) | Korea University of Technology and Education (KOREATECH) |
| Chaewon Lee | M.S. (February 2026) | KT |
| Woohyun Jeong | M.S. (February 2026) | Vieworks |
| Donggyu Lee | M.S. (February 2026) | LG CNS |
| Anney Vo | M.S. (August 2025) | KAIST |
| Junhee Lee | M.S. (February 2025) | Hanwha Aerospace |
| Seunghyuck Park | M.S. (February 2025) | LG CNS |
| Gyuna Lim | M.S. (February 2024) | KAIST |
| Beomju Kim | M.S. (February 2024) | Tomocube |
| Taeyun Woo | M.S. (August 2023) | KAIST (Ph.D. program) |
| Inha Kang | M.S. (August 2022) | KAIST (Ph.D. program) |
| Minyoung Park | M.S. (February 2022) | LG Electronics |
| Youjin Chung | M.S. (February 2022) | Hyundai Motor |
| Joowon Lim | M.S. (Febuary 2021) | Naver |
| Hyunyul Cho | M.S. (February 2020) | XCENA |
| Youngjin An | M.S. (February 2019) | Socar |
| Inwoo Hwang | M.S. (February 2018) | Seoul National University (Ph.D. program) |
| Stuart Burmeister | M.S. (February 2017) | Shinsegae I&C |
| Eunbi Park | M.S. (August 2016); M.S. (TU Berlin, August 2016) | Mobinity |
| Youngju Oh | M.S. (February 2016) | Datarize |
| Uitae Kim | M.S. (February 2016) | Devcra |
| Deok-Jae Song | M.S. (August 2015) | Neople |
| Hojin Ryoo | M.S. (February 2015) | Samsung Medison |
| Chris Seonggyu Kim | M.S. (February 2014) | Vieworks |
| Mi-Hee Jo | M.S. (February 2012) | Korean Air |
| Jaehyun Cho | M.S. (February 2012) | Samsung Electronics |
| Seok Kim | M.S. (February 2011) | POSCO |
| Ye-Seul Park | M.S. (February 2010) | Naver |
| Jaehwan Cho | M.S. (August 2009) | Telecommunications Technology Association (TTA) |
| Yun-Kyu Choi | M.S. (August 2009) | MWN Tech |
| Daeseok Kim | M.S.E. (August 2007) | SIA |
| Seongyoon Cho | M.S.E. (August 2006) | Crazing Lab |
| Dongwook Lee | M.S.E. (August 2006) |  |
| Jihwan Park | Ph.D. (State University of New York at Stony Brook), M.S.E. (February 2006) | University of Oklahoma |

## 최근 논문 목록 (2021–2026)

연구실 게시 목록에서 손과 물체의 상호작용, 촉각, 가상 착용, 입자·유체 계산, 의료 영상의 생성·분석 방법을 다룬 40편이다. 연도는 누리집 기재 연도의 2021–2026년 구역을 사용한다. 학술지·학회 분류와 기재 날짜를 함께 적고, 시연·포스터 같은 발표 형식도 보존했다. 2026년 학회 항목 가운데 연구실 소식이 채택을 알리고 출판 기록은 따로 제시하지 않은 항목은 채택으로 표시했다. 연도 구역 기준이므로 2021년 10월 13일 이전 논문도 포함한다.[^publications] VCM의 정식 제목은 대표 논문 표에, 최근 목록의 제목은 연구실이 적은 짧은 표기로 실었다.[^medical][^p3]

**2026**

- Jewoo Shin, Suyong Kim, Hyungki Son, Inwook Hwang, Jinah Park. "Unified Haptic Rendering of Deformable Objects with an XPBD Particle Framework". *AsiaHaptics 2026 (채택) (누리집 분류: International Conference; 누리집 기재 날짜: 2026.09.09)*.
- Jewoo Shin, Jinah Park. "OmniBody: Discretized Local Constraints for Real-Time Destructible and Flexible Soft Bodies Simulation". *SIGGRAPH 2026 Poster (채택) (누리집 분류: International Conference; 누리집 기재 날짜: 2026.05.24)*.
- Hyunsoo Kim, Ehsan Pajouheshga, Sabine Süsstrunk, Wenzel Jakob, Jinah Park. "Neural Particle Automata: Learning Self-Organizing Particle Dynamics". *SIGGRAPH 2026 (채택) (누리집 분류: International Conference; 누리집 기재 날짜: 2026.03.31)*.
- Woohyun Jeong, Suhyun Ahn, Jinah Park. "Shape-Guided Self-Supervised Learning for Intracranial Aneurysm Segmentation". *2026 IEEE 23rd International Symposium on Biomedical Imaging (누리집 분류: International Conference; 누리집 기재 날짜: 2026.02.03)*.
- Anney Vo, Chanhyeok Lee, Jinah Park. "Vibration–Color–Emotion Correspondences for Affective Haptic Feedback". *Haptic Symposium 2026 (채택) (누리집 분류: International Conference; 누리집 기재 날짜: 2026.01.28)*.
- Suhyun Ahn Donggyu Lee Jinah Park. "Adaptability of Vision Foundation Models for 3D Medical Image Segmentation". *IEEE Open Journal of Signal Processing (누리집 분류: International Journal; 누리집 기재 날짜: 2026.01.01)*.

**2025**

- Wonjung Park Suhyun Ahn Maria del C. Valdés Hernández Susana Muñoz Maniega Jinah Park. "BrainODE: Neural Shape Dynamics for Age- and Disease-aware Brain Trajectories". *NeurIPS 2025 (누리집 분류: International Conference; 누리집 기재 날짜: 2025.12.02)*.
- Hyunsoo Kim Jinah Park. "Train Once, Generate Anywhere: Discretization Agnostic Neural Cellular Automata Using SPH Method". *SIGGRAPH 2025 (Poster) (누리집 분류: International Conference; 누리집 기재 날짜: 2025.08.09)*.
- Gyuna Lim Anney Vo Jinah Park. "Enhancing Smoothness Perception in Mid-Air Haptic Systems: Instroducing Continuity Length and Movement-Adaptive Feedback for Active Touch". *IEEE World Haptics Conference 2025 (누리집 분류: International Conference; 누리집 기재 날짜: 2025.07.08)*.
- Gyuna Lim Anney Vo Eunhye Choi Jinah Park. "TouchArt: Vibrotactile Interaction for Color Perception in Virtual Painting". *Hands-On Demos at WHC 2025 (누리집 분류: International Conference; 누리집 기재 날짜: 2025.07.08)*.
- Wonjung Park Maria del C. Valdés Hernández Jaeil Kim Susana Muñoz Maniega Fraser Sneden Karen J. Ferguson Mark E. Bastin Joanna M. Wardlaw Simon R. Cox Jinah Park. "AI-based deformable hippocampal mesh reflects hippocampal morphological characteristics in relation to cognition in healthy older adults". *NeuroImage (누리집 분류: International Journal; 누리집 기재 날짜: 2025.03.21)*.
- Suhyun Ahn Wonjung Park Jihoon Cho Seunghyuck Park Jinah Park. "Volumetric Conditioning Module to Control Pretrained Diffusion Models". *WACV 2025 (누리집 분류: International Conference; 누리집 기재 날짜: 2025.02.28)*.

**2024**

- Soonchan Park Jinah Park. "Full-body virtual try-on using top and bottom garments with wearing style control". *Computer Vision and Image Understanding (누리집 분류: International Journal; 누리집 기재 날짜: 2024.12.16)*.
- Taeyun Woo Tae-Kyun Kim Jinah Park. "Hand-Object Reconstruction Via Interaction-Aware Graph Attention Mechanism". *ICIP 2024 (누리집 분류: International Conference; 누리집 기재 날짜: 2024.10.29)*.
- Wonjung Park Suhyun Ahn Jinah Park. "Lateral Ventricle Shape Modeling using Peripheral Area Projection for Longitudinal Analysis". *MIUA 2024 (누리집 분류: International Conference; 누리집 기재 날짜: 2024.07.24)*.
- Soonchan Park Jinah Park Jiyoung Park. "이미지 기반 가상 착용 이미지 합성 기술 동향 (A survey of Image-based Virtual Try-on Technology)". *전자통신동향분석 (ETRI Electronics and Telecommunications Trends); Vol 39,No 3,pp. 107-115 (누리집 분류: Domestic Journal; 누리집 기재 날짜: 2024.05.09)*.
- Jihoon Cho Hyungjoon Bae Xiaofeng Liu Fangxu Xing Kyungeun Lee Georges Elfakhri Van Wedeen Jonghye Woo Jinah Park. "3D Segmentation of Subcortical Brain Structure with Few Labeled Data using 2D Diffusion Models". *ISMRM 2024 (누리집 분류: International Conference; 누리집 기재 날짜: 2024.05.09)*.
- Jihoon Cho Xiaofeng Liu Fangxu Xing Jinsong Ouyang Georges El Fakhri Jinah Park Jonghye Woo. "A Unified Approach for Synthesizing Multimodal Brain MR Images via Gated Hybrid Fusion". *ISMRM 2024 (누리집 분류: International Conference; 누리집 기재 날짜: 2024.05.06)*.
- Wonjung Park Hyunsoo Kim Jinah Park. "Data-driven Viscosity Solver for Fluid Simulation". *GRAPP 2024 (누리집 분류: International Conference; 누리집 기재 날짜: 2024.02.27)*.
- Jihoon Cho Xiaofeng Liu Fangxu Xing Jinsong Ouyang Georges El Fakhri Jinah Park Jonghye Woo. "Disentangled multimodal brain MR image translation via transformer-based modality infuser". *SPIE Medical Imaging: Image Processing (누리집 분류: International Conference; 누리집 기재 날짜: 2024.02.19)*.
- Hyunsoo Kim Jinah Park. "Vertebral segmentation without training using differentiable appearance modeling of a deformable spine template". *SPIE Medical Imaging: Image Processing (누리집 분류: International Conference; 누리집 기재 날짜: 2024.02.19)*.

**2023**

- Taeyoon Woo Wonjung Park Woohyun Jung Jinah Park. "A survey of deep learning methods and datasets for hand pose estimation from hand-object interaction images". *Computers and Graphics(Pergamon); Vol 116,pp. 474 - 490 (누리집 분류: International Journal; 누리집 기재 날짜: 2023.11)*.
- Soonchan Park Jinah Park. "Position Puzzle Network and Augmentation: localizing human keypoints beyond the bounding box". *Machine Vision and Applications (누리집 분류: International Journal; 누리집 기재 날짜: 2023.10.23)*.
- Wang Sik Lee Inha Kang Sung-Jin Yoon Hyunjung Kim Yugyeong Sim Youngjun Park Jinah Park Jinyoung Jeong. "Three-dimensional label-free visualization of the interactions of PM2. 5 with macrophages and epithelial cells using optical diffraction tomography". *Journal of Hazardous Materials; Vol 456,pp. 131678 (누리집 분류: International Journal; 누리집 기재 날짜: 2023.08)*.
- Jihoon Cho Inha Kang Jinah Park et. al. "Why Is the Winner the Best?". *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR); pp. 19955-19966 (누리집 분류: International Journal; 누리집 기재 날짜: 2023.06)*.
- Marc Aubreville Nikolas Stathonikos Christof A. Bertram Robert Klopfleisch Youjin Chung Jinah Park et al. "Mitosis domain generalization in histopathology images: The MIDOG challenge". *Medical Image Analysis; Vol. 84,pp. 102699 (누리집 분류: International Journal; 누리집 기재 날짜: 2023.02)*.

**2022**

- Wonjung Park Yujin Chung Soonchan Park Jinah Park. "VACS: 패션 객체 영역 분할 기법을 통한 가상 착용 기술 아티팩트 보정 시스템". *Journal of KIISE; Vol 49,No 10,pp. 802-806 (누리집 분류: Domestic Journal; 누리집 기재 날짜: 2022.10)*.
- Chanhyeok Lee Jinah Park. "볼륨 데이터 상호작용을 위한 점구름 생성 및 처리의 GPU 기반 가속화 방법". *2022 한국컴퓨터종합학술대회 (KCC2022); pp. 1504 - 1506 (누리집 분류: Domestic Conference; 누리집 기재 날짜: 2022.06.29)*.
- Taeyoon Woo Wonjung Park Hyunsoo Kim Jinah Park. "원자로 해체 공정작업 가상훈련을 위한 3D 모델 절단 및 평가 시스템". *2022 한국컴퓨터종합학술대회 (KCC2022); pp. 1507 - 1509 (누리집 분류: Domestic Conference; 누리집 기재 날짜: 2022.06.29)*.
- Youjin Chung Jihoon Cho Jinah Park. "Domain-Robust Mitotic Figure Detection with Style Transfer". *Biomedical Image Registration, Domain Generalisation and Out-of-Distribution Analysis.; pp. 23-31 (누리집 분류: International Journal; 누리집 기재 날짜: 2022.03.02)*.
- Minyoung Park Jinah Park. "Domain Transformation for PMMA-Inserted Vertebral Body Segmentation". *Journal of Computing Science and Engineering; Vol 16,No 1,pp. 43-51 (누리집 분류: Domestic Journal; 누리집 기재 날짜: 2022.03)*.
- Hyunsoo Kim Wonjung Park Taeyoon Woo Jinah Park. "Haptic Guidance for Robot Arm Teleoperation using Ray-based Holistic Collision Avoidance". *AsiaHaptics 2022 (누리집 분류: International Conference; 누리집 기재 날짜: 2022.11.12)*.
- Jaehyun Jang William Frier Jinah Park. "Multimodal Volume Data Exploration through Mid-Air Haptics". *2022 IEEE International Symposium on Mixed and Augmented Reality (ISMAR) (누리집 분류: International Conference; 누리집 기재 날짜: 2022.10.20)*.

**2021**

- Joowon Lim Jinah Park. "Interpolation Method for CT Image Reconstruction using Features Inferred by Self-Supervised Learning (자기지도학습으로 추론된 특징을 이용한 CT 영상의 보간 방법)". *Journal of KIISE (정보과학회논문지); Vol 48,No 9,pp. 1007-1013 (누리집 분류: Domestic Journal; 누리집 기재 날짜: 2021.09.15)*.
- Soonchan Park Jinah Park. "Localizing Human Keypoints beyond the Bounding Box". *Preceedings of the IEEE International Conference on Computer Vision(ICCV) Workshops 2021 (누리집 분류: International Conference; 누리집 기재 날짜: 2021.08.12)*.
- Joong-Youn Lee Jinah Park. "Deep Regression Network-Assisted Efficient Streamline Generation Method". *IEEE ACCESS (누리집 분류: International Conference; 누리집 기재 날짜: 2021.07.26)*.
- Jaehyun Jang Jinah Park. "Interacting with Fluids Using Ultrasonic Mid-Air Haptic Device". *IEEE World Haptics Conference 2021 (Demo) (누리집 분류: International Conference; 누리집 기재 날짜: 2021.07.08)*.
- Jaehyun Jang William Frier Orestis Georgiou Jinah Park. "Using Mid-Air Tactile Patterns in Interactive Volume Exploration". *IEEE World Haptics Conference 2021 (Demo) (누리집 분류: International Conference; 누리집 기재 날짜: 2021.07.08)*.
- Wonjung Park Youjin Chung Soonchan Park Jinah Park. "VACS: 패션 객체 영역 분할 기법을 통한 가상 착용 기술 아티팩트 보정 시스템". *한국컴퓨터종합학술대회; pp. 691-693 (누리집 분류: Domestic Conference; 누리집 기재 날짜: 2021.06.01)*.
- Jaehyun Jang Joowon Lim Jinah Park. "Real-time volume exploration technique for holographic display". *Proceedings Volume 11792, International Forum on Medical Imaging in Asia 2021; Vol 11792,pp. 1-6 (누리집 분류: International Conference; 누리집 기재 날짜: 2021.04.20)*.

## 특허

연구실 게시 날짜가 2021년 10월 13일–2026년 10월 13일에 드는 특허 기록 5건이다. 아래 날짜는 누리집 기재 날짜이며, 출원일·등록일로 별도 표기하지 않은 날짜의 법적 의미를 추정하지 않았다.[^patents]

- 2024.12.03 · Method for object interaction in extened reality, device for performing the same, and extended reality display system including the device (발명자 Chanhyeok Lee Jinah Park; 출원번호 18/966,279)
- 2024.10.22 · Method for visualizing cutting path in simulation apparatus and simulation device for performing the same (발명자 Taeyun Woo Jinah Park; 출원번호 18/922,567)
- 2024.07.24 · 가상 유체와의 상호작용에 기반한 촉각 피드백 제공 방법 및 이를 수행하는 장치 (발명자 Jaehyun Jang Jinah Park; 출원번호 10-2021-0176503,; 등록번호 10-2689320)
- 2023.08.10 · 관심 물질 및 경계면 강조를 위한 전이 함수를 제어하는 사용자 인터페이스 제공 방법 및 장치 (발명자 Joowon Lim Jinah Park; 출원번호 10-2020-0179596,; 등록번호 10-2567428)
- 2023.03.23 · 볼륨 데이터 상호작용에 대한 촉각 피드백 제공 방법 및 장치 (발명자 Jaehyun Jang Jinah Park; 출원번호 10-2021-0078848,; 등록번호 10-2514713)

## 수상과 선정

2022년 9월–2026년 9월의 수상·경진대회 성과 13건이다. 날짜는 연구실 소식의 게시 날짜다.

- 2026-09-05 · Suhyun Ahn이 MICCAI 2026 FOMO Challenge Open Track 전체 과제에서 종합 1위를 했다.[^news26]
- 2026-09-05 · Hyunjun Park이 MICCAI 2026 VLM3D Challenge CT Abnormality Classification 과제에서 3위를 했다.[^news26]
- 2026-09-05 · Hyunjun Park이 MICCAI 2026 VLM3D Challenge CT Report Generation 과제에서 3위를 했다.[^news26]
- 2026-09-05 · Woojin Na가 MICCAI 2026 VLM3D Challenge MR Volume Generation 과제에서 2위를 했다.[^news26]
- 2026-09-05 · Woojin Na가 MICCAI 2026 VLM3D Challenge CT Volume Generation 과제에서 1위를 했다.[^news26]
- 2026-07-03 · Hyunsoo Kim이 「Neural Particle Automata」로 KCGS 2026 우수논문상 대상을 받았다.[^news26]
- 2025-07-15 · Suhyun Ahn·Wonjung Park·박진아의 「Are Medical Image Generative Models Biologically Trustworthy?」가 BISCUIT@ICCVW 2025 Best Paper로 선정됐다고 연구실이 알렸다.[^news25]
- 2024-10-16 · Jihoon Cho·Seunghyuck Park·박진아 팀이 MICCAI Brasyn Challenge 2024에서 1위를 했다.[^news24]
- 2024-07-06 · Wonjung Park·Suhyun Ahn·박진아의 측뇌실 주변 영역 투영 기반 모델링 포스터가 KSIIM 2024 최우수 포스터상을 받았다.[^news24]
- 2024-04-22 · 박진아 교수가 과학기술포장을 받았다고 연구실이 알렸다.[^news24][^faculty]
- 2023-11-24 · Gyuna Lim·박진아의 「실시간 상호작용이 가능한 스타일러스 기반 고점성 유체 햅틱 렌더링」 포스터가 KHC 2024 Best Poster를 받았다고 연구실이 알렸다.[^news23]
- 2022-11-14 · Hyunsoo Kim·Wonjung Park·Taeyoon Woo·박진아 팀의 로봇 팔 햅틱 안내 연구가 AsiaHaptics 2022 Best Demo Award 최종 후보로 선정됐다.[^news22]
- 2022-09-22 · Inha Kang·Jihoon Cho·박진아 팀이 MICCAI MOOD Challenge 2022 Pixel-level 부문에서 공동 1위를 했다.[^news22]

## 소식

2022년 1월 13일–2026년 10월 12일의 논문 채택·발표·인터뷰·전시·학술 행사 소식 33건이다. 날짜는 연구실 소식이 적은 날짜다.

- 2026-10-12 · Jewoo Shin·박진아의 연성 물체 시뮬레이션 연구를 소개한 인터뷰가 80 Level에 실렸다.[^news26]
- 2026-09-09 · 「Unified Haptic Rendering of Deformable Objects with an XPBD Particle Framework」가 AsiaHaptics 2026에 채택됐다.[^news26]
- 2026-08-28 · 「3D Brain Shape Modeling for Neuroanatomical Analysis and Longitudinal Prediction」가 MICCAI 2026 Doctoral Symposium의 Spotlight 발표로 채택됐다.[^news26]
- 2026-06-25 · 뇌 영상 처리를 주제로 Maria del C. Valdés Hernández의 세미나를 열었다.[^news26]
- 2026-06-21 · 박진아 교수가 Canada-Korea Conference on Science and Technology 2026에서 한국의 AI 전환을 주제로 강연했다.[^news26]
- 2026-06-15 · 자기공명영상의 응용을 주제로 Neil Roberts의 세미나를 열었다.[^news26]
- 2026-05-25 · 「OmniBody: Discretized Local Constraints for Real-Time Destructible and Flexible Soft Bodies Simulation」가 SIGGRAPH 2026 Poster에 채택됐다.[^news26]
- 2026-03-31 · 「Neural Particle Automata: Learning Self-Organizing Particle Dynamics」가 SIGGRAPH 2026에 채택됐다.[^news26]
- 2026-02-03 · Shape-Guided Self-Supervised Learning for Intracranial Aneurysm Segmentation이 ISBI 2026에 채택됐다.[^news26]
- 2026-01-29 · 「Vibration–Color–Emotion Correspondences for Affective Haptic Feedback」가 Haptics Symposium 2026에 채택됐다.[^news26]
- 2026-01-26 · 의료 영상 인공지능의 평가·합성·분석을 다루는 세미나 일정을 공지했다.[^news26]
- 2026-01-10 · Adaptability of Vision Foundation Models for 3D Medical Image Segmentation이 IEEE Open Journal of Signal Processing에 게재 승인됐다.[^news26]
- 2025-09-19 · 「BrainODE: Neural Shape Dynamics for Age- and Disease-aware Brain Trajectories」가 NeurIPS 2025에 채택됐다.[^news25]
- 2025-08-09 · Hyunsoo Kim이 SIGGRAPH 2025에서 「Trained Once, Generate Anywhere: Discretization Agnostic Neural Cellular Automata Using SPH Method」 포스터를 발표했다.[^news25]
- 2025-07-12 · 연구실이 KSIIM 2025에서 연구 성과를 발표했다.[^news25]
- 2025-07-08 · 연구실이 World Haptics 2025에서 연구 성과를 발표했다.[^news25]
- 2025-04-15 · AI-based deformable hippocampal mesh reflects hippocampal morphological characteristics in relation to cognition in healthy older adults가 NeuroImage에 게재 승인됐다.[^news25]
- 2024-10-28 · 「Volumetric Conditioning Module to Control Pretrained Diffusion Models for 3D Medical Images」가 WACV 2025에 채택됐다.[^news24]
- 2024-05-09 · Jihoon Cho가 ISMRM 2024에서 연구 두 편을 발표했다.[^news24]
- 2024-04-09 · Gyuna Lim이 IEEE Haptics Symposium 2024에서 공중 햅틱으로 변형 가능한 선형 물체를 조작하는 방법의 포스터를 발표했다.[^news24]
- 2024-02-27 · Wonjung Park이 GRAPP 2024에서 「Data-driven Viscosity Solver for Fluid Simulation」을 발표했다.[^news24]
- 2024-02-18 · Hyunsoo Kim이 SPIE Medical Imaging 2024에서 학습 자료 없이 척추를 분할하는 변형 모형 연구를 발표했다.[^news24]
- 2024-02-18 · Jihoon Cho가 SPIE Medical Imaging 2024에서 Modality Infuser 기반 다중 MR 영상 변환 연구를 발표했다.[^news24]
- 2024-02-05 · Tomocube의 Taeho Kim이 볼륨 렌더링을 주제로 세미나를 했다.[^news24]
- 2023-09-19 · Samsung Medison의 Hojin Ryoo가 측뇌실을 주제로 세미나를 했다.[^news23]
- 2023-06-22 · 미세먼지와 세포의 상호작용을 삼차원으로 관측하는 연구가 언론에 소개됐다고 연구실이 알렸다.[^news23]
- 2023-05-26 · 호서대학교 Jungdo Kim 교수의 강연을 포함한 후각 장치 워크숍을 열었다.[^news23]
- 2023-04-20 · 박진아 교수가 PacificVis 2023에서 변형 모델링과 햅틱 렌더링을 통한 자료 시각화를 주제로 기조강연을 했다.[^news23]
- 2023-04-20 · Beomju Kim·Suhyun Ahn·박진아가 PacificVis 2023 포스터 세션에서 「Revealing Zebrafish Gut Motility Patterns through STMap Extraction and Customized Warping Techniques」를 발표했다.[^news23]
- 2022-11-11 · CGV 팀이 AsiaHaptics 2022에서 로봇 팔 원격 조작용 햅틱 안내 연구를 시연했다.[^news22]
- 2022-10-28 · Jihoon Cho가 막수포럼에서 의료 영상 이상 검출의 이차원·삼차원 신경망 공동 표현을 주제로 발표했다.[^news22]
- 2022-06-30 · Jaehyun의 연구가 N1에 전시됐다고 연구실이 알렸다.[^news22]
- 2022-01-13 · 오타와대학교 Wonsook Lee 교수의 세미나를 열었다.[^news22]

## 연락과 위치

- 교수연구실: KAIST 전산학부 건물 E3-1, 2404호[^faculty][^professor]
- 학생 연구 공간: E3-1, 2413호[^students]
- 주소: 대전광역시 유성구 대학로 291, KAIST, 우편번호 34141[^professor]
- 연구실 전화: +82-(0)42-350-7755[^members]
- 교수 전화: +82-(0)42-350-3555[^professor]

## 각주
[^news22]: 연구실 News in 2022. <https://cgv.kaist.ac.kr/news/2022> (관측 2026-10-27).
[^news23]: 연구실 News in 2023. <https://cgv.kaist.ac.kr/news/2023> (관측 2026-10-27).
[^news24]: 연구실 News in 2024. <https://cgv.kaist.ac.kr/news/2024> (관측 2026-10-27).
[^research]: 연구실 Research. 의료 영상 분석·모델링, 컴퓨터 햅틱스와 가상현실, 시뮬레이션·시각화 연구 설명. <https://cgv.kaist.ac.kr/research> (관측 2026-10-26).
[^professor]: 연구실 Professor. Jinah Park의 직위·학력·연구 관심·위치·연락처. <https://cgv.kaist.ac.kr/members/professor> (관측 2026-10-26).
[^faculty]: KAIST 전산학부 박진아 교수 소개. 국문 연구실명·직위·전공·학력·수상. <https://cs.kaist.ac.kr/people/view?idx=370&kind=faculty&menu=160> (관측 2026-10-27).
[^metalab]: 메타버스대학원 CGV 참여 연구실 소개. <https://meta.kaist.ac.kr/labs/cgv-lab> (관측 2026-10-27).
[^metaprof]: 메타버스대학원 교수진. 박진아, Full-time, 전산학부 표기. <https://meta.kaist.ac.kr/professors/> (관측 2026-10-27).
[^medical]: 연구실 삼차원 의료 영상 생성·분할 연구 소개. <https://cgv.kaist.ac.kr/research/foundation_models_3d_medical_imaging/> (관측 2026-10-27).
[^members]: 연구실 Members. 박사과정·석사과정 학생 명단. <https://cgv.kaist.ac.kr/members> (관측 2026-10-26).
[^alumni]: 연구실 Alumni. 박사·석사 졸업생 명단과 게시 진로. <https://cgv.kaist.ac.kr/allumni> (관측 2026-10-26).
[^news26]: 연구실 News in 2026. 날짜는 소식 게시 날짜. <https://cgv.kaist.ac.kr/news/2026> (관측 2026-10-26).
[^news25]: 연구실 News in 2025. 날짜는 소식 게시 날짜. <http://cgv.kaist.ac.kr/news/2025/> (관측 2026-10-27).
[^patents]: 연구실 Patent 분류 목록. 게시 날짜·출원번호·등록번호·발명자. <https://cgv.kaist.ac.kr/publication/tags/patent/> (관측 2026-10-27).
[^students]: 연구실 학생 개별 소개의 연구 관심과 연구 공간. <https://cgv.kaist.ac.kr/members/soohyunahn/> <https://cgv.kaist.ac.kr/members/hyunsookim/> <https://cgv.kaist.ac.kr/members/chanhyeoklee/> <https://cgv.kaist.ac.kr/members/jihwanpark/> <https://cgv.kaist.ac.kr/members/eunhyechoi/> <https://cgv.kaist.ac.kr/members/jewooshin/> <https://cgv.kaist.ac.kr/members/woojinna/> <https://cgv.kaist.ac.kr/members/hyunjunpark/> <https://cgv.kaist.ac.kr/members/hyeokjaecho/> (관측 2026-10-27).
[^publications]: 연구실 Publication 전체 목록과 분류별 목록. <https://cgv.kaist.ac.kr/publication> <https://cgv.kaist.ac.kr/publication/2/> <https://cgv.kaist.ac.kr/publication/3/> <https://cgv.kaist.ac.kr/publication/4/> <https://cgv.kaist.ac.kr/publication/5/> <https://cgv.kaist.ac.kr/publication/6/> <https://cgv.kaist.ac.kr/publication/tags/international_journal/> <https://cgv.kaist.ac.kr/publication/tags/international_conference/3/> (첫 쪽 관측 2026-10-26, 나머지 2026-10-27).
[^p1]: H. Kim 외, J. Park, SIGGRAPH 2026 (채택) (2026). <https://cgv.kaist.ac.kr/research/neural_particle_automata/> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://cgv.kaist.ac.kr/research/neural_particle_automata/> (관측 2026-10-27).
[^p2]: W. Park 외, J. Park, Advances in Neural Information Processing Systems 38 (2025). <https://doi.org/10.52202/085713-3954> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://papers.nips.cc/paper_files/paper/2025/hash/abdc8c031aa6c6917c3b593166e5e340-Abstract-Conference.html> (관측 2026-10-27).
[^p3]: S. Ahn 외, J. Park, arXiv:2410.21826 (WACV 2025 관련 판) (2025). <https://arxiv.org/abs/2410.21826> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.21826> (관측 2026-10-27).
[^p4]: W. Park, S. Ahn, J. Park, arXiv:2410.07148 (MIUA 2024 관련 판) (2024). <https://arxiv.org/abs/2410.07148> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.07148> (관측 2026-10-27).
[^p5]: W. Park, H. Kim, J. Park, arXiv:2409.14653 (GRAPP 2024 관련 판) (2024). <https://arxiv.org/abs/2409.14653> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.14653> (관측 2026-10-27).
[^p6]: T. Woo, T.-K. Kim, J. Park, arXiv:2409.17629 (ICIP 2024 채택 판) (2024). <https://arxiv.org/abs/2409.17629> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2409.17629> (관측 2026-10-27).
[^p7]: G. Lim, A. Vo, J. Park, 2025 IEEE World Haptics Conference (WHC) (2025). <https://doi.org/10.1109/WHC64065.2025.11123390> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/978-3-030-97281-3_15|10.1016/j.bspc.2026.109712|10.1016/j.jhazmat.2023.131678|10.1016/j.neuroimage.2025.121145|10.1109/haptics66823.2026.11495492|10.1109/iccvw69036.2025.00072|10.1109/isbi60581.2025.10981074|10.1109/isbi61048.2026.11515789|10.1109/ojsp.2025.3650437|10.1109/whc64065.2025.11123390|10.1117/12.2590772|10.1117/12.3006602|10.1117/12.3006895|10.14245/ns.2346536.268|10.5626/jcse.2022.16.1.43|10.5626/jok.2021.48.9.1007|10.58530/2024/1397|10.58530/2024/2242> (관측 2026-10-27).
[^p8]: A. Vo, C. Lee, J. Park, 2026 IEEE Haptics Symposium (HAPTICS) (2026). <https://doi.org/10.1109/HAPTICS66823.2026.11495492> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/978-3-030-97281-3_15|10.1016/j.bspc.2026.109712|10.1016/j.jhazmat.2023.131678|10.1016/j.neuroimage.2025.121145|10.1109/haptics66823.2026.11495492|10.1109/iccvw69036.2025.00072|10.1109/isbi60581.2025.10981074|10.1109/isbi61048.2026.11515789|10.1109/ojsp.2025.3650437|10.1109/whc64065.2025.11123390|10.1117/12.2590772|10.1117/12.3006602|10.1117/12.3006895|10.14245/ns.2346536.268|10.5626/jcse.2022.16.1.43|10.5626/jok.2021.48.9.1007|10.58530/2024/1397|10.58530/2024/2242> (관측 2026-10-27).

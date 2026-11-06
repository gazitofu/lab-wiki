# BIOINSPIRED EMBODIED INTELLIGENCE ROBOTICS LABORATORY

**서울대학교 공과대학 기계공학부 · 조규진 교수**

- 영문 이름: SNU Biorobotics Lab.
- 분야: 생물 모방 로봇, 소프트 로봇, 착용형 보조 로봇, 전개형 로봇[^overview][^dept]
- 대분야: 기계·로봇·제조
- 태그: 착용형 로봇·외골격[^wear], 재활·보조·접근성 기술[^wear], 소프트 로보틱스[^soft], 로봇 조작·파지[^soft], 로봇 구동기·센서[^soft], 3D 프린팅[^soft], 전개형 구조물·종이접기 공학[^deploy]
- 홈페이지: <https://www.biorobotics.snu.ac.kr/>
- 근거와 출처: [BIOINSPIRED EMBODIED INTELLIGENCE ROBOTICS LABORATORY 근거 페이지](biorobotics-sources.md)

> 생물의 움직임과 몸 구조에서 설계 원리를 찾아, 사람의 동작을 돕는 착용형 로봇과 환경에 맞춰 움직이고 접히는 로봇을 만드는 연구실이다.

## 무엇을 연구하나

생물의 운동 원리를 로봇의 구조와 움직임 생성 방법으로 옮긴다. 소프트 로봇(부드럽고 잘 휘는 재료로 몸체와 움직이는 부분을 만든 로봇), 새로운 제조 방법, 구동기(공급받은 에너지를 힘과 움직임으로 바꾸는 장치)를 결합하는 것이 공통 방향이다. 연구는 착용형 로봇·의수, 생물 모방 이동 로봇, 소프트 로봇, 전개형 로봇으로 나뉜다.[^overview]

착용형 로봇에서는 손과 팔의 동작, 물건 운반, 호흡 등을 돕는 구조를 설계한다. 일상생활 보조와 재활뿐 아니라 운동 기능의 증강과 부상 예방도 목표로 삼는다. 자연과 인체의 힘 전달 원리를 참고해 기구와 제어 시스템을 만들고, 몸에 닿는 방식 및 사용자의 의도를 전달하는 방식에서 안전성과 편안함을 함께 다룬다.[^wear]

이동 로봇은 뛰기·기어가기·미끄러져 날기·오르기를 구현하고, 서로 다른 이동 방식을 한 로봇에 통합한다. 전개형 로봇은 보관할 때 접거나 말아 부피를 줄이고, 사용할 때 펼쳐 힘을 지지하도록 만든다. 소프트 로봇에서는 딱딱한 관절과 연결 막대에만 의존하지 않는 움직임과 그리퍼(물체를 붙잡는 로봇의 끝장치)를 개발한다.[^bio][^deploy][^soft]

## 주요 연구 주제

### 착용형 손 로봇·의수와 호흡 보조

손에 착용하는 로봇에서는 텐던(당기는 힘을 전달하는 줄)으로 손가락을 움직이고, 적은 수의 구동기로 여러 관절을 다루는 구조를 연구한다. 대표 논문 1은 줄마다 처음의 늘어진 길이를 다르게 해 엄지와 다른 손가락의 움직임 순서를 나누고, 한 구동기로 두 가지 잡기 방식을 보조하는 Exo-Glove Poly III를 제안했다.[^p1] 연구실은 의수의 관절과 구동 구조도 설계하며, 사용자가 일상생활과 스포츠에 참여하도록 돕는 것을 목표로 한다.[^wear]

호흡 보조에서는 복부에 압박을 가해 숨쉬기·기침·말하기를 돕는 착용형 로봇을 개발한다. 대표 논문 2의 Exo-Abs는 사용자의 자발적인 호흡 노력에 맞춰 압박을 전달하도록 설계되었으며, 세 호흡 기능을 보조하는 성능을 보였다.[^p2]

### 생물 모방 이동과 복합 이동

동물의 이동 방식을 연구해 크기가 작은 로봇이 정돈되지 않은 지형을 통과하도록 설계한다. 뛰기와 기어가기 등을 결합해 한 이동 방식만 사용할 때의 활동 범위를 넓히려 한다.[^bio] 대표 논문 3은 도약을 위한 에너지 저장과 다리를 웅크리는 동작을 분리했다. 클러치(힘과 운동의 전달 경로를 연결하거나 끊는 장치)가 둘 사이의 연결을 바꾸도록 해 도약 높이 조절과 이동 방식 전환을 구현했다.[^p3]

### 소프트 관절·그리퍼와 재료 출력 방법

연구실은 유연한 재료와 제조 방법을 이용해 소프트 관절, 구동기, 물체를 붙잡고 다루는 장치를 개발한다.[^soft] 3D 프린팅(재료를 층층이 쌓아 입체 물체를 만드는 제조 방법)의 출력 조건으로, 재료가 미리 정한 모양으로 돌아올 때의 변형량을 연속적으로 정하는 방법도 연구한다.[^soft]

대표 논문 4는 잘 늘어났다가 회복되는 재료를 이용해 소프트 관절에서 토크(물체를 회전시키는 힘의 효과)의 방향이 바뀌는 메커니즘을 구현했다. 압축 조건에 따라 일시적으로 두 안정 상태가 나타나는 성질을 이용해 에너지 저장·방출과 급격한 움직임을 탐구했다.[^p4] 대표 논문 5의 MOGrip은 손가락으로 잡은 물체를 손바닥 쪽에 저장하고 다시 하나씩 꺼내 놓는다. 대표 논문 6은 서로 다른 재료로 출력한 필라멘트(재료를 공급하는 가는 줄)를 프린터에 다시 넣어, 출력물 내부에서 힘을 버티는 성질과 전기가 흐르는 정도, 색을 위치에 따라 설계하는 방법을 제안했다.[^p5][^p6]

### 접히고 말리는 전개형 구조

종이접기 구조를 이용해 접었을 때의 휴대성과 펼쳤을 때의 기능을 함께 확보한다. 연구실은 큰 하중(구조물에 외부에서 가해지는 힘)을 버티는 전개형 기계를 목표로 구조를 설계하고 크기를 키우는 방향을 제시한다.[^deploy] 대표 논문 7은 띠들을 엇갈려 연결해 접고 말 수 있으면서도 펼친 상태에서 하중을 지지하는 구조를 만들었다.[^p7] 대표 논문 8은 접힘선의 강성(힘을 받았을 때 변형에 저항하는 정도)을 조절하는 단위 부품을 결합해, 하중을 지지하면서 펼쳐지는 소프트 로봇을 제안하고 로봇 팔과 텐트 골조에 적용했다.[^p8]

## 대표 논문

서울대 재직 시기의 논문 가운데 착용형 보조, 이동 로봇, 소프트 관절·파지, 제조 방법, 전개형 구조를 고르게 다루도록 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸의 마지막 저자는 저자 순서를 뜻한다.

| 번호 | 연도 | 논문 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2025 | [Exo-Glove Poly III: Grasp Assistance by Modulating Thumb and Finger Motion Sequence with a Single Actuator](https://doi.org/10.1089/soro.2024.0113)[^p1] | 1저자 Kyu Bum Kim, 마지막 저자 Kyu‐Jin Cho | 줄마다 처음 늘어진 길이를 다르게 해 엄지와 다른 손가락의 움직임 순서를 나누는 착용형 손 로봇이다. 한 구동기로 두 가지 잡기 방식을 보조하며, 장치의 동작을 확인했다. |
| 2 | 2022 | [Exo-Abs: A Wearable Robotic System Inspired by Human Abdominal Muscles for Noninvasive and Effort-Synchronized Respiratory Assistance](https://doi.org/10.1109/tro.2022.3167399)[^p2] | 1저자 Sang-Yoep Lee, 마지막 저자 Kyu‐Jin Cho | 사용자의 자발적인 호흡 노력에 맞춰 복부를 압박하는 착용형 로봇이다. 숨쉬기뿐 아니라 기침과 말하기를 보조하도록 플랫폼을 설계하고 세 기능의 보조 성능을 보였다. |
| 3 | 2022 | [Agile and Energy-Efficient Jumping–Crawling Robot Through Rapid Transition of Locomotion and Enhanced Jumping Height Adjustment](https://doi.org/10.1109/tmech.2022.3190673)[^p3] | 1저자 Soo-Hwan Chae, 마지막 저자 Kyu‐Jin Cho | 뛰기 위한 에너지 저장과 다리를 웅크리는 동작 사이의 연결을 클러치로 전환한다. 이를 통해 도약 높이를 조절하고 뛰기와 기어가기 사이의 전환을 빠르게 하는 로봇을 제시했다. |
| 4 | 2025 | [A hyperelastic torque-reversal mechanism for soft joints with compression-responsive transient bistability](https://doi.org/10.1126/scirobotics.ado7696)[^p4] | 1저자 Woo-Young Choi, 마지막 저자 Kyu-Jin Cho | 잘 늘어났다가 회복되는 재료로 회전력 방향이 바뀌는 소프트 관절을 만들었다. 압축 조건에 따라 나타났다 사라지는 두 안정 상태를 이용해 에너지 저장·방출과 급격한 움직임을 구현하는 원리를 제시했다. |
| 5 | 2024 | [MOGrip: Gripper for multiobject grasping in pick-and-place tasks using translational movements of fingers](https://doi.org/10.1126/scirobotics.ado3939)[^p5] | 1저자 Jaemin Eom, 마지막 저자 Kyu-Jin Cho | 네 손가락이 물체를 손바닥으로 보내 여러 개를 저장하고, 거꾸로 동작하면 저장한 물체를 하나씩 꺼내 놓는다. 손가락의 물체 이동과 손바닥의 저장 기능을 결합해 집고 놓는 작업을 수행했다. |
| 6 | 2024 | [3D printing with a 3D printed digital material filament for programming functional gradients](https://doi.org/10.1038/s41467-024-47480-5)[^p6] | 1저자 Sang‐Joon Ahn, 마지막 저자 Kyu‐Jin Cho | 서로 다른 기본 재료의 농도와 배치를 정해 재료 줄을 먼저 출력한 뒤, 같은 프린터에서 그 줄을 다시 녹여 물체를 만든다. 이 방법으로 물체 안의 강도와 전기가 흐르는 정도, 색을 위치별로 정한다. |
| 7 | 2025 | [Foldable and rollable interlaced structure for deployable robotic systems](https://doi.org/10.1126/scirobotics.adv4696)[^p7] | 1저자 Sun-Pill Jung, 마지막 저자 Kyu‐Jin Cho | 여러 띠를 엇갈려 연결해 펼치면 하중을 지지하고, 접으면 층층이 쌓여 축에 감기는 구조를 제안했다. 이를 이용해 펼쳐지는 로봇 팔과 입체 프린팅 장치를 지지하는 전개형 골조를 만들었다. |
| 8 | 2026 | [3D Printed Meter‐Scale Soft Origami Robots Capable of Load‐Bearing Actuation Via Crease Stiffness Modulation](https://doi.org/10.1002/advs.77127)[^p8] | 1저자 Sung Yol Yu, 마지막 저자 Kyu‐Jin Cho | 접힘선의 강성을 단위 부품의 조립으로 조절해 펼쳐지는 동안 형태를 안정적으로 유지하는 로봇 구동기를 제안했다. 미터 크기의 로봇 팔과 자동으로 펼치고 접히는 텐트 골조에 적용했다. |

## 교수와 전문 분야

조규진 교수는 서울대학교 공학사(1998)·공학석사(2000), MIT 공학박사(2007) 학위를 받았다. 학과 경력은 서울대학교 기계공학부의 2008–2017년 부교수와 2018년 이후 교수로 적고 있다. 학과 소개에는 학부장과 인간중심소프트로봇연구센터장 보직도 기재되어 있다.[^dept]

공식 연구 분야는 생체모사로봇, 소프트 로봇, 소프트 웨어러블 로봇, 재활·보조 로봇이다.[^dept] 최근 논문은 사람에게 힘을 전달하는 로봇 구조, 생물 모방 이동 기구, 유연한 관절과 파지 장치, 접이식 구조의 저장 방식과 하중 지지를 다룬다. 이들 논문에서 조규진 교수는 마지막 저자로 참여했다.[^p1][^p2][^p3][^p4][^p5][^p7][^p8]

## 응용 분야

연구실이 제시하는 응용은 손·팔 동작과 호흡의 보조, 재활, 운동 활동, 부상 예방, 구조·재난 현장의 이동 로봇이다. 접이식 구조는 휴대가 가능한 로봇 팔과 큰 하중을 다루는 구조물로 연결한다.[^wear][^bio][^deploy] 대표 논문에서는 여러 물체를 함께 옮기고 하나씩 놓는 작업, 물체 내부의 성질을 위치에 따라 정하는 출력 방법도 다룬다.[^p5][^p6]

## 구성원

2026년 11월 6일 관측한 현재 구성원은 박사후연구원 2명, 박사과정 16명, 석사과정 14명이다. 과정·연구 주제·학교 이메일은 랩의 게시 표기를 따른다. ‘대표 논문 참여’는 위 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^postdoc][^phd][^ms]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Sojung Yim (임소정) | 박사후연구원 | Bio-inspired robots |  |  |
| Hye Ju Yoo (유혜주) | 박사후연구원 | Wearable Robots, Biomedical Robotics, Soft Actuators | hyoo1@snu.ac.kr |  |
| Yongmin Park (박용민) | 박사과정 | Origami Inspired Robots | pym2437@snu.ac.kr |  |
| Pilwoo Lee (이필우) | 박사과정 | Bio-inspired Robots |  |  |
| Dohyeon Pyeon (편도현) | 박사과정 | Soft Robots, Tendon-driven Robots | pdh4693@snu.ac.kr |  |
| Jungmin Ahn (안정민) | 박사과정 | Wearable Robots |  |  |
| Seunghyun An (안승현) | 박사과정 | Bio-inspired Robots |  |  |
| Jong Min Kim (김종민) | 박사과정 | Origami Inspired Robots | kjmin1118@snu.ac.kr |  |
| Chan Kim (김찬) | 박사과정 | Origami Inspired Robots | iopn1213@snu.ac.kr | 7 |
| Wonseok Choi (최원석) | 박사과정 | Wearable Robots |  |  |
| Wonkyeong Kang (강원경) | 박사과정 | Soft Robotics | wk000106@snu.ac.kr |  |
| Bada Seo (서바다) | 박사과정 | Wearable Robots |  |  |
| Guyeol Jeong (정구열) | 박사과정 | Wearable Robots | kuyul@snu.ac.kr |  |
| In-chul Jeong (정인철) | 박사과정 | Wearable Robots | dlscjf410@snu.ac.kr |  |
| Ji-sang Kang (강지상) | 박사과정 | Wearable Robots | j.s.kang@snu.ac.kr |  |
| Wonchul Lee (이원철) | 박사과정 | Soft Robotics | wonchull@snu.ac.kr | 8 |
| Seunguk Moon (문승욱) | 박사과정 | Soft Robotics | dnr0412@snu.ac.kr | 4, 8 |
| Seungwon Yang (양승원) | 박사과정 | Wearable Robotics, AI-Based System Modeling | swyang15@snu.ac.kr |  |
| Haseon Kim (김하선) | 석사과정 | Origami Inspired Robots | haseonalex@snu.ac.kr |  |
| Sungjin Park (박성진) | 석사과정 | Wearable Robots | sjin3998@snu.ac.kr |  |
| Tae-Hyun Kim (김태현) | 석사과정 | Wearable Robots | taehyunk@snu.ac.kr |  |
| Younseo Lee (이윤서) | 석사과정 | Origami Structure, Robotic Manipulation | ys.lee@snu.ac.kr |  |
| Hyeonho Jung (정현호) | 석사과정 | Bio-inspired Robots | gusgh0513@snu.ac.kr |  |
| Haewoo Lee (이해우) | 석사과정 | Soft Robots | collin0114@snu.ac.kr |  |
| Hwang Deukkyum (황득겸) | 석사과정 | Origami Structure | emrrua@snu.ac.kr |  |
| sung wook Choi (최성욱) | 석사과정 | Robotic Manipulation | swchoi1@snu.ac.kr |  |
| SeungMin Kim (김승민) | 석사과정 | Soft Robots | fkdlqm0101@snu.ac.kr |  |
| Minseo Oh (오민서) | 석사과정 | Bio-inspired Robots |  |  |
| Seongmin Son (손성민) | 석사과정 | Bio-inspired Robots |  |  |
| Gyujin Cho (조규진) | 석사과정 | Wearable Robotics |  |  |
| Jonghan Park (박종한) | 석사과정 | Lower Body Gait Control using AI/ML | mjh03040513@snu.ac.kr |  |
| Jongsun Park (박종선) | 석사과정 | Wearable Robotics | jay887@snu.ac.kr |  |

## 졸업생·이전 구성원 진로

2026년 11월 6일 관측한 Alumni의 76명이다. 학위·과정과 진로는 누리집 게시 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yong-Jai Park (박용재) | Ph.D. | Professor of Kangwon National University(강원대학교) |
| Je-Sung Koh (고제성) | Ph.D. | Professor of Ajou University (아주대학교) |
| Hyunki In (인현기) | Ph.D. | 한국과학기술연구원 (KIST) |
| Seung-Won Kim (김승원) | Ph.D. | 한국과학기술연구원 (KIST) |
| Min-Ki Sin (신민기) | Ph.D. | KIMM |
| Gwang-Pil Jung (정광필) | Ph.D. | Professor at Seoul Nat'l Univ. of Science and Tech. (서울과학기술대학교) |
| Useok Jeong (정우석) | Ph.D. | Hyundai Motor Company (현대자동차) |
| Daegeun Park (박대근) | Ph.D. | Post-Doctoral Researcher at Istituto Italiano di Tecnologia |
| Brian Byunghyun Kang (강병현) | Ph.D. | Professor of Sejong University(세종대학교) |
| Dae-Young Lee (이대영) | Ph.D. | Professor at Korea Advanced Institute of Science and Technology (KAIST) |
| Jun-Young Lee (이준영) | Ph.D. | Staff Engineer, Mechatronics R&D Center, Samsung Electronics Co., Ltd. |
| Byung-Chul Kim (김병철) | Ph.D. | Post-Doctoral Researcher at MIT's Computer Science & Artificial Intelligence Laboratory |
| Joonmyeong Choi (최준명) | Ph.D. | Principal Engineer, Mechatronics R&D Center, Samsung Electronics Co., Ltd. |
| Jongwoo Kim (김종우) | Ph.D. | Professor at Kyung Hee University (경희대학교) |
| Sun-Pil Jung (정순필) | Ph.D. |  |
| Hae-Min Lee (이해민) | Ph.D. | 만드로 (Mand.ro) |
| Sang-Yoep Lee (이상엽) | Ph.D. | Postdoctoral researcher at d’Arbeloff lab. & TTDD lab., Department of Mechanical Engineering, MIT |
| Jung-Hwan Byun (변정환) | Ph.D. | 한국과학기술연구원 (KIST) |
| Amir Firouzeh | Ph.D. | Post-Doctoral Researcher at EPFL's Soft Transducers Laboratory |
| Sang-Min Baek (백상민) | Ph.D. | Samsung Electronics Co., Ltd. |
| Sang-Hun Kim (김상훈) | Ph.D. | Samsung Research |
| Woongbae Kim (김웅배) | Ph.D. | 한국과학기술연구원 (KIST) |
| Sung-Sik Yun (윤성식) | Ph.D. | 리보디스 |
| Jongeun Lee (이종은) | Ph.D. | Samsung Electronics Co., Ltd. |
| Christian W. Bundschu (Jae-Min) (재민) | Ph.D. | 리보디스 |
| Jae-Kyeong Kim (김재경) | Ph.D. |  |
| Jong-Hoo Park (박종후) | Ph.D. |  |
| Hyung-Min Choi (최형민) | Ph.D. | Samsung Electronics Co., Ltd. |
| Mun-Hyuk Jang (장문혁) | Ph.D. | Samsung Electronics Co., Ltd. |
| Kyu-Bum Kim (김규범) | Ph.D. |  |
| JaeMin Eom (엄재민) | Ph.D. | Postdoctoral Researcher at CREATE Lab, EPFL |
| Jae-Ryeong Choi (최재령) | Ph.D. | Postdoctoral Researcher at Harvard University |
| Sangjoon Ahn (안상준) | Ph.D. | Postdoctoral Researcher at Faculty of Aerospace Engineering, TU DELFT |
| Soo-Hwan Chae (채수환) | Ph.D. |  |
| Sang-Heui Cheon (천상희) | Ph.D. |  |
| Sung Yol Yu (유성렬) | Ph.D. | Postdoctoral Researcher at 한국과학기술연구원 (KIST) |
| Se Hyeok Ahn (안세혁) | Ph.D. |  |
| Sung-Min An (안성민) | M.S. | LG Electronics |
| Hong-Jip Kim (김홍집) | M.S. | Ph.D. Candidate at Virginia Tech., USA |
| Seok-Ryung Kwon (권석령) | M.S. | Hyundai Motor Company |
| Ji-Suk Kim (김지석) | M.S. | ADD (국방과학연구소) |
| Gyu Han Cho (조규한) | M.S. | ADD (국방과학연구소) |
| Inook Koo (구인욱) | M.S. | ADD (국방과학연구소) |
| Hong-Cheol Choi (최홍철) | M.S. | 육군사관학교 |
| Jae-Hoon Choi (최재훈) | M.S. |  |
| Sareum Kim (김사름) | M.S. | Ph.D. Candidate at University of California - Berkeley, USA |
| Woo-Young Choi (최우영) | M.S. | Naver Labs |
| Jae-Hyuk Choi (최재혁) | M.S. |  |
| Hyeong-Joon Joo (주형준) | M.S. |  |
| Jae-Hwan Kim (김재환) | M.S. |  |
| Liu TianXin (刘天鑫) | Ph.D. Candidate |  |
| Eun-Chan Kwak (곽은찬) | M.S. |  |
| Young-June Park (박영준) | M.S. |  |
| Kipyeong Yu (유기평) | M.S. |  |
| Minjo Park (박민조) | M.S. | Ph. D. Candidate at Max Planck Institute's Physical Intelligence Lab |
| Aaron Jeong (정원영) | M.S. |  |
| Jewoo Lee (이제우) | M.S. | WIRobotics |
| Jaeyoung Song (송재영) | M.S. |  |
| Mingshan He (하명산) | M.S. |  |
| Junghun Park (박정훈) | M.S. |  |
| Dahyun Nam (남다현) | M.S. |  |
| JaeHyun Lee (이재현) | M.S. |  |
| Yohan Yoon (윤요한) | M.S. |  |
| Suk-Jun Kim 김석준 | BS. | Carnegie Mellon University, U.S.A. |
| Tae Myung Huh 허태명 | BS. | Biomimetics and Dexterous Manipulation Lab at Stanford |
| Yoon-Ho Kim 김윤호 | BS. | Daewoo shipbuilding & Marine Engineering |
| Min-Kyun Noh 노민균 | BS. | Precision Motion Control LAB at M.I.T |
| Young-Sun Park 박영선 | BS. | School of dentistry, Yonsei Univ. |
| Don-Suk Lee 이돈석 | BS. |  |
| Sung-Koo Kang 강성구 | BS. | Debasish Dutta LAB at Ilinois univ. |
| Ye-in Kim 김예인 | BS. | University of Illinois at Urbana-Champaign |
| Dana Vogtmann |  |  |
| Gene Merewether |  |  |
| Jessica Lee |  |  |
| Laura Matloff |  |  |
| Whitney Huang |  |  |

Alumni에 기재된 Dana Vogtmann의 연구 주제는 Small scale mobile robot, Gene Merewether는 Rehabilitation robotics, Jessica Lee는 Biologically inspired robot, Laura Matloff는 Bio-inspired aerial robots, Whitney Huang은 Soft Robotics다.[^alumni]

## 최근 논문 목록 (2021–2026)

학술지 논문 41편, 심사 국제학회 논문 2편, 기타 국제학회 논문 3편, 국내 학술지 논문 4편, 국내 학회 논문 33편이다. 연도는 누리집의 연도 구역과 각 항목의 연도 표기를 따른다. 저자·제목·발표처는 랩의 게시 표기이며, 저자 뒤의 별표와 †는 누리집의 기호다.[^journals][^refconf][^otherconf][^domestic][^shoulder][^forearm]

**2026**

- Sung Yol Yu, Sang-Joon Ahn, Wonchul Lee, Seunguk Moon, Hyun-Jin Hong, Kyu-Jin Cho. "3D Printed Meter-Scale Soft Origami Robots Capable of Load-Bearing Actuation Via Crease Stiffness Modulation". *Advanced Science, 2026. DOI: 10.1002/advs.77127*.
- Jae-Ryeong Choi, Jisang Kang, Kyu-Jin Cho, HyunKi In. "A Passive Clamping Capstan Brake for Strap-Based Wearable Robots". *IEEE Robotics and Automation Letters, 2026. DOI: 10.1109/lra.2026.3706929*.
- Jisang Kang, Jae-Ryeong Choi, Sukyung Kang, Juyeon Park, Moon Seok Park, Kyu-Jin Cho. "A Lightweight Multi-Articular Passive Exoskeleton Using a Single Elastic Band to Improve Crouch Gait Pattern: A Pilot Study". *IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2026. DOI: 10.1109/tnsre.2026.3687896*.
- Sang-Yoep Lee, Jaewon Beom, Jin-Oh Hahn, Jae-Young Lim, Kyu-Jin Cho. "Exhalation-Synchronous Robotic Abdominal Compression for User-Centered Respiratory Assistance and Training in Neurological Patients". *Journal of NeuroEngineering and Rehabilitation, 2026. DOI: 10.1186/s12984-025-01798-3*.

**2025**

- Jae-Kyeong Kim, Se Hyeok Ahn, Sun-Pill Jung, Jemoon Kim, Deuk-Gyeom Hwang, Haseon Kim, Seung-Won Kim, Dae-Young Lee, Jinkyu Yang, Kyu-Jin Cho. "Double-Layer Self-Locking Origami Based on Opposite Folding Motion". *Soft Robotics, 2025. DOI: 10.1177/21695172251401337*.
- Parham Rezaei, Sang-Yoep Lee, Kyujin Cho, Jin-Oh Hahn. "Robust Control of Exo-Abs, a Wearable Platform for Ubiquitous Respiratory Assistance". *Journal of Dynamic Systems, Measurement, and Control, 2025. DOI: 10.1115/1.4066266*.
- Brian B. Vuong, Josie Davidson, Sangheui Cheon, Kyujin Cho, Allison M. Okamura. "Effects of Wrist-Worn Haptic Feedback on Force Accuracy and Task Speed During a Teleoperated Robotic Surgery Task". *IEEE Robotics and Automation Letters, 2025. DOI: 10.1109/lra.2025.3626226*.
- Sareum Kim, Dae-Young Lee, Je-Sung Koh, Kyu-Jin Cho. "Programmable Shape-Changing System Through Origami Pop-Up Cells". *IEEE Robotics and Automation Letters, 2025. DOI: 10.1109/lra.2025.3588796*.
- Sun-Pill Jung, Jaeyoung Song , Chan Kim, Haemin Lee, Inchul Jeong, Jongmin Kim, Kyu-Jin Cho. "Foldable and rollable interlaced structure for deployable robotic systems". *Science Robotics, 2025. DOI: 10.1126/scirobotics.adv4696*.
- Jongeun Lee, Amir Firouzeh, Seunghyun An, Pilwoo Lee, Kyu-Jin Cho. "A Miniature Rotary Electrostatic Clutch for Assigning Multi-Degrees of Freedom to Insect-Scale Robots". *Advanced Intelligent Systems, 2025. DOI: 10.1002/aisy.202500625*.
- Soomin Choi\*, Kyu Bum Kim\*, Donguk Kwon, Brian Byunghyun Kang, Kyu-Jin Cho. "Topology Optimization of Exo-Glove Poly II for Enhancing Functionality and Wearability". *Advanced Intelligent Systems, 2025. DOI: 10.1002/aisy.202500411*.
- Kyu Bum Kim, Hyungmin Choi, Byungchul Kim, Brian Byunghyun Kang, Sangheui Cheon, Kyu-Jin Cho. "Exo-Glove Poly III: Grasp Assistance by Modulating Thumb and Finger Motion Sequence with a Single Actuator". *Soft Robotics, 2025. DOI: 10.1089/soro.2024.0113*.
- Byungchul Kim, Useok Jeong, Kyu-Jin Cho. "Dual-Tendon Routing: Tendon Routing for Under-actuated Tendon-Driven Soft Hand-wearable Robot". *IEEE Robotics and Automation Letters, 2025. DOI: 10.1109/lra.2025.3544056*.
- Byungchul Kim, Useok Jeong, Kyu-Jin Cho. "Exo-Glove Pinch: A Soft, Hand-Wearable Robot Designed Through Constrained Tendon Routing Analysis". *IEEE Robotics and Automation Letters, 2025. DOI: 10.1109/lra.2025.3598647*.
- Woo-Young Choi, Woongbae Kim, Jae-Ryeong Choi, Sung Yol Yu, Seunguk Moon, and Kyu-Jin Cho. "A hyperelastic torque-reversal mechanism for soft joints with compression-responsive transient bistability". *Science Robotics, 2025. DOI: 10.1126/scirobotics.ado7696*.
- 김찬, 정순필, 김장길, 조규진. "원심하중 조건에서 로터세일용 다중 Sarrus 전개 구조의 설계와 동역학검증". *한국정밀공학회지, 2025*.
- 신민기, 김기영, 조장호, 김기원, 정성근, 조규진. "견갑상완 리듬 특성을 활용한 효율적 어깨 보조장치 개발". *한국로봇학회 논문지, 2025. DOI: 10.7746/jkros.2025.20.1.032*.

**2024**

- Hang Man Cho, Jae-Ryeong Choi, Jung-Hwan Moon, Kyu-Jin Cho, and Seung-Won Kim. "Evaluation of an assistive exosuit for alleviating neck and shoulder muscle fatigue during prolonged flexed neck posture". *Journal of NeuroEngineering and Rehabilitation, 2024. DOI: 10.1186/s12984-024-01540-5*.
- Kieran Gilday, Dohyeon Pyeon, Sudhakar Dhanush, Kyu-Jin Cho, Josie Hughes. "Exploiting passive behaviours for diverse musical playing using the parametric hand". *Frontiers in Robotics and AI, 2024. DOI: 10.3389/frobt.2024.1463744*.
- Jaemin Eom, Sung Yol Yu, Woongbae Kim, Chunghoon Park, Kristine Yoonseo Lee, and Kyujin Cho. "MOGrip: Gripper for multiobject grasping in pick-and-place tasks using translational movements of fingers". *Science Robotics, 2024. DOI: 10.1126/scirobotics.ado3939*.
- Jae-Ryeong Choi, Seung-Won Kim, and Kyu-Jin Cho. "Self-Unlocking Active Clutch for Quasi-Passive Wearable Robots". *IEEE/ASME Transactions on Mechatronics, 2024. DOI: 10.1109/tmech.2024.3509854*.
- Byungchul Kim, Hyungmin Choi, Kyu Bum Kim, Sejin Jeong, and Kyu-Jin Cho. "Exo-Glove Shell: A Hybrid Rigid-Soft Wearable Robot for Thumb Opposition with an Under-Actuated Tendon-Driven System". *Soft Robotics, 2024. DOI: 10.1089/soro.2023.0089*.
- Dohyeon Pyeon, Jungmin Ahn, Dong Hyun Kim, Sangheui Cheon, Guyeol Jeong, Kyu-Jin Cho. "A Cable-Driven Exosuit for Bidirectional  Upper Limb Resistance Exercises". *IEEE Robotics and Automation Letters, 2024. DOI: 10.1109/lra.2024.3455947*.
- Sang-Joon Ahn, Howon Lee, and Kyu-Jin Cho. "3D printing with a 3D printed digital material filament for programming functional gradients". *Nature Communications, 2024. DOI: 10.1038/s41467-024-47480-5*.
- Munhyeok Chang, Incheol Jung, Kangwoo Seo, Jonghoo Park, Hyungmin Choi, and Kyu-Jin Cho. "Posture-dependent variable transmission mechanism for prosthetic hand inspired by human grasping characteristics". *Intelligent Service Robotics, 2024. DOI: 10.1007/s11370-024-00516-7*.
- Jonghoo Park, Munhyeok Chang, Incheol Jung, Haemin Lee,  and Kyu-Jin Cho. "3D Printing in the Design and Fabrication of Anthropomorphic Hands: A Review". *Advanced Intelligence Systems, 2024. DOI: 10.1002/aisy.202300607*.
- Hyungmin Choi, Kyu Bum Kim, Sangheui Cheon, Joon-Ho Shin, and Ky-Jin Cho. "Soft Robotic Glove Modulating Joint Torque Through  Novel Passive Extensor Mechanisms". *IEEE Robotics and Automation Letters, 2024. DOI: 10.1109/lra.2024.3362593*.
- Eojin Rho, Woongbae Kim, Jungwook Mun, Sung Yol Yu, Kyu-Jin Cho, and Sungho Jo. "Impact of Physical Parameters and Vision Data on Deep Learning-based Grip Force Estimation for Fluidic Origami Soft Grippers". *IEEE Robotics and Automation Letters, vol. 9, no. 3, 2024. DOI: 10.1109/lra.2024.3356979*.

**2023**

- A. Firouzeh, J. Lee, H. Yang, D. Lee, and K.-J. Cho. "Perching and grasping using a passive dynamic bioinspired gripper". *in IEEE/ASME Transactions on Robotics, 2023. DOI: 10.1109/tro.2023.3336216*.
- Sojung Yim, Sang-Min Baek, Pilwoo Lee, Soo-Hwan Chae, Jongeun Lee, Seok-Haeng Huh, Gwang-Pil Jung, Kyu-Jin Cho. "Development of the sub-10 cm, sub-100 g jumping–crawling robot". *Intelligent Service Robotics, pp. 1-14. DOI: 10.1007/s11370-023-00497-z*.
- Hye Ju Yoo\*, Jewoo Lee\*, and Kyu-Jin Cho. "Arm Back Support Suit (Abs-Suit) for Parcel Delivery with a Passive Load Redistribution Mechanism". *IEEE Robotics and Automation Letters, vol. 9, no. 2, pp. 1238-1245, Feb. 2024, doi: 10.1109/LRA.2023.3340511. DOI: 10.1109/lra.2023.3340511*.
- Sang-Hun Kim, Useok Jeong, and Kyu-Jin Cho. "Multiparameter Remote Contact Force Sensor With Embedded Bend Sensing for Tendon-Driven Hand Robots". *IEEE/ASME Transactions on Mechatronics, 2023. DOI: 10.1109/tmech.2023.3281062*.
- Yu-Ki Lee, Yue Hao, Zhonghua Xi, Woongbae Kim, Youngmin Park, Kyu-Jin Cho, Jyh-Ming Lien, and In-Suk Choi. "Zygote structure enables pluripotent shape-transforming deployable structure". *PNAS Nexus, vol.2, no.3, 2023. DOI: 10.1093/pnasnexus/pgad022*.
- Sung-Sik Yun, Christian William Bundschu, and Kyu-Jin Cho. "A Hybrid Anchoring Technology Composed of Reinforced Flexible Shells for a Knee Unloading Exosuit". *Soft Robotics, 2023. DOI: 10.1089/soro.2021.0223*.
- Yuna Yoo, Jaemin Eom, MinJo Park, and Kyu-Jin Cho. "Compliant Suction Gripper with Seamless Deployment and Retraction for Robust Picking against Depth and Tilt Errors". *IEEE Robotics and Automation Letters, vol.8, no.3, 2023. DOI: 10.1109/lra.2023.3238903*.
- Jaeyoung Yoon, Junghwan Byun, Minjo Park, Hayun Kim, Woongbae Kim, Jinsu Yoon, Kyu-Jin Cho, and Yongtaek Hong. "Reconfigurable Innervation of Modular Soft Machines via Soft, Sticky, and Instant Electronic Adhesive Interlocking". *Advanced Intelligent Systems, 2023. DOI: 10.1002/aisy.202300013*.
- 김규범, 박지훈, 조규진. "전완의 회외 및 회내를 보조하는 유연한 착용형 로봇 개발". *한국로봇학회 논문지, 2023. DOI: 10.7746/jkros.2023.18.4.359*.
- 임소정, 이성준, 백상민, 허석행, 유재관, 조규진. "소형 곤충형 지상 이동 로봇 주행 메커니즘의 다리 기구 설계 및 분석". *한국로봇학회 논문지, 2023*.
- 최형민, 조규진. "택배 기사의 어깨 및 허리 보조를 위한 소프트 웨어러블 수트". *제18회 한국로봇종합학술대회, 2023*.
- 김규범, 조규진. "2자유도 엄지 움직임이 가능한 일상 생활 보조용 착용형 손 로봇". *제18회 한국로봇종합학술대회, 2023*.
- 안정민, 조규진. "와이어 기반 슬라이더 선형 구동기를 위한 와이어 감기 메커니즘". *제18회 한국로봇종합학술대회, 2023*.

**2022**

- MinJo Park, Woongbae Kim, Sung-Yol Yu, Jungmin Cho, Wonkyeong Kang, Junghwan Byun, Useok Jeong, and Kyu-Jin Cho. "Deployable Soft Origami Modular Robotic Arm With Variable Stiffness Using Facet Buckling". *IEEE Robotics and Automation Letters, vol.8, no.2, 2023. DOI: 10.1109/lra.2022.3232267*.
- Haemin Lee, JongHoo Park, Brian Byunghyun Kang, and Kyu-Jin Cho. "Single-Step 3D Printing of Bio-Inspired Printable Joints Applied to a Prosthetic Hand". *3D Printing and Additive Manufacturing, 2022. DOI: 10.1089/3dp.2022.0120*.
- Soo-Hwan Chae, Sang-Min Baek, Jongeun Lee, and Kyu-Jin Cho. "Agile and Energy-Efficient Jumping–Crawling Robot Through Rapid Transition of Locomotion and Enhanced Jumping Height Adjustment". *IEEE/ASME Transactions on Mechatronics, vol. 27, no.6, 2022. DOI: 10.1109/tmech.2022.3190673*.
- Jewoo Lee, Kyu-Jin Cho, and Useok Jeong. "Motion Tracking Smart Work Suit With a Modular Joint Angle Sensor Using Screw Routing". *IEEE Robotics and Automation Letters, vol. 7, no. 4, 2022. DOI: 10.1109/lra.2022.3193450*.
- Sang-Yoep Lee, Jin-Oh Hahn, Jaewon Beom, Ji-Hong Park, Han Eol Cho, Seong-Woong Kang, and Kyu-Jin Cho. "Exo-Abs: A Wearable Robotic System Inspired by Human Abdominal Muscles for Noninvasive and Effort-Synchronized Respiratory Assistance". *IEEE Transactions on Robotics, vol. 38, no. 5, 2022. DOI: 10.1109/tro.2022.3167399*.
- Byungchul Kim and Kyu-Jin Cho. "Building Simple Yet Competent Soft-Rigid Hybrid Hand Wearable Robots". *in RAS/EMBS IEEE 9th International Conference on Biomedical Robotics and Biomechatronics (BioRob) , 2022*.
- 박종후, 조규진. "4D 프린팅 출력 조건에 따른 PETG 재료의 형상 변화 특성". *한국정밀공학회 추계학술대회, 2022*.
- 유혜주, 이제우, 신민기, 조규진. "택배 기사의 어깨 및 허리 보조를 위한 소프트 웨어러블 수트". *대한기계학회 바이오공학부문, 2022*.
- 윤성식, 조규진. "에너지 저장과 방출 조건을 분리하는 착용형 장치를 위한 스프링 기반 반능동적 시스템의 개발". *대한기계학회 바이오공학부문, 2022*.
- 백상민, 이종은. 채수환, 임소정, 조규진. "생체모방 전개형 글라이더의 방향전환 메커니즘". *한국정밀공학회 춘계학술대회, 2022*.
- 임소정,백상민,조규진. "결합 기반 소형 이종 다중 로봇 시스템의 결합 방법의 설계". *한국정밀공학회 춘계학술대회, 2022*.
- 채수환, 백상민, 이종은, 조규진. "기동성이 확보된 소형 주행-도약 로봇 개발". *한국정밀공학회 춘계학술대회, 2022*.
- 이종은, 정광필, 채수환, 조규진. "소형 주행로봇을 활용한 이동식 플랫폼 설계". *한국정밀공학회 춘계학술대회, 2022*.
- 이필우, 조규진, 백상민. "가변 다리 경로를 이용한 복합 거동 주행 로봇". *한국정밀공학회 춘계학술대회, 2022*.
- 엄재민, 김웅배, 최재령, 조규진. "차세대 비정형 물류 공정을 위한 소프트 메커니즘을 활용한 그리퍼 개발". *제 17회 한국로봇종합학술대회, 2022*.
- 안상준, 이호원, 조규진. "용융압출적층기술을 이용한 다재료, 다기능 물체 프린팅 방법". *제 17회 한국로봇종합학술대회, 2022*.
- 안세혁, 정순필, 천영조, 김종민, 조규진. "큰 하중을 버틸 수 있는 종이접기 기반 접이식 스캐폴딩 시스템의 설계 및 제작". *제 17회 한국로봇종합학술대회, 2022*.
- 정순필, 조규진. "핫멜트 접착제 함침 천을 FDM 3D 프린팅에 적용한 두꺼운 패널의 오리가미 구조 유연 관절 제작 방법". *제 17회 한국로봇종합학술대회, 2022*.
- 정원영, 조규진. "면 탄성을 이용한 자가전개 오리가미 붐". *제 17회 한국로봇종합학술대회, 2022*.
- 박민조, 유성렬, 김웅배, 조규진. "공압 전개형 소프트 오리가미 링크". *제 17회 한국로봇종합학술대회, 2022*.
- 최재령, 최원석, 조규진. "운동학 데이터를 활용한 근전도 신호 추정 기반 스윙 레그 감속 의도 파악". *대한기계학회 춘계학술대회 , 2022*.

**2021**

- Woongbae Kim, Bada Seo, Sung Yol Yu, and Kyu-Jin Cho†. "Deployable Soft Pneumatic Networks (D-PneuNets) Actuator With Dual-Morphing Origami Chambers for High-Compactness". *IEEE Robotics and Automation Letters, vol. 7, no. 2, 2021. DOI: 10.1109/lra.2021.3137504*.
- Woongbae Kim, Jaemin Eom, and Kyu-Jin Cho†. "A Dual-Origami Design that Enables the Quasisequential Deployment and Bending Motion of Soft Robots and Grippers". *Advanced Intelligent Systems, vol. 4, no. 3, 2021. DOI: 10.1002/aisy.202100176*.
- Byungchul Kim, Useok Jeong, Brian Byunghyun Kang, and Kyu-Jin Cho. "Slider Tendon Linear Actuator with Under actuation and Fast connection for Soft Wearable Robots". *in IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM) , 2021*.
- Hyungmin Choi and Kyu-Jin Cho. "A Compact Mechanical Safety Mechanism for Tendon Transmission based on Magnets and Capstan Brake". *21st International Conference on Control, Automation and Systems (ICCAS 2021), 2021*.
- Kyu Bum Kim, Byungchul Kim, and Kyu-Jin Cho. "Data-Driven Inverse Kinematics for Human Hand". *21st International Conference on Control, Automation and Systems (ICCAS 2021), 2021*.
- Sangheui Cheon, Sunwoo Hwang, Jungmin Ahn, and Kyu-Jin Cho. "Towards Tendon-based Integrated Tracking and Constraining System for a Soft Teleoperation Glove with Haptic-Feedback Capability". *21st International Conference on Control, Automation and Systems (ICCAS 2021), 2021*.
- 김상훈, 조규진. "보던 케이블 기반의 고유감각 모사 촉각 및 굽힘 센서". *대한기계학회 바이오공학부문, 2021*.
- 김병철, 조규진. "Wrist Anchor for the Soft Hand Wearable Robot". *대한기계학회 바이오공학부문, 2021*.
- 임소정, 백상민, 이종은, 채수환, 정광필, 유재관, 허석행, 조규진. "곤충형 지상이동로봇 메커니즘의 개발". *한국정밀공학회 춘계학술대회, 2021*.
- 백상민, 임소정, 이종은, 채수환, 조규진. "모듈형 주행 메커니즘 개발". *한국정밀공학회 춘계학술대회, 2021*.
- 엄재민, 유성렬, 조규진. "비정형 환경에서 사용 가능한 다물체 파지 그리퍼 설계". *제 16회 한국로봇종합학술대회, 2021*.
- 김웅배, 유성렬, 박민조, 조규진. "소프트 로봇팔을 위한 전체가 유연한 대변형 접이식 공압 링크 모듈의 개발". *제 16회 한국로봇종합학술대회, 2021*.
- 이종은, 채수환, 조규진. "소형 주행 로봇을 위한 방향 전환 메커니즘의 개발". *한국군사과학기술학회 종합학술대회, 2021*.
- 채수환, 이종은, 조규진. "소형 주행 로봇의 군집 탐색 알고리즘 성능 평가를 위한 테스트 베드 구축". *한국군사과학기술학회 종합학술대회, 2021*.
- 유혜주, 박영준, 조규진. "안전한 달리기를 위한 공압 신발". *한국정밀공학회 추계학술대회, 2021*.
- 박용민, 정순필, 고제성, 유장우, 이홍석, 이창건, 조규진. "고속 정밀 이동이 가능한 소형 경량 오리가미 델타로봇". *한국정밀공학회 추계학술대회, 2021*.
- 정순필, 박용민, 김재경, 조규진. "강성 증가용 락킹 요소를 가지는 전개식 오리가미 붐 구조의 개발". *한국정밀공학회 추계학술대회, 2021*.
- 정원영, 정순필, 김재경, 박용민, 조규진. "태양 돛을 위한 종이접기 기반 전개식 붐 구조". *한국정밀공학회 추계학술대회, 2021*.
- 김재경, 이대영, 조규진. "종이접기 기반 가변강성 메커니즘을 활용한 경량 웨어러블 디바이스 개발". *한국정밀공학회 추계학술대회, 2021*.
- 최재령, 조규진. "다양한 속도의 보행 보조를 위한 가변 탄성 클러치 개발". *한국정밀공학회 추계학술대회, 2021*.
- 백상민, 임소정, 채수환, 조규진. "생체모방 오리가미 기반 로봇 설계". *한국기계학회(본부), 2021*.

## 특허

2021년 10월 22일부터 2026년 10월 22일 사이 출원·등록 날짜가 적힌 국내외 특허 35건이다. 발명자·제목·번호와 출원·등록 구분은 랩의 게시 표기를 따른다.[^patents]

- 2025-03-06 · [Domestic, Patent Applications] 조규진, 천영조, 김언, 이원호, 김종민, 이동주, 안세혁, 박용민, 정순필, "접이식 비계장치", Domestic Patent (ApplicationNumber: 10-2025-0029306, Date: 25.03.06), 2025.
- 2024-12-02 · [Domestic, Patent Applications] 조규진, 김재경, 안상훈, 정순필, "종이접기 거동기반 자가잠금 메커니즘 구조", Domestic Patent (ApplicationNumber: 10-2024-0176410, Date: 24.12.02), 2024.
- 2024-04-24 · [Domestic, Patent Applications] 조규진, 유성렬, 안상준, "소프트 오리가미 액추에이터 및 그 제조방법", Domestic Patent (Application Number: 10-2024-0054749, Date: 24.04.24), 2024.
- 2024-04-24 · [Domestic, Patent Applications] 조규진, 이호원, 안상준, "다중 소재 3D 프린팅을 위한 3D 프린터 제어 장치 및 방법", Domestic Patent (Application Number: 10-2024-0054749, Date: 24.04.24), 2024.
- 2023-04-07 · [Domestic, Patent Applications] 조규진, 편도현, 김병철, 최형민, "장갑형 로봇 장치", Domestic Patent (Registration Number: 10-2023-0045844, Date: 23.04.07), 2023.
- 2022-12-02 · [Domestic, Patent Applications] 조규진, 윤성식, "자기 정렬이 가능한 관절 보조 장치", Domestic Patent (Registration Number: 10-2022-0019508, Date: 22.12.02), 2022.
- 2022-10-17 · [Domestic, Patent Applications] 조규진, 천상희, 최형민, "와이어 구동 장치", Domestic Patent (Registration Number: 10-2022-0133139, Date: 22.10.17), 2022.
- 2022-08-31 · [Domestic, Patent Applications] 조규진, Amir Firouzeh, 이종은, "비행체용 그리퍼 장치", Domestic Patent (Registration Number: 10-2022-0110025, Date: 22.08.31), 2022.
- 2022-02-03 · [Domestic, Patent Applications] 조규진, 최재령, "가변 클러치", Domestic Patent (Registration Number: 10-2022-0013914, Date: 22.02.03), 2022.
- 2022-05-25 · [Domestic, Patent Applications] 조규진, 윤성식, 이제우, 서바다, "자세 교정용 보조 장치", Domestic Patent (Registration Number: 10-2022-0064015, Date: 22.05.25), 2022.
- 2022-04-28 · [Domestic, Patent Applications] 조규진, 김상훈, "촉각 센서", Domestic Patent (Registration Number: 10-2022-0052514, Date: 22.04.28), 2022.
- 2021-11-23 · [Domestic, Patent Applications] 조규진, 윤성식, 크리스티안 번드슈, "착용형 무릎 견인 장치", Domestic Patent (Registration Number: 10-2021-0161950, Date: 21.11.23), 2021.
- 2024-04-05 · [Domestic, Patent Issued] 조규진, 이호원, 안상준, "다중 소재 3D 프린팅을 위한 3D 프린터 제어 장치 및 방법", Domestic Patent (Registration Number: 10-2655339, Date: 24.04.05), 2024.
- 2024-01-12 · [Domestic, Patent Issued] 조규진, 엄재민, 유윤아, 박민조, "길이 방향 전개형 진공 흡입 컵", Domestic Patent (Registration Number: 10-2624036, Date: 24.01.12), 2024.
- 2023-02-06 · [Domestic, Patent Issued] 조규진, 엄재민, 유성렬, 김웅배, "내부 저장고를 가지는 다물체 파지 그리퍼", Domestic Patent (Registration Number: 10-2497956, Date: 23.02.06), 2023.
- 2023-01-31 · [Domestic, Patent Issued] 조규진, 윤성식, 정봉근, 유기평, "고관절 발목 연동형 보행 보조 장치", Domestic Patent (Registration Number: 10-2495560, Date: 23.01.31), 2023.
- 2022-11-16 · [Domestic, Patent Issued] 조규진, 안세혁, 정순필, 김종민, 천영조, 이동주, "잠금기능을 구비한 접철식 작업대", Domestic Patent (Registration Number: 10-2469208, Date: 22.11.16), 2022.
- 2022-11-16 · [Domestic, Patent Issued] 조규진, 안세혁, 정순필, 김종민, 천영조, 이동주, "접철식 작업대", Domestic Patent (Registration Number: 10-2469207, Date: 22.11.16, 2022.
- 2022-04-18 · [Domestic, Patent Issued] 조규진, 장문혁, 김상훈, "와이어 구동 스포츠용 의수", Domestic Patent (Registration Number: 10-2389180-0000, Date: 22.04.18), 2022.
- 2022-04-13 · [Domestic, Patent Issued] 조규진, 조성호, 강병현, 김대겸, 최형민, 김규범, "텐던-시스 메커니즘이 적용된 웨어러블 로봇의 구동 방법 및 장치", Domestic Patent (Registration Number: 10-2387841-0000, Date: 22.04.13), 2022.
- 2022-03-10 · [Domestic, Patent Issued] 조규진, 강병현, 김규범, 최형민, 조성호, 김대겸, "사용자의 의도 예측 방법 및 이를 수행하기 위한 장치", Domestic Patent (Registration Number: 10-2374448-0000, Date: 22.03.10), 2022.
- 2022-03-08 · [Domestic, Patent Issued] 조규진 ,최형민, 강병현, 김규범, 이승주, 이금주, "착용형 로봇을 위한 늘어짐 방지 회전형 와이어 연결 장치", Domestic Patent (Registration Number: 10-2373755-0000, Date: 22.03.08), 2022.
- 2022-02-24 · [Domestic, Patent Issued] 조규진, 천상희, 안주은, 김수덕, "악력 증강용 웨어러블 로봇 장갑", Domestic Patent (Registration Number: 10-2369322-0000, Date: 22.02.24), 2022.
- 2021-11-12 · [Domestic, Patent Issued] 조규진, 정봉근, 윤성식, "신발 형태의 발목 보조 장치", Domestic Patent (Registration Number: 10-2322466-0000, Date: 21.11.12), 2021.
- 2021-12-09 · [Domestic, Patent Issued] 조규진, 이대영, 김재경, "가변 강성 지지장치", Domestic Patent (Registration Number: 10-2339188-0000, Date: 21.12.09), 2021.
- 2021-12-03 · [Domestic, Patent Issued] 유재관, 조용진, 구지훈, 조규진, 백상민, 임소정, 이종은, 채수환, "방향 전환이 가능한 주행 로봇", Domestic Patent (Registration Number: 10-2337275-0000, Date: 21.12.03), 2021.
- 2025-05-28 · [International, Patent Applications] 조규진, 엄재민, 유윤아, 박민조, "Longitudinally Deployable Vacuum Suction Cup", International Patent (US, Registration Number: 19/221,448, Date: 25.05.28), 2025.
- 2024-08-14 · [International, Patent Applications] 조규진, 윤성식, "Self-Aligning Joint Assistance Device", International Patent (US, Registration Number: 18/805,499, Date: 24.08.14), 2024.
- 2024-02-05 · [International, Patent Applications] 조규진, 김승원, 조항만, 문정환, 최재령, "Assistive Wearable System for Relieving Muscle Fatigue in the Neck and Shoulders", International Patent (US, Registration Number: 18/432,792, Date: 24.02.05), 2024.
- 2023-08-17 · [International, Patent Applications] 조규진, 정봉근, 윤성식, 유기평, "Hip Joint and Ankle Connecting Type Gait Assistance Apparatus", International Patent (Registration Number: EP 23855166.7, Date: 23.08.17), 2023.
- 2023-01-20 · [International, Patent Applications] 조규진, 윤성식, "Self-Aligning Joint Assistance Device", International Patent (Registration Number: PCT/KR2023/001031, Date: 23.01.20), 2023.
- 2026-06-02 · [International, Patent Issued] 조규진, 윤성식, "Self-Aligning Joint Assistance Device", International Patent (US, Registration Number: 12,642,679, Date: 26.06.02), 2026.
- 2026-05-12 · [International, Patent Issued] 조규진, 김승원, 조항만, 문정환, 최재령, "Assistive Wearable System for Relieving Muscle Fatigue in the Neck and Shoulders", International Patent (US, Registration Number: 12,622,800, Date: 26.05.12), 2026.
- 2024-10-01 · [International, Patent Issued] 조규진, 조성호, 강병현, 김대겸, 최형민, 김규범, "Method for Predicting Intention of User and Apparatus for Performing Same", International Patent (US, Registration Number: 12,102,411, Date: 24.10.01), 2024.
- 2024-05-21 · [International, Patent Issued] 조규진, 윤성식, "Wearable Device Using Flexible Non-Powered Variable Impedance Mechanism", International Patent (US, Registration Number: 11,986,693, Date: 24.05.21), 2024.

## 수상과 선정

Lab News에 2023–2024년 연월이 적힌 수상 게시 항목 4건이다. 한 게시 항목에서 동상 두 건을 함께 알렸다.[^news]

- 2024-05 · Sun-Pill Jung, Jaeyoung Song, Chan Kim, Haemin Lee, Inchul Jeong이 MassRobotics 2024 Form & Function University Robotics Challenge에서 우승했다.
- 2024-02 · Sung Yol Yu와 Sangjoon Ahn이 제18회 한국로봇종합학술대회 RED Show에서 Excellence Award를 받았다.
- 2023-11 · Jae-Min Eom, Sung Yol Yu, Yuna Yoo가 제8회 KSME-SEMES Open Innovation Challenge에서 Bronze Award 두 건을 받았다.
- 2023-10 · Sang-Joon Ahn이 제2회 International Conference on Design for 3D Printing에서 Best Paper Award를 받았다.

## 소식

Lab News에 2023–2025년 연월이 적힌 논문 게재 소식 4건이다.[^news]

- 2025-01 · 소프트 관절의 압축 반응형 일시적 쌍안정성을 이용한 토크 반전 메커니즘 논문이 Science Robotics에 게재되었다.
- 2024-12 · 손가락의 병진 이동(물체의 모든 점이 같은 방향으로 같은 거리만큼 움직이는 운동)을 이용해 여러 물체를 잡고 옮기는 MOGrip 논문이 Science Robotics에 게재되었다.
- 2024-05 · 기능의 공간적 변화를 설계하는 디지털 재료 필라멘트 프린팅 논문이 Nature Communications에 게재되었다.
- 2023-12 · 수동 동역학을 이용한 생물 모방 그리퍼의 매달리기와 파지 논문이 IEEE/ASME Transactions on Robotics에 게재되었다.

## 연락과 위치

- 교수 이메일: kjcho@snu.ac.kr[^prof][^contact]
- 연구실 전화: 02-880-1663, 02-880-1703[^contact]
- 교수실 전화: 02-880-1679[^dept]
- 연구실: 서울특별시 관악구 관악로 1, 서울대학교 312동 402호[^dept][^contact]
- 교수실: 서울대학교 301동 1401호[^dept][^prof]

## 각주
[^dept]: 서울대학교 기계공학부, 「조규진 (Cho, Kyu-Jin)」. <https://me.snu.ac.kr/snu__professor/%ec%a1%b0%ea%b7%9c%ec%a7%84-cho-kyu-jin/> 2026-11-06 관측.
[^overview]: SNU Biorobotics Lab., 「Research Overview」. <https://www.biorobotics.snu.ac.kr/research-overview> 2026-11-06 관측.
[^wear]: SNU Biorobotics Lab., 「Wearables & Prosthetics」. <https://www.biorobotics.snu.ac.kr/wearables-prosthetics> 2026-11-06 관측.
[^bio]: SNU Biorobotics Lab., 「Bioinspired Robots」. <https://www.biorobotics.snu.ac.kr/bioinspired-robots> 2026-11-06 관측.
[^soft]: SNU Biorobotics Lab., 「Soft Robots」. <https://www.biorobotics.snu.ac.kr/soft-robots> 2026-11-06 관측.
[^deploy]: SNU Biorobotics Lab., 「Deployable Robots」. <https://www.biorobotics.snu.ac.kr/deployable-robots> 2026-11-06 관측.
[^prof]: SNU Biorobotics Lab., 「Professor」. <https://www.biorobotics.snu.ac.kr/professor> 2026-11-06 관측.
[^postdoc]: SNU Biorobotics Lab., 「Post-Doctoral Researchers」. <https://www.biorobotics.snu.ac.kr/postdoc> 2026-11-06 관측.
[^phd]: SNU Biorobotics Lab., 「Ph. D. Candidates」. <https://www.biorobotics.snu.ac.kr/student> 2026-11-06 관측.
[^ms]: SNU Biorobotics Lab., 「M.S. Candidates」. <https://www.biorobotics.snu.ac.kr/student-1> 2026-11-06 관측.
[^alumni]: SNU Biorobotics Lab., 「Alumni」. <https://www.biorobotics.snu.ac.kr/alumni> 2026-11-06 관측.
[^journals]: SNU Biorobotics Lab., 「Journal Articles」. <https://www.biorobotics.snu.ac.kr/journal-articles> 2026-11-06 관측.
[^refconf]: SNU Biorobotics Lab., 「Refereed Conference Papers」. <https://www.biorobotics.snu.ac.kr/refereec-conference-papers> 2026-11-06 관측.
[^otherconf]: SNU Biorobotics Lab., 「Other Conference Papers」. <https://www.biorobotics.snu.ac.kr/other-conference-papers> 2026-11-06 관측.
[^domestic]: SNU Biorobotics Lab., 「Domestic」. <https://www.biorobotics.snu.ac.kr/domestic> 2026-11-06 관측.
[^patents]: SNU Biorobotics Lab., 「Patent」. <https://www.biorobotics.snu.ac.kr/patent> 2026-11-06 관측.
[^news]: SNU Biorobotics Lab., 「Lab News」. <https://www.biorobotics.snu.ac.kr/news> 2026-11-06 관측.
[^contact]: SNU Biorobotics Lab., 「Contact」. <https://www.biorobotics.snu.ac.kr/application> 2026-11-06 관측.
[^shoulder]: 신민기 외, 로봇학회 논문지 20(1), 32–39 (2025), 「견갑상완 리듬 특성을 활용한 효율적 어깨 보조장치 개발」. DOI: 10.7746/jkros.2025.20.1.032. <https://jkros.org/_PR/view/?aidx=44003&bidx=3973> 초록 기준(논문 페이지 게시 초록). 2026-11-06 관측.
[^forearm]: 김규범, 박지훈, 조규진, 로봇학회 논문지 18(4), 359–366 (2023), 「전완의 회외 및 회내를 보조하는 유연한 착용형 로봇 개발」. DOI: 10.7746/jkros.2023.18.4.359. <https://jkros.org/_PR/view/?aidx=38514&bidx=3478> 초록 기준(논문 페이지 게시 초록). 2026-11-06 관측.
[^p1]: K. B. Kim 외, K.-J. Cho, Soft Robotics (2025). <https://doi.org/10.1089/soro.2024.0113> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p2]: S.-Y. Lee 외, K.-J. Cho, IEEE Transactions on Robotics (2022). <https://doi.org/10.1109/tro.2022.3167399> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p3]: S.-H. Chae, S.-M. Baek, J. Lee, K.-J. Cho, IEEE/ASME Transactions on Mechatronics (2022). <https://doi.org/10.1109/tmech.2022.3190673> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p4]: W.-Y. Choi 외, K.-J. Cho, Science Robotics 10 (2025). <https://doi.org/10.1126/scirobotics.ado7696> 초록 기준(OpenAlex 등록 초록). Crossref 등록 서지 <https://api.crossref.org/works/10.1126/scirobotics.ado7696>. 논문번호 eado7696. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p5]: J. Eom 외, K.-J. Cho, Science Robotics 9 (2024). <https://doi.org/10.1126/scirobotics.ado3939> 초록 기준(OpenAlex 등록 초록). Crossref 등록 서지 <https://api.crossref.org/works/10.1126/scirobotics.ado3939>. 논문번호 eado3939. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p6]: S.-J. Ahn, H. Lee, K.-J. Cho, Nature Communications (2024). <https://doi.org/10.1038/s41467-024-47480-5> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p7]: S.-P. Jung 외, K.-J. Cho, Science Robotics (2025). <https://doi.org/10.1126/scirobotics.adv4696> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.
[^p8]: S. Y. Yu 외, K.-J. Cho, Advanced Science (2026). <https://doi.org/10.1002/advs.77127> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5062631070,publication_year:2021-2026> 2026-11-06 관측.

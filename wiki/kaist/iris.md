# 인터랙티브 로봇 시스템 연구실 (Interactive Robotic Systems Laboratory, IRiS Lab)

**KAIST 건설및환경공학과 · 유지환 교수**

- 분야: 햅틱과 원격조종, 성장형 소프트 로봇, 자율주행, 기계 구조와 꼬임줄 구동기[^dept][^r1][^r2][^r3][^r4]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 햅틱[^r1], 인간–로봇 상호작용[^dept], 소프트 로보틱스[^r2], 자율주행[^r3], 제어 이론·제어 공학[^r1][^r4], 착용형 로봇·외골격[^r4], 인공 근육[^r4]
- 홈페이지: <https://iris.kaist.ac.kr>
- 근거와 출처: [IRiS Lab 근거 페이지](iris-sources.md)

> 사람이 접근하기 어려운 곳에서 로봇을 조종하고, 로봇이 사람과 주변 환경에 맞춰 움직이도록 장치의 구조와 제어 방법을 함께 개발하는 연구실이다.[^home][^r1]

## 무엇을 연구하나

IRiS Lab은 재난 대응·건설·채굴·농업 등의 현장에서 사람을 대신할 로봇의 상호작용 기술을 연구한다. 네 갈래는 햅틱(힘·진동 등으로 사람에게 촉각과 움직임의 느낌을 전달하는 기술)과 원격조종, 성장형 소프트 로봇(부드러운 재료나 구조로 된 몸체가 길어지며 주변 공간으로 진입하는 로봇), 자율주행, 기계 구조를 이용한 기능 구현이다. 로봇의 제어(장치에 가하는 입력을 정해 움직임이나 상태를 목표에 맞추는 일)와 하드웨어(장치의 물리적 구성 요소)를 함께 설계한다.[^home][^r1][^r2][^r3][^r4] 학과 소개는 이 연구실의 목적을 인간 또는 주변환경과 상호작용하는 로봇 시스템의 이론과 기술 개발로 설명한다.[^dept]

원격조종에서는 사람이 로봇을 움직일 때 접촉한 힘을 다시 느낄 수 있게 하는 햅틱 장치를 개발한다.[^r1] 작업과 로봇에 맞춘 조종 장치와 접촉 중의 힘을 전달하는 방법을 개발하며, 조종 지연이 있거나 단단한 가상 환경과 접촉할 때에도 동작이 불안정해지지 않게 하는 제어를 연구한다.[^r1] 사람이 시범으로 수행한 접촉 작업에서 힘과 움직임 정보를 얻어 로봇에 기술을 가르치는 연구도 한다. 대표 논문 1은 누르고 놓는 동작 동안 주고받은 에너지(운동이나 상태를 바꾸는 일을 할 수 있는 양)를 이용하는 제어, 대표 논문 2는 협동로봇(사람과 같은 공간에서 함께 작업하도록 만든 로봇)을 촉감 전달 장치로 쓸 때 생기는 마찰(접촉한 물체의 상대 움직임을 방해하는 작용)을 추정하고 보상하는 방법이다.[^r1][^p1][^p2]

소프트 로봇에서는 길이가 늘어나며 주변 공간으로 진입하는 성장형 로봇을 개발한다.[^r2] 연구실의 로봇은 안에 말린 몸체를 끝에서 바깥으로 뒤집어 내보내며 자란다. 몸체 안으로 도구를 전달할 통로를 유지하고, 원하는 방향으로 돌리며, 다시 회수하는 구조가 핵심이다. 대표 논문 3은 공기를 넣어 부풀리는 구조로 내부 통로를 확보한다. 대표 논문 4는 조향(진행 방향을 바꾸는 일)·카메라 유지·회수 기능을 통합한 내시경(몸 안에 넣어 내부를 관찰하는 기구)을 제안한다.[^r2][^p3][^p4]

자율주행에서는 공개 지도와 차량의 관측 자료를 이용해 위치를 알아내고, 주변을 인식하며, 이동 경로를 정하는 기술을 개발한다.[^r3] 적은 학습 자료로 작동하는 방법과 기기 안에서 계산 부담을 줄이는 구조를 함께 연구한다. 위치 추정(관측 자료로 자신이나 대상이 어디에 있는지 알아내는 일) 연구인 대표 논문 5는 차량 관측과 공개 지도를 연결한다. 대표 논문 6은 LiDAR(Light Detection and Ranging, 빛을 보내고 반사되어 돌아오는 정보를 이용해 거리를 재는 기술)의 관측과 공개 거리 사진을 연결해 차량의 위치와 방향을 추정한다.[^r3][^p5][^p6]

기계 구조 연구에서는 구동기(공급된 에너지를 기계적 움직임으로 바꾸는 장치)와 변속기(입력축과 출력축 사이의 회전 속도·회전력 전달 관계를 바꾸는 장치)를 설계한다. 모터가 줄을 꼬아 길이를 줄이면서 당기는 힘을 만드는 꼬임줄 구동기를 인공 근육(전기·열·화학 자극으로 늘었다 줄었다 하며 힘을 내는 소재·구동기)으로 개발한다.[^r4] 대표 논문 7은 줄의 장력(물체를 팽팽하게 당길 때 그 내부에서 길이 방향으로 전달되는 힘)을 제어하고, 대표 논문 8은 반지름이 변하는 두 드럼(원통 모양의 회전 부품)을 이용해 이동 범위를 늘리고 회전과 직선 이동 사이의 전달 관계를 개선한다. 연구실은 꼬임줄 구동기를 통합한 착용형 로봇·외골격(몸 바깥에 입어 움직임을 돕는 구조물)을 개발해 팔·어깨·엉덩이·무릎의 움직임을 돕는다.[^r4] 전기식 감지·판단 장치를 추가하지 않고 외부 힘에 반응하는 바퀴·물체 잡기 장치도 개발한다.[^r4][^p7][^p8]

## 주요 연구 주제

### 햅틱과 원격조종

연구실은 사람의 동작과 촉각 정보를 기록하는 장치, 로봇이 학습할 수 있도록 촉각 정보를 표현하는 방법, 사람의 작업 기술을 로봇에 전달하는 방법을 함께 연구한다. 양팔 협동로봇을 이용하는 조종 장치와 접촉을 안정시키는 제어도 개발한다. 대표 논문 1은 누르는 동작과 놓는 동작을 하나의 주기로 보고 에너지 교환을 조절해, 안정적으로 표현할 수 있는 접촉 특성과 힘 전달의 충실도를 높인다.[^r1][^p1]

### 성장형 소프트 로봇의 통로·조향·회수

좁고 복잡한 공간에서 자라는 몸체의 내부 통로를 열어 두고, 끝에 붙인 카메라와 도구를 운반하며, 원하는 방향으로 이동하고 회수하는 하드웨어를 개발한다. 대표 논문 3의 내부 통로는 대기압(지표 위 공기가 누르는 압력)을 유지해 몸체를 부풀리는 압력의 간섭 없이 도구와 재료가 지나가게 한다. 대표 논문 4는 부드러운 내시경의 구조에 카메라 유지, 공기 압력으로 움직이는 조향 장치, 접혀 꺾이지 않고 회수하는 장치를 결합한다.[^r2][^p3][^p4]

### 공개 지도에 기반한 자율주행

비용이 큰 사전 고정밀 지도(차선·표지 같은 도로 정보를 세밀하게 기록한 지도)에 의존하지 않도록 공개 지도를 가공하고, 차량의 주변 인식·위치 추정·경로 계획을 설계한다. 대표 논문 5는 공개 평면 지도에 차량 관측을 맞추고, 대표 논문 6은 빛으로 잰 거리 관측과 거리 사진을 같은 특징 공간(자료의 특성을 수치 좌표로 나타낸 공간)에서 연결한다.[^r3][^p5][^p6]

### 꼬임줄 구동기와 기계 구조에 담은 기능

꼬임줄 구동기(Twisted String Actuator, TSA)의 수학 모형(수와 식으로 대상의 관계나 변화를 나타낸 표현)과 제어를 개발하고, 이를 몸의 움직임을 돕는 착용형 로봇에 통합한다.[^r4] 대표 논문 7은 강성(변형에 저항하는 정도)과 원래 길이가 달라지는 줄의 특성을 추정해 장력을 제어한다. 대표 논문 8은 두 드럼의 구조로 줄의 이동 범위와 전달 관계를 조절한다. 연구실은 입력에 따라 반지름이 바뀌는 바퀴와, 물체를 잡는 동작에서 회전시키는 동작으로 전환하는 기계 구조도 설계한다.[^r4][^p7][^p8]

## 대표 논문

KAIST 재직 시기의 논문 가운데 네 연구 갈래를 고르게 보여 주는 8편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸의 「마지막 저자」는 전체 저자 목록의 순서를 뜻한다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2024 | [Relaxing Conservatism for Enhanced Impedance Range and Transparency in Haptic Interaction](https://doi.org/10.1109/toh.2024.3359230) · IEEE Transactions on Haptics | Hüseyin Tugcan Dinc · 유지환(마지막 저자) | 접촉에서 누르고 놓는 동안 교환한 에너지를 살핀 뒤 다음 주기에 저항(감쇠)을 조절해, 접촉 안정성과 힘 전달의 충실도를 개선한다.[^p1] |
| 2 | 2024 | [Model-free energy-based friction compensation for industrial collaborative robots as haptic displays](https://doi.org/10.1109/tmech.2024.3410330) · IEEE/ASME transactions on mechatronics | Huseyin Tugcan Dinc · Joong-Ku Lee · 유지환(마지막 저자) | 로봇의 움직임에서 마찰로 소모된 에너지를 이용해 마찰을 추정하고 보상한다. 협동로봇을 사람이 힘을 느끼는 장치로 사용하기 위한 방법이다.[^p2] |
| 3 | 2024 | [Inflatable-Structure-Based Working-Channel Securing Mechanism for Soft Growing Robots](https://doi.org/10.1109/lra.2024.3426322) · IEEE Robotics and Automation Letters | Dongoh Seo · Nam Gyun Kim · 유지환(마지막 저자) | 자라는 로봇 안에 대기압을 유지하는 통로를 만들어 도구와 재료가 몸체를 부풀리는 압력의 간섭 없이 지나가게 한다.[^p3] |
| 4 | 2026 | [A soft growing robotic endoscope for painless and strain-free insertion](https://doi.org/10.1177/21695172251369693) · Soft Robotics | Nam Gyun Kim · 유지환(마지막 저자) | 끝에서 자라는 부드러운 내시경에 카메라 유지·조향·회수 구조를 결합했다. 모형과 생체 내 시험에서 기존 내시경보다 삽입 힘과 대장 변형이 줄어드는 결과를 보였다.[^p4] |
| 5 | 2024 | [Autonomous Vehicle Localization without Prior High-Definition Map](https://doi.org/10.1109/tro.2024.3392149) · IEEE Transaction on Robotics | Sangmin Lee · 유지환(마지막 저자) | 차량 센서의 관측과 누구나 구할 수 있는 평면 지도를 맞춰, 미리 고정밀 지도를 만들지 않고도 차량 위치를 알아내는 방법이다.[^p5] |
| 6 | 2026 | [LSV-Loc: LiDAR to StreetView Image Cross-Modal Localization](https://doi.org/10.1109/lra.2026.3653282) · IEEE Robotics and Automation Letter | Sangmin Lee · DongHyun Choi · 유지환(마지막 저자) | 차량의 레이저 거리 관측을 위치 정보가 붙은 공개 거리 사진과 비교한다. 고정밀 지도 없이도 사진과 관측의 대응 관계로 위치와 방향을 추정한다.[^p6] |
| 7 | 2023 | [Tension Control of Twisted String Actuators in Variation of Stiffness and Original Length of Strings](https://doi.org/10.1109/tmech.2023.3253565) · IEEE/ASME Transactions on Mechatronics | Seungjoon Baek · 유지환(마지막 저자) | 줄의 강성과 원래 길이가 달라지는 정도를 추정하고 모터의 회전 각도를 조절해, 꼬인 줄이 당기는 힘을 간접적으로 제어한다.[^p7] |
| 8 | 2026 | [Dual Variable-Radius Drum for Transmission Ratio Linearization and Stroke Enhancement in Twisted String Actuators](https://doi.org/10.1109/lra.2026.3665071) · IEEE Robotics and Automation Letters | Juyeong Seo · Jaehyung Jang · 유지환(마지막 저자) | 반지름이 변하는 두 드럼을 사용해 꼬임줄 구동기의 이동 범위를 늘리고, 회전과 직선 이동 사이의 전달 관계를 거의 일정하게 만드는 구조다.[^p8] |

## 교수와 전문 분야

유지환 교수는 인하대학교 기계공학과 학사(1995), KAIST 기계공학과 석사(1997)·박사(2002)를 받았다. 2005–2019년 한국기술교육대학교 기계공학부에서 조교수·부교수·교수로 재직했고, 2019–2022년 KAIST 건설및환경공학과 부교수를 거쳐 2023년부터 교수로 재직한다.[^dept]

전문 분야는 건설로봇, 햅틱과 원격조종, 성장형 소프트 로봇, 유연 구동기와 착용형 보조 장치, 자율주행이다. 최근 대표 논문은 접촉 제어와 마찰 보상, 내부 통로를 유지하는 성장형 로봇, 공개 지도를 이용한 차량 위치 추정, 꼬임줄 구동기의 장력 제어와 구조 설계로 이어진다.[^dept][^pi][^p1][^p2][^p3][^p5][^p7][^p8]

교수 소개는 KAIST Space Institute·KAIST Institute for Robotics·G-School·Human-Robot Interaction Research Center·Robotics Program의 겸임 직위를 적고 있다. 2025년부터 IEEE Transactions on Haptics 편집장을 맡으며 IEEE Robotics and Automation Society Administrative Committee와 Korea Haptics Society에서도 활동한다.[^pi]

## 응용 분야

재난 현장과 좁은 공간의 탐색·구조, 산업 설비 점검, 지하 굴착, 건설·채굴·농업 현장의 로봇 작업이 주요 응용이다. 사람의 기술을 전달하는 원격조종은 위험 현장과 제조 조립에, 성장형 로봇은 도구 운반과 내시경에, 꼬임줄 구동기는 재활·농작업·머리 위 작업을 돕는 착용형 장치에 연결한다.[^home][^r1][^r2][^r4][^j201][^j206][^j207][^j208][^j212]

## 구성원

2026년 11월 6일 연구실 목록 기준으로 박사후연구원 6명, 박사과정 14명, 석사과정 12명이다. 과정은 목록의 구분, 연구 주제와 학교 이메일은 구성원 소개의 표기를 따른다. 「대표 논문 참여」는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Marion Pontreau | 박사후연구원 |  | Mechanical Intelligence Team; Haptics; Wearables |  |  |
| Jaehyung Jang | 박사후연구원 |  | Mechanical Intelligence Team | jhjang.kd@kaist.ac.kr | 8 |
| Joong-Ku Lee | 박사후연구원 |  | Haptics and Telerobotics Team; Telerobotics; Haptics; Artificial Intelligence | iamjoong9@kaist.ac.kr | 2 |
| Nam Gyun Kim | 박사후연구원 |  | Soft Growing Robots Team; Soft Robotics; Control Theory; Biomimetics | nam96bird@kaist.ac.kr | 3, 4 |
| Hyeonseok Choi | 박사후연구원 |  | Haptics and Telerobotics Team; Teleoperation; Haptics; Control | and1013@kaist.ac.kr |  |
| Kwang-Hyun Lee | 박사후연구원 | 2019 | Haptics and Telerobotics Team | kwanghyun90@kaist.ac.kr |  |
| Dong-Geol Lee | 박사과정 |  | Haptics and Telerobotics Team; Telerobotics; Robot/AI-Assisted Surgery; Task Automation and Learning | slfjdkgh08@kaist.ac.kr |  |
| Lev Kozlov | 박사과정 |  | Haptics and Telerobotics; Contact-rich Manipulation; Reinforcement Learning | l.kozlov@kaist.ac.kr |  |
| Igor Alentev | 박사과정 |  | Haptics and Telerobotics Team; Variational Integrators; Optimal Control |  |  |
| Juyeong Seo | 박사과정 |  | Mechanical Intelligence Team Leader; Cable-Driven Parallel Robot; Mechanical Intelligence Embedded System; Twisted String Actuator | jyseo0206@kaist.ac.kr | 8 |
| Heejin Song | 박사과정 |  | Autonomous Vehicles Team; Autonomous Vehicle; Localization; Sensor Fusion; Navigation | heejincandy@kaist.ac.kr |  |
| Sanghun Lee | 박사과정 |  | Soft Growing Robots Team Leader; Soft Robotics; Soft Growing Robot; Bioinspired | lsh4304@kaist.ac.kr | 4 |
| Handong Lee | 박사과정 |  | Autonomous Vehicles Team Leader; Autonomous Vehicle; Generative AI; Planning | hdong564@kaist.ac.kr |  |
| Shinwoo Park | 박사과정 |  | Soft Growing Robots Team; Soft Growing Robot; Soft Robotics; Soft Actuators; Wearable Devices | parkswoo@kaist.ac.kr | 4 |
| Seong-Su Park | 박사과정 |  | Haptics and Teleorobotics Team Leader; Skill Transfer; Teleoperation; Learning-Based Control; Artificial Intelligence | simon.park@kaist.ac.kr |  |
| Chang Nho Cho | 박사과정 | 2025 | Haptics and Telerobotics Team | cncho@kaist.ac.kr |  |
| Euibin Shin | 박사과정 |  | Mechanical Intelligence Team; Twist |  |  |
| Taeil Chung | 박사과정 |  | Haptics and Telerobotics Team |  |  |
| Yongjun Kim | 박사과정 |  | Haptics and Telerobotics Team; Interactive robot; Haptics; Control | yongjun@kaist.ac.kr |  |
| Hyeonseok Seong | 박사과정 |  | Mechanical Intelligence Team; Twisted String Actuator; Exoskeleton; Biomimetics | hysk.seong@kaist.ac.kr |  |
| Junsu Park | 석사과정 |  | Haptics and Telerobotics Team; Learning from Teleoperation; Multimodal Robot Learning | park00@kaist.ac.kr |  |
| Dong-hyun Choi | 석사과정 |  | Soft Growing Robots Team; Soft Growing Robot; Soft Robotics; Mechanism Design | dhc456@kaist.ac.kr |  |
| Chaewon Kim | 석사과정 |  | Haptics and Telerobotics Team; Contact-rich Manipulation; Multimodal Robot Learning | clkimcw@kaist.ac.kr |  |
| Purevzaya Amarzaya | 석사과정 |  | Autonomous Vehicles Team; Computer Vision; Planning |  |  |
| Jungyue Han | 석사과정 |  | Mechanical Intelligence Team; Construction Robot; Gripper; Robot Hand; Exosuit | 6june.h@kaist.ac.kr |  |
| Manh Duc Duong | 석사과정 |  | Autonomous Vehicles Team; Autonomous Driving; Mobile Robot |  |  |
| Junhyeong Park | 석사과정 |  | Mechanical Intelligence Team; Hardware | jamesjun2000@kaist.ac.kr |  |
| Seungmin Lee | 석사과정 |  | Haptics and Telerobotics Team; Teleoperation; Artificial Intelligence | lsm224@kaist.ac.kr |  |
| Jae Yun Hwang | 석사과정 |  | Soft Growing Robots Team; Soft Growing Robot; Soft Robotics | Jaeyun.Hwang@kaist.ac.kr |  |
| Ivan Domrachev | 석사과정 |  | Haptics and Telerobotics Team; Convex Optimization; Motion planning; Optimal Control; Stohastic Model Predictive Control |  |  |
| Jihan An | 석사과정 |  | Haptics and Telerobotics Team; Learning from Teleoperation; Artificial Intelligence; Control Theory | jihanan0221@kaist.ac.kr |  |
| Donghyeon Youn | 석사과정 |  | Haptics and Telerobotics Team; Teleoperation | youndonghyeon@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 Alumni에 게시된 37명이다. 학위·연도는 소개에 적힌 KAIST 또는 한국기술교육대학교의 학력이고, 진로는 연구실이 적은 직위와 기관이다. 한국기술교육대학교 시기의 이전 구성원도 포함한다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seif Farag | M.S. Robotics Program (KAIST) (2025) | Senior Robotics Engineer |
| Nabila Adawy | M.S. Robotics Program (KAIST) (2025) | Former Researcher |
| DongHyun Choi | M.S. Civil and Environmental Engineering (KAIST) (2025) | Robotics Research Engineer @ POSCO DX |
| Shubhranil Sengupta | M.S. Robotics Program (KAIST) (2023) | Robotics Researcher @ Samsung Research |
| Seung-Lyeol Lee | M.S. Civil and Environmental Engineering (KAIST) (2023) | Robotics Research Engineer @ LIG Nex-1 |
| Huseyin Tugcan Dinc | Ph.D. Robotics Program (KAIST) (2025) | TU WIEN |
| Sangmin Lee | Ph.D. Civil and Environmental Engineering (KAIST) (2026) | Autonomous Driving AI Researcher @ Hanwha Aerospace |
| Ji-Hun Kim | M.S. Mechanical Engineering (KOREATECH) (2021) | Mechanical Research Engineer @ ASML |
| Younghun Cho | Ph.D. Civil and Environmental Engineering (KAIST) (2024) | Researcher @ Korea Institute of Machinery & Materials (KIMM) |
| Simeon Nedelchev | M.S. Mechanical Engineering (KOREATECH) (2018) | Senior Lecturer @ Innopolis University |
| Muhammad Arshad Khan | M.S. Mechanical Engineering (KOREATECH) (2019) | Senior Software Engineer @ Better Physiology |
| Hiba Latifee | M.S. Mechanical Engineering (KOREATECH) (2019) | STEM Coordinator @ Alpha College |
| Bhivraj Suthar | Ph.D. Mechanical Engineering (KOREATECH) (2020) | Assistant Professor, IIT Jodhpur |
| Muhammad Usman | M.S. Mechanical Engineering (KOREATECH) (2018) | System Engineer @ M-ECS |
| Zain Mehdi | M.S. Mechanical Engineering (KOREATECH) (2018) | PhD Researcher @ KU Leuven |
| Harsimran Singh | Ph.D. Mechanical Engineering (KOREATECH) (2017) | Research Scientist @ DLR, Germany |
| Usman Mehmood | Ph.D. Mechanical Engineering (KOREATECH) (2021) | Postdoctoral Researcher @ Asan Medical Center (AMC) |
| Naveed Ahmed Usmani | M.S. Mechanical Engineering (KOREATECH) (2016) | Senior Software Engineer @ HERE Technologies |
| Vitalii Pruks | Ph.D. Mechanical Engineering (KOREATECH) (2019) | Founding Robotics Engineer @ Imagine Health |
| Muhammad Nabeel | M.S. Mechanical Engineering (KOREATECH) (2015) | Co-founder and CEO @ Exitbase |
| Dong-Hwi Lee | M.S. Mechanical Engineering (KOREATECH) (2019) | Battery Management Researcher @ SK-On |
| Tae-Hwan Kim |  | Former Researcher |
| Sangwoo Ji | M.S. Mechatornics, Robotics, and Automation Engineering (KOREATECH) (2002) | System Engineer @ Google AI |
| Aghil Jafari | Ph.D. Mechanical Engineering (KOREATECH) (2015) | Assistant Professor, UWE Bristol |
| Sang-Goo Jeong | M.S. Mechanical Engineering (KOREATECH) (2020) | Mechatronics Engineer @ Bear Robotics |
| Kwang-Uk Jeong | M.S. Mechanical Engineering (KOREATECH) (2019) | SLAM Research Engineer @ RideFlux |
| Boris Gromov |  | Team Lead @ Hexagon Mining |
| Chan-Il Lee | M.S. Mechanical Engineering (KOREATECH) (2019) | Robotics Research Engineer @ LIG Nex-1 |
| Jeon-Jin Kang | M.S. Mechanical Engineering (KOREATECH) (2013) | Former Researcher |
| YoungUk Song | M.S. Mechanical Engineering (KOREATECH) (2012) | Seoul National University |
| Dmitry Popov | Ph.D Mechanical Engineering (KOREATECH) (2014) | Co-Founder & CEO @ WurQ |
| Quang Ha Van | M.S. Mechanical Engineering (KOREATECH) (2011) | University of Innsbruck |
| Seung-Jun Lee | B.S. Mechanical Engineering (KOREATECH) (2014) | LIG NEX1 |
| Beibei Han | M.S. Mechanical Engineering (KOREATECH) (2008) | Sensing Technology Analyst @ Apple |
| Ildar Farkhatdinov | M.Sc. Mechanical Engineering (KOREATECH) (2008) | Associate Professor @ King’s College London |
| Nguyen Ba Hai | Ph.D. Mechanical Engineering (KOREATECH) (2010, 2008) | Head @ HoChiMinh City University of Technical Education |
| JaeSeok Kim | M.S. Mechanical Engineering (KOREATECH) (2014) | Postdoctoral Researcher @ Università degli Studi di Firenze |

## 최근 논문 목록 (2021–2026)

연구실 Publications·연구 소개·과제 소개에 게시된 44편이다. 연도와 제목·저자·발표처는 연구실의 구역·인용 표기를 따르고, 연도가 없는 한 편은 등록된 출판 연도를 따른다. arXiv 사전 공개본은 연구 소개의 판본 표기를 유지했다. 학회 이름과 연도만 적힌 항목은 연구실 기재 표기다.[^pubs][^r1][^r2][^r4][^j208][^oa]

**2026**

- Juyeong Seo, Jaehyung Jang, Seungjoon Baek, Jee-Hwan Ryu. "Dual Variable-Radius Drum for Transmission Ratio Linearization and Stroke Enhancement in Twisted String Actuators". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2026.3665071>.
- Nam Gyun Kim, Shinwoo Park, Dongoh Seo, Sanghun Lee, Hyuk Yoon, Jaihwan Kim, Jee-Hwan Ryu. "A soft growing robotic endoscope for painless and strain-free insertion". *Soft Robotics*. DOI: <https://doi.org/10.1177/21695172251369693>.
- Sangmin Lee, DongHyun Choi, Jee-Hwan Ryu. "LSV-Loc: LiDAR to StreetView Image Cross-Modal Localization". *IEEE Robotics and Automation Letter*. DOI: <https://doi.org/10.1109/LRA.2026.3653282>.
- Park, S., Kim, N. G., Seo, D., Lee, S., & Ryu, J. H. Bistable Steering Mechanism for Enhanced Control in Soft Toroidal Robots. Soft Robotics, 21695172261438632. DOI: <https://doi.org/10.1177/21695172261438632>.
- Lee, S., Kim, N. G., Park, S., Lee, D. Y., & Ryu, J. H. (2026). Origami-Based Inner Channel Securing Mechanism for Soft Growing Robots. IEEE Robotics and Automation Letters, 11(5), 5970-5977. DOI: <https://doi.org/10.1109/lra.2026.3677746>.
- Jang, J., Seo, J. Y., Lee, D. Y., & Ryu, J. H. (2026). MORPH wheel: A passive variable-radius wheel embedding mechanical behavior logic for input-responsive transformation. arXiv preprint arXiv:2602.06265. DOI: <https://doi.org/10.48550/arXiv.2602.06265>.
- Jang, J., Park, J., Lee, J. K., & Ryu, J. H. (2026). SPINE Gripper: A Twisted Underactuated Mechanism-based Passive Mode-Transition Gripper. arXiv preprint arXiv:2601.06833. DOI: <https://doi.org/10.48550/arXiv.2601.06833>.

**2025**

- Nam Gyun Kim, William E Heap, Yimeng Qin, Elvy B Yao, Jee-Hwan Ryu, Allison M Okamura. "Self-Wearing Adaptive Garments via Soft Robotic Unfurling". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2025.3634909>.
- Hyeonseok Choi, Nam Gyun Kim, Seungjoon Baek, Christian Ott, Jee-Hwan Ryu. "Unidirectional virtual inerter for high-bandwidth robot motion control". *The International Journal of Robotics Research*. DOI: <https://doi.org/10.1177/02783649251363999>.
- Handong Lee, DongHyun Choi, Heejin Song, Sangmin Lee, Jee-Hwan Ryu. "Navigation in Underground Parking Lot by Semantic Occupancy Grid Map Prediction". *2025 22nd International Conference on Ubiquitous Robots (UR)*. DOI: <https://doi.org/10.1109/UR65550.2025.11078039>.
- DongHyun Choi, Sangmin Lee, Handong Lee, Jee-Hwan Ryu. "VFT-LIO: Visual Feature Tracking for Robust LiDAR Inertial Odometry Under Repetitive Patterns". *2025 22nd International Conference on Ubiquitous Robots (UR)*. DOI: <https://doi.org/10.1109/UR65550.2025.11078091>.
- Nam Gyun Kim, Nikita J Greenidge, Joshua Davy, Shinwoo Park, James H Chandler, Jee-Hwan Ryu, Pietro Valdastri. "External steering of vine robots via magnetic actuation". *Soft Robotics*. DOI: <https://doi.org/10.1089/soro.2023.0182>.
- Joong-Ku Lee, Hyeonseok Choi, Young Soo Park, Jee-Hwan Ryu. "Teaching Robots to Handle Nuclear Waste: A Teleoperation-Based Learning Approach". *Waste Management Symposia 2025*. DOI: <https://doi.org/10.48550/arXiv.2504.01405>.
- Saewoong Oh, Jaehyung Jang, Wonhee Ji, Yang Yang, Mannan Khan, Carmel Majidi, Jee-Hwan Ryu, Il-Kwon Oh. "Embodied Auxetic Intelligence in a Glove-Type Wearable Haptic Interface Connecting Humans to Robots and the Metaverse". *Adv. Funct. Mater. 2025, 2502222*. DOI: <https://doi.org/10.1002/adfm.202502222>.
- Lee, S., Kim, N. G., Seo, D., Park, S., & Ryu, J. H. (2025, May). Helical Structured Soft Growing Robot for Hazardous Gas Suction in Inaccessible Environments. In 2025 IEEE International Conference on Robotics and Automation (ICRA) (pp. 12907-12913). IEEE. DOI: <https://doi.org/10.1109/icra55743.2025.11128325>.

**2024**

- Huseyin Tugcan Dinc, Thomas Hulin, Michael Rothammer, Hyeonseok Seong, Bertram Willberg, Benedikt Pleintinger, Jee-Hwan Ryu, Christian Ott. "CoaxHaptics-3RRR: A Novel Mechanically Overdetermined Haptic Interaction Device Based on a Spherical Parallel Mechanism". *2024 IEEE Conference on Telepresence CalTech, USA*. DOI: <https://doi.org/10.1109/telepresence63209.2024.10841776>.
- Joong-Ku Lee, Donghyeon Kim, Seong-Su Park, Jiye Lee, Jee-Hwan Ryu. "Development of a Collaborative Robotic Arm-based Bimanual Haptic Display". *AsiaHaptics 2024. Sunway University, Malaysia*. DOI: <https://doi.org/10.48550/arXiv.2411.07402>.
- Donghyeon Kim, Seong-Su Park, Kwang-Hyun Lee, Dongheui Lee, Jee-Hwan Ryu. "Is a Simulation better than Teleoperation for Acquiring Human Manipulation Skill Data?". *2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*. DOI: <https://doi.org/10.1109/IROS58592.2024.10801865>.
- Kang-Won Lee, Dae-Kwan Ko, Yongjun Kim, Jee-Hwan Ryu, Soo-Chul Lim. "Latency-free driving scene prediction for on-road teledriving with future-image-generation". *IEEE Transactions on Intelligent Transportation Systems*. DOI: <https://doi.org/10.1109/TITS.2024.3435481>.
- Dongoh Seo, Nam Gyun Kim, Jee-Hwan Ryu. "Inflatable-Structure-Based Working-Channel Securing Mechanism for Soft Growing Robots". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2024.3426322>.
- Seungjoon Baek, Jaehyung Jang, Jee-Hwan Ryu. "Enhancing Maximum Stroke of Twisted String Actuators by Adjusting Twisting Ratio". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2024.3397537>.
- Huseyin Tugcan Dinc, Joong-Ku Lee, Jee-Hwan Ryu. "Model-free energy-based friction compensation for industrial collaborative robots as haptic displays". *IEEE/ASME transactions on mechatronics*. DOI: <https://doi.org/10.1109/TMECH.2024.3410330>.
- Shubhranil Sengupta, Jee-Hwan Ryu. "Design of a Knee-joint Exoskeleton to Reduce Misalignment in Both the Sagittal and Coronal Planes". *2024 IEEE International Conference on Robotics and Automation (ICRA)*. DOI: <https://doi.org/10.1109/ICRA57147.2024.10610400>.
- Sangmin Lee, Jee-Hwan Ryu. "Autonomous Vehicle Localization without Prior High-Definition Map". *IEEE Transaction on Robotics*. DOI: <https://doi.org/10.1109/TRO.2024.3392149>.
- Joong-Ku Lee, Jee-Hwan Ryu. "Optimizing Setup Configuration of a Collaborative Robot Arm-Based Bimanual Haptic Display for Enhanced Performance". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2024.3355771>.
- Han, G., Seo, D., Ryu, JH. et al. RootBot: root-inspired soft-growing robot for high-curvature directional excavation. Acta Geotech. 19, 1365–1377 (2024). DOI: <https://doi.org/10.1007/s11440-023-02073-2>.
- Relaxing Conservatism for Enhanced Impedance Range and Transparency in Haptic Interaction. IEEE Transactions on Haptics, 2024. DOI: <https://doi.org/10.1109/toh.2024.3359230>.
- H.-S. Seong, S. Farag, S.-W. Lee, I. Gaponov, and J.-H. Ryu,“Wearable robot control method based on vision-language models,”in First Workshop on Vision-Language Models for Navigationand Manipulation at ICRA 2024.

**2023**

- Nam Gyun Kim, Dongoh Seo, Shinwoo Park, Jee-Hwan Ryu. "Self-retractable soft growing robots for reliable and fast retraction while preserving their inherent advantages". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2023.3341697>.
- Seungjoon Baek, Jee-Hwan Ryu. "Tension Control of Twisted String Actuators in Variation of Stiffness and Original Length of Strings". *IEEE/ASME Transactions on Mechatronics*. DOI: <https://doi.org/10.1109/TMECH.2023.3253565>.
- Hyeonseok Seong, Zhenishbek Zhakypov, Allison Okamura, Jee-Hwan Ryu. "A TSA-Based Haptic Display with a Rhombus Structure for Rendering Linearized High Force". *International Conference on Control, Automation and Systems*. DOI: <https://doi.org/10.23919/ICCAS59377.2023.10317056>.
- Dong-Geol Lee, Nam Gyun Kim, Jee-Hwan Ryu. "High-curvature consecutive tip steering of a soft growing robot for improved target reachability". *2023 IEEE/RSJ International Conference on Intelligent Robots and Systems*. DOI: <https://doi.org/10.1109/IROS55552.2023.10341407>.
- Seong-Su Park, Huseyin Tugcan Dinc, Kwang-Hyun Lee, Jee-Hwan Ryu. "Enhancing Contact Stability in Admittance-Type Haptic Interaction Using Bidirectional Time-Domain Passivity Control". *2023 32nd IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)*. DOI: <https://doi.org/10.1109/RO-MAN57019.2023.10309365>.
- Yongjun Kim, Donghyeon Kim, Jee-Hwan Ryu. "Haptic field and force feedback generation for wheeled vehicle teleoperation on 2.5 D environments". *International Conference on Intelligent Autonomous Systems 18*. DOI: <https://doi.org/10.1007/978-3-031-44851-5_7>.
- Nam Gyun Kim, Jee-Hwan Ryu. "Reconfigurable inflated soft arms". *2023 IEEE International Conference on Robotics and Automation*. DOI: <https://doi.org/10.1109/ICRA48891.2023.10160569>.
- Nam Gyun Kim, Jee-Hwan Ryu. "A soft growing robot using hyperelastic material". *Advanced Intelligent Systems*. DOI: <https://doi.org/10.1002/aisy.202200264>.
- Error-Domain Conservativity Control to Transparently Increase the Stability Range of Time-Discretized Controllers. IEEE ICRA, 2023. DOI: <https://doi.org/10.1109/icra48891.2023.10161459>.

**2022**

- Kwang-Hyun Lee; Harsimran Singh; Thomas Hulin; Jee-Hwan Ryu. "Simultaneous Use of Autonomy Guidance Haptic Feedback and Obstacle Avoiding Force Feedback for Mobile Robot Teleoperation". *2022 22nd International Conference on Control, Automation and Systems (ICCAS)*. DOI: <https://doi.org/10.23919/ICCAS55662.2022.10003886>.
- Joong-Ku Lee, Jee-Hwan Ryu. "Learning Robotic Rotational Manipulation Skill from Bilateral Teleoperation". *2022 19th International Conference on Ubiquitous Robots (UR)*. DOI: <https://doi.org/10.1109/UR55393.2022.9826276>.
- Hyeonseok Choi, Ribin Balachandran, Jee-Hwan Ryu. "Chattering-free time domain passivity approach". *IEEE Transactions on Haptics*. DOI: <https://doi.org/10.1109/TOH.2022.3178426>.
- Younghun Cho, Giseop Kim, Sangmin Lee, Jee-Hwan Ryu. "OpenStreetMap-Based LiDAR Global Localization in Urban Environment Without a Prior LiDAR Map". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2022.3152476>.
- Jaehyung Jang, Young-Uk Song, Jee-Hwan Ryu. "Active-type continuously variable transmission system based on a twisted string actuator". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2022.3144782>.
- Hyeonseok Choi, Nam Gyun Kim, Aghil Jafari, Harsimran Singh, Jee-Hwan Ryu. "Virtual inertia as an energy dissipation element for haptic interfaces". *IEEE Robotics and Automation Letters*. DOI: <https://doi.org/10.1109/LRA.2022.3144492>.
- Method for generating real-time interactive virtual fixture for shared teleoperation in unknown environments. The International Journal of Robotics Research, 2022. DOI: <https://doi.org/10.1177/02783649221102980>.

## 특허

연구실 Publications의 특허 가운데 게시된 날짜가 2021년 10월 13일–2026년 10월 13일에 드는 1건이다. 날짜는 누리집 게시 날짜이며 출원·등록 구분은 게시되어 있지 않다. 발명자·제목·번호는 연구실 표기다.[^patent]

- February 2022 · Soft Growing Robot Having Folding Type Growing Unit (발명자 Jee-Hwan Ryu, Yong-Jae Kim, Ji-Hun Kim; 번호 10-2397825-0000 KR; 번호 뒤 날짜 표기 「5 10, 2022」)

## 과제

연구실 Projects의 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 14건이다. 기간·지원 기관·과제 이름은 연구실 표기이며 2019년에 시작한 과제도 포함한다.[^projects]

- A Study on a Soft Growing Robotic Colonoscope for Pain-Relief Insertion in Endoluminal Procedures (기간 March 1, 2025 ~ February 28, 2028; 지원 National Research Foundation of Korea, Korea Health Industry Development Institute, Naver)
- The planning on the technology development of non-stop train system for hypertube station configuration (기간 2024.12.27. - 2025.12.26.; 지원 Ministry of Land, Infrastructure and Transport (MOLIT) of the Republic of Korea)
- UWB-based Parking Lot Detection (기간 2019.3.1 ~ 2023.3.1; 지원 Ministry of SMEs and startup)
- Development of a shared autonomy control framework based on deep reinforcement learning for a dexterous dual manipulation in unstructured environment (기간 2020.04.01. - 2021.12.31.; 지원 MOTIE)
- Development of shared autonomy control framework and AI-based application technology for enhancing tasks of hyper realistic telepresence robots in unstructured environment (기간 2023.04.01. - 2026.12.31.; 지원 MOTIE)
- Development of the AI-based autonomous task planning and robot teaching solution for highly complex manufacturing assembly process (기간 2024.04.01. - 2027.12.31.; 지원 MOTIE)
- Translational Research on a Soft Upper Limb Rehabilitation Robot Driven by Twisted String Actuators (기간 2020.04.01-2021.11.30 & 2022.05.04-2023.11.30; 지원 Ministry of Health and Welfare of the Republic of Korea)
- Upper limb exoskeleton research for overhead task assistance (기간 2023.01.01. - 2023.10.31.; 지원 Samsung Heavy Industry)
- Development of a stable admittance controller for an artificial joint surgical robot (기간 2022.02.01 - 2022.12.31)
- Development of mobile robot for moving inside containers and transporting flexible robots (기간 2022.07.01 - 2024.12.31; 지원 Korea Customs Service)
- Development of a Telemedicine Booth Capable of Multi-Biometric Signal Measurement and Realistic Interaction Physical Examinations at the Level of In-Person Consultations (기간 2024.04.01. - 2026.12.31.; 지원 MOTIE)
- Assistive Suit development for enhancing agricultural task efficiency (기간 2020.01.01. - 2022.12.31.; 지원 Ministry of Agriculture and Forestry of the Republic of Korea)
- Development of a high-performance twisted string actuator based on dedicated direct drive motor for robotics applications (기간 2021.08.01. - 2025.11.31.; 지원 Ministry of National Defense of the Republic of Korea)
- A Novel Soft Growing Robot for Exploration and Rescue in Confined Environments (기간 March 1, 2020 ~ February 28, 2025; 지원 NRF)

## 수상과 선정

연구실 소식과 교수 소개에 기재된 수상·선정 8건이다. 날짜는 본문에 적힌 시상일을 우선하고 나머지는 게시 날짜다. 2022년 항목의 연도는 교수 소개의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^awards]

- 2026-06-05 · VINE 팀이 「Self-Wearing Adaptive Garments via Soft Robotic Unfurling」으로 IEEE Robotics and Automation Letters Best Paper Award를 받았다. 시상은 2026 IEEE ICRA에서 이루어졌다.
- 2026-03-30 · Sangmin Lee가 2026 Jang Young Sil Fellow Program의 Excellence Track에 선정되었다.
- 2026-02-11 · 유지환 교수가 KAIST Breakthroughs의 2025년 가을호 Readers’ Choice Award를 받았다.
- 2025-06-09 · Dongoh Seo·Nam Gyun Kim·유지환 교수의 「Inflatable-Structure-Based Working-Channel Securing Mechanism for Soft Growing Robots」가 2024 IEEE Robotics and Automation Letters Best Paper Award를 받았다. 시상은 2025 IEEE ICRA에서 이루어졌다.
- 2025-01-03 · 유지환 교수가 IEEE Robotics and Automation Society Administrative Committee의 아시아·태평양 지역 대표로 선출되었다.
- 2024-12-23 · 유지환 교수의 IEEE Fellow 선정을 알렸다. 교수 경력 소개의 적용 연도는 2025년이다.
- 2024-11-22 · 유지환 교수의 IEEE Transactions on Haptics 편집장 선임을 알렸다. 임기는 2025년 1월 시작이다.
- 2022 · 유지환 교수, KAIST special award for outstanding faculty in social service

## 소식

연구실 소식의 로봇 기술 시연 2건이다. 날짜는 게시 날짜다.[^news]

- 2026-04-03 · 미국 캘리포니아주 의회 방문단에 양팔 원격조종 시스템을 시연했다.
- 2025-04-03 · Meta 방문단에 양팔 원격조종·양팔 조립 작업·성장형 소프트 로봇의 미로 이동을 시연했다.

## 연락과 위치

- 교수 이메일: jhryu@kaist.ac.kr[^dept]
- 교수 기관 전화: 042-350-3638[^dept]
- 교수 오피스: W1-2동 3206호[^dept]
- 연구실 주소: 34141 대전광역시 유성구 대학로 291 KAIST 건설및환경공학과 W16, Interactive Robotic Systems Lab[^home]

## 각주
[^home]: IRiS Lab, Interactive Robotic Systems Laboratory, KAIST. <https://iris.kaist.ac.kr> 관측일 2026-11-06.
[^dept]: KAIST 건설및환경공학과 유지환 교수 소개. <https://cee.kaist.ac.kr/boards/view/professor/79/sc_category/1> 관측일 2026-11-06.
[^r1]: IRiS Lab, Haptics and Telerobotics. <https://iris.kaist.ac.kr/teleoperation> 관측일 2026-11-06.
[^r2]: IRiS Lab, Soft Growing Robots. <https://iris.kaist.ac.kr/soft-robot> 관측일 2026-11-06.
[^r3]: IRiS Lab, Data-Efficient Autonomous Driving Framework. <https://iris.kaist.ac.kr/autonomous> 관측일 2026-11-06.
[^r4]: IRiS Lab, Mechanical Intelligence. <https://iris.kaist.ac.kr/tsa> 관측일 2026-11-06.
[^pi]: IRiS Lab, Jee-Hwan Ryu 교수의 Career·Interests·Education·Professional Services. <https://iris.kaist.ac.kr/author/jee-hwan-ryu> 관측일 2026-11-06.
[^pubs]: IRiS Lab, Publications의 연도별 학술지·학회·특허 목록. <https://iris.kaist.ac.kr/publication> 관측일 2026-11-06.
[^patent]: IRiS Lab, Publications의 특허 상세. <https://iris.kaist.ac.kr/publication/soft-growing-robot-having-folding-type-growing-unit/> 관측일 2026-11-06.
[^oa]: OpenAlex, Jee-Hwan Ryu의 2021–2026년 논문 서지와 등록 초록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5019438521,publication_year:2021-2026> 관측일 2026-11-06.
[^members]: IRiS Lab, People·Post-docs·PhD Students·Master’s Students 및 개인 소개. <https://iris.kaist.ac.kr/people> <https://iris.kaist.ac.kr/postdocs> <https://iris.kaist.ac.kr/phds> <https://iris.kaist.ac.kr/masters> <https://iris.kaist.ac.kr/researchers> <https://iris.kaist.ac.kr/author/jaehyung-jang/> <https://iris.kaist.ac.kr/author/joong-ku-lee/> <https://iris.kaist.ac.kr/author/nam-gyun-kim/> <https://iris.kaist.ac.kr/author/hyeonseok-choi/> <https://iris.kaist.ac.kr/author/kwang-hyun-lee/> <https://iris.kaist.ac.kr/author/dong-geol-lee/> <https://iris.kaist.ac.kr/author/lev-kozlov/> <https://iris.kaist.ac.kr/author/igor-alentev/> <https://iris.kaist.ac.kr/author/juyeong-seo/> <https://iris.kaist.ac.kr/author/heejin-song/> <https://iris.kaist.ac.kr/author/sanghun-lee/> <https://iris.kaist.ac.kr/author/handong-lee/> <https://iris.kaist.ac.kr/author/shinwoo-park/> <https://iris.kaist.ac.kr/author/seong-su-park/> <https://iris.kaist.ac.kr/author/chang-nho-cho/> <https://iris.kaist.ac.kr/author/euibin-shin/> <https://iris.kaist.ac.kr/author/taeil-chung/> <https://iris.kaist.ac.kr/author/yongjun-kim/> <https://iris.kaist.ac.kr/author/hyeonseok-seong/> <https://iris.kaist.ac.kr/author/junsu-park/> <https://iris.kaist.ac.kr/author/dong-hyun-choi/> <https://iris.kaist.ac.kr/author/chaewon-kim/> <https://iris.kaist.ac.kr/author/jungyue-han/> <https://iris.kaist.ac.kr/author/manh-duc-duong/> <https://iris.kaist.ac.kr/author/junhyeong-park/> <https://iris.kaist.ac.kr/author/seungmin-lee/> <https://iris.kaist.ac.kr/author/jae-yun-hwang/> <https://iris.kaist.ac.kr/author/ivan-domrachev/> <https://iris.kaist.ac.kr/author/jihan-an/> <https://iris.kaist.ac.kr/author/donghyeon-youn/> 관측일 2026-11-06.
[^alumni]: IRiS Lab, Alumni 및 이전 구성원의 학력·진로 소개. <https://iris.kaist.ac.kr/alumni> <https://iris.kaist.ac.kr/author/seif-farag/> <https://iris.kaist.ac.kr/author/nabila-adawy/> <https://iris.kaist.ac.kr/author/donghyun-choi/> <https://iris.kaist.ac.kr/author/shubhranil-sengupta/> <https://iris.kaist.ac.kr/author/seung-lyeol-lee/> <https://iris.kaist.ac.kr/author/huseyin-tugcan-dinc/> <https://iris.kaist.ac.kr/author/sangmin-lee/> <https://iris.kaist.ac.kr/author/ji-hun-kim/> <https://iris.kaist.ac.kr/author/younghun-cho/> <https://iris.kaist.ac.kr/author/simeon-nedelchev/> <https://iris.kaist.ac.kr/author/muhammad-arshad-khan/> <https://iris.kaist.ac.kr/author/hiba-latifee/> <https://iris.kaist.ac.kr/author/bhivraj-suthar/> <https://iris.kaist.ac.kr/author/muhammad-usman/> <https://iris.kaist.ac.kr/author/zain-mehdi/> <https://iris.kaist.ac.kr/author/harsimran-singh/> <https://iris.kaist.ac.kr/author/usman-mehmood/> <https://iris.kaist.ac.kr/author/naveed-ahmed-usmani/> <https://iris.kaist.ac.kr/author/vitalii-pruks/> <https://iris.kaist.ac.kr/author/muhammad-nabeel/> <https://iris.kaist.ac.kr/author/dong-hwi-lee/> <https://iris.kaist.ac.kr/author/sangwoo-ji/> <https://iris.kaist.ac.kr/author/aghil-jafari/> <https://iris.kaist.ac.kr/author/sang-goo-jeong/> <https://iris.kaist.ac.kr/author/kwang-uk-jeong/> <https://iris.kaist.ac.kr/author/boris-gromov/> <https://iris.kaist.ac.kr/author/chan-il-lee/> <https://iris.kaist.ac.kr/author/jeon-jin-kang/> <https://iris.kaist.ac.kr/author/younguk-song/> <https://iris.kaist.ac.kr/author/dmitry-popov/> <https://iris.kaist.ac.kr/author/quang-ha-van/> <https://iris.kaist.ac.kr/author/seung-jun-lee/> <https://iris.kaist.ac.kr/author/beibei-han/> <https://iris.kaist.ac.kr/author/ildar-farkhatdinov/> <https://iris.kaist.ac.kr/author/nguyen-ba-hai/> <https://iris.kaist.ac.kr/author/jaeseok-kim/> 관측일 2026-11-06.
[^projects]: IRiS Lab, Projects and Collaborations와 과제별 수행 기간·지원 기관. <https://iris.kaist.ac.kr/project> <https://iris.kaist.ac.kr/project/page/2/> <https://iris.kaist.ac.kr/project/a-study-on-a-soft-growing-robotic-colonoscope-for-pain-relief-insertion-in-endoluminal-procedures/> <https://iris.kaist.ac.kr/project/the-planning-on-the-technology-development-of-non-stop-train-system-for-hypertube-station-configuration/> <https://iris.kaist.ac.kr/project/uwb-based-parking-lot-detection/> <https://iris.kaist.ac.kr/project/development-of-a-shared-autonomy-control-framework-based-on-deep-reinforcement-learning-for-a-dexterous-dual-manipulation-in-unstructured-environment/> <https://iris.kaist.ac.kr/project/development-of-shared-autonomy-control-framework-and-ai-based-application-technology-for-enhancing-tasks-of-hyper-realistic-telepresence-robots-in-unstructured-environment/> <https://iris.kaist.ac.kr/project/development-of-the-ai-based-autonomous-task-planning-and-robot-teaching-solution-for-highly-complex-manufacturing-assembly-process/> <https://iris.kaist.ac.kr/project/translational-research-on-a-soft-upper-limb-rehabilitation-robot-driven-by-twisted-string-actuators/> <https://iris.kaist.ac.kr/project/upper-limb-exoskeleton-research-for-overhead-task-assistance/> <https://iris.kaist.ac.kr/project/development-of-a-stable-admittance-controller-for-an-artificial-joint-surgical-robot/> <https://iris.kaist.ac.kr/project/development-of-mobile-robot-for-moving-inside-containers-and-transporting-flexible-robots/> <https://iris.kaist.ac.kr/project/development-of-a-telemedicine-booth-capable-of-multi-biometric-signal-measurement-and-realistic-interaction-physical-examinations-at-the-level-of-in-person-consultations/> <https://iris.kaist.ac.kr/project/assistive-suit-development-for-enhancing-agricultural-task-efficiency/> <https://iris.kaist.ac.kr/project/development-of-a-high-performance-twisted-string-actuator-based-on-dedicated-direct-drive-motor-for-robotics-applications/> <https://iris.kaist.ac.kr/project/a-novel-soft-growing-robot-for-exploration-and-rescue-in-confined-environments/> 관측일 2026-11-06.
[^awards]: IRiS Lab, 수상·선정 소식과 교수 Honors and Awards. <https://iris.kaist.ac.kr/post/vine-team-wins-ra-l-best-paper-award-for-the-second-year-in-a-row-at-2026-ieee-icra/> <https://iris.kaist.ac.kr/post/dr-sangmin-lee-selected-for-the-2026-jang-young-sil-fellow-program-for-his-research-on-autonomous-driving-frameworks/> <https://iris.kaist.ac.kr/post/prof-jee-hwan-ryu-receives-kaist-breakthroughs-readers-choice-award-for-soft-robotics-innovation/> <https://iris.kaist.ac.kr/post/we-wins-best-paper-award-at-icra-2025-for-innovative-soft-growing-robot-technology/> <https://iris.kaist.ac.kr/post/professor-jee-hwan-ryu-elected-to-ieee-robotics-and-automation-society-administrative-committee/> <https://iris.kaist.ac.kr/post/professor-ryu-named-ieee-fellow/> <https://iris.kaist.ac.kr/post/professor-jee-hwan-ryu-appointed-editor-in-chief-of-prestigious-ieee-transactions-on-haptics/> <https://iris.kaist.ac.kr/author/jee-hwan-ryu> 관측일 2026-11-06.
[^news]: IRiS Lab, 연구 기술 시연 소식. <https://iris.kaist.ac.kr/post/california-state-legislature-shakes-hands-with-the-future-at-iris-lab/> <https://iris.kaist.ac.kr/post/visitors-from-meta-in-iris-lab/> 관측일 2026-11-06.
[^j201]: IRiS Lab, A Study on a Soft Growing Robotic Colonoscope for Pain-Relief Insertion in Endoluminal Procedures. <https://iris.kaist.ac.kr/project/a-study-on-a-soft-growing-robotic-colonoscope-for-pain-relief-insertion-in-endoluminal-procedures/> 관측일 2026-11-06.
[^j206]: IRiS Lab, Development of the AI-based autonomous task planning and robot teaching solution for highly complex manufacturing assembly process. <https://iris.kaist.ac.kr/project/development-of-the-ai-based-autonomous-task-planning-and-robot-teaching-solution-for-highly-complex-manufacturing-assembly-process/> 관측일 2026-11-06.
[^j207]: IRiS Lab, Translational Research on a Soft Upper Limb Rehabilitation Robot Driven by Twisted String Actuators. <https://iris.kaist.ac.kr/project/translational-research-on-a-soft-upper-limb-rehabilitation-robot-driven-by-twisted-string-actuators/> 관측일 2026-11-06.
[^j208]: IRiS Lab, Upper limb exoskeleton research for overhead task assistance. <https://iris.kaist.ac.kr/project/upper-limb-exoskeleton-research-for-overhead-task-assistance/> 관측일 2026-11-06.
[^j212]: IRiS Lab, Assistive Suit development for enhancing agricultural task efficiency. <https://iris.kaist.ac.kr/project/assistive-suit-development-for-enhancing-agricultural-task-efficiency/> 관측일 2026-11-06.
[^p1]: H. T. Dinc, T. Hulin, C. Ott, J.-H. Ryu, IEEE Transactions on Haptics (2024). <https://doi.org/10.1109/toh.2024.3359230> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5019438521,publication_year:2021-2026> 관측일 2026-11-06.
[^p2]: H. T. Dinc, J.-K. Lee, J.-H. Ryu, IEEE/ASME transactions on mechatronics (2024). <https://doi.org/10.1109/tmech.2024.3410330> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/model-free-energy-based-friction-compensation-for-industrial-collaborative-robots-as-haptic-displays/> 관측일 2026-11-06.
[^p3]: D. Seo, N. G. Kim, J.-H. Ryu, IEEE Robotics and Automation Letters (2024). <https://doi.org/10.1109/lra.2024.3426322> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/inflatable-structure-based-working-channel-securing-mechanism-for-soft-growing-robots/> 관측일 2026-11-06.
[^p4]: N. G. Kim 외, J.-H. Ryu, Soft Robotics (2026). <https://doi.org/10.1177/21695172251369693> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/a-soft-growing-robotic-endoscope-for-painless-and-strain-free-insertion/> 관측일 2026-11-06.
[^p5]: S. Lee, J.-H. Ryu, IEEE Transaction on Robotics (2024). <https://doi.org/10.1109/tro.2024.3392149> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/autonomous-vehicle-localization-without-prior-high-definition-map/> 관측일 2026-11-06.
[^p6]: S. Lee, D. Choi, J.-H. Ryu, IEEE Robotics and Automation Letter (2026). <https://doi.org/10.1109/lra.2026.3653282> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/lsv-loc-lidar-to-streetview-image-cross-modal-localization/> 관측일 2026-11-06.
[^p7]: S. Baek, J.-H. Ryu, IEEE/ASME Transactions on Mechatronics (2023). <https://doi.org/10.1109/tmech.2023.3253565> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/tension-control-of-twisted-string-actuators-in-variation-of-stiffness-and-original-length-of-strings/> 관측일 2026-11-06.
[^p8]: J. Seo, J. Jang, S. Baek, J.-H. Ryu, IEEE Robotics and Automation Letters (2026). <https://doi.org/10.1109/lra.2026.3665071> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://iris.kaist.ac.kr/publication/dual-variable-radius-drum-for-transmission-ratio-linearization-and-stroke-enhancement-in-twisted-string-actuators/> 관측일 2026-11-06.

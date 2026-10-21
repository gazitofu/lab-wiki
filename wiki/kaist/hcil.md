# KAIST HCI Lab (HCIL)

**KAIST 전산학부 · 이기혁 교수**

- 분야: 인간–컴퓨터 상호작용(HCI), 새로운 입력 장치와 상호작용 기법, 가상·증강현실(VR·AR) 컨트롤러, 햅틱(촉각) 인터페이스, 노트북·마우스 입력, 시각장애인 접근성
- 대분야: 컴퓨팅·AI
- 태그: 인간–컴퓨터 상호작용[^soc][^p6], 햅틱[^p3][^p2][^p4], 가상·증강현실[^p5][^p1], 재활·보조·접근성 기술[^p8]
- 홈페이지: <https://hcil.kaist.ac.kr/>
- 근거와 출처: [KAIST HCI Lab 근거 페이지](hcil-sources.md)

> 새로운 컴퓨터에 맞는 새로운 입력 방법을 만드는 연구실이다. 손가락으로 굴리는 공이 든 VR 컨트롤러, 손목에 차는 힘 되먹임 장치, 손가락을 들어 올리는 동작을 읽는 마우스, 소리 없이 진동만으로 타자를 치게 하는 시각장애인용 스마트폰 장치처럼 하드웨어를 직접 만들어 시험한다.[^about][^p1][^p2][^p6][^p8]

## 무엇을 연구하나

랩 소개는 2015년 ACM Interactions 칼럼을 인용해, 연구실이 HCI의 여러 분야 가운데 "새로운 종류의 컴퓨터를 위한 새로운 상호작용 기법"을 주로 연구한다고 적는다. 전산학 연구실이지만, 지금 하드웨어의 한계를 넘는 설계 가능성을 찾기 위해 새 하드웨어를 만들고 기존 하드웨어를 개조한다.[^about] 연구 페이지 대신 논문 목록과 연구 소개 영상을 꾸준히 올린다.[^research] 교수는 학부 명단에 연구 분야를 인간–컴퓨터 상호작용, 인터랙션 장치와 기법으로 적는다.[^soc]

첫 번째 갈래는 **VR·AR 컨트롤러와 햅틱**이다. 가상 물체를 돌릴 때 팔 전체를 움직이는 대신 엄지와 검지로 컨트롤러 속 작은 트랙볼 두 개를 굴리게 해 팔의 움직임과 피로를 크게 줄였고,[^p1] 전자기 클러치로 손목에 세 방향 힘을 주면서도 손목을 자유롭게 움직이게 하는 장치,[^p2] 0.2 mm 나일론 실로 손가락을 눌러 단단함·무게 느낌을 바꾸는 장치,[^p3] 맨손 상호작용 때 독립적으로 움직이는 네 개의 장치로 팔뚝 피부를 당겨 힘의 방향을 전하는 장치를 만들었다.[^p4] 메뉴를 보지 않고도 고르는 VR 포인팅 기법도 내놓았다.[^p5]

두 번째 갈래는 **노트북·마우스 같은 일상 기기의 새 입력**이다. 마우스 버튼 아래 근접 센서로 손가락 높이를 읽어 화면의 겹친 층을 오가게 하는 마우스,[^p6] 노트북 손목 받침에 진동 소자 배열을 넣어 게임 상황을 손바닥으로 느끼게 하는 장치를 만들었다.[^p7] 랩 논문 목록에는 손목 받침을 미는 힘으로 단축키를 쓰는 입력, 마우스 휠, 엄지 스와이프 같은 연구도 이어진다.[^papers]

세 번째 갈래는 **접근성**이다. 시끄럽거나 사생활이 걱정되는 곳에서 소리 피드백을 쓰기 어려운 시각장애인이, 스마트폰 양옆의 압전 소자(전기를 걸면 떨리는 소자) 진동과 화면 위에 덧대 줄을 구분하게 한 촉각 덧판만으로 소리 피드백과 비슷한 속도와 정확도로 타자를 치게 했다.[^p8]

## 주요 연구 주제

### 1. VR·AR 컨트롤러와 착용형 햅틱

손가락 회전 입력, 손목 힘 되먹임, 손가락 촉감 조절, 팔뚝 피부 당김, 시선 없는 메뉴 선택.[^p1][^p2][^p3][^p4][^p5] 대표 논문 1–5.

### 2. 노트북·마우스 입력과 햅틱

손가락 들기 마우스, 손목 받침 햅틱과 입력.[^p6][^p7][^papers] 대표 논문 6, 7.

### 3. 시각장애인을 위한 촉각 입력

진동 기반 스마트폰 타자.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 정규 논문 중 교수가 마지막 저자인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [TwinSpin: A Virtual Ball in a VR Controller Enabling In-Hand 3DoF Rotation](https://doi.org/10.1145/3746059.3747735) · ACM UIST 2025 | VR 컨트롤러에 엄지와 검지로 굴리는 작은 트랙볼 두 개를 넣어, 손안의 공을 굴리듯 가상 물체를 세 방향으로 돌리게 했다. 팔을 움직이는 기존 방식보다 팔 이동 거리·회전·작업 시간이 줄고 손목·팔·어깨 피로도 덜했다. UIST 2025 Honorable Mention을 받았다.[^p1][^news] | 1저자 Changsung Lim, 마지막 저자 이기혁 |
| 2 | 2026 | [ConCon: A Wrist-Worn Clutch-Coupled Force-Feedback Device for VR Controller](https://doi.org/10.1145/3772318.3790371) · ACM CHI 2026 | 모터와 전자기 클러치로 손목에 세 방향 힘을 주는 착용형 장치. 클러치로 힘을 연속·단계·순간 해제 방식으로 조절하고, 힘을 주지 않을 때는 손목이 거의 저항 없이 움직인다. 새총·문·낚시 같은 VR 장면 6개로 사용자 시험을 했다.[^p2] | 1저자 YoungIn Kim, 마지막 저자 이기혁 |
| 3 | 2025 | [StringTouch: A Non-occlusive 3DoF Haptic Interface Using String Structures for Modulating Finger Sensations](https://doi.org/10.1145/3746059.3747658) · ACM UIST 2025 | 0.2 mm 나일론 실로 손가락을 세 방향으로 눌러, 손가락을 덮지 않고도 실제 물체(대용 물체)의 방향·단단함·무게 느낌을 바꾸는 장치. 얇은 라텍스 손가락 덮개보다 감각 구분이 나았고 일부 과제에서는 맨손과 비슷했다.[^p3] | 1저자 YoungIn Kim, 마지막 저자 이기혁 |
| 4 | 2024 | [QuadStretcher: A Forearm-Worn Skin Stretch Display for Bare-Hand Interaction in AR/VR](https://doi.org/10.1145/3613904.3642067) · ACM CHI 2024 | 손에 아무것도 끼지 않는 맨손 AR·VR에서 촉감을 주기 위해, 팔뚝을 감싼 네 개의 장치로 피부를 당기는 착용형 디스플레이를 만들었다. 20명 비교에서 기존 방식보다 힘의 방향 표현과 사실감이 뛰어났다.[^p4] | 1저자 Taejun Kim, 마지막 저자 이기혁 |
| 5 | 2024 | [Pro-Tact: Hierarchical Synthesis of Proprioception and Tactile Exploration for Eyes-Free Ray Pointing on Out-of-View VR Menus](https://doi.org/10.1145/3654777.3676324) · ACM UIST 2024 | 시야 밖의 VR 메뉴를 몸의 위치 감각으로 대략 가리키고 촉감으로 미세 조정해, 보지 않고 고르는 기법. 54개 항목에서 95% 정확도로 골랐고 피로와 멀미가 줄었다.[^p5] | 1저자 Yeonsu Kim, 마지막 저자 이기혁 |
| 6 | 2025 | [Over the Mouse: Navigating across the GUI with Finger-Lifting Operation Mouse](https://doi.org/10.1145/3706598.3713340) · ACM CHI 2025 | 버튼 아래 근접 센서로 손가락을 얼마나 들었는지 읽는 마우스와, 이를 써서 화면의 겹친 층(창 전환, 영상 미리보기, 지도 확대)을 오가는 기법. 창 전환과 영상 미리보기에서 일반 마우스보다 나았다.[^p6] | 1저자 YoungIn Kim, 마지막 저자 이기혁 |
| 7 | 2026 | [HapPalm: Providing Rich Spatio-Temporal Vibrotactile Feedback on the Palm for Laptop Gaming](https://doi.org/10.1145/3772318.3791735) · ACM CHI 2026 | 노트북 손목 받침에 4×6 진동 소자 배열 두 개를 넣어 게임 상황을 손바닥으로 느끼게 하는 장치. 11가지 진동 패턴을 만들어 검증했고, 위치감 있는 진동이 재미·몰입·사실감을 크게 높였다.[^p7] | 1저자 Yohan Yun, 마지막 저자 이기혁 |
| 8 | 2025 | [Typing Haptically: Towards Enabling Non-auditory Smartphone Text Entry with Haptic Feedback for Blind and Low Vision Users](https://doi.org/10.1145/3746059.3747801) · ACM UIST 2025 | 시각장애인이 소리 없이 진동만으로 스마트폰 타자를 치게 하는 장치(TypeHap). 스마트폰 양옆의 압전 소자로 음소 단위 진동을 주고 화면에 촉각 덧판을 붙였다. 4일 훈련 뒤 소리 피드백과 비슷한 속도와 정확도를 냈다.[^p8] | 1저자 Jisu Yim, 마지막 저자 이기혁 |

## 교수와 전문 분야

이기혁 교수는 KAIST 전산학부 교수로, 교수실은 N1동 708호다.[^soc] 메타버스대학원 참여 연구실로도 올라 있다.[^gsmv]

논문으로 보면 전문 분야는 세 갈래다.

- **새로운 입력 장치 설계**: VR 컨트롤러, 마우스, 노트북 손목 받침.[^p1][^p6][^p7]
- **착용형·휴대형 햅틱**: 손목 힘 되먹임, 손가락 촉감, 팔뚝 피부 당김.[^p2][^p3][^p4]
- **보지 않는 상호작용과 접근성**: 시선 없는 메뉴 선택, 시각장애인 진동 타자.[^p5][^p8]

## 응용 분야

대표 논문으로 보면 VR·AR 기기와 게임, 노트북·PC 입력 장치, 장애인 보조 기술에 닿아 있다.[^p1][^p7][^p8] 학생들은 2025년 ICT 챌린지 장관상을 받아 CES 2026에 참가했다.[^news] 졸업생은 삼성전자·삼성리서치·LG CNS·LG전자·현대자동차·소니 인터랙티브 엔터테인먼트·ETRI·국방과학연구소, UNIST·DGIST·울산대·버지니아대, 조지아공대·미시간대·카네기멜런대 박사과정 등으로 진출했다.[^people]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 구성원 페이지는 이름과 과정만 적는다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Yeonsu Kim | 박사과정 | 5 |
| Yohan Yun | 박사과정 | 3, 5, 6, 7 |
| Kyunghwan Kim | 박사과정 | 5 |
| YoungIn Kim | 박사과정 | 2, 3, 4, 6 |
| Wenqing Sun | 석사과정 |  |
| Martin Karastoyanov | 석사과정 |  |
| Nguyen Dinh Tuan Anh | 석사과정 |  |
| Yumeng Hou | 석사과정 |  |

## 졸업생 진로

랩 구성원 페이지의 졸업생 목록(45명)이다. 학위·시기와 진로는 랩 표기를 옮겼다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Taejun Kim | Postdoc (Aug. 2026) |  |
| Changsung Lim | M.S. (Feb. 2026) | Ph.D. student (Georgia Tech) |
| Jisu Yim | M.S. (Feb. 2025) | Ph.D. student (University of Michigan) |
| Jaehyun Kim | M.S. (Feb. 2025) | LG CNS |
| Donghyeon Ko | Postdoc (Feb. 2025) | University of Ulsan |
| Sunbum Kim | Ph.D. (Feb. 2025) | Samsung Electronics |
| Keunwoo Park | Ph.D. (Aug. 2023) | Peekaby |
| Youngbo Shim | Ph.D. (Feb. 2023) | Sony Interactive Entertainment |
| Sangyoon Lee | Ph.D. (Feb. 2023) | Samsung Electronics |
| Auejin Ham | M.S. (Feb. 2023) | BHaptics |
| Joyoung Han | M.S. (Feb. 2022) | JOYCITY |
| Youngwoo Yoon | Ph.D. (Feb. 2022) | ETRI |
| Sunggeun Ahn | Ph.D. (Feb. 2022) | Samsung Electronics |
| Eunhye Youn | Ph.D. (Feb. 2022) | Samsung Research |
| Jeongmin Son | Ph.D. (Aug. 2021) | Samsung Electronics |
| Daehwa Kim | M.S. (Feb. 2021) | Ph.D. student (CMU, HCII) |
| Jiseong Gu | Ph.D. (Feb. 2021) | Samsung Electronics |
| Jingun Jung | Ph.D. (Feb. 2021) | Samsung Electronics |
| Jaeyeon Lee | Ph.D. (Aug. 2020) | UNIST |
| Sunmin Son | M.S. (Aug. 2020) | Beyless |
| Sunjun Kim | Ph.D. (Feb. 2017) | DGIST |
| Seongkook Heo | Ph.D. (Feb. 2017) | University of Virginia |
| Jaehyun Han | Ph.D. (Aug. 2016) | Samsung Electronics |
| Sunyu Hwang | M.S. | ADD |
| Jonggi Hong | M.S. (Aug. 2014) | Univ. of Maryland |
| Seunghwan Lee | Ph.D. (Feb. 2012) | Hyundai Motors |
| Sangwon Choi | M.S. (Feb. 2012) | BHaptics |
| Jiho Yeom | M.S. (Feb. 2012) | Bunny Burnit! |
| Jinhyuk Choi | Ph.D. (Aug. 2010) | Inforience |
| Jiseok Song | M.S. (August 2009) |  |
| Yuri Ahn | M.S. (February 2009) |  |
| Jungsuk Seo | M.S. (February 2009) |  |
| Jung Min Baek | M.S. (February 2008) |  |
| Sumi Yun | M.S. (February 2008) |  |
| Hojin Kim | M.S. |  |
| Byeongsoo Kim | M.S. |  |
| Seyoung Pyo | M.S. (Aug. 2007) | Satrec Initiative |
| Seungeun Lee | M.S. (Aug. 2007) | Daum Communications |
| Jaewook Jung | M.S. (Feb. 2006) |  |
| Soolim Ryu | M.S. (Feb. 2006) | LG Electronics |
| Byoungkon Sohn | M.S. (Feb. 2006) |  |
| Jaewon Shim | M.S. (Aug. 2005) | Daewoo Electronics? |
| Misook Sohn | M.S. (Feb. 2004) |  |
| Yunkyoung Jeong | M.S. (Feb. 2004) | Samsung Electronics |
| Kyuwan Choi | M.S. (Aug. 2003) |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록에 실린 2021–2026년 논문 46편이다. 데모·짧은 논문(LBW)도 랩 게시대로 실었다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- Mukhiddin Toshpulatov, Wookey Lee, Suan Lee, Geehyuk Lee. "Real-Time Multimodal Fingertip Contact Detection via Depth and Motion Fusion for Vision-Based Human-Computer Interaction". *CVPR 2026*.
- Yubin Lee, Liwei Chan, Geehyuk Lee, Sang Ho Yoon. "CurvedTouch: Effects of Surface Curvature and Cursor Mapping Method for XR Touch Input on Curved Surface". *IMWUT 2026*.
- Wen Ying, Yeonsu Kim, Adil Rahman, Erzhen Hu, Geehyuk Lee, Seongkook Heo. "Redirected Pinch: Efficient and Comfortable Bare-Hand Interaction for 2D Windows in VR". *CHI 2026*.
- Yohan Yun, Jaehyun Kim Geehyuk Lee. "HapPalm : Providing Rich Spatio-Temporal Vibrotactile Feedback on the Palm for Laptop Gaming". *CHI 2026*.
- YoungIn Kim, Geehyuk Lee. "ConCon: A Wrist-Worn Clutch-Coupled Force-Feedback Device for VR Controller". *CHI 2026*.
- Taejun Kim, Vimal Mollyn, Riku Arakawa, Chris Harrison. "HiFiGaze: Improving Eye Tracking Accuracy Using Screen Content Knowledge". *CHI 2026. (Honorable Mention Award 🏆)*.
- Mukhiddin Toshpulatov, Furkat Safarov, Ugiloy Khojamuratova, Komoliddin Misirov, Zafar Ganiyev & Geehyuk Lee. "Adaptive feature refinement for texture-preserving single image super-resolution". *The Journal of Networks, Software Tools and Applications, Cluster Computing 2026*.

**2025**

- Yohan Yun, Jisu Yim, Geehyuk Lee. "AutoPark: Adaptive Friction Mouse Facilitating Stable Multi-touch Gesture Input". *ISS 2025 (PACM HCI)*.
- Changsung Lim, Taejun Kim, Geehyuk Lee. "TwinSpin: A Virtual Ball in a VR Controller Enabling In-Hand 3DoF Rotation". *UIST 2025. (Honorable Mention Award 🏆)*.
- Jisu Yim, Donghyeon Ko, Taeho Kim, Taejun Kim, Jonggi Hong, Geehyuk Lee. "Typing Haptically: Towards Enabling Non-auditory Smartphone Text Entry with Haptic Feedback for Blind and Low Vision Users". *UIST 2025*.
- YoungIn Kim, Jisu Yim, Yohan Yun, Donghyeon Ko, Geehyuk Lee. "StringTouch: A Non-occlusive 3DoF Haptic Interface Using String Structures for Modulating Finger Sensations". *UIST 2025*.
- Changsung Lim, Yohan Yun, Geehyuk Lee. "Demonstrating TwinSpin: A Virtual Ball in a VR Controller Enabling In-Hand 3DoF Rotation". *UIST Adjunct (Demo). (People’s Choice Honorable Mention Award 🏆)*.
- Taejun Kim, Ludwig Sidenmark, Parastoo Abtahi, Jisu Yim, YoungIn Kim, Geehyuk Lee. "Tension&Gaze: Gaze-Responsive UI Gated by Finger Tension". *UIST 2025 Adjunct (Demo)*.
- Sunbum Kim, Kyunghwan Kim, Changsung Lim, Geehyuk Lee. "Ball20: An In-Hand Near-Spherical 20-Sided Tangible Controller for Diverse Gesture Interaction in AR/VR". *CHI 2025 LBW*.
- YoungIn Kim, Yohan Yun, Taejun Kim, Geehyuk Lee. "Over the Mouse: Navigating across the GUI with Finger-Lifting Operation Mouse". *CHI 2025*.
- Sangyoon Lee, Youngbo Aram Shim, Yohan Yun, Geehyuk Lee. "ThumbSwipe: A New Input Technique for Efficient One-Handed Concurrent Touchpad Interactions". *International Journal of Human–Computer Interaction 2025, Vol 41, NO. 23. (Published online: 28 Apr 2025)*.
- Yeonsu Kim, Eunseok Song, Yohan Yun, Yubin Lee, Geehyuk Lee. "HeadsetSpace: Exploring the Design Space of VR Headset as an Input Controller". *KCC 2025*.

**2024**

- Joyoung Han, YoungIn Kim, Jinjun Jung, Keunwoo Park, Geehyuk Lee. "Effects of Waveform, Time Delay, and Vibration Axis on the Perception of Vibrotactile Compliance Illusions on Smartphone Touchscreens". *International Journal of Human-Computer Interaction (Published online: 09 Aug 2024)*.
- Yeonsu Kim, Jisu Yim, Kyunghwan Kim, Yohan Yun, Geehyuk Lee. "Pro-Tact: Hierarchical Synthesis of Proprioception and Tactile Exploration for Eyes-Free Ray Pointing on Out-of-View VR Menus". *UIST 2024*.
- Jisu Yim, Seoyeon Bae, Taejun Kim, Sunbum Kim, Geehyuk Lee. "Palmrest+: Expanding Laptop Input Space with Shear Force on Palm-Resting Area". *UIST 2024*.
- Changsung Lim, Sangyoon Lee, Geehyuk Lee. "DualPad: Exploring Non-Dominant Hand Interaction on Dual-Screen Laptop Touchpads". *UIST 2024 Adjunct (Demo)*.
- Sunbum Kim, YoungIn Kim, Geehyuk Lee. "Pressure-Based Menu Selection on a Spherical Tangible Device". *CHI 2024 LBW*.
- Yeonsu Kim, Jisu Yim, Jaehyun Kim, Kyunghwan Kim, Geehyuk Lee. "STButton: Exploring Opportunities for Buttons with Spatio-Temporal Tactile Output". *CHI 2024 Interactivity (Jury Honorable Mention Award)*.
- Taejun Kim, Youngbo Aram Shim, YoungIn Kim, Sunbum Kim, Jaeyeon Lee, Geehyuk Lee. "QuadStretcher: A Forearm-Worn Skin Stretch Display for Bare-Hand Interaction in AR/VR". *CHI 2024*.
- Sunbum Kim, Geehyuk Lee. "Evaluating an In-Hand Ball-Shaped Controller for Object Manipulation in Virtual Reality". *IEEE VR 2024*.

**2023**

- Taejun Kim, Amy Karlson, Aakar Gupta, Tovi Grossman, Jason Wu, Parastoo Abtahi, Christopher Collins, Michael Glueck, Hemant Bhaskar Surale. "STAR: Smartphone-analogous Typing in Augmented Reality". *UIST 2023*.
- Kyunghwan Kim, Geehyuk Lee. "Virtual Rolling Temple: Expanding the Vertical Input Space of a Smart Glasses Touchpad". *UIST 2023 Adjunct (Demo)*.
- Youngbo Aram Shim, Sangyoon Lee, HyeonBeom Yi, Geehyuk Lee. "ExpanStick: Augmenting Gamepad Thumbstick using Force at the Limit". *CHI Play 2023*.
- Jisu Yim, Sangyoon Lee, Geehyuk Lee. "HapticPalmrest: Haptic Feedback through the Palm for the Laptop Keyboard". *CHI 2023 LBW*.
- Sunbum Kim, Geehyuk Lee. "Virtual Trackball on VR Controller: Evaluation of 3D Rotation Methods in Virtual Reality". *CHI 2023 LBW*.
- Sunmin Son, Jingun Jung, Auejin Ham, Geehyuk Lee. "TouchWheel: Enabling Flick-and-Stop Interaction on the Mouse Wheel". *International Journal of Human-Computer Interaction (Published online: 20 Mar 2023)*.

**2022**

- Youngbo Shim, Taejun Kim, Sangyoon Lee, Sunbum Kim, Geehyuk Lee. "QuadStretch: A Forearm-wearable Skin Stretch Display for Immersive VR Experience". *SIGGRAPH Asia 2022 Emerging Technologies*.
- Sunbum Kim, Youngbo Aram Shim, Geehyuk Lee. "Exploration of Form Factor and Bimanual 3D Manipulation Performance of Rollable In-hand VR Controller". *VRST 2022*.
- Eunhye Youn, Taejun Kim, Geehyuk Lee. "WristMenu with Tactons: An Eyes- and Ears-free Menu with Tactons Describing Menu Items in the Wrist Rotation Space". *International Journal of Human-Computer Interaction. (published online: Dec 28, 2022)*.
- HyeonBeom Yi, Yeeun Shin, Sehee Lee, Eunhye Youn, Auejin Ham, Geehyuk Lee, Woohun Lee. "WonderScope: Practical Near-surface AR Device for Museum Exhibits". *ACM SIGGRAPH 2022 Emerging Technologies*.
- Youngbo Aram Shim, Taejun Kim, Geehyuk Lee. "QuadStretch: A Forearm-wearable Multi-dimensional Skin Stretch Display for Immersive VR Haptic Feedback". *CHI 2022 Interactivity. (Best Demo Award)*.
- Jeongmin Son, Sunggeun Ahn, Sunbum Kim, Geehyuk Lee. "Effect of Contact Points Feedback on Two-Thumb Touch Typing in Virtual Reality". *CHI 2022 LBW*.
- Taejun Kim, Auejin Ham, Sunggeun Ahn, Geehyuk Lee. "Lattice Menu: A Low-Error Gaze-Based Marking Menu Utilizing Target-Assisted Gaze Gestures on a Lattice of Visual Anchors". *CHI 2022*.
- Jiseong Gu, Geehyuk Lee. "Towards More Direct Text Editing with Handwriting Interfaces". *International Journal of Human Computer Interaction. (Published online: 18 Apr 2022)*.

**2021**

- Joyoung Han, Geehyuk Lee. "Finding a More Pleasant Compliance Illusion Method for a Hand-Held Device. IEEE Access, vol 9, Dec 2021. [DOI]". **.
- Youngwoo Yoon\*, Keunwoo Park\*, Minsu Jang, Jaehong Kim, Geehyuk Lee. "SGToolkit: An Interactive Gesture Authoring Toolkit for Embodied Conversational Agents". *UIST 2021. [DOI] [Video]*.
- Eunhye Youn, Sangyoon Lee, Sunbum Kim, Youngbo Aram Shim, Liwei Chan, Geehyuk Lee. "WristDial: An Eyes-Free Integer-Value Input Method by Quantizing the Wrist Rotation". *International Journal of Human-Computer Interaction. [DOI]*.
- Daehwa Kim, Keunwoo Park, Geehyuk Lee. "AtaTouch: Robust Finger Pinch Detection for a VR Controller Using RF Return Loss". *CHI 2021. [DOI] [Video] [Project] (Honorable Mention Award)*.
- Jingun Jung, Sunmin Son, Sangyoon Lee, Yeonsu Kim, Geehyuk Lee. "ThroughHand: 2D Tactile Interaction to Simultaneously Recognize and Touch Multiple Objects". *CHI 2021. [DOI] [Video] (Honorable Mention Award)*.
- Taejun Kim, Youngbo Aram Shim, Geehyuk Lee. "Heterogeneous Stroke: Using Unique Vibration Cues to Improve the Wrist-Worn Spatiotemporal Tactile Display". *CHI 2021. [DOI] [Video]*.
- Sunggeun Ahn, Stephanie Santosa, Mark Parent, Daniel Wigdor, Tovi Grossman, and Marcello Giordano. "StickyPie: A Gaze-Based, Scale-Invariant Marking Menu Optimized for AR/VR". *CHI 2021. (Internship project with Chatham Labs) [DOI] [Video]*.

## 소식

랩 첫 화면의 최근 소식(원문)이다.[^news]

- May 7, 2026 · Yeonsu, Kyunghwan, Yohan presents at ITRC 인재양성대전 2026
- April 6, 2026 · HiFiGaze Received Honorable Mention Award at CHI 2026
- April 6, 2026 · Yohan presents HapPalm at CHI 2026
- April 6, 2026 · YoungIn presents ConCon at CHI 2026
- April 6, 2026 · Taejun presents HiFiGaze at CHI 2026
- April 6, 2026 · Journal published to Cluster Computing 2026
- February 1, 2026 · HCIL at CES conference 2026!
- October 2, 2025 · TwinSpin received People’s Choice Honorable Mention Award for UIST 2025 Demos
- October 1, 2025 · TwinSpin Received Honorable Mention Award at UIST 2025
- September 19, 2025 · We are recruiting Master’s students for Spring 2026.

## 연락과 위치

- 교수 이메일: geehyuk@kaist.ac.kr[^about]
- 연구실 전화: 042-350-7757[^about]
- 교수실: KAIST N1동 708호, 전화 042-350-3557[^soc]
- 연구실: KAIST N1동 722호 (대전 유성구 대학로 291)[^about]

[^about]: 랩 소개·연락처 페이지(About) <https://hcil.kaist.ac.kr/about/> (2026-10-19 열람)
[^research]: 랩 연구 페이지 <https://hcil.kaist.ac.kr/research/> (2026-10-19 열람)
[^people]: 랩 구성원 페이지(People) <https://hcil.kaist.ac.kr/people/> (2026-10-19 열람)
[^papers]: 랩 논문 목록 <https://hcil.kaist.ac.kr/publications/> (2026-10-19 열람)
[^news]: 랩 첫 화면 소식 <https://hcil.kaist.ac.kr/> (2026-10-19 열람)
[^soc]: KAIST 전산학부 교수 명단 <https://cs.kaist.ac.kr/people/faculty> (2026-10-20 열람)
[^gsmv]: KAIST 메타버스대학원 참여 연구실 페이지(HCIL) <https://meta.kaist.ac.kr/labs/hcil> (2026-10-19 열람)
[^p1]: C. Lim, T. Kim, G. Lee, Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology, 1-13 (온라인 2025-09-27). <https://doi.org/10.1145/3746059.3747735> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: Y. Kim, G. Lee, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-17 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3790371> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Y. Kim 외, G. Lee, Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology, 1-14 (온라인 2025-09-27). <https://doi.org/10.1145/3746059.3747658> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: T. Kim 외, G. Lee, Proceedings of the CHI Conference on Human Factors in Computing Systems, 1-15 (온라인 2024-05-11). <https://doi.org/10.1145/3613904.3642067> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Kim 외, G. Lee, Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology, 1-11 (온라인 2024-10-11). <https://doi.org/10.1145/3654777.3676324> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. Kim, Y. Yun, T. Kim, G. Lee, Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, 1-14 (온라인 2025-04-25). <https://doi.org/10.1145/3706598.3713340> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y. Yun, J. Kim, G. Lee, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-20 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3791735> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: J. Yim 외, G. Lee, Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology, 1-16 (온라인 2025-09-27). <https://doi.org/10.1145/3746059.3747801> 초록 기준(Semantic Scholar 등록 초록).

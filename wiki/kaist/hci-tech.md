# HCI Tech Lab (Human-Centered Interactive Technologies Laboratory)

**KAIST 문화기술대학원 · 윤상호 교수**

- 분야: 인간–컴퓨터 상호작용(HCI), 햅틱(촉각) 기술, 확장현실(XR) 입력, 착용형 센싱, 생성형 AI 기반 디자인 도구
- 대분야: 컴퓨팅·AI
- 태그: 햅틱[^p4][^p3][^p2], 가상·증강현실[^p5][^p8], 인간–컴퓨터 상호작용[^ct][^p6][^p8], 생성 인공지능[^p1][^p7], 인간–로봇 상호작용[^projects], 재활·보조·접근성 기술[^p7]
- 홈페이지: <https://hcitech.org/>
- 근거와 출처: [HCI Tech Lab 근거 페이지](hci-tech-sources.md)

> 사람이 가상현실과 컴퓨터를 손과 몸으로 더 자연스럽게 다루도록, 손끝에 촉감을 주는 장갑과 장치, 몸의 움직임을 읽는 센서, 진동 패턴을 글로 만들어 주는 인공지능 같은 상호작용 기술을 만든다.[^home][^p1][^p4]

## 무엇을 연구하나

연구실은 물리 세계와 디지털 세계를 잇는 체화 지능(몸을 가진 기계가 현실과 상호작용하는 인공지능, 피지컬 AI)과 몰입형 기술(XR)로 사람의 잠재력을 키우는 것을 목표로 내건다. 주요 연구 주제는 첨단 센싱 기술, 다중 감각 햅틱 기술, 사용자 경험 저작 도구다.[^home] 교수는 HCI, 햅틱, 상호작용 기법, 착용형 컴퓨팅, 확장현실을 연구 분야로 적는다.[^ct]

첫 번째 갈래는 **햅틱, 곧 촉감을 만드는 기술**이다. 가상현실에서 물건을 잡아도 손에 아무 느낌이 없으면 실감이 떨어진다. 연구실은 손가락 마디마다 정전기 브레이크로 힘을 걸어 물체 모양을 느끼게 하는 130 g 장갑,[^p4] 두 지점만 눌러도 압력이 손 위를 움직이는 듯 느끼게 하는 장치,[^p3] 손가락 힘줄에 진동을 줘 손가락이 움직이는 듯한 착각을 일으키는 방법을 만들었다.[^p2]

두 번째 갈래는 **확장현실 입력과 착용형 센싱**이다. 맨손으로 가상현실 자판을 칠 때 손끝에 초음파로 공중 촉감을 주는 착용형 장치로 입력 자신감과 사용성을 높였고,[^p5] 랩 학술지 목록에는 시선과 손가락 동작을 결합한 입력, 굽은 표면 위 터치 입력 연구도 많다.[^papers]

세 번째 갈래는 **생성형 AI 기반 디자인·저작 도구**다. 글로 원하는 느낌을 쓰면 진동 신호를 만들어 주는 생성 모델,[^p1] 가상 물체의 어느 부분을 어떻게 잡고 움직일지 추천해 주는 시각–언어 모델 도구,[^p6] 집 안 물건과 환자 사진으로 맞춤 재활 운동을 짜 주는 모델,[^p7] 안무가가 가상현실 안에서 춤을 만들 때 동작을 제안하고 분석해 주는 도구를 내놓았다.[^p8]

## 주요 연구 주제

### 1. 착용형 햅틱 장치와 촉각 착각

정전기 브레이크 장갑, 압력 착각, 힘줄 진동, 초음파 공중 촉각.[^p2][^p3][^p4][^p5] 대표 논문 2, 3, 4, 5.

### 2. 생성형 AI와 창작·재활 도구

텍스트–진동 생성, 손–물체 상호작용 저작, 재활 운동 계획, 안무 창작 지원.[^p1][^p6][^p7][^p8] 대표 논문 1, 6, 7, 8.

### 3. XR 입력과 피지컬 AI

시선·손 입력, 맥락 인지 인간–로봇 상호작용. 연구실은 2026년부터 한국연구재단 우수신진연구로 "공존형 인간–로봇 상호작용을 위한 맥락 인지 멀티모달 피지컬 AI" 과제를 이끈다.[^projects][^papers]

## 대표 논문

랩 논문 목록의 2021–2026년 동료 심사 논문 중 교수가 마지막 저자인 것에서 주제별로 골랐다(1번은 랩 목록의 공동 마지막 저자 표기). "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [HapticGen: Generative Text-to-Vibration Model for Streamlining Haptic Design](https://doi.org/10.1145/3706598.3713609) · ACM CHI 2025 | 글로 원하는 느낌을 입력하면 진동 신호를 만들어 주는 생성 모델. 소리 33만 5천 개를 진동으로 바꾼 자료로 학습하고 전문 디자이너의 평가로 다시 조정했다. 32명 비교 실험에서 사실감 등 다섯 가지 체험 지표와 사용성이 기존 방식보다 좋았다.[^p1] | 공동 1저자 Youjin Sung·Kevin John, 윤상호·Hasti Seifi(랩 목록 ** 표기) |
| 2 | 2026 | [Finger Tendon Vibration: Finger Movement Illusions for Immersive Virtual Object Interaction](https://doi.org/10.1145/3772318.3790557) · ACM CHI 2026 | 손가락 힘줄에 진동을 주면 손가락이 움직이는 듯한 착각이 생긴다. 이를 가상 물체 상호작용에 쓰는 6가지 장면과 4가지 진동 방식을 설계·평가해 지침을 만들었고, 손가락에 실제 같은 저항감을 줘 "내 손" 같은 느낌을 크게 높였다.[^p2] | 1저자 Kun-Woo Song, 마지막 저자 윤상호 |
| 3 | 2025 | [Moving-Press: Pressure-based Moving Phantom Sensation for Immersive VR Hand Interaction](https://doi.org/10.1145/3770682) · ACM IMWUT | 고정된 두 개의 구동기로 누르는 깊이를 시간에 따라 바꾸면, 압력이 손 위를 연속으로 움직이는 듯한 착각(움직이는 유령 감각)이 생긴다는 것을 보이고 이를 쓰는 착용형 장치를 만들었다. 부피가 큰 압력 장치를 작게 만들 수 있는 방법이다.[^p3] | 공동 1저자 DongKyu Kwak·Kyungjin Seo, 마지막 저자 윤상호 |
| 4 | 2024 | [EStatiG: Wearable Haptic Feedback with Multi-Phalanx Electrostatic Brake for Enhanced Object Perception in VR](https://doi.org/10.1145/3678567) · ACM IMWUT | 손끝뿐 아니라 손가락 마디마다 힘 되먹임을 주는 130 g 햅틱 장갑. 정전기 클러치를 겹쳐 마디별 브레이크를 만들었고, 가상 물체를 쥘 때 손가락 각도 인식과 사실감·몰입감이 크게 좋아졌다.[^p4] | 공동 1저자 Nicha Vanichvoranun·Hojeong Lee, 마지막 저자 윤상호 |
| 5 | 2025 | [UltraBoard: Always-available Wearable Ultrasonic Mid-air Haptic Interface for Responsive and Robust VR Inputs](https://doi.org/10.1145/3731413) · ACM IMWUT | 손에 다는 초음파 위상 배열(여러 초음파 소자의 박자를 맞춰 한 점에 음압을 모으는 장치)로 손끝을 포함한 손 전체에 공중 촉감을 주는 장치. 손 위치에 맞춰 배열을 움직여 가상현실 타자 때 촉감을 꾸준히 주고, 오타를 촉감으로 알려 입력 자신감과 사용성을 높였다.[^p5] | 1저자 Changhyeon Park, 마지막 저자 윤상호 |
| 6 | 2026 | [HOICraft: In-Situ VLM-based Authoring Tool for Part-Level Hand-Object Interaction Design in VR](https://doi.org/10.1145/3772318.3790823) · ACM CHI 2026 | 가상현실에서 물체의 어느 부분을 어떻게 잡고 움직일지 정하는 손–물체 상호작용 설계를, 시각–언어 모델(이미지와 글을 함께 이해하는 인공지능)이 상호작용할 부분을 추천하고 손 움직임과 물체 동작을 연결해 주는 도구로 도왔다. 디자이너 12명 실험에서 시행착오가 크게 줄었다.[^p6] | 1저자 Dohui Lee, 마지막 저자 윤상호 |
| 7 | 2026 | [RehabGen: Generative Expert-in-the-Loop Vision-Language Model for Everyday Contextualized Rehabilitation Exercises](https://doi.org/10.1145/3810235) · ACM IMWUT | 환자 시점 사진과 집 안 물건을 보고 맞춤 재활 운동을 짜 주는 시각–언어 모델. 전문가 의견으로 만든 선호 자료로 모델을 조정했고, 전문가 23명 평가에서 기본 모델보다 항목 단위 선호율 57.6%를 기록했다.[^p7] | 1저자 Youjin Sung, 마지막 저자 윤상호 |
| 8 | 2025 | [ChoreoCraft: In-situ Crafting of Choreography in Virtual Reality through Creativity Support Tool](https://doi.org/10.1145/3706598.3714220) · ACM CHI 2025 | 안무가가 가상현실 안에서 춤을 만들 때 상황에 맞는 동작을 제안하고 안무를 분석해 주는 도구. 창작의 정체를 넘고 기억 부담을 줄이며 효율을 높였다.[^p8] | 공동 1저자 Kyungeun Jung·Hyunyoung Han(랩 표기), 마지막 저자 윤상호 |

## 교수와 전문 분야

윤상호 교수는 미국 카네기멜런대에서 기계공학 학사·석사(2004–2008), 퍼듀대에서 기계공학 박사(2013–2017)를 받았다.[^ct] LG디스플레이 연구원(2008–2010), LG전자 주임연구원(2010–2013), 마이크로소프트 응용과학연구소 연구 엔지니어(2017–2020), 삼성전자 삼성리서치 수석연구원(2020–2021)을 거쳐 2021년 9월 KAIST 문화기술대학원에 부임했고 지금은 부교수다.[^ct] 전산학부·메타버스대학원·로봇공학 학제전공·AX학과 겸임교수다.[^people]

논문으로 보면 전문 분야는 세 갈래다.

- **착용형 햅틱 하드웨어**: 장갑형 힘 되먹임, 촉각 착각, 초음파 촉각.[^p2][^p3][^p4][^p5]
- **AI 기반 상호작용 설계 도구**: 진동 생성, 상호작용 저작, 재활·창작 지원.[^p1][^p6][^p7][^p8]
- **확장현실 입력 기법**: 시선·손 입력과 착용형 센싱.[^papers]

## 응용 분야

대표 논문과 과제로 보면 가상현실 게임·협업, 착용형 기기와 촉각 장갑, 재활 의료, 공연 예술 창작, 인간–로봇 공존 환경에 닿아 있다.[^p4][^p7][^p8][^projects] 2026년 ISMAR에서 최우수 논문상(Best Paper Award)과 Honorable Mention을 받았다.[^home] 졸업생은 KAIST 박사후연구원, 삼성전자, PIT IN AI 로봇팀 등으로 진출했고 상당수가 같은 연구실 박사과정으로 이어졌다.[^people]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다. 구성원 페이지는 이메일과 시작 시점을 적지 않는다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Jinwook Kim | 박사후연구원 | Multimodal Interaction |  |
| Youjin Sung | 박사과정 | Multimodal Human-AI Interaction | 1, 7 |
| Jina Kim | 박사과정 | Multimodal interaction & Sensing for XR |  |
| Kyungeun Jung | 박사과정 | Motion-Aware Haptic Interaction | 8 |
| Min-yung Kim | 박사과정 | Multimodal Interactions |  |
| Dong Kyu Kwak | 박사과정 | Wearable Haptic Devices | 3 |
| Soyeong Yang | 박사과정 | Viscoelastic Haptic Rendering |  |
| Hyung Il Yi | 박사과정 |  |  |
| Kun-Woo Song | 박사과정 |  | 2 |
| Hojeong Lee | 박사과정 | Haptics, Soft Actuator | 4 |
| Hanseok Jeong | 박사과정 | AI-based Sensing Technology |  |
| Hyung Wook Yi | 박사과정 | Sensor Fabrication & Toolkit |  |
| Kyoungwhan Mheen | 박사과정 | Eye & Hand Interaction |  |
| Dohui Lee | 박사과정 | Human-Centered XR Interaction with AI | 6 |
| Minju Baeck | 박사과정 | (Co-advised by Prof. Woontack Woo) |  |
| Kyungjin Seo | 박사과정 | (On leave, working@ Samsung Global Research Tech & Experience Team) | 3 |
| Changhyeon Park | 석사과정 | Sensing & Haptics Interaction | 5 |
| Rachel Jungmin Kim | 석사과정 |  | 3 |
| Murad Eynizada | 석사과정 |  |  |
| Youngrae Kim | 석사과정 | AI-driven Haptic Effects Generation | 2 |
| Eun Ho Kim | 석사과정 |  |  |
| Donghee Hyun | 석사과정 |  |  |
| HyeongJin Do | 석사과정 | Haptics, AI-based sensing |  |
| Hyunwook Jung | 석사과정 | Human-Centered XR Interaction with AI |  |
| Yejin Jang | 석사과정 | Haptics |  |
| Eun Ji Shin | 학부 연구생 |  |  |
| Nahyeong Kim | 행정 직원 |  |  |
| EunJi Cho | 행정 직원 |  |  |

## 졸업생 진로

랩 구성원 페이지의 대학원 졸업생 목록이다. 기간과 진로는 랩 표기를 옮겼다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seo Young Oh | Ph.D. Student (Co-advised) (Fall 2023 - Summer 2026) | PostDoc, KAIST |
| Fangqing Li | M.S. Student (Fall 2023 - Summer 2026) |  |
| Hanseok Jeong | M.S. Student (Spring 2024 - Winter 2026) | Ph.D Student @ HCI Tech Lab, KAIST |
| Yubin Lee | M.S. Student (Spring 2024 - Winter 2026) |  |
| Hyung Wook Yi | M.S. Student (Fall 2023 - Winter 2026) | Ph.D Student @ HCI Tech Lab, KAIST |
| Hojeong Lee | M.S. Student (Fall 2023 - Summer 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Kun-woo Song | M.S. Student (Fall 2023 - Summer 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Hyunyoung Han | M.S. Student (Fall 2023 - Summer 2025) | Ph.D. Student @ WIT Lab, KAIST |
| Dongkyu Kwak | M.S. Student (Spring 2023 - Winter 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Soyeong Yang | M.S. Student (Spring 2023 - Winter 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Min-yung Kim | M.S. Student (Spring 2023 - Winter 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Hyung Il Yi | M.S. Student (Spring 2023 - Winter 2025) | Ph.D Student @ HCI Tech Lab, KAIST |
| Junghoon Seo | M.S. Student (Spring 2023 - Winter 2025) | Principal Researcher @ PIT IN AI Robot Team |
| Nicha Vanichvoranun | M.S. Student (Summer 2022 - Summer 2024) | Staff Engineer @ Samsung Electronics |
| Kyungeun Jung | M.S. Student (Winter 2022 - Summer 2024) | Ph.D Student @ HCI Tech Lab, KAIST |
| Kyungjin Seo | M.S. Student (Fall 2022 - Summer 2024) | Ph.D Student @ HCI Tech Lab, KAIST |
| Jina Kim | M.S. Student (Winter 2022 - Summer 2024) | Ph.D Student @ HCI Tech Lab, KAIST |
| Youjin Sung | M.S. Student (Spring 2022 - Summer 2023) | Ph.D Student @ HCI Tech Lab, KAIST |
| Minjae Jo | M.S. Student (Spring 2022 - Winter 2023) |  |

## 최근 논문 목록 (2022–2026)

랩 논문 목록의 동료 심사 학술대회·학술지 논문 45편이다(포스터·데모·투고 중 논문 제외). 서지는 랩 표기를 옮겼고, \*는 랩이 붙인 공동 1저자 또는 공동 교신 표시다.[^papers] 대표 논문은 위 표에서 쉬운 설명을 붙였다.

**2026**

- Jina Kim, Eric J Gonzalez, Yang Zhang, Sang Ho Yoon. "GazeTune: Facilitating Precise Gaze-Driven Interactions with Cascaded Touch Input". *ACM UIST 2026*.
- Rachel Kim, Xun Qian\*, Sang Ho Yoon\*. "DOBI: Dynamic Opportunistic Body Input via Spare Joint Recruitment for Hands-Free XR". *ACM UIST 2026*.
- Kyoungwhan Mheen, Jinwook Kim\*, Sang Ho Yoon\*. "UniScale: Exploring Unimanual Gesture Mapping Strategies for Gaze+Pinch-based Scaling Interaction". *IEEE Transactions on Visualization and Computer Graphics (TVCG/ISMAR2026)*.
- Minju Baeck, Yoonseok Shin, Hyunjin Lee, Boram Yoon, Woontack Woo\*, Sang Ho Yoon\*. "Sharing Roughness with Hand-Outline Visualization to Reduce Sensory Asymmetry in VR Collaboration". *IEEE Transactions on Visualization and Computer Graphics (TVCG/ISMAR2026) (Best Paper Award)*.
- Seo Young Oh, Taejun Son, Jooyoung Lee, Woontack Woo\*, Sang Ho Yoon\*. "GeoCtrl: Finger-based Geometric Mapping and Speed-Adaptive Gain for In-Hand Object Rotation in AR/VR". *IEEE ISMAR 2026*.
- Sungwon In, Minju Baeck, Yalong Yang, Sang Ho Yoon, Woontack Woo, Mallesham Dasari. "Understanding Organizational Strategies Across Multimodal Artifacts in Immersive Computational Notebooks". *IEEE ISMAR 2026 (Honorable Mention Award)*.
- Hyung Il Yi, Hyung Wook Yi, Sang Ho Yoon. "Thermal Crossing: Palm-Free Thermal Rendering with Thermal Illusions". *ACM ISWC Notes and Briefs (UbiComp/ISWC 2026)*.
- Daegeun Park, Hojeong Lee, Sang Ho Yoon, Sung-Uk Jung. "A Novel Flexible Shaft-driven Mechanism for Multidirectional Active Force Feedback in Haptic Gloves: A Preliminary Study". *IEEE Robotics and Automation Letters (RA-L)*.
- Youjin Sung, Heejin Jeong, Xuhai "Orson" Xu, Sang Ho Yoon. "RehabGen: Generative Expert-in-the-Loop Vision-Language Model for Everyday Contextualized Rehabilitation Exercises". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2026)*.
- Yubin Lee, Liwei Chan, Geehyuk Lee, Sang Ho Yoon. "CurvedTouch: Effects of Surface Curvature and Cursor Mapping Method for XR Touch Input on Curved Surface". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2026)*.
- Hojeong Lee, Eunho Kim, Rachel Kim, Sang Ho Yoon. "VibGrasp: Spatiotemporal Vibration Based Multimodal Haptic Rendering with a Lightweight Exo-Glove for 3D Shape Perception". *IEEE Transactions on Haptics (TOH)*.
- Min-yung Kim, Jinwook Kim, Ken Pfeuffer, Sang Ho Yoon. "Align-to-Scale: Mode Switching Technique for Unimanual 3D Object Manipulation with Gaze-Hand-Object Alignment in Extended Reality". *Proceedings of the ACM on Computer Graphics and Interactive Techniques (ETRA26)*.
- Dohui Lee, Qi Sun, Sang Ho Yoon. "HOICraft: In-Situ VLM-based Authoring Tool for Part-Level Hand-Object Interaction Design in VR". *ACM CHI 2026*.
- Kun-Woo Song, Youngrae Kim, Sang Ho Yoon. "Finger Tendon Vibration: Finger Movement Illusions for Immersive Virtual Object Interaction". *ACM CHI 2026*.
- Soyeong Yang, Sang Ho Yoon. "AquaHaptics: Hand-based Multimodal Haptic Interactions for Immersive Virtual Underwater Experience". *IEEE Transactions on Visualization and Computer Graphics (TVCG)*.
- Seo Young Oh, Junghoon Seo, Juyoung Lee, Boram Yoon, Woontack Woo\*, Sang Ho Yoon\*. "ForceCtrl: Hand-Raycasting with User-Defined Pinch Force for Control-Display Gain Application". *IEEE Transactions on Visualization and Computer Graphics (TVCG)*.

**2025**

- Dongkyu Kwak\*, Kyungjin Seo\*, Rachel Kim, Sang Ho Yoon. "Moving-Press: Pressure-based Moving Phantom Sensation for Immersive VR Hand Interaction". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2026)*.
- Hyung Il(IL) Yi\*, Kun-Woo Song\*, Nihar Sabnis, Andrea Bianchi, Sang Ho Yoon. "InvisiBow: Finger-Held Device for Bimanual Haptic Illusions during Virtual Archery". *ACM ISWC Notes and Briefs (UbiComp/ISWC 2025)*.
- Minju Baeck, Yoonseok Shin, Dooyoung Kim, Hyunjin Lee, Woontack Woo\*, Sang Ho Yoon\*. "Visuo-Tactile Feedback with Hand Outline Styles for Modulating Affective Roughness Perception". *IEEE Transactions on Visualization and Computer Graphics (TVCG/ISMAR2025) (Best Paper Award)*.
- Kun-Woo Song, Sang Ho Yoon. "Neck Goes VRrr: Reducing Rotation-Induced Virtual Reality Sickness through Neck Muscle Vibrations". *IEEE Transactions on Visualization and Computer Graphics (TVCG/ISMAR2025)*.
- Hojeong Lee, Eun Ho Kim, Sang Ho Yoon. "3D Shape Perception through Spatiotemporal Vibrotactile Patterns with Kinesthetic Feedback". *IEEE WHC2025*.
- Changhyeon Park, Yubin Lee, Sang Ho Yoon. "UltraBoard: Always-Available Wearable Ultrasonic Mid-air Haptic Interface for Responsive and Robust VR Inputs". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2025)*.
- Wonseok Roh, Hwanhee Jung, Giljoo Nam, , Dong In Lee, Hyeongcheol Park, Sang Ho Yoon, Jungseock Joo, Sangpil Kim. "Insightful Instance Features for 3D Instance Segmentation". *IEEE CVPR 2025*.
- Jina Kim, Yang Zhang, Sang Ho Yoon. "T2IRay: Design of Thumb-to-Index based Indirect Pointing for Continuous and Robust AR/VR Input". *ACM CHI 2025 (Honorable Mention Award)*.
- Kyungeun Jung\*, Hyunyoung Han\*, Sang Ho Yoon. "ChoreoCraft: In-situ Crafting of Choreography in Virtual Reality through Creativity Support Tool". *ACM CHI 2025 (Honorable Mention Award)*.
- Youjin Sung\*, Kevin John\*, Hasti Seifi\*\*, Sang Ho Yoon\*\*. "HapticGen: Generative Text-to-Vibration Model for Streamlining Haptic Design". *ACM CHI 2025*.
- Shih Ying-Lei, Tang Dongxu, Weiming Hu, Sang Ho Yoon, Yitian Shao. "VibWalk: Mapping Lower-limb Haptic Experiences of Everyday Walking". *ACM CHI 2025*.
- Sieun Kim, Jaehwan Jeong, Sumin In, Seung Hyun Lee, Seungryong Kim, Saerom Kim, Wooyeol Baek, Sang Ho Yoon, Eugenio Culurciello, Sangpil Kim. "Semantically complex audio to video generation with audio source separation". *Engineering Applications of Artificial Intelligence*.
- Gyeongrok Oh, Sungjune Kim, Heon Gu, Sang Ho Yoon, Jinkyu Kim, Sangpil Kim. "FPANet: Frequency-based video demoireing using frame-level post alignment". *Neural Networks*.
- Jaehwan Jeong, Sumin In, Sieun Kim, Hannie Shin, Jongheon Jeong, Sang Ho Yoon, Jaewook Chung, Sangpil Kim. "FaceShield: Defending Facial Image against Deepfake Threats". *ICCV2025*.
- Seunggwan Lee, Hwanhee Jung, ByoungSoo Koh, Qixing Huang, Sang Ho Yoon, Sangpil Kim. "PASTA: Part-Aware Sketch-to-3D Shape Generation with Text-Aligned Prior". *ICCV2025*.

**2024**

- Kyungjin Seo\*, Junghoon Seo\*, Hanseok Jeong, Sangpil Kim, Sang Ho Yoon. "Posture-Informed Muscular Force Learning for Robust Hand Pressure Estimation". *NeurIPS 2024*.
- Nicha Vanichvoranun\*, Hojeong Lee\*, Seoyeon Kim, Sang Ho Yoon. "EStatiG: Wearable Haptic Feedback with Multi-Phalanx Electrostatic Brake for Enhanced Object Perception in VR". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2024)*.
- Hyung Il Yi, Hojeong Lee, Sang Ho Yoon. "ThermicVib: Enabling Dynamic Thermal Sensation with Multimodal Haptic Glove for Thermal-Responsive Interaction". *IEEE ISMAR 2024*.
- Seunghyun Lee, Seung Hyun Lee, Sieun Kim, Wonmin Byeon, Gyeongrok Oh, Sumin In, Hyeongcheol Park, Sang Ho Yoon, Sung-hee Hong, Jinkyu Kim\*, Sangpil Kim\*. "Audio-Guided Implicit Neural Representation for Local Image Stylization". *Computational Visual Media*.
- Youjin Sung, Rachel Kim, Kun Woo Song, Yitian Shao, Sang Ho Yoon. "HapticPilot: Authoring In-situ Hand Posture-Adaptive Vibrotactile Feedback for Virtual Reality". *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT, UbiComp/ISWC 2024)*.
- Kyungeun Jung, Sangpil Kim, Seungjae Oh\*, Sang Ho Yoon\*. "HapMotion: Motion-to-Tactile Framework with Wearable Haptic Devices for Immersive VR Performance Experience". *Springer Virtual Reality*.
- Seunghyun Lee, Hyung-gun Chi, Wonmin Byeon, Gyeongrok Oh, Sang Ho Yoon, Hyunje Park, Wonjun Cho, Jinkyu Kim, Sangpil Kim. "Robust Sound-Guided Image Manipulation". *Neural Networks*.
- Wonseok Roh, Hwanhee Jung, Giljoo Nam, Jinseop Yeom, Hyunje Park, Sang Ho Yoon, Sangpil Kim. "Edge-Aware 3D Instance Segmentation Network with Intelligent Semantic Prior". *IEEE CVPR 2024*.

**2023**

- Jina Kim, Min-Yung Kim, Woosuk Lee, Sang Ho Yoon. "VibAware: Context-Aware Tap and Swipe Gestures Using Bio-Acoustic Sensing". *ACM SUI 2023*.
- Minjae Jo, DongKyu Kwak, Sang Ho Yoon. "WriMouCon: Wrist-Mounted Haptic Controller for Rendering Physical Properties in Virtual Reality". *IEEE WHC 2023*.
- Kyungeun Jung, Sang Ho Yoon. "Mo2Hap: Rendering VR Performance Motion Flow to Upper-body Vibrotactile Haptic Feedback". *ACM UIST Demo 2023*.

**2022**

- Seung Hyun Lee, Gyeongrok Oh, Wonmin Byeon, Jihyun Bae, Chanyoung Kim, Won Jeong Ryoo, Sang Ho Yoon, Jinkyu Kim, Sangpil Kim. "Sound-Guided Semantic Video Generation". *Springer ECCV 2022*.
- Hyuckjin Jang, Taehei Kim, Seoyoung Oh, Jeongmi Lee, Sunghee Lee, Sang Ho Yoon. "Sense of Embodiment Inducement for People With Reduced Lower-body Mobility and Sensations With Partial-visuomotor Stimulation". *ACM SIGGRAPH Emerging Technologies 2022*.
- Seunghyun Lee, Wonseok Roh, Wonmin Byeon, Sang Ho Yoon, Chanyoung Kim, Jinkyu Kim, Sangpil Kim. "Sound-Guided Semantic Image Manipulation". *IEEE CVPR 2022*.

## 연구 과제

랩 과제 페이지의 연구실 과제(진행 10건, 완료 8건)다.[^projects]

- Context-Aware Multimodal Physical AI Framework for Coexistence-Oriented Human–Robot Interaction (공존형 인간-로봇 상호작용을 위한 사용자 맥락 인지 멀티모달 피지컬 AI 프레임워크 연구) (상태 진행; 지원 National Research Foundation (NRF); program Early-Career Research Award (우수신진); 기간 2026.03 - 2031.02; 역할 Principal Investigator (PI))
- Generative Haptics and Fine Response Inference for Flexible Tactile Interfaces (유연소재 촉각 인터페이스에 대한 지능적 촉각 생성과 미세 반응 추론 기술) (상태 진행; 지원 IITP; program Development of Hyper-sensory Cognitive Spatial Computing Technology (초감각인지공간컴퓨팅 기술개발); 기간 2025.04 - 2028.12; 역할 Principal Investigator (PI))
- Metaverse & AI-based Rehabilitation Technology with Cognitive and Physiological Modeling (메타버스 및 인공지능을 활용한 인지·생리학 모델링 기반 재활 기술 연구) (상태 진행; 지원 IITP; program Global Research Support Program in the Digital Field (디지털분야글로벌연구지원); 기간 2024.04. - 2026.12; 역할 Principal Investigator (PI))
- Egocentric Data Sensing and Spatial Immersive Experience Technology (화자 중심 데이터 센싱 및 공간 실감 체험 기술 개발) (상태 진행; 지원 IITP; program Development of Core Technologies for Immersive Content (실감콘텐츠핵심 원천기술개발); 기간 2026.04. - 2028.12; 역할 Co-Investigator (Co-I))
- Multi-modal Content Creation Technology Based on Intelligent Spatial Sensory Restoration and Expansion (공간 감각의 지능형 복원·확장 기반 멀티모달 체험 콘텐츠 창작 기술 개발) (상태 진행; 지원 Korea Creative Content Agency (KOCCA); program Technology Development for Cultural Content IP Planning and Creation (문화콘텐츠 IP 기획·창작 기술개발); 기간 2026.04 - 2028.12; 역할 Co-Investigator (Co-I))
- High-precision hand-crafting and service technologies based on physical AI (피지컬 AI 기반 고정밀 손기술 창작 및 서비스 기술 개발) (상태 진행; 지원 Korea Creative Content Agency (KOCCA); program Technology Development for Cultural Content IP Planning and Creation (문화콘텐츠 IP 기획·창작 기술개발); 기간 2026.04 - 2028.12; 역할 Co-Investigator (Co-I))
- An AI-Powered Physical Interface through Multimodal Biophysiological Sensing Integration (생리신호 기반 멀티모달 센싱 융합을 통한 AI 물리 인터페이스 개발) (상태 진행; 지원 TIPA (중소기업기술정보진흥원); program Industry-Academia-Research Collaborative R&D (산학연 Collabo R&D); 기간 2026.04 - 2028.03; 역할 Research Contract)
- SpaceTop: Spatial Computing HCI Technology for Everywhere XR Productivity Workstation (장소 제약 없이 XR 생산성 공간 제공을 위한 공간 컴퓨팅 HCI 기술) (상태 진행; 지원 IITP; program Information Technology Research Center (ITRC); 기간 2026.01. - 2029.12; 역할 Co-Investigator (Co-I))
- Graduate School of Metaverse Convergence (메타버스 융합대학원) (상태 진행; 지원 IITP; program Convergence Research Program (융합연구사업단); 기간 2022.07. - 2027.12; 역할 Co-Investigator (Co-I))
- Open XR platform for high immersive collaboration (Untact 실감형 OpenXR 플랫폼 기술 개발) (상태 진행; 지원 National Research Council of Science & Technology (NST); program Convergence Research Program (융합연구사업단); 기간 2021.11. - 2027.11; 역할 Co-Investigator (Co-I))
- A wearable multimodal sensing framework for adaptive interaction in extended reality (확장현실 적응형 인터랙션 제공을 위한 웨어러블 멀티모달 센서 프레임워크 연구) (상태 완료; 지원 National Research Foundation (NRF); program Early-Career Research Award (우수신진); 기간 2023.03 - 2026.02; 역할 Principal Investigator (PI))
- Motion-Haptic-Cognition Research Laboratory for Avatar-Mediated Interaction in Metaverse (메타버스를 위한 동작-촉감 통합적 사용자 인터랙션 및 아바타 행동 기술 개발) (상태 완료; 지원 National Research Foundation (NRF); program Basic Research Lab (기초연구실); 기간 2022.06 - 2025.02; 역할 Co-Investigator (Co-I))
- Development of Real-time Virtual Convergence-based Performing Arts Education Platform Technology (실시간 실가상 융합 기반 공연예술 교육 플랫폼 기술 개발) (상태 완료; 지원 Korea Creative Content Agency (KOCCA); program Technology Development for Immersive Services in Arts and Culture (문화예술 실감서비스 기술개발); 기간 2023.04 - 2025.12; 역할 Co-Investigator (Co-I))
- Development of an in-camera based interactive digital VFX content production pipeline technology (인카메라 기반 인터랙티브 디지털 VFX 콘텐츠 제작 파이프라인 기술개발) (상태 완료; 지원 Korea Creative Content Agency (KOCCA); program Technology Development Program for the Cultural Industry (문화산업 선도형 기술개발); 기간 2023.04 - 2025.12; 역할 Co-Investigator (Co-I))
- 4D Content Generation and Copyright Protection with Artificial Intelligence (인공지능을 활용한 4D 실감 콘텐츠 창작물 생성 및 저작권 핵심 기술 연구개발) (상태 완료; 지원 Korea Creative Content Agency (KOCCA); program Development of Core Technologies for Next-Generation Immersive Content Copyright (차세대 실감 콘텐츠 저작권 핵심기술 개발); 기간 2022.04 - 2023.12; 역할 Co-Investigator (Co-I))
- Enabling Clear Interaction with Wearable Active Sensing Techniques for Extended Reality (확장현실에서 명확한 인터랙션 제공을 위한 착용형 능동감지 기법 개발) (상태 완료; 지원 National Research Foundation (NRF); program Basic Research (기본연구); 기간 2022.06 - 2023.05; 역할 Principal Investigator (PI))
- Research and Development of Immersive Haptic Interaction Generation Technology for Cultural and Artistic Performances (문화예술공연을 위한 실감 햅틱 인터랙션 생성 기술 연구 개발) (상태 완료; 지원 KAIST; program Post-AI 자체사업; 기간 2022.09 - 2022.11)
- Multi-modal Sensing and Haptic Interface for Context-aware Interaction (상황 인지 상호 작용을 위한 다중모달 센싱 및 협력 인터페이스) (상태 완료; 지원 KAIST; program Start-up Research Grant; 기간 2021.09 - 2024.12; 역할 Principal Investigator (PI))

## 연락과 위치

- 교수 이메일: sangho@kaist.ac.kr[^contact]
- 교수 전화: 042-350-2915[^ct]
- 교수실: KAIST 문화기술대학원 N5동 2327호[^ct]
- 연구실: KAIST N5동 2337호, 우편물은 2346호 (대전 유성구 대학로 291)[^home][^contact]

[^home]: 랩 첫 화면 <https://hcitech.org/> (2026-10-19 열람)
[^people]: 랩 구성원 페이지(Team) <https://hcitech.org/team> (2026-10-19 열람)
[^papers]: 랩 논문 목록 <https://hcitech.org/publications> (2026-10-19 열람)
[^projects]: 랩 과제 페이지 <https://hcitech.org/projects> (2026-10-19 열람)
[^contact]: 랩 연락처 페이지 <https://hcitech.org/contact> (2026-10-19 열람)
[^ct]: KAIST 문화기술대학원 교수 소개(윤상호) <https://ct.kaist.ac.kr/boards/view/faculty_board/119> (2026-10-19 열람)
[^p1]: Y. Sung, K. John, S. H. Yoon, H. Seifi, Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, 1-24 (온라인 2025-04-25). <https://doi.org/10.1145/3706598.3713609> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K.-W. Song, Y. Kim, S. H. Yoon, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-17 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3790557> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D. Kwak, K. Seo, R. Kim, S. H. Yoon, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9, 1-24 (온라인 2025-12-02). <https://doi.org/10.1145/3770682> 초록 기준.
[^p4]: N. Vanichvoranun, H. Lee, S. Kim, S. H. Yoon, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 8, 1-29 (온라인 2024-09-09). <https://doi.org/10.1145/3678567> 초록 기준.
[^p5]: C. Park, Y. Lee, S. H. Yoon, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9, 1-31 (온라인 2025-06-18). <https://doi.org/10.1145/3731413> 초록 기준.
[^p6]: D. Lee, Q. Sun, S. H. Yoon, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-25 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3790823> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y. Sung, H. Jeong, X. Xu, S. H. Yoon, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 10, 1-23 (온라인 2026-06-15). <https://doi.org/10.1145/3810235> 초록 기준.
[^p8]: H. Han, K. Jung, S. H. Yoon, Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, 1-21 (온라인 2025-04-25). <https://doi.org/10.1145/3706598.3714220> 초록 기준(Semantic Scholar 등록 초록).

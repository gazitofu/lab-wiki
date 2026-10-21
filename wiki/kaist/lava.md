# 실감 아바타·에이전트 연구실 (Lifelike Avatar & Agent Laboratory, LAVA Lab)

**KAIST 문화기술대학원 · 이성희 교수**

- 분야: 디지털 휴먼·아바타 모델링과 애니메이션, 모션 캡처, 원격 현장감(텔레프레즌스) 아바타, 디지털 패션(의복 패턴·옷감 시뮬레이션), 인공지능 에이전트의 동작 생성
- 대분야: 컴퓨팅·AI
- 태그: 디지털 휴먼·아바타[^gsmv][^p2][^p7], 가상·증강현실[^news][^p1][^p3], 3차원 복원·인식[^p4][^p5][^p6], 디지털 패션·의복 시뮬레이션[^p8]
- 홈페이지: <https://lava.kaist.ac.kr/>
- 근거와 출처: [LAVA Lab 근거 페이지](lava-sources.md)

> 가상현실·메타버스·게임에 나오는 아바타와 가상 캐릭터가 사람처럼 자연스럽게 움직이고 행동하게 만드는 연구실이다. 라이다 센서 하나로 몸 동작을 잡아내는 기술, 서로 다른 방에 있는 사람들이 아바타로 한 공간에 있는 것처럼 만나는 기술, 옷의 재단 패턴을 만들고 옷감을 시뮬레이션하는 디지털 패션 기술을 개발한다.[^home][^research]

## 무엇을 연구하나

연구실은 아바타와 가상 캐릭터 같은 인공 인간을 위한 기술을 발전시키는 것을 목표로, 디지털 휴먼(아바타, 캐릭터, 에이전트)의 모델링·애니메이션·시뮬레이션을 연구한다고 소개한다. 이전 이름은 모션 컴퓨팅 연구실(Motion Computing Lab)이며, 연구는 컴퓨터 애니메이션, 게임, VR·AR·메타버스, 디지털 패션 같은 분야에 쓰인다.[^home] 연구 주제 페이지는 동작 연구(캐릭터 애니메이션, AI 에이전트 동작, 모션 캡처, K팝 안무), 텔레프레즌스(아바타 동작, 공간 생성), 디지털 패션(의복 모델링, 의복 업사이클링, 딥러닝 옷감 시뮬레이션)을 든다.[^research]

첫 번째 갈래는 **원격 현장감(텔레프레즌스) 아바타**다. 혼합현실(MR)에서 멀리 있는 사람을 내 방에 아바타로 불러와 함께 있는 것처럼 상호작용하게 하는 기술이다. 서로 구조가 다른 방을 겹쳐 함께 쓸 공간을 맞추고 나머지 공간을 사용자 거리에 따라 보이게 하는 시스템,[^p1] 내 방과 상대 방의 가구 배치가 달라도 시선·손가리킴 같은 상체 동작이 상대에게 제대로 전달되도록 아바타 동작을 바꿔 주는 인공지능,[^p2] 동작이 잘 전달되는 자리로 사용자를 안내하는 시각 안내 시스템을 만들었다.[^p3]

두 번째 갈래는 **모션 캡처와 캐릭터 애니메이션**이다. 몸에 장비를 붙이지 않고 라이다(레이저로 거리를 재는 센서) 한 대로 실시간 전신 동작을 잡아내는 기술을 만들었고,[^p4][^p5] 가상현실 헤드셋과 두 손 컨트롤러 세 점의 신호만으로 다양한 체형의 전신 자세를 추정했다.[^p6] 신체 부위마다 다른 동작 스타일을 입히는 동작 스타일 변환 기술도 개발했다.[^p7]

세 번째 갈래는 **디지털 패션**이다. 대부분의 옷이 평평한 재단 조각(패턴)으로 만들어진다는 점에 착안해, 옷의 3차원 모양과 재단 패턴을 짝지은 대규모 합성 데이터셋을 자동으로 만드는 방법을 내놓았다.[^p8] 최근 논문 목록에는 사진 한 장에서 재단 패턴을 추정하는 연구, 헐렁한 옷의 움직임을 계산하는 연구, 인공지능 에이전트로 의복 패턴을 만드는 연구가 이어진다.[^papers]

## 주요 연구 주제

### 1. 혼합현실 텔레프레즌스 아바타

공간 겹치기와 가시성 조절, 상체 동작 변환, 위치 안내.[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 모션 캡처와 캐릭터 애니메이션

단일 라이다 모션 캡처, 세 점 추적 전신 추정, 동작 스타일 변환.[^p4][^p5][^p6][^p7] 대표 논문 4–7.

### 3. 디지털 패션

의복 패턴 데이터셋, 패턴 추정, 옷감 애니메이션.[^p8][^papers] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 교수가 랩 목록 저자 순서의 마지막인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [Voronoi Rooms: Dynamic Visibility Modulation of Overlapping Spaces for Telepresence](https://doi.org/10.1145/3777900) · ACM Transactions on Graphics | 여러 사람의 방을 겹쳐 함께 쓸 공간을 맞춘 뒤, 겹치지 않는 각자의 공간까지 보여 주는 혼합현실 텔레프레즌스 시스템. 서로 겹치는 부분은 보로노이 도형(가장 가까운 사람의 영역으로 나누는 방법)으로 가까운 사람의 공간을 우선 보여 주고, 사람이 움직이면 실시간으로 바꾼다.[^p1] | 1저자 Taehei Kim, 마지막 저자 이성희 |
| 2 | 2025 | [Real-time Translation of Upper-body Gestures to Virtual Avatars in Dissimilar Telepresence Environments](https://doi.org/10.1109/tvcg.2025.3577156) · IEEE TVCG | 구조가 다른 공간에서 아바타가 사용자의 의도를 제대로 전하도록 시선, 손가리킴, 자유 동작과 그 사이 전환을 실시간으로 바꿔 주는 신경망. 한 사람의 데이터로 학습했지만 체형·주로 쓰는 손·주시안(두 눈 가운데 주로 쓰는 눈)이 달라도 자연스러운 동작을 만들고, 짝지은 학습 데이터가 필요 없다.[^p2] | 1저자 Jiho Kang, 마지막 저자 이성희 |
| 3 | 2024 | [Visual Guidance for User Placement in Avatar-Mediated Telepresence Between Dissimilar Spaces](https://doi.org/10.1109/tvcg.2024.3354256) · IEEE TVCG | 상대 방의 아바타를 통해 시선과 손가리킴이 잘 전달되는 자리를 계산해, 내 방 바닥에 색으로 나눈 부채꼴로 추천 위치를 보여 주는 안내 시스템. 상대 방의 가상 물체도 내 방에 겹쳐 보여 준다.[^p3] | 1저자 Dongseok Yang, 마지막 저자 이성희 |
| 4 | 2024 | [ELMO: Enhanced Real-time LiDAR Motion Capture through Upsampling](https://doi.org/10.1145/3687991) · ACM Transactions on Graphics | 라이다 한 대가 초당 20장 찍는 점 구름(레이저가 부딪힌 지점들의 3차원 좌표 모음)으로 초당 60프레임 전신 동작을 만들어 내는 실시간 모션 캡처. 트랜스포머(문맥을 함께 보는 신경망 구조) 기반 생성 모델과, 점 구름 한 장으로 사용자 뼈대 길이를 맞추는 골격 보정, 라이다 시뮬레이터로 늘린 학습 데이터를 썼다.[^p4] | 공동 1저자 Deok-Kyeong Jang 등 4명, 마지막 저자 이성희(랩 목록 기준) |
| 5 | 2023 | [MOVIN: Real-time Motion Capture using a Single LiDAR](https://doi.org/10.1111/cgf.14961) · Computer Graphics Forum | 비싸고 다루기 어려운 기존 모션 캡처 대신, 라이다 한 대의 3차원 점 구름에서 자세 변화를 배우는 생성 모델로 전신 동작과 몸 전체의 위치를 실시간으로 잡아낸다.[^p5] | 공동 1저자 Deok-Kyeong Jang 등 4명, 마지막 저자 이성희 |
| 6 | 2024 | [DivaTrack: Diverse Bodies and Motions from Acceleration-Enhanced Three-Point Trackers](https://doi.org/10.1111/cgf.15057) · Computer Graphics Forum | VR 헤드셋과 두 손 컨트롤러의 세 위치 신호에 가속도 센서 정보를 더해 발이 바닥에 닿는지 예측하고, 두 단계 모델로 다양한 체형과 활동의 전신 자세를 기존 방법보다 잘 추정했다. Eurographics 2024에서 Honorable Mention(입선)을 받았다.[^p6][^news] | 1저자 Dongseok Yang, 마지막 저자 이성희 |
| 7 | 2022 | [Motion Puzzle: Arbitrary Motion Style Transfer by Body Part](https://doi.org/10.1145/3516429) · ACM Transactions on Graphics | 신체 부위마다 다른 동작 스타일을 따로 입힐 수 있는 첫 동작 스타일 변환 신경망. 골격 구조를 유지하면서 퍼덕이기·비틀거리기 같은 역동적인 스타일도 잘 옮기고, 스타일 표시나 짝지은 데이터 없이 학습한다.[^p7] | 1저자 Deok-Kyeong Jang, 마지막 저자 이성희 |
| 8 | 2021 | Generating Datasets of 3D Garments with Sewing Patterns · NeurIPS Datasets and Benchmarks Track | 대부분의 옷이 평평한 재단 조각으로 만들어진다는 점에서, 매개변수로 정한 패턴 틀로부터 옷의 3차원 모델과 재단 패턴을 거의 손대지 않고 자동으로 만드는 파이프라인을 만들어 대규모 합성 데이터셋을 공개했다. 3차원 스캔의 결함을 흉내 낸 버전도 함께 만든다.[^p8] | 1저자 Maria Korosteleva, 마지막 저자 이성희 |

## 교수와 전문 분야

이성희 교수는 서울대 기계공학 학사(1996)·석사(2000)와 미국 UCLA 컴퓨터과학 박사(2008)를 받았다. UCLA 박사후연구원(2008–2009), 혼다 연구소 박사후연구원(2009–2010), 광주과학기술원(GIST) 조교수(2010–2013)를 거쳐 2013년 KAIST에 부임했고 지금은 문화기술대학원 교수다. 리듬앤휴즈 스튜디오, 마이크로소프트 연구소에서 인턴으로 일했다.[^prof] IEEE Transactions on Visualization and Computer Graphics 부편집장(2023–), Pacific Graphics 2023 학술대회 위원장, SIGGRAPH 기술 논문 위원 등을 맡았다.[^prof] 메타버스대학원 참여 연구실 소개는 관심 분야를 디지털 휴먼·아바타 모델링, 디지털 휴먼 동작 생성, AR·VR 텔레프레즌스 아바타로 적는다.[^gsmv]

논문으로 보면 전문 분야는 세 갈래다.

- **아바타 기반 혼합현실 텔레프레즌스**.[^p1][^p2][^p3]
- **데이터 기반 모션 캡처와 애니메이션**.[^p4][^p5][^p6][^p7]
- **의복 모델링과 디지털 패션**.[^p8]

## 응용 분야

대표 논문과 소식으로 보면 게임·영상 캐릭터 애니메이션, 메타버스와 원격 협업, 저비용 모션 캡처, 디지털 패션에 닿아 있다.[^p1][^p4][^p8] 연구실은 2024년 과학기술정보통신부 '메타버스 랩'에 선정됐고, ISMAR 2024 최고 데모 부문 Honorable Mention(입선)과 2025 가상융합서비스 개발자 경진대회 우수상(Excellence Award)을 받았으며, 실제 공간을 결합한 XR 소셜 플랫폼 ParameterRoom을 메타 스토어에 얼리 액세스로 내놓았다.[^news]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 연구 주제는 랩 표기를 옮겼다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Libao, Ian | 박사과정 | Cloth simulation, Geometry processing | iandlibao@kaist.ac.kr |  |
| Park, Soomin | 박사과정 | Character animation, Human Motion | sumny@kaist.ac.kr | 7 |
| Choi, Byeoli | 박사과정 | 3D Cloth Reconstruction, Modeling | byeol2@kaist.ac.kr | 4, 5 |
| Lim, Seungchan | 박사과정 | Garment modeling, Geometry processing | thecross1227@kaist.ac.kr |  |
| Lee, Myeongjin | 박사과정 | Cloth simulation, Computer animation | myeongjin.lee@kaist.ac.kr |  |
| Kang, Jiho | 박사과정 | Human Animation, Telepresence Avatar Motion | jhkang0408@kaist.ac.kr | 1, 2, 3, 6 |
| Kwon, Hyun Song | 박사과정 | Digital Garments, Robotic Manipulation | hyunsong.kwon@kaist.ac.kr |  |
| Kim, Meongeun | 박사과정 | Character Animation, Motion Generation | meongeun@kaist.ac.kr |  |
| Shin, Jihun | 박사과정 | Computer graphics, XR, Telepresence | jihun.shin@kaist.ac.kr | 1 |
| Kim, Hyeshim | 박사과정 | Generative 3D Scene Synthesis, 3D Reconstruction, Telepresence | hyedeep@kaist.ac.kr | 1, 2 |
| Kim, Hyeonjin | 석사과정 | Telepresence, XR | hyeonjin@kaist.ac.kr |  |
| Chae, Yeongmin | 석사과정 | Garment modeling, Computer graphics | youngmin.chae@kaist.ac.kr |  |
| Lee, Eunseong | 석사과정 | Character animation, Motion generation | dmstjd2757@kaist.ac.kr |  |
| Lee, Taehui | 석사과정 | Character animation, Motion generation | taehui@kaist.ac.kr |  |
| Shin, Rim Soo | 석사과정 | AI, Computer Graphics, Virtual Garments | flyingtiger@kaist.ac.kr |  |
| Shin, Dong Hwan | 석사과정 | Auto-Agent, LLM Based Motion/Action Planning/Avatar Auto-Generation | sdhqaa@kaist.ac.kr |  |
| Choi, Yuna | 석사과정 | Telepresence, Motion Generation | yunicorn0413@kaist.ac.kr |  |
| Song, Hawon | 석사과정 | Telepresence, User Interaction | hawon.song@kaist.ac.kr |  |
| Jiang, Fengjian | 석사과정 | Computer Graphics, AI-assisted Character Animation, Physical Fidelity | fengjianjiang@kaist.ac.kr |  |
| Balasooriya, Lasni | 석사과정 | Digital fashion, Garment pattern modeling | lasniminoja@kaist.ac.kr |  |
| Ko, Dayeon | 석사과정 | Robotic Manipulation, Computer Vision | dayeon@kaist.ac.kr |  |
| Choi, Junghoon | 석사과정 | Computer Graphics, Character Animation, Motion Generation | j.choi@kaist.ac.kr |  |

## 졸업생 진로

랩 졸업생 페이지의 박사·석사 졸업생과 랩이 적은 현재 소속이다. 진로 칸이 비어 있는 졸업생은 랩이 소속을 적지 않은 경우다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kim, Taehei | Ph.D. | InnoCORE Postdoc |
| Yeom, Mingi | Ph.D. |  |
| Jeong, Choongho | Ph.D. | MOVIN |
| Yang, Dongseok | Ph.D. | Co-founder of MOVIN |
| Jin, Taeil | Ph.D. | Professor at Chung-Ang Univ. |
| Jang, Deok-Kyeong (DK) | Ph.D. | CTO of MOVIN |
| Maria Korosteleva | Ph.D. | Researcher at Meshcapade |
| Kim, Hye-Ji | Ph.D. | Research Professor at Seoul National Univ. of Science and Technology |
| Yoon, Leonard | Ph.D. | ReconLabs |
| Kim, Yeonjoon | Ph.D. |  |
| Bang, Seungbae | Ph.D. | Amazon USA |
| Lee, Suk-won | Ph.D. | Professor at Kangwon National Univ. |
| Lee, Jeong-Seob | Ph.D. | Founder of Bipole |
| Park, Han-Gil | Ph.D. | Nexon |
| Kim, Meekyoung | Ph.D. | CLO virtual fashion |
| Kim, Hye-Jin | Ph.D. | Seoul Intsitute of Technology |
| Kang, Changgu | Ph.D. | Professor at Gyeongsang National Univ. |
| Lee, Kwangbin | M.S. |  |
| Kim, Hyeshim | M.S. | Ph.D. candidate in LAVA Lab. |
| Shin, Jihun | M.S. | Ph.D. candidate in LAVA Lab. |
| Lee, Yewon | M.S. | AI Engineer (company name withheld) |
| Kim, Sumin | M.S. |  |
| Chibisova, Tatiana | M.S. | Skonec |
| Jin, Yurhee | M.S. | LG Electronics R&D |
| Kwon, Haram | M.S. | Krafton |
| Kwon, Hyunsong | M.S. | Ph.D. candidate in LAVA Lab. |
| Kang, Jiho | M.S. | Ph.D. candidate in LAVA Lab. |
| Lee, Myeongjin | M.S. | Ph.D. candidate in LAVA Lab. |
| Lim, Seungchan | M.S. | Ph.D. candidate in LAVA Lab. |
| Choi, Byeoli | M.S. | CEO of MOVIN, Ph.D. candidate in LAVA Lab. |
| Park, Soomin | M.S. | Ph.D. candidate in LAVA Lab. |
| Kim, Taehei | M.S. | Ph.D. candidate in LAVA Lab. |
| Yeom, Mingi | M.S. | Ph.D. candidate in LAVA Lab. |
| Yang, Dongseok | M.S. | Ph.D. candidate in LAVA Lab. |
| Kim, Zeehyo | M.S. |  |
| Choi, Youjin | M.S. | Co-founder of Classum |
| Kim, Meejin | M.S. | KETI |
| Jin, Sam | M.S. | Co-founder of CUZ |
| Jeong, Choongho | M.S. | Ph.D. candidate in LAVA Lab. |
| Lee, Youjin | M.S. | Samsung Electronics |
| Sang, Jonghee | M.S. | ETRI |
| Jang, Sung-Ah | M.S. |  |
| Oh, Jihye | M.S. | LG Chem |
| Ko, Sang-Ah | M.S. |  |
| Suh, Sangwon | M.S. | ETRI |
| Choi, Hyeon-Cheol | M.S. | KAKAO |
| Kim, Han-Sol | M.S. | Samsung Electronics |
| Kim, Sin-Young | M.S. | Hanwha |
| Jung, Seunghwan | Researcher |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021–2026년 논문 34편(학술지, 학술대회, 포스터·데모 포함)이다. 수상·발표 형식 표기는 랩 표기를 옮겼다.[^papers]

**2026**

- Taehei Kim, Hyeshim Kim, Jihun Shin, Hyeonjin Kim, and Sung-Hee Lee. "Neighborhood: Dynamic Spatial Alignment for Traversable Telepresence Across Remote Spaces". *The ACM Symposium on User Interface Software and Technology (UIST), 2026*.
- Jiho Kang\*, Junghoon Choi\*, Jihun Shin, and Sung-Hee Lee. "PropGesture: Few-shot Co-speech Gesture Synthesis for Handheld Props". *Computer Graphics Forum (Proc. Pacific Graphics), 2026*.
- Hyeshim Kim, Taehei Kim\*, Jihun Shin\*, Hyeonjin Kim, and Sung-Hee Lee. "TranSpace: Progressive Anchoring for Metric-Consistent Scene Synthesis". *ACM Multimedia (MM) Oral, 2026*.
- Soomin Park, Eunseong Lee, Kwang Bin Lee, and Sung-Hee Lee. "MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters". *CVPR (Highlight), 2026*.
- Choongho Chung, DongHwan Shin, and Sung-Hee Lee. "Action Sequence Transfer via LLMs for Heterogeneous Environments". *International Conference on Robotics and Automation (ICRA), 2026*.
- Mingi Yeom, Rimsoo Shin, and Sung-Hee Lee. "GarmentoPIA: Generating Garment Pattern Models using Intelligent Agents". *Computational Visual Media, 2026 (will be presented at CVM)*.

**2025**

- Taehei Kim, Jihun Shin, Hyeshim Kim, Hyuckjin Jang, Jiho Kang, and Sung-Hee Lee. "Voronoi Rooms: Dynamic Visibility Modulation of Overlapping Spaces for Telepresence". *ACM Transactions on Graphics, 2025*.
- Myeongjin Lee, Emmanuel Ian Libao, and Sung-Hee Lee. "Hybrid Retrieval–Regression for Motion-Driven Loose-Fitting Garment Animation". *Pacific Graphics 2025 , Oct. 2025*.
- Minseok Kim, Wonjeong Seo, Sung-Hee Lee, Jungdam Won. "ViSA: Physics-based Virtual Stunt Actors for Ballistic Stunts". *ACM Transactions on Graphics (Proc. SIGGRAPH 2025), Aug. 2025*.
- Jiho Kang, Taehei Kim, Hyeshim Kim, and Sung-Hee Lee. "Real-time Translation of Upper-body Gestures to Virtual Avatars in Dissimilar Telepresence Environments". *IEEE Transactions on Visualization and Computer Graphics (TVCG), Jun. 2025*.
- Taeil Jin, Yewon Lee, and Sung-Hee Lee. "InterFaceRays: Interaction-Oriented Furniture Surface Representation for Human Pose Retargeting". *Computer Graphics Forum (Proc. Eurographics 2025), Feb. 2025*.
- Taehei Kim, Hyeshim Kim, Jeongmi Lee, and Sung-Hee Lee. "Evaluating user perception toward physics-adapted avatar in remote heterogeneous spaces". *Computers & Graphics, Feb. 2025*.

**2024**

- Deok-Kyeong Jang\*, Dongseok Yang\*, Deok-Yun Jang\*, Byeoli Choi\*, Donghoon Shin, and Sung-Hee Lee. "ELMO: Enhanced Real-time LiDAR Motion Capture through Upsampling". *ACM Transactions on Graphics (Proc. SIGGRAPH ASIA), Dec. 2024*.
- Seungchan Lim, Sumin Kim, and Sung-Hee Lee. "SPnet: Estimating Garment Sewing Patterns from a Single Image of a Posed User". *Eurographics 2024 Conference, Short, Apr. 2024*.
- Hyun-Song Kwon and Sung-Hee Lee. "DeepIron: Predicting Unwarped Garment Texture from a Single Image". *Eurographics 2024 Conference, Short, Apr. 2024*.
- Dongseok Yang, Jiho Kang, Lingni Ma, Joseph Greer, Yuting Ye, and Sung-Hee Lee. "DivaTrack: Diverse Bodies and Motions from Acceleration-Enhanced Three-Point Trackers". *Computer Graphics Forum (Proc. Eurographics 2024 Honorable Mention Award), Apr. 2024*.
- Choongho Chung and Sung-Hee Lee. "Continuous Prediction of Pointing Targets With Motion and Eye-Tracking in Virtual Reality". *IEEE Access, Jan. 2024*.
- Dongseok Yang, Jiho Kang, Taehei Kim, and Sung-Hee Lee. "Visual Guidance for User Placement in Avatar-Mediated Telepresence between Dissimilar Spaces". *IEEE Transactions on Visualization and Computer Graphics (TVCG), Jan. 2024*.

**2023**

- Deok-Kyeong Jang, Yuting Ye, Jungdam Won, and Sung-Hee Lee. "MOCHA: Real-time Motion Characterization via Context Matching". *SIGGRAPH ASIA 2023, Dec. 2023*.
- Emmanuel Ian Libao, Myeongjin Lee, Sumin Kim, and Sung-Hee Lee. "MeshGraphNetRP: Improving Generalization of GNN-based Cloth Simulation". *ACM Motion, Interaction and Games (MIG) 2023, Nov. 2023*.
- Jiho Kang, Dongseok Yang, Taehei Kim, Yewon Lee, and Sung-Hee Lee. "Real-time Retargeting of Deictic Motion to Virtual Avatars for Augmented Reality Telepresence". *IEEE International Symposium on Mixed and Augmented Reality (ISMAR) 2023, Oct. 2023*.
- Taeil Jin, Sung-Hee Lee. "DAFNet: Generating Diverse Actions for Furniture Interaction by Learning Conditional Pose Distribution". *Computer Graphics Forum (Proc. Pacific Graphics) 2023, Sep. 2023*.
- Deok-Kyeong Jang\*, Dongseok Yang\*, Deokyun Jang\*, Byeoli Choi\*, Taeil Jin, and Sung-Hee Lee. "MOVIN: Real-time Motion Capture using a Single LiDAR". *Computer Graphics Forum (Proc. Pacific Graphics) 2023, Sep. 2023*.

**2022**

- Hye Ji Kim, Michael Neff, Sung-Hee Lee. "The Perceptual Consistency and Association of the LMA Effort Elements". *ACM Transactions on Applied Perception (TAP), 2022*.
- Hyuckjin Jang\*, Taehei Kim\*, Seo Young Oh, Jeongmi Lee, Sung-Hee Lee, and Sang Ho Yoon. "Sense of Embodiment Inducement for People with Reduced Lower-body Mobility and Sensations with Partial-Visuomotor". *ACM SIGGRAPH 2022 Emerging Technologies, Aug. 2022*.
- Maria Korosteleva and Sung-Hee Lee. "NeuralTailor: Reconstructing Sewing Pattern Structures from 3D Point Clouds of Garments". *ACM Transactions on Graphics (TOG), ACM SIGGRAPH 2022, July 2022*.
- Deok-Kyeong Jang, Soomin Park, Sung-Hee Lee. "Motion Puzzle: Arbitrary Motion Style Transfer by Body Part". *ACM Transactions on Graphics (TOG), Jan. 2022 (presented at ACM SIGGRAPH 2022)*.

**2021**

- Maria Korosteleva and Sung-Hee Lee. "Generating Datasets of 3D Garments with Sewing Patterns". *NeurIPS (NIPS) Datasets and Benchmarks Track, Sep. 2021*.
- Taehei Kim and Sung-Hee Lee. "Quadruped Locomotion on Elastic Ground using Reinforcement Learning (Poster)". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Aug. 2021 [Poster]*.
- Hyung-il Kim, Taehei Kim, Eunhwa Song, Seo Young Oh, Dooyoung Kim, and Woontack Woo. "Multi-scale Mixed Reality Collaboration for Digital Twin (Poster)". *IEEE International Symposium on Mixed and Augmented Reality (ISMAR), Aug. 2021 [Poster]*.
- Taehei Kim and Sung-Hee Lee. "Quadruped Locomotion on Non-Rigid Terrain using Reinforcement Learning". *arXiv:2107.02955v1, July 2021*.
- Soomin Park, Deok-Kyeong Jang, and Sung-Hee Lee. "Diverse Motion Stylization for Multiple Style Domains via Spatial-Temporal Graph-Based Generative Model". *The ACM SIGGRAPH / Eurographics Symposium on Computer Animation (SCA), June 2021*.
- Seungbae Bang, Maria Korosteleva, and Sung-Hee Lee. "Estimating Garment Patterns from Static Scan Data". *Computer Graphics Forum, May 2021*.
- Dongseok Yang, Doyeon Kim, and Sung-Hee Lee. "LoBSTr: Real-time Lower-body Pose Prediction from Sparse Upper-body Tracking Signals". *Eurographics 2021 Conference, in Computer Graphics Forum, May 2021*.

## 소식

- 2026-03-26 · LAVA Lab and VCL Lab Presented Demo “Situately” at IEEE VR 2026 in Daegu
- LAVA Lab launched “ParameterRoom” Early Access on Meta Store
- LAVA Lab received Excellence Award and presented following demo at ISMAR 2025
- 2025-01-06 · LAVA Lab was featured in Kaistian newsletter
- 2024-11-12 · A CT Lab Tour was held at LAVA Lab for Ling Tung University students
- 2024-11-12 · LAVA Lab participated in the X-Space performance held at the Daejeon Arts Center
- 2024-10-28 · LAVA Lab received the Best Demo Honorable Mention Award at ISMAR 2024
- 2024-05-27 · LAVA Lab Selected for ‘Metaverse Lab’ by the Ministry of Science and ICT
- 2024-04-27 · Dongsoek Yang received the Honorable Mention Award at Eurographics 2024 Conference
- 2023-11-14 · Tech Talk: Insights on Apparel & Fashion with R3iLAB

## 연락과 위치

- 교수 이메일: sunghee.lee@kaist.ac.kr[^contact]
- 교수 전화: 042-350-2925[^contact]
- 교수실: KAIST N5동 2333호 (대전 유성구 대학로 291)[^contact]

[^home]: LAVA Lab 누리집 첫 화면 <https://lava.kaist.ac.kr/> (2026-10-19 열람)
[^prof]: LAVA Lab 교수 소개 <https://lava.kaist.ac.kr/?page_id=41> (2026-10-19 열람)
[^members]: LAVA Lab 구성원 페이지 <https://lava.kaist.ac.kr/?page_id=267> (2026-10-19 열람)
[^alumni]: LAVA Lab 졸업생 페이지 <https://lava.kaist.ac.kr/?page_id=439> (2026-10-19 열람)
[^research]: LAVA Lab 연구 주제 페이지 <https://lava.kaist.ac.kr/?page_id=1021> (2026-10-19 열람)
[^papers]: LAVA Lab 논문 목록 <https://lava.kaist.ac.kr/?page_id=81> (2026-10-19 열람)
[^news]: LAVA Lab 소식 <https://lava.kaist.ac.kr/?cat=6> (2026-10-19 열람)
[^contact]: LAVA Lab 연락처 <https://lava.kaist.ac.kr/?page_id=90> (2026-10-19 열람)
[^gsmv]: KAIST 메타버스대학원 참여 연구실 소개(LAVA Lab) <https://meta.kaist.ac.kr/labs/lava-lab?lang=en> (2026-10-19 열람)
[^p1]: T. Kim 외, S.-H. Lee, ACM Transactions on Graphics 45, 1-15 (온라인 2025-12-19). <https://doi.org/10.1145/3777900> 초록 기준.
[^p2]: J. Kang, T. Kim, H. Kim, S.-H. Lee, IEEE Transactions on Visualization and Computer Graphics (2025). <https://doi.org/10.1109/tvcg.2025.3577156> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: D. Yang, J. Kang, T. Kim, S.-H. Lee, IEEE Transactions on Visualization and Computer Graphics 30, 7558-7570 (2024). <https://doi.org/10.1109/tvcg.2024.3354256> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: D.-K. Jang 외, D. Shin, ACM Transactions on Graphics 43, 1-14 (온라인 2024-11-19). <https://doi.org/10.1145/3687991> 초록 기준.
[^p5]: D.-K. Jang 외, S.-H. Lee, Computer Graphics Forum 42, e14961 (온라인 2023-11-05). <https://doi.org/10.1111/cgf.14961> 초록 기준.
[^p6]: D. Yang 외, S.-H. Lee, Computer Graphics Forum 43, e15057 (온라인 2024-04-27). <https://doi.org/10.1111/cgf.15057> 초록 기준.
[^p7]: D.-K. Jang, S. Park, S.-H. Lee, ACM Transactions on Graphics 41, 1-16 (온라인 2022-06-09). <https://doi.org/10.1145/3516429> 초록 기준.
[^p8]: M. Korosteleva, S.-H. Lee, NeurIPS Datasets and Benchmarks Track (2021). <https://lava.kaist.ac.kr/?page_id=81> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).

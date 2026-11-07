# Statistical Inference & Information Theory Laboratory (SIIT)

**KAIST 전기및전자공학부 · 김준모 교수**

- 영문 이름: Statistical Inference & Information Theory Laboratory
- 분야: 컴퓨터 비전, 생성 인공지능, 멀티모달 학습, 인공지능 안전[^intro]
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^intro], 멀티모달 AI[^intro]
- 홈페이지: <https://siit.kaist.ac.kr/>
- 근거와 출처: [Statistical Inference & Information Theory Laboratory 근거 페이지](siit-sources.md)

> 이미지·영상·글·소리를 함께 이해하는 인공지능과, 새로운 자료를 생성하고 안전하게 학습하는 방법을 연구한다.

## 무엇을 연구하나

SIIT는 컴퓨터 비전(사진·영상에서 물체와 장면의 정보를 알아내는 기술)과 멀티모달 학습(이미지·글·소리처럼 종류가 다른 자료를 함께 다루도록 배우는 방법)을 중심으로 인공지능의 원리와 응용을 연구한다.[^intro] 실제 세계를 보고 이해하며 행동하는 지능 시스템을 목표로 하며, 인공지능 안전도 연구 범위에 둔다.[^intro]

새로운 이미지와 사람의 동작을 다루는 생성 모형(자료가 만들어지는 규칙을 나타내어 새로운 자료를 만들 수 있게 한 모형)을 개발한다. 이미지의 가려진 부분을 채우는 생성 과정에서는 모형 자체의 정보를 이용해 결과의 품질과 다양성을 조절하는 방법을 연구했다. 사람 동작에서는 기준 동작과 글로 쓴 수정 지시를 함께 받아, 기존 동작의 핵심 의미를 유지하면서 원하는 변화가 반영된 동작을 찾아내는 방법을 제안했다.[^p3][^p1]

글과 시각 자료를 함께 배우는 방법, 글로 인공지능에 지시하는 방법도 연구한다. 이미지·글의 관계와 이미지끼리의 관계를 하나의 학습 공간에서 다루는 대비 학습(관련 있는 자료의 표현은 가깝게, 관련 없는 자료의 표현은 멀게 만드는 학습 방법)을 제안했다. 대형 언어 모델(Large Language Model, 많은 글로 학습해 글을 이해하고 생성하는 인공지능 모형)에 넣을 지시문은 강화학습(행동에 따른 누적 보상을 키우도록 행동 방법을 배우는 학습 방식)으로 탐색하며, 탐색 중 학습의 안정성을 유지하는 방법을 다룬다.[^p4][^p5]

학습한 모형을 안전하고 효율적으로 쓰는 문제와 의료 영상의 구조를 구분하는 문제도 다룬다. 인공지능의 응답만으로 학습 자료의 비공개 정보를 복원하는 공격을 연구해 정보 유출 위험을 시험하고, 제한된 계산 자원에 맞추어 신경망(서로 연결된 계산 단위와 그 연결의 값을 이용해 입력을 출력으로 바꾸는 모형)의 크기를 줄이는 방법을 개발한다. 의료 영상에서는 기관지와 혈관의 위치 관계를 이용하여 폐 안의 구역을 나누는 알고리즘(정해진 순서와 규칙에 따라 문제를 푸는 계산 절차)을 제안했다.[^p6][^p8][^p7]

## 주요 연구 주제

### 시각 인식과 공간 정보

자율주행에서는 합성한 주행 시나리오를 실제 주행 자료와 함께 학습하는 SynAD를 제안했다. 합성 시나리오에서 차량을 정하고 지도에서 내려다본 공간의 특징을 만든 뒤, 이를 실제 자료와 통합하는 학습 전략으로 연결한다.[^p2] 의료 영상에서는 폐 구역의 위치를 확률 지도(각 위치가 특정 구역에 속할 가능성을 나타낸 자료)로 나타내고, 기관지·혈관과 구역 경계 사이의 해부학적 관계를 반영해 분할한다.[^p7]

### 생성 모형과 사람 동작

이미지 생성에서는 모형 자체의 정보를 이용하는 자기 유도 방법으로 생성 결과의 품질과 다양성 사이의 균형을 개선한다.[^p3] 사람 동작 검색에서는 기준 동작에서 유지할 의미와 글 지시에 따라 달라질 변화를 나누어 배우는 표현 방법을 연구한다.[^p1]

### 멀티모달 학습과 언어 모델

이미지·글의 쌍과 이미지끼리의 쌍을 함께 학습하면서, 자료 종류에 따라 생기는 차이를 조정하는 표현 학습(자료를 과제에 필요한 특징으로 바꾸는 방법을 배우는 일)을 연구한다.[^p4] 언어 모델에서는 지시문을 자동으로 찾되, 기존에 배운 언어 능력을 유지하면서 탐색을 이어 가도록 학습 갱신의 정도를 조절한다.[^p5]

### 모델의 안전과 계산 효율

모형 내부를 볼 수 없는 조건에서 응답을 이용해 학습 자료의 정보를 되찾는 모델 역전 공격을 연구한다. 복원할 자료의 표현을 찾는 과정을 강화학습으로 구성하여 개인정보 보호가 필요한 이유를 보인다.[^p6] 계산 효율에서는 목표 계산량과 모형 크기를 학습 과정에 반영하고, 중요한 연결 값을 고르면서 신경망의 일부를 제거하는 가지치기 방법을 개발한다.[^p8]

## 대표 논문

김준모 교수가 KAIST에 재직하며 저자로 참여한 논문 가운데 시각 인식·생성·멀티모달·안전과 효율의 갈래가 드러나도록 골랐다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [TransMotion: Text-Guided Transformation Learning for Composed Human Motion Retrieval](https://doi.org/10.3390/app162110842) · Applied Sciences | 글 한 문장만으로 원하는 사람 동작을 정확하게 지정하기 어렵다는 문제에서 출발한다. 기준 동작과 글로 쓴 수정 지시를 함께 받아 목표 동작을 찾는 과제를 제안하고, 기준·목표 동작에서 유지할 의미와 글 지시에 따라 달라질 변화를 나누어 학습했다. 두 자료 집합에서 기존 동작 편집·검색 방법을 이 과제에 맞춘 비교 방법들보다 좋은 검색 성능을 보였다.[^p1] | 1저자 Gyojin Han·Jongsuk Kim(누리집 공동 기여), 마지막 저자 김준모 |
| 2 | 2025 | [SynAD: Enhancing Real-World End-to-End Autonomous Driving Models through Synthetic Data Integration](https://doi.org/10.1109/iccv51701.2025.02337) · ICCV 2025 | 실제 주행 자료만으로는 학습할 상황의 다양성에 한계가 있어 합성한 주행 시나리오를 활용하려 했다. 합성 시나리오에서 주행 정보가 가장 풍부한 참여 차량을 기준 차량으로 정하고, 경로를 지도 위의 위치로 옮긴 뒤 센서 입력 없이 위에서 내려다본 장면의 특징을 만드는 방법을 제안했다. 이 합성 자료와 실제 자료를 통합해 학습한 결과 자율주행 모형의 안전 성능이 향상되었다.[^p2] | 1저자 Jongsuk Kim, 마지막 저자 김준모 |
| 3 | 2024 | [Unlocking the Capabilities of Masked Generative Models for Image Synthesis via Self-Guidance](https://doi.org/10.52202/079017-4163) · NeurIPS 2024 | 이미지의 일부를 가리고 채우는 생성 모형에서 결과의 품질과 다양성을 조절하는 자기 유도 방법을 제안했다. 자료의 의미가 매끄럽게 이어지도록 돕는 보조 과제를 이용하고, 효율적인 추가 학습 및 자료 생성 방법과 결합했다. 여러 설정의 실험에서 기존 방법보다 품질과 다양성의 균형을 개선하고 학습·생성 비용을 줄였다.[^p3] | 1저자 Jiwan Hur, 교신저자 Yunho Jeon·김준모 |
| 4 | 2022 | [UniCLIP: Unified Framework for Contrastive Language-Image Pre-training](https://doi.org/10.52202/068431-0074) · NeurIPS 2022 | 기존 방법이 이미지·글 관계와 이미지끼리의 관계를 따로 학습하면서 함께 활용할 수 있는 조합을 놓친다는 문제를 다뤘다. 두 종류의 관계를 하나의 공통 공간에서 학습하도록 통합하고, 자료를 변형한 방식과 자료 종류에 따라 생기는 차이를 조정하는 구성 요소를 제안했다. 이미지와 글을 따로 또는 함께 다루는 후속 과제에서 기존 학습 방법보다 좋은 성능을 보였다.[^p4] | 1저자 Janghyeon Lee·Jongsuk Kim(누리집 공동 기여), 마지막 저자 김준모 |
| 5 | 2024 | [StablePrompt : Automatic Prompt Tuning using Reinforcement Learning for Large Language Model](https://doi.org/10.18653/v1/2024.emnlp-main.551) · EMNLP 2024 | 언어 모델에 넣을 지시문을 강화학습으로 찾을 때 학습이 불안정해지는 문제를 다뤘다. 지시문을 찾는 모형과 목표 언어 모델 사이의 상호작용을 학습 문제로 구성하고, 기준이 되는 언어 모델을 이용해 행동 방법을 바꾸는 정도를 적응적으로 조절했다. 기존 언어 능력을 유지하며 지시문을 탐색하도록 했고, 글 분류·질의응답·글 생성 과제에서 기존 방법보다 좋은 성능을 보였다.[^p5] | 1저자 Minchan Kwon, 마지막 저자 김준모 |
| 6 | 2023 | [Reinforcement Learning-Based Black-Box Model Inversion Attacks](https://doi.org/10.1109/cvpr52729.2023.01964) · CVPR 2023 | 모형 내부를 보지 않고도 응답을 이용해 학습 자료의 비공개 정보를 복원하는 공격을 제안했다. 복원할 이미지의 표현을 찾는 과정을 강화학습 문제로 구성하고, 생성 이미지에 대한 모형의 신뢰도 점수를 보상으로 이용했다. 여러 자료와 모형을 대상으로 학습 정보가 복원되는 결과를 보여 주며, 개인정보를 보호하는 학습 방법의 필요성을 강조했다.[^p6] | 1저자 Gyojin Han, 마지막 저자 김준모 |
| 7 | 2026 | [PSGMM++: Pulmonary Segment Segmentation with Anatomical Insights](https://doi.org/10.1109/tmi.2026.3741804) · IEEE Transactions on Medical Imaging | 폐 안의 구역은 영상의 겉모습만으로 나누기 어렵고, 기관지나 동맥을 중심으로 하며 구역 경계가 그 중심에서 떨어져 있다는 해부학적 지식이 필요하다. 기관지·혈관의 위치를 이용하는 기존 모형에 이러한 위치 관계와 주변의 국소적 구조 정보를 명시적으로 결합했다. 각 구역의 확률 분포(가능한 값과 그 값이 나타날 가능성의 관계)를 생성하도록 학습하는 기준(EM 손실)도 새로 설계했다. 전체적으로 분할 성능이 향상되었다.[^p7] | 1저자 Seunghee Koh, 마지막 저자 김준모 |
| 8 | 2025 | [Tailored Channel Pruning: Achieve Targeted Model Complexity Through Adaptive Sparsity Regularization](https://doi.org/10.1109/access.2025.3529465) · IEEE Access | 제한된 계산 자원에 맞추어 신경망의 크기를 줄이면서 인식 성능을 유지하는 방법을 다뤘다. 목표 계산량과 매개변수(모형의 특성을 정하는 값) 수를 학습 중에 반영하고, 제거를 유도하는 정도를 적응적으로 조절하며 중요한 연결 값을 선택했다. 학습과 가지치기를 통합하여 목표 예산을 만족하는 신경망을 만들었으며, 이미지 분류 자료에서 방법의 효과를 보였다.[^p8] | 1저자 Suwoong Lee, 마지막 저자 김준모 |

## 교수와 전문 분야

김준모 교수는 서울대학교에서 학사 학위(1998), Massachusetts Institute of Technology에서 석사(2000)와 박사(2005) 학위를 받았다. 삼성종합기술원 연구원으로 근무한 뒤 2009년 KAIST 조교수로 부임했고, 부교수를 거쳐 2025년부터 교수로 재직한다.[^faculty] 전기및전자공학부 교수 목록은 주요 연구를 통계적 신호 처리(불확실성이 있는 관측 자료에서 통계적 방법으로 정보를 얻는 기술), 영상 처리와 컴퓨터 비전, 정보 이론(정보의 양과 전달·저장의 한계를 수학적으로 다루는 분야)으로 적는다.[^dept]

최근 논문에서 드러나는 전문 분야는 이미지·동작의 생성과 검색, 서로 다른 종류의 자료를 함께 배우는 방법, 언어 모델의 학습과 지시문 탐색, 인공지능의 정보 유출 위험과 계산 자원 절약이다. 자율주행 학습과 의료 영상 분할에서도 새로운 알고리즘을 개발한다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

연구실은 입체 시각 정보와 자율주행, 생성 모형과 확산 모형(자료에 잡음을 더하는 과정과 그 반대의 복원 과정을 이용해 새로운 자료를 생성하는 모형), 대형 언어 모델과 멀티모달 학습, 인공지능 안전, 의료·과학 인공지능을 최근 관심 분야로 제시한다.[^home] 대표 논문은 실제 주행 자료와 합성 자료를 결합하는 자율주행 학습, 기준 동작과 글 지시를 결합한 동작 검색, 폐 구역 분할, 계산 자원이 제한된 환경에서의 신경망 활용을 다룬다.[^p2][^p1][^p7][^p8]

## 구성원

2026년 11월 7일 연구실 Researchers·PhD Students·MS Students 기준이다. 박사후연구원 1명, 박사과정 17명(Part-time 4명 포함), 석사과정 6명이며, 연구 주제는 구성원 소개의 Research Interest 표기다.[^researchers][^phd][^ms] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Gyojin Han (한교진) | 박사후연구원 | Generative Model / 3D Vision | hangj0820@kaist.ac.kr | 1, 2, 3, 6 |
| Donghun Kim (김동훈) | 박사과정 |  | actruce@kaist.ac.kr |  |
| Jaesung Ahn (안재성) | 박사과정 |  | jaesung2@kaist.ac.kr |  |
| Seunghee Koh (고승희) | 박사과정 | AI safety / LLM unlearning / Machine unlearning / 3D medical segmentation | seunghee1215@kaist.ac.kr | 7 |
| Sojeong Song (송소정) | 박사과정 | 3D Vision / Self-supervised learning / Implicit neural representation | akqjq4985@kaist.ac.kr |  |
| Jiwan Hur (허지완) | 박사과정 | Generative Model / 3D Vision | jiwan.hur@kaist.ac.kr | 3 |
| Minchan Kwon (권민찬) | 박사과정 | LLM/VLM with RL | kmc0207@kaist.ac.kr | 5 |
| Dongjae Lee (이동재) | 박사과정 |  | jhtwosun@kaist.ac.kr |  |
| Junwon Ko (고준원) | 박사과정 | 3D Vision / Diffusion Model / Generated Image Detection | kojunewon@kaist.ac.kr |  |
| Minsu Kim (김민수) | 박사과정 | 3D Vision / Model Quantization | minshu.kim@kaist.ac.kr |  |
| Minseo Kim (김민서) | 박사과정 | Diffusion Models, Personalized Generative AI | alstj1571@kaist.ac.kr | 7 |
| Youngwoo Shin (신영우) | 박사과정 |  | yshin0917@kaist.ac.kr |  |
| Dongyeun Lee (이동연) | 박사과정 |  | ledoye@kaist.ac.kr |  |
| Changho Choi (최창호) | 박사과정 |  | ccho4702@kaist.ac.kr |  |
| Sungdae Sim (심성대) | 박사과정 (Part-time) |  |  |  |
| Jiho Chang (장지호) | 박사과정 (Part-time) |  | changjh@kaist.ac.kr |  |
| Gayoung Lee (이가영) | 박사과정 (Part-time) |  |  |  |
| Minki Jo (조민기) | 박사과정 (Part-time) |  | themis12@kaist.ac.kr |  |
| Hojoon Ki (기호준) | 석사과정 |  | joon4366@kaist.ac.kr |  |
| Yusung Ro (노유성) | 석사과정 | Explainable AI / MLLM | ysro3067@kaist.ac.kr |  |
| Hanna Bae (배한나) | 석사과정 | Autonomous driving / 3D vision | hannabae@kaist.ac.kr |  |
| Sungjae Choi (최성재) | 석사과정 |  | sungjae579@kaist.ac.kr |  |
| Sungwoo Kim (김성우) | 석사과정 |  | jinxyou@kaist.ac.kr |  |
| Minsung Bae (배민성) | 석사과정 |  | ms021230@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 Alumni에 게시된 2012–2026년의 69명이다. 학위·연도와 진로는 연구실이 적은 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Minju Jung (정민주) | Ph.D (2026) |  |
| Sunghyun Baek (백성현) | Ph.D (2026) | Samsung Research |
| Jongsuk Kim (김종석) | Ph.D (2026) | PYLER |
| Hyounguk Shon (손형욱) | Ph.D (2026) | Samsung Research |
| Gyojin Han (한교진) | Ph.D (2026) | PostDoc. at SIIT lab |
| Chanho Lee (이찬호) | Ph.D (2026) | Samsung Research |
| Jaehyun Choi (최재현) | Ph.D (2026) | ETRI |
| Suwoong Lee (이수웅) | Ph.D (2025) | ETRI |
| Gaeun Kim (김가은) | MS (2025) | KAI |
| HyeongGwon Hong (홍형권) | Ph.D (2025) | Samsung Research |
| Haeil Lee (이해일) | Ph.D (2025) | LG Energy Solution |
| Jaemyung Yu (유재명) | Ph.D (2025) | Naver AI Lab |
| Mintae Kang (강민태) | Ph.D (2025) |  |
| Seoyeon Gye (계서연) | MS (2025) | LG Electronics |
| Jae Young Lee (이재영) | Ph.D (2025) | Ainex |
| HanByel Cho (조한별) | Ph.D (2025) | Samsung Electronics |
| Yooshin Cho (조유신) | Ph.D (2024) | Samsung Research |
| Eojindl Yi (이어진들) | Ph.D (2024) | Samsung Research |
| Hyungmin Kim (김형민) | Ph.D (2024) | Samsung Electro-Mechanics |
| Seoyun Yang (양서윤) | MS (2024) | Naver |
| Jinsu Son (손진수) | MS (2024) | Hanwha Aerospace |
| Juseung Yun (윤주승) | Ph.D (2023) | LG AI Research |
| Juyoung Yang (양주영) | Ph.D (2023) | Hyundai Motors |
| Doyeon Kim (김도연) | Ph.D (2023) | Hyundai Motors |
| Woonghyun Ka (가웅현) | MS (2023) | Hyundai Motors |
| Jung-Jae Yu (유정재) | Ph.D (2022) | ETRI |
| Jung Eun (은정) | Ph.D (2022) | Woori Bank |
| Jinhyung Kim (김진형) | Ph.D (2022) | LG AI Research |
| Pyunghwan Ahn (안평환) | Ph.D (2022) | LG AI Research |
| DongGyu Joo (주동규) | Ph.D (2022) | Samsung Research |
| Kim, Hye-Jin S. (김혜진) | Ph.D (2022) | ETRI |
| Jeonghyo Ha (하정효) | Ph.D (2022) | SK Siltron |
| Jeongwoo Ju (주정우) | Ph.D (2022) | CPS Tech, Inc |
| Youngsoo Kim (김영수) | Ph.D (2022) | Hutom |
| Dongwon Oh (오동원) | MS (2022) | Vieworks |
| Sewhan Chun (천세환) | MS (2022) | NAVER CLOVA |
| ByungIn Yoo (유병인) | Ph.D (2021) | SAIT |
| Janghyeon Lee (이장현) | Ph.D (2021) | LG AI Research |
| Sihaeng Lee (이시행) | Ph.D (2021) | LG AI Research |
| Jihee Yoo (유지희) | Ph.D (2021) | ADD |
| Youngdong Kim (김영동) | Ph.D (2021) | Assistant Professor at HBNU |
| Beomyoung Kim (김범영) | MS (2021) | NAVER CLOVA |
| Sangeun Han (한상은) | MS (2021) | Samsung Research |
| Byungju Kim (김병주) | Ph.D (2020) | Mathpresso Inc. |
| Dongjae Lee (이동재) | MS (2020) | kakao |
| Hansang Lee (이한상) | Ph.D. (2019) |  |
| Jaeyoung Lee (이재영) | MS (2019) | Hanwha Aerospace |
| Sihyeon Seong (성시현) | Ph.D. (2019) | mofl Inc. |
| Yunho Jeon (전윤호) | Ph.D (2019) | Associate Professor at HBNU |
| Junho Yim (임준호) | Ph.D (2019) | LG Energy Solution |
| Haechang Jung (정해창) | MS (2018) | LG Electronics |
| Jiwhan Kim (김지환) | Ph.D (2018) | SAIT |
| Dongyoon Han (한동윤) | Ph.D (2018) | Naver AI Lab |
| Heechul Jung (정희철) | Ph.D. (2018) | Associate Professor at KNU |
| Jaemyung Lee (이재명) | MS (2018) | Kakao Brain |
| Jongho Lee (이종호) | MS (2018) | TmaxSoft |
| Gayoung Lee (이가영) | MS (2016) | Naver CLOVA OCR |
| Sunjeong Park (박선정) | MS (2015) | UBI sound |
| Wonjun Hwang (황원준) | Ph.D. (2015) | Professor at Korea University |
| Youngwook Kee (기영욱) | Ph.D. (2015) | Memorial Sloan Kettering Cancer Center |
| Hyungseok Lee (이형석) | MS (2015) | Creverse |
| Sojung Yun (윤소정) | MS (2015) | Samsung Electronics |
| Joong Won Hwang (황중원) | MS (2014) | ETRI |
| Jong Hoon Kwak (곽종훈) | MS (2014) | KETI |
| Sungryull Sohn (손성열) | MS (2013) | PhD Course @ Univ. of Michigan |
| Ilma Andayana | MS (2012) |  |
| Kibok Lee (이기복) | MS (2012) | Associate Professor at Yonsei University |
| Dewey Ho Lee (이호) | MS (2012) | Waymo |
| Sandeul Kang (강산들) | MS (2012) | Hyundai Motors |

## 최근 논문 목록 (2021–2026)

연구실 Journals·Conferences의 2021–2026년 구역에서 학술지 16건과 학회 93건, 총 109건을 싣는다. 연도·제목·저자·발표처는 누리집 표기이며, DOI는 해당 논문의 식별 주소다.[^journals][^conferences][^bibliography] “채택”은 연구실 소식이 채택을 알린 학회 항목이고, “연구실 기재”는 누리집에 적힌 발표처이며, “사전 공개본 연결”은 연구실이 연결한 판본이 사전 공개본인 항목이다.[^home][^conferences]

**2026**

- Gyojin Han\*, Jongsuk Kim\*, Junmo Kim (equally contributed by the authors\*). "TransMotion: Text-Guided Transformation Learning for Composed Human Motion Retrieval". Applied Sciences. DOI: <https://doi.org/10.3390/app162110842>.
- Haeil Lee\*, Hansang Lee\*, and Junmo Kim (equally contributed by the authors\*). "The Effects of Mixed Sample Data Augmentation Are Class Dependent". IEEE Access. DOI: <https://doi.org/10.1109/access.2026.3731600>.
- Seunghee Koh, Chanho Lee, Jaehyun Choi, Jae Young Lee, Minseo Kim, Youngno Yoon, Changyoung Lee, and Junmo Kim. "PSGMM++: Pulmonary Segment Segmentation with Anatomical Insights". IEEE Transactions on Medical Imaging. DOI: <https://doi.org/10.1109/tmi.2026.3741804>.
- Dongyeun Lee, Amir Zandieh, Vahab Mirrokni, Junmo Kim†, and Insu Han† (Corresponding authors†). "HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택). DOI: <https://doi.org/10.48550/arxiv.2607.03012>.
- Jiwan Hur, Dong-Jae Lee, Dongyeun Lee, Gyojin Han, and Junmo Kim. "SCALE: Improving Guidance-Free Visual Generation via Self-Contrastive Alignment for Likelihood Estimation". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택).
- Dong-Jae Lee and Junmo Kim. "Module Specialization in Transformer Factual Recall under Correlated Fact Distributions". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택).
- Gyojin Han\*, Dong-Jae Lee\*, Changho Choi\*, Jongsuk Kim\*, and Junmo Kim (equally contributed by the authors\*). "Continuous Audio Thinking for Large Audio Language Models". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택). DOI: <https://doi.org/10.48550/arxiv.2606.18273>.
- Youngwoo Shin, Yusung Ro, Minseo Kim, and Junmo Kim. "Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택). DOI: <https://doi.org/10.48550/arxiv.2610.01595>.
- Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, and Junmo Kim. "Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context RL". NeurIPS 2026 Spotlight (Conference on Neural Information Processing Systems) (채택).
- Gayoung Lee, Junho Kim, Jin-Hwa Kim†, and Junmo Kim† (Corresponding authors†). "Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction". NeurIPS 2026 (Conference on Neural Information Processing Systems) (채택).
- Sungjae Choi\*, Hanna Bae\*, Sunghyun Baek and Junmo Kim (equally contributed by the authors\*). "VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges". ACCV 2026 (The 18th Asian Conference on Computer Vision) (채택).
- Jongsuk Kim, Qiyu Wu†, Zhuoyuan Mao, Hiromi Wakaki, Junmo Kim and Yuki Mitsufuji. "MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations". EMNLP 2026 (The 2026 Conference on Empirical Methods in Natural Language Processing) (채택).
- Seunghee Koh, Sungjae Choi, Minchan Kwon, Sunghyun Baek and Junmo Kim. "`</think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination`". EMNLP 2026 (The 2026 Conference on Empirical Methods in Natural Language Processing) (채택).
- Junwon Ko, Dong-Jae Lee, Minchan Kwon, Sunghyun Baek and Junmo Kim. "Direct Diversity Optimization for Diverse Successful Trajectories in Preference Post-Training". EMNLP 2026 (The 2026 Conference on Empirical Methods in Natural Language Processing) (채택).
- Dong-Jae Lee\*, Sunghyun Baek\* and Junmo Kim (equally contributed by the authors\*). "IWP: Token Pruning as Implicit Weight Pruning in Large Vision Language Models". EMNLP 2026 Findings (The 2026 Conference on Empirical Methods in Natural Language Processing Findings) (채택).
- Youngtaek Oh, Qiyu Wu, Hiromi Wakaki, Junmo Kim and Yuki Mitsufuji. "Syn-Omni: Structured Specialization and Progressive Collaboration for Omnimodal Embeddings". EMNLP 2026 Findings (The 2026 Conference on Empirical Methods in Natural Language Processing Findings) (채택).
- Dong-Jae Lee\*, Gyojin Han\* and Junmo Kim (equally contributed by the authors\*). "Calibration-Free Early Stopping for Chain-of-Thought Reasoning via E-processes". EMNLP 2026 Findings (The 2026 Conference on Empirical Methods in Natural Language Processing Findings) (채택).
- Sungjae Choi, Seunghee Koh and Junmo Kim. "PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting". BMVC 2026 (The 37th British Machine Vision Conference) (채택).
- Myungchul Kim, Kwanyong Park, Junmo Kim† and In So Kweon† (Corresponding authors†). "ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search". ECCV 2026 (The 19th European Conference on Computer Vision). DOI: <https://doi.org/10.1007/978-3-032-37026-6_7>.
- Minchan Kwon, Sunghyun Baek, Minseo Kim, Jaemyung Yu, Dongyoon Han†, and Junmo Kim† (Corresponding authors†). "Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance". ICML 2026 Spotlight (Forty-Third International Conference on Machine Learning) (채택). DOI: <https://doi.org/10.48550/arxiv.2605.00553>.
- Seunghee Koh, Sunghyun Baek, Youngdong Kim†, and Junmo Kim† (Corresponding authors†). "Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens". ACL 2026 (The 64th Annual Meeting of the Association for Computational Linguistics). DOI: <https://doi.org/10.18653/v1/2026.acl-long.1175>.
- Sungjae Choi, Seunghee Koh, and Junmo Kim. "PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting". CVPRW 2026 (CVPR Workshop on 3D from multi-view and sensors) (연구실 기재).
- Yusung Ro, Jaehyun Choi, and Junmo Kim. "Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP". CVPR Findings 2026 (IEEE Conference on Computer Vision and Pattern Recognition Findings) (연구실 기재).
- Gyojin Han and Junmo Kim. "Cross-Axis Feature Fusion with Joint-Wise Motion Difference Prediction for Text-Based 3D Human Motion Editing". CVPR 2026 (IEEE Conference on Computer Vision and Pattern Recognition) (연구실 기재).
- Jaehyun Choi, Jiwan Hur, Gyojin Han, Jaemyung Yu, and Junmo Kim. "PRISM: Video Dataset Condensation with Progressive Refinement and Insertion for Sparse Motion". CVPR 2026 (IEEE Conference on Computer Vision and Pattern Recognition) (사전 공개본 연결). DOI: <https://doi.org/10.48550/arxiv.2505.22564>.
- Minseo Kim, Minchan Kwon, Dongyueun Lee, Yunho Jeon†, and Junmo Kim† (Corresponding authors†). "ConceptPrism: Concept Disentanglement in Personalized Diffusion Models via Residual Token Optimization". CVPR 2026 (IEEE Conference on Computer Vision and Pattern Recognition) (사전 공개본 연결). DOI: <https://doi.org/10.48550/arxiv.2602.19575>.
- Youngwoo Shin\*, Jiwan Hur\*, and Junmo Kim (equally contributed by the authors\*). "SSG: Scaled Spatial Guidance for Multi-Scale Visual Autoregressive Generation". ICLR 2026 (International Conference on Learning Representations) (채택).
- Minsu Kim, Dongyeun Lee, Jaemyung Yu, Jiwan Hur, Giseop Kim, and Junmo Kim. "Inlier-Centric Post-Training Quantization for Object Detection Models". ICLR 2026 (International Conference on Learning Representations) (채택).
- Sunghyun Baek, Jaemyung Yu, Seunghee Koh, Minsu Kim, Hyeonseong Jeon, and Junmo Kim. "IMSE: Intrinsic Mixture of Spectral Experts Fine-tuning for Test-Time Adaptation". ICLR 2026 (International Conference on Learning Representations) (채택).
- Hojoon Ki, Jongsuk Kim, Minchan Kwon, and Junmo Kim. "FxSearcher: gradient-free text-driven audio transformation". ICASSP 2026 (International Conference on Acoustics, Speech, and Signal Processing). DOI: <https://doi.org/10.1109/icassp55912.2026.11460939>.
- Sungwoo Kim, and Junmo Kim. "PHYSIO-MAMBA: Physiologically-Guided MAMBA Network for Continuous Calibration-free ABP Reconstruction from PPG". ICASSP 2026 (International Conference on Acoustics, Speech, and Signal Processing). DOI: <https://doi.org/10.1109/icassp55912.2026.11463566>.

**2025**

- Minju Jung, Sunghyun Baek, Yunho Jeon† and Junmo Kim† (Corresponding authors†). "Prior knowledge of layer-specific pruning numbers guarantees effective random pruning at initialization". Pattern Analysis and Applications. DOI: <https://doi.org/10.1007/s10044-025-01574-y>.
- Mintae Kang and Junmo Kim. "Enhancing self-supervised visual representation learning through adversarially generated examples". Neural Computing and Applications. DOI: <https://doi.org/10.1007/s00521-025-11236-z>.
- Suwoong Lee, Yunho Jeon, Seungjae Lee, and Junmo Kim. "Tailored Channel Pruning: Achieve Targeted Model Complexity Through Adaptive Sparsity Regularization". IEEE Access. DOI: <https://doi.org/10.1109/access.2025.3529465>.
- Minchan Kwon, Junwon Ko, Kangil Kim†, and Junmo Kim† (Corresponding authors†). "Preference Distillation via Value based Reinforcement Learning". NeurIPS 2025 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/085713-3549>.
- Dong-Jae Lee, Jiwan Hur, Jaehyun Choi, Jaemyung Yu, and Junmo Kim. "Frequency-Aware Token Reduction for Efficient Vision Transformer". NeurIPS 2025 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/085713-1144>.
- Chenshuang Zhang, Kang Zhang, Joon Son Chung†, In So Kweon†, Junmo Kim†, and Chengzhi Mao† (Corresponding authors†). "Video Diffusion Models Excel at Tracking Similar-Looking Objects Without Supervision". NeurIPS 2025 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/085713-1341>.
- Changho Choi\*, Youngwoo Shin\*, Gyojin Han, Dong-Jae Lee, and Junmo Kim (equally contributed by the authors\*). "B4DL: A Benchmark for 4D LiDAR LLM in Spatio-Temporal Understanding". ACMMM 2025 (ACM International Conference on Multimedia) (연구실 기재).
- Yooshin Cho, Hanbyel Cho, Janghyeon Lee, HyeongGwon Hong, Jaesung Ahn, and Junmo Kim. "Controllable Feature Whitening for Hyperparameter-Free Bias Mitigation". ICCV 2025 (IEEE International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv51701.2025.00433>.
- Jongsuk Kim, Jae Young Lee, Gyojin Han, Dong-Jae Lee, Minki Jeong, and Junmo Kim. "SynAD: Enhancing Real-World End-to-End Autonomous Driving Models through Synthetic Data Integration". ICCV 2025 (IEEE International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv51701.2025.02337>.
- Dongyeun Lee, Jiwan Hur, Hyounguk Shon, Jae Young Lee, and Junmo Kim. "DMQ: Dissecting Outliers of Diffusion Models for Post-Training Quantization". ICCV 2025 (IEEE International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv51701.2025.01720>.
- Chaeyoung Jung, Hojoon Ki, Ji-Hoon Kim, Junmo Kim†, and Joon son Chung† (Corresponding authors†). "InfiniteAudio: Infinite-Length Audio Generation with Consistency". INTERSPEECH 2025. DOI: <https://doi.org/10.21437/interspeech.2025-209>.
- Jongsuk Kim, Jaemyung Yu, Minchan Kwon, and Junmo Kim. "FairASR: Fair Audio Contrastive Learning for Automatic Speech Recognition". INTERSPEECH 2025. DOI: <https://doi.org/10.21437/interspeech.2025-2590>.
- Minseo Kim, Minchan Kwon, Dongyeun Lee, Yunho Jeon†, and Junmo Kim† (Corresponding authors†). "Comparison Reveals Commonality: Customized Image Generation through Contrastive Inversion". CVPRW 2025 (CVPR Workshop on AI for Content Creation) (사전 공개본 연결). DOI: <https://doi.org/10.48550/arxiv.2508.07755>.
- JooHyun Kwon\*, Hanbyel Cho\*, and Junmo Kim (equally contributed by the authors\*). "Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation". CVPR 2025 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52734.2025.02501>.
- Jaehyun Choi\*, Junwon Ko\*, Dong-Jae Lee\*, and Junmo Kim (equally contributed by the authors\*). "AH-OCDA: Amplitude-based Curriculum Learning and Hopfield Segmentation Model for Open Compound Domain Adaptation". WACV 2025 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv61041.2025.00803>.
- Haeil Lee\*, Hansang Lee\*, Seoyeon Gye, and Junmo Kim (equally contributed by the authors\*). "Beta Sampling is All You Need: Efficient Image Generation Strategy for Diffusion Models using Stepwise Spectral Analysis". WACV 2025 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv61041.2025.00414>.
- Seoyeon Gye\*, Junwon Ko\*, Hyounguk Shon\*, Minchan Kwon, and Junmo Kim (equally contributed by the authors\*). "Reducing the Content Bias for AI-generated Image Detection". WACV 2025 Oral (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv61041.2025.00049>.

**2024**

- Hyungmin Kim, Sungho Suh, Sunghyun Baek, Daehwan Kim, Daun Jeong, Hansang Cho, and Junmo Kim. "AI-KD: Adversarial learning and Implicit regularization for self-Knowledge Distillation". Knowledge-Based Systems. DOI: <https://doi.org/10.1016/j.knosys.2024.111692>.
- Chenshuang Zhang, Chaoning Zhang, Kang Zhang, Axi Niu, Junmo Kim†, and In So Kweon† (Corresponding authors†). "Towards Understanding Dual BN In Hybrid Adversarial Training". Transactions on Machine Learning Research.
- Hyungmin Kim, Donghun Kim, Pyunghwan Ahn, Sungho Suh, Hansang Cho, and Junmo Kim. "ContextMix: A Context-Aware Data Augmentation Method for Industrial Visual Inspection Systems". Engineering Applications of Artificial Intelligence. DOI: <https://doi.org/10.1016/j.engappai.2023.107842>.
- Jiwan Hur, Dong-Jae Lee, Gyojin Han, Jaehyun Choi, Yunho Jeon†, and Junmo Kim†(Corresponding authors†). "Unlocking the Capabilities of Masked Generative Models for Image Synthesis via Self-Guidance". NeurIPS 2024 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/079017-4163>.
- Jaemyung Yu, Jaehyun Choi, Dong-Jae Lee, HyeongGwon Hong, and Junmo Kim​. "Self-supervised Transformation Learning for Equivariant Representations". NeurIPS 2024 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/079017-2643>.
- Youngtaek Oh, Jae Won Cho, Dong-Jin Kim, In So Kweon†, and Junmo Kim†(Corresponding authors†). "Preserving Multi-Modal Capabilities of Pre-trained VLMs for Improving Vision-Linguistic Compositionality". EMNLP 2024 (The 2024 Conference on Empirical Methods in Natural Language Processing). DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.1062>.
- Minchan Kwon, Gaeun Kim, Jongsuk Kim, Haeil Lee, and Junmo Kim. "StablePrompt : Automatic Prompt Tuning using Reinforcement Learning for Large Language Model". EMNLP 2024 (The 2024 Conference on Empirical Methods in Natural Language Processing). DOI: <https://doi.org/10.18653/v1/2024.emnlp-main.551>.
- Sojeong Song\*, Seoyun Yang\*, Chang D. Yoo†, and Junmo Kim†(equally contributed by the authors\*, Corresponding authors†). "Implicit Steganography Beyond the Constraints of Modality". ECCV 2024 (European Conference on Computer Vision). DOI: <https://doi.org/10.1007/978-3-031-73016-0_17>.
- Gyojin Han, Jiwan Hur, Jaehyun Choi, and Junmo Kim. "Learning Neural Deformation Representation for 4D Dynamic Shape Generation". ECCV 2024 (European Conference on Computer Vision). DOI: <https://doi.org/10.1007/978-3-031-73220-1_11>.
- Jongsuk Kim, Jiwon Shin, and Junmo Kim. "AVCap: Leveraging Audio-Visual Features as Text Tokens for Captioning​​". INTERSPEECH 2024. DOI: <https://doi.org/10.21437/interspeech.2024-526>.
- Hyounguk Shon, Seunghee Koh, Yunho Jeon, and Junmo Kim. "Neural Vicinal Risk Minimization: Noise-robust Distillation for Noisy Labels". IJCAIW 2024 (IJCAI Workshop on Artificial Intelligence Safety) (연구실 기재).
- Jongsuk Kim\*, Hyeongkeun Lee\*, Kyeongha Rho\*, Junmo Kim, and Joon Son Chung(equally contributed by the authors\*). "EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning". ICML 2024 (The International Conference on Machine Learning​) (사전 공개본 연결). DOI: <https://doi.org/10.48550/arxiv.2403.09502>.
- Chenshuang Zhang, Fei Pan, Junmo Kim\*, In So Kweon\*, and Chengzhi Mao\* (Corresponding authors\*). "ImageNet-D: Benchmarking Neural Network Robustness on Diffusion Synthetic Object". CVPR 2024 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52733.2024.02055>.
- Woonghyun Ka\*, Jae Young Lee\*, Jaehyun Choi, and Junmo Kim (equally contributed by the authors\*). "Stereo-Matching Knowledge Distilled Monocular Depth Estimation Filtered by Multiple Disparity Consistency". ICASSP 2024 (IEEE International Conference on Acoustics, Speech and Signal Processing). DOI: <https://doi.org/10.1109/icassp48485.2024.10448168>.
- Chanho Lee, Jinsu Son, Hyounguk Shon, Yunho Jeon, and Junmo Kim. "FRED: Towards a Full Rotation-Equivariance in Aerial Image Object Detection". AAAI 2024 (The Thirty-Eighth AAAI Conference on Artificial Intelligence). DOI: <https://doi.org/10.1609/aaai.v38i4.28069>.
- HyeongGwon Hong, Yooshin Cho, Hanbyel Cho, Jaesung Ahn, and Junmo Kim. "Foreseeing Reconstruction Quality of Gradient Inversion: An Optimization Perspective". AAAI 2024 (The Thirty-Eighth AAAI Conference on Artificial Intelligence). DOI: <https://doi.org/10.1609/aaai.v38i11.29140>.
- Jae Young Lee\*, Woonghyun Ka\*, Jaehyun Choi, and Junmo Kim (equally contributed by the authors\*). "Modeling Stereo-Confidence Out of the End-to-End Stereo-Matching Network via Disparity Plane Sweep". AAAI2024 (The Thirty-Eighth AAAI Conference on Artificial Intelligence). DOI: <https://doi.org/10.1609/aaai.v38i4.28071>.
- Youngbeom Yoo\*, Jae Young Lee\*, Dong-Jae Lee, Jiwoon Jeon, and Junmo Kim (equally contributed by the authors\*). "Real-Time Polyp Detection in Colonoscopy using Lightweight Transformer". WACV2024 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv57701.2024.00763>.
- Jiwan Hur, Jaehyun Choi, Gyojin Han, Dong-Jae Lee, and Junmo Kim. "Expanding Expressiveness of Diffusion Models with Limited Data via Self-Distillation based Fine-Tuning". WACV2024 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv57701.2024.00495>.

**2023**

- Jae Young Lee, Jiwan Hur, Jaehyun Choi, Rae-Hong Park, and Junmo Kim. "Multi-Scale Foreground-Background Separation for Light Field Depth Estimation with Deep Convolutional Networks". Pattern Recognition Letters. DOI: <https://doi.org/10.1016/j.patrec.2023.05.014>.
- Yooshin Cho, Hanbyel Cho, Hyeong Gwon Hong, Jaesung Ahn, Dongmin Cho, JungWoo Chang, and Junmo Kim. "Localization using Multi-Focal Spatial Attention for Masked Face Recognition". FG 2023 (IEEE International Conference on Automatic Face and Gesture Recognition). DOI: <https://doi.org/10.1109/fg57933.2023.10042672>.
- Hanbyel Cho, Jaesung Ahn, Yooshin Cho, and Junmo Kim. "Video Inference for Human Mesh Recovery with Vision Transformer". FG 2023 (IEEE International Conference on Automatic Face and Gesture Recognition). DOI: <https://doi.org/10.1109/fg57933.2023.10042731>.
- Hanbyel Cho and Junmo Kim. "Generative Approach for Probabilistic Human Mesh Recovery using Diffusion Models". ICCVW 2023 (ICCV Workshop on Computer Vision for Metaverse). DOI: <https://doi.org/10.1109/iccvw60793.2023.00452>.
- Seunghee Koh, Hyounguk Shon, Janghyeon Lee, Hyeong Gwon Hong, and Junmo Kim. "Disposable Transfer Learning for Selective Source Task Unlearning". ICCV 2023 (IEEE International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv51070.2023.01079>.
- Hyungmin Kim, Sungho Suh, Daehwan Kim, Daun Jeong, Hansang Cho, and Junmo Kim. "Proxy Anchor-based Unsupervised Learning for Continuous Generalized Category Discovery". ICCV 2023 (IEEE International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv51070.2023.01530>.
- Doyeon Kim, Dongyeun Lee, Donggyu Joo, and Junmo Kim. "Training Cartoonization Network without Cartoon". ICIP 2023 (IEEE International Conference on Image Processing). DOI: <https://doi.org/10.1109/icip49359.2023.10223141>.
- Gyojin Han\*, Jaehyun Choi\*, Hyeong Gwon Hong, and Junmo Kim (equally contributed by the authors\*). "Data Poisoning Attack Aiming the Vulnerability of Continual Learning". ICIP 2023 (IEEE International Conference on Image Processing). DOI: <https://doi.org/10.1109/icip49359.2023.10222168>.
- Gyojin Han, Dong-Jae Lee, Jiwan Hur, Jaehyun Choi, and Junmo Kim. "Deep Cross-Modal Steganography Using Neural Representations". ICIP 2023 Oral (IEEE International Conference on Image Processing). DOI: <https://doi.org/10.1109/icip49359.2023.10222113>.
- Hanbyel Cho, Yooshin Cho, Jaesung Ahn, and Junmo Kim. "Implicit 3D Human Mesh Recovery using Consistency with Pose and Shape from Unseen-view". CVPR 2023 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52729.2023.02026>.
- Dongyeun Lee, Jae Young Lee, Doyeon Kim, Jaehyun Choi, Jaejun Yoo, and Junmo Kim. "Fix the Noise: Disentangling Source Feature for Controllable Domain Translation". CVPR 2023 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52729.2023.01367>.
- Gyojin Han, Jaehyun Choi, Haeil Lee, and Junmo Kim. "Reinforcement Learning-Based Black-Box Model Inversion Attacks". CVPR 2023 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52729.2023.01964>.
- Eojindl Yi, and Junmo Kim. "Test‐Time Synthetic‐to‐Real Adaptive Depth Estimation". ICRA 2023 (IEEE International Conference on Robotics and Automation). DOI: <https://doi.org/10.1109/icra48891.2023.10160773>.
- Dong-Jae Lee\*, Jae Young Lee\*, Hyounguk Shon, Eojindl Yi, Yeong-Hun Park, Sung-Sik Cho, and Junmo Kim (equally contributed by the authors\*). "Lightweight Monocular Depth Estimation via Token-Sharing Transformer". ICRA 2023 (IEEE International Conference on Robotics and Automation). DOI: <https://doi.org/10.1109/icra48891.2023.10160566>.
- Jinhyung Kim, Taeoh Kim , Minho Shim , Dongyoon Han , Dongyoon Wee, and Junmo Kim. "Frequency Selective Augmentation for Video Representation Learning". AAAI 2023 (The Thirty-Seventh AAAI Conference on Artificial Intelligence). DOI: <https://doi.org/10.1609/aaai.v37i1.25194>.
- Jiwan Hur\*, Jae Young Lee\*, Jaehyun Choi, and Junmo Kim (equally contributed by the authors\*). "I See-Through You: A Framework for Removing Foreground Occlusion in Both Sparse and Dense Light Field Images". WACV2023 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv56688.2023.00031>.

**2022**

- Youngsoo Kim, Jeonghyo Ha, Yooshin Cho, and Junmo Kim. "Unsupervised Blur Kernel Estimation and Correction for Blind Super-Resolution". IEEE Access. DOI: <https://doi.org/10.1109/access.2022.3170053>.
- Hyejin S. Kim, Yoonsoo Han, and Junmo Kim. "3D Measurement using a Single Image for Smart Manufacturing of Microscopic Products in a Ceramic Powder Pressing Process". International Journal of Precision Engineering and Manufacturing-Green Technology. DOI: <https://doi.org/10.1007/s40684-022-00434-y>.
- Pyunghwan Ahn, Juyoung Yang, Eojindl Yi, Chanho Lee, and Junmo Kim. "Projection-Based Point Convolution for Efficient Point Cloud Segmentation". IEEE Access. DOI: <https://doi.org/10.1109/access.2022.3144449>.
- Jeongwoo Ju, Heechul Jung, and Junmo Kim. "Extending Contrastive Learning to Unsupervised Redundancy Identification". Applied Sciences. DOI: <https://doi.org/10.3390/app12042201>.
- Jeongwoo Ju, Heechul Jung, Yoonju Oh, and Junmo Kim. "Extending Contrastive Learning to Unsupervised Coreset Selection". IEEE Access. DOI: <https://doi.org/10.1109/access.2022.3142758>.
- Hansang Lee, Haeil Lee, Helen Hong, and Junmo Kim. "Noisy Label Classification Using Label Noise Selection with Test-Time Augmentation Cross-Entropy and NoiseMix Learning". MICCAIW 2022 (MICCAI Workshop on Data Augmentation, Labelling, and Imperfections). DOI: <https://doi.org/10.1007/978-3-031-17027-0_8>.
- Gyojin Han\*, Jaehyun Choi\*, Hyeong Gwon Hong, and Junmo Kim (equally contributed by the authors\*). "Training Time Adversarial Attack Aiming the Vulnerability of Continual Learning". NeurIPSW 2022 (NeurIPS Workshop on Machine Learning Safety) (연구실 기재).
- Janghyeon Lee\*, Jongsuk Kim\*, Hyounguk Shon, Bumsoo Kim, Seung Hwan Kim, Honglak Lee, and Junmo Kim (equally contributed by the authors\*). "UniCLIP: Unified Framework for Contrastive Language-Image Pre-training". NeurIPS 2022 (Conference on Neural Information Processing Systems). DOI: <https://doi.org/10.52202/068431-0074>.
- Seung Ho Na, Hyeong Gwon Hong, Junmo Kim and Seungwon Shin. "Closing the Loophole: Rethinking Reconstruction Attacks in Federated Learning from a Privacy Standpoint". ACSAC 2022 (Annual Computer Security Applications Conference). DOI: <https://doi.org/10.1145/3564625.3564657>.
- Hyounguk Shon, Janghyeon Lee, Seung Hwan Kim, and Junmo Kim. "DLCFT: Deep Linear Continual Fine-Tuning for General Incremental Learning". ECCV 2022 (European Conference on Computer Vision). DOI: <https://doi.org/10.1007/978-3-031-19827-4_30>.
- Juseung Yun, Janghyeon Lee, Hyounguk Shon, Eojindl Yi, Seung Hwan Kim, and Junmo Kim. "On the Angular Update and Hyperparameter Tuning of a Scale-Invariant Network". ECCV 2022 (European Conference on Computer Vision). DOI: <https://doi.org/10.1007/978-3-031-19775-8_8>.
- Sihaeng Lee\*, Eojindl Yi\*, Janghyeon Lee, and Junmo Kim. "Multi-Scaled and Densely Connected Locally Convolutional Layers for Depth Completion". IROS 2022 (IEEE/RSJ International Conference on Intelligent Robots and Systems). DOI: <https://doi.org/10.1109/iros47612.2022.9982179>.
- Eojindl Yi, and Junmo Kim. "Subspace-based Feature Alignment for Unsupervised Domain Adaptation". IROS 2022 (IEEE/RSJ International Conference on Intelligent Robots and Systems). DOI: <https://doi.org/10.1109/iros47612.2022.9981324>.
- Sewhan Chun, Jae Young Lee, and Junmo Kim. "Cyclic Test Time Augmentation with Entropy Weight Method". UAI 2022 (The Conference on Uncertainty in Artificial Intelligence) (연구실 기재).
- Yooshin Cho, Youngsoo Kim, Hanbyel Cho, Jaesung Ahn, Hyeong Gwon Hong, and Junmo Kim. "Rethinking Efficacy of Softmax for Lightweight Non-Local Neural Networks". ICIP 2022 (IEEE International Conference on Image Processing). DOI: <https://doi.org/10.1109/icip46576.2022.9897905>.
- Donggyu Joo, Sunghyun Baek, and Junmo Kim. "Which Metrics For Network Pruning: Final Accuracy? or Accuracy Drop?". ICIP 2022 (IEEE International Conference on Image Processing). DOI: <https://doi.org/10.1109/icip46576.2022.9898051>.
- Dongyeun Lee, Jae Young Lee, Doyeon Kim, Jaehyun Choi, Junmo Kim. "Fix the Noise: Disentangling Source Feature for Transfer Learning of StyleGAN". CVPRW 2022 Best Paper (CVPR Workshop on AI for Content Creation) (사전 공개본 연결). DOI: <https://doi.org/10.48550/arxiv.2204.14079>.
- Donggyu Joo, Doyeon Kim, Eojindl Yi and Junmo Kim. "Linear Combination Approximation of Feature for Channel Pruning". CVPRW 2022 (Efficient Deep Learning for Computer Vision CVPR Workshop). DOI: <https://doi.org/10.1109/cvprw56347.2022.00313>.
- Beomyoung Kim, Youngjoon Yoo, Chaeeun Rhee and Junmo Kim. "Beyond Semantic to Instance Segmentation: Weakly-Supervised Instance Segmentation via Semantic Knowledge Transfer and Self-Refinement". CVPR 2022 (IEEE Conference on Computer Vision and Pattern Recognition). DOI: <https://doi.org/10.1109/cvpr52688.2022.00424>.
- Eojindl Yi, Juyoung Yang and Junmo Kim. "Enhanced Prototypical Learning for Unsupervised Domain Adaptation in LiDAR Semantic Segmentation". ICRA 2022 (IEEE International Conference on Robotics and Automation). DOI: <https://doi.org/10.1109/icra46639.2022.9811838>.
- Beomyoung Kim, Janghyeon Lee, Sihaeng Lee, Doyeon Kim and Junmo Kim. "TricubeNet: 2D Kernel-Based Object Representation for Weakly-Occluded Oriented Object Detection". WACV 2022 (Winter Conference on Applications of Computer Vision). DOI: <https://doi.org/10.1109/wacv51458.2022.00348>.

**2021**

- Yunho Jeon and Junmo Kim. "Integrating Multiple Receptive Fields through Grouped Active Convolution". IEEE Transactions on Pattern Analysis and Machine Intelligence. DOI: <https://doi.org/10.1109/tpami.2020.2995864>.
- Jung-Jae Yu, Juwon Lee, and Junmo Kim. "SinBlowUp: Outpainting from Learning a Single Image". ICCE-Asia 2021 (IEEE International Conference on Consumer Electronics-Asia). DOI: <https://doi.org/10.1109/icce-asia53811.2021.9641974>.
- Juyoung Yang, Pyunghwan Ahn, Doyeon Kim, Haeil Lee and Junmo Kim. "Progressive Seed Generation Auto-encoder for Unsupervised Point Cloud Learning". ICCV 2021 (IEEE Conference on International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv48922.2021.00635>.
- Hanbyel Cho, Yooshin Cho, Jaemyung Yu and Junmo Kim. "Camera Distortion-aware 3D Human Pose Estimation in Video with Optimization-based Meta-Learning". ICCV 2021 (IEEE Conference on International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv48922.2021.01098>.
- Yooshin Cho, Hanbyel Cho, Youngsoo Kim and Junmo Kim. "Improving Generalization of Batch Whitening by Convolutional Unit Optimization". ICCV 2021 (IEEE Conference on International Conference on Computer Vision). DOI: <https://doi.org/10.1109/iccv48922.2021.00527>.

## 수상과 선정

교수 소개의 2023·2025년 수상과 학회 목록의 2022년 Best Paper 표기다. 교수 수상의 연도는 누리집의 연도 표기이며 날짜는 게시되어 있지 않다.[^faculty][^conferences]

- 2025 · 김준모, KAIST EE Outstanding Lecture Award
- 2023 · 김준모, Korean Artificial Intelligence Association Academic Award
- 2022 · Fix the Noise: Disentangling Source Feature for Transfer Learning of StyleGAN, CVPRW 2022 Best Paper (CVPR Workshop on AI for Content Creation)

## 소식

연구실 첫 화면의 2026년 1–9월 학회 논문 채택 소식이다.[^home]

- 2026-09 · NeurIPS 2026에 논문 7편 채택 (Spotlight 포함)
- 2026-09 · ACCV 2026에 논문 1편 채택
- 2026-08 · EMNLP 2026에 논문 6편 채택
- 2026-08 · BMVC 2026에 논문 1편 채택
- 2026-06 · ECCV 2026에 논문 1편 채택
- 2026-05 · ICML 2026에 논문 1편 채택 (Spotlight)
- 2026-04 · ACL 2026에 논문 1편 채택
- 2026-03 · CVPR 2026에 논문 4편 채택
- 2026-01 · ICLR 2026에 논문 3편 채택
- 2026-01 · ICASSP 2026에 논문 2편 채택

## 연락과 위치

- 교수 이메일: junmo.kim@kaist.ac.kr[^faculty]
- 교수 연구실: IT융합빌딩 N1 210호, 전화 +82-042-350-3488[^faculty]
- 연구실: ITC Building N1 214호, 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^home]
- 연구실 전화: +82-042-350-8088[^home]

## 각주
[^intro]: SIIT, 연구실 소개: 컴퓨터 비전·멀티모달 학습·인공지능 안전의 원리와 응용. <https://siit.kaist.ac.kr/>. 관측일 2026-11-07.
[^home]: SIIT, 첫 화면 연구 소개·News·연락과 위치. <https://siit.kaist.ac.kr/>. 관측일 2026-11-07.
[^faculty]: SIIT, Faculty, Junmo Kim의 연구 분야·학력·경력·수상·연락처. <https://siit.kaist.ac.kr/members/faculty>. 관측일 2026-11-07.
[^dept]: KAIST 전기및전자공학부, 교수 목록, 김준모. <https://ee.kaist.ac.kr/professor-s1/>. 관측일 2026-11-07.
[^researchers]: SIIT, Researchers, 박사후연구원과 Research Interest. <https://siit.kaist.ac.kr/members/researchers>. 관측일 2026-11-07.
[^phd]: SIIT, PhD Students, 구성원과 Research Interest. <https://siit.kaist.ac.kr/members/phd>. 관측일 2026-11-07.
[^ms]: SIIT, MS Students, 구성원과 Research Interest. <https://siit.kaist.ac.kr/members/ms>. 관측일 2026-11-07.
[^alumni]: SIIT, Alumni, 학위·연도·진로. <https://siit.kaist.ac.kr/members/alumni>. 관측일 2026-11-07.
[^journals]: SIIT, Journals, 연도별 학술지 논문 목록. <https://siit.kaist.ac.kr/publications/journals>. 관측일 2026-11-07.
[^conferences]: SIIT, Conferences, 연도별 학회 논문 목록. <https://siit.kaist.ac.kr/publications/conferences>. 관측일 2026-11-07.
[^bibliography]: OpenAlex, Junmo Kim의 2021–2026년 등록 서지와 논문별 DOI. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5100606266,publication_year:2021-2026>. Crossref, Integrating Multiple Receptive Fields Through Grouped Active Convolution의 등록 서지 <https://api.crossref.org/works/10.1109/TPAMI.2020.2995864>, ICCV 2021 세 논문의 등록 서지 <https://api.crossref.org/works/10.1109/iccv48922.2021.00635>, <https://api.crossref.org/works/10.1109/iccv48922.2021.01098>, <https://api.crossref.org/works/10.1109/iccv48922.2021.00527>. 관측일 2026-11-07.
[^p1]: G. Han, J. Kim, J. Kim, Applied Sciences (2026). <https://doi.org/10.3390/app162110842> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7225130192>. 관측일 2026-11-07.
[^p2]: J. Kim 외, J. Kim, IEEE/CVF International Conference on Computer Vision (ICCV) (2025). <https://doi.org/10.1109/iccv51701.2025.02337> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7160150019>. 관측일 2026-11-07.
[^p3]: J. Hur 외, J. Kim, NeurIPS (2024). <https://doi.org/10.52202/079017-4163> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4415800554>. 관측일 2026-11-07.
[^p4]: J. Lee 외, J. Kim, NeurIPS (2022). <https://doi.org/10.52202/068431-0074> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7133188672>. 관측일 2026-11-07.
[^p5]: M. Kwon 외, J. Kim, Conference on Empirical Methods in Natural Language Processing (EMNLP) (2024). <https://doi.org/10.18653/v1/2024.emnlp-main.551> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4404782438>. 관측일 2026-11-07.
[^p6]: G. Han, J. Choi, H. Lee, J. Kim, CVPR (2023). <https://doi.org/10.1109/cvpr52729.2023.01964> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4386076307>. 관측일 2026-11-07.
[^p7]: S. Koh 외, J. Kim, IEEE Transactions on Medical Imaging (2026). <https://doi.org/10.1109/tmi.2026.3741804> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W7221503892>. 관측일 2026-11-07.
[^p8]: S. Lee, Y. Jeon, S. Lee, J. Kim, IEEE Access (2025). <https://doi.org/10.1109/access.2025.3529465> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W4406354235>. 관측일 2026-11-07.

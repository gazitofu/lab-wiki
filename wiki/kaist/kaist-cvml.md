# KAIST CVML Lab (Computer Vision & Machine Learning Lab)

**KAIST 김재철AI대학원 · 심현정 부교수**

- 분야: 컴퓨터 비전, 기계학습, 인공지능(AI, Artificial Intelligence), 이미지 생성, 공간 이해, 안전한 주행 인식, 학습 효율
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^home], 생성 인공지능[^home], 멀티모달 AI[^home], 자율주행[^home], 모델 경량화·양자화[^home], 책임 있는 AI·공정성[^home], 데이터 중심 AI·데이터 효율 학습[^home]
- 홈페이지: <https://kaist-cvml.github.io>
- 근거와 출처: [KAIST CVML Lab 근거 페이지](kaist-cvml-sources.md)

> 그림과 글을 함께 이해하고 새 이미지를 만드는 인공지능을 연구하며, 현실의 공간·주행 환경을 이해하는 능력과 사람에 대한 공정성, 학습·계산 효율을 함께 다룬다.[^home]

## 무엇을 연구하나

KAIST CVML Lab은 심현정 부교수가 이끄는 컴퓨터 비전(컴퓨터가 사진·영상의 내용을 알아보고 처리하는 분야)·기계학습(자료에서 규칙을 배워 예측이나 판단에 사용하는 방법) 연구실이다. 대학원은 교수의 연구 분야를 컴퓨터 비전과 기계학습으로 소개한다.[^gsai] 연구실은 안전하고 물리적 현실에 근거하며 신뢰할 수 있는 인공지능을 연구 방향으로 제시한다. 그림·글처럼 종류가 다른 자료를 함께 다루는 멀티모달 인공지능과, 물체의 위치·방향·관계를 헤아리는 공간 추론을 연결하는 것이 한 축이다.[^home]

첫째는 **사람의 요구와 가치에 맞는 생성**이다. 연구실은 글로 이미지·영상·입체 모양을 만들고, 원하는 대상이나 사용자에 맞게 결과를 조정하는 개인화와 편향(특정 집단이나 조건에 대해 판단이 체계적으로 치우치는 성질)의 제거·공정성을 함께 연구한다.[^home] 대표 논문 1은 확산 모델(자료에 잡음을 더하고 이를 되돌리는 과정을 학습해 새 자료를 만드는 생성 모델)을 사람이 선호하는 결과에 맞추는 학습법을 제안했다. 기준 모델의 갱신을 안정화하고 생성 단계별 선호 학습의 불균형을 조절해, 사람의 선호에 맞는 결과를 내는 성능을 개선했다.[^p1]

둘째는 **현실 공간을 이해하고 안전하게 인식하는 방법**이다. 연구실은 비전-언어 모델(그림과 글을 함께 처리하는 인공지능 모델)에 입체 공간과 물리 법칙을 가르치고, 어두운 환경·악천후·자율주행에서 작동하는 인식 기술을 개발한다.[^home] 대표 논문 2는 이미 학습된 모델의 구조를 바꾸지 않고 기하 정보(물체의 위치·거리·모양 같은 공간 관계)를 학습시키는 방법으로 공간 이해를 개선했다.[^p2] 대표 논문 3은 악천후의 거리 관측 자료에서 안전과 관련된 물체 범주를 놓치는 문제를 다루며, 범주의 의미와 국소 관측의 손상을 함께 줄이는 방법을 제안했다.[^p3]

셋째는 **자료와 계산 자원의 효율**이다. 연구실은 적은 자원을 사용하는 학습, 모델 압축(구조나 수치 표현 등을 바꾸어 저장 공간·계산량을 줄이는 방법), 양자화(수치를 정해진 단계의 값들로 나타내는 방법), 데이터셋 증류(원래 학습 자료의 정보를 작은 학습 자료에 담는 방법)를 연구한다.[^home] 대표 논문 4는 압축된 이미지마다 학습용 정답 정보를 보강해 학습 신호를 늘렸고,[^p4] 대표 논문 5와 7은 정답을 붙이는 부담을 줄이면서 이미지의 범주와 영역을 알아내는 방법을 다뤘다.[^p5][^p7] 의료 영상에서는 이미 학습된 잡음 제거기의 결과와 원래 영상을 국소적으로 조합해 질감을 보존하는 알고리즘도 제안했다.[^p6]

## 주요 연구 주제

### 생성 결과를 사람의 선호에 맞추기

글을 입력해 이미지를 만드는 모델에서 선호 학습을 개선한다. 대표 논문 1은 기존의 직접 선호 최적화(좋은 결과와 나쁜 결과의 선호 쌍을 이용해 생성 모델을 조정하는 학습법)를 확산 모델에 적용할 때 생기는 한계를 다루며, 기준 모델 갱신과 시간 단계별 학습 조절을 결합했다.[^p1] 연구실은 생성의 개인화뿐 아니라 편향을 줄이는 것을 주요 목표로 삼는다.[^home]

### 그림과 글의 공간 이해, 악천후의 물체 인식

대표 논문 2는 서로 다른 영상에서 대응하는 지점, 상대적인 깊이 관계, 대응 비용을 담은 입체 정보를 기존 비전-언어 모델로 전달한다. 이를 통해 자연스러운 그림·글 입력을 유지하면서 공간 추론과 인식을 개선했다.[^p2] 대표 논문 3은 라이다(LiDAR, Light Detection and Ranging, 빛을 보내 되돌아오는 시간이나 위상으로 거리를 재는 기술)의 관측점에 의미 범주를 붙이는 문제를 다룬다. 물체의 특징(자료의 성질을 계산에 쓰도록 나타낸 값)을 상위 범주와 연결하고, 깨끗한 관측과 손상된 관측의 특징이 맞도록 학습을 조절했다.[^p3]

### 적은 정답 정보로 이미지 이해하기

대표 논문 4는 합성 이미지의 일부 영역을 뽑아 추가적인 학습용 정답을 만들며, 작은 학습 자료에서도 풍부한 의미 정보를 전달한다.[^p4] 대표 논문 5는 한 이미지에 여러 범주를 붙이는 분류에서 물체 주변의 여러 시야를 고르고, 기존 비전-언어 모델이 만들어 준 임시 정답의 편향을 줄였다.[^p5] 대표 논문 7은 이미지 수준의 범주 정보와 주목 영역 지도(이미지에서 눈에 띄는 영역을 표시한 지도)를 결합해 의미 분할(이미지의 각 지점에 대상 범주를 붙여 영역을 나누는 방법)을 학습한다. 두 정보의 상호 보완 관계를 이용하고 주목 영역 지도의 오류를 다루는 전략으로 물체 경계를 개선했다.[^p7]

### 의료 영상의 잡음을 줄이면서 질감 보존하기

대표 논문 6은 저선량(엑스선을 쪼이는 양이 적은) 전산화단층촬영(CT, Computed Tomography, 여러 방향의 엑스선 측정으로 몸속 단면을 만드는 영상 기술)에서 잡음을 없애다가 영상이 과도하게 매끈해지는 문제를 다룬다. 기존 잡음 제거기의 출력과 입력 영상에 남은 차이를 위치별로 조합하고, 정상 선량 영상의 잡음 수준과 국소적으로 맞추는 알고리즘을 제안했다. 추가 학습 자료 없이 기존 잡음 제거기에 적용하며, 영상의 세부 구조와 질감 보존을 평가했다.[^p6]

## 대표 논문

KAIST 재직 시기의 연구에서 생성·공간 이해·안전한 인식·학습 효율·영상 복원을 고르게 보여 주는 논문을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자는 등록된 저자 순서의 첫 저자와 심현정의 위치이며, 교신저자 여부를 뜻하지 않는다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Rethinking Direct Preference Optimization in Diffusion Models](https://doi.org/10.1609/aaai.v40i7.37480) · AAAI | 첫 저자 Junyong Kang, 마지막 저자 Hyunjung Shim | 글로 이미지를 만드는 확산 모델이 사람의 선호를 배우도록, 기준 모델 갱신과 생성 단계별 학습 조절을 결합했다.[^p1] |
| 2 | 2025 | [3D-Aware Vision-Language Models Fine-Tuning with Geometric Distillation](https://doi.org/10.18653/v1/2025.findings-emnlp.562) · EMNLP Findings | 첫 저자 Seonho Lee, 마지막 저자 Hyunjung Shim | 기존 모델의 구조를 유지한 채 영상 사이의 대응과 깊이 관계를 전달해 입체 공간을 이해하도록 학습했다.[^p2] |
| 3 | 2025 | [No Thing, Nothing: Highlighting Safety-Critical Classes for Robust LiDAR Semantic Segmentation in Adverse Weather](https://doi.org/10.1109/cvpr52734.2025.00627) · CVPR | 첫 저자 Junsung Park, 마지막 저자 Hyunjung Shim | 악천후에 물체가 다른 범주로 잘못 인식되는 문제를 줄이도록, 상위 범주 정보와 관측 손상에 견디는 학습을 결합했다.[^p3] |
| 4 | 2025 | [Label-Augmented Dataset Distillation](https://doi.org/10.1109/wacv61041.2025.00149) · WACV | 첫 저자 Seoungyoon Kang, 마지막 저자 Hyunjung Shim | 압축된 이미지의 일부 영역마다 학습용 정답을 추가해, 작은 학습 자료가 전달하는 정보를 늘렸다.[^p4] |
| 5 | 2025 | [Classifier-guided CLIP Distillation for Unsupervised Multi-label Classification](https://doi.org/10.1109/cvpr52734.2025.00439) · CVPR | 첫 저자 Dongseob Kim, 마지막 저자 Hyunjung Shim | 추가 정답 없이 물체 주변의 여러 시야를 고르고 기존 모델의 예측 편향을 줄여, 한 이미지의 여러 범주를 알아냈다.[^p5] |
| 6 | 2024 | [Adapting low-dose CT denoisers for texture preservation using zero-shot local noise-level matching](https://doi.org/10.1002/mp.17015) · Medical Physics | 첫 저자 Youngjun Ko, 마지막 저자 Hyunjung Shim | 잡음 제거 결과와 원래 영상의 차이를 위치별로 조합해, 추가 학습 없이 저선량 영상의 세부 구조와 질감을 보존한다.[^p6] |
| 7 | 2023 | [Saliency as Pseudo-Pixel Supervision for Weakly and Semi-Supervised Semantic Segmentation](https://doi.org/10.1109/tpami.2023.3273592) · IEEE TPAMI | 첫 저자 Minhyun Lee, 마지막 저자 Hyunjung Shim | 이미지의 범주와 주목 영역을 함께 학습해 물체의 경계를 찾고, 주목 영역 지도에 생긴 오류를 다루는 학습법을 제안했다.[^p7] |

## 교수와 전문 분야

심현정은 KAIST 김재철AI대학원 부교수이며, 연구 분야는 컴퓨터 비전과 기계학습이다.[^gsai] 연구실은 2022년 7월 KAIST AI로 이동했다고 알렸다.[^news] 최근 논문을 보면 이미지 생성의 선호 학습, 그림·글의 공간 이해, 악천후 물체 인식, 적은 정답 정보를 이용하는 학습, 의료 영상의 잡음 제거 알고리즘을 전문 주제로 다룬다.[^p1][^p2][^p3][^p4][^p6][^p7]

## 응용 분야

연구실은 개인화 이미지·영상·입체 콘텐츠 생성, 안전이 중요한 자율주행 인식, 공간을 이해하는 인공지능, 자원 효율적인 학습을 응용 방향으로 제시한다.[^home] 과제에는 문서 생성, 편향 검출·교정·설명, 대기질 예측, 이미지 영역 분할, 가상 캐릭터 표현, 소수 예시 생성 학습이 올라 있다.[^projects] 의료 영상의 공학적 응용으로는 저선량 CT 영상 복원이 있다.[^p6]

## 구성원

구성원 쪽의 현재 구성원 21명과 게시된 과정·연구 주제·학교 이메일이다(2026-11-09). 대표 논문 참여는 이름의 철자·순서가 완전히 같은 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| NaHyeon Park | 박사과정 | Generative Models | julia19@kaist.ac.kr |  |
| Na Min An | 박사과정 | Multimodal Models | naminan@kaist.ac.kr |  |
| Junsung Park | 박사과정 | AI for Robotics | jshackist@kaist.ac.kr | 2, 3 |
| Jiho Choi | 박사과정 | Vision-Language Models, Agentic AI | jihochoi@kaist.ac.kr | 2 |
| Seojeong Park | 박사과정 | Multimodal | seojeong.park@kaist.ac.kr |  |
| Junyong Kang | 박사과정 | Representation Learning, Explainable AI | jykang@kaist.ac.kr | 1 |
| Inha Kang | 박사과정 | Vision-Language Models, Multimodal | rkswlsj13@kaist.ac.kr | 2, 3 |
| Wonjeong Ryu | 박사과정 | Computer Vision, RAS | petac@kaist.ac.kr |  |
| Soyeon Yoon | 박사과정 | 3D & 4D Generation | thoyeony@kaist.ac.kr |  |
| Seungjun Yu | 박사과정 | Multimodal, Autonomous Driving | seungjunyu@kaist.ac.kr |  |
| Jinwoo Lee | 석사과정 | 3D Computer Vision | bestgenius10@kaist.ac.kr |  |
| Debjyoti Mondal | 석사과정 | Graph Neural Networks, Representation Learning | deb.kit2@kaist.ac.kr |  |
| Hojun Choi | 박사과정 | Vision-Language Models, Multimodal | hchoi256@kaist.ac.kr |  |
| Jiwook Kim | 박사과정 | High-dimensional Vision, Vision Foundation Model, World Model | tom919@kaist.ac.kr | 2 |
| Suin Lee | 박사과정 | 3D Computer Vision, 3D Generative Models | suinlee@kaist.ac.kr |  |
| Youjin Jeon | 박사과정 | World Models, Vision Language Action Models, 3D Vision | ngbrjyj@kaist.ac.kr |  |
| Cholmin Kang | 박사과정 | Computer Vision, Augmentation, Style transfer, Medical AI | stevekang@kaist.ac.kr |  |
| Jaeyo Shin | 박사과정 | 3D Understanding, Generative Models | jaeyo_shin@kaist.ac.kr |  |
| Kyuan Oh | 인턴 | Vision-Language-Action Models, Omnimodal AI, World Models | oka04108@cau.ac.kr |  |
| ByungHyun Jeon | 인턴 | 3D Reconstruction/Generation, 3D Understanding | jbh030312@khu.ac.kr |  |
| Yoonhyung Park | 인턴 | Multimodal Models, Tactile Sensing, Embodied AI |  |  |

## 졸업생 진로

구성원 쪽의 Alumni 23명이다. 학위·과정, 연월과 진로는 게시 표기다. 연구실이 2022년 7월 KAIST AI로 이동하기 전의 이력도 포함한다.[^people][^news]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Minjoon Kim | Masters (2015-12) | Seoul National University |
| Joohyun Park | Masters (2019-12) | MedGo CTO |
| Armagan Elibol | Postdoc (2016-01) | Japan Advanced Institute of Science and Technology |
| Sukmyung Lee | Postdoc (2016-12) |  |
| Duhyeon Bang | PhD (2020-02) | Vision AI Labs, T3K, SK telecom |
| Junsuk Choe | PhD (2020-08) | Assistant Professor at Sogang University |
| Song Park | PhD (2022-02) | NAVER AI Lab |
| Chanyeong Shin | Masters (2022-02) |  |
| Kyungjune Baek | PhD (2023-02) | Assistant Professor at Sejong University |
| Youngjun Ko | PhD (2023-02) | SAMSUNG MEDISON |
| Seungho Lee | PhD (2024-08) | Samsung Advanced Institute of Technology |
| Seoungyoon Kang | PhD (2024-08) | Samsung Global Research |
| Minhyun Lee | PhD (2024-08) | Samsung Advanced Institute of Technology |
| Dongseob Kim | PhD (2024-08) | Samsung Electronics MX |
| Kyungmin Kim | PhD (2025-02) |  |
| Hwijeong Lee | Masters (2025-02) |  |
| Hyogon Ryu | Masters (2025-02) | KRAFTON AI |
| Yunji Jung | Masters (2025-08) | Riiid |
| Youngsun Lim | Masters (2025-08) | PhD Student at Boston University |
| Seohyun Lim | Masters (2025-08) | FASOO |
| Eunki Kim | Masters (2026-02) | SKT |
| Seongjong Song | PhD (2026-02) |  |
| Seonho Lee | Masters (2026-02) | KRAFTON AI |

## 최근 5년 논문 목록

논문 쪽의 2021–2026년 구역에 있는 66개 게시 항목이다. 제목·저자·발표처와 연도 구역은 연구실 표기이며, 학회 채택은 「채택」, 학술지 게재 승인은 「게재 승인」으로 구분한다. 2022년 7월 연구실의 KAIST 이동 전 항목도 포함한다. 저자 이름 뒤 별표는 누리집 표시이며 역할을 뜻하지 않는다.[^pubs][^news]

**2026**

- NaHyeon Park, Minhyun Lee, Hyunjung Shim. "Keep It CALM: Analyzing the Limits of Global Unsafety in Text-to-Image Generation". *NeurIPS (채택)*.
- Junsung Park, Hyunjung Shim. "Grounding Driving VLA via Inverse Kinematics". *NeurIPS (채택)*.
- Seungjun Yu, Seonho Lee, Namho Kim, Jaeyo Shin, Junsung Park, Wonjeong Ryu, Raehyuk Jung, Hyunjung Shim. "WaymoQA: A Multi-View Visual Question Answering Dataset for Safety-Critical Reasoning in Autonomous Driving". *EMNLP Findings (채택); DOI: https://doi.org/10.18653/2026.findings-emnlp.1028*.
- Eunki Kim\*, Na Min An\*, Wan Ju Kang, Sangryul Kim, James Thorne, Hyunjung Shim. "Are Large Vision-Language Models Ready to Guide Blind and Low-Vision Individuals?". *COLM (채택)*.
- Jaeyo Shin\*, Jiwook Kim\*, Hyunjung Shim. "Representation Alignment for Just Image Transformers is not Easier than You Think". *ECCV (채택); DOI: https://doi.org/10.1007/978-3-032-37271-0_33*.
- Na Min An\*, Inha Kang\*, Minhyun Lee, Hyunjung Shim. "Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding". *ECCV (채택); DOI: https://doi.org/10.1007/978-3-032-37350-2_21*.
- Jiho Choi\*, Seonho Lee\*, Seojeong Park, Hyunjung Shim. "Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views". *ECCV (채택); DOI: https://doi.org/10.1007/978-3-032-37429-5_11*.
- Hojun Choi, Youngsun Lim, Jaeyo Shin, Hyunjung Shim. "CoT-PL: Chain-of-Thought Pseudo-Labeling for Open-Vocabulary Object Detection". *ECCV (채택)*.
- Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee. "Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints". *ECCV (채택); DOI: https://doi.org/10.1007/978-3-032-37167-6_5*.
- Seojeong Park\*, Jiho Choi\*, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim. "Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling". *ICML (채택)*.
- NaHyeon Park\*, Kunhee Kim\*, Hyunjung Shim. "Boosting Text Encoder for Personalized Text-to-Image Generation". *Transactions on Machine Learning Research (TMLR) (게재 승인)*.
- Jiho Choi\*, Seojeong Park\*, Seongjong Song, Hyunjung Shim. "PosterForest: Hierarchical Multi-Agent Collaboration for Scientific Poster Generation". *ACL (채택)*.
- Na Min An, Yoonna Jang, Yusuke Hirota, Ryo Hachiuma, Isabelle Augenstein, Hyunjung Shim. "Interpretable Debiasing of Vision-Language Models for Social Fairness". *CVPR (채택)*.
- Inha Kang, Eunki Kim, Wonjeong Ryu, Jaeyo Shin, Seungjun Yu, Yoon-Hee Kang, Seongeun Jeong, Eunhye Kim, Soontae Kim, Hyunjung Shim. "Real-Time Long Horizon Air Quality Forecasting via Group-Relative Policy Optimization". *CVPR (채택)*.
- Soyeon Yoon, Chang Wook Seo, Hyunjung Shim. "SGSoft: Learning Fused Semantic-Geometric Features for 3D Shape Correspondence via Template-Guided Soft Signals". *CVPR (채택)*.
- Eunsu Kim\*, Junyeong Park\*, Na Min An\*, Jun Seong Kim, Hitesh Laxmichand Patel, Jiho Jin, Julia Kruk, Amit Agarwal, Srikant Panda, Fenal Ashokbhai Ilasariya, Hyunjung Shim, Alice Oh. "World in a Frame: Understanding Culture Mixing as a New Challenge for Vision-Language Models". *CVPR (채택)*.
- Inha Kang, Youngsun Lim, Seonho Lee, Jiho Choi, Junsuk Choe, Hyunjung Shim. "What 'Not' to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging". *ICLR (채택)*.
- Kunhee Kim\*, NaHyeon Park\*, Kibeom Hong, Hyunjung Shim. "Directional Textual Inversion for Personalized Text-to-Image Generation". *ICLR (채택)*.
- Seojeong Park, Jiho Choi, Kyungjune Baek, Hyunjung Shim. "MomentMix Augmentation with Length-Aware DETR for Temporally Robust Moment Retrieval". *WACV (채택); DOI: https://doi.org/10.1109/wacv61042.2026.00116*.
- Junyong Kang\*, Seohyun Lim\*, Kyungjune Baek, Hyunjung Shim. "Rethinking Direct Preference Optimization in Diffusion Models". *AAAI (채택)*.

**2025**

- Minhyun Lee\*, Seungho Lee\*, Song Park, Dongyoon Han, Byeongho Heo, Hyunjung Shim. "MaskRIS: Semantic Distortion-aware Data Augmentation for Referring Image Segmentation". *Transactions on Machine Learning Research (TMLR) (게재 승인)*.
- Seonho Lee\*, Jiho Choi\*, Inha Kang, Jiwook Kim, Junsung Park, Hyunjung Shim. "3D-Aware Vision-Language Models Fine-Tuning with Geometric Distillation". *EMNLP Findings (채택); DOI: https://doi.org/10.18653/v1/2025.findings-emnlp.562*.
- Seonho Lee\*, Jiho Choi\*, Seohyun Lim, Jiwook Kim, Hyunjung Shim. "Scribble-Guided Diffusion for Training-free Text-to-Image Generation". *ICIP (채택); DOI: https://doi.org/10.1109/icip55913.2025.11084547*.
- Na Min An\*, Eunki Kim\*, James Thorne, Hyunjung Shim. "I0T: Embedding Standardization Method Towards Zero Modality Gap". *ACL (채택); DOI: https://doi.org/10.18653/v1/2025.acl-long.1319*.
- Jiho Choi\*, Seonho Lee\*, Minhyun Lee, Seungho Lee, Hyunjung Shim. "Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation". *CVPR (채택); DOI: https://doi.org/10.1109/cvpr52734.2025.00914*.
- Dongseob Kim, Hyunjung Shim. "Classifier-guided CLIP Distillation for Unsupervised Multi-label Classification". *CVPR (채택); DOI: https://doi.org/10.1109/cvpr52734.2025.00439*.
- Junsung Park, Hwijeong Lee, Inha Kang, Hyunjung Shim. "No Thing, Nothing: Highlighting Safety-Critical Classes for Robust LiDAR Semantic Segmentation in Adverse Weather". *CVPR (채택); DOI: https://doi.org/10.1109/cvpr52734.2025.00627*.
- Hyogon Ryu, NaHyeon Park, Hyunjung Shim. "DGQ: Distribution-Aware Group Quantization for Text-to-Image Diffusion Models". *ICLR (채택)*.
- Jiwook Kim\*, Seonho Lee\*, Jaeyo Shin, Jiho Choi, Hyunjung Shim. "DreamCatalyst: Fast and High-Quality 3D Editing via Controlling Editability and Identity Preservation". *ICLR (채택)*.
- Seoungyoon Kang\*, Youngsun Lim\*, Hyunjung Shim. "Label-Augmented Dataset Distillation". *WACV (채택); DOI: https://doi.org/10.1109/wacv61041.2025.00149*.
- Youngsun Lim\*, Hojun Choi\*, Hyunjung Shim. "Evaluating Image Hallucination in Text-to-Image Generation with Question-Answering". *AAAI (채택); DOI: https://doi.org/10.1609/aaai.v39i25.34827*.

**2024**

- Jiho Choi\*, Seonho Lee\*, Seungho Lee, Minhyun Lee, Hyunjung Shim. "Understanding Multi-Granularity for Open-Vocabulary Part Segmentation". *NeurIPS; DOI: https://doi.org/10.52202/079017-4358*.
- Junsung Park, Kyungmin Kim, Hyunjung Shim. "Rethinking Data Augmentation for Robust LiDAR Semantic Segmentation in Adverse Weather". *ECCV; DOI: https://doi.org/10.1007/978-3-031-72640-8_18*.
- Minhyun Lee\*, Song Park\*, Byeongho Heo, Dongyoon Han, Hyunjung Shim. "SeiT++: Masked Token Modeling Improves Storage-efficient Training". *ECCV; DOI: https://doi.org/10.1007/978-3-031-73390-1_11*.
- Hyogon Ryu, Seohyun Lim, Hyunjung Shim. "Memory-Efficient Fine-Tuning for Quantized Diffusion Model". *ECCV; DOI: https://doi.org/10.1007/978-3-031-72640-8_20*.
- Seungho Lee, Hwijeong Lee, Hyunjung Shim. "Learning from Spatio-temporal Correlation for Semi-Supervised LiDAR Semantic Segmentation". *IROS; DOI: https://doi.org/10.1109/iros58592.2024.10801453*.
- Dongseob Kim, Hyunjung Shim. "Locally Conditioned GANs: Self-supervised Local Patch Representation Learning for Conditional Generation". *IEEE Access; DOI: https://doi.org/10.1109/access.2024.3418884*.
- Youngsun Lim, Hyunjung Shim. "Preventing Image Hallucination in Text-to-Image Generation through Factual Image Retrieval". *IJCAI TIDMwFM*.
- Youngjun Ko\*, Seongjong Song\*, Jongduk Baek, Hyunjung Shim. "Adapting Low-Dose CT Denoisers for Texture Preservation using Zero-Shot Local Noise-level Matching". *Medical Physics (MP); DOI: https://doi.org/10.1002/mp.17015*.
- Dongseob Kim\*, Seungho Lee\*, Junsuk Choe, Hyunjung Shim. "Weakly Supervised Semantic Segmentation for Driving Scenes". *AAAI; DOI: https://doi.org/10.1609/aaai.v38i3.28053*.
- Seungho Lee\*, Seoungyoon Kang\*, Hyunjung Shim. "Self-Supervised Vision Transformers Are Efficient Segmentation Learners for Imperfect Labels". *AAAIW*.
- Junsung Park, Hyunjung Shim. "Precision matters: Precision-aware ensemble for weakly supervised semantic segmentation". *AAAIW*.
- Seoungyoon Kang\*, Yunji Jung\*, Hyunjung Shim. "Local Expert Diffusion Models for Efficient Training in Denoising Diffusion Probabilistic Models". *AAAIW*.

**2023**

- M Lee\*, S Lee\*, J Lee, Hyunjung Shim. "Saliency as Pseudo-pixel Supervision for Weakly and Semi-supervised Semantic Segmentation". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI); DOI: https://doi.org/10.1109/tpami.2023.3273592*.
- D Hwang, J-W. Ha, Hyunjung Shim, J Choe. "Entropy Regularization for Weakly Supervised Object Localization". *Pattern Recognition Letters; DOI: https://doi.org/10.1016/j.patrec.2023.03.018*.
- NaHyeon Park\*, Kunhee Kim\*, Song Park, Jung-Woo Ha, Hyunjung Shim. "TADA: Timestep-Aware Data Augmentation for Diffusion Models". *NeurIPS Workshop*.
- D Kim, M Kim, Hyunjung Shim, J Lee. "Your Lottery Ticket is Damaged: Towards All-Alive Pruning for Extremely Sparse Networks". *Information Sciences (IS); DOI: https://doi.org/10.1016/j.ins.2023.03.122*.
- M Han, Hyunjung Shim, J Baek. "Utilization of an Attentive Map to Preserve Anatomical Features for Training Convolutional Neural Network based Low-dose CT Denoiser". *Medical Physics (MP); DOI: https://doi.org/10.1002/mp.16263*.
- J Moon, Y Jeong, D-K Chae, J Choi, Hyunjung Shim, J Lee. "CoMix: Collaborative Filtering with Mixup for Implicit Datasets". *Information Sciences (IS); DOI: https://doi.org/10.1016/j.ins.2023.01.110*.
- S Park\*, S Chun\*, S Lee, J Cha, B Lee, Hyunjung Shim. "Few-shot Font Generation with Weakly Supervised Localized Representations". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI); DOI: https://doi.org/10.1109/tpami.2022.3196675*.
- S Kang, M Kim, Hyunjung Shim. "F2RPC: Fake to Real Portrait Control from a Virtual Character". *IEEE Access; DOI: https://doi.org/10.1109/access.2023.3306836*.
- S Kang\*, M Lee\*, M Kim, Hyunjung Shim. "HybridMatch: Semi-supervised Facial Landmark Detection via Hybrid Heatmap Representations". *IEEE Access; DOI: https://doi.org/10.1109/access.2023.3257180*.

**2022**

- S Han, E Choi, C Lim, J Lee, Hyunjung Shim, J Lee. "Long-tail Mixup for Extreme Multi-label Classification". *CIKM; DOI: https://doi.org/10.1145/3511808.3557632*.
- B Kim, Hyunjung Shim, J Baek. "A streak artifact reduction algorithm in sparse-view CT using a self-supervised neural representation". *Medical Physics (MP); DOI: https://doi.org/10.1002/mp.15885*.
- M Han, Hyunjung Shim, J Baek. "Perceptual CT Loss: Implementing CT Image Specific Perceptual Loss for CNN-Based Low-Dose CT Denoiser". *IEEE Access; DOI: https://doi.org/10.1109/access.2022.3182821*.
- J Choe\*, S-J Oh\*, S Chun, S Lee, Z Akata, Hyunjung Shim. "Evaluation for Weakly Supervised Object Localization: Protocol, Metrics, and Datasets". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI); DOI: https://doi.org/10.1109/tpami.2022.3169881*.
- J-W Lee, M Choi, S Lee, Hyunjung Shim, J Lee. "Knowledge distillation meets recommendation: collaborative distillation for top-N recommendation". *Knowledge and Information Systems (KIS); DOI: https://doi.org/10.1007/s10115-022-01667-8*.
- D Bang\*, K Baek\*, J Kim, Y Jeon, JH Kim, J Kim, J Lee, Hyunjung Shim. "Logit Mixing Training for More Reliable and Accurate Prediction". *IJCAI; DOI: https://doi.org/10.24963/ijcai.2022/390*.
- K Baek, Hyunjung Shim. "Commonality in Natural Images Rescues GANs: Pretraining GANs with Generic and Privacy-free Synthetic Data". *CVPR; DOI: https://doi.org/10.1109/cvpr52688.2022.00770*.
- M Lee\*, D Kim\*, Hyunjung Shim. "Threshold Matters in WSSS: Manipulating the Activation for the Robust and Accurate Segmentation Model Against Thresholds". *CVPR; DOI: https://doi.org/10.1109/cvpr52688.2022.00429*.
- K Baek\*, S Lee\*, Hyunjung Shim. "Learning from Better Supervision: Self-distillation for Learning with Noisy Labels". *ICPR; DOI: https://doi.org/10.1109/icpr56361.2022.9956388*.
- Y Choi, M Han, H Jang, Hyunjung Shim, J Baek. "Two-phase Learning-based 3D Deblurring Method for Digital Breast Tomosynthesis Images". *Plos One; DOI: https://doi.org/10.1371/journal.pone.0262736*.
- M Choi, J Kim, J Lee, Hyunjung Shim, J Lee. "S-Walk: Accurate and Scalable Session-based Recommendation with Random Walks". *WSDM*.

**2021**

- J Lee, M Choi, Hyunjung Shim, J Lee. "Knowledge Distillation Meets Recommendation: Collaborative Distillation for Top-N Recommendation". *Knowledge and Information Systems (KAIS)*.
- K Baek, Y Choi, Y Uh, J Yoo, Hyunjung Shim. "Rethinking the Truly Unsupervised Image-to-Image Translation". *ICCV; DOI: https://doi.org/10.1109/iccv48922.2021.01389*.
- S Park, S Chun, J Cha, B Lee, Hyunjung Shim. "Multiple Heads are Better than One: Few-shot Font Generation with Multiple Localized Experts". *ICCV; DOI: https://doi.org/10.1109/iccv48922.2021.01364*.

## 과제

수행 기간이 2021-10-13–2026-10-13과 겹치는 과제 9건이다. 과제명·지원기관·수행 기간·상태는 게시 표기이며, 연도만 적힌 기간은 그 연도 표기를 따랐다. 이 가운데 기간이 연도만 적힌 2021년 과제 1건은 월이 게시되어 있지 않아 기간과의 겹침을 확정할 수 없다. 2022년 7월 연구실의 KAIST 이동 전 과제도 포함한다.[^projects][^news]

- Content-based visual rich document generation (지원 Samsung Research; 기간 2025.08 - 2026.08; 상태 ongoing)
- Development of self-evolving AI bias detection-correction-explain platform based on international multidisciplinary governance (지원 Institute for Information & communication Technology Planning & evaluation (IITP); 기간 2025.04 - 2028.12; 상태 ongoing)
- Development of an air quality prediction model using artificial intelligence (지원 National Institute of Environmental Research (NIER); 기간 2023 - 2027; 상태 ongoing)
- Development of Open-Vocabulary Image Segmentation Method (지원 Samsung DS; 기간 2024; 상태 completed)
- Development of High Performance/High Efficiency/High Reliability in Image Segmentation Algorithm (지원 SFA; 기간 2023; 상태 completed)
- 3D Aware Vision Language Model (지원 Samsung SR; 기간 2024; 상태 completed)
- Low-shot Learning for Image Generative Models (지원 Naver AI; 기간 2023-2024; 상태 completed)
- Photorealistic Enhancement of Virtual Character (지원 NCSOFT; 기간 2022; 상태 completed)
- Developing a Generalized Feature Extractor for Handling Both Real and Synthetic Faces (지원 NCSOFT; 기간 2021; 상태 completed)

## 수상과 선정

2021-10-13–2026-10-13의 수상·선정 게시 항목 3건이다. 2025년 항목의 연도는 논문에 적힌 학회 연도이며, 수상 날짜는 게시되어 있지 않다.[^news][^pubs]

- 2026-10-12 · Junsung Park이 NeurIPS 2026 Main Track의 Top Reviewer로 선정되었다.
- 2026-02-06 · Inha Kang이 IPIU 2026의 Grand Prize와 Silver Prize를, Hojun Choi가 Best Poster Award를 받았다.
- 2025 · I0T: Embedding Standardization Method Towards Zero Modality Gap 논문이 ACL 2025의 Outstanding paper로 표기되어 있다.

## 소식

연구실이 2022-07-15–2026-09-25에 게시한 논문 채택·게재 승인·발표 선정 소식 24건이다. 첫 날짜는 해당 소식의 게시일이다. 2022년 7월 KAIST 이동 무렵의 소식도 포함한다.[^news]

- 2026-09-25 · NeurIPS 2026에 논문 2편이 채택되었다.
- 2026-08-31 · WaymoQA 논문이 EMNLP 2026 Findings에 채택되었다.
- 2026-07-09 · 시각장애인·저시력자 안내를 위한 비전-언어 모델 평가 논문이 COLM 2026에 채택되었다.
- 2026-06-18 · ECCV 2026에 논문 5편이 채택되었다.
- 2026-05-01 · 멀티모달 평가 모델의 지각적 판단 편향을 줄이는 논문이 ICML 2026에 채택되었다.
- 2026-04-07 · PosterForest 논문이 ACL 2026에 채택되었다.
- 2026-02-23 · CVPR 2026에 논문 4편이 채택되었다.
- 2026-01-29 · ICLR 2026에 논문 2편이 채택되었다.
- 2025-11-09 · 확산 모델의 직접 선호 최적화 논문이 AAAI 2026에 채택되고 구두 발표로 선정되었다.
- 2025-08-01 · 3차원 인식 비전-언어 모델의 기하 증류 논문이 EMNLP 2025 Findings에 채택되었다.
- 2025-06-01 · I0T 논문이 ACL 2025 구두 발표로 선정되었다.
- 2025-05-01 · ACL 2025에 논문 1편이 채택되었다.
- 2025-02-01 · CVPR 2025에 논문 3편이 채택되었다.
- 2025-01-15 · ICLR 2025에 논문 2편이 채택되었다.
- 2025-01-10 · Label-Augmented Dataset Distillation 논문이 WACV 2025 구두 발표로 선정되었다.
- 2025-01-05 · 질의응답을 이용한 이미지 생성 오류 평가 논문이 AAAI 2025 구두 발표로 선정되었다.
- 2024-12-01 · 질의응답을 이용한 이미지 생성 오류 평가 논문이 AAAI 2025에 채택되었다.
- 2024-09-01 · 오픈 어휘 부위 분할의 여러 세분 수준을 다루는 논문이 NeurIPS 2024에 채택되었다.
- 2024-08-15 · Label-Augmented Dataset Distillation 논문이 WACV 2025에 채택되었다.
- 2024-08-10 · 악천후 라이다 분할의 자료 증강 논문이 ECCV 2024 구두 발표로 선정되었다.
- 2024-07-01 · ECCV 2024에 논문 3편, IROS 2024에 논문 1편이 채택되었다.
- 2023-12-01 · 주행 장면의 약한 지도 영상 분할 논문이 AAAI 2024에 채택되었다.
- 2023-04-01 · 주목 영역을 이용한 약한 지도·부분 지도 영상 분할 논문이 IEEE Transactions on Pattern Analysis and Machine Intelligence에 게재 승인되었다.
- 2022-07-15 · 소수 예시 글꼴 생성 논문이 IEEE Transactions on Pattern Analysis and Machine Intelligence에 게재 승인되었다.

## 연락과 위치

- 교수 이메일: kateshim@kaist.ac.kr[^people]
- 연구실 위치: 서울특별시 서초구 태봉로 108, 양재AI허브 6층[^home]
- 교수 사무실: 양재캠퍼스 6층(602)[^gsai]

## 각주
[^home]: KAIST CVML Lab 첫 화면. <https://kaist-cvml.github.io> 관측 2026-11-09.
[^gsai]: KAIST 김재철AI대학원 구성원, 전임교수 심현정 소개. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-11-09.
[^people]: KAIST CVML Lab People. <https://kaist-cvml.github.io/pages/people.html> 구성원·졸업생 게시 내용 <https://kaist-cvml.github.io/data/people.json> 관측 2026-11-09.
[^pubs]: KAIST CVML Lab Publications. <https://kaist-cvml.github.io/pages/publications.html> 논문 게시 내용 <https://kaist-cvml.github.io/data/publications.json> 관측 2026-11-09.
[^projects]: KAIST CVML Lab Research Projects. <https://kaist-cvml.github.io/pages/projects.html> 과제 게시 내용 <https://kaist-cvml.github.io/data/projects.json> 관측 2026-11-09.
[^news]: KAIST CVML Lab 첫 화면 Latest News. <https://kaist-cvml.github.io> 소식 게시 내용 <https://kaist-cvml.github.io/data/news.json> 관측 2026-11-09.

[^p1]: J. Kang, S. Lim, K. Baek, H. Shim, Proceedings of the AAAI Conference on Artificial Intelligence (2026). <https://doi.org/10.1609/aaai.v40i7.37480> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p2]: S. Lee 외, H. Shim, Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP) (2025). <https://doi.org/10.18653/v1/2025.findings-emnlp.562> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p3]: J. Park, H. Lee, I. Kang, H. Shim, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2025). <https://doi.org/10.1109/cvpr52734.2025.00627> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p4]: S. Kang, Y. Lim, H. Shim, IEEE Winter Conference on Applications of Computer Vision (2025). <https://doi.org/10.1109/wacv61041.2025.00149> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p5]: D. Kim, H. Shim, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2025). <https://doi.org/10.1109/cvpr52734.2025.00439> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p6]: Y. Ko, S. Song, J. Baek, H. Shim, Medical Physics (2024). <https://doi.org/10.1002/mp.17015> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.
[^p7]: M. Lee, S. Lee, J. Lee, H. Shim, IEEE Transactions on Pattern Analysis and Machine Intelligence (2023). <https://doi.org/10.1109/tpami.2023.3273592> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5079082222,publication_year:2021-2026> 관측 2026-11-09.

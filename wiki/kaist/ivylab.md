# IVYLab & IVLLab

**KAIST 전기및전자공학부 · 노용만 교수**

- 분야: 영상·음성·언어를 함께 다루는 인공지능, 영상 인식과 생성, 모델의 판단 근거와 안정성
- 대분야: 컴퓨팅·AI
- 태그: 멀티모달 AI[^overview], 컴퓨터 비전[^overview], 음향·오디오 AI[^overview], 설명 가능한 AI(XAI)[^overview]
- 홈페이지: <https://www.ivylab.kaist.ac.kr/ivylab-ivllab>
- 근거와 출처: [IVYLab & IVLLab 근거 페이지](ivylab-sources.md)

> 영상·소리·글을 함께 이해하고 서로 바꾸는 인공지능을 만들며, 입 모양을 읽는 음성 인식부터 말하는 얼굴 생성, 영상 이해와 모델의 판단 근거까지 연구한다.[^overview][^fields]

## 무엇을 연구하나

노용만 교수가 이끄는 연구실은 Image and Video Systems Lab과 Integrated Vision and Language Lab이라는 두 이름을 함께 쓴다. 소개에 따르면 IVY Lab은 1997년 KAIST에서 설립됐고 설립 때부터 노용만 교수가 이끌었다. 연구의 큰 축은 컴퓨터 비전(컴퓨터가 영상에서 물체와 장면의 내용을 알아보는 기술)과 멀티모달 학습(영상·음성·글처럼 종류가 다른 자료를 함께 다루는 학습)이다. 서로 다른 자료가 가진 정보를 결합해 한 종류의 자료만으로 해결하기 어려운 인식과 소통 문제를 다룬다.[^overview][^prof]

구체적으로는 입 모양 영상으로 말을 알아보는 시각 음성 인식, 소리를 만들어 내는 음성 합성, 말소리에 맞춰 움직이는 얼굴 영상 생성, 영상과 소리를 함께 쓰는 음성 인식과 번역을 연구한다. 이때 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)을 이용해 자료 사이의 대응을 배운다. 예를 들어 영상에서 알아낸 내용을 소리나 글로 바꾸거나, 글을 바탕으로 영상을 만드는 문제를 다룬다. 연구실은 이런 방법을 사람마다 언어나 의사소통 조건이 다른 상황의 소통에도 연결한다.[^overview][^fields]

최근의 또 다른 축은 많은 자료로 미리 학습한 대형 모델을 여러 종류의 자료에 맞게 쓰는 일이다. 연구실은 영상·소리·글을 다루는 사전학습 대형 모델에 줄 프롬프트(모델에 과제나 응답 방향을 알려 주는 입력)를 설계하는 방법을 연구한다. 학습 자료를 바탕으로 만들어진 모델이 무엇을 기억하고 어떤 근거로 결과를 내는지도 함께 다룬다. 특히 해석 가능성(판단에 쓰인 근거나 과정을 사람이 이해할 수 있는 성질)과 강건성(입력이나 조건이 달라져도 성능을 유지하는 성질)을 연구 목표로 내세우며, 설명을 생성하고 적대적 공격(모델을 틀리게 하려고 입력을 의도적으로 바꾸는 행위) 아래의 예측을 분석한다.[^overview][^fields]

## 주요 연구 주제

### 시청각 음성 인식과 언어 사이의 번역

입 모양과 음성을 함께 사용하거나 한쪽에서 다른 쪽의 정보를 떠올려 말을 이해하는 방법을 연구한다. Zero-AVSR(Zero-Shot Audio-Visual Speech Recognition)는 대상 언어의 시청각 음성 학습 자료 없이도 인식하도록, 먼저 음성과 입 모양에서 로마자 글을 예측하는 표현을 배우고 이를 언어별 문자로 바꾸거나 언어 모델(말이나 글의 이어짐을 학습해 언어 자료를 처리하거나 생성하는 계산 모형)과 직접 연결하는 방법을 제안한다. AV2AV(Audio-Visual Speech to Audio-Visual Speech Translation)는 영상과 소리를 함께 받은 뒤 번역된 소리와 이에 맞는 입 모양 영상을 함께 만든다. 여기서는 두 종류의 자료를 함께 나타내는 표현을 미리 배워, 소리만 있는 번역 자료로 번역기를 학습시키는 방법을 제안한다.[^fields][^p2][^p3]

### 음성에 맞는 얼굴 영상 생성

말하는 얼굴을 만들 때는 입의 움직임이 음성과 맞아야 한다. SyncTalkFace는 음성과 입 모양의 관계를 메모리(정보를 저장했다가 필요할 때 꺼내 쓰는 기능이나 장치)에 학습시키는 방법을 제안한다. 실제 영상의 연속된 입 움직임에서 얻은 특징을 저장하고 음성의 특징과 대응시켜 두었다가, 새 음성이 들어오면 관련 입 움직임을 꺼내 얼굴 영상을 합성한다. 연구실은 얼굴 영상 생성과 함께 음성 합성, 시청각 대화도 멀티모달 연구의 주요 대상으로 제시한다.[^p4][^overview]

### 긴 영상 이해와 대형 모델의 지식 전달

영상에 질문할 때 어떤 프레임(동영상을 이루는 개별 정지 영상)을 고를지와, 큰 모델이 배운 내용을 작은 모델에 어떻게 전달할지를 다룬다. ReFoCUS(Reinforcement-guided Frame Optimization for Contextual Understanding)는 강화학습(행동의 결과로 받는 보상을 바탕으로 행동 방법을 배우는 학습)을 통해 질문에 맞는 프레임 조합을 고르는 방법을 제안한다. VLsI(Verbalized Layers-to-Interactions)는 지식 증류(다른 모델의 출력이나 내부 표현을 학습 신호로 써서 지식을 전달하는 방법)를 사용하며, 큰 모델과 작은 모델의 각 층에서 나온 표현을 글의 의미를 나타내는 공간으로 연결해 학습시킨다.[^p1][^p5]

### 판단 근거·편향·공격에 대한 신뢰성

자료 속 편향(특정 조건이나 대상에 치우친 경향)과 공격에 모델이 어떻게 반응하는지 분석하고 그 영향을 줄이는 방법을 만든다. 적대적 입력에 관한 인과 분석 연구는 예측에 영향을 주는 관계를 추정하고, 거기서 얻은 특징을 방어 모델에 전달한다. 보행자 검출 연구는 가시광(사람의 눈에 보이는 파장 범위의 빛)과 열 영상(물체가 내는 적외선의 분포를 영상으로 나타낸 것)을 함께 쓰면서 생기는 자료의 통계적 치우침을 다룬다. 의료 영상 응용에서는 병변(질병으로 달라진 조직 부분)의 위치 정보와 두 종류의 사진 차이를 학습하는 모듈(시스템에서 특정 기능을 맡는 구성 부분)을 개발해 각막염(눈 앞쪽 투명한 막인 각막에 생기는 염증) 사진을 분류한다.[^overview][^p6][^p7][^p8]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 음성 인식·번역, 얼굴 생성, 영상 이해, 모델의 신뢰성, 의료 영상 알고리즘을 고르게 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. 주요 저자 칸의 순서는 등록 저자 목록 기준이다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [ReFoCUS: Reinforcement-Guided Frame Optimization for Contextual Understanding](https://doi.org/10.1109/cvprf71909.2026.00796) · CVPR Findings | 영상에 대한 질문을 잘 풀도록 프레임을 고르는 학습 방법을 제안했다. 기준 모델이 프레임 조합에 주는 평가를 보상으로 사용해 선택 방법을 배우며, 질문과 앞선 선택을 조건으로 다음 프레임을 정한다. 프레임마다 정답을 직접 붙이지 않고도 질문과 관련 있는 장면 조합을 학습하고, 여러 영상 질의응답 평가에서 추론 정확도를 높였다.[^p1] | 1저자 Hosu Lee, 마지막 저자 노용만 |
| 2 | 2025 | [Zero-AVSR: Zero-Shot Audio-Visual Speech Recognition with LLMs by Learning Language-Agnostic Speech Representations](https://doi.org/10.1109/iccv51701.2025.00630) · ICCV | 대상 언어의 시청각 음성 자료를 학습에 쓰지 않고 말을 알아보는 틀을 제안했다. 음성과 입 모양에서 로마자 글을 예측하는 표현을 배운 뒤, 언어 모델이 이를 언어별 문자로 바꾸게 한다. 이 단계들을 잇는 방식과 시청각 표현을 언어 모델에 직접 연결하는 방식을 살폈다. 실험은 학습 때 본 언어를 넘어 지원 언어를 넓힐 가능성을 보여 준다.[^p2] | 1저자 Jeong Hun Yeo, 마지막 저자 노용만 |
| 3 | 2024 | [AV2AV: Direct Audio-Visual Speech to Audio-Visual Speech Translation with Unified Audio-Visual Speech Representation](https://doi.org/10.1109/cvpr52733.2024.02580) · CVPR | 소리와 입 모양 영상을 함께 받아 다른 언어의 소리와 얼굴 영상을 함께 출력하는 번역 방법이다. 먼저 시청각 정보를 함께 나타내는 표현을 배우고, 소리만 있는 번역 자료로 번역 시스템을 학습시킨다. 번역된 소리와 영상을 병렬로 만드는 생성기를 두어 원래 화자를 유지하고 입 움직임을 맞추도록 설계했으며, 여러 언어 사이의 번역 실험으로 평가했다.[^p3] | 1저자 Jeongsoo Choi, 마지막 저자 노용만 |
| 4 | 2022 | [SyncTalkFace: Talking Face Generation with Precise Lip-Syncing via Audio-Lip Memory](https://doi.org/10.1609/aaai.v36i2.20102) · AAAI | 음성에 맞는 세밀한 입 모양을 만들도록 음성과 입 움직임의 대응을 저장하는 메모리를 제안했다. 실제 영상에서 얻은 입 움직임 특징과 해당 음성 특징을 연결해 두고, 합성할 때 음성으로 관련 입 움직임을 불러온다. 영상 사이의 동기화를 위한 학습 조건도 추가했으며, 실험에서 입력 음성에 맞는 입 모양 영상을 생성하는 성능을 평가했다.[^p4] | 1저자 Se Jin Park, 마지막 저자 노용만 |
| 5 | 2025 | [VLsI: Verbalized Layers-to-Interactions from Large to Small Vision Language Models](https://doi.org/10.1109/cvpr52734.2025.02751) · CVPR | 큰 영상·언어 모델의 지식을 작은 모델로 옮기는 방법을 제안했다. 각 층의 특징을 언어 공간으로 바꾸는 중간 장치를 넣어 작은 모델이 큰 모델의 추론 과정을 층별로 따라 배우게 한다. 최종 출력만 흉내 내는 학습에서 생기는 불안정성을 줄이도록 설계했고, 여러 영상·언어 평가에서 성능을 검증했다.[^p5] | 1저자 Byung-Kwan Lee, 노용만은 5명 중 4번째 저자 |
| 6 | 2023 | [Demystifying Causal Features on Adversarial Examples and Causal Inoculation for Robust Network by Adversarial Instrumental Variable Regression](https://doi.org/10.1109/cvpr52729.2023.01184) · CVPR | 적대적 입력에 대한 예측을 인과 관계의 관점에서 분석했다. 알려지지 않은 다른 요인의 영향을 분리해 예측과 특징의 관계를 추정하고, 올바른 예측과 관련된 특징을 찾는 방법을 제안한다. 이 특징을 방어용 신경망에 전달해 적대적 입력에 대한 강건성을 높이는 방법도 제시했다.[^p6] | 공동 기여 저자 Byung-Kwan Lee·Junho Kim, 마지막 저자 노용만[^conf2] |
| 7 | 2024 | [Causal Mode Multiplexer: A Novel Framework for Unbiased Multispectral Pedestrian Detection](https://doi.org/10.1109/cvpr52733.2024.02529) · CVPR | 가시광과 열 영상을 함께 쓰는 보행자 검출기가 학습 자료의 상관관계에 치우치는 문제를 다룬다. 입력과 예측 사이의 인과 관계를 학습하는 틀을 제안하고, 기존 자료에서 잘 다루지 않은 가림 상황을 포함한 평가 자료도 만들었다. 기존 자료와 새 자료에서 통계적 치우침이 달라질 때의 검출 성능을 평가했다.[^p7] | 1저자 Taeheon Kim, 마지막 저자 노용만 |
| 8 | 2023 | [Deep learning-based classification system of bacterial keratitis and fungal keratitis using anterior segment images](https://doi.org/10.3389/fmed.2023.1162124) · Frontiers in Medicine | 눈 앞부분의 사진으로 세균성 각막염과 진균성 각막염을 구분하는 알고리즘을 제안했다. 병변의 위치를 배우는 모듈과 광폭 빔·세극 빔 두 종류의 사진에서 필요한 특징을 뽑아내는 모듈을 넣었다. 연구 자료와 외부 영상 자료에서 기준 분류기와 비교해 진단 분류 정확도의 개선 가능성을 보였다.[^p8] | 1저자 Yeo Kyoung Won, 노용만은 7명 중 6번째 저자 |

## 교수와 전문 분야

노용만 교수는 KAIST에서 1992년 박사학위를 받았으며, 전기및전자공학부 교수로 재직한다. 연구실 소개는 1997년 설립 때부터 IVY Lab을 이끌었다고 적는다. 교수 소개는 Columbia University와 University of California, Berkeley에서의 연구 경력, University of Toronto에서의 방문교수 경력을 밝힌다.[^dept][^prof][^overview]

교수 소개가 제시하는 전문 분야는 영상·음성·언어의 통합, 멀티모달 학습, 물체와 움직임의 인식, 사람 사이의 의사소통을 지원하는 방법, 모델의 판단 근거와 강건성, 컴퓨터 비전과 멀티미디어다. 최근 논문에서는 여러 언어의 음성 인식과 번역, 말하는 얼굴 생성, 질문에 맞춘 영상 이해, 적대적 입력과 자료 편향을 다루는 알고리즘으로 이어진다.[^prof][^p1][^p2][^p3][^p4][^p6][^p7]

## 응용 분야

연구실 소개는 시청각 음성 인식, 다국어 번역, 영상 설명 생성, 영상 검색, 음성 향상, 장면 이해, 여러 의사소통 조건의 사람 사이 대화를 응용 대상으로 든다. 영상·언어 모델을 통한 질의응답과 보행자 검출, 의료 영상 분류도 논문에서 다루는 응용이다.[^overview][^p1][^p7][^p8]

## 구성원

2026년 11월 9일 연구실 Members 쪽 기준이다. 박사후연구원 1명, 박사과정 12명, 석사과정 4명이며 과정과 괄호의 역할·소속은 연구실 게시 표기다. ‘대표 논문 참여’는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Jeong Hun Yeo | 박사후연구원 | sedne246@kaist.ac.kr | 2 |
| Hyun Jun Kim | 박사과정 | kimhj709@kaist.ac.kr |  |
| Chae Won Kim | 박사과정 | chaewonkim@kaist.ac.kr | 2 |
| Yeon Ju Kim | 박사과정 | yeonju7.kim@kaist.ac.kr |  |
| Hyeongseop Rha | 박사과정 (Student Representative) | ryool_1832@kaist.ac.kr |  |
| Beomchan Park | 박사과정 | bpark0810@kaist.ac.kr |  |
| Minho Park | 박사과정 | roger618@kaist.ac.kr |  |
| Sangyun Chung | 박사과정 | jelarum@kaist.ac.kr |  |
| Bella Godiva | 박사과정 | bgodiva@kaist.ac.kr |  |
| Sung Kwang Cho | 박사과정 (Samsung Electronics, Device Solutions, System LSI) | sungkwang2@kaist.ac.kr |  |
| Youngchae Chee | 박사과정 | litcoderr@kaist.ac.kr |  |
| Juwan Chung | 박사과정 | juwan99@kaist.ac.kr |  |
| Junil Won | 박사과정 | dnjswnsdlf48@kaist.ac.kr |  |
| Seongho Kim | 석사과정 | taho43@kaist.ac.kr |  |
| Hosu Lee | 석사과정 | leehosu01@kaist.ac.kr | 1 |
| Sunghyun Lee | 석사과정 | romanticbox@kaist.ac.kr |  |
| Minyeong Jeong | 석사과정 | alsdud6943@kaist.ac.kr |  |

## 졸업생 진로

연구실 Alumni 쪽의 박사 40행과 석사 69행이다. 학위·연도·진로는 게시 표기대로이며 같은 이름이 다른 학위 구획에 있으면 각 행을 두었다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Taeheon Kim | Ph.D. (2026) |  |
| Jeong Hun Yeo | Ph.D. (2026) | Postdoctal researcher at IVL Lab, KAIST |
| Se Jin Park | Ph.D. (2026) | Assistant Professor at Kyung Hee University |
| Sungjune Park | Ph.D. (2026) | Postdoctal researcher at IVL Lab, KAIST |
| Youngjoon Yu | Ph.D. (2026) | Postdoctal researcher at IVL Lab, KAIST |
| Yeongyun Kim | Ph.D. (2026) | Principal Researcher at Agency for Defense Development (ADD) |
| Byung Kwan Lee | Ph.D. (2025) | Research Scientist at NVIDIA |
| Junho Kim | Ph.D. (2025) | Postdoctoral researcher at University of Illinois Urbana–Champaign (UIUC) |
| Seongyeop Kim | Ph.D. (2025) | Senior Researcher at ETRI |
| Minsu Kim | Ph.D. (2024) | Research Scientist at DeepMind |
| Joanna Hong | Ph.D. (2024) | Research Scientist at DeepMind |
| Hakmin Lee | Ph.D. (2024) | Senior Researcher at Samsung Electronics |
| Hong Joo Lee | Ph.D. (2023) | Assistant Professor at Seoul National University of Science and Technology |
| Sangmin Lee | Ph.D. (2023) | Professor at Sungkyunkwan University (SKKU) |
| Jung Uk Kim | Ph.D. (2022) | Professor at Kyung Hee University (KHU) |
| Hyung-Il Kim | Ph.D. (2021) | Professor at Chonnam National University |
| Jongho Lee | Ph.D. (2021) | Senior Researcher at Agency for Defense Development (ADD) |
| Wissam J. Baddar | Ph.D. (2019) | Senior Researcher at Samsung Advanced Institute of Technology (SAIT) |
| Leslie Tiong Ching Ow | Ph.D. (2019) | Senior Researcher at Semiconductor Research Center, Samsung Electronics |
| Hak Gu Kim | Ph.D. (2019) | Professor at Chung-Ang University (CAU) |
| Seong Tae Kim | Ph.D. (2019) | Professor at Kyung Hee University (KHU) |
| Seong-Il Lee | Ph.D. | Senior Researcher at SK Hynix |
| Dae Hoe Kim | Ph.D. | Senior Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Sang-Heun Shim | Ph.D. | Senior Researcher at Agency for Defense Development (ADD) |
| Seung Ho Lee | Ph.D. | Professor at Korea Tech |
| Semin Kim | Ph.D. | Professor at Andong National University |
| Hosik Sohn | Ph.D. | Senior Researcher at Samsung Electronics |
| Ju-Won  Kwon | Ph.D. | USA |
| Jae Hyun Jeon | Ph.D. | Senior Researcher at DTaQ |
| Hyun Seok Min | Ph.D. | Senior Researcher at Tomocube |
| Sihyoung Lee | Ph.D. | Senior Researcher at Samsung Electronics |
| Jae Young Choi | Ph.D. | Professor at Hankuk University of Foreign Studies (HUFS) |
| Cheon Seog Kim | Ph.D. | CEO at Woori Computer System Technology |
| Sung Ho Jin | Ph.D. | Senior Researcher at NICE Information Service |
| Cong-Thang Truong | Ph.D. | Professor at The University of Aizu, Japan |
| Seung Ji Yang | Ph.D. | Executive Vice President  at SK Telecom |
| Tae Meon Bae | Ph.D. | Senior Researcher at SHARP Laboratories of America |
| Ho Kyung kang | Ph.D. | Senior Researcher at Samsung Electronics |
| Ki Hyun Kim | Ph.D. | Senior Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Yong Ju Jung | Ph.D. | Professor at Gachon University |
| Se Yeon Kim | M.S. (2026) |  |
| Damin Yeom | M.S. (2025) | Researcher at Samsung Electronics |
| Dahye Lee | M.S. (2025) | Ph.D. at AMI Lab, KAIST |
| Seunghee Han | M.S. (2024) | Researcher at Samsung Electronics |
| Sebin Shin | M.S. (2024) | Researcher at AVIKUS |
| Jongwook Han | M.S. (2023) | Ph.D. Student at Seoul National University |
| Godiva Bella | M.S. (2023) |  |
| Byeongcheon Kim | M.S. (2021) | Researcher at Samsung Electronics |
| Dae Hwi Choi | M.S. (2021) | Researcher at Samsung Electronics |
| Eunsung Kim | M.S. (2020) | Researcher at TmaxSoft |
| Minho Park | M.S. (2020) | Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Hyebin Lee | M.S. (2020) | Law student at SKKU Law School |
| Sangmin Lee | M.S. (2019) | Researcher at YBRAIN |
| Hyeonok Park | M.S. (2019) | Researcher at Samsung Electronics |
| Kihyun Kim | M.S. (2019) | Researcher at LG Display |
| Jung Su Kwon | M.S. (2019) | Researcher at Koh Young Technology |
| Heountaek Lim | M.S. | Researcher at NC Soft |
| Tae Kwan Lee | M.S. | Researcher at NAVER Clova |
| Geon Mo Gu | M.S. | Researcher at NAVER Clova |
| Seong Wook Ham | M.S. | Ph. D. candidate at KAIST |
| Hyunwook Jeong | M.S. | Researcher at Hyundai Mobis |
| Yeoreum Choi | M.S. | Researcher at Agency for Defense Development (ADD) |
| Junam Song | M.S. | Researcher at Samsung Electronics |
| Sung Yeong Park | M.S. | Researcher at Agency for Defense Development (ADD) |
| Jisoo Son | M.S. | Researcher at JLK-Inspection |
| Jeongjik Seo | M.S. | Researcher at Agency for Defense Development (ADD) |
| Dongkyu Kim | M.S. | Ph. D. candidate at KAIST |
| Soo Sung Yoon | M.S. | Researcher at Agency for Defense Development (ADD) |
| Jung Ik Moon | M.S. | Researcher at SK Hynix |
| Eunjoon Kim | M.S. | Researcher at Agency for Defense Development (ADD) |
| Jin Hyon Hwang | M.S. | Researcher at Hyundai Motors |
| Seung Hyun Lee | M.S. | Researcher at LG Electronics |
| Wook Jin Shin | M.S. | Researcher at Hyundai Motors |
| Won Yong Eom | M.S. | Researcher at Defense Agency for Technology and Quality |
| Jae Hyun Jeon | M.S. | Researcher at Defense Agency for Technology and Quality |
| Min Seo Choi | M.S. | Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| In A Jo | M.S. | Researcher at Korea Air |
| Esla Timothy Anzaku | M.S. | Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Sun Il Jo | M.S. | Researcher at Agency for Defense Development (ADD) |
| Jae Seok Jang | M.S. | Researcher at Samsung Electronics |
| Young Bok Lee | M.S. | Researcher at Toss Lab |
| Hana Yoo | M.S. | Researcher at Hyundai Motors |
| Jong Su Choi | M.S. | Researcher at Defense Agency for Technology and Quality |
| Yeon Gyun Kim | M.S. | Researcher at Agency for Defense Development (ADD) |
| Dong Su Lee | M.S. | Researcher at HUMAX |
| Bwalya Kelvin | M.S. | Researcher at Zambia Revenue Autho |
| Jung Hwa Choi | M.S. | Researcher at Samsung Electronics |
| Dong Jun Suh | M.S. | Researcher at Korea Institute of Science and Information Technology (KISTI) |
| Do Quan | M.S. | Researcher at GIST |
| Yong Geun Won | M.S. | Researcher at Korean Broadcasting System (KBS) |
| Jun Ho Cho | M.S. | Researcher at Samsung Electronics |
| Kyong Sok Seo | M.S. | Researcher at Samsung Electronics |
| Duck Yeon Kim | M.S. | Researcher at Samsung Electronics |
| Young Suk Kim | M.S. | Researcher at Korea Telecom (KT) |
| Seok-Jun Kang | M.S. | Researcher at Daewoo Electronics |
| Sun-Woo Yang | M.S. | Researcher at LG Electronics |
| Hee-Jun Han | M.S. | Researcher at Korea Institute of Science and Information Technology (KISTI) |
| Jin-Ho Choo | M.S. | Researcher at Samsung Electronics |
| Jaewook Lee | M.S. | Researcher at LASPURT |
| Nguyen Ngoc Thanh | M.S. | Researcher at Vietnam Post and Telecom |
| Beet-Nara Bae | M.S. | Researcher at HUMAX |
| Hee-Kyung Lee | M.S. | Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Kwang-Suh Jung | M.S. | Researcher at LG Electronics |
| Yoon Jeong Hyun | M.S. | Researcher at Electronics and Telecommunications Research Institute (ETRI) |
| Sung-Kon Oh | M.S. | Researcher at Ministry of Science and ICT |
| Woon-Kee Min | M.S. | Researcher at IBM |
| So-Yeon Kim | M.S. | Researcher at Agency for Defense Development (ADD) |
| Ki-Won You | M.S. | Researcher at Samsung Electronics |
| Jin-Hwan Lee | M.S. | Senior researcher at Electronics and Telecommunications Research Institute (ETRI) |

## 최근 5년 논문 목록

연구실 국제 학회·국제 학술지 목록의 2021–2026년 98편이다. 제목·저자·발표처는 연구실 표기이며 DOI를 함께 적었다. 학회 채택 항목은 ‘채택’, 학술지 게재 승인 항목은 ‘게재 승인’으로 표시했다. 연도 없이 게시된 학술지 세 편은 등록 연도인 2026년에 두었다. ‘연구실 기재’는 연구실이 적은 발표처 표기다.[^conference][^conf2][^journal][^home][^oa]

**2026**

- Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro. "Diffusion Large Language Models for Visual Speech Recognition". \*EMNLP 2026 (채택)\*.
- Youngchae Chee\*, Hosu Lee\*, Sungjune Park, Junho Kim, Yong Man Ro (\*equal contribution). "PRISM: Predictive Recomposition via Semantic Latent Decomposition for View-invariant Video Representation Learning". \*EMNLP 2026 (채택)\*.
- Juwan Chung, Sungjune Park, Yeongyun Kim, Yong Man Ro. "From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs". \*EMNLP 2026 (채택)\*.
- Jeong Hun Yeo, Minsu Kim, Hyeongseop Rha, Yong Man Ro. "Decoding Strategies for Diffusion-Based ASR: A Systematic Evaluation of Confidence-Based Thresholding". \*EMNLP 2026 (채택)\*.
- Bella Godiva, Yeonju Kim, Yong Man Ro. "Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models". \*EMNLP 2026 (채택)\*.
- Minho Park, Minyeong Ju, Yong Man Ro. "PhysCache: Accelerating Physics-Sensitive Image Editing with Risk-Aware Caching". \*BMVC 2026 (채택)\*.
- Junho Kim, Hosu Lee, James M. Rehg, Minsu Kim, Yong Man Ro. "STRIDE: When to Speak Meets Sequence Denoising for Streaming Video Understanding". \*ECCV 2026 (채택)\*.
- Byung-Kwan Lee, Ryo Hachiuma, Yong Man Ro, Yu-Chiang Frank Wang, Yueh-Hua Wu. "GenRecal: Generation after Recalibration from Large to Small Vision-Language Models". \*ECCV 2026\*. DOI <https://doi.org/10.1007/978-3-032-37281-9_9>.
- Sangyun Chung, Se Yeon Kim, Youngchae Chee, and Yong Man Ro. "MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models". \*CVPR 2026 (채택)\*.
- Byung-Kwan Lee\*,  Youngchae Chee\*, Yong Man Ro (\*equal contribution). "Recursive Think-Answer Process for LLMs and VLMs". \*CVPR 2026 Findings\*. DOI <https://doi.org/10.1109/cvprf71909.2026.00920>.
- Hosu Lee\*, Junho Kim\*, Hyunjun Kim, Yong Man Ro (\*equal contribution). "ReFoCUS: Reinforcement-guided Frame Optimization for Contextual Understanding". \*CVPR 2026 Findings\*. DOI <https://doi.org/10.1109/cvprf71909.2026.00796>.
- Beomchan Park\*, Seongho Kim\*, Hyunjun Kim, Sungjune Park, Yong Man Ro (\*equal contribution). "Robust Grounding with MLLMs against Occlusion and Small Objects via Language-Guided Semantic Cues". \*ICASSP 2026\*. DOI <https://doi.org/10.1109/icassp55912.2026.11463586>.
- Hyeongseop Rha, Jeong Hun Yeo, KIM YEONJU, Yong Man Ro. "Emotion-Coherent Reasoning for Multimodal LLMs via Emotional Rationale Verifier". \*AAAI 2026 (연구실 기재)\*.
- Yeonju Kim, Se Jin Park, Yong Man Ro. "Empathetic Response in Audio-Visual Conversations Using Emotion Preference Optimization and MambaCompressor". \*IEEE Transactions on Affective Computing (게재 승인)\*. DOI <https://doi.org/10.1109/taffc.2026.3707832>.
- Sangyun Chung\*, Youngjoon Yu\*, Se Yeon Kim, Youngchae Chee, Yong Man Ro (\*equal contribution). "Enhanced Vision-Language Models for Diverse Sensor Understanding: Cost-Efficient Optimization and Benchmarking". \*IEEE Transactions on Image Processing (게재 승인)\*. DOI <https://doi.org/10.1109/tip.2026.3707796>.
- Jeong Hun Yeo\*, Sangyun Chung\*, Sungjune Park, Dae Hoe Kim, Jinyoung Moon, Yong Man Ro (\*equal contribution). "GCAgent: Long-Video Understanding via Schematic and Narrative Episodic Memory". \*IEEE Transactions on Multimedia (게재 승인)\*. DOI <https://doi.org/10.1109/tmm.2026.3724344>.
- Youngjoon Yu, Yong Man Ro. "A Causal Lens on Non-RGB Vision Sensor Understanding in Vision Language Models". \*IEEE Transactions on Image Processing, vol. 35, pp. 3909-3924, 2026\*. DOI <https://doi.org/10.1109/tip.2026.3675431>.
- Seongyeop Kim, Hyung-Il Kim, Yong Man Ro. "Adaptive Integration of Textual Context and Visual Embeddings for Underrepresented Vision Classification". \*Pattern Recognition, vol. 172, pp. 112420, 2026\*. DOI <https://doi.org/10.1016/j.patcog.2025.112420>.
- Junho Kim\*, Byung-Kwan Lee\*, Yong Man Ro (\*equal contributor). "Causal Unsupervised Semantic Segmentation". \*Pattern Recognition, vol. 171, pp. 112173, 2026\*. DOI <https://doi.org/10.1016/j.patcog.2025.112173>.
- Minsu Kim, Jee-weon Jung, Hyeongseop Rha, Soumi Maiti, Siddhant Arora, Xuankai Chang, Shinji Watanabe,  Yong Man Ro. "TMT: Tri-Modal Translation between Speech, Image, and Text by Processing Different Modalities as Different Languages". \*IEEE Transactions on Multimedia, vol. 28, pp. 1976-1988, Jan. 2026\*.

**2025**

- Byung-Kwan Lee,  Ryo Hachiuma, Yong Man Ro, Frank Wang, Yueh-Hua Wu. "Unified Reinforcement and Imitation Learning for Vision-Language Models". \*NeurIPS 2025\*. DOI <https://doi.org/10.52202/085713-5231>.
- Youngchae Chee, Taeheon Kim, Youngjoon Yu, HyunWook Park, and Yong Man Ro. "Closing the Modality Gap: Integrating LLMs with LiDAR for 3D Object Detection and Object-level Understanding". \*ICIP 2025\*.
- Minho Park, Young Joo Jo, Jae-Hyeok Lee, Ji Yong Lee, Dong-oh Kang, Yong Man Ro. "Focus Where It Matters: LLM-Guided Regional Identification for Instruction-based Image Editing". \*ACM MM 2025\*. DOI <https://doi.org/10.1145/3746027.3754711>.
- Jeong Hun Yeo, Minsu Kim, Chae Won Kim, Stavros Petridis, Yong Man Ro. "Zero-AVSR: Zero-Shot Audio-Visual Speech Recognition with LLMs by Learning Language-Agnostic Speech Representations". \*ICCV 2025\*. DOI <https://doi.org/10.1109/iccv51701.2025.00630>.
- Jeong Hun Yeo, Hyeongseop Rha, Se Jin Park, Yong Man Ro. "MMS-LLaMA: Efficient LLM-based Audio-Visual Speech Recognition with Minimal Multimodal Speech Tokens". \*ACL 2025\*. DOI <https://doi.org/10.18653/v1/2025.findings-acl.1065>.
- Se Jin Park, Julian Salazar, Aren Jansen, Keisuke Kinoshita, Yong Man Ro, RJ Skerry-Ryan. "Long-Form Speech Generation with Spoken Language Models". \*ICML 2025 Oral\*.
- Junho Kim\*, Hyunjun Kim\*, Hosu Lee, Yong Man Ro (\* equal contributor). "SALOVA: Segment-Augmented Long Video Assistant for Targeted Retrieval and Routing in Long-Form Video Analysis". \*CVPR 2025\*. DOI <https://doi.org/10.1109/cvpr52734.2025.00318>.
- Byung-Kwan Lee, Ryo Hachiuma, Yu-Chiang Frank Wang, Yong Man Ro, Yueh-Hua Wu. "VLsI: Verbalized Layers-to-Interactions from Large to Small Vision Language Models". \*CVPR 2025\*. DOI <https://doi.org/10.1109/cvpr52734.2025.02751>.
- Jeong Hun Yeo, Chae Won Kim, Hyunjun Kim, Hyeongseop Rha, Seunghee Han, Wen-Huang Cheng, Yong Man Ro. "Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language". \*AAAI 2025\*. DOI <https://doi.org/10.1609/aaai.v39i9.33026>.
- Taeheon Kim, Sangyun Chung, Damin Yeom, Youngjoon Yu, Hak Gu Kim, Yong Man Ro. "MSCoTDet: Language-driven Multi-modal Fusion for Improved Multispectral Pedestrian Detection". \*IEEE Transactions on Circuits and Systems for Video Technology, vol. 35, no. 5, pp. 5006-5021, May 2025\*. DOI <https://doi.org/10.1109/tcsvt.2024.3524645>.
- Minsu Kim, Hyeong-Il Kim, Yong Man Ro. "Prompt Tuning of Deep Neural Networks for Speaker-adaptive Visual Speech Recognition". \*IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 47, no. 2, pp. 1042-1055, Feb. 2025\*. DOI <https://doi.org/10.1109/tpami.2024.3484658>.
- Youngjoon Yu, Yeonju Kim, Yong Man Ro. "Advancing Causal Intervention in Image Captioning with Causal Prompt". \*IEEE Transactions on Neural Networks and Learning Systems, vol. 36, no. 7, pp. 12631-12642, July 2025\*. DOI <https://doi.org/10.1109/tnnls.2024.3487200>.

**2024**

- Byung-Kwan Lee, Chae Won Kim, Beomchan Park, Yong Man Ro. "Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models". \*NeurIPS 2024\*. DOI <https://doi.org/10.52202/079017-1274>.
- Junho Kim\*, Hyunjun Kim\*, Yeonju Kim, Yong Man Ro (\*equal contribution). "CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models". \*NeurIPS 2024\*. DOI <https://doi.org/10.52202/079017-4246>.
- Byung-Kwan Lee, Sangyun Chung, Chae Won Kim, Beomchan Park, Yong Man Ro. "TroL: Traversal of Layers for Large Language and Vision Models". \*EMNLP 2024\*. DOI <https://doi.org/10.18653/v1/2024.emnlp-main.633>.
- Jeong Hun Yeo\*, Seunghee Han\*, Minsu Kim, Yong Man Ro (\* equal contributor). "Where Visual Speech Meets Language: VSP-LLM Framework for Efficient and Context-Aware Visual Speech Processing". \*EMNLP 2024\*. DOI <https://doi.org/10.18653/v1/2024.findings-emnlp.666>.
- Junho Kim, Yeon Ju Kim, Yong Man Ro. "What if...?: Thinking Counterfactual Keywords Helps to Mitigate Hallucination in Large Multi-modal Models". \*EMNLP 2024\*. DOI <https://doi.org/10.18653/v1/2024.findings-emnlp.626>.
- Minsu Kim\*, Jeonghun Yeo\*, Se Jin Park, Hyeongseop Rha, Yong Man Ro (\* equal contributor). "Efficient Training for Multilingual Visual Speech Recognition: Pre-training with Discretized Visual Speech Representation". \*ACM Multimedia 2024\*. DOI <https://doi.org/10.1145/3664647.3681221>.
- Byung-Kwan Lee, Beomchan Park, Chae Won Kim, Yong Man Ro. "MoAI: Mixture of All Intelligence for Large Language and Vision Models". \*ECCV 2024\*. DOI <https://doi.org/10.1007/978-3-031-72967-6_16>.
- Hyunjun Kim, Dahye Lee, Sungjune Park, Yong Man Ro. "Weather-aware Drone-view Object Detection via Environmental Context Understanding". \*ICIP 2024\*. DOI <https://doi.org/10.1109/icip51287.2024.10647388>.
- Taeheon Kim\*, Sangyun Chung\*, Youngjoon Yu\*, Yong Man Ro (\* equal contributor). "Revisiting Misalignment in Multispectral Pedestrian Detection: A Language-driven Approach for Cross-modal Alignment Fusion". \*ICIP Workshop 2024\*. DOI <https://doi.org/10.1109/icipcw64161.2024.10769164>.
- Byung-Kwan Lee, Beomchan Park, Chae Won Kim, Yong Man Ro. "CoLLaVO: Crayon Large Language and Vision mOdel". \*ACL 2024\*. DOI <https://doi.org/10.18653/v1/2024.findings-acl.66>.
- Se Jin Park\*, Chae Won Kim\*, Hyeongseop Rha, Minsu Kim, Joanna Hong, Jeonghun Yeo, and Yong Man Ro (\* equal contributor). "Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation". \*ACL 2024 (Oral)\*. DOI <https://doi.org/10.18653/v1/2024.acl-long.860>.
- Taeheon Kim\*, Sebin Shin\*, Youngjoon Yu, Hak Gu Kim, and Yong Man Ro (\* equal contributor). "Causal Mode Multiplexer: A Novel Framework for Unbiased Multispectral Pedestrian Detection". \*CVPR 2024\*. DOI <https://doi.org/10.1109/cvpr52733.2024.02529>.
- Jeongsoo Choi\*, Se Jin Park\*, Minsu Kim\* and Yong Man Ro (\* equal contributor). "AV2AV: Direct Audio-Visual Speech to Audio-Visual Speech Translation with Unified Audio-Visual Speech Representation". \*CVPR 2024\*. DOI <https://doi.org/10.1109/cvpr52733.2024.02580>.
- Minsu Kim, Jeongsoo Choi, Soumi Maiti, Jeong Hun Yeo, Shinji Watanabe, and Yong Man Ro. "Towards Practical and Efficient Image-To-Speech Captioning With Vision-Language Pre-Training and Multi-Modal Tokens". \*ICASSP 2024\*. DOI <https://doi.org/10.1109/icassp48485.2024.10446888>.
- Jeong Hun Yeo\*, Minsu Kim\*, Shinji Watanabe, and Yong Man Ro. "Visual Speech Recognition for Languages with Limited Labeled Data using Automatic Labels from Whisper". \*ICASSP 2024\*. DOI <https://doi.org/10.1109/icassp48485.2024.10446720>.
- Seunghee Han, Se Jin Park, Chae Won Kim, and Yong Man Ro. "Persona Extraction through Semantic Similarity for Emotional Support Conversation Generation". \*ICASSP 2024\*. DOI <https://doi.org/10.1109/icassp48485.2024.10445957>.
- Jeongsoo Choi, Minsu Kim, Se Jin Park, and Yong Man Ro. "Text-driven Talking Face Synthesis by Reprogramming Audio-driven Models". \*ICASSP 2024\*. DOI <https://doi.org/10.1109/icassp48485.2024.10448506>.
- Se Jin Park, Minsu Kim, Jeongsoo Choi, and Yong Man Ro. "Exploring Phonetic Context-aware Lip-Sync for Talking Face Generation". \*ICASSP 2024\*. DOI <https://doi.org/10.1109/icassp48485.2024.10447284>.
- Seongyeop Kim, Hyung-Il Kim, and Yong Man Ro. "Improving Open Set Recognition via Visual Prompts distilled from Common-sense Knowledge". \*AAAI 2024\*. DOI <https://doi.org/10.1609/aaai.v38i3.28058>.
- Minsu Kim, Jeongsoo Choi, Dahun Kim, Yong Man Ro. "Textless Unit-to-Unit training for Many-to-Many Multilingual Speech-to-Speech Translation". \*IEEE Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 3934-3946, 2024.\*. DOI <https://doi.org/10.1109/taslp.2024.3444470>.
- Sangmin Lee, Hyung-Il Kim, Yong Man Ro. "Text-Guided Distillation Learning to Diversify Video Embeddings for Text-Video Retrieval". \*Pattern Recognition, vol. 156, no. 3, pp. 110754, 2024.\*. DOI <https://doi.org/10.1016/j.patcog.2024.110754>.
- Sungjune Park\*, Hyunjun Kim\*, Yong Man Ro (\* equal contributor). "Robust Pedestrian Detection via Constructing Versatile Pedestrian Knowledge Bank". \*Pattern Recognition, vol. 153, no. 4, pp. 110539, 2024.\*. DOI <https://doi.org/10.1016/j.patcog.2024.110539>.
- Sungjune Park\*, Hyunjun Kim\*, Yong Man Ro (\* equal contributor). "Integrating Language-Derived Appearance Elements with Visual Cues in Pedestrian Detection". \*IEEE Transactions on Circuits and Systems for Video Technology, pp. 1-1, 2024.\*. DOI <https://doi.org/10.1109/tcsvt.2024.3383914>.
- Jeong Hun Yeo, Minsu Kim, Jeongsoo Choi, Dae Hoe Kim, and Yong Man Ro. "AKVSR: Audio Knowledge Empowered Visual Speech Recognition by Compressing Audio  Knowledge of a Pretrained Model". \*IEEE Transactions on Multimedia, vol. 26, pp. 6462-6474, 2024.\*. DOI <https://doi.org/10.1109/tmm.2024.3352388>.
- Hong Joo Lee and Yong Man Ro. "Defending Video Recognition Model against Adversarial Perturbations via Defense Patterns". \*IEEE Transactions on Dependable and Secure Computing, vol. 21, no. 04, pp. 4110-4121, 2024.\*. DOI <https://doi.org/10.1109/tdsc.2023.3346064>.
- Hong Joo Lee, Youngjoon Yu, and Yong Man Ro. "Advancing Adversarial Training by Injecting Booster Signal". \*IEEE Transactions on Neural Networks and Learning Systems, vol. 35, no. 9, pp. 12665-12677, Sept. 2024\*. DOI <https://doi.org/10.1109/tnnls.2023.3264256>.

**2023**

- Joanna Hong, Se Jin Park, and Yong Man Ro. "Intuitive Multilingual Audio-Visual Speech Recognition with a Single-Trained Model". \*EMNLP 2023\*. DOI <https://doi.org/10.18653/v1/2023.findings-emnlp.324>.
- Minsu Kim\*, Jeong Hun Yeo\*, Jeongsoo Choi, and Yong Man Ro (\* equal contribution). "Lip Reading for Low-resource Languages by Learning and Combining General Speech Knowledge and Language-specific Knowledge". \*ICCV 2023\*. DOI <https://doi.org/10.1109/iccv51070.2023.01409>.
- Byung-Kwan Lee\*, Junho Kim\*, and Yong Man Ro (\* equally contributed). "Mitigating Adversarial Vulnerability through Causal Parameter Estimation by Adversarial Double Machine Learning". \*ICCV 2023\*. DOI <https://doi.org/10.1109/iccv51070.2023.00415>.
- Jeongsoo Choi\*, Joanna Hong\*, and Yong Man Ro (\* equally contributed). "DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding". \*ICCV 2023\*. DOI <https://doi.org/10.1109/iccv51070.2023.00718>.
- YeonJu Kim, Junho Kim, Byung-Kwan Lee, Sebin Shin, and Yong Man Ro. "Mitigating Dataset Bias in Image Captioning through CLIP Confounder-free Captioning Network". \*ICIP 2023\*. DOI <https://doi.org/10.1109/icip49359.2023.10222502>.
- Sungjune Park, Jung Uk Kim, Jin Mo Song, and Yong Man Ro. "Robust multispectral pedestrian detection via spectral position-free feature mapping". \*ICIP 2023\*. DOI <https://doi.org/10.1109/icip49359.2023.10222485>.
- Jeongsoo Choi, Minsu Kim, and Yong Man Ro. "Intelligible Lip-to-speech Synthesis with Speech Units". \*INTERSPEECH 2023\*. DOI <https://doi.org/10.21437/interspeech.2023-194>.
- Joanna Hong\*, Minsu Kim\*, Jeongsoo Choi, and Yong Man Ro (\* equally contributed). "Watch or Listen: Robust Audio-Visual Speech Recognition with Visual Corruption Modeling and Reliability Scoring". \*CVPR 2023\*. DOI <https://doi.org/10.1109/cvpr52729.2023.01801>.
- Byung-Kwan Lee\*, Junho Kim\*, and Yong Man Ro (\*: equally contributed). "Demystifying Causal Features on Adversarial Examples and Causal Inoculation for Robust Network by Adversarial Instrumental Variable Regression". \*CVPR 2023\*. DOI <https://doi.org/10.1109/cvpr52729.2023.01184>.
- Minsu Kim\*, Joanna Hong\*, and Yong Man Ro (\* equally contributed). "Lip-to-speech Synthesis in the Wild with Multi-task Learning". \*ICASSP 2023\*. DOI <https://doi.org/10.1109/icassp49357.2023.10095582>.
- Jung Uk Kim and Yong Man Ro. "Similarity Relation Preserving Cross-Modal Learning For Multispectral Pedestrian Detection Against Adversarial Attacks". \*ICASSP 2023\*. DOI <https://doi.org/10.1109/icassp49357.2023.10096549>.
- Jeong Hun Yeo, Minsu Kim, and Yong Man Ro. "Multi-Temporal Lip-Audio Memory for Visual Speech Recognition". \*ICASSP 2023\*. DOI <https://doi.org/10.1109/icassp49357.2023.10094693>.
- Minsu Kim,  Chae Won Kim, and Yong Man Ro. "Deep Visual Forced Alignment: Learning to Align Transcription with Talking Face Video". \*AAAI 2023\*. DOI <https://doi.org/10.1609/aaai.v37i7.25998>.
- Taeheon Kim, Youngjoon Yu, and Yong Man Ro. "Multispectral Invisible Coating: Laminated Visible-Thermal Physical Attack against Multispectral Object Detectors using Transparent Low-e films". \*AAAI 2023\*. DOI <https://doi.org/10.1609/aaai.v37i1.25197>.
- Jung Uk Kim and Yong Man Ro. "Enabling Visual Object Detection with Object Sounds via Visual Modality Recalling Memory". \*IEEE Transactions on Neural Networks and Learning Systems, pp. 1-13, 2023.\*. DOI <https://doi.org/10.1109/tnnls.2023.3323560>.
- Hakmin Lee and Yong Man Ro. "Adversarial anchor-guided feature refinement for adversarial defense". \*Image and Vision Computing, vol. 136, pp. 104722, 2023.\*. DOI <https://doi.org/10.1016/j.imavis.2023.104722>.
- Hong Joo Lee and Yong Man Ro. "Robust Proxy: Improving Adversarial Robustness by Robust Proxy Learning". \*IEEE Transactions on Information Forensics & Security, vol. 18, pp. 4021-4033, 2023\*. DOI <https://doi.org/10.1109/tifs.2023.3288672>.
- Yeo Kyoung Won\*, Hyebin Lee\*, Youngjun Kim, Gyule Han, Tae-Young Chung, Yong Man Ro and Dong Hui Lim (\* equal contributor). "Deep learning-based classification system of bacterial keratitis and fungal keratitis using anterior segment images". \*Frontiers in Medicine, vol. 10, pp. 1162124, 2023.\*. DOI <https://doi.org/10.3389/fmed.2023.1162124>.
- Jung Uk Kim, Hyung-Il Kim, and Yong Man Ro. "Stereoscopic Vision Recalling Memory for Monocular 3D Object Detection". \*IEEE Transactions on Image Processing, vol. 32, pp. 2749-2760, 2023.\*. DOI <https://doi.org/10.1109/tip.2023.3274479>.

**2022**

- Taeheon Kim, Youngjoon Yu, and Yong Man Ro. "Defending Physical Adversarial Attack on Object Detection via Adversarial Patch-Feature Energy". \*ACM MM 2022\*. DOI <https://doi.org/10.1145/3503161.3548362>.
- Minsu Kim, Hyunjun Kim, and Yong Man Ro. "Speaker-adaptive Lip Reading with User-dependent Padding". \*ECCV 2022\*. DOI <https://doi.org/10.1007/978-3-031-20059-5_33>.
- Joanna Hong, Minsu Kim, and Yong Man Ro. "VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection". \*ECCV 2022\*. DOI <https://doi.org/10.1007/978-3-031-20059-5_26>.
- Sangmin Lee, Sungjune Park, and Yong Man Ro. "Audio-Visual Mismatch-Aware Video Retrieval via Association and Adjustment". \*ECCV 2022\*. DOI <https://doi.org/10.1007/978-3-031-19781-9_29>.
- Joanna Hong\*, Minsu Kim\*, Daehun Yoo, and Yong Man Ro (\* equally contributed). "Visual Context-driven Audio Feature Enhancement for Robust End-to-End Audio-Visual Speech Recognition". \*Interspeech 2022\*. DOI <https://doi.org/10.21437/interspeech.2022-11311>.
- Byung-Kwan Lee\*, Junho Kim\*, Yong Man Ro (\*: equally contributed). "Masking Adversarial Damage: Finding Adversarial Saliency for Robust and Sparse Network". \*CVPR 2022\*. DOI <https://doi.org/10.1109/cvpr52688.2022.01470>.
- Sangmin Lee, Hyung-Il Kim, and Yong Man Ro. "Weakly Paired Associative Learning for Sound and Image Representations via Bimodal Associative Memory". \*CVPR 2022\*. DOI <https://doi.org/10.1109/cvpr52688.2022.01028>.
- Taeheon Kim, Hong Joo Lee, Yong Man Ro. "MAP: Multispectral Adversarial Patch to Attack Person Detection". \*ICASSP 2022\*. DOI <https://doi.org/10.1109/icassp43922.2022.9747896>.
- Sungjune Park, Dae Hwi Choi, Jung Uk Kim, Yong Man Ro. "Robust Thermal Infrared Pedestrian Detection by Associating Visible Pedestrian Knowledges". \*ICASSP 2022\*. DOI <https://doi.org/10.1109/icassp43922.2022.9746886>.
- Minsu Kim, Jeong Hun Yeo, and Yong Man Ro. "Distinguishing Homophenes using Multi-head Visual-audio Memory for Lip Reading". \*AAAI 2022\*. DOI <https://doi.org/10.1609/aaai.v36i1.20003>.
- Se Jin Park, Minsu Kim, Joanna Hong, Jeongsoo Choi, and Yong Man Ro. "SyncTalkFace: Talking Face Generation with Precise Lip-syncing via Audio-Lip Memory". \*AAAI 2022\*. DOI <https://doi.org/10.1609/aaai.v36i2.20102>.
- Jung Uk Kim, Sungjune Park, and Yong Man Ro. "Towards Versatile Pedestrian Detector with Multisensory-Matching and Multispectral Recalling Memory". \*AAAI 2022\*. DOI <https://doi.org/10.1609/aaai.v36i1.20001>.
- Youngjoon Yu, Hong Joo Lee, Hakmin Lee, and Yong Man RoHakmin Lee and Yong Man Ro. "Defending Person Detection Against Adversarial Patch Attack by using Universal Defensive Frame". \*IEEE Transactions on Image Processing, vol. 31, pp. 6976-6990, 2022.\*. DOI <https://doi.org/10.1109/tip.2022.3217375>.
- Hyung-Il Kim, Kimin Yun, and Yong Man Ro. "Face Shape-Guided Deep Feature Alignment for Face Recognition Robust to Face Misalignment". \*IEEE Transactions on Biometrics, Behavior, and Identity Science, vol. 4, no. 4, pp. 556-569, 2022.\*. DOI <https://doi.org/10.1109/tbiom.2022.3213845>.
- Wissam J. Baddar, Sangmin Lee, and Yong Man Ro. "On-the-Fly Facial Expression Prediction Using LSTM Encoded Appearance-Suppressed Dynamics". \*IEEE Transactions on Affective Computing, vol. 13, no. 1, pp. 159-174, 2022.\*. DOI <https://doi.org/10.1109/taffc.2019.2957465>.[^onfly]
- Junho Kim, Seongyeop Kim, Seong Tae Kim, and Yong Man Ro. "Robust Perturbation for Visual Explanation:Cross-checking Mask Optimization to Avoid Class Distortion". \*IEEE Transactions on Image Processing, vol. 31, pp. 301-313, 2022.\*.

**2021**

- Minsu Kim, Joanna Hong, and Yong Man Ro. "Lip to Speech Synthesis with Visual Context Attentional GAN". \*NeurIPS 2021\*.
- Junho Kim\*, Byung-Kwan Lee\*, and Yong Man Ro (\*: equally contributed). "Distilling Robust and Non-Robust Features in Adversarial Examples by Information Bottleneck". \*NeurIPS 2021\*.
- Minsu Kim\*, Joanna Hong\*, Se Jin Park, and Yong Man Ro (\*: equally contributed). "Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video". \*ICCV 2021\*. DOI <https://doi.org/10.1109/iccv48922.2021.00036>.
- Jung Uk Kim\*, Sungjune Park\*, and Yong Man Ro (\*: equally contributed). "Robust Small-scale Pedestrian Detection with Cued Recall via Memory Learning". \*ICCV 2021\*. DOI <https://doi.org/10.1109/iccv48922.2021.00304>.
- Joanna Hong, Minsu Kim, Se Jin Park, Yong Man Ro. "Speech Reconstruction with Reminiscent Sound via Visual Voice Memory". \*IEEE Transactions on Audio Speech and Language Processing, vol. 29, pp. 3654-3667, 2021.\*. DOI <https://doi.org/10.1109/taslp.2021.3126925>.

## 수상과 선정

연구실 첫 화면의 2026년 선정 소식과 교수 소개의 2022년·2024년 수상 표기다. 연도만 적힌 항목의 연도는 누리집 표기이며 구체적인 날짜는 게시되어 있지 않다.[^home][^prof]

- 2026-03-19 · Jeong Hun Yeo가 2026 Jang Young Sil Fellow Program (Excellence Track)에 선정됐다.
- 2024 · Outstanding Paper Award in ACL
- 2022 · 1st Place Winner of Ad-hoc Video Search Competition, Video Browser Showdown
- 2022 · Top Research Achievement Award in KAIST

## 소식

연구실 첫 화면이 날짜와 함께 전하는 논문 채택·게재 승인 소식이다.[^home]

- 2026-08-22 · Jeong Hun Yeo의 「Diffusion Large Language Models for Visual Speech Recognition」이 EMNLP 2026에 채택됐다.
- 2026-08-22 · Youngchae Chee와 Hosu Lee의 「PRISM: Predictive Recomposition via Semantic Latent Decomposition for View-invariant Video Representation Learning」이 EMNLP 2026에 채택됐다.
- 2026-08-22 · Juwan Chung의 「From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs」가 EMNLP 2026에 채택됐다.
- 2026-08-22 · Jeong Hun Yeo의 「Decoding Strategies for Diffusion-Based ASR: A Systematic Evaluation of Confidence-Based Thresholding」이 EMNLP 2026에 채택됐다.
- 2026-08-22 · Bella Godiva의 「Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models」가 EMNLP 2026에 채택됐다.
- 2026-08-11 · Minho Park의 「PhysCache: Accelerating Physics-Sensitive Image Editing with Risk-Aware Caching」가 BMVC 2026에 채택됐다.
- 2026-06-23 · Yeonju Kim의 「Empathetic Response in Audio-Visual Conversations Using Emotion Preference Optimization and MambaCompressor」가 IEEE Transactions on Affective Computing의 게재 승인을 받았다.
- 2026-06-21 · Junho Kim, Hosu Lee, Minsu Kim의 「STRIDE: When to Speak Meets Sequence Denoising for Streaming Video Understanding」이 ECCV 2026에 채택됐다.
- 2026-06-21 · Byung-Kwan Lee의 「GenRecal: Generation after Recalibration from Large to Small Vision-Language Models」가 ECCV 2026에 채택됐다.
- 2026-06-18 · Sangyun Chung과 Youngjoon Yu의 「Enhanced Vision-Language Models for Diverse Sensor Understanding: Cost-Efficient Optimization and Benchmarking」가 IEEE Transactions on Image Processing의 게재 승인을 받았다.
- 2026-05-25 · Jeong Hun Yeo와 Sangyun Chung의 「GCAgent: Long-Video Understanding via Schematic and Narrative Episodic Memory」가 IEEE Transactions on Multimedia의 게재 승인을 받았다.
- 2026-02-24 · Sangyun Chung의 「MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models」가 CVPR 2026에 채택됐다.
- 2026-02-24 · Byung-Kwan Lee와 Youngchae Chee의 「Recursive Think-Answer Process for LLMs and VLMs」가 CVPR 2026 Findings에 채택됐다.
- 2026-02-24 · Hosu Lee와 Junho Kim의 「ReFoCUS: Reinforcement-guided Frame Optimization for Contextual Understanding」이 CVPR 2026 Findings에 채택됐다.
- 2026-01-18 · Beomchan Park와 Seongho Kim의 「Robust Grounding with MLLMs against Occlusion and Small Objects via Language-Guided Semantic Cues」가 ICASSP 2026에 채택됐다.

## 연락과 위치

- 교수 업무 이메일: ymro@kaist.ac.kr.[^dept]
- 학부 교수 소개의 연락처 표기: 3494.[^dept]
- 교수 위치: IT융합빌딩 N1, 414호.[^dept]
- 연구실 주소: 대전광역시 유성구 구성동 KAIST, Kim Beang-Ho & Kim Sam-Youl ITC Building (N1), 418호.[^contact]
- 연구실 전화: +82-42-350-5494, 8094.[^contact]

## 각주
[^overview]: IVYLab & IVLLab, Lab Overview. <https://www.ivylab.kaist.ac.kr/research_1/lab-overview> 관측 2026-11-09.
[^fields]: IVYLab & IVLLab, Research Fields. <https://www.ivylab.kaist.ac.kr/research_1/research-fields> 관측 2026-11-09.
[^prof]: IVYLab & IVLLab, Professor. <https://www.ivylab.kaist.ac.kr/people/professor> 관측 2026-11-09.
[^dept]: KAIST 전기및전자공학부, 노용만 교수 소개. <https://ee.kaist.ac.kr/professor/12170/> 관측 2026-11-09.
[^members]: IVYLab & IVLLab, Members. <https://www.ivylab.kaist.ac.kr/people/members> 관측 2026-11-09.
[^alumni]: IVYLab & IVLLab, Alumni. <https://www.ivylab.kaist.ac.kr/people/alumni> 관측 2026-11-09.
[^conference]: IVYLab & IVLLab, International Conference. <https://www.ivylab.kaist.ac.kr/publications_1/international-conference> 관측 2026-11-09.
[^conf2]: IVYLab & IVLLab, International Conference 2. <https://www.ivylab.kaist.ac.kr/publications_1/international-conference/international-conference_2> 관측 2026-11-09.
[^journal]: IVYLab & IVLLab, International Journal. <https://www.ivylab.kaist.ac.kr/publications_1/international-journal> 관측 2026-11-09.
[^home]: IVYLab & IVLLab, 첫 화면 News. <https://www.ivylab.kaist.ac.kr/ivylab-ivllab> 관측 2026-11-09.
[^contact]: IVYLab & IVLLab, Contact. <https://www.ivylab.kaist.ac.kr/contact> 관측 2026-11-09.
[^oa]: OpenAlex, 노용만의 2021–2026년 논문 서지·초록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p1]: H. Lee 외, Y. M. Ro, CVPR 2026 Findings (2026). <https://doi.org/10.1109/cvprf71909.2026.00796> 초록 기준(OpenAlex 등록 초록). 연구실 기재 발표처 CVPR 2026 Findings <https://www.ivylab.kaist.ac.kr/publications_1/international-conference>. 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p2]: J. H. Yeo 외, Y. M. Ro, IEEE/CVF International Conference on Computer Vision (ICCV) (2025). <https://doi.org/10.1109/iccv51701.2025.00630> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p3]: J. Choi, S. J. Park, M. Kim, Y. M. Ro, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2024). <https://doi.org/10.1109/cvpr52733.2024.02580> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p4]: S. J. Park 외, Y. M. Ro, Proceedings of the AAAI Conference on Artificial Intelligence (2022). <https://doi.org/10.1609/aaai.v36i2.20102> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p5]: B.-K. Lee 외, Y. M. Ro, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2025). <https://doi.org/10.1109/cvpr52734.2025.02751> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p6]: J. Kim, B.-K. Lee, Y. M. Ro, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2023). <https://doi.org/10.1109/cvpr52729.2023.01184> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p7]: T. Kim 외, Y. M. Ro, IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2024). <https://doi.org/10.1109/cvpr52733.2024.02529> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^p8]: Y. K. Won 외, D. H. Lim, Frontiers in Medicine (2023). <https://doi.org/10.3389/fmed.2023.1162124> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5038798134,publication_year:2021-2026> 관측 2026-11-09.
[^onfly]: W. J. Baddar, S. Lee, Y. M. Ro, IEEE Transactions on Affective Computing 13(1), 159–174 (인쇄판 2022-01-01). <https://doi.org/10.1109/TAFFC.2019.2957465> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/taffc.2019.2957465> 날짜 서지 <https://api.crossref.org/works/10.1109/TAFFC.2019.2957465> 관측 2026-11-09.

# Bio Imaging, Signal Processing, and Machine Learning Lab (BISPL)

**KAIST 김재철AI대학원 · 예종철 교수**

- 분야: 생성 모형의 원리와 학습, 영상 생성·복원, 의료 영상 재구성과 영상·언어 결합
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 생성 인공지능[^home][^p1][^p4], 컴퓨터 비전[^home][^p2][^p5], 의료 AI[^home][^p8], 의료 영상 기기·재구성[^home][^p6]
- 홈페이지: <https://bispl-website.github.io/>
- 근거와 출처: [BISPL 근거 페이지](bispl-sources.md)

> 영상과 의료 자료에서 출발해 새로운 학습 원리와 계산 방법을 만들고, 이를 영상 생성·복원과 의료 자료 해석에 연결하는 연구실이다.[^home]

## 무엇을 연구하나

BISPL은 예종철 교수가 이끄는 연구실로, 영상·신호 처리와 기계학습을 기반으로 새로운 인공지능(Artificial Intelligence, AI)의 원리와 알고리즘을 연구한다. 신호 처리는 관측한 값에서 필요한 정보를 얻거나 원치 않는 성분을 줄이는 계산이고, 기계학습은 자료에서 규칙을 배워 새 자료를 처리하는 방법이다. 연구실은 실제 문제로부터 수학적 원리와 학습 방법을 만들고, 그 원리를 실제 응용으로 돌려보내는 연구 방향을 밝힌다.[^home]

한 축은 생성 모형(자료의 규칙성을 배워 새로운 자료를 만드는 계산 모형)의 원리다. 확산 모형은 자료에 잡음(원하는 정보에 섞인 불규칙한 성분)을 더하는 과정과 그 반대 과정을 학습해 자료를 생성하는 모형이고, 흐름 모형은 단순한 자료 분포(가능한 값에 어떤 확률이 배정되는지 나타내는 관계)를 원하는 분포로 연속적으로 바꾸는 모형이다. 연구실은 이들 모형의 이론과 강화학습(시행착오에서 얻는 보상을 기준으로 행동 방법을 배우는 학습)을 주요 연구 갈래로 둔다. 보상을 이용한 생성 모형 학습을 통합된 수학적 관점에서 설명하고, 생성 경로의 굽은 정도를 줄여 계산 부담을 낮추는 방법을 연구했다.[^home][^p1][^p4]

다른 축은 역문제(관측 결과에서 그 결과를 만든 원래 상태를 추정하는 문제)다. 손상된 영상에서 원래 영상을 복원하거나, 일부만 측정한 자료에서 영상을 만드는 문제가 여기에 속한다. 학습한 생성 모형과 실제 측정값이 서로 맞도록 계산을 결합하며, 잡음이 있는 관측과 시간에 따라 이어지는 동영상을 다루는 새 방법을 개발한다.[^home][^p2][^p3][^p5]

의료 분야에서는 영상과 글을 함께 다루는 방법을 연구한다. 의료 영상의 측정값에서 영상을 재구성하는 방법, 현미경 영상의 해상도(서로 가까운 구조를 구별하는 능력)를 높이는 방법, 흉부 영상과 설명문을 함께 이해하고 생성하는 방법을 다룬다. 의료 문제를 계산 방법의 개발과 연결하는 연구다.[^dept][^p6][^p7][^p8]

## 주요 연구 주제

### 생성 모형의 학습 원리와 보상에 따른 조정

보상은 생성 결과가 원하는 기준을 얼마나 충족하는지 나타내는 값이다. 대표 논문 1은 이미 학습한 확산·흐름 모형을 보상이 높은 결과 쪽으로 조정하는 여러 방법을 하나의 틀에서 설명한다. 대표 논문 4는 생성 과정의 경로가 굽는 정도와 수치 계산의 오차를 연결하고, 경로를 학습해 생성에 필요한 계산을 줄인다.[^p1][^p4] 이는 생성 모형이 작동하는 이유를 이해하고 새로운 이론과 알고리즘을 만들겠다는 연구실의 방향과 이어진다.[^home]

### 관측값을 반영하는 영상 복원

영상 복원은 관측 자료에서 손실·잡음·흐림의 영향을 줄여 원래 영상 정보를 추정하는 일이다. 대표 논문 5는 잡음이 있는 선형·비선형 관측에서 생성 모형으로 가능한 원래 영상을 구하는 방법을 제안한다. 대표 논문 3은 연속적인 흐름 모형에도 관측 정보와 잡음을 결합하는 풀이를 만든다. 대표 논문 2는 동영상을 순차적으로 복원해 첫 결과까지의 대기와 반복 계산을 줄이는 방법을 제안한다.[^p5][^p3][^p2]

### 의료·현미경 영상의 재구성과 개선

자기공명영상(Magnetic Resonance Imaging, MRI, 자기장과 전파에 반응하는 원자핵의 신호로 몸속을 영상화하는 방법)을 다룬다. 대표 논문 6은 일부 측정값으로부터 영상을 만드는 과정에 학습한 영상 규칙성과 측정값의 일관성을 함께 반영한다.[^p6] 형광 현미경은 물질이 빛을 흡수한 뒤 내는 빛을 이용해 구조를 관찰하는 장치다. 대표 논문 7은 짝지은 고해상도 정답 영상 없이 입체 현미경 영상의 방향별 해상도 차이를 줄이고 영상의 세부 구조를 복원하는 방법을 제안한다.[^p7]

### 영상과 언어를 함께 다루는 의료 모형

대형 언어 모델(Large Language Model, LLM)은 많은 글을 학습해 글을 이해하고 생성하는 대규모 계산 모형이다. 대표 논문 8은 글로만 학습한 언어 모형이 흉부 X선 영상도 이해하고 생성하도록 가르친다. 영상에서 설명문을 만들거나 글에서 영상을 만드는 여러 과제를 함께 학습한다. 이 논문은 시각 정보와 언어 정보가 모형 안에서 함께 작동하도록 하는 학습 방법을 제안한다.[^p8]

## 대표 논문

예종철 교수가 저자로 참여한 최근 논문에서 생성 모형의 이론·학습, 영상 역문제, 의료 영상, 영상·언어 결합을 고르게 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 연도와 발표처는 연구실의 게시 구역을 따르며, 각주는 설명에 쓴 판본을 밝힌다.[^pubs]

| 번호 | 연도 | 논문과 발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Reward Score Matching: Unifying Reward-based Fine-tuning for Flow and Diffusion Models](https://doi.org/10.48550/arXiv.2604.17415) · NeurIPS 2026(채택) | 1저자 Jeongjae Lee, 마지막 저자 Jong Chul Ye | 생성 모형이 원하는 기준을 충족하도록 다시 학습시키는 여러 방법을 하나의 틀로 설명하고, 그 관점에서 간단한 재설계 방법을 제안한다.[^p1] |
| 2 | 2026 | [Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models](https://doi.org/10.48550/arXiv.2605.20624) · NeurIPS 2026(채택) | 1저자 Taesung Kwon, 마지막 저자 Jong Chul Ye | 동영상 전체를 한꺼번에 처리하는 대신 순차적으로 복원하고 초기값에 관측 정보를 반영해, 첫 결과까지의 대기와 반복 계산을 줄인다.[^p2] |
| 3 | 2025 | [FlowDPS: Flow-Driven Posterior Sampling for Inverse Problems](https://doi.org/10.1109/iccv51701.2025.01146) · ICCV 2025 | 1저자 Jeongsol Kim, 마지막 저자 Jong Chul Ye | 흐름 모형의 계산을 원래 영상 추정과 잡음 추정으로 나누고 각각에 관측 정보와 잡음을 반영해, 추가 학습 없이 역문제를 푼다.[^p3] |
| 4 | 2023 | [Minimizing Trajectory Curvature of ODE-based Generative Models](https://doi.org/10.48550/arxiv.2301.12003) · ICML 2023 | 1저자 Sangyun Lee, 마지막 저자 Jong Chul Ye | 생성 과정이 따르는 경로의 굽은 정도를 학습으로 줄여, 생성 품질을 유지하면서 결과를 만드는 계산 부담을 낮춘다.[^p4] |
| 5 | 2023 | [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://doi.org/10.48550/arxiv.2209.14687) · ICLR 2023 | 1저자 Hyungjin Chung, 마지막 저자 Jong Chul Ye | 잡음이 있는 선형·비선형 관측에도 확산 모형을 쓸 수 있도록 가능한 원래 영상을 뽑는 계산을 바꾼다.[^p5] |
| 6 | 2022 | [Score-based diffusion models for accelerated MRI](https://doi.org/10.1016/j.media.2022.102479) · Medical Image Analysis | 1저자 Hyungjin Chung, 마지막 저자 Jong Chul Ye | 학습한 영상 규칙성과 실제 측정값을 번갈아 반영해, 일부만 측정한 자기공명 자료에서 영상을 재구성한다. 생성 방식의 특성을 이용해 결과의 불확실성도 다룬다.[^p6] |
| 7 | 2022 | [Deep learning enables reference-free isotropic super-resolution for volumetric fluorescence microscopy](https://doi.org/10.1038/s41467-022-30949-6) · Nature Communications | 1저자 Hyoungjun Park, 마지막 저자 Jong Chul Ye | 입체 현미경 영상의 서로 다른 방향 평면들을 짝 없이 학습해, 별도의 고해상도 정답 없이 방향에 따른 해상도 차이를 줄인다.[^p7] |
| 8 | 2024 | [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://doi.org/10.48550/arXiv.2305.11490) · ICLR 2024 | 1저자 Suhyeon Lee, 마지막 저자 Jong Chul Ye | 글 모델에 흉부 영상 이해와 영상 생성 과제를 함께 가르쳐, 영상에 관한 질문에 답하고 글이나 영상으로 응답하게 한다.[^p8] |

## 교수와 전문 분야

예종철 교수는 2004년 KAIST에 부임했으며 현재 김재철AI대학원 교수다.[^cv][^dept] 연구실 교수 소개는 생체·의료 영상의 신호 처리와 기계학습에 대한 기여를 IEEE Fellow 선정 문구로 소개한다.[^prof] 최근 대표 논문을 종합하면 전문 분야는 생성 모형의 수학적 학습 원리, 관측값을 반영하는 영상 복원, 의료 영상 재구성, 영상과 언어의 결합으로 볼 수 있다.[^p1][^p3][^p4][^p6][^p8]

## 응용 분야

생성 모형의 학습과 조정은 생성 결과를 원하는 기준에 맞추는 데 쓰이고, 역문제 풀이는 손상된 사진·동영상의 복원에 쓰인다. 의료 분야에서는 자기공명 영상 재구성, 현미경 영상 개선, 흉부 영상의 이해와 생성이 응용 대상이다.[^p1][^p2][^p5][^p6][^p7][^p8]

## 구성원

연구실 People에 게시된 박사후연구원 4명, 박사과정 21명, 석사과정 17명이다. 학력 칸의 BS는 학사, MS는 석사, PhD는 박사 표기다. 「대표 논문 참여」는 대표 논문의 전체 저자와 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 학력 (게시 표기) | 대표 논문 참여 |
| --- | --- | --- | --- |
| Nayeon Kim | 박사후연구원 | MS/PhD. Biotechnology, Yonsei Univ. |  |
| Jeongsol Kim | 박사후연구원 | PhD. KAIST (2026.2) | 1, 3, 5 |
| Geon Yeong Park | 박사후연구원 | PhD. KAIST (2026.2) |  |
| Taesung Kwon | 박사후연구원 | PhD. KAIST (2026.2) | 2 |
| Anna Povolná | 박사과정 | MS: Czech Technical University in Prague |  |
| Beomsu Kim | 박사과정 | MS. BBE, KAIST | 4 |
| Choonghan Kim | 박사과정 | MS. AI, POSTECH |  |
| Hyunmin Hwang | 박사과정 | MS. KAIST AI |  |
| Jaa-Yeon Lee | 박사과정 | MS. Bio/Brain, KAIST |  |
| Duy Khanh Pham | 박사과정 | MS. KAIST |  |
| Jinho Chang | 박사과정 | MS. KAIST AI | 1, 8 |
| Chang Sun Lee | 박사과정 | MS. AI, KAIST |  |
| Hangeol Chang | 박사과정 | MS. AI, KAIST |  |
| Suhyeon Lee | 박사과정 | MS. AI, KAIST | 8 |
| Jang Ho Park | 박사과정 | MS. AI, KAIST |  |
| Jaemin Kim | 박사과정 | MS. AI, KAIST |  |
| Dohun Lee | 박사과정 | MS. AI, KAIST |  |
| Hongeun Kim | 박사과정 | MS. AI, KAIST |  |
| ByungHee Cha | 박사과정 | MS. AI, KAIST |  |
| Yeobin Hong | 박사과정 | MS. AI, KAIST |  |
| Seonghyun Jin | 박사과정 | BS. CSE / BA. Econ., SNU |  |
| Jongmin Kim | 박사과정 | MS. AI, KAIST |  |
| Youngjun Jun | 박사과정 | MS. AI, Yonsei Univ. |  |
| Hyeonjae Kim | 박사과정 | MS. CSE, Hanyang Univ. |  |
| Chanyu Moon | 박사과정 | MS. EECS, DGIST |  |
| Byungjun Kim | 석사과정 | MS. AI, KAIST |  |
| Jonghyun Park | 석사과정 | BS. SNU | 2 |
| Hun Chang | 석사과정 | BS. UCLA |  |
| Sunwoo Park | 석사과정 | BS. EE, Hanyang |  |
| Chunsan Hong | 석사과정 | BS. EE, KAIST |  |
| Jeongjae Lee | 석사과정 | BS. ECE, SNU | 1 |
| Jaeyun Shin | 석사과정 | BS. EEE, Sungkyunkwan Univ. |  |
| Taehoon Lee | 석사과정 | BS. SNU |  |
| Geonyoung Lee | 석사과정 | BS. Biomedical Engineering/Math, Korea Univ. |  |
| Jeongchan Kim | 석사과정 | BS. BME/EE, Korea Univ. |  |
| Yoojin Oh | 석사과정 | BS. AI, Ewha Womans Univ. |  |
| Yunkyung Ko | 석사과정 | BS. Statistics, Korea Univ. |  |
| Youngmin Kim | 석사과정 | BS. CS, Korea Univ. |  |
| Chaebeen Bang | 석사과정 | BS. AI, Kyunghee Univ. |  |
| Mingeon Kim | 석사과정 | BS. MAS/EE, KAIST |  |
| Yeonwoo Seo | 석사과정 | BS. CSE, Korea Univ. |  |
| Shayan Baghayi Nejad | 석사과정 | BS. CSE, Sharif University of Technology, Iran. |  |

## 졸업생과 이전 구성원

연구실 Alumni의 Academia 20명, Further Study 11명, Industry 57명, Visiting Faculty 6명이다. 학위·과정과 기간, 진로는 연구실의 게시 표기를 따른다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyungjin Chung | PhD (2025. 2) | EverEx · Assistant Professor · Korea University |
| Yujin Oh | PhD (2024.2) | Harvard Univ. · Assistant Professor · Yonsei University |
| Kwanyoung Kim | PhD (2024.8) | Samsung Research · Assistant Professor · GIST · (Gwangju Institute of Science & Technology) |
| Soobin Um | PhD (2025.8) | Assistant Professor · Kookmin University |
| Boah Kim | PhD (2023.2) | NIH · Assistant Professor · Sungkyunkwan University |
| Kangjoo Lee | M.S. (2011.2) | McGuill Univ (PhD) · Assistant Professor · Florida International University (FIU) |
| Sangjoon Park, MD | Ph.D. (2023.2) | Assistant Professor · Yonsei University Medical School |
| Yoseob Han | Ph.D (2019. 6) | Los Alamos National Lab · --> Havard Univ. · Assistant Professor · Soongsil University, Korea |
| Kyong Hwan Jin | Ph.D. (2015.2) | EPFL --> DGIST · Associate Professor · Korea University |
| Minwoo Kim | M.S. (2009.2) | PhD (UIUC) · Assistant Professor · Pusan National University |
| Shujaat Khan | Ph.D. (2022) | Siemens Research USA · Assistant Professor · King Fahd University of Petroleum and Minerals (KFUPM), · Saudi Arabia |
| Paul Han | M.S. (2013.2) | Assistance Professor · Yale University Medical School |
| Sharad Gupta | Postdoc (2006-2007) | Professor · Indian Institute of Technology (IIT), Gandhinagar · India |
| Eunju Cha | PhD (2021.2) | Samsung SAIT · Assistant Professor · Sookmyung Women's University |
| Byung-Hoon Kim, MD | PhD (2021.2) | Clinical Assistant Professor · Yonsei Severance Hospital |
| Jaejun Yoo | Ph.D (2018.2) | Naver --> EPFL · Associate Professor · UNIST, Korea |
| Huisu Yoon | Ph.D. (2015.2) | Samsung Medicine · Associate Professor · Ulsan University |
| Okkyun Lee | Ph.D. (2014.2) | Johns Hopkins Univ. · Assistant Professor · DGIST |
| Kyungsang Kim | Ph.D. (2014.8) | Assistant Professor · Havard Medical School |
| Abdul Wahab | Research Professor (2016-2018) | Associate Professor · Sultan Qaboos University, Oman |
| Bryan Sangwoo Kim | MS (2026. 2) | PhD Student · Stanford Univ. CS Dept. USA |
| Chanyong Jung | PhD (2024.2) | Samsung Research · Univ. of Michigan |
| Dr. Chamlee Cho | Postdoc (2025-2026) | Postdoc · Samsung Medical Center |
| WonJun Kim | MS (2025.8) | PhD Student · EPFL |
| Uiyun Kim | MS (2024.2) | PhD Student, KAIST |
| Cristina Eunbee Cho, MD | MS (2026.2) | Medical Doctor |
| Hyelin Nam | MS (2025.2) | PhD Student · University of Michigan, Ann Arbor |
| Hyoungjun Park | Resaercher @ BISPL (2020-2022) | MS. Neuroscience, ETH Zurich · BS. Brain and Cognitive Science, MIT · Ph.D student at EMBL, Germany |
| Finn Wolfreys | M.S. (2012.2) | Univ. Oxford (PhD) · Postdoc Researcher, UCSF |
| Maryam Ghahremani | M.S. (2013. 8) | Ph.D. Student · The University of Western Ontario, Canada |
| Deborah Martin | MS (2020. 6) | PhD Student, DGIST · BS. Computer Science |
| Gwanghyun Kim | MS (2022.2) | NVidia, USA |
| Gyutaek Oh | PhD (2025.2) | Samsung Research |
| Junyoung Kim | PhD (2025.2) | Samsung Co. |
| Caruzzo Cedric Patrick Jean-Pierre | MS (2025.2) | Lunit Co. |
| Heemin Jung | MS (2025.2) |  |
| Gihyun Kwon | PhD (2024.8) | Krafton Inc. --> Amazon, Australia |
| Sangmin Lee | PhD (2024.8) | Samsung Mobile |
| Jaemin Kim | M.S (2024.8) | Wrtn AI |
| Sehui Kim | BS. BE Korea University | Naver |
| Joonyoung Song | Ph.D. (2022.8) | Samsung Electronics. |
| Junghyun Lee | MS (2020. 6) | Samsung Electronics. |
| Hyeonho Jeong | MS (2025. 8) | Adobe Research, UK |
| Ara Seo | MS (2025. 8) |  |
| Serin Yang | PhD (2025.2) | Samsung Co. |
| Naeun Ko | MS (2025.2) | Naver Corporation |
| Inhwa Han | PhD (2025.2) |  |
| Byeongsu Sim | PhD (2024. 8) | Samsung Research |
| Jaeyoung Huh | PhD (2024.2) | Siemens Corporate Research · Princeton, USA |
| Hyokyoung Bae | M.S.; (2023.2) | Samsung Research |
| Dohoon Ryu | M.S. (2023.2) | SK Telecom |
| Woon Kyung Sung | MS (2021.2) | Voroni.io |
| Dongwook Lee | Ph.D (2019. 6) | Samsung Electronics |
| Hyunjong Kim | MS (2021.2) | DRTECH Co. |
| Joo Won Lim | M.S. (2016.2) | Ph.D. (2020) EPFL · Microsoft Research Cambridge · UK |
| Jawook Gu | PhD (2021.2) | Samsung Research· Soombit AI |
| Sungjun Lim |  | Samsung Research |
| Juyoung Lee | Ph.D (2019. 6) | Samsung Inst. of Technology (SAIT) |
| Yeohun Yoon | M.S. (2018.2) | AI Venture Company |
| Heejoon Koo | Research Intern | AI Venture |
| Joonhyung Lee | MS (2020. 6) | Vuno Co. · Naver |
| Eunhee Kang | Ph.D (2019. 6) | Samsung Inst. of Technology (SAIT) |
| Hyoryang Kim | M.S. (2018.2) | Lieutenant Commander · Korean Army |
| Woong Bae | M.S. (2017.8) | Kakao Brain · CEO at Soombit AI |
| Yeong Sik Kim | M.S. (2017.2) | AI Venture Compnay |
| Jaehyun Nam | M.S. (2013.2) | AI venture company |
| Yohan Lee | M.S. (2013.2) | AI venture company |
| Jun Hong Min | Ph.D. (2016.5) | Samsung Electronics Co. |
| Minji Lee | Ph.D. (2015.8) |  |
| Arshi Khalid | Ph.D. (2015.2) |  |
| Jeonghyeon Lee | M.S. (2013.2) | Korea Hydro & Nuclear Power Co. |
| Jongmin Kim | Post Doc. (2013.2) | Professor at Korea Science Academy of KAIST |
| Jinwook Jung | Ph.D. (2012.2) | Samsung Electronics Co. · Health & Medical Equpment (HME) |
| Sungho Tak | Ph.D. (2011.7) | Senior Researcher · KBSI |
| Hong Jung | Ph.D. (2011.2) | CTO at HDX-Willmed Co. |
| Younghan Oh | M.S. (2011.2) |  |
| Jaeheung Yoo | M.S. (2008.2) | Medical Doctor · Samsung Medical Center · Nuclear Medicine |
| Jinhee Kim | Undergraduate trainee | Medical Doctor · Seoul National University Medical School |
| Jaeyun Cho | Undergraduate trainee | Ph.D. at Dept. of Univ. California, Berkeley · Now patent laywer at Boston |
| Daria | Undergraduate exchange student |  |
| Jiyoung Choi | Ph.D. (2012.2) | SK Telecom |
| Sehi Lee | M.S. (2012.2) | M.D. Student · Catholic University of Medicine |
| Jaeduck Jang | Ph.D. (2011.7) | Samsung Advanced Institute of Technology |
| Hua Li | M.S. (2011.7) | Senior Scientist, Bio-Rad Laboratories · CA, USA |
| Kwangeun Jang | M.S. (2009.2) | Ph.D student · Stanford University |
| Suyeon Lee | M.S. (2009.2) | MD Student · Yonsei University School of Medicine |
| Liu yu | M.S. (2007.2) | MBA from Duke University · Now working for Lenova, USA |
| Hyunjoon Ahn | M.S. (2010.2) | Ph.D (SNU) · Vuno Co. |
| Eun Sun Lee, MD/Ph.D | Visiting Professor · (2021.9-2022.8) | Associate Professor · Department of Radiology · Chungang University Hospital |
| Hyungjung Park, MD, PhD | Visiting Professor · (2023.1-2024.1) | Dept. of Radiology · School of Medicine · Chung Ang University |
| Woo Hee Choi , MD, Ph.D | Visiting Professor · (2023.9-2024.8) | Division of Nuclear Medicine, Department of Radiology, · St. Vincent’s Hospital · College of Medicine, · The Catholic University of Korea |
| Jeong Eun Lee, MD/Ph.D | Visiting Professor · (2022.3-2023.2) | Associate Professor · Department of Radiology · Chungnam National University Hospital |
| Tae Hoon Roh , MD, PhD | Visiting Professor · (2024.3-2024.8) | Department of Neurosurgery, · Ajou University School of Medicine |
| Cheong-Il Shin , MD, PhD | Visiting Professor · (2023.9-2024.8) | Department of Radiology · College of Medicine · Seoul National University |

## 최근 논문 목록 (2021–2026)

연구실 Publications에 게시된 KAIST 재직 시기의 논문과 저서 144건이다. 제목·저자·발표처는 연구실의 표기이며, 연도는 게시 구역을 따른다.[^pubs][^cv] Medical Image Analysis의 「in press」는 게재 승인으로, NeurIPS 2026의 여섯 항목은 「채택」으로 표시했다.[^pubs][^news]

**2026**

- Hyungjin Chung, Dohun Lee, Zihui Wu, Byung-Hoon Kim, Katherine L. Bouman, and Jong Chul Ye. "ContextMRI: Enhancing Compressed Sensing MRI through Metadata Conditioning". Medical Image Analysis (in press) , 2026. DOI <https://doi.org/10.1016/j.media.2026.104353> (게재 승인)
- Taesung Kwon, Jonghyun Park, Hyungjin Chung, and Jong Chul Ye. "Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. (채택)
- Jeongsol Kim, Jong Chul Ye , Yufei Wang, and Jian Wang. "Accelerated Image Editing via Consistency-Aware Source Token Pruning". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. (채택)
- Byungjun Kim, Soobin Um, and Jong Chul Ye. "MotionCFG: Boosting Motion Dynamics via Semantic Motion Sharpening". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. (채택)
- Jeongjae Lee, Jinho Chang, Jeongsol Kim, and Jong Chul Ye. "Reward Score Matching: Unifying Reward-based Fine-tuning for Flow and Diffusion Models". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. DOI <https://doi.org/10.48550/arXiv.2604.17415> (채택)
- Seonghyun Jin, Youngmin Kim, Sunwoo Park, and Jong Chul Ye. "CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. (채택)
- Jaewoo Lee, Hyeongyu Kang, Dohyun Kim, Kyuil Sim, Woocheol Shin, Minsu Kim, Taeyoung Yun, Jeongjae Lee, Sanghyeok Choi, Tabitha Edith Lee, Jong Chul Ye , and Jinkyoo Park. "Aligning Few-Step Generative Model via Amortizing Sample-Based Variational Inference". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2026. (채택)
- Choonghan Kim, Hyunmin Hwang, Hangeol Chang, Jaemin Kim, Jinse Park, Jae-Sung Lim, and Jong Chul Ye. "Dementia-R1: Reinforced Pretraining and Reasoning from Unstructured Clinical Notes for Real-World Dementia Prognosis". In Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing , Oct 2026.
- Jaemin Kim and Jong Chul Ye. "Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models". In Findings of the Association for Computational Linguistics: EMNLP 2026 , Oct 2026.
- Chaeyoung Huh, Hyunmin Hwang, Jung Hwan Shin, Sungyang Jo, Jinse Park, and Jong Chul Ye. "PACE-RAG: Patient-Aware Contextual and Evidence-Constrained RAG for Clinical Drug Recommendation". In Findings of the Association for Computational Linguistics: EMNLP 2026 , Oct 2026.
- Seonghyun Jin and Jong Chul Ye. "FILT3R: Latent State Adaptive Kalman Filter for Streaming 3D Reconstruction". In The 19th European Conference on Computer Vision (ECCV) , 2026.
- Yeobin Hong, Suhyeon Lee, Hyungjin Chung, and Jong Chul Ye. "InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem". In The 19th European Conference on Computer Vision (ECCV) , 2026. DOI <https://doi.org/10.1007/978-3-032-37419-6_5>
- Bryan Sangwoo Kim, Jonghyun Park, and Jong Chul Ye. "Tiled Prompts: Overcoming Prompt Misguidance in Image and Video Super-Resolution". In The 19th European Conference on Computer Vision (ECCV) , 2026. DOI <https://doi.org/10.1007/978-3-032-37255-0_2>
- Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye , Duygu Ceylan, and Hyeonho Jeong. "Memory-V2V: Memory-Augmented Video-to-Video Diffusion for Consistent Multi-Turn Editing". In The 19th European Conference on Computer Vision (ECCV) , 2026. DOI <https://doi.org/10.1007/978-3-032-37324-3_5>
- Geon Yeong Park, Roman Shapovalov, Rakesh Ranjan, Jong Chul Ye , Andrea Vedaldi, and Thu Nguyen-Phuoc. "3D-ReGen: A Unified 3D Geometry Regeneration Framework". In The 19th European Conference on Computer Vision (ECCV) , 2026.
- Chunsan Hong, Sanghyun Lee, and Jong Chul Ye. "Unifying Masked Diffusion Models with Various Generation Orders and Beyond". In International Conference on Machine Learning ( ICML ) , 2026 spotlight, top 2.2%.
- Jaemin Kim, Hangeol Chang, Hyunmin Hwang, Choonghan Kim, and Jong Chul Ye. "Universal Reasoner: A Single, Composable Plug-and-Play Reasoner for Frozen LLMs". In International Conference on Machine Learning ( ICML ) , 2026.
- Jaa-Yeon Lee, Yeobin Hong, Taesung Kwon, and Jong Chul Ye. "Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models". In International Conference on Machine Learning ( ICML ) , 2026 spotlight, top 2.2%.
- Beomsu Kim, ByungHee Cha, and Jong Chul Ye. "Align Your Trajectory Tangent: Training Better Consistency Models via Manifold-Aligned Tangents". In International Conference on Machine Learning ( ICML ) , 2026.
- Jinho Chang, Changsun Lee, Hyungjin Chung, and Jong Chul Ye. "ContrastiveCFG: Guiding Diffusion Sampling by Contrasting Positive and Negative Concepts". In International Conference on Machine Learning ( ICML ) , 2026.
- Suhyeon Lee and Jong Chul Ye. "PromptLoop: Plug-and-Play Prompt Refinement via Latent Feedback for Diffusion Model Alignment". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2026.
- Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung, and Jong Chul Ye. "ReDirector: Creating Any-Length Video Retakes with Rotary Camera Encoding". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2026.
- Taesung Kwon, Lorenzo Bianchi, Lennart Wittke, Felix Watine, Fabio Carrara, Jong Chul Ye , Romann M. Weber, and Vinicius C. Azevedo. "Reviving ConvNeXt for Efficient Convolutional Diffusion Models". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2026.
- Jangho Park, Taesung Kwon, and Jong Chul Ye. "Zero4D: Training-Free 4D Video Generation From Single Video Using Off-the-Shelf Video Diffusion Models". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Findings , 2026.
- Jinho Chang, Jaemin Kim, and Jong Chul Ye. "Training-Free Reward-Guided Image Editing via Trajectory Optimal Control". In Proceedings of the Fourteenth International Conference on Learning Representations (ICLR) , 2026.
- Chunsan Hong, Seonho An, Min-Soo Kim, and Jong Chul Ye. "Improving Discrete Diffusion Unmasking Policies Beyond Explicit Reference Policies". In Proceedings of the Fourteenth International Conference on Learning Representations (ICLR) , 2026.
- Jeongjae Lee and Jong Chul Ye. "PCPO: Proportionate Credit Policy Optimization for Preference Alignment of Image Generation Models". In Proceedings of the Fourteenth International Conference on Learning Representations (ICLR) , 2026.
- Jeongsol Kim, Yeobin Hong, Jonghyun Park, and Jong Chul Ye. "FlowAlign: Trajectory-Regularized, Inversion-Free Flow-based Image Editing". In Proceedings of the Fourteenth International Conference on Learning Representations (ICLR) , 2026.
- Byungjun Kim, Soobin Um, and Jong Chul Ye. "Diverse Text-to-Image Generation via Contrastive Noise Optimization". In Proceedings of the Fourteenth International Conference on Learning Representations (ICLR) , 2026.
- Geon Yeong Park, Inhwa Han, Serin Yang, Yeobin Hong, Seongmin Jeong, Heechan Jeon, Myeongjin Goh, Sung Yi, Jin Nam, and Jong Chul Ye. "DreamMakeup: Face Makeup Customization using Latent Diffusion Models". In The IEEE/CVF Winter Conference on Applications of Computer Vision , 2026.
- C. Lee, S. Park, C. I. Shin, W. H. Choi, H. J. Park, J. E. Lee, and Jong Chul Ye. "Read like a radiologist: Efficient vision-language model for 3d medical imaging interpretation". Medical Image Analysis , 2026. DOI <https://doi.org/10.1016/j.media.2026.104077>

**2025**

- Bryan Sangwoo Kim, Jeongsol Kim, and Jong Chul Ye. "Chain-of-Zoom: Extreme Super-Resolution via Scale Autoregression and Preference Alignment". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2025 Spotlight. DOI <https://doi.org/10.52202/085713-4181>
- Jaa-Yeon Lee, ByungHee Cha, Jeongsol Kim, and Jong Chul Ye. "Aligning Text to Image in Diffusion Models is Easier Than You Think". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2025. DOI <https://doi.org/10.52202/085713-5249>
- Jiachen Yao, Abbas Mammadov, Julius Berner, Gavin Kerrigan, Jong Chul Ye , Kamyar Azizzadenesheli, and Anima Anandkumar. "Guided Diffusion Sampling on Function Spaces with Applications to PDEs". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2025. DOI <https://doi.org/10.52202/085713-4233>
- Noam Elata, Hyungjin Chung, Jong Chul Ye , Tomer Michaeli, and Michael Elad. "InvFussion: Bridging Supervised and Zero-shot Diffusion for Inverse Problems". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2025.
- Hyeonho Jeong, Suhyeon Lee, and Jong Chul Ye. "Reangle-A-Video: 4D Video Generation as Video-to-Video Translation". In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2025, Hawaii , 2025. DOI <https://doi.org/10.1109/iccv51701.2025.01039>
- Taesung Kwon and Jong Chul Ye. "VISION-XL: High Definition Video Inverse Problem Solver using Latent Image Diffusion Models". In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2025, Hawaii , 2025. DOI <https://doi.org/10.1109/iccv51701.2025.00974>
- Jaemin Kim, Bryan Sangwoo Kim, and Jong Chul Ye. "Free2Guide: Training-Free Text-to-Video Alignment using Image LVLM". In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2025, Hawaii , 2025.
- Jeongsol Kim, Bryan Sangwoo Kim, and Jong Chul Ye. "FlowDPS : Flow-Driven Posterior Sampling for Inverse Problems". In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2025, Hawaii , 2025. DOI <https://doi.org/10.1109/iccv51701.2025.01146>
- Geon Yeong Park, Sang Wan Lee, and Jong Chul Ye. "Inference-Time Diffusion Model Distillation". In Proceedings of the IEEE International Conference on Computer Vision (ICCV) 2025, Hawaii , 2025. DOI <https://doi.org/10.1109/iccv51701.2025.00386>
- Soobin Um, Beomsu Kim, and Jong Chul Ye. "Boost-and-Skip: A Simple Guidance-Free Diffusion for Minority Generation". In International Conference on Machine Learning ( ICML ) , 2025.
- Jinho Chang and Jong Chul Ye. "LDMol: Text-to-Molecule Diffusion Model with Structurally Informative Latent Space Space Surpass the AR Models". In International Conference on Machine Learning ( ICML ) , 2025.
- Soobin Um and Jong Chul Ye. "Minority-Focused Text-to-Image Generation via Prompt Optimization". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2025 , 2025 selected as oral presentation, top 0.74%. DOI <https://doi.org/10.1109/cvpr52734.2025.01949>
- Hyelin Nam, Jaemin Kim, Dohun Lee, and Jong Chul Ye. "Optical-Flow Guided Prompt Optimization for Coherent Video Generation". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2025. DOI <https://doi.org/10.1109/cvpr52734.2025.00734>
- Won Jun Kim, Hyungjin Chung, Jaemin Kim, Sangmin Lee, Byeongsu Sim, and Jong Chul Ye. "Derivative-Free Diffusion Manifold-Constrained Gradient for Unified XAI". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2025. DOI <https://doi.org/10.1109/cvpr52734.2025.02216>
- Dohun Lee, Bryan Sangwoo Kim, Geon Yeong Park, and Jong Chul Ye. "VideoGuide: Improving Video Diffusion Models without Training Through a Teacher’s Guide". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2025. DOI <https://doi.org/10.1109/cvpr52734.2025.00248>
- Hyeonho Jeong, Chun-Hao Paul Huang, Jong Chul Ye , Niloy Mitra, and Duygu Ceylan. "Track4Gen: Teaching Video Diffusion Models to Track Points Improves Video Generation". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2025. DOI <https://doi.org/10.1109/cvpr52734.2025.00682>
- Taesung Kwon and Jong Chul Ye. "Solving Video Inverse Problems Using Image Diffusion Models". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Hyungjin Chung, Jeongsol Kim, Geon Yeong Park, Hyelin Nam, and Jong Chul Ye. "CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Jeongsol Kim, Geon Yeong Park, Hyungjin Chung, and Jong Chul Ye. "Regularization by Texts for Latent Diffusion Inverse Solvers". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Serin Yang, Taesung Kwon, and Jong Chul Ye. "ViBiDSampler: Enhancing Video Interpolation Using Bidirectional Diffusion Sampler". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Gihyun Kwon and Jong Chul Ye. "TweedieMix: Improving Multi-Concept Fusion for Diffusion-based Image/Video Generation". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Beomsu Kim, Jaemin Kim, Jeongsol Kim, and Jong Chul Ye. "Generalized Consistency Trajectory Models for Image Manipulation". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Beomsu Kim, Yu-Guan Hsieh, Michal Klein, cuturi, Jong Chul Ye , Bahjat Kawar, and James Thornton. "Simple ReFlow: Improved Techniques for Fast Flow Models". In The Thirteenth International Conference on Learning Representations (ICLR) , 2025.
- Geon Yeong Park, Hyeonho Jeong, Sang Wan Lee, and Jong Chul Ye. "Spectral Motion Alignment for Video Motion Transfer using Diffusion Models". In Proceedings of the 39th Annual AAAI Conference on Artificial Intelligence (AAAI) , 2025. DOI <https://doi.org/10.1609/aaai.v39i6.32685>
- Dongjin Seo, Soobin Um, Sangbin Lee, Jong Chul Ye , and Haejun Chung. "Physics-guided and fabrication-aware inverse design of photonic devices using diffusion models". ACS Photonics , vol. 13, no. 2, pp. 363–372, 2025. DOI <https://doi.org/10.1021/acsphotonics.5c00993>
- Taesung Kwon, Gookho Song, Yoosun Kim, Jong Chul Ye , and Mooseok Jang. "Video Diffusion Posterior Sampling for Seeing Beyond Dynamic Scattering Layers". IEEE Transactions on Pattern Analysis and Machine Intelligence , vol. 47, no. 12, pp. 11152–11167, 2025. DOI <https://doi.org/10.1109/tpami.2025.3598457>
- Kwanyoung Kim, Yujin Oh, Sangjoon Park, Hwa Kyung Byun, Joongyo Lee, Jin Sung Kim, Yong Bae Kim, and Jong Chul Ye. "End-to-End Breast Cancer Radiotherapy Planning via LMMs with Consistency Embedding". Medical Image Analysis (in press) , 2025. DOI <https://doi.org/10.1016/j.media.2025.103646>
- Riccardo Barbano, Alexander Denker, Hyungjin Chung, Tae Hoon Roh, Simon Arridge, Peter Maass, Bangti Jin, and Jong Chul Ye. "Steerable conditional diffusion for out-of-distribution adaptation in medical image reconstruction". IEEE Transactions on Medical Imaging , vol. 44, no. 5, pp. 2093–2104, 2025. DOI <https://doi.org/10.1109/tmi.2024.3524797>

**2024**

- Hyeonho Jeong, Jinho Chang, Geon Yeong Park, and Jong Chul Ye. "DreamMotion: Space-Time Self-Similarity Score Distillation for Zero-Shot Video Editing". In Proceedings of 2024 European Conference on Computer Vision (ECCV) , 2024.
- Soobin Um and Jong Chul Ye. "Self-Guided Generation of Minority Samples Using Diffusion Models". In Proceedings of 2024 European Conference on Computer Vision (ECCV) , 2024. DOI <https://doi.org/10.1007/978-3-031-73113-6_24>
- Hyungjin Chung and Jong Chul Ye. "Deep Diffusion Image Prior for Efficient OOD Adaptation in 3D Inverse Problems". In Proceedings of 2024 European Conference on Computer Vision (ECCV) , 2024. DOI <https://doi.org/10.1007/978-3-031-73226-3_25>
- Kwanyoung Kim, Yujin Oh, and Jong Chul Ye. "OTSeg: Multi-prompt Sinkhorn Attention for Zero-Shot Semantic Segmentation". In Proceedings of 2024 European Conference on Computer Vision (ECCV) , 2024. DOI <https://doi.org/10.1007/978-3-031-72980-5_12>
- Jeongsol Kim, Geon Yeong Park, and Jong Chul Ye. "DreamSampler: Unifying Diffusion Sampling and Score Distillation for Image Manipulation". In Proceedings of 2024 European Conference on Computer Vision (ECCV) , 2024. DOI <https://doi.org/10.1007/978-3-031-73007-8_23>
- Sangmin Lee, Abbas Mammadov, and Jong Chul Ye. "Defining Neural Network Architecture through Polytope Structures of Dataset". In Proceedings of the International Conference on Machine Learning (ICML) , 2024.
- Hyungjin Chung, Jong Chul Ye , Peyman Milanfar, and Mauricio Delbracio. "Prompt-tuning latent diffusion models for inverse problems". In Proceedings of the International Conference on Machine Learning (ICML) , 2024.
- Hyelin Nam, Gihyun Kwon, Geon Yeong Park, and Jong Chul Ye. "Contrastive Denoising Score for Text-guided Latent Diffusion Image Editing". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2024. DOI <https://doi.org/10.1109/cvpr52733.2024.00878>
- Hyeonho Jeong, Geon Yeong Park, and Jong Chul Ye. "One-Shot Video Motion Customization using Temporal Attention Adaption for Text-to-Video Diffusion Models". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2024.
- Geon Yeong Park, Chanyong Jung, Sangmin Lee, Jong Chul Ye , and Sang Wan Lee. "Self-supervised debiasing using low rank regularization". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2024. DOI <https://doi.org/10.1109/cvpr52733.2024.01178>
- Gihyun Kwon, Simon Jenni, Dingzeyu Li, Joon-Young Lee, Jong Chul Ye , and Fabian Caba Heilbron. "Concept Weaver: Enabling Multi-Concept Fusion in Text-to-Image Models". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2024. DOI <https://doi.org/10.1109/cvpr52733.2024.00848>
- Hyeonho Jeong and Jong Chul Ye. "Ground-A-Video: Zero-shot Grounded Video Editing using Text-to-image Diffusion Models". In International Conference on Learning Representations ( ICLR ) , 2024.
- Hyungjin Chung, Suhyeon Lee, and Jong Chul Ye. "Decomposed Diffusion Sampler for Accelerating Large-Scale Inverse Problems". In International Conference on Learning Representations ( ICLR ) , 2024.
- Beomsu Kim, Gihyun Kwon, Kwanyoung Kim, and Jong Chul Ye. "Unpaired Image-to-Image Translation via Neural Schrödinger Bridge". In International Conference on Learning Representations ( ICLR ) , 2024.
- Soobin Um, Suhyeon Lee, and Jong Chul Ye. "Don’t Play Favorites: Minority Guidance for Diffusion Models". In International Conference on Learning Representations ( ICLR ) , 2024.
- JangHo Park, Gihyun Kwon, and Jong Chul Ye. "ED-NeRF: Efficient Text-Guided Editing of 3D Scene With Latent Space NeRF". In International Conference on Learning Representations ( ICLR ) , 2024.
- Suhyeon Lee, Won Jun Kim, Jinho Chang, and Jong Chul Ye. "LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation". In International Conference on Learning Representations ( ICLR ) , 2024.
- Chanyong Jung, Gihyun Kwon, and Jong Chul Ye. "Patch-Wise Graph Contrastive Learning for Image Translation". In The 38th Annual AAAI Conference on Artificial Intelligence (AAAI) , 2024. DOI <https://doi.org/10.1609/aaai.v38i12.29199>
- Sehui Kim, Hyungjin Chung, Se Hie Park, Eui-Sang Chung, Kayoung Yi, and Jong Chul Ye. "Fundus image enhancement through direct diffusion bridges". IEEE Journal of Biomedical and Health Informatics , 2024. DOI <https://doi.org/10.1109/JBHI.2024.3446866>
- Yujin Oh, Sangjoon Park, Hwa Kyung Byun, Yeona Cho, Ik Jae Lee, Jin Sung Kim, and Jong Chul Ye. "LLM-driven Multimodal Target Volume Contouring in Radiation Oncology". Nature Communications , vol. 15, no. 1, pp. 9186, 2024. DOI <https://doi.org/10.1038/s41467-024-53387-y>
- S. Park, I. J. Lee, J. W. Kim, and Jong Chul Ye. "MS-DINO: Masked Self-Supervised Distributed Learning Using Vision Transformer". IEEE Journal of Biomedical and Health Informatics , vol. 28, no. 10, pp. 6180–6192, Oct 2024. DOI <https://doi.org/10.1109/jbhi.2024.3423797>
- Sangmin Lee and Jong Chul Ye. "Magnitude and Angle Dynamics in Training Single ReLU Neurons". Neural Networks (in press) , 2024. DOI <https://doi.org/10.1016/j.neunet.2024.106435>
- Jinho Chang and Jong Chul Ye. "Bidirectional generation of structure and properties through a single molecular foundation model". Nature Communications , vol. 15, no. 1, pp. 2323, 2024. DOI <https://doi.org/10.1038/s41467-024-46440-3>
- Gyutaek Oh, Yeonsil Moon, Won-Jin Moon, and Jong Chul Ye. "Unpaired Deep Learning for Pharmacokinetic Parameter Estimation from Dynamic Contrast-Enhanced MRI without AIF Measurements". NeuroImage , vol. 291, pp. 120571, May 2024. DOI <https://doi.org/10.1016/j.neuroimage.2024.120571>
- G. Oh, S. Jung, J. E. Lee, and Jong Chul Ye. "Annealed Score-Based Diffusion Model for MR Motion Artifact Reduction". IEEE Transactions on Computational Imaging , vol. 10, pp. 43–53, 2024. DOI <https://doi.org/10.1109/tci.2023.3347917>
- J. Huh, S. Park, J. E. Lee, and Jong Chul Ye. "Improving Medical Speech-to-Text Accuracy using Vision-Language Pre-training Models". IEEE Journal of Biomedical and Health Informatics , vol. 28, no. 3, pp. 1692–1703, Mar 2024. DOI <https://doi.org/10.1109/jbhi.2023.3345897>
- Boah Kim, Yujin Oh, Bradford J. Wood, Ronald M. Summers, and Jong Chul Ye. "C-DARL: Contrastive diffusion adversarial representation learning for label-free blood vessel segmentation". Medical Image Analysis , vol. 91, pp. 103022, Jan 2024. DOI <https://doi.org/10.1016/j.media.2023.103022>
- Sangjoon Park, Eun Sun Lee, Kyung Sook Shin, Jeong Eun Lee, and Jong Chul Ye. "Self-supervised Multi-modal Training from Uncurated Image and Reports Enables Zero-shot Oversight Artificial Intelligence in Radiology". Medical Image Analysis , vol. 91, pp. 103021, Jan 2024.

**2023**

- Jong Chul Ye , Yonina C. Eldar, and Michael Unser. "Deep Learning for Biomedical Image Reconstruction". Cambridge University Press , ISBN 978-1-316-51751-2(edited volume) , 2023. DOI <https://doi.org/10.1017/9781009042529>
- Geon Yeong Park, Jeongsol Kim, Beomsu Kim, Sang Wan Lee, and Jong Chul Ye. "Energy-Based Cross Attention for Bayesian Context Update in Text-to-Image Diffusion Models". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2023. DOI <https://doi.org/10.52202/075280-3339>
- Hyungjin Chung, Jeongsol Kim, and Jong Chul Ye. "Direct Diffusion Bridge using Data Consistency for Inverse Problems". In Conference on Neural Information Processing Systems ( NeurIPS ) , 2023.
- Serin Yang, Hyunmin Hwang, and Jong Chul Ye. "Zero-shot contrastive loss for text-guided diffusion image style transfer". In IEEE/CVF International Conference on Computer Vision (ICCV) , 2023. DOI <https://doi.org/10.1109/iccv51070.2023.02091>
- S. Lee, H. Chung, M. Park, J. Park, W. S. Ryu, and Jong Chul Ye. "Improving 3D Imaging with Pre-Trained Perpendicular 2D Diffusion Models". In IEEE/CVF International Conference on Computer Vision (ICCV) , 2023. DOI <https://doi.org/10.1109/iccv51070.2023.00983>
- Beomsu Kim and Jong Chul Ye. "Denoising MCMC for Accelerating Diffusion-Based Generative Models". In International Conference on Machine Learning ( ICML ), oral presentation , 2023.
- Sangyun Lee, Beomsu Kim, and Jong Chul Ye. "Minimizing Trajectory Curvature of ODE-based Generative Models". In International Conference on Machine Learning ( ICML ), (2023) , 2023.
- Geon Yeong Park, Sangmin Lee, Sang Wan Lee, and Jong Chul Ye. "Training debiased subnetworks with contrastive weight pruning". In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2023. DOI <https://doi.org/10.1109/cvpr52729.2023.00766>
- Hyungjin Chung, Jeongsol Kim, Sehui Kim, and Jong Chul Ye. "Parallel Diffusion Models of Operator and Image for Blind Inverse Problems". In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2023. DOI <https://doi.org/10.1109/cvpr52729.2023.00587>
- Hyungjin Chung, Dohoon Ryu, Michael T. Mccann, Marc L. Klasky, and Jong Chul Ye. "Solving 3D Inverse Problems using Pre-trained 2D Diffusion Models". In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2023. DOI <https://doi.org/10.1109/cvpr52729.2023.02159>
- Hyungjin Chung, Jeongsol Kim, Michael Thompson Mccann, Marc Louis Klasky, and Jong Chul Ye. "Diffusion Posterior Sampling for General Noisy Inverse Problems". In International Conference on Learning Representations ( ICLR ), 2023 Spotlight Presentation , 2023.
- Boah Kim, Yujin Oh, and Jong Chul Ye. "Diffusion Adversarial Representation Learning for Self-supervised Vessel Segmentation". In International Conference on Learning Representations ( ICLR ) , 2023.
- Gihyun Kwon and Jong Chul Ye. "Diffusion-based Image Translation using disentangled style and content representation". In International Conference on Learning Representations ( ICLR ) , 2023.
- Sangjoon Park, Haruhito Yuki, Takayuki Niida, Keishi Suzuki, Daisuke Kinoshita, Iris McNulty, Alexander Broersen, Jouke Dijkstra, Hang Lee, Tsunekazu Kakuta, Jong Chul Ye , and Ik-Kyung Jang. "A Novel Deep Learning Model for a Computed Tomography Diagnosis of Coronary Plaque Erosion". Scientific Reports , vol. 13, no. 1, pp. 22992, 2023. DOI <https://doi.org/10.1038/s41598-023-50483-9>
- Gihyun Kwon and Jong Chul Ye. "One-Shot Adaptation of GAN in Just One CLIP". IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI) , vol. 45, pp. 12179–12191, Oct 2023. DOI <https://doi.org/10.1109/tpami.2023.3283551>
- Yujin Oh, Go Eun Bae, Kyung-Hee Kim, Min-Kyung Yeo, and Jong Chul Ye. "Multi-Scale Hybrid Vision Transformer for Learning Gastric Histology: AI-Based Decision Support System for Gastric Cancer Treatment". IEEE Journal of Biomedical and Health Informatics , vol. 27, no. 8, pp. 4143–4153, Aug 2023. DOI <https://doi.org/10.1109/jbhi.2023.3276778>
- W. C. Karl, J. E. Fowler, C. A. Bouman, M. Çetin, B. Wohlberg, and Jong Chul Ye. "The Foundations of Computational Imaging: A signal processing perspective". IEEE Signal Processing Magazine , vol. 40, no. 5, pp. 40–53, Jul 2023. DOI <https://doi.org/10.1109/msp.2023.3274328>
- Sangjoon Park, Jong Chul Ye , Eun Sun Lee, Gyeongme Cho, Jin Woo Yoon, Joo Hyeok Choi, Ijin Joo, and Yoon Jin Lee. "Deep learning-enabled detection of pneumoperitoneum in supine and erect abdominal radiography: modeling using transfer learning and semi-supervised learning". Korean Journal of Radiology , vol. 24, no. 6, pp. 541, 2023. DOI <https://doi.org/10.3348/kjr.2022.1032>
- Makoto Araki, Sangjoon Park, Akihiro Nakajima, Hang Lee, Jong Chul Ye , and Ik-Kyung Jang. "Diagnosis of coronary layered plaque by deep learning". Scientific Reports , vol. 13, no. 1, pp. 2432, 2023. DOI <https://doi.org/10.1038/s41598-023-29293-6>
- B. Kim, J. Kim, and Jong Chul Ye. "Task-Agnostic Vision Transformer for Distributed Learning of Image Processing". IEEE Transactions on Image Processing , vol. 32, pp. 203–218, 2023. DOI <https://doi.org/10.1109/tip.2022.3226892>
- H. Chung, E. S. Lee, and Jong Chul Ye. "MR Image Denoising and Super-Resolution Using Regularized Reverse Diffusion". IEEE Transactions on Medical Imaging , vol. 42, no. 4, pp. 922–934, Apr 2023. DOI <https://doi.org/10.1109/tmi.2022.3220681>
- Chanseok Lee, Gookho Song, Hyeonggeon Kim, Jong Chul Ye , and Mooseok Jang. "Deep learning based on parameterized physical forward model for adaptive holographic imaging with unpaired data". Nature Machine Intelligence , vol. 5, no. 1, pp. 35–45, 2023. DOI <https://doi.org/10.1038/s42256-022-00584-3>
- Joonyoung Song and Jong Chul Ye. "Wavelet Subband Discriminator for Efficient UnsupervisedChest X-ray Image Restoration". Medical Physics , vol. 50, no. 4, pp. 2263–2278, Apr 2023. DOI <https://doi.org/10.1002/mp.16088>
- S. Park and Jong Chul Ye. "Multi-Task Distributed Learning Using Vision Transformer With Random Patch Permutation". IEEE Transactions on Medical Imaging , vol. 42, no. 7, pp. 2091–2105, Jul 2023. DOI <https://doi.org/10.1109/tmi.2022.3218783>
- Jaeyoung Huh, Shujaat Khan, Sungjin Choi, Dongkuk Shin, Jeong Eun Lee, Eun Sun Lee, and Jong Chul Ye. "Tunable Image Quality Control of 3-D Ultrasound using Switchable CycleGAN". Medical Image Analysis , vol. 83, pp. 102651, Jan 2023. DOI <https://doi.org/10.1016/j.media.2022.102651>
- Z. Zhao, Jong Chul Ye , and Y. Bresler. "Generative Models for Inverse Imaging Problems: From mathematical foundations to physics-driven applications". IEEE Signal Processing Magazine , vol. 40, no. 1, pp. 148–163, Jan 2023. DOI <https://doi.org/10.1109/msp.2022.3215282>

**2022**

- Jong Chul Ye. "Geometry of Deep Learning: A Signal Processing Perspective". Springer , Mathematics in Industry, ISBN 978-981-16-6045-0, 2022. DOI <https://doi.org/10.1007/978-981-16-6046-7>
- Sangyun Lee, Hyungjin Chung, Jaehyeon Kim, and Jong Chul Ye. "Progressive deblurring of diffusion models for coarse-to-fine image synthesis". In NeurIPS 2022 Workshop on Score-Based Methods , 2022.
- Beomsu Kim and Jong Chul Ye. "Energy-Based Contrastive Learning of Visual Representations". In Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS) , 2022. DOI <https://doi.org/10.52202/068431-0315>
- Hyungjin Chung, Byeongsu Sim, Dohoon Ryu, and Jong Chul Ye. "Improving Diffusion Models for Inverse Problems using Manifold Constraints". In Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS) , 2022. DOI <https://doi.org/10.52202/068431-1862>
- Yujin Oh and Jong Chul Ye. "CXR Segmentation by AdaIN-based Domain Adaptation and Knowledge Distillation". In European Conference on Computer Vision ( ECCV ), 2022 , 2022. DOI <https://doi.org/10.1007/978-3-031-19803-8_37>
- Boah Kim, Inhwa Han, and Jong Chul Ye. "DiffuseMorph: Unsupervised Deformable Image Registration Using Diffusion Models". In European Conference on Computer Vision ( ECCV ) , 2022.
- Chanyong Jung, Joonhyung Lee, Sun Kyoung You, and Jong Chul Ye. "Patch-wise Deep Metric Learning for Unsupervised Low-Dose CT Denoising". In International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI) , 2022. DOI <https://doi.org/10.1007/978-3-031-16446-0_60>
- Boah Kim and Jong Chul Ye. "Diffusion deformable model for 4D temporal medical image generation". In the 25th International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI) , 2022. DOI <https://doi.org/10.1007/978-3-031-16431-6_51>
- Gwanghyun Kim and Jong Chul Ye. "Diffusion CLIP : Text-guided image manipulation using diffusion models". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2022.
- Chanyong Jung, Gihyun Kwon, and Jong Chul Ye. "Exploring Patch-wise Semantic Relation for Contrastive Learning in Image-to-Image Translation Tasks". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2022. DOI <https://doi.org/10.1109/cvpr52688.2022.01772>
- Gihyun Kwon and Jong Chul Ye. "C LIP styler: Image style transfer with a single text condition". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2022. DOI <https://doi.org/10.1109/cvpr52688.2022.01753>
- Kwanyoung Kim, Taesung Kwon, and Jong Chul Ye. "Noise d istribution a daptive s elf- s upervised i mage d enoising using Tweedie d istribution and s core m atching". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2022. DOI <https://doi.org/10.1109/cvpr52688.2022.00205>
- Hyungjin Chung, Byeongsu Sim, and Jong Chul Ye. "Come-Closer-Diffuse-Faster: Accelerating Conditional Diffusion Models for Inverse Problems through Stochastic Contraction". In IEEE/CVF Conference on Computer Vision and Pattern Recognition ( CVPR ) , 2022. DOI <https://doi.org/10.1109/cvpr52688.2022.01209>
- A. Wahab, S. Khan, I. Naseem, and Jong Chul Ye. "Performance Analysis of Fractional Learning Algorithms". IEEE Transactions on Signal Processing , vol. 70, pp. 5164–5177, 2022. DOI <https://doi.org/10.1109/tsp.2022.3215735>
- Hyunjong Kim, Gyutaek Oh, Joon Beom Seo, Hye Jeon Hwang, Sang Min Lee, Jihye Yun, and Jong Chul Ye. "Multi-domain CT translation by a routable translation network". Physics in Medicine & Biology , vol. 67, no. 21, pp. 215002, 2022. DOI <https://doi.org/10.1088/1361-6560/ac950e>
- Sangjoon Park, Makoto Araki, Akihiro Nakajima, Hang Lee, Valentin Fuster, Jong Chul Ye , and Ik-Kyung Jang. "Enhanced diagnosis of plaque erosion by deep learning in patients with acute coronary syndromes". JACC: Cardiovascular Interventions , vol. 15, no. 20, pp. 2020–2031, Oct 2022. DOI <https://doi.org/10.1016/j.jcin.2022.08.040>
- Eunju Cha, Hyungjin Chung, Jaeduck Jang, Junho Lee, Eunha Lee, and Jong Chul Ye. "Low-dose sparse-view HAADF-STEM-EDX tomography of nanocrystals using unsupervised deep learning". ACS Nano , vol. 16, no. 7, pp. 10314–10326, Jun 2022. DOI <https://doi.org/10.1021/acsnano.2c00168>
- Sangjoon Park, Gwanghyun Kim, Yujin Oh, Joon Beom Seo, Sang Min Lee, Jin Hwan Kim, Sungjun Moon, Jae-Kwang Lim, Chang Min Park, and Jong Chul Ye. "Self-evolving vision transformer for chest X-ray diagnosis through knowledge distillation". Nature communications , vol. 13, no. 1, pp. 3848, 2022. DOI <https://doi.org/10.1038/s41467-022-31514-x>
- Hyoungjun Park, Myeongsu Na, Bumju Kim, Soohyun Park, Ki Hean Kim, Sunghoe Chang, and Jong Chul Ye. "Deep learning enables reference-free isotropic super-resolution for volumetric fluorescence microscopy". Nature Communications , vol. 13, no. 1, pp. 3297, 2022. DOI <https://doi.org/10.1038/s41467-022-30949-6>
- Hyungjin Chung and Jong Chul Ye. "Score-based diffusion models for accelerated MRI". Medical Image Analysis , vol. 80, pp. 102479, Aug 2022. DOI <https://doi.org/10.1016/j.media.2022.102479>
- Gyutaek Oh, Hyokyoung Bae, Hyun-Seo Ahn, Sung-Hong Park, Won Jin Moon, and Jong Chul Ye. "Unsupervised Resolution-Agnostic Quantitative Susceptibility Mapping using Adaptive Instance Normalization". Medical Image Analysis , vol. 79, pp. 102477, Jul 2022. DOI <https://doi.org/10.1016/j.media.2022.102477>
- M. Moinuddin, S. Khan, A. U. Alsaggaf, M. J. Abdulaal, U. M. Al-Saggaf, and Jong Chul Ye. "Medical ultrasound image speckle reduction and resolution enhancement using texture compensated multi-resolution convolution neural network". Frontiers in Physiology , 2022. DOI <https://doi.org/10.3389/fphys.2022.961571>
- M. Akçakaya, B. Yaman, H. Chung, and Jong Chul Ye. "Unsupervised Deep Learning Methods for Biological Image Reconstruction and Enhancement: An overview from a signal processing perspective". IEEE Signal Processing Magazine , vol. 39, no. 2, pp. 28–44, Mar 2022. DOI <https://doi.org/10.1109/MSP.2021.3119273>
- Sangjoon Park, Gwanghyun Kim, Yujin Oh, Joon Beom Se, Sang Min Lee, Jin Hwan Kim, Sungjun Moon, Jae-Kwang Lim, and Jong Chul Ye. "Multi-task vision transformer using low-level chest X-ray feature corpus for COVID-19 diagnosis and severity quantification". Medical Image Analysis , vol. 75, pp. 102299, Jan 2022. DOI <https://doi.org/10.1016/j.media.2021.102299>
- Eunju Cha, Chanseok Lee, Mooseok Jang, and Jong Chul Ye. "DeepPhaseCut: Deep Relaxation in Phase for Unsupervised Fourier Phase Retrieval". IEEE Transactions on Pattern Analysis and Machine Intelligence , vol. 44, no. 12, pp. 9931–9943, Dec 2022. DOI <https://doi.org/10.1109/tpami.2021.3138897>

**2021**

- Kwanyoung Kim and Jong Chul Ye. "Noise2Score: Tweedie’s Approach to Self-Supervised Image Denoising without Clean Images". In Proceedings of the Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS) , Virtual, December , 2021.
- Sangjoon Park, Gwanghyun Kim, Jeongsol Kim, Boah Kim, and Jong Chul Ye. "Federated Split Task-Agnostic Vision Transformer for COVID-19 CXR Diagnosis". In Proceedings of the Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS) , Virtual, December 2021. (\*co-first authors) , 2021. 논문집 초록 <https://proceedings.neurips.cc/paper/2021/hash/ceb0595112db2513b9325a85761b7310-Abstract.html>
- Byung-Hoon Kim, Jong Chul Ye , and Jae-Jin Kim. "Learning Dynamic Graph Representation of Brain Connectome with Spatio-Temporal Attention". In Proceedings of the Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS) , Virtual, December , 2021.
- Kwon Gihyun and Jong Chul Ye. "Diagonal Attention and Style-based GAN for Content-Style Disentanglement in Image Generation and Translation". In IEEE/CVF International Conference on Computer Vision (ICCV) , 2021. DOI <https://doi.org/10.1109/iccv48922.2021.01372>
- T. Kwon and Jong Chul Ye. "Cycle-Free CycleGAN Using Invertible Generator for Unsupervised Low-Dose CT Denoising". IEEE Transactions on Computational Imaging , vol. 7, pp. 1354–1368, 2021. DOI <https://doi.org/10.1109/TCI.2021.3129369>
- J. Lee, J. Gu, and Jong Chul Ye. "Unsupervised CT Metal Artifact Learning Using Attention-Guided β-CycleGAN". IEEE Transactions on Medical Imaging , vol. 40, no. 12, pp. 3932–3944, Dec 2021. DOI <https://doi.org/10.1109/TMI.2021.3101363>

## 수상과 선정

연구실이 구성원에게 매년 수여하는 자체 연례상(BISPL Award) 15항목과, 소식에 게시된 외부 수상·선정 6항목이다. 연례상은 부문별 한 항목이며, 같은 부문의 공동 수상자는 한 줄에 적었다. 날짜는 시상일 또는 소식 게시일이다.[^awards][^news][^mathaward][^gold][^fellow][^bookaward]

- 2026-09-09 · KAIRI 하계 인턴, ECCV 2026 Perception Test Challenge의 Grounded Video-QA 트랙 우승.
- 2026-07-10 · ICML 2026 SPIGM Workshop Best Paper Award.
- 2025-12-30 · 2025 BISPL Award Best Researcher of the Year: Jeongsol Kim
- 2025-12-30 · 2025 BISPL Award Best Doctoral Student: Jemin Kim
- 2025-12-30 · 2025 BISPL Award Best Master Student: Bryan Sangwoo Kim
- 2024-12-27 · 2024 BISPL Award Best Researcher of the Year: Hyungjin Chung
- 2024-12-27 · 2024 BISPL Award Best PhD Student: Geon Yeong Park, Jeongsol Kim
- 2024-12-27 · 2024 BISPL Award Best Master Student: Hyeonho Jeong, Jemin Kim
- 2023-12-27 · 2023 BISPL Award Best Researcher of the Year: Hyungjin Chung
- 2023-12-27 · 2023 BISPL Award Best Doctoral Student: Gihyun Kwon
- 2023-12-27 · 2023 BISPL Award Best Master Student: Hyeonho Jeong
- 2023-12-17 · 예종철 교수, 한국과학기술한림원 Fellow 선정.
- 2023-11-27 · 예종철 교수, 최석정상 수상.
- 2023-03-09 · Hyungjin Chung, 2023 Humantech Thesis Award 신호처리 부문 Gold Award 수상.
- 2022-12-21 · 2022 BISPL Award Best Researcher of the Year: Hyungjin Chung
- 2022-12-21 · 2022 BISPL Award Best Doctoral Student: Sangjoon Park
- 2022-12-21 · 2022 BISPL Award Best Master Student: Beomsu Kim
- 2022-01-08 · Geometry of Deep Learning, BookAuthority의 신간 신호처리 도서 선정.
- 2021-12-29 · 2021 BISPL Award Best Researcher of the Year: Hyungjin Chung
- 2021-12-29 · 2021 BISPL Award Best Doctoral Student: Sangjoon Park
- 2021-12-29 · 2021 BISPL Award Best Master Student: Gwanghyun Kim

## 소식

연구실 소식에 게시된 논문 채택·게재 32건이다. 날짜는 게시일이고, 학회 논문 채택은 「채택」으로 표시했다.[^news]

- 2026-10-12 · ContextMRI, Medical Image Analysis 게재 승인.
- 2026-09-26 · 논문 6편, NeurIPS 2026 채택.
- 2026-08-21 · 논문 3편, EMNLP 2026 채택(Findings 2편 포함).
- 2026-06-18 · 논문 5편, ECCV 2026 채택.
- 2026-04-30 · 논문 5편, ICML 2026 채택.
- 2026-02-21 · 논문 4편, CVPR 2026 채택(Findings 1편 포함).
- 2026-01-26 · 논문 5편, ICLR 2026 채택.
- 2025-09-18 · 논문 4편, NeurIPS 2025 채택.
- 2025-08-04 · 논문, IEEE T-PAMI 게재 승인.
- 2025-06-25 · 논문 5편, ICCV 2025 채택.
- 2025-05-01 · 논문 2편, ICML 2025 채택.
- 2025-02-26 · 논문 5편, CVPR 2025 채택.
- 2025-01-22 · 논문 7편, ICLR 2025 채택.
- 2024-07-02 · 논문 5편, ECCV 2024 채택.
- 2024-05-02 · 논문 2편, ICML 2024 채택.
- 2024-03-14 · 화학 기반 모형 논문, Nature Communications 게재.
- 2024-02-26 · 논문 4편, CVPR 2024 채택.
- 2024-01-17 · 논문 6편, ICLR 2024 채택.
- 2023-12-20 · Gyutaek의 논문, IEEE TCI 게재 승인.
- 2023-12-17 · Jaehyung의 논문, IEEE Journal of Biomedical & Health Informatic 게재 승인.
- 2023-11-01 · 논문 2편, Medical Image Analysis 게재 승인.
- 2023-09-21 · 논문 2편, NeurIPS 2023 채택.
- 2023-07-14 · 논문 2편, ICCV 2023 채택.
- 2023-06-09 · 논문, IEEE T-PAMI 게재 승인.
- 2023-04-28 · 논문 2편, ICML 2023 채택.
- 2023-03-09 · 논문 3편, CVPR 2023 채택.
- 2023-01-21 · 논문 3편, ICLR 2023 채택.
- 2022-11-04 · 심층 학습 논문, Nature Machine Intelligence 게재.
- 2022-09-14 · 논문 2편, NeurIPS 2022 채택.
- 2022-07-06 · 논문 2편, ECCV 2022 채택.
- 2022-06-27 · 심층 학습 논문, ACS Nano 게재.
- 2022-03-02 · 논문 5편, CVPR 2022 채택.

## 연락과 위치

- 연구실 주소: 108 Taebong-ro, Seocho-gu, Seoul, 06764, Republic of Korea.[^home]
- 교수 사무실: 양재캠퍼스 7층(701).[^dept]
- 교수 업무 이메일: jong.ye@kaist.ac.kr.[^dept]
[^home]: 연구실 About. <https://bispl-website.github.io/> (관측일 2026-11-07).
[^dept]: KAIST 김재철AI대학원 교수진. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (관측일 2026-11-07).
[^prof]: 연구실 Professor. <https://bispl-website.github.io/professor/> (관측일 2026-11-07).
[^people]: 연구실 People. <https://bispl-website.github.io/people/> (관측일 2026-11-07).
[^alumni]: 연구실 Alumni. <https://bispl-website.github.io/alumni/> (관측일 2026-11-07).
[^pubs]: 연구실 Publications. <https://bispl-website.github.io/publications/> (관측일 2026-11-07).
[^news]: 연구실 News. <https://bispl-website.github.io/news/> (관측일 2026-11-08).
[^awards]: 연구실 Hall of Fame. <https://bispl-website.github.io/awards/> (관측일 2026-11-08).
[^mathaward]: 최석정상 수상 소식. <https://bispl-website.github.io/news/2023-11-01-prof-ye-received-the-prestigious-korean-mathematics-award/> (관측일 2026-11-08).
[^cv]: 예종철 교수 CV. <https://bispl-website.github.io/assets/pdf/cv.pdf> (관측일 2026-11-08).
[^gold]: Hyungjin Chung의 Humantech Thesis Award Gold Award 수상 소식. <https://bispl-website.github.io/news/2023-03-01-congraturations/> (관측일 2026-11-08).
[^fellow]: 한국과학기술한림원 Fellow 선정 소식. <https://bispl-website.github.io/news/2023-12-01-prof-ye-is-selected-as-the-fellow-of-korean-academy-of-science-and-tec/> (관측일 2026-11-08).
[^bookaward]: Geometry of Deep Learning의 BookAuthority 선정 소식. <https://bispl-website.github.io/news/2022-01-01-geometry-of-deep-learning-by-prof-ye-made-it-to-bookauthoritys-best-ne/> (관측일 2026-11-08).
[^p1]: J. Lee, J. Chang, J. Kim, J. C. Ye, arXiv (온라인 2026-04-19). <https://doi.org/10.48550/arXiv.2604.17415> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.17415> (관측일 2026-11-08).
[^p2]: T. Kwon, J. Park, H. Chung, J. C. Ye, arXiv (온라인 2026-05-20). <https://doi.org/10.48550/arXiv.2605.20624> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2605.20624> (관측일 2026-11-08).
[^p3]: J. Kim, B. S. Kim, J. C. Ye, IEEE/CVF International Conference on Computer Vision (ICCV) (온라인 2025-10-19). <https://doi.org/10.1109/iccv51701.2025.01146> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works/https://doi.org/10.1109/iccv51701.2025.01146> (관측일 2026-11-07).
[^p4]: S. Lee, B. Kim, J. C. Ye, arXiv (Cornell University) (온라인 2023-01-27). <https://doi.org/10.48550/arxiv.2301.12003> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works/https://doi.org/10.48550/arxiv.2301.12003> (관측일 2026-11-07).
[^p5]: H. Chung 외, J. C. Ye, arXiv (Cornell University) (온라인 2022-09-29). <https://doi.org/10.48550/arxiv.2209.14687> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works/https://doi.org/10.48550/arxiv.2209.14687> (관측일 2026-11-07).
[^p6]: H. Chung, J. C. Ye, arXiv (온라인 2021-10-08). <https://doi.org/10.48550/arXiv.2110.05243> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2110.05243> (관측일 2026-11-08).
[^p7]: H. Park 외, J. C. Ye, Nature Communications 13, 3297 (온라인 2022-06-08). <https://doi.org/10.1038/s41467-022-30949-6> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/W3166384617> (관측일 2026-11-07).
[^p8]: S. Lee, W. J. Kim, J. Chang, J. C. Ye, arXiv (온라인 2023-05-19). <https://doi.org/10.48550/arXiv.2305.11490> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2305.11490> (관측일 2026-11-08).

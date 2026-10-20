# 음악 및 오디오 컴퓨팅 연구실 (Music and Audio Computing Lab, MACLab)

**KAIST 문화기술대학원 · 남주한 교수**

- 분야: 음악 정보 검색(음악 이해·태깅·캡셔닝·추천), 오디오 신호 처리, 음악·오디오용 기계학습, 음악을 위한 인간-AI 상호작용, 연주 분석·모델링(피아노 전사, AI 연주 시스템), 소리 합성과 디지털 오디오 효과
- 홈페이지: <https://mac.kaist.ac.kr/>
- 근거와 출처: [MACLab 근거 페이지](mac-sources.md)

> 사람이 음악을 즐기고 연주하고 만드는 방식을 기술로 넓히려는 연구실이다. 음악을 듣고 이해해 말로 설명하거나 찾아 주는 AI, 영상에 맞는 효과음이나 악기 소리를 만들어 내는 AI, 피아노 연주를 실시간으로 받아 적고 사람과 함께 연주하는 AI를 만든다.[^home][^research]

## 무엇을 연구하나

연구실은 문화기술대학원의 음악 연구 그룹으로, 사람들이 음악을 즐기고 연주하고 만드는 방식을 기술로 개선하는 것을 목표로 한다. 특히 음악을 이해하고 그 의미를 사람이 알기 쉬운 형태로 나타내며 새로운 음악 콘텐츠를 만들어 사람의 창작을 돕는 "음악 AI"에 관심을 둔다고 소개한다. 주요 분야로 음악 정보 검색(음악 데이터에서 곡의 성격을 알아내고 분류·검색하는 분야, MIR), 오디오 신호 처리, 음악·오디오를 위한 기계학습과 딥러닝, 음악을 위한 인간-AI 상호작용, 연주의 계산적 분석과 모델링, 소리 합성과 디지털 오디오 효과를 든다.[^home]

첫 번째 갈래는 **음악을 이해하고 언어로 잇는 연구**다. 연구실은 다중 모달 음악 검색(소리, 글, 영상처럼 종류가 다른 데이터를 함께 다루는 검색), 음악 태깅과 캡셔닝(곡에 장르·분위기 같은 꼬리표나 설명 문장을 붙이는 일)을 다룬다.[^research] 대표 논문에서는 대형 언어 모델(방대한 글로 학습해 문장을 만들어 내는 AI)로 음악 설명 문장을 대량으로 만들어 캡셔닝 모델을 학습시켰고,[^p1] 음악 단어를 이해하는 단어 임베딩(단어의 뜻을 숫자 묶음으로 나타낸 것)을 만들었으며,[^p2] 대화로 음악을 찾아 주는 시스템용 대화 데이터를 만들었다.[^p3] 대형 언어 모델을 음악 제작, 노래 교육, 음악 추천에 쓰는 과제도 진행한다.[^research]

두 번째 갈래는 **소리를 만들고 다듬는 연구**다. 녹음 환경 바꾸기와 음질 높이기, 효과음(폴리) 생성, 악기 소리 합성, 신경망 오디오 코덱, 노래 음성 합성·편집을 과제로 묶어 연구한다.[^research] 대표 논문에서는 영상에 맞는 효과음을 만들어 내는 시스템과,[^p4] 페이저·플랜저 같은 오디오 효과를 하나의 신경망으로 흉내 내고 조절하는 모델을 만들었다.[^p5]

세 번째 갈래는 **연주를 이해하고 함께 연주하는 AI**다. 사람과 상호작용하는 AI 연주 시스템을 위해 실시간 소리·영상 음악 전사(연주 녹음을 음표 정보로 옮기는 일), 연주 신호 감지, 악보 따라가기, 표현력 있는 연주 제어를 연구하고, 피아니스트 동작 데이터를 모아 동작을 생성하는 산업 과제도 한다.[^research] 대표 논문에서는 가볍고 실시간으로 동작하는 피아노 전사 모델과,[^p6] 연주 영상·소리·손 위치를 함께 담은 피아노 연주 데이터셋을 만들었다.[^p7] 연구실 첫 화면은 조수미 공연예술연구센터와의 활동을 함께 소개한다.[^home]

이 밖에 AI DJ와 음악 구조 분석 같은 지능형 음악 제작, 악보 기반(심볼릭) 음악 생성, 해금·가야금 표현 분석과 국악 데이터셋 같은 한국 전통 음악 연구도 한다.[^research] 대표 논문에서는 박자와 곡의 구간(도입, 후렴 등)을 한 모델로 함께 찾는 방법을 만들었다.[^p8]

## 주요 연구 주제

### 1. 음악 이해와 언어

음악 캡셔닝, 음악 단어 임베딩, 대화형 음악 검색.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 소리 생성과 오디오 효과

영상 기반 효과음 생성, 조절 가능한 신경망 오디오 효과.[^p4][^p5] 대표 논문 4, 5.

### 3. 연주 AI와 음악 전사

실시간 피아노 전사, 다중 모달 피아노 연주 데이터셋.[^p6][^p7] 대표 논문 6, 7.

### 4. 음악 구조 분석과 지능형 음악 제작

박자·구간 동시 분석.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 남주한 교수가 마지막 저자인 것에서 네 연구 주제를 고르게 담도록 골랐다. ISMIR는 음악 정보 검색 국제학회, IEEE/ACM TASLP는 오디오·음성·언어 처리 학술지, DAFx는 디지털 오디오 효과 국제학회, WASPAA는 오디오·음향 신호 처리 응용 워크숍이다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2023 | [LP-MusicCaps: LLM-Based Pseudo Music Captioning](https://arxiv.org/abs/2307.16372) · ISMIR 2023 | 곡을 듣고 설명 문장을 만드는 음악 캡셔닝은 학습용 음악-문장 데이터를 모으기가 비싸고 느려 데이터가 적었다. 대규모 꼬리표 데이터에서 대형 언어 모델로 설명 문장을 만들어 오디오 약 50만 개에 문장 약 220만 개를 짝지은 데이터셋을 만들었고, 이 데이터로 학습한 캡셔닝 모델이 기존 지도학습 모델보다 나았다.[^p1] | 1저자 Seungheon Doh, 마지막 저자 남주한 |
| 2 | 2025 | [Musical Word Embedding for Music Tagging and Retrieval](https://doi.org/10.1109/taslpro.2025.3577408) · IEEE/ACM TASLP | 일반 글로 학습한 단어 임베딩은 음악 맥락이나 가수·곡 이름을 잘 이해하지 못한다. 일상 어휘와 음악 어휘를 함께 학습한 음악 단어 임베딩을 만들어 소리와 단어를 같은 공간에 놓고 태깅·검색에 썼다. 꼬리표 수준 학습은 태깅에, 곡 수준 학습은 검색에 유리하다는 점을 보이고 둘을 함께 쓰는 학습법을 제안했다.[^p2] | 1저자 SeungHeon Doh, 마지막 저자 남주한 |
| 3 | 2024 | [Music Discovery Dialogue Generation Using Human Intent Analysis and Large Language Model](https://arxiv.org/abs/2411.07439) · ISMIR 2024 | 대화로 음악을 찾아 주는 시스템을 만들려면 대화 기록이 필요하지만 공개 데이터가 적다. 사용자 의도 분석, 데이터베이스 필터링, 대형 언어 모델을 이어 음악 탐색 대화를 만드는 틀을 만들고, 28만 8천여 개 대화로 된 데이터셋을 만들었다. 이 합성 데이터는 사람이 만든 소규모 대화 데이터와 견줄 만했다.[^p3] | 1저자 Seungheon Doh, 마지막 저자 남주한 |
| 4 | 2025 | [Video-Foley: Two-Stage Video-To-Sound Generation via Temporal Event Condition For Foley Sound](https://doi.org/10.1109/taslpro.2025.3597477) · IEEE/ACM TASLP | 영상에 맞춰 효과음을 넣는 폴리 작업을 자동화하려면 소리가 나는 시점을 맞춰야 한다. 소리 크기의 시간 변화(RMS)를 영상에서 먼저 예측하고, 이를 조건으로 음색을 지정한 소리를 만드는 2단계 시스템을 사람의 표시 없이 학습시켜, 시점·세기·음색 조절과 영상-소리 일치에서 가장 좋은 성능을 냈다.[^p4] | 1저자 Junwon Lee, 마지막 저자 남주한 |
| 5 | 2024 | [CONMOD: Controllable Neural Frame-based Modulation Effects](https://arxiv.org/abs/2406.13935) · DAFx 2024 | 페이저·플랜저처럼 소리를 주기적으로 일렁이게 하는 오디오 효과를 신경망으로 흉내 낸 기존 모델은 조절 손잡이를 돌릴 수 없었다. 여러 효과를 하나의 모델로 흉내 내면서 일렁임 빠르기와 되먹임 정도를 조절할 수 있게 했고, 두 페이저 효과 사이를 오가며 새 소리를 만들 수도 있게 했다.[^p5] | 1저자 Gyubin Lee, 마지막 저자 남주한 |
| 6 | 2024 | [Towards Efficient and Real-Time Piano Transcription Using Neural Autoregressive Models](https://doi.org/10.1109/taslp.2024.3507568) · IEEE/ACM TASLP | 피아노 전사 모델은 정확해졌지만 대부분 녹음이 끝난 뒤 처리하는 큰 모델이었다. 기존 자기회귀 전사 모델(앞서 낸 결과를 다음 예측에 다시 쓰는 모델)을 고쳐 주파수에 따라 필터를 조정하는 층과 음 하나의 상태 변화를 따라가는 층을 넣고, 고성능형과 소형 두 모델로 실시간 피아노 전사를 구현했다.[^p6] | 1저자 Taegyun Kwon, 마지막 저자 남주한 |
| 7 | 2025 | [PianoVAM: A Multimodal Piano Performance Dataset](https://arxiv.org/abs/2509.08800) · ISMIR 2025 | 아마추어 피아니스트가 평소 연습하는 모습을 디스클라비어 피아노(연주를 MIDI로 기록하는 피아노)로 녹음하고 위에서 찍은 영상을 맞춰, 소리·MIDI(연주 정보)·영상·손 위치·운지 정보를 함께 담은 데이터셋을 만들었다. 소리만 쓰는 전사와 소리·영상을 함께 쓰는 전사의 기준 성능도 제시했다.[^p7] | 1저자 Yonghyun Kim, 마지막 저자 남주한 |
| 8 | 2023 | [All-In-One Metrical And Functional Structure Analysis With Neighborhood Attentions on Demixed Audio](https://doi.org/10.1109/waspaa58266.2023.10248148) · IEEE WASPAA 2023 | 음악에는 박자부터 곡의 구간까지 여러 층의 구조가 있는데, 기존 연구는 층마다 따로 풀었다. 악기별로 분리한 소리를 입력으로 박자, 마디 첫 박, 곡 구간 나누기와 이름 붙이기를 한 모델로 함께 풀어, 네 과제 모두에서 가장 좋은 성능을 내면서 모델 크기는 작게 유지했다.[^p8] | 1저자 Taejun Kim, 마지막 저자 남주한 |

## 교수와 전문 분야

남주한 교수는 미국 스탠퍼드대 컴퓨터 음악·음향 연구센터(CCRMA)에서 음악 박사를 받았다. 그 전에는 영창(커즈와일)에서 신시사이저와 디지털 피아노를 개발하는 소프트웨어·DSP 엔지니어로 일했고, KAIST에 오기 전 퀄컴 오디오 R&D 팀의 스태프 연구 엔지니어였다. 문화기술대학원 교수이며 김재철AI대학원과 메타버스대학원 겸임교수이고, Neutune과 AudAi의 공동 창업자라고 적는다.[^prof]

랩 소식에 따르면 2025년 9월 정교수가 됐고, 2025년 KAIST 석좌교수로 3년 임기 임명됐으며, 같은 해 KAIST Outstanding Teaching Award를 받았다. IEEE/ACM Transactions on Audio, Speech, and Language Processing(2023)과 Journal of the Audio Engineering Society(2021)의 부편집장을 맡았고, ISMIR 2021 학술 프로그램 공동 위원장을 지냈으며, 2025년 ISMIR 학회를 KAIST에서 열었다.[^home] 랩 논문 목록은 ISMIR 2023 Best Paper Award Nomination(LP-MusicCaps)과 WASPAA 2023 Best Student Paper Award(All-In-One)를 적는다.[^papers]

논문으로 보면 전문 분야는 세 갈래다.

- **음악 정보 검색과 음악-언어 표현 학습**.[^p1][^p2][^p3][^p8]
- **신경망 오디오 생성과 오디오 효과 모델링**.[^p4][^p5]
- **피아노 연주 전사와 연주 데이터**.[^p6][^p7]

## 응용 분야

대표 논문과 과제로 보면 음악 스트리밍의 검색·추천, 영상 제작의 효과음, 음악 제작 도구, 연주 교육과 AI 협연에 닿아 있다.[^p1][^p3][^p4][^p5][^p7][^research] 랩 소식에 따르면 카카오엔터테인먼트와의 산업 과제 기술이 2025년 멜론의 새 음악 추천 서비스에 쓰였고, 야마하와 산업 과제를 진행하며, 2024년 어도비 리서치에서 연구 기금을 받았다.[^home] 졸업생들은 Neutune, AudAi, SORI 같은 음악 AI 스타트업을 공동 창업했고, 서강대 교수, 소니, 엔씨소프트, 네이버 등으로 진출했다고 랩이 적는다.[^people]

## 구성원

2026년 10월 20일 랩 People 페이지 기준이다. 괄호 안 "Graduate School of AI"는 랩이 적은 소속이다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| 배준형 (Joonhyung Bae) | 박사후연구원 | 7 |
| 천경수 (Kyungsoo Chun) | 박사과정 (On Leave) |  |
| 김원일 (Wonil Kim) | 박사과정 |  |
| 최민석 (Minsuk Choi) | 박사과정 |  |
| 임재권 (Jaekwon Im) | 박사과정 | 4 |
| 김현수 (Houn Su Kim) | 박사과정 | 5 |
| 박지윤 (Jiyun Park) | 박사과정 |  |
| 한단비내린 (Danbinaerin Han) | 박사과정 |  |
| 최재란 (Jaeran Choi) | 박사과정 |  |
| Carolina Carusi | 박사과정 |  |
| 김종수 (Jongsoo Kim) | 박사과정 |  |
| 이준원 (Junwon Lee) | 박사과정 (Graduate School of AI) | 4, 5 |
| 방하연 (Hayeon Bang) | 박사과정 |  |
| 김다빈 (Dabin Kim) | 박사과정 | 4 |
| 손호열 (Hoyeol Sohn) | 박사과정 |  |
| 이세인 (Sein Lee) | 박사과정 |  |
| 박윤정 (Yoonjeong Park) | 석사과정 (Graduate School of AI) |  |
| 이민희 (Minhee Lee) | 석사과정 |  |
| 이규빈 (Gyubin Lee) | 석사과정 (Graduate School of AI) | 5 |
| 고계훈 (Gyehun Go) | 석사과정 |  |
| 원선재 (Sunjae Won) | 석사과정 |  |
| 김기홍 (Kihong Kim) | 석사과정 |  |
| 강우진 (Woojin Kang) | 석사과정 |  |
| 온재현 (Jaehyun On) | 석사과정 |  |
| Rui Lin | 석사과정 |  |

## 졸업생

랩 People 페이지의 박사·석사 졸업생과 진로, 전 박사과정생, 방문 학생이다. 진로는 랩이 적은 순서(->)를 그대로 옮겼다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 배준형 (Joonhyung Bae) | 박사 (2026) | MS 2021 -> PhD 2026 -> KAIST Post-Doc |
| 최은진 (Eunjin Choi) | 박사 (2026) | MS 2022 -> PhD 2026 -> NHN Cloud |
| 김혜미 (Hyemi Kim) | 박사 (2026) | PhD 2026 (ETRI Researcher, Part-Time PhD) |
| 도승헌 (Seungheon Doh) | 박사 (2025) | MS 2021 -> PhD 2025 -> KAIST Post-Doc -> Sony, Creative AI Team (Research Scientist) |
| 임우택 (Wootaek Lim) | 박사 (2025) | PhD 2025 (ETRI Researcher, Part-Time PhD) |
| 김태준 (Taejun Kim) | 박사 (2024) | PhD 2024 -> Neutune (Co-founder, Research Scientist) |
| 권태균 (Taegyun Kwon) | 박사 (2024) | MS 2018 -> PhD 2024 -> KAIST Post-Doc -> SORI (Co-founder, CEO) |
| 용상언 (Sangeon Yong) | 박사 (2024) | MS 2017 -> PhD 2024 -> AudAi (Co-founder, CTO) |
| 최순범 (Soonbeom Choi) | 박사 (2023) | MS 2018 -> PhD 2023 -> AudAi (Co-Founder, CEO) |
| 박새별 (Saebyul Park) | 박사 (2023) | PhD 2023 -> Artist & Yonsei University's Underwood International College (Adjunct professor) |
| 이종필 (Jongpil Lee) | 박사 (2021) | MS 2017 -> PhD 2021 -> Neutune (Co-founder, CEO) |
| 금상은 (Sangeun Kum) | 박사 (2021) | MS 2016 -> PhD 2021 -> Neutune (Co-founder, Research Scientist) |
| 김근형 (Keunhyoung Kim) | 박사 (2021) | PhD 2021 -> Neutune (Co-founder, Research Scientist/Software Engineer) |
| 정다샘 (Dasaem Jeong) | 박사 (2020) | PhD 2020 -> SKTelecom T-Brain (Research Scientist) -> 서강대 아트&테크놀로지학과 Sogang University Department of Art and Technology (Associate Professor) |
| 김승훈 (Seunghun Kim) | 박사 (2016) | PhD 2016 -> Samsung Electronics -> LG Electronics -> Asleep (Researcher) |
| 손호열 (Hoyeol Sohn) | 석사 (2026) | MS 2026 -> KAIST PhD (MACLab) |
| 이세인 (Sein Lee) | 석사 (2026) | MS 2026 -> KAIST PhD (MACLab) |
| 권대용 (Daeyong Kwon) | 석사 (2026) | MS 2026 -> Seoul National University PhD (Language and Data Intelligence Lab) |
| 김다빈 (Dabin Kim) | 석사 (2025) | MS 2025 -> Sony CSL Intern -> KAIST PhD (MACLab) |
| 김기락 (Kirak Kim) | 석사 (2025) | MS 2025 -> KAIST PhD (AIRIS Lab) |
| 방하연 (Hayeon Bang) | 석사 (2025) | MS 2025 -> KAIST PhD (MACLab) |
| 이준원 (Junwon Lee) | 석사 (2025) | MS 2025 -> KAIST PhD (MACLab) |
| Megan Finch | 석사 (2024) | MS 2024 -> Durham University PhD |
| 김용현 (Yonghyun Kim) | 석사 (2024) | MS 2024 -> Georgia Tech MS/PhD |
| 조혜윤 (Hyeyoon Cho) | 석사 (2024) | MS 2024 -> KAIST CTRI Researcher |
| 김종수 (Jongsoo Kim) | 석사 (2024) | MS 2024 -> KAIST PhD (MACLab) |
| Carolina Carusi | 석사 (2024) | MS 2024 -> KAIST PhD (MACLab) |
| 최재란 (Jaeran Choi) | 석사 (2024) | MS 2024 -> KAIST PhD (MACLab) |
| 정윤진 (Yoonjin Chung) | 석사 (2023) | MS 2023 (GSAI) -> Gaudio Lab (Researcher) -> NYU PhD |
| 박지윤 (Jiyun Park) | 석사 (2023) | MS 2023 -> KAIST PhD (MACLab) |
| 김현수 (Houn Su Kim) | 석사 (2023) | MS 2023 -> KAIST PhD (MACLab) |
| 김헤이븐 (Haven Kim) | 석사 (2023) | MS 2023 -> Sony CSL (Researcher) -> UC San Diego PhD |
| 이설희 (Seolhee Lee) | 석사 (2023) | MS 2023 -> NCSoft (Researcher) -> NC AI (Researcher) |
| 최영준 (Young June Choi) | 석사 (2022) | MS 2022 -> KAIST PhD (TXLab) |
| 임재권 (Jaekwon Im) | 석사 (2022) | MS 2022 -> KAIST PhD (MACLab) |
| 이경연 (Kyungyun Lee) | 석사 (2021) | MS 2021 -> Weverse -> Gaudio Lab -> Aalto University PhD |
| 김유진 (Yoojin Kim) | 석사 (2021) | MS 2021 -> Samsung Research -> Yonsei University Law School -> Lawyer |
| 김태완 (Taewan Kim) | 석사 (2020) | MS 2020 -> Neutune (Co-founder, Design Researcher) |
| 김원일 (Wonil Kim) | 석사 (2020) | MS 2020 -> KAIST PhD (MACLab) |
| 최민석 (Minsuk Choi) | 석사 (2020) | MS 2020 -> KAIST PhD (MACLab) |
| 최정 (Jeong Choi) | 석사 (2020) | MS 2020 -> NCSoft (AI Researcher) -> NAVER |
| 박채린 (Chaelin Park) | 석사 (2019) | MS 2019 -> LOTTE e-commerce (UX Designer) -> Elice (UX Designer) |
| 박승순 (Seungsoon Park) | 석사 (2018) | MS 2018 -> Neutune (Co-founder, Chief Creative Officer), KAIST PhD (MAC Lab) |
| 박지영 (Jiyoung Park) | 석사 (2018) | MS 2018 -> NAVER |
| 김태형 (Taehyoung Kim) | 석사 (2017) | MS 2017 -> Mediascope -> Neutune |
| 이장원 (Jangwon Lee) | 박사과정 (Former PhD Student) |  |
| 오창현 (Changheun Oh) | 박사과정 (Former PhD Student) |  |
| 박승순 (Seungsoon Park) | 박사과정 (Former PhD Student) |  |
| Daniel Bin Schmid | 방문 학생 | MS Student, TU Munich (visiting period: Oct 2024 - Jun 2025) |
| Zheng Xun Ng | 방문 학생 | Undergrad Student, Nanyang Technical University (visiting period: Aug 2023 - Jan 2024) |
| Yuya Yamamoto | 방문 학생 | PhD Student, Tsukuba University (visiting period: Aug 2022 - Dec 2022) |
| Guillaume Grannec | 방문 학생 | MS Student, Cnam-Enjmin (visiting period: Jul 2016 - Aug 2016) |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021년 이후 학술지·학회·워크숍 논문과 초록·데모 발표다. 괄호 안 수상은 랩 표기다.[^papers]

**2026**

- Hyemi Kim, Jiyun Park, Taegyun Kwon, Sein Lee, Sunjae Won, and Juhan Nam. "KRAISLER: A Multi-track Dataset of Piano and Violin Duet Recordings for MIR Research". *Transactions of the International Society for Music Information Retrieval*.
- Taejun Kim, Jongsoo Kim, Hyungyu Kim, Juhan Nam. "Raveform: A Dataset of DJ Mixes and Structure Annotations for EDM". *Transactions of the International Society for Music Information Retrieval*.
- Hayeon Bang, Hounsu Kim, Wonil Kim, and Juhan Nam. "VocalCoachBench: Benchmarking Audio-Language Models on Expert Feedback for Singing". *NeurIPS 2026 Evaluations and Datasets Track*.
- Jongsoo Kim, Woojin Kang, and Juhan Nam. "StemPrint: Stem-Aware Audio Fingerprinting Framework for Automatic Sample Identification". *Proceedings of the 18th Asia Pacific Signal and Information Processing Association Annual Summit and Conference*.
- Hyemi Kim, Jiyun Park, and Juhan Nam. "Phase-Based Onset-Enhancement for Piano Transcription in Ensemble Settings". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Sein Lee, Jiyun Park, and Juhan Nam. "STRAdi: Real-time Violin Transcription for Score Following". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Joonhyung Bae, Dawon Park, Taegyun Kwon, Yoon-Seok Choi, Hyeon Hur, Satoshi Obata, Shigeru Kai, Yohei Wada, Yu Takahashi, Akira Maezawa, Jaebum Park, Jonghwa Park, and Juhan Nam. "SKY Piano: A Multimodal Piano Performance Dataset". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Joonhyung Bae and Juhan Nam. "Pianoid: 3D Pianist Body Motion Generation from MIDI". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Danbinaerin Han, Wonil Kim, Seah Hong, Dongju Moon, Jaeok Lee, Jongpil Lee, Chaewon Kim, and Juhan Nam. "Gugak-VocalSet: A Multi-Genre Studio-Quality Dataset of Korean Traditional Singing with Sigimsae Annotations". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Yonghyun Kim, Hoyeol Sohn, Juhan Nam, and Alexander Lerch. "Multi-Task Multi-Frame Visual Piano Transcription". *Proceedings of the 27th International Society for Music Information Retrieval Conference*.
- Seungheon Doh, Bruno Sguerra, Sergio Oramas, Elena V. Epure and Juhan Nam. "LLM-as-a-Judge for Evaluating System Responses in Conversational Music Recommendation". *Proceedings of the 20th ACM Conference on Recommender Systems*.
- Dabin Kim, Junwon Lee, and Juhan Nam. "AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control". *Proceedings of the 27th INTERSPEECH Conference*.
- Hoyeol Sohn and Juhan Nam. "DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection". *Proceedings of the 27th INTERSPEECH Conference*.
- Hounsu Kim and Juhan Nam. "SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion". *Proceedings of the 27th INTERSPEECH Conference*.
- Yoonjeong Park, Jaekwon Im, and Juhan Nam. "Melody-Aware & Total Duration Preserving Singing Voice Editing with Flow Matching Infilling". *Proceedings of the 27th INTERSPEECH Conference*.
- Minsuk Choi, Dabin Kim, and Juhan Nam. "DDSP-based Neural Vehicle Sound Synthesis Conditioned on Driving Signals". *Proceedings of the Audio Engineering Society Conference on Automotive Audio (Best Student Paper Award)*.
- Seungheon Doh and Juhan Nam. "Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking". *ML for Audio Workshop, the International Conference on Machine Learning*.
- Jaeran Choi, Hikari Kuriyama, Gou Koutaki, and Juhan Nam. "Playing Together with a Semi-Automated Robotic Flute on a Gesture Cue Detection System". *Proceedings of the New Interfaces for Musical Expression*.
- Gyubin Lee, Junwon Lee, and Juhan Nam. "CounterFlow: A Two-Phase Inference-Time Sampling for Counterfactual Video Foley Generation". *The IEEE/CVF Conference on Computer Vision & Pattern Recognition, Sight and Sound Workshop*.
- Junwon Lee, Juhan Nam, and Jiyoung Lee. "Selva: Hear What Matters! Text-conditioned Selective Video-to-Audio Generation". *Proceedings of the IEEE/CVF Conference on Computer Vision & Pattern Recognition*.
- Daeyong Kwon, Seungheon Doh, and Juhan Nam. "ArtistMus: A Globally Diverse, Artist-Centric Benchmark for Retrieval-Augmented Music Question Answering". *Proceedings of the 15th biennial Language Resources and Evaluation Conference*.
- Seungheon Doh, Junghyun Koo, Marco A. Martínez-Ramírez, Woosung Choi, Wei-Hsiang Liao, Qiyu Wu, Juhan Nam, and Yuki Mitsufuji. "LLM2Fx-Tools: Tool Calling For Music Post-Production". *Proceedings of the 14th International Conference on Learning Representations*.
- Jihoo Jung, Ji-Hoon Kim, Doyeop Kwak, Junwon Lee, Juhan Nam, and Joon Son Chung. "UNMIXX: Untangling Highly Correlated Singing Voices Mixtures". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Hyunjae Kim, Juhan Nam, and Kyung Myun Lee. "Transferable Audio Lottery Tickets: Gradient Accumulation for Extreme Sparsity". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Eunjin Choi, Hounsu Kim, Hayeon Bang, Taegyun Kwon, and Juhan Nam. "D3PIA: A Discrete Denoising Diffusion Model for Piano Accompaniment Generation from Lead sheet". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Jaekwon Im and Juhan Nam. "SAGA-SR: Semantically and Acoustically Guided Audio Super-Resolution". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.

**2025**

- Junwon Lee, Jaekwon Im, Dabin Kim, and Juhan Nam. "Video-Foley: Two-Stage Video-To-Sound Generation via Temporal Event Condition For Foley Sound". *IEEE Transactions on Audio, Speech and Language Processing*.
- SeungHeon Doh, Jongpil Lee, Dasaem Jeong, and Juhan Nam. "Musical Word Embedding for Music Tagging and Retrieval". *IEEE Transactions on Audio, Speech and Language Processing*.
- Joonhyung Bae, Eunjin Choi, and Juhan Nam. "Cutting Kim: Playful Transgression Through VR Voice Interaction in Public Exhibition Contexts". *SIGGRAPH Asia 2025 Art Papers*.
- Wonil Kim, Hyeongseok Wi, Seungsoon Park, Taejun Kim, Sangeun Keum, Keunhyoung Kim, Taewan Kim, Jongmin Jung, Taehyoung Kim, Gaetan Guerrero, Mael Le Goff, Julie Po, Dongjoo Moon, Juhan Nam, and Jongpil Lee. "From Generation to Attribution: Music AI Agent Architectures for the Post-Streaming Era". *NeurIPS 2025 Workshop on AI for Music*.
- Seungheon Doh, Keunwoo Choi, and Juhan Nam. "Conversational Music Recommendation with LLM Tool Calling". *NeurIPS 2025 Workshop on AI for Music*.
- Seungheon Doh, Junghyun Koo , Marco A. Martínez-Ramírez , WeiHsiang Liao, Juhan Nam, and Yuki Mitsufuji. "Can Large Language Models Predict Audio Effects Parameters from Natural Language?". *Proceedings of the IEEE Workshop on Applications of Signal Processing to Audio and Acoustics*.
- Gyehun Go, Satbyul Han, Ahyeon Choi, Eunjin Choi, Juhan Nam, and Jeong Mi Park. "AImoclips: A Benchmark for Evaluating Emotion Conveyance in Text-to-Music Generation". *HCMIR25: 3rd Workshop on Human-Centric Music Information Research at ISMIR 2025*.
- Yonghyun Kim, Junhyung Park, Joonhyung Bae, Kirak Kim, Taegyun Kwon, Alexander Lerch, and Juhan Nam. "PianoVAM: A Multimodal Piano Performance Dataset". *Proceedings of the 26th International Society for Music Information Retrieval Conference*.
- Jiyun Park, Carlos Eduardo Cancino-Chacón, Suhit Chiruthapudi, and Juhan Nam. "Matchmaker: an Open Source Library for Real Time Piano Score Following and Systematic Evaluation". *Proceedings of the 26th International Society for Music Information Retrieval Conference*.
- Jaeran Choi, Taegyun Kwon, and Juhan Nam. "Predicting Flutist Onset Timing in Duet Performance: A Multimodal Analysis of Gesture and Breath Cues". *Proceedings of the 26th International Society for Music Information Retrieval Conference*.
- Hayeon Bang, Eunjin Choi, SeungHeon Doh, and Juhan Nam. "PianoBind: A Multi-modal Joint Embedding Model for Pop-piano Music". *Proceedings of the 26th International Society for Music Information Retrieval Conference*.
- Eunjin Choi, Hyerin Kim, Jiwoo Ryu, Juhan Nam, and Dasaem Jeong. "On the De-duplication of the Lakh MIDI dataset". *Proceedings of the 26th International Society for Music Information Retrieval Conference*.
- Yoonjin Chung, Pilsun Eu, Junwon Lee, Keunwoo Choi, Juhan Nam, Ben Sangbae Chon. "KAD: No More FAD! An Effective and Efficient Evaluation Metric for Audio Generation". *Workshop on Machine Learning for Audio, International Conference on Machine Learning*.
- Shangda Wu, Guo Zhancheng, Ruibin Yuan, Junyan Jiang, SeungHeon Doh, Gus Xia, Juhan Nam, Xiaobing Li, Feng Yu, Maosong Sun. "CLaMP 3: Universal Music Information Retrieval Across Unaligned Modalities and Unseen Languages". *The Annual Meeting of the Association for Computational Linguistics*.
- Hayeon Bang, Taegyun Kwon, and Juhan Nam. "Dialogue in the Resonance: a Piece for the Piano and the Real-time Automatic Music Transcription". *Proceedings of the International Computer Music Conference*.
- Jaeran Choi, Jiyun Park, and Juhan Nam. "ARGhost: Envisioning Sonic Heritage Preservation through AR Interactive Sound Design Game". *Proceedings of the International Symposium on Electronic Art*.
- Kirak Kim, Hyojin Kim, Youjin Choi, Juhan Nam, and Jeongmi Lee. "Designing VR Music Game for Stress Reduction". *Proceedings of the IEEE VR conference*.
- Geoffroy Peeters, Zafar Rafii, Magdalena Fuentes, Zhiyao Duan, Emmanouil Benetos, Juhan Nam, and Yuki Mitsufuji. "Twenty-Five Years of MIR Research: Achievements, Practices, Evaluations, and Future Challenges". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Hounsu Kim, Taegyun Kwon, and Juhan Nam. "D3RM: A Discrete Denoising Diffusion Refinement Model for Piano Transcription". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Jaekwon Im and Juhan Nam. "FlashSR: One-step Versatile Audio Super-resolution via Diffusion Distillation". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Sungyong Shin, HyeonBeom Yi, Junsuk Seo, Chi Yoon Jeong, Chang Hee Lee, Woohun Lee, and Juhan Nam. "Haptic Music Feedback through Audio Decomposition". *Demos in the ACM Symposium on User Interface Software and Technology*.
- Danbinaerin Han, Dasaem Jeong, and Juhan Nam. "Motive-level Analysis of Form-functions Association in Korean Folk Song". *Late Breaking Demo in the 26th International Society for Music Information Retrieval Conference*.
- Junhyung Park, Yonghyun Kim, Joonhyung Bae, Kirak Kim, Taegyun Kwon, Alexander Lerch, and Juhan Nam. "Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation". *Late Breaking Demo in the 26th International Society for Music Information Retrieval Conference*.
- Joonhyung Bae, Hyeyoon Cho, Kirak Kim, Dawon Park, Taegyun Kwon, Yoon-Seok Choi, Hyeon Hur, Shigeru Kai, Yohei Wada, Satoshi Obata, Akira Maezawa, Jaebum Park, Jonghwa Park, and Juhan Nam. "Designing a Multimodal Viewer for Piano Performance Analysis - a Pedagogy-First Approach". *Late Breaking Demo in the 26th International Society for Music Information Retrieval Conference*.

**2024**

- Taegyun Kwon, Dasaem Jeong, and Juhan Nam. "Towards Efficient and Real-Time Piano Transcription Using Neural Autoregressive Models". *IEEE/ACM Transactions on Audio*.
- Saebyul Park, Eunjin Choi, Jeounghoon Kim and Juhan Nam. "Mel2Word: A Text-based Melody Representation for Symbolic Music Analysis". *Music and Science*.
- Hayeon Bang, Eunjin Choi, Megan Finch, Seungheon Doh, Seolhee Lee, Gyeong-Hoon Lee, and Juhan Nam. "PIAST: A Multimodal Piano Dataset with Audio, Symbolic and Text". *Proceedings of the 3nd Workshop on NLP for Music and Spoken Audio*.
- Saebyul Park, Halla Kim, Jiye Jung, Juyong Park, Jeounghoon Kim, and Juhan Nam. "Quantitative Analysis of Melodic Similarity in Music Copyright Infringement Cases". *Proceedings of the 25th International Society for Music Information Retrieval Conference*.
- Seungheon Doh, Keunwoo Choi, Daeyong Kwon, Taesoo Kim, and Juhan Nam. "Music Discovery Dialogue Generation Using Human Intent Analysis and Large Language Model". *Proceedings of the 25th International Society for Music Information Retrieval Conference*.
- Gyubin Lee, Hounsu Kim, Junwon Lee and Juhan Nam. "CONMOD: Controllable Neural Frame-based Modulation Effects". *Proceedings of the International Conference on Digital Audio Effects (Best Paper Award)*.
- Haven Kim, Jongmin Jung, Dasaem Jeong, Juhan Nam. "K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling". *Proceedings of the Joint International Conference on Computational Linguistics, Language Resources and Evaluation*.
- Seungheon Doh, Minhee Lee, Dasaem Jeong, and Juhan Nam. "Enriching Music Descriptions with A Finetuned-LLM and Metadata for Text-to-Music Retrieval". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Yoonjin Chung, Junwon Lee, and Juhan Nam. "T-Foley: A Controllable Waveform-domain Diffusion Model for Temporal-event-guided Foley Sound Synthesis". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Wootaek Lim and Juhan Nam. "Enhancing Spatial Audio Generation with Source Separation and Channel Panning Loss". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Jaekwon Im and Juhan Nam. "DIFFRENT: A Diffusion Model for Recording Environment Transfer of Speech". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Jiyun Park, Sangeon Yong, Taegyun Kwon, and Juhan Nam. "A Real-time Lyrics Alignment System Using Chroma and Phonetic Features For Classical Vocal Performance". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Hounsu Kim, Soonbeom Choi, and Juhan Nam. "Expressive Acoustic Guitar Sound Synthesis With an Instrument-specific Input Representation and Diffusion Outpainting". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Yeonghyeon Lee, Inmo Yeon, Juhan Nam, and Joon Son Chung. "VoiceLDM: Text-to-speech with Environmental Context". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Jaeran Choi, Taegyun Kwon, Joonhyung Bae, Jiyun Park, Yonghyun Kim, Juhan Nam. "Real-time Flutist Gesture Cue Detection System for Auto-Accompaniment". *Late Breaking Demo in the 25th International Society for Music Information Retrieval Conference*.
- Jiyun Park, Carlos Cancino-Chacón, Taegyun Kwon, Juhan Nam. "Matchmaker: A Python library for Real-time Music Alignment". *Late Breaking Demo in the 25th International Society for Music Information Retrieval Conference*.
- Dabin Kim, Junwon Lee, Minseo Kim, Juhan Nam. "Pitch-ControlNet: Continuous Pitch Control for Monophonic Instrument Sound Generation". *Late Breaking Demo in the 25th International Society for Music Information Retrieval Conference*.

**2023**

- Zhiyao Duan, Peter van Kranenburg, Juhan Nam, Preeti Rao. "Editorial for TISMIR Special Collection: Cultural Diversity in MIR Research (Editorial)". *Transactions of the International Society for Music Information Retrieval*.
- Ilaria Manco, Benno Weck, SeungHeon Doh, Minz Won, Yixiao Zhang, Dmitry Bogdanov, Yusong Wu, Ke Chen, Philip Tovstogan, Emmanouil Benetos, Elio Quinton, György Fazekas, and Juhan Nam. "The Song Describer Dataset: a Corpus of Audio Captions for Music-and-Language Evaluation". *Workshop on Machine Learning for Audio, Neural Information Processing Systems*.
- Vanessa Tan, JungHyun Nam, Juhan Nam, and Junyong Noh. "Motion to Dance Music Generation using Latent Diffusion Model". *Proceedings of the SIGGRAPH Asia 2023 Technical Communications*.
- Eunjin Choi, Hyerin Kim, Juhan Nam, and Dasaem Jeong. "Teaching Chorale Generation Model to Avoid Parallel Motions". *Proceedings of the 16th International Symposium on Computer Music Multidisciplinary Research*.
- Seungheon Doh, Keunwoo Choi, Jongpil Lee and Juhan Nam. "LP-MusicCaps: LLM-Based Pseudo Music Captioning". *Proceedings of the 24th International Society for Music Information Retrieval Conference (Best Paper Award Nomination)*.
- Haven Kim, Kento Watanabe, Masataka Goto, and Juhan Nam. "A Computational Evaluation Framework for Singable Lyric Translation". *Proceedings of the 24th International Society for Music Information Retrieval Conference*.
- Eugene Hwang, Joonhyung Bae, Wonil Kim, Juhan Nam, and Jeongmi Lee. "Sense of Convergence: Exploring the Artistic Potential of Cross-modal Sensory Transfer in Virtual Reality". *Proceedings of the 22nd IEEE International Symposium on Mixed and Augmented Reality Poster*.
- Taejun Kim and Juhan Nam. "All-In-One Metrical And Functional Structure Analysis With Neighborhood Attentions on Demixed Audio". *Proceedings of the IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (Best Student Paper Award)*.
- Yuya Yamamoto, Juhan Nam, and Hiroko Terasawa. "PrimaDNN':A Characteristics-aware DNN Customization for Singing Technique Detection". *Proceedings of the 31st European Signal Processing Conference*.
- Saebyul Park and Juhan Nam. "The Language of Jazz: A Natural Language Processing-based Analysis of the Patterns and Vocabulary of Jazz Solo Improvisation". *Proceedings of the 17th International Conference on Music Perception and Cognition*.
- Seungheon Doh, Minz Won, Keunwoo Choi, and Juhan Nam. "Textless Speech-to-Music Retrieval Using Emotion Similarity". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Seungheon Doh, Minz Won, Keunwoo Choi, and Juhan Nam. "Toward Universal Text-to-Music Retrieval". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Hyemi Kim, Jiyun Park, Taegyun Kwon, Dasaem Jeong, and Juhan Nam. "A Study of Audio Mixing Methods for Piano Transcription in Violin-Piano Ensembles". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Sangeon Yong, Li Su, and Juhan Nam. "A Phoneme-informed Neural Network Model for Note-level Singing Transcription". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Seolhee Lee, Eunjin Choi, Joonhyung Bae, Hyerin Kim, Eita Nakamura, Dasaem Jeong, and Juhan Nam. "Bridging Audio and Symbolic Piano Data through a Web-Based Annotation Interface". *Late Breaking Demo in the 24th International Society for Music Information Retrieval Conference*.
- Taejun Kim and Juhan Nam. "DJ StructFreak: automatic DJ system built with Music Structure Embeddings". *Late Breaking Demo in the 24th International Society for Music Information Retrieval Conference*.
- Hyunjae Kim, Eunji Oh, Jieun Park, Yoonjin Chung, Juhan Nam and Kyung Myun Lee. "A Comparison of Melody Interpolation Performed by Human and Artificial Intelligence Based on Human Similarity Judgments". *Proceedings of the 17th International Conference on Music Perception and Cognition*.
- Taegyun Kwon, Dawon Park, Joonhyung Bae, Jonghwa Park, Jaebum Park, and Juhan Nam. "Automated Gap-filling Algorithm for Kinetic Data of Finger Movement: Pianist Hand Motion Cleaning Using Spatio-temporal Imputation". *Proceedings of the 29th Congress of International Society of Biomechanics*.
- Dawon Park, Taegyun Kwon, Joonhyung Bae, Jonghwa Park, Juhan Nam, and Jaebum Park. "Multivariate Kinematic Analysis of Piano Performance: a Case Study of a Professional Pianist". *Proceedings of the 29th Congress of International Society of Biomechanics*.

**2022**

- Eunjin Choi, Yoonjin Chung, Seolhee Lee, Jong Ik Jeon, Taegyun Kwon, and Juhan Nam. "YM2413-MDB : A Multi-Instrumental FM Video Game Music Dataset with Emotion Annotations". *Proceedings of the 23rd International Society for Music Information Retrieval Conference*.
- Yuya Yamamoto, Juhan Nam, and Hiroko Terasawa. "Analysis and Detection of Singing Techniques in Repertoires of J-POP Solo Singers". *Proceedings of the 23rd International Society for Music Information Retrieval Conference*.
- Jaekwon Im, Soonbeom Choi, Sangeon Yong, and Juhan Nam. "Neural Vocoder Feature Estimation for Dry Singing Voice Separation". *Proceedings of the 14th Asia Pacific Signal and Information Processing Association Annual Summit and Conference*.
- Taejun Kim, Juhan Nam. "Temporal Feedback Convolutional Recurrent Neural Networks for Speech Command Recognition". *Proceedings of the 14th Asia Pacific Signal and Information Processing Association Annual Summit and Conference*.
- Taesu Kim, SeungHeon Doh, Gyunpyo Lee, Hyung seok Jun, Juhan Nam, and Hyeon-Jeong Suk. "Hi, KIA: A Speech Emotion Recognition Dataset for Wake-Up Words". *Proceedings of the 14th Asia Pacific Signal and Information Processing Association Annual Summit and Conference*.
- Taejun Kim, Yi-Hsuan Yang, and Juhan Nam. "Joint Estimation of Fader and Equalizer Gains of DJ Mixers using Convex Optimization". *Proceedings of the International Conference on Digital Audio Effects*.
- Yuya Yamamoto, Juhan Nam, and Hiroko Terasawa. "Deformable CNN and Imbalance-Aware Feature Learning for Singing Technique Classification". *Proceedings of the 23rd INTERSPEECH Conference*.
- Sangeun Kum, Jongpil Lee, Keunhyoung Luke Kim, Taehyoung Kim, and Juhan Nam. "Pseudo-Label Transfer from Frame-Level to Note-Level in a Teacher-Student Framework for Singing Transcription from Polyphonic Music". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.
- Soonbeom Choi and Juhan Nam. "A Melody-Unsupervision Model for Singing Voice Synthesis". *Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing*.

**2021**

- Sarah Kim, Jeong Mi Park, Seungyeon Rhyu, Juhan Nam, Kyogu Lee. "Quantitative Analysis of Piano Performance Proficiency Focusing on Difference Between Hands". *PLOS ONE*.
- Leonardo Gabrielli, György Fazekas, and Juhan Nam. "Special Issue on Deep Learning for Applications in Acoustics: Modeling, Synthesis, and Listening (Editorial)". *Applied Sciences*.
- Yuya Yamamoto, Juhan Nam, Hiroko Terasawa, and Yuzuru Hiraga. "Investigating Time-Frequency Representations for Audio Feature Extraction in Singing Technique Classification". *Proceedings of the 13th Asia Pacific Signal and Information Processing Association Annual Summit and Conference*.
- Seungheon Doh, Junwon Lee, and Juhan Nam. "Music Playlist Title Generation: A Machine-Translation Approach". *Proceedings of the 2nd Workshop on NLP for Music and Spoken Audio*.
- Keunhyoung Kim, Jongpil Lee, Sangeun Kum, and Juhan Nam. "Learning a Cross-Domain Embedding Space of Vocal and Mixed audio with a Structure-Preserving Triplet Loss". *Proceedings of the 22nd International Society for Music Information Retrieval Conference*.
- Hsiao-Tzu Hung, Joann Ching, Seungheon Doh, Nabin Kim, Juhan Nam, and Yi-Hsuan Yang. "EMOPIA: A Multi-Modal Pop Piano Dataset For Emotion Recognition and Emotion-based Music Generation". *Proceedings of the 22nd International Society for Music Information Retrieval Conference*.
- Seungsoon Park, Jongpil Lee, Taewan Kim, Tae Hong Park, Joonhyung Bae, and Juhan Nam. "Mixed Scape: Development of Framework and Artwork for Auditory Correspondence in Mixed Reality". *Proceedings of International Computer Music Conference*.
- Taejun Kim, Yi-Hsuan Yang, and Juhan Nam. "Reverse-Engineering The Transition Regions of Real-World DJ Mixes using Sub-band Analysis with Convex Optimization". *Proceedings of the New Interfaces for Musical Expression*.
- SeungHeon Doh, Jongpil Lee, and Juhan Nam. "Million Song Search: Web Interface for Semantic Music Search Using Musical Word Embedding". *Late Breaking Demo in the 22nd International Society for Music Information Retrieval Conference*.
- Yoojin Kim, Jeongmi Park, Dasaem Jeong, Taegyun Kwon, Jonghwa Park, and Juhan Nam. "Emotion Classification and Analysis of Expressive Performances in Classical Piano Music". *Proceedings of the 16th International Conference on Music Perception and Cognition*.
- Ju-Sung Ham, Youjeong Hong, Jeongmi Park, Jonghwa Park, Juhan Nam, and Kyogu Lee. "Communication of Emotion Modified by the Performer in Classical Piano Pieces". *Proceedings of the 16th International Conference on Music Perception and Cognition*.
- Sarah Kim, Seungyeon Rhyu, Juhan Nam, and Kyogu Lee. "Correlation Analysis Between Both Hands and Musical Score for Quantitative Evaluation of Piano Performance". *Proceedings of the 16th International Conference on Music Perception and Cognition*.

## 연구 과제

랩 Research 페이지의 진행 중 과제와 지원 기관·기간이다.[^research]

- Real-Time Audio-Visual Music Information Processing for Interactive AI Performance System (지원 한국연구재단(National Research Foundation of Korea); 기간 2023–2027)
- Multimodal Piano Performance Dataset Collection and Motion Generation (지원 야마하(Yamaha); 기간 2023–2026)
- LLM for Music (지원 한국콘텐츠진흥원(KOCCA); 기간 2025–2027)
- Neural Audio Processing and Synthesis (지원 한국연구재단(National Research Foundation of Korea); 기간 2023–2026)

## 소식

랩 첫 화면 소식란의 2021년 이후 소식이다.[^home]

- 2026-07-31 · Minsuk received the Best Student Paper Award at the AES conference on Automotive Audio
- 2026-07-12 · Six papers were accepted to ISMIR 2026!
- 2026-07-10 · Prof. Nam gave an invited talk in the ICML 2026 ML for Audio Workshop
- 2026-06-28 · Dr. Seungheon Doh, Prof. Dasaem Jeong, and Prof. Nam were invited to the Dagstuhl Seminar on Open Music Data for Music Processing Research and had a great time!
- 2026-06-23 · Our lab members and Prof. Jieun Song's group visited the Neurocognition of Music and Language Research Group at MPI Emperical Aesthetics under the NRF Germany-Korean R&D Network Program
- 2026-06-18 · Our lab members and the KACES group visited IRCAM for collaboration research on a sound art education program for children
- 2026-03-30 · Prof. Nam gave a special talk to KAIST undergraduates, sharing his lifelong journey in music technology
- 2025-12-22 · Prof. Nam gave an invited lecture at the Central Conservatory of Music (CCoM) in China
- 2025-12-17 · We invited AIST researchers from Japan and hosted the International Symposium on Intelligent Sound: AI for Speech, Music, and Acoustics at KAIST
- 2025-12-10 · We hosted Dr. Douglas McCausland from CCRMA at Stanford University, who gave a talk titled "ENTANGLEMENT: Composing at the Intersection of Interface Design, Spatial Audio, and Intermedia."
- 2025-12-10 · Prof. Nam received an Outstanding Teaching Award from KAIST
- 2025-11-21 · Jiyun received an Outstanding Presentation Award at the Acoustical Society of Korea Conference
- 2025-11-13 · We visited Yamaha R&D in Yokohama for the midterm review of our industry project and had a wonderful time!
- 2025-11-02 · Prof. Nam appeared on the SBS television program "Sunday Special Documentary."
- 2025-10-22 · Our lab participated in the 2025 Asia-Pacific Performing Arts Centres (AAPPAC) General Assembly at the Daejeon Arts Center, where our performance team showcased an AI piano system and Prof. Nam joined a panel discussion
- 2025-09-21 · We proudly hosted the ISMIR 2025 conference at KAIST!
- 2025-09-19 · Prof. Meinard Müller and Dr. Stefan Balke from the International Audio Laboratories Erlangen (AudioLabs) visited our lab
- 2025-08-12 · A group of high school students participating in the KAIST Academic Program of the APEC Youth STEM Conference visited our lab
- 2025-07-07 · Technology from our industry project with Kakao Entertainment was deployed in Melon's new music recommendation service
- 2025-06-30 · Prof. Bo Li of the Jacobs School of Music at Indiana University and Prof. Sujin Kim of the School of Art at Carnegie Mellon University visited our lab and presented their research and artwork
- 2025-06-23 · Prof. Nam was promoted to full professor, effective September 2025!
- 2025-06-16 · Dr. Keunwoo Choi joined the KAIST Graduate School of Culture Technology as an adjunct professor!
- 2025-06-07 · Five papers were accepted to ISMIR 2025!
- 2025-05-28 · A group of students from the CN Yang Scholars Programme (CNYSP) at Nanyang Technological University (NTU), Singapore, visited our lab
- 2025-04-18 · Our AI Piano performance team gave a talk and performance at the 2025 World Science Culture Forum
- 2025-04-18 · We organized the inaugural symposium of the Korean Society for Music Informatics at KAIST
- 2025-04-15 · The Sumi Jo Performing Arts Research Center hosted jazz pianist Hayoung Lyou and Dr. Keunwoo Choi for a joint performance, artist talk, and research talk titled "Jazz Composition and Improvisation in Juxtaposition with Large Language Models."
- 2025-02-24 · Prof. Nam was appointed a KAIST Endowed Chair Professor for a three-year term
- 2025-02-07 · Our lab's music AI research was featured on KAIST's official YouTube channel
- 2025-01-22 · Dr. Yiğit Özer , who earned his PhD in Prof. Müller's group at AudioLabs and is now a research intern at Sony AI, visited our lab and presented his research
- 2024-12-12 · Wootaek and Seongheon successfully defended their PhD theses! Congratulations!
- 2024-09-28 · We participated in "KAISTxDaejeon Arts Center Performance Laboratory, X-Space" and organized the follow-up symposium
- 2024-09-07 · Our undergrad research student, Gyubin, with Hounsu and Junwon, received the Best Student Award at DAFx 2024!
- 2024-07-01 · Jiyun begins her summer internship at Yamaha R&D (Hamamatsu, Japan). Congratulations!
- 2024-06-05 · We showcase our AI performance systems with world-renowned soprano Sumi Jo (조수미) at Innovate Korea 2024
- 2024-06-04 · We received a gift fund from Adobe Research
- 2024-05-27 · Seungheon begins his summer internship at Adobe Research (San Francisco, US). Congratulations!
- 2024-05-20 · Dr. Minz Won, a research scientist at Suno, gave a talk on music representation learning in the GCT634 class
- 2024-04-22 · Prof. George Fazekas of Queen Mary University of London and Prof. Vipul Arora of IIT Kanpur visited our lab
- 2024-04-08 · Johannes Zeitler and Simon Schwär, two PhD students in Prof. Meinard Müller's group, visited our lab
- 2024-01-17 · Dr. Seung-Goo Kim of the Max Planck Institute for Empirical Aesthetics visited our lab and gave a talk on the neural encoding of musical emotions, jointly hosted with the Music and Brain Lab
- 2023-12-14 · Seven papers were accepted to ICASSP 2024!
- 2023-12-12 · Sangeon, Taegyun, and Taejun successfully defended their PhD theses! Congratulations!
- 2023-12-01 · We organized the International Symposium on AI and Music Performance (ISAIMP 2023) at KAIST
- 2023-11-05 · Seungheon's ISMIR paper has been nominated for the Best Paper Award at ISMIR 2023! Congratulations!
- 2023-10-22 · Taejun won the Best Student Paper at WASPAA 2023! Congratulations!
- 2023-10-10 · Our AI piano team participated in the Daejeon Arts Center's 20th-anniversary concert with flutist Jasmine Choi (최나경)
- 2023-09-22 · Hayeon and Yonghyun participated in the "Four Seasons 2050" concert project at KAIST
- 2023-08-23 · Three KAIST labs-MACLab, MuB Lab, and AIRIS Lab-visited Yamaha headquarters to participate in the joint KAIST–Yamaha workshop
- 2023-08-21/22 · Prof. Nam gave talks at the University of Tsukuba in Prof. Hiroko Terasawa's lab and at AIST in Dr. Masataka Goto's group
- 2023-08-11 · We invited Hanoi Hantrakul of ByteDance to KAIST, where he gave a talk titled "Transcultural Machine Learning in Music."
- 2023-07-31 · Seungheon received the Kim Young Han Global Scholarship
- 2023-07-20 · We participated in the Music and Audio Workshop 2023
- 2023-06-28 · Our AI Piano Team showcased an AI-based performance system with world-renowned soprano Sumi Jo (조수미)
- 2023-06-21 · Two papers were accepted to ISMIR 2023!
- 2023-06-19 · Prof. Nam gave a keynote speech at the Yamaha Global R&D Meetup 2023
- 2023-05-09 · Prof. Nam was appointed an associate editor of the IEEE/ACM Transactions on Audio, Speech, and Language Processing
- 2023-02-16 · Four papers were accepted to ICASSP 2023!
- 2022-12-13 · Saebyul and Soonbeom successfully defended their PhD theses! Saebyul received recognition from the media
- 2022-11-19 · Prof. Nam gives an invited talk at the Korean Society for Posthuman Studies (한국포스트휴먼연구회)
- 2022-11-11 · Joonhyung Bae (PhD student) and Seolhee Lee (MS student) were invited to the "Unfold X" exhibition
- 2022-11-02 · Prof. Nam gave an invited talk at the International Copyright Technology Conference 2022
- 2022-08-22 · Yuya Yamamoto , a PhD student at the University of Tsukuba, joined our lab as a visiting student for four months
- 2022-07-14 · Two papers were accepted to ISMIR 2022!
- 2022-06-01 · Seungheon Doh, a PhD student, began a visiting research appointment at the NYU Center for Data Science under the supervision of Prof. Kyunghyun Cho
- 2022-05-24 · Joonhyung Bae (PhD student) and Seolhee Lee (MS student) won the CHI 2022 Student Game Competition!
- 2022-05-13 · Sumi Jo Performing Arts Research Center Opens​
- 2022-05-02 · Eunjin Choi, a PhD student, received an NC Scholarship
- 2022-04-15 · The KAIST and Sogang piano performance research team participates in the Daejeon Arts Center 2022 Spring Festival Music, Haydn Avent
- 2022-02-20 · Prof. Nam participated in the Dagstuhl Seminar on "Deep Learning and Knowledge Integration for Music Audio Analysis" as a co-organizer
- 2022-01-22 · Two papers were accepted to ICASSP 2022!
- 2022-01-06 · Our AI pianist "VirtuosoNet" accompanied Soprano Sumi Jo (Distinguished Visiting Professor at KAIST) during the Special Concert at KAIST
- 2021-11-17 · Prof. Nam gives a keynote talk on "Deep Learning for Expressive Piano Performance Rendering" at the Workshop on AI in Music and Live Concert in conjunction with the 4th IEEE Artificial Intelligence & Virtual Reality
- 2021-11-12 · Prof. Nam gives an invited talk on "Music Auto-Tagging: From Audio Classification To Word Embedding" at the 2nd Workshop on NLP4MusA
- 2021-07-28 · Prof. Nam gives a special talk on "AI for Classical Music Performance" at the Asia Culture Center
- 2021-07-07 · Our lab alumnus Dr. Dasaem Jeong will be joining Art & Technology at Sogang University as an assistant professor. Congratulations!
- 2021-06-08 · Media art exhibition, "Game and Art: Auguries of Fantasy", is open. The exhibition was co-organized by KAIST and Daejeon Museum of Art and was supported by NCSoft and the Korea Creative Content Agency
- 2021-04-01 · Saebyul Park (PhD stuent) is introduced in Science Dong-A (과학 동아), a science magazine in Korea,
- 2021-04-01 · An interview article with Prof. Nam is introduced in Auditorium (객석), a performing arts magazine in Korea.
- 2021-03-20 · Prof. Nam has been appointed as an associate editor of the Journal of Audio Engineering Society
- 2021-02-17 · Prof. Nam has received an international joint research award in commemoration of the 50th Anniversary of KAIST
- 2021-02-16 · Our AI Pianist, VirtuosoNet, performs with pianist Jong Hwa Park in the 50th anniversary ceremony of KAIST
- 2021-02-05 · Prof. Nam serves as a scientific program co-chair of ISMIR 2021
- 2021-01-06 · The Applied Sciences special issue titled "Deep Learning for Applications in Acoustics: Modeling, Synthesis, and Listening" has been published (Prof. Juhan Nam served as a guest editor)

## 연락과 위치

- 연구실: 대전 KAIST N25 3236호[^home]

[^home]: MACLab 누리집 첫 화면(소식 포함) <https://mac.kaist.ac.kr/> (2026-10-20 열람)
[^people]: MACLab People 페이지 <https://mac.kaist.ac.kr/people.html> (2026-10-20 열람)
[^research]: MACLab Research 페이지 <https://mac.kaist.ac.kr/research.html> (2026-10-20 열람)
[^papers]: MACLab 논문 목록 <https://mac.kaist.ac.kr/pubs.html> (2026-10-20 열람)
[^prof]: 남주한 교수 개인 페이지 <https://mac.kaist.ac.kr/~juhan/> (2026-10-20 열람)
[^p1]: S. Doh, K. Choi, J. Lee, J. Nam, Proceedings of the 24th International Society for Music Information Retrieval Conference (2023). <https://arxiv.org/abs/2307.16372> 초록 기준(arXiv 판).
[^p2]: S. Doh, J. Lee, D. Jeong, J. Nam, IEEE Transactions on Audio, Speech and Language Processing 33, 2377-2387 (2025). <https://doi.org/10.1109/taslpro.2025.3577408> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Doh 외, J. Nam, Proceedings of the 25th International Society for Music Information Retrieval Conference (2024). <https://arxiv.org/abs/2411.07439> 초록 기준(arXiv 판).
[^p4]: J. Lee, J. Im, D. Kim, J. Nam, IEEE Transactions on Audio, Speech and Language Processing 33, 3813-3825 (2025). <https://doi.org/10.1109/taslpro.2025.3597477> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: G. Lee, H. Kim, J. Lee, J. Nam, Proceedings of the International Conference on Digital Audio Effects (2024). <https://arxiv.org/abs/2406.13935> 초록 기준(arXiv 판).
[^p6]: T. Kwon, D. Jeong, J. Nam, IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, 5106-5116 (2024). <https://doi.org/10.1109/taslp.2024.3507568> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Y. Kim 외, J. Nam, Proceedings of the 26th International Society for Music Information Retrieval Conference (2025). <https://arxiv.org/abs/2509.08800> 초록 기준(arXiv 판).
[^p8]: T. Kim, J. Nam, 2023 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), 1-5 (2023). <https://doi.org/10.1109/waspaa58266.2023.10248148> 초록 기준(Semantic Scholar 등록 초록).

# Machine Learning and Intelligence Lab (MLILAB)

**KAIST 김재철AI대학원 · 양은호 부교수**

- 분야: 기계학습 알고리즘, 영상·언어 이해, 생성 모형, 의료 자료의 계산 방법[^home][^profile]
- 대분야: 컴퓨팅·AI
- 태그: 생성 인공지능[^profile], 연합학습·분산 학습[^p5], 그래프 기계학습·지식 그래프[^p6][^p7]
- 홈페이지: <https://mli.kaist.ac.kr>
- 근거와 출처: [MLILAB 근거 페이지](mli-sources.md)

> 자료에서 규칙을 배우는 방법을 연구하고, 영상과 글을 함께 이해하는 모형, 영상 생성·편집, 의료 자료를 처리하는 계산 방법으로 연결하는 연구실이다.

## 무엇을 연구하나

MLILAB은 기계학습(자료로부터 규칙이나 관계를 배워 작업 수행을 개선하는 계산 방법)을 연구한다. 첫 화면은 기계학습 알고리즘(자료에서 규칙을 배우도록 정해진 계산 절차), 멀티모달 학습(영상·글·소리처럼 종류가 다른 자료를 함께 배우는 방법), 대형 언어 모델(많은 글을 학습해 글을 이해하고 생성하는 계산 모형), 컴퓨터 비전(사진·영상의 내용이나 구조를 컴퓨터로 알아내는 기술), 의료를 위한 기계학습을 연구 갈래로 제시한다.[^home] 양은호 교수는 통계적 기계학습과 고차원 통계(변수가 많은 자료의 분석과 추정을 다루는 통계 분야), 다양한 학습 알고리즘을 연구하며 최근에는 생성 모형(자료가 나타나는 확률적 규칙을 나타내고 새 자료를 만드는 계산 모형)에 초점을 둔다고 소개한다.[^profile]

첫째는 **영상과 글이 맞게 연결되는지 살피는 연구**다. 대표 논문 1은 영상 언어 모형(이미지와 글을 함께 처리하는 계산 모형)이 이미지에 없는 대상을 질문에 나왔다는 이유로 있다고 취급하는 문제를 다룬다. 모형 내부에서 대상의 부재를 나타내는 반응을 찾아 검출부를 만들고, 그 결과에 따라 질문을 다시 해석하거나 생성 중인 낱말을 바꾸는 방법을 제안했다.[^p1]

둘째는 **언어 모형의 학습 비용과 안전성**이다. 대표 논문 2는 지식 증류(교사 모형의 출력이나 내부 표현을 학생 모형이 따르도록 학습시키는 방법)를 다룬다. 교사 전체를 다시 학습시키는 대신 학생의 안내에 따라 프롬프트(모형의 작업 방향을 정하는 입력)를 조정해 학생이 배우기 좋은 지식을 전달한다.[^p2] 대표 논문 3은 안전 정렬(모형의 출력을 안전 기준에 맞추는 학습)이 낯선 형태의 입력에서 실패하는 문제를 분석하고, 유해한 입력의 표현을 바꾸어 그 취약성을 시험하는 방법을 제안했다.[^p3]

셋째는 **영상 생성·편집과 분산된 자료의 학습**이다. 대표 논문 4는 얼굴 영상에서 인물의 정체성과 움직임에 해당하는 특징(자료를 구별하고 학습에 사용하는 속성이나 표현)을 분리하고, 시간에 따라 달라지지 않는 특징을 조정해 장면 사이 편집의 일관성을 유지한다.[^p4] 대표 논문 5는 연합학습(여러 참여자가 각자의 자료를 보관하면서 모형 학습 결과를 교환하는 방법) 환경에서 확산 모형(잡음으로 변형된 자료를 복원하는 과정을 배워 자료를 생성하는 모형)을 학습하는 알고리즘을 제안했다. 민감한 자료를 나누어 가진 환경에서 이미지 생성 품질과 자료 보호를 함께 다룬다.[^p5]

넷째는 **관계가 있는 자료에서 배우고 예측의 확신을 보정하는 연구**다. 그래프(대상과 그 사이의 관계를 점과 선으로 나타낸 구조)는 크기와 연결 방식이 일정하지 않아 학습 자료를 섞기 어렵다. 대표 논문 6은 중요한 부분 구조를 골라 서로 다른 그래프를 섞고, 그 내용에 맞게 정답을 조정하는 자료 증강(기존 자료를 변형하거나 조합해 학습 자료를 만드는 방법)을 제안했다.[^p6] 대표 논문 7은 이웃 점들의 예측 유사성과 각 점의 확신 수준을 함께 사용해 점들을 묶고, 묶음마다 예측의 확신과 실제 정답률이 맞도록 보정하는 방법을 제안했다.[^p7]

다섯째는 **의료 영상에서 부족한 시간 정보를 계산하는 연구**다. 대표 논문 8은 시간에 따라 변하는 입체 영상 사이에 들어갈 영상을 만드는 보간(알고 있는 값 사이의 값을 추정하는 계산)을 다룬다. 중간 시점의 정답 영상을 주지 않고도 보간을 학습하는 틀을 제안해, 자료가 제한된 의료 영상의 시간 변화를 다루었다.[^p8] 최근 논문에는 병변(질병으로 변한 조직의 부위)의 영역을 지시에 따라 나누는 방법, 전자의무기록(의료기관이 전자 형태로 관리하는 진료 기록)에서 연구 대상과 특징을 추출하는 자동화 체계도 있다.[^lesion][^emr]

## 주요 연구 주제

### 1. 영상과 언어의 연결

이미지에 없는 대상에 대한 잘못된 응답을 검출하고 수정하는 방법이다. 대표 논문 1.[^p1]

### 2. 언어 모형의 효율과 안전

학생 모형에 맞춘 지식 전달과 안전 기준을 벗어나는 입력에 대한 취약성 분석이다. 대표 논문 2, 3.[^p2][^p3]

### 3. 영상 생성·편집과 분산 학습

얼굴 영상의 특징 분리와 일관된 편집, 분산된 민감 자료로 생성 모형을 학습하는 방법이다. 대표 논문 4, 5.[^p4][^p5]

### 4. 그래프 학습과 예측 보정

부분 구조를 섞어 학습 자료를 만드는 방법과 그래프 예측의 확신을 보정하는 방법이다. 대표 논문 6, 7.[^p6][^p7]

### 5. 의료 영상과 기록의 계산 방법

중간 영상 없이 시간 보간을 학습하는 방법, 지시 기반 영상 분할과 의료 기록의 구조화 방법이다. 대표 논문 8.[^p8][^lesion][^emr]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 영상·언어 이해, 언어 모형, 영상 생성, 그래프 학습, 의료 영상의 계산 방법을 고르게 보여 주는 논문을 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://doi.org/10.18653/v1/2025.emnlp-main.1092) · EMNLP | 이미지에 없는 대상을 있다고 답하는 현상을 모형 내부의 반응으로 검출한다. 검출 결과를 이용해 질문을 다시 해석하거나 출력 중인 낱말을 바꾸어 잘못된 응답을 줄였다.[^p1] | 1저자 Sohee Kim, 마지막 저자 Eunho Yang |
| 2 | 2024 | [PromptKD: Distilling Student-Friendly Knowledge for Generative Language Models via Prompt Tuning](https://doi.org/10.18653/v1/2024.findings-emnlp.364) · Findings of EMNLP | 교사의 지식을 학생 모형이 배우기 좋은 형태로 전달한다. 교사 전체를 다시 학습시키지 않고 학생의 안내에 따라 소량의 프롬프트만 조정해 지식을 전달했다.[^p2] | 1저자 Gyeongman Kim, 마지막 저자 Eunho Yang |
| 3 | 2025 | [Playing the Fool: Jailbreaking LLMs and Multimodal LLMs with Out-of-Distribution Strategy](https://doi.org/10.1109/cvpr52734.2025.02786) · CVPR | 유해한 질문의 표현이 안전 학습에서 본 형태를 벗어나면 모형이 악의적 의도를 판단하기 어려워지는 취약성을 조사했다. 글이나 이미지의 표현을 변형하는 시험 틀을 제안하고 여러 언어·영상 언어 모형에서 확인했다.[^p3] | 1저자 Joonhyun Jeong, 마지막 저자 Eunho Yang |
| 4 | 2023 | [Diffusion Video Autoencoders: Toward Temporally Consistent Face Video Editing via Disentangled Video Encoding](https://doi.org/10.1109/cvpr52729.2023.00590) · CVPR | 얼굴 영상의 인물 정체성과 움직임을 분리해 표현한다. 시간에 따라 유지되는 특징을 조정하여 영상의 장면 사이에서 편집 내용이 일관되도록 했다.[^p4] | 1저자 Gyeongman Kim, 마지막 저자 Eunho Yang |
| 5 | 2025 | [VQ-FedDiff: Federated Learning Algorithm of Diffusion Models with Client-Specific Vector-Quantized Conditioning](https://doi.org/10.1109/tpami.2025.3602282) · IEEE TPAMI | 각 기관이나 기기가 민감한 자료를 따로 가진 상태에서 확산 모형을 함께 학습하는 알고리즘을 제안했다. 자료 분포가 같은 경우와 다른 경우에 이미지 생성 성능을 평가하고 자료 보호를 함께 다뤘다.[^p5] | 1저자 Tehrim Yoon, 마지막 저자 Eunho Yang |
| 6 | 2022 | [Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure Preservation](https://doi.org/10.1609/aaai.v36i7.20767) · AAAI | 크기와 연결 방식이 다른 그래프에서 중요한 부분 구조를 골라 섞어 학습 자료를 만든다. 섞인 부분에 맞게 정답도 조정하며 여러 그래프 분류 자료에서 방법을 평가했다.[^p6] | 1저자 Joonhyung Park, 마지막 저자 Eunho Yang |
| 7 | 2025 | [Towards Precise Prediction Uncertainty in GNNs: Refining GNNs with Topology-grouping Strategy](https://doi.org/10.1609/aaai.v39i19.34239) · AAAI | 이웃의 예측이 비슷해도 각 점의 확신 수준에 따라 오차가 달라지는 문제를 다룬다. 두 조건으로 점들을 묶고 묶음별로 확신을 보정해 예측의 불확실성을 조정했다.[^p7] | 1저자 Hyunjin Seo, 마지막 저자 Eunho Yang |
| 8 | 2024 | [Data-Efficient Unsupervised Interpolation Without Any Intermediate Frame for 4D Medical Images](https://doi.org/10.1109/cvpr52733.2024.01079) · CVPR | 시간에 따라 변하는 입체 의료 영상에서 중간 시점의 정답 영상 없이 보간을 배우는 틀을 제안했다. 제한된 자료를 사용하는 조건에서도 기존 보간 방법들과 성능을 비교했다.[^p8] | 1저자 JungEun Kim, 마지막 저자 Eunho Yang |

## 교수와 전문 분야

양은호 교수는 KAIST 김재철AI대학원 부교수이며, 연구실 소개에는 전산학부 소속도 함께 적혀 있다. 대학원 명단은 KAIST 석좌교수라는 칭호를 함께 적는다.[^faculty][^profile] 2016년 여름 KAIST에 부임하기 전 IBM T. J. Watson Research Center에서 연구원으로 근무했고, 2014년 University of Texas at Austin에서 박사학위를 받았다. 서울대학교에서 2006년 석사, 2004년 학사학위를 받았다.[^profile]

교수 소개의 전문 분야는 통계적 기계학습, 고차원 통계, 다양한 기계학습 알고리즘과 생성 모형이다.[^profile] 대표 논문은 영상과 글의 연결, 언어 모형의 지식 전달·안전성, 영상 편집과 연합학습, 그래프 자료의 학습·예측 보정, 의료 영상의 시간 보간으로 그 연구를 보여 준다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 구성원

2026년 11월 9일 연구실 People 쪽에 게시된 현재 구성원 32명이다. 박사후연구원 1명, 박사과정 15명, 석사과정 7명과 Part-Time (Industrial) 구획 5명, KT-AI Corporate Scholarship 구획 4명이다. 시작 시기와 연구 주제는 게시 표기이며, 뒤 두 구획의 학위과정은 따로 정하지 않는다.[^people] 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Junhyeok Choi | 박사후연구원 | Since Fall 2026 | Efficient Deep Learning, Tabular Foundation Models | cjunh4810@kaist.ac.kr |  |
| Hangyul Yoon | 박사과정 | Since Spring 2022 | Medical Deep Learning, Multimodal Learning | hangyulmd@mli.kaist.ac.kr | 8 |
| Sihwan Park | 박사과정 | Since Fall 2022 | Self-Supervised Learning, Graph Neural Networks, Generalization in Deep Learning | psh150204@kaist.ac.kr |  |
| Yoonjeon Kim | 박사과정 | Since Spring 2023 | Image/Video Manipulation, Motion Transfer | yoonkim313@kaist.ac.kr |  |
| Heecheol Yun | 박사과정 | Since Fall 2023 | LLM Ensemble, World model | yoon6503@kaist.ac.kr |  |
| Minyeong Hwang | 박사과정 | Since Fall 2023 | Generative Models, Self-Supervised Learning | myhwang99@kaist.ac.kr |  |
| Sohee Kim | 박사과정 | Since Spring 2024 | Multimodal Learning, Video Understanding | joyhee@kaist.ac.kr | 1 |
| Doohyuk Jang | 박사과정 | Since Fall 2024 | Natural Language Processing | jadohu@kaist.ac.kr | 2 |
| Soohyun Ryu | 박사과정 | Since Fall 2024 | Vision-Language Models, Multimodal reasoning | rsoohyun@kaist.ac.kr | 1 |
| Donghyeon Cho | 박사과정 | Since Spring 2025 | Generative Models, Diffusion Models, Computer Vision |  |  |
| Hyeongwon Jang | 박사과정 | Since Fall 2025 | Time Series Analysis, Natural Language Processing | janghw0911@kaist.ac.kr |  |
| Joowon Kim | 박사과정 | Since Fall 2025 | Multimodal Reasoning, World Models, Physical AI | kjwispro@kaist.ac.kr |  |
| Haechan Kim | 박사과정 | Since Spring 2026 | AutoResearch, Agentic RL, Reinforcement Learning with Verifiable Reward | kim.haechan@kaist.ac.kr |  |
| Seokhan Lee | 박사과정 | Since Spring 2026 | Large Language Models, Agents, AI Safety and Alignment | shlee_2@kaist.ac.kr |  |
| Jongheon Kim | 박사과정 | Since Spring 2025 | Natural Language Processing, Decision Making Under Uncertainty | jongheon@kaist.ac.kr |  |
| Uigyu Kim | 박사과정 | Since Spring 2025 | Natural Language Processing, Large Language Models | uigyu@kaist.ac.kr |  |
| Joonhyun Jeong | Part-Time (Industrial) | Since Fall 2024 | Computer Vision, Vision-Language Models | joonhyun.jeong@mli.kaist.ac.kr | 3 |
| Kwanhyung Lee | Part-Time (Industrial) | Since Fall 2024 | Time Series Data, Tabular Data, Medical Deep Learning, Multimodal Learning | kwanlee9209@mli.kaist.ac.kr |  |
| Jinbae Im | Part-Time (Industrial) | Since Spring 2026 | Multimodal Large Language Models / Data Selection | jinbae.im@kaist.ac.kr |  |
| Junghyun Lee | Part-Time (Industrial) | Since Spring 2026 | LLM/VLM Efficiency | onliwad101@kaist.ac.kr |  |
| Wooseok Han | Part-Time (Industrial) | Since Fall 2026 | LLM Agents, Speech AI | wooseok@kaist.ac.kr |  |
| Gyouk Chu | 석사과정 | Since Spring 2025 | LLM RL, Superintelligence, Self-Evolving AI | kyouwook@kaist.ac.kr |  |
| Hyun Ryu | 석사과정 | Since Spring 2025 | LLM reasoning and argumentation | ryuhyun1905@kaist.ac.kr |  |
| Thanh-Long V. Le | 석사과정 | Since Spring 2025 | Reinforcement Learning for Foundation Models | thanhlong0780@kaist.ac.kr |  |
| Yoonsik Park | 석사과정 | Since Spring 2026 | Multimodal Learning, Reliable AI | yoonsik.park@kaist.ac.kr |  |
| Seungho Shin | 석사과정 | Since Fall 2026 | World Models, Agentic AI | ssh9918@kaist.ac.kr |  |
| Seungwan Cho | 석사과정 | Since Fall 2026 | Large Language Models, Model Compression | scho0202@kaist.ac.kr |  |
| Kiung Yang | 석사과정 | Since Spring 2026 | Natural Language Processing, Multimodal Learning | 33kyang@kaist.ac.kr |  |
| Sungmin Jo | KT-AI Corporate Scholarship | Since Spring 2025 | Large Language Models, Multimodal Reasoning | ead3070@kaist.ac.kr |  |
| Yuchan Jung | KT-AI Corporate Scholarship | Since Spring 2025 | Multimodal Reasoning, Knowledge Distillation | yuchan@kaist.ac.kr |  |
| Inki Park | KT-AI Corporate Scholarship | Since Spring 2026 | Large Language Models, Trustworthy AI | inkey.park@kaist.ac.kr |  |
| Hangyeol Jung | KT-AI Corporate Scholarship | Since Fall 2026 | Mechanistic Interpretability, Superintelligence | han.jung@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 11월 9일 People 쪽의 Alumni 구획에 게시된 박사후연구원 3명, 박사 10명, 석사 24명이다. 학위·과정, 연도, 진로는 연구실이 게시한 표기다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Bokyeong Kim | PostDoc's (2020) | Nota AI |
| Kyungsu Kim | PostDoc's (2020) | Assistant Professor, Seoul National University |
| Myeongho Jeon | PostDoc's (2026) | Samsung Electronics DS |
| Sung-Yub Kim | Ph.D. in AI (2024) | SAIT |
| Hajin Shim | Ph.D. in AI (2024) | SAIT |
| Tehrim Yoon | Ph.D. in AI (2024) | Postdoctoral Researcher at Baylor College of Medicine |
| Geondo Park | Ph.D. in AI (2025) | KB Kookmin Bank AI |
| Gyeongman Kim | Ph.D. in AI (2025) | KRAFTON |
| Jihun Yun | Ph.D. in AI (2025) | KRAFTON |
| June Yong Yang | Ph.D. in AI (2025) | LG AI Research |
| Jaeyun Song | Ph.D. in AI (2026) | KRAFTON |
| Yeonsung Jung | Ph.D. in AI (2026) |  |
| Joonhyung Park | Ph.D. in AI (2025) | Assistant Professor, Kyung Hee University |
| Youngki Hong | M.S. in CS (2019) | NAVER Cloud |
| Ingyo Chung | M.S. in CS (2020) | CryptoQuant |
| Joonyoung Yi | M.S. in CS (2020) | HYPERCONNECT |
| Wonjun Chung | M.S. in CS (2020) | LINE Plus |
| Yongsu Baek | M.S. in CS (2021) | HYPERCONNECT |
| Juhyuk Lee | M.S. in AI (2021) | Samsung Research |
| Soonwoo Kwon | M.S. in AI (2021) | Riiid |
| Eunhyouk Shin | M.S. in AI (2022) | HYPERCONNECT |
| Seohui Bae | M.S. in AI (2022) | LG AI Research |
| Sumin Shin | M.S. in AI (2022) | LINE Plus |
| Jonghoon Shin | M.S. in AI (2023) | KT DS |
| Youngho Jeong | M.S. in AI (2023) | RideFlux |
| Changhun Kim | M.S. in AI (2024) | Ph.D. Student at UW–Madison |
| Hyunjin Seo | M.S. in AI (2024) | Ph.D. Student at KAIST |
| JungEun Kim | M.S. in AI (2024) | General Robotics |
| Kyusung Seo | M.S. in AI (2024) | LINE Plus |
| Seungyeon Woo | M.S. in AI (2024) | Skelter Labs |
| Taewon Kim | M.S. in AI (2024) | Ph.D. Student at KAIST |
| Will Arnold | M.S. in AI (2025) | NVIDIA |
| Chanjae Park | M.S. in AI (2026) |  |
| Gilhyun Nam | M.S. in AI (2026) |  |
| Jina Kim | M.S. in AI (2026) | KT AI |
| MinTaek Oh | M.S. in AI (2026) | KT AI |
| Seyun Bae | M.S. in AI (2026) | KT AI |

## 최근 논문 목록 (2021–2026)

연구실 Publications 쪽의 2021–2026년 구역에서 옮긴 89편이다. 연도·제목·저자·발표처는 연구실 표기를 따른다. 별표와 공동 기여 표기는 연구실이 적은 표시다. 날짜가 확인되는 2021년 논문은 2021년 10월 13일부터의 범위를 적용하고, 연도만 있는 항목은 해당 연도 구역에 둔다.[^pubs][^dates] DOI(Digital Object Identifier, 온라인 자료를 구별하는 고유 식별자)는 대응 논문의 등록 식별자다.[^oa] 소식에서 채택을 알린 항목 중 출판 기록 대신 채택 사실을 나타내는 항목은 「채택」, 나머지 발표처 표시는 「연구실 기재」로 구분했다. 같은 제목이 학회와 워크숍에 각각 게시되어 있으면 각각의 발표 항목으로 적는다.

**2026**

- Joowon Kim\*, Seungho Shin\*, Joonhyung Park, Eunho Yang (\*: equal contribution). "CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models". *Conference on Neural Information Processing Systems (NeurIPS) (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2605.08735>.
- Jangho Choi, Seongho Kim, Jaehyun Choi, Dahye Kim, Sungwon Yi, Eunho Yang. "Stability-Weighted Direction Regularization Disentangles Generator Shortcuts from Detection Signal". *Conference on Neural Information Processing Systems (NeurIPS) (연구실 기재)*.
- Kwanhyung Lee\*, Sungsoo Hong\*, Joonhyung Park, Jeonghyeop Lim, Juhwan Choi, Donghwee Yoon, Eunho Yang  (\*: equal contribution). "EMR-AGENT: An LLM Agent Framework for Cohort and Feature Extraction from Heterogeneous EHR Databases". *Conference on Empirical Methods in Natural Language Processing (EMNLP) (findings) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2510.00549>.[^emr]
- Doohyuk Jang\*, Yoonjeon Kim\*, Chanjae Park, Hyun Ryu, Eunho Yang  (\*: equal contribution). "Reasoning Model is Stubborn: Diagnosing and Mitigating Reasoning Rigidity in Large Language Models". *Conference on Empirical Methods in Natural Language Processing (EMNLP) (findings) (채택)*.
- Hyun Ryu, Doohyuk Jang, Hyemin S. Lee, Joonhyun Jeong, Gyeongman Kim, Donghyeon Cho, Gyouk Chu, Minyeong Hwang, Hyeongwon Jang, Changhun Kim, Haechan Kim, Jina Kim, Joowon Kim, Yoonjeon Kim, Kwanhyung Lee, Chanjae Park, Heecheol Yun, Gregor Betz, Eunho Yang. "ReviewScore: Misinformed Peer Review Detection with Large Language Models". *Conference on Empirical Methods in Natural Language Processing (EMNLP) (findings) (채택)*.
- Haechan Kim, Soohyun Ryu, Gyouk Chu, Doohyuk Jang, Eunho Yang. "Discounted Beta-Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards". *International Conference on Machine Learning (ICML) (채택)*.
- Jung Hyun Lee, June Yong Yang, Jungwook Choi, Eunho Yang. "LFQ: Logit-aware Final-block Quantization for Boosting the Generation Quality of Low-Bit Quantized LLMs". *International Conference on Machine Learning (ICML) (채택)*.
- Ziseok Lee\*, Minyeong Hwang\*, Sanghyun Jo, Wooyeol Lee, Jihyung Ko, Young Bin Park, Jae-Mun Choi, Eunho Yang, Kyungsu Kim  (\*: equal contribution). "On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2512.10339>.
- Yoonjeon Kim\*, Doohyuk Jang\*, Eunho Yang (\*: equal contribution). "Verifying Meta-Awareness via Predictive Rewards in Reasoning Models". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2510.03259>.
- Joonhyung Park, Jaeyun Song, Sihwan Park, Eunho Yang. "Bringing Real-World Relations into Video Generation with Graph-Structured Knowledge". *Annual Meeting of the Association for Computational Linguistics (ACL) (main) (채택)*.
- Seyun Bae, Seokhan Lee, Eunho Yang. "CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge". *Annual Meeting of the Association for Computational Linguistics (ACL) (findings) (채택)*.
- Jina Kim, Myeongho Jeon, Soohyun Cho, Chae-Gyun Lim, Jongmin Lim, Haewon Min, Eunho Yang. "PhaseMI: A Motivational Interviewing Dataset for Enhancing Phase Progression in LLM-based Counseling". *Annual Meeting of the Association for Computational Linguistics (ACL) (findings)*. DOI: <https://doi.org/10.18653/v1/2026.findings-acl.1970>.[^phase]
- Geon Choi\*, Hangyul Yoon\*, Hyunju Shin, Hyunki Park, Sang Hoon Seo, Eunho Yang, Edward Choi (\*: equal contribution). "Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2511.15186>.[^lesion]
- Joonhyung Park\*, Hyeongwon Jang\*, Joowon Kim, Eunho Yang (\*: equal contribution). "Progress by Pieces: Test-Time Scaling for Autoregressive Image Generation". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (연구실 기재)*.
- Changhun Kim\*, Yechan Mun\*, Hyeongwon Jang, Eunseo Lee, Sangchul Hahn, Eunho Yang (\*: equal contribution). "Delta-XAI: A Unified Framework for Explaining Prediction Changes in Online Time Series Monitoring". *International Conference on Learning Representations (ICLR) (채택)*.
- Rohan Choudhury\*, JungEun Kim\*, Jinhyung Park, Eunho Yang, Laszlo A. Jeni, Kris Kitani (\*: equal contribution). "Faster Vision Transformers with Adaptive Patches". *International Conference on Learning Representations (ICLR) (채택)*.
- Thanh-Long V. Le, Myeongho Jeon, Kim Vu, Viet Lai, Eunho Yang. "No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping". *International Conference on Learning Representations (ICLR) (채택)*.
- Jaeyun Song, Geondo Park, Uigyu Kim, Joonhyung Park, Eunho Yang. "Secure Inference for Diffusion Models via Unconditional Scores". *International Conference on Learning Representations (ICLR) (채택)*.
- Heecheol Yun, Kwangmin Ki, Junghyun Lee, Eunho Yang. "When to Ensemble: Identifying Token-Level Points for Stable and Fast LLM Ensembling". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2510.15346>.
- Gilhyun Nam\*, Taewon Kim\*, Joonhyun Jeong, Eunho Yang (\*: equal contribution). "Towards Reliable Test-Time Adaptation: Style Invariance as a Correctness Likelihood". *IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*. DOI: <https://doi.org/10.1109/wacv61042.2026.00302>.
- Juhwan Choi\*, Kwanhyung Lee\*, Sangchul Hahn, Eunho Yang (\*: equal contribution). "LLM Plug-ins Are Not a Free Lunch for Clinical Time-Series Prediction". *EACL Workshop on Linguistic Analysis for Health*. DOI: <https://doi.org/10.18653/v1/2026.healing-1.17>.[^plugin]

**2025**

- Seungseop Lim, Gibaeg Kim, Hyunkyung Lee, Wooseok Han, Jean Seo, Jaehyo Yoo, Eunho Yang. "H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis". *NeurIPS Workshop on GenAI for Health (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2510.03700>.[^hddx]
- Jean Seo, Hyunkyung Lee, Gibaeg Kim, Wooseok Han, Jaehyo Yoo, Seungseop Lim, Kihun Shin, Eunho Yang. "Taxonomy of Comprehensive Safety for Clinical Agents". *EMNLP Industry Track (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2509.22041>.[^tacos]
- Sohee Kim\*, Soohyun Ryu\*, Joonhyung Park, Eunho Yang (\*: equal contribution). "Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens". *Conference on Empirical Methods in Natural Language Processing (EMNLP)*. DOI: <https://doi.org/10.18653/v1/2025.emnlp-main.1092>.
- Joowon Kim\*, Ziseok Lee\*, Donghyeon Cho, Sanghyun Jo, Yeonsung Jung, Kyungsu Kim, Eunho Yang (\*: equal contribution). "Early Timestep Zero-Shot Candidate Selection for Instruction-Guided Image Editing". *IEEE/CVF International Conference on Computer Vision (ICCV)*. DOI: <https://doi.org/10.1109/iccv51701.2025.01751>.
- Tehrim Yoon\*, Minyeong Hwang\*, Eunho Yang (\*: equal contribution). "VQ-FedDiff: Federated Learning Algorithm of Diffusion Models with Client-Specific Vector-Quantized Conditioning". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*. DOI: <https://doi.org/10.1109/tpami.2025.3602282>.
- Minyeong Hwang, Ziseok Lee, Kwang-Soo Kim, Kyungsu Kim, Eunho Yang. "HybridLinker: Topology-Guided Posterior Sampling for Enhanced Diversity and Validity in 3D Molecular Linker Generation". *ICML Workshop on Generative AI and Biology (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2502.17349>.
- Changhun Kim\*, Yechan Mun\*, Sangchul Hahn, Eunho Yang (\*: equal contribution). "DeltaSHAP: Explaining Prediction Evolutions in Online Patient Monitoring with Shapley Values". *ICML Workshop on Actionable Interpretability (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2507.02342>.[^delta]
- Hyeongwon Jang\*, Changhun Kim\*, Eunho Yang (\*: equal contribution). "TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2506.05035>.
- Joonhyun Jeong, Seyun Bae, Yeonsung Jung, Jaeryong Hwang, Eunho Yang. "Playing the Fool: Jailbreaking LLMs and Multimodal LLMs with Out-of-Distribution Strategy". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. DOI: <https://doi.org/10.1109/cvpr52734.2025.02786>.
- Yoonjeon Kim\*, Soohyun Ryu\*, Yeonsung Jung, Hyunkoo Lee, Joowon Kim, June Yong Yang, Jaeryong Hwang, Eunho Yang (\*: equal contribution). "Preserve or Modify? Context-Aware Evaluation for Balancing Preservation and Modification in Text-Guided Image Editing". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. DOI: <https://doi.org/10.1109/cvpr52734.2025.02186>.
- Hyun Ryu, Gyeongman Kim, Hyemin S. Lee, Eunho Yang. "Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2410.08047>.
- Doohyuk Jang\*, Sihwan Park\*, June Yong Yang, Yeonsung Jung, Jihun Yun, Souvik Kundu, Sung-Yub Kim, Eunho Yang (\*: equal contribution). "LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2410.03355>.
- Taewon Kim\*, Hyunjin Seo\*, Sungsoo Ahn, Eunho Yang (\*: equal contribution). "ReBind: Enhancing Ground-state Molecular Conformation Prediction via Force-Based Graph Rewiring". *International Conference on Learning Representations (ICLR) (채택)*.
- Byungjai Kim, Chanho Ahn, Wissam J. Baddar, Kikyung Kim, Huijin Lee, Saehyun Ahn, Seungju Han, Sungjoo Suh, Eunho Yang. "Test-Time Ensemble via Linear Mode Connectivity: A Path to Better Adaptation". *International Conference on Learning Representations (ICLR) (채택)*.
- Jung Hyun Lee\*, June Yong Yang\*, Byeongho Heo, Dongyoon Han, Kyungsu Kim, Eunho Yang, Kang Min Yoo (\*: equal contribution). "Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models". *International Conference on Learning Representations (ICLR) (채택)*.
- Minki Kang\*, Wooseok Han\*, Eunho Yang (\*: equal contribution). "Face-StyleSpeech: Enhancing Zero-shot Speech Synthesis from Face Images with Improved Face-to-Speech Mapping". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*. DOI: <https://doi.org/10.1109/icassp49660.2025.10889667>.
- Wooseok Han\*, Minki Kang\*, Changhun Kim, Eunho Yang (\*: equal contribution). "Stable-TTS: Stable Speaker-Adaptive Text-to-Speech Synthesis via Prosody Prompting". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*. DOI: <https://doi.org/10.1109/icassp49660.2025.10890553>.
- Hyeongwon Jang\*, Changhun Kim\*, Eunho Yang (\*: equal contribution). "TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation". *ICLR Workshop on XAI4Science: From Understanding Model Behavior to Discovering New Scientific Knowledge (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2506.05035>.
- Sihwan Park\*, Doohyuk Jang\*, Sung-Yub Kim, Souvik Kundu, Eunho Yang (\*: equal contribution). "LANTERN++: Enhanced Relaxed Speculative Decoding with Static Tree Drafting for Visual Auto-regressive Models". *ICLR Workshop on Scalable Optimization for Efficient and Adaptive Foundation Models (Oral Presentation) (연구실 기재)*.
- Jung Hyun Lee\*, Jeonghoon Kim\*, June Yong Yang, Se Jung Kwon, Eunho Yang, Kang Min Yoo, Dongsoo Lee (\*: equal contribution). "LRQ: Optimizing Post-Training Quantization for Large Language Models by Learning Low-Rank Weight-Scaling Matrices". *Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL)*. DOI: <https://doi.org/10.18653/v1/2025.naacl-long.393>.
- Hyunjin Seo, Kyusung Seo\*, Joonhyung Park\*, Eunho Yang (\*: equal contribution). "Towards Precise Prediction Uncertainty in GNNs: Refining GNNs with Topology-grouping Strategy". *AAAI Conference on Artificial Intelligence (AAAI)*. DOI: <https://doi.org/10.1609/aaai.v39i19.34239>.

**2024**

- Changhun Kim\*, Taewon Kim\*, Seungyeon Woo, June Yong Yang, Eunho Yang (\*: equal contribution). "AdapTable: Test-Time Adaptation for Tabular Data via Shift-Aware Uncertainty Calibrator and Label Distribution Handler". *NeurIPS Workshop on Table Representation Learning (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2407.10784>.
- Yeonsung Jung\*, Jaeyun Song\*, June Yong Yang, Jin-Hwa Kim, Sung-Yub Kim, Eunho Yang (\*: equal contribution). "A Simple Remedy for Dataset Bias via Self-Influence: A Mislabeled Sample Perspective". *Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Gyeongman Kim, Doohyuk Jang, Eunho Yang. "PromptKD: Distilling Student-Friendly Knowledge for Generative Language Models via Prompt Tuning". *Conference on Empirical Methods in Natural Language Processing (EMNLP) (findings)*. DOI: <https://doi.org/10.18653/v1/2024.findings-emnlp.364>.
- Hyeongwon Jang\*, June Yong Yang\*, Jaeryong Hwang, Eunho Yang (\*: equal contribution). "Time Series Classification with Large Language Models via Linguistic Scaffolding". *IEEE Access*. DOI: <https://doi.org/10.1109/access.2024.3475471>.
- Hajin Shim\*, Changhun Kim\*, Eunho Yang (\*: equal contribution). "CloudFixer: Test-Time Adaptation for 3D Point Clouds via Diffusion-Guided Geometric Transformation". *European Conference on Computer Vision (ECCV)*. DOI: <https://doi.org/10.1007/978-3-031-72751-1_26>.
- Sanghyun Jo\*, Soohyun Ryu\*, Sungyub Kim,  Eunho Yang, Kyungsu Kim (\*: equal contribution). "TTD: Text-Tag Self-Distillation Enhancing Image-Text Alignment in CLIP to Alleviate Single Tag Bias". *European Conference on Computer Vision (ECCV)*. DOI: <https://doi.org/10.1007/978-3-031-73004-7_20>.
- Yeonsung Jung, Heecheol Yun, Joonhyung Park, Jin-Hwa Kim, Eunho Yang. "PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2406.00798>.
- JungEun Kim\*, Hangyul Yoon\*, Geondo Park, Kyungsu Kim, Eunho Yang (\*: equal contribution). "Data-Efficient Unsupervised Interpolation Without Any Intermediate Frame for 4D Medical Images". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. DOI: <https://doi.org/10.1109/cvpr52733.2024.01079>.
- June Yong Yang\*, Geondo Park\*, Joowon Kim, Hyeongwon Jang, Eunho Yang (\*: equal contribution). "Language-Interfaced Tabular Oversampling via Progressive Imputation and Self-Authentication". *International Conference on Learning Representations (ICLR) (채택)*.
- Hyunjin Seo\*, Jihun Yun\*, Eunho Yang (\*: equal contribution). "TEDDY: Trimming Edges with Degree-based Discrimination strategY". *International Conference on Learning Representations (ICLR) (연구실 기재)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2402.01261>.
- Yeongho Jeong, Gyeongman Kim, Doohyuk Jang, Jaeryong Hwang, Eunho Yang. "SeamsTalk: Seamless Talking Face Generation via Flow-Guided Inpainting". *IEEE Access*. DOI: <https://doi.org/10.1109/access.2024.3381992>.

**2023**

- Sung-Yub Kim, Kyungsu Kim, Eunho Yang. "GEX: A flexible method for approximating influence via Geometric Ensemble". *Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Jihun Yun, Eunho Yang. "Riemannian SAM: Sharpness-Aware Minimization on Riemannian Manifolds". *Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Joonhyung Park, Hyunjin Seo, Eunho Yang. "PC-Adapter: Topology-Aware Adapter for Efficient Domain Adaption on Point Clouds with Rectified Pseudo-label". *IEEE/CVF International Conference on Computer Vision (ICCV)*. DOI: <https://doi.org/10.1109/iccv51070.2023.01059>.
- Changhun Kim, Joonhyung Park, Hajin Shim, Eunho Yang. "SGEM: Test-Time Adaptation for Automatic Speech Recognition via Sequential-Level Generalized Entropy Minimization". *Conference of the International Speech Communication Association (INTERSPEECH)*. DOI: <https://doi.org/10.21437/interspeech.2023-1282>.
- Minki Kang\*, Wooseok Han\*, Sung Ju Hwang, Eunho Yang (\*: equal contribution). "ZET-Speech: Zero-shot adaptive Emotion-controllable Text-to-Speech Synthesis with Diffusion and Style-based Models". *Conference of the International Speech Communication Association (INTERSPEECH)*. DOI: <https://doi.org/10.21437/interspeech.2023-754>.
- Yeonsung Jung, Hajin Shim, June Yong Yang, Eunho Yang. "Fighting Fire with Fire: Contrastive Debiasing without Bias-free Data via Generative Bias-transformation". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2112.01021>.
- Jaeyun Song\*, Sung-Yub Kim\*, Eunho Yang (\*: equal contribution). "RGE: A Repulsive Graph Rectification for Node Classification via Influence". *International Conference on Machine Learning (ICML) (채택)*.
- Jongin Lim, Youngdong Kim, Byungjai Kim, Chanho Ahn, Jinwoo Shin, Eunho Yang, Seungju Han. "BiasAdv: Bias-Adversarial Augmentation for Model Debiasing". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. DOI: <https://doi.org/10.1109/cvpr52729.2023.00373>.
- Gyeongman Kim, Hajin Shim, Hyunsu Kim, Yunjey Choi, Junho Kim, Eunho Yang. "Diffusion Video Autoencoders: Toward Temporally Consistent Face Video Editing via Disentangled Video Encoding". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. DOI: <https://doi.org/10.1109/cvpr52729.2023.00590>.
- Youngsung Kim, Yoonsuk Hyun, Jae-Joon Han, Eunho Yang, Sung Ju Hwang, Jinwoo Shin. "Deep Self-Supervised Diversity Promoting Learning on Hierarchical Hyperspheres for Regularization". *IEEE Access*. DOI: <https://doi.org/10.1109/access.2023.3346430>.
- Kyusung Seo, Joonhyung Park, Jaeyun Song, Eunho Yang. "WeavSpeech: Data Augmentation Strategy for Automatic Speech Recognition via Semantic-Aware Weaving". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*. DOI: <https://doi.org/10.1109/icassp49357.2023.10097196>.
- Yoonjeon Kim, Hyunsu Kim, Junho Kim, Yunjey Choi, Eunho Yang. "Learning Input-agnostic Manipulation Directions in StyleGAN with Text Guidance". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2302.13331>.
- Sung-Yub Kim, Sihwan Park, Kyungsu Kim, Eunho Yang. "Scale-invariant Bayesian Neural Networks with Connectivity Tangent Kernel". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2209.15208>.

**2022**

- Bruno Andreis, Seanie Lee, A. Tuan Nguyen, Juho Lee, Eunho Yang, Sung Ju Hwang. "Set Based Stochastic Subsampling". *International Conference on Machine Learning (ICML) (채택)*.
- Jaeyun Song\*, Joonhyung Park\*, Eunho Yang (\*: equal contribution). "TAM: Topology-Aware Margin Loss for Class-Imbalanced Node Classification". *International Conference on Machine Learning (ICML) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2206.12917>.
- Juhyuk Lee\*, Min-Joong Lee\*, June Yong Yang\*, Eunho Yang (\*: equal contribution). "Does it Really Generalize Well on Unseen Data? Systematic Evaluation of Relational Triple Extraction Methods". *Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)*. DOI: <https://doi.org/10.18653/v1/2022.naacl-main.282>.
- Joonhyung Park\*, Jaeyun Song\*, Eunho Yang (\*: equal contribution). "GraphENS: Neighbor-Aware Ego Network Synthesis for Class-Imbalanced Node Classification". *International Conference on Learning Representations (ICLR) (채택)*.
- Youngmin Oh, Jinwoo Shin, Eunho Yang, Sung Ju Hwang. "Model-augmented Prioritized Experience Replay". *International Conference on Learning Representations (ICLR) (채택)*.
- Jaehong Yoon, Divyam Madaan, Eunho Yang, Sung Ju Hwang. "Online Coreset Selection for Rehearsal-based Continual Learning". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2106.01085>.
- Hae Beom Lee, Hayeon Lee, Jaewoong Shin, Eunho Yang, Timothy Hospedales, Sung Ju Hwang. "Online Hyperparameter Meta-Learning with Hypergradient Distillation". *International Conference on Learning Representations (ICLR) (채택)*. 연결된 arXiv 판 DOI: <https://doi.org/10.48550/arxiv.2110.02508>.
- Jihun Yun, Aurelie C. Lozano, Eunho Yang. "AdaBlock: SGD with Practical Block Diagonal Matrix Adaptation for Deep Learning". *International Conference on Artificial Intelligence and Statistics (AISTATS) (채택)*.
- Youngbum Hur, Eunho Yang, Sung Ju Hwang. "A Simple Framework for Robust Out-of-Distribution Detection". *IEEE Access*. DOI: <https://doi.org/10.1109/access.2022.3153723>.
- Joonhyung Park\*, Hajin Shim\*, Eunho Yang (\*: equal contribution). "Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure Preservation". *AAAI Conference on Artificial Intelligence (AAAI)*. DOI: <https://doi.org/10.1609/aaai.v36i7.20767>.
- Joonhyung Park, June Yong Yang, Jinwoo Shin, Sung Ju Hwang, Eunho Yang. "Saliency Grafting: Innocuous Attribution-Guided Mixup with Calibrated Label Mixing". *AAAI Conference on Artificial Intelligence (AAAI)*. DOI: <https://doi.org/10.1609/aaai.v36i7.20766>.
- Tehrim Yoon, Sumin Shin, Eunho Yang. "Learning Polymorphic Neural ODEs with Time-Evolving Mixture". *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) (연구실 기재)*.

**2021**

- Jaeyun Song, Hajin Shim, Eunho Yang. "Learning How Long to Wait: Adaptively-Constrained Monotonic Multihead Attention for Streaming ASR". *IEEE Workshop on Automatic Speech Recognition and Understanding (ASRU)*. DOI: <https://doi.org/10.1109/asru51503.2021.9688138>.
- Jihun Yun, Aurelie C. Lozano, Eunho Yang. "Adaptive Proximal Gradient Methods for Structured Neural Networks". *Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Youngkyu Hong, Eunho Yang. "Unbiased Classification through Bias-Contrastive and Bias-Balanced Learning". *Conference on Neural Information Processing Systems (NeurIPS) (채택)*.
- Kyung-Su Kim, Jung Hyun Lee, Eunho Yang. "Compressed Sensing via Measurement-Conditional Generative Models". *IEEE Access*. DOI: <https://doi.org/10.1109/access.2021.3128721>.
- Geondo Park, Gyeongman Kim, Eunho Yang. "Distilling Linguistic Context for Language Model Compression". *Conference on Empirical Methods in Natural Language Processing (EMNLP)*. DOI: <https://doi.org/10.18653/v1/2021.emnlp-main.30>.
- Jung Hyun Lee\*, Jihun Yun\*, Sung Ju Hwang, Eunho Yang (\*: equal contribution). "Cluster-Promoting Quantization with Bit-Drop for Minimizing Network Quantization Loss". *IEEE/CVF International Conference on Computer Vision (ICCV)*. DOI: <https://doi.org/10.1109/iccv48922.2021.00532>.
- Jaehong Yoon, Wonyong Jeong, Giwoong Lee, Eunho Yang, Sung Ju Hwang. "Federated Continual Learning with Weighted Inter-client Transfer". *International Conference on Machine Learning (ICML) (채택)*.
- Dongchan Min, Dong Bok Lee, Eunho Yang, Sung Ju Hwang. "Meta-StyleSpeech : Multi-Speaker Adaptive Text-to-Speech Generation". *International Conference on Machine Learning (ICML) (채택)*.
- Wonyong Jeong, Jaehong Yoon, Eunho Yang, Sung Ju Hwang. "Federated Semi-Supervised Learning with Inter-Client Consistency & Disjoint Learning". *International Conference on Learning Representations (ICLR) (채택)*.
- Tehrim Yoon, Sumin Shin, Sung Ju Hwang, Eunho Yang. "FedMix: Approximation of Mixup under Mean Augmented Federated Learning". *International Conference on Learning Representations (ICLR) (채택)*.
- Youngmin Oh, Kimin Lee, Jinwoo Shin, Eunho Yang, Sung Ju Hwang. "Learning to Sample with Local and Global Contexts in Experience Replay Buffer". *International Conference on Learning Representations (ICLR) (채택)*.

## 소식

연구실 News 쪽에 게시된 2021년 10월 13일–2026년 10월 13일의 논문 채택·게재 승인 소식 30건이다. 날짜는 게시일이다. 여러 논문을 한 글로 알린 경우 하나의 소식으로 적고, 아래 편수는 그 글에서 다루는 논문 가운데 이 문서의 논문 범위에 해당하는 편수다.[^news]

- 2026-08-31 · 논문 3편이 EMNLP 2026에 채택되었다.
- 2026-05-01 · 논문 4편이 ICML 2026에 채택되었다.
- 2026-04-21 · 논문 3편이 ACL 2026에 채택되었다.
- 2026-01-27 · 논문 5편이 ICLR 2026에 채택되었다.
- 2025-08-25 · 논문 1편이 EMNLP 2025 main에 채택되었다.
- 2025-08-13 · 논문 1편이 TPAMI 2025에 게재 승인되었다.
- 2025-06-26 · 논문 1편이 ICCV 2025에 채택되었다.
- 2025-05-07 · 논문 1편이 ICML 2025에 채택되었다.
- 2025-02-26 · 논문 2편이 CVPR 2025에 채택되었다.
- 2025-01-23 · 논문 5편이 ICLR 2025에 채택되었다.
- 2025-01-22 · 논문 1편이 NAACL 2025에 채택되었다.
- 2024-12-21 · 논문 2편이 ICASSP 2025에 채택되었다.
- 2024-12-10 · 논문 1편이 AAAI 2025에 채택되었다.
- 2024-09-26 · 논문 1편이 NeurIPS 2024에 채택되었다.
- 2024-07-02 · 논문 2편이 ECCV 2024에 채택되었다.
- 2024-05-08 · 논문 1편이 ICML 2024에 채택되었다.
- 2024-02-27 · 논문 1편이 CVPR 2024에 채택되었다.
- 2024-01-17 · 논문 2편이 ICLR 2024에 채택되었다.
- 2023-09-22 · 논문 2편이 NeurIPS 2023에 채택되었다.
- 2023-07-13 · 논문 1편이 ICCV 2023에 채택되었다.
- 2023-05-17 · 논문 2편이 INTERSPEECH 2023에 채택되었다.
- 2023-04-24 · 논문 2편이 ICML 2023에 채택되었다.
- 2023-02-27 · 논문 2편이 CVPR 2023에 채택되었다.
- 2023-02-15 · 논문 1편이 ICASSP 2023에 채택되었다.
- 2023-01-21 · 논문 2편이 ICLR 2023에 채택되었다.
- 2022-05-14 · 논문 2편이 ICML 2022에 채택되었다.
- 2022-04-07 · 논문 1편이 NAACL 2022에 채택되었다.
- 2022-01-24 · 논문 4편이 ICLR 2022에 채택되었다.
- 2022-01-19 · 논문 1편이 AISTATS 2022에 채택되었다.
- 2021-11-29 · 논문 2편이 AAAI 2022에 채택되었다.

## 연락과 위치

- 연구실: Yangjae, SEOUL AI HUB 5층, 서울특별시 서초구 태봉로 108, 우편번호 06764.[^contact]
- 교수 사무실: 양재캠퍼스 5층 503호.[^faculty]
- 교수 이메일: eunhoy@kaist.ac.kr.[^contact]
- 연구실 대표 연락 담당: Doohyuk Jang, jadohu@kaist.ac.kr.[^contact]
[^home]: MLILAB 첫 화면의 연구 갈래. <https://mli.kaist.ac.kr> (2026-11-09).
[^profile]: MLILAB People의 교수 소개와 연구 관심. <https://mli.kaist.ac.kr/people/> (2026-11-09).
[^faculty]: KAIST 김재철AI대학원 구성원 명단의 양은호 교수 항목. 직위·연구분야·사무실. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (2026-11-09).
[^people]: MLILAB People의 현재 구성원과 Alumni. <https://mli.kaist.ac.kr/people/> (2026-11-09).
[^pubs]: MLILAB Publications의 학술지·학회·기타 발표 목록. <https://mli.kaist.ac.kr/publications/> (2026-11-09).
[^news]: MLILAB News의 논문 채택·게재 승인 소식. <https://mli.kaist.ac.kr/news/> (2026-11-09).
[^contact]: MLILAB Contact Information. 연구실 주소·업무 이메일. <https://mli.kaist.ac.kr/contact/> (2026-11-11).
[^oa]: Eunho Yang의 OpenAlex 논문 기록. 논문별 DOI와 날짜·초록. <https://openalex.org/A5086698569> (2026-11-11).
[^dates]: Crossref의 2021년 논문 날짜 기록. DOI 등록일: Cluster-Promoting Quantization 2022-02-28, Distilling Linguistic Context 2021-12-17, Compressed Sensing 2021-11-17. <https://api.crossref.org/works/10.1109/iccv48922.2021.00532> <https://api.crossref.org/works/10.18653/v1/2021.emnlp-main.30> <https://api.crossref.org/works/10.1109/access.2021.3128721> (2026-11-11).
[^lesion]: G. Choi 외, Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset. CVPR 2026 최종 원고판 표시, 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2511.15186> (2026-11-11).
[^emr]: K. Lee 외, EMR-AGENT: Automating Cohort and Feature Extraction from EMR Databases. 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.00549> (2026-11-11).
[^phase]: J. Kim 외, PhaseMI, Findings of the Association for Computational Linguistics: ACL 2026, 39538–39570. <https://doi.org/10.18653/v1/2026.findings-acl.1970> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2026.findings-acl.1970/> (2026-11-11).
[^plugin]: J. Choi, K. Lee, S. Hahn, E. Yang, LLM Plug-ins Are Not a Free Lunch for Clinical Time-Series Prediction, HeaLing 2026, 203–211. <https://doi.org/10.18653/v1/2026.healing-1.17> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2026.healing-1.17/> (2026-11-11).
[^hddx]: S. Lim 외, H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis. GenAI4Health @ NeurIPS 2025 표기, 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.03700> (2026-11-11).
[^tacos]: J. Seo 외, Taxonomy of Comprehensive Safety for Clinical Agents. EMNLP 2025 Industry 표기, 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2509.22041> (2026-11-11).
[^delta]: C. Kim, Y. Mun, S. Hahn, E. Yang, DeltaSHAP: Explaining Prediction Evolutions in Online Patient Monitoring with Shapley Values. ICML 2025 Workshop on Actionable Interpretability 채택 표기, 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2507.02342> (2026-11-11).
[^p1]: S. Kim, S. Ryu, J. Park, E. Yang, Conference on Empirical Methods in Natural Language Processing (EMNLP) (2025). <https://doi.org/10.18653/v1/2025.emnlp-main.1092> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p2]: G. Kim, D. Jang, E. Yang, Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP) (2024). <https://doi.org/10.18653/v1/2024.findings-emnlp.364> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p3]: J. Jeong 외, E. Yang, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2025). <https://doi.org/10.1109/cvpr52734.2025.02786> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p4]: G. Kim 외, E. Yang, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2023). <https://doi.org/10.1109/cvpr52729.2023.00590> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p5]: T. Yoon, M. Hwang, E. Yang, IEEE Transactions on Pattern Analysis and Machine Intelligence (2025). <https://doi.org/10.1109/tpami.2025.3602282> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p6]: J. Park, H. Shim, E. Yang, Proceedings of the AAAI Conference on Artificial Intelligence (2022). <https://doi.org/10.1609/aaai.v36i7.20767> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p7]: H. Seo, K. Seo, J. Park, E. Yang, Proceedings of the AAAI Conference on Artificial Intelligence (2025). <https://doi.org/10.1609/aaai.v39i19.34239> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).
[^p8]: J. Kim 외, E. Yang, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (2024). <https://doi.org/10.1109/cvpr52733.2024.01079> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5086698569> (2026-11-11).

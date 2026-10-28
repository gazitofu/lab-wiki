# 기계학습 및 비전 연구실 (Machine Learning and Vision Lab, MLV)

**KAIST 전산학부·김재철AI대학원·데이터사이언스대학원 · 김현우 부교수**

- 분야: 영상·언어 이해, 범용인공지능과 에이전트, 분자·기상 자료를 위한 기계학습, 생성 모델, 입체 장면 표현
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^research][^p2], 멀티모달 AI[^research][^p5], 대형 언어 모델[^p1][^p5], 생성 인공지능[^research][^p7], 그래프 기계학습·지식 그래프[^research][^p5], 강화학습[^p1][^p2], 과학·공학 AI[^labinfo][^p5]
- 홈페이지: <https://www.hyunwoojkim.com/>
- 근거와 출처: [기계학습 및 비전 연구실 근거 페이지](hyunwoojkim-sources.md)

> 영상·글·분자 구조처럼 형태가 다른 자료를 이해하고 새로운 자료를 생성하는 인공지능을 연구하며, 여러 과제를 스스로 해결하는 모델과 계산 자원을 효율적으로 쓰는 방법을 만든다.[^home][^research]

## 무엇을 연구하나

기계학습 및 비전 연구실은 KAIST 전산학부 김현우 부교수가 이끈다. KAIST 연구실은 2025년 2월 시작했으며, 그전에는 고려대학교에서 연구실을 운영했다.[^home][^faculty] 기계학습(자료에서 규칙과 작업 방법을 배우는 기술)과 컴퓨터 비전(사진·영상의 내용을 컴퓨터가 이해하는 기술)의 기본 문제를 풀어, 다양한 복잡한 과제를 수행할 범용인공지능(Artificial General Intelligence, AGI)을 개발하는 것이 목표다.[^home][^labinfo]

첫 축은 **영상과 언어를 함께 이해하는 인공지능**이다. 연구실은 영상의 내용을 묻고 답하는 비디오 질의응답, 영상과 글을 함께 다루는 비디오·언어 모델, 여러 과제에 바탕으로 쓸 수 있게 학습한 기초 모델을 연구한다. 특정 과제만 배우는 대신 이미지·영상·지식 그래프(개체와 그 사이의 관계로 사실을 표현한 자료) 등 여러 종류의 정보를 활용해 처음 접하는 과제도 배우고 수행하는 범용 학습 시스템을 지향한다.[^research] 대표 연구는 영상 모델의 추론 학습, 영상 검색을 되풀이하며 질문에 맞는 장면을 찾는 에이전트(목표에 따라 판단하고 행동하는 계산 주체), 질문에 필요한 표 이미지의 정보만 남기는 모델로 이어진다.[^p1][^p2][^p3]

둘째 축은 **과학 자료의 구조를 이해하는 인공지능**이다. 원자와 결합으로 이루어진 분자나 지점 사이의 관계를 가진 기상 자료를 다룬다. 연구 소개는 그래프 신경망(점과 선으로 나타낸 자료의 관계를 학습하는 신경망)을 이용한 분자 언어 모델, 신약 탐색을 위한 분자 최적화, 날씨 예측을 다룬다고 밝힌다. 자료를 평면 좌표로만 보지 않고 그래프와 곡면 등 그 구조에 맞게 배우는 방법에 관심을 둔다.[^research] CoLLaMo는 분자의 문자열·결합 구조·입체 구조를 함께 다루는 언어 모델을 제안한 사례다.[^p5]

셋째 축은 **자료 생성과 계산 효율**이다. 생성 모델(학습 자료의 확률분포를 익혀 새 자료를 만드는 모델)로 이미지·영상·분자를 만들고, 실제 시각 자료를 대규모로 처리하거나 계산 자원이 제한된 환경에서 사용할 수 있는 방법을 연구한다.[^home][^research] 최근 논문에서는 생성 과정의 계산 오차를 유도 신호로 활용하거나, 모델이 처리할 정보의 일부를 고르고 결합해 학습과 생성 계산을 줄인다. 사진으로 입체 장면을 나타낼 때도 장면의 복잡도에 따라 표현 요소를 배분한다.[^p6][^p7][^p8]

## 주요 연구 주제

### 영상·언어 이해와 추론

영상의 어느 부분이 질문에 해당하는지 찾으려면 영상 안의 사건뿐 아니라 검색 과정도 다뤄야 한다. VideoSearch-R1은 영상 검색 엔진과 여러 차례 상호작용하면서 검색 질문을 수정하고, 찾은 영상에서 질문에 맞는 시간 구간을 찾는다.[^p2] DeepVideo-R1은 대형 언어 모델(Large Language Model, LLM; 많은 언어 자료로 학습해 언어를 이해하고 생성하는 모델)을 영상에 확장한 모델의 추론 능력을 강화학습(행동의 결과로 받는 보상을 바탕으로 행동 방법을 배우는 학습)으로 높이는 방법을 연구한다.[^p1]

표 이미지와 시각 인식도 같은 갈래에 있다. TabFlash는 트랜스포머(자료 조각 사이의 관련성을 계산하는 어텐션 구조를 쓰는 모델)에 질문 정보를 단계적으로 넣고, 토큰(모델이 처리하는 자료의 단위) 가운데 배경에 해당하는 부분을 제거한다.[^p3] TransMiter는 작은 모델이 특정 작업에 적응하며 배운 지식을 크기와 구조가 다른 모델로 전달한다. 이때 전달받는 모델에 역전파(출력에서 입력 방향으로 미분값을 전달해 변수에 대한 기울기를 계산하는 방법)를 적용하지 않는 방식을 제안했다.[^p4]

### 과학 자료와 분자 구조

연구실은 분자와 날씨 등 과학 자료를 이해하고 생성하는 AI for Science를 연구한다. 분자 언어 모델과 분자 최적화, 기상 예측을 그래프 학습과 연결하고, 관측값으로 예측 모형을 갱신하며 다음에 평가할 후보를 고르는 베이지안 최적화도 다룬다.[^research][^labinfo] CoLLaMo에서는 원자 사이의 결합 관계와 입체적 위치 관계를 모델 안의 정보 교환에 반영했다. 분자를 글로 설명하고, 성질에 관한 질문에 답하며, 구조의 부분 유형을 세고 이름을 예측하는 과제로 모델을 평가했다.[^p5]

### 생성 모델의 계산과 학습

확산 모델(잡음에서 출발해 자료를 생성하는 과정을 배우는 모델)과 다른 생성 모델의 계산 경로를 연구한다.[^research] ERK-Guid는 확산 생성의 수치 계산에서 생기는 오차를 생성 방향을 정하는 신호로 이용한다.[^p6] SPRINT는 입력 토큰을 모두 처리하는 앞부분과 토큰 일부만 처리하는 뒷부분을 결합해, 이미지 생성 모델의 학습 계산과 생성 계산을 다룬다.[^p7] 분자 후보를 생성하고 최적화하는 연구와 이미지·영상 생성이 연구 소개의 응용 대상이다.[^research]

### 입체 장면 표현과 인공지능의 신뢰성

연구실은 점군(공간의 위치를 점들의 집합으로 나타낸 자료), 입체 모양의 분류와 정합(서로 다른 자료의 위치·형태 대응을 맞추는 작업), 암묵적 신경 표현(좌표를 입력받는 신경망으로 신호나 장면을 표현하는 방식)에 관심을 둔다.[^research] F4Splat은 사진에서 입체 장면을 나타내는 가우시안(정규분포 형태의 공간 요소)을 지역별로 얼마나 배치할지 예측한다.[^p8] 별도로 안전한 인공지능 연구에서는 입력을 교란하는 공격과 방어, 모델 예측의 불확실성을 다룬다. 의료 영상에서는 구조를 가진 자료의 표현과 통계 모형, 자료와 정답 표기가 제한된 상황의 학습 방법을 연구한다고 밝힌다.[^research]

## 대표 논문

김현우 교수가 저자인 2025–2026년 논문에서 영상·언어 이해, 과학 자료, 생성 계산, 입체 표현을 골랐다. 연도와 학회는 랩 목록 표기이며, 링크와 각주의 서지는 실제로 초록을 읽은 arXiv 사전 공개본이다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다. 저자 역할은 전체 저자 순서로 표시했으며 교신저자 여부를 뜻하지 않는다.[^pubs]

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2025 | [DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO](https://doi.org/10.48550/arXiv.2506.07464) · NeurIPS 2025 | 영상 언어 모델의 추론을 강화학습으로 개선한다. 기존 학습 방법에서 학습을 막는 두 문제를 분석하고, 출력의 상대적 이점을 직접 예측하는 회귀 문제로 학습 목표를 바꿨다. 질문과 영상의 난이도를 모델이 풀 수 있는 수준으로 바꾸는 자료 확장도 함께 사용했으며, 여러 평가 자료에서 영상 추론 성능이 향상됐다.[^p1] | 마지막 저자 김현우 |
| 2 | 2026 | [VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement](https://doi.org/10.48550/arXiv.2607.00446) · ECCV 2026 | 처음 검색에서 적합한 영상을 놓치면 그 뒤의 장면 이해도 실패할 수 있다는 문제를 다룬다. 검색을 한 번으로 끝내지 않고 검색 엔진과 반복해서 상호작용한다. 검색어를 글로 다시 쓰는 대신 모델 내부의 연속적인 표현을 조정하고, 검색 결과와 후속 과제의 보상으로 학습했다. 영상 모음에서 관련 영상을 찾고 그 안의 시간 구간을 찾는 과제를 평가했다.[^p2] | 마지막 저자 김현우 |
| 3 | 2026 | [TabFlash: Efficient Table Understanding with Progressive Question Conditioning and Token Focusing](https://doi.org/10.48550/arXiv.2511.13283) · AAAI 2026 | 표 이미지에 답과 무관한 배경이 많고 질문마다 필요한 부분이 다르다는 점을 이용한다. 시각 정보를 처리하는 층에 질문을 점차 자주 넣어 질문에 맞는 특징을 만들고, 배경 토큰을 제거한다. 남은 토큰에 필요한 정보가 모이도록 학습해 정보 손실을 다룬다. 표 이해 과제에서 정확도와 계산·메모리 사용을 평가했다.[^p3] | 마지막 저자 김현우 |
| 4 | 2026 | [Transferable Model-agnostic Vision-Language Model Adaptation for Efficient Weak-to-Strong Generalization](https://doi.org/10.48550/arXiv.2508.08604) · AAAI 2026, 구두 발표 | 이미 학습한 시각·언어 모델과 특정 과제에 맞춰 조정한 모델의 지식 차이를 담는 어댑터 TransMiter를 제안한다. 이 어댑터를 학습한 뒤에는 다른 크기와 구조의 모델에 역전파 없이 적응 지식을 전달한다. 정답 표기가 없는 방식으로 지식 차이를 배우며, 일부 정답 자료를 더 쓰는 경우도 실험했다. 시각 인식 과제에서 모델 사이의 지식 전달과 일반화 능력을 평가했다.[^p4] | 마지막 저자 김현우 |
| 5 | 2026 | [Improving Large Molecular Language Model via Relation-aware Multimodal Collaboration](https://doi.org/10.48550/arXiv.2601.12256) · AAAI 2026 | 분자의 문자열, 원자와 결합의 그래프, 입체 구조를 함께 다루는 분자 언어 모델 CoLLaMo를 제안한다. 원자 사이의 구조적·공간적 관계를 반영해 자료 형태 사이에서 정보를 교환한다. 분자 이해를 평가하기 위해 사실과 다른 설명을 측정하는 지표와 설명 품질 평가도 제안했다. 분자 설명, 성질 질의응답, 부분 구조 개수 세기, 화학 이름 예측 등에서 평가했다.[^p5] | 마지막 저자 김현우 |
| 6 | 2026 | [Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance](https://doi.org/10.48550/arXiv.2603.03692) · ICLR 2026 | 확산 모델의 생성 경로가 급격히 바뀌는 구간에서는 계산 오차가 생성 품질에 영향을 준다. 이 오차를 버릴 대상이 아니라 생성 방향을 정하는 신호로 활용하는 ERK-Guid를 제안했다. 오차와 경로 특성의 관계를 이론과 실험으로 분석하고, 인공 자료와 ImageNet에서 생성 결과를 비교했다.[^p6] | 마지막 저자 김현우 |
| 7 | 2026 | [SPRINT: Sparse-Dense Residual Fusion for Efficient Diffusion Transformers](https://doi.org/10.48550/arXiv.2510.21986) · ICLR 2026 | 확산 트랜스포머에서 토큰을 단순히 버리면 표현 품질이 떨어지는 문제를 다룬다. 앞부분의 층은 전체 토큰으로 세부 정보를 처리하고, 뒷부분의 층은 일부 토큰만 처리한 뒤 두 결과를 결합한다. 일부 토큰으로 사전 학습한 다음 전체 토큰으로 조정하는 학습 순서를 사용했다. 학습 비용뿐 아니라 생성 때의 계산을 줄이는 방법도 평가했다.[^p7] | 8명 중 6번째 저자 김현우 |
| 8 | 2026 | [F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting](https://doi.org/10.48550/arXiv.2603.21304) · ECCV 2026 | 사진마다 공간 표현 요소를 균일하게 배치하면 여러 시점에서 같은 요소가 중복될 수 있다. 장면의 복잡도와 시점 사이의 겹침을 고려해 지역별 밀도 점수를 예측하고, 필요한 곳에 표현 요소를 배분한다. 재학습 없이 전체 요소 수를 조절할 수 있게 했으며, 사용 요소 수와 새 시점 영상의 품질을 함께 비교했다.[^p8] | 마지막 저자 김현우 |

## 교수와 전문 분야

김현우(Hyunwoo J. Kim) 부교수는 KAIST 전산학부 소속이며, 랩 교수 소개는 김재철AI대학원과 데이터사이언스대학원을 겸무(Adjunct) 소속으로 적는다.[^people][^faculty] 2017년 미국 University of Wisconsin-Madison 전산학과에서 박사 학위를 받았고 통계학을 부전공했다. Amazon Lab126에서 근무했으며, 2019년 3월부터 2025년 1월까지 고려대학교에서 연구실을 이끈 뒤 2025년 2월 KAIST 연구실을 시작했다.[^people][^home]

교수 소개의 전문 분야는 기계학습과 컴퓨터 비전을 바탕으로 한 시각적 이해이며, 범용인공지능, 멀티모달 기초 모델, 생성 모델, 입체 비전, 암묵적 신경 표현, 그래프 신경망, 의료 영상을 포함한다.[^people] 최근 대표 논문으로 보면 영상 추론을 위한 학습과 검색,[^p1][^p2] 시각·언어 모델의 정보 선택과 지식 전달,[^p3][^p4] 분자의 여러 표현을 결합하는 학습,[^p5] 생성 모델의 계산 경로와 효율,[^p6][^p7] 입체 장면 표현[^p8]으로 전문성을 이어가고 있다.

랩 소개는 CVPR·ICCV·ICLR 등 학회의 Area Chair 활동을 적고, 누리집 소식은 TMLR Action Editor와 AAAI Senior Program Committee 등 예정된 학술 활동도 전한다.[^faculty][^home]

## 응용 분야

영상 검색·질의응답과 표 이미지 이해는 사람이 묻는 내용에 맞춰 영상과 문서에서 정보를 찾는 문제로 이어진다.[^p2][^p3] 과학 쪽에서는 분자 구조 이해와 생성, 분자 후보 최적화, 기상 예측을 목표로 한다.[^labinfo][^research] 연구 소개는 입체 자료의 응용으로 로봇, 자율주행, 드론과 장면 복원을 들며, 시각 장면 이해를 스마트 홈·사무실·도시의 서비스와 연결한다. 의료 영상에서도 구조를 가진 자료의 표현과 학습 방법을 연구한다.[^research]

## 구성원

2026년 10월 28일 People 페이지 기준으로 박사후연구원 5명, 석박사통합과정 13명, 석사과정 14명, Interns 구획의 학부생 6명이다. 과정은 개별 카드의 표기이며, Ph.D. Students 구획도 카드가 MS/Ph.D Integrated Student로 적은 것을 따랐다. 연구 주제와 학교 이메일은 랩 게시 내용이다. "대표 논문 참여"는 위 표의 번호로, 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Jinyoung Park (박진영) | 박사후연구원 | Artificial General Intelligence (AGI); AI for Science; Machine Learning on Graphs | jinyoung.park@kaist.ac.kr | 1, 5 |
| Seunghun Lee (이승훈) | 박사후연구원 | Machine Learning on Graphs | llsshh319@korea.ac.kr |  |
| Jihwan Park (박지환) | 박사후연구원 | Computer Vision; Machine Learning on Graphs | jseven7071@kaist.ac.kr | 4 |
| Seunghwan Lee (이승환) | 박사후연구원 | Computer Vision; Multimodal understanding | shlee0@kaist.ac.kr |  |
| Sungho Lee (이성호) | 박사후연구원 | Audio inverse problems | sh-lee@snu.ac.kr |  |
| Sihyeon Kim (김시현) | 석박사통합과정 | 3D structured data processing; 3D deep learning | sh_bs15@korea.ac.kr |  |
| Dohwan Ko (고도환) | 석박사통합과정 | Multi-modal Understanding; Video Understanding; Foundation Models; Large Language Models | ikodoh@korea.ac.kr | 2 |
| Joonmyung Choi (최준명) | 석박사통합과정 | Computer Vision; Meta Learning | pizard@korea.ac.kr |  |
| Sojin Lee (이소진) | 석박사통합과정 | Computer Vision; Meta Learning | sojin.lee@kaist.ac.kr | 6 |
| Minseok Joo (주민석) | 석박사통합과정 | Generative Model; 3D Vision; Video World Model | wlgkcjf87@korea.ac.kr | 8 |
| Injae Kim (김인재) | 석박사통합과정 | 3D vision; Generative model | injae.kim@kaist.ac.kr | 8 |
| Jongha Kim (김종하) | 석박사통합과정 | Multimodal LLM; Scene Understanding | jonghakim@korea.ac.kr | 2, 3 |
| Se Hyung Kim (김세형) | 석박사통합과정 | Computer Vision | shkim129@korea.ac.kr |  |
| Jaewon Chu (주재원) | 석박사통합과정 | Black Box Optimization; Large Language Models; AI for Science | allonsy07@korea.ac.kr |  |
| Jin Young Kim (김진영) | 석박사통합과정 | Computer Vision; Agentic Reasoning | k012100@korea.ac.kr | 1 |
| Ji Soo Lee (이지수) | 석박사통합과정 | Computer Vision | simplewhite9@korea.ac.kr |  |
| Tae Hoon Song (송태훈) | 석박사통합과정 | Computer Vision | taehoons@kaist.ac.kr | 4 |
| Minseo Yoon (윤민서) | 석박사통합과정 | Machine Learning on Graphs; AI for Science | yms020615@kaist.ac.kr |  |
| Chaehyeon Kim (김채현) | 석사과정 | Generative Model; 3D Vision | chann01@korea.ac.kr | 8 |
| Jeehye Na (나지혜) | 석사과정 | Artificial General Intelligence (AGI); Multimodal Learning | jeehyena@kaist.ac.kr | 1, 5 |
| Taehoon Lee (이태훈) | 석사과정 | Generative Model; Computer Vision | dlxogns183@kaist.ac.kr |  |
| Minseong Bae (배민성) | 석사과정 | Machine Learning on Graphs; Generative Model; AI for Science | bms2002@kaist.ac.kr | 3, 5, 8 |
| Jaewon Cho (조재원) | 석사과정 (co-advised by Alice Oh) | Multimodal LLM | cho35750@kaist.ac.kr |  |
| Kyujin Lee (이규진) | 석사과정 | Generative Model; Computer Vision | kyujinlee@kaist.ac.kr |  |
| Seungmin Yun (윤승민) | 석사과정 | Multimodal AI | yunn2345@kaist.ac.kr |  |
| Jinwoo Seo (서진우) | 석사과정 | Artificial General Intelligence (AGI); Generative Model | sjwoo0612@kaist.ac.kr |  |
| Soonhyeok Choi (최순혁) | 석사과정 | Agentic AI; Multimodal LLM | choe0920@korea.ac.kr |  |
| Seohyun Lee (이서현) | 석사과정 | Multi-modal Understanding; Video Understanding; Agentic AI | seohyunlee@kaist.ac.kr | 2 |
| Junhyung Park (박준형) | 석사과정 | Multi-modal LLM; Video Understanding | kevin2001112@kaist.ac.kr |  |
| Seoung Choi (최서웅) | 석사과정 | Multimodal LLM | choisw0823@kaist.ac.kr | 2 |
| Yejun Ju (주예준) | 석사과정 | Multimodal AI; Computer Vision | dpwns99@kaist.ac.kr |  |
| 이재현 (Jaehyeon Lee) | 석사과정 | Generative Model; AI4Science | jic4656@kaist.ac.kr |  |
| Youngseo Cho (조영서) | 학부 연구생 | Computer Vision; Agentic AI; Artificial General Intelligence (AGI) | 0seo23@kaist.ac.kr |  |
| 김형태 (Hyeongtae Kim) | 학부 연구생 | Agentic AI; Prompt Optimization | kht0830@kaist.ac.kr |  |
| 정민호 (Jonathan Minho Chung) | 학부 연구생 | Large Language Models; Generative Models; Agentic AI | kht0830@kaist.ac.kr |  |
| 구자윤 (Jayun Ku) | 학부 연구생 | Agentic AI; Large Language Models | kujayun@kaist.ac.kr |  |
| 정희준 (Heejun Jung) | 학부 연구생 | Generative Model; Computer Vision | dezavva@kaist.ac.kr |  |
| 정지인 (Jiin Jung) | 학부 연구생 | Multimodal LLM; Agentic AI | jji01011@kaist.ac.kr |  |

## 졸업생과 이전 구성원

2026년 10월 28일 People 페이지의 Doctoral Alumni 8명과 Master's Alumni 24명이다. 졸업 시기는 2022–2026년으로 적혀 있으며 Junhyun Lee는 연도 표기가 없다. 학위·시기와 진로는 랩 표기를 따르고, 예정된 진로는 예정 표현을 유지했다. 고려대학교에서 연구실을 운영하던 시기의 졸업생도 포함한다. 박사후연구원으로 남은 사람은 현재 구성원 표와 졸업생 표에 함께 나온다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dogyun Park 박도균 | 박사 (Oct in 2026) | at Snap |
| Sanghyeok Lee 이상혁 | 박사 (Sep in 2026) | at Twelve Labs |
| Jihwan Park 박지환 | 박사 (Feb in 2026) | a post-doctoral researcher at KAIST |
| Jinyoung Park 박진영 | 박사 (Aug in 2025) | a post-doctoral researcher at KAIST |
| Seunghun Lee 이승훈 | 박사 (Aug in 2025) | a post-doctoral researcher at KAIST |
| Seongjun Yun 윤성준 | 박사 (Aug in 2022) | at Amazon |
| Bumsoo Kim 김범수 | 박사 (Feb in 2022) | an assistant professor (조교수) at Chung-Ang University (중앙대) after LG AI Research, and KakaoBrain |
| Junhyun Lee 이준현 | 박사 | an assistant professor (조교수) at HUFS (한국외대) |
| Byungoh Ko 고병오 | 석사 (Feb in 2026) | at EXAONE Lab, LG AI Research |
| Chanhyeong Yang 양찬형 | 석사 (Aug in 2025) | will join LG Energy Solution |
| Inho Kong 공인호 | 석사 (Aug in 2025) | an intern at Naver Cloud, and will join Kakao Entertainment as AI Research Scientist |
| Choi Min Hyuk 최민혁 | 석사 (Feb in 2025) | at JLK |
| Ju Han Cha 차주한 | 석사 (Aug in 2024) | at MORAI after 42dot |
| Shinyeong Noh 노신영 | 석사 (Aug in 2024) | at LG CNS |
| Eulrang Cho 조을랑 | 석사 (Feb in 2024) | a Ph.D. student at Carnegie Mellon University |
| Jihyeon Kang 강지현 | 석사 (Feb in 2024) | at Samsung Electronics |
| Jaewoon Byun 변재운 | 석사 (Feb in 2024) | at Hanwha Vision |
| Juyeon Ko 고주연 | 석사 (Feb in 2024) | at KT |
| Jooyeon Kim 김주연 | 석사 (Feb in 2024) | at Samsung Electronics |
| Hyeong Kyu Choi 최형규 | 석사 (Aug in 2023) | a Ph.D. student at the University of Wisconsin-Madison |
| Minkyu Jeon 전민규 | 석사 (Aug in 2023) | a Ph.D. student at Princeton University |
| Chiyoon Kim 김치윤 | 석사 (Aug in 2023) | at LG Electronics |
| Mouad Lasri | 석사 (Aug in 2023) |  |
| Jaewon Lee 이재원 | 석사 (Feb in 2023) | at AIMatics |
| Hwan Heo 허환 | 석사 (Feb in 2023) | at NCSOFT |
| Dasol Hwang 황다솔 | 석사 (Feb in 2023) | at LG AI Research |
| SeungJun Lee 이승준 | 석사 (Feb in 2023) | at LG AI Research |
| Sungdong Yoo 유성동 | 석사 (Aug in 2022) | at LG AI Research |
| Seungdong Yoa 여승동 | 석사 (Feb in 2022) | at LG AI Research |
| Hyeonjin Park 박현진 | 석사 (Feb in 2022) | at NAVER CLOVA |
| Chongkeun Paik 백종근 | 석사 (Feb in 2022) | at Samsung Electro-Mechanics |
| Youngjin Oh 오영진 | 석사 (Feb in 2022) | at Imagoworks |

## 최근 논문 목록 (2021–2026)

영상·언어 이해, 그래프 학습, 생성 모델, 입체 자료 처리와 관련 소자·계산 연구를 포함한 랩 Publications 페이지의 2021–2026년 구역이다. 학회·워크숍·학술지 논문과 arXiv 항목을 포함한 96항목이며, 제목·저자·발표처는 랩 표기를 따른다. 같은 제목의 학술지판과 사전 공개본이 별도 항목으로 올라온 경우 게시 항목을 각각 적었다. 김현우 교수는 2025년 2월 KAIST 연구실을 시작했으므로 이전 소속에서 수행한 연구도 섞여 있다. 연도는 목록의 연도 구역이며, 월·일 없이 게재 승인이나 채택으로 적힌 항목도 그 구역을 따른다. 학회 accepted는 「채택」, 학술지 accepted는 「게재 승인」으로 구분하고 Arxiv 표기는 사전 공개본이다. 원문에서 뜻을 밝히지 않은 별표는 역할로 해석하지 않았다.[^pubs][^home]

**2026**

- Ji Soo Lee, Jinyoung Park, Seohyun Lee, Jongha Kim, Joonmyung Choi, Jinsung Yoon, Hyunwoo J. Kim. "Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (채택)*.
- Minseo Yoon, Minseong Bae, Sojin Lee, Hyunwoo J. Kim. "PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (채택)*.
- Jaewon Chu, Jinwoo Seo, Jaewon Cho, Jeehye Na, Yunyang Xiong, Youngdae Kim, Hyunwoo J. Kim. "AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (채택)*.
- Sihyeon Kim, Seunghun Lee, Vikas Singh, Hyunwoo J. Kim. "Learning to Solve Generative ODEs Beyond the Linear Span". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (채택)*.
- Minseok Joo, Dogyun Park, Taehoon Lee, Kyujin Lee, Hyunwoo J. Kim. "Retrieve What’s Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation". *Advances in Neural Information Processing Systems (NeurIPS), 2026. (채택)*.
- Dong-Hee Kim, Seonwoo Choi, Changbeen Kim, Jungmyung Wi, Juyeon Ko, Youngju Choi, Il Hyeon Mun, Hyunwoo J. Kim, Donghyun Kim. "Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG". *Advances in Neural Information Processing Systems (NeurIPS), Evaluations and Datasets Track, 2026. (채택)*.
- Jinyoung Park, Sanghyeok Lee, Omar Zia Khan, Hyunwoo J. Kim, Joo-Kyung Kim. "HyperGraphPro: Progress-Aware Reinforcement Learning for Structure-Guided Hypergraph RAG". *Advances in Neural Information Processing Systems (NeurIPSW), Pre-to-Post Workshop, 2026. (채택)*.
- Seungbeom Park, Jaewon Chu, Hyunwoo J. Kim. "SkillCombiner: Optimizing Agent Skills via Edit Combination Search". *EMNLP Workshop (EMNLPW) REALM, 2026. (채택)*.
- Dohwan Ko, Ji Soo Lee, Pierce Chuang, Debojeet Chatterjee, Ashish Shenoy, Yichao Lu, Seungwhan Moon, Xin Luna Dong, Vikas Bhardwaj, Hyunwoo J. Kim. "SVMemAgent: A Streaming Video Memory Agent for Query-Agnostic Online Frame Selection". *Wearable AI Workshop, European Conference on Computer Vision Workshop (ECCVW), 2026. (채택)*.
- Byungoh Ko, Jinyoung Park, Jongha Kim, Jeehye Na, Jaewon Cho, Hyunwoo J. Kim. "Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization". *European Conference on Computer Vision (ECCV), 2026*.
- Injae Kim, Chaehyeon Kim, Minseong Bae, Minseok Joo, Hyunwoo J. Kim. "F⁴Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting". *European Conference on Computer Vision (ECCV), 2026*.
- Seohyun Lee, Seoung Choi, Dohwan Ko, Jongha Kim, Hyunwoo J. Kim. "VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement". *European Conference on Computer Vision (ECCV), 2026*.
- Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim. "MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models". *Computer Vision and Pattern Recognition (CVPR), 2026*.
- Jihwan Park, Chanhyeong Yang, Jinyoung Park, Taehoon Song, Hyunwoo J. Kim. "RegFormer: Transferable Relational Grounding for Efficient Weakly-Supervised Human-Object Interaction Detection". *Computer Vision and Pattern Recognition (CVPR), 2026*.
- Joonmyung Choi, Sanghyeok Lee, Jongha Kim, Sehyung Kim, Dohwan Ko, Jihyung Kil, Hyunwoo J. Kim. "DocPrune: Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning". *Computer Vision and Pattern Recognition (CVPR), 2026*.
- Jing-Jia Luo, Jiangjiang Xia , Baoxiang Pan , Yoo-Geun Ham , Xiaofeng Li , Wei Shanguan , Wei Xue , Yaqiang Wang , Bin Mu , Youngjoon Hong , Hao Li , Xiaohui Zhong , Kan Dai , Lei Bai , Fenghua Ling , Niklas Boers , Christopher Bretherton , Bin Chen , Dongjin Cho , Pierre Gentine , Zijie Guo , Xiaomeng Huang , Daehyun Kang , Hyunwoo J Kim, Jeong-Hwan Kim , Lili Lei , Fan Meng , Seol-Hee Oh , Bo Qin , Zixiong Shen , Qiming Sun , Yuheng Tang , Xuan Tong , Bingcheng Wan , Lina Wang , Ya Wang , Yiming Wang , Jiye Wu , Yi Xiao , Lina Yao , Song Yang , Chaoxia Yuan , Shijin Yuan , Tingzhao Yu , Mengchu Zhao. "AI for atmosphere-ocean sciences: advancements, challenges, and ways forward". *National Science Review, 2026 (게재 승인)*.
- Inho Kong\*, Sojin Lee\*, Youngjoon Hong, Hyunwoo J. Kim. "Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance". *International Conference on Learning Representations (ICLR), 2026*.
- Dogyun Park, Moayed Haji-Ali, Yanyu Li, Willi Menapace, Sergey Tulyakov, Hyunwoo J. Kim, Aliaksandr Siarohin, Anil Kag. "SPRINT: Sparse-Dense Residual Fusion for Efficient Diffusion Transformers". *International Conference on Learning Representations (ICLR), 2026*.
- Jongha Kim, Byungoh Ko, Jeehye Na, Jinsung Yoon, Hyunwoo J. Kim. "Relevance-aware Multi-context Contrastive Decoding for Retrieval-augmented Visual Question Answering". *The IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2026*.
- Jihwan Park, Taehoon Song, Sanghyeok Lee, Miso Choi, Hyunwoo J. Kim. "Transferable Model-agnostic Vision-Language Model Adaptation for Efficient Weak-to-Strong Generalization". *AAAI Conference on Artificial Intelligence (AAAI), 2026. (Oral presentation)*.
- Jinyoung Park, Minseong Bae, Jeehye Na, Hyunwoo J. Kim. "Improving Large Molecular Language Model via Relation-aware Multimodal Collaboration". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.
- Jongha Kim, Minseong Bae, Sanghyeok Lee, Jinsung Yoon, Hyunwoo J. Kim. "TabFlash: Efficient Table Understanding with Progressive Question Conditioning and Token Focusing". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.
- Jongha Kim, Jihwan Park, Jinyoung Park, Jinyoung Kim, Sehyung Kim, Hyunwoo J. Kim. "Improved Query Specialization for Transformer-based Visual Relationship Detection". *Information Sciences, 2026*.
- Jinyoung Park, Juyeon Ko, Sanghyeok Lee, Joonmyung Choi, Hyunwoo J. Kim. "Parameter-Efficient Fine-Tuning via Meta-Regularizer". *International Journal of Computer Vision (IJCV), 2026*.

**2025**

- Haewon Seo, Min-Kyu Song, Hyun Woo Ko, Ji-Hoon Kang, Giho Lee, SunYoung Park, Hyunwoo J. Kim, Sungchul Mun, Jeehwan Kim, Min-Chul Park, and Kyung Joong Yoon. "In-cell neuromorphic computing in solid oxide fuel cells for bifunctional electrochemical power generation and artificial intelligence". *Cell Reports Physical Science, 2025 (게재 승인)*.
- Dogyun Park, Taehoon Lee, Minseok Joo, Hyunwoo J. Kim. "Blockwise Flow Matching: Improving Flow Matching Models For Efficient High-Quality Generation". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Jinyoung Park, Jeehye Na, Jinyoung Kim, Hyunwoo J. Kim. "DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Jaewon Chu, Seunghun Lee, Hyunwoo J. Kim. "PRESTO: Preimage-Informed Instruction Optimization for Prompting Black-Box LLMs". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Chanhyeong Yang, Taehoon Song, Jihwan Park, Hyunwoo J. Kim. "Visual Diversity and Region-aware Prompt Learning for Zero-shot HOI Detection". *Advances in Neural Information Processing Systems (NeurIPS), 2025*.
- Ji Soo Lee, Byungoh Ko, Jaewon Cho, Howoong Lee, Jaewoon Byun, Hyunwoo J. Kim. "Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization". *Empirical Methods in Natural Language Processing (EMNLP), Findings 2025*.
- Dohwan Ko\*, Ji Soo Lee\*, Minhyuk Choi, Zihang Meng, Hyunwoo J. Kim. "Bidirectional Likelihood Estimation with Multi-Modal Large Language Models for Text-Video Retrieval". *International Conference on Computer Vision (ICCV), 2025. (Highlight)*.
- Joonmyung Choi\*, Sanghyeok Lee\*, Byungoh Ko, Eunseo Kim, Jihyung Kil, Hyunwoo J. Kim. "Representation Shift: Unifying Token Compression with FlashAttention". *International Conference on Computer Vision (ICCV), 2025. (채택)*.
- Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Lemeng Wu, Jun Chen, Chenchen Zhu, Zechun Liu, Fanyi Xiao, Balakrishnan Varadarajan, Florian Bordes, Zhuang Liu, Hu Xu, Hyunwoo J. Kim, Bilge Soran, Raghuraman Krishnamoorthi, Mohamed Elhoseiny, Vikas Chandra. "LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding". *International Conference on Machine Learning (ICML), 2025*.
- Dohoon Lee, Jaehyun Park, Hyunwoo J. Kim, Kyogu Lee. "Multidimensional Adaptive Coefficient for Inference Trajectory Optimization in Flow and Diffusion". *International Conference on Machine Learning (ICML), 2025*.
- Yujin Kim\*, Hyunsoo Kim\*, Hyunwoo J. Kim, Suhyun Kim. "When Model Knowledge meets Diffusion Model: Diffusion-assisted Data-free Image Synthesis with Alignment of Domain and Class". *International Conference on Machine Learning (ICML), 2025*.
- Sanghyeok Lee, Joonmyung Choi, Hyunwoo J. Kim. "EfficientViM: Efficient Vision Mamba with Hidden State Mixer based State Space Duality". *Computer Vision and Pattern Recognition (CVPR), 2025*.
- Jinyoung Park, Seongjun Yun, Hyeonjin Park, Jaewoo Kang, Jisu Jeong, Kyung-Min Kim, Jung-Woo Ha, and Hyunwoo J. Kim. "Deformable Graph Transformer". *Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2025*.
- Jisu Jang, Jung Pyo Hong, Sang-Jun Kim, Jongtae Ahn, Byoung-Soo Yu, Jaewon Han, Kihyun Lee, Aelim Ha, Eunki Yoon, Wonsik Kim, Suyeon Jo, Hyun Woo Ko, Seon Kyu Yoon, Takashi Taniguchi, Kenji Watanabe, Hogil Baek, Dae-Yeon Kim, Kimoon Lee, Sungchul Mun, Kyu Hyoung Lee, Soohyung Park, Kwanpyo Kim, Young Jae Song, Seung Ah Lee, Hyunwoo J. Kim, Jae Won Shim, Gunuk Wang, Ji-Hoon Kang, Min-Chul Park and Do Kyung Hwang. "Conductive-bridge interlayer contacts for two-dimensional optoelectronic devices". *Nature Electronics, 2025*.
- Seunghun Lee, Jinyoung Park, Jaewon Chu, Minseo Yoon, Hyunwoo J. Kim. "Latent Bayesian Optimization via Autoregressive Normalizing Flows". *International Conference on Learning Representations (ICLR), 2025. (Oral presentation)*.
- Sehyung Kim\*, Chanhyeong Yang\*, Jihwan Park, Taehoon Song, Hyunwoo J. Kim. "Super-class guided Transformer for Zero-Shot Attribute Classification". *AAAI Conference on Artificial Intelligence (AAAI), 2025*.
- Ji Soo Lee\*, Jongha Kim\*, Jeehye Na, Jinyoung Park, Hyunwoo J. Kim. "VidChain: Chain-of-Tasks with Metric-based Direct Preference Optimization for Dense Video Captioning". *AAAI Conference on Artificial Intelligence (AAAI), 2025*.

**2024**

- Jinyoung Park, Minseong Bae, Dohwan Ko, Hyunwoo J. Kim. "LLaMo: Large Language Model-based Molecular Graph Assistant". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Dogyun Park, Sojin Lee, Sihyeon Kim, Taehoon Lee, Youngjoon Hong\*, Hyunwoo J. Kim\*. "Constant Acceleration Flow". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Jaewon Chu\*, Jinyoung Park\*, Seunghun Lee, Hyunwoo J. Kim. "Inversion-based Latent Bayesian Optimization". *Advances in Neural Information Processing Systems (NeurIPS), 2024*.
- Jinyoung Park, Minseok Joo, Joo-Kyung Kim, Hyunwoo J. Kim. "Generative Subgraph Retrieval for Knowledge Graph–Grounded Dialog Generation". *Empirical Methods in Natural Language Processing (EMNLP), 2024*.
- Sojin Lee\*, Dogyun Park\*, Inho Kong, Hyunwoo J. Kim. "Diffusion Prior-Based Amortized Variational Inference for Noisy Inverse Problems". *European Conference on Computer Vision (ECCV), 2024. (Oral presentation)*.
- Sotirios Panagiotis Chytas,  Hyunwoo J. Kim, Vikas Singh. "Understanding Multi-compositional Learning in Vision and Language Models via Category Theory". *European Conference on Computer Vision (ECCV), 2024*.
- Juyeon Ko\*, Inho Kong\*, Dogyun Park, Hyunwoo J. Kim. "Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis". *International Conference on Machine Learning (ICML), 2024*.
- Joonmyung Choi\*, Sanghyeok Lee\*, Jaewon Chu, Minhyuk Choi, Hyunwoo J. Kim. "vid-TLDR: Training Free Token merging for Light-weight Video Transformer". *Computer Vision and Pattern Recognition (CVPR), 2024*.
- Sanghyeok Lee\*, Joonmyung Choi\*, Hyunwoo J. Kim. "Multi-criteria Token Fusion with One-step-ahead Attention for Efficient Vision". *Computer Vision and Pattern Recognition (CVPR), 2024*.
- Jongha Kim\*, Jihwan Park\*, Jinyoung Park\*, Jinyoung Kim, Sehyung Kim, Hyunwoo J. Kim. "Groupwise Query Specialization and Quality-Aware Multi-Assignment for Transformer-based Visual Relationship Detection". *Computer Vision and Pattern Recognition (CVPR), 2024*.
- Jinyoung Park, Juyeon Ko, Hyunwoo J. Kim. "Prompt Learning via Meta-Regularization". *Computer Vision and Pattern Recognition (CVPR), 2024*.
- Jooyeon Kim\*, Eulrang Cho\*, Sehyung Kim, Hyunwoo J. Kim. "Retrieval-Augmented Open-Vocabulary Object Detection". *Computer Vision and Pattern Recognition (CVPR), 2024*.
- Dogyun Park, Sihyeon Kim, Sojin Lee, Hyunwoo J. Kim. "Domain-agnostic Latent Diffusion Models for Synthesizing High-Quality Implicit Neural Representations". *International Conference on Learning Representations (ICLR), 2024*.
- Juhan Cha\*, Minseok Joo\*, Jihwan Park, Sanghyeok Lee, Hyunwoo J. Kim. "Robust Multimodal 3D Object Detection via Modality-Agnostic Decoding and Proximity-based Modality Ensemble". *Arxiv, 2024*.

**2023**

- Dohwan Ko\*, Ji Soo Lee\*, Woo-Young Kang, Byungseok Roh, Hyunwoo J. Kim. "Large Language Models are Temporal and Causal Reasoners for Video Question Answering". *Empirical Methods in Natural Language Processing (EMNLP), 2023*.
- Hyeong Kyu Choi, Seunghun Lee, Jaewon Chu, Hyunwoo J. Kim. "NuTrea: Neural Tree Search for Context-guided Multi-hop KGQA". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Seunghun Lee\*, Jaewon Chu\*, Sihyeon Kim\*, Juyeon Ko, Hyunwoo J. Kim. "Advancing Bayesian Optimization via Learning Correlated Latent Spaces". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Injae Kim\*, Minhyuk Choi\*, Hyunwoo J. Kim. "Unconstrained Pose Prior-Free Neural Radiance Field". *Advances in Neural Information Processing Systems (NeurIPS), 2023*.
- Dohwan Ko, Ji Soo Lee, Miso Choi, Jaewon Chu, Jihwan Park, Hyunwoo J. Kim. "Open-Vocabulary Video Question Answering: A New Benchmark for Evaluating the Generalizability of Video Question Answering Models". *International Conference on Computer Vision (ICCV), 2023*.
- Eulrang Cho\*,  Jooyeon Kim\*, Hyunwoo J. Kim. "Distribution-Aware Prompt Tuning for Vision-Language Models". *International Conference on Computer Vision (ICCV), 2023*.
- Sihyeon Kim, Minseok Joo, Jaewon Lee, Juyeon Ko, Juhan Cha, Hyunwoo J. Kim. "Semantic-Aware Template Learning via Part Deformation Consistency". *International Conference on Computer Vision (ICCV), 2023*.
- Dongjun Lee\*, Seokwon Song\*, Jihee Suh, Joonmyung Choi, Sanghyeok Lee, Hyunwoo J. Kim. "Read-only Prompt Optimization for Vision-Language Few-shot Learning". *International Conference on Computer Vision (ICCV), 2023*.
- Hwan Heo, Taekyung Kim, Jiyoung Lee, Jaewon Lee, Soohyun Kim, Hyunwoo J. Kim\*, Jin-Hwa Kim\*. "Robust Camera Pose Refinement for Multi-Resolution Hash Encoding". *In International Conference on Machine Learning (ICML), 2023*.
- Dohwan Ko\*, Joonmyung Choi\*, Hyeong Kyu Choi, Kyoung-Woon On, Byungseok Roh, Hyunwoo J. Kim. "MELTR: Meta Loss Transformer for Learning to Fine-tune Video Foundation Models". *Computer Vision and Pattern Recognition (CVPR), 2023*.
- Jinyoung Park\*, Sanghyeok Lee\*, Sihyeon Kim, Yunyang Xiong, Hyunwoo J. Kim. "Self-positioning Point-based Transformer for Point Cloud Understanding". *Computer Vision and Pattern Recognition (CVPR), 2023*.
- Jinyoung Park\*, Hyeong Kyu Choi\*, Juyeon Ko\*, Hyeonjin Park, Ji-Hoon Kim, Jisu Jeong, Kyungmin Kim, Hyunwoo J. Kim. "Relation-aware Language-Graph Transformer for Question Answering". *AAAI Conference on Artificial Intelligence (AAAI), 2023*.
- Tae Hyuk Kim, Byoung-Soo Yu, Hyun Woo Ko, Na Won Park, Muhammad Ahsan Saeed,Jongtae Ahn, Suyeon Jo, Dae-Yeon Kim, Seon Kyu Yoon, Kwang-Hoon Lee, Sang Young Jeong, Han Young Woo, Hyunwoo J. Kim, Tae Geun Kim,\* JaeHong Park,\*Min-Chul Park,\* Do Kyung Hwang,\* and Jae Won Shim\*. "Self-Powering Sensory Device with Multi-Spectrum Image Realization for Smart Indoor Environments". *Advanced Materials, 2023*.
- Hyeong Kyu Choi, Chong Keun Paik, Hyun Woo Ko, Min-Chul Park, Hyunwoo J. Kim. "Recurrent DETR: Transformer-based Object Detection for Crowded Scenes". *IEEE ACCESS, 2023*.
- Dasol Hwang, Sojin Lee, Joonmyung Choi, Je-Keun Rhe, Hyunwoo J. Kim. "Robust Auxiliary Learning with Weighting Function for Biased Data". *Information Sciences, 2023*.
- Bryce Chudomelka, Youngjoon Hong\*, John Morgan, Hyunwoo Kim\*, Jinyoung Park. "Deep Neural Network for Solving Differential Equations Motivated by Legendre-Galerkin Approximation". *International Journal of Numerical Analysis and Modeling, 2023*.
- Hodong Kim, Changhee Hahn, Hyunwoo J. Kim, Youngjoo Shin, Junbeom Hur. "Deep Learning based Detection for Multiple Cache Side-channel Attacks". *IEEE Transactions on Information Forensics & Security (TIFS), 2023*.
- Injae Kim\*, Jongha Kim\*, Joonmyung Choi, Hyunwoo J. Kim. "Concept Bottleneck with Visual Concept Filtering for Explainable Medical Image Classification". *MICCAI 2023 1st International Workshop on Foundation Models for General Medical AI (MedAGI), 2023. (Oral Presentation)*.

**2022**

- Sanghyeok Lee\*, Minkyu Jeon\*, Injae Kim, Yunyang Xiong, Hyunwoo J. Kim. "SageMix: Saliency-Guided Mixup for Point Clouds". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Byeongkeun Ahn, Chiyoon Kim, Youngjoon Hong\*, Hyunwoo J. Kim\*. "Invertible Monotone Operators for Normalizing Flows". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Hyeong Kyu Choi\*, Joonmyung Choi\*, Hyunwoo J. Kim. "TokenMixup: Efficient Attention-guided Token-level Data Augmentation for Transformers". *Advances in Neural Information Processing Systems (NeurIPS), 2022*.
- Minkyu Jeon, Hyeonjin Park, Hyunwoo J. Kim\*, Michael Morley\*, Hyunghoon Cho\*. "k-SALSA: k-anonymous synthetic averaging of retinal images via local style alignment". *European Conference on Computer Vision (ECCV), 2022*.
- Dohwan Ko, Joonmyung Choi, Juyeon Ko, Shinyeong Noh, Kyoung-Woon On, Eun-Sol Kim, Hyunwoo J. Kim. "Video-Text Representation Learning via Differentiable Weak Temporal Alignment". *Computer Vision and Pattern Recognition (CVPR), 2022*.
- Jihwan Park, SeungJun Lee, Hwan Heo, Hyeong Kyu Choi, Hyunwoo J. Kim. "Consistency Learning via Decoding Path Augmentation for Transformers in Human Object Interaction Detection". *Computer Vision and Pattern Recognition (CVPR), 2022*.
- Jinyoung Park, Sungdong Yoo, Jihwan Park, Hyunwoo J. Kim. "Deformable Graph Convolutional Networks". *AAAI Conference on Artificial Intelligence (AAAI), 2022*.
- Youngjin Oh\*, Minkyu Jeon\*, Dohwan Ko, Hyunwoo J. Kim. "Randomly Shuffled Convolution for Self-Supervised Representation Learning". *Information Sciences, 2022*.
- Seongjun Yun, Minbyul Jeong , Sungdong Yoo, Seunghun Lee, Sean S. Yi , Raehyun Kim , Jaewoo Kang, Hyunwoo J. Kim. "Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs". *Neural Networks (NN), 2022*.
- Hyojung Choi, Chanhwi Jung, Taein Kang, Hyunwoo J. Kim, Il-Youp Kwak. "Explainable Time-series Prediction using a Residual Network and Gradient-based methods". *IEEE ACCESS, 2022*.
- Wuming Gong, Hyunwoo J. Kim, Daniel J Garry, Il-Youp Kwak. "Single cell lineage reconstruction using distance-based algorithms and the R package, DCLEAR". *BMC Bioinformatics, 2022*.
- Jinyoung Park, Seongjun Yun, Hyeonjin Park, Jaewoo Kang, Jisu Jeong, Kyung-Min Kim, Jung-woo Ha, Hyunwoo J. Kim. "Deformable Graph Transformer". *Arxiv, 2022*.

**2021**

- Hyeonjin Park\*, Seunghun Lee\*, Sihyeon Kim, Jinyoung Park, Jisu Jeong, Kyung-Min Kim, Jung-Woo Ha, Hyunwoo J. Kim. "Metropolis-Hastings Data Augmentation for Graph Neural Networks". *Advances in Neural Information Processing Systems (NeurIPS), 2021*.
- Seongjun Yun, Seoyoon Kim, Junhyun Lee, Jaewoo Kang, Hyunwoo J. Kim. "Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction". *Advances in Neural Information Processing Systems (NeurIPS), 2021*.
- Sihyeon Kim\*, Sanghyeok Lee\*, Dasol Hwang,  Jaewon Lee, Seong Jae Hwang, Hyunwoo J. Kim. "Point Cloud Augmentation with Weighted Local Transformations". *International Conference on Computer Vision (ICCV), 2021*.
- Bumsoo Kim, Junhyun Lee, Jaewoo Kang, Eun-Sol Kim, Hyunwoo J. Kim. "HOTR: End-to-End Human-Object Interaction Detection with Transformers". *Computer Vision and Pattern Recognition (CVPR), 2021. (Oral presentation)*.
- Hyeonjin Park\*, Seunghun Lee\*, Dasol Hwang, Jisu Jeong, Kyung-Min Kim, Jung-Woo Ha, and Hyunwoo J. Kim. "Learning Augmentation for GNNs with Consistency Regularization". *IEEE ACCESS, 2021*.
- Seungdong Yoa, Minkyu Jeon, Youngjin Oh, Hyunwoo J. Kim. "Learning to Balance Local Losses via Meta-Learning". *IEEE ACCESS, 2021*.
- Seungdong Yoa\*, Jinyoung Park\*, Hyunwoo J. Kim. "Learning Non-parametric Surrogate Losses with Correlated Gradients". *IEEE ACCESS, 2021*.
- Hwan Heo\*, Dohwan Ko\*, Jaewon Lee\*, Youngjoon Hong, Hyunwoo J. Kim. "Search-and-Attack: Temporally SparseAdversarial Perturbations on Videos". *IEEE ACCESS, 2021*.
- Seungdong Yoa\*, Seungjun Lee\*, Chiyoon Kim, and Hyunwoo J. Kim. "Self-Supervised Learning for Anomaly Detection with Dynamic Local Augmentation". *IEEE ACCESS, 2021*.
- Dasol Hwang\*, Jinyoung Park\*, Sunyoung Kwon, Kyung-Min Kim, Jung-Woo Ha, Hyunwoo J. Kim. "Self-supervised Auxiliary Learning for Graph Neural Networks via Meta-Learning". *Arxiv, 2021*.
- Seongjun Yun, Minbyul Jeong, Sungdong Yoo, Seunghun Lee, Sean S. Yi, Raehyun Kim, Jaewoo Kang, Hyunwoo J. Kim. "Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs". *Arxiv, 2021*.

2022년 논문 DCLEAR는 세포 계보(세포 분열로 이어지는 세포 사이의 관계)를 복원하는 R(통계 계산용 프로그래밍 언어)용 소프트웨어다. 세포 쌍 사이의 차이를 표로 나타낸 거리 행렬을 추정한 뒤 그 표에서 계보의 가지 구조를 복원하며, 거리 행렬 추정 방법 두 가지를 제안했다.[^dclear]

## 과제

첫 화면에 게시된 과제 가운데 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 3건이다. 2025년 2월 KAIST 연구실 시작 전부터 이어진 과제도 포함한다. 기간과 사업·협력 기관 표기는 누리집 게시 내용이다.[^home]

- Multilingual Personalized AI Tutors (기간 2024–2027; 협력 기관 IITP, Google, MLV, KAIST)
- Extreme Weather Forecasting (CLIMECAST) (기간 2024–2027; 사업 한계도전 R&D 프로젝트)
- Hyperscale AI project with KakaoBrain (기간 2021–2024; 협력 기관 KakaoBrain)

## 수상과 선정

첫 화면의 날짜 있는 소식 중 2021년 10월 13일–2026년 10월 13일에 해당하는 13건이다. 2025년 2월 KAIST 연구실 시작 전의 교수·연구실·구성원 수상도 포함한다. 날짜는 소식에 적힌 날짜다.[^home]

- 2025-10-18 · 주재원(Jaewon Chu)이 NeurIPS 2025 우수 심사자로 선정됐다.
- 2025-08-29 · 연구팀이 제4회 Weather-AI Boostcamp에서 Honorable Mention(입선)을 받았다.
- 2025-08-05 · 김현우 교수가 KCCV Test-of-Time Award(이상욱 학술상)를 받았다.
- 2025-06-24 · 공저 논문이 한국방송·미디어공학회 2025 하계학술대회 Best Paper Award를 받았다.
- 2024-11-15 · 박진영(Jinyoung Park)이 Google Ph.D Fellowship을 받았다.
- 2024-09-25 · ICT Challenge 2024 장관상을 받았다.
- 2024-02-23 · 고도환(Dohwan Ko)이 Outstanding Paper Award를 받았다.
- 2024-02-21 · 박진영(Jinyoung Park)이 KU Achievement Award를 받았다.
- 2022-11-24 · 2022 AI Grand Challenge에서 KEIT Award를 받았다(누리집은 한국전자기술연구원장상으로 병기).
- 2022-05-26 · Google의 GCP Credit Award를 받았다.
- 2022-05-05 · 김현우 교수가 2021년 가을 Deep Learning 강의로 석탑강의상(Granite Tower Lecture Award)을 받았다.
- 2022-01-25 · 박진영(Jinyoung Park)이 BK21 KU-Future Talent Fellowship에 선정됐다.
- 2021-12-09 · 재난대응 드론을 위한 2021 AI Grand Challenge에서 장관상(3위)을 받았다.

## 소식

첫 화면의 날짜 있는 소식 중 2021년 10월 13일–2026년 10월 13일에 해당하는 연구·학술 활동 52건이다. 김현우 교수가 고려대학교에서 연구실을 이끌던 시기와 KAIST 연구실 시작 뒤의 소식이 함께 있다. 날짜와 앞으로 맡을 활동의 예정 표현은 게시 내용을 따른다.[^home]

- 2026-09-26 · NeurIPS 2026에 논문 7편이 채택됐다(본회의 5편, Evaluations and Datasets Track 1편, 워크숍 1편).
- 2026-08-23 · 김현우 교수가 AAAI 2027 및 AAAI 2027 AI Alignment Track의 Senior Program Committee를 맡을 예정이다.
- 2026-06-19 · 김현우 교수가 Transactions on Machine Learning Research의 Action Editor를 맡을 예정이다.
- 2026-06-18 · ECCV 2026에 논문 3편이 채택됐다.
- 2026-06-14 · 김현우 교수가 WACV 2027의 Area Chair를 맡을 예정이다.
- 2026-02-21 · CVPR 2026에 논문 3편이 채택됐다.
- 2026-01-27 · TransMiter 연구(AAAI 2026 구두 발표)가 AI타임즈·조선일보·YTN에 소개됐다.
- 2026-01-26 · ICLR 2026에 논문 2편이 채택됐다.
- 2025-11-20 · 김현우 교수가 ICML 2026의 Area Chair를 맡을 예정이다.
- 2025-11-11 · WACV 2026에 논문 1편이 채택됐다.
- 2025-11-08 · AAAI 2026에 논문 3편이 채택됐다.
- 2025-09-18 · NeurIPS 2025에 논문 4편이 채택됐다.
- 2025-09-05 · International Journal of Computer Vision에 논문 1편의 게재가 승인됐다.
- 2025-09-02 · Information Sciences에 논문 1편의 게재가 승인됐다.
- 2025-08-21 · EMNLP 2025 Findings에 논문 1편이 채택됐다.
- 2026-08-17 · 김현우 교수가 CVPR 2026의 Area Chair를 맡을 예정이다(누리집 기재 날짜).
- 2026-08-16 · 김현우 교수가 ICLR 2026의 Area Chair를 맡을 예정이다(누리집 기재 날짜).
- 2025-07-25 · ICCV 2025 논문 1편이 Highlight로 선정됐다.
- 2025-06-26 · ICCV 2025에 논문 2편이 채택됐다.
- 2025-06-23 · 김현우 교수가 WACV 2026의 Area Chair를 맡을 예정이다.
- 2025-05-02 · ICML 2025에 논문 3편이 채택됐다.
- 2025-02-27 · CVPR 2025에 논문 1편이 채택됐다.
- 2025-02-21 · Transactions on Pattern Analysis and Machine Intelligence에 논문 1편의 게재가 승인됐다.
- 2025-02-05 · Nature Electronics에 논문 1편의 게재가 승인됐다.
- 2025-01-23 · ICLR 2025에 논문 1편이 구두 발표로 채택됐다.
- 2024-12-09 · AAAI 2025에 논문 2편이 채택됐다.
- 2024-09-26 · NeurIPS 2024에 논문 3편이 채택됐다.
- 2024-09-21 · EMNLP 2024 본회의에 논문 1편이 채택됐다.
- 2024-09-14 · 김현우 교수가 CVPR 2025의 Area Chair를 맡을 예정이다.
- 2024-08-20 · 김현우 교수가 ICLR 2025의 Area Chair를 맡을 예정이다.
- 2024-08-13 · ECCV 2024 논문 1편이 구두 발표로 채택됐다.
- 2024-07-02 · ECCV 2024에 논문 2편이 채택됐다.
- 2024-06-19 · 한계도전 R&D 과제 제안이 선정됐다.
- 2024-05-02 · ICML 2024에 논문 1편이 채택됐다.
- 2024-02-27 · CVPR 2024에 논문 5편이 채택됐다.
- 2024-01-17 · ICLR 2024에 논문 1편이 채택됐다.
- 2023-10-31 · MLV Lab이 2023년 AI 학회에서 논문 12편을 발표했다고 알렸다.
- 2023-10-12 · 김현우 교수가 MedAGI(MICCAI의 의료 범용 AI 기초 모델 워크숍)의 Organizing Chair를 맡았다.
- 2023-10-07 · EMNLP 2023에 논문 1편이 채택됐다.
- 2023-09-22 · NeurIPS 2023에 논문 3편이 채택됐다.
- 2023-08-14 · 김현우 교수가 CVPR 2024의 Area Chair를 맡을 예정이다.
- 2023-07-14 · ICCV 2023에 논문 4편이 채택됐다.
- 2023-04-25 · ICML 2023에 논문 1편이 채택됐다.
- 2023-02-28 · CVPR 2023에 논문 2편이 채택됐다.
- 2023-01-15 · Information Sciences에 논문 1편의 게재가 승인됐다.
- 2022-11-19 · Naver AI Lab과 공저한 논문 1편이 AAAI 2023에 채택됐다.
- 2022-09-15 · NeurIPS 2022에 논문 3편이 채택됐다.
- 2022-07-04 · ECCV에 논문 1편이 채택됐다.
- 2022-05-27 · Neural Networks에 논문 1편의 게재가 승인됐다.
- 2022-03-02 · CVPR 2022에 논문 2편이 채택됐다.
- 2021-12-01 · AAAI 2022에 논문 1편이 채택됐다.
- 2021-10-19 · 카카오브레인과의 Hyperscale AI 과제(2021–2024)를 알렸다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 크래프톤 SoC 빌딩(E3-5) 206·207호[^contact]
- 교수 연구실: 같은 건물 205호[^contact][^faculty]
- 연구실 전화: 042-350-7718[^contact]
- 교수 전화: 042-350-3518[^contact][^people]
- 교수 이메일: hyunwoojkim@kaist.ac.kr[^people]
[^home]: Machine Learning & Vision Lab, Home. KAIST 연구실은 2025년 2월 시작했으며, 영상·언어 이해와 분자·기상 자료의 이해·생성 및 계산 효율을 연구한다고 소개한다. <https://www.hyunwoojkim.com/> 관측 2026-10-27.
[^labinfo]: KAIST 전산학부, 기계학습 및 비전 연구실 소개. 범용인공지능, 비디오·언어 모델과 분자 구조 이해·생성, 그래프의 멀티모달 시계열 자료 및 극한 기상 예측을 설명한다. <https://cs.kaist.ac.kr/research/labView?sn=122&menu=64> 관측 2026-10-27.
[^faculty]: KAIST 전산학부, 김현우 교수 상세 소개. 부교수, 2025년 KAIST 부임, 전공·박사 학위·교수 연구실 표기. <https://cs.kaist.ac.kr/people/view?idx=652&kind=faculty&menu=170> 관측 2026-10-28.
[^people]: Machine Learning & Vision Lab, People. 교수 이력·주 소속과 겸무, 현재 구성원·졸업생·연구 주제·학교 이메일. <https://www.hyunwoojkim.com/people> 관측 2026-10-28.
[^research]: Machine Learning & Vision Lab, Research. 연구실은 여러 종류의 자료로 과제를 배우는 범용 학습 시스템, 그래프 신경망과 과학 자료 학습, 이미지·영상·분자 생성 모델, 장면 이해와 입체 시각 알고리즘, 모델의 불확실성과 공격·방어 및 의료 영상의 표현·학습 방법을 연구한다고 설명한다. <https://www.hyunwoojkim.com/research> 관측 2026-10-28.
[^pubs]: Machine Learning & Vision Lab, Publications. 2021–2026년 학회·워크숍·학술지·arXiv 게시 목록. <https://www.hyunwoojkim.com/publications> 관측 2026-10-28.
[^contact]: Machine Learning & Vision Lab, Contact. E3-5 학생 연구실 206·207호, 교수 연구실 205호와 연락처. <https://www.hyunwoojkim.com/contact> 관측 2026-10-28.
[^dclear]: W. Gong, H. J. Kim, D. J. Garry, I.-Y. Kwak, BMC Bioinformatics (2022). <https://doi.org/10.1186/s12859-022-04633-x> 초록 기준(Crossref 등록 초록). 관측 2026-10-28.
[^p1]: J. Park, J. Na, J. Kim, H. J. Kim, arXiv (온라인 2025-06-09). <https://doi.org/10.48550/arXiv.2506.07464> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.07464> 관측 2026-10-28.
[^p2]: S. Lee 외, H. J. Kim, arXiv (온라인 2026-07-01). <https://doi.org/10.48550/arXiv.2607.00446> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2607.00446> 관측 2026-10-28.
[^p3]: J. Kim 외, H. J. Kim, arXiv (온라인 2025-11-17). <https://doi.org/10.48550/arXiv.2511.13283> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2511.13283> 관측 2026-10-28.
[^p4]: J. Park 외, H. J. Kim, arXiv (온라인 2025-08-12). <https://doi.org/10.48550/arXiv.2508.08604> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2508.08604> 관측 2026-10-28.
[^p5]: J. Park, M. Bae, J. Na, H. J. Kim, arXiv (온라인 2026-01-18). <https://doi.org/10.48550/arXiv.2601.12256> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.12256> 관측 2026-10-28.
[^p6]: I. Kong, S. Lee, Y. Hong, H. J. Kim, arXiv (온라인 2026-03-04). <https://doi.org/10.48550/arXiv.2603.03692> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.03692> 관측 2026-10-28.
[^p7]: D. Park 외, A. Kag, arXiv (온라인 2025-10-24). <https://doi.org/10.48550/arXiv.2510.21986> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.21986> 관측 2026-10-28.
[^p8]: I. Kim 외, H. J. Kim, arXiv (온라인 2026-03-22). <https://doi.org/10.48550/arXiv.2603.21304> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.21304> 관측 2026-10-28.

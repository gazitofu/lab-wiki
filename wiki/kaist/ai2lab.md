# AI² 연구실 (AI² Lab)

**KAIST 전산학부 · 김대영 교수**

- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^ml][^p5], 멀티모달 AI[^ml][^p3][^p4], 대형 언어 모델[^ml][^bscore], 엣지 컴퓨팅·엣지 AI[^ml], 모델 경량화·양자화[^ml], 그래프 기계학습·지식 그래프[^p2], 책임 있는 AI·공정성[^p4][^bscore]
- 홈페이지: <https://www.ai2lab.kaist.ac.kr/>
- 근거: [읽은 자료와 표기 차이](ai2lab-sources.md)

> 사물인터넷의 자료를 표준에 맞게 연결하고 공유하는 플랫폼과, 글·영상·음성을 이해하고 생성하는 인공지능을 연구한다. 기기 안에서 동작하는 언어 모델, 모델의 편향과 학습 유지, 영상 복원·가상 착의·의료영상 분석을 함께 다룬다.

## 무엇을 연구하나

AI² 연구실은 **사물인터넷과 기계학습**을 두 축으로 삼는다. 사물인터넷(IoT, Internet of Things)은 통신망으로 연결된 사물들이 자료를 주고받고 서비스를 제공하는 체계다. 연구실의 Oliot은 GS1 국제표준을 바탕으로 사물을 식별하고, 자료를 모으고 공유하며, 필요한 서비스를 등록하고 찾는 공개 소프트웨어 플랫폼이다. 연구실은 서로 다른 기관·시스템이 자료를 함께 쓰도록 자료의 표현과 공유 방식을 설계한다. 데이터공학(자료를 모으고 가공·저장·공유하는 체계를 설계하는 분야)과 기계학습(자료에서 규칙을 배워 예측이나 판단을 수행하는 방법)을 연결하는 방향이다. IoT 소개는 블록체인(여러 참여자가 연결된 기록 묶음을 나눠 갖고 함께 검증하는 분산 장부 기술)을 이용한 자료·서비스 공유와 스마트시티·선박·버스 적용을 설명한다.[^labview][^iot][^prof]

대표 논문은 자료를 표현하는 표준이 서로 달라 함께 쓰기 어려운 문제와, 제품의 복잡한 이력을 조회하는 문제를 다룬다. 첫 논문은 사건 중심의 EPCIS(Electronic Product Code Information Service: 사물과 관련된 사건 정보를 공유하는 표준)와 개체 중심의 NGSI(Next Generation Services Interface: 개체를 중심으로 자료를 표현하고 주고받는 표준)를 연결하는 OLIOT Mediation Gateway를 제안한다. 게이트웨이(서로 다른 체계 사이에서 자료를 전달·변환하는 연결 시스템)를 육류 공급망의 정보 시스템 통합 사례에 적용했다.[^p1] 다른 논문은 디지털 제품 여권(DPP, Digital Product Passport: 제품의 이력 정보를 담아 공유하는 디지털 기록)을 위해 EPCIS 2.0의 사건 자료를 지식 그래프(대상과 그 관계를 점과 선으로 표현한 자료 구조)로 연결한다. 여러 번의 변환·묶음을 거친 제품의 전체 이력을 한 번의 질의(원하는 자료를 얻기 위한 조회 요청)로 조회하는 구조를 제안했다.[^p2]

다른 축은 **언어와 시각 정보를 함께 다루는 인공지능**이다. 비전-언어 모델(VLM, Vision-Language Model)은 영상과 글을 함께 받아 그 관계를 다루는 모델이고, 대형 언어 모델(LLM, Large Language Model)은 많은 글을 학습해 글을 이해하고 생성하는 모델이다. 연구실은 학습 자료 생성과 양자화(모델 안의 수를 정해진 표현값으로 바꾸는 방법)로 소형 언어 모델(SLM, Small Language Model)을 만들어 휴대전화·노트북 같은 기기에서 실행하는 연구를 소개한다. 학습 사례가 적은 범주의 인식과 메타학습(여러 과제의 학습 경험을 새 과제의 학습에 이용하는 방법)도 다룬다.[^ml] 대표 논문 Model-Dowser는 미세 조정(이미 학습한 모델을 특정 과제의 자료로 추가 학습하는 과정) 중 기존 능력을 잃는 현상을 줄이고, Vision Language Models are Biased와 B-score는 모델이 자료를 판단하거나 답할 때 보이는 편향을 측정한다.[^p3][^p4][^bscore]

**영상 복원과 생성**에서는 초해상도(해상도가 낮은 영상에서 해상도가 높은 영상을 복원하는 기술), 가상 착의(사람이 특정 옷을 입은 모습을 영상으로 합성하는 기술), 여러 센서의 자료를 함께 쓰는 인식을 연구한다.[^ml] VSRM은 동영상의 공간적 특징과 시간에 따른 변화를 함께 다뤄 복원하며, FIP-VITON은 옷의 형태를 사람에게 맞추는 단계와 착의 영상을 만드는 단계를 결합해 옷의 질감과 사람의 고유한 특징을 보존한다.[^p5][^p6] 센서 융합(여러 센서가 얻은 자료를 결합해 정보를 만드는 방법) 연구는 가시광선 영상과 적외선 영상을 함께 이용하는 선박·항공기 탐지를 대상으로 한다.[^ml]

**의료영상과 음성의 분석·생성 방법**도 연구한다. 의료영상에서는 분할(영상의 각 위치를 대상이나 영역별로 구분하는 작업)과 검출·분류를 다룬다.[^ml] 대표 논문은 영상을 분석해 얻은 특징을 위치별 예측으로 바꾸는 디코더(내부 표현을 목표 출력으로 바꾸는 계산 부분)를 새로 설계해, 생체 표지(몸의 상태나 생물학적 과정을 나타내는 측정 지표)의 영역을 구분하는 정확도를 높인다.[^p7] 음성 연구의 DailyTalk은 대화형 음성 합성(TTS, Text-to-Speech: 글을 음성으로 바꾸는 기술)을 위한 녹음 자료와 기준 모델을 제시한다. 앞선 대화의 정보를 음성 생성에 반영하는 문제를 다룬다.[^p8]

## 주요 연구 주제

### 1. 사물인터넷 플랫폼과 표준 기반 자료 공유

Oliot을 중심으로 사물 식별, 자료 수집·공유, 서비스 등록·탐색을 연결한다. GS1 표준을 따르는 플랫폼에 블록체인과 자료 처리 기술을 결합하고, 도시·선박·버스의 서비스로 연결한다. 대표 논문은 서로 다른 표준의 자료를 연결하는 게이트웨이와, 제품 이력을 연결·조회하는 지식 그래프 구조를 다룬다.[^iot][^labview][^p1][^p2]

### 2. 언어·시각 모델의 편향, 학습 유지와 기기 내 실행

Model-Dowser의 기존 능력 보존, VLM의 시각적 편향 측정, 응답 이력을 이용한 B-score가 대표 사례다. 학습 자료 생성과 양자화를 이용해 기기에서 실행할 언어 모델을 만드는 연구도 진행한다.[^p3][^p4][^bscore][^ml]

### 3. 영상의 화질 복원, 가상 착의와 센서 융합

이미지·동영상 초해상도, 옷과 사람의 특징을 보존하는 착의 영상 생성, 가시광선·적외선 자료를 함께 쓰는 인식을 다룬다. 대표 논문은 동영상 복원의 VSRM과 가상 착의의 FIP-VITON이다.[^ml][^p5][^p6]

### 4. 의료영상의 영역 분리와 대화형 음성 생성

서로 다른 규모의 영상 특징을 결합하는 의료영상 디코더와, 대화의 흐름을 반영하는 음성 합성용 자료·모델을 연구한다.[^p7][^p8]

## 대표 논문

2021–2026년 목록 가운데 김대영 교수가 저자인 논문 8편을 골랐다. 사물인터넷의 표준·제품 이력 공유, 모델의 편향과 학습 유지, 영상 복원·생성, 의료영상 분석, 음성 생성을 담았다. "쉽게 말하면" 칸은 논문별로 각주에 밝힌 OpenAlex 등록 초록 2편과 arXiv 판 초록 6편만을 근거로 썼다. 연도는 연구실의 학술지·학회 표기이며, 링크는 등록 DOI 또는 설명에 쓴 arXiv 판을 가리킨다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2021 | [Towards Interoperability of Entity-Based and Event-Based IoT Platforms: The Case of NGSI and EPCIS Standards](https://doi.org/10.1109/ACCESS.2021.3069194) · IEEE Access | 사물인터넷 자료가 여러 기관과 시스템에 나뉘어 있으면 서로 다른 표준 때문에 함께 쓰기 어렵다. 사건을 중심으로 자료를 표현하는 EPCIS와 개체를 중심으로 표현하는 NGSI를 연결하는 OLIOT Mediation Gateway를 제안했다. 육류 공급망의 정보 시스템을 통합하는 실제 사례에 적용해 이 연결 방식의 적용 가능성과 실현 가능성을 보였다.[^p1] | Yalew Tolcha 외, Daeyoung Kim(마지막 저자) |
| 2 | 2025 | [Building Digital Product Passports: EPCIS 2.0 Meets Knowledge Graphs](https://doi.org/10.1109/RFID64926.2025.11015538) · IEEE RFID 2025 | 제품의 소유자가 바뀌거나 여러 제품이 합쳐지고 나뉘면 전체 이력을 조회하기 복잡해진다. EPCIS 2.0과 지식 그래프를 결합하고 GS1 식별키로 사건들을 연결하는 구조를 제안했다. 공급망의 여러 단계에서 일어난 변환과 묶음 관계를 그래프로 표현해, 제품의 전체 이력을 한 번의 질의로 조회한다. 여러 출처의 사건 정보를 실시간으로 받아 처리하도록 설계했다.[^p2] | Yalew Kidane Tolcha, Gunwoo Park, Daeyoung Kim(마지막 저자) |
| 3 | 2026 | [Model-Dowser: Data-Free Importance Probing to Mitigate Catastrophic Forgetting in Multimodal Large Language Models](https://arxiv.org/abs/2602.04509) · ICML 2026 (채택) | 영상과 글을 함께 다루는 모델을 새 과제로 추가 학습하면 기존 과제의 능력이 떨어질 수 있다. 모델의 가중치(학습으로 정해지는 계산 계수), 입력에 대한 반응과 출력의 민감도를 함께 고려해 각 계수의 중요도를 잰다. 중요한 계수는 보존하고 나머지를 갱신해 기존 능력의 손실을 줄이는 Model-Dowser를 제안했다. LLaVA와 NVILA 모델에서 기존 능력의 손실을 줄이면서 자원 사용과 모델 규모 확장도 고려한 결과를 보였다.[^p3] | Hyeontaek Hwang, Nguyen Dinh Son, Daeyoung Kim(마지막 저자) |
| 4 | 2026 | [Vision Language Models are Biased](https://arxiv.org/abs/2505.23941) · ICLR 2026 | 모델이 널리 알려진 사물에 관한 지식 때문에 실제 그림을 잘못 읽는지 시험했다. 동물·로고·게임판 등 7개 영역의 개수 세기와 식별에서 편향을 발견했고 개수 세기 평균 정확도는 17.05%였다. 영상 배경을 제거하면 정확도가 21.09%포인트 높아졌다. 모델이 이미지를 판단할 때의 편향을 검사하는 자동화 틀을 제시했다.[^p4] | An Vo 외, Daeyoung Kim(마지막 저자) |
| 5 | 2025 | [VSRM: A Robust Mamba-Based Framework for Video Super-Resolution](https://arxiv.org/abs/2506.22762) · ICCV 2025 | 동영상의 화질을 복원할 때 여러 장면에 걸친 관계를 반영하기 위해 Mamba라는 계산 모델을 이용했다. 공간에서 시간으로, 시간에서 공간으로 특징을 전달하는 두 부분과 인접 장면을 맞추는 부분을 설계했다. 복원 영상과 정답 영상 사이의 주파수 성분(영상 변화의 반복 정도에 따라 나눈 성분) 차이도 학습에 반영해 세부 무늬를 보존했다. 여러 평가 자료에서 성능을 시험했다.[^p5] | Dinh Phu Tran, Dao Duy Hung, Daeyoung Kim(마지막 저자) |
| 6 | 2024 | [Time-Efficient and Identity-Consistent Virtual Try-On Using A Variant of Altered Diffusion Models](https://arxiv.org/abs/2403.07371) · ECCV 2024 (채택) | 가상 착의에서는 옷의 질감뿐 아니라 문신·장신구 같은 사람의 특징을 보존해야 한다. FIP-VITON은 옷을 사람의 형태에 맞추는 부분과, 옷을 다듬고 빠진 부분을 생성하는 부분을 결합했다. 사람의 고유한 특징을 보존하는 후처리도 더했다. 초록은 당시 비교 방법보다 추론(학습한 모델이 결과를 계산하는 과정)이 거의 20배 빨랐고, 두 평가 자료에서 최근 비교 방법과 견줄 만한 정량 결과를 얻었다고 보고한다.[^p6] | Phuong Dam, Jihoon Jeong, Anh Tran, Daeyoung Kim(마지막 저자) |
| 7 | 2025 | [Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention](https://arxiv.org/abs/2506.18335) · CVPR 2025 | 의료영상은 염색이나 모양의 차이 때문에 대상 영역을 나누기 어렵다. 영상을 분석한 특징을 디코더로 옮기는 과정에 주목해, 서로 다른 규모의 특징을 통합하고 중요한 영역을 강조하며 위치 정보를 복원하는 구조를 제안했다. 여러 영상 분석 모델과 결합할 수 있도록 설계했고, 네 평가 자료와 각 구성 요소의 역할을 살피는 실험으로 분할 성능의 개선을 확인했다.[^p7] | Saad Wazir, Daeyoung Kim(마지막 저자) |
| 8 | 2023 | [DailyTalk: Spoken Dialogue Dataset for Conversational Text-to-Speech](https://arxiv.org/abs/2207.01063) · ICASSP 2023 | 개별 문장 중심의 기존 음성 자료를 보완하려고, 앞뒤 맥락이 있는 대화를 음성으로 녹음한 DailyTalk을 만들었다. 공개 대화 자료에서 2,541개 대화를 골라 수정·녹음하고, 앞선 대화 정보를 조건으로 쓰는 음성 합성 기준 모델도 제시했다. 실험에서는 일반 음성 합성 자료로 쓸 수 있고 대화 맥락도 표현할 수 있음을 보였다. 자료와 기준 코드에 학술 사용을 위한 공개 이용 조건을 명시했다.[^p8] | Keon Lee, Kyumin Park, Daeyoung Kim(마지막 저자) |

## 교수와 전문 분야

김대영 교수의 학위는 University of Florida의 박사(2001)다. 전산학부는 전공을 사물인터넷·데이터공학·딥러닝으로 적고, Oliot의 개발을 주도하며 GS1과 국제 연구 파트너들과 공동 연구를 진행한다고 소개한다.[^prof] 연구실 교수 소개는 1992–1997년 한국전자통신연구원 연구원, 2001–2002년 Arizona State University의 Assistant Professor of Research, 2002–2014년 KAIST의 Assistant/Associate Professor, 2014년 3월 이후 전산학부 Professor 경력을 적는다. AutoID Labs at KAIST와 Data Engineering & Analytics Lab, Global USN National Research Laboratory의 운영 역할도 적는다.[^director]

전문 분야의 한 축은 **사물을 식별하고 자료를 연결하는 표준 기반 플랫폼**이다. 학과 교수 소개는 자료의 수집·가공·공유·분석을 아우르는 Oliot 프로젝트를 설명하고, 연구실 IoT 페이지는 서비스의 등록·탐색과 블록체인을 결합한 공유를 소개한다. 사물인터넷 표준 간 연결과 지식 그래프를 이용한 제품 이력 조회도 대표 논문으로 다룬다.[^prof][^iot][^p1][^p2] 다른 축은 **학습한 인공지능의 능력을 유지하고, 편향을 평가하며, 영상·글·음성의 관계를 다루는 방법**이다. 최근 논문에는 모델의 기존 능력 보존과 시각적 편향, 동영상 복원과 가상 착의, 의료영상 디코더 설계가 함께 나타난다.[^p3][^p4][^bscore][^p5][^p6][^p7] 대화형 음성 생성 자료의 설계도 연구 범위에 들어간다.[^p8]

## 응용 분야

Oliot의 적용 대상으로 스마트시티·선박·버스를 들며, 학과 연구실 소개는 유통과 자동차 분야도 설명한다.[^iot][^labview] 현재 과제 페이지는 항공기 인공지능 기술, 재활용 로봇용 인공지능, 이동형 도시 실험실을 소개한다.[^projects] 기계학습 연구는 기기 안에서 동작하는 언어 모델, 전자상거래의 가상 착의, 영상의 화질 복원과 의료영상 분석으로 이어진다.[^ml][^p6][^p7] 대화형 음성 합성은 대화 이력을 반영하는 음성 생성 기술의 자료·기준 모델을 제공한다.[^p8]

## 구성원

2026년 10월 27일 연구실 게시 기준으로 연구원 쪽 3명, 박사과정 쪽 13명, 석사과정 쪽 10명이다. 과정·연구 주제·시작 시기는 각 페이지 표기이며, 시작은 과정별 진학일로 다시 해석하지 않은 Entrance Date다. 연구원 Yalew Kidane의 시작은 게시된 Senior Researcher 경력 시작이다.[^fellows][^phd][^master] "대표 논문 참여"는 전체 저자 명단의 이름과 구성원 이름이 일치하는 경우의 표 번호다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Yalew Kidane | 연구원 (Senior Researcher; Associate Director at AutoID Labs KAIST) | August 2023 | Internet of Things; Blockchain for IoT; Generative AI | yalewkidane@kaist.ac.kr |  |
| Jaesung Lee | 연구원 | Sep. 2024 | Computer Vision; 3D Generation | ljs6017@kaist.ac.kr |  |
| Gabriel Davin | 연구원 | Sep. 2024 | Computer Vision; Self-supervised Learning | gabrieldavin23@kaist.ac.kr |  |
| Hyunhak Kim | 박사과정 (Part time) | Mar, 2016 | WSN, Embedded Systems, IoT; Edge Computing, Deep Learning | overflow@kaist.ac.kr |  |
| Junyong Park | 박사과정 (Part time) | Mar, 2020 | Artificial Neural Networks; Edge Computing |  |  |
| Jeongseok Kim | 박사과정 (Part time) | Sep, 2022 | Deep Learning for Computer Vision; Embedded System | jskim88@kaist.ac.kr |  |
| Dohyeun Kim | 박사과정 (Part time) | Sep, 2022 | Reinforcement Learning; Health Care | stalker7@kaist.ac.kr |  |
| Hyeontaek Hwang | 박사과정 | Mar, 2023 | Meta-Learning; Computer Vision |  | 3 |
| Saad Wazir | 박사과정 | Mar, 2023 | Computer Vision; Medical Image Analysis | saad.wazir@kaist.ac.kr | 7 |
| Duy Thao Do | 박사과정 | Sept, 2023 | Graph Neural Networks; Document Analysis | thaodo@kaist.ac.kr |  |
| Nguyen Dinh Son | 박사과정 | Sep. 2022 | Computer Vision; Natural Language Processing | nguyendinhson@kaist.ac.kr | 3 |
| Seonkwon Kim | 박사과정 | Sep. 2024 | ML for CPS; XAI for CPS | lukaskim@kaist.ac.kr |  |
| Hoang Phuong Dam | 박사과정 | Mar. 2023 | Virtual Try-on; Deep Learning | hoangphuong1211@kaist.ac.kr |  |
| Tran Dinh Phu | 박사과정 | Mar. 2023 | Image/Video Restoration; Multi-modal Models Understanding and Reasoning | phutx2000@kaist.ac.kr | 5 |
| Seungmin Yang | 박사과정 | Mar. 2024 | Deep Learning; Explainable AI | smyang88@kaist.ac.kr |  |
| Sehwan Hong | 박사과정 | Sep. 2026 | Computer Vision; Multi-Modal Large Language Model | samhong657@kaist.ac.kr |  |
| Nguyen Duc Quyen | 석사과정 | Mar. 2025 | Generative Models; Virtual Try-on | nguyenducquyen2311@kaist.ac.kr |  |
| Dang Thi Tuong Vy | 석사과정 | Mar. 2025 | LLMs / VLMs; Human-Computer Interaction(HCI) | vydang@kaist.ac.kr |  |
| Seongah Kim | 석사과정 | Jan. 2025 | Computer Vision; Natural Language Processing | kimsa0322@kaist.ac.kr |  |
| Son Hoang | 석사과정 | Mar. 2025 | Virtual Try On; Deep learning | sonhm2910@kaist.ac.kr |  |
| Do Minh Duc | 석사과정 | Mar. 2025 | Computer Vision; Generative AI | ducdm200158@kaist.ac.kr |  |
| Tran Tuan Phong | 석사과정 | Sep. 2025 | Speech Processing; Multimodal AI | phongtt263@kaist.ac.kr |  |
| Hyojin Choi | 석사과정 | Sep. 2025 | Computer Vision; Multimodal NLP | hyojinchoi@kaist.ac.kr |  |
| Jaesuk Lim | 석사과정 | Mar. 2026 | LLMs / VLMs; Agentic AI | flight0454@kaist.ac.kr |  |
| Tran Van Cuong | 석사과정 | Mar. 2026 | Computer Vision; Multimodal AI | tranvancuong@kaist.ac.kr |  |
| Minjun Choe | 석사과정 | Sep. 2026 | Reinforcement Learning; Deep Learning | choemj@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 페이지의 KAIST 석사·박사 학위 연도가 2021–2026년인 16행이다. 같은 이름 Kyumin Park의 두 카드는 연구 주제와 게시 이메일이 달라 두 행을 유지했다. 학위 연도는 학력 칸 표기이고, 진로는 이름 옆에 게시된 기관이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jihoon Jeong | M.S. (2025) |  |
| Patrick Vibild | M.S. (2024) |  |
| Sungpil Woo | Ph.D. (2025) | ETRI |
| Sofia Maria Palomino Chamizo | M.S. (2025) |  |
| Hung Dao Duy | M.S. (2025) |  |
| Jon Hernandez | M.S. (2024) |  |
| Mikel Lainsa | M.S. (2024) |  |
| Sangkyu Kim | Ph.D. (2023) |  |
| Kyumin Park | M.S. (2023) |  |
| Kyumin Park | M.S. (2023) |  |
| Jaryong Lee | M.S. (2023) | Humelo |
| Keon Lee | M.S. (2022) | Krafton |
| Mingu Kang | M.S. (2021) | Lunit |
| Trung Tran | M.S. (2021) |  |
| Thao Do | M.S. (2021) | Ftech |
| HyungRok Ham | M.S. (2021) | TMax |

## 최근 논문 목록 (2021–2026)

생체 신호에서 감정을 인식하고 심전도(심장의 전기적 활동을 기록한 신호)를 분류하는 학습 방법, 치료 선택을 학습하는 방법과 원격 건강 감시 시스템도 다룬다.[^bio1][^bio2][^bio3][^bio5][^bio6]

모델의 학습·평가, 영상·음성 처리, 사물인터넷의 표준과 자료 공유를 다룬다. 연구실 Publication 페이지의 국제 학술지·국제 학회 및 워크숍·국내 학회 구역에서 58편을 담았다. 연도는 원문의 연도 구역이며, 2022–2023년 묶음은 본문에 2022년이 명시된 항목을 제외하고 2023년 아래에 모았다. 그 묶음의 날짜 없는 학술지 게재 승인 항목도 같은 곳에 두었다. 같은 심전도 분류 논문이 두 연도 구역에 있으면 2024년 출판 행 하나로 표시했다. 2021년 구역은 연도 전체를 포함한다. 제목·저자·발표처는 연구실 표기이고, 학술지의 Accepted는 게재 승인, 학회의 Accepted는 채택으로 표시했다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. arXiv의 채택 표기만 확인한 항목도 채택으로 적었다.[^pubs][^vton-news][^p3][^bscore][^medcagd][^bio5]

**2026**

- Gabriel Manalu, Khanh An Vo, Duc Do Minh, Quang Tau, DINH SON NGUYEN, Minh Son Hoang, Hyeontaek Hwang, Jaesung Lee, Hyojin Choi, Tuan Phong Tran, Daeyoung Kim. "RADBench: Evaluating Foundation VLMs for Corner Case Description on A Comprehensive Dataset". *IEEE Intelligent Vehicles Symposium (IV 2026), Detroit, MI, United States, June 22 – 25, 2026*.
- An Vo, Khai-Nguyen Nguyen, Mohammad Reza Taesiri, Vy Tuong Dang, Anh Totti Nguyen, Daeyoung Kim. "Vision Language Models are Biased". *The Fourteenth International Conference on Learning Representations (ICLR 2026), Rio de Janeiro, Brazil, April 23-27, 2026*.
- Tran Dinh Phu, Thao Do, Saad Wazir, Seongah Kim, Seon Kwon Kim, and Daeyoung Kim. "SAT: Selective Aggregation Transformer for Image Super-Resolution". *In Findings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026), Denver Convention Center, Denver, Colorado, USA, June 5–7, 2026*.
- Hyeontaek Hwang\* and Nguyen Dinh Sonn\* (equal contribution), and D. Kim. "Model-Dowser: Data-Free Importance Probing to Mitigate Catastrophic Forgetting in Multimodal Large Language Models". *in Proc. 43rd Int'l Conf. on Machine Learning (ICML 2026), Seoul, South Korea, July 6-11, 2026 (채택)*.
- Duc Dm, Thao Do, Minh Son Hoang, Anh Le Duc Tran, Daeyoung Kim, and Huy Nguyen. "FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction". *in Proc. 43rd Int'l Conf. on Machine Learning (ICML 2026), Seoul, South Korea, July 6-11, 2026*.
- Hyeontaek Hwang, Cheonghwan Hur, and Daeyoung Kim. "Node-Level Gating for Long-Tailed Recognition under Neural Collapse Geometry". *13th Workshop on Fine-Grained Visual Categorization (FGVC) at CVPR 2026, Denver, CO, USA, June 3-7, 2026*.
- Thao Do, Dinh Phu Tran, An Vo, Seon Kwon Kim, Daeyoung Kim. "Efficient Encoder-Only Context Compression via Marginal Contribution Scoring". *Int'l Conf. on Machine Learning ICML 2026 Workshop (AdaptFM), Seoul, South Korea, July 6-11, 2026*.
- Saad Wazir, Patrick Vibild, Dinh Phu Tran, Seongah Kim, Daeyoung Kim. "MedCAGD: Context-Aware Gated Decoder for Robust Medical Image Segmentation". *The 19th European Conference on Computer Vision (ECCV 2026), in Malmö, Sweden, September 8 – 12th, 2026 (채택)*.
- Minh Son Hoang\*, Dinh Phu Tran\* (equal contribution), Quyen Nguyen Duc, Dam Hoang Phuong, Daeyoung Kim. "FreqOrtho-SR: Frequency-Guided Orthogonal Expert Learning for Real-World Image Super-Resolution". *The 19th European Conference on Computer Vision (ECCV 2026), in Malmö, Sweden, September 8 – 12th, 2026*.
- Junyong Park, Yong-Ju Lee, Daeyoung Kim. "CoVLA: Vision-Language Alignment with Fewer Vision Tokens". *The Third Conference on Language Modeling (COLM 2026), San Francisco, USA, October 6-9, 2026*.
- Gabriel Manalu, Minh Son Hoang, Hyeontaek Hwang, Jaesung Lee, Hyojin Choi, Tran Tuan Phong, Seon Kwon Kim, Saad Wazir, Daeyoung Kim. "Evaluating Video LLMs’ Understanding of Corner Cases in Autonomous Driving". *The 37th British Machine Vision Conference (BMVC 2026), Lancaster, UK, November 23-26, 2026*.
- An Vo\*, Vy Tuong Dang\* (equal contribution), Khai-Nguyen Nguyen, Emilio Villa-Cueva, Thamar Solorio, Anh Totti Nguyen, Daeyoung Kim. "Deep and shallow biases in language models". *The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026), Budapest, Hungary, October 24 –29, 2026*.
- Thao Do, Dinh Phu Tran, An Vo, Seon Kwon Kim, Daeyoung Kim. "EnComp: Lightweight Encoder-Only Context Compression for Retrieval-Augmented Question Answering". *The 5th Asia-Pacific Chapter of the Association for Computational Linguistics (AACL 2026), Hengqin, China, November 6 – 10, 2026 (Oral)*.
- Vy Tuong Dang, An Vo, Emilio Villa-Cueva, Quang Tau, Duc Dm, Thamar Solorio, Daeyoung Kim. "VMMU: A Vietnamese Multitask Multimodal Understanding and Reasoning Benchmark". *Findings of The 5th Asia-Pacific Chapter of the Association for Computational Linguistics (AACL 2026), Hengqin, China, November 6 – 10, 2026*.
- Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim. "ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting". *The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS 2026), Sydney, Australia, December 6-12, 2026 (Spotlight)*.
- Dohyeun Kim, Hwin Dol Park, Jae-Hun Choi, Tae Joon Jun, Jin Won Huh, Yun Jung Jung, Jee Hwan Ahn, and Daeyoung Kim. "DDRL:Dyna-Based Discriminative Reinforcement Learning for Optimizing Sepsis Treatment Pathways in Offline Environments". *IEEE Journal of Biomedical and Health Informatics (J-BHI), 2026*.
- Jeongseok Kim, Byeongju Woo, Hoseong Kim, Byeonghyun Pak, and Daeyoung Kim. "VVSQ: Vision Vulnerability Score-Guided Post-Training Quantization for Vision-Language Models". *Neurocomputing, 2026*.
- Wilson Engelmann, Yalew Kidane Tolcha, Daeyoung Kim, Rodrigo da Rosa Righi, and Fausto Neri da Silva Vanin. "Infrastructural Regulation in the Fourth Industrial Revolution: GS1 Standards and Blockchain as Mechanisms of Technical Self-Regulation". *Revista de Estudos Constitucionais, Hermenêutica e Teoria do Direito (Journal of Constitutional Studies, Hermeneutics and Theory of Law), 2026*.

**2025**

- Thao Do, Dinh Phu Tran, An Vo, and Daeyoung Kim. "Reference-Based Post-OCR Processing with LLM for Precise Diacritic Text in Historical Document Recognition". *The 39th Annual AAAI Conference on Artificial Intelligence (AAAI 2025), Philadelphia, USA, Feb. 25 – Mar 4, 2025*.
- Saad Wazir, Daeyoung Kim. "Rethinking Decoder Design: Improving Biomarker Segmentation Using Depth-to-Space Restoration and Residual Linear Attention". *The IEEE/CVF Conference on Computer Vision and Pattern Recognition 2025 (CVPR 2025), Nashville TN, USA, 11th - 15th June 2025*.
- Yalew Kidane, Gunwoo Park, Daeyoung Kim. "Building Digital Product Passports: EPCIS 2.0 Meets Knowledge Graphs". *IEEE RFID 2025 ATLANTA, GEORGIA · APRIL 22-24, 2025*.
- An Vo, Mohammad Reza Taesiri, Anh Totti Nguyen, Daeyoung Kim. "B-score: Detecting biases in large language models using response history". *Forty-Second International Conference on Machine Learning (ICML 2025), Vancouver Convention Center , July 13th - July 19th, 2025 (채택)*.
- Yalew Kidane Tocha, Fausto Neri da Silva Vanin, Gunwoo Park, Cristiano André da Costa, Rodrigo da Rosa Righi, Daeyoung Kim. "Hybrid EPCIS: Integrating GS1/ISO Standards with On-Chain and Off-Chain Distributed Ledger for Supply Chain Traceability". *The 7th IEEE International Conference on Decentralized Applications and Infrastructures(IEEE DAPPS 2025), July 21st to 24th, 2025, Tucson, Arizona, USA*.
- Dinh Phu Tran, Duy Hung Dao, Daeyoung Kim. "VSRM: A Robust Mamba-Based Framework for Video Super-Resolution". *International Conference on Computer Vision, ICCV 2025 Oct 19 – 23th, 2025, Honolulu, USA*.
- Gunwoo Park, Yalew K Tolcha, Youngjong Yi, Manki Jung and Daeyoung Kim. "From Tag to Digital Twin: Unlocking Service Resolution through GS1 Digital Link". *2025 IEEE International Conference on RFID Technology and Applications (RFID-TA) - IEEE RFID-TA 2025, Valence, France, 27-30, October, 2025*.
- Yalew K Tolcha, Gunwoo Park and Daeyoung Kim. "LLM-Powered Digital Link Agent". *2025 IEEE International Conference on RFID Technology and Applications (RFID-TA) - IEEE RFID-TA 2025, Valence, France, 27-30, October, 2025*.
- Saad Wazir, Rao Faizan, and Daeyoung Kim. "HistoSeg++: Delving deeper with attention and multiscale feature fusion for biomarker segmentation". *ICBBE 2025 November 27 - 30th, 2025, Tokyo, Japan*.
- Sofia M Palomino Chamizo, Daeyoung Kim. "Optimizing Object Detection with Multispectral RGB/IR Fusion". *2025 16th International Conference on Information and Communication Technology Convergence (ICTC), JEJU, Korea*.
- Jon Hernandez Aranda, Patrick Vibild, Daeyoung Kim. "Distance-Aware Single-Stage Detectors: Combining Detection with Object-Specific Distance Estimation". *2025 16th International Conference on Information and Communication Technology Convergence (ICTC), JEJU, Korea*.
- Jeongseok Kim, Jemin Lee, Yongin Kwon, Daeyoung Kim. "QuantuneV2: Local Metric-Driven Mixed Precision Quantization from a Compiler Perspective for Practical Embedded AI Applications". *Future Generation Computer Systems, Volume 166, 107718, May 2025*.
- Sungpil Woo\*, Muhammad Zubair\*, Sunhwan Lim, and Daeyoung Kim. "Deep Multimodal Emotion Recognition using Modality-Aware Attention and Proxy-based Multimodal Loss". *Internet of Things, Elsevier*.
- Muhammad Zubair\*, Sungpil Woo\*, Sunhwan Lim, and Daeyoung Kim. "Deep Representation Learning with Assisted Domain Adaptation for EEG-based Cross-Subject Emotion Recognition". *IEEE Transactions on Computational Social Systems*.
- Jeongseok Kim, Daeyeon Kim, Eunjin Koh, Daeyoung Kim. "IntegraScale: A Unified Integral Framework for PSF-Aware Quantized Subpixel Image Scaling". *IEEE Access*.
- Minjun Choe, Saeyeon Oh, Sanghoon Lee, Jihoon Jeong, Hyeontaek Hwang, Daeyoung Kim. "Real-Time Building Detection and Address Retrieval Using a Single RGB Camera". *2025 한국컴퓨터종합학술대회 (KCC2025), 제주국제컨벤션센터(ICC 제주) , 1-4, July, 2025*.
- Gunwoo Park, Tolcha Yalew Kidane, Youngjong Yi, Daeyoung Kim. "Design and Implementation of weapon system MRO technologies based on international standards and blockchain". *2025 한국컴퓨터종합학술대회 (KCC2025), 제주국제컨벤션센터(ICC 제주) , 1-4, July, 2025*.
- Seungmin Yang, Hyeontaek Hwang, Vibild Patrick Dominique, Daeyoung Kim. "AI Accelerator Implementation Technology for On-Device Deployment in Defense AI". *2025 한국컴퓨터종합학술대회 (KCC2025), 제주국제컨벤션센터(ICC 제주) , 1-4, July, 2025*.

**2024**

- Phuong Dam, Jihoon Jeong, Anh Tran, and Daeyoung Kim. "Time-Efficient and Identity-Consistent Virtual Try-On Using A Variant of Altered Diffusion Models". *The 18th European Conference on Computer Vision (ECCV 2024), Milano, Italy, Sep 29th - Oct 4th, 2024 (채택)*.
- Dinh Phu Tran, Dao Duy Hung, and Daeyoung Kim. "Channel-Partitioned Windowed Attention And Frequency Learning for Single Image Super-Resolution". *The 35th British Machine Vision Conference (BMVC 2024), Glasgow, UK, 25th - 28th Nov 2024*.
- Yalew Tolcha, Fausto Vanin, Rodrigo da Rosa Righi, Cristiano André da Costa, and Daeyoung Kim. "Enhancing Supply Chain Security and Interoperability with GS1 ISO EPCIS/CBV Open Standards using Decentralized Ledgers". *IEEE Global Blockchain Conference (GBC 2024), Shanghai, China, 21-23 Aug, 2024*.
- Fausto Vanin, Yalew Tolcha, Rodrigo da Rosa Righi, Cristiano André da Costa, and Daeyoung Kim. "Decentralized Ledger Technology for EPCIS 2.0: Utilizing NFTs for Enhanced Product Traceability". *The 7th IEEE International Conference on Blockchain (Blockchain 2024), Copenhagen, Denmark, 19-22 Aug, 2024*.
- Patrick Vibild, Jon Hernandez, and Daeyoung Kim. "Sailing Through Data: Automated Data Acquisition Systems for Machine Learning Applications in Maritime Navigation". *14th International Conference on the Internet of Things (IoT 2024), Oulu, Finland, 20-22 Nov, 2024*.
- Saad Wazir and Daeyoung Kim. "Rethinking the Nested U-Net Approach: Enhancing Biomarker Segmentation with Attention Mechanisms and Multiscale Feature Fusion". *The 5th International Conference on Medical Imaging and Computer-Aided Diagnosis (MICAD 2024), Nov. 19-21, 2024, Manchester, UK*.
- Sungpil Woo, Muhammad Zubair, Sunhwan Lim, and Daeyoung Kim. "Empirical Study of Attention Mechanism on Neural Ordinary Differential Equations". *The 15th International Conference on ICT Convergence, 16-18 October 2024, Jeju Island, Korea*.
- Sungpil Woo, Sunhwan Lim, and Daeyoung Kim. "Empirical Study of Rectifier and Dropout in Feedforward Neural Networks". *The 15th International Conference on ICT Convergence, 16-18 October 2024, Jeju Island, Korea*.
- Muhammad Zubair\*, Sungpil Woo\*, Sunhwan Lim, and Daeyoung Kim. "Deep Representation Learning with Sample Generation and Augmented Attention Module for Imbalanced ECG Classification". *IEEE Journal of Biomedical and Health infomatics, Volume: 28, Issue: 5, pp. 2461-2472 , May 2024*.
- Mikel Lainsa and Daeyoung Kim. "Zero-Shot Texture Analysis and Regression-Based Deformation Recognition for Rail Anomaly Detection". *IEEE Access, 2024*.

**2023**

- Sangkyu Kim, Hae-yong Yang, and Daeyoung Kim. "Fully Complex Deep Learning Classifiers for Signal Modulation Recognition in Non-Cooperative Environment". *IEEE Access (게재 승인)*.
- Yalew Tolcha, Kyounghoon Kim, and Daeyoung Kim. "ImprovedSSGAN: Ranking Discriminator With Semi-Supervised GAN for Ordinal Information". *IEEE Access, 2023 (게재 승인)*.
- V. F. Rodrigues, R. R. Righi, C. A. Costa, F. A Zeiser, B. Eskofier, A. Maier,& D. Kim. "Digital health in smart cities: Rethinking the remote health monitoring architecture on combining edge, fog, and cloud". *Spring Nature, April. 6, 2023 (게재 승인)*.
- Keon Lee, Kyumin Park, and Daeyoung Kim. "Dailytalk: Spoken Dialogue Dataset for Conversational Text-to-Speech". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), June. 4-10, 2023 (채택)*.

**2022**

- Sungpil Woo\*, Muhammad Zubair\* (co-first author), Sunhwan Lim, Chan-Won Park, and Daeyoung Kim. "Conditional GAN based Collaborative Filtering with Data Augmentation for Cold-Start User". *The 14th International Conference on ICT Convergence (ICTC 2022), in Jeju, Korea, October 19-21, 2022*.

**2021**

- Y. Tolcha, A. Kassahun, T. Montanaro, D. Conzon, G. Schwering, J. Maselyne, D. Kim. "Towards Interoperability of Entity-Based and Event-Based IoT Platforms: The Case of NGSI and EPCIS Standards". *in IEEE Access, vol. 9, pp. 49868-49880, 2021, doi: 10.1109/ACCESS.2021.3069194*.
- Nguyen G., Chen S., Jun T.J., Kim D. (2021) Explaining How Deep Neural Networks Forget by Deep Visualization. In: Del Bimbo A. et al. (eds) Pattern Recognition. ICPR International Workshops and Challenges. ICPR 2021. Lecture Notes in Computer Science, vol 12663. Springer, Cham. https://doi.org/10.1007/978-3-030-68796-0_12
- Mingu Kang, Trung Quang Tran, Seungju Cho and Daeyoung Kim. "CAP-GAN: Towards Adversarial Robustness with Cycle-consistent Attentional Purification". *International Joint Conference on Neural Networks (IJCNN), July. 18-22, 2021*.
- Trung Tran Quang, Mingu Kang, Daeyoung Kim. "ReRankMatch: Semi-Supervised Learning with Semantics-Oriented Similarity Representation". *International Joint Conference on Neural Networks (IJCNN), July. 18-22, 2021*.
- Thao Do, Daeyoung Kim. "QuickBrowser: A Unified Model to Detect and Read Simple Object in Real-time". *International Joint Conference on Neural Networks (IJCNN), July. 18-22, 2021*.
- Keon Lee, Kyumin Park, Daeyoung Kim. "STYLER: Style Factor Modeling with Rapidity and Robustness via Speech Decomposition for Expressive and Controllable Neural Text to Speech". *Interspeech 2021*.
- Giang Nguyen, Daeyoung Kim, Anh Nguyen. "The effectiveness of feature attribution methods and its correlation with automatic evaluation scores". *Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS 2021 (NIPS 2021)), Dec. 6-14, 2021*.

## 과제

현재 과제 페이지에 게시된 3건이다. 시작·종료 연도와 지원기관은 게시 표기이며, 종료가 적히지 않은 기간은 그대로 두었다.[^projects]

- AiFly: Artificial Intelligence Technologies for Aircraft (지원 KAI; 기간 2023~)
- AiRobot: Artificial Intelligence Technologies for Recycling Robot (지원 ROBOne; 기간 2023 ~)
- Ailee 2024: Mobile City Laboratory "IoT, AI, Data, GS1 Standards" (지원 MSIT; 기간 2022 ~ 2025)

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291, KAIST N1 924호[^intro]
- 연구실 전화: +82-42-350-7851[^intro]
- 교수연구실: N1 902호, 교수 전화 042-350-3551[^labview][^director]
- 교수 이메일: kimd@kaist.ac.kr[^intro]

## 각주
[^intro]: 연구실 소개와 연락. <https://www.ai2lab.kaist.ac.kr/introduction> 2026-10-27 열람. 2002년 2월 설립, 2017년 DEAL 명칭 사용 이력과 연구실 주소·이메일을 게시한다.
[^labview]: 전산학부 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=72&menu=64> 2026-10-27 열람. AI² 연구실, 김대영, N1 902호. Oliot의 식별·자료 모델·공유·서비스 탐색과 유통·자동차·도시·선박 연구를 소개한다.
[^prof]: 전산학부 김대영 교수 소개. <https://cs.kaist.ac.kr/people/view?idx=373&kind=faculty&menu=160> 2026-10-27 열람. 교수, 사물인터넷·데이터공학·딥러닝, PhD University of Florida 2001. Oliot 개발과 GS1 국제 공동 연구를 소개한다.
[^director]: 연구실 교수 소개. <https://www.ai2lab.kaist.ac.kr/members/director> 2026-10-27 열람. KAIST 2002년 2월 이후 경력과 2014년 3월 이후 Professor 경력, 연구 관심과 운영 역할을 게시한다.
[^ml]: 현재 기계학습 연구. <https://www.ai2lab.kaist.ac.kr/research-area/machine-learning> 2026-10-27 열람. 메타학습과 학습 자료의 범주 불균형, 비전-언어 모델, 기기 내 소형 언어 모델 개발을 소개한다. 학습 자료 생성·양자화를 이용하며 이미지·동영상 초해상도, 가상 착의, 가시광선·적외선 센서 융합과 의료영상 처리를 연구한다.
[^iot]: 현재 사물인터넷 연구. <https://www.ai2lab.kaist.ac.kr/research-area/iot> 2026-10-27 열람. Oliot의 GS1 기반 식별·자료 수집·공유·서비스 등록·탐색을 설명한다. 블록체인과 자료 처리 기술을 결합한 자료·서비스 공유, 스마트시티·스마트십·스마트버스 적용을 소개한다.
[^fellows]: Research Fellows. <https://www.ai2lab.kaist.ac.kr/members/research-prof-postdoc> 2026-10-27 열람. Yalew Kidane, Jaesung Lee, Gabriel Davin 3명을 게시한다. Yalew Kidane의 Senior Researcher와 Associate Director 경력 시작은 August 2023이다.
[^phd]: Ph.D students. <https://www.ai2lab.kaist.ac.kr/members/ph-d-student> 2026-10-27 열람. 13명의 이름·연구 주제·학력·Entrance Date를 게시한다. Hyunhak Kim, Junyong Park, Jeongseok Kim, Dohyeun Kim은 Part time 표기다.
[^master]: Master students. <https://www.ai2lab.kaist.ac.kr/members/master-student> 2026-10-27 열람. 10명의 이름·연구 주제·학력·Entrance Date를 게시한다.
[^alumni]: Alumni. <https://www.ai2lab.kaist.ac.kr/members/alumni> 2026-10-27 열람. 학력 칸에 KAIST 석사·박사 2021–2026년이 게시된 16행을 담았다. Kyumin Park의 두 카드를 구분하고 이름 옆의 진로 기관을 옮겼다.
[^pubs]: 연구실 논문 목록. <https://www.ai2lab.kaist.ac.kr/publication> 2026-10-27 열람. 2021–2026년 구역의 국제 학술지·국제 학회 및 워크숍·국내 학회 원행 63건에서 4행을 제외하고 같은 논문의 중복 1행을 합쳐 58편이다. 2022–2023년 묶음과 게재 승인·채택 표기를 포함한다.
[^projects]: 현재 과제. <https://www.ai2lab.kaist.ac.kr/projects> 2026-10-27 열람. AiFly(KAI, 2023~), AiRobot(ROBOne, 2023 ~), Ailee 2024(MSIT, 2022 ~ 2025)를 게시한다.
[^vton-news]: 가상 착의 연구 소개. <https://www.ai2lab.kaist.ac.kr/highlights/time-efficient-and-indentity-consistent-vton> 2026-10-27 열람. ECCV 2024 채택을 명시한다. 게시일은 별도로 적지 않는다.
[^medcagd]: MedCAGD arXiv 초록. <https://arxiv.org/abs/2607.00409> 2026-10-27 열람. ECCV 2026 채택을 명시하고, 의료영상 분할용 디코더의 설계를 설명한다.
[^bscore]: B-score arXiv 초록. <https://arxiv.org/abs/2505.18545> 2026-10-27 열람. 응답 이력으로 언어 모델의 편향을 검출하는 지표를 제안하며 ICML 2025 채택을 명시한다.
[^bio1]: DDRL:Dyna-Based Discriminative Reinforcement Learning for Optimizing Sepsis Treatment Pathways in Offline Environments; OpenAlex 등록 초록. <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211> 2026-10-27 열람. DDRL은 판별기와 모의 학습 경험을 결합한 새 강화학습 방법을 제안한다. DOI 10.1109/JBHI.2026.3684575.
[^bio2]: Deep Multimodal Emotion Recognition using Modality-Aware Attention and Proxy-based Multimodal Loss; OpenAlex 등록 초록. <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211> 2026-10-27 열람. 생체 신호 융합을 위한 새 주의 기법과 다중 자료 손실 함수를 제안한다. DOI 10.1016/j.iot.2025.101562.
[^bio3]: Deep Representation Learning with Assisted Domain Adaptation for EEG-based Cross-Subject Emotion Recognition; OpenAlex 등록 초록. <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211> 2026-10-27 열람. ADARL의 새 주의 모듈과 범주별 응집 손실 함수를 제안한다. DOI 10.1109/tcss.2025.3622319.
[^bio5]: Deep Representation Learning with Sample Generation and Augmented Attention Module for Imbalanced ECG Classification; OpenAlex 등록 초록. <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211> 2026-10-27 열람. 심전도 분류의 새 재표본화 전략과 주의 모듈을 제안한다. DOI 10.1109/JBHI.2023.3325540.
[^bio6]: Digital health in smart cities: Rethinking the remote health monitoring architecture on combining edge, fog, and cloud; Europe PMC 등록 초록. <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/s12553-023-00753-3%22> 2026-10-27 열람. VitalSense는 계층별 자료 압축·암호화·알림·실행·처리 분담을 결합한 새 원격 건강 감시 구조를 제안한다. DOI 10.1007/s12553-023-00753-3.
[^p1]: Y. Tolcha 외, D. Kim, IEEE Access (2021). <https://doi.org/10.1109/ACCESS.2021.3069194> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211>. 2026-10-27 열람.
[^p2]: Y. K. Tolcha, G. Park, D. Kim, 2025 IEEE International Conference on RFID (RFID) (2025). <https://doi.org/10.1109/RFID64926.2025.11015538> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s12553-023-00753-3%7C10.1016/j.eswa.2021.115211%7C10.1016/j.iot.2025.101562%7C10.1109/access.2021.3069194%7C10.1109/jbhi.2023.3325540%7C10.1109/jbhi.2026.3684575%7C10.1109/rfid64926.2025.11015538%7C10.1109/tcss.2025.3622319%7C10.9717/kmms.2026.29.2.211>. 2026-10-27 열람.
[^p3]: H. Hwang, N. D. Son, D. Kim, ICML 2026; arXiv 판 (온라인 2026-02-04). <https://arxiv.org/abs/2602.04509> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.04509>. 2026-10-27 열람.
[^p4]: A. Vo 외, D. Kim, ICLR 2026; arXiv 판 (온라인 2025-05-29). <https://arxiv.org/abs/2505.23941> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2505.23941>. 2026-10-27 열람.
[^p5]: D. P. Tran, D. D. Hung, D. Kim, ICCV 2025; arXiv 판 (온라인 2025-06-28). <https://arxiv.org/abs/2506.22762> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.22762>. 2026-10-27 열람.
[^p6]: P. Dam, J. Jeong, A. Tran, D. Kim, ECCV 2024; arXiv 판 (온라인 2024-03-12). <https://arxiv.org/abs/2403.07371> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.07371>. 2026-10-27 열람.
[^p7]: S. Wazir, D. Kim, CVPR 2025; arXiv 판, 30861-30871 (온라인 2025-06-23). <https://arxiv.org/abs/2506.18335> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.18335>. 2026-10-27 열람.
[^p8]: K. Lee, K. Park, D. Kim, ICASSP 2023; arXiv 판 (온라인 2022-07-03). <https://arxiv.org/abs/2207.01063> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2207.01063>. 2026-10-27 열람.

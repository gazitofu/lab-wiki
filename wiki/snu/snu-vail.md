# 자율주행 및 차량 지능 연구실 (Vehicle Autonomy & Intelligence Lab, VAIL)

**서울대학교 공과대학 기계공학부 · 좌은혁 조교수**

- 분야: 자율주행, 제어공학, 차량 동역학[^dept]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 자율주행[^home], 제어 이론·제어 공학[^home][^dept]
- 홈페이지: <https://sites.google.com/view/snu-vail>
- 근거와 출처: [자율주행 및 차량 지능 연구실 근거 페이지](snu-vail-sources.md)

> 차량이 안전하게 스스로 달리고 새로운 도로와 도시에서도 작동하도록, 자율주행의 판단·움직임과 차량 제어 방법을 연구한다.

## 무엇을 연구하나

자율주행 및 차량 지능 연구실은 자율주행 시스템과 차량 제어 시스템이 실제 차량에서 안전하게 작동하고, 새로운 도로와 도시로 확장되며, 에너지를 효율적으로 쓰는 것을 목표로 한다. 차량과 이동 로봇이 스스로 판단하고 움직이는 데 필요한 이론과 알고리즘(문제를 풀기 위한 계산 절차)을 개발한다.[^home]

연구 범위에는 차량의 행동과 이동 경로를 정하는 계획, 시각·언어·행동 모형(Vision-Language-Action, VLA, 영상과 언어 정보를 함께 처리해 행동을 생성하는 계산 모형)을 이용한 의사결정, 차량 동역학(힘과 회전 작용에 따른 차량의 움직임을 다루는 분야)과 제어가 있다. 계획한 행동을 실행한 결과를 다시 반영하는 폐루프 계획을 실제 차량에서 검증하고, 미끄러운 도로에서 차량이 다룰 수 있는 움직임의 한계를 넓히는 연구를 내세운다.[^home][^research]

학과 교수 소개는 자율주행을 위한 이론과 알고리즘 개발을 전문 분야로 밝히고, 강화학습(행동에 따른 보상을 바탕으로 행동 방식을 배우는 기계학습 방법)과 모델 예측 제어를 예로 든다. 모델 예측 제어는 모형으로 앞날의 움직임을 예측해 입력을 정하고, 새 측정값이 오면 이 계산을 반복하는 방법이다.[^dept]

## 주요 연구 주제

### 1. 자율주행의 행동과 이동 계획

주변 상황에 맞춰 어떤 행동을 하고 어떻게 움직일지 정하는 방법을 연구한다. 연구 소개는 자율 시스템이 할 수 있는 행동의 범위를 넓히는 것을 목표로 삼으며, 첫 화면은 폐루프 계획과 실제 차량 검증을 연구 범위로 든다.[^research][^home]

### 2. 시각·언어·행동 모형의 판단

이 모형을 의사결정에 쓰는 연구다.[^home] 대표 논문은 모형이 만들어 낸 추론 내용이 행동에 미치는 세기를 조절한다. 추론 내용을 포함한 경우와 제거한 경우를 이용해 단계마다 그 영향을 낮추거나 높이고, 각 선택의 결과를 측정한 값으로 제어 방법을 학습한다.[^p1]

### 3. 차량의 움직임과 제어

차체의 주행 관련 장치를 다루는 섀시 제어와 차량이 다룰 수 있는 움직임의 한계에서의 제어를 연구 범위로 든다. 연구 소개는 미끄러운 도로에서 차량의 움직임을 제어하는 능력을 높여 생명을 보호한다는 목표를 제시한다.[^home][^research]

## 대표 논문

좌은혁 교수가 서울대에 부임한 2026년 3월 이후 서울대 소속으로 발표한 논문 가운데, 개별 초록이 있고 교신저자 역할이 표시된 사전 공개 논문 한 편을 골랐다. “쉽게 말하면” 칸은 이 논문의 초록만을 근거로 썼다.[^people][^paper-role]

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function](https://doi.org/10.48550/arxiv.2610.40002) · arXiv 사전 공개본, 2026-10-29 | 영상과 언어를 행동으로 연결하는 모형이 쓴 추론 내용은 행동을 잘못 이끌 수 있다. 연구진은 추론 내용의 영향력을 행동 생성 단계마다 조절하고, 각 조절값을 한 단계 적용한 뒤 현재 제어 방법으로 나머지 계획을 완성해 그 결과의 가치를 측정했다. 이 값으로 평가 모형을 학습해 조절값을 선택한다. Alpasim 운전 모의 환경의 폐루프 평가에서는 300개 장면 가운데 262개를 통과했으며, 원래 모형은 252개를 통과했다.[^p1] | 1저자 Dabin Seo, 교신저자·마지막 저자 Eunhyek Joa[^paper-role] |

## 교수와 전문 분야

좌은혁(Eunhyek Joa)은 서울대학교 기계공학부 조교수다. 연구실 교수 소개는 기계공학부 부임을 2026년 3월, Department of Future Autonomotive Mobility의 조교수 시작을 2026년 5월로 적는다.[^dept][^people]

서울대학교에서 기계공학 학사(2014)와 석사(2016)를 받고, University of California, Berkeley에서 기계공학 박사(2024)를 받았다. 석사 지도교수는 이경수, 박사 지도교수는 Francesco Borrelli다. 2025년 1월부터 2026년 2월까지 Amazon의 로보택시 회사 Zoox에서 자율주행 행동 분야 소프트웨어 엔지니어로 일했다.[^people]

전문 분야는 자율주행, 제어공학, 차량 동역학이다. 현재 연구는 차량이 할 행동을 정하는 이론과 알고리즘, 움직임의 안전성과 에너지 효율, 시각·언어·행동 모형의 의사결정으로 이어진다.[^dept][^home]

## 응용 분야

목표 응용은 실제 도로에서 안전하고 에너지 효율적으로 움직이는 자율주행 차량과 이동 로봇이다. 연구실은 차량에서 작동하는 계획·제어 방법을 새로운 도로와 도시로 확장하는 것을 목표로 한다. 후원 기관으로 Hyundai Motor Company, 한국교통안전공단, SUM, 경기도, KakaoMobility를 적는다.[^home]

## 구성원

2026년 11월 9일 연구실 People에 게시된 박사과정 9명, 석사과정 2명, 인턴 1명이다. 괄호 안 ME·AI와 숫자는 누리집의 과정 표기이고, 연구 주제도 게시 표기 그대로다. 이현지·이승훈의 시작 연월은 첫 화면의 합류 소식에 적힌 2026년 9월이다. “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people][^home]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| 김상윤 (Sangyoon Kim) · 랩장 | 박사과정 (ME 21a) |  | Reinforcement learning | oiei0806@snu.ac.kr |  |
| 서다빈 (Dabin Seo) | 박사과정 (ME 21a) |  | Vision-Language-Action Model | sdabin@snu.ac.kr | 1 |
| 김동영 (Dongyoung Kim) | 박사과정 (ME 20a) |  | Diffusion Planner | kimdy0324@snu.ac.kr |  |
| 노한석 (Hanseok Noh) | 박사과정 (ME 20a) |  | Scenario generation | nhs0601@snu.ac.kr |  |
| 송혜령 (Hyeryeong Song) | 박사과정 (AI 22a) |  | 3D Perception, Sensor Fusion, End-to-End Autonomous Driving | hr.song@snu.ac.kr |  |
| 곽지섭 (Jisub Kwak) | 박사과정 (ME 21a) |  | 3D reconstruction | kjs675252@snu.ac.kr |  |
| 전명근 (Myeonggeun Jun) | 박사과정 (ME 21b) |  | Optimization, Control | wjsaud0909@snu.ac.kr |  |
| 이태훈 (Taehoon Lee) | 박사과정 (ME 22a) |  | Optimization, Control | tae.hoon.lee@snu.ac.kr |  |
| 국윤영 (Yunyoung Kook) | 박사과정 (ME 21b) |  | 3D Perception, Sensor Fusion, Local Map Generation | chloecook0524@snu.ac.kr |  |
| 이현지 (Hyeonji Lee) | 석사과정 (ME 26b) | 2026.09 |  | hyeonjilee@snu.ac.kr |  |
| 이승훈 (Seunghoon Lee) | 석사과정 (ME 26b) | 2026.09 |  | kl690374@snu.ac.kr |  |
| 양재민 (Jaemin Yang) | 인턴 |  |  |  |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 2026년 학회 채택 논문 1편과 Research의 선정 논문 가운데 2023–2025년 7편이다. 2023–2025년 논문은 좌은혁 교수의 2026년 3월 서울대 부임 전 논문이다. 제목·저자·발표처는 연구실 표기이고, DOI를 함께 적었다. 연구실이 Accepted로 적은 학회 논문은 발표처 뒤에 “채택”으로 표시한다.[^pubs][^research][^people][^oa]

**2026**

- Myeonggeun Jun and Eunhyek Joa. "Predictive Safety Filter for Multi-Modal Learned Policies". *65th IEEE Conference on Decision and Control (CDC), Hawaii, USA, 2026 (채택)*.

**2025**

- Shengfan Cao, Eunhyek Joa, and Francesco Borrelli. "A Simple Approach to Constraint-Aware Imitation Learning with Application to Autonomous Racing". *2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) · DOI <https://doi.org/10.1109/iros60139.2025.11247769>*.
- Eunhyek Joa and Francesco Borrelli. "Approximate solution of stochastic infinite horizon optimal control problems for constrained linear uncertain systems". *IEEE Transactions on Automatic Control (2025) · DOI <https://doi.org/10.1109/tac.2025.3560212>*.

**2024**

- Eunhyek Joa, Eric Yongkeun Choi, and Francesco Borrelli. "Energy-efficient predictive control for connected, automated driving under localization uncertainty". *IEEE Transactions on Intelligent Vehicles (2024) · DOI <https://doi.org/10.1109/tiv.2024.3442670>*.
- S. H. Nair\*, H. Lee\*, Eunhyek Joa\*, et al. "Predictive control for autonomous driving with uncertain, multimodal predictions". *IEEE transactions on control systems technology 33.4 (2024): 1178-1192 · DOI <https://doi.org/10.1109/tcst.2024.3451370>*.
- Eunhyek Joa et al. "Piecewise affine relaxation of discrete value functions in learning model predictive control with application to autonomous racing". *IEEE Control Systems Letters 8 (2024): 2187-2192 · DOI <https://doi.org/10.1109/lcsys.2024.3455174>*.

**2023**

- Eunhyek Joa\*, H. Lee\*, et al. "Energy-efficient lane changes planning and control for connected autonomous vehicles on urban roads". *2023 IEEE Intelligent Vehicles Symposium (IV) · DOI <https://doi.org/10.1109/iv55152.2023.10186574>*.
- Eunhyek Joa, Monimoy Bujarbaruah, and Francesco Borrelli. "Output Feedback Stochastic MPC with Hard Input Constraints". *2023 American Control Conference · DOI <https://doi.org/10.23919/acc55779.2023.10155959>*.

## 소식

연구실 첫 화면의 2026년 3월 출범 소식과 2026년 7월 모델 순위 소식이다. 3월은 누리집이 적은 연월이고, 순위는 7월 7일 기준이다.[^home]

- 2026-07-07 · 서다빈의 모델이 Waymo vision e2e challenge에서 1위를 기록했다(Spotlight 시나리오에서도 1위, 7월 7일 기준).
- 2026-03 · 서울대학교에서 Vehicle Autonomy & Intelligence Lab을 출범했다.

## 연락과 위치

- 교수 사무실: 서울대학교 301동 1407호[^dept]
- 연구실: 서울대학교 301동 1201호[^dept]
- 전화: 02-880-9104(학과 교수 상세 상단 연락처)[^dept]
- 홈페이지: <https://sites.google.com/view/snu-vail>
[^home]: Vehicle Autonomy & Intelligence Lab, Home의 About Us·연구 분야·News·후원 기관. <https://sites.google.com/view/snu-vail/home> 관측 2026-11-09.
[^people]: Vehicle Autonomy & Intelligence Lab, People의 교수 경력·학력과 구성원. <https://sites.google.com/view/snu-vail/people> 관측 2026-11-09.
[^research]: Vehicle Autonomy & Intelligence Lab, Research의 Autonomy Behaviors·Vehicle Dynamics and Control 및 선정 논문 목록. <https://sites.google.com/view/snu-vail/research> 관측 2026-11-09.
[^pubs]: Vehicle Autonomy & Intelligence Lab, Publications의 2026년 학회 채택 논문. <https://sites.google.com/view/snu-vail/publications> 관측 2026-11-09.
[^dept]: 서울대학교 기계공학부, 좌은혁 (Joa, Eunhyek) 교수 상세의 직급·연구실명·연구 분야·연락처·위치. <https://me.snu.ac.kr/snu__professor/%ec%a2%8c%ec%9d%80%ed%98%81-joa-eunhyek/> 관측 2026-11-09.
[^oa]: OpenAlex, Eunhyek Joa(ORCID 0000-0003-2973-2144)의 2021–2026년 논문 서지·초록 18편. <https://openalex.org/A5061734977> 관측 2026-11-09.
[^paper-role]: Dabin Seo·Eunhyek Joa, How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function, arXiv:2610.40002v1의 서울대학교 기계공학부 소속 및 교신저자 표시. <https://arxiv.org/html/2610.40002v1> 관측 2026-11-09.
[^p1]: D. Seo, E. Joa, arXiv:2610.40002v1（사전 공개본） (온라인 2026-10-29). <https://doi.org/10.48550/arxiv.2610.40002> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.40002> 관측 2026-11-09.

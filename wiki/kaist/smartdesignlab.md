# 스마트설계연구실 (Smart Design Lab, SDL)

**KAIST 기계공학과 · 강남우 부교수**

- 분야: 인공지능 기반 공학 설계, 자율설계, 설계 최적화[^research][^prof]
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 설계 최적화(위상·형상 최적화)[^research], 과학·공학 AI[^research]
- 홈페이지: <https://www.smartdesignlab.org/>
- 근거와 출처: [스마트설계연구실 근거 페이지](smartdesignlab-sources.md)

> 인공지능으로 제품의 설계안을 만들고 성능과 고객 선호를 예측하며, 주어진 조건에 맞는 부품의 모양과 기계의 연결 구조를 찾는 연구실이다.[^research]

## 무엇을 연구하나

스마트설계연구실은 강남우 교수가 이끄는 인공지능 기반 공학 설계 연구실이다. 인공지능(Artificial Intelligence, AI)은 학습·추론·판단 같은 지적 작업을 계산으로 수행하는 기술이다. 연구실은 설계 최적화(정해진 조건을 만족시키면서 목표값을 최소화하거나 최대화하도록 제품의 모양·치수 등을 정하는 방법)와 인공지능을 결합하는 원리를 연구하고, 제품 설계에 필요한 새 방법을 개발한다.[^research]

연구는 설계안 생성, 성능 예측, 최적 설계의 세 축으로 구성된다. 생성 인공지능(학습 자료의 패턴을 바탕으로 새로운 이미지·글 등의 자료를 만드는 인공지능)을 이용해 설계 후보를 만들고, 후보의 공학적 성능·제조 가능성·심미성 등을 예측한다. 이어 목표 성능과 제약 조건에 맞는 설계안을 찾는다. 여기서 심미성은 외형에서 느끼는 아름다움의 성질을 뜻한다.[^research]

연구실이 지향하는 자율설계는 사람의 감독 아래 인공지능이 문제를 정의하고 도구를 선택하며 설계안을 발전시키는 방식이다. 이를 위해 물리 법칙에 근거해 제품의 작동을 예측하는 능력과, 작업 순서를 계획하고 여러 공학 도구를 연결해 결과를 고치는 능력을 함께 개발한다. 연구 소개는 이 기술의 적용 분야로 모빌리티(사람과 물건을 이동시키는 수단과 서비스), 전자제품, 중공업, 로봇을 든다.[^research]

## 주요 연구 주제

### 1. 요구 조건에 맞는 설계안 생성

제품의 모양과 구조를 여러 안으로 만들고, 원하는 동작이나 성능을 갖춘 후보를 찾는다. 예를 들어 네 개의 막대가 연결된 기구를 대상으로, 각 막대 길이와 요구되는 움직임·힘 조건의 관계를 학습한 생성 모형을 개발했다. 이 모형은 같은 요구 조건을 만족하는 서로 다른 연결 기구들을 생성했다. 준정적 조건은 운동 상태의 변화를 거스르는 관성의 영향을 무시하고, 힘과 돌림 작용이 균형을 이루는 것으로 다루는 조건이다.[^p5]

### 2. 물리 거동과 공학 성능 예측

제품의 모양과 작동 조건을 받아 성능을 계산하는 예측 방법을 연구한다. 시뮬레이션(대상의 작동을 계산 모형으로 재현하는 방법)의 계산 부담을 줄이기 위해, 그 결과를 근사하는 대리모델을 만든다. 신경망은 연결된 계산 단위들이 자료에서 입력과 출력의 관계를 학습하는 모형이다. 그래프 신경망(Graph Neural Network, GNN)은 자료의 각 대상과 대상 사이의 연결 관계를 함께 학습하는 신경망이다. 한 연구는 그래프 신경망에서 제품 형상을 나눈 계산 요소의 크기를 조절하면서 중요한 형상 정보를 유지하고 성능을 예측한다. 다른 연구는 유체의 흐름을 시간 순서대로 예측할 때 오차가 누적되는 문제를 다룬다.[^p4][^p2]

### 3. 기구의 성능과 제조 비용을 함께 고려하는 설계

기구는 부품들이 연결되어 정해진 움직임을 만드는 구조다. 연구진은 여러 사용 조건에 맞는 기구 설계를 먼저 구한 뒤, 이를 묶어 공통으로 쓸 대표 설계를 정하는 방법을 제안했다. 공통 부품을 사용해 생산 규모의 이점을 얻는 것과, 조건별 요구 성능에서 벗어나는 정도를 함께 고려한다. 제조 비용을 정하는 값들이 달라질 때 어떤 모듈화 전략을 선택할지도 분석한다. 모듈화는 시스템을 일정한 연결 규칙에 따라 조합할 수 있는 기능 단위로 나누어 구성하는 방식이다.[^p3]

### 4. 설계 특징과 개인별 선호 예측

제품 외형을 이루는 정보를 간추리고, 사람마다 다른 디자인 선호를 예측한다. 연구진은 설계 샘플을 적은 수의 특징값으로 바꾸고, 다른 사람들의 선호 경향도 활용해 개인별 선호를 예측하는 방법을 제안했다. 제품 개발과 개인별 제품 추천을 돕는 것이 목표다.[^p1]

## 대표 논문

강남우 교수가 KAIST 소속 교신저자로 참여한 2021–2026년 논문 가운데 설계안 생성, 물리 거동 예측, 기구 설계 최적화, 고객 선호 예측을 보여 주는 6편을 골랐다. 교신저자는 논문의 질의와 연락을 담당하는 저자다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Learning design preferences through design feature extraction and weighted ensemble](https://doi.org/10.1093/jcde/qwag029) · Journal of Computational Design and Engineering | 제품 외형의 많은 정보를 적은 수의 특징값으로 간추리고, 다른 사람들의 선호 경향을 함께 활용해 개인의 디자인 선호를 예측하는 방법을 제안했다. 설계의 핵심 특징을 찾고 개인별 제품 추천을 돕는 틀이다.[^p1] | 1저자 Dongju Shin · 교신저자 Namwoo Kang |
| 2 | 2025 | [Model-agnostic AI framework with explicit time integration for long-term fluid dynamics prediction](https://doi.org/10.1093/jcde/qwaf099) · Journal of Computational Design and Engineering | 유체의 다음 상태를 반복해서 예측하면 오차가 쌓이는 문제를 다룬다. 과거의 변화율을 이용하는 시간 계산법과, 학습 중 미래 시점별 중요도를 조절하는 방법을 결합했다. 방정식 예제와 원기둥 주위 흐름에서 장기 예측의 안정성과 정확도를 평가했다.[^p2] | 1저자 Sunwoong Yang · 교신저자 Namwoo Kang |
| 3 | 2025 | [Modular Mechanism Design Optimization in Large-Scale Systems with Manufacturing Cost Considerations](https://doi.org/10.1007/s40684-025-00770-9) · International Journal of Precision Engineering and Manufacturing-Green Technology | 사용 조건별로 최적 기구를 구하고 설계들을 여러 묶음으로 나누어, 묶음의 모든 조건을 만족하는 대표 설계를 정한다. 부품을 공통으로 생산할 때의 이점과 성능 차이를 함께 고려하며, 제조 비용을 정하는 값들을 분석해 설계 전략 선택을 돕는다.[^p3] | 1저자 Sumin Lee · 교신저자 Namwoo Kang |
| 4 | 2024 | [BMO-GNN: Bayesian mesh optimization for graph neural networks to enhance engineering performance prediction](https://doi.org/10.1093/jcde/qwae102) · Journal of Computational Design and Engineering | 제품 형상을 나눈 계산 요소와 그 연결 관계에서 성능을 학습하는 모형이다. 베이지안 최적화로 계산 요소의 크기를 정한다. 질량, 림 강성, 디스크 강성을 예측한다고 보고했고, 형상의 세부 정보와 계산 부담을 함께 고려한다.[^p4] | 1저자 Jangseop Park · 교신저자 Namwoo Kang |
| 5 | 2024 | [Deep generative model-based synthesis framework of four-bar linkage mechanisms with target conditions](https://doi.org/10.1093/jcde/qwae084) · Journal of Computational Design and Engineering | 네 막대 연결 기구의 요구 조건과 막대 길이 사이의 관계를 학습하는 생성 모형을 제안했다. 움직일 수 있는 범위와 기하 구조를 목표로 삼아, 지정된 움직임과 준정적 조건을 만족하는 다양한 기구를 생성하고 기존 최적화·생성 방법과 비교했다.[^p5] | 1저자 Sumin Lee · 교신저자 Namwoo Kang |
| 6 | 2023 | [Adaptive neural network ensemble using prediction frequency](https://doi.org/10.1093/jcde/qwad071) · Journal of Computational Design and Engineering | 여러 신경망의 예측값에서 자주 모이는 범위를 찾아 결합한다. 그 범위에 속한 예측값들이 퍼진 정도를 이용해 학습 자료를 순차적으로 추가하는 방법도 제안했다. 여러 예제에서 기존 예측 결합법과 자료 선택법을 비교했다.[^p6] | 1저자 Ungki Lee · 교신저자 Namwoo Kang |

## 교수와 전문 분야

강남우 교수(Namwoo Kang)는 KAIST 기계공학과 부교수다. 서울대학교에서 기계항공공학 학사(2005)와 기술경영 석사(2007)를, 미국 미시간대학교에서 Design Science 박사(2014)를 받았다. 현대자동차 연구원(2007–2010), 미시간대학교 연구원·강사(2014–2016), KAIST K-School 조교수(2016–2018), 숙명여자대학교 기계시스템학부 조교수(2018–2021)를 지냈다. 2021년 KAIST 모빌리티대학원 조교수로 복귀했고, 2023–2026년 같은 대학원 부교수를 거쳐 2026년 기계공학과 부교수로 옮겼다.[^prof] 2021년 6월 출판 기록에서 이미 KAIST 조천식녹색교통대학원 소속으로 적혀 있다.[^appointment]

교수 소개가 밝힌 전문 분야는 인공지능 기반 공학 설계, 생성형 설계, 자료 기반 설계, 기계학습·딥러닝, 설계 최적화, 위상 최적화, 컴퓨터 지원 설계·제조·해석, 인간과 컴퓨터의 상호작용이다. 기계학습은 자료에서 규칙을 학습해 예측이나 판단을 하는 방법이고, 딥러닝은 여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야다. 위상 최적화는 정해진 공간에서 재료를 어디에 놓을지 정해 목표 성능을 얻는 설계 방법이다. 교수는 나니아랩스 대표도 맡고 있다.[^prof]

## 응용 분야

연구 소개는 모빌리티·전자제품·중공업·로봇 등 제조 분야의 제품 개발을 응용 대상으로 든다. 생성, 예측, 최적화를 연결해 제품 개발 속도와 성능을 개선하는 것을 목표로 한다. 연구실에서 분사한 나니아랩스는 공학 설계를 위한 로코드(직접 작성하는 프로그램 코드를 줄여 응용 기능을 구성하는 방식) 인공지능 플랫폼을 제공한다.[^research]

## 구성원

2026년 11월 7일 연구실 RESEARCHERS에 게시된 19명이다. 박사과정 8명, 석박사통합과정 1명, 석사과정 9명, 연구 직원 1명이다. 연구 주제와 학교 이메일은 게시 표기를 따른다. "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| SEOKJUN KIM (김석준) | 박사과정 (Lab representative) | Generative Design & Optimization, Time-series Data, Multi-fidelity Method | waiatz1214@kaist.ac.kr |  |
| JANGSEOP PARK (박장섭) | 박사과정 | LLM for Engineering Applications Design Optimization Surrogate Modeling 3D Deep Learning | jangseop@kaist.ac.kr | 4 |
| SANGHYUK KIM (김상혁) | 박사과정 | AI-driven Engineering Design, Autonomous Design, Design Optimization | sanghyukkim@kaist.ac.kr |  |
| JIYONG KIM (김지용) | 박사과정 | AI for CAE Constrained-Aware Layout Optimization Reinforcement Learning | sbo05050@kaist.ac.kr |  |
| YONGMIN KWON (권용민) | 박사과정 | Autonomous Design, Engineering Foundation Model | kymin1002@kaist.ac.kr |  |
| LEEKYO JEONG (정이교) | 박사과정 | Generative Design Editing |  |  |
| DONGEON LEE (이동언) | 석박사통합과정 | Generative Design, Design Optimization, Virtual Product Development | dongeon.lee@kaist.ac.kr |  |
| DONGJU SHIN (신동주) | 박사과정 | AI-based 3D CAE, Design Optimization | dongju1118@kaist.ac.kr | 1 |
| JIHOON KIM (김지훈) | 박사과정 | Design for Manufacturing (DFM), Design Optimization, Generative Design | jihoon.kim@kaist.ac.kr | 5 |
| WONJAE JANG (장원재) | 석사과정 | 3D Generative Model, Design Optimization, LLM for Engineering Applications | wonjae.jang@kaist.ac.kr |  |
| JINSEONG HAN (한진성) | 석사과정 | Multi-physics, Autonomous Design, Design Optimization | nethan1012@kaist.ac.kr |  |
| SANGHYEON KIM (김상현) | 석사과정 | SciML, AI for CAE | csmd2012@kaist.ac.kr |  |
| YURIM LEE (이유림) | 석사과정 | Parametric Design CAD Generation | yurim.lee@kaist.ac.kr |  |
| DONGHOON OH (오동훈) | 석사과정 | Generative Design, Design Optimization, Smart Manufacturing | ohdonghoon9@kaist.ac.kr |  |
| YUBIN LEE (이유빈) | 석사과정 | Design Exploration, Generative Design | yubin.lee@kaist.ac.kr |  |
| JINSU RA (나진수) | 석사과정 | Thermo-Fluid Predictive AI, Generative Design LLM for Engineering Applications | jsera001@kaist.ac.kr |  |
| SUHO YOO (유수호) | 석사과정 | Generative Design, Reinforcement Learning | dbtngh1031@kaist.ac.kr |  |
| HYEONBEEN SEO  (서현빈) | 석사과정 | Optimization AI, Bayesian Optimization, Electrified Mobility | shbj0524@kaist.ac.kr |  |
| BOKYEONG KIM (김보경) | 연구 직원 |  | sirom27@kaist.ac.kr |  |

## 졸업생과 이전 구성원

ALUMNI의 대학원생·박사후 구획 13명, 연구원 구획 6명, 학부 인턴 구획 12명이다. 학위·과정과 소속, 진로는 게시 표기대로 적었다. Experience로 시작하는 칸은 현재 직위가 아닌 경력 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| KYUYEOL PARK  (박규열) | M.S. (2026), Division of Future Vehicle, KAIST | RebuilderAI (CTO) |
| YESEUL CHO (조예슬) | M.S. (2026), CCS Graduate School of Mobility, KAIST | KORAIL |
| SANGHOON JIN (진상훈) | M.S. (2026), CCS Graduate School of Mobility, KAIST | ADD (Agency for Defense Development) |
| SUN WOONG YANG  (양선웅) | Postdoc (2026), Machine Technology Research Institute, KAIST | Hanyang University ERICA (Assistant Professor) |
| SO YOUNG YOO  (유소영) | Postdoc (2026), InnoCORE PRISM-AI Center, KAIST PhD (2025), CCS Graduate School of Mobility, KAIST M.S.(2020), Mechanical Systems Engineering, Sookmyung Women's University | Samsung Electronics |
| SU MIN LEE  (이수민) | PhD (2025), Mechanical Engineering, KAIST M.S.(2022), Mechanical Engineering, KAIST | Jeonbuk National University (Assistant Professor) |
| SEUNG YEON SHIN (신승연) | Researcher(2023), CCS Graduate School of Mobility, KAIST M.S.(2023), CCS Graduate School of Mobility, KAIST | Hyundai Motor Company |
| AH HYEON JIN  (진아현) | Researcher(2022), CCS Graduate School of Mobility, KAIST M.S.(2022), Mechanical Systems Engineering, Sookmyung Women's University | Hyundai Motor Company |
| UNG KI LEE (이웅기) | Postdoc(2022), CCS Graduate School of Mobility, KAIST PhD, Mechanical Engineering, KAIST | Korea University (Assistant Professor) |
| SEONG SIN KIM (김성신) | Postdoc(2022), CCS Graduate School of Mobility, KAIST PhD(2022), Mechanical Systems Engineering, Sookmyung Women's University | Soongsil University (Assistant Professor) |
| MIN YOUNG JWA (좌민영) | M.S.(2022), Mechanical Systems Engineering, Sookmyung Women's University | Hyundai Mobis |
| EUN JI KIM (김은지) | M.S.(2021), Mechanical Systems Engineering, Sookmyung Women's University | Narnia Labs (Co-founder) |
| SUNG HEE LEE (이성희) | M.S.(2021), Mechanical Systems Engineering, Sookmyung Women's University | Narnia Labs (Co-founder) |
| SEUNG GYU KIM (김승규) | Researcher(2023), CCS Graduate School of Mobility, KAIST |  |
| SEONG JUN HONG (홍성준) | Researcher(2022), CCS Graduate School of Mobility, KAIST | Narnia Labs (Co-founder) |
| GI BBEUM LEE (이기쁨) | Researcher, Mechanical Systems Engineering, Sookmyung Women's University | KAIST 문화기술대학원 (PhD Student) |
| YE BIN YOUN (윤예빈) | Researcher, Mechanical Systems Engineering, Sookmyung Women's University Researcher, CCS Graduate School of Mobility, KAIST | Narnia Labs |
| SANG EUN OH (오상은) | Researcher, Mechanical Systems Engineering, Sookmyung Women's University | Experience: SK, KAIST |
| TAI SHIN CHUNG (정태신) | Researcher, Mechanical Systems Engineering, Sookmyung Women's University | Experience: KAIST, 이화여대 |
| SEUNG HEON JANG (장승헌) | Undergraduate Student(2022), Mechanical Engineering, KAIST |  |
| JUNG HUN LEE (이정훈) | Undergraduate Student(2022), Industrial Design, Hongik University |  |
| YUN HA PARK (박윤하) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| EUN JU JUNG (정은주) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| WOO JIN KWAK (곽우진) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| SEO HUI JOUNG (정서희) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| GYU WON LEE (이규원) | Undergraduate Intern, Department of Applied Physics, Sookmyung Women's University |  |
| HYUN JI OH (오현지) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| JI HYUN LEE (이지현) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| HAE SEUL JEON (전해슬) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| MIN YOUNG KIM (김민영) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |
| HAN YOUNG RYU (류한영) | Undergraduate Intern, Mechanical Systems Engineering, Sookmyung Women's University |  |

## 최근 논문과 저술 목록 (2021–2026)

PUBLICATIONS의 국제 학술지 36편, 국내 학술지 5편, 국제 학회 30건, 국내 학회 108건, 책·책 속 장 3건, 박사 학위논문 3편, 석사 학위논문 10편과 심사 중 원고 5편이다. 연도·저자·제목·발표처는 게시 표기이며, 날짜가 없는 2021년 항목은 게시 연도를 따른다. 게재 승인으로 적힌 2편은 출판 논문과 구분했다. 심사 중 원고는 연결된 arXiv 사전 공개본의 연도를 쓴다. 이 목록은 강남우 교수의 개인 연구 이력에 따른 것으로, 숙명여자대학교 재직 시기의 학위논문도 포함한다.[^pubs][^prof][^oa][^ocean]

**2026**

- [심사 중 원고] Kim, S., Yang, S., and Kang, N.\* "Distance-Aware Attention and Wall-Distance Expert Routing for Transformer-Based 3D Flow Prediction" (심사 중; arXiv 사전 공개본) · DOI: <https://doi.org/10.48550/arxiv.2609.07222>
- [심사 중 원고] Jeong, L., Lee, Y., and Kang, N.\* "Risk-Aware Generative Inpainting for Optimized Design Editing of EV Battery Cooling Channels" (심사 중; arXiv 사전 공개본) · DOI: <https://doi.org/10.48550/arxiv.2609.08387>
- [심사 중 원고] Han, J., Yang, S.\*, Kang, N.\*  "A Multi-Agent System for Motor Design Optimization Using an FEA-AI Hybrid Approach" (심사 중; arXiv 사전 공개본) · DOI: <https://doi.org/10.48550/arxiv.2606.09037>
- [국제 학술지] Yoo, S., Jeong, L., Ra, J., Lee, D., Yang, S., Jeong, H. and Kang, N.\* (2026) "DeepJEB++: Foundation Model-Driven Large-Scale 3D Engineering Dataset via 2D Latent Space Augmentation", Journal of Mechanical Design (게재 승인)
- [국제 학술지] Kwon, Y., and Kang, N.\* (2026) "Zero-Shot Rib Design: Merging Training-Free Generative Prior with Topology Optimization", Advanced Engineering Informatics (게재 승인) · DOI: <https://doi.org/10.1016/j.aei.2026.105276>
- [국제 학술지] Kim, J., Yang, S.\*, and Kang, N.\* (2026) "Point-wise Conditional Diffusion Models for Physical Systems with Shape Variations: Applications to Spatio-temporal and Large-scale Systems" Neural Networks, 203, 109186. · DOI: <https://doi.org/10.1016/j.neunet.2026.109186>
- [국제 학술지] Kim, S., Seo, M., Yang, S.\*, and Kang, N.\* (2026) "Rigid-Deformation Decomposition AI Framework for 3D Spatio-Temporal Prediction of Vehicle Collision Dynamics", Advanced Engineering Informatics, 74, 104749. · DOI: <https://doi.org/10.1016/j.aei.2026.104749>
- [국제 학술지] Kwon, Y., and Kang, N.\* (2026) "Three-dimensional Geometric Augmentation Guided by Engineering Uncertainty", Engineering Applications of Artificial Intelligence, 175, 114648. · DOI: <https://doi.org/10.1016/j.engappai.2026.114648>
- [국제 학술지] Yang, S., Vinuesa, R., and Kang, N.\* (2026) “Mesh-Agnostic Prediction of Unsteady Flow Dynamics using Graph U-Nets”, Expert Systems with Applications, 316, 131843. · DOI: <https://doi.org/10.1016/j.eswa.2026.131843>
- [국제 학술지] Shin, D., Lee, S., and Kang, N.\* (2026) "Learning Design Preferences through Design Feature Extraction and Weighted Ensemble", Journal of Computational Design and Engineering, 13(4), 157-178. · DOI: <https://doi.org/10.1093/jcde/qwag029>
- [국제 학술지] Park, J. and Kang, N.\* (2026) "Point-DeepONet: Predicting Nonlinear Fields on Non-Parametric Geometries under Variable Load Conditions.", Neural Networks, 198, 108560 · DOI: <https://doi.org/10.1016/j.neunet.2026.108560>
- [국내 학술지] Lee, D., Kim, J., Kim, S., Cho, S., Ha, Y., and Kang, N.\* (2026) “베이지안 하이퍼파라미터 최적화를 활용한 파력발전시스템의 대리모델 구축 및 설계 최적화”, Trans. Korean Soc. Mech. Eng. A, 50(4), pp. 317-326
- [국제 학회] Kwon, Y., Kang, N.\* (2026) "SLIM: Spatially-Localized Implicit Manifold for Manufacturable Shape Optimization", ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Jang, W., Kang, N.\* (2026) "Autonomous 3D Design Optimization from 2D Drawings", ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Kim, J., Kim, S., Kang, N.\* (2026) "Constraint-Aware Large-Scale 3D Layout Optimization via Hybrid Deep Reinforcement Learning", ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Han, J., Yang, S., Kang, N.\* (2026) "A Multi-Agent System for IPMSM Design Optimization via FEA-AI Hybrid Approach", ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Park, J. and Kang, N.\* (2026) "LLM-Guided Adaptive Penalty Parameter Updates for Analytical Target Cascading.", the Asian Congress of Structural and Multidisciplinary Optimization 2026 (ACSMO 2026).
- [국제 학회] Kim, S., Yang, S., and Kang, N.\* (2026) "An Efficient Cross-Attention Method for Large-Scale 3D Flow Field Prediction", the Asian Congress of Structural and Multidisciplinary Optimization 2026 (ACSMO 2026).
- [국제 학회] Lee, D., Jeong, L., Yoo, S., Yang, S., and Kang, N.\* (2026) "Enhancing Creativity in 3D Generative Design via a TRIZ-Inspired Text-to-CAD Framework", ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Kim, S., Kang, N.\* (2026) "Mixture-of-Experts for Predictive Modeling of Redefined Multi-Fidelity Time-Series Data"  , ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Jeong, L., Kang, N.\* (2026) "Distributional Reinforcement Learning based Inpainting Agent for Optimal EV Cooling Channel Design" , ASME 2026 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2026)
- [국제 학회] Kim S, Kim H, and Kang N\* (2026) Text-guided multiscale topology optimization for mechanical anisotropy design with TPMS. 17th World Congress on Computational Mechanics (WCCM) & 10th European Congress on Computational Methods in Applied Sciences and Engineering (ECCOMAS)
- [국제 학회] Yoo, S., Jeong, L., Kim, J., Jang, W., and Kang, N.\* (2026) "From Idea to Engineering-Aware Product Design: A Case Study of Toy Car Development using Generative AI", the Asian Congress of Structural and Multidisciplinary Optimization 2026 (ACSMO 2026).
- [국내 학회] Cho, Y., Park, J., Kang, N.\* (2026) “A Data-Driven Framework for Railway Track Condition Assessment Using the Analytic Hierarchy Process”, 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회 (포스터)
- [국내 학회] Ra, J., Yang, S., Kang, N.\* (2026) “Explainable Framework for Aircraft Conceptual Design using a Knowledge Graph-Guided Large Language Model”, 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Kwon, Y., Kang, N.\* (2026) "Zero-Shot Rib Design: Merging Training-Free Generative Model with Topology Optimization", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Jang, W., Kang, N.\* (2026) "Self-Correcting Loop-based Parametric CAD Reconstruction and Optimization from 2D Drawings", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학 술대회
- [국내 학회] Lee, Y., Kang, N.\* (2026) "Generative Pattern Design Framework by Structuring Formative Principles from Heterogeneous References", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회 (포스터)
- [국내 학회] Oh, D., Kang, N.\* (2026) "Graph-Based Manufacturability Evaluation Framework for Sheet Metal Part Design", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회 (포스터)
- [국내 학회] Kim, J., Kim, S., Kang, N.\* (2026) "Constraint-Aware Large-Scale 3D Layout Optimization via Hybrid Deep Reinforcement Learning", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Han, J., Yang, S., Kang, N.\* (2026) "A Multi-Agent System-Based Non-Parametric Image Generation for IPMSM Design Optimization", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Jin, S., Lee, S., Kang, N.\* (2026) "A Global Routing Method for Electronic Circuit Design Integrating Flow Matching and Constrained A\*", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Lee, D., Kang, N.\* (2026) "Federated Learning-based Surrogate Modeling to Address Data Scarcity in Manufacturing", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Kim, S., Yang, S., and Kang, N.\* (2026) "3D Vehicle Aerodynamic Field Prediction Using Physics-Conditioned Expert Transformer", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Jeong, L., Han, J., Jin, S., Kim, D., Park, K., and Kang, N.\* (2026) "Continuous Flow for Discrete Topology: Generative Design Editing of IPMSM via VQ-VFM", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Kim S, Kim H, and Kang N\* (2026) "Text-Guided 3D Multiscale Topology Optimization: TPMS-Based Anisotropic Design for Shape and Stiffness Programming", 대한기계학회 CAE 및 응용역학부문 2026년도 춘계학술대회
- [국내 학회] Ra, J., Yang, S., Kang, N\*. (2026) “Development of a Retrieval-Augmented Local Large Language Model for Aircraft Conceptual Design”, 한국항공우주학회 2026 춘계학술대회

**2025**

- [국제 학술지] Kim, D., Park, D., Seo, J., Cho, H., Ahn, S., Kang, N., and Kim, S\*. (2025). Estimation of Electromagnetic Field Strength: Experiments Using Vision Transformers, IEEE Access, 13, 195735 - 195748
- [국제 학술지] Yang, S., Vinuesa, R., and Kang, N.\* (2025) “Model-Agnostic AI Framework with Explicit Time Integration for Long-Term Fluid Dynamics Prediction”, Journal of Computational Design and Engineering, 12(10), 133-153 · DOI: <https://doi.org/10.1093/jcde/qwaf099>
- [국제 학술지] Kim, S., Kim, H.\*, Kang, N., and Lee, T. H.\* (2025) "Projected Variable Three-Term Conjugate Gradient Algorithm for Enhancing Generalization Performance in Deep Neural Network Training", Neurocomputing, 657, 131568
- [국제 학술지] Lee, S., Yang, S., and Kang, N.\* (2025) “Multi-objective Generative Design Framework and Realization for Quasi-serial Manipulator: Considering Kinematic and Dynamic Performance”, Engineering Applications of Artificial Intelligence, 161, 112142
- [국제 학술지] Yoo, S. and Kang, N.\* (2025) "DeepWheel: Generating a 3D Synthetic Wheel Dataset for Design and Performance Evaluation", Journal of Mechanical Design, 148(5), 051702 · DOI: <https://doi.org/10.1115/1.4069899>
- [국제 학술지] Yang, S., Lee. Y., and Kang, N.\* (2025) "Data-Efficient Deep Operator Network for Unsteady Flow: A Multi-Fidelity Approach with Physics-Guided Subsampling", Computer Methods in Applied Mechanics and Engineering, 446, 118254 · DOI: <https://doi.org/10.1016/j.cma.2025.118254>
- [국제 학술지] Lee, S. and Kang, N.\* (2025) "Modular Mechanism Design Optimization in Large-Scale Systems with Manufacturing Cost Considerations", International Journal of Precision Engineering and Manufacturing-Green Technology, 13(2), 565-589 · DOI: <https://doi.org/10.1007/s40684-025-00770-9>
- [국제 학술지] Kwon, Y. and Kang, N.\* (2025) “3D Deep Shape Optimization with a Limited Dataset”, Engineering Applications of Artificial Intelligence, Volume 159, Part A, 1 November 2025, 111504
- [국제 학술지] Kang, N. (2025) "Generative AI-driven Design Optimization: Eight Key Application Scenarios", JMST Advances, 7, 105-111 · DOI: <https://doi.org/10.1007/s42791-025-00097-1>
- [국제 학술지] Kim, J., Park, J., Kim N., Yu, Y., Chang, K., Woo, C., and Yang, S.\*, and Kang, N.\* (2025) “Physics-Constrained Graph Neural Networks for Spatio-Temporal Prediction of Drop Impact on OLED Display Panels”, Expert Systems with Applications, 274, 126907 · DOI: <https://doi.org/10.1016/j.eswa.2025.126907>
- [국제 학술지] Hong, S., Kwon, Y., Shin, D., Park, J., and Kang, N.\* (2025) “DeepJEB: 3D Deep Learning-based Synthetic Jet Engine Bracket Dataset”, Journal of Mechanical Design, 147(4), 041703 · DOI: <https://doi.org/10.1115/1.4067089>
- [국내 학술지] Kang, N. (2025) “생성형 AI로 최적 설계하기: 8가지 핵심 사용 시나리오”, 기계저널, 65(7), pp. 30-35.
- [국내 학술지] Kim, J. and Kang, N. (2025) “OLED 디스플레이 충격 거동 예측을 위한 그래프 신경망 모델”, 소음진동, 35(4), pp.26-31.
- [국제 학회] Kim, J., Yang, S.\*, and Kang, N.\* (2025) "Point-based Diffusion Model for Predicting Spatio-Temporal Dynamics in Physical Systems", APCOM 2025
- [국제 학회] Kwon, Y., Kang, N.\* (2025) "3D Geometry Augmentation Guided by Engineering Uncertainty", APCOM 2025
- [국제 학회] Kim, S., Yang, S., Seo, M., and Kang, N.\* (2025) “Decoupled Dynamics Framework with Neural Fields for 3D Spatio-Temporal Prediction of Vehicle Collisions”, ASME 2025 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference (IDETC/CIE 2025), DETC2025-167614. · DOI: <https://doi.org/10.1115/detc2025-167614>
- [국제 학회] Park, J. & Kang, N.\* (2025). A PointNet-Enhanced Deep Operator Network for Nonlinear Analysis of Non-Parametric 3D Geometries Under Varying Load Conditions. In The 16th World Congress of STRUCTURAL AND MULTIDISCIPLINARY OPTIMIZATION. The International Society for Structural and Multidisciplinary Optimization.
- [국제 학회] Kang, N. (2025) “Deep Generative Design: Revolutionizing Engineering Design through Generative AI”, NAFEMS World Congress 2025.
- [국내 학회] Jeong, L., Lee, Y., Kang, N.\* (2025) "Designing like the Ship of Theseus: Distributional RL based Inpainting Agent for Optimal EV Cooling Channel Design", 대한기계학회 2025년도 학술대회
- [국내 학회] Yang, S., Kang, N.\* (2025) "AI Agents for Multi-Fidelity Aerodynamic Shape Optimization", 대한기계학회 2025년도 학술대회
- [국내 학회] Lee, Y., Kang, N.\* (2025) "Deep Learning-Based CAD Generation Considering Design Intent and Inter-Feature Constraints", 대한기계학회 2025년도 학술대회 (포스터)
- [국내 학회] Jin, S., Kang, N.\* (2025) "Safe Reinforcement Learning-based Global Routing Considering Constraints", 대한기계학회 2025년도 학술대회
- [국내 학회] Cho, Y., Kang, N.\* (2025) "AI-Driven Integrated System for Railway Track Deformation Prediction and Optimized Maintenance", 대한기계학회 2025년도 학술대회 (포스터)
- [국내 학회] Kim, S., Kang, N.\* (2025) "Multi-Fidelity Neural Networks as Experts: A Mixture-of-Experts Approach", 대한기계학회 2025년도 학술대회
- [국내 학회] Lee, D., Jeong, L., Yoo, S., Yang, S., and Kang, N.\* (2025) "Prompt Engineering-based Parametric CAD Code Generation Framework for 3D Geometric Design Optimization", 대한기계학회 2025년도 학술대회
- [국내 학회] Kim, J., Kim, S., Jin, S., Lee, Y., and Kang, N.\* (2025) "Safe Reinforcement Learning for 3D Large Scale Constrained Layout Optimization", 대한기계학회 2025년도 학술대회
- [국내 학회] Han, J., Yang, S., and Kang, N.\* (2025) "IPMSM Shape Optimization based FEA-AI Hybrid Model using LLM agents", 대한기계학회 2025년도 학술대회
- [국내 학회] Park, J. and Kang, N.\* (2025) "DialogCAD: Interactive CAD Generation Framework with a Multi-Agent System via Model Context Protocol", 대한기계학회 2025년도 학술대회
- [국내 학회] Park, J., Kim, J., Jang, W., Lee, Y., Lee, S., and Kang, N.\* (2025) “A Study on 3D Topology Optimization Shape Reconstruction with CSG-Based Deep Learning”, 대한기계학회 2025년도 학술대회 (포스터)
- [국내 학회] Kim, S., Yang, S., Kim, S., Han, J., and Kang, N.\* (2025) "Transformer-based Framework for Large-Scale 3D Flow Prediction", 대한기계학회 2025년도 학술대회
- [국내 학회] Jang, W., and Kang, N.\* (2025) “From 2D Drawings to 3D CAD: Enhancing MLLM Spatial Reasoning through In-Context Learning”, 대한기계학회 2025년도 학술대회 (포스터)
- [국내 학회] Kim, S., Kim, H., and Kang, N.\* (2025) “Generative AI-Driven Mixture-of-Experts Framework using Implicit Neural Representations for Additive Manufacturing”, 대한기계학회 2025년도 학술대회
- [국내 학회] Kim, S., Han, J., Kim, S., Cho, Y., and Kang, N.\* (2025) “Manufacturing-Aware 3D Geometry Post-Processing Framework via Depth Maps for 3-Axis CNC Milling”, 대한기계학회 2025년도 학술대회
- [국내 학회] Yang, S., Lee, Y., and Kang, N.\* (2025) “Physics-Guided Multi-Fidelity DeepONet for Data-Efficient Flow Field Prediction”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Lee, S., Kang, N.\* (2025) “A Modular Design Framework for Large-Scale Design Optimization: Considering Manufacturing Cost and Performance Trade-off”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Kim, S., Yang, S., Kim, S., Han, J., Cho, B., Song, C., Kang, J., and Kang, N.\* (2025) “Spatio-Temporal Flow Field Prediction of Variable Multi-Cylinder Configurations via DeepONet”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Kwon, Y., Kang, N.\* (2025) “SAGE: Shape Augmentation with Guidance of Engineering Uncertainty”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Jeong, L., Kang, N.\* (2025) “Optimal Design of EV Cooling Channel Diffusion-Based Inpainting & Surrogate Modeling Approach”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회 (포스터)
- [국내 학회] Lee, D., Kang, N.\* (2025) “Topology Optimization Using a Foundation Model to Overcome Small Data Challenges”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Kim, J., Yang, S., and Kang, N.\* (2025) “Point-based Diffusion Model for Predicting 2D Spatio-Temporal and 3D Large-Scale Physical Systems with Shape Variations”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Kim, S., Kang, N.\* (2025) “Adaptive Multi-Fidelity Learning for Robust Time-Series Prediction”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [국내 학회] Han, J., Kim, S., Kim, S., Yang, S., Cho, B., Song, C., Kang, J., Song, M., and Kang, N.\* (2025) “Time-Series Flow Field Prediction of Multi-Cylinder using Spatio-Temporal Coordinate-based Neural Network”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회 (포스터)
- [국내 학회] Jin, S., Kang, N.\* (2025) “Preliminary Study on Deep Reinforcement Learning based Layout in 3D Space for Performance Optimization”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회 (포스터)
- [국내 학회] Park, J. and Kang, N.\* (2025) “SG-DeepONet: A Spatial Gradient-Aware Deep Operator Network for Vehicle Aerodynamic Analysis”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회 (포스터)
- [국내 학회] Shin, D., Seo, M., Kim, K., Cho, I., Lim, B., Park, S., Cho, D., Kim, J., and Kang, N.\* (2025) “Generative Design for the Cross-Section of Vehicle Battery Pack Case-to-Body Connection”, 대한기계학회 CAE 및 응용역학부문 2025년도 춘계학술대회
- [박사 학위논문] Lee, S. (2025) "A Data-Driven Framework for Mechanism Design Optimization to Meet Diverse Requirements", Ph.D. Dissertation, Department of Mechanical Engineering, KAIST.
- [박사 학위논문] Yoo, S. (2025) "Engineering-Aware Generative AI for Wheel Design: Bridging 2D Concept Generation and 3D Performance Optimization", Ph.D. Dissertation, Cho Chun Shik Graduate School of Mobility, KAIST.
- [석사 학위논문] Kim, S. (2025) “Redefining Multi-Fidelity Time-Series Data and Mixture-of-Experts-Based Predictive Modeling”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.

**2024**

- [심사 중 원고] Lee, D., Yang, S., Oh, J., Cho, S., Kim, S., and Kang, N.\* “AI-powered Digital Twin of the Ocean: Reliable Uncertainty Quantification for Real-time Wave Height Prediction with Deep Ensemble" (심사 중; arXiv 사전 공개본) · DOI: <https://doi.org/10.48550/arxiv.2412.05475>
- [심사 중 원고] Kim, J., Kwon, Y., and Kang, N.\* “Towards Mass-manufacturable Deep Generative Design: Meeting Constraints in Casting and Injection Molding”  (심사 중; arXiv 사전 공개본) · DOI: <https://doi.org/10.48550/arxiv.2403.12098>
- [국제 학술지] Lee, S. and Kang, N.\* (2024) “Vehicle Suspension Recommendation System: Multi-Fidelity Neural Network-based Mechanism Design Optimization”, Structural and Multidisciplinary Optimization, 68(3), pp.1-33 · DOI: <https://doi.org/10.1007/s00158-024-03957-x>
- [국제 학술지] Park, J. and Kang, N.\* (2024) “BMO-GNN: Bayesian Mesh Optimization for Graph Neural Networks to Enhance Engineering Performance Prediction”, Journal of Computational Design and Engineering, 11(6), pp.260-271 · DOI: <https://doi.org/10.1093/jcde/qwae102>
- [국제 학술지] Lee, S., Kim, J., and Kang, N.\* (2024) “Deep Generative Model-based Synthesis Framework of Four-bar Linkage Mechanisms with Target Conditions”, Journal of Computational Design and Engineering, 11(5), pp.318-332 · DOI: <https://doi.org/10.1093/jcde/qwae084>
- [국제 학술지] Shin, S. and Kang, N.\* (2024) “Weighted Unsupervised Domain Adaptation Considering Geometry Features and Engineering Performance of 3D Design Data”, Expert Systems with Applications, 256, 124928 · DOI: <https://doi.org/10.1016/j.eswa.2024.124928>
- [국제 학술지] Yoo, S., Lee, S., Kim, S., Kim, E, Hwangbo, H., and Kang, N.\* (2024) “ The Anxiety Consumers Feel About Using Robotaxis: HMI Design for Anxiety Factor Analysis and Anxiety Relief Based on Field Tests”, Archives of Design Research, 37(3), 47-63 · DOI: <https://doi.org/10.15187/adr.2024.07.37.3.47>
- [국제 학술지] Yang, S., Kim, H., Hong, Y., Yee, K., Maulik, R., and Kang, N.\* (2024) “Data-driven Physics-Informed Neural Networks: A Digital Twin Perspective”, Computer Methods in Applied Mechanics and Engineering, 428, 117075 · DOI: <https://doi.org/10.1016/j.cma.2024.117075>
- [국제 학회] Yang, S., Vinuesa, R., and Kang, N.\* (2024) “Mesh-agnostic Spatio-temporal Prediction of Flows using Improved Graph U-nets”, The 26th International Congress of Theoretical and Applied Mechanics 2024 (ICTAM2024).
- [국제 학회] Kim, J., Park, J., Yang, S., and Kang, N.\* (2024) “Design Optimization of Multi-layered Display Panels for Drop Impact using Physics-Constrained Graph Neural Network”, The 26th International Congress of Theoretical and Applied Mechanics 2024 (ICTAM2024).
- [국제 학회] Kim, J., Kwon, Y., and Kang, N.\* (2024) “Deep Generative Design for Manufacturing: Meeting the Design Constraints of Casting and Injection Molding”, Asian Congress of Structural and Multidisciplinary Optimization 2024 (ACSMO2024).
- [국제 학회] Park, D., Ryu, S., Lee, S., Kang, N., Kim, S., Kim, K., Choi, D., and Ahn, S. (2024) “5G Base Station Electromagnetic Field Strength Estimation Method in Complex Hotspot Area using Deep Learning”, 2024 IEEE EMC+SIPI. · DOI: <https://doi.org/10.1109/emcsipi49824.2024.10705614>
- [국내 학회] Yang, S., Wang, Y., Vishwasrao, A., Vinuesa, R., and Kang, N.\* (2024) “그래프 신경망 기반 비정상 유동 모델링을 위한 시계열 예측 방법론 개선”, 대한기계학회 2024년도 학술대회
- [국내 학회] Kim, J., Kwon, Y., and Kang, N.\* (2024) “대량생산을 위한 2차원 확산 모델 기반 3차원 설계 최적화”, 대한기계학회 2024년도 학술대회
- [국내 학회] Kim, S., Seo, M., and Kang, N.\* (2024) “암시적 신경 표현을 활용한 차량 충돌 역학의 3차원 시공간 예측”, 대한기계학회 2024년도 학술대회
- [국내 학회] Lee, D., Kim, S., Kim, J., Cho, S., and Kang, N.\* (2024) “파력발전시스템의 연간 에너지 생산량 예측 모델을 위한 베이지안 하이퍼파라미터 최적화에 대한 연구”, 대한기계학회 2024년도 학술대회 (포스터)
- [국내 학회] Kim, S., Yang, S., and Kang, N.\* (2024) “성능 저하를 방지하는 피드백 기반 멀티 피델리티 접근법의 고도화 및 최적화 연구”, 대한기계학회 2024년도 학술대회 (포스터)
- [국내 학회] Lee, S., and Kang, N.\* (2024) “최적의 차량 서스펜션 메커니즘을 위한 다중 충실도 모델 기반 설계 프레임워크”, 대한기계학회 2024년도 학술대회
- [국내 학회] Yoo, S., and Kang, N.\* (2024) “산업 디자이너 및 엔지니어를 위한 생성형 AI 기반 co-design 프레임워크”, 대한기계학회 2024년도 학술대회
- [국내 학회] Park, J. and Kang, N.\* (2024) “Latent-DeepONet을 활용한 임의의 3D 형상에 대한 비선형 정적 해석에서의 응력장 예측”, 대한기계학회 2024년도 학술대회 (포스터)
- [국내 학회] Jeong, L., Lee, Y., and Kang, N.\* (2024) “강화 학습 기반 전기차 배터리 냉각 채널 최적 설계”, 대한기계학회 2024년도 학술대회
- [국내 학회] Kim, J., Yang, S., and Kang, N.\* (2024) “2D Cylinder 유체 흐름에서의 시공간 예측 성능 비교 분석: Meshgraphnet vs Neural Implicit Representation”, 대한기계학회 2024년도 학술대회 (포스터)
- [국내 학회] Kwon, Y., Hong, S., Shin, D., Park, J., and Kang, N.\* (2024) “DeepJEB: 3D 합성 제트 엔진 브라켓 데이터셋”, 대한기계학회 2024년도 학술대회
- [국내 학회] Yoo, S and Kang, N.\* (2024) “Generative AI-based Co-design Framework for Industrial and Engineering Designers", 2024 실용인공지능학회 (AAiCON)
- [국내 학회] Yang, S., Vinuesa, R., and Kang, N.\* (2024) “그래프 신경망을 활용한 원형 실린더의 Vortex Shedding 예측”, 한국전산유체공학회 2024년도 춘계학술대회
- [국내 학회] Lee, S., Yang, S., and Kang, N.\* (2024) “매니퓰레이터 메커니즘 설계 최적화를 위한 예측 모델 활용 및 민감도 분석을 통한 설계 규칙 추출 방법론”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Yang, S., Vinuesa, R., and Kang, N.\* (2024) “격자 제약이 없는 Graph U-Nets 기반 시계열 유동장 예측”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Kim, J., Kwon, Y., and Kang, N.\* (2024) “대량생산이 가능한 딥 제너레이티브 디자인”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Kim, J., and Kang, N.\* (2024) “낙하 충돌 시 OLED 디스플레이 내구성 예측을 위한 하이퍼그래프 신경망 기반 대리 모델 개발”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Kwon, Y. and Kang, N.\* (2024) “경계 조건 조정 딥 제너레이티브 모델”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 (포스터)
- [국내 학회] Lee, D., Yang, S., Oh, J., Cho, S., Kim, S., and Kang, N.\* (2024) “파력발전시스템의 디지털 트윈을 위한 딥러닝 기반 실시간 수위 예측의 불확실성 정량화에 대한 연구”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Shin, D., Park, J., Seo, M., and Kang, N.\* (2024) “암시적 신경 표현을 활용한 3D 필드 예측과 불확실성 정량화”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회
- [국내 학회] Kim, S., and Kang, N.\* (2024) “고차 보 이론을 이용한 딥러닝 기반 차량 프레임 구조적 성능 예측”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 (포스터)
- [국내 학회] Kim, S., Yang, S., and Kang, N.\* (2024) “시계열 예측을 위한 멀티피델리티 LSTM 의 타당성 분석”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 (포스터)
- [국내 학회] Jeong, L. and Kang, N.\* (2024) “열폭주 발생 완화를 위한 전기차 언더커버 최적설계”, 대한기계학회 CAE 및 응용역학부문 2024년도 춘계학술대회 (포스터)
- [책·책 속 장] Kang, N. et al. (2024) “인류세 풍경: 우리 곁의 파국들과 희망들”, 이음.
- [책·책 속 장] Choi, H., Kang, N. et al. (2024)"AI로 친환경 제품 설계하기", 과학잡지 에피(28호), 이음.
- [석사 학위논문] Kwon, Y. (2024) “3D Deep Shape Optimization with a Limited Dataset”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.

**2023**

- [국제 학술지] Lee, U., Kang, N.\*, and Lee, Y. (2023) “Shared autonomous electric vehicle system design and optimization under dynamic battery degradation considering varying load conditions”, Journal of Cleaner Production, 423, 138795 · DOI: <https://doi.org/10.1016/j.jclepro.2023.138795>
- [국제 학술지] Lee, U., Kang, N.\*, and Lee, Y. (2023) “Optimization of module structure considering mechanical and thermal safety of pouch cell lithium-ion batteries using a reliability-based design optimization approach”, Journal of Energy Storage, 72, 108650 · DOI: <https://doi.org/10.1016/j.est.2023.108650>
- [국제 학술지] Shin, S., Shin, D., and Kang, N.\* (2023) “Topology Optimization via Machine Learning and Deep Learning: A Review", Journal of Computational Design and Engineering, 10(4), pp.1736-1766 · DOI: <https://doi.org/10.1093/jcde/qwad072>
- [국제 학술지] Lee, U. and Kang, N.\* (2023) “Adaptive Neural Network Ensemble Using Prediction Frequency", Journal of Computational Design and Engineering, 10(4), pp.1547-1560 · DOI: <https://doi.org/10.1093/jcde/qwad071>
- [국제 학술지] Shin, S., Jin, A., Yoo, S., Lee, S., Kim, C., Heo, S., and Kang, N.\* (2023) “Wheel Impact Test by Deep Learning: Prediction of Location and Magnitude of Maximum Stress", Structural and Multidisciplinary Optimization, 66, 24 · DOI: <https://doi.org/10.1007/s00158-022-03485-6>
- [국제 학회] Kang, N. (2023) “3D Deep Learning-based Generative Design: Generation, Exploration, Prediction, and Optimization”, JSME-KSME Joint Symposium on Computational Mechanics & CAE 2023.
- [국제 학회] Park, J. and Kang, N.\* (2023) “Bayesian Mesh Optimization for Graph Neural Networks to Enhance Engineering Performance Prediction”, Proceedings of the ASME 2023 International Design & Engineering Technical Conferences. · DOI: <https://doi.org/10.1115/detc2023-113308>
- [국제 학회] Lee, S., Kim, J., and Kang, N.\* (2023) “Deep Generative Model-based Synthesis of Four-bar Linkage Mechanisms Considering Both Kinematic and Dynamic Conditions”, Proceedings of the ASME 2023 International Design & Engineering Technical Conferences. · DOI: <https://doi.org/10.1115/detc2023-114464>
- [국제 학회] Kang, N. (2023) “Generative AI-powered Product Design for Manufacturing”, International Conference on Multi-scale Science and Engineering.
- [국내 학회] Lee, S., Yang, S., and Kang, N.\* (2023) “인공지능을 이용한 2-자유도 로봇 메커니즘의 최적 컨셉 설계 방법론”, 대한기계학회 2023년도 춘추학술대회
- [국내 학회] Kwon, Y. and Kang, N.\* (2023) “소량 데이터를 활용한 음함수 표현 형상 최적화”, 대한기계학회 2023년 학술대회
- [국내 학회] Kim, J., Lee, S., and Kang, N.\* (2023) “공학적 성능 및 적층 제조를 고려한 딥러닝 기반 파라메트릭 역설계”, 대한기계학회 2023년 학술대회
- [국내 학회] Shin D., Hong, S., and Kang, N.\* (2023) “심미성 향상을 위한 강화학습 기반의 제너레이티브 디자인”, 대한기계학회 2023년 학술대회
- [국내 학회] Shin S. and Kang, N.\* (2023) “3D 설계 데이터의 기하 특성과 공학 성능을 고려한 가중 비지도 도메인 적응”, 대한기계학회 2023년 학술대회
- [국내 학회] Yang, S., Kim, H., Kang, N.\*, Hong, Y., Yee, K. (2023) “2차원 유동장 예측을 위한 와류 인식 물리지식기반 신경망”, 대한기계학회 2023년 학술대회
- [국내 학회] Yoo, S. and Kang, N.\* (2023) “Stable Diffusion 기반의 컨셉 휠 디자인 프로세스: 공학적 패턴에서 실사적 렌더링까지”, 대한기계학회 2023년 학술대회
- [국내 학회] Lee, D., Oh, J., Cho, S., and Kang, N.\* (2023) “도메인 지식 기반 딥러닝을 활용한 불규칙 시계열 데이터 실시간 예측 연구: OWC-WEC 시스템 사례”, 대한기계학회 2023년 학술대회
- [국내 학회] Lee, S. and Kang, N.\* (2023) “인공지능을 이용한 2-자유도 로봇 메커니즘의 최적 컨셉 설계 방법론”, 대한기계학회 2023년 학술대회
- [국내 학회] Yoo, S., Kwon, Y., Kim, E., Shin, D., Ryu, H., Lee, S., Lim, B., Jang, J., Cho, I., Hong, S., and Kang, N.\* (2023) “3D 딥러닝 기반의 제너레이티브 디자인: 잠재공간에서 수행하는 생성, 탐색, 예측 및 최적화”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회
- [국내 학회] Kim, J. and Kang, N.\* (2023) “절점-요소 하이퍼그래프 기반 그래프 신경망을 통한 충격 해석”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회
- [국내 학회] Park, J., Kim, J., Yu, Y., Kim, N., Ha, S., Chang, K., and Kang, N.\* (2023) “디스플레이 패널 구조 최적화를 위한 그래프 신경망 기반 충격해석에 관한 연구”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회
- [국내 학회] Kim, J., Lee, S., and Kang, N.\* (2023) “동역학 조건을 고려한 딥러닝 기반 4 절링크 메커니즘 설계”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회
- [국내 학회] Lee, S., Kim, S., and Kang, N.\* (2023) “딥 제너레이티브 디자인을 이용한 다축 로봇 링크 생성”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회
- [국내 학회] Kwon, Y. and Kang, N.\* (2023) “음함수 표현을 활용한 3D 형상 최적화”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회 (포스터)
- [국내 학회] Lee, D., Oh, J., Kim, K., Cho, S., and Kang, N.\* (2023) “LSTM 을 이용한 진동수주형 파력발전장치 수주높이 실시간 예측연구”, 대한기계학회 CAE 및 응용역학부문 2023년도 춘계학술대회 (포스터)
- [국내 학회] Kim, S., Lee, S., and Kang, N.\* (2023) “딥러닝을 사용한 다축로봇 역설계”, 2023 실용인공지능학회 (AAiCON)
- [국내 학회] Lee, S., Kim, J., Kim, S., Jin, A., Shin, S., Shin, D., Kwon, Y., and Kang, N.\* (2023) “제너레이티브 디자인을 통한 3D 데이터 생성”, 2023 한국CDE학회
- [책·책 속 장] Kim, Y. T., Kang, N. et al. (2023) "문제를 푸는 사람들: KAIST 혁신기업 창업사", KAIST.
- [석사 학위논문] Shin, S. (2023) “Weighted Unsupervised Domain Adaptation Considering Geometry Feature and Engineering Performance of 3D Design Data”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.
- [석사 학위논문] Kim, J. (2023) “Impact Analysis with Node-Element Hypergraph-based Graph Neural Networks”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.
- [석사 학위논문] Shin, D. (2023) “Learning Design Preferences through Design Feature Extraction and Weighted Ensemble”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.
- [석사 학위논문] Park, J. (2023) “Bayesian Mesh Optimization for Graph Neural Networks to Enhance Engineering Performance Prediction”, M.S. Thesis, Cho Chun Shik Graduate School of Mobility, KAIST.

**2022**

- [국제 학술지] Kim, S., Jwa, M., Lee, S., Park, S., and Kang, N.\* (2022) “Deep Learning-Based Inverse Design for Engineering Systems: Multidisciplinary Design Optimization of Automotive Brakes", Structural and Multidisciplinary Optimization, 65, 323 · DOI: <https://doi.org/10.1007/s00158-022-03386-8>
- [국제 학술지] Lee, Y., Lee, U., and Kang, N.\* (2022) “Multiscale Design Optimization of Electric Vehicles by Analytical Target Cascading: From Battery Cell Level to Marketing Level", Journal of Cleaner Production, 368, 133235 · DOI: <https://doi.org/10.1016/j.jclepro.2022.133235>
- [국제 학술지] Kim, E., Ryu, H., Oh, H., and Kang, N.\* (2022) “Safety Monitoring System of Personal Mobility Driving Using Deep Learning", Journal of Computational Design and Engineering, 9, 1397–1409 · DOI: <https://doi.org/10.1093/jcde/qwac061>
- [국제 학술지] Jang, S., Yoo, S., and Kang, N.\* (2022) “Generative Design by Reinforcement Learning: Enhancing the Diversity of Topology Optimization Designs", Computer-Aided Design, 146, 103225 · DOI: <https://doi.org/10.1016/j.cad.2022.103225>
- [국제 학술지] Kim, S., Lee, U., Lee, I., and Kang, N.\* (2022) “Idle Vehicle Relocation Strategy through Deep Learning for Shared Autonomous Electric Vehicle System Optimization", Journal of Cleaner Production, 333, 130055 · DOI: <https://doi.org/10.1016/j.jclepro.2021.130055>
- [국내 학술지] Yoo, S., Lee, S., Kim, E., and Kang, N.\* (2022) “가상 제품 개발과 메타버스를 위한 3D 합성 데이터 생성”, 기계저널, 62(11), pp.32-37.
- [국내 학술지] Shin, D., Kwon, Y., and Kang, N.\* (2022) “인공지능 기반 모빌리티 설계: Deep Generative Design”, 정보과학회지, 40(6), pp. 25-34.
- [국제 학회] Lee, U., Lee, Y., and Kang, N.\* (2022) “Multiscale Design Optimization of Electric Vehicles by Analytical Target Cascading: From Battery Cell Level to Marketing Level”, Asian Congress of Structural and Multidisciplinary Optimization 2022 (ACSMO2022).
- [국제 학회] Lee, G., Kang, N., and Lee, J. (2022) “Human Driver’s Reasoning on Moral Dilemma of Autonomous Vehicles: Values and Themes”, 5th International Conference on Intelligent Human Systems Integration (IHSI 2022). · DOI: <https://doi.org/10.54941/ahfe1001053>
- [국내 학회] Yoo, S., Shin, D., Park, U., Yang, U., and Kang, N.\* (2022) "전기자동차의 통합열관리 시스템을 위한 물리 기반 인공신경망", 2022 한국자동차공학회 추계학술대회
- [국내 학회] Park, J. and Kang, N.\* (2022) "그래프 신경망을 위한 베이지안 메쉬 최적화", 대한기계학회 2022년 학술대회
- [국내 학회] Shin, S., Jwa, M., Kwon, Y., Nam, Y., and Kang, N.\* (2022) "머신러닝 기반 스몰오버랩 충돌에 대한 차량 거동 예측", 대한기계학회 2022년 학술대회
- [국내 학회] Kwon, Y., Shin, S., and Kang, N.\* (2022) "공학 성능을 고려한 SDF 기반 잠재공간 임베딩", 대한기계학회 2022년 학술대회 (우수논문상)
- [국내 학회] Shin, D., Lee, S., and Kang, N.\* (2022) "디자인 특징 추출을 통한 딥러닝 기반 디자인 선호도 예측", 대한기계학회 2022년 학술대회
- [국내 학회] Kim, J., Lee, U., Kwon, Y., and Kang, N.\* (2022) "화공 플랜트를 위한 대규모 배치 최적화", 대한기계학회 2022년 학술대회
- [국내 학회] Lee, S., Kim, S., and Kang, N.\* (2022) "다물체 동역학 조건을 고려한 다축 로봇 프레임 제너레이티브 디자인", 대한기계학회 2022년 학술대회 (포스터)
- [국내 학회] Kim, S., Lee, S., and Kang, N.\* (2022) "높은 토크 전달력을 이용한 4절 링크 로봇 팔 설계", 대한기계학회 2022년 학술대회 (포스터)
- [국내 학회] Lee, J., Jang, S., Jin, A., and Kang, N.\* (2022) "차량 리어 스포일러를 위한 딥러닝 기반 제너레이티브 디자인", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터) (학생경진대회 금상)
- [국내 학회] Park, J., Shin, D., Yoo, S., and Kang, N.\* (2022) "그래프 신경망을 이용한 3D 휠 성능 예측 기초 연구", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터) (학생경진대회 은상)
- [국내 학회] Lee, U. and Kang, N.\* (2022) "Statistical Ensemble Method for Artificial Neural Network", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회
- [국내 학회] Jin, A., Shin, S., Yoo, S., Kim, J., and Kang, N.\* (2022) “비지도학습을 통한 TV 스탠드 역설계", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회
- [국내 학회] Jwa, M., Shin, S., Shin, D., Jin, A., and Kang, N.\* (2022) “딥러닝 기반 역설계 기법의 성능 분석", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회
- [국내 학회] Lee, Y., Lee, U., and Kang, N.\* (2022) "전기 자동차의 다중 스케일 설계 최적화 연구", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회
- [국내 학회] Hong, S. and Kang, N.\* (2022) " 심층강화학습을 통한 위상최적화", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터)
- [국내 학회] Jang, S., Jin, A., and Kang, N.\* (2022) "파라메트릭 휠 디자인을 위한 딥러닝 기반 역설계", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터) (우수논문상)
- [국내 학회] Kwon, Y., Yoo, S., and Kang, N.\* (2022) "도메인 적응을 이용한 상세 설계 휠의 강성 예측 연구", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터)
- [국내 학회] Shin S., Kwon, Y., and Kang, N.\* (2022) "SDF 기반 3D 제너레이티브 디자인 기초연구", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터)
- [국내 학회] Kim, S., Kang, N.\* (2022) “조건적 생성 모델을 통한 차량 브레이크 시스템 역설계", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터)
- [국내 학회] Kim, J., Lee, U., Jwa, M., and Kang, N.\* (2022) "머신러닝 기반 차량충돌성능 예측과 민감도 분석", 대한기계학회 CAE 및 응용역학부문 2022년도 춘계학술대회 (포스터)
- [국내 학회] Jin, A., Shin, S., Yoo, S., Kim, J., Myung, J., Hong, C., Han, I., Cho, G., Kim, S., and Kang, N.\* (2022) “TV 스탠드를 위한 딥러닝 기반 제너레이티브 디자인 프로세스", 한국CDE학회 2022년도 동계학술대회
- [석사 학위논문] Jin, A. (2022) “구조설계최적화를 위한 딥러닝 기반 역설계: TV 스탠드 경량화 설계 사례 연구”, M.S. Thesis, Department of Mechanical Systems Engineering, Sookmyung Women’s University.
- [석사 학위논문] Jwa, M. (2022) “최적설계와 딥러닝 기반 역설계의 성능 비교”, M.S. Thesis, Department of Mechanical Systems Engineering, Sookmyung Women’s University.

**2021**

- [국제 학술지] Lee, K. J., Kang, N.\*, Kokkolaras, M., and Papalambros, P. Y. (2021) “Design Optimization of a Hybrid Electric Vehicle Cooling System Considering Performance and Packaging”, International Journal of Vehicle Design, 85(2/3/4), pp. 154-177 · DOI: <https://doi.org/10.1504/ijvd.2021.120422>
- [국제 학회] Kim, S., Jwa, M., Lee, S., Park, S, and Kang, N.\* (2021) “Multidisciplinary Inverse Design using Deep Learning: a Case Study of Brake Systems”, Asia Pacific Conference on Prognostics and Health Management Society 2021 (PHMAP21) (Best Student Award).
- [국제 학회] Kim, E. Ryu, H., Oh, H., and Kang, N.\* (2021) “Personal Mobility Driving Safety Monitoring System Using Deep Learning”, Asia Pacific Conference on Prognostics and Health Management Society 2021 (PHMAP21).
- [국제 학회] Shin, D., Yoo, S., Lee, S., Kim, M., Hwang K.H., Park, J.H., and Kang, N.\* (2021) “How to Trade off Aesthetics and Performance in Generative Design?”, The 2021 World Congress on Advances in Structural Engineering and Mechanics (ASEM21).
- [국제 학회] Shin, S., Shin, D., Kim, M., Ryu, H., and Kang, N.\* (2021) “Machine Learning-based Topology Optimization: A Review”, The 2021 World Congress on Advances in Structural Engineering and Mechanics (ASEM21).
- [국내 학회] Kim, S., Kang, N.\* (2021) “Inverse Design of Automotive Brakes Using Generative Models", 2021년 한국전산구조공학회 학술심포지엄
- [국내 학회] Jin, A., Lee, S., Yoo, S., Shin, S., Kim, C., Heo, S., and Kang, N.\* (2021) “딥러닝 기반의 최대응력과 위치 예측 기법: 로드 휠 충격 테스트 예시", 대한기계학회 CAE 및 응용역학부문 2021년도 춘계학술대회 (우수학생발표상)
- [국내 학회] Jwa, M., Jin, A., Shin, D., Shin, S., and Kang, N.\* (2021) “딥러닝 기반 역설계와 최적 설계의 비교", 대한기계학회 CAE 및 응용역학부문 2021년도 춘계학술대회 (포스터) (우수포스터논문상)
- [국내 학회] Kim, S., Kang, N.\* (2021) “비지도학습을 이용한 브레이크 시스템 역설계", 대한기계학회 CAE 및 응용역학부문 2021년도 춘계학술대회 (포스터)
- [국내 학회] Jwa, M., Lee, G., Kim, E., Ryu, H., Seo, W., Lee, K., and Kang, N.\* (2021) “인공신경망을 이용한 NCAP 지수의 설계 민감도 분석”, 대한기계학회 IT융합부문 2021년도 춘계학술대회
- [박사 학위논문] Kim, S. (2021) "Deep Learning-based Mobility Design: Shared Autonomous Electric Vehicle System and Vehicle Brake System Optimization", Ph.D. Dissertation, Department of Mechanical Systems Engineering, Sookmyung Women’s University.
- [석사 학위논문] Kim, E. (2021) “딥러닝을 활용한 퍼스널 모빌리티 주행 안전도 모니터링 시스템”, M.S. Thesis, Department of Mechanical Systems Engineering, Sookmyung Women’s University.
- [석사 학위논문] Lee, S. (2021) “딥러닝 기반 디자인 선호도 예측 및 추천시스템: 자동차 휠 설계 사례”, M.S. Thesis, Department of Mechanical Systems Engineering, Sookmyung Women’s University.

## 연구 과제

RESEARCH_PROJECTS의 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제 38건이다. 지원 기관, 과제명, 기간과 역할은 게시 표기다. 연구책임자는 PI(Principal Investigator)로 표시되어 있다. 이 목록에는 강남우 교수가 숙명여자대학교에 재직하던 때 시작한 과제도 포함한다.[^projects][^prof]

- 삼성중공업, "슬로싱 국부 하중 초기 추정법 개발", 2026.4-2026.12 (PI)
- 삼성중공업, "실적기반 엔진룸 장비 배치 알고리즘 개발", 2026.4-2026.8 (PI)
- 현대자동차 & 팜테크 & 나니아랩스, "인공지능을 활용한 하이드로 부싱 필드 거동 특성 분석", 2026.8-2026.10 (PI)
- 현대자동차 & 나니아랩스, "인공지능을 활용한 IPMSM 전자계해석 모델 생성 및 성능 예측", 2025.7-2026.6 (PI)
- 한국수자력원자력(K-CLOUD), "생성형 AI 기반의 대형원전 개념개발 플랫폼 개발", 2026.3-2028.2 (PI)
- 연구개발특구진흥재단, "AI 글로벌 빅테크 육성 사업", 2025.8-2027.12 (PI)
- 과학기술정보통신부(글로벌 TOP 전략연구단), "SMR 가상원자로 플랫폼 개발 연구단", 2024.5-2029.5 (PI)
- 과학기술정보통신부, "인공지능 기반 기지국 전자파 인체노출량 예측 알고리즘 개발", 2022.4-2026.12 (참여연구원)
- 국토교통과학기술진흥원, "국토교통 DNA플러스 도로교통분야 융합기술대학원", 2021-2027 (참여연구원)
- 현대자동차, "차량 개발의 신속성 확보 위한 생성형 AI와 Parametric Design 연계한 클로저 시스템 설계 방법론 연구", 2025.6-2026.6 (PI)
- 현대자동차, "이상치 탐지 모델을 활용한 고장 예측 알고리즘 개발", 2024.3-2025.3 (PI)
- 현대자동차, "차체시스템 산학 자문단 운영", 2024.7-2024.11 (기술자문)
- 현대자동차, "연구개발본부 AI 경진대회", 2023.6-2023.10 (기술자문)
- 현대자동차, "로드휠의 형상 제시를 위한 디자인 생성 가이드라인과 AI 기반 분류 기법 개발", 2021.7-2022.6 (PI)
- 현대자동차, "연구개발본부 AI 경진대회", 2022.7-2022.9 (기술자문)
- 현대자동차, "통합열관리제어로직 개발에 사용될 학습기반 에어컨 PLANT/CONTROL 모델 구축 기법 개발", 2021.6-2022.5 (PI)
- 현대자동차, "AI 연계 스몰오버랩 충돌 대응 차량 거동 성능 지표 추출 및 휠 설계 기법 연구", 2021.5-2022.5 (PI)
- 포스코, "스타일드휠 디자인 개선을 위한 성형성 기반의 자율모델링 방법론 연구", 2023.3-2023.12 (PI)
- LG디스플레이, "GENERATIVE DESIGN과 MESHGRAPHNET을 활용한 패널 적층 구조 최적화 요소 기술 개발", 2022.5-2023.2 (PI)
- LG 전자, "TV 설계자동화 : AI GENERATIVE DESIGN 기반 설계자동화", 2021.3-2021.12 (PI)
- DLE&C, "GENERATIVE DESIGN 기술을 활용한 기기배치 자동화 개발(알고리즘 개발)", 2021.5-2022.10 (PI)
- 삼성중공업 & 서울컨설턴츠, “AI에 기반한 Flare Tower 설계 자동화 프로그램 개발”, 2024.7-2024.12 (PI)
- 과학기술정보통신부, "대량의 공학적 최적 설계안 자동생성을 위한 인공지능 기반 제너레이티브 디자인 기술 및 생산연계 기술 개발", 2022.4-2025.12 (PI)
- 산업통상자원부(알키미스트), "아이디어를 현실로 만드는 Generative Manufacturing 기술개발", 2024.4-2025.12 (PI)
- 한국연구재단(선도연구센터), "인류세 연구센터", 2018.6-2025.2 (핵심연구원)
- 한국연구재단(세종과학펠로우십), "디지털 트윈 환경에서의 범용성 및 사용자 친화성이 고려된 AI 기반 유동 예측 프레임워크 구축", 2024.5-2029.4 (양선웅 박사후연구원)
- 선박해양플랜트연구소, "AI 기반 해양 재생에너지 발전량 예측 요소기술 개발", 2023.3-2025.9 (PI)
- 선박해양플랜트연구소, "진동수주형 파력발전시스템의 수주실 수위 예측을 위한 인공지능 모델 개선", 2023.3-2023.7 (PI)
- 한국지능정보사회진흥원(NIA), "인공지능 학습용 데이터 구축 사업: 3D 에셋-이미지 쌍 데이터", 2022.6-2023.1 (PI)
- 한국연구재단(신진연구), "공유경제를 통한 친환경 교통시스템의 혁신: 전기차 및 충전소 공유시스템의 최적 디자인 프레임워크 개발", 2017.3-2022.2 (PI)
- 중소벤처기업부 & 메드올스, "식약처 의료기기 정보DB와 결합된 의료기기 포탈과 정보제공 온라인 매거진 개발", 2020.8-2022.8 (PI)
- KAIST, "인공지능 기반 모빌리티 설계", 2021.5-2024.12 (PI)
- KAIST, "생성형 AI를 이용한 매니퓰레이터의 실시간 최적설계 프레임워크", 2023.7-2023.12 (PI)
- KAIST, "노후된 E-모빌리티 업사이클링 생태계 조성을 위한 핵심 기술 개발", 2022.1-2022.12 (참여연구원)
- KAIST, "KAIST 캠퍼스 교통 흐름 및 주차 공간 분석", 2022.5-2022.10 (PI)
- KAIST, "딥러닝 기반 제너레이티브 디자인을 이용한 다축 로봇 링크의 실시간 최적 설계", 2022.8-2022.12 (PI)
- KAIST, "제조업의 AI/DX 적용을 위한 3D DATA & AI SOLUTION", 2022.6-2022.9 (PI)
- KAIST, "AI 기반 CAE 및 최적설계를 위한 클라우드서비스 개발", 2021.8-2021.12 (PI)

## 수상과 선정

AWARDS에 게시된 2021년 11월 11일–2026년 10월 2일의 수상·선정 45건이다. 날짜는 게시일이며, 수상 학술대회 연도가 게시 연도와 다른 경우가 있다. 이 목록에는 교수 개인의 수상과 연구실 구성원·분사 기업의 수상·선정이 함께 있다.[^awards]

- 2026-10-02 · 우수 학생연구상 - 권용민
- 2026-09-07 · IPESK 차세대 공학연구자 (3기) 선정 - 권용민
- 2026-09-07 · IPESK 차세대 공학연구자 (3기) 선정 - 박장섭
- 2026-08-31 · 석사과정생연구장려금지원사업 선정 - 나진수
- 2026-05-20 · Best Student Paper Award - 정이교
- 2026-05-07 · 학생경진대회 동상 - 권용민
- 2026-05-07 · 우수논문상 - 김지용
- 2026-05-07 · 우수논문상 - 신동주
- 2026-03-31 · 한국수력원자력 K-CLOUD 연구기관 선정 - 스마트설계연구실
- 2026-01-14 · 한국최적설계학회 우수학위논문상(박사) - 이수민
- 2025-12-31 · Outstanding Service Award - 강남우 교수
- 2025-12-24 · 산업부 장관상 수상 - 강남우 교수
- 2025-12-12 · 대한기계학회 조인트 세션 강연 감사장 - 강남우 교수
- 2025-12-11 · 대한기계학회 전문가리뷰 세션 강연 감사장 - 강남우 교수
- 2025-08-28 · 석사과정생연구장려금지원사업 선정 - 장원재
- 2025-07-04 · 우수논문상 - 김상혁
- 2025-04-30 · KAIST 미래선도기술 대표연구성과 선정 - 강남우 교수
- 2025-04-17 · 2025 년 대한기계학회 CAE 및 응용역학부문 감사패
- 2025-04-18 · 학생경진대회 은상 - 이동언
- 2025-04-17 · 우수논문상 - 이수민
- 2024-10-18 · KAIST 기계공학과 우수조교상 - 이수민
- 2024-10-11 · KAIST 조천식모빌리티대학원 공로상 - 김지용
- 2024-09-27 · 삼성전자 MX사업부 연구장학생 선정 - 이수민
- 2024-08-21 · KAIST 조천식모빌리티대학원 감사패 - 강남우 교수
- 2024-06-28 · 우수논문상 - 유소영
- 2024-05-20 · 세종펠로우십 선정 - 양선웅
- 2024-05-02 · 2024년 대한기계학회 CAE 및 응용역학부문 감사패
- 2024-05-02 · 우수논문상 - 양선웅
- 2024-02-26 · 우수박사학위논문상 - 양선웅
- 2024-02-02 · Readers' Choice Award - 강남우 교수
- 2023-11-28 · 2023 KAIST Q-DAY 특별포상 수상자 선정 - 유소영
- 2023-11-02 · KSME-SEMES 오픈 이노베이션 챌린지 장려상 - 이수민 & 김지훈
- 2023-10-26 · 나니아랩스 코리아 AI 스타트업 선정
- 2023-05-18 · 우수논문상 - 장승헌 & 진아현
- 2023-05-18 · 우수논문상 - 권용민 & 신승연
- 2023-03-24 · Outstanding Contribution Award - 강남우 교수
- 2023-01-31 · 제조첨단화 및 지능화 도전과제 최우수상 - 이수민 & 김승규
- 2022-10-14 · K-테크 스타트업 왕중왕전 대상 수상
- 2022-05-19 · 대한기계학회 CAE 및 응용역학부문 젊은연구자상 - 강남우 교수
- 2022-05-19 · 2022 대한기계학회 CAE 및 응용역학부문 우수학생발표상 - 진아현
- 2022-05-19 · 2022 대한기계학회 CAE 및 응용역학부문 우수포스터논문 - 좌민영
- 2022-05-19 · 2022 대한기계학회 우수학위논문상 - 이웅기
- 2022-05-19 · 2022 대한기계학회 CAE 및 응용역학부문 학생경진대회 은상 - 박장섭
- 2022-05-19 · 2022 대한기계학회 CAE 및 응용역학부문 학생경진대회 금상 - 이정훈
- 2021-11-11 · 스마트설계연구실 KAIST E\*5 LAB STARTUP 1위

## 소식

연구실 NEWS의 2023년 4월과 2024년 10월 연구·사업화 소식이다. 날짜는 게시 연월이다.[^news2023][^news2024]

- 2024-10 · KAIST 공과대학 뉴스레터에 이수민의 인공지능 기반 기계 기구 메커니즘 설계 자동화 기술 개발이 소개되었다.
- 2023-04 · 연구실에서 분사한 나니아랩스가 생성 인공지능 기술로 프리-A 투자를 유치했다.

## 연락과 위치

- 교수 이메일: nwkang@kaist.ac.kr[^prof][^contact]
- 교수 소개의 사무실: N7-4 건물 7108호, 전화 +82-42-350-3037[^prof]
- CONTACT의 연구실: F431, 사무실 F432, 전화 +82-42-350-1269[^contact]
- CONTACT의 주소: KAIST, 193 Munji-ro, Jeonmin-dong, Yuseong-gu, Daejeon, 34051, Korea[^contact]
[^p1]: D. Shin, S. Lee, N. Kang, Journal of Computational Design and Engineering (2026). <https://doi.org/10.1093/jcde/qwag029> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^p2]: S. Yang, R. Vinuesa, N. Kang, Journal of Computational Design and Engineering (2025). <https://doi.org/10.1093/jcde/qwaf099> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^p3]: S. Lee, N. Kang, International Journal of Precision Engineering and Manufacturing-Green Technology (2025). <https://doi.org/10.1007/s40684-025-00770-9> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^p4]: J. Park, N. Kang, Journal of Computational Design and Engineering (2024). <https://doi.org/10.1093/jcde/qwae102> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^p5]: S. Lee, J. Kim, N. Kang, Journal of Computational Design and Engineering (2024). <https://doi.org/10.1093/jcde/qwae084> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^p6]: U. Lee, N. Kang, Journal of Computational Design and Engineering (2023). <https://doi.org/10.1093/jcde/qwad071> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026>. 관측 2026-11-07.

[^research]: RESEARCH_TOPICS. <https://www.smartdesignlab.org/research/research_topics> 관측 2026-11-07.

[^prof]: PROFESSOR. <https://www.smartdesignlab.org/people/professor> 관측 2026-11-07.

[^members]: RESEARCHERS. <https://www.smartdesignlab.org/people/researchers> 관측 2026-11-07.

[^alumni]: ALUMNI. <https://www.smartdesignlab.org/people/alumni> 관측 2026-11-07.

[^pubs]: PUBLICATIONS. <https://www.smartdesignlab.org/publications> 관측 2026-11-07.

[^projects]: RESEARCH_PROJECTS. <https://www.smartdesignlab.org/research/research_projects> 관측 2026-11-07.

[^awards]: AWARDS. <https://www.smartdesignlab.org/news/awards> 관측 2026-11-07.

[^news2023]: NEWS 2023. <https://www.smartdesignlab.org/news/news_2023> 관측 2026-11-07.

[^news2024]: NEWS 2024. <https://www.smartdesignlab.org/news/news_2024> 관측 2026-11-07.

[^contact]: CONTACT. <https://www.smartdesignlab.org/contact> 관측 2026-11-07.

[^oa]: OpenAlex Namwoo Kang의 2021–2026년 출판 기록. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026> 관측 2026-11-07.

[^ocean]: AI-powered Digital Twin of the Ocean, arXiv:2412.05475. <https://arxiv.org/abs/2412.05475> 관측 2026-11-07.

[^appointment]: OpenAlex의 2021년 논문 저자 소속과 출판일. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5016809344,publication_year:2021-2026> 관측 2026-11-07. DOI 10.1007/s00158-021-02953-9의 publication_date는 2021-06-14이며, Namwoo Kang의 저자 소속은 The Cho Chun Shik Graduate School of Green Transportation, Korea Advanced Institute of Science and Technology로 적혀 있다.

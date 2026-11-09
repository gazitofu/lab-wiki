# 임베디드 인공지능 연구실 (KAIST Embedded AI Lab)

**KAIST 전기및전자공학부 · 이슬기 부교수**

- 분야: 기기 내부 인공지능, 메모리 효율적 학습, 인공지능 실행 소프트웨어, 기기와 물리 환경의 상호작용
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 엣지 컴퓨팅·엣지 AI[^statement], AI 시스템·인프라[^statement], 실시간·임베디드 시스템[^statement], 프로그래밍 언어·컴파일러[^statement][^research], 멀티모달 AI[^statement], 연속학습[^statement]
- 홈페이지: <https://sites.google.com/view/embeddedai>
- 근거와 출처: [임베디드 인공지능 연구실 근거 페이지](embeddedai-sources.md)

> 계산 능력과 저장 공간, 에너지와 통신에 제약이 있는 기기에서 인공지능이 배우고 판단하고 행동하도록, 학습 모형과 실행 시스템을 함께 연구하는 연구실이다.[^statement]

## 무엇을 연구하나

AI(Artificial Intelligence, 인공지능)를 로봇·휴대전화·가전제품처럼 실제 환경과 상호작용하는 기기 안에서 실행하는 것이 중심 목표다. 이런 임베디드 시스템(다른 기기 안에 들어가 특정 기능을 수행하는 계산 시스템)은 계산 능력뿐 아니라 메모리(프로그램과 자료를 보관하고 접근하는 저장 공간), 에너지, 통신 연결에도 제약이 있다. 연구실은 기기에서 관측한 정보로 행동을 선택하고 그 결과를 살펴 다시 적응하는 과정을, 학습 모형과 계산 실행 구조를 함께 설계하는 문제로 다룬다.[^statement]

한 갈래는 기기에서 학습과 추론(학습된 모형으로 새 입력의 출력을 계산하는 과정)을 수행할 실행 소프트웨어다. 여러 프로그램에 자원을 배분하는 운영체제, 실행 중 계산을 관리하는 런타임, 프로그램을 다른 언어나 기계 명령으로 바꾸는 컴파일러를 연구한다. 종류가 다른 기기 하드웨어에서도 인공지능이 효율적이고 안정적으로 실행되도록 하는 것이 목적이다. 정해진 시간 조건에 맞춰 결과를 내는 실시간 실행도 다룬다.[^statement][^research] 2026년 AISTATS 논문 ECAI(Efficient Convolution Activation Inversion)는 학습 중 필요한 중간 계산값을 계속 저장하는 대신 다시 복원해, 신경망(연결된 계산 단위 사이의 가중치로 입력을 출력으로 바꾸는 계산 모형)의 학습 메모리를 줄이는 방법을 제안했다.[^p1]

다른 갈래는 기기의 자원 제약에 맞춘 기반 모형(폭넓은 자료로 미리 학습해 여러 후속 작업에 맞춰 사용하는 모형)과 에이전트(주변 정보와 목표에 따라 행동을 선택하고 수행하는 시스템)다. 영상·소리·글처럼 종류가 다른 정보를 함께 다루는 멀티모달 모형을 기기에서 실행하도록 설계한다. 경험을 저장하고 필요한 지식을 꺼내는 기억 구조, 개인에 맞춘 적응, 새 자료를 배우면서 기존 능력을 유지하는 연속학습도 연구한다. 장기적으로는 여러 기기가 지식과 계산을 나누고 행동을 조율하는 방향을 제시한다.[^statement]

학습 대상에는 시계열(시간 순서대로 기록한 자료)도 있다. OliO는 자료 자체에서 학습 목표를 만드는 자기지도학습으로 시간의 앞뒤 변화를 배우고, 미래를 예측하는 데 필요한 자료의 표현을 구성한다.[^p4] 물리 환경에서의 응용으로는 달 표면의 충돌구를 찾는 LunarDet이 있다. 학부 연구성과 소개는 이 방법이 제한된 계산·에너지 자원에서 동작하도록 설계됐고, 지식 증류(다른 모형의 출력을 학습 정보로 삼아 대상 모형을 가르치는 방법)를 이용해 계산량·추론 지연·에너지 소비를 줄였다고 설명한다.[^crater]

## 주요 연구 주제

### 기기에서 배우고 실행하는 인공지능

학습 알고리즘과 실행 구조를 함께 바꿔 기기의 저장 공간과 계산 자원에 맞춘다. 가전제품의 통신 모뎀(통신 규격에 맞게 자료와 신호를 변환해 주고받는 장치)에서 신경망을 학습시키는 연구와, 합성곱(이웃한 자료값에 같은 계산 규칙을 적용해 특징을 뽑는 연산) 신경망의 중간 계산값을 복원하는 연구가 이 갈래에 해당한다.[^p1][^p2]

### 기기 내부의 영상 생성

영상·이미지·언어 모형을 임베디드 기기에서 실행하는 방법을 다룬다.[^research] MOVD는 이미 학습된 영상 생성 모형에 계산 단계를 줄이는 방법과 시간 방향의 자료 단위를 합치는 방법을 적용해, 휴대전화급 하드웨어에서 문장으로 영상을 생성하도록 했다.[^p3]

### 시간에 따른 변화와 기기 적응

시계열의 앞뒤 변화 관계를 배우는 학습 방법을 연구한다.[^p4] 현재 연구 방향은 기기에서 경험을 기억하고 검색하며, 자원과 주변 환경이 바뀌어도 기존 능력을 유지하면서 새 자료에 적응하는 학습 시스템으로 이어진다.[^statement]

### 물리 환경과 상호작용하는 시스템

센서(물리량이나 상태를 측정 가능한 신호로 바꾸는 장치)의 관측, 기억, 계산 실행과 행동을 함께 조율하는 시스템을 연구한다. 로봇·착용형 기기·차량·주변 상황에 적응하는 기계에서 제때 판단하고 동작하는 것이 목표다.[^statement]

## 대표 논문

KAIST 재직 시기인 2026년에 출판·발표되었거나 학회에 채택된 논문에서 학습 메모리, 가전제품, 영상 생성, 시계열 예측을 골랐다. 이슬기 교수는 2026년 2월 4일 KAIST에 부임했다. 출판·발표 시기는 연구를 시작한 기관을 뜻하지 않는다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. OliO는 NeurIPS 2026 채택 논문이며 설명은 arXiv 사전 공개본 기준이다.[^appointment][^pubs][^p4]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [ECAI: Efficient Convolution Activation Inversion for Constant-Memory Convolutional Neural Networks Training](https://proceedings.mlr.press/v300/lee26c.html) · AISTATS | 신경망을 학습할 때 앞선 계산의 중간값을 저장해 두면 층이 늘면서 필요한 메모리가 커진다. ECAI는 합성곱 계산에서 필요한 중간값을 복원해 같은 저장 공간을 다시 쓴다. 실험에서는 모형 정확도를 떨어뜨리지 않으면서 중간값 저장 공간을 일정하게 유지했다고 보고했다.[^p1] | 1저자 Changhyeon Lee, 마지막 저자 Seulki Lee |
| 2 | 2026 | [Beyond Communication: On-Modem DNN Inference and Training for Home Appliances](https://doi.org/10.1109/percom67906.2026.11524490) · PerCom | 가전제품에 이미 들어 있는 통신 모뎀의 쓰이지 않거나 적게 쓰이는 계산 자원으로 신경망의 추론과 학습을 수행하는 방법이다. 모뎀에 맞춘 실행·학습 구조를 제안하고, 실제 LG전자 세탁기에서 남은 세탁 시간 예측과 불균형 오류 예측을 구현했다.[^p2] | 1저자 Insung Jung, 마지막 저자 Seulki Lee |
| 3 | 2026 | [Mobile-Oriented Video Diffusion: Enabling Text-to-Video Generation on Mobile Devices Without Retraining, Compression, or Pruning](https://doi.org/10.1109/wacv61042.2026.00386) · WACV | 문장으로 영상을 만드는 확산 모형은 잡음을 지우는 계산을 반복한다. MOVD는 이 계산 단계를 줄이고, 시간상 연속한 자료 단위를 합쳐 계산 부담을 줄인다. 큰 모형을 실행 가능한 부분으로 나눠 불러오는 방법도 결합해, 대상 모형을 다시 학습하거나 압축하거나 일부를 제거하지 않고 iPhone 15 Pro에서 실행했다.[^p3] | 1저자 Bosung Kim·Kyuhwan Lee(공동 기여), 마지막 저자 Seulki Lee |
| 4 | 2026 | [OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting](https://doi.org/10.48550/arXiv.2610.23345) · arXiv, NeurIPS 2026 채택 | 시간 간격의 차이를 잡음으로 취급하거나 자료 일부를 가리면 예측에 필요한 시간 변화 관계를 잃을 수 있다. OliO는 시간 이동에 따른 앞뒤 변화를 연속적인 체계로 배우고, 시간 이동량이 다른 자료의 내부 표현을 맞춘다. 계산 구조에 제약을 두어 수치적 안정성을 확보하고 장기 의존 관계를 담도록 설계했다. 여러 예측 모형과 평가 자료에서 예측 성능 향상을 보고했다.[^p4] | 1저자 Kwangryeol Park, 교신저자 Seulki Lee |

## 교수와 전문 분야

이슬기 교수는 2021년 University of North Carolina at Chapel Hill에서 컴퓨터과학 박사학위를 받았다. UNIST에서 2021년 8월–2025년 8월 조교수, 2025년 9월–2026년 2월 부교수로 재직했고, 2026년 2월 4일 KAIST 전기및전자공학부에 부임했다. 학부 전임교수 목록은 AI시스템학과를 겸임학과로 적는다.[^appointment][^deptlist]

학부 소개에 적힌 전문 분야는 임베디드 시스템, 기기 내부 인공지능, 기계학습, 모바일·감지 시스템과 실시간 계산이다.[^dept] 논문으로는 중간 계산값의 저장 부담을 줄이는 학습, 기존 가전제품 하드웨어의 학습 활용, 휴대전화에서의 영상 생성과 시간 변화 관계를 배우는 예측 방법을 다룬다.[^p1][^p2][^p3][^p4]

## 응용 분야

연구 방향은 사람과 실제 환경에 반응하는 로봇, 착용형 기기, 차량, 가전제품과 주변 조건에 적응하는 기계를 포함한다.[^statement] 논문에서 구현한 응용에는 세탁 시간·불균형 오류 예측과 휴대전화 영상 생성이 있고, 학부 성과 소개는 달 탐사 장치의 충돌구 탐지도 다룬다.[^p2][^p3][^crater]

## 구성원

2026년 11월 9일 연구실 Team 페이지에 적힌 교수 외 구성원 17명이다. PhD는 박사과정, MS-PhD는 석박사통합과정, Master는 석사과정으로 옮겼다. 시작은 첫 화면에 적힌 연구실 합류 연월이며 KAIST 입학 연월을 뜻하지 않는다. 「대표 논문 참여」는 전체 저자 목록에 영문 이름이 완전히 일치할 때 표시했다.[^team][^home]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Changhyeon Lee (이창현) | 박사과정 | Dec 2021 | 1 |
| Isu Jeong (정이수) | 석박사통합과정 | Feb 2022 | 3 |
| Bosung Kim (김보성) | 석박사통합과정 | Mar 2022 | 3 |
| Jeongmin Cheon (전정민) | 석사과정 | Jun 2022 |  |
| Kwangryeol Park (박광렬) | 석박사통합과정 | Aug 2022 | 4 |
| Yoel Park (박요엘) | 박사과정 | Jun 2023 |  |
| Kyu Hwan Lee (이규환) | 석사과정 | Jun 2023 |  |
| Jiwoon Chang (장지운) | 석사과정 | Aug 2024 |  |
| Yeojin Lee (이여진) | 석사과정 | Aug 2024 | 3 |
| Jaeyoung Lim (임재영) | 석사과정 | Jan 2025 |  |
| Wonheng Lee (이원행) | 석사과정 | Mar 2026 |  |
| Dongseok Ji (지동석) | 석사과정 | Mar 2026 |  |
| Hyunsun Hong (홍현선) | 박사과정 | Jul 2026 |  |
| Sungjeh Oh (오성제) | 석사과정 | Jul 2026 |  |
| Sangin Mun (문상인) | 석사과정 | Jul 2026 |  |
| Yuhyun Lee (이유현) | 석사과정 | Aug 2026 |  |
| Minseong Kim (김민성) | 석사과정 | Aug 2026 |  |

## 졸업생과 이전 구성원

Team 페이지의 Previous 구획에 적힌 4명이다. 학위·시기와 진로는 누리집 표기이며, 모두 이슬기 교수의 KAIST 부임 전 시기다.[^team][^appointment]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Insung Jung (정인성) | Master (2024 Spring) | LG Electronics |
| Jae Wook Lee (이재욱) | Master (2025 Spring) | Deloitte |
| Jaeho Kim (김재호) | Ph.D. (2025 Fall) | University of Virginia |
| Yunseok Lee (이윤석) | Master (2025 Fall) | Deloitte |

## 최근 논문 목록 (2021–2026)

연구실 Publication의 Conferences and Journals 구획 22편과 Preprints (Archives) 구획의 사전 공개본 1편이다. 연도·제목·저자·발표처는 연구실 표기다. 이슬기 교수의 2026년 2월 KAIST 부임 전 논문이 포함되어 있다. OliO는 NeurIPS 2026 「채택」으로 표시했고, 설명에 사용한 판본은 arXiv 사전 공개본이다. 별도 Preprints 구획의 On-device Sora도 사전 공개본으로 표시했다.[^pubs][^appointment][^p4]

**2026**

- Kwangryeol Park and Seulki Lee. "OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting". *The Fortieth Annual Conference on Neural Information Processing Systems, Sydney, Australia, Dec 2026. (채택; 초록 판본: arXiv:2610.23345) DOI: <https://doi.org/10.48550/arXiv.2610.23345>*.
- Isu Jeong, Seulki Lee\*, and Hyojung Ahn\*. "Intelligent Onboard Crater Detection for Lunar Exploration Systems Using Knowledge Distillation". *The third International Academy of Astronautics (IAA) Conference on Artificial Intelligence for Space, Korea, August 2026*.
- Yunseok Lee and Seulki Lee. "Enabling Fine-Tuning of Direct Feedback Alignment via Feedback-Weight Matching". *The Fourteenth International Conference on Learning Representations, Rio de Janeiro, Brazil, April 2026*.
- Changhyeon Lee and Seulki Lee. "ECAI: Efficient Convolution Activation Inversion for Constant-Memory Convolutional Neural Networks Training". *Twenty-Ninth Annual Conference on Artificial Intelligence and Statistics, Tangier, Morocco, May 2026*.
- Insung Jung and Seulki Lee. "Beyond Communication: On-Modem DNN Inference and Training for Home Appliances". *The 20th International Conference on Pervasive Computing and Communications, Pisa, Italy, Mar 2026. DOI: <https://doi.org/10.1109/percom67906.2026.11524490>*.
- Yoel Park, Jae Wook Lee, and Seulki Lee. "Designing Extremely Memory-Efficient CNNs for On-device Vision and Audio Tasks". *International Journal of Computer Vision (IJCV), Springer Nature, 2026. DOI: <https://doi.org/10.1007/s11263-025-02688-w>*.
- Bosung Kim\*, Kyuhwan Lee\*, Isu Jeong, Jungmin Cheon, Yeojin Lee, and Seulki Lee. "Mobile-Oriented Video Diffusion: Enabling Text-to-Video Generation on Mobile Devices Without Retraining, Compression, or Pruning". *The IEEE/CVF Winter Conference on Applications of Computer Vision 2026, Tucson, Arizona, Mar 2026. DOI: <https://doi.org/10.1109/wacv61042.2026.00386>*.

**2025**

- Kwangryeol Park, Jaeho Kim, and Seulki Lee. "AliO: Output Alignment Matters in Long-Term Time Series Forecasting". *The Thirty-Ninth Annual Conference on Neural Information Processing Systems, San Diego, USA, Dec 2025*.
- Jaeho Kim\*, Kwangryeol Park\*, Kyu Hwan Lee\*, Jeongmin Oh, Dongjin Park, Hyunseok Oh, Youngrock Chung, Kyung-Woo Lee, Dae-Un Sung, and Seulki Lee. "Smart ECU: Scalable On-Vehicle Deployment of Drivetrain Fault Classification Systems for Commercial Electric Vehicles". *The 34th ACM International Conference on Information and Knowledge Management (Applied Research Track), Seoul, Korea, Nov 2025. DOI: <https://doi.org/10.1145/3746252.3761522>*.
- Jaeho Kim and Seulki Lee. "TransPL: VQ-Code Transition Matrices for Pseudo-Labeling of Time Series Unsupervised Domain Adaptation". *The Forty-Second International Conference on Machine Learning, Vancouver, Canada, July 2025*.
- Jaeho Kim\*, Yunseok Lee\*, and Seulki Lee. "Position: The AI Conference Peer Review Crisis Demands Author Feedback and Reviewer Rewards". *The Forty-Second International Conference on Machine Learning, Vancouver, Canada, July 2025*.
- Isu Jeong and Seulki Lee. "Bayesian Code Diffusion for Efficient Automatic Deep Learning Program Optimization". *The 19th USENIX Symposium on Operating Systems Design and Implementation, Boston, Massachusetts, USA, July 2025*.
- Jaeho Kim\*, Kwangryeol Park\*, Sukmin Yun, and Seulki Lee. "PPT: Patch Order Do Matters In Time Series Pretext Task". *The Thirteenth International Conference on Learning Representations, Singapore, April 2025*.
- Kwangryeol Park and Seulki Lee. "SMMF: Square-Matricized Momentum Factorization for Memory-Efficient Optimization". *The 39th Annual AAAI Conference on Artificial Intelligence, Philadelphia, Pennsylvania, USA, Feb 2025. DOI: <https://doi.org/10.1609/aaai.v39i19.34186>*.
- Bosung Kim\*, Kyuhwan Lee\*, Isu Jeong, Jungmin Cheon, Yeojin Lee, and Seulki Lee. "On-device Sora: Enabling Diffusion-Based Text-to-Video Generation for Mobile Devices". *arXiv (사전 공개본), Feb, 2025. DOI: <https://doi.org/10.48550/arXiv.2502.04363>*.

**2024**

- Jae Wook Lee, Yoel Park, and Seulki Lee. "Designing Extremely Memory-Efficient CNNs for On-device Vision Tasks". *The 17th Asian Conference on Computer Vision, Hanoi, Vietnam, Dec 2024. DOI: <https://doi.org/10.1007/978-981-96-0966-6_25>*.
- Jaeho Kim, Seok-Ju Hahn, Yoontae Hwang, Junghye Lee, and Seulki Lee. "CAFO: Feature-Centric Explanation on Time Series Classification". *The 30th SIGKDD Conference on Knowledge Discovery and Data Mining, Aug 2024, Barcelona, Spain, Aug 2024. DOI: <https://doi.org/10.1145/3637528.3671724>*.
- Isu Jeong and Seulki Lee. "On-Demand Federated Learning for Arbitrary Target Class Distributions". *The 27th International Conference on Artificial Intelligence and Statistics, Valencia, Spain, May 2024*.

**2023**

- Changhyeon Lee and Seulki Lee. "Softmax Output Approximation for Activation Memory-Efficient Training of Attention-based Networks". *The 37th Annual Conference on Neural Information Processing Systems, New Orleans, LA, USA, Dec 2023*.
- Bosung Kim and Seulki Lee. "On-NAS: On-Device Neural Architecture Search on Memory-Constrained Intelligent Embedded Systems". *The 21st ACM Conference on Embedded Networked Sensor Systems, Istanbul, Turkiye, Nov 2023. DOI: <https://doi.org/10.1145/3625687.3625814>*.
- Seulki Lee. "MicroDeblur: Image Motion Deblurring on Microcontroller-based Vision Systems". *The 22nd International Conference on Information Processing in Sensor Networks, San Antonio, Texas, USA, May 2023. DOI: <https://doi.org/10.1145/3583120.3586970>*.
- Jaeho Kim, Hyewon Kang, Jaewan Yang, Haneul Jung, Seulki Lee, and Junghye Lee. "Multitask Deep Learning for Human Activity, Speed, and Body Weight Estimation using Commercial Smart Insoles". *Proceedings of IEEE Internet of Things Journal, Apr 2023. DOI: <https://doi.org/10.1109/jiot.2023.3267335>*.

**2022**

- Seulki Lee and Shahriar Nirjon. "Weight Separation for Memory-Efficient and Accurate Deep Multitask Learning". *The 20th International Conference on Pervasive Computing and Communications, Pisa, Italy, March 2022. DOI: <https://doi.org/10.1109/percom53586.2022.9762400>*.

## 수상과 선정

Honors and Awards와 첫 화면·교수 개인 페이지에 적힌 2023–2026년 수상·선정 16건이다. 연월이 있는 항목은 해당 표기를 썼고, 연도만 있는 2024·2025년 항목의 연도는 누리집 구획·항목 표기이며 날짜는 게시되어 있지 않다. 2025학년도 표기는 누리집의 Academic Year 2025다. 이슬기 교수의 2026년 2월 KAIST 부임 전 수상·선정도 포함되어 있다.[^awards][^home][^pi][^appointment]

- 2026-08 · 정이수·이슬기·Hyojung Ahn, IAA SpaceAI 2026 Best Student Paper Award 수상.
- 2026-04 · Isu Jeong·Bosung Kim·Kyu Hwan Lee·Seulki Lee, 2026 Google Research Award 선정(Cloud Research Credits, 50,000달러).
- 2026-05 · 이슬기, ICML 2026 Gold (Top) Reviewer 선정.
- 2026-08 · 이슬기, KAIA Summer Conference 2026 Best Reviewer 수상.
- 2025-07 · Jaeho Kim·Yunseok Lee·Seulki Lee, ICML 2025 Outstanding Position Paper Award 수상.
- 2025-10 · 정이수, Qualcomm Innovation Fellowship Korea 2025 (QIFK 2025) Finalist 선정.
- 2025학년도 · Jaeho Kim, UNIST Outstanding Graduate Thesis Award 수상.
- 2025-05 · 이슬기, SenSys 2025 Distinguished TPC Member Award 수상.
- 2024-12 · Jae Wook Lee·Yoel Park·Seulki Lee, ACCV 2024 Best Application Paper Award 수상.
- 2024-03 · Bosung Kim, 2024 Hyundai Mobis Edge AI Research Contest 2nd Place Award 수상.
- 2024-03 · Jaeho Kim, 2024 Hyundai Mobis Edge AI Research Contest 4th Place Award 수상.
- 2025 · Isu Jeong, UNIST AI Technology Open Workshop Best Poster Award 수상. 대상 논문은 「Bayesian Code Diffusion for Efficient Automatic Deep Learning Program Optimization」이다.
- 2024-09 · Jaeho Kim, UNIST AI Technology Open Workshop Best Poster Award 수상. 대상 논문은 「CAFO: Feature-Centric Explanation on Time Series Classification」이다.
- 2023-05 · 이슬기, IPSN 2023 Best Paper Runner-Up Award 수상.
- 2024 · 이슬기, Google Cloud Platform Credit Award: Gemma 2 Academic Program 선정.
- 2024-11 · Jaeho Kim, K-Data Science Conference 2024 Creative Researcher Award의 3rd Place Award 수상.

## 소식

연구실 첫 화면 News의 2021년 12월–2026년 9월 논문 채택·게재 승인 소식 21건이다. 날짜는 누리집의 연월이고, 당시 알린 사실을 옮겼다. 2026년 2월 KAIST 부임 전 소식이 포함되어 있다. 학술지 accepted는 「게재 승인」, 학회 accepted는 「채택」, with shepherding은 「조건부 채택」으로 표시했다.[^home][^appointment]

- 2026-09 · 논문 「OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting」의 NeurIPS 2026 채택을 알렸다.
- 2026-01 · 논문 「Enabling Fine-Tuning of Direct Feedback Alignment via Feedback-Weight Matching」의 ICLR 2026 채택을 알렸다.
- 2026-01 · 논문 「ECAI: Efficient Convolution Activation Inversion for Constant-Memory Convolutional Neural Networks Training」의 AISTATS 2026 채택을 알렸다.
- 2025-12 · 논문 「Beyond Communication: On-Modem DNN Inference and Training for Home Appliances」의 PerCom 2026 조건부 채택(with shepherding)을 알렸다.
- 2025-11 · 논문 「Mobile-Oriented Video Diffusion: Enabling Text-to-Video Generation on Mobile Devices Without Retraining, Compression, or Pruning」의 WACV 2026 채택을 알렸다.
- 2025-09 · 논문 「AliO: Output Alignment Matters in Long-Term Time Series Forecasting」의 NeurIPS 2025 채택을 알렸다.
- 2025-09 · 논문 「Designing Extremely Memory-Efficient CNNs for On-device Vision and Audio Tasks」의 IJCV (International Journal of Computer Vision) 게재 승인을 알렸다.
- 2025-08 · 논문 「Smart ECU: Scalable On-Vehicle Deployment of Drivetrain Fault Classification Systems for Commercial Electric Vehicles」의 CIKM 2025 채택을 알렸다.
- 2025-05 · 논문 「TransPL: Pseudo-Labeling via Code Transitions for Time Series Adaptation」의 ICML 2025 채택을 알렸다.
- 2025-05 · 논문 「Position: Towards a Sustainable AI Conference Peer Review System with Author Feedback and Reviewer Rewards」의 ICML 2025 채택을 알렸다.
- 2025-03 · 논문 「Bayesian Code Diffusion for Efficient Automatic Deep Learning Program Optimization」의 OSDI 2025 채택을 알렸다.
- 2025-01 · 논문 「PPT: Patch Order Do Matters In Time Series Pretext Task」의 ICLR 2025 채택을 알렸다.
- 2024-12 · 논문 「SMMF: Square-Matricized Momentum Factorization for Memory-Efficient Optimization」의 AAAI 2025 채택을 알렸다.
- 2024-09 · 논문 「Designing Extremely Memory-Efficient CNNs for On-device Vision Tasks」의 ACCV 2024 채택을 알렸다.
- 2024-05 · 논문 「CAFO: Feature-Centric Explanation on Time Series Classification」의 KDD 2024 채택을 알렸다.
- 2024-01 · 논문 「On-Demand Federated Learning for Arbitrary Target Class Distributions」의 AISTATS 2024 채택을 알렸다.
- 2023-09 · 논문 「Softmax Output Approximation for Activation Memory-Efficient Training of Attention-based Networks」의 NeurIPS 2023 채택을 알렸다.
- 2023-09 · 논문 「On-NAS: On-Device Neural Architecture Search on Memory-Constrained Intelligent Embedded Systems」의 SenSys 2023 채택을 알렸다.
- 2023-04 · 논문 「Multitask Deep Learning for Human Activity, Speed, and Body Weight Estimation using Commercial Smart Insoles」의 IEEE Internet of Things Journal 게재 승인을 알렸다.
- 2023-02 · 논문 「MicroDeblur: Image Motion Deblurring on Microcontroller-based Vision Systems」의 IPSN 2023 채택을 알렸다.
- 2021-12 · 논문 「Weight Separation for Memory-Efficient and Accurate Deep Multitask Learning」의 PerCom 2022 채택을 알렸다.

## 연락과 위치

- 교수 이메일: seulki.lee@kaist.ac.kr[^dept]
- 교수 연락처: 7475(학부 교수 소개 표기)[^dept]
- 교수 연구실: IT융합빌딩 N1 209호[^dept][^pi]
- 연구실 공간: N1 211호. 연구실 첫 화면은 건물 이름을 Kim Beang-Ho KIM Sam-Youl ITC로 적는다.[^home]
- 주소: 대전광역시 유성구 대학로 291 KAIST[^dept]

## 각주
[^home]: 연구실 첫 화면. <https://sites.google.com/view/embeddedai> 관측일 2026-11-09.
[^team]: Team. <https://sites.google.com/view/embeddedai/team> 관측일 2026-11-09.
[^statement]: Research Statement. <https://sites.google.com/view/embeddedai/statement> 관측일 2026-11-09.
[^research]: Research Topics. <https://sites.google.com/view/embeddedai/research> 관측일 2026-11-09.
[^pubs]: Publication. <https://sites.google.com/view/embeddedai/publication> 관측일 2026-11-09.
[^awards]: Honors and Awards. <https://sites.google.com/view/embeddedai/honors-and-awards> 관측일 2026-11-09.
[^pi]: 이슬기 교수 개인 소개와 경력. <https://sites.google.com/view/seulkilee> 관측일 2026-11-09.
[^dept]: 학부 이슬기 교수 상세 소개. <https://ee.kaist.ac.kr/professor/%ec%9d%b4%ec%8a%ac%ea%b8%b0/> 관측일 2026-11-09.
[^deptlist]: 학부 전임교수 목록 3쪽. <https://ee.kaist.ac.kr/professor-s1/?page=3> 관측일 2026-11-09.
[^appointment]: 이슬기 교수의 2026년 2월 4일 부임 안내. <https://ee.kaist.ac.kr/en/notices/%EC%A0%84%EA%B8%B0%EB%B0%8F%EC%A0%84%EC%9E%90%EA%B3%B5%ED%95%99%EB%B6%80-%EC%8B%A0%EC%9E%84-%EA%B5%90%EC%9B%90-%EC%9D%B4%EC%8A%AC%EA%B8%B0-%EA%B5%90%EC%88%98-%EB%B6%80%EC%9E%84-%EC%95%88%EB%82%B4/> 관측일 2026-11-09.
[^crater]: 정이수의 IAA SpaceAI 2026 수상과 LunarDet 연구 소개. <https://ee.kaist.ac.kr/en/research-achieve/isu-jeong-ph-d-student-advised-by-prof-seulki-lee-wins-best-student-paper-award-at-iaa-spaceai-2026/> 관측일 2026-11-09.
[^p1]: C. Lee, S. Lee, Proceedings of The 29th International Conference on Artificial Intelligence and Statistics 300, 2638–2646 (2026). <https://proceedings.mlr.press/v300/lee26c.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v300/lee26c.html>. 관측일 2026-11-09.
[^p2]: I. Jung, S. Lee, IEEE International Conference on Pervasive Computing and Communications (2026). <https://doi.org/10.1109/percom67906.2026.11524490> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100658136>. 관측일 2026-11-09.
[^p3]: B. Kim 외, S. Lee, IEEE Winter Conference on Applications of Computer Vision (2026). <https://doi.org/10.1109/wacv61042.2026.00386> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5100658136>. 관측일 2026-11-09.
[^p4]: K. Park, S. Lee, arXiv (NeurIPS 2026 채택) (온라인 2026-10-16). <https://doi.org/10.48550/arXiv.2610.23345> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.23345>. 관측일 2026-11-09.

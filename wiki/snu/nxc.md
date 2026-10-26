# 네트워크 컴퓨팅 및 Connected AI 연구실 (Networked Computing Lab., NXC)

**서울대학교 공과대학 전기·정보공학부 · 이경한 교수**

- 분야: 네트워크 시스템, 연결형 인공지능, 모바일 컴퓨팅
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: AI 시스템·인프라[^p1][^p2], 대형 언어 모델[^p1], 컴퓨터 네트워크[^p6], 무선·이동통신[^p3][^p4]
- 홈페이지: <https://nxc.snu.ac.kr/home>
- 근거: [읽은 자료와 확인 범위](nxc-sources.md)

> 휴대기기와 서버, 통신망이 계산과 데이터 전송을 함께 조율하도록 만드는 연구실이다. 모바일 인공지능의 실행 시간과 에너지 소비, 이동통신 서비스의 지연, 영상회의 서버와 데이터 압축을 연구한다.

## 무엇을 연구하나

이 연구실의 출발점은 인공지능 모델만 바꾸는 데서 그치지 않고, 모델을 실행하는 기기와 데이터를 나르는 통신망을 함께 설계하는 것이다. 홈페이지는 이를 Connected AI와 네트워크 컴퓨팅 연구로 소개하며, 모바일·착용형 기기, 인공지능 서비스 시스템, 인공지능과 결합한 이동통신망을 연구 대상으로 든다. 이경한 교수의 관심 분야도 연결·협력형 인공지능 시스템과 지연을 제어하는 네트워크 시스템이다.[^home][^prof]

모바일 인공지능에서는 추론(학습한 모델로 입력에 대한 결과를 계산하는 과정)을 어떤 순서와 자원으로 실행할지 연구한다. ASPEN은 신경망의 연산을 나누는 단위를 바꾸어 여러 계산을 함께 실행할 기회를 찾는다. mzCache는 여러 앱이 함께 실행되는 휴대기기에서 언어 모델의 메모리가 회수된 뒤 이를 복원하는 문제를 다룬다. NeuroBalancer는 가능한 한 일찍 계산을 끝내기보다 서비스가 정한 시간 안에서 계산을 분산하고, 처리장치와 메모리의 동작 주파수를 조절한다.[^p1][^p2][^p8]

통신 쪽에서는 RAN(무선 접속망, Radio Access Network)을 응용 서비스의 요구와 연결한다. CORA는 휴대기기에서 서버로 보내는 전송, 서버 계산, 결과를 받는 전송에 시간을 나누어 배정하고 각 단계의 자원을 조율한다. QCON은 이동통신 기지국에 동시에 연결하는 다중 연결을 활용하면서, 영상 서비스의 QoE(사용자가 체감하는 서비스 품질, Quality of Experience)를 기준으로 무선 자원을 배분한다.[^p3][^p4]

전송할 데이터와 서버 내부 구조도 연구 대상이다. nCTX는 송신자와 수신자가 미리 공유한 정보로 원래 데이터를 모사하고 그 차이를 함께 보내는 무손실 압축전송(원래 데이터를 그대로 복원할 수 있도록 전송량을 줄이는 방식)을 제안한다. eXpressSFU는 영상회의 서버에서 느린 제어 경로를 빠른 제어·데이터 처리 경로와 분리하고, 통신 처리를 수행하는 SmartNIC(스마트 네트워크 인터페이스 카드, Smart Network Interface Card)을 활용한다. 한편 관계망에서 상태가 퍼지는 현상을 다룬 논문에서는 그래프 신경망(개체와 관계를 점과 선으로 나타낸 자료를 처리하는 신경망)으로 기존 확산 모형의 표현력을 확장했다.[^p5][^p6][^p7]

## 주요 연구 주제

### 모바일 인공지능의 실행과 자원 관리

ASPEN은 텐서(다차원 배열)를 처리하는 연산마다 실행을 기다리는 경계가 생긴다는 점에 주목한다. 연산을 세분한 계산 조각의 의존 관계를 나타내고, 실행 중에 가능한 계산을 찾아 배정하는 방식이다. mzCache는 대형 언어 모델(많은 글을 학습해 언어를 처리하는 모델, Large Language Model)의 메모리를 공유 버퍼(여러 처리장치가 함께 접근하는 임시 저장 공간)로 나눈다. GPU(그래픽처리장치, Graphics Processing Unit)의 추론과 CPU(중앙처리장치, Central Processing Unit)의 메모리 복원을 함께 진행하도록 설계한다. NeuroBalancer는 신경망 연산의 지연과 에너지 소비를 이용해 처리장치와 메모리의 주파수를 조절한다.[^p1][^p2][^p8]

### 무선 접속망과 서버의 공동 조율

CORA는 무선 전송과 서버 계산이 서로 다른 자원을 사용하면서도 하나의 응답시간을 만든다는 점을 다룬다. 작업의 특성에 따라 단계별 시간 예산을 바꾸고 각 자원 배정기를 그 예산에 맞춘다. QCON은 상용 이동통신망이 보조 연결의 사용을 제한하는 정책을 고려하면서, 무선 접속망 안에서 응용 서비스의 체감 품질을 추정하고 연결별 전송을 조절한다.[^p3][^p4]

### 공유 정보 압축과 영상회의 시스템

nCTX는 데이터의 부호화와 복원을 수행하는 코덱에 신경망 기반 생성 모델과 서로 일치하는 데이터 블록을 활용한다. 공유한 정보로 입력을 모사한 결과에 원본과의 차이를 보충해 원래 데이터를 복원한다. eXpressSFU는 영상회의 참가자의 영상 데이터를 골라 다른 참가자에게 전달하는 SFU(선택적 전달 장치, Selective Forwarding Unit)의 처리 지연을 분석하고, 느린 제어 경로를 빠른 제어·데이터 처리 경로와 분리해 미디어 패킷(전송을 위해 데이터를 나눈 단위)의 처리를 가속한다.[^p5][^p6]

### 관계망 확산의 학습 모형

「Augmenting Epidemic Models with Graph Neural Networks」는 기존 유행 확산 모형이 수학적으로 다루기 위한 제한을 두거나 전체 평균 행동에 집중한다는 문제를 다룬다. 기존 모형의 유용한 수학 구조를 유지하면서 그래프 신경망으로 표현력을 확장하고, 개체별 관점과 관계망 전체 관점에서 확산 시간을 예측하는 새 모형을 제안했다. 질병 치료나 임상 평가가 아니라 확산 현상을 표현하고 예측하는 계산 방법에 관한 연구다.[^p7]

## 대표 논문

모바일 인공지능 실행, 무선 접속망과 서버 조율, 압축·영상회의, 관계망 모형을 나누어 골랐다. 이경한 교수가 저자인 서울대 재직 시기의 논문이며, 교신저자 표시는 랩 목록의 정의를 따랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. mzCache의 초록은 학회판과 연결된 arXiv 사전 공개본이다.[^pubs]

| 번호 | 연도 | 논문 · 발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2026 | [mzCache: On-Device LLM Memory Management under Multitasking](https://arxiv.org/abs/2609.01338) · arXiv, MobiCom 2026 연결 판본 | 휴대기기에서 앱을 오가면 운영체제가 언어 모델의 메모리를 회수할 수 있다. 다시 추론할 때 저장장치에서 읽거나 이전 계산을 다시 해야 하는 문제를 다룬다. 모델 메모리를 공유 저장 공간으로 나누고 일부 회수와 복원을 허용해, 처리장치가 추론하는 동안 다른 처리장치가 메모리를 복원하게 했다. 안드로이드 앱으로 구현해 실제 다중 작업 상황에서 평가했다.[^p1] | 교신저자 |
| 2 | 2023 | [ASPEN: Breaking Operator Barriers for Efficient Parallelization of Deep Neural Networks](https://doi.org/10.52202/075280-3002) · NeurIPS | 기존 신경망 실행 방식에서는 연산마다 다른 계산을 기다리는 경계가 생긴다. ASPEN은 신경망을 세분한 계산 조각들의 연결로 표현하고 실행 중에 함께 수행할 계산을 찾아 배정한다. 연산 경계를 넘어 계산할 기회를 활용하며, 중앙처리장치에서 구현한 시스템으로 평가했다.[^p2] | 교신저자 |
| 3 | 2025 | [End-to-End Coordination of RAN and Edge Server for Latency-Critical Inference Serving over Cellular Networks](https://doi.org/10.1145/3768987) · Proceedings of the ACM on Networking / CoNEXT | 휴대기기의 인공지능 요청이 무선 전송, 서버 계산, 결과 전송을 거치는 동안 여러 작업이 같은 자원을 다투는 문제를 다룬다. CORA는 작업마다 각 단계에 허용할 시간을 조절하고 무선 자원과 계산 자원의 배정을 맞춘다. 실제 무선 시험망에서 다양한 신경망 작업을 이용해 평가했다.[^p3] | 공동 교신저자 |
| 4 | 2026 | [QCON: Seamless QoE-Aware 5G Streaming via Multi-Connectivity](https://www.usenix.org/conference/nsdi26/presentation/lee) · USENIX NSDI | 영상 서비스는 통신 상태가 흔들려도 처리량과 지연을 유지해야 한다. QCON은 여러 이동통신 기지국에 동시에 연결하는 기능을 이용하되, 보조 연결을 아끼려는 통신 사업자의 정책도 고려한다. 무선 접속망 안에서 영상 서비스 품질을 추정해 연결별 자원을 배정하고 영상 중단을 막는 재전송 방식을 설계했다.[^p4] | 공동저자 |
| 5 | 2025 | [nCTX: A Neural Network-Powered Lossless Compressive Transmission Using Shared Information](https://doi.org/10.1109/TMC.2025.3530950) · IEEE Transactions on Mobile Computing | 보내는 쪽과 받는 쪽이 공유한 정보를 이용해 전송해야 하는 데이터 양을 줄인다. 생성 모델과 서로 일치하는 데이터 블록을 활용해 입력을 모사하고, 원본과의 차이를 보충해 원래 데이터를 복원한다. 공유 정보의 양과 압축률 사이의 관계를 활용하는 무손실 전송 시스템을 제안하고 모바일 환경에서 평가했다.[^p5] | 교신저자 |
| 6 | 2026 | [eXpressSFU: Toward Super-Scalable Video Conferencing with SmartNICs](https://www.usenix.org/conference/nsdi26/presentation/tran) · USENIX NSDI | 영상회의 서버가 참가자의 데이터를 처리하고 전달하는 시간이 확장성을 제한한다는 분석에서 출발한다. 느린 제어 경로를 빠른 제어·데이터 처리 경로와 분리하고 SmartNIC 같은 네트워크 기술로 미디어 패킷 처리를 가속하는 구조를 제안했다. 실험에서 처리 지연, 동시 이용자 수와 계산 전력 소비를 평가했다.[^p6] | 공동저자 |
| 7 | 2023 | [Augmenting Epidemic Models with Graph Neural Networks](https://doi.org/10.1145/3595244.3595249) · ACM SIGMETRICS Performance Evaluation Review | 기존 유행 확산 모형은 수학적 분석을 위해 관계망이나 접촉 과정에 제한을 두거나 전체 평균만 다루는 경우가 있다. 그래프 신경망으로 기존 모형을 보강하되 유용한 수학 구조는 보존하는 접근을 제안했다. 모의실험에서 개체별 관점과 관계망 전체 관점의 확산 시간을 예측했다.[^p7] | 교신저자 |
| 8 | 2025 | [NeuroBalancer: Balancing System Frequencies With Punctual Laziness for Timely and Energy-Efficient DNN Inferences](https://doi.org/10.1109/TMC.2024.3524628) · IEEE Transactions on Mobile Computing | 신경망 계산을 서비스가 요구하는 시점보다 일찍 끝내느라 에너지를 쓰는 문제를 다룬다. 정해진 지연 한도 안에 작업을 시간적으로 분산하는 자원 배정 전략을 제안하고, 연산 특성을 이용해 처리장치와 메모리의 동작 주파수를 조절한다. 안드로이드 기기와 여러 신경망 모델에서 평가했다.[^p8] | 교신저자 |

## 교수와 전문 분야

이경한 교수는 KAIST에서 학사(2002), 석사(2004), 박사(2009) 학위를 받았다. 2010년 4월부터 2012년 7월까지 North Carolina State University에서 연구했고, 2012년 8월부터 2020년 2월까지 UNIST 조교수·부교수로 재직했다. 서울대학교에는 2020년 3월 부교수로 부임했고 2023년 9월부터 교수로 재직한다. 랩 소개의 경력에는 2025년 9월부터 2026년 8월까지 KAIST 인공지능대학원 방문교수 이력도 있다.[^eceprof][^prof]

학과 소개는 전문 분야를 네트워크 시스템, Connected AI, 모바일 컴퓨팅으로 적는다. 구체적인 관심 연구에는 성능 보장형 이동통신망, 기계학습을 가속하는 분산 계산·네트워크, 시맨틱 통신(수신 작업에 필요한 의미나 정보를 고려하는 통신), 저전력·저발열 컴퓨팅이 있다. 최근 논문으로 보면 계산 실행과 메모리 관리, 무선 접속망과 서버 자원 배정, 압축전송과 영상회의 구조를 연결하는 시스템 설계가 전문 분야다.[^eceprof][^p1][^p2][^p3][^p5][^p6]

교수는 서울대의 **Cloud-Native AI-RAN Center**를 운영하는 PI(연구책임자, Principal Investigator)다. 랩 소개는 인공지능을 위한 무선 접속망과 차세대 이동통신망 재설계, 연결·협력형 인공지능, 상호작용 서비스용 네트워크 시스템을 관심 분야로 적는다.[^home][^prof]

## 응용 분야

대표적인 대상은 휴대기기에서 실행하는 언어 모델과 신경망, 이동통신망을 거쳐 서버가 처리하는 인공지능 요청, 실시간 영상 스트리밍과 영상회의다. 계산만 가속하거나 전송량만 줄이는 데서 그치지 않고, 응용 서비스의 응답시간과 무선 자원, 서버의 데이터 처리 구조를 함께 다룬다.[^p1][^p8][^p3][^p4][^p6]

## 구성원

2026년 10월 26일 랩 Ph.D/MS Students 게시 명단 28명이다. 석박사통합과정 22명, 박사과정 5명, 석사과정 1명이며 박사과정 칸에는 KAIST로 표기된 Siyavushkhon Kholmatov도 포함된다. 연구 주제와 팀 역할은 게시 표기다. 「대표 논문 참여」는 위 표 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Sanghyun Han | 석박사통합과정 | Switch ML, Kernel-bypass networking, XDP |  |
| DongGyu Yang | 석박사통합과정 | Network architecture design for machine learning acceleration |  |
| Taekyoung Han | 석박사통합과정 | Network Infrastructure for ML workloads |  |
| Jaeyoon Hwang | 석박사통합과정 | Data center congestion control/flow control, inference serving system |  |
| Serae Kim | 석박사통합과정 | Reinforcement learning and radio resource management | 3 |
| Gibum Park | 석박사통합과정 | Neural network offloading solution for low latency | 2 |
| Byunggu Kang | 석박사통합과정 (Team Lead - Computing) | Data encoding, semantic communication |  |
| Dongsu Kwak | 석박사통합과정 | Communication efficiency in distributed machine learning |  |
| Sunghyun Jin | 석박사통합과정 | Network slicing and radio resource management for guaranteed networks | 3 |
| Minjae Lee | 석박사통합과정 | Distributed Learning, Federated Learning |  |
| Huijeong Choe | 석박사통합과정 (Team Lead - Algorithm) | Semantic communication, Deep learning-based data encoding |  |
| Chanjeong Park | 석박사통합과정 (NXC Lab Head) | Scalable distributed computing |  |
| Daewook Hwang | 석박사통합과정 (Team Lead - Networking) | NIC microarchitecture and host network systems |  |
| Taehun Kim | 석박사통합과정 | Neural video compression; Low latency streaming system |  |
| Yonghwa Cho | 석박사통합과정 | On-Device inference acceleration, Edge-Server collaborative inference |  |
| Hongseung Yu | 석박사통합과정 | End-to-End System Design for AI inferences; Computation and Communication Co-Optimization | 1 |
| Sooyoung Kwon | 석박사통합과정 | Efficient deep learning system |  |
| Jusuk Kim | 석박사통합과정 | Real-time video streaming system, Neural video codec |  |
| Hojoon Kim | 석박사통합과정 | Communication optimization in distributed ML |  |
| Hyunah Kim | 석박사통합과정 | Systems for Efficient Large Language Model Inference |  |
| Bansuk Kim | 석박사통합과정 | Flexible encoding/decoding on wireless network |  |
| Yubin Song | 석박사통합과정 | AI-aware dynamic radio resource management |  |
| JongYun Lee | 박사과정 | Scalable multi-agent streaming systems |  |
| SeongSik Cho | 박사과정 | Predictive proactive control for cellular networks |  |
| Minsung Kim | 박사과정 | Agentic AI communication and serving system | 1 |
| Ilmuk Choi | 박사과정 | Framework for Distributed ML Networks |  |
| Siyavushkhon Kholmatov | 박사과정 | AI-RAN, OpenRAN, M obile C omputing, and AI |  |
| Jaewon In | 석사과정 | Privacy Preserving Machine Learning; Split Learning |  |

## 졸업생과 이전 구성원

2026년 10월 26일 Alumni 페이지의 Ph.D. 칸 8명과 M.S. 칸 4명이다. 서울대 학위 취득자뿐 아니라 다른 대학에서 박사학위를 받은 뒤 NXC에서 박사후연구원으로 참여한 사람도 함께 있다. 학위·과정과 진로는 페이지 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Seyeon Kim | PostDoc at NXC (Ph.D. KAIST, 2022) | Korea University (Assistant Professor, CS) |
| Junseon Kim | PostDoc at NXC (Ph.D. UNIST, 2022) | Catholic Univ. (Assistant Professor, EE) |
| Sungyong Lee | PostDoc at NXC (Ph.D. UNIST, 2023) | Samsung DS AI (Senior Researcher) |
| Shinik Park | Ph.D. SNU (NXC), 2025.02 | Samsung MX (Staff Engineer) |
| Kyungmin Bin | Ph.D. SNU (NXC), 2025.02 | Samsung SDS (Senior Engineer) |
| WooSeung Nam | Ph.D. SNU (NXC), 2025.08 | KAIST (InnoCore Post Doc., Daejeon, KR) |
| Jeongmin Bae | PostDoc at NXC (Ph.D. KAIST, 2023) | CMU (Post Doc., Pittsburgh, PA) |
| GoodSol Lee | Ph.D. SNU (NXC), 2026.02 | Nokia Bell Labs. (Murray Hill, NJ) |
| Jongseok Park | M.S. SNU (NXC), 2024.08 | UC Berkeley (Ph.D. Student) |
| Dongwook Choi | M.S. SNU (NXC), 2025.02 | Samsung Networks (Staff Engineer) |
| Gyulim Gu | M.S. SNU (GSEP & NXC), 2023.02 | LG Electronics (Staff Engineer) |
| Wonjun Bang | M.S. SNU (NXC), 2026.08 | Yale University (Ph.D. Student) |

## 최근 논문 목록 (2021–2026)

랩 Publications의 Selected Publications 가운데 2021–2026년 표기 47편이다. 전체 원문은 서울대 부임 전 논문도 함께 싣는 교수 개인의 선정 목록이며, 이 목록은 서울대 연구실만의 전체 실적으로 한정하지 않는다. 연도는 누리집의 표기를 따른다. 2021년 논문은 월과 관계없이 포함했다. 학술지의 「게재 승인」은 출판 논문과 구분했고, mzCache와 TACToC는 랩 소식의 학회 채택을 함께 표시했다. 별표는 누리집이 정의한 교신저자 표시다.[^pubs][^home]

**2026**

- Wonjun Bang, Jongseok Park, Hongseung Yu, Sanghyun Han, Kyungmin Bin, and Kyunghan Lee\*. "BVSR: BitVector-Sum Representation for Distribution-Aware LLM Weight Quantization". *Neurocomputing, 게재 승인, 2026*.
- Jaeyoon Hwang, Youngwook Son, Hojun Kim, Juhun Shin, Taekyoung Han, Junhong Min, Daewook Hwang, Sangtae Ha\*, and Kyunghan Lee\*. "Unlocking Opportunistic Transmission in Datacenter Flow Control". *ACM CoNEXT, Utrecht, Netherlands, 2026. (Proceedings of the ACM on Networking, Volume 4, Issue CoNEXT2, Jun. 2026.)*.
- Taekyoung Han, Daewook Hwang, Shinik Park, Donggyu Yang, Gibum Park, Sanghyun Han, Jaeyoon Hwang, Byunggu Kang, Sangtae Ha\*, and Kyunghan Lee\*. "PRC: Process-centric Rate Control for Transient Stragglers in Hybrid-Parallel Training". *ACM CoNEXT, Utrecht, Netherlands, 2026. (Proceedings of the ACM on Networking, Volume 4, Issue CoNEXT2, Jun. 2026.)*.
- Hongseung Yu, Minsung Kim, Jonseok Park, and Kyunghan Lee\*. "mzCache: On-Device LLM Memory Management under Multitasking". *ACM MobiCom, Austin, TX, 2026. (랩 소식의 MobiCom 채택, 초록은 arXiv 사전 공개본)*.
- Huijeong Choe, Minjae Lee, Wooseung Nam, Taehun Kim, and Kyunghan Lee\*. "TACToC: Enabling Task-Adaptive Communication System with a Task-Describable Encoder". *ACM MobiCom, Austin, TX, 2026. (랩 소식의 MobiCom 채택)*.
- Jeongmin Bae, Harim Kang, Taehun Kim, Taegun An, Seunghyun Lee, Junhao Cai, Changhee Joo\*, and Kyunghan Lee\*. "RXC: Runtime Extra Compression for Time-Critical Content Delivery". *IEEE Communications Magazine, 게재 승인, 2026*.
- Jeongmin Bae, Junseon Kim, Carlee Joe-Wong\*, and Kyunghan Lee\*. "Redefining the Role of Large AI Models in Real-time RAN Control". *IEEE Communications Magazine, 게재 승인, 2026*.
- Junseon Kim, Jeongmin Bae\*, and Kyunghan Lee\*. "ATC: An Active Cellular Network Architecture for Application Performance Guarantee in 6G". *IEEE Communications Magazine, 게재 승인, 2026*.
- Tuan Tran, Shirin Ebady, S. M. Hossein Hosseini, Woongsub Shin, Evan Ram, Youngwook Son, Seyeon Kim, Nam Bui, Kyunghan Lee, Eric Keller, and Sangtae Ha. "DeepSFU: Scalable Deepfake Detection for Video Conferencing". *ACM SIGCOMM, 2026*.
- Siyavushkhon Kholmatov, Seongsik Cho, Song Chong, and Kyunghan Lee\*. "Toward AI-on-RAN: Enabling on-RAN Intelligence for AI-Native 6G Networks". *IEEE NETWORK, 게재 승인, 2026*.
- Chanjeong Park, Donggyu Yang, Sooyoung Kwon, Gibum Park, Carlee Joe-Wong\*, and Kyunghan Lee\*. "Ouroboros: Instilling Motion Awareness in ViTs for Efficient Video Analytics on the Edge". *ACM MobiSys, Cambridge, UK, 2026*.
- Gibum Park, Sanghyun Han, Yonghwa Cho, Chanjeong Park, and Kyunghan Lee\*. "SAIL: Redesigning Collaborative Language Inference with a Single Server-to-Mobile Handoff". *ACM MobiSys, Cambridge, UK, 2026*.
- Chanjeon Park, Gibeom Park, Carlee Joe-Wong, and Kyunghan Lee\*. "(poster) Accelerating Offloaded ViT Inference via Progressive Refinement". *ACM MobiSys, Cambridge, UK, 2026*.
- Gibeom Park, Sanghyun Han, Yonghwa Cho, Chanjeong Park, and Kyunghan Lee\*. "(poster) Selective Semantic Cache Transfer for Mobile-Cloud LLM Inference". *ACM MobiSys, Cambridge, UK, 2026*.
- Jongyun Lee, Jeongmin Bae, Sanghyun Han, Sangtae Ha, and Kyunghan Lee\*. "DECENTO: A New Scalable Interactive Live Streaming System via Control Plane Decentralization". *IEEE INFOCOM, Tokyo, Japan, 2026*.
- Goodsol Lee, Seyeon Kim, Juheon Yi, Junhong Min, Tuan Tran, Sangtae Ha, Kyunghan Lee, and Saewoong Bahk. "PAVE: Mitigating Non-Congestive Delay for Seamless Video Calls over NextG Mobile Networks". *IEEE INFOCOM, Tokyo, Japan, 2026*.
- Goodsol Lee, Junhong Min, Seyeon Kim, Juheon Yi, Kwang Taik Kim, Mung Chiang, Sangtae Ha, Kyunghan Lee, and Saewoong Bahk. "QCON: Seamless QoE-aware 5G Streaming via Multi-Connectivity". *NSDI, Renton, WA, 2026*.
- Tuan Tran, S.M. Hosseini, Seyeon Kim, Kyunghan Lee, Nam Bui, Dirk Grunwald, and Sangtae Ha\*. "eXpressSFU: Toward Super-Scalable Video Conferencing with SmartNICs". *NSDI, Renton, WA, 2026*.

**2025**

- Sunghyun Jin, Serae Kim, Sangtae Ha\*, and Kyunghan Lee\*. "End-to-End Coordination of RAN and Edge Server for Latency-Critical Inference Serving over Cellular Networks". *ACM CoNEXT, Hong Kong, China, 2025. (Proceedings of the ACM on Networking, Volume 3, Issue CoNEXT4, No. 40, pp. 1-23, Nov. 2025.)*.
- Siyavushkhon Kholmatov, Seongsik Cho, Song Chong, and Kyunghan Lee\*. "AoRA: AI-on-RAN Architecture for Backhaul-free Edge Inference". *ACM SIGCOMM (short), Coimbra, Portugal, 2025*.
- Donggyu Yang, Wooseung Nam, Byunggu Kang, and Kyunghan Lee\*. "Empilo: Realizing Immersive Mobile 3D Video Conferencing through Parameterized Communication". *ACM MobiSys, Anaheim, CA, 2025*.
- Wooseung Nam, Sungyong Lee, Joohyun Lee, and Kyunghan Lee\*. "nCTX: A Neural Network-Powered Lossless Compressive Transmission using Shared Information". *IEEE Transactions on Mobile Computing, vol. 24, no. 5, pp. 5386-5399, Jun. 2025*.
- Wooseung Nam, Sungyong Lee, Jinsung Lee, Huijeong Choi, Sangtae Ha, and Kyunghan Lee\*. "N-epitomizer: A Semantic Offloading Framework leveraging Essential Information for Timely Neural Network Inferences". *IEEE/ACM Transactions on Networking, vol. 33, no. 3, pp. 1041-1055, Jun. 2025*.
- Kyungmin Bin, Seyeon Kim, Sangtae Ha, Song Chong, and Kyunghan Lee\*. "NeuroBalancer: Balancing System Frequencies with Punctual Laziness for Timely and Energy-efficient DNN Inferences". *IEEE Transactions on Mobile Computing, vol. 24, no. 5, pp. 4339-4354, May 2025*.
- Hyunsoo Kim, Sangwi Kang, Kyunghan Lee, and Taekyoung Kwon\*. "A Certificate-centric Security Oracle for the Trustworthy Internet". *ACM WWW (short), Sydney, Australia, 2025*.
- Masoud Shokrnezhad, Hao Yu, Tarik Taleb, Richard Li, Kyunghan Lee, Jaeseung Song, and Cedric Westphal. "Towards a Dynamic Future with Adaptable Computing and Network Convergence (ACNC)". *IEEE NETWORK, vol. 39, no. 2, pp. 268-288, Mar. 2025*.
- Dongwook Choi, Shinik Park, Donggyu Yang, and Kyunghan Lee\*. "ADQ: Application-aware Socket Buffer Dequeueing for Mobile Devices". *IEEE CCNC, Las Vegas, NV, 2025*.

**2024**

- Kyungmin Bin, Jongseok Park, Chanjeong Park, Seyeon Kim, and Kyunghan Lee\*. "CoActo: CoActive Neural Network Inference Offloading with Fine-grained and Concurrent Execution". *ACM MobiSys, Tokyo, Japan, 2024*.
- Shinik Park, Sanghyun Han, Jongyun Lee, Junseon Kim, Sangtae Ha, and Kyunghan Lee\*. "ExStream: A Delay-minimized Streaming System with Explicit Frame Queueing Delay Measurement". *IEEE INFOCOM, Vancouver, Canada, 2024*.
- Hyoyoung Lim, Jinsung Lee, Jongyun Lee, Sandesh Dhawaskar Sathyanarayana, Junseon Kim, Anh Nguyen, Kwang Taik Kim, Youngbin Im, Mung Chiang, Dirk Grunwald, Kyunghan Lee, and Sangtae Ha. "An Empirical Study of 5G: Effect of Edge on Transport Protocol and Application Performance". *IEEE Transactions on Mobile Computing, vol. 23, no. 4, pp.3172-3186, Apr. 2024*.
- Junseon Kim, Youngbin Im, and Kyunghan Lee\*. "Enabling Delay-Guaranteed Congestion Control with One-Bit Feedback in Cellular Networks". *IEEE/ACM Transactions on Networking, vol. 32, no. 1, pp.3-16, Feb. 2024*.

**2023**

- Jongseok Park, Kyunbmin Bin, Gibum Park, Sangtae Ha, and Kyunghan Lee\*. "ASPEN: Breaking Operator Barriers for Efficient Parallelization of Deep Neural Networks". *NeurIPS, New Orleans, LA, 2023*.
- Seyeon Kim, Kyungmin Bin, Donggyu Yang, Sangtae Ha, Song Chong, and Kyunghan Lee\*. "ENTRO: Tackling the Encoding and Networking Trade-off in Offloaded Video Analytics". *ACM Multimedia, Ottawa, Canada, 2023*.
- Sungyong Lee, Wooseung Nam, Jinsung Lee, Sangtae Ha, and Kyunghan Lee\*. "N-epitomizer: Enabling Semantic Offloading for Neural Network Inferences". *IEEE MASS (invited), Toronto, Canada, 2023*.
- Sandesh Dhawaskar Sathyanarayana, Kyunghan Lee, Dirk Grunwald, and Sangtae Ha. "Converge: QoE-driven Multipath Video Conferencing over WebRTC". *ACM SIGCOMM, New York, NY, 2023*.
- Sungyong Lee, Jinsung Lee, and Kyunghan Lee\*. "DeepVehicleSense: An Energy-efficient Transportation Mode Recognition Leveraging Staged Deep Learning over Sound Samples". *IEEE Transactions on Mobile Computing, vol. 22, no. 6, pp.3270-3286, Jun. 2023*.
- Wonjun Hwang, Yoora Kim, and Kyunghan Lee\*. "Augmenting Epidemic Models with Graph Neural Networks". *ACM SIGMETRICS Performance Evaluation Review, vol. 50, no. 4, pp.11-13, Mar. 2023. (from ACM SIGMETRICS 2022 poster track)*.
- Junseon Kim, Byonghyo Shim, and Kyunghan Lee\*. "Towards Enabling Performance-Guaranteed Networking in Next-Generation Cellular Networks". *IEEE Communications Magazine, vol. 61, no. 1, pp.32-37, Jan. 2023*.

**2022**

- Insoo Lee, Seyeon Kim, Sandesh Dhawaskar Sathyanarayana, Kyungmin Bin, Song Chong, Kyunghan Lee\*, Dirk Grunwald, and Sangtae Ha\*. "R-FEC: RL-based FEC Adjustment for better QoE in WebRTC". *ACM Multimedia, Lisbon, Portugal, 2022*.
- Jongseok Park, Kyungmin Bin, and Kyunghan Lee\*. "mGEMM: Low Latency Convolution with Minimal Memory Overhead Optimized for Mobile Devices". *ACM MobiSys, Oregon, PO, 2022*.
- Een-Kee Hong, Inkyu Lee, Byonghyo Shim, Young-Chai Ko, Sang-Hyo Kim, Sangheon Pack, Kyunghan Lee, Sunwoo Kim, Jae-Hyun Kim, Yoan Shin, Younghan Kim, and Haejoon Jung. "6G R&D Vision: Requirements and Candidate Technologies". *Journal of Communications and Networks, vol. 24, no. 2, pp.232-245, Apr. 2022*.
- Seyeon Kim, Kyungmin Bin, Sangtae Ha, Kyunghan Lee\*, and Song Chong. "zTT: Learning-based DVFS with Zero Thermal Throttling for Mobile Devices". *ACM GetMobile: Mobile Computing and Communications Review, vol. 25, no.4, pp.30-34, Mar. 2022*.

**2021**

- Insoo Lee, Jinsung Lee, Kyunghan Lee, Dirk Grunwald, and Sangtae Ha. "Demystifying Commercial Video Conferencing Applications". *ACM Multimedia, Chengdu, China, 2021*.
- Seyeon Kim, Kyungmin Bin, Sangtae Ha, Kyunghan Lee\*, and Song Chong. "zTT: Learning-based DVFS with Zero Thermal Throttling for Mobile Devices". *ACM MobiSys, 2021*.
- Junseon Kim, Youngbin Im, and Kyunghan Lee\*. "ECLAT: An ECN Marking System for Latency Guarantee in Cellular Networks". *IEEE INFOCOM, Vancouver, Canada, 2021*.
- Jason Schnitzer, Prasanth Prahladan, Parisa Rahimzadeh, Chad Humble, Jinsung Lee\*, Jihoon Lee, Kyunghan Lee, and Sangtae Ha. "Towards Programmable DOCSIS 4.0 Networks: Adaptive Modulation in OFDM Channels". *IEEE Transactions on Network and Service Management, vol. 18, no. 1, pp. 441-455, Mar. 2021*.
- Wooseung Nam, Joohyun Lee, Ness B. Shroff, and Kyunghan Lee\*. "An Inter-data Encoding Technique that Exploits Synchronized Data for Network Applications". *IEEE Transactions on Mobile Computing, vol. 20, no. 1, pp. 75-92, Jan. 2021*.

## 과제

게시 과제 28건 중 기간이 2021년 10월 22일–2026년 10월 22일과 겹치는 15건이다. 누리집의 진행 과제 칸 9건과 완료 과제 칸 6건이며, 구분은 누리집 표기다. 교수 개인의 과제 목록으로 서울대 부임 전인 2017·2018년에 시작한 과제도 포함된다. PI는 연구책임자, Co-PI는 공동 연구책임자다.[^projects][^prof]

- 초저지연/무손실/고대역폭 AI 데이터센터 패브릭 플랫폼 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2026-04-01–2030-12-31)
- [중견연구] 차세대 네트워크 응용을 위한 통합 작업 지향 통신 시스템 연구 (지원 한국연구재단 (NRF); 역할 PI; 기간 2025-03-01–2030-02-28)
- 고수준 응용-네트워크 연동 프로그래머블 인터페이스 기술 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 PI; 기간 2024-04-01–2028-12-31)
- 차세대통신클라우드 리더십 구축사업 (지원 과학기술정보통신부 (MSIT - IITP); 역할 PI; 기간 2024-07-01–2028-12-31)
- 6G 종단간 초정밀 네트워킹을 위한 핵심기술 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 PI; 기간 2022-04-01–2025-12-31)
- AI-Native 응용서비스 지원 AI 오케스트레이터 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2024-04-01–2028-12-31)
- 오픈랜 인력양성 프로그램 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2024-07-01–2028-12-31)
- [ERC] 인지증강 메타통신 연구센터 (지원 한국연구재단 (NRF); 역할 Co-PI; 기간 2023-03-01–2029-02-28)
- [ITRC] UAM 고밀도 운항을 위한 URAN (Ultra Reliable Aerial Network) 설계 및 원천기술 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2021-07-01–2028-12-31)
- [중견연구] 차세대 네트워크 응용을 위한 AI 모델 기반 초고효율 압축전송 연구 (지원 한국연구재단 (NRF); 역할 PI; 기간 2021-03-01–2025-02-28)
- 6G 네트워크 아키텍처 및 핵심 요소기술 국제 협력 연구 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2021-07-01–2024-06-30)
- 유저레벨 초저지연 전송 프로토콜 개발 (지원 과학기술정보통신부 (MSIT - IITP); 역할 Co-PI; 기간 2018-07-01–2023-12-31)
- On-path Computing enabling Large-scale Neural Network Services in 6G (지원 삼성 미래기술육성센터; 역할 PI; 기간 2020-07-01–2023-06-30)
- A Next Generation WiFi System for High-resolution/Low-latency AR/VR/MR Services (지원 삼성 미래기술육성센터; 역할 Co-PI; 기간 2018-09-01–2022-05-30)
- 이동 객체에 대한 증강현실 서비스 실현을 위한 정보-영상 정합기술 연구 (지원 과학기술정보통신부 (MSIT - IITP); 역할 PI; 기간 2017-04-01–2022-12-31)

## 특허

누리집 Registered Patents 가운데 등록일 표기가 2021년 10월 22일–2026년 10월 22일에 해당하는 31건이다. 미국 2건과 한국 29건이며, 제목·등록번호·등록일은 게시 표기다.[^projects]

- Method and apparatus for determining bottleneck link (등록번호 US11974352B2; 등록일 2024-04-30; 국가 미국)
- Image processing apparatus and data receiving apparatus, and methods thereof (등록번호 US11252408B2; 등록일 2022-02-15; 국가 미국)
- Modem device based on neural network computation (등록번호 KR 10-2938794; 등록일 2026-03-12; 국가 한국)
- Method and system for encoding and decoding based on deep neural network (등록번호 KR 10-2827987; 등록일 2025-06-26; 국가 한국)
- Camera exposure control method and camera exposure control system (등록번호 KR 10-2806714; 등록일 2025-05-28; 국가 한국)
- Method for guaranteeing 6g end-to-end application-level latency using network transport api and electronic device (등록번호 KR 10-2793447; 등록일 2025-04-04; 국가 한국)
- Apparatus and method computing low-latency convolution optimized for mobile devices (등록번호 KR 10-2733737; 등록일 2024-11-20; 국가 한국)
- Scalable video coding apparatus and method for real-time video streaming (등록번호 KR 10-2709561; 등록일 2024-09-20; 국가 한국)
- Device of compressing data, system of compressing data and method of compressing data (등록번호 KR 10-2706107; 등록일 2024-09-09; 국가 한국)
- Apparatus for processing media streaming and method therefor (등록번호 KR 10-2643682; 등록일 2024-02-28; 국가 한국)
- Object recognition processing apparatus and method for AR device (등록번호 KR 10-2592551; 등록일 2023-10-18; 국가 한국)
- Image data processing apparatus and method (등록번호 KR 10-2573511; 등록일 2023-08-29; 국가 한국)
- Apparatus and method for evaluating performance of video streaming system (등록번호 KR 10-2565295; 등록일 2023-08-04; 국가 한국)
- Congestion control apparatus and method for objectified data (등록번호 KR 10-2564057; 등록일 2023-08-01; 국가 한국)
- Apparatus and method for transmitting packets in wireless communication system (등록번호 KR 10-2560594; 등록일 2023-07-24; 국가 한국)
- Transmission control apparatus and method through deep learning based-channel loss prediction (등록번호 KR 10-2555936; 등록일 2023-07-11; 국가 한국)
- Method for communication based on UAV (unmanned aerial vehicle) BS (base station) using reinforcement learning and apparatus for performing the method (등록번호 KR 10-2529331; 등록일 2023-05-02; 국가 한국)
- Driving control method and apparatus (등록번호 KR 10-2527972; 등록일 2023-04-26; 국가 한국)
- Data compressing and restoring apparatus for lossless image compression (등록번호 KR 10-2524547; 등록일 2023-04-18; 국가 한국)
- Method and apparatus for dynamic adjustment of aggressiveness parameters for packet flow in the network (등록번호 KR 10-2471228; 등록일 2022-11-22; 국가 한국)
- Method and apparatus for network throughput estimation (등록번호 KR 10-2461257; 등록일 2022-10-26; 국가 한국)
- Method and apparatus for communication control (등록번호 KR 10-2432668; 등록일 2022-08-10; 국가 한국)
- Method and apparatus for performing artificial neural network inference in mobile terminal (등록번호 KR 10-2422545; 등록일 2022-07-14; 국가 한국)
- Apparatus for media streaming control and method therefor (등록번호 KR 10-2419087; 등록일 2022-07-05; 국가 한국)
- Method and apparatus for receiving of real time data streaming, system for transmitting and receiving of real time data streaming, computer-readable storage medium and computer program (등록번호 KR 10-2409915; 등록일 2022-06-13; 국가 한국)
- Method and apparatus for selecting a transmission path in a distributed network (등록번호 KR 10-2400952; 등록일 2022-05-18; 국가 한국)
- Method and apparatus for control transmission based on transmission control protocol in a communication system (등록번호 KR 10-2363534; 등록일 2022-02-11; 국가 한국)
- Method and apparatus for streaming service (등록번호 KR 10-2353492; 등록일 2022-01-17; 국가 한국)
- Method and apparatus for object recognition (등록번호 KR 10-2346964; 등록일 2021-12-30; 국가 한국)
- Method and apparatus for guided driving based on road-side infrastructure (등록번호 KR 10-2332820; 등록일 2021-11-25; 국가 한국)
- Method and apparatus for image processing (등록번호 KR 10-2320496; 등록일 2021-10-27; 국가 한국)

## 수상과 선정

홈페이지의 기간 안 수상·지원 선정 공지 25항목과 교수 소개의 연도만 적힌 2항목이다. 한 공지가 여러 수상자를 함께 적은 경우 한 항목으로 옮겼다. 연도만 적힌 2024·2025년 항목은 월일 표기가 없음을 표시했다. 상 이름의 연도와 공지 날짜가 다른 경우 두 표기를 구분했다.[^home][^prof]

- 2026-07-06 · Myungha(NXC 인턴): 한국연구재단 BK21 Outstanding Undergraduate Researcher Grant 선정.
- 2026-05-14 · Hyunah: ACM MobiSys 2026 Student Travel Grant 선정.
- 2025-12-26 · 이경한: IEEE INFOCOM 2026 Technical Program Committee Distinguished Member 선정.
- 2025-05-23 · Byunggu: ACM MobiSys 2025 Student Travel Grant 선정.
- 2025-03-10 · 이경한과 담당 조교: 서울대학교 공과대학 Lee Byoungho Excellence in Teaching Award, 2024년 가을 데이터통신망의 기초 강의.
- 2025-02-12 · Daewook·Taekyoung: 삼성휴먼테크논문대상 통신·네트워크 분야 동상.
- 2024-11-04 · Chanjeong: A3 Foresight Program 2024 Best Presentation Award(베이징).
- 2024-10-16 · 이경한: 서울대학교 공과대학 신양공학학술상 학술부문.
- 2024-09-27 · 이경한: 일본 Okawa Foundation의 Okawa Research Grant Award 2024 선정.
- 2024-08-16 · Kyungmin: 삼성 DS 부문 Outstanding Paper Award 2024.
- 2024-06-24 · Jeongmin Bae(NXC 박사후연구원): 한국연구재단 Next-Generation Scholar Grant 선정.
- 2024-06-17 · Donggyu: A3 Foresight Program 2024 Best Presentation Award(제주).
- 2024-06-11 · 이경한: 「6G R&D Vision: Requirements and Candidate Technologies」 공저 논문의 JCN Best Paper 2024 수상.
- 2024-05-08 · Chanjeong: ACM MobiSys 2024 Student Travel Grant 선정.
- 2024-02-07 · 삼성휴먼테크논문대상: 금상 Jeongmin·Jongyun, 장려상 Shinik·Wooseung·Jongseok
- 2023-09-21 · Jeongmin: A3 Foresight Program 2023 Best Presentation Award(난징).
- 2022-12-20 · Junseon: UNIST NAVER Ph.D. Fellowship Award 2022.
- 2022-09-29 · 이경한: 한국공학교육학회 우수강의 교수상 2022.
- 2022-05-24 · Jongseok: ACM MobiSys 2022 Student Travel Grant 선정.
- 2022-05-10 · Junseon Kim(NXC 박사후연구원): 한국연구재단 Next-Generation Scholar Grant 선정.
- 2022-03-07 · 이경한과 담당 조교: 서울대학교 전기·정보공학부 Excellence in Teaching Award, 2021년 가을 자료구조의 기초 강의.
- 2022-01-27 · Sungyong: 삼성휴먼테크논문대상 동상(홈페이지 공지의 상 이름에는 2021년으로 표기).
- 2021-12-31 · 이경한: 5G·6G 기술 발전 기여에 대한 과학기술정보통신부 장관 표창.
- 2021-12-10 · Junseon: UNIST NAVER Ph.D. Fellowship Award 2021.
- 2021-12-02 · 이경한: 한국과학기술한림원 차세대회원(Y-KAST) 선정.
- 2024년 (월일 표기 없음) · 이경한: 과학기술정보통신부 장관 표창, AI-integrated RAN architecture 기여
- 2025년 (월일 표기 없음) · 이경한: 서울대학교 전기·정보공학부 Excellence in Teaching Award

## 소식

홈페이지의 2021년 10월 22일–2026년 10월 22일 공지 중 연구 논문·포스터의 채택과 게재 승인, 공동연구 지원 선정을 알린 36항목이다. 날짜는 공지가 적은 날짜이고 출판일과는 다르다.[^home]

- 2026-10-04 · 「BVSR: BitVector-Sum Representation for Distribution-Aware LLM Weight Quantization」: NeuroComputing 게재 승인.
- 2026-09-10 · 「Unlocking Opportunistic Transmission in Datacenter Flow Control」: ACM CoNEXT 2026 (Utrecht, Netherlands) 채택.
- 2026-08-13 · Parent-Child AI Model Architecture, Runtime eXtra Compression, Active Cellular Network Architecture 연구 논문이 IEEE Communications Magazine 게재 승인을 받았다.
- 2026-06-30 · 「mzCache: On-Device LLM Memory Management under Multitasking」: ACM MobiCom 2026 (Austin, TX) 채택.
- 2026-06-30 · 「DeepSFU: Scalable Deepfake Detection for Video Conferencing」: ACM SIGCOMM 2026 (Denver, CO) 채택.
- 2026-04-29 · 포스터 「Accelerating Offloaded ViT Inference via Progressive Refinement」와 「Selective Semantic Cache Transfer for Mobile-Cloud LLM Inference」가 ACM MobiSys 2026에 채택됐다.
- 2026-03-29 · 「PRC: Process-centric Rate Control for Transient Stragglers in Hybrid-Parallel Training」: ACM CoNEXT 2026 (Utrecht, Netherlands) 채택.
- 2026-03-26 · 「Toward AI-on-RAN: Enabling on-RAN Edge Intelligence for AI-Native 6G Networks」: IEEE Network Magazine 게재 승인.
- 2026-03-01 · Gibum과 Changjeong이 각각 제1저자인 Connected AI 논문이 ACM MobiSys 2026에 채택됐다.
- 2026-02-04 · Jongyun·Donggyu·Huijeong의 다중 에이전트 시스템용 계산·통신 구조 제안이 MSIT-MSRA 공동연구 지원에 선정됐다.
- 2026-02-01 · 「TACToC: Enabling Task-Adaptive Communication System with a Task-Describable Encoder」: ACM MobiCom 2026 (Austin, TX) 채택.
- 2025-12-08 · 「DECENTO: A New Scalable Interactive Live Streaming System via Control Plane Decentralization」: IEEE INFOCOM 2026 (Tokyo, Japan) 채택.
- 2025-12-08 · 「PAVE: Mitigating Non-Congestive Delay for Seamless Video Calls over NextG Mobile Networks」: IEEE INFOCOM 2026 채택.
- 2025-09-13 · 「End-to-End Coordination of RAN and Edge Server for Latency-Critical Inference Serving over Cellular Networks」: ACM CoNEXT 2025 채택.
- 2025-07-14 · 「QCON: Seamless QoE-Aware 5G Streaming via Multi-Connectivity」: USENIX NSDI 2026 (Renton, WA) 채택.
- 2025-07-14 · 「eXpressSFU: Toward Super-Scalable Video Conferencing with SmartNICs」: USENIX NSDI 2026 (Renton, WA) 채택.
- 2025-07-13 · 「AoRA: AI-on-RAN Architecture for Backhaul-free Edge Inference」: ACM SIGCOMM 2025 as a short version 채택.
- 2024-04-04 · 「Empilo: Realizing Immersive Mobile 3D Video Conferencing through Parameterized Communication」: ACM MobiSys 2025 채택.
- 2025-01-20 · 「A Certificate-centric Security Oracle for the Trustworthy Internet」: ACM WWW 2025 as a short version 채택.
- 2025-01-13 · 「nCTX: A Neural Network-Powered Lossless Compressive Transmission using Shared Information」: IEEE Transactions on Mobile Computing 게재 승인.
- 2024-12-19 · 「NeuroBalancer: Balancing System Frequencies with Punctual Laziness for Timely and Energy-efficient DNN Inferences」: IEEE Transactions on Mobile Computing 게재 승인.
- 2024-12-15 · 「Towards a Dynamic Future with Adaptable Computing and Network Convergence (ACNC)」: IEEE Network 게재 승인.
- 2024-12-13 · 「N-epitomizer: A Semantic Offloading Framework leveraging Essential Information for Timely Neural Network Inferences」: IEEE/ACM Transactions on Networking 게재 승인.
- 2024-09-29 · 「ADQ: Application-aware Socket Buffer Dequeueing for Mobile Devices」: IEEE CCNC 2025 채택.
- 2024-03-07 · 「CoActo: CoActive Neural Network Inference Offloading with Fine-grained and Concurrent Execution」: ACM MobiSys 2024 채택.
- 2023-12-01 · 「ExStream: A Delay-minimized Streaming System with Explicit Frame Queueing Delay Measurement」: INFOCOM 2024 채택.
- 2023-09-22 · 「ASPEN: Breaking Operator Barriers for Efficient Parallelization of Deep Neural Networks」: NeurIPS 2023 채택.
- 2023-07-26 · 「ENTRO: Tackling the Encoding and Networking Trade-off in Offloaded Video Analytics」: ACM Multimedia (MM) 2023 채택.
- 2023-05-18 · 「Converge: QoE-driven Multipath Video Conferencing over WebRTC」: ACM SIGCOMM 2023 채택.
- 2023-04-24 · 「An Empirical Study of 5G: Effect of Edge on Transport Protocol and Application Performance」: IEEE Transactions on Mobile Computing 게재 승인.
- 2023-04-04 · 「Towards Enabling Performance-Guaranteed Slice Management and Orchestration in 6G」: 2023 EuCNC & 6G Summit 채택.
- 2023-04-02 · 「Enabling Delay-Guaranteed Congestion Control with One-Bit Feedback in Cellular Networks」: IEEE/ACM Transactions on Networking 게재 승인.
- 2022-09-13 · 「Towards Enabling Performance-Guaranteed Networking in Next-Generation Cellular Networks」: IEEE Communications Magazine 게재 승인.
- 2022-06-30 · 「R-FEC: RL-based FEC Adjustment for better QoE in WebRTC」: ACM Multimedia (MM) 2022 채택.
- 2022-03-19 · 「mGEMM: Low-latency Convolution with Minimal Memory Overhead Optimized for Mobile Devices」: ACM MobiSys 2022 채택.
- 2022-01-05 · 「DeepVehicleSense: An Energy-efficient Transportation Mode Recognition Leveraging Staged Deep Learning over Sound Samples」: IEEE Transactions on Mobile Computing 게재 승인.

## 연락과 위치

- 교수 연구실: 서울대학교 301동 1006호[^prof][^eceprof]
- 연구 공간: 301동 1151-2호, 132동 402호(뉴미디어통신공동연구소)[^contact]
- 기관 전화: 02-880-1672[^ecelab][^prof]
- 주소: 서울특별시 관악구 관악로 1 서울대학교, 08826[^contact]
[^home]: NXC 홈페이지의 연구 방향, Cloud-Native AI-RAN Center 소개와 날짜 붙은 소식. <https://nxc.snu.ac.kr/home> (2026-10-26 관측).
[^prof]: 교수 소개, 경력·관심 분야·수상과 연락처. <https://nxc.snu.ac.kr/people/kyunghanlee> (2026-10-26 관측).
[^students]: Ph.D/MS Students 게시 명단과 연구 관심. <https://nxc.snu.ac.kr/people/students> (2026-10-26 관측).
[^alumni]: Alumni의 학위·참여 이력과 진로. <https://nxc.snu.ac.kr/people/alumni> (2026-10-26 관측).
[^pubs]: Selected Publications와 교신저자 기호 정의. <https://nxc.snu.ac.kr/publications> (2026-10-26 관측).
[^projects]: 진행·완료 과제와 미국·한국 등록특허 목록. <https://nxc.snu.ac.kr/projects-patents> (2026-10-26 관측).
[^contact]: 연구 공간과 기관 주소. <https://nxc.snu.ac.kr/contact> (2026-10-26 관측).
[^ecelab]: 학과의 연구실 상세 소개. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=75> (2026-10-26 관측).
[^eceprof]: 학과 교수 소개의 직급·학력·경력·연구 관심. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p841> (2026-10-26 관측).
[^p1]: H. Yu, M. Kim, J. Park, K. Lee, arXiv (MobiCom 2026 연결 판본) (온라인 2026-09-01). <https://arxiv.org/abs/2609.01338> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.01338>
[^p2]: J. Park 외, K. Lee, Advances in Neural Information Processing Systems 36 (2023). <https://doi.org/10.52202/075280-3002> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d899a31938c7838965b589d9b14a5ca6-Abstract-Conference.html>
[^p3]: S. Jin, S. Kim, S. Ha, K. Lee, Proceedings of the ACM on Networking 3, 1–23 (2025). <https://doi.org/10.1145/3768987> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/397970817_End-to-End_Coordination_of_RAN_and_Edge_Server_for_Latency-Critical_Inference_Serving_over_Cellular_Networks>
[^p4]: G. Lee 외, S. Bahk, 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26), 1721–1739 (2026). <https://www.usenix.org/conference/nsdi26/presentation/lee> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/nsdi26/presentation/lee>
[^p5]: W. Nam, S. Lee, J. Lee, K. Lee, IEEE Transactions on Mobile Computing 24, 5386–5399 (2025). <https://doi.org/10.1109/TMC.2025.3530950> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/388136743_nCTX_A_Neural_Network-Powered_Lossless_Compressive_Transmission_using_Shared_Information>
[^p6]: T. Tran 외, S. Ha, 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26), 2355–2369 (2026). <https://www.usenix.org/conference/nsdi26/presentation/tran> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/nsdi26/presentation/tran>
[^p7]: W. Hwang, Y. Kim, K. Lee, ACM SIGMETRICS Performance Evaluation Review 50, 11–13 (2023). <https://doi.org/10.1145/3595244.3595249> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/370356557_Augmenting_Epidemic_Models_with_Graph_Neural_Networks>
[^p8]: K. Bin 외, K. Lee, IEEE Transactions on Mobile Computing 24, 4339–4354 (2025). <https://doi.org/10.1109/TMC.2024.3524628> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/387653315_NeuroBalancer_Balancing_System_Frequencies_with_Punctual_Laziness_for_Timely_and_Energy-efficient_DNN_Inferences>

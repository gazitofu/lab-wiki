# 지능형 네트워크 구조 연구실 (Intelligent Network Architecture Lab, INA)

**KAIST 김재철AI대학원 · 한동수 교수**

- 분야: AI를 위한 컴퓨터 시스템(대규모 딥러닝 학습·추론 가속, 텐서 프로그램(딥러닝 모델의 행렬 연산 코드) 최적화), 시스템을 위한 AI(그래프 신경망·강화학습을 이용한 클라우드 자원 관리), AI 기반 영상 전송·처리, 데이터센터 네트워크 전송 기술, 이동통신망(5G·6G) 시스템, 신뢰 실행 환경 보안
- 대분야: 컴퓨팅·AI
- 태그: AI 시스템·인프라[^p2][^p1][^p3], 컴퓨터 네트워크[^p8][^home], 강화학습[^p4], 컴퓨터 비전[^p6][^p7]
- 홈페이지: <https://ina.kaist.ac.kr/>
- 근거와 출처: [INA 근거 페이지](ina-sources.md)

> 인터넷 서비스와 클라우드, 그리고 인공지능을 돌리는 컴퓨터 시스템을 더 빠르고 싸게 만드는 연구실이다. 값싼 GPU로도 거대한 AI 모델을 빨리 학습시키는 방법, 동영상을 AI로 선명하게 만들어 전송하는 기술, 데이터센터 네트워크의 효율을 높이는 기술을 실제로 만들어 검증한다.[^home][^projects]

## 무엇을 연구하나

연구실은 인터넷 서비스와 응용, 클라우드 인프라, 인공지능을 받치는 시스템에서 새로운 아이디어를 추구한다고 소개한다. 인터넷·클라우드 서비스의 진화와 새 하드웨어에서 생기는 문제를 찾아 실제 문제에 대한 해법을 설계·구현하는 것이 목표이며, 김재철AI대학원 소속이다.[^home] SIGCOMM, NSDI, OSDI 같은 최상위 시스템 학회에 논문 15편 이상을 냈다고 적는다.[^home]

첫 화면은 연구를 세 방향으로 나눈다. **AI·기계학습 시스템과 인프라**(대규모 신경망 학습 가속, 학습된 색인으로 DNA 서열 분석 가속, 그래프 신경망 기반 마이크로서비스 자동 확장, 대형 언어 모델 학습·추론 시스템), **AI 기반 미디어 전송**(신경망 화질 개선과 적응형 영상 스트리밍 결합, 대규모 화질 개선 가속, 화질 개선용 영상 코덱 최적화, 자동 화면 해설 생성), **지능형 네트워크 시스템과 시스템 보안**(신뢰 실행 환경과 네트워크 시스템 결합, 5G·6G 자원 효율, 데이터센터 혼잡 제어)이다.[^home] 과제 페이지에는 이 세 분야로 묶은 22개 연구 프로젝트가 있다.[^projects]

첫 번째 갈래는 **AI를 위한 시스템**이다. 동영상 딥러닝의 전처리 부담을 줄이는 프로그래밍 추상화를 SOSP에 발표했고,[^p1] 소비자용 GPU와 클라우드를 섞어 쓰는 환경에서 학습을 크게 빠르게 하는 방법,[^p2] 연산 수준까지 함께 최적화하는 텐서 프로그램 최적화기를 만들었다.[^p3] AI로 시스템을 다루는 쪽으로는 강화학습으로 마이크로서비스 과부하를 제어하고,[^p4] 학습된 색인으로 DNA 짧은 서열 정렬을 빠르게 했다.[^p5]

두 번째 갈래는 **AI 기반 영상 전송**이다. 실시간 방송 영상을 서버에서 신경망으로 선명하게 만드는 비용을 크게 줄였고,[^p6] 이미지 복원 신경망의 계산량을 줄이는 압축 방식을 만들었다.[^p7]

세 번째 갈래는 **데이터센터 네트워크**다. 기존 전송 방식과 함께 쓰며 점진적으로 도입할 수 있는 크레디트(송신 허가) 기반 전송 방식을 만들었다.[^p8]

## 주요 연구 주제

### 1. AI·기계학습 시스템과 인프라

동영상 딥러닝 전처리 추상화, 멀티 클러스터 학습 가속, 텐서 프로그램 최적화, 마이크로서비스 과부하 제어, 학습 색인 DNA 정렬.[^p1][^p2][^p3][^p4][^p5] 대표 논문 1–5.

### 2. AI 기반 미디어 전송

대규모 실시간 영상 화질 개선, 복원 인식 이미지 압축.[^p6][^p7] 대표 논문 6, 7.

### 3. 데이터센터 네트워크

유연한 크레디트 기반 전송.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 교수가 마지막 저자인 것에서 세 연구 방향을 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [SAND: A New Programming Abstraction for Video-based Deep Learning](https://doi.org/10.1145/3731569.3764847) · SOSP 2025 | 동영상으로 학습하는 딥러닝은 압축된 영상을 풀고 다듬는 전처리가 복잡하고 GPU 학습보다 오래 걸린다. 전처리 단계를 가상 객체로 감싸는 추상화와 객체 재사용 관리로 GPU 활용률을 CPU·GPU 기준 방식보다 최대 12.3배·2.9배 높이고, 전처리 코드를 수백·수천 줄에서 10줄 미만으로 줄였다.[^p1] | 1저자 Juncheol Ye, 마지막 저자 한동수 |
| 2 | 2024 | [Accelerating Model Training in Multi-cluster Environments with Consumer-grade GPUs](https://doi.org/10.1145/3651890.3672228) · ACM SIGCOMM 2024 | 학계처럼 소비자용 GPU와 제한된 클라우드 GPU만 가진 곳에서 여러 클러스터에 걸쳐 학습하면 성능이 크게 떨어진다. 캐시를 고려한 기울기(학습 중 모델을 고치는 방향 값) 압축, 필요한 부분만 갱신하는 CPU 기반 희소 최적화기 등을 상황에 맞게 조합하는 StellaTrain으로 클러스터 간 학습을 PyTorch DDP보다 최대 104배 빠르게 했다.[^p2] | 1저자 Hwijoon Lim, 마지막 저자 한동수 |
| 3 | 2026 | [Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation](https://doi.org/10.1145/3779212.3790240) · ASPLOS 2026 | 기존 텐서 프로그램 최적화기는 연산 그래프 수준과 연산자 내부 스케줄링을 따로 다뤄, FlashAttention 같은 수작업 커널의 최적화를 자동으로 찾지 못한다. 대수적 동치, 메모리 입출력, 연산 배치를 함께 최적화하는 Trinity로 Transformer 변형들에서 TensorRT보다 최대 2.09배 빨라졌다.[^p3] | 1저자 Jaehyeong Park, 마지막 저자 한동수 |
| 4 | 2024 | [TopFull: An Adaptive Top-Down Overload Control for SLO-Oriented Microservices](https://doi.org/10.1145/3651890.3672253) · ACM SIGCOMM 2024 | 클라우드 응용을 이루는 마이크로서비스가 과부하에 빠지지 않도록, 입구에서 API별로 받아들일 요청량을 강화학습 기반 제어기로 조절하는 TopFull을 만들었다. 목표 응답 시간을 지키며 처리한 요청량이 기존 방법보다 1.82–2.26배 많았다.[^p4] | 1저자 Jinwoo Park, 마지막 저자 한동수 |
| 5 | 2022 | [BWA-MEME: BWA-MEM emulated with a machine learning approach](https://doi.org/10.1093/bioinformatics/btac137) · Bioinformatics | 차세대 염기서열 분석에서 짧은 서열을 기준 DNA에 정렬하는 첫 단계는 메모리 접근이 많아 느리다. 학습된 색인(데이터 위치를 예측하는 모델)을 처음으로 실제 정렬 소프트웨어에 적용해, 결과는 그대로 두고 이 첫 단계(시딩)의 처리량을 기존 BWA-MEM2보다 최대 3.45배 높였다.[^p5] | 1저자 Youngmok Jung, 마지막 저자 한동수 |
| 6 | 2022 | [NeuroScaler: Neural Video Enhancement at Scale](https://pure.kaist.ac.kr/en/publications/neuroscaler-neural-video-enhancement-at-scale/) · ACM SIGCOMM 2022 | 실시간 방송 영상의 화질은 방송자의 업로드 속도에 묶인다. 서버에서 신경망으로 해상도를 높이는 방식을 대규모로 쓸 수 있도록 초해상도·인코딩·GPU 전환 비용을 줄이는 알고리즘과 자원 스케줄러를 만들어, 공용 클라우드에서 비용을 매 프레임을 처리하는 방식보다 22.3배, 일부 프레임만 처리하는 방식보다 3.0–11.1배 줄였다.[^p6] | 1저자 Hyunho Yeo, 마지막 저자 한동수 |
| 7 | 2023 | [AccelIR: Task-aware Image Compression for Accelerating Neural Restoration](https://doi.org/10.1109/cvpr52729.2023.01747) · CVPR 2023 | 이미지 복원 신경망(초해상도, 잡음 제거, 흐림 제거)은 계산이 무겁다. 복원 품질에 주는 영향에 따라 이미지 블록별 압축 수준을 정하는 AccelIR로 같은 화질과 파일 크기를 유지하면서 가벼운 복원 신경망을 쓸 수 있게 해, 계산량을 평균 29–49% 줄였다.[^p7] | 1저자 Juncheol Ye, 마지막 저자 한동수 |
| 8 | 2023 | [FlexPass: A Case for Flexible Credit-based Transport for Datacenter Networks](https://doi.org/10.1145/3552326.3587453) · EuroSys 2023 | 데이터센터에서 송신자마다 대역폭을 미리 배정하는 크레디트 기반 전송은 모든 장비를 통제할 수 있어야 해 실제 도입이 어렵다. 기존 전송과 함께 쓰며 점진적으로 도입할 수 있게 설계한 FlexPass로 기존 트래픽보다 흐름 완료 시간을 최대 44% 줄였다.[^p8] | 1저자 Hwijoon Lim, 마지막 저자 한동수 |

## 교수와 전문 분야

한동수 교수는 미국 카네기멜런대 컴퓨터과학과에서 박사(2012)를 받았고 KAIST 김재철AI대학원 교수다. 연구 관심사를 네트워크·클라우드 시스템 설계, 시스템을 위한 AI, AI를 위한 시스템으로 적는다.[^members] 랩 소식에 따르면 2025년 APNet 기조연설을 맡았다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **AI 학습·추론 시스템과 컴파일러 최적화**.[^p1][^p2][^p3]
- **AI를 이용한 클라우드·영상·생명정보 시스템**.[^p4][^p5][^p6][^p7]
- **데이터센터 네트워크 전송**.[^p8]

## 응용 분야

대표 논문과 프로젝트로 보면 대형 AI 모델의 학습·서빙 비용 절감, 클라우드 서비스 안정성, 고화질 영상 스트리밍, 유전체 분석 가속, 데이터센터 네트워크에 닿아 있다.[^p1][^p2][^p5][^p6][^projects] 졸업생은 메타, 엔비디아, 삼성전자, SAP 같은 기업과 인하대·성신여대 교수 등으로 진출했다고 랩이 적는다.[^members]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다. 괄호는 랩이 적은 소속(학과·연구단)이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Jeonghun Lee | 박사후연구원 (Information & Electronics Research Institute) |  |
| Wooseung Nam | 박사후연구원 (Information & Electronics Research Institute) |  |
| Juncheol Ye | 박사후연구원 (InnoCORE-LLM) | 1, 2, 6, 7 |
| Insup Lee | 박사후연구원 (InnoCORE-LLM) |  |
| Yunheon Lee | 박사과정 (School of Electrical Engineering) |  |
| Jaehyeong Park | 박사과정 (School of Electrical Engineering) | 3, 4 |
| Jinyeong Lim | 박사과정 (School of Electrical Engineering) |  |
| Taehyun Kim | 박사과정 (Graduate School of AI) |  |
| Taehoon Kim | 박사과정 (Graduate School of AI) |  |
| Seyeon Lee | 박사과정 (Graduate School of AI) |  |
| Sirui Li | 박사과정 (Graduate School of AI) |  |
| Seungkook Lee | 석사과정 (School of Electrical Engineering) | 1 |
| Youngchan Kim | 석사과정 (School of Electrical Engineering) | 3 |
| Seunggeun Cho | 석사과정 (School of Electrical Engineering) |  |
| Jihyuk Lee | 석사과정 (Graduate School of AI) | 1 |
| Sanmaru Um | 석사과정 (Graduate School of AI) |  |
| Jaeung Choi | 석사과정 (Graduate School of AI) |  |
| Junhyeong Jeon | 석사과정 (Graduate School of AI) |  |
| Vincent Alec Baguio | 석사과정 (Graduate School of AI) |  |
| Wonjun Song | 석사과정 (Graduate School of AI) |  |

## 졸업생

랩 구성원 페이지 졸업생 구간의 이름, 학위·연도, 랩이 적은 현재 소속이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Le Tu Ngoc Minh |  | Master Student, School of Electrical Engineering |
| Jinwoo Park | 박사 (2025) | System Software Engineer at MangoBoost |
| Seunghwan Noh |  | Republic of Korea Air Force |
| Hwijoon Lim | 박사 (2024) | Research Scientist at Meta |
| Jaehong Kim | 박사 (2024) | Assistant Professor at Inha University |
| Uitaek Hong | 석사 (2024) | ML Engineer at maum.ai |
| Youngmok Jung | 박사 (2024) | AI research scientist at Genome Insight |
| Yechan Kim | 석사 (2023) | AI DevTech Engineer at NVIDIA |
| Hyunho Yeo | 박사 (2023) | Software Engineer at Meta (MTIA SW) |
| Jeongmin Kim | 박사 (2023) | Network Group Manager at PiLab |
| Juhyeng Han | 박사 (2022) | Software engineer at SAP Labs Korea |
| Joonhyuk Lee | 석사 (2021) |  |
| Byungkwon Choi | 박사 (2021) | Staff engineer at Samsung Electronics Mobile Division |
| Seongmin Kim | 박사 (2019) | Assistant Professor at Sungshin Women’s University |
| Hejing Li | 석사 (2020) | Ph.D. student at Max Planck Institute |
| Quang Nguyen Ngoc | 석사 (2019) | Software engineer at CyberLogitec |
| Daeyang Cho | 석사 (2020) | Software engineer at KLleon |
| Inho Cho | 석사 (2018) | Ph.D. student at MIT EECS |
| Byeoksan Lee | 석사 (2017) | Software engineer at LINE Plus |
| Woohyun Choi | 석사 (2017) | Software engineer at TMaxSoft |
| Changhyun Lee | 박사 (2015) | Researcher at ETRI |
| Keon Jang | 박사후연구원 | Staff engineer at Rubrik |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021년 이후 논문이다. 2027년 표기(NSDI 게재 예정) 1편을 포함한다.[^papers]

**2027**

- Yunheon Lee\*, Jaehong Kim\*, and Dongsu Han. "FlaME: MAC Scheduling at Scale in Virtualized Radio Access Network". *24th USENIX Symposium on Networked Systems Design and Implementation (NSDI) (To appear) 2027*.

**2026**

- Taehoon Kim, Seunggeun Cho, and Dongsu Han. "Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation". *The 40th Annual Conference on Neural Information Processing Systems (To appear) Dec 2026*.
- Le Tu Ngoc Minh\*, Jinyeong Lim\*, and Dongsu Han. "ProtoKV: Streaming Video Understanding under Delayed Query with Summary-State Memory". *the 43rd International Conference on Machine Learning Jul 2026*.
- Seongjin Cha, Gyuwan Kim, Dongsu Han, Tao Yang, and Insu Han. "KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem". *the 43rd International Conference on Machine Learning Jul 2026*.
- Jaehyeong Park, Youngchan Kim, Haechan An, Gieun Jeong, Jeehoon Kang, and Dongsu Han. "Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation". *the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems Mar 2026*.
- Yunheon Lee, Juncheol Ye, Jaehong Kim, and Dongsu Han. "NerVast: Compression-Efficient Scaling of Implicit Neural Video Representations via Scene-based Parameter-sharing". *the IEEE/CVF Winter Conference on Applications of Computer Vision Mar 2026*.
- Seyeon Lee, Juncheol Ye, Jaehong Kim, and Dongsu Han. "Neural-Centric Video Processing Pipeline for Unified Multi-Task Inference". *the IEEE/CVF Conference on Computer Vision and Pattern Recognition Mar 2026*.
- Jaehong Kim, Joon Ha Kim, Yunheon Lee, and Dongsu Han. "BlenDR: Bandwidth-efficient RGB-D Representation and Delivery for Live 3D Video Streaming". *In Proceedings of the 24th Annual International Conference on Mobile Systems, Applications and Services Mar 2026*.
- Jaber Daneshamooz, Eugene Vuong, Alagappan Ramanathan, Manni Moghimi, Haarika Manda, Satyam Kumar, Snithik Thode, Satyandra Guthula, Sylee Beltiukov, Dongsu Han, Tarun Mangla, Sangeetha Abdu Jyothi, Walter Willinger, and Arpit Gupta. "Pramana: A Composable, Domain-Specific Backend for Empirical Networking Research". *the 25th ACM Workshop on Hot Topics in Networks (To appear) Nov 2026*.

**2025**

- Juncheol Ye, Seungkook Lee, Hwijoon Lim, JiHyuk Lee, Uitaek Hong, Youngjin Kwon, and Dongsu Han. "SAND: A New Programming Abstraction for Video-based Deep Learning". *the 31st Symposium on Operating Systems Principles Oct 2025*.
- Jinwoo Park, Seunggeun Cho, and Dongsu Han. "SpecEdge: Scalable Edge-Assisted Serving Framework for Interactive LLMs". *The 39th Annual Conference on Neural Information Processing Systems Dec 2025*.
- Sagar Patel, Dongsu Han, Nina Narodytska, and Sangeetha Abdu Jyothi. "Agua: A Concept-Based Explainer for Systems". *the ACM SIGCOMM 2025 conference Sep 2025*.
- Jaehyeong Park, Juncheol Ye, Seungkook Lee, Hyun W. Ka, and Dongsu Han. "NarrAD: Automatic Generation of Audio Descriptions for Movies with Rich Narrative Context". *the IEEE/CVF Winter Conference on Applications of Computer Vision Mar 2025*.
- Qiang Su, Zhixiong Niu, Ran Shu, Peng Cheng, Yongqiang Xiong, Dongsu Han, Chun Jason Xue, and Hong Xu. "Low-Overhead Intra-Host Container Communication With Hardware Offloading". *IEEE/ACM Transactions on Networking Jan 2025*.
- Jinyeong Lim, Juncheol Ye, Jaehong Kim, Hwijoon Lim, Hyunho Yeo, Junhyeok Jang, Myoungsoo Jung, and Dongsu Han. "Efficient Disaggregated Cloud Storage for Cold Videos with Neural Enhancement". *IEEE Micro Apr 2025*.
- Alagappan Ramanathan, Eunju Kang, Dongsu Han, and Sangeetha Abdu Jyothi. "Towards an Agentic Workflow for Internet Measurement Research". *the 24th ACM Workshop on Hot Topics in Networks Nov 2025*.
- Jihyuk Lee, Dongsu Han, and Jaehong Kim. "Presto: Hybrid CPU-GPU Preprocessing Framework for Video-based AI Inference System". *the 3rd International Workshop on Networked AI Systems Jun 2025*.
- Gyuyeong Kim, and Dongsu Han. "A Memory Pool Allocator for eBPF Applications". *the 3rd Workshop on eBPF and Kernel Extensions Jun 2025*.

**2024**

- Hwijoon Lim, Juncheol Ye, Sangeetha Abdu Jyothi, and Dongsu Han. "Accelerating Model Training in Multi-cluster Environments with Consumer-grade GPUs". *the ACM SIGCOMM 2024 conference on SIGCOMM Aug 2024*.
- Jinwoo Park, Jaehyeong Park, Youngmok Jung, Hwijoon Lim, Hyunho Yeo, and Dongsu Han. "TopFull: An Adaptive Top-Down Overload Control for SLO-Oriented Microservices". *the ACM SIGCOMM 2024 conference on SIGCOMM Aug 2024*.
- Yechan Kim\*, Hwijoon Lim\*, and Dongsu Han. "Scaling Beyond the GPU Memory Limit for Large Mixture-of-Experts Model Training". *the 41st International Conference on Machine Learning Jul 2024*.
- Jinwoo Park, Byungkwon Choi, Chunghan Lee, and Dongsu Han. "Graph Neural Network-based SLO-aware Proactive Resource Autoscaling Framework for Microservices". *IEEE/ACM Transactions on Networking Aug 2024*.
- Sagar Patel, Dongsu Han, Nina Narodytska, and Sangeetha Abdu Jyothi. "Toward Trustworthy Learning-Enabled Systems with Concept-Based Explanations". *the 16th ACM Workshop on Hot Topics in Networks Nov 2024*.

**2023**

- Hwijoon Lim, Jaehong Kim, Inho Cho, Keon Jang, Wei Bai, and Dongsu Han. "FlexPass: A Case for Flexible Credit-based Transport for Datacenter Networks". *the Eighteenth European Conference on Computer Systems May 2023*.
- Juncheol Ye, Hyunho Yeo, Jinwoo Park, and Dongsu Han. "AccelIR: Task-aware Image Compression for Accelerating Neural Restoration". *the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Jun 2023*.
- Jinyeong Lim, Juncheol Ye, Jaehong Kim, Hwijoon Lim, Hyunho Yeo, and Dongsu Han. "Neural Cloud Storage: Innovative Cloud Storage Solution for Cold Video". *the 15th ACM Workshop on Hot Topics in Storage and File Systems Jul 2023*.
- Uitaek Hong, Hwijoon Lim, Hyunho Yeo, Jinwoo Park, and Dongsu Han. "SAND: A Storage Abstraction for Video-based Deep Learning". *the 15th ACM Workshop on Hot Topics in Storage and File Systems Jul 2023*.

**2022**

- Hyunho Yeo, Hwijoon Lim, Jaehong Kim, Youngmok Jung, Juncheol Ye, and Dongsu Han. "NeuroScaler: Neural Video Enhancement at Scale". *the ACM SIGCOMM 2022 conference on SIGCOMM Aug 2022*.
- Hwijoon Lim, Yechan Kim, Sukmin Yun, Jinwoo Shin, and Dongsu Han. "TSPipe: Learn from Teacher Faster with Pipelines". *the 39th International Conference on Machine Learning Jul 2022*.
- Youngmok Jung, and Dongsu Han. "BWA-MEME: BWA-MEM emulated with a machine learning approach". *Bioinformatics Mar 2022*.
- Jaehong Kim, Yunheon Lee, Hwijoon Lim, Youngmok Jung, Song Min Kim, and Dongsu Han. "OutRAN: Co-Optimizing for Flow Completion Time in Radio Access Network". *the 18th International Conference on Emerging Networking EXperiments and Technologies Mar 2022*.
- Qiang Su, Chuanwen Wang, Zhixiong Niu, Ran Shu, Peng Cheng, Yongqiang Xiong, Dongsu Han, Chun Jason Xue, and Hong Xu. "PipeDevice: A Hardware-Software Co-Design Approach to Intra-Host Container Communication". *the 18th International Conference on emerging Networking EXperiments and Technologies Dec 2022*.
- Juhyeng Han, Insu Yun, Seongmin Kim, Taesoo Kim, Sooel Son, and Dongsu Han. "Scalable and Secure Virtualization of HSM with ScaleTrust". *IEEE/ACM Transactions on Networking Nov 2022*.

**2021**

- Jinwoo Park\*, Byungkwon Choi\*, Chunghan Lee, and Dongsu Han. "GRAF: A Graph Neural Network Based Proactive Resource Allocation Framework for SLO-Oriented Microservices". *the 17th International Conference on Emerging Networking EXperiments and Technologies Nov 2021*.
- Byungkwon Choi, Jinwoo Park, Chunghan Lee, and Dongsu Han. "PHPA: A Proactive Autoscaling Framework for Microservice Chain". *5th Asia-Pacific Workshop on Networking (APNet 2021) Nov 2021*.
- Hwijoon Lim, Wei Bai, Yibo Zhu, Youngmok Jung, and Dongsu Han. "Towards Timeout-Less Transport in Commodity Datacenter Networks". *the Sixteenth European Conference on Computer Systems Nov 2021*.

## 연구 프로젝트

랩 프로젝트 페이지의 프로젝트 이름과 한 줄 설명이다.[^projects]

- SAND: A New Programming Abstraction for Video-based Deep Learning
- SpecEdge: A scalable edge-assisted framework that achieves enhanced cost efficiency and reduced latency
- StellaTrain: A holistic framework that achieves near-optimal training speeds in multi-cloud environments.
- TopFull: An Adaptive Top-Down Overload Control for Microservices.
- ES-MoE: Efficient scaling of Mixture-of-Experts training on a limited number of GPUs.
- TSPipe: Train knowledge distillation (KD) and self-supervised learning (SSL) faster with pipelines
- BWA-MEME: BWA-MEM emulated with a machine learning approach
- GRAF: A GNN-based proactive resource allocation framework for SLO-oriented microservices.
- NarrAD: AI-based system for generating barrier-free audio descriptions
- AccelIR: Accelerate image-restoration for image compression
- NeuroScaler: Enable neural-enhanced video streaming at scale
- NEMO: Run real-time video super-resolution on commercial smartphones
- LiveNAS: Stream high-quality live videos even when the network becomes congested
- NAS: Watch videos in high-quality even when the network becomes congested
- BlenDR: Bandwidth-efficient RGB-D Representation and Delivery for Live 3D Video Streaming
- FlexPass: Flexible and practical proactive transport protocol for datacenter networks
- OutRAN: A cell-scale flow scheduler designed for Radio Access Networks
- TLT: Timeout-less Transport in Commodity Datacenter Networks
- APPx: Automatically generates acceleration proxies for mobile apps
- TEE Systems: Security-enhanced network system by leveraging trusted execution environment (TEE)
- DFC: High-Performance String Matching Algorithm that accelerates network middlebox applications
- ExpressPass: Credit-Scheduled Delay-Bounded Congestion Control for Datacenters

## 소식

랩 첫 화면의 최근 소식이다.[^home]

- 2026 Mar · Our paper titled “BlenDR: Bandwidth-efficient RGB-D Representation and Delivery for Live 3D Video Streaming” has been accepted to MobiSys’26. Congratulations!
- 2026 Mar · Our paper titled “Neural-Centric Video Processing Pipeline for Unified Multi-Task Inference” has been accepted to CVPR’26. Congratulations!
- 2026 Feb · Our paper titled “NerVast: Compression-Efficient Scaling of Implicit Neural Video Representations via Scene-based Parameter-sharing” has been published to WACV’26. Congratulations!
- 2025 Nov · Our paper titled “Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation” has been accepted to ASPLOS’26. Congratulations!
- 2025 Sep · Our paper titled “SpecEdge: Scalable Edge-Assisted Serving Framework for Interactive LLMs” has been accepted as an spotlight paper to NeurIPS’25. Congratulations!
- 2025 Sep · Our paper titled “Towards an Agentic Workflow for Internet Measurement Research”, in collaboration with Sangeetha Jyothi, has been accepted to HotNets’25. Congratulations!
- 2025 Jul · Dongsu Han will be giving a Keynote at APNet 2025.
- 2025 Jul · Our paper titled “SAND: A New Programming Abstraction for Video-based Deep Learning” has been accepted to SOSP’25. Congratulations!
- 2025 Jun · Our paper titled “Agua: A Concept-Based Explainer for Learning-Enabled Systems”, in collaboration with Sangeetha Jyothi, has been accepted to SIGCOMM’25. Congratulations!
- 2025 Jan · Our paper titled “NarrAD: Automatic Generation of Audio Descriptions for Movies with Rich Narrative Context” has been accepted as an oral paper at WACV’25. Congratulations!

## 연락과 위치

- 교수 위치: KAIST 서울 AI 허브(서울 서초구 우면동 141)[^members]

[^home]: INA 누리집 첫 화면 <https://ina.kaist.ac.kr/> (2026-10-19 열람)
[^members]: INA 구성원 페이지 <https://ina.kaist.ac.kr/team/> (2026-10-19 열람)
[^papers]: INA 논문 목록 <https://ina.kaist.ac.kr/publications/> (2026-10-19 열람)
[^projects]: INA 프로젝트 페이지 <https://ina.kaist.ac.kr/projects/> (2026-10-19 열람)
[^p1]: J. Ye 외, D. Han, Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles, 589-605 (온라인 2025-10-12). <https://doi.org/10.1145/3731569.3764847> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Lim, J. Ye, S. A. Jyothi, D. Han, Proceedings of the ACM SIGCOMM 2024 Conference, 707-720 (온라인 2024-08-04). <https://doi.org/10.1145/3651890.3672228> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Park 외, D. Han, Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2, 2079-2107 (온라인 2026-03-22). <https://doi.org/10.1145/3779212.3790240> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Park 외, D. Han, Proceedings of the ACM SIGCOMM 2024 Conference, 876-890 (온라인 2024-08-04). <https://doi.org/10.1145/3651890.3672253> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y. Jung, D. Han, Bioinformatics 38, 2404-2413 (온라인 2022-03-07). <https://doi.org/10.1093/bioinformatics/btac137> 초록 기준.
[^p6]: H. Yeo 외, D. Han, ACM SIGCOMM 2022 (랩 표기). <https://pure.kaist.ac.kr/en/publications/neuroscaler-neural-video-enhancement-at-scale/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p7]: J. Ye, H. Yeo, J. Park, D. Han, 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 18216-18226 (2023). <https://doi.org/10.1109/cvpr52729.2023.01747> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: H. Lim 외, D. Han, Proceedings of the Eighteenth European Conference on Computer Systems, 606-622 (온라인 2023-05-08). <https://doi.org/10.1145/3552326.3587453> 초록 기준(Semantic Scholar 등록 초록).

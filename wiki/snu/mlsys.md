# 머신러닝 시스템 연구실 (Machine Learning Systems Lab)

**서울대학교 첨단융합학부 차세대지능형반도체전공, 공과대학 전기·정보공학부, 대학원 협동과정 인공지능전공 · 서지원 부교수**

- 분야: 머신러닝 학습·추론 시스템, 언어 모델 추론의 계산 배치, 모델 양자화, 모델 보안·검사, 그래프 처리
- 대분야: 컴퓨팅·AI
- 태그: AI 시스템·인프라[^home][^ece], 대형 언어 모델[^p3][^p4], 컴퓨터 비전[^p1][^p5], 모델 경량화·양자화[^p1], AI·기계학습 보안·프라이버시[^research]
- 홈페이지: <https://mlsys.snu.ac.kr/home>
- 근거와 출처: [머신러닝 시스템 연구실 근거 페이지](mlsys-sources.md)

> 인공지능 모델을 학습시키고 실행하는 컴퓨터 시스템의 속도·자원 사용·운영 방식과 보안을 연구한다. 모델의 계산 순서를 바꾸고 수를 표현하는 방식을 조절해, 주어진 장비에서 학습과 추론을 수행하는 방법을 개발한다.[^home][^ece]

## 무엇을 연구하나

머신러닝(자료에서 규칙을 학습하는 계산 방법) 모델이 실제로 작동하려면 모델의 계산뿐 아니라 데이터를 옮기고 여러 장비에 일을 나누는 시스템이 필요하다. 이 연구실은 학습(자료를 이용해 모델의 내부 값을 조정하는 과정)과 추론(학습한 모델로 입력에 대한 결과를 계산하는 과정)을 실행하는 시스템을 연구한다. 프로그램을 작성하기 쉬운지, 처리 규모를 늘릴 수 있는지, 운영하기 편한지, 실행 성능이 어떤지를 함께 다룬다.[^home][^ece]

한 갈래는 대규모 언어 모델(LLM, Large Language Model, 많은 언어 자료로 학습해 글을 처리하고 생성하는 모델)의 실행이다. 여러 GPU(Graphics Processing Unit, 다수의 계산을 병렬로 처리하는 프로세서)에 작업을 나누고, 어떤 계산을 어느 시점에 실행할지 정하는 스케줄링을 연구한다. 최근에는 추측 디코딩(작은 모델이 미리 제안한 출력 조각을 목표 모델로 검증하는 생성 방법)의 검증량을 조절하고, 추측 계산을 통상 계산과 병행하는 시스템을 발표했다.[^home][^p3][^p4]

다른 갈래는 속도와 정확도의 관계다. 양자화(모델이 사용하는 수를 정해진 유한한 값의 집합으로 표현하는 방법)를 통해 저장과 계산에 쓰는 비트(bit, 이진 정보의 단위)를 조절한다. FlexiQ는 시각 모델의 일부 계산에 적용하는 정밀도를 실행 중 바꾸고, DASH-Q는 학습이 끝난 언어 모델을 양자화할 때 보정 자료로부터 얻는 민감도 추정의 잡음을 다룬다. 영상의 필요한 영역에만 초해상도(입력 영상에서 해상도를 높인 영상을 추정하는 기술)를 적용하고 계산 깊이를 조절하는 공동연구도 수행했다.[^p1][^p2][^p5]

모델이 잘못된 판단을 하도록 유도하는 적대적 입력(모델의 오작동을 유도하도록 만든 입력)을 생성하고 감지하는 방법도 연구한다. 그래프(대상과 그 관계를 점과 연결선으로 표현한 자료)의 연결이 확률로 주어질 때, 여러 가능한 그래프를 표본으로 만들어 분석하는 계산을 효율적으로 처리하는 연구도 소개한다. 첫 화면은 에이전트 AI(목표에 따라 작업을 선택하고 수행하는 인공지능) 시스템과 Physical AI(물리적 환경에서 인식하고 행동하는 인공지능) 시스템의 설계·최적화도 연구 주제로 제시한다.[^research][^home]

## 주요 연구 주제

### 언어 모델 추론의 계산 배치

언어 모델이 다음 토큰(모델이 글을 나누어 처리하는 단위)을 계산할 때, 추측한 출력이 받아들여질 가능성과 장비의 자원 사용을 함께 고려한다. Speculative Verification은 보조 모델을 이용해 검증할 길이를 조절한다. Spexis는 모델의 계산 단계를 나누는 파이프라인 병렬화와 한 계산을 나누는 텐서 병렬화에 추측 계산을 결합하며, 앞으로의 추측 품질과 메모리 사용을 예측해 실행 순서를 정한다.[^p3][^p4]

### 양자화와 실행 중 품질 조절

FlexiQ는 시각 모델에서 특징 채널(모델이 추출한 특징을 구분해 저장하는 갈래)의 값 범위를 고려해 계산 정밀도를 정하고, 낮은 비트 수를 사용하는 채널의 비율을 실행 중 바꾼다. DASH-Q는 보정 자료(모델 변환 과정의 오차를 추정하고 조절하는 데 쓰는 자료)로부터 수치 변화에 대한 민감도를 추정하고 반복적으로 오차를 보정한다. 전자는 실행 중 부하 변화에 대응하고, 후자는 낮은 비트 수로 모델을 표현할 때의 추정 안정성을 다룬다.[^p1][^p2]

### 시각 모델의 동적 실행

초해상도를 물체 검출(영상에서 물체의 종류와 위치를 찾는 기술)과 함께 쓸 때 필요한 계산량을 연구한다. DQC-SR(Dynamic Quality Control Super-Resolution)은 관심 영역에만 영상 복원을 적용하고, 같은 변수를 공유하는 계산 구조와 중간 단계에서 계산을 끝내는 구조를 결합한다. 관심 영역의 수에 따라 처리 깊이를 바꾸어 영상 품질과 실행량을 조절한다.[^p5]

### 모델 보안과 그래프 처리

연구 소개는 딥러닝(여러 층의 신경망으로 자료의 표현을 학습하는 방법) 모델을 속이는 입력의 효율적인 생성과 감지를 주요 주제로 든다. 또 연결이 확률로 주어지는 그래프에서 표본 그래프들을 압축하는 등 분석에 필요한 자원 사용을 줄이는 방법을 다룬다.[^research]

## 대표 논문

서울대 부임 연도인 2025년 이후 논문에서 언어 모델 추론, 양자화, 시각 모델의 실행, 계산 자원 배분을 보여 주는 6편을 골랐다. 표의 연도와 제목은 연결한 판본을 따른다. arXiv는 정식 논문집과 구분되는 사전 공개 저장소이며, 아래 arXiv 항목은 그 판본의 초록으로 설명했다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.[^prof]

| 번호 | 연도 | 논문과 발표처 | 쉽게 말하면 | 교수의 역할 |
|---|---|---|---|---|
| 1 | 2025 | [FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks](https://arxiv.org/abs/2510.02822) · arXiv 사전 공개본, EuroSys 2026 출판 예정 표기 | 시각 모델에서 일부 특징 채널에 낮은 비트 수의 계산을 적용하고, 그 비율을 실행 중 바꾸는 방법이다. 값 범위가 작은 채널을 선택하고 양자화 오차를 줄이는 방법을 결합한다. 자체 NPU(Neural Processing Unit, 신경망 계산용 프로세서)와 GPU에서 실행기를 구현해, 변하는 추론 작업량에 맞춰 정확도와 지연시간을 조절하는 방식을 평가했다.[^p1] | 마지막 저자 |
| 2 | 2026 | [Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate](https://arxiv.org/abs/2604.13806) · arXiv 사전 공개본 v2 | 학습이 끝난 언어 모델을 낮은 비트 수로 바꿀 때 보정 자료가 적으면 민감도 추정에 잡음이 생길 수 있다. DASH-Q는 변수마다의 민감도를 개별적으로 근사하고, 가중 최소제곱법(오차마다 가중치를 주어 오차 제곱의 합을 줄이는 방법)을 반복 적용한다. 이를 통해 양자화 과정에서 표본 잡음의 영향을 다루며 모델의 중요한 특징을 보존하려 한다.[^p2] | 마지막 저자 |
| 3 | 2026 | [Speculative Verification: Exploiting Information Gain for Speculative Decoding](https://doi.org/10.18653/v1/2026.findings-acl.1809) · ACL Findings | 작은 모델이 미리 만든 토큰을 큰 모델로 검증하는 과정에서, 거절될 토큰을 확인하느라 드는 계산을 줄이는 방법이다. 작은 보조 모델의 출력 분포(출력 후보별 가능성을 나타낸 값)에서 얻는 정보를 이용해 추측의 정확성을 예상하고 검증 길이를 조절한다. 여러 언어 처리 과제와 모델 조합에서 검증했으며, 초록은 큰 배치(한 번에 묶어 처리하는 입력들의 집합)에서 기존 추측 디코딩 대비 평균 1.4배 속도 향상을 보고한다.[^p3] | 마지막 저자 |
| 4 | 2026 | [Spexis: Speculative Lookahead Scheduling for LLM Inference](https://arxiv.org/abs/2609.34370) · arXiv 사전 공개본, EMNLP 2026 main 표기 | 여러 GPU에서 언어 모델을 실행하면서 추측 계산을 통상 계산과 병행하는 시스템이다. 이전 계산의 정보를 저장하는 KV 캐시(Key-Value cache)의 사용량을 늘리지 않으면서 병렬 계산의 축을 추가한다. 앞으로의 추측 품질과 메모리 부담을 예상해 불필요한 추측, 캐시 제거와 재계산을 줄인다. 초록은 파이프라인·텐서 병렬화의 최적 조합을 쓴 기준 시스템보다 최대 34%의 속도 향상을 보고한다.[^p4] | 마지막 저자 |
| 5 | 2025 | [Efficient Image Super-Resolution Using Dynamic Quality Control With Recursive Model Structures](https://doi.org/10.1109/ACCESS.2025.3582604) · IEEE Access | 물체를 검출하기 전에 영상의 해상도를 높이면 계산량이 늘어난다. 이 연구는 필요한 영역에만 초해상도를 적용하고, 같은 변수를 공유하는 반복 구조와 계산을 중간에 끝내는 구조를 함께 사용한다. 관심 영역의 수에 따라 계산 깊이를 바꾸며 장치에서 실시간 추론을 수행하도록 했다. 번호판 인식 상황을 이용한 평가로 방법의 효과를 보였다.[^p5] | 7명 중 5번째 저자. 교신저자는 Yongjun Park |
| 6 | 2025 | [PIM-CARE: A Compiler-Assisted Dynamic Resource Allocation Framework for Real-world DRAM PIM](https://doi.org/10.1145/3721145.3725777) · ICS | 메모리 칩 안에 계산 기능을 넣는 PIM(Processing-In-Memory, 메모리 내 연산) 시스템에서 여러 응용 프로그램에 계산 자원을 배분하는 틀이다. 컴파일러(프로그램을 실행에 필요한 형태로 변환하는 소프트웨어)의 지원을 받아 응용마다 적합한 자원량을 정한다. 실행 중에는 자원 할당·반환 요청을 관찰하고, 남은 자원과 각 응용의 요구량을 고려해 우선순위에 따라 실행 순서를 조절한다. 실제 PIM 시스템에서 처리량과 평균 작업 완료 시간을 평가했다.[^p6] | Crossref 저자 순서 9명 중 6번째. 랩 목록의 J. Seo |

## 교수와 전문 분야

서지원 교수(Jiwon Seo)는 서울대학교 부교수다. 전기·정보공학부 교수 소개와 첨단융합학부 교수진 목록이 같은 연구실 누리집과 18동 418호를 연결하며, 첨단융합학부는 차세대지능형반도체전공으로 표시한다. 랩 교수 소개는 협동과정 인공지능 소속도 함께 적는다.[^prof][^snuti][^pi]

서울대학교 전기공학부에서 학사 학위(2005)를, Stanford University 전기공학에서 석사(2008)와 박사(2015) 학위를 받았다. UNIST 조교수(2016–2017), 한양대학교 조교수·부교수(2017–2025)를 거쳐 2025년 서울대학교 부교수로 부임했다. 학과 소개에는 LinkedIn 방문연구원(2014), Pinterest 소프트웨어 시스템 아키텍트(2015), Stanford University 박사후연구원(2015) 경력도 기재돼 있다.[^prof]

공식 교수 소개가 든 전문 분야는 머신러닝 시스템, 언어 모델 학습·추론 최적화, AI 모델 최적화·경량화 및 검사, 빅데이터 시스템이다. 최근 논문은 모델이 계산을 수행하는 순서를 조절하는 기술, 수치 표현을 바꾸는 기술, 영상 처리의 계산량을 실행 중 조절하는 기술을 보여 준다.[^prof][^p1][^p3][^p5]

## 응용 분야

언어 모델 추론 서비스와 여러 계산 장비를 사용하는 학습·추론 시스템이 주요 대상이다. 시각 모델 연구에서는 물체 검출에 앞선 영상 복원과 장치의 계산 자원 사용을 함께 다룬다. 학교의 연구실 소개는 임베디드 시스템(특정 기능을 수행하도록 기기에 들어가는 컴퓨터 시스템)부터 분산 시스템(여러 컴퓨터가 협력해 작업하는 시스템)까지를 연구 환경으로 든다.[^ece][^p3][^p5]

## 구성원

2026년 10월 26일 랩 Members 페이지에 게시된 교수 외 구성원 21명이다. 과정·직위는 페이지의 구획을 따른다.[^members]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| 김성균 | 박사후연구원 |  |
| 이준열 | 박사과정 |  |
| 최강 | 박사과정 |  |
| 김재민 | 박사과정 |  |
| 박기현 | 박사과정 |  |
| 남찬희 | 박사과정 |  |
| 이동혁 | 석사과정 |  |
| 유재혁 | 석사과정 |  |
| 김관중 | 석사과정 |  |
| 공상진 | 석사과정 |  |
| 이지현 | 석사과정 |  |
| 정현규 | 석사과정 |  |
| 김도윤 | 석사과정 |  |
| 정성원 | 석사과정 |  |
| 소지원 | 석사과정 |  |
| 최훈서 | 석사과정 |  |
| 김 주형 | 인턴 |  |
| 최준영 | 인턴 |  |
| 이은지 | 인턴 |  |
| 강현우 | 인턴 |  |
| 임창준 | 인턴 |  |

## 졸업생과 이전 구성원

랩 Members 페이지 Alumni 구획의 21명이다. 진로는 해당 구획 괄호 안의 게시 표기를 따른다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 윤도경 |  | 42dot |
| 강건 |  | 코넥시오에이치 |
| 오형준 |  | Moreh |
| 김기홍 |  | 42dot |
| 정홍석 |  | KT |
| 방경록 |  | 솔트룩스 |
| 김나훈 |  | 오케스트로 |
| 이용주 |  | 에이오팜 |
| 한병현 |  | CUBOX |
| 조동빈 |  | CJ |
| 강한성 |  | Vueron |
| 김형주 |  | 카카오 |
| 손동현 |  | Neurodigm |
| 이은재 |  | 네이버/라인 |
| 김정현 |  | 카카오 |
| 김영석 |  | 카카오 |
| 조봉기 |  | 쿠팡 |
| 이진원 |  | 삼성전자 |
| 안건주 |  | 티맥스 소프트 |
| Moeen Mirhosseini |  | Meta/Facebook |
| Junghoon Kim |  | UNIST Assistant Professor |

## 최근 논문 목록 (2021–2026)

랩 Publications의 2021–2026년 구역을 기준으로 한 목록이다. 서지원 교수는 2025년 서울대에 부임했으므로 2021–2024년 항목은 이전 소속 시기의 논문이며, 2025년 구역은 부임 연도에 발표된 공동연구를 포함한다. 제목·저자·발표처와 연도 구역은 랩 표기이고, *는 누리집 표시다. arXiv를 병기한 항목은 사전 공개판과 학회판을 구별한 것이다. 대표 논문 표는 실제 연결한 판본의 제목·서지를 별도로 따른다.[^pubs][^prof]

**2026**

- Hyungyu Jung, Jaehyeok Yu, Hoonseo Choi, Sungkyun Kim, Jinho Lee, and Jiwon Seo\*. "Spexis: Speculative and Lookahead Scheduling for LLM Inference". *Empirical Methods in Natural Language Processing (EMNLP), 2026; arXiv 사전 공개판 2609.34370 병기*.
- Sungkyun Kim, Jaemin Kim, Dogyung Yoon, Jiho Shin, Junyeol Lee, and Jiwon Seo\*. "Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding". *Association for Computational Linguistics (ACL Findings), 2026*.
- Jaemin Kim, Hongjun Um, Sungkyun Kim, Yongjun Park, and Jiwon Seo\*. "FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks". *In Proceedings of the European Conference on Computer Systems (EuroSys), 2026; arXiv 사전 공개판 2510.02822 병기*.
- Jaemin Kim, Sungkyun Kim, Junyeol Lee, and Jiwon Seo\*. "Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate". *In Proceedings of the Workshop on Machine Learning and Systems (EuroMLSys), 2026; arXiv 사전 공개판 2604.13806 병기*.

**2025**

- I. Hwang, D. Kim, S. Kang, T. Park, T. Kim, J. Seo, H. Kim, Y. Kim, Y. Park\*. "PIM-CARE: A Compiler-Assisted Dynamic Resource Allocation Framework for Real-world DRAM PIM". *In Proceedings of the ACM International Conference on Supercomputing (ICS), 2025*.
- Inho Lee, Jaemin Park, Seunghwan Lee, Tae Hyun Kim, Jiwon Seo, Hunjun Lee, and Yongjun Park\*. "Efficient Image Super-Resolution Using Dynamic Quality Control With Recursive Model Structures". *IEEE Access (Volume 13), 2025*.

**2024**

- Hyungjun Oh, Kihong Kim, Jaemin Kim, Sungkyun Kim, Du-seong Chang, and Jiwon Seo\*. "ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference". *In Proceedings of the Architectural Support for Programming Languages and Operating Systems (ASPLOS), 2024*.
- Younghyun Lee, Hyejun Kim, Yongseung Yu, Myeongjin Cho, Jiwon Seo, and Yongjun Park\*. "Discovering Efficient Fused Layer Configurations for Executing Multi-Workloads on Multi-core NPUs". *In Proceedings of Design Automation and Test in Europe (DATE), 2024*.

**2023**

- Seokwon Kang, Jongbin Kim, Gyeongyong Lee, Jeongmyung Lee, Jiwon Seo, Hyungsoo Jung, Yongho Song, and Yongjun Park\*. "ISP Agent: A Generalized In-Storage-Processing Workload Offloading Framework by Providing Multiple Optimization Opportunities". *ACM Transactions on Architecture and Code Optimization (TACO), 2023*.
- Yongseung Yu, Donghyun Son, Younghyun Lee, Sunghyun Park, Giha Ryu, Myeongjin Cho, Jiwon Seo\*, and Yongjun Park. "Tailoring Tiling-based GEMM Performance using Supervised Learning". *In Proceedings of IEEE International Conference on Computer Design (ICCD), 2023*.
- Mehrad Moradshahi, Tianhao Shen, Kalika Bali, Monojit Choudhury, Gael de Chalendar, Anmol Goel, Sungkyun Kim, Prashant Kodali, Ponnurangam Kumaraguru, Nasredine Semmar, Sina Semnani, Jiwon Seo, Vivek Seshadri, Manish Shrivastava, Michael Sun, Aditya Yadavalli, Chaobin You, Deyi Xiong, Monica Lam. "X-RiSAWOZ: High-Quality End-to-End Multilingual Dialogue Datasets and Few-shot Agents". *Association for Computational Linguistics (ACL Findings), 2023*.
- Eunjae Lee, Sam H. Noh, and Jiwon Seo\*. "SAGE: A System for Uncertain Network Analysis". *In Proceedings of the International Conference on Very Large Data Bases (VLDB), 2022-2023*.
- Kang Choi, Donghyun Son, Younghoon Kim, and Jiwon Seo\*. "Testing the Channels of Convolutional Neural Networks". *In Proceedings of the 37th AAAI Conference on Artificial Intelligence (AAAI), 2023*.

**2022**

- Kanggeun Lee, Dongbin Cho, Jinho Jang, Kang Choi, Hyoung-oh Jeong, Jiwon Seo\*, Won-Ki Jeong, Semin Lee. "RAMP: response-aware multi-task learning with contrastive regularization for cancer drug response prediction". *Briefings in Bioinformatics, 2022*.
- Hyungjun Oh, Junyeol Lee, Hyeongju Kim, and Jiwon Seo\*. "Out-Of-Order BackProp: An Effective Scheduling Technique for Deep Learning". *In Proceedings of the European Conference on Computer Systems (EuroSys), 2022*.
- Junyeol Lee, Hyeongju Kim, Hyungjun Oh, Jaemin Kim, Hongseok Jeung, Yung-Kyun Noh, and Jiwon Seo\*. "Gyro Dropout: Maximizing Ensemble Effect in Neural Network Training". *In Proceedings of the Fifth Conference on Machine Learning and Systems (MLSys), 2022*.

**2021**

- Seongyun Ko, Taesung Lee, Kijae Hong, Wonseok Lee, In Seo, Jiwon Seo, and Wook-Shin Han. "iTurboGraph: Scaling and Automating Incremental Graph Analytics". *In Proceedings of the International Conference on Management of Data (SIGMOD), 2021*.
- Yunyong Ko, Kibong Choi, Jiwon Seo\*, and Sang-Wook Kim. "An In-Depth Analysis of Distributed Training of Deep Neural Networks". *In Proceedings of IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2021*.

## 과제

게시 기간이 2021-10-22–2026-10-22와 겹치는 과제·자문 13건이다. 랩이 적은 참여·책임 구분과 기간을 따른다. 2025년 서울대 부임 전 시작한 과제와 이전 소속에서 수행한 과제가 함께 들어 있다.[^projects][^prof]

- 물리지능행동모델을 위한 co-working 테스트베드 기술개발 (기간 2026.8~2030.12; 지원 정보통신산업진흥원 과제; 역할 참여)
- NPU 파편화로 인한 AI 추론 오류 탐지·제어 프레임워크 기술 연구·개발 (기간 2026.3~2030.2; 지원 한국연구재단 핵심연구[유형B] 과제; 역할 참여)
- AI반도체를 위한 저수준 최적화 프로그램 API 기술 개발 (기간 2025.4~2030.12; 지원 정보통신기획평가원 과제; 역할 참여)
- AI 반도체 통합 자원관리 기술 개발 (기간 2025.4~2030.12; 지원 정보통신기획평가원 과제; 역할 참여)
- 익명화된 기밀실행을 이용한 전주기적 데이터 프라이버시 보호 기술 개발 (기간 2024.6~2027.12; 지원 정보통신기획평가원 과제; 역할 참여)
- 하이퍼-캄포저블 데이터센터를 위한 차세대 컴퓨팅 기술 개발 (기간 2021.7~2028.12; 지원 ITRC; 역할 참여)
- 거대 학습 모델 초고속 처리를 위한 고효율 AI 컴퓨팅SW 핵심 기술개발 (기간 2022.4~2025.12; 지원 정보통신기획평가원 과제; 역할 참여)
- AI 모델 실행 가속을 위한 모델 경량화 및 최적화 연구 (기간 2024.2~2024.8; 지원 산학 과제; 역할 책임)
- 초거대규모 자연어 처리 모델의 분산 학습 최적화 기술 개발 (기간 2024.2~2024.9; 지원 KT 산학 과제; 역할 책임)
- 인공지능 학습/추론 효율성 향상을 위한 서버용 SW 프레임워크 개발 (기간 2021.4~2024.12; 지원 정보통신기획평가원 과제; 역할 참여)
- 초거대규모 자연어 처리 모델의 분산 학습 최적화 기술 개발 (기간 2021.8~2023.7; 지원 KT 산학 과제; 역할 책임)
- (엑소브레인-2세부) WiseKB: 빅데이터 이해 기반 자가학습형 지식베이스 및 추론 기술 개발 (기간 2018.1~2022.12; 지원 정보통신기획평가원 과제; 역할 참여)
- Giant Model 기계 학습 동향 및 이를 위한 컴퓨팅 연구 (기간 2021.4~2021.12; 지원 ETRI 위탁 과제)

## 수상

누리집 논문 목록이 적은 2022년 ICPP 최우수논문상이다. 서지원 교수의 서울대 부임 전 성과다.[^pubs][^prof]

- 2022 · BWA-MEM-SCALE: Accelerating Genome Sequence Mapping on Commodity Servers: ICPP best paper award

## 연락과 위치

- 교수 연구실: 서울대학교 18동 418호[^contact][^snuti]
- 전화: 02-880-8089[^prof][^snuti]
- 교수 이메일: seojiwon@snu.ac.kr[^snuti]

## 각주
[^home]: Machine Learning Systems Lab, 첫 화면의 연구 주제와 시스템 소개. <https://mlsys.snu.ac.kr/home> (관측 2026-10-26).
[^ece]: 서울대학교 전기·정보공학부, 머신러닝 시스템 연구실 상세의 연구실 소개 및 연구분야. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=149> (관측 2026-10-26).
[^research]: Machine Learning Systems Lab, Research의 모델 보안·테스팅, 대규모 딥러닝, 성능·정확도, 불확정성 그래프 설명. <https://mlsys.snu.ac.kr/research> (관측 2026-10-26).
[^prof]: 서울대학교 전기·정보공학부, 서지원 부교수 소개의 학력·주요경력·연구 분야. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p915> (관측 2026-10-26).
[^snuti]: 서울대학교 첨단융합학부, 교수진 중 서지원 부교수 항목. <https://snuti.snu.ac.kr/commt/professor/> (관측 2026-10-26).
[^pi]: Machine Learning Systems Lab, JiwonSeo의 소속과 경력. <https://mlsys.snu.ac.kr/members_2/jiwonseo> (관측 2026-10-26).
[^members]: Machine Learning Systems Lab, Members의 Postdoctoral Researchers·Ph.D Students·M.S. Students·Interns·Alumni 구획. <https://mlsys.snu.ac.kr/members_2> (관측 2026-10-26).
[^pubs]: Machine Learning Systems Lab, Publications의 2021–2026년 구역과 저자 역할 안내. <https://mlsys.snu.ac.kr/publications> (관측 2026-10-26).
[^projects]: Machine Learning Systems Lab, Projects의 현재·지난 수행 과제. <https://mlsys.snu.ac.kr/projects> (관측 2026-10-26).
[^contact]: Machine Learning Systems Lab, Contact의 교수 연구실 위치. <https://mlsys.snu.ac.kr/cont> (관측 2026-10-26).

[^p1]: J. Kim 외, J. Seo, arXiv:2510.02822, EuroSys 2026 출판 예정 표기 (온라인 2025-10-03). <https://arxiv.org/abs/2510.02822> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.02822>.
[^p2]: J. Kim, S. Kim, J. Lee, J. Seo, arXiv:2604.13806v2 (온라인 2026-04-15). <https://arxiv.org/abs/2604.13806> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.13806>. 초록은 2026-09-16 개정 v2를 따른다.
[^p3]: S. Kim 외, J. Seo, Findings of the Association for Computational Linguistics: ACL 2026, 36290–36307 (2026). <https://doi.org/10.18653/v1/2026.findings-acl.1809> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2026.findings-acl.1809/>.
[^p4]: H. Jung 외, J. Seo, arXiv:2609.34370, EMNLP 2026 main 표기 (온라인 2026-09-28). <https://arxiv.org/abs/2609.34370> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.34370>.
[^p5]: I. Lee 외, Y. Park, IEEE Access 13, 134143–134159 (온라인 2025-06-24). <https://doi.org/10.1109/ACCESS.2025.3582604> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/392992298_Efficient_Image_Super-Resolution_Using_Dynamic_Quality_Control_with_Recursive_Model_Structures>.
[^p6]: I. Hwang 외, Y. Park, Proceedings of the 39th ACM International Conference on Supercomputing (2025). <https://doi.org/10.1145/3721145.3725777> 초록 기준(OpenAlex 등록 초록).

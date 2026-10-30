# CAMEL: 컴퓨터 아키텍처 및 메모리 시스템 연구실 (Computer Architecture and Memory Systems Laboratory)

**KAIST 전기및전자공학부·반도체시스템공학과·인공지능반도체대학원·김재철AI대학원·AI시스템학과 · 정명수 교수(KAIST 석좌교수)**

- 영문 이름: Computer Architecture and Memory Systems Laboratory, CAMELab[^home]
- 소속: 전기및전자공학부가 본래 소속이며, 인공지능반도체대학원과 김재철AI대학원 교수진도 이를 소속으로 적는다. 김재철AI대학원의 겸임교수 명단에 올라 있고, AI시스템학과 교수진에도 겸임교수로 적혀 있다.[^home][^aisemi][^gsai][^ais]
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 구조·운영체제[^research], 저장 시스템·SSD[^research], AI 시스템·인프라[^research], AI 반도체·가속기[^research][^p1]
- 홈페이지: <https://camelab.org/pmwiki.php>

> 프로세서와 메모리, 저장장치의 연결 구조부터 운영체제와 장치 내부 소프트웨어까지 함께 설계해, AI와 데이터 처리에 필요한 메모리 용량·데이터 이동·저장 성능 문제를 푸는 연구실이다.[^research]

## 무엇을 연구하나

CAMEL은 컴퓨터 아키텍처(컴퓨터 구성 요소의 구조와 동작 방식)와 운영체제(컴퓨터 자원을 관리하고 프로그램 실행을 지원하는 소프트웨어)를 함께 연구한다. 중심 대상은 프로세서(명령을 해석하고 실행하는 부품), 메모리(정보를 저장하는 장치), 저장장치이며, 이들을 연결하고 관리하는 방식까지 다룬다. 데이터센터(컴퓨터와 관련 설비를 모아 서비스를 운영하는 시설)에서 AI 계산에 필요한 데이터를 어디에 두고 어떻게 옮길지가 주요 문제다.[^home][^research]

첫 갈래는 CXL(Compute Express Link, 프로세서와 장치 사이의 메모리 접근과 데이터 공유를 지원하는 연결 표준)을 이용한 메모리 확장이다. 연구실은 프로세서·가속기(특정 계산을 수행하는 전용 처리 장치)·메모리·저장장치를 조합할 수 있는 데이터센터 구조를 설계한다. CXL 제어기(연결 규칙에 따라 데이터 전송을 관리하는 장치)와 스위치(여러 연결 사이에서 데이터가 갈 경로를 정하는 장치), 메모리 공동 이용과 실제 응용을 실행할 소프트웨어를 함께 개발한다.[^research]

둘째는 계산을 데이터 가까이에서 처리하는 메모리·저장 시스템이다. SSD(Solid-State Drive, 반도체 메모리에 데이터를 보관하는 저장장치) 안이나 가까이에서 데이터 준비와 계산을 수행하고, AI 학습·추론(학습한 모델로 결과를 구하는 과정)에 필요한 이동을 줄이려 한다. 연구 대상에는 LLM(Large Language Model, 대규모 언어 자료로 학습한 모델), 검색 증강 생성(외부에서 찾은 정보를 생성 과정에 함께 쓰는 방식), 그래프(대상과 그 관계를 점과 연결로 나타낸 구조) 데이터 처리가 포함된다.[^research]

셋째는 저장 시스템의 성능과 신뢰성을 하드웨어·소프트웨어 공동 설계로 개선하는 일이다. 펌웨어(장치 동작을 제어하는 내장 소프트웨어), 제어기, 운영체제의 정책과 작업 특성을 함께 고려한다. 여러 SSD를 묶는 저장 구조, 요청 처리 순서, 온도 관리, 내구성과 지연 시간도 연구한다. 시뮬레이션(모형으로 시스템 동작을 재현하는 방법)과 재구성 가능한 하드웨어를 이용한 실험 플랫폼도 만들어, 응용에서 장치까지 이어지는 설계를 평가한다.[^research]

## 주요 연구 주제

### CXL 메모리 확장과 메모리 중심 데이터센터

메모리를 개별 호스트(장치를 사용하고 제어하는 컴퓨터)에서 분리해 공동으로 쓸 수 있는 구조를 연구한다. CXL-GPU는 GPU(Graphics Processing Unit, 그래픽 등을 위한 병렬 계산 처리 장치)에 여러 CXL 연결을 두고 메모리와 SSD를 연결하는 설계다. CXL-ANNS는 근사 최근접 이웃 검색(질의와 가까운 자료를 근사적으로 찾는 방법)에 필요한 데이터를 메모리 풀(함께 사용할 수 있도록 묶은 메모리 자원)에 두고, 자주 찾을 데이터를 캐시에 보관하거나 미리 읽어 검색을 처리한다.[^p2][^p4]

### AI 데이터 준비와 저장장치 내부 연산

GNN(Graph Neural Network, 그래프의 연결 관계를 이용해 자료의 표현을 학습하는 신경망)의 전처리는 계산할 그래프를 변환하고 필요한 부분을 고르는 과정이다. 신경망은 연결된 계산 단위의 관계를 학습에 사용하는 모형이다. AutoGNN은 FPGA(Field-Programmable Gate Array, 회로 구성을 바꿔 사용할 수 있는 반도체)를 이용해 이 전처리를 수행한다. HolisticGNN은 그래프 학습 알고리즘을 데이터가 있는 저장장치 가까이에서 실행하고, 사용자가 장치 구성을 직접 다루지 않고도 프로그램을 작성하도록 지원한다.[^p1][^p5]

### SSD 어레이와 예측 가능한 응답 시간

올플래시 어레이(여러 반도체 저장장치를 묶은 저장 시스템)는 여러 SSD의 용량과 성능을 활용하는 구조다. ScalaAFA는 사용자 공간(운영체제 핵심 영역 밖에서 프로그램이 실행되는 영역)에 저장 엔진을 두고, 일부 내부 작업을 SSD에 맡겨 처리량과 데이터 이동을 다룬다. 작업 사이의 동기화도 함께 설계한다. Vigil-KV는 키–값 저장소(값을 식별하는 키와 그에 대응하는 값을 묶어 저장하는 체계)에서 SSD 내부 작업과 사용자 요청의 실행 시점을 조정해 일부 요청의 응답이 길어지는 문제를 줄인다.[^p3][^p6]

## 대표 논문

AI 데이터 준비, CXL 메모리 확장, 저장장치 내부 연산과 저장 시스템 설계를 보여 주는 6편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. AutoGNN과 CXL-GPU는 arXiv 사전 공개본을 설명하며, AutoGNN의 학회 채택 표시는 연구실 소식에 따른다.[^news]

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [AutoGNN: End-to-End Hardware-Driven Graph Preprocessing for Enhanced GNN Performance](https://doi.org/10.48550/arXiv.2602.00803) · arXiv 사전 공개본; HPCA 채택 | GNN 실행에 앞서 그래프를 변환하고 필요한 부분을 고르는 작업을 재구성 가능한 하드웨어가 수행한다. 입력 그래프를 분석해 하드웨어 설정도 바꾼다.[^p1] |
| 2 | 2025 | [CXL-GPU: Pushing GPU Memory Boundaries with the Integration of CXL Technologies](https://doi.org/10.48550/arXiv.2506.15601) · arXiv 사전 공개본 | GPU에 여러 CXL 연결을 두어 메모리와 SSD를 연결하고, 읽기·쓰기 방식을 설계해 저장 매체의 응답 시간 변동을 다룬다.[^p2] |
| 3 | 2024 | [ScalaAFA: Constructing User-Space All-Flash Array Engine with Holistic Designs](https://www.usenix.org/conference/atc24/presentation/yi-shushu) · USENIX ATC | 여러 SSD를 묶는 소프트웨어의 실행 위치와 동기화, 데이터 배치를 함께 바꾸고 일부 작업을 SSD가 처리하게 한다.[^p3] |
| 4 | 2023 | [CXL-ANNS: Software-Hardware Collaborative Memory Disaggregation and Computation for Billion-Scale Approximate Nearest Neighbor Search](https://www.usenix.org/conference/atc23/presentation/jang) · USENIX ATC | 검색 자료를 CXL 메모리 풀에 두고, 자주 방문할 자료의 캐시 보관과 미리 읽기, 여러 하드웨어의 병렬 검색을 함께 설계한다.[^p4] |
| 5 | 2022 | [Hardware/Software Co-Programmable Framework for Computational SSDs to Accelerate Deep Learning Service on Large-Scale Graphs](https://www.usenix.org/conference/fast22/presentation/kwon) · FAST | HolisticGNN은 그래프 신경망 알고리즘을 데이터가 있는 곳에서 실행하도록 지원한다. 그래프용 프로그램 인터페이스를 제공하고 계산형 SSD에 구현했다.[^p5] |
| 6 | 2022 | [Vigil-KV: Hardware-Software Co-Design to Integrate Strong Latency Determinism into Log-Structured Merge Key-Value Stores](https://www.usenix.org/conference/atc22/presentation/kwon) · USENIX ATC | 저장장치의 내부 작업과 키–값 저장소의 요청을 함께 조정해 응답이 오래 걸리는 요청의 지연을 줄이는 시스템이다.[^p6] |

## 교수와 전문 분야

정명수 교수는 2013년 Pennsylvania State University에서 컴퓨터과학 박사학위를 받았고, 2019년 KAIST 부교수로 부임했다. 누리집은 2024년부터 교수, 2025년부터 KAIST 석좌교수로 적는다. 이전에는 University of Texas at Dallas와 연세대학교에서 조교수로 재직했다.[^ee][^home]

전문 분야는 컴퓨터 구조와 운영체제, 메모리·저장 시스템, CXL 연결 구조, AI 계산을 위한 하드웨어·소프트웨어 공동 설계다. GNN 전처리 가속기, CXL을 이용한 GPU 메모리 확장, SSD 내부 작업과 저장 소프트웨어의 공동 설계가 최근 논문에 나타난다.[^research][^p1][^p2][^p6]

누리집은 정명수 교수가 2022년부터 파네시아(Panmnesia)의 대표라고 적는다. 연구에는 KAIST와 파네시아를 함께 소속으로 적은 논문 및 파네시아 단독 게재라고 표시한 항목이 포함된다.[^people][^pubs]

## 응용 분야

- AI 데이터센터: 프로세서·가속기·메모리·저장장치를 조합하는 연결 구조와 메모리 공동 이용.[^research]
- AI 학습·추론 서비스: 언어 모델과 그래프 모델의 데이터 준비, 저장장치 내부 처리, 학습 상태 저장.[^research]
- 대규모 검색과 추천: CXL 메모리 풀에 자료를 두고 수행하는 근사 최근접 이웃 검색.[^p4]
- 고성능 컴퓨팅과 데이터 저장 서비스: 메모리 중심 구조, SSD 어레이의 처리량·응답 시간·신뢰성 관리.[^research][^p3][^p6]

## 구성원

People 페이지의 현재 명단에 게시된 35명이다(박사과정 17명, 석사과정 12명, Researchers 6명). 과정·연구 주제는 랩 표기를 따른다. 「대표 논문 참여」는 해당 논문의 전체 저자 명단에서 같은 이름을 확인한 경우이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Donghyun Gouk | 박사과정 | Computing Switch/Network, Kernel, ML Accelerators, RISC-V | 1, 2, 5 |
| Junhyeok Jang | 박사과정 | Machine Learning, NVMe, Reliability, Security | 1, 2, 4 |
| Hanyeoreum Bae | 박사과정 | New Storage, ZNS, IOD | 2, 4 |
| Hyunkyu Choi | 박사과정 | Network/Storage, RISC-V | 1, 6 |
| Seungkwan Kang | 박사과정 | Storage-Integrated Accelerator | 1, 2 |
| Seungjun Lee | 박사과정 | OS, Storage Stack Optimization | 1, 2, 4, 6 |
| Dongsuk Oh | 박사과정 | Storage-Integrated Bioinformatics, Quantum, Process-In-Memory |  |
| Jiseon Kim | 박사과정 | Cache Coherent Interconnect, CXL, CCIX, Memory | 2 |
| Hanjin Choi | 박사과정 | AI Acceleration Hardware, CXL, Digital Circuit | 4 |
| Seonghyeon Jang | 박사과정 | Digital Circuit, Silicon, CXL |  |
| Eojin Ryu | 박사과정 |  | 2 |
| Dongpyung Kim | 박사과정 |  | 2 |
| Hyunwoo You | 박사과정 |  |  |
| Hyungseok Ko | 박사과정 |  |  |
| Heemin Kim | 석사과정 |  |  |
| Junseok Moon | 박사과정 |  |  |
| Eunjee Na | 박사과정 |  |  |
| Hongjoo Jung | 박사과정 |  |  |
| Sangyoon Ji | 석사과정 |  |  |
| Jinwoo Baek | 석사과정 |  |  |
| Hyein Woo | 석사과정 |  |  |
| Junhee Kim | 석사과정 |  |  |
| Kyungkuk Nam | 석사과정 |  | 2 |
| Minchul Jung | 석사과정 |  |  |
| Junbeom Kang | 석사과정 |  |  |
| Hyun Dong Lee | 석사과정 |  |  |
| Chaehun Kwak | 석사과정 |  |  |
| Jeongjin Han | 석사과정 |  |  |
| Hosung Cho | 석사과정 |  |  |
| Jinwook Lee | 연구원 |  |  |
| Hyojin Kwon | 연구원 |  |  |
| Seunghyeon Bang | 연구원 |  |  |
| Gicheol Lee | 연구원 |  |  |
| Hyung Joon Cho | 연구원 |  |  |
| Minju Lee | 연구원 |  |  |

## 졸업생과 이전 구성원

People 페이지의 Alumni에 올라 있는 84개 게시 항목이다. Ph.D. 구획 4명, Master 16명, Part-time Graduates 3명, Undergraduate Interns 57명, Visitors 4명을 담았다. 과정과 기간은 원문 표기이며, 재학 기간을 졸업 연도로 바꾸지 않았다. 같은 사람이 서로 다른 과정이나 현재 구성원 명단에도 올라 있을 수 있다. 진로는 랩이 게시한 기관과 직위다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jie Zhang | Ph.D. (CAMEL Ph.D. Student 2014~2020; Postdoc at CAMEL 2020~2021) | Tenure-track Professor, Peking University, School of Electronics Engineering and Computer Science (EECS) |
| Wonil Choi | Ph.D. Researcher (Mahmut Kandemir 공동지도) (2013~2015) | Tenure-track Professor, Hanyang University, College of Computing (ERICA) |
| Miryeong Kwon | Ph.D. (CAMEL Ph.D. Student 2019~2023; CAMEL M.S. Student 2016~2018) | President, Chief Operating Officer (COO), and Co-founder, Panmnesia, Inc. |
| Sangwon Lee | Ph.D. (CAMEL Ph.D. Student 2019~2023) | Director and Co-founder, Panmnesia, Inc. |
| Eunjee Na | Master | Co-founder of Panmnesia |
| Hyunwoo You | Master | Co-founder of Panmnesia |
| Eojin Ryu | Master | Co-founder of Panmnesia |
| Hyungseok Ko | Master | Co-founder of Panmnesia |
| Junseok Moon | Master | Co-founder of Panmnesia |
| Hongjoo Jung | Master | Co-founder of Panmnesia |
| Dongpyung Kim | Master | Co-founder of Panmnesia |
| Seonghyeon Jang | Master | Co-founder of Panmnesia |
| Hanjin Choi | Master | Co-founder of Panmnesia |
| Jiseon Kim | Master | Co-founder of Panmnesia |
| Hyunkyu Choi | Master | First landing: Panmnesia while pursuing a Ph.D. at KAIST |
| Dongsuk Oh | Master | Co-founder of Panmnesia |
| Donghyun Gouk | Master | Co-founder of Panmnesia |
| Miryeong Kwon | Master | Co-founder of Panmnesia |
| Sungjoon Koh | Master | First landing: TMAX |
| Shuwen Gao | Master | First landing: Intel, now at Google |
| Kisung Kim, SK Hynix Semiconductor | Part-time Graduates (2020 ~ 2022) |  |
| Hungyung Cho, SK Hynix Semiconductor | Part-time Graduates (2020 ~ 2022) |  |
| Youngwha Jo, SK Hynix Semiconductor | Part-time Graduates (2022 ~ 2023) |  |
| Minju Lee | Undergraduate Interns (2026 Summer) |  |
| Gicheol Lee | Undergraduate Interns (2026 Summer) |  |
| Seunghyeon Bang | Undergraduate Interns (2026 Summer) |  |
| Hyung Joon Cho | Undergraduate Interns (2026 Summer) |  |
| Jeongjin Han | Undergraduate Interns (2026 Summer) |  |
| Jinwook Lee | Undergraduate Interns (2026 Spring, 2026 Summer) |  |
| Hyun Dong Lee | Undergraduate Interns (2025 Winter) |  |
| Youngha Chun | Undergraduate Interns (2025 Winter) |  |
| Chaehun Kwak | Undergraduate Interns (2025 Fall, 2025 Winter) |  |
| Seojin Kim | Undergraduate Interns (2025 Summer, 2025 Fall) |  |
| Hyojin Kwon | Undergraduate Interns (2025 Summer, 2025 Fall, 2026 Summer) |  |
| Yeon Woo Jeong | Undergraduate Interns (2024 Winter) |  |
| Sanghyeok Boo | Undergraduate Interns (2024 Winter) |  |
| Jiyoung Lim | Undergraduate Interns (2024 Winter) |  |
| Jingwoong Hwang | Undergraduate Interns (2024 Fall, 2024 Winter) |  |
| Myounghun Park | Undergraduate Interns (2024 Summer, 2024 Fall, 2024 Winter) |  |
| Junbeom Kang | Undergraduate Interns (2024 Summer, 2024 Fall, 2024 Winter) |  |
| Minchul Jung | Undergraduate Interns (2024 Spring, 2024 Summer, 2024 Fall, 2024 Winter) |  |
| Kyungkuk Nam | Undergraduate Interns (2024 Spring, 2024 Summer) |  |
| Jinwoo Baek | Undergraduate Interns (2023 Summer, 2023 Fall) |  |
| Hongjoo Jung | Undergraduate Interns (2023 Summer) |  |
| Seungkuk Lee | Undergraduate Interns (2023 Summer) |  |
| Hyein Woo | Undergraduate Interns (2023 Summer, 2023 Fall, 2024 Spring) |  |
| Eunjee Na | Undergraduate Interns (2023 Spring, 2023 Summer) |  |
| Heemin Kim | Undergraduate Interns (2022 Winter, 2023 Summer) |  |
| Junseok Moon | Undergraduate Interns (2022 Winter, 2023 Spring, 2023 Summer) |  |
| Dongpyung Kim | Undergraduate Interns (2022 Winter) |  |
| Huiwon Choi | Undergraduate Interns (2022 Winter) |  |
| Minyoung Choi | Undergraduate Interns (2022 Fall, 2022 Winter) |  |
| Yongsik Kim | Undergraduate Interns (2022 Summer) |  |
| Sunho Lee | Undergraduate Interns (2022 Summer) |  |
| Jinwoong Hwang | Undergraduate Interns (2022 Summer) |  |
| Junhee Kim | Undergraduate Interns (2022 Summer, 2023 Fall, 2024 Spring) |  |
| Eojin Ryu | Undergraduate Interns (2021 Winter, 2022 Summer, 2022 Fall, 2022 Winter) |  |
| Hyungseok Ko | Undergraduate Interns (2021 Winter, 2022 Spring, 2022 Summer, 2022 Winter, 2023 Spring, 2023 Summer) |  |
| Hyunwoo You | Undergraduate Interns (2021 Summer, 2021 Winter, 2022 Spring, 2022 Summer, 2022 Fall, 2022 Winter, 2023 Spring, 2023 Summer) |  |
| Sangyoon Ji | Undergraduate Interns (2021 Winter, 2022 Winter, 2023 Summer, 2023 Fall) |  |
| Hanjin Choi | Undergraduate Interns (2021 Summer, 2021 Winter) |  |
| Seonghyeon Jang | Undergraduate Interns (2021 Summer, 2021 Winter) |  |
| Jiseon Kim | Undergraduate Interns (2020 Winter, 2021 Spring, 2021 Summer) |  |
| Junseok Lee | Undergraduate Interns (2020 Winter) |  |
| Sanghyun Han | Undergraduate Interns (2020 Summer) |  |
| Geunwoo Jeon | Undergraduate Interns (2018 Winter) |  |
| Seongmin Lee | Undergraduate Interns (2018 Winter) |  |
| Joonyong Lee | Undergraduate Interns (2018 Winter) |  |
| Hanjoo Yoo | Undergraduate Interns (2018 Winter) |  |
| Jongwook Han | Undergraduate Interns (2018 Winter) |  |
| Junhyeok Jang | Undergraduate Interns (2018 Summer) |  |
| Changrim Lee | Undergraduate Interns (2018 Summer) |  |
| Sungjoon Koh | Undergraduate Interns (2018 Summer) |  |
| Gyuyoung Park | Undergraduate Interns (2017 Winter) |  |
| Woonsung Baek | Undergraduate Interns (2017 Winter) |  |
| Hyunjun Kim | Undergraduate Interns (2017 Winter) |  |
| Hyungjoo Moon | Undergraduate Interns (2016 Summer) |  |
| Jongmin Park | Undergraduate Interns (2016 Summer) |  |
| Seoyoon Choi | Undergraduate Interns (2016 Summer) |  |
| Minwoo Lee | Undergraduate Interns (2015 Winter) |  |
| Ahmed Abulila | Visitors (2015) | University of Wisconsin–Madison |
| Narges Shahidi | Visitors (2015) | Pennsylvania State University |
| Damian Szmulewicz | Visitors (2015) | Texas Instruments |
| Erick Macias | Visitors (2015) | Texas Instruments |

## 최근 논문 목록 (2021–2026)

CXL 메모리 확장, AI 가속기, 저장 시스템과 운영체제 연구를 담은 교수 개인 누리집의 목록이다. Full Publication List의 2021–2026년 구역 65편이며, 학술지·학회·워크숍 논문과 기술 보고서를 포함한다. 제목·저자·발표처·연도는 랩 표기를 따른다. 파네시아 단독 게재로 표시된 항목도 포함된다. 연구실 소식에서 채택을 알린 AutoGNN·MemLLM은 「채택」으로 표시했다.[^pubs][^news]

**2026**

- Seungkwan Kang, Hyungseok Ko, Hyun Dong Lee, Myoungsoo Jung. "LATTIX: A Sparse Processing-In-Memory Accelerator for Speculative LLM Inference". *2nd Workshop on Sparsity, the Key Ingredient from HPC to Efficient LLMs (SPICE), co-located with MICRO*.
- Myoungsoo Jung, Hyein Woo, Junhee Kim, Jinwoo Baek, Kyungkuk Nam, Eunjee Na, Hyunkyu Choi, Seonghyeon Jang, Hanjin Choi, Kayvon Shakeri, Han Wang, Miryeong Kwon. "One-Chip-Like Datacenter Design Enabled by CXL-Based Scale-Up Fabrics". *Nature Reviews Electrical Engineering*.
- Jie Zhang, Shushu Yi, Xiurui Pan, Yiming Xu, Qiao Li, Qiang Li, Chenxi Wang, Bo Mao, Myoungsoo Jung. "Enhancing the Performance of Next-Generation SSD Arrays: A Holistic Approach". *ACM Transactions on Storage (TOS)*.
- Seungkwan Kang, Hyungseok Ko, Myeonghoon Park, Jinseok Kim, Hyun Dong Lee, Myoungsoo Jung. "The Host Is Not Idle: Computational SSDs for Host-Free Checkpointing in Multimodal LLM Training". *The ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Seungkwan Kang, Hyungseok Ko, Jinseok Kim, Myeonghoon Park, Hyun Dong Lee, Myoungsoo Jung. "GraceSSD: Per-File Reliability Hints for Error-Tolerant Machine Learning Storage". *The ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Seungkwan Kang, Hyungseok Ko, Heemin Kim, Myoungsoo Jung. "MemLLM: End-to-End In-Storage Acceleration of On-Device Retrieval-Augmented Generation using Precomputed KV Caches". *59th IEEE/ACM International Symposium on Microarchitecture (MICRO) (채택)*.
- Miryeong Kwon, Seungjun Lee, Donghyun Gouk, Hongjoo Jung, Eojin Ryu, Seyeong Huh, Junseok Moon, Hyein Woo, Junhee Kim, Kyungkuk Nam, Jinwoo Baek, Hyunkyu Choi, Woojin Choi, Yongjin Cho, Myoungsoo Jung. "A Silicon-Proven Unified Low-Latency CXL Controller and Port-Based Routing Switch for Memory-Centric Fabrics". *The 53rd International Symposium on Computer Architecture (ISCA): Panmnesia's sole publication (Industry Track)*.
- Seungkwan Kang, Seungjun Lee, Donghyun Gouk, Miryeong Kwon, Hyunkyu Choi, Junhyeok Jang, Sangwon Lee, Huiwon Choi, Jie Zhang, Wonil Choi, Mahmut T Kandemir, Myoungsoo Jung. "AutoGNN: End-to-End Hardware-Driven Graph Preprocessing for Enhanced GNN Performance". *The 32nd IEEE International Symposium on High-Performance Computer Architecture (HPCA) (채택)*.

**2025**

- Huiwon Choi, Myoungsoo Jung. "Memoization: Accelerating MCD BNN by Attribution-Based Dynamic Precision Scaling". *7th International Workshop on Domain Specific System Architecture (DoSSA), co-located with MICRO*.
- Seungjun Lee, Seungkwan Kang, Miryeong Kwon, Hyunkyu Choi, Myoungsoo Jung. "Zero-Overhead Sparsity Prediction for Dynamic Algorithm Selection in Deep Learning Models". *Sparsity, the Key Ingredient from HPC to Efficient LLMs (SPICE), co-located with MICRO*.
- Miryeong Kwon, Donghyun Gouk, Hyein Woo, Junhee Kim, Jinwoo Baek, Kyungkuk Nam, Sangyoon Ji, Jiseon Kim, Hanyeoreum Bae, Junhyeok Jang, Hyunwoo You, Junseok Moon, Myoungsoo Jung. "MPI-over-CXL: Enhancing Communication Efficiency in Distributed HPC Systems". *Sparsity, the Key Ingredient from HPC to Efficient LLMs (SPICE), co-located with MICRO*.
- Seungkwan Kang, Miryeong Kwon, Seungjun Lee, Huiwon Choi, Myoungsoo Jung. "Bridging Natural Resilience and Cost-Effectiveness in SSDs for Containerized ML Applications". *The International Workshop on Practical Adoption Challenges of ML for Systems (PACMI), co-located with SOSP*.
- Hyein Woo, Miryeong Kwon, Jiseon Kim, Eunjee Na, Hanjin Choi, Seonghyeon Jang, Myoungsoo Jung. "ScalePool: Hybrid XLink-CXL Fabric for Composable Resource Disaggregation in Unified Scale-up Domains". *The International Workshop on Disruptive Memory Systems (DIMES), co-located with SOSP*.
- Seungkwan Kang, Eunjee Na, Seungjun Lee, Myoungsoo Jung. "Mitigating Heat-induced Performance Cliffs of SSDs via OS-level Thermal-aware I/O Throttling". *The International Workshop on Big Memory (BigMem), co-located with SOSP*.
- Donghyun Gouk, Seungkwan Kang, Seungjun Lee, Jiseon Kim, Kyungkuk Nam, Eojin Ryu, Sangwon Lee, Dongpyung Kim, Junhyeok Jang, Hanyeoreum Bae, Myoungsoo Jung. "CXL-GPU: Pushing GPU Memory Boundaries with the Integration of CXL Technologies". *IEEE Micro*.
- Miryeong Kwon, Donghyun Gouk, Junhyeok Jang, Jinwoo Baek, Hyunwoo You, Sangyoon Ji, Hongjoo Jung, Junseok Moon, Seungjoon Lee, Seungkwan Kang, Myoungsoo Jung. "From Block to Byte: Transforming PCIe SSDs with CXL Memory Protocol and Instruction Annotation". *IEEE Micro*.
- Myoungsoo Jung. "Compute Can't Handle the Truth: Why Communication Tax Prioritizes Memory and Interconnects in Modern AI Infrastructure". *Panmnesia Technical Report*.
- Dongsuk Oh, Miryeong Kwon, Jiseon Kim, Eunjee Na, Junseok Moon, Hyunkyu Choi, Seonghyeon Jang, Hanjin Choi, Hongjoo Jung, Sangwon Lee, Myoungsoo Jung. "CXL Topology-Aware and Expander-Driven Prefetching: Unlocking SSD Performance". *IEEE Micro*.
- Miryeong Kwon, Donghyun Gouk, Jiseon Kim, Eunjee Na, Junhee Kim, Hyein Woo, Eojin Ryu, Hyunkyu Choi, Jinwoo Baek, Hanyeoreum Bae, Mahmut Kandemir, Myoungsoo Jung. "Containerized In-Storage Processing and Computing-Enabled SSD Disaggregation". *IEEE Micro*.
- Jinyeong Lim, Junhyuck Jang, Myoungsoo Jung, Dongsu Han. "Efficient Disaggregated Cloud Storage for Cold Videos with Neural Enhancement". *IEEE Micro*.

**2024**

- Shaocong Sun, Li Peng, Yingbo Sun, Ming-Chang Yang, Zhichao Cao, Qiao Li, Myoungsoo Jung, Ke Zhou, Jie Zhang. "BIZA: Design of Self-Governing Block-Interface ZNS AFA for Endurance and Performance". *The 30th Symposium on Operating Systems Principles (SOSP)*.
- Donghyun Gouk, Seungkwan Kang, Hanyeoreum Bae, Eojin Ryu, Sangwon Lee, Dongpyung Kim, Junhyeok Jang, Myoungsoo Jung. "Breaking Barriers: Expanding GPU Memory with Sub-Two Digit Nanosecond Latency CXL Controller". *The ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Shushu Yi, Xiurui Pan, Qiao Li, Qiang Li, Chenxi Wang, Bo Mao, Myoungsoo Jung, Jie Zhang. "ScalaAFA: Constructing User-Space All-Flash Array Engine with Holistic Designs". *The USENIX Annual Technical Conference (ATC)*.
- Xiurui Pan, Yuda An, Shengwen Liang, Bo Mao, Mingzhe Zhang, Qiao Li, Myoungsoo Jung, Jie Zhang. "Flagger: Cooperative Acceleration for Large-Scale Cross-Silo Federated Learning Aggregation". *The IEEE/ACM International Symposium on Computer Architecture (ISCA)*.
- Junhyeok Jang, Hanjin Choi, Hanyeoreum Bae, Seungjun Lee, Miryeong Kwon, and Myoungsoo Jung. "Bridging Software-Hardware for CXL Memory Disaggregation in Billion-Scale Nearest Neighbor Search". *ACM Transaction on Storage*.
- Donghyun Gouk, Miryeong Kwon, Hanyeoreum Bae, Myoungsoo Jung. "DockerSSD: Containerized In-Storage Processing and Hardware Acceleration for Computational SSDs". *The 30th IEEE International Symposium on High-Performance Computer Architecture (HPCA)*.

**2023**

- Donghyun Gouk, Miryeong Kwon, Hanyeoreum Bae, Myoungsoo Jung. "Containerized In-Storage Processing Model and Hardware Acceleration for Fully-Flexible Computational SSDs". *IEEE Computer Architecture Letter (CAL)*.
- Miryeong Kwon, Sangwon Lee, Myoungsoo Jung. "Cache in Hand: Expander-Driven CXL Prefetcher for Next Generation CXL-SSD". *The 15th ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Junhyeok Jang, Hanjin Choi, Hanyeoreum Bae, Seungjun Lee, Miryeong Kwon, Myoungsoo Jung. "CXL-ANNS: Software-Hardware Collaborative Memory Disaggregation and Computation for Billion-Scale Approximate Nearest Neighbor Search". *The USENIX Annual Technical Conference (ATC)*.
- Jiho Kim, Myoungsoo Jung, John Kim. "Decoupled SSD: Rethinking SSD Architecture through Network-based Flash Controllers". *The IEEE/ACM International Symposium on Computer Architecture (ISCA)*.
- Miryeong Kwon, Junhyeok Jang, Hanjin Choi, Sangwon Lee, Myoungsoo Jung. "Training Resilience with Persistent Memory Pooling using CXL Technology". *Heterogeneous and Composable Memory Workshop at HPCA*.
- Hanyeoreum Bae, Donghyun Gouk, Seungjun Lee, Jiseon Kim, Sungjoon Koh, Jie Zhang, Myoungsoo Jung. "Intelligent SSD Firmware for Zero-Overhead Journaling". *IEEE Computer Architecture Letter (CAL)*.
- Junhyeok Jang, Miryeong Kwon, Donghyun Gouk, Hanyeoreum Bae, Myoungsoo Jung. "GraphTensor: Comprehensive GNN-Acceleration Framework for Efficient Parallel Processing of Massive Datasets". *37th IEEE International Parallel & Distributed Processing Symposium (IPDPS)*.
- Shushu Yi, Yanning Yang, Yunxiao Tang, Zixuan Zhou, Junzhe Li, Yue Chan, Myoungsoo Jung, Jie Zhang. "Optimizations of Linux Software RAID System for Next-Generation Storage". *14th Annual Non-Volatile Memories Workshop (NVMW)*.
- Ahmed Abulila, Izzat El Hajj, Myoungsoo Jung, Nam Sung Kim. "Asynchronous Persistence with ASAP". *14th Annual Non-Volatile Memories Workshop (NVMW)*.
- Miryeong Kwon, Seungjun Lee, Hyunkyu Choi, Jooyoung Hwang, Myoungsoo Jung. "Realizing Strong Determinism Contract on Log-Structured Merge Key-Value Stores". *ACM Transaction on Storage*.
- Miryeong Kwon, Junhyeok Jang, Hanjin Choi, Sangwon Lee, Myoungsoo Jung. "Failure Tolerant Training with Persistent Memory Disaggregation over CXL". *IEEE Micro*.
- Donghyun Gouk, Miryeong Kwon, Hanyeoreum Bae, Sangwon Lee, Myoungsoo Jung. "Memory Pooling with CXL". *IEEE Micro*.
- Md Hafizul Islam Chowdhuryy, Myoungsoo Jung, Fan Yao, Amro Awad. "D-Shield: Enabling Processor-Side Encryption and Integrity Verification for Secure NVMe Drives". *The 29th IEEE International Symposium on High-Performance Computer Architecture (HPCA)*.

**2022**

- Donghyun Gouk, Sangwon Lee, Miryeong Kwon, Myoungsoo Jung. "Practical Memory Disaggregation using Compute Express Link". *The 3rd Workshop On Resource Disaggregation and Serverless Computing (WORDS'22)*.
- Donghyun Gouk, Seungkwan Kang, Miryeong Kwon, Junhyeok Jang, Hyunkyu Choi, Myoungsoo Jung. "PreGNN: Hardware Acceleration to Take Preprocessing Off the Critical Path in Graph Neural Networks". *IEEE Computer Architecture Letters (CAL)*.
- Miryeong Kwon, Donghyun Gouk, Myoungsoo Jung. "Large-scale Graph Neural Network Services through Computational SSD and In-Storage Processing Architectures". *Symposum on High Performance Chips (HotChips)*.
- Myoungsoo Jung. "Hello Bytes, Bye Blocks: PCIe Storage Meets Compute Express Link for Memory Expansion (CXL-SSD)". *The 14th ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Hanyeoreum Bae, Jiseon Kim, Miryeong Kwon, Myoungsoo Jung. "What You Can't Forget: Exploiting Parallelism for Zoned Namespaces". *The 14th ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Shushu Yi, Yanning Yang, Yunxiao Tang, Zixuan Zhou, Junzhe Li, Yue Chen, Myoungsoo Jung, Jie Zhang. "ScalaRAID: Optimizing Linux Software RAID System for Next-Generation Storage". *The 14th ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)*.
- Donghyun Gouk, Sangwon Lee, Miryeong Kwon, Myoungsoo Jung. "Direct Access, High-Performance Memory Disaggregation with DirectCXL". *The USENIX Annual Technical Conference (ATC)*.
- Miryeong Kwon, Seungjun Lee, Hyunkyu Choi, Jooyoung Hwang, Myoungsoo Jung. "Vigil-KV: Hardware-Software Co-Design to Integrate Strong Latency Determinism into Log-Structured Merge Key-Value Stores". *The USENIX Annual Technical Conference (ATC)*.
- Myoungsoo Jung. "Realizing Scale-Out, High-Performance Memory Disaggregation with Compute Express Link (CXL)". *KAIST Technology Report*.
- Sangwon Lee, Miryeong Kwon, Gyuyoung Park, Myoungsoo Jung. "LightPC: Hardware and Software Co-Design for Energy-Efficient Full System Persistence". *The IEEE/ACM International Symposium on Computer Architecture (ISCA)*.
- Ahmed Abulila, Izzat El Hajj, Myoungsoo Jung, Nam Sung Kim. "ASAP: Architecture Support for Asynchronous Persistence". *The IEEE/ACM International Symposium on Computer Architecture (ISCA)*.
- Jie Zhang, Miryeong Kwon, Donghyun Gouk, Sungjoon Koh, Nam Sung Kim, Mahmut Kandemir, Myoungsoo Jung. "HAMS: Hardware Automated Memory-over-Storage for Large-scale Memory Expansion". *13rd Annual Non-Volatile Memories Workshop (NVMW)*.
- Miryeong Kwon, Donghyun Gouk, Sangwon Lee, Myoungsoo Jung. "HolisticGNN: Geometric Deep Learning Engines for Computational SSDs". *13rd Annual Non-Volatile Memories Workshop (NVMW)*.
- Jie Zhang, Myoungsoo Jung. "Integrating New Photonic-Based Heterogeneous Memory into Throughput Accelerators". *13rd Annual Non-Volatile Memories Workshop (NVMW)*.
- Hanyeoreum Bae, Miryeong Kwon, Donghyun Gouk, Sanghyun Han, Sungjoon Koh, Changrim Lee, Dongchul Park, Myoungsoo Jung. "Slow is Fast: Rethinking In-Memory Graph Analysis with Persistent Memory". *13rd Annual Non-Volatile Memories Workshop (NVMW)*.
- Miryeong Kwon, Donghyun Gouk, Sangwon Lee, Myoungsoo Jung. "Hardware/Software Co-Programmable Framework for Computational SSDs to Accelerate Deep Learning Service on Large-Scale Graphs". *The 20th USENIX Conference on File and Storage Technologies (FAST)*.

**2021**

- Jiho Kim, Myoungsoo Jung, Jhon Kim. "Decoupled SSD: Reducing Data Movement on NAND-based Flash SSD". *IEEE Computer Architecture Letters (CAL)*.
- Hanyeoreum Bae, Miryeong Kwon, Donghyun Gouk, Sanghyun Han, Sungjoon Koh, Changrim Lee, Dongchul Park, Myoungsoo Jung. "Empirical Guide to Use of Persistent Memory for Large-Scale In-Memory Graph Analysis". *The 39th IEEE International Conference on Computer Design (ICCD)*.
- Jie Zhang, Myoungsoo Jung. "Ohm-GPU: Integrating New Optical Network and Heterogeneous Memory into GPU Multi-Processors". *54th IEEE/ACM International Symposium on Microarchitecture (MICRO)*.
- Jie Zhang, Miryeong Kwon, Donghyun Gouk, Sungjoon Koh, Nam Sung Kim, Mahmut Kandemir, Myoungsoo Jung. "Revamping Storage Class Memory With Hardware Automated Memory-Over-Storage Solution". *The IEEE/ACM International Symposium on Computer Architecture (ISCA)*.
- Jie Zhang, Myoungsoo Jung. "Architecting Throughput Processors with New Flash". *12th Annual Non-Volatile Memories Workshop (NVMW)*.
- Jie Zhang, Gyuyoung Park, David Donofrio, John Shalf, Myoungsoo Jung. "DRAM-less Accelerator for Energy Efficient Data Processing". *12th Annual Non-Volatile Memories Workshop (NVMW)*.
- Jie Zhang, Miryeong Kwon, Michael Swift, Myoungsoo Jung. "Manycore-Based Scalable SSD Architecture Towards One and More Million IOPS". *12th Annual Non-Volatile Memories Workshop (NVMW)*.
- Miryeong Kwon, Donghyun Gouk, Changrim Lee, ByoungGeun Kim, Jooyoung Hwang, Myoungsoo Jung. "Deterministic I/O and Resource Isolation for OS-level Virtualization In Server Computing". *12th Annual Non-Volatile Memories Workshop (NVMW)*.
- Chun-Yi Liu, Yunju Lee, Wonil Choi, Myoungsoo Jung, Mahmut Kandemir, Wonil Choi. "Prolonging 3D NAND SSD Lifetime via Read Latency Relaxation". *The 26th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS)*.
- Chun-Yi Liu, Yunju Lee, Wonil Choi, Myoungsoo Jung, Mahmut Kandemir, Chita Das. "GSSA: A Resource Allocation Scheme Customized for 3D NAND SSDs". *The 26th IEEE International Symposium on High-Performance Computer Architecture (HPCA)*.

## 특허

Publications의 Published and Issued Patents 가운데 2022–2025년 구역에 적힌 미국 B2 등록공보 7건이다. 연도·제목·발명자는 랩 게시 표기다.[^pubs]

- 2025 · Hybrid memory system and accelerator including the same (발명자 Myoungsoo Jung; 국가 America; 번호 US12210744B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2025 · Method of supporting persistence and computing device (발명자 Myoungsoo Jung; 국가 America; 번호 US12386657B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2024 · Computational SSD accelerating deep learning service on large-scale graphs (발명자 Myoungsoo Jung; 국가 America; 번호 US12169636B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2024 · Data storage device for determining a write address using a neural network (발명자 Junhyeok Jang, Myoungsoo Jung; 국가 America; 번호 US11921628B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2023 · Computing device and storage card (발명자 Myoungsoo Jung; 국가 America; 번호 US11689621B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2022 · Graph processing system including different kinds of memory devices, and operation method thereof (발명자 Myoungsoo Jung, Miryeong Kwon; 국가 America; 번호 US11409798B2; 상태 B2 등록공보; 연도는 랩 게시 연도)
- 2022 · Memory controller and operating method thereof (발명자 Junhyeok Jang, Myoungsoo Jung; 국가 America; 번호 US11301371B2; 상태 B2 등록공보; 연도는 랩 게시 연도)

## 수상과 선정

교수 개인 누리집의 Awards·People과 연구실 소식에 게시된 19건이다. 2022–2025년 수상·선정과 날짜가 붙은 2026년 1월 수상·헌액을 담았다. CES 항목의 연도는 상의 이름에 든 연도이며 소식 게시일과 다를 수 있다.[^services][^people][^news]

- 2026-01-08 · Korea Science and Technology Award · 대한민국 과학기술인상 , Ministry of Science and ICT, 2026
- 2025 · Outstanding SME (Small and Medium-Sized Enterprise) of 2025 · 중소기업청장상 , Daejeon and Sejong Regional Office of SMEs and Startups
- 2025 · 31st Daejeon Metropolitan City Economic & Science Award (Venture Category) · 대전광역시 경제과학대상 , Daejeon Metropolitan Government, 2025
- 2025 · Digital Innovation Award · 부총리 겸 과학기술정보통신부 장관 표창 , Minister of Science and ICT, 2025
- 2026-01-24 · IEEE/ACM HPCA Hall of Fame, 2026
- 2025 · Presidential Commendation · 대통령 표창 , 2025 K-Tech Inside Show (Materials, Parts, and Equipment & Core Technology Exhibition), 2025
- 2025 · Minister's Commendation · 산업통상자원부 장관 표창 , Minister of Trade, Industry and Energy, 2025
- 2025 · KAIST Q-Day Faculty Special Award · KAIST Q-Day 교원 특별포상 , KAIST, 2025
- 2025 · Minister's Award, Korea Innovative Startup Award · 과학기술정보통신부 장관상 , Ministry of Science and ICT, 2025
- 2025 · CES Innovation Award, "CXL-Enabled AI Accelerator", CES, 2025
- 2024 · Digital Innovation Award · 과학기술정보통신부 장관 표창 , Minister of Science and ICT, 2024
- 2024 · IEEE/ACM ISCA Hall of Fame, 2024
- 2024 · CES Innovation Award, "CXL-Enabled AI Accelerator", CES, 2024
- 2022 · NVMW Memorable Paper Award, " HolisticGNN: Geometric Deep Learning Engines for Computational SSDs ", Non-Volatile Memories Workshop (NVMW), 2022
- 2022 · Samsung Best Paper Award (Grand Prize), "Hardware–Software Co-Design to Integrate Strong Latency Determinism into Log-Structured Merge Key–Value Stores", Samsung Electronics, 2022
- 2024-04-01 · Miryeong Kwon: KAIST 우수 박사학위논문상
- 2025 · 정명수: FIX Innovation Awards
- 2025 · 정명수: IITP President’s Award
- 2022 · Hyunkyu Choi: Best Teaching Assistant Award at KAIST EE

## 연구실 소식

News의 2021-10-13–2026-10-13 게시 글 53건이다. 목록 날짜는 게시일이며, 발표·초청·채택·수상·지원 선정 등 글이 밝힌 사실을 옮겼다.[^news]

- 2026-09-09 · 메타·파네시아의 CXL 기반 데이터센터 리뷰 논문과 보도 소식을 알렸다.
- 2026-07-25 · HotStorage 2026에 체크포인트 저장과 GraceSSD 연구 2편이 채택됐다.
- 2026-07-09 · 저장장치 내부에서 검색 증강 생성을 가속하는 MemLLM이 MICRO 2026에 채택됐다.
- 2026-06-29 · ISCA 2026에서 CXL 제어기와 패브릭 스위치를 발표했다.
- 2026-01-24 · 정명수 교수가 IEEE HPCA 명예의 전당에 헌액됐다.
- 2026-01-08 · 정명수 교수가 2026년 1월 대한민국 과학기술인상 수상자로 선정됐다.
- 2025-11-08 · AutoGNN이 HPCA 2026에 채택됐다.
- 2025-10-29 · 정명수 교수가 2025 K-Tech Inside Show에서 대통령 표창을 받았다.
- 2025-10-23 · ETH Zürich SAFARI 연구진을 초청해 연구 세미나를 열었다.
- 2025-10-21 · 정명수 교수가 전자·IT의 날 행사에서 산업통상자원부 장관 표창을 받았다.
- 2025-10-19 · MICRO 2025의 SPICE·DoSSA 워크숍에서 희소성 예측, MPI-over-CXL, Memoization 연구를 발표했다.
- 2025-10-13 · SOSP 2025의 BigMem·PACMI 워크숍에서 SSD 온도 관리와 NatureSSD 연구를 발표했다.
- 2025-09-10 · 정명수 교수가 대한민국 혁신창업상 과학기술정보통신부 장관상을 받았다.
- 2025-05-21 · CXL 연결 구조와 메모리 확장 장치 기반 미리 읽기 연구가 IEEE Micro에 게재 승인됐다.
- 2025-05-21 · 컨테이너 기반 저장장치 내부 처리와 SSD 분리 연구가 IEEE Micro에 게재 승인됐다.
- 2025-01-15 · 연구팀이 메모리 확장 장치를 이용한 AI 인프라 솔루션으로 CES 2025 혁신상을 받았다.
- 2024-12-02 · 정명수 교수가 2024 대한민국 디지털 혁신 시상식에서 과학기술정보통신부 장관 표창을 받았다.
- 2024-08-07 · ZNS 기반 올플래시 어레이 연구 BIZA가 SOSP 2024에 채택됐다.
- 2024-07-16 · 정명수 교수가 CXL 기반 미래 AI 데이터센터를 주제로 기조강연을 예고했다.
- 2024-05-01 · 사용자 공간 올플래시 어레이 엔진 ScalaAFA가 USENIX ATC 2024에 채택됐다.
- 2024-04-08 · 기관 간 연합학습 집계를 가속하는 Flagger가 ISCA 2024에 채택됐다.
- 2024-04-01 · Miryeong Kwon 박사가 KAIST 우수 박사학위논문상을 받았다.
- 2023-11-22 · 연구팀이 CXL 기반 AI 가속기 기술로 CES 2024 혁신상을 받았다.
- 2023-10-23 · DockerSSD의 SSD 가상화 연구가 HPCA 2024에 채택됐다.
- 2023-10-16 · 연구실이 2023 삼성미래기술육성사업에 선정돼 초거대 AI의 하드웨어·소프트웨어 공동 설계를 연구한다.
- 2023-09-20 · 정명수 교수가 베이징대학교의 CXL 기술 관련 저명인사 강연에 초청받았다.
- 2023-07-22 · SIGARCH 2023에서 CXL의 의미와 향후 방향을 다룬 초청강연을 했다.
- 2023-07-04 · OCP 2023 Regional Summit에서 CXL 메모리 공동 이용과 AI를 주제로 발표했다.
- 2023-05-25 · 서울대학교 초청강연에서 CXL 기반 검색과 메모리 확장 연구를 소개했다.
- 2023-05-20 · CXL-SSD의 확장 장치 기반 미리 읽기 연구가 HotStorage 2023에 채택됐다.
- 2023-04-29 · CXL-ANNS가 USENIX ATC 2023에 채택됐다.
- 2023-04-21 · 연구진이 삼성 글로벌 기술 심포지엄에서 연구를 발표하도록 초청받았다.
- 2023-03-10 · 고성능 가속기와 메모리 어레이 연구를 소개했다.
- 2023-02-21 · Junhyeok Jang이 HPCA 2023의 Heterogeneous and Composable Memory 워크숍 개회 강연에 초청받았다.
- 2023-02-18 · CPU·메모리 기업들과 CXL 워크숍에 참여했다.
- 2023-02-07 · Computer System Society 2023에서 CXL 메모리 공동 이용을 주제로 초청강연을 했다.
- 2023-01-28 · 공개 GNN 가속 프레임워크 GraphTensor가 IEEE IPDPS 2023에 채택됐다.
- 2023-01-08 · CXL 기반 영구 메모리 분리를 이용한 장애 대응 학습 연구가 IEEE Micro에 게재 승인됐다.
- 2023-01-07 · CXL 메모리 공동 이용 연구가 IEEE Micro에 초청돼 게재 승인됐다.
- 2022-12-13 · 메모리 내 연산과 AI 반도체 전략기술 심포지엄에서 CXL 기조강연을 했다.
- 2022-11-21 · SC 2022의 CXL 패널 토론에 참여하고 저명인사 강연에서 CXL 스위치와 시스템 설계를 시연했다.
- 2022-09-30 · 정명수 교수가 SC 2022와 함께 열리는 RESDIS의 개회 저명인사 강연에 초청받았다.
- 2022-08-26 · Miryeong Kwon이 삼성 최우수 논문상을 받았다.
- 2022-07-22 · 연구실이 CXL Forum 2022에 초청돼 CXL 플랫폼 2종 시연을 예고했다.
- 2022-07-21 · Miryeong Kwon이 NVMW Memorable Paper Award를 받았다.
- 2022-07-20 · CXL 메모리 확장 장치와 전체 시스템 연구가 The Next Platform에 소개됐다.
- 2022-06-20 · HotChips와 HotStorage에서 연구 4건을 시연할 예정이라고 알렸다.
- 2022-04-30 · DirectCXL을 이용한 메모리 공동 이용 연구가 USENIX ATC 2022에 채택됐다.
- 2022-04-30 · 지연 시간을 예측 가능하게 하는 Vigil-KV가 USENIX ATC 2022에 채택됐다.
- 2022-04-16 · 대규모 계산형 SSD 연구가 IITP 지원 대상으로 선정됐다.
- 2022-03-05 · CXL 기반 메모리 분리 기술을 공개했다.
- 2022-03-03 · 하드웨어·소프트웨어 공동 설계로 시스템 상태를 보존하는 LightPC가 ISCA 2022에 채택됐다.
- 2021-12-11 · 계산형 SSD로 GNN 서비스를 가속하는 HolisticGNN 연구가 FAST 2022에 채택됐다.

## 연락과 위치

- 교수 연구실: KAIST IT융합빌딩(N1) 411호.[^ee]
- 연구실 누리집 하단 위치: 대전광역시 유성구 대학로 291, N1 421호.[^research]
- 교수 연락처: 내선 7455, m.jung@kaist.ac.kr.[^ee]
[^home]: 연구실 누리집 첫 화면의 소속·약력·연구 관심사. <https://camelab.org/pmwiki.php> (2026-10-30 열람)
[^research]: Research 페이지의 AI Datacenter Fabrics and CXL Hardware–Software Co-Design, Computational Memory and Storage for AI/LLM Systems, Datacenter SSD Controllers and System Software, Modeling and Open Research Platforms for HW/SW Co-Design 등 연구 소개. 프로세서·가속기·메모리·저장장치를 연결하는 모듈형 AI 데이터센터, 데이터 가까이에서 처리하는 계산형 저장 시스템, 제어기·운영체제·평가 도구를 직접 설계한다고 밝힌다. <https://camelab.org/pmwiki.php/Main/ResearchProject> (2026-10-30 열람)
[^people]: People 페이지의 교수 약력, 현재 Members 및 Alumni의 Ph.D.·Master·Part-time Graduates·Undergraduate Interns·Visitors 구획. <https://camelab.org/pmwiki.php/Main/Members> (2026-10-30 열람)
[^pubs]: Publications 페이지의 Full Publication List와 Published and Issued Patents. <https://camelab.org/pmwiki.php/Main/Publications> (2026-10-30 열람)
[^news]: News 페이지의 날짜가 붙은 연구·강연·수상·지원 선정 게시 글. <https://camelab.org/pmwiki.php/Main/News> (2026-10-30 열람)
[^services]: Awards and Services 페이지의 Awards 구획. <https://camelab.org/pmwiki.php/Main/AwardsAndServices> (2026-10-30 열람)
[^ee]: KAIST 전기및전자공학부 정명수 교수 소개. 직위 「교수 (KAIST 석좌교수)」, 연구 분야, 박사학위, N1 411호·내선 7455·학교 이메일. <https://ee.kaist.ac.kr/professor/16603/> (2026-10-30 열람)
[^ais]: KAIST AI시스템학과 교수진의 정명수 겸임교수 항목. <https://aicollege.kaist.ac.kr/ais/faculty/index/page/4> (2026-10-30 열람)
[^aisemi]: KAIST 인공지능반도체대학원 교수진의 정명수 교수 항목. 소속 전기및전자공학부, 연구 분야 SSD 스토리지·비휘발성 메모리·컴퓨터 구조·파일 및 운영 시스템. <https://aisemi.kaist.ac.kr/professorall> (2026-10-30 열람)
[^gsai]: KAIST 김재철AI대학원 구성원의 겸임교수 구획에 있는 정명수 항목. 직위 전기및전자공학부 교수, 연구 분야 미래 메모리 및 가속 기술을 갖춘 AI 데이터센터 구조. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (2026-10-30 열람)
[^p1]: S. Kang 외, M. Jung, arXiv (2026). <https://doi.org/10.48550/arXiv.2602.00803> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2602.00803> (2026-10-30 열람)
[^p2]: D. Gouk 외, M. Jung, arXiv (2025). <https://doi.org/10.48550/arXiv.2506.15601> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.15601> (2026-10-30 열람)
[^p3]: S. Yi 외, J. Zhang, 2024 USENIX Annual Technical Conference (USENIX ATC 24), 141–156 (2024). <https://www.usenix.org/conference/atc24/presentation/yi-shushu> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.usenix.org/conference/atc24/presentation/yi-shushu> (2026-10-30 열람)
[^p4]: J. Jang 외, M. Jung, 2023 USENIX Annual Technical Conference (USENIX ATC 23), 585–600 (2023). <https://www.usenix.org/conference/atc23/presentation/jang> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.usenix.org/conference/atc23/presentation/jang> (2026-10-30 열람)
[^p5]: M. Kwon, D. Gouk, S. Lee, M. Jung, 20th USENIX Conference on File and Storage Technologies (FAST 22), 147–164 (2022). <https://www.usenix.org/conference/fast22/presentation/kwon> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.usenix.org/conference/fast22/presentation/kwon> (2026-10-30 열람)
[^p6]: M. Kwon 외, M. Jung, 2022 USENIX Annual Technical Conference (USENIX ATC 22), 755–772 (2022). <https://www.usenix.org/conference/atc22/presentation/kwon> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://www.usenix.org/conference/atc22/presentation/kwon> (2026-10-30 열람)

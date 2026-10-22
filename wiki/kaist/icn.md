# 컴퓨터 시스템 및 네트워크 연구실 (Computer System & Network Lab, CSNL)

**KAIST 전기및전자공학부 · 김동준 교수**

- 분야: 컴퓨터 구조, 대규모 분산 학습을 잇는 상호연결망과 집합 통신, 메모리·저장장치 시스템과 메모리 안 연산(PIM), GPU 온칩 네트워크와 하드웨어 보안, 사람을 돕는 모바일·상호작용 시스템
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 구조·운영체제[^home][^eeprof][^p4], AI 시스템·인프라[^p1][^p2], 컴퓨터 네트워크[^p1][^p2], 메모리 내 연산[^p3], 하드웨어 보안[^home][^p6][^p7], 인간–컴퓨터 상호작용[^research][^p8]
- 홈페이지: <https://icn.kaist.ac.kr>
- 근거와 출처: [CSNL 근거 페이지](icn-sources.md)

> 컴퓨터 구조와 상호연결망(프로세서·메모리·컴퓨터 사이에서 데이터를 나르는 연결망), 하드웨어 보안을 연구하는 연구실이다.[^home][^members]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 김동준 교수가 이끄는 연구실이다.[^eeprof] 누리집은 이름을 Computer System & Network Lab(CSNL)으로 적고,[^home] 전기및전자공학부와 반도체시스템공학과의 교수·연구실 목록은 「컴퓨터 시스템 및 네트워크 연구실」로 올린다.[^eeprof][^sselab] 누리집 첫 화면은 연구 분야를 세 칸으로 나눈다. 컴퓨터 구조(Computer Architecture) 칸은 딥러닝 가속기, 메모리 시스템, 온칩 네트워크(칩 안의 여러 부품을 잇는 통신망), 스케일아웃 시스템(컴퓨터를 여러 대 이어 규모를 키우는 시스템)을 포함한 차세대 컴퓨터 구조를 탐구한다고 적는다. 상호연결망(Interconnection Networks) 칸은 서로 다른 종류의 부품이 섞인 시스템에서 성능과 신뢰성이 높은 상호연결망 설계와 온칩 네트워크 구조를, 하드웨어 보안(Hardware Security) 칸은 GPU 같은 병렬 구조와 서버 규모의 NUMA 시스템(프로세서마다 가까운 메모리와 먼 메모리의 접근 시간이 다른 다중 프로세서 서버)에 대한 마이크로아키텍처(프로세서 내부 구현 구조) 수준의 공격을 든다.[^home] 학생 모집 안내는 컴퓨터 구조, GPU, 하드웨어 보안, 딥러닝 구조에 관심 있는 학생을 찾는다고 적는다.[^home]

대표 논문은 상호연결망을 규모를 키울 수 있는 시스템의 핵심 부품으로 보고, 분산 학습(인공지능 모델 학습을 여러 컴퓨터에 나눠 하는 방식)에서 상호연결망의 통신 대역폭이 집합 통신(여러 컴퓨터가 함께 데이터를 모으고 나누는 통신) 성능을 바로 좌우한다고 적고,[^p1] 딥러닝의 학습과 추론에서 여러 컴퓨터 사이의 집합 통신이 전체 성능을 정하는 핵심 요소라고 적는다.[^p2] 같은 관점을 메모리 안 연산(PIM, 계산 장치를 메모리 가까이 옮겨 데이터 이동을 줄이는 방식) 시스템에도 적용해, 실제 PIM 시스템에서 연산 장치 사이의 통신이 확장성을 가로막는다는 것을 보였다.[^p3]

연구 페이지는 지금까지의 연구를 여섯 칸으로 소개한다. 대규모 네트워크에서 트래픽을 적은 수의 링크로 모아 나머지 링크의 전력을 미리 끄는 전력 관리 방법 TCEP(ISCA 2018), 합성곱 신경망 학습에서 가중치 기울기(모델의 가중치를 고칠 방향을 담은 값)의 통신량을 줄이는 다차원 병렬 학습 MPT(MICRO 2018), NUMA 서버의 프로세서 사이 연결망 중재가 만드는 성능 불공정 분석, 다중 소켓 서버의 프로세서 사이 연결망 하드웨어를 악용해 운영체제 커널을 고치지 않고도 피해자의 메모리 영역에 권한 없이 접근하는 루트킷(침입한 컴퓨터에서 악성 프로그램을 숨기는 도구) PIkit(USENIX Security 2016), 하이브리드 메모리 큐브로 만든 메모리 네트워크로 여러 GPU의 메모리 관리를 쉽게 하는 연구, 그리고 감지와 개입을 위한 모바일 시스템(Mobile Systems for Detection & Intervention)이다.[^research][^pubs]

최근 연구는 네 갈래로 모인다. 첫째, **대규모 분산 학습을 잇는 상호연결망과 집합 통신**이다. 분산 학습에서 기울기 조각 일부를 무작위로 건너뛰어 집합 통신을 빠르게 하는 SkipReduce를 제안했고,[^p1] 2차원 메시(장치를 가로세로 격자로 놓고 이웃한 장치끼리 잇는 연결 구조) 연결망의 성질을 그대로 활용하는 집합 통신 알고리즘 TidalMesh를 만들었다.[^p2] 둘째, **메모리·저장장치 시스템과 메모리 안 연산**이다. 실제 상용 PIM 시스템을 평가해 연산 장치 사이 통신이 확장성의 한계라는 것을 보였고,[^p3] SSD(플래시 메모리로 만든 저장장치) 안의 플래시 컨트롤러들을 온칩 네트워크로 이어 입출력 경로와 정리 작업 경로를 나누는 Decoupled SSD를 제안했으며,[^p4] 낸드 플래시 패키지 안 여러 다이(웨이퍼에서 잘라 낸 칩 하나)의 순간 전류가 겹치지 않도록 다이 사이에서 순서를 정하는 N-DIPPER를 만들었다.[^p5] 셋째, **GPU 온칩 네트워크와 하드웨어 보안**이다. 여러 세대의 NVIDIA GPU에서 온칩 네트워크의 지연과 대역폭을 실제로 재어 코어 위치에 따라 지연이 다르다는 것을 보였고,[^p6] GPU의 온칩 대역폭 경쟁이 정보를 새게 하는 부채널 공격(실행 시간 같은 간접 신호로 비밀을 알아내는 공격)을 보인 뒤 이를 막는 중재 방법을 제안했다.[^p7] 넷째, **사람을 돕는 모바일·상호작용 시스템**이다. 짧은 영상 플랫폼의 넘기기 화면과 추천 기능이 어린이의 기억력에 주는 영향을 실험으로 살폈다.[^p8] 최근 논문 목록에는 완전 동형 암호(암호를 풀지 않고 계산하는 암호 방식) 가속기 연구(ISCA 2022, MICRO 2022), 대규모 언어 모델의 분산 시스템에서 계산과 통신을 겹치는 연구(MICRO 2026), 소셜 미디어의 MBTI 사용(CSCW 2025)과 이메일 사용 습관(MobileHCI 2025)을 다룬 연구도 있다.[^pubs]

## 주요 연구 주제

### 1. 대규모 분산 학습을 잇는 상호연결망과 집합 통신

분산 학습의 기울기 일부를 건너뛰는 집합 통신 SkipReduce, 2차원 메시 연결망에 맞춘 집합 통신 알고리즘 TidalMesh, 고기수(high-radix) 네트워크의 적응형 경로 선택.[^p1][^p2][^pubs] 대표 논문 1, 2.

### 2. 메모리·저장장치 시스템과 메모리 안 연산

실제 PIM 시스템의 확장성 평가, 플래시 컨트롤러를 네트워크로 잇는 SSD 구조, 낸드 플래시 다이 사이의 최대 전력 관리.[^p3][^p4][^p5] 대표 논문 3–5.

### 3. GPU 온칩 네트워크와 하드웨어 보안

실제 GPU 온칩 네트워크의 지연·대역폭 분석, 온칩 연결망 경쟁을 이용한 부채널 공격과 이를 막는 중재 방법.[^p6][^p7] 대표 논문 6, 7.

### 4. 사람을 돕는 모바일·상호작용 시스템

짧은 영상 플랫폼의 넘기기 화면과 추천 기능이 어린이의 단기 기억과 작업 기억에 주는 영향.[^p8][^research] 대표 논문 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 김동준 교수가 마지막 저자인 학회·학술지 논문을 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [SkipReduce: (Interconnection) Network Sparsity to Accelerate Distributed Machine Learning](https://doi.org/10.1145/3725843.3756092) · MICRO 2025 | 상호연결망은 규모를 키울 수 있는 시스템의 핵심 부품이며, 그 통신 대역폭이 분산 학습의 집합 통신 성능을 바로 좌우한다. 통신 중의 기울기(패킷) 일부를 무작위로 건너뛰어도 정확도에 주는 영향이 작다는 점을 확인했다. 다만 기울기를 하나씩 건너뛰면 집합 통신이 모두 맞춰 움직이는 성질 때문에 정보만 잃고 통신은 빨라지지 않아, 기울기 조각 단위로 건너뛰어 AllReduce(모든 컴퓨터의 값을 합쳐 다시 모두에게 나눠 주는 통신)의 일부 단계를 생략하는 SkipReduce를 제안했다. 같은 컴퓨터의 기울기만 반복해서 건너뛰면 치우침이 생겨 정확도가 떨어지므로 건너뛸 조각을 무작위로 바꾸었고, 층마다 통신 희소성이 달라 희소한 층에만 SkipReduce를 적용했다. NCCL의 링 방식 AllReduce 위에 구현했고, 기본 AllReduce보다 목표 정확도에 이르는 시간이 최대 1.58배 빨라지면서 최종 학습 정확도는 유지됐다.[^p1] | 1저자 H. Kasan, 마지막 저자 김동준 |
| 2 | 2025 | [TidalMesh: Topology-Driven AllReduce Collective Communication for Mesh Topology](https://doi.org/10.1109/hpca61900.2025.00114) · HPCA 2025 | 딥러닝의 학습과 추론에서 여러 컴퓨터 사이의 집합 통신은 전체 성능을 정하는 핵심 요소다. AllReduce의 성능은 쓰는 알고리즘(논리 토폴로지)과 컴퓨터들을 실제로 잇는 연결 구조(물리 토폴로지)에 함께 달려 있다. 기존 연구가 정해진 물리 연결 구조에 기존 알고리즘을 맞추는 방식이었다면, 이 연구는 연결 구조의 성질에서 출발해 새 알고리즘을 만드는 방식을 택했다. 여러 스케일아웃 시스템에 쓰이는 2차원 메시 구조에서 양 끝 노드 사이로 데이터 흐름을 밀어 보내는 TidalMesh AllReduce를 제안했고, 대역폭 부담을 줄인 Sparse TidalMesh와, 집합 통신을 펼쳐 AllReduce의 여러 단계를 겹치는 소프트웨어 파이프라이닝도 보였다. 8×8 배열 64노드 2차원 메시에서 여러 딥러닝 모델의 AllReduce 성능이 기존 최고 방법보다 최대 24% 좋아졌고, 논리 링 알고리즘의 단순함은 유지했다.[^p2] | 1저자 D. Lim, 마지막 저자 김동준 |
| 3 | 2024 | [Scalability Limitations of Processing-in-Memory using Real System Evaluations](https://doi.org/10.1145/3639046) · Proceedings of the ACM on Measurement and Analysis of Computing Systems (SIGMETRICS 2024) | 메모리 안 연산(PIM)은 계산을 메모리 가까이 옮겨 새로운 작업을 빠르게 하려는 방식으로, 메모리 회사들이 여러 PIM 시스템을 내놓았다. UPMEM PIM 기반의 실제 시스템을 폭넓게 평가해, PIM에 이점이 있지만 PIM 노드 수가 늘수록 확장성의 한계가 드러난다는 것을 보였다. 특히 많은 작업에 흔한 집합 통신이 문제였다. AllReduce가 필요한 추천 시스템의 임베딩 테이블과, 모든 노드가 서로 데이터를 주고받아야 하는 완전 동형 암호의 NTT 커널을 분석하고 데이터 분할을 바꿔 PIM 구조에 효율적으로 옮기는 방법을 보였다. 그러나 각 PIM 연산 장치는 자기 메모리에만 접근할 수 있어 노드 사이 통신이 호스트 CPU를 거쳐야 하고, 이것이 성능을 크게 떨어뜨렸다. 앞으로의 PIM 구조에는 PIM 노드 사이의 효율적인 통신망과 이를 위한 하드웨어·소프트웨어 지원이 필요하다고 주장했다.[^p3] | 1저자 G. Jonatan, 마지막 저자 김동준 |
| 4 | 2023 | [Decoupled SSD: Rethinking SSD Architecture through Network-based Flash Controllers](https://doi.org/10.1145/3579371.3589096) · ISCA 2023 | 낸드 플래시 기반 SSD는 빠른 NVMe 연결과 내부 플래시 대역폭으로 입출력 요청을 빠르게 처리한다. 그런데 SSD의 관리 소프트웨어(FTL)는 입출력 외에 쓰레기 수집(쓸모없어진 데이터 칸을 정리해 다시 쓸 수 있게 하는 작업) 같은 관리 작업도 하며, 이 둘이 시스템 버스와 DRAM 같은 자원을 함께 쓰면서 서로 방해해 성능이 떨어진다. 코어·시스템 버스·DRAM이 있는 앞단과 플래시 메모리가 있는 뒷단을 떼어 놓는 Decoupled SSD(dSSD)를 제안하고, 플래시 컨트롤러들을 잇는 온칩 네트워크(fNoC)로 입출력 경로와 쓰레기 수집 경로를 나눴다. fNoC를 통한 전역 복사 명령과, 플래시 컨트롤러 안에서 묶음 블록을 재활용하는 방법도 제안했다. 평가에서 입출력 대역폭이 최대 42.7%, 쓰레기 수집 성능이 63.8% 좋아졌고 꼬리 지연(요청 가운데 늦게 끝나는 일부가 겪는 지연)이 평균 약 31.4배 개선됐으며, 수명이 약 23% 늘었다.[^p4] | 1저자 J. Kim, 마지막 저자 김동준 |
| 5 | 2026 | [N-DIPPER: A Distributed Inter-Die Peak Power Management Network for Nand Systems](https://doi.org/10.1109/hpca68181.2026.11408558) · HPCA 2026 | 낸드 플래시가 계속 확장되면서 워드라인을 높이 쌓고 프로그램 전압이 높아져, 한 패키지 안 여러 다이의 순간 최대 전류가 겹치는 일이 심해졌다. 이 겹침은 전원 관리 칩(PMIC)의 한도를 넘게 하고 전압 강하와 신뢰성 저하를 부른다. 컨트롤러가 속도를 늦추는 식의 고정된 방법은 공정·전압·온도 변화와 마모로 다이 사이 시점과 전류 크기가 계속 달라져 넉넉한 여유를 둬야 하고, 그만큼 병렬성과 성능을 잃는다. 패키지 안의 가벼운 다이 간 연결망으로 큰 전류가 필요한 단계를 실행 중에 함께 조율하는 N-DIPPER를 제안했다. 연결망에서 토큰을 주고받아 큰 전류 단계를 차례로 실행하게 하고, 소자 정보를 써서 최악 조건에 맞춘 여유를 쓰지 않게 했다. 여러 작업과 다이 구성에서 PMIC 한도 위반을 모두 없애면서 최대 전력 관리를 하지 않을 때 처리량의 97%를 유지했다.[^p5] | 1저자 J. Park, 마지막 저자 김동준 |
| 6 | 2024 | [Uncovering Real GPU NoC Characteristics: Implications on Interconnect Architecture](https://doi.org/10.1109/micro61859.2024.00070) · MICRO 2024 | GPU 같은 고처리량 프로세서에서 많은 코어와 메모리 구역을 잇는 온칩 네트워크(NoC)는 핵심 부품이다. 여러 세대의 최신 NVIDIA GPU에서 실제 NoC의 지연과 대역폭을 자세히 분석했다. 코어와 메모리 구역 사이의 지연은 GPU 안의 물리적 위치에 따라 고르지 않아 온칩 지연이 최대 약 70% 차이 났지만, 코어에서 메모리 구역으로 가는 대역폭은 거의 고르게 나타났다. 여러 GPU '파티션'으로 이루어진 최근 GPU는 파티션 사이에서 통신할 때 지연과 대역폭 특성이 달랐다. 이 분석을 바탕으로 부채널 공격의 시간 측정과 NoC 구조에 주는 뜻을 논의했고, 코어 위치가 실행 시간에 영향을 주므로 고르지 않은 지연이 GPU 안의 시간 부채널 공격에 쓰일 수 있음을 보였다.[^p6] | 1저자 Z. Jin, 마지막 저자 김동준 |
| 7 | 2024 | [Ghost Arbitration: Mitigating Interconnect Side-Channel Timing Attacks in GPU](https://doi.org/10.1109/micro61859.2024.00086) · MICRO 2024 | 온칩 네트워크는 여러 코어가 함께 쓰는 자원이고, 함께 쓰는 자원은 부채널 공격으로 이어질 수 있다. GPU의 온칩 대역폭을 두고 벌어지는 경쟁이 세밀한 정보 유출을 일으킬 수 있음을 보였고, 사례로 실제 GPU에서 RSA 암호 키의 비트 정보가 새어 나가는 것을 보였다. 부채널에서 얻은 연결망 특성(interconnect-gram)으로 GPU에서 돌아가는 프로그램을 알아낼 수 있다는 것도 설명했다. 이를 막으려고, 다른 노드가 차례를 받을 때 생기는 '유령' 요청을 기록해 연결망 경쟁이 정보 유출에 쓰이지 않게 하는 고스트 중재(ghost arbitration)를 제안했다. 공격자가 중재 방식을 역으로 알아내면 단순한 구현은 여전히 정보가 샐 수 있어, 악의적인 통신 패턴을 활용하는 가중 고스트 중재도 제안했다. 기존의 안전한 중재 방식인 엄격한 시분할 방식보다 성능이 최대 4배 좋았다.[^p7] | 1저자 Z. Jin, 마지막 저자 김동준 |
| 8 | 2026 | [Endless Swipes and Recommendations: The Impact of Short-Form Video Platforms on Context-Switching and Children’s Working Memory](https://doi.org/10.1145/3772318.3791959) · CHI 2026 | 짧은 영상 플랫폼은 점점 인기를 얻지만, 빠른 전환이 어린이의 인지 기능에 주는 영향은 잘 알려져 있지 않다. 참가자 180명을 여러 집단으로 나눈 실험으로 YouTube Shorts가 단기 기억과 작업 기억(머릿속에 정보를 잠시 붙잡아 두고 다루는 능력)에 주는 영향을 숫자 따라 말하기 과제(앞으로·거꾸로)로 쟀다. 쉬운 넘기기 화면과 추천 기능이라는 두 핵심 기능을 조작한 네 조건과, 긴 영상 기준 조건 둘을 비교했다. 기능 조합과 기준 조건 비교는 단기 기억이나 작업 기억의 변화와 관련이 없었다. 그러나 넘기기 조작은 영상 전환을, 추천 콘텐츠는 주제 전환을 늘렸고, 두 전환이 함께 많을수록 작업 기억 성적에 경계 수준의 영향이 나타났고 단기 기억은 영향을 받지 않았다.[^p8] | 1저자 C. Siy, 마지막 저자 김동준 |

## 교수와 전문 분야

김동준(John Kim) 교수는 미국 Cornell University에서 학사(B.S.)와 공학 석사(M.Eng)를, Stanford University에서 박사 학위를 받았다.[^members] 전기및전자공학부 교수 소개는 학위를 "Ph.D. (2008) Stanford University"로 적는다.[^eeprof] 연구실 소개에 따르면 대학원에 가기 전에 Intel과 Motorola에서 여러 마이크로프로세서의 설계에 참여했다.[^members] 전기및전자공학부 교수 소개는 직위를 교수로, 괄호 안에 "IEEE 석학회원"으로 적고, 소속 디비전을 Computer division으로 적는다.[^eeprof] 반도체시스템공학과 교수진 목록에도 올라 있고 연구 분야는 "컴퓨터, 인공지능 및 소프트웨어"로 분류된다.[^ssefac]

전기및전자공학부 교수 소개는 주요 연구분야를 Security, Computer Architecture, Software Systems & Networking으로, 주요 연구를 컴퓨터 시스템, 컴퓨터 구조, 하드웨어 보안으로 적는다.[^eeprof] 연구실 소개는 교수의 연구 관심을 컴퓨터 구조, 상호연결망, 보안, 모바일 시스템으로 적는다.[^members] 교수 소개의 대표업적에는 TCEP(ISCA 2018), 가려움 관리를 돕는 착용형 모바일 시스템 Itchtector(CHI 2017), 프로세서 사이 연결망 루트킷 PIkit(USENIX Security 2016), 메모리 네트워크로 여러 GPU를 잇는 설계(MICRO 2014), Dragonfly 토폴로지(ISCA 2008)가 올라 있다.[^eeprof]

랩 Publications 페이지의 목록을 시기별로 보면, 2005–2008년 논문은 대규모 상호연결망에 쓰는 고기수 라우터의 구조, Flattened Butterfly·Dragonfly 같은 연결 구조(토폴로지), 적응형 경로 선택을 다룬다. 2009–2014년 논문은 많은 코어를 가진 프로세서와 GPU의 온칩 네트워크, 나노포토닉스(나노미터 단위 구조로 빛을 다루는 기술) 온칩 연결망, 메모리 중심 시스템 연결망을 다루고, 2014–2018년 논문은 여러 GPU 시스템, 서버 프로세서 사이 연결망의 보안과 공정성, 아이 돌봄과 언어 발달을 돕는 모바일 시스템을 다룬다. 2018년 이후 논문은 딥러닝 학습 시스템, GPU 구조, 분산 학습의 집합 통신, SSD와 PIM, GPU 하드웨어 보안이 중심이다.[^pubs] 목록에는 "Best Paper Award"로 표시된 논문 두 편(PACT 2013 메모리 중심 시스템 연결망, CSCW 2014 TalkBetter)과 "Best Paper Finalist"(PACT 2016), "Best student paper finalist"(SC 2006) 표시, IEEE Micro Top Picks에 실린 Dragonfly 토폴로지 글(2009)도 있다.[^pubs]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 분산 학습을 위한 상호연결망과 집합 통신 알고리즘이다(대표 논문 1, 2).[^p1][^p2] 둘째, 메모리 안 연산과 SSD·낸드 플래시 같은 저장장치 시스템의 구조다(대표 논문 3–5).[^p3][^p4][^p5] 셋째, GPU 온칩 네트워크의 실측 분석과 이를 노리는 부채널 공격·방어다(대표 논문 6, 7).[^p6][^p7] 넷째, 어린이와 가족의 기기 사용을 살피는 상호작용 연구다(대표 논문 8).[^p8]

## 응용 분야

대표 논문은 여러 컴퓨터로 인공지능 모델을 학습하는 분산 학습의 통신 가속(NCCL 링 AllReduce 위 구현),[^p1] 딥러닝 학습과 추론에 쓰는 2차원 메시 스케일아웃 시스템,[^p2] 추천 시스템의 임베딩 테이블과 완전 동형 암호의 NTT 커널을 돌리는 PIM 시스템,[^p3] 낸드 플래시 SSD의 입출력 성능·수명,[^p4] 낸드 패키지의 전원 관리 칩 한도 관리,[^p5] GPU에서 암호 키 유출을 막는 보안 설계[^p7]를 대상으로 한다. 최근 논문 목록에는 완전 동형 암호 가속기(ISCA 2022, MICRO 2022)와 대규모 언어 모델 분산 시스템(MICRO 2026) 연구도 있다.[^pubs] 랩이 적은 졸업생의 진로로는 NVIDIA Research, XCENA, MangoBoost, ARM Research(now assistant professor at POSTECH), ETRI(now assistant professor at Kangwon University), Samsung Research, Furiosa AI(박사 졸업생)와 Samsung, Samsung LSI, Samsung Foundry, Samsung Memory, Samsung DS, SK Hynix, BOS Semiconductor, Huawei Research Center Switzerland, Codeplay Software, KaKao Brain, Naver, Nat Games, Tmax Soft(석사 졸업생)가 있다.[^members]

## 구성원

2026년 10월 22일 랩 Members 페이지 기준이다. Ph.D Students 칸 9명과 M.S. Students 칸 11명이며, 과정은 칸 이름(박사과정, 석사과정)을 옮겼다. 시작은 카드에 적힌 KAIST 합류 시기이고, 연구 주제는 카드의 연구 주제 문장, 이메일은 카드에 적힌 학교 이메일이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Cheryl Siy | 박사과정 | Sep. 2020 | Human Computer Interface | cmsiy@kaist.ac.kr | 8 |
| Gilbert Jonatan | 박사과정 | Sep. 2021 | interconnection network & homomorphic encryption | gilbertjonatan@kaist.ac.kr | 3 |
| Jihyun Kim | 박사과정 | Sep. 2022 | hardware security for emerging architectures | kimjihyun@kaist.ac.kr |  |
| Jonghoon Kang | 박사과정 | Sept 2023 | System Architecture mainly for AI, NoC, and memory subsystem | jh.kang@kaist.ac.kr |  |
| Dongkyun Lim | 박사과정 | March 2024 | collective communication and microarchitectural security | dk.lim@kaist.ac.kr | 2 |
| Jina Song | 박사과정 | March 2024 | interconnection networks and AI acceleration | s_jina@kaist.ac.kr | 7 |
| Gyeonggeun Jung | 박사과정 | March 2025 | interconnection networks & processing-in-memory | gyeonggeun@kaist.ac.kr |  |
| Yaejoon Oh | 박사과정 | March 2025 | interconnection network & computer architecture | ohyeah5@kaist.ac.kr |  |
| Jiyoung Lim | 박사과정 | March 2025 | AI acceleration | jiyounglim@kaist.ac.kr |  |
| Hyeonwoo Sung | 석사과정 | September 2024 | processing-in-memory | hwsung@kaist.ac.kr |  |
| Seongwon Jo | 석사과정 | March 2025 | computer architecture and interconnection network | seongwon.jo@kaist.ac.kr |  |
| Dang Vu Hai | 석사과정 | March 2025 | performance modeling and computer architecture | dang.vh@kaist.ac.kr |  |
| Kyungsoo Lee | 석사과정 | July 2025 | on-chip interconnection network | kyungsoo.lee@kaist.ac.kr |  |
| Gyeongjae Lee | 석사과정 | September 2025 | Interconnection Networks | gyeongjae@kaist.ac.kr |  |
| Hwanjin Song | 석사과정 | March 2026 | processing-in-memory | hwanjin.song@kaist.ac.kr |  |
| Yeonghun Kim | 석사과정 | March 2026 | Interconnection Network & Computer Architecture | yh_kim@kaist.ac.kr |  |
| Wooseong Baek | 석사과정 | March 2026 | collective communication | wooseong.baek@kaist.ac.kr |  |
| Doheon Kwon | 석사과정 | March 2026 | interconnection network and AI acceleration | dhkwon03@kaist.ac.kr |  |
| Piljun Oh | 석사과정 | March 2026 | processor-memory interconnect | opj369@kaist.ac.kr |  |
| Duhoe Lee | 석사과정 | September 2026 | interconnection networks, memory systems and AI acceleration | sridoo@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Members 페이지 Alumni 칸의 박사(Ph.D.) 9명과 석사(Masters) 24명이다. 석사 졸업생에는 연도가 적혀 있고 박사 졸업생에는 연도가 없다. 진로는 랩이 적은 곳이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hans Kasan | Ph.D. | NVIDIA Research |
| Kihoon Jung | Ph.D. | TBA |
| Hyojun Son | Ph.D. | XCENA |
| Jiho Kim | Ph.D. | MangoBoost |
| Gwangsun Kim | Ph.D. | ARM Research (now assistant professor at POSTECH) |
| Wonjun Song | Ph.D. | ETRI (now assistant professor at Kangwon University) |
| Jongin Lee | Ph.D. | Startup company |
| Seokwoo Song | Ph.D. | Samsung Research |
| Byungchul Hong | Ph.D. | Furiosa AI |
| Jinwoo Park | Masters (2026) | Samsung |
| Beomsu Kim | Masters (2026) |  |
| Yuanxin Pang | Masters (2025) |  |
| Christopher Rocca | Masters (2025) | Huawei Research Center Switzerland |
| Gyubeom Jeon | Masters (2025) | Samsung |
| Xiangyu Wu | Masters (2024) | PhD student at HKUST (GZ) |
| Sanzhar Shabdarov | Masters (2024) | Samsung Foundry |
| Hyuntaek Cho | Masters (2023) | SK Hynix |
| Yassawe Kainolda | Masters (2023) | TBA |
| Tho Mai | Masters (2023) | BOS Semiconductor |
| Jangpyo Lee | Masters (2022) | Samsung LSI |
| Jiheon Lee | Masters (2022) | Samsung LSI |
| Sangheon Lee | Masters (2021) | Samsung Memory |
| Muhammad Tanvir | Masters (2021) | Codeplay Software |
| Jaeguk Ahn | Masters (2021) | Samsung DS |
| Jaeyoung Choi | Masters (2021) | Samsung LSI |
| Sanghun Cho | Masters (2021) | KaKao Brain |
| Gi Hong Do | Masters (2021) | Nat Games |
| Cheolgyu Jin | Masters (2020) | Samsung Research |
| Gyuyoung Gwak | Masters (2020) | Tmax Soft |
| Ian Libao | Masters (2020) | KAIST (Graduate School of Culture Technology) |
| Youngkwang Han | Masters (2019) | KAIST (graduate school) |
| Jaemoon Sim | Masters (2018) | Naver |
| Yeonju Ro | Masters (2018) | Samsung Research (now PhD student at UT Austin) |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021–2026년 구역에 실린 27편이다. 연도는 페이지의 연도 구역이고, 제목·저자·학회와 학술지 표기는 랩 표기 그대로다. 2025년의 I-PIM 한 편은 랩이 포스터(POSTER)로 표시한 발표다. 2026년의 MICRO 2026 논문 한 편은 첫 화면이 2026년 7월에 채택을 알린 논문으로, 학회 발표 전이라 「MICRO 2026 채택」으로 표시했다.[^pubs][^home]

**2026**

- Jonghoon Kang, Zhixian Jin, John Kim. "In-Flight Collectives: Characterizing and Accelerating Compute-Communication Overlap in Distributed LLM System". *In Proceedings of the 59th International Symposium on Microarchitecture (MICRO), Athens, Greece, October-November 2026* (MICRO 2026 채택).
- Cheryl Siy, Kihoon Jung, Seokwoo Song, Kwan Hong Lee, and John Kim. "Endless Swipes and Recommendations: The Impact of Short-Form Video Platforms on Context-Switching and Children’s Working Memory". *In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI ’26), Barcelona, Spain, April 2026*.
- Jinwoo Park, John Kim. "N-DIPPER: A Distributed Inter-die Peak Power Management Network for NAND Systems". *In Proceedings of the 32nd IEEE International Symposium on High-Performance Computer Architecture (HPCA), Sydney, Australia, January – February, 2026*.

**2025**

- Cheryl Siy, Yuanxin Pang, Kihoon Jung, John Kim. "One MBTI does not Fit All: Perceptions and Usage of MBTI in Social Media". *Proceedings of the ACM in Human-Computer Interaction (PACMHCI-CSCW), Bergen, Norway, October 2025*.
- Hans Kasan, Dennis Abts, Jungwook Choi, John Kim. "SkipReduce: (Interconnection) Network Sparsity to Accelerate Distributed Machine Learning". *In Proceedings of the 58th International Symposium on Microarchitecture (MICRO), Seoul, Korea, October 2025*.
- Cheryl Siy, Gihong Do, Kihoon Jung, Kwan Hong Lee, John Kim. "E-litter: Nudging Email Usage Behavior One Byte at a Time". *Proceedings of the ACM on Human-Computer Interactions (PACMHCI-MobileHCI), Sharm El-Sheikh, Egypt, September 2025*.
- Gyubeom Jeon, Jiho Kim, Zhixian Jin, Jangpyo Lee, Hyojun Son, John Kim. "I-PIM: Indirect Address Hashing for Efficient Processing-In-Memory on GPU". *in the proceedings of the 62nd Annual Design Automation Conference 2025 (DAC), San Francisco, CA, June 2025 (POSTER)*.
- Dongkyun Lim, John Kim. "TidalMesh: Topology-Driven AllReduce Collective Communication for Mesh Topology". *In Proceedings of the 31st International Symposium on High Performance Computer Architecture (HPCA), Las Vegas, USA, March 2025*.
- Hyojun Son, Gilbert Jonatan, Wu Xiangyu, Haeyoon Cho, Kaustubh Shivdikar, José L. Abellán, Ajay Joshi, David Kaeli, John Kim. "PIMnet: A Domain-Specific Network for Efficient Collective Communication in Scalable PIM". *In Proceedings of the 31st International Symposium on High Performance Computer Architecture (HPCA), Las Vegas, USA, March 2025*.

**2024**

- Zhixian Jin, Christopher Rocca, Jiho Kim, Hans Kasan, Minsoo Rhu, Ali Bakhoda, Tor Aamodt, John Kim. "Uncovering Real GPU NoC Characteristics: Implications on Interconnect Architecture". *In Proceedings of the 57th International Symposium on Microarchitecture (MICRO), Austin, TX, Nov. 2024*.
- Zhixian Jin, Jaeguk Ahn, Jiho Kim, Hans Kasan, Jina Song, Wonjun Song, John Kim. "Ghost Arbitration: Mitigating Interconnect Side-Channel Timing Attacks in GPU". *In Proceedings of the 57th International Symposium on Microarchitecture (MICRO), Austin, TX, Nov. 2024*.
- Gilbert Jonatan, Haeyoon Cho, Hyojun Son, Xiangyu Wu, Neal Livesay, Evelio Mora, Kaustubh Shivdikar, José L. Abellán, Ajay Joshi, David Kaeli, and John Kim. "Scalability Limitations of Processing-in-Memory using Real System Evaluations". *in the Proceedings of the ACM on Measurement and Analysis of Computing Systems (SIGMETRICS), Venice, Italy, March 2024*.

**2023**

- Jiho Kim, Myoungsoo Jung, John Kim. "Decoupled SSD: Rethinking SSD Architecture through Network-based Flash Controllers". *in the proceedings of International Symposium on Computer Architecture (ISCA) , Orlando, FL, USA, June 2023*.
- Hans Kasan, John Kim. "VVQ: Virtualizing Virtual Channel for Cost-Efficient Protocol Deadlock Avoidance". *in the proceedings of International Symposium on High-Performance Computer Architecture (HPCA) , Montreal, Canada, Feb. 2023*.
- Jo Sanghoon, Hyojun Son, John Kim. "Logical/Physical Topology-Aware Collective Communication in Deep Learning Training". *in the proceedings of International Symposium on High-Performance Computer Architecture (HPCA) , Montreal, Canada, Feb. 2023*.

**2022**

- Jiho Kim, Seokwon Kang, Yongjun Park, John Kim. "Networked SSD: Flash Memory Interconnection Network for High-Bandwidth SSD". *in the proceedings of International Symposium on Microarchitecture (MICRO) , Chicago, IL, October 2022*.
- Jongmin Kim, Gwangho Lee, Sangpyo Kim, Gina Sohn, John Kim, Minsoo Rhu, and Jung Ho Ahn. "ARK: Fully Homomorphic Encryption Accelerator with Runtime Data Generation and Inter-Operation Key Reuse". *in the proceedings of International Symposium on Microarchitecture (MICRO) , Chicago, IL, October 2022*.
- Hans Kasan, Gwangsun Kim, Yung Yi, and John Kim. "Dynamic Global Adaptive Routing in High-radix Networks". *in the proceedings of International Symposium on Computer Architecture (ISCA) , New York, NY, June 2022*.
- Sangpyo Kim, Jongmin Kim, Michael Jaemin Kim, Wonkyung Jung, Minsoo Rhu, John Kim, and Jung Ho Ahn. "BTS: An Accelerator for Bootstrappable Fully Homomorphic Encryption". *in the proceedings of International Symposium on Computer Architecture (ISCA) , New York, NY, June 2022*.
- Dennis Abts, Garrin Kimmell, Andrew Ling, John Kim (KAIST); Matt Boyd, Andrew Bitar, Sahil Parmar, Ibrahim Ahmed, Roberto DiCecco, David Han, John Thompson, Michael Bye, Jennifer Hwang, Jeremy Fowers, Peter Lillian, Ashwin Murthy, Elyas Mehtabuddin, Chetan Tukur, Thomas Sohmers, Kris Kang, Jonathan Ross. "A Software-defined Tensor Streaming Multiprocessor for Large-Scale Machine Learning". *in the proceedings of International Symposium on Computer Architecture (ISCA) , New York, NY, June 2022*.

**2021**

- Jiho Kim, Myoungsoo Jung, John Kim. "Decoupled SSD: Reducing Data Movement on NAND-Based Flash SSD". *in IEEE Computer Architecture Lectures , Jan. 2021*.
- Jaeguk Ahn, Jiho Kim, Hans Kasan, Leila Delshadtehrani, Wonjun Song, Ajay Joshi, John Kim. "Network-on-Chip Microarchitecture-based Covert Channel in GPUs". *in the proceedings of IEEE/ACM International Symposium on Microarchitecture Oct. 2021*.
- Yeonju Ro, Seongwook Jin, Jaehyuk Huh, John Kim. "Ghost Routing to Enable Oblivious Computation on Memory-centric Networks". *in the proceedings of International Symposium on Computer Architecture (ISCA) , Virtual June 2021*.
- Trinayan Baruah, Kaustubh Shivdikar, Shi Dong, Yifan Sun, Saiful A Mojumder, Kihoon Jung, Jose L Abellan, Yash Ukidave, Ajay Joshi, John Kim, David Kaeli. "GNNMark: A Benchmark Suite to CharacterizeGraph Neural Network Training on GPUs". *IEEE International Symposium on Perfor- mance Analysis of Systems and Software (ISPASS) , Virtual March 2021*.
- Hans Kasan, John Kim. "The Case for Dynamic Bias in Global Adaptive Routing". *in IEEE Computer Architecture Lectures , Jan. 2021*.
- Jaeguk Ahn, Cheolgyu Jin, Jiho Kim, Minsoo Rhu, Yunsi Fei, David Kaeli, John Kim. "Trident: A Hybrid Correlation-Collision GPU Cache Timing Attack for AES Key Recovery". *in the proceedings of International Symposium on High-Performance Computer Architecture (HPCA), Virtual, Feb. 2021*.
- Kwauk Gyuyoung, Seungkwang Kang, Hans Kasan, Hyojune Son, John Kim. "BoomGate: Deadlock Avoidance in Non-Minimal Routing for High-Radix Networks". *in the proceedings of International Symposium on High-Performance Computer Architecture (HPCA), Virtual, Feb. 2021*.

## 소식

랩 첫 화면 Recent Publications 칸의 2021년 10월 이후 16건과 WELCOME 칸의 새 구성원 소식 10건이다. 날짜는 랩이 적은 달이고, 글은 랩 표기 그대로다.[^home]

- July 2026 · Congratulations, Jonghoon! Our “In-Flight Collectives: Characterizing and Accelerating Compute-Communication Overlap in Distributed LLM System” paper has been accepted at MICRO 2026
- March 2026 · Welcome Hwanjin Song, Yeonghun Kim, Wooseong Baek, Doheon Kwon, Piljun Oh to the lab!
- January 2026 · Congratulations, Cheryl! Our “Endless Swipes and Recommendations: The Impact of Short-Form Video Platforms on Context-Switching and Children’s Working Memory” paper has been accepted at CHI 2026
- November 2025 · Congratulations, Jinwoo! Our “N-DIPPER: A Distributed Inter-die Peak Power Management Network for NAND Systems” paper has been accepted at HPCA 2026
- Sept 2025 · Welcome Duhoe Lee to the lab!
- Sept 2025 · Welcome Gyeongjae Lee to the lab!
- July 2025 · Congratulations, Cheryl! Our “One MBTI does not Fit All: Perceptions and Usage of MBTI in Social Media” paper has been accepted at CSCW 2025
- July 2025 · Congratulations, Hans! Our “SkipReduce: (Interconnection) Network Sparsity to Accelerate Distributed Machine Learning” paper has been accepted at MICRO 2025
- July 2025 · Welcome Kyungsoo Lee to the lab!
- May 2025 · Congratulations, Cheryl! Our “E-litter: Nudging Email Usage Behavior One Byte at a Time” paper has been accepted at MobileHCI 2025
- March 2025 · Welcome Gyeonggeun Jung, Seongwon Jo, YaeJoon Oh, Jiyoung Lim, Dang Vu Hai, Jinwoo Park to the lab!
- November 2024 · Congratulations Dongkyun! Our “TidalMesh: Topology-Driven AllReduce Collective Communication for Mesh Topology” paper has been accepted at HPCA 2025
- November 2024 · Congratulations Hyojun! Our “PIMnet: A Domain-Specific Network for Efficient Collective Communication in Scalable PIM” paper has been accepted at HPCA 2025
- Sept 2024 · Welcome Hyeonwoo Sung to the lab!
- August 2024 · Congratulations Jihyun! Our “Ghost Arbitration: Mitigating Interconnect Side-Channel Timing Attacks” paper has been accepted at MICRO 2024
- August 2024 · Congratulations Jihyun! Our “Uncovering Real GPU NoC Characteristics: Implications on Interconnect Architecture” paper has been accepted at MICRO 2024
- March 2024 · Congratulations, Gilbert! Our “Scalability Limitations of Processing-in-Memory using Real System Evaluations” paper has been accepted at SIGMETRICS 2024
- March 2024 · Welcome Amin Hong, Dongkyun Lim, Beomsu Kim and Jina Song to the lab!
- Sept 2023 · Welcome Yuanxin Pang and Chistopher Rocca to the lab!
- March 2023 · Congratulations, Jiho! Our “Decoupled SSD Architecture through Network-based Flash Controllers” paper has been accepted at IEEE ISCA 2023
- March 2023 · Welcome Gyubeom Jeon to the lab!
- Oct 2022 · Congratulations, Hans! Our “VVQ: Virtualizing Virtual Channel for Cost-Efficient Protocol Deadlock Avoidance” paper has been accepted at HPCA 2023
- Sept 2022 · Welcome Jihyun Kim and Xiangyu Wu to the lab!
- July 2022 · Congratulations, Jiho! Our “Networked SSD: The Flash Memory Interconnection Network for High-Bandwidth SSD” paper has been accepted at IEEE MICRO 2022
- Mar 2022 · Congratulations, Hans! Our “Dynamic global adaptive routing in high-radix networks” paper has been accepted at IEEE ISCA 2022
- Oct 2021 · Congratulations! Our “Decoupled SSD: Reducing Data Movement on NAND-Based Flash SSD” paper has been accepted at IEEE CAL 2021

## 연락과 위치

- 연구실: N1 518 Kim Byeong-ho IT building, 291, Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea[^contact]
- 교수 연구실: IT융합빌딩(N1) 514호, 전화 042-350-7448[^eeprof][^ssefac]
- 전화: +82-42-350-7548(연구실), 팩스 +82-42-350-3510[^contact]
- 이메일: icnee@kaist.ac.kr(연구실), jjk12@kaist.ac.kr(교수)[^contact]
[^home]: 연구실 누리집 첫 화면 <https://icn.kaist.ac.kr/> (Research AREA, Recent Publications, WELCOME, OPENINGS 칸, 2026-10-22 열람)
[^research]: Research 페이지 <https://icn.kaist.ac.kr/index.php/research/> (2026-10-22 열람)
[^pubs]: Publications 페이지 <https://icn.kaist.ac.kr/index.php/publications/> (2026–2005년 구역과 Before 2005 구역, 2026-10-22 열람)
[^members]: Members 페이지 <https://icn.kaist.ac.kr/index.php/members/> (Professor, Ph.D Students, M.S. Students, Alumni 칸, 2026-10-22 열람)
[^contact]: Contact 페이지 <https://icn.kaist.ac.kr/index.php/contact/> (2026-10-22 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(김동준) <https://ee.kaist.ac.kr/professor/16047/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 학위, 대표업적, 2026-10-22 열람)
[^ssefac]: KAIST 반도체시스템공학과 교수진 목록 <https://sse.kaist.ac.kr/professor/> (2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^p1]: H. Kasan, D. Abts, J. Choi, J. Kim, Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture, 643-658 (온라인 2025-10-17). <https://doi.org/10.1145/3725843.3756092> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: D. Lim, J. Kim, 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA), 1526-1540 (2025). <https://doi.org/10.1109/hpca61900.2025.00114> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: G. Jonatan 외, J. Kim, Proceedings of the ACM on Measurement and Analysis of Computing Systems 8, 1-28 (온라인 2024-02-21). <https://doi.org/10.1145/3639046> 초록 기준.
[^p4]: J. Kim, M. Jung, J. Kim, Proceedings of the 50th Annual International Symposium on Computer Architecture, 1-13 (온라인 2023-06-17). <https://doi.org/10.1145/3579371.3589096> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Park, J. Kim, 2026 IEEE International Symposium on High Performance Computer Architecture (HPCA), 1-14 (2026). <https://doi.org/10.1109/hpca68181.2026.11408558> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Z. Jin 외, J. Kim, 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO), 885-898 (2024). <https://doi.org/10.1109/micro61859.2024.00070> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: Z. Jin 외, J. Kim, 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO), 1138-1152 (2024). <https://doi.org/10.1109/micro61859.2024.00086> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: C. Siy 외, J. Kim, Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, 1-15 (온라인 2026-04-13). <https://doi.org/10.1145/3772318.3791959> 초록 기준(Semantic Scholar 등록 초록).

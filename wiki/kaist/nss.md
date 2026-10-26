# 네트워크 및 시스템 보안 연구실 (Network and System Security Laboratory, NSS Lab)

**KAIST 전기및전자공학부·정보보호대학원 · 신승원 교수**

- 분야: 네트워크·시스템 보안(소프트웨어 정의 네트워킹 보안, 네트워크 위협 분석과 방어, 하드웨어 부채널, 블록체인 공격과 남용 탐지), 인공지능 시스템의 보안과 인공지능을 쓴 보안(대형 언어 모델의 안전, 백도어 공격과 방어, 다크웹 언어 모델), 빠르고 안전한 클라우드·네트워크 시스템(스마트NIC 가속, 기밀 서버리스, 컨테이너 네트워크 보안)
- 대분야: 컴퓨팅·AI
- 태그: 네트워크 보안·프라이버시[^gsislab][^research][^p5], 컴퓨터 네트워크[^research][^p6], 대형 언어 모델[^faculty][^research][^p1], 퍼징[^research][^p4], 하드웨어 보안[^home][^p7][^p8], 블록체인[^home][^research], AI·기계학습 보안·프라이버시[^research]
- 홈페이지: <https://nss.kaist.ac.kr/>
- 근거와 출처: [NSS Lab 근거 페이지](nss-sources.md)

> 새로 나타나는 위협을 밝혀 이해하고 컴퓨팅을 안전하게 만드는 새 시스템과 알고리즘을 설계하는 연구실로, 인공지능(AI)·보안(Security)·시스템(System) 세 갈래를 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 신승원 교수가 이끄는 연구실이다.[^home][^faculty] 누리집은 연구실 이름을 Network and System Security (NSS) Laboratory로 적고,[^home] 전기및전자공학부 교수 소개는 교수의 소속 연구실을 「네트워크 및 시스템 보안 연구실」로,[^ee] 정보보호대학원 연구실 목록은 Network and System security (NSS) Lab으로 적는다.[^gsislab] 정보보호대학원 교수진 목록은 교수의 소속을 전기및전자공학부와 정보보호대학원으로 적는다.[^gsisfac]

누리집 첫 화면은 연구실이 새로 나타나는 위협을 밝혀 이해하고, 컴퓨팅을 안전하게 만드는 새 시스템과 알고리즘을 설계한다고 소개하고, 연구 분야를 AI, Security, System 셋으로 나눈다.[^home] 정보보호대학원 연구실 목록은 연구실을 네트워크 보안 분야에 두고 분야를 Software Defined Networking security와 Botnet analysis and detection으로 적으며, 연구실이 네트워크와 시스템 보안을 중점적으로 연구하고 특히 차세대 네트워크 기술인 SDN(Software Defined Network, 네트워크 장비의 데이터 전달 기능과 제어 기능을 나누어 제어를 소프트웨어 제어기가 맡게 하고 망을 프로그램으로 관리하는 방식) 보안, SDN을 활용한 임베디드 시스템과 IoT, 그리고 웹·모바일 같은 여러 주제를 함께 연구한다고 소개한다.[^gsislab] 전기및전자공학부 교수 소개는 교수의 주요 연구를 Network and system security, Software-defined networking, Network function virtualisation(NFV, 네트워크 기능 가상화, 방화벽 같은 네트워크 기능을 전용 장비 대신 범용 서버의 소프트웨어로 실행하는 방식), IoT로 적는다.[^ee]

첫째 갈래는 **AI 시스템의 보안과 AI를 쓴 보안**이다. Research 페이지는 AI가 이제 보안 연구의 대상이자 도구라고 적고, 연구실이 AI 시스템이 적대적 압력 아래에서 어떻게 실패하는지와 AI 시스템을 더 믿을 수 있고 견고하게 만드는 방법을 연구한다고 소개한다. 그 예로 텍스트로 이미지를 만드는 모델에 대한 탈옥 공격(jailbreak, 모델에 걸린 안전 제한을 우회해 막아 둔 출력을 내게 하는 공격) 연구(PC²), 전문가 혼합(MoE, Mixture-of-Experts, 여러 하위 신경망(전문가)과 입력마다 어느 전문가를 쓸지 정하는 장치로 이뤄진 모델 구조) 대형 언어 모델의 안전 취약점과 방어(MoEvil, SafeMoE), 언러닝(학습에 쓴 자료의 일부가 모델에 남긴 영향을 지우는 일)을 이용한 적대적 공격, 백도어(모델에 몰래 심어, 특정 신호가 든 입력에서만 공격자가 정한 동작을 하게 만드는 숨은 장치) 공격과 방어(Obliviate, CGBA)를 든다. 함께 기계학습과 자연어 처리 기술을 보안 문제에 쓰는 연구로, 다크웹 자료로 사전 학습한 언어 모델(DarkBERT), 자격 증명 재사용의 대규모 예측(PassREfinder), 온라인 커뮤니티의 불법 약물 탐지(JEDIS)를 든다.[^research] 누리집 Faculty 페이지는 교수가 대형 언어 모델과 생성 AI의 보안, 특히 텍스트-이미지 모델에 대한 탈옥 공격과 MoE 구조의 안전한 미세조정을 연구한다고 적는다.[^faculty] 대표 논문에서는 대형 언어 모델의 기존 매개변수 대부분을 고정한 채 적은 수의 매개변수만 학습시켜 새 과제에 맞추는 매개변수 효율 미세조정(PEFT)에 숨어드는 과제 무관 백도어를 무력화하는 방어 Obliviate를 내놓았다.[^p1] 사용자가 비밀번호를 재사용할 가능성이 높은 웹사이트 사이의 관계를 그래프 신경망(점과 선으로 이뤄진 그래프 자료를 다루는 신경망)으로 웹사이트 그래프의 연결로 나타내, 다른 곳에서 유출된 계정 정보로 여러 사이트에 로그인을 시도하는 크리덴셜 스터핑(credential stuffing) 공격의 위험을 미리 예측하는 PassREfinder와,[^p2] 다크웹(일반 검색 엔진에 잡히지 않고 특정 소프트웨어나 설정으로만 접속할 수 있는 웹 영역) 자료로 사전 학습한 언어 모델 DarkBERT도 만들었다.[^p3] 최근 논문 목록에는 웹 기능을 갖춘 대형 언어 모델이 만드는 새 위협을 제목에 단 USENIX Security 2025 논문(When LLMs Go Online)과, 대형 언어 모델(LLM) 에이전트의 스킬에 대한 언어·코드 교차 공격의 벤치마크와 방어를 제목에 단 ACSAC 2026 채택 논문(SkillMutator)도 있다.[^pubs][^home]

둘째 갈래는 **네트워크·하드웨어·블록체인의 위협 분석과 방어**다. Research 페이지는 위협을 드러내고 네트워크로 연결된 시스템을 지키는 일을 연구실이 처음부터 내세운 사명으로 적고, 시스템에 대한 깊은 이해에 공격 연구와 방어 연구를 함께 묶는다고 소개한다. 그 예로 보안 출처 추적(security provenance, 시스템에서 일어난 사건들의 인과 관계를 기록한 정보)으로 침입의 근본 원인을 추적하는 연구(SECTRACER), SDN과 SD-WAN(소프트웨어로 제어하는 광역 통신망)의 제어 평면(망에서 데이터를 어디로 보낼지 정하는 기능을 맡는 부분)에 대한 퍼징과 지문 분석(fingerprinting, 겉으로 관찰되는 신호로 대상의 종류나 구성을 알아내는 일)(Ambusher, Heimdallr), 마이크로아키텍처(프로세서 내부의 하드웨어 구현 구조) 부채널과 타이밍 부채널(계산 결과가 아니라 실행 시간·전력 소비 같은 부수 신호로 정보가 새는 경로)의 발견(AVXProbe, AVX-TSCHA), 익명 통신망의 익명성 해제와 네트워크 구조 추론에 맞서는 방어(MUFFLER, EqualNet), 누구나 참여할 수 있는 블록체인에 대한 공격과 그 남용의 탐지(Partitioning Ethereum, CENSor)를 든다.[^research] 누리집 첫 화면은 이 갈래를 깊은 시스템 분석, 부채널 연구, 위협 포렌식으로 네트워크·하드웨어·블록체인 전반의 위협을 드러내고 막는 연구로 요약한다.[^home] 대표 논문에서는 광역망에서 쓰는 분산 SDN 제어기의 프로토콜 취약점을 프로토콜 상태 퍼징으로 찾는 시험 도구 Ambusher를 만들었다.[^p4] 또 공격자가 경로 추적 도구로 알아낸 망 구조 정보를 링크 범람 공격(LFA, 망의 특정 연결 구간에 트래픽을 몰아 통신을 마비시키는 서비스 거부 공격)에 쓰지 못하도록, 추적 흐름이 노드와 링크에 고르게 퍼지게 해 중요한 지점을 가려내지 못하게 하는 장기 망 구조 위장 방어 EqualNet을 내놓았다.[^p5] Faculty 페이지는 교수의 연구가 다크웹 위협 인텔리전스, 사이버 범죄 추적, 프로그래밍 가능한 네트워크의 보안 자동화도 아우른다고 적는다.[^faculty]

셋째 갈래는 **빠르고 안전한 클라우드·네트워크 시스템**이다. Research 페이지는 이제 시스템이 빠르면서 동시에 안전하기를 요구받는다고 적고, 연구실이 하드웨어·소프트웨어 공동 설계로 보안을 효율적으로 만들어 둘을 함께 이루는 방법을 연구한다고 소개한다. 그 예로 스마트NIC(SmartNIC, 자체 연산 장치를 갖추어 패킷 처리 같은 작업을 호스트 CPU 대신 직접 할 수 있는 네트워크 카드)에서 서비스 메시(마이크로서비스 사이의 통신을 맡아 관리하는 기반 소프트웨어 계층)의 인그레스(외부 트래픽이 들어오는 관문)를 가속하는 연구(HybridMesh, HardMesh), 컨테이너에 RDMA(Remote Direct Memory Access, 상대 컴퓨터의 CPU를 거치지 않고 그 메모리를 직접 읽고 쓰는 통신 방식)를 고려한 네트워킹과 하드웨어로 격리된 네트워킹을 주는 연구(RDNet, Hyperion, HardWhale), 재구성 가능한 하드웨어로 SDN과 NFV에 회선 속도의 패킷 검사를 넣는 연구(Reinhardt), 빠른 스냅숏과 가속으로 기밀 서버리스의 부담을 줄이는 연구(AccelFaaS, TDSnap, Cryonics)를 든다.[^research] Faculty 페이지는 교수가 클라우드 컴퓨팅 최적화에서 FaaS(Function-as-a-Service, 이용자가 올린 함수 단위의 코드를 클라우드가 호출이 있을 때 실행해 주는 서비스) 성능을 가속하고 Trusted Domain Snapshots로 안전한 실행을 보장하는 방법을 설계하며, 네트워크 기반 시설에서는 서비스 메시 인그레스 성능을 높이는 하드웨어·소프트웨어 혼합 시스템을 개발한다고 적는다.[^faculty] 대표 논문에서는 서비스 메시에서 외부 트래픽의 주 진입점인 인그레스 게이트웨이가 성능 병목이 된다는 점을 밝히고, 트래픽 분석과 전달을 스마트NIC에 맡기고 가벼운 CPU 쪽 프록시를 더한 HybridMesh를 만들었다.[^p6] 서버리스 컴퓨팅에 SGX 같은 신뢰 실행 환경(TEE, 하드웨어의 도움으로 다른 소프트웨어와 격리된 실행 구역을 만들어 그 안의 코드와 데이터를 지키는 환경)을 쓸 때 엔클레이브 생성 때문에 함수 시작이 늦어지는 문제를 스냅숏 기반 엔클레이브로 줄인 Cryonics와,[^p7] 컨테이너 트래픽 검사 전체를 스마트NIC로 옮겨 호스트 운영체제와 물리적으로 떼어 낸 네트워크 보안 집행 시스템 HardWhale도 내놓았다.[^p8]

## 주요 연구 주제

### 1. AI 시스템의 보안과 AI를 쓴 보안

매개변수 효율 미세조정에 숨은 과제 무관 백도어의 무력화(Obliviate), 웹사이트 그래프로 크리덴셜 스터핑 위험 예측(PassREfinder), 다크웹 자료로 사전 학습한 언어 모델(DarkBERT).[^p1][^p2][^p3] Research 페이지는 전문가 혼합 대형 언어 모델의 안전 취약점과 방어, 텍스트-이미지 모델에 대한 탈옥 공격도 든다.[^research]

### 2. 네트워크·하드웨어·블록체인의 위협 분석과 방어

분산 SDN 제어기의 프로토콜 상태 퍼징(Ambusher), 링크 범람 공격을 어렵게 하는 망 구조 위장(EqualNet).[^p4][^p5] Research 페이지는 침입의 근본 원인 추적, 부채널 발견, 블록체인에 대한 공격과 남용 탐지도 든다.[^research]

### 3. 빠르고 안전한 클라우드·네트워크 시스템

스마트NIC를 쓴 서비스 메시 인그레스 가속(HybridMesh), 스냅숏 기반 엔클레이브로 빨리 시작하는 신뢰 서버리스(Cryonics), 스마트NIC로 호스트와 격리한 컨테이너 네트워크 보안 집행(HardWhale).[^p6][^p7][^p8]

## 대표 논문

누리집 논문 목록의 2021–2026년 논문 가운데 신승원 교수가 저자인 학술지·학회 논문을 앞의 세 연구 갈래에 고르게 담도록 골랐고, 교수가 마지막 저자인 논문을 우선했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Obliviate: Neutralizing Task-agnostic Backdoors within the Parameter-efficient Fine-tuning Paradigm](https://doi.org/10.18653/v1/2025.findings-naacl.71) · Findings of the Association for Computational Linguistics: NAACL 2025 | 매개변수 효율 미세조정(PEFT)은 대형 언어 모델의 핵심 학습 전략이 됐지만, 학습하는 매개변수가 적다는 점 때문에 과제 무관 백도어(어떤 과제에 쓰이든 작동하는 백도어) 같은 보안 위험이 생긴다. 과제 무관 백도어는 여러 과제에 큰 피해를 주는데도, PEFT 환경에서 이를 효과적으로 막는 실용적인 방어는 없었다. 이 논문은 PEFT에 통합할 수 있는 백도어 방어 Obliviate를 제안했다. PEFT 층 안의 정상(benign) 뉴런을 키우는 기법과 트리거 토큰(백도어를 작동시키는 입력 낱말)의 영향에 벌점을 주는 기법 두 가지를 개발했다. 주요 PEFT 구조 세 가지에서 평가한 결과 최신 과제 무관 백도어의 공격 성공률을 크게 낮췄고(초록 표기 83.6%↓), 특정 과제를 노린 백도어와 방어에 맞춰 바꾼 적응형 공격에도 견고한 방어 능력을 보였다.[^p1] | 1저자 Jaehan Kim, 마지막 저자 신승원 |
| 2 | 2024 | [PassREfinder: Credential Stuffing Risk Prediction by Representing Password Reuse between Websites on a Graph](https://doi.org/10.1109/sp54263.2024.00020) · 2024 IEEE Symposium on Security and Privacy (SP) | 크리덴셜 스터핑이 퍼지면서 여러 웹사이트에 같은 비밀번호를 쓰는 온라인 사용자들이 큰 피해를 입었다. 연구자들은 같은 비밀번호를 쓰는 사용자나 악성 로그인을 탐지하려 했지만, 기존 탐지 방법은 비밀번호 생성이나 웹사이트 접속을 막아 비밀번호의 사용성을 해치고, 계정 정보를 공유하는 복잡한 방식 때문에 실제로 도입하기도 어렵다. 이 논문은 탐지에 기대지 않고, 사용자 행동을 방해하기 전에 크리덴셜 스터핑 공격을 막는 위험 예측 틀을 제안했다. 사용자가 비밀번호를 재사용할 가능성이 높은 웹사이트 사이의 관계를 새로 정의하고, 그래프 신경망으로 이를 웹사이트 그래프의 간선(두 점을 잇는 선)으로 나타낸 뒤, 연결 예측(link prediction, 그래프에서 두 점 사이에 연결이 있을지 예측하는 일)으로 웹사이트 사이의 위험을 찾는다. 공개된 웹사이트 정보를 쓰고 새로 관측한 웹사이트 노드를 그래프에 이어 붙이므로 임의의 많은 웹사이트에 적용할 수 있다. 웹사이트 2만 2,378곳에서 유출된 계정 3억 6천만 개로 이뤄진 실제 자료로 평가한 결과, 두 가지 그래프 학습 설정에서 F1 점수(정밀도와 재현율을 함께 반영한 분류 성능 지표) 0.9559와 0.9100으로 위험을 예측했다. 각 설계 전략의 효과도 보였고, 예측 결과를 비밀번호 재사용의 예상 비율을 나타내는 위험 점수로 쓸 수 있음을 확인했다.[^p2] | 1저자 Jaehan Kim, 마지막 저자 신승원 |
| 3 | 2023 | [DarkBERT: A Language Model for the Dark Side of the Internet](https://doi.org/10.18653/v1/2023.acl-long.415) · Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) | 다크웹에서 쓰이는 언어는 일반 웹(Surface Web)의 언어와 분명히 다르다는 연구가 있다. 다크웹 연구에는 이 영역의 글 분석이 흔히 필요하므로, 다크웹에 특화한 언어 모델이 연구자에게 쓸모 있는 통찰을 줄 수 있다. 이 논문은 다크웹 자료로 사전 학습한 언어 모델 DarkBERT를 소개했다. 다크웹의 극심한 어휘·구조 다양성은 이 영역을 제대로 표현하는 데 방해가 될 수 있어, 이에 대응하려고 학습용 글 자료를 걸러 모은 단계를 설명했다. DarkBERT와 그 기본판(vanilla counterpart), 널리 쓰이는 다른 언어 모델을 여러 사용 사례에서 평가해 다크웹 특화 모델의 이점을 확인했다. 평가에서 DarkBERT는 현재의 언어 모델들보다 좋은 성능을 보였고, 앞으로의 다크웹 연구에 가치 있는 자원이 될 수 있다.[^p3] | 1저자 Youngjin Jin, 마지막 저자 신승원 |
| 4 | 2024 | [Ambusher: Exploring the Security of Distributed SDN Controllers through Protocol State Fuzzing](https://doi.org/10.1109/tifs.2024.3402967) · IEEE Transactions on Information Forensics and Security | 분산 SDN 제어기는 광역망(WAN), 특히 SD-WAN에서 넓은 네트워크 기반 시설의 확장성과 장애 허용(일부가 고장 나도 계속 동작하는 성질)을 주는 핵심 요소가 됐다. 그러나 이 제어기들의 구조는 지금까지 충분히 주목받지 못한 새로운 공격 표면(공격자가 노릴 수 있는 지점들)을 만든다. 이 논문은 분산 SDN 제어기에서 쓰는 프로토콜의 취약점을 찾는 시험 도구 Ambusher를 내놓았다. Ambusher는 추론한 상태 기계(입력에 따라 정해진 상태들 사이를 옮겨 가는 동작 모형)를 바탕으로 공격 시나리오를 체계적으로 찾는 프로토콜 상태 퍼징을 쓴다. 여러 제어기로 이뤄진 클러스터에서 상태를 배우기는 복잡하므로, 하나의 비교적 단순한 상태 기계를 뽑아내는 새 방법론으로 효율적인 상태 기반 퍼징을 한다. 두 캠퍼스 네트워크와 한 기업 네트워크에 걸친 실제 SD-WAN 배치에서 평가해, 널리 쓰이는 분산 제어기 플랫폼에서 잠재적 취약점 6개를 찾아냈다.[^p4] | 1저자 Jinwoo Kim, 마지막 저자 신승원 |
| 5 | 2022 | [EqualNet: A Secure and Practical Defense for Long-term Network Topology Obfuscation](https://doi.org/10.14722/ndss.2022.23154) · Proceedings 2022 Network and Distributed System Security Symposium | traceroute 같은 경로 추적 도구는 네트워크 운영자가 장애를 찾아 고치는 단순하지만 기본적인 디버깅 도구다. 그러나 공격자도 이 도구로 알려지지 않은 네트워크 구조(토폴로지) 정보를 얻을 수 있고, 이 정보는 링크 범람 공격(LFA) 같은 정교한 서비스 거부 공격을 더 효율적으로 하는 열쇠다. 지난 몇 년 동안 가상(가짜) 구조를 보여 주어 잠재적 병목 링크를 공격자에게서 감추는 네트워크 위장 방어가 여럿 나왔지만, 그 가상 구조가 주는 보안성과 유용성을 포괄적·체계적으로 분석한 연구는 없었다. 이 논문은 최신 네트워크 위장 방어 세 가지를 보안 분석해, 가상 구조의 보안성과 유용성을 크게 떨어뜨릴 수 있는 공통 한계 네 가지를 밝혔다. 이를 바탕으로 한 네트워크 영역 안에서 LFA를 줄이는 안전하고 실용적인 장기 네트워크 구조 위장 방어 EqualNet을 내놓았다. EqualNet은 추적 흐름이 노드와 링크에 고르게 퍼지게 해 공격자가 어느 것이 가장 중요한지 가려내지 못하게 하고, 그래서 LFA를 하는 비용을 크게 높인다. 동시에 서브넷 정보는 남겨, 경로 추적 도구로 네트워크를 디버깅하는 운영자를 돕는다. SDN으로 전체 시제품을 구현해 소프트웨어와 하드웨어에서 폭넓게 평가했고, 네트워크 안의 라우터 가운데 적은 수만 SDN을 지원해도 작은·중간·큰 네트워크의 추적 흐름 분포를 고르게 만드는 데 효과적이었다. 끝으로 여러 공격에 대한 EqualNet의 보안을 분석했다.[^p5] | 1저자 Jinwoo Kim, 마지막 저자 신승원 |
| 6 | 2026 | [HybridMesh: A Hardware-software Hybrid Approach for Accelerating Service Mesh Ingress](https://www.usenix.org/conference/nsdi26/presentation/you) · 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26) | 서비스 메시는 클라우드 환경에서 마이크로서비스 사이의 통신을 가능하게 하는 데 꼭 필요해졌지만, 네트워크 부담이 크다. 이 논문은 외부 트래픽의 주 진입점인 인그레스 게이트웨이가 주요 성능 병목이 됐음을 밝혔다. 이 부담은 현재 인그레스 게이트웨이의 두 한계, 곧 CPU를 많이 쓰는 트래픽 분석과 복잡한 패킷 전달 경로에서 온다. 분석 결과 이런 비효율은 네트워크 처리량을 최대 4배 떨어뜨리면서 CPU 사용률을 크게 높일 수 있었다. 이에 스마트NIC로 트래픽을 빠르게 분석하고 효율적으로 전달하는 하드웨어·소프트웨어 혼합 인그레스 게이트웨이 HybridMesh를 제안했다. 스마트NIC에서 실행하기 알맞지 않은 여러 트래픽 관리 기능은 가벼운 CPU 쪽 프록시(중간에서 트래픽을 받아 대신 처리하고 넘겨주는 프로그램)가 맡는다. 평가에서 HybridMesh는 기존 인그레스 게이트웨이보다 HTTP 처리량을 4.4배 높였고, 소프트웨어만 쓰는 설계와 하드웨어만 쓰는 설계에 견줘 비용 효율은 2.3배, 전력 효율은 2.8배 높았다.[^p6] | 1저자 Myoungsung You, 마지막 저자 신승원 |
| 7 | 2023 | [Cryonics: Trustworthy Function-as-a-Service using Snapshot-based Enclaves](https://doi.org/10.1145/3620678.3624789) · Proceedings of the 2023 ACM Symposium on Cloud Computing | 최근 연구들은 서버리스 컴퓨팅에 SGX 같은 신뢰 실행 환경(TEE)을 써서, 안전하지 않은 시스템 소프트웨어, 같은 서버에 함께 올라간 악의적 이용자, 의심스러운 클라우드 운영자의 위협을 막자고 제안했다. 그러나 가장 성숙한 TEE 가운데 하나인 SGX를 서버리스 컴퓨팅에 넣으면, 엔클레이브(SGX가 만드는 격리된 실행 구역) 생성 때문에 함수 시작이 늦어져 성능이 크게 떨어진다. SGX는 함수를 부를 때마다 많은 응용 코드·라이브러리·데이터를 다시 초기화하는 서버리스 함수의 시작 절차를 고려해 설계되지 않았기 때문이다. 모든 페이지를 엔클레이브에 더하거나 페이지 권한을 제한하는 SGX 고유의 한계는 TLB(최근의 메모리 주소 변환 결과를 담아 두는 프로세서 안의 저장소) 비우기, 문맥 전환, 엔클레이브 재진입을 일으켜 성능을 떨어뜨린다. 이 논문은 서버리스 함수의 본래 특성에서 핵심 관찰을 얻어, 함수 인스턴스가 앞으로 쓸 작업 집합(working set)을 미리 만들어 함수 인스턴스의 시작을 빠르게 하는 스냅숏 기반 엔클레이브 제공 방법 Cryonics를 제안했다. 엔클레이브 안 함수 인스턴스의 페이지 지역성과 더 쓰이지 않는 페이지를 고려해, 요청 처리에 쓸 가벼운 작업 집합을 만든다. 평가에서 Cryonics는 기존 콜드 스타트(함수 인스턴스를 처음부터 새로 띄우는 방식) 기반 방법에 견줘 시작 시간에서 최대 100배 나은 성능을 보였고, 시작 시간이 안정적임을 보였다.[^p7] | 1저자 Seong-Joong Kim, 마지막 저자 신승원 |
| 8 | 2024 | [HardWhale: A Hardware-isolated Network Security Enforcement System for Cloud Environments](https://doi.org/10.1109/icdcs60910.2024.00053) · 2024 IEEE 44th International Conference on Distributed Computing Systems (ICDCS) | 마이크로서비스 배포에 컨테이너가 널리 쓰이면서 컨테이너 네트워크의 보안이 중요한 문제가 됐다. 그러나 현재 보안 방법은 호스트 운영체제에 기대어 컨테이너 트래픽에 네트워크 정책을 집행한다. 이 설계는 부담이 크고, 공격자가 호스트 운영체제에 접근하면 컨테이너 네트워크 보안을 보장하지 못한다. 이 논문은 호스트 운영체제에 기대지 않고 높은 성능과 견고한 네트워크 보안을 주는, 하드웨어로 격리된 컨테이너용 네트워크 보안 집행 시스템 HardWhale을 제안했다. HardWhale은 스마트NIC를 써서 컨테이너 트래픽 검사 전체를 호스트에서 물리적으로 떼어 내고 검사 작업을 가속한다. 검사 정책은 스마트NIC 안에 안전하게 머물고, 격리된 정책 관리 방식 덕분에 호스트를 거치지 않고 실행 중에 갱신된다. 그래서 호스트가 공격자에게 노출돼도 컨테이너의 네트워크 보안이 지켜진다. 평가에서 HardWhale은 침해된 환경에서 여러 네트워크 공격으로부터 컨테이너를 보호했고, 최신 방법에 견줘 HTTP 처리량을 3배, HTTP 지연을 2.3배 개선했다.[^p8] | 1저자 Myoungsung You, 마지막 저자 신승원 |

## 교수와 전문 분야

신승원 교수는 Texas A&M University에서 컴퓨터공학(Computer Engineering) 박사 학위를, KAIST에서 전기및컴퓨터공학(Electrical & Computer Engineering) 석사·학사 학위를 받았다.[^faculty] 전기및전자공학부 교수 소개는 학위를 "Ph.D (2013) Texas A&M Univ."로 적는다.[^ee] 누리집 Faculty 페이지에 따르면 교수는 2013년 KAIST에 오기 전 9년 동안 산업계에서 네트워킹 시스템을 개발했고, MIT의 방문 과학자(visiting scientist)와 SRI International의 인턴을 지냈으며, Open Networking Foundation(ONF) 보안 작업반(security working group)의 research associate로 활동했다.[^faculty] 같은 페이지는 교수를 KAIST 전기및전자공학부 교수(Professor)이자 NSS Laboratory의 연구책임자(Principal Investigator)로 적고,[^faculty] 전기및전자공학부 교수진 목록과 교수 소개도 직위를 교수로 적는다.[^eelist][^ee] 전기및전자공학부 교수 소개의 주요 연구분야 칸은 AI & Machine Learning, Security, Software Systems & Networking이고 디비전은 Computer division이다.[^ee] 정보보호대학원 교수진 목록은 교수의 연구 분야를 「네트워크보안, 소프트웨어 정의 네트워킹」으로 적는다.[^gsisfac]

전기및전자공학부 교수 소개는 교수의 대표 업적으로 「Attacking SDN Infrastructure: Are We Ready for the Next-Gen Networking?」, 「A First Step Towards Network Security Virtualization: From Concept To Prototype」, 「Rosemary: A Robust, Secure, and High-performance Network Operating System」, 「AVANT-GUARD: Scalable and Vigilant Switch Flow Management in Software-Defined Networks」, 「FRESCO: Modular Composable Security Services for Software-Defined Networks」 다섯 건을 든다.[^ee] 누리집 논문 목록을 시기별로 보면, 2015–2019년 항목은 SDN의 보안 평가 틀(DELTA), 네트워크 운영체제와 SDN 응용의 권한·정책 관리, SDN으로 만드는 보안 기능, 다크웹의 암호화폐 남용과 피싱 서비스 조사를 다룬다. 2020–2022년 항목은 SDN 정책 불일치 탐지, 컨테이너 네트워크 보안(BASTION, XDP/eBPF를 쓴 컨테이너 간 통신 보호), 정규 표현식 패킷 검사 하드웨어(Reinhardt), 망 구조 감추기(BottleNet, EqualNet), 블록체인 측정, 다크웹 언어 분석을 다룬다. 2023–2026년 항목에는 대형 언어 모델을 포함한 기계학습 모델의 보안, 스마트NIC를 쓰는 클라우드 네트워크 시스템, 서버리스 함수의 신뢰 실행을 다룬 논문이 이어진다.[^pubs] 누리집 Award 페이지는 ACSAC 2025의 Distinguished Paper Award를 적고, 논문 목록은 같은 저자 5명(교수는 4번째 저자)의 MoEvil 논문 제목 뒤에 이 상을 표시한다.[^awards][^pubs]

논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, 대형 언어 모델의 백도어 방어와 함께 그래프 신경망·언어 모델 같은 기계학습으로 크리덴셜 스터핑 위험을 예측하고 다크웹 글을 분석하는 AI와 보안의 결합이다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 분산 SDN 제어기의 취약점을 퍼징으로 찾고 망 구조를 위장해 링크 범람 공격을 어렵게 하는 네트워크 보안이다(대표 논문 4, 5).[^p4][^p5] 셋째, 스마트NIC와 신뢰 실행 환경을 써서 클라우드의 서비스 메시·서버리스·컨테이너 네트워크를 빠르고 안전하게 만드는 시스템 설계다(대표 논문 6–8).[^p6][^p7][^p8]

## 응용 분야

대표 논문은 대형 언어 모델의 미세조정,[^p1] 여러 웹사이트에 같은 비밀번호를 쓰는 사용자 계정의 보호,[^p2] 다크웹 연구,[^p3] 캠퍼스·기업 네트워크에 배치한 SD-WAN,[^p4] 링크 범람 공격에 맞서야 하는 네트워크 운영,[^p5] 클라우드 마이크로서비스의 통신,[^p6] 서버리스 컴퓨팅,[^p7] 컨테이너로 배포한 마이크로서비스[^p8]를 대상으로 한다. 정보보호대학원 연구실 목록은 SDN을 활용한 임베디드 시스템과 IoT, 웹, 모바일을 연구실이 함께 연구하는 주제로 든다.[^gsislab] 누리집 Research 페이지는 온라인 커뮤니티의 불법 약물 탐지(JEDIS)도 AI를 보안에 쓰는 연구의 예로 든다.[^research] 졸업생의 진로로는 University of Seoul, Kwangwoon University, Chonnam National University, Incheon National University, Dankook University의 Assistant Professor와 Samsung Research, NCsoft, S2W, ETRI, SKT, NSR, KHNP CRI, Theori, FURIOSA AI, Hyperconnect, Atto Research, Indiana University Bloomington, KAIST가 있다.[^alumni]

## 구성원

2026년 10월 25일 누리집 People 하위 페이지 기준이다. Postdoctoral Researchers 2명, Doctoral Students 9명, Master's Students 2명이며, 과정은 각 페이지의 제목을 옮겼다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Kwanwoo Kim | 박사후연구원 |  |
| Youngjin Jin | 박사후연구원 | 2, 3 |
| Minkyoo Song | 박사과정 | 1, 2 |
| Hanna Kim | 박사과정 |  |
| Youngduk Kim | 박사과정 |  |
| Taeha Kim | 박사과정 |  |
| Bom Kim | 박사과정 |  |
| Isu Kim | 박사과정 |  |
| Kay Kyoung-ju Kwak | 박사과정 |  |
| Inwook Hwang | 박사과정 |  |
| Myungchul Kang | 박사과정 |  |
| Jihye Lee | 석사과정 |  |
| Heeju Yeo | 석사과정 |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 Ph.D. 18명과 Master's 16명이다. 학위·과정은 페이지의 구역 이름(Ph.D., Master's)을 옮겼고, 페이지에는 졸업 연도가 없다. 진로는 이름 옆에 적힌 곳이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Haney Kang | Ph.D. |  |
| Seong-Joong Kim | Ph.D. |  |
| Jaehan Kim | Ph.D. |  |
| Hyunmin Seo | Ph.D. |  |
| Myoungsung You | Ph.D. | Assistant Professor at University of Seoul |
| Suryeon Kim | Ph.D. |  |
| Seung Ho Na | Ph.D. | Samsung Research |
| Hyeonseong Jo | Ph.D. | NCsoft |
| Yeonkeun Kim | Ph.D. | S2W |
| Hwanjo Heo | Ph.D. | ETRI |
| Jinwoo Kim | Ph.D. | Assistant Professor at Kwangwoon University |
| Jinho Choi | Ph.D. |  |
| Taejune Park | Ph.D. | Assistant Professor at Chonnam National University |
| Sengsoo Lee | Ph.D. | Assistant Professor at Incheon National University |
| Heedo Kang | Ph.D. | SKT |
| Jaehyun Nam | Ph.D. | Assistant Professor at Dankook University |
| Seunghyeon Lee | Ph.D. | S2W |
| Chang hoon Yoon | Ph.D. | S2W |
| Younghyo Kang | Master's |  |
| Ki-Jung Ryu | Master's | KHNP CRI |
| Sumin Cho | Master's | Theori |
| Dongmin Choi | Master's | NSR |
| Nahyeon Park | Master's | KAIST |
| Taehwa Lee | Master's |  |
| Minjae Seo | Master's | ETRI |
| Jian Cui | Master's | Indiana University Bloomington |
| Suyeol Lee | Master's | FURIOSA AI |
| Seonghwan Joe | Master's | Hyperconnect |
| Sengyoung Jeong | Master's | NSR |
| Junsik Seo | Master's | Atto Research |
| Seungwon Woo | Master's | ETRI |
| Sora Kim | Master's |  |
| Chanhee Lee | Master's | S2W |
| Chanwoo Bae | Master's | NSR |

## 최근 논문 목록 (2021–2026)

누리집 Publication / Talk 페이지의 2021–2026년 연도 구역에 실린 60편이다(2026년 9편, 2025년 15편, 2024년 11편, 2023년 9편, 2022년 12편, 2021년 4편). 연도는 누리집의 연도 구역이고, 제목·저자·학술지와 학회 이름은 누리집 표기 그대로다. 학술지·학회 이름 뒤 괄호의 약칭은 누리집이 제목 앞에 붙인 약칭이다. 저자 이름 뒤의 \*는 누리집이 공동 1저자(Co-first author)로 밝힌 표시다. 학회 이름 뒤의 (To appear)는 누리집 표시이고, 누리집 첫 화면 News 칸은 (To appear)가 붙은 세 편(SkillMutator, SWIFT, TDSnap)을 각각 ACSAC 2026과 DAC 2026에 채택(Accepted)된 논문으로 알린다.[^pubs][^home]

**2026**

- Youngduk Kim, Minkyoo Song, Seungwon Shin. "SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills". *IEEE Annual Computer Security Applications Conference (ACSAC), 2026 (To appear)*.
- Inwook Hwang, Ngseo Kim, Seungwon Shin, Myoungsung You. "SWIFT: Robust Code Watermarking via Structural Canonicalization and LLM-Based Rewriting". *IEEE Annual Computer Security Applications Conference (ACSAC), 2026 (To appear)*.
- Wonwoo Choi\*, Minjae Seo\*, Minkyoo Song, Hwanjo Heo, Seungwon Shin, Myoungsung You (\* Co-first author). "𝑃𝐶²: Politically Controversial Content Generation via Jailbreaking Attacks on GPT-based Text-to-Image Models". *ACM Conference on Computer and Communications Security (CCS), 2026*.
- Bom Kim, Seungwon Shin, Seungsoo Lee. "A unified framework for cognition-driven security policy generation in cloud-native environments". *Journal of Network and Computer Applications (JNCA), 2026*.
- Seong-Joong Kim, Seungwon Shin and Myoungsung You. "AccelFaaS: Accelerating FaaS via Pre-warmed Memory and Control Channel Offloading". *IEEE Transactions on Cloud Computing (TCC), 2026*.
- Seong-Joong Kim, Seungwon Shin and Myoungsung You. "TDSnap: Enabling Secure Function-as-a-Service with Trusted Domain Snapshot". *Design Automation Conference (DAC), 2026 (To appear)*.
- Jaehan Kim, Minkyoo Song, Seungwon Shin, Sooel Son. "SafeMoE: Safe Fine-Tuning for MoE LLMs by Aligning Harmful Input Routing". *International Conference on Learning Representations (ICLR), 2026*.
- Myoungsung You, Jaehyun Nam, Minjae Seo, Taejune Park, Seungwon Shin. "HybridMesh: A Hardware-software Hybrid Approach for Accelerating Service Mesh Ingress". *USENIX Networked Systems Design and Implementation (NSDI), 2026*.
- Myoungsung You, Minjae Seo, Seungwon Shin, Jaehyun Nam. "RDNet: An RDMA-aware Container Network Interface for Cloud Environments". *IEEE International Conference on Computer Communications, 2026 (INFOCOM)*.

**2025**

- Haney Kang\*, Eduard Marin\*, Myoungsung You, Diego Perino, Seungwon Shin, Jinwoo Kim (\* Co-first author). "BEACON: Automatic Container Policy Generation using Environment-aware Dynamic Analysis". *Elsevier Computers & Security (COMSEC)*.
- Seunghyeon Lee\*, Hyunmin Seo\*, Hwanjo Heo, Anduo Wang, Seungwon Shin, and Jinwoo Kim (\* Co-first author). "SECTRACER: A Framework for Uncovering the Root Causes of Network Intrusions via Security Provenance". *Elsevier Computers & Security (COMSEC)*.
- Jaehan Kim, Minkyoo Song, Minjae Seo, Youngjin Jin, Seungwon Shin and Jinwoo Kim. "PassREfinder-FL: Privacy-Preserving Credential Stuffing Risk Prediction via Graph-Based Federated Learning for Representing Password Reuse between Websites". *Elsevier Expert Systems with Applications (ESWA)*.
- Jaehan Kim, Seung Ho Na, Minkyoo Song, Seungwon Shin, Sooel Son. "MoEvil: Poisoning Expert to Compromise the Safety of Mixture-of-Experts LLMs (Distinguished Paper Award)". *The Annual Computer Security Applications Conference (ACSAC), 2025*.
- Eugene Jang, Kimin Lee, Jin-Woo Chung, Keuntae Park, Seungwon Shin. "Improbable Bigrams Expose Vulnerabilities of Incomplete Tokens in Byte-Level Tokenizers". *Conference on Empirical Methods in Natural Language Processing, 2025 (EMNLP)*.
- Minkyoo Song, Hanna Kim, Jaehan Kim, Seungwon Shin, Sooel Son. "Refusal Is Not an Option: Unlearning Safety Alignment of Large Language Models". *34th USENIX Security Symposium, 2025*.
- Myoungsung You, Jaehyun Nam, Minjae Seo, Taejune Park, Seungwon Shin. "HardMesh: Enabling High-performance Service Mesh Ingress Processing with SmartNICs". *ACM SIGCOMM 25 (Shorts)*.
- Seong-Joong Kim, Myoungsung You, Seungwon Shin. "CR-ATTACKER: Exploiting Crash-reporting Systems using Timing Gap and Unrestricted File-based Workflow". *IEEE Access, 2025*.
- Hanna Kim, Minkyoo Song, Seung Ho Na, Seungwon Shin, Kimin Lee. "When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs". *34th USENIX Security Symposium, 2025*.
- Jaehan Kim, Minkyoo Song, Seung Ho Na, Seungwon Shin. "Obliviate: Neutralizing Task-agnostic Backdoors within the Parameter-efficient Fine-tuning Paradigm". *Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2025 (NAACL Findings)*.
- Minkyoo Song, Hanna Kim, Jaehan Kim, Youngjin Jin, Seungwon Shin. "Claim-Guided Textual Backdoor Attack for Practical Applications". *Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2025 (NAACL Findings)*.
- Suryeon Kim, Seung Ho Na, Jaehan Kim, Seungwon Shin, Hyunwoo Choi. "AVXProbe: Enhancing Website Fingerprinting with Side-Channel-Assisted Kernel-Level Traces". *ACM ASIA Conference on Computer and Communications Security, 2025 (ASIACCS)*.
- Minjae Seo\*, Myoungsung You\*, Jaehan Kim, Taejune Park, Seungwon Shin, Jinwoo Kim (\* Co-first author). "MUFFLER: Secure Tor Traffic Obfuscation with Dynamic Connection Shuffling and Splitting". *IEEE International Conference on Computer Communications, 2025 (INFOCOM)*.
- Minkyoo Song, Eugene Jang, Jaehan Kim and Seungwon Shin. "Covering Cracks in Content Moderation: Delexicalized Distant Supervision for Illicit Drug Jargon Detection". *SIGKDD Conference on Knowledge Discovery and Data Mining, 2025*.
- Jian Cui, Hanna Kim, Eugene Jang, Dayeon Yim, Kicheol Kim, Yongjae Lee, Jin-Woo Chung, Seungwon Shin, and Xiaojing Liao. "Tweezers: A Framework for Security Event Detection via Event Attribution-centric Tweet Embedding". *The Network and Distributed System Security Symposium, 2025 (NDSS)*.

**2024**

- Dongmin Choi, Hyunmin Seo, Kwanwoo Kim, Myoungsung You, Seungwon Shin, and Jinwoo Kim. "Uncovering Threats in Container Systems: A Study on Misconfigured Container Components in the Wild". *IEEE Access, 2024*.
- Minjae Seo, Jaehan Kim, Myoungsung You, Seungwon Shin, and Jinwoo Kim. "gShock: A GNN-based Fingerprinting System for Permissioned Blockchain Networks over Encrypted Channels". *IEEE Access, 2024*.
- Suyeol Lee, Jaehan Kim, Minjae Seo, Seung Ho Na, Seungwon Shin and Jinwoo Kim. "CENSor: Detecting Illicit Bitcoin Operation via GCN-based Hyperedge Classification". *IEEE Access, 2024*.
- Hyunmin Seo, Seungwon Shin, and Seungsoo Lee. "BotFence: A Framework for Network-Enriched Botnet Detection and Response with SmartNICs". *IEEE Access, 2024*.
- Jinwoo Kim, Minjae Seo, Eduard Marin, Seungsoo Lee, Jaehyun Nam, and Seungwon Shin. "Ambusher: Exploring the Security of Distributed SDN Controllers through Protocol State Fuzzing". *IEEE Transactions on Information Forensics and Security (TIFS)*.
- Myoungsung You, Minjae Seo, Jaehan Kim, Seungwon Shin, and Jaehyun Nam. "Hyperion: Hardware-based High-performance and Secure System for Container Networks". *IEEE Transactions on Cloud Computing (TCC)*.
- Myoungsung You, Jaehyun Nam, Hyunmin Seo, Minjae Seo, Jaehan Kim, Dongmin Choi, Seungwon Shin. "HardWhale: A Hardware-isolated Network Security Enforcement System for Cloud Environments". *44th IEEE International Conference on Distributed Computing Systems (ICDCS)*.
- Eugene Jang, Jian Cui, Dayeon Yim, Youngjin Jin, Jin-Woo Chung, Seungwon Shin, Yongjae Lee. "Ignore Me But Don’t Replace Me: Utilizing Non-Linguistic Elements for Pretraining on the Cybersecurity Domain". *Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2024 (NAACL Findings)*.
- Jinwoo Kim, Minjae Seo, Seungsoo Lee, Jaehyun Nam, Vinod Yegneswaran, Phillip Porras, Guofei Gu, Seungwon Shin. "Enhancing Security in SDN: Systematizing Attacks and Defenses from a Penetration Perspective". *Elsevier Computer Networks 2024*.
- Hanna Kim, Jian Cui , Eugene Jang , Chanhee Lee, Yongjae Lee, Jin-Woo Chung, Seungwon Shin. "DRAINCLoG: Detecting Rouge Accounts with Illegally-obtained NFTs using Classifiers Learned on Graphs". *The Network and Distributed System Security Symposium, 2024 (NDSS)*.
- Jaehan Kim, Minkyoo Song, Minjae Seo, Youngjin Jin, Seungwon Shin. "PassREfinder: Credential Stuffing Risk Prediction by Representing Password Reuse between Websites on a Graph". *IEEE Symposium on Security and Privacy, 2024 (IEEE S&P)*.

**2023**

- Minjae Seo, Myoungsung You, Taejune Park, Seungwon Shin, Jinwoo Kim. "Poster: Towards a Secure and Practical System to Obfuscate Tor Network Traffic". *The 8th IEEE European Symposium on Security and Privacy (Euro S&P), 2023*.
- Seong-Joong Kim, Myoungsung You, Seungwon Shin. "Cryonics: Trustworthy Function-as-a-Service using Snapshot-based Enclaves". *ACM Symposium on Cloud Computing, 2023 (SoCC)*.
- Myoungsung You, Jaehyun Nam, Minjae Seo, Seungwon Shin. "HELIOS: Hardware-assisted High-performance Security Extension for Cloud". *ACM Symposium on Cloud Computing, 2023 (SoCC)*.
- Seung Ho Na, Sumin Cho, Seungwon Shin. "Evolving Bots: The New Generation of Comment Bots and their Underlying Scam Campaigns in YouTube". *Internet Measurement Conference, 2023 (IMC)*.
- Suryeon Kim, Seungwon Shin, Hyunwoo Choi. "AVX-TSCHA: Leaking Information Through AVX Extensions in Commercial Processors". *Elsevier Computers & Security (COMSEC), 2023*.
- Seung Ho Na, Kwanwoo Kim, Seungwon Shin. "Witnessing Erosion of Membership Inference Defenses: Understanding Effects of Data Drift in Membership Privacy". *Research in Attacks, Intrusions and Defenses, 2023 (RAID)*.
- Youngjin Jin, Eugene Jang, Jian Cui, Jin-Woo Chung, Yongjae Lee and Seungwon Shin. "DarkBERT: A Language Model for the Dark Side of the Internet". *Annual Meeting of the Association for Computational Linguistics, 2023 (ACL)*.
- Hyunwoo Choi, Suryeon Kim and Seungwon Shin. "AVX Timing Side-Channel Attacks against Address Space Layout Randomization". *Design Automation Conference, 2023 (DAC)*.
- Hwanjo Heo, Seungwon Woo, Taeung Yoon, Min Suk Kang and Seungwon Shin. "Partitioning Ethereum without Eclipsing It". *The Network and Distributed System Security Symposium, 2023 (NDSS)*.

**2022**

- Jinwoo Kim, Yeonkeun Kim, Vinod Yegneswaran, Phillip Porras, Seungwon Shin and Taejune Park. "Extended SDN Data Plane Architecture for In-Network Security Services". *Computers & Security (COMSEC)*.
- Myoungsung You, Yeonkeun Kim, Jaehan Kim, Minjae Seo, Sooel Son, Seungwon Shin and Seungsoo Lee. "FuzzDocs: An Automated Security Evaluation Framework for IoT". *IEEE Access, 2022*.
- Jaehyun Nam, Seungsoo Lee, Phillip Porras, Vinod Yegneswaran, Seungwon Shin. "Secure Inter-Container Communications using XDP/eBPF". *IEEE/ACM Transactions on Networking, 2022 (TON)*.
- Minjae Seo, Jaehan Kim, Eduard Marin, Myoungsung You, Taejune Park, Seungsoo Lee, Seungwon Shin, Jinwoo Kim. "Heimdallr: Fingerprinting SD-WAN Control-Plane Architecture via Encrypted Control Traffic". *The Annual Computer Security Applications Conference ( ACSAC ), 2022*.
- Seung Ho Na, Hyeong Gwon Hong, Junmo Kim, Seungwon Shin. "Closing the Loophole: Rethinking Reconstruction Attacks in Federated Learning from a Privacy Standpoint". *The Annual Computer Security Applications Conference ( ACSAC ), 2022*.
- Jaehyun Nam, Seung Ho Na, Seungwon Shin, Taejune Park. "Reconfigurable Regular Expression Matching Architecture for Real-time Pattern Update and Payload Inspection". *Journal of Network and Computer Applications, 2022 (JNCA)*.
- Jian Cui, Kwanwoo Kim, Seung Ho Na, Seungwon Shin. "Meta-Path-based Fake News Detection Leveraging Multi-level Social Context Information". *The 31st ACM International Conference on Information and Knowledge Management (CIKM)*.
- Taejune Park, Myoungsung You, Jian Cui, Youngjin Jin, Kilho Lee, Seungwon Shin. "MECaNIC: SmartNIC to Assist URLLC Processing in Multi-Access Edge Computing Platforms". *The 30th IEEE International Conference on Network Protocols (ICNP)*.
- Hyeonseong Jo, Yongjae Lee, Seungwon Shin. "Vulcan: Automatic Extraction and Analysis of Cyber Threat Intelligence from Unstructured Text". *Elsevier Computers & Security, 2022 (COMSEC)*.
- Youngjin Jin, Eugene Jang, Yongjae Lee, Seungwon Shin, Jin-Woo Chung. "Shedding New Light on the Language of the Dark Web". *Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2022 (NAACL)*.
- Seungsoo Lee, Seungwon Woo, Jinwoo Kim, Jaehyun Nam, Vinod Yegneswaran, Phillip Porras, Seungwon Shin. "A Framework for Policy Inconsistency Detection in Software-Defined Networks". *IEEE / ACM Transaction on Networking, 2022 (TON)*.
- Jinwoo Kim, Eduard Marin, Mauro Conti, Seungwon Shin. "EqualNet: A Secure and Practical Defense for Long-term Network Topology Obfuscation". *The Network and Distributed System Security Symposium, 2022 (NDSS)*.

**2021**

- Taejune park, Jaehyun Nam, Seung Ho Na, Jaewoong Chung and Seungwon Shin. "Reinhardt: Real-time Reconfigurable Hardware Architecture for Regular Expression Matching in DPI". *Annual Computer Security Application Conference, 2021 (ACSAC)*.
- Hwanjo Heo and Seungwon Shin. "Understanding Block and Transaction Logs of Permissionless Blockchain Networks". *Security and Communication Networks, 2021 [Journal] (SCN)*.
- Jinwoo Kim, Jaehyun Nam, Suyeol Lee, Vinod Yegneswaran, Phillip Porras, and Seungwon Shin. "BottleNet: Hiding Network Bottlenecks using SDN-based Topology Deception". *IEEE Transactions on Information Forensics and Security, 2021 (TIFS)*.
- Hwanjo Heo and Seungwon Shin. "Behind Block Explorers: Public Blockchain Measurement and Security Implication". *IEEE International Conference on Distributed Computing Systems, 2021 (ICDCS)*.

## 수상

누리집 Award 페이지의 2021–2025년 연도 구역에 실린 15줄이다(2025년 2줄, 2024년 1줄, 2023년 5줄, 2022년 2줄, 2021년 5줄). 한 줄은 연도, 대회·학회 이름, 상 이름, 수상자 순서다. 대회·상 이름과 수상자 이름은 누리집 표기 그대로이고, 같은 상을 받은 팀이 여럿인 줄은 팀 사이를 쌍반점(;)으로 나눴다.[^awards]

- 2025 · Annual Computer Security Applications Conference 2025 (ACSAC) · Distinguished Paper Award · 수상자 Jaehan Kim, Seung Ho Na, Minkyoo Song, Seungwon Shin, Sooel Son
- 2025 · 2025 National Cyber Security Paper Contest · Encouragement Award (장려상) · 수상자 Myoungsung You, Isu Kim, Seungwon Shin; Jaehan Kim, Minkyoo Song, Seungwon Shin
- 2024 · 2024 National Cyber Security Paper Contest · Encouragement Award (장려상) · 수상자 Myoungsung You, Seungwon Shin; Jaehan Kim, Seung Ho Na, Seungwon Shin
- 2023 · 2023 National Cyber Security Paper Contest · Grand Prize (대상) · 수상자 Myoungsung You, Jaehyun Nam, Seungwon Shin
- 2023 · 2023 National Cyber Security Paper Contest · Best Paper Award (최우수상) · 수상자 Jaehan Kim, Minkyoo Song, Youngjin Jin, Seungwon Shin
- 2023 · 2023 National Cyber Security Paper Contest · Excellence Award (우수상) · 수상자 Suryeon Kim, Seung Ho Na, Seungwon Shin
- 2023 · 2023 National Cyber Security Paper Contest · Encouragement Award (장려상) · 수상자 Hanna Kim, Geon Choi, Seungwon Shin; Jaehan Kim, Minkyoo Song, Seungwon Shin; Seung Ho Na, Sumin Cho, Seungwon Shin; Minkyoo Song, Jaehan Kim, Seungwon Shin
- 2023 · 2023 Samsung HumanTech Paper Award · Bronze Prize (동상) · 수상자 Jaehan Kim, Myoungsung You, Seungwon Shin, Jinwoo Kim
- 2022 · 2022 National Cyber Security Paper Contest · Excellence Award (우수상) · 수상자 Myoungsung You, Hyunmin Seo, Dongmin Choi, Jaehyun Nam, Seungwon Shin
- 2022 · 2022 Samsung HumanTech Paper Award · Silver Prize (은상) · 수상자 Jinwoo Kim, Seungwon Shin
- 2021 · 2021 Samsung HumanTech Paper Award · Silver Prize (은상) · 수상자 Taejune Park, Myoungsung You, Geon Choi, Youngjin Jin, Seungwon Shin
- 2021 · 2021 National Cyber Security Paper Contest · Excellence Award (우수상) · 수상자 Jinho Choi, Seungwon Shin
- 2021 · 2021 National Cyber Security Paper Contest · Encouragement Award (장려상) · 수상자 Minjae Seo, Jinwoo Kim, Jaehan Kim, Taejune Park, Myoungsung You, Seungwon Shin
- 2021 · 5th Financial Security Institute (FSI) Paper Contest · Best Paper Award (최우수상) · 수상자 Seung Ho Na, Hanna Kim, Seungwon Shin
- 2021 · 2021 KIISC Honam Branch Paper Contest · Best Paper Award (최우수상) · 수상자 Myoungsung You, Jinwoo Kim, Taejune Park, Seungwon Shin

## 소식

누리집 첫 화면 News 칸(Recent publications and highlights)의 10건이다(2025년 11월–2026년 9월). 날짜와 문구는 누리집 표기 그대로다.[^home]

- September 2026 · SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills · Accepted to ACSAC 2026
- September 2026 · SWIFT: Robust Code Watermarking via Structural Canonicalization and LLM-Based Rewriting · Accepted to ACSAC 2026
- August 2026 · A unified framework for cognition-driven security policy generation in cloud-native environments · Accepted to JNCA 2026
- May 2026 · PC²: Politically Controversial Content Generation via Jailbreaking Attacks on GPT-based Text-to-Image Models · Accepted to CCS 2026
- February 2026 · AccelFaaS: Accelerating FaaS via Pre-warmed Memory and Control Channel Offloading · Accepted to TCC 2026
- February 2026 · TDSnap: Enabling Secure Function-as-a-Service with Trusted Domain Snapshots · Accepted to DAC 2026
- January 2026 · SafeMoE: Safe Fine-Tuning for MoE LLMs by Aligning Harmful Input Routing · Accepted to ICLR 2026
- December 2025 · HybridMesh: A Hardware-software Hybrid Approach for Accelerating Service Mesh Ingress · Accepted to NSDI 2026
- December 2025 · RDNet: An RDMA-aware Container Network Interface for Cloud Environments · Accepted to INFOCOM 2026
- November 2025 · SECTRACER: A Framework for Uncovering the Root Causes of Network Intrusions via Security Provenance · Accepted to Computers & Security 2025

## 연락과 위치

- 연구실: N1 Building, Room 820, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon, Korea(누리집 표기)[^home]
- 이메일: claude@kaist.ac.kr(누리집 Contact 칸, 전기및전자공학부 교수 소개의 교수 이메일과 같다)[^home][^ee]
- 교수 사무실: IT융합빌딩 (N1) 910, 연락처 7438(전기및전자공학부 표기)[^ee][^eelist]
- 정보보호대학원 교수진 목록의 교수 전화: 042-350-8323[^gsisfac]
[^home]: 연구실 누리집 첫 화면 <https://nss.kaist.ac.kr/> (연구실 소개, Research Areas, News, Find Us·Contact 칸, 2026-10-25 열람)
[^research]: 누리집 Research 페이지 <https://nss.kaist.ac.kr/research/> (AI, Security, System 세 갈래 소개와 하위 항목, 2026-10-25 열람)
[^faculty]: 누리집 Faculty 페이지 <https://nss.kaist.ac.kr/people/faculty/> (교수 직함, 연구 소개, 경력, Education, 2026-10-25 열람)
[^people]: 누리집 People 페이지 <https://nss.kaist.ac.kr/people/> 와 하위 페이지 Postdoctoral Researchers <https://nss.kaist.ac.kr/people/postdoc/>, Doctoral Students <https://nss.kaist.ac.kr/people/phd/>, Master's Students <https://nss.kaist.ac.kr/people/masters/> (2026-10-25 열람)
[^alumni]: 누리집 Alumni 페이지 <https://nss.kaist.ac.kr/people/alumni/> (Ph.D., Master's 구역, 2026-10-25 열람)
[^pubs]: 누리집 Publication / Talk 페이지 <https://nss.kaist.ac.kr/publications/> (2015–2026년 연도 구역, 2026-10-25 열람)
[^awards]: 누리집 Award 페이지 <https://nss.kaist.ac.kr/awards/> (2018–2025년 연도 구역, 2026-10-25 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(신승원) <https://ee.kaist.ac.kr/professor/12962/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 연락처, 이메일, 웹사이트, 디비전, 학위, 대표업적, 2026-10-25 열람)
[^eelist]: KAIST 전기및전자공학부 교수진 목록 2쪽 <https://ee.kaist.ac.kr/professor-s1/?page=2> (신승원 항목, 2026-10-25 열람)
[^gsisfac]: KAIST 정보보호대학원 교수진 목록 <https://gsis.kaist.ac.kr/people/faculty> (신승원 교수 항목, 2026-10-25 열람)
[^gsislab]: KAIST 정보보호대학원 연구실 목록 <https://gsis.kaist.ac.kr/research/center> (네트워크 보안 구역의 Network and System security (NSS) Lab 항목, 2026-10-25 열람)
[^p1]: J. Kim, M. Song, S. H. Na, S. Shin, Findings of the Association for Computational Linguistics: NAACL 2025, 1288-1307 (2025). <https://doi.org/10.18653/v1/2025.findings-naacl.71> 초록 기준(OpenAlex 등록 초록).
[^p2]: J. Kim 외, S. Shin, 2024 IEEE Symposium on Security and Privacy (SP), 1385-1404 (2024). <https://doi.org/10.1109/sp54263.2024.00020> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: Y. Jin 외, S. Shin, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 7515-7533 (2023). <https://doi.org/10.18653/v1/2023.acl-long.415> 초록 기준(OpenAlex 등록 초록).
[^p4]: J. Kim 외, S. Shin, IEEE Transactions on Information Forensics and Security 19, 6264-6279 (2024). <https://doi.org/10.1109/tifs.2024.3402967> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Kim, E. Marin, M. Conti, S. Shin, Proceedings 2022 Network and Distributed System Security Symposium (2022). <https://doi.org/10.14722/ndss.2022.23154> 초록 기준(OpenAlex 등록 초록).
[^p6]: M. You 외, S. Shin, 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26), 359-375 (2026). <https://www.usenix.org/conference/nsdi26/presentation/you> 초록 기준(논문 페이지 게시 초록).
[^p7]: S.-J. Kim, M. You, B. J. Kim, S. Shin, Proceedings of the 2023 ACM Symposium on Cloud Computing, 528-543 (온라인 2023-10-31). <https://doi.org/10.1145/3620678.3624789> 초록 기준(OpenAlex 등록 초록).
[^p8]: M. You 외, S. Shin, 2024 IEEE 44th International Conference on Distributed Computing Systems (ICDCS), 496-507 (2024). <https://doi.org/10.1109/icdcs60910.2024.00053> 초록 기준(OpenAlex 등록 초록).

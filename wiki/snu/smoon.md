# 가상머신 및 최적화 연구실 (Virtual Machine & Optimization Lab, VMO Lab)

**서울대학교 공과대학 전기·정보공학부 · 문수묵 교수**

- 분야: 컴파일러와 가상머신 최적화(레지스터 할당, 최적화 단계의 순서 결정, 실행 중 컴파일, DRAM 테스트 패턴 프로그램의 번역과 비교), 블록체인(계정 상태 데이터의 최적화, 스마트 계약 취약점 탐지, 영지식 증명, 신뢰 실행 환경 기반 오프체인 결제), 인공지능(연합학습, 그래프 신경망, 지름길 학습, 코드 생성용 언어 모델)
- 대분야: 컴퓨팅·AI
- 태그: 블록체인[^home][^bc][^p1], 소프트웨어·시스템 보안[^bc][^p3], 프로그램 분석·검증[^compiler][^p3], 그래프 기계학습·지식 그래프[^ai], 대형 언어 모델[^ai][^compiler], 강화학습[^p8]
- 홈페이지: <https://altair.snu.ac.kr>
- 근거와 출처: [VMO Lab 근거 페이지](smoon-sources.md)

> 컴파일러와 가상머신 최적화 기술을 바탕으로 여러 소프트웨어 플랫폼의 최적화를 연구해 온 연구실로, 최근에는 블록체인의 데이터 크기·성능 최적화와 보안 강화, 그리고 연합학습·그래프 신경망·지름길 학습·코딩 AI용 언어 모델 같은 인공지능 연구도 한다.[^home]

## 무엇을 연구하나

연구실은 서울대학교 공과대학 전기·정보공학부 문수묵 교수가 이끄는 가상머신 및 최적화 연구실이다.[^ecelabd][^eceprof] 누리집은 영문 이름을 Virtual Machine & Optimization Lab(VMO Lab)으로 적고,[^home] 교수 페이지는 Virtual Machine and Optimization (VM&O) Laboratory로 적는다.[^prof] 학과 연구실 목록은 이 연구실을 스마트 임베디드 시스템 연구그룹에 올리고,[^ecelab] 학과 연구실 소개는 연구 분야를 "컴퓨터 및 VLSI 시스템"으로 적는다.[^ecelabd] 누리집 첫 화면은 연구실이 컴파일러(사람이 쓴 프로그램을 컴퓨터가 실행하는 기계어로 바꿔 주는 프로그램) 최적화와 가상머신(실제 컴퓨터 위에 소프트웨어로 만든 가상의 실행 환경) 최적화 기술을 바탕으로 여러 소프트웨어 플랫폼의 최적화를 연구해 왔고, 최근에는 블록체인과 인공지능 연구도 한다고 소개한다.[^home] 지금 연구하는 주제로는 인공지능(연합학습, 그래프 신경망, 지름길 학습, AI4Code), 블록체인(상태 최적화, 보안과 프라이버시), 컴파일러(컴파일과 최적화)를 든다.[^home] 학과 연구실 소개는 연구실이 가상머신 기반 플랫폼의 이식성과 간단함을 최대한 살리는 연구와 플랫폼의 성능·기능을 높이는 연구를 하고, 대형 오픈소스 프로그램을 다뤄 온 엔지니어링 지식과 경험을 바탕으로 블록체인 연구를 한다고 적는다.[^ecelabd]

첫째 갈래는 **블록체인 상태 데이터의 최적화**다. 블록체인은 여러 참여자가 같은 거래 기록을 나눠 갖고 함께 검증하는 분산 장부 기술이다. 연구 페이지는 이더리움 같은 계정 기반 블록체인이 계속 늘어나는 상태 데이터(모든 계정의 현재 값을 모아 둔 자료) 때문에 확장성과 동기화에 큰 부담을 겪는다고 보고, 활성 계정 유지(Ethanos), 지난 상태 데이터의 부담 줄이기, 확장 가능한 블록체인 저장 시스템을 위한 데이터베이스 구조 최적화를 다룬다고 적는다.[^bc] 학과 연구실 소개는 블록체인 데이터가 선형으로 늘어나는 구조라 시간이 갈수록 저장 공간이 많이 들고, 새 노드(네트워크에 참여하는 컴퓨터)가 네트워크에 들어오는 부트스트래핑(참여에 필요한 자료를 받아 맞추는 과정)도 오래 걸려 네트워크의 보안성이 떨어진다고 설명한다. 그래서 블록체인 프로토콜과 클라이언트의 성능과 공간을 최적화해 부트스트래핑을 빠르게 하는 연구를 한다고 적는다.[^ecelabd] 대표 논문에서는 상태 트라이(값을 나무 모양으로 나눠 저장하는 자료 구조) 노드에 논스(채굴자가 바꿔 가며 블록에 넣어 보는 임의의 수) 칸을 더해 채굴 과정에서 트라이 노드가 차례대로 저장되게 하고, 따로 큰 데이터 집합을 두지 않고 블록 헤더로 메모리 경도(계산에 큰 메모리가 필요해 전용 칩으로도 쉽게 빨라지지 않는 성질)를 얻는 작업 증명(계산 문제를 먼저 풀어 다음 블록을 만들 자격을 얻는 합의 방식) 채굴 알고리즘 Trie-Hashimoto를 제안했다.[^p1] 또 쓰이지 않고 잠든 계정이 대부분이라는 관찰에서, 상태 트라이를 주기마다 비우고 그 주기에 쓰인 활성 계정만으로 다시 만드는 Ethanos를 제안했다.[^p2] 최근 논문 목록에는 압축 트라이(Compact Trie)로 계정 기반 블록체인의 상태 데이터를 줄이는 Ethane(EuroSys 2026)도 있다.[^pubs]

둘째 갈래는 **블록체인 보안과 프라이버시**다. 연구 페이지는 블록체인 시스템이 온체인(블록체인 위)과 오프체인(블록체인 밖) 환경 모두에서 보안, 프라이버시, 신뢰성을 강하게 보장해야 한다고 보고, 인공지능 기반 스마트 계약(블록체인 위에서 정해진 조건대로 자동 실행되는 프로그램) 취약점 분석(BugSweeper), 영지식 증명(내용을 드러내지 않고 어떤 주장이 참임을 증명하는 암호 기법) 시스템, 거래 프라이버시를 위한 암호화 멤풀(블록에 담기기를 기다리는 거래들이 모이는 대기 공간) 프로토콜, 신뢰 실행 환경(TEE, Trusted Execution Environment, 프로세서 안에서 다른 프로그램이 들여다보거나 바꿀 수 없게 격리한 실행 영역)에 기반한 안전한 오프체인 결제 프로토콜을 다룬다고 적는다.[^bc] 학과 연구실 소개도 블록체인 데이터 분석과 클라이언트 최적화, 트랜잭션 처리와 블록에 대한 이론 연구와 함께 합의 알고리즘(참여자들이 같은 기록에 동의하게 하는 절차)이나 SGX(Software Guard Extensions, 프로세서가 제공하는 신뢰 실행 환경 기술의 하나)를 쓴 블록체인 보안 연구를 든다.[^ecelabd] 대표 논문에서는 이더리움 스마트 계약의 소스 코드를 함수 단위 그래프로 바꾸고 두 단계 그래프 신경망으로 취약점을 찾는 BugSweeper를 만들었고,[^p3] 신뢰 실행 환경을 갖춘 중앙 호스트 위에서 결제 내역을 호스트에게도 숨기며 블록체인 밖 결제를 처리하는 RouTEE를 만들었다.[^p4] 최근 논문 목록에는 영지식 주소 추상화(Zero-Knowledge Address Abstraction)로 블록체인 주소를 넘어서려는 연구(SAC 2025)도 있다.[^pubs]

셋째 갈래는 **인공지능: 연합학습, 그래프 신경망, 지름길 학습, 코드 생성 언어 모델**이다. 연구 페이지는 연합학습(데이터를 각 기기에 둔 채 기기마다 학습한 모델만 모아 함께 모델을 만드는 학습 방법)이 클라이언트 데이터의 프라이버시를 지키면서 엣지 기기(사용자 가까이에서 쓰는 단말 기기)로 모델을 학습하게 해 주지만 실제로 쓰기에는 한계가 남아 있다고 보고, 데이터 이질성, 시스템 이질성, 백도어(특정 입력에서만 몰래 틀린 동작을 하도록 심어 둔 장치) 취약성, 모델 프라이버시 문제를 다룬다고 적는다.[^ai] 그래프 신경망(점과 선으로 이뤄진 그래프 자료를 다루는 신경망)은 메시지 전달(이웃한 점끼리 정보를 주고받으며 표현을 고치는 과정)을 되풀이하면서 과평활화(over-smoothing)와 과압축(over-squashing) 같은 한계를 겪는데, 연구실은 학습 전에 인접 행렬(어느 점끼리 이어져 있는지 나타낸 표)을 알맞게 고치는 리와이어링(rewiring) 기법으로 그래프 구조를 최적화해 이 문제를 줄이려 한다.[^ai] 지름길 학습(shortcut learning) 연구는 학습 데이터 자체에 치우침이 있을 때 신경망이 치우친 특징을 배우는 까닭을 설명하고 이를 줄이는 알고리즘을 만드는 것을 목표로 하며, 신경 탄젠트 커널(NTK, Neural Tangent Kernel)을 분석 틀로 내세워 치우친 특징이 다른 특징보다 빨리 학습되는 까닭을 밝힌다.[^ai] AI4Code는 코드 관련 작업을 위한 언어 모델을 발전시켜 더 효과적이고 안전한 코드 생성을 하려는 연구로, 여러 종류의 언어 모델을 코드 분야에 맞추는 방법, 그중에서도 올바르고 믿을 수 있고 안전한 코드를 만드는 능력을 높이는 방법을 살피며, 특히 기존 자기회귀 모델(앞의 낱말을 보고 다음 낱말을 차례로 만들어 가는 모델)과 다른 생성 방식인 확산 언어 모델(Diffusion Language Model)에 집중한다.[^ai] 대표 논문에서는 자원이 서로 다른 클라이언트에게 전체 모델의 깊은 층을 잘라 낸 모델을 나눠 주고 상호 자기 증류로 깊은 층의 학습 부족을 줄이는 DepthFL을 제안했고,[^p5] 연합학습 알고리즘들이 실제로 따라가는 수정된 손실 함수를 역방향 오차 분석으로 구해 방법마다 수렴 양상이 다른 까닭을 설명했으며,[^p6] 신경 탄젠트 커널로 선형 신경망을 분석해, 군집마다 표본 수가 다른 데이터에서 생기는 지름길 특징이 신경 탄젠트 커널의 고윳값(커널이 정하는 변환에서 그 특징이 몇 배로 바뀌는지 나타내는 값)이 큰 특징에 해당함을 보였다.[^p7] 최근 논문 목록에는 탈중앙 연합학습을 빠르고 믿을 수 있게 하는 방법 FRAIN(SAC 2026)과 블록체인 기반의 대규모 모델 추론·학습 플랫폼 BRAIN(IEEE Access, 2024)도 있다.[^pubs]

넷째 갈래는 **컴파일러 최적화**다. 컴파일러 연구 페이지는 세 주제를 든다. 첫째는 기계학습으로 최적화 단계의 순서를 정하는 일(phase ordering)이다. 현대 컴파일러에는 수십 년 동안 쌓인 최적화 패스(프로그램을 고쳐 빠르게 만드는 변환 단계, transform이라고도 한다)가 많고, 이 변환들은 흔히 정보를 잃으며 되돌릴 수 없어 적용 순서가 성능에 크게 영향을 준다. 연구실은 대형 언어 모델(LLM, Large Language Model)을 포함한 기계학습 모델로 프로그램에 맞춘 최적화 패스 순서(파이프라인)를 정해 실행 성능을 높인다. 기계학습을 쓴 순서 결정은 -O3(컴파일러에 미리 정해 둔 최적화 단계 묶음) 같은 기존 파이프라인을 앞설 수 있지만 시간이 오래 걸리고 큰 계산 장비가 필요해, 좋은 파이프라인을 효율적으로 찾는 방법도 함께 연구하며, 메타휴리스틱(정답을 보장하지 않는 대신 넓은 후보 가운데 좋은 해를 찾아 가는 범용 탐색 방법)과 LLM을 결합하는 방법을 살피고 있다.[^compiler] 둘째는 사전 컴파일(AOT, ahead-of-time, 실행 전에 미리 기계어로 바꿔 두는 방식)과 실행 중 컴파일(JIT, just-in-time, 실행하는 동안 필요한 부분을 기계어로 바꾸는 방식) 컴파일러 구조의 최적화로, 지금은 JIT 컴파일러의 실행 중 컴파일 지연을 줄이는 연구를 한다. JIT 컴파일러 사용자는 실행 중 컴파일 시간과 실행 시간을 모두 기다려야 하므로, 미리 컴파일해 둔 프로그램 조각을 쓰는 비용 대비 효과적인 최적화를 넣어 컴파일 지연과 실행 시간 사이의 맞바꿈을 고를 수 있는 조절 장치를 JIT 컴파일러에 더한다.[^compiler] 셋째는 도메인 특화 언어(DSL, Domain-Specific Language, 특정 용도에 맞춰 만든 작은 프로그래밍 언어)의 문제 풀이로, 서로 다른 두 DRAM 테스트 패턴 프로그램이 같은 동작을 하는지 비교하는 연구를 한다. 두 프로그램을 실행하지 않고 비교하는 일은 복잡한 반복문 구조와 기호 상태 갱신 탓에 규모를 키우기 어려운데, 연구실은 프로그램을 반복문을 인식하는 그래프 기반 중간 표현(IR, Intermediate Representation, 컴파일러가 분석과 변환에 쓰는 내부 표현)으로 옮기고, 핵심 동작을 스칼라 진화(SCEV, Scalar Evolution) 형태로 뽑아 다면체 분석(polyhedral analysis)의 언어로 나타낸 뒤 해시값으로 비교해 이 문제를 푼다.[^compiler] 학과 연구실 소개는 DRAM 테스트에 쓰는 자동 시험 장비(ATE, Automated Test Equipment)를 구동하는 프로그램을 패턴 프로그램이라 부르며, 장비마다 프로그래밍 언어와 하드웨어 구조가 달라 한 장비용 패턴 프로그램을 다른 장비용으로 자동 번역하는 소프트웨어 플랫폼을 제안하고 중간 표현, 레지스터 할당(계산할 값을 프로세서 안의 저장 칸인 레지스터에 배정하는 일), 명령어 스케줄링 같은 최적화 컴파일러의 개념을 이 플랫폼 위에서 다시 정의해 해법을 제안한다고 적는다.[^ecelabd] 대표 논문에서는 이 장비의 불규칙한 레지스터 구조에 맞춘 레지스터 할당 문제를 심층 강화학습으로 풀었다.[^p8] 최근 논문 목록에는 테스트 패턴 프로그램을 번역할 때의 불규칙한 레지스터 할당 연구(ACM Transactions on Architecture and Code Optimization, 2021)와, 실행 중인 웹 앱을 다른 기기로 옮겨 이어서 실행하는 웹 앱 이주 연구(ICWE 2021·2022, Journal of Web Engineering 2023)도 있다.[^pubs]

학과 연구실 소개는 연구 주제로 블록체인 기반의 탈중앙화 딥러닝 플랫폼, 블록체인 부트스트래핑과 성능·공간 최적화, 엣지 컴퓨팅 환경에서의 DNN(Deep Neural Network, 심층 신경망) 연산 오프로딩 플랫폼, DRAM 테스트 패턴 프로그램의 변환 플랫폼, 웹 플랫폼 성능 최적화의 다섯 가지를 든다.[^ecelabd] 오프로딩(계산을 다른 컴퓨터에 넘겨 대신 처리하게 하는 일) 연구는 하드웨어가 제한된 모바일 기기에서 연산량이 많은 DNN 앱을 돌리려고 DNN 연산을 가까운 엣지 클라우드에 넘겨 수행하는 기술이고, 웹 플랫폼 연구는 웹 앱이 로딩된 뒤의 상태를 파일로 저장해 두었다 다시 써서 로딩 시간을 줄이는 스냅샷 기술과 리소스를 미리 불러와 네트워크 지연을 줄이는 기술을 다룬다고 적는다.[^ecelabd]

## 주요 연구 주제

### 1. 블록체인 상태 데이터의 최적화

이더리움 같은 계정 기반 블록체인에서 계속 늘어나는 상태 데이터를 줄이고 새 노드의 부트스트래핑을 빠르게 한다. 활성 계정 유지, 지난 상태 데이터의 부담 줄이기, 블록체인 저장 시스템의 데이터베이스 구조 최적화를 다룬다.[^bc][^ecelabd] 상태 트라이 기반 작업 증명 채굴 알고리즘 Trie-Hashimoto, 활성 계정만으로 상태 트라이를 다시 만드는 Ethanos가 이 갈래다.[^p1][^p2] 대표 논문 1, 2.

### 2. 블록체인 보안과 프라이버시

인공지능 기반 스마트 계약 취약점 분석, 영지식 증명 시스템, 거래 프라이버시를 위한 암호화 멤풀 프로토콜, 신뢰 실행 환경 기반의 안전한 오프체인 결제 프로토콜을 연구한다.[^bc] 스마트 계약 취약점을 그래프 신경망으로 찾는 BugSweeper, 신뢰 실행 환경 기반의 오프체인 결제 RouTEE가 이 갈래다.[^p3][^p4] 대표 논문 3, 4.

### 3. 인공지능: 연합학습, 그래프 신경망, 지름길 학습, 코드 생성 언어 모델

연합학습의 데이터·시스템 이질성과 백도어 취약성·모델 프라이버시, 그래프 신경망의 리와이어링, 지름길 학습의 원리 분석과 완화, 코드 생성을 위한 확산 언어 모델을 다룬다.[^ai] 깊이를 줄인 로컬 모델로 자원이 다른 기기를 학습에 참여시키는 DepthFL, 역방향 오차 분석으로 본 연합학습의 수렴, 신경 탄젠트 커널로 본 지름길 특징이 이 갈래다.[^p5][^p6][^p7] 대표 논문 5–7.

### 4. 컴파일러 최적화

기계학습과 LLM으로 최적화 단계의 순서 정하기, JIT 컴파일러의 컴파일 지연 줄이기, DRAM 테스트 패턴 프로그램 같은 도메인 특화 프로그램의 비교와 번역을 연구한다.[^compiler][^ecelabd] 자동 시험 장비 프로그램의 레지스터 할당을 심층 강화학습으로 푼 연구가 이 갈래다.[^p8] 대표 논문 8.

## 대표 논문

랩 Publication 페이지의 2021–2026년 논문 가운데 문수묵 교수가 마지막 저자인 학회·학술지 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Trie-Hashimoto: State Trie-Based Proof-of-Work Mining for Optimizing Blockchain Storage](https://doi.org/10.1109/access.2024.3360379) · IEEE Access | 블록체인은 P2P 네트워크(중앙 서버 없이 참여 컴퓨터끼리 직접 주고받는 망)에서 무결성과 합의를 이루려고 암호 해시(자료를 고정 길이의 요약값으로 바꾸는 계산)를 많이 쓰지만, 해시 때문에 생기는 비효율도 있다. 블록체인은 데이터를 해시 요약값을 열쇠로 삼아 데이터베이스에 저장하므로 늘 무작위 순서로 읽고 쓰는데, 이는 상태 트라이라는 거대한 해시 기반 계정 자료 구조를 유지해야 하는 이더리움 같은 계정 기반 블록체인의 성능에 특히 영향을 줄 수 있다. 또 작업 증명(PoW) 합의 알고리즘은 채굴자에게 블록 해시를 난이도 기준보다 낮게 만드는 논스(채굴자가 바꿔 가며 블록에 넣어 보는 임의의 수)를 찾게 하는데, 병렬로 해시를 계산하는 ASIC(특정 용도 전용 칩) 때문에 PoW는 메모리 경도(계산에 큰 메모리가 필요해 전용 칩으로도 쉽게 빨라지지 않는 성질)와 ASIC 저항성을 얻으려고 Ethash DAG 같은 큰 데이터 집합을 쓰게 되었다. 그런데 많은 경량 클라이언트(블록체인 전체를 저장하지 않는 가벼운 참여 프로그램)는 이 데이터 집합의 부담을 감당하지 못해 논스를 검증하기 어렵다. 이 연구는 이 문제들을 풀려고 새 PoW 채굴 알고리즘 Trie-Hashimoto를 제안했다. 상태 트라이 노드에 논스 칸을 더하고, 채굴자가 새 블록에서 새로 생기는 모든 트라이 노드의 논스를 찾아 각 노드의 해시 요약값 앞부분이 블록 번호와 같아지게 한다. 그러면 트라이 노드를 차례대로 저장할 수 있어 데이터베이스 성능이 빨라진다. 메모리 경도도 다른 방식으로 얻는데, 따로 데이터 집합을 두지 않고 모든 클라이언트가 유지해야 하는 블록 헤더를 쓴다. 계정의 머클 증명(어떤 자료가 전체 기록에 들어 있음을 해시 몇 개로 보이는 증명) 몇 개로 일부만 검증할 수도 있어, 자원이 최소인 클라이언트나 연동되는 다른 블록체인의 스마트 계약도 높은 확률로 블록을 검증할 수 있다. 끝으로 채굴자 사이의 네트워크 부담을 키워 큰 채굴 풀(여러 채굴자가 힘을 합친 집단)을 억제한다. 50만 블록과 1억 계정으로 Geth 클라이언트에서 한 실험에서 Trie-Hashimoto는 거래 실행 시간을 눈에 띄게 개선해 전체 동기화 시간을 절반으로 줄였고, Ethash만큼 충분한 메모리 경도를 보였다. Trie-Hashimoto 채굴 풀은 전체 채굴자 수에 비례해 매우 자주 메시지를 주고받아야 한다.[^p1] | 1저자 Jae-Yun Kim, 마지막 저자 문수묵 |
| 2 | 2021 | [Ethanos: Efficient Bootstrapping for Full Nodes on Account-based Blockchain](https://doi.org/10.1145/3447786.3456231) · EuroSys 2021 | 이더리움은 계정 기반 블록체인(계정마다 잔액과 상태를 기록하는 블록체인)으로, 계정과 거래 수가 치솟아 데이터가 폭증했다. 그 결과 PC나 스마트폰을 쓰는 일반 사용자는 풀 노드(모든 거래를 스스로 검증하는 참여 컴퓨터)로 부트스트래핑하기 어려워 다른 풀 노드에 거래 검증을 맡기고, 그만큼 보안 위험에 노출된다. 가장 큰 부담은 블록의 상태 트라이에 담긴 모든 계정의 상태를 동기화하는 일로, 수십 기가바이트에 이른다. 계정의 95%가 넘게 쓰이지 않고 잠들어 있다는 관찰에서, 상태 트라이를 주기마다 비우고 그 주기의 거래에 쓰인 활성 계정만으로 다시 만드는 상태 최적화 기법 Ethanos를 제안했다. 거래는 현재 주기의 상태 트라이와 바로 앞 주기 끝의 상태 트라이에 있는 계정으로 처리하고, 두 트라이 어디에도 없는 계정은 복원 거래를 보내 먼저 스스로를 되살린다. 이 상태 관리의 중요한 결과로, 노드는 가장 최근 주기의 상태 트라이만으로 부트스트래핑하면서도 그 뒤의 모든 거래를 온전히 검증할 수 있다. 700만 번째 블록부터 30만 블록의 실제 이더리움 거래로, 상태 트라이를 1주일마다 비우는 조건에서 평가했다. Ethanos는 복원 거래가 아주 적은 비율만 생기면서 상태 트라이를 크게 줄였고, 시간이 갈수록 계속 커지는 이더리움 상태 트라이와 달리 1주일 동안 활성인 계정이 100만 개를 넘을 때도 주기 끝의 상태 트라이 크기가 수백 MB를 넘지 않았다.[^p2] | 1저자 Jae-Yun Kim, 마지막 저자 문수묵 |
| 3 | 2026 | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](https://doi.org/10.1609/aaai.v40i1.37021) · AAAI 2026 | 이더리움이 빠르게 커지면서 스마트 계약의 취약점을 빠르고 정확하게 찾는 일이 더 중요해졌다. 기계학습 기반 방법이 어느 정도 가능성을 보였지만, 상당수는 여전히 분야 전문가가 설계한 규칙 기반 전처리에 기댄다. 규칙 기반 전처리는 소스 코드의 중요한 맥락을 버리는 일이 많아 일부 취약점을 놓치게 하고 새로 나타나는 위협에 맞춰 바꾸기 어렵게 할 수 있다. 이 연구는 사람이 손으로 설계하는 작업 없이 소스 코드에서 바로 취약점을 찾는 종단간(입력부터 결과까지 한 모델로 처리하는) 딥러닝 틀 BugSweeper를 내놓았다. Solidity(스마트 계약을 작성하는 프로그래밍 언어) 함수 하나하나를 함수 단위 추상 구문 그래프(FLAG)로 나타내는데, 이는 추상 구문 트리(AST, 프로그램의 문법 구조를 나무 모양으로 나타낸 것)에 제어 흐름과 데이터 흐름의 의미를 더한 새 그래프다. 이어 두 단계 그래프 신경망(GNN)이 이 그래프를 분석한다. 첫 단계 GNN은 구문 그래프에서 잡음을 걸러 내고, 둘째 단계 GNN은 여러 취약점을 찾는 높은 수준의 추론을 한다. 실제 계약으로 한 폭넓은 실험에서 BugSweeper는 최신 탐지 방법 모두를 크게 앞섰다. 손으로 만든 규칙이 필요 없어, 보안 전문가에 기대지 않고 스마트 계약을 지키는 튼튼하고 자동화되고 규모를 키울 수 있는 해법을 제시한다.[^p3] | 1저자 Uisang Lee, 마지막 저자 문수묵 |
| 4 | 2024 | [RouTEE: Secure, Scalable, and Efficient Off-Chain Payments using Trusted Execution Environments](https://doi.org/10.1109/acsac63791.2024.00048) · ACSAC 2024 | 신뢰 실행 환경(TEE)을 갖춘 중앙 호스트(서비스를 운영하는 컴퓨터) 위에서 돌면서 기밀성과 무결성을 보장하고 규모를 크게 키울 수 있는 결제 시스템 trusTEE-chain을 제안했다. 그 구현인 RouTEE는 오픈소스 TEE 응용 프로그램으로, 기존 결제 시스템의 여러 문제를 한꺼번에 푸는 해법을 내놓는다. 호스트가 RouTEE를 돌리지만 결제 내역을 비롯한 데이터는 호스트에게 숨길 수 있고, RouTEE는 자체 담보 없이 사용자의 예치금을 받아 결제한다. 사용자는 블록체인 전체가 아니라 블록 헤더만 비동기로 검증하면 되고, 금전 손실 걱정 없이 무기한 오프라인 상태로 있을 수 있다. 결제 처리량이 TEE 성능에만 제한되므로 규모를 크게 키울 수 있다. 다만 호스트가 가짜 블록을 넣거나 동작을 멈추는 식으로 부정을 저지를 수 있어 TEE만으로는 충분하지 않다. 그래서 새 프로토콜과 보상 구조(인센티브 모델)를 도입해 합리적인 호스트가 정직하게 행동하도록 만들었고, 고장, 뚫린 TEE, 비합리적인 호스트에 대한 해법도 제안했다. RouTEE는 UTXO(Unspent Transaction Output, 거래에서 아직 쓰이지 않은 출력을 단위로 잔액을 관리하는 방식) 기반의 어떤 블록체인에서도 작동하고 디지털 서명만 필요해 이식성이 높다. 비트코인 위에서 Intel SGX로 구현한 결과, 데이터 백업이 잦은 경우에도 15만 명이 넘는 사용자에 대해 높은 처리량을 냈다.[^p4] | 1저자 Junmo Lee, 마지막 저자 문수묵 |
| 5 | 2023 | [DepthFL: Depthwise Federated Learning for Heterogeneous Clients](https://openreview.net/forum?id=pf8RIZTMU58) · ICLR 2023 | 연합학습은 클라이언트(학습에 참여하는 기기)의 개인 데이터를 모으지 않고 전체 모델을 학습하는 방법이다. 대신 클라이언트는 자기 기기에서 고친 가중치나 기울기를 되풀이해 올려야 하므로 학습에 참여할 만큼의 계산·통신 자원이 필요한데, 실제로는 클라이언트마다 자원이 제각각이다. 자원이 모자란 클라이언트도 작은 로컬 모델을 학습하도록 전체 모델의 채널 수를 줄이는 너비 축소 기법이 쓰여 왔지만, 너비가 다른 로컬 모델들을 평균할 때의 이질성 때문에 자원이 모자란 클라이언트를 학습에서 그냥 빼는 경우보다도 정확도가 낮았다. 이 연구는 깊이 축소에 기반한 새 방법 DepthFL을 제안했다. DepthFL은 전체 모델에서 가장 깊은 층들을 잘라 내 깊이가 다른 로컬 모델들을 정하고, 클라이언트의 가용 자원에 따라 나눠 준다. 많은 클라이언트가 깊은 로컬 모델을 학습할 자원이 모자라, 깊은 층은 얕은 층과 달리 모자란 데이터로 일부만 학습되는 문제가 생긴다. DepthFL은 로컬 모델 안에서 깊이가 다른 분류기들이 서로의 지식을 나눠 배우는 상호 자기 증류(한 모델 안의 여러 부분이 서로의 예측을 따라 배우게 하는 학습)로 이 문제를 줄인다. 실험에서 깊이를 줄인 로컬 모델이 너비를 줄인 모델보다 전체 모델을 더 잘 만들었고, 자기 증류는 데이터가 모자란 깊은 층을 학습시키는 데 매우 효과적이었다.[^p5] | 1저자 Minjae Kim, 마지막 저자 문수묵 |
| 6 | 2025 | [Convergence Analysis of Federated Learning Methods Using Backward Error Analysis](https://doi.org/10.1609/aaai.v39i18.34060) · AAAI 2025 | 역방향 오차 분석(backward error analysis)을 쓰면 최적화 방법의 영향 아래에서 매개변수 갱신이 실제로 따라가는 수정된 손실 함수(학습이 줄이려는 오차를 나타내는 함수)를 찾을 수 있다. 이 수정된 함수에 더해지는 손실 항을 암묵적 정규화 항이라 부른다. 이 연구는 클라이언트마다 데이터 분포가 다른(non-IID) 상황에서 여러 연합학습 알고리즘의 암묵적 정규화 항을 구하고, 방법마다 수렴 양상이 다른 까닭을 설명하려 했다. 먼저 FedAvg의 암묵적 정규화 항이 각 클라이언트의 기울기를 평균 기울기에서 흩어지게 해 기울기의 분산을 키운다는 것을 보였고, 이 항이 수렴을 방해한다는 것도 실험으로 보였다. 같은 방식으로 FedSAM과 SCAFFOLD의 암묵적 정규화 항을 계산해 두 방법이 더 잘 수렴하는 까닭을 설명했다. 기존 수렴 분석이 FedSAM과 SCAFFOLD의 장점을 짚는 데 집중한 것과 달리, 이 접근은 복잡한 비볼록(non-convex) 상황에서 두 방법의 한계도 설명할 수 있다. 구체적으로 FedSAM은 FedAvg 암묵적 정규화 항의 1차 항에 든 치우침을 일부 없애고, SCAFFOLD는 1차 항의 치우침은 모두 없애지만 2차 항의 치우침은 없애지 못함을 보였다. 따라서 암묵적 정규화 항은 다른 이론적 관점에서 연합학습의 수렴 양상을 이해하는 데 유용한 통찰을 줄 수 있다.[^p6] | 1저자 Jinwoo Lim, 마지막 저자 문수묵 |
| 7 | 2025 | [Shortcut Features as Top Eigenfunctions of NTK: A Linear Neural Network Case and More](https://doi.org/10.52202/085713-3149) · NeurIPS 2025 | 지름길 학습은 딥러닝 모델의 고질적인 문제 가운데 하나다. 학습 데이터 대부분이 어떤 특징에 지배되면, 신경망은 그 특징이 학습 데이터 밖에서는 통하지 않더라도 그 특징을 배우는 쪽을 택한다. 이 연구는 신경 탄젠트 커널(NTK)의 틀에서 선형 신경망의 경우를 분석해 지름길 학습의 중요한 성질 몇 가지를 끌어냈다. 신경망의 「특징」을 NTK의 고유함수(커널이 정하는 변환을 거쳐도 모양은 그대로이고 일정한 배수로만 바뀌는 함수로, 그 배수를 고윳값이라 한다)로 정의했고, 지름길이 군집을 이룬 분포에서 표본 수의 불균형 때문에 생길 때 지름길 특징이 고윳값이 큰 특징에 해당한다는 것을 찾았다. 또 고윳값이 큰 특징은 군집 안 데이터의 분산 때문에 학습이 끝난 뒤에도 신경망 출력에 큰 영향을 남긴다는 것을 보였다. 이런 특정 특징에 대한 선호는 신경망 출력의 마진(분류에서 정답 쪽 출력이 다른 쪽보다 얼마나 앞서는지를 나타내는 값)을 조절해도 남아, 최대 마진 편향(학습이 마진을 가장 크게 하는 해 쪽으로 기우는 경향)이 지름길 학습의 유일한 주된 원인은 아님을 보여 준다. 선형 신경망의 이 성질들을 2층 ReLU(음수 입력은 0으로, 양수 입력은 그대로 내보내는 함수) 완전 연결 신경망과 ResNet-18 같은 더 복잡한 신경망으로도 실험으로 넓혀 확인했다.[^p7] | 1저자 Jinwoo Lim, 마지막 저자 문수묵 |
| 8 | 2022 | [Solving PBQP-Based Register Allocation using Deep Reinforcement Learning](https://doi.org/10.1109/cgo53902.2022.9741272) · CGO 2022 | 구조가 불규칙한 레지스터는 추상화하고 할당하기 어렵다. 분할 불리언 이차 계획법(PBQP, Partitioned Boolean Quadratic Programming, 여러 선택지의 조합 가운데 비용 합이 가장 작은 것을 고르는 최적화 문제의 한 형식)은 복잡한 레지스터 제약을 나타내는 데 쓸모 있는 추상화로, DRAM 메모리 칩의 자동 시험 장비(ATE)처럼 매우 불규칙한 프로세서의 제약까지 나타낼 수 있다. PBQP 문제는 NP-난해(효율적으로 정확히 푸는 방법이 알려지지 않은 어려운 문제 부류)라서 휴리스틱(경험에 기댄 근사 풀이) 해법이 필요하다. 그런데 ATE에서처럼 스필(레지스터가 모자라 값을 메모리로 내보내는 일)이 허용되지 않으면 스필 하나가 곧 컴파일 전체의 실패를 뜻하므로, 근사하기보다 더 많이 열거해 해를 찾아야 한다. 이 연구는 PBQP 문제를 심층 강화학습, 구체적으로 검증된 심층 강화학습 기술인 Alphazero에서 쓰인 몬테카를로 트리 탐색(무작위 시뮬레이션 결과로 유망한 선택을 골라 가며 탐색 나무를 넓히는 방법)과 심층 신경망을 함께 쓰는 모델 기반 접근으로 풀자고 제안했다. 무작위 PBQP 그래프로 공들여 학습한 심층 강화학습 풀이기는 탐색 공간을 크게 줄여 열거 기반 해법의 부담을 덜었다. 알맞은 색칠 순서(그래프의 점에 레지스터를 배정해 가는 순서)와 되돌아가기 탐색(backtracking)을 함께 쓰면 적당히 학습한 신경망으로도 더 작은 탐색 공간에서 해를 찾을 수 있었다. 실험에서 제품 수준의 ATE 프로그램 10개의 해를 찾으면서 이전 PBQP 열거 풀이기보다 훨씬 적은 상태(예: 3,500분의 1)만 탐색했고, 일반 CPU용 llvm-test-suite의 C 프로그램에서는 LLVM에 있는 기존 PBQP 레지스터 할당기와 견줄 만한 성능을 냈다.[^p8] | 1저자 Minsu Kim, 마지막 저자 문수묵 |

## 교수와 전문 분야

문수묵 교수는 1987년 서울대학교 컴퓨터공학과에서 학사를, 미국 University of Maryland, College Park에서 1990년 석사와 1993년 박사를 받았다.[^eceprof][^prof] 교수 페이지 약력은 교수가 1992–1993년 IBM Thomas J. Watson Research Center에서 IBM VLIW 컴파일러(VLIW는 Very Long Instruction Word, 여러 연산을 긴 명령어 하나에 묶어 동시에 실행하는 프로세서 구조)를 개발했고, 1993–1994년 Hewlett-Packard Company의 California Language Lab에서 소프트웨어 설계 엔지니어로 PA-RISC 프로세서용 최적화 컴파일러 개발에 참여했다고 적는다. 1994년부터 서울대학교 전기·정보공학부 교수로 있으며 지금은 정교수이고, 1997년 여름 IBM T. J. Watson 연구소의 방문 연구원(visiting scientist), 2002–2003년 Sun Microsystems의 방문 교수였다. 2012–2015년에는 LG전자와 함께 LG webOS 플랫폼 최적화를 한 LG-SNU 플랫폼 센터를 이끌었고, 플랫폼 연구에 더해 최근 블록체인과 인공지능 연구로 넓혔다고 적는다.[^prof] 학과 교수 소개의 주요경력은 1991년 여름과 1992–1993년 IBM Thomas J. Watson Research Center 인턴 근무, 1993–1994년 Hewlett-Packard Company(California Language Lab) Software design engineer, 1994년부터 서울대학교 전기공학부 교수, 1997년 7–8월 IBM Watson 연구소 visiting scientist, 2002년 Sun Microsystems Visiting Professor로 적는다.[^eceprof]

교수 페이지 Awards 칸은 IBM Faculty Partnership Awards(2000년 9월), LG그룹의 LG Group R&D Awards(2012년 3월), 서울대학교 공과대학 Best Teacher Award(2024, 2022, 2002년), 서울대학교 전기·정보공학부(School of Electrical and Computer Engineering) Best Teacher Award(2023, 2021, 2019, 2018년)를 적는다.[^prof] 교수 페이지의 산업 과제 목록에는 IBM T. J. Watson Research Center와 한 자바 가상머신용 JIT 컴파일러 LaTTe·VLaTTe, Sun Microsystems·HP와 한 명령어·파이프라인 스케줄링 과제, Intel과 한 EPIC 구조용 자바 JIT 컴파일 과제, 삼성전자와 한 모바일 플랫폼·GPU의 LLVM(오픈소스 컴파일러 기반 구조) 기반 최적화, 안드로이드 Dalvik 가상머신 최적화, 모바일 자바스크립트 엔진의 JIT 컴파일, DRAM 테스트 패턴 프로그램 번역, LG전자와 한 디지털 TV·블루레이 디스크 플레이어용 자바 최적화가 올라 있다.[^prof]

학과 교수 소개는 전공을 컴파일러 최적화, 가상머신 최적화, 웹 브라우저 최적화, 인공지능을 위한 엣지 컴퓨팅, 프로그램 변환, 블록체인 가상머신으로, 분야를 컴파일러, 가상머신, 블록체인, 연합학습으로 적고, Research Interest로 블록체인 최적화, 연합학습, 메모리 반도체 테스트 프로그램의 변환, 웹 앱의 가속화를 든다.[^eceprof] 교수 페이지의 관심 분야는 컴파일러와 가상머신 최적화, 인공지능 연구(연합학습, 그래프 신경망, 지름길 학습, AI4Code), 블록체인(상태 최적화, 보안과 프라이버시)이다.[^prof] 랩 Publication 페이지의 목록을 시기별로 보면, Old papers 구역의 1995–2006년 논문은 VLIW 프로세서를 위한 명령어 스케줄링과 소프트웨어 파이프라이닝(반복문의 여러 회차를 겹쳐 실행하도록 명령어를 배치하는 기법), 레지스터 할당, 자바 JIT 컴파일러 VLaTTe와 자바 가상머신의 메모리 관리·예외 처리를 주로 다룬다. 2007–2014년 논문은 임베디드 기기·디지털 TV·블루레이 디스크 플레이어용 자바 사전 컴파일과 JIT 컴파일, 안드로이드 Dalvik 가상머신, 모바일 자바스크립트 JIT 컴파일러를, 2015–2020년 논문은 자바스크립트 사전 컴파일, 스냅샷으로 웹 앱 로딩을 빠르게 하는 연구, 기기 사이의 웹 앱 이주, 모바일 기기의 심층 신경망 연산을 엣지 서버로 넘기는 오프로딩, DRAM 테스트 패턴 프로그램 번역을 주로 다룬다. 블록체인 논문은 2018년 블록체인 기반 엣지 컴퓨팅 워크숍 논문이 처음이고, 2021년 이후 논문은 블록체인 상태 최적화와 보안, 연합학습과 신경망 학습 이론, 레지스터 할당, 웹 앱 이주가 중심이다.[^pubs]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 이더리움 같은 계정 기반 블록체인의 상태 데이터를 줄여 저장과 동기화 부담을 덜고 새 노드의 참여를 쉽게 하는 상태 최적화다(대표 논문 1, 2).[^p1][^p2] 둘째, 스마트 계약의 취약점을 찾고 블록체인 밖에서 하는 결제를 안전하게 만드는 블록체인 보안이다(대표 논문 3, 4).[^p3][^p4] 셋째, 연합학습 방법의 설계와 수렴 분석, 그리고 신경망이 치우친 특징을 배우는 원리의 분석이다(대표 논문 5–7).[^p5][^p6][^p7] 넷째, 레지스터 할당 같은 컴파일러 최적화 문제를 강화학습 같은 새 방법으로 푸는 연구다(대표 논문 8).[^p8]

## 응용 분야

누리집은 블록체인 연구가 데이터 크기와 성능을 최적화하고 보안을 높이는 데 초점을 둔다고 적고,[^home] 연구 페이지는 이더리움 같은 계정 기반 블록체인의 확장성·동기화 부담과 온체인·오프체인 환경의 보안·프라이버시를 연구 대상으로 든다.[^bc] AI4Code 연구는 프로그래밍 관련 응용에서 코드 생성 성능과 언어 모델의 신뢰성을 높이는 것을 목표로 한다.[^ai] 대표 논문은 PC나 스마트폰을 쓰는 일반 사용자가 이더리움 풀 노드로 참여하는 일,[^p2] 이더리움 스마트 계약의 취약점 탐지,[^p3] 신뢰 실행 환경을 쓴 블록체인 밖 결제,[^p4] 자원이 적은 경량 클라이언트의 블록 검증,[^p1] 계산·통신 자원이 서로 다른 기기들이 함께 하는 연합학습,[^p5] 메모리 칩 시험 장비 프로그램의 컴파일[^p8]을 대상으로 한다. 학과 연구실 소개는 장비마다 다른 패턴 프로그램을 자동으로 번역하면 여러 시험 장비를 함께 써서 테스트의 생산성을 높일 수 있다고 적고, 연구실이 IBM, SUN, INTEL, HP, 삼성전자, LG전자 같은 기업과 많은 연구개발 과제를 해 왔다고 적는다.[^ecelabd] 랩 News 페이지의 해커톤 수상 작품에는 온체인 결제를 위한 AI 보안 계층(Aegis402), 블록체인 기반 AI 프롬프트 시장(Capture the Prompt), 영지식 가상머신(Tabula), 영지식 증명을 쓴 온체인 게임(zkDungeon)이 있다.[^news] 졸업생의 진로로는 삼성전자(System LSI, Samsung Research, 메모리사업부 등), 네이버, SAP 코리아, SK 텔레콤 Network 기술연구원, 국방과학연구소, Google, Amazon, Intel, AMD, Grammarly, 경희대학교·전북대학교·성균관대학교·경기과학기술대학교 교수, Superblock·AIM Intelligence·팅크웨어의 CEO 등이 있다.[^alumni]

## 구성원

2026년 10월 23일 랩 Students 페이지 기준이다. PostDoctoral Researchers 칸 1명, PhD Students 칸 12명, MS Students 칸 5명이며, 과정은 칸 이름을 옮겼고 연구 주제는 카드에 적힌 분야다.[^students] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. 석사과정 Minsu Kim은 졸업생 명단의 박사 졸업생 김민수(Minsu Kim)와 이름이 같고 대표 논문 8의 저자 Minsu Kim이 어느 사람인지 가릴 수 없어, 그 행에는 참여 번호를 붙이지 않았다.[^alumni]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Junmo Lee | 박사후연구원 | Blockchain | 1, 2, 3, 4 |
| Jong-gen Park | 박사과정 | Web Engine & DSL Translator |  |
| KwangYong Shin | 박사과정 | Deep Learning |  |
| SangHyeon Park | 박사과정 | Blockchain & Federated Learning | 2, 4 |
| Jaehoon Kim | 박사과정 | Blockchain |  |
| Jiyong Youn | 박사과정 | Blockchain |  |
| MinJae Kim | 박사과정 | Federated Learning | 5 |
| Uisang Lee | 박사과정 | Machine Learning | 3 |
| Jinwoo Lim | 박사과정 | Federated Learning | 6, 7 |
| Juneyoung Park | 박사과정 | Compiler |  |
| Changhoon Chung | 박사과정 | GNN | 3 |
| Sanghyeon Lee | 박사과정 | Compiler |  |
| Wonjae Choi | 박사과정 | Blockchain |  |
| Donguk Ju | 석사과정 | Compiler |  |
| Minsu Kim | 석사과정 | Blockchain |  |
| Kunhwa Lee | 석사과정 | Federated Learning |  |
| Dongha Hwang | 석사과정 | Compiler |  |
| Seunghyeon Suh | 석사과정 | Federated Learning |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 박사 졸업생 18명과 석사 졸업생 45명이다. 이름은 랩이 적은 국문·영문 표기 그대로이고, 진로는 랩이 이름 뒤에 적은 곳이다. 졸업 연도는 적혀 있지 않다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 심상민 (SangMin Shim) | Ph.D. |  |
| 박진표 (Jinpyo Park) | Ph.D. | 삼성전자 (System LSI) |
| 김수현 (Suhyun Kim) | Ph.D. | 경희대학교 교수, (전) KIST, (전) IBM TJ Watson |
| 이승일 (SeungIl Lee) | Ph.D. | Grammarly, San Francisco, USA |
| 이제형 (Je-Hyung Lee) | Ph.D. | 삼성전자 (System LSI) |
| 정동헌 (Dong-Heon Jung) | Ph.D. | 삼성전자 (Samsung Research) |
| 최형규 (Hyung-Kyu Choi) | Ph.D. | dsrvlabs |
| 홍성현 (Sunghyun Hong) | Ph.D. | 삼성전자 (System LSI) |
| 이성원 (SeongWon Lee) | Ph.D. | 네이버 |
| 오형석 (HyungSeok Oh) | Ph.D. | 삼성전자 (Samsung Research) |
| 오진석 (JinSeok Oh) | Ph.D. | 삼성전자 (반도체연구소) |
| 양병선 (Byung-Sun Yang) | Ph.D. | Amazon, Seattle, USA |
| 박혁우 (HyukWoo Park) | Ph.D. | 전북대학교 교수, (전) 삼성리서치 |
| 권진우 (JinWoo Kwon) | Ph.D. | 삼성전자 (VD) |
| 여지환 (JiHwan Yeo) | Ph.D. | 삼성리서치 (Samsung Research) |
| 정혁진 (Hyuk-jin Jeong) | Ph.D. | AMD, San Jose |
| 김민수 (Minsu Kim) | Ph.D. | 삼성전자 생산기술연구소 |
| 김재윤 (Jae-Yun Kim) | Ph.D. | Superblock CEO |
| 박성배 (Seongbae Park) | M.S. | Google, Mountain View, USA |
| 안재우 (Jaewoo Ahn) | M.S. | 경기과학기술대학교 교수 |
| 홍승표 (Seungpyo Hong) | M.S. | SK 텔레콤 Network 기술연구원 |
| 임찬식 (Chansik Im) | M.S. | Intel, Oregon, USA |
| 윤한샘 (Han-Saem Yun) | M.S. | 국방과학연구소 |
| 이흥복 (HeungBok Lee) | M.S. | 팅크웨어 CEO |
| 정유철 (Yoo C. Chung) | M.S. | Google, New York, USA |
| 정홍집 (HongJip Jung) | M.S. | 삼성전자 (System LSI) |
| 문민수 (Minsoo Moon) | M.S. | 삼성전자 (메모리사업부) |
| 정회목 (HoeMok Chung) | M.S. | 가산종합법률사무소 |
| 이준표 (Junpyo Lee) | M.S. | 팅크웨어 이사 |
| 이재목 (Jae-mok Lee) | M.S. |  |
| 이하영 (Lee Ha Young) | M.S. | 유비벨록스㈜ |
| 김정래 (Kim Jungrae) | M.S. | 성균관대학교 교수, 전 (Microsoft, 시애틀, 미국) |
| 황성욱 (Sunguk Hwang) | M.S. |  |
| 이상규 (SangGyu Lee) | M.S. | 삼성전자 (Samsung Research) |
| 유준민 (JunMin Yu) | M.S. | 유비벨록스㈜ |
| 최선일 (Sunil Choi) | M.S. | 삼성전자 (VD 사업부) |
| 배성환 (Sung-Hwan Bae) | M.S. | 삼성전자 (메모리사업부) |
| 박종국 (JongKuk Park) | M.S. | 새마을금고연합회, (전)NHN |
| 김진철 (JinChul Kim) | M.S. | SAP R&D Center Korea |
| 김성무 (SungMoo Kim) | M.S. | SK 텔레콤 Network 기술연구원 |
| 김익현 (IkHyun Kim) | M.S. | 삼성전자 (무선사업부) |
| 이석영 (Seok-Young Lee) | M.S. | 변호사 법무법인 다래 |
| 김재진 (Jae-Jin Kim) | M.S. | 삼성전자 (무선사업부) |
| 김범준 (Beom-Jun Kim) | M.S. | SAP코리아 |
| 유영호 (Young-Ho You) | M.S. | SAP코리아 |
| 심명보 (Myung-Bo Shim) | M.S. | SAP코리아 |
| 정은지 (EunJi Jeong) | M.S. | 삼성전자 (Samsung Research) |
| 김선규 (Seon-Kyu Kim) | M.S. | 성균관대학교 의과대학 |
| 정원기 (Won-Ki Jung) | M.S. | NHN엔터테인먼트 |
| 김영완 (Youngwan Kim) | M.S. | 삼성전자 (System LSI) |
| 차명수 (Myung-su Cha) | M.S. | 삼성전자 (System LSI) |
| 정인창 (In-Chang Jung) | M.S. | 네이버 |
| 김성국 (Seong-guk Kim) | M.S. | UC Davis |
| 이현재 (HyeonJae Lee) | M.S. | SAP 코리아 |
| 신창현 (ChangHyun Shin) | M.S. | ㈜Lomin |
| 임재현 (JaeHyeon Rim) | M.S. | SAP 코리아 |
| 구연재 (YeonJae Koo) | M.S. | 넥슨코리아 |
| 유용환 (Yong-Hwan Yoo) | M.S. | 슈퍼브에이아이 |
| 조중하 (Joongha Cho) | M.S. | 삼성전자 (메모리) |
| 유상윤 (Sangyoon Yu) | M.S. | AIM Intelligence CEO |
| 김태훈 (Taehoon Kim) | M.S. | Kroma |
| 이준하 (Joonha Lee) | M.S. | SAP 코리아 |
| 김민석 (Miseok Kim) | M.S. | Superblock |

## 최근 논문 목록 (2021–2026)

랩 Publication 페이지 2021–2026년 연도 구역의 16편(2026년 3, 2025년 3, 2024년 3, 2023년 2, 2022년 2, 2021년 3)이다. 연도는 페이지의 연도 구역이고, 저자·제목·학회와 학술지 이름은 랩 표기 그대로다. 학회 이름 뒤의 (Oral), (Spotlight), (Distinguished Paper Award)도 랩이 덧붙인 표기다.[^pubs]

**2026**

- Junmo Lee, Jaehun Kim, Jiyong Youn, Soo-Mook Moon. "Ethane: Debloating State Data using Compact Trie for Account-based Blockchain". *Proceedings of the 21st European Conference on Computer Systems (EuroSys 2026)*.
- Sanghyeon Park, Soo-Mook Moon. "FRAIN to Train: A Fast-and-Reliable Solution for Decentralized Federated Learning". *The 41st ACM/SIGAPP Symposium On Applied Computing (SAC 2026)*.
- Uisang Lee, Changhoon Chung, Junmo Lee, Soo-Mook Moon. "BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks". *Proceedings of the AAAI conference on artificial intelligence (AAAI 2026). (Oral)*.

**2025**

- Jinwoo Lim, Suhyun Kim, Soo-Mook Moon. "Convergence Analysis of Federated Learning Methods Using Backward Error Analysis". *Proceedings of the AAAI conference on artificial intelligence (AAAI 2025)*.
- Sanghyeon Park, Jeong Hyuk Lee, Seunghwa Lee, Jung Hyun Chun, Hyeonmyeong Cho, MinGi Kim, Hyun Ki Cho, Soo-Mook Moon. "Beyond the Blockchain Address: Zero-Knowledge Address Abstraction". *The 40th ACM/SIGAPP Symposium On Applied Computing (SAC 2025)*.
- Jinwoo Lim, Suhyun Kim, Soo-Mook Moon. "Shortcut Features as Top Eigenfunctions of NTK: A Linear Neural Network Case and More". *39th Conference on Neural Information Processing Systems (NeurIPS 2025). (Spotlight)*.

**2024**

- Junmo Lee, Seongjun Kim, Sanghyeon Park, Soo-Mook Moon. "RouTEE: Secure, Scalable, and Efficient Off-Chain Payments using Trusted Execution Environments". *Proceedings of the 39th Annual Computer Security Applications Conference (ACSAC 2024)*.
- Jae-Yun Kim, Junmo Lee, Soo-Mook Moon. "Trie-Hashimoto: State Trie-Based Proof-of-Work Mining for Optimizing Blockchain Storage". *IEEE ACCESS, Vol. 12, 2024*.
- Sanghyeon Park, Junmo Lee, Soo-Mook Moon. "BRAIN: Blockchain-based Inference and Training Platform for Large-Scale Models". *IEEE ACCESS, Vol. 12, 2024*.

**2023**

- Minjae Kim, Sangyoon Yu, Suhyun Kim, Soo-Mook Moon. "DEPTHFL: DEPTHWISE FEDERATED LEARNING FOR HETEROGENEOUS CLIENTS". *The Eleventh International Conference on Learning Representations. 2023*.
- Jae-Yun Kim, Soo-Mook Moon. "Disclosure: Improving Performance and Security of Web App Migration in Liquid Computing". *Journal of Web Engineering (2023): 79-104*.

**2022**

- Minsu Kim, Jeong-Keun Park, Soo-Mook Moon. "Solving PBQP-based Register Allocation using Deep Reinforcement Learning". *2022 International Symposium on Code Generation and Optimization (CGO), April 2022*.
- Jae-Yun Kim, Soo-Mook Moon. "Disclosure: Efficient Instrumentation-based Web App Migration for Liquid Computing". *2022 International Conference on Web Engineering (ICWE), Jul 2022 (Distinguished Paper Award)*.

**2021**

- Minsu Kim, Jeong-Keun Park, Soo-Mook Moon. "Irregular Register Allocation for Translation of Test-pattern Programs". *ACM Transactions on Architecture and Code Optimization, Volume 18 , Issue 1. January 2021*.
- Jae-Yun Kim, Junmo Lee, Yeonjae Koo, Sanghyeon Park, Soo-Mook Moon. "Ethanos: Efficient Bootstrapping for Full Nodes on Account-based Blockchain". *2021 European Conference on Computer Systems (EuroSys 2021)*.
- Yong-Hwan Yoo, Soo-Mook Moon. "Snapshot-based Migration of ES6 JavaScript". *International Conference on Web Engineering. Springer, Cham, 2021*.

## 과제

교수 페이지 Current and Previous Industry Projects 칸의 11건이다. 과제 이름과 괄호 안의 기관은 랩 표기 그대로다. 칸 이름대로 지금 과제와 지난 과제가 함께 올라 있고, 과제마다 기간은 적혀 있지 않다.[^prof]

- LLVM-based Optimization of Mobile platform and GPUs (Samsung Electronics)
- LaTTe and VLaTTe: Optimized Java VM JIT compilers for RISCs and VLIWs (IBM T. J. Watson Research Center)
- Translation of DRAM Test-Pattern Programs for Automated Test Equipment (Samsung Electronics)
- Optimizations for Android Dalvik Virtual Machines for Multicores (Samsung Electronics)
- Instruction scheduling for In-Order Superscalar Processors (Sun Microsystems)
- Java Just-in-Time Compilation for Instruction-level Parallelism on EPIC Architectures (Intel)
- Enhanced Pipelinine Scheduling for EPIC Architectures (HP-Intel IPF University Grants Program)
- Enhanced Pipeline Scheduling for IPF with Cache Optimizations (Gelato at UIUC for HP)
- Just-in-Time Compilation for Mobile JavaScript Engines (Samsung Electronics)
- Java Optimization for Digital TVs and Blu-ray Disc Players (LG Electronics)
- Optimizing Compilers for CalmRISC 8/16/32-bit microcontrollers (Samsung Electronics)

## 수상

랩 News 페이지에 올라 있는 글 17건 가운데 게시일이 2021년 10월 22일–2026년 10월 22일인 6건이다. 여섯 건 모두 Award 분류의 해커톤 수상 글이다. 날짜는 글의 게시일이고, 제목과 본문의 수상자·작품 이름·대회 연월은 페이지 표기 그대로다.[^news]

- June 4, 2026 · 2026 ETHGlobal Open Agents Hackathon 우승 · 박상현 외 3명 / Aegis402: AI-powered security layer for safer onchain payments: pre-audits, post-audits, and escrow protection.
- June 4, 2026 · 2026 ETHGlobal Open Agents Hackathon 우승 · 박상현, 이준모 외 2명 / OpenDAIO: Decentralized AI Consensus for High-Stakes Review
- February 22, 2026 · 2026 이더리움 덴버 해커톤 우승 · ETH Denver BUIDLathon 2026 / 이더리움 덴버 해커톤 메인 트랙 우승: 최원재 / 2026년 2월 / Tabula: Zero-knowledge Virtual Machine for typed, tabular state transitions
- January 9, 2026 · 2025 Sui Walrus 해커톤 수상 · Sui Walrus Haulout Hackthon 2025 / Best Technical Implementation: 최원재 / zkDungeon: Verifiable and Scalable On-chain Game via Zero-Knowledge Proofs / 2025년 12월
- June 4, 2024 · 2024 ETHGlobal ETHOnline Hackathon 우승 · 박상현 외 2명 / Capture the Prompt: A blockchain-based AI Prompt Market via CTF
- December 6, 2022 · 2022 드림플러스 블록체인 해커톤 대상 · 글로벌 1등상 : 유상윤, 이준하 외 2명 / 2022년 11월 / Web3Mon: virtual state channel을 활용해 빠르고 안전한 Cross-Chain NFT 배들 게임

## 연락과 위치

- 연구실: (08826) 서울특별시 관악구 관악로1 서울대학교 공과대학 301동(제1공학관) 815호[^contact]
- 교수 연구실: 301동 801호[^eceprof]
- 전화: 교수 02-880-1814,[^prof][^eceprof] 연구실 02-883-8430[^ecelabd]
- 교수 이메일: smoon@snu.ac.kr[^apply]
[^home]: 연구실 누리집 첫 화면 <https://altair.snu.ac.kr/> (Welcome To VMOLAB, 연구실 소개와 현재 연구 주제, 2026-10-23 열람)
[^prof]: 교수 페이지 <https://altair.snu.ac.kr/smoon/> (Areas of Interests, Selected Publications over the Last 10 Years, Awards, Current and Previous Industry Projects, Biographical Sketch, 2026-10-23 열람)
[^bc]: Blockchain Research 페이지 <https://altair.snu.ac.kr/blockchain-research/> (State Optimization, Security and Privacy, 2026-10-23 열람)
[^ai]: AI Research 페이지 <https://altair.snu.ac.kr/ai-research/> (Federated Learning, Graph Neural Networks, Shortcut Learning, AI4Code, 2026-10-23 열람)
[^compiler]: Compiler Research 페이지 <https://altair.snu.ac.kr/compiler-research/> (Phase Ordering with ML, Optimizing Ahead-of-time and Just-in-time Compiler Structure, DSL Specialized Problem Solving, 2026-10-23 열람)
[^students]: Students 페이지 <https://altair.snu.ac.kr/students/> (PostDoctoral Researchers, PhD Students, MS Students 칸, 2026-10-23 열람)
[^alumni]: Alumni 페이지 <https://altair.snu.ac.kr/alumni/> (박사 졸업생, 석사 졸업생 칸, 2026-10-23 열람)
[^pubs]: Publication 페이지 <https://altair.snu.ac.kr/publication/> (2007–2026년 연도 구역과 Old papers 구역, 2026-10-23 열람)
[^news]: News 페이지 <https://altair.snu.ac.kr/tag/news/> 와 2쪽 <https://altair.snu.ac.kr/tag/news/page/2/>, 2021년 10월 이후 게시 글 6쪽(주소 목록은 근거 페이지) (2026-10-23 열람)
[^apply]: Apply 페이지 <https://altair.snu.ac.kr/apply/> (지원 안내, 2026-10-23 열람)
[^contact]: Contact 페이지 <https://altair.snu.ac.kr/contact/> (ADDRESS, 2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-23 열람)
[^ecelabd]: 서울대학교 전기·정보공학부 연구실 소개(가상머신 및 최적화 연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=34> (연구 분야, 연락처, 연구실 소개 및 연구분야, 주요 연구과제, 2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 소개(문수묵) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p012> (학위, 전공, 분야, 학력, 주요경력, Research Interest, 연락처, 2026-10-23 열람)
[^p1]: J.-Y. Kim, J. Lee, S.-M. Moon, IEEE Access 12, 18315-18329 (2024). <https://doi.org/10.1109/access.2024.3360379> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J.-Y. Kim 외, S.-M. Moon, Proceedings of the Sixteenth European Conference on Computer Systems, 99-113 (온라인 2021-04-21). <https://doi.org/10.1145/3447786.3456231> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: U. Lee, C. Chung, J. Lee, S.-M. Moon, Proceedings of the AAAI Conference on Artificial Intelligence 40, 570-578 (온라인 2026-03-14). <https://doi.org/10.1609/aaai.v40i1.37021> 초록 기준.
[^p4]: J. Lee, S. Kim, S. Park, S.-M. Moon, 2024 Annual Computer Security Applications Conference (ACSAC), 456-472 (2024). <https://doi.org/10.1109/acsac63791.2024.00048> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: M. Kim, S. Yu, S. Kim, S.-M. Moon, The Eleventh International Conference on Learning Representations (ICLR 2023). <https://openreview.net/forum?id=pf8RIZTMU58> 초록 기준(OpenReview 게시 초록).
[^p6]: J. Lim, S. Kim, S.-M. Moon, Proceedings of the AAAI Conference on Artificial Intelligence 39, 18719-18727 (온라인 2025-04-11). <https://doi.org/10.1609/aaai.v39i18.34060> 초록 기준.
[^p7]: J. Lim, S. Kim, S.-M. Moon, Advances in Neural Information Processing Systems 38, 104430-104458 (2025). <https://doi.org/10.52202/085713-3149> 초록 기준(OpenReview 게시 초록).
[^p8]: M. Kim, J.-K. Park, S.-M. Moon, 2022 IEEE/ACM International Symposium on Code Generation and Optimization (CGO), 1-12 (2022). <https://doi.org/10.1109/cgo53902.2022.9741272> 초록 기준(Semantic Scholar 등록 초록).

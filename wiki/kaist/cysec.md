# 사이버 보안 시스템 연구실 (Cyber Security Systems Research Lab, CySec Lab)

**KAIST 전산학부·정보보호대학원 · 강병훈 교수**

- 분야: 시스템 보안(운영체제 커널 무결성 감시, 하드웨어 기반 신뢰 실행 환경, 커널·프로세스 안의 권한 분리와 메모리 보호), 악성코드 분석과 방어, 인공지능 시스템의 보안, 네트워크 프로토콜과 블록체인 네트워크의 보호
- 대분야: 컴퓨팅·AI
- 태그: 소프트웨어·시스템 보안[^cslab][^p4][^p6], 하드웨어 보안[^intro][^p1][^p3], 네트워크 보안·프라이버시[^dialect][^p2], 컴퓨터 구조·운영체제[^p1][^p4]
- 홈페이지: <https://cysec.kr/>
- 근거와 출처: [CySec Lab 근거 페이지](cysec-sources.md)

> 보안에 취약할 수밖에 없는 기존 컴퓨팅 시스템이 현재와 미래의 사이버 위협에도 보안성과 안정성을 갖추게 하는 시스템 설계와 방어 기술을 연구하는 연구실로, 최근에는 컴퓨팅 시스템에 대한 보안 위협을 독립된 신뢰 실행 환경으로 막는 연구를 주로 한다.[^intro]

## 무엇을 연구하나

연구실은 KAIST 전산학부 강병훈 교수가 이끄는 연구실이다.[^intro][^cslab] 누리집은 연구실 이름을 Cyber Security Systems Research Lab으로 적고, 소식 글에서는 CySecLab으로 부른다.[^home] 교수 소개 페이지는 연구실을 사이버 시스템 보안 연구실 CysecLab(Cyber Systems Security Lab)으로,[^intro] 전산학부 연구실 소개는 「사이버 보안 시스템 연구실」로,[^cslab] 정보보호대학원 연구실 목록은 Cyber system Security (CySec) Lab으로 적는다.[^gsislab] 정보보호대학원 교수진 목록은 교수의 소속을 전산학부와 정보보호대학원으로 적는다.[^gsisfac]

교수 소개 페이지는 연구실이 보안에 취약할 수밖에 없는 기존 컴퓨팅 시스템이 현재와 미래의 사이버 위협에도 보안성과 안정성을 확보하게 하는 시스템 설계와 방어 기술 연구를 목표로 하며, 최근에는 갈수록 커지는 컴퓨팅 시스템의 보안 위협을 독립된 신뢰 실행 환경(TEE, Trusted Execution Environment, 하드웨어의 도움으로 일반 운영체제와 격리된 실행 구역을 만들어 그 안의 코드와 데이터의 기밀성과 무결성을 지키는 환경)으로 막는 연구를 주로 한다고 적는다.[^intro] 주 연구 분야는 TEE 설계와 이를 이용한 안전한 호스트 시스템 설계이고, 그 예로 운영체제 커널(하드웨어 자원을 관리하고 응용 프로그램이 그 자원을 쓰도록 중개하는 운영체제의 핵심 부분) 무결성 모니터, 하드웨어 기반 신뢰 실행 환경, 메모리 주소 변환 무결성, 코드 재사용 공격(새 코드를 넣지 않고 프로그램에 이미 있는 코드를 다시 써서 공격자가 원하는 동작을 실행하게 만드는 공격) 방어를 든다.[^intro] 같은 페이지의 영문 소개는 연구 관심사에 힙 메모리 방어와 악성코드 분석도 넣는다.[^intro]

전산학부 연구실 소개는 연구실이 공격 기법과 기존 시스템의 취약점을 분석해 공격으로부터 안전한 컴퓨터 시스템을 연구한다고 적는다. 운영체제와 네트워크에 대한 이해를 바탕으로 현재 문제가 되는 사이버 공격을 근원적으로 막거나 탐지하고, 특정 대상을 겨냥한 고도화된 은닉 공격으로부터 컴퓨터 시스템을 보호하는 방법을 연구하며, 주요 연구 주제로 Trusted Execution Environment, TEE를 사물인터넷 기기에 응용하는 연구(TEE-based Applications to IoT Devices), UAV(무인 항공기) 시스템을 든다.[^cslab] 정보보호대학원 연구실 목록은 연구 분야를 System security, Malware analysis and defense, Anti-spam으로 적고, 악성코드에 감염됐을 때 생기는 여러 현상을 분석해 미리 탐지하는 악성코드 행위 분석, 운영체제에 대한 이해를 바탕으로 하드웨어·가상화 시스템을 써서 운영체제의 신뢰성을 보장하는 시스템 보안, 안드로이드 시스템에 여러 보안 정책을 적용하는 실용 플랫폼을 다루는 모바일 보안을 소개한다.[^gsislab] 정보보호대학원 교수진 목록은 교수의 연구 분야를 「시스템 보안, 신뢰가능 AI 시스템, 넷트워크 분산 시스템, 블록체인, 악성코드방어」로 적는다.[^gsisfac]

첫째 갈래는 **하드웨어와 신뢰 실행 환경으로 지키는 시스템**이다. 전산학부 연구실 소개는 커널 무결성 감시(kernel integrity monitoring) 도구 Vigilare와 KI-Mon, ATRA, SeCReT, Hacking in Darkness를 연구실의 대표 성과로 들고,[^cslab] 누리집 첫 화면 소식은 KI-MON과 VIGILARE를 운영체제 루트킷(공격자가 시스템에 몰래 머물며 높은 권한을 유지하도록 자신과 다른 악성 활동을 숨기는 악성 소프트웨어) 공격을 막도록 설계한 하드웨어 기반 보안 모니터로 소개한다.[^home] 대표 논문에서는 CPU 주 코어 가까이에 분할된 보안 감시 하드웨어를 두어, TEE 같은 특권 소프트웨어(높은 실행 권한으로 시스템을 관리하는 소프트웨어)를 노리는 공격을 감시하고 제때 막는 Interstellar를 제안했다.[^p1] 클라우드 VPN(가상 사설망, 공용망 위에 가상의 통로를 만들어 떨어진 네트워크나 기기를 하나의 사설망으로 잇는 기술)의 IPsec 게이트웨이(IP 통신을 암호화·인증하는 표준 규약 IPsec으로 네트워크 사이의 통신을 보호하는 관문 장치)를 SGX(프로세서가 엔클레이브라는 격리된 메모리 구역을 만들어 그 안의 코드와 데이터를 다른 소프트웨어의 접근에서 지키는 하드웨어 보안 기능)로 보호하면서 격리 메모리를 아껴 쓰는 EnclaveVPN도 만들었다.[^p2] 또 ARM 프로세서의 TrustZone으로 만든 TEE 안에서 제3자 사물인터넷 서비스 업체가 자기 커널 드라이버(운영체제 커널 안에서 장치나 기능을 다루는 프로그램)를 기존 TEE의 보안을 해치지 않고 실행하게 하는 3rdParTEE를 내놓았다.[^p3] 누리집 첫 화면 소식(날짜 표기 없음)은 연구팀이 ARM CCA 기반 기밀 컴퓨팅(confidential computing, 처리 중인 데이터를 하드웨어 기반 신뢰 실행 환경 안에서 계산해 보호하는 기술) 플랫폼 Islet에 기여한다고 알린다.[^home] 최근 논문 목록에는 상용 PIM(Processing-In-Memory, 메모리 안에서 계산하는 하드웨어)에 ORAM(Oblivious RAM, 프로그램이 메모리의 어느 곳에 접근하는지 겉으로 드러나지 않게 접근 패턴을 감추는 기법) 기본 기능을 넣는 것을 제목에 단 ACSAC 2025 논문(PIM-ORAM)과, 분리형 구조(disaggregated architecture, 프로세서·메모리 같은 자원을 한 서버에 묶지 않고 따로 두어 네트워크로 이어 쓰는 컴퓨터 구조)를 위한 확장·설정 가능한 시뮬레이션을 제목에 단 SIMPAT 2023 논문도 있다.[^pubs]

둘째 갈래는 **운영체제·프로세스 안의 격리와 메모리 보호**다. 정보보호대학원 연구실 목록은 운영체제에 대한 이해를 바탕으로 하드웨어·가상화 시스템을 써서 운영체제의 신뢰성을 보장하는 연구를 소개하고,[^gsislab] 교수 소개 페이지는 연구 관심사에 코드 재사용 공격 방어와 힙 메모리 방어를 넣는다.[^intro] 대표 논문에서는 커널 안을 권한이 다른 구역으로 나누는 권한 분리(privilege separation, 시스템을 권한이 다른 부분으로 나눠 한 부분이 뚫려도 다른 부분의 자원에 접근하지 못하게 하는 설계)를 특정 프로세서 구조에 묶이지 않게, 오늘날 프로세서에 흔한 하드웨어 보안 기능만으로 구현한 Genesis를 제안했다.[^p4] x86 프로세서에서 잘 쓰이지 않는 중간 특권 수준을 활용해 응용 프로그램 안에 비밀을 지키는 더 높은 권한의 사용자 실행 층을 만든 LOTRx86과,[^p5] 스택(함수가 실행되는 동안 지역 변수와 돌아갈 주소 등을 쌓아 두는 메모리 영역)의 배치를 무작위로 바꿔 메모리 오류가 악용될 가능성을 줄이는 SaVioR도 만들었다.[^p6] 최근 논문 목록에는 ARM Cortex-M 프로세서에서 섀도 스택(함수가 돌아갈 주소를 따로 보관해 두고 함수가 끝날 때 대조해 변조를 막는 기법)을 효율적으로 보호하는 것을 제목에 단 Computers & Security 2023 논문(SuM), 컨테이너(응용 프로그램과 실행에 필요한 파일을 묶어 호스트 운영체제 커널을 함께 쓰면서 다른 프로그램과 격리해 실행하는 단위)의 공격 표면을 줄이는 동적 시스템 호출(응용 프로그램이 운영체제 커널에 기능 수행을 요청하는 방법) 필터링을 제목에 단 Journal of Cloud Computing 2024 논문(Optimus), ARM에서 프로세서 내부 구조의 특성으로 에뮬레이션(어떤 컴퓨터 시스템의 동작을 다른 시스템 위에서 재현해 실행하는 일) 여부를 탐지하는 것을 제목에 단 Computers & Security 2021 논문(EmuID)도 있다.[^pubs]

셋째 갈래는 **인공지능 시스템의 보안**이다. 정보보호대학원 교수진 목록은 교수의 연구 분야에 신뢰가능 AI 시스템을 넣는다.[^gsisfac] 대표 논문에서는 스파이킹 신경망(SNN, 뉴런들이 시간에 따라 일어나는 스파이크라는 펄스 신호로 정보를 주고받는 신경망)을 겨냥한 적대적 공격(모델이 틀린 답을 내도록 입력에 의도적인 변화를 더하는 공격)이 여러 시간 단계를 처리하느라 오래 걸리는 문제를 SNN의 성질을 이용해 줄인 TCA를 제안했다.[^p7] 다중 객체 추적(영상 속 여러 물체를 찾아 프레임마다 같은 물체끼리 이어 각 물체의 이동 궤적을 만드는 기술) 시스템이 물체 위치를 바꾸지 않아도 물체의 신원을 계속 뒤바꾸게 하는 적대적 공격 BankTweak도 내놓았다.[^p8] 최근 논문 목록에는 실시간 물체 검출 모델을 제목에 단 RTSS 2025 논문(CF-DETR)과 실시간 다중 객체 검출을 위한 적응형 스파이킹 신경망을 제목에 단 DAC 2026 논문도 있다.[^pubs]

넷째 갈래는 **네트워크 프로토콜과 블록체인 네트워크의 보호**다. 교수가 보안뉴스에 쓴 기술 칼럼(2022-10-12 등록)은 「네트워크 시스템 보안을 위한 프로토콜 다이얼렉트」 기술을 소개한다. 칼럼에 따르면 이 기술은 클라이언트가 서버에 보내는 첫 요청 메시지에 특별한 요구사항을 두어, 네트워크 프로토콜(컴퓨터끼리 통신할 때 따르는 규약)의 첫 메시지만으로 공격자를 포함한 비인가 사용자를 처음부터 가려낸다. 요구사항은 암호학적 방법으로 만든 값에서 유도하고, 기존 프로토콜의 필드를 분석해 통신 당사자 사이의 인증 정보를 넣을 수 있는 영역을 찾아 쓰므로 기존 프로토콜과 호환되고 새 프로토콜을 배포할 필요가 없다. 인증 정보는 한 번만 쓰이게 만들어, 도청해 저장한 트래픽을 다시 보내는 재생 공격(replay attack)도 막는다.[^dialect] 칼럼은 이 기술을 OpenSSL에 적용해 시험한 결과 공격자가 서버와 계속 통신해야 하는 공격이 막히고 공격자가 서버 소프트웨어와 상호작용할 수 있는 범위가 줄었으며, 시제품은 TLS(HTTPS의 기반)와 IKEv2(IPSec VPN에 사용됨)를 대상으로 만들고 있다고 적는다.[^dialect] 누리집 첫 화면 소식(날짜 표기 없음)도 이 기술의 언론 소개를 알린다.[^home] 최근 논문 목록에는 비트코인 작업증명(proof-of-work, 계산 작업을 들여 정해진 조건을 만족하는 값을 찾았음을 증명한 참여자가 새 거래 기록 묶음을 덧붙이게 하는 합의 방식) 블록체인 네트워크를 겨냥한 분할 공격(partitioning attack, 네트워크의 참여자들을 서로 연결이 끊긴 무리로 나누는 공격)의 탐지 방법을 제목에 단 JIPS 2026 논문(HEMERA)도 있다.[^pubs]

## 주요 연구 주제

### 1. 하드웨어와 신뢰 실행 환경으로 지키는 시스템

특권 소프트웨어를 노리는 공격을 막는 프로세서 옆 보안 감시 하드웨어(Interstellar), SGX로 보호한 클라우드 VPN 게이트웨이(EnclaveVPN), TrustZone으로 만든 TEE에서 제3자 사물인터넷 서비스의 커널 드라이버 실행(3rdParTEE).[^p1][^p2][^p3] 누리집 소식은 기밀 컴퓨팅 플랫폼 Islet 기여를 알린다.[^home]

### 2. 운영체제·프로세스 안의 격리와 메모리 보호

특정 구조에 묶이지 않는 커널 내부 권한 분리(Genesis), x86 중간 특권 수준을 쓴 프로세스 안 비밀 보호(LOTRx86), 스택 배치 무작위화(SaVioR).[^p4][^p5][^p6]

### 3. 인공지능 시스템의 보안

스파이킹 신경망에 대한 적대적 공격의 지연 줄이기(TCA), 다중 객체 추적 시스템을 겨냥한 적대적 공격(BankTweak).[^p7][^p8]

### 4. 네트워크 프로토콜과 블록체인 네트워크의 보호

첫 요청 메시지로 비인가 사용자를 가려내는 프로토콜 다이얼렉트 기술,[^dialect] 비트코인 작업증명 블록체인 네트워크에 대한 분할 공격 탐지(HEMERA).[^pubs]

## 대표 논문

누리집 논문 목록의 2021–2026년 논문 가운데 강병훈 교수가 저자인 학술지·학회 논문을 앞의 세 연구 갈래에 고르게 담도록 골랐고, 교수가 마지막 저자인 논문을 우선했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2024 | [Interstellar: Fully Partitioned and Efficient Security Monitoring Hardware Near a Processor Core for Protecting Systems against Attacks on Privileged Software](https://doi.org/10.1145/3658644.3690247) · Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security | 프로그램이 실행한 명령어의 기록(명령어 추적)을 살펴 공격을 찾는 기존 보안 감시 하드웨어는 특권 소프트웨어에 기대고 있어, 특권 소프트웨어 자체를 노리는 공격을 막기 어렵다. 이를 풀려고 CPU의 주 코어 가까이에 분할된 하드웨어를 두어 하드웨어 수준에서 보안을 감시하는 Interstellar를 제안했다. Interstellar는 완전히 분할되고 병렬로 동작하며 동시에 탐지하는 보안 감시 하드웨어다. 악성 소프트웨어가 Interstellar의 탐지 방식을 거꾸로 알아내기 어렵게 설계했고, 신뢰 실행 환경(TEE) 같은 특권 소프트웨어를 노리는 공격으로부터 시스템을 효율적으로 지킨다. 유한 상태 기계(정해진 여러 상태 가운데 하나에 있다가 입력에 따라 다른 상태로 옮겨 가는 계산 모형)로 설계해, CPU 코어를 멈추지 않고 여러 공격을 감시할 뿐 아니라 제때 막는다.[^p1] | 1저자 YongHo Song, 마지막 저자 강병훈 |
| 2 | 2023 | [EnclaveVPN: Toward Optimized Utilization of Enclave Page Cache and Practical Performance of Data Plane for Security-Enhanced Cloud VPN](https://doi.org/10.1145/3607199.3607210) · Proceedings of the 26th International Symposium on Research in Attacks, Intrusions and Defenses | 클라우드 VPN은 클라우드를 빌려 쓰는 이용자가 자기 사내망을 클라우드 네트워크와 잇는 데 꼭 필요한 기반 시설이지만, 이용자들은 키 유출, 사칭, 패킷 엿보기 같은 보안 걱정 때문에 도입을 꺼린다. SGX는 격리된 메모리(엔클레이브 페이지 캐시, EPC) 안에 엔클레이브를 만들어 보안에 민감한 코드와 데이터를 악의적 접근에서 지킬 수 있어 이 문제를 풀 후보다. 이 논문은 SGX로 보안을 강화한 IPsec 게이트웨이 EnclaveVPN을 제안했다. 엔클레이브 안에서 암호 키를 관리하고 암호 연산을 실행하며, 클라우드 네트워크 안과 그 안팎으로 암호화된 패킷만 오가게 하고, EPC 사용을 최적화하고 데이터 평면(패킷을 실제로 받아 처리하고 전달하는 부분)의 부담을 줄이는 기능을 갖췄다. 실제 SGX v1.0 장비에 시제품을 구현하고 실험과 벤치마크로 EPC를 절약하는 정도와, SGX를 쓰지 않는 IPsec 게이트웨이에 견준 데이터 평면 성능을 보고했다.[^p2] | 1저자 Jaemin Park, 마지막 저자 강병훈 |
| 3 | 2022 | [3rdParTEE: Securing Third-Party IoT Services Using the Trusted Execution Environment](https://doi.org/10.1109/jiot.2022.3152555) · IEEE Internet of Things Journal | 사물인터넷(IoT) 기기가 늘며 스마트 그리드 같은 여러 서비스가 가능해졌지만 공격자도 몰린다. TrustZone 기술로 만들 수 있는 TEE는 IoT 기기의 중요한 동작과 민감한 데이터를 지키는 유망한 수단이다. 그러나 TrustZone은 마이크로컨트롤러부터 고성능 스마트 기기까지 대부분의 ARM 구조 기기에 있는데도, TEE의 보안을 지키려고 TEE 플랫폼 업체가 TEE를 관리하기 때문에 접근이 제한되어 제3자 IoT 서비스 업체에는 널리 쓰이지 못했다. 제3자가 TEE에 신뢰 서비스를 올리려면 엄격한 정책과 절차를 따라야 해 IoT 서비스의 빠른 개발과 배포가 어렵다. 3rdParTEE는 제3자 IoT 서비스 업체가 TEE 관리자에게 덜 기대고 자기 신뢰 서비스를 바로 실행할 수 있게 한다. 구체적으로는 기존 TEE 구성 요소의 보안을 해치지 않으면서 제3자의 커널 드라이버를 TEE 안에서 안전하게 실행하게 한다. IoT 서비스 플랫폼 유지에 쓰는 커널 드라이버 세 개(예: 커널 무결성 검사)를 TEE에서 실행해 효과를 보였고, 이렇게 안전하게 실행할 때 성능 부담은 최대 7%로 적정한 수준이었다.[^p3] | 1저자 Jinsoo Jang, 마지막 저자 강병훈 |
| 4 | 2024 | [GENESIS: A Generalizable, Efficient, and Secure Intra-kernel Privilege Separation](https://doi.org/10.1145/3605098.3635951) · Proceedings of the 39th ACM/SIGAPP Symposium on Applied Computing | 운영체제 커널의 신뢰성을 지키는 일은 시스템의 어떤 보안 목표에도 꼭 필요하다. 그러나 흔히 쓰는 커널은 대부분 모놀리식(커널의 모든 기능이 같은 권한으로 하나의 주소 공간에서 실행되는 구조)이고 자주 바뀌어 새 소프트웨어 버그가 들어갈 수 있다. 같은 권한과 하나의 주소 공간 때문에 공격자는 어떤 취약점이든 시스템 전체가 무너지는 단일 실패 지점으로 바꿀 수 있다. 그래서 커널 안에서 권한을 나누는 여러 격리 설계가 나왔지만, 대상 구조의 특정 기능에 기대어 그 구조에 묶이는 경우가 많다. Genesis는 특정 구조에 묶이지 않는 커널 내부 권한 분리 설계로, 오늘날의 프로세서 구조에 사실상 표준으로 있는 하드웨어 보안 기능만으로 스스로를 보호하는 실행 환경을 만든다. 그래서 큰 재설계 없이 다른 구조에도 적용할 수 있다. 시제품은 x86-64의 SMAP(supervisor-mode access prevention, 커널 권한으로 실행되는 코드가 사용자 영역 메모리에 접근하지 못하게 막는 프로세서 기능) 같은 일반 하드웨어 기능 위에 커널 권한 낮추기(kernel deprivileging)와 안전한 도메인 전환(secure domain switching)이라는 두 기법을 구현했다. 일반화 가능성을 유지하면서 표준 벤치마크와 Nginx·Memcached 같은 실제 응용에서 중간 정도의 성능 부담을 보였다.[^p4] | 1저자 Seongman Lee, 마지막 저자 강병훈 |
| 5 | 2023 | [Harnessing the x86 Intermediate Rings for Intra-Process Isolation](https://doi.org/10.1109/tdsc.2022.3192524) · IEEE Transactions on Dependable and Secure Computing | 오늘날 응용 프로그램은 민감한 정보를 자주 다루지만, 사용자 공간(일반 응용 프로그램이 실행되는 권한 영역) 안에 권한 분리가 없어 암호 키 같은 비밀도 평범한 문자열과 똑같이 보호받지 못한다. 새 하드웨어 보안 기능이 나오고 있지만 특정 제조사에만 있거나 이전 세대 프로세서와 호환되지 않아, 개발자에게는 민감한 부분을 보호할 이식 가능한 방법이 없다. 이 논문은 사용자 공간 권한 분리를 위한 이식 가능한 방법 LOTRx86을 제안했다. x86 구조에서 잘 쓰이지 않는 중간 특권 수준을 활용해 일반 사용자 모드보다 높은 권한의 사용자 실행 층 PrivUser를 만든다. PrivUser 메모리 공간(프로세스 주소 공간 안에서 사용자 모드가 접근하지 못하는 페이지들)은 응용 프로그램의 비밀과 그 비밀을 다루는 루틴을 두는 안전한 장소가 된다. 사용자가 PrivUser의 비밀 처리 루틴을 부르는 privcall 인터페이스를 구현해, 비밀이 관련된 민감한 작업이 엄격히 통제된 방식으로 실행되게 했다. 메모리 접근 통제가 권한에 기반하므로 보호된 비밀에 접근할 때 권한만 바꾸면 되고, 비용이 큰 원격 프로시저 호출이나 주소 공간 변경이 필요 없다. SSL 연결 중 자기 개인 키에 안전하게 접근하는 LOTRx86 적용 웹 서버를 개념 증명으로 만들어 Intel과 AMD PC에서 성능을 쟀고, 성능 부담이 제한적임을 확인했다.[^p5] | 1저자 Hojoon Lee, 마지막 저자 강병훈 |
| 6 | 2022 | [SaVioR: Thwarting Stack-Based Memory Safety Violations by Randomizing Stack Layout](https://doi.org/10.1109/tdsc.2021.3063843) · IEEE Transactions on Dependable and Secure Computing | 스택의 메모리 손상 취약점은 공격자가 임의 코드를 실행하고 임의 메모리를 읽고 쓰는 데 악용되어 왔다. 스택의 메모리 오류를 막는 기존 방법은 공간적 공격(할당된 범위 밖의 메모리에 접근하는 오류를 노리는 공격)과 시간적 공격(유효 기간이 끝난 메모리에 접근하는 오류를 노리는 공격) 가운데 한 종류만 막거나 성능을 크게 떨어뜨렸다. SaVioR는 스택의 배치를 무작위로 바꿔 예측과 악용을 어렵게 하는 효율적이고 포괄적인 스택 보호 방법이다. 각 객체를 공간적·시간적으로 이웃한 취약한 객체와 떼어 놓고 객체마다 위치를 무작위로 정해, 공격자가 스택 배치를 예측하지 못하게 하고 메모리 오류가 악용될 가능성을 줄인다. LLVM 컴파일러 틀로 구현해 SPEC CPU2006 벤치마크와 실제 응용에 적용했다. 보안 평가에서 스택 배치의 무작위성이 높아 스택의 공간적·시간적 메모리 오류를 악용하는 공격의 성공 가능성이 줄었고, 성능 평가에서 SPEC CPU2006 기준 성능 부담은 14%로, 최신 스택 보호 방법과 비슷한 보안 수준을 유지하면서 그보다 성능이 나았다.[^p6] | 1저자 Seongman Lee, 마지막 저자 강병훈 |
| 7 | 2026 | [Timestep-Compressed Attack on Spiking Neural Networks Through Timestep-Level Backpropagation](https://doi.org/10.1609/aaai.v40i7.37479) · Proceedings of the AAAI Conference on Artificial Intelligence | 스파이킹 신경망(SNN)에 대한 최신 기울기 기반 적대적 공격은 대부분 기존 공격 틀을 확장한 것이라, 여러 시간 단계를 처리하느라 공격 지연이 커서 실시간 응용에는 쓰기 어렵다. 이런 비효율은 일반 인공 신경망의 방식을 그대로 확장해 SNN의 핵심 성질을 활용하지 못한 데서 온다. 이 논문은 공격 지연을 크게 줄이는 틀인 TCA(timestep compressed attack)를 제안했다. 첫째 구성 요소인 시간 단계 수준 역전파(TLBP)는 교란을 만드는 역전파에서 전체 시간 정보가 공격 성공에 결정적이지 않다는 발견에 기반해, 시간 단계마다 평가하고 일찍 멈출 수 있게 한다. 둘째 구성 요소인 적대적 막전위 재사용(A-MPR)은 처음 시간 단계들이 막전위를 쌓는 데 비효율적으로 쓰인다는 관찰에 기반해, 이 준비 구간을 미리 계산해 다시 쓴다. CIFAR-10/100과 CIFAR10-DVS 데이터셋에서 VGG-11·ResNet-17로 실험한 결과, 최신 방법과 비슷한 공격 성공률을 유지하면서 필요한 공격 지연을 화이트박스 설정(공격자가 모델 내부를 아는 경우)에서 최대 56.6%, 블랙박스 설정(모르는 경우)에서 최대 57.1% 줄였다.[^p7] | 1저자 Donghwa Kang, 마지막 저자 강병훈 |
| 8 | 2025 | [BankTweak: Adversarial Attack Against Multi-Object Trackers by Manipulating Feature Banks](https://doi.org/10.24963/ijcai.2025/206) · Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence | 오늘날 다중 객체 추적(MOT)은 주로 먼저 물체를 검출한 뒤 검출 결과를 이어 물체의 궤적을 만드는 방식(tracking-by-detection)에 기댄다. 기존 MOT 공격은 특정 프레임의 검출 품질만 떨어뜨려 효율이 낮았고, 최신 공격은 연결 단계에서 물체 위치를 조작해 공격이 끝난 뒤에도 물체의 신원(ID)이 계속 뒤바뀌게 했다. 이 논문은 그런 최신 공격이 연결 단계의 거리 관련 매개변수를 조정하는 것만으로 쉽게 무력화되어 강건하지 않다는 점을 밝혔다. 이를 넘으려고, 특징 기반 MOT 시스템을 겨냥해 물체 위치를 바꾸지 않고(강건성) 신원이 계속 뒤바뀌게 하는(효율성) 적대적 공격 BankTweak을 제안했다. BankTweak은 연결 단계에서 특징 저장소(feature bank)에 변형된 특징을 넣어 MOT 시스템의 짝 맞추기 알고리즘의 약점을 이용한다. 여러 검출기·특징 추출기·추적기를 조합해 MOT17과 MOT20 데이터셋에서 실험한 결과 최신 공격을 최대 11.8배 앞섰고, 검출 후 추적 방식의 근본적인 취약점을 드러냈다.[^p8] | 1저자 Woojin Shin, 교수는 6명 중 4번째 저자(마지막 저자 Hyeongboo Baek) |

## 교수와 전문 분야

강병훈 교수는 University of California at Berkeley에서 컴퓨터과학 박사, University of Maryland at College Park에서 석사, 서울대학교에서 학사 학위를 받았다.[^intro] 전산학부 교수 소개는 학위를 "Ph.D., University of California at Berkeley, 2004"로 적고, 누리집 논문 목록은 박사 논문을 「S2D2: A Framework for Scalable and Secure Optimistic Replication」(UC Berkeley, 2004)으로 적는다.[^csfac][^pubs] 교수 소개 페이지에 따르면 교수는 George Mason University Volgenau School of Engineering의 associate professor(부교수)를 지냈고, KAIST 전산학부 소속으로 정보보호대학원 책임교수(Chief Professor)를 역임했으며, 현재 전산학부 교수다.[^intro] 전산학부 교수 소개 글은 「2013년부터 카이스트 부교수로 재직 중」이라고 적고, 같은 페이지의 직위 칸과 정보보호대학원 교수진 목록, 누리집은 교수(Professor)로 적는다.[^csfac][^gsisfac][^home] 전산학부 교수 소개의 전공 칸은 「시스템 보안」이고, 연구분야 칸은 인공지능·정보서비스, 시큐어 컴퓨팅, 시스템·네트워크다.[^csfac]

학술 활동으로 교수 소개 페이지는 IEEE Security and Privacy, ACM CCS, USENIX SECURITY의 프로그램 위원회(Program Committee)와 ACM CCS의 Tutorial co-chair를 들고, 국문 소개는 IEEE Security and Privacy, ACM CCS, USENIX SECURITY, NDSS에서 프로그램 위원회 직책을 맡고 있다고 적는다.[^intro] 전산학부 교수 소개는 2011·2012년 ACM CCS Tutorial co-chair와 2015년 USENIX SECURITY, 2015년 ICDCS, 2015–2017년 ACM CCS, 2016–2018년 IEEE S&P의 프로그램 위원회를 적는다.[^csfac] 교수 소개 페이지는 교수가 NSF 지원을 받은 실습형 정보보증(Information Assurance) 교육 프로그램 시리즈를 만들었다고 적고, 연구 후원 기관으로 ONR, NRF, IARPA, ARO, NSF, ADD, ETRI, IITP(Brain Scouting Program), TIAA-CREF Faculty Fellowship, Bank of America, LG, SK Telecom, Samsung을 기간 표기 없이 든다.[^intro] 누리집 COURSE 칸은 IS632 Hypervisor System Security(봄), IS631 Kernel System Security(가을), IS511 Introduction to Information Security(봄), IS522 Intro to System Security(봄) 네 과목을 적는다. IS632는 하이퍼바이저(컴퓨터 하드웨어를 가상화해 여러 운영체제를 한 하드웨어 위에서 함께 실행하게 하는 소프트웨어 플랫폼)의 기초와 내부 동작을 새로운 보안·감시·분석 도구 설계의 관점에서 다루고, IS631은 리눅스 운영체제 커널의 원리와 동작을 보안 중심으로 가르쳐 운영체제를 장악·조작하는 루트킷 악성코드에 대한 분석 방법과 대응책을 익히게 한다고 적는다.[^home] 누리집 첫 화면 소식은 연구실이 교육용 시스템 취약점 악용(system exploitation) 문제를 제공하는 워게임 사이트 pwnable.kr의 서버를 운영하며, 이 사이트는 연구실 학생 한 명이 만들었다고 적는다.[^home]

누리집 논문 목록을 시기별로 보면, 2005–2011년 항목은 이메일 기반 시설의 권한·평판 관리와 스팸 대응, P2P 봇넷(악성코드에 감염되어 원격 조종되는 컴퓨터 무리 가운데, 중앙 지휘 서버 없이 감염된 컴퓨터끼리 직접 명령을 주고받는 형태)의 구조와 탐지를 주로 다룬다. 2012–2016년 항목은 운영체제 커널 무결성 감시 하드웨어(Vigilare, KI-Mon), 하드웨어 기반 외부 모니터를 겨냥한 주소 변환 공격(ATRA), TEE와 일반 실행 환경 사이의 보안 채널(SeCReT), SGX 연구용 공개 플랫폼(OpenSGX)이 중심이고, 2016–2020년 항목은 ARM TrustZone과 SGX를 쓰는 격리 실행, 힙 메모리와 객체 배치의 무작위화, 악성코드 분류와 악성 URL·공격 도구 탐지를 다룬다.[^pubs] 누리집 첫 화면 소식은 장진수 교수와 강병훈 교수의 공동 연구팀이 SelMon으로 MobiSys 2020의 Best Paper Honourable Mention(입선)을 받았다고 알린다.[^home]

논문으로 보면 지금의 전문 분야는 세 갈래다. 첫째, 프로세서 옆 보안 감시 하드웨어와 SGX·TrustZone 같은 하드웨어 기반 신뢰 실행 환경으로 특권 소프트웨어와 클라우드·사물인터넷 서비스를 지키는 시스템 설계다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 운영체제 커널과 응용 프로그램 안을 권한이 다른 구역으로 나누고 메모리 오류의 악용을 막는 격리·보호 기법이다(대표 논문 4–6).[^p4][^p5][^p6] 셋째, 스파이킹 신경망과 다중 객체 추적 시스템 같은 인공지능 시스템을 겨냥한 적대적 공격의 연구다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

대표 논문은 TEE 같은 특권 소프트웨어를 노리는 공격으로부터의 시스템 보호,[^p1] 클라우드 이용자의 사내망을 클라우드와 잇는 클라우드 VPN,[^p2] 스마트 그리드 같은 서비스를 가능하게 하는 사물인터넷 기기의 제3자 서비스,[^p3] Nginx·Memcached 같은 실제 응용,[^p4] SSL 연결에서 개인 키를 써야 하는 웹 서버,[^p5] 실시간 응용에서 쓸 수 있도록 지연을 줄인 스파이킹 신경망 공격,[^p7] 다중 객체 추적 시스템[^p8]을 대상으로 한다. 전산학부 연구실 소개는 TEE를 사물인터넷 기기에 응용하는 연구와 UAV 시스템을 주요 연구 주제로 든다.[^cslab] 교수의 기술 칼럼은 프로토콜 다이얼렉트를 사용자 기기 인증에 활용할 수 있고, 패스워드·사용자 인증서·OTP 같은 기존 사용자 인증에 더해 통신 초기에 기기 인증을 도입하는 심층 방어(Defense-in-depth)에도 쓸 수 있다고 적는다.[^dialect] 누리집 논문 목록에는 교수를 포함한 4명이 기여자로 오른 「Software Supply Chain Security Guidance」(Ministry of Science and ICT, and National Intelligence Service, and Presidential Committee on the Digital Platform Government)도 있다.[^pubs] 졸업생의 진로로는 경희대학교·충남대학교·성균관대학교 교수, National Security Research Institute (NSR), Electronics and Telecommunications Research Institute (ETRI), KAIST Cyber Security Research Center, Georgia Tech와 KAIST의 박사후연구원(Postdoc fellow), Samsung Electronics, Samsung Research, Samsung SDS, LG, LINE(Japan), S2W, Ground X, Theori, CysecuLab이 있다.[^people]

## 구성원

2026년 10월 25일 누리집 MEMBERS 칸 기준이다. Doctoral Students 칸 10명과 Master's Students 칸 5명이며, 과정은 카드의 표기(Ph.D. Student, M.S. Student)를 옮겼다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Hyeonwoo Kang | 박사과정 | 6 |
| Chang-il Lim | 박사과정 |  |
| Eunjin Kim | 박사과정 |  |
| Sangyoon Kim | 박사과정 |  |
| Donghwa Kang | 박사과정 | 7, 8 |
| Byeongsu Woo | 박사과정 | 1, 4 |
| Seo-ye Kim | 박사과정 | 4 |
| Doohyun Kim | 박사과정 | 7 |
| ChanU Kang | 박사과정 |  |
| Hojun Choe | 박사과정 |  |
| Jongmin Kim | 석사과정 |  |
| Mingyu Jun | 석사과정 |  |
| Juchang Lee | 석사과정 |  |
| Hyunseok Kim | 석사과정 |  |
| Taein Lim | 석사과정 |  |

## 졸업생과 이전 구성원

누리집 MEMBERS 칸 Alumni 카드 39장이다(Ph.D. Graduate 17명, M.S. Graduate 21명, 학위 줄 없이 기관 이름만 적힌 카드 1장). 학위와 연도는 카드의 표기(Ph.D. Graduate in 연도, M.S. Graduate in 연도)를 옮겼고, 진로는 카드에 적힌 곳이다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kihwan Kim | M.S. Graduate (2013) | LG |
| Sunjune Kong | M.S. Graduate (2015) | Samsung Electronics |
| Seunghyeon Lee | M.S. Graduate (2015) | S2W |
| Kuenwhee Oh | M.S. Graduate (2017) |  |
| Minsu Kim | Ph.D. Graduate (2018) | S2W |
| Geonwoo Kim | M.S. Graduate (2018) | CysecuLab |
| Minjoon Park | M.S. Graduate (2018) | CysecuLab |
| Daehee Jang | Ph.D. Graduate (2019) | Professor at Kyung Hee University |
| Jinsoo Jang | Ph.D. Graduate (2019) | Professor at Chungnam National University |
| Deokjin Kim | Ph.D. Graduate (2019) | National Security Research Institute (NSR) |
| Hojoon Lee | Ph.D. Graduate (2019) | Professor at Sungkyunkwan University |
| Jiseong Noh | Ph.D. Graduate (2019) | National Security Research Institute (NSR) |
| Sejin Jeong | M.S. Graduate (2019) |  |
| Soohun Kim | M.S. Graduate (2019) | National Security Research Institute (NSR) |
| Seokjoo Mun | M.S. Graduate (2019) | LG |
| Chihyun Song | M.S. Graduate (2019) | Ground X |
| Changho Choi | Ph.D. Graduate (2020) | Samsung Research |
| Dongjae Jung | Ph.D. Graduate (2020) | KAIST Cyber Security Research Center |
| Jonghwan Kim | Ph.D. Graduate (2020) | LINE, Japan |
| Suyeon Yoo | Ph.D. Graduate (2020) | National Security Research Institute (NSR) |
| Yunjong Jeong | M.S. Graduate (2020) | Ground X |
| Seungyeop Lee | M.S. Graduate (2020) | Ground X |
| Nohyun Kwak |  | Ground X |
| Jaehyuk Lee | Ph.D. Graduate (2021) | Postdoc fellow at Georgia Tech |
| Wonwoo Choi | M.S. Graduate (2022) | National Security Research Institute (NSR) |
| Hyunsoo Shin | M.S. Graduate (2022) | Ground X |
| Yeseul Choi | Ph.D. Graduate (2023) | Electronics and Telecommunications Research Institute (ETRI) |
| Youngkwang Han | Ph.D. Graduate (2023) | Postdoc fellow at KAIST |
| Daegyeong Kim | Ph.D. Graduate (2023) | Postdoc fellow at KAIST |
| Seongman Lee | Ph.D. Graduate (2023) | Postdoc fellow at KAIST |
| Junsu Lee | M.S. Graduate (2023) | Theori |
| Taehyeon Lee | M.S. Graduate (2023) | National Security Research Institute (NSR) |
| Changjo Yun | M.S. Graduate (2023) | CysecuLab |
| Seungyong Yang | Ph.D. Graduate (2025) | S2W |
| Yongho Song | Ph.D. Graduate (2025) | CysecuLab |
| Eunyeong Ahn | M.S. Graduate (2025) | National Security Research Institute (NSR) |
| Hyeonsu Lee | M.S. Graduate (2025) | CysecuLab |
| Jong Heon Lee | M.S. Graduate (2025) | Samsung SDS |
| Sungkwang Ji | M.S. Graduate (2026) | National Security Research Institute (NSR) |

## 최근 논문 목록 (2021–2026)

누리집 PUBLICATIONS 칸(SELECTED PUBLICATIONS)의 Systems Security and Malware Defense 칸에서 학술지·학회 이름 뒤에 2021–2026년이 적힌 16편이다(2026년 3편, 2025년 3편, 2024년 3편, 2023년 3편, 2022년 2편, 2021년 2편). 연도는 학술지·학회 이름 뒤의 연도이고, 제목·저자·학술지와 학회 이름은 누리집 표기 그대로다. 제목 뒤의 [to appear]는 누리집 표시다.[^pubs]

**2026**

- Taehyeon Lee, Minjoon Park, Dongmin Choi and Brent Byunghoon Kang. "HEMERA: The Detection Mechanism of Partitioning Attacks against Bitcoin Proof-of-Work Blockchain Network". *Journal of Information Processing Systems (JIPS) 2026*.
- Donghwa Kang, Woojin Shin, Cheol-Ho Hong, Byunghoon Kang, Jinkyu Lee and Hyeongboo Baek. "Adaptive Spiking Neural Networks for Real-Time Multi-Object Detection Tasks [to appear]". *Design Automation Conference (DAC) 2026*.
- Donghwa Kang, Doohyun Kim, Sang-Ki Ko, Jinkyu Lee, Hyeongboo Baek and Brent ByungHoon Kang. "Timestep-Compressed Attack on Spiking Neural Networks Through Timestep-Level Backpropagation [to appear]". *AAAI Conference on Artificial Intelligence (AAAI) 2026*.

**2025**

- Byeongsu Woo, Kha Dinh Duy, Youngkwang Han, Brent Byunghoon Kang and Hojoon Lee. "PIM-ORAM: Towards Oblivious RAM Primitives in Commodity Processing-In-Memory". *IEEE Annual Computer Security Applications Conference (ACSAC) 2025*.
- Woojin Shin, Donghwa Kang, Byeongyun Park, Brent Byunghoon Kang, Jinkyu Lee and Hyeongboo Baek. "CF-DETR: Coarse-to-Fine Transformer for Real-Time Object Detection". *IEEE Real-Time Systems Symposium (RTSS) 2025*.
- Woojin Shin, Donghwa Kang, Daejin Choi, Brent Byunghoon Kang, Jinkyu Lee and Hyeongboo Baek. "BankTweak: Adversarial Attack Against Multi-Object Trackers by Manipulating Feature Banks". *International Joint Conference on Artificial Intelligence (IJCAI) 2025*.

**2024**

- YongHo Song, Byeongsu Woo, Youngkwang Han and Brent ByungHoon Kang. "Interstellar: Fully Partitioned and Efficient Security Monitoring Hardware Near a Processor Core for Protecting Systems against Attacks on Privileged Software". *ACM SIGSAC Conference on Computer and Communications Security (CCS) 2024*.
- Seungyong Yang, Brent Byunghoon Kang and Jaehyun Nam. "Optimus: association-based dynamic system call filtering for container attack surface reduction". *Journal of Cloud Computing 2024*.
- Seongman Lee, Seoye Kim, Chihyun Song, Byeongsu Woo, Eunyeong Ahn, Junsu Lee, Yeongjin Jang, Jinsoo Jang, Hojoon Lee and Brent Byunghoon Kang. "GENESIS: A Generalizable, Efficient, and Secure Intra-kernel Privilege Separation". *ACM/SIGAPP Symposium on Applied Computing (SAC) 2024*.

**2023**

- Wonwoo Choi, Minjae Seo, Seongman Lee and Brent Byunghoon Kang. "SuM: Efficient shadow stack protection on ARM Cortex-M". *Computers & Security 2023*.
- Jaemin Park and Brent Byunghoon Kang. "EnclaveVPN: Toward Optimized Utilization of Enclave Page Cache and Practical Performance of Data Plane for Security-Enhanced Cloud VPN". *International Symposium on Research in Attacks, Intrusions and Defenses (RAID) 2023*.
- Daegyeong Kim, Wonwoo Choi, Chang-il Lim, Eunjin Kim, Geonwoo Kim, Yongho Song, Junsu Lee, Youngkwang Han, Hojoon Lee, Brent Byunghoon Kang. "Towards scalable and configurable simulation for disaggregated architecture". *Simulation Modelling Practice and Theory (SIMPAT) 2023*.

**2022**

- Hojoon Lee, Chihyun Song and Brent Byunghoon Kang. "Harnessing the x86 Intermediate Rings for Intra-Process Isolation". *IEEE Transactions on Dependable and Secure Computing (TDSC) 2022*.
- Jinsoo Jang and Brent Byunghoon Kang. "3rdParTEE: Securing Third-Party IoT Services Using the Trusted Execution Environment". *IEEE Internet of Things (IoT) Journal 2022*.

**2021**

- Yeseul Choi, Yunjong Jeong, Daehee Jang, Brent Byunghoon Kang and Hojoon Lee. "EmuID: Detecting presence of emulation through microarchitectural characteristic on ARM". *Computers & Security 2021*.
- Seongman Lee, Hyeonwoo Kang, Jinsoo Jang and Brent Byunghoon Kang. "SaVioR: Thwarting Stack-Based Memory Safety Violations by Randomizing Stack Layout". *IEEE Transactions on Dependable and Secure Computing (TDSC) 2021*.

같은 칸에는 연도 표기 없이 「Software Supply Chain Security Guidance」(Contributed by Minjoon Park, Changil Lim, Changjo Yun, Brent Byunghoon Kang; Ministry of Science and ICT, and National Intelligence Service, and Presidential Committee on the Digital Platform Government)도 실려 있다.[^pubs]

## 특허

교수가 보안뉴스에 쓴 기술 칼럼(2022-10-12 등록)이 프로토콜 다이얼렉트 기술에 대해 적은 2건이다. 이름과 번호는 칼럼 표기다. 칼럼은 앞의 건을 특허를 취득한 것으로, 뒤의 건을 미국에 제품을 등록한 상태로 적는다.[^dialect]

- 네트워크에 연결된 시스템의 보안을 위한 프로토콜 다이얼렉트 기법 (번호 10-2021-0049779)
- PROTOCOL DIALECT FOR NETWORK SYSTEM SECURITY (번호 US 17374084)

## 연락과 위치

- 연구실: N5 2320 at KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon, Republic of Korea 305-701(누리집 표기)[^home]
- 연구실 전화: +82 (42) 350-8338[^home]
- 교수연구실: N5 2315호, 전화 042-350-8322[^csfac][^cslab][^gsisfac]
[^home]: 연구실 누리집 첫 화면 <https://cysec.kr/> (연구실 이름, 소식 칸, COURSE 칸, ADDRESS·CONTACTS 칸, 2026-10-25 열람)
[^people]: 누리집 첫 화면 MEMBERS 칸 <https://cysec.kr/#members> (Faculty, Doctoral Students, Master's Students, Alumni 카드. 카드 자료 <https://cysec.kr/js/members.js>, 2026-10-25 열람)
[^pubs]: 누리집 첫 화면 PUBLICATIONS 칸 <https://cysec.kr/#publications> (SELECTED PUBLICATIONS의 Systems Security and Malware Defense, Book Chapter/Articles (Refereed), Cyber Security Education (Hands-on Labs) and Others 칸. 목록 자료 <https://cysec.kr/js/papers.js>, 2026-10-25 열람)
[^intro]: 누리집 교수 소개 페이지 <https://cysec.kr/brentkang/new_brentkang.html> (영문·국문 소개, 2026-10-25 열람)
[^csfac]: KAIST 전산학부 교수 소개(강병훈) <https://cs.kaist.ac.kr/people/view?idx=510&kind=faculty&menu=160> (2026-10-25 열람)
[^cslab]: KAIST 전산학부 연구실 소개(사이버 보안 시스템 연구실) <https://cs.kaist.ac.kr/research/labView?sn=95&menu=64> (2026-10-25 열람)
[^gsisfac]: KAIST 정보보호대학원 교수진 목록 <https://gsis.kaist.ac.kr/people/faculty> (2026-10-25 열람)
[^gsislab]: KAIST 정보보호대학원 연구실 목록 <https://gsis.kaist.ac.kr/research/center> (Cyber system Security (CySec) Lab 항목, 2026-10-25 열람)
[^dialect]: 보안뉴스 「[테크칼럼] 네트워크 시스템 보안 위한 ‘프로토콜 다이얼렉트’ 기술」(글 강병훈, 2022-10-12 등록) <http://www.boannews.com/news/articleView.html?idxno=110440> (2026-10-25 열람)
[^p1]: Y. Song, B. Woo, Y. Han, B. B. Kang, Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security, 198-212 (온라인 2024-12-09). <https://doi.org/10.1145/3658644.3690247> 초록 기준(OpenAlex 등록 초록).
[^p2]: J. Park, B. B. Kang, Proceedings of the 26th International Symposium on Research in Attacks, Intrusions and Defenses, 397-411 (온라인 2023-10-16). <https://doi.org/10.1145/3607199.3607210> 초록 기준(OpenAlex 등록 초록).
[^p3]: J. Jang, B. B. Kang, IEEE Internet of Things Journal 9, 15814-15826 (2022). <https://doi.org/10.1109/jiot.2022.3152555> 초록 기준(OpenAlex 등록 초록).
[^p4]: S. Lee 외, B. B. Kang, Proceedings of the 39th ACM/SIGAPP Symposium on Applied Computing, 1366-1375 (온라인 2024-05-21). <https://doi.org/10.1145/3605098.3635951> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: H. Lee, C. Song, B. B. Kang, IEEE Transactions on Dependable and Secure Computing 20, 3251-3268 (2023). <https://doi.org/10.1109/tdsc.2022.3192524> 초록 기준(OpenAlex 등록 초록).
[^p6]: S. Lee, H. Kang, J. Jang, B. B. Kang, IEEE Transactions on Dependable and Secure Computing 19, 2559-2575 (2022). <https://doi.org/10.1109/tdsc.2021.3063843> 초록 기준(OpenAlex 등록 초록).
[^p7]: D. Kang 외, B. B. Kang, Proceedings of the AAAI Conference on Artificial Intelligence 40, 5602-5610 (온라인 2026-03-14). <https://doi.org/10.1609/aaai.v40i7.37479> 초록 기준.
[^p8]: W. Shin 외, H. Baek, Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence, 1847-1855 (2025). <https://doi.org/10.24963/ijcai.2025/206> 초록 기준.

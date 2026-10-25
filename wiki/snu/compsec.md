# 시스템 보안 연구실 (Computer Security Lab, CompSec Lab)

**서울대학교 공과대학 전기·정보공학부 · 이병영 교수**

- 대분야: 컴퓨팅·AI
- 태그: 소프트웨어·시스템 보안[^research], 프로그램 분석·검증[^research], 퍼징[^research], 컴퓨터 구조·운영체제[^research], 하드웨어 보안[^research], 대형 언어 모델[^research]
- 홈페이지: https://compsec.snu.ac.kr/
- 교수 누리집: https://lifeasageek.github.io/

> 운영체제와 브라우저, 보안 하드웨어, AI 에이전트가 데이터를 처리하고 권한을 행사하는 과정의 취약점을 찾아 방어 체계를 만드는 연구실이다.[^home][^research]

## 무엇을 연구하나

시스템이 정상적으로 제공하는 기능이 어떤 조건에서 보안 문제로 바뀌는지 살피고, 이를 막는 소프트웨어와 시스템을 설계한다. 운영체제(프로그램 실행과 컴퓨터 자원을 관리하는 기본 소프트웨어), 사용자 응용 프로그램, 하드웨어가 함께 연구 대상이다. 커널(운영체제에서 자원과 접근 권한을 관리하는 핵심 부분)의 공격과 방어, 브라우저 취약점, 하드웨어의 정보 유출을 다룬다.[^home][^research]

최근에는 대형 언어 모델(많은 글을 학습해 언어를 처리하고 생성하는 인공지능 모델, Large Language Model, LLM)을 바탕으로 도구를 사용하는 AI 에이전트(목표에 따라 행동과 도구 사용을 결정하는 소프트웨어)의 보안을 연구한다. 외부 데이터에 포함된 지시가 동작을 바꾸는 간접 프롬프트 주입과, 믿을 수 있는 데이터로 위장한 입력을 구분해 살핀다. 데이터가 저장되었다가 다시 읽힐 때에도 신뢰 경계(서로 다른 신뢰 수준의 데이터나 실행 영역을 나누는 구분)가 유지되도록 하는 방어를 개발한다.[^research][^p1][^p2]

오류를 자동으로 찾는 연구에서는 퍼징(검사 입력을 자동 생성·변형하여 오류를 찾는 소프트웨어 시험)을 쓴다. 웹 브라우저와 하이퍼바이저(가상머신을 관리하고 실행하는 시스템 소프트웨어), 커널 등을 검사한다. 하드웨어 연구에서는 추측 실행(명령의 실행 필요성이 확정되기 전에 미리 처리하는 방식)과 메모리 보호 기능이 만날 때의 취약점, 부채널(시간이나 캐시 상태처럼 간접 관측을 통해 정보를 드러내는 경로)을 분석하고 대응책을 제안한다.[^research][^p5][^p6][^p7][^p8]

또 다른 축은 기밀 연산(실행 중인 데이터의 비밀성과 무결성을 보호하는 연산, confidential computing)이다. 데이터를 맡아 처리하는 개발자나 클라우드 관리자를 전적으로 신뢰하기 어려운 환경에서도 데이터 이용 정책을 지키도록 연구한다. 훈련 데이터 유출을 제한하는 모델 학습과 데이터 분석 과정의 정책 집행이 그 예다.[^research][^p3][^p4]

## 주요 연구 주제

### 1. AI 에이전트의 데이터 신뢰와 방어

DualView는 에이전트와 사람이 보는 데이터를 나누어 외부 입력이 저장 후 다시 읽히는 경우까지 신뢰 경계를 유지한다. Agent Data Injection은 악성 지시문뿐 아니라 신뢰할 데이터로 위장한 입력도 에이전트의 의도하지 않은 행동을 유발할 수 있음을 분석한다.[^p1][^p2]

### 2. 기밀 연산과 데이터 이용 정책

DLBox는 개발자가 제공한 학습 코드에 데이터 이용 규칙을 적용하고 기밀 연산으로 보호한다. 학습된 모델을 통한 모든 유출을 완전히 막는다고 주장하는 대신, 허용되지 않은 경로의 데이터 유출을 제한하는 것을 목표로 한다. Laputa는 Spark(여러 컴퓨터에서 데이터를 나누어 처리하는 소프트웨어) 분석의 실행 계획에서 정책을 검사하고 분석 과정을 보호한다.[^p3][^p4]

### 3. 자동 취약점 탐색

FuzzOrigin은 브라우저에서 웹페이지 사이의 보안 경계가 깨지는 오류를 자동으로 찾는다. MundoFuzz는 하이퍼바이저 검사에서 입력의 형식과 실행 범위를 분석하여 취약점을 찾는다. 커널의 동시 실행 과정에서 생기는 오류도 연구실의 자동 탐색 대상이다.[^p5][^p6][^research]

### 4. 하드웨어와 커널의 공격·방어

TikTag는 ARM의 메모리 태깅(메모리와 포인터에 표식을 붙여 접근의 유효성을 검사하는 기능, Memory Tagging Extension, MTE)과 추측 실행 사이의 보안 위험을 밝히고 완화책을 제안한다. Pspray는 Linux 커널의 시간 관측을 통한 정보 유출이 메모리 취약점의 악용 가능성에 미치는 영향을 분석하고 방어 방법을 제시한다.[^p7][^p8]

## 대표 논문

최근 연구와 서로 다른 연구 갈래를 함께 보여 주도록 8편을 골랐다. 모두 이병영 교수가 마지막 저자인 논문이며, 마지막 저자라는 사실만으로 교신저자라고 단정하지 않는다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. arXiv 항목은 사전 공개본이며, TikTag는 2024년 arXiv 판을 설명한다.[^pubs][^pipubs]

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [DualView: Preventing Indirect Prompt Injection in Personal AI Agents](https://arxiv.org/abs/2607.03821) | 에이전트에는 신뢰하지 않는 데이터를 기호로 보이고 사람과 도구에는 원문을 유지한다. 데이터가 저장된 뒤 다시 읽혀도 이 구분을 이어 가며, 평가한 간접 프롬프트 주입 공격을 차단했다.[^p1] |
| 2 | 2026 | [Agent Data Injection Attacks are Realistic Threats to AI Agents](https://arxiv.org/abs/2607.05120) | 명령이 아니라 믿을 수 있는 데이터로 위장한 입력도 AI 에이전트의 행동을 바꿀 수 있음을 보였다. 실제 웹·코딩 에이전트에서 신뢰할 입력과 그렇지 않은 입력의 분리가 부족한 문제를 분석했다.[^p2] |
| 3 | 2025 | [DLBox: New Model Training Framework for Protecting Training Data](https://www.ndss-symposium.org/ndss-paper/dlbox-new-model-training-framework-for-protecting-training-data/) | 데이터를 맡은 개발자가 학습 코드나 모델을 통해 훈련 데이터를 유출하는 문제를 다룬다. 학습 규칙과 기밀 연산을 결합해 부적절한 유출 경로를 제한하는 프레임워크를 구현했다.[^p3] |
| 4 | 2025 | [Secure Data Analytics in Apache Spark with Fine-grained Policy Enforcement and Isolated Execution](https://www.ndss-symposium.org/ndss-paper/secure-data-analytics-in-apache-spark-with-fine-grained-policy-enforcement-and-isolated-execution/) | 데이터를 분석하는 사용자나 클라우드 관리자가 데이터 이용 정책을 어기는 것을 막는 Laputa를 제안했다. 분석 실행 계획을 검사하고 기밀 연산으로 분석 과정을 보호했으며, 악성 응용 프로그램을 차단하는지 평가했다.[^p4] |
| 5 | 2022 | [FuzzOrigin: Detecting UXSS vulnerabilities in Browsers through Origin Fuzzing](https://www.usenix.org/conference/usenixsecurity22/presentation/kim) | 브라우저가 서로 다른 웹페이지 사이의 보안 경계를 잘못 처리하는 취약점(UXSS, Universal Cross-Site Scripting)을 자동으로 찾는다. Chrome과 Firefox에서 새 취약점을 찾아 제조사의 확인을 받았다.[^p5] |
| 6 | 2022 | [MundoFuzz: Hypervisor Fuzzing with Statistical Coverage Testing and Grammar Inference](https://www.usenix.org/conference/usenixsecurity22/presentation/myung) | 가상머신을 관리하는 소프트웨어의 실행 범위 측정에서 잡음을 걸러 내고 입력 형식을 추론해 검사한다. QEMU와 Bhyve를 대상으로 새로운 오류를 찾았다.[^p6] |
| 7 | 2024 | [TikTag: Breaking ARM's Memory Tagging Extension with Speculative Execution](https://arxiv.org/abs/2406.08719) | 메모리 오류를 막기 위한 ARM의 표식 보호가 추측 실행에 의해 약해질 수 있음을 보였다. 실제 시스템에서 위험을 평가하고 완화 방법을 제안한 사전 공개본이다.[^p7] |
| 8 | 2023 | [Pspray: Timing Side-Channel based Linux Kernel Heap Exploitation Technique](https://www.usenix.org/conference/usenixsecurity23/presentation/lee-yoochan) | Linux 커널에서 시간 정보가 메모리 취약점 악용의 성공 가능성을 높이는 문제를 분석했다. 그 위협을 줄이는 방어를 함께 제안하고 영향을 평가했다.[^p8] |

## 교수와 전문 분야

이병영 교수는 2009년 포항공과대학교 컴퓨터공학과 학사, 2011년 같은 대학 석사, 2016년 조지아공과대학교 컴퓨터과학 박사 학위를 받았다. 2016–2018년 퍼듀대학교 컴퓨터과학과 조교수로 재직했고, 2018년 서울대학교에 부임했다.[^deptpi]

학과는 전문 분야를 컴퓨터 보안, 시스템·소프트웨어 보안, 취약점 분석과 방어, 기밀 연산 및 데이터·개인정보 보호로 소개한다. 최근 연구에는 AI 에이전트 보안이 더해져 있다. 대표 논문으로 보면 자동 검사 도구에서 데이터 처리 환경의 정책 집행까지 보안 경계를 구현하고 분석하는 것이 전문 분야다.[^deptpi][^pi][^p1][^p3][^p5]

## 응용 분야

브라우저와 운영체제의 취약점 검사, 가상화 기반 클라우드의 보안, 데이터를 제공하는 주체와 모델 개발자가 다른 환경의 학습·분석, 도구를 사용하는 AI 에이전트의 안전한 실행이 연구의 응용 대상이다.[^research][^p3][^p4][^p5][^p6]

## 구성원

연구실 People 페이지의 교수 외 구성원 11명이다. 과정은 연구실 표기이고 시작 연월은 개인 소개에 적힌 값이다. 대표 논문 저자와 같은 이름을 같은 사람으로 보아 참여 번호를 표시했다.[^people][^memberprofiles]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Sangyun Kim | 박사과정 | 2020.09 | sangyun.kim@snu.ac.kr | 3 |
| Young Min Kim | 박사과정 | 2021.09 | ym.kim@snu.ac.kr | 1, 5 |
| Sihyun Roh | 박사과정 | 2023.09 | sihyeonroh@snu.ac.kr | 7 |
| Jaeyoung Chung | 박사과정 | 2024.03 | jjy600901@snu.ac.kr | 7 |
| Woohyuk Choi | 박사과정 | 2025.03 | 00cwooh@snu.ac.kr | 1, 2 |
| Minhye Yoo | 석사과정 |  | yoominhye@snu.ac.kr |  |
| Junghyun Park | 박사과정 | 2025.09 | mastpark2001@snu.ac.kr |  |
| Eulgyu Kim | 박사과정 | 2025.09 | eulgyukim@snu.ac.kr |  |
| Taehyun Kang | 박사과정 | 2025.09 | gangtaeng_parangvo@snu.ac.kr | 1, 2 |
| Jonguk Cheong | 박사과정 | 2026.03 | jdal3031@snu.ac.kr |  |
| Myungbin Hwang | 박사과정 | 2026.03 | auddl1020@snu.ac.kr |  |

## 졸업생과 이전 구성원

연구실 Alumni의 18명과 교수 누리집에만 있는 Kyungtae Kim을 함께 실었다. Purdue 학위 표기가 있는 이전 구성원을 포함하며, 학위·연월·진로는 연구실 표기를 우선한다. 두 누리집의 이표기는 [근거 페이지](compsec-sources.md)에 따로 정리했다.[^people][^pipeople]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yuseok Jeon | PhD (Purdue) (2020.12) | UNIST (Assistant Professor) |
| Gwangmu Lee | PhD (2022.02) | Swiss National Supercomputing Centre (CSCS) |
| Seonghyun Park | MS (2022.02) | Rebellions |
| Sunwoo Kim | MS (2022.02) | Samsung Research |
| Adil Ahmad | PhD (Purdue) (2022.08) | Arizona State University (Assistant Professor) |
| Jinwoo Lee | MS (2022.08) | HealthHub |
| Jinhan Kwak | MS (2023.02) | Start-up |
| Jaewon Hur | PhD (2023.08) | Apple (Software Engineer) |
| Byeongwook Kim | MS (2024.02) | SK Hynix |
| Hyokyung Kim | MS (2024.08) | National Security Research Institute |
| Cheolwoo Myung | PhD (2025.02) | Samsung Electronics |
| Youngjoo Lee | MS (2025.02) | Microsoft |
| Chulmin Lee | MS (2025.02) | MD course in Medical school |
| Yoochan Lee | PhD (2025.08) | Max Plank Institute (Postdoc) |
| Suhwan Song | PhD (2025.08) | Samsung Electronics |
| Kyungwook Boo | PhD (2026.08) | Samsung Electronics |
| Juhee Kim | PhD (2026.08) | Microsoft Azure Research |
| Chia Ni Lim | MS (2026.08) | Samsung Electronics |
| Kyungtae Kim | PhD at Purdue (2022.08) | Assistant Professor at Dartmouth |

## 최근 논문 목록 (2021–2026)

연구실 Publications의 2021–2026년 구역과 교수 개인 목록을 대조한 38항목이다. 교수 개인 목록을 함께 썼으며, 이 기간은 2018년 서울대 부임 이후다. 연도는 누리집 구역을 따르며 2021년 항목은 월·일과 관계없이 포함한다. 논문·워크숍·BlackHat 발표·arXiv 사전 공개본을 포함하고, 발표 예정 표기는 교수 누리집의 to appear를 따른다. TikTag의 2025년 학회 항목은 대표 논문에서 설명한 2024년 사전 공개본과 구분한다. 별표와 공동 1저자 표기는 원문 그대로다.[^pubs][^pipubs][^deptpi]

**2026**

- Woohyuk Choi\*, Juhee Kim\*, Taehyun Kang, Jihyeon Jeong, Luyi Xing, and Byoungyoung Lee (\* co-first authors). "Agent Data Injection Attacks are Realistic Threats to AI Agents". *arXiv Preprint 2026（사전 공개본）*.
- Juhee Kim\*, Woohyuk Choi\*, Taehyun Kang, Youngmin Kim, and Byoungyoung Lee (\* co-first authors). "DualView: Preventing Indirect Prompt Injection in Personal AI Agents". *arXiv Preprint 2026（사전 공개본）*.
- Juhee Kim\*, Jaeyoung Chung\*, Dae R. Jeong, and Byoungyoung Lee (\* co-first authors). "DMGuard: Safeguarding Kernels from Physical Page Use-After-Free Vulnerabilities". *USENIX Security Symposium (Security) 2026 · to appear（발표 예정）*.
- Sihyun Roh, Woohyuk Choi, Jaeyoung Chung, Yoochan Lee, Suhwan Song, and Byoungyoung Lee. "GHost in the SHELL: A GPU-to-Host Memory Attack and Its Mitigation". *IEEE Symposium on Security and Privacy (SP) 2026*.
- Yoochan Lee, Sihyun Roh, Hyuk Kwon, Byoungyoung Lee, and Thorsten Holz. "Heap Localization: Cache Side-Channel based Linux Kernel Heap Exploit Techniques". *IEEE Symposium on Security and Privacy (SP) 2026*.
- Suyoung Lee, Seongho Keum, Changoo Lee, Dongwon Shin, Sanghyun Hong, Byoungyoung Lee, and Sooel Son. "Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions". *IEEE Symposium on Security and Privacy*.
- Yongbi Son, Changoo Lee, Dongwon Shin, Byoungyoung Lee, Sanghyun Hong, and Sooel Son. "AgentBreaker: Evaluating Context-Aware Indirect Prompt Injection Risks in Modern Web Agents". *ACM SIGSOFT International Symposium on Software Testing and Analysis · to appear（발표 예정）*.

**2025**

- Jaewon Hur, Juheon Yi, Cheolwoo Myung, Sangyun Kim, Youngki Lee, and Byoungyoung Lee. "DLBox: New Model Training Framework for Protecting Training Data". *Network and Distributed System Security Symposium (NDSS) 2025*.
- Byeongwook Kim\*, Jaewon Hur\*, Adil Ahmad, and Byoungyoung Lee (\* co-first authors). "Secure Data Analytics in Apache Spark with Fine-grained Policy Enforcement and Isolated Execution". *Network and Distributed System Security Symposium (NDSS) 2025*.
- Juhee Kim, Jinbum Park, Sihyun Roh, Jaeyoung Chung, Youngjoo Lee, Taesoo Kim, and Byoungyoung Lee. "TikTag: Breaking ARM's Memory Tagging Extension with Speculative Execution". *IEEE Symposium on Security and Privacy (SP) 2025*.
- Juhee Kim\*, Woohyuk Choi\*, and Byoungyoung Lee (\* co-first authors). "Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents". *arXiv Preprint 2025（사전 공개본）*.
- Kyungwook Boo, and Byoungyoung Lee. "Finding Device Driver Bugs With Fuzzing PCIe Configuration Input". *IEEE Access*.

**2024**

- Juhee Kim, Jinbum Park, Yoochan Lee, Chengyu Song, Taesoo Kim, and Byoungyoung Lee. "PeTAL: Ensuring Access Control Integrity against Data-only Attacks on Linux". *ACM Conference on Computer and Communications Security (CCS) 2024*.
- Dae R. Jeong, Yewon Choi, Byoungyoung Lee, Insik Shin, and Youngjin Kwon. "OZZ: Identifying Kernel Out-of-Order Concurrency Bugs with In-Vivo Memory Access Reordering". *ACM Symposium on Operating Systems Principles (SOSP) 2024*.
- Juhee Kim, Jinbum Park, Sihyun Roh, Jaeyoung Chung, Youngjoo Lee, Taesoo Kim, and Byoungyoung Lee. "Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack". *BlackHat USA 2024*.
- Jaehyun Song, Bumsuk Kim, Minwoo Kwak, Byoungyoung Lee, Euiseong Seo, and Jinkyu Jeong. "A Secure, Fast, and Resource-Efficient Serverless Platform with Function REWIND". *USENIX Annual Technical Conference (ATC) 2024*.
- Gwangmu Lee, Duo Xu, Solmaz Salimi, Byoungyoung Lee, and Mathias Payer. "SyzRisk: A Change-Pattern-Based Continuous Kernel Regression Fuzzer". *ACM Symposium on Information, Computer and Communications Security (ASIACCS) 2024*.
- Chulmin Lee, Jaewon Hur, Sangho Lee, and Byoungyoung Lee. "TEEMATE: Fast and Efficient Confidential Container using Shared Enclave". *arXiv preprint（사전 공개본）*.

**2023**

- Suhwan Song, and Byoungyoung Lee. "Metamong: Detecting Render-update Bugs in Web Browsers through Fuzzing". *ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE) 2023*.
- Adil Ahmad, Alex Schultz, Byoungyoung Lee, and Pedro Fonseca. "An Extensible Orchestration and Protection Framework for Confidential Cloud Computing". *USENIX Symposium on Operating Systems Design and Implementation (OSDI) 2023*.
- Dae R. Jeong, Byoungyoung Lee, Insik Shin, and Youngjin Kwon. "SEGFUZZ: Segmentizing Thread Interleaving to Discover Kernel Concurrency Bugs through Fuzzing". *IEEE Symposium on Security and Privacy (SP) 2023*.
- Jaewon Hur, and Byoungyoung Lee. "GRAMINER: Fuzz Testing Gramine LibOS to Harden the Trusted Computing Base". *Workshop on System Software for Trusted Execution (SysTEX) 2023*.
- Young Min Kim, and Byoungyoung Lee. "Extending a Hand to Attackers: Browser Privilege Escalation Attacks via Extensions". *USENIX Security Symposium (Security) 2023*.
- Yoochan Lee, Jinhan Kwak, Junesoo Kang, Yuseok Jeon, and Byoungyoung Lee. "Pspray: Timing Side-Channel based Linux Kernel Heap Exploitation Technique". *USENIX Security Symposium (Security) 2023*.
- Dae R. Jeong, Minkyu Jung, Yoochan Lee, Byoungyoung Lee, Insik Shin, and Youngjin Kwon. "Diagnosing Kernel Concurrency Failures with AITIA". *ACM EuroSys Conference (EuroSys) 2023*.

**2022**

- Yoochan Lee, Byoungyoung Lee, Yuseok Jeon, Jinhan Kwak, and Junesoo Kang. "Perfect Spray: A Journey From Finding a New Type of Logical Flaw at Linux Kernel To Developing a New Heap Exploitation Technique". *BlackHat Europe 2022*.
- Jaewon Hur, Suhwan Song, Sunwoo Kim, and Byoungyoung Lee. "SpecDoctor: Differential Fuzz Testing to Find Transient Execution Vulnerabilities". *ACM Conference on Computer and Communications Security (CCS) 2022*.
- Sunwoo Kim, Young Min Kim, Jaewon Hur, Suhwan Song, Gwangmu Lee, and Byoungyoung Lee. "FuzzOrigin: Detecting UXSS vulnerabilities in Browsers through Origin Fuzzing". *USENIX Security Symposium (Security) 2022*.
- Ju Chen, Wookhyun Han, Mingjun Yin, Haochen Zeng, Yuxuan Chen, Chengyu Song, Byoungyoung Lee, Heng Yin, and Insik Shin. "SYMSAN: Time and Space Efficient Concolic Execution via Dynamic Data-flow Analysis". *USENIX Security Symposium (Security) 2022*.
- Cheolwoo Myung, Gwangmu Lee, and Byoungyoung Lee. "MundoFuzz: Hypervisor Fuzzing with Statistical Coverage Testing and Grammar Inference". *USENIX Security Symposium (Security) 2022*.
- Suhwan Song, Jaewon Hur, Sunwoo Kim, Philip Rogers, and Byoungyoung Lee. "R2Z2: Detecting Rendering Regressions in Web Browsers through Differential Fuzz Testing". *IEEE/ACM International Conference on Software Engineering (ICSE) 2022*.
- Kyungtae Kim, Taegyu Kim, Ertza Warraich, Byoungyoung Lee, Kevin Butler, Antonio Bianchi, and Dave (Jing) Tian. "FuzzUSB: Hybrid Stateful Fuzzing of USB Gadget Stacks". *IEEE Symposium on Security and Privacy (SP) 2022*.

**2021**

- Jaewon Hur, Suhwan Song, Dongup Kwon, Eunjin Baek, Jangwoo Kim, and Byoungyoung Lee. "DiFuzzRTL: Differential Fuzz Testing to Find CPU Bugs". *IEEE Symposium on Security and Privacy (SP) 2021*.
- Yoochan Lee, Changwoo Min, and Byoungyoung Lee. "ExpRace: Exploiting Kernel Races through Raising Interrupts". *USENIX Security Symposium (Security) 2021*.
- Gwangmu Lee, Woochul Shim, and Byoungyoung Lee. "Constraint-guided Directed Greybox Fuzzing". *USENIX Security Symposium (Security) 2021*.
- Arslan Khan, Hyungsub Kim, Byoungyoung Lee, Dongyan Xu, Antonio Bianchi, and Dave Tian. "M2MON: Building an MMIO-based Security Reference Monitor for Unmanned Vehicles". *USENIX Security Symposium (Security) 2021*.
- Adil Ahmad, Sangho Lee, Pedro Fonseca, and Byoungyoung Lee. "KARD: Lightweight Data Race Detection with Per-Thread Memory Protection". *International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS) 2021*.
- Adil Ahmad, Juhee Kim, Jaebaek Seo, Insik Shin, Pedro Fonseca, and Byoungyoung Lee. "Chancel: Efficient Multi-client Isolation Under Adversarial Programs". *Network and Distributed System Security Symposium (NDSS) 2021*.

## 수상과 선정

교수 누리집 Honors의 2021-10-22–2026-10-22 범위에 해당하는 2건이다. 날짜는 원문이 밝힌 연도다.[^honors]

- 2024 · SOSP 2024 Best Paper Award（OZZ）
- 2023 · ACM CCS Top Reviewer Award

## 소식

연구실 첫 화면의 연구 관련 공지 8건이다. 기간은 2025년 9월 9일–2026년 10월 22일이며, 연구 결과와 소프트웨어·자료 공개, 논문 채택을 다룬다.[^home][^blog][^dualblog][^badblog]

- 2026-10-22 · 발견·신고한 취약점을 모은 CVEs 페이지 공개.
- 2026-10-21 · AI 코딩 에이전트에 비밀정보 대신 가려진 표기를 보이는 공개 소프트웨어 Mandu 발표.
- 2026-07-12 · 웹 에이전트의 의도하지 않은 동작을 유발하는 Agent Data Injection 사전 공개본 소개.
- 2026-07-07 · 개인 AI 에이전트의 간접 프롬프트 주입을 막는 DualView 사전 공개본 소개.
- 2026-06-25 · Linux 커널의 epoll 하위 시스템에서 발견한 경쟁 상태 기반 메모리 취약점 Bad Epoll 공개.
- 2026-03 · Heap Localization의 IEEE S&P 2026 채택 공지.
- 2025-12-18 · DMGuard의 USENIX Security 2026 채택 공지.
- 2025-09-09 · GHost in the SHELL의 IEEE S&P 2026 채택 공지.

## 연락과 위치

- 연구실: 서울대학교 303동 561-1호. 서울특별시 관악구 관악로 1, 우편번호 08826.[^visit]
- 교수연구실: 서울대학교 301동 709호. 전화 02-880-7266.[^deptpi]
- 교수 이메일: byoungyoung@snu.ac.kr.[^pi][^people]
- 문서 기준일: 2026-10-22. 누리집 관측일: 2026-10-25.
- [자료와 표기 근거](compsec-sources.md)

## 각주
[^home]: CompSec Lab, 첫 화면의 연구 소개와 Latest Updates. <https://compsec.snu.ac.kr/> (2026-10-25 열람).
[^research]: CompSec Lab, Research. AI Agent Security, Hardware & Microarchitectural Security, Vulnerability Finding, System Attack & Defense, Confidential Computing & Trusted Execution의 연구 소개. <https://compsec.snu.ac.kr/research> (2026-10-25 열람).
[^pi]: Byoungyoung Lee, 교수 개인 누리집. <https://lifeasageek.github.io/> (2026-10-25 열람).
[^deptpi]: 서울대학교 전기·정보공학부, 이병영 전임교수 소개. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p826> (2026-10-25 열람).
[^people]: CompSec Lab, People의 Members와 Alumni. <https://compsec.snu.ac.kr/people> (2026-10-25 열람).
[^pipeople]: Byoungyoung Lee, People. <https://lifeasageek.github.io/people.html> (2026-10-25 열람).
[^memberprofiles]: CompSec Lab, 구성원 개인 소개의 Since 표기. <https://compsec.snu.ac.kr/people/sangyunkim>, <https://compsec.snu.ac.kr/people/youngminkim>, <https://compsec.snu.ac.kr/people/sihyunroh>, <https://compsec.snu.ac.kr/people/jaeyoungchung>, <https://compsec.snu.ac.kr/people/woohyukchoi>, <https://compsec.snu.ac.kr/people/junghyunpark>, <https://compsec.snu.ac.kr/people/eulgyukim>, <https://compsec.snu.ac.kr/people/taehyunkang>, <https://compsec.snu.ac.kr/people/jongukcheong>, <https://compsec.snu.ac.kr/people/myungbinhwang> (2026-10-25 열람).
[^pubs]: CompSec Lab, Publications. <https://compsec.snu.ac.kr/publications> (2026-10-25 열람).
[^pipubs]: Byoungyoung Lee, Publications의 Conference와 Journal. <https://lifeasageek.github.io/publications.html> (2026-10-25 열람).
[^honors]: Byoungyoung Lee, Honors & Awards. <https://lifeasageek.github.io/honors.html> (2026-10-25 열람).
[^blog]: CompSec Lab, Blog 게시 목록. <https://compsec.snu.ac.kr/blog> (2026-10-25 열람).
[^dualblog]: Juhee Kim, “DualView: Defending personal AI agents like OpenClaw against indirect prompt injection”, 2026-07-07. <https://compsec.snu.ac.kr/blog/dualview> (2026-10-25 열람).
[^badblog]: Jaeyoung Chung, “Bad Epoll: The bug missed by Mythos”, 2026-06-25. <https://compsec.snu.ac.kr/blog/badepoll> (2026-10-25 열람).
[^visit]: CompSec Lab, Visit Us. <https://compsec.snu.ac.kr/visit> (2026-10-25 열람).

[^p1]: J. Kim 외, B. Lee, arXiv 사전 공개본 (온라인 2026-09-14). <https://arxiv.org/abs/2607.03821> 초록 기준(arXiv 판).
[^p2]: W. Choi 외, B. Lee, arXiv 사전 공개본 (온라인 2026-07-06). <https://arxiv.org/abs/2607.05120> 초록 기준(arXiv 판).
[^p3]: J. Hur 외, B. Lee, Network and Distributed System Security Symposium. <https://www.ndss-symposium.org/ndss-paper/dlbox-new-model-training-framework-for-protecting-training-data/> 초록 기준(학회 논문집 페이지 게시 초록).
[^p4]: B. Kim, J. Hur, A. Ahmad, B. Lee, Network and Distributed System Security Symposium. <https://www.ndss-symposium.org/ndss-paper/secure-data-analytics-in-apache-spark-with-fine-grained-policy-enforcement-and-isolated-execution/> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: S. Kim 외, B. Lee, 31st USENIX Security Symposium (USENIX Security 22), 1008–1023 (2022). <https://www.usenix.org/conference/usenixsecurity22/presentation/kim> 초록 기준(학회 아카이브 게시 초록).
[^p6]: C. Myung, G. Lee, B. Lee, 31st USENIX Security Symposium (USENIX Security 22), 1257–1274 (2022). <https://www.usenix.org/conference/usenixsecurity22/presentation/myung> 초록 기준(학회 아카이브 게시 초록).
[^p7]: J. Kim 외, B. Lee, arXiv 사전 공개본 (온라인 2024-06-13). <https://arxiv.org/abs/2406.08719> 초록 기준(arXiv 판).
[^p8]: Y. Lee 외, B. Lee, 32nd USENIX Security Symposium (USENIX Security 23), 6825–6842 (2023). <https://www.usenix.org/conference/usenixsecurity23/presentation/lee-yoochan> 초록 기준(학회 아카이브 게시 초록).

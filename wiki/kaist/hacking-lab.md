# 해킹 연구실 (Hacking Lab)

**KAIST 전기및전자공학부 · 윤인수 교수**

- 분야: 시스템·소프트웨어 보안, 퍼징(무작위에 가까운 입력으로 오류를 찾는 시험 기법), 운영체제 커널 공격·방어, 바이너리(기계어 코드) 분석, 이동통신 베이스밴드(휴대폰 통신 칩 소프트웨어) 보안, 대형 언어 모델(LLM) 에이전트를 이용한 취약점 자동 수정
- 홈페이지: <https://hacking.kaist.ac.kr/>
- 근거와 출처: [해킹 연구실 근거 페이지](hacking-lab-sources.md)

> 소프트웨어와 시스템의 보안 약점을 해커의 눈으로 찾아내고, 이를 막는 기술을 만드는 연구실이다. 웹 브라우저·운영체제·휴대폰 통신 칩에서 실제 취약점을 찾아 보고하고, 해킹 대회와 AI 보안 경진대회에서도 성과를 내고 있다.[^home]

## 무엇을 연구하나

연구실은 "보안을 위한 시스템을 만들고, 시스템의 보안을 연구한다"고 소개한다.[^home] 전기및전자공학부는 교수의 연구를 시스템 보안과 소프트웨어 보안으로 적는다.[^ee] 연구실 소식에는 논문 소식과 함께 해킹 대회·버그 바운티(취약점을 찾아 알리면 기업이 주는 보상) 성과가 올라 있다. DEF CON CTF 34 결선 2위(2026), AI 사이버 보안 경진대회 AIxCC에서 Team Atlanta의 우승(2025), Pwn2Own 2024에서 랩 소식에 적힌 Seunghyun의 크롬·엣지 공략(상금 14만 5천 달러), 구글 커널·V8 버그 바운티, 마이크로소프트 보안대응센터(MSRC) 2026 Most Valuable Researchers 선정(구성원 4명) 등이다.[^home]

첫 번째 갈래는 **퍼징과 바이너리 분석으로 버그 찾기**다. 웹어셈블리 실행 환경의 컴파일러 규칙을 뽑아 시험 입력을 만드는 퍼저로 새 버그 20개를 찾았고,[^p1] 디컴파일된 코드 위에서 분석 규칙을 쓰는 기호 분석(입력을 기호로 두고 가능한 실행 경로를 따지는 분석) 도구로 윈도 커널 등에서 버그 15개를 찾아 마이크로소프트 버그 바운티 18만 달러를 받았다.[^p2]

두 번째 갈래는 **운영체제 보안**이다. 리눅스 커널 공격의 핵심 단계인 교차 캐시 공격(커널 메모리의 한 저장 구역에서 풀린 공간을 다른 구역의 객체로 다시 채워 덮어쓰는 공격)을 분석해 성공률을 크게 높인 전략과 자동화 도구를 제시했고,[^p3] 윈도 파일 시스템 설계의 약점이 실제 취약점으로 이어지는 구조를 분석했다.[^p4]

세 번째 갈래는 **이동통신 베이스밴드 보안**이다. 삼성·미디어텍 베이스밴드의 무결성 보호(통신 메시지가 중간에 바뀌지 않았는지 확인하는 장치) 구현을 분석해 버그 29개를 찾았고,[^p5] 무선으로 베이스밴드 하위 계층을 시험하는 공동 연구로 상용 칩 15종에서 메모리 오류 9개를 찾았다.[^p6]

네 번째 갈래는 **사회 기반 소프트웨어 보안과 AI 기반 자동 수정**이다. 국내 금융 서비스 이용자에게 사실상 의무였던 보안 프로그램(KSA 2.0)의 취약점 19개를 찾아 보고한 공동 연구,[^p7] 여러 LLM 에이전트를 묶어 퍼징이 찾은 취약점을 계속 고치는 시스템을 발표했다.[^p8]

## 주요 연구 주제

### 1. 퍼징과 바이너리 분석

웹어셈블리 퍼저, 디컴파일 코드 기호 분석.[^p1][^p2] 대표 논문 1, 2.

### 2. 운영체제 커널·파일 시스템 보안

리눅스 교차 캐시 공격, 윈도 파일 시스템 설계 약점.[^p3][^p4] 대표 논문 3, 4.

### 3. 이동통신 베이스밴드 보안

무결성 보호 비교 분석, 하위 계층 무선 시험.[^p5][^p6] 대표 논문 5, 6.

### 4. 사회 기반 소프트웨어 보안과 AI 자동 수정

금융 보안 프로그램 분석, LLM 에이전트 취약점 수정.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문에서 주제별로 골랐다. 6과 7은 교수가 공저자로 참여한 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [RGFuzz: Rule-Guided Fuzzer for WebAssembly Runtimes](https://doi.org/10.1109/sp61157.2025.00003) · IEEE S&P 2025 | 웹어셈블리 실행 환경에 들어 있는 컴파일러는 복잡한 최적화 규칙 때문에 기존 시험 도구로는 버그를 잘 못 찾는다. 실행 환경(wasmtime)에서 컴파일러 규칙을 뽑아 시험 입력 생성에 쓰고, 입력을 다양하게 만드는 방법을 더한 차분 퍼저(같은 입력을 여러 프로그램에 넣어 결과 차이로 버그를 찾는 도구) RGFuzz로 엔진 6종에서 새 버그 20개(CVE, 즉 공개 등록된 보안 취약점 1건 포함)를 찾았다.[^p1] | 1저자 Junyoung Park, 마지막 저자 윤인수 |
| 2 | 2023 | [QueryX: Symbolic Query on Decompiled Code for Finding Bugs in COTS Binaries](https://doi.org/10.1109/sp46215.2023.10179314) · IEEE S&P 2023 | 소스 코드 없이 기계어만 있는 프로그램에서, 분석가가 디컴파일된 코드 위에 직관적인 규칙을 써서 기호 분석으로 버그를 찾게 하는 QueryX를 만들었다. 윈도 커널·시스템 서비스·자동차 바이너리에 적용해 CVE 10건을 포함한 버그 15개를 찾고 마이크로소프트 버그 바운티로 18만 달러를 받았다.[^p2] | 1저자 HyungSeok Han, 마지막 저자 윤인수 |
| 3 | 2025 | [CROSS-X: Generalized and Stable Cross-Cache Attack on the Linux Kernel](https://doi.org/10.1145/3719027.3765152) · ACM CCS 2025 | 리눅스 커널 공격에 널리 쓰이지만 불안정하다고 여겨지던 교차 캐시 공격을 분석해, 두 가지 최적화 전략과 알맞은 목표 객체를 자동으로 찾는 시스템을 제시했다. 합성 취약점 1개와 실제 취약점 9개에서 시스템이 한가할 때 99% 넘게, 바쁠 때 85% 넘게 성공했다.[^p3] | 1저자 Dongok Kim, 마지막 저자 윤인수 |
| 4 | 2025 | [Windows plays Jenga: Uncovering Design Weaknesses in Windows File System Security](https://doi.org/10.1145/3719027.3765217) · ACM CCS 2025 | 윈도 파일 시스템을 악용한 권한 상승 공격이 거듭되는데, 마이크로소프트는 근본 재설계 대신 개별 패치로 대응해 왔다. 윈도와 리눅스의 차이가 실제 응용의 취약점으로 이어지는 과정을 분석해 고위험 취약점 13개(새로 찾은 11개 포함)를 밝혔고, 프로그래밍 언어 6종의 호환 계층(운영체제마다 다른 파일 시스템 동작을 감춰 주는 언어 내부 장치)과 개발자 21명 조사로 대응이 부족함을 보였다.[^p4] | 1저자 Dong-uk Kim, 마지막 저자 윤인수 |
| 5 | 2023 | [BaseComp: A Comparative Analysis for Integrity Protection in Cellular Baseband Software](https://pure.kaist.ac.kr/en/publications/basecomp-a-comparative-analysis-for-integrity-protection-in-cellular-baseband-software/) · USENIX Security 2023 | 이동통신에서 가장 중요한 단계인 무결성 보호를 베이스밴드 소프트웨어가 규격대로 구현했는지 확률 추론과 기호 분석으로 따지는 반자동 방법 BaseComp를 만들었다. 삼성·미디어텍 펌웨어 16개와 공개 소프트웨어(srsRAN)에서 버그 29개를 찾았고, 그중 삼성의 인증 우회 취약점은 치명 등급을 받았다.[^p5] | 1저자 Eunsoo Kim, 마지막 저자 윤인수 |
| 6 | 2025 | [LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers](https://hacking.kaist.ac.kr/publication/hoang-llfuzz/) · USENIX Security 2025 | 원격으로 악용될 수 있는 베이스밴드 메모리 오류 가운데 덜 연구된 하위 계층(PDCP, RLC, MAC, PHY)을 무선으로 시험하는 LLFuzz를 만들었다. 채널과 설정을 바꿔 가며 규격에 맞는 시험 입력을 만들어, 5개 제조사의 상용 베이스밴드 15종에서 알려지지 않은 메모리 오류 9개를 찾았다.[^p6] | 1저자 Tuan Dinh Hoang, 공저 윤인수, 마지막 저자 Yongdae Kim |
| 7 | 2025 | [Too Much of a Good Thing: (In-)Security of Mandatory Security Software for Financial Services in South Korea](https://pure.kaist.ac.kr/en/publications/too-much-of-a-good-thing-in-security-of-mandatory-security-software-for-financial-services-in-south-korea/) · USENIX Security 2025 | 2023년 북한발 해킹에 악용된 국내 금융 보안 프로그램(KSA 2.0)을 조사해 키 입력 가로채기, 중간자 공격, 원격 코드 실행 등으로 이어지는 취약점 19개를 찾아 정부와 업체에 알렸고 패치됐다. 이용자 400명 설문에서 은행 서비스 이용자의 97%가 설치했지만 59%는 기능을 몰랐고, 사용자 48명의 컴퓨터에는 평균 9개가 깔려 있었다.[^p7] | 1저자 Taisic Yun, 공저 윤인수, 마지막 저자 Yongdae Kim |
| 8 | 2026 | [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://hacking.kaist.ac.kr/publication/kim-patchisland/) · ACSAC 2026(게재 예정) | 지속적 퍼징이 찾은 많은 취약점을 고치는 일은 아직 대부분 손으로 한다. 여러 LLM 에이전트를 묶어 다양한 프로젝트·버그·언어에 대응하고 중복 충돌과 패치를 걸러 내는 PatchIsland를 만들어 내부 평가에서 취약점 92개 중 84개를 고쳤다. AIxCC 결선에서는 일주일 넘게 스스로 운영하며 43개 중 31개를 고쳐, 참가 시스템 가운데 가장 많은 패치를 냈다.[^p8] | 1저자 Wonyoung Kim, 마지막 저자 윤인수 |

## 교수와 전문 분야

윤인수 교수는 미국 조지아공대에서 박사(2020)를 받았고 KAIST 전기및전자공학부 교수로 해킹 연구실을 이끈다. 학부는 연구 분야를 보안, 소프트웨어 시스템과 네트워킹으로, 대표 업적으로 힙 공격 기법 자동 발견(USENIX Security 2020), 하이브리드 퍼징용 기호 실행 엔진 QSYM(USENIX Security 2018), API 사용 오류 검사 APISan(USENIX Security 2016)을 든다.[^ee] 랩 소식에 따르면 QSYM은 2023년 ICSB(랩 표기)에서 Frontiers of Science Award를 받았다.[^home]

논문으로 보면 전문 분야는 세 갈래다.

- **퍼징·기호 분석 기반 취약점 발견**.[^p1][^p2][^p6]
- **운영체제·통신 소프트웨어 보안 분석**.[^p3][^p4][^p5][^p7]
- **LLM 에이전트를 이용한 자동 취약점 수정**.[^p8]

## 응용 분야

대표 논문과 소식으로 보면 웹 브라우저와 실행 환경, 운영체제, 휴대폰 통신 칩, 금융 보안 소프트웨어의 취약점 발견과 수정, 오픈소스 보안 자동화에 닿아 있다.[^p1][^p4][^p5][^p8][^home] 졸업생은 삼성반도체·삼성리서치, 엔키화이트햇, 티오리, 금융보안원, S2W 등 보안 기업과 기관, 조지아공대 박사후연구원으로 갔다고 랩이 적는다.[^members]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Donghyeon Kim | 박사과정 |  |
| Dongjun Lee | 박사과정 |  |
| Eunkyu Lee | 박사과정 |  |
| Gunhee Ahn | 박사과정 |  |
| Haein Lee | 박사과정 | 8 |
| JunYoung Park | 박사과정 | 1, 4 |
| Minwoo Baek | 박사과정 | 5, 8 |
| Sujin Han | 박사과정 |  |
| Ga-eun Bae | 석사과정 |  |
| Gyumin Baek | 석사과정 |  |
| Junghoon Cho | 석사과정 |  |
| Kyeongmin Kim | 석사과정 |  |
| Minwoo Jeong | 석사과정 |  |
| Seoyeon Oh | 석사과정 |  |
| Sungjun Park | 석사과정 |  |

## 졸업생

랩 구성원 페이지 졸업생 구간의 이름, 학위·연도, 랩이 적은 진로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Juhyun Song | 석사 (2026) | Samsung Semiconductor |
| Hyeon Heo | 석사 (2025) | ENKI WhiteHat |
| Seunggi Min | 석사 (2025) | Financial Security Institute |
| Wonyoung Kim | 석사 (2025) | Samsung Research |
| Dong-uk Kim | 석사 (2025) | PK Security |
| Dongok Kim | 석사 (2025) | ENKI WhiteHat |
| Taisic Yun | 석사 (2024) | Theori |
| Wonyoung Jung | 석사 (2024) | 78ResearchLab |
| HyungSeok Han | 박사 (2023) | Postdoc at Georgia Tech |
| Hyunsik Jeong | 석사 (2021) | S2W |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021년 이후 28편이다. 해킹 대회·보안 학회 발표(TyphoonCon, POC)도 랩 목록대로 실었다.[^papers]

**2026**

- Wonyoung Kim, Seunggi Min, Minjae Gwon, Haein Lee, Dowoo Baik, Hyeon Heo, Minjae Lee, Min Woo Baek, Yonghwi Jin, Younggi Park, Yunjae Choi, Taesoo Kim, Sangdon Park, Insu Yun. "PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair (to appear)". *Proceedings of the 42nd Annual Computer Security Applications Conference (ACSAC)*.
- Kyeongmin Kim, Insu Yun. "MTEscape: Bypassing Asynchronous Kernel MTE via Conventional Memory Corruption Vulnerabilities (to appear)". *Proceedings of the 33rd ACM Conference on Computer and Communications Security (CCS)*.
- Yunjae Choi, Min Woo Baek, Insu Yun. "Prism: A Multi-Team Orchestration of LLM Agents for Automatic Program Repair (to appear)". *Proceedings of the 2026 International Symposium on Research in Attacks, Intrusions and Defenses (RAID)*.
- Seoyeon Oh, Juhyun Song, Jaemin Park, Kwanghee Lee, Minae Hyeon, Minji Kim, Sehyuk Ka, Gwangwun Jung, Brian Pak, Insu Yun. "QueryHouse: Cross-DBMS Differential Testing with LLM and Query Transpilation (to appear)". *Proceedings of the 31st European Symposium on Research in Computer Security (ESORICS)*.
- Dongjun Lee, Ga-eun Bae, Insu Yun. "CTFusion: A CTF-based Benchmark for LLM Agent Evaluation". *Proceedings of the Second Workshop on Agents in the Wild: Safety, Security, and Beyond (ICML AIWILD)*.
- Insu Yun, Eunkyu Lee. "Function-Level Fuzzing for RTOS Kernels with RTCon". *Proceedings of the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST) Tutorial*.
- Eunkyu Lee, Junyoung Park, Insu Yun. "RTCon: Context-Adaptive Function-Level Fuzzing for RTOS Kernels". *Proceedings of the 2026 Annual Network and Distributed System Security Symposium (NDSS)*.

**2025**

- CheolJun Park, Marc Egli, Beomseok Oh, Tuan Dinh Hoang, Suhwan Jeong, Martin Crettol, Insu Yun, Mathias Payer, Yongdae Kim. "OTABase: Enhancing Over-the-Air Testing to Detect Memory Crashes in Cellular Basebands". *Proceedings of the 41st Annual Computer Security Applications Conference (ACSAC)*.
- Dong-uk Kim, Junyoung Park, Sanghak Oh, Hyoungshick Kim, Insu Yun. "Windows plays Jenga: Uncovering Design Weaknesses in Windows File System Security". *Proceedings of the 32nd ACM Conference on Computer and Communications Security (CCS)*.
- Dongok Kim, Juhyun Song, Insu Yun. "CROSS-X: Generalized and Stable Cross-Cache Attack on the Linux Kernel". *Proceedings of the 32nd ACM Conference on Computer and Communications Security (CCS)*.
- Jihee Park, Insu Yun, Sukyoung Ryu. "Bridging the Gap between Real-World and Formal Binary Lifting through Filtered-Simulation". *Proceedings of the ACM SIGPLAN International Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA) 2025*.
- Taesoo Kim, HyungSeok Han, Soyeon Park, Dae R. Jeong, Dohyeok Kim, Dongkwan Kim, Eunsoo Kim, Jiho Kim, Joshua Wang, Kangsu Kim, Sangwoo Ji, Woosun Song, Hanqing Zhao, Andrew Chin, Gyejin Lee, Kevin Stevens, Mansour Alharthi, Yizhuo Zhai, Cen Zhang, Joonun Jang, Yeongjin Jang, Ammar Askar, Dongju Kim, Fabian Fleischer, Jeongin Cho, Junsik Kim, Kyungjoon Ko, Insu Yun, Sangdon Park, Dowoo Baik, Haein Lee, Hyeon Heo, Minjae Gwon, Minjae Lee, Minwoo Baek, Seunggi Min, Wonyoung Kim, Yonghwi Jin, Younggi Park, Yunjae Choi, Jinho Jung, Gwanhyun Lee, Junyoung Jang, Kyuheon Kim, Yeonghyeon Cha, Youngjoon Kim. "ATLANTIS: AI-driven Threat Localization, Analysis, and Triage Intelligence System". *(랩 목록에 게재처 표기 없음)*.
- Taisic Yun, Suhwan Jeong, Yonghwa Lee, Seungjoo Kim, Hyoungshick Kim, Insu Yun, Yongdae Kim. "Too Much of a Good Thing: (In-)Security of Mandatory Security Software for Financial Services in South Korea". *Proceedings of the 34th USENIX Security Symposium (Security)*.
- Tuan Dinh Hoang, Taekkyung Oh, CheolJun Park, Insu Yun, Yongdae Kim. "LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers". *Proceedings of the 34th USENIX Security Symposium (Security)*.
- Suhwan Jeong, Beomseok Oh, Kwangmin Kim, Insu Yun, Yongdae Kim, CheolJun Park. "FirmState: Bringing Cellular Protocol States to Shannon Baseband Emulation". *Proceedings of the 18th ACM Conference on Security and Privacy in Wireless and Mobile Networks (WiSec)*.
- Sujin Han, Jinseo Kim, Sung-Ju Lee, Insu Yun. "Automated Attack Synthesis for Constant Product Market Makers". *Proceedings of the ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA) 2025*.
- Junyoung Park, Yunho Kim, Insu Yun. "RGFuzz: Rule-Guided Fuzzer for WebAssembly Runtimes". *Proceedings of the 46th IEEE Symposium on Security and Privacy (Oakland)*.

**2024**

- Haein Lee, Insu Yun. "From the Vulnerability to the Victory: A Chrome Renderer 1-Day Exploit’s Journey to v8CTF Glory". *TyphoonCon 2024*.

**2023**

- Dongok Kim, Seunghyun Lee, Insu Yun. "One shot, Triple kill: Pwning all three Google kernelCTF instances with a single 1-day Linux vulnerability". *POC 2023*.
- Eunsoo Kim, Min Woo Baek, CheolJun Park, Dongkwan Kim, Yongdae Kim, Insu Yun. "BaseComp: A Comparative Analysis for Integrity Protection in Cellular Baseband Software". *Proceedings of the 32nd USENIX Security Symposium (Security)*.
- HyungSeok Han, JeongOh Kyea, Yonghwi Jin, Jinoh Kang, Brian Park, Insu Yun. "QueryX: Symbolic Query on Decompiled Code for Finding Bugs in COTS Binaries". *Proceedings of the 44th IEEE Symposium on Security and Privacy (Oakland)*.

**2022**

- Juhyeng Han, Insu Yun, Seongmin Kim, Taesoo Kim, Sooel Son, Dongsu Han. "Scalable and Secure Virtualization of HSM with ScaleTrust". *IEEE/ACM Transactions on Networking (ToN)*.
- Daehee Jang, Ammar Askar, Insu Yun, Stephen Tong, Yiqin Cai, Taesoo Kim. "Fuzzing@Home: Distributed Fuzzing on Untrusted Heterogeneous Clients". *Proceedings of the 2022 International Symposium on Research in Attacks, Intrusions and Defenses (RAID)*.
- CheolJun Park, Sangwook Bae, Beomseok Oh, Jiho Lee, Eunkyu Lee, Insu Yun, Yongdae Kim. "DoLTEst: In-depth Downlink Negative Testing Framework for LTE Devices". *Proceedings of the 31th USENIX Security Symposium (Security)*.

**2021**

- Insu Yun, Woosun Song, Seunggi Min, Taesoo Kim. "HardsHeap: A Universal and Extensible Framework for Evaluating Secure Allocators". *Proceedings of the 28th ACM Conference on Computer and Communications Security (CCS)*.
- Brian Wickman, Hong Hu, Insu Yun, Daehee Jang, Jungwon Lim, Sanidhya Kashyap, Taesoo Kim. "Preventing Use-After-Free Attacks with Fast Forward Allocation". *Proceedings of the 30th USENIX Security Symposium (Security)*.
- Hyunsik Jung, Insu Yun, Yongdae Kim. "Analyzing Qualcomm Hexagon Emulators via Differential Testing". *Proceedings of the Conference on Information Security and Cryptography Summer(CISC-S) 2021*.
- Eunsoo Kim, Dongkwan Kim, CheolJun Park, Insu Yun, Yongdae Kim. "BaseSpec: Comparative Analysis of Baseband Software and Cellular Specifications for L3 Protocols". *Proceedings of the 2021 Annual Network and Distributed System Security Symposium (NDSS)*.

## 소식

랩 첫 화면의 소식 목록이다.[^home]

- 2026-09-16 · QueryHouse wins the Best Paper Award Runner-up at ESORICS ‘26!
- 2026-09-09 · PatchIsland is accepted to ACSAC ‘26!
- 2026-08-29 · MTEscape is accepted to CCS ‘26!
- 2026-08-09 · Team 0x4b52 wins 2nd place at DEF CON CTF 34 Finals!
- 2026-07-24 · Four members of our lab are named Microsoft MSRC 2026 Most Valuable Researchers!
- 2026-07-10 · Prism is accepted to RAID ‘26!
- 2026-06-12 · QueryHouse is accepted to ESORICS ‘26!
- 2026-05-30 · “Should Opt-Out Depend on Where You Live? Comparing Mobile Privacy Choices Across Jurisdictions” accepted to HotPETS ‘26
- 2026-05-22 · CTFusion is accepted to the Agents in the Wild workshop at ICML ‘26!
- 2025-12-05 · RTCon is accepted to NDSS ‘26
- 2025-09-03 · OTABase is accepted to ACSAC ‘25!
- 2025-08-21 · Two papers got accepted to CCS ‘25
- 2025-08-09 · Team Atlanta wins AIxCC!
- 2025-05-30 · LLFuzz is accepted to USENIX Security ‘25!
- 2025-04-28 · FirmState is accepted to WiSec ‘25!
- 2025-03-31 · CPMM-Exploiter is accepted to ISSTA ‘25!
- 2024-12-30 · Security analysis of mandatory security software in South Korea is accepted to USENIX Security ‘25!
- 2024-12-19 · FIBLE is accepted to OOPSLA ‘25!
- 2024-09-10 · RGFuzz is accepted to IEEE S&P ‘25!
- 2024-08-11 · Team Atlanta proceeds to the AIxCC final!
- 2024-03-22 · Seunghyun won Pwn2Own 2024 by exploiting Google Chrome and Microsoft Edge ($145K)!
- 2024-01-25 · $10K Bug Bounty from Google v8CTF (V8/CVE-2023-6702).
- 2023-10-25 · We got 2nd place in cyber security challenge 2023!
- 2023-10-04 · $67K Bug Bounty from Google kernelCTF (Linux/CVE-2023-3390).
- 2023-07-17 · QSYM got a Frontiers of Science Award from ICSB!
- 2023-06-06 · BaseComp is accepted to Usenix Security'23!
- 2023-01-19 · $7K Bug Bounty from Google (V8/CVE-2023-0696).
- 2022-11-11 · QueryX is accepted to IEEE S&P'23!
- 2022-11-04 · ScaleTrust is accepted to ToN'22!
- 2022-06-11 · FuzzCoin is accepted to RAID'22!
- 2021-09-04 · DoLTEst is conditionally accepted to Usenix Security'22!
- 2021-07-21 · HardsHeap is conditionally accepted to CCS'21!

## 연락과 위치

- 교수 이메일: insuyun@kaist.ac.kr, 교내 전화 7469[^ee]
- 위치: KAIST 김병호·김삼열 IT융합빌딩(N1) 812호 (대전 유성구 대학로 291)[^ee]

[^home]: 해킹 연구실 누리집 첫 화면(소식) <https://hacking.kaist.ac.kr/> (2026-10-19 열람)
[^members]: 해킹 연구실 구성원 페이지 <https://hacking.kaist.ac.kr/people/> (2026-10-19 열람)
[^papers]: 해킹 연구실 논문 목록 <https://hacking.kaist.ac.kr/publication/> (2026-10-19 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(Yun, Insu) <https://ee.kaist.ac.kr/en/professor/17988/> (2026-10-19 열람)
[^p1]: J. Park, Y. Kim, I. Yun, 2025 IEEE Symposium on Security and Privacy (SP), 920-938 (2025). <https://doi.org/10.1109/sp61157.2025.00003> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: H. Han 외, I. Yun, 2023 IEEE Symposium on Security and Privacy (SP), 3279-3295 (2023). <https://doi.org/10.1109/sp46215.2023.10179314> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: D.-o. Kim, J. Song, I. Yun, Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 216-230 (온라인 2025-11-22). <https://doi.org/10.1145/3719027.3765152> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: D.-u. Kim 외, I. Yun, Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 3900-3914 (온라인 2025-11-22). <https://doi.org/10.1145/3719027.3765217> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: E. Kim 외, I. Yun, Proceedings of the 32nd USENIX Security Symposium (Security) (2023). <https://pure.kaist.ac.kr/en/publications/basecomp-a-comparative-analysis-for-integrity-protection-in-cellu/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p6]: T. D. Hoang 외, Y. Kim, Proceedings of the 34th USENIX Security Symposium (Security) (2025). <https://hacking.kaist.ac.kr/publication/hoang-llfuzz/> 초록 기준(논문 페이지 게시 초록).
[^p7]: T. Yun 외, Y. Kim, Proceedings of the 34th USENIX Security Symposium (Security) (2025). <https://pure.kaist.ac.kr/en/publications/too-much-of-a-good-thing-in-security-of-mandatory-security-softwa/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p8]: W. Kim 외, I. Yun, Proceedings of the 42nd Annual Computer Security Applications Conference (ACSAC) (2026). <https://hacking.kaist.ac.kr/publication/kim-patchisland/> 초록 기준(논문 페이지 게시 초록).

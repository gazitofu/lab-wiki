# 프로그래밍 시스템 연구실 (Prosys Lab)

**KAIST 전산학부·정보보호대학원 · 허기홍 교수**

- 분야: 프로그램 분석(프로그램을 실행하지 않거나 실행해 보며 오류를 찾는 기술), 소프트웨어 보안 취약점 탐지, 퍼징(무작위에 가까운 입력으로 오류를 찾는 시험 기법), 컴파일러 정확성 검증, 프로그램 합성, 대형 언어 모델(LLM)을 쓰는 신뢰할 수 있는 코딩 에이전트
- 대분야: 컴퓨팅·AI
- 태그: 프로그램 분석·검증[^research][^p3][^p6], 퍼징[^p2][^p7], 소프트웨어·시스템 보안[^p1], 대형 언어 모델[^research][^p8]
- 홈페이지: <https://prosys.kaist.ac.kr/>
- 근거와 출처: [프로그래밍 시스템 연구실 근거 페이지](prosys-sources.md)

> 소프트웨어 속 깊이 숨은 오류와 보안 취약점을 자동으로 찾고 고치는 도구를 만드는 연구실이다. 프로그래밍 언어 이론과 인공지능을 함께 써서, 컴파일러(사람이 쓴 코드를 기계어로 바꾸는 프로그램)가 바르게 동작하는지 확인하고 AI가 만든 코드도 믿고 쓸 수 있게 하는 기술을 연구한다.[^home][^cslab]

## 무엇을 연구하나

연구실은 안전하고 믿을 수 있는 소프트웨어를 위한 차세대 프로그래밍 시스템을 연구한다고 소개한다. 깊은 의미상의 버그를 찾는 AI 기반 프로그램 분석 시스템, 안전하고 효율적인 소프트웨어를 위한 범용 프로그램 단순화 시스템, 소프트웨어를 자동으로 만들고 고치는 프로그램 합성 시스템을 실제로 만든다.[^home] 전산학부 연구실 소개는 소프트웨어의 심각한 오류를 자동으로 찾아 고치는 기술, 용도에 맞게 프로그램을 자동으로 바꾸거나 만드는 기술, 더 편리한 프로그래밍 환경을 연구하고, 그 바탕인 프로그래밍 언어·분석 이론과 인공지능 기법을 탐구한다고 적는다.[^cslab] 연구 페이지는 연구를 프로그램 분석, 컴파일러 정확성, 소프트웨어 개발을 위한 에이전트형 AI 세 분야로 나눈다.[^research]

첫 번째 갈래는 **프로그램 분석과 취약점·버그 탐지**다. 연구실은 정적 분석(실행하지 않고 코드를 따져 보는 분석), 동적 분석(실행하며 관찰하는 분석), AI를 결합해 분석 능력을 크게 끌어올리는 것을 목표로 한다.[^research] 코드 모양은 달라도 같은 위험 동작을 공유하는 취약점을 찾아 새 취약점 281개를 찾았고,[^p1] 프로그램의 특정 지점을 겨냥하는 퍼징 도구,[^p2] 정적 분석 경보에서 진짜 버그를 앞세우는 학습 방법,[^p3] 오류 위치를 더 정확히 짚는 방법,[^p4] 특정 위치의 예외를 일으키는 단위 테스트를 자동으로 만드는 도구를 개발했다.[^p5]

두 번째 갈래는 **컴파일러 정확성**이다. LLVM(여러 언어가 함께 쓰는 컴파일러 기반)과 V8(크롬의 JavaScript 엔진) 같은 널리 쓰이는 최적화 컴파일러가 코드를 바르게 번역하는지 엄밀한 번역 검증과 효율적인 퍼징을 결합해 확인한다.[^research] 크롬 브라우저의 JavaScript 엔진 V8의 JIT 컴파일러를 검증하는 도구를 만들었고,[^p6] 최신 LLVM에서 잘못된 최적화 버그 55개를 찾았다.[^p7] 교수는 이 V8 검증 연구로 2024년 아마존 연구상(Amazon Research Award)을 받았다.[^gsis]

세 번째 갈래는 **소프트웨어 개발을 위한 신뢰할 수 있는 AI**다. 프로그램 분석과 대형 언어 모델을 함께 써서 자동 코드 생성과 모바일 에이전트 같은 중요한 작업에서 AI 시스템의 견고성과 신뢰성을 보장하려 한다.[^research] 자연어로 쓴 요구에서 형식 명세를 뽑아내 AI가 만든 코드를 검사할 기준을 만드는 시스템을 발표했다.[^p8]

## 주요 연구 주제

### 1. 프로그램 분석과 버그·취약점 탐지

취약점 서명(같은 위험 동작을 나타내는 코드 특징) 분석, 지향성 퍼징, 경보 확률 모델, 오류 위치 추정, 표적 단위 테스트 합성.[^p1][^p2][^p3][^p4][^p5] 대표 논문 1–5.

### 2. 컴파일러 정확성

V8 JIT 번역 검증, 최적화 지향 컴파일러 퍼징.[^p6][^p7] 대표 논문 6, 7.

### 3. 신뢰할 수 있는 AI 코딩

자연어 의도에서 형식 명세 추출.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 교수가 마지막 저자인 것을 중심으로 주제별로 골랐다. 2는 교수가 공저자로 참여한 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2022 | [Tracer: Signature-based Static Analysis for Detecting Recurring Vulnerabilities](https://pure.kaist.ac.kr/en/publications/tracer-signature-based-static-analysis-for-detecting-recurring-vu/) · ACM CCS 2022 | 개발자가 같은 코드를 재사용하거나 같은 실수를 하면 비슷한 취약점이 되풀이된다. 코드 모양이 달라도 같은 위험 동작을 공유하는 취약점을 찾기 위해, 알려진 취약점에서 외부 입력이 위험한 곳까지 흘러가는 흔적을 뽑아 서명으로 모으고 새 프로그램의 흔적과 비교하는 TRACER를 만들었다. Debian의 C/C++ 패키지 273개에서 알려지지 않은 취약점 281개를 찾았고 그중 6개에 CVE 번호(공개 등록된 보안 취약점 번호)가 붙었다.[^p1] | 1저자 Wooseok Kang, 마지막 저자 허기홍 |
| 2 | 2023 | [DAFL: Directed Grey-box Fuzzing Guided by Data Dependency](https://pure.kaist.ac.kr/en/publications/dafl-directed-grey-box-fuzzing-guided-by-data-dependency/) · USENIX Security 2023 | 프로그램의 특정 지점을 겨냥하는 지향성 퍼징은 프로그램이 복잡하면 잘 확장되지 않는다. 목표와 관련된 코드 부분에서만 실행 범위 정보를 얻고, 데이터 흐름을 고려해 입력이 목표에 얼마나 가까운지 정밀하게 계산하는 DAFL을 만들었다. 실제 버그 41개에서 기존 도구들보다 더 많은 버그를 찾았고, 비교한 지향성 퍼저 3종보다 평균 4.99배 이상 빨랐다.[^p2] | 1저자 Tae Eun Kim, 공저 허기홍, 마지막 저자 Sang Kil Cha |
| 3 | 2022 | [Learning Probabilistic Models for Static Analysis Alarms](https://doi.org/10.1145/3510003.3510098) · ICSE 2022 | 정적 분석은 경보를 많이 내 사람이 일일이 확인하기 어렵다. 기존 확률 모델은 구조가 고정돼 다른 프로그램으로 지식을 옮기지 못하고 진짜 버그를 잘못 감추기도 했다. 버그 표시가 있는 학습 프로그램으로 모델의 구조와 가중치를 함께 배우는 BayeSmith를 만들어, 세 가지 확률 추론 시스템의 성능을 크게 높였다.[^p3] | 1저자 Hyunsu Kim, 마지막 저자 허기홍 |
| 4 | 2025 | [Improving Fault Localization with External Oracle by using Counterfactual Execution](https://doi.org/10.1145/3695997) · ACM TOSEM | 프로그램이 맞게 동작했는지를 밖에서 끝에만 판정할 수 있으면 오류 위치를 짚기 어렵다. 분기 조건을 참이나 거짓으로 고정해 다시 실행해 보는 반사실 실행으로 실패와 무관한 문장을 걸러내는 Flex를 만들어, C와 Java 프로그램에서 기존 오류 위치 추정 기법의 정확도를 평균 24%·22% 높였다.[^p4] | 1저자 Jongchan Park, 마지막 저자 허기홍 |
| 5 | 2025 | [UnitCon: Synthesizing Targeted Unit Tests for Java Runtime Exceptions](https://doi.org/10.1145/3729362) · FSE 2025 | 프로그램의 특정 위치에서 실행 중 예외가 나는지 드러내는 표적 단위 테스트를 자동으로 만드는 UnitCon. 정적 분석으로 후보 테스트의 의미를 미리 짐작해 탐색 범위를 줄이고 순서를 정한다. 기존 도구보다 나았고, 오픈소스 51개 프로젝트의 널 포인터 예외(가리키는 대상이 없는 참조를 쓰다 생기는 오류) 경보를 점검해 알려지지 않은 버그 21개를 찾았다.[^p5] 랩 목록은 이 논문이 우수 논문상(Distinguished Paper Award)을 받았다고 적는다.[^papers] | 1저자 Sujin Jang, 마지막 저자 허기홍 |
| 6 | 2024 | [Translation Validation for JIT Compiler in the V8 JavaScript Engine](https://doi.org/10.1145/3597503.3639189) · ICSE 2024 | V8 JavaScript 엔진의 JIT 컴파일러(TurboFan)가 코드를 의미대로 바르게 번역했는지 논리식 판정기(SMT)로 확인하는 번역 검증기 TurboTV를 만들었다. 검증을 단계로 나누고 퍼저로 만든 많은 함수로 최적화 과정을 시험했으며, LLVM에서 TurboFan으로 이어지는 번역 사슬도 검증해 LLVM의 새 잘못된 번역을 찾았다.[^p6] | 1저자 Seungwan Kwon, 마지막 저자 허기홍 |
| 7 | 2025 | [Optimization-Directed Compiler Fuzzing for Continuous Translation Validation](https://doi.org/10.1145/3729275) · PLDI 2025 | 잘못된 컴파일러 최적화는 예상치 못한 동작과 보안 취약점을 낳는다. 특정 최적화를 일으키는 입력 프로그램을 효율적으로 만드는 지향성 퍼징과 번역 검증을 결합한 Optimuzz를 LLVM과 TurboFan에 적용해 기존 도구보다 잘 찾았고, 최신 LLVM에서 새 잘못된 번역 버그 55개를 발견했다.[^p7] | 1저자 Jaeseong Kwon, 마지막 저자 허기홍 |
| 8 | 2026 | [Expecto: Extracting Formal Specifications from Natural Language Description for Trustworthy Oracles](https://doi.org/10.1145/3808332) · PLDI 2026 | LLM이 자연어 요구로 코드를 만들수록 자연어 명세의 모호함이 문제가 된다. LLM과 프로그램 합성을 결합해 명세 추출을 작은 단위로 나눠 위에서부터 차례로 만드는 Expecto로, 자연어 의도에서 믿을 수 있는 형식 명세를 자동으로 뽑았다. LLM만 쓰는 방식보다 정확했고, 실제 버그 프로그램 모음(Defects4J)에서 비교 대상보다 더 많은 버그를 잡는 명세를 만들었다.[^p8] | 1저자 Dongjae Lee, 마지막 저자 허기홍 |

## 교수와 전문 분야

허기홍 교수는 서울대 컴퓨터공학 학사(2005–2009)와 박사(2009–2017)를 받고, 미국 펜실베이니아대 박사후연구원(2017–2019)을 거쳐 2020년 KAIST 조교수로 부임했다. 지금은 부교수다.[^heo] 전산학부는 교수가 박사 과정 중에 개발한 소프트웨어 오류 검출 기술이 Facebook의 오류 검출기 Infer에 탑재돼 쓰이고 있고, 2019년 PLDI와 ICSE에서 최우수 논문상을 받았다고 소개한다.[^csfac] 전공은 프로그램 분석, 프로그래밍 언어, 소프트웨어 보안이다.[^csfac] 2024년에는 소프트웨어 자동 검증 분야에서 아마존 연구상을 받았다.[^gsis] 강의로는 정보보호개론, 프로그램 추론, 프로그래밍 언어 이론, 프로그램 분석 등을 맡아 왔다.[^heo]

논문으로 보면 전문 분야는 세 갈래다.

- **정적·동적 프로그램 분석과 취약점 탐지**.[^p1][^p2][^p3][^p4][^p5]
- **컴파일러 번역 검증과 컴파일러 퍼징**.[^p6][^p7]
- **프로그램 합성과 LLM 결합 명세 추출**.[^p8]

## 응용 분야

대표 논문과 연구 소개로 보면 소프트웨어 보안 취약점 자동 탐지, 웹 브라우저와 컴파일러의 안전성 검증, AI 코딩 도구의 신뢰성 확보에 닿아 있다.[^p1][^p6][^p8] 졸업생은 KAIST 박사과정 진학 외에 Rebellions, Furiosa AI, Theory 등 기업으로 갔다고 랩이 적는다.[^members]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Yeonhee Ryou (류연희) | 박사과정 | 5 |
| Tae Eun Kim (김태은) | 박사과정 | 2, 4 |
| Sujin Jang (장수진) | 박사과정 | 5 |
| Dongjae Lee (이동재) | 박사과정 | 8 |
| Bongjun Jang (장봉준) | 석사과정 | 7 |
| Hyunbin Kim (김현빈) | 석사과정 |  |

## 졸업생

랩 구성원 페이지의 졸업생과 랩이 적은 진로·수상이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 랩이 적은 수상 |
|---|---|---|---|
| Dongjae Lee (이동재) | M.S. (2026) | KAIST 박사과정 | 전산학부 우수 석사 논문상 |
| Geon Park (박건) | M.S. (2026) |  |  |
| Jaehoon Jang (장재훈) | M.S. (2026) |  |  |
| Changgong Lee (이창공) | M.S. (2025) |  |  |
| Jaeseong Kwon (권재성) | M.S. (2025) | Rebellions |  |
| Sujin Jang (장수진) | M.S. (2024) | KAIST 박사과정 |  |
| Jaeho Kim (김재호) | M.S. (2024) |  |  |
| Jongchan Park (박종찬) | M.S. (2024) | Furiosa AI |  |
| Tae Eun Kim (김태은) | M.S. (2023) | KAIST 박사과정 | 전산학부 우수 석사 논문상 |
| Seungwan Kwon (권승완) | M.S. (2023) | Rebellions | 전산학부 우수 석사 논문상 |
| Wooseok Kang (강우석) | M.S. (2023) | Theory | 전산학부 우수 석사 논문상 |
| Hyunsu Kim (김현수) | M.S. (2022) | Furiosa AI |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021–2026년 논문 12편이다.[^papers]

**2026**

- Dongjae Lee, Kihong Heo. "Expecto: Extracting Formal Specifications from Natural Language Description for Trustworthy Oracles". *PLDI 2026: ACM SIGPLAN Conference on Programming Language Design and Implementation, 2026*.

**2025**

- Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin. "Safeguarding Mobile GUI Agent via Logic-based Action Verification". *MobiCom 2025: International Conference on Mobile Computing and Networking, 2025*.
- Jaeseong Kwon, Bongjun Jang, Juneyoung Lee, Kihong Heo. "Optimization-Directed Compiler Fuzzing for Continuous Translation Validation". *PLDI 2025: ACM SIGPLAN Conference on Programming Language Design and Implementation, 2025*.
- Sujin Jang, Yeonhee Ryou, Heewon Lee, Kihong Heo. "UnitCon: Synthesizing Targeted Unit Tests for Java Runtime Exceptions". *FSE 2025: ACM International Conference on the Foundations of Software Engineering, 2025 (Distinguished Paper Award)*.
- Jongchan Park, Tae Eun Kim, Dongsun Kim, Kihong Heo. "Improving Fault Localization with External Oracle by using Counterfactual Execution". *TOSEM: ACM Transactions on Software Engineering and Methodology, 2025*.

**2024**

- Tae Eun Kim, Jaeseung Choi, Seongjae Im, Kihong Heo, Sang Kil Cha. "Evaluating Directed Fuzzers: Are We Heading in the Right Direction?". *FSE 2024: International Conference on the Foundations of Software Engineering, 2024*.
- Seungwan Kwon, Jaeseong Kwon, Wooseok Kang, Juneyoung Lee, Kihong Heo. "Translation Validation for JIT Compiler in the V8 JavaScript Engine". *ICSE 2024: International Conference on Software Engineering, 2024*.

**2023**

- Tae Eun Kim, Jaeseung Choi, Kihong Heo, Sang Kil Cha. "DAFL: Directed Grey-box Fuzzing Guided by Data Dependency". *Security 2023: USENIX Security Symposium, 2023*.

**2022**

- Wooseok Kang, Byoungho Son, Kihong Heo. "Tracer: Signature-based Static Analysis for Detecting Recurring Vulnerabilities". *CCS 2022: ACM Conference on Computer and Communications Security, 2022*.
- Hyunsu Kim, Mukund Raghothaman, Kihong Heo. "Learning Probabilistic Models for Static Analysis Alarms". *ICSE 2022: International Conference on Software Engineering, 2022 (Best Artifact Award)*.
- Pardis Pashakhanloo, Aravind Machiry, Hyonyoung Choi, Anthony Canino, Kihong Heo, Insup Lee, Mayur Naik. "PacJam: Securing Dependencies Continuously via Package-Oriented Debloating". *ASIACCS 2022: ACM ASIA Conference on Computer and Communications Security, 2022*.

**2021**

- Tianyi Chen, Kihong Heo, Mukund Raghothaman. "Boosting Static Analysis Accuracy With Instrumented Test Executions". *ESEC/FSE 2021: ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, 2021*.

## 수상

- 2025 · FSE 2025 ACM SIGSOFT 우수 논문상(Distinguished Paper Award), UnitCon
- 2022 · ICSE 2022 Best Artifact Award, Learning Probabilistic Models for Static Analysis Alarms
- 2024 · 허기홍 교수, 아마존 연구상(Amazon Research Award), 소프트웨어 자동 검증 분야, 과제 「V8을 위한 생성형 번역 검산」

## 연구실 글

연구실 블로그(Posts)의 글 목록이다. 연구 소개, 학회 참가기, 교수의 연구 단상이 실려 있다.[^posts]

- 2026-09-14 · 호모 엑스플라난스 (글쓴이 김태은)
- 2026-09-12 · 작은 호기심이 연구가 되기까지 (글쓴이 장수진)
- 2026-09-09 · Me and My Ph.D (글쓴이 이동재)
- 2026-07-12 · AI 시대에 PL을 연구하는 대학원생의 고민 (글쓴이 이동재)
- 2026-07-09 · 모두가 자연어의 모호함과 싸우고 있다 (글쓴이 허기홍)
- 2025-11-25 · PL 연구자가 바라본 MobiCom (글쓴이 이동재)
- 2025-11-24 · 안전한 정적 분석과 시대정신 (글쓴이 허기홍)
- 2025-10-15 · Optimuzz: 안전한 컴파일러를 위한 오번역 자동 탐지 기술 (글쓴이 장봉준)
- 2025-09-30 · 몰입을 위한 약속 (글쓴이 허기홍)
- 2025-07-28 · 두 번 가서 배로 좋은 PLDI와 FSE 여행기 (글쓴이 장수진)
- 2025-07-25 · 두 번 생각하는 두 학회 여행기 (글쓴이 류연희)
- 2025-07-03 · 문제가 문제다(1): 하늘을 보아야 별을 딴다 (글쓴이 허기홍)
- 2025-07-03 · 문제가 문제다(2): 높이 올라가야 멀리 보인다 (글쓴이 허기홍)
- 2025-06-30 · 홈그라운드에서 열린 PL 학회 탐방기 (글쓴이 김태은)
- 2025-06-29 · PLDI 2025에 가서 (글쓴이 박건)
- 2025-06-28 · PLDI 데뷔기 (글쓴이 이동재)
- 2025-06-28 · PLDI 2025 여행기 (글쓴이 장봉준)
- 2025-06-26 · 보안쟁이의 PL 학회 생존기 (글쓴이 장재훈)
- 2025-06-25 · 야, 너두 네트워킹 할 수 있어 (글쓴이 김태은)
- 2025-06-12 · 행복한 삶에 이르는 뜻밖의 길 (글쓴이 허기홍)
- 2025-02-04 · 은은하게 퍼지는 쉬운전문용어와 소박한 공부 (글쓴이 허기홍)
- 2024-12-23 · 성적을 보고 서운한 학생에게 (글쓴이 허기홍)
- 2024-08-02 · 그래서 남은 것은 무엇인가? (글쓴이 허기홍)
- 2024-07-29 · 나의 첫 남미 학회 탐방기 (글쓴이 김태은)
- 2024-05-15 · 지향성 퍼징 기술의 최신 동향 (글쓴이 김태은)
- 2024-04-30 · 우연과 인연 (글쓴이 허기홍)
- 2024-04-29 · 나의 첫 소프트웨어 공학 해외 학회 탐방기 (글쓴이 김태은)
- 2024-04-28 · 나의 첫 학회 연구 발표 (글쓴이 권재성)
- 2023-09-11 · USENIX Security 2023 여행기 (글쓴이 류연희)
- 2023-09-10 · 나의 첫 해외학회 탐방기 (글쓴이 박종찬)
- 2023-09-09 · 2023 Usenix Security 를 다녀와서 (글쓴이 장수진)
- 2023-09-07 · 나의 첫 발표하러 간 해외 학회 탐방기 (글쓴이 김태은)
- 2023-08-18 · 장님과 앉은뱅이 (글쓴이 허기홍)
- 2023-07-11 · 2023 PLDI를 다녀와서 (글쓴이 김재호)
- 2023-06-29 · 나의 첫 해외 PL 학회 탐방기 (글쓴이 김태은)
- 2023-03-31 · 내 마음 나도 몰라 (글쓴이 허기홍)
- 2023-03-09 · 구글 버그바운티 카이스트 기부 인터뷰 (글쓴이 권승완)
- 2022-12-08 · CCS 기행문 (글쓴이 강우석)
- 2022-12-02 · 앞으로의 삶 정적 분석하기 (글쓴이 김재호)
- 2022-12-01 · ESEC/FSE 2022 @ 싱가포르 (글쓴이 류연희)
- 2022-11-28 · 2022 ACM CCS 학회를 다녀와서 (글쓴이 권승완)
- 2022-11-25 · 나의 첫 해외 학회 탐방기 (글쓴이 김태은)
- 2022-11-15 · Tracer 의 실패 여정 (글쓴이 허기홍)
- 2022-11-04 · AI, 어떻게 해야 신뢰할 수 있을까? (글쓴이 허기홍)
- 2022-04-15 · 출석체크 (글쓴이 허기홍)
- 2019-12-31 · 환영합니다! (글쓴이 허기홍)
- 2017-06-15 · 박사학위를 받으며 (글쓴이 허기홍)
- 2015-03-18 · 단순한 아름다움 (글쓴이 허기홍)

## 연락과 위치

- 연구실: KAIST 전산학동(N4) 1424호, 전화 042-350-7781[^home][^cslab]
- 교수실: KAIST N5 2321호, 교내 전화 3581[^csfac]

[^home]: 프로그래밍 시스템 연구실 누리집 첫 화면 <https://prosys.kaist.ac.kr/> (2026-10-19 열람)
[^research]: 프로그래밍 시스템 연구실 연구 페이지 <https://prosys.kaist.ac.kr/research/> (2026-10-19 열람)
[^members]: 프로그래밍 시스템 연구실 구성원 페이지 <https://prosys.kaist.ac.kr/members/> (2026-10-19 열람)
[^papers]: 프로그래밍 시스템 연구실 논문 목록 <https://prosys.kaist.ac.kr/publications/> (2026-10-19 열람)
[^posts]: 프로그래밍 시스템 연구실 블로그 글 목록 <https://prosys.kaist.ac.kr/posts/> (2026-10-20 열람)
[^cslab]: KAIST 전산학부 연구실 소개(프로그래밍 시스템 연구실) <https://cs.kaist.ac.kr/research/labView?sn=107&menu=64> (2026-10-19 열람)
[^csfac]: KAIST 전산학부 교수 소개(허기홍) <https://cs.kaist.ac.kr/people/view?idx=598&kind=faculty&menu=160> (2026-10-19 열람)
[^heo]: 허기홍 교수 누리집 <https://kihongheo.kaist.ac.kr/> (2026-10-20 열람)
[^gsis]: KAIST 정보보호대학원 소식 "허기홍 교수, 아마존 연구상 (Amazon Research Award) 수상"(2024-04-25) <https://gsis.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=1412&menu=106> (2026-10-20 열람)
[^p1]: W. Kang, B. Son, K. Heo, ACM Conference on Computer and Communications Security (CCS 2022, 랩 표기). <https://pure.kaist.ac.kr/en/publications/tracer-signature-based-static-analysis-for-detecting-recurring-vu/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p2]: T. E. Kim, J. Choi, K. Heo, S. K. Cha, USENIX Security Symposium (Security 2023, 랩 표기). <https://pure.kaist.ac.kr/en/publications/dafl-directed-grey-box-fuzzing-guided-by-data-dependency/> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p3]: H. Kim, M. Raghothaman, K. Heo, Proceedings of the 44th International Conference on Software Engineering, 1282-1293 (온라인 2022-07-05). <https://doi.org/10.1145/3510003.3510098> 초록 기준(KAIST 연구자 포털 PURE 게시 초록).
[^p4]: J. Park, T. E. Kim, D. Kim, K. Heo, ACM Transactions on Software Engineering and Methodology 34, 1-22 (온라인 2025-01-24). <https://doi.org/10.1145/3695997> 초록 기준.
[^p5]: S. Jang, Y. Ryou, H. Lee, K. Heo, Proceedings of the ACM on Software Engineering 2, 2053-2074 (온라인 2025-06-19). <https://doi.org/10.1145/3729362> 초록 기준.
[^p6]: S. Kwon 외, K. Heo, Proceedings of the IEEE/ACM 46th International Conference on Software Engineering, 1-12 (온라인 2024-04-12). <https://doi.org/10.1145/3597503.3639189> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Kwon, B. Jang, J. Lee, K. Heo, Proceedings of the ACM on Programming Languages 9, 627-650 (온라인 2025-06-13). <https://doi.org/10.1145/3729275> 초록 기준.
[^p8]: D. Lee, K. Heo, Proceedings of the ACM on Programming Languages 10, 2134-2156 (온라인 2026-06-08). <https://doi.org/10.1145/3808332> 초록 기준.

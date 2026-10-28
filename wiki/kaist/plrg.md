# 프로그래밍 언어 연구 그룹 (Programming Language Research Group, PLRG)

**KAIST 전산학부 · 류석영 교수, Endowed Professor**

- 분야: 프로그래밍 언어, 컴파일러, 프로그램 분석, 언어 명세와 구현의 시험, C-to-Rust 변환, 양자 소프트웨어 시험
- 대분야: 컴퓨팅·AI
- 태그: 프로그램 분석·검증[^home][^p2][^p5], 퍼징[^p2], 양자 컴퓨팅[^p7]
- 홈페이지: <https://plrg.kaist.ac.kr/>
- 근거와 출처: [프로그래밍 언어 연구 그룹 근거 페이지](plrg-sources.md)

> 프로그래밍 언어의 규칙을 정밀하게 표현하고, 그 규칙으로 프로그램을 분석·변환·시험해 안전하고 믿을 수 있는 소프트웨어를 만드는 연구 그룹이다.[^home][^lab]

## 무엇을 연구하나

KAIST 전산학부 류석영 교수가 이끄는 프로그래밍 언어 연구 그룹이다.[^faculty][^lab] 연구실은 프로그래밍 언어(컴퓨터가 수행할 동작을 표현하는 언어), 컴파일러(원시 코드를 다른 코드로 번역하는 도구), 프로그램 분석, 프로그래밍 환경을 연구한다. 목표는 프로그래밍 언어 기술로 개발자가 품질 높은 소프트웨어를 만들도록 돕는 것이다. 안전하고 믿을 수 있는 시스템을 위해 타입 시스템(값과 연산의 종류 및 그 사용 규칙을 정하는 체계), 컴파일러의 올바름, 자동 프로그램 분석, 디버깅(오류의 원인을 찾아 고치는 작업)과 시험 도구를 다룬다.[^home][^lab]

첫째는 **언어의 규칙과 구현이 서로 맞는지 확인하는 연구**다. 언어 명세(구문과 실행 의미를 정해 놓은 문서)와 실제 구현이 함께 바뀌는 상황에서는 어느 한쪽을 무조건 정답으로 삼기 어렵다. JEST는 명세에서 프로그램과 검사 조건을 만들고 여러 자바스크립트 실행기의 결과를 비교하는 차등 시험(같은 입력에 대한 여러 구현의 결과를 비교하는 시험)으로 명세와 구현 양쪽의 오류를 찾는다.[^p1] 최근에는 P4(프로그래밍 가능한 네트워크 장치의 동작을 적는 언어)의 타입 규칙을 기계화(규칙을 컴퓨터가 처리할 수 있는 형식으로 표현하는 일)하고, 거부해야 할 프로그램을 만들어 타입 검사기(프로그램이 타입 규칙에 맞는지 판단하는 도구)를 시험한다.[^p2]

둘째는 **WebAssembly의 시험과 오류 재현**이다. WebAssembly(Wasm)는 여러 실행 환경에서 동작하도록 설계된 저수준 명령어 형식이다.[^p3] WEST는 기계화된 명세에서 문법과 검증 규칙을 따르는 시험 프로그램을 만들며, 언어 기능의 일부만 지원하는 실행기도 시험 대상으로 삼는다.[^p3] 오류가 난 프로그램을 개발자가 살펴볼 수 있게 줄이는 연구도 한다. RR-Reduce는 오류를 일으키는 함수를 골라 나머지 프로그램과 주고받은 동작을 기록하고 재생하며, Hybrid-Reduce는 여기에 실행을 고려하지 않는 축소 방법을 결합한다.[^p4]

셋째는 **기존 C 프로그램을 Rust로 자동 변환하는 연구**다. Concrat은 데이터 경쟁(여러 실행 흐름이 같은 메모리 위치에 동기화 없이 접근하고 그중 쓰기가 포함되는 상황)을 막기 위해 쓰는 잠금(공유 자료의 접근을 제어하는 수단)을 다룬다. C 코드의 잠금 사용을 정적 분석(프로그램을 실행하지 않고 성질을 알아내는 방법)으로 정리하고, 이를 Rust의 타입 검사가 적용되는 잠금 함수로 바꾼다.[^p5] Forcrat은 입출력 API(Application Programming Interface, 소프트웨어 기능을 호출하는 약속)를 바꾼다. 자료가 들어오는 곳과 읽기·쓰기 기능, 오류를 확인하는 방식의 차이를 분석해 C의 표준 입출력 함수를 Rust 표준 라이브러리(프로그램에서 불러 쓰도록 제공되는 코드 모음)의 함수로 바꾼다.[^p6]

넷째는 **양자 소프트웨어가 올바르게 계산하는지 시험하는 연구**다. 양자 회로(큐비트에 적용할 연산을 순서와 연결 관계로 나타낸 계산 표현)를 바꾸는 도구와 그 회로를 모의 실행하는 도구가 시험 대상이다. QASMInfer는 회로의 가능한 결과에 대한 확률분포(각 결과가 나타날 확률을 나타낸 것)를 계산해 정답 판정 기준으로 쓴다. 연구진은 그 결과가 양자 계산의 물리 원리와 일치함을 증명하고, 구현과 증명을 Coq 증명 보조기(논리적 증명 과정을 컴퓨터로 작성하고 검사하는 도구)로 기계화했다.[^p7]

## 주요 연구 주제

### 1. 언어 명세와 구현의 일치

명세와 여러 자바스크립트 구현을 함께 시험하는 JEST, P4 타입 규칙에서 거부해야 할 입력을 만드는 시험 생성 연구다. 타입 규칙을 어겼을 때를 시험 대상으로 구분하고, 그 조건을 얼마나 시험했는지 나타내는 지표도 만든다. 정상 프로그램을 잘못된 프로그램으로 바꾸며 시험 범위를 넓히는 퍼저(시험 입력을 자동 생성하거나 변형하며 오류를 찾는 도구)도 개발한다.[^p1][^p2]

### 2. WebAssembly 시험과 오류 재현

명세로부터 시험 프로그램을 생성하는 WEST와, 오류를 유지하면서 프로그램을 줄이는 RR-Reduce·Hybrid-Reduce를 연구한다. 시험 입력을 만드는 과정과 오류가 난 뒤 원인을 살피는 과정을 모두 다룬다.[^p3][^p4]

### 3. C-to-Rust 자동 변환

잠금 함수와 입출력 함수를 분석해 C와 Rust의 서로 다른 사용 규칙을 연결한다. 프로그램의 동작을 보존하면서 Rust의 언어 기능과 표준 라이브러리를 사용하도록 코드를 바꾸는 연구다.[^p5][^p6]

### 4. 양자 소프트웨어의 올바름

양자 회로의 결과 확률을 계산하고 물리 원리와의 일치를 증명해, 회로 변환기와 모의 실행기를 시험하는 공통 정답 판정 기준을 만든다. 실행이 중단되지 않아도 계산 결과가 잘못되는 오류를 찾는 것이 연구 대상이다.[^p7]

## 대표 논문

2021–2026년 논문 가운데 류석영 교수가 저자인 논문을 네 연구 갈래에 걸쳐 골랐다. 2026년 논문 한 편을 포함한다. 류 교수는 논문 4에서 전체 다섯 저자 중 네 번째이고 나머지 여섯 편에서는 마지막 저자다. "쉽게 말하면"은 각 논문의 학회 아카이브 게시 초록을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2021 | [JEST: N+1-version Differential Testing of Both JavaScript Engines and Specification](https://conf.researchr.org/details/icse-2021/icse-2021-papers/43/JEST-N-1-version-Differential-Testing-of-Both-JavaScript-Engines-and-Specification) · ICSE | 명세와 구현이 함께 바뀌면 명세에도 오류가 있을 수 있다. 명세에서 자바스크립트 프로그램을 만들고 실행 뒤 상태를 검사할 조건을 넣어 여러 실행기에서 돌린다. 결과를 비교해 실행기와 명세의 오류를 찾고, 통계 정보로 명세 안의 오류 위치를 좁힌다.[^p1] | 1저자 Jihyeok Park, 마지막 저자 류석영 |
| 2 | 2026 | [Failing with Purpose: Dangling Coverage-Guided Negative Test Generation from a Mechanized P4 Type System](https://doi.org/10.1145/3797109) · FSE | 타입 검사기는 규칙에 맞는 프로그램을 받아들이는 것뿐 아니라 틀린 프로그램을 거부해야 한다. P4의 타입 규칙을 기계가 읽는 형태로 만들고, 어기면 타입 오류가 되는 전제를 찾았다. 그 전제들을 얼마나 시험했는지 재는 지표를 제안하고, 정상 프로그램을 잘못된 프로그램으로 바꾸며 시험 범위를 넓혔다. 생성된 시험으로 컴파일러의 앞단에서 알려지지 않았던 오류를 찾았고 시험들이 P4C의 시험 모음에 통합됐다.[^p2] | 1저자 Jaehyun Lee, 마지막 저자 류석영 |
| 3 | 2025 | [WEST: Specification-Based Test Generation for WebAssembly](https://doi.org/10.1109/ASE63991.2025.00119) · ASE | WebAssembly 명세가 커지거나 일부 기능만 지원하는 실행기를 시험하려면 그에 맞는 입력이 필요하다. WEST는 SpecTec으로 작성된 기계화 명세에서 문법·검증 규칙과 실행 동작에 맞는 시험 프로그램을 자동 생성한다. 여러 입력 생성 전략을 결합할 수 있고, 전체 명세와 부분 명세를 각각 시험할 수 있다. 학회 게시 초록은 다섯 실행기에서 오류 18건을 찾았고 이 중 10건이 확인·수정됐다고 보고한다.[^p3] | 1저자 Dongjun Youn, 마지막 저자 류석영 |
| 4 | 2025 | [Execution-Aware Program Reduction for WebAssembly via Record and Replay](https://doi.org/10.1109/ASE63991.2025.00073) · ASE | 오류를 일으킨 WebAssembly 프로그램에서 같은 오류가 나는 축소본을 만든다. RR-Reduce는 원인 함수와 나머지 프로그램 사이의 상호작용을 기록한 뒤 그 함수만 떼어 재생한다. Hybrid-Reduce는 다른 축소 기법을 함께 써 프로그램 크기를 줄인다. 세 실행기의 오류를 일으키는 프로그램들을 대상으로 크기와 축소 시간을 평가했다.[^p4] | 1저자 Doehyun Baek, 류석영은 5명 중 4번째 |
| 5 | 2023 | [Concrat: An Automatic C-to-Rust Lock API Translator for Concurrent Programs](https://doi.org/10.1109/ICSE48619.2023.00069) · ICSE | C에서 잠금 함수를 쓰던 코드를 Rust로 번역한 뒤에도 C 방식의 잠금이 남는 문제를 다룬다. 정적 분석기가 어떤 자료를 어떤 잠금으로 보호하는지 요약하고, 코드 변환기가 그 정보를 받아 Rust의 잠금 함수로 바꾼다. 프로그램의 의미를 보존하는 변환을 목표로 했고, 실제 프로그램의 74%를 처리했다고 보고한다.[^p5] | 1저자 Jaemin Hong, 마지막 저자 류석영 |
| 6 | 2025 | [Forcrat: Automatic I/O API Translation from C to Rust via Origin and Capability Analysis](https://doi.org/10.1109/ASE63991.2025.00130) · ASE | C와 Rust는 입출력 자료의 출처·읽기·쓰기 기능을 표현하는 종류와 오류 처리 방식이 다르다. 자료의 출처와 가능한 기능, 오류의 출처를 정적 분석해 기존 변환기가 남겨 둔 C 입출력 함수를 Rust 함수로 바꾼다. 시험 모음이 있는 프로그램 32개가 변환 후 모두 시험을 통과했고, 입출력 함수 호출의 82%를 교체했다고 보고한다.[^p6] | 1저자 Jaemin Hong, 마지막 저자 류석영 |
| 7 | 2025 | [Exact Inference for Quantum Circuits: A Testing Oracle for Quantum Software Stacks](https://doi.org/10.1109/ASE63991.2025.00203) · ASE | 양자 회로 변환기와 모의 실행기의 결과를 판정할 기준을 만든다. QASMInfer는 OpenQASM으로 적은 회로의 가능한 결과 확률을 계산한다. 계산 결과가 양자 물리 원리를 따름을 증명하고 Coq에서 구현과 증명을 기계화했다. 학회 게시 초록은 양자 소프트웨어 여섯 개를 시험해 오류 20건을 찾았고 이 중 15건은 실행이 중단되지 않는 오류라고 보고한다.[^p7] | 1저자 Kanguk Lee, 마지막 저자 류석영 |

## 교수와 전문 분야

류석영 교수(Sukyoung Ryu)는 KAIST 전산학부 교수다. 교수진 목록의 직위는 「교수, Endowed Professor」이고 개인 소개는 「KAIST ICT Endowed Chair Professor」로 적는다.[^faculty][^prof] KAIST에서 전산학 학사(1995), 석사(1996), 박사(2001) 학위를 받았다. 2001년 10월–2005년 1월 하버드대학교 공학·응용과학 부문의 Research Associate, 2005년 2월–2009년 11월 Sun Microsystems Laboratories의 Member of Technical Staff로 일했다.[^prof]

개인 소개의 연구 관심은 자바스크립트 분석 체계 SAFE, 의료 영상 처리의 분석과 성능 향상, 규모 확장성과 정확성·실용성을 갖춘 프로그램 분석, 디버깅·시험을 위한 프로그래밍 환경, 프로그래밍 언어와 프로그램 분석을 위한 증명 보조기다.[^prof] 최근 논문에 나타나는 전문 분야는 언어 명세와 구현의 오류 탐지,[^p1][^p2] 명세 기반 시험 생성과 실행 기록을 이용한 오류 재현,[^p3][^p4] 정적 분석을 이용한 프로그램 자동 변환,[^p5][^p6] 양자 회로 결과 계산과 그 올바름 증명이다.[^p7]

학술 활동에는 PLDI의 자바스크립트 명세·도구 튜토리얼(2022)과 실제 프로그래밍 언어의 기계화 명세 튜토리얼(2026), P4 Workshop 발표(2024), P4 Developer Days 발표(2025), Cornell University 전산학 콜로퀴엄 강연(2024), 기술과 사회적 공익을 위한 프로그래밍 언어 연구를 주제로 한 PLDI 기조강연(2025)이 있다.[^pubs]

## 응용 분야

연구의 직접 대상은 자바스크립트와 P4의 언어 구현,[^p1][^p2] WebAssembly 실행기,[^p3][^p4] 기존 C 시스템 소프트웨어의 Rust 전환,[^p5][^p6] 양자 회로 변환기와 모의 실행기다.[^p7] 분석·시험 도구를 개발해 소프트웨어의 규칙 위반과 잘못된 동작을 찾고, 기존 코드를 다른 언어의 기능에 맞게 고치는 데 초점을 둔다.[^home][^p5][^p6]

공개 소프트웨어 목록에는 자바스크립트 with 구문을 고치는 JSWithRewriter, 모듈 기능을 넣은 λJS, Coq로 기계화한 Fortress 언어 모형, ThisJava 컴파일러와 CoreThisJ 해석기, Project Fortress, SML/NJ 예외 분석기가 있다.[^software]

## 구성원

2026년 10월 28일 구성원 명단의 박사후연구원 1명, 석박사통합과정 2명, 박사과정 5명, 석사과정 5명이다. 과정은 명단의 구획을 따랐고, 시작 시점과 연구 주제는 연구실이 게시한 개인 소개를 함께 썼다.[^members][^dongjun][^gyeongwon][^yusung] "대표 논문 참여"는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| 윤동준 (Dongjun Youn) | 박사후연구원 (PhD, 2026) | 학위과정 Mar. 2020 | Declarative languages; Mechanized Specification; Program transformation | 1, 3 |
| 김경원 (Gyeongwon Kim) | 석박사통합과정 | Mar. 2020 | Program Analysis; Software Security | 1 |
| Seokhun Jeong | 석박사통합과정 |  |  | 2 |
| 심유성 (Yusung Sim) | 박사과정 | Mar. 2023 | Programming language specification frameworks; WebAssembly; Rust |  |
| Kanguk Lee | 박사과정 |  |  | 7 |
| Hyerin Park | 박사과정 |  |  |  |
| Seungmin Jeon | 박사과정 |  |  |  |
| Jaehyun Lee | 박사과정 |  |  | 2 |
| Hyunhee Kang | 석사과정 |  |  |  |
| Jeongwon Park | 석사과정 |  |  |  |
| Eunsu Kim | 석사과정 |  |  |  |
| Sehyuk Ahn | 석사과정 |  |  |  |
| Jihun Kim | 석사과정 |  |  |  |

## 졸업생 진로

구성원 페이지 Alumni의 2021–2026년 학위 취득자 11명이다. 학위·연도와 진로는 연구실이 적은 표기를 따랐다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sungjae Hwang | PhD (2021) | Sungkyunkwan University |
| Sangwook Park | MS (2021) | Furiosa AI |
| Joonyoung Park | PhD (2022) | Carillon |
| Jihyeok Park | PhD (2022) | Korea University |
| Seungmin An | MS (2022) | Furiosa AI |
| Jaeho Choi | MS (2024) | Moreh |
| Jaemin Hong | PhD (2025) | UNIST |
| Doehyun Baek | MS (2025) | University of Stuttgart |
| Wonho Shin | MS (2025) |  |
| Jihee Park | PhD (2026) | Furiosa AI |
| Suhyeon Ryu | MS (2026) |  |

## 최근 논문 목록 (2021–2026)

언어 명세·타입 검사·정적 분석, WebAssembly, C-to-Rust 변환과 양자 소프트웨어 시험을 다룬다. 연구실 논문 목록의 2021–2026년 구역에서 류석영 교수가 저자인 논문 35편과 심유성의 연구실 개인 소개에 실린 국내 논문 3편이다. 제목·저자·발표처는 각 목록의 표기를 따른다. 2026년 구역의 「to appear」는 게재 예정이며, 그 밖의 연도는 연구실이 둔 구역이다. 저자 이름 뒤의 별표는 누리집 표시다.[^pubs][^yusung]

**2026**

- Jaemin Hong, Hyunhee Kang, and Sukyoung Ryu. "Replacing Output Parameters with Algebraic Data Types in C-to-Rust Translation". *ACM Transactions on Software Engineering and Methodology (TOSEM), to appear*.
- Jaehyun Lee, Seokhun Jeong, Sehyuk Ahn, Haechan Kwon, and Sukyoung Ryu. "P4-SpecTec: Integrating a Language Mechanization Framework into the Real-World P4 Specification". *Proceedings of the ACM on Programming Languages (PACMPL) OOPSLA 2026, October 2026*.
- Seungmin Jeon, Jaeho Choi, Jonguk Jeon, Kanguk Lee, Kyeongmin Cho, Sukyoung Ryu, and Jeehoon Kang. "Quantum Monte Carlo Estimation via Probabilistic Programming". *Proceedings of the ACM on Programming Languages (PACMPL) OOPSLA 2026, October 2026*.
- Seokhun Jeong, Gyeongmin Dan, Sukyoung Ryu, and Sungjae Hwang. "SpecTrum: Specification-Guided Differential Fuzzing for Ethereum Consensus Clients". *Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE), October 2026*.
- Yusung Sim, Sukyoung Ryu, and Jaemin Hong. "Rust's Type Checker Implementation is Unsound: An Empirical Study on Soundness Bugs in rustc". *Proceedings of the ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA), October 2026*.
- Eunsu Kim, Sukyoung Ryu, and Jaemin Hong. "Securing Union-Based Type Punning in C-to-Rust Translation". *IEEE Security & Privacy, July 2026*.
- Jaemin Hong, Kanguk Lee, Hanliang Zhang, Hyunhee Kang, Eunsu Kim, Justin Restivo, Thanos Typaldos, Ramla Ijaz, Sukyoung Ryu, and Zhong Shao. "PROCTOR: An Extensible C-to-Rust Translation Framework with Static-Analysis-Driven Plugins". *IEEE Security & Privacy, July 2026*.
- Jaehyun Lee, Seokhun Jeong, and Sukyoung Ryu. "Failing with Purpose: Dangling Coverage-Guided Negative Test Generation from a Mechanized P4 Type System". *Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), July 2026*.
- Kanguk Lee, Seunghwan Kim, Jihyeok Park, and Sukyoung Ryu. "Selective Feature-Sensitive Coverage for Conformance Testing of Programming Languages". *ACM Transactions on Software Engineering and Methodology (TOSEM), April 2026*.

**2025**

- Dongjun Youn, Wonho Shin, and Sukyoung Ryu. "WEST: Specification-Based Test Generation for WebAssembly". *Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), November 2025*.
- Kanguk Lee, Jaemin Hong, and Sukyoung Ryu. "Exact Inference for Quantum Circuits: A Testing Oracle for Quantum Software Stacks". *Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), November 2025*.
- Jaemin Hong and Sukyoung Ryu. "Forcrat: Automatic I/O API Translation from C to Rust via Origin and Capability Analysis". *Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), November 2025*.
- Doehyun Baek, Daniel Lehmann, Ben L. Titzer, Sukyoung Ryu, and Michael Pradel. "Execution-Aware Program Reduction for WebAssembly via Record and Replay". *Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE), November 2025*.
- Jaemin Hong and Sukyoung Ryu. "Automatically Translating C to Rust". *Communications of the ACM (CACM), Volume 68, No. 11, November 2025*.
- Jihee Park, Insu Yun, and Sukyoung Ryu. "Bridging the Gap between Real-World and Formal Binary Lifting through Filtered-Simulation". *Proceedings of the ACM on Programming Languages (PACMPL) OOPSLA 2025, October 2025*.
- Jaemin Hong and Sukyoung Ryu. "Type-Migrating C-to-Rust Translation using a Large Language Model". *Empirical Software Engineering (EMSE), Volume 30, Article Number 3, 2025*.

**2024**

- Jaemin Hong, Sunghwan Shim, Sanguk Park, Tae Woo Kim, Jungwoo Kim, Junsoo Lee, Sukyoung Ryu, and Jeehoon Kang. "Taming Shared Mutable States of Operating Systems in Rust". *Science of Computer Programming (SCICO), Volume 238, December 2024*.
- Jaemin Hong and Sukyoung Ryu. "To Tag, or Not to Tag: Translating C’s Unions to Rust’s Tagged Unions". *Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE), October 2024*.
- Doehyun Baek\*, Jakob Getz\*, Yusung Sim, Daniel Lehmann, Ben Titzer, Sukyoung Ryu, and Michael Pradel. "Wasm-R3: Record-Reduce-Replay for Realistic and Standalone  WebAssembly Benchmarks". *Proceedings of the ACM on Programming Languages (PACMPL) OOPSLA 2024, October 2024*.
- Jaemin Hong and Sukyoung Ryu. "Don't Write, but Return: Replacing Output Parameters with Algebraic Data Types in C-to-Rust Translation". *Proceedings of the 45th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI), June 2024*.
- Dongjun Youn, Wonho Shin, Jaehyun Lee, Sukyoung Ryu, Joachim Breitner, Philippa Gardner, Sam Lindley, Matija Pretnar, Xiaojia Rao, Conrad Watt, and Andreas Rossberg. "Bringing the WebAssembly Standard up to Speed with SpecTec". *Proceedings of the 45th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI), June 2024*.
- Sukyoung Ryu and Jihyeok Park. "JavaScript Language Design and Implementation in Tandem". *Communications of the ACM (CACM), Volume 67, No. 5, May 2024*.
- Sungjae Hwang, Sungho Lee, and Sukyoung Ryu. "An Empirical Study of JVMs’ Behaviors on Erroneous JNI Interoperations". *IEEE Transactions on Software Engineering (TSE), Volume 50, No. 4, April 2024*.
- Yusung Sim, Doehyun Baek, Jakob Getz, & Sukyoung Ryu. "Wasm Benchmark Generation by Recording and Replaying the Host Interoperation". *KIISE Transactions on Computing Practices, 30(7), 341-346*.

**2023**

- Dongjun Youn, Sungho Lee, and Sukyoung Ryu. "Declarative Static Analysis for Multilingual Programs using CodeQL". *Software: Practice and Experience (SPE), Volume 53, Issue 7, July 2023*.
- Jihyeok Park, Dongjun Youn, Kanguk Lee, and Sukyoung Ryu. "Feature-Sensitive Coverage for Conformance Testing of Programming Language Implementations". *Proceedings of the 44th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI), June 2023*.
- Emily Ruppel, Sihang Liu, Elba Garza, Sukyoung Ryu, Alexandra Silva, and Talia Ringer. "Long-Term Mentoring for Computer Science Researchers". *Communications of the ACM (CACM), Volume 66, No. 5, May 2023*.
- Jihee Park\*, Sungho Lee\*, Jaemin Hong, and Sukyoung Ryu. "Static Analysis of JNI Programs via Binary Decompilation". *IEEE Transactions on Software Engineering (TSE), Volume 49, No. 5, May 2023*.
- Jaemin Hong and Sukyoung Ryu. "Concrat: An Automatic C-to-Rust Lock API Translator for Concurrent  Programs". *Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE), May 2023*.
- Jihee Park, Jaemin Hong, and Sukyoung Ryu. "Semantic Transformation Framework for Rewriting Rules". *Proceedings of the ACM SIGPLAN Workshop on Partial Evaluation and Program Manipulation (PEPM), January 2023*.
- Yusung Sim, Doehyun Baek, Jakob Getz, & Sukyoung Ryu. "Wasm Benchmark Generation by Recording and Replaying the Host Interoperation". *한국정보과학회 학술발표논문집, 부산, 2023-12-20*.

**2022**

- Jihyeok Park, Seungmin An, and Sukyoung Ryu. "Automatically Deriving JavaScript Static Analyzers from Specifications using Meta-Level Static Analysis". *Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE), November 2022*.
- Yusung Sim, & Sukyoung Ryu. "Program Equivalence Checking for WebAssembly via Symbolic Execution". *한국정보과학회 학술발표논문집, 제주, 2022-12-20*.

**2021**

- Jihyeok Park, Seungmin An, Wonho Shin, Yusung Sim, and Sukyoung Ryu. "JSTAR: JavaScript Specification Type Analyzer using Refinement". *Proceedings of the 36th IEEE/ACM International Conference on Automated Software Engineering (ASE), November 2021*.
- Joonyoung Park\*, Jihyeok Park\*, Dongjun Youn, and Sukyoung Ryu. "Accelerating JavaScript Static Analysis via Dynamic Shortcuts". *Proceedings of the 29th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE), August 2021*.
- Jihyeok Park\*, Hongki Lee\*, and Sukyoung Ryu. "A Survey of Parametric Static Analysis". *ACM Computing Surveys (CSUR), Volume 54, Issue 7, Article No. 149, pp 1–37, July 2021*.
- Jihyeok Park, Seungmin An, Dongjun Youn, Gyeongwon Kim, and Sukyoung Ryu. "JEST: N+1-version Differential Testing of Both JavaScript Engines and Specification". *Proceedings of the 43rd ACM/IEEE International Conference on Software Engineering (ICSE), May 2021*.
- Sungjae Hwang, Sungho Lee, Jihoon Kim, and Sukyoung Ryu. "JUSTGen: Effective Test Generation for Unspecified JNI Behaviors on JVMs". *Proceedings of the 43rd ACM/IEEE International Conference on Software Engineering (ICSE), May 2021*.

## 과제

2021년 10월 13일–2026년 10월 13일 범위에서 KAIST가 알린 연구 지원 선정이다. 날짜는 발표일이다.[^leader]

- 2026-05-28 · 류석영 교수가 컴퓨터 소프트웨어 분야의 기초연구사업 리더연구 유형A에 선정됐다.[^leader] (지원 과학기술정보통신부; 상태 선정)

## 수상과 선정

2021년 10월 13일–2026년 10월 13일 범위의 교수 교육상과 논문상이다.[^teaching][^pubs]

- 2025-05-20 · 류석영 교수, 임형규 링크제네시스 베스트 티쳐 어워드 대상 수상자로 발표됐다.[^teaching]
- 2025-11 · Dongjun Youn·Wonho Shin·Sukyoung Ryu의 WEST 논문이 ACM SIGSOFT Distinguished Paper Award를 받았다.[^pubs][^p3]

## 소식

2021년 10월 13일–2026년 10월 13일 범위의 KAIST 연구 소식이다.[^kaistnews]

- 2024-07-03 · KAIST는 류석영·강지훈 교수 연구팀의 PLDI 2024 논문 발표를 알렸다. 류석영 교수의 공저 논문에는 C-to-Rust 변환과 WebAssembly 명세를 다룬 연구가 포함됐다.[^kaistnews]

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 전산학부 E3-1 4409호·4410호[^home]
- 연구실 전화: +82-42-350-7738(4409호), +82-42-350-7838(4410호)[^home]
- 교수 연구실: E3-5 304호, 전화 +82-42-350-3538[^prof][^faculty]
[^home]: 연구실 첫 화면. <https://plrg.kaist.ac.kr/> 2026-10-28 열람. 연구 관심, 개발자의 소프트웨어 품질 향상이라는 목표, 타입 시스템·분석·디버깅·시험 도구, 연구실 연락처.
[^lab]: KAIST 전산학부 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=85&menu=64> 2026-10-27 열람. 국문 연구실 이름, 지도교수, 연구 분야와 연구 방향.
[^faculty]: KAIST 전산학부 교수진. <https://cs.kaist.ac.kr/people/faculty> 2026-10-27 열람. 류석영 이름·직위·소속·연구 분야, 교수연구실.
[^prof]: 류석영 교수 개인 소개. <https://plrg.kaist.ac.kr/ryu> 2026-10-28 열람. 영문 이름, KAIST ICT Endowed Chair Professor, 학력과 경력, 연구 관심, 교수연구실.
[^members]: 연구실 구성원. <http://plrg.kaist.ac.kr/members> 2026-10-28 열람. 현재 구성원 구획과 Alumni의 학위·연도·진로.
[^pubs]: 연구실 논문 목록. <http://plrg.kaist.ac.kr/research/publications> 2026-10-28 열람. 2021–2026년 논문, 저자 순서, 강연·튜토리얼, WEST 논문상.
[^software]: 연구실 공개 소프트웨어. <http://plrg.kaist.ac.kr/research/software> 2026-10-28 열람. 공개 도구와 언어 모형.
[^dongjun]: 윤동준 개인 소개. <https://plrg.kaist.ac.kr/members/%EC%9C%A4%EB%8F%99%EC%A4%80-dongjun-youn> 2026-10-28 열람. 한글 이름, 과정 시작과 연구 주제.
[^gyeongwon]: 김경원 개인 소개. <https://plrg.kaist.ac.kr/members/%EA%B9%80%EA%B2%BD%EC%9B%90-gyeongwon-kim> 2026-10-28 열람. 한글 이름, 과정 시작과 연구 주제.
[^yusung]: 심유성 개인 소개. <https://plrg.kaist.ac.kr/members/%EC%8B%AC%EC%9C%A0%EC%84%B1-yusung-sim> 2026-10-28 열람. 한글 이름, 과정 시작과 연구 주제, 국내 논문 3편.
[^kaistnews]: KAIST 연구 소식: PLDI 2024 논문 발표. <https://www.kaist.ac.kr/news/html/news/?mng_no=37950&mode=V> 2026-10-28 열람. 2024-07-03 소식, C-to-Rust 변환과 WebAssembly 명세 성과.
[^leader]: KAIST 연구 소식: 리더연구 선정. <https://www.kaist.ac.kr/researchnews/html/news/?mng_no=62251&mode=V> 2026-10-28 열람. 2026-05-28 발표의 리더연구 유형A 선정과 컴퓨터 소프트웨어 분야.
[^teaching]: KAIST 교육혁신의 날 소식. <https://news.kaist.ac.kr/news/html/news/?mng_no=46650&mode=V> 2026-10-28 열람. 2025-05-20 발표의 임형규 링크제네시스 베스트 티쳐 어워드 대상.
[^p1]: J. Park 외, S. Ryu, Proceedings of the 43rd ACM/IEEE International Conference on Software Engineering (ICSE) (2021). <https://conf.researchr.org/details/icse-2021/icse-2021-papers/43/JEST-N-1-version-Differential-Testing-of-Both-JavaScript-Engines-and-Specification> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/icse-2021/icse-2021-papers/43/JEST-N-1-version-Differential-Testing-of-Both-JavaScript-Engines-and-Specification>. 2026-10-28 열람.
[^p2]: J. Lee, S. Jeong, S. Ryu, Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE) (2026). <https://doi.org/10.1145/3797109> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/196/Failing-with-Purpose-Dangling-Coverage-Guided-Negative-Test-Generation-from-a-Mechan>. 2026-10-28 열람.
[^p3]: D. Youn, W. Shin, S. Ryu, Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) (2025). <https://doi.org/10.1109/ASE63991.2025.00119> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/ase-2025/ase-2025-papers/54/WEST-Specification-Based-Test-Generation-for-WebAssembly>. 2026-10-28 열람.
[^p4]: D. Baek 외, M. Pradel, Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) (2025). <https://doi.org/10.1109/ASE63991.2025.00073> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/ase-2025/ase-2025-papers/28/Execution-Aware-Program-Reduction-for-WebAssembly-via-Record-and-Replay>. 2026-10-28 열람.
[^p5]: J. Hong, S. Ryu, Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE) (2023). <https://doi.org/10.1109/ICSE48619.2023.00069> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/icse-2023/icse-2023-technical-track/66/Concrat-An-Automatic-C-to-Rust-Lock-API-Translator-for-Concurrent-Programs>. 2026-10-28 열람.
[^p6]: J. Hong, S. Ryu, Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) (2025). <https://doi.org/10.1109/ASE63991.2025.00130> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/ase-2025/ase-2025-papers/177/Forcrat-Automatic-I-O-API-Translation-from-C-to-Rust-via-Origin-and-Capability-Analy>. 2026-10-28 열람.
[^p7]: K. Lee, J. Hong, S. Ryu, Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) (2025). <https://doi.org/10.1109/ASE63991.2025.00203> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/ase-2025/ase-2025-papers/215/Exact-Inference-for-Quantum-Circuits-A-Testing-Oracle-for-Quantum-Software-Stacks>. 2026-10-28 열람.

# 소프트웨어 테스팅 및 검증 연구실 (Software Testing and Verification Group, SWTV)

**KAIST 전산학부 · 김문주 부교수**

- 분야: 소프트웨어 자동 테스팅·디버깅, 프로그램 분석, 테스트 입력 자동 생성, 결함 위치 추정
- 대분야: 컴퓨팅·AI
- 태그: 프로그램 분석·검증[^intro][^pi], 퍼징[^p2][^p4], 대형 언어 모델[^p1]
- 홈페이지: <https://swtv.kaist.ac.kr/>
- 근거와 출처: [SWTV 근거 페이지](swtv-sources.md)

> 복잡한 소프트웨어의 오류를 자동으로 찾아내고 고치는 기술을 연구하며, 사람이 일일이 쓰기 어려운 테스트 입력과 실행 조건을 프로그램 분석으로 만드는 연구실이다.[^intro][^home]

## 무엇을 연구하나

소프트웨어 테스팅(소프트웨어가 요구한 조건을 충족하는지 확인하고 오류를 찾는 활동)과 디버깅(오류의 원인을 찾아 수정하는 작업)을 자동화한다. 프로그램에는 자료를 저장하고 다루는 구조와 반복 실행, 여러 작업이 함께 진행되는 동작이 얽혀 있다. 연구실은 이런 복잡함 때문에 사람이 작성한 시험만으로 다양한 실행 상황을 다루기 어렵다고 보고, 프로그램의 성질을 분석하는 이론과 자동화 도구를 연구한다.[^home][^intro]

한 갈래는 **시험할 입력과 실행 조건을 함께 찾는 일**이다. 같은 프로그램이라도 커맨드 라인 옵션(명령어에 붙여 동작 방식을 지정하는 설정)이 달라지면 실행하는 부분이 달라진다. POWER(Program Option-Aware Fuzzer)는 옵션 조합과 입력 파일에 서로 다른 탐색 전략을 적용하고, 다양한 실행을 유도하는 옵션 조합을 골라 오류를 찾는다. 퍼징(입력을 대량으로 생성하거나 변형해 프로그램의 오류를 찾는 시험 기법)의 대상을 파일 내용에서 프로그램을 실행하는 설정까지 넓힌 연구다.[^p2]

다른 갈래는 **프로그램의 일부를 시험하는 코드를 만드는 일**이다. 유닛 테스팅(함수나 구성 요소 같은 개별 단위를 대상으로 하는 시험)에서는 입력값뿐 아니라 그 단위를 호출하는 코드도 필요하다. CITRUS(C++ unIt Testing for Reliable and Usable Software)는 C++ 소스 코드(프로그래밍 언어로 작성한 프로그램)를 분석해 여러 함수 호출로 이루어진 테스트 드라이버(시험 대상을 호출하고 실행을 준비하는 프로그램)를 생성한다. 이어 호출 코드와 함수에 전달하는 값을 바꿔 다양한 상태를 시험한다. Clementine 연구는 복잡한 C++ 문법 때문에 생성된 테스트 코드를 실행할 수 없게 되는 문제를 다뤘다.[^p3][^p5]

최근에는 **대형 언어 모델(LLM, Large Language Model, 많은 언어 자료를 학습해 글과 코드를 이해하고 생성하는 인공지능 모델)을 이용한 규칙 검사**도 한다. LASIK은 여러 에이전트(주어진 정보로 판단하고 행동하는 소프트웨어 주체)를 구성해 MISRA C(안전성과 신뢰성을 위한 C 언어 코딩 지침) 위반을 검사한다. 필요한 프로그램 맥락과 실제 실행 중 얻은 자료를 함께 제공해, 규칙을 어긴 부분을 찾으면서 오탐(문제가 아닌 것을 문제로 보고하는 판정)을 억제하는 방법이다.[^p1]

## 주요 연구 주제

### 입력 탐색과 자동 테스팅의 결합

POWER는 옵션 조합과 파일 입력을 구분해 탐색한다. CONUZZ(원문 풀이 CONolic + fUZZing)는 콘콜릭 테스팅(실제 값을 넣는 실행과 입력을 기호로 나타내는 분석을 결합한 시험)과 퍼징을 함께 사용하는 유닛 시험 기술이다. 두 방식의 서로 다른 동작 특성을 결합해 시험 효과를 높이려는 연구이며, 두 방식을 조합한 유닛 시험 기술을 개발하고, 실험으로 시험 효과를 살피는 연구다.[^p2][^p4]

테스트 커버리지(정해진 시험 기준 가운데 실제 시험이 충족한 부분의 비율)도 주요 관심사다. EvoSuite 연구는 Java 프로그램을 자동 시험하는 도구가 실행하지 못한 분기를 분류하고, 그 원인을 구체적인 예로 설명했다. 높은 수치만 제시하는 대신 자동 시험이 어디에서 막히는지 조사한 연구다.[^p6]

### C++ 테스트 코드의 생성과 실행 가능성

CITRUS는 소스 코드를 분석해 시험용 호출 코드를 만들고, 그 코드를 변형하거나 함수 입력값을 바꾸어 프로그램의 여러 상태에 도달한다. 실제 C++ 프로그램을 대상으로 한 실험에서 시험 효과를 평가했다.[^p3] Clementine 연구는 컴파일(소스 코드를 실행에 사용할 수 있는 형태로 변환하는 과정)되지 않는 테스트 코드의 원인이 되는 C++ 문법 사례를 정리하고 도구를 수정했다. 생성한 시험 코드가 실제로 실행될 수 있도록 만드는 문제에 초점을 둔다.[^p5]

### 실행 자료를 활용하는 규칙 검사와 오류 분석

LASIK은 언어 모델을 이용해 코딩 규칙 위반을 검사한다. 여러 에이전트에 필요한 코드 맥락을 제공하고, 실행 중의 증거를 함께 사용해 MISRA C 위반을 찾는다. 프로그램을 실행하지 않고 코드를 살피는 정적 분석 도구와 비교해 검사 결과를 평가했다.[^p1] 교수의 연구 관심에는 변이 분석(프로그램에 의도적으로 변화를 주고 그 영향을 살피는 분석)을 통한 결함 위치 추정(오류의 원인이 있을 코드 위치를 찾는 작업)과 테스트 생성도 들어 있다.[^pi]

## 대표 논문

2021–2026년 논문 가운데 자동 시험 입력 생성, C++ 유닛 시험, 언어 모델 기반 규칙 검사를 보여 주는 여섯 편이다. ‘쉽게 말하면’은 각 논문의 초록을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 김문주 교수의 저자 위치 |
|---|---|---|---|---|
| 1 | 2026 | [Top-Down Multi-agent LLM System with Runtime Data for MISRA C Violation Detection](https://doi.org/10.1145/3832783.3834497) · IEEE/ACM ASE | MISRA C 위반을 검사하는 LASIK을 제안했다. 여러 언어 모델 에이전트에 필요한 코드 맥락과 실제 실행 자료를 제공한다. 임베디드 소프트웨어와 산업용 소프트웨어 평가에서 비교한 정적 분석 도구 및 단순 언어 모델 방식보다 실제 위반을 많이 찾고 오탐 비율을 낮게 유지했다고 보고했다.[^p1] | 마지막 저자·교신저자 |
| 2 | 2022 | [POWER: Program Option-Aware Fuzzer for High Bug Detection Ability](https://swtv.kaist.ac.kr/files/publications/international_conference/POWER-IEEEeXpress-2022017668.pdf) · IEEE ICST | 프로그램의 실행 옵션 조합을 만들고 선택하는 시험과 입력 파일을 바꾸는 시험에 서로 다른 전략을 쓴다. 서로 다른 실행을 유도하는 옵션들을 골라, 실제 프로그램 실험에서 비교한 퍼징 기법보다 많은 비정상 종료 오류를 찾았다.[^p2] | 마지막 저자 |
| 3 | 2022 | [CITRUS: Automated Unit Testing Tool for Real-world C++ Programs](https://swtv.kaist.ac.kr/files/publications/international_conference/icst22-citrus.pdf) · IEEE ICST Testing Tools track | 복잡한 C++ 프로그램을 자동 시험하는 도구다. 코드를 분석해 여러 함수 호출로 이루어진 시험 프로그램을 만들고, 호출 코드와 함수에 넣는 값을 바꾼다. 실제 C++ 프로그램에 적용해 시험이 실행한 코드의 범위를 평가했다.[^p3] | 마지막 저자 |
| 4 | 2022 | [Concolic 테스팅과 Fuzzing을 결합한 유닛 테스팅 자동화 기술](https://swtv.kaist.ac.kr/files/publications/domestic_conference/CONUZZ-KCSE22.pdf) · KCSE (short paper) | 자동으로 시험 입력을 생성하는 콘콜릭 테스팅과 퍼징은 서로 다른 방식으로 동작한다. 두 기술을 조합한 새 유닛 시험 기술을 개발하고, 함께 사용할 때의 시험 효과를 실험으로 살피는 연구다.[^p4] | 마지막 저자 |
| 5 | 2023 | [Challenges in Automated Unit Testing of Complex C++ Programs](https://swtv.kaist.ac.kr/files/publications/domestic_conference/Challenges-in-Automated-Unit-Testing-of-Complex-C-Programs-v13.pdf) · KSC | C++ 자동 시험 도구 Clementine이 복잡한 문법 때문에 실행할 수 없는 시험 코드를 만드는 문제를 조사했다. 문제를 일으키는 문법 사례를 정리하고 수정한 뒤, 실제 프로그램 실험에서 컴파일되지 않는 시험 코드를 줄이고 모든 대상 함수에 실행 가능한 시험 코드를 생성했다고 보고했다.[^p5] | 마지막 저자 |
| 6 | 2021 | [Empirical Study of Effectiveness of EvoSuite on the SBST 2020 Tool Competition Benchmark](https://swtv.kaist.ac.kr/files/publications/international_conference/ssbseRENE21-evoStudy.pdf) · SSBSE | Java 자동 시험 도구 EvoSuite가 도달하지 못하는 코드의 원인을 조사했다. 실제 프로젝트에서 뽑은 평가 자료를 시험한 뒤 실행하지 못한 분기를 사람이 분류하고, 도구의 한계를 구체적인 예로 보고했다.[^p6] | 마지막 저자 |

## 교수와 전문 분야

김문주(Moonzoo Kim) 부교수는 1995년 KAIST 전산학 학사, 2001년 미국 University of Pennsylvania CIS 박사 학위를 받았다. 2006년 9월 KAIST 전산학부 조교수로 부임했고, 2012년 3월부터 부교수로 재직한다고 소개한다. 2019년 9월부터 자동 소프트웨어 시험 도구·서비스·교육을 제공하는 VPlusLab의 CEO도 맡고 있다.[^pi][^members]

학과 교수 명단은 전문 분야를 소프트웨어 테스팅, 소프트웨어 디버깅, 소프트웨어 공학으로 적는다.[^faculty] 교수 소개의 연구 관심은 동적 기호 실행(실행 중 얻은 정보를 이용해 입력 조건을 기호식으로 분석하는 방법), 자동 유닛 시험과 결함 위치 추정, 변이 기반 프로그램 분석, 자동 테스팅·디버깅의 산업 적용이다.[^pi] 대표 논문에서는 시험 입력 생성과 C++ 시험 도구 개발, 자동 시험 도구의 한계 분석, 언어 모델을 이용한 코딩 규칙 검사를 확인할 수 있다.[^p1][^p2][^p3][^p6]

## 응용 분야

교수 소개는 삼성 스마트폰, LG 가전, 현대자동차 등을 자동 시험·디버깅 기술의 산업 적용 대상으로 든다.[^pi] 최근 대표 논문은 실제 C++ 프로그램의 유닛 시험과 임베디드 소프트웨어의 코딩 규칙 검사를 다룬다.[^p1][^p3] 연구실이 게시한 과제에는 소프트웨어 재난 탐지와 회귀 테스팅(프로그램을 변경한 뒤 기존 기능이 유지되는지 확인하는 시험)을 위한 유닛 퍼징이 있다.[^projects]

## 구성원

2026년 10월 28일 Members 페이지 기준으로 박사과정 1명과 석사과정 2명이다. ‘대표 논문 참여’는 위 표의 번호이며, 원문 전체 저자 목록에서 같은 이름을 확인해 표시했다.[^members]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Ahcheong Lee (이아청 李我淸) | 박사과정 | ahcheong.lee@kaist.ac.kr | 1, 2, 5 |
| Sechang Jang (장세창 張世昌) | 석사과정 | newwin0198@kaist.ac.kr | 1 |
| Jaewoo Kim (김재우 金哉佑) | 석사과정 | eoaud0108@kaist.ac.kr |  |

이아청은 KAIST 전산학부 학사(2019)·석사(2021), 장세창은 Handong Global University Computer Science 학사(2025), 김재우는 Korea University Cyber Defense 학사(2025)로 소개되어 있다.[^members]

## 졸업생 진로

Members 페이지가 게시한 졸업생 19명이다. 학위 논문 제목은 Publications 페이지 표기다.[^members][^pubs]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Yeongbin Kang (강영빈 康永彬) | M.S. School of Computing, KAIST '26 (2026) |  | Yeongbin Kang, Rule-Specialized Strategies for LLM Agents in MISRA C Violation Detection, Master’s Thesis, School of Computing, KAIST, Aug. 2026 |
| Heechan Yang (양희찬 梁熙讚) | M.S. School of Computing, KAIST '26 (2026) |  | Heechan Yang, Systematic Dataset Construction for Deep Learning-Based Fault Localization(DLFL) with Mutation-Based Fault Localization(MBFL) Features, Master’s Thesis, School of Computing, KAIST, Feb. 2026 |
| YeongSeok Choi (최영석 崔榮晳) | M.S. School of Computing, KAIST '25 (2025) | SuresoftTech Inc. | Youngseok Choi, System Execution Data-Driven Function-Level Regression Fuzzing, Master’s Thesis, School of Computing, KAIST, Feb. 2025 |
| Irfan Ariq | M.S. School of Computing, KAIST '23 (2023) |  | Irfan Ariq, Automated Unit Testing Framework for Complex C++ Programs, Master’s Thesis, School of Computing, KAIST, Aug. 2023 |
| Nakwon Lee (이낙원 李樂遠) | Ph.D School of Computing, KAIST '22 (co-advised with Prof. Jongmoon Baik) (2022) | Samsung Electronics DS | Nakwon Lee, A Novel Target Directed Model Checking for Fast Abstract Reachability Analysis, Ph.D Dissertation, School of Computing, KAIST, Feb. 2022 |
| Zidong Yang (양재동 杨梓栋) | M.S. School of Computing, KAIST '22 (2022) | Nvidia Shanghai, China | Zidong Yang, Analysis and Improvement of Unit-level Concolic Testing for Real-world C Programs, Master’s Thesis, School of Computing, KAIST, Feb. 2022 |
| Robert Sebastian Herlim | M.S. School of Computing, KAIST '22 (2022) | ASM Korea | Robert Sebastian Herlim, On Understanding and Improving Automated Unit-level Test Generation for C++ Programs, Master’s Thesis, School of Computing, KAIST, Feb. 2022 |
| Kunwoo Park (박건우 朴乾雨) | M.S. School of Computing, KAIST '20 (2020) | TMAX | Kunwoo Park, Effective Concolic Search Strategy Using Dynamic Taint Analysis, Master’s Thesis, School of Computing, KAIST, Feb. 2020 |
| Loc Duy Phan | M.S. School of Computing, KAIST '20 (2020) | LG CTO | Phan Duy Loc, Effective Mutant Reduction using Fine-grained Mutation Operators, Master’s Thesis, School of Computing, KAIST, Feb. 2020 |
| Hyunsu Lim (임현수 林炫秀) | M.S. School of Computing, KAIST '19 (2019) |  | Hyunsu Lim, Concolic Unit Testing With Dynamic Unit Contexts Carved from System Tests, Master’s Thesis, School of Computing, KAIST, Feb. 2019 |
| Hyunwoo Kim (김현우 金鉉雨) | M.S. School of Computing, KAIST '18 (2018) |  | Hyunwoo Kim, Concolic Testing Guidelines for Test Coverage Improvement: an Industrial Case Study, Master’s Thesis, School of Computing, KAIST, Aug. 2018 |
| Yunho Kim (김윤호 金潤浩) | Ph.D School of Computing, KAIST Feb '17 (Best Ph.D Thesis award) (2017) | Hanyang University as an assistant professor | Yunho Kim, Automated Unit Test Generation with Realistic Unit Context Synthesis for Low False Alarms, Ph.D Dissertation, School of Computing, KAIST, Feb. 2017 (Best dissertation award) |
| Taejin Kim (김태진 金泰蓁) | M.S. School of Computing, KAIST Aug '16 (2016) |  | Taejin Kim, Coverage Improvement of Concolic Testing by Optimizing Symbolic Array Index Operations, Master’s Thesis, School of Computing, KAIST, Aug. 2016 |
| Taehoon Kwak (곽태훈 郭太勳) | M.S. School of Computing, KAIST Feb '16 (2016) |  | Taehoon Kwak, Mutation-based Debugging of Real-world Multilingual Programs, Master’s Thesis, School of Computing, KAIST, Feb. 2016 |
| Shin Hong (홍신 洪申) | Ph.D School of Computing, KAIST Aug '15 (2015) | Chungbuk National University as an associate professor | Shin Hong, Effective and Efficient Test Generation for Multithreaded Programs Using Concurrency Coverage Metrics, Ph.D Dissertation, School of Computing, KAIST, Aug. 2015 |
| Yongbae Park (박용배 朴容培) | M.S. School of Computing, KAIST Feb '15 (Best KAIST CS MS thesis award) (2015) | the Defense Ministry Research Institute | Yongbae Park, Automated Testing of Reactive Software with Non-deterministic Events: A Case Study on LG Electric Oven, Master’s Thesis, Computer Science Department, KAIST, Feb. 2015 (Best thesis award) |
| Seokhyeon Mun (문석현 文晳鉉) | M.S. School of Computing, KAIST Feb '14 (Best KAIST CS MS thesis award) (2014) | Samsung SDS | Seokhyeon Moon, Effective Software Fault Localization using Dynamic Program Behaviors, Master’s Thesis, Computer Science Department, KAIST, Feb. 2014 (Best thesis award) |
| Jaemin Ahn (안재민 安宰民) | M.S. School of Computing, KAIST Aug '13 (교과석사) (2013) | ADD |  |
| Young Joo Kim (김영주 金映周) | M.S. School of Computing, KAIST Feb '13 (Distinguished best KAIST CS MS thesis award) (2013) | Amazon | Youngjoo Kim, Hybrid Statistical Model Checking Technique for Reliable Safety Critical Systems, Master’s Thesis, Computer Science Department, KAIST, Feb. 2013 (Distinguished best thesis award) |

## 최근 5년 논문 목록

2021–2026년의 학술지·학회 논문 16편이다. 자동 시험 입력 생성과 퍼징, 오류 위치 추정, 프로그램 검증과 언어 모델 기반 규칙 검사를 다룬다. 제목·저자·발표처와 날짜는 연구실이 게시한 표기이며, 2021년 논문은 해당 연도 항목을 함께 싣는다.[^pubs]

**2026**

- A. Lee, Y. Kang, S. Jang, H. Yang, M. Kim, Top-down Multi-agent LLM System with Runtime Data for MISRA C Violation Detection, IEEE/ACM International Conference on Automated Software Engineering (ASE) Industry showcase, October 12-16, 2026
- 강영빈, 이아청, 김문주, Agentic LLM 기반 MISRA C 위반 탐지를 위한 규칙 특화·증거 기반 프롬프트 설계, Korea Computer Congress, June 22-24, 2026
- 양희찬, 이아청, 조규태, 김문주, 딥러닝 기반 국방 SW 결함위치추정을 위한 변이 기반 데이터셋 구축의 체계적 연구, Korea Conference on Software Engineering, Feb 4-6, 2026

**2025**

- A.Lee, Y.Choi, S.Hong, Y.Kim, K.Cho, and M.Kim. ZigZagFuzz: Interleaved Fuzzing of Program Options and Files. ACM Transactions on Software Engineering and Methodology (TOSEM). Volume 34, Issue 2, Artical 39. Feb. 2025.
- 김지웅, 강영빈, 이아청, 김문주, 홍신, OSS-Fuzz 테스트 이력을 활용한 체계적인 프로젝트 교차-결함 사례의 수집, Korea Conference on Software Engineering, Jan 20-22, 2025

**2024**

- 최영석, 이아청, 남효주, 이인섭, 정남훈, 조규태, 김문주, 유닛 동적 상태 데이터 기반회귀 유닛 테스팅의 오탐 필터링 기법, Journal of KIISE, Vol. 51, Num. 11, Oct. 2024 ( Best paper award by Korea SE society )
- 양희찬, 이아청, 이인섭, 남효주, 정남훈, 조규태, 김문주, 결함위치탐지 모델 학습을 위한 데이터셋 생성 방법: JsonCpp 사례연구, Korea Computer Congress, June 26-28, 2024

**2023**

- Letian Zhang, 이아청, 김문주, Challenges in Automated Unit Testing of Complex C++ Programs, Korea Software Congress (KSC), Dec 20-22, 2023

**2022**

- A. Lee, I. Ariq, Y. Kim, and M. Kim, POWER: Program Option-Aware Fuzzer for High Bug Detection Ability, IEEE International Conference on Software Testing, Verification and Validation (ICST), April 4 - 13, 2022
- R. S. Herlim, Y. Kim, and M. Kim, CITRUS: Automated Unit Testing Tool for Real-world C++ Programs, IEEE International Conference on Software Testing, Verification and Validation (ICST) Testing Tools track, April 4 - 13, 2022
- 이아청, 김윤호, 김문주, 커맨드 라인 옵션을 변이 및 선택하여 테스팅 효과를 높이는 퍼징 기법, Journal of KIISE, Vol.49, Num. 11, Nov 2022
- 김윤삼, 김문주, Concolic 테스팅과 Fuzzing을 결합한 유닛 테스팅 자동화 기술 , Korea Conference on Software Engineering (KCSE), Jan 2022 (short paper)

**2021**

- N.Lee, Y.Kim, M.Kim, D.Ryu and J.Baik, Directed Model Checking for Fast Abstract Reachability Analysis, IEEE Access, Volume 9, page 158738-158750, Nov 25, 2021.
- R. S. Herlim, S. Hong, Y. Kim, and M. Kim, Empirical Study of Effectiveness of EvoSuite on the SBST 2020 Tool Competition Benchmark, Proceedings of the 13th International Symposium on Search Based Software Engineering (SSBSE), Bari, Italy, October 11-15, 2021
- 이아청, 김윤호, 김문주, 동적 함수 관련도를 이용한 퍼징 커버리지 향상 기법, Journal of KIISE, Vol.48, Num. 4, Apr 2021
- 이아청, 김윤호, 김문주, 유용한 커맨드 라인 옵션을 선택하여 커버리지와 오류 탐지 능력을 높이는 퍼징 기법, Korea Software Congress (KSC), Dec 20-22, 2021 (Best paper award)

## 과제

게시된 과제 중 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 2건이다. ‘현재’는 연구실 게시 표기다.[^projects]

- NRF ERC 경북대 SW재난센터 참여 연구 (1그룹 SW재난 탐지), 2021.06.01 - 현재 (KRW 189,250,000, 2021R1A5A1021944)
- NRF 중견연구: Regression testing을 위한 효과적이고 효율적인 SW 유닛 Fuzzing, 2021.3.1-2024.2.29 (KRW 577,361,000, 2021R1A2C2009384)

## 수상

2021년 10월 13일–2026년 10월 13일 범위의 수상 4건이다. 학회 논문상은 연구실이 적은 학회 기간을 함께 표시했다.[^pubs]

- 2022-02 · 이아청, 「함수 관련도를 이용한 퍼징의 커버리지 향상」, KAIST 전산학부 Best Master’s Thesis Award
- 2021-12-17 · 이아청, 「POWER: Program Option-Aware Fuzzer for High Bug Detection Ability」, 전자신문 ICT 논문 공모 대제전 장려상
- 2024-05-27–31 (누리집 기재 학회 기간) · S. Moon, Y. Kim, M. Kim, S. Yoo, 「Ask the Mutants: Mutating Faulty Programs for Fault Localization」, ICST Most Influential Paper Award
- 2021-12-20–22 (누리집 기재 학회 기간) · 이아청, 김윤호, 김문주, 「유용한 커맨드 라인 옵션을 선택하여 커버리지와 오류 탐지 능력을 높이는 퍼징 기법」, KSC Best paper award

## 소식

2021년 10월 13일–2026년 10월 13일에 게시된 연구실 소식이다.[^home]

- 2026-05-10 · 김문주 교수가 제19회 IEEE ICST 2026을 주최한다고 연구실이 공지했다.
- 2024-06-10 · 연구실 이름을 Provable SW Lab에서 Software Testing and Verification (SW TV) Group으로 바꿨다고 공지했다.
- 2021-12-29 · SWTV 구성원이 설립한 VPlusLab의 소프트웨어 자동 테스팅 기술과 CROWN 2.0을 다룬 기사 세 편을 소개했다.

## 연락과 위치

- 교수 연구실: KAIST E3-1 전산학부 2434호(East wing).[^members][^faculty]
- 학생 연구실: E3-1 2438호.[^members]
- 교수 연구실 전화: 042-350-3543.[^members]

## 각주
[^home]: SWTV, 첫 화면의 연구 소개·Announcements. <https://swtv.kaist.ac.kr/> 관측 2026-10-27.
[^intro]: KAIST 전산학부, 소프트웨어 테스팅 및 검증 연구실 소개. 복잡한 소프트웨어의 오류 자동 검출·수정, 코드 분석에 의한 테스트 케이스 생성과 자동 디버깅을 설명한다. <https://cs.kaist.ac.kr/research/labView?sn=89&menu=64> 관측 2026-10-27.
[^faculty]: KAIST 전산학부, 교수진 명단의 김문주 부교수 항목. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-28.
[^members]: SWTV, Members. <https://swtv.kaist.ac.kr/members/> 관측 2026-10-28.
[^pubs]: SWTV, Publications. <https://swtv.kaist.ac.kr/publications/> 관측 2026-10-28.
[^projects]: SWTV, Projects. <https://swtv.kaist.ac.kr/projects/> 관측 2026-10-28.
[^pi]: Moonzoo Kim, Background·Research Interests. 자동 테스팅·디버깅, 변이 기반 프로그램 분석과 산업 적용을 연구 관심으로 적는다. <https://swtv.kaist.ac.kr/moonzoo/> 관측 2026-10-28.

[^p1]: A. Lee 외, M. Kim, IEEE/ACM ASE 2026 (2026). <https://doi.org/10.1145/3832783.3834497> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/international_conference/LASIK_ASE_2026.pdf> 관측 2026-10-28.
[^p2]: A. Lee, I. Ariq, Y. Kim, M. Kim, IEEE ICST 2022 (2022). <https://swtv.kaist.ac.kr/files/publications/international_conference/POWER-IEEEeXpress-2022017668.pdf> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/international_conference/POWER-IEEEeXpress-2022017668.pdf> 관측 2026-10-28.
[^p3]: R. S. Herlim, Y. Kim, M. Kim, IEEE ICST 2022 Testing Tools track (2022). <https://swtv.kaist.ac.kr/files/publications/international_conference/icst22-citrus.pdf> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/international_conference/icst22-citrus.pdf> 관측 2026-10-28.
[^p4]: Y. Kim, M. Kim, Korea Conference on Software Engineering (KCSE) (2022). <https://swtv.kaist.ac.kr/files/publications/domestic_conference/CONUZZ-KCSE22.pdf> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/domestic_conference/CONUZZ-KCSE22.pdf> 관측 2026-10-28.
[^p5]: L. Zhang, A. Lee, M. Kim, Korea Software Congress (KSC) (2023). <https://swtv.kaist.ac.kr/files/publications/domestic_conference/Challenges-in-Automated-Unit-Testing-of-Complex-C-Programs-v13.pdf> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/domestic_conference/Challenges-in-Automated-Unit-Testing-of-Complex-C-Programs-v13.pdf> 관측 2026-10-28.
[^p6]: R. S. Herlim, S. Hong, Y. Kim, M. Kim, SSBSE 2021 (2021). <https://swtv.kaist.ac.kr/files/publications/international_conference/ssbseRENE21-evoStudy.pdf> 초록 기준(연구실 게시 논문 원문 초록). 초록 원문 <https://swtv.kaist.ac.kr/files/publications/international_conference/ssbseRENE21-evoStudy.pdf> 관측 2026-10-28.

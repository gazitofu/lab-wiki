# 복잡도 및 실수 연산 연구실 (Complexity and Real Computation Laboratory)

**KAIST 전산학부 · 지글러 마틴 부교수**

- 분야: 실수와 연속 자료의 계산, 계산 가능성과 복잡도, 프로그램의 의미와 올바름 검증
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 프로그램 분석·검증[^p3]
- 홈페이지: <http://kaist.theoryofcomputation.asia>
- 근거와 출처: [복잡도 및 실수 연산 연구실 근거 페이지](theoryofcomputation-sources.md)

> 실수·함수처럼 연속적으로 변하는 자료를 컴퓨터가 어떻게 표현하고 계산해야 하는지, 그 계산의 정확성과 필요한 시간·기억 공간을 어떻게 보장할지 연구한다.[^home][^research][^lab]

## 무엇을 연구하나

컴퓨터는 비트(두 가지 값 가운데 하나를 담는 정보 단위)와 정수처럼 구분되는 자료를 처리한다. 반면 과학과 공학의 계산에는 실수(수직선 위의 점으로 나타내는 수), 함수(입력마다 출력을 정하는 대응), 미분방정식(함수와 그 변화율 사이의 관계를 나타내는 방정식)이 등장한다. 이 연구실은 이러한 연속 자료를 다루는 전산학의 기초부터 구현과 응용까지 연구한다. 연구 소개는 단순히 계산이 가능한지를 묻는 계산 가능성과, 그 계산에 필요한 시간·기억 공간 등을 따지는 계산 복잡도를 구분한다.[^home][^research]

한 갈래는 연속 자료를 정확하게 다루는 프로그램이다. 누리집은 계산 도중 근삿값의 정밀도를 조절해 실수 연산을 지원하는 소프트웨어와, 그 위에서 벡터(덧셈과 수의 곱셈 규칙을 만족하는 수학적 대상)와 행렬(성분을 행과 열로 배열한 수학적 대상)을 다루는 방법을 소개한다. 대표 논문 3은 임의의 실수를 기본 자료형으로 쓰는 언어 ERC(Exact Real Computation)를 제안하고, 프로그램의 의미를 수학적으로 정한 뒤 올바름을 증명하는 논리를 함께 제시한다. 대표 논문 6은 ERC의 기본 연산에 계산 비용을 부여해 다항 시간 계산과의 대응을 보인다.[^home][^p3][^p6]

다른 갈래는 연속 자료의 표현이 계산 비용에 미치는 영향이다. 같은 수나 함수도 컴퓨터에 전달하는 부호화 방식에 따라 계산 성질이 달라진다. 대표 논문 1은 연속 자료의 표현과 표현 간 변환에 정량적인 연속성 기준을 세우고, 함수의 연속성과 부호를 변환하는 계산의 연속성 사이 관계를 정량적으로 다룬다. 대표 논문 2는 함수를 변수로 받는 다항식(변수의 거듭제곱에 계수를 곱한 항들을 더한 식)에 차수를 정의해 고차 계산의 자원 사용을 분석한다.[^p1][^p2]

함수와 방정식을 실제로 계산할 때 필요한 조건도 다룬다. 연구 소개는 상미분방정식(독립변수 하나에 대한 변화율을 포함한 방정식)과 편미분방정식(여러 독립변수에 대한 변화율을 포함한 방정식)의 풀이를 주요 배경으로 든다. 대표 논문 4는 적분 가능한 함수의 계산을 다루는 이론을 제안하고, 대표 논문 5는 제곱적분 가능 함수의 다항 시간 계산에 서로 다른 정의를 검토한다.[^research][^p4][^p5]

## 주요 연구 주제

### 연속 자료의 표현과 계산 복잡도

수나 함수의 표현과 그 표현을 바꾸는 계산의 비용을 함께 연구한다. 정량적 허용성을 통해 연속 자료를 담는 표현을 평가하고, 연속 자료의 함수와 그 부호를 변환하는 계산 사이의 정량적 관계를 밝힌다. 고차 다항식 연구에서는 함수 자체를 받는 변수와 값만 받는 변수를 함께 다뤄 차수와 합성의 관계를 밝힌다.[^p1][^p2]

### 실수 프로그램의 의미와 올바름

ERC는 실수 연산과 극한을 지원하는 명령형 언어다. 연구는 표시적 의미론으로 프로그램의 의미를 정하고, 특정 정수 연산과 실수 변환을 제한한 논리 체계의 판정 가능성을 증명한다. 또한 사전 조건과 사후 조건을 적는 호어 논리를 확장해 프로그램의 종료와 결과의 올바름을 함께 증명하도록 한다.[^p3]

대표 논문 6은 ERC의 기본 연산에 비트 비용(비트 단위의 처리를 기준으로 세는 계산 비용)을 부여한다. 이 비용이 다항식으로 제한되는 실수 함수 계산과 튜링 기계(기호를 읽고 쓰며 정해진 규칙에 따라 계산하는 추상 기계)의 다항 시간 계산이 서로 대응하도록 비용을 정한다. iRRAM 소프트웨어 구현의 실행 시간 측정도 이론적 성능 예측을 뒷받침한다.[^p6]

### 함수 공간과 방정식의 계산

적분 가능한 복소함수의 공간에서 계산 복잡도를 다루기 위해 서로 다른 매개화의 관계를 연구한다. 대표 논문 4는 함수의 변화, 푸리에 급수의 수렴 속도, 계단함수에 의한 근사 속도에 바탕을 둔 표현 사이의 선형 동등성을 보인다. 대표 논문 5는 제곱적분 가능 함수를 다항 시간에 계산한다는 두 정의가 특정 복잡도 가정 아래 서로 포함되지 않음을 보인다.[^p4][^p5]

## 대표 논문

연속 자료의 표현, 고차 계산 복잡도, 프로그램 검증, 함수 공간의 계산을 중심으로 골랐다. 「쉽게 말하면」은 각주에 밝힌 초록만을 근거로 썼다. arXiv 사전 공개본은 발표처에 그 상태를 표시했다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 교수 역할 |
|---|---|---|---|---|
| 1 | 2025 | [Quantitative Coding and Complexity Theory of Continuous Data: Part I: Motivation, Definition, Consequences](https://doi.org/10.1145/3705609) · Journal of the ACM | 연속 자료를 어떤 방식으로 표현해야 계산에 적합한지를 정량적으로 다룬다. 표현의 허용성에 다항식·선형 기준을 도입하고, 함수의 연속성과 그 부호를 변환하는 계산의 연속성 사이 관계를 정량적으로 증명했다.[^p1] | 마지막 저자 |
| 2 | 2025 | [Degrees of Second and Higher-Order Polynomials](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.42) · FSTTCS 2025 | 함수를 변수로 받는 다항식에도 계산량의 증가를 구분할 차수를 정의했다. 덧셈·곱셈·최댓값을 쓰는 식으로 차수를 나타내고, 다항식을 합성할 때 차수가 어떻게 바뀌는지 보였다. 이를 고차 다항식의 계층으로 확장했다.[^p2] | 마지막 저자 |
| 3 | 2024 | [Semantics, Specification Logic, and Hoare Logic of Exact Real Computation](https://doi.org/10.46298/lmcs-20(2:17)2024) · Logical Methods in Computer Science | 실수를 정확하게 다루는 명령형 언어 ERC와 그 수학적 의미를 제시했다. 정수 연산과 실수 변환을 제한한 논리의 판정 가능성을 증명하고, 프로그램이 종료하며 조건에 맞는 답을 내는지 증명하는 호어 논리를 확장했다.[^p3] | 마지막 저자 |
| 4 | 2025 | [Second-Order Parameterizations for the Complexity Theory of Integrable Functions](https://doi.org/10.48550/arXiv.2506.11210) · arXiv 사전 공개본 | 적분 가능한 함수 공간의 계산 복잡도를 다루는 통합 이론을 제안했다. 실수 단위 구간의 적분 가능한 복소함수에 대해 함수의 변화, 푸리에 급수의 수렴, 계단함수 근사에 바탕을 둔 세 매개화가 서로 선형적으로 동등함을 증명했다.[^p4] | 마지막 저자 |
| 5 | 2026 | [What is a POLYNOMIAL-TIME Computable L2-Function?](https://doi.org/10.48550/arXiv.2601.17078) · arXiv 사전 공개본 | 제곱적분 가능 함수를 다항 시간에 계산한다는 두 가지 자연스러운 정의를 제시했다. 복잡도 클래스(문제를 필요한 계산 자원에 따라 묶은 범주) FP₁이 #P₁을 포함하지 않는다는 가정 아래 두 정의 사이에 포함 관계가 없음을 보였다.[^p5] | 마지막 저자 |
| 6 | 2026 | [Algorithmic Cost in "Exact Real Computation"](https://doi.org/10.48550/arxiv.2608.23603) · arXiv 사전 공개본 | ERC의 기본 연산에 비트 비용을 부여해 다항 비용으로 계산하는 실수 함수와 튜링 기계가 다항 시간에 계산하는 실수 함수가 서로 대응하도록 했다. iRRAM C++ 소프트웨어의 실행 시간 측정은 이론적 성능 예측을 뒷받침했다.[^p6] | 마지막 저자 |

## 교수와 전문 분야

지글러 마틴(Martin Ziegler) 부교수는 독일 Paderborn대학교에서 전산학 박사 학위와 교수자격을 각각 2002년과 2008년에 취득했다. 2010–2015년 TU Darmstadt 응용수학과 교수로 재직했고, 2015년 KAIST 전산학부에 부임했다. 전산학부는 전공을 전산이론, 복잡도, 실수 연산으로 적는다.[^prof][^faculty]

최근 논문의 전문 분야는 연속 자료의 표현과 계산 복잡도, 실수 계산 언어의 수학적 의미와 프로그램 검증, 적분 가능한 함수의 계산 이론으로 이어진다. 대표 논문 여섯 편 모두 Martin Ziegler가 마지막 저자다.[^p1][^p2][^p3][^p4][^p5][^p6]

## 응용 분야

연구 소개는 유체역학, 계산 재료과학, 우주 임무 설계를 실수 계산이 필요한 분야로 든다. 누리집은 실수를 다루는 소프트웨어에서 출발해 벡터·행렬·함수와 미분방정식 계산을 연결한다. 이러한 계산에서 근사 오차와 계산 자원을 함께 다루는 것이 연구의 방향이다.[^research][^home]

## 구성원

2026년 10월 30일 Members 페이지 기준, 학생 3명과 외부 자문 1명이다. 과정과 역할은 누리집 표기를 따른다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| Donghyun Lim | 박사과정 (on leave) |  | 1, 2 |
| 박세훈 | 석사과정 |  |  |
| Jaden Jorradol | 석사과정 |  |  |
| Alexander Stoimenov | external consultant | Computational Knot Theory |  |

## 졸업생과 이전 구성원

Members 페이지 Alumni 칸의 12명이다. 학위·과정과 연도, 진로는 해당 목록의 표기다. 학위 외에 인턴과 방문 연구교수로 적힌 이전 구성원도 포함한다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Nguyên Trần Bảo | intern (2025) |  |
| August Lykke Thomsen | MSc dual degree with DTU |  |
| Sewon Park | PhD (2021) | Postdoc at Kyoto University |
| Jiman Hwang | M.S. (2021) |  |
| Junhee Cho | M.S. (2018) | Google |
| Seungwoo Schin | M.S. (2019) | founder of 미국주식 사관학교 |
| Chansu Park | M.S. (2019) | Skelter Labs |
| Dongsong Seon | M.S. (2019) | KRAFTON Game Union |
| Hyunwoo Lee | M.S. (2020) | Craft Technologies |
| Seokbin Lee | Undergrad Researcher (2019) | combined MSc/PhD at Georgia Tech |
| Ivan Koswara | M.S. (2020) | PhD student at NUS |
| Svetlana Selivanova | KRF BrainPool Visiting Research Professor (2018~2022) |  |

## 최근 논문 목록 (2021–2026)

연속 자료의 부호화, 함수의 계산 복잡도, 실수 프로그램의 검증, 편미분방정식의 계산을 다룬다. 공개 서지 OpenAlex의 KAIST 소속 저자 목록을 바탕으로 개별 논문 페이지의 서지를 함께 쓴 목록이다. 학술지·학회 논문과 arXiv 사전 공개본을 함께 싣고 사전 공개본은 발표처에 표시했다.[^oa][^p1][^p2][^p3][^p4][^p5][^p6][^pde]

**2026**

- Aras Bacho, Svetlana Selivanova, Martin Ziegler. "What is a Polynomial-Time Computable Square-Integrable Function?". *Lecture Notes in Computer Science*.
- Jihoon Hyun, Holger Thies, Martin Ziegler. "Algorithmic Cost in "Exact Real Computation". *arXiv:2608.23603 (사전 공개본, 2026-08-20)*.
- Aras Bacho, Svetlana Selivanova, Martin Ziegler. "What is a POLYNOMIAL-TIME Computable L2-Function?". *arXiv:2601.17078 (사전 공개본, 2026-01-23)*.

**2025**

- Aras Bacho, Martin Ziegler. "Second-Order Parameterizations for the Complexity Theory of Integrable Functions". *Lecture Notes in Computer Science*.
- Donghyun Lim, Martin Ziegler. "Degrees of Second and Higher-Order Polynomials". *FSTTCS 2025, LIPIcs 360, 42:1–42:20 (arXiv:2305.03439 사전 공개본 포함)*.
- Aras Bacho, Martin Ziegler. "Second-Order Parameterizations for the Complexity Theory of Integrable Functions". *arXiv:2506.11210 (사전 공개본, 2025-06-12)*.

**2024**

- Donghyun Lim, Martin Ziegler. "Quantitative Coding and Complexity Theory of Continuous Data: Part I: Motivation, Definition, Consequences". *Journal of the ACM 72(1), 4:1–4:39 (온라인 2024, 인쇄 2025)*.
- Klaus Meer, Martin Ziegler. "Software Testing in Computable Analysis". *Lecture Notes in Computer Science*.
- Sewon Park, Franz Brauße, Pieter Collins, SunYoung Kim, Michal Konečný, Gyesik Lee, Norbert Müller, Eike Neumann, Norbert Preining, Martin Ziegler. "Semantics, Specification Logic, and Hoare Logic of Exact Real Computation". *Logical Methods in Computer Science 20(2), 17*.

**2023**

- Ivan Koswara, Gleb Pogudin, Svetlana Selivanova, Martin Ziegler. "Bit-complexity of classical solutions of linear evolutionary systems of partial differential equations". *Journal of Complexity 76, 101727*.

**2022**

- Franz Brauße, Pieter Collins, Martin Ziegler. "Computer Science for Continuous Data". *Lecture Notes in Computer Science*.

**2021**

- Svetlana Selivanova, Florian Steinberg, Holger Thies, Martin Ziegler. "Exact Real Computation of Solution Operators for Linear Analytic Systems of Partial Differential Equations". *Lecture Notes in Computer Science*.
- Ivan Koswara, Gleb Pogudin, Svetlana Selivanova, Martin Ziegler. "Bit-Complexity of Solving Systems of Linear Evolutionary Partial Differential Equations". *Lecture Notes in Computer Science*.

## 연구 발표 소식

Talks 페이지에 실린 2021년 10월 13일–2026년 10월 13일 범위의 연구 발표 3건이다.[^talks]

- 2026-08 · Jaden Jorradol이 부산 WAAC 2026에서 「Calculation of the signature with Gordon-Litherland formula」를 발표했다.
- 2026-03 · Sehun Park이 교토 CCC 2026에서 「Parallelizing Picard Iterations」를 발표했다.
- 2024-10 · Jaden Jorradol이 니스 CCC 2024에서 「iRRAM for Knots」를 발표했다.

## 연락과 위치

- 교수연구실: KAIST 전산학부 N1 506호[^prof][^members]
- 전화: +82-42-350-3568[^members]
[^home]: 연구실 첫 화면. <http://kaist.theoryofcomputation.asia> 관측 2026-10-27.
[^lab]: 전산학부 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=97&menu=64> 관측 2026-10-27.
[^faculty]: 전산학부 교수진. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-30.
[^prof]: 전산학부 지글러 마틴 상세. <https://cs.kaist.ac.kr/people/view?idx=517&kind=faculty&menu=160> 관측 2026-10-30.
[^research]: Research. <http://kaist.theoryofcomputation.asia/research> 관측 2026-10-30.
[^members]: Members. <http://kaist.theoryofcomputation.asia/members> 관측 2026-10-30.
[^talks]: Talks. <http://kaist.theoryofcomputation.asia/talks> 관측 2026-10-30.
[^oa]: OpenAlex KAIST 소속 저자 논문 목록. <https://api.openalex.org/works?filter=raw_author_name.search:Martin%20Ziegler,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> 관측 2026-10-30.
[^p1]: D. Lim, M. Ziegler, Journal of the ACM 72, 4:1–4:39 (온라인 2024-11-29). <https://doi.org/10.1145/3705609> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?filter=raw_author_name.search:Martin%20Ziegler,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> OpenAlex 항목 W4404836487. 관측 2026-10-30.
[^p2]: D. Lim, M. Ziegler, FSTTCS 2025, Leibniz International Proceedings in Informatics 360, 42:1–42:20 (온라인 2025-12-09). <https://doi.org/10.4230/lipics.fsttcs.2025.42> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2025.42> 관측 2026-10-30.
[^p3]: S. Park 외, M. Ziegler, Logical Methods in Computer Science 20, 17 (온라인 2024-06-24). <https://doi.org/10.46298/lmcs-20(2:17)2024> 초록 기준(출판사 논문 페이지). 초록 원문 <https://lmcs.episciences.org/13822> 관측 2026-10-30.
[^p4]: A. Bacho, M. Ziegler, arXiv:2506.11210 (사전 공개본) (온라인 2025-06-12). <https://doi.org/10.48550/arXiv.2506.11210> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.11210> 관측 2026-10-30.
[^p5]: A. Bacho, S. Selivanova, M. Ziegler, arXiv:2601.17078 (사전 공개본) (온라인 2026-01-23). <https://doi.org/10.48550/arXiv.2601.17078> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2601.17078> 관측 2026-10-30.
[^p6]: J. Hyun, H. Thies, M. Ziegler, arXiv:2608.23603 (사전 공개본) (온라인 2026-08-20). <https://doi.org/10.48550/arxiv.2608.23603> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?filter=raw_author_name.search:Martin%20Ziegler,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> OpenAlex 항목 W7204245569. 관측 2026-10-30.
[^pde]: I. Koswara, G. Pogudin, S. Selivanova, M. Ziegler, “Bit-complexity of classical solutions of linear evolutionary systems of partial differential equations”, Journal of Complexity 76, 101727 (2023). FSTTCS 2025 논문집의 참고문헌 18. <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2025.42> <https://doi.org/10.1016/j.jco.2022.101727> 관측 2026-10-30.

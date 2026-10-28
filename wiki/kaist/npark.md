# 빅데이터 분석 및 학습 연구실 (Laboratory of Big Data Analytics and Learning, BigDyL in WISE)

**KAIST 전산학부·김재철AI대학원·데이터사이언스대학원·AI수학대학원 · 박노성 부교수**

- 분야: 그래프·신호 처리와 미분방정식을 이용한 딥러닝, 과학 계산, 생성 모델과 대형 언어 모델, 표 자료의 표현 학습, 추천, 시계열·시공간 자료의 생성·예측·이상 탐지
- 대분야: 컴퓨팅·AI
- 태그: 그래프 기계학습·지식 그래프[^lab][^home], 과학·공학 AI[^lab][^p1], 생성 인공지능[^home][^p8], 대형 언어 모델[^home][^p4], 추천 시스템[^p6]
- 홈페이지: <https://sites.google.com/view/npark>
- 근거와 출처: [BigDyL 근거 페이지](npark-sources.md)

> 그래프·신호 처리와 미분방정식의 관점으로 학습 모델을 설계하고, 과학 계산부터 표 자료, 추천, 시간에 따라 변하는 자료의 생성·예측까지 연구하는 연구실이다.[^lab][^home]

## 무엇을 연구하나

KAIST 전산학부 박노성 부교수가 이끄는 BigDyL은 웹·산업·과학 환경의 문제를 인공지능으로 푸는 연구실이다. 이름의 WISE는 Web, Industrial, and Scientific Environments를 뜻한다.[^lab][^home] 연구의 공통 기반은 기계학습(자료에서 규칙을 배우는 계산 방법)과 딥러닝(계산 단계를 깊게 쌓은 신경망으로 자료의 표현을 학습하는 방법)이다. 신경망은 연결된 계산 단위들을 통해 입력을 출력으로 바꾸며 학습하는 모델이다. 학과 소개는 과학적 지식을 바탕으로 이러한 모델을 개선·설계하는 일과, 그 모델로 과학 문제를 푸는 일을 함께 강조한다.[^lab]

첫 갈래는 그래프(대상과 관계를 점과 선으로 나타낸 구조)를 이용한 학습과 그래프 신호 처리(그래프에 주어진 값을 연결 구조에 따라 분석·변환하는 방법)다. 누리집은 그래프 합성곱 신경망(연결된 대상의 정보를 모아 각 대상의 표현을 계산하는 신경망)과 기하 학습(자료의 형태·대칭 같은 기하학적 성질을 반영하는 학습)을 현재 연구로 든다.[^home] 트랜스포머(자기 주의를 중심으로 자료 사이의 관계를 학습하는 신경망 구조)의 자기 주의(입력 요소들이 서로의 정보를 얼마나 반영할지 계산하는 기법)를 그래프 필터(그래프 신호의 성분을 선택·변환하는 연산)로 해석해 다시 설계한다. 대표 논문은 자료의 표현이 서로 구별되지 않게 되는 과도한 평활화 문제를 다루고, 언어 모델(글의 확률적 특성을 학습하는 모델)의 내부 계산도 필터들의 조합으로 해석한다.[^p3][^p4]

둘째 갈래는 미분방정식(미지의 함수와 그 변화율 사이의 관계를 나타낸 식)을 바탕으로 하는 딥러닝과 과학 계산이다. 누리집은 물리 정보 신경망(학습할 때 물리 방정식의 관계를 반영하는 신경망), 과학 파운데이션 모델(여러 과학 문제에 활용할 수 있도록 학습하는 기반 모델), 연산자 학습(함수를 입력받아 함수를 내보내는 관계를 학습하는 방법)을 연구한다고 적는다.[^home] 대표 논문에서는 물리계의 조건을 정하는 값이 달라지는 편미분방정식(여러 변수에 대한 변화율을 포함하는 미분방정식)의 해를 학습한다. 또 측정 자료에서 주기 패턴을 배워 관측한 구간 밖의 신호를 예측하는 신경망 구조를 제안한다.[^p1][^p2]

셋째 갈래는 실제 자료를 표현하고 예측하거나 새로 만드는 일이다. 표 자료의 표현 학습(분석에 쓸 특징을 모델이 자료에서 학습하는 방법), 생성 모델(자료의 분포를 학습해 새 자료를 만들어 내는 모델), 대형 언어 모델을 연구한다. 추천에서는 이용자·항목의 기록을 이용하는 협업 필터링과, 행동 순서를 반영하는 순차 추천을 다룬다. 시계열(시간 순서로 놓인 자료)과 시공간 자료(시간과 장소에 따라 달라지는 자료)에서는 생성·예측·이상 탐지(기대되는 양상과 다른 자료를 찾는 일)를 연구한다.[^home] 표 자료에 쓰는 자기 주의 구조를 바꾸는 연구, 이용자의 행동 순서에서 다음 항목을 추천하는 연구, 예측이 실제 변화보다 늦게 움직이는 문제를 다루는 연구, 규칙·불규칙 시간 간격의 시계열을 만드는 연구가 이에 해당한다.[^p5][^p6][^p7][^p8]

## 주요 연구 주제

### 과학 계산과 주기 신호

물리계를 설명하는 방정식의 조건이 달라질 때 그 해를 학습하는 것이 한 축이다. P²INNs(Parameterized Physics-informed Neural Networks)는 방정식의 조건을 정하는 매개변수 정보를 모델 안에서 표현해 여러 조건의 해를 다룬다.[^p1] 주기 신호 연구는 시간이나 공간에서 반복되는 패턴을 측정값으로부터 추출하고, 그 패턴으로 신호를 표현하는 신경망을 제안한다. 논문은 미분방정식의 주기적인 해, 시계열의 빠진 값 채우기, 관측 구간 밖 예측에 이 방법을 적용한다.[^p2]

### 그래프·신호 처리와 학습 구조

그래프 필터를 학습 모델의 구성 요소로 삼는다. GFSA(Graph-Filter-based Self-Attention)는 자기 주의를 그래프 신호 처리 관점으로 재설계해 영상·글·그래프·음성·코드 분류 과제에서 평가한다.[^p3] HADES(Hierarchical ADaptive filter bank for Efficient SSMs)는 Mamba2 언어 모델을 적응형 필터들의 조합으로 해석한다. SSM은 State-Space Model의 줄임말로, 내부 상태의 변화와 관측값 사이의 관계를 나타내는 상태 공간 모델이다. HADES는 전체적인 저주파 성분과 국소적인 고주파 성분을 맡는 필터를 구분한 계층 구조를 제안한다.[^p4]

### 정형 데이터와 추천

표 자료의 행과 열에 담긴 관계를 표현하는 방법을 연구한다. 표 자료용 자기 주의 연구는 행렬 다항식을 이용해 기존 연산을 바꾸고, 자료 표현이 서로 비슷해지는 현상을 다룬다.[^p5] 순차 추천에서는 TV-Rec(Time-Variant Convolutional Filters for Sequential Recommendation)이 행동 순서의 위치에 따라 달라지는 필터를 제안한다. 이 필터로 이용자 행동 사이의 관계를 포착하며, 고정된 필터와 자기 주의를 대체한다.[^p6]

### 시계열 예측과 생성

예측값이 실제 변화보다 늦게 움직이는 현상에 주목한다. 연속 시간 GRU(Gated Recurrent Unit, 이전 상태의 정보를 얼마나 유지·반영할지 조절하는 순환 신경망의 계산 단위)를 상미분방정식(하나의 변수에 대한 변화율을 포함하는 미분방정식)으로 구성하고, 시간에 따른 변화율을 학습에 반영해 예측 지연을 줄이는 방법을 제안한다.[^p7] 시계열 생성에서는 조건부 스코어(조건부 확률 밀도의 로그를 자료값에 대해 미분한 값)를 학습하고, 그 학습에 맞는 잡음 제거 목적식을 도출한다. 같은 틀에서 규칙적인 시간 간격과 불규칙한 시간 간격의 시계열을 다룬다.[^p8]

## 대표 논문

연구 갈래를 고르게 보여 주도록 KAIST 재직 시기의 논문 8편을 골랐다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다. arXiv 판을 설명하는 항목은 그 판본을 표시했으며, 「Neural Functions」와 「TSGM」은 arXiv 사전 공개본을 기준으로 적었다.

| 번호 | 연도 | 논문 · 발표처·판본 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2024 | [Parameterized Physics-informed Neural Networks for Parameterized PDEs](https://proceedings.mlr.press/v235/cho24b.html) · ICML | 물리 방정식의 조건이 달라질 때마다 해를 구하는 문제를 다룬다. 조건을 정하는 값의 표현을 모델에 넣는 P²INNs를 제안해 여러 조건의 해를 학습하고, 논문의 시험 문제에서 정확도와 매개변수 효율을 평가했다.[^p1] |
| 2 | 2025 | [Neural Functions for Learning Periodic Signal](https://arxiv.org/abs/2506.09526) · arXiv 사전 공개본 | 시간이나 공간에서 반복되는 신호의 패턴을 측정값으로부터 뽑아내는 신경망을 제안했다. 미분방정식의 주기적인 해와 실제 시계열의 빠진 값 채우기·관측 구간 밖 예측에 적용했다.[^p2] |
| 3 | 2024 | [Graph Convolutions Enrich the Self-Attention in Transformers!](https://arxiv.org/abs/2312.04234) · NeurIPS 채택, arXiv 판 | 깊은 트랜스포머에서 자료 표현이 서로 구별되지 않게 되는 문제를 다룬다. 자기 주의를 그래프 필터로 보고 GFSA를 제안했으며, 영상·글·그래프·음성·코드 과제에서 성능을 평가했다.[^p3] |
| 4 | 2026 | [Graph Signal Processing Meets Mamba2: Adaptive Filter Bank via Delta Modulation](https://arxiv.org/abs/2603.22333) · ICLR, arXiv 판 | Mamba2 언어 모델의 내부 계산을 그래프 필터들의 조합으로 해석하고 HADES를 제안했다. 공유 필터와 전문가 필터를 계층적으로 배치했으며, 언어 모델링·상식 추론·긴 문맥 검색의 시험에서 원래 매개변수의 58.9%로 기준 모델과 비슷한 성능을 보고했다.[^p4] |
| 5 | 2024 | [Polynomial-based Self-Attention for Table Representation Learning](https://proceedings.mlr.press/v235/kim24ae.html) · ICML | 표 자료를 학습하는 트랜스포머에서도 자료 표현이 서로 비슷해지는 문제가 생김을 보였다. 행렬 다항식으로 자기 주의 층을 바꿔 이 현상과 표현 성능을 평가했다.[^p5] |
| 6 | 2025 | [TV-Rec: Time-Variant Convolutional Filter for Sequential Recommendation](https://arxiv.org/abs/2510.25259) · NeurIPS, arXiv 판 | 이용자 행동 순서의 위치에 따라 달라지는 필터를 이용해 다음 항목을 추천하는 TV-Rec을 제안했다. 고정된 필터와 자기 주의를 대체하며, 공개 자료에서 추천 성능과 계산 효율을 평가했다.[^p6] |
| 7 | 2024 | [Addressing Prediction Delays in Time Series Forecasting: A Continuous GRU Approach with Derivative Regularization](https://arxiv.org/abs/2407.01622) · KDD 채택, arXiv 판 | 예측값이 실제 변화보다 늦게 움직이는 문제를 다룬다. GRU를 연속 시간 모델로 바꾸고 시간 변화율을 학습에 반영해, 여러 자료에서 예측 오차와 지연을 평가했다.[^p7] |
| 8 | 2025 | [TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models](https://arxiv.org/abs/2511.21335) · arXiv 사전 공개본 | 시계열의 조건부 스코어를 배우는 신경망과 이에 맞는 잡음 제거 학습 목적식을 제안했다. 규칙적·불규칙한 시간 간격의 자료를 생성하고, 생성 결과의 품질과 다양성을 평가했다.[^p8] |

## 교수와 전문 분야

박노성 교수는 전산학부 교수진 명단에서 부교수로 소개된다.[^faculty] 개인 소개는 전산학부를 본래 소속으로, 김재철AI대학원·데이터사이언스대학원·AI수학대학원과 Auto-ID Lab Korea를 Adjunct로 적는다. 2024년 2월 연구실과 함께 KAIST 전산학부로 옮겼다.[^prof][^home] 이전에는 연세대학교(2020–2024), George Mason University(2018–2019), University of North Carolina at Charlotte(2016–2018)에서 재직했다. University of Maryland, College Park에서 2016년 컴퓨터과학 박사학위를 받았고, 석사는 KAIST, 학사는 숭실대학교에서 받았다.[^prof]

개인 소개는 데이터 마이닝과 기계학습을 전문 분야로 적으며, 과학 기계학습·생성 학습·시공간 및 시계열 처리·추천을 응용 분야로 든다. TMLR 편집위원과 ICML·ICLR·NeurIPS·AAAI 등의 영역위원장 활동, CIKM 2025 대회장 활동도 소개한다.[^prof] 최근 논문을 함께 보면 전문 분야는 과학 계산용 신경망, 그래프·신호 처리에 기반한 학습 구조, 표 자료·추천·시계열 모델 설계로 정리할 수 있다.[^p1][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

과학 계산에서는 조건이 달라지는 물리 방정식의 해를 학습하고, 주기적인 신호를 표현·예측한다.[^p1][^p2] 자료 서비스에서는 이용자 행동 순서에 따른 추천과 표 자료의 표현 학습을 다룬다.[^p5][^p6] 시간에 따라 변하는 자료에서는 예측 지연을 다루고, 규칙적·불규칙한 간격의 자료를 생성한다.[^p7][^p8] HADES 논문은 언어 모델링·상식 추론·긴 문맥 검색을 평가 대상으로 삼는다.[^p4]

## 구성원

2026년 10월 28일 Members 페이지 기준으로 교수 외 박사후연구원 1명, 박사과정 표기 7명, 석사과정 표기 10명, 학부 인턴 1명이다. Yongseok Kwon은 원문이 Ph.D. (석박통합)으로 적는다. Jongwoo Kim과 Jiwon Jeong은 Prof. Mun Yi가 주지도교수이고, Yongseok Kwon은 Prof. Donghwan Kim과 공동지도한다. 과정·시작 연월은 누리집 표기다.[^members] “대표 논문 참여”는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Jeongwhan Choi | 박사후연구원 (전문연구원) | 2025.09 ~ Present | 3, 5, 6 |
| Sheoyon Jhin | 박사과정 | 2025.03 ~ Present | 7 |
| Jayoung Kim | 박사과정 | 2024.09 ~ Present | 3, 5 |
| Hyowon Wi | 박사과정 | 2024.09 ~ Present | 3, 5 |
| Yehjin Shin | 박사과정 | 2024.09 ~ Present | 3, 4, 5, 6 |
| Jihyeon Hur | 박사과정 | 2026.03 ~ Present |  |
| Jongwoo Kim | 박사과정 | 2024.03 ~ Present |  |
| Yongseok Kwon | 박사과정 (석박통합) | 2026.03 ~ Present |  |
| Sumin Park | 석사과정 | 2024.09 ~ Present |  |
| Jaehyun Park | 석사과정 | 2024.09 ~ Present |  |
| Seojin Kim | 석사과정 | 2024.09 ~ Present | 4, 6, 7 |
| Woosung Kang | 석사과정 | 2025.03 ~ Present |  |
| Jonghyeok Shin | 석사과정 | 2025.09 ~ Present |  |
| Inhyeok Jeong | 석사과정 | 2025.09 ~ Present |  |
| Jiwon Jeong | 석사과정 | 2025.03 ~ Present |  |
| Junyeong Song | 석사과정 | 2026.03 ~ Present |  |
| Sehun Lim | 석사과정 | 2026.03 ~ Present |  |
| Mingi Jo | 석사과정 | 2026.03 ~ Present |  |
| Minseo Kim | 학부 인턴 |  |  |

## 졸업생과 이전 구성원

Members 페이지의 Alumni & Past Members 35행이다. 연세대학교 등 KAIST 부임 전 기관의 지도 학생과 이전 인턴도 포함하며, 날짜를 적은 일부 인턴 경력을 제외하면 학위 취득·연구실 이탈 연도는 적혀 있지 않다. 진로는 해당 명단의 표기이고, 현재 구성원으로도 실린 사람이 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Youn-Yeol Yu | Part-time Ph.D. in AI at Yonsei | Returned to his workplace, LG Display |
| Jeongwhan Choi | Ph.D. in AI at Yonsei | Joined KAIST BigDyL as a postdoc |
| Seonkyu Lim | Part-time Ph.D. in AI at Yonsei | Returned to his workplace, the Korea Financial Telecommunications and Clearings Institute |
| Sheoyon Jhin | Master in AI at Yonsei | Joined KAIST BigDyL  as a Ph.D. student |
| Yehjin Shin | Master in CS at Yonsei | Joined KAIST BigDyL as a Ph.D. student |
| Hyowon Wi | Master in CS at Yonsei | Joined KAIST BigDyL as a Ph.D. student |
| Jayoung Kim | Master in AI at Yonsei | Joined KAIST BigDyL  as a Ph.D. student |
| Jinsung Jeon | Ph.D. in AI at Yonsei | Joined UCSD for his visiting postdoc under the supervision of Julian McAuley |
| Woojin Cho | Master in AI at Yonsei | Telefix |
| Jaehyun Park | Undergraduate intern | Joined KAIST BigDyL as a Master student |
| Seojin Kim | Undergraduate intern | Joined KAIST BigDyL as a Master student |
| Chaejeong Lee | Master in AI at Yonsei | Joined Korea Telecom as a researcher |
| Seoyoung Hong | Master in AI at Yonsei | Joined Boeing Korea as an ML researcher |
| Seungji Kook | Master in AI at Yonsei | Joined LG Innotek |
| Seunghyun Cho | Master in AI at Yonsei | Joined CJ |
| Minju Jo | Master in AI at Yonsei | Joined LG CNS and will join Sorbonne University for Ph.D. under the supervision of Prof. Patrick Gallinari |
| Jaehoon Lee | Master in CS at Yonsei | Joined LG AI Research |
| Sujie Kim | Part-time Master in Engineering at Yonsei | Returned to her workplace, LG U+ |
| Jihyeon Hyeong | Graduate intern from 2020 to 2021 at Yonsei AI | Joined Max Planck Institute for Ph.D |
| Jeehyun Hwang | Undergraduate intern from 2019 to 2021 | Joined UCLA for Ph.D. in Computer Science under the supervision of Prof. Wei Wang |
| Heejoo Shin | Undergraduate intern at 2021 | Joined UCSD for Master in Computer Science |
| Jeonghak Kim | Undergraduate intern at 2021 | Joined Kakao as a data engineer |
| Taeyong Kong | Advising remotely during the last two semesters of his Master's degree while he is working in Human ICT | Human ICT |
| Solhee Park | Undergraduate intern at 2021 | Joined Hynix |
| Jaeeun Jung | Undergraduate intern at 2021 | Joined Kakao as a researcher in a recommendation team |
| Ganghyeon Park | Undergraduate intern at 2020 | Joined Kakao as a developer |
| Seunghyun Hwang | Undergraduate intern at 2020 | Joined Purdue University for Ph.D. in Electrical and Computer Engineering under the supervision of Prof. Qiang Qiu |
| Soyoung Kang | Undergraduate intern at 2020 | Joined Naver CLOVA as a researcher |
| Jungeun Kim | Co-advising at 2020 |  |
| Jing Liu | Advising for her Master at GMU | Researcher at Walmart Lab |
| Nasheen Nur | Co-advising for her Ph.D. at UNCC | Assistant Professor in Florida Institute of Technology |
| Mahmoud Mohammadi | Co-advising for his Ph.D. at UNCC | Software Engineer at Microsoft |
| Kshitij Gorde | Co-advising for his Master in UNCC | Developer in Water Island Capital, LLC in New York |
| Ankesh Anand | Internship during  2017 Summer | Ph.D. Student in Montreal Institute for Learning Algorithms |
| Joel Moniz | Internship during  2017 Summer | Master in Computer Science at Carnegie Mellon University |

## 최근 논문 목록 (2021–2026)

그래프·과학 계산·표 자료·추천·시계열을 비롯한 연구 논문 목록이다. KAIST 부임 전인 2021–2023년 논문과 2024년 초 항목도 포함한다. 연도는 연구실의 논문 목록 표기를 따르며, 개별 연도가 없는 게재 승인 항목 3편은 주변 2022년 항목과 함께 두고 그 사실을 표시했다. 제목·저자·발표처는 연구실 표기다. 연구실 소식에서 채택을 확인한 2026년 NeurIPS·CIKM 항목은 채택으로 표시했다.[^pubs][^home]

최근 범위의 논문은 104편이다. 약물 사이의 상호작용을 예측하는 모형, 심장 전기 신호로 부정맥(심장 박동이 정상적인 리듬을 벗어나는 상태)을 분류하는 모형, 레이더로 움직임을 읽어 스트레스를 탐지하는 방법도 다룬다.[^suppn1][^suppn2][^suppn3]

**2026**

- Jaehyeon Park, Inhyeok Jeong, and Noseong Park. "SBNO : Schrödinger Bridge Neural Operator for the Forward and Inverse Problems under Missing Information". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Sheo yon Jhin, B. Aditya Prakash, and Noseong Park. "TimeOperator: A Function-to-Function Approach to Time Series Modeling". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Jaehyeon Park, Mingu Kang, Dongseok Lee, Woojin Cho, Kookjin Lee, Anthony Gruber, Youngjoon Hong, and Noseong Park. "PDE-PFN: Prior-Data Fitted Neural PDE Solver". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Seojin Kim, and Noseong Park. "Global Importance Estimation for KV Cache Eviction". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Inhyeok Jeong, Jeongwhan Choi, Jaehyeon Park, and Noseong Park. "Learning Hierarchical Forward Processes For Discrete Diffusion Language Models". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Seojin Kim, Yehjin Shin, and Noseong Park. "Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention". *Conference on Neural Information Processing Systems (NeurIPS), 2026 (채택)*.
- Hyunju Kim, Sheo Yon Jhin, Noseong Park, and Nabil Imam. "HyBrain: Spatiotemporal Hyperedges for EEG Seizure Detection and Prediction". *ACM International Conference on Information and Knowledge Management (CIKM), 2026 (채택)*.
- Jihyeon Hur, Yongseok Kwon, Min-Gi Jo, Jeongwhan Choi, and Noseong Park. "How Much Memory Do We Need? Adaptive Memory Gate for Neural Operators". *ICML 2026 Workshop on AI for Physics (AI4Physics), 2026*.
- Byeongwoo An, Kapilan Balagopalan, Sehwa Jeong, Jiun Jeong, Kyoungseok Jang, Hyowon Wi, Noseong Park, Gi-Soo Kim, and Kwang-Sung Jun. "Efficient Algorithms for Contextual Apple Tasting with Log-Loss". *ICML 2026 Workshop on Decision-Making from Offline Datasets to Online Adaptation: Black-Box Optimization to Reinforcement Learning (DEMO), 2026*.
- Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, and Noseong Park. "One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2026*.
- Sumin Park, Seojin Kim, and Noseong Park. "Q-Delta: Beyond Key–Value Associative State Evolution". *International Conference on Machine Learning (ICML), 2026*.
- Sumin Park, and Noseong Park. "STAR: Rethinking MoE Routing as Structure-Aware Subspace Learning". *International Conference on Machine Learning (ICML), 2026*.
- Jayoung Kim, Kookjin Lee, Noseong Park, and Sanghyun Hong. "Adversarial Robustness of Implicit Neural Representation-Based Classifiers". *International Conference on Machine Learning (ICML), 2026*.
- Hyowon Wi, and Noseong Park. "Can Spectral-Clipping Enable Better Learning While Forgetting Less for Low-Rank Adaptation?". *Annual Meeting of the Association for Computational Linguistics (ACL), 2026*.
- Pin-Jui Huang, Yu-Hsuan Liao, Soo Heon Kim, Noseong Park, Jong Bae Park, and Dongmyung Shin. "Efficient Cell Painting Image Representation Learning via Cross-Well Aligned Masked Siamese Network". *Learning Meaningful Representations of Life (LMRL) Workshop at ICLR, 2026*.
- Sheo Yon Jhin, and Noseong Park. "Point-wise Anomaly Detection via Fold-bifurcation ODE". *International Conference on Learning Representations (ICLR), 2026*.
- Yehjin Shin, Seojin Kim, and Noseong Park. "Graph Signal Processing Meets Mamba2: Adaptive Filter Bank via Delta Modulation". *International Conference on Learning Representations (ICLR), 2026*.
- Jeongwhan Choi, Jongwoo Kim, Woosung Kang, and Noseong Park. "Learning Posterior Predictive Distributions for Node Classification from Synthetic Graph Priors". *International Conference on Learning Representations (ICLR), 2026*.
- Jeongwhan Choi, Seungjun Park, Sumin Park, Sung-Bae Cho, and Noseong Park. "Are Graph Transformers Necessary? Efficient Long-Range Message Passing with Fractal Nodes in MPNNs". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.
- Sumin Park, and Noseong Park. "How Many Experts Are Enough? Towards Optimal Semantic Specialization for Mixture-of-Experts". *AAAI Conference on Artificial Intelligence (AAAI), 2026*.

**2025**

- Haksoo Lim, Jaehoon Lee, Sewon Park, Minjung Kim, and Noseong Park. "TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models". *IEEE International Conference on Big Data (IEEE BigData), 2025*.
- Yehjin Shin, Jeongwhan Choi, Seojin Kim, and Noseong Park. "TV-Rec: Time-Variant Convolutional Filter for Sequential Recommendation". *Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Minju Jo, Woojin Cho, Uvini Balasuriya Mudiyanselage, Seungjun Lee, Noseong Park, and Kookjin Lee. "PDEfuncta: Spectrally-Aware Neural Representation for PDE Solution Modeling". *Conference on Neural Information Processing Systems (NeurIPS), 2025*.
- Jihoon Ko, Seojeong Kim, Kyuhan Lee, Shinhwan Kang, Dongyeong Hwang, Kijung Shin, and Noseong Park. "Inductive Influence Estimation and Maximization over Unseen Social Networks under Two Diffusion Models". *Data Mining and Knowledge Discovery, 2025*.
- Kanghyun Choi, Deokki Hong, Hojae Yoon, Joonsang Yu, Noseong Park, Youngsok Kim, and Jinho Lee. "DANCE++: Differentiable Accelerator/Network Co-Exploration with Hard Constraints and Data-Free Training for Real-World Scenarios". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2025*.
- Yehjin Shin, Seojin Kim, and Noseong Park. "Graph Signal Processing Meets Mamba2: Adaptive Filter Bank via Delta Modulation". *Workshop on Efficient Systems for Foundation Models (ES-FoMo) at ICML, 2025*.
- Seojin Kim, Yehjin Shin, and Noseong Park. "Mitigating Over-Smoothing in Mamba2 via Spectral Domain Analysis". *Workshop on Efficient Systems for Foundation Models (ES-FoMo) at ICML, 2025*.
- Yeon Uk Jeong, Jeongwhan Choi, Noseong Park, Jae Yong Ryu, and Yi Rang Kim. "Predicting Drug-Drug Interactions: A Deep Learning Approach with GCN-Based Collaborative Filtering". *Artificial Intelligence in Medicine, 2025*.
- Hyowon Wi, Jeongwhan Choi, and Noseong Park. "Learning Advanced Self-Attention for Linear Transformers in the Singular Value Domain". *International Joint Conference on Artificial Intelligence (IJCAI), 2025*.
- Jinsung Jeon, Jaehyeon Park, Sewon Park, Jeongwhan Choi, Minjung Kim, and Noseong Park. "Possibility for Proactive Anomaly Detection". *I Can't Believe It's Not Better: Challenges in Applied Deep Learning (ICBINB) Workshop at ICLR, 2025*.
- Sumin Park, and Noseong Park. "DARS : Robust Sparse Fine-tuning  with Regularized Subspace Disalignment". *Workshop on Scalable Optimization for Efficient and Adaptive Foundation Models (SCOPE) at ICLR, 2025*.
- Uvini Balasuriya Mudiyanselage, Woojin Cho, Minju Jo, Noseong Park, and Kookjin Lee. "Unveiling the Potential of Superexpressive Networks in Implicit Neural Representations". *Workshop on Neural Network Weights as a New Data Modality (WSL) at ICLR, 2025*.
- Woojin Cho, Kookjin Lee, Noseong Park, Donsub Rim, and Gerrit Welper. "FastLRNR and Sparse Physics Informed Backpropagation". *Results in Applied Mathematics, 2025*.
- Youn-Yeol Yu, Jeongwhan Choi, Jaehyeon Park, Kookjin Lee, and Noseong Park. "PIORF: Physics-Informed Ollivier-Ricci Flow for Long–Range Interactions in Mesh Graph Neural Networks". *International Conference on Learning Representations (ICLR), 2025*.
- Woojin Cho, Minju Jo, Kookjin Lee, and Noseong Park. "Neural Functions for Learning Periodic Signal". *International Conference on Learning Representations (ICLR), 2025*.
- Anthony Gruber, Kookjin Lee, Haksoo Lim, Noseong Park, and Nathaniel Trask. "Efficiently Parameterized Neural Metriplectic Systems". *International Conference on Learning Representations (ICLR), 2025*.
- Seonkyu Lim, Jeongwhan Choi, Hyeyoung Yoon, and Noseong Park. "FraudCenGCL: Enhancing Fraud Detection via Dual-View Graph Contrastive Learning with Account Centrality Features". *Workshop on AI for Social Impact (AISI) at AAAI, 2025*.
- Seonkyu Lim, Jeongwhan Choi, Jaehoon Lee, and Noseong Park. "FrAug: Enhanced Fraud Detection in Interbank Transfers via Augmented Account Features". *Artificial Intelligence for Time Series Analysis (AI4TS) Workshop at AAAI, 2025*.
- Kanghyun Choi, Hyeyoon Lee, Dain Kwon, SunJong Park, Kyuyeun Kim, Noseong Park, Jonghyun Choi, and Jinho Lee. "MimiQ: Low-Bit Data-Free Quantization of Vision Transformers with Encouraging Inter-Head Attention Similarity". *AAAI Conference on Artificial Intelligence (AAAI), 2025*.
- Chaejeong Lee, Jeongwhan Choi, Hyowon Wi, Sung-Bae Cho, and Noseong Park. "SCONE: A Novel Stochastic Sampling to Generate Contrastive Views and Hard Negative Samples for Recommendation". *ACM International WSDM Conference (WSDM), 2025*.

**2024**

- Taeyang Lee, Jeongwhan Choi, Inyeob Na, Insun Yoo, Sungil Woo, Kwang Jong Kim, Mikyung Park, Joonghwan Yang, Jeongguk Min, Seokwoo Lee, Noseong Park, and Joonyoung Yang. "Graph-Based Representation Approach for Deep Learning of Organic Light-Emitting Diode Devices". *Advanced Intelligent Systems, 2024*.
- Mingu Kang, Dongseok Lee, Woojin Cho, Kookjin Lee, Anthony Gruber, Nathaniel Trask, Youngjoon Hong, and Noseong Park. "Can we pre-train ICL-based SFMs for the zero-shot inference of the 1D CDR problem with noisy data?". *NeurIPS Workshop on Foundation Models for Science: Progress, Opportunities, and Challenges (FM4Science), 2024*.
- Jeongwhan Choi, Hyowon Wi, Jayoung Kim, Yehjin Shin, Kookjin Lee, Nathaniel Trask, and Noseong Park. "Graph Convolutions Enrich the Self-Attention in Transformers!". *Conference on Neural Information Processing Systems (NeurIPS), 2024*.
- Seonkyu Lim, Jeongwhan Choi, Noseong Park, Sang-Ha Yoon, Shinhyuck Kang, Young-Min Kim, and Hyunjoong Kang. "Bridging Dynamic Factor Models and Neural Controlled Differential Equations for Nowcasting GDP". *ACM International Conference on Information and Knowledge Management (CIKM), 2024*.
- Fan Wu, Woojin Cho, David Korotky, Sanghyun Hong, Donsub Rim, Noseong Park, and Kookjin Lee. "Identifying Contemporaneous and Lagged Dependence Structures by Promoting Sparsity in Continuous-time Neural Networks". *ACM International Conference on Information and Knowledge Management (CIKM), 2024*.
- Sheo Yon Jhin, Seojin Kim, and Noseong Park. "Addressing Prediction Delays in Time Series Forecasting: A Continuous GRU Approach with Derivative Regularization". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2024*.
- Jayoung Kim, Yehjin Shin, Jeongwhan Choi, Hyowon Wi, and Noseong Park. "Polynomial-based Self-Attention for Table Representation Learning". *International Conference on Machine Learning (ICML), 2024*.
- Jeongwhan Choi, Sumin Park, Hyowon Wi, Sung-Bae Cho, and Noseong Park. "PANDA: Expanded Width-Aware Message Passing Beyond Rewiring". *International Conference on Machine Learning (ICML), 2024*.
- Woojin Cho, Minju Jo, Haksoo Lim, Kookjin Lee, Dongeun Lee, Sanghyun Hong, and Noseong Park. "Parameterized Physics-informed Neural Networks for Parameterized PDEs". *International Conference on Machine Learning (ICML), 2024*.
- Hyeyoon Lee, Kanghyun Choi, Dain Kwon, SunJong Park, Mayoore Selvarasa Jaiswal, Noseong Park, Jonghyun Choi, and Jinho Lee. "DataFreeShield: Defending Adversarial Attacks without Training Data". *International Conference on Machine Learning (ICML), 2024*.
- Seoyoung Hong, Jeongwhan Choi, Yeon-Chang Lee, Srijan Kumar, and Noseong Park. "SVD-AE: Simple Autoencoders for Collaborative Filtering". *International Joint Conference on Artificial Intelligence (IJCAI), 2024*.
- Jinsung Jeon and Noseong Park. "SPI-GAN: Denoising Diffusion GANs with Straight-Path Interpolations". *ICLR Workshop on Practical ML for Limited/Low-resource Settings (PML4LRS), 2024*.
- Woojin Cho, Minju Jo, Haksoo Lim, Kookjin Lee, Dongeun Lee, Sanghyun Hong, and Noseong Park. "Extension of Physics-informed Neural Networks to Solving Parameterized PDEs". *ICLR Workshop on AI4DifferentialEquations in Science (AI4DiffEqtnsInSci), 2024*.
- Jinsung Jeon, Hyundong Jin, Jonghyun Choi, Sanghyun Hong, Dongeun Lee, Kookjin Lee, and Noseong Park. "PAC-FNO: Parallel-Structured All-Component Fourier Neural Operators for Recognizing Low-Quality Images". *International Conference on Learning Representations (ICLR), 2024*.
- Youn-Yeol Yu, Jeongwhan Choi, Woojin Cho, Kookjin Lee, Nayong Kim, Kiseok Chang, Changseung Woo, Ilho Kim, Seokwoo Lee, Joon Young Yang, Sooyoung Yoon, and Noseong Park. "Learning Flexible Body Collision Dynamics with Hierarchical Contact Mesh Transformer". *International Conference on Learning Representations (ICLR), 2024*.
- Yehjin Shin, Jeongwhan Choi, Hyowon Wi, and Noseong Park. "An Attentive Inductive Bias for Sequential Recommendation beyond the Self-Attention". *AAAI Conference on Artificial Intelligence (AAAI), 2024*.
- Woojin Cho, Seunghyeon Cho, Hyundong Jin, Jinsung Jeon, Kookjin Lee, Sanghyun Hong, Dongeun Lee, Jonghyun Choi, and Noseong Park. "Operator-learning-inspired Modeling of Neural Ordinary Differential Equations". *AAAI Conference on Artificial Intelligence (AAAI), 2024*.
- Hyowon Wi, Yehjin Shin, and Noseong Park. "Continuous-time Autoencoders for Regular and Irregular Time Series Imputation". *ACM International Web Search and Data Mining Conference (WSDM), 2024*.

**2023**

- Seonkyu Lim, Jaehyeon Park, Seojin Kim, Hyowon Wi, Haksoo Lim, Jinsung Jeon, Jeongwhan Choi, and Noseong Park. "Long-term Time Series Forecasting based on Decomposition and Neural Ordinary Differential Equations". *IEEE International Conference on Big Data (IEEE BigData), 2023*.
- Woojin Cho, Kookjin Lee, Donsub Rim, and Noseong Park. "Hypernetwork-based Meta-Learning for Low-Rank Physics-Informed Neural Networks". *Conference on Neural Information Processing Systems (NeurIPS), 2023*.
- Jaehoon Lee, Chan Kim, Gyumin Lee, Haksoo Lim, Jeongwhan Choi, Kookjin Lee, Dongeun Lee, Sanghyun Hong, and Noseong Park. "HyperNetwork Approximating Future Parameters for Time Series Forecasting under Temporal Drifts". *NeurIPS Workshop on Distribution Shifts (DistShift), 2023*.
- Haksoo Lim, Sewon Park, Minjung Kim, Jaehoon Lee, Seonkyu Lim, and Noseong Park. "MadSGM: Multivariate Anomaly Detection with Score-based Generative Models". *ACM International Conference on Information and Knowledge Management (CIKM), 2023*.
- Sheo Yon Jhin, Jaehoon Lee, and Noseong Park. "Precursor-of-Anomaly Detection for Irregular Time Series". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2023*.
- JaeYeon Park, Kichang Lee, Noseong Park, Seng Chan You, and JeongGil Ko. "Self-Attention LSTM-FCN Model for Arrhythmia Classification and Uncertainty Assessment". *to appear in Artificial Intelligence In Medicine, 2023 (게재 승인)*.
- Jeongwhan Choi, Seoyoung Hong, Noseong Park, and Sung-Bae Cho. "GREAD: Graph Neural Reaction-Diffusion Networks". *International Conference on Machine Learning (ICML), 2023*.
- Chaejeong Lee, Jayoung Kim, and Noseong Park. "CoDi: Co-evolving Contrastive Diffusion Models for Mixed-type Tabular Synthesis". *International Conference on Machine Learning (ICML), 2023*.
- Minju Jo, Seungji Kook, and Noseong Park. "Hawkes Process based on Controlled Differential Equations". *International Joint Conference on Artificial Intelligence (IJCAI), 2023*.
- Jeongwhan Choi, Seoyoung Hong, Noseong Park, and Sung-Bae Cho. "Blurring-Sharpening Process Models for Collaborative Filtering". *International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR), 2023*.
- Jeongwhan Choi, and Noseong Park. "Graph Neural Rough Differential Equations for Traffic Forecasting". *ACM Transactions on Intelligent Systems and Technology, Vol. 14, No. 4, 2023*.
- Jaewon Jung, Jaeyong Song, Hongsun Jang, Hyeyoon Lee, Kanghyun Choi, Noseong Park, and Jinho Lee. "Fast Adversarial Training with Dynamic Batch-level Attack Control". *Design Automation Conference (DAC), 2023*.
- Jayoung Kim, Chaejeong Lee, and Noseong Park. "STaSy: Score-based Tabular Data Synthesis". *International Conference on Learning Representations (ICLR), 2023*.
- Sheo Yon Jhin, Minju Jo, Seungji Kook, and Noseong Park. "Learnable Path in Neural Controlled Differential Equations". *AAAI Conference on Artificial Intelligence (AAAI), 2023*.

**2022**

- Seoyoung Hong, Minju Jo, Seungji Kook, Jaeeun Jung, Hyowon Wi, and Noseong Park. "TimeKit: A Time-series Forecasting-based Upgrade Kit for Collaborative Filtering". *IEEE International Conference on Big Data (IEEE BigData), 2022 [Best Student Paper Award]*.
- Jinsung Jeon, Jeonghak Kim, Haryong Song, Seunghyeon Cho, and Noseong Park. "GT-GAN: General Purpose Time Series Synthesis with Generative Adversarial Networks". *Conference on Neural Information Processing Systems (NeurIPS), 2022*.
- Hwangyong Choi, Jeehyun Hwang, Jeongwhan Choi, Kookjin Lee, Dongeun Lee, and Noseong Park. "Climate Modeling with Neural Diffusion Equations". *to appear in Knowledge and Information Systems (게재 승인, 개별 연도 표기 없음)*.
- Sheo Yon Jhin, Heejoo Shin, Sujie Kim, Seoyoung Hong, Solhee Park, Noseong Park, Seungbeom Lee, Hwiyoung Maeng, and Seungmin Jeon. "Attentive Neural Controlled Differential Equations for Time-series Classification and Forecasting". *to appear in Knowledge and Information Systems (게재 승인, 개별 연도 표기 없음)*.
- Taeri Kim, Noseong Park, Jiwon Hong, and Sang-Wook Kim. "Phishing URL Detection: A Network-based Approach Robust to Evasion". *ACM Conference on Computer and Communications Security (CCS), 2022*.
- Seoyoung Hong, Heejoo Shin, Jeongwhan Choi, and Noseong Park. "Prediction-based One-shot Dynamic Parking Pricing". *ACM International Conference on Information and Knowledge Management (CIKM), 2022, Full Research Paper*.
- Jihyeon Hyeong, Jayoung Kim, Noseong Park, and Sushil Jajodia. "An Empirical Study on the Membership Inference Attack against Tabular Data Synthesis Models". *ACM International Conference on Information and Knowledge Management (CIKM), 2022, Short Research Paper*.
- Manh Tuan Do, Noseong Park, and Kijung Shin. "Two-Stage Training of Graph Neural Networks for Graph Classification". *to appear in Neural Processing Letters (게재 승인, 개별 연도 표기 없음)*.
- Seunghyeon Cho, Sanghyun Hong, Kookjin Lee, and Noseong Park. "AdamNODEs: When Neural ODE Meets Adaptive Moment Estimation". *ICML Workshop on Continuous Time Methods for Machine Learning, 2022*.
- Jayoung Kim, ChaeJeong Lee, Yehjin Shin, Sewon Park, Minjung Kim, Noseong Park, and Jihoon Cho. "SOS: Score-based Oversampling Minor Classes for Tabular Data". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2022*.
- Kanghyun Choi, Hye Yoon Lee, Deokki Hong, Joonsang Yu, Noseong Park, Youngsok Kim, and Jinho Lee. "It's All In the Teacher: Zero-Shot Quantization Brought Closer to the Teacher". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022*.
- Thai Le, Noseong Park, and Dongwon Lee. "SHIELD: Defending Textual Neural Networks against Black-Box Adversarial Attacks with Stochastic Multi-Expert Patcher". *Annual Meeting of the Association for Computational Linguistics (ACL), 2022*.
- Deokki Hong, Kanghyun Choi, Hey Yoon Lee, Joonsang Yu, Youngsok Kim, Noseong Park, and Jinho Lee. "Enabling Hard Constraints in Differentiable Neural Network and Accelerator Co-Exploration". *Design Automation Conference (DAC), 2022*.
- Jaehoon Lee, Jinsung Jeon, Sheo yon Jhin, Jihyeon Hyeong, Jayoung Kim, Minju Jo, Seungji Kook, and Noseong Park. "LORD: Lower-Dimensional Embedding of Log-Signature in Neural Rough Differential Equations". *International Conference on Learning Representations (ICLR), 2022*.
- Sheo Yon Jhin, Jaehoon Lee, Minju Jo, Seungji Kook, Jinsung Jeon, Jihyeon Hyeong, Jayoung Kim and Noseong Park. "EXIT: Extrapolation and Interpolation-based Neural Controlled Differential Equations for Time-series Classification and Forecasting". *The Web Conference (WWW), 2022*.
- Jeongwhan Choi, Hwangyong Choi, Jeehyun Hwang, Noseong Park. "Graph Neural Controlled Differential Equations for Traffic Forecasting". *AAAI Conference on Artificial Intelligence (AAAI), 2022*.
- Taeyong Kong, Taeri Kim, Jinsung Jeon, Jeongwhan Choi, Yeon-Chang Lee, Noseong Park, and Sang-Wook Kim. "Linear, or Non-Linear, That is the Question!". *ACM International WSDM Conference (WSDM), 2022*.

**2021**

- Jaehoon Lee, Jihyeon Hyung, Jinsung Jeon, Noseong Park, and Jihoon Cho. "Invertible Tabular GANs: Killing Two Birds with One Stone for Tabular Data Synthesis". *Conference on Neural Information Processing Systems (NeurIPS), 2021*.
- Kanghyun Choi, Deokki Hong, Noseong Park, Youngsok Kim, and Jinho Lee. "Qimera: Data-free Quantization with Synthetic Boundary Supporting Samples". *Conference on Neural Information Processing Systems (NeurIPS), 2021*.
- Jeehyun Hwang, Jeongwhan Choi, Hwangyong Choi, and Noseong Park. "Climate Modeling with Neural Diffusion Equations". *IEEE International Conference on Data Mining (ICDM), 2021*.
- Sheo Yon Jhin, Heejoo Shin, Seoyoung Hong, Solhee Park, and Noseong Park. "Attentive Neural Controlled Differential Equations for Time-series Classification and Forecasting". *IEEE International Conference on Data Mining (ICDM), 2021*.
- Jinsung Jeon, Soyoung Kang, Minju Jo, Seunghyeon Cho, Noseong Park, Seonghoon Kim, and Chiyoung Song. "LightMove: A Lightweight Next-POI Recommendation for Taxicab Rooftop Advertising". *ACM International Conference on Information and Knowledge Management (CIKM), 2021*.
- Jeongwhan Choi, Jinsung Jeon, and Noseong Park. "LT-OCF: Learnable-Time ODE-based Collaborative Filtering". *ACM International Conference on Information and Knowledge Management (CIKM), 2021*.
- Sheo Yon Jhin, Minju Jo, Taeyong Kong, Jinsung Jeon, and Noseong Park. "ACE-NODE: Attentive Co-Evolving Neural Ordinary Differential Equations". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2021*.
- Duanshun Li, Jing Liu, Jinsung Jeon, Seoyoung Hong, Thai Le, Dongwon Lee, and Noseong Park. "Large-Scale Data-Driven Airline Market Influence Maximization". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2021*.
- Duanshun Li, Jing Liu, Dongeun Lee, Ali Seyedmazloom, Giridhar Kaushik, Kookjin Lee, and Noseong Park. "A Novel Method to Solve Neural Knapsack Problems". *International Conference on Machine Learning (ICML), 2021*.
- Thai Le, Noseong Park, and Dongwon Lee. "A Sweet Rabbit Hole by DARCY: Using Honeypots to Detect Universal Trigger's Adversarial Attacks". *Annual Meeting of the Association for Computational Linguistics (ACL), 2021*.
- Jayoung Kim, Jinsung Jeon, Jaehoon Lee, Jihyeon Hyung, and Noseong Park. "OCT-GAN: Neural ODE-based Conditional Tabular GANs". *The Web Conference (WWW), 2021*.
- Jinsung Jeon, Jing Liu, Jayoung Kim, Jaehoon Lee, Jamie Jooyeon Lee, Ozlem Uzuner, Sushil Jajodia, and Noseong Park. "Scalable Graph Synthesis with Adj and 1 – Adj". *SIAM International Conference on Data Mining (SDM), 2021*.
- Jinsung Jeon,Dongeun Lee, Seunghyun Hwang,Soyoung Kang, Duanshun Li, Kookjin Lee, Jing Liu, and Noseong Park. "Large-Scale Flight Frequency Optimization with Global Convergence in the US Domestic Air Passenger Markets". *SIAM International Conference on Data Mining (SDM), 2021*.
- Jungeun Kim, Kookjin Lee, Dongeun Lee, Sheo Yon Jhin, and Noseong Park. "DPM: A Novel Training Method for Physics-Informed Neural Networks in Extrapolation". *AAAI Conference on Artificial Intelligence (AAAI), 2021*.
- Jonghoon Shin, Junhyung Moon, Beomsik Kim, Jihwan Eom, Noseong Park, and Kyoungwoo Lee. "Attention-based Stress Detection exploiting Non-contact Monitoring of Movement Patterns with IR-UWB radar". *ACM/SIGAPP Symposium On Applied Computing (SAC), Poster, 2021*.

## 과제

아래는 수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제와, 같은 기간에 선정·지원 소식을 알린 과제다. 연세대학교 재직 시기에 시작한 과제도 포함한다. 날짜가 붙은 항목은 선정·지원 소식의 게시일이고, 수행 기간은 별도로 적힌 경우만 표시했다.[^home]

- Tabular data synthesis using GANs (지원 Samsung; 기간 2021.04 ~ 2022.03; 연구비 1억 1천만 원)
- Anomaly detection in time-series data (지원 IITP; 기간 2021.04 ~ 2023.12; 연구비 연 1억 원)
- Synopsis table synthesis using GANs, VAEs, invertible neural networks, and other generative models (지원 IITP; 기간 2021.04 ~ 2024.12; 연구비 연 1억 2천만 원)
- 2025-12-23 · Network Intelligent Analysis via LLM Agents (지원 Microsoft Research Asia; 상태 지원 예정)
- 2025-03-10 · LLM-driven Chain-of-Thought Analysis for Tabular Data (지원 Microsoft Research Asia; 상태 지원 예정)
- 2025-08-04 · 생성AI선도인재양성사업 (협력 기관 LG AI 연구원; 상태 선정)
- 2025-08-04 · 독자AI파운데이션모델사업(가칭 국가대표 LLM 사업) (협력 기관 NC AI; 상태 선정)
- 2024-10-11 · Scientific Foundation Model 연구 제안 (지원 삼성미래기술육성센터; 상태 연구 제안 선정)

## 수상

KAIST 부임 전인 2024년 1월 연구실 소식에 게시된 수상이다.[^home]

- 2024-01-11 · 임선규 학생, 금융위원회 주관 D-테스트베드 사업의 딥러닝·머신러닝 활용 금융사기탐지 모델 최적화 연구로 최우수상(핀테크지원센터 이사장상) 수상.

## 소식

2023년 10월 20일–2026년 9월 25일에 날짜를 붙여 게시한 연구·학술 활동 소식이다. KAIST 부임 전의 2023년 소식과 2024년 1월 소식도 포함한다. 예정으로 알린 강연과 직책은 예정으로 적었다.[^home]

- 2026-09-25 · NeurIPS 2026 논문 6편 채택.
- 2026-08-11 · CIKM 2026 논문 1편 채택.
- 2026-06-23 · One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets의 KDD 2026 구두 발표 선정.
- 2026-06-19 · 박노성 교수의 TMLR 편집위원 활동 예정과 NeurIPS·ICML·ICLR 영역위원장 활동.
- 2026-06-05 · 박노성 교수의 Special Semester on AI in Scientific Computing에서 과학 계산의 학습 기반 방법 강연 예정.
- 2026-05-26 · ICML 2026 워크숍 논문 2편 채택. 해당 연도 본 학회 논문 3편과 워크숍 논문 2편.
- 2026-05-16 · KDD 2026 논문 1편 채택.
- 2026-05-01 · ICML 2026 논문 3편 채택.
- 2026-04-06 · ACL 2026 본 학회 논문 1편 채택.
- 2026-03-02 · ICLR 2026 LMRL 워크숍 논문 1편 채택.
- 2026-03-01 · Jeongwhan Choi의 Learning on Graphs Conference 2026 대회장 활동 예정.
- 2026-02-20 · Sheoyon Jhin의 Emory University 초청 강연 On the Dynamical Nature of Time-Series: A Continuous-Time Perspective 예정.
- 2026-01-26 · ICLR 2026 논문 3편 채택.
- 2025-12-08 · 박노성 교수의 KAIST AI수학대학원 참여.
- 2025-11-08 · AAAI 2026 논문 2편 채택. 구두 발표 1편과 포스터 1편.
- 2025-10-23 · IEEE BigData 2025 논문 1편 채택.
- 2025-09-19 · NeurIPS 2025 논문 2편 채택.
- 2025-07-12 · Data Mining and Knowledge Discovery 논문 1편 게재 승인.
- 2025-06-13 · IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 논문 1편 게재 승인.
- 2025-06-12 · ICML 2025 ES-FoMo 워크숍 논문 2편 채택.
- 2025-05-29 · Artificial Intelligence in Medicine 논문 1편 게재 승인.
- 2025-04-29 · IJCAI 2025 논문 1편 채택.
- 2025-03-06 · ICLR 2025 워크숍 논문 3편 채택. 해당 연도 본 학회 논문 3편과 워크숍 논문 3편.
- 2025-02-05 · Results in Applied Mathematics 논문 1편 게재 승인.
- 2025-01-23 · ICLR 2025 논문 3편 채택.
- 2024-12-19 · AAAI 2025 워크숍 논문 2편 채택. 해당 연도 본 학회 논문 1편과 워크숍 논문 2편.
- 2024-12-10 · AAAI 2025 본 학회 논문 1편 채택.
- 2024-10-29 · Advanced Intelligent Systems 논문 1편 출판.
- 2024-10-24 · WSDM 2025 논문 1편 채택.
- 2024-10-11 · NeurIPS 2024 FM4Science 워크숍 논문 1편 채택.
- 2024-09-26 · NeurIPS 2024 논문 1편 채택.
- 2024-07-16 · CIKM 2024 논문 2편 채택.
- 2024-06-29 · 박노성 교수의 한국 개최 CIKM 2025 대회장 활동 예정.
- 2024-06-07 · Parameterized Physics-informed Neural Networks for Parameterized PDEs의 ICML 2024 구두 발표 선정.
- 2024-05-17 · KDD 2024 논문 1편 채택.
- 2024-05-07 · 박노성 교수의 제18회 WSDM 튜토리얼 세션 위원장 활동 예정.
- 2024-05-02 · ICML 2024 논문 4편 채택.
- 2024-04-17 · SVD-AE: Simple Autoencoders for Collaborative Filtering의 IJCAI 2024 채택.
- 2024-03-04 · Extension of Physics-informed Neural Networks to Solving Parameterized PDEs와 SPI-GAN: Denoising Diffusion GANs with Straight-Path Interpolations의 ICLR 2024 워크숍 채택.
- 2024-02-01 · BigDyL in WISE의 KAIST 전산학부 이전과 박노성 교수의 정년보장 부교수 부임.
- 2024-01-16 · PAC-FNO: Parallel-Structured All-Component Fourier Neural Operators for Recognizing Low-Quality Images와 Learning Flexible Body Collision Dynamics with Hierarchical Contact Mesh Transformer의 ICLR 2024 채택.
- 2023-12-09 · Operator-learning-inspired Modeling of Neural Ordinary Differential Equations와 An Attentive Inductive Bias for Sequential Recommendation beyond the Self-Attention의 AAAI 2024 채택.
- 2023-10-29 · Long-term Time Series Forecasting based on Decomposition and Neural Ordinary Differential Equations의 IEEE BigData 2023 채택.
- 2023-10-28 · HyperNetwork Approximating Future Parameters for Time Series Forecasting under Temporal Drifts의 NeurIPS 2023 DistShift 워크숍 채택.
- 2023-10-20 · Continuous-time Autoencoders for Regular and Irregular Time Series Imputation의 WSDM 2024 구두 발표 채택.

## 연락과 위치

- 교수 이메일: noseong@kaist.ac.kr[^prof]
- 교수연구실: E3-5, 604호. 전산학부 교수진 명단 표기다.[^faculty]
- 연구실 소개 페이지의 사무실: E3-1, 3425호.[^lab]
- 전화: 042-350-3514[^lab]
- 학과 주소: 대전광역시 유성구 대학로 291 KAIST 전산학부[^lab]

## 각주
[^home]: BigDyL in WISE, 연구 소개와 News. <https://sites.google.com/view/npark> 관측일 2026-10-27.
[^lab]: KAIST 전산학부, 빅데이터 분석 및 학습 연구실 소개. <https://cs.kaist.ac.kr/research/labView?sn=118&menu=64> 관측일 2026-10-27.
[^faculty]: KAIST 전산학부 교수진 명단, 박노성: 부교수·교수연구실 604, E3-5·Machine Learning. <https://cs.kaist.ac.kr/people/faculty> 관측일 2026-10-27.
[^prof]: Noseong Park, 개인 소개·학력·재직 이력·겸무·학술 활동·이메일. <https://sites.google.com/view/noseong> 관측일 2026-10-28.
[^members]: BigDyL in WISE, Members. <https://sites.google.com/view/npark/members> 관측일 2026-10-28.
[^pubs]: BigDyL in WISE, Publications. <https://sites.google.com/view/npark/publications> 관측일 2026-10-28.
[^p1]: W. Cho 외, N. Park, Proceedings of the 41st International Conference on Machine Learning 235, 8510-8533 (2024). <https://proceedings.mlr.press/v235/cho24b.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/cho24b.html> 관측일 2026-10-28.
[^p2]: W. Cho, M. Jo, K. Lee, N. Park, arXiv 사전 공개본 (온라인 2025-06-11). <https://arxiv.org/abs/2506.09526> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.09526> 관측일 2026-10-28.
[^p3]: J. Choi 외, N. Park, NeurIPS 2024 채택, arXiv 판 (2024). <https://arxiv.org/abs/2312.04234> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2312.04234> 관측일 2026-10-28.
[^p4]: Y. Shin, S. Kim, N. Park, ICLR 2026, arXiv 판 (2026). <https://arxiv.org/abs/2603.22333> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.22333> 관측일 2026-10-28.
[^p5]: J. Kim 외, N. Park, Proceedings of the 41st International Conference on Machine Learning 235, 24509-24526 (2024). <https://proceedings.mlr.press/v235/kim24ae.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/kim24ae.html> 관측일 2026-10-28.
[^p6]: Y. Shin, J. Choi, S. Kim, N. Park, NeurIPS 2025, arXiv 판 (2025). <https://arxiv.org/abs/2510.25259> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2510.25259> 관측일 2026-10-28.
[^p7]: S. Y. Jhin, S. Kim, N. Park, KDD 2024 채택, arXiv 판 (2024). <https://doi.org/10.1145/3637528.3671969> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2407.01622> 관측일 2026-10-28.
[^p8]: H. Lim 외, N. Park, arXiv 사전 공개본 (온라인 2025-11-26). <https://arxiv.org/abs/2511.21335> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2511.21335> 관측일 2026-10-28.
[^suppn1]: Yeon Uk Jeong, Jeongwhan Choi, Noseong Park, Jae Yong Ryu, Yi Rang Kim, Artificial Intelligence in Medicine (2025). <https://doi.org/10.1016/j.artmed.2025.103185> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.artmed.2023.102570%7C10.1016/j.artmed.2025.103185%7C10.1145/3412841.3442089%7C10.1186/s12859-022-04633-x> 관측일 2026-10-28.
[^suppn2]: JaeYeon Park, Kichang Lee, Noseong Park, Seng Chan You, JeongGil Ko, Artificial Intelligence in Medicine (2023). <https://doi.org/10.1016/j.artmed.2023.102570> 초록 기준(Europe PMC 초록). 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.artmed.2023.102570%22> 관측일 2026-10-28.
[^suppn3]: Jonghoon Shin, Junhyung Moon, Beomsik Kim, Jihwan Eom, Noseong Park, Kyoungwoo Lee, Proceedings of the 36th Annual ACM Symposium on Applied Computing (2021). <https://doi.org/10.1145/3412841.3442089> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1016/j.artmed.2023.102570%7C10.1016/j.artmed.2025.103185%7C10.1145/3412841.3442089%7C10.1186/s12859-022-04633-x> 관측일 2026-10-28.

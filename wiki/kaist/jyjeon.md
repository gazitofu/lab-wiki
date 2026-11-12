# Predictive Analytics Lab

**KAIST AI미래학과 · 전주영 부교수**

- 영문 이름: Jooyoung Jeon
- 분야: 확률적 미래 예측, 통계·인공지능 방법을 통한 위험 추정, 에너지·환경·금융 자료의 예측 모형[^home][^faculty]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 시계열 분석·예측[^home], 통계적 추론·검정[^home][^faculty]
- 홈페이지: <https://sites.google.com/view/jyjeon/about-me>
- 근거와 출처: [Predictive Analytics Lab 근거 페이지](jyjeon-sources.md)

> 미래의 수요·발전량·환경 변화를 예측하고, 예측이 얼마나 불확실한지도 수량으로 나타내는 방법을 연구한다. 에너지와 금융시장에 이를 적용하며, 글과 의료 영상을 분석하는 공저 연구도 있다.[^home][^p1][^p2][^p3][^p4]

## 무엇을 연구하나

전주영 교수가 이끄는 연구실은 새 예측 모형을 개발하고 불확실성(가능한 결과가 하나로 정해져 있지 않은 정도)을 수량으로 나타내는 데 관심을 둔다. 확률 예측은 미래 값을 하나로만 제시하지 않고 가능한 값들의 발생 가능성이나 값이 놓일 구간을 함께 제시하는 방법이다. 연구실은 풍력·파력·태양광 발전과 스마트 계량기가 기록한 전력 사용 자료, 대기오염·기온·일사량, 금융시장의 위험을 주요 적용 대상으로 든다.[^home] 학과 소개도 확률적 미래 예측, 통계 및 인공지능 방법론을 통한 위험 추정과 자료에 근거한 의사결정을 연구 분야로 적는다.[^faculty]

전력 수요 연구에서는 적은 수의 가구를 묶었을 때의 수요를 예측하고, 어떤 가구들을 함께 묶어야 예측 오차가 줄어드는지를 다룬다. 대표 논문 1은 주어진 에너지 수요에 맞춰 가구 수요를 묶는 세 방법을 제안한다. 세 방법 모두 무작위로 가구를 묶은 경우보다 예측 정확도를 높였고, 한국과 아일랜드 자료에서는 세 방법 가운데 Seasonal Residual 접근법이 나머지 두 방법보다 정확도와 계산 효율에서 나았다.[^p1] 예측 방법 전반을 정리한 대표 논문 5는 예측의 준비·생성·조직·평가에 쓰이는 이론과 방법, 실제 적용 사례를 함께 다룬다.[^p5]

환경 변화가 금융시장에 미치는 영향도 살핀다. 대표 논문 2는 미국 에너지 기업들이 위치한 지역의 가뭄 위험 추세에 따라 집단을 나누고 주식 수익률을 비교했다. 가뭄 위험이 커지는 지역의 기업은 위험이 줄어드는 지역의 기업보다 수익률이 낮았으며, 특히 2010년 이후에 이런 차이가 나타났다. 연료 생산과 전력 공급으로 나눈 두 부문에서도 2010년 이후 가뭄 위험이 주가에 부정적인 영향을 미쳤다고 보고한다.[^p2]

공저 연구에는 글의 구조를 정량적으로 설명하는 모형도 있다. 대표 논문 3은 단어의 출현 빈도와 단어 사이 상호작용을 함께 나타내는 성장 모형으로 한국어 글을 분석했다. 글의 종류가 달라도 단어 빈도 분포의 척도 지수(scaling exponent)는 비슷했지만, 전문 보고서에서는 비교 대상인 소설보다 상호작용 효과가 컸다. 연구진은 이 결과를 글의 결속과 장르를 추론하는 방법의 가능성으로 제시한다.[^p3]

의료 영상 공저 연구에서는 종류가 다른 눈 영상을 결합하는 새 분류 틀을 개발했다. 대표 논문 4는 세균성·진균성 각막염(눈의 투명한 앞부분인 각막에 세균·곰팡이가 일으키는 염증)을 구분하도록 영상 처리 모형을 결합하는 세 틀을 제안하고 성능을 비교했다. 서로 다른 영상의 정보를 함께 처리하는 방식으로 분류 성능을 높였다고 보고한다.[^p4]

## 주요 연구 주제

### 1. 확률 예측과 에너지 수요의 묶음 구성

여러 가구의 수요를 어떤 조합으로 묶을지와 그 수요의 불확실성을 함께 다룬다. 연구실은 부분 집단과 전체처럼 포함 관계가 있는 대상들의 예측을 다루는 계층 예측에도 관심을 두며, 전력·환경 자료에 맞는 새 예측 모형을 개발한다.[^home][^p1]

### 2. 환경 위험과 금융시장

가뭄 위험과 에너지 기업 주식 수익률의 관계를 분석하는 공저 연구로, 에너지 산업이 물의 이용 가능성에 의존한다는 점을 다룬다.[^home][^p2]

### 3. 글의 정량 모형

단어 빈도의 분포(각 값이 얼마나 자주 나타나는지를 나타낸 관계)와 단어 사이 상호작용을 모형으로 표현한다. 한국어 글에서 장르에 따른 차이를 단어 빈도 분포의 모양과 글의 결속으로 살핀다.[^p3]

### 4. 서로 다른 의료 영상의 결합

눈의 앞부분을 서로 다른 방식으로 찍은 영상들을 함께 처리해 세균성 각막염과 진균성 각막염을 구별하는 분류 틀을 개발한다. 단일 영상 종류를 쓰는 방식과 여러 종류를 결합하는 방식을 비교한다.[^p4]

## 대표 논문

KAIST 재직 시기의 논문 중 에너지 예측, 환경과 금융, 글의 정량 모형, 의료 영상 분류, 예측 방법 종합을 보여 주는 5편이다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자와 교수 역할 |
|---|---|---|---|---|
| 1 | 2024 | [Probabilistic forecast-based portfolio optimization of electricity demand at low aggregation levels](https://doi.org/10.1016/j.apenergy.2023.122109) · Applied Energy | 적은 수의 가구를 묶어 전력 수요를 예측할 때, 어떤 가구를 함께 묶을지도 정하는 방법이다. 주어진 수요에 맞춰 가구 수요를 구성하는 세 접근법을 제안했고, 모두 무작위 구성보다 예측 정확도를 높였다. 한국과 아일랜드 자료에서는 세 접근법 가운데 Seasonal Residual 접근법이 다른 두 방법보다 정확도와 계산 효율에서 나았다.[^p1] | 1저자 Jungyeon Park, 전주영은 전체 7명 중 3번째 저자 |
| 2 | 2024 | [Drought and energy stock markets in the United States](https://doi.org/10.1088/1748-9326/ad61ff) · Environmental Research Letters | 미국 에너지 기업을 지역의 가뭄 위험 추세에 따라 나누어 주식 수익률을 비교했다. 위험이 커지는 지역의 기업은 위험이 줄어드는 지역보다 수익률이 낮았고, 특히 2010년 이후 차이가 나타났다. 연료 생산과 전력 공급 두 부문 모두 2010년 이후 가뭄 위험이 주가에 부정적인 영향을 미쳤다고 보고한다.[^p2] | 1저자 Seongeun Kim, 전주영은 전체 3명 중 2번째 저자 |
| 3 | 2023 | [Scaling behavior and text cohesion in Korean texts](https://doi.org/10.1371/journal.pone.0290168) · PLoS ONE | 단어 사이 상호작용을 포함한 성장 모형으로 한국어 글의 단어 빈도와 결속을 설명했다. 한국어 글은 장르와 관계없이 단어 빈도 분포의 척도 지수(scaling exponent)가 비슷했지만, 전문 보고서에서는 비교 대상 소설보다 상호작용 효과가 컸다. 글의 결속으로 장르를 추론할 가능성을 제시한다.[^p3] | 1저자 Hokyun Kim, 전주영은 전체 9명 중 7번째 저자 |
| 4 | 2025 | [Deep learning by Vision Transformer to classify bacterial and fungal keratitis using different types of anterior segment images](https://doi.org/10.1016/j.compbiomed.2025.109976) · Computers in Biology and Medicine | 세균성·진균성 각막염을 구분하기 위해 서로 다른 종류의 눈 앞부분 영상을 결합하는 세 분류 틀을 개발했다. 영상의 여러 부분 사이 관계를 처리하는 비전 트랜스포머(Vision Transformer) 모형에 벡터(여러 값을 순서대로 묶은 것)를 추가하거나, 입력 요소 사이 관계를 계산해 정보를 합치는 자기 주의 방식으로 모형들을 결합했다. 서로 다른 영상 종류를 함께 처리하는 방식이 진단 분류 성능을 높였다고 보고한다.[^p4] | 1저자 Yeo Kyoung Won, 전주영은 전체 5명 중 3번째 저자 |
| 5 | 2022 | [Forecasting: theory and practice](https://doi.org/10.1016/j.ijforecast.2021.11.001) · International Journal of Forecasting | 예측의 이론과 실무를 폭넓게 정리한 비체계적 문헌 검토다. 예측을 준비하고 만들고 조직하고 평가하는 여러 모형·원칙·방법을 소개하고, 실제 상황에 적용되는 사례를 보여 준다. 무료·공개 소프트웨어와 공개 자료 목록도 함께 제공한다.[^p5] | 1저자 Fotios Petropoulos, 전주영은 중간 저자 |

## 교수와 전문 분야

전주영(Jooyoung Jeon)은 2019년부터 KAIST에서 부교수로 재직하고 있다. 현재 누리집의 소속 표기는 Department of AI and Futures Studies이며, 학과 교수진 목록의 국문 이름은 AI미래학과다.[^home][^faculty] 전문 분야는 새 예측 모형 개발과 관련 불확실성의 정량화이고, 에너지·환경·금융시장 위험을 주요 적용 대상으로 삼는다.[^home]

서울대학교에서 컴퓨터과학·통계학 학사 학위를, 런던비즈니스스쿨에서 금융학 석사 학위를 받았다. 옥스퍼드대학교 Saïd Business School에서는 경영과학을 세부 전공으로 경영학 박사 학위를 받았다. KAIST 부임 전에는 옥스퍼드대학교 연구 펠로, 스트래스클라이드대학교 조교수, 바스대학교 조교수로 재직했고, 2016–2018년 서울대학교 공학전문대학원 방문 부교수 경력도 있다.[^home]

강의는 Quantitative Research Methodology(GFS701), Time Series & AI Forecasting(FS693)을 안내한다.[^home]

## 응용 분야

풍력·파력·태양광 발전과 스마트 계량기가 기록한 전력 사용 자료의 예측, 대기오염·기온·일사량 예측, 금융시장 위험 모형화가 누리집이 밝힌 적용 분야다.[^home] 공저 논문에서는 가구 수요를 묶는 구성 방법, 가뭄과 에너지 기업의 주식 수익률, 한국어 글의 구조, 서로 다른 눈 영상의 분류를 다룬다.[^p1][^p2][^p3][^p4]

## 구성원

2026년 11월 12일 누리집의 Students 절은 박사과정 재학 9명과 석사과정 재학 16명을 안내한다.[^home]

## 졸업생

누리집의 Students 절은 박사 졸업 4명과 석사 졸업 22명을 안내한다.[^home]

## 최근 논문 목록 (2021–2026)

교수 누리집 Publications 절의 2022–2025년 논문 6편이다. 연도·저자·제목·발표처는 누리집 표기이며, 「in press」는 누리집의 게재 예정 표기다.[^home]

**2025**

- YK Won, CH Kim, J Jeon, J Cha, DH Lim. "Deep learning by Vision Transformer to classify bacterial and fungal keratitis using different types of anterior segment images". *Computers in Biology and Medicine, 190, 109976. DOI: 10.1016/j.compbiomed.2025.109976*.

**2024**

- S Kim, J Jeon, H Kim. "Drought and energy stock markets in the United States". *Environmental Research Letters, 19 (9), 094012. DOI: 10.1088/1748-9326/ad61ff*.
- J Park, E Alvatenga, J Jeon, R Li, F Petropoulos, H Kim and K Ahn. "Probabilistic Forecast-based Portfolio Optimization of Electricity Demand at Low Aggregation Levels". *Applied Energy, 353, 122109. DOI: 10.1016/j.apenergy.2023.122109*.

**2023**

- H Kim, S Park, M Jeong, H Byun, J Kim, Dy Lee, J Jeon, E Yi, K Ahn. "Scaling behavior and text cohesion in Korean texts". *Plos One, 18(8). DOI: 10.1371/journal.pone.0290168*.
- H Kim, E Yi, J Jeon, T Park, K Ahn. "After the Split: Market Efficiency of Bitcoin Cash". *Computational Economics, 1-17. DOI: 10.1007/s10614-023-10427-x*.

**2022**

- Petropoulos, F., Apiletti, D., Assimakopoulos, V., ... Jeon, Jooyoung, …, Ziel. "Forecasting: theory and practice". *International Journal of Forecasting, in press. DOI: 10.1016/j.ijforecast.2021.11.001*.

## 수상과 선정

교수 누리집 Honors & Awards 절의 수상 4건이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^home]

- 2022 · KAIST President's Award for Impact Research
- 2023 · KAIST President's Award for Impact Research
- 2024 · KAIST President's Award for Impact Research
- 2025 · KAIST President's Award for Impact Research

## 연락과 위치

- 교수 업무 이메일: j.jeon@kaist.ac.kr[^home][^faculty]
- 기관 전화: 042-350-4032[^faculty][^gsds]
- 교수 위치: 융합연구동(N5) 2250호[^faculty]
[^home]: Predictive Analytics Lab, Research Interests·Education·Positions Held·Publications·Honors & Awards·Teaching·Research Projects·Students. <https://sites.google.com/view/jyjeon/about-me> 관측일 2026-11-12.
[^faculty]: KAIST AI미래학과 교수진, 전주영 전임교수의 연구 분야·연락처·위치. <https://aicollege.kaist.ac.kr/fx/faculty> 관측일 2026-11-11.
[^gsds]: KAIST 데이터사이언스대학원 사람들, 전주영 교수의 국문 이름과 기관 전화. <https://gsds.kaist.ac.kr/people> 관측일 2026-11-12.
[^p1]: J. Park 외, K. Ahn, Applied Energy (2023 온라인 공개). <https://doi.org/10.1016/j.apenergy.2023.122109> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050756677,publication_year:2021-2026> 관측일 2026-11-12.
[^p2]: S. Kim, J. Jeon, H. Kim, Environmental Research Letters (2024). <https://doi.org/10.1088/1748-9326/ad61ff> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050756677,publication_year:2021-2026> 관측일 2026-11-12.
[^p3]: H. Kim 외, K. Ahn, PLoS ONE (2023). <https://doi.org/10.1371/journal.pone.0290168> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050756677,publication_year:2021-2026> 관측일 2026-11-12.
[^p4]: Y. K. Won 외, D. H. Lim, Computers in Biology and Medicine (2025). <https://doi.org/10.1016/j.compbiomed.2025.109976> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050756677,publication_year:2021-2026> 관측일 2026-11-12.
[^p5]: F. Petropoulos 외, F. Ziel, International Journal of Forecasting (2022). <https://doi.org/10.1016/j.ijforecast.2021.11.001> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5050756677,publication_year:2021-2026> 관측일 2026-11-12.

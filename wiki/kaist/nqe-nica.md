# 원자력 계측제어 및 자율운전 연구실 (Nuclear I&C and Autonomous Operation Laboratory, NICA)

**KAIST 원자력및양자공학과 · 김종현 교수**

- 분야: 원자력 발전소 운전의 자동화와 자율운전, 운전 지원 인공지능(사고 진단과 상태 예측), 인간 신뢰도 분석과 인적 오류, 인간공학과 디지털 주제어실·운전원 지원 시스템 설계
- 대분야: 에너지·환경·지구, 산업·시스템
- 태그: 원자로·원자력 시스템[^ov][^prof][^p1], 강화학습[^p1], 과학·공학 AI[^p2]
- 홈페이지: <https://nqe-nica.kaist.ac.kr/>
- 근거와 출처: [원자력 계측제어 및 자율운전 연구실 근거 페이지](nqe-nica-sources.md)

> 원자력 발전소의 안전을 위해 운전원의 인적 오류를 줄이는 것을 목표로, 발전소 운전을 자동화하는 인공지능과 운전원이 오류를 일으킬 가능성을 정량화하는 인간 신뢰도 분석을 함께 연구하는 원자력및양자공학과 연구실이다.[^ov][^prof]

## 무엇을 연구하나

연구실은 KAIST 원자력및양자공학과 김종현 교수가 이끄는 원자력 계측제어 및 자율운전 연구실(NICA)이다.[^dept][^notice][^prof] 계측제어(I&C, Instrumentation and Control)는 시설의 상태를 재는 계측 설비와 그 값을 바탕으로 설비를 조절하는 제어 설비를 함께 이르는 말이다.

누리집 Overview 페이지는 「Human error contribution : over the world」라는 제목 아래 세계 원자력 발전소 사건의 원인을 INPO, WANO, IAEA, OECD/NEA, EPRI, NRC 등의 운전 보고서로 모은 자료(2010–2011년, 모두 2379건)를 싣고, 기술로 사람의 수행도를 높일 수 있다고 적는다.[^ov] 이어 인적 오류(사람이 작업 중에 저지르는 실수나 잘못된 판단)의 가능성을 줄이는 것이 원자력 발전소의 안전에 결정적이며, 연구실은 원자력 발전소의 인적 오류를 0으로 만드는 것을 목표로 연구한다고 적는다.[^ov]

교수 소개 페이지는 연구 관심 분야를 다섯 가지로 적는다. 인간공학(사람의 능력과 한계에 맞춰 기계·작업·환경을 설계하는 분야), 원자력 발전소의 자동화와 자율운전, 원자력 발전소의 인간 신뢰도 분석, 원자력 발전소 운전에 대한 인공지능 응용, 디지털 주제어실과 전산화된 운전원 지원 시스템의 설계다.[^prof]

누리집 Project 페이지에서 2024년 이후 시작한 과제에는 「소형모듈형원자로 지능형 자동운전 및 디지털트윈 프레임기술 개발」, 「SMR 가상원자로 플랫폼 개발」, 「가상원자로 슈퍼컴퓨팅 플랫폼 개발-고수준 자율운전 핵심기술 개발」, 「인공신경망 기반 혁신적 원자로 감시 및 보호 시스템 개념 개발 및 타당성 연구」, 「실시간 3차원 노심출력분포 계산 및 운전지원 통합시스템 개발」, 「다중모듈환경 인적수행도 자료 수집 및 분석」, 「데이터 기반 철도시스템 안전 평가 예측 기술 개발」이 있다.[^proj] 2022–2023년에 시작한 과제에는 「인적오류 저감을 위한 비정상 운전 의사결정지원 인공지능 방법 개발」, 「비상대응조직 의사소통 신뢰도 평가방법 개발」, 「중대사고관리지침서 전산화 요소기술 개발」, 「철도 종사자의 인적오류 분석·평가·예방 기술개발」이 있다.[^proj] 누리집 Facility 페이지는 「원자력 발전소 다중모듈 주제어실 (Main Control Room)」 항목에 혁신형 SMR 운전 환경을 모사한 다중 모듈 주제어실 실험 설비 구축을 적는다.[^fac]

대표 논문 1은 SMR의 출력 증가 운전을 심층 강화학습과 규칙 기반 시스템으로 자동화하는 알고리즘을, 대표 논문 2는 설명 가능한 인공지능으로 발전소 진단에 쓸 변수를 고르는 방법을 다룬다.[^p1][^p2] 대표 논문 3은 발전소 운전의 의사소통에서 오류가 날 확률을 화행(말을 통해 요청·보고 같은 행위를 하는 것) 단위로 추정하는 방법을 제안한다.[^p3] 구성원 카드의 연구 주제에는 원자력 발전소 운전원 지원 시스템, 다중 모듈 원자력 발전소 운전원의 인간 신뢰도 분석, 강건한 인공지능 기반 자율운전 틀, 자동화 수준과 기능 배분, 부하 추종 운전(전력 수요 변화에 맞춰 발전 출력을 바꾸는 운전)을 위한 강화학습 모형, 센서 고장을 찾는 온라인 감시가 있다.[^students]

## 주요 연구 주제

### 1. 원자력 발전소 운전의 자동화와 운전 지원 인공지능

원자력 발전소의 자동화와 자율운전을 연구하며, 출력 증가 운전 같은 운전 업무를 강화학습과 규칙 기반 시스템을 결합한 알고리즘으로 자동화한다.[^prof][^p1] SMR의 지능형 자동운전과 가상원자로 플랫폼의 자율운전 기술 과제를 수행한다.[^proj] 발전소 상태 변수로 비정상·비상 상황을 진단할 때 설명 가능한 인공지능으로 진단에 쓸 변수를 고르는 연구도 한다.[^p2]

### 2. 인간 신뢰도 분석과 인적 오류

원자력 발전소 운전원이 오류를 일으킬 확률을 추정하는 인간 신뢰도 분석 방법을 연구하고, 조직 안과 조직 사이 의사소통의 오류 확률을 화행 단위로 정량화한다.[^prof][^p3] Project 페이지에는 다중 모듈 환경의 인적 수행도 자료 수집과 비상 대응 조직의 의사소통 신뢰도 평가 과제가 있다.[^proj]

### 3. 디지털 주제어실과 운전원 지원 시스템 설계

인간공학을 바탕으로 디지털 주제어실과 전산화된 운전원 지원 시스템을 설계하고, 혁신형 SMR 운전 환경을 모사한 다중 모듈 주제어실 실험 설비를 구축한다.[^prof][^fac]

## 대표 논문

누리집 Journals 게시판의 2021–2026년 논문 가운데 김종현 교수의 KAIST 부임(2024년 3월) 뒤 출판되고 교수 소속이 KAIST로 기록된 논문에서 초록을 확인할 수 있는 세 편을 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Automating Power-Increase Operation for Small Modular Reactors Based on Task Analysis with Proximal Policy Optimization](https://doi.org/10.1016/j.net.2025.103767) · Nuclear Engineering and Technology 58 | 소형모듈원자로(SMR)는 여러 모듈을 함께 운전하도록 설계되어 운전원의 업무 부담이 늘어나는 문제가 있고, 오랜 시간 계속 감시하며 손으로 조정해야 하는 출력 증가 운전에서 이 부담이 더 커진다. 이를 해결하려고 SMR 출력 증가 운전의 업무를 자율적으로 수행하는 알고리즘을 제안했다. SMR 운전을 모사하는 일체형 가압경수로(integral pressurized water reactor, 가압경수로는 물에 높은 압력을 가해 끓지 않게 한 채 냉각재로 쓰는 원자로) 시뮬레이터로 먼저 출력 증가 운전의 업무 분석(task analysis)을 해 자동화할 후보 업무를 찾고 자동화 전략을 세웠다. 그 결과를 바탕으로 심층 강화학습 기반 시스템인 근위 정책 최적화(PPO, proximal policy optimization)와 if-then 규칙 기반 시스템을 결합해 알고리즘을 설계했다. 실험에서 알고리즘은 운전 제약 안에 머물면서 원자로 출력 100 %에 이르러 출력 증가 운전을 해냈다. 개발한 알고리즘을 그래픽 사용자 화면으로 구현해, 출력 증가 운전 중 주요 변수를 실시간으로 감시할 수 있게 했다.[^p1] | 1저자 H.-J. Lee, 마지막 저자 김종현 (3명) |
| 2 | 2025 | [Enhancing nuclear power plant diagnostics: A comparative analysis of XAI-based feature selection methods for abnormal and emergency scenario detection](https://doi.org/10.1016/j.pnucene.2025.105759) · Progress in Nuclear Energy 185 | 설명 가능한 인공지능(XAI, 인공지능 모델의 판단 과정이나 근거를 사람이 이해할 수 있게 드러내는 기법)을 원자력 발전소 진단의 특징 선택(모델에 넣을 입력 변수 가운데 필요한 것을 고르는 일)에 적용했다. 기울기 기반 기법, 층별 관련도 전파(LRP), DeepSHAP, 적분 기울기, LIME, 돌출 지도(saliency map) 같은 XAI 방법을 전통적 방법인 주성분 분석(PCA, 여러 변수를 서로 상관없는 새 변수들로 바꿔 자료의 변동을 나타내는 통계 기법)과 비교했다. 비정상·비상 시나리오 35개와 상태 변수 116개를 담은 IAEA iPWR 시뮬레이터 자료에 적용해, XAI 기반 방법이 발전소 상태를 서로 구별하는 변수를 고르는 데 더 뛰어남을 보였다. 높은 진단 정확도를 유지하면서 입력 변수를 116개에서 20개로 줄였다. 특히 돌출 지도와 DeepSHAP이 비정상 상황마다 뚜렷한 패턴을 드러내 전통 기법을 앞섰다. 저자들은 입력 차원을 줄이면 사이버 보안, 사람과 기계 사이 화면, 계산 효율에 이점이 있다고 적는다.[^p2] | 1저자 Y. H. Chae, 마지막 저자 김종현 (5명) |
| 3 | 2025 | [Method to Estimate Communication Error Probabilities Based on Speech Acts for Nuclear Power Plants](https://doi.org/10.1016/j.net.2025.103740) · Nuclear Engineering and Technology 57 | 의사소통 오류는 원자력 발전소의 안전에 영향을 주지만 기존 인간 신뢰도 분석은 이를 따로 분석하지 않아, 의사소통 오류 확률(CEP)을 추정하기 어렵다. 지금의 방법은 정성 평가에 기대거나 통계적 근거가 부족하다. 이 연구는 화행에 기반해 발전소 운전의 CEP를 추정하는 방법을 제안했다. 의사소통을 요청(Request), 보고(Report), 선언(Declaration), 확인(Acknowledgment), 복구(Recovery)의 다섯 화행으로 나누고, 절차상 의사소통 순서를 나타내는 도표를 만들어 의사소통 흐름을 모형화하며, CEP를 계산하는 식을 세웠다. 화행별 오류 확률은 조직 안 의사소통은 시뮬레이터 훈련 관찰 자료의 통계 분석으로, 조직 사이 의사소통은 전문가 의견 수렴(expert elicitation)으로 추정했다. 사례 연구로 조직 안 의사소통에서는 고압 안전 주입 계통(사고 때 원자로 냉각재 계통에 높은 압력으로 물을 넣는 설비)을 기동하는 운전원 실패를, 조직 사이 의사소통에서는 1 MW 이동형 가스 터빈 발전기를 배치하는 실패를 분석했다. 조직 안팎의 CEP에 영향을 주는 수행 영향 인자(PSF, performance shaping factor, 사람의 작업 수행에 영향을 주는 조건)도 논의했다.[^p3] | 1저자 I. Song, 마지막 저자 김종현 (3명) |

## 교수와 전문 분야

김종현 교수(Jonghyun Kim)는 KAIST 원자력및양자공학과 교수다.[^dept][^prof] 교수 소개 페이지에 따르면 KAIST에서 원자력공학 학사(1996년 2월)와 석사(1998년 2월)를, 원자력및양자공학 박사(2004년 2월)를 받았다. 박사 학위 논문은 원자력 발전소 진단 업무의 정보 흐름과 정보 보조 수단의 효과를 정량화하는 연구다(「A Study on Quantification of the Information Flow and Effectiveness of Information Aids for Diagnosis Tasks in Nuclear Power Plants」).[^prof] 경력 줄은 KAIST Center for Advanced Reactor Research(CARR) 박사후연구원(2004년 3–12월), KEPCO Engineering and Construction(KEPCO E&C) Probabilistic Safety Assessment(PSA, 확률론적 안전성 평가) Group 연구원(2004년 12월–2005년 11월), Korea Hydro & Nuclear Power(KHNP) Central Research Institute의 Man-Machine Interface System(MMIS) Team 연구원(2005년 11월–2009년 1월), 스위스 Paul Scherrer Institute의 Risk and Human Reliability Group 과학자(Scientist, 2009년 2월–2011년 6월), KEPCO International Nuclear Graduate School(KINGS) 부교수(2011년 7월–2015년 9월), 조선대학교(Chosun University) 교수(2015년 10월–2024년 2월), KAIST 교수(2024년 3월–)다. 2014년 3–6월과 2017년 3–6월에는 KAIST 대우교수(Adjunct Professor)를 지냈다고 적혀 있다.[^prof] 확률론적 안전성 평가는 사고로 이어지는 사건들의 발생 확률을 따져 시설의 위험도를 평가하는 방법이다. 전공 분야(Major Field)는 원자력공학(Nuclear Engineering)이고, 책 「Autonomous Nuclear Power Plants with Artificial Intelligence」(Lecture Notes in Energy 94, Springer, 2023)의 공저자다.[^prof]

누리집 Journals 게시판은 교수의 논문을 1999년부터 싣는다. 교수의 KAIST 부임 전인 2018–2020년 항목에는 LSTM(long short-term memory, 시간 순서로 들어오는 자료의 앞뒤 관계를 기억해 처리하는 순환 신경망의 한 종류)을 쓴 사고 진단 알고리즘, 심층 강화학습과 규칙 기반 시스템으로 원자력 발전소 출력 증가 운전을 자율로 하는 알고리즘, 다수기 확률론적 안전성 평가에서 인적 실패 사건의 종속성을 분석하는 방법 논문이 있다.[^journals]

연구 관심 분야, 경력, 2021–2026년 논문으로 보면 전문 분야는 세 갈래다.

- **원자력 발전소 운전 자동화와 인공지능**: 강화학습과 인공지능으로 원자력 발전소의 운전 업무를 자동화하고 발전소 상태를 진단하는 연구.[^prof][^p1][^p2]
- **인간 신뢰도 분석**: 운전원과 조직의 오류 확률을 추정하고 인적 오류를 분석하는 방법 연구.[^prof][^p3]
- **인간공학과 주제어실 설계**: 디지털 주제어실과 전산화된 운전원 지원 시스템의 설계.[^prof][^fac]

## 응용 분야

연구 대상은 원자력 발전소와 여러 모듈을 함께 운전하는 SMR의 운전과 안전이다.[^ov][^fac][^p1] Project 페이지의 과제 발주 기관에는 한국원자력연구원, 한국수력원자력, 한국전력기술, 한전원자력연료, 한국원자력안전재단, Idaho National Laboratory가 있고, 철도기술연구원과 국토교통부 과제로 철도 시스템의 안전 평가와 철도 종사자의 인적 오류도 다룬다.[^proj] 졸업생 진로 칸에는 KINAC, 한국원자력연구원, 한국원자력통제기술원, 한국수력원자력 중앙연구원, 한전기술, Idaho National Laboratory, Institute for Energy Technology 등이 있다.[^alumni][^hera]

## 구성원

2026년 10월 23일 누리집 Students·Staff 페이지 기준이다. Students 페이지 11명과 Staff 페이지의 위촉연구원 1명이며, 과정과 연구 주제는 각 카드의 「과정」「관심연구분야」「역할」「분야」 표기를 옮겼다. 이메일은 카드에 적힌 주소다.[^students][^staff] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Kim, Hyojin (김효진) | 박사과정 | Development of operator support system for nuclear power plants | kim05140@kaist.ac.kr |  |
| Kim, Taeryeon (김태련) | 박사과정 | Human Relibility Analysis of Operators in Multi-Module Nuclear Power Plants, Human Factors Engineering Evaluation of Nuclear Power Plant Operators | bkteddy00@kaist.ac.kr |  |
| Lee, Heejae (이희재) | 박사과정 | Robust AI-based Autonomous Operation Framework (Event Diagnosis, Operation Automation) | lee.heejae21@kaist.ac.kr | 1 |
| Kim, Huijeong (김희정) | 박사과정 | Levels of automation (LOAs), functional requirements analysis (FRA), and function allocation (FA) | huijeong.kim@kaist.ac.kr |  |
| Bang, Junhyeong (방준형) | 석사과정 | Development of Reinforcement Learning Models for Load-Following Operation of Nuclear Power Plants | bjun201gosegulv@kaist.ac.kr |  |
| Lee, Jiyong (이지용) | 박사과정 | On-Line Monitoring for Detecting Sensor Fault | jylee2588@kaist.ac.kr |  |
| Jhee, Taeyoung (지태영) | 석사과정 | human factor engineering, Human Reliability Analysis for Small Modular Reactor | docterjhee@kaist.ac.kr |  |
| Kim, Gwanwoo (김관우) | 석사과정 | AI-based Autonomous Operation on Nuclear Power Plant | kwanwoo1017@kaist.ac.kr |  |
| Kim, Doyeon (김도연) | 학부 연구생 | AI-Based Autonomous Driving Technology for SMRs | kimdoyeon707@kaist.ac.kr |  |
| Choi, Suhyeon (최수현) | 석사과정 | Flexible Operation of Nuclear Power Plants and Operational Situation Prediction | science326@kaist.ac.kr |  |
| Park, Eunsoo (박은수) | 석사과정 | Human factors modeling for adaptive safety-critical systems | silveres@kaist.ac.kr |  |
| Yang, Taewon (양태원) | 연구원 | Human factors engineering, Human Reliability Analysis, Simulator study |  | 3 |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 「NICA Alumni」 구역 4명과 「HERA Alumni」 구역 13명을 그 순서대로 실었다. 학위 칸, 졸업 연월, 진로 칸은 각 줄의 표기다.[^alumni][^hera] 교수는 2024년 3월 KAIST에 부임했으며, HERA Alumni 구역의 졸업 연월(2019년 2월–2025년 2월)은 대부분 그 전이다.[^prof][^hera] 진로 칸이 빈 줄이 있다.

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| bin Mohamad Fahmi, Adam Haziq | 석사 (2026.2) |  |
| 이기연 | 석사 (2026.2) |  |
| 이찬서 | 박사 (2025.8) | KINAC |
| 송일근 | 석사 (2025.2) |  |
| 박주영 | 석사 (2019.2) | Idaho National Laboratory |
| 양재민 | 석사 (2019.2) | University of Illinois Urbana-Champaign |
| Arigi Mohammed Awwal | 박사 (2020.2) | Institute for Energy Technology |
| 박가영 | 석사 (2020.2) | 한국수력원자력 중앙연구원 |
| 이승헌 | 석사 (2020.2) | BEES |
| 이수봉 | 석사 (2020.8) | 한국원자력통제기술원 |
| 윤경민 | 석사 (2021.2) | BEES |
| 박범준 | 석사 (2022.2) | ㈜ 유엠아이 |
| 김효진 | 석사 (2022.2) | 한국과학기술원 박사과정 진학 |
| 이대일 | 박사 (2023.2) | 한국원자력연구원 |
| 최윤희 | 석사 (2023.2) | 한국원자력통제기술원 |
| 김재현 | 석사 (2025.2) | 한전기술 |
| 양태원 | 석사 (2025.2) | Idaho National Laboratory |

## 최근 논문 목록 (2021–2026)

누리집 Journals 게시판(1–60번)의 2021–2026년 항목 42–60번 가운데 같은 논문을 두 번 적은 2건을 한 번씩만 실은 17편과, Conferences 게시판(1–77번)의 2021–2026년 항목 41–77번 37편을 합친 54편이다(2026년 8편, 2025년 7편, 2024년 8편, 2023년 9편, 2022년 10편, 2021년 12편).[^journals][^conf] 두 게시판은 교수의 논문 목록이라, 교수의 KAIST 부임(2024년 3월) 전 조선대학교 시기 논문이 섞여 있다.[^prof] 연도는 게시판의 연도 분류이고, 저자·제목·학술지·학회 표기는 누리집 그대로다. 「(Corresponding Author)」 표시도 누리집 표기다. 목록 구성 기준은 근거 페이지에 적었다.

**2026**

- Hyojin Kim, Seungheon Lee, Jonghyun Kim. Mitigation action-dependent prediction of nuclear plant parameters for severe accident management via conditional generative model, Reliability Engineering & System Safety (2026): 112892
- Hee-Jae Lee, Jonghyun Kim. Autonomous Power-Increase Operation for Small Modular Reactor based on Task Analysis with Proximal Policy Optimization, PSAM, July, 2026
- Dong Hyeon Shin, Hee-Jae Lee, Jonghyun Kim. Intelligent Signal Classification for False Alarm Reduction via Multi-domain Feature Transformation, KNS, May, 2026
- Huijeong Kim and Jonghyun Kim. Development of a New Methodology for Function Allocation in Small Modular Reactors (KNS), Jeju, Korea, 2026
- Tae Young Jhee, Tae Ryoun Kim, and Jonghyun Kim(KAIST), Soonae Lee(KHNP). Development of a Built-in Automatic Testing Method for Digital Protection Logic (KNS), Jeju, Korea, 2026
- Hee-Jae Lee and Jonghyun Kim. Development of ADS-based Operator Action Support System for Abnormal Operation (KNS), Jeju, Korea, 2026
- Junhyeong Bang and Jonghyun Kim. Control-Rod Position Prediction for Load-Following Operation via a Reinforcement Learning Platform with a Pre-trained CVAE (KNS), Jeju, Korea, 2026
- Gwanwoo Kim, Hee-jae Lee, and Jonghyun Kim. Developing a Robust Multi-agent Reinforcement Learning Framework for Autonomous SMR Abnormal Operations using Abstraction Hierarchy (KNS), Jeju, Korea, 2026

**2025**

- Chae, Y. H., Kim, S. G., Choi, J., Koo, S. R., & Kim, J. Enhancing nuclear power plant diagnostics: A comparative analysis of XAI-based feature selection methods for abnormal and emergency scenario detection. Progress in Nuclear Energy, 185, 105759.
- Song, I., Yang, T., & Kim, J. Method to Estimate Communication Error Probabilities Based on Speech Acts for Nuclear Power Plants. Nuclear Engineering and Technology, 103740, 2025.
- Hee-Jae Lee, Daeil Lee, Jonghyun Kim. Automating Power-Increase Operation for Small Modular Reactors Based on Task Analysis with Proximal Policy Optimization, Nuclear Engineering and Technology (2025): 103767.
- Huijeong Kim, Jonghyun Kim. Taxonomies of Levels of Automation for Nuclear Power Plants Based on Operational Conditions, NPIC&HMIT, June, 2025
- Geonju Lee, Hee-Jae Lee, Jonghyun Kim. Signal Anomaly Classification in Piezoelectric Sensor System Using Tree-Based Ensemble Models, KNS, Oct. 2025
- Adam Haziq, M. F., & Kim, J. Redefinition of Performance Shaping Factors (PSFs) Pertinent to Small Modular Reactors (SMRs).
- Yang, T., Boring, R., & Park, J. Time Distribution Analysis for Task Primitives to Support Dynamic Human Reliability Analysis. Human Error, Reliability, Resilience, and Performance, 173, 12, 2025.

**2024**

- Taewon Yang, Ronald L. Boring, Chad Pope, Jonghyun Kim and Jooyoung Park. Analysis of Human Error and Performance in Correlation with Simulator Complexity, Annals of Nuclear Energy, Vol. 207, 110727, 2024
- Jaehyun Kim, Sungheon Lee, Awwal Arigi, Jonghyun Kim. Quantitative analysis of contributing factors to the resilience of emergency response organizations in nuclear power plants, Progress in Nuclear Energy, Vol. 172, 2024 (Corresponding Author)
- Hee-Jae Lee, Daeil Lee, Jonghyun Kim. Event diagnosis method for a nuclear power plant using meta-learning, Nuclear Engineering and Technology, Vol 56, 2024 (Corresponding Author)
- Hee-Jae Lee, Daeil Lee, San Kang, Jonghyun Kim. Power-Increase Automation Algorithm of Small Modular Reactor Using Robust AI-based Reinforcement Learning and a Rule-Based System, ISOFIC, Dec. 2024
- Hee-Jae Lee, Daeil Lee, Jonghyun Kim. Power Increase Automation of Small Modular Reactor Using Proximal Policy Optimization and a Rule-based System, KNS, Oct. 2024
- Ilgeun Song, Taewon Yang, Jonghyun Kim. “Expert Elicitation for Estimating Inter-Organizational Communication Error Probabilities in NPP operations” Korean Nuclear Society Autumn Meeting, Changwon, Korea, 2024. Oct.
- Taewon Yang, Jonghyun Kim. “Evaluation of Communication Error Probabilities Among Main Control Room Operators During Emergency Situations in Nuclear Power Plants” Korean Nuclear Society Autumn Meeting, Changwon, Korea, 2024. Oct.
- Park, J., Yang, T., Boring, R., & Kim, J. Approach for Inferring Full-Scope Human Reliability Data Based on Simplified Simulator Data. Transactions of the American Nuclear Society, 130(1), 278-281, 2024.

**2023**

- Jooyoung Park, Taewon Yang, Ronald L. Boring, Thomas A. Ulrich and Jonghyun Kim. Analysis of Human Performance Differences between Students and Operators when Using the Rancor Microworld Simulator, Annals of Nuclear Energy, Vol. 180, 109502, 2023
- Hyojin Kim, Jonghyun Kim. Long-term prediction of safety parameters with uncertainty estimation in emergency situations at nuclear power plants, Nuclear Engineering and Technology, Vol., 1630-1643, 2023 (Corresponding Author)
- Hee-Jae Lee, Daeil Lee, Jonghyun Kim. Anomaly Recovery Algorithm Based on Robust AI Concept for Nuclear Power Plants, NPIC-HMIT, July, 2023
- Hee-Jae Lee, Daeil Lee, Jonghyun Kim. Development of Anomaly Recovery Algorithm Based on Concept of Robust AI, KNS, May, 2023
- Junghwan Yun, Taewon Yang, Jaehyun Kim, Jonghyun Kim. "Estimation of communication reliability for human reliability analysis at nuclear power plants," Korean Nuclear Society Autumn Meeting, Gyeongju, Korea, 2023. Oct.
- Taewon Yang, Jooyoung Park, Ronald L. Boring and Jonghyun Kim. “Comparison of Error Rate Depending on Operator Expertise and Simulator Complexity”, Korean Nuclear Society Spring Meeting, Jeju, Korea, 2023, May.
- Jooyoung Park, Taewon Yang, Jonghyun Kim, Ronald Boring and Chad Pope. " An Investigation of Time Distributions for Task Primitives to Support the HUNTER Dynamic Human Reliability Analysis," AHFE 2023 International Conference on Human Factors in Design, Engineering, and Computing, 2023, Dec
- Ji Suk Kim, Ronald L. Boring, Torrey J. Mortenson, Thomas A. Ulrich, Jooyoung Park, Taewon Yang, Jonghyun Kim. "Dynamicizing SPAR-H: Generalized Form for Auto-Calculating the Performance Shaping Factor for Experience and Training", 13th Nuclear Plant Instrumentation, Control & Human-Machine Interface Technologies (NPIC&HMIT), Knoxville, TN, 2023. July.
- Taewon Yang, Jooyoung Park, Ronald L. Boring and Jonghyun Kim. "An Experimental Investigation of Students’ Learning Effects When Using a Simplified Nuclear Simulator", 13th Nuclear Plant Instrumentation, Control & Human-Machine Interface Technologies (NPIC&HMIT), Knoxville, TN, 2023. July.

**2022**

- Sunghen Lee, Jaehyun Kim, Awwal Arigi, Jonghyun Kim. Identification of contributing factors to organizational resilience in the emergency response organization for nuclear power plants, Energies, Vol. 15, 2022
- Daeil Lee, Seoryong Koo, Inseok Jang, Jonghyun Kim. Comparison of Deep Reinforcement Learning and PID Controllers for Automatic Cold Shutdown Operation, Energies, Vol. 15, 2022 (Corresponding Author)
- Jooyoung Park, Ronald Boring, Thomas Ulrich, Roger Lew, Sungheon Lee, Bumjun Park, Jonghyun Kim. A framework to collect human reliability analysis data for nuclear power plants using a simplified simulator and student operators, Reliability Engineering and System Safety, Vol. 221, 2022 (Corresponding Author)
- Younhee Choi, Gyeongmin Yoon, Jonghyun Kim. Unsupervised learning algorithm for signal validation in emergency situations at nuclear power plants, Nuclear Engineering Technology, Vol. 54, 1230-1244, 2022 (Corresponding Author)
- Subong Lee, Jonghyun Kim. Design of computerized operator support system for technical specification monitoring, Annals of Nuclear Energy, Vol. 165, 2022 (Corresponding Author)
- Gayoung Park, Awwal M. Arigi, Seo-Ryong Koo and Jonghyun Kim. Dependency Analysis of Human Failures in Multi-unit Scenarios: Types and Evaluation Method, Probabilistic Safety Assessment and Management Conference (PSAM), Honolulu, USA, 2022
- Hee-Jae Lee, Daeil Lee and Jonghyun Kim. Anomaly Diagnosis of Nuclear Power Plants Using Robust AI, ANS Winter Meeting, Phoenix, AZ, USA, Nov. 13-17, 2022
- Younhee Choi and Jonghyun Kim. Faulty Signal Restoration Algorithm in the Emergency Situation Using Deep Learning Methods, International Conference on Applied Human Factors and Ergonomics (AHFE), Springer, Cham, July, 2022
- Deail Lee, Hee-Jae Lee and Jonghyun Kim. Robust AI for Accident Diagnosis of Nuclear Power Plants Using Meta-Learning, International Conference on Applied Human Factors and Ergonomics (AHFE), Springer, Cham, July, 2022
- Taewon Yang, Jooyoung Park, Ronald L. Boring and Jonghyun Kim. Human Performance Analysis Depending on Expertise and Simulator Complexity, ANS Annual Meeting, Anaheim, CA, USA, June 12-16, 2022

**2021**

- Awwal M. Arigi, Gayoung Park, Jonghyun Kim. An approach to analyze diagnosis errors in advanced main control room operations using the Cause-Based Decision Tree method, Energies, Vol. 14, 2021 (Corresponding Author)
- Ji Tae Kim, Jonghyun Kim, Poong Hyun Seong, Jooyoung Park. Quantitative resilience evaluation on recovery from emergency situations in nuclear power plants, Annals of Nuclear Energy, Vol. 156, 2021
- Hyojin Kim, Awwal Mohammed Arigi, Jonghyun Kim. Development of a diagnostic algorithm abnormal situations using long short-term memory and variational autoencoder, Annals of Nuclear Energy, Vol 153, 2021 (Corresponding Author)
- Jaehyun Kim, Sungheon Lee and Jonghyun Kim. Identification of Contributing Factors to Reliability of Emergency Response Organization Using the Delphi and Analytic Hierarchy Process Methods, International Conference on System Reliability and Science (ICSRS), November, 2021
- Taewon Yang, Bumjun Park, Sungheon Lee, Jeong Hun Choi, Jooyoung Park, Ronald L. Boring and Jonghyun Kim. An Experimental Analysis of Human Performance According to the Simulator Complexity, International Conference on System Reliability and Science (ICSRS), November, 2021
- Hyojin Kim and Jonghyun Kim. Development of a Long-Term Prediction Algorithm with Uncertainty Estimation Using BiLSTM and AM, International Symposium on Future I&C for Nuclear Power Plants (ISOFIC), November, 2021
- Hyojin Kim and Jonghyun Kim. Multi-Step Prediction Algorithm for Critical Safety Parameters at Nuclear Power Plants Using BiLSTM and AM, Proceedings of the 31st European Safety and Reliability Conference (ESREL 2021), Angers, France, September, 2021
- Daeil Lee, Hyojin Kim, Younhee Lee, Jonghyun Kim. Development of Autonomous Operation Agent for Normal and Emergency Situations in Nuclear Power Plants, International Conference on System Reliability and Science (ICSRS), November, 2021
- Daeil Lee, and Jonghyun Kim. Autonomous Agent for Emergency Operation of Nuclear Power Plant Using Soft Actor-Critic Agent, International Symposium on Future I&C for Nuclear Power Plants (ISOFIC), November, 2021
- Younhee Choi, Gyengmin Yoon and Jonghyun Kim. Algorithm for the Signal Validation in the Emergency Situation Using Unsupervised Learning Methods, International Conference on Applied Human Factors and Ergonomics (AHFE), Springer, Cham, 2021
- Awwal M. Arigi and Jonghyun Kim. Examining the effect of a proposed operator support system on human error probability estimation, Proceedings of the 31st European Safety and Reliability Conference (ESREL 2021), Angers, France, September, 2021
- Daeil Lee, and Jonghyun Kim. Autonomous Emergency Operation of Nuclear Power Plant Using Deep Reinforcement Learning." International Conference on Applied Human Factors and Ergonomics. Springer (AHFE), Cham, 2021

## 특허

누리집 Patents 게시판 1–7번 가운데 출원일·등록일이 2021-10-13 이후인 4건이다. 번호, 날짜, 발명자는 누리집 표기이며, 네 건 모두 교수의 KAIST 부임(2024년 3월) 전 날짜다.[^patents][^prof]

- 원자력 발전소의 비정상 운전원을 위한 운전지원 시스템 및 방법 (출원번호 10-2023-0101269; 출원일 2023.08.02; 발명자 김종현, 나만균, 이대일, 박지훈, 최윤희, 오상원, 김효진)
- 신뢰도 문제에 따라 분기 방식 적용이 가능한 동적이산사건수목 분석 장치 및 그 작동 방법 (등록번호 10-2447891-0000; 등록일 2022.09.22; 발명자 허균영, 백세진, 김태완, 김종현, 서재승)
- 동적이산사건수목의 분석 장치 및 그 방법 (등록번호 10-2424416-0000; 등록일 2022.07.19; 발명자 허균영, 김태완, 백세진, 김종현)
- 원자력발전소 안전해석용 데이터 연계 시스템 및 그 동작 방법 (등록번호 10-2354122-0000; 등록일 2022.01.18; 발명자 허균영, 김태완, 김종현)

## 연구 과제

누리집 Project 페이지의 과제 34건 가운데 연구 기간이 2021-10-13–2026-10-13과 겹치는 26건이다. 과제명, 발주 기관(목록의 「지원」), 기간은 누리집 표기다. Project 페이지는 교수의 KAIST 부임(2024년 3월) 전 과제도 함께 싣는다.[^proj][^prof]

- AI + S&T 혁신 기술 개발 (지원 한국과학기술원; 기간 2026.04.01 ~ 2029.12.31)
- 인공신경망 기반 혁신적 원자로 감시 및 보호 시스템 개념 개발 및 타당성 연구 (지원 한국과학기술원; 기간 2026.01.20 ~ 2029.01.19)
- 실시간 3차원 노심출력분포 계산 및 운전지원 통합시스템 개발 (지원 한전원자력연료; 기간 2025.06.01 ~ 2028.12.31)
- 데이터 기반 철도시스템 안전 평가 예측 기술 개발 (지원 철도기술연구원; 기간 2025.04.01 ~ 2029.12.31)
- 소형모듈형원자로 지능형 자동운전 및 디지털트윈 프레임기술 개발 (지원 한국원자력연구원; 기간 2025.04.01 ~ 2029.12.31)
- SMR 가상원자로 플랫폼 개발 (지원 한국원자력연구원; 기간 2024.05.01 ~ 2029.12.31)
- 가상원자로 슈퍼컴퓨팅 플랫폼 개발-고수준 자율운전 핵심기술 개발 (지원 국가과학기술연구회; 기간 2024.06.01 ~ 2029.05.31)
- 새울3,4호기 설계기준초과사고 및 중대사고 관련 인간공학 확인 및 검증 수행평가 (지원 한국전력기술; 기간 2024.07.01 ~ 2025.06.30)
- 다중모듈환경 인적수행도 자료 수집 및 분석 (지원 한국원자력연구원; 기간 2024.07.01 ~ 2025.12.31)
- 중대사고관리지침서 전산화 요소기술 개발 (지원 한국수력원자력; 기간 2023.11.01 ~ 2025.10.31)
- 자율 운전 성능과 안전성 향상을 위한 다목적 고정밀 계측 시스템 개발 (혁신형 SMR 예타) (지원 한국연구재단; 기간 2023.04.01 ~ 2027.12.31)
- 다수기 사고대응 인적행위 종속성 분석 방법 개발 및 Level 1 모델 HRA 종속성 분석 (지원 한국안전재단(KAERI 용역); 기간 2023.07.01 ~ 2024.11.30)
- An Investigation of Time Distributions for Task Primitives to Support the HUNTER Dynamic Human Reliability Analysis (지원 Idaho National Laboratory (INL); 기간 2023.04.01 ~ 2024.02.29)
- 철도 종사자의 인적오류 분석·평가·예방 기술개발 (지원 국토교통부 ((주)비즈 용역); 기간 2023.04.01 ~ 2027.12.31)
- 인적오류 저감을 위한 비정상 운전 의사결정지원 인공지능 방법 개발 (지원 한국연구재단; 기간 2022.04.01 ~ 2026.12.31)
- 비상대응조직 의사소통 신뢰도 평가방법 개발 (지원 한국연구재단; 기간 2022.04.26 ~ 2024.12.31)
- 혁신형 SMR 자율운전 요건 및 요소기술 개발 (지원 한국수력원자력(주) (한양대 주관 학술용역); 기간 2022.04.01 ~ 2023.11.30)
- 가동원전 사고관리계획서 인간공학 기술적용 방법론 개발 및 3자 검토 (지원 한국전력기술(주); 기간 2021.12.02 ~ 2023.11.30)
- Rancor Microworld Operator Validation Studies with Chosun University: Additional Experiment Using Compact Nuclear Simulator (지원 Idaho National Laboratory (INL); 기간 2021.06.17 ~ 2022.09.30)
- 동적신뢰도분석 DICETM에 기반한 L1/L2 PSA 분기확률 모형 개발 (지원 한국원자력안전재단; 기간 2021.04.01 ~ 2023.12.31)
- 신형 주제어실 특성을 반영한 인간신뢰도분석 수행을 위한 국내기술자문 (지원 한국전력기술㈜; 기간 2021.01.11 ~ 2024.01.10)
- 레질리언스 기반 원전 비상대응조직 신뢰도평가 방법 개발 (지원 한국원자력안전재단; 기간 2020.04.01 ~ 2022.12.31)
- 인공지능기술을 활용한 플랜트 상태 진단, 예측 및 비정상상태 안전조치 최적화 기술 개발 (지원 한국연구재단; 기간 2018.07.18 ~ 2023.06.30)
- SRA를 위한 인적/조직적 요소 분석 및 평가 방법 개발 (지원 한국원자력안전재단; 기간 2017.06.01 ~ 2021.12.31)
- 중대사고관리 지원시스템을 위한 인간공학프로그램기반 HSI 설계 (지원 한국연구재단(KAERI 위탁); 기간 2017.04.10 ~ 2021.12.31)
- 자율운전 소형모듈형 원자로 연구센터 (지원 한국연구재단(KAIST 주관); 기간 2016.06.01 ~ 2022.12.31)

## 수상

누리집 News 게시판의 수상 글 1건이다. 날짜는 게시글 작성일이고, 문장은 게시글 제목과 본문 표기를 따른다.[^news]

- 2025-11-06 · 2025 한국원자력학회(KNS) 추계학술발표회 학술발표회 우수 논문상, 김태련

## 연락과 위치

- 위치: Korea Advanced Institute of Science and Technology (KAIST) 291 Daehak-ro Guseong-dong, Yuseong-gu, Daejeon 305-701, Korea, Office: Room 1401, N7-1 (Mechanical Building)(누리집 바닥글 표기)[^home]
- 교수 연구실: N7-1, 2409(학과 교수 페이지 표기)[^deptprof]
- 교수 이메일: jonghyun.kim@kaist.ac.kr[^prof][^deptprof]
[^home]: 연구실 누리집 첫 화면 <https://nqe-nica.kaist.ac.kr/> (메뉴, 바닥글의 연구실 영문 이름·주소·사무실, 2026-10-23 열람)
[^ov]: 누리집 Introduction 「Overview」 페이지 <https://nqe-nica.kaist.ac.kr/m01_01> (인적 오류 기여 자료의 제목·설명 문구와 연구 목표 문장, 2026-10-23 열람)
[^prof]: 누리집 Family 「Professor」 페이지 <https://nqe-nica.kaist.ac.kr/m03_01> (교수 직위·연구실 이름·이메일, Major Field, Research Interests, Education, Thesis, Careers, Book, 2026-10-23 열람)
[^proj]: 누리집 Research 「Project」 페이지 <https://nqe-nica.kaist.ac.kr/m02_03> (과제명·발주기관·총연구기간 34건, 2026-10-23 열람)
[^fac]: 누리집 Research 「Facility」 페이지 <https://nqe-nica.kaist.ac.kr/m02_02> (다중모듈 주제어실 항목, 2026-10-23 열람)
[^students]: 누리집 Family 「Students」 페이지 <https://nqe-nica.kaist.ac.kr/m03_02> (학생 카드 11장, 2026-10-23 열람)
[^staff]: 누리집 Family 「Staff」 페이지 <https://nqe-nica.kaist.ac.kr/m03_03> (위촉연구원 카드, 2026-10-23 열람)
[^alumni]: 누리집 Family 「Alumni」 페이지의 NICA Alumni 구역 <https://nqe-nica.kaist.ac.kr/m03_04> (4건, 2026-10-23 열람)
[^hera]: 누리집 Family 「Alumni」 페이지의 HERA Alumni 구역 <https://nqe-nica.kaist.ac.kr/m03_04_01> (13건, 2026-10-23 열람)
[^journals]: 누리집 Publication 「Journals」 게시판 <https://nqe-nica.kaist.ac.kr/m04_01> (1–60번, 2026-10-23 열람)
[^conf]: 누리집 Publication 「Conferences」 게시판 1–6쪽 <https://nqe-nica.kaist.ac.kr/m04_02> (1–77번, 2026-10-23 열람)
[^patents]: 누리집 Publication 「Patents」 게시판 <https://nqe-nica.kaist.ac.kr/m04_03> (1–7번, 2026-10-23 열람)
[^news]: 누리집 Boards 「News」 게시판 글 「2025 한국원자력학회(KNS) 추계학술발표회 학술발표회 우수 논문상」 <https://nqe-nica.kaist.ac.kr/m05_02/3> (작성일 2025-11-06, 2026-10-23 열람)
[^notice]: 누리집 Boards 「Notice」 게시판 글 「연구실 인턴 및 석박사과정 신입생 모집」 <https://nqe-nica.kaist.ac.kr/m05_01/2> (연구실 국문 이름, 2026-10-23 열람)
[^dept]: KAIST 원자력및양자공학과 연구그룹 페이지 <https://nuclear.kaist.ac.kr/research/the_lap.php> (연구실 국문 이름, 교수 이름·학위·이메일·누리집, 2026-10-23 열람)
[^deptprof]: KAIST 원자력및양자공학과 교수 페이지 <https://nuclear.kaist.ac.kr/people/professor.php> (교수 직위·학위·연구실 위치·이메일·누리집, 2026-10-23 열람)
[^p1]: H.-J. Lee, D. Lee, J. Kim, Nuclear Engineering and Technology 58, 103767 (2026, OpenAlex 출판일 2025-06-22). <https://doi.org/10.1016/j.net.2025.103767> 초록 기준(OpenAlex 등록 초록).
[^p2]: Y. H. Chae 외, J. Kim, Progress in Nuclear Energy 185, 105759 (2025, OpenAlex 출판일 2025-03-29). <https://doi.org/10.1016/j.pnucene.2025.105759> 초록 기준(OpenAlex 등록 초록).
[^p3]: I. Song, T. Yang, J. Kim, Nuclear Engineering and Technology 57, 103740 (2025, OpenAlex 출판일 2025-06-05). <https://doi.org/10.1016/j.net.2025.103740> 초록 기준(OpenAlex 등록 초록).

# 소프트웨어 프로세스 개선 및 신뢰성 검증 연구실 (SPIRAL, Software Process Improvement and Reliability Assurance Laboratory)

**KAIST 전산학부 · 백종문 교수**

- 분야: 소프트웨어공학, 소프트웨어 신뢰성, 소프트웨어 품질 보증
- 대분야: 컴퓨팅·AI
- 태그: 프로그램 분석·검증[^p3][^p5][^p8], 대형 언어 모델[^p3][^p6], 생성 인공지능[^p4], 소프트웨어·시스템 보안[^p5], 엣지 컴퓨팅·엣지 AI[^p7], 다중 에이전트 시스템·분산 의사결정[^p7]
- 홈페이지: <https://cs.kaist.ac.kr/research/labView?sn=88&menu=64>

> 소프트웨어를 만드는 과정과 프로그램의 품질을 연구하며, 결함 예측·신뢰성 평가·코드 검토·취약점 분석과 엣지 컴퓨팅 서비스 추천 방법을 개발하는 연구실이다.

## 무엇을 연구하나

SPIRAL은 소프트웨어공학(프로그램을 체계적으로 개발·운영·유지하는 방법을 다루는 분야)을 연구한다. 중심 관심은 개발 공정과 소프트웨어 품질을 유지하고 개선하는 것이다. 학과 연구실 소개는 프로그램이 믿을 만하게 동작하는지 확인하고, 개발 과정을 모형으로 나타내며, 결점을 예측하고 시스템의 모형을 검증하는 일을 주요 연구 분야로 든다.[^lab]

소프트웨어 신뢰성(정해진 조건과 기간에 프로그램이 고장 없이 동작할 가능성)을 다루는 연구에서는 개발·시험 중 발견되는 결함의 흐름을 살핀다. 개발 공정의 모델링(과정의 요소와 관계를 모형으로 나타내는 일)과 시뮬레이션(모형을 실행해 변화 과정을 살피는 일), 모델 검증(시스템의 모형이 정해진 성질을 만족하는지 확인하는 일)도 연구 범위에 들어간다. 백종문 교수는 소프트웨어 개발의 경제성과 품질 개선 방법에도 관심을 두고 있다.[^lab][^prof]

최근 논문에서는 자료가 부족할 때 프로그램의 신뢰성을 예측하는 방법, 코드가 바뀌는 시점의 결함 가능성을 판단하는 방법을 다룬다. 소프트웨어 결함(요구한 동작에서 벗어나게 할 수 있는 프로그램의 결점)을 예측하는 일과, 실제 실패를 일으킨 결함의 위치를 찾는 일은 구분된다. 연구진은 결함 자료를 구성하고 예측 모델을 평가하는 한편, 프로젝트(개발 과제를 수행하는 단위)의 지식을 활용해 결함 위치를 찾는 방법도 제안한다.[^p1][^p2][^p3]

코드 검토(프로그램의 변경 내용을 살펴 품질을 확인하는 활동)와 취약점(보안 침해에 악용될 수 있는 프로그램의 약점) 분석도 최근 연구에 포함된다. 과거 검토 사례를 찾아 언어 모델(언어 자료의 규칙을 학습해 언어를 처리하거나 생성하는 모형)의 검토 의견 생성에 제공하거나, 코드에서 바뀔 가능성이 있는 줄을 먼저 찾아 취약점 분석에 활용하는 방식이다.[^p4][^p5]

엣지 컴퓨팅(자료가 생기는 기기나 그 가까운 장치에서 계산하는 방식)과 클라우드(네트워크로 연결된 원격 컴퓨팅 자원을 필요에 따라 쓰는 방식)를 함께 사용하는 서비스도 다룬다. 사용자의 이동을 예측하고 비어 있는 서비스 성능 정보를 보완하며, 이 정보를 바탕으로 서버를 추천하는 구조를 제안한다.[^p7]

## 주요 연구 주제

### 코드 변경의 결함 예측과 모델 평가

변경 시점 결함 예측(JIT-SDP, Just-in-Time Software Defect Prediction: 코드가 바뀌는 시점에 해당 변경의 결함 가능성을 예측하는 방법)을 연구한다. ReDef는 변경을 되돌린 기록과 이후의 수정 이력을 활용해 결함 여부를 표시한 자료를 구성한다. 코드 언어 모델(프로그램 코드를 이해하거나 생성하도록 학습한 언어 모델)에 변경 정보를 제시하는 방식과, 모델이 변경의 의미를 이해하는지도 평가한다.[^p1]

PROPER-SDP는 프로젝트가 변화해 온 정보를 프롬프트(언어 모델에 제공하는 요청과 입력 정보)에 직접 넣어 변경 시점의 결함을 예측한다. 프로젝트별 학습 자료가 없는 상황에서도 변화 이력이 제공하는 맥락을 활용하는 방법이다.[^p6]

### 자료가 부족한 상황의 신뢰성 예측

신뢰성 성장 모델(SRGM, Software Reliability Growth Model)을 통해 시험·운영 중의 결함 발견 기록으로 소프트웨어 신뢰성의 변화를 예측한다. DSC-SRGM은 기존 모형으로 합성 자료(실제 관측값을 그대로 모은 것이 아니라 계산이나 생성 과정으로 만든 자료)를 만들고, 대상 프로젝트와 유사한 흐름을 골라 예측에 사용한다. 합성 자료를 과도하게 사용하거나 실제 자료와 단순히 섞으면 예측 성능이 낮아질 수 있다는 한계도 제시한다.[^p2]

### 코드 검토·결함 위치 찾기·취약점 분석

대형 언어 모델(LLM, Large Language Model: 많은 언어 자료로 학습해 글을 이해하고 생성하는 인공지능 모델)에 프로젝트의 목적·구조·과거 문제 해결 기록을 제공하는 방법을 연구한다. MemFL은 프로젝트 요약과 이전 디버깅(프로그램의 결함을 찾아 고치는 활동)에서 얻은 단서를 외부 기억으로 유지해 결함 위치를 찾는다. 검토 의견 생성 연구는 검색 증강 생성(RAG, Retrieval-Augmented Generation: 검색한 자료를 생성 모델의 입력에 더해 출력을 만드는 방법)으로 과거 코드와 검토 의견을 활용한다.[^p3][^p4]

변이 기반 결함 위치 찾기(MBFL, Mutation-Based Fault Localization)도 연구한다. HOTFUZ는 시험용 프로그램의 변경들을 고차 변이로 결합해 실행할 변이의 수와 결함 위치 분석의 비용을 줄이는 방법이다. 결함 위치 판단의 정확도 저하를 억제하면서 분석 비용을 다루는 데 목적을 둔다.[^p8]

LOSVER는 앞으로 수정될 가능성이 있는 코드 줄을 찾고 그 줄에 중요도를 부여해 취약점의 존재와 유형을 판단한다. 사전 학습 모델(해당 과제에 맞춰 학습하기 전에 다른 자료로 미리 학습한 모델)이 코드의 어느 부분에 주목해야 하는지를 안내하는 접근이다.[^p5]

### 엣지 컴퓨팅의 서비스 추천

서비스 품질(QoS, Quality of Service)을 고려해 이동 중인 사용자에게 서버를 추천하는 방법을 연구한다. 사용자 이동을 예측하는 계층, 언어 모델로 의사결정을 수행하는 엣지 계층, 여러 자료를 결합해 비어 있는 품질 정보를 채우는 클라우드 계층으로 역할을 나눈다. 이 다중 에이전트 시스템은 사용자의 이동과 부족한 품질 정보를 함께 고려해 서버 추천을 수행하도록 설계됐다.[^p7]

## 대표 논문

연구 갈래와 최근 연구를 함께 보여 주도록 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다. arXiv 항목은 사전 공개본이다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [ReDef: Do Code Language Models Truly Understand Code Changes for Just-in-Time Software Defect Prediction?](https://doi.org/10.1145/3808179) · FSE 2026[^p1] | 변경을 되돌린 기록을 바탕으로 결함 예측 자료를 만들고 코드 언어 모델을 평가했다. 코드 변경 정보를 왜곡해도 예측 성능이 거의 유지되는 결과를 통해, 모델이 변경의 의미보다 표면적인 단서에 의존하는 한계를 보였다. |
| 2 | 2026 | [DSC‐SRGM: A Deep Synthetic Cross‐Project Software Reliability Growth Model](https://doi.org/10.1002/stvr.70028) · Software Testing, Verification and Reliability[^p2] | 실제 결함 자료가 부족한 상황에서 기존 신뢰성 모형으로 합성 자료를 만들고 유사한 흐름을 골라 예측에 활용했다. 합성 자료를 과도하게 쓰거나 실제 자료와 단순히 섞으면 예측 성능이 낮아질 수 있다는 한계도 제시했다. |
| 3 | 2025 | [Improving LLM-Based Fault Localization with External Memory and Project Context](https://arxiv.org/html/2506.03585v1) · arXiv 사전 공개본[^p3] | 프로그램 구조의 요약과 이전 디버깅에서 얻은 단서를 별도의 기억에 담아 언어 모델에 제공하는 MemFL을 제안했다. 프로젝트 지식을 이용해 결함 위치를 찾고, 반복 시도에서 얻은 단서를 기억에 반영한다. |
| 4 | 2025 | [Retrieval-Augmented Code Review Comment Generation](https://doi.org/10.48550/arXiv.2506.11591) · arXiv 사전 공개본[^p4] | 검토할 코드와 비슷한 과거 사례를 검색해 언어 모델에 함께 제공하고 검토 의견을 생성했다. 과거 사례 검색과 문장 생성을 결합해 검토 의견과 사용 빈도가 낮은 표현의 생성을 평가했다. |
| 5 | 2025 | [LOSVER: Line-Level Modifiability Signal-Guided Vulnerability Detection and Classification](https://conf.researchr.org/details/ase-2025/ase-2025-papers/39/LOSVER-Line-Level-Modifiability-Signal-Guided-Vulnerability-Detection-and-Classifica) · ASE 2025[^p5] | 앞으로 바뀔 가능성이 있는 코드 줄을 찾아 중요도를 부여하는 방법을 제안했다. 이 정보를 활용해 프로그램의 취약점을 탐지하고 유형을 분류했다. |
| 6 | 2026 | [Project Evolution-aware Prompting of LLMs for Just-in-time Defect Prediction in Edge-cloud Systems](https://doi.org/10.13052/jwe1540-9589.2535) · Journal of Web Engineering[^p6] | 프로젝트가 변화해 온 정보를 언어 모델의 입력에 직접 넣어 코드 변경의 결함을 예측하는 PROPER-SDP를 제안했다. 프로젝트별 학습 자료가 없는 초기 상황에서도 변화 이력의 맥락을 활용하도록 설계했다. |
| 7 | 2026 | [LLM-driven Multi-agent Architecture for QoS-aware Server Recommendation in Mobile-Edge-Cloud Environments](https://doi.org/10.13052/jwe1540-9589.2533) · Journal of Web Engineering[^p7] | 사용자의 이동을 예측하고, 엣지 계층의 언어 모델로 판단하며, 클라우드에서 비어 있는 서비스 품질 정보를 채우는 서버 추천 구조를 제안했다. 사용자 이동과 부족한 품질 정보를 함께 고려하는 서비스 추천을 다룬다. |
| 8 | 2021 | [HOTFUZ: Cost‐effective higher‐order mutation‐based fault localization](https://doi.org/10.1002/stvr.1802) · Software Testing, Verification and Reliability[^p8] | 프로그램의 여러 변경을 결합한 고차 변이로 결함 위치 분석의 실행 비용을 다뤘다. 실행할 변이 수를 줄이면서 결함 위치 판단의 정확도 저하를 억제하는 방법을 제안했다. |

## 교수와 전문 분야

백종문은 KAIST 전산학부 교수이며 전공은 소프트웨어공학이다. 서던캘리포니아 대학교에서 전산학 박사 학위를 받았고, 2001년 1월부터 2005년 5월까지 모토로라 연구실에서 소프트웨어 품질 개선 연구를 이끌었다. 학과 소개는 현재 관심 분야로 소프트웨어 프로세스 모델링, 소프트웨어 이코노믹스(소프트웨어 개발의 비용과 경제적 가치를 다루는 분야), 소프트웨어 신뢰성 공학, 소프트웨어 식스 시그마(자료 분석으로 공정의 변동과 결함을 줄이는 품질 개선 방법)를 든다.[^prof][^faculty]

KAIST-삼성SDI 배터리 인재양성 프로그램의 참여교수로도 소개되며, 해당 소개의 본래 소속은 전산학부다.[^ksbp]

최근 논문을 함께 보면 전문 분야는 소프트웨어의 결함과 신뢰성을 예측·평가하고, 언어 모델을 이용해 개발 과정의 품질 확인을 지원하는 방법으로 이어진다. ReDef의 코드 변경 평가, DSC-SRGM의 신뢰성 예측, MemFL과 HOTFUZ의 결함 위치 찾기, LOSVER의 취약점 분석이 그 사례다. 엣지 컴퓨팅 환경의 서비스 추천과 결함 예측도 연구한다.[^p1][^p2][^p3][^p5][^p6][^p7][^p8]

## 응용 분야

프로그램 변경의 결함 위험 판단, 시험·운영 중 신뢰성 예측, 코드 검토 의견 생성, 결함 위치 파악, 소프트웨어 취약점 탐지와 분류에 적용하는 방법을 연구한다. 사용자 이동과 서비스 품질을 고려한 엣지 컴퓨팅 서버 추천도 다룬다.[^p1][^p2][^p3][^p4][^p5][^p7]

## 최근 5년 논문 목록

소프트웨어 신뢰성 예측, 코드 변경의 결함 예측, 코드 검토·취약점 분석과 엣지 컴퓨팅 서비스를 다룬다. OpenAlex의 KAIST 소속 공개 서지 목록을 기준으로, 기존의 학회 발표 페이지와 arXiv 자료를 함께 반영한 2021–2026년 목록이다. 연도·제목·저자·발표처는 각 서지가 적은 표기를 따른다. arXiv 항목은 사전 공개본이며, ReDef는 FSE 2026에 발표한 판으로 적었다.[^bibliography][^p1][^p4]

**2026**

- Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "DSC‐SRGM: A Deep Synthetic Cross‐Project Software Reliability Growth Model". *Software Testing, Verification and Reliability*.
- Inseok Yeo, Sungu Lee, Duksan Ryu, Jongmoon Baik. "PROPER-SDP: PROmpt-Based Project Evolution-awaRe Software Defect Prediction for Edge-Cloud Systems". *Communications in Computer and Information Science*.
- Doha Nam, Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "ReDef: Do Code Language Models Truly Understand Code Changes for Just-in-Time Software Defect Prediction?". *Proceedings of the ACM on Software Engineering*.
- Inseok Yeo, Sungu Lee, Duksan Ryu, Jongmoon Baik. "Project Evolution-aware Prompting of LLMs for Just-in-time Defect Prediction in Edge-cloud Systems". *Journal of Web Engineering*.
- Eunjeong Ju, Jeonghwa Lee, Duksan Ryu, Jongmoon Baik. "LLM-Driven Multi-agent Recommendation for QoS-Aware Edge Server Selection in Mobile Environments". *Communications in Computer and Information Science*.
- Jeonghwa Lee, Eunjeong Ju, Duksan Ryu, Suntae Kim, Jongmoon Baik. "Spatio-temporal Mamba for User Mobility Prediction in Mobile Edge Computing". *Journal of Web Engineering*.
- Eunjeong Ju, Junghwa Lee, Duksan Ryu, Suntae Kim, Jongmoon Baik. "LLM-driven Multi-agent Architecture for QoS-aware Server Recommendation in Mobile-Edge-Cloud Environments". *Journal of Web Engineering*.

**2025**

- Doha Nam, Jongmoon Baik. "LOSVER: Line-Level Modifiability Signal-Guided Vulnerability Detection and Classification". *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*.
- Hyunsun Hong, Sungu Lee, Duksan Ryu, Jongmoon Baik. "Enhancing Software Defect Prediction in Ansible Scripts Using Code-Smell-Guided Prompting with Large Language Models in Edge-Cloud Infrastructures". *Communications in Computer and Information Science*.
- Hyunsun Hong, Sungu Lee, Duksan Ryu, Jongmoon Baik. "Code Smell-guided Prompting for LLM-based Defect Prediction in Ansible Scripts". *Journal of Web Engineering*.
- Yeo, Inseok, Ryu, Duksan, Baik, Jongmoon. "Improving LLM-Based Fault Localization with External Memory and Project Context". *arXiv (Cornell University) (사전 공개본)*.
- Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "Deep Synthetic Cross-Project Approaches for Software Reliability Growth Modeling". *arXiv:2509.16939v1 (사전 공개본)*.
- Hyunsun Hong, Jongmoon Baik. "Retrieval-Augmented Code Review Comment Generation". *arXiv:2506.11591v1 (사전 공개본)*.

**2024**

- Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "Automated Machine Learning for Enhanced Software Reliability Growth Modeling: A Comparative Analysis with Traditional SRGMs". *2024 IEEE 24th International Conference on Software Quality, Reliability and Security (QRS)*.
- Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "Enhancing Software Reliability Growth Modeling: A Comprehensive Analysis of Historical Datasets and Optimal Model Selections". *2024 IEEE 24th International Conference on Software Quality, Reliability and Security (QRS)*.
- Sunjae Kwon, Sungu Lee, Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "Exploring the Feasibility of ChatGPT for Improving the Quality of Ansible Scripts in Edge-Cloud Infrastructures Through Code Recommendation". *Communications in Computer and Information Science*.

**2023**

- Sunjae Kwon, Duksan Ryu, Jongmoon Baik. "An effective approach to improve the performance of eCPDP (early cross-project defect prediction) via data-transformation and parameter optimization". *Software Quality Journal*.
- Sunjae Kwon, Sungu Lee, Duksan Ryu, Jongmoon Baik. "Pre-trained Model-based Software Defect Prediction for Edge-cloud Systems". *Journal of Web Engineering*.
- Jiwon Choi, Saranya Manikandan, Duksan Ryu, Jongmoon Baik. "An Empirical Analysis on Just-In-Time Defect Prediction Models for Self-driving Software Systems". *Communications in Computer and Information Science*.
- Sunjae Kwon, Sungu Lee, Taehyoun Kim, Duksan Ryu, Jongmoon Baik. "Exploring LLM-based Automated Repairing of Ansible Script in Edge-Cloud Infrastructures". *Journal of Web Engineering*.
- Jiwon Choi, Taeyoung Kim, Duksan Ryu, Jongmoon Baik, Suntae Kim. "Just-in-Time Defect Prediction for Self-driving Software via a Deep Learning Model". *Journal of Web Engineering*.
- Sunjae Kwon, Jong-In Jang, Sungu Lee, Duksan Ryu, Jongmoon Baik. "CodeBERT Based Software Defect Prediction for Edge-Cloud Systems". *Communications in Computer and Information Science*.

**2021**

- Eunseob Kim, Jongmoon Baik, Duksan Ryu. "Heterogeneous Defect Prediction through Correlation-Based Selection of Multiple Source Projects and Ensemble Learning". *2021 IEEE 21st International Conference on Software Quality, Reliability and Security (QRS)*.
- Sunjae Kwon, Duksan Ryu, Jongmoon Baik. "eCPDP: Early Cross-Project Defect Prediction". *2021 IEEE 21st International Conference on Software Quality, Reliability and Security (QRS)*.
- Jong‐In Jang, Duksan Ryu, Jongmoon Baik. "HOTFUZ: Cost‐effective higher‐order mutation‐based fault localization". *Software Testing, Verification and Reliability*.
- Jonggu Kang, Sunjae Kwon, Duksan Ryu, Jongmoon Baik. "HASPO: Harmony Search-Based Parameter Optimization for Just-in-Time Software Defect Prediction in Maritime Software". *Applied Sciences*.
- Jiwon Choi, Jaewook Lee, Duksan Ryu, Suntae Kim, Jongmoon Baik. "GAIN-QoS: A Novel QoS Prediction Model for Edge Computing". *Journal of Web Engineering*.
- Nakwon Lee, Yunho Kim, Moonzoo Kim, Duksan Ryu, Jongmoon Baik. "Directed Model Checking for Fast Abstract Reachability Analysis". *IEEE Access*.

## 연락과 위치

- 위치: KAIST N1 502호[^lab][^faculty]
- 전화: 042-350-3556[^lab]

## 각주
[^lab]: KAIST 전산학부, 「소프트웨어 프로세스 개선 및 신뢰성 검증 연구실」. <https://cs.kaist.ac.kr/research/labView?sn=88&menu=64> (관측일 2026-10-30).
[^prof]: KAIST 전산학부, 「백종문」 교수 소개. <https://cs.kaist.ac.kr/people/view?idx=371&kind=faculty&menu=160> (관측일 2026-10-30).
[^faculty]: KAIST 전산학부, 「교수진」 백종문 항목. <https://cs.kaist.ac.kr/people/faculty> (관측일 2026-10-30).
[^ksbp]: KAIST-삼성SDI 배터리 인재양성 프로그램, 「백종문」 참여교수 소개. <https://ksbp.kaist.ac.kr/s0401/view/id/52> (관측일 2026-10-30).
[^bibliography]: OpenAlex, Jongmoon Baik 저자 이름·KAIST 소속·2021-01-01 이후 출판 조건의 공개 서지 목록. <https://api.openalex.org/works?filter=raw_author_name.search:Jongmoon%20Baik,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> (관측일 2026-10-30).
[^p1]: D. Nam, T. Kim, D. Ryu, J. Baik, FSE 2026 Research Papers (2026). <https://doi.org/10.1145/3808179> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/143/ReDef-Do-Code-Language-Models-Truly-Understand-Code-Changes-for-Just-in-Time-Softwar> (관측일 2026-10-30).
[^p2]: T. Kim, D. Ryu, J. Baik, Software Testing, Verification and Reliability (온라인 2026-08-17). <https://doi.org/10.1002/stvr.70028> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?filter=raw_author_name.search:Jongmoon%20Baik,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> (관측일 2026-10-30).
[^p3]: I. Yeo, D. Ryu, J. Baik, arXiv:2506.03585v1 (사전 공개본) (온라인 2025-06-04). <https://doi.org/10.48550/arxiv.2506.03585> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/html/2506.03585v1> (관측일 2026-10-30).
[^p4]: H. Hong, J. Baik, arXiv:2506.11591v1 (사전 공개본) (온라인 2025-06-13). <https://doi.org/10.48550/arXiv.2506.11591> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2506.11591> (관측일 2026-10-30).
[^p5]: D. Nam, J. Baik, ASE 2025 Research Papers (2025). <https://doi.org/10.1109/ase63991.2025.00092> 초록 기준(학회 아카이브 게시 초록). 초록 원문 <https://conf.researchr.org/details/ase-2025/ase-2025-papers/39/LOSVER-Line-Level-Modifiability-Signal-Guided-Vulnerability-Detection-and-Classifica> (관측일 2026-10-30).
[^p6]: I. Yeo, S. Lee, D. Ryu, J. Baik, Journal of Web Engineering (온라인 2026-04-19). <https://doi.org/10.13052/jwe1540-9589.2535> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.13052/jwe1540-9589.2535> (관측일 2026-10-30).
[^p7]: E. Ju 외, J. Baik, Journal of Web Engineering (온라인 2026-04-19). <https://doi.org/10.13052/jwe1540-9589.2533> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.13052/jwe1540-9589.2533> (관측일 2026-10-30).
[^p8]: J.-I. Jang, D. Ryu, J. Baik, Software Testing, Verification and Reliability (온라인 2021-12-13). <https://doi.org/10.1002/stvr.1802> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?filter=raw_author_name.search:Jongmoon%20Baik,institutions.ror:https://ror.org/05apxxy63,from_publication_date:2021-01-01&per-page=200&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index> (관측일 2026-10-30).

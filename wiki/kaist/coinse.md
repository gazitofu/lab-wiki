# 계산지능형 소프트웨어 공학 연구실 (Computational Intelligence for Software Engineering Lab, COINSE)

**KAIST 전산학부 · 유신 교수, 석좌교수(Endowed Chair Professor)**

- 대분야: 컴퓨팅·AI
- 태그: 프로그램 분석·검증[^dept][^p6], 대형 언어 모델[^p1][^p2][^p4], AI 시스템·인프라[^p1]
- 홈페이지: <https://coinse.github.io>

> 인공지능으로 소프트웨어의 오류를 찾아 설명하고 고치는 방법과, 인공지능을 품은 소프트웨어 자체를 시험하는 방법을 함께 연구한다.

## 무엇을 연구하나

COINSE는 소프트웨어공학(소프트웨어를 개발·시험·유지하는 방법을 다루는 분야)과 인공지능이 만나는 문제를 연구한다. 테스트(입력과 실행 결과로 원하는 동작을 확인하는 시험)를 자동으로 만들고, 오류 원인을 찾는 디버깅(프로그램 오류의 원인을 찾아 수정하는 작업)을 돕는다. 사람이 쓴 프로그램뿐 아니라 자료에서 규칙을 배우는 기계학습 모델의 품질도 연구 대상이다.[^home][^dept]

오류를 찾을 때는 위치와 이유를 함께 제시하려 한다. AutoFL은 대형 언어 모델(LLM, Large Language Model; 많은 글을 학습해 글을 이해하고 생성하는 인공지능 모델)이 저장소를 탐색하면서 결함 위치와 설명을 내놓게 한다. AutoSD는 오류 원인에 대한 가설을 세우고, 프로그램 실행을 살펴 그 가설을 확인한 뒤 수정안을 만든다. 두 연구는 개발자가 자동 도구의 결론을 판단할 때 필요한 설명을 다룬다.[^p4][^p3]

모바일 앱의 화면 시험에서는 사람이 사용하는 목적을 시험 목표로 삼는다. DROIDAGENT는 에이전트(목표에 따라 행동을 선택하고 도구를 사용하는 소프트웨어)가 앱에서 수행할 일을 정하고 직접 화면과 상호작용하게 한다. 버튼이나 화면을 방문했는지에 더해, 앱 기능에 맞는 실제 사용 과정을 수행하는지가 연구의 관심사다.[^p5]

기계학습 모델을 시험할 입력과, 언어 모델의 계산을 이어 갈지를 고르는 방법도 연구한다. Surprise Adequacy는 새 입력에서 나타나는 신경망(연결된 계산 단위의 값을 조절해 입력과 출력의 관계를 배우는 모델)의 반응이 학습 자료에서의 반응과 얼마나 다른지 살핀다. Clotho는 답을 생성하기 전에 입력의 실패 가능성을 평가하고, Atropos는 진행 중인 에이전트 추론(학습된 모델로 입력에 대한 결과를 계산하는 과정)의 성공 여부를 예측해 중단하거나 다른 모델로 이어 간다.[^p7][^p2][^p1]

## 주요 연구 주제

### 1. 프로그램의 관계 분석과 설명 가능한 자동 수정

프로그램의 어느 부분이 다른 부분에 영향을 주는지 알아야 오류 원인을 좁힐 수 있다. CPDA(Causal Program Dependence Analysis, 인과적 프로그램 의존 분석)는 실행 중 값에 개입하고 그 변화를 관찰해 코드 부분 사이 영향의 강도를 추정한다. 여기서 인과 추론은 어떤 요인을 바꾸었을 때 다른 요인이 어떻게 달라지는지 분석하는 방법이다. 연구는 이 의존 관계를 프로그램의 기능별 묶음과 특정 코드 부분의 맥락을 이해하는 데 활용한다.[^p6]

AutoFL은 소스 코드(프로그램의 명령과 구조를 적은 글)를 한꺼번에 모두 읽히는 대신, 언어 모델이 함수를 호출해 저장소를 탐색하게 한다. 결과는 의심되는 결함 위치와 그 이유다. AutoSD는 가설을 세우고 실행 결과로 판단하는 과정을 수정안의 설명으로 연결한다. AutoSD의 사용자 연구에서는 설명을 받은 참여자들이 연구 대상 실제 오류 여섯 건 중 다섯 건에서 수정안의 올바름을 더 정확하게 판단했다.[^p4][^p3]

### 2. 앱 사용 목표를 세우는 화면 시험

DROIDAGENT는 GUI(Graphical User Interface, 그림·버튼·입력창으로 소프트웨어를 조작하는 화면)의 시험 목표를 스스로 세우고 그 목표를 달성하려 한다. 언어 모델과 과거 정보를 유지하는 장·단기 메모리(정보를 저장해 사용하는 기능)를 함께 쓴다. 논문 초록은 메시지 앱에서 계정을 만들고 친구로 추가하는 사용 과정을 사람의 개입 없이 시험한 사례를 든다.[^p5]

### 3. 인공지능 시험 입력의 선택과 추론 비용 관리

Surprise Adequacy(SA, 입력에 대한 모델 반응이 학습 때의 반응과 다른 정도를 재는 시험 적합도)는 신경망 내부 반응을 이용해 시험 입력을 평가한다. 논문은 이 값으로 모델 동작의 정확성을 예측하고, 모델이 틀리도록 만든 적대적 입력을 탐지하는 쓰임을 평가했다. Clotho는 특정 작업의 입력 가운데 사람이 정답을 붙일 대상을 골라 기준 자료를 만들고, 모델 내부 상태로 아직 보지 않은 입력의 실패 가능성에 순서를 매긴다. 출력 생성 전 점수를 계산하며, 공개 모델에서 얻은 점수를 비공개 모델의 시험 입력 선택에 적용한 결과도 제시한다.[^p7][^p2]

Atropos는 자기 일관성(self-consistency, 같은 문제를 여러 번 풀고 결과를 모아 최종 답을 고르는 방법)을 사용하는 에이전트의 추론 경로를 그래프(대상과 관계를 점과 선으로 나타낸 구조)로 합친다. 이 구조에서 최종 실패를 예측하고, 실패할 것으로 예측한 추론을 중단하거나 진행 중인 맥락을 다른 언어 모델로 옮긴다. 이처럼 계산을 언제 멈추고 어떤 모델에서 계속할지 정해, 에이전트의 성과와 추론 비용 사이의 관계를 개선하려는 연구다.[^p1]

## 대표 논문

유신 교수가 KAIST 재직 중 저자로 참여한 2023–2026년 논문 7편을 연구 갈래별로 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Atropos: Improving Cost-Benefit Trade-off of LLM-Based Agents under Self-Consistency with Early Termination and Model Hotswap](https://doi.org/10.1145/3832156)[^p1] | 진행 중인 에이전트 추론이 실패할지를 예측한다. 실패가 예상되면 계산을 멈추거나 그때까지의 맥락을 다른 언어 모델로 옮겨, 성과와 비용의 균형을 조절한다. |
| 2 | 2026 | [Clotho: Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs](https://doi.org/10.1145/3797114)[^p2] | 언어 모델이 답을 만들기 전에 내부 상태로 입력의 실패 가능성을 평가한다. 사람이 정답을 붙일 입력을 골라 기준 자료를 만들고, 새 입력의 시험 순서를 정한다. |
| 3 | 2025 | [Explainable Automated Debugging via Large Language Model-driven Scientific Debugging](https://doi.org/10.1007/s10664-024-10594-x)[^p3] | 언어 모델이 오류 원인의 가설을 세우고 프로그램 실행을 살펴 결론을 낸 뒤 수정안을 만든다. 수정안이 어떻게 나왔는지 설명해 개발자의 판단을 돕고자 한다. |
| 4 | 2024 | [A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization](https://doi.org/10.1145/3660771)[^p4] | 언어 모델이 함수 호출로 코드 저장소를 탐색하고 의심되는 오류 위치와 그 이유를 함께 알려 준다. 실제 오류 평가와 개발자 면담으로 결과를 살폈다. |
| 5 | 2024 | [Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents](https://doi.org/10.1109/ICST60714.2024.00020)[^p5] | 모바일 앱에서 시험할 목표를 세우고 직접 화면을 조작하는 에이전트를 만든다. 실제 앱 사용에 맞는 작업을 스스로 수행하는지를 평가했다. |
| 6 | 2024 | [Causal Program Dependence Analysis](https://doi.org/10.1016/j.scico.2024.103208)[^p6] | 프로그램 실행 중 값을 바꾸어 다른 코드 부분에 생기는 변화를 관찰한다. 부분 사이 영향의 강도를 추정해 프로그램 이해와 디버깅에 활용한다. |
| 7 | 2023 | [Evaluating Surprise Adequacy for Deep Learning System Testing](https://doi.org/10.1145/3546947)[^p7] | 새 입력에서 신경망이 보이는 반응을 학습 자료에서의 반응과 비교해 시험 입력의 가치를 잰다. 이 값을 동작 정확성 예측과 적대적 입력 탐지에 활용하는 방법을 평가했다. |

## 교수와 전문 분야

유신(Shin Yoo)은 KAIST 전산학부의 교수, 석좌교수(Endowed Chair Professor)다. 학과는 전문 분야를 소프트웨어공학·소프트웨어테스팅으로 소개한다. 연구실은 결함 위치 식별, 프로그램 자동 수정, 기계학습 모델의 검증을 연구 갈래로 설명한다.[^faculty][^dept]

2009년 King's College London에서 전산학 박사학위를 받았고, 2015년 8월 KAIST 조교수로 부임했다. 연구실의 교수 소개에는 2018년 2월 부교수, 2021년 3월 정년보장 부교수, 2025년 3월 교수로 이어지는 이력이 있다. 이전에는 University College London에서 Lecturer로 재직했다.[^faculty][^pi]

교수 소개에 게시된 학술 활동은 IEEE Transactions on Software Engineering의 Associate Editor, Empirical Software Engineering의 Editorial Board Member, ICST·ASE·SSBSE의 Steering Committee Member 등이다. 학회 운영 이력에는 ASE 2025 General Chair, ICSE 2024 Testing and Analysis Area Co-chair, SSBSE 2022 General Chair가 있다.[^pi]

## 응용 분야

연구는 개발자가 오류 위치와 수정안을 판단하는 자동 디버깅 도구, 모바일 앱의 화면 시험, 언어 모델을 이용한 소프트웨어의 시험 입력 선택과 에이전트 운영에 연결된다. 산업 협력 소식에는 SAP HANA의 시험 실패·충돌 원인 분석과 Samsung Research와의 화면 시험 수정 연구가 있다.[^p1][^p2][^p3][^p4][^p5][^news]

## 구성원

2026-10-27 연구실 Members 페이지에 게시된 재학생 7명(박사과정 3명, 석사과정 4명)이다. 「시작」은 개인 소개에 적힌 현재 학위과정의 전공·학교·시작 시기다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름을 확인한 사람에게 번호를 붙였으며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Juyeon Yoon | 박사과정 | Computer Science, KAIST Mar. 2022 - Present[^m1] | greenmon@kaist.ac.kr | 2, 5 |
| Somin Kim | 박사과정 | Computer Science, KAIST March 2025 - Present[^m2] | somin.kim@kaist.ac.kr | 2 |
| Naryeong Kim | 박사과정 | Computer Science, KAIST Sep 2026 - Present[^m3] | naryeong.kim@kaist.ac.kr | 1 |
| Jinsu Choi | 석사과정 | Computer Science, KAIST Mar 2025 - Present[^m4] | jinsuchoi@kaist.ac.kr |  |
| Jae Yong Lee | 석사과정 | Computer Science, KAIST Sep 2025 - Present[^m5] | jaeyonglee0205@kaist.ac.kr |  |
| Sihyun Ahn | 석사과정 | Computer Science, KAIST Mar 2026 - Present[^m6] | sihyun.ahn@kaist.ac.kr |  |
| Hongseok Park | 석사과정 | Information Security, KAIST Sep 2026 - Present[^m7] | hongseok.park@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Members 페이지 Alumni 17명 가운데 학위 연도가 2021–2026년인 13명이다. 학위·연도·진로는 랩 표기다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyunjoon Cho | MSc (2026) | a ML engineer at Mango Boost |
| Fathony Achmad | MSc (2025) |  |
| Louis Milliken | MSc (2025) | a ML research engineer at Perplexity AI |
| Doam Lee | MSc (2025) | a softrware engineer at LG CNS |
| Banseok Woo | MSc (2025) | a software engineer at Infobank |
| Hyeonseok Lee | MSc (2024) | a software engineer at SAP Labs Korea |
| Sungmin Kang | PhD (2024) | a postdoctoral researcher at NUS, Singapore |
| Gabin An | PhD (2024) | an assistant professor at Korea University, Korea |
| Saeyoon Oh | MSc (2024) | at Furiosa AI |
| Jinhan Kim | PhD (2023) | a postdoctoral researcher at University of Lugano, Switzerland |
| Seongmin Lee | PhD (2022) | a postdoctoral researcher at University of California Los Angeles, USA |
| Seungjun Chung | MSc (2022) | a TTS engineer at Krafton AI |
| Jeongju Sohn | PhD (2021) | an assistant professor at Kyoungpook National University, Korea |

## 최근 논문 목록 (2021–2026)

연구실 Publications 페이지의 2021–2026년 구역에 실린 학술지 16편과 학회·워크숍 44편, 합계 60편이다. 오류 위치 식별과 자동 수정, 프로그램 관계 분석, 화면 시험, 기계학습 모델과 언어 모델의 시험을 다룬다. 제목·저자·발표처는 연구실 표기이고, 연도는 누리집의 연도 구역이다. 연구실 소식에서 채택을 확인하고 연결 자료가 사전 공개본인 학회 항목은 채택과 판본을 표시했다. 권·쪽 정보 없이 학회명만 적힌 나머지 항목은 「연구실 게시 PDF 판」 또는 「누리집 기재」로 구분했다.[^pubs]

**2026**

- Felix Dobslaw, Robert Feldt, Juyeon Yoon and Shin Yoo. "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy". *ACM Transactions on Software Engineering and Methodology, 35(9)(261):1–24*.
- Naryeong Kim and Shin Yoo. "Atropos: Improving Cost-Benefit Trade-off of LLM-Based Agents under Self-Consistency with Early Termination and Model Hotswap". *Proceedings of the ACM on Software Engineering (PACMSE), 3(ISSTA065):1492–1512*.
- Juyeon Yoon, Somin Kim, Robert Feldt and Shin Yoo. "Clotho: Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs". *Proceedings of the ACM on Software Engineering (PACMSE), 3(FSE):1910–1932*.
- Hyunjoon Cho and Shin Yoo. "STARouter: Internal State based LLM Router for Software Testing Tasks". *Proceedings of the 19th IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), p9–16*.
- Sihyun Ahn, Juyeon Yoon, Taehyoung Kim, Eunki Song and Shin Yoo. "WanderVision: Scenario-Based GUI Testing for Smart TVs via Vision-Language Models". *Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), p57–64*.
- Jinhan Kim, Nargiz Humbatova, Gunel Jahangirova, Shin Yoo and Paolo Tonella. "Revisiting “Revisiting Neuron Coverage for DNN Testing: A Layer-Wise and Distribution-Aware Criterion”: A Critical Review and Implications on DNN Coverage Testing". *Proceedings of the 48th International Conference on Software Engineering (누리집 기재)*.
- Sungmin Kang, Sumi Yun, Jingun Hong, Shin Yoo and Gabin An. "Finding the Needle in the Crash Stack: Industrial-Scale Crash Root Cause Localization with AutoCrashFL". *Proceedings of the 44th International Conference on Software Engineering - Software Engineering in Practice (채택; 연결 자료: arXiv 사전 공개본, 2025)[^crash]*.

**2025**

- Nargiz Humbatova, Jinhan Kim, Gunel Jahangirova, Shin Yoo and Paolo Tonella. "An empirical study of fault localisation techniques for deep neural networks". *Empirical Software Engineering, 30(5):124*.
- Sungmin Kang, Bei Chen, Shin Yoo and Jian-Guang Lou. "Explainable Automated Debugging via Large Language Model-driven Scientific Debugging". *Journal of Empirical Software Engineering, 30(45):1–28*.
- Shin Yoo, Robert Feldt, Somin Kim and Naryeong Kim. "Capturing Semantic Flow of ML-based Systems". *Proceedings of the ACM International Conference on the Foundations of Software Engineering - Ideas, Visions and Reflections Track, p601–605*.
- Jaeyong Lee, Sungmin Kang and Shin Yoo. "Predictive Prompt Analysis". *Proceedings of the ACM International Conference on the Foundations of Software Engineering - Ideas, Visions and Reflections Track, p646–650*.
- Jeongki Son, Gabin An, Jingun Hong and Shin Yoo. "Evaluating Machine Learning-Based Test Case Prioritization in the Real World: An Experiment with SAP HANA". *Proceedings of the 18th IEEE International Conference on Software Testing, Verification & Validation, p522–532*.
- Juyeon Yoon, Seah Kim, Somin Kim, Sukchul Jung and Shin Yoo. "Integrating LLM-Based Text Generation with Dynamic Context Retrieval for GUI Testing". *Proceedings of the 18th IEEE International Conference on Software Testing, Verification & Validation, p394–405*.
- Juyeon Yoon, Robert Feldt and Shin Yoo. "Adaptive Testing for LLM-Based Applications: A Diversity-based Approach". *Proceedings of the 8th IEEE International Workshop on Next Level of Test Automation (연구실 게시 PDF 판)[^postedpdf]*.
- Somin Kim and Shin Yoo. "DANDI: Diffusion as Normative Distribution for Deep Neural Network Input". *Proceedings of the 6th International Workshop on Deep Learning for Testing and Testing for Deep Learning (연구실 게시 PDF 판)[^postedpdf]*.
- Hyeonseok Lee, Gabin An and Shin Yoo. "METAMON: Finding Inconsistencies between Program Documentation and Behavior using Metamorphic LLM Queries". *Proceedings of the Second International Workshop on Large Language Models for Code (연구실 게시 PDF 판)[^postedpdf]*.
- Hyunjoon Cho, Sungmin Kang, Gabin An and Shin Yoo. "COSMosFL: Ensemble of Small Language Models for Fault Localisation". *Proceedings of the Second International Workshop on Large Language Models for Code (연구실 게시 PDF 판)[^postedpdf]*.
- Louis Milliken, Sungmin Kang and Shin Yoo. "Beyond pip install: Evaluating LLM Agents for the Automated Installation of Python Projects". *Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (연구실 게시 PDF 판)[^postedpdf]*.
- Naryeong Kim, Sungmin Kang, Gabin An and Shin Yoo. "Lachesis: Predicting LLM Inference Accuracy using Structural Properties of Reasoning Paths". *Proceedings of the 6th International Workshop on Deep Learning for Testing and Testing for Deep Learning (연구실 게시 PDF 판)[^postedpdf]*.

**2024**

- Sungmin Kang, Robert Feldt and Shin Yoo. "Deceiving Humans and Machines Alike: Search-Based Test Input Generation for DNNs Using Variational Autoencoders". *ACM Transactions on Software Engineering Methodologies, 33(4):103:1–24*.
- Sungmin Kang, Gabin An and Shin Yoo. "A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization". *Proceedings of the ACM on Software Engineering, 1(FSE):1424–1446*.
- Seongmin Lee, Dave Binkley, Robert Feldt, Nicolas Gold and Shin Yoo. "Causal Program Dependence Analysis". *Science of Computer Programming, 103208*.
- Sungmin Kang, Juyeon Yoon, Nargiz Askarbekkyzy and Shin Yoo. "Evaluating Diverse Large Language Models for Automatic and General Bug Reproduction". *IEEE Transactions on Software Engineering, 50(10):2677–2694*.
- Jinsu Choi, Gabin An and Shin Yoo. "Iterative Refactoring of Real-World Open-Source Programs with Large Language Models". *Proceedings of the 16th International Symposium on Search-Based Software Engineering . Springer Nature. 49–55*.
- Jaeyong Lee, Sungmin Kang, Juyeon Yoon and Shin Yoo. "The GitHub Recent Bugs Dataset for Evaluating LLM-Based Debugging Applications". *Proceedings of the IEEE Conference on Software Testing, Verification and Validation - Tools and Demonstratin Track, p442–444*.
- Gabin An, Juyeon Yoon, Thomas Bach, Jingun Hong and Shin Yoo. "Just-in-Time Flaky Test Detection via Abstracted Failure Symptom Matching". *Proceedings of the 40th International Conference on Software Maintenance and Evolution (연구실 게시 PDF 판)[^postedpdf]*.
- Juyeon Yoon, Robert Feldt and Shin Yoo. "Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents". *Proceedings of the 16th IEEE International Conference on Software Testing, Verification and Validation, p129–139*.

**2023**

- Jinhan Kim, Gabin An, Robert Feldt and Shin Yoo. "Learning Test-Mutant Relationship for Accurate Fault Localisation". *Information and Software Technology, 162:107272*.
- Jinhan Kim, Robert Feldt and Shin Yoo. "Evaluating Surprise Adequacy for Deep Learning System Testing". *ACM Transactions on Software Engineering and Methodology, 32(2):42:1–29*.
- Jeongju Sohn, Sungmin Kang and Shin Yoo. "Arachne: Search Based Repair of Deep Neural Networks". *ACM Transactions on Software Engineering Methodology, 32(4):85:1–26*.
- A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, S. Yoo and J. M. Zhang. "Large Language Models for Software Engineering: Survey and Open Problems". *Proceedings of the 45th IEEE/ACM International Conference on Software Engineering: Future of Software Engineering, p31–53*.
- Jinhan Kim, Jongchan Park and Shin Yoo. "The Inversive Relationship Between Bugs and Patches: An Empirical Study". *Proceedings of the 18th International Workshop on Mutation Analysis, p314–323*.
- Sungmin Kang and Shin Yoo. "GLAD: Neural Predicate Synthesis to Repair Omission Faults". *2023 IEEE/ACM 45th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion), p320–321*.
- Robert Feldt, Sungmin Kang, Juyeon Yoon and Shin Yoo. "Towards Autonomous Testing Agents via Conversational Large Language Models". *Proceedings of the 38th IEEE/ACM International Conference on Automated Software Engineering (ASE), p1688–1693*.
- Gabin An, Minhyuk Kwon, Kyunghwa Choi, Jooyong Yi and Shin Yoo. "BUGSC++: A Highly Usable Real World Defect Benchmark for C/C++". *Proceedings of the 38th IEEE/ACM International Conference on Automated Software Engineering, p2034–2037*.
- Sungmin Kang, Wonkeun Choi and Shin Yoo. "A Bayesian Framework for Automated Debugging". *Proceedings of the 32nd International Symposium on Software Testing and Analysis, p880–891*.
- Sungmin Kang and Shin Yoo. "Towards Objective-Tailored Genetic Improvement Through Large Language Models". *Proceedings of the 12th International Workshop on Genetic Improvement, p19–20*.
- Jinhan Kim, Nargiz Humbatova, Gunel Jahangirova, Paolo Tonella and Shin Yoo. "Repairing DNN Architecture: Are We There Yet?". *Proceedings of the 16th IEEE International Conference on Software Testing, Verification and Validation, p234–245*.
- Sungmin Kang, Juyeon Yoon and Shin Yoo. "Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction". *Proceedings of the 45th IEEE/ACM International Conference on Software Engineering, p2312–2323*.
- Gabin An, Jingun Hong, Naryeong Kim and Shin Yoo. "Fonte: Finding Bug Inducing Commits from Failures". *Proceedings of the 45th IEEE/ACM International Conference on Software Engineering, p589–601*.

**2022**

- Jinhan Kim, Juyoung Jeon, Shin Hong and Shin Yoo. "Predictive Mutation Analysis via Natural Language Channel in Source Code". *ACM Transactions on Software Engineering and Methodology, 31(4):1–27*.
- Seungjun Chung and Shin Yoo. "Augmenting Equivalent Mutant Dataset Using Symbolic Execution". *Proceedings of the 2022 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW), p150–159*.
- Sungmin Kang and Shin Yoo. "Language Models Can Prioritize Patches for Practical Program Patching". *Proceedings of the 3rd International Workshop on Automated Program Repair, p8–15*.
- Gabin An and Shin Yoo. "FDG: A Precise Measurement of Fault Diagnosability Gain of Test Cases". *Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis, p14–26*.
- Gabin An, Juyeon Yoon, Jeongju Sohn, Jingun Hong, Dongwon Hwang and Shin Yoo. "Automatically Identifying Shared Root Causes of Test Breakages in SAP HANA". *Proceedings of the 44th IEEE/ACM International Conference on Software Engineering - Software Engineering In Practice Track, p65–74*.
- Juyeon Yoon, Seungjoon Chung, Kihyuck Shin, Jinhan Kim, Shin Hong and Shin Yoo. "Repairing Fragile GUI Test Cases Using Word and Layout Embedding". *Proceedings of the 15th IEEE International Conference on Software Testing, Verification and Validation, Industry Track, p291–301*.

**2021**

- Seongmin Lee, David Binkley, Robert Feldt, Nicolas Gold and Shin Yoo. "Observation-based approximate dependency modeling and its use for program slicing". *Journal of Systems and Software, 179:110988*.
- Jeongju Sohn and Shin Yoo. "Empirical Evaluation of Fault Localisation Using Code and Change Metrics". *IEEE Transactions on Software Engineering, 47(8):1605–1625*.
- K. Liu, D. Kim, T. F. Bissyande, S. Yoo and Y. Le Traon. "Mining Fix Patterns for FindBugs Violations". *IEEE Transactions on Software Engineering, 47(1):165–188*.
- Yu-Seung Ma, Shin Yoo and Taeho Kim. "Selecting Test Inputs for DNNs Using Differential Testing with Subspecialized Model Instances". *Proceedings of the 29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering, p1467–1470*.
- Juyeon Yoon and Shin Yoo. "Enhancing Lexical Representation of Test Coverage for Failure Clustering". *Proceedings of the 36th IEEE/ACM International Conference on Automated Software Engineering Workshops (NLP-SEA 2021), p232–238*.
- Gabin An, Juyeon Yoon and Shin Yoo. "Searching for multi-fault programs in Defects4J". *Proceedings of the 13th International Symposium on Search Based Software Engineering, p136–150*.
- Jinhan Kim, Gabin An, Robert Feldt and Shin Yoo. "Ahead of Time Mutation Based Fault Localisation using Statistical Inference". *Proceedings of the 32nd International Symposium on Software Reliability Engineering, p253–263*.
- Gabin An and Shin Yoo. "Reducing the search space of bug inducing commits using failure coverage". *Proceedings of the ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, p1459–1462*.
- Junghyun Lee, Chani Jung, Yoo Hwa Park, Dongmin Lee, Juyeon Yoon and Shin Yoo. "Preliminary Evaluation of SWAY in Permutation Decision Space via a Novel Euclidean Embedding". *Proceedings of the 13th International Symposium on Search Based Software Engineering, p26–40*.
- Saeyoon Oh, Seongmin Lee and Shin Yoo. "Effectively Sampling Higher Order Mutants Using Causal Effect". *Proceedings of the 16th International Workshop on Mutation Analysis, p19–24*.
- Seunghee Han, Jaeuk Kim, Geon Kim, Jaemin Cho, Jiin Kim and Shin Yoo. "Preliminary Evaluation of Path-aware Crossover Operators for Search-Based Test Data Generation for Autonomous Driving". *Proceedings of the 14th International Workshop on Search Based Software Testing, p44–47*.
- Seah Kim and Shin Yoo. "Multimodal Surprise Adequacy Analysis of Inputs for Natural Language Processing DNN Models". *Proceedings of the 2nd ACM/IEEE International Conference on Automated Software Testing, p80–89*.
- Jeongju Sohn, Gabin An, Jingun Hong, Dongwon Hwang and Shin Yoo. "Assisting Bug Report Assignment Using Automated Fault Localisation: An Industrial Case Study". *Proceedings of the 14th IEEE International Conference on Software Testing, Verification and Validation, p284–294*.
- Jeongju Sohn, Yasutaka Kamei, Shane McIntosh and Shin Yoo. "Leveraging Fault Localisation to Enhance Defect Prediction". *Proceedings of the 28th IEEE International Conference on Software Analysis, Evolution and Reengineering, p284–294*.

## 수상

아래 날짜는 수상 소식의 게시일이다. 2024년 ICST 수상은 유신 교수의 KAIST 부임 전 University College London 재직 시절 공동 연구한 논문에 대한 수상이다.[^award][^mip]

- 2024-10-10 · 「Just-in-Time Flaky Test Detection via Abstracted Failure Symptom Matching」이 ICSME 2024 Best Industry Paper Award를 수상했다.[^award]
- 2024-05-30 · 유신 교수가 University College London 재직 중 KAIST SWTV 그룹과 공동 연구한 2014년 논문 「Ask the Mutant: Mutating Faulty Programs for Fault Localization」이 ICST 2024에서 IEEE TCSE Most Influential Award를 수상했다.[^mip]

## 소식

2021-10-13–2026-10-13 사이 게시된 연구 소식 15건이다. 날짜는 게시일이며, 각 문장은 당시의 채택·게재 승인 공지 내용이다.[^news]

- 2026-04-21 · Atropos 논문이 ISSTA 2026에 채택됐다.
- 2025-12-22 · 언어 모델 입력의 작업별 시험 적합도를 다룬 Clotho 논문이 FSE 2026에 채택됐다.
- 2025-12-05 · SAP과 공동 연구한 대규모 충돌 원인 위치 식별 논문 AutoCrashFL이 ICSE SEIP 2026에 채택됐다.
- 2024-11-12 · 자동 과학적 디버깅 연구 AutoSD가 Empirical Software Engineering에 게재 승인됐다.
- 2024-09-03 · 실행 때마다 결과가 달라지는 시험을 탐지하는 논문이 ICSME 2024 발표 예정으로 공지됐다.
- 2024-04-24 · 언어 모델로 결함 위치와 그 이유를 함께 제시하는 AutoFL 논문이 FSE 2024에 채택됐다.
- 2023-12-29 · 언어 모델 기반 자율 에이전트의 모바일 화면 시험 논문이 ICST 2024에 채택됐다.
- 2023-05-03 · 자동 디버깅을 위한 베이지안 틀 논문이 ISSTA 2023에 채택됐다.
- 2022-12-14 · 실패 결과로 결함을 유발한 코드 변경을 찾는 Fonte 논문이 ICSE 2023에 채택됐다.
- 2022-12-12 · 언어 모델로 오류 보고에서 재현 시험을 생성하는 논문이 ICSE 2023에 채택됐다.
- 2022-06-12 · 시험이 결함 진단에 주는 정보 증가를 측정하는 FDG 논문이 ISSTA 2022에 채택됐다.
- 2022-03-12 · 동등 변이체 자료를 자동으로 늘리는 기법의 논문이 MUTATION 2022에 채택됐다.
- 2022-02-09 · SAP HANA 시험 실패의 공통 원인을 찾는 논문이 ICSE SEIP 2022에 채택됐다.
- 2022-01-12 · 소스 코드의 자연어 정보를 이용해 변이 분석 결과를 예측하는 논문이 ACM Transactions on Software Engineering and Methodology에 게재 승인됐다.
- 2021-12-28 · COINSE와 Samsung Research가 공동 연구한 화면 시험 수정 기법 논문이 ICST 2022 Industry Track에 채택됐다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 전산학부 E3-5 310호, 교수 연구실 E3-5 305호[^members][^dept]
- 교수 이메일: shin.yoo@kaist.ac.kr[^members]
- 교수 전화: +82 42 350 3567[^pi]
[^home]: COINSE 첫 화면의 연구 소개. <https://coinse.github.io> (2026-10-27 관측).
[^dept]: KAIST 전산학부 「계산지능형 소프트웨어 공학 연구실」 소개. <https://cs.kaist.ac.kr/research/labView?sn=96&menu=64> (2026-10-27 관측).
[^faculty]: KAIST 전산학부 교수 명단과 유신 교수 소개. 전문 분야·직급·학위·연구실. <https://cs.kaist.ac.kr/people/faculty> <https://cs.kaist.ac.kr/people/view?idx=516&kind=faculty&menu=160> (2026-10-27 관측).
[^pi]: 연구실 Shin Yoo 소개. Education and Employment, Academic Service, 연락처. <https://coinse.github.io/members/shin.yoo/> (2026-10-27 관측).
[^members]: COINSE Members의 재학생·Alumni·학교 이메일·사무실. <https://coinse.github.io/members> (2026-10-27 관측).
[^pubs]: COINSE Publications의 2021–2026년 Journals와 Conferences and Workshops. <https://coinse.github.io/publications> (2026-10-27 관측).
[^news]: COINSE News의 날짜·제목·연구 요약. <https://coinse.github.io/news> (2026-10-27 관측).
[^award]: COINSE 「ICSME 2024 Best Indistry Paper Award」, 2024-10-10 게시. 본문 수상명은 Best Industry Paper Award다. <https://coinse.github.io/2024/10/10/Best-Industry-Paper.html> (2026-10-27 관측).
[^mip]: COINSE 「ICST 2024 MBFL Paper about MUSE received Most Influential Paper Award at ICST 2024」, 2024-05-30 게시. 본문 수상명은 IEEE TCSE Most Influential Award다. <https://coinse.github.io/2024/05/30/ICST-2024-MIP.html> (2026-10-27 관측).
[^crash]: AutoCrashFL의 연구실 연결 PDF는 arXiv:2510.22530v1, 2025-10-26 사전 공개본이다. <https://coinse.github.io/publications/pdfs/Kang2026wb.pdf> 채택 공지는 COINSE News의 2025-12-05 항목이다. <https://coinse.github.io/news> (2026-10-27 관측).
[^postedpdf]: 연구실이 각 학회 항목에 연결한 동일 제목·저자 PDF의 초록과 첫머리. <https://coinse.github.io/publications/pdfs/Yoon2025aa.pdf> <https://coinse.github.io/publications/pdfs/Kim2025ab.pdf> <https://coinse.github.io/publications/pdfs/Lee2025aa.pdf> <https://coinse.github.io/publications/pdfs/Cho2025aa.pdf> <https://coinse.github.io/publications/pdfs/Milliken2025aa.pdf> <https://coinse.github.io/publications/pdfs/Kim2025aa.pdf> <https://coinse.github.io/publications/pdfs/An2024wm.pdf> (2026-10-27 관측).
[^m1]: COINSE juyeon 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/juyeon/> (2026-10-27 관측).
[^m2]: COINSE somin 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/somin/> (2026-10-27 관측).
[^m3]: COINSE naryeong 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/naryeong/> (2026-10-27 관측).
[^m4]: COINSE jinsu 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/jinsu/> (2026-10-27 관측).
[^m5]: COINSE jaeyong 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/jaeyong/> (2026-10-27 관측).
[^m6]: COINSE sihyun 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/sihyun/> (2026-10-27 관측).
[^m7]: COINSE hongseok 개인 소개의 Education, 현재 학위과정 시작 시기. <https://coinse.github.io/members/hongseok/> (2026-10-27 관측).
[^p1]: N. Kim, S. Yoo, Proceedings of the ACM on Software Engineering 3, Article ISSTA065, 21 pages (2026). <https://doi.org/10.1145/3832156> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Kim2026ab.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p2]: J. Yoon, S. Kim, R. Feldt, S. Yoo, Proceedings of the ACM on Software Engineering 3, Article FSE086, 23 pages (2026). <https://doi.org/10.1145/3797114> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Yoon2026cv.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p3]: S. Kang, B. Chen, S. Yoo, J.-G. Lou, Empirical Software Engineering 30, Article 45, 28 pages (2025). <https://doi.org/10.1007/s10664-024-10594-x> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Kang2025sn.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p4]: S. Kang, G. An, S. Yoo, Proceedings of the ACM on Software Engineering 1, Article 64, 23 pages (2024). <https://doi.org/10.1145/3660771> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Kang2024ay.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p5]: J. Yoon, R. Feldt, S. Yoo, Proceedings of the 16th IEEE International Conference on Software Testing, Verification and Validation, 129–139 (2024). <https://doi.org/10.1109/ICST60714.2024.00020> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Yoon2024aa.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p6]: S. Lee 외, S. Yoo, Science of Computer Programming, 103208 (2024). <https://doi.org/10.1016/j.scico.2024.103208> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Lee2024ab.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).
[^p7]: J. Kim, R. Feldt, S. Yoo, ACM Transactions on Software Engineering and Methodology 32, Article 42, 29 pages (2023). <https://doi.org/10.1145/3546947> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://coinse.github.io/publications/pdfs/Kim2022hg.pdf> (연구실이 올린 논문 PDF, 2026-10-27 관측).

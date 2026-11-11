# Edward Choi's Lab

**KAIST 김재철AI대학원 · 최윤재 부교수**

- 분야: 의료 기록·영상·생체신호를 위한 인공지능, 자연어 처리, 환자·사용자 대화 모사
- 대분야: 컴퓨팅·AI
- 태그: 의료 AI[^cx-project], 대형 언어 모델[^cx-project][^patient-project], 다중 에이전트 시스템·분산 의사결정[^hadmin-project], 자연어 처리·계산언어학[^transenv-project]
- 홈페이지: <https://mp2893.com/>
- 근거와 출처: [Edward Choi's Lab 근거 페이지](edlab-sources.md)

> 의료 기록·영상·생체신호를 함께 다루는 학습 방법을 만들고, 근거를 제시하는 진단 보조와 환자·사용자의 대화를 모사하는 인공지능 시스템을 연구한다.[^projects][^p1][^p2][^p3]

## 무엇을 연구하나

최윤재 부교수가 이끄는 연구실로, 의료 인공지능(Artificial Intelligence, AI), 자연어 처리(사람의 언어를 계산으로 분석·이해·생성하는 방법), 인물 역할을 수행하는 소프트웨어와 사용자 모사를 연구 관심으로 제시한다. 의료 기록의 형식 차이와 여러 종류의 입력을 함께 다루는 학습 방법을 개발한다.[^home][^gsai][^p1][^p2]

**의료 기록을 여러 기관과 과제에 걸쳐 학습하는 방법**이 한 갈래다. 전자의무기록(Electronic Health Records, EHR: 환자의 진료 정보를 전자 형태로 관리하는 기록)은 병원마다 코드와 자료 구조가 다르다. GenHPF(General Healthcare Predictive Framework)는 이 기록을 계층적인 글 형태로 바꾸어 여러 자료원과 예측 과제를 함께 학습한다. RawMed는 여러 표와 시간 순서가 있는 원래 기록의 구조를 반영하여 합성 의료 기록을 만드는 방법이다.[^p1][^p8]

**영상·보고서·생체신호를 연결하는 모형**도 개발한다. MedViLL(Medical Vision Language Learner)은 의료 영상과 보고서 사이에 정보를 참조하는 범위를 조절하는 새 학습 방법으로 영상 이해와 보고서 생성을 함께 다룬다. Auto-TTE는 임상 보고서를 조건으로 심전도(심장의 전기 활동을 시간에 따라 기록한 신호)를 생성한다. MD-ViSCo(Multi-Directional Vital-Sign Converter)는 심전도와 맥파(맥박에 따른 변화를 기록한 신호), 동맥혈압(혈액이 동맥 벽에 가하는 압력)의 파형(신호 값이 시간에 따라 변하는 모양)을 한 모형으로 변환한다.[^p2][^p3][^p4]

**언어 모형의 근거 확인과 대화 모사**가 또 다른 갈래다. 대형 언어 모델(Large Language Model, LLM: 많은 글을 학습해 글을 이해하고 생성하는 인공지능 모형)을 도구와 결합하여, 흉부 방사선영상의 측정값·위치·시각 표시를 근거로 답하는 CXReasonAgent를 개발한다.[^cx-project] H-AdminSim은 직원과 환자 에이전트(정보와 목표에 따라 판단하고 행동하는 소프트웨어)가 대화하며 접수와 일정 관리 등 병원 행정을 모사하는 다중 에이전트 시스템이다.[^hadmin-project] PatientSim은 실제 임상 자료와 환자의 성격·언어 능력·병력 회상·인지 혼란을 결합해 다양한 환자 대화를 모사한다.[^patient-project][^p7] Trans-EnV에서는 언어학 지식과 언어 모형을 결합해 평가 자료를 여러 영어 변종으로 바꾸고 언어 사용 차이에 따른 견고성(입력이나 조건이 바뀌어도 기능·성능을 유지하는 성질)을 평가하는 자연어 처리 방법을 개발한다.[^transenv-project]

의료 밖의 일반적인 추론·설명 방법도 다룬다. KG-GPT는 지식 그래프(개체와 개체 사이 관계를 연결해 나타낸 자료 구조)에서 필요한 정보를 찾아 언어 모형의 추론에 연결한다. SpectralX(Spectral eXplanation)는 시계열(시간 순서에 따라 기록한 자료) 분류 모형의 판단을 시간과 주파수(단위 시간에 반복되는 횟수) 양쪽에서 설명한다.[^p5][^p6]

## 주요 연구 주제

### 1. 서로 다른 의료 기록의 통합 학습과 생성

GenHPF는 의료 코드와 자료 구조가 다른 기록을 계층적 글 표현으로 다루어 여러 예측 문제에 적용하는 방법이다. RawMed는 미리 고른 몇 가지 검사값에 한정하지 않고 여러 표의 관계와 시간 변화를 담은 합성 기록을 생성한다.[^p1][^p8]

### 2. 의료 영상·생체신호의 이해와 생성

MedViLL은 영상과 보고서를 함께 학습하여 진단 분류, 관련 영상·보고서 검색, 영상 질문응답과 보고서 생성을 다룬다. Auto-TTE는 글에서 심전도를 생성하고, MD-ViSCo는 하나의 입력 파형에서 다른 종류의 파형을 생성하도록 모형을 통합한다.[^p2][^p3][^p4]

### 3. 근거를 찾아 추론하고 판단을 설명하는 방법

KG-GPT는 문장을 나누고, 관련 그래프 부분을 찾고, 그 근거로 결론을 내리는 세 단계를 연결한다. SpectralX는 시간과 주파수를 함께 표현한 자료의 일부를 바꾸어 분류 결과가 어떻게 달라지는지 살피며, 어떤 정보가 판단에 기여했는지 설명한다.[^p5][^p6]

### 4. 환자·사용자와의 대화를 모사하고 평가하는 시스템

PatientSim은 환자별 임상 정보와 행동 특성을 결합한 대화 환경을 제공한다. PICon은 인물 역할을 맡은 에이전트에 논리적으로 이어지는 질문을 여러 차례 던져 모순을 드러내는 평가 구조다. H-AdminSim은 환자·직원 사이 상호작용과 병원 행정 처리 흐름을 함께 모사한다.[^p7][^projects]

## 대표 논문

KAIST 재직 시기의 연구에서 의료 기록 학습, 영상·신호 생성, 지식 그래프 추론, 시계열 설명과 대화 모사를 고르게 골랐다. ‘쉽게 말하면’은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [GenHPF: General Healthcare Predictive Framework for Multi-Task Multi-Source Learning](https://doi.org/10.1109/jbhi.2023.3327951) · IEEE Journal of Biomedical and Health Informatics | 병원마다 의료 코드와 자료의 구조가 달라 모형을 함께 학습하기 어려운 문제를 다뤘다. 기록을 계층적 글 표현으로 바꿔 여러 예측 과제와 자료원에 적용하는 GenHPF를 제안했다. 공개 의료 기록 자료 세 종류의 여러 예측 과제에서, 여러 기관 자료를 합치거나 다른 자료로 학습한 지식을 옮기는 경우에 기존 방법보다 나은 결과를 보고했다.[^p1] | 1저자 Kyunghoon Hur, 마지막 저자 Edward Choi |
| 2 | 2022 | [Multi-Modal Understanding and Generation for Medical Images and Text via Vision-Language Pre-Training](https://doi.org/10.1109/jbhi.2022.3207502) · IEEE Journal of Biomedical and Health Informatics | 방사선영상과 보고서를 함께 이해하고 보고서를 생성하는 MedViLL을 제안했다. 영상과 글의 정보를 참조하는 범위를 조절하는 새 학습 방식을 결합했다. 진단 분류, 영상·보고서 검색, 의료 영상 질문응답, 보고서 생성에서 과제별로 설계한 모형을 포함한 기준 방법들과 비교하여 성능을 보였다.[^p2] | 1저자 Jong Hak Moon, 마지막 저자 Edward Choi |
| 3 | 2023 | [Text-to-ECG: 12-Lead Electrocardiogram Synthesis Conditioned on Clinical Text Reports](https://doi.org/10.1109/icassp49357.2023.10096898) · ICASSP | 임상 보고서의 글을 조건으로 12유도 심전도를 생성하는 Auto-TTE를 제안했다. 유도는 서로 다른 방향에서 본 심장의 전기 활동을 기록하는 방식이다. 앞서 생성한 내용을 이용하여 다음 내용을 순차적으로 만드는 생성 모형으로, 하나의 유도나 질병 분류에 한정된 기존 방식의 제약을 다뤘다. 수치 평가와 심장 전문의의 평가로 생성 신호의 사실성과 글의 의미에 맞는 정도를 살폈다.[^p3] | 1저자 Hyunseung Chung, 마지막 저자 Edward Choi |
| 4 | 2026 | [MD-ViSCo: A Unified Model for Multi-Directional Vital Sign Waveform Conversion](https://doi.org/10.1109/jbhi.2025.3639315) · IEEE Journal of Biomedical and Health Informatics | 입력과 출력 신호의 짝마다 별도 모형을 만들던 방식 대신, 한 모형으로 심전도·광용적맥파·동맥혈압 파형 사이 변환을 다뤘다. 광용적맥파는 빛을 이용해 혈액량 변화를 기록한 신호다. 공개 자료 두 종류에서 여러 방향의 변환을 평가하여 기준 방법보다 평균 오차와 상관관계 지표가 개선되었다고 보고했다. 생성한 심전도를 이용한 심방세동 분류에서도 기준 방법보다 나은 결과를 보였다.[^p4] | 1저자 Franck Meyer, 마지막 저자 Edward Choi |
| 5 | 2023 | [KG-GPT: A General Framework for Reasoning on Knowledge Graphs Using Large Language Models](https://doi.org/10.18653/v1/2023.findings-emnlp.631) · Findings of EMNLP | 자유롭게 쓰인 글과 구조화된 지식 그래프를 연결하는 KG-GPT를 제안했다. 문장 분할, 관련 그래프 검색, 논리적 추론을 차례로 수행하여 필요한 사실을 찾고 결론을 낸다. 지식 그래프 기반 사실 검증과 질문응답에서 평가했고, 여러 완전지도 학습 모형보다 좋은 결과도 보고했다. 완전지도 학습은 정답이 붙은 학습 자료를 이용하는 방식이다.[^p5] | 1저자 Jiho Kim, 마지막 저자 Edward Choi |
| 6 | 2024 | [Time is Not Enough: Time-Frequency based Explanation for Time-Series Black-Box Models](https://doi.org/10.1145/3627673.3679844) · CIKM | 시계열 분류 모형의 판단을 시간만으로 설명하면 반복되는 주파수 특성을 놓칠 수 있다는 문제를 다뤘다. 시간·주파수 설명 구조인 SpectralX와, 특징을 넣거나 지우고 결합하여 중요도를 추정하는 FIA(Feature Importance Approximations)를 제안했다. 합성 자료와 여러 시계열 자료에서 설명 성능을 비교하고, 사용자 평가로 실제 활용 가능성을 확인했다.[^p6] | 1저자 Hyunseung Chung, 마지막 저자 Edward Choi |
| 7 | 2025 | [PatientSim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions](https://doi.org/10.52202/085713-0861) · NeurIPS Datasets and Benchmarks | 의사 역할 언어 모형을 학습·평가할 수 있도록 다양한 환자와 여러 차례 대화하는 PatientSim을 개발했다. 임상 자료에 성격, 언어 능력, 병력 회상 정도, 인지 혼란 정도를 결합해 환자 역할을 구성한다. 언어 모형의 사실 정확성과 인물 특성의 일관성을 평가했으며, 공개 소프트웨어로 제공하여 다양한 의료 대화 연구와 교육 환경에 맞출 수 있게 했다.[^p7] | 1저자 Daeun Kyung, 마지막 저자 Edward Choi |
| 8 | 2025 | [Generating Multi-Table Time Series EHR from Latent Space with Minimal Preprocessing](https://doi.org/10.52202/085713-0903) · NeurIPS | 개인정보 제약 때문에 공유하기 어려운 의료 기록을 대신할 합성 자료를 만드는 RawMed를 제안했다. 여러 표와 시간 순서가 있는 기록을 글 표현과 압축 기법으로 다루어, 일부 특징만 골라 생성하던 방식의 제약을 다뤘다. 자료의 분포, 표 사이 관계, 시간 변화, 개인정보 보호를 평가하는 구조도 제안했고, 공개 자료 두 종류에서 원자료와의 유사성과 활용성을 비교했다.[^p8] | 1저자 Eunbyeol Cho, 마지막 저자 Edward Choi |

## 교수와 전문 분야

최윤재 부교수는 서울대학교 컴퓨터공학 학사, KAIST 전산학 석사, Georgia Institute of Technology 컴퓨터과학 박사 학위를 받았다. 박사 연구는 설명 가능한 의료 딥러닝(여러 층의 연결된 계산 단위로 자료의 표현을 단계적으로 학습하는 방법)이었고, Google Health Research에서 연구개발을 수행한 뒤 2020년 2월 KAIST에 부임했다.[^background][^home] 현재 소속과 직위는 김재철AI대학원 부교수다.[^gsai]

공개 이력은 전자의무기록의 숨은 관계를 학습하는 예측 모형, 신경망(연결된 계산 단위가 자료의 입력과 출력 관계를 학습하는 모형) 구조의 자동 학습, 설명 가능한 의료 예측과 자연어 처리 경험을 소개한다.[^background] 최근 논문을 기준으로 한 전문 분야는 서로 다른 의료 기록의 통합 학습과 생성, 영상·글·생체신호를 연결하는 모형, 구조화 자료에 근거한 언어 모형 추론, 환자 대화 모사다.[^p1][^p2][^p3][^p4][^p5][^p7][^p8]

## 응용 분야

의료 기록을 이용한 예측, 흉부 영상 판독 보조와 근거 제시, 임상 보고서·생체신호 생성, 환자 면담 교육과 의료 대화 시스템 평가, 병원 접수·일정 관리 모사에 연결한다. 언어 모형이 영어 사용 방식의 차이에 얼마나 견고한지 평가하거나, 가상 인물이 대화 중 일관된 역할을 유지하는지 확인하는 응용도 연구한다.[^projects][^p1][^p2][^p3][^p4]

## 구성원

2026년 11월 9일 연구실 Members 쪽의 박사후연구원 3명, 박사과정 15명, 석사과정 2명, 연구원 1명이다. 과정·직위는 해당 구획 표기이며 교수는 위 소개에 따로 적었다.[^members] ‘대표 논문 참여’는 위 표 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Ji-Ho Kim | 박사후연구원 |  |
| Junu Kim | 박사후연구원 | 1 |
| Jungwoo Oh | 박사후연구원 | 1 |
| Seong-Su Bae | 박사과정 |  |
| Eun-Byeol Cho | 박사과정 |  |
| Geon Choi | 박사과정 |  |
| Junseong Choi | 박사과정 |  |
| Yera Choi | 박사과정 |  |
| Sujeong Im | 박사과정 |  |
| Sumin Jo | 박사과정 | 6 |
| Jiyoun Kim | 박사과정 | 1, 8 |
| Minseo Kim | 박사과정 |  |
| Yeonsu Kwon | 박사과정 | 5, 6 |
| Ji-Young Lee | 박사과정 |  |
| Jun-Min Lee | 박사과정 |  |
| Franck Meyer | 박사과정 | 4 |
| Chaeeun Shim | 박사과정 |  |
| Jeewon Yang | 박사과정 |  |
| Junhee Lee | 석사과정 |  |
| Minhyung Lee | 석사과정 |  |
| Sewon Kim | 연구원 |  |

## 졸업생과 이전 구성원

연구실 Members 쪽 Alumni의 박사 졸업생 11명과 석사 졸업생 11명이다. 학위는 구획 표기를 옮겼다. Ji-Ho Kim·Junu Kim·Jungwoo Oh는 졸업생과 현재 박사후연구원 양쪽에 적혀 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hyun-Seung Chung | 박사 |  |
| Kyunghoon Hur | 박사 |  |
| Ji-Ho Kim | 박사 |  |
| Junu Kim | 박사 |  |
| Sun-Jun Kweon | 박사 |  |
| Da-Eun Kyung | 박사 |  |
| Gyu-Bok Lee | 박사 |  |
| Hyun-Gyung Lee | 박사 |  |
| Jong-Hak Moon | 박사 |  |
| Jungwoo Oh | 박사 |  |
| Sung-Jin Park | 박사 |  |
| Woosog Chay | 석사 |  |
| Seon-Hee Cho | 석사 |  |
| Radhika Dua | 석사 |  |
| Hyeon-Ji Hwang | 석사 |  |
| Dae-Young Kim | 석사 |  |
| Seungho Kim | 석사 |  |
| Min-Jae Lee | 석사 |  |
| Jae-Hee Ryu | 석사 |  |
| Seung-Woo Ryu | 석사 |  |
| Won-Cheol Shin | 석사 |  |
| Seong-Jun Yang | 석사 |  |

## 최근 논문 목록 (2021–2026)

연구실 Publications 쪽의 학술지·학회 논문 및 워크숍·공개 원고 구획에 게시한 2021–2026년 논문이다. 제목·저자·발표처는 연구실 표기이며, 워크숍·공개 원고는 발표처 뒤에 구획을 표시했다. 연구실이 학회 채택을 알렸고 출판 기록 대신 연결된 원고를 제시한 항목에는 ‘채택’을 붙였다. ‘연구실 기재’는 해당 발표처를 연구실이 적은 경우다.[^pubs][^home]

**2026**

- Hyungyung Lee, Hangyul Yoon, Edward Choi. "CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays". *Proc. of Machine Learning for Health (ML4H) 2026; DOI: <https://doi.org/10.48550/arxiv.2602.23276> (연구실 기재)*.
- Sumin Jo, Edward Choi. "HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths". *Proc. of Neural Information Processing Systems (NeurIPS) 2026 Datasets and Benchmarks (채택)*.
- Yeonsu Kwon\*, Jiho Kim\*, Junseong Choi, Paloma Rabaey, Minseo Kim, Sujeong Im, Jeewon Yang, Jun-Min Lee, Sangji Lee, Jiwon Kim, Hangyul Yoon, Hyunwook Kwon, Edward Choi. "Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records". *Proc. of Neural Information Processing Systems (NeurIPS) 2026 Datasets and Benchmarks; DOI: <https://doi.org/10.48550/arxiv.2605.26463> (채택)*.
- Eunbyeol Cho\*, Yunseung Lee\*, Mirae Kim, Jeewon Yang, Youngjun Kwak, Edward Choi. "K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance". *Findings in Empirical Methods in Natural Language Processing (EMNLP) 2026 (채택)*.
- Matthew BA McDermott, Ethan Steinberg, Jason A Fries, Robin P van de Water, Chao Pang, Patrick Rockenschaub, Pawel Renc, Jungwoo Oh, Kamilė Stankevičiūtė, Justin Xu, Tom J Pollard, Nassim Oufattole, Michael Wornow, Teya S Bergamaschi, Hyewon Jeong, Simon A Lee, Vincent Jeanselme, Kiril V Klein, Mikkel Odgaard, Maria E Montgomery, Arkadiusz Sitek, Mads Nielsen, Jeffrey N Chiang, Noa Dagan, Isaac Kohane, Shalmali Joshi, Edward Choi, Nigam H Shah. "MEDS: An Emerging Data Standard and Ecosystem for Health AI Research". *NEJM AI; DOI: <https://doi.org/10.1056/aira2501253>*.
- Jun-Min Lee, Meong Hi Son, Edward Choi. "H-AdminSim: A Multi-Agent Simulator for Realistic Hospital Administrative Workflows with FHIR Integration". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2026 (채택)*.
- Junu Kim, Xiao Liu, Zhenghao Lin, Lei Ji, Yeyun Gong, Edward Choi. "LayerNorm Induces Recency Bias in Transformer Decoders". *Findings in Association for Computational Linguistics (ACL) 2026; DOI: <https://doi.org/10.18653/v1/2026.findings-acl.1430>*.
- Geon Choi\*, Hangyul Yoon\*, Hyunju Shin, Hyunki Park, Sang Hoon Seo, Eunho Yang, Edward Choi. "Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset". *Proc. of Computer Vision and Pattern Recognition (CVPR) 2026 (채택)*.
- Paloma Rabaey\*, Jong Hak Moon\*, Jung-Oh Lee, Min Gwan Kim, Hangyul Yoon, Thomas Demeester, Edward Choi. "Modeling Clinical Uncertainty in Radiology Reports: from Explicit Uncertainty Markers to Implicit Reasoning Pathways". *Proc. of Language Resources and Evaluation Conference (LREC) 2026; DOI: <https://doi.org/10.63317/2i8nrgcnb52p>*.
- Jiyoun Kim, Junu Kim, Kyunghoon Hur, Edward Choi. "Federated Learning for Heterogeneous Electronic Health Record Systems with Cost Effective Participant Selection". *Scientific Reports; DOI: <https://doi.org/10.1038/s41598-026-38299-9>*.
- Hyunseung Chung, Jungwoo Oh, Daeun Kyung, Jiho Kim, Yeonsu Kwon, Min-Gyu Kim, Edward Choi. "ECG-Agent: On-Device Tool-Calling Agent for ECG Multi-Turn Dialogue". *Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2026; DOI: <https://doi.org/10.1109/icassp55912.2026.11464123>*.
- Jiho Kim, Junseong Choi, Woosog Chay, Daeun Kyung, Yeonsu Kwon, Yohan Jo, Edward Choi. "ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation". *Proc. of International Conference on Learning Representations (ICLR) 2026 (채택)*.
- Franck Meyer\*, Kyunghoon Hur\*, Edward Choi. "MD-ViSCo: A Unified Model for Multi-Directional Vital Sign Waveform Conversion". *Journal of Biomedical and Health Informatics (JBHI); DOI: <https://doi.org/10.1109/jbhi.2025.3639315>*.

**2025**

- Jong Hak Moon, Geon Choi, Paloma Rabaey, Min Gwan Kim, Hyuk Gi Hong, Jung-Oh Lee, Hangyul Yoon, Eun Woo Doe, Jiyoun Kim, Harshita Sharma, Daniel C Castro, Javier Alvarez-Valle, Edward Choi. "Lunguage: A Benchmark for Structured and Sequential Chest X-ray Interpretation". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2026; DOI: <https://doi.org/10.48550/arxiv.2505.21190> (채택)*.
- Sumin Jo\*, Junseong Choi\*, Jiho Kim, Edward Choi. "R2-KG: General-Purpose Dual-Agent Framework for Reliable Reasoning on Knowledge Graphs". *Findings in International Joint Conference on Natural Language Processing & Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL) 2025; DOI: <https://doi.org/10.48550/arxiv.2502.12767> (채택)*.
- Eunbyeol Cho, Jiyoun Kim, Minjae Lee, Sungjin Park, Edward Choi. "Generating Multi-Table Time Series EHR from Latent Space with Minimal Preprocessing". *Proc. of Neural Information Processing Systems (NeurIPS) 2025; DOI: <https://doi.org/10.52202/085713-0903>*.
- Daeun Kyung, Hyunseung Chung, Seongsu Bae, Jiho Kim, Jae Ho Sohn, Taerim Kim, Soo Kyung Kim\*, Edward Choi\*. "PatientSim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions". *Proc. of Neural Information Processing Systems (NeurIPS) 2025 Datasets and Benchmarks; DOI: <https://doi.org/10.52202/085713-0861>*.
- Hyungyung Lee, Geon Choi, Jung-Oh Lee, Hangyul Yoon, Hyuk Gi Hong, Edward Choi. "CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays". *Proc. of Neural Information Processing Systems (NeurIPS) 2025 Datasets and Benchmarks; DOI: <https://doi.org/10.52202/085713-2928>*.
- Jiyoung Lee\*, Seungho Kim\*, Jieun Han, Jun-Min Lee, Kitaek Kim, Alice Oh, Edward Choi. "Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties". *Proc. of Neural Information Processing Systems (NeurIPS) 2025 Datasets and Benchmarks; DOI: <https://doi.org/10.52202/085713-3640>*.
- Sunjun Kweon, Sooyohn Nam, Hyunseung Lim, Hwajung Hong, Edward Choi. "A Large-Scale Real-World Evaluation of an LLM-Based Virtual Teaching Assistant". *Proc. of Association for Computational Linguistics (ACL) 2025 Industry Track; DOI: <https://doi.org/10.18653/v1/2025.acl-industry.60>*.
- Sujeong Im\*, Jungwoo Oh\*, Edward Choi. "LabTOP: A Unified Model for Lab Test Outcome Prediction on Electronic Health Records". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2025; DOI: <https://doi.org/10.48550/arxiv.2502.14259> (연구실 기재)*.
- Daeun Kyung, Junu Kim, Tackeun Kim, Edward Choi. "Towards Predicting Temporal Changes in a Patient's Chest X-ray Images based on Electronic Health Records". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2025; DOI: <https://doi.org/10.48550/arxiv.2409.07012> (채택)*.
- Sungjin Park, Xiao Liu, Yeyun Gong, Edward Choi. "Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning". *Proc. of North American Chapter of the Association for Computational Linguistics (NAACL) 2025; DOI: <https://doi.org/10.18653/v1/2025.naacl-long.515>*.
- Soyoung Yang, Hojun Cho, Jiyoung Lee, Sohee Yoon, Edward Choi, Jaegul Choo, Won Ik Cho. "Single Ground Truth Is Not Enough: Add Linguistic Variability to Aspect-based Sentiment Analysis Evaluation". *Proc. of North American Chapter of the Association for Computational Linguistics (NAACL) 2025 (연구실 기재)*.

**2024**

- Yeonsu Kwon\*, Jiho Kim\*, Gyubok Lee, Seongsu Bae, Daeun Kyung, Wonchul Cha, Tom Pollard, Alistair Johnson, Edward Choi. "EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records". *Proc. of Neural Information Processing Systems (NeurIPS) 2024 Datasets and Benchmarks; DOI: <https://doi.org/10.52202/079017-2835>*.
- Daehoon Gwak\*, Junwoo Park\*, Minho Park, Chaehun Park, Hyunchan Lee, Edward Choi, Jaegul Choo. "Forecasting Future International Events: A Reliable Dataset for Text-Based Event Modeling". *Findings in Empirical Methods in Natural Language Processing (EMNLP) 2024; DOI: <https://doi.org/10.18653/v1/2024.findings-emnlp.526>*.
- Jongseong Jang\*, Daeun Kyung\*, Seung Hwan Kim, Honglak Lee, Kyunghoon Bae, Edward Choi. "Significantly Improving Zero-shot X-ray Pathology Classification via Fine-tuning Pre-trained Image-Text Encoders". *Scientific Reports; DOI: <https://doi.org/10.1038/s41598-024-73695-z>*.
- Hyunseung Chung, Sumin Jo, Yeonsu Kwon, Edward Choi. "Time is Not Enough: Time-Frequency based Explanation for Time-Series Black-Box Models". *Proc. of International Conference on Information and Knowledge Management (CIKM) 2024; DOI: <https://doi.org/10.1145/3627673.3679844>*.
- Junu Kim, Chaeeun Shim, Bosco Seong Kyu Yang, Chami Im, Sung Yoon Lim, Han-Gil Jeong, Edward Choi. "General-Purpose Retrieval-Enhanced Medical Prediction Model Using Near-Infinite History". *Proc. of Machine Learning for Healthcare (MLHC) 2024; DOI: <https://doi.org/10.48550/arxiv.2310.20204> (채택)*.
- Jiyoung Lee\*, Minwoo Kim\*, Seungho Kim, Junghwan Kim, Seunghyun Won, Hwaran Lee, Edward Choi. "KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge". *Findings in Association for Computational Linguistics (ACL) 2024; DOI: <https://doi.org/10.18653/v1/2024.findings-acl.666>*.
- Sunjun Kweon\*, Junu Kim\*, Jiyoun Kim, Sujeong Im, Eunbyeol Cho, Seongsu Bae, Jungwoo Oh, Gyubok Lee, Jong Hak Moon, Seng Chan You, Seungjin Baek, Chang Hoon Han, Yoon Bin Jung, Yohan Jo, Edward Choi. "Publicly Shareable Clinical Large Language Model Built on Synthetic Clinical Notes". *Findings in Association for Computational Linguistics (ACL) 2024; DOI: <https://doi.org/10.48550/arxiv.2309.00237> (채택)*.
- Hyungyung Lee, Da Young Lee, Wonjae Kim, Jin-Hwa Kim, Tackeun Kim, Jihang Kim, Leonard Sunwoo, Edward Choi. "Vision-Language Generative Model for View-Specific Chest X-ray Generation". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2024; DOI: <https://doi.org/10.48550/arxiv.2302.12172> (채택)*.
- Junwoo Park, Daehoon Gwak, Jaegul Choo, Edward Choi. "Self-Supervised Contrastive Learning for Long-term Forecasting". *Proc. of International Conference on Learning Representations (ICLR) 2024; DOI: <https://doi.org/10.48550/arxiv.2402.02023> (채택)*.
- Sungjin Park, Edward Choi. "Multimodal Transformer with a Low-Computational-Cost Guarantee". *Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2024; DOI: <https://doi.org/10.1109/icassp48485.2024.10447954>*.
- Kiduk Kim, Kyungjin Cho, Ryoungwoo Jang, Sunggu Kyung, Soyoung Lee, Sungwon Ham, Edward Choi, Gil-Sun Hong, Namkug Kim. "Updated Primer on Generative Artificial Intelligence and Large Language Models in Medical Imaging for Medical Professionals". *Korean Journal of Radiology (KJR); DOI: <https://doi.org/10.3348/kjr.2023.0818>*.
- Kyunghoon Hur, Jungwoo Oh, Junu Kim, Min Jae Lee, Eunbyeol Cho, Jiyoun Kim, Seong-Eun Moon, Young-Hak Kim, Louis Atallah, Edward Choi. "GenHPF : General Healthcare Predictive Framework for Multi-task Multi-source Learning". *Journal of Biomedical and Health Informatics (JBHI); DOI: <https://doi.org/10.1109/jbhi.2023.3327951>*.
- Jiho Kim, Woosog Chay, Hyeonji Hwang, Daeun Kyung, Hyunseung Chung, Eunbyeol Cho, Yohan Jo, Edward Choi. "DialSim: A Real-Time Simulator for Evaluating Long-Term Dialogue Understanding of Conversational Agents". *(워크숍·공개 원고 구획)*.
- Gyubok Lee, Woosog Chay, Seonhee Cho, Edward Choi. "TrustSQL: Benchmarking Text-to-SQL Reliability with Penalty-Based Scoring". *; DOI: <https://doi.org/10.48550/arxiv.2403.15879> (워크숍·공개 원고 구획)*.

**2023**

- Jiho Kim, Yeonsu Kwon, Yohan Jo, Edward Choi. "KG-GPT: A General Framework for Reasoning on Knowledge Graphs Using Large Language Models". *Findings in Empirical Methods in Natural Language Processing (EMNLP) 2023; DOI: <https://doi.org/10.18653/v1/2023.findings-emnlp.631>*.
- Seongsu Bae\*, Daeun Kyung\*, Jaehee Ryu, Eunbyeol Cho, Gyubok Lee, Sunjun Kweon, Jungwoo Oh, Lei Ji, Eric I-Chao Chang, Tackeun Kim, Edward Choi. "EHRXQA: A Multi-Modal Question Answering Dataset for Electronic Health Records with Chest X-ray Images". *Proc. of Neural Information Processing Systems (NeurIPS) 2023 Datasets and Benchmarks; DOI: <https://doi.org/10.48550/arxiv.2310.18652> (채택)*.
- Jiyoung Lee, Seungho Kim, Seunghyun Won, Joonseok Lee, Marzyeh Ghassemi, James Thorne, Jaeseok Choi, O-Kil Kwon, Edward Choi. "VisAlign: Dataset for Measuring the Alignment between AI and Humans in Visual Perception". *Proc. of Neural Information Processing Systems (NeurIPS) 2023 Datasets and Benchmarks; DOI: <https://doi.org/10.48550/arxiv.2308.01525> (채택)*.
- Kwanhyung Lee, Soojeong Lee, Sangchul Hahn, Heejung Hyun, Edward Choi, Byungeun Ahn, Joohyung Lee. "Learning Missing Modal Electronic Health Records with Unified Multi-modal Data Embedding and Modality-Aware Attention". *Proc. of Machine Learning for Healthcare (MLHC) 2023; DOI: <https://doi.org/10.48550/arxiv.2305.02504> (연구실 기재)*.
- Junwoo Park, Jungsoo Lee, Youngin Cho, Woncheol Shin, Dongmin Kim, Jaegul Choo, Edward Choi. "Deep Imbalanced Time-series Forecasting via Local Discrepancy Density". *Proc. of European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD) 2023; DOI: <https://doi.org/10.1007/978-3-031-43424-2_9>*.
- Jiho Kim, Sungjin Park, Yeonsu Kwon, Yohan Jo, James Thorne, Edward Choi. "FactKG: Fact Verification via Reasoning on Knowledge Graph". *Proc. of Association for Computational Linguistics (ACL) 2023; DOI: <https://doi.org/10.18653/v1/2023.acl-long.895>*.
- Sunjun Kweon, Yeonsu Kwon, Seonhee Cho, Yohan Jo, Edward Choi. "Open-WikiTable : Dataset for Open Domain Question Answering with Complex Reasoning over Table". *Findings in Association for Computational Linguistics (ACL) 2023; DOI: <https://doi.org/10.18653/v1/2023.findings-acl.526>*.
- Eunbyeol Cho\*, Min Jae Lee\*, Kyunghoon Hur, Jiyoun Kim, Jinsung Yoon, Edward Choi. "Rediscovery of CNN's Versatility for Text-based Encoding of Raw Electronic Health Records". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2023; DOI: <https://doi.org/10.48550/arxiv.2303.08290> (채택)*.
- Hyunseung Chung, Jiho Kim, Joon-myoung Kwon, Ki-Hyun Jeon, Min Sung Lee, Edward Choi. "Text-To-ECG: 12-Lead Electrocardiogram Synthesis Conditioned on Clinical Text Reports". *Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2023; DOI: <https://doi.org/10.1109/icassp49357.2023.10096898>*.
- Daeun Kyung\*, Kyungmin Jo\*, Jaegul Choo, Joonseok Lee, Edward Choi. "Perspective Projection-Based 3D CT Reconstruction from Biplanar X-rays". *Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2023 (Oral Presentation, Best Student Paper Award); DOI: <https://doi.org/10.1109/icassp49357.2023.10096296>*.
- Woncheol Shin, Gyubok Lee, Jiyoung Lee, Eunyi Lyou, Joonseok Lee, Edward Choi. "Exploration into Translation-Equivariant Image Quantization". *Proc. of International Conference on Acoustics, Speech, and Signal Processing (ICASSP) 2023 (Oral Presentation) (연구실 기재)*.
- Jungsoo Lee, Jeonghoon Park, Daeyoung Kim, Juyoung Lee, Edward Choi, Jaegul Choo. "Revisiting the Importance of Amplifying Bias for Debiasing". *Proc. of Association for the Advancement of Artificial Intelligence (AAAI) 2023; DOI: <https://doi.org/10.1609/aaai.v37i12.26748>*.
- Radhika Dua, Seongjun Yang, Yixuan Li, Edward Choi. "Task Agnostic and Post-hoc Unseen Distribution Detection". *Proc. of Winter Conference on Applications of Computer Vision (WACV) 2023; DOI: <https://doi.org/10.1109/wacv56688.2023.00140>*.
- Kwanhyung Lee, John Won, Heejung Hyun, Sangchul Hahn, Edward Choi, Joohyung Lee. "Self-Supervised Predictive Coding with Multimodal Fusion for Patient Deterioration Prediction in Fine-grained Time Resolution". *Trustworthy Machine Learning for Healthcare Workshop at ICLR 2023; DOI: <https://doi.org/10.1007/978-3-031-39539-0_4> (워크숍·공개 원고 구획)*.

**2022**

- Sungjin Park, Seungwoo Ryu, Edward Choi. "Do Language Models Understand Measurements?". *Findings in Empirical Methods in Natural Language Processing (EMNLP) 2022; DOI: <https://doi.org/10.18653/v1/2022.findings-emnlp.128>*.
- Jiyoung Lee, Hantae Kim, Hyunchang Cho, Edward Choi, Cheonbok Park. "Specializing Multi-domain NMT via Penalizing Low Mutual Information". *Proc. of Empirical Methods in Natural Language Processing (EMNLP) 2022; DOI: <https://doi.org/10.18653/v1/2022.emnlp-main.680>*.
- Hojun Cho, Dohee Kim, Seungwoo Ryu, ChaeHun Park, Hyungjong Noh, Jeong-in Hwang, Minseok Choi, Edward Choi, Jaegul Choo. "Rethinking Style Transformer with Energy-based Interpretation: Adversarial Unsupervised Style Transfer using a Pretrained Model". *Proc. of Empirical Methods in Natural Language Processing (EMNLP) 2022; DOI: <https://doi.org/10.18653/v1/2022.emnlp-main.366>*.
- Hyungyung Lee, Sungjin Park, Joonseok Lee, Edward Choi. "Unconditional Image-Text Pair Generation with Multimodal Cross Quantizer". *Proc. of British Machine Vision Conference (BMVC) 2022 (채택)*.
- Jong Hak Moon, Wonjae Kim, Edward Choi. "Correlation between Alignment-Uniformity and Performance of Dense Contrastive Representations". *Proc. of British Machine Vision Conference (BMVC) 2022; DOI: <https://doi.org/10.48550/arxiv.2210.08819> (채택)*.
- Jong Hak Moon\*, Hyungyung Lee\*, Woncheol Shin, Young-Hak Kim, Edward Choi. "Multi-modal Understanding and Generation for Medical Images and Text via Vision-Language Pre-Training". *Journal of Biomedical and Health Informatics (JBHI); DOI: <https://doi.org/10.1109/jbhi.2022.3207502>*.
- Taehee Kim\*, ChaeHun Park\*, Jimin Hong, Radhika Dua, Edward Choi, Jaegul Choo. "Reweighting Strategy based on Synthetic Data Identification for Sentence Similarity". *Proc. of International Conference on Computational Linguistics (COLING) 2022; DOI: <https://doi.org/10.48550/arxiv.2208.13376> (연구실 기재)*.
- Jungwoo Oh, Hyunseung Chung, Joon-myoung Kwon, Dong-gyun Hong, Edward Choi. "Lead-agnostic Self-supervised Learning for Local and Global Representations of Electrocardiogram". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2022; DOI: <https://doi.org/10.48550/arxiv.2203.06889> (채택)*.
- Daeyoung Kim, Seongsu Bae, Seungho Kim, Edward Choi. "Uncertainty-Aware Text-to-Program for Question Answering on Structured Electronic Health Records". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2022; DOI: <https://doi.org/10.48550/arxiv.2203.06918> (채택)*.
- Sungjin Park, Seongsu Bae, Jiho Kim, Tackeun Kim, Edward Choi. "Graph-Text Multi-Modal Pre-training for Medical Representation Learning". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2022; DOI: <https://doi.org/10.48550/arxiv.2203.09994> (채택)*.
- Kyunghoon Hur\*, Jiyoung Lee\*, Jungwoo Oh, Wesley Price, Young-Hak Kim, Edward Choi. "Unifying Heterogenous Electronic Health Records Systems via Text-Based Code Embedding". *Proc. of Conference on Health, Inference, and Learning (CHIL) 2022*.
- Junu Kim, Kyunghoon Hur, Seongjun Yang, Edward Choi. "Universal EHR Federated Learning Framework". *Extended abstract in Machine Learning for Health (ML4H) 2022; DOI: <https://doi.org/10.48550/arxiv.2211.07300> (워크숍·공개 원고 구획)*.
- Radhika Dua, Jiyoung Lee, Joon-myoung Kwon, Edward Choi. "Automatic Detection of Noisy Electrocardiogram Signals without Explicit Noise Labels". *Pattern Recognition for Healthcare Analytics Workshop at ICPR 2022; DOI: <https://doi.org/10.1007/978-3-031-37742-6_49> (워크숍·공개 원고 구획)*.

**2021**

- Seongsu Bae, Daeyoung Kim, Jiho Kim, Edward Choi. "Question Answering for Complex Electronic Health Records Database using Unified Encoder-Decoder Architecture". *Proc. of Machine Learning for Health (ML4H) 2021 (Oral Spotlight, Best Poster Award); DOI: <https://doi.org/10.48550/arxiv.2111.14703> (연구실 기재)*.
- Kangyeol Kim\*, Sunghyun Park\*, Junsoo Lee, Joonseok Lee, Sookyung Kim, Jaegul Choo, Edward Choi. "Continuous-Time Video Generation via Learning Motion Dynamics with Neural ODE". *Proc. of British Machine Vision Conference (BMVC) 2021; DOI: <https://doi.org/10.5244/c.35.7>*.
- Jiyoung Lee, Wonjae Kim, Daehoon Gwak, Edward Choi. "Conditional Generation of Periodic Signals with Fourier-Based Decoder". *Deep Generative Models and Downstream Applications Workshop at NeurIPS 2021; DOI: <https://doi.org/10.48550/arxiv.2110.12365> (워크숍·공개 원고 구획)*.
- Jeonghoon Park\*, Jimin Hong\*, Radhika Dua\*, Daehoon Gwak, Yixuan Li, Jaegul Choo, Edward Choi. "Natural Attribute-based Shift Detection". *; DOI: <https://doi.org/10.48550/arxiv.2110.09276> (워크숍·공개 원고 구획)*.

## 공개 프로젝트

연구실 Projects 쪽에 소개된 연구 프로젝트다. 수행 기간과 게시 날짜는 적혀 있지 않다.[^projects]

- PICon: A Multi-Turn Interrogation Framework for Evaluating Persona Agent Consistency
- CXReasonAgent: An Evidence-Grounded Diagnostic Reasoning Agent for Chest X-Rays
- H-AdminSim: A Multi-Agent Simulation Framework for Hospital Administrative Workflows
- PatientSim: An Open-Source LLM-Powered Patient Simulator
- Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties

## 수상과 선정 (2021–2026)

연구실 첫 화면의 최근 소식에 게시된 수상과 선정이다. 날짜는 소식에 적힌 연월이다.[^home]

- 2026-08 · Doctor AI 논문: MLHC 2026 Test of Time Award
- 2026-06 · Jun-Min Lee: H-AdminSim, CHIL 2026 Best Paper Award
- 2025-04 · Sujeong Im·Jungwoo Oh: LabTOP, CHIL 2025 Best Paper Award
- 2023-02 · Daeun Kyung: PerX2CT, ICASSP 2023 Best Student Paper Award (Oral)
- 2023-02 · Woncheol Shin: Exploration into Translation-Equivariant Image Quantization, ICASSP 2023 논문 선정 (Oral)
- 2021-12 · Seongsu Bae: Question Answering for Complex EHR Database, ML4H 2021 Best Poster Award (Oral Spotlight)

## 연구 소식 (2021–2026)

연구실 첫 화면의 최근 소식에서 논문 게재·게재 승인·학회 채택·발표 예정과 프로젝트 공개를 옮겼다. 날짜는 게시된 연월이며, 학회의 ‘채택’과 학술지의 ‘게재 승인’을 구분했다.[^home]

- 2026-09 · HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths: NeurIPS 2026 Datasets and Benchmarks 채택
- 2026-09 · Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records: NeurIPS 2026 Datasets and Benchmarks 채택
- 2026-08 · K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance: Findings of EMNLP 2026 채택
- 2026-05 · MEDS: An Emerging Data Standard and Ecosystem for Health AI Research: NEJM AI 게재
- 2026-04 · PICon·CXReasonAgent·H-AdminSim·PatientSim 프로젝트와 시연 공개
- 2026-04 · H-AdminSim: A Multi-Agent Simulator for Realistic Hospital Administrative Workflows with FHIR Integration: CHIL 2026 채택
- 2026-04 · Lunguage: A Benchmark for Structured and Sequential Chest X-ray Interpretation: CHIL 2026 채택
- 2026-04 · LayerNorm Induces Recency Bias in Transformer Decoders: Findings of ACL 2026 채택
- 2026-02 · Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset: CVPR 2026 채택
- 2026-02 · Modeling Clinical Uncertainty in Radiology Reports: from Explicit Uncertainty Markers to Implicit Reasoning Pathways: LREC 2026 채택
- 2026-01 · Federated Learning for Heterogeneous Electronic Health Record Systems with Cost Effective Participant Selection: Scientific Reports 게재 승인
- 2026-01 · ECG-Agent: On-Device Tool-Calling Agent for ECG Multi-Turn Dialogue: ICASSP 2026 채택
- 2026-01 · ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation: ICLR 2026 채택
- 2026-01 · MD-ViSCo: A Unified Model for Multi-Directional Vital Sign Waveform Conversion: JBHI 게재
- 2025-10 · R2-KG: General-Purpose Dual-Agent Framework for Reliable Reasoning on Knowledge Graphs: Findings of IJCNLP-AACL 2025 채택
- 2025-09 · Generating Multi-Table Time Series EHR from Latent Space with Minimal Preprocessing: NeurIPS 2025 채택
- 2025-09 · PatientSim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions: NeurIPS 2025 Datasets and Benchmarks (Spotlight) 채택
- 2025-09 · CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays: NeurIPS 2025 Datasets and Benchmarks (Spotlight) 채택
- 2025-09 · Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties: NeurIPS 2025 Datasets and Benchmarks 채택
- 2025-05 · A Large-Scale Real-World Evaluation of an LLM-Based Virtual Teaching Assistant: ACL 2025 Industry Track 채택
- 2025-04 · Towards Predicting Temporal Changes in a Patient's Chest X-ray Images based on Electronic Health Records: CHIL 2025 채택
- 2025-01 · Ensembling Large Language Models with Process Reward-Guided Tree Search for Better Complex Reasoning: NAACL 2025 채택
- 2025-01 · Single Ground Truth Is Not Enough: Add Linguistic Variability to Aspect-based Sentiment Analysis Evaluation: NAACL 2025 발표 예정
- 2024-09 · EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records: NeurIPS 2024 Datasets and Benchmarks (Spotlight) 채택
- 2024-09 · Forecasting Future International Events: A Reliable Dataset for Text-Based Event Modeling: Findings of EMNLP 2024 발표 예정
- 2024-09 · Significantly Improving Zero-shot X-ray Pathology Classification via Fine-tuning Pre-trained Image-Text Encoders: Scientific Reports 게재 승인
- 2024-07 · Time is Not Enough: Time-Frequency based Explanation for Time-Series Black-Box Models: CIKM 2024 채택
- 2024-07 · General-Purpose Retrieval-Enhanced Medical Prediction Model Using Near-Infinite History: MLHC 2024 채택
- 2024-05 · KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge: Findings of ACL 2024 채택
- 2024-05 · Publicly Shareable Clinical Large Language Model Built on Synthetic Clinical Notes: Findings of ACL 2024 채택
- 2024-04 · Vision-Language Generative Model for View-Specific Chest X-ray Generation: CHIL 2024 채택
- 2024-01 · Self-Supervised Contrastive Learning for Long-term Forecasting: ICLR 2024 채택
- 2023-12 · Multimodal Transformer with a Low-Computational-Cost Guarantee: ICASSP 2024 채택
- 2023-12 · Updated Primer on Generative Artificial Intelligence and Large Language Models in Medical Imaging for Medical Professionals: Korean Journal of Radiology 게재 예정
- 2023-10 · GenHPF : General Healthcare Predictive Framework for Multi-task Multi-source Learning: JBHI 게재 승인
- 2023-10 · KG-GPT: A General Framework for Reasoning on Knowledge Graphs Using Large Language Models: Findings of EMNLP 2023 채택
- 2023-09 · EHRXQA: A Multi-Modal Question Answering Dataset for Electronic Health Records with Chest X-ray Images: NeurIPS 2023 Datasets and Benchmarks 채택
- 2023-09 · VisAlign: Dataset for Measuring the Alignment between AI and Humans in Visual Perception: NeurIPS 2023 Datasets and Benchmarks 채택
- 2023-09 · Learning Missing Modal Electronic Health Records with Unified Multi-modal Data Embedding and Modality-Aware Attention: MLHC 2023 발표 예정
- 2023-06 · Deep Imbalanced Time-series Forecasting via Local Discrepancy Density: ECML-PKDD 2023 채택
- 2023-05 · FactKG: Fact Verification via Reasoning on Knowledge Graph: ACL 2023 채택
- 2023-05 · Open-WikiTable : Dataset for Open Domain Question Answering with Complex Reasoning over Table: Findings of ACL 2023 채택
- 2023-04 · Rediscovery of CNN's Versatility for Text-based Encoding of Raw Electronic Health Records: CHIL 2023 (Oral Presentation) 채택
- 2023-02 · Text-To-ECG: 12-Lead Electrocardiogram Synthesis Conditioned on Clinical Text Reports: ICASSP 2023 채택
- 2022-11 · Revisiting the Importance of Amplifying Bias for Debiasing: AAAI 2023 발표 예정
- 2022-10 · Task Agnostic and Post-hoc Unseen Distribution Detection: WACV 2023 채택
- 2022-10 · Do Language Models Understand Measurements?: Findings of EMNLP 2022 채택
- 2022-10 · Specializing Multi-domain NMT via Penalizing Low Mutual Information: EMNLP 2022 채택
- 2022-10 · Rethinking Style Transformer with Energy-based Interpretation: Adversarial Unsupervised Style Transfer using a Pretrained Model: EMNLP 2022 발표 예정
- 2022-10 · Reweighting Strategy based on Synthetic Data Identification for Sentence Similarity: COLING 2022 발표 예정
- 2022-10 · Multi-modal Understanding and Generation for Medical Images and Text via Vision-Language Pre-Training: JBHI 게재 승인
- 2022-09 · Unconditional Image-Text Pair Generation with Multimodal Cross Quantizer: BMVC 2022 채택
- 2022-09 · Correlation between Alignment-Uniformity and Performance of Dense Contrastive Representations: BMVC 2022 채택
- 2022-03 · Lead-agnostic Self-supervised Learning for Local and Global Representations of Electrocardiogram: CHIL 2022 채택
- 2022-03 · Uncertainty-Aware Text-to-Program for Question Answering on Structured Electronic Health Records: CHIL 2022 채택
- 2022-03 · Graph-Text Multi-Modal Pre-training for Medical Representation Learning: CHIL 2022 채택
- 2022-03 · Unifying Heterogenous Electronic Health Records Systems via Text-Based Code Embedding: CHIL 2022 채택

## 연락과 위치

- 교수 이메일: edwardchoi@kaist.ac.kr[^gsai]
- 사무실: 성남연구센터[^gsai]
[^home]: Edward Choi's Lab, 첫 화면의 연구 관심·Recent Update. <https://mp2893.com/> 관측 2026-11-09.
[^members]: Edward Choi's Lab, Members. <https://mp2893.com/members.html> 관측 2026-11-09.
[^pubs]: Edward Choi's Lab, Publications. <https://mp2893.com/publication.html> 관측 2026-11-09.
[^projects]: Edward Choi's Lab, Projects의 PICon·CXReasonAgent·H-AdminSim·PatientSim·Trans-EnV 개별 설명. <https://mp2893.com/projects.html> 관측 2026-11-09.
[^cx-project]: Edward Choi's Lab, CXReasonAgent 개별 연구 설명. <https://mp2893.com/projects.html> 관측 2026-11-09.
[^hadmin-project]: Edward Choi's Lab, H-AdminSim 개별 연구 설명. <https://mp2893.com/projects.html> 관측 2026-11-09.
[^patient-project]: Edward Choi's Lab, PatientSim 개별 연구 설명. <https://mp2893.com/projects.html> 관측 2026-11-09.
[^transenv-project]: Edward Choi's Lab, Trans-EnV 개별 연구 설명. <https://mp2893.com/projects.html> 관측 2026-11-09.
[^background]: Edward Choi's Lab, Professional Experience·Education. <https://mp2893.com/background.html> 관측 2026-11-09.
[^gsai]: KAIST 김재철AI대학원, 전임교수 최윤재 소개. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-11-09.

[^p1]: K. Hur 외, E. Choi, IEEE Journal of Biomedical and Health Informatics (2023). <https://doi.org/10.1109/jbhi.2023.3327951> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p2]: J. H. Moon 외, E. Choi, IEEE Journal of Biomedical and Health Informatics (2022). <https://doi.org/10.1109/jbhi.2022.3207502> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p3]: H. Chung 외, E. Choi, IEEE International Conference on Acoustics Speech and Signal Processing (2023). <https://doi.org/10.1109/icassp49357.2023.10096898> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p4]: F. Meyer, K. Hur, E. Choi, IEEE Journal of Biomedical and Health Informatics (2026). <https://doi.org/10.1109/jbhi.2025.3639315> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p5]: J. Kim, Y. Kwon, Y. Jo, E. Choi, Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP) (2023). <https://doi.org/10.18653/v1/2023.findings-emnlp.631> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p6]: H. Chung, S. Jo, Y. Kwon, E. Choi, ACM International Conference on Information and Knowledge Management (CIKM) (2024). <https://doi.org/10.1145/3627673.3679844> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p7]: D. Kyung 외, E. Choi, neural information processing systems (2025). <https://doi.org/10.52202/085713-0861> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.
[^p8]: E. Cho 외, E. Choi, neural information processing systems (2025). <https://doi.org/10.52202/085713-0903> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5034622258,publication_year:2021-2026> 관측 2026-11-11.

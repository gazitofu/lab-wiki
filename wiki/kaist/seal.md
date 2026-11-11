# SEAL (Scalable & Efficient AI Lab)

**KAIST 김재철AI대학원 · 김세훈 조교수**

- 분야: 인공지능의 학습·실행 효율, 언어 모델, 추론과 자율 작업 수행[^home][^dept]
- 대분야: 컴퓨팅·AI
- 태그: AI 시스템·인프라[^home], 대형 언어 모델[^people][^p4], 모델 경량화·양자화[^home]
- 홈페이지: <https://seal-kaist.github.io/>
- 근거와 출처: [SEAL 근거 페이지](seal-sources.md)

> 인공지능의 계산과 저장 부담을 줄이는 방법을 모델 설계부터 실행 시스템까지 함께 연구하며, 언어 모델과 자율 작업 수행 기술을 다양한 계산 환경에서 쓸 수 있게 만드는 연구실이다.[^home]

## 무엇을 연구하나

SEAL은 계산 자원이 많이 드는 인공지능의 학습과 실행을 효율화하는 알고리즘(문제를 풀기 위한 계산 절차)과 시스템을 개발한다. 연구실은 기반 모델(넓은 범위의 자료로 학습해 여러 과제에 활용하는 인공지능 모델)의 구조, 학습·추론(학습한 모델로 새 입력의 결과를 계산하는 과정) 시스템, 압축과 배포를 함께 다룬다.[^home] 대형 언어 모델(Large Language Model, LLM)은 많은 글을 학습해 글을 이해하고 생성하는 큰 인공지능 모델이다. 교수는 인공지능 시스템, 효율적인 인공지능, 대형 언어 모델을 연구한다.[^people] 연구실의 PhaseGate는 기기 안에서 언어 모델 추론과 자료 검색을 함께 실행하는 방법을 다룬다.[^p4]

한 갈래는 모델이 저장하고 읽어야 하는 정보를 줄이는 연구다. 신경망(서로 연결된 계산 단위의 연결 강도를 학습하는 모형)의 한 구조인 트랜스포머는 입력 요소 사이의 관련도를 계산해 정보를 처리한다. 이를 반복 적용하는 모델에서, 반복 단계 사이의 공통 정보와 차이를 나눠 저장하거나 중간 계산을 활용해 다음 출력을 미리 제안한다. ResidualQuant는 저장 부담을, LoopSpec은 출력 생성에 드는 시간을 줄이는 방법을 제안한다.[^p1][^p2]

또 다른 갈래는 모델 계산과 자료 이동을 함께 조절하는 실행 시스템이다. SketchSSM은 모델 내부 상태를 갱신하는 과정과 그 상태를 읽는 과정을 나눠, 읽기에는 압축된 요약을 활용한다. PhaseGate는 한 기기에서 언어 모델과 자료 검색을 함께 실행할 때, 언어 모델의 실행 단계에 맞춰 검색 작업의 동시 실행 수를 조절한다.[^p3][^p4]

연구실은 에이전트(환경과 상호작용하며 목표를 달성하도록 행동을 선택하는 인공지능)의 추론, 계획, 자기 개선과 도구 사용도 연구한다. GEPA-Curator는 에이전트의 프롬프트(모델에 과제와 조건을 전달하는 입력 내용)를 개선할 때 어떤 과제와 과거 경험을 쓸지 고르는 방법이다.[^home][^p5]

## 주요 연구 주제

### 1. 반복 모델의 저장 부담과 생성 시간 절감

모델 경량화는 모델의 구조나 계산·저장 표현을 바꿔 필요한 자원을 줄이는 방법이다. 연구실은 이를 위한 모델 구조와 압축 방법을 개발한다.[^home] 이 계산에서 쓰는 벡터는 여러 수를 순서대로 모은 수학적 표현이다. ResidualQuant는 KV 캐시(Key-Value cache, 이전 입력에서 계산한 키와 값 벡터를 다시 쓰기 위해 보관하는 공간)의 양자화(연속적이거나 정밀한 수치를 한정된 대표값으로 나타내는 방법)를 다룬다. LoopSpec은 반복 계산의 앞 단계에서 출력 초안을 만들고 검증과 겹쳐 실행한다.[^p1][^p2]

### 2. 추론 시스템과 내부 상태 접근

연구실은 기반 모델의 학습·추론·배포를 맡는 시스템을 개발한다.[^home] SketchSSM은 내부 상태를 갱신할 때 만든 압축 요약으로 후속 출력을 계산해, 전체 상태를 반복해서 읽는 부담을 줄인다. PhaseGate는 입력을 한꺼번에 처리하는 단계와 출력을 차례로 만드는 단계에 각각 다른 검색 동시 실행 한도를 적용한다. 처리량과 지연 시간을 함께 고려하는 기기 내부 실행 연구다.[^p3][^p4]

### 3. 에이전트의 계획과 경험 선택

연구실은 여러 단계에 걸쳐 행동하는 에이전트의 계획과 자기 개선을 연구한다. GEPA-Curator는 개선에 부정확한 신호를 줄 수 있는 과제를 걸러 내고, 같은 과제의 과거 성공 경로를 골라 프롬프트 개선에 제공한다. 프롬프트 개선에 쓸 과제와 경험을 선택하는 방법이다.[^home][^p5]

## 대표 논문

KAIST 재직 시기에 공개된 논문에서 모델 압축, 생성 가속, 실행 시스템과 에이전트 연구를 고르게 골랐다. 아래 다섯 편은 arXiv 사전 공개본이며 PhaseGate는 학회 워크숍 채택도 발표했다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다.[^p1][^p2][^p3][^p4][^p5]

| 번호 | 연도 | 논문 | 쉽게 말하면 | 주요 저자와 김세훈의 역할 |
|---|---|---|---|---|
| 1 | 2026 | [ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals](https://doi.org/10.48550/arxiv.2610.10381) | 반복 단계의 저장값이 서로 비슷하다는 점을 이용해, 마지막 단계의 값을 기준으로 두고 나머지는 차이만 압축해 저장한다. | 1저자 Heejun Kim; 김세훈 마지막 저자[^p1] |
| 2 | 2026 | [LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers](https://doi.org/10.48550/arxiv.2609.17184) | 반복 계산의 앞 단계에서 출력 초안을 얻고, 다음 출력의 초안 생성과 현재 출력의 검증을 겹쳐 실행한다. 별도 초안 모델이나 추가 학습 없이 생성을 가속한다. | 공동 1저자 SangLyul Cho·Langqing Cui; 김세훈 중간 저자[^p2][^aff-loop] |
| 3 | 2026 | [SketchSSM: Write to the Full State, Read from a Compact Sketch](https://doi.org/10.48550/arxiv.2609.33051) | 모델의 전체 내부 상태는 그대로 갱신하면서, 미리 계산한 작은 요약에서 출력에 필요한 값을 재구성해 전체 상태를 읽는 횟수를 줄인다. | 1저자 Omin Kwon; 김세훈·Jae W. Lee 공동 지도[^p3][^pubs] |
| 4 | 2026 | [PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory](https://doi.org/10.48550/arxiv.2610.04537) | 언어 모델이 입력을 처리할 때와 출력을 만들 때에 검색 작업을 동시에 허용하는 수를 다르게 정한다. 실험에서 지연 시간 제한을 지키며 검색 처리량을 높였다. | 1저자 Seoyoon Yum; 김세훈 마지막 저자[^p4] |
| 5 | 2026 | [GEPA-Curator: Curated Learning for Self Improving Agents](https://doi.org/10.48550/arxiv.2610.37651) | 에이전트의 개선에 도움이 되지 않는 과제를 거르고, 과거 성공 경험을 골라 제공해 프롬프트를 개선한다. | 공동 1저자 Zack Yu·Nicholas Lee; 김세훈·Amir Gholami 공동 지도[^p5][^pubs] |

## 교수와 전문 분야

김세훈(Sehoon Kim)은 2026년 8월 KAIST에 부임한 조교수다. 전문 분야는 인공지능 시스템, 효율적인 인공지능, 대형 언어 모델이다. KAIST 부임 전 xAI에서 Grok의 추론 및 강화학습 기반 시설을 개발했고, UC Berkeley에서 전산학 박사학위를 받았다. 강화학습은 행동의 결과로 얻는 보상을 바탕으로 행동 선택 방법을 배우는 기계학습이다.[^dept][^pi][^people]

이력에는 UC Berkeley 전산학 석사·박사 과정 2020–2024년, 서울대학교 전기·컴퓨터공학(Electrical and Computer Engineering) 학사 과정 2015–2020년, Narada AI Founding Engineer 2022년 5월–2024년 12월, xAI Member of Technical Staff 2025년 1월–2026년 4월이 적혀 있다.[^pi]

## 응용 분야

기반 모델을 다양한 계산 환경에서 학습·추론·배포하는 시스템, 언어 모델의 저장 공간 절감, 기기 안에서 언어 모델과 자료 검색을 함께 실행하는 도우미, 여러 단계의 작업을 수행하는 에이전트가 연구 대상이다.[^home][^p1][^p4][^p5]

## 구성원

2026년 11월 9일 People의 Students 구획에 게시된 네 명이다. 과정은 게시 표기대로 적었고, 「대표 논문 참여」는 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^people]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Heejun Kim | 석사과정 | 1 |
| JunYoung Lee | Undergraduate Student(학부생) |  |
| SangLyul Cho | Undergraduate Student(학부생) | 1, 2 |
| Seoyoon Yum | Undergraduate Student(학부생) | 4 |

## 최근 논문 목록 (2021–2026)

Publications의 2021–2026년 연도 구역에 게시된 논문과 책의 장 29편이다. 연도·제목·저자·발표처는 연구실의 표기이며, 김세훈의 2026년 8월 KAIST 부임 전 연구가 함께 들어 있다. 2026년의 Preprint 다섯 편은 arXiv 사전 공개본이며 PhaseGate의 NeurIPS 2026 Workshop 표기는 채택이다. 그 밖의 학회·워크숍·학술지 이름은 연구실 기재대로다. 별표는 공동 기여, †는 공동 지도이며 Squeezeformer의 *¹·*²는 서로 다른 공동 기여 묶음이다.[^pubs][^pi][^p4]

**2026**

- Zack Yu\*, Nicholas Lee\*, Minjae Lee, Lakshya Agarwal, Luca Manolache, Wonjun Kang, Matei Zaharia, Michael W. Mahoney, Kurt Keutzer, Sehoon Kim†, Amir Gholami†. "GEPA-Curator: Curated Learning for Self Improving Agents". *Preprint 2026*. DOI: <https://doi.org/10.48550/arxiv.2610.37651>.
- Heejun Kim, Junyoung Lee, SangLyul Cho, Dongsu Han, Insu Han, Sehoon Kim. "ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals". *Preprint 2026*. DOI: <https://doi.org/10.48550/arxiv.2610.10381>.
- Seoyoon Yum, Sehoon Kim. "PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory". *NeurIPS 2026 Workshop (채택)*. DOI: <https://doi.org/10.48550/arxiv.2610.04537>.
- Omin Kwon, JoongWon Shin, Minseo Kim, Kurt Keutzer, Sehoon Kim†, Jae W. Lee†. "SketchSSM: Write to the Full State, Read from a Compact Sketch". *Preprint 2026*. DOI: <https://doi.org/10.48550/arxiv.2609.33051>.
- SangLyul Cho\*, Langqing Cui\*, Sehoon Kim, Dongsu Han, Insu Han. "LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers". *Preprint 2026*. DOI: <https://doi.org/10.48550/arxiv.2609.17184>.

**2025**

- Coleman Hooper\*, Sebastian Zhao\*, Luca Manolache, Sehoon Kim, Michael W. Mahoney, Yakun Sophia Shao, Kurt Keutzer, Amir Gholami. "Multipole Attention for Efficient Long Context Reasoning". *NeurIPS 2025*. DOI: <https://doi.org/10.52202/085713-1255>.
- Coleman Hooper\*, Sehoon Kim\*, Hiva Mohammadzadeh, Monishwaran Maheswaran, June Paik, Michael W. Mahoney, Kurt Keutzer, Amir Gholami. "Squeezed Attention: Accelerating Long Context Length LLM Inference". *ACL 2025*. DOI: <https://doi.org/10.18653/v1/2025.acl-long.1568>.
- Lutfi Eren Erdogan\*, Nicholas Lee\*, Sehoon Kim, Suhong Moon, Hiroki Furuta, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami. "Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks". *ICML 2025*.
- Rishabh Tiwari\*, Haocheng Xi\*, Aditya Tomar\*, Coleman Hooper, Sehoon Kim, Maxwell Horton, Mahyar Najibi, Michael W. Mahoney, Kurt Keutzer, Amir Gholami. "QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache". *ICML 2025*.
- Coleman Hooper, Sehoon Kim, Suhong Moon, Kerem Dilmen, Monishwaran Maheswaran, Nicholas Lee, Michael W. Mahoney, Sophia Shao, Kurt Keutzer, Amir Gholami. "ETS: Efficient Tree Search for Inference-Time Scaling". *Preprint, 2025*. DOI: <https://doi.org/10.48550/arxiv.2502.13575>.

**2024**

- Lutfi Eren Erdogan\*, Nicholas Lee\*, Siddharth Jha\*, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Hooper, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami. "TinyAgent: Function Calling at the Edge". *EMNLP Demo Track 2024*.
- Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W. Mahoney, Yakun Sophia Shao, Kurt Keutzer, Amir Gholami. "KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization". *NeurIPS 2024*. DOI: <https://doi.org/10.52202/079017-0040>.
- Suhong Moon\*, Siddharth Jha\*, Lutfi Eren Erdogan, Sehoon Kim, Woosang Lim, Kurt Keutzer, Amir Gholami. "Efficient and Scalable Estimation of Tool Representations in Vector Space". *Preprint, 2024*. DOI: <https://doi.org/10.48550/arxiv.2409.02141>.
- Siddharth Jha, Lutfi Eren Erdogan, Sehoon Kim, Kurt Keutzer, Amir Gholami. "Characterizing Prompt Compression Methods for Long Context Inference". *ICML Workshop 2024*.
- Siddharth Jha, Coleman Hooper, Xiaoxuan Liu, Sehoon Kim, Kurt Keutzer. "Learned Best-Effort LLM Serving". *ICML Workshop 2024*.
- Nicholas Lee\*, Thanakul Wattanawong\*, Sehoon Kim, Karttikeya Mangalam, Sheng Shen, Gopala Anumanchipali, Michael W. Mahoney, Kurt Keutzer, Amir Gholami. "LLM2LLM: Boosting LLMs with Novel Iterative Data Enhancement". *ACL 2024*. DOI: <https://doi.org/10.18653/v1/2024.findings-acl.388>.
- Sehoon Kim\*, Suhong Moon\*, Ryan Tabrizi, Nicholas Lee, Michael W. Mahoney, Kurt Keutzer, Amir Gholami. "An LLM Compiler for Parallel Function Calling". *ICML 2024*.
- Sehoon Kim\*, Coleman Hooper\*, Amir Gholami\*, Zhen Dong, Xiuyu Li, Sheng Shen, Michael W. Mahoney, Kurt Keutzer. "SqueezeLLM: Dense-and-Sparse Quantization". *ICML 2024*.
- Amir Gholami, Zhewei Yao, Sehoon Kim, Coleman Hooper, Michael W. Mahoney, Kurt Keutzer. "AI and Memory Wall". *IEEE Micro Journal Special Issue, 2024*. DOI: <https://doi.org/10.1109/mm.2024.3373763>.

**2023**

- Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Hasan Genc, Kurt Keutzer, Amir Gholami, Sophia Shao. "SPEED: Speculative Pipelined Execution for Efficient Decoding". *NeurIPS Workshop 2023*.
- Sehoon Kim\*, Coleman Hooper\*, Thanakul Wattanawong, Minwoo Kang, Ruohan Yan, Hasan Genc, Grace Dinh, Qijing Huang, Kurt Keutzer, Michael W. Mahoney, Yakun Sophia Shao, Amir Gholami. "Full Stack Optimization of Transformer Inference: A Survey". *ISCA Workshop 2023*.
- Sehoon Kim, Karttikeya Mangalam, Suhong Moon, Jitendra Malik, Michael W. Mahoney, Amir Gholami, Kurt Keutzer. "Speculative Decoding with Big Little Decoder". *NeurIPS 2023*. DOI: <https://doi.org/10.52202/075280-1705>.

**2022**

- Sehoon Kim\*¹, Amir Gholami\*¹, Albert Shaw\*², Nicholas Lee\*², Karttikeya Mangalam, Jitendra Malik, Michael W. Mahoney, Kurt Keutzer. "Squeezeformer: An Efficient Transformer for Automatic Speech Recognition". *NeurIPS 2022*.
- Woosuk Kwon\*, Sehoon Kim\*, Michael W. Mahoney, Joseph Hassoun, Kurt Keutzer, Amir Gholami. "A Fast Post-Training Pruning Framework for Transformers". *NeurIPS 2022*.
- Sehoon Kim\*, Sheng Shen\*, David Thorsley\*, Amir Gholami\*, Woosuk Kwon, Joseph Hassoun, Kurt Keutzer. "Learned Token Pruning for Transformers". *KDD 2022*. DOI: <https://doi.org/10.1145/3534678.3539260>.
- Sehoon Kim, Amir Gholami, Zhewei Yao, Nicholas Lee, Patrick Wang, Anirudda Nrusimha, Bohan Zhai, Tianren Gao, Michael W. Mahoney, Kurt Keutzer. "Integer-only Zero-shot Quantization for Efficient Speech Recognition". *ICASSP 2022*. DOI: <https://doi.org/10.1109/icassp43922.2022.9747552>.
- Shixing Yu\*, Zhewei Yao\*, Amir Gholami\*, Zhen Dong\*, Sehoon Kim, Michael W. Mahoney, Kurt Keutzer. "Hessian-Aware Pruning and Optimal Neural Implant". *WACV 2022*. DOI: <https://doi.org/10.1109/wacv51458.2022.00372>.

**2021**

- Amir Gholami\*, Sehoon Kim\*, Zhen Dong\*, Zhewei Yao\*, Michael W. Mahoney, Kurt Keutzer. "A Survey of Quantization Methods for Efficient Neural Network Inference". *Low-Power Computer Vision book chapter, 2021*. DOI: <https://doi.org/10.1201/9781003162810-13>.
- Taebum Kim, Eunji Jeong, Geon-Woo Kim, Yunmo Koo, Sehoon Kim, Gyeong-In Yu, Byung-Gon Chun. "Terra: Imperative-Symbolic Co-Execution of Imperative Deep Learning Programs". *NeurIPS 2021*.

## 수상과 선정

교수 개인 이력의 2024년 선정 두 건이다. 모두 김세훈의 2026년 8월 KAIST 부임 전 이력이다. 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다.[^pi]

- 2024 · 김세훈, MLCommons ML and Systems Rising Star 선정
- 2024 · 김세훈, NVIDIA Graduate Fellowship Program Finalist 선정

## 연락과 위치

- 연구실 주소: 서울특별시 서초구 태봉로 108, 06764.[^home][^people]
- 교수 사무실: 양재캠퍼스 6층 603호.[^dept]

## 각주
[^home]: SEAL, Home, 연구실 소개와 현재 연구 방향. <https://seal-kaist.github.io/> (관측 2026-11-09).
[^people]: SEAL, People, 교수 소개와 Students. <https://seal-kaist.github.io/people> (관측 2026-11-09).
[^dept]: KAIST 김재철AI대학원, 구성원, 전임교수 김세훈의 직위·연구 분야·사무실. <https://gsai.kaist.ac.kr/people-2/?lang=ko> (관측 2026-11-09).
[^pubs]: SEAL, Publications, 2021–2026년 논문과 저자 기여 기호 설명. <https://seal-kaist.github.io/publications> (관측 2026-11-09).
[^pi]: Sehoon Kim, 개인 소개·학력·경력·선정 이력. <https://sehoonkim.org/> (관측 2026-11-11).
[^aff-loop]: S. Cho 외, LoopSpec, 저자 소속과 공동 기여·교신 표시. <https://arxiv.org/html/2609.17184v1> (관측 2026-11-11).
[^p1]: H. Kim 외, S. Kim, arXiv 사전 공개본 (온라인 2026-10-07). <https://doi.org/10.48550/arxiv.2610.10381> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.10381> (v2, 2026-10-29; 관측 2026-11-11).
[^p2]: S. Cho 외, I. Han, arXiv 사전 공개본 (온라인 2026-09-15). <https://doi.org/10.48550/arxiv.2609.17184> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.17184> (v1, 2026-09-15; 관측 2026-11-11).
[^p3]: O. Kwon 외, J. W. Lee, arXiv 사전 공개본 (온라인 2026-09-27). <https://doi.org/10.48550/arxiv.2609.33051> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.33051> (v2, 2026-10-06; 관측 2026-11-11).
[^p4]: S. Yum, S. Kim, arXiv 사전 공개본; NeurIPS 2026 Workshop (채택) (온라인 2026-10-03). <https://doi.org/10.48550/arxiv.2610.04537> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.04537> (v1, 2026-10-03; 관측 2026-11-11).
[^p5]: Z. Yu 외, A. Gholami, arXiv 사전 공개본 (온라인 2026-10-27). <https://doi.org/10.48550/arxiv.2610.37651> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2610.37651> (v1, 2026-10-27; 관측 2026-11-11).

# 빅데이터 지능 연구실 (Big Data Intelligence Lab, BDI Lab)

**KAIST AI컴퓨팅학과·전산학부 · 황지영 교수**

- 분야: 그래프 기계학습, 딥러닝, 지식 그래프, 데이터 마이닝, 빅데이터 분석, 데이터 과학
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^areas][^p8], 멀티모달 AI[^areas][^p5], 이상·변화점 탐지[^areas][^projects]
- 홈페이지: <https://bdi-lab.kaist.ac.kr/>
- 근거와 출처: [빅데이터 지능 연구실 근거 페이지](bdi-lab-sources.md)

> 데이터를 개체와 개체 사이의 관계로 나타내고 해석하는 그래프 기계학습·데이터 마이닝 알고리즘을 만드는 연구실이다. 교수의 최근 연구 관심은 사람의 지식을 개체와 관계의 연결로 정리한 지식 그래프의 표현 학습과 그래프 신경망이다.[^about][^cslab][^prof]

## 무엇을 연구하나

연구실은 KAIST AI컴퓨팅학과 황지영 교수가 이끄는 연구실이다.[^about] 연구실 누리집은 여러 과학·산업 분야에서 생기는 크고 복잡한 데이터 묶음을 다루는 새로운 계산 알고리즘을 개발하는 데 중점을 두고 데이터 지능의 여러 측면을 기초부터 연구한다고 소개한다. 특히 데이터를 개체 사이의 상호작용으로 나타내고 해석하는 그래프 기계학습(점과 선으로 이루어진 연결망 구조의 데이터에서 배우는 기계학습)과 마이닝(큰 데이터에서 쓸모 있는 패턴을 찾아내는 일) 기술에 집중한다.[^about] 전산학부 연구실 소개는 실생활 곳곳에 흩어진 다양한 데이터에서 유의미한 정보를 뽑아내는 새로운 인공지능·기계학습 알고리즘을 개발하고, 인공지능·그래프 기계학습·데이터 마이닝 분야에서 아직 풀지 못한 문제들을 정형화해 이를 풀 새 알고리즘을 만든다고 적는다.[^cslab]

누리집은 연구 영역을 여섯 가지로 든다.[^areas] 그래프 기계학습에서는 소셜 네트워크·지식 그래프·생물 네트워크처럼 복잡한 관계 데이터에서 배우고 분석하는 알고리즘을 만들고, 시간에 따라 바뀌는 그래프, 사실 하나에 여러 보조 정보가 붙는 초관계 그래프, 여러 종류의 점과 선이 섞인 이종 그래프에서도 견고하고 일반화되게 하는 문제를 다룬다. 지식 그래프에서는 지식 그래프의 구축, 임베딩(개체와 관계를 숫자 벡터로 바꾸는 일), 추론 기술을 연구하고, 기호로 적힌 지식과 신경망 표현을 결합해 귀납적 링크 예측(학습 때 없던 개체 사이의 연결을 예측하는 일)과 질의응답 같은 복잡한 추론으로 넓힌다. 딥러닝에서는 심층 신경망 모델을 효율적이고 규모를 키울 수 있게 설계하며, 최근에는 대형 언어 모델(LLM)과 멀티모달 학습(그림·글처럼 종류가 다른 자료를 함께 배우는 학습)으로 범위를 넓혀 안전성·해석 가능성·도메인 간 적응을 다룬다. 데이터 마이닝에서는 군집화·분류·이상 탐지(평소와 다른 데이터를 찾아내는 일) 알고리즘을 만들고, 구조 패턴과 이상 전파 방식을 활용해 금융 사기 탐지와 웹 스팸 탐지를 겨냥한다. 빅데이터 분석에서는 분산 컴퓨팅 환경에서 거대한 데이터를 처리하는 알고리즘과 시스템을 만들고, 마이크로서비스(작은 서비스 여러 개로 나눠 만든 소프트웨어)의 장애 근본 원인 분석 같은 분석 틀을 개발한다. 데이터 과학에서는 데이터 수집·전처리·시각화·모델링의 전 과정을 다루며 로봇공학부터 공공 정책까지 여러 분야의 학제 간 과제에 참여한다.[^areas]

교수가 2026년 KDD(지식 발견·데이터 마이닝 학회)에서 연 튜토리얼 소개에 따르면, 지식 그래프는 사람의 지식을 구조화해 나타낸 것으로 오늘날 많은 지식 발견 시스템에 꼭 필요하다. 지식 그래프 임베딩과 표현 학습은 개체와 관계를 특징 벡터로 바꿔 데이터 마이닝·기계학습 응용에 넣을 수 있게 하며, 최근 연구는 그래프 구조 데이터로 검색 증강 생성(RAG, 답을 만들기 전에 관련 자료를 찾아 함께 쓰는 방식)을 개선하는 GraphRAG처럼 지식 그래프를 대형 언어 모델과 함께 쓰는 방향도 탐색한다.[^talks]

대표 논문으로 보면 연구는 다섯 갈래로 모인다. 첫째, 학습 때 보지 못한 개체·관계가 나타나는 지식 그래프와 사실에 보조 정보가 붙은 초관계 지식 그래프의 표현 학습이다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 지식 그래프 표현 학습 모델이 처음 보는 데이터에서도 잘 맞을지를 이론으로 따지는 일반화 이론이다(대표 논문 4).[^p4] 셋째, 그림과 글을 함께 쓰는 멀티모달 지식 그래프다(대표 논문 5).[^p5] 넷째, 그래프 신경망(연결망 구조의 데이터를 다루는 신경망)을 사기 탐지와 메시지 전달 구조 개선에 쓰는 연구다(대표 논문 6, 7).[^p6][^p7] 다섯째, 검색 증강 언어 모델의 견고성이다(대표 논문 8).[^p8] 최근 논문 목록에는 마스크 이산 확산으로 초관계 사실을 생성하는 표현 학습(ICML 2026), 귀납적 지식 그래프 완성에서 부분 그래프 추론 모델의 안정성과 일반화 능력(ICML 2025), 자동으로 만든 탈옥 프롬프트(모델의 안전장치를 우회하게 만드는 입력)로 LLM의 안전 취약점을 살피는 연구(Findings of EMNLP 2025), 코드와 지식 그래프로 고칠 코드의 위치를 찾는 다중 에이전트 틀(NeurIPS 2026 게재 예정)도 있다.[^pubs]

## 주요 연구 주제

### 1. 처음 보는 개체·관계와 초관계 사실을 다루는 지식 그래프 표현 학습

관계 그래프로 새 개체와 새 관계의 임베딩을 만드는 귀납적 방법(InGram), 숫자 값이 섞인 초관계 지식 그래프의 트랜스포머 표현 학습(HyNT), 구조만으로 표현을 계산하는 초관계 지식 그래프 학습(MAYPL).[^p1][^p2][^p3] 대표 논문 1, 2, 3.

### 2. 지식 그래프 표현 학습의 일반화 이론

기존 모델을 적어도 15가지 담는 틀 ReED로 지식 그래프 표현 학습의 PAC-베이즈 일반화 한계를 보였다.[^p4] 대표 논문 4.

### 3. 그림과 글을 함께 쓰는 멀티모달 지식 그래프

사실까지 그림으로 설명되는 시각-텍스트 지식 그래프와 그 표현 학습 방법(VISTA).[^p5] 대표 논문 5.

### 4. 그래프 신경망의 응용과 언어 모델의 견고성

사기 패거리의 공격으로 본 그래프 신경망 사기 탐지기의 취약성(MonTi), 언제 어디에 가상 노드를 연결할지 배우는 메시지 전달(MAVN), 서로 충돌하는 검색 문서에 흔들리지 않는 언어 모델.[^p6][^p7][^p8] 대표 논문 6, 7, 8.

## 대표 논문

최근 5년 논문 가운데 황지영 교수가 마지막 저자이자 교신저자(* 표기)인 것에서 연구 갈래마다 고르게 골랐다. 최근 논문 목록의 대부분은 학회 논문이다.[^pubs] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2023 | [InGram: Inductive Knowledge Graph Embedding via Relation Graphs](https://proceedings.mlr.press/v202/lee23c.html) · ICML 2023 | 지식 그래프(개체와 개체 사이의 관계를 주체 개체·관계·대상 개체를 묶은 트리플렛으로 모은 데이터)에서 빠진 사실을 채우는 일 가운데, 학습 때 보지 못한 새 개체에 대한 사실을 예측하는 것을 귀납적 지식 그래프 완성이라 한다. 기존 방법 대부분은 개체는 새로 나타나도 되지만 관계는 새로 나타날 수 없다고 가정해, 새 개체가 새 관계와 함께 나타나는 실제 지식 그래프를 제대로 다루지 못했다. 연구진은 추론 시점에 새 개체뿐 아니라 새 관계의 임베딩도 만들어 내는 InGram을 제안했다. 관계들과 관계 사이의 친밀도 가중치로 이루어진 관계 그래프를 정의하고, 이 관계 그래프와 원래 지식 그래프를 바탕으로 이웃의 임베딩을 어텐션(중요한 정보에 더 큰 가중치를 두는 방식)으로 모아 관계와 개체의 임베딩을 만드는 법을 배운다. 실험에서 InGram은 여러 귀납 학습 상황에서 기존 최고 수준 방법 14가지보다 좋은 성능을 보였다.[^p1] | 1저자 J. Lee, 마지막·교신 저자 황지영 |
| 2 | 2023 | [Representation Learning on Hyper-Relational and Numeric Knowledge Graphs with Transformers](https://doi.org/10.1145/3580305.3599490) · KDD 2023 | 초관계 지식 그래프에서는 하나의 사실(트리플렛)에 관계와 개체로 이루어진 한정어(qualifier)를 여럿 붙여 보조 정보를 줄 수 있다. 기존 초관계 지식 그래프 임베딩 방법은 개체를 모두 따로 떨어진 대상으로 보지만, 어떤 정보는 숫자 값으로 나타내야 한다. 예를 들어 (J.R.R., was born in, 1892) 같은 사실이 있고, (J.R.R., educated at, Oxford Univ.)라는 사실에는 (start time, 1911) 같은 한정어가 붙을 수 있다. 연구진은 사실이나 한정어에 숫자 값이 들어 있는 초관계 지식 그래프의 표현을 배우는 통합 틀 HyNT를 제안했다. 사실과 한정어 사이의 상관관계와 숫자 정보를 함께 바탕으로 표현을 배우도록 문맥 트랜스포머와 예측 트랜스포머(트랜스포머는 어텐션으로 입력 사이의 관계를 계산하는 신경망 구조)를 두고, 사실과 한정어를 간결한 표현으로 바꿔 넣어 트랜스포머의 계산 비용을 줄였다. HyNT로 빠진 개체·관계뿐 아니라 빠진 숫자 값도 예측할 수 있으며, 실제 데이터 묶음에서 기존 최고 수준 방법보다 크게 좋은 성능을 보였다.[^p2] | 공동 1저자 C. Chung·J. Lee(‡), 마지막·교신 저자 황지영 |
| 3 | 2025 | [Structure Is All You Need: Structural Representation Learning on Hyper-Relational Knowledge Graphs](https://proceedings.mlr.press/v267/lee25ah.html) · ICML 2025 | 초관계 지식 그래프(HKG)는 사실(트리플렛)에 보조 정보인 한정어를 붙여 지식 그래프를 넓힌 것이다. 많은 HKG 표현 학습 방법이 나왔지만 HKG의 구조를 잘 활용하지 못하는 경우가 많다. 이 논문은 HKG 위에서 추론하려면 그 구조를 충분히 쓰는 것이 결정적이며, 구조만으로 표현을 배우는 방법으로도 여러 링크 예측 과제에서 최고 수준 성능을 낼 수 있음을 보였다. 제안한 MAYPL은 HKG의 구조를 바탕으로 표현 벡터의 초깃값을 정하는 법을 배우고, 사실 단위의 메시지 계산과 개체 중심·관계 중심의 모으기로 이루어진 어텐션 기반 메시지 전달(이웃끼리 정보를 주고받으며 표현을 갱신하는 방식)로 구조만을 바탕으로 표현을 계산한다. 구조에서 배우기 때문에 새 개체와 새 관계에 대해서도 귀납 추론을 할 수 있다. 10개 데이터 묶음에서 지식 그래프 완성 방법 40가지보다 좋은 성능을 보였다.[^p3] | 1저자 J. Lee, 마지막·교신 저자 황지영 |
| 4 | 2024 | [PAC-Bayesian Generalization Bounds for Knowledge Graph Representation Learning](https://proceedings.mlr.press/v235/lee24i.html) · ICML 2024 | 지난 10년 동안 지식 그래프 표현 학습(KGRL) 방법이 많이 나왔지만 이론 분석은 거의 없었다. 이 논문은 KGRL 방법에 대한 첫 PAC-베이즈 일반화 한계(학습한 모델이 처음 보는 데이터에서 낼 오차가 어디까지일지를 확률적으로 보장하는 이론적 상한)를 내놓았다. 넓은 범위의 KGRL 모델을 분석하려고 관계를 고려하는 메시지 전달 인코더와 사실 분류 디코더로 이루어진 일반 틀 ReED를 제안했는데, 이 틀은 R-GCN·CompGCN 같은 그래프 신경망 기반 모델과 RotatE·ANALOGY 같은 얕은 구조의 모델을 포함해 기존 KGRL 모델을 적어도 15가지 나타낼 수 있다. ReED의 일반화 한계는 KGRL에서 흔히 쓰는 매개변수 공유와 가중치 정규화 같은 기법에 이론적 근거를 주고, 실제 방법을 설계할 때 바람직한 선택을 안내한다. 실제 지식 그래프 세 개에서 일반화 한계의 핵심 요인이 실제 일반화 오차를 설명함을 실험으로 보였다.[^p4] | 1저자 J. Lee, 마지막·교신 저자 황지영 |
| 5 | 2023 | [VISTA: Visual-Textual Knowledge Graph Representation Learning](https://doi.org/10.18653/v1/2023.findings-emnlp.488) · Findings of EMNLP 2023 | 지식 그래프는 주체 개체·관계·대상 개체를 묶은 트리플렛으로 사람의 지식을 나타낸다. 기존 지식 그래프 임베딩 방법 대부분은 지식 그래프의 구조만 보고, 최근 나온 몇몇 멀티모달 방법은 개체의 그림이나 글 설명을 쓴다. 연구진은 개체뿐 아니라 사실(트리플렛)도 그림으로 설명할 수 있고 개체와 관계 모두 글 설명을 갖는 시각-텍스트 지식 그래프(VTKG)를 제안했다. 그림으로 나타낼 수 있는 상식 지식을 모아, 사실 자체가 그림으로 설명되고 개체와 관계의 뜻이 글로 설명된 새 벤치마크 데이터 묶음을 만들었다. 또 개체 인코딩·관계 인코딩·사실 디코딩 트랜스포머로 개체와 관계의 시각·텍스트 표현을 함께 쓰는 지식 그래프 표현 학습 방법 VISTA를 제안했다. 실험에서 VISTA는 실제 VTKG에서 최고 수준의 지식 그래프 완성 방법들보다 좋은 성능을 보였다.[^p5] | 1저자 J. Lee, 5명 중 마지막·교신 저자 황지영 |
| 6 | 2025 | [Unveiling the Threat of Fraud Gangs to Graph Neural Networks: Multi-Target Graph Injection Attacks against GNN-Based Fraud Detectors](https://doi.org/10.1609/aaai.v39i15.33760) · AAAI 2025 | 그래프 신경망(GNN)은 사기 사용자를 가려내고 악성 행위를 찾아내는 사기 탐지에 효과적인 도구가 됐다. 그러나 GNN 기반 사기 탐지기를 노리는 공격과 그 위험은 거의 연구되지 않아 잠재적 위협이 방치돼 왔다. 최근 사기가 점점 패거리나 집단으로 조직된다는 점에 주목해, 연구진은 사기 패거리가 공모해 불법 활동을 위장함으로써 자기 사기 노드(그래프의 점)를 정상으로 잘못 분류되게 하는 공격 시나리오를 설계했다. 스팸 리뷰, 가짜 뉴스, 의료 보험 사기의 세 가지 실제 사기 사례에서 이런 공격을 흉내 내 GNN 기반 사기 탐지기에 대한 적대적 공격을 연구했다. 이 공격을 여러 표적 그래프 주입 공격(그래프에 가짜 노드를 넣어 여러 대상의 판정을 바꾸려는 공격)으로 정의하고, 트랜스포머 기반 공격 모델 MonTi를 제안했다. MonTi는 모든 공격 노드의 속성과 연결을 트랜스포머 인코더로 한꺼번에 만들어, 이를 차례로 만드는 기존 방법 대부분보다 속성과 연결 사이의 상호 의존성을 더 잘 잡는다. 또 공격 노드마다 연결 수 예산을 적응적으로 나눠 다양한 주입 구조를 탐색한다. 실제 그래프 다섯 개에서 기존 최고 수준의 그래프 주입 공격 방법보다 좋은 성능을 보였다.[^p6] | 1저자 J. Choi, 마지막·교신 저자 황지영 |
| 7 | 2026 | [Learn When and Where to Connect: Adaptive Virtual Nodes for Dynamic Message Passing on Graphs](https://doi.org/10.1145/3770855.3818013) · KDD 2026 | 메시지 전달 신경망(MPNN, 그래프의 노드들이 이웃과 정보를 주고받으며 표현을 갱신하는 신경망)에서는 메시지 전달을 돕기 위해 가상 노드(VN, 실제 데이터에는 없지만 여러 노드를 이어 주려고 덧붙이는 노드)를 자주 쓴다. 그런데 기존 방법은 모든 노드가 같은 수의 가상 노드에 연결되도록 묶고, MPNN을 적용하기 전에 연결을 고정하며, 같은 가상 노드에 연결되는 다른 노드와 상관없이 연결을 정하는 한계가 있다. 연구진은 노드와 가상 노드 사이의 연결에 제약을 두지 않고, 층을 거치며 바뀌는 노드 표현에 따라 필요할 때 가상 노드를 들여오는 MAVN을 제안했다. MAVN은 연결의 상대적 중요도에 따라 언제(어느 층에서), 어디에(어느 노드에) 가상 노드를 들여와 연결할지 스스로 배우며, 노드와 가상 노드가 서로를 얼마나 선호하는지를 함께 보는 점수 방식으로 층마다 필요한 가상 노드를 후보 가운데서 고른다. 어떤 연결 패턴이든 이를 흉내 내는 MAVN 매개변수가 있음을 이론으로 증명했고, 실제 데이터 묶음 아홉 개에서 바탕 MPNN의 성능을 꾸준히 높여 최대 46.5% 개선했으며 비교 방법들보다 좋은 성능을 보였다.[^p7] | 1저자 J. Lee, 마지막·교신 저자 황지영 |
| 8 | 2024 | [Why So Gullible? Enhancing the Robustness of Retrieval-Augmented Models against Counterfactual Noise](https://doi.org/10.18653/v1/2024.findings-naacl.159) · Findings of NAACL 2024 | 검색 증강 언어 모델(질문에 맞는 문서를 찾아 함께 읽고 답하는 언어 모델) 대부분은 찾아온 문서를 질문과 관련 있는 것과 없는 것으로만 나눈다. 연구진은 관련 있는 문서조차 잘못되거나 오해를 부르는 정보를 담아, 찾아온 문서끼리 충돌하고 모델의 판단을 흔드는 잡음이 되는 더 어려운 상황을 살폈다. 기존 언어 모델은 미세 조정과 문맥 속 소수 예시 학습 모두에서 충돌하는 정보에 크게 취약했다. 연구진은 판별기를 따로 미세 조정하거나 GPT-3.5가 판별 능력을 끌어내도록 프롬프트를 주는 방식으로 문서 사이의 지식 충돌을 다루는 방법을 제안했고, 열린 영역 질의응답에서 이 방법들이 모델의 견고함을 크게 높였다. 또 미세 조정한 판별기의 판단을 문맥 속 학습 과정에 넣어 두 학습 방식의 장점을 함께 쓰는 방법을 제시했고, 이 방향의 연구를 위해 기계로 만든 충돌 유발 데이터 묶음 MacNoise를 내놓았다.[^p8] | 공동 1저자 G. Hong·J. Kim·J. Kang(‡), 5명 중 마지막·교신 저자 황지영 |

## 교수와 전문 분야

황지영 교수(Joyce Jiyoung Whang)는 KAIST AI컴퓨팅학과 부교수(Associate Professor)이고, 전산학부·김재철AI대학원·데이터사이언스대학원(GSDS)의 겸임교수(Adjunct Professor)다.[^prof] AI컴퓨팅학과 교수진 목록은 직위를 전임교수로, 전산학부 교수 소개는 부교수로, 전기및전자공학부 교수 소개는 겸임교수로 적는다.[^aic][^cs][^ee] 전산학부와 전기및전자공학부 교수 소개는 연구 분야를 인공지능·정보서비스와 소셜 컴퓨팅으로 적고, 전산학부 교수 소개는 전공을 인공지능, 데이터 마이닝, 기계학습으로 적는다.[^cs][^ee] 데이터사이언스대학원 명단은 분야(Focus Area)를 데이터사이언스 방법론으로 적고,[^gsds] 반도체시스템공학과 연구실 목록에도 빅데이터 지능 연구실이 올라 있다.[^sse]

교수는 2015년 12월 미국 텍사스 오스틴 대학교(The University of Texas at Austin)에서 Inderjit S. Dhillon 교수의 지도로 컴퓨터과학 박사 학위를 받았다. 2016년 3월부터 2020년 6월까지 성균관대학교 조교수로 빅데이터 연구실을 이끌었고, 2020년 7월 KAIST에 와 빅데이터 지능 연구실을 이끌고 있다.[^cs][^prof] 연구실 누리집은 교수가 ICML·NeurIPS·ICLR의 Area Chair, KDD 2026의 workshop chair, 학술지 ACM Transactions on Knowledge Discovery from Data(TKDD)의 associate editor를 맡고 있다고 적는다. 교수의 주된 연구 관심은 그래프 기계학습과 데이터 마이닝이며, 여러 분야의 그래프 모델을 위한 새로운 계산 알고리즘 개발에 집중하고, 최근에는 지식 그래프 표현 학습과 그래프 신경망에 관심을 둔다.[^prof]

교수는 지식 그래프 표현 학습을 주제로 2025년 IEEE BigComp, 2025년 국제 시맨틱 웹 학회(ISWC), 2026년 KDD에서 튜토리얼을 열었다. 초청 강연으로는 The University of Edinburgh(2024), Samsung Global Research(2025), The University of North Carolina at Chapel Hill(2026), KDD 2026 Data Day, New York University(2026) 강연이 누리집에 올라 있다.[^talks]

논문으로 보면 전문 분야는 다섯 갈래다. 첫째, 새 개체·관계와 초관계 사실을 다루는 지식 그래프 표현 학습이다(대표 논문 1–3).[^p1][^p2][^p3] 둘째, 지식 그래프 표현 학습의 일반화 이론이다(대표 논문 4).[^p4] 셋째, 그림과 글을 함께 쓰는 멀티모달 지식 그래프다(대표 논문 5).[^p5] 넷째, 그래프 신경망의 사기 탐지 응용과 메시지 전달 구조다(대표 논문 6, 7).[^p6][^p7] 다섯째, 검색 증강 언어 모델의 견고성이다(대표 논문 8).[^p8] 누리집 논문 목록의 2020년까지 논문으로는 겹치는 군집을 찾는 군집화(Non-exhaustive, Overlapping k-means, SDM 2015 등), 겹치는 커뮤니티 탐지(CIKM 2013, TKDE 2016), 웹 스팸 탐지(Anti-TrustRank) 연구가 있다.[^pubs]

## 응용 분야

대표 논문이 든 쓰임은 다음과 같다. 사기 패거리 공격 연구는 스팸 리뷰, 가짜 뉴스, 의료 보험 사기의 실제 사례로 공격을 흉내 냈고,[^p6] 검색 증강 언어 모델 연구는 열린 영역 질의응답에서 모델의 견고함을 높였다.[^p8] HyNT는 지식 그래프에서 빠진 숫자 값을 예측할 수 있게 한다.[^p2]

누리집 과제 목록에 따르면 연구실은 기업·기관과 함께 다음 주제의 과제를 맡아 왔다.[^projects] 삼성전자와는 반도체 공정 데이터의 다각적 분석을 위한 지식 그래프 모델링(2020–2023), AI 에이전트 기반 Omni Knowledge Graph 구축과 활용 기술(2025–2030), 코드베이스를 포괄적으로 이해하는 그래프 AI 에이전트(2025–2027)를 다룬다. LG전자와는 지식 그래프 기반 콘텐츠 추천(2026)을, Kyobo & DPLANEX와는 그래프 신경망 기반 보험사기 예측(2022–2025)과 개인 맞춤형 서비스를 위한 멀티모달 크로스 도메인 추천 시스템(2024–2025)을 맡았다. DevStack과는 거대언어모델과 지식그래프로 컨테이너(프로그램을 실행 환경째 묶은 단위)로 운영하는 오픈스택(클라우드 환경을 만드는 공개 소프트웨어)과 쿠버네티스(K8s, 여러 컨테이너를 자동으로 배치·관리하는 소프트웨어)의 장애 원인을 분석하고 대응 방안을 제시하는 기술(2024, 2025)을, Telecommunications Technology Association(TTA)과는 생성형 AI의 안정성 평가체계와 AI 위험 분야별 안전성 평가 데이터셋 로드맵(2024)을 연구했다.[^projects]

## 구성원

2026년 10월 22일 연구실 누리집 Members 절 기준이다. Ph.D. Students와 M.S. Students 칸의 구성원이며, 과정과 시작 시점은 누리집 표기를 옮겼다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Chanyoung Chung (정찬영) | 석박사통합과정 (M.S./Ph.D. Integrated Program in School of Computing) | Mar. 2022 ~ | 1, 2, 5 |
| Jaejun Lee (이재준) | 박사과정 (Ph.D. Program in School of Computing) | Mar. 2023 ~ | 1, 2, 3, 4, 5, 7 |
| Heehyeon Kim (김희현) | 박사과정 (Ph.D. Program in School of Computing) | Sep. 2024 ~ | 6 |
| Minsung Hwang (황민성) | 박사과정 (Ph.D. Program in School of Computing) | Sep. 2024 ~ | 4 |
| Kyeongryul Lee (이경률) | 박사과정 (Ph.D. Program in School of Computing) | Mar. 2026 ~ |  |
| Donggyu Yoon (윤동규) | 석사과정 (M.S. Program in School of Computing) | Mar. 2025 ~ |  |
| Kidong Nam (남기동) | 석사과정 (KT-AI M.S. Program in School of Computing) | Mar. 2025 ~ |  |
| Jeemin Kim (김지민) | 석사과정 (M.S. Program in School of Computing) | Mar. 2026 ~ |  |
| Seheon Kim (김세헌) | 석사과정 (M.S. Program in School of Computing) | Mar. 2026 ~ |  |
| Suhyeon Lim (임수현) | 석사과정 (KT-AI M.S. Program in School of Computing) | Mar. 2026 ~ |  |
| Min Park (박민) | 석사과정 (M.S. Program in AI Computing) | Aug. 2026 ~ |  |
| Woo Jin Kim (김우진) | 석사과정 (M.S. Program in Graduate School of Data Science) | Aug. 2026 ~ |  |

## 졸업생과 이전 구성원

누리집 Members 절 Alumni 칸의 8명이다. 학위·연도와 학위 논문 제목은 누리집 표기다. Jaejun Lee, Heehyeon Kim, Minsung Hwang, Kyeongryul Lee는 석사 학위 뒤 같은 연구실 박사과정 구성원으로 위 표에도 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Jaejun Lee (이재준) | M.S. in Computing, KAIST (Feb. 2023) |  | Image-based Augmented Knowledge Graph Embedding |
| Seunghwan Kong (공승환) | M.S. in Computing, KAIST (Feb. 2023) |  | Representation Learning on Knowledge Graphs with Entity Types |
| Heehyeon Kim (김희현) | M.S. in Computing, KAIST (Aug. 2024) |  | Fraud Detection Using Graph Neural Networks |
| Minsung Hwang (황민성) | M.S. in Computing, KAIST (Aug. 2024) |  | Theoretical Generalization Bounds for Knowledge Graph Representation Learning |
| Jinhyeok Choi (최진혁) | M.S. in Computing, KAIST (Feb. 2025) |  | Spatio-Temporal Graph Forecasting by Modeling Long-Range Dependency via Selective State Spaces |
| Junho Park (박준호) | M.S. in Computing, KAIST (Feb. 2025) |  | Root Cause Analysis for Microservice Systems with Resource-Sharing Dependencies |
| Kyeongryul Lee (이경률) | M.S. in Data Science, KAIST (Feb. 2026) |  | Probing Safety Vulnerabilities in Large Language Models and Multimodal Models via Auto-Generated Jailbreak Prompts |
| Minhyeong An (안민형) | M.S. in Computing, KAIST (Feb. 2026) |  | Graph-enhanced Retrieval-Augmented Generation for Microservice Root Cause Analysis with Large Language Models |

## 최근 논문 목록 (2021–2026)

누리집 Selected Publications 절의 2021–2026년 항목으로, 국제 논문(International) 26편과 국내 논문(Domestic) 3편이다. 국제 논문 가운데 2026년 2편은 누리집이 게재 예정(To appear)으로 적는다. 국내 논문은 학회지 이름 뒤에 (국내)를 붙였다. 제목·저자·학회 이름은 누리집 표기 그대로이고, 저자 이름 뒤 ‡는 공동 기여, *는 교신저자 표시다.[^pubs]

**2026**

- C. Chung, J. Kim, and J. J. Whang\*. "Ask KG Agent: A Multi-Agent Framework for Code Localization Using Code and Knowledge Graphs". *To appear in Neural Information Processing Systems (NeurIPS)*.
- C. Chung, M. Hwang, and J. J. Whang\*. "FIETA: Few-Shot Inductive Knowledge Graph Completion via Task-Aware Graph Neural Networks". *To appear in ACM Conference on Information and Knowledge Management (CIKM)*.
- M. Hwang, D. Yoon, K. Jang, G. Hwang, and J. J. Whang\*. "Dialogue Generation for Conversational Recommendation Using User Search Interactions and Knowledge Graphs". *Evaluating and Applying Recommender Systems (EARL) Workshop at Conference on Information and Knowledge Management (CIKM)*.
- D. Yoon‡, M. Hwang‡, J. Baek, D. Shin, and J. J. Whang\*. "Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction". *Knowledge-Enhanced Information Retrieval (KEIR) Workshop at Conference on Information and Knowledge Management (CIKM)*.
- J. Lee and J. J. Whang\*. "Learn When and Where to Connect: Adaptive Virtual Nodes for Dynamic Message Passing on Graphs". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*.
- J. Lee, S. Kim, and J. J. Whang\*. "Generative Representation Learning on Hyper-relational Knowledge Graphs via Masked Discrete Diffusion". *International Conference on Machine Learning (ICML)*.

**2025**

- H. Kim, K. Lee, and J. J. Whang\*. "Beneath the Facade: Probing Safety Vulnerabilities in LLMs via Auto-Generated Jailbreak Prompts". *Findings of the Association for Computational Linguistics: EMNLP (Findings of EMNLP)*.
- J. Lee and J. J. Whang\*. "Structure Is All You Need: Structural Representation Learning on Hyper-Relational Knowledge Graphs". *International Conference on Machine Learning (ICML)*.
- M. Hwang, J. Lee, and J. J. Whang\*. "Stability and Generalization Capability of Subgraph Reasoning Models for Inductive Knowledge Graph Completion". *International Conference on Machine Learning (ICML)*.
- J. Choi, H. Kim, and J. J. Whang\*. "Unveiling the Threat of Fraud Gangs to Graph Neural Networks: Multi-Target Graph Injection Attacks against GNN-Based Fraud Detectors". *AAAI Conference on Artificial Intelligence (AAAI)*.
- C. Chung, K. Lee, S. Park, and J. J. Whang\*. "Unifying Inductive, Cross-Domain, and Multimodal Learning for Robust and Generalizable Recommendation". *Multimodal Generative Search and Recommendation (MMGenSR) Workshop at Conference on Information and Knowledge Management (CIKM)*.
- K. Lee, H. Kim, and J. J. Whang\*. "SAIF: A Comprehensive Framework for Evaluating the Risks of Generative AI in the Public Sector". *AI for Public Missions (AIPM) Workshop at AAAI Conference on Artificial Intelligence (AAAI)*.
- 박준호, 황지영. "Root Cause Analysis for Microservice Systems Using Anomaly Propagation by Resource Sharing (자원 공유에 따른 이상치 전파를 활용한 마이크로서비스 시스템 결함의 근본 원인 분석)". *정보과학회논문지 (Journal of KIISE), 2025년 4월 (국내)*.

**2024**

- J. Lee, M. Hwang, and J. J. Whang\*. "PAC-Bayesian Generalization Bounds for Knowledge Graph Representation Learning". *International Conference on Machine Learning (ICML)*.
- G. Hong‡, J. Kim‡, J. Kang‡, S. Myaeng, and J. J. Whang\*. "Why So Gullible? Enhancing the Robustness of Retrieval-Augmented Models against Counterfactual Noise". *Findings of the Association for Computational Linguistics: NAACL (Findings of NAACL)*.
- J. Choi, H. Kim, M. An, and J. J. Whang\*. "SpoT-Mamba: Learning Long-Range Dependency on Spatio-Temporal Graphs with Selective State Spaces". *Spatio-Temporal Reasoning and Learning (STRL) Workshop at International Joint Conference on Artificial Intelligence (IJCAI)*.

**2023**

- J. Lee, C. Chung, H. Lee, S. Jo, and J. J. Whang\*. "VISTA: Visual-Textual Knowledge Graph Representation Learning". *Findings of Empirical Methods in Natural Language Processing (Findings of EMNLP)*.
- J. Kim‡, G. Hong‡, S. Myaeng, and J. J. Whang\*. "FinePrompt: Unveiling the Role of Finetuned Inductive Bias on Compositional Reasoning in GPT-4". *Findings of Empirical Methods in Natural Language Processing (Findings of EMNLP)*.
- C. Chung‡, J. Lee‡, and J. J. Whang\*. "Representation Learning on Hyper-Relational and Numeric Knowledge Graphs with Transformers". *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*.
- J. Lee, C. Chung, and J. J. Whang\*. "InGram: Inductive Knowledge Graph Embedding via Relation Graphs". *International Conference on Machine Learning (ICML)*.
- C. Chung and J. J. Whang\*. "Learning Representations of Bi-level Knowledge Graphs for Reasoning beyond Link Prediction". *AAAI Conference on Artificial Intelligence (AAAI)*.
- H. Kim, J. Choi, and J. J. Whang\*. "Dynamic Relation-Attentive Graph Neural Networks for Fraud Detection". *Machine Learning on Graphs (MLoG) Workshop at IEEE International Conference on Data Mining (ICDM)*.

**2022**

- J. H. Kwak‡, J. Lee‡, J. J. Whang\*, and S. Jo\*. "Semantic Grasping via a Knowledge Graph of Robotic Manipulation: A Graph Representation Learning Approach". *IEEE Robotics and Automation Letters*.
- S. Wi, S. Woo, J. J. Whang, and S. Son\*. "HiddenCPG: Large-Scale Vulnerable Clone Detection Using Subgraph Isomorphism of Code Property Graphs". *The ACM Web Conference*.
- 공승환, 정찬영, 주수헌, 황지영. "Knowledge Graph Embedding with Entity Type Constraints (개체 유형 정보를 활용한 지식 그래프 임베딩)". *정보과학회논문지 (Journal of KIISE), 2022년 9월 (국내)*.
- 황민성, 황지영. "Knowledge Graph Embedding with Dynamic Attention (동적 어텐션을 이용한 지식그래프 임베딩)". *한국컴퓨터종합학술대회 논문집, 2022년 6월 (국내)*.

**2021**

- C. Chung and J. J. Whang\*. "Knowledge Graph Embedding via Metagraph Learning". *International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)*.
- J. Bum, H. Choo, and J. J. Whang\*. "Image-based Lifelogging: User Emotion Perspective". *Computers, Materials & Continua*.
- J. Bum, J. J. Whang\*, and H. Choo\*. "Sentiment-based Sub-event Segmentation and Key Photo Selection". *Journal of Visual Communication and Image Representation*.

## 특허

누리집 Publications 절 Patents 칸의 1건이다.[^pubs]

- 2025 · 복층 지식 그래프 임베딩 방법 및 그 시스템 (발명자 황지영, 정찬영; 등록번호 10-2834344-0000)

## 과제

누리집 Projects 절의 과제 가운데 기간이 2021년 10월 이후에 걸친 16건이다. 과제 이름·지원 기관·기간·역할은 누리집 표기다.[^projects]

- Responsible Multimodal Graph AI (책임 있는 멀티모달 그래프 인공지능) (기간 Mar. 2025 ~ Feb. 2028; 지원 National Research Foundation of Korea; 역할 Principal Investigator)
- Extendable Graph Representation Learning (확장 가능한 그래프 표현학습) (기간 Mar. 2022 ~ Feb. 2025; 지원 National Research Foundation of Korea; 역할 Principal Investigator)
- MARS Artificial Intelligence Integrated Research Center (MARS 인공지능 통합연구센터) (기간 Aug. 2018 ~ Feb. 2024; 지원 National Research Foundation of Korea)
- Semi-Supervised Multi-View Learning with Graphs (다각적 데이터 융합을 통한 그래프기반 준지도 학습) (기간 Mar. 2019 ~ Feb. 2022; 지원 National Research Foundation of Korea; 역할 Principal Investigator)
- AI Agent-based Omni Knowledge Graph Construction and its Applications (AI Agent 기반 Omni Knowledge Graph 구축 및 활용 기술 개발) (기간 Oct. 2025 ~ Sep. 2030; 지원 Samsung Electronics; 역할 Principal Investigator)
- Graph AI Agents for Comprehensive Codebase Understanding (코드베이스의 포괄적 이해를 위한 그래프 AI 에이전트 연구) (기간 Dec. 2025 ~ Dec. 2027; 지원 Samsung Electronics; 역할 Principal Investigator)
- Knowledge Graph Modeling for Semiconductor Data (반도체 공정 데이터의 다각적 분석을 위한 지식 그래프 모델링) (기간 Sep. 2020 ~ Sep. 2023; 지원 Samsung Electronics; 역할 Principal Investigator)
- Knowledge Graph-based Content Recommendation (지식 그래프 기반 콘텐츠 추천) (기간 Jan. 2026 ~ Dec. 2026; 지원 LG Electronics; 역할 Principal Investigator)
- LG AI STAR Talent Development Program for Leading Large-Scale Generative AI Models in the Physical AI Domain (Physical AI 분야의 거대 생성모델 기술 선도를 위한 LG AI STAR 인재양성 사업) (기간 Jul. 2025 ~ Dec. 2028; 지원 Institute of Information & communications Technology Planning & Evaluation (IITP))
- Development of AI Technology to support Expert Decision-making that can Explain the Reasons/Grounds for Judgment Results based on Expert Knowledge (전문지식 대상 판단결과의 이유/근거를 설명가능한 전문가 의사결정 지원 인공지능 기술개발) (기간 Apr. 2022 ~ Dec. 2026; 지원 Institute of Information & communications Technology Planning & Evaluation (IITP))
- Multimodal Cross-Domain Recommendation Systems for Personalized Services (개인 맞춤형 서비스를 위한 멀티모달 크로스 도메인 추천 시스템) (기간 Dec. 2024 ~ Nov. 2025; 지원 Kyobo & DPLANEX; 역할 Principal Investigator)
- GNN-based Insurance Fraud Detection (그래프 신경망(GNN) 기반 보험사기 예측 연구) (기간 Aug. 2022 ~ Nov. 2025; 지원 Kyobo & DPLANEX; 역할 Principal Investigator)
- 생성형 AI의 기술 혁신에 대응 가능한 안정성 평가체계 수립 연구 (기간 Oct. 2024 ~ Dec. 2024; 지원 Telecommunications Technology Association (TTA); 역할 Principal Investigator)
- AI 위험 분야별 안전성 평가를 위한 데이터셋 로드맵 구축 (기간 Oct. 2024 ~ Dec. 2024; 지원 Telecommunications Technology Association (TTA); 역할 Principal Investigator)
- Development of a Technology for Analyzing Root Causes and Proposing Countermeasures for Containerized OpenStack Service’s Failures Using LLM and Knowledge Graphs (거대언어모델 및 지식그래프를 활용하여 컨테이너화된 오픈스택 장애원인 분석 및 대응방안 제시 기술개발) (기간 Mar. 2025 ~ Nov. 2025; 지원 DevStack; 역할 Principal Investigator)
- Development of Intelligent Kubernetes Fault Cause Analysis and Response Proposal Method Using LLM and Knowledge Graphs (LLM 및 지식그래프를 활용한 지능형 K8s 장애 원인 분석 및 대응 방안 제시 기술 개발) (기간 May 2024 ~ Nov. 2024; 지원 DevStack; 역할 Principal Investigator)

## 강연과 튜토리얼

누리집 Talks 절에서 2021년 10월부터 2026년 10월 사이의 튜토리얼 3건과 초청 강연 5건이다. 날짜·제목·행사 이름은 누리집 표기다.[^talks]

**튜토리얼**

- 2026-08 · Knowledge Discovery with Knowledge Graphs: From Structural Embeddings to Generative Reasoning (KnowKG) · SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2026)
- 2025-11 · Key Facets in Modern Knowledge Graph Representation Learning (KeyKGRL) · International Semantic Web Conference (ISWC 2025)
- 2025-02 · Representation Learning on Knowledge Graphs · IEEE International Conference on Big Data and Smart Computing (BigComp)

**초청 강연**

- 2026-10 · Beyond Static Memorization: Structural Inference and Generative Reasoning in Knowledge Graphs · New York University
- 2026-08 · Connect Data, Discover Knowledge: Empowering AI with Graph Intelligence · SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), Data Day
- 2026-06 · From Memorization to Understanding: Structural Representation Learning on Knowledge Graphs · The University of North Carolina at Chapel Hill
- 2025-09 · AI Agents and Graph Machine Learning: Towards an Interconnected World · Samsung Global Research
- 2024-07 · Knowledge Graph Representation Learning with Multimodality, Structure, and Theoretical Grounds · The University of Edinburgh

## 연락과 위치

- 교수연구실: KAIST N1 Building 905호, 전화 042-350-3584[^contact][^cs]
- 연구실: KAIST N1 Building 921호, 전화 042-350-7784[^contact][^cslab]
- 교수 이메일: jjwhang@kaist.ac.kr[^aic]
- 주소: KAIST 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea[^contact]
- 누리집 Recruit 절은 석사 신입생과 학부 연구생 모집을 안내한다.[^contact]
[^p1]: J. Lee, C. Chung, J. J. Whang, Proceedings of the 40th International Conference on Machine Learning, PMLR 202, 18796–18809 (2023). <https://proceedings.mlr.press/v202/lee23c.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p2]: C. Chung, J. Lee, J. J. Whang, Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 310-322 (온라인 2023-08-04). <https://doi.org/10.1145/3580305.3599490> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Lee, J. J. Whang, Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 33765–33783 (2025). <https://proceedings.mlr.press/v267/lee25ah.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p4]: J. Lee, M. Hwang, J. J. Whang, Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 26589–26620 (2024). <https://proceedings.mlr.press/v235/lee24i.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: J. Lee 외, J. Whang, Findings of the Association for Computational Linguistics: EMNLP 2023, 7314-7328 (2023). <https://doi.org/10.18653/v1/2023.findings-emnlp.488> 초록 기준(학회 논문집 페이지 게시 초록).
[^p6]: J. Choi, H. Kim, J. J. Whang, Proceedings of the AAAI Conference on Artificial Intelligence 39, 16028-16036 (온라인 2025-04-11). <https://doi.org/10.1609/aaai.v39i15.33760> 초록 기준.
[^p7]: J. Lee, J. J. Whang, Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 2485-2496 (온라인 2026-08-08). <https://doi.org/10.1145/3770855.3818013> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: G. Hong 외, J. Whang, Findings of the Association for Computational Linguistics: NAACL 2024, 2474-2495 (2024). <https://doi.org/10.18653/v1/2024.findings-naacl.159> 초록 기준(Semantic Scholar 등록 초록).
[^about]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> About 절 소개문 (2026-10-22 열람)
[^areas]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> About 절 Research Areas의 연구 영역별 설명(Graph Machine Learning, Deep Learning, Knowledge Graphs, Data Mining, Big Data Analytics, Data Science) (2026-10-22 열람)
[^prof]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Professor 절(직위, 학력, 연구 관심, Biography) (2026-10-22 열람)
[^members]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Members 절(Ph.D. Students, M.S. Students, Alumni) (2026-10-22 열람)
[^pubs]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Selected Publications 절(International, Domestic, Patents) (2026-10-22 열람)
[^talks]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Selected Talks 절(Tutorials, Invited Talks와 강연 소개문) (2026-10-22 열람)
[^projects]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Projects 절 (2026-10-22 열람)
[^contact]: 연구실 누리집 <https://bdi-lab.kaist.ac.kr/> Recruit 절과 Location (2026-10-22 열람)
[^cs]: KAIST 전산학부 교수 소개(황지영) <https://cs.kaist.ac.kr/people/view?idx=605&kind=faculty&menu=160> (직위, 연구분야, 전공, 학위, 교수연구실, 소개문, 2026-10-22 열람)
[^cslab]: KAIST 전산학부 연구실 소개(빅데이터 지능 연구실) <https://cs.kaist.ac.kr/research/labView?sn=109&menu=64> (2026-10-22 열람)
[^aic]: KAIST AI컴퓨팅학과 교수진 <https://aicollege.kaist.ac.kr/aic/faculty> (2026-10-22 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(황지영) <https://ee.kaist.ac.kr/professor/%ed%99%a9%ec%a7%80%ec%98%81/> (2026-10-22 열람)
[^gsds]: KAIST 데이터사이언스대학원 사람들 <https://gsds.kaist.ac.kr/people> (2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)

# 가변적 기계학습 알고리즘 연구실 (FlexML Lab, Flexible Machine Learning Lab)

**KAIST 전기및전자공학부 · 한인수 교수**

- 분야: 효율적 기계학습(Efficient ML), 모델 압축과 양자화, 빠른 추론과 실행 최적화, 대형 언어 모델의 효율화(어텐션 근사·KV 캐시·추측 디코딩), 대규모 기계학습을 위한 근사 알고리즘
- 대분야: 컴퓨팅·AI
- 태그: 대형 언어 모델[^research][^p2][^p4], AI 시스템·인프라[^research][^p1], 생성 인공지능[^p1], 과학·공학 AI[^p3]
- 홈페이지: <https://flexml.kaist.ac.kr/> (교수 개인 누리집 <https://insuhan.github.io/>)
- 근거와 출처: [FlexML Lab 근거 페이지](insuhan-sources.md)

> 대형 언어 모델 같은 큰 인공지능 모델을 더 빠르게, 더 적은 메모리로 돌리는 기계학습 알고리즘을 이론적 바탕 위에서 만들고 분석하는 연구실이다. 모델 압축과 양자화, 실제 장치에서의 빠른 추론, 대형 언어 모델의 효율화를 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 한인수 조교수의 연구실이다.[^ee][^people] 누리집 이름은 FlexML Lab(Flexible Machine Learning Lab)이고, 반도체시스템공학과 연구실 목록과 교수진 목록은 국문 이름 「가변적 기계학습 알고리즘 연구실」로 적는다.[^home][^ssel][^ssep] 전기및전자공학부 교수 소개는 주요 연구를 대규모 기계학습을 위한 근사 알고리즘(Approximate algorithms for largescale machine learning)과 파운데이션 모델(foundation model, 여러 일에 두루 쓰도록 많은 데이터로 미리 학습한 큰 인공지능 모델)의 효율적 추론(Efficient inference of foundation models)으로 적는다.[^ee]

누리집 첫 화면은 연구실의 방향을 빠르고(fast), 메모리를 적게 쓰고(memory-efficient), 실제로 배치할 수 있는(deployable) 기계학습으로 요약한다.[^home] 이론적 바탕에서 착안해 빠르고 메모리 효율이 높은 기계학습 알고리즘을 만들고 분석해, 인공지능 모델을 효율적으로 배치(deployment, 학습을 마친 모델을 실제 서비스나 장치에서 돌리도록 올리는 일)하는 것이 목표다.[^home] 연구 페이지는 빠르고 메모리 효율이 높은 기계학습을 위한 기본 알고리즘과 이론 틀을 만드는 데 집중한다고 적고, 연구 갈래로 모델 압축과 양자화(quantization, 숫자를 더 적은 비트로 나타내 저장 공간과 계산을 줄이는 방법), 빠른 추론과 실행 최적화, 대형 언어 모델의 효율화 세 가지를 든다.[^research]

연구실 논문이 다루는 문제의 한 예는 대형 언어 모델의 메모리다. 대형 언어 모델은 긴 문맥을 다룰 때 KV 캐시(Key-Value cache, 앞서 처리한 토큰의 키·값 벡터를 저장해 두고 다시 쓰는 메모리)에 많은 메모리를 쓰고, 이를 줄이는 흔한 방법이 양자화다.[^p4] 연구실은 이런 문제에서 양자화 방법(대표 논문 4, 6), 어텐션(attention, 트랜스포머 모델이 입력의 각 토큰을 다른 토큰들과 얼마나 관련지을지 계산하는 연산) 계산을 적은 메모리로 근사하는 알고리즘(대표 논문 5), 생성 속도를 높이는 추측 디코딩(speculative decoding, 가벼운 초안 모델이 다음 토큰들을 먼저 제안하고 원래 모델이 이를 검증해 글 생성을 빠르게 하는 방법, 대표 논문 2), 영상 생성 모델의 희소 어텐션(모든 토큰 쌍이 아니라 골라 낸 일부 쌍만 계산하는 어텐션, 대표 논문 1)을 내놓았다.[^p1][^p2][^p4][^p5][^p6] 연구실 누리집 소식은 대표 논문 5가 NeurIPS 2025에, 대표 논문 4가 AISTATS 2026에, 대표 논문 2·3이 ICML 2026에 채택됐다고 알리며, ICML 2026 논문 두 편에는 연구실 석사과정 학생이 저자로 참여했다.[^home][^pubs][^people]

## 주요 연구 주제

### 1. 모델 압축과 양자화

모델 크기와 추론 비용을 정확도 손실을 적게 하면서 크게 줄이는 새 양자화 기법과 가지치기(pruning, 모델에서 덜 중요한 연결이나 값을 덜어 내는 방법) 방법을 연구한다.[^research] 연구 페이지는 이 갈래의 낱말로 INT4/INT8(정수 4비트·8비트 표현), 극좌표 변환(Polar Transform), 희소성(Sparsity)을 든다.[^research] 대형 언어 모델의 KV 캐시를 극좌표로 바꿔 각도를 양자화하는 방법과, 멀티모달 대형 언어 모델의 KV 캐시를 1비트로 양자화하는 방법이 이 갈래의 논문이다. 대표 논문 4, 6.[^p4][^p6]

### 2. 빠른 추론과 실행 최적화

실제 장치에서 지연 시간을 줄이고 처리량을 높여 배치하도록, 하드웨어를 고려한 추론 알고리즘과 메모리 효율이 높은 실행 시스템을 연구한다.[^research] 연구 페이지는 이 갈래의 낱말로 지연 시간(Latency), 처리량(Throughput), GPU·엣지 장치(GPU/Edge)를 든다.[^research] 영상 생성 모델의 희소 어텐션을 현대 GPU 커널의 고정된 타일 구조에 맞춘 연구와, 하드웨어별 층 지연 시간을 모형화해 추측 디코딩의 초안 모델을 고르는 연구가 이 갈래와 이어진다. 대표 논문 1, 2.[^p1][^p2]

### 3. 대형 언어 모델의 효율화

어텐션 근사, KV 캐시 최적화, 추측 디코딩으로 대형 언어 모델을 실제로 배치할 수 있도록 효율을 높인다.[^research] 연구 페이지는 이 갈래의 낱말로 LLM, KV Cache, Attention을 든다.[^research] 어텐션 계산을 적은 메모리로 근사하는 스트리밍 알고리즘, KV 캐시 양자화, 층을 건너뛰는 자기 추측 디코딩이 이 갈래의 논문이다. 대표 논문 2, 4, 5.[^p2][^p4][^p5]

## 대표 논문

한인수 교수가 KAIST 소속으로 저자에 오른 2025–2026년 논문 가운데 초록을 확인할 수 있는 여섯 편을 연구 갈래마다 골랐다. 1번은 누리집이 NeurIPS 2026으로 적은 논문으로, 서지와 초록은 2026년 7월의 arXiv 사전 공개본이다. 6번은 학회 워크숍 발표다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs][^pdf] |
|---|---|---|---|---|
| 1 | 2026 | [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012) · arXiv 사전 공개본, 2026 (누리집 학회 표기 NeurIPS 2026) | 영상을 만드는 비디오 확산 트랜스포머(잡음에서 시작해 단계마다 잡음을 걷어 내며 영상을 만드는 트랜스포머 모델)는 고화질 영상을 만들지만, 셀프 어텐션의 계산량이 입력 길이의 제곱에 비례해 늘어 긴 영상을 만들기 어렵다. 비슷한 토큰을 묶어 계산을 줄이는 군집 기반 희소 어텐션이 있으나, 군집을 찾는 부담이 크고 군집이 만드는 불규칙한 블록 때문에 GPU의 연산 묶음(CTA, Cooperative Thread Array)을 잘 채우지 못한다. 이 논문은 추가 학습 없이 쓰는 희소 어텐션 틀 HVA를 내놓았다. 영상 토큰이 시간·공간으로 가까운 성질을 이용해 군집 중심을 정해진 이웃 범위에서만 찾게 하고(전용 Triton 커널로 구현), 기준 단계에서만 전체 군집을 계산하고 그 사이 단계에서는 일부 토큰만 갱신하며, 하드웨어 실행 비용을 줄이도록 군집을 병렬로 합친다. 글로 영상을 만드는 실험에서 기존 무학습 희소 어텐션보다 화질을 높이면서 전체 지연 시간을 최대 2.13배 줄였다.[^p1] | 1저자 Dongyeun Lee, 마지막 저자 한인수(Junmo Kim과 함께 교신저자) |
| 2 | 2026 | [KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem](https://arxiv.org/abs/2602.20217) · ICML 2026 | 자기 추측 디코딩(SSD)은 대형 언어 모델의 일부 층을 건너뛴 초안 모델로 생성을 빠르게 하는데, 기존 방법은 고정된 규칙에 기대어 긴 문맥에서 어텐션 계산 부담이 달라지는 점을 반영하지 못한다. KnapSpec은 초안 모델의 구성을 고르는 일을 배낭 문제(knapsack problem, 정해진 용량 안에서 고른 물건의 가치 합을 최대로 하는 최적화 문제)로 바꿔, 시간당 생성 토큰 수를 최대로 하는 추가 학습 없는 틀이다. 어텐션 층과 MLP 층을 나눠 하드웨어별 지연 시간을 문맥 길이의 함수로 모형화하고, 병렬 동적 계획법(큰 문제를 작은 부분 문제의 답을 저장해 가며 푸는 방법)으로 그때그때 초안 구성을 정한다. 은닉 상태(신경망 중간 층이 내놓는 값) 사이의 코사인 유사도가 토큰 수락률(초안 모델이 제안한 토큰을 원래 모델이 받아들이는 비율)을 대신하는 지표로 수학적으로 타당함을 이론으로 분석했다. Qwen3·Llama3 실험에서 기존 SSD 방법보다 꾸준히 나았고 실제 시간 기준 최대 1.47배 빨랐으며, 추가 학습 없이 원래 모델의 출력 분포를 해치지 않는다.[^p2] | 공동 1저자 Seongjin Cha·Gyuwan Kim, 마지막 저자·교신저자 한인수 |
| 3 | 2026 | [DNAChunker: Learnable Tokenization for DNA Language Models](https://arxiv.org/abs/2601.03019) · ICML 2026 | DNA 언어 모델은 유전체 서열을 표현하는 데 쓰이는데, 성능이 염기를 모델 입력 단위로 바꾸는 방식에 크게 좌우된다. DNA에는 자연어의 단어 같은 정해진 경계가 없어, 고정된 토큰 나누기는 서열이 밀리거나 일부가 끼어들거나 빠질 때와 짧은 반복이 있을 때 취약하다. DNAChunker는 문맥에 따라 길이가 다른 단위를 만드는 학습형 분할 모듈을 넣은 마스크 DNA 언어 모델(입력 일부를 가리고 맞히도록 학습하는 모델)이다. 기능 요소가 많은 영역은 잘게 나누고 반복되거나 중복된 서열은 압축하도록 배운다. 사람 참조 유전체로 사전 학습해 다섯 벤치마크에서 고정 토큰 나누기를 쓴 기준 모델보다 꾸준히 나았고, 분석 결과 분할이 생물학 정보를 반영하고 돌연변이에 잘 흔들리지 않는 방식으로 학습됐다.[^p3] | 1저자 Taewon Kim, 마지막 저자 한인수(Sungsoo Ahn과 함께 공동 지도 표시) |
| 4 | 2026 | [PolarQuant: Quantizing KV Caches with Polar Transformation](https://arxiv.org/abs/2502.02617) · AISTATS 2026 | 대형 언어 모델은 긴 문맥을 다룰 때 KV 캐시에 키·값 임베딩(자료를 숫자 벡터로 나타낸 것)을 저장하느라 메모리를 많이 쓰고, 이를 줄이려 흔히 양자화를 쓴다. PolarQuant는 무작위 사전 조건화(데이터를 계산 전에 무작위로 변환하는 처리) 뒤 KV 임베딩을 효율적인 재귀 알고리즘으로 극좌표로 바꾸고, 그 각도를 양자화한다. 사전 조건화 뒤 각도의 분포는 좁게 몰리고 해석적으로 계산할 수 있는 형태를 띠어, 기존 양자화가 데이터 블록마다 줄이지 않은 원래 정밀도로 저장해야 했던 영점·스케일 같은 정규화 값이 필요 없어 메모리를 크게 아낀다. 긴 문맥 평가에서 KV 캐시를 4.2배 넘게 압축하면서 비교한 최신 방법들 가운데 가장 좋은 품질 점수를 냈다.[^p4] | 저자 5명(알파벳순) 가운데 첫 번째 한인수, 마지막 Amir Zandieh |
| 5 | 2025 | [Streaming Attention Approximation via Discrepancy Theory](https://doi.org/10.52202/085713-0705) · NeurIPS 2025 | 대형 언어 모델이 긴 문맥에서 토큰을 생성할 때 메모리 요구가 크다는 문제에서 출발해, 토큰 생성의 핵심 계산인 어텐션 근사를 스트리밍(자료를 차례로 한 번 훑으며 적은 메모리만 쓰는 계산 방식)으로 할 때의 복잡도를 연구했다. 주된 결과는 BalanceKV로, Banaszczyk의 벡터 균형 이론에 따라 키·값 토큰 가운데 균형 잡힌 묶음을 고르는 기하학적 과정으로 어텐션 계산을 정해진 오차(ε) 안에서 근사하는 스트리밍 알고리즘이다. 스트리밍 어텐션 계산에 필요한 공간의 하한도 함께 제시했다. 이론적 보장과 함께, 어텐션 근사와 여러 긴 문맥 벤치마크의 전체 성능에서 기존 방법보다 나아진 것을 실험으로 확인했다.[^p5] | 1저자 Ekaterina Kochetkova, 5명 중 3번째 한인수, 마지막 저자 Michael Kapralov |
| 6 | 2025 | [CalibQuant: 1-Bit KV Cache Quantization for Multimodal LLMs](https://arxiv.org/abs/2502.14882) · ICML 2025 LCFM 워크숍 | 멀티모달 대형 언어 모델(MLLM, 글과 이미지 같은 여러 종류의 자료를 함께 다루는 대형 언어 모델)은 여러 응용에서 성능이 좋지만 배치할 때 계산 부담이 크다. KV 캐시는 메모리를 써서 계산을 줄이지만, 캐시가 커지면 처리량이 떨어지고 메모리가 적은 GPU에서 오래 돌리기 어렵다. CalibQuant는 시각 정보를 1비트로 양자화하는 방식에, KV 캐시 고유의 패턴에 맞춘 사후 스케일링과 보정 기법을 더해 메모리와 계산 부담을 함께 줄인다. Triton으로 실행을 최적화해 InternVL 모델에서 처리량을 10배 높였고, 구조를 바꾸지 않고 기존 MLLM에 붙여 쓸 수 있다.[^p6] | 공동 1저자 4명(무작위 순서) 가운데 첫 번째 한인수, 프로젝트 책임 Kun Wan·Wentian Zhao |

## 교수와 전문 분야

한인수 교수(Insu Han)는 KAIST 전기및전자공학부 조교수이고 디비전은 Computer다.[^ee] 전기및전자공학부 교수 소개는 주요 연구분야를 AI & Machine Learning, Information, Communication & Coding으로 적고,[^ee] 반도체시스템공학과 교수진 목록은 연구분야를 '컴퓨터, 인공지능 및 소프트웨어'로 적는다.[^ssep] 연구실 누리집은 교수의 연구 관심을 Efficient ML, Model Compression, Quantization, LLM Optimization, Hardware-aware AI로 적고,[^people] 교수 개인 누리집은 대규모 기계학습과 그 응용을 위한 근사 알고리즘의 설계와 분석에 연구 관심을 둔다고 소개한다.[^prof]

KAIST에서 전기전자공학·수학(부전공) 학사와 전기공학 석사를 받았고, KAIST 전기및전자공학부에서 Jinwoo Shin 교수의 지도로 박사(2021)를 받았다.[^prof][^people][^ee] 2018년 봄 Tel Aviv University에서 Haim Avron 교수와 방문 학생으로, 2019년 여름 Google New York City에서 Jennifer Gillenwater와 연구 인턴으로 일했고, 2019년 Microsoft Research Asia Fellowship을 받았다.[^prof] KAIST에 오기 전에는 Adobe Firefly의 Applied Scientist와 Yale Institute for Foundations of Data Science(FDS)의 박사후연구원을 지냈다.[^prof][^people] 2024년에는 Amin Karbasi, Amir Zandieh와 함께 AI를 더 강력하고 비용 효율적으로 만드는 연구로 Roberts Innovation Fund Award 수상자로 선정됐다.[^prof]

논문 목록으로 보면 2021–2024년(KAIST 부임 전) 논문은 행렬식 점 과정(determinantal point process, 비슷한 항목끼리는 함께 뽑히기 어렵게 해 다양한 부분집합을 고르는 확률 모형)의 샘플링·학습·추론, 신경 탄젠트 커널(neural tangent kernel, 신경망의 학습 과정을 자료 사이의 유사도 함수로 나타낸 것)을 스케치(큰 자료를 무작위로 줄인 요약으로 근사하는 기법)와 무작위 특징으로 근사하는 방법, 대규모 커널 방법(자료 사이의 유사도 함수로 학습하는 기계학습 방법)을 위한 무작위 특징, 트랜스포머 어텐션을 커널 밀도 추정(각 자료 점에 정해진 모양의 함수를 놓고 더해 확률 분포를 추정하는 방법)과 거의 선형 시간(입력 길이에 거의 비례하는 계산 시간) 알고리즘으로 가속하는 방법(KDEformer, HyperAttention)을 제목으로 다룬다.[^pubs] 2025–2026년 KAIST 소속 논문은 위 대표 논문처럼 KV 캐시 양자화, 스트리밍 어텐션 근사, 추측 디코딩, 영상 생성 모델의 희소 어텐션으로 이어진다.[^pubs][^p1][^p2][^p4][^p5]

## 응용 분야

연구 페이지는 연구의 쓰임을 실제 장치(GPU·엣지 장치)에서 지연 시간이 짧고 처리량이 높게 모델을 배치하는 것과, 대형 언어 모델을 실제로 배치할 수 있게 효율을 높이는 것으로 적는다.[^research] 대표 논문은 대형 언어 모델의 긴 문맥 생성(대표 논문 2, 4, 5), 멀티모달 대형 언어 모델(대표 논문 6), 글로 영상을 만드는 비디오 확산 모델(대표 논문 1)에 방법을 적용했다.[^p1][^p2][^p4][^p5][^p6]

2026년 ICML 논문(대표 논문 3)은 사람 참조 유전체로 사전 학습한 DNA 언어 모델에서 염기 서열을 모델 입력 단위로 나누는 방법을 학습하게 해, 언어 모델 기법을 유전체 서열 표현에 적용했다.[^p3]

## 구성원

누리집 Members 페이지의 석사과정(M.S. Students) 4명과 학부생·인턴(누리집 표기 Undergraduate Students/Interns) 2명이다. 과정 칸 괄호 안의 학년과 연구 주제는 페이지 표기 그대로다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Seongjin Cha | 석사과정 (2nd Year) | Self-speculative Decoding, Quantization |  | 2 |
| Langqing Cui | 석사과정 (2nd Year) | KV Cache, Diffusion Language Models |  |  |
| Jihwan Shin | 석사과정 (1st Year) | Diffusion Language Models, DNA Foundation Models |  | 3 |
| Seoungsub Lee | 석사과정 (1st Year) | Efficient AI, Agentic AI | seoungsub@kaist.ac.kr |  |
| Haesung Lee | 학부 연구생 | Vision-Language-Language Model Quantization |  |  |
| Sanghyeok Moon | 학부 연구생 | Time Series Foundation Models |  |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 연도 구역 논문 19편(학회 논문 17편, 학회 워크숍 발표 2편)이다. 교수 개인의 논문 목록이라 교수가 KAIST 박사과정, Yale 박사후연구원, Adobe에 있던 때의 논문이 섞여 있어, 모두 현재 KAIST 연구실의 성과로 묶지 않는다. 저자 순서와 제목·학회 표기는 누리집 그대로이고, *는 누리집이 적은 공동 기여 표시, Oral·Spotlight는 누리집이 적은 발표 형식이다. 2026년 구역의 NeurIPS 2026 논문 한 편은 누리집이 학회 이름과 연도만 적은 항목으로, 출판본 대신 2026년 7월의 arXiv 사전 공개본을 확인해 「arXiv 사전 공개본」으로 표시했다.[^pubs][^p1]

**2026**

- Dongyeun Lee, Amir Zandieh, Vahab Mirrokni, Junmo Kim, Insu Han. "HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion". *Neural Information Processing Systems (NeurIPS 2026)* (arXiv 사전 공개본, 2026).
- Seongjin Cha\*, Gyuwan Kim\*, Dongsu Han, Tao Yang, Insu Han (\* Equal contribution). "KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem". *International Conference on Machine Learning (ICML 2026)*.
- Taewon Kim, Jihwan Shin, Hyomin Kim, Youngmok Jung, Jonhoon Lee, Won-Chul Lee, Sungsoo Ahn, Insu Han. "DNAChunker: Learnable Tokenization for DNA Language Models". *International Conference on Machine Learning (ICML 2026)*.
- Insu Han, Praneeth Kacham, Amin Karbasi, Vahab Mirrokni, Amir Zandieh. "PolarQuant: Quantizing KV Caches with Polar Transformation". *International Conference on Artificial Intelligence and Statistics (AISTATS 2026)*.

**2025**

- Ekaterina Kochetkova, Kshiteej Sheth, Insu Han, Amir Zandieh, Michael Kapralov. "Streaming Attention Approximation via Discrepancy Theory". *Advances in Neural Information Processing Systems (NeurIPS 2025), Spotlight*.
- Daewon Choi, Seunghyuk Oh, Saket Dingliwal, Jihoon Tack, Kyuyoung Kim, Woomin Song, Seojin Kim, Insu Han, Jinwoo Shin, Aram Galstyan, Shubham Katiyar, Sravan Babu Bodapati. "Mamba Drafters for Speculative Decoding". *Conference on Empirical Methods in Natural Language Processing (EMNLP Findings 2025)*.
- Insu Han, Zeliang Zhang, Zhiyuan Wang, Yifan Zhu, Susan Liang, Jiani Liu, Haiting Lin, Mingjie Zhao, Chenliang Xu, Kun Wan, Wentian Zhao. "CalibQuant: 1-Bit KV Cache Quantization for Multimodal LLMs". *International Conference on Machine Learning (ICML 2025) Long Context Foundation Model (LCFM) Workshop*.
- Amir Zandieh\*, Insu Han\*, Vahab Mirrokni, Amin Karbasi (\* Equal Contribution). "ClusterGen: Token Generation in Sublinear Time and Memory". *International Conference on Learning Representations (ICLR 2025) SLLM Workshop*.
- Amir Zandieh, Majid Daliri, Insu Han. "QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead". *Association for the Advancement of Artificial Intelligence (AAAI 2025)*.

**2024**

- Daniel Levine\*, Syed Asad Rizvi\*, Sacha Levy, Nazreen Pallikkavaliyaveetil, David Zhang, Xingyu Chen, Sina Ghadermarzi, Ruiming Wu, Zihe Zheng, Ivan Vrkic, Anna Zhong, Daphne Raskin, Insu Han, Antonio Henrique de Oliveira Fonseca, Josue Ortega Caro, Amin Karbasi, Rahul M. Dhodapkar, David van Dijk. "Cell2Sentence: Teaching Large Language Models the Language of Biology". *International Conference on Machine Learning (ICML 2024)*.
- Insu Han, Rajesh Jayaram, Amin Karbasi, Vahab Mirrokni, David P. Woodruff, Amir Zandieh. "HyperAttention: Long-context Attention in Near-Linear Time". *International Conference on Learning Representations (ICLR 2024)*.

**2023**

- Amir Zandieh, Insu Han, Haim Avron. "Near Optimal Reconstruction of Spherical Harmonic Expansions". *Advances in Neural Information Processing Systems (NeurIPS 2023)*.
- Amir Zandieh, Insu Han, Majid Daliri, Amin Karbasi. "KDEformer: Accelerating Transformers via Kernel Density Estimation". *International Conference on Machine Learning (ICML 2023)*.

**2022**

- Insu Han, Amir Zandieh, Jaehoon Lee, Roman Novak, Amin Karbasi. "Fast Neural Kernel Embeddings for General Activations". *Advances in Neural Information Processing Systems (NeurIPS 2022)*.
- Insu Han, Mike Gartrell, Elvis Dohmatob, Amin Karbasi. "Scalable MCMC Sampling for Nonsymmetric Determinantal Point Processes". *International Conference on Machine Learning (ICML 2022), Oral*.
- Insu Han, Amir Zandieh, Haim Avron. "Random Gegenbauer Features for Scalable Kernel Methods". *International Conference on Machine Learning (ICML 2022), Oral*.
- Insu Han, Mike Gartrell, Jennifer Gillenwater, Elvis Dohmatob, Amin Karbasi. "Scalable Sampling for Nonsymmetric Determinantal Point Processes". *International Conference on Learning Representations (ICLR 2022), Spotlight*.

**2021**

- Insu Han, Amir Zandieh, Haim Avron, Neta Shoham, Chaewon Kim, Jinwoo Shin. "Scaling Neural Tangent Kernels via Sketching and Random Features". *Advances in Neural Information Processing Systems (NeurIPS 2021)*.
- Mike Gartrell, Insu Han, Elvis Dohmatob, Jennifer Gillenwater, Victor-Emmanuel Brunel. "Scalable Learning and MAP Inference for Nonsymmetric Determinantal Point Processes". *International Conference on Learning Representations (ICLR 2021), Oral*.

## 소식

누리집 첫 화면 News & Highlights의 5건(2025년 9월–2026년 5월) 전부다. 날짜는 누리집의 월 단위 표기이고 문구는 누리집 그대로다.[^home]

- May 2026 · Paper · 2 papers (KnapSpec, DNAChunker) are accepted in ICML 2026! (Accepted at ICML 2026)
- Mar 2026 · Join · Jihwan Shin joined the FlexML group. Welcome!
- Jan 2026 · Paper · PolarQuant: Quantizing KV Caches with Polar Transformation (Accepted at AISTATS 2026)
- Sep 2025 · Join · Seongjin Cha and Langqing Cui joined the FlexML group. Welcome!
- Sep 2025 · Paper · Streaming Attention Approximation via Discrepancy Theory (Accepted at NeurIPS 2025 (Spotlight))

## 연락과 위치

- 교수 연구실: IT융합빌딩(N1) 914호[^ee]
- 누리집 첫 화면의 위치 표기: N1 917, KAIST, Daejeon, Korea[^home]
- 연락처(교내 번호): 7477[^ee]
- 교수 이메일: insu.han@kaist.ac.kr[^ee]
[^p1]: D. Lee 외, I. Han, arXiv 사전 공개본 (2026), 누리집 학회 표기 NeurIPS 2026. <https://arxiv.org/abs/2607.03012> 초록 기준(arXiv 판).
[^p2]: S. Cha 외, I. Han, International Conference on Machine Learning (ICML 2026) (2026). <https://arxiv.org/abs/2602.20217> 초록 기준(arXiv 판).
[^p3]: T. Kim 외, I. Han, International Conference on Machine Learning (ICML 2026) (2026). <https://arxiv.org/abs/2601.03019> 초록 기준(arXiv 판).
[^p4]: I. Han 외, A. Zandieh, International Conference on Artificial Intelligence and Statistics (AISTATS 2026) (2026). <https://arxiv.org/abs/2502.02617> 초록 기준(arXiv 판).
[^p5]: E. Kochetkova 외, M. Kapralov, Advances in Neural Information Processing Systems 38, 23731-23768 (2025). <https://doi.org/10.52202/085713-0705> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: I. Han 외, W. Zhao, International Conference on Machine Learning (ICML 2025) Long Context Foundation Model (LCFM) Workshop (2025). <https://arxiv.org/abs/2502.14882> 초록 기준(arXiv 판).
[^home]: 가변적 기계학습 알고리즘 연구실(FlexML Lab) 누리집 첫 화면 <https://flexml.kaist.ac.kr/> (소개문, 모집 안내, News & Highlights, 위치, 2026-10-23 열람)
[^people]: FlexML Lab 누리집 Members 페이지 <https://flexml.kaist.ac.kr/people> (교수 소개, 석사과정·학부생·인턴, 2026-10-23 열람)
[^research]: FlexML Lab 누리집 Research 페이지 <https://flexml.kaist.ac.kr/research> (세 연구 갈래와 낱말, 2026-10-23 열람)
[^pubs]: FlexML Lab 누리집 Publications 페이지 <https://flexml.kaist.ac.kr/publications/> (연도별 논문 목록, 2026-10-23 열람)
[^prof]: 한인수 교수 개인 누리집 <https://insuhan.github.io/> (About Me, Publications, Research experiences, 2026-10-23 열람)
[^ee]: KAIST 전기및전자공학부 교수 소개(한인수) <https://ee.kaist.ac.kr/professor/%ed%95%9c%ec%9d%b8%ec%88%98/> (직위, 주요 연구분야, 주요 연구, 위치, 연락처, 이메일, 웹사이트, 디비전, 학위, 2026-10-23 열람)
[^ssel]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (가변적 기계학습 알고리즘 연구실 항목, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (한인수 교수 항목, 2026-10-23 열람)
[^pdf]: 대표 논문 1–4·6의 arXiv 원문 첫 쪽 <https://arxiv.org/pdf/2607.03012> (v1), <https://arxiv.org/pdf/2602.20217> (v2), <https://arxiv.org/pdf/2601.03019> (v4), <https://arxiv.org/pdf/2502.02617> (v1), <https://arxiv.org/pdf/2502.14882> (v2) (저자 소속, 교신·공동 지도·공동 기여 표시와 저자 순서 설명, 2026-10-23 열람)

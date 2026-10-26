# 컴퓨터 시스템 아키텍쳐 연구실 (VIA Research Group, Vertically Integrated Architecture)

**KAIST 전기및전자공학부 · 유민수 교수**

- 분야: 컴퓨터 구조, 대형 언어 모델·AI 에이전트를 위한 AI 서버 시스템, 메모리 안 연산(PIM), 추천 모델 서빙 시스템, 프라이버시 보호 머신러닝과 엣지 기기용 AI 가속기
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: 컴퓨터 구조·운영체제[^home][^eeprof][^p5], AI 시스템·인프라[^p1][^p3][^p6], 대형 언어 모델[^p1][^p2][^p3], AI 반도체·가속기[^research][^p7][^p8], 메모리 내 연산[^p5], AI·기계학습 보안·프라이버시[^p7], 추천 시스템[^p6], 엣지 컴퓨팅·엣지 AI[^p8]
- 홈페이지: <https://sites.google.com/view/kaist-via>
- 근거와 출처: [VIA 근거 페이지](via-sources.md)

> 반도체 집적회로 기술, 컴퓨터 시스템 구조, 응용과 알고리즘을 함께 최적화하는 방식으로 앞으로의 인공지능 시스템을 위한 고성능 컴퓨터 구조를 연구하는 연구실이다.[^home]

## 무엇을 연구하나

연구실은 KAIST 전기및전자공학부 유민수 교수가 이끄는 연구실이다.[^eeprof] 누리집은 이름을 VIA(Vertically Integrated Architecture) Research Group으로 적고, 전기및전자공학부 교수 소개와 반도체시스템공학과 연구실 목록은 「컴퓨터 시스템 아키텍쳐 연구실」로 올린다.[^eeprof][^sselab] 누리집은 연구실이 전기및전자공학부, 반도체시스템공학과, Graduate School of Artificial Intelligence(AI), Graduate School of AI Semiconductor에 함께 속해 있다고 적는다.[^home]

누리집 첫 화면은 연구실이 컴퓨터 구조(프로세서·메모리 같은 컴퓨터 하드웨어의 짜임새) 분야를 "수직 통합" 방식으로 연구한다고 적는다. VLSI 기술(많은 회로를 칩 하나에 모아 만드는 반도체 집적회로 기술), 컴퓨터 시스템 구조, 응용과 알고리즘을 함께 최적화해, 앞으로의 '지능형' 시스템을 위한 고성능 컴퓨팅 플랫폼을 만드는 것이 목표다. 이 플랫폼은 프로그래밍할 수 있고, 견고하고, 믿을 수 있고, 안전하고, 에너지 효율이 높아야 한다고 적는다.[^home]

연구 페이지는 연구 분야를 두 갈래로 나눈다. 컴퓨터 구조 갈래에는 GPU 컴퓨팅을 위한 고처리량 프로세서 구조, 캐시와 메모리로 이루어진 메모리 계층 설계, DRAM(컴퓨터의 주 메모리로 쓰는 반도체 메모리) 구조, 컴퓨터 비전·머신러닝을 위한 구조적 지원, 컴퓨터 보안, 머신러닝·컴퓨터 비전용 ASIC(한 가지 용도에 맞춰 만든 전용 칩) 설계와 FPGA(회로 구성을 다시 짤 수 있는 칩) 시제품 제작이 있다. 머신러닝 갈래에는 NPU(신경망 처리 장치) 설계, 자율주행과 운전자 보조 시스템, 자연어 처리와 번역 서비스, 음성 인식이 있다.[^research]

최근 연구는 다섯 갈래로 모인다. 첫째, **대형 언어 모델·AI 에이전트를 위한 AI 서버 시스템**이다. 추론형 대형 언어 모델의 추론 단계와 답변 단계를 나눠 처리하는 서빙 스케줄러 PASCAL을 만들었고,[^p1] 외부 도구와 함께 여러 단계로 추론하는 AI 에이전트가 쓰는 자원·지연 시간·에너지·데이터센터 전력을 시스템 관점에서 분석했다.[^p2] 대형 언어 모델 학습의 병렬화 구성과 비용을 빠르게 평가하는 시뮬레이터 vTrain을 만들었고,[^p3] NVIDIA GPU의 대안으로 Intel Gaudi NPU를 성능·에너지 효율·프로그래밍 용이성에서 평가했다.[^p4] 둘째, **메모리 안 연산(PIM, 계산 장치를 메모리 안이나 가까이 두어 데이터 이동을 줄이는 방식)**이다. 상용 PIM 기술인 UPMEM-PIM의 시뮬레이터 uPIMulator를 만들어 그 설계를 분석하고 앞으로의 PIM 구조에 필요한 기능을 제시했다.[^p5] 셋째, **추천 모델을 위한 서빙·학습 시스템**이다. 추천 모델의 서로 다른 자원 수요에 맞춰 자원을 잘게 나누는 서빙 구조 ElasticRec을 제안했다.[^p6] 넷째, **프라이버시 보호 머신러닝 하드웨어**다. 차등 프라이버시 학습 알고리즘의 병목을 분석하고 이를 위한 가속기 DiVa를 제안했다.[^p7] 다섯째, **엣지 기기용 AI 가속기**다. 영상 인식용 상태 공간 모델인 Vision Mamba를 엣지 기기에서 돌리는 가속기 Mamba-X를 제안했다.[^p8] 최근 논문 목록에는 PIM 시스템의 메모리 관리 장치(PIM-MMU, MICRO 2024)와 동적 메모리 할당기(PIM-malloc, HPCA 2026), 추천 모델 학습 데이터의 저장장치 내 전처리(PreSto, ISCA 2024), 차등 프라이버시 추천 모델 학습(LazyDP, ASPLOS 2024), 그래프 합성곱 신경망 가속기(GROW, HPCA 2023), 전문가 혼합 모델의 추론 가속(SpecMoE, DAC 2026), 기기 안 AI 에이전트 가속(Agent-X, MobiSys 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 대형 언어 모델·AI 에이전트를 위한 AI 서버 시스템

추론형 대형 언어 모델의 단계 인식 서빙 스케줄링, AI 에이전트와 테스트 시점 확장의 시스템 비용 분석, 대형 언어 모델 학습 구성의 시뮬레이션, GPU와 Intel Gaudi NPU의 AI 시스템 비교 평가.[^p1][^p2][^p3][^p4] 대표 논문 1–4.

### 2. 메모리 안 연산(PIM)

상용 PIM 기술의 시뮬레이터와 설계 분석, PIM 시스템의 메모리 관리와 데이터 전송.[^p5][^pubs] 대표 논문 5.

### 3. 추천 모델을 위한 서빙·학습 시스템

추천 모델 추론 서빙의 자원 탄력성과 메모리 효율, 학습 데이터 전처리 시스템.[^p6][^pubs] 대표 논문 6.

### 4. 프라이버시 보호 머신러닝 하드웨어

차등 프라이버시 학습 알고리즘의 작업 특성 분석과 전용 가속기.[^p7] 대표 논문 7.

### 5. 엣지 기기용 AI 가속기

Vision Mamba 모델을 위한 스캔 연산 배열과 하드웨어 친화적 양자화.[^p8] 대표 논문 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 유민수 교수가 마지막 저자인 학회 논문을 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models](https://doi.org/10.1109/hpca68181.2026.11408493) · HPCA 2026 | 사고 사슬(Chain-of-Thought) 추론을 쓰는 추론형 대형 언어 모델은 답을 내기 전에 긴 추론 단계를 거치므로, 사용자가 첫 토큰(모델이 내놓는 글 조각)을 받기까지의 시간(TTFT)이 늘어난다. 기존 언어 모델 서빙 프레임워크는 추론 단계와 답변 단계를 구분하지 않아 GPU 메모리가 부족할 때 성능이 떨어진다. PASCAL은 추론 단계를 우선 처리해 TTFT를 줄이고, 답변 단계에서는 통제된 선점(실행 중인 요청을 잠시 멈추는 일)과 토큰 속도 조절로 사용자 체감 품질을 지키는 단계 인식 스케줄링 알고리즘이다. 인스턴스(모델을 실행하는 단위) 사이의 배치와 인스턴스 안의 실행을 함께 다루는 계층형 스케줄러로, 단계가 바뀌는 시점에 요청을 옮겨 부하를 고르게 하고 서로 방해하는 일을 줄인다. DeepSeek-R1-Distill-Qwen-32B를 쓴 벤치마크에서 느린 쪽 요청의 TTFT(tail TTFT)를 최대 72% 줄이면서 답변 단계의 서비스 목표(SLO) 달성을 유지했다.[^p1] | 1저자 E. Cho, 마지막 저자 유민수 |
| 2 | 2026 | [The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective](https://doi.org/10.1109/hpca68181.2026.11408569) · HPCA 2026 | 대형 언어 모델 기반 AI 에이전트는 외부 도구와 함께 여러 단계로 생각하는 동적 추론으로 다양한 일을 해내지만, 한 번 묻고 답하던 추론이 여러 차례 오가는 작업 흐름으로 바뀌면서 시스템 비용과 효율, 지속 가능성 문제가 생긴다. 여러 에이전트 설계와 테스트 시점 확장(추론할 때 계산을 더 써서 정확도를 높이는 전략)에서 자원 사용량, 지연 시간, 에너지 소비, 데이터센터 전체의 전력 수요를 재어 AI 에이전트를 시스템 수준에서 종합 분석했다. 퓨샷 프롬프트(질문에 예시 몇 개를 함께 주는 방식), 성찰 깊이, 병렬 추론 같은 설계 선택이 정확도와 비용의 균형에 주는 영향도 살폈다. 에이전트는 계산을 더 쓸수록 정확도가 오르지만 그 이득이 빠르게 줄고, 지연 시간의 편차가 커지며, 인프라 비용이 감당하기 어려운 수준으로 커진다는 것을 보였다. 그래서 실제 환경의 제약 안에서 성능과 배포 가능성을 함께 따지는, 계산 효율적인 추론 쪽으로 에이전트 설계가 바뀌어야 한다고 주장한다.[^p2] | 1저자 J. Kim, 마지막 저자 유민수 |
| 3 | 2024 | [vTrain: A Simulation Framework for Evaluating Cost-Effective and Compute-Optimal Large Language Model Training](https://doi.org/10.1109/micro61859.2024.00021) · MICRO 2024 | 대형 언어 모델을 비용 효과적으로 학습하는 일이 큰 과제다. 지금의 학습 계획은 병렬화 방법의 선택지를 철저히 살피지 않고 경험적 관찰에 기댄 병렬 학습 전략을 써서, 성능을 다 끌어내지 못하고 학습 비용을 낭비한다. 실제 측정(프로파일링)에 바탕을 둔 시뮬레이터 vTrain으로, 효율적이고 비용 효과적인 학습 시스템 구성을 빠르고 정확하게 정하게 했다. 학습 시간과 비용의 균형을 맞추는 병렬화 전략 평가, 여러 언어 모델 학습 작업을 함께 돌리는 GPU 클러스터 스케줄러, 정해진 계산 예산에서 계산 최적의 모델 구조 결정 같은 사례 연구로 쓰임을 보였다.[^p3] | 1저자 J. Bang, 마지막 저자 유민수 |
| 4 | 2025 | [Debunking the CUDA Myth Towards GPU-based AI Systems](https://doi.org/10.1145/3695053.3731050) · ISCA 2025 | AI 시스템 설계의 사실상 표준인 NVIDIA GPU의 대안으로 Intel Gaudi NPU를 종합 평가했다. 마이크로벤치마크(기본 연산 하나하나의 성능을 따로 재는 시험 프로그램)로 Gaudi-2와 NVIDIA A100을 비교해, Gaudi-2가 기본적인 AI 계산·메모리·통신 연산뿐 아니라 여러 주요 AI 작업을 처음부터 끝까지 실행할 때도 대등한 성능을 낸다는 것을 보였다. 행렬 곱셈 라이브러리 FBGEMM의 핵심 연산자와 언어 모델 서빙 프로그램 vLLM을 구현하는 소프트웨어 최적화 전략으로 Gaudi의 프로그래밍 용이성을 GPU용 최적화 구현과 비교했다. Gaudi-2는 A100과 비슷한 에너지 효율을 냈지만 소프트웨어 성숙도에는 개선할 점이 있었다. 상위 AI 프레임워크와 잘 통합되면 Gaudi NPU가 AI 서버 시장에서 NVIDIA GPU에 도전할 수 있지만, NVIDIA의 소프트웨어 생태계와 겨루려면 더 개선이 필요하다고 결론 내렸다.[^p4] | 공동 1저자 Y. Lee·J. Lim(랩 표시), 마지막 저자 유민수 |
| 5 | 2024 | [Pathfinding Future PIM Architectures by Demystifying a Commercial PIM Technology](https://doi.org/10.1109/hpca57654.2024.00029) · HPCA 2024 | 메모리 안 연산(PIM)은 수십 년 동안 연구됐지만 큰 설계 부담과 결정적 활용처가 없어 실제 제품이 되지 못했다. 메모리를 많이 쓰는 중요한 작업이 늘면서 특정 용도용부터 범용까지 여러 상용 PIM 기술이 시장에 나왔다. 프로그래밍이 쉬운 범용 PIM 병렬 컴퓨팅 구조인 UPMEM의 상용 PIM 기술을 깊이 살폈다. 먼저 UPMEM-PIM 소스 코드를 기계어 수준 명령으로 컴파일하고, 이를 사이클 단위 성능 시뮬레이터가 받아 쓰는 유연한 PIM 시뮬레이터 uPIMulator를 만들었다. uPIMulator로 UPMEM의 PIM 설계를 자세히 분석했고, 사례 연구로 지금 UPMEM-PIM 시스템의 주요 한계와 앞으로의 PIM 구조가 갖춰야 할 중요한 구조적 기능을 제시했다.[^p5] | 1저자 B. Hyun, 마지막 저자 유민수 |
| 6 | 2024 | [ElasticRec: A Microservice-based Model Serving Architecture Enabling Elastic Resource Scaling for Recommendation Models](https://doi.org/10.1109/isca59077.2024.00038) · ISCA 2024 | 추천 시스템이 널리 쓰이면서 데이터센터의 계산 자원 수요가 크게 늘었다. 지금의 추천 모델 서빙 구조는 모델 단위로 자원을 나눠 자원을 잘 쓰지 못하고, 총소유비용(장비를 사고 운영하는 데 드는 전체 비용)이 최적보다 커진다. 추천 모델의 서로 다른 자원 수요에 맞춰 자원을 잘게 나누는 마이크로서비스(기능을 작은 독립 서비스로 쪼갠 소프트웨어 구조) 기반 서빙 구조 ElasticRec을 제안했고, 효용 기반 자원 할당으로 메모리 효율을 높였다. 최신 추천 추론 서빙 시스템과 비교해 메모리 할당 크기를 평균 3.3배 줄이고 메모리 효용을 평균 8.1배 높여, 배포 비용을 평균 1.6배 줄였다.[^p6] | 1저자 Y. Choi, 마지막 저자 유민수 |
| 7 | 2022 | [DiVa: An Accelerator for Differentially Private Machine Learning](https://doi.org/10.1109/micro56248.2022.00084) · MICRO 2022 | 머신러닝이 널리 쓰이면서 학습 데이터를 낸 사용자의 프라이버시를 지키는 일이 큰 걱정거리가 됐고, 차등 프라이버시(DP, 어떤 한 사람의 데이터가 학습에 들어갔는지를 결과로 알아내기 어렵게 하는 수학적 보호 기준)가 산업계에서 프라이버시 보호의 실용 표준으로 빠르게 자리 잡고 있다. 그런데 이 알고리즘이 컴퓨터 시스템 설계에 주는 의미는 거의 연구되지 않았다. 최신 차등 프라이버시 학습 알고리즘 DP-SGD의 작업 특성을 자세히 분석해, 일반 학습보다 메모리 용량과 계산 요구가 큰 점 같은 고유한 성질과 핵심 병목의 근본 원인을 찾았다. 이를 바탕으로 차등 프라이버시 머신러닝 가속기 DiVa를 제안했고, 계산 장치 활용도를 크게 높여 기존 시스톨릭 배열(계산 장치를 격자로 잇고 데이터를 차례로 흘려보내는 하드웨어 구조)보다 에너지 효율이 2.6배 높았다.[^p7] | 공동 1저자 B. Park·R. Hwang(랩 표시), 마지막 저자 유민수 |
| 8 | 2025 | [Mamba-X: An End-to-End Vision Mamba Accelerator for Edge Computing Devices](https://doi.org/10.1109/iccad66269.2025.11240777) · ICCAD 2025 | 트랜스포머(어텐션 연산으로 입력의 각 부분 사이 관계를 계산하는 신경망 구조)는 언어 모델에서 효과적이지만 입력 길이의 제곱으로 늘어나는 계산·메모리 요구에 묶인다. 상태 공간 모델(SSM, 내부 상태를 차례로 갱신하며 입력을 처리하는 모델)은 어텐션의 계산 복잡도를 입력 길이의 제곱에서 입력 길이에 비례하는 수준으로 낮추고 메모리도 덜 쓴다. Vision Mamba는 이 방식을 컴퓨터 비전 작업에 맞춰 기존 트랜스포머 모델보다 지연 시간과 메모리 사용을 줄였지만, 차례로 진행하는 스캔 연산 때문에 GPU를 효율적으로 쓰기 어려워 엣지 기기(데이터가 생기는 현장에서 직접 계산하는 기기)에 올리기 어렵다. 병렬성을 최대로 끌어내고 메모리 이동을 줄이는 시스톨릭 스캔 배열과, 정확도를 잃지 않고 메모리 사용을 줄이며 하드웨어 효율을 높이는 하드웨어 친화적 혼합 양자화(수를 더 적은 비트로 나타내 메모리와 계산을 줄이는 방법) 기법을 갖춘 Vision Mamba 전용 가속기 Mamba-X를 제안했다.[^p8] | 1저자 D. Yoon, 마지막 저자 유민수 |

## 교수와 전문 분야

유민수(Minsoo Rhu) 교수는 University of Texas at Austin에서 박사 학위(2014)를 받았다.[^eeprof] 전기및전자공학부 교수 소개는 직위를 부교수로, 괄호 안에 "디비젼 체어"로 적고, 소속 디비전을 Computer와 Circuit division으로 적는다.[^eeprof] 주요 연구분야는 Security, Computer Architecture, Software Systems & Networking으로, 주요 연구는 컴퓨터 구조, VLSI SoC 설계, 딥-러닝, 컴퓨터 비전으로 적는다.[^eeprof] 반도체시스템공학과 교수진 목록에도 올라 있고 연구분야는 "컴퓨터, 인공지능 및 소프트웨어"로 분류된다.[^ssefac]

연구실 소식에 따르면 교수는 2019년 12월 KAIST Graduate School of Artificial Intelligence(AI)의 겸임교수(adjunct professor)를 맡았고, 2020년 9월 부교수(Associate Professor)로, 2024년 7월 정년 보장 부교수(Tenured Associate Professor)로 승진했으며, 2026년 2월 KAIST 지정석좌교수(KAIST Endowed Chair Professor)로 임명됐다.[^news] 2024년 6월 IEEE Transactions on Computers의 부편집장(Associate Editor)을 맡았고, 2025년 제58회 IEEE/ACM 마이크로아키텍처 국제 학술대회(MICRO-58)의 프로그램 공동 위원장(Program Co-Chair)을 맡았다. 연구실 소식은 이것이 MICRO 58년 역사에서 아시아 대학 교수가 프로그램 위원장으로 뽑힌 첫 사례라고 적는다.[^news]

연구실 Awards 페이지는 교수의 국제 수상·영예로 MICRO-58 Program Co-Chair(2025), IEEE Micro Top Picks - Honorable Mention(입선)(2025, 2021, 2020), ISCA Hall of Fame(2024), HPCA Best Paper Award(2024), Google Research Scholar Award(2023), IEEE Senior Member(2022), MICRO Hall of Fame(2022), HPCA Hall of Fame(2021), Facebook Faculty Research Award(2020)를 적는다. 국내 항목으로는 KAIST 지정석좌교수(2026), KAIST 공과대학 Impact Research Award(2025), 전기및전자공학부 Best Teaching Award(EE312 Introduction to Computer Architecture 2025, EE595 Parallel Computer Architecture 2021), KAIST 대표연구성과 10선(2024), 삼성미래기술육성사업 Research Award(2024, 2017), SW Starlab(2024), Y-KAST(Young Korean Academy of Science and Technology) Membership(2022), KAIST 공과대학 Technology Innovation Award(2022)를 적는다.[^awards] 소식에 따르면 HPCA-30(2024) Best Paper Award는 대표 논문 5(uPIMulator) 연구가 받았고, 이 논문은 IEEE Micro Top Picks - Honorable Mention(입선)과 KAIST 대표연구성과 10선(2024)에도 뽑혔다.[^news]

전기및전자공학부 교수 소개의 대표업적에는 에너지 효율적인 GPU를 위한 지역성 인식 메모리 계층(MICRO-46, 2013), 확장 가능하고 메모리 효율적인 신경망 설계를 위한 가상화 심층 신경망 vDNN(MICRO-49, 2016), 압축·희소 합성곱 신경망 가속기 SCNN(ISCA-44, 2017), 심층 신경망 학습에서 활성값 희소성을 활용하는 압축 DMA 엔진(HPCA-24, 2018), 심층 신경망 학습을 위한 메모리 중심 HPC 시스템 구조(IEEE CAL, 2018)가 올라 있다.[^eeprof] 랩 Publications 목록을 시기별로 보면, 2009–2010년 논문은 JPEG2000 영상 압축용 산술 부호기의 하드웨어 구조를, 2012–2015년 논문은 GPU의 제어 흐름 분기 처리·SIMD 자원 활용·메모리 계층·캐시 할당·전압 잡음을, 2016–2018년 논문은 심층 신경망 학습의 메모리 관리와 희소 신경망 가속기, GPU용 DRAM 시스템, 여러 GPU를 잇는 구조를 다룬다. 2018–2020년 논문은 딥러닝을 위한 메모리 중심 시스템과 근접 메모리 처리(TensorDIMM), NPU의 주소 변환(NeuMMU)과 작업 스케줄링(PREMA), 추천 모델 가속기(Centaur)를 다룬다.[^pubs]

논문으로 보면 지금의 전문 분야는 다섯 갈래다. 첫째, 대형 언어 모델과 AI 에이전트의 서빙·학습을 위한 AI 서버 시스템과 AI 가속기 평가다(대표 논문 1–4).[^p1][^p2][^p3][^p4] 둘째, 메모리 안 연산 시스템의 구조와 시뮬레이션이다(대표 논문 5).[^p5] 셋째, 추천 모델의 서빙 시스템이다(대표 논문 6).[^p6] 넷째, 차등 프라이버시 머신러닝을 위한 가속기다(대표 논문 7).[^p7] 다섯째, 엣지 기기용 비전 모델 가속기다(대표 논문 8).[^p8]

## 응용 분야

대표 논문은 추론형 대형 언어 모델의 서빙(DeepSeek-R1-Distill-Qwen-32B 벤치마크),[^p1] AI 에이전트를 돌리는 데이터센터의 전력과 비용,[^p2] 대형 언어 모델 학습 비용과 GPU 클러스터 스케줄링,[^p3] Intel Gaudi NPU와 NVIDIA GPU 기반 AI 서버,[^p4] 상용 PIM 시스템,[^p5] 데이터센터의 추천 모델 추론 서빙,[^p6] 사용자 프라이버시를 지키는 머신러닝 학습,[^p7] 엣지 기기의 영상 인식 모델 실행[^p8]을 대상으로 한다. 연구실 소식에 따르면 연구실은 고성능 AI 모델 서빙 시스템 개발(삼성미래기술육성사업, 2024년 선정)과 안전하고 프라이버시를 지키는 AI 시스템·시스템 소프트웨어 개발(SW스타랩, 2024년 선정, 지원 기간 8년) 과제를 맡았고, 2021년 9월 한국연구재단 중견연구자 지원 사업에 선정됐다.[^news] 랩이 적은 박사 졸업생의 진로는 NVIDIA, Google, Samsung Electronics(Device Solutions), UNIST이고, 석사 졸업생의 진로에는 Rebellions, Klleon, MangoBoost, HD Korea Shipbuilding & Offshore Engineering(AI center), SK Hynix와 KAIST 박사과정 진학이 있다.[^people]

## 구성원

2026년 10월 22일 랩 People 페이지 기준이다. Ph.D. Students 칸 14명과 M.S. Students 칸 11명이며, 과정은 칸 이름(박사과정, 석사과정)을 옮겼다. 누리집 People 페이지에는 구성원의 이메일과 연구 주제가 적혀 있지 않다.[^people] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Taehun Kim | 박사과정 | 5 |
| Dongho Yoon | 박사과정 | 7, 8 |
| Jinha Chung | 박사과정 | 2 |
| Jehyeon Bang | 박사과정 | 1, 3, 4 |
| Dongjae Lee | 박사과정 | 5, 8 |
| Gwangoo Yeo | 박사과정 |  |
| Jiin Kim | 박사과정 | 2, 6 |
| Juntaek Lim | 박사과정 | 4 |
| Eunyeong Cho | 박사과정 | 1, 4 |
| Hyeseong Kim | 박사과정 |  |
| Gungyu Lee | 박사과정 | 8 |
| Jaewon Chang | 박사과정 | 8 |
| Byeongjun Shin | 박사과정 | 2 |
| Taekwon Lee | 박사과정 |  |
| Jinseop Im | 석사과정 | 4 |
| Junga Lee | 석사과정 |  |
| Yokyung Lee | 석사과정 |  |
| Byeongkyu Park | 석사과정 |  |
| Jiwoong Yang | 석사과정 |  |
| Seungjun Lee | 석사과정 |  |
| Kiho Kim | 석사과정 |  |
| Cheoljung Lee | 석사과정 |  |
| Sihoon Lee | 석사과정 |  |
| Myeongsoo Song | 석사과정 |  |
| Jiwoo Hong | 석사과정 |  |

## 졸업생과 학부 연구 인턴

랩 People 페이지의 Alumni (Ph.D.) 6명, Alumni (M.S.) 22명, Undergraduate Research Interns 74명이다. 졸업생의 연도와 진로는 랩이 적은 것이고, 석사 졸업생 16명은 KAIST 박사과정으로 이어졌다고 적혀 있다. 학부 연구 인턴의 괄호 안은 누리집이 적은 참여 학기(Winter 2018–Fall 2026)이며, 지금 학기(Fall 2026)의 인턴도 함께 들어 있다. 한 사람이 석사 졸업생, 박사 졸업생, 학부 연구 인턴, 현재 구성원 칸에 함께 오른 경우가 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Youngeun Kwon | 박사 (2024) | NVIDIA, Santa Clara, CA, USA |
| Yujeong Choi | 박사 (2024) | Google, Sunnyvale, CA, USA |
| Bongjoon Hyun | 박사 (2025) | Samsung Electronics (Device Solutions), South Korea |
| Ranggi Hwang | 박사 (2025) | UNIST, South Korea |
| Yunjae Lee | 박사 (2025) | Samsung Electronics (Device Solutions), South Korea |
| Jiwon Lee | 박사 (2026) | Samsung Electronics (Device Solutions), South Korea |
| Yujeong Choi | 석사 (2020) | continuing as a Ph.D. student @ KAIST |
| Ranggi Hwang | 석사 (2021) | continuing as a Ph.D. student @ KAIST |
| Yunjae Lee | 석사 (2021) | continuing as a Ph.D. student @ KAIST |
| Taehun Kim | 석사 (2021) | continuing as a Ph.D. student @ KAIST |
| Yunseong Kim | 석사 (2022) | Rebellions |
| Minhoo Kang | 석사 (2022) | Rebellions |
| Dongho Yoon | 석사 (2022) | continuing as a Ph.D. student @ KAIST |
| Beomsik Park | 석사 (2023) | Klleon |
| Jehyeon Bang | 석사 (2023) | continuing as a Ph.D. student @ KAIST |
| Yoonhyuk Choi | 석사 (2024) | MangoBoost |
| Jiin Kim | 석사 (2024) | continuing as a Ph.D. student @ KAIST |
| Gwangoo Yeo | 석사 (2024) | continuing as a Ph.D. student @ KAIST |
| Dongjae Lee | 석사 (2024) | continuing as a Ph.D. student @ KAIST |
| Juntaek Lim | 석사 (2024) | continuing as a Ph.D. student @ KAIST |
| Eunyeong Cho | 석사 (2025) | continuing as a Ph.D. student @ KAIST |
| Hyeseong Kim | 석사 (2025) | continuing as a Ph.D. student @ KAIST |
| Seongjin Gong | 석사 (2025) | HD Korea Shipbuilding & Offshore Engineering (AI center) |
| Hyesung Ahn | 석사 (2025) | SK Hynix |
| Gungyu Lee | 석사 (2026) | continuing as a Ph.D. student @ KAIST |
| Jaewon Chang | 석사 (2026) | continuing as a Ph.D. student @ KAIST |
| Byeongjun Shin | 석사 (2026) | continuing as a Ph.D. student @ KAIST |
| Taekwon Lee | 석사 (2026) | continuing as a Ph.D. student @ KAIST |
| Hojin Ahn | 학부 연구 인턴 (Fall 2026) |  |
| Yelin Kim | 학부 연구 인턴 (Fall 2026) |  |
| Sehyun Choi | 학부 연구 인턴 (Fall 2026) |  |
| Donghyun Kim | 학부 연구 인턴 (Fall 2026) |  |
| Hyunwoo Seo | 학부 연구 인턴 (Summer 2026) |  |
| Jimin Byeon | 학부 연구 인턴 (Summer 2026) |  |
| Jae Yeong Seo | 학부 연구 인턴 (Summer 2026) |  |
| Dongmin Ku | 학부 연구 인턴 (Summer 2026) |  |
| Juwon Lee | 학부 연구 인턴 (Summer 2026) |  |
| Chaehun Mun | 학부 연구 인턴 (Summer 2026) |  |
| HyeonJun Boo | 학부 연구 인턴 (Summer 2026) |  |
| Hyungi Choi | 학부 연구 인턴 (Spring 2026) |  |
| Hyuckjun Choi | 학부 연구 인턴 (Spring 2026, Summer 2026) |  |
| Yongjune Lee | 학부 연구 인턴 (Spring 2026) |  |
| Seokho Hong | 학부 연구 인턴 (Spring 2026) |  |
| Seungyup Kim | 학부 연구 인턴 (Spring 2026, Fall 2026) |  |
| Byunghoon Hwang | 학부 연구 인턴 (Winter 2025) |  |
| Jihwan Kim | 학부 연구 인턴 (Winter 2025, Spring 2026, Summer 2026) |  |
| Byungjoo Kim | 학부 연구 인턴 (Winter 2025) |  |
| Hokyung Lee | 학부 연구 인턴 (Winter 2025) |  |
| Chaeyoung Son | 학부 연구 인턴 (Winter 2025) |  |
| Wonheng Lee | 학부 연구 인턴 (Fall 2025) |  |
| Jeongmin Lee | 학부 연구 인턴 (Summer 2025, Fall 2025) |  |
| Kiho Kim | 학부 연구 인턴 (Spring 2025, Fall 2025, Winter 2025) |  |
| Cheoljung Lee | 학부 연구 인턴 (Winter 2024, Summer 2025, Fall 2025, Winter 2025) |  |
| Sihoon Lee | 학부 연구 인턴 (Winter 2024, Summer 2025, Winter 2025) |  |
| Byeongkyu Park | 학부 연구 인턴 (Winter 2024, Spring 2025) |  |
| Yokyung Lee | 학부 연구 인턴 (Fall 2024, Winter 2024, Spring 2025) |  |
| Sanghyeok Boo | 학부 연구 인턴 (Fall 2024) |  |
| Seungjun Lee | 학부 연구 인턴 (Fall 2024, Summer 2025, Fall 2025, Winter 2025) |  |
| Jaeuk Lee | 학부 연구 인턴 (Summer 2024) |  |
| Myeongsoo Song | 학부 연구 인턴 (Summer 2024, Fall 2024, Winter 2025, Spring 2026, Summer 2026) |  |
| Byeongjun Shin | 학부 연구 인턴 (Winter 2023, Spring 2024, Summer 2024) |  |
| Jinseop Im | 학부 연구 인턴 (Winter 2023, Spring 2024, Summer 2024, Fall 2024, Winter 2024) |  |
| Taeha Kim | 학부 연구 인턴 (Fall 2023) |  |
| Woonggyu Park | 학부 연구 인턴 (Summer 2023) |  |
| Jongeun Park | 학부 연구 인턴 (Spring 2023) |  |
| Dongkyun Lim | 학부 연구 인턴 (Spring 2023) |  |
| Donghyun Choi | 학부 연구 인턴 (Fall 2022, Winter 2022, Spring 2023) |  |
| Gungyu Lee | 학부 연구 인턴 (Winter 2022, Fall 2023) |  |
| Yoonsoo Oh | 학부 연구 인턴 (Summer 2022) |  |
| Jinwoo Baek | 학부 연구 인턴 (Summer 2022) |  |
| Eunjee Na | 학부 연구 인턴 (Summer 2022) |  |
| Hyeseong Kim | 학부 연구 인턴 (Spring 2022, Summer 2022, Fall 2022, Winter 2022) |  |
| Hankyul Kim | 학부 연구 인턴 (Winter 2021, Spring 2022) |  |
| Seungjae Lee | 학부 연구 인턴 (Winter 2021) |  |
| Juntaek Lim | 학부 연구 인턴 (Winter 2021, Spring 2022, Summer 2022) |  |
| Eunyeong Cho | 학부 연구 인턴 (Summer 2021, Fall 2021, Winter 2021, Spring 2022) |  |
| Junseo Cha | 학부 연구 인턴 (Spring 2021, Summer 2021, Fall 2021) |  |
| Seonho Lee | 학부 연구 인턴 (Spring 2021, Summer 2021, Fall 2021, Winter 2021) |  |
| Gwangoo Yeo | 학부 연구 인턴 (Spring 2021, Summer 2021, Fall 2021) |  |
| Seunghyun Chung | 학부 연구 인턴 (Winter 2020) |  |
| Seungbin Shin | 학부 연구 인턴 (Winter 2020) |  |
| Minwoo Roh | 학부 연구 인턴 (Winter 2020) |  |
| Hyuntae Song | 학부 연구 인턴 (Winter 2020) |  |
| Yoonhyuk Choi | 학부 연구 인턴 (Winter 2020, Fall 2021, Winter 2021) |  |
| Dongjae Lee | 학부 연구 인턴 (Fall 2020, Winter 2020, Winter 2021) |  |
| Yunjin Ki | 학부 연구 인턴 (Fall 2020) |  |
| Woojin Lee | 학부 연구 인턴 (Summer 2020) |  |
| Joonwon Ko | 학부 연구 인턴 (Summer 2020) |  |
| Beomsik Park | 학부 연구 인턴 (Summer 2020, Fall 2020, Winter 2020, Spring 2021, Summer 2021) |  |
| Jiin Kim | 학부 연구 인턴 (Summer 2020, Fall 2020) |  |
| Joonsuk Ro | 학부 연구 인턴 (Summer 2020) |  |
| Zhixian Jin | 학부 연구 인턴 (Winter 2020) |  |
| Jiwon Kang | 학부 연구 인턴 (Winter 2020) |  |
| Jisun Kim | 학부 연구 인턴 (Winter 2020) |  |
| Jehyeon Bang | 학부 연구 인턴 (Winter 2020) |  |
| Minhoo Kang | 학부 연구 인턴 (Fall 2019) |  |
| Jinha Chung | 학부 연구 인턴 (Spring 2019, Summer 2019, Winter 2019, Spring 2020, Summer 2020, Fall 2020, Winter 2020) |  |
| Sirawit Putpat | 학부 연구 인턴 (Winter 2018, Spring 2019) |  |
| Inje Hwang | 학부 연구 인턴 (Winter 2018) |  |
| Gangmin Bae | 학부 연구 인턴 (Winter 2018) |  |
| Seyoung Oh | 학부 연구 인턴 (Winter 2018) |  |
| Yunseong Kim | 학부 연구 인턴 (Winter 2018, Spring 2019, Summer 2019, Fall 2019) |  |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021–2026년 연도 구역에 실린 42편이다(2026년 9, 2025년 5, 2024년 13, 2023년 2, 2022년 6, 2021년 7). 저자 순서와 제목·학회·학술지 표기는 랩 표기 그대로이고, 저자 이름 뒤 *는 랩이 밝힌 공동 1저자 표시다. 괄호 안의 수상 표시는 랩이 논문 아래에 적은 것이다. 2026년 IEEE Computer Architecture Letters 논문 한 편(LPDDR6 시스템 메타데이터 모드, 1저자 Dongjae Lee)은 목록이 권호 기간(Jul.-Dec. 2026)만 적는다. 2026년 10월 17일 소식은 제목 없이 Dongjae의 IEEE Computer Architecture Letters 논문 게재 승인을 알리고, 목록에서 같은 1저자의 2026년 이 학술지 논문은 이 한 편뿐이라 이 항목에 「2026년 10월 게재 승인 소식」을 붙였다. 2024년 ISCA-51의 Pre-gated MoE 한 편은 유민수 교수가 저자 명단에 없는 논문으로, 랩 목록대로 실었다.[^pubs][^news]

**2026**

- Dongjae Lee and Minsoo Rhu. "The Hidden Cost of Reliability: Performance Impact of LPDDR6 System Metadata Mode". *IEEE Computer Architecture Letters, Jul.-Dec. 2026 (2026년 10월 게재 승인 소식)*.
- Gwangoo Yeo, Zhiyang Shen, Wei Cui, Matteo Interlandi, Rathijit Sen, Bailu Ding, Qi Chen, and Minsoo Rhu. "ZipFlow: a Compiler-based Framework to Unleash Compressed Data Movement for Modern GPUs". *The 52nd International Conference on Very Large Data Bases (VLDB-52), Boston, USA, Aug.2026*.
- Jinha Chung, Byeongjun Shin, Jiin Kim, and Minsoo Rhu. "Agent-X: Full Pipeline Acceleration of On-device AI Agents". *The 24th ACM International Conference on Mobile Systems, Applications, and Services (MobiSys-24), Cambridge, UK, Jun. 2026*.
- Jehyeon Bang, Eunyeong Cho, Ranggi Hwang, Jinha Chung, and Minsoo Rhu. "SpecMoE: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding". *The 63rd ACM/IEEE Design Automation Conference (DAC), Long Beach, CA, Jul. 2026*.
- Jiin Kim\*, Gwangoo Yeo\*, Yujeong Choi, and Minsoo Rhu. "PREBA: A Hardware/Software Co-Design for Multi-Instance GPU based AI Inference Servers". *The 63rd ACM/IEEE Design Automation Conference (DAC), Long Beach, CA, Jul. 2026*.
- Hyesung Ahn, Ranggi Hwang, and Minsoo Rhu. "Exploring KV Cache Quantization in Multimodal Large Language Model Inference". *IEEE Computer Architecture Letters, Jan.-Jun. 2026*.
- Dongjae Lee\*, Bongjoon Hyun\*, Youngjin Kwon, and Minsoo Rhu. "PIM-malloc: A Fast and Scalable Dynamic Memory Allocator for Processing-In-Memory (PIM) Architectures". *The 32nd International Symposium on High-Performance Computer Architecture (HPCA-32), Sydney, Australia, Feb.2026*.
- Eunyeong Cho, Jehyeon Bang, Ranggi Hwang, and Minsoo Rhu. "PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models". *The 32nd International Symposium on High-Performance Computer Architecture (HPCA-32), Sydney, Australia, Feb.2026*.
- Jiin Kim, Byeongjun Shin, Jinha Chung, and Minsoo Rhu. "The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective". *The 32nd International Symposium on High-Performance Computer Architecture (HPCA-32), Sydney, Australia, Feb.2026*.

**2025**

- Yujeong Choi, John Kim, and Minsoo Rhu. "Hera: A Heterogeneity-Aware Multi-Tenant Inference Server for Personalized Recommendations". *The 34th International Conference on Parallel Architectures and Compilation Techniques (PACT-34), Irvine, CA, Nov.2025*.
- Dongho Yoon, Gungyu Lee, Jaewon Chang, Yunjae Lee, Dongjae Lee, and Minsoo Rhu. "Mamba-X: An End-to-End Vision Mamba Accelerator for Edge Computing Devices". *The 44th IEEE/ACM International Conference on Computer-Aided Design (ICCAD-44), Munich, Germany, Oct. 2025*.
- Yunjae Lee\*, Juntaek Lim\*, Jehyeon Bang, Eunyeong Cho, Huijong Jeong, Taesu Kim, Hyungjun Kim, Joonhyung Lee, Jinseop Im, Ranggi Hwang, Se Jung Kwon, Dongsoo Lee, and Minsoo Rhu. "Debunking the CUDA Myth Towards GPU-based AI Systems". *The 52nd IEEE/ACM International Symposium on Computer Architecture (ISCA-52), Tokyo, Japan, Jun. 2025*.
- Taehun Kim, Yunjae Lee, Juntaek Lim, and Minsoo Rhu. "A Characterization of Generative Recommendation Models: Study of Hierarchical Sequential Transduction Unit". *IEEE Computer Architecture Letters, Jan.-Jun. 2025*.
- Jiwon Lee, Yunjae Lee, Youngeun Kwon, and Minsoo Rhu. "Characterization and Analysis of the 3D Gaussian Splatting Rendering Pipeline". *IEEE Computer Architecture Letters, Jan.-Jun. 2025*.

**2024**

- Eunyeong Cho, Jehyeon Bang, and Minsoo Rhu. "Characterization and Analysis of Text-to-Image Diffusion Models". *IEEE Computer Architecture Letters, Jul.-Dec. 2024*.
- Zhixian Jin, Christopher Rocca, Jiho Kim, Hans Kasan, Minsoo Rhu, Ali Bakhoda, Tor Aamodt, and John Kim. "Uncovering Real GPU NoC Characteristics: Implications on Interconnect Architecture". *The 57th IEEE/ACM International Symposium on Microarchitecture (MICRO-57), Austin, TX, Nov. 2024*.
- Dongjae Lee, Bongjoon Hyun, Taehun Kim, and Minsoo Rhu. "PIM-MMU: A Memory Management Unit for Accelerating Data Transfers in Commercial PIM Systems". *The 57th IEEE/ACM International Symposium on Microarchitecture (MICRO-57), Austin, TX, Nov. 2024*.
- Jehyeon Bang, Yujeong Choi, Myeongwoo Kim, Yongdeok Kim, and Minsoo Rhu. "vTrain: A Simulation Framework for Evaluating Cost-effective and Compute-optimal Large Language Model Training". *The 57th IEEE/ACM International Symposium on Microarchitecture (MICRO-57), Austin, TX, Nov. 2024*.
- Dongho Yoon\*, Taehun Kim\*, Jae W. Lee, and Minsoo Rhu. "A Quantitative Analysis of State Space Model-based Large Language Model: Study of Hungry Hungry Hippos". *IEEE Computer Architecture Letters, Jul.-Dec. 2024*.
- Dongjae Lee, Bongjoon Hyun, Taehun Kim, and Minsoo Rhu. "Analysis of Data Transfer Bottlenecks in Commercial PIM Systems: A Study with UPMEM-PIM". *IEEE Computer Architecture Letters, Jul.-Dec. 2024*.
- Ranggi Hwang\*, Jianyu Wei\*, Shijie Cao, Changho Hwang, Xiaohu Tang, Ting Cao, and Mao Yang. "Pre-gated MoE: An Algorithm-System Co-Design for Fast and Scalable Mixture-of-Expert Inference". *The 51st IEEE/ACM International Symposium on Computer Architecture (ISCA-51), Buenos Aires, Argentina, Jun. 2024*.
- Yunjae Lee\*, Hyeseong Kim\*, and Minsoo Rhu. "PreSto: An In-Storage Data Preprocessing System for Training Recommendation Models". *The 51st IEEE/ACM International Symposium on Computer Architecture (ISCA-51), Buenos Aires, Argentina, Jun. 2024*.
- Yujeong Choi, Jiin Kim, and Minsoo Rhu. "ElasticRec: A Microservice-based Model Serving Architecture Enabling Elastic Resource Scaling for Recommendation Models". *The 51st IEEE/ACM International Symposium on Computer Architecture (ISCA-51), Buenos Aires, Argentina, Jun. 2024*.
- Juntaek Lim, Youngeun Kwon, Ranggi Hwang, Kiwan Maeng, Edward Suh, and Minsoo Rhu. "LazyDP: Co-Designing Algorithm-Software for Scalable Training of Differentially Private Recommendation Models". *The 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS-29), San Diego, CA, Apr. 2024*.
- Maximilian Lam, Jeff Johnson, Wenjie Xiong, Kiwan Maeng, Udit Gupta, Yang Li, Liangzhen Lai, Minsoo Rhu, Hsien-Hsin S. Lee, Vijay Janapa Reddi, Gu-Yeon Wei, David Brooks, and Edward Suh. "GPU-based Private Information Retrieval for On-Device Machine Learning Inference". *The 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS-29), San Diego, CA, Apr. 2024*.
- Bongjoon Hyun, Taehun Kim, Dongjae Lee, and Minsoo Rhu. "Pathfinding Future PIM Architectures by Demystifying a Commercial PIM Technology". *The 30th IEEE International Symposium on High-Performance Computer Architecture (HPCA-30), Edinburgh, UK, Feb. 2024 (Best Paper Award; IEEE Micro Top Picks - Honorable Mention(입선))*.
- Hyeseong Kim\*, Yunjae Lee\*, and Minsoo Rhu. "FPGA-Accelerated Data Preprocessing for Personalized Recommendation Systems". *IEEE Computer Architecture Letters, Jan.-Jun. 2024*.

**2023**

- Ranggi Hwang\*, Minhoo Kang\*, Jiwon Lee, Dongyun Kam, Youngjoo Lee, and Minsoo Rhu. "GROW: A Row-Stationary Sparse-Dense GEMM Accelerator for Memory-Efficient Graph Convolutional Neural Networks". *The 29th IEEE International Symposium on High-Performance Computer Architecture (HPCA-29), Montreal, Canada, Feb. 2023*.
- Seonho Lee, Ranggi Hwang, Jongse Park, and Minsoo Rhu. "HAMMER: Hardware-friendly Approximate Computing for Self-attention with Mean-redistribution and Linearization". *IEEE Computer Architecture Letters, Jan.-Jun. 2023*.

**2022**

- Beomsik Park\*, Ranggi Hwang\*, Dongho Yoon, Yoonhyuk Choi, and Minsoo Rhu. "DiVa: An Accelerator for Differentially Private Machine Learning". *The 55th IEEE/ACM International Symposium on Microarchitecture (MICRO-55), Chicago, IL, Oct. 2022*.
- Jongmin Kim, Gwangho Lee, Sangpyo Kim, Gina Sohn, John Kim, Minsoo Rhu, and Jung Ho Ahn. "ARK: Fully Homomorphic Encryption Accelerator with Runtime Data Generation and Inter-Operation Key Reuse". *The 55th IEEE/ACM International Symposium on Microarchitecture (MICRO-55), Chicago, IL, Oct. 2022*.
- Yunseong Kim, Yujeong Choi, and Minsoo Rhu. "PARIS and ELSA: An Elastic Scheduling Algorithm for Reconfigurable Multi-GPU Inference Servers". *The 59th ACM/IEEE Design Automation Conference (DAC), San Francisco, CA, Jul. 2022*.
- Yunjae Lee, Jinha Chung, and Minsoo Rhu. "SmartSAGE: Training Large-scale Graph Neural Networks using In-Storage Processing Architectures". *The 49th IEEE/ACM International Symposium on Computer Architecture (ISCA-49), New York, NY, Jun. 2022*.
- Youngeun Kwon and Minsoo Rhu. "Training Personalized Recommendation Systems from (GPU) Scratch: Look Forward not Backwards". *The 49th IEEE/ACM International Symposium on Computer Architecture (ISCA-49), New York, NY, Jun. 2022*.
- Sangpyo Kim, Jongmin Kim, Michael Jaemin Kim, Wonkyung Jung, John Kim, Minsoo Rhu, and Jung Ho Ahn. "BTS: An Accelerator for Bootstrappable Fully Homomorphic Encryption". *The 49th IEEE/ACM International Symposium on Computer Architecture (ISCA-49), New York, NY, Jun. 2022*.

**2021**

- Jaehyun Park, Byeongho Kim, Sungmin Yun, Eojin Lee, Minsoo Rhu, and Jung Ho Ahn. "TRiM: Enhancing Processor-Memory Interfaces with Scalable Tensor Reduction in Memory". *The 54th IEEE/ACM International Symposium on Microarchitecture (MICRO-54), Athens, Greece, Oct. 2021*.
- Bongjoon Hyun, Jiwon Lee, and Minsoo Rhu. "Characterization and Analysis of Deep Learning for 3D Point Cloud Analytics". *IEEE Computer Architecture Letters, Jul.-Dec. 2021*.
- Yunjae Lee, Youngeun Kwon, and Minsoo Rhu. "Understanding the Implication of Non-Volatile Memory for Large-Scale Graph Neural Network Training". *IEEE Computer Architecture Letters, Jul.-Dec. 2021*.
- Youngeun Kwon, Yunjae Lee, and Minsoo Rhu. "Tensor Casting: Co-Designing Algorithm-Architecture for Personalized Recommendation Training". *The 27th IEEE International Symposium on High-Performance Computer Architecture (HPCA-27), Seoul, South Korea, Feb. 2021*.
- Yujeong Choi, Yunseong Kim, and Minsoo Rhu. "LazyBatching: An SLA-aware Batching System for Cloud Machine Learning Inference". *The 27th IEEE International Symposium on High-Performance Computer Architecture (HPCA-27), Seoul, South Korea, Feb. 2021*.
- Jaeguk Ahn, Cheolgyu Jin, Jiho Kim, Minsoo Rhu, Yunsi Fei, David Kaeli, and John Kim. "Trident: A Hybrid Correlation-Collision GPU Cache Timing Attack for AES Key Recovery". *The 27th IEEE International Symposium on High-Performance Computer Architecture (HPCA-27), Seoul, South Korea, Feb. 2021*.
- Byeongho Kim, Jaehyun Park, Eojin Lee, Minsoo Rhu, and Jung Ho Ahn. "TRiM: Tensor Reduction in Memory". *IEEE Computer Architecture Letters, Jan.-Jun. 2021*.

## 수상과 영예

랩 Awards 페이지의 2022–2026년 항목 19건이다(교수 국제 7, 교수 국내 8, 학생 4). 페이지는 연도만 적는다. 괄호 안은 페이지의 구분(교수 국제·국내, 학생)과 학생 수상자 이름이다.[^awards]

- 2025 · Program Co-Chair for the 58th IEEE/ACM International Symposium on Microarchitecture (MICRO-58) (교수, 국제)
- 2025 · IEEE Micro Top Picks - Honorable Mention(입선) (교수, 국제)
- 2024 · ISCA Hall of Fame (교수, 국제)
- 2024 · HPCA Best Paper Award (교수, 국제)
- 2023 · Google Research Scholar Award (교수, 국제)
- 2022 · IEEE Senior Member (교수, 국제)
- 2022 · MICRO Hall of Fame (교수, 국제)
- 2026 · KAIST Endowed Chair Professor (KAIST 지정석좌교수) (교수, 국내)
- 2025 · KAIST Impact Research Award, College of Engineering (교수, 국내)
- 2025 · KAIST Best Teaching Award (EE312: Introduction to Computer Architecture), School of Electrical Engineering (교수, 국내)
- 2024 · KAIST Top 10 Research Achievements in 2024 (KAIST 대표연구성과 10선) (교수, 국내)
- 2024 · Research Award from Samsung Research Funding & Incubation Center (삼성미래기술육성사업) (교수, 국내)
- 2024 · SW Starlab (교수, 국내)
- 2022 · Y-KAST (Young Korean Academy of Science and Technology) Membership (교수, 국내)
- 2022 · KAIST Technology Innovation Award, College of Engineering (교수, 국내)
- 2026 · Best TA Award (학생 수상, Gwangoo Yeo)
- 2025 · Korea Presidential Scholarship in Science and Technology (대통령 과학 장학금) (학생 수상, Juntaek Lim)
- 2022 · Google Ph.D. Fellowship Award (학생 수상, Yujeong Choi)
- 2022 · Best TA Award (학생 수상, Jinha Chung)

## 소식

랩 News 페이지의 2021년 10월 13일 이후 글 66건(2021-12-15–2026-10-17)이다. 날짜는 연도 구역과 글 앞의 월·일 표기를 합친 것이고, 글은 랩 표기 그대로다.[^news]

- 2026-10-17 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Dongjae!
- 2026-08-24 · We have two graduate students joining our group this fall. Welcome aboard Myeongsoo and Jiwoo!
- 2026-06-12 · Jiin has won the Excellence Award at the Global AI Research Leap (GARL) Challenge 2026 hosted by the National AI Research Lab (NAIRL). Congratulations Jiin!
- 2026-05-26 · Our paper titled "ZipFlow: a Compiler-based Framework to Unleash Compressed Data Movement for Modern GPUs" has been accepted for presentation at the 52nd International Conference on Very Large Data Bases (VLDB-52), Boston, USA. Congratulations Gwangoo!
- 2026-02-28 · Our paper titled "Agent-X: Full Pipeline Acceleration of On-device AI Agents" has been accepted for presentation at the 24th International Conference on Mobile Systems, Applications, and Services (MobiSys-24), Cambridge, United Kingdom. Congratulations Jinha, Byeongjun, and Jiin!
- 2026-02-25 · Prof. Rhu has been appointed as the KAIST Endowed Chair Professor (KAIST 지정석좌교수).
- 2026-02-24 · Our group has two papers accepted for presentation at the 63rd ACM/ESDA/IEEE Design Automation Conference (DAC) (DAC-63), Long Beach, CA, Jul. 2026. Congratulations Jehyeon, Eunyeong, Jinha, Jiin, and Gwangoo!
- 2026-02-22 · Jiwon successfully defended his Ph.D. thesis! "Dr." Lee will be joining Samsung Electronics (Device Solutions) as a Staff Engineer. Congratulations and wish you all the best in your next journey!
- 2026-02-22 · We have four graduate students joining our group this spring. Welcome aboard Seungjun, Kiho, Cheoljung, and Sihoon!
- 2025-12-17 · Prof. Rhu received the 2025 KAIST College of Engineering Impact Research Award.
- 2025-12-13 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Hyesung and Dr. Hwang!
- 2025-11-08 · Our group has three papers accepted for presentation at the 32nd International Symposium on High-Performance Computer Architecture (HPCA-32), Sydney, Australia. Congratulations Jiin, Byeongjun, Jinha, Eunyeong, Jehyeon, and Dongjae!
- 2025-09-03 · Prof. Rhu received the Best Teaching Award (EE312: Introduction to Computer Architecture) from the School of EE.
- 2025-08-25 · We have three graduate students joining our group this fall. Welcome aboard Yokyung, Byeongkyu and Jiwoong!
- 2025-08-21 · Ranggi successfully defended his Ph.D. thesis! "Dr." Hwang will be joining Ulsan National Institute of Science and Technology (울산과학기술원) as an Assistant Professor. Congratulations and wish you all the best in your next journey in academia!
- 2025-08-21 · Yunjae successfully defended his Ph.D. thesis! "Dr." Lee will be joining Samsung Electronics (Device Solutions) as a Staff Engineer. Congratulations and wish you all the best in your next journey!
- 2025-08-01 · Our paper titled "Hera: A Heterogeneity-Aware Multi-Tenant Inference Server for Personalized Recommendations" has been accepted for presentation at the 34th International Conference on Parallel Architectures and Compilation Techniques (PACT-34), Irvine, CA. Congratulations Dr. Choi!
- 2025-07-01 · Our paper titled "Mamba-X: An End-to-End Vision Mamba Accelerator for Edge Computing Devices" has been accepted for presentation at the 44th IEEE/ACM International Conference on Computer-Aided Design (ICCAD-44), Munich, Germany. Congratulations Dongho, Gungyu, Jaewon, Yunjae, and Dongjae!
- 2025-06-05 · Juntaek has won the prestigious Korea Presidential Scholarship in Science and Technology (대통령 과학 장학금) this year. Congratulations Juntaek!
- 2025-03-22 · Our paper titled "Debunking the CUDA Myth Towards GPU-based AI Systems" has been accepted for presentation at the 52nd IEEE International Symposium on Computer Architecture (ISCA-52), Tokyo, Japan. Congratulations Yunjae, Juntaek, Jehyeon, Eunyeong, Jinseop, and Ranggi!
- 2025-02-25 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Taehun, Yunjae, and Juntaek!
- 2025-02-24 · We have two graduate students joining our group this spring. Welcome aboard Taekwon and Junga!
- 2025-02-19 · Our paper on uPIMulator (published last year at HPCA-30) has been selected as one of the 2024 Top 10 Research Achievements at KAIST (KAIST 대표연구성과 10선). Congratulations!
- 2025-02-09 · Prof. Rhu is serving as the Program Co-Chair for the 58th IEEE/ACM International Symposium on Microarchitecture (MICRO-58). This marks the first time in MICRO's 58-year history that a faculty member from a university in Asia has been selected as Program Chair.
- 2025-02-08 · Our paper on uPIMulator (published last year at HPCA-30) has been selected as one of the top 24 papers listed as IEEE Micro Top Picks - Honorable Mention(입선)! The featured article will be published on the July/August 2025 issue of "IEEE Micro - Special Issue on Top Picks from the 2024 Computer Architecture Conferences". Congratulations!
- 2024-11-18 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Jiwon and Yunjae!
- 2024-10-11 · Our group's proposal (Primary Investigator: Prof. Rhu, Minsoo) on developing a "high-performance AI model serving system" has been awarded the prestigious Samsung Research Funding & Incubation Center (삼성미래기술육성사업) research grant.
- 2024-09-27 · Bongjoon successfully defended his Ph.D. thesis! "Dr." Hyun will be joining Samsung Electronics (Device Solutions) as a Staff Engineer. Congratulations and wish you all the best in your next journey!
- 2024-09-13 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Eunyeong and Jehyeon!
- 2024-09-02 · We have one graduate student joining our group this fall. Welcome aboard Byeongjun and Jinseop!
- 2024-07-31 · Our group's proposal (Primary Investigator: Prof. Rhu, Minsoo) on developing a "Secure and Private AI System and System Software" has been awarded the prestigious SW Starlab (SW스타랩) research grant (funding period: 8 years).
- 2024-07-18 · Our group has three papers accepted for presentation at the 57th IEEE/ACM International Symposium on Microarchitecture (MICRO-57), Austin, TX. Congratulations Jehyeon, Dongjae, Bongjoon, and Taehun!
- 2024-07-03 · Prof. Rhu is inducted into the ISCA Hall of Fame.
- 2024-07-02 · Prof. Rhu promoted to Tenured Associate Professor.
- 2024-06-22 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Dongho and Taehun!
- 2024-06-10 · Prof. Rhu is appointed as an Associate Editor for IEEE Transactions on Computers.
- 2024-04-11 · Yujeong successfully defended her Ph.D. thesis! "Dr." Choi will be joining Google, Sunnyvale, CA as a Postdoctoral Researcher. Congratulations and wish you all the best in your next journey in the Bay Area!
- 2024-03-30 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Dongjae, Bongjoon and Taehun!
- 2024-03-20 · Our group members will be presenting three papers which are accepted at the 51st IEEE International Symposium on Computer Architecture (ISCA-51), Buenos Aires, Argentina. Congratulations Yujeong, Jiin, Yunjae, Hyeseong, and Ranggi!
- 2024-03-05 · Our work on uPIMulator ("Pathfinding Future PIM Architectures by Demystifying a Commercial PIM Technology") won the Best Paper Award at HPCA-30! This is the first time a research group from Korea won a best paper award at a top-tier computer architecture conference. Congratulations Bongjoon, Taehun, and Dongjae!
- 2024-02-16 · Youngeun successfully graduated with a Ph.D.! "Dr." Kwon will be joining NVIDIA, Santa Clara, CA as a Senior Deep Learning Performance Engineer. Congratulations and wish you all the best in your next journey in the Bay Area!
- 2024-02-15 · Ranggi received an internship offer to join NVIDIA Research this summer. He will be working as a research intern in the Architecture Research Group (ARG) at Austin, TX. Congratulations and have a great summer in the "greatest" city in the US :-)
- 2024-02-15 · We have two graduate students joining our group this spring. Welcome aboard Gungyu and Jaewon!
- 2023-11-12 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Hyeseong and Yunjae!
- 2023-11-08 · Our group has one paper accepted for presentation at the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS-29), San Diego, CA, Mar. 2024. Congratulations Juntaek, Youngeun, and Ranggi!
- 2023-10-23 · Our group has one paper accepted for presentation at the 30th IEEE International Symposium High-Performance Computer Architecture (HPCA-30), Edinburgh, UK, February 2024. Congratulations Bongjoon, Taehun, and Dongjae!
- 2023-09-01 · We have one graduate student joining our group this Fall. Welcome aboard Hyesung !
- 2023-05-15 · Jinha will be joining Samsung Advanced Institute of Technology (SAIT) this upcoming summer~fall as a research intern. Congratulations!
- 2023-04-20 · Prof. Rhu has won the prestigious Google Research Scholar Award.
- 2023-02-01 · We have three graduate students joining our group this spring. Welcome aboard Eunyeong / Seongjin / Hyeseong !
- 2022-12-12 · Prof. Rhu is elected as a member of the next generation Korean Academy of Science and Technology (Y-KAST).
- 2022-11-30 · Our group has a paper accepted for publication at IEEE Computer Architecture Letters. Congratulations Seonho and Ranggi!
- 2022-11-22 · Prof. Rhu is elevated to IEEE Senior Member.
- 2022-10-18 · Our group has one paper accepted for presentation at the 29th IEEE International Symposium High-Performance Computer Architecture (HPCA-29), Montreal, Canada, February 2023. Congratulations Ranggi, Minhoo, and Jiwon!
- 2022-10-05 · Prof. Rhu is inducted into the MICRO Hall of Fame.
- 2022-09-16 · Jinha has won the Best TA Award for his contributing role as head TA in EE209: Programming Structure for Electrical Engineering course in Spring 2022. Congratulations Jinha!
- 2022-09-08 · Yujeong has won the prestigious Google Ph.D. Fellowship Award this year. Congratulations Yujeong!
- 2022-07-20 · Our group has two papers accepted for presentation at the 55th IEEE/ACM International Symposium on Microarchitecture (MICRO-55), Chicago, IL. Congratulations Beomsik, Ranggi, Dongho, and Yoonhyuk!
- 2022-06-28 · We have one graduate student joining our group this fall. Welcome aboard Juntaek!
- 2022-06-27 · We have three undergraduate research interns joining us this summer. Welcome aboard Eunjee / Jinwoo / Yoonsoo!
- 2022-05-01 · Ranggi will be joining Microsoft Research Asia, Beijing this upcoming fall semester as a research intern. Congratulations!
- 2022-03-03 · Our group has three papers accepted for presentation at the 49th IEEE International Symposium on Computer Architecture (ISCA-49), New York, NY. Congratulations Yunjae, Jinha, and Youngeun!
- 2022-02-23 · We have four undergraduate research interns joining us this spring. Welcome aboard Eunyeong / Joontaek / Hankyul / Hyeseong !
- 2022-02-22 · Our paper titled "PARIS and ELSA: An Elastic Scheduling Algorithm for Reconfigurable Multi-GPU Inference Servers" has been accepted for presentation at the 59th ACM/ESDA/IEEE Design Automation Conference (DAC), San Francisco, CA, Jul. 2022. Congratulations Yunseong and Yujeong!
- 2022-02-21 · We have four graduate students joining our group this spring. Welcome aboard Dongjae / Gwangoo / Jiin / Yoonhyuk!
- 2021-12-15 · We have five undergraduate research interns joining us this winter. Welcome aboard Eunyeong / Sunho / Joontaek / Seungjae / Hankyul !

## 연락과 위치

- 교수 연구실: IT융합빌딩(N1) 809호, 전화 042-350-7447[^eeprof][^ssefac]
[^home]: 연구실 누리집 첫 화면 <https://sites.google.com/view/kaist-via> (연구실 소개, Latest News, 2026-10-22 열람)
[^research]: Research 페이지 <https://sites.google.com/view/kaist-via/research> (Computer Architecture, Machine Learning 항목, 2026-10-22 열람)
[^people]: People 페이지 <https://sites.google.com/view/kaist-via/people> (Ph.D. Students, M.S. Students, Alumni (Ph.D.), Alumni (M.S.), Undergraduate Research Interns 칸, 2026-10-22 열람)
[^pubs]: Publications 페이지 <https://sites.google.com/view/kaist-via/publications> (2026–2009년 연도 구역, 2026-10-22 열람)
[^news]: News 페이지 <https://sites.google.com/view/kaist-via/news> (2026–2017년 연도 구역, 2026-10-22 열람)
[^awards]: Awards 페이지 <https://sites.google.com/view/kaist-via/awards> (Primary Investigator International·Domestic, Student Awards, 2026-10-22 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(유민수) <https://ee.kaist.ac.kr/professor/16045/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 디비전, 학위, 대표업적, 2026-10-22 열람)
[^ssefac]: KAIST 반도체시스템공학과 교수진 목록 <https://sse.kaist.ac.kr/professor/> (유민수 교수 항목, 2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (컴퓨터 시스템 아키텍쳐 연구실 항목, 2026-10-22 열람)
[^p1]: E. Cho, J. Bang, R. Hwang, M. Rhu, 2026 IEEE International Symposium on High Performance Computer Architecture (HPCA), 1-16 (2026). <https://doi.org/10.1109/hpca68181.2026.11408493> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Kim, B. Shin, J. Chung, M. Rhu, 2026 IEEE International Symposium on High Performance Computer Architecture (HPCA), 1-16 (2026). <https://doi.org/10.1109/hpca68181.2026.11408569> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Bang 외, M. Rhu, 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO), 153-167 (2024). <https://doi.org/10.1109/micro61859.2024.00021> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: Y. Lee 외, M. Rhu, Proceedings of the 52nd Annual International Symposium on Computer Architecture, 1760-1776 (온라인 2025-06-20). <https://doi.org/10.1145/3695053.3731050> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: B. Hyun, T. Kim, D. Lee, M. Rhu, 2024 IEEE International Symposium on High-Performance Computer Architecture (HPCA), 263-279 (2024). <https://doi.org/10.1109/hpca57654.2024.00029> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: Y. Choi, J. Kim, M. Rhu, 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA), 410-423 (2024). <https://doi.org/10.1109/isca59077.2024.00038> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: B. Park 외, M. Rhu, 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO), 1200-1217 (2022). <https://doi.org/10.1109/micro56248.2022.00084> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: D. Yoon 외, M. Rhu, 2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD), 1-9 (2025). <https://doi.org/10.1109/iccad66269.2025.11240777> 초록 기준(Semantic Scholar 등록 초록).

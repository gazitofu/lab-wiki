# 가속화지능형시스템연구실 (Accelerated Intelligent Systems Lab, AISys)

**서울대학교 공과대학 전기·정보공학부, 첨단융합학부 차세대지능형반도체전공, 협동과정 인공지능 전공 · 이진호 부교수**

- 분야: 인공지능 시스템과 컴퓨터 구조, AI 가속기 설계와 메모리 안 연산(PIM), 분산 딥러닝 학습 시스템, 신경망 양자화·압축, GPU·PIM 같은 새 하드웨어 위의 응용 가속(그래프 처리, 벡터 검색, 유전체 서열 정렬, 데이터베이스)
- 대분야: 컴퓨팅·AI, 전기전자·반도체·광학
- 태그: AI 시스템·인프라[^home][^p3][^p4], AI 반도체·가속기[^research][^p1][^p2], 메모리 내 연산[^research][^p1][^p8], 컴퓨터 구조·운영체제[^home][^ecelabd], 대형 언어 모델[^research][^p3][^p5]
- 홈페이지: <https://aisys.snu.ac.kr>
- 근거와 출처: [AISys 근거 페이지](aisys-sources.md)

> 딥러닝, 압축 알고리즘, 그래프 처리 같은 응용을 빠르게 돌리기 위한 컴퓨터 시스템과 하드웨어 구조를 연구하는 연구실이다. AI 전용 가속기, 여러 GPU로 나눠 하는 딥러닝 학습, 신경망 양자화와 압축, GPU·메모리 안 연산 장치 같은 새 하드웨어 위의 프로그램 최적화를 주로 다룬다.[^home][^research]

## 무엇을 연구하나

연구실은 서울대학교 공과대학 전기·정보공학부 이진호 부교수가 이끄는 연구실이다.[^eceprof][^ecelabd] 누리집은 이름을 Accelerated Intelligent Systems Lab(AISys)으로 적고, 서울대 전기·정보공학부(ECE)에 속한 연구실이라고 밝힌다.[^home] 학과 연구실 소개는 연구 분야를 "인공지능 시스템 및 최적화, 컴퓨터 구조"로 적고,[^ecelabd] 학과 연구실 목록은 이 연구실을 스마트 임베디드 시스템, 인공지능 및 머신러닝, 차세대 컴퓨팅, 빅데이터 및 인공지능 플랫폼의 네 연구그룹에 함께 올린다.[^ecelab] 연구실은 딥러닝, 압축 알고리즘, 그래프 처리(점과 그 사이를 잇는 선으로 이뤄진 연결 구조 자료를 다루는 계산) 같은 여러 응용을 빠르게 돌리기 위한 시스템과 컴퓨터 구조(프로세서·메모리 같은 컴퓨터 하드웨어를 어떻게 짜고 잇는지에 관한 설계) 문제를 연구하며, 특히 FPGA(Field-Programmable Gate Array, 만든 뒤에도 회로 구성을 바꿔 쓸 수 있는 반도체 칩)와 GPU(많은 계산을 한꺼번에 나눠 처리하는 그래픽 처리 장치) 위에서 연구한다고 적는다.[^home][^research] 누리집은 석박사 신입생과 학부생 인턴을 늘 뽑는다고 알린다.[^home]

연구 페이지는 진행 중인 연구 주제를 네 가지로 소개하고, 스스로 정한 주제를 가져와도 된다고 덧붙인다.[^research] 첫째는 AI 가속기(인공지능 계산을 빠르게 하도록 만든 전용 하드웨어)다. 지금 AI에 가장 많이 쓰는 가속기는 GPU지만 흐름이 AI 전용 가속기로 옮겨 가고 있어 가속기 설계에 개선할 여지가 많다고 보고, 예로 데이터 흐름(dataflow, 계산 단계 사이에서 데이터가 옮겨 가는 순서와 경로) 최적화, 희소 신경망 구조(값 대부분이 0인 연결을 가진 신경망) 활용, 메모리 안 연산(PIM, Processing-In-Memory, 데이터를 프로세서로 옮기지 않고 메모리 안이나 가까이에서 계산하는 방식) 기법을 든다.[^research] 둘째는 분산 딥러닝이다. 심층 신경망(DNN, Deep Neural Network, 여러 층의 인공 신경망을 겹쳐 쌓은 모델)을 빠르게 학습하려고 GPU 같은 장치 여러 대를 함께 쓰는 분산 학습에서, 새 통신 알고리즘을 고안하거나, 작업들을 파이프라인(앞 작업이 끝나기 전에 다음 작업을 겹쳐 진행하는 방식)으로 잘 엮거나, 장치끼리 동기화하는 방식을 바꾸는 개선 방향을 든다.[^research]

셋째는 신경망 가속과 압축이다. 심층 신경망을 효율적으로 쓰고 학습하려면 계산과 메모리 부담을 함께 줄여야 한다고 보고, 앞선 양자화(숫자를 더 적은 비트로 나타내 계산과 저장을 줄이는 기법)와 압축 기법으로 추론(학습을 마친 모델로 답을 내는 일)과 학습을 모두 빠르게 하는 데 집중한다.[^research] 대상 모델로는 대형 언어 모델(LLM, Large Language Model), 확산 모델(잡음에서 출발해 조금씩 걷어 내며 이미지를 만드는 생성 모델) 기반 이미지 생성, 그래프 신경망(그래프 자료를 다루는 신경망), 스파이킹 신경망(신호를 짧은 펄스로 주고받는 신경망)을 들고, 정확도를 크게 잃지 않으면서 여러 하드웨어에서 빠르고 자원을 적게 쓰는 학습과 추론을 목표로 한다.[^research] 넷째는 시스템 최적화와 가속이다. GPU, CXL(Compute Express Link, 프로세서와 메모리·가속기를 빠르게 잇는 연결 규격), PIM 같은 새 상용 하드웨어 위에서 여러 프로그램과 응용을 최적화하고 가속하며, 통신 라이브러리, 그래프 처리 알고리즘, 벡터 데이터베이스(자료를 숫자 묶음인 벡터로 저장해 비슷한 자료를 찾는 데이터베이스), 과학 응용을 다룬다. 하드웨어 특성을 고려한 가속과 알고리즘 최적화를 함께 써서 시스템 소프트웨어를 최적화하고 실제 작업의 성능을 크게 높이는 것을 목표로 한다고 적는다.[^research]

대표 논문으로 보면, AI 가속기 갈래에서는 미리 계산한 결과를 표에 넣어 두고 찾아 쓰는 룩업 테이블(LUT, Look-Up Table)을 DRAM 기반 메모리 안 연산 장치에 두고, 곱셈·누산 연산 여러 개를 한 번의 표 찾기로 묶어 적은 비트로 양자화한 신경망의 추론을 빠르게 하는 LoCaLUT을 만들었고,[^p1] 신경망 구조와 하드웨어 가속기 설계를 미분 가능한 방식으로 함께 찾는 DANCE++를 내놓았다.[^p2] 분산 학습 갈래에서는 실제 GPU 클러스터(여러 컴퓨터를 묶어 한 시스템처럼 쓰는 장비 무리)의 연결 속도 차이와 GPU마다의 메모리 한도를 반영해 대형 언어 모델 학습의 병렬화 설정을 자동으로 찾는 Pipette와,[^p3] 서버 여러 대로 이뤄진 클러스터에서 그래프 신경망을 빠르게 학습하는 GraNNDis를 만들었다.[^p4] 양자화·압축 갈래에서는 낮은 비트 부동소수점 형식인 FP8로 양자화한 본체 모델에 LoRA 어댑터를 바로 합쳐 대형 언어 모델의 미세조정을 빠르게 하는 FALQON과,[^p5] 원래 학습 데이터 없이 비전 트랜스포머를 낮은 비트로 양자화하는 MimiQ를 내놓았다.[^p6] 시스템 최적화 갈래에서는 여러 GPU로 그래프 기반 근사 최근접 이웃 검색을 빠르게 하는 PathWeaver와,[^p7] 상용 PIM 메모리 모듈 안 처리 소자들 사이의 집단 통신을 빠르게 하는 PID-Comm을 만들었다.[^p8]

최근 논문 목록에는 이 밖에도 저장장치 가까이에서 계산하는 장치로 대형 언어 모델을 학습하거나 긴 문맥의 대형 언어 모델을 추론하는 연구(HPCA 2024, ASPLOS 2026), 저장장치를 써서 메모리가 부족해도 그래프 전체로 그래프 신경망을 학습하는 연구(MLSys 2026), 낸드 플래시 메모리 안에서 계산하는 연구(MICRO 2025, MICRO 2026 채택), GPU로 데이터베이스 질의를 빠르게 하는 연구(PACT 2025, ICDE 2026), GPU로 유전체 서열 정렬을 빠르게 하는 연구(PPoPP 2024, ICS 2025)가 있다.[^pubs] 학습 데이터 없이 적대적 공격(사람이 알아채기 어려운 작은 입력 변화로 인공지능의 판단을 틀리게 만드는 공격)을 막는 연구(ICML 2024), 검색 증강 언어 모델(외부 문서를 찾아 답에 참고하는 언어 모델)을 겨냥한 데이터 오염 공격 연구(EMNLP 2026 채택), 영상에서 인공위성 궤적 잡음을 지우는 연구(ECCV 2026), 적외선 밝기·색과 시간에 따른 변화를 기계학습으로 분석해 어린 별(YSO)과 AGB 별(진화 후기 단계의 별)을 분류하는 천체물리 연구(The Astrophysical Journal, 2026), 웨이퍼 제조 결함에서 패턴을 나눠 내는 연구(DAC 2026)도 올라 있다.[^pubs]

## 주요 연구 주제

### 1. AI 가속기와 메모리 안 연산

데이터 흐름 최적화, 희소 신경망 구조 활용, 메모리 안 연산 기법으로 AI 전용 가속기의 설계를 개선한다.[^research] DRAM 기반 메모리 안 연산 장치에서 룩업 테이블로 양자화 신경망의 추론을 빠르게 하는 LoCaLUT, 신경망 구조와 가속기 설계를 함께 찾는 DANCE++가 이 갈래다.[^p1][^p2] 대표 논문 1, 2.

### 2. 분산 딥러닝 학습

장치 여러 대로 심층 신경망을 학습할 때의 통신 알고리즘, 작업 파이프라인, 장치 사이 동기화 방식을 개선한다.[^research] 실제 GPU 클러스터에서 대형 언어 모델의 학습 설정을 자동으로 찾는 Pipette, 여러 서버에서 그래프 신경망을 학습하는 GraNNDis가 이 갈래다.[^p3][^p4] 대표 논문 3, 4.

### 3. 신경망 양자화와 압축

대형 언어 모델, 확산 모델 기반 이미지 생성, 그래프 신경망, 스파이킹 신경망의 추론과 학습을 양자화와 압축으로 빠르게 한다.[^research] FP8로 양자화한 모델의 LoRA 미세조정을 빠르게 하는 FALQON, 원래 학습 데이터 없이 비전 트랜스포머를 양자화하는 MimiQ가 이 갈래다.[^p5][^p6] 대표 논문 5, 6.

### 4. GPU·PIM 같은 새 하드웨어 위의 시스템 최적화

GPU, CXL, PIM 같은 상용 하드웨어 위에서 통신 라이브러리, 그래프 처리 알고리즘, 벡터 데이터베이스, 과학 응용을 최적화하고 가속한다.[^research] 여러 GPU로 근사 최근접 이웃 검색을 빠르게 하는 PathWeaver, PIM 메모리 모듈의 처리 소자 사이 집단 통신 틀인 PID-Comm이 이 갈래다.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 논문 가운데 교수가 서울대에 온 뒤인 2024–2026년에 나왔고 이진호 교수가 마지막 저자인 학회·학술지 논문을, 네 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM](https://doi.org/10.1109/hpca68181.2026.11408523) · HPCA 2026 | 룩업 테이블(LUT)은 입력값을 미리 계산해 둔 결과에 바로 대응시키는 계산 방식이라 산술 회로가 필요 없다. 회로를 단순하게 할 뿐 아니라 비트 수마다 따로 회로를 두지 않고도 여러 숫자 정밀도를 다룰 수 있어, 양자화한 심층 신경망에서 점점 중요해지는 성질을 갖는다. 대역폭이 크고 메모리는 넉넉하지만 넣을 수 있는 논리 회로가 적은 DRAM 기반 메모리 안 연산(DRAM-PIM)에서는 메모리 용량을 논리 회로 대신 써서 계산 처리량을 높이는 맞바꿈이 잘 맞는다. 이 연구는 곱셈·누산(MAC) 연산 여러 개를 한 번의 표 찾기로 묶어 메모리 용량과 성능을 맞바꾸는 PIM 설계 LoCaLUT을 제안했다. 표 안의 중복 항목을 없애 표 크기를 줄이는 LUT 정규화, 가중치 묶음을 정규화에 필요한 형태로 바꿔 주는 작은 보조 표인 재배열 LUT, 필요한 표 열만 버퍼로 흘려보내 여러 가중치 묶음에 다시 쓰는 LUT 조각 스트리밍을 더했다. UPMEM 장치로 만든 실제 시스템에서 여러 숫자 정밀도와 신경망 모델에 걸쳐 기하평균 1.82배 빨라졌다.[^p1] | 1저자 J. Hong, 마지막 저자 이진호 |
| 2 | 2026 | [DANCE++: Differentiable Accelerator/Network Co-Exploration With Hard Constraints and Data-Free Training for Real-World Scenarios](https://doi.org/10.1109/tcad.2025.3582196) · IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems | 신경망 구조와 하드웨어 가속기를 함께 찾는 공동 탐색은 특히 사양이 낮은 시스템의 계산 비용 문제를 풀 방법으로 떠올랐지만, 강화학습이나 진화 탐색에 기반한 기존 방법은 탐색 비용이 크다. 이 연구는 하드웨어와 신경망 구조를 미분 가능한 방식으로 함께 탐색하는 DANCE++를 내놓았다. 핵심은 하드웨어 지표를 신경망으로 본뜬 미분 가능한 평가 신경망으로, 이것으로 역전파(출력의 오차를 거꾸로 전해 가며 값을 고치는 계산)를 거쳐 가속기를 설계할 수 있다. 기존 방법보다 탐색 시간을 크게 줄이고 정확도와 하드웨어 비용 지표를 개선했다. 실제 상황을 위해 두 가지를 더 다뤘다. 초당 프레임 수 같은 엄격한 제약을 지키는 해를 찾도록 미분 가능한 최적화를 이끄는 기울기 조작 알고리즘을 제안했고, 학습 데이터에 접근할 수 없는 경우를 위해 공동 탐색과 학습 단계 모두에 데이터 없이 학습하는 방법을 썼다.[^p2] | 1저자 K. Choi, 마지막 저자 이진호 |
| 3 | 2024 | [Pipette: Automatic Fine-Grained Large Language Model Training Configurator for Real-World Clusters](https://doi.org/10.23919/date58400.2024.10546826) · DATE 2024 | 대형 언어 모델은 계산량과 메모리 요구가 커서, 흔히 GPU 클러스터에서 데이터 묶음, 파이프라인 단계, 층 안의 텐서(여러 차원의 숫자 배열) 세 방향으로 모델을 나누는 3차원 병렬화로 학습한다. 그러면 방향마다 몇 갈래로 나눌지와 나눈 모델을 어느 GPU에 둘지 정하는 문제가 새로 생긴다. 최적 설정을 자동으로 찾으려던 이전 연구들은 실제 클러스터에서 연결 링크마다 실제로 얻는 대역폭이 다르다는 점을 흔히 무시했고, 통신을 제대로 고려하지 않은 핵심 경로 모델링 탓에 최적이 아닌 설정에 빠지기 쉬웠으며, GPU마다 필요한 메모리를 고려하지 않아 실행할 수 없는 설정을 추천하기도 했다. 이 연구는 실제 클러스터를 위한 자동 세밀 학습 설정 도구 Pipette를 제안했다. 더 나은 성능 모델, 메모리 추정기, GPU 하나하나를 세밀하게 배정하는 방법으로 메모리 제약을 지키면서 더 빠른 설정을 찾았고, 큰 클러스터에서 이전 방법보다 크게 빨라졌음을 보였다.[^p3] | 공동 1저자 J. Yim, J. Song, 마지막 저자 이진호 |
| 4 | 2024 | [GraNNDis: Fast Distributed Graph Neural Network Training Framework for Multi-Server Clusters](https://doi.org/10.1145/3656019.3676892) · PACT 2024 | 그래프 신경망(GNN)은 딥러닝에서 빠르게 커 가는 분야다. 학습 처리량을 높이려는 분산 GNN 학습 틀이 많이 나왔지만, 서버 여러 대로 이뤄진 클러스터에서는 세 가지 한계가 있다. 서버 사이와 서버 안의 대역폭 차이를 고려하지 않아 서버 사이 통신이 병목이 되고, 겹치는 메모리 사용과 계산이 규모 확장을 막으며, 미니배치 학습(자료를 작은 묶음으로 나눠 차례로 학습하는 방식)의 사실상 표준인 표본 추출이 불필요한 오차를 낳는다. 이 연구는 이 한계들을 여러 서버 클러스터의 특성을 이용해 푸는 GraNNDis를 제안했다. 필요한 정점 의존 관계를 서버별로 미리 실어 두어 느린 서버 사이 통신을 줄이는 유연한 사전 적재, 빠른 서버 안 통신을 써서 메모리를 아끼고 중복을 줄이는 협력 배칭, 속도 향상에 영향을 주는 서버 경계 부분만 표본으로 뽑는 확장 인식 표본 추출, 이를 여러 서버 환경에서 구현하는 계산·통신 구조인 한 단계 그래프 마스킹을 더했다. 여러 서버 클러스터에서 최신 분산 GNN 학습 틀보다 크게 빨랐다.[^p4] | 1저자 J. Song, 마지막 저자 이진호 |
| 5 | 2025 | [FALQON: Accelerating LoRA Fine-tuning with Low-Bit Floating-Point Arithmetic](https://doi.org/10.52202/085713-4110) · NeurIPS 2025 | FP8 같은 낮은 비트 부동소수점 형식은 최신 GPU와 NPU(신경망 계산 전용 처리 장치)가 하드웨어로 지원해 모델 학습을 크게 빠르게 하고 메모리를 아낀다. 그런데 분석해 보니 FP8 양자화는 큰 차원의 행렬 곱셈에서 주로 빨라지고, 대형 언어 모델을 효율적으로 미세조정하려고 작은 차원의 행렬을 쓰는 LoRA(저랭크 적응)에서는 양자화에 드는 부담 때문에 속도 이득이 줄었다. 이를 풀려고, 미세조정 중에 LoRA 어댑터를 FP8로 양자화한 본체 모델에 바로 합쳐 따로 도는 LoRA 계산 경로의 양자화 부담을 없애는 FALQON을 제안했다. 합친 어댑터의 순전파와 역전파 계산(입력에서 출력으로 가는 계산과 오차를 거꾸로 전하는 계산)을 다시 짜 양자화 부담을 크게 줄이고, 큰 갱신을 양자화된 본체에 효율적으로 반영하는 행 단위 대리 갱신 방식도 더했다. 기존 양자화 LoRA 방법과 비슷한 정확도에서 학습이 약 3배 빨라졌고, 처음부터 끝까지 FP8로 진행해 학습 뒤 따로 양자화할 필요가 없어 배포도 쉬워진다.[^p5] | 1저자 K. Choi, 마지막 저자 이진호 |
| 6 | 2025 | [MimiQ: Low-Bit Data-Free Quantization of Vision Transformers with Encouraging Inter-Head Attention Similarity](https://doi.org/10.1609/aaai.v39i15.33761) · AAAI 2025 | 데이터 없는 양자화(DFQ)는 원래 학습 데이터 없이, 흔히 합성 데이터를 만들어 원래 정밀도의 신경망에서 가벼운 신경망을 얻는 기법이다. 비전 트랜스포머(ViT, 이미지를 작은 조각으로 나눠 조각 사이 관계를 학습하는 신경망 구조)를 위한 DFQ 방법이 여럿 나왔지만 낮은 비트에서는 효과를 내지 못했다. 기존 방법의 합성 데이터는 어텐션 맵(신경망이 입력의 어느 부분에 주목하는지 나타낸 지도)이 서로 어긋나는 반면 실제 데이터의 어텐션 맵은 잘 맞아 있다는 점을 관찰했고, 합성 데이터의 어텐션 맵을 맞추면 양자화한 ViT의 성능이 좋아진다는 것을 찾았다. 이를 바탕으로 어텐션 헤드 사이의 유사성을 높이는 DFQ 방법 MimiQ를 만들었다. 먼저 공간 위치별 질의 조각마다 헤드별 어텐션 출력을 맞춰 합성 데이터를 만들고, 이어 헤드별 구조적 어텐션 증류(원래 모델의 주목 방식을 양자화한 모델이 따라 배우게 하는 학습)로 양자화한 신경망의 어텐션 맵을 원래 정밀도의 교사 신경망에 맞췄다. 실험에서 비교 방법들보다 크게 나은 성능을 보였다.[^p6] | 1저자 K. Choi, 마지막 저자 이진호 |
| 7 | 2025 | [PathWeaver: A High-Throughput Multi-GPU System for Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/html/2507.17094v1) · USENIX ATC 2025 | 그래프 기반 근사 최근접 이웃 검색(ANNS, 질의와 가장 비슷한 자료를 정확도를 조금 양보하고 빠르게 찾는 검색)은 추천 시스템, 자연어 처리, 컴퓨터 비전 등에 널리 쓰인다. GPU 가속으로 ANNS 성능이 크게 나아졌지만 자료 규모가 계속 커져 여러 GPU를 효율적으로 쓰는 방법이 필요해졌다. 기존 방법은 GPU를 늘려도 큰 자료를 담을 메모리를 넓히는 데만 써서, 자료를 나눈 뒤 GPU마다 따로 비슷한 점을 찾는 비효율이 있었다. 이 연구는 큰 자료의 ANNS를 여러 GPU로 확장하고 빠르게 하는 PathWeaver를 제안했다. GPU 사이 통신을 써서 이전 방법의 중복 탐색 반복을 줄이는 파이프라인 기반 경로 확장, 대표 자료 묶음으로 질의의 좋은 출발점을 찾아 어려운 질의의 탐색 범위를 줄이는 고스트 스테이징, 탐색 초반에 관련 없는 점을 걸러 불필요한 메모리 접근과 거리 계산을 줄이는 방향 안내 선택을 더했다. 여러 자료에서 95% 재현율(찾아야 할 이웃 가운데 실제로 찾은 비율) 기준으로 최신 다중 GPU ANNS 틀보다 기하평균 3.24배, 최대 5.30배 빨랐다.[^p7] | 1저자 S. Kim, 마지막 저자 이진호 |
| 8 | 2024 | [PID-Comm: A Fast and Flexible Collective Communication Framework for Commodity Processing-in-DIMM Devices](https://doi.org/10.1109/isca59077.2024.00027) · ISCA 2024 | 최근의 DIMM(컴퓨터에 꽂는 메모리 모듈)은 메모리 뱅크에 처리 소자(PE)를 붙여 메모리 안 연산(PIM)을 지원하기 시작했다. 메모리를 많이 쓰는 연산을 처리 소자에 맡겨 데이터 이동 병목을 넘을 수 있지만, 처리 소자 사이 집단 통신(여러 처리 장치가 함께 데이터를 모으거나 나눠 주는 통신)의 큰 부담 때문에 속도 향상이 막히곤 하며, 이는 주로 CPU를 거치는 느린 통신 방식에서 온다. 이 연구는 상용 PIM DIMM을 위한 빠르고 유연한 처리 소자 사이 집단 통신 틀 PID-Comm을 제안했다. 처리 소자들을 다차원 하이퍼큐브(정육면체를 여러 차원으로 넓힌 연결 모양)로 추상화하고, 하이퍼큐브의 특정 차원에 속한 처리 소자끼리 여러 집단 통신을 함께 할 수 있게 했다. 이를 바탕으로 응용이 복잡한 통신을 쉽게 나타내도록 처리 소자 사이 집단 통신 패턴 여덟 가지를 정의하고, DIMM에 맞춰 최적화한 고성능 구현을 제공했다. UPMEM DIMM 16개와 대표적인 병렬 알고리즘으로 평가한 결과, 기존 통신 구현보다 최대 5.19배 빨라졌다.[^p8] | 공동 1저자 S. U. Noh, J. Hong, 마지막 저자 이진호 |

## 교수와 전문 분야

이진호 교수는 서울대학교에서 전기공학부 학사(2009년 2월), 전기컴퓨터공학부 석사(2011년 2월)와 박사(2016년 2월)를 받았다.[^eceprof] 학과 교수 소개는 주요 경력을 2016–2019년 IBM 박사후연구원(Postdoc.)·연구원(Research Staff Member), 2019–2022년 연세대학교 컴퓨터과학과·인공지능학과 조교수, 2022년부터 서울대학교 전기정보공학부 조교수로 적는다.[^eceprof] 교수 개인 페이지는 서울대에 오기 전 연세대 컴퓨터과학과와 IBM(Austin)에 있었다고 적고,[^prof] 랩 소식은 교수가 2019년 9월 연세대 컴퓨터과학과에, 2023년 9월 서울대 전기·정보공학부에 조교수로 왔다고 적는다.[^news] 지금 학과 교수 소개와 협동과정 인공지능 전공·첨단융합학부의 교수진 목록은 직위를 부교수로 적고, 첨단융합학부 목록은 차세대지능형반도체전공 칸에 교수를 올린다.[^eceprof][^gsai][^snuti]

누리집 Lecture 페이지는 2019년 가을부터 2025년 봄까지 학기마다 맡은 강의를 적는다. 학부 과목으로 Programming Methodology, Logic Circuit Design, Multicore and GPU Programming, Digital System Design, Embedded System Design, Creative Engineering Design 등을, 대학원 과목으로 Parallel and Distributed Computing, Memory-centric Computing Systems, Memory Systems and Interconnection Networks, Parallel and Distributed Programming을 든다.[^lecture] 랩 소식은 교수가 2020년 연세대 Best Teaching Award를 받았다고 적는다(2021년 3월 소식).[^news] 연구실 논문으로는 PACT 2022에서 Slice-and-Forge가 Best Paper Award를, HPCA 2024에서 Smart-Infinity가 Best Paper Award Honorable Mention(입선)을 받았고, HPCA 2026에서는 LoCaLUT이 Best Paper Candidates 세션에서 발표되었다.[^news][^pubs]

교수 개인 페이지는 연구 관심을 AI 시스템을 위한 가속기와 구조 최적화로 적고,[^prof] 학과 교수 소개는 Research Interest를 ML systems and optimizations와 Computer architecture로, 분야를 "인공지능 시스템 및 최적화, 컴퓨터 구조"로 적는다.[^eceprof] 랩 Publications 페이지의 목록을 시기별로 보면, 2009–2015년 논문은 3차원 온칩 네트워크(NoC, 칩 안의 여러 코어와 메모리를 잇는 통신망)의 경로 설정과 여러 코어를 담은 SoC(시스템 하나를 칩 하나에 담은 반도체)의 작업 배치·일정을 주로 다룬다. 2016–2017년 논문은 DRAM 안의 숨은 병렬성을 끌어내는 연산 구조와 저장장치 가까이에서 그래프를 처리하는 가속기를, 2017–2020년 논문은 FPGA로 하는 데이터베이스 가속, 데이터 압축 풀기, 그래프 데이터베이스, 분산 딥러닝의 통신(FlexReduce) 등을 다룬다. 2021년 이후 논문은 AI 가속기, 메모리 안 연산, 분산 학습 시스템, 신경망 양자화가 중심이다.[^pubs]

논문으로 보면 서울대 시기의 전문 분야는 네 갈래다. 첫째, 메모리 안 연산 장치와 전용 가속기로 신경망 계산을 빠르게 하는 하드웨어 구조 설계다(대표 논문 1, 2).[^p1][^p2] 둘째, GPU 클러스터에서 대형 언어 모델과 그래프 신경망의 학습을 나눠 빠르게 하는 분산 학습 시스템이다(대표 논문 3, 4).[^p3][^p4] 셋째, 정확도를 지키면서 낮은 비트로 신경망을 학습·추론하는 양자화 기법이다(대표 논문 5, 6).[^p5][^p6] 넷째, 여러 GPU와 상용 PIM 메모리 모듈 위에서 검색과 통신을 빠르게 하는 시스템 소프트웨어다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

누리집은 가속하려는 응용으로 딥러닝, 압축 알고리즘, 그래프 처리를 들고,[^home] 시스템 최적화 갈래에서는 통신 라이브러리, 그래프 처리 알고리즘, 벡터 데이터베이스, 과학 응용에서 실제 작업의 성능을 높이려 한다고 적는다.[^research] 대표 논문은 대형 언어 모델의 학습과 미세조정,[^p3][^p5] 서버 여러 대에서의 그래프 신경망 학습,[^p4] 추천 시스템·자연어 처리·컴퓨터 비전에 쓰이는 근사 최근접 이웃 검색,[^p7] 초당 프레임 수 같은 제약이 있는 실제 상황의 신경망·가속기 설계[^p2]를 대상으로 한다. 최근 논문 목록에는 유전체 서열 정렬, GPU 데이터베이스 질의, 천체 분류, 웨이퍼 제조 결함 분석을 다룬 연구도 있다.[^pubs] 누리집 People 페이지 Alumni 칸은 이전 구성원의 진로로 Hana Bank(하나은행), Sapeon, Jane Street를 적는다.[^people]

## 구성원

2026년 10월 23일 랩 People 페이지 기준이다. Graduate Students 칸의 18명이며, 과정은 카드 표기(Postdoc Researcher, PhD Student, MS/PhD Student)를 옮겼다.[^people] 연구 주제는 각자의 개인 페이지 소개 글에서 연구 관심을 밝힌 문장을 그대로 옮겼고, 시작은 개인 페이지 Education 칸에 적힌 지금 과정의 시작 연월이며, 이메일은 개인 페이지 Email 단추에 걸린 학교 주소다.[^member] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Kanghyun Choi | 박사후연구원 |  | My research focuses on neural network optimization, particularly in developing advanced quantization and compression techniques for deep learning models. | kanghyun.choi@snu.ac.kr | 2, 5, 6 |
| Jaeyong Song | 박사과정 | September 2023 | My research interests are systems and architectures for AI, such as distributed AI systems and AI accelerators. | jaeyong.song@snu.ac.kr | 3, 4 |
| Hyeyoon Lee | 박사과정 | September 2023 | I am interested in building safe and efficient AI, where the applications include building adversarially robust AI, and accelerating heavy generative AI. | hylee817@snu.ac.kr | 2, 5, 6 |
| Jaewon Jung | 박사과정 | September 2023 | My research interests are adversarial robustness, large language model and distributed learning. |  | 3, 4 |
| Seongyeon Park | 석박사통합과정 |  | My research interests are accelerating applications (e.g., bioinformatics, graph processing) with GPUs. | syeonp@snu.ac.kr | 1, 7, 8 |
| Hongsun Jang | 석박사통합과정 | Mar. 2023 | My research aims to overcome memory and communication bottlenecks in large-scale AI. | hongsun.jang@snu.ac.kr | 3, 4 |
| Junguk Hong | 박사과정 |  | My research interests are systems for AI and accelerating applications. | junguk16@snu.ac.kr | 1, 7, 8 |
| SunJong Park | 석박사통합과정 |  | My primary research interests lie in the exciting fields of graph neural networks and spiking neural networks. | ryan0507@snu.ac.kr | 5, 6 |
| Si Ung Noh | 석박사통합과정 |  | My research interests include AI accelerators and systems for AI. | siung98@snu.ac.kr | 1, 7, 8 |
| Hunseong Lim | 석박사통합과정 | Feb. 2024 |  | hunseong.lim@snu.ac.kr | 4, 7 |
| Changmin Shin | 석박사통합과정 | Feb.2024 | My research interests are computer architectures, such as processing-in-memory and domain specific accelerators. | scm8432@snu.ac.kr | 1 |
| Sukjin Kim | 석박사통합과정 |  | My research focuses on vector databases, with a particular interest in accelerating large-scale similarity search in multi-GPU environments and exploring Compute Express Link (CXL) technologies for high-performance data processing. | iamksj1212@snu.ac.kr | 1, 7 |
| Jun Sung | 석박사통합과정 | Feb. 2025 | My research focuses on computer architecture. | junsung3737@snu.ac.kr |  |
| Dain Kwon | 석박사통합과정 | March 2025 | I am interested in efficient AI, quantization, and innovative ideas to deploy AI in resource-constrained environments while preserving task performance. | dain.kwon@snu.ac.kr | 5, 6 |
| Woobeen Jo | 석박사통합과정 | Aug.2025 | My research interests include computer architectures. | chowoobin102@snu.ac.kr |  |
| Taehee Kwon | 석박사통합과정 | Aug.2025 |  | jessica314@snu.ac.kr | 1, 7 |
| Shingeon Kim | 석박사통합과정 | Mar.2026 | My research interests lie in efficient AI and AI for science, where I focus on developing computationally efficient AI systems and applying AI to solve scientific problems. | happyriosshs@snu.ac.kr |  |
| Jihwan Jang | 석박사통합과정 | Mar. 2026 | My research focuses on ML systems, with an emphasis on distributed systems for training large language models. | pi2bangool@snu.ac.kr |  |

## 졸업생과 이전 구성원

랩 People 페이지 Alumni 칸의 4명이다. 학위·과정과 진로는 카드 표기 그대로이고, 졸업 연도는 적혀 있지 않다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Hohyun Kim | MS | Hana Bank |
| Mingi Yoo | MS | Sapeon |
| Deokki Hong | MS | Sapeon |
| Seoyong Lee | BS Intern | Jane Street |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지 2021–2026년 연도 구역의 53편(2026년 14, 2025년 10, 2024년 8, 2023년 7, 2022년 8, 2021년 6)이다. 연도는 페이지의 연도 구역이고, 저자·제목·학회와 학술지 이름·연월은 랩 표기 그대로다. 저자 이름 뒤의 ¹은 랩이 표시한 공동 1저자다. 2026년 10월·11월 학회로 적힌 세 편(WiFlash, Spexis, CamoDocs)은 랩 첫 화면 소식이 채택을 알린 논문이라 「채택」으로 표시했다. 랩은 Smart-Infinity(HPCA, 2024) 항목에 "Best Paper Award-Honorable Mention!"을 덧붙이고, Slice-and-Forge(2022) 항목의 학회 이름을 "PACT (Best Paper Award)"로 적는다.[^pubs][^home] 랩 소식은 교수의 서울대 부임을 2023년 9월로, 학과 교수 소개는 서울대 경력을 2022년부터로 적으며, 2021–2023년 구역에는 교수가 연세대학교에 있던 때의 논문이 섞여 있다.[^news][^eceprof]

**2026**

- Hyungyu Jung, Jaehyeok Yu, Hoonseo Choi, Sungkyun Kim, Jinho Lee, Jiwon Seo. "Spexis: Speculative Lookahead Scheduling for LLM Inference". *Empirical Methods in Natural Language Processing (EMNLP), Nov 2026, 채택*.
- Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee. "CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents". *Empirical Methods in Natural Language Processing (EMNLP), Nov 2026, 채택*.
- Hyunjin Kim¹, Juchan Lee¹, Inseong Choi, Jinho Lee, Jae-Joon Kim. "WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array". *IEEE/ACM International Symposium on Microarchitecture (MICRO), Oct 2026, 채택*.
- Shingeon Kim, Hyeyoon Lee, Dain Kwon, Kanghyun Choi, Sunjong Park, Mi-Ryang Kim, Jeong-Eun Lee, Jinho Lee. "STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation". *European Conference on Computer Vision (ECCV), Sep 2026*.
- Dain Kwon, Kanghyun Choi, Hyeyoon Lee, Sunjong Park, Seoyong Lee, Sukjin Kim, Jinho Lee. "TopGQ: Fast GNN Post-Training Quantization Leveraging Topology Information". *Design Automation Conference (DAC), Jul 2026*.
- Dain Kwon, Changmin Shin, Sunjong Park, Kanghyun Choi, Hyeyoon Lee, Jaewon Jang, Minseok Choi, Jinho Lee. "SePArate: Segmenting Patterns from Defects in Wafer Manufacturing Using Weak Supervision". *Design Automation Conference (DAC), Jul 2026*.
- Subin Ki, Kyuseung Han, Hyuk Kim, Taewook Kang, Kwang-Il Oh, ..., Sukho Lee, Jae-Jin Lee, Jaehyoung Lee, Woojoo Lee, Jinho Lee. "CRISP: End-to-End Fingerprint Recognition Leveraging Hardware-Anchored Liveness Detection". *Dependable Systems and Networks (DSN) - Industry Track, Jun 2026*.
- Mi-Ryang Kim, Jeong-Eun Lee, Myungshin Im, Jinho Lee, Ji Hoon Kim, ..., Donghwan Hyun, Won-Hyeong Lee, Hyeyoon Lee, Shingeon Kim, S. Thomas Megeath. "7DT Insight: Variability in Young Stellar Objects". *The Astrophysical Journal (ApJ), May 2026*.
- Jaeyong Song, Seongyeon Park, Hongsun Jang, Jaewon Jung, Hunseong Lim, Junguk Hong, Jinho Lee. "GriNNder: Breaking the Memory Capacity Wall in Full-Graph GNN Training with Storage Offloading". *Annual Conference on Machine Learning and Systems (MLSys), May 2026*.
- Hyunwook Jheonn, Jeong-Eun Lee, Jinho Lee, Seonjae Lee, Hyeyoon Lee, Shingeon Kim, Carlos Contreras Peña, Mi-Ryang Kim. "Refined classification of YSOs and AGB stars by IR magnitudes, colors, and time-domain analysis with machine learning". *The Astrophysical Journal (ApJ), May 2026*.
- Chaemin Lim, Suhyun Lee, Jinwoo Choi, Kwanghyun Park, Jinho Lee, Joonsung Kim, Youngsok Kim. "FaScalSQL: A Fast and Scalable GPU-Accelerated SQL Query Engine for Out-of-Memory Tables". *IEEE International Conference on Data Engineering (ICDE), May 2026*.
- Seongyeon Park, Jaeyong Song, Changmin Shin, Sukjin Kim, Junguk Hong, Jinho Lee. "FlexiWalker: Extensible GPU Framework for Efficient Dynamic Random Walks with Runtime Adaptation". *European Conference on Computer Systems (EuroSys), Apr 2026*.
- Hongsun Jang, Jaeyong Song, Changmin Shin, Si Ung Noh, Jaewon Jung, Jisung Park, Jinho Lee. "A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs". *ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Mar 2026*.
- Junguk Hong, Changmin Shin, Sukjin Kim, Si Ung Noh, Taehee Kwon, SeongYeon Park, Hanjun Kim, Youngsok Kim, Jinho Lee. "LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM". *International Symposium on High-Performance Computer Architecture (HPCA), Feb 2026*.

**2025**

- Kanghyun Choi, Hyeyoon Lee, SunJong Park, Dain Kwon, Jinho Lee. "FALQON: Accelerating LoRA Fine-tuning with Low-Bit Floating-Point Arithmetic". *Neural Information Processing Systems (NeurIPS), Dec 2025*.
- Seoyong Lee, Jinho Lee. "AGIS: Fast Approximate Graph Pattern Mining with Structure-Informed Sampling". *Proceedings of International Conference on Very Large Data Bases (VLDB), Dec 2025*.
- Chaemin Lim, Suhyun Lee, Jinwoo Choi, Joonsung Kim, Jinho Lee, Youngsok Kim. "DMO-DB: Mitigating the Data Movement Bottlenecks of GPU-Accelerated Relational OLAP". *International Conference on Parallel Architectures and Compilation Techniques (PACT), Nov 2025*.
- Changmin Shin, Jaeyong Song, Seongmin Na, Jun Sung, Hongsun Jang, Jinho Lee. "FALA: Locality-Aware PIM-Host Cooperation for Graph Processing with Fine-Grained Column Access". *IEEE/ACM International Symposium on Microarchitecture (MICRO), Oct 2025*.
- Hyunjin Kim, Seunghwan Song, Sukhyun Choi, Jeongin Choe, Sanghyeok Han, Jisung Park, Jinho Lee, Jae-Joon Kim. "CrossBit: Bitwise Computing in NAND Flash Memory with Inter-Bitline Data Communication". *IEEE/ACM International Symposium on Microarchitecture (MICRO), Oct 2025*.
- Sukjin Kim, Seongyeon Park, Si Ung Noh, Junguk Hong, Taehee Kwon, Hunseong Lim, Jinho Lee. "PathWeaver: A High-Throughput Multi-GPU System for Graph-Based Approximate Nearest Neighbor Search". *USENIX Annual Technical Conference (USENIX ATC), Jul 2025*.
- Kanghyun Choi, Deokki Hong, Hyeyoon Lee, Joonsang Yu, Noseong Park, Youngsok Kim, Jinho Lee. "DANCE++: Differentiable Accelerator/Network Co-Exploration with Hard Constraints and Data-Free Training for Real-World Scenarios". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), Jun 2025*.
- Yeejoo Han, Sunwoo Kim, Seongyeon Park, Jinho Lee. "G³SA: A GPU-Accelerated Gold Standard Genomics Library for End-to-End Sequence Alignment". *International Conference on Supercomputing (ICS), Jun 2025*.
- Changmin Shin, Jaeyong Song, Hongsun Jang, Dogeun Kim, Jun Sung, Taehee Kwon, Jae Hyung Ju, Frank Liu, Yeonkyu Choi, Jinho Lee. "Piccolo: Large-Scale Graph Processing with Fine-Grained In-Memory Scatter-Gather". *International Symposium on High-Performance Computer Architecture (HPCA), Mar 2025*.
- Kanghyun Choi, Hyeyoon Lee, Dain Kwon, SunJong Park, Kyuyeun Kim, Noseong Park, Jonghyun Choi, Jinho Lee. "MimiQ: Low-Bit Data-Free Quantization of Vision Transformers with Encouraging Inter-Head Attention Similarity". *AAAI Conference on Artificial Intelligence (AAAI), Feb 2025*.

**2024**

- Jaeyong Song, Hongsun Jang, Hunseong Lim, Jaewon Jung, Youngsok Kim, Jinho Lee. "GraNNDis: Fast Distributed Graph Neural Network Training Framework for Multi-Server Clusters". *The International Conference on Parallel Architectures and Compilation Techniques (PACT), Oct 2024*.
- Si Ung Noh¹, Junguk Hong¹, Chaemin Lim, Seongyeon Park, Jeehyun Kim, Hanjun Kim, Youngsok Kim, Jinho Lee. "PID-Comm: A Fast and Flexible Collective Communication Framework for Commodity Processing-in-DIMMs". *International Symposium on Computer Architecture (ISCA), Jul 2024*.
- Hyeyoon Lee, Kanghyun Choi, Dain Kwon, SunJong Park, Mayoore Selvarasa Jaiswal, Noseong Park, Jonghyun Choi, Jinho Lee. "DataFreeShield: Defending Adversarial Attacks without Training Data". *International Conference on Machine Learning (ICML), May 2024*.
- Jinkyu Yim¹, Jaeyong Song¹, Yerim Choi, Jaebeen Lee, Jaewon Jung, Hongsun Jang, Jinho Lee. "Pipette: Automatic Fine-Grained Large Language Model Training Configurator for Real-World Clusters". *Design, Automation and Test in Europe Conference (DATE), Mar 2024*.
- Changmin Shin¹, Taehee Kwon¹, Jaeyong Song, Jae Hyung Ju, Frank Liu, Yeonkyu Choi, Jinho Lee. "A Case for In-Memory Random Scatter-Gather for Fast Graph Processing". *IEEE Computer Architecture Letters (CAL), Mar 2024*.
- Jaewon Jung, Hongsun Jang, Jaeyong Song, Jinho Lee. "PeerAiD: Improving Adversarial Distillation from a Specialized Peer Tutor". *Computer Vision and Pattern Recognition Conference (CVPR), Mar 2024*.
- Hongsun Jang, Jaeyong Song, Jaewon Jung, Jaeyoung Park, Youngsok Kim, Jinho Lee. "Smart-Infinity: Fast Large Language Model Training using Near-Storage Processing on a Real System". *International Symposium on High-Performance Computer Architecture (HPCA), Mar 2024*.
- Seongyeon Park, Junguk Hong, Jaeyong Song, Hajin Kim, Youngsok Kim, Jinho Lee. "AGAThA: Fast and Efficient GPU Acceleration of Guided Sequence Alignment for Long Read Mapping". *ACM Annual Symposium on Principles and Practice of Parallel Programming (PPoPP), Feb 2024*.

**2023**

- Jinwoo Choi, Yeonan Ha, Jounghoo Lee, Sangsu Lee, Jinho Lee, Hanhwi Jang, Youngsok Kim. "Enabling Fine-Grained Spatial Multitasking on Systolic-Array NPUs Using Dataflow Mirroring". *IEEE Transactions on Computers, Dec 2023*.
- Jaewon Jung, Jaeyong Song, Hongsun Jang, Hyeyoon Lee, Kanghyun Choi, Noseong Park, Jinho Lee. "Fast Adversarial Training with Dynamic Batch-level Attack Control". *Design Automation Conference (DAC), Jul 2023*.
- Chaemin Lim, Suhyun Lee, Jinwoo Choi, Jounghoo Lee, Seongyeon Park, Hanjun Kim, Jinho Lee, Youngsok Kim. "Design and Analysis of a Processing-in-DIMM Join Algorithm: A Case Study with UPMEM DIMMs". *Proceedings of the ACM on Management of Data, Jun 2023*.
- Hongsun Jang, Jaewon Jung, Jaeyong Song, Joonsang Yu, Youngsok Kim, Jinho Lee. "Pipe-BD: Pipelined Parallel Blockwise Distillation". *2023 Design, Automation & Test in Europe Conference & Exhibition (DATE), Apr 2023*.
- Mingi Yoo¹, Jaeyong Song¹, Jounghoo Lee, Namhyung Kim, Youngsok Kim, Jinho Lee. "SGCN: Exploiting Compressed-Sparse Features in Deep Graph Convolutional Network Accelerators". *2023 IEEE International Symposium on High-Performance Computer Architecture (HPCA), Feb 2023*.
- Jaeyong Song¹, Jinkyu Yim¹, Jaewon Jung, Hongsun Jang, Hyung-Jin Kim, Youngsok Kim, Jinho Lee. "Optimus-CC: Efficient Large NLP Model Training with 3D Parallelism Aware Communication Compression". *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2, Jan 2023*.
- Deokki Hong, Kanghyun Choi, Hye Yoon Lee, Joonsang Yu, Noseong Park, Youngsok Kim, Jinho Lee. "Enabling Hard Constraints in Differentiable Neural Network and Accelerator Co-Exploration". *Design Automation Conference (DAC), Jan 2023*.

**2022**

- Baozhou Zhu, Peter Hofstee, Jinho Lee, Zaid Al-Ars. "Improving Gradient Paths for Binary Convolutional Neural Networks". *BMVC, Nov 2022*.
- Jinwoo Choi, Jaeyeon Kim, Chaemin Lim, Suhyun Lee, Jinho Lee, Dokyung Song, Youngsok Kim. "GuardiaNN: Fast and Secure On-Device Inference in TrustZone Using Embedded SRAM and Cryptographic Hardware". *Proceedings of the 23rd ACM/IFIP International Middleware Conference, Oct 2022*.
- Shinnung Jeong, Yongwoo Lee, Jaeho Lee, Heelim Choi, Seungbin Song, Jinho Lee, Youngsok Kim, Hanjun Kim. "Decoupling Schedule, Topology Layout, and Algorithm to Easily Enlarge the Tuning Space of GPU Graph Processing". *Proceedings of the International Conference on Parallel Architectures and Compilation Techniques, Oct 2022*.
- Mingi Yoo¹, Jaeyong Song¹, Hye Yoon Lee, Jounghoo Lee, Namhyung Kim, Youngsok Kim, Jinho Lee. "Slice-and-Forge: Making Better Use of Caches for Graph Convolutional Network Accelerators". *PACT (Best Paper Award), Oct 2022*.
- Namhyung Kim, Hanmin Park, Dongwoo Lee, Sungbum Kang, Jinho Lee, Kiyoung Choi. "ComPreEND: Computation Pruning through Predictive Early Negative Detection for ReLU in a Deep Neural Network Accelerator". *IEEE Transactions on Computers, Jul 2022*.
- Jounghoo Lee, Yeonan Ha, Suhyun Lee, Jinyoung Woo, Jinho Lee, Hanhwi Jang, Youngsok Kim. "GCoM: a detailed GPU core model for accurate analytical modeling of modern GPUs". *Proceedings of the 49th Annual International Symposium on Computer Architecture, Jun 2022*.
- Seongyeon Park, Hajin Kim, Tanveer Ahmad, Nauman Ahmed, Zaid Al-Ars, H. Peter Hofstee, Youngsok Kim, Jinho Lee. "SALoBa: Maximizing Data Locality and Workload Balance for Fast Sequence Alignment on GPUs". *2022 IEEE International Parallel and Distributed Processing Symposium (IPDPS), May 2022*.
- Kanghyun Choi, Hye Yoon Lee, Deokki Hong, Joonsang Yu, Noseong Park, Youngsok Kim, Jinho Lee. "It's All In the Teacher: Zero-Shot Quantization Brought Closer to the Teacher". *Computer Vision and Pattern Recognition Conference (CVPR), Apr 2022*.

**2021**

- Kanghyun Choi¹, Deokki Hong¹, Hojae Yoon¹, Joonsang Yu, Youngsok Kim, Jinho Lee. "DANCE: Differentiable Accelerator/Network Co-Exploration". *Design Automation Conference (DAC), Dec 2021*.
- Jounghoo Lee, Jinwoo Choi, Jaeyeon Kim, Jinho Lee, Youngsok Kim. "Dataflow Mirroring: Architectural Support for Highly Efficient Fine-Grained Spatial Multitasking on Systolic-Array NPUs". *2021 58th ACM/IEEE Design Automation Conference (DAC), Dec 2021*.
- Kanghyun Choi, Deokki Hong, Noseong Park, Youngsok Kim, Jinho Lee. "Qimera: Data-free Quantization with Synthetic Boundary Supporting Samples". *Neural Information Processing Systems (NeurIPS), Nov 2021*.
- Baozhou Zhu, Peter Hofstee, Johan Peltenburg, Jinho Lee, Zaid Al-Ars. "AutoReCon: Neural Architecture Search-based Reconstruction for Data-free Compression". *IJCAI, Aug 2021*.
- Mingi Yoo¹, Jaeyong Song¹, Jounghoo Lee, Namhyung Kim, Youngsok Kim, Jinho Lee. "Making a Better Use of Caches for GCN Accelerators with Feature Slicing and Automatic Tile Morphing". *IEEE Computer Architecture Letters, Jul 2021*.
- Heesu Kim, Hanmin Park, Taehyun Kim, Kwanheum Cho, Eojin Lee, Soojung Ryu, Hyuk-Jae Lee, Kiyoung Choi, Jinho Lee. "GradPIM: A Practical Processing-in-DRAM Architecture for Gradient Descent". *2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA), Feb 2021*.

## 수상

랩 News 페이지의 2021년 10월–2026년 9월 소식 가운데 수상을 알린 5건이다. 날짜와 문구는 페이지 표기 그대로다. 2022년의 2건은 랩 소식이 적은 서울대 부임(2023년 9월) 전의 것이다.[^news]

- Sep. 2026 · We won the first place award from Agentic FPGA Backend Optimization Competition@FPL 2026. Congratulations to Sookwan Han, Sihun Lim, Jun Sung, and Haeun Ji!
- Jan. 2026 · Kanghyun Choi, Hyeyoon Lee, Sunjong Park, and Dain Kwon won a gold prize, and Hongsun Jang, Jaeyong Song, Changmin Shin, and Si Ung Noh won a silver prize at the 32nd Samsung Humantech Paper Awards. Warm congratulations to the awardees!
- Mar. 2024 · Received the best paper award honorable mention from HPCA 2024. Congratulations to the authors of "Smart-Infinity"!
- Oct. 2022 · Best paper award received from PACT 2022! Congratulations and thanks to the authors of "Slice-and-Forge"
- Feb. 2022 · Kanghyun Choi, Deokki Hong, and Hye Yoon Lee won a silver prize in 28th Samsung Humantech Paper Awards.

## 소식

랩 News 페이지의 2021년 10월–2026년 9월 소식 53건 가운데 위 수상 5건을 뺀 48건이다. 날짜와 문구는 페이지 표기 그대로다. 2023년 7월까지의 소식은 랩 소식이 적은 서울대 부임(2023년 9월) 전의 것이다.[^news]

- Aug. 2026 · Two papers have been accepted to EMNLP 2026. Congratulations! CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents Spexis: Speculative Lookahead Scheduling for LLM Inference CamoDocs is a collaboration with CMU (Prof. Beidi Chen), and Spexis is a collaboration with SNU MLSys Lab. (Prof. Jiwon Seo).
- Jun. 2026 · Our paper STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation has been accepted to ECCV 2026. Congratulations to authors!
- Jun. 2026 · Our paper WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array has been accepted to MICRO 2026, a collaboration with SNU VLSI Lab. (Prof. Jae-Joon Kim).
- Feb. 2026 · Two papers have been accepted to DAC 2026. Warm congratulations to the authors! TopGQ: Fast GNN Post-Training Quantization Leveraging Topology Information SePArate: Segmenting Patterns from Defects in Wafer Manufacturing Using Weak Supervision
- Feb. 2026 · Two papers have been accepted from collaboration: CRISP: End-to-End Fingerprint Recognition Leveraging Hardware-Anchored Liveness Detection (DSN-Industry) 7DT Insight: Variability in Young Stellar Objects (Astrophysical Journal)
- Feb. 2026 · At HPCA 2026, our paper "LoCaLUT" was presented in the Best Paper Candidates session.
- Jan. 2026 · Our paper GriNNder: Breaking the Memory Capacity Wall in Full-Graph GNN Training with Storage Offloading has been accepted to MLSys 2026. Congratulations to authors and see you at Bellevue!
- Jan. 2026 · Our paper A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs has been accepted to ASPLOS 2026. Congratulations to authors and see you at Pittsburgh!
- Nov. 2025 · Our paper Refined classification of YSOs and AGB stars by IR magnitudes, colors, and time-domain analysis with machine learning has been accepted to The Astrophysical Journal. Looks like our pursuit of system scalability reached stellar-system scale this time.
- Nov. 2025 · Our paper FaScalSQL: A Fast and Scalable GPU-Accelerated SQL Query Engine for Out-of-Memory Tables has been accepted to ICDE 2026. Congratulations to authors! This is another work done in collaboration with HPCP Lab. (Prof. Youngsok Kim) at Yonsei Univ. and CISA Lab. (Prof. Joonsung Kim) at SKKU
- Nov. 2025 · Our paper LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM has been accepted to HPCA 2026. Congratulations to authors! This work was done in collaboration with HPCP Lab. (Prof. Youngsok Kim) and Core Lab (Prof. Hanjun Kim) at Yonsei Univ.
- Sep. 2025 · Our paper FALQON: Accelerating LoRA Fine-tuning with Low-Bit Floating-Point Arithmetic has been accepted to NeurIPS 2025. Congratulations to authors!
- Sep. 2025 · Our paper FlexiWalker: Extensible GPU Framework for Efficient Dynamic Random Walks with Runtime Adaptation has been accepted to EuroSys. Congratulations!
- Sep. 2025 · Our paper AGIS: Fast Approximate Graph Pattern Mining with Structure-Informed Sampling has been accepted to VLDB. Congratulations Seoyong, it is an exceptional achievement as an undergraduate student :)
- Aug. 2025 · Our paper DMO-DB: Mitigating the Data Movement Bottlenecks of GPU-Accelerated Relational OLAP has been accepted to PACT. This work was done in collaboration with HPCP Lab. (Prof. Youngsok Kim) at Yonsei Univ. and CISA Lab. (Prof. Joonsung Kim) at SKKU
- Jul. 2025 · two papers have been accepted to MICRO 2025. Congratulations! FALA: Locality-Aware PIM-Host Cooperation for Graph Processing with Fine-Grained Column Access CrossBit: Bitwise Computing in NAND Flash Memory with Inter-Bitline Data Communication FALA was done within our group, and CrossBit was done in collaboration with SNU VLSI Lab. (Prof. Jae-Joon Kim), and CAOS Lab. (Prof. Jisung Park) at Postech
- Jul. 2025 · A warm welcome to Taehee Kwon and Woobeen Jo!
- Jun. 2025 · Our paper DANCE++: Differentiable Accelerator/Network Co-Exploration with Hard Constraints and Data-Free Training for Real-World Scenarios has been accepted to IEEE TCAD. Congratulations!
- May. 2025 · Our paper PathWeaver: A High-Throughput Multi-GPU System for Graph-Based Approximate Nearest Neighbor Search has been accepted to ATC 2025. Congratulations to authors!
- Apr. 2025 · Our paper G^3SA: A GPU-Accelerated Gold Standard Genomics Library for End-to-End Sequence Alignment has been accepted to ICS 2025. Congratulations to authors!
- Jan. 2025 · Welcome to our lab, Dain Kwon and Jun Sung!
- Dec. 2024 · Our paper MimiQ: Low-Bit Data-Free Quantization of Vision Transformers with Encouraging Inter-Head Attention Similarity has been accepted to AAAI 2025. Congratulations to authors!
- Nov. 2024 · Our paper Piccolo: Large-Scale Graph Processing with Fine-Grained In-Memory Scatter-Gather has been accepted to HPCA 2025. Congratulations!
- Aug. 2024 · Sukjin Kim joined the lab. Welcome aboard!
- Jun. 2024 · Our paper GraNNDis: Fast Distributed Graph Neural Network Training Framework for Multi-Server Clusters has been accepted to PACT 2024. Congratulations!
- May. 2024 · Our paper titled DataFreeShield: Defending Adversarial Attacks without Training Data has been accepted to ICML 2024. Cheers to your endeavor!
- Mar. 2024 · Our paper titled PID-Comm: A Fast and Flexible Collective Communication Framework for Commodity Processing-in-DIMMs has been accepted to ISCA 2024. Congratulations to authors and see you at Buenos Aires!
- Mar. 2024 · A warm welcome to Changmin Shin, Hunseong Lim, Si Ung Noh, and Sunjong Park!
- Feb. 2024 · Our paper titled PeerAiD: Improving Adversarial Distillation from a Specialized Peer Tutor has been accepted to CVPR 2024. Congratulations to authors!
- Feb. 2024 · Our paper A Case for In-Memory Random Scatter-Gather for Fast Graph Processing has been accepted to IEEE CAL. Congratulations!
- Nov. 2023 · We got a paper accpeted in PPoPP 2024: AGAThA: Fast and Efficient GPU Acceleration of Guided Sequence Alignment for Long Read Mapping. Conguratulations to authors and see you at Edinburgh Ü
- Nov. 2023 · Our paper Pipette: Automatic Fine-grained Large Language Model Training Configurator for Real-World Clusters has been accepted at DATE 2024. Congratulations!
- Oct. 2023 · We got a paper accepted in HPCA 2024: Smart-Infinity: Fast Large Language Model Training using Near-Storage Processing on a Real System. Congratulations to authors!
- Sep. 2023 · Jinho Lee joined ECE, Seoul Nationl University as an assistant professor.
- Jul. 2023 · Our paper titled Enabling Fine-Grained Spatial Multitasking on Systolic-Array NPUs Using Dataflow Mirroring has been accepted to IEEE TC. Congratulations to authors!
- Feb. 2023 · We got a paper accepted in DAC 2023: Fast Adversarial Training with Dynamic Batch-level Attack Control congratulations to authors!
- Jan. 2023 · We got a new year's first paper accepted to SIGMOD 2023: Design and Analysis of a Processing-in-DIMM Join Algorithm: A Case Study with UPMEM DIMMs congratulations to authors!
- Jan. 2023 · We welcome Junguk Hong as our new member Ü
- Nov. 2022 · We got a paper accepted in DATE 2023: Pipe-BD: Pipelined Parallel Blockwise Distillation congratulations to authors, see you at Antwerp!
- Oct. 2022 · Our paper titled SGCN: Exploiting Compressed-Sparse Features in Deep Graph Convolutional Network Accelerators has been accepted to HPCA 2023. Nice job!
- Sep. 2022 · Optimus-CC: Efficient Large NLP Model Training with 3D Parallelism Aware Communication Compression has been accepted to ASPLOS 2023. Congratulations authors!
- Aug. 2022 · two papers have been accepted to PACT 2022. Nice work! Slice-and-Forge: Making Better Use of Caches for Graph Convolutional Network Accelerators Decoupling Schedule, Topology Layout, and Algorithm to Easily Enlarge the Tuning Space of GPU Graph Processing
- Aug. 2022 · Hongsun Jang joins the Lab. Welcome :)
- Mar. 2022 · Our CVPR 2022 paper 'AIT' has been selected for an oral presentation. Double congratulations!
- Feb. 2022 · We have two newly accepted papers on Valentines day. Congratulations authors Ü Enabling Hard Constraints in Differentiable Neural Network and Accelerator Co-Exploration @ DAC 2022 GuardiaNN: Fast and Secure Inference in TrustZone Using Embedded SRAM and Cryptographic Hardware @ Middleware 2022
- Jan. 2022 · Our paper SALoBa: Maximizing Data Locality and Workload Balance for Fast Sequence Alignment on GPUs has been accepted at IPDPS 2022. Hope we get to travel to France :) It's going virtual.
- Jan. 2022 · SeongYeon Park joins the Lab. Welcome!
- Oct. 2021 · Jaewon Jung joins the Lab. Welcome!

## 연락과 위치

- 교수 연구실: 서울대학교 공과대학 301동 1009호[^prof][^snuti]
- 학과 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^eceprof]
- 교수 전화: 02-880-1816[^eceprof]
- 교수 이메일: leejinho@snu.ac.kr[^gsai][^snuti]
[^home]: 연구실 누리집 첫 화면 <https://aisys.snu.ac.kr/> (연구실 소개, Hiring, News, Research Topics, 2026-10-23 열람)
[^research]: Research 페이지 <https://aisys.snu.ac.kr/research/> (Research Topics의 AI Accelerators, Distributed Deep Learning, Neural Network Acceleration and Compression, System Optimization and Acceleration, 2026-10-23 열람)
[^people]: People 페이지 <https://aisys.snu.ac.kr/team/> (Professor, Graduate Students, Alumni 칸, 2026-10-23 열람)
[^prof]: 교수 개인 페이지 <https://aisys.snu.ac.kr/members/JinhoLee.html> (2026-10-23 열람)
[^member]: People 페이지의 카드에서 이어지는 구성원 개인 페이지 18쪽(<https://aisys.snu.ac.kr/members/KanghyunChoi.html> 등, 주소 목록은 근거 페이지) (소개 글, Education, Email 단추, 2026-10-23 열람)
[^pubs]: Publications 페이지 <https://aisys.snu.ac.kr/publications/> (2009–2026년 연도 구역, 2026-10-23 열람)
[^news]: News 페이지 <https://aisys.snu.ac.kr/news/> (2019–2026년 소식, 2026-10-23 열람)
[^lecture]: Lecture 페이지 <https://aisys.snu.ac.kr/lecture/> (2026-10-23 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-23 열람)
[^ecelabd]: 서울대학교 전기·정보공학부 연구실 소개(가속화지능형시스템연구실) <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=98> (2026-10-23 열람)
[^eceprof]: 서울대학교 전기·정보공학부 교수 소개(이진호) <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p877> (직위, 학력, 주요경력, Research Interest, 연락처, 2026-10-23 열람)
[^gsai]: 서울대학교 협동과정 인공지능 전공 교수진 목록 <https://gsai.snu.ac.kr/%ea%b5%90%ec%88%98%ec%a7%84-%eb%aa%a9%eb%a1%9d/> (2026-10-23 열람)
[^snuti]: 서울대학교 첨단융합학부 교수진 <https://snuti.snu.ac.kr/commt/professor/> (차세대지능형반도체전공 칸, 2026-10-23 열람)
[^p1]: J. Hong 외, J. Lee, 2026 IEEE International Symposium on High Performance Computer Architecture (HPCA), 1-16 (2026). <https://doi.org/10.1109/hpca68181.2026.11408523> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: K. Choi 외, J. Lee, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 45, 915-928 (2026). <https://doi.org/10.1109/tcad.2025.3582196> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Yim 외, J. Lee, 2024 Design, Automation & Test in Europe Conference & Exhibition (DATE), 1-6 (2024). <https://doi.org/10.23919/date58400.2024.10546826> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Song 외, J. Lee, Proceedings of the 2024 International Conference on Parallel Architectures and Compilation Techniques, 91-107 (온라인 2024-10-13). <https://doi.org/10.1145/3656019.3676892> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: K. Choi 외, J. Lee, Advances in Neural Information Processing Systems 38, 136663-136688 (2025). <https://doi.org/10.52202/085713-4110> 초록 기준(arXiv 판).
[^p6]: K. Choi 외, J. Lee, Proceedings of the AAAI Conference on Artificial Intelligence 39, 16037-16045 (온라인 2025-04-11). <https://doi.org/10.1609/aaai.v39i15.33761> 초록 기준.
[^p7]: S. Kim 외, J. Lee, USENIX Annual Technical Conference (USENIX ATC 2025) (2025). <https://arxiv.org/html/2507.17094v1> 초록 기준(arXiv 판).
[^p8]: S. U. Noh 외, J. Lee, 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA), 245-260 (2024). <https://doi.org/10.1109/isca59077.2024.00027> 초록 기준(Semantic Scholar 등록 초록).

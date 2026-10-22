# CAST Lab (CAST Hardware Innovation Lab)

**KAIST 전기및전자공학부 · 김주영 교수**

- 분야: VLSI 설계, 컴퓨터 구조, FPGA, 하드웨어-소프트웨어 코디자인, AI 가속기, 메모리 내 연산(PIM), 데이터센터용 다중 FPGA 시스템
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: AI 반도체·가속기[^home][^research][^p2], 메모리 내 연산[^about][^p3][^p4], 컴퓨터 구조·운영체제[^home][^eelist][^p7], 집적회로 설계[^home][^eelist][^p5], 대형 언어 모델[^p1][^p2], AI 시스템·인프라[^research][^p1]
- 홈페이지: <https://castlab.kaist.ac.kr/>
- 근거와 출처: [CAST Lab 근거 페이지](castlab-sources.md)

> 인공지능 계산을 빠르고 적은 전력으로 처리하는 전용 하드웨어를 칩 회로부터 컴퓨터 구조, FPGA 서버 시스템까지 함께 설계해, 앞으로의 인공지능 응용을 위한 고성능·확장형 컴퓨팅 플랫폼을 만드는 연구실이다.[^home][^about]

## 무엇을 연구하나

연구실 이름의 CAST는 회로(Circuits), 구조(Architecture), 시스템(Systems), 기술(Technology)의 머리글자다.[^home] 연구실은 무어의 법칙(반도체 칩에 넣는 트랜지스터 수가 꾸준히 늘어 왔다는 경험칙) 이후의 시대에 특정 용도에 맞춘 전용 하드웨어로 현대 컴퓨터 시스템을 발전시키는 것을 목표로 한다고 소개한다. 연구 분야로 컴퓨터 구조, VLSI(초대규모 집적회로, 아주 많은 트랜지스터를 한 칩에 넣은 회로) 설계, FPGA(만든 뒤에도 회로 구성을 다시 프로그래밍할 수 있는 칩), 하드웨어·소프트웨어 공동 설계, 메모리 내 연산(PIM, 데이터를 프로세서로 옮기지 않고 메모리 안이나 가까이에서 계산하는 방식)을 들고, 여러 수준의 하드웨어 설계를 함께 다루는 전체적 접근으로 시스템 성능을 높인다고 적는다. 지금의 목표는 미래 인공지능 응용을 위한 고성능·확장형 컴퓨팅 플랫폼을 만드는 것이다.[^home][^about]

연구실 소개는 컴퓨팅 성능을 끌어올리던 전통적인 방식이 한계에 이르렀다고 보고, 계산 속도보다 데이터 이동이라는 근본 병목을 겨냥한 메모리 중심 컴퓨팅을 개척한다고 밝힌다. 교수가 Microsoft의 Project Catapult 초기 멤버로 데이터센터에 FPGA를 대규모로 배치해 기계학습·데이터 저장·네트워킹을 가속한 경험이, 학술 연구와 상용화 가능성을 잇는 연구 방향의 바탕이 된다고 적는다.[^about]

연구 영역 페이지는 ASIC(특정 용도 전용 칩), Architecture, FPGA 세 영역을 둔다.[^research] AI 가속기 연구에서는 다음 세대 인공지능·기계학습 작업을 위해 여러 종류의 연산 장치를 묶은 확장형 구조의 설계 공간을 탐색하고, 소프트웨어·하드웨어를 함께 설계한 시스템 해법을 만든다. 이 해법을 시험하는 시뮬레이션 틀을 만든 뒤 FPGA와 ASIC 같은 실제 장치로 구현해 개발·디버깅·배치까지 한다.[^research] 다중 FPGA 연구에서는 데이터센터 서비스를 가속하면서 맞춤형 시스템 설계도 할 수 있는 다중 FPGA 서버 인프라를 만든다. 연구 영역 페이지는 FPGA 가속기가 ASIC 가속기보다 새 연산을 지원하려고 다시 설계하는 비용이 적고, GPU 가속기보다 장치·전력 비용이 낮아 총소유비용이 낮다고 설명한다.[^research]

연구실은 설계한 구조를 실제 칩으로 만든다. Chip Gallery에는 2020–2026년에 만든 칩 14종이 올라 있다. 대형 언어 모델 가속기 Adelia(4nm 공정), 글로 사람 동작을 만드는 텍스트-동작 프로세서 HuMoniX, 암호화된 데이터를 그대로 계산하는 동형 암호 가속기 OmniCrypt, 시각-언어 모델 가속기 Tri-Oracle, 메모리 안에서 계산하는 Z-PIM·T-PIM·SP-PIM·DPIM 같은 칩이다.[^chips]

대표 논문으로 보면 연구는 다섯 갈래다. 첫째, 대형 언어 모델(LLM, 많은 글을 학습해 글을 이해하고 만들어 내는 큰 인공지능 모델)이 글을 만들어 내는 추론을 빠르게 하는 다중 FPGA 장치와 전용 프로세서다(대표 논문 1, 2).[^p1][^p2] 둘째, 메모리 안이나 옆에서 계산해 데이터 이동을 줄이는 PIM 칩과 구조다(대표 논문 3, 4).[^p3][^p4] 셋째, 글로 사람 동작을 만드는 생성 인공지능을 기기에서 실시간으로 돌리는 칩이다(대표 논문 5).[^p5] 넷째, 암호화된 데이터를 그대로 계산하는 동형 암호의 가속기다(대표 논문 6).[^p6] 다섯째, 이미지 인식용 비전 트랜스포머와 단백질 구조 예측 모델처럼 특정 인공지능 모델에 맞춘 가속기다(대표 논문 7, 8).[^p7][^p8]

## 주요 연구 주제

### 1. 대형 언어 모델 추론용 FPGA 장치와 프로세서

글을 한 단어씩 만들어 내는 생성 단계에서 GPU 성능이 떨어지는 문제를 겨냥해, FPGA 네 개로 GPT-2 모델 추론을 처음부터 끝까지 실행하는 장치 DFX를 만들었다. 교수가 창업한 HyperAccel이 내놓은 LLM 추론 프로세서 LPU(메모리 대역폭과 계산 논리의 균형을 맞춘 구조, 삼성 4nm 공정으로 합성)를 다룬 논문도 썼다.[^p1][^p2] 대표 논문 1, 2.

### 2. 메모리 안에서 계산하는 PIM

기기 안에서 기계학습 모델을 다시 학습시키는 PIM 칩 SP-PIM을 28nm 공정으로 만들었고, 고대역폭 메모리(HBM)의 작은 저장 단위 옆에 연산 장치를 넣어 글 생성을 가속하는 PIM 구조 SAL-PIM을 제안했다.[^p3][^p4] 대표 논문 3, 4.

### 3. 생성 인공지능을 기기에서 돌리는 칩

글이나 음악 입력으로 3차원 사람 동작을 만드는 확산 모델과 몸 형상 계산을 실시간으로 처리하는 14nm 칩 HuMoniX를 만들었다.[^p5] 대표 논문 5.

### 4. 동형 암호 가속

암호문의 잡음을 되돌리는 부트스트래핑을 여러 암호문을 묶어 처리하도록 바꾼 스트리밍 가속기 Strix를 설계했다.[^p6] 대표 논문 6.

### 5. 특정 인공지능 모델에 맞춘 가속기

비슷한 이미지 조각을 이미지에 맞춰 합쳐 비전 트랜스포머를 가속하는 AdapTiV와, 단백질 구조 예측 모델의 서열 길이 한계를 넘는 LightNobel을 만들었다.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 Publications 목록의 2022–2026년 논문 가운데 김주영 교수가 마지막 저자인 논문을, 랩 첫 화면 「Selected Paper」에 오른 논문을 중심으로 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2022 | [DFX: A Low-latency Multi-FPGA Appliance for Accelerating Transformer-based Text Generation](https://doi.org/10.1109/micro56248.2022.00051) · IEEE/ACM International Symposium on Microarchitecture (MICRO) | 트랜스포머(문장 속 단어들 사이의 관계를 계산하는 딥러닝 모델 구조)는 데이터센터의 자연어 처리 서비스에 널리 쓰이고, 그중 GPT는 글 생성에서 뛰어난 성능을 보였다. 글 생성은 큰 입력 문맥을 처리하는 요약 단계 뒤에 한 번에 한 단어씩 만드는 생성 단계가 이어진다. GPU 같은 기존 플랫폼은 요약 단계의 대규모 병렬 처리에 맞춰져 있어 순차적인 생성 단계에서는 성능이 크게 떨어진다. 그래서 GPT-2 모델 추론을 두 단계 모두 낮은 지연과 높은 처리량으로 처음부터 끝까지 실행하는 다중 FPGA 가속 장치 DFX를 내놓았다. 모델 병렬화와 모델·하드웨어를 함께 고려한 데이터 흐름으로 여러 장치가 동시에 일하게 했고, 계산 코어는 전용 명령어로 GPT-2 연산을 처리한다. Xilinx Alveo U280 FPGA 네 개에 구현하고 고대역폭 메모리(HBM)의 모든 채널을 썼다. NVIDIA V100 GPU 네 개보다 5.58배 빠르고 에너지 효율이 3.99배 높았으며, GPU 장치보다 비용 효율이 8.21배 높아 클라우드 데이터센터의 글 생성 작업에 유망한 해법이라고 보았다.[^p1] | 1저자 S. Hong, 마지막 저자 김주영 |
| 2 | 2024 | [LPU: A Latency-Optimized Highly Scalable Processor for Large Language Model Inference](https://doi.org/10.1109/mm.2024.3420728) · IEEE Micro | 수십억 개의 사전 학습 변수로 이루어진 대형 언어 모델(LLM)이 ChatGPT 등장 뒤 세계로 퍼졌다. HyperAccel은 LLM 추론을 가속하는 지연 최적화·고확장성 프로세서 구조 LPU(latency processing unit)를 내놓았다. LPU는 메모리 대역폭과 계산 논리의 균형을 맞추고 간결한 데이터 흐름으로 성능과 효율을 끌어올리며, 여러 LPU 사이의 데이터 동기화 지연을 숨기는 확장형 동기화 연결을 갖췄다. 소프트웨어 틀 HyperDex로 LLM 응용을 돌린다. 1.3B·66B 모델(이름의 B는 변수 개수가 10억 단위라는 뜻)에서 토큰당 1.25 ms·20.9 ms로 GPU보다 각각 2.09배·1.37배 빨랐다. 삼성 4nm 공정으로 합성한 LPU는 면적 0.824 mm², 소비 전력 284.31 mW이고, LPU 기반 서버는 Nvidia H100·L4 서버보다 에너지 효율이 1.33배·1.32배 높았다.[^p2] | 1저자 S. Moon, 마지막 저자 김주영 (17명) |
| 3 | 2024 | [SP-PIM: A Super-Pipelined Processing-In-Memory Accelerator with Local Error Prediction for Area/Energy-Efficient On-Device Learning](https://doi.org/10.1109/jssc.2024.3369326) · IEEE Journal of Solid-State Circuits (JSSC) | 기계학습을 쓰는 엣지 기기(데이터가 생기는 현장의 기기)는 환경이 바뀔 때 모델 정확도를 되찾으려고 기기 안에서 학습(ODL)을 한다. 그러나 배터리가 한정된 기기에서 학습하면 큰 중간 데이터가 생기고 프로세서와 메모리 사이 데이터 이동이 잦아 전력이 많이 든다. 메모리에 계산 논리를 넣은 PIM 가속기도 학습 과정에 파이프라인(작업을 단계로 나눠 겹쳐 처리하는 방식)이 없어 지연이 길고, 부동소수점 연산의 전력·면적 부담과 학습 데이터의 희소성(값이 0인 데이터가 많은 성질)을 다 다루지 못하는 한계가 있었다. SP-PIM은 국소 오차 예측(EP)에 바탕을 둔 여러 단계의 파이프라인으로 학습 속도를 7.31배 높였다. 2의 거듭제곱 무작위 가중치로 오차를 예측하는 가벼운 회로(LEPU)로 전력을 많이 쓰는 외부 메모리 접근을 59.09% 줄였고, 학습 중 활성값과 오차 데이터의 희소성을 모두 활용했다. 28nm CMOS 공정으로 만든 칩은 초당 8.81 에포크(학습 데이터 전체를 한 번 도는 단위)로 학습하고, 면적 5.76 mm²에 20–450 MHz에서 6.91–433.25 mW를 쓴다. CIFAR10·CIFAR100 데이터셋으로 기기 안 학습을 처음부터 끝까지 해 보였고, 면적 효율 560.6 GFLOPS/mm²와 전력 효율 22.4 TFLOPS/W를 얻었다.[^p3] | 1저자 J. Heo, 마지막 저자 김주영 |
| 4 | 2025 | [SAL-PIM: A Subarray-level Processing-in-Memory Architecture with LUT-based Linear Interpolation for Transformer-based Text Generation](https://doi.org/10.1109/tc.2025.3576935) · IEEE Transactions on Computers | GPT 같은 생성 모델의 글 생성은 입력을 병렬로 처리하는 요약 단계와 출력 토큰을 하나씩 반복해 만드는 생성 단계로 나뉜다. 생성 단계는 병렬화가 어렵고, 반복마다 모델 전체를 읽지만 다시 쓸 데이터가 거의 없어 외부 메모리 대역폭이 시스템의 병목이 된다. SAL-PIM은 트랜스포머 기반 글 생성을 처음부터 끝까지 가속하는 첫 HBM 기반 PIM 구조라고 밝힌다. 메모리의 서브어레이(메모리 안의 작은 저장 단위 묶음) 옆에 연산 장치(S-ALU)를 여러 개 넣어 더 높은 내부 대역폭을 쓴다. 같은 뱅크에 명령이 느린 클록으로 들어오는 점을 이용해 곱셈·누산 장치를 함께 써 면적을 줄였고, 뱅크의 서브어레이 몇 개를 조회표(LUT)로 써서 비선형 함수를 선형 보간으로 계산한다. HBM의 버퍼 다이에는 여러 뱅크의 데이터를 합하는 채널 단위 연산 장치(C-ALU)를 더했다. 논리 장치를 28nm CMOS 공정으로 구현한 뒤 DRAM 공정으로 환산해 실현 가능성을 확인했고, GPT-2 medium 모델(변수 3억 4,500만 개)에서 면적을 4.81% 늘려 Nvidia Titan RTX GPU보다 최대 4.72배, 평균 1.83배 빨랐다.[^p4] | 1저자 W. Han, 마지막 저자 김주영 |
| 5 | 2026 | [A 57.3 fps 12.8 TFLOPS/W Text-to-Motion Processor with Inter-Iteration Output Sparsity and Inter-Frame Joint Similarity](https://doi.org/10.1109/jssc.2025.3631087) · IEEE Journal of Solid-State Circuits (JSSC) | 3차원 사람 동작 생성은 영화 제작이나 AR·VR 기기 같은 미디어 응용에 꼭 필요해졌다. 예전에는 관절 동작을 만드는 데 몇 시간에서 며칠이 걸렸고, 확산 모델(잡음을 조금씩 걷어 내며 데이터를 만들어 내는 생성 인공지능)이 이를 몇 초 안으로 줄였다. 그러나 엣지 기기에서 실시간으로 돌리기에는 반복되는 잡음 제거 계산과 SMPL 모델(관절 움직임으로 사람 몸의 3차원 형상을 만드는 모델) 기반 메시 구성 시간이 걸림돌이다. HuMoniX는 소프트웨어와 하드웨어를 함께 설계한 텍스트-동작 생성 프로세서다. 반복 사이에 중복되는 연산을 건너뛰고, 움직임이 큰 프레임에서만 SMPL을 계산해 지연을 줄였다. 하드웨어는 관절 생성과 메시 구성을 따로 맡는 두 엔진 묶음으로 이루어진다. 14nm 공정으로 만든 칩은 면적 12 mm²에 50–600 MHz에서 39.18–1382.39 mW를 쓰며, 글이나 음악 입력으로 사람 동작을 만들면서 정확도 손실을 최소로 했다. 속도는 초당 57.3 프레임으로 비교한 GPU 시스템보다 최대 650.5배 빨랐다.[^p5] | 1저자 J. Heo, 마지막 저자 김주영 |
| 6 | 2023 | [Strix: An End-to-End Streaming Architecture with Two-Level Ciphertext Batching for Fully Homomorphic Encryption with Programmable Bootstrapping](https://doi.org/10.1145/3613424.3614264) · IEEE/ACM International Symposium on Microarchitecture (MICRO) | 동형 암호(HE)는 암호화된 데이터를 그대로 계산할 수 있게 하는 암호 기술이다. 보안을 위해 데이터를 잡음 아래 숨기는데, 잡음이 너무 커지지 않도록 암호문의 잡음 수준을 되돌리는 부트스트래핑은 큰 키가 필요하고 계산 비용이 크다. TFHE 방식은 더 빠르고 프로그래밍할 수 있는 부트스트래핑(PBS)을 제공하지만 여러 암호문을 한데 묶어 처리하지 못해 처리량이 낮다. 연구진은 GPU에서 TFHE를 가속할 때의 병목을 분석하고, PBS에서 한 번에 처리하는 묶음 크기를 키우는 2단계 묶음 방식을 제안했다. 이를 구현하려고 스트리밍·완전 파이프라인 구조의 가속기 Strix를 만들었고, 분해 연산용 새 미세구조와 접기 방식을 쓴 FFT 미세구조로 처리량을 2배로 높이고 면적을 1.7배 줄였다. Strix는 PBS를 포함한 TFHE 실행에서 최신 CPU·GPU 구현보다 처리량이 각각 1,067배·37배 넘게 높았고, 기존 TFHE 가속기 MATCHA보다 7.4배 높았다.[^p6] | 1저자 A. Putra, 마지막 저자 김주영 |
| 7 | 2024 | [AdapTiV: Sign-Similarity based Image-Adaptive Token Merging for Vision Transformer Acceleration](https://doi.org/10.1109/micro61859.2024.00015) · ACM/IEEE International Symposium on Microarchitecture (MICRO) | 비전 트랜스포머(ViT, 이미지를 작은 조각인 토큰으로 나눠 트랜스포머로 처리하는 모델)는 자기주의(토큰들 사이의 관계를 모두 계산하는 연산)로 컴퓨터 비전 성능을 크게 높였다. 그러나 자기주의의 계산량이 토큰 수의 제곱으로 늘고 이미지 토큰 사이에 중복이 많아 계산 효율이 떨어진다. 비슷한 토큰을 합쳐 입력을 줄이는 토큰 병합이 연구됐지만 비효율적인 계산과 고정된 병합 비율 때문에 지연 성능이 나빠졌다. AdapTiV는 이미지에 맞춰 토큰을 병합하는 소프트웨어·하드웨어 공동 설계 가속기다. 병합할 토큰을 찾는 범위를 좁히는 지역 매칭, 토큰 사이 유사도 계산을 단순화한 부호 유사도, 이미지마다 병합 비율을 바꾸는 동적 병합 비율을 쓰고, 병합에 드는 시간을 층 정규화 과정 안에 숨긴다. 추가 학습 없이 정확도 손실을 1% 아래로 유지하면서 엣지 CPU·엣지 GPU·서버 CPU·서버 GPU보다 평균 309.4배·18.4배·89.8배·6.3배 빨랐다.[^p7] | 공동 1저자 S. Yoo·H. Kim, 마지막 저자 김주영 |
| 8 | 2025 | [LightNobel: Improving Sequence Length Limitation in Protein Structure Prediction Model via Adaptive Activation Quantization](https://doi.org/10.1145/3695053.3731006) · ACM/IEEE International Symposium on Computer Architecture (ISCA) | AlphaFold2·ESMFold 같은 단백질 구조 예측 모델(PPM)은 단백질의 3차원 접힘 구조를 전례 없는 정확도로 예측해 계산생물학을 바꿨다. 그러나 아미노산 서열이 긴 단백질(예를 들어 서열 길이가 1,000을 넘는 경우)에서는 활성값 크기가 기하급수적으로 커져 메모리와 계산 요구가 크게 늘어난다. LightNobel은 PPM의 서열 길이 한계를 넘으려고 만든 첫 소프트웨어·하드웨어 공동 설계 가속기라고 밝힌다. 소프트웨어 쪽에서는 토큰별 특성을 이용해 정확도를 해치지 않고 세밀하게 양자화(수를 더 적은 비트로 표현해 계산량을 줄이는 기법)하는 토큰별 적응 활성 양자화(AAQ)를 쓰고, 하드웨어 쪽에서는 여러 정밀도로 다시 구성할 수 있는 행렬 처리 장치와 다용도 벡터 처리 장치를 넣었다. NVIDIA A100·H100 GPU보다 최대 8.44배·8.41배 빠르고 전력 효율이 37.29배·43.35배 높았으며, 정확도 손실은 무시할 만했다. 최대 메모리 요구량을 최대 120.05배 줄여 서열이 긴 단백질도 처리할 수 있게 했다.[^p8] | 공동 1저자 S. Han·S. Choi, 마지막 저자 김주영 |

## 교수와 전문 분야

김주영 교수는 KAIST 전기및전자공학부 부교수다.[^eelist][^prof] 전기및전자공학부 교수진 목록은 주요 연구를 VLSI 설계, 컴퓨터 구조, FPGA, 하드웨어-소프트웨어 코디자인으로 적고 연구 디비전을 Circuit, Computer로 적는다.[^eelist] 반도체시스템공학과 연구실 목록에도 반도체 시스템 및 집적회로 분야의 CAST Hardware Innovation Lab으로 올라 있다.[^sselist] KAIST에서 전기공학 학사(2005), 석사(2007), 박사(2010)를 받았고, 박사학위 논문은 시각 인지 엔진을 갖춘 고성능·저전력 실시간 다중 물체 인식 프로세서였다(지도교수 Hoi-Jun Yoo).[^prof]

연구실 Professor 페이지에 따르면 교수는 KAIST 박사후연구원(2010–2012)을 거쳐 Microsoft Research에서 방문연구원(2010–2011), 연구원(2012–2014), 선임연구원(2014–2017)으로 일했고, Microsoft Azure에서 하드웨어 엔지니어링 리드(2017–2019)로 대규모 빅데이터 분석 플랫폼 Azure Data Lake의 하드웨어 가속을 맡았다. Microsoft Research의 Catapult 프로젝트 초기 멤버로 데이터센터에 FPGA 묶음을 배치해 기계학습·데이터 저장·네트워킹 같은 핵심 클라우드 서비스를 가속했다.[^prof] 지금은 KAIST AI Semiconductor Systems Research Center 센터장이고, 2023년 생성 인공지능용 AI 프로세서를 만드는 AI 칩 스타트업 HyperAccel을 창업했다.[^prof] 연구 관심사는 VLSI 설계, 컴퓨터 구조, FPGA, 특정 분야 전용 가속기, 하드웨어·소프트웨어 공동 설계, 빠르게 반복하는 하드웨어 개발 방식(agile hardware development)이다.[^prof]

교수는 2024 IEEE Micro Best Paper Award, 2016·2014 IEEE Micro Top Picks Award, 2010·2008 DAC/ISSCC Student Design Contest Award, 2006 A-SSCC Student Design Contest Award를 받았고, 2020–2022년 학술지 IEEE Transactions on Circuits and Systems I: Regular Papers의 부편집장(Associate Editor)을 지냈다.[^prof] IEEE Senior Member이며,[^prof] 2026년 2월 Y-KAST 회원으로 선임됐다는 소식이 있다.[^news] Patents 페이지에는 Microsoft 재직 때의 미국 특허(서버에서의 심층 신경망 분할, 하드웨어 가속기 위의 합성곱 신경망, 무손실 압축용 고대역 구조)와 2011년에 등록된 국내 특허가 발명자 목록과 함께 올라 있다.[^patents]

논문으로 보면 전문 분야는 다섯 갈래다. 대형 언어 모델 추론용 FPGA 장치와 프로세서(대표 논문 1, 2),[^p1][^p2] PIM 칩과 구조(대표 논문 3, 4),[^p3][^p4] 생성 인공지능을 기기에서 돌리는 칩(대표 논문 5),[^p5] 동형 암호 가속(대표 논문 6),[^p6] 특정 인공지능 모델에 맞춘 가속기(대표 논문 7, 8)다.[^p7][^p8]

## 응용 분야

대표 논문들은 DFX가 클라우드 데이터센터의 글 생성 작업에 유망한 해법이고,[^p1] HuMoniX가 자원이 제한된 엣지 환경의 사람 동작 생성에 효율적이고 실용적인 해법이라고 보았다.[^p5] SP-PIM은 배터리가 한정된 엣지 기기에서의 학습을 겨냥해 CIFAR10·CIFAR100 데이터셋으로 기기 안 학습을 처음부터 끝까지 해 보였다.[^p3] LightNobel은 큰 단백질이나 복합체처럼 생물학·제약에서 중요한 긴 서열 단백질의 구조 예측을 가능하게 한다고 보았다.[^p8] LPU는 교수가 창업한 HyperAccel이 내놓은 LLM 추론 프로세서이고, 대표 논문 2는 LPU 기반 서버의 에너지 효율을 Nvidia 서버와 비교했다.[^p2][^prof]

교수가 연구 책임자로 이끄는 Artificial Intelligence Semiconductor System Research Center(AISS)는 인재 양성 성과로 MSIT 장관상(Minister’s Award)을 받았고, 교수 개인도 2022 Future AI Semiconductor Technology Conference에서 AI 프로세서와 PIM 반도체 기술의 국가 연구개발, 반도체 인재 양성, 팹리스(칩을 설계만 하고 생산은 맡기는 회사) 생태계에 기여한 공로로 MSIT 장관상을 받았다.[^awards] 첫 화면의 Research Partners에는 Microsoft Research, 삼성전자, SK하이닉스, 현대자동차그룹, Naver Labs의 로고가 있다.[^home]

## 구성원

연구실 누리집 Students 페이지의 박사과정 30명, 석사과정 19명과 2026년 학부 개별연구(Individual Research) 학생 12명이다.[^students] 과정과 입학 학기는 페이지 표기이고, 박사과정 가운데 두 명은 입학 학기 옆에 (MS)가 적혀 있다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Seungjae Yoo | 박사과정 | 입학 2023 Spring | goldenyoo@kaist.ac.kr | 7 |
| Junsoo Kim | 박사과정 | 입학 2023 Spring | junsoo999@kaist.ac.kr | 1, 2 |
| Seungjae Moon | 박사과정 | 입학 2023 Fall | sjaemoon@kaist.ac.kr | 1, 2 |
| Jaeuk Kim | 박사과정 | 입학 2023 Fall | kju5789@kaist.ac.kr | 3 |
| Sukbin Lim | 박사과정 | 입학 2023 Fall | sukbin.lim@kaist.ac.kr | 2 |
| In-Jun Jung | 박사과정 | 입학 2023 Fall | injun@kaist.ac.kr |  |
| Adiwena Putra | 박사과정 | 입학 2023 Fall | adiwena.research@kaist.ac.kr | 5, 6 |
| Geonwoo Ko | 박사과정 | 입학 2024 Spring | geonwooko@kaist.ac.kr |  |
| Jaeyoung Kim | 박사과정 | 입학 2024 Spring | jykim1109@kaist.ac.kr |  |
| Seunghee Han | 박사과정 | 입학 2024 Spring | shhan1755@kaist.ac.kr | 8 |
| Hyunjun Cho | 박사과정 | 입학 2024 Fall | h.cho@kaist.ac.kr | 4 |
| Yi Chen | 박사과정 | 입학 2024 Fall | chenyi@kaist.ac.kr | 6 |
| Junseo Cha | 박사과정 | 입학 2024 Fall | chajs0909@kaist.ac.kr | 2 |
| Jinho Yang | 박사과정 | 입학 2025 Spring | jh_yang@kaist.ac.kr |  |
| Jieon Yoon | 박사과정 | 입학 2025 Spring | j9e8y@kaist.ac.kr | 5 |
| Sungwoong Yune | 박사과정 | 입학 2025 Spring | imwooong@kaist.ac.kr | 5 |
| Seri Ham | 박사과정 | 입학 2025 Spring | seri1215@kaist.ac.kr |  |
| Jaeho Jeon | 박사과정 | 입학 2024 Spring (MS) | math15738@kaist.ac.kr |  |
| Hangyeol Kim | 박사과정 | 입학 2025 Fall | khk070623@kaist.ac.kr | 7 |
| Seeyeon Kim | 박사과정 | 입학 2025 Fall | seeyakim@kaist.ac.kr |  |
| Tho Mai | 박사과정 | 입학 2025 Fall | thomh1511@kaist.ac.kr |  |
| Cuong Duong Manh | 박사과정 | 입학 2025 Fall | cuongdm1410@kaist.ac.kr |  |
| Teokkyu Suh | 박사과정 | 입학 2026 Spring | ejrrb102@kaist.ac.kr |  |
| Muyoung Son | 박사과정 | 입학 2026 Spring | kkt1690@kaist.ac.kr |  |
| Yuntae Kim | 박사과정 | 입학 2026 Spring | yuntaekim@kaist.ac.kr |  |
| Soongyu Choi | 박사과정 | 입학 2026 Spring | soongyu1291@kaist.ac.kr | 2, 8 |
| Ryeowook Ko | 박사과정 | 입학 2026 Spring | ryeowookko@kaist.ac.kr | 2 |
| Hangyeol Lee | 박사과정 | 입학 2026 Spring | lhg4294@kaist.ac.kr | 5 |
| Gyeongrok Yang | 박사과정 | 입학 2026 Fall | toddlerf@kaist.ac.kr |  |
| Wonjin Shin | 박사과정 | 입학 2025 Fall (MS) | 2swj1202@kaist.ac.kr |  |
| Sejeong Yang | 석사과정 | 입학 2025 Spring | 02yangsj@kaist.ac.kr |  |
| Joonyong Park | 석사과정 | 입학 2025 Spring | wndy2001@kaist.ac.kr |  |
| Jaeha Min | 석사과정 | 입학 2025 Spring | derekmin0807@kaist.ac.kr |  |
| Hyojeong Lee | 석사과정 | 입학 2025 Spring | hjlee8877@kaist.ac.kr |  |
| Quang-Anh Pham | 석사과정 | 입학 2025 Spring | anhpq3105@kaist.ac.kr |  |
| Jaehun Lee | 석사과정 | 입학 2025 Spring | jaehunlee@kaist.ac.kr |  |
| Suheon Jeong | 석사과정 | 입학 2025 Spring | sh.jeong@kaist.ac.kr |  |
| Sanghyun Lee | 석사과정 | 입학 2025 Fall | lysanghyun@kaist.ac.kr |  |
| Jong-Jin Baek | 석사과정 | 입학 2025 Fall | jjbaek@kaist.ac.kr |  |
| Hyunwoo Yoo | 석사과정 | 입학 2026 Spring | yhwoo7@kaist.ac.kr |  |
| Juhyeong Jin | 석사과정 | 입학 2026 Spring | pearlbro@kaist.ac.kr |  |
| Won Ji | 석사과정 | 입학 2026 Spring | won.ji@kaist.ac.kr |  |
| Donggeun Kim | 석사과정 | 입학 2026 Spring | kdg01723@kaist.ac.kr |  |
| Junha Park | 석사과정 | 입학 2026 Spring | qkrwnsgk0303@kaist.ac.kr |  |
| Woong-Gyu Park | 석사과정 | 입학 2026 Spring | wgpark00@kaist.ac.kr |  |
| Jeongmo Lee | 석사과정 | 입학 2026 Spring | dlsxprmfkf1234@kaist.ac.kr |  |
| Doyeong Yoo | 석사과정 | 입학 2026 Spring | tony8181@kaist.ac.kr |  |
| Nahye Kim | 석사과정 | 입학 2026 Fall | iachristian@kaist.ac.kr |  |
| Kyoungju Kim | 석사과정 | 입학 2026 Fall | jfmam_jjasond12@kaist.ac.kr |  |
| Youngrae Cho | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Hyeonmin Han | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Yang Woo Lee | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Chaeyoung Son | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Chaehyeon Kwak | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Kyoungju Kim | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Mingyu Choi | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Tsai-Yen Hsieh | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Seung Ik Jo | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Hyeongwoo Jin | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Birm Jin Kim | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |
| Soyun Kim | 학부 연구생 (Individual Research, Spring) | 2026 |  |  |

## 졸업생과 이전 구성원

누리집 Alumni 페이지의 박사 7명·석사 12명과, Students 페이지의 2021–2025년 학부 개별연구 참여 90건이다(같은 사람이 여러 해에 올라 있으면 해마다 한 줄). 학위·과정 칸의 괄호는 누리집이 적은 입학 학기 또는 참여 학기이고, 진로는 누리집 표기다.[^alumni][^students]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Ji-Hoon Kim | Ph.D. (입학 2019 Fall) | Apple Inc. |
| Prasetiyo | Ph.D. (입학 2020 Spring) | Samsung Electronics |
| Seongmin Hong | Ph.D. (입학 2020 Fall) | Co-Founder at HyperAccel |
| Jaehoon Heo | Ph.D. (입학 2022 Spring) | Meta |
| Junghoon Kim | Ph.D. (입학 2022 Spring) | Co-Founder at HyperAccel |
| Sungyeob Yoo | Ph.D. (입학 2022 Spring) |  |
| Donghyuk Kim | Ph.D. (입학 2022 Fall) | AMD |
| Sanghyun Jeong | M.S. (입학 2020 Spring) | Samsung Electronics |
| Yeoreum Park | M.S. (입학 2020 Spring) | Samsung Electronics |
| Gyeongcheol Shin | M.S. (입학 2020 Fall) | SK Hynix |
| Je Yang | M.S. (입학 2020 Fall) | Ph.D. Student at Columbia University |
| Yashael Faith Arthanto | M.S. (입학 2020 Fall) | Rebellions Inc. |
| Wontak Han | M.S. (입학 2021 Spring) | Samsung Electronics |
| Nogeun Joo | M.S. (입학 2021 Spring) | Sk Hynix |
| Sukjin Lee | M.S. (입학 2022 Spring) | Samsung Electronics |
| Donghyeon Choi | M.S. (입학 2023 Fall) | HyperAccel |
| Minjun Park | M.S. (입학 2024 Fall) |  |
| Junsoo Lim | M.S. (입학 2024 Fall) |  |
| Hyunmin Choi | M.S. (입학 2024 Fall) | Qualcomm |
| Eunyong Lee | 학부 연구생 (Individual Research, Spring) (2025) |  |
| Wonjin Shin | 학부 연구생 (Individual Research, Spring) (2025) |  |
| Jeongmin Oh | 학부 연구생 (Individual Research, Spring) (2025) |  |
| Dongseok Ji | 학부 연구생 (Individual Research, Spring) (2025) |  |
| Junha Park | 학부 연구생 (Individual Research, Spring) (2025) |  |
| Jeongmo Lee | 학부 연구생 (Individual Research, Spring, Summer, Fall) (2025) |  |
| Siyeon Lee | 학부 연구생 (Individual Research, Summer) (2025) |  |
| Jaegeun Lee | 학부 연구생 (Individual Research, Summer) (2025) |  |
| Jonghyeon Lee | 학부 연구생 (Individual Research, Summer, Fall) (2025) |  |
| Hyeonmin Han | 학부 연구생 (Individual Research, Summer, Fall, Winter) (2025) |  |
| Juseung Choi | 학부 연구생 (Individual Research, Summer) (2025) |  |
| Jung Woo Kang | 학부 연구생 (Individual Research, Summer) (2025) |  |
| Mingyu Choi | 학부 연구생 (Individual Research, Summer, Fall, Winter) (2025) |  |
| Hyunseo Kim | 학부 연구생 (Individual Research, Fall) (2025) |  |
| Hyojin Kwon | 학부 연구생 (Individual Research, Fall) (2025) |  |
| Youngrae Cho | 학부 연구생 (Individual Research, Fall) (2025) |  |
| Kyoungju Kim | 학부 연구생 (Individual Research, Fall, Winter) (2025) |  |
| Chaehyeon Kwak | 학부 연구생 (Individual Research, Fall, Winter) (2025) |  |
| Yang Woo Lee | 학부 연구생 (Individual Research, Winter) (2025) |  |
| Seyun Bae | 학부 연구생 (Individual Research, Winter) (2025) |  |
| Jeongmin Lee | 학부 연구생 (Individual Research, Winter) (2025) |  |
| Yeonwoo Ji | 학부 연구생 (Individual Research, Winter) (2025) |  |
| Gurim Park | 학부 연구생 (Individual Research, Winter) (2025) |  |
| Chaeyoung Son | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Seungbin Shin | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Minjun Park | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Minkyu Lee | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Jaehyun Ryu | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Soohun Jung | 학부 연구생 (Individual Research, Spring, Summer, Fall) (2024) |  |
| Gyeongrok Yang | 학부 연구생 (Individual Research, Spring) (2024) |  |
| Sejung Yang | 학부 연구생 (Individual Research, Summer, Fall) (2024) |  |
| Seungjun Lee | 학부 연구생 (Individual Research, Summer) (2024) |  |
| Hyunkyu Park | 학부 연구생 (Individual Research, Summer) (2024) |  |
| Yoongun Song | 학부 연구생 (Individual Research, Summer) (2024) |  |
| Yongwon Park | 학부 연구생 (Individual Research, Summer) (2024) |  |
| Dongwan Kim | 학부 연구생 (Individual Research, Summer) (2024) |  |
| Hyojung Lee | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Seoyoon Kim | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Wonjin Shin | 학부 연구생 (Individual Research, Fall, Winter) (2024) |  |
| Byungkyu Park | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Jaeha Min | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Seunghun Shin | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Dongeun Kim | 학부 연구생 (Individual Research, Fall) (2024) |  |
| Mingyu Choi | 학부 연구생 (Individual Research, Winter) (2024) |  |
| Jeongmo Lee | 학부 연구생 (Individual Research, Winter) (2024) |  |
| Hyeonjoong Kim | 학부 연구생 (Individual Research, Winter) (2024) |  |
| Dongha Kim | 학부 연구생 (Individual Research, Summer, Winter) (2023) |  |
| Sejung Yang | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Wonjin Shin | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Hyeri Shin | 학부 연구생 (Individual Research, Spring, Summer, Fall) (2023) |  |
| Kiho Kim | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Dongmin Choi | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Byungkyu Park | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Yuntae Kim | 학부 연구생 (Individual Research, Summer, Fall) (2023) |  |
| Hangyeol Lee | 학부 연구생 (Individual Research, Summer) (2023) |  |
| Teokkyu Seo | 학부 연구생 (Individual Research, Summer, Fall) (2023) |  |
| Minjun Park | 학부 연구생 (Individual Research, Fall) (2023) |  |
| Jaehyun Ryu | 학부 연구생 (Individual Research, Fall, Winter) (2023) |  |
| Mintaek Lim | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Jaeha Min | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Soohun Jung | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Gyeongrok Yang | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Minkyu Lee | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Chaeeun Yoo | 학부 연구생 (Individual Research, Winter) (2023) |  |
| Seeyeon Kim | 학부 연구생 (Individual Research, Summer, Fall) (2022) |  |
| Jieon Yoon | 학부 연구생 (Individual Research, Summer) (2022) |  |
| Kiyeon Lee | 학부 연구생 (Individual Research, Summer) (2022) |  |
| Seongho Kim | 학부 연구생 (Individual Research, Spring) (2022) |  |
| Hyunjun Cho | 학부 연구생 (Individual Research, Spring) (2022) |  |
| Junseo Cha | 학부 연구생 (Individual Research, Spring) (2022) |  |
| Chaeran Yun | 학부 연구생 (Individual Research, Winter) (2022) |  |
| Jaegeun Bae | 학부 연구생 (Individual Research, Winter) (2022) |  |
| Seongjin Gong | 학부 연구생 (Individual Research, Winter) (2022) |  |
| Seoungjun Lee | 학부 연구생 (Individual Research, Fall) (2021) |  |
| Woojin Jeong | 학부 연구생 (Individual Research, Summer) (2021) |  |
| Sihun Kim | 학부 연구생 (Individual Research, Summer) (2021) |  |
| Taehyung Park | 학부 연구생 (Individual Research, Spring) (2021) |  |
| Yoongjeong Cha | 학부 연구생 (Individual Research, Spring, Summer) (2021) |  |
| Huichan Shin | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Minseok Kim | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Seungguk Lee | 학부 연구생 (Individual Research, Winter, Spring) (2021) |  |
| Byeongjun Shin | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Donghyeon Choi | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Minh Quang Nguyen | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Seunghee Han | 학부 연구생 (Individual Research, Winter, Spring, Summer) (2021) |  |
| Sukbin Lim | 학부 연구생 (Individual Research, Winter, Spring) (2021) |  |
| Inki Kim | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Jaeuk Kim | 학부 연구생 (Individual Research, Winter, Spring) (2021) |  |
| Jaeyoung Kim | 학부 연구생 (Individual Research, Winter) (2021) |  |
| Youngmin Sim | 학부 연구생 (Individual Research, Winter) (2021) |  |

## 최근 논문 목록 (2021–2026)

2021–2026년 논문 90편이다. 누리집 Journal 목록의 학술지 논문 25편, 누리집 논문 목록의 학회 논문 63편, Books 페이지의 책과 책 속 장 2편이다. 학술지 논문과 랩 첫 화면에 실린 학회 논문 10편은 랩 표기를 따랐고, 저자 이름 앞이나 뒤의 *는 누리집이 같은 기여(equal contribution)로 적은 표시다.[^pubs][^crossref]

**2026**

- Jaehun Lee, In-Jun Jung, and Joo-Young Kim. "3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving". *IEEE Computer Architecture Letters (CAL), 2026*.
- Seunghee Han, Seokman Kim, Sanghyun Han, Younghwan Kim, Joo-Young Kim. "A 0.06pJ/b Current-Conveyor-based Current-Domain Transceiver with DC-Balanced Multi-Transmission-Line PAM Symbol Encoding". *2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*.
- Sungwoong Yune\*, Jieon Yoon\*, Hangyeol Lee, Adiwena Putra, Jaehoon Heo, Joo-Young Kim (\*equal contribution). "A 11.0 TOPS/W Diffusion Accelerator with Temporal Data Reuse for Real-Time Text-to-Motion Generation". *IEEE Journal of Solid-State Circuits (JSSC), 2026*.
- APT: Accelerating Diffusion Transformers via Attention Probability-Guided Pruning and Quantization (2026)
- Sukbin Lim\*, Jung-Hoon Kim\*, Seungjae Moon, Junseo Cha, Dongjin Seo, Jongho Kim, Hunjong Lee, Jinwon Lee, Joo-Young Kim (\*equal contribution). "Adelia: A 4-nm LLM Processing Unit with Streamlined Dataflow and Dual-Mode Parallelism for Maximizing Hardware Efficiency". *IEEE Journal of Solid-State Circuits (JSSC), 2026*.
- Soongyu Choi, Yuntae Kim, Muyoung Son, Joo-Young Kim. "Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding". *2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA)*.
- CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution (2026)
- Yi Chen, Hanna Hsieh, Shuhong Liu, Chuanbo Hua, Zihan Ma, Kun Wang, Joo-Young Kim. "Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness". *The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2026*.
- Sungwoong Yune, Suheon Jeong, Joo-Young Kim. "FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis". *Lecture Notes in Computer Science*.
- Teokkyu Suh, Junsoo Lim, Jae-Young Kim, Minjun Park, Hyunmin Choi, Jaeha Min, Sungwoong Yune, Joo-Young Kim. "GAREN: A 890.9 FPS, 412 iter/s 3D Gaussian Splatting Rendering and Modeling Accelerator with Hybrid Sorting, Out of Range Filtering, and Gradient Skipping". *IEEE Asian Solid-State Circuits Conference (A-SSCC), 2026*.
- Jongjin Baek, Won Ji, Seungjae Yoo, Joo-Young Kim. "Hot–Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving". *IEEE Computer Architecture Letters (CAL), 2026*.
- MASQ: Accelerating Masked Diffusion via Stage-Wise Multi-Precision Quantization (2026)
- NOVA: Technology-Architecture Co-Design of Near-Memory Processing for Attention-SSM-MoE Hybrid LLM Inference (2026)
- NetFED: Network-Aware Acceleration for Multi-Key Privacy-Preserving Federated Learning Aggregation (2026)
- ORBIS: Output-Guided Token Reduction with Distribution-Aware Matching for Video Diffusion Acceleration (2026)
- Adiwena Putra, Hyunjun Cho, Sungwoong Yune, Cuong Manh Duong, Jaeho Jeon, Joo-Young Kim. "OmniCrypt: A 435.86M GOPS/W Bootstrappable Multi-Scheme FHE Accelerator with On-Chip Data Generation for Privacy-Preserving Computation". *2026 IEEE International Solid-State Circuits Conference (ISSCC)*.
- Yi Chen, Wonjin Shin, Shuhong Liu, Tho Mai, Jeongmo Lee, Chuanbo Hua, Kun Wang, Jun Liu, Joo-Young Kim. "POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models". *The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), 2026*.
- Joonyong Park, Hyojeong Lee, Sejeong Yang, Joo-young Kim. "PaFeDSE: Pareto-Feedback-Guided Microarchitecture Design Space Exploration for Efficient Pareto Search". *32nd Asia and South Pacific Design Automation Conference (ASP-DAC), 2027*.
- Tho Mai, Joo-Young Kim. "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference". *The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS), 2026*.
- Hangyeol Lee, Hyojeong Lee, Joo-Young Kim. "Rethinking Token Reduction for Diffusion Models via Output-Similarity-Awareness". *Lecture Notes in Computer Science*.
- Jae-Young Kim, Teokkyu Suh, Junsoo Lim, Minjun Park, Hyunmin Choi, Jaeha Min, Donghyuk Kim, Joo-Young Kim. "Specter: 376 fps 2.67 nJ/pixel 4DGS Processor for Spatiotemporal Reconstruction with Contribution-Ordered Rendering and Deformation-aware Modeling". *2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*.
- Seungjae Yoo, Hangyeol Kim, Muyoung Son, Yi Chen, Suheon Jeong, Joo-Young Kim. "Tri-Oracle: A 17.78 μJ/Token Vision-Language Model Accelerator with Token-Attention-Weight Redundancy Prediction". *2026 IEEE International Solid-State Circuits Conference (ISSCC)*.
- Trident: A 28nm 1.83-to-9.74 pJ/bit Multi-Parameter FHE Processor with Unified Constant Geometry Datapath for Privacy Preserving Client-Server Computing (2026)
- Donghyuk Kim, Sejeong Yang, Wonjin Shin, Joo-Young Kim. "V-Rex: Real-Time Streaming Video LLM Acceleration via Dynamic KV Cache Retrieval". *2026 IEEE International Symposium on High Performance Computer Architecture (HPCA)*.
- ZK-Flex: A Flexible and Scalable Framework for Accelerating Zero-Knowledge Proofs (2026)

**2025**

- Jaehoon Heo, Adiwena Putra, Sungwoong Yune, Jieon Yoon, Hangyeol Lee, Ji-Hoon Kim, Joo-Young Kim. "A 57.3 fps 12.8 TFLOPS/W Text-to-Motion Processor with Inter-Iteration Output Sparsity and Inter-Frame Joint Similarity". *IEEE Journal of Solid-State Circuits (JSSC), 2025*.
- Gyeongrok Yang, Jaeha Min, In-Jun Jung, Joo-Young Kim. "A Quantitative Analysis of Mamba-2-based Large Language Model: Study of State Space Duality". *IEEE Computer Architecture Letters (CAL), 2025*.
- Sungwoong Yune, Hyojeong Lee, Adiwena Putra, Hyunjun Cho, Cuong Duong Manh, Jaeho Jeon, Joo-Young Kim. "ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption". *2025 62nd ACM/IEEE Design Automation Conference (DAC)*.
- Junsoo Kim, Hunjong Lee, Geonwoo Ko, Gyubin Choi, Seri Ham, Seongmin Hong, Joo-Young Kim. "ADOR: A Design Exploration Framework for LLM Serving with Enhanced Latency and Throughput". *2025 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)*.
- Jung-Hoon Kim, Sukbin Lim, Junseo Cha, Seungjae Moon, Dongjin Seo, Hunjong Lee, Jongho Kim, Jinwon Lee, Joo-Young Kim. "Adelia: A 4nm LLM Accelerator with Streamlined Dataflow and Dual-Mode Parallelization for Efficient Generative AI Inference". *2025 Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*.
- Hangyeol Kim, Joo-Young Kim. "An Efficient FPGA Accelerator with Spatiotemporal Tubelet Merging for Video Transformers". *2025 IEEE Asian Solid-State Circuits Conference (A-SSCC)*.
- Sungyeob Yoo, Seeyeon Kim, Geonwoo Ko, Seri Ham, Yi Chen, Joo-Young Kim. "An End-to-End Diffusion Accelerator With Reconfigurable Hyper-Precision and Unified Non-Matrix Processing Engine". *IEEE Transactions on Circuits and Systems I (TCAS-I), 2025*.
- Yi Chen, Muyoung Son, Chuanbo Hua, Joo-Young Kim. "AoP-SAM: Automation of Prompts for Efficient Segmentation". *Proceedings of the AAAI Conference on Artificial Intelligence*.
- Donghyuk Kim, In-Jun Jung, Geonwoo Ko, Seri Ham, Cuong Duong Manh, Gyeongrok Yang, Joo-Young Kim. "D3TA: 38.9TOPS/W Transformer Accelerator with Dual-Port 3T-eDRAM Digital Compute-In-Memory Using HyperAttention and Triple-Sparsity-Handling". *2025 IEEE European Solid-State Electronics Research Conference (ESSERC)*.
- Donghyuk Kim, Jae-Young Kim, Hyunjun Cho, Seungjae Yoo, Sukjin Lee, Sungwoong Yune, Sejeong Yang, Hoichang Jeong, Keonhee Park, Ki-Soo Lee, Jongchan Lee, Chanheum Han, Gunmo Koo, Yuli Han, Jaejin Kim, Jaemin Kim, Kyuho Jason Lee, Joo-Hyung Chae, Kunhee Cho, and Joo-Young Kim. "DPIM: A 2T1C eDRAM Transformer-in-Memory Chip with Sparsity-Aware Quantization and Heterogeneous Dense-Sparse Core". *IEEE Journal of Solid-State Circuits (JSSC), 2025*.
- Donghyuk Kim, Jae-Young Kim, Wontak Han, Jongsoon Won, Haerang Choi, Yongkee Kwon, Joo-Young Kim. "Darwin: A DRAM-based Multi-level Processing-in-Memory Architecture for Column-Oriented Database". *IEEE Transactions on Emerging Topics in Computing (TETC), 2024*.
- Jaehoon Heo, Adiwena Putra, Jieon Yoon, Sungwoong Yune, Hangyeol Lee, Ji-Hoon Kim, Joo-Young Kim. "EXION: Exploiting Inter- and Intra-Iteration Output Sparsity for Diffusion Models". *2025 IEEE International Symposium on High Performance Computer Architecture (HPCA)*.
- In-Jun Jung, Gyeongrok Yang, Jaeha Min, Joo-Young Kim. "HLX: A Unified Pipelined Architecture for Optimized Performance of Hybrid Transformer-Mamba Language Models". *Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture*.
- Sukbin Lim, Jaehoon Heo, Jinho Yang, Joo-Young Kim. "Hawkeye: A Point Cloud Neural Network Processor with Virtual Pillar and Quadtree-based Workload Management for Real-Time Outdoor BEV Detection". *IEEE Journal of Solid-State Circuits (JSSC), 2025*.
- Jaehoon Heo, Adiwena Putra, Sungwoong Yune, Jieon Yoon, Hangyeol Lee, Jihoon Kim, Joo-Young Kim. "HuMoniX: A 57.3 fps 12.8 TFLOPS/W Text-to-Motion Processor with Inter-Iteration Output Sparsity and Inter-Frame Joint Similarity". *IEEE International Solid-State Circuits Conference (ISSCC), 2025*.
- Seungjae Moon, Junseo Cha, Hyunjun Park, Joo-Young Kim. "Hybe: GPU-NPU Hybrid System for Efficient LLM Inference with Million-Token Context Window". *Proceedings of the 52nd Annual International Symposium on Computer Architecture*.
- \*Seunghee Han, \*Soongyu Choi, Joo-Young Kim (\*equal contribution). "LightNobel: Improving Sequence Length Limitation in Protein Structure Prediction Model via Adaptive Activation Quantization". *ACM/IEEE International Symposium on Computer Architecture (ISCA), 2025*.
- Jieon Yoon, Sungwoong Yune, Hangyeol Lee, Adiwena Putra, Jaehoon Heo, Joo-Young Kim. "MoDiff: a 11.0 TOPS/W Diffusion Accelerator with Temporal Data Reuse for Real-Time Text-to-Motion Generation". *2025 IEEE Asian Solid-State Circuits Conference (A-SSCC)*.
- Minsu Kim, Seongmin Hong, RyeoWook Ko, Soongyu Choi, Hunjong Lee, Junsoo Kim, Joo-Young Kim, Jongse Park. "Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization". *Proceedings of the 52nd Annual International Symposium on Computer Architecture*.
- Wontak Han, Hyunjun Cho, Donghyuk Kim, Joo-Young Kim. "SAL-PIM: A Subarray-level Processing-in-Memory Architecture with LUT-based Linear Interpolation for Transformer-based Text Generation". *IEEE Transactions on Computers (TC), 2025*.
- Jinho Yang, Ji-Hoon Kim, Joo-Young Kim. "SCRec: A Scalable Computational Storage System with Statistical Sharding and Tensor-train Decomposition for Recommendation Models". *IEEE Transactions on Computers (TC), 2025*.
- \*Geonwoo Ko, \*Sungyeob Yoo, Seri Ham, Seeyeon Kim, Minkyu Kim, Joo-Young Kim (\*equal contribution). "SuFP: Piecewise Bit Allocation Floating-Point for Robust Neural Network Quantization". *Transactions on Machine Learning Research (TMLR), 2025*.

**2024**

- Sukbin Lim, Jaehoon Heo, Jinho Yang, Joo-Young Kim. "A 38.5TOPS/W Point Cloud Neural Network Processor with Virtual Pillar and Quadtree-based Workload Management for Real-Time Outdoor BEV Detection". *2024 IEEE Custom Integrated Circuits Conference (CICC)*.
- Jinho Yang, Sungwoong Yune, Sukbin Lim, Donghyuk Kim, Joo-Young Kim. "ACane: An Efficient FPGA-based Embedded Vision Platform with Accumulation-as-Convolution Packing for Autonomous Mobile Robots". *2024 29th Asia and South Pacific Design Automation Conference (ASP-DAC)*.
- Hyunjun Cho, Jaeho Jeon, Jaehoon Heo, Joo-Young Kim. "APINT: A Full-Stack Framework for Acceleration of Privacy-Preserving Inference of Transformers based on Garbled Circuits". *Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design*.
- \*Seungjae Yoo, \*Hangyeol Kim, Joo-Young Kim (\*equal contribution). "AdapTiV: Sign-Similarity based Image-Adaptive Token Merging for Vision Transformer Acceleration". *ACM/IEEE International Symposium on Microarchitecture (MICRO), 2024*.
- Seunghee Han, Seungjae Moon, Teokkyu Suh, JaeHoon Heo, Joo-Young Kim. "BLESS: Bandwidth and Locality Enhanced SMEM Seeding Acceleration for DNA Sequencing". *2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA)*.
- Donghyuk Kim, Jae-Young Kim, Hyunjun Cho, Seungjae Yoo, Sukjin Lee, Sungwoong Yune, Hoichang Jeong, Keonhee Park, Ki-Soo Lee, Jongchan Lee, Chanheum Han, Gunmo Koo, Yuli Han, Jaejin Kim, Jaemin Kim, Kyuho Lee, Joo-Hyung Chae, Kunhee Cho, Joo-Young Kim. "DPIM: A 19.36TOPS/W 2T1C eDRAM Transformer-in-Memory Chip with Sparsity-Aware Quantization and Heterogeneous Dense-Sparse Core". *2024 IEEE European Solid-State Electronics Research Conference (ESSERC)*.
- Junsoo Kim, Seunghee Han, Geonwoo Ko, Ji-Hoon Kim, Changha Lee, Taewoo Kim, Chan-Hyun Youn, Joo-Young Kim. "EPU: An Energy-Efficient Explainable AI Accelerator with Sparsity-free Computation and Heat Map Compression/Pruning". *IEEE Journal of Solid-State Circuits (JSSC), 2024*.
- Seungjae Moon, Jung-Hoon Kim, Junsoo Kim, Seongmin Hong, Junseo Cha, Minsu Kim, Sukbin Lim, Gyubin Choi, Dongjin Seo, Jongho Kim, Hunjong Lee, Hyunjun Park, Ryeowook Ko, Soongyu Choi, Jongse Park, Jinwon Lee, Joo-Young Kim. "LPU: A Latency-Optimized Highly Scalable Processor for Large Language Model Inference". *IEEE Micro, 2024*.
- Prasetiyo, Adiwena Putra, Joo-Young Kim. "Morphling: A Throughput-Maximized TFHE-based Accelerator using Transform-domain Reuse". *2024 IEEE International Symposium on High-Performance Computer Architecture (HPCA)*.
- Sungyeob Yoo, Geonwoo Ko, Seri Ham, Seeyeon Kim, Yi Chen, Joo-Young Kim. "Picasso: A 28nm 4.96 TOPS/W End-to-End Diffusion Accelerator with Reconfigurable Hyper-Precision and Unified Non-Matrix Processing Engine". *2024 IEEE European Solid-State Electronics Research Conference (ESSERC)*.
- Sungyeob Yoo, Geonwoo Ko, Seri Ham, Seeyeon Kim, Yi Chen, Joo-Young Kim. "Picasso: An Area/Energy-Efficient End-to-End Diffusion Accelerator with Hyper-Precision Data Type". *2024 IEEE Hot Chips 36 Symposium (HCS)*.
- \*Jaehoon Heo, \*Jung-Hoon Kim, Wontak Han, Jaeuk Kim, Joo-Young Kim (\*equal contribution). "SP-PIM: A Super-Pipelined Processing-In-Memory Accelerator with Local Error Prediction for Area/Energy-Efficient On-Device Learning". *IEEE Journal of Solid-State Circuits (JSSC), 2024*.
- Ji-Hoon Kim, Seunghee Han, Kwanghyun Park, Soo-Young Ji, Joo-Young Kim. "Trinity: In-Database Near-data Machine Learning Acceleration Platform for Advanced Data Analytics". *IEEE Access, 2024*.

**2023**

- Junsoo Kim, Geonwoo Ko, Ji-Hoon Kim, Changha Lee, Taewoo Kim, Chan-Hyun Youn, Joo-Young Kim. "A 26.55TOPS/W Explainable AI Processor with Dynamic Workload Allocation Heat Map Compression/Pruning". *2023 IEEE Custom Integrated Circuits Conference (CICC)*.
- Donghyuk Kim, Sanghyun Jeong, Joo-Young Kim. "Agamotto: A Performance Optimization Framework for CNN Accelerator with Row Stationary Dataflow". *IEEE Transactions on Circuits and Systems I (TCAS-I), 2023*.
- HyperAccel LPU: Accelerating Hyperscale Models for Generative AI (2023)
- Je Yang, Sukbin Lim, Sukjin Lee, Jae-Young Kim, Joo-Young Kim. "JNPU: A 1.04TFLOPS Joint-DNN Training Processor with Speculative Cyclic Quantization and Triple Heterogeneity on Microarchitecture / Precision / Dataflow". *ESSCIRC 2023- IEEE 49th European Solid State Circuits Conference (ESSCIRC)*.
- LightTrader: A Standalone AI-enabled High-Frequency Trading System with 16 TFLOPS / 64 TOPS Deep Learning Inference Accelerators (2023)
- Jaehoon Heo, Yongwon Shin, Sangjin Choi, Sungwoong Yune, Jung-Hoon Kim, Hyojin Sung, Youngjin Kwon, Joo-Young Kim. "PRIMO: A Full-Stack Processing-in-DRAM Emulation Framework for Machine Learning Workloads". *2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD)*.
- Jung-Hoon Kim, Jaehoon Heo, Wontak Han, Jaeuk Kim, Joo-Young Kim. "SP-PIM: A 22.41TFLOPS/W, 8.81Epochs/Sec Super-Pipelined Processing-In-Memory Accelerator with Local Error Prediction for On-Device Learning". *2023 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*.
- Ji-Hoon Kim, Sungyeob Yoo, Joo-Young Kim. "South Korea’s Nationwide Effort for AI Semiconductor Industry". *Communications of the ACM (CACM), 2023*.
- Adiwena Putra, Prasetiyo, Yi Chen, John Kim, Joo-Young Kim. "Strix: An End-to-End Streaming Architecture with Two-Level Ciphertext Batching for Fully Homomorphic Encryption with Programmable Bootstrapping". *IEEE/ACM International Symposium on Microarchitecture (MICRO), 2023*.

**2022**

- Jung-Hoon Kim, Sukjin Lee, Seungjae Moon, Sungyeob Yoo, Joo-Young Kim. "A 409.6 GOPS and 204.8 GFLOPS Mixed-Precision Vector Processor System for General-Purpose Machine Learning Acceleration". *2022 IEEE Asian Solid-State Circuits Conference (A-SSCC)*.
- Yeo-Reum Park, Ji-Hoon Kim, Jaeyoung Do, Joo-Young Kim. "A Dual-Mode Similarity Search Accelerator based on Embedding Compression for Online Cross-Modal Image-Text Retrieval". *2022 IEEE 30th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)*.
- Prasetiyo, Seongmin Hong, Yashael Faith Arthanto, Joo-Yong Kim. "Accelerating Deep Convolutional Neural Networks Using Number Theoretic Transform". *IEEE Transactions on Circuits and Systems I (TCAS-I), 2022*.
- Ji-Hoon Kim, Yeo-Reum Park, Jaeyoung Do, Soo-Young Ji, Joo-Young Kim. "Accelerating Large-Scale Graph-based Nearest Neighbor Search on a Computational Storage Platform". *IEEE Transactions on Computers (TC), 2022*.
- Gyeongcheol Shin, Junsoo Kim, Joo-Young Kim. "An Open-Source Shell Generation Framework for High-Performance Design on Multi-Die FPGAs". *2022 IEEE 30th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)*.
- Donghyuk Kim, Chengshuo Yu, Shanshan Xie, Yuzong Chen, Joo-Young Kim, Bongjin Kim, Jaydeep Kulkarni, Tony Tae-Hyoung Kim. "An Overview of Processing-in-Memory Circuits for Artificial Intelligence and Machine Learning". *IEEE Journal on Emerging Selected Topics in Circuits Systems (JETCAS), 2022*.
- Seongmin Hong, Seungjae Moon, Junsoo Kim, Sungjae Lee, Minsub Kim, Dongsoo Lee, Joo-Young Kim. "DFX: A Low-latency Multi-FPGA Appliance for Accelerating Transformer-based Text Generation". *IEEE/ACM International Symposium on Microarchitecture (MICRO), 2022*.
- DFX: A Low-latency Multi-FPGA Appliance for Accelerating Transformer-based Text Generation (2022)
- Wontak Han, Jaehoon Heo, Junsoo Kim, Sukbin Lim, Joo-Young Kim. "Design of Processing-in-Memory with Triple Computational Path and Sparsity Handling for Energy-Efficient DNN Training". *IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), 2022*.
- Yashael Faith Arthanto, David Ojika, Joo-Young Kim. "FSHMEM: Supporting Partitioned Global Address Space on FPGAs for Large-Scale Hardware Acceleration Infrastructure". *2022 32nd International Conference on Field-Programmable Logic and Applications (FPL)*.
- Je Yang, JaeUk Kim, Joo-Young Kim. "LearningGroup: A Real-Time Sparse Training on FPGA via Learnable Weight Grouping for Multi-Agent Reinforcement Learning". *2022 International Conference on Field-Programmable Technology (ICFPT)*.
- Hyunsung Kim, Sungyeob Yoo, Jaewan Bae, Kyeongryeol Bong, Yoonho Boo, Karim Charfi, Hyo-Eun Kim, Hyun Suk Kim, Jinseok Kim, Byungjae Lee, Jaehwan Lee, Myeongbo Shim, Sungho Shin, Jeong Seok Woo, Joo-Young Kim, Sunghyun Park, Jinwook Oh. "LightTrader: World’s first AI-enabled High-Frequency Trading Solution with 16 TFLOPS / 64 TOPS Deep Learning Inference Accelerators". *2022 IEEE Hot Chips 34 Symposium (HCS)*.
- Processing-in-Memory for AI: From Circuits to Systems- ISBN 9783030987817. Joo-Young Kim, Donghyuk Kim and Jaehoon Heo. Springer, 2022
- Jaehoon Heo, Junsoo Kim, Wontak Han, Sukbin Lim, Joo-Young Kim. "T-PIM: A 2.21-to-161.08TOPS/W Processing-In-Memory Accelerator for End-to-End On-Device Training". *2022 IEEE Custom Integrated Circuits Conference (CICC)*.
- Jaehoon Heo, Junsoo Kim, Sukbin Lim, Wontak Han, Joo-Young Kim. "T-PIM: An Energy-Efficient Processing-In-Memory Accelerator for End-to-End On-Device Training". *IEEE Journal of Solid-State Circuits (JSSC), 2022*.
- Ji-Hoon Kim, Seunghee Han, Kwanghyun Park, Soo-Young Ji, Joo-Young Kim. "Trinity: End-to-End In-Database Near-Data Machine Learning Acceleration Platform for Advanced Data Analytics". *2022 IEEE Hot Chips 34 Symposium (HCS)*.

**2021**

- A Heterogeneous Vector-Array Architecture with Resource Scheduling for Multi-User/Multi-DNN Workloads (2021)
- Ji-Hoon Kim, Yeo-Reum Park, Jaeyoung Do, Soo-Young Ji, Joo-Young Kim. "Accelerating Large-Scale Nearest Neighbor Search with Computational Storage Device". *2021 IEEE 29th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)*.
- Je Yang, Seongmin Hong, Joo-Young Kim. "FIXAR: A Fixed-Point Deep Reinforcement Learning Platform with Quantization-Aware Training and Adaptive Parallelism". *2021 58th ACM/IEEE Design Automation Conference (DAC)*.
- Ji-Hoon Kim, Juhyoung Lee, Jinsu Lee, Jaehoon Heo, Joo-Young Kim. "Z-PIM: A Sparsity-Aware Processing-In-Memory Architecture with Fully-Variable Weight Bit-Precision for Energy-Efficient Deep Neural Networks". *IEEE Journal of Solid-State Circuits (JSSC), 2021*.
- “Chapter 5 FPGA based neural network accelerators”, Advances in Computers – ISBN 9780128231234. Joo-Young Kim. Elsevier, 2021

## 수상

누리집 Awards 페이지의 10건이다. 날짜는 같은 일을 알린 News 글의 게시일이고, News 글이 없는 건은 Awards 페이지가 적은 연도이고, AISS 센터 장관상 1건은 수상 연도가 적혀 있지 않다.[^awards][^news]

- 2026-07-06 · Sungwoong Yune is awarded Deputy Prime Minister’s Award at 2026 AI Semiconductor Outstanding Achievement Competition
- 2026-02-24 · Jieon Yoon and Donghyuk Kim win Gold and Bronze Prizes at the 32nd Samsung Humantech Paper Award
- 2025-09-10 · Prof. Joo-Young Kim is awarded Minister of Trade, Industry and Energy Award in Startup Nation Korea 2025
- 2023 · Jaehoon Heo is awarded KI Convergence Day Outstanding Researcher Award
- 2023 · Prof. Joo-Young Kim is awarded Research prize in Research Category of Outstanding Faculty Awards in Commemoratino of the 53rd Founding Anniversary
- 2023 · Prof. Joo-Young Kim is awarded KAIST Q-Day Faculty Special Awards in S (technology value creation) category
- 2023-02-20 · Je Yang’s paper on Joint-DNN Training Processor gets Gold Prize
- 2022 · Prof. Joo-Young Kim awards the Minister’s Award from MSIT as individual
- 수상 연도 미상 · Prof. Joo-Young Kim’s AISS center awards Minister’s Award from MSIT
- 2021-11-18 · Announcing 2021 Kwon Young-Se Scholarship Award Winners

## 소식

누리집 News 게시판(1–8쪽)의 2021-10-14–2026-02-25 게시 글 58건이다. 수상을 알린 글은 위 「수상」에 있다. 날짜는 게시일이고 제목은 게시된 그대로다.[^news]

- 2026-02-25 · Prof. Joo-Young Kim appointed as a member of Y-KAST
- 2025-08-27 · [TMLR 2025] Geonwoo Ko and Sungyeob Yoo’s paper on SuFP: Piecewise Bit Allocation Floating-Point for Robust Neural Network Quantization is accepted
- 2025-08-27 · [A-SSCC 2025] Jieon Yoon and Sungwoong Yune’s paper on MoDiff: a 11.0 TOPS/W Diffusion Accelerator with Temporal Data Reuse for Real-Time Text-to-Motion Generation is accepted
- 2025-08-27 · [A-SSCC 2025] Hangyeol Kim’s paper on An Efficient FPGA Accelerator with Spatiotemporal Tubelet Merging for Video Transformers is accepted
- 2025-08-27 · [MICRO 2025] In-Jun Jung’s paper on HLX: A Unified Pipelined Architecture for Optimized Performance of Hybrid Transformer-Mamba Language Models is accepted
- 2025-06-04 · [ESSERC 2025] Donghyuk Kim and In-Jun Jung’s paper on D3TA: 38.9TOPS/W Transformer Accelerator with Dual-Port 3T-eDRAM Digital Compute-In-Memory Using HyperAttention and Triple-Sparsity-Handling is accepted
- 2025-06-04 · [TC 2025] Wontak Han’s paper on SAL-PIM: A Subarray-level Processing-in-Memory Architecture with LUT-based Linear Interpolation for Transformer-based Text Generation is accepted
- 2025-04-02 · [VLSI 2025] Jung-Hoon Kim’s paper on Adelia: A 4nm LLM Accelerator with Streamlined Dataflow and Dual-Mode Parallelization for Efficient Generative AI Inference is accepted
- 2025-03-24 · [ISCA 2025] Seungjae Moon and Junseo Cha’s paper on Hybe: GPU-NPU Hybrid System for Efficient LLM Inference with Million-Token Context Window is accepted
- 2025-03-24 · [ISCA 2025] Sungmin Hong’s paper on Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization is accepted
- 2025-03-24 · [ISCA 2025] Seunghee Han and Soongyu Choi’s paper on Improving Sequence Length Limitation in Protein Structure Prediction Model via Adaptive Activation Quantization is accepted
- 2025-03-24 · [ISPASS 2025] Junsoo Kim’s paper on ADOR: A Design Exploration Framework for LLM Serving with Enhanced Latency and Throughput is accepted
- 2025-02-18 · [DAC 2025] Sungwoong Yune’s paper on ABC-FHE: A Resource-Efficient Accelerator Enabling Bootstrappable Parameters for Client-Side Fully Homomorphic Encryption is accepted
- 2024-12-11 · [AAAI 2025] Yi Chen’s paper on AoP-SAM: Automation of Prompts for Efficient Segmentation is accepted
- 2024-12-10 · [JSSC 2025] Sukbin Lim’s paper on Hawkeye: A Point Cloud Neural Network Processor with Virtual Pillar and Quadtree-based Workload Management for Real-Time Outdoor BEV Detection is accepted
- 2024-12-10 · [HPCA 2025] Jaehoon Heo’s paper on EXION: Exploiting Inter- and Intra-Iteration Output Sparsity for Diffusion Models is accepted
- 2024-11-05 · [TETC 2024] Donghyuk Kim’s paper on Darwin: A DRAM-based Multi-level Processing-in-Memory Architecture for Column-Oriented Database is accepted
- 2024-10-11 · [ISSCC 2025] Jaehoon Heo’s paper on HuMoniX: A 57.3 fps 12.8 TFLOPS/W Text-to-Motion Processor with Inter-Iteration Output Sparsity and Inter-Frame Joint Similarity is accepted
- 2024-07-19 · [MICRO 2024] Seungjae Yoo and Hangyeol Kim’s paper on AdapTiV: Sign-Similarity based Image-Adaptive Token Merging for Vision Transformer Acceleration is accepted
- 2024-07-10 · [IEEE Micro 2024] Seungjae Moon’s paper on LPU: A Latency-Optimized Highly Scalable Processor for Large Language Model Inference is accepted
- 2024-07-10 · [ICCAD 2024] Hyunjun Cho’s paper on APINT: A Full-Stack Framework for Acceleration of Privacy-Preserving Inference of Transformers based on Garbled Circuits is accepted
- 2024-05-27 · [ESSERC 2024] Sungyeob Yoo’s paper on A 28nm 4.96 TOPS/W End-to-End Diffusion Accelerator with Reconfigurable Hyper-Precision and Unified Non-Matrix Processing Engine is accepted
- 2024-05-27 · [ESSERC 2024] Donghyuk Kim’s paper on DPIM: A 19.36TOPS/W 2T1C eDRAM Transformer-in-Memory Chip with Sparsity-Aware Quantization and Heterogeneous Dense-Sparse Core is accepted
- 2024-05-09 · [HotChips 2024] Sungyeob Yoo’s paper on Picasso: An Area/Energy-Efficient End-to-End Diffusion Accelerator with Hyper-Precision Data Type is accepted
- 2024-04-15 · [ISCA 2024] Seunghee Han and Seungjae Moon’s paper on BLESS: Bandwidth and Locality Enhanced SMEM Seeding Acceleration for DNA Sequencing is accepted
- 2024-02-19 · [JSSC 2024] Jaehoon Heo and Junghoon Kim’s paper on SP-PIM: A Super-Pipelined Processing-In-Memory Accelerator with Local Error Prediction for Area/Energy-Efficient On-Device Learning is accepted
- 2024-01-13 · [IEEE Custom Integrated Circuits Conference (CICC), 2024] Sukbin Lim’s paper on A 38.5TOPS/W Point Cloud Neural Network Processor with Virtual Pillar and Quadtree-based Workload Management for Real-Time Outdoor BEV Detection is accepted
- 2024-01-13 · [IEEE Journal of Solid-State Circuits (JSSC), 2024] Junsoo Kim’s paper on EPU: An Energy-Efficient Explainable AI Accelerator with Sparsity-free Computation and Heat Map Compression/Pruning is accepted
- 2024-01-13 · [IEEE Access 2024] Ji-Hoon Kim’s paper on Trinity: In-Database Near-data Machine Learning Acceleration Platform for Advanced Data Analytics is accepted
- 2023-10-25 · [IEEE International Symposium on High-Performance Computer Architecture 2024] Prasetiyo’s paper on Throughput-Maximized TFHE-based Accelerator is accepted
- 2023-09-11 · [Asia and South Pacific Design Automation Conference 2024] Jinho Yang’s paper on FPGA-based Embedded Vision Platform is accepted
- 2023-07-26 · [IEEE/ACM International Symposium on Microarchitecture 2023] Adiwena Putra’s paper on Homomorphic Encryption is accepted
- 2023-07-21 · [IEEE/ACM International Conference on Computer-Aided Design 2023] Jaehoon Heo’s paper on Processing-in-DRAM Emulation Framework is accepted
- 2023-06-27 · [Communications of the ACM 2023] Ji-Hoon Kim’s paper on AI Semiconductor Inductry is accepted
- 2023-06-07 · [ESSCIRC 2023] Je Yang’s paper on Joint-DNN Training Processor is accepted
- 2023-05-18 · [Hotchips 2023] Seungjae Moon’s paper on Accelerating Hyperscale Models for Generative AI is accepted
- 2023-04-03 · [VLSI 2023] Junghoon Kim and Jaehoon Heo’s paper on Super-Pipelined Processing-In-Memory Accelerator is accepted
- 2023-03-27 · Professor Joo-Young Kim has been promoted to Associate Professor and has become a distinguished lecturer for the Solid-State Circuits Society (SSCS).
- 2023-03-15 · [TCAS-I 2023] Donghyuk Kim’s paper on Framework for CNN Accelerator is accepted
- 2023-01-19 · [Spring 2023] Welcome New Faces!
- 2023-01-16 · [CICC 2023] Junsoo Kim’s paper on Explainable AI Processor is accepted
- 2022-10-27 · [JSSC 2022] Jaehoon Heo’s paper on On-device training PIM is accepted
- 2022-10-27 · [HPCA 2023] Sungyeob Yoo’s paper on AI-enabled High-Frequency Trading System is accepted
- 2022-10-27 · [FPT 2022] Yang Je’s paper on Real-Time sparse MARL accelerator is accepted
- 2022-10-26 · [TCAS-I 2022] Prasetiyo’s paper on DNN NTT accelerator is accepted
- 2022-08-19 · [A-SSCC 2022] Junghoon KIM’s paper on Mixed-precision Vector Processor is accepted
- 2022-08-19 · [Fall 2022] Welcome New Faces!
- 2022-08-05 · Prof. Joo-Young Kim and his students publish the book “Processing-in-Memory for AI: From Circuits to Systems”
- 2022-07-20 · [MICRO 2022] Seongmin Hong’s paper on DFX is accepted
- 2022-07-20 · [Hotchips 2022] 3 papers from Ji-Hoon Kim, Seongmin Hong, and Sungyeob Yoo are accepted
- 2022-07-13 · [FPL 2022] Yashael’s paper on FSHMEM is accepted
- 2022-04-25 · [JETCAS 2022] Wontak Han’s paper on PIM with Triple Computational Path and Sparsity Handling is accepted
- 2022-04-07 · [FCCM 2022] 2 papers from Yeo-Reum Park and Gyeongcheol-Shin are accepted
- 2022-03-22 · [JETCAS 2022] Donghyuk Kim’s paper on overview of PIM for AI and ML is accepted
- 2022-02-28 · [TC 2022] Jihoon Kim’s paper on Computational Storage Platform is accepted
- 2022-01-14 · [Spring 2022] Welcome New Faces!
- 2022-01-10 · [CICC 2022] Jaehoon Heo’s paper on T-PIM is accepted
- 2021-10-14 · [ACSMD Workshop 2021] Sungyeob Yoo and Junghoon Kim’s paper on A Heterogeneous Vector-Array Architecture is accepted

## 연락과 위치

- 연구실: (34141) 대전광역시 유성구 대학로 291 KAIST 전기및전자공학부동(E3-2) 4209호[^about]
- 교수 연구실: E3-2동 4202호, 전화 042-350-7461[^prof][^eelist]
- 교수 이메일: jooyoung1203@kaist.ac.kr[^prof]
- 연구실 이메일: castlab@kaist.ac.kr[^home]
- 연구실은 석사·박사과정(KAIST 입학 일정에 맞춰 교수에게 이력서와 성적표를 보냄), 박사후연구원, 학부 연구(URP·개별연구)와 방학 인턴을 모집한다고 안내한다.[^about]
[^p1]: S. Hong 외, J.-Y. Kim, 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO), 616-630 (2022). <https://doi.org/10.1109/micro56248.2022.00051> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: S. Moon 외, J.-Y. Kim, IEEE Micro 44, 17-33 (2024). <https://doi.org/10.1109/mm.2024.3420728> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Heo 외, J.-Y. Kim, IEEE Journal of Solid-State Circuits 59, 2671-2683 (2024). <https://doi.org/10.1109/jssc.2024.3369326> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: W. Han, H. Cho, D. Kim, J.-Y. Kim, IEEE Transactions on Computers 74, 2909-2922 (2025). <https://doi.org/10.1109/tc.2025.3576935> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Heo 외, J.-Y. Kim, IEEE Journal of Solid-State Circuits 61, 3085-3097 (2026). <https://doi.org/10.1109/jssc.2025.3631087> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: A. Putra 외, J.-Y. Kim, 56th Annual IEEE/ACM International Symposium on Microarchitecture, 1319-1331 (온라인 2023-12-08). <https://doi.org/10.1145/3613424.3614264> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: S. Yoo, H. Kim, J.-Y. Kim, 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO), 64-77 (2024). <https://doi.org/10.1109/micro61859.2024.00015> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: S. Han, S. Choi, J.-Y. Kim, Proceedings of the 52nd Annual International Symposium on Computer Architecture, 1940-1955 (온라인 2025-06-20). <https://doi.org/10.1145/3695053.3731006> 초록 기준(Semantic Scholar 등록 초록).
[^home]: CAST Lab 누리집 첫 화면 <https://castlab.kaist.ac.kr/> (연구실 소개, Latest Publications, Selected Paper, Research Partners, 2026-10-22 열람)
[^about]: CAST Lab 누리집 About Us <https://castlab.kaist.ac.kr/about-us/> (2026-10-22 열람)
[^research]: CAST Lab 누리집 Research 페이지 ASIC·Architecture·FPGA <https://castlab.kaist.ac.kr/research-main/research-area/>, <https://castlab.kaist.ac.kr/research-main/research-area-architecture/>, <https://castlab.kaist.ac.kr/research-main/research-area-fpga/> (2026-10-22 열람)
[^chips]: CAST Lab 누리집 Chip Gallery <https://castlab.kaist.ac.kr/chip-gallery/> (2026-10-22 열람)
[^prof]: CAST Lab 누리집 Professor 페이지 <https://castlab.kaist.ac.kr/professor/> (Biography, Education, Employment, Honors, 2026-10-22 열람)
[^eelist]: KAIST 전기및전자공학부 교수진 목록 <https://ee.kaist.ac.kr/professor-s1/> (김주영 항목, 2026-10-22 열람)
[^sselist]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^patents]: CAST Lab 누리집 Patents 페이지 <https://castlab.kaist.ac.kr/patents/> (2026-10-22 열람)
[^students]: CAST Lab 누리집 Students 페이지 <https://castlab.kaist.ac.kr/students/> (2026-10-22 열람)
[^alumni]: CAST Lab 누리집 Alumni 페이지 <https://castlab.kaist.ac.kr/students-alumni/> (2026-10-22 열람)
[^pubs]: CAST Lab 누리집 Publications 메뉴: Journal <https://castlab.kaist.ac.kr/journal-papers/>, Conference <https://castlab.kaist.ac.kr/paper/>, Books <https://castlab.kaist.ac.kr/books/>와 누리집의 논문 공개 목록 (목록 범위는 근거 페이지, 2026-10-22 열람)
[^crossref]: 학회 논문의 출판사 등록 서지(Crossref) <https://api.crossref.org/> (2026-10-22 조회)
[^news]: CAST Lab 누리집 News 게시판 1–8쪽 <https://castlab.kaist.ac.kr/news/> (2026-10-22 열람)
[^awards]: CAST Lab 누리집 Awards 페이지와 글 10건 <https://castlab.kaist.ac.kr/award/> (2026-10-22 열람)

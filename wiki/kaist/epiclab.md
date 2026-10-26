# EPIC Lab (Embedded Processor & Intelligent Computing Lab)

**KAIST 전기및전자공학부·AI시스템학과 · 이영주 교수**

- 분야: VLSI 신호처리, 디지털 시스템 온 칩 설계, 응용 특화 프로세서, 알고리즘–하드웨어 공동 설계
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 집적회로 설계[^home][^eeprof], AI 반도체·가속기[^home][^research][^p1], 오류 정정 부호[^research][^p4][^p5], 무선·이동통신[^home][^research][^p3], 메모리 내 연산[^project][^p6], 대형 언어 모델[^p2], 컴퓨터 구조·운영체제[^home][^research][^project], 모델 경량화·양자화[^p2]
- 홈페이지: <https://sites.google.com/view/epiclab>
- 근거와 출처: [EPIC Lab 근거 페이지](epiclab-sources.md)

> 기계학습 모델, 차세대 통신, 사람 중심의 사물인터넷 기기처럼 특정 응용에 맞춘 임베디드 프로세서를 알고리즘, 컴퓨터 구조, 시스템 온 칩 설계까지 함께 다뤄, 에너지 효율이 높은 하드웨어·소프트웨어 구성 요소를 만드는 연구실이다.[^home]

## 무엇을 연구하나

누리집 첫 화면은 EPIC Lab을 KAIST 전기및전자공학부와 AI시스템학과에 함께 속한 연구 그룹으로 소개한다. 연구실은 응용 특화 임베디드 프로세서(특정 기기 안에 들어가 정해진 일을 맡는 프로세서)를 위한 효율적인 하드웨어·소프트웨어 구성 요소를 만들며, 새로 등장하는 여러 계산 작업에서 지능형 계산에 초점을 둔다.[^home] 연구는 알고리즘, 컴퓨터 구조, 시스템 온 칩(SoC, 여러 기능의 회로를 칩 하나에 모은 것) 설계에 걸쳐 있고, 지금은 압축한 기계학습 모델을 위한 에너지 효율 높은 프로세서, 차세대 통신 시스템을 위한 고성능 기저대역 프로세서(통신 신호를 부호화·복호화하고 처리하는 칩), 사람 중심 응용을 위한 새로운 사물인터넷(IoT) 플랫폼에 집중한다고 적는다.[^home] 전기및전자공학부 교수 소개는 주요 연구를 VLSI 신호처리(신호처리 알고리즘을 대규모 집적회로로 구현하는 일), 디지털 시스템 온 칩 설계, 응용 특화 프로세서, 알고리즘–하드웨어 공동 설계 방법론으로 적는다.[^eeprof]

Research 페이지는 연구 주제로 임베디드 프로세서 구조, 시스템 온 칩 설계, VLSI 신호처리, 심층 신경망, 통신 알고리즘을 들고, 목표 응용으로 에너지 효율 높은 기계학습 처리용 가속기 구조, 고급 오류 정정 부호(전송·저장 중 생긴 오류를 고칠 수 있게 덧붙이는 부호)를 위한 SoC 설계, 대규모 MIMO(안테나 여러 개로 여러 신호를 동시에 주고받는 기술) 처리의 하드웨어·소프트웨어 공동 최적화, 양자내성암호(PQC)·완전 동형 암호(FHE)·프라이버시 보호 기계학습(PPML)을 위한 VLSI 해법, 의공학을 위한 응용 특화 컴퓨터 시스템을 든다.[^research]

진행 중인 과제는 이 방향을 그대로 보여 준다. 통신 세대 진화를 위한 채널 부호 부복호와 채널 추정 기술을 다루는 네트워크 전문연구실(2024년 4월–2031년 12월), 점진적으로 적응하는 온디바이스 AI 학습 플랫폼(2026년 4월–2029년 12월), 대규모 언어모델에 특화한 다중 비트 저항변화메모리 기반 PIM 칩(2025년 4월–2028년 12월), 지능형 보안 수중 통신 특화연구실(2022년 12월–2028년 12월), SSD를 위한 초고속 오류정정 솔루션(2025년 9월–2028년 9월), NPU(신경망 계산 전용 처리 장치)를 긴밀하게 붙인 맞춤형 다중 코어 RISC-V 프로세서(2025년 5월–2028년 4월) 등 12건이 진행 중으로 적혀 있다.[^project]

연구실은 2025년 2월 KAIST 전기및전자공학부로 옮겨 왔다고 소식에 적었다.[^news] 대표 논문은 그 뒤에 게재가 결정되고 출판된 여덟 편으로, 다섯 갈래로 나뉜다. 기계학습 가속기와 대형 언어 모델 경량화(대표 논문 1, 2),[^p1][^p2] 차세대 통신의 채널 추정 가속기(대표 논문 3),[^p3] 오류 정정 부호 복호기(대표 논문 4, 5),[^p4][^p5] 메모리 내 연산 구조(대표 논문 6),[^p6] 비선형 함수 연산 하드웨어와 스타일러스 펜 입력 처리(대표 논문 7, 8)다.[^p7][^p8]

## 주요 연구 주제

### 1. 기계학습 가속기와 모델 경량화

상태 공간 모델(입력을 차례로 받으며 내부 상태를 갱신해 계산하는 시퀀스 모델)을 위한 LUT(미리 계산한 값을 표로 저장해 두고 찾아 쓰는 방식) 기반 가속기 칩을 만들었고,[^p1] 대형 언어 모델이 쓰는 KV 캐시(앞서 처리한 토큰의 키·값을 저장해 두는 메모리)를 키와 값의 성질에 맞춰 다르게 줄이는 압축 방법을 내놓았다.[^p2] 딥러닝에 쓰는 비선형 함수를 구간별 선형 근사로 적은 비용에 계산하는 하드웨어 설계 틀도 만들었다.[^p7] 2025–2026년 논문 목록에는 혼합 정밀도 양자화(층마다 다른 비트 수로 값을 줄여 표현하는 방법)로 대형 언어 모델을 압축하는 IterQuant, 칩 안 네트워크를 고려한 혼합 정밀도 양자화 NMIX, 긴 문맥 추론을 위한 검색 유도 추측 디코딩 ReSpec(발표 승인), 시각·언어·행동 모델을 학습 뒤에 양자화하는 CHASE-VLA(발표 승인), FPGA(회로 구성을 나중에 바꿔 쓸 수 있는 칩) 기반 실시간 영상 신호 처리 가속기도 있다.[^pubs] 대표 논문 1, 2, 7.

### 2. 차세대 통신의 기저대역 처리

B5G/6G(5세대 이후·6세대 이동통신)를 위한 AI-RAN 채널 추정 가속기를 알고리즘과 하드웨어를 함께 최적화해 만들었다.[^p3] 2026년 논문 목록에는 혼합 정밀도 SIMD(명령 하나로 여러 데이터를 함께 처리하는 방식) 가속을 쓴 저지연 소프트웨어 5G NR 수신기와 6G 상위 중대역(FR3) 기지국의 전력 모형도 있다.[^pubs] 진행 중인 과제로 초고효율 기계학습 기저대역 시스템 개발이 적혀 있다.[^project] 대표 논문 3.

### 3. 오류 정정 부호 복호기

저장 장치용 고부호율 비이진 LDPC 부호(여러 비트를 묶은 기호 단위로 오류를 고치는 부호)의 메모리 요구를 줄인 열 단위 계층 복호기와,[^p4] 초고신뢰·저지연 통신(URLLC)에서 짧은 BCH 부호를 순서 통계 복호(OSD, 받은 신호의 신뢰도 순서를 이용해 후보 부호어를 찾는 복호 방법)로 푸는 계산을 줄인 하이브리드 복호 알고리즘과 복호기를 만들었다.[^p4][^p5] 2025–2026년 논문 목록에는 5G NR용 메모리 효율 LDPC 복호기, 짧은 길이의 PAC 폴라 부호 복호기의 하드웨어 효율 분석도 있다.[^pubs] 대표 논문 4, 5.

### 4. 메모리 내 연산

비휘발성 메모리 배열에서 계산하는 메모리 내 연산(PIM) 구조의 비선형성 때문에 생기는 오류를, 신경망 가중치를 고치지 않고 입력의 희소성(값이 0인 입력이 많은 성질)을 이용해 바로잡는 보상 방법과 구조를 내놓았다.[^p6] 2025–2026년 논문 목록에는 ECRAM(이온 이동으로 저항을 바꾸는 메모리 소자) 기반 아날로그 PIM의 보존 특성 보상 연구와, 같은 소자를 쓴 학습 시스템 논문(게재 승인)도 있다.[^pubs] 대표 논문 6.

### 5. 사람 중심 기기와 IoT

전자기 공명(EMR) 방식 스타일러스 펜 신호에서 좌표를 정확히 추정하는 가벼운 딥러닝 틀을 만들었다.[^p8] 2025–2026년 논문 목록에는 수동형 스타일러스 펜의 기울기·방위각 추정, 스스로 개인에 맞추는 이상 탐지기를 쓴 가벼운 심전도(ECG) 분류 시스템, 측정 깔창과 심층 신경망으로 노인의 병적 보행을 가려내는 연구도 있다.[^pubs] 대표 논문 8.

### 6. 프라이버시 보호 계산을 위한 암호 가속기

Research 페이지는 양자내성암호·완전 동형 암호·프라이버시 보호 기계학습을 위한 VLSI 해법을 목표 응용으로 든다.[^research] 2025–2026년 논문 목록에는 완전 동형 암호를 위한 유연한 RNS-CKKS 프로세서와, 동형 암호 계산의 핵심 연산인 수론 변환(NTT) 가속기에서 메모리를 아끼는 회전 인자 생성기가 있다.[^pubs]

## 대표 논문

연구실이 KAIST로 옮겨 온 2025년 2월 뒤에 게재가 결정되고 출판된 논문 가운데 이영주 교수가 마지막 저자이자 교신저자(\*)인 논문을, 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [LUT-SSM: A 99.3TFLOPS/W LUT-Based State-Space Model Accelerator Using Energy-Efficient Element-Wise Layer Fusion and LUT-Friendly Weight-Only Quantization](https://doi.org/10.1109/isscc49663.2026.11409105) · IEEE International Solid-State Circuits Conference (ISSCC) | 상태 공간 모델(SSM)과 가중치만 양자화하는 방법은 정확도를 조금만 잃으면서 외부 메모리 접근을 크게 줄인다. 둘을 함께 효율적으로 지원하려고, 다대다(many-to-many) LUT 누산기(LUT-ACC)와 원소별(EW) 층 융합을 갖춘 LUT 기반 SSM 가속기 LUT-SSM을 내놓았다. 정수와 부동소수점을 섞은 행렬 곱(INT-FP GEMM)과 SSM 블록 안의 순차적인 원소별 연산을 효율적으로 처리한다. 28nm FD-SOI 공정으로 만든 칩은 최고 효율 99.3 TFLOPS/W, Mamba 1.4B 모델에서 96.1 TFLOPS/W를 얻어 최근 설계보다 에너지 효율을 1.28배 높였다.[^p1] | 1저자 Sunwoo Yoo, 마지막·교신 저자 이영주 (6명) |
| 2 | 2026 | [Asymmetric KV Cache Compression Using State-Aware Sparsity and Quantization](https://doi.org/10.1109/tcasai.2026.3670075) · IEEE Transactions on Circuits and Systems for Artificial Intelligence | 대형 언어 모델(LLM)을 자원이 적은 기기에서 돌리려고 KV 캐시를 양자화나 희소성(일부 값을 버려 0으로 두는 방식)으로 압축하는 연구가 있었지만, 키와 값 상태의 구조 차이와 두 압축 방식의 상호작용을 놓쳐 정확도와 메모리 효율 모두에 한계가 있었다. 요청마다 생성되는 토큰 길이가 달라 성능이 일정하지 않은 문제도 있었다. 이 연구는 키와 값 상태마다 양자화 단위, 희소성 압축의 종류와 정도를 다르게 맞추는 비대칭·상태 인지 KV 캐시 압축 파이프라인을 내놓았다. 압축 연산의 순서에 따라 정확도 저하와 KV 캐시 사용량이 달라진다는 점을 보였고, 회전 위치 임베딩(RoPE)을 적용하기 전에 채널별 영향을 평가해 채널을 구조적으로 잘라 내는 기준을 새로 정했다. 디코딩 때 추가 계산과 메모리 부담이 생기지 않게 했다. 실험에서 양자화를 쓰든 쓰지 않든 정확도와 메모리 사이의 균형이 기존보다 좋았고, 시퀀스 길이에 관계없이 메모리를 고르게 줄였다.[^p2] | 1저자 Myeongji Yun, 마지막·교신 저자 이영주 (4명) |
| 3 | 2026 | [UniC-Vision: A 14.4Gb/s 7.3pJ/b Universal Vision Transformer OFDM Channel Estimation Accelerator for B5G/6G AI-RAN](https://doi.org/10.1109/isscc49663.2026.11409283) · IEEE International Solid-State Circuits Conference (ISSCC) | 차세대 통신을 위한 AI-RAN 채널 추정(전파가 지나온 경로의 영향을 추정해 받은 신호를 바로잡는 일) 가속기다. 매우 높은 신뢰성, 낮은 지연, 모든 주파수 범위를 지원해 B5G/6G 요구를 맞추려 했다. 알고리즘과 하드웨어를 함께 최적화하고 구조를 최적화해, 28nm CMOS 공정 시제품이 비트당 7.3 pJ의 에너지로 14.4 Gb/s를 처리했다. 최신 채널 추정 시스템보다 신뢰성은 7.7–18.9 dB, 처리량은 16–39배 높였다.[^p3] | 1저자 Sangbu Yun, 마지막·교신 저자 이영주 (6명) |
| 4 | 2026 | [A 3.3 Gb/s/mm² Area-Efficient Non-Binary LDPC Decoder Using Column-Layered Processing](https://doi.org/10.1109/tcsi.2025.3632901) · IEEE Transactions on Circuits and Systems I: Regular Papers | 비이진 LDPC(NB-LDPC) 부호는 이진 부호보다 오류 정정 성능이 좋지만, 기존 복호기는 차수가 높은 갈루아 체(부호 계산에 쓰는 유한한 수 체계)와 긴 부호어를 지원할 때 처리가 복잡하고 메모리가 많이 들었다. 이 복호기는 트렐리스 최소-최대 알고리즘과 열 단위 계층 복호 순서를 쓰고 메시지를 그때그때 계산해 메모리 요구를 줄였다. 열 사이에 최신 정보를 나눠 기본 설계보다 빨리 수렴한다. 고부호율 부호의 구조에 맞춰 여러 열을 함께 처리하고 메모리를 뱅크로 나눴으며, 하위 모듈을 최적화해 병렬 처리 부담을 줄였다. 28nm CMOS 공정으로 만든 4KB·부호율 0.9 시제품 복호기는 최신 설계보다 면적 효율이 1.42배 높았다. 저장 장치 요구를 바탕으로 설계했지만 무선·광통신 같은 다른 분야에도 맞출 수 있다.[^p4] | 1저자 Jeongwon Choe, 마지막·교신 저자 이영주 (2명) |
| 5 | 2025 | [Hybrid Ordered Statistics Decoding of Short-Length BCH Codes for URLLC Systems: Theoretical Analysis and Decoder Implementation](https://doi.org/10.1109/tcsi.2025.3570034) · IEEE Transactions on Circuits and Systems I: Regular Papers | 순서 통계 복호(OSD)는 짧은 선형 블록 부호에서 최대 우도 복호(가장 그럴듯한 부호어를 고르는 복호)에 가까운 성능을 내 URLLC에서 주목받지만 계산이 많다. 이 연구는 경판정 대수 복호의 결과를 활용해 연판정 OSD 연산을 필요할 때만 켜는 하이브리드 OSD 알고리즘으로 계산을 크게 줄였다. 오류 정정 특성을 분석해, 이 알고리즘이 기본 OSD보다 오류 정정 성능이 좋음이 보장되는 이론 조건을 끌어냈다. 경판정과 연판정 연산을 묶은 복호기 구조도 내놓았다. (127, 64) BCH 부호에서 28nm 공정 시제품 복호기는 목표 블록 오류율 10⁻⁵에서 평균 처리 지연 773 ns를 보였고, 이전 OSD 하드웨어보다 정보 처리량을 4.2배, 에너지 효율을 35배 높이면서 부호 이득도 얻었다.[^p5] | 1저자 Jaehee Kim, 마지막·교신 저자 이영주 (7명) |
| 6 | 2025 | [Cost-efficient Processing-in-Memory Architecture with Training-free and Universal Error Compensation](https://doi.org/10.1109/islped65674.2025.11261781) · IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) | 메모리 중심의 심층 신경망(DNN) 계산은 에너지 효율이 좋지만, 기존 메모리 내 연산(PIM) 구조가 가진 비선형성 때문에 정확도가 크게 떨어져 벡터-행렬 곱셈 결과를 바로잡을 방법이 필요하다. 이 연구는 DNN 가중치를 고치지 않고, 미리 모은 오류와 입력의 특성을 써서 비휘발성 메모리(NVM) 배열의 열 방향으로 쌓인 오류를 동적으로 바로잡는 입력 희소성 기반 오류 보상 방법을 내놓았다. 기존 아날로그-디지털 변환기(ADC)를 조금 고치거나 NVM 배열에 행 몇 개를 더해 이 보상 방식을 넣은 PIM 구조도 제시했다. 실험에서 여러 신소자 메모리 셀의 비선형 효과를 줄여, 하드웨어 부담이 무시할 만한 수준에서 이상적인 경우에 가까운 DNN 정확도를 얻었다.[^p6] | 1저자 Myeongji Yun, 마지막·교신 저자 이영주 (7명) |
| 7 | 2026 | [CL-PLAC: A Generalized Design Framework for Nonlinear Functions Using Comparator-Less Piecewise Linear Approximate Computation](https://doi.org/10.1109/tcasai.2026.3674441) · IEEE Transactions on Circuits and Systems for Artificial Intelligence | 비선형 함수를 칩에서 적은 비용으로 계산하는 비교기 없는 구간별 선형 근사 계산(CL-PLAC) 방법이다. 기존 구간별 선형 근사(PLAC)는 비교기로 구간을 찾는 부담이 컸는데, CL-PLAC는 이를 LUT 기반 다단계 방식으로 바꿔 넓은 정밀도 범위를 지원한다. 하드웨어 비용을 고려해 구간과 섹터 길이를 함께 최적화하는 섹터별 균일 분할 알고리즘을 만들고, 시프트 연산으로 계수를 계산하고 LUT를 병렬로 찾는 전용 하드웨어를 설계했다. 같은 정밀도에서 최신 PLAC 설계보다 면적-시간 복잡도(ATC)를 최대 70.2%, 에너지 소모를 최대 79.3% 줄였고, 확산 기반 생성 모델과 대형 언어 모델에서는 ATC를 65.4%, 에너지를 75.4% 줄였다.[^p7] | 1저자 Jin Hyun, 마지막·교신 저자 이영주 (3명) |
| 8 | 2026 | [StylusNet: ML-Based Coordinate Extractor for EMR Stylus Touch Devices](https://doi.org/10.1109/jsen.2026.3684492) · IEEE Sensors Journal | 전자기 공명(EMR) 방식 스타일러스 펜의 기존 신호 처리는 펜의 기울기·방위각 변화와 하드웨어 인터페이스 때문에 좌표가 한쪽으로 치우치고 직선이 휘는 문제가 있었다. StylusNet은 EMR 펜 신호에서 좌표를 정확히 추정하는 가벼운 딥러닝 틀로, 자동 이득 조절(AGC)로 신호를 다듬는 전처리와 거친 좌표를 정밀한 좌표로 다듬는 2단계 신경망 예측기를 묶었다. 직선을 그었을 때의 휘어짐과 벗어남을 재는 평가 기준도 새로 내놓았다. 실제 EMR 데이터셋 세 개에서 이전 방법보다 평균 좌표 오차를 최대 87.8% 줄였고, 여러 기울기·방위각·환경 조건에서 직선성을 높였으며, 임베디드 시스템에서 실시간으로 추론했다.[^p8] | 1저자 Eunbin Park, 마지막·교신 저자 이영주 (4명) |

## 교수와 전문 분야

이영주 교수는 KAIST 전기및전자공학부 부교수이고 Circuit 디비전에 속하며, 겸임학과는 AI시스템학과다.[^eeprof][^eelist] 학위는 KAIST 박사(2014)로 적혀 있다.[^eeprof] 전기및전자공학부 교수 소개의 주요 연구분야는 AI & Machine Learning, Multimedia Signal Processing, Information, Communication & Coding, Computer Architecture, Software Systems & Networking, Integrated Circuits & Semiconductor Systems이고, 반도체시스템공학과 교수진에는 연구분야 「반도체 시스템 및 집적회로」로 올라 있다.[^eeprof][^ssep]

연구실 소식에 따르면 EPIC Lab은 2020년 1월 이영주 교수가 다시 세웠고, 2025년 2월 KAIST 전기및전자공학부로 옮겨 왔다.[^news] 옮기기 전의 소식에는 구성원이 POSTECH 전자전기공학과(POSTECH EE)의 학위 논문상과 펠로십, Samsung-POSTECH 연구센터의 상을 받은 일이 적혀 있다.[^news] 2026년 3월에는 교수가 KAIST 전기및전자공학부 우수강의상(Outstanding Lecture Award)을 받았다.[^news] Research 페이지의 수상 목록은 교수가 학생이던 시절의 수상도 적는다. 박인철 교수의 지도를 받으며 대한민국 반도체 설계대전 Bronze Medal(2008)과 Special Award(2011)를 받았고, 공동 저자로 ISOCC Best Design Award(2011), Qualcomm Korea Innovation Contest Innovation Award(2013), ISOCC Best Demo Award(2013)를 받았다.[^research]

전기및전자공학부 교수 소개가 대표업적으로 드는 여섯 편은 2024–2025년의 FP-INT 행렬 곱 가속기(FIGLUT, HPCA 2025), 비대칭 양자화와 비트 단위 희소성을 쓴 DNN 가속기(Panacea, HPCA 2025), 완전 동형 암호용 RNS-CKKS 프로세서(IEEE JSSC 2025), 지능형 반사 표면 제어 SoC(IEEE TCAS-I 2024), 대형 생성 언어 모델을 위한 LUT 기반 양자화 행렬 곱(LUT-GEMM, ICLR 2024), 5G/6G URLLC용 BOSS FEC 복호기(ISSCC 2024)다.[^eeprof] 이 논문들은 연구실이 KAIST로 옮기기 전에 게재가 결정되었다.[^news] Publication 페이지는 KAIST, POSTECH을 비롯한 국내외 대학·기관의 공동연구자 21명을 적는다.[^publication]

논문으로 보면 KAIST에서의 전문 분야는 다섯 갈래다. 기계학습 가속기와 모델 경량화(대표 논문 1, 2, 7),[^p1][^p2][^p7] 차세대 통신의 채널 추정 가속기(대표 논문 3),[^p3] 오류 정정 부호 복호기(대표 논문 4, 5),[^p4][^p5] 메모리 내 연산(대표 논문 6),[^p6] 사람 중심 기기의 입력 처리(대표 논문 8)다.[^p8]

## 응용 분야

대표 논문은 Mamba 1.4B 같은 상태 공간 모델의 추론 가속(대표 논문 1), 자원이 적은 기기에서의 대형 언어 모델 실행(대표 논문 2), 확산 기반 생성 모델과 대형 언어 모델의 비선형 함수 계산(대표 논문 7)을 다룬다.[^p1][^p2][^p7] 통신 쪽에서는 B5G/6G AI-RAN의 채널 추정(대표 논문 3)과 URLLC 시스템의 짧은 부호 복호(대표 논문 5)를, 저장 장치 쪽에서는 저장 장치 요구에 맞춘 비이진 LDPC 복호기(대표 논문 4)를 겨냥한다.[^p3][^p5][^p4] 대표 논문 8은 스타일러스 펜 입력 기기의 좌표 추정을 다룬다.[^p8] 진행 중인 과제에는 SSD용 오류정정 솔루션, 지능형 보안 수중 통신, 지능형 의료영상 진단 솔루션 연구센터 참여가 있다.[^project]

## 구성원

연구실 누리집 Member 페이지의 박사후연구원 1명, 박사과정 10명, 석사과정 11명이다.[^member] 과정은 페이지의 구역 이름이고, 박사과정 한 명은 학생 대표(Student Representative)로 적혀 있다. "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Jeongwon Choe | 박사후연구원 | 4 |
| Junseo Jo | 박사과정 |  |
| Jung Gyu Min | 박사과정 | 6 |
| Eunbin Park | 박사과정 | 8 |
| Jin Hyun | 박사과정 (Student Representative) | 7 |
| Jaehee Kim | 박사과정 | 5 |
| Gyuhyun Jung | 박사과정 |  |
| Soonhyun Kwon | 박사과정 | 1, 3, 5 |
| Chanhee Lee | 박사과정 | 3 |
| Jiwoo Kim | 박사과정 |  |
| Junehyuk Oh | 박사과정 |  |
| Daeun Seo | 석사과정 | 8 |
| Jaewon Chun | 석사과정 |  |
| Jeonghwan Ahn | 석사과정 |  |
| Yeji Lee | 석사과정 |  |
| Jinwoong Hwang | 석사과정 |  |
| Dasom Jeong | 석사과정 |  |
| Kwanwoo Park | 석사과정 |  |
| Wonyeol Choi | 석사과정 |  |
| Jaeeun Jeong | 석사과정 |  |
| Hyungyo Jeong | 석사과정 |  |
| Jiwon Lee | 석사과정 |  |

Member 페이지는 이 밖에 2024–2026년에 머문 방문 연구자 5명을 따로 적는다. 누리집이 적은 출신 기관은 EPFL(스위스), University of Leeds(영국), Technical University of Munich(독일), Nanjing University(중국), KU Leuven(벨기에)이다.[^member]

## 졸업생과 이전 구성원

누리집 Member 페이지 Alumni 구역의 박사 9명과 석사 14명이다. 학위 칸은 누리집 표기(예: PhD26/MS22)를 네 자리 연도로 옮긴 것이고, 진로는 누리집 표기 그대로다. 학위를 받은 학교는 누리집에 적혀 있지 않으며, 연구실이 2025년 2월 KAIST로 옮겨 오기 전의 졸업생이 섞여 있다.[^member][^news]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sunwoo Yoo | Ph.D. 2026, M.S. 2022 | Senior Engineer at SK Hynix |
| Seungwoo Hong | Ph.D. 2026, M.S. 2021 | Researcher at ETRI |
| Sangbu Yun | Ph.D. 2026 | InnoCORE Postdoc Researcher at KAIST |
| Hyeokjun Kwon | Ph.D. 2025, M.S. 2021 | Assistant Professor at Ajou University |
| Gunho Park | Ph.D. 2024, M.S. 2021 | Research Scientist at a2sys |
| Dongyun Kam | Ph.D. 2024, M.S. 2020 | Assistant Professor at UNIST |
| Younghoon Byun | Ph.D. 2024, M.S. 2020 | Senior Engineer at SAIT, Samsung Electronics |
| Hyunhoon Lee | Ph.D. 2024, M.S. 2020 | Senior Engineer at SAIT, Samsung Electronics |
| Seungsik Moon | Ph.D. 2023, M.S. 2020 | Assistant Professor at Chungbuk National University |
| Myeongjun Lee | M.S. 2026 | Senior Engineer at DRAM Development Division, SK Hynix |
| Seungjun Kim | M.S. 2026 | Engineer at Memory Business, Samsung Electronics |
| Myeongji Yun | M.S. 2025 | Ph.D. Student at University of Michigan |
| Dain Park | M.S. 2025 | Engineer at Memory Business, Samsung Electronics |
| Jungyun Kim | M.S. 2025 | Officer at Republic of Korea Marine Corps |
| Doeun Sim | M.S. 2024 | Engineer at RX Business Promotion Office, Samsung Electronics |
| Sangil Han | M.S. 2024 | Senior Engineer at Memory Business, Samsung Electronics |
| Eunji Yoo | M.S. 2024 | Engineer at SAIT, Samsung Electronics |
| Jiwon Kim | M.S. 2023 | Engineer at Memory Business, Samsung Electronics |
| Hyunsung Kim | M.S. 2022 | Engineer at Rebellions Inc. |
| Changhyeon Kim | M.S. 2022 | Engineer at S.LSI Business, Samsung Electronics |
| Dongyoung Rim | M.S. 2022 | Engineer at S.LSI Business, Samsung Electronics |
| Jongmin Park | M.S. 2021 | Engineer at Krafton |
| Seokha Hwang | M.S. 2019 | Senior Hardware Engineer at FuriosaAI |

## 최근 논문 목록 (2021–2026)

누리집 Journal Papers·Conference Proceedings 페이지의 2021–2026년 연도 구역 논문 118편이다. 국제 학술지 40편, 국내 학술지 2편, 국제 학회 논문 60편, 국내 학회 논문 16편이며, 같은 연구가 학술지와 학회에 함께 실린 경우는 누리집 목록대로 각각 적었다. 국내 학술지·학회 논문은 이름 뒤에 (국내)를 붙였다. 제목·저자·학술지·학회 이름은 누리집 표기 그대로이고, 저자 이름 뒤 \*·+ 표시도 누리집 표기다. 누리집 2026년 구역에서 [Accepted]로 표시한 학술지 2편과 학회 3편은 끝에 「게재 승인」·「발표 승인」을 붙여 출판된 논문과 구분했다. 연구실은 2025년 2월 KAIST로 옮겨 왔으므로, 그 전에 나온 논문은 KAIST로 옮겨 오기 전의 성과다. 교수가 교신저자가 아닌 공동연구 논문도 누리집 목록대로 실었다.[^pubs][^news]

**2026**

- Sangbu Yun, Chanhee Lee, Soonhyun Kwon, Jeongtaek Chang, Zhengya Zhang, and Youngjoo Lee\*. "A 14.4-Gb/s 7.3-pJ/b universal vision transformer OFDM channel estimation processor for B5G/6G communication systems". *IEEE Transactions on Circuits and Systems I: Regular Papers (게재 승인)*.
- Jinho Byun+, Jung Gyu Min+, Seungkun Kim+, Jeonghoon Son, Jaehee Kim, Youngjoo Lee\*, and Seyoung Kim\*. "Retention-resilient ECRAM-PIM training system with device-algorithm-controller co-design". *IEEE Transactions on Circuits and Systems I: Regular Papers. (Invited) (게재 승인)*.
- Jin Hyun+, Seungwoo Hong+, and Youngjoo Lee\*. "CL-PLAC: A generalized design framework for nonlinear functions using comparator-less piecewise linear approximate computation". *IEEE Transactions on Circuits and Systems for Artificial Intelligence, vol. 3, no. 5, pp. 340-353, Oct. 2026*.
- Myeongji Yun, Dongyun Kam, Priyadarshini Panda, and Youngjoo Lee\*. "Asymmetric KV cache compression using state-aware sparsity and quantization". *IEEE Transactions on Circuits and Systems for Artificial Intelligence, vol. 3, no. 4, pp. 246-259, Aug. 2026*.
- Eunbin Park, Daeun Seo, Hyungcheol Sin, and Youngjoo Lee\*. "StylusNet: ML-based coordinate extractor for EMR stylus touch devices". *IEEE Sensors Journal, vol. 26, no. 11, pp. 17385-17397, June 2026*.
- Junseo Jo, Hyungcheol Sin, and Youngjoo Lee\*. "Machine learning assisted tilt/azimuth estimation for passive stylus pens using position-based model selection". *IEEE Access, vol. 14, pp. 69050-69058, May 2026*.
- Jeongwon Choe and Youngjoo Lee\*. "A 3.3 Gb/s/mm^2 area-efficient non-binary LDPC decoder using column-layered processing". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 73, no. 4, pp. 2847-2857, Apr. 2026*.
- Hyowon Lee, Youngmok Park, Jeongwoo Park, Mintaek Oh, Jinseok Choi, Yo-Seb Jeon, Jeonghun Park, Youngjoo Lee, Jemin Lee, and Namyoon Lee\*. "수중 음향 통신을 위한 채널 모델링과 송수신 기법 연구 동향". *The Journal of Korean Institute of Communications and Information Sciences, vol. 51, no. 2, pp. 285-302, Feb. 2026 (국내)*.
- Jin Hyun, Jung Gyu Min, Gyuhyun Jung, and Youngjoo Lee\*. "CHASE-VLA: Post-training quantization framework for vision-language-action models with chunk-aware scale estimation". *Asian Conference on Computer Vision (ACCV), Osaka, Japan, Dec. 2026 (발표 승인)*.
- Jeonghwan Ahn, Soonhyun Kwon, Sangbu Yun, Chanhee Lee, Dongyun Kam, and Youngjoo Lee\*. "ReSpec: Retrieval-guided speculative decoding for long-context LLM inference". *IEEE Asia Pacific Conference on Circuits and Systems (APCCAS), Fukuoka, Japan, Oct. 2026 (발표 승인)*.
- Hwiwon Lee, Jeonghwan Ahn, Siraj Yahyazade, Ando Ki, Youngjoo Lee\*. "Parameterized MAC IP generator for extremely low-precision floating-point arithmetic on FPGAs". *IEEE Asia Pacific Conference on Circuits and Systems (APCCAS), Fukuoka, Japan, Oct. 2026 (발표 승인)*.
- Seungjun Kim, Sangbu Yun, Jeongwon Choe, and Youngjoo Lee\*. "Memory-efficient partially self-corrected min-sum LDPC decoder for 5G NR applications". *IEEE International Symposium on Circuits and Systems (ISCAS), Shanghai, China, May 2026*.
- Gyuhyun Jung+, Hyunhoon Lee+, and Youngjoo Lee\*. "Memory-efficient twiddle factor generator in parallel NTT accelerators for FHE applications". *IEEE International Symposium on Circuits and Systems (ISCAS), Shanghai, China, May 2026*.
- Jaehee Kim+, Chanhee Lee+, Jaewha Kim, Nam-Il Kim, and Youngjoo Lee\*. "Low-latency software-defined 5G NR PUSCH receiver with mixed-precision SIMD acceleration". *IEEE International Symposium on Circuits and Systems (ISCAS), Shanghai, China, May 2026*.
- Emanuele Peschiera, Sangbu Yun, Youngjoo Lee, Liesbet Van der Perre, François Rottenberg\*. "A parametric power model of upper mid-band (FR3) base stations for 6G". *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Barcelona, Spain, May 2026*.
- Hyungyo Jeong, Jiwoo Kim, Hyeokjun Kwon, Jaeho Lee, and Youngjoo Lee\*. "IterQuant: Iterative quantization framework for mixed-precision LLM compression". *IEEE/ACM Design, Automation and Test in Europe (DATE), Verona, Italy, Apr. 2026*.
- Sunwoo Yoo+, Dongyun Kam+, Gunho Park, Soonhyun Kwon, Dongsoo Lee, and Youngjoo Lee\*. "LUT-SSM: A 99.3TFLOPS/W LUT-based state-space model accelerator using energy-efficient element-wise layer fusion and LUT-friendly weight-only quantization". *IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, Feb. 2026*.
- Sangbu Yun, Chanhee Lee, Soonhyun Kwon, Jeongtaek Chang, Zhengya Zhang, and Youngjoo Lee\*. "UniC-Vision: A 14.4Gb/s 7.3pJ/b universal vision transformer OFDM channel estimation accelerator for B5G/6G AI-RAN". *IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, Feb. 2026*.
- Cheng-Hsun Lu, Wei Tang, Jaehee Kim, Youngjoo Lee, and Zhengya Zhang\*. "A 1.1mm^2, 14.4ns, 13.1pJ/b forward error correction with ordered-statistics post processing for ultra-reliable and low-latency communications". *IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, Feb. 2026*.

**2025**

- Xinyi Li+, Eunbin Park+, Myeongjun Lee, Wenjie Fan, Yuxiang Fu, Li Li\*, and Youngjoo Lee\*. "NMIX: NoC-aware mixed precision quantization for energy-efficient ML accelerator". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 72, no. 12, pp. 2002-2006, Dec. 2025*.
- Jaehee Kim, Changhyeon Kim, Sangbu Yun, Dongyun Kam, Soonhyun Kwon, Yongjune Kim, and Youngjoo Lee\*. "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 72, no. 11, pp. 6528-6540, Nov. 2025. (Invited)*.
- Sunwoo Yoo, Seungwoo Hong, Dongyun Kam, and Youngjoo Lee\*. "A lightweight ML-based ECG classification system using self-personalized anomaly detector". *IEEE Journal of Biomedical and Health Informatics, vol. 29, no. 10, pp. 7274-7284, Oct. 2025*.
- Wonhee Lee+, Jin Hyun+, Seung-Ick Choi, Sangbu Yun, Kwangho Chung, Seok Jong Chung, Jun Kyu Hwang, Eun Joo Yang, Youngjoo Lee\*, and Na Young Kim\*. "Distinguishing pathologic gait in older adults using instrumented insoles and deep neural networks". *IEEE Journal of Biomedical and Health Informatics, vol. 29, no. 7, pp. 4758-4768, July 2025*.
- Jeongwon Choe and Youngjoo Lee\*. "Area-efficient non-binary LDPC decoder with column-wise trellis min-max algorithm". *IEEE Journal of Solid-State Circuits, vol. 60, no. 3, pp. 1082-1091, Mar. 2025*.
- Hyeokjun Kwon+, Hyunhoon Lee+, Gyuhyun Jung, and Youngjoo Lee\*. "Energy-efficient flexible RNS-CKKS processor for FHE-based privacy-preserving computing". *IEEE Journal of Solid-State Circuits, vol. 60, no. 1, pp. 136-145, Jan. 2025. (Invited)*.
- Sangbu Yun+, Jeongwon Choe+, and Youngjoo Lee\*. "High-throughput software-defined LDPC encoder and decoder with x86-based data-level parallelism". *IEEE Transactions on Vehicular Technology, vol. 74, no. 1, pp. 50-60, Jan. 2025*.
- Doeun Sim, Younghoon Byun, Inseob Kim, and Youngjoo Lee\*. "High-performance and low-complexity multi-touch detection for variable ground states". *IEEE Sensors Journal, vol. 25, no. 2, pp. 3138-3150, Jan. 2025*.
- Eunbin Park and Youngjoo Lee\*. "mDARTS: Searching ML-based ECG classifiers against membership inference attacks". *IEEE Journal of Biomedical and Health Informatics, vol. 29, no. 1, pp. 177-187, Jan. 2025*.
- Jaehee Kim, Changhyeon Kim, Sangbu Yun, Dongyun Kam, Soonhyun Kwon, Yongjune Kim, and Youngjoo Lee\*. "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation". *IEEE International Symposium on Integrated Circuits and Systems (ISICAS, TCAS-I Special Issue), Qingdao, China, Oct. 2025. (IEEE CASS Student Travel Grants)*.
- Seungwoo Hong, Jung Gyu Min, Jin Hyun, Jaehee Kim, Dongyun Kam, Eunji Yoo, Pilsu Kim, Jaehyung Yoo, Hyoung-Euk Lee, and Youngjoo Lee\*. "FPGA-based real-time ISP accelerator using low-cost line buffers and non-linear functions". *IEEE Asia Pacific Conference on Circuits and Systems (APCCAS), Busan, Korea, Oct. 2025. (Best Live Demo Award - Silver Tier)*.
- Hayun Oh and Youngjoo Lee\*. "A quantitative evaluation method of neural rendering accelerators". *IEEE Asia Pacific Conference on Circuits and Systems (APCCAS), Busan, Korea, Oct. 2025*.
- Junehyuk Oh, Soonhyun Kwon, Dongyun Kam, and Youngjoo Lee\*. "On the hardware efficiency of short-length polarization-adjusted convolutional polar decoders". *IEEE Asia Pacific Conference of Circuits and Systems (APCCAS), Busan, Korea, Oct. 2025*.
- Seungkun Kim+, Jinho Byun+, Jung Gyu Min+, Jeonghoon Son, Jaehee Kim, Youngjoo Lee\*, and Seyoung Kim\*. "Ultra-fast CV-ECRAM-based analog PIM with dynamic retention compensation techniques". *IEEE European Solid-State Electronics Research Conference (ESSERC), Munich, Germany, Sep. 2025*.
- Myeongji Yun, Jung Gyu Min, Sein Oh, Jiwoung Choi, Minkyu Je, Jang-Sik Lee, and Youngjoo Lee\*. "Cost-efficient processing-in-memory architecture with training-free and universal error compensation". *ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED), Reykjavik, Iceland, Aug. 2025. (Best Paper Award Candidate)*.
- Yeji Lee+, Eunbin Park+, and Youngjoo Lee\*. "AMC: Adaptive mixed compression for ML models based on block-wise sensitivity". *IEEE International Symposium on Circuits and Systems (ISCAS), London, UK, May 2025*.
- Gunho Park+, Hyeokjun Kwon+, Jiwoo Kim, Jeongin Bae, Baeseong Park, Dongsoo Lee, and Youngjoo Lee\*. "FIGLUT: An energy-efficient accelerator design for FP-INT GEMM using look-up tables". *IEEE International Symposium on High-Performance Computer Architecture (HPCA), Las Vegas, NV, USA, Mar. 2025*.
- Dongyun Kam, Myeongji Yun, Sunwoo Yoo, Seungwoo Hong, Zhengya Zhang, and Youngjoo Lee\*. "Panacea: Novel DNN accelerator using accuracy-preserving asymmetric quantization and energy-saving bit-slice sparsity". *IEEE International Symposium on High-Performance Computer Architecture (HPCA), Las Vegas, NV, USA, Mar. 2025*.
- Gunil Kang+, Dahoon Park+, Hojin Lee, Sangwoo Jung, Jiyong Park, Jung Gyu Min, Youngjoo Lee, and Jaeha Kung\*. "RISC-V driven orchestration of vector processing units and eFlash compute-in-memory arrays for fast and accurate keyword spotting". *IEEE/ACM Asia and South Pacific Design Automation Conference (ASP-DAC), Tokyo, Japan, Jan. 2025*.
- 김시훈, 이예찬, 최정현, 홍승우, 이영주\*. "Deep learning을 이용한 demosaicing 알고리즘 개발 및 하드웨어 구현". *반도체공학회 동계종합학술대회, Jan. 2025. (Best Poster Award) (국내)*.

**2024**

- Sangwoo Jung, Jaehyun Lee, Dahoon Park, Youngjoo Lee, Jong-Hyeok Yoon, and Jaeha Kung\*. "A dual-precision and low-power CNN inference engine using a heterogeneous processing-in-memory architecture". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 71, no. 12, pp. 5546-5559, Dec. 2024*.
- Jaehee Kim+, Sangil Han+, Dongyun Kam, Byeong Yong Kong, and Youngjoo Lee\*. "A design framework for cost-efficient sorters with arbitrary input/output constraints". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 71, no. 12, pp. 5410-5419, Dec. 2024. (Invited)*.
- Dain Park, Dongyun Kam, Sangbu Yun, Jeongwon Choe, and Youngjoo Lee\*. "Hard-decision SCL polar decoder with weighted pruning operation for storage applications". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 71, no. 9, pp. 4181-4185, Sep. 2024*.
- Hyeongtaek Lee, Seungsik Moon, Youngjoo Lee, Jaeky Oh, Jaehoon Chung, and Junil Choi\*. "Multi-group multicasting systems using multiple RISs". *IEEE Transactions on Wireless Communications, vol. 23, no, 8, pp. 9488-9501, Aug. 2024*.
- Seungsik Moon and Youngjoo Lee\*. "A 43.9 μs IRS controller SoC with grid-based phase-shift optimization in 28 nm CMOS technology for next-generation communication". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 71, no. 7, pp. 3401-3412, July 2024*.
- Sangbu Yun, Seungsik Moon, Yo-Seb Jeon, and Youngjoo Lee\*. "Intelligent MIMO detection with momentum-induced unfolded layers". *IEEE Wireless Communications Letters, vol. 13, no. 3, pp. 879-883, Mar. 2024*.
- Sangbu Yun and Youngjoo Lee\*. "A 5.76 Gb/s 79.7 pJ/b 128×32 massive deep-learning uplink MIMO detector in 28nm CMOS technology". *IEEE Asian Solid-State Circuits Conference (A-SSCC), Hiroshima, Japan, Nov. 2024*.
- Seungjun Kim, Jeongwon Choe, and Youngjoo Lee\*. "On the decoding complexity of error correction code transformer". *International Conference on ICT Convergence (ICTC), Jeju, Korea, Oct. 2024*.
- Jeongwon Choe and Youngjoo Lee\*. "Cost-efficient partially-parallel LDPC decoder architecture for 50G-PON standard". *International SoC Design Conference (ISOCC), Sapporo, Japan, Aug. 2024*.
- Younghoon Byun and Youngjoo Lee\*. "Partially-structured transformer pruning with patch-limited XOR-gate compression for stall-free sparse-model access". *Design Automation Conference (DAC), San Francisco, CA, USA, June 2024*.
- Jiwoo Kim, Gunho Park, and Youngjoo Lee\*. "Low-power encoder and compressor design for approximate radix-8 Booth multiplier". *IEEE International Symposium on Circuits and Systems (ISCAS), Singapore, Singapore, May 2024*.
- Sangil Han+, Jaehee Kim+, Dongyun Kam, Byeong Yong Kong, Mijung Kim, Young-Seok Kim, and Youngjoo Lee\*. "Constrained sorter design using zero-one principle". *IEEE International Symposium on Circuits and Systems (ISCAS), Singapore, Singapore, May 2024. (IEEE CASS Student Travel Grants)*.
- Eunbin Park, Myungjun Jin, and Youngjoo Lee\*. "Cost-efficient SIMD ASIP architecture for mobile touchscreen controllers". *IEEE International Symposium on Circuits and Systems (ISCAS), Singapore, Singapore, May 2024*.
- Gunho Park+, Baeseong Park+, Minsub Kim, Sungjae Lee, Jeonghoon Kim, Beomseok Kwon, Se Jung Kwon, Byeongwook Kim, Youngjoo Lee, and Dongsoo Lee\*. "LUT-GEMM: Quantized matrix multiplication based on LUTs for efficient inference in large-scale generative language models". *International Conference on Learning Representations (ICLR), Vienna, Austria, May 2024*.
- Hyunhoon Lee+, Hyeokjun Kwon+, and Youngjoo Lee\*. "A 2.7~13.3 uJ/boot/slot flexible RNS-CKKS processor in 28nm CMOS technology for FHE-based privacy-preserving computing". *IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, Feb. 2024. (Student Travel Grant Award)*.
- Dongyun Kam, Sangbu Yun, Jeongwon Choe, Zhengya Zhang, Namyoon Lee, and Youngjoo Lee\*. "A 21.9 ns, 15.7 Gbps/mm^2 (128, 15) BOSS FEC decoder for 5G/6G URLLC applications". *IEEE International Solid-State Circuits Conference (ISSCC), San Francisco, CA, USA, Feb. 2024*.
- 류정현, 현진, 이영주\*. "Look-up Table 최적화를 통한 효율적인 Softmax 연산기 설계". *반도체공학회 하계학술대회, July 2024 (국내)*.

**2023**

- Dongwha Han, Jeonghun Park, Youngjoo Lee, H. Vincent Poor, and Namyoon Lee\*. "Block orthogonal sparse superposition codes for ultra-reliable low-latency communications". *IEEE Transactions on Communications, vol. 71, no. 12, pp. 6884-6897, Dec. 2023*.
- Hyunhoon Lee and Youngjoo Lee\*. "Optimizations of privacy-preserving DNN for low-latency inference on encrypted data". *IEEE Access, vol. 11, pp. 104775-104788, Sep. 2023*.
- Seungsik Moon, Namyoon Lee, and Youngjoo Lee\*. "Cost-efficient GPIP processing for large-scale multi-user MIMO systems". *IEEE Access, vol. 11, pp. 75325-75336, July 2023*.
- Seungsik Moon, Namyoon Lee, and Youngjoo Lee\*. "A scalable precoding processor for large-scale MU-MIMO systems". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 70, no. 7, pp. 3029-3039, July 2023*.
- Dongyun Kam, Byeong Yong Kong, and Youngjoo Lee\*. "Low-latency SCL polar decoder architecture using overlapped pruning operations". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 70, no. 3, pp. 1417-1427, Mar. 2023*.
- Gunho Park, Jaeha Kung, and Youngjoo Lee\*. "Simplified compressor and encoder designs for low-cost approximate radix-4 Booth multiplier". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 70, no.3, pp. 1154-1158, Mar. 2023*.
- 류은지, 이영주\*. "효율적 Transformer 모델 경량화를 위한 구조화된 프루닝". *반도체공학회 논문지, vol. 1, no. 1, pp. 23-30, Oct. 2023 (국내)*.
- Jiwon Kim, Seungsik Moon, and Youngjoo Lee\*. "Low-complexity phase shift design for IRS-aided SU-MIMO wireless systems". *International SoC Design Conference (ISOCC), Jeju, Korea, Oct. 2023*.
- Sangbu Yun and Youngjoo Lee\*. "Analysis of deep learning-based MIMO detectors". *International Conference on ICT Convergence (ICTC), Jeju, Korea, Oct. 2023*.
- Jin Hyun, Kwangho Chung, Wonhee Lee, Seungick Choi, Youngjoo Lee, and Nayoung Kim\*. "Assessing gait improvement after total knee arthroplasty using smart insole and deep neural network". *International Conference of the Korean Academy of Rehabilitation Medicine, Incheon, Korea, Oct. 2023*.
- Wonhee Lee, Jin Hyun, Seungick Choi, Sangbu Yun, Youngjoo Lee, and Nayoung Kim\*. "Distinguishing pathologic gait in the elderly by using instrumented insole and deep neural networks". *International Conference of the Korean Academy of Rehabilitation Medicine, Incheon, Korea, Oct. 2023*.
- Jung Gyu Min, Dongyun Kam, Younghoon Byun, Gunho Park, and Youngjoo Lee\*. "Energy-efficient RISC-V-based vector processor for cache-aware structurally-pruned transformers". *ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED), Vienna, Austria, Aug. 2023*.
- Eunji Yoo+, Gunho Park+, Jung Gyu Min, Se Jung Kwon, Baeseong Park, Dongsoo Lee, and Youngjoo Lee\*. "TF-MVP: Novel sparsity-aware transformer accelerator with mixed-length vector pruning". *Design Automation Conference (DAC), San Francisco, CA, USA, July 2023*.
- Jeongwon Choe and Youngjoo Lee\*. "A 2.35 Gb/s/mm^2 (7440, 6696) NB-LDPC decoder over GF(32) using memory-reduced column-wise trellis min-max algorithm in 28nm CMOS technology". *IEEE Symposium on VLSI Technology and Circuits (VLSI), Kyoto, Japan, June 2023*.
- Younghoon Byun+, Seungsik Moon+, Baeseong Park, Se Jung Kwon, Dongsoo Lee, Gunho Park, Eunji Yoo, Jung Gyu Min, and Youngjoo Lee\*. "Sparsity-aware memory interface architecture using stacked XORNet compression for accelerating pruned-DNN models". *Conference on Machine Learning and Systems (MLSys), Miami, FL, USA, June 2023*.
- Ranggi Hwang, Minhoo Kang, Jiwon Lee, Dongyun Kam, Youngjoo Lee, and Minsoo Rhu\*. "GROW: A row-stational sparse-dense GEMM accelerator for memory-efficient graph convolutional neural networks". *IEEE International Symposium on High-Performance Computer Architecture (HPCA), Montreal, QC, Canada, Feb. 2023*.
- Byeong Yong Kong\*, Hoyoung Yoo, and Youngjoo Lee. "An automated synthesis framework for fast evaluation of maximum operating frequency". *International Conference on Electronics, Information, and Communication (ICEIC), Singapore, Singapore, Feb. 2023*.
- 류은지, 이영주\*. "혼합 길이 벡터 프루닝을 이용한 새로운 희소성 인식 transformer 가속기". *반도체공학회 종합학술대회, Dec. 2023 (국내)*.
- 최정원, 이영주\*. "스토리지 용 NB-LDPC 복호기 하드웨어 개발". *반도체공학회 종합학술대회, Dec. 2023. (우수논문상) (국내)*.
- 이형택, 문승식, 이영주, 최준일\*. "다중 그룹 멀티캐스팅 환경에서의 실질적인 지능형 반사 표면 활용 기법". *제 33회 통신정보 합동학술대회 (JCCI), Apr. 2023 (국내)*.
- 윤상부, 이영주\*. "5G software 기지국을 위한 polar decoder의 고속 병렬처리". *제 33회 통신정보 합동학술대회 (JCCI), Apr. 2023 (국내)*.

**2022**

- Sanghyeon Ju, Youngjoo Lee, and Sunggu Lee\*. "Convolution neural networks with discrete cosine transform features". *IEEE Transactions on Computers, vol. 71, no. 12, pp. 3389-3395, Dec. 2022*.
- Jeongwon Choe and Youngjoo Lee\*. "High-throughput non-binary LDPC decoder architecture using parallel EMS algorithm". *IEEE Journal of Solid-State Circuits, vol. 57, no. 10, pp. 2969-2978, Oct. 2022. (Invited)*.
- Hyeokjun Kwon, Younghoon Byun, Seokhyeong Kang, and Youngjoo Lee\*. "CHAMP: Channel merging process for cost-efficient highly-pruned CNN acceleration". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 8, pp. 3308-3319, Aug. 2022*.
- Changhyeon Kim, Dongyun Kam, Seokki Kim, Giyoon Park, and Youngjoo Lee\*. "Simplified ordered statistic decoding for short-length linear block codes". *IEEE Communications Letters, vol. 26, no. 8, pp. 1720-1724, Aug. 2022*.
- Seungsik Moon, Hyeongtaek Lee, Junil Choi, and Youngjoo Lee\*. "Low-complexity beamforming optimization for IRS-aided MU-MIMO wireless systems". *IEEE Transactions on Vehicular Technology, vol. 71, no. 5, pp. 5587-5592, May 2022*.
- Seungwoo Hong, Dongyun Kam, Sangbu Yun, Jeongwon Choe, Namyoon Lee, and Youngjoo Lee\*. "Low-complexity and low-latency SVC decoding architecture using modified MAP-SP algorithm". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 4, pp. 1774-1787, Apr. 2022*.
- Sangbu Yun, Byeong Yong Kong, and Youngjoo Lee\*. "Area- and energy-efficient LDPC decoder using mixed-resolution check-node processing". *IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 69, no. 3, pp. 999-1003, Mar. 2022*.
- Jiwon Kim, Seungsik Moon, and Youngjoo Lee\*. "Hardware analysis of channel estimation method for IRS-aided MIMO wireless systems". *International SoC Design Conference (ISOCC), Gangneung, Korea, Oct. 2022. (ETRI Award)*.
- Gyuhyun Jung, Hyeokjun Kwon, Hyunhoon Lee, and Youngjoo Lee\*. "Fast estimation of NTT/INTT accelerator costs for RNS-based homomorphic encryption". *International SoC Design Conference (ISOCC), Gangneung, Korea, Oct. 2022*.
- Nayoung Kim\*, Seungick Choi, Sangbu Yun, Jin Hyun, Wonhee Lee, and Youngjoo Lee\*. "Classification of pathological gait using smart insole and machine-learning algorithm". *International Conference of the Korean Academy of Rehabilitation Medicine, Incheon, Korea, Oct. 2022*.
- Dongyun Kam, Byeong Yong Kong, and Youngjoo Lee\*. "A 1.1µs 1.56Gb/s/mm^2 cost-efficient large-list SCL polar decoder using fully-reusable LLR buffers in 28nm CMOS technology". *IEEE Symposium on VLSI Technology and Circuits (VLSI), Honolulu, HI, USA, June 2022*.
- Seungsik Moon+, Jaehyun Ko+, Byungsub Kim, and Youngjoo Lee\*. "A study on reliable high-speed HBC enhanced by ECC for wearable neural interfaces". *IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS), Incheon, Korea, June 2022*.
- Myeongji Yun, Seungwoo Hong, Sunwoo Yoo, Sungmin Park, Junho Kim, and Youngjoo Lee\*. "Lightweight end-to-end stress recognition using binarized CNN-LSTM models". *IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS), Incheon, Korea, June 2022*.
- Dongyoung Rim, Hyeokjun Kwon, and Youngjoo Lee\*. "Algorithm-hardware co-optimization for cost-efficient ML-based ISP accelerator". *IEEE International Symposium on Circuits and Systems (ISCAS), Austin, TX, USA, May 2022*.
- Seungsik Moon, Namyoon Lee, and Youngjoo Lee\*. "A 2.86Gb/s fully-flexible MU-MIMO processor for jointly optimizing user selection, power allocation, and precoding in 28nm CMOS technology". *IEEE Custom Integrated Circuits Conference (CICC), Newport Beach, CA, USA, Apr. 2022*.
- Dongyun Kam+, Jung Gyu Min+, Jongho Yoon, Sunmean Kim, Seokhyeong Kang, and Youngjoo Lee\*. "Design and evaluation frameworks for advanced RISC-based ternary processor". *IEEE/ACM Design, Automation and Test in Europe (DATE), Antwerp, Belgium, Mar. 2022*.
- 윤상부, 최정원, 김석기, 김남일, 이영주\*. "소프트웨어 모뎀을 위한 LDPC 부/복호기의 병렬화". *반도체공학회 하계학술대회, July 2022 (국내)*.
- 민정규, 이영주\*. "오픈 ISA 기반 벡터 프로세서의 희소행렬 압축 방식 분석". *대한전자공학회 하계종합학술대회, June 2022 (국내)*.
- 심도은, 박군호, 이영주\*. "Low-precision posit과 floating-point arithmetic의 정밀도 및 하드웨어 복잡도 분석". *대한전자공학회 하계종합학술대회, June 2022 (국내)*.
- 문승식, 이형택, 최준일, 이영주\*. "저지연 IRS 통신을 위한 그룹 기반 위상 최적화 기법". *제 32회 통신정보 합동학술대회 (JCCI), Apr. 2022 (국내)*.
- 감동윤, 이영주\*. "Complexity-latency tradeoff for 5G SCL polar decoder architecture". *제 29회 한국반도체학술대회, Jan. 2022 (국내)*.
- 홍승우, 이영주\*. "압축 센싱 복원을 위한 최소 제곱 솔버 구조". *제 29회 한국반도체학술대회, Jan. 2022 (국내)*.
- 변영훈, 이영주\*. "64bit RISC-V 기반 칩 검증 플랫폼 설계". *제 29회 한국반도체학술대회, Jan. 2022 (국내)*.

**2021**

- Byeong Yong Kong\*, Youngjoo Lee, and Hoyoung Yoo. "On the hardware complexity of tree expansion in MIMO detection". *Journal of Semiconductor Engineering, vol. 2, no. 3, pp. 136-141, Dec. 2021*.
- Gunho Park, Jaeha Kung, and Youngjoo Lee\*. "Design and analysis of approximate compressors for balanced error accumulation in MAC operator". *IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 68, no. 7, pp. 2950-2961, July 2021*.
- Hyunhoon Lee, Young-Seok Kim, Mijung Kim, and Youngjoo Lee\*. "Low-cost network scheduling of 3D-CNN processing for embedded action recognition". *IEEE Access, vol. 9, pp. 83901-83912, June 2021*.
- Dongyun Kam, Hoyoung Yoo, and Youngjoo Lee\*. "Ultra-low-latency successive cancellation polar decoding architecture using tree-level parallelism". *IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 29, no. 6, pp. 1083-1094, June 2021*.
- Minho Ha, Younghoon Byun, Seungsik Moon, Youngjoo Lee, and Sunggu Lee\*. "Layerwise buffer voltage scaling for energy-efficient convolutional neural network". *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 40, no. 1, pp. 1-10, Jan. 2021*.
- Jeongwon Choe and Youngjoo Lee\*. "A 7Gbps (160, 80) non-binary LDPC decoder with dual-message EMS algorithm in 22nm FinFET Technology". *IEEE Asian Solid-State Circuits Conference (A-SSCC), Busan, Korea, Nov. 2021*.
- Changhyeon Kim, Dongyoung Rim, Jeongwon Choe, Dongyun Kam, Giyoon Park, Seokki Kim, and Youngjoo Lee\*. "FPGA-based ordered statistic decoding architecture for B5G/6G URLLC IIOT networks". *IEEE Asian Solid-State Circuits Conference (A-SSCC), Busan, Korea, Nov. 2021*.
- Dongyoung Rim and Youngjoo Lee\*. "Performance evaluation of systolic DCNN accelerators". *International Conference on Consumer Electronics Asia (ICCE-Asia), Goseong, Korea, Nov. 2021*.
- Hyunsung Kim and Youngjoo Lee\*. "Utilizing energy-quality trade-off for low-cost ML-based compressive sensing reconstruction". *Asilomar Conference on Signals, Systems and Computers (ACSSC), Nov. 2021*.
- Jin Hyun, Seungsik Moon, and Youngjoo Lee\*. "Low-complexity voice activity detection algorithm for edge-level device". *International SoC Design Conference (ISOCC), Jeju, Korea, Oct. 2021. (Best Paper Award)*.
- Sunwoo Yoo, Seungwoo Hong, and Youngjoo Lee\*. "Low-complexity on-device ECG classifier using binarized neural network". *International SoC Design Conference (ISOCC), Jeju, Korea, Oct. 2021*.
- Hyunsung Kim, Jaehee Kim, Young-Seok Kim, Mijung Kim, and Youngjoo Lee\*. "Energy-efficient intelligent EPTS device using novel DCNN-based dynamic sensor activation". *IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS), June 2021*.
- Dongyun Kam, Byeong Yong Kong, and Youngjoo Lee\*. "Low-latency polar decoder using overlapped SCL processing". *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), June 2021*.
- Younghoon Byun and Youngjoo Lee\*. "Rapid design space exploration of near-optimal memory-reduced DCNN architecture using multiple model compression techniques". *IEEE International Symposium on Circuits and Systems (ISCAS), May 2021*.
- Yesung Kang, Eunji Kwon, Seunggyu Lee, Younghoon Byun, Youngjoo Lee, and Seokhyeong Kang\*. "Approach to improve the performance using bit-level sparsity in neural networks". *IEEE/ACM Design, Automation and Test in Europe (DATE), Feb. 2021*.
- 임동영, 이영주\*. "On-device 채널 구현을 위한 고효율 양자화된 가우시안 난수 생성기". *반도체공학회 하계학술대회, July 2021. (우수논문상) (국내)*.
- 박군호, 궁재하, 김영석, 김미정, 이영주\*. "저전력 딥러닝 가속기를 위한 근사 곱셈기 설계 프레임워크". *대한전자공학회 하계종합학술대회, July 2021. (네이버 논문상) (국내)*.
- 현진, 류동헌, 정강민, 이영주\*. "VoiceID: 딥러닝 기반 음성인식을 통한 모바일 보안 솔루션". *대한전자공학회 하계종합학술대회, July 2021 (국내)*.

## 특허

누리집 Patents 페이지 가운데 출원번호에 2021년 이후 연도가 적힌 국내 출원 18건과 국제(PCT) 출원 2건이다. 출원·등록 번호와 발명자는 페이지 표기 그대로이고, 등록번호가 함께 적힌 것은 3건이다. 출원 연도가 모두 2021–2024년이라, 연구실이 KAIST로 옮겨 오기 전에 출원한 것이다.[^patents][^news]

- Electronic device for predicting early gastric cancer lymph node metastasis based on ensemble model and learning method thereof (발명자 Youngjoo Lee, Sunwoo Yoo, and Kwangil Yim; 출원번호 PCT/KR2023/019834)
- Compensation pruning method optimized for low power capsule network operation and device thereof (발명자 Youngjoo Lee, Young-Seok Kim, and Junseo Jo; 출원번호 PCT/KR2021/003776)
- 상용화된 스마트 깔창을 이용한 딥러닝 기반의 노인의 보행 이상 분류 시스템 및 방법 (발명자 김나영, 이원희, 최승익, 이영주, 현진; 출원번호 10-2024-0166782; 등록번호 10-2864092)
- 신경망 연산 가속기, 신경망 연산 가속 방법, 트랜스포머 신경망의 혼합 길이 벡터 프루닝 방법 (발명자 이영주, 류은지, 박군호; 출원번호 10-2023-0195569)
- 가변 RNS 모듈러스 변환 연산 장치 및 방법 (발명자 이영주, 권혁준; 출원번호 10-2023-0192626)
- 통신 시스템에서 지능형 반사 표면을 이용한 통신 방법 및 장치 (발명자 김석기, 김남일, 문승식, 이영주; 출원번호 10-2023-0191942)
- 통신 시스템에서 지능형 반사 표면을 이용한 통신 방법 및 장치 (발명자 김석기, 김남일, 김지원, 이영주; 출원번호 10-2023-0191786)
- 저밀도 패리티 체크 부복호화 방법 (발명자 김석기, 김남일, 윤상부, 이영주, 최정원; 출원번호 10-2023-0191154)
- 앙상블 모델 기반의 조기 위암 림프절 전이를 예측하는 전자 장치 및 그의 학습 방법 (발명자 이영주, 유선우, 임광일; 출원번호 10-2023-0157522)
- 종양미세환경 내 세포에 대한 어노테이션을 수행하는 전자 장치 및 그의 어노테이션 방법 (발명자 이영주, 김은영, 유선우, 임광일; 출원번호 10-2023-0157523)
- 비선형 함수를 근사하는 방법 및 그 전자장치, 비선형 함수의 연산을 수행하는 전자 장치 (발명자 이영주, 홍승우, 현진; 출원번호 10-2023-0100434)
- 조기위암에서 내시경적 절제 후, 추가로 수술해야 하는 적응증을 결정하는 모델 (발명자 이영주, 유선우, 임광일; 출원번호 10-2022-0168122)
- 종양미세환경 주석 프로그램 (발명자 이영주, 김은영, 유선우, 임광일; 출원번호 10-2022-0168123)
- 리소스가 제한된 디바이스를 위한 하드웨어 효율적인 심전도 분류 방법 및 장치 (발명자 이영주, 김영석, 유선우, 홍승우; 출원번호 10-2022-0161456)
- 극단적 저해상도 채널에 적합한 폴라코드 알고리즘 기반 복호화 방법 및 장치 (발명자 이영주, 박다인, 김영석; 출원번호 10-2022-1060355)
- 부분곱 생성기, 부분곱 누적기 및 이들을 포함하는 근사 곱셈기 (발명자 이영주, 박군호, 김영석; 출원번호 10-2022-0160911)
- 컨벌루션 레이어의 연산 최적화 방법 및 컨벌루션 신경망 가속기 (발명자 이영주, 권혁준, 김영석; 출원번호 10-2022-0160902)
- 연판정 복호 방법 및 장치 (발명자 김석기, 박기윤, 박옥선, 이영주, 김창현; 출원번호 10-2022-0041533)
- 저전력 캡슐 네트워크 동작에 최적화된 보상 프루닝 방법 및 장치 (발명자 이영주, 조준서, 김영석; 출원번호 10-2021-0039290; 등록번호 10-2515579)
- 짧은 오류 정정 부호를 위한 하드웨어에 최적화된 OSD 알고리즘 복호화 방법 및 장치 (발명자 이영주, 김창현, 김석기, 박기윤; 출원번호 10-2021-0030981; 등록번호 10-2571253)

## 연구과제

누리집 Project 페이지 가운데 기간이 2021년 10월–2026년 10월에 걸치는 35건이다. 진행 중인 연구과제 12건, 끝난 연구과제 18건, 끝난 교육 사업 5건이며, 기간과 과제 이름·지원 사업은 페이지 표기 그대로다. 2025년 2월 KAIST로 옮겨 오기 전에 시작한 과제가 섞여 있다.[^project][^news]

- 2024/04~2031/12 · 네트워크 전문연구실(NRC): 통신 세대 진화를 위한 채널 부호 부복호 및 채널 추정 기술 (과학기술정보통신부 방송통신 산업기술 개발사업) (상태 진행 중)
- 2026/04~2029/12 · 점진적 적응형 온디바이스 AI 학습 플랫폼 (과학기술정보통신부 경량-저전력 AI 한계극복기술 개발사업) (상태 진행 중)
- 2025/04~2028/12 · 대규모 언어모델 특화 multi-bit 저항변화메모리 기반 초고효율 PIM 칩 개발 (과학기술정보통신부 PIM 인공지능반도체 핵심기술 개발사업) (상태 진행 중)
- 2022/12~2028/12 · 지능형 보안 수중 통신 특화연구실 (국방부 특화연구실 지원사업) (상태 진행 중)
- 2025/09~2028/09 · SSD architecture를 위한 초고속 초고효율 오류정정 솔루션 개발 (삼성전자 전략산학과제) (상태 진행 중)
- 2025/06~2028/05 · 극한효율 초거대 아이싱 파운데이션 모델 학습 시스템 연구실 (과학기술정보통신부 글로벌 기초연구실) (상태 진행 중)
- 2020/07~2027/12 · 지능형 의료영상 진단 솔루션 연구센터 (과학기술정보통신부 대학ICT연구센터 지원사업) (상태 진행 중)
- 2025/05~2027/04 · Customized multi-core RISC-V processor with tightly-coupled NPU architecture (삼성종합기술원 NPRC 전략산학) (상태 진행 중)
- 2024/04~2026/12 · 파장 정합성 유기수/발광다이오드 및 수직트랜지스터 통합소자를 활용한 고성능 유연 광통신 시스템 개발 (과학기술정보통신부 나노 및 소재기술 개발사업) (상태 진행 중)
- 2023/04~2026/12 · IoT intelligence용 eFLASH 파운더리 공정 기반 MPU/Connectivity/경량 신경망 통합 반도체 개발 (과학기술정보통신부 PIM 인공지능반도체 핵심기술 개발사업) (상태 진행 중)
- 2026/05~2026/12 · 지능형 통신을 위한 초고효율 ML baseband 시스템 개발 (KI Prototype 연구사업) (상태 진행 중)
- 2025/12~2026/05 · 초고속 고신뢰 LDPC 인코더 및 디코더 설계 ((주)에이아이오 산학과제) (상태 진행 중)
- 2022/09~2026/02 · 차세대 초고효율 6G 베이스밴드 시스템을 위한 알고리즘-하드웨어 융합최적화 (과학기술정보통신부 중견연구자지원사업) (상태 종료)
- 2023/04~2025/12 · CMOS 공정호환 강유전체 트랜지스터 기반 초고효율 3D vertical 컴퓨팅-인-메모리 집적 플랫폼 개발 (과학기술정보통신부 차세대 지능형반도체기술 개발사업) (상태 종료)
- 2022/01~2025/12 · 5G+ 지능형 기지국 소프트웨어 모뎀 개발 (과학기술정보통신부 방송통신산업기술 개발사업) (상태 종료)
- 2018/09~2025/08 · Emerging storage에 최적화된 오류정정시스템 개발 (삼성전자 전략산학과제) (상태 종료)
- 2024/06~2025/05 · Ultra-efficient LLM inference with layer-wise mixed-precision quantization and bit-level sparsity-aware processing (네이버/인텔 AI공동연구센터 사업) (상태 종료)
- 2021/04~2024/12 · HW지원 프라이버시 보장 암호데이터 고속처리 기술 개발 (과학기술정보통신부 정보보호 핵심원천기술 개발사업) (상태 종료)
- 2020/07~2024/12 · 동북권 Grand ICT연구센터 (과학기술정보통신부 Grand ICT연구센터 지원사업) (상태 종료)
- 2022/11~2024/10 · AI ISP SW/HW co-optimization (삼성종합기술원 산학협력과제) (상태 종료)
- 2023/07~2024/06 · Multi-touch에 대한 grouping 및 merge/separation 기술 개발 ((주)하이딥 산학과제) (상태 종료)
- 2023/07~2024/06 · Stylus pen의 tilt/azimuth 검출 및 좌표 보정에 관한 연구 ((주)하이딥 산학과제) (상태 종료)
- 2020/07~2024/04 · 벡터-연산자 확장을 통한 오픈ISA 기반 프로세서의 성능 개선 (과학기술정보통신부 슈퍼컴퓨터 개발 선도사업) (상태 종료)
- 2023/07~2023/11 · 50G PON용 HD-LDPC FPGA 하드웨어 기술 개발 (한국전자통신연구원 용역과제) (상태 종료)
- 2020/07~2023/02 · 신소자 개발지원을 위한 CMOS 통합 집적 센서 인터페이스 SoC 개발 (과학기술정보통신부 차세대 지능형반도체기술 개발사업) (상태 종료)
- 2018/12~2022/12 · 축구 국가대표 경기력 향상 훈련시스템 및 우수선수 발굴육성 시스템 개발 (문화체육관광부 첨단기술기반 국가대표 경기력 향상 사업) (상태 종료)
- 2022/01~2022/12 · Fine-grained pruning 지원 하드웨어 구현 및 검증 (네이버 산학과제) (상태 종료)
- 2019/06~2022/02 · 병렬 신경망 구조에 기반한 차세대 무선 통신용 초저전력 폴라 복호화 시스템 (과학기술정보통신부 개인연구지원사업) (상태 종료)
- 2021/05~2021/11 · 5G NR 데이터 채널 부호기 및 복호기의 벡터 가속화 구현 (한국전자통신연구원 위탁과제) (상태 종료)
- 2021/05~2021/11 · B5G URLLC 채널부호 FPGA 설계 및 검증 (한국전자통신연구원 위탁과제) (상태 종료)
- 2020/04~2025/12 · 바이오메디컬 시스템반도체 융합설계 인력육성 센터 참여연구실 (과학기술정보통신부 시스템반도체 융합전문인력 육성사업) (상태 종료, 교육 사업)
- 2024/07~2025/02 · 글로벌 데이터 융합전공 참여연구실 (과학기술정보통신부 글로벌 데이터 융합 리더 양성 사업) (상태 종료, 교육 사업)
- 2024/09~2025/02 · 반도체 대학원 참여연구실 (산업통상자원부 첨단산업 특성화대학원 사업) (상태 종료, 교육 사업)
- 2020/09~2025/02 · 지능형 정보융합 미래인재 교육연구단 참여연구실 (교육부 4단계 BK21 사업) (상태 종료, 교육 사업)
- 2019/09~2023/12 · POSTECH 스포츠AIX대학원 참여연구실 (문화체육관광부 스포츠산업 융복합 대학원 사업) (상태 종료, 교육 사업)

## 수상

Research 페이지 Research Awards 목록 가운데 2021–2025년 항목 22건이다. 연도는 페이지가 적은 행사 연도라 2021년 항목에는 2021년 10월 전 행사도 들어 있고, 상 이름·행사·논문 제목·수상자 표기는 페이지 그대로다. 2025년 2월 전의 수상은 연구실이 KAIST로 옮겨 오기 전의 것이다.[^research][^news] 교수의 수상은 「교수와 전문 분야」에 있다.

- 2025 · Chip Design Contest Best Poster Award (International SoC Design Conference (ISOCC)): "A low-latency polar decoder for URLLC with worst-case latency reduction in 28nm CMOS technology", Soonhyun Kwon, Dongyun Kam, Sangbu Yun, Jung Gyu Min, and Youngjoo Lee
- 2025 · Best Live Demo Award (Siver Tier) (IEEE Asia Pacific Conference on Circuits and Systems (APCCAS)): "FPGA-based real-time ISP accelerator using low-cost line buffers and non-linear functions", Seungwoo Hong, Jung Gyu Min, Jin Hyun, Jaehee Kim, Dongyun Kam, Eunji Yoo, Pilsu Kim, Jaehyung Yoo, Hyoung-Euk Lee, and Youngjoo Lee
- 2025 · Student Travel Grants (IEEE Circuits and Systems Society): "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation" (presented at ISICAS 2025), Jaehee Kim (Advisor: Prof. Youngjoo Lee)
- 2025 · Best Paper Award Candidate (ACM/IEEE International Symposium on Low Power Electronics and Designs (ISLPED)): "Cost-efficient processing-in-memory architecture with training-free and universal error compensation", Myeongji Yun, Jung Gyu Min, Sein Oh, Jiwoung Choi, Minkyu Je, Jang-Sik Lee, and Youngjoo Lee
- 2025 · Bronze Prize (Circuit Design Section) (제 31회 삼성 휴먼테크논문대상): "Panacea: Novel DNN accelerator using asymmetric quantization and energy-saving bit-slice sparsity", 윤명지, 유선우, 홍승우 (지도교수: 이영주)
- 2025 · Best Poster Award (반도체공학회 동계종합학술대회): "Deep learning을 이용한 demosaicing 알고리즘 개발 및 하드웨어 구현", 김시훈, 이예찬, 최정현, 홍승우, 이영주\*
- 2024 · Best Paper Award (산학협력 최우수논문상) (POSTECH-삼성전자 산학협력 교류회): "A 21.9 ns, 15.7 Gbps/mm^2 (128, 15) BOSS FEC decoder for 5G/6G URLLC applications", 감동윤 (지도교수: 이영주)
- 2024 · Best Design Award (IDEC Congress Chip Design Contest): "High-throughput and scalable deep learning driven massive MIMO detector in 28nm CMOS technology", 윤상부 (지도교수: 이영주)
- 2024 · Student Travel Grants (IEEE Circuits and Systems Society): "Constrained sorter design using zero-one principle" (presented at ISCAS 2024), Jaehee Kim (Advisor: Prof. Youngjoo Lee)
- 2024 · Student Travel Grant Award (IEEE International Solid-State Circuits Conference (ISSCC)): "A 2.7~13.3 uJ/boot/slot flexible RNS-CKKS processor in 28nm CMOS technology for FHE-based privacy-preserving computing", Hyunhoon Lee (Advisor: Prof. Youngjoo Lee)
- 2023 · Best Paper Award (우수논문상) (반도체공학회 종합학술대회): "스토리지 용 NB-LDPC 복호기 하드웨어 개발", 최정원, 이영주
- 2023 · Excellence Paper Award (산학협력 우수논문상) (POSTECH-삼성전자 산학협력 교류회): "A 2.35 Gb/s/mm^2 (7440, 6696) NB-LDPC decoder over GF(32) using memory-reduced column-wise trellis min-max algorithm in 28nm CMOS technology", 최정원 (지도교수: 이영주)
- 2023 · Excellence Design Award (POSTECH BMSC Chip Design Contest): "A 2.35 Gb/s/mm^2 4KB 0.9-rate NB-LDPC decoder using column-wise trellis min-max algorithm in 28nm CMOS technology", 최정원 (지도교수: 이영주)
- 2022 · ETRI Award (International SoC Design Conference (ISOCC)): "Hardware analysis of channel estimation method for IRS-aided MIMO wireless systems", Jiwon Kim, Seungsik Moon, and Youngjoo Lee
- 2022 · SK Telecom Award (one of top 10 research ideas) (ICT 챌린지): "딥러닝 기반 위암 치료 지원 시스템", 유선우, 홍승우 (지도교수: 이영주)
- 2022 · Excellence Design Award (우수설계상) (IDEC Congress Chip Design Contest): "A 2.86Gb/s fully-flexible MU-MIMO processor for jointly optimizing user selection, power allocation, and precoding in 28nm CMOS technology", 문승식 (지도교수: 이영주)
- 2022 · Excellence Poster Award (우수포스터상) (IDEC Congress Chip Design Contest): "Area- and energy-efficient LDPC decoder using mixed-resolution check-node processing", 윤상부 (지도교수: 이영주)
- 2021 · Bronze Medal (특허청장상) (제 22회 대한민국 반도체 설계대전): "Ordered statistic decoding architecture for B5G/6G URLLC IIoT networks", 김창현 (지도교수: 이영주)
- 2021 · Best Paper Award (IEEE CASS Daegu Chapter Award) (International SoC Design Conference (ISOCC)): "Low-complexity voice activity detection algorithm for edge-level device", Jin Hyun, Seungsik Moon, and Youngjoo Lee
- 2021 · Best Paper Award (최우수논문상) (POSTECH-삼성전자 산학협력 교류회): "Low-latency unfolded-KES architecture for emerging storage class memories", 문승식 (지도교수: 이영주)
- 2021 · Excellence Paper Award (우수논문상) (반도체공학회 하계학술대회): "On-device 채널 구현을 위한 고효율 양자화된 가우시안 난수 생성기", 임동영, 이영주
- 2021 · Best Paper Award (네이버 논문상) (대한전자공학회 하계종합학술대회): "저전력 딥러닝 가속기를 위한 근사 곱셈기 설계 프레임워크", 박군호, 궁재하, 김영석, 김미정, 이영주

## 소식

누리집 News 페이지의 2021년 10월–2026년 9월 글 110건이다. 날짜는 게시된 연·월이고 문장은 게시된 그대로다. 2025년 2월 전의 글은 연구실이 KAIST로 옮겨 오기 전의 소식이다.[^news]

- 2026/09 · Our paper entitled "CHASE-VLA: Post-training quantization framework for vision-language-action models with chunk-aware scale estimation" has been accepted for presentation at the 18th Asian Conference on Computer Vision (ACCV 2026).
- 2026/08 · Our paper entitled "A 14.4-Gb/s 7.3-pJ/b universal vision transformer OFDM channel estimation processor for B5G/6G communication systems" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2026/07 · Our paper entitled "ReSpec: Retrieval-guided speculative decoding for long-context LLM inference" has been accepted for presentation at the 2026 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2026).
- 2026/07 · Our paper entitled "Parameterized MAC IP generator for extremely low-precision floating-point arithmetic on FPGAs" has been accepted for presentation at the 2026 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2026).
- 2026/06 · Our paper enetitled "Retention-resilient ECRAM-PIM training system with device-algorithm-controller co-design" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2026/05 · Our project on multi-core RISC-V architecture has received the Best Research Award from the Samsung Neural Processing Research Center (NPRC).
- 2026/04 · Our paper entitled "Machine learning assisted tilt/azimuth estimation for passive stylus pens using position-based model selection" has been accepted for publication in the IEEE Access.
- 2026/04 · Our paper entitled "StylusNet: ML-based coordinate extractor for EMR stylus touch devices" has been accepted for publication in the IEEE Sensors Journal.
- 2026/03 · Prof. Lee has received the Outstanding Lecture Award from KAIST EE.
- 2026/03 · Our paper entitled "CL-PLAC: A generalized design framework for nonlinear functions using comparator-less piecewise linear approximate computation" has been accepted for publication in the IEEE Transactions on Circuits and Systems for Artificial Intelligence.
- 2026/02 · Our paper entitled "Asymmetric KV cache compression using state-aware sparsity and quantization" has been accepted for publication in the IEEE Transactions on Circuits and Systems for Artificial Intelligence.
- 2026/01 · Our paper entitled "Memory-efficient partially self-corrected min-sum LDPC decoder for 5G NR applications" has been accetped for presentation at the 2026 IEEE International Symposium on Circuits and Systems (ISCAS 2026).
- 2026/01 · Our paper entitled "Memory-efficient twiddle factor generator in parallel NTT accelerators for FHE applications" has been accetped for presentation at the 2026 IEEE International Symposium on Circuits and Systems (ISCAS 2026).
- 2026/01 · Our paper entitled "Low-latency software-defined 5G NR PUSCH receiver with mixed-precision SIMD acceleration" has been accetped for presentation at the 2026 IEEE International Symposium on Circuits and Systems (ISCAS 2026).
- 2026/01 · Our paper entitled "A parametric power model of upper mid-band (FR3) base stations for 6G" has been accepted for presentation at the 2026 IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2026).
- 2025/11 · Our paper entitled "LUT-SSM: A 99.3TFLOPS/W LUT-based state-space model accelerator using energy-efficient element-wise layer fusion and LUT-friendly weight-only quantization" has been accepted for presentation at the 2026 IEEE International Solid-State Circuits Conference (ISSCC 2026).
- 2025/11 · Our paper entitled "UniC-Vision: A 14.4Gb/s 7.3pJ/b universal vision transformer OFDM channel estimation accelerator for B5G/6G AI-RAN" has been accepted for presentation at the 2026 IEEE International Solid-State Circuits Conference (ISSCC 2026).
- 2025/11 · Our paper entitled "A 1.1mm^2, 14.4ns, 13.1pJ/b forward error correction with ordered-statistics post processing for ultra-reliable and low-latency communications" has been accepted for presentation at the 2026 IEEE International Solid-State Circuits Conference (ISSCC 2026).
- 2025/11 · Our paper entitled "IterQuant: Iterative quantization framework for mixed-precision LLM compression" has been accepted for presentation at the 2026 IEEE/ACM Design, Automation and Test in Europe (DATE 2026).
- 2025/11 · Our paper entitled "A 3.3 Gb/s/mm^2 area-efficient non-binary LDPC decoder using column-layered processing" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2025/10 · Our research on the URLLC polar decoder has been selected as the Chip Design Contest Best Poster Award at the 2025 International SoC Design Conference (ISOCC 2025).
- 2025/10 · Our research on the FPGA-based ISP accelerator has been selected as the Best Live Demo Award at the 2025 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2025).
- 2025/09 · Our paper entitled "NMIX: NoC-aware mixed precision quantization for energy-efficient ML accelerator" has been accepted for publication in the IEEE Transactions on Circuits and Systems II: Express Briefs.
- 2025/09 · Jaehee has received the Student Travel Grants by IEEE CASS for his paper "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation" at IEEE ISICAS 2025.
- 2025/08 · Our paper entitled "FPGA-based real-time ISP accelerator using low-cost line buffers and non-linear functions" has been accepted for presentation at the 2025 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2025).
- 2025/08 · Our paper entitled "A quantitative evaluation method of neural rendering accelerators" has been accepted for presentation at the 2025 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2025).
- 2025/08 · Our paper entitled "On the hardware efficiency of short-length polarization-adjusted convolutional polar decoders" has been accepted for presentation at the 2025 IEEE Asia Pacific Conference of Circuits and Systems (APCCAS 2025).
- 2025/08 · Our paper entitled "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation" has been accepted for presentation at the 2025 IEEE International Symposium on Integrated Circuits and Systems (ISICAS 2025, TCAS-I Special Issue).
- 2025/07 · Our paper entitled "A lightweight ML-based ECG classification system using self-personalized anomaly detector" has been accepted for publication in the IEEE Journal of Biomedical and Health Informatics.
- 2025/06 · Our research on the universal error compensation for PIM architectures has been selected as the Best Paper Award Candidate at the 2025 ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED 2025).
- 2025/05 · Our paper entitled "Ultra-fast CV-ECRAM-based analog PIM with dynamic retention compensation techniques" has been accepted for presentation at the 2025 IEEE European Solid-State Electronics Research Conference (ESSERC 2025).
- 2025/05 · Our paper entitled "Cost-efficient processing-in-memory architecture with training-free and universal error compensation" has been accepted for presentation at the 2025 ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED 2025).
- 2025/05 · Our paper entitled "Hybrid ordered statistics decoding of short-length BCH codes for URLLC systems: Theoretical analysis and decoder implementation" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2025/03 · Our paper entitled "Distinguishing pathologic gait in older adults using instrumented insoles and deep neural networks" has been accepted for publication in the IEEE Journal of Biomedical and Health Informatics.
- 2025/02 · We have been relocated to KAIST EE, continuing our EPIC journey for a better world.
- 2025/02 · Our research on the energy-efficient DNN accelerator has received the Bronze Prize at the 31st Samsung Humantech Paper Awards (Circuit Design Section).
- 2025/01 · Our paper entitled "AMC: Adaptive mixed compression for ML models based on block-wise sensitivity" has been accepted for presentation at the 2025 IEEE International Symposium on Circuits and Systems (ISCAS 2025).
- 2025/01 · Our research on the ML-based demosaicing algorithm has received the Best Poster Award at the 7th Annual Winter Conference of ISE.
- 2024/12 · Our paper entitled "Energy-efficient flexible RNS-CKKS processor for FHE-based privacy-preserving computing" has been accepted for publication in the IEEE Journal of Solid-State Circuits.
- 2024/11 · Our paper entitled "High-performance and low-complexity multi-touch detection for variable ground states" has been accepted for publication in the IEEE Sensors Journal.
- 2024/11 · Our paper entitled "FIGLUT: An energy-efficient accelerator design for FP-INT GEMM using look-up tables" has been accepted for presentation at the 2025 IEEE International Symposium on High-Performance Computer Architecture (HPCA 2025).
- 2024/11 · Our paper entitled "Panacea: Novel DNN accelerator using accuracy-preserving asymmetric quantization and energy-saving bit-slice sparsity" has been accepted for presentation at the 2025 IEEE International Symposium on High-Performance Computer Architecture (HPCA 2025).
- 2024/10 · Our paper entitled "mDARTS: Searching ML-based ECG classifiers against membership inference attacks" has been accepted for publication in the IEEE Journal of Biomedical and Health Informatics.
- 2024/09 · Our paper entitled "On the decoding complexity of error correction code transformer" has been accepted for presentation at the 15th International Conference on ICT Convergence (ICTC 2024).
- 2024/09 · Our paper entitled "Area-efficient non-binary LDPC decoder with column-wise trellis min-max algorithm" has been accepted for publication in the IEEE Journal of Solid-State Circuits.
- 2024/09 · Our paper entitled "RISC-V driven orchestration of vector processing units and eFlash compute-in-memory arrays for fast and accurate keyword spotting" has been accepted for presentation at the 2025 IEEE/ACM Asia and South Pacific Design Automation Conference (ASP-DAC 2025).
- 2024/08 · Our project on the low-cost FEC solution for storage systems has been selected as the most valuable research project by the Samsung-POSTECH Research Center to celebrate the 50-th anniversary of Samsung Semiconductor Business.
- 2024/08 · Our research on the cost-efficient BOSS decoder design has received the Best Paper Awared by the Samsung-POSTECH Research Center.
- 2024/08 · Our paper entitled "High-throughput software-defined LDPC encoder and decoder with x86-based data-level parallelism" has been accepted for publication in the IEEE Transactions on Vehicular Technology.
- 2024/08 · Dongyun has received the PIURI PostDoc Fellowship by POSTECH.
- 2024/08 · Our paper entitled "A 5.76 Gb/s 79.7 pJ/b 128×32 massive deep-learning uplink MIMO detector in 28nm CMOS technology" has been accepted for presentation at the 2024 IEEE Asian Solid-State Circuits Conference (A-SSCC 2024).
- 2024/07 · Our research on the ML-based MIMO detector has received the Best Design Award at the 2024 IDEC Congress Chip Design Contest.
- 2024/06 · Our paper entitled "A design framework for cost-efficient sorters with arbitrary input/output constraints" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2024/05 · Our paper entitled "Cost-efficient partially-parallel LDPC decoder architecture for 50G-PON standard" has been accepted for presentation at the 21st International SoC Design Conference (ISOCC 2024).
- 2024/05 · Jaehee has received the Student Travel Grants by IEEE CASS for his paper "Constrained sorter design using zero-one principle" at IEEE ISCAS 2024.
- 2024/04 · Our paper entitled "A 43.9 μs IRS controller SoC with grid-based phase-shift optimization in 28 nm CMOS technology for next-generation communication" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2024/04 · Our paper entitled "A dual-precision and low-power CNN inference engine using a heterogeneous processing-in-memory architecture" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2024/04 · Dongyun has received the POSTECHIAN Fellowship by POSTECH EE.
- 2024/03 · Our paper entitled "Hard-decision SCL polar decoder with weighted pruning operation for storage applications" has been accepted for publication in the IEEE Transactions on Circuits and Systems II: Express Briefs.
- 2024/02 · Our paper entitled "Partially-structured transformer pruning with patch-limited XOR-gate compression for stall-free sparse-model access" has been accepted for presentation at the 61st Design Automation Conference (DAC 2024).
- 2024/02 · Hyunhoon has received the Student Travel Grant Award by IEEE ISSCC 2024.
- 2024/02 · Seungsik has received the Best PhD Thesis Award by POSTECH EE.
- 2024/02 · Eunji has received the Best MS Thesis Award by POSTECH EE.
- 2024/01 · Our paper entitled "Multi-group multicasting systems using multiple RISs" has been accepted for publication in the IEEE Transactions on Wireless Communications.
- 2024/01 · Our paper entitled "LUT-GEMM: Quantized matrix multiplication based on LUTs for efficient inference in large-scale generative language models" has been accepted for presentation at the 12th International Conference on Learning Representations (ICLR 2024).
- 2024/01 · Our paper entitled "Low-power encoder and compressor design for approximate radix-8 Booth multiplier" has been accepted for presentation at the IEEE International Symposium on Circuits and Systems (ISCAS 2024).
- 2024/01 · Our paper entitled "Constrained sorter design using zero-one principle" has been accepted for presentation at the IEEE International Symposium on Circuits and Systems (ISCAS 2024).
- 2024/01 · Our paper entitled "Cost-efficient SIMD ASIP architecture for mobile touchscreen controllers" has been accepted for presentation at the IEEE International Symposium on Circuits and Systems (ISCAS 2024).
- 2023/12 · Our paper entitled "Intelligent MIMO detection with momentum-induced unfolded layers" has been accepted for publication in the IEEE Wireless Communications Letters.
- 2023/12 · Our research on the storage-aware non-binary LDPC decoder design has received the Best Paper Award at the 2023 Annual Conference of ISE.
- 2023/10 · Our paper entitled "A 2.7~13.3 uJ/boot/slot flexible RNS-CKKS processor in 28nm CMOS technology for FHE-based privacy-preserving computing" has been accepted for presentation at the IEEE International Solid-State Circuits Conference (ISSCC 2024).
- 2023/10 · Our paper entitled "A 21.9 ns, 15.7 Gbps/mm^2 (128, 15) BOSS FEC decoder for 5G/6G URLLC applications" has been accepted for presentation at the IEEE International Solid-State Circuits Conference (ISSCC 2024).
- 2023/09 · Our paper entitled "Optimizations of privacy-preserving DNN for low-latency inference on encrypted data" has been accepted for publication in the IEEE Access.
- 2023/09 · Our paper entitled "Block orthogonal sparse superposition codes for ultra-reliable low-latency communications" has been accepted for publication in the IEEE Transactions on Communications.
- 2023/08 · Our paper entitled "Analysis of deep learning-based MIMO detectors" has been accepted for presentation at the 14th International Conferenc on ICT Convergence (ICTC 2023).
- 2023/08 · Our research on the low-complexity non-binary LDPC decoder architecture for storage applications has received the Excellence Paper Award by the Samsung-POSTECH Research Center.
- 2023/08 · Our paper entitled "Low-complexity phase shift design for IRS-aided SU-MIMO wireless systems" has been accepted for presentation at the 20th International SoC Design Conference (ISOCC 2023).
- 2023/08 · Our research on the area-efficient 4KB 0.9-rate NB-LDPC decoder has received the Excellence Design Award at the 2023 POSTECH BMSC Chip Design Contest.
- 2023/07 · Our paper entitled "Cost-efficient GPIP processing for large-scale multi-user MIMO systems" has been accepted for publication in the IEEE Access.
- 2023/05 · Our paper entitled "Energy-efficient RISC-V-based vector processor for cache-aware structurally-pruned transformers" has been accepted for presentation at the 2023 ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED 2023).
- 2023/04 · Our paper entitled "A scalable precoding processor for large-scale MU-MIMO systems" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2023/03 · Our paper entitled "A 2.35 Gb/s/mm^2 (7440, 6696) NB-LDPC decoder over GF(32) using memory-reduced column-wise trellis min-max algorithm in 28nm CMOS technology" has been accepted for presentation at the 2023 IEEE Symposium on VLSI Technology and Circuits (VLSI 2023).
- 2023/02 · Our paper entitled "TF-MVP: Novel sparsity-aware transformer accelerator with mixed-length vector pruning" has been accepted for presentation at the 60th Design Automation Conference (DAC 2023).
- 2023/02 · Our paper entitled "Sparsity-aware memory interface architecture using stacked XORNet compression for accelerating pruned-DNN models" has been accepted for presentation at the 6th Conference on Machine Learning and Systems (MLSys23).
- 2022/12 · Our paper entitled "Low-latency SCL polar decoder architecture using overlapped pruning operations" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2022/10 · Our paper entitled "An automated synthesis framework for fast evaluation of maximum operating frequency" has been accepted for presentation at the 22nd International Conference on Electronics, Information, and Communication (ICEIC 2023).
- 2022/10 · Our research on the channel estimation of IRS-aided MIMO systems has been received the ETRI Award at the 19th International SoC Design Conference (ISOCC 2022).
- 2022/10 · Our paper entitled "Simplified compressor and encoder designs for low-cost approximate radix-4 Booth multiplier" has been accepted for publication in the IEEE Transactions on Circuits and Systems II: Express Briefs.
- 2022/10 · Our paper entitled "GROW: A row-stational sparse-dense GEMM accelerator for memory-efficient graph convolutional neural networks" has been accepted for presentation at the 29th IEEE International Symposium on High-Performance Computer Architecture (HPCA 2023).
- 2022/09 · Our research on the ML-based tumor microenvironment analysis has received the SK Telecom Award (one of top 10 ideas) at the ICT Challenge 2022.
- 2022/08 · Our paper entitled "Hardware analysis of channel estimation method for IRS-aided MIMO wireless systems" has been accepted for presentation at the 19th International SoC Design Conference (ISOCC 2022).
- 2022/08 · Our paper entitled "Fast estimation of NTT/INTT accelerator costs for RNS-based homomorphic encryption" has been accepted for presentation at the 19th International SoC Design Conference (ISOCC 2022).
- 2022/08 · Our Ph.D. student Seungsik Moon has been selected as a recipient of IEEE CASS Pre-Doctoral Grants.
- 2022/07 · Our research on the high-performance MU-MIMO processor has received the Excellence Design Award at the 2022 IDEC Congress Chip Design Contest.
- 2022/07 · Our research on the high-speed LDPC decoder architecture has received the Excellence Poster Award at the 2022 IDEC Congress Chip Design Contest.
- 2022/05 · Our paper entitled "High-throughput non-binary LDPC decoder architecture using parallel EMS algorithm" has been accepted for publication in the IEEE Journal of Solid-State Circuits.
- 2022/05 · Our paper entitled "Simplified ordered statistic decoding for short-length linear block codes" has been accepted for publication in the IEEE Communications Letters.
- 2022/05 · Our paper entitled "CHAMP: Channel merging process for cost-efficient highly-pruned CNN acceleration" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2022/04 · Our paper entitled "A 1.1µs 1.56Gb/s/mm^2 cost-efficient large-list SCL polar decoder using fully-reusable LLR buffers in 28nm CMOS technology" has been accepted for presentation at the 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI 2022).
- 2022/03 · Our paper entitled "A study on reliable high-speed HBC enhanced by ECC for wearable neural interfaces" has been accepted for presentation at the IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS 2022).
- 2022/03 · Our paper entitled "Lightweight end-to-end stress recognition using binarized CNN-LSTM models" has been accepted for presentation at the IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS 2022).
- 2022/02 · Our paper entitled "Low-complexity beamforming optimization for IRS-aided MU-MIMO wireless systems" has been accepted for publication in the IEEE Transactions on Vehicular Technology.
- 2022/01 · Our paper entitled "Algorithm-hardware co-optimization for cost-efficient ML-based ISP accelerator" has been accepted for presentation at the 2022 IEEE International Symposium on Circuits and Systems (ISCAS 2022).
- 2022/01 · Our paper entitled "A 2.86Gb/s fully-flexible MU-MIMO processor for jointly optimizing user selection, power allocation, and precoding in 28nm CMOS technology" has been accepted for presentation at the 2022 IEEE Custom Integrated Circuits Conference (CICC 2022).
- 2022/01 · Our paper entitled "Convolutional neural networks with discrete cosine transform features" has been accepted for publication in the IEEE Transactions on Computers.
- 2021/12 · Our paper entitled "Low-complexity and low-latency SVC decoding architecture using modified MAP-SP algorithm" has been accepted for publication in the IEEE Transactions on Circuits and Systems I: Regular Papers.
- 2021/11 · Our research on the low-latency OSD hardware for IIoT networks has received the Bronze Medal (특허청장상) at the 22nd Korea Semiconductor Design Contest.
- 2021/11 · Our paper entitled "Design and evaluation frameworks for advanced RISC-based ternary processor" has been accepted for presentation at IEEE/ACM Design, Automation and Test in Europe Conference (DATE 2022).
- 2021/10 · Our research on the low-complexity DNN-based voice activity recognition has received the Best Paper Award (IEEE CASS Daegu Chapter Award) at the 18th International SoC Design Conference (ISOCC 2021).
- 2021/10 · Our paper entitled "Performance evaluation of systolic DCNN accelerators" has been accepted for presentation at the 6th International Conference on Consumer Electrocins Asia (ICCE-Asia 2021).

## 연락과 위치

- 주소: EPIC LAB, #4219, Information & Electronics Building (E3-2), KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon 34141[^contact]
- 교수 연구실: 전기및전자공학부동(E3-2) 5201호[^eeprof]
- 전화: +82-(0)42-350-7480, +82-(0)42-350-7579[^contact]
- 교수 이메일: youngjoo@kaist.ac.kr[^eeprof]
[^p1]: S. Yoo 외, Y. Lee, 2026 IEEE International Solid-State Circuits Conference (ISSCC), 544-546 (2026). <https://doi.org/10.1109/isscc49663.2026.11409105> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: M. Yun, D. Kam, P. Panda, Y. Lee, IEEE Transactions on Circuits and Systems for Artificial Intelligence 3, 246-259 (2026). <https://doi.org/10.1109/tcasai.2026.3670075> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: S. Yun 외, Y. Lee, 2026 IEEE International Solid-State Circuits Conference (ISSCC), 48-50 (2026). <https://doi.org/10.1109/isscc49663.2026.11409283> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: J. Choe, Y. Lee, IEEE Transactions on Circuits and Systems I: Regular Papers 73, 2847-2857 (2026). <https://doi.org/10.1109/tcsi.2025.3632901> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: J. Kim 외, Y. Lee, IEEE Transactions on Circuits and Systems I: Regular Papers 72, 6528-6540 (2025). <https://doi.org/10.1109/tcsi.2025.3570034> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: M. Yun 외, Y. Lee, 2025 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED), 1-7 (2025). <https://doi.org/10.1109/islped65674.2025.11261781> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J. Hyun, S. Hong, Y. Lee, IEEE Transactions on Circuits and Systems for Artificial Intelligence 3, 340-353 (2026). <https://doi.org/10.1109/tcasai.2026.3674441> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: E. Park, D. Seo, H. Shin, Y. Lee, IEEE Sensors Journal 26, 17385-17397 (2026). <https://doi.org/10.1109/jsen.2026.3684492> 초록 기준(Semantic Scholar 등록 초록).
[^home]: EPIC Lab 누리집 첫 화면 <https://sites.google.com/view/epiclab> (연구실 소개, Latest News, 2026-10-23 열람)
[^research]: EPIC Lab 누리집 Research 페이지 <https://sites.google.com/view/epiclab/research> (Research Topics, Target Applications, Research Awards, 2026-10-23 열람)
[^member]: EPIC Lab 누리집 Member 페이지 <https://sites.google.com/view/epiclab/member> (Advisor, Postdoc Researchers, Ph.D. Students, M.S. Students, Alumni, Visiting Scholars, 2026-10-23 열람)
[^project]: EPIC Lab 누리집 Project 페이지 <https://sites.google.com/view/epiclab/project> (On-going Funded Research Projects, Previous Funded Projects, Previous Funded Education Programs, 2026-10-23 열람)
[^publication]: EPIC Lab 누리집 Publication 페이지 <https://sites.google.com/view/epiclab/publication> (Academic Collaborators, 2026-10-23 열람)
[^pubs]: EPIC Lab 누리집 Journal Papers <https://sites.google.com/view/epiclab/publication/journal-papers>, Conference Proceedings <https://sites.google.com/view/epiclab/publication/conference-proceedings> (목록 범위는 근거 페이지, 2026-10-23 열람)
[^patents]: EPIC Lab 누리집 Patents 페이지 <https://sites.google.com/view/epiclab/publication/patents> (International Patents, Domestic Patents, 2026-10-23 열람)
[^news]: EPIC Lab 누리집 News 페이지 <https://sites.google.com/view/epiclab/news> (2020–2026년 글, 2026-10-23 열람)
[^contact]: EPIC Lab 누리집 Contact 페이지 <https://sites.google.com/view/epiclab/contact> (Address, Tel., 2026-10-23 열람)
[^eeprof]: KAIST 전기및전자공학부 교수 소개(이영주) <https://ee.kaist.ac.kr/professor/%ec%9d%b4%ec%98%81%ec%a3%bc/> (직위, 주요 연구분야, 주요 연구, 소속연구실, 위치, 이메일, 디비전, 학위, 대표업적, 2026-10-23 열람)
[^eelist]: KAIST 전기및전자공학부 교수진 목록 3쪽 <https://ee.kaist.ac.kr/professor-s1/?page=3> (이영주 항목의 겸임학과, 2026-10-23 열람)
[^ssep]: KAIST 반도체시스템공학과 교수진 <https://sse.kaist.ac.kr/professor/> (이영주 교수 항목, 2026-10-23 열람)

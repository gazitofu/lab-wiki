# 비전 및 학습 연구실 (Vision and Learning Laboratory, VL)

**KAIST 전산학부·AI대학원 · 홍승훈 부교수**

- 분야: 시각 자료를 이해하고 생성하는 기계학습, 적은 예시로 배우는 범용 시각 예측, 그래프와 구조화 자료 학습, 생성 모델의 계산 효율, 기반 모델의 학습 후 개선
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^intro][^dept], 생성 인공지능[^projects][^p1][^p7], 그래프 기계학습·지식 그래프[^projects][^p3], 데이터 중심 AI·데이터 효율 학습[^projects][^p4][^p6], 모델 경량화·양자화[^projects]
- 홈페이지: <https://vllab.kaist.ac.kr/>
- 근거와 출처: [VL 근거 페이지](vllab-sources.md)

> 이미지·영상·입체 자료를 이해하고 생성하는 알고리즘을 만들며, 사람의 정답 표시를 줄여 새로운 과제에 적응하는 학습과 모델의 구조·계산 효율을 연구한다.[^intro][^projects]

## 무엇을 연구하나

홍승훈 교수가 이끄는 연구실은 기계학습(자료에서 규칙을 배워 새로운 입력의 결과를 계산하는 기술)으로 시각 세계를 이해하는 방법을 연구한다. 이미지와 영상뿐 아니라 포인트 클라우드(공간 속 점들의 좌표로 물체나 장면을 나타낸 자료)도 다룬다. 목표는 시각 자료를 인식하고 이해하며 새 자료를 생성하는 알고리즘을 만드는 것이다.[^intro][^dept]

연구실은 확장성(다루는 자료·개념·과제 규모를 늘려도 적용할 수 있는 성질)과 해석 가능성(모델이 어떤 근거로 결과를 냈는지 사람이 이해할 수 있는 성질)을 강조한다. 사람이 일일이 정답을 붙이는 지도를 최소화하면서 여러 개념과 과제를 배우게 하고, 사람이 모델의 학습·판단 과정을 이해하고 그 과정에 관여하게 하는 것이 연구 방향이다.[^intro]

이를 위해 딥러닝(여러 층의 신경망을 통해 자료의 표현을 단계적으로 학습하는 기계학습 분야)을 시각 자료와 관계 자료에 맞게 설계한다. 소량 예시 학습(적은 수의 정답 예시로 새 과제를 배우는 방법)에서는 학습 때 보지 못한 과제나 대상 조합에 기존 지식을 재사용한다. 그래프(개체를 점으로, 개체 사이 관계를 선으로 나타낸 자료)와 구조화 자료에서는 대칭성과 기하학적 원리에 맞는 범용 학습 알고리즘을 만든다.[^projects]

생성 모델(학습한 자료의 확률분포를 바탕으로 새 자료를 만드는 모델)과 기반 모델(여러 과제에 재사용할 수 있도록 폭넓은 자료로 미리 학습한 모델)도 주요 연구 대상이다. 확산 모델(잡음을 더하는 과정의 역방향을 학습해 자료를 생성하는 모델)과 흐름 정합(자료를 연속적으로 바꾸는 속도를 학습 목표로 삼는 방법)으로 이미지·영상·언어·구조화 자료의 생성을 연구한다. 기반 모델에서는 사전 학습(후속 과제에 쓸 지식을 미리 자료에서 학습하는 과정) 뒤의 적응과 모델 병합(서로 학습한 모델의 매개변수를 합쳐 한 모델로 만드는 일)을 다룬다.[^projects]

## 주요 연구 주제

### 확산·흐름 기반 생성 모델

학습한 생성 모델에서 실제 결과물을 뽑는 계산과, 생성에 필요한 단계 수를 줄이는 방법을 연구한다. FlowBind는 글·이미지·소리 사이의 정보를 공유하는 잠재 공간(모델이 자료를 내부 값으로 나타내는 공간)을 학습하고, 각 자료 종류와 이 공간을 양방향으로 잇는 변환을 함께 학습한다. 이를 이용해 서로 다른 종류의 입력과 출력 사이 생성을 수행한다.[^projects][^p1] ReDi는 이산 자료(서로 구별되는 값들로 이루어진 자료)를 생성할 때 생기는 근사 오차를 분석하고, 시작 자료와 목표 자료 사이의 대응을 반복해서 고쳐 적은 단계의 생성을 가능하게 하는 방법을 제안한다.[^p2]

긴 영상에서는 트랜스포머(토큰 사이 관계를 주의 기제로 계산하는 신경망 구조)의 계산량을 다룬다. MeBT(Memory-efficient Bidirectional Transformer, 메모리 효율을 고려한 양방향 트랜스포머)는 영상의 관측 부분을 내부 값들로 모으고, 이를 이용해 가려진 부분을 병렬로 복원하도록 학습한다. 쌍으로 주어진 자료 사이의 연속 변환을 배우는 연구에서는 두 자료를 내부 공간으로 옮긴 뒤 흐름 정합을 적용해, 자료 쌍의 대응 관계가 깨지는 문제를 다룬다.[^p7][^p5]

### 적은 예시로 새 시각 과제에 적응하기

연구실은 제한된 지도만으로 새로운 과제·개념·자료 환경·물체 조합에 일반화(학습 때 보지 못한 자료나 과제에도 학습한 규칙을 적용하는 성질)하는 시스템을 연구한다.[^projects] Visual Token Matching은 이미지와 정답 자료를 부분 단위로 대응시켜, 밀집 예측(이미지의 각 위치에 값을 부여하는 예측)을 서로 다른 과제에 같은 구조로 적용한다.[^p6] Chameleon은 학습 때 보지 못한 정답 구조에 적은 예시로 적응하도록 범용 모델을 설계하고, 영상·입체 자료·의료·생물 자료·사용자 상호작용 과제에 적용했다.[^p4]

### 대칭성과 구조를 이용한 그래프 학습

그래프와 구조화 자료를 위한 범용 알고리즘을 대칭성과 기하학에 근거해 개발한다.[^projects] 대표 논문은 그래프 위에서 무작위로 이동한 기록을 신경망이 읽고 점이나 그래프 전체의 값을 예측하게 한다. 점의 이름을 익명화한 기록으로 그래프의 이름 붙이기에 영향을 받지 않는 성질을 보장할 수 있음을 분석하고, 이동 기록을 글로 만들어 언어 모델이 그래프 과제를 풀게 하는 방법도 보인다.[^p3]

### 기반 모델의 학습 후 개선과 계산 효율

연구실은 추론(학습한 모델로 새 입력의 결과를 계산하는 과정) 시점의 적응, 학습이 끝난 모델들의 결합, 효율적인 토큰 압축을 연구한다.[^projects] 모델 병합 논문은 각 과제에 따로 맞춘 모델들의 학습 값을 추가 학습 없이 합치는 문제를 다룬다. 학습 값의 평균을 중심으로 과제별 차이를 나타내고, 그 차이를 제한된 수의 성분으로 근사해 과제 사이 간섭을 줄이는 방법을 제안했다.[^p8]

## 대표 논문

네 연구 갈래를 보여 주는 8편이다. 표의 연도와 발표처는 연구실 목록 기준이며, 설명은 연결된 arXiv 판의 초록을 기준으로 썼다. 여덟 편 모두 홍승훈 교수가 마지막 저자다. '쉽게 말하면' 칸은 각 논문의 초록만을 근거로 썼다.[^pubs]

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [FlowBind: Efficient Any-to-Any Generation with Bidirectional Flows](https://arxiv.org/abs/2512.15420) · ICLR 2026 (채택) | 글·이미지·소리를 공통 내부 공간과 잇는 양방향 변환을 함께 학습해, 서로 다른 자료 종류 사이에서 생성한다. 일부 종류만 짝지어진 자료도 학습에 사용할 수 있게 한다.[^p1] |
| 2 | 2025 | [ReDi: Rectified Discrete Flow](https://arxiv.org/abs/2507.15897) · NeurIPS 2025 (채택) | 이산 자료 생성의 근사 오차가 시작·목표 자료의 대응에 따라 달라짐을 분석하고, 그 대응을 반복해서 고쳐 적은 단계로 생성하는 방법을 제안한다.[^p2] |
| 3 | 2025 | [Revisiting Random Walks for Learning on Graphs](https://arxiv.org/abs/2407.01214) · ICLR 2025; GRaM Workshop @ICML 2024 | 그래프 위 이동 기록을 신경망이 읽어 점이나 그래프를 예측하게 한다. 점의 이름을 익명화하면 이름 붙이기에 영향을 받지 않는 성질을 확률적으로 보장할 수 있음을 분석한다.[^p3] |
| 4 | 2024 | [Chameleon: A Data-Efficient Generalist for Dense Visual Prediction in the Wild](https://arxiv.org/abs/2404.18459) · ECCV 2024 | 새 과제의 정답 자료 구조가 달라져도 적은 예시로 적응하도록 범용 시각 모델을 만든다. 여러 실제 과제에서 최대 50장의 정답 이미지로 적응하는 실험을 했다.[^p4] |
| 5 | 2024 | [Simulation-Free Training of Neural ODEs on Paired Data](https://arxiv.org/abs/2410.22918) · NeurIPS 2024 | 신경 상미분방정식(신경망으로 연속 변화율을 나타내는 모델)을 학습할 때, 쌍 자료의 대응을 유지하도록 내부 공간에서 흐름 정합을 수행한다. 회귀와 분류 과제에서 방법을 평가했다.[^p5] |
| 6 | 2023 | [Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching](https://arxiv.org/abs/2303.14969) · ICLR 2023 | 이미지와 정답의 부분별 내부 값을 대응시키는 방법으로 여러 종류의 밀집 예측 과제를 학습한다. 학습 때 보지 못한 과제에 소량 예시로 적응하는 구조를 제안했다.[^p6] |
| 7 | 2023 | [Towards End-to-End Generative Modeling of Long Videos with Memory-Efficient Bidirectional Transformers](https://arxiv.org/abs/2303.11251) · CVPR 2023 | 영상의 일부를 보고 가려진 시공간 부분을 병렬로 복원하는 학습을 통해 긴 영상의 관계를 다룬다. 관측 정보를 일정한 수의 내부 값으로 모아 계산 구조를 설계했다.[^p7] |
| 8 | 2024 | [Revisiting Weight Averaging for Model Merging](https://arxiv.org/abs/2412.12153) · arXiv 2024 | 과제별로 따로 학습한 모델들을 평균값을 중심으로 결합한다. 과제별 차이를 일부 성분으로 근사해 간섭을 줄이는 방법을 제안하고 시각·언어 과제에서 평가했다.[^p8] |

## 교수와 전문 분야

홍승훈 교수의 전공은 기계학습과 컴퓨터비전이다. 학과 소개는 2019년부터 KAIST 전산학부에서 재직하며, 기계학습을 활용한 자율적 시각 인지 시스템을 연구한다고 밝힌다. POSTECH에서 2011년 학사, 2017년 박사 학위를 받았고, 2017–2019년 University of Michigan 박사후연구원과 2019년 Google Brain 방문교수 경력을 적는다.[^faculty] 연구실 구성원 소개는 전산학부 소속과 KAIST AI 겸무를 함께 적는다. AI대학원 구성원 명단에는 전산학부 부교수로 실려 있다.[^members][^ai]

최근 논문에서 드러나는 전문 분야는 적은 예시로 새 시각 과제에 적응하는 범용 학습, 그래프 구조를 반영하는 학습, 영상·여러 자료 종류의 생성, 학습한 모델들을 결합하는 방법이다.[^p1][^p3][^p4][^p8]

## 응용 분야

연구의 대상은 이미지·영상·입체 자료의 이해와 생성, 글·이미지·소리 사이의 생성, 그래프 자료의 예측이다.[^intro][^p1][^p3] Chameleon은 영상·입체 자료 외에도 의료·생물 자료와 사용자 상호작용 과제에 적응하는 범용 시각 예측 방법을 다룬다.[^p4]

## 구성원

연구실이 게시한 박사후연구원 2명, 박사과정 3명, 석사과정 9명, 학부 연구 인턴 6명이다. 같은 이름의 저자를 같은 사람으로 보아 대표 논문 참여 번호를 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Donggyun Kim | 박사후연구원 | Few-shot Learning | kdgyun425@kaist.ac.kr | 4, 6, 8 |
| Jinwoo Kim | 박사후연구원 | Geometric Deep Learning | jinwoo-kim@kaist.ac.kr | 3, 5, 6 |
| Jaehoon Yoo | 박사과정 | Efficient Transformer | wogns98@kaist.ac.kr | 2, 5, 7 |
| Semin Kim | 박사과정 | Generative Models | seminkim@kaist.ac.kr | 1, 4, 5, 7 |
| Kiet Nguyen Tuan | 박사과정 | Efficient Transformer | kietngt00@kaist.ac.kr |  |
| Yeonwoo Cha | 석사과정 | Generative Modeling | ckdusdn03@kaist.ac.kr | 1, 5 |
| Chanhyuk Lee | 석사과정 | Multi-Task Learning, Generative Modeling | chan3684@kaist.ac.kr | 8 |
| Sunoh Lee | 석사과정 | Open-World Perception, Representation Learning | sunoh0131@kaist.ac.kr |  |
| Chanryeol Lee | 석사과정 | Efficient AI | lcy9442@kaist.ac.kr |  |
| Jiyun Park | 석사과정 | Geometric Deep Learning | jiyun02@kaist.ac.kr |  |
| Chanwoo Kim | 석사과정 | Few-shot Learning | chanwoo.kim282@kaist.ac.kr |  |
| Jinhyeon Kwon | 석사과정 | Generative Modeling | jh.kwon@kaist.ac.kr | 1 |
| Wonjung Kim | 석사과정 | Generative Modeling | wjhj16@kaist.ac.kr | 2 |
| Kyungbin Min | 석사과정 | Geometric Deep Learning | kbm04@kaist.ac.kr |  |
| Nayun Kim | 학부 인턴 | Geometric deep learning | kny031016@kaist.ac.kr |  |
| Yeonwoo Choi | 학부 인턴 | Generative Modeling | lotus_68@kaist.ac.kr |  |
| Yunseo Park | 학부 인턴 | Generative Modeling | yunseopark@kaist.ac.kr |  |
| Jihwan Yoon | 학부 인턴 | Generative Modeling | jihwan.yoon4@kaist.ac.kr |  |
| Wonjun Cho | 학부 인턴 |  |  |  |
| Youngmin Ryou | 학부 인턴 | Geometric deep learning | yym3055@kaist.ac.kr | 3 |

### 방문 학생

연구실이 게시한 방문 학생과 방문 연도다.[^members]

| 이름 | 방문 당시 소속·연도 | 게시된 후속 진로 |
|---|---|---|
| David Li | Mohamed Bin Zayed University, 2026 | |
| Nicole Shen | Massachusetts Institute of Technology, 2024 | |
| Olga Zaghen | University of Trento, 2023 | PhD student @ AMLab, University of Amsterdam |
| Honi Selahaddin | Istanbul Technical University, 2023 | PhD student @ NC Lab, KAIST |

## 졸업생·이전 인턴 진로

학위 졸업생 10명과 이전 연구 인턴 11명의 게시 정보다. Donggyun Kim과 Jinwoo Kim은 박사 졸업생과 현재 박사후연구원에 함께 올라 있다. HyeongJoo Hwang은 김기응 교수와 공동 지도한 졸업생으로 적혀 있다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Whie Jung | 박사 (2026) | researcher @ Qualcomm AI Research |
| Jiho Choi | 석사 (2026) |  |
| Donggyun Kim | 박사 (2026) | postdoc @ VL Lab, KAIST |
| Jinwoo Kim | 박사 (2026) | postdoc @ VL Lab, KAIST |
| Dong Hoon Lee | 박사 (2026) | researcher @ NAVER Cloud |
| HyeongJoo Hwang | 박사 (2024) | ML Engineer @ Samsung AI Center |
| Wonkwang Lee | 석사 (2022) | PhD student @ VL Lab, SNU |
| Sunghyun Myung | 석사 (2023) | researcher @ Theori |
| Seongwoong Cho | 석사 (2025) | researcher @ Mobilint |
| Suho Yang | 석사 (2025) |  |
| Sungbin Park | 연구 인턴 · KAIST (2026) |  |
| Hanbo Shim | 연구 인턴 · KAIST (2026) |  |
| Junee Kim | 연구 인턴 · KAIST (2024-2025) |  |
| Kyeongmin Kim | 연구 인턴 · KAIST (2024) |  |
| Hyeonseok Lee | 연구 인턴 · KAIST (2024) |  |
| Ayhan Suleymanzade | 연구 인턴 · KAIST (2023-2024) | PhD student @ EPFL |
| Ali Ahmed Sheikh | 연구 인턴 · KAIST (2023) |  |
| Tien Dat Nguyen | 연구 인턴 · KAIST (2021-2023) | MSc student @ R2L Lab, UWaterloo |
| Sungho (Daniel) Jung | 연구 인턴 · Penn State University (2021) | MSc student @ CV Lab, SNU |
| Saeyoon Oh | 연구 인턴 · KAIST (2021) | Engineer @ FuriosaAI |
| Chanhyeok Park | 연구 인턴 · KAIST (2021) | research intern @ 3D AI Lab, KAIST |

## 최근 5년 논문 목록

시각 자료의 이해·생성, 그래프 학습, 모델의 효율과 여러 과제의 학습을 다룬다. 연구실 목록의 날짜에 적힌 2021–2026년 기준 49편이다. 연구실 소식에서 채택을 확인한 학회 항목은 채택으로 표시했다. 학회명과 별도로 arXiv 링크를 게시한 논문들의 대표 논문 설명은 해당 사전 공개본 기준이다.[^pubs][^news]

**2026**

- Chanryeol Lee, Chanhyuk Lee, Yeonwoo Choi, Donggyun Kim†, Seunghoon Hong†. "PatchKV: Weight-Space Compensation of KV Cache". *NeurIPS 2026 (채택)*.
- Semin Kim, Jihwan Yoon, Seunghoon Hong. "Root-Selecting Fixed-Point Inversion for Rectified Flows via Trajectory Straightness". *NeurIPS 2026 (채택)*.
- Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim†, Seunghoon Hong†. "Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models". *NeurIPS 2026 (채택)*.
- Donggyun Kim, Chanwoo Kim, Seunghoon Hong. "HyperFlow: Gradient-Free Emulation of Few-Shot Fine-Tuning". *NeurIPS 2026 (채택)*.
- Chanhyuk Lee, Jaehoon Yoo, Manan Agarwal, Sheel Shah, Jerry Huang, Aditi Raghunathan, Seunghoon Hong, Nicholas M. Boffi†, Jinwoo Kim†. "Flow Map Language Models: One-step Language Modeling via Continuous Denoising". *NeurIPS 2026; NonAR-LM Workshop @ COLM 2026 Spotlight Presentation (채택)*.
- Manan Agarwal\*, Sheel Shah\*, Chanhyuk Lee, Jaehoon Yoo, Jerry Huang, Seunghoon Hong, Aditi Raghunathan, Jinwoo Kim†, Nicholas M. Boffi†. "Posterior Refinement: Fast Language Generation via Any-Order Flow Maps". *NonAR-LM Workshop @ COLM 2026 Spotlight Presentation (채택)*.
- Jaehoon Yoo\*, Wonjung Kim\*, Floor Eijkelboom, Chanhyuk Lee, Nicholas M. Boffi, Seunghoon Hong†, Jinwoo Kim†. "Self-conditioned Flow Map Language Models via Fixed-point Flows". *NonAR-LM Workshop @ COLM 2026 Oral Presentation (채택)*.
- Donggyun Kim\*, Jack Lu\*, Chanwoo Kim, Mengye Ren, Seunghoon Hong. "HyperThink: Text-to-parameter hypernetworks for efficient reasoning". *COLM 2026 (채택)*.
- Jiho Choi, Jaemin Kim, Sanghwan Kim†, Seunghoon Hong†, Jin-Hwi Park†. "When Sinks Help or Hurt: Unified Framework for Attention Sink in Large Vision-Language Models". *ECCV 2026 (채택)*.
- Yeonwoo Cha, Jaehoon Yoo, Semin Kim, Yunseo Park, Jinhyeon Kwon, Seunghoon Hong. "Training-Free Refinement of Flow Matching with Divergence-based Sampling". *ECCV 2026 (채택)*.
- Dong Hoon Lee, Seunghoon Hong. "Variable-Length Tokenization via Learnable Global Merging for Diffusion Transformers". *ICML 2026 (채택)*.
- Jaehoon Yoo\*, Wonjung Kim\*, Chanhyuk Lee, Seunghoon Hong. "Infinite Mask Diffusion for Few-Step Distillation". *ICML 2026 (채택)*.
- Jinwoo Kim\*, Sékou-Oumar Kaba\*, Jiyun Park, Seunghoon Hong†, Siamak Ravanbakhsh†. "Inverting Data Transformations via Diffusion Sampling". *ICML 2026 (채택)*.
- Chanhyuk Lee, Jiho Choi, Chanryeol Lee, Donggyun Kim, Seunghoon Hong. "AdaRank: Adaptive Rank Pruning for Enhanced Model Merging". *ICLR 2026 (채택)*.
- Yeonwoo Cha\*, Semin Kim\*, Jinhyeon Kwon, Seunghoon Hong. "FlowBind: Efficient Any-to-Any Generation with Bidirectional Flows". *ICLR 2026 (채택)*.

**2025**

- Jinwoo Kim\*, Xingyue Huang\*, Krzysztof Olejniczak, Kyungbin Min, Michael Bronstein, Seunghoon Hong, İsmail İlkan Ceylan. "Flock: A Knowledge Graph Foundation Model via Learning on Random Walks". *ICLR 2026 (채택)*.
- Jinwoo Kim, Max Beier, Petar Bevanda, Nayun Kim, Seunghoon Hong. "Sequence Modeling with Spectral Mean Flows". *NeurIPS 2025 (채택)*.
- Kiet T Nguyen, Chanhyuk Lee, Donggyun Kim, Dong Hoon Lee, Seunghoon Hong. "Universal Few-shot Spatial Control for Diffusion Models". *NeurIPS 2025 (채택)*.
- Jaehoon Yoo, Wonjung Kim, Seunghoon Hong. "ReDi: Rectified Discrete Flow". *NeurIPS 2025 (채택)*.
- Whie Jung, Dong Hoon Lee, Seunghoon Hong. "Disentangled Representation Learning via Modular Compositional Bias". *NeurIPS 2025 (채택)*.
- Whie Jung, Semin Kim, Junee Kim, Seunghoon Hong. "Bridging the gap to real-world language-grounded visual concept learning". *NeurIPS 2025 (채택)*.
- Jinwoo Kim, Olga Zaghen\*, Ayhan Suleymanzade\*, Youngmin Ryou, Seunghoon Hong. "Revisiting Random Walks for Learning on Graphs". *ICLR 2025 Spotlight Presentation; GRaM Workshop @ICML 2024*.
- Sungjun Cho, Dae-Woong Jeong, Sung Moon Ko, Jinwoo Kim, Sehui Han, Seunghoon Hong, Honglak Lee, Moontae Lee. "3D Denoisers are Good 2D Teachers: Molecular Pretraining via Denoising and Cross-Modal Distillation". *AAAI 2025 Oral Presentation*.

**2024**

- Jiho Choi\*, Donggyun Kim\*, Chanhyuk Lee, Seunghoon Hong. "Revisiting Weight Averaging for Model Merging". *arXiv 2024*.
- Seongwoong Cho\*, Donggyun Kim\*, Jinwoo Lee, Seunghoon Hong. "Meta-Controller: Few-Shot Imitation of Unseen Embodiments and Tasks in Continuous Control". *NeurIPS 2024*.
- Semin Kim\*, Jaehoon Yoo\*, Jinwoo Kim, Yeonwoo Cha, Saehoon Kim, Seunghoon Hong. "Simulation-Free Training of Neural ODEs on Paired Data". *NeurIPS 2024*.
- Dong Hoon Lee, Seunghoon Hong. "Learning to Merge Tokens via Decoupled Embedding for Efficient Vision Transformers". *NeurIPS 2024*.
- Donggyun Kim, Seongwoong Cho, Semin Kim, Chong Luo, Seunghoon Hong. "Chameleon: A Data-Efficient Generalist for Dense Visual Prediction in the Wild". *ECCV 2024 Oral Presentation*.
- Whie Jung, Jaehoon Yoo, Sungjin Ahn, Seunghoon Hong. "Learning to Compose: Improving Object Centric Learning by Injecting Compositionality". *ICLR 2024*.

**2023**

- Tien Dat Nguyen\*, Jinwoo Kim\*, Hongseok Yang, Seunghoon Hong. "Learning Symmetrization for Equivariance with Orbit Distance Minimization". *NeurReps Workshop @ NeurIPS 2023*.
- HyeongJoo Hwang, Seokin Seo, Youngsoo Jang, Sungyoon Kim, Geon-Hyeong Kim, Seunghoon Hong, Kee-Eung Kim. "Information-Theoretic State Space Model for Multi-View Reinforcement Learning". *ICML 2023 Oral Presentation*.
- Jinwoo Kim, Tien Dat Nguyen, Ayhan Suleymanzade, Hyeokjun An, Seunghoon Hong. "Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance". *NeurIPS 2023 Spotlight Presentation*.
- Jaehoon Yoo, Semin Kim, Doyup Lee, Chiheon Kim, Seunghoon Hong. "Towards End-to-End Generative Modeling of Long Videos with Memory-Efficient Bidirectional Transformers". *CVPR 2023*.
- Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong. "Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching". *ICLR 2023 Outstanding Paper*.

**2022**

- Sungjun Cho, Seonwoo Min, Jinwoo Kim, Moontae Lee, Honglak Lee, Seunghoon Hong. "Transformers meet Stochastic Block Models: Attention with Data-Adaptive Sparsity and Cost". *NeurIPS 2022*.
- Jinwoo Kim, Tien Dat Nguyen, Seonwoo Min, Sungjun Cho, Moontae Lee, Honglak Lee, Seunghoon Hong. "Pure Transformers are Powerful Graph Learners". *NeurIPS 2022*.
- Jinwoo Kim, Saeyoon Oh, Sungjun Cho, Seunghoon Hong. "Equivariant Hypergraph Neural Networks". *ECCV 2022*.
- Woo Jae Kim, Seunghoon Hong, Sung-Eui Yoon. "Diverse Generative Perturbations On Attention Space For Transferable Adversarial Attacks". *ICIP 2022*.
- Yoonki Cho, Woo Jae Kim, Seunghoon Hong, Sung-Eui Yoon. "Part-based Pseudo Label Refinement for Unsupervised Person Re-identification". *CVPR 2022*.
- Jaechang Kim, Yunjoo Lee, Seunghoon Hong, Jungseul Ok. "Learning Continuous Representation of Audio for Arbitrary Scale Super-Resolution". *ICASSP 2022*.
- Donggyun Kim, Seongwoong Cho, Wonkwang Lee, Seunghoon Hong. "Multi-Task Neural Processes". *ICLR 2022*.
- Sungwon Park, Sungwon Han, Donghyun Ahn, Jaeyeon Kim, Jeasurk Yang, Susang Lee, Seunghoon Hong, Jihee Kim, Sangyoon Park, Hyunjoo Yang, Meeyoung Cha. "Learning Economic Indicators by Aggregating Multi-level Geospatial Information". *AAAI 2022*.

**2021**

- Jinwoo Kim, Saeyoon Oh, Seunghoon Hong. "Transformers Generalize DeepSets and Can be Extended to Graphs and Hypergraphs". *NeurIPS 2021*.
- HyeongJoo Hwang, Geon-hyeong Kim, Seunghoon Hong, Kee-Eung Kim. "Multi-View Representation Learning via Total Correlation Objective". *NeurIPS 2021*.
- Kyungmoon Lee, Sungyeon Kim, Seunghoon Hong, Suha Kwak. "Learning to Generate Novel Classes for Deep Metric Learning". *BMVC 2021*.
- Jinwoo Kim\*, Jaehoon Yoo\*, Juho Lee, Seunghoon Hong. "SetVAE: Learning Hierarchical Composition for Generative Modeling of Set-Structured Data". *CVPR 2021*.
- Sungwon Park\*, Sungwon Han\*, Sungdong Kim, Danu Kim, Sangkyu Park, Seunghoon Hong, Meeyoung Cha. "Improving Unsupervised Image Clustering With Robust Learning". *CVPR 2021*.
- Wonkwang Lee, Whie Jung, Han Zhang, Ting Chen, Jing Yu Koh, Thomas Huang, Hyungsuk Yoon, Honglak Lee, Seunghoon Hong. "Revisiting Hierarchical Approach for Persistent Long-Term Video Prediction". *ICLR 2021*.
- Minkyo Seo, Dongkeun Kim, Kyungmoon Lee, Seunghoon Hong, Jae Seok Bae, Jung Hoon Kim, Suha Kwak. "Neural Contrast Enhancement of CT Image". *WACV 2021*. [DOI](https://doi.org/10.1109/wacv48630.2021.00402).[^ct]

## 최근 5년 진행 연구

연구실이 진행 중으로 표시한 네 연구 갈래와 게시 시작 연도다.[^projects]

- Diffusion and Flow-based Models (기간 2021-; 상태 진행 중)
- Improving Foundation Models (기간 2022-; 상태 진행 중)
- Data-Efficient Generalization (기간 2020-; 상태 진행 중)
- Geometric Deep Learning (기간 2021-; 상태 진행 중)

## 최근 5년 수상·선정

2021-10-13–2026-10-13 사이 연구실이 게시한 논문상·연구 지원 선정 5건이다.[^news]

- 2023-03-22 · 범용 소량 예시 학습 논문이 ICLR 2023 Outstanding Paper Award를 받았다.
- 2023-01-30 · Donggyun Kim이 제29회 삼성휴먼테크논문대상 은상을 받았다.
- 2022-11-18 · Jinwoo Kim이 Qualcomm Innovation Fellowship Korea 2022에 선정됐다.
- 2022-08-29 · Tien Dat Nguyen이 URP 연구 과제로 우수상을 받았다.
- 2022-04-18 · Jinwoo Kim이 관정이종환교육재단 장학생으로 선정됐다.

## 최근 5년 소식

2021-10-13–2026-10-13 사이의 논문 채택과 연구실 이전 소식 28건이다.[^news]

- 2026-09-27 · NeurIPS 2026에 논문 7편이 채택됐으며, 그중 1편은 Spotlight 발표로 선정됐다.
- 2026-09-10 · COLM 2026 워크숍에 논문 3편이 채택됐으며, 1편은 Oral, 2편은 Spotlight 발표로 선정됐다.
- 2026-07-10 · COLM 2026에 논문 1편이 채택됐다.
- 2026-06-18 · ECCV 2026에 논문 2편이 채택됐다.
- 2026-05-01 · ICML 2026에 논문 3편이 채택됐다.
- 2025-11-11 · ICLR 2026에 논문 3편이 채택됐다.
- 2025-11-11 · WACV 2026에 논문 1편이 채택됐다.
- 2025-09-17 · NeurIPS 2025에 논문 5편이 채택됐다.
- 2025-06-10 · 연구실이 KRAFTON SoC Building(E3-5)의 새 사무실로 이전했다.
- 2025-01-23 · ICLR 2025에 논문 1편이 Spotlight 발표로 채택됐다.
- 2024-12-20 · AAAI 2025에 논문 1편이 Oral 발표로 채택됐다.
- 2024-09-25 · NeurIPS 2024에 논문 3편이 채택됐다.
- 2024-08-13 · ECCV 2024에 논문 1편이 Oral 발표로 채택됐다.
- 2024-07-02 · ICML 2024 워크숍에 논문 1편이 채택됐다.
- 2024-02-07 · ICLR 2024에 논문 1편이 채택됐다.
- 2023-09-05 · NeurIPS 2023에 논문 2편이 채택됐다. Spotlight 발표 1편과 워크숍 논문 1편이다.
- 2023-07-05 · ICML 2023에 논문 1편이 Oral 발표로 채택됐다.
- 2023-02-28 · CVPR 2023에 논문 1편이 채택됐다.
- 2023-01-21 · ICLR 2023에 논문 1편이 Oral 발표로 채택됐다.
- 2022-09-25 · NeurIPS 2022에 논문 2편이 채택됐다.
- 2022-07-20 · ECCV 2022에 논문 1편이 채택됐다.
- 2022-06-20 · ICIP 2022에 논문 1편이 채택됐다.
- 2022-04-01 · ICASSP 2022에 논문 1편이 채택됐다.
- 2022-03-02 · CVPR 2022에 논문 1편이 채택됐다.
- 2022-02-09 · ICLR 2022의 MLDD 워크숍에 논문 1편이 채택됐다.
- 2022-02-09 · ICLR 2022에 논문 1편이 채택됐다.
- 2021-10-28 · BMVC 2021에 논문 1편이 채택됐다.
- 2021-10-27 · NeurIPS 2021에 논문 2편이 채택됐다.

## 연락과 위치

- 교수 이메일: seunghoon.hong@kaist.ac.kr.[^members]
- 연구실: 대전광역시 유성구 대학로 291, KAIST KRAFTON Building(E3-5) 512호.[^home]
- 교수 연구실: E3-5 506호. 학과 교수진 명단의 교내 전화는 3579다.[^roster][^faculty]

## 각주
[^p1]: Y. Cha, S. Kim, J. Kwon, S. Hong, arXiv (온라인 2025-12-17). <https://arxiv.org/abs/2512.15420> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2512.15420>. 관측 2026-10-30.
[^p2]: J. Yoo, W. Kim, S. Hong, arXiv (온라인 2025-07-21). <https://arxiv.org/abs/2507.15897> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2507.15897>. 관측 2026-10-30.
[^p3]: J. Kim 외, S. Hong, arXiv (온라인 2024-07-01). <https://arxiv.org/abs/2407.01214> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2407.01214>. 관측 2026-10-30.
[^p4]: D. Kim 외, S. Hong, arXiv (온라인 2024-04-29). <https://arxiv.org/abs/2404.18459> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2404.18459>. 관측 2026-10-30.
[^p5]: S. Kim 외, S. Hong, arXiv (온라인 2024-10-30). <https://arxiv.org/abs/2410.22918> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2410.22918>. 관측 2026-10-30.
[^p6]: D. Kim 외, S. Hong, arXiv (온라인 2023-03-27). <https://arxiv.org/abs/2303.14969> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2303.14969>. 관측 2026-10-30.
[^p7]: J. Yoo 외, S. Hong, arXiv (온라인 2023-03-20). <https://arxiv.org/abs/2303.11251> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2303.11251>. 관측 2026-10-30.
[^p8]: J. Choi, D. Kim, C. Lee, S. Hong, arXiv (온라인 2024-12-11). <https://arxiv.org/abs/2412.12153> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2412.12153>. 관측 2026-10-30.
[^intro]: Vision and Learning Laboratory, 연구실 소개. 이미지·영상·포인트 클라우드의 인식·이해·생성과, 최소한의 지도·확장성·해석 가능성을 연구 방향으로 적는다. <https://vllab.kaist.ac.kr/api/data/index/index> 관측 2026-10-30.
[^projects]: Vision and Learning Laboratory, 현재 연구 갈래 4건. 확산·흐름 모델의 생성 계산과 단계 축소, 기반 모델의 추론 시 적응·학습 후 결합·효율적 토큰 압축, 제한된 지도로 새 과제에 일반화하는 학습, 대칭성과 기하학에 기초한 그래프·구조화 자료의 범용 딥러닝을 연구한다고 설명한다. <https://vllab.kaist.ac.kr/api/data/projects/index> 관측 2026-10-30.
[^dept]: KAIST 전산학부, 비전 및 학습 연구실. 이미지·비디오·포인트 클라우드를 이해·분석·생성하는 기계학습과, 최소한의 지도·확장성·해석 가능성을 연구한다고 소개한다. <https://cs.kaist.ac.kr/research/labView?sn=116&menu=64> 관측 2026-10-27.
[^faculty]: KAIST 전산학부, 홍승훈 교수 상세 소개. 직급·전공·학력·2019년 이후 KAIST 재직과 이전 경력·교수 연구실. <https://cs.kaist.ac.kr/people/view?idx=593&kind=faculty&menu=160> 관측 2026-10-30.
[^roster]: KAIST 전산학부 교수진 명단, 홍승훈 부교수 항목. <https://cs.kaist.ac.kr/people/faculty> 관측 2026-10-27.
[^members]: Vision and Learning Laboratory, 구성원 자료. 교수 1명, 대학원생·연구원 14명, 인턴 6명, 학위 졸업생 10명, 이전 인턴 11명, 방문 학생 4명. <https://vllab.kaist.ac.kr/api/data/members/index> 관측 2026-10-30.
[^pubs]: Vision and Learning Laboratory, 논문 목록. 최근 목록은 날짜의 연도를 기준으로 하고 저자·제목·발표처 표기는 연구실 목록을 따른다. <https://vllab.kaist.ac.kr/api/data/publications/index> 관측 2026-10-30.
[^news]: Vision and Learning Laboratory, 소식 40건. 본문의 소식과 수상·선정은 게시일 2021-10-13–2026-10-13 기준이다. <https://vllab.kaist.ac.kr/api/data/news/index> 관측 2026-10-30.
[^home]: Vision and Learning Laboratory, 첫 화면 아래 연락·위치. <https://vllab.kaist.ac.kr/> 관측 2026-10-30.
[^ai]: KAIST 김재철AI대학원, 구성원 명단. 홍승훈을 전산학부 부교수로, 연구분야를 컴퓨터 비전·머신 러닝으로 적는다. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측 2026-10-30.
[^ct]: M. Seo 외, S. Kwak, WACV 2021, 3972–3981. <https://doi.org/10.1109/wacv48630.2021.00402> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=5&select=id,doi,title,publication_year,primary_location,authorships,abstract_inverted_index&search=Neural%20Contrast%20Enhancement%20of%20CT%20Image>. 관측 2026-10-30.

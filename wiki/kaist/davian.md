# DAVIAN

**KAIST 김재철AI대학원 · 주재걸 교수**

- 분야: 기계학습, 시각 자료 생성·인식, 3차원 표현, 자연어 처리, 언어 모델, 강화학습, 시계열 분석, 모델 효율·적응, 설명 가능한 인공지능, 데이터 시각화, 의료 영상 처리
- 대분야: 컴퓨팅·AI
- 태그: 생성 인공지능[^generative], 대형 언어 모델[^nlp], 자연어 처리·계산언어학[^nlp], 강화학습[^rl], 시계열 분석·예측[^timeseries], 데이터 시각화·시각적 분석[^visualization], 책임 있는 AI·공정성[^trust], 설명 가능한 AI(XAI)[^trust]
- 홈페이지: <https://davian.kaist.ac.kr/>
- 근거와 출처: [DAVIAN 근거 페이지](davian-sources.md)

> 이미지·영상과 언어를 다루는 인공지능을 만들고, 그 결과를 사람이 이해하고 조절할 수 있게 하는 방법을 연구한다.[^home][^nlp][^visualization]

## 무엇을 연구하나

DAVIAN은 주재걸 교수가 이끄는 연구실이다. 기계학습(자료에서 규칙과 관계를 찾아 예측이나 판단 방법을 학습하는 분야)을 바탕으로 이미지·영상 생성, 언어 처리, 로봇의 행동 학습, 자료 분석을 연구한다. 신경망은 연결된 계산 단위들이 입력을 변환하고 학습으로 연결의 강도를 조절하는 계산 모형이다. 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야)도 주요 방법이며, 층은 입력에 일정한 변환을 적용하여 다음 단계로 전달하는 계산 단위의 묶음이다.[^home][^research]

시각 자료 연구에서는 생성 모델(학습한 자료의 구조와 특성을 이용해 새로운 자료를 만드는 계산 모형)의 품질과 조절 가능성을 높인다. 사람이 지정한 조건에 맞춰 이미지와 영상을 만들고 편집하며, 가상으로 옷을 입혀 보는 방법도 개발한다.[^generative] 확산 모델(자료에 잡음을 더하는 과정과 이를 되돌리는 과정을 학습해 새 자료를 만드는 생성 모델)을 영상의 생성·조절에 사용하는 연구가 이 갈래에 들어간다.[^generative] 잡음은 원하는 정보와 관계없이 자료에 섞이는 변동 성분이다. 영상 속 물체를 찾거나 영역별로 구분하는 방법과 입체 정보를 이용해 영상을 그리는 방법도 연구하며, 학습 자료와 다른 환경에서 인식 성능을 유지하는 문제를 다룬다.[^recognition]

언어 연구에서는 자연어 처리(Natural Language Processing, 사람이 쓰는 언어를 계산으로 분석·이해·생성하는 분야)와 대형 언어 모델(Large Language Model, 많은 언어 자료로 학습하여 글을 이해하고 생성하는 큰 계산 모형)을 다룬다. 번역·대화뿐 아니라 문서를 편집하는 에이전트(주어진 목표에 따라 정보를 처리하고 행동을 선택하는 프로그램), 특정 대상에 관한 지식을 지우는 방법, 그림과 글을 함께 다루는 모델을 개발한다.[^nlp]

행동과 시간 변화도 연구 대상이다. 강화학습(행동 결과에 주어지는 평가값을 이용해 장기적인 성과가 커지도록 행동을 학습하는 방법)의 계산 규모를 늘릴 수 있는 구조를 만들고 로봇 조작에 연결한다.[^rl] 시계열(시간 순서에 따라 관측한 자료)의 예측과 이상 탐지(평소와 다른 값이나 변화를 찾는 일)에서는 학습할 때와 사용할 때 자료의 성질이 달라져도 신뢰성을 유지할 수 있는 방법을 개발한다.[^timeseries]

결과를 사람이 이해하고 고칠 수 있게 하는 것도 중요한 축이다. 모델의 판단을 해석 가능한 개념으로 설명하고 자료와 생성 모델의 편향을 줄인다.[^trust] 편향은 자료나 판단에 특정 경향이 체계적으로 치우치는 현상이다. 사람이 자료의 구조를 그림으로 살피고 조작하는 시각적 분석 시스템도 만든다.[^visualization] 의료 응용에서는 영상의 주요 지점을 사용자가 수정하는 방법과 제한된 X선 영상으로 단층 영상(몸속 단면을 찍은 영상)을 재구성하는 방법을 개발한다.[^medical][^med-methods][^p8]

## 주요 연구 주제

### 이미지·영상 생성과 의료 영상 처리

생성 결과의 세부와 구조를 보존하면서 사용자가 원하는 내용으로 바꾸는 방법을 연구한다.[^generative] 예를 들어 StableVITON은 옷과 신체 사이의 의미상 대응을 학습해 옷의 세부를 가상 착용 결과에 반영한다.[^p2] 의료 영상에서는 원근 투영(같은 크기의 물체라도 거리에 따라 영상에서 차지하는 크기가 달라지도록 공간을 평면에 나타내는 방식)을 반영한 단층 영상 재구성을 제안했다.[^p8]

### 언어 모델과 에이전트의 안전성

언어 모델을 번역·대화·문서 편집에 쓰는 방법과 모델에 남은 특정 지식을 제거하는 방법을 연구한다.[^nlp] Opt-Out은 특정 대상 전체에 관한 지식을 지우면서 다른 기능을 유지하는 문제를 다룬다.[^p3] Membrane은 해로운 요청을 막는 조건과 겉보기에 비슷한 정상 요청을 허용하는 조건을 함께 기억하여 새로운 공격에 대응하도록 설계했다.[^p1]

### 강화학습의 확장과 시계열의 변화 대응

강화학습에서는 모델의 규모를 키울 때 학습 효율도 높아질 수 있는 계산 구조를 연구한다.[^rl] SimBa는 입력과 중간 특징(자료의 성질을 구별할 수 있게 나타낸 정보)의 크기를 조절하고 입력에서 출력으로 이어지는 선형 경로를 제공한다.[^p4] 선형은 입력의 합과 배수에 대해 출력도 같은 합과 배수로 변하는 성질이다. 시계열에서는 정상 자료의 성질이 시간에 따라 바뀌는 문제를 다루며, 실제로 예측하는 중에도 그 변화를 학습하여 이상 탐지를 조정한다.[^timeseries][^p6] 큰 모델을 실제로 쓰기 위해 일부 변수만 조정하는 학습, 다른 모델의 지식을 옮기는 학습, 모델의 일부 요소를 덜어내거나 수치의 표현을 바꾸는 방법도 연구한다. 이미 학습한 모델을 새로운 자료와 과제에 맞추는 방법을 함께 다룬다.[^efficient]

### 모델 설명·공정성과 사람 참여형 분석

해석 가능한 개념을 추출해 모델이 어떻게 판단하는지 살피고, 자료와 모델의 편향을 줄여 공정성과 신뢰성을 개선한다.[^trust] PatchSAE는 시각 모델의 개념과 그림 속 위치를 연결해 모델을 특정 과제에 맞출 때 무엇이 달라지는지 분석한다.[^p5] DASH는 사람이 시각적으로 편향 요인을 찾고 합성 이미지를 만들어 분류 모델의 학습을 조정하는 분석 시스템이다.[^visualization][^p7]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문 가운데 생성, 언어 모델, 강화학습, 모델 설명, 시계열, 시각적 분석, 의료 영상의 갈래를 고르게 골랐다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다. 교수의 참여는 저자 순서로 표시한다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자와 교수 참여 |
|---|---|---|---|---|
| 1 | 2026 | [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://doi.org/10.18653/2026.emnlp-main.2651) · EMNLP 2026 (채택) | 해로운 요청과 겉보기에 비슷한 정상 요청을 함께 기억하는 안전 장치를 제안했다. 공격 방식별로 기억을 정리하고, 새 상호작용에서 얻은 정보를 추가 학습 없이 반영한다. 시험에서는 여섯 가지 공격 모두에서 가장 높은 F1을 기록했고, 정상 요청을 거절하는 비율도 기존 방어 장치보다 크게 낮았다.[^p1] | 1저자 Minseok Choi, 주재걸은 8명 중 7번째 저자 |
| 2 | 2024 | [StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On](https://doi.org/10.1109/cvpr52733.2024.00781) · CVPR 2024 | 옷 사진과 사람 사진으로 가상 착용 이미지를 만드는 방법이다. 학습된 확산 모델의 잠재 공간(자료의 주요 특징을 수치로 표현하는 공간) 안에서 옷과 신체의 대응을 학습한다. 대응 관계에 집중하는 계산과 옷의 세부를 보존하는 학습 기준을 결합해, 비교 방법보다 좋은 정성·정량 결과를 보였다.[^p2] | 1저자 Jeongho Kim, 마지막 저자 주재걸 |
| 3 | 2025 | [Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport](https://doi.org/10.18653/v1/2025.acl-long.1371) · ACL 2025 | 언어 모델에서 무작위 자료 몇 개를 지우는 문제를 넘어 특정 사람이나 대상과 관련된 지식 전체를 지우는 방법을 연구했다. 원래 모델과의 차이를 조절하는 최적 수송(분포 사이의 이동 비용을 최소화하는 대응을 구하는 수학적 방법)을 이용하고 평가 자료도 제시했다. 다른 기능을 유지하면서 대상을 잊는 실험에서 기존 방법보다 나았다.[^p3] | 1저자 Minseok Choi, 마지막 저자 주재걸 |
| 4 | 2025 | [SimBa: Simplicity Bias for Scaling Up Parameters in Deep Reinforcement Learning](https://doi.org/10.48550/arxiv.2410.09754) · ICLR 2025, 설명은 연결된 arXiv 판 | 강화학습 모델의 규모를 키우면서도 일반화(학습하지 않은 자료나 상황에도 배운 규칙을 적용하는 성질)를 돕는 계산 구조를 제안했다. 입력의 통계를 맞추는 층, 입력에서 출력으로 선형 경로를 제공하는 잔차 블록(입력 일부를 변환 결과에 더해 전달하는 계산 묶음), 중간 특징의 크기를 조절하는 층을 결합했다. 여러 강화학습 방법에서 같은 자료량으로 얻는 학습 효율을 높였다.[^p4] | 1저자 Hojoon Lee, 주재걸은 10명 중 8번째 저자 |
| 5 | 2025 | [Sparse Autoencoders Reveal Selective Remapping of Visual Concepts during Adaptation](https://doi.org/10.48550/arxiv.2412.05276) · ICLR 2025, 설명은 연결된 arXiv 판 | PatchSAE라는 희소 자동부호기(입력을 압축했다 복원하도록 배우며 일부 표현만 활성화되도록 하는 신경망)를 만들어 시각 모델의 모양·색·의미 개념과 영상 속 위치를 뽑았다. 모델을 특정 과제에 맞추는 과정에서 개념과 출력의 관계가 어떻게 달라지는지 분석했다. 시험한 적응 과제의 성능 향상은 상당 부분 원래 모델에 이미 있던 개념으로 설명되었다.[^p5] | 1저자 Hyesu Lim, 주재걸은 4명 중 3번째 저자 |
| 6 | 2024 | [When Model Meets New Normals: Test-time Adaptation for Unsupervised Time-series Anomaly Detection](https://doi.org/10.1609/aaai.v38i12.29210) · AAAI 2024 | 정상적인 시계열의 성질이 바뀌면 이전에 배운 이상 탐지 기준이 맞지 않을 수 있다. 이를 해결하려고 추세를 추정하고 자료 자체에서 학습 신호를 얻는 방법으로, 실제 사용하는 중에 새 정상 상태를 학습하도록 했다. 실제 자료의 평가에서 기존 이상 탐지기의 성능과 자료 변화에 대한 대응이 개선되었다.[^p6] | 1저자 Dongmin Kim, 마지막 저자 주재걸 |
| 7 | 2022 | [DASH: Visual Analytics for Debiasing Image Classification via User-Driven Synthetic Data Augmentation](https://doi.org/10.2312/evs.20221099) · EuroVis 2022 Short Paper | 이미지 분류기가 판단과 무관한 특징의 동시 출현에 기대는 편향을 사람이 찾고 줄이도록 했다. 사람은 시각적 분석 화면에서 편향 요인을 확인하고 합성 이미지를 반복해 만든 뒤 모델 학습을 조정한다. 정량 평가와 사용자 연구에서 시스템의 유용성을 보였다.[^p7] | 1저자 Bum Chul Kwon, 마지막 저자 주재걸 |
| 8 | 2023 | [Perspective Projection-Based 3D CT Reconstruction from Biplanar X-rays](https://doi.org/10.1109/icassp49357.2023.10096296) · ICASSP 2023 | 서로 직각인 방향의 X선 영상에서 입체 단층 영상을 만드는 PerX2CT를 제안했다. 원근 투영을 반영하고 공간의 좌표마다 다른 국소·전체 특징을 결합해 입체 위치 정보를 얻도록 한다. 선택한 부분을 높은 해상도(영상에서 구별할 수 있는 공간적 세부의 정도)로 재구성할 가능성을 보였고, 여러 지표에서 비교 방법보다 나았다. 임상 응용은 가능성으로 제시했다.[^p8] | 공동 1저자 Daeun Kyung·Kyungmin Jo(공동 기여, 누리집 표기), 주재걸은 5명 중 3번째 저자 |

## 교수와 전문 분야

주재걸 교수(Jaegul Choo)는 KAIST 김재철AI대학원 교수다. 2020–2025년에는 같은 대학원 부교수로 재직했고, 그전에는 고려대학교 컴퓨터학과·인공지능학과에서 일했다. 조지아공과대학교에서 2009년 석사와 2013년 박사 학위를 받았으며 서울대학교에서 학사 학위를 받았다.[^dept][^bio]

대학원은 전문 분야를 컴퓨터 비전, 자연어 처리, 데이터 시각화 분석으로 소개한다.[^dept] 최근 논문으로 보면 옷과 사람의 대응을 이용한 이미지 생성, 언어 모델의 지식 제거와 안전성, 강화학습의 계산 구조, 사람이 개입하는 모델 해석·편향 개선을 함께 연구한다.[^p1][^p2][^p3][^p4][^p5][^p7]

## 응용 분야

대표 논문이 다룬 쓰임은 가상 의류 착용, 언어 모델의 정보 삭제와 안전 장치, 행동 학습, 변화하는 시계열의 이상 탐지, 사람이 자료 편향을 고치는 분석 화면이다.[^p1][^p2][^p3][^p4][^p6][^p7] 의료 영상 재구성은 제한된 촬영 방향으로 입체 정보를 얻는 계산 방법을 다루며, 임상 적용 가능성을 제시한다.[^p8]

## 구성원

2026년 11월 9일 People 쪽의 PostDoc 4명, Ph.D. 40명, M.S. 12명이다. 과정과 연구 주제는 게시 표기이며, 시작 칸의 Fall 2026은 연구실 소식의 합류 시기다.[^people][^news] 「대표 논문 참여」는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Junwoo Park | 박사후연구원 |  | Time Series, Game AI | junwoo.park@kaist.ac.kr |  |
| Minseok Choi | 박사후연구원 |  | LLM, AI Safety | minseok.choi@kaist.ac.kr | 1, 3 |
| Junha Hyung | 박사후연구원 |  | NeRF, GAN, 3D Synthesis | sharpeeee@kaist.ac.kr |  |
| Minho Park | 박사후연구원 |  | Robotics, Diffusion, RL | m.park@kaist.ac.kr |  |
| Daehoon Gwak | 박사과정 |  | Machine Learning | daehoon.gwak@kaist.ac.kr |  |
| Kangyeol Kim | 박사과정 |  | Computer Vision, Active Learning | kangyeolk@kaist.ac.kr |  |
| Hojun Cho | 박사과정 |  | Natural Language Generation, 3D Computer Vision | hojun.cho@kaist.ac.kr |  |
| Seunghwan Choi | 박사과정 |  | GAN, Image Translation, Image Disentangling | shadow2496@kaist.ac.kr |  |
| Byungkun Lee | 박사과정 |  | Reinforcement Learning | byungkun.lee@kaist.ac.kr |  |
| Jeonghoon Park | 박사과정 |  | Computer Vision, Safety of AI | jeonghoon_park@kaist.ac.kr |  |
| Taehee Kim | 박사과정 |  | Natural Language Processing, QA | taeheekim@kaist.ac.kr |  |
| Wonwoo Cho | 박사과정 |  | Computer Vision, Medical Image Analysis | wcho@kaist.ac.kr |  |
| Gyuhyeon Sim | 박사과정 |  | Computer Vision, Neural ODE, Medical Imaging | ghsim@kaist.ac.kr |  |
| Youngwoo Youn | 박사과정 |  | Machine Learning, Time Series Data Analysis | ywyoun@kaist.ac.kr |  |
| Yujin Baek | 박사과정 |  | Natural Language Processing, Neural Machine Translation | yujinbaek@kaist.ac.kr |  |
| Hyunseung Kim | 박사과정 |  | Reinforcement Learning | mynsng@kaist.ac.kr | 4 |
| Jimin Hong | 박사과정 |  | Natural Language Processing, AI Safety | jimmyh@kaist.ac.kr |  |
| Jooyeol Yun | 박사과정 |  | Computer Vision, Computational Photography | blizzard072@kaist.ac.kr |  |
| Dongyoon Hwang | 박사과정 |  | Reinforcement Learning | godnpeter@kaist.ac.kr | 4 |
| Min-Jung Kim | 박사과정 |  | Computer Vision | emjay73@kaist.ac.kr |  |
| Rodrigo Hormazabal | 박사과정 |  | Graph Representation Learning, Geometric Deep Learning, Molecular Design |  |  |
| Jaeseong Lee | 박사과정 |  | Computer Vision, Reenactment, Generative View Synthesis | wintermad1245@kaist.ac.kr |  |
| Seungil Lee | 박사과정 |  | Quantitative Trading, Natural Language Processing | silly5921@kaist.ac.kr |  |
| Youngjoo Jo | 박사과정 |  | Computer Vision, GAN, Video Generation | ghjk7979@kaist.ac.kr |  |
| Jinho Choi | 박사과정 |  | Computer Vision, Multimodal | jinhochoi@kaist.ac.kr | 5 |
| Sejik Park | 박사과정 |  | Reinforcement Learning, Computer Vision, Natural Language Processing | sejik.park@kaist.ac.kr |  |
| Kyungmin Lee | 박사과정 |  | GAN, Diffusion Model, Reinforcement Learning | kmlee@kaist.ac.kr |  |
| Dohyun Lee | 박사과정 |  | Natural Language Processing, Large Language Model | aiclaudev@kaist.ac.kr | 3 |
| Seungbin Yang | 박사과정 |  | Natural Language Processing | sby99@kaist.ac.kr | 1 |
| Taewoong Kang | 박사과정 |  | Computer Vision, Generative Models, 3D | keh0t0@kaist.ac.kr |  |
| Cheonbok Park | 박사과정 |  | Large Language Models, Generative Models, Machine Translation | cbok.park@kaist.ac.kr |  |
| Jaehyun Shim | 박사과정 |  | Data Analysis, LLM, LLM Agents | jaehyunshim@kaist.ac.kr |  |
| Jihwan Kim | 박사과정 |  | Computer Vision, Generative Models, Multimodal | jihvvan.kim@kaist.ac.kr |  |
| ChanHee Kang | 박사과정 |  | Generative Model, Neural Rendering, Neural Differential Equations | ducati@kaist.ac.kr |  |
| Dongjin Kim | 박사과정 |  | VLA, Multimodal | dj_kim@kaist.ac.kr |  |
| Hoiyeong Jin | 박사과정 |  | Computer Vision, Generative Models | hy.jin@kaist.ac.kr |  |
| Hyojin Jang | 박사과정 |  | Computer Vision, Video Diffusion Models, 3D Vision | wkdgywlsrud@kaist.ac.kr |  |
| Kinam Kim | 박사과정 |  | Computer Vision, Video Diffusion Models | kinamplify@kaist.ac.kr |  |
| Sibeen Kim | 박사과정 |  | Dexterous Manipulation | bioceo78@kaist.ac.kr |  |
| Yunseung Lee | 박사과정 |  | Domain Generalization, Debiasing, Multimodal | yunseung_lee@kaist.ac.kr | 1 |
| Hyeongjun Yun | 박사과정 |  | Recommendation System | hj.yun@kaist.ac.kr |  |
| Sangjun Park | 박사과정 |  | Medical AI, VLM, Generative Model | s_park@kaist.ac.kr |  |
| Seokju Yun | 박사과정 |  | LLM, RL, 3D/4D Generation | sj_yun@kaist.ac.kr |  |
| Seunghan Yang | 박사과정 | Fall 2026 | Always-on AI, Agentic AI, Physical AI | seunghan@kaist.ac.kr |  |
| Beomsoo Kim | 석사과정 |  | Representation Learning, Natural Language Processing | bombskim@kaist.ac.kr |  |
| Kyudan Jung | 석사과정 |  | Large Language Models, Audio Language Models, Knowledge Control | kyudan@kaist.ac.kr |  |
| Minwoo Lee | 석사과정 |  | Speech Representation Learning, Trustworthy AI | minwoo011015@kaist.ac.kr |  |
| Euijin Shin | 석사과정 |  | CV, Agentic AI, multimodal | ejshin0310@kaist.ac.kr |  |
| Jintae Park | 석사과정 |  | Agentic AI, Multimodal | sonjt00@kaist.ac.kr |  |
| Jungwoo Ahn | 석사과정 |  | Generative Models, Computer Vision, Physical AI | jungwooahn@kaist.ac.kr |  |
| Junyeong Ahn | 석사과정 |  | Computer Vision, Generative Models, 3D Vision | justinahn@kaist.ac.kr |  |
| Minseo Jung | 석사과정 |  | LLM, Diffusion | minseo.jung@kaist.ac.kr |  |
| Geon Tack Lee | 석사과정 | Fall 2026 | Efficient AI, CV | geontack@kaist.ac.kr |  |
| Jiheon Kim | 석사과정 | Fall 2026 | Large Language Model, Agentic AI, VLM | ben8169@kaist.ac.kr |  |
| Serin Chang | 석사과정 | Fall 2026 | LLM, Physical AI, Agentic AI | serinchang@kaist.ac.kr |  |
| Yoonsang Oh | 석사과정 | Fall 2026 | Robot Learning, Reinforcement Learning | 5yoondori@kaist.ac.kr |  |

## 졸업생과 이전 구성원

People 쪽 Alumni의 68명이다. Ph.D. 24명, M.S. 43명, Post-Docs 1명이며, 게시된 종료 시기는 2018–2026년이다. 교수의 KAIST 부임 전 이전 소속 시기 구성원도 포함한다. 학위·시기·진로는 연구실 표기다.[^people][^bio]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Junha Song | Ph.D. (August 2026) |  |
| Sanghyeon Lee | Ph.D. (August 2026) |  |
| Sungwon Hwang | Ph.D. (August 2026) |  |
| Youngwoo Cho | Ph.D. (August 2026) |  |
| Daniel Rim | Ph.D. (February 2026) | Senior Research Engineer at Hyundai Motor Company |
| Hojoon Lee | Ph.D. (February 2026) | Holiday Robotics |
| Hyesu Lim | Ph.D. (February 2026) | Postdoctoral researcher at Helmholtz Munich |
| Jeongho Kim | Ph.D. (February 2026) | Qualcomm AI Research |
| Min-Cheol Sagong | Ph.D. (February 2026) | Assistant Professor at Kangwon National University |
| Soyoung Yang | Ph.D. (February 2026) | Samsung AI Center |
| Kyungmin Jo | Ph.D. (August 2025) |  |
| ChaeHun Park | Ph.D. (February 2025) | Assistant Professor at Chonnam National University |
| Chaeyeon Chung | Ph.D. (February 2025) | NVIDIA |
| Gyumin Shim | Ph.D. (February 2025) | Samsung Electronics |
| Seohyun Back | Ph.D. (February 2025) | Samsung Research |
| Taesung Kim | Ph.D. (February 2025) | Upstage |
| Chung Park | Ph.D. (August 2024) | SK Telecom |
| Jinhee Kim | Ph.D. (August 2024) | Samsung Research |
| Jungsoo Lee | Ph.D. (February 2024) | Qualcomm AI Research |
| Sunghyun Park | Ph.D. (February 2024) | Qualcomm AI Research |
| Sungha Choi | Ph.D. (February 2022) | Assistant Professor at Kyung Hee University |
| Kyeongpil Kang | Ph.D. (February 2021) | Scatter Lab |
| Mohammad Azam Khan | Ph.D. (February 2020) | Associate Professor at Daffodil International University, Bangladesh |
| Minsuk Choi | Ph.D. (August 2019) | Samsung Research |
| Youngdo Lee | M.S. (August 2026) |  |
| Donghu Kim | M.S. (February 2026) | Holiday Robotics |
| Dongjae Lee | M.S. (February 2025) | Naver Corp. |
| Donghyun Kim | M.S. (August 2024) | Naver Corp. |
| Dongmin Choi | M.S. (February 2024) | Saige Research |
| Gyojung Gu | M.S. (February 2024) | Fliption |
| Koanho Lee | M.S. (February 2024) | Samsung Advanced Institute of Technology |
| Dohee Kim | M.S. (August 2023) | Bering Lab |
| Dongmin Kim | M.S. (August 2023) | LG AI Research |
| Huiwon Yun | M.S. (August 2023) | Kakao Brain |
| Junui Hong | M.S. (August 2023) | SK Telecom |
| Munkhsoyol Ganbat | M.S. (August 2023) | Nestyle Inc. |
| Yeojeong Park | M.S. (August 2023) | Korea Telecom |
| Daejin Kim | M.S. (February 2023) | Scatter Lab |
| Youngin Cho | M.S. (February 2023) | NCSOFT Corp. |
| Minsoo Lee | M.S. (August 2022) | LG AI Research |
| Sanghun Jung | M.S. (August 2022) | University of Washington |
| Taewoo Kim | M.S. (August 2022) | Neosapience |
| Jihyeon Lee | M.S. (February 2022) | Kakao Brain |
| Eungyeup Kim | M.S. (August 2021) | Carnegie Mellon University |
| Juntae Kim | M.S. (August 2021) | Datarize |
| Hyoungwoo Lee | M.S. (February 2021) | Korea Telecom |
| Junsoo Lee | M.S. (February 2021) | Naver Webtoon |
| Kibeom Kim | M.S. (February 2021) | Samsung Electronics |
| Wooyoung Kim | M.S. (February 2021) | SK Telecom |
| Yonggyu Kim | M.S. (February 2021) | Kakao Brain |
| Yongjang Jo | M.S. (February 2021) | Mediaiplus Inc. |
| Yunwon Tae | M.S. (February 2021) | Vuno Inc. |
| Sanghyeon Na | M.S. (August 2020) | Kakao Brain |
| SeungJoo Yoo | M.S. (August 2020) | Carnegie Mellon University |
| Hyojin Bahng | M.S. (February 2020) | MIT |
| Seongjae Choi | M.S. (February 2020) | Naver Corp. |
| Sunwoong Lee | M.S. (February 2020) | Angleswing |
| Wonwoong Cho | M.S. (February 2020) | Purdue University |
| David Keetae Park | M.S. (August 2019) | Columbia University |
| Sunghyo Chung | M.S. (August 2019) | Kakao Corp. |
| Jurim Lee | M.S. (February 2019) | SK Telecom |
| Sungbok Shin | M.S. (February 2019) | University of Maryland |
| Taehun Kim | M.S. (February 2019) | Samsung Electronics |
| Jisu Leem | M.S. (August 2018) | Ruyi Corp. |
| Minje Choi | M.S. (August 2018) | University of Michigan |
| Minjeong Kim | M.S. (August 2018) | Upstage |
| Yunjey Choi | M.S. (August 2018) | Naver Corp. |
| Sanghoon Lee | Post-Docs (August 2026) | Postdoc at UNIST |

## 최근 논문 목록 (2021–2026)

연구실 Publication 쪽의 2021–2026년 연도 구역 논문 165편이다. 제목·저자·발표처는 연구실 표기이며 저자 이름 뒤 별표도 게시 기호다. 소식에서 학회 채택을 알린 2026년 논문은 「채택」으로 표시했다. DOI는 논문 식별자다.[^pubs][^news]

**2026**

- Minseok Choi, Seungbin Yang, Dongjin Kim, Subin Kim, Jungmin Son, Yunseung Lee, Jaegul Choo, and Youngjun Kwak. "Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense". *EMNLP · Conference on Empirical Methods in Natural Language Processing (채택) · DOI: 10.18653/2026.emnlp-main.2651*.
- Parsa Esmati, Junha Hyung, Amirhossein Dadashzadeh, Jaegul Choo, Majid Mirmehdi. "Probability-Conserving Flow Guidance". *NeurIPS · Conference on Neural Information Processing Systems (채택)*.
- Hyeongjun Yun, Taesan Kim, Dongjoon Hong, Junui Hong, Jihoon Oh, Kijung Park, MinCheol Cho, Kihyuk Song, Jaegul Choo, Chung Park. "CURE: Coupled User-Grouped Reinforcement Learning for Cross-Domain Recommendation with Non-Overlapping Users". *NeurIPS · Conference on Neural Information Processing Systems (채택)*.
- Kyungmin Lee\*, Sibeen Kim\*, Youngdo Lee, Minho Park, Hyunseung Kim, Dongyoon Hwang, Donghu Kim, Hojoon Lee, Jaegul Choo. "PHUMA: Physically Reliable Humanoid Locomotion Dataset". *CoRL · Conference on Robot Learning · Spotlight (채택)*.
- Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo, Yasuyuki Matsushita. "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement". *CoRL · Conference on Robot Learning (채택)*.
- Dohyun Lee\*, Minho Park\*, Jeonghoon Park, Dongyoon Hwang, Junha Hyung, Sungwon Hwang, Byungkun Lee, Jaegul Choo. "Procedural Memory for Proactive Robot Assistance". *CoRL · Conference on Robot Learning (채택)*.
- Hyeongjun Yun, Kihyuk Song, Jaegul Choo, and Chung Park. "A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain Sequential Recommendation". *CIKM · ACM International Conference on Information and Knowledge Management (채택)*.
- Yongyi Ji, Fuxiang Chen, Jaegul Choo, seung-won hwang, and Lu Liu. "Unveiling Sentiment Representations in Code-LLMs". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP (채택) · DOI: 10.18653/2026.findings-emnlp.443*.
- Cheonbok Park, Jihwan Kim, Shinyoung Joo, Joosung Lee, Hwiyeol Jo, Jeonghoon Kim, and Jaegul Choo. "From Unverifiable Domain Text to Cross-Lingual RLVR via Code-Switched Task Synthesis". *EMNLP · Conference on Empirical Methods in Natural Language Processing (채택)*.
- Youngwoo Cho, Semin Joung, Jaemin Seo, Young-chul Ghim, and Jaegul Choo. "Data-driven Plasma Equilibrium Forecasting in Magnetic Fusion Tokamak". *KDD · ACM SIGKDD International Conference on Knowledge Discovery and Data Mining · AI4Sciences Track (채택) · DOI: 10.1145/3770855.3818830*.
- Junha Song, Byeongho Heo, Geonmo Gu, Jaegul Choo, Dongyoon Han, Sangdoo Yun. "Learning to See What You Need: Gaze Attention for Multimodal Large Language Models". *COLM · Conference on Language Modeling (채택)*.
- Dongyoon Hwang\*, Byungkun Lee\*, Dongjin Kim\*, Hyojin Jang, Hoiyeong Jin, Jueun Mun, Minho Park, Hojoon Lee, Hyunseung Kim, Jaegul Choo. "3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance". *IROS · IEEE/RSJ International Conference on Intelligent Robots and Systems (채택)*.
- Jooyeol Yun, Jintae Park, Hyesu Lim, Junha Hyung, Hyungjin Chung, and Jaegul Choo. "ReDesign: Recovering Editable Design Structures from Raster Images via Agentic Decomposition". *ECCV · European Conference on Computer Vision (채택)*.
- Min-Jung Kim, Jeongho Kim, Hoiyeong Jin, Junha Hyung, and Jaegul Choo. "Infinite-Homography as Robust Conditioning for Camera-Controlled Video Generation". *ECCV · European Conference on Computer Vision (채택)*.
- Hoiyeong Jin, Hyojin Jang, Junha Hyung, Jeongho Kim, Kinam Kim, Dongjin Kim, Huijin choi, Hyeonji Kim, and Jaegul Choo. "InsertAnywhere: Geometrically Grounded and Optics-Aware Video Object Insertion". *ECCV · European Conference on Computer Vision (채택)*.
- Geon Tack Lee, Jaegul Choo, and Kang Eun Jeon. "Denoised Variance-Based Pruning with Optimal Brain Bias Compensation". *ECCV · European Conference on Computer Vision (채택)*.
- Seokhoon Moon, Kyudan Jung, and Jaegul Choo. "SLICE: Speech Enhancement via Layer-wise Injection of Conditioning Embeddings". *InterSpeech · Conference of the International Speech Communication Association (채택)*.
- Donghu Kim, Youngdo Lee, Hojoon Lee, Johan Obando-Ceron, Byungkun Lee, Aaron Courville, Pablo Samuel Castro, Jaegul Choo, and Clare Lyle. "V-Simba: Unleashing the Architectural Potential of RL in Visual Continuous Control". *RLC · Reinforcement Learning Conference (채택)*.
- Daehoon Gwak, Minhyung Lee, Junwoo Park, and Jaegul Choo. "Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques". *IJCAI · International Joint Conference on Artificial Intelligence · Survey-Track Paper (채택)*.
- Donghu Kim, Youngdo Lee, Minho Park, Kinam Kim, Takuma Seno, I Made Aswin Nahrendra, Sehee Min, Daniel Palenicek, Florian Vogt, Danica Kragic, Jan Peters, Jaegul Choo, Hojoon Lee. "FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control". *RSS · Robotics Science and Systems (채택)*.
- Youngwoo Cho\*, Jaekak Yoo\*, Soyoung Yang, Dong-Joon Yi, Seung Mi Lee, Mun Seok Jeong, Jaegul Choo. "Position: Significant impact of numerical precision in scientific machine learning". *ICML · International Conference on Machine Learning · Position Track (채택)*.
- Kyudan Jung, Jihwan Kim, Soyoon Kim, Jeonghoon Kim, Jaegul Choo, and Cheonbok Park. "Sommelier: Scalable Open Multi-turn Audio Pre-processing for Full-duplex Speech Language Models". *ACL · Annual Meeting of the Association for Computational Linguistics · Industry-Track Paper (채택)*.
- Taehee Kim\*, Seungbin Yang\*, Jihwan Kim, Jaegul Choo. "Retrieve Only Relevant Tables Whether Few or Many: Adaptive Table Retrieval Method". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL (채택) · DOI: 10.18653/v1/2026.findings-acl.635*.
- Kyudan Jung, Hojun Cho, Jooyeol Yun, Soyoung Yang, Jaehyeok Jang, Jaegul Choo. "Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL (채택) · DOI: 10.18653/v1/2026.findings-acl.166*.
- Yunseung Lee, Subin Kim, Youngjun Kwak, and Jaegul Choo. "BankMathBench: A Benchmark for Numerical Reasoning in Banking Scenarios". *LREC · Language Resources and Evaluation Conference (채택)*.
- Seunghwan Choi, Jooyeol Yun, Youngdo Lee, Jaegul Choo. "Selectively Extracting and Injecting Visual Attributes into Text-to-Image Models". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Taewoong Kang\*, Hyojin Jang\*, Sohyun Jeong\*, Seunggi Moon, Gihwi Kim, Hoon Jin Jung, Jaegul Choo. "AHS: Adaptive Head Synthesis via Synthetic Data Augmentations". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Taewoong Kang\*, Kinam Kim\*, Dohyeon Kim\*, Minho Park, Junha Hyung, Jaegul Choo. "EgoX: Egocentric Video Generation from a Single Exocentric Video". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Jooyeol Yun, Jaegul Choo. "Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Sunghyun Park, Jeongho Kim, Hyoungwoo Park, Debasmit Das, Sungrack Yun, Munawar Hayat, Jaegul Choo, Fatih Porikli, Seokeon Choi. "Memory-Efficient Fine-Tuning Diffusion Transformer via Dynamic Patch Sampling and Block Skipping". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Sanghyeon Lee, Minwoo Lee, Euijin Shin, Kangyeol Kim, Seunghwan Choi, Jaegul Choo. "OPRO: Orthogonal Panel-Relative Operators for Panel-Aware In-Context Image Generation". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Minho Park, Sunghyun Park, Jungsoo Lee, Hyojin Park, Kyuwoong Hwang, Fatih Porikli, Jaegul Choo, Sungha Choi. "CA-LoRA: Concept-Aware LoRA for Domain-Aligned Segmentation Dataset Generation". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Junha Song, Yongsik Jo, So Yeon Min, Quanting Xie, Taehwan Kim, Yonatan Bisk, Jaegul Choo. "MM-SeR: Multimodal Self-Refinement for Lightweight Image Captioning". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition (채택)*.
- Minho Park\*, Kinam Kim\*, Junha Hyung, Hyojin Jang, Hoiyeong Jin, Jooyeol Yun, Hojoon Lee, Jaegul Choo. "ACG: Action Coherence Guidance for Flow-Based Vision-Language-Action Models". *ICRA · IEEE International Conference on Robotics & Automation (채택)*.
- Jaeseong Lee\*, Junyeong Ahn\*, Taewoong Kang, Jaegul Choo. "TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars". *3DV · International Conference on 3D Vision (채택)*.
- Youngwoo Cho\*, Seunghoon Yi\*, Wooil Yang, Sungmo Kang, Young-woo Son, Jaegul Choo, Joonseok Lee, Soo Kyung Kim, Hongkee Yoon. "Robust and Interpretable Adaptation of Equivariant Materials Foundation Models via Sparsity-promoting Fine-tuning". *ICLR · International Conference on Learning Representations (채택)*.
- Seungbin Yang\*, Jihwan Kim\*, Jaemin Choi, Dongjin Kim, Soyoung Yang, ChaeHun Park, Jaegul Choo. "LiveWeb-IE: A Benchmark For Online Web Information Extraction". *ICLR · International Conference on Learning Representations (채택)*.
- Minseok Choi\*, Dongjin Kim\*, Seungbin Yang\*, Subin Kim, Youngjun Kwak, Juyoung Oh, Jaegul Choo, Jungmin Son. "ExpGuard: LLM Content Moderation in Specialized Domains". *ICLR · International Conference on Learning Representations (채택)*.
- Junha Song, Sangdoo Yun, Dongyoon Han, Jaegul Choo, Byeongho Heo. "RL makes MLLMs see better than SFT". *ICLR · International Conference on Learning Representations (채택)*.
- Chung Park, Hyeongjun Yun, Taesan Kim, Junui Hong, Dongjoon Hong, Mira Myong, Jihoon Oh, MinCheol Cho, Kijung Park, Min sung Choi, Jihwan Seok, Jaegul Choo. "More Than What Was Chosen: LLM-based Explainable Recommendation Beyond Noisy User Preferences". *ICLR · International Conference on Learning Representations (채택)*.
- Minho Park, Taewoong Kang, Jooyeol Yun, Sungwon Hwang, and Jaegul Choo. "SphereDiff: Tuning-free 360° Static and Live Wallpaper Generation via Spherical Latent Representation". *AAAI · AAAI Conference on Artificial Intelligence · Oral (채택)*.
- Chung Park, Taesan Kim, Hyeongjun Yun, Dongjoon Hong, Junui Hong, Kijung Park, MinCheol Cho, Min sung Choi, Jihwan Seok, and Jaegul Choo. "Think Wise, Collaborate Effectively: A Rationale-Aware LLM-Based Recommender with Reinforcement Learning from Collaborative Signals". *AAAI · AAAI Conference on Artificial Intelligence · Oral (채택)*.

**2025**

- ChaeHun Park, Hojun Cho, and Jaegul Choo. "Evaluating Automatic Speech Recognition Systems for Korean Meteorological Experts". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of ACL · DOI: 10.18653/v1/2025.findings-emnlp.561*.
- Hojun Cho, Donghu Kim, Soyoung Yang, Chan Lee, Hunjoo Lee, and Jaegul Choo. "Building Resource-Constrained Language Agents: A Korean Case Study on Chemical Toxicity Information". *EMNLP · Conference on Empirical Methods in Natural Language Processing · DOI: 10.18653/v1/2025.emnlp-industry.191*.
- Daehoon Gwak,\* Minseo Jung,\* Junwoo Park, Minho Park, ChaeHun Park, Junha Hyung, and Jaegul Choo. "Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs". *EMNLP · Conference on Empirical Methods in Natural Language Processing · DOI: 10.18653/v1/2025.emnlp-main.1754*.
- Kinam Kim, Junha Hyung, and Jaegul Choo. "Temporal In‑Context Fine‑Tuning for Versatile Control of Video Diffusion Models". *NeurIPS · Conference on Neural Information Processing Systems*.
- Jinho Choi, Hyesu Lim, Steffen Schneider, and Jaegul Choo. "Characterizing Dataset Bias via Disentangled Visual Concepts". *NeurIPS · Conference on Neural Information Processing Systems*.
- Junwoo Park, Kyudan Jung, Dohyun Lee, Hyuck Lee, Daehoon Gwak, ChaeHun Park, Jaegul Choo, and Jaewoong Cho. "Delving into Large Language Models for Effective Time-Series Anomaly Detection". *NeurIPS · Conference on Neural Information Processing Systems*.
- Jeongho Kim,\* Hoiyeong Jin,\* Sunghyun Park, and Jaegul Choo. "PromptDresser: Improving the Quality and Controllability of Virtual Try-On via Generative Textual Prompt and Prompt-aware Mask". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51701.2025.01487*.
- Jeonghoon Park, Juyoung Lee, Chaeyeon Chung, Jaeseong Lee, Jaegul Choo, Jindong Gu. "Fair Generation without Unfair Distortions: Debiasing Text-to-Image Generation with Entanglement-Free Attention". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51701.2025.01632*.
- ChaeHun Park,\* Yujin Baek,\* Jaeseok Kim, Yu-Jung Heo, Du-Seong Chang, and Jaegul Choo. "Evaluating Visual and Cultural Interpretation: The K-Viscuit Benchmark with Human-VLM Collaboration". *ACL · Annual Meeting of the Association for Computational Linguistics · DOI: 10.18653/v1/2025.acl-long.1066*.
- Minseok Choi, Daniel Rim, Dohyun Lee, and Jaegul Choo. "Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport". *ACL · Annual Meeting of the Association for Computational Linguistics · DOI: 10.18653/v1/2025.acl-long.1371*.
- Junwoo Park, Hyuck Lee, Dohyun Lee, Daehoon Gwak, and Jaegul Choo. "Revisiting LLMs as Zero-Shot Time Series Forecasters: Small Noise Can Break Large Models". *ACL · Annual Meeting of the Association for Computational Linguistics · Short Paper · DOI: 10.18653/v1/2025.acl-short.71*.
- Dohyun Lee, Seungil Chad Lee, Chanwoo Yang, Yujin Baek, and Jaegul Choo. "Exploring In-context Example Generation for Machine Translation". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL · DOI: 10.18653/v1/2025.findings-acl.1362*.
- Daniel Rim, Minsoo Cho, Changwoo Chun, and Jaegul Choo. "To Chat or Task: a Multi-turn Dialogue Generation Framework for Task-Oriented Dialogue Systems". *ACL · Annual Meeting of the Association for Computational Linguistics · Industry-Track Paper · Oral · DOI: 10.18653/v1/2025.acl-industry.41*.
- Hojoon Lee,\* Youngdo Lee,\* Takuma Seno, Donghu Kim, Peter Stone, and Jaegul Choo. "Hyperspherical Normalization for Scalable Deep Reinforcement Learning". *ICML · International Conference on Machine Learning · Spotlight*.
- Kyungmin Jo, Jooyeol Yun, and Jaegul Choo. "Devil is in the Detail: Towards Injecting Fine Details of Image Prompt in Image Generation via Conflict-free Guidance and Stratified Attention". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52734.2025.02197*.
- Sohyun Jeong, Taewoong Kang, Hyojin Jang, and Jaegul Choo. "Zero-Shot Head Swapping in Real-World Scenarios". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52734.2025.01009*.
- Junha Hyung, Kinam Kim, Susung Hong, Min-Jung Kim, and Jaegul Choo. "Spatiotemporal Skip Guidance for Enhanced Video Diffusion Sampling". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52734.2025.01028*.
- Soyoung Yang, Hojun Cho, Jiyoung Lee, Sohee Yoon, Edward Choi, Jaegul Choo, and Won Ik Cho. "Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation". *NAACL · Annual Conference of the North American Chapter of the Association for Computational Linguistics · DOI: 10.18653/v1/2025.naacl-long.603*.
- Jaeseong Lee, Taewoong Kang, Marcel Buehler, Min-Jung Kim, Sungwon Hwang, Junha Hyung, Hyojin Jang, and Jaegul Choo. "SurFhead: Affine Rig Blending for Geometrically Accurate 2D Gaussian Surfel Head Avatars". *ICLR · International Conference on Learning Representations*.
- Hyesu Lim, Jinho Choi, Jaegul Choo, and Steffen Schneider. "Sparse Autoencoders Reveal Selective Remapping of Visual Concepts during Adaptation". *ICLR · International Conference on Learning Representations*.
- Hojoon Lee, Dongyoon Hwang, Donghu Kim, Hyunseung Kim, Jun Jet Tai, Kaushik Subramanian, Peter R. Wurman, Jaegul Choo, Peter Stone, and Takuma Seno. "SimBa: Simplicity Bias for Scaling Up Parameters in Deep Reinforcement Learning". *ICLR · International Conference on Learning Representations · Spotlight*.
- Chaeyeon Chung, Sunghyun Park, Jeongho Kim, and Jaegul Choo. "What to Preserve and What to Transfer: Faithful, Identity-Preserving Diffusion-based Hairstyle Transfer". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v39i3.32261*.
- Sanghyeon Lee, Jooyeol Yun, and Jaegul Choo. "Enabling Region-Specific Control via Lassos in Point-Based Colorization". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v39i5.32479*.
- Seunghwan Choi, Jooyeol Yun, Jeonghoon Park, and Jaegul Choo. "Disentangling Subject-Irrelevant Elements against Subject in Personalized Text-to-Image Diffusion via Filtered Self-distillation". *WACV · Winter Conference on Applications of Computer Vision*.
- Kyungmin Jo and Jaegul Choo. "Skip-and-Play: Depth-Driven Pose-Preserved Image Generation for Any Objects". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv61041.2025.00077*.
- Jinhee Kim,\* Taesung Kim,\* Taewoo Kim, Dong-Wook Kim, Byungduk Ahn, Yoon-Ji Kim, In-Seok Song, and Jaegul Choo. "Attend-and-Refine: Interactive Keypoint Estimation and Quantitative Cervical Vertebrae Analysis for Bone Age Assessment". *· DOI: 10.1016/j.media.2025.103715*.

**2024**

- Jinhee Kim,\* Taesung Kim,\* and Jaegul Choo. "EPIC: Effective Prompting for Imbalanced-Class Data Synthesis in Tabular Data Classification via Large Language Models". *NeurIPS · Conference on Neural Information Processing Systems · DOI: 10.52202/079017-0990*.
- Hyunseung Kim, Byungkun Lee, Hojoon Lee, Dongyoon Hwang, Donghu Kim, and Jaegul Choo. "Do's and Don'ts: Learning Desirable Skills with Instruction Videos". *NeurIPS · Conference on Neural Information Processing Systems · DOI: 10.52202/079017-1512*.
- Junha Hyung, Susung Hong, Sungwon Hwang, Jaeseong Lee, Jaegul Choo, and Jin-Hwa Kim. "Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting". *NeurIPS · Conference on Neural Information Processing Systems · DOI: 10.52202/079017-3505*.
- Changdae Oh,\* Hyesu Lim,\* Mijoo Kim, Dongyoon Han, Sangdoo Yun, Jaegul Choo, Alexander G Hauptmann, Zhi-Qi Cheng, and Kyungwoo Song. "Towards Calibrated Robust Fine-Tuning of Vision-Language Models". *NeurIPS · Conference on Neural Information Processing Systems · DOI: 10.52202/079017-0403*.
- Minseok Choi, Kyunghyun Min, and Jaegul Choo. "Cross-Lingual Unlearning of Selective Knowledge in Multilingual Language Models". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · DOI: 10.18653/v1/2024.findings-emnlp.630*.
- Daehoon Gwak,\* Junwoo Park,\* Minho Park, ChaeHun Park, Hyunchan Lee, Edward Choi, and Jaegul Choo. "Forecasting Future International Events: A Reliable Dataset for Text-Based Event Modeling". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · DOI: 10.18653/v1/2024.findings-emnlp.526*.
- Wonwoo Cho, Kangyeol Kim, Saemee Choi, and Jaegul Choo. "Training Spatial-Frequency Visual Prompts and Probabilistic Clusters for Accurate Black-Box Transfer Learning". *MM · ACM International Conference on Multimedia · DOI: 10.1145/3664647.3680955*.
- ChaeHun Park, Minseok Choi, Dohyun Lee, and Jaegul Choo. "PairEval: Open-domain Dialogue Evaluation Metric with Pairwise Comparisons". *COLM · Conference on Language Modeling*.
- Jinhee Kim,\* Taesung Kim,\* and Jaegul Choo. "Bones Can't Be Triangles: Accurate and Efficient Vertebrae Keypoint Estimation through Collaborative Error Revision". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-73021-4_26*.
- Jeongho Kim,\* Min-Jung Kim,\* Junsoo Lee, and Jaegul Choo. "TCAN: Animating Human Images with Temporally Consistent Pose Guidance using Diffusion Models". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-73202-7_19*.
- Jaeseong Lee,\* Junha Hyung,\* Sohyun Jeong, and Jaegul Choo. "SelfSwapper: Self-Supervised Face Swapping via Shape-Agnostic Masked AutoEncoder". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-73001-6_22*.
- Sungwon Hwang,\* Min-Jung Kim,\* Taewoong Kang, Jayeon Kang, and Jaegul Choo. "VEGS: View Extrapolation of Urban Scenes in 3D Gaussian Splatting using Learned Priors". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-73001-6_1*.
- Jooyeol Yun, and Jaegul Choo. "Scaling Up Personalized Image Aesthetic Assessment via Task Vector Customization". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-73661-2_18*.
- Junha Song, Tae Soo Kim, Junha Kim, Gunhee Nam, Thijs Kooi, and Jaegul Choo. "Is User Feedback Always Informative? Retrieval Latent Defending for Semi-Supervised Domain Adaptation without Source Data". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-72698-9_5*.
- ChaeHun Park,\* Koanho Lee,\* Hyesu Lim, Jaeseok Kim, Junmo Park, Yu-Jung Heo, Du-Seong Chang, and Jaegul Choo. "Translation Deserves Better: Analyzing Translation Artifacts in Cross-lingual Visual Question Answering". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL · DOI: 10.18653/v1/2024.findings-acl.308*.
- Dohyun Lee,\* Daniel Rim,\* Minseok Choi, and Jaegul Choo. "Protecting Privacy Through Approximating Optimal Parameters for Sequence Unlearning in Language Models". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL · DOI: 10.18653/v1/2024.findings-acl.936*.
- Dongyoon Hwang,\* Byungkun Lee,\* Hojoon Lee, Hyunseung Kim, and Jaegul Choo. "A Simple Convolution Injector for Vision Transformer Towards Effective Adaptation in Visuo-Motor Control". *ICML · International Conference on Machine Learning*.
- Donghu Kim,\* Hojoon Lee,\* Kyungmin Lee,\* Dongyoon Hwang, and Jaegul Choo. "Investigating Pre-Training Objectives for Generalization in Visual Reinforcement Learning". *ICML · International Conference on Machine Learning*.
- Hojoon Lee, Hyeonseo Cho, Hyunseung Kim, Donghu Kim, Dugki Min, Jaegul Choo, and Clare Lyle. "Slow and Steady Wins the Race: Maintaining Plasticity with Hare and Tortoise Networks". *ICML · International Conference on Machine Learning*.
- Chung Park, Taesan Kim, Hyungjun Yoon, Junui Hong, Yelim Yu, Mincheol Cho, Minsung Choi, and Jaegul Choo. "Pacer and Runner: Cooperative Learning Framework between Single- and Cross-Domain Sequential Recommendation". *SIGIR · International ACM SIGIR Conference on Research and Development in Information Retrieval · DOI: 10.1145/3626772.3657710*.
- Jeonghoon Park,\* Chaeyeon Chung,\* Juyoung Lee, and Jaegul Choo. "Enhancing Intrinsic Features for Debiasing via Investigating Class-Discerning Common Attributes in Bias-Contrastive Pair". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52733.2024.01172*.
- Jeongho Kim, Gyojung Gu, Minho Park, Sunghyun Park, and Jaegul Choo. "StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52733.2024.00781*.
- Junwoo Park, Daehoon Gwak, Jaegul Choo, and Edward Choi. "Self-Supervised Contrastive Forecasting". *ICLR · International Conference on Learning Representations*.
- Taewoong Kang,\* Jeongsik Oh,\* Jaeseong Lee, Sunghyun Park, and Jaegul Choo. "Expression Domain Translation Network for Cross-domain Head Reenactment". *ICASSP · IEEE International Conference on Acoustics, Speech and Signal Processing · DOI: 10.1109/icassp48485.2024.10447878*.
- Junha Hyung,\* Jaeyo Shin,\* and Jaegul Choo. "MagiCapture: High-Resolution Multi-Concept Portrait Customization". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v38i3.28020*.
- Dongmin Choi, Wonwoo Cho, Kangyeol Kim, and Jaegul Choo. "iDet3D: Towards Efficient Interactive Object Detection for LiDAR Point Clouds". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v38i2.27897*.
- Dongmin Kim, Sunghyun Park, and Jaegul Choo. "When Model Meets New Normals: Test-time Adaptation for Unsupervised Time-series Anomaly Detection". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v38i12.29210*.
- Min-Jung Kim, Gyojung Gu, and Jaegul Choo. "LensNeRF: Rethinking Volume Rendering based on Thin-Lens Camera Model". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv57701.2024.00315*.
- Wonwoo Cho, Dongmin Choi, Hyesu Lim, Jinho Choi, Saemee Choi, Hyun-seok Min, Sungbin Lim, and Jaegul Choo. "Slice and Conquer: A Planar-to-3D Framework for Efficient Interactive Segmentation of Volumetric Images". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv57701.2024.00744*.
- Jaekak Yoo,\* Youngwoo Cho,\* Dong Hyeon Kim, Jaeseok Kim, Tae Geol Lee, Seung Mi Lee, Jaegul Choo, and Mun Seok Jeong. "Unraveling the Role of Raman Modes in Evaluating the Degree of Reduction in Graphene Oxide via Explainable Artificial Intelligence". *· DOI: 10.1016/j.nantod.2024.102366*.

**2023**

- Minseok Choi, Chaeheon Gwak, Seho Kim, Si Hyeong Kim, and Jaegul Choo. "SimCKP: Simple Contrastive Learning of Keyphrase Representations". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · DOI: 10.18653/v1/2023.findings-emnlp.199*.
- Dohee Kim,\* Ra Yoo,\* Soyoung Yang, Hee Yang, and Jaegul Choo. "AniEE: A Dataset of Animal Experimental Literature for Event Extraction". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · DOI: 10.18653/v1/2023.findings-emnlp.863*.
- Dohee Kim,\* Yujin Baek,\* Soyoung Yang, and Jaegul Choo. "Towards Formality-Aware Neural Machine Translation by Leveraging Context Information". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · Short Paper · DOI: 10.18653/v1/2023.findings-emnlp.494*.
- Hyunseung Kim,\* Byungkun Lee,\* Sejik Park, Hojoon Lee, Dongyoon Hwang, Kyushik Min, and Jaegul Choo. "Learning to Discover Skills through Guidance". *NeurIPS · Conference on Neural Information Processing Systems*.
- Hojoon Lee,\* Hanseul Cho,\* Hyunseung Kim,\* Daehoon Gwak, Joonkee Kim, Jaegul Choo, Se-Young Yun, and Chulhee Yun. "PLASTIC: Improving Input and Label Plasticity for Sample Efficient Reinforcement Learning". *NeurIPS · Conference on Neural Information Processing Systems*.
- Heungseok Park, Aeree Cho, Hyojun Jeon, Hayoung Lee, Youngil Yang, Sungjae Lee, Heungsub Lee, and Jaegul Choo. "HPC ClusterScape: Increasing Transparency and Efficiency of Shared High-Performance Computing Clusters for Large-scale AI Models". *VDS · Visualization in Data Science*.
- Minseok Choi, Hyesu Lim, and Jaegul Choo. "PRiSM: Enhancing Low-Resource Document-Level Relation Extraction with Relation-Aware Score Calibration". *IJCNLP-AACL · International Joint Conference on Natural Language Processing and the Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics · Short Paper · DOI: 10.18653/v1/2023.findings-ijcnlp.4*.
- Jimin Hong,\* ChaeHun Park,\* and Jaegul Choo. "Learning to Diversify Neural Text Generation via Degenerative Model". *IJCNLP-AACL · International Joint Conference on Natural Language Processing and the Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics · Short Paper · DOI: 10.18653/v1/2023.findings-ijcnlp.6*.
- Chung Park, Taekyoon Choi, Taesan Kim, Mincheol Cho, Junui Hong, Minsung Choi, and Jaegul Choo. "FedGeo: Privacy-Preserving User Next Location Prediction with Federated Learning". *SIGSPATIAL · ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems · DOI: 10.1145/3589132.3625582*.
- Hojoon Lee,\* Hawon Jeong,\* Byungkun Lee,\* Kyungyup Daniel Lee, and Jaegul Choo. "ST-RAP: A Spatio-Temporal Framework for Real Estate Appraisal". *CIKM · ACM International Conference on Information and Knowledge Management · Short Paper · DOI: 10.1145/3583780.3615168*.
- Chung Park, Taesan Kim, Taekyoon Choi, Junui Hong, Yelim Yu, Mincheol Cho, Kyunam Lee, Sungil Ryu, Hyungjun Yoon, Minsung Choi, and Jaegul Choo. "Cracking the Code of Negative Transfer: A Cooperative Game Theoretic Approach for Cross-Domain Sequential Recommendation". *CIKM · ACM International Conference on Information and Knowledge Management · DOI: 10.1145/3583780.3614828*.
- Chaeyeon Chung,\* Yeojeong Park,\* Seunghwan Choi, Munkhsoyol Ganbat, and Jaegul Choo. "Shortcut-V2V: Compression Framework for Video-to-Video Translation based on Temporal Redundancy Reduction". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.00700*.
- Minho Park,\* Jooyeol Yun,\* Seunghwan Choi, and Jaegul Choo. "Learning to Generate Semantic Layouts for Higher Text-Image Correspondence in Text-to-Image Synthesis". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.00698*.
- Jungsoo Lee, Debasmit Das, Jaegul Choo, and Sungha Choi. "Towards Open-Set Test-Time Adaptation Utilizing the Wisdom of Crowds in Entropy Minimization". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.01501*.
- Sunghyun Park, Seunghan Yang, Jaegul Choo, and Sungrack Yun. "Label Shift Adapter for Test-Time Adaptation under Covariate and Label Shifts". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.01505*.
- Sungwon Hwang, Junha Hyung, Daejin Kim, Min-Jung Kim, and Jaegul Choo. "FaceCLIPNeRF: Text-driven 3D Face Manipulation using Deformable Neural Radiance Fields". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.00321*.
- Sanghun Jung, Jungsoo Lee, Nanhee Kim, Amirreza Shaban, Byron Boots, and Jaegul Choo. "CAFA: Class-Aware Feature Alignment for Test-time Adaptation". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.01747*.
- Kyungmin Jo,\* Wonjoon Jin,\* Jaegul Choo, Hyunjoon Lee, and Sunghyun Cho. "3D-Aware Generative Model for Improved Side-View Image Synthesis". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv51070.2023.02090*.
- Seunghoon Yi, Youngwoo Cho, Jinhwan Sul, Seung Woo Ko, Soo Kyung Kim,, Jaegul Choo, Hongkee Yoon, and Joonseok Lee. "Towards Physically Reliable Molecular Representation Learning". *UAI · Conference on Uncertainty in Artificial Intelligence · Oral*.
- Chung Park, TaeSan Kim, Junui Hong, Minsung Choi, and Jaegul Choo. "Pre-training Contextual Location Embeddings in Personal Trajectories via Efficient Hierarchical Location Representations". *ECML/PKDD · European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases · DOI: 10.1007/978-3-031-43430-3_8*.
- Junwoo Park, Jungsoo Lee, Youngin Cho, Woncheol Shin, Dongmin Kim, Jaegul Choo, and Edward Choi. "Deep Imbalanced Time-series Forecasting via Local Discrepancy Density". *ECML/PKDD · European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases · DOI: 10.1007/978-3-031-43424-2_9*.
- Soyoung Yang, Minseok Choi, Youngwoo Cho, and Jaegul Choo. "HistRED: A Historical Document-Level Relation Extraction Dataset". *ACL · Annual Meeting of the Association for Computational Linguistics · DOI: 10.18653/v1/2023.acl-long.180*.
- Yujin Baek,\* Koanho Lee,\* Dayeon Ki, Hyoung-Gyu Lee, Cheonbok Park, and Jaegul Choo. "Towards Accurate Translation via Semantically Appropriate Application of Lexical Constraints". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL · DOI: 10.18653/v1/2023.findings-acl.298*.
- ChaeHun Park, Seungil Cha Lee, Daniel Rim, and Jaegul Choo. "DEnsity: Open-domain Dialogue Evaluation Metric using Density Estimation". *ACL · Annual Meeting of the Association for Computational Linguistics · Findings of ACL · DOI: 10.18653/v1/2023.findings-acl.896*.
- Hojoon Lee, Koanho Lee, Dongyoon Hwang, Hyunho Lee, Byungkun Lee, and Jaegul Choo. "On the Importance of Feature Decorrelation for Unsupervised Representation Learning in Reinforcement Learning". *ICML · International Conference on Machine Learning*.
- Daeun Kyung,\* Kyungmin Jo,\* Jaegul Choo, Joonseok Lee, and Edward Choi. "Perspective Projection-Based 3D CT Reconstruction from Biplanar X-rays". *ICASSP · IEEE International Conference on Acoustics, Speech and Signal Processing · DOI: 10.1109/icassp49357.2023.10096296*.
- Junha Hyung, Sungwon Hwang, Daejin Kim, Hyunji Lee, and Jaegul Choo. "Local 3D Editing via 3D Distillation of CLIP Knowledge". *CVPR · IEEE International Conference on Computer Vision and Pattern Recognition · DOI: 10.1109/cvpr52729.2023.01219*.
- Jihyeon Lee,\* TaeHee Kim,\* Yunwon Tae,\* Cheonbok Park, and Jaegul Choo. "PePe: Personalized Post-editing Model Utilizing User-generated Post-edits". *EACL · Conference of the European Chapter of the Association for Computational Linguistics · DOI: 10.18653/v1/2023.findings-eacl.18*.
- Hyesu Lim, Byeonggeun Kim, Jaegul Choo, and Sungha Choi. "TTN: A Domain-Shift Aware Batch Normalization in Test-Time Adaptation". *ICLR · International Conference on Learning Representations*.
- Jungsoo Lee,\* Jeonghoon Park,\* Daeyoung Kim,\* Juyoung Lee, Edward Choi, and Jaegul Choo. "Revisiting the Importance of Amplifying Bias for Debiasing". *AAAI · AAAI Conference on Artificial Intelligence · DOI: 10.1609/aaai.v37i12.26748*.
- Youngin Cho,\* Junsoo Lee,\* Soyoung Yang, Juntae Kim, Yeojeong Park, Haneol Lee, Mohammad Azam Khan, Daesik Kim, and Jaegul Choo. "Guiding Users to Where to Give Color Hints for Efficient Interactive Sketch Colorization via Unsupervised Region Prioritization". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv56688.2023.00186*.
- Wonwoo Cho, Jeonghoon Park, and Jaegul Choo. "Training Auxiliary Prototypical Classifiers for Explainable Anomaly Detection in Medical Image Segmentation". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv56688.2023.00265*.
- Kyungmin Jo,\* Gyumin Shim,\* Sanghun Jung, Soyoung Yang, and Jaegul Choo. "CG-NeRF: Conditional Generative Neural Radiance Fields for 3D-aware Image Synthesis". *WACV · Winter Conference on Applications of Computer Vision · DOI: 10.1109/wacv56688.2023.00079*.
- Sanghyeon Lee,\* JooYeol Yun,\* Minho Park,\* and Jaegul Choo. "iColoriT: Towards Propagating Local Hint to the Right Region in Interactive Colorization by Leveraging Vision Transformer". *WACV · Winter Conference on Applications of Computer Vision*.
- Jaekak Yoo,\* Youngwoo Cho,\* Byeonggeun Jeong, Soo Ho Choi, Ki Kang Kim, Seong Chu Lim, Seung Mi Lee, Jaegul Choo, and Mun Seok Jeong. "Explainable Artificial Intelligence Approach to Identify the Origin of Phonon-Assisted Emission in WSe2 Monolayer". *· DOI: 10.1002/aisy.202200463*.
- Seungmin Jin, Hyunwook Lee, Cheonbok Park, Hyeshin Chu, Yunwon Tae, Jaegul Choo, and Sungahn Ko. "A Visual Analytics System for Improving Traffic Forecasting Models". *TVCG · IEEE Transactions on Visualization and Computer Graphics*.

**2022**

- Hojun Cho, Dohee Kim, Seungwoo Ryu, ChaeHun Park, Hyungjong Noh, Jeong-in Hwang, Minseok Choi, Edward Choi, and Jaegul Choo. "Rethinking Style Transformer by Energy-based Interpretation: Adversarial Unsupervised Style Transfer using Pretrained Model". *EMNLP · Conference on Empirical Methods in Natural Language Processing*.
- Nyoungwoo Lee, ChaeHun Park, Ho-Jin Choi, and Jaegul Choo. "PNEG: Prompt-based Negative Response Generation for Dialogue Response Selection Task". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Short Paper · DOI: 10.18653/v1/2022.emnlp-main.733*.
- Youngin Cho,\* Daejin Kim,\* Dongmin Kim, Mohammad Azam Khan, and Jaegul Choo. "WaveBound: Dynamic Error Bounds for Stable Time Series Forecasting". *NeurIPS · Conference on Neural Information Processing Systems*.
- Youngin Cho,\* Daejin Kim,\* Mohammad Azam Khan, and Jaegul Choo. "Mining Multi-Label Samples from Single Positive Labels". *NeurIPS · Conference on Neural Information Processing Systems*.
- Rodrigo Hormazabal, Changyoung Park, Soonyoung Lee, Sehui Han, Yeonsik Jo, Jaewan Lee, Ahra Jo, Seung Hwan Kim, Jaegul Choo, Moontae Lee, and Honglak Lee. "CEDe: A collection of expert-curated datasets with atom-level entity annotations for Optical Chemical Structure Recognition". *NeurIPS · Conference on Neural Information Processing Systems*.
- TaeHee Kim,\* ChaeHun Park,\* Jimin Hong, Radhika Dua, Edward Choi, and Jaegul Choo. "Reweighting Strategy based on Synthetic Data Identification for Sentence Similarity". *COLING · International Conference on Computational Linguistics*.
- Daejin Kim,\* Youngin Cho,\* Dongmin Kim, Cheonbok Park, and Jaegul Choo. "Residual Correction in Real-Time Traffic Forecasting". *CIKM · ACM International Conference on Information and Knowledge Management · DOI: 10.1145/3511808.3557432*.
- Kangyeol Kim,\* Sunghyun Park,\* Jaeseong Lee,\* Sunghyo Chung, Junsoo Lee, and Jaegul Choo. "AnimeCeleb: Large-Scale Animation CelebHeads Dataset for Head Reenactment". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-20074-8_24*.
- Taewoo Kim,\* Chaeyeon Chung,\* Yoonseo Kim,\* Sunghyun Park, Kangyeol Kim, and Jaegul Choo. "Style Your Hair: Latent Optimization for Pose-Invariant Hairstyle Transfer via Local-Style-Aware Hair Alignment". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-19790-1_12*.
- SangYun Lee,\* Gyojung Gu,\* Sunghyun Park, Seunghwan Choi, and Jaegul Choo. "High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-19790-1_13*.
- Wonwoo Cho and Jaegul Choo. "Towards Accurate Open-Set Recognition via Background-Class Regularization". *ECCV · European Conference on Computer Vision · DOI: 10.1007/978-3-031-19806-9_38*.
- Gyumin Shim,\* Minsoo Lee,\* and Jaegul Choo. "ReFu: Refine and Fuse the Unobserved View for Detail-Preserving Single-Image 3D Human Reconstruction". *MM · ACM International Conference on Multimedia · DOI: 10.1145/3503161.3547971*.
- Jinhee Kim,\* Taesung Kim,\* Taewoo Kim, Jaegul Choo, Dong-Wook Kim, Byungduk Ahn, In-Seok Song, and Yoon-Ji Kim. "Morphology-Aware Interactive Keypoint Estimation". *MICCAI · International Conference on Medical Image Computing and Computer Assisted Intervention · DOI: 10.1007/978-3-031-16437-8_65*.
- Junwoo Park, Youngwoo Cho, Gyuhyeon Sim, Hojoon Lee, and Jaegul Choo. "Enemy Spotted: In-game Gun Sound Dataset for Gunshot Classification and Localization". *CoG · IEEE Conference on Games · DOI: 10.1109/cog51982.2022.9893670*.
- Bum Chul Kwon, Jungsoo Lee, Chaeyeon Chung, Nyoungwoo Lee, Ho-Jin Choi, and Jaegul Choo. "DASH: Visual Analytics for Debiasing Image Classification via User-Driven Synthetic Data Augmentation". *EuroVis · EG/VGTC Conference on Visualization · Short Paper*.
- Hojoon Lee, Dongyoon Hwang, Kyushik Min, and Jaegul Choo. "Towards Validating Long-Term User Feedbacks in Interactive Recommendation Systems". *SIGIR · International ACM SIGIR Conference on Research and Development in Information Retrieval · Short Paper · DOI: 10.1145/3477495.3531869*.
- Hojoon Lee,\* Dongyoon Hwang,\* Hyunseung Kim, Byungkun Lee, and Jaegul Choo. "DraftRec: Personalized Draft Recommendation for Victory in Multi-Player Online Battle Arena Games". *WWW · International World Wide Web Conference*.
- Taesung Kim,\* Jinhee Kim,\* Yunwon Tae, Cheonbok Park, Jang-Ho Choi, and Jaegul Choo. "Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift". *ICLR · International Conference on Learning Representations*.
- Chung Park, Junui Hong, Cheonbok Park, Taesan Kim, Minsung Choi, and Jaegul Choo. "PASTA: Parallel Spatio-Temporal Attention with Spatial Auto-Correlation Gating for Fine-Grained Crowd Flows Prediction". *PAKDD · Pacific-Asia Conference on Knowledge Discovery and Data Mining*.

**2021**

- Chaeyeon Chung,\* Taewoo Kim,\* Hyelin Nam,\* Seunghwan Choi, Gyojung Gu, Sunghyun Park, and Jaegul Choo. "HairFIT: Pose-Invariant Hairstyle Transfer via Flow-based Hair Alignment and Semantic-Region-Aware Inpainting". *BMVC · British Machine Vision Conference · Oral · DOI: 10.5244/c.35.161*.
- Jungsoo Lee,\* Jooyeol Yun,\* Sunghyun Park, Yonggyu Kim, and Jaegul Choo. "Improving Face Recognition with Large Age Gaps by Learning to Distinguish Children". *BMVC · British Machine Vision Conference · DOI: 10.5244/c.35.222*.
- Kangyeol Kim,\* Sunghyun Park,\* Junsoo Lee, Joonseok Lee, Sookyung Kim, Jaegul Choo, and Edward Choi. "Continuous-Time Video Generation via Learning Motion Dynamics with Neural ODE". *BMVC · British Machine Vision Conference · DOI: 10.5244/c.35.7*.
- Jungsoo Lee,\* Eungyeup Kim,\* Juyoung Lee, Jihyeon Lee, and Jaegul Choo. "Learning Debiased Representation via Disentangled Feature Augmentation". *NeurIPS · Conference on Neural Information Processing Systems · Oral*.
- Beomsoo Kim, Jang-Ho Choi, and Jaegul Choo. "Augmenting Imbalanced Time-series Data via Adversarial Perturbation in Latent Space". *ACML · Asian Conference on Machine Learning*.
- Jimin Hong,\* Taehee Kim,\* Hyesu Lim,\* and Jaegul Choo. "AVoCaDo: Strategy for Adapting Vocabulary to Downstream Domain". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Short Paper · DOI: 10.18653/v1/2021.emnlp-main.385*.
- Fuxiang Chen, Mijung Kim, and Jaegul Choo. "Novel Natural Language Summarization of Program Code via Leveraging Multiple Input Representations". *EMNLP · Conference on Empirical Methods in Natural Language Processing · Findings of EMNLP · DOI: 10.18653/v1/2021.findings-emnlp.214*.
- Sanghun Jung,\* Jungsoo Lee,\* Daehoon Gwak, Sungha Choi, and Jaegul Choo. "Standardized Max Logit: A Simple yet Effective Approach for Identifying Unexpected Road Obstacles in Urban-Scene Segmentation". *ICCV · International Conference on Computer Vision · Oral · DOI: 10.1109/iccv48922.2021.01514*.
- Eungyeup Kim,\* Sanghyeon Lee,\* Jeonghoon Park,\* Somi Choi, Choonghyun Seo, and Jaegul Choo. "Deep Edge-Aware Interactive Colorization against Color-Bleeding Effects". *ICCV · International Conference on Computer Vision · Oral · DOI: 10.1109/iccv48922.2021.01440*.
- Eungyeup Kim,\* Jihyeon Lee,\* and Jaegul Choo. "BiaSwap: Removing Dataset Bias with Bias-Tailored Swapping Augmentation". *ICCV · International Conference on Computer Vision · DOI: 10.1109/iccv48922.2021.01472*.
- Cheonbok Park,\* Soyoung Yang,\* Inyoup Na,\* Sunghyo Chung, Sungbok Shin, Bum Chul Kwon, Deokgun Park, and Jaegul Choo. "VATUN: Visual Analytics for Testing and Understanding Convolutional Neural Networks". *EuroVis · EG/VGTC Conference on Visualization · Short Paper*.
- Chaeyeon Chung,\* Jungsoo Lee,\* Kyungmin Park, Junsoo Lee, Minjae Kim, Mookyung Song, Yeonwoo Kim, Jaegul Choo, and Sungsoo Ray Hong. "Understanding Human-side Impact of Sampling Image Batches in Subjective Attribute Labeling". *CSCW · ACM Conference on Computer-Supported Cooperative Work and Social Computing · DOI: 10.1145/3476037*.

## 수상과 선정

연구실 소식, 논문 옆 수상 표기, 교수의 수상 목록에 나온 8항목이다. 2022년·2024년처럼 연도만 적은 행은 누리집의 연도 표기이며 수상 날짜는 게시되어 있지 않다. Honorable Mention은 「입선」을 병기했다.[^news][^pubs][^pi]

- 2026-07-22 · FlashSAC 논문이 RSS 2026 Best Paper Award를 받았다.
- 2024 · Pacer and Runner 논문이 SIGIR 2024 Best Paper Honorable Mention Award(입선)를 받았다.
- 2023-02-15 · Perspective Projection-Based 3D CT Reconstruction from Biplanar X-rays 논문의 ICASSP 2023 Best Student Paper Award 소식.
- 2022-08-02 · Sunghyun이 AnimeCeleb 논문으로 KAIA Summer Conference 2022 Best Paper Award를 받았다.
- 2022-07-15 · Hojoon이 Towards Validating Long-Term User Feedbacks in Interactive Recommendation Systems 논문으로 SIGIR 2022 Best Short Paper Honorable Mention Award(입선)를 받았다.
- 2022 · DASH 논문이 EuroVis 2022 Short Paper Honorable Mention Award(입선)를 받았다.
- 2022-02-23 · Gyuhyeon이 이끄는 창업기업 Letsur가 Samsung C-Lab Outside에 선정되었다.
- 2022-01-11 · Hyesu·Jeonghoon·Sanghyeon이 AVoCaDo와 Deep Edge-Aware Interactive Colorization against Color-Bleeding Effects 논문으로 KAIST AI Workshop에서 Best Poster Award 2건을 받았다.

## 소식

연구실 News의 2021년 10월 15일–2026년 9월 28일 소식 54건이다. 학회 논문은 소식에 적힌 채택 사실로 표시한다.[^news]

- 2026-09-28 · 논문 2편이 NeurIPS 2026에 채택되었다.
- 2026-09-24 · Hyunseung Kim이 KRAFTON의 PUBG Ally 개발을 공동 주도했다. 음성으로 소통하는 언어 모델 에이전트와 게임 내 행동 제어를 결합했다.
- 2026-09-07 · 논문 3편이 CoRL 2026에 채택되었다.
- 2026-08-24 · 논문 3편이 EMNLP 2026에 채택되었다.
- 2026-08-24 · 논문 1편이 CIKM 2026에 채택되었다.
- 2026-07-24 · 논문 1편이 KDD 2026에 채택되었다.
- 2026-07-22 · 논문 1편이 ICML 2026에 채택되었다.
- 2026-07-21 · 논문 1편이 COLM 2026에 채택되었다.
- 2026-06-17 · 논문 4편이 ECCV 2026에 채택되었다.
- 2026-06-16 · 논문 1편이 IROS 2026에 채택되었다.
- 2026-06-05 · 논문 1편이 InterSpeech 2026에 채택되었다.
- 2026-05-20 · 논문 1편이 IJCAI 2026에 채택되었다.
- 2026-05-08 · 논문 1편이 RLC 2026에 채택되었다.
- 2026-04-27 · 논문 1편이 RSS 2026에 채택되었다.
- 2026-04-04 · 논문 3편이 ACL 2026에 채택되었다.
- 2026-02-24 · 외부 시점 영상을 1인칭 시점으로 만드는 EgoX 연구가 국내 언론에 소개되었다.
- 2026-02-23 · 논문 8편이 CVPR 2026에 채택되었다.
- 2026-02-13 · 논문 1편이 LREC 2026에 채택되었다.
- 2026-01-31 · 논문 1편이 ICRA 2026에 채택되었다.
- 2026-01-22 · 논문 5편이 ICLR 2026에 채택되었다.
- 2025-11-08 · 논문 2편이 AAAI 2026에 채택되었다.
- 2025-11-05 · 논문 1편이 3DV 2026에 채택되었다.
- 2023-12-13 · 논문 1편이 ICASSP 2024에 채택되었다.
- 2023-12-09 · 논문 3편이 AAAI 2024에 채택되었다.
- 2023-10-20 · 논문 2편이 WACV 2024에 채택되었다.
- 2023-10-06 · 논문 3편이 Findings of EMNLP 2023에 채택되었다.
- 2023-09-22 · 논문 2편이 NeurIPS 2023에 채택되었다.
- 2023-09-08 · 논문 1편이 SIGSPATIAL 2023에 채택되었다.
- 2023-09-04 · 논문 2편이 Findings of IJCNLP-AACL 2023에 채택되었다.
- 2023-08-04 · 논문 2편이 CIKM 2023에 채택되었다.
- 2023-07-13 · 논문 7편이 ICCV 2023에 채택되었다.
- 2023-06-05 · 논문 2편이 ECML/PKDD 2023에 채택되었다.
- 2023-05-08 · 논문 1편이 UAI 2023에 채택되었다.
- 2023-05-01 · 논문 1편이 ACL 2023, 2편이 Findings of ACL 2023에 채택되었다.
- 2023-04-24 · 논문 1편이 ICML 2023에 채택되었다.
- 2023-02-27 · 논문 1편이 CVPR 2023에 채택되었다.
- 2023-01-21 · 논문 1편이 ICLR 2023에 채택되었다.
- 2023-01-20 · 논문 1편이 Findings of EACL 2023에 채택되었다.
- 2022-11-18 · 논문 1편이 AAAI 2023에 채택되었다.
- 2022-10-10 · 논문 4편이 WACV 2023에 채택되었다.
- 2022-10-06 · 논문 2편이 EMNLP 2022에 채택되었다.
- 2022-09-14 · 논문 2편이 NeurIPS 2022, 1편이 Datasets and Benchmarks Track에 채택되었다.
- 2022-08-15 · 논문 1편이 COLING 2022에 채택되었다.
- 2022-08-01 · 논문 1편이 CIKM 2022에 채택되었다.
- 2022-07-03 · 논문 4편이 ECCV 2022에 채택되었다.
- 2022-06-29 · 논문 1편이 ACMMM 2022에 채택되었다.
- 2022-06-02 · 논문 1편이 MICCAI 2022에 채택되었다.
- 2022-04-30 · 논문 1편이 CoG 2022에 채택되었다.
- 2022-03-31 · 논문 1편이 SIGIR 2022에 채택되었다.
- 2022-03-26 · 논문 1편이 EuroVis 2022에 채택되었다.
- 2022-01-24 · 논문 1편이 ICLR 2022에 채택되었다.
- 2022-01-15 · 논문 1편이 PAKDD 2022에 채택되었다.
- 2022-01-13 · 논문 1편이 WWW 2022에 채택되었다.
- 2021-10-15 · 논문 3편이 BMVC 2021에 채택되었다.

## 연락과 위치

- 교수 업무 이메일: jchoo@kaist.ac.kr[^people]
- 교수 연구실 전화: +82-42-350-1813[^people]
- 성남 연구실: 경기도 성남시 분당구 성남대로331번길 8, KINS Tower 904호·1801호, 우편번호 13558[^home]
- 판교 연구센터: 경기도 성남시 수정구 창업로 43, 판교글로벌비즈센터 업무동 4층, 우편번호 13449[^home]

## 각주
[^home]: DAVIAN 연구실 소개와 위치. <https://davian.kaist.ac.kr/> 관측일 2026-11-09.
[^research]: DAVIAN Research. <https://davian.kaist.ac.kr/research> 관측일 2026-11-09.
[^people]: DAVIAN People. <https://davian.kaist.ac.kr/people> 관측일 2026-11-09.
[^pubs]: DAVIAN Publication. <https://davian.kaist.ac.kr/publication> 관측일 2026-11-09.
[^news]: DAVIAN News. <https://davian.kaist.ac.kr/news> 관측일 2026-11-09.
[^medical]: DAVIAN Medical & Healthcare AI 연구 소개. <https://davian.kaist.ac.kr/research/medical> 관측일 2026-11-09.
[^generative]: DAVIAN Generative Models & Diffusion 연구 소개. <https://davian.kaist.ac.kr/research/generative> 관측일 2026-11-11.
[^nlp]: DAVIAN Large Language Models & NLP 연구 소개. <https://davian.kaist.ac.kr/research/nlp> 관측일 2026-11-11.
[^rl]: DAVIAN Reinforcement Learning & Robotics 연구 소개. <https://davian.kaist.ac.kr/research/rl> 관측일 2026-11-11.
[^timeseries]: DAVIAN Time-Series & Data Mining 연구 소개. <https://davian.kaist.ac.kr/research/timeseries> 관측일 2026-11-11.
[^trust]: DAVIAN Trustworthy & Interpretable AI 연구 소개. <https://davian.kaist.ac.kr/research/interpretability> 관측일 2026-11-11.
[^visualization]: DAVIAN Data Visualization & Visual Analytics 연구 소개. <https://davian.kaist.ac.kr/research/visualization> 관측일 2026-11-11.
[^efficient]: DAVIAN Efficient & Adaptation Methods 연구 소개. <https://davian.kaist.ac.kr/research/efficient> 관측일 2026-11-11.
[^recognition]: DAVIAN Visual Recognition & 3D 연구 소개. <https://davian.kaist.ac.kr/research/recognition> 관측일 2026-11-11.
[^dept]: KAIST 김재철AI대학원 전임교수 소개: 주재걸. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측일 2026-11-09.
[^bio]: Jaegul Choo Short Bio. <https://sites.google.com/site/jaegulchoo/bio> 관측일 2026-11-11.
[^pi]: Jaegul Choo 교수 개인 쪽의 Awards. <https://sites.google.com/site/jaegulchoo> 관측일 2026-11-11.
[^med-methods]: J. Kim 외, Attend-and-Refine: Interactive keypoint estimation and quantitative cervical vertebrae analysis for bone age assessment, Medical Image Analysis (2025, 게재 승인 표기). <https://arxiv.org/abs/2507.07670> 초록 기준(arXiv 판). 관측일 2026-11-11. 초록은 사용자 상호작용을 반영하는 ARNet과 형태 보존 학습 기준을 제안한다.
[^p1]: M. Choi 외, Y. Kwak, EMNLP 2026 (채택) (2026). <https://doi.org/10.18653/2026.emnlp-main.2651> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p2]: J. Kim 외, J. Choo, IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings (온라인 2024-06-16). <https://doi.org/10.1109/cvpr52733.2024.00781> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p3]: M. Choi, D. J. Rim, D. Lee, J. Choo, Proceedings of the conference - Association for Computational Linguistics. Meeting (2025). <https://doi.org/10.18653/v1/2025.acl-long.1371> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p4]: H. Lee 외, T. Seno, International Conference on Learning Representations (ICLR 2025) (온라인 2024-10-13). <https://doi.org/10.48550/arxiv.2410.09754> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p5]: H. Lim, J. Choi, J. Choo, S. Schneider, International Conference on Learning Representations (ICLR 2025) (온라인 2024-12-06). <https://doi.org/10.48550/arxiv.2412.05276> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p6]: D. Kim, S. Park, J. Choo, Proceedings of the AAAI Conference on Artificial Intelligence (온라인 2024-03-24). <https://doi.org/10.1609/aaai.v38i12.29210> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p7]: B. C. Kwon 외, J. Choo, EuroVis 2022 (Short Paper) (온라인 2022-06-13). <https://doi.org/10.2312/evs.20221099> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.
[^p8]: D. Kyung 외, E. Choi, IEEE International Conference on Acoustics Speech and Signal Processing (온라인 2023-05-05). <https://doi.org/10.1109/icassp49357.2023.10096296> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5047912015,publication_year:2021-2026> 관측일 2026-11-11.

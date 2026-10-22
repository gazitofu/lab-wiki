# KAIST 비주얼 AI 그룹 (KAIST Visual AI Group)

**KAIST AI컴퓨팅학과 · 성민혁 교수**

- 분야: 기계 학습, 컴퓨터 비전, 컴퓨터 그래픽스, 기하 처리, 확산·흐름 생성 모델의 생성 과정 조절과 빠른 생성, 3차원 형상의 생성·변형·편집, 비전-언어 모델의 공간 추론, 생성형 정책 학습, 단백질·생물 데이터 생성
- 대분야: 컴퓨팅·AI
- 태그: 생성 인공지능[^home][^p1][^p3], 컴퓨터 비전[^home][^p7][^p8], 멀티모달 AI[^joinus][^p7][^p8], 강화학습[^joinus]
- 홈페이지: <https://visualai.kaist.ac.kr>
- 근거와 출처: [KAIST Visual AI Group 근거 페이지](visualai-sources.md)

> 이미지·영상·3차원 모양 같은 여러 시각 데이터를 만들고, 다루고, 분석하는 기술을 연구하는 연구실이다. 기계 학습, 컴퓨터 비전, 컴퓨터 그래픽스에 걸쳐 일하며, 지금은 생성 모델링, 공간 지능, 멀티모달 기반 모델 같은 주제에 중점을 둔다고 밝힌다.[^home][^prof][^joinus]

## 무엇을 연구하나

연구실은 KAIST AI컴퓨팅학과 성민혁 교수가 이끄는 연구실이다.[^prof] 연구실 누리집은 여러 시각 데이터를 만들고(생성), 다루고(처리), 분석하는 기술을 발전시키는 연구를 하며 그 범위가 기계 학습, 컴퓨터 비전(컴퓨터가 사진·영상을 알아보게 하는 분야), 컴퓨터 그래픽스(컴퓨터로 그림과 3차원 장면을 만들고 표현하는 분야)에 걸친다고 소개한다.[^home] 연구실 소식에 따르면 연구실은 2021년 1월 KAIST에서 문을 열었다.[^news] 반도체시스템공학과 연구실 목록과 메타버스대학원 참여 연구실 목록에도 올라 있고, 메타버스대학원은 연구실의 트랙을 '메타버스 생성'으로, 관심 분야를 기계 학습, 컴퓨터 그래픽, 컴퓨터 비전, 기하학 처리로 적는다.[^sse][^metalab]

연구실 모집 안내는 시각 데이터를 위한 기계 학습 기술을 주로 연구한다고 밝히고, 지금 중점을 두는 주제로 생성 모델링, 단백질·생물 데이터 생성, 공간 지능(Spatial Intelligence), 강화학습·정책 학습(RL / Policy Learning), 멀티모달 기반 모델(그림·글처럼 종류가 다른 자료를 함께 다루는 대형 인공지능 모델)을 든다.[^joinus] 인턴 모집 안내는 이를 더 자세히 나눈다. 생성 모델링에는 서로 다른 종류의 자료를 오가는 생성, 연속·이산 확산과 흐름 모델, 보상으로 이끄는 표본 추출을, 생물 데이터 생성에는 단백질·DNA 생성과 에너지 기반 생성 모델을, 생성형 정책 학습에는 확산 정책 학습과 시각-언어-행동(VLA) 모델을, 공간 지능에는 몸을 가진 에이전트의 질의응답(Embodied Question Answering)과 월드 모델링을 넣는다.[^intern] 연구실은 기계 학습(NeurIPS, ICML, ICLR, AISTATS), 컴퓨터 비전(CVPR, ICCV, ECCV), 컴퓨터 그래픽스(SIGGRAPH, SIGGRAPH Asia) 학회에 논문을 낸다고 적는다.[^joinus]

첫째 갈래는 **확산·흐름 생성 모델의 생성 과정 조절과 빠른 생성**이다. 확산 모델은 잡음에서 출발해 잡음을 조금씩 걷어 내며 그림을 만드는 생성 인공지능이고, 흐름 모델은 잡음을 그림으로 옮기는 경로를 배워 그림을 만드는 비슷한 계열의 모델이다. 대표 논문에서는 그림을 만드는 도중에 여러 후보를 함께 굴리며 사용자가 원하는 성질(보상)에 맞추는 방법에서, 후보를 보상을 반영한 분포에서 뽑아 시작하면 맞춤 성능이 크게 좋아짐을 보였고,[^p1] 미리 학습된 모델이 적은 단계만으로 그림을 만들도록 생성 경로를 베지에 곡선으로 나타내 짧은 학습으로 배우는 방법을 내놓았다.[^p2] 최근 논문 목록에는 흐름 모델의 추론 시점 확장(Inference-Time Scaling), 보상 정렬용 잡음 조절(NoiseTilt), 이산 흐름 모델의 적은 단계 생성(PairFlow) 같은 논문도 있다.[^pubs]

둘째 갈래는 **여러 생성 과정을 맞물리는 동기화 생성**이다. 미리 학습된 이미지 확산 모델 하나로 여러 확산 과정을 함께 돌리며 서로 맞물리게 해, 파노라마나 3차원 물체의 표면 무늬 같은 콘텐츠를 추가 학습 없이 만드는 연구다.[^p3] 대표 논문에서는 여러 확산 과정을 공통 공간을 통해 맞물리는 경우들을 분석하고 SyncTweedies라는 일반적인 동기화 방법을 제안했으며,[^p3] 3차원 메시 위에 물리 기반 렌더링용 재질 무늬(PBR 텍스처)를 만들기 위해 이미지 생성 모델의 잠재 공간을 재질 정보까지 담도록 조정한 MatLat을 내놓았다.[^p4] 연구실 누리집은 이 갈래의 앞선 작업으로 여러 역확산 과정을 맞물려 다양한 크기의 일관된 그림을 만드는 SyncDiffusion(NeurIPS 2023)과, 확산 동기화와 점수 증류 샘플링을 합쳐 360° 파노라마·메시 텍스처 같은 임의의 공간에서 그림을 만드는 StochSync(ICLR 2025)를 꼽는다.[^home]

셋째 갈래는 **3차원 형상의 생성·변형·편집**이다. 대표 논문에서는 3차원 모양을 부품 단위로 나누어 나타내고 두 단계 확산으로 배우는 SALAD를 만들어, 모양을 새로 만들 뿐 아니라 추가 학습 없이 부품 단위로 채우고 고칠 수 있게 했다.[^p5] 또 사용자가 메시(삼각형 면을 이어 만든 3차원 모형)의 손잡이 점을 옮겨 모양을 바꿀 때, 2차원 이미지 확산 모델의 지식을 빌려 결과가 그럴듯하게 남도록 하는 변형 기법을 제안했다.[^p6] 연구실 누리집은 NeRF·3D 가우시안 스플래팅·SVG처럼 매개변수로 나타낸 그림을 편집하는 최적화 방법(Posterior Distillation Sampling, CVPR 2024)과 여러 신경 암시 함수(신경망으로 나타낸 3차원 모양)에 쓰는 듀얼 컨투어링(함수로 나타낸 모양을 메시로 바꾸는 기법) 방법(Occupancy-Based Dual Contouring, SIGGRAPH Asia 2024)도 연구 성과로 든다.[^home] 연구실 소식에 따르면 Posterior Distillation Sampling은 2024 삼성전자 DS-KAIST R&D 교류회에서 Best Paper Award를 받았다.[^news]

넷째 갈래는 **비전-언어 모델의 공간 추론**이다. 그림과 글을 함께 다루는 인공지능이 장면을 다른 사람의 시점에서 헤아리거나 조금 옮긴 시점에서 어떻게 보일지 이해하게 하는 연구다. 대표 논문에서는 사람이 머릿속 그림으로 시점을 바꾼다는 점에 착안해 장면을 추상화한 뒤 시점을 바꾸는 틀 APC를 제안했고,[^p7] 그림의 화소 대신 모델 안의 이미지 토큰을 옮겨 가까운 시점에서의 모습을 추론하게 하는 방법을 보였다.[^p8] 연구실 누리집은 글로 그림을 만들 때 여러 물체의 3차원 방향을 지정하는 ORIGEN(NeurIPS 2025)도 같은 시기 연구로 든다.[^home] 이 밖에 연구실 누리집은 선형 편미분방정식(공간과 시간에 따라 바뀌는 양을 다루는 방정식)을 위한 신경 연산자 Neural Green's Functions(NeurIPS 2025)를 들고,[^home] 최근 논문 목록에는 편미분방정식 풀이의 장기 예측 계획을 다룬 DiffusionRollout(TMLR)과 한 단계로 행동을 만들어 내는 생성형 정책 Drifting Field Policy(NeurIPS 2026)도 있다.[^pubs]

## 주요 연구 주제

### 1. 확산·흐름 생성 모델의 생성 과정 조절과 빠른 생성

그림을 만드는 도중 보상에 맞추는 표본 추출(Ψ-Sampler), 적은 단계 생성을 위한 생성 경로 학습(BézierFlow).[^p1][^p2] 대표 논문 1, 2.

### 2. 여러 생성 과정을 맞물리는 동기화 생성

파노라마·메시 텍스처·3D 가우시안 스플랫 텍스처를 추가 학습 없이 만드는 동기화 확산(SyncTweedies), 3차원 메시용 재질 무늬 생성(MatLat).[^p3][^p4] 대표 논문 3, 4.

### 3. 3차원 형상의 생성·변형·편집

부품 단위 3차원 모양 생성과 편집(SALAD), 그럴듯함을 지키는 메시 변형(As-Plausible-As-Possible).[^p5][^p6] 대표 논문 5, 6.

### 4. 비전-언어 모델의 공간 추론

다른 사람의 시점에서 장면을 헤아리는 추론(APC), 토큰을 옮겨 가까운 시점을 이해하는 방법(Token Warping).[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

최근 5년 논문 가운데 성민혁 교수가 마지막 저자인 것에서 연구 갈래마다 두 편씩 골랐고, 2026년 논문 세 편을 넣었다. 연구실은 주로 학회에 논문을 낸다.[^joinus] "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2025 | [Ψ-Sampler: Initial Particle Sampling for SMC-Based Inference-Time Reward Alignment in Score Models](https://doi.org/10.52202/085713-3498) · NeurIPS 2025 (Spotlight) | 점수 기반 생성 모델(잡음을 조금씩 걷어 내며 그림을 만드는 생성 모델)이 그림을 만드는 시점(추론 시점)에 결과를 보상(사용자가 원하는 성질을 점수로 매긴 값)에 맞추게 하는 틀을 제안했다. 이런 추론 시점 보상 정렬은 최근 크게 주목받고 있으며, 그 중심에는 여러 후보(입자)를 함께 굴리며 좋은 것을 남기는 순차 몬테카를로(SMC) 기법을 잡음 제거 과정에 쓰는 방법이 있다. 그런데 기존 방법은 입자를 가우스 사전 분포(보상과 무관한 기본 잡음 분포)에서 뽑아 시작하므로 보상과 관련된 영역을 잘 담지 못하고 표본 추출 효율이 떨어진다. 연구진은 보상을 반영한 사후 분포에서 입자를 뽑아 시작하면 정렬 성능이 크게 좋아짐을 보였고, 차원이 높은 잠재 공간에서 이렇게 뽑기 위해 차원이 커져도 잘 작동하는 제안과 기울기 정보를 함께 쓰는 pCNL 알고리즘을 도입했다. 배치(레이아웃)에 맞춰 그리기, 개수에 맞춰 그리기, 미적 선호에 맞춰 그리기 같은 여러 보상 정렬 과제에서 성능이 꾸준히 좋아졌다.[^p1] | 공동 1저자 T. Yoon·Y. Min·K. Yeo(랩 표기 * equal contributions), 마지막 저자 성민혁 |
| 2 | 2026 | [BézierFlow: Learning Bézier Stochastic Interpolant Schedulers for Few-Step Generation](https://arxiv.org/abs/2512.13255) · ICLR 2026 | 미리 학습된 확산·흐름 모델이 적은 단계만으로 그림을 만들도록 돕는 가벼운 학습 방법이다. 모델 계산 횟수(NFE) 10회 이하로 그림을 만들 때 성능을 2–3배 높이면서 학습에는 15분만 든다. 최근의 가벼운 학습 방법들은 어느 시점들을 거칠지를 배우는 데 그쳤는데, 연구진은 생성 경로를 어떻게 바꿀지를 배우도록 범위를 넓혀 확률 보간 스케줄러(잡음과 그림 사이의 경로를 정하는 함수)를 매개변수로 나타냈다. 이 함수는 양 끝 조건, 미분 가능성, 신호 대 잡음비가 한 방향으로만 바뀌는 성질을 지켜야 하는데, 이를 베지에 함수(몇 개의 조절점으로 모양이 정해지는 매끄러운 곡선)로 나타내 조절점이 이 성질들을 저절로 지키게 했다. 그러면 문제가 시간 범위 안의 순서 있는 점들을 배우는 일로 줄어든다. 여러 사전 학습 확산·흐름 모델에서 기존의 시점 학습 방법보다 꾸준히 나았다.[^p2] | 공동 1저자 Y. Min·J. Koo(랩 표기 * equal contributions), 마지막 저자 성민혁 |
| 3 | 2024 | [SyncTweedies: A General Generative Framework Based on Synchronized Diffusions](https://doi.org/10.52202/079017-3016) · NeurIPS 2024 | 미리 학습된 이미지 확산 모델 하나로 두 가지로 보이는 그림(ambiguous image), 파노라마, 3차원 메시의 표면 무늬, 3D 가우시안 스플랫(흐릿한 작은 점들을 모아 입체를 나타내는 방식)의 표면 무늬 같은 여러 시각 콘텐츠를 만드는 확산 동기화 틀을 제안했다. 먼저 여러 확산 과정을 하나의 기준 공간(정준 공간)을 통해 맞물리는 여러 경우를 분석했고, 이를 바탕으로 여러 공간에서 잡음을 걷어 내면서 트위디 공식(잡음 섞인 값에서 원래 값을 추정하는 공식)의 출력을 평균 내는 SyncTweedies를 내놓았다. 미세 조정으로 동기화하던 이전 연구와 달리 추가 학습이 필요 없어, 인터넷 규모 이미지로 학습한 모델의 풍부한 사전 지식을 특정 분야에 치우치지 않고 그대로 살린다. 여러 응용에 가장 넓게 쓸 수 있고 응용마다 기존 최고 방법보다 성능이 나았다고 보고했다.[^p3] | 공동 1저자 J. Kim·J. Koo·K. Yeo(랩 표기 * equal contributions), 마지막 저자 성민혁 |
| 4 | 2026 | [MatLat: Material Latent Space for PBR Texture Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_MatLat_Material_Latent_Space_for_PBR_Texture_Generation_CVPR_2026_paper.html) · CVPR 2026 (Highlight) | 주어진 3차원 메시 위에 PBR 텍스처(빛의 반사를 물리 법칙에 맞춰 계산하는 렌더링에 쓰는, 재질 정보를 담은 표면 무늬)를 높은 품질로 만드는 생성 틀이다. 큰 PBR 텍스처 데이터 묶음이 드물기 때문에, 미리 학습된 잠재 이미지 생성 모델(그림을 압축한 잠재 공간에서 만드는 모델)의 임베딩 공간과 확산 사전 지식을 살리면서 재질 잠재 공간 MatLat을 맞춤 미세 조정으로 배운다. 임베딩 신경망을 고정해 두는 기존 방법은 PBR 채널을 더 넣을 때 분포가 어긋나 뒤이은 확산 학습을 방해하는데, 연구진은 사전 학습된 VAE(그림을 잠재 공간으로 압축했다가 되살리는 신경망)를 미세 조정해 새 재질 채널을 넣어도 잠재 분포가 거의 바뀌지 않게 했다. 또 여러 시점에서 본 모습을 맞추려면 대응 관계를 보는 어텐션만으로는 부족하고 잠재와 그림 사이의 대응이 위치를 지켜야 함을 보였고, 잠재 조각을 잘라 되살린 뒤 그림의 해당 부분과 맞추는 정규화를 넣었다. 실험에서 PBR 텍스처의 충실도가 좋아졌고 각 구성 요소가 모두 중요했다.[^p4] | 1저자 K. Yeo, 마지막 저자 성민혁 |
| 5 | 2023 | [SALAD: Part-Level Latent Diffusion for 3D Shape Generation and Manipulation](https://doi.org/10.1109/iccv51070.2023.01328) · ICCV 2023 | 부품 단위의 암시적 3차원 표현(모양을 점이나 면 목록 대신 함수로 나타내는 방식)을 바탕으로 한 단계식(캐스케이드) 확산 모델을 제안했다. 생성 품질이 뛰어나면서, 조건을 주는 설정에서 추가 학습 없이 부품 단위로 모양을 편집하고 조작할 수 있다. 기존 3차원 확산 모델 연구는 여러 데이터 표현으로 생성 능력을 높이는 데 집중했으나 구조 정보가 없어 빈 곳 채우기와 편집에 한계가 있었다. 부품의 고차원 표현을 잘 배우도록 먼저 부품의 외부 매개변수를 담은 낮은 차원 공간에서, 그다음 부품의 고유 속성을 담은 높은 차원 공간에서 확산을 배우는 두 단계 구조를 썼다. 실험에서 생성과 부품 단위 채우기·조작 모두 기존 방법보다 나았다.[^p5] | 공동 1저자 J. Koo·S. Yoo·M. H. Nguyen(랩 표기 * equal contributions), 마지막 저자 성민혁 |
| 6 | 2024 | [As-Plausible-As-Possible: Plausibility-Aware Mesh Deformation Using 2D Diffusion Priors](https://doi.org/10.1109/cvpr52733.2024.00413) · CVPR 2024 | 사용자가 메시의 모양을 바꿀 때 결과가 그럴듯하게 남도록 2차원 확산 모델의 사전 지식을 쓰는 메시 변형 기법(APAP)이다. 변형은 면마다의 야코비 행렬(면이 늘어나고 돌아가는 정도를 담은 값)로 나타내고, 꼭짓점 좌표는 미분 가능한 푸아송 풀이로 계산한다. 변형된 메시를 그림으로 그려 점수 증류 샘플링(SDS, 이미지 확산 모델이 그림을 고칠 방향을 알려 주게 하는 방법)에 넣어 그럴듯함에 관한 사전 지식을 뽑고, 고친 메시가 원래 물체다움을 잃지 않도록 확산 모델을 LoRA(일부 변수만 고치는 가벼운 미세 조정)로 조정한다. SDS에서 얻은 기울기와 사용자가 지정한 손잡이 이동을 면마다의 야코비 행렬로 되돌려 보내고, 반복 경사 하강으로 사용자 편집과 결과의 그럴듯함 사이의 균형을 맞춘다. 2차원·3차원 메시에서 기존 기법이 쓰던 모양 보존·뒤틀림 최소화 기준보다 질적·양적으로 나아졌다.[^p6] | 공동 1저자 S. Yoo·K. Kim(랩 표기 * equal contributions), 마지막 저자 성민혁 |
| 7 | 2025 | [Perspective-Aware Reasoning in Vision-Language Models via Mental Imagery Simulation](https://doi.org/10.1109/iccv51701.2025.00863) · ICCV 2025 | 비전-언어 모델(VLM, 그림과 글을 함께 다루는 인공지능)이 머릿속 그림(심상)을 흉내 내어 다른 시점에서 추론하게 하는 틀이다. 다른 시점에서 환경이나 상황을 보는 능력(관점 취하기)은 사람 수준의 시각 이해를 재는 중요한 기준이고 환경과 상호작용하거나 자율 에이전트와 협업하는 데 꼭 필요하지만, 최근 연구에 따르면 지금의 VLM은 이 능력이 크게 모자라고 자기 시점으로 해석하는 경향이 강하다. 연구진은 사람이 추상화된 표현으로 시점을 바꾼다는 점에 주목해, 물체 검출·분할·방향 추정 같은 시각 기반 모델로 장면을 추상화하고 시점을 바꾸는 APC(Abstract Perspective Change)를 제안했다. 합성 그림과 실제 사진 벤치마크에서 여러 VLM보다 크게 나아졌고, 공간 추론용으로 미세 조정한 모델과 새 시점 영상 합성에 기반한 방법보다도 나았다.[^p7] | 1저자 P. Y. Lee, 마지막 저자 성민혁 |
| 8 | 2026 | [Token Warping Helps MLLMs Look from Nearby Viewpoints](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Token_Warping_Helps_MLLMs_Look_from_Nearby_Viewpoints_CVPR_2026_paper.html) · CVPR 2026 | 멀티모달 대형 언어 모델(MLLM, 그림과 글을 함께 다루는 대형 언어 모델)이 가까운 다른 시점에서 장면이 어떻게 보일지 이해하도록, 화소 대신 토큰(모델이 그림을 잘게 나눠 다루는 단위)을 옮기는(워핑) 방법을 살폈다. MLLM은 시각 추론을 잘하지만 시점 변화에 약하고, 화소 단위 워핑은 작은 깊이 오차에도 민감해 모양이 일그러지기 쉽다. 사람이 시점을 바꿀 때 부분 단위의 구조적 표현을 쓴다는 심상 이론에 기대어, ViT(그림을 조각으로 나눠 처리하는 신경망) 기반 MLLM의 이미지 토큰이 시점 변환의 바탕이 될 수 있는지 시험했다. 앞으로 옮기는 방식과 뒤로 옮기는 방식을 비교한 결과, 목표 시점에 촘촘한 격자를 깔고 격자점마다 원래 시점의 토큰을 가져오는 뒤로 옮기기가 더 안정적이고 의미의 일관성을 잘 지켰다. 연구진이 만든 ViewBench 벤치마크에서 토큰 단위 워핑은 화소 워핑, 공간 추론용 미세 조정 MLLM, 생성형 워핑 방법을 포함한 모든 비교 대상보다 꾸준히 나았다.[^p8] | 공동 1저자 P. Y. Lee·C. Park(랩 표기 * equal contributions), 마지막 저자 성민혁 |

## 교수와 전문 분야

성민혁 교수(Minhyuk Sung)는 KAIST AI컴퓨팅학과 부교수(Associate Professor)이고 전산학부, AI대학원(Graduate School of AI), 메타버스 프로그램(Metaverse Program)에도 소속돼 있다.[^prof] AI컴퓨팅학과 교수진 목록은 직위를 전임교수로, 전산학부 교수진 목록은 부교수로 적고, 전산학부 목록의 연구 분야는 기계 학습, 컴퓨터 그래픽, 컴퓨터 비전, 기하학 처리다.[^aic][^cs] 메타버스대학원 교수진 목록은 겸임으로 표시하고 소속을 전산학부, 분야를 3D 머신 러닝과 CG/CV로 적는다.[^metaprof] KAIST에 오기 전에는 Adobe Research의 연구 과학자였고, 스탠퍼드대에서 Leonidas Guibas 교수의 지도로 박사 학위를, KAIST에서 학사와 석사 학위를 받았다.[^prof] 석사 논문은 「A Spectral Approach to Shape Matching Using a Heat Kernel Function」(KAIST, 2010), 박사 논문은 「Learning and Exploring the Compositional Structure of 3D Data」(스탠퍼드대, 2019)다.[^pubs] 교수는 자신의 연구가 이미지·영상·3차원 데이터를 포함한 여러 시각 데이터를 만들고, 조작하고, 분석하는 데 초점을 둔다고 소개한다.[^prof]

교수는 2024년 Asiagraphics Young Researcher Award를 받았다.[^prof][^news] 연구실 소식에 따르면 2025년 2월 KAIST의 Prize for Excellence in Teaching을, 2025년 12월 KAIST의 2025 College of Engineering Technology Innovation Award를 받았다.[^news] 학계 활동으로는 CVPR 2027, ICLR 2027, 3DV 2027의 area chair와 AAAI 2027 senior program committee member를 맡고 있다.[^prof] 연구실 소식에 따르면 학술지 TMLR의 Action Editor(2026년 6월 소식)와 학술지 Graphical Models의 associate editor(2022년 8월 소식)를 맡았고, 한국컴퓨터그래픽스학회(KCGS) 2026 학술대회 공동 프로그램 위원장, SIGGRAPH Asia 2022·2023 technical paper committee member, Pacific Graphics 2023 program committee member 겸 local arrangement chair, AAAI 2023 senior program committee member, Eurographics 2022 International Program Committee member로 일했다.[^news] 확산 모델을 주제로 SIGGRAPH 2024·2025와 Eurographics 2024에서, 3차원 생성 모델을 주제로 Pacific Graphics 2023에서 튜토리얼을 했고, CVPR 2023과 ICCV 2021의 「Structural and Compositional Learning on 3D Data」 워크숍, CVPR 2026의 2nd Workshop on Multimodal Spatial Intelligence, NeurIPS 2026의 BeNTo 워크숍을 함께 열었다.[^news]

강의로는 3차원 데이터를 위한 기계 학습(CS479), 확산·흐름 모델(CS492), 생성 모델 입문(AIC313/CS378), 컴퓨터 그래픽스(CS380, CS580), 기하 모델링과 처리(CS492)를 맡아 왔다.[^courses]

논문으로 보면 전문 분야는 네 갈래다. 첫째, 확산·흐름 생성 모델이 그림을 만드는 과정을 보상에 맞추거나 더 적은 단계로 줄이는 방법이다(대표 논문 1, 2).[^p1][^p2] 둘째, 여러 확산 과정을 맞물려 파노라마와 3차원 표면 무늬를 만드는 방법이다(대표 논문 3, 4).[^p3][^p4] 셋째, 3차원 모양의 생성·편집·변형이다(대표 논문 5, 6).[^p5][^p6] 넷째, 그림과 글을 다루는 인공지능의 시점 추론이다(대표 논문 7, 8).[^p7][^p8] 2020년 이전 논문으로는 3차원 모델링 부품 추천(ComplementMe, SIGGRAPH Asia 2017)과 모양 변형 옮기기(DeformSyncNet, SIGGRAPH Asia 2020)처럼 3차원 모양의 구조와 변형을 다룬 논문이 있다.[^pubs]

## 응용 분야

대표 논문이 직접 든 쓰임은 다음과 같다. 그림 생성을 원하는 배치·개수·미적 선호에 맞추는 일,[^p1] 파노라마 그림과 3차원 메시·3D 가우시안 스플랫의 표면 무늬를 만드는 일,[^p3] 3차원 메시에 실제 같은 재질 무늬를 입히는 일,[^p4] 사용자가 3차원 메시를 그럴듯하게 고치는 일이다.[^p6] 관점 취하기 연구는 이 능력이 환경과 상호작용하고 자율 에이전트와 협업하는 데 꼭 필요하다고 본다.[^p7] 연구실 누리집은 NeRF·3D 가우시안 스플래팅·SVG 편집에 쓸 수 있는 최적화 방법과 선형 편미분방정식을 푸는 신경 연산자도 연구 성과로 든다.[^home]

연구실 소식에는 산업계와의 교류도 보인다. 교수는 NVIDIA, Google, Adobe Research, Netflix, LG AI Research 등에서 강연을 했고,[^news] 학생들은 Adobe Research(2024)와 Amazon(2025)에서 인턴을 했으며 2026년에는 Google DeepMind, Netflix, Meta에 학생 연구원으로 간다고 적는다.[^news] 학생들은 Qualcomm Innovation Fellowship(2022, 2025)을 받았다.[^news]

## 구성원

2026년 10월 22일 랩 Members 페이지 기준이다. Ph.D. Students, Master's Students, Undergraduate Students 칸의 구성원이며, 과정은 카드의 표기(Ph.D. Student, M.S. Student)와 칸 이름을 옮겼다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다. Phillip (Yuseung) Lee는 논문에 Phillip Y. Lee 또는 Yuseung Lee로 올라 있다.[^pubs]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Juil Koo | 박사과정 | 2, 3, 5, 8 |
| Jaihoon Kim | 박사과정 | 3, 4 |
| Seungwoo Yoo | 박사과정 | 2, 5, 6, 8 |
| Phillip (Yuseung) Lee | 박사과정 | 7, 8 |
| Jisung Hwang | 박사과정 |  |
| Mingue Park | 박사과정 | 8 |
| Chanho Park | 석사과정 | 7, 8 |
| Prin Phunyaphibarn | 석사과정 |  |
| Daehyeon Choi | 석사과정 |  |
| Yunhong Min | 석사과정 | 1, 2, 4 |
| Kyeongmin Yeo | 석사과정 | 1, 3, 4 |
| Byoungkwon Kim | 석사과정 |  |
| Jiwon Choi | 석사과정 |  |
| Yunjae Jeong | 석사과정 |  |
| Sangwoo Youn | 학부 연구생 |  |
| Seungjun Kim | 학부 연구생 |  |
| Heeyeon Hwang | 학부 연구생 |  |
| Jongwook Jeon | 학부 연구생 |  |
| Juneha Hwang | 학부 연구생 |  |
| Ualibyek Nurgulan | 학부 연구생 |  |

## 졸업생과 이전 구성원

랩 Members 페이지 Alumni 칸의 4명이다. 학위와 연도는 랩 표기다.[^members]

| 이름 | 학위·과정 (연도) |
|---|---|
| Hyunjin Kim | M.S. (2024) |
| Kunho Kim | M.S. (2024) |
| Eunji Hong | M.S. (2024) |
| Taehoon Yoon | M.S. (2026) |

Visitors 칸에는 다음 다섯 명이 랩이 적은 기간과 함께 올라 있다.[^members]

| 이름 | 랩이 적은 기간 |
|---|---|
| Guillaume Vitalis | Mar 2026 - Present |
| Nail Ibrahimli | May 2025 - Dec 2025 |
| Wei-Tung Lin | Sep 2024 - Jan 2025 |
| Daniel Korth | Mar 2024 - Jul 2024 |
| Jihyeon Je | Jun 2023 - Aug 2023 |

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 2021–2026년 연도 구역 56편이다. 연도는 페이지의 연도 구역이고, 제목·저자·학회 이름과 학회 이름 뒤 괄호의 발표 형식(Oral, Spotlight, Highlight 등)은 랩 표기 그대로다. 저자 이름 뒤 \*와 그 뜻을 밝힌 괄호(공동 1저자 equal contributions, 공동 교신저자 co-corresponding authors)도 랩 표기다.[^pubs]

**2026**

- Kyeongmin Yeo\*, Yunhong Min\*, Minhyuk Sung (\* equal contributions). "MUNI: Multimodal Unified Latent Diffusion for Coherent Any-to-Any Generation". *NeurIPS 2026*.
- Jaihoon Kim, Taehoon Yoon, Prin Phunyaphibarn, Seungjun Kim, Morteza Mardani, Minhyuk Sung. "Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion". *NeurIPS 2026*.
- Chanho Park, Daehyeon Choi, Jihyun Lee, Minhyuk Sung. "Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information". *NeurIPS 2026*.
- Juil Koo, Mingue Park, Jiwon Choi, Yunhong Min, Minhyuk Sung. "Drifting Field Policy: A One-Step Generative Policy via Wasserstein Gradient Flow". *NeurIPS 2026*.
- Jisung Hwang, Yunhong Min, Jaihoon Kim, I-Chao Shen\*, Minhyuk Sung\* (\* co-corresponding authors). "NoiseTilt: Noise-Tilted Reverse Kernels for Diffusion Reward Alignment". *ECCV 2026*.
- Mingue Park\*, Prin Phunyaphibarn\*, Phillip Y. Lee, Minhyuk Sung (\* equal contributions). "DiverseVAR: Balancing Diversity and Quality of Next-Scale Visual Autoregressive Models". *ECCV 2026*.
- Taeyeon Kim\*, Youngju Na\*, Jumin Lee, Minhyuk Sung, Sung-eui Yoon (\* equal contributions). "MorphGS: Morphology-Adaptive Articulated 3D Motion Transfer from Videos". *ECCV 2026*.
- Jisung Hwang, Minhyuk Sung. "Gradient Preconditioning for Efficient and Reliable Reward-Guided Generation". *ICML 2026*.
- Kyeongmin Yeo, Yunhong Min, Jaihoon Kim, Minhyuk Sung. "MatLat: Material Latent Space for PBR Texture Generation". *CVPR 2026 (Highlight)*.
- Phillip Y. Lee\*, Chanho Park\*, Mingue Park, Seungwoo Yoo, Juil Koo, Minhyuk Sung (\* equal contributions). "Token Warping Helps MLLMs Look from Nearby Viewpoints". *CVPR 2026*.
- Jaihoon Kim, Rajarshi Saha, Minhyuk Sung, Youngsuk Park. "Demystifying Transition Matching: When and Why It Can Beat Flow Matching". *AISTATS 2026*.
- Yunhong Min\*, Juil Koo\*, Seungwoo Yoo, Minhyuk Sung (\* equal contributions). "BézierFlow: Learning Bézier Stochastic Interpolant Schedulers for Few-Step Generation". *ICLR 2026*.
- Mingue Park\*, Jisung Hwang\*, Seungwoo Yoo\*, Kyeongmin Yeo, Minhyuk Sung (\* equal contributions). "PairFlow: Closed-Form Source-Target Coupling for Few-Step Generation in Discrete Flow Models". *ICLR 2026*.
- Seungwoo Yoo\*, Juil Koo\*, Daehyeon Choi\*, Minhyuk Sung (\* equal contributions). "DiffusionRollout: Uncertainty-Aware Rollout Planning in Long-Horizon PDE Solving". *TMLR*.
- Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung. "Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation". *3DV 2026*.
- Juil Koo\*, Wei-Tung Lin\*, Chanho Park, Chanhyeok Park, Minhyuk Sung (\* equal contributions). "BoxSplitGen: A Generative Model for 3D Part Bounding Boxes in Varying Granularity". *WACV 2026*.
- Prin Phunyaphibarn, Phillip Y. Lee, Jaihoon Kim, Minhyuk Sung. "Unconditional Priors Matter! Improving Conditional Generation of Fine-Tuned Diffusion Models". *WACV 2026*.

**2025**

- Taehoon Yoon\*, Yunhong Min\*, Kyeongmin Yeo\*, Minhyuk Sung (\* equal contributions). "Ψ-Sampler: Initial Particle Sampling for SMC-Based Inference-Time Reward Alignment in Score Models". *NeurIPS 2025 (Spotlight)*.
- Jaihoon Kim\*, Taehoon Yoon\*, Jisung Hwang\*, Minhyuk Sung (\* equal contributions). "Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing". *NeurIPS 2025*.
- Yunhong Min\*, Daehyeon Choi\*, Kyeongmin Yeo, Jihyun Lee, Minhyuk Sung (\* equal contributions). "ORIGEN: Zero-Shot 3D Orientation Grounding in Text-to-Image Generation". *NeurIPS 2025*.
- Jisung Hwang, Jaihoon Kim, Minhyuk Sung. "Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models". *NeurIPS 2025*.
- Seungwoo Yoo, Kyeongmin Yeo, Jisung Hwang, Minhyuk Sung. "Neural Green’s Functions". *NeurIPS 2025*.
- Phillip Y. Lee, Jihyeon Je, Chanho Park, Mikaela Angelina Uy, Leonidas Guibas, Minhyuk Sung. "Perspective-Aware Reasoning in Vision-Language Models via Mental Imagery Simulation". *ICCV 2025*.
- Chunsan Hong, Tae-Hyun Oh\*, Minhyuk Sung\* (\* co-corresponding authors). "MemBench: Memorized Image Trigger Prompt Dataset for Diffusion Models". *TMLR*.
- Juil Koo, Paul Guerrero, Chun-Hao Paul Huang, Duygu Ceylan, Minhyuk Sung. "VideoHandles: Editing 3D Object Compositions in Videos Using Video Generative Priors". *CVPR 2025*.
- Jihyun Lee, Weipeng Xu, Alexander Richard, Shih-En Wei, Shunsuke Saito, Shaojie Bai, Te-Li Wang, Minhyuk Sung, Tae-Kyun Kim, Jason Saragih. "REWIND: Real-Time Egocentric Whole-Body Motion Diffusion with Exemplar-Based Identity Conditioning". *CVPR 2025*.
- Kyeongmin Yeo\*, Jaihoon Kim\*, Minhyuk Sung (\* equal contributions). "StochSync: Stochastic Diffusion Synchronization for Image Generation in Arbitrary Spaces". *ICLR 2025*.

**2024**

- Jaihoon Kim\*, Juil Koo\*, Kyeongmin Yeo\*, Minhyuk Sung (\* equal contributions). "SyncTweedies: A General Generative Framework Based on Synchronized Diffusions". *NeurIPS 2024*.
- Seungwoo Yoo, Juil Koo, Kyeongmin Yeo, Minhyuk Sung. "Neural Pose Representation Learning for Generating and Transferring Non-Rigid Object Poses". *NeurIPS 2024*.
- Phillip Y. Lee\*, Taehoon Yoon\*, Minhyuk Sung (\* equal contributions). "GrounDiT: Grounding Diffusion Transformers via Noisy Patch Transplantation". *NeurIPS 2024*.
- Eunji Hong, Nguyen Minh Hieu, Mikaela Angelina Uy, Minhyuk Sung. "MV2Cyl: Reconstructing 3D Extrusion Cylinders from Multi-View Images". *NeurIPS 2024*.
- Jisung Hwang, Minhyuk Sung. "Occupancy-Based Dual Contouring". *SIGGRAPH Asia 2024*.
- Phillip Y. Lee, Minhyuk Sung. "ReGround: Improving Textual and Spatial Grounding at No Cost". *ECCV 2024*.
- Hyunjin Kim, Minhyuk Sung. "PartSTAD: 2D-to-3D Part Segmentation Task Adaptation". *ECCV 2024*.
- Juil Koo, Chanho Park, Minhyuk Sung. "Posterior Distillation Sampling". *CVPR 2024*.
- Seungwoo Yoo\*, Kunho Kim\*, Vladimir Kim, Minhyuk Sung (\* equal contributions). "As-Plausible-As-Possible: Plausibility-Aware Mesh Deformation Using 2D Diffusion Priors". *CVPR 2024*.
- Jihyun Lee, Shunsuke Saito, Giljoo Nam, Minhyuk Sung, Tae-Kyun Kim. "InterHandGen: Two-Hand Interaction Generation via Cascaded Reverse Diffusion". *CVPR 2024*.
- Chanhyeok Park, Minhyuk Sung. "Split, Merge, and Refine: Fitting Tight Bounding Boxes via Over-Segmentation and Iterative Search". *3DV 2024*.

**2023**

- Yuseung Lee, Kunho Kim, Hyunjin Kim, Minhyuk Sung. "SyncDiffusion: Coherent Montage via Synchronized Joint Diffusions". *NeurIPS 2023*.
- Jihyun Lee, Junbong Jang, Donghwan Kim, Minhyuk Sung, Tae-Kyun Kim. "FourierHandFlow: Neural 4D Hand Representation Using Fourier Query Flow". *NeurIPS 2023*.
- Kunho Kim\*, Mikaela Angelina Uy\*, Despoina Paschalidou, Alec Jacobson, Leonidas Guibas, Minhyuk Sung (\* equal contributions). "OptCtrlPoints: Finding the Optimal Control Points for Biharmonic 3D Shape Deformation". *Pacific Graphics 2023 (Full Paper)*.
- Juil Koo\*, Seungwoo Yoo\*, Minh Hieu Nguyen\*, Minhyuk Sung (\* equal contributions). "SALAD: Part-Level Latent Diffusion for 3D Shape Generation and Manipulation". *ICCV 2023*.
- Jihyun Lee, Minhyuk Sung, Honggyu Choi, Tae-Kyun Kim. "Im2Hands: Learning Attentive Implicit Representation of Interacting Two-Hand Shapes". *CVPR 2023*.
- Panos Achlioptas, Ian Huang, Minhyuk Sung, Sergey Tulyakov, Leonidas Guibas. "ShapeTalk: A Language Dataset and Framework for 3D Shape Edits and Deformations". *CVPR 2023*.
- Junghyun Kim, Kaichun Mo, Minhyuk Sung\*, Woontack Woo\* (\* co-corresponding authors). "Seg&Struct: The Interplay Between Part Segmentation and Structure Inference for 3D Shape Parsing". *WACV 2023*.

**2022**

- Ian Huang, Panos Achlioptas, Tianyi Zhang, Sergei Tulyakov, Minhyuk Sung, Leonidas Guibas. "LADIS: Language Disentanglement for 3D Shape Editing". *Findings of EMNLP 2022*.
- Kai Wang, Paul Guerrero, Vladimir Kim, Siddhartha Chaudhuri, Minhyuk Sung, Daniel Ritchie. "The Shape Part Slot Machine: Contact-based Reasoning for Generating 3D Shapes from Parts". *ECCV 2022*.
- Juil Koo, Ian Huang, Panos Achlioptas, Leonidas Guibas, Minhyuk Sung. "PartGlot: Learning Shape Part Segmentation from Language Reference Games". *CVPR 2022 (Oral)*.
- Jihyun Lee\*, Minhyuk Sung\*, Hyunjin Kim, Tae-Kyun Kim (\* equal contributions). "Pop-Out Motion: 3D-Aware Image Deformation via Learning the Shape Laplacian". *CVPR 2022*.
- Mikaela Angelina Uy\*, Yen-yu Chang\*, Minhyuk Sung, Purvi Goel, Joseph Lambourne, Tolga Birdal, Leonidas Guibas (\* equal contributions). "Point2Cyl: Reverse Engineering 3D Objects from Point Clouds to Extrusion Cylinders". *CVPR 2022*.

**2021**

- Youngsun Kwon, Minhyuk Sung\*, Sung-Eui Yoon\* (\* co-corresponding authors). "Implicit LiDAR Network: LiDAR Super-Resolution via Interpolation Weight Prediction". *ICRA 2022*.
- Eric-Tuan Lê, Minhyuk Sung, Duygu Ceylan, Radomír Měch, Tamy Boubekeur, Niloy Mitra. "CPFN: Cascaded Primitive Fitting Networks for High-Resolution Point Clouds". *ICCV 2021*.
- Jinwoo Lee, Hyunsung Go, Hyunjoon Lee, Sunghyun Cho, Minhyuk Sung, Junho Kim. "CTRL-C: Camera calibration TRansformer with Line-Classification". *ICCV 2021*.
- Minghua Liu, Minhyuk Sung, Radomír Měch, Hao Su. "DeepMetaHandles: Learning Deformation Meta-Handles of 3D Meshes with Biharmonic Coordinates". *CVPR 2021 (Oral)*.
- Jiahui Huang, He Wang, Tolga Birdal, Minhyuk Sung, Federica Arrigoni, Shi-Min Hu, Leonidas Guibas. "MultiBodySync: Multi-Body Segmentation and Motion Estimation via 3D Scan Synchronization". *CVPR 2021 (Oral)*.
- Mikaela Angelina Uy, Vladimir G. Kim, Minhyuk Sung, Noam Aigerman, Siddhartha Chaudhuri, Leonidas Guibas. "Joint Learning of 3D Shape Retrieval and Deformation". *CVPR 2021*.

## 수상과 선정

랩 News 페이지에서 수상·장학·선정을 알린 글 17건이다. 날짜와 문구는 랩 표기 그대로다.[^news]

- Jul 2026 · Seungwoo and Kyeongmin have been selected as recipients of the Presidential Science Scholarship for Graduate Students!
- Apr 2026 · Kyeongmin’s MatLat has been selected as a CVPR 2026 Highlight!
- Dec 2025 · Minhyuk has received the 2025 College of Engineering Technology Innovation Award at KAIST.
- Dec 2025 · Daehyeon received the National Excellence Scholarship for Master’s Students in Science and Engineering.
- Nov 2025 · Yuseung won the Qualcomm Innovation Fellowship South Korea 2025 with APC (ICCV 2025 paper)!
- Jul 2025 · Kyeongmin received the Young-Han Kim Global Leader Scholarship.
- Jul 2025 · Jisung won the Outstanding Master’s Thesis Award at Korea Computer Graphics Society (KCGS 2025).
- Jun 2025 · Yunhong has been selected as one of 120 recipients of the 2nd Presidential Science Scholarship for Graduate Students out of 2,355 applicants.
- Feb 2025 · Seungwoo and Kyeongmin received the KAIST Global Leadership Award.
- Feb 2025 · Minhyuk received a Prize for Excellence in Teaching at KAIST.
- Sep 2024 · Minhyuk won the Asiagraphics Young Researcher Award in 2024.
- Aug 2024 · Juil's Posterior Distillation Sampling received the Best Paper Award at the 2024 Samsung Electronics DS-KAIST R&D Exchange Meeting.
- Apr 2024 · Seungwoo has been selected as one of 120 recipients of the 1st Presidential Science Scholarship for Graduate Students out of 2,980 applicants.
- Feb 2023 · Juil’s Master’s thesis was awarded the outstanding thesis award.
- Nov 2022 · Juil received the Qualcomm Innovation Fellowship Korea (QIFK) 2022 for his PartGlot paper.
- Jul 2022 · Juil won the Outstanding Master’s Thesis Award at Korea Computer Graphics Society (KCGS 2022).
- Sep 2021 · We have been awarded the Google exploreCSR grant for the Rising Stars 2022 program at KAIST. Stay tuned for the details of the event!

## 소식

랩 News 페이지의 나머지 글 85건이다(2021년 1월–2026년 9월). 날짜와 문구는 랩 표기 그대로다.[^news]

- Sep 2026 · Four papers have been accepted to NeurIPS 2026.
- Sep 2026 · NoiseTilt and DiverseVAR will be presented as oral presentations at the LoViF Workshop at ECCV 2026.
- Jul 2026 · We are co-organizing "BeNTo: Beyond Next-Token Prediction: Diffusion & Flow Models for Next-Generation Decoding" at NeurIPS 2026. Click to check out the workshop webpage.
- Jul 2026 · Minhyuk gave a talk at the SCALE Workshop at ICML 2026 titled "Generative Modeling for Multimodal AI Agents: Reasoning, Action, and Simulation". Click to download the slides.
- Jun 2026 · Minhyuk is serving as an Action Editor for TMLR.
- Jun 2026 · Three papers have been accepted to ECCV 2026.
- Jun 2026 · Minhyuk gave a talk at NVIDIA and Netflix titled "Generative Modeling Beyond Scale: Efficiency, Guidance, and Multimodality". Click to download the slides.
- May 2026 · Yuseung, Jaihoon, and Juil will join as student researchers at Google DeepMind, Netflix, and Meta, respectively.
- May 2026 · Minhyuk gave a talk at Singapore Vision Day 2026. Click to download the slides.
- May 2026 · One paper has been accepted to ICML 2026.
- Mar 2026 · Minhyuk gave a talk at IVSP&MLHMI 2026 conference on "Image and Video Generation: Present and Future".
- Feb 2026 · Minhyuk is serving as a co-program chair for the Korean Computer Graphics Society (KCGS) Conference 2026.
- Feb 2026 · Two papers have been accepted to CVPR 2026.
- Feb 2026 · We are organizing the 2nd Workshop on Multimodal Spatial Intelligence at CVPR 2026. The Call for Papers is now open! Click to check out the workshop webpage.
- Feb 2026 · Minhyuk gave a talk at LG AI Research titled "Toward Ambulatory Vision: Generative Action Policies for Spatial Understanding". Click to download the slides.
- Jan 2026 · Two papers have been accepted to ICLR 2026.
- Jan 2026 · One paper has been accepted to AISTATS 2026.
- Jan 2026 · One paper has been accepted to TMLR.
- Dec 2025 · Minhyuk gave a talk at UC San Diego titled "Inference-Time Guided Generation Using Diffusion and Flow Models".
- Dec 2025 · Jisung has started a visiting researcher position at the University of Tokyo.
- Nov 2025 · One paper has been accepted to 3DV 2026.
- Nov 2025 · One paper has been accepted to WACV 2026 (in the second round).
- Oct 2025 · Our group participated in OpenKAIST and presented our research on "AI techniques for perceiving the world like humans".
- Sep 2025 · Five papers have been accepted to NeurIPS 2025, including one spotlight.
- Sep 2025 · One paper has been accepted to WACV 2026 (in the first round).
- Aug 2025 · Minhyuk presented a tutorial at SIGGRAPH 2025 on "Diffusion-Based Image/Video Generation".
- Aug 2025 · Minhyuk talked about "The Present and Future of Content Generation" at the KAIST AI Transformation Workshop. Click to check out the recording.
- Aug 2025 · Minhyuk gave talks at NVIDIA, Google, Stanford, and SFU titled "Inference-Time Guided Generation Using Diffusion and Flow Models". Click to download the slides.
- Jul 2025 · Minhyuk participated as a panelist at Intel AI Summit Seoul 2025 in "Shaping a Responsible and Sustainable AI Ecosystem".
- Jul 2025 · Jaihoon begins internship at Amazon.
- Jul 2025 · Minhyuk gave lectures on diffusion models at MLSS-Senegal 2025.
- Jun 2025 · One paper has been accepted to ICCV 2025.
- Jun 2025 · One paper has been accepted to TMLR.
- Apr 2025 · Minhyuk gave talks at HKUST (as a keynote at CVM 2025) and NTU (MMLab) titled "Inference-Time Guided Generation with Diffusion and Flow Models". Click to download the slides.
- Feb 2025 · Minhyuk gave a talk at the Asiagraphics Workshop on Intelligent Graphics titled "Guidance in the Generative Process of Diffusion Models". Click to download the slides.
- Feb 2025 · Two papers have been accepted to CVPR 2025.
- Jan 2025 · One paper has been accepted to ICLR 2025.
- Dec 2024 · Minhyuk gave talks at the SIGGRAPH Asia 2024 pre-conference workshop and K-BOF on "Visual Content Generation Using Diffusion Models".
- Dec 2024 · Minhyuk gave a talk at the University of Tokyo on "Visual Content Generation with Image Diffusion Models".
- Sep 2024 · Four papers have been accepted to NeurIPS 2024.
- Sep 2024 · One paper has been accepted at SIGGRAPH Asia 2024.
- Aug 2024 · Minhyuk presented a tutorial on "Diffusion Models for Visual Content Generation" at SIGGRAPH 2024. Click here for more details.
- Jul 2024 · Minhyuk gave talks at Stanford and Adobe Research on "Visual Content Generation with Image Diffusion Models". Click here to download the slides.
- Jul 2024 · Two papers have been accepted at ECCV 2024.
- Jun 2024 · Juil begins internship at Adobe Research.
- Jun 2024 · Minhyuk presented at the 2nd Workshop on Compositional 3D Vision (C3DV) at CVPR 2024. Click here to download the slides.
- Apr 2024 · Minhyuk gave talks at TUM, ETH, and École Polytechnique on Visual Content Generation with Image Diffusion Models. Click here to download the slides.
- Apr 2024 · Minhyuk gave a tutorial on "Diffusion Models for Visual Computing" at Eurographics 2024. Click here for more details.
- Feb 2024 · Three papers have been accepted at CVPR 2024.
- Dec 2023 · Minhyuk gave a talk at NVIDIA Toronto AI Lab with the title: "Moving Beyond 3D Generation to Editing with Image Diffusion Priors". Click here to download the slides.
- Oct 2023 · One paper has been accepted at 3DV 2024.
- Oct 2023 · Minhyuk presented a tutorial at Pacific Graphics 2023 about 3D generative models. Click here for more details.
- Oct 2023 · Minhyuk gave a talk at University College London and Adobe Research Paris with the title: "Towards Shape Editability and Multi-View Consistency in 3D Generation". Click here to download the slides.
- Sep 2023 · Two papers have been accepted at NeurIPS 2023. Congratulations Yuseung on the first paper! Please check out our Hugging Face demo on our project webpage by clicking here.
- Aug 2023 · OptCtrlPoints has been accepted to Pacific Graphics 2023 as a full paper. Congrats Kunho!
- Jul 2023 · SALAD has been accepted at ICCV 2023. Kudos to Juil, Seungwoo, and Hieu! Click here to check out our Hugging Face demo on our project webpage.
- Jul 2023 · Minhyuk presented a tutorial talk at the Korea AI Association conference titled "3D Generation via 2D Priors and Neural Rendering: Recent Advances, Limitations, and Future Directions." Click here to download the slides.
- Jun 2023 · Minhyuk gave a talk about 3D generative models at the POSTECH CSE/GSAI seminar series. Click to download the slides.
- Apr 2023 · Minhyuk is serving as a technical paper committee member at SIGGRAPH Asia 2023.
- Apr 2023 · Minhyuk is serving as a program committee member and a local arrangement chair at Pacific Graphics 2023.
- Mar 2023 · Minhyuk is co-organizing a workshop at CVPR 2023: Structural and Compositional Learning on 3D Data. Click here for more details.
- Feb 2023 · Two papers have been accepted at CVPR 2023.
- Nov 2022 · We are hosting KAIST Geometric and Visual Computing Workshop (GVC Workshop). Click this for more details.
- Nov 2022 · Minhyuk gave a talk about language and 3D & differential Poisson Solver at the KAIST GSAI Colloquium. Click to download the slides.
- Oct 2022 · One paper has been accepted at WACV 2023 (Algorithm Track).
- Oct 2022 · One paper has been accepted at Findings of EMNLP 2022.
- Sep 2022 · Minhyuk is serving as a senior program committee member at AAAI 2023.
- Aug 2022 · Minhyuk gave an invited talk at the GrUVi Lab at Simon Fraser University during his visit for SIGGRAPH 2022.
- Aug 2022 · We are hosting the 2022 Women Tech Stars workshop at KAIST, supported by the Google ExploreCSR program. Click this to check out the webpage.
- Aug 2022 · Minhyuk is serving as an associate editor of Graphical Models.
- Aug 2022 · Minhyuk wrote a blog post about 'How do I structure a paper?' at SIGGRAPH Research Career Development Committee (RCDC) webpage. Click to check it out.
- Jul 2022 · Minhyuk gave an invited online talk to Mohamed Elhoseiny's group at KAUST on language and 3D.
- Jul 2022 · Minhyuk presented a keynote talk at the ICME Workshop on 3D Multimedia Analytics, Search and Generation. Click here for more details.
- Jul 2022 · Minhyuk gave a lecture on "Introduction to Neural Rendering" at the Summer School of KCGS 2022. Click to download the slides.
- Jul 2022 · One paper has been accepted at ECCV 2022.
- Jun 2022 · Minhyuk gave a talk about language and 3D at Stanford University. Click to download the slides.
- Apr 2022 · Minhyuk is serving as a technical paper committee member at SIGGRAPH Asia 2022.
- Mar 2022 · Three papers have been accepted at CVPR 2022 including Juil's oral.
- Feb 2022 · Minhyuk gave a talk at Asiagraphics as a webinar speaker. Click here for more details.
- Feb 2022 · One paper has been accepted at ICRA 2022.
- Sep 2021 · Minhyuk is serving as an International Program Committee member at Eurographics 2022.
- Jul 2021 · Two papers have been accepted at ICCV 2021.
- Apr 2021 · Minhyuk is co-organizing a workshop at ICCV 2021: Structural and Compositional Learning on 3D Data. Click here for more details.
- Mar 2021 · Three papers have been accepted at CVPR 2021 including two orals.
- Jan 2021 · We've just launched our group at KAIST!

## 연락과 위치

- 주소: KAIST Department of AI Computing, Rm. 507, Bldg. E3-5 (KRAFTON Building), 291 Daehak-ro, Yuseong-gu, Daejeon, South Korea 34141[^contact]
- 전화: +82-42-350-3587[^contact]
- 연구실 인턴 근무 장소: KAIST, KRAFTON SoC Building (E3-5), Rm 510[^intern]
- 교수연구실: 크래프톤 SoC 빌딩 (E3-5), 507호(AI컴퓨팅학과 교수진 표기)[^aic]
- 대학원 입학과 인턴 문의는 연구실 Join Us·Internship 페이지가 안내한다.[^joinus][^intern]
[^p1]: T. Yoon, Y. Min, K. Yeo, M. Sung, Advances in Neural Information Processing Systems 38, 115985-116021 (2025). <https://doi.org/10.52202/085713-3498> 초록 기준(학회 논문집 페이지 게시 초록).
[^p2]: Y. Min, J. Koo, S. Yoo, M. Sung, ICLR 2026(랩 표기), arXiv:2512.13255. <https://arxiv.org/abs/2512.13255> 초록 기준(Semantic Scholar 등록 초록, arXiv 판).
[^p3]: J. Kim, J. Koo, K. Yeo, M. Sung, Advances in Neural Information Processing Systems 37, 95198-95237 (2024). <https://doi.org/10.52202/079017-3016> 초록 기준(학회 논문집 페이지 게시 초록).
[^p4]: K. Yeo, Y. Min, J. Kim, M. Sung, Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 4602–4612 (2026). <https://openaccess.thecvf.com/content/CVPR2026/html/Yeo_MatLat_Material_Latent_Space_for_PBR_Texture_Generation_CVPR_2026_paper.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^p5]: J. Koo, S. Yoo, M. H. Nguyen, M. Sung, 2023 IEEE/CVF International Conference on Computer Vision (ICCV), 14395-14405 (2023). <https://doi.org/10.1109/iccv51070.2023.01328> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: S. Yoo, K. Kim, V. G. Kim, M. Sung, 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 4315-4324 (2024). <https://doi.org/10.1109/cvpr52733.2024.00413> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: P. Y. Lee 외, M. Sung, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 9241-9251 (2025). <https://doi.org/10.1109/iccv51701.2025.00863> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: P. Y. Lee 외, M. Sung, Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 3476–3488 (2026). <https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Token_Warping_Helps_MLLMs_Look_from_Nearby_Viewpoints_CVPR_2026_paper.html> 초록 기준(학회 논문집 페이지 게시 초록).
[^home]: 연구실 누리집 첫 화면 <https://visualai.kaist.ac.kr> (소개문, Research Highlights, 2026-10-22 열람)
[^members]: Members 페이지 <https://visualai.kaist.ac.kr/members/> (교수, 구성원, Alumni, Visitors, 2026-10-22 열람)
[^pubs]: Publications 페이지 <https://visualai.kaist.ac.kr/publications/> (논문 목록, 2026-10-22 열람)
[^news]: News 페이지 <https://visualai.kaist.ac.kr/news/> (글 102건, 2026-10-22 열람)
[^courses]: Courses 페이지 <https://visualai.kaist.ac.kr/courses/> (2026-10-22 열람)
[^joinus]: Join Us 페이지 <https://visualai.kaist.ac.kr/join_us/> (대학원생 모집 안내, 2026-10-22 열람)
[^intern]: Internship 페이지 <https://visualai.kaist.ac.kr/internship/> (인턴 모집 안내, 2026-10-22 열람)
[^contact]: Contact 페이지 <https://visualai.kaist.ac.kr/contact/> (2026-10-22 열람)
[^prof]: 교수 개인 누리집 <https://mhsung.github.io/> (소개문, News, 2026-10-22 열람)
[^aic]: KAIST AI컴퓨팅학과 교수진 <https://aicollege.kaist.ac.kr/aic/faculty> (2026-10-22 열람)
[^cs]: KAIST 전산학부 교수진 <https://cs.kaist.ac.kr/people/faculty> (2026-10-22 열람)
[^sse]: KAIST 반도체시스템공학과 연구실 목록 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^metalab]: KAIST 메타버스대학원 참여 연구실 목록 <https://meta.kaist.ac.kr/labs/> 과 KAIST Visual AI Group 소개 <https://meta.kaist.ac.kr/labs/3dai-lab> (2026-10-22 열람)
[^metaprof]: KAIST 메타버스대학원 교수진 <https://meta.kaist.ac.kr/professors/> (2026-10-22 열람)

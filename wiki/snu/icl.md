# 지능형 계산영상 연구실 (Intelligent Computational imaging Lab, ICL)

**서울대학교 공과대학 전기·정보공학부, 대학원 협동과정 인공지능전공 · 전세영 교수**

- 분야: 계산 영상과 의료 영상의 신호 처리·기계학습(확산 모델 기반 영상 역문제, 압축 센싱 표본화와 재구성, 정량 SPECT 산란 추정, 병리 전체 슬라이드 영상 분석), 확산 생성 모델의 개념 지우기와 메모리·계산 효율화, 시각-언어 모델의 객체 환각과 멀티모달 표현, 사물 어포던스 인식과 3차원 사람 복원·생성
- 대분야: 컴퓨팅·AI
- 태그: 컴퓨터 비전[^pi][^p1][^p8], 생성 인공지능[^p5][^p6], 멀티모달 AI[^home][^p7], 생물 영상 분석[^p4]
- 홈페이지: <https://icl.snu.ac.kr/>
- 근거와 출처: [ICL 근거 페이지](icl-sources.md)

> 측정의 물리에 맞춘 계산 영상에 뿌리를 두고, 그 바탕을 멀티모달 표현과 기반 모델, 물리 세계에서 행동하는 에이전트로 넓히는 연구실이다.[^home] 계산 영상과 의료 영상의 영상 복원·재구성,[^ecelabv][^pi] 확산 생성 모델의 안전과 효율,[^p5][^p6] 시각-언어 모델과 사물과의 상호작용 인식[^p7][^p8]을 연구한다.

## 무엇을 연구하나

지능형 계산영상 연구실(ICL)은 서울대학교 전기·정보공학부 전세영 교수가 이끄는 연구실이며, 누리집은 연구실이 대학원 협동과정 인공지능전공(Interdisciplinary Program in Artificial Intelligence)에도 함께 속해 있다고 적는다.[^home] 첫 화면은 연구실의 지향을 "Grounded AI that sees, reasons, and acts"(보고, 추론하고, 행동하는 근거 있는 인공지능)로 내건다. 소개 글에 따르면 연구실의 뿌리는 계산 영상(computational imaging, 센서가 잰 신호에 계산을 더해 영상을 만들어 내는 방법)이며, 수학적으로 엄밀하면서 효율적인 최적화로 모든 영상을 그 영상이 측정된 물리 과정에 맞춘다. 이 바탕을 여러 종류의 자료와 여러 규모를 함께 다루는 표현(멀티모달·멀티스케일 표현)과 기반 모델(foundation model, 많은 자료로 미리 학습해 여러 과제에 맞춰 쓰는 인공지능 모델)로 옮겨 엄밀함을 잃지 않고 규모를 키울 수 있는 알고리즘을 설계하고, 물리 세계에서 행동하며 사람과 함께 일하는 에이전트(스스로 판단해 행동하는 인공지능 프로그램)까지 잇는다고 적는다. 이때 모든 입력과 측정, 사람의 안내를 똑같이 가치 있지만 불확실한 것으로 다룬다고 밝힌다.[^home]

학과 연구실 목록은 이 연구실을 멀티미디어 신호처리, 생체전자정보, 인공지능 및 머신러닝 세 연구그룹에 함께 올린다.[^ecelab] 학과 연구실 소개는 컴퓨팅이 의료영상을 포함한 현대 이미징에서 중요한 역할을 하며 이상적이지 못한 상황에서 생기는 문제를 컴퓨팅으로 풀어 사람이 더 멀리 있는 것, 더 깊은 것, 훨씬 더 작은 것을 볼 수 있게 되었다고 쓰고, 연구실이 계산영상, 특히 의료영상을 위한 신호처리와 머신러닝을 연구한다고 적는다. 계산·의료 영상에서 생기는 문제를 일반화해 풀어서 그 해법을 컴퓨터 비전 같은 다른 응용 분야에도 쓸 수 있게 한다고 덧붙이고, 최근 관심 분야로 계산 및 의료영상, 신호처리, 머신러닝을 든다.[^ecelabv] 교수 소개 페이지는 교수의 관심을 중요도가 높은(mission-critical) 대규모 계산 영상(CI)이나 의료 영상(MI)에서 생기는 신호 처리(SP), 기계학습(ML), 물리 기반 저수준 컴퓨터 비전(low-level CV, 화소 단위로 영상 자체의 질을 다루는 컴퓨터 비전) 문제로 적고, 그 조건으로 영상 획득이 비선형인 경우, 측정과 정답 표시에 모두 잡음이 섞인 경우, 촬영 대상이 움직이는 경우를 든다. 연구실은 이런 문제를 계산·의료 영상뿐 아니라 저수준 컴퓨터 비전과 기계학습 응용에도 쓰일 알고리즘으로 풀고, 신호 처리·의료 영상 학술지와 기계학습·컴퓨터 비전 학회에 논문을 낸다고 적는다.[^pi]

첫째 갈래는 **물리에 맞춘 계산 영상과 역문제**다. 역문제(inverse problem)는 관측된 결과에서 그 결과를 만든 원인을 거꾸로 추정하는 문제로, 흐리거나 일부만 잰 측정에서 원래 영상을 되찾는 일이 여기에 든다. 대표 논문에서는 확산 모델(자료에 잡음을 더해 가는 과정을 거꾸로 되돌리도록 학습해 새 자료를 만들어 내는 생성 모델)로 영상 역문제를 풀 때 측정과 맞추는 안내, 분류기 없는 안내(조건을 준 예측과 주지 않은 예측의 차이로 생성 결과를 조건 쪽으로 끄는 방법), 무작위성이라는 세 요소의 세기를 시간에 따라 어떻게 바꿀지 함께 최적화하는 TriPS를 내놓았고,[^p1] 푸리에 압축 센싱(compressed sensing은 신호를 적은 수의 측정으로 얻고 신호의 구조적 성질을 이용해 복원하는 방법이며, 푸리에 압축 센싱은 그 측정이 신호의 주파수 성분인 경우)에서 입력 자료마다 알맞은 표본화 마스크(어느 측정값을 취할지 정한 무늬)와 재구성 신경망을 골라 쓰는 방법을 만들었다.[^p2] 최근 논문 목록에는 렌즈 없는 영상(lensless imaging, 렌즈 대신 다른 광학 부품과 계산으로 상을 얻는 영상 방식)의 역문제를 확산 모델로 푸는 연구(Image and Vision Computing, 2026), 압축 센싱 자기공명영상(MRI, Magnetic Resonance Imaging) 재구성 알고리즘(IEEE Transactions on Computational Imaging, 2025), 베이어 배열(영상 센서 화소 위에 빨강·초록·파랑 색 필터를 반복 무늬로 놓은 배열)과 비베이어 배열 영상 센서의 디모자이킹(화소마다 한 색만 잰 센서 자료에서 화소마다 모든 색을 채워 넣는 일)을 한 모델로 하는 연구(ICCV 2023)도 있다.[^pubs]

둘째 갈래는 **의료 영상**이다. 대표 논문에서는 정량 SPECT(단일 광자 방출 단층촬영, Single Photon Emission Computed Tomography는 몸에 넣은 방사성 물질이 내는 감마선을 여러 방향에서 재서 몸속 분포를 단면 영상으로 만드는 핵의학 영상이고, 정량은 영상 값으로 방사능의 양을 잰다는 뜻)에서 산란 성분(감마선이 몸속에서 방향이 바뀐 채 검출되는 성분)을 추정할 때, 짧게 돌린 몬테카를로 모사(무작위 수를 써서 결과를 어림하는 계산 방법) 결과를 약한 정답으로 삼아 신경망으로 보강하는 물리 기반 약지도 학습(정답 표시가 부정확하거나 일부만 있는 자료로 학습하는 방법) 틀을 제안했고,[^p3] 병리 전체 슬라이드 영상(WSI, Whole Slide Image: 조직 유리 슬라이드 전체를 스캔한 디지털 영상)에서 이전에 배운 과제를 적게 잊으면서 새 과제에 적응하고 영상 조각 단위로 위치도 찾는 연속 다중 인스턴스 학습(여러 조각을 묶은 단위에만 붙은 표시로 학습하는 방법) 틀 CoMEL을 만들었다.[^p4] 최근 논문 목록에는 콘빔 CT(cone-beam CT, 원뿔 꼴로 퍼지는 X선 다발로 찍는 CT이며, CT는 Computed Tomography의 줄임말로 컴퓨터 단층촬영을 뜻한다)를 적은 방향의 촬영으로 재구성하는 연구(Computers in Biology and Medicine, 2025), 여러 후속 과제에 맞춰 MR 재구성을 최적화하는 연구(MICCAI 2025)도 있다.[^pubs]

셋째 갈래는 **확산 생성 모델의 안전과 효율**이다. 대표 논문에서는 텍스트-이미지 확산 모델이 해로운 내용을 만들지 않도록 개념 지우기(생성 모델이 특정 개념을 담은 이미지를 만들지 못하게 고치는 일)를 하되, 이미지 안에서 표적 개념이 나타난 영역만 골라 지우는 학습 없는 방법 GLoCE를 내놓았고,[^p5] 텍스트 인코더(글 지시를 모델이 쓰는 숫자 표현으로 바꾸는 부분)의 일부 층을 건너뛰거나 다시 써서 메모리 사용을 줄이는 Skrr를 만들었다.[^p6] 최근 논문 목록에는 수천 개 개념을 한꺼번에 지우는 연구(CVPR 2026), 이미지의 영역마다 해상도를 달리 써서 확산 트랜스포머(트랜스포머 구조로 만든 확산 모델)의 생성을 빠르게 하는 학습 없는 방법(CVPR 2026), 양자화(모델 안의 숫자를 정해진 적은 수의 값으로 나타내는 일)한 확산 모델을 역전파(출력의 오차를 입력 쪽으로 거꾸로 전하며 신경망의 가중치마다 고칠 방향을 계산하는 방법) 없이 개인화하는 연구(CVPR 2025), 오디오 확산 모델용 워터마크(결과물에 출처나 소유를 확인할 수 있는 표시를 넣는 기술, Pattern Recognition Letters, 2025)도 있다.[^pubs]

넷째 갈래는 **멀티모달 이해와 사물과의 상호작용**이다. 대표 논문에서는 대형 시각-언어 모델(LVLM, Large Vision-Language Model: 이미지와 글을 함께 받아 글로 답하는 대형 인공지능 모델)이 이미지에 없는 물체를 설명해 버리는 객체 환각을, 비전 인코더(이미지를 모델이 쓰는 표현으로 바꾸는 부분) 안의 불확실한 시각 토큰(이미지 조각마다 만든 표현)을 가려서 줄였고,[^p7] 물체에 담긴 상호작용 가능성인 어포던스(affordance)를 행동하는 사람 바깥에서 찍은 이미지만으로 대조 학습(같은 것끼리는 가깝게, 다른 것끼리는 멀게 표현을 배우는 방법)해 이미지에서 짚어 내는 INTRA를 만들었다.[^p8] 최근 논문 목록에는 쌍곡 공간(hyperbolic space, 휘어진 정도가 어디서나 같은 음의 값을 갖는 기하 공간)에 표현을 두는 시각-언어 모델(CVPR 2026, ECCV 2026), 상호작용하는 여러 사람의 3차원 모습을 한 장의 이미지에서 복원하는 연구(CVPR 2026), 원격탐사 영상의 개방 어휘 분할(학습 때 정하지 않은 이름의 대상까지 글로 지정해 영상의 영역을 나누는 일, IEEE Access, 2026), 대형 언어 모델의 학습 뒤 압축(NeurIPS 2026 채택)도 있다.[^pubs]

과제로는 2026년 하반기 삼성미래기술육성사업에 「Forgetting as a Fundamental Operation of Intelligence」 과제가 선정되었다.[^news][^engnews] 공과대학 소식은 이 과제가 불필요한 기억을 가려서 지우는 '선택적 망각' 능력을 갖춘 AI 연구이며, AI가 기억의 향후 쓸모를 스스로 판단해 필요한 기억은 남기고 불필요한 기억은 지우는 기술을 개발할 계획이고, 개발한 기술은 영상과 언어를 함께 이해하며 장시간 대화와 작업을 이어 가는 멀티모달 AI 에이전트에서 단계적으로 검증한다고 적는다.[^engnews] 2026년 3월에는 성균관대학교(SKKU) Hoon Kim 교수와 함께 NVIDIA Academic Grant Program에 선정되어, NVIDIA가 메가베이스(megabase, DNA 길이를 염기 수로 재는 단위의 하나) 규모 DNA 기반 모델(megabase-scale DNA foundation model) 과제에 A100 GPU 32,000시간을 지원한다고 소식 페이지가 적는다.[^news]

## 주요 연구 주제

### 1. 물리에 맞춘 계산 영상과 역문제

확산 모델 사후 표집에서 측정 일관성 안내·분류기 없는 안내·무작위성의 일정 최적화(TriPS), 푸리에 압축 센싱의 자료별 표본화 마스크·재구성 신경망 선택, 렌즈 없는 영상과 디모자이킹(대표 논문 1, 2).[^p1][^p2][^pubs]

### 2. 의료 영상

정량 SPECT의 물리 기반 약지도 산란 추정, 병리 전체 슬라이드 영상의 연속 다중 인스턴스 학습(CoMEL), MR·CT 재구성(대표 논문 3, 4).[^p3][^p4][^pubs]

### 3. 확산 생성 모델의 안전과 효율

텍스트-이미지 확산 모델의 국소 개념 지우기(GLoCE)와 대규모 개념 지우기, 텍스트 인코더 층 건너뛰기·재사용(Skrr), 확산 모델의 가속과 개인화(대표 논문 5, 6).[^p5][^p6][^pubs]

### 4. 멀티모달 이해와 사물과의 상호작용

시각 토큰의 불확실성으로 본 시각-언어 모델의 객체 환각 줄이기, 외부 시점 이미지만 쓰는 약지도 어포던스 그라운딩(INTRA), 쌍곡 시각-언어 모델과 3차원 사람 복원(대표 논문 7, 8).[^p7][^p8][^pubs]

## 대표 논문

누리집 Publications 페이지의 2021–2026년 학술지·학회 정규 논문 가운데 전세영 교수가 마지막 저자인 논문을 네 연구 갈래에 두 편씩 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules](https://arxiv.org/abs/2605.26470) · ICML 2026 (확인한 판본 arXiv 2605.26470 사전 공개본) | 확산 모델로 사후 표집(관측된 측정에 맞는 원래 영상의 후보를 확률에 따라 뽑는 일)을 해서 영상 역문제를 푸는 방법이 주류가 되었다. 이 방법은 보통 측정과 맞추는 데이터 일관성(DC) 안내, 분류기 없는 안내(CFG, classifier-free guidance), 무작위성의 세 요소로 이뤄진다. 기존 연구는 각 요소를 만드는 데 집중했고, 세 요소를 언제 얼마나 쓸지 정하는 일정은 경험으로 고정하거나 일부만 조정해 왔다. 세 요소의 일정이 서로 주고받는 영향이 성능에 중요하다고 보고 분석한 결과, 표집 초반의 강한 CFG가 DC 안내와 부딪히고 무작위성은 표집 경로를 확률이 높은 영역으로 되돌린다는 점을 확인했다. 이를 바탕으로 사후 표집을 시간에 따라 바뀌는 제어 문제로 다시 세우고, DC와 무작위성의 크기는 줄이면서 CFG의 크기는 늘리는 세 요소의 추세를 따라 일정을 최적화하는 TriPS를 제안했다. 함수 형태의 사전 지식(functional priors) 위의 틀 기반 탐색으로 믿을 만한 기본 일정을 얻고, GRPO(Group Relative Policy Optimization) 기반 강화학습(행동에 따라 받는 보상으로 시행착오를 거쳐 행동 방식을 배우는 기계학습)으로 더 유연한 시간 곡선을 얻는다. 실험에서 TriPS는 최신 기준 방법들보다 데이터 충실도와 지각적 사실감이 나았다.[^p1] | 공동 1저자 Junseo Bang, Dong Ju Mun(누리집 표기 co-first authors), 마지막 저자 전세영 |
| 2 | 2024 | [Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing](https://doi.org/10.1007/978-3-031-73650-6_18) · ECCV 2024 (Lecture Notes in Computer Science) | 압축 센싱(CS)은 나이퀴스트 표본화(신호를 그대로 되살리는 데 필요하다고 표본화 이론이 정한 빠르기 이상으로 신호를 재는 방식)의 비효율을 넘으려고 나왔지만, 최적화 기반 재구성은 느리고 실제로는 정확한 영상을 얻지 못한다. 딥러닝 기반 재구성은 정확도와 계산 속도에서 최적화 기반 재구성을 앞서는 대안이지만, 특히 푸리에 CS에서 딥러닝 재구성과 함께 쓸 효율적인 표본화 방법을 찾는 일은 여전히 어렵다. 표본화 마스크(어느 측정을 취할지 정한 무늬)와 재구성을 함께 최적화하는 기존 방식(H1)은 자료마다 적응하지 않아 잠재력이 낮고, 적응형 표본화(H2)는 최적화가 어렵고 파레토 준최적(다른 성능을 해치지 않고도 어떤 성능을 더 높일 여지가 남은 상태) 문제가 있다. 입력 자료마다 가장 좋은 표본화 마스크와 재구성 신경망을 고르는 적응형 선택 틀(H1.5)을 제안하고, 이 방법이 H1보다 잠재력이 높으며 마스크마다 따로 재구성 신경망을 써서 파레토 준최적 문제를 효과적으로 푼다는 정리를 제시했다. 가장 좋은 마스크를 고르려고 초해상도(낮은 해상도의 영상에서 높은 해상도의 영상을 만들어 내는 일) 공간 생성 모델로 입력의 고주파 성분에 대한 베이즈 불확실성(확률 분포로 나타낸 추정의 불확실성)을 정량화했다. 여러 푸리에 CS 문제에서 H1과 H2보다 크게 개선했다.[^p2] | 1저자 Seongmin Hong, 마지막 저자 전세영(누리집 표기 Jongho Lee와 co-corresponding authors) |
| 3 | 2023 | [Physics-Guided Deep Scatter Estimation by Weak Supervision for Quantitative SPECT](https://doi.org/10.1109/tmi.2023.3270868) · IEEE Transactions on Medical Imaging | 정량 SPECT에서 산란(방출된 감마선이 몸속에서 방향이 바뀐 채 검출되는 성분)을 정확히 추정하는 일은 영상의 대비와 정확도를 높이는 데 중요하다. 광자 이력이 많은 몬테카를로(MC) 모사는 산란을 정확히 추정하지만 계산이 많이 들고, 최근 딥러닝 방법은 빠르게 정확한 추정을 내지만 모든 학습 자료의 정답 표시를 만들려면 여전히 완전한 MC 모사가 필요하다. 100배 짧은 MC 모사 결과를 약한 정답 표시로 쓰고 이를 심층 신경망으로 보강하는 물리 기반 약지도 학습 틀을 제안했다. 새 시험 자료가 오면 짧은 MC 모사를 한 번 더 해서 학습한 신경망을 빠르게 미세 조정할 수 있어 환자별 산란 모형화가 가능하다. 다양한 해부 구조와 방사능 분포의 XCAT 팬텀(영상 실험에 쓰는, 사람 몸을 나타낸 모형) 18개로 학습하고, XCAT 팬텀 6개, 실제와 비슷한 가상 환자 팬텀 4개, 몸통 팬텀 1개, 환자 2명의 임상 촬영 3건으로 평가했다(단일·이중 광봉우리(검출된 감마선의 에너지 분포에서 방출 에너지에 해당하는 봉우리) 113, 208 keV의 177Lu(방사성 동위원소 루테튬-177) SPECT). 팬텀 실험에서는 정답 표시를 쓰는 지도 학습과 비슷한 성능을 내면서 표시에 드는 계산을 크게 줄였고, 환자별 미세 조정을 더하면 임상 촬영에서 지도 학습보다 정확한 산란 추정을 얻었다.[^p3] | 1저자 Hanvit Kim, 마지막 저자 전세영 |
| 4 | 2025 | [Continual Multiple Instance Learning with Enhanced Localization for Histopathological Whole Slide Image Analysis](https://doi.org/10.1109/iccv51701.2025.02157) · ICCV 2025 | 다중 인스턴스 학습(MIL, 여러 조각을 묶은 단위에만 붙은 표시로 학습하는 방법)은 묶음 단위의 약한 표시만으로 학습해, 병리 전체 슬라이드 영상(WSI) 같은 큰 영상의 표시 비용을 크게 줄였다. 그러나 이전 것을 적게 잊으면서 연속된 과제에 적응하는 능력, 특히 위치를 찾기 위한 인스턴스 분류에서의 능력은 거의 연구되지 않았다. 연속 위치 찾기를 위한 약지도 점진 학습 분할 연구는 자연 이미지에서 사전 학습 모델로 수백 개의 작은 조각(예: 16×16) 사이의 전체 관계를 이용하는데, 큰 조각(예: 256×256)이 약 10만 개(10^5)에 이르고 암세포처럼 쓸 수 있는 전체 관계가 없는 MIL 위치 찾기에는 맞지 않아 보인다. 이를 풀려고 위치 찾기와 적은 망각의 적응을 함께 노린 MIL 틀 CoMEL을 제안했다. CoMEL은 인스턴스를 효율적으로 부호화하는 GDAT(Grouped Double Attention Transformer), 믿을 만한 인스턴스 의사 표시(모델이 스스로 추정해 붙인 임시 정답)를 만드는 BPPL(Bag Prototypes-based Pseudo-Labeling), 묶음과 인스턴스 분류 모두에서 망각을 줄이는 OWLoRA(Orthogonal Weighted Low-Rank Adaptation)로 이뤄진다. 공개 WSI 데이터셋 세 개의 연속 MIL 설정 실험에서 이전 방법보다 묶음 단위 정확도는 최대 11.00%, 위치 찾기 정확도는 최대 23.4% 높았다.[^p4] | 1저자 Byung Hyun Lee, 마지막 저자 전세영 |
| 5 | 2025 | [Localized Concept Erasure for Text-to-Image Diffusion Models Using Training-Free Gated Low-Rank Adaptation](https://doi.org/10.1109/cvpr52734.2025.01733) · CVPR 2025 | 미세 조정 기반 개념 지우기는 표적 개념은 없애고 나머지 개념은 지켜, 텍스트-이미지 확산 모델이 해로운 내용을 만들지 않게 하는 데 좋은 결과를 보였다. 개념을 지운 뒤에도 생성 능력을 유지하려면, 표적 개념이 이미지의 일부에만 나타날 때 그 영역만 없애고 다른 영역은 그대로 두어야 한다. 그러나 기존 방법은 특정 영역의 표적 개념을 지우려다 다른 영역의 충실도를 해쳐 전체 이미지 생성 성능을 떨어뜨리곤 했다. 이를 위해 이미지에서 표적 개념이 있는 영역만 지우고 나머지 영역은 지키는 국소 개념 지우기라는 틀을 먼저 내놓고, 그 해법으로 확산 모델에 가벼운 모듈을 끼워 넣는 학습 없는 방법 GLoCE(Gated Low-rank adaptation for Concept Erasure)를 제안했다. GLoCE는 저랭크 행렬(행렬 두 개의 곱으로 나타내되 그 사이 차원을 작게 둔 행렬)과 단순한 게이트(조건에 따라 모듈을 켜고 끄는 장치)로 이뤄지며, 학습 없이 개념마다 몇 번의 생성 단계만으로 정해진다. 이미지 임베딩(이미지를 모델이 쓰는 숫자 벡터로 바꾼 것)에 바로 적용하고 게이트가 표적 개념에만 켜지도록 설계해, 표적 개념과 나머지 개념이 한 이미지에 함께 있어도 표적 개념의 영역만 골라 없앤다. 실험에서 국소 표적 개념을 지운 뒤 텍스트 지시에 대한 이미지 충실도가 좋아졌고, 효과·특이성·강건성에서 기존 방법을 큰 차이로 앞섰으며, 많은 개념을 한꺼번에 지우는 일로도 넓혀 쓸 수 있다.[^p5] | 공동 1저자 Byung Hyun Lee, Sungjin Lim(누리집 표기 co-first authors), 마지막 저자 전세영 |
| 6 | 2025 | [Skrr: Skip and Re-use Text Encoder Layers for Memory Efficient Text-to-Image Generation](https://arxiv.org/abs/2502.08690) · ICML 2025 (확인한 판본 arXiv 2502.08690 사전 공개본) | 텍스트-이미지(T2I) 확산 모델의 큰 텍스트 인코더는 글 지시로 질 높은 이미지를 만드는 데 뛰어난 성능을 보였다. 여러 단계를 반복하는 잡음 제거 모듈과 달리 텍스트 인코더는 텍스트 임베딩을 한 번의 순방향 계산으로 만든다. 그래서 전체 추론 시간과 부동소수점 연산량(FLOPs)에서 차지하는 몫은 작지만, 메모리는 잡음 제거 모듈보다 최대 8배까지 훨씬 많이 쓴다. 이 비효율을 풀려고 T2I 확산 모델의 텍스트 인코더에 맞춘 가지치기(신경망의 일부를 덜어 내는 방법) 전략 Skrr(Skip and Re-use layers)를 제안했다. Skrr는 트랜스포머 블록 안의 중복을 이용해 일부 층을 T2I 과제에 맞게 건너뛰거나 다시 써서, 성능을 해치지 않고 메모리 사용을 줄인다. 실험에서 희소도(신경망에서 덜어 낸 부분의 비율)가 높아도 원래 모델과 비슷한 이미지 품질을 유지해 기존 블록 단위 가지치기 방법을 앞섰고, FID, CLIP, DreamSim, GenEval 점수를 포함한 여러 평가 지표에서 성능을 지키면서 최신 기술 수준(state-of-the-art)의 메모리 효율을 냈다.[^p6] | 공동 1저자 Hoigi Seo, Wongi Jeong(누리집 표기 co-first authors), 마지막 저자 전세영 |
| 7 | 2025 | [On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models](https://doi.org/10.52202/085713-4352) · NeurIPS 2025 | 비전 인코더(VE)와 대형 언어 모델을 합친 대형 시각-언어 모델(LVLM)은 여러 과제에서 큰 성공을 거뒀지만, 입력 이미지에 없는 물체를 설명하는 객체 환각 같은 중요한 문제가 남아 있다. VE 안의 불확실한 시각 토큰(이미지를 나눈 조각마다 만든 표현)이 객체 환각의 핵심 요인이라고 보고, 통계 분석으로 인식론적 불확실성(모델의 지식이 모자라서 생기는 불확실성)이 높은 시각 토큰과 환각 발생 사이에 양의 상관관계가 있음을 찾았다. 또 VE의 앞쪽 층에서 작은 적대적 섭동(모델을 헷갈리게 하려고 일부러 넣는 작은 변화)에 표현이 크게 흔들리는 시각 토큰이 인식론적 불확실성이 높다는 것을 이론과 실험으로 보였다. 이를 바탕으로 VE만 고쳐 객체 환각을 줄이는 간단한 전략을 제안했다. 적대적 섭동을 쓰는 대리 방법으로 불확실한 시각 토큰을 효율적으로 찾고, VE 중간 층의 셀프 어텐션(입력 조각들이 서로를 얼마나 참고할지 계산하는 과정)에서 이 토큰들을 가려 시각 부호화에 주는 영향을 억눌러 환각을 줄인다. 실험에서 LVLM의 객체 환각을 크게 줄였고, 이 방법은 다른 기존 방법과 함께 써서 서로 효과를 더할 수 있다.[^p7] | 공동 1저자 Hoigi Seo, Dong Un Kang(누리집 표기 co-first authors), 마지막 저자 전세영 |
| 8 | 2024 | [INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding](https://doi.org/10.1007/978-3-031-73039-9_2) · ECCV 2024 (Lecture Notes in Computer Science) | 어포던스는 물체에 담긴 상호작용 가능성을 뜻하며, 어포던스를 알아보면 지능형 에이전트가 새 환경을 효율적으로 돌아다니고 상호작용할 수 있다. 약지도 어포던스 그라운딩은 비싼 화소 단위 표시 없이 외부 시점(exocentric, 행동하는 사람 바깥에서 본) 이미지로 에이전트에게 어포던스 개념을 가르친다. 최근 좋은 결과가 나왔지만, 외부 시점 이미지와 1인칭 시점(egocentric) 이미지를 짝지은 데이터셋이 필요하고 한 물체의 여러 어포던스를 짚기 어렵다는 과제가 남아 있었다. 이를 풀려고 INTRA를 제안했다. 이전 방법과 달리 이 문제를 외부 시점 이미지만으로 대조 학습(같은 것끼리는 가깝게, 다른 것끼리는 멀게 표현을 배우는 방법)을 통해 상호작용의 고유한 특징을 찾는 표현 학습으로 다시 세워, 짝지은 데이터셋이 필요 없게 했다. 또 시각-언어 모델의 임베딩을 써서 어떤 텍스트로든 어포던스 그라운딩을 유연하게 하고, 대조 학습에 상호작용 관계를 반영하는 텍스트 조건 어포던스 지도 생성과 텍스트 동의어 증강(같은 뜻의 다른 낱말로 바꿔 학습 자료를 늘리는 일)으로 강건성을 높였다. AGD20K, IIT-AFF, CAD, UMD 같은 여러 데이터셋에서 이전 방법보다 나았고, 실험 결과는 이 방법이 합성 이미지·삽화로 영역을 넓혀도 잘 작동하며 처음 보는 상호작용과 물체에도 어포던스 그라운딩을 할 수 있음을 보여 주었다.[^p8] | 공동 1저자 Ji Ha Jang, Hoigi Seo(누리집 표기 co-first authors), 마지막 저자 전세영 |

## 교수와 전문 분야

전세영 교수는 서울대학교에서 전기공학 학사(1999)를, 미국 미시간 대학교에서 전기공학(EE:Systems) 석사와 수학 석사(2005), 전기공학(EE:Systems) 박사(2009)를 받았다.[^pi][^eceprof] 하버드 의과대학·매사추세츠 종합병원 영상의학과(2009–2011)와 미시간 대학교 전기전자컴퓨터공학·영상의학과(2011–2013)에서 박사후 연구원(Research Fellow)으로 일했고, 울산과학기술원(UNIST) 전기전자컴퓨터공학에서 조교수(2013–2017)와 부교수(2017–2021, 2020년 정년 보장)를 지냈다.[^pi][^eceprof] 2021년부터 2024년까지 서울대학교 전기·정보공학부 부교수였고, 2024년부터 교수(2024년 정년 보장)다.[^pi][^eceprof] Members 페이지는 교수의 서울대 시작 시점을 2021년 2월(Feb 2021-)로 적는다.[^members] 2021년부터 뉴미디어통신공동연구소(Institute of New Media and Communications)와 대학원 협동과정 인공지능전공에도 함께 속해 있다.[^pi] 학과 교수 소개는 분야를 신호처리, 계산영상으로, 연구 관심을 계산영상 및 의료영상, 신호처리 및 머신러닝으로 적고,[^eceprof] 협동과정 인공지능전공 교수진 목록은 전공을 AI기반 신호처리, 계산의료영상으로 적는다.[^gsai]

교수 소개 페이지의 Selected Honor / Award 칸은 SNU CoE Outstanding Teaching Award(2022), IEEE Signal Processing Society Outstanding Editorial Board Member Award for IEEE Transactions on Computational Imaging(2021), UNIST Outstanding Faculty Award (Education)(2020), The Bruce Hasegawa Young Investigator Medical Imaging Science Award (IEEE NPSS)(2015), UNIST Outstanding Teaching Award(2014), Society of Nuclear Medicine Computer and Instrumentation Young Investigator Award, 2nd place(2010)를 적는다.[^pi] 학술 활동으로는 IEEE Transactions on Image Processing 부편집장(Associate Editor, 2023–2025), IEEE Transactions on Computational Imaging 부편집장(2019–), IEEE Vehicular Technology Society에 대한 IEEE Biometrics Council Representative(2023–), IEEE 바이오 영상·신호처리 기술위원회(BISP TC) 위원(2021–), IEEE ICASSP 영역 의장(Area Chair, 2018, 2020, 2022, 2024), IEEE 신호처리학회 계산 영상 기술위원회(CI TC) 위원(2016–2021), MICCAI 2019 병리 그랜드 챌린지 PAIP 2019(간암 분할)의 조직위원회(Organizing Committee)를 적는다.[^pi] 소식 페이지는 교수가 NeurIPS 2026 영역 의장을 맡는다는 것과 ECCV 2026 Beyond Euclidean 워크숍에서 초청 기조연설을 했다는 것을 적는다.[^news] 서울대학교에서는 학부 과목 Introduction to Random Variables and Processes, Signals and Systems, Linear Algebra for Electrical Systems, Creative Engineering Design과 대학원 과목 Special Topics in Signal Processing(주제 Generative Diffusion Models, Computational Imaging with Signal Processing and Machine Learning)을 가르쳤다.[^teaching]

누리집 Publications 페이지의 2004–2020년 목록을 연도 구역별로 보면, 2004–2009년 무렵에는 뇌 피질 전기 신호(ECoG, electrocorticography: 뇌 표면에 댄 전극으로 잰 전기 신호)의 사건 검출과 B-스플라인(조각마다 다항식으로 이은 매끈한 곡선 함수)을 쓰는 비강체 영상 정합(휘거나 늘어나는 변형까지 허용해 두 영상의 같은 위치를 맞추는 일)이, 2009–2013년 무렵에는 PET(Positron Emission Tomography, 양전자 방출 단층촬영)와 MR 동시 촬영의 움직임 보정과 정량 SPECT 재구성이 주로 나온다.[^pubs] 2013–2020년 구역에는 비국소 평균 필터(영상 안에서 떨어진 곳이라도 비슷한 조각들을 찾아 가중 평균하는 잡음 제거 방법)를 쓰는 핵의학 영상 잡음 제거와 재구성, 심전도(ECG, electrocardiogram) 기반 사용자 인증, 정답 영상 없이 딥러닝 잡음 제거기를 학습하는 방법, 저선량 CT 재구성, 영상 흐림 제거, 로봇 파지 검출이 실려 있다.[^pubs] 교수가 공저한 서베이 논문 「Deep Internal Learning: Deep Learning from a Single Input」(IEEE Signal Processing Magazine, 2024)은 주어진 입력 하나만으로 신경망을 처음부터 학습하거나, 추론 때 이미 학습한 신경망을 주어진 입력 예에 맞추는 심층 내부 학습 기법들을 정리한다.[^dil]

논문으로 보면 지금의 전문 분야는 네 갈래다. 첫째, 확산 모델과 압축 센싱으로 측정에서 영상을 되찾는 계산 영상의 역문제다(대표 논문 1, 2).[^p1][^p2] 둘째, 핵의학 영상의 물리 기반 산란 추정과 병리 영상의 약지도·연속 학습 같은 의료 영상 알고리즘이다(대표 논문 3, 4).[^p3][^p4] 셋째, 텍스트-이미지 확산 모델의 개념 지우기와 메모리 효율화다(대표 논문 5, 6).[^p5][^p6] 넷째, 시각-언어 모델의 환각 줄이기와 이미지에서 사물의 상호작용 가능성을 찾는 멀티모달 인식이다(대표 논문 7, 8).[^p7][^p8]

## 응용 분야

학과 연구실 소개는 연구실이 계산·의료 영상의 문제를 일반화해 풀어 그 해법이 계산영상뿐만 아니라 컴퓨터 비전이나 다른 응용 분야에도 쓰일 수 있게 한다고 적는다.[^ecelabv] 대표 논문은 정량 SPECT의 환자별 산란 모형화,[^p3] 병리 전체 슬라이드 영상의 분류와 위치 찾기,[^p4] 텍스트-이미지 확산 모델의 해로운 내용 생성 방지,[^p5] 텍스트-이미지 생성의 메모리 절약,[^p6] 대형 시각-언어 모델의 객체 환각 줄이기,[^p7] 지능형 에이전트가 새 환경에서 사물과 상호작용하기 위한 어포던스 인식[^p8]을 대상으로 한다. 삼성미래기술육성사업 과제에 대해 공과대학 소식은 긴 작업에서도 맥락을 잃지 않는 AI 비서와 더 적은 메모리와 전력으로 작동하는 온디바이스 AI로 이어질 기반을 마련하고자 한다고 적는다.[^engnews] 특허 목록에는 여러 화질 저하 요인을 한 모델로 복원하는 화질 개선 모델, 생성 AI 모델을 쓰는 오디오 데이터 관리, 어포던스 그라운딩 장치, 사전 학습 확산 모델로 고해상도 사람 중심 장면을 만드는 방법이 있다.[^pubs] Members 페이지가 적은 졸업생 진로로는 서울대 졸업생의 NVIDIA, LG Display, Samsung DS, Siemens Healthineers, Samsung Research, LG Electronics가 있고, UNIST 졸업생의 Samsung Research, ETRI, KETI, GIST(조교수), Deepnoid, LG Display, Huawei Research Center, Sony Interactive Entertainment와 KAIST·Catholic Univ of America·TU Delft 박사과정 진학이 있다.[^members]

## 구성원

2026-10-25에 읽은 Members 페이지 Current members 칸의 교수 외 27명이다(박사후연구원 1명, PhD Students 칸 19명, MS Students 칸 5명, Undergraduate Students 칸 2명). 과정은 각 이름 줄의 표기(Postdoc, PhD student, MS/PhD student, MS student, Undergrad student)를 옮겼고, 괄호 안은 같은 줄 「@」 뒤의 소속 표기다(ECE는 전기·정보공학부, IPAI는 대학원 협동과정 인공지능전공, INMC는 뉴미디어통신공동연구소). 시작은 이름 옆 괄호의 표기다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Seongmin Hong | 박사후연구원 (INMC) | Sep 2025- | 1, 2 |
| Haechang Lee | 박사과정 (ECE) | Sep 2022- |  |
| Byung Hyun Lee | 석박사통합과정 (ECE) | Mar 2021- | 4, 5 |
| Junseo Bang | 석박사통합과정 (ECE) | Mar 2021- | 1 |
| Wongi Jeong | 석박사통합과정 (ECE) | Mar 2022- | 4, 6 |
| Dong Ju Mun | 석박사통합과정 (ECE) | Mar 2022- | 1 |
| Seunggyu Lee | 석박사통합과정 (ECE) | Mar 2023- |  |
| Ji Ha Jang | 석박사통합과정 (ECE) | Mar 2023- | 8 |
| Younguk Kim | 박사과정 (ECE) | Mar 2025- |  |
| Hayeon Kim | 석박사통합과정 (ECE) | Sep 2023- |  |
| Hyewon Bae | 석박사통합과정 (ECE) | Sep 2023- |  |
| Suh Yoon Jeon | 석박사통합과정 (ECE) | Sep 2023- |  |
| Hoigi Seo | 석박사통합과정 (ECE) | Mar 2024- | 1, 6, 7, 8 |
| Woojae Han | 석박사통합과정 (IPAI) | Mar 2024- | 4 |
| Kyeonghyun Lee | 석박사통합과정 (ECE, SNU) | Sep 2024- |  |
| Kyungryeol Lee | 석박사통합과정 (ECE, SNU) | Sep 2024- |  |
| Joohoon Lee | 석박사통합과정 (IPAI) | Sep 2024- | 7 |
| Hyunjin Cho | 석박사통합과정 (ECE) | Mar 2025- | 7 |
| Jaehyun Cho | 석박사통합과정 (IPAI) | Mar 2025- |  |
| Jason Park | 석박사통합과정 (ECE) | Mar 2025- |  |
| Junghun J. Kim | 석사과정 (IPAI) | Mar 2025- |  |
| Chulwon Lee | 석사과정 (IPAI) | Mar 2025- |  |
| Dohyun Mah | 석박사통합과정 (ECE) | Mar 2026- |  |
| Chaeeun Lee | 석박사통합과정 (IPAI) | Mar 2026- |  |
| Daewon Choi | 석사과정 (IPAI) | Mar 2026- |  |
| Youngwook Kim | 학부 연구생 (EES/CSE, SNU) | Jul 2026- |  |
| Yoonchae Choi | 학부 연구생 (ECE, SNU) | Jul 2026- |  |

## 졸업생과 이전 구성원

Members 페이지 Past members 칸의 서울대 졸업생 6명(Graduates @ SNU), UNIST 졸업생 10명(Graduates & Undergraduate interns w/ thesis @ UNIST), 서울대 학부 인턴 32명(Undergraduate Interns @ SNU, 2021–2026년), UNIST 학부 인턴 7명(Undergraduate interns w/ thesis @ UNIST)이다. 학위·과정 칸의 괄호 안 표기(학위, 전공, 연·월)와 진로는 페이지 표기 그대로이고, 서울대 학부 인턴은 연도별 명단에 오른 해를 모아 적었다. 학부 인턴 가운데 여러 명은 지금 대학원생 구성원으로 위 표에도 있다. UNIST 졸업생 칸은 UNIST에서 학위를 받은 사람들이고(교수의 UNIST 재직은 2013–2021년), 그 가운데 Dongwon Park 줄에는 Postdoc in IPAI@SNU 2024.2 표기도 함께 있다.[^members][^pi]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Gwanghyun Kim | 서울대 졸업생 · PhD in ECE 2026.2 | Research Scientist @ NVIDIA, USA |
| Joonhee Lee | 서울대 졸업생 · PhD in ECE 2026.2 | Researcher @ LG Display, Korea |
| Sungjin Lim | 서울대 졸업생 · MS in IPAI 2026.2 | Researcher @ Samsung DS, Korea |
| Dong Un Kang | 서울대 졸업생 · PhD in ECE 2025.8, MS in EE@UNIST 2021.2 | Research Fellow @ Siemens Healthineers, USA |
| Hyunwoo Lee | 서울대 졸업생 · MS in ECE 2025.2 | Researcher @ Samsung Research, Korea |
| Okchul Jung | 서울대 졸업생 · MS in ECE 2023.8 | Researcher @ LG Electronics, Korea |
| Dongwon Park | UNIST 졸업생 · Postdoc in IPAI@SNU 2024.2, PhD in ECE 2023.2, MS in ECE 2019.8 | Researcher @ Samsung Research, Korea |
| Hanvit Kim | UNIST 졸업생 · PhD in ECE 2022.2, MS in ECE 2018.2 | Researcher @ ETRI, Korea |
| Yong Hyeok Seo | UNIST 졸업생 · MS in ECE 2021.2 | Researcher @KETI, Korea |
| Kwanyoung Kim | UNIST 졸업생 · MS in ECE 2020.8 | PhD student @Bio Brain Eng, KAIST, Korea and then Assistant Professor @GIST, Korea |
| Won Jae Hong | UNIST 졸업생 · MS in ECE 2020.2 | Researcher @Deepnoid, Korea |
| Jisoo Kim | UNIST 졸업생 · MS in ECE 2020.2 | Researcher @LG Display, Korea |
| Magauiya Zhussip | UNIST 졸업생 · MS in ECE 2019.8 | Researcher @Huawei Research Center, Russia |
| Shakarim Soltanayev | UNIST 졸업생 · MS in ECE 2019.8 | Researcher @Sony Interactive Entertainment, UK |
| Thanh Quoc Phan | UNIST 졸업생 · MS in ECE 2018.8 | PhD student @BME, Catholic Univ of America, USA |
| Minh Phuong Nguyen | UNIST 졸업생 · MS in ECE 2016.8 | PhD student @Biom Imag, TU Delft, Netherlands |
| Justin Yu | 서울대 학부 인턴 · 2026 |  |
| Junsung Park | 서울대 학부 인턴 · 2025 |  |
| Dohyun Mah | 서울대 학부 인턴 · 2025 |  |
| Seungmin Shin | 서울대 학부 인턴 · 2025 |  |
| Heechang Kim | 서울대 학부 인턴 · 2023, 2024, 2025 |  |
| Hangyeol Seo | 서울대 학부 인턴 · 2025 |  |
| Insoo Chung | 서울대 학부 인턴 · 2025 |  |
| Yeong Mok Cho | 서울대 학부 인턴 · 2025 |  |
| Daehyeop Kim | 서울대 학부 인턴 · 2025 |  |
| Kyeonghyun Lee | 서울대 학부 인턴 · 2023, 2024 |  |
| Kyungryeol Lee | 서울대 학부 인턴 · 2023, 2024 |  |
| Hyunjin Cho | 서울대 학부 인턴 · 2023, 2024 |  |
| Ye Eun Song | 서울대 학부 인턴 · 2023, 2024 |  |
| Donggyu Lee | 서울대 학부 인턴 · 2023, 2024 |  |
| Jae Hyun Cho | 서울대 학부 인턴 · 2024 |  |
| Seongryun Jo | 서울대 학부 인턴 · 2024 |  |
| Hoigi Seo | 서울대 학부 인턴 · 2022, 2023 |  |
| Hayeon Kim | 서울대 학부 인턴 · 2023 |  |
| Seungchan Moon | 서울대 학부 인턴 · 2023 |  |
| Jin Myeong Kim | 서울대 학부 인턴 · 2023 |  |
| Jae Hong Moon | 서울대 학부 인턴 · 2023 |  |
| Ji Ha Jang | 서울대 학부 인턴 · 2022 |  |
| Seunggyu Lee | 서울대 학부 인턴 · 2022 |  |
| Junseo Lee | 서울대 학부 인턴 · 2022 |  |
| Jiho Kim | 서울대 학부 인턴 · 2022 |  |
| Jin Ha Park | 서울대 학부 인턴 · 2022 |  |
| Inbum Park | 서울대 학부 인턴 · 2022 |  |
| Jaekeun Lee | 서울대 학부 인턴 · 2022 |  |
| Wongi Jeong | 서울대 학부 인턴 · 2021 |  |
| Si Yeon Noh | 서울대 학부 인턴 · 2021 |  |
| Chae Won Park | 서울대 학부 인턴 · 2021 |  |
| Sanghun Shin | 서울대 학부 인턴 · 2021 |  |
| Temirlan Amangeldinov | UNIST 학부 인턴(w/ thesis) |  |
| Jiye Son | UNIST 학부 인턴(w/ thesis) |  |
| Dong Un Kang | UNIST 학부 인턴(w/ thesis) |  |
| Yong Hyeok Seo | UNIST 학부 인턴(w/ thesis) |  |
| Byung Hyun Lee | UNIST 학부 인턴(w/ thesis) |  |
| Kwanyoung Kim | UNIST 학부 인턴(w/ thesis) |  |
| Hanvit Kim | UNIST 학부 인턴(w/ thesis) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications 페이지의 2021–2026년 연도 구역에서 Patent 칸을 뺀 125항목 가운데 116편이다(2026년 21편, 2025년 40편, 2024년 26편, 2023년 15편, 2022년 9편, 2021년 5편). 연도는 페이지의 연도 구역이고, 각 연도 안의 순서는 페이지 순서(Journal, Conference (full papers), Conference (short papers, abstracts or workshop papers), Conference (domestic), Technical Report)이며, 줄 끝 「·」 뒤에 그 칸을 학술지, 학회 정규 논문, 학회 단편·초록·워크숍 논문, 국내 학회, 기술 보고서로 적었다. 저자(머리글자 표기)·제목·학술지와 학회 표기, 「*」 표시와 괄호 안 co-first authors·co-corresponding authors, Oral·Spotlight·Highlight 같은 발표 형식 표기, 「was arXiv:…」 같은 이전 판본 표기는 페이지 그대로다. 같은 연구가 학회 정규 논문, 워크숍 발표, 기술 보고서로 따로 실린 경우도 페이지대로 두었다.[^pubs] 교수의 서울대 시작은 2021년 2월이어서(Members 페이지 표기 Feb 2021-), 2021년 구역에는 그 전에 나온 논문(Medical Image Analysis, 2021년 1월)과 UNIST 졸업생이 1저자인 논문도 들어 있다.[^members]

학회 이름 앞의 「Accepted at」도 페이지 표기이며, 이 줄들에는 권·쪽 같은 출판 기록이 페이지에 적혀 있지 않다. 그 가운데 NeurIPS 2026 세 편은 첫 화면과 소식 페이지가 2026년 9월 채택 소식으로 알린 논문이라 「채택」으로 표시했다.[^home][^news] 다른 「Accepted at」 줄에는 이 문서를 쓰며 확인한 판본(arXiv 사전 공개본과 그 판본의 학회 표기, 또는 학술대회 논문집의 출판 기록)을 괄호에 적었고, 판본을 확인하지 못한 줄은 「누리집 표기」로 적었다.

**2026**

- S Y Jo, J W Shon, S H An, Y J Nam, D W Choi, S M Lee, H G Seo, S Y Chun, H Kim, G H Kim. "Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research". *Theranostics 16(10):5240-58, Mar 2026 · 학술지*.
- S J Lim\*, D U Kang\*, Y M Cho, S Y Chun. "Dual Context-Conditioned Open-Vocabulary Semantic Segmentation in Remote Sensing". *IEEE Access 14:43664-78 (IEEE Geoscience and Remote Sensing Society Section), Mar 2026 (\*co-first authors) · 학술지*.
- H C Lee\*, D J Mun\*, H W Lee\*, K C Lee, S M Hong, G H Kim, S A Lee\*\*, S Y Chun\*\*. "Fidelity-Preserving Zero-shot Diffusion Models for Highly Ill-posed Inverse Problems in Lensless Imaging". *Image and Vision Computing, 165:105786, Jan 2026 (\*co-first authors, \*\*co-corresponding authors) · 학술지*.
- H G Seo\*, B H Lee\*, M J Kim\*, D H Mah, J H Lee, S Y Chun. "Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs". *Accepted at NeurIPS, 2026 (\*co-first authors) (Spotlight) (채택) (확인한 판본 arXiv 2610.04580 사전 공개본) · 학회 정규 논문*.
- J S Bang, D W Choi, D J Mun, S Y Chun. "FLINT: Coupling Proximal Initialization and Bounded Stochasticity for Flow-Matching Inverse Problems". *Accepted at NeurIPS 2026 (채택) · 학회 정규 논문*.
- J H Park, S Y Chun, M G Seok. "DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels". *Accepted at NeurIPS, 2026 (채택) · 학회 정규 논문*.
- J H Jang\*, H Y Kim\*, C W Lee, J J Kim, S Y Chun. "HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding". *Accepted at ECCV, 2026 (\*co-first authors) (확인한 판본 arXiv 2607.00428 사전 공개본, 판본 표기 Accepted to ECCV 2026) · 학회 정규 논문*.
- J S Bang\*, D J Mun\*, H G Seo, S M Hong, S Y Chun. "Triadic Dynamics Aware Diffusion Posterior Sampling for Inverse Problems: Optimizing Guidance and Stochasticity Schedules". *Accepted at ICML, Jul 2026 (\*co-first authors) (확인한 판본 arXiv 2605.26470 사전 공개본) · 학회 정규 논문*.
- G H Kim\*, J J Kim\*, S Y Jeon\*, J S Park, S Y Chun. "Human Interaction-Aware 3D Reconstruction from a Single Image". *Accepted at CVPR, Jun 2026 (\*co-first authors) (Highlight) (확인한 판본 arXiv 2604.05436 사전 공개본, 판본 표기 Accepted to CVPR 2026) · 학회 정규 논문*.
- H Y Kim\*, J H Jang\*, J J Kim, S Y Chun. "Uncertainty-guided Compositional Alignment with Part-to-Whole Semantic Representativeness in Hyperbolic Vision-Language Models". *Accepted at CVPR, Jun 2026 (\*co-first authors) (Highlight) (확인한 판본 arXiv 2603.22042 사전 공개본, 판본 표기 Accepted to CVPR 2026) · 학회 정규 논문*.
- H G Seo\*, B H Lee\*, J H Cho, S J Lim, S Y Chun. "Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models". *Accepted at CVPR, Jun 2026 (\*co-first authors) (확인한 판본 arXiv 2604.16481 사전 공개본) · 학회 정규 논문*.
- W G Jeong\*, H G Seo\*, S Y Chun. "Training-free, Perceptually Consistent Low-Resolution Previews with High-Resolution Image for Efficient Workflows of Diffusion Models". *Accepted at CVPR, Jun 2026 (\*co-first authors) (확인한 판본 arXiv 2604.09227 사전 공개본) · 학회 정규 논문*.
- W G Jeong\*, K R Lee\*, H G Seo, S Y Chun. "Training-free Mixed-Resolution Latent Upsampling for Spatially Accelerated Diffusion Transformers". *Accepted at CVPR, Jun 2026 (\*co-first authors) (was arXiv:2507.08422) (Highlight) (확인한 판본 arXiv 2507.08422 사전 공개본) · 학회 정규 논문*.
- S M Hong\*, J J Kim\*, D H Kim, I S Chung, S Y Chun. "DiffBMP: Differentiable Rendering with Bitmap Primitives". *Accepted at CVPR, Jun 2026 (\*co-first authors) (확인한 판본 arXiv 2602.22625 사전 공개본, 판본 표기 Accepted to CVPR 2026) · 학회 정규 논문*.
- J H Park, S Y Chun, M G Seok. "AdaRadar: Rate Adaptive Spectral Compression for Radar-based Perception". *Accepted at CVPR, Jun 2026 (확인한 판본 arXiv 2603.17979 사전 공개본, 판본 표기 Accepted to CVPR 2026) · 학회 정규 논문*.
- H G Seo\*, B H Lee\*, J H Cho, S J Lim, S Y Chun. "Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models". *Accepted at CVPRW MUV (Machine Unlearning for Computer Vision), Jun 2026 (\*co-first authors) (누리집 표기) · 학회 단편·초록·워크숍 논문*.
- K R Lee\*, K H Lee\*, S M Hong\*, B H Lee, S Y Chun. "Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models". *Accepted at CVPRW MUV (Machine Unlearning for Computer Vision), Jun 2026 (\*co-first authors) (누리집 표기) · 학회 단편·초록·워크숍 논문*.
- G H Kim\*, J J Kim\*, S Y Jeon\*, J S Park, S Y Chun. "Human Interaction-Aware 3D Reconstruction from a Single Image". *Accepted at CVPRW PhysHuman (Physically Grounded Human Perception and Modeling), Jun 2026 (\*co-first authors) (Oral) (누리집 표기) · 학회 단편·초록·워크숍 논문*.
- H Y Kim\*, J H Jang\*, J J Kim, S Y Chun. "Uncertainty-guided Compositional Alignment with Part-to-Whole Semantic Representativeness in Hyperbolic Vision-Language Models". *Accepted at CVPRW VisCon (Visual Concepts), Jun 2026 (\*co-first authors) (누리집 표기) · 학회 단편·초록·워크숍 논문*.
- S J Lim\*, C W Lee\*, D U Kang, Y M Cho, S Y Chun. "Feature-guided CRF Refinement for Training-free Open-Vocabulary Remote Sensing Segmentation". *ICEIC, Jan 2026 (\*co-first authors) · 학회 단편·초록·워크숍 논문*.
- K R Lee\*, K H Lee\*, S M Hong\*, B H Lee, S Y Chun. "Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models". *arXiv:2603.10445 [cs.LG], Mar 2026 (\*co-first authors) · 기술 보고서*.

**2025**

- K R Lee\*, S M Hong\*, S Y Chun. "Robust Watermarks for Audio Diffusion Models by Quadrature Amplitude Modulation". *Pattern Recognition Letters 198:22-28, Dec 2025 (\*co-first authors) · 학술지*.
- T Hong, Z Xu, S Y Chun, L Hernandez-Garcia, J A Fessler. "Convergent Complex Quasi-Newton Proximal Methods for Gradient-Driven Denoisers in Compressed Sensing MRI Reconstruction". *IEEE Transactions on Computational Imaging 11:1534-1547, Nov 2025 · 학술지*.
- K W Hong\*, M H Jo\*, H C Lee\*, S Y Chun, A No. "A Simple Extension of Bayer Demosaicing For Light-Weight Non-Bayer Demosaicing". *IEEE Access 13:131061-73, Jul 2025 (\*co-first authors) · 학술지*.
- H J Shin, T H Kim, J H Lee, S Y Chun, S R Cho, D M Shin. "Sparse-view CBCT reconstruction using meta-learned neural attenuation field and hash-encoding regularization". *Computers in Biology and Medicine 189:109900, May 2025 (was arXiv:2312.01689) · 학술지*.
- H W Lee, H C Lee, B H Lee, S Y Chun. "Continual Test-time Adaptation for Robust Remote Photoplethysmography Estimation". *IEEE Access 13:55049-60, Apr 2025 · 학술지*.
- D U Kang\*, H W Lee\*, S Y Chun. "Class Concept Representation from Contextual Texts for Training-Free Multi-Label Recognition". *IEEE Access 13:36965-36977, Mar 2025 (\*co-first authors) · 학술지*.
- J H Lee, D W Park, S Y Chun. "Image Quality Assessments By Leveraging Diverse Visual Tasks". *IEEE Access 13:15639-49, Jan 2025 · 학술지*.
- C Cui, K-J Jung, M A Al-masni, J-H Kim, S-Y Kim, M Park, S Y Huang, S Y Chun, D-H Kim. "Deep Network Regularization for Phase-based Magnetic Resonance Electrical Properties Tomography with Stein’s Unbiased Risk Estimator". *IEEE Transactions on Biomedical Engineering 72(1):43-55, Jan 2025 · 학술지*.
- H G Seo\*, D U Kang\*, H J Cho, J H Lee, S Y Chun. "On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models". *Accepted at NeurIPS, 2025 (\*co-first authors) (확인한 출판 기록 Advances in Neural Information Processing Systems 38) · 학회 정규 논문*.
- B H Lee, W G Jeong, W J Han, K B Lee, S Y Chun. "Continual Multiple Instance Learning with Enhanced Localization for Histopathological Whole Slide Image Analysis". *ICCV 23232-42, Oct 2025 (was arXiv:2507.02395) · 학회 정규 논문*.
- G H Kim\*, S Y Jeon\*, S G Lee, S Y Chun. "PersonaCraft: Personalized Full-Body Image Synthesis for Multiple Identities from Single References Using 3D-Model-Conditioned Diffusion". *ICCV 12034-44, Oct 2025 (\*co-first authors) (was arXiv:2411.18068) · 학회 정규 논문*.
- H Y Kim\*, J H Jang\*, S Y Chun. "Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with Regularized Score Distillation Sampling". *ICCV 5501-10, Oct 2025 (\*co-first authors) (was arXiv:2507.11061) · 학회 정규 논문*.
- G H Kim, X Li, Y Yuan, K Nagano, T Li, J Kautz, S Y Chun, U Iqbal. "GeoMan: Temporally Consistent Human Geometry Estimation using Image-to-Video Diffusion". *ICCV 7451-7461, Oct 2025 (was arXiv:2505.23085) · 학회 정규 논문*.
- H H Jeong, S Y Chun, J H Lee. "MOST: MR reconstruction Optimization for multiple downStream Tasks via continual learning". *MICCAI 11:396-406, Sep 2025 (was ISMRM 2024 & arXiv:2409.10394) · 학회 정규 논문*.
- H G Seo\*, W G Jeong\*, J-S Seo, S Y Chun. "Skrr: Skip and Re-use Text Encoder Layers for Memory Efficient Text-to-Image Generation". *ICML 267:53867-905, Jul 2025 (\*co-first authors) (was arXiv:2502.08690) · 학회 정규 논문*.
- B H Lee\*, S J Lim\*, S Y Chun. "Localized Concept Erasure for Text-to-Image Diffusion Models Using Training-Free Gated Low-Rank Adaptation". *CVPR 18596-606, Jun 2025 (\*co-first authors) (2025 Qualcomm Innovation Fellowship Korea Finalist) · 학회 정규 논문*.
- H G Seo\*, W G Jeong\*, K R Lee, S Y Chun. "Efficient Personalization of Quantized Diffusion Model without Backpropagation". *CVPR 7717-27, Jun 2025 (\*co-first authors) · 학회 정규 논문*.
- D U Kang, H Y Kim, S Y Chun. "Class Distribution-induced Attention Map for Open-vocabulary Semantic Segmentations". *ICLR, Apr 2025 · 학회 정규 논문*.
- B H Lee\*, S J Lim\*, S G Lee, D U Kang, S Y Chun. "Concept Pinpoint Eraser for Text-to-image Diffusion Models via Residual Attention Gate". *ICLR, Apr 2025 (\*co-first authors) · 학회 정규 논문*.
- G H Kim\*, S Y Jeon\*, S G Lee, S Y Chun. "PersonaCraft: Personalized Full-body Image Synthesis for Multiple Identities from Single References Using 3D-Model-Conditioned Diffusion". *ICCV Workshops (P13N) Extended Abstract, Oct 2025 (\*co-first authors) · 학회 단편·초록·워크숍 논문*.
- H G Seo\*, W G Jeong\*, K R Lee, S Y Chun. "Efficient Personalization of Quantized Diffusion Model without Backpropagation". *CVPR Workshops (EDGE) Extended Abstract, Jun 2025 (\*co-first authors) · 학회 단편·초록·워크숍 논문*.
- M J Kim, H H Jeong, H G Seo, W G Jeong, J H Park, S Y Chun, J H Lee. "Harmonization for a black-box deep learning model". *ISMRM, May 2025 (oral, summa cum laude, AMPC select) · 학회 단편·초록·워크숍 논문*.
- H H Jeong, H Y Lee, S Y Chun, J H Lee. "Blind harmonization reinvented via 3D diffusion model". *ISMRM, May 2025. · 학회 단편·초록·워크숍 논문*.
- J H Lee, J S Bang, S Y Chun. "Few-Shot Arbitrary Super-Resolution Considering Consistency and Realness". *ICEIC, Jan 2025 · 학회 단편·초록·워크숍 논문*.
- D U Kang, S Y Chun. "Focusing on Representation of Multi-Head Attention for Open-Vocabulary Semantic Segmentation". *ICEIC, Jan 2025 · 학회 단편·초록·워크숍 논문*.
- H C Lee, D J Mun, J H Lee, H W Lee, S Y Chun. "Zero-Shot Diffusion Models for Demosaicing in Bayer and Non-Bayer Image Sensors". *ICEIC, Jan 2025 · 학회 단편·초록·워크숍 논문*.
- H W Bae\*, S Y Jeon\*, S Y Chun. "Object-Interactive Human Motion Generation via Affordance Reasoning". *Conference on Electronics, Semiconductor and AI, Aug 2025 (Best Paper Award) · 국내 학회*.
- K H Lee\*, W J Han\*, S Y Chun. "Robust Panoramic Localization via Hybrid Optimization". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- S G Lee\*, H W Bae\*, S Y Chun. "Training-Free Dynamics Score Control in Text-to-Video Diffusion Models via Wavelet-Based Latent Refinement". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- J S Bang\*, J H Lee\*, H C Lee, D U Kang, S Y Chun. "Self-Cascade Coordinate-guided Residual Diffusion Models for Arbitrary-Scale Perceptual Image Super-Resolution". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- J S Park, G H Kim, J J Kim, S Y Jeon, S Y Chun. "Detailed texture reconstruction for multiple interacting humans using an iterative method". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- S Y Jeon\*, H W Bae\*, J H Jang\*, S Y Chun. "SpecArtDiff: ControlNet-Guided Fusion of Panoramic Visuals and Auditory Spectrograms". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- K R Lee, S Y Chun. "Closed-form Instance Unlearning for Explicit Distributions". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- H J Cho, H G Seo, D U Kang, J H Lee, S Y Chun. "Mitigating Hallucinations in Large Vision-Language Models via Norm-Guided Visual Filtering". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- D J Mun\*, J S Bang\*, S Y Chun. "Zero-shot Diffusion Model based Highly Ill-posed Inverse Problem Solver via Tweedie Variable Optimization with Total Variation". *Conference on Electronics, Semiconductor and AI, Aug 2025 · 국내 학회*.
- H C Kim, G H Kim, S Y Chun. "LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation". *arXiv:2509.24469 [cs.CV], Sep 2025 · 기술 보고서*.
- D G Lee, S M Hong, S Y Chun. "Principled Reframing in Motion Transfer with Video Diffusion Models". *Available at SSRN, Aug 2025 · 기술 보고서*.
- J S Bang\*, J H Lee\*, K H Lee\*, H C Lee, D U Kang, S Y Chun. "Self-Cascaded Diffusion Models for Arbitrary-Scale Image Super-Resolution". *arXiv:2506.07813 [cs.CV], Jun 2025 (\*co-first authors) · 기술 보고서*.
- T Hong, Z Xu, S Y Chun, L Hernandez-Garcia, J A Fessler. "Convergent Complex Quasi-Newton Proximal Methods for Gradient-Driven Denoisers in Compressed Sensing MRI Reconstruction". *arXiv:2505.04820 [eess.IV], May 2025 · 기술 보고서*.
- H G Seo\*, J S Bang\*, H C Lee\*, J H Lee, B H Lee, S Y Chun. "Geometrical Properties of Text Token Embeddings for Strong Semantic Binding in Text-to-Image Generation". *arXiv:2503.23011 [cs.CV], Mar 2025 (\*co-first authors) · 기술 보고서*.

**2024**

- T Tirer, R Giryes, S Y Chun, Y C Eldar. "Deep Internal Learning: Deep Learning from a Single Input". *IEEE Signal Processing Magazine 41(4):40-57, Jul 2024 (was arXiv:2312.07425) · 학술지*.
- S M Hong, S Y Jeon, K H Lee, E K Ryu\*\*, S Y Chun\*\*. "Gradient-free Decoder Inversion in Latent Diffusion Models". *NeurIPS 37:82982-83007, Dec 2024 (\*\*co-corresponding authors) (was arXiv:2409.18442) · 학회 정규 논문*.
- J H Jang\*, H G Seo\*, S Y Chun. "INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding". *ECCV 15122:18-34, Oct 2024 (\*co-first authors) (was arXiv:2409.06210) · 학회 정규 논문*.
- D W Park, H Y Kim, S Y Chun. "Contribution-based Low-Rank Adaptation with Pre-training Model for Real Image Restoration". *ECCV 15122:87-105, Oct 2024 (was arXiv:2408.01099) · 학회 정규 논문*.
- G H Kim\*, H Y Kim\*, H G Seo\*, D U Kang\*, S Y Chun. "BeyondScene: Higher-Resolution Human-Centric Scene Generation With Pretrained Diffusion". *ECCV 15122:126-142, Oct 2024 (\*co-first authors) (was arXiv:2404.04544) · 학회 정규 논문*.
- S M Hong, J H Bae, J H Lee\*\*, S Y Chun\*\*. "Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing". *ECCV 15123:307-322, Oct 2024 (\*\*co-corresponding authors) (was arXiv:2409.11738) · 학회 정규 논문*.
- J H Park, S Y Chun, M G Seok. "UL-VIO: Ultra-Lightweight Visual-Inertial Odometry with Noise Robust Test-Time Adaptation". *ECCV 15121:415-432, Oct 2024 (was arXiv:2409.13106) · 학회 정규 논문*.
- S M Hong, K H Lee, S Y Jeon, H W Bae, S Y Chun. "On Exact Inversion of DPM-Solvers". *CVPR 7069-7078, Jun 2024 (was arXiv:2311.18387) (2024 Qualcomm Innovation Fellowship Korea) · 학회 정규 논문*.
- B H Lee, M H Oh, S Y Chun. "Doubly Perturbed Task Free Continual Learning". *AAAI 13346-13354, Feb 2024 (was arXiv:2312.13027) (Oral) · 학회 정규 논문*.
- V Hosu et al. (including J H Lee, J S Bang, S Y Chun), AIM 2024 Challenge on UHD Blind Photo Quality Assessment, ECCV Workshops (AIM), 2024 · 학회 단편·초록·워크숍 논문
- J H Park, S Y Chun, M G Seok. "Ultra-lightweight Visual-Inertial Odometry with Noise Robust Test-time Adaptation". *ECCV Workshops (VCAD) Extended Abstract, 2024 (oral) · 학회 단편·초록·워크숍 논문*.
- J H Jang\*, H G Seo\*, S Y Chun. "INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding". *ECCV Workshops (ACVR) Extended Abstract, 2024 (oral) (\*co-first authors) · 학회 단편·초록·워크숍 논문*.
- S M Hong, J H Bae, J H Lee\*\*, S Y Chun\*\*. "Uncertainty-Adaptive Selection of Sampling-Reconstruction for Fourier Compressed Sensing". *ECCV Workshops (UnCV) Extended Abstract, 2024 (\*\*co-corresponding authors) · 학회 단편·초록·워크숍 논문*.
- H H Jeong, S Y Chun, J H Lee. "MOST: MR reconstruction Optimization for multiple downStream Tasks via continual learning". *ISMRM 2024 (oral, magna cum laude) · 학회 단편·초록·워크숍 논문*.
- H V Kim, Z Li, J Y Son, J A Fessler, Y K Dewaraja, S Y Chun. "Physics-Guided Deep Scatter Estimation by Weak Supervision for Quantitative SPECT". *IEEE ICASSP 2024 as a Journal presentation (for IEEE Transactions on Medical Imaging 42(10):2961-2973, Oct 2023) · 학회 단편·초록·워크숍 논문*.
- B H Lee, S J Lim, S Y Chun. "Selective Concept Erasing for Safe Diffusion Models". *Korea Signal Processing Conference, Oct 2024 (Best Poster Presentation Award) · 국내 학회*.
- D J Mun, H C Lee, H W Lee, K C Lee, S A Lee, S Y Chun. "Zero-shot diffusion model using DDPG for lensless image restoration". *Korea Signal Processing Conference, Oct 2024 · 국내 학회*.
- J S Bang, J H Lee, S Y Chun. "Zero-Shot Super-Restoration Using Fourier-Guided Parallel Diffusion Model". *Korea Signal Processing Conference, Oct 2024 · 국내 학회*.
- S G Lee, J H Jang, S Y Chun. "Personalization of Abstract Concept in Text-to-Image Diffusion Model". *Korea Signal Processing Conference, Oct 2024 · 국내 학회*.
- W G Jeong, H G Seo, S Y Chun. "Towards Personalization of Generative Models Via Zeroth-Order Optimization". *Korea Signal Processing Conference, Oct 2024 · 국내 학회*.
- W J Han, G H Lee, S M Hong, S Y Chun. "Enhanced Depth Map Upsampling Using ControlNet". *Korea Signal Processing Conference, Oct 2024 · 국내 학회*.
- H W Bae, S Y Chun. "Efficient Representation of Heterogenous Features in Tabular Data: Unifying Structures for a Foundation Model". *Conference on Electronics, Semiconductor and AI, Aug 2024 · 국내 학회*.
- H Y Kim, J H Jang, J B Choi, J O Cha, S Y Chun. "ACE-LCM: Attention-based Controllability and direct classifier-free guidance based quality Enhancing in few-step Latent Consistency Model". *Conference on Electronics, Semiconductor and AI, Aug 2024 · 국내 학회*.
- S Y Jeon, S Y Chun. "Improving Prompt Fidelity in Style-Aligned Image Generation via Attention Manipulation". *Conference on Electronics, Semiconductor and AI, Aug 2024 · 국내 학회*.
- S G Lee, B H Lee, S Y Chun. "Expert classifier ensemble based post-processing correction for unbiased scene graph generation". *Workshop on Image Processing and Image Understanding (IPIU), Jan 2024 · 국내 학회*.
- H J Cho, D U Kang, S Y Chun. "Short-term Object Interaction Anticipation with Disentangled Object Detection @ Ego4D Short Term Object Interaction Anticipation Challenge". *arXiv:2407.05713 [cs.CV], Jul 2024 (3rd place at the 2024 Ego4D-Ego-Exo4D Challenge in the Short-term Object Interaction Anticipation Track at CVPR'24) · 기술 보고서*.

**2023**

- H Choi\*, B H Lee\*, S Y Chun\*\*, J Lee\*\*. "Towards accelerating model parallelism in distributed deep learning systems". *Plos One 18(11): e0293338, Nov 2023 (\*co-first authors, \*\*co-corresponding authors) · 학술지*.
- K M Kim\*, K B Lee\*, S D Cho\*, D U Kang\* et al. (including S Y Chun\*\*). "PAIP 2020: Microsatellite Instability Prediction in Colorectal Cancer". *Medical Image Analysis 89:102886, Oct 2023 (\*co-first authors, \*\*co-corresponding authors) · 학술지*.
- H V Kim, Z Li, J Y Son, J A Fessler, Y K Dewaraja, S Y Chun. "Physics-Guided Deep Scatter Estimation by Weak Supervision for Quantitative SPECT". *IEEE Transactions on Medical Imaging 42(10):2961-2973, Oct 2023 · 학술지*.
- H C Lee\*, D W Park\*, W G Jeong\*, K J Kim, H W Je, D I Ryu, S Y Chun. "Efficient Unified Demosaicing for Bayer and Non-Bayer Patterned Image Sensors". *ICCV 12750-12759, Oct 2023 (\*co-first authors) · 학회 정규 논문*.
- S M Hong, I B Park, S Y Chun. "On the Robustness of Normalizing Flows for Inverse Problems in Imaging". *ICCV 10745-10755, Oct 2023 (was arXiv:2212.04319 [cs.CV]) · 학회 정규 논문*.
- B H Lee\*, O C Jung\*, J H Choi\*\*, S Y Chun\*\*. "Online Continual Learning on Hierarchical Label Expansion". *ICCV 11761-11770, Oct 2023 (\*co-first authors, \*\*co-corresponding authors) · 학회 정규 논문*.
- G H Kim, J H Jang, S Y Chun. "PODIA-3D: Domain Adaptation of 3D Generative Model Across Large Domain Gap Using Pose-Preserved Text-to-Image Diffusion". *ICCV 22603-22612, Oct 2023 (was arXiv:2304.01900 [cs.CV]) · 학회 정규 논문*.
- G H Kim, S Y Chun. "DATID-3D: Diversity-Preserved Domain Adaptation Using Text-to-Image Diffusion for 3D Generative Model". *CVPR 14203-14213, Jun 2023 (was arXiv:2211.16374 [cs.CV]) (2023 Qualcomm Innovation Fellowship Korea) · 학회 정규 논문*.
- D W Park, B H Lee, S Y Chun. "All-in-one Image Restoration for Unknown Degradations Using Adaptive Discriminative Filters for Specific Degradations". *CVPR 5815-5824, Jun 2023 · 학회 정규 논문*.
- S M Hong, S Y Chun. "Neural Diffeomorphic Non-Uniform B-Spline Flows". *AAAI 12225-12233, Feb 2023 (was arXiv:2304:04555) (Oral) · 학회 정규 논문*.
- H C Lee\*, W G Jeong\*, D I Ryu\*, H W Je, A No, K J Kim\*\*, S Y Chun\*\*. "Fully Quantized Always-on Face Detector Considering Mobile Image Sensors". *ICCVW (LBQNN), 2023 (\*co-first authors, \*\*co-corresponding authors) (oral) (was arXiv:2311.01001) · 학회 단편·초록·워크숍 논문*.
- D W Park, M J Kim, H J Kim, J H Lee, S Y Chun. "Domain adaptation from posteroanterior to anteroposterior X-ray radiograph classification via deep neural converter with label recycling". *ICEIC, Feb 2023. · 학회 단편·초록·워크숍 논문*.
- D W Park, M J Kim, H J Kim, J H Lee, S Y Chun. "Domain adaptation from posteroanterior to anteroposterior X-ray radiograph classification via deep neural converter with label recycling". *IFMIA, Jan 2023. · 학회 단편·초록·워크숍 논문*.
- G H Kim\*, D U Kang\*, H G Seo\*, H Y Kim\*, S Y Chun. "Detailed Human-Centric Text Description-Driven Large Scene Synthesis". *arXiv:2311.18654 [cs.CV], Nov 2023 (This work was superceded by arXiv:2404.04544) · 기술 보고서*.
- H G Seo\*, H Y Kim\*, G H Kim\*, S Y Chun. "DITTO-NeRF: Diffusion-based Iterative Text To Omni-directional 3D Model". *arXiv:2304.02827 [cs.CV], Apr 2023 (\*co-first authors) · 기술 보고서*.

**2022**

- S Abu-Hussein, T Tirer, S Y Chun, Y C Eldar, R Giryes. "Image Restoration by Deep Projected GSURE". *WACV 3602-3611, Jan 2022 (was arXiv:2102.02485 [cs.CV]) · 학회 정규 논문*.
- A Ignatov et al. (including B H Lee, D W Park, S M Hong, J H Lee, S G Lee, S Y Chun), Efficient Single-Image Depth Estimation on Mobile Devices, Mobile AI & AIM 2022 Challenge: Report, ECCV Workshops, Oct 2022 · 학회 단편·초록·워크숍 논문
- A Ignatov et al. (including S M Hong, D W Park, J H Lee, B H Lee, S G Lee, S Y Chun), Efficient and Accurate Quantized Image Super-Resolution on Mobile NPUs, Mobile AI & AIM 2022 Challenge: Report, ECCV Workshops, Oct 2022 · 학회 단편·초록·워크숍 논문
- J H Park, D W Park, H G Shin, E J Choi, D M Shin, S Y Chun, J H Lee. "Coil to Coil: Self-supervised denoising using phased-array coil images". *ISMRM 1157, May 2022 · 학회 단편·초록·워크숍 논문*.
- H V Kim\*, S Y Yie\*, S Y Chun\*\*, J S Lee\*\*. "PUREcomb: Poisson Unbiased Risk Estimator based Ensemble of Self-supervised Deep Denoisers for Clinical Bone Scan Image". *IEEE ISBI, Mar 2022 (\*co-first authors, \*\*co-corresponding authors) · 학회 단편·초록·워크숍 논문*.
- D U Kang, S Y Chun. "Multi-Scale Curriculum Learning For Efficient Automatic Whole Slide Image Segmentation". *IEEE BigComp AI-BioHealth Workshop, Jan 2022 · 학회 단편·초록·워크숍 논문*.
- J H Park, D W Park, H-G Shin, E-J Choi, H J An, M J Kim, D M Shin, S Y Chun, J H Lee. "Coil2Coil: Self-supervised MR image denoising using phased-array coil images". *arXiv:2208.07552 [cs.CV], Aug 2022 · 기술 보고서*.
- O C Jung\*, D U Kang\*, G H Kim\*, S Y Chun. "Adaptive GLCM sampling for transformer-based COVID-19 detection on CT". *arXiv:2207.01520 [cs.CV], Jul 2022 (\*co-first authors) · 기술 보고서*.
- I Y Chun\*, D W Park\*, X Zheng\*, S Y Chun, Y Long. "Self-supervised regression learning using domain knowledge: Applications to improving self-supervised denoising in imaging". *arXiv:2205.04821 [cs.CV], May 2022 (\*co-first authors) · 기술 보고서*.

**2021**

- Y Kang et al. (including W J Hong, D U Kang, S Y Chun). "Development and Operation of A Digital Platform for Sharing Pathology Image Data". *BMC Medical Informatics and Decision Making 21,114, Apr 2021 · 학술지*.
- Y J Kim, H Jang, K Lee et al. (including J S Kim, W J Hong, S Y Chun\*\*). "PAIP 2019: Liver cancer segmentation challenge". *Medical Image Analysis 67,101854, Jan 2021 (\*\*Co-corresponding authors) · 학술지*.
- Y S Jo, S Y Chun, J H Choi. "Rethinking Deep Image Prior for Denoising". *ICCV 5087-5096, Oct 2021 · 학회 정규 논문*.
- K Y Kim, D W Park, K I Kim, S Y Chun. "Task-Aware Variational Adversarial Active Learning". *CVPR 8166-8175, Jun 2021 (was arXiv:2002.04709 [cs.LG]) · 학회 정규 논문*.
- B H Lee, S Y Chun. "Empirically Accelerating Scaled Gradient Projection Using Deep Neural Network For Inverse Problems In Image Processing". *IEEE ICASSP 1415-1419, Jun 2021 (was arXiv:1902.02449 [cs.LG]) · 학회 단편·초록·워크숍 논문*.

## 과제

소식 페이지가 알린 선정 2건이다. 과제 이름과 지원 기관, 협력 표기는 소식 글 그대로다.[^news] 삼성미래기술육성사업 선정은 공과대학 소식(2026-10-12 게시)도 2026년 하반기 선정으로 알린다.[^engnews]

- 2026 Oct · Forgetting as a Fundamental Operation of Intelligence (지원 Samsung Science & Technology Foundation (Samsung Science & Technology Program))
- 2026 Mar · megabase-scale DNA foundation model project (NVIDIA will be providing 32,000 A100 GPU-hours to SNU) (지원 NVIDIA Academic Grant Program; 협력 기관 Prof. Hoon Kim at SKKU)

## 특허

누리집 Publications 페이지 연도 구역의 Patent 칸 가운데 출원이나 등록 날짜가 2021-10-22–2026-10-22에 드는 17건이다. 날짜는 줄 끝의 표기이고(2022년 줄은 연도만 적혀 있다), 발명자·제목·출원과 등록 표기는 페이지 그대로다. 같은 발명의 한국·미국·국제(PCT) 출원과 등록이 따로 실려 있다.[^pubs]

- Apr 2026 · S Y Chun, S M Hong, K R Lee, "Audio Data Management Device and Method Using A Generative AI Model," PCT Filed, Apr 2026
- Feb 2026 · S Y Chun, D W Park, B H Lee, "All-in-one image quality improvement model providing method performing image quality restoration for multiple image quality degradation factors," US Patent Granted (12,555,203), Feb 2026
- Dec 2025 · S Y Chun, G H Kim, "Diversity-Preserving Domain Adaptation Using Text-to-image Diffusion For 3D Generative Model," Korea Patent Granted (10-2903508), Dec 2025
- Dec 2025 · S Y Chun, D W Park, B H Lee, "Method for providing all-in-one image quality improvement model that performs image quality restoration for multiple image quality inhibitors," Korea Patent Granted (10-2903223), Dec 2025
- Apr 2025 · S Y Chun, S M Hong, K R Lee, "Audio Data Management Device and Method Using A Generative AI Model," Korea Patent Filed, Apr 2025
- Mar 2025 · S Y Chun, J H Jang, H G Seo, "Method For Affordance Grounding and Apparatus Therefor," Korea Patent Filed, Mar 2025
- Feb 2025 · S Y Chun, H G Seo, H W Bae, D U Kang, H Kim, H J Sun, "Device and Method for Extracting High-Dimensional Gene Fearures Based on Data Dimension Reduction," Korea Patent Filed,Feb 2025
- Jan 2025 · S Y Chun, G H Kim, H Y Kim, H G Seo, D U Kang, "Method and Apparatus for Generating High-resolution Human-centric Scene Using Pretrained Diffusion Model," US Patent Filed, Jan 2025
- Nov 2024 · S Y Chun, D W Park, H Y Kim, "Learning Method for Image Restoration Model and Apparatus for Performing The Same," US Patent Filed, Nov 2024
- Oct 2024 · S Y Chun, G H Kim, "Domain Adaptation Using Pose-Preserved Text-to-image Diffusion For 3D Generative Model," US Patent Filed, Oct 2024
- Aug 2024 · S Y Chun, G H Kim, H Y Kim, H G Seo, D U Kang, "Method and Apparatus for Generating High-resolution Human-centric Scene Using Pretrained Diffusion Model," Korea Patent Filed, Aug 2024
- Feb 2024 · S Y Chun, D W Park, H Y Kim, "Learning Method for Image Restoration Model and Apparatus for Performing The Same," Korea Patent Filed, Feb 2024
- Dec 2023 · S Y Chun, G H Kim, "Diversity-Preserved Domain Adaptation Using Text-to-image Diffusion For 3D Generative Model," US Patent Filed, Dec 2023
- Nov 2023 · S Y Chun, G H Kim, "Domain Adaptation Using Pose-Preserved Text-to-image Diffusion For 3D Generative Model," Korea Patent Filed, Nov 2023
- Jul 2023 · J H Choi, Y S Jo, S Y Chun, "Method and Device for Denoising Image with Noise by Using Deep Image Prior Which Has Been Applied With Stochastic Temporal Ensembling and Optimized Stopping Timing Automatic Decision Algorithm," Korea Patent Granted (10-2561613), Jul 2023
- May 2023 · S Y Chun, D W Park, D U Kang, "Deep Learning-Based Image Deblurring Method And Apparatus," US Patent Granted (11,645,738), May 2023
- 2022 · S Y Chun, D W Park, Y H Seo, "Robot grasping method based on single neural network and apparatus performing the same," Korea Patent Granted (10-2397079), 2022

## 수상과 선정

날짜가 2021-10-22–2026-10-22에 드는 수상과 선정 16건이다. 소식 페이지, Publications 페이지 논문 줄의 괄호 표기, Members 페이지의 구성원 줄, 교수 소개 페이지에서 모았고, 상 이름과 순위 표기는 원문 그대로이며 괄호 안 이름은 원문이 적은 수상자다. 원문이 연도만 적은 항목은 연도만 적었다. ISMRM 발표의 oral·summa cum laude·magna cum laude·AMPC select는 논문 줄의 괄호 표기다.[^news][^pubs][^members][^pi]

- 2026 Aug · Youlchon AI Star (Wongi Jeong)
- 2026 Jun · CVPR Compute Transparency Champion award: 「Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models」(CVPR 2026). This work was also highlighted at the Popular Science.
- 2026 Feb · IPAI Best Master's Thesis Award (Sungjin Lim)
- 2025 Oct · BK21Four - SNU Fellowship of Research Excellence (Hoigi Seo)
- 2025 Sep · 2nd place at MICCAI'25 Challenge on REport Generation in pathology using Pan-Asia Giga-pixel WSIs (REG) (Byung Hyun Lee, Sungjin Lim, Joohoon Lee, Gwanghyun Kim)
- 2025 Aug · Best Paper Award: 「Object-Interactive Human Motion Generation via Affordance Reasoning」 (Conference on Electronics, Semiconductor and AI)
- 2025 Jun · 2025 Qualcomm Innovation Fellowship Korea Finalist: 「Localized Concept Erasure for Text-to-Image Diffusion Models Using Training-Free Gated Low-Rank Adaptation」(CVPR 2025, Byung Hyun Lee)
- 2025 May · ISMRM 발표 「Harmonization for a black-box deep learning model」 (oral, summa cum laude, AMPC select)
- 2025 · ECE outstanding PhD dissertation award (Seongmin Hong)
- 2025 · Youlchon AI Star (Byung Hyun Lee)
- 2024 Oct · Best Poster Presentation Award: 「Selective Concept Erasing for Safe Diffusion Models」 (Korea Signal Processing Conference)
- 2024 Jul · 3rd place at the 2024 Ego4D-Ego-Exo4D Challenge in the Short-term Object Interaction Anticipation Track at CVPR'24
- 2024 · ISMRM 2024 발표 「MOST: MR reconstruction Optimization for multiple downStream Tasks via continual learning」 (oral, magna cum laude)
- 2024 · 2024 Qualcomm Innovation Fellowship Korea: 「On Exact Inversion of DPM-Solvers」(CVPR 2024, Seongmin Hong)
- 2023 · 2023 Qualcomm Innovation Fellowship Korea: 「DATID-3D: Diversity-Preserved Domain Adaptation Using Text-to-Image Diffusion for 3D Generative Model」(CVPR 2023)
- 2022 · SNU CoE Outstanding Teaching Award (전세영 교수)

## 소식

소식 페이지 Recent News / Publications (~1 year) 칸 22건 가운데 연구·학술 활동 소식 8건이다(2026년 3월–2026년 9월). 날짜는 글머리의 연·월 표기이고, 문장은 각 글의 알림 문장을 옮긴 것이다. 소식에 함께 붙은 논문 서지는 최근 논문 목록에 있고, 선정과 수상 소식은 위 과제와 수상 절에 있다.[^news]

- 2026 Sep · Three papers accepted at NeurIPS'26 (1 selected as Spotlight).
- 2026 Sep · Se Young Chun gave an invited keynote at ECCV'26 Beyond Euclidean Workshop.
- 2026 Jun · One paper accepted at ECCV'26.
- 2026 May · One paper accepted at ICML'26.
- 2026 Apr · Se Young Chun will serve as an Area Chair of NeurIPS'26.
- 2026 Apr · Seven papers accepted at CVPR'26 (3 selected as Highlights!).
- 2026 Mar · One collaboration paper published at Theranostics
- 2026 Mar · One paper accepted at IEEE Access (IEEE Geoscience and Remote Sensing Society Section).

## 연락과 위치

- 교수실: 서울대학교 301동 904호[^eceprof]
- 전화: 02-880-1811[^eceprof][^ecelabv]
- 주소: 08826 서울특별시 관악구 관악로 1 서울대학교 전기·정보공학부[^eceprof]
- 참여 안내: Join ICL? 페이지는 전기·정보공학부(ECE)나 인공지능전공(AI)의 석박사통합과정(combined MS/PhD)을 하려는 대학원생 자리가 보통 몇 개 있고, 박사과정은 자리가 매우 적다고 적는다. 학부 인턴 프로그램은 보통 여름·겨울 방학마다 열며, 이력서와 성적표를 교수에게 보내되 여름 인턴은 보통 4–5월, 겨울 인턴은 10–11월에 연락하라고 적는다.[^join]
[^home]: 연구실 누리집 첫 화면 <https://icl.snu.ac.kr/> (연구실 소개, 소속, Recent News / Publications 칸, 2026-10-25 열람)
[^pi]: PI 페이지 <https://icl.snu.ac.kr/pi> (연구 관심, Academic Appointments, Education, Selected Honor / Award, Academic Services, 2026-10-25 열람)
[^members]: Members 페이지 <https://icl.snu.ac.kr/members> (Current members, Past members 칸, 2026-10-25 열람)
[^pubs]: Publications 페이지 <https://icl.snu.ac.kr/publications> (2004–2026년 연도 구역의 Journal·Conference·Technical Report·Patent 칸, 2026-10-25 열람)
[^news]: News 페이지 <https://icl.snu.ac.kr/news> (Recent News / Publications (~1 year) 칸, 2026-10-25 열람)
[^teaching]: Teaching 페이지 <https://icl.snu.ac.kr/teaching> (SNU·UNIST 학부·대학원 강의, 2026-10-25 열람)
[^join]: Join ICL? 페이지 <https://icl.snu.ac.kr/join-icl> (대학원생·학부 인턴 안내, 2026-10-25 열람)
[^ecelab]: 서울대학교 전기·정보공학부 연구실 목록 <https://ece.snu.ac.kr/research-faculty/research/lab> (연구그룹별 연구실, 2026-10-25 열람)
[^ecelabv]: 서울대학교 전기·정보공학부 연구실 소개 「지능형 계산영상 연구실」 <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=101> (연구실 소개 및 연구분야, 최근 관심분야, 전화, 2026-10-25 열람)
[^eceprof]: 서울대학교 전기·정보공학부 전임교수 소개 「전세영」 <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p869> (학위, 분야, 학력, 주요경력, Research Interest, 교수실과 전화, 2026-10-25 열람)
[^gsai]: 서울대학교 대학원 협동과정 인공지능전공 교수진 목록 <https://gsai.snu.ac.kr/%ea%b5%90%ec%88%98%ec%a7%84-%eb%aa%a9%eb%a1%9d/> (전공 표기, 2026-10-25 열람)
[^engnews]: 서울대학교 공과대학 공대뉴스광장 「'잊을 줄 아는 AI'·'느낄 줄 아는 로봇'…서울대, 삼성미래기술육성사업 2개 과제 선정」 <https://eng.snu.ac.kr/communication/promotion/news?md=v&bbsidx=8428> (2026-10-12 게시, 2026-10-25 열람)
[^dil]: T. Tirer, R. Giryes, S. Y. Chun, Y. C. Eldar, IEEE Signal Processing Magazine 41, 40-57 (2024). <https://doi.org/10.1109/msp.2024.3385950> 초록 기준(Semantic Scholar 등록 초록).
[^p1]: J. Bang 외, S. Y. Chun, ICML 2026 (누리집 표기 Accepted at ICML, Jul 2026). <https://arxiv.org/abs/2605.26470> 초록 기준(arXiv 2605.26470 판, 판본 표기 ICML 2026).
[^p2]: S. Hong, J. Bae, J. Lee, S. Y. Chun, Lecture Notes in Computer Science, 307-322 (ECCV 2024, 누리집 표기 ECCV 15123:307-322, 온라인 2024-11-21). <https://doi.org/10.1007/978-3-031-73650-6_18> 초록 기준(arXiv 2409.11738 판, 판본 표기 Accepted to ECCV 2024).
[^p3]: H. Kim 외, S. Y. Chun, IEEE Transactions on Medical Imaging 42, 2961-2973 (2023). <https://doi.org/10.1109/tmi.2023.3270868> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: B. H. Lee 외, S. Y. Chun, 2025 IEEE/CVF International Conference on Computer Vision (ICCV), 23232-23242 (2025). <https://doi.org/10.1109/iccv51701.2025.02157> 초록 기준(arXiv 2507.02395 판, 판본 표기 Accepted at ICCV 2025).
[^p5]: B. H. Lee, S. Lim, S. Y. Chun, 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 18596-18606 (2025). <https://doi.org/10.1109/cvpr52734.2025.01733> 초록 기준(arXiv 2503.12356 판, 판본 표기 Accepted to CVPR 2025).
[^p6]: H. Seo, W. Jeong, J. Seo, S. Y. Chun, ICML 2025 (누리집 표기 ICML 267:53867-905, Jul 2025). <https://arxiv.org/abs/2502.08690> 초록 기준(arXiv 2502.08690 판).
[^p7]: H. Seo 외, S. Y. Chun, Advances in Neural Information Processing Systems 38, 144787-144842 (2025). <https://doi.org/10.52202/085713-4352> 초록 기준(arXiv 2510.09008 판).
[^p8]: J. H. Jang, H. Seo, S. Y. Chun, Lecture Notes in Computer Science, 18-34 (ECCV 2024, 누리집 표기 ECCV 15122:18-34, 온라인 2024-10-31). <https://doi.org/10.1007/978-3-031-73039-9_2> 초록 기준(arXiv 2409.06210 판).

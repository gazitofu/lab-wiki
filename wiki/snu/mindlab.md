# 기계지능 및 데이터사이언스 연구실 (Machine Intelligence and Data Science Lab, M.IN.D Lab)

**서울대학교 공과대학 전기·정보공학부 · 문태섭 교수**

- 분야: 적응형 기계학습, 연속학습, 강화학습, 공정하고 설명할 수 있는 인공지능, 시각·언어 학습, 뇌영상 데이터 분석
- 대분야: 컴퓨팅·AI
- 태그: 강화학습[^research][^p2], 멀티모달 AI[^research][^p4], 대형 언어 모델[^p3], 컴퓨터 비전[^p4][^p8]
- 홈페이지: <https://mindlab-snu.notion.site/>
- 근거와 출처: [기계지능 및 데이터사이언스 연구실 근거 페이지](mindlab-sources.md)

> 자료와 환경이 바뀌어도 배움을 이어 가는 기계학습, 공정하고 믿을 수 있는 인공지능, 실제 데이터 문제를 푸는 학습 방법을 연구한다. 시각·언어 모델과 뇌영상 분석이 주요 연구 사례다.[^research][^p3][^p7]

## 무엇을 연구하나

문태섭 교수가 이끄는 M.IN.D Lab은 기계학습(machine learning, ML, 자료에서 규칙을 배워 분류나 예측 모델을 만드는 방법)과 딥러닝(deep learning, 여러 층의 신경망으로 자료의 규칙을 학습하는 방법) 알고리즘을 개발한다. 연구실은 제한되고 시간에 따라 바뀌는 정보를 다루는 적응형 기계학습, 공정성·안전성·설명 가능성을 다루는 신뢰할 수 있는 기계학습, 실제 데이터에 대한 응용을 현재 연구의 세 갈래로 소개한다.[^prof][^research]

적응형 학습에서는 **새 자료를 배우면서 이전의 지식을 유지하는 일**을 다룬다. 연속학습(continual learning, 새 자료나 과제를 순서대로 배우면서 이전에 배운 지식을 유지하는 학습)이 중심 주제다. 자기지도학습(self-supervised learning, 자료 자체에서 학습 신호를 만들어 배우는 방법)에서는 이전 모델과 현재 모델의 출력을 이용해 새 표현이 과거의 배움과 충돌하지 않도록 하는 PNR(Pseudo-Negative Regularization)을 제안했다. 강화학습(reinforcement learning, 행동에 따른 보상을 이용해 행동 규칙을 배우는 방법)에서는 사람이 여러 행동 기록 가운데 무엇을 얼마나 선호하는지 반영해 보상을 추정하는 LiRE(Listwise Reward Estimation)를 연구했다.[^research][^p1][^p2]

신뢰할 수 있는 학습에서는 **누구에게나 공정한 결과와 흔들리지 않는 설명**을 목표로 한다. 연구실은 알고리즘 공정성, 인공지능 안전성, 설명 가능한 인공지능, 강건성(입력이나 조건이 달라져도 기능을 유지하는 성질)을 주요 주제로 든다. FairDRO는 집단 공정성(집단별 예측 결과나 오류 사이의 차이를 정해진 기준으로 다루는 것)을 학습 목표에 넣고, 분포 강건 최적화(자료 분포가 달라지는 경우도 고려해 학습 목표가 정한 값을 최소화하는 해를 찾는 방법)를 통해 집단별 가중치(각 항목이 계산 결과에 미치는 비중을 정하는 값)를 정한다. 설명 연구에서는 특징 기여도(입력의 각 부분이 예측에 기여한 정도)가 입력 변화에 따라 달라지는 문제를 분석하고, 설명을 표시할 때 쓰는 정규화(수치의 척도나 범위를 정해진 기준에 맞추는 변환)를 고려한 학습 방법을 제안했다.[^research][^p5][^p6]

시각·언어 연구에서는 **종류가 다른 자료를 함께 배우고 이미 배운 지식을 새 과제에 맞게 쓰는 일**을 다룬다. 멀티모달 학습(multimodal learning, 그림·글·소리처럼 종류가 다른 자료를 함께 다루는 학습)이 한 축이다. GRIT-VLP(Grouped Mini-batch Sampling for Efficient Vision and Language Pre-training)는 그림과 글을 묶어 학습할 때 비슷한 사례를 한 묶음에 모으는 방법을 제안했다. DoMIX는 대형 언어 모델(많은 글로 학습해 언어를 처리하는 인공지능 모델)의 분야별 지식을 병렬로 학습하고, 파인튜닝(fine-tuning, 이미 학습한 모델의 매개변수를 새 과제에 맞게 조정하는 과정)에 활용한다.[^research][^p3][^p4]

데이터과학 응용에는 뇌과학, 배터리 관리, 양자역학, 유전체, 반도체의 무작위 변동 모형화, 공기질 관측, 원격탐사가 포함된다.[^research] 뇌영상 연구의 TABLeT(Two-dimensionally Autoencoded Brain Latent Transformer)는 기능적 자기공명영상(functional Magnetic Resonance Imaging, fMRI, 뇌활동과 관련된 신호 변화를 자기공명영상으로 측정하는 방법)을 압축한 뒤 시간에 따른 변화를 학습한다. 자연 이미지용 오토인코더(입력을 압축했다가 복원하도록 학습한 신경망)를 활용하는 방법이다.[^p7] SEED(Semantic Evaluation for Visual Brain Decoding)는 뇌 신호에서 복원한 이미지가 원래 이미지의 의미를 얼마나 담았는지 평가하는 지표를 제안하고, 사람의 평가와 대조한다.[^p8]

## 주요 연구 주제

### 1. 연속학습과 강화학습

자료가 순서대로 들어올 때 이전 지식을 유지하는 자기지도학습과, 이미 모아 둔 행동 기록으로 배우는 오프라인 강화학습을 연구한다. PNR은 이전 모델과 현재 모델의 출력을 학습에 활용하고, LiRE는 여러 행동 기록의 선호 순서를 보상 추정에 이용한다.[^p1][^p2]

### 2. 언어·시각 모델의 효율적인 학습

이미지와 글을 함께 학습할 때 학습 사례를 어떻게 묶을지, 분야별로 배운 지식을 어떤 과제에 어떻게 결합할지 다룬다. GRIT-VLP는 학습 묶음의 구성을, DoMIX는 분야별 사전 학습과 과제별 결합을 연구한다.[^p3][^p4]

### 3. 공정성과 설명의 안정성

집단 간 예측 격차를 학습 과정에 반영하는 FairDRO와, 입력이 달라져도 예측 이유의 설명이 안정적으로 남도록 하는 국소 기울기 정렬을 연구한다. 기울기는 입력 변화에 따라 출력이 어느 방향으로 얼마나 변하는지를 나타내는 값이다.[^p5][^p6]

### 4. 뇌영상 모델과 평가

시간에 따라 변하는 뇌영상 신호를 압축해 학습하는 TABLeT와, 뇌 신호에서 복원한 그림의 의미를 평가하는 SEED를 연구한다. 새로운 모델 구조와 평가 방법을 개발하는 갈래다.[^p7][^p8]

## 대표 논문

문태섭 교수가 마지막 저자이고 서울대 재직 시기에 나온 논문에서 네 갈래별로 두 편씩 골랐다. 2026년 논문 두 편을 포함한다. 학회 논문집이 있는 세 편은 그 논문집의 초록을, 나머지 다섯 편은 표에 표시한 arXiv 판의 초록을 기준으로 설명했다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [Regularizing with Pseudo-Negatives for Continual Self-Supervised Learning](https://proceedings.mlr.press/v235/cha24a.html) · ICML | 자료가 차례로 바뀌는 자기지도학습에서 새로 배운 표현과 과거의 표현이 충돌하지 않도록 하는 PNR을 제안했다. 현재 모델과 이전 모델이 만든 출력을 이용해 학습을 규제한다. 대조 학습(사례 사이의 관계를 구별해 표현을 배우는 방법)에서는 두 모델로 만든 가상 음성 사례(서로 다른 것으로 취급하는 비교 사례)를 학습 목표와 규제에 함께 쓴다. 기존에 이런 비교 사례를 필요로 하지 않는 학습에도 이전 모델 출력을 이용한 규제를 도입했다. 실험에서 새로운 것을 배우는 능력과 기존 지식을 유지하는 능력의 균형을 다뤘다.[^p1] | Sungmin Cha, Kyunghyun Cho, Taesup Moon(마지막 저자) |
| 2 | 2024 | [Listwise Reward Estimation for Offline Preference-based Reinforcement Learning](https://proceedings.mlr.press/v235/choi24b.html) · ICML | 사람이 어느 행동 기록을 선호하는지로 강화학습의 보상을 배우되, 단순히 어느 쪽이 좋은지를 넘어 선호의 상대적 강도를 반영하는 LiRE를 제안했다. 행동 기록에 순서를 매긴 목록을 만들며, 기존 방법과 같은 세 가지 선택의 피드백으로 이 목록을 구성한다. 추정한 보상의 영향을 평가할 데이터셋도 제안했다. 실험에서는 피드백 수가 제한되거나 피드백에 잡음이 섞이는 조건에서 방법을 평가했다.[^p2] | Heewoong Choi, Sangwon Jung, Hongjoon Ahn, Taesup Moon(마지막 저자) |
| 3 | 2025 | [DoMIX: An Efficient Framework for Exploiting Domain Knowledge in Fine-Tuning](https://aclanthology.org/2025.acl-long.710/) · ACL | 이미 학습한 모델에 여러 분야의 지식을 더할 때 계산비용, 자료를 배우는 순서, 과제별 맞춤 문제를 함께 다룬다. 모델의 일부 변수만 조정하는 학습 모듈을 활용해 분야별 사전 학습을 병렬로 진행하고, 모아 둔 지식을 특정 과제에 맞춰 이용하는 DoMIX를 제안했다. 분야별 자료를 순차적으로 한 모델에 넣는 방식의 한계를 다루며, 일반적인 대형 언어 모델 파인튜닝에도 확장할 수 있음을 보였다.[^p3] | Dohoon Kim, Donghun Kang, Taesup Moon(마지막 저자) |
| 4 | 2022 | [GRIT-VLP: Grouped Mini-batch Sampling for Efficient Vision and Language Pre-training](https://arxiv.org/abs/2208.04060) · arXiv 사전 공개본 | 그림과 글의 사전 학습에서 서로 구별하기 어려운 사례를 고르는 방법과 글의 일부를 가리는 비율이 학습 결과에 영향을 준다는 점을 분석했다. 비슷한 사례를 한 학습 묶음에 모으는 GRIT, 이미지·글 대조 학습의 일관성을 위한 학습 목표, 글을 가리는 비율 조정을 결합했다. 같은 학습 자료에서 기존 ALBEF와 비슷한 성능을 학습 주기 수 3분의 1로 얻었다고 보고했다.[^p4] | Jaeseok Byun, Taebaek Hwang, Jianlong Fu, Taesup Moon(마지막 저자) |
| 5 | 2023 | [Re-weighting Based Group Fairness Regularization via Classwise Robust Optimization](https://arxiv.org/abs/2303.00442) · arXiv 사전 공개본 | 집단 공정성을 높이는 두 접근인 학습 사례의 가중치 조절과 학습 목표에 공정성 규제를 넣는 방법을 결합했다. 공정성 지표를 분류 범주별 분포 강건 최적화의 학습 목표에 넣고, 집단별 가중치를 반복적으로 자동 산출하는 FairDRO를 제안했다. 여러 평가 데이터에서 정확도와 공정성 사이의 균형을 비교했다.[^p5] | Sangwon Jung, Taeeon Park, Sanghyuk Chun, Taesup Moon(마지막 저자) |
| 6 | 2023 | [Towards More Robust Interpretation via Local Gradient Alignment](https://arxiv.org/abs/2211.15900) · AAAI 2023, arXiv v2 초록 | 신경망이 예측한 이유를 보여 주는 특징 기여도가 입력의 작은 교란에 흔들리는 문제를 다뤘다. 특정 신경망에서는 정규화된 기울기가 같아도 기존의 기울기 견고함 기준값은 달라질 수 있음을 보였다. 기울기의 방향을 고려하는 기준을 분석하고 크기와 방향을 함께 고려하는 학습 규제를 제안했다. 실험에서 분류 정확도를 크게 해치지 않으면서 설명의 안정성이 좋아졌다고 보고했다.[^p6] | Sunghwan Joo, Seokhyeon Jeong, Juyeon Heo, Adrian Weller, Taesup Moon(마지막 저자) |
| 7 | 2026 | [Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?](https://arxiv.org/abs/2604.03619) · CVPR 2026, arXiv 초록 | 뇌영상의 시간적 변화를 학습할 때 영상 자료의 크기로 인해 긴 시간 구간을 다루기 어려운 문제에 대응하는 TABLeT를 제안했다. 자연 이미지로 미리 학습한 2차원 오토인코더로 3차원 뇌영상을 압축하고, 압축된 토큰(모델이 처리하는 정보 단위)의 긴 시퀀스(순서가 있는 열)를 트랜스포머(입력 요소 사이의 관계를 학습하는 신경망 구조)로 학습한다. 여러 뇌영상 데이터에서 계산·메모리 효율과 과제 성능을 평가했으며, 일부 토큰을 가리고 맞히는 자기지도 사전 학습도 개발했다. 뇌활동의 시간·공간 모델링에 활용할 가능성을 제시한다.[^p7] | Peter Yongho Kim 외, Taesup Moon(마지막 저자) |
| 8 | 2026 | [SEED: Towards More Accurate Semantic Evaluation for Visual Brain Decoding](https://arxiv.org/abs/2503.06437) · ICLR 2026, arXiv v3 초록 | 뇌 신호에서 복원한 그림이 원래 그림의 의미를 얼마나 보존했는지를 재는 SEED를 제안했다. 이미지의 의미적 유사성을 서로 다른 측면에서 재는 세 지표를 결합하고, 사람이 직접 평가한 자료와 비교했다. 기존 평가에서 높은 점수를 받은 모델도 의미 정보의 중요한 부분을 잃을 수 있음을 보였다. 평가 방법 연구를 위해 사람의 평가 자료와 코드를 공개했다.[^p8] | Juhyeon Park, Peter Yongho Kim, Jiook Cha, Shinjae Yoo, Taesup Moon(마지막 저자) |

## 교수와 전문 분야

문태섭 교수(Taesup Moon)는 서울대학교 공과대학 전기·정보공학부 교수다. 2021년 3월 서울대 부교수로 부임했고, 2024년 9월부터 교수로 재직한다. 서울대학교 전기공학 학사(2002), 스탠퍼드대학교 전기공학 석사(2004)·박사(2008) 학위를 받았다.[^prof]

서울대 부임 전에는 Yahoo! Labs 연구원, UC 버클리 통계학과 박사후연구원, 삼성전자 종합기술원 전문연구원, DGIST 정보통신융합공학전공 조교수, 성균관대학교 전자전기공학부 조교수·부교수로 일했다.[^prof] 연구실 교수 소개에는 스탠퍼드대학교 방문교수(2024.9–2025.8), 전기·정보공학부 교무 담당 부학부장(Vice Chair of Academic Affairs, 2025.9부터) 경력이 있다.[^pi]

학과는 전문 분야를 머신러닝·인공지능·정보이론으로, 연구 분야를 적응형 기계학습·신뢰가능 AI·데이터 응용으로 소개한다.[^prof] 대표 논문에서는 연속학습과 사람의 선호를 반영하는 강화학습, 언어·시각 모델의 효율적인 학습, 집단 공정성과 설명의 안정성, 뇌영상 모델·평가 방법을 개발하는 전문성이 드러난다.[^p1][^p2][^p3][^p5][^p6][^p7][^p8]

## 응용 분야

연구실은 뇌과학, 배터리 관리, 양자역학, 유전체, 반도체 변동 모형, 공기질 관측, 원격탐사를 데이터과학 응용으로 제시한다. 뇌과학은 Jiook Cha·Jangsup Moon, 배터리 관리는 Jang Wook Choi, 양자역학은 Joon Hee Choi 등과의 협업으로 소개한다.[^research] 대표 논문의 구체적인 쓰임은 사람이 선호하는 행동을 배우는 보상 추정, 분야 지식에 맞춘 언어 모델 조정, 그림과 글의 공동 학습, 뇌영상 신호의 시간적 변화 학습과 복원 이미지 평가다.[^p2][^p3][^p4][^p7][^p8]

## 구성원

구성원 보기의 박사과정 12명, 석박사통합과정 4명, 석사과정 4명이다. 과정과 연구 주제는 구성원 보기의 표기를 따르고, 시작 시기와 학교 이메일은 각 사람의 소개에 적힌 값을 사용했다. 시작 칸의 괄호는 해당 날짜에 붙은 과정 표기다. 대표 논문 참여는 게시된 이름과 저자 이름을 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Taeeon Park[^m1] | 박사과정 | 2021.09 (Ph.D.) | AI Safety, Trustworty ML, Data Science Applications | pte1235@snu.ac.kr | 5 |
| Hongjoon Ahn[^m2] | 박사과정 |  | RL, Continual Learning |  | 2 |
| Yong Jin Jeong[^m3] | 박사과정 |  | Physics+AI, Data Science Applications | yongjin.jeong@snu.ac.kr |  |
| Jihwan Kwak[^m4] | 박사과정 |  | Adaptive ML, Generative Models |  |  |
| Dohoon Kim[^m5] | 박사과정 | 2022.03 (M.S./Ph.D) | Adaptive ML, Generative Models, LLM |  | 3 |
| Hyunwoong Bae[^m6] | 박사과정 |  | AI Safety, Generative Models | hwbae0326@snu.ac.kr |  |
| Heewoong Choi[^m7] | 박사과정 | 2023.03 (M.S./Ph.D) | Adaptive ML, RL | chw0501@snu.ac.kr | 2 |
| Juhyeon Park[^m8] | 박사과정 |  | AI Safety, Brain + AI | parkjh9229@snu.ac.kr | 7, 8 |
| Sumin Yu[^m9] | 박사과정 | 2023.03 (M.S./Ph.D) | AI Safety, Trustworty ML | ysmsoomin@snu.ac.kr |  |
| Yongho Kim (김용호)[^m10] | 박사과정 |  | AI Safety, Brain + AI, Generative Models | peterkim98@snu.ac.kr | 7, 8 |
| Jinu Hyeon[^m11] | 박사과정 | 2023.03 (M.S / Ph.D) | RL, Adaptive ML |  |  |
| Jisu Han[^m12] | 박사과정 |  | Physics+AI, RL | jshcdi@snu.ac.kr |  |
| Jung Yoon Hwang[^m13] | 석박사통합과정 | 2025.03 (M.S./Ph.D) | Adaptive ML, Generative Models | danieljyh@snu.ac.kr |  |
| Yoseop Jeong[^m14] | 석박사통합과정 | 2026.03 (M.S./Ph.D) | RL | gs16100@snu.ac.kr |  |
| Joonyoung Chang[^m15] | 석박사통합과정 | 2026.03 (M.S./Ph.D) | AI Safety, Brain + AI | jjoon0@snu.ac.kr |  |
| Yeonwoo Kim[^m16] | 석박사통합과정 | 2026.09 (M.S./Ph.D) | Brain + AI | yeonwoo4@snu.ac.kr |  |
| Seyoon Kim[^m17] | 석사과정 |  | LLM |  |  |
| Changmin Lee[^m18] | 석사과정 | 2026.03 (M.S.) | Data Science Applications |  |  |
| Hoyoung Kim[^m19] | 석사과정 | 2026.03 (M.S.) | RL, Generative Models |  |  |
| Yu En Yeoh[^m20] | 석사과정 | 2025.09 (M.S.) |  | ian0204@snu.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 보기의 박사 5명과 석사 11명이다. 학위 연도는 각 소개의 Degree Year, 진로는 Current Position 표기를 따른다. 연도 범위는 2017–2026년이며, 문태섭 교수의 서울대 부임 전 구성원도 포함한다.[^alumni][^prof]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jaeseok Byun[^a1] | PhD (2026) | Amazon AGI |
| Donggyu Lee[^a2] | PhD (2025) | Samsung Electronics |
| Sunghwan Joo[^a3] | PhD (2025) | Postdoc@M.IN.D Lab |
| Sangwon Jung[^a4] | PhD (2025) | Trillion Labs |
| Sungmin Cha[^a5] | PhD (2023) | NYU → Meta |
| Jin Park[^a6] | MS (2026) | Hyundai Motors |
| SeokHyun Jeong[^a7] | MS (2025) | Sionic AI |
| Dohyun Kim[^a8] | MS (2022) | Anatomage Korea |
| Junha Jeon[^a9] | MS (2021) |  |
| Juyeon Heo[^a10] | MS (2020) | Apple |
| Hyeongmin Park[^a11] | MS (2020) |  |
| Yongbee Park[^a12] | MS (2020) |  |
| Jungtae Lee[^a13] | MS (2019) | Samsung Electronics |
| Youngeun Seo[^a14] | MS (2019) | Samsung Electronics |
| Byungjoon Kwon[^a15] | MS (2017) | Samsung Research |
| Jinhee Park[^a16] | MS (2017) |  |

## 최근 논문 목록 (2021–2026)

연구실 논문 목록의 2021–2026년 구역에 기재된 논문이다. 연도는 누리집의 연도 구역이고, 학술지·학회·워크숍을 함께 싣는다. 2021년은 연도 구역 전체를 쓰므로, 문태섭 교수의 2021년 3월 서울대 부임 전 연구 이력이 함께 들어갈 수 있다. 채택 공지가 있는 2026년 EMNLP·AIES·ICML·ACL 항목은 「채택」으로 표시한다. 저자와 서지 표기는 연구실 목록을 따른다.[^pubs][^home][^prof]

**2026**

- Dohoon Kim, Junho Park, Hyungwoong Bae, Seyoon Kim, Taesup Moon. "Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval". *EMNLP (채택)*.
- Sumin Yu, Juhyeon Park, Taesup Moon. "PopResume: Causal Fairness Evaluation of LLM/VLM Resume Screeners with Population-Representative Dataset". *EMNLP (Oral) (채택)*.
- Sumin Yu and Taesup Moon. "Who Will Become the Next Senior?: How Generative AI Erodes the Development Pathway in Software Engineering". *AIES (Oral) (채택)*.
- Jinu Hyeon, Woobin Park, Hongjoon Ahn, and Taesup Moon. "Action-Sufficient Goal Representations". *ICML (채택)*.
- Junho Park, Dohoon Kim, and Taesup Moon. "PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation". *ACL (Oral) (채택)*.
- Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, and Taesup Moon. "Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?". *CVPR*.
- Dongkyu Cho, Taesup Moon, Rumi Chunara, Kyunghyun Cho, and Sungmin Cha. "Forget Forgetting: Continual Learning in a World of Abundant Memory". *ICLR*.
- Juhyeon Park, Peter Yongho Kim, Jiook Cha, Shinjae Yoo, and Taesup Moon. "SEED: Towards More Accurate Semantic Evaluation for Visual Brain Decoding". *ICLR*.
- Yong Jin Jeong and Taesup Moon. "PPIE-Net: Physics-inspired parametric input embedding for data-efficient surrogate modeling of parametric simulations". *Applied Soft Computing*.

**2025**

- Hongjoon Ahn, Heewoong Choi, Jisu Han and Taesup Moon. "Option-aware Temporally Abstracted Value for Offline Goal-Conditioned Reinforcement Learning". *NeurIPS (Spotlight)*.
- Jaeseok Byun, Young Kyun Jang, Seokhyeon Jeong, Donghyun Kim, Taesup Moon. "MA-CIR: A Multimodal Arithmetic Benchmark for Composed Image Retrieval". *ICCV*.
- Jaeseok Byun, Seokhyeon Jeong, Wonjae Kim, Sanghyukk Chun, Taesup Moon. "An Efficient Post-hoc Framework for Reducing Task Discrepancy of Text Encoders for Composed Image Retrieval". *ICCV*.
- Dohoon Kim, Donghun Kang, Taesup Moon. "DoMIX: An Efficient Framework for Exploiting Domain Knowledge in Fine-Tuning". *ACL*.
- Juhyeon Park, SeokHyun Jeong, Taesup Moon. "TLDR: Text Based Last-layer Retraining for Debiasing Image Classifiers". *WACV*.
- Hongjoon Ahn, Jinu Hyeon, Youngmin Oh, Bosun Hwang, Taesup Moon. "Prevalence of Negative Transfer in Continual Reinforcement Learning: Analyses and a Simple Baseline". *ICLR*.
- Sangwon Jung, Alex Oesterling, Claudio Mayrink Verdun, Sajani Vithana, Taesup Moon, Flavio Calmon. "Multi-Group Proportional Representations for Text-to-Image Models". *CVPR*.
- Hyunwoong Bae, Jaeseok Byun, Yongwoo Lee, and Taesup Moon. "Efficient and Robust SEM Image Denoising for Wafer Defect Inspection". *Microscopy and Microanalysis*.
- Yong Jin Jeong and Taesup Moon. "Physics-Informed Fine-Tuning for Physics Discovery from Random and Sparse Data". *Engineering Applications of Artificial Intelligence*.
- Taeeon Park, Sangwon Jung, Taesup Moon. "FairDRO: Group Fairness Regularization via Classwise Robust Optimization". *Neural Networks*.
- Sumin Yu, Taesup Moon. "SP-Guard: Selective Prompt-adaptive Guidance for Safe Text-to-Image Generation". *ECAI Workshop*.
- Sumin Yu, Hyungwoon Bae, and Taesup Moon. "Revisiting VLLM Safety Evaluation: Disentangling Benign Grounding from True Safety Failures in VLLMs". *ICCV Workshop*.
- Hongjoon Ahn, Jinu Hyeon, Hyeonseop Shin, Taesup Moon. "Revisiting Warm-Start Training: No Generalization Loss under Standard Training Schemes". *NeurIPS Workshop*.

**2024**

- Sungmin Cha, Naeun Ko, Heewong Choi, Youngjoon Yoo, Taesup Moon. "NCIS: Neural Contextual Iterative Smoothing for Purifying Adversarial Perturbations". *WACV*.
- Sungmin Cha, Sungjun Cho, Dasol Hwang, Honglak Lee, Taesup Moon, Moontae Lee. "Learning to Unlearn: Instance-wise Unlearning for Pre-trained Classifiers". *AAAI*.
- Donggyu Lee, Sangwon Jung, Taesup Moon. "Continual Learning in the Presence of Spurious Correlations: Analyses and a Simple Baseline". *ICLR*.
- Jaeseok Byun, Dohoon Kim, Taesup Moon. "MAFA: Managing False Negatives for Vision-Language Pre-training". *CVPR*.
- Sungmin Cha, Kyunghyun Cho, Taesup Moon. "Regularizing with Pseudo-Negatives for Continual Self-Supervised Learning". *ICML*.
- Heewoong Choi, Sangwon Jung, Hongjoon Ahn, Taesup Moon. "Listwise Reward Estimation for Offline Preference-based Reinforcement Learning". *ICML*.
- Jihwan Kwak, Sungmin Cha, Taesup Moon. "Towards Realistic Incremental Scenario in Class Incremental Semantic Segmentation". *CoLLAs*.
- Sungmin Cha, Jihwan Kwak, Dongsub Shim, Hyunwoo Kim, Moontae Lee, Honglak Lee, Taesup Moon. "Towards More Diverse Evaluation of Class Incremental Learning: Representation Learning Perspective". *CoLLAs*.
- Sangwon Jung, Sumin Yu, Sanghyuk Chun, Taesup Moon. "Do Counterfactually Fair Image Classifiers Satisfy Group Fairness? – A Theoretical and Empirical Study". *NeurIPS*.
- Sunghwan Joo, Taesup Moon. "Debiased Learning via Composed Conceptual Sensitivity Regularization". *IEEE Access*.
- Sangwon Jung, Claudio Mayrink Verdun, Alex Oesterling, Sajani Vithana, Taesup Moon, Flavio du Pin Calmon. "Measuring Representational Harms in Image Generation with a Multi-Group Proportional Metric". *NeurIPS Workshop*.

**2023**

- Sunghwan Joo, SeokHyeon Jeong, Juyeon Heo, Adrian Weller, Taesup Moon. "Towards More Robust Interpretation via Local Gradient Alignment". *AAAI*.
- Sangwon Jung, Taeeon Park, Sanghyuk Chun, Taesup Moon. "Re-weighting Based Group Fairness Regularization via Classwise Robust Optimization". *ICLR*.
- Sungmin Cha, Sungjun Cho, Dasol Hwang, Sunwon Hong, Moontae Lee, Taesup Moon. "Rebalancing Batch Normalization for Exemplar-based Class-Incremental Learning". *CVPR*.
- Peter Yongho Kim, Junbeom Kwon, Sunghwan Joo, Sangyoon Bae, Donggyu Lee, Yoonho Jung, Shinjae Yoo, Jiook Cha, Taesup Moon. "SwiFT: Swin 4D fMRI Transformer". *NeurIPS*.
- Joonhyun Jeong, Sungmin Cha, Jongwon Choi, Sangdoo Yun, Taesup Moon, Youngjoon Yoo. "Observations on K-Image Expansion of Image-Mixing Augmentation". *IEEE Access*.
- Donggyu Lee, Sangwon Jung, and Taesup Moon. "Issues for Continual Learning in the Presence of Dataset Bias". *AAAI Bridge*.
- Sungmin Cha, Jihwan Kwak, Dongsub Shim, Hyunwoo Kim, Moontae Lee, Honglak Lee, Taesup Moon. "Towards More Objective Evaluation of Class Incremental Learning: Representation Learning Perspective". *CVPR Workshop*.

**2022**

- Sangwon Jung, Sanghyuk Chun, and Taesup Moon. "Learning Fair Classifiers with Partially Annotated Group Labels". *CVPR*.
- Jaeseok Byun, Taebaek Hwang, Jianlong Fu, and Taesup Moon. "GRIT-VLP: Grouped Mini-batch Sampling for Efficient Vision and Language Pre-training". *ECCV*.
- Hongjoon Ahn, Youngyi Yang, Quan Gan, David Wipf, Taesup Moon. "Descent Steps of a Relation-Aware Energy Produce Heterogeneous Graph Neural Networks". *NeurIPS*.
- Taeeon Park, Jihwan Kwak, Hongjoon Ahn, Jinwoong Lee, Jaehyuk Lim, Sangho Yu, Changhwan Shin, and Taesup Moon. "GAN-Based Framework for Unified Estimation of Process-Induced Random Variation in FinFET". *IEEE Access*.
- Sungmin Cha, Soonwon Hong, Moontae Lee, and Taesup Moon. "Task-Balanced Batch Normalization for Exemplar-based Class-Incremental Learning". *CVPR Workshop*.

**2021**

- Sungmin Cha, Taeeon Park, Byeongjoon Kim, Jongduk Baek, Taesup Moon. "GAN2GAN: Generative noise learning for blind image denoising with single noisy images". *ICLR*.
- Sungmin Cha, Hsiang Hsu, Taebaek Hwang, Flavio P. Calmon, Taesup Moon. "CPR: Classifier-Projection Regularization for Continual Learning". *ICLR*.
- Jaeseok Byun, Sungmin Cha, Taesup Moon. "FBI-Denoiser: Fast Blind Image Denoiser for Poisson-Gaussian Noise". *CVPR*.
- Sangwon Jung, Donggyu Lee, Taeeon Park, Taesup Moon. "Fair Feature Distillation for Visual Recognition". *CVPR*.
- Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, Taesup Moon. "SS-IL: Separated Softmax for Incremental Learning". *ICCV*.
- Sungmin Cha, Beomyoung Kim, Youngjoon Yoo, Taesup Moon. "SSUL: Semantic Segmentation with Unknown Label for Exemplar-based Class-Incremental Learning". *NeurIPS*.
- Jinwoong Lee, Taeeon Park, Hongjoon Ahn, Jihwan Kwak, Taesup Moon, Changhwan Shin. "Prediction Model for Random Variation in FinFET Induced by Line-Edge-Roughness (LER)". *Electronics*.
- Donggyu Lee, Hyeongmin Park, Taesup Moon, Youngwook Kim. "Continual Learning of Micro-Doppler Signatures based Human Activity Classification". *IEEE Geoscience and Remote Sensing Letters*.

## 과제

게시된 기간이 2021-10-22–2026-10-22와 겹치는 과제다. 책임·참여와 지원기관은 누리집 표기다. 2021년에 시작한 과제에는 교수의 이전 소속 시기가 포함될 수 있다.[^research][^prof]

- 범용 인공지능 에이전트를 위한 멀티모달 구성적 추론 연구 (지원 한국연구재단 (NRF) 글로벌기초연구실 (BRL); 역할 책임; 기간 25.6~28.5)
- 실용적 제약이 있는 데이터와 환경을 다루는 새로운 연속 학습 알고리즘 연구 (지원 한국연구재단 (NRF) 중견연구자지원사업; 역할 책임; 기간 21.3~26.2)
- 지속 가능한 협업형 멀티 모달 평생 학습 프레임워크 개발 (지원 정보통신기획평가원 (IITP); 역할 참여; 기간 22.4~26.12)
- 의사결정 지원을 위한 퓨샷 학습 기반 시각 및 언어에 대한 인과관계 추론기술개발 (지원 정보통신기획평가원 (IITP); 역할 참여; 기간 22.4~26.12)
- Pre-training large-scale multi-modal model (지원 IITP-MSRA; 기간 2021-2022)

## 수상과 선정

2021-10-22–2026-10-22에 날짜가 있는 수상·선정이다.[^home][^qif]

- 2026-08-28 · Jaeseok Byun, 서울대학교 전기·정보공학부 Distinguished Dissertation Award
- 2026-08-26 · Dohoon Kim, 2026 Yulchon AI Star Scholarship 선정
- 2025-11-27 · 김도훈 박사과정, Qualcomm Innovation Fellowship Korea 2025 Winner 선정

## 연구 소식

날짜가 2021-10-22–2026-10-22에 드는 논문 채택·발표와 과제 승인 소식이다.[^news][^home]

- 2026-09-07 · Sumin Yu의 AIES 2026 논문이 Oral 발표 논문으로 선정되고 서울대와 언론에 소개됨
- 2026-08-20 · PopResume와 Axis-LoRA, EMNLP 2026 Main Track 채택
- 2026-08-12 · Yong Jin Jeong의 논문, Applied Soft Computing Journal 채택
- 2026-07-17 · Sumin Yu의 논문, AIES 2026 채택
- 2026-05-01 · Jinu Hyeon·Woobin Park·Hongjoon Ahn 참여 논문, ICML 2026 채택
- 2026-04-07 · Junho와 Dohoon 참여 논문, ACL 2026 채택 및 Oral 발표 선정
- 2025-06-26 · Jaeseok Byun·SeokHyun Jeong 참여 논문 두 편, ICCV 2025 채택
- 2025-05-28 · 3년 BRL(글로벌기초연구실) 과제 「Multimodal Compositional Reasoning for General-Purpose AI Agent」 선정
- 2025-05-15 · Dohoon Kim 참여 논문 한 편, ACL 2025 채택
- 2025-03-05 · 논문 한 편, ICLR Workshop on Weight Space Learning 채택
- 2025-03-02 · Juhyun·SeokHyun 참여 논문 한 편, WACV 2025 발표
- 2025-02-26 · Sangwon 참여 논문 한 편, CVPR 2025 채택
- 2025-01-22 · Hongjoon·Jinu 참여 논문 한 편, ICLR 2025 채택

## 연락과 위치

- 교수 연구실: 서울특별시 관악구 관악로 1 서울대학교 301동 707호.[^prof][^pi]
- 교수 전화: 02-880-7297.[^prof]
- 연구실 전화: 880-8369(학과 연구실 안내 표기).[^lab]

## 각주
[^home]: 연구실 누리집(Notion 공개 사이트), 첫 화면의 연구 소개·최근 소식. <https://mindlab-snu.notion.site/> (관측 2026-10-26).
[^research]: 연구실 누리집(Notion 공개 사이트), Research의 Adaptive ML·Trustworthy ML·Data Science Applications 및 Projects. <https://mindlab-snu.notion.site/research-page> (관측 2026-10-26).
[^prof]: 서울대학교 전기·정보공학부 문태섭 교수 소개, 직위·학력·경력·전공·연구 분야·연락처. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p870> (관측 2026-10-26).
[^pi]: 연구실 누리집(Notion 공개 사이트), Taesup Moon, Ph.D 소개. <https://mindlab-snu.notion.site/taesup-moon> (관측 2026-10-26).
[^lab]: 서울대학교 전기·정보공학부, 기계지능 및 데이터사이언스 연구실 안내. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=37> (관측 2026-10-26).
[^members]: 연구실 누리집(Notion 공개 사이트), Current Members 보기. <https://mindlab-snu.notion.site/member-page?v=1b83765631c2809384d5000cea71292b> (관측 2026-10-26).
[^alumni]: 연구실 누리집(Notion 공개 사이트), Alumni 보기. <https://mindlab-snu.notion.site/member-page?v=1b83765631c28060ab06000c08a7c2d1> (관측 2026-10-26).
[^pubs]: 연구실 누리집(Notion 공개 사이트), Research에 있는 Publications와 별도 Publications의 By Year 보기. <https://mindlab-snu.notion.site/research-page> <https://mindlab-snu.notion.site/p/1b83765631c280b1b98ff6dae9d36d01> (관측 2026-10-26).
[^news]: 연구실 누리집(Notion 공개 사이트), News의 2025년 날짜 있는 항목. <https://mindlab-snu.notion.site/news-page> (관측 2026-10-26).
[^qif]: 서울대학교 전기·정보공학부, 김도훈 박사과정 등의 2025 Qualcomm Innovation Fellowship 수상 소식, 게시 2026-01-07, 행사 2025-11-27. <https://ece.snu.ac.kr/ece/news?md=v&bbsidx=57154> (관측 2026-10-26).
[^m1]: 연구실 누리집(Notion 공개 사이트), Taeeon Park 소개. <https://mindlab-snu.notion.site/Taeeon-Park-1b83765631c280dcb164ffdc055853d6?pvs=25> (관측 2026-10-26).
[^m2]: 연구실 누리집(Notion 공개 사이트), Hongjoon Ahn 소개. <https://mindlab-snu.notion.site/Hongjoon-Ahn-1b83765631c2802a86b3c224394abd04?pvs=25> (관측 2026-10-26).
[^m3]: 연구실 누리집(Notion 공개 사이트), Yong Jin Jeong 소개. <https://mindlab-snu.notion.site/Yong-Jin-Jeong-1b83765631c2803ba2e9c4a1eea5629c?pvs=25> (관측 2026-10-26).
[^m4]: 연구실 누리집(Notion 공개 사이트), Jihwan Kwak 소개. <https://mindlab-snu.notion.site/Jihwan-Kwak-1b83765631c2804fb993c03d0df1b90b?pvs=25> (관측 2026-10-26).
[^m5]: 연구실 누리집(Notion 공개 사이트), Dohoon Kim 소개. <https://mindlab-snu.notion.site/Dohoon-Kim-1b83765631c280339161f0a2785a338e?pvs=25> (관측 2026-10-26).
[^m6]: 연구실 누리집(Notion 공개 사이트), Hyunwoong Bae 소개. <https://mindlab-snu.notion.site/Hyunwoong-Bae-1b83765631c280ceabe9c409214af4f7?pvs=25> (관측 2026-10-26).
[^m7]: 연구실 누리집(Notion 공개 사이트), Heewoong Choi 소개. <https://mindlab-snu.notion.site/Heewoong-Choi-1b83765631c2803aa39dc32dd3dfcc3e?pvs=25> (관측 2026-10-26).
[^m8]: 연구실 누리집(Notion 공개 사이트), Juhyeon Park 소개. <https://mindlab-snu.notion.site/Juhyeon-Park-1b83765631c2805fbf5cf20d56cebb94?pvs=25> (관측 2026-10-26).
[^m9]: 연구실 누리집(Notion 공개 사이트), Sumin Yu 소개. <https://mindlab-snu.notion.site/Sumin-Yu-1b83765631c280958c26c839eea9732d?pvs=25> (관측 2026-10-26).
[^m10]: 연구실 누리집(Notion 공개 사이트), Yongho Kim (김용호) 소개. <https://mindlab-snu.notion.site/Yongho-Kim-1b83765631c2805bb6d2d78d4f4cbf5b?pvs=25> (관측 2026-10-26).
[^m11]: 연구실 누리집(Notion 공개 사이트), Jinu Hyeon 소개. <https://mindlab-snu.notion.site/Jinu-Hyeon-1b83765631c2805ba586e187a0607b20?pvs=25> (관측 2026-10-26).
[^m12]: 연구실 누리집(Notion 공개 사이트), Jisu Han 소개. <https://mindlab-snu.notion.site/Jisu-Han-2383765631c280e1a1f1c6cd04c3a777?pvs=25> (관측 2026-10-26).
[^m13]: 연구실 누리집(Notion 공개 사이트), Jung Yoon Hwang 소개. <https://mindlab-snu.notion.site/Jung-Yoon-Hwang-1b83765631c280889036ce432f6bc8ec?pvs=25> (관측 2026-10-26).
[^m14]: 연구실 누리집(Notion 공개 사이트), Yoseop Jeong 소개. <https://mindlab-snu.notion.site/Yoseop-Jeong-3263765631c2806d8deccdee37989609?pvs=25> (관측 2026-10-26).
[^m15]: 연구실 누리집(Notion 공개 사이트), Joonyoung Chang 소개. <https://mindlab-snu.notion.site/Joonyoung-Chang-3263765631c280429cb9c6e0ca960934?pvs=25> (관측 2026-10-26).
[^m16]: 연구실 누리집(Notion 공개 사이트), Yeonwoo Kim 소개. <https://mindlab-snu.notion.site/Yeonwoo-Kim-3ca3765631c280d681b0f088600f7f58?pvs=25> (관측 2026-10-26).
[^m17]: 연구실 누리집(Notion 공개 사이트), Seyoon Kim 소개. <https://mindlab-snu.notion.site/Seyoon-Kim-3263765631c280729184df1d362f3d5c?pvs=25> (관측 2026-10-26).
[^m18]: 연구실 누리집(Notion 공개 사이트), Changmin Lee 소개. <https://mindlab-snu.notion.site/Changmin-Lee-3263765631c280909da0e240d3bd7eb4?pvs=25> (관측 2026-10-26).
[^m19]: 연구실 누리집(Notion 공개 사이트), Hoyoung Kim 소개. <https://mindlab-snu.notion.site/Hoyoung-Kim-3263765631c280db8ac0f3cf7c4891f2?pvs=25> (관측 2026-10-26).
[^m20]: 연구실 누리집(Notion 공개 사이트), Yu En Yeoh 소개. <https://mindlab-snu.notion.site/Yu-En-Yeoh-3263765631c28091a6e1e460b2e047a9?pvs=25> (관측 2026-10-26).
[^a1]: 연구실 누리집(Notion 공개 사이트), Jaeseok Byun 소개. <https://mindlab-snu.notion.site/Jaeseok-Byun-Ph-D-1b83765631c280f2a412f9b037b25385?pvs=25> (관측 2026-10-26).
[^a2]: 연구실 누리집(Notion 공개 사이트), Donggyu Lee 소개. <https://mindlab-snu.notion.site/Donggyu-Lee-Ph-D-1b83765631c280378d04ed185e46f138?pvs=25> (관측 2026-10-26).
[^a3]: 연구실 누리집(Notion 공개 사이트), Sunghwan Joo 소개. <https://mindlab-snu.notion.site/Sunghwan-Joo-Ph-D-1b83765631c280d2b162eefea341e8cd?pvs=25> (관측 2026-10-26).
[^a4]: 연구실 누리집(Notion 공개 사이트), Sangwon Jung 소개. <https://mindlab-snu.notion.site/Sangwon-Jung-Ph-D-1b83765631c2803f9729e541c0653d9b?pvs=25> (관측 2026-10-26).
[^a5]: 연구실 누리집(Notion 공개 사이트), Sungmin Cha 소개. <https://mindlab-snu.notion.site/Sungmin-Cha-Ph-D-1b83765631c28015b0aaf882b61774d5?pvs=25> (관측 2026-10-26).
[^a6]: 연구실 누리집(Notion 공개 사이트), Jin Park 소개. <https://mindlab-snu.notion.site/Jin-Park-1b83765631c280d09c07ea21616a6a33?pvs=25> (관측 2026-10-26).
[^a7]: 연구실 누리집(Notion 공개 사이트), SeokHyun Jeong 소개. <https://mindlab-snu.notion.site/SeokHyun-Jeong-1b83765631c280568851cc6fa730803e?pvs=25> (관측 2026-10-26).
[^a8]: 연구실 누리집(Notion 공개 사이트), Dohyun Kim 소개. <https://mindlab-snu.notion.site/Dohyun-Kim-MS-1b83765631c280e1bfe6e45489494511?pvs=25> (관측 2026-10-26).
[^a9]: 연구실 누리집(Notion 공개 사이트), Junha Jeon 소개. <https://mindlab-snu.notion.site/Junha-Jeon-MS-1b83765631c280418a44cdba83173633?pvs=25> (관측 2026-10-26).
[^a10]: 연구실 누리집(Notion 공개 사이트), Juyeon Heo 소개. <https://mindlab-snu.notion.site/Juyeon-Heo-MS-1b83765631c280bcb690e0a65fd4a8a9?pvs=25> (관측 2026-10-26).
[^a11]: 연구실 누리집(Notion 공개 사이트), Hyeongmin Park 소개. <https://mindlab-snu.notion.site/Hyeongmin-Park-MS-1b83765631c280f79931de540899a3c7?pvs=25> (관측 2026-10-26).
[^a12]: 연구실 누리집(Notion 공개 사이트), Yongbee Park 소개. <https://mindlab-snu.notion.site/Yongbee-Park-MS-1b83765631c280b1a36ac7d28c0f8c8a?pvs=25> (관측 2026-10-26).
[^a13]: 연구실 누리집(Notion 공개 사이트), Jungtae Lee 소개. <https://mindlab-snu.notion.site/Jungtae-Lee-MS-1b83765631c280499829c85f084e0ea4?pvs=25> (관측 2026-10-26).
[^a14]: 연구실 누리집(Notion 공개 사이트), Youngeun Seo 소개. <https://mindlab-snu.notion.site/Youngeun-Seo-MS-1b83765631c28067bd04f07087288e4c?pvs=25> (관측 2026-10-26).
[^a15]: 연구실 누리집(Notion 공개 사이트), Byungjoon Kwon 소개. <https://mindlab-snu.notion.site/Byungjoon-Kwon-MS-1b83765631c280bdaf39dcc3aec266d9?pvs=25> (관측 2026-10-26).
[^a16]: 연구실 누리집(Notion 공개 사이트), Jinhee Park 소개. <https://mindlab-snu.notion.site/Jinhee-Park-MS-1b83765631c280e9b20ec5f1351ca9d6?pvs=25> (관측 2026-10-26).
[^p1]: S. Cha, K. Cho, T. Moon, Proceedings of the 41st International Conference on Machine Learning 235, 6048–6065 (2024). <https://proceedings.mlr.press/v235/cha24a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/cha24a.html>.
[^p2]: H. Choi, S. Jung, H. Ahn, T. Moon, Proceedings of the 41st International Conference on Machine Learning 235, 8651–8671 (2024). <https://proceedings.mlr.press/v235/choi24b.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/choi24b.html>.
[^p3]: D. Kim, D. Kang, T. Moon, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 14581–14602 (2025). <https://doi.org/10.18653/v1/2025.acl-long.710> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://aclanthology.org/2025.acl-long.710/>.
[^p4]: J. Byun, T. Hwang, J. Fu, T. Moon, arXiv 사전 공개본 (온라인 2022-08-08). <https://doi.org/10.48550/arXiv.2208.04060> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2208.04060>.
[^p5]: S. Jung, T. Park, S. Chun, T. Moon, arXiv 사전 공개본 (온라인 2023-03-01). <https://doi.org/10.48550/arXiv.2303.00442> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2303.00442>.
[^p6]: S. Joo 외, T. Moon, arXiv 사전 공개본 (AAAI 2023 채택 표기) (온라인 2022-11-29). <https://doi.org/10.48550/arXiv.2211.15900> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2211.15900>.
[^p7]: P. Y. Kim 외, T. Moon, arXiv 사전 공개본 (CVPR 2026 표기) (온라인 2026-04-04). <https://doi.org/10.48550/arXiv.2604.03619> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2604.03619>.
[^p8]: J. Park 외, T. Moon, arXiv 사전 공개본 v3 (ICLR 2026 표기) (온라인 2025-03-09). <https://doi.org/10.48550/arXiv.2503.06437> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2503.06437>.

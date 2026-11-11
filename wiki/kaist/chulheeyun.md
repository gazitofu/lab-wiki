# Optimization & Machine Learning (OptiML) Laboratory

**KAIST 김재철AI대학원 · 윤철희 부교수**

- 분야: 기계학습 이론, 딥러닝 이론, 최적화[^home]
- 대분야: 컴퓨팅·AI, 수학·통계
- 태그: 수리 최적화·최적화 알고리즘[^home], 기계학습 이론·알고리즘[^home][^p5][^p7]
- 홈페이지: <https://chulheeyun.github.io>
- 근거와 출처: [Optimization & Machine Learning (OptiML) Laboratory 근거 페이지](chulheeyun-sources.md)

> 학습 알고리즘이 어떤 답을 찾고 어떤 정보를 배우는지 수학적으로 설명하며, 그 원리에 기반한 학습 방법을 만드는 연구실이다.

## 무엇을 연구하나

OptiML은 기계학습(자료에서 규칙을 배워 예측이나 판단에 사용하는 방법)의 이론과 최적화(주어진 조건에서 목표 수치를 가장 작거나 크게 만드는 값을 찾는 계산)를 연구한다.[^home] 신경망은 연결된 계산 단위들이 입력을 변환해 출력을 만드는 모형이며, 딥러닝은 여러 층의 신경망으로 자료의 표현을 단계적으로 배우는 분야다. 연구실은 이런 신경망을 학습시킬 때 수학적 이론과 신경망 학습의 실제 행동 사이의 간극을 메우고, 원리에 근거한 알고리즘(문제를 풀기 위한 계산 절차)을 개발하는 것을 목표로 한다.[^home]

한 갈래는 최적화 방법이 언제 원하는 답에 가까워지는지 따지는 연구다. 기울기 하강법(각 변수에 대한 함수의 변화율을 이용해 함수값을 줄이는 쪽으로 변수를 바꾸는 계산)의 변형을 분석한다. Sharpness-Aware Minimization(SAM)은 현재 위치 주변의 변화를 살핀 뒤 갱신하는 학습 방법이다. 대표 논문 3은 주변을 살피는 범위를 일정하게 유지하고 변화 방향의 크기를 일정하게 맞추는 실제 설정에서, 확률적으로 자료를 이용하는 SAM이 최적값 근처에만 머물 수 있음을 보였다. 대표 논문 4는 한쪽이 값을 줄이고 다른 쪽이 값을 키우는 최소최대 문제에서, 자료 순서를 섞는 방식만으로는 학습이 불안정할 수 있음을 분석하고 보정을 더한 방법을 제안했다.[^p3][^p4]

학습이 진행되는 경로 자체도 연구 대상이다. 대표 논문 5는 시작값이 다른 학습 경로들이 적절히 다시 표현하면 같은 구조에 정렬되는 현상을 관찰하고, 자료 한 개로 학습한 단순한 신경망 모형에서 이를 증명했다. 대표 논문 1은 선형 대각 신경망(입력 좌표별 연결로 이루어지고 층 사이에 비선형 변환을 넣지 않는 신경망)을 분석했다. 특정 SAM 설정에서 학습 초반에는 작은 입력 좌표에 의존하다가 학습이 진행되면 큰 좌표로 옮겨 가는 현상을 밝히고, 그 원인을 분석했다.[^p5][^p1]

자료에서 무엇을 기억하는지도 다룬다. 대표 논문 6은 자료의 분포(자료값별 발생 가능성을 나타내는 방식)가 변하지 않는 상황에서, 이미 배운 가중치(신경망 안 연결의 영향력을 정하는 값)를 새 학습의 시작값으로 쓰는 경우를 분석했다. 잡음(관심 있는 규칙과 무관한 자료의 변동)을 외운 것이 새 정보를 배우는 능력을 떨어뜨리는 주요 원인임을 밝히고, 배운 특징(자료를 구별하거나 예측하는 데 쓰이는 속성)을 보존하면서 기억한 잡음을 선택적으로 줄이는 방법을 제안했다. 대표 논문 7은 자료 증강(기존 자료를 변형하거나 조합해 학습 자료를 만드는 방법)이 드물게 나타나는 특징의 학습에 미치는 영향을 수학적으로 분석했다.[^p6][^p7]

문자열을 다루는 모형과 그 학습 방식도 연구한다. Transformer(입력의 각 부분 사이 관계에 따라 정보를 결합하는 신경망 구조)에 산술 과제의 자릿수 관계를 반영한 대표 논문 8은, 학습 때보다 긴 덧셈을 처리하는 방법을 제안했다. 대표 논문 2는 언어 모델(앞뒤 말의 관계를 배워 글을 처리하거나 만드는 모형)을 학습시킬 때 학습률(학습할 값을 한 번에 바꾸는 정도)을 미리 줄이는 일정 없이 작동하는 방법을 분석하고, 추가 저장 공간 없이 가중치를 평균하는 효과가 나타남을 보였다.[^p8][^p2]

## 주요 연구 주제

### 최적화 알고리즘의 수렴과 한계

실제 학습 설정에서 원하는 답에 가까워질 수 있는지, 계산을 반복해도 남는 오차가 있는지를 분석한다. 최소최대 문제에서는 자료를 처리하는 순서와 보정을 결합한 새로운 계산 방법도 개발한다.[^p3][^p4]

### 학습 경로와 암묵적 편향

암묵적 편향은 학습 목표에 명시하지 않아도 학습 방법이나 모형 구조 때문에 특정한 답을 선호하는 성질이다. 서로 다른 시작값에서 나온 학습 경로가 공유하는 구조와, 신경망 깊이에 따라 배우는 입력 좌표의 순서가 달라지는 현상을 분석한다.[^p5][^p1]

### 특징 학습과 일반화

일반화는 학습에 쓰지 않은 자료에서도 배운 규칙이 작동하는 성질이다. 기존 학습 결과를 이어 쓰면서 새 정보를 배우는 능력을 유지하는 방법과, 자료 증강이 희귀한 특징의 학습을 바꾸는 원리를 연구한다.[^p6][^p7]

### 언어 모델의 학습과 과제 구조

산술 과제에 필요한 입력 간 관계를 모형에 반영하고, 언어 모델의 학습을 지속적으로 늘려 가는 상황에 맞는 학습 방법을 분석한다.[^p8][^p2]

## 대표 논문

KAIST 재직 시기인 2023–2026년 논문에서 최적화, 학습 경로, 특징 학습, 언어 모델을 다루는 8편을 골랐다. 「쉽게 말하면」은 각 논문 페이지에 게시된 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 · 발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2026 | [Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization](https://chulheeyun.github.io/publication/moon2026minor/) · ICLR 2026[^p1] | 1저자 Chaewon Moon · 윤철희 공저 | 선형 대각 신경망에서 SAM의 설정과 깊이에 따라 학습 방향이 달라짐을 분석했다. 특정 설정에서는 작은 입력 좌표를 먼저 이용하다가 큰 좌표로 옮겨 가는 현상을 설명한다. |
| 2 | 2025 | [Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training](https://doi.org/10.52202/085713-4248) · NeurIPS 2025[^p2] | 1저자 Minhak Song·Beomhan Baek(누리집 공동 기여 표기) · 윤철희 공저 | 학습률 감소 일정을 미리 정하지 않는 방법이 추가 저장 공간 없이 가중치를 평균하는 효과를 냄을 분석했다. 이전 갱신 방향을 이어받는 설정의 변화에 대한 안정성과 큰 묶음 자료에서의 성능을 개선한 변형을 제안했다. |
| 3 | 2023 | [Practical Sharpness-Aware Minimization Cannot Converge All the Way to Optima](https://doi.org/10.52202/075280-1140) · NeurIPS 2023 (Spotlight)[^p3] | 1저자 Dongkuk Si · 윤철희 공저 | 주변을 살피는 범위를 줄이지 않는 실제 SAM 설정을 분석했다. 연구에서 다룬 확률적 설정에서는 최적값에 가까워져도 없애기 어려운 오차가 남을 수 있음을 보였다. |
| 4 | 2024 | [Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements](https://doi.org/10.52202/079017-3932) · NeurIPS 2024[^p4] | 1저자 Jiseok Chae · 윤철희 공저 | 최소최대 문제에서 자료 순서를 섞는 것만으로는 계산이 답에서 멀어질 수 있음을 보였다. 순서 섞기와 추가 보정을 결합해 답에 가까워지는 방법을 제안했다. |
| 5 | 2023 | [Trajectory Alignment: Understanding the Edge of Stability Phenomenon via Bifurcation Theory](https://doi.org/10.52202/075280-3137) · NeurIPS 2023[^p5] | 1저자 Minhak Song · 윤철희 공저 | 시작값이 다른 학습 경로를 적절히 다시 표현하면 같은 구조에 정렬되는 현상을 관찰했다. 자료 한 개로 학습한 단순한 선형·비선형 신경망에서 이를 증명해 학습이 불안정해지는 경계(Edge of Stability)에 가까워지는 현상을 설명했다. |
| 6 | 2024 | [DASH: Warm-Starting Neural Network Training in Stationary Settings without Loss of Plasticity](https://doi.org/10.52202/079017-1372) · NeurIPS 2024[^p6] | Baekrok Shin·Junsoo Oh(누리집 공동 기여 표기) · 윤철희 공저 | 자료 분포가 변하지 않는 상황에서, 이미 학습한 가중치를 이어 쓸 때 잡음 기억이 새 정보를 배우는 능력을 떨어뜨리는 원인임을 분석했다. 배운 특징을 남기고 잡음 기억을 줄이는 Direction-Aware SHrinking(DASH)을 제안해 영상 과제에서 평가했다. |
| 7 | 2024 | [Provable Benefit of Cutout and CutMix for Feature Learning](https://doi.org/10.52202/079017-3641) · NeurIPS 2024 (Spotlight)[^p7] | 1저자 Junsoo Oh · 윤철희 공저 | 특정 자료 모형과 두 층 신경망에서, Cutout은 증강 없는 학습이 놓치는 희귀한 특징을 배우고 CutMix는 그보다 드문 특징도 배울 수 있음을 증명했다. |
| 8 | 2024 | [Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure](https://doi.org/10.52202/079017-0701) · NeurIPS 2024[^p8] | 1저자 Hanseul Cho·Jaeyoung Cha(누리집 공동 기여 표기) · 윤철희 공저 | 관련 있는 입력 부분에 같은 위치 표시를 주는 방법을 제안했다. 덧셈에서는 같은 자릿수의 숫자를 연결하며, 학습 범위를 넘는 길이의 덧셈 처리와 단순한 모형에서의 이론적 성질을 보였다. |

## 교수와 전문 분야

윤철희는 KAIST 김재철AI대학원 부교수이며 OptiML을 이끈다. 교수 소개는 기계학습·딥러닝의 이론과 최적화를 연구 관심으로 제시한다. 최근 논문에서는 최적화 방법의 한계와 학습 경로의 구조, 특징을 배우는 원리를 중심으로 전문 분야가 드러난다.[^faculty][^home][^p3][^p5][^p7]

KAIST 전기공학(Electrical Engineering) 학사 과정을 2007–2014년, Stanford University 전기공학 석사 과정을 2014–2016년, Massachusetts Institute of Technology 전기공학·컴퓨터과학 박사 과정을 2016–2021년에 마쳤다. 박사 과정에서는 Suvrit Sra와 Ali Jadbabaie의 공동 지도를 받았다.[^home]

## 응용 분야

영상 과제에서의 학습 정확도와 학습 효율, 새 자료가 들어올 때 기존 학습 결과를 이어 쓰는 방법, 언어 모델 학습, 산술 과제를 처리하는 신경망에 연구를 연결한다.[^p6][^p7][^p2][^p8]

## 구성원

Research Group에 게시된 구성원 18명이다. 과정 구획은 원문 표기를 유지했으며 박사·석박사통합 구획과 석사 구획의 학생은 모두 KAIST AI 소속으로 표기되어 있다. 「대표 논문 참여」는 전체 저자 목록에서 같은 이름의 저자를 같은 사람으로 보아 표시했다. 관측일은 2026-11-09다.[^home]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Yoonsoo Nam | Postdocs/InnoCORE Fellows (PhD) |  |
| Jaeyoung Cha | PhD and MS/PhD Students | 8 |
| Hanseul Cho | PhD and MS/PhD Students | 6, 8 |
| Changmin Kang | PhD and MS/PhD Students |  |
| Donghwa Kim | PhD and MS/PhD Students |  |
| Yujun Kim | PhD and MS/PhD Students |  |
| Junghyun Lee | PhD and MS/PhD Students (co-advised with Prof. Se-Young Yun) |  |
| Junsoo Oh | PhD and MS/PhD Students | 6, 7 |
| Baekrok Shin | PhD and MS/PhD Students | 6 |
| Jueun Kim | Master’s Students |  |
| Myeongkyu Lee | Master’s Students |  |
| Chaewon Moon | Master’s Students | 1 |
| Jerry Song | Master’s Students |  |
| Youngjun Song | Master’s Students |  |
| Daehan Yoon | Master’s Students |  |
| Huiwone Kim | Undergraduate Students/KAIRI Interns (SNU ECE) |  |
| Jihwan Kim | Undergraduate Students/KAIRI Interns (SNU Math/CS) |  |
| Yelynn Suh | Undergraduate Students/KAIRI Interns (KAIST EE) |  |

## 졸업생·이전 인턴

Research Group의 Former Graduate Students/Notable Former Interns 구획에 게시된 9명이다. 학위·과정과 연월·기간은 원문 표기다.[^home]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Yeseul Cho | MSc (Aug 2026) |  |
| Geonhui Yoo | MSc (Aug 2025) |  |
| Jaewook Lee | MSc (Feb 2025) |  |
| Dongkuk Si | MSc (Feb 2024) |  |
| Beomhan Baek | KAIRI (Jul 2024–Aug 2026) |  |
| Minhak Song | Intern (Feb 2022–Aug 2026) |  |
| Minseop Shin | KAIRI (Jan 2025–Feb 2026) |  |
| Hyunji Jung | KAIRI (Jul 2023–Sep 2024) |  |
| Prin Phunyaphibarn | KAIRI (Jan 2023–Feb 2024) |  |

## 최근 5년 논문 목록

교수 개인 Publications 목록의 2022–2026년 표기 46편이다. 개인 목록으로, 2022년 1월 말 KAIST 부임 전 연구한 논문도 포함한다. 연도는 목록 끝의 게시 연도이며 학회 연도와 다를 수 있다. NeurIPS 2026 본 학회 6편은 「채택」, 해당 학회 워크숍 7편은 공지에 따라 「발표 예정, 연구실 기재」로 표시했다. arXiv preprint는 사전 공개 논문이다.[^pubs][^news1][^news4]

**2026**

- Jaewook Lee, Ernest K. Ryu, Chulhee Yun. "Nesterov Acceleration with Operator Decomposition". *arXiv preprint*.
- Minchan Jung, Hanseul Cho, Chulhee Yun. "Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Jihwan Kim, Dogyoon Song, Chulhee Yun. "From Geometry to Generalization: Why Row Normalization Can Beat Adam and Muon". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Chulhee Yun, Ananda Theertha Suresh. "Beyond Loss Gaps: Stability and Geometry in Dynamic Sample Reweighting". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Yujun Kim, Jaeyoung Cha, Chulhee Yun. "The Phase Transition in Random Reshuffling: Tight Rates under Strong Convexity". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Chaewon Moon, Yeseul Cho, Chulhee Yun. "Machine Unlearning with a Destination: Tracking a Minimizer Path to the Retain-Only Objective". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Donghwa Kim, Chulhee Yun. "Beyond Rate Optimality: How Polyak’s Momentum Shapes Non-Convex Optimization". *NeurIPS 2026 Workshop on Optimization for Machine Learning (OPT 2026)*. (발표 예정, 연구실 기재)
- Minseop Shin, Jaeyoung Cha, Chulhee Yun. "In-Context Learning of Hidden Markov Models by Loop Transformers". *NeurIPS 2026 Workshop on AI for Stochastic Dynamics (STODY)*. (발표 예정, 연구실 기재)
- Jueun Kim, Baekrok Shin, Jihun Yun, Beomhan Baek, Minhak Song, Chulhee Yun. "AMUSE: Anytime Muon with Stable Gradient Evaluation". *NeurIPS 2026 (Spotlight)*. (채택)
- Changmin Kang, Jihun Yun, Baekrok Shin, Yeseul Cho, Chulhee Yun. "Uniform Spectral Growth under Factor-wise Gradient Orthogonalization in Matrix Factorization". *NeurIPS 2026*. (채택)
- Yeseul Cho, Baekrok Shin, Changmin Kang, Chulhee Yun. "Label-Efficient Dataset Pruning via Semi-Supervised Pseudo-Labeling". *NeurIPS 2026*. (채택)
- Daehan Yoon, Chulhee Yun. "Transformers Can Learn Multiclass Classification In-Context: Isotropy Governs Generalization". *NeurIPS 2026*. (채택)
- Junghyun Lee, Yujun Kim, Chulhee Yun, Se-Young Yun. "Looking Through the Mirror: Minimax-Optimal Regularized Regrets in Online Learning and Bandits". *NeurIPS 2026*. (채택)
- Junghyun Lee, Minju Hong, Kwang-Sung Jun, Chulhee Yun, Se-Young Yun. "Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences". *NeurIPS 2026*. (채택)
- Jaeyoung Cha, Hanseul Cho, Chulhee Yun. "Layer Verification Accelerates Speculative Tree Decoding". *ICML 2026 Workshop on Resource-Adaptive Foundation Model Inference (AdaptFM)*.
- Jihwan Kim, Dogyoon Song, Chulhee Yun. "Scaling Laws of SignSGD in Linear Regression: When Does It Outperform SGD?". *ICLR 2026*.
- Chaewon Moon, Dongkuk Si, Chulhee Yun. "Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization". *ICLR 2026*.

**2025**

- Beomhan Baek, Minhak Song, Chulhee Yun. "Implicit Bias of Per-sample Adam on Separable Data: Departure from the Full-batch Regime". *ICLR 2026*.
- Baekrok Shin, Chulhee Yun. "Implicit Bias and Loss of Plasticity in Matrix Completion: Depth Promotes Low-Rankness". *ICLR 2026*.
- Yujun Kim, Chaewon Moon, Chulhee Yun. "The Cost of Robustness: Tighter Bounds on Parameter Complexity for Robust Memorization in ReLU Nets". *NeurIPS 2025*. [DOI](https://doi.org/10.52202/085713-5380)
- Junsoo Oh, Jerry Song, Chulhee Yun. "From Linear to Nonlinear: Provable Weak-to-Strong Generalization through Feature Learning". *NeurIPS 2025*. [DOI](https://doi.org/10.52202/085713-5636)
- Minhak Song, Beomhan Baek, Kwangjun Ahn, Chulhee Yun. "Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training". *NeurIPS 2025*. [DOI](https://doi.org/10.52202/085713-4248)
- Donghwa Kim, Jaewook Lee, Chulhee Yun. "Provable Benefit of Random Permutations over Uniform Sampling in Stochastic Coordinate Descent". *ICML 2025*.
- Geonhui Yoo, Minhak Song, Chulhee Yun. "Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More". *ICML 2025*.
- Yujun Kim, Jaeyoung Cha, Chulhee Yun. "Incremental Gradient Descent with Small Epoch Counts is Surprisingly Slow on Ill-Conditioned Problems". *ICML 2025*.
- Yeseul Cho, Baekrok Shin, Changmin Kang, Chulhee Yun. "Lightweight Dataset Pruning without Full Training via Example Difficulty and Prediction Uncertainty". *ICML 2025*.
- Hyunsu Kim, Giung Nam, Chulhee Yun, Hongseok Yang, Juho Lee. "Parameter Expanded Stochastic Gradient Markov Chain Monte Carlo". *ICLR 2025*.
- Hyunji Jung, Hanseul Cho, Chulhee Yun. "Convergence and Implicit Bias of Gradient Descent on Continual Linear Classification". *ICLR 2025*.
- Hanseul Cho, Jaeyoung Cha, Srinadh Bhojanapalli, Chulhee Yun. "Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count". *ICLR 2025*.
- Minhak Song, Kwangjun Ahn, Chulhee Yun. "Does SGD really happen in tiny subspaces?". *ICLR 2025*.

**2024**

- Jiseok Chae, Chulhee Yun, Donghwan Kim. "Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements". *NeurIPS 2024*. [DOI](https://doi.org/10.52202/079017-3932)
- Baekrok Shin, Junsoo Oh, Hanseul Cho, Chulhee Yun. "DASH: Warm-Starting Neural Network Training in Stationary Settings without Loss of Plasticity". *NeurIPS 2024*. [DOI](https://doi.org/10.52202/079017-1372)
- Junsoo Oh, Chulhee Yun. "Provable Benefit of Cutout and CutMix for Feature Learning". *NeurIPS 2024 (Spotlight)*. [DOI](https://doi.org/10.52202/079017-3641)
- Hanseul Cho, Jaeyoung Cha, Pranjal Awasthi, Srinadh Bhojanapalli, Anupam Gupta, Chulhee Yun. "Position Coupling: Improving Length Generalization of Arithmetic Transformers Using Task Structure". *NeurIPS 2024*. [DOI](https://doi.org/10.52202/079017-0701)
- Prin Phunyaphibarn, Junghyun Lee, Bohan Wang, Huishuai Zhang, Chulhee Yun. "Gradient Descent with Polyak's Momentum Finds Flatter Minima via Large Catapults". *ICML 2024 Workshop on High-dimensional Learning Dynamics 2024: The Emergence of Structure and Reasoning*.
- Jaewook Lee, Hanseul Cho, Chulhee Yun. "Fundamental Benefit of Alternating Updates in Minimax Optimization". *ICML 2024 (Spotlight)*.

**2023**

- Kwangjun Ahn, Xiang Cheng, Minhak Song, Chulhee Yun, Ali Jadbabaie, Suvrit Sra. "Linear attention is (maybe) all you need (to understand transformer optimization)". *ICLR 2024*.
- Junghyun Lee, Hanseul Cho, Se-Young Yun, Chulhee Yun. "Fair Streaming Principal Component Analysis: Statistical and Algorithmic Viewpoint". *NeurIPS 2023*.
- Minhak Song, Chulhee Yun. "Trajectory Alignment: Understanding the Edge of Stability Phenomenon via Bifurcation Theory". *NeurIPS 2023*. [DOI](https://doi.org/10.52202/075280-3137)
- Hojoon Lee, Hanseul Cho, Hyunseung Kim, Daehoon Gwak, Joonkee Kim, Jaegul Choo, Se-Young Yun, Chulhee Yun. "PLASTIC: Improving Input and Label Plasticity for Sample Efficient Reinforcement Learning". *NeurIPS 2023*.
- Dongkuk Si, Chulhee Yun. "Practical Sharpness-Aware Minimization Cannot Converge All the Way to Optima". *NeurIPS 2023 (Spotlight)*. [DOI](https://doi.org/10.52202/075280-1140)
- Junsoo Oh, Chulhee Yun. "Provable Benefit of Mixup for Finding Optimal Decision Boundaries". *ICML 2023*.
- Jaeyoung Cha, Jaewook Lee, Chulhee Yun. "Tighter Lower Bounds for Shuffling SGD: Random Permutations and Beyond". *ICML 2023 (Oral)*.
- David X. Wu, Chulhee Yun, Suvrit Sra. "On the Training Instability of Shuffling SGD with Batch Normalization". *ICML 2023*.

**2022**

- Hanseul Cho, Chulhee Yun. "SGDA with shuffling: faster convergence for nonconvex-PŁ minimax optimization". *ICLR 2023*.
- Chulhee Yun, Shashank Rajput, Suvrit Sra. "Minibatch vs Local SGD with Shuffling: Tight Convergence Bounds and Beyond". *ICLR 2022 (Oral)*.

## 수상과 선정

연구실 소개와 소식에서 알린 2022–2026년 수상 8건이다. 교수 개인 수상도 포함한다. 연도만 쓴 2024·2025년 항목은 학회 연도에 붙은 논문 수상 표기이며 날짜는 게시되어 있지 않다.[^home][^news1][^news2][^news3]

- 2026-05-15 · 윤철희 교수, 2026 KSIAM Outstanding Young Investigator Award 수상.
- 2025-02-23 · 윤철희 교수, KAIST Ewon Assistant Professorship 수상. 칭호와 3년 연구 지원이 수반되는 교내 신진교수 상이다.
- 2023-07-13 · 「Practical Sharpness-Aware Minimization Cannot Converge All the Way to Optima」, CKAIA 2023 Outstanding Paper Award 수상.
- 2022-11-16 · 「SGDA with shuffling: faster convergence for nonconvex-PŁ minimax optimization」, JKAIA 2022 NAVER Outstanding Theory Paper Award 수상.
- 2025 · 「The Cost of Robustness: Tighter Bounds on Parameter Complexity for Robust Memorization in ReLU Nets」, CKAIA 2025 KAIA Outstanding Paper Award 수상.
- 2025 · 「From Linear to Nonlinear: Provable Weak-to-Strong Generalization through Feature Learning」, CKAIA 2025 KT Best Paper Award 수상.
- 2024 · 「Convergence and Implicit Bias of Gradient Descent on Continual Linear Classification」, JKAIA 2024 Best Paper Award 수상.
- 2024 · 「Provable Benefit of Cutout and CutMix for Feature Learning」, CKAIA 2024 KT Best Paper Award 수상.

## 소식

교수 개인 News 목록의 2022-01-29–2026-09-30 연구 성과 소식 16건이다. 2022년 1월 말 KAIST 부임 전 연구한 논문의 발표 안내도 포함한다.[^news1][^news2][^news3][^news4]

- 2026-09-30 · NeurIPS 2026 논문 6편 채택. 이 가운데 1편은 Spotlight이며, OPT 워크숍 6편과 STODY 워크숍 1편의 발표 예정도 알렸다.
- 2026-01-27 · ICLR 2026 논문 4편 채택.
- 2025-09-19 · NeurIPS 2025 논문 3편 채택.
- 2025-01-23 · ICLR 2025 논문 4편 채택.
- 2024-09-26 · NeurIPS 2024 논문 4편 채택. Cutout·CutMix 자료 증강의 이론 분석 논문은 Spotlight 발표로 선정됐다.
- 2024-06-19 · ICML 2024 Long-Context Foundation Models 워크숍 1편과 Advancing Neural Network Training 워크숍 1편의 채택·발표 예정 안내.
- 2024-06-17 · ICML 2024 High-dimensional Learning Dynamics 워크숍 논문 3편 채택.
- 2024-05-02 · 최소최대 최적화의 교대 갱신 이점을 다룬 논문이 ICML 2024에 채택됐으며 Spotlight로 선정됐다.
- 2024-03-05 · 교대 기울기 하강·상승법을 분석한 논문이 ICLR 2024 Bridging the Gap Between Practice and Theory in Deep Learning 워크숍에 채택됐다.
- 2024-01-17 · 선형 Transformer의 최적화 특성을 다룬 논문이 ICLR 2024에 채택됐다.
- 2023-10-28 · NeurIPS 2023 Mathematics of Modern Machine Learning 워크숍 논문 2편 채택. 두 논문 모두 구두 발표로 선정됐다.
- 2023-09-22 · NeurIPS 2023 논문 4편 채택. Sharpness-Aware Minimization 분석 논문은 Spotlight로 선정됐다.
- 2023-04-25 · ICML 2023 논문 3편 채택. 이 가운데 1편이 구두 발표로 선정됐다.
- 2023-01-21 · ICLR 2023 논문 1편 채택.
- 2022-10-13 · 자료 순서를 섞는 확률적 기울기 하강·상승법을 분석한 사전 공개 논문 안내.
- 2022-01-29 · 자료 순서를 섞는 연합 최적화 방법 분석 논문의 ICLR 2022 발표 예정 및 구두 발표 선정 안내.

## 연락과 위치

- 기관 전화: +82-2-958-0765.[^home]
- 교수 연구실: KAIST Seoul Campus Building #9, 9401.[^home]
- 교수 이메일: chulhee.yun@kaist.ac.kr[^faculty]
[^home]: Chulhee “Charlie” Yun, Home의 교수 소개·Research Group·연락처·논문별 수상 표기. <https://chulheeyun.github.io> 관측일 2026-11-09.
[^faculty]: KAIST 김재철AI대학원, 구성원 국문 페이지의 전임교수 윤철희 항목. <https://gsai.kaist.ac.kr/people-2/?lang=ko> 관측일 2026-11-09.
[^pubs]: Chulhee “Charlie” Yun, Publications. <https://chulheeyun.github.io/publication/> 관측일 2026-11-09.
[^news1]: Chulhee “Charlie” Yun, News 첫 쪽. <https://chulheeyun.github.io/news/> 관측일 2026-11-09.
[^news2]: Chulhee “Charlie” Yun, News 둘째 쪽. <https://chulheeyun.github.io/news/page/2/> 관측일 2026-11-11.
[^news3]: Chulhee “Charlie” Yun, News 셋째 쪽. <https://chulheeyun.github.io/news/page/3/> 관측일 2026-11-11.
[^news4]: Chulhee “Charlie” Yun, News 넷째 쪽의 ICLR 2022 발표 및 KAIST 부임 안내. <https://chulheeyun.github.io/news/page/4/> 관측일 2026-11-11.
[^p1]: C. Moon, D. Si, C. Yun, International Conference on Learning Representations 2026 (2026). <https://chulheeyun.github.io/publication/moon2026minor/> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/moon2026minor/> 관측일 2026-11-11.
[^p2]: M. Song, B. Baek, K. Ahn, C. Yun, Neural Information Processing Systems 2025 (2025). <https://doi.org/10.52202/085713-4248> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/song2025through/> 관측일 2026-11-11.
[^p3]: D. Si, C. Yun, Neural Information Processing Systems 2023 (Spotlight Presentation) (2023). <https://doi.org/10.52202/075280-1140> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/si2023practical/> 관측일 2026-11-11.
[^p4]: J. Chae, C. Yun, D. Kim, Neural Information Processing Systems 2024 (2024). <https://doi.org/10.52202/079017-3932> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/chae2024stochastic/> 관측일 2026-11-11.
[^p5]: M. Song, C. Yun, Neural Information Processing Systems 2023 (2023). <https://doi.org/10.52202/075280-3137> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/song2023trajectory/> 관측일 2026-11-11.
[^p6]: B. Shin, J. Oh, H. Cho, C. Yun, Neural Information Processing Systems 2024 (2024). <https://doi.org/10.52202/079017-1372> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/shin2024dash/> 관측일 2026-11-11.
[^p7]: J. Oh, C. Yun, Neural Information Processing Systems 2024 (Spotlight Presentation) (2024). <https://doi.org/10.52202/079017-3641> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/oh2024provable/> 관측일 2026-11-11.
[^p8]: H. Cho 외, C. Yun, Neural Information Processing Systems 2024 (2024). <https://doi.org/10.52202/079017-0701> 초록 기준(논문 페이지 게시 초록). 초록 원문 <https://chulheeyun.github.io/publication/cho2024position/> 관측일 2026-11-11.

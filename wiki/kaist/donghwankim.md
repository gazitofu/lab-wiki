# 김동환 교수 연구실

**KAIST 수리과학과 · 김동환 부교수**

- 영문 교수 이름: Donghwan Kim
- 분야: 최적화 이론 및 응용, 최적화와 학습 동역학, 일반화, 생성 모형[^dept][^home]
- 대분야: 수학·통계, 컴퓨팅·AI
- 태그: 수리 최적화·최적화 알고리즘[^p1][^p3]
- 홈페이지: <https://mathsci.kaist.ac.kr/~donghwankim/>
- 근거와 출처: [김동환 교수 연구실 근거 페이지](donghwankim-sources.md)

> 학습 과정에서 값을 어떤 순서와 크기로 바꿔야 원하는 결과에 도달하는지 수학적으로 분석하고, 그 계산 방법을 개발하는 연구실이다.[^p1][^p3][^p4]

## 무엇을 연구하나

김동환 교수 연구실은 최적화(주어진 조건 안에서 목표가 되는 함수의 값을 가장 작게 하거나 가장 크게 만드는 입력을 찾는 일) 알고리즘(문제를 풀기 위한 계산 절차)을 개발한다. 학과가 적은 전문 분야는 최적화 이론 및 응용이다. 함수의 기울기(각 입력 방향으로 함수가 변하는 비율을 모은 값)를 이용하는 일차 방법(함수의 일차 변화 정보까지를 이용하는 반복 계산법)을 중심으로, 계산이 목표에 도달하는 조건과 필요한 계산량을 분석한다.[^dept][^p1][^p2][^p3]

주요 대상은 미니맥스 문제(한쪽 변수의 선택에 대해 다른 쪽 변수가 만들 수 있는 함수의 최댓값을 최소화하는 문제)다. 이때는 단순히 계산이 멈추는 것과 원하는 최적점에 도달하는 것이 다를 수 있다. 연구진은 국소 미니맥스점(주변의 작은 변화 범위에서 최소화와 최대화의 순서를 고려한 최적 조건을 만족하는 점)을 찾는 방법을 연구한다. 추가기울기법(예측 지점에서 기울기를 다시 계산한 뒤 그 정보로 현재 값을 갱신하는 방법)에서 변수의 갱신 순서와 갱신 속도 차이를 바꾸는 연구가 여기에 속한다.[^p3][^p6]

확률적 계산(무작위로 정해지는 정보를 이용하는 계산)에서 수렴(반복 계산이 목표가 되는 값이나 점에 가까워지는 성질)을 보장하는 일도 다룬다. 여러 함수의 합으로 이루어진 미니맥스 문제에서 함수들을 사용하는 순서를 섞는 방법을 분석하고, 반복 계산에 고정된 기준점의 정보를 함께 사용하는 방법을 제안했다. 계산 정보에 오차가 있거나 한 번의 반복에서 요청할 수 있는 계산 횟수가 고정되어 있을 때도 필요한 계산량을 따진다.[^p2][^p4][^p5]

학습률(학습 과정에서 값을 한 번 바꾸는 크기를 정하는 계수)을 어떻게 정할지도 연구 대상이다. Schedule-Free 방법은 학습률을 학습 도중 어떤 일정으로 바꿀지 설계하고 조정하는 부담을 줄이려는 방법이다. 연구진은 이 방법의 최악 조건에서의 수렴 속도를 분석하고, 특정 종류의 안장점에 머무르지 않는 조건을 밝혔다. 여기서 안장점은 기울기가 사라지면서 주변에 함수의 값이 커지는 방향과 작아지는 방향이 함께 있는 점이다.[^p1]

## 주요 연구 주제

### 1. 미니맥스 문제의 해와 갱신 규칙

최소화하는 변수와 최대화하는 변수의 갱신 속도를 다르게 두는 방법을 분석한다. 변수를 번갈아 갱신하는 단계와 두 갱신 속도의 차이를 점차 늘리는 규칙을 결합해, 일정한 조건에서 기존의 두 갱신 속도를 쓰는 방법들이 도달하지 못하는 국소 미니맥스점에도 도달하는 방법을 제안했다. 다른 연구에서는 미니맥스의 국소 최적점만 찾는 일차 방법이 존재하는지를 공개 문제로 제시했다.[^p3][^p6]

### 2. 무작위 계산과 오차를 포함한 반복법

확률적 추가기울기법에서 함수의 순서를 섞는 방식만으로는 계산이 발산(반복 계산한 값이 일정한 값에 가까워지지 않는 현상)할 수 있음을 보이고, 기준점 정보를 함께 쓰는 방법의 수렴을 분석했다. 또한 계산 오차를 허용하는 반복법과 반복당 계산 요청 수를 고정한 방법을 연구한다. 목표는 주어진 정확도에 도달하는 데 필요한 계산량을 줄이고, 달성할 수 있는 계산량의 한계를 밝히는 것이다.[^p2][^p4][^p5]

### 3. 학습 과정의 수학적 분석

학습 동역학(학습 변수가 시간이나 반복에 따라 달라지는 규칙)을 분석해 학습 방법의 작동 조건을 설명한다. Schedule-Free 연구는 시간을 연속된 양으로 놓고 변수의 변화율을 적은 식을 이용해 반복 계산을 분석하고, 수렴 속도와 안장점 회피 조건을 제시한다. 누리집은 현재 관심 분야로 최적화와 학습 동역학 외에도 일반화(학습에 쓰지 않은 자료에도 학습한 규칙이 적용되는 성질), 생성 모형(학습한 자료의 특성을 바탕으로 새 자료를 만들어 내는 모형), 추론과 에이전트(주변 정보를 바탕으로 목표를 위한 행동을 선택하는 주체) 학습을 적는다.[^p1][^home]

## 대표 논문

김동환 교수가 저자로 참여한 2021–2026년 연구 가운데 미니맥스 최적화, 확률적 계산, 학습 과정 분석을 보여 주는 7편이다. 학회 논문집의 논문 3편과 사전 공개본 4편이며, 아래에서 판본과 누리집의 학회 표기를 함께 적었다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Understanding Schedule-Free Methods in Nonconvex Optimization: Rate Guarantees and Escaping Saddles](https://doi.org/10.48550/arxiv.2607.09167) · arXiv 사전 공개본, 누리집 NeurIPS 2026 기재 | 학습률 일정의 설계·조정 부담을 줄이는 Schedule-Free 방법의 이론을 다룬다. 입력 변화에 비례한 한계 안에서 기울기가 변하지만 볼록성은 보장하지 않는 함수를 대상으로 한다. 볼록성은 두 입력 사이의 함숫값이 양 끝의 함숫값을 이은 직선보다 높지 않은 성질이다. 기울기 계산에 무작위성을 두는 방식과 그렇지 않은 방식의 최악 조건 수렴 속도를 분석했다. 무작위성을 두지 않는 방식은 한 번의 임의로 작은 교란 아래 엄격 안장점에 머무르지 않음도 증명했다. 엄격 안장점은 기울기가 사라지지만 어떤 방향으로 함수가 아래로 휘는 점이다.[^p1] | 1저자 Jiseok Chae, 마지막 저자 Donghwan Kim |
| 2 | 2026 | [Accelerated Algorithms for Stochastic Monotone Inclusions with Fixed Queries](https://doi.org/10.48550/arxiv.2609.35631) · arXiv 사전 공개본, 투고·준비 원고 | 오차를 포함한 계산 정보를 이용하면서 반복당 계산 요청 수를 고정한 가속 방법을 연구한다. 정해진 확률적 오차 조건 아래 계산량을 줄이는 방법을 제안하고, 일반적으로 달성할 수 없는 계산량의 조합도 보인다. 기존에는 반복마다 요청 수를 늘려야 달성하던 계산량 보장을 고정된 요청 수로 달성하는 방법도 제시한다.[^p2] | 1저자 Sucheol Lee, 마지막 저자 Donghwan Kim |
| 3 | 2024 | [Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements](https://proceedings.mlr.press/v235/kim24m.html) · ICML, PMLR 235 | 미니맥스 문제에서 두 변수의 갱신 속도 차이를 크게 두어도 일부 국소 최적점에서는 기존 방법이 불안정할 수 있다. 변수를 번갈아 두 단계로 갱신하는 규칙과 갱신 속도 차이를 점차 늘리는 규칙을 추가기울기법에 도입했다. 완만한 조건 아래 기존의 두 갱신 속도를 쓰는 방법들이 도달하지 못하는 일부 국소 미니맥스점에도 도달함을 보였다.[^p3] | 1저자 Kyuwon Kim, 마지막 저자 Donghwan Kim |
| 4 | 2024 | [Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements](https://doi.org/10.48550/arxiv.2501.00511) · arXiv 사전 공개본, NeurIPS 2024 | 여러 함수의 합으로 된 미니맥스 문제에서 함수를 쓰는 순서를 섞는 확률적 추가기울기법을 분석했다. 최소화 변수에는 볼록성이, 최대화 변수에는 오목성이 성립하는 문제에서도 순서 섞기만으로는 발산할 수 있음을 보였다. 오목성은 두 입력 사이의 함숫값이 양 끝의 함숫값을 이은 직선보다 낮지 않은 성질이다. 기준점 정보를 함께 사용하는 방법이 이 조건에서 수렴함을 보이고, 최소화 변수에는 볼록성이, 최대화 변수에는 오목성이 일정 수준 이상 성립하는 문제(강볼록-강오목)에서는 계산량의 상한과 하한도 분석했다.[^p4] | 1저자 Jiseok Chae, 마지막 저자 Donghwan Kim |
| 5 | 2024 | [Revisiting Inexact Fixed-Point Iterations for Min-Max Problems: Stochasticity and Structured Nonconvexity](https://doi.org/10.48550/arxiv.2402.05071) · arXiv 사전 공개본, ICML 2024 | 제약이 있고 계산에 무작위성이 포함될 수 있는 미니맥스 문제에서, 반복법이 다룰 수 있는 문제 조건의 범위를 넓혔다. 계산을 정확하게 수행하지 않는 반복법에 대한 분석을 다듬어 요구되는 오차 조건을 완화했고, 다른 확률적 반복법의 계산량도 분석했다.[^p5] | 1저자 Ahmet Alacaoglu, 가운데 저자 Donghwan Kim, 마지막 저자 Stephen J. Wright |
| 6 | 2023 | [Open Problem: Is There a First-Order Method that Only Converges to Local Minimax Optima?](https://proceedings.mlr.press/v195/chae23a.html) · COLT, PMLR 195 | 미니맥스 문제의 국소 최적점만 찾는 일차 방법이 존재하는지를 묻는 공개 문제다. 최소화·최대화의 순서를 고려한 국소 최적점의 정의와, 일부 국소 최적점에 도달하는 추가기울기법의 결과를 논의한다. 계산이 멈추는 점을 찾는 일과 적절한 미니맥스 최적점을 찾는 일의 차이를 설명한다.[^p6] | 1저자 Jiseok Chae, 마지막 저자 Donghwan Kim |
| 7 | 2021 | [Fast Extra Gradient Methods for Smooth Structured Nonconvex-Nonconcave Minimax Problems](https://papers.nips.cc/paper/2021/hash/be767243ca8f574c740fb4c26cc6dceb-Abstract.html) · NeurIPS 34 | 일정한 구조 조건을 만족하는 미니맥스 문제를 위해 두 갱신 속도와 기준점 정보를 결합한 추가기울기법을 제안했다. 반복 횟수에 따라 기울기의 제곱 크기가 줄어드는 속도를 개선했고, 문제의 상수를 모르는 경우를 위한 변형과 확률적 분석도 제시했다.[^p7] | 1저자 Sucheol Lee, 마지막 저자 Donghwan Kim |

## 교수와 전문 분야

김동환 부교수는 KAIST 수리과학과 소속이며 University of Michigan에서 박사학위를 받았다. 개인 누리집은 직위를 associate professor로 적고 Graduate School of AI for Math(AI4Math)와의 연계도 밝힌다.[^dept][^home] 학과의 2019년 9월 27일 소식에는 당시 수리과학과 교수로 적혀 있다.[^career]

최근 논문의 방법을 바탕으로 보면 전문 분야는 기울기를 이용하는 최적화 방법의 설계와 수렴 분석이다. 미니맥스 문제에서 목표로 삼을 해를 정의하고 찾는 일, 계산 정보의 오차와 무작위성을 포함한 반복법을 분석하는 일, 학습률 규칙이 학습 과정에 미치는 영향을 설명하는 일이 연결되어 있다.[^p1][^p2][^p3][^p5][^p6]

## 응용 분야

대표 논문이 직접 다루는 응용 맥락은 기계학습(자료에서 규칙을 찾아 새 입력의 결과를 예측하거나 행동을 정하는 계산 방법)의 학습 과정이다. 생성적 적대 신경망(Generative Adversarial Network, GAN, 자료를 만드는 모형과 이를 구별하는 모형이 경쟁하며 학습하는 방식)의 학습은 미니맥스 최적화의 사례로 등장한다. 공개 문제 논문은 생성 결과의 다양성이 부족해지는 현상과 미니맥스의 국소 최적점 사이의 관계를 논의한다.[^p6] Schedule-Free 논문은 기계학습에서 사용하는 학습 방법의 수렴 속도와 안장점 회피를 다룬다.[^p1]

## 구성원

누리집 Group의 Students 9명과 Co-Advised Students 1명이다. 과정과 기간은 게시 표기를 따른다. Shiwon Park는 AI4Math 석박사통합과정이며 Changhyun Kwon 교수와 공동 지도한다고 적혀 있다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^group]

| 이름 | 과정 | 시작 | 대표 논문 참여 |
|---|---|---|---|
| Dongchul Kim | 박사과정 | M.S. Jan. 2019 - Aug. 2020; Ph.D. Sep. 2020 - |  |
| Wonyeong Song | 석박사통합과정 | Aug. 2021 - |  |
| Kyuwon Kim | 석박사통합과정 | Aug. 2022 - | 3, 6 |
| Kyungjae Lee | 석박사통합과정 | Feb. 2024 - |  |
| Yejun Kim | 석박사통합과정 | Aug. 2024 - |  |
| Dongchan Shin | 석박사통합과정 | Aug. 2024 - |  |
| Natdanai Treesakul | 석사과정 | Sep. 2025 - |  |
| Eunsung Ji | 석박사통합과정 | Mar. 2026 - |  |
| Kangjun Lee | 석사과정 | Sep. 2026 - |  |
| Shiwon Park | 석박사통합과정 | Mar. 2026 - |  |

## 졸업생과 이전 구성원

누리집 Group의 Alumni에 실린 10명이다. 박사후연구원, 박사·석사 졸업생, 인턴과 URP 참여자를 포함한다. 과정·기간·진로는 게시 표기를 따른다. URP는 누리집의 과정 표기이며, 진로의 화살표는 앞에 적힌 소속에서 뒤의 소속으로 이어지는 게시 순서다.[^group]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Jimyeong Kim | Postdoc (Postdoc, Mar. 2024 - Dec. 2024) | Samsung SDS |
| Jiseok Chae | M.S.-Ph.D.; Postdoc (M.S.-Ph.D. Aug. 2021 - Feb. 2026, Postdoc, Mar. 2026) | KAIST NSRI / Yonsei Univ. PDE & AI Lab Postdoc |
| Hyeokjoo Park | Ph.D. (Ph.D. Mar. 2020 - Feb. 2024; co-advised by Prof. Do Young Kwak) | Yonsei Univ. CSE Postdoc → Korea Univ. Sejong Campus Assistant Prof. |
| Sucheol Lee | M.S.-Ph.D. (M.S.-Ph.D. Mar. 2016 - Feb. 2022; advised since Nov. 2019) | Samsung Advanced Institute of Technology |
| Hyeonmin Lee | M.S. (M.S. Jan. 2019 - Feb. 2021) | KAIST ISysE Ph.D. Program |
| Euntaek Shin | M.S. (M.S. Jul. 2019 - Feb. 2021) | MOBILTECH |
| Trong Doan Nguyen | Intern (KAI-X Research Internship Jul. 2026 - Aug. 2026) |  |
| Keyan Shi | Intern (KAI-X Research Internship, Jun. 2023 - Aug. 2023) |  |
| Minhak Song | URP (URP, Jan. 2026 - Jun. 2026) |  |
| Woohyuck Kim | URP (URP, Jan. 2022 - Jun. 2022) |  |

## 최근 논문 목록 (2021–2026)

교수 개인 누리집 Publications의 Journal/Conference Papers 9편과 Submitted Papers/In Preparation의 사전 공개본 1편이다. 학회·학술지 논문의 제목·저자·발표처는 게시 표기대로 두었다. 투고·준비 원고는 사전 공개본으로 표시하고 연도는 해당 판본의 첫 게시 연도를 썼다. 2026년 NeurIPS 항목은 누리집 기재이며, 저자 이름 뒤의 별표는 누리집이 밝힌 공동 기여 표시다.[^pubs][^p2]

**2026**

- S. Lee, D. Kim. "Accelerated algorithms for stochastic monotone inclusions with fixed queries". *arXiv:2609.35631 (투고·준비 원고, 사전 공개본)*.
- J. Chae, D. Kim. "Understaning schedule-free methods in nonconvex optimization: Rate guarantees and escaping saddles". *Neural Information Processing Systems (NeurIPS), 2026*.
- Y. Kim\*, K. Lee\* and D. Kim. "Minimax optimization without spurious solutions in optimal transport learning". *Neural Information Processing Systems (NeurIPS), 2026*.
- J. Chae\*, K. Kim\* and D. Kim. "Rethinking memorization-generalization trade-off in generative models". *Neural Information Processing Systems (NeurIPS), 2026*.

**2024**

- J. Chae, C. Yun, and D. Kim. "Stochastic extragradient with flip-flop shuffling & anchoring: Provable improvements". *Neural Information Processing Systems (NeurIPS), 2024*.
- K. Kim and D. Kim. "Double-step alternating extragradient with increasing timescale separation for finding local minimax points: Provable improvements". *International Conference on Machine Learning (ICML), 2024*.
- A. Alacaoglu, D. Kim and S. J. Wright. "Revisiting inexact fixed-point iterations for min-max problems: Stochasticity and structured nonconvexity". *International Conference on Machine Learning (ICML), 2024*.
- J. Chae, K. Kim and D. Kim. "Two-timescale extragradient for finding local minimax points". *International Conference on Learning Representations (ICLR), 2024*.

**2023**

- J. Chae, K. Kim and D. Kim. "Open Problem: Is there a first-order method that only converges to local minimax optima?". *Conference on Learning Theory (COLT), 2023*.

**2021**

- S. Lee and D. Kim. "Fast extra gradient methods for smooth structured nonconvex-nonconcave minimax problems". *Neural Information Processing Systems (NeurIPS), 2021*.

## 수상과 선정

누리집 Group에 실린 구성원의 학위논문 수상 2건이다. 연도는 누리집의 표기이고 날짜는 게시되어 있지 않다.[^group]

- 2025 · Jiseok Chae: KAIST outstanding dissertation award 수상
- 2024 · Sucheol Lee: Korean Mathematical Society outstanding dissertation award 수상

## 연락과 위치

- 연구실 위치: 산업경영학동 3205[^dept]
- 기관 전화 표기: T2717[^dept]
- 교수 이메일: donghwankim@kaist.ac.kr[^cv]
[^home]: Donghwan Kim, 개인 누리집 첫 화면의 About Me·Current Research Interests. <https://mathsci.kaist.ac.kr/~donghwankim/> 관측 2026-11-07.
[^dept]: KAIST 수리과학과 교수 목록의 김동환 항목. <https://mathsci.kaist.ac.kr/home/people/professor/> 관측 2026-11-07.
[^group]: Donghwan Kim, Group의 Students·Co-Advised Students·Alumni. <https://mathsci.kaist.ac.kr/~donghwankim/group.html> 관측 2026-11-07.
[^pubs]: Donghwan Kim, Publications의 Submitted Papers/In Preparation·Journal/Conference Papers·Technical reports. <https://mathsci.kaist.ac.kr/~donghwankim/publications.html> 관측 2026-11-07.
[^career]: KAIST 수리과학과, Professors Donghwan Kim and Jaehoon Kim Chosen for POSCO Science Fellowship 2019, 게시 2019-09-27, 수정 2019-10-21. <https://mathsci.kaist.ac.kr/home/en/2019/09/professors-donghwan-kim-and-jaehoon-kim-chosen-as-posco-science-fellowship-2019/> 관측 2026-11-07.

[^p1]: J. Chae, D. Kim, arXiv (온라인 2026-07-10). <https://doi.org/10.48550/arxiv.2607.09167> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2607.09167>. 관측 2026-11-07.
[^p2]: S. Lee, D. Kim, arXiv (온라인 2026-09-28). <https://doi.org/10.48550/arxiv.2609.35631> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2609.35631>. 관측 2026-11-07.
[^p3]: K. Kim, D. Kim, Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 24059-24093 (2024). <https://proceedings.mlr.press/v235/kim24m.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v235/kim24m.html>. 관측 2026-11-07.
[^p4]: J. Chae, C. Yun, D. Kim, arXiv (온라인 2024-12-31). <https://doi.org/10.48550/arxiv.2501.00511> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2501.00511>. 관측 2026-11-07.
[^p5]: A. Alacaoglu, D. Kim, S. J. Wright, arXiv (온라인 2024-02-07). <https://doi.org/10.48550/arxiv.2402.05071> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2402.05071>. 2026-09-26 개정판 초록. 관측 2026-11-07.
[^p6]: J. Chae, K. Kim, D. Kim, Proceedings of Thirty Sixth Conference on Learning Theory, PMLR 195, 5957-5964 (2023). <https://proceedings.mlr.press/v195/chae23a.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://proceedings.mlr.press/v195/chae23a.html>. 관측 2026-11-07.
[^p7]: S. Lee, D. Kim, Advances in Neural Information Processing Systems 34 (2021). <https://papers.nips.cc/paper/2021/hash/be767243ca8f574c740fb4c26cc6dceb-Abstract.html> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://papers.nips.cc/paper/2021/hash/be767243ca8f574c740fb4c26cc6dceb-Abstract.html>. 관측 2026-11-07.
[^cv]: Donghwan Kim, CV. <http://mathsci.kaist.ac.kr/~donghwankim/doc/donghwan-cv.pdf> 관측일 2026-11-07.

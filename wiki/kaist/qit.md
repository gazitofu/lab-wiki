# Quantum Information Theory Group (KAIST QIT)

**KAIST 물리학과 · 오창훈 조교수**

- 분야: 이론 양자 정보, 양자 학습, 양자 장치의 계산 능력과 고전적 모의, 양자 계측·센싱[^research][^dept]
- 대분야: 물리·양자
- 태그: 양자 컴퓨팅[^home][^dept], 양자 정보·얽힘[^research][^dept], 양자 계측·센싱[^research][^dept]
- 홈페이지: <https://sites.google.com/view/qitkaistphysics>
- 근거와 출처: [Quantum Information Theory Group 근거 페이지](qit-sources.md)

> 양자 장치가 계산·학습·측정에서 갖는 이점과 그 한계를 이론으로 따지는 연구실이다.[^home][^research]

## 무엇을 연구하나

연구실은 양자 정보(양자 상태로 정보를 표현하고 처리하며 측정하는 원리)를 연구한다. 양자 상태는 물리계의 측정 결과가 어떤 확률로 나오는지 정하는 수학적 표현이며, 얽힘은 여러 부분으로 이루어진 양자계의 전체 상태를 각 부분의 독립된 상태들의 확률적 혼합으로 나타낼 수 없는 상관이다. 연구실은 이런 자원을 사용하는 양자 컴퓨팅(양자 중첩과 얽힘을 계산 자원으로 이용하는 계산)이 어떤 문제에서 고전적 계산(양자 중첩을 계산 자원으로 사용하지 않는 계산)과 구별되는 능력을 갖는지 연구한다.[^home][^dept]

첫 갈래는 양자 학습(양자계의 상태나 작용에 관한 정보를 관측 자료로 알아내는 연구)이다. 같은 정보를 알아내는 데 필요한 자료 수, 계산의 효율, 계산 능력이 양자역학의 성질에 따라 어떻게 달라지는지 묻는다. 특히 표본 복잡도(정해진 정확도와 성공 확률을 얻는 데 필요한 관측 자료의 수)를 비교해 양자 자원이 학습에서 이점을 주는 조건을 찾는다.[^research]

둘째는 잡음(의도한 신호나 동작을 방해하는 불규칙한 변동)이 있는 양자 장치의 능력과 고전적 모의(일반 컴퓨터로 대상 장치의 동작이나 출력 특성을 계산하는 것)의 경계다. 주요 대상으로 보손 샘플링(빛의 양자 단위인 광자들이 광학 회로를 지난 뒤 검출되는 배치를 확률분포에 따라 뽑는 계산 문제), 특정 양자 회로의 출력 추출, 양자 오류 정정(양자 정보에 생긴 오류를 부호를 이용해 알아내고 바로잡는 방법)을 든다. 무엇을 계산하는지와 어떤 자원을 허용하는지에 따라 양자 장치의 이점이 남는 범위를 분석한다.[^research]

셋째는 양자 계측·센싱(양자 상태와 측정의 성질을 이용해 물리량을 추정하는 기술)이다. 연구실은 얽힘 등 양자 자원이 측정 정밀도를 어떻게 높일 수 있는지 연구한다. 응용 대상으로 간섭계(파동이 겹치는 성질로 위상 차이를 재는 장치), 시계, 영상, 장과 힘의 측정, 여러 센서를 연결한 분산 측정을 든다.[^research][^dept]

## 주요 연구 주제

### 1. 학습에 필요한 양자 자원

양자 학습에서 얽힘의 양과 양자 메모리(양자 상태를 저장하고 유지하는 장치)가 맡는 역할을 구별한다. 대표 논문 2는 양자 메모리와의 얽힘이 작더라도 학습에 이점을 줄 수 있지만, 이를 돕는 양자 비트의 수가 충분하지 않으면 필요한 관측 자료 수가 급격히 늘 수 있음을 보였다. 양자 비트는 서로 구별되는 두 기준 상태와 그 중첩으로 정보를 나타내는 단위다. 대표 논문 1은 연속변수(끊어지지 않은 범위의 값을 갖는 변수) 양자 상태를 학습하는 자원 조건을, 대표 논문 3은 광학 플랫폼에서 구현한 학습 이점을 다룬다.[^p1][^p2][^p3]

### 2. 광학 양자 회로를 일반 컴퓨터로 계산할 수 있는 조건

선형 광학 회로(입력 빛의 진폭에 선형 변환을 가해 출력 빛의 진폭을 정하는 광학 회로)의 계산 문제를 분석한다. 대표 논문 4는 측정 결과를 다음 동작에 반영하는 단계 수에 따라 관측량의 기댓값(같은 조건의 측정을 반복했을 때 결과의 평균으로 주어지는 값)을 일반 컴퓨터로 효율적으로 구할 수 있는 경계를 보였다. 대표 논문 5는 단계 수가 적은 보손 샘플링의 출력 확률을 추정하는 문제가 평균적인 경우에도 어려운지를 다룬다.[^p4][^p5]

### 3. 손실이 있는 센서망과 양자 영상

연구실은 양자 자원을 이용한 정밀 측정과 센서망을 연구한다.[^research] 대표 논문 6은 광자 손실을 견디는 광학 분산 센싱 구성을 제안하고 분석한다. 대표 논문 7은 학습 이론을 이용해 영상에서 안정적으로 추정할 수 있는 특징을 구분하고, 서로 가까이 놓인 여러 작은 광원을 다루는 영상 획득 방법을 제시한다.[^p6][^p7]

## 대표 논문

오창훈 교수가 KAIST에 부임한 2024년 4월 이후의 논문 가운데 양자 학습, 고전적 모의와 계산 복잡도(입력 크기에 따라 필요한 시간·저장 공간 등 계산 자원이 늘어나는 정도), 양자 계측·영상을 고르게 다루는 7편을 골랐다. 연도 칸은 Full Publications의 연도 구역이며, 발표처·게재 승인 표기와 교신 표시는 연구실 목록을 따른다. 주요 저자의 전체 이름과 순서는 등록 서지를 따른다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다. 1번은 연구실의 arXiv·게재 승인 표기와 등록 학술지 DOI를 함께 적었으며, 설명은 해당 DOI의 등록 초록을 기준으로 썼다.[^leader][^pubs]

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Exponential advantage in continuous-variable quantum state learning](https://arxiv.org/abs/2501.17633) · arXiv:2501.17633 (2025) (npj Quantum Inf. in press) (게재 승인) · [등록 학술지 DOI](https://doi.org/10.1038/s41534-026-01391-z) | 연속변수 양자 상태를 학습할 때 얽힌 측정과 입력 상태의 성질 등이 필요한 상태 사본 수를 어떻게 정하는지 분석했다. 얽힘을 쓰지 않는 방식이 충분한 경우와 여러 자원을 함께 갖춰야 효율적인 학습이 가능한 경우를 구분했다.[^p1] | Eugen Coroi(첫 저자), Changhun Oh(마지막·교신저자) |
| 2 | 2026 | [On the fundamental resource for exponential advantage in quantum channel learning](https://doi.org/10.1038/s41467-026-68532-y) · Nature Communications 17 (1) 1822 (2026) | 양자 채널(양자 상태가 겪는 물리적 변화를 나타내는 규칙)을 배우는 데 얽힘의 양과 보조 양자 비트의 수가 미치는 영향을 나누어 분석했다. 입력 상태의 얽힘이 작아도 이점을 얻을 수 있지만, 양자 메모리의 크기가 핵심 자원임을 보였다.[^p2] | Minsoo Kim(첫 저자), Changhun Oh(마지막·교신저자) |
| 3 | 2025 | [Quantum learning advantage on a scalable photonic platform](https://doi.org/10.1126/science.adv2560) · Science 389 (6767) 1332-1335 (2025) | 많은 변수를 가진 물리 과정을 학습하는 양자 방식을 광학 플랫폼에서 구현했다. 불완전한 얽힘을 사용하면서도 얽힘이 없는 고전적 방법에 비해 필요한 관측 자료 수를 줄이는 양자 학습 이점을 보였다.[^p3] | Zhenghao Liu(첫 저자), Changhun Oh(11/15번째 저자), Ulrik L. Andersen(마지막 저자) |
| 4 | 2026 | [Classical Algorithms for Measurement-Adaptive Gaussian Circuits](https://doi.org/10.1103/rpl7-ylg8) · PRX Quantum 7 (1) 010329 (2026) | 측정 결과에 따라 다음 동작을 바꾸는 광학 회로에서 관측량의 기댓값을 계산하는 문제를 연구했다. 이런 적응 단계가 적을 때는 일반 컴퓨터로 효율적으로 계산할 수 있음을 보이고, 단계 수에 따른 계산 난도의 경계를 분석했다.[^p4] | Changhun Oh(첫·교신저자), Youngrong Lim(마지막 저자) |
| 5 | 2026 | [On computational complexity and average-case hardness of shallow-depth boson sampling](https://doi.org/10.22331/q-2026-03-13-2026) · Quantum 10 2026 (2026) | 회로 깊이(동시에 수행할 수 있는 연산을 한 층으로 묶었을 때의 단계 수)를 제한한 보손 샘플링의 계산 난도를 분석했다. 출력 확률 추정이 평균적인 경우에도 어려운 조건에 관한 결과를 제시하고, 광자 손실이 있는 경우까지 다뤘다.[^p5] | Byeongseon Go(첫 저자), Changhun Oh(2/3번째·교신저자), Hyunseok Jeong(마지막·교신저자) |
| 6 | 2026 | [All-optical Loss-tolerant Distributed Quantum Sensing](https://doi.org/10.1038/s41534-025-01123-9) · npj Quantum Information 12 (1) 18 (2026) | 광학 증폭기(빛의 세기를 키우는 장치)와 간섭계를 결합한 분산 양자 센싱 방식을 제안하고 분석했다. 센서망 전체의 성질을 추정할 때의 민감도와 광자 손실을 견디는 성질을 평가하고, 현재 광양자 기술을 통한 구현 가능성을 제시했다.[^p6] | Rajveer Nehra(첫·교신저자), Changhun Oh(2/4번째·교신저자), Alireza Marandi(마지막 저자) |
| 7 | 2026 | [Advancing quantum imaging through learning theory](https://doi.org/10.1038/s41467-025-67884-1) · Nature Communications 17 (1) 1124 (2025) | 영상 장치를 학습 장치로 보고, 측정 자료에서 안정적으로 추정할 수 있는 특징과 그에 필요한 표본 수를 분석했다. 가까이 놓인 여러 작은 광원을 다루도록 초해상도(통상적인 광학 분해능의 한계를 넘어 세부를 구분하는 기술) 방법을 확장하고 영상 과제에서 성능을 보였다.[^p7] | Yunkai Wang(첫 저자), Changhun Oh(2/5번째 저자), Sisi Zhou(마지막 저자) |

## 교수와 전문 분야

오창훈 교수는 2014년 서강대학교에서 물리학 학사, 2020년 서울대학교에서 물리학 박사 학위를 받았다. 2020년 3월–2024년 3월 시카고대학교 Pritzker School of Molecular Engineering에서 박사후연구원으로 일했고, 2024년 4월 KAIST 물리학과 조교수로 부임했다.[^dept][^leader] 학과는 전문 분야를 이론 양자 정보와 양자 컴퓨팅으로 소개한다.[^dept] 대표 논문에서 드러나는 전문 분야는 양자 학습의 자원과 표본 비용, 광학 양자 회로의 고전적 계산 가능성, 양자 센싱과 영상의 정보 추정 이론이다.[^p2][^p4][^p6][^p7]

## 응용 분야

연구실은 양자 장치의 계산 이점을 평가하는 이론, 양자계의 성질을 알아내는 학습, 정밀 측정과 분산 센싱을 응용 방향으로 든다.[^research][^dept] 대표 논문에는 광학 플랫폼의 학습 실험, 손실을 고려한 광학 센서망, 여러 광원이 가까이 놓인 영상 과제가 포함된다.[^p3][^p6][^p7]

## 구성원

누리집 Group Members에 게시된 박사후연구원 2명, 대학원생 7명, 학부생 2명이다. 과정·연구 주제와 학교 이메일은 게시 표기대로 적었다. "대표 논문 참여"는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Chandan Kumar | 박사후연구원 | Continuous variable quantum information theory; Quantum metrology and quantum communication | chandan@kaist.ac.kr |  |
| Simone Cavazzoni | 박사후연구원 | Quantum Sensing and Metrology; Quantum Walks; Quantum Routing and Transport | simone.cavazzoni@kaist.ac.kr |  |
| Minsoo Kim | 대학원생 | Quantum learning; Tensor network | nijgnuy@kaist.ac.kr | 2 |
| Sojeong Park | 대학원생 | Boson sampling; Quantum simulation | sojeong.park@kaist.ac.kr |  |
| Jiwon Heo | 대학원생 | Quantum information theory | 4865sj@kaist.ac.kr |  |
| Vaughan Sohn | 대학원생 | Quantum cryptography; Quantum error correction | webb41@kaist.ac.kr |  |
| Eugen Coroi | 대학원생 | Quantum learning theory; Quantum algorithms | eugen@kaist.ac.kr | 1 |
| Eunbin Yang | 대학원생 | Quantum learning theory; Quantum information theory; Quantum algorithms | ybse1013@kaist.ac.kr |  |
| Hodong Lee | 대학원생 | Quantum machine learning; Quantum information theory | ghehd1024@kaist.ac.kr |  |
| Hyeongu Kang | 학부 연구생 | Quantum metrology; Quantum learning theory; Quantum information theory | venator2021@kaist.ac.kr |  |
| Myeongjin Shin | 학부 연구생 | Quantum learning theory; Quantum property testing; Quantum algorithms |  |  |

## 졸업생과 이전 구성원

누리집 Alumni 구획의 이전 구성원 1명이다. 학위·과정 칸은 게시된 역할이고 괄호 안은 재직 기간이다. 진로는 누리집 표기 그대로다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Sangwoo Jeon | Research Assistant (03.2025. ~ 08.2026.) | Waterloo University |

## 최근 논문 목록 (2021–2026)

누리집 Publications의 Full Publications에 게시된 2024–2026년 문헌 48편이다. 연도 구역은 2026년 33편, 2025년 7편, 2024년 8편이며, 각 줄의 제목·저자·발표처와 서지 연도는 게시 표기 그대로다. 연도 구역과 각 줄의 서지 연도는 다를 수 있다. "in press" 2편은 학술지 게재 승인으로 구분했고, arXiv 번호와 "alphabetic order" 표기는 원문대로 적었다. 저자 이름 뒤 별표는 교신 표시다. 오창훈 교수는 2024년 4월 KAIST에 부임했으며, 2024년 목록에는 부임 전 시카고대학교 시기의 논문도 포함된다.[^pubs][^leader]

**2026**

- S. Park and C. Oh\*. "Matrix product state approach to lossy boson sampling and noisy IQP sampling". *arXiv:2510.24137 (2025) (npj Quantum Inf. in press)*. (게재 승인) <https://arxiv.org/abs/2510.24137>
- M. Shin, J. Lee, and C. Oh\*. "Heisenberg-Limited Hamiltonian Learning Without Short-Time Control". *PRX Quantum 7 (4) 043011 (2026)*. DOI: <https://doi.org/10.1103/kjvf-jgqj>
- S. Park and C. Oh\*. "Exponential Quantum Advantage in Stationary Signal Sensing". *arXiv:2610.14424 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2610.14424>
- Y.-X. Wang, J. Bringewatt, A. Seif, A. J. Brady, C. Oh, and A. V. Gorshkov. "Exponential Entanglement Advantage in Sensing Correlated Noise". *Physical Review Letters 137 (15) 150803 (2026)*. DOI: <https://doi.org/10.1103/nmk6-924g>
- G. Cho, C. Oh\*, and D. Kim. "Quantum state learning beyond approximate unitary designs". *arXiv:2609.39994 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2609.39994>
- S. Cavazzoni\* and C. Oh\*. "Metrological Benchmarking of Random Quantum Circuits". *arXiv:2609.39226 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2609.39226>
- M. Hhan, C. Oh, and V. Sohn. "Need for Coherent Access in Constructing Quantum Cryptography". *arXiv:2609.40301 (2026) (alphabetic order)*. DOI: <https://doi.org/10.48550/arxiv.2609.40301>
- J. Heo, M. Shin, and C. Oh\*. "Efficient Learning of Fermionic Magic States under Free-Fermion Evolution". *arXiv:2609.39372 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2609.39372>
- J. Heo, O. Reardon-Smith, M. Oszmaniec, Z. Zimborás, and C. Oh\*. "Fast classical simulation algorithms for free-fermion dynamics with magic input". *arXiv:2609.40187 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2609.40187>
- B. Seron, H. Thomas, E. Araujo, A. Arkhipov, C. Oh, and L. Novo. "Efficient classical algorithm for estimating linear statistics of Boson Sampling". *arXiv:2609.35447 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2609.35447>
- E. Coroi and C. Oh\*. "Exponential advantage in continuous-variable quantum state learning". *arXiv:2501.17633 (2025) (npj Quantum Inf. in press)*. (게재 승인) <https://arxiv.org/abs/2501.17633>
- C. Oh\*, S. H. Lie, and Y. Lim. "Ultimate Information Rate for Quantum Sensing under Multilevel Relaxation". *arXiv:2609.21418 (2026)*. <https://arxiv.org/abs/2609.21418>
- C. Oh\*. "Logarithmic-depth quantum simulation of boson sampling". *arXiv:2609.18907 (2026)*. <https://arxiv.org/abs/2609.18907>
- Y. Lim and C. Oh\*. "Classical Algorithms for Estimating Expectation Values in Linear Optical Circuits". *Physical Review Letters 137 (12) 120602 (2026)*. DOI: <https://doi.org/10.1103/bl9r-2gyb>
- S. Jeon, V. Sohn, and C. Oh\*. "Optimal copy complexity of quantum state cloning". *arXiv:2608.24484 (2026)*. <https://arxiv.org/abs/2608.24484>
- B. Go, H. Jeong, and C. Oh\*. "Threshold and parity BosonSampling in the linear-mode regime". *arXiv:2608.24008 (2026)*. <https://arxiv.org/abs/2608.24008>
- B. Go, C. Oh\*, and H. Jeong. "Hardness and complexity transition of noisy random circuit sampling". *arXiv:2607.20804 (2026)*. <https://arxiv.org/abs/2607.20804>
- H. Kang, S. Jeon, and C. Oh\*. "Bound entanglement is insufficient for an exponential quantum learning advantage". *arXiv:2607.19017 (2026)*. <https://arxiv.org/abs/2607.19017>
- S.-B. B. Lee, C.-Y. Park, C. Oh, and S.-S. B. Lee. "Coherent-disorder-driven complexity transitions in a quantum-advantage architecture". *arXiv:2607.18938 (2026)*. <https://arxiv.org/abs/2607.18938>
- M. Kim, C. Oh\*, and D. Kim. "Disentangling Haldane phase by generalized Clifford circuits". *arXiv:2607.03939 (2026)*. <https://arxiv.org/abs/2607.03939>
- V. Sohn and C. Oh\*. "When to Skip Syndrome Extraction in Surface-GKP Codes". *arXiv:2606.24469 (2026)*. <https://arxiv.org/abs/2606.24469>
- C. Oh\*, M. Oszmaniec, O. Reardon-Smith, and Z. Zimborás. "Classical simulation of free-fermionic dynamics and quantum chemistry with magic input". *arXiv:2604.26813 (2026)*. <https://arxiv.org/abs/2604.26813>
- B. Go, H. Jeong, and C. Oh\*. "Complexity phase transition for continuous-variable cluster state". *arXiv:2604.07804 (2026)*. <https://arxiv.org/abs/2604.07804>
- H. Kwon, C. Oh, Y. Lim, H. Jeong, S.-W. Lee, and L. Jiang. "Virtual purification complements quantum error correction in quantum metrology". *npj Quantum Information 12 (1) 88 (2026)*. DOI: <https://doi.org/10.1038/s41534-026-01231-0>
- Z. Kolarovszki, B. Bakó, M. Oszmaniec, C. Oh, and Z. Zimborás. "Generative modeling with Gaussian boson sampling: classically trainable bosonic Born machines". *arXiv:2603.11195 (2026)*. <https://arxiv.org/abs/2603.11195>
- B. Go, C. Oh\*, and H. Jeong\*. "On computational complexity and average-case hardness of shallow-depth boson sampling". *Quantum 10 2026 (2026)*. DOI: <https://doi.org/10.22331/q-2026-03-13-2026>
- C. Oh\* and Y. Lim. "Classical Algorithms for Measurement-Adaptive Gaussian Circuits". *PRX Quantum 7 (1) 010329 (2026)*. DOI: <https://doi.org/10.1103/rpl7-ylg8>
- M. Kim and C. Oh\*. "On the fundamental resource for exponential advantage in quantum channel learning". *Nature Communications 17 (1) 1822 (2026)*. DOI: <https://doi.org/10.1038/s41467-026-68532-y>
- Y. Kim, K. Lee, C. Oh, Y.-S. Ra, K. W. Kim, and B. Min. "Classical Petermann factor as a measure of quantum squeezing in photonic time crystals". *arXiv:2601.17369 (2026)*. <https://www.arxiv.org/abs/2601.17369>
- R. Nehra\*, C. Oh\*, L. Jiang, and A. Marandi. "All-optical Loss-tolerant Distributed Quantum Sensing". *npj Quantum Information 12 (1) 18 (2026)*. DOI: <https://doi.org/10.1038/s41534-025-01123-9>
- Y. Wang, C. Oh, J. Liu, L. Jiang, and S. Zhou. "Advancing quantum imaging through learning theory". *Nature Communications 17 (1) 1124 (2025)*. DOI: <https://doi.org/10.1038/s41467-025-67884-1>
- J. Heo, S. Park, and C. Oh\*. "Classical simulation of a quantum circuit with noisy magic inputs". *arXiv:2601.10111 (2026)*. DOI: <https://doi.org/10.48550/arxiv.2601.10111>
- S. Jeon and C. Oh\*. "On the query complexity of unitary channel certification". *npj Quantum Information 12 (1) 2 (2025)*. DOI: <https://doi.org/10.1038/s41534-025-01135-5>

**2025**

- B. Go, C. Oh\*, and H. Jeong\*. "Sufficient conditions for hardness of lossy Gaussian boson sampling". *arXiv:2511.07853 (2025)*. DOI: <https://doi.org/10.48550/arxiv.2511.07853>
- S.-u. Lee, S. Ghosh, C. Oh, K. Noh, B. Fefferman, and L. Jiang. "Classical simulation of noisy random circuits from exponential decay of correlation". *arXiv:2510.06328 (2025)*. DOI: <https://doi.org/10.48550/arxiv.2510.06328>
- J. T. Iosue, Y.-X. Wang, I. Datta, S. Ghosh, C. Oh, B. Fefferman, and A. V. Gorshkov. "Higher moment theory and learnability of bosonic states". *arXiv:2510.01610 (2025)*. DOI: <https://doi.org/10.48550/arxiv.2510.01610>
- Z.-H. Liu, R. Brunel, E. E. B. Østergaard, O. Cordero, S. Chen, Y. Wong, J. A. H. Nielsen, A. B. Bregnsbo, S. Zhou, H.-Y. Huang, C. Oh, L. Jiang, J. Preskill, J. S. Neergaard-Nielsen, and U. L. Andersen. "Quantum learning advantage on a scalable photonic platform". *Science 389 (6767) 1332-1335 (2025)*. DOI: <https://doi.org/10.1126/science.adv2560>
- B. Go, C. Oh\*, and H. Jeong\*. "Quantum Computational Advantage of Noisy Boson Sampling with Partially Distinguishable Photons". *PRX Quantum 6 (3) 030362 (2025)*. DOI: <https://doi.org/10.1103/rflv-gc66>
- C. Oh\*. "Classical simulability of constant-depth linear-optical circuits with noise". *npj Quantum Information 11 (1) 126 (2025)*. DOI: <https://doi.org/10.1038/s41534-025-01041-w>
- C. Oh\*. "Recent theoretical and experimental progress on boson sampling". *Curr. Opt. Photon. 9, 1-18 (2025)*. <https://www.coppjournal.org/journal/view.html?uid=1651>

**2024**

- C. Oh\*, S. Chen\*, Y. Wong, S. Zhou, H.-Y. Huang, J. A. H. Nielsen, Z.-H. Liu, J. S. Neergaard-Nielsen, U. L. Andersen, L. Jiang, and J. Preskill. "Entanglement-Enabled Advantage for Learning a Bosonic Random Displacement Channel". *Physical Review Letters 133 (23) 230604 (2024)*. DOI: <https://doi.org/10.1103/physrevlett.133.230604>
- S.-u. Lee\*, C. Oh, Y. Wong, S. Chen, and L. Jiang. "Universal Spreading of Conditional Mutual Information in Noisy Random Circuits". *Physical Review Letters 133 (20) 200402 (2024)*. DOI: <https://doi.org/10.1103/physrevlett.133.200402>
- C. Oh\*, M. Liu\*, Y. Alexeev, B. Fefferman, and L. Jiang. "Classical algorithm for simulating experimental Gaussian boson sampling". *Nature Physics 20 (9) 1461-1468 (2024)*. DOI: <https://doi.org/10.1038/s41567-024-02535-8>
- C. Oh\*, B. Fefferman, L. Jiang, and N. Quesada. "Quantum-Inspired Classical Algorithm for Graph Problems by Gaussian Boson Sampling". *PRX Quantum 5 (2) 020341 (2024)*. DOI: <https://doi.org/10.1103/prxquantum.5.020341>
- B. Go, C. Oh\*, L. Jiang, and H. Jeong. "Exploring shallow-depth boson sampling: Toward a scalable quantum advantage". *Physical Review A 109 (5) 052613 (2024)*. DOI: <https://doi.org/10.1103/physreva.109.052613>
- S. Chen\*, C. Oh, S. Zhou, H.-Y. Huang, and L. Jiang\*. "Tight Bounds on Pauli Channel Learning without Entanglement". *Physical Review Letters 132 (18) 180805 (2024)*. DOI: <https://doi.org/10.1103/physrevlett.132.180805>
- H. Kwon, C. Oh\*, Y. Lim, H. Jeong, and L. Jiang. "Efficacy of virtual purification-based error mitigation on quantum metrology". *Physical Review A 109 (2) 022410 (2024)*. DOI: <https://doi.org/10.1103/physreva.109.022410>
- C. Oh\*, Y. Lim, Y. Wong, B. Fefferman, and L. Jiang. "Quantum-inspired classical algorithms for molecular vibronic spectra". *Nature Physics 20 (2) 225-231 (2024)*. DOI: <https://doi.org/10.1038/s41567-023-02308-9>

## 연락과 위치

- 기관 전화: +82-42-350-2521[^dept]
- 교수 연구실: KAIST KI building(E4) A321[^home][^dept]
- 학생 연구 공간: E4 A322·A323[^home]
- 주소: 291 Daehak-ro, Yuseong-gu, Daejeon 34141, South Korea[^home]
[^home]: Quantum Information Theory Group, Home. <https://sites.google.com/view/qitkaistphysics> 관측일 2026-11-07.
[^research]: KAIST QIT, Research Topics. <https://sites.google.com/view/qitkaistphysics/research> 관측일 2026-11-07.
[^dept]: KAIST 물리학과, Oh, Changhun 교수 소개. <https://physics.kaist.ac.kr/index.php?document_srl=16267&mid=p_people1> 관측일 2026-11-07.
[^leader]: KAIST QIT, Team Leader. <https://sites.google.com/view/qitkaistphysics/people/team-leader> 관측일 2026-11-07.
[^members]: KAIST QIT, Group Members. <https://sites.google.com/view/qitkaistphysics/people/members> 관측일 2026-11-07.
[^pubs]: KAIST QIT, Publications의 Full Publications 전체 논문 목록. <https://script.google.com/macros/s/AKfycbzn8fni1DMQw90cbUxGh8BaBy9vqM1mRXLxp39S11RiOb7X1kganP56xKYWyPP6MwLE/exec> 관측일 2026-11-07.
[^p1]: E. Coroi, C. Oh, npj Quantum Information (2026). <https://doi.org/10.1038/s41534-026-01391-z> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p2]: M. Kim, C. Oh, Nature Communications (2026). <https://doi.org/10.1038/s41467-026-68532-y> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p3]: Z. Liu 외, U. L. Andersen, Science (2025). <https://doi.org/10.1126/science.adv2560> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p4]: C. Oh, Y. Lim, PRX Quantum (2026). <https://doi.org/10.1103/rpl7-ylg8> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p5]: B. Go, C. Oh, H. Jeong, Quantum (2026). <https://doi.org/10.22331/q-2026-03-13-2026> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p6]: R. Nehra, C. Oh, L. Jiang, A. Marandi, npj Quantum Information (2026). <https://doi.org/10.1038/s41534-025-01123-9> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.
[^p7]: Y. Wang 외, S. Zhou, Nature Communications (2025). <https://doi.org/10.1038/s41467-025-67884-1> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5022686032,publication_year:2021-2026> 관측일 2026-11-07.

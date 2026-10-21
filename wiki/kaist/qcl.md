# 양자컴퓨팅 연구실 (Jaewook Ahn's Quantum Computing Lab)

**KAIST 물리학과 · 안재욱 교수**

- 분야: 리드버그 원자(전자 하나를 아주 높은 에너지로 들뜨게 한 원자) 양자컴퓨터와 양자 시뮬레이터, 광집게(레이저 빛으로 원자 하나를 붙잡는 장치) 원자 배열 제어, 양자 최적화 계산, 초고속 레이저 양자 제어, 테라헤르츠 분광
- 대분야: 물리·양자
- 태그: 양자 컴퓨팅[^home], 양자 정보·얽힘[^p6], 원자 물리·광집게 원자 배열[^p7], 테라헤르츠 분광·소자[^research][^physics]
- 홈페이지: <http://qcl.kaist.ac.kr/>
- 근거와 출처: [양자컴퓨팅 연구실 근거 페이지](qcl-sources.md)

> 레이저로 원자를 하나씩 붙잡아 원하는 모양으로 늘어놓고, 원자들 사이의 강한 상호작용을 이용해 양자컴퓨터와 양자 시뮬레이터를 만드는 연구실이다. 이 장치로 어려운 최적화 문제를 풀거나, 원자를 던지고 받아 옮기는 기술을 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 리드버그 원자와 양자 제어 방법으로 양자컴퓨터와 양자 시뮬레이터를 개발한다고 소개한다.[^home] 연구 페이지는 실험 장치 세 가지를 중심으로 연구를 설명한다. ALICE는 움직일 수 있는 광집게 100개와 리드버그 들뜸 장치를 갖춘 루비듐 원자 장치로, 광 미세 트랩을 재배치해 원자 30개를 사슬로 늘어놓은 양자 시뮬레이션에 쓰였다. BOB은 모양을 다듬은 초고속 레이저 펄스로 원자·분자의 양자 상태를 조작하는 양자 제어 장치이고, EVE는 광 미세 트랩에 잡은 루비듐 원자 하나를 큐비트(양자 정보의 기본 단위)로 삼아 초고속으로 제어하는 장치다. 그 밖에 펌프–프로브 분광기와 테라헤르츠 분광·방출 현미경을 운영한다.[^research] 물리학과는 교수의 연구 관심사를 중성 원자 양자컴퓨팅, 양자 제어, 테라헤르츠 분광과 광학으로 적고, 교수가 KAIST institute for optical science and technology(KI-OST)의 테라헤르츠 공동 연구실을 운영한다고 적는다.[^physics]

첫 번째 갈래는 **리드버그 원자로 푸는 최적화 문제**다. 연결망에서 서로 이웃하지 않는 점을 가장 많이 고르는 최대 독립 집합 문제처럼 계산이 어려운 조합 최적화 문제를, 원자 배열의 바닥 상태(에너지가 가장 낮은 상태)로 바꿔 푸는 방법을 연구한다. 보조 원자로 멀리 떨어진 원자를 잇는 「양자 전선」 방식을 3차원 원자 배열에서 시험해 Nature Physics에 발표했고,[^p1] 3차원 입체 모양의 연결망을 평면 배열로 옮겨 풀었다.[^p2] 원자 연결망에 곱셈표를 프로그래밍하는 방식으로 작은 수의 소인수분해를 보였고,[^p3] 원자 실험 데이터를 고전 최적화 알고리즘의 출발점으로 쓰는 혼합 방법도 시험했다.[^p4] 연구실 첫 화면은 2024년 가을 연구 성과로 35의 소인수분해, 리드버그 HUBO(고차 이진 최적화) 프로그래밍, 양자 강화 담금질 모사를 든다.[^home]

두 번째 갈래는 **리드버그 원자 양자 시뮬레이션과 측정**이다. 원자 사이 상호작용을 조절해 자석 속 스핀 들뜸이 움직이는 방식을 흉내 냈고,[^p5] 보조 원자를 이용해 여러 원자의 양자 상태를 통째로 재구성하는 측정법을 제안했다.[^p6]

세 번째 갈래는 **광집게로 원자를 옮기는 기술**이다. 광집게로 원자를 던지고 다른 광집게로 받아 내는 실험을 보였고,[^p7] 원자를 빠르면서도 잃지 않고 먼 거리까지 옮기는 제어 방법을 개발했다.[^p8] 랩 소식에 따르면 원자 던지고 받기 실험은 New Scientist에 소개됐고, 같은 해 Nature Photonics 소식(제목 "Take me out to the ball game")도 랩 소식에 올라 있다.[^home]

## 주요 연구 주제

### 1. 리드버그 원자 양자 최적화

양자 전선, 플라톤 입체 그래프, 소인수분해, 양자 강화 담금질 모사.[^p1][^p2][^p3][^p4] 대표 논문 1–4.

### 2. 양자 시뮬레이션과 상태 측정

비등방 하이젠베르크 자석(방향에 따라 세기가 다른 원자 자석 간 상호작용 모형), 보조 원자 양자 단층 촬영(여러 번 측정해 양자 상태 전체를 되짚는 방법).[^p5][^p6] 대표 논문 5, 6.

### 3. 광집게 원자 이동

원자 던지고 받기, 단열 지름길 이동.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 논문 목록의 2021–2026년 학술지 논문 가운데 교수가 마지막 저자인 것에서 주제별로 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2022 | [Rydberg Quantum Wires for Maximum Independent Set Problems](https://doi.org/10.1038/s41567-022-01629-5) · Nature Physics | 가까운 미래 양자컴퓨터의 쓰임 하나는 계산이 어려운 조합 최적화 문제를 푸는 것이다. 리드버그 원자로 연결망의 최대 독립 집합(서로 이웃하지 않는 점을 가장 많이 고른 묶음)을 찾는 실험 방법을 제시했다. 보조 원자로 멀리 떨어진 큐비트를 잇는 「양자 전선」을 3차원 원자 배열에서 시험해, 평면으로 그릴 수 없거나 한 점이 여섯 점과 이어진 연결망의 해를 찾았다.[^p1] | 1저자 Minhyuk Kim, 마지막 저자 안재욱 |
| 2 | 2022 | [Finding the maximum independent sets of Platonic graphs using Rydberg atoms](https://doi.org/10.1103/prxquantum.3.030305) · PRX Quantum | 양자 전선으로 멀리 떨어진 원자를 이어, 정사면체·정육면체·정팔면체 모양의 3차원 연결망을 평면 원자 배열로 옮겨 구현했다. 원자 22개 미만의 작은 실험에서 각 연결망의 바닥 상태 스핀 배치를 확인했다.[^p2] | 1저자 Andrew Byun, 마지막 저자 안재욱 |
| 3 | 2024 | [Rydberg-atom experiment for the integer factorization problem](https://doi.org/10.1103/physrevresearch.6.023241) · Physical Review Research | 리드버그 원자 연결망에 이진 곱셈표를 프로그래밍해 바닥 상태가 인수분해 답들의 중첩이 되게 하고, 단열 양자 계산(조건을 아주 천천히 바꿔 답이 담긴 바닥 상태에 이르게 하는 방식)으로 6=2×3, 15=3×5, 35=5×7을 실험으로 풀었다. 현재 리드버그 양자컴퓨터로 규모를 키우는 데 따르는 한계도 논의했다.[^p3] | 1저자 Juyoung Park, 마지막 저자 안재욱 |
| 4 | 2025 | [Quantum-Enhanced Simulated Annealing Using Rydberg Atoms](https://doi.org/10.1002/qute.202500070) · Advanced Quantum Technologies | 고전 최적화 방법인 담금질 모사에 리드버그 원자 실험 데이터로 출발점을 주는 혼합 알고리즘(QESA)이 최대 독립 집합 문제에서 담금질 모사만 쓸 때보다 계산 시간 이점을 보였다. 개인용 컴퓨터로 하루 안에 다룰 수 있는 최대 연결망 크기도 추정했다.[^p4] | 1저자 Seokho Jeong, 마지막 저자 안재욱 |
| 5 | 2024 | [Realization of an extremely anisotropic Heisenberg magnet in Rydberg atom arrays](https://doi.org/10.1103/physrevx.14.011025) · Physical Review X | 리드버그 양자 시뮬레이터로, 스핀 들뜸(마그논)끼리의 상호작용이 들뜸이 옮겨 가는 세기보다 두 자릿수 큰 자석을 만들어 강하게 상관된 스핀 수송을 관찰했다. 가까운 들뜸들은 짝을 이뤘고, 단단히 묶인 짝은 멈춰 있고 느슨한 짝은 움직였다.[^p5] | 1저자 Kangheun Kim, 마지막 저자 안재욱 |
| 6 | 2023 | [Quantum tomography of Rydberg atom graphs by configurable ancillas](https://doi.org/10.1103/prxquantum.4.020316) · PRX Quantum | 여러 큐비트의 양자 상태를 재구성하려면 보통 큐비트 하나하나를 정밀하게 제어해야 한다. 상호작용을 연속으로 조절할 수 있는 보조 원자로 재구성에 충분한 측정을 만드는 방법을 제안했고, 리드버그 원자 배열에서 높은 충실도(목표 상태와 얼마나 같은지)로 상태를 재구성했다.[^p6] | 1저자 Kangheun Kim, 마지막 저자 안재욱 |
| 7 | 2023 | [Optical tweezers throw and catch single atoms](https://doi.org/10.1364/optica.480535) · Optica | 붙잡힌 채 끌려가는 원자 대신, 광집게로 던지고 받는 자유 비행 원자를 보였다. 40 µK의 차가운 루비듐 원자를 가속하는 광집게로 던져 초속 최대 0.65 m로 4.2 µm를 날게 한 뒤 감속하는 광집게로 받아, 94% 효율로 옮겼다. 날아다니는 양자 메모리로 쓰일 수 있다.[^p7] | 1저자 Hansub Hwang, 마지막 저자 안재욱 |
| 8 | 2025 | [Fast and reliable atom transport by optical tweezers](https://doi.org/10.1364/opticaq.546797) · Optica Quantum | 광집게로 원자를 옮길 때 기존 방식은 느리거나 진동 가열로 원자를 잃는다. 단열 지름길(STA, 천천히 바꾼 것과 같은 결과를 빠르게 얻는 제어) 방식의 광집게 경로로 두 지점 이동, 도중 속도 조절, 곡선 경로 이동을 빠르고 안정적으로 해내, 센티미터 규모의 먼 거리 이동에도 맞는 방법임을 보였다.[^p8] | 1저자 Sunhwa Hwang, 마지막 저자 안재욱 |

## 교수와 전문 분야

안재욱 교수는 서울대 물리학 학사(1992)·석사(1994)와 미국 미시간대 물리학 박사(2002)를 받았다. 미국 로스앨러모스 국립연구소 Director's Postdoctoral Fellow(2002–2004)를 거쳐 2004년부터 KAIST에서 조교수·부교수·교수로 일하고 있으며, 물리학과는 직위를 Professor / KAIST Endowed Chair Professor(석좌교수)로 적는다.[^physics]

논문으로 보면 전문 분야는 세 갈래다.

- **리드버그 원자 양자 최적화 계산**.[^p1][^p2][^p3][^p4]
- **리드버그 원자 양자 시뮬레이션과 상태 측정**.[^p5][^p6]
- **광집게 원자 배열 제어와 이동**.[^p7][^p8]

## 응용 분야

대표 논문과 연구 소개로 보면 중성 원자 양자컴퓨터, 조합 최적화와 암호 관련 계산 문제, 양자 메모리를 옮기는 동적 양자컴퓨팅 구조에 닿아 있다.[^home][^p1][^p3][^p7] 졸업생은 고려대·한국표준과학연구원(KRISS)·서울대·로스앨러모스 국립연구소·국방과학연구소·삼성전자 등에 있다.[^members]

## 구성원

2026년 10월 19일 랩 구성원 페이지 기준이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Sunhwa Hwang | 박사과정 | gtg3146@kaist.ac.kr | 8 |
| JuYoung Park | 박사과정 | idoru2222@kaist.ac.kr | 3, 4, 7 |
| Kangjin Kim | 박사과정 | axdw0987@kaist.ac.kr | 8 |
| Maynardo Pratama Soegianto | 박사과정 | maynardosoegianto@kaist.ac.kr | 8 |

## 졸업생과 이전 구성원

랩 구성원 페이지의 졸업생·이전 구성원과 학위 논문 제목, 랩이 적은 현재 소속이다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Seokho Jeong | Ph.D. | Korea University | Quantum Programming with Rydberg atoms |
| Hansub Hwang | Ph.D. | University of Wisconsin | Implementations and Applications of Atom Throw and Catch by Optical Tweezer |
| Kangheun Kim | Ph.D. | KRISS | Quantum computing and simulation with Rydberg atom arrays |
| Andrew Byun (Woojeong Byun) | Ph.D. (2024) | University of Innsbruck | Quantum technological application of the Rydberg atom graph |
| Minhyuk Kim | Ph.D. (2021) | Korea University | Implementations and Applications of Three-Dimensional Rydberg Atom Assemblies |
| Haeun Sun | M.S. (2021) |  | Holographic 3D imaging method for scalable Rydberg atom quantum computing |
| Yunheung Song | Ph.D. (2019) | KRISS | Ultrafast quantum gates for trapped neutral atom qubits |
| HanLae Jo | Ph.D. (2019) | SEMES Co. Ltd | Coherent control of neutral-atom qubit systems: robust control, leakage suppression, and entanglement generation |
| Woojun Lee | Ph.D. (2018) | Seoul National University | Formation and control of Rydberg atom arrays for quantum information processing |
| Heejeong Jeong | 연구조교수(2018/08/15–2019/02/28) | Associate Professor at University of Malaya |  |
| Hyosub Kim | Ph.D. (2017) | Los Alamos National Lab | Reconfigurable single-atom array for Rydberg atom quantum simulation |
| Geol Moon | 박사후연구원(2017/06–2017/12) | Assistant Professor at Chonnam National University |  |
| Han-gyeol Lee | Ph.D. (2016) | University of Kassel | Quantum control of cold alkali atoms by using hybrid temporal-spectral pulse shaping |
| Kyungtae Kim | 대학원생(2015/07–2017/06) |  |  |
| Daehoon Han | Ph.D. (2016) | Semiconductor R&D Center, Samsung Electronics Co., Ltd | Lattice vibrations of minimal and polarization dependence of material in a slit using terahertz waves |
| Kanghee Lee | Ph.D. (2013) | Agency for Defense Development | Fourier optical phenomena and applications using ultra-broadband terahertz waves |
| Minwoo Yi | Ph.D. (2012) | Agency for Defense Development | Terahertz wave generation from semiconductor thin films and its applications |
| Junwoo Cho | Ph.D. (2011) | Samsung Electronics Co., Ltd | Enhancement of magneto-optical trap of ytterbium atoms via optical repumping of triplet P-states |
| Youngchan Kim | Ph.D. (2011) | Lecturer (Assistant Professor) at University of Surrey (UK) | Development of high-speed, high-resolution, and polarization-sensitive terahertz spectroscopic techniques |
| Sangkyung Lee | Ph.D. (2010) | Agency for Defense Development | Analytical coherent controls of Alkali atoms in strong field regime |
| Kyeong-Jin Jang | Ph.D. (2010) | Samsung Electronics Co., Ltd | The study of coherent optical and acoustic phonons in correlated electron materials (CMR, multiferroic), |
| Jongseok Lim | Ph.D. (2011) | Imperial College London | Coherent Control in 2D Fourier Transform Spectroscopy |
| Heejae Jeong | 연구원(2014/04–10) |  |  |
| Hoang-Van DO | 프랑스 ENS 교환학생(2015/01–07) |  |  |

## 최근 논문 목록 (2021–2026)

랩 논문 목록의 2021–2026년 항목 26건이다. 사전 공개(preprint) 표기 항목은 랩 표기대로 실었다.[^papers]

**2026**

- Junwoo Jung and Jaewook Ahn. "Shots-to-Approximate-Solution Scaling in Neutral-Atom Quantum Optimization". *preprint (2026)*.
- Sunhwa Hwang, Hansub Hwang, JuYoung Park, and Jaewook Ahn. "Collision-Induced Entanglement in Two Flying Atoms". *preprint (2026)*.
- Maynardo P. Soegianto, JuYoung Park, and Jaewook Ahn. "Neutral-atom graph programming for combinatorial optimization problems: from hardware-native maximum independent set to Sudoku". *preprint (2026)*.
- Juyoung Park, Junwoo Jung, and Jaewook Ahn. "Quantum-Enhanced Deterministic Inference of k-Independent Set Instances on Neutral Atom Arrays". *arXiv:2602.05432 (2025)*.
- JuYoung Park, Jaewook Ahn, and Minhyuk Kim. "Quantum dynamics and correlations in interacting bilayer arrays of Rydberg atoms". *preprint (2025)*.

**2025**

- Kangjin Kim, Kangheun Kim, and Jaewook Ahn. "Blinking optical tweezers for atom arrangements". *Advanced Quantum Technologies, e500531 (2025)*.
- Seokho Jeong, JuYoung Park, and Jaewook Ahn. "Quantum-Enhanced Simulated Annealing Using Rydberg Atoms". *Advanced Quantum Technologies, e2500070 (2025)*.
- Hansub Hwang, Sunhwa Hwang, Jaewook Ahn, S. Yoshida, and J. Burgdorfer. "Impact-parameter selective Rydberg atom collision by optical tweezers". *J. Phys. B: At. Mol. Phys. 58, 115202 (2025)*.
- Sunhwa Hwang, Hansub Hwang, Kangjin Kim, Andrew Byun, Kangheun Kim, Seokho Jeong, Maynardo Pratama Soegianto, and Jaewook Ahn. "Fast and reliable atom transport by optical tweezers". *Optica Quantum 3, 64 (2025)*.

**2024**

- Andrew Byun, Seokho Jeong, and Jaewook Ahn. "Programming higher-order interactions of Rydberg atoms". *Physical Review A 110, 042612 (2024)*.
- Andrew Byun, Junwoo Jung, Kangheun Kim, Minhyuk Kim, Seokho Jeong, Heejeong Jeong, and Jaewook Ahn. "Rydberg-atom graphs for quadratic unconstrained binary optimization problems". *Advanced Quantum Technologies 2024, 2300398 (2024)*.
- Juyoung Park, Seokho Jeong, Minhyuk Kim, Kangheun Kim, Andrew Byun, Louis Vignoli, Louis-Paul Henry, Loic Henriet, and Jaewook Ahn. "Rydberg-atom experiment for the integer factorization problem". *Physical Review Research 6, 023241 (2024)*.
- Kangheun Kim, Fan Yang, Klaus Mølmer, and Jaewook Ahn. "Realization of an extremely anisotropic Heisenberg magnet in Rydberg atom arrays". *Physical Review X 14, 011025 (2024)*.
- Kangheun Kim, Minhyuk Kim, Juyoung Park, Andrew Byun, and Jaewook Ahn. "Quantum Computing Dataset of Maximum Independent Set Problem on King's Lattice of over Hundred Rydberg Atoms". *Scientific Data 11, 111 (2024)*.

**2023**

- Constantin Dalyac, Louis-Paul Henry, Minhyuk Kim, Jaewook Ahn, and Loïc Henriet. "Exploring the impact of graph locality for the resolution of the maximum-independent-set problem with neutral atom devices". *Physical Review A 108, 052323 (2023)*.
- Seokho Jeong, Minhyuk Kim, Minki Hhan, JuYoung Park, and Jaewook Ahn. "Quantum programming of the satisfiability problem with Rydberg atom graphs". *Physical Review Research 5, 043037 (2023)*.
- Kangheun Kim and Jaewook Ahn. "Quantum tomography of Rydberg atom graphs by configurable ancillas". *PRX Quantum 4, 020316 (2023)*.
- Minhyuk Kim, Jaewook Ahn, Yunheung Song, Jongchul Moon, and Heejeong Jeong. "Quantum computing with Rydberg atom graphs". *J. Kor. Phys. Soc. 82, 827 (2023)*.
- Hansub Hwang, Andrew Byun, Juyoung Park, Sylvain de Léséleuc, and Jaewook Ahn. "Optical tweezers throw and catch single atoms". *Optica 10(3), 401 (2023)*.
- Ignacio R. Sola, Vladimir S. Malinovsky, Jaewook Ahn, Seokmin Shin, and Bo Y. Chang. "Two-qubit atomic gates: Spatio-temporal control of Rydberg interaction". *Nanoscale 14, 4325 (2023)*.

**2022**

- Andrew Byun, Minhyuk Kim, and Jaewook Ahn. "Finding the maximum independent sets of Platonic graphs using Rydberg atoms". *PRX Quantum 3, 030305 (2022)*.
- Seokho Jeong, Xiao-Feng Shi, Minhyuk Kim, and Jaewook Ahn. "Rydberg wire gates for universal quantum computation". *Frontiers in Physics 10, 875673 (2022)*.
- Minhyuk Kim, Kangheun Kim, Jaeyong Hwang, Eun-Gook Moon, and Jaewook Ahn. "Rydberg Quantum Wires for Maximum Independent Set Problems". *Nature Physics 18, 755–759 (2022/06/20)*.

**2021**

- Daryl Ryan Chong, Minhyuk Kim, Jaewook Ahn, and Heejeong Jeong. "Machine learning identification of symmetrized base states of Rydberg atoms". *Frontiers of Physics 17, 12504 (2021/08/11)*.
- Yunheung Song, Minhyuk Kim, Hansub Hwang, Woojun Lee, and Jaewook Ahn. "Quantum simulation of Cayley-tree Ising Hamiltonians with three-dimensional Rydberg atoms". *Physical Review Research 3, 013286 (2021/03/29)*.
- Haeun Sun, Yunheung Song, Andrew Byun, Heejeong Jeong, and Jaewook Ahn. "Imaging three-dimensional single-atom arrays all at once". *Optics Express 29(3), 4082-4090 (2021/01/25)*.

## 소식과 행사

랩 첫 화면의 소식·행사 목록이다.[^home]

- Alumni, DAMOP Providence, 2026
- 2025/10/21-23 · KPS APEC QST FORUM
- 2025/02/05 · 세계 양자 과학 및 기술의 해 (International Year of Quantum Science and Technology), 한국 선포식, 과학기술회관
- 2024/08/19-23 · The 15th Asian International Seminar on Atomic and Molecular Physics, KAIST Fusion Hall
- 2024/01/10 · 한국물리학회 대전충남세종 지부학회, 공주대 자연과학대학 강당
- 2023/10/24-27 · KPS Focus Session for Tweezer trap systems
- 2023/08/08 · Introduction to Rydberg-atom quantum computer (in korean)
- 2023/05/04 · Nature Photonics, “Take me out to the ball game,”
- 2023/03/05-10 · APS March Meeting, Las Vegas (Minhyuk, Hansub, Andrew, Kangheun, Seokho)
- 2022/12/22 · Lasers used to throw and catch single atoms (New Scientist).
- 2022/12/12-15 · KOFST BrainLink 2022 - Quantum Information Science Strategy, Yeosu, Korea
- 2022/01/25 · Quantum simulation, among seven technologies to watch in 2022 (Nature).
- 2021/06/21-23 · AMP 2021
- 2021/05/09-14 · CLEO 2021, Online, (Minhyuk, Hansub)
- 2021/04/21-23 · KPS 2021 Spring, Online, (Kangjin, Seokho, Woojeong)
- 2020/11/04-06 · KPS 2020 Fall, Online, (Minhyuk, Woojeong)
- 2020/05/11-15 · CLEO 2020, Online, (Yunheung, Haeun)

## 연락과 위치

- 교수 이메일: jwahn@kaist.ac.kr, 전화 042-350-2546[^members][^physics]
- 위치: KAIST 자연과학동(E6-2) 3305호 (대전 유성구 대학로 291)[^members]

[^home]: 양자컴퓨팅 연구실 누리집 첫 화면 <http://qcl.kaist.ac.kr/index.php/Jaewook_Ahn%27s_Quantum_Computing_Lab> (2026-10-19 열람)
[^research]: 양자컴퓨팅 연구실 연구 페이지 <http://qcl.kaist.ac.kr/index.php/Research> (2026-10-19 열람)
[^members]: 양자컴퓨팅 연구실 구성원 페이지 <http://qcl.kaist.ac.kr/index.php/Members> (2026-10-19 열람)
[^papers]: 양자컴퓨팅 연구실 논문 목록 <http://qcl.kaist.ac.kr/index.php/Publications> (2026-10-19 열람)
[^physics]: KAIST 물리학과 교수 소개(안재욱) <https://physics.kaist.ac.kr/index.php?document_srl=304&mid=p_people1> (2026-10-19 열람)
[^p1]: M. Kim 외, J. Ahn, Nature Physics 18, 755-759 (온라인 2022-06-20). <https://doi.org/10.1038/s41567-022-01629-5> 초록 기준(출판사 논문 페이지).
[^p2]: A. Byun, M. Kim, J. Ahn, PRX Quantum 3, 030305 (온라인 2022-07-08). <https://doi.org/10.1103/prxquantum.3.030305> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: J. Park 외, J. Ahn, Physical Review Research 6, 023241 (온라인 2024-06-04). <https://doi.org/10.1103/physrevresearch.6.023241> 초록 기준.
[^p4]: S. Jeong, J. Park, J. Ahn, Advanced Quantum Technologies 8, e2500070 (온라인 2025-07-28). <https://doi.org/10.1002/qute.202500070> 초록 기준.
[^p5]: K. Kim, F. Yang, K. Mølmer, J. Ahn, Physical Review X 14, 011025 (온라인 2024-02-21). <https://doi.org/10.1103/physrevx.14.011025> 초록 기준.
[^p6]: K. Kim, J. Ahn, PRX Quantum 4, 020316 (온라인 2023-04-27). <https://doi.org/10.1103/prxquantum.4.020316> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: H. Hwang 외, J. Ahn, Optica 10, 401 (온라인 2023-03-09). <https://doi.org/10.1364/optica.480535> 초록 기준.
[^p8]: S. Hwang 외, J. Ahn, Optica Quantum 3, 64 (온라인 2025-01-30). <https://doi.org/10.1364/opticaq.546797> 초록 기준.

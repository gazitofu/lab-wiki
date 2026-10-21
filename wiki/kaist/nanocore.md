# 원자 수준 소자 시뮬레이션 연구실 (Atomic-Scale Device Simulation Lab)

**KAIST 전기및전자공학부 · 김용훈 교수**

- 분야: 비평형 제1원리 계산 이론(다공간 밀도범함수론, MS-DFT), AI 기반 전자구조 계산, 원자 수준 반도체 소자 설계(TCAD), 2차원 반데르발스 소자의 접촉·계면·결함, 새로운 양자 소자 원리(부성 저항), 에너지 소재 계산
- 대분야: 전기전자·반도체·광학, 물리·양자
- 태그: 제1원리 계산[^p2][^p3], 소자 설계 시뮬레이션[^theory][^p3], 2차원 소재[^p4][^p5][^p7], 과학·공학 AI[^p1], 차세대 트랜지스터·논리 소자[^p6][^devices], 수소 저장·운송[^p8]
- 홈페이지: <https://nanocore.kaist.ac.kr/>
- 근거와 출처: [NANOCORE 근거 페이지](nanocore-sources.md)

> 실험값 없이 양자역학 방정식만으로 원자 수준에서 계산해, 실리콘 다음 세대 반도체 소자가 어떻게 작동할지 미리 설계하는 연구실이다. 전압이 걸려 전류가 흐르는 상황을 원자 수준에서 계산하는 독자 이론을 만들고, AI로 이 계산을 빠르게 한다.[^home][^theory]

## 무엇을 연구하나

연구실은 기능성 양자 소재의 물리와, 이를 차세대 전자·에너지 소자로 구현하는 설계 원리를 원자 수준에서 이해하는 것을 목표로 한다. 이를 위해 비평형 양자 과정(전압이 걸려 전류가 흐르는 상태)의 전자구조 계산 이론과 방법을 만들고, 고성능 계산과 AI를 결합해 더 큰 규모로 넓힌다고 소개한다.[^overview]

첫 번째 갈래는 **계산 이론과 AI**다. 연구실의 바탕은 제1원리 계산(실험값 없이 양자역학 기본 방정식만으로 물질 성질을 계산하는 방법)이며, 그중 밀도범함수 이론(DFT, 전자 밀도로 물질의 에너지를 계산하는 방법)을 주로 쓴다. 연구실은 10년 넘는 노력으로 전류가 흐르는 열린 양자계를 다루는 다공간 밀도범함수론(MS-DFT)을 세웠고, 이를 표준 방법을 대신할 수 있는 관점으로 내세운다. 이를 바탕으로 차세대 반도체 소자의 TCAD(반도체 소자를 컴퓨터로 설계·시험하는 기술)를 원자 수준에서 가능하게 하는 연구를 하며, 그래핀 기반 2차원 이종접합 트랜지스터의 제1원리 소자 시뮬레이션을 처음 보였다고 적는다.[^theory] 대표 논문에서는 이 계산의 반복 계산 단계(SCF)를 신경망으로 줄이거나 건너뛰는 DeepSCF를 만들었고,[^p1] 전압이 걸린 전극 표면에 분자가 붙는 에너지를 계산하는 이론과,[^p2] 2차원 반도체에서 전자가 전극을 뚫고 지나가는 한계를 재는 방법을 만들었다.[^p3]

두 번째 갈래는 **2차원 소자의 원자 수준 설계**다. 연구실은 트랜지스터가 극도로 작아지면 금속 전극·절연막과의 경계면이 반도체 채널만큼 중요해진다고 보고, 원자 수준 시뮬레이션으로 이런 접촉의 성질을 밝히고 설계 규칙을 제시한다.[^devices] 대표 논문에서는 그래핀·질화붕소 적층 트랜지스터에서 전류가 오히려 줄어드는 현상의 원인을 찾았고,[^p4] 실험 연구진과 함께 질화붕소 속 결함을 짚어 냈으며,[^p5] 전력을 적게 쓰는 2차원 반도체 게이트 구조와,[^p6] 금속과 이황화몰리브데넘 사이의 깨끗한 접촉을 설명했다.[^p7]

세 번째 갈래는 **새로운 소자 원리와 소재**다. 연구실은 다치 논리 소자, 탄소·2차원 전자소자, 뉴로모픽 소자, 양자 DNA 염기서열 분석과 스핀 큐비트 같은 양자 소자, 태양전지·양자점 LED·촉매·배터리 같은 에너지 소자를 연구 대상으로 든다. 나노 경계면의 양자 상태가 전압에 따라 끊어지며 생기는 양자 혼성 부성 저항(전압을 높이는데 전류가 줄어드는 현상) 원리를 제안했다고 적는다.[^devices] 대표 논문에서는 상온에서 수소를 많이 저장하는 탄소 소재의 원리를 계산으로 밝혔다.[^p8]

연구실이 적은 진행 과제로는 SK하이닉스의 2차원 TMD 소자 응용 연구센터, 삼성전자 DS부문의 2차원 산화물 반도체 MOSFET 제1원리 TCAD 프레임워크 개발, 한국연구재단의 다공간 밀도범함수론 기반 비평형 멀티스케일 계산 방법론 개발과 반도체소자물리 온라인 R&D 플랫폼 과제가 있다.[^projects]

## 주요 연구 주제

### 1. 비평형 제1원리 계산 이론과 AI

DeepSCF, 비평형 흡착 에너지, 2차원 반도체 터널링 한계.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 2차원 소자의 원자 수준 설계

수직 그래핀 소자의 부성 저항, 질화붕소 결함, 고유전율 게이트, 반데르발스 접촉.[^p4][^p5][^p6][^p7] 대표 논문 4–7.

### 3. 에너지 소재

상온 수소 저장 탄소 소재.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 김용훈 교수가 교신저자(랩 표기 *)이거나 마지막 저자인 것에서 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2024 | [Convolutional network learning of self-consistent electron density via grid-projected atomic fingerprints](https://doi.org/10.1038/s41524-024-01433-0) · npj Computational Materials | DFT 계산에서 전자 밀도를 반복 계산으로 맞춰 가는 단계(자기 일관 계산)를 줄이거나 건너뛰는 방법은 중요한 문제다. 원자들의 밀도를 단순히 더한 초기값과 최종 전자 밀도 사이의 관계를 3차원 합성곱 신경망으로 학습하는 DeepSCF를 만들고, 다양한 결합을 가진 작은 유기 분자로 학습시켜 탄소나노튜브 기반 DNA 염기서열 분석 장치 모형에서 효과를 보였다.[^p1] | 1저자 Ryong-Gyu Lee, 교신 김용훈 |
| 2 | 2024 | [Ab initio theory of the nonequilibrium adsorption energy](https://doi.org/10.1038/s41524-024-01242-5) · npj Computational Materials | 분자가 전극 표면에 붙는 흡착 에너지는 전압이 걸리지 않은 평형 상태에서만 정의돼 있었다. 다공간 밀도범함수론 안에서 전압이 걸린 경계면의 전기적 엔탈피를 계산하는 이론을 세워 비평형 흡착 에너지를 구했고, 물-금과 물-그래핀 경계면에서 전극에 따라 물 분자 배치가 전압에 다르게 반응함을 보였다.[^p2] | 1저자 Juho Lee, 교신 김용훈 |
| 3 | 2026 | [Ab initio transfer length method simulations of tunneling limits in 2D semiconductors](https://doi.org/10.1038/s41524-026-02101-1) · npj Computational Materials | 2 nm 이하 공정으로 갈수록 전극 접촉 저항의 양자 한계를 알아야 한다. 단층 이황화몰리브데넘에 스칸듐·은·금·팔라듐 전극을 위·옆으로 붙인 소자를 제1원리로 계산해, 채널이 10 nm보다 짧으면 직접 터널링이, 길면 열전자 방출(열에너지를 얻은 전자가 장벽을 넘어가는 현상)이 지배한다는 전환을 찾았다. n형에는 일함수(금속에서 전자 하나를 떼어 내는 데 드는 에너지)가 낮은 금속 윗면 접촉이, p형에는 일함수가 높은 금속 옆면 접촉이 좋다는 지침도 냈다.[^p3] | 1저자 Tae Hyung Kim, 마지막 저자 김용훈 |
| 4 | 2022 | [Gate-versus defect-induced voltage drop and negative differential resistance in vertical graphene heterostructures](https://doi.org/10.1038/s41524-022-00731-9) · npj Computational Materials | 그래핀/질화붕소(전기가 통하지 않는 2차원 물질)/그래핀을 수직으로 쌓은 트랜지스터를 비평형 제1원리 방법으로 계산해, 전압을 높이는데 전류가 줄어드는 부성 저항이 게이트에 의한 두 그래핀의 에너지 어긋남뿐 아니라 질화붕소 속 결함 준위의 이동으로도 생길 수 있음을 보였다. 결함이 어느 층에 있느냐에 따라 소자 특성이 크게 달라졌다.[^p4] | 1저자 Tae Hyung Kim, 교신 김용훈 |
| 5 | 2024 | [Characterizing Defects Inside Hexagonal Boron Nitride Using Random Telegraph Signals in van der Waals 2D Transistor](https://doi.org/10.1021/acsnano.4c06929) · ACS Nano | 질화붕소로 감싼 이황화몰리브데넘 트랜지스터의 저주파 잡음을 극저온에서 재서, 전류가 두 값 사이를 오가는 랜덤 텔레그래프 신호가 질화붕소 안의 한 종류 결함에서 나온다는 것을 확인했다. 다공간 밀도범함수론 계산으로 그 결함이 붕소 자리에 들어간 탄소 원자임을 밝혔다.[^p5] | 1저자 Zhujun Huang, 교신 김용훈·Davood Shahrjerdi |
| 6 | 2024 | [High-κ Dielectric (HfO2)/2D Semiconductor (HfSe2) Gate Stack for Low-Power Steep-Switching Computing Devices](https://doi.org/10.1002/adma.202312747) · Advanced Materials | 2차원 반도체 HfSe2를 플라즈마로 산화해 그 위에 HfO2 절연막을 만들어, 원자 수준으로 깨끗한 경계면을 얻었다. 계산으로 산소가 셀레늄 자리를 장벽 없이 차지하며 한 층씩 산화된다는 원리를 밝혔고, 트랜지스터는 이상에 가까운 61 mV/dec의 문턱 아래 기울기(트랜지스터가 꺼진 상태에서 켜진 상태로 얼마나 가파르게 바뀌는지 나타내는 값)를, 충격 이온화 트랜지스터는 상온에서 3.43 mV/dec를 보였다.[^p6] | 1저자 Taeho Kang, 교신 Jongwook Jeon·김용훈·Sungjoo Lee |
| 7 | 2021 | [Origins of genuine Ohmic van der Waals contact between indium and MoS2](https://doi.org/10.1038/s41699-020-00191-z) · npj 2D Materials and Applications | 인듐을 낮은 에너지로 증착하고 기판을 약 100 K로 식혀 이황화몰리브데넘과 깨끗한 반데르발스 접촉(화학 결합 없이 약한 힘으로 맞닿은 접촉)을 만들었고, 2.4–300 K에서 옴 접촉(전압에 비례해 전류가 흐르는 접촉)에 가까운 전류 특성을 보였다. 계산으로 인듐과 이황화몰리브데넘의 상태가 섞이며 생긴 띠틈(전자가 가질 수 없는 에너지 구간) 속 상태가 그 원인임을 밝혀, 페르미 준위 고정(금속을 바꿔도 접촉 장벽이 거의 변하지 않는 현상)을 피하는 접촉 설계 방향을 제시했다.[^p7] | 1저자 Bum-Kyu Kim, 교신 김용훈·Myung-Ho Bae |
| 8 | 2023 | [Amorphized defective fullerene with a single-atom platinum for room-temperature hydrogen storage](https://doi.org/10.1002/aenm.202300041) · Advanced Energy Materials | 단일 원자 백금을 붙인 비정질 결함 풀러렌은 결정 풀러렌보다 표면적과 기공이 크게 늘어, 상온 압력 변화만으로 무게 대비 6.8 wt%, 부피 대비 64.9 kg/m³의 수소를 되풀이해 저장했다. 계산으로 휘어진 탄소 구조를 지키는 것이 수소를 빠르게 옮기는 열쇠임을 밝혔다.[^p8] | 1저자 Heebin Lee, 교신 김용훈·Jeung Ku Kang |

## 교수와 전문 분야

김용훈 교수는 서울대 물리학과 학사(1995), 미국 일리노이대 어배나-섐페인 물리학 박사(2000, 지도교수 Richard M. Martin)를 받았다. 독일 뮌헨공대 훔볼트 펠로(2000–2002), 미국 칼텍 박사후연구원(2002–2004), 고등과학원 계산과학부 조교수(2004–2006), 서울시립대 신소재공학과 조교수(2006–2010)를 거쳐 2010년부터 KAIST 전기및전자공학부·EEWS대학원 교수다. 2023년부터 EDISON 2.0 반도체물리 센터장을 맡고 있고, 한국물리학회 펠로이며 IOP Journal of Physics: Materials 편집위원이다.[^prof]

랩이 적은 수상으로는 S-Oil 우수학위논문 지도교수상 IT 분야 대상(2021), 나노코리아 연구혁신상 장관상(2017), 한국연구재단 EDISON 시뮬레이션 소프트웨어 개발 우수성과상(2015) 등이 있다.[^prof] 연구실은 자체 개발 프로그램을 공개 저장소(GitHub YHKlab)에 둔다.[^facilities]

논문으로 보면 전문 분야는 세 갈래다.

- **비평형 밀도범함수 이론과 AI 가속 전자구조 계산**.[^p1][^p2][^p3]
- **2차원 반도체 소자의 접촉·계면·결함 원자 수준 해석**.[^p4][^p5][^p6][^p7]
- **에너지 소재의 제1원리 해석**.[^p8]

## 응용 분야

대표 논문과 과제로 보면 차세대 반도체 소자의 컴퓨터 설계(TCAD), 2차원 반도체 트랜지스터의 접촉과 게이트 설계, 저전력 논리 소자, 수소 저장 소재에 닿아 있다.[^p3][^p6][^p8][^projects] 연구실은 2025년 SK하이닉스 KAIST 클러스터 산학과제와 삼성전자 DS부문 전략산학과제에 선정됐다고 적는다.[^home] 졸업생은 삼성전자, SK하이닉스, 삼성SDI, 한국과학기술정보연구원 등과 충북대 조교수로 진출했다.[^alumni]

## 구성원

2026년 10월 20일 랩 Current Members 페이지 기준이다. 연구 관심사와 이메일은 랩이 적은 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Lee Ryong Gyu | 박사후연구원 | 2D van der Waals Transistor, Machine learning, Optoelectronic devices | ronggyulee@kaist.ac.kr | 1, 2, 4, 5, 6 |
| Seunghyun Yu | 박사과정 | 2D van der Waals Transistor, Multi-scale device simulation | littleyu@kaist.ac.kr |  |
| Jeong Won Lee | 박사과정 | Multi-scale device simulation, perovskite | jeongwon.lee@kaist.ac.kr | 5 |
| Minsu Jeong | 박사과정 | 2D van der Waals Transistor, Machine learning, Quasi-Fermi level | minsu.jeong@kaist.ac.kr |  |
| Hyeonjun Kang | 석사과정 |  | wns1616khj1616@kaist.ac.kr |  |
| Joonho Park | 박사후연구원 | Catalytic Reaction such as CO2 reduction, Oxygen reduction reactions, Molecular Dynamics based on Artificial Intelligence Potential. | hopefulp@kaist.ac.kr | 6, 8 |

## 졸업생과 이전 구성원

랩 Alumni 게시판의 이름, 과정·기간, 랩이 적은 현재 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Rajput Kaptansinh suryabalisinh | 박사후연구원 (2022.2~2025.12) |  |
| Hyeonwoo Yeo | 박사 (2017.6~2025.9) |  |
| Song Ji Yoon | 석사 (2022.8-2025.2) | SK Hynix |
| Jae Eun Kim | 석사 (2022.2 - 2024.8) |  |
| Tae Hyung Kim | 박사 (2016.9~2024.2) | Samsung Electronics |
| Yumin Song | 석사 (2020.03-2022.02) | Samsung Electronics |
| Juho Lee | 박사 (2016.9~2020.8), 박사후연구원 (2020.9~2021.11) | Samsung Electronics |
| Jun Seong Lee | 석사 (2019.3~2021.2) | Micro INSPECTION |
| Min Jong Noh | 박사 (2017.02-2021.08) | Samsung SDI |
| Seongjae Byeon | 석사 (2017.3~2019.2) | Samsung Electronics (R&D) |
| Hu Sung Kim | 박사 (2011.3~2018.8) | Senior Researcher, KISTI |
| Dongjae Shin | 석사 (2016.3~2018.2) | Ph. D. Course, Postech |
| Han Seul Kim | 박사 (2011.3-2017.2) | Assistant Professor in Chungbuk National University |
| Muhammad Sufyan Ramzan | 석사 (2015.3~2017.2) | Research assistant, Universität Leipzig |
| Kwan Ho Ko | 석사 (2013.9~2016.9) |  |
| Yoon Su Shim | 석사 (2014.3~2016.2) | Ph.D. Course, KAIST |
| Seong Sik Kim | 석사 (2013.3~2015.2) | SK Hynix (R&D) |
| Joon-Ho Lee | 박사후연구원 (2021.3~2024.2) | Lecturer in Chungju National University |
| Junga Ryou | 연구원 (2018-2019) | Virtual Lab |
| Soungmin Bae | 연구원 (2018~2019) | Tokyo Institude of Technology, Japan |
| Muhammad Ejaz Khan | 연구원 (2016~2019) | Professor of National University of Technology, Pakistan |
| Lamjed Debbichi | 연구원 (2015~2018) | LPCT ／ Physique et Chimie Théoriques - Université de Lorraine |
| Jung Hoon Park | 학사 | Ph.D. course, KAIST |
| Hye Min Lee | 학사 | Samsung Mobile Display |
| Gain Lee | 공동 지도 (Prof. J. K. Kang) | Postdoctoral researcher, Stanford, USA |
| Kyeong Eun Kwon | 공동 지도 (Prof. G. S. Hwang) | Postdoctoral researcher, Univ. of Texas, USA |
| Yong Ju Kang | 공동 지도 (Prof. K. J. Chang, KAIST) | Research staff, Samsung |
| Joongoo Kang | 공동 지도 (Prof. K. J. Chang, KAIST) | Research staff, Quantum Simulation Group, Lawrence Livermore National Laboratory |
| Seungkyu Min | 공동 지도 (Prof. K. S. Kim, POSTECH) | Assistant Professor, Department of Chemistry, UNIST |
| Wooyoun Kim | 공동 지도 (Prof. K. S. Kim, POSTECH) | Associate Professor, Department of Chemistry, KAIST |
| Chris George | 공동 지도 (Prof. W. A. Goddard, Caltech) | Ph.D. course, Northwestern Univ., USA |
| Yuki Matsuda | 공동 지도 (Prof. W. A. Goddard, Caltech) | Research staff, GE Nuclear-Hitachi, Japan |
| Santiago Solares | 공동 지도 (Prof. W. A. Goddard, Caltech) | Associate Professor, George Washington University |

## 최근 논문 목록 (2021–2026)

랩 Articles & Patents 게시판의 2021년 이후 논문이다. 저자 이름 뒤 *는 교신저자를 뜻하는 랩 표기다.[^papers]

**2026**

- Yong-Hoon Kim, Han Seul Kim, Juho Lee, Tae Hyung Kim, and Ryong-Gyu Lee. "Toward ab initio technology computer-aided design". *Current Applied Physics, 92, 148–161 (2026)*.
- Inseong Lee, Joonho Park, Seungsun Yoo, Seunghyun Yu, Mingu Kang, Seohak Park, Min Kyu Lee, Hyeongjin Lim, Dongyoung Kim, Kunwoo Roh, Sejin Kim, Kihyuk Kim, Wonbae Ahn, Kibum Kang, Yong-Hoon Kim, and Sung-Yool Choi. "Barrier-Assisted Plasma Doping for Spatially Selective Resistance Engineering in MoS₂ Transistors". *Advanced Materials, 38(55), e74389 (2026)*.
- Tae Hyung Kim, Juho Lee, Yong-Hoon Kim. "Ab initio transfer length method simulations of tunneling limits in 2D semiconductors". *npj computational materials, 12, 283 (2026)*.

**2025**

- Taeho Kang, Joonho Park, Seung Yong Lee, Hanggyo Jung, Jongwook Jeon, Yong-Hoon Kim, Sungjoo Lee. "High-κ dielectric van der Waals integration on 2D semiconductors for three-dimensional complementary logic systems". *Nature Communication, 16 (2025)*.
- Seungjae Lee, Heeseung Lee, Joonho Park, Hyeonwoo Yeo, Junho Kim, Changjo Kim, Hyojun Kim, Seyun Lee, Jihyung Lee, Yun Hoo Kim, Seungbok Lee, Seonju Jeong, Wu Bin Ying, Ryong-Gyu Lee, Yong-Hoon Kim, Jung-Yong Lee. "Lead-Free Tin-Based Perovskite LEDs Toward Rec. 2020: Organic Anion Coordination for Oxidation Suppression". *Advanced Science , e11006 (2025)*.
- Donguk Kim, Hyemin Lee, Minwoo Song, Jongwoo Nam, Changjun Lee, Jaeyong Woo,Juntae Jang, Minsu Jeong, Hyeonwoo Yeo, Ryong-Gyu Lee, Eunje Park, Hyeonmin Choi,Yong- Hoon Kim, Keehoon Kang, Takhee Lee. "Enhanced gating efficiency in vertical mixed molecular transistors with deep orbital level". *Science Advances, 11(25) (2025)*.
- Noki Lee, Jeongwon Lee, Sehoon Oh, Ryong-Gyu Lee, Hyeonwoo Yeo, Yong-Hoon Kim, and Jaichan Lee. "Design of Self-Assembled Monolayer in Tungsten Diselenide Bilayer for Exciton Dissociation". *ACS Nano, 19(10), 9779-9787 (2025)*.

**2024**

- Yong-Hoon Kim and Ryong-Gyu Lee. "A New Direction for First-Principles Device Simulations". *IEEE Nanotechnology Magazine, 18(6), 1-7 (2024)*.
- Ryong-Gyu Lee, and Yong-Hoon Kim\*. "Convolutional network learning of self-consistent electron density via grid-projected atomic fingerprints". *npj Computational Materials, 10, 248 (2024)*.
- Zhujun Huang, Ryong-Gyu Lee, Edoardo Cuniberto, Jiyoon Song, Jeongwon Lee, Abdullah Alharbi, Kim Kisslinger, Takashi Taniguchi, Kenji Watanabe, Yong-Hoon Kim\*, and Davood Shahrjerdi\*. "Characterizing Defects Inside Hexagonal Boron Nitride Using Random Telegraph Signals in van der Waals 2D Transistor". *ACS Nano, 18, 28700–28711 (2024)*.
- Taeho Kang, Joonho Park, Hanggyo Jung, Haeju Choi, Sang-Min Lee, Nayeong Lee, Ryong-Gyu Lee, Gahye Kim, Seung-Hwan Kim, Hyung-jun Kim, Cheol-Woong Yang, Jongwook Jeon\*, Yong-Hoon Kim\*, Sungjoo Lee\*. "High-κ Dielectric (HfO2)/2D Semiconductor (HfSe2) Gate Stack for Low-Power Steep-Switching Computing Devices". *Advanced Materials, 36, 2312747 (2024)*.
- Juho Lee, Hyeonwoo Yeo, Ryong-Gyu Lee and Yong-Hoon Kim\*. "Ab initio theory of the nonequilibrium adsorption energy". *npj Computational Materials, 10, 60 (2024)*.

**2023**

- Yongmin Shin, Hyungwoo Suh, Byoung-Hwa Kwon, Joonho Park, Hyunsu Cho, Chul Woong Joo, Sukyung Choi, Jin-Wook Shin, Chan-mo Kang, Dae Hyun Ahn, Won Jun Lee, Yong-Hoon Kim, Junho Jang\* and Byeong-Soo Bae\*. "Environmentally stable luminescent perovskite nanocrystals passivated and encapsulated by siloxane hybrids enabling reliable color-converted organic light-emitting diodes". *Chemical Engineering Journal, 474, 145889 (2023)*.
- Soungmin Bae, Tae-Young Jeong, Hannes Raebiger, K. J. Yee\* and Yong-Hoon Kim\*. "Localized coherent phonon generation in monolayer MoSe2 from ultrafast exciton trapping at shallow traps". *Nanoscale Horizons, 8, 1282-1287 (2023)*.
- Heebin Lee, Dong Gyu Park, Joonho Park, Yong-Hoon Kim\* and Jeung Ku Kang\*. "Amorphized defective fullerene with a single-atom platinum for room-temperature hydrogen storage". *Advanced Energy Materials, 13, 2300041 (2023)*.

**2022**

- Yejin Kim, Soungmin Bae, Joohee Park, Trang Thi Thu Nguyen, Hye Ri Jung, William Jo, Yong-Hoon Kim, Hannes Raebiger and Seokhyun Yoon\*. "Parallel alignment of methylammonium cations in an orthorhombic CH3NH3PbCl3 single crystal observed by polarized micro-Raman scattering spectroscopy". *Chemistry of Materials, 34, 2972-2980 (2022)*.
- Jihyun Kim, Joonho Park, Yong-Hoon Kim\* and William Jo\*. "Improvement of Open-Circuit Voltage Deficit via Pre-Treated NH4+ Ion Modification of Interface between SnO2 and Perovskite Solar Cells". *Small, 18, 2204173 (2022)*.
- Soungmin Bae\*, Kana Matsumoto, Hannes Raebiger, Ken-ichi Shudo, Yong-Hoon Kim, Ørjan Sele Handegård, Tadaaki Nagao, Masahiro Kitajima, Yuji Sakai, Xiang Zhang, Robert Vajtai, Pulickel Ajayan, Junichiro Kono, Jun Takeda\*, Ikufumi Katayama\*. "K-point longitudinal acoustic phonons are responsible for ultrafast intervalley scattering in monolayer MoSe2". *Nature communications, 13, 4279 (2022)*.
- Juho Lee, Muhammad Ejaz Khan and Yong-Hoon Kim\*. "Quantum hybridization negative differential resistance from non-toxic halide perovskite nanowire heterojunctions and its strain control". *Nano Convergence, 9, 25 (2022)*.
- Tae Hyung Kim, Juho Lee, Ryong-Gyu Lee, and Yong-Hoon Kim\*. "Gate-versus defect-induced voltage drop and negative differential resistance in vertical graphene heterostructures". *Npj Computational Materials, 8, 50 (2022)*.
- Hanbyeol Jang, Yumin Song, Yongwook Seok, Heungsoon Im, Tae Hyung Kim, Joo-Hyoung Lee, Yong-Hoon Kim\*, and Kayoung Lee\*. "Zero power infrared sensing in 2D/3D-assembled heterogeneous graphene/In/InSe/Au". *Nanoscale, 14, 3004 (2022)*.
- Hyeonje Son, Juho Lee, Tae Hyung Kim, Seunghuck Choi, Haeju Choi, Yong-Hoon Kim\*, Sungjoo Lee\*. "Emergence of multiple negative differential transconductance from a WSe2 double lateral homojunction platform". *Applied Surface Science, 581, 152396 (2022)*.

**2021**

- Hyeong-Yong Hwang, Sehyuk Lee, Yong-Hoon Kim, Farman Ullah, Chinh Tam Le, Yong Soo Kim, Ki-Ju Yee Christopher J Stanton and Young-Dahl Jho. "Shear-strain-mediated photoluminescence manipulation in two-dimensional transition metal dichalcogenides". *2D Materials, 9, 015011 (2021)*.
- Seunghwan Seo, Je-Jun Lee, Ryong-Gyu Lee, Tae Hyung Kim, Maksim Andreev, Sangyong Park, Kil-Su Jung, Seyong Oh, Sooyoung Jung, Ho-Jun Lee, Hyun-Kyu Lee, Ki Seok Kim, Geun Yong Yeom, Yong-Hoon Kim\*, and Jin-Hong Park\*. "An optogenetics-Inspired Flexible van der Waals Optoelectronic Synapse and its Applicaltion to an Convolutional Neural Network". *Advanced Materials, 33, 2102980 (2021)*.
- Da-Eun Yoon, Juho Lee, Hyeonwoo Yeo, Junga Ryou, Young Kuk Lee, Yong-Hoon Kim\*, and Doh C. Lee\*. "Atomistics of Asymmetric Lateral Growth of Colloidal Zincblende CdSe Nanoplatelets". *Chemistry of Materials, 33, 4813-4820 (2021)*.
- Soungmin Bae, William Espinosa-García, Yoon-Gu Kang, Noriyuki Egawa, Juho Lee, Kazuaki Kuwahata, Mohammad Khazaei, Kaoru Ohno, Yong-Hoon Kim, Myung Joon Han, Hideo Hosono, Gustavo M. Dalpian,\* and Hannes Raebiger\*. "MXene Phase with C3 Structure Unit: A Family of 2D Electrides". *Advanced Functional Materials, 31, 2100009 (2021)*.
- Soungmin Bae\*, Yoon-Gu Kang, Mohammad Khazaei\*, Kaoru Ohno, Yong-Hoon Kim, Myung Joon Han, Kee Joo Chang and Hannes Raebiger\*. "Electronic and magnetic properties of carbide MXenes-the role of electron correlations". *Materials Today Advances, 9, 100118 (2021)*.
- Bum-Kyu Kim, Tae-Hyung Kim, Dong-Hwan Choi, Hanul Kim, Kenji Watanabe, Takashi Taniguchi, Heesuk Rho, Ju-Jin Kim, Yong-Hoon Kim\* & Myung-Ho Bae\*. "Origins of genuine Ohmic van der Waals contact between indium and MoS2". *NPJ 2D Materials and Applications, 5, 1-10 (2021)*.
- Hongyue Jing, Hyeonwoo Yeo, Benzheng Lyu, Junga Ryou, Seunghyuk Choi, Jin-Hong Park, Byoung Hun Lee, Yong-Hoon Kim, and Sungjoo Lee\*. "Modulation of the Electronic Properties of MXene (Ti3C2Tx) via Surface-Covalent Functionalization with Diazonium". *ACS Nano, 15(1), 1388-1396 (2021)*.
- Nikolai Tsvetkov, Muhammad Ejaz Khan, Byeong Cheul Moon, Yong-Hoon Kim\*, and Jeung Ku Kang\*. "Strain-induced Metallization and Defect Suppression at Zipper-like Interdigitated Atomically Thin Interfaces Enabling High-Efficiency Halide Perovskite Solar Cells". *ACS Nano, 15(1), 1805-1816 (2021)*.

## 특허와 기술이전

같은 게시판의 2021년 이후 특허와 기술이전 항목이다.[^papers]

- 2023 · 파일 정렬 시스템 (발명자 김용훈, 이준호, 박준호; 번호 국내특허출원, KR, 출원번호 10-2023-0016093)
- 2021 · First-principles-derived effective mass approximation simulation method for the accurate description of optical properties of 1D and 2D nanostrcutreus and the system therof (발명자 김용훈; 번호 해외특허 출원, 출원번호 : 17/522,424)
- 2021 · 1차원 및 2차원 양자 나노구조의 광 특성의 정확한 전산 모사를 위한 제1원리 기반의 유효질량 근사 시뮬레이션 방법 및 그 시스템 (발명자 김용훈; 번호 국내특허 출원, 출원번호 10-2021-0137711)
- 2021 · 양자 나노 구조의 광특성의 정확한 전산모사를 위한 제1원리 기반 유효질량 근사 시뮬레이션 방법 (발명자 김용훈; 번호 기술이전, 업체명: 버추얼랩, 계약일 2021.4.21, 계약기간 ~2025. 11. 10)
- 2021 · 다전극 전자 여기를 통한 나노 소자의 비평형 전자구조 시뮬레이션 방법 및 그 장치 (발명자 김용훈, 김한슬, 이주호; 번호 국내특허, KR, 10-2283109)

## 연구 과제

랩 Projects 페이지의 진행 중 과제와 기간, 지원 기관이다.[^projects]

- 2D TMD 소자 응용 연구센터 (기간 2025~현재; 지원 SK하이닉스)
- 2차원 산화물 반도체 MOSFET 제1원리 기반 TCAD 프레임워크 개발 (기간 2025~현재; 지원 삼성전자DS)
- 다공간 밀도범함수론 기반 비평형 멀티 스케일 계산 방법론의 개발 (기간 2023~현재; 지원 한국연구재단)
- 반도체소자물리 온라인 R&D 플랫폼 구축 및 활용 활성화 (기간 2023~현재; 지원 한국연구재단)

## 수상

교수 페이지에 적힌 수상이다.[^prof]

- 2021.12 · S-Oil Best PhD Thesis Advisor Award: IT Field Grand Prize (KoreaAcademy of Sciences and Technology & S-Oil Science and Culture Foundation)
- 2017.07 · Nano Korea Research Innovation Award – Minister Award (Ministry of Science, ICT, & Future Planning)
- 2016.10 · KAIST Research, Education, Development, & Business Project Outstanding Achievement (KAIST)
- 2015.03 · Outstanding Achievement Award - EDISON Simulation S/W Development (National Research Foundation)
- 2011.10 · Outstanding Alumni Award (Korea Institute for Advanced Study)
- 2007.11 · Hynix Best Lecture Note Award (Korean Society for Engineering Education)
- 2006.08 · Best Oral Presentation Award (IEEE Nanotechnology Materials and Devices Conference)
- 2002 Fall · IPAM fellowship for the "Mathematics in Nanoscale Science and Engineering" program (Institute for Pure and Applied Mathematics, UCLA, U.S.)
- 2001-2002 · Humboldt Fellowship (Humboldt Foundation, Germany)

## 소식

랩 News 게시판의 2021년 이후 소식이다.[^news]

- 2026-02-23 · 이룡규 학생 박사과정 졸업
- 2025-08-31 · 여현우 학생 박사과정 졸업
- 2025-07-06 · 정민수 통합과정 학생 제16회 KIAS CAC Summer School on Aritifical Intelligence & Parallel Computi…
- 2025-07-06 · 유승현 박사과정 학생 제16회 KIAS CAC Summer School on Aritifical Intelligence & Parallel Computi…
- 2024-12-05 · 삼성전자 DS부문 기술산학 과제 선정
- 2024-11-21 · 여현우 박사과정 학생 한국물리학회 2024가을학술대회 우수 구두발표상 수상
- 2024-11-21 · 송지윤 석사과정 학생 한국물리학회 2024가을학술대회 우수 포스터발표상 수상
- 2024-02-14 · 김태형 학생 박사과정 졸업
- 2023-12-01 · Stephan Roche 교수님(스페인 ICREA) 방문 및 KAIST Distinguished Lecture 수행.
- 2023-08-11 · 여현우 박사과정 학생 Samsung Global Technology Symposium INSPIRE Award 수상
- 2023-08-11 · 김재은 석사과정 학생 Samsung Global Technology Symposium INSPIRE Award 수상
- 2023-05-04 · Kieron Burke 교수님(미국 University of California at Irvine)이 방문 및 Distinguished Lecture 수…
- 2023-04-13 · 연구실 최신 연구 결과 KAIST Breakthroughs 2023년 봄호 소개
- 2023-02-28 · 김한슬 박사 충북대 조교수 임용
- 2022-05-24 · 이룡규 박사과정 학생 한국물리학회 2022봄학술대회 우수 구두발표상 수상
- 2022-02-08 · 이주호 박사 제29회 한국반도체학술대회에서 KSC 2021 최우수논문상 수상
- 2021-12-12 · 이주호 박사 제11회 에쓰-오일 우수학위논문상 IT 분야 대상 수상
- 2021-12-03 · 이룡규 박사과정 학생 한국물리학회 2021가을학술대회 우수 구두발표상 수상
- 2021-12-03 · 김태형 박사과정 학생 한국물리학회 2021가을학술대회 우수 구두발표상 수상
- 2021-08-31 · 노민종 학생 박사과정 졸업
- 2021-04-05 · KAIST Research Highlights of 2020 선정
- 2021-02-20 · 이준성 학생 석사과정 졸업
- 2021-02-15 · 유동석 박사 삼성전자 LSI 정규직 연구원 취업
- 2021-02-01 · 박준호 박사 박사후 연구원 합류

## 연락과 위치

- 교수실: KAIST 전기및전자공학부 E3-2동 6209호[^prof]
- 연구실: E3-2동 6210호[^members]

[^home]: 연구실 누리집 첫 화면 <https://nanocore.kaist.ac.kr/> (2026-10-20 열람)
[^overview]: Research Overview 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub2_0> (2026-10-20 열람)
[^theory]: Theory & Computation 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub2_1> (2026-10-20 열람)
[^devices]: Next-Generation Devices 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub2_2> (2026-10-20 열람)
[^projects]: Projects 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub2_4> (2026-10-20 열람)
[^papers]: Articles & Patents 게시판 1–3쪽 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (2026-10-20 열람)
[^prof]: Professor 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (2026-10-20 열람)
[^members]: Current Members 게시판 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub1_3> (2026-10-20 열람)
[^alumni]: Alumni 게시판 1–3쪽 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub1_2> (2026-10-20 열람)
[^news]: News 게시판 1–3쪽 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub5_1> (2026-10-20 열람)
[^facilities]: Facilities 페이지 <https://nanocore.kaist.ac.kr/bbs/board.php?bo_table=sub5_4> (2026-10-20 열람)
[^p1]: R.-G. Lee, Y.-H. Kim, npj Computational Materials 10, 248 (온라인 2024-10-24). <https://doi.org/10.1038/s41524-024-01433-0> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: J. Lee, H. Yeo, R.-G. Lee, Y.-H. Kim, npj Computational Materials 10, 60 (온라인 2024-03-22). <https://doi.org/10.1038/s41524-024-01242-5> 초록 기준.
[^p3]: T. H. Kim, J. Lee, Y.-H. Kim, npj Computational Materials 12, 283 (온라인 2026-05-28). <https://doi.org/10.1038/s41524-026-02101-1> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: T. H. Kim, J. Lee, R.-G. Lee, Y.-H. Kim, npj Computational Materials 8, 50 (온라인 2022-03-25). <https://doi.org/10.1038/s41524-022-00731-9> 초록 기준.
[^p5]: Z. Huang 외, D. Shahrjerdi, ACS Nano 18, 28700-28711 (온라인 2024-09-28). <https://doi.org/10.1021/acsnano.4c06929> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: T. Kang 외, S. Lee, Advanced Materials 36, 2312747 (온라인 2024-04-08). <https://doi.org/10.1002/adma.202312747> 초록 기준.
[^p7]: B.-K. Kim 외, M.-H. Bae, npj 2D Materials and Applications 5, 9 (온라인 2021-01-08). <https://doi.org/10.1038/s41699-020-00191-z> 초록 기준.
[^p8]: H. Lee 외, J. K. Kang, Advanced Energy Materials 13, 2300041 (온라인 2023-03-18). <https://doi.org/10.1002/aenm.202300041> 초록 기준.

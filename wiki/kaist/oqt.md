# KAIST OQT LAB

**KAIST 물리학과 · 김동규 조교수**

- 분야: 원자 기반 양자 정보 처리, 원자 제어, 광학 영상, 양자 센싱[^research][^dept]
- 대분야: 물리·양자, 전기전자·반도체·광학
- 태그: 양자 컴퓨팅[^home], 양자 정보·얽힘[^research], 광학 영상·현미경[^research][^dept]
- 홈페이지: <https://oqt.kaist.ac.kr/>
- 근거와 출처: [KAIST OQT LAB 근거 페이지](oqt-sources.md)

> 빛으로 원자를 제어하는 양자 정보 처리 장치를 연구한다. 원자 배열을 이용한 계산과 시뮬레이션, 원자와 빛을 연결하는 제어·영상 기술을 다룬다.[^home][^research]

## 무엇을 연구하나

연구실은 냉각한 원자(각 원소의 화학적 성질을 유지하는 최소 단위)를 배열해 양자 프로세서(양자 상태를 이용해 정보를 처리하는 연산 장치)를 연구한다. 양자 상태는 대상의 물리적 성질과 측정 결과의 확률을 나타내는 상태다. 원자의 상태를 정보로 표현하는 큐비트(서로 구별되는 두 상태를 기준으로 정보를 표현하는 양자 정보의 기본 단위)를 빛으로 제어하고, 이를 이용한 양자 컴퓨팅과 시뮬레이션(연구 대상을 다른 물리계나 계산 모형으로 구현해 거동을 살피는 방법)을 연구한다.[^home][^research]

연구 소개는 원자 큐비트와 결맞음 광학 영상의 접점에서 양자 정보를 처리하는 원리와 기술을 연구한다고 설명한다. 빛의 진동이 한 주기 안에서 진행한 위치를 위상이라 하고, 결맞음은 서로 다른 위치나 시각의 진동이 일정한 위상 관계를 유지하는 성질이다. 연구실은 원자와 빛의 결맞음을 연결할 때 나타나는 역할과 한계를 연구하며, 학과 소개도 양자 정보 처리를 위한 광학 영상·현미경 기술을 연구 분야로 든다.[^research][^dept]

대표 논문 1은 원하는 위치의 원자만 정밀하게 제어하는 문제를 다룬다. 광학 집게(집중된 빛이 가하는 힘으로 입자를 붙잡고 움직이는 장치) 안에서 원자가 움직일 때의 원자와 빛의 상호작용을 학습하고, 신경망(연결된 계산 단위들의 가중치를 학습해 입력과 출력의 관계를 나타내는 모형)이 합성 펄스(짧은 시간 동안 가해지는 신호들을 조합한 제어 신호)를 설계하게 했다. 기존 제어 장치와 함께 쓸 수 있는 펄스를 제시하고, 빛의 초점(렌즈나 거울을 지난 빛이 모이는 지점)이 이상적인 형태에서 벗어나거나 빔(한 방향으로 모여 나아가는 빛의 묶음)의 위치가 어긋나는 경우에도 제어가 견디는지를 살폈다.[^p1]

대표 논문 2는 스핀(입자 자체가 지닌 회전 관련 양자적 성질)을 이용하는 센서 집단에서 어느 부분을 골라야 측정에 유리한지 묻는다. 감도(측정 대상의 작은 변화를 가려낼 수 있는 정도)의 문턱을 정해 최적의 부분집합을 찾고, 펄스를 쓰는 방식과 빛을 연속적으로 가하는 방식의 자기장(자기력이 작용하는 공간의 상태) 측정에 적용했다.[^p2] 대표 논문 3은 가시광(사람의 눈으로 감지할 수 있는 빛)의 세기·위상·공간 분포를 바꾸는 변조 기술을 검토한 리뷰다. 원자 기반 양자 기술의 제어·측정, 증강현실(현실의 모습에 가상 정보를 겹쳐 보여 주는 기술) 화면, 생물 시스템의 측정·제어를 응용 대상으로 들고 관련 광학 기술을 비교한다.[^p3]

## 주요 연구 주제

### 원자 큐비트의 위치별 제어

원자 배열을 이용하는 양자 프로세서의 제어와 계산이 연구실의 주요 갈래다.[^home] 대표 논문 1에서는 원자의 움직임을 포함한 학습으로 제어 펄스를 설계하고, 광학계(렌즈·거울 등으로 빛의 경로를 만드는 장치들의 조합)의 불완전함에 대한 견고함을 다뤘다.[^p1]

### 센서 집단의 최적 부분집합

대표 논문 2는 센서마다 특성이 다른 집단의 감도를 계산하고, 측정에 기여할 스핀을 고르는 기준을 제시한다. 명목상 균일한 영역만 쓰는 기존 방식과 비교해 최대 8배의 개선을 보였으며, 빛을 공간적으로 조절해 선택한 집단을 구현했다.[^p2]

### 원자와 광학 영상의 연결

원자 큐비트와 결맞음 광학 시스템의 접점이 연구 소개의 중심이다.[^research] 대표 논문 3은 가시광 변조 기술을 속도·제어 전력·크기·광학 대역폭(다룰 수 있는 빛의 진동수, 곧 단위 시간에 진동이 반복되는 횟수의 범위)·기술 성숙도로 비교한다.[^p3]

## 대표 논문

김동규 교수가 저자로 참여한 2021–2026년 연구 가운데 원자 제어·센싱·광학 기술을 보여 주는 세 편을 골랐다. 2번과 3번은 arXiv 사전 공개본으로 소개한다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지·학회 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Autonomously designed pulses for robust, site-selective control of atomic qubits](https://doi.org/10.1103/dspx-fgp2) · Physical Review Applied 25, 064057 | 원자가 광학 집게 안에서 움직이는 상황을 학습한 신경망으로 제어 펄스를 설계한다. 기존 제어 장치와 호환되면서 원하는 위치의 큐비트를 제어하는 방법이며, 광학계의 초점 왜곡과 빔 위치 오차에 대한 견고함도 보였다.[^p1] | 1저자 Sanghyo Park, 교신·마지막 저자 Donggyu Kim |
| 2 | 2025 | [Sensitivity threshold defines the optimal spin subset for ensemble quantum sensing](https://doi.org/10.48550/arXiv.2512.10549) · arXiv:2512.10549 (사전 공개본·심사 중) | 반응이 서로 다른 스핀을 모두 쓰는 대신 감도 문턱으로 최적의 부분집합을 찾는다. 두 자기장 측정 방식에서 기존 방식 대비 최대 8배의 개선을 보였고, 빛의 위상만 조절하는 디지털 홀로그래피(빛의 위상·세기 분포를 수치로 설계하거나 기록해 빛의 분포를 재현하는 기술)로 선택한 집단을 구현했다.[^p2] | 첫 저자 Suwan I. Kang·Minhyeok Kim(누리집 공동 기여 표시), 마지막 저자 Donggyu Kim |
| 3 | 2024 | [Technologies for Modulation of Visible Light and their Applications](https://doi.org/10.48550/arXiv.2403.15606) · arXiv:2403.15606 (사전 공개본·리뷰) | 가시광을 제어하는 기술과 응용을 정리한 리뷰다. 원자 기반 양자 기술, 증강현실 화면, 생물 시스템의 측정·제어를 다루며, 기존 광학 장치와 빛을 다루는 기능을 칩에 모은 집적 광학 기술을 비교한다.[^p3] | 1저자 Sanghyo Park, 공저자 Donggyu Kim, 마지막 저자 Sara Mouradian |

## 교수와 전문 분야

김동규(Donggyu Kim) 교수는 KAIST 물리학과 조교수다. 고려대학교에서 물리학 학사(2011)·석사(2013)를 받고, Massachusetts Institute of Technology에서 기계공학 박사(2019)를 받았다. 2019–2021년 QuEra Computing에서 Research Scientist로 일했고, 학과 경력표는 2021년부터 KAIST 조교수로 적는다.[^dept]

연구실 교수 소개는 박사과정에서 원자 기반 양자 기술을 위한 디지털 홀로그래피 틀을 개발했고, QuEra Computing에서는 외부에서 접근할 수 있는 중성 원자(전체 전하가 없는 원자) 양자컴퓨터 개발에 참여했다고 설명한다. KAIST OQT Lab 경력은 2022년부터로 적고, 차세대 양자 기술을 위한 원자와 빛의 상호작용을 연구한다고 밝힌다.[^team] 최근 논문에서 드러나는 전문 분야는 원자 큐비트 제어, 스핀 집단 센싱, 가시광 제어 기술이다.[^p1][^p2][^p3]

## 응용 분야

연구실이 내건 응용은 원자 배열 기반 양자 프로세서의 계산·시뮬레이션과 양자 제어다.[^home] 대표 논문 1은 제어 펄스 설계를 다른 원자 유사 플랫폼에도 확장할 수 있다고 제안하고,[^p1] 대표 논문 2는 빛이 산란하는 환경에서 최적의 양자 센싱을 수행하는 방법으로 제시한다.[^p2]

## 구성원

누리집 Team에 게시된 교수 외 현재 구성원 12명이다. 연구 주제는 해당 구성원 소개의 표기를 따르고, 시작 시점은 Activities의 합류 소식에 적힌 연월이다. "대표 논문 참여"는 위 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^team][^activities]

| 이름 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|
| 신형우 (Hyoungwoo Shin) |  | quantum error correction and digital-analog quantum simulation |  |
| 김우진 (Woojin Kim) |  | high-fidelity single-qubit gates and quantum error correction in large-scale atomic qubit arrays |  |
| 김준우 (Junwoo Kim) |  | the precise control and calibration of gate beams for neutral-atom quantum computing |  |
| 정웅균 (Unggyun Jung) |  | precision qubit control and quantum simulation |  |
| 전상진 (Sangjin Jeon) |  | the single-atom feedback control |  |
| 이세욱 (Seuk Lee) | 2022-01 | local addressing of neutral atoms in optical tweezer arrays | 1 |
| 박상효 (Sanghyo Park) | 2022-01 | developing hybrid quantum computing architectures | 1, 2, 3 |
| 김민혁 (Minhyeok Kim) | 2022-01 | optical imaging interfaces for quantum-emitter platforms | 1, 2 |
| 이근영 (Keunyoung Lee) |  | designing a scalable system architecture of controlling atomic qubits | 1, 2 |
| 김동범 (Dongbeom Kim) |  | developing a neutral- atom quantum information processor |  |
| 강수완 (Suwan Kang) |  | single neutral-atom control and quantum ensemble sensing |  |
| 장민호 (Minho Jang) |  | developing the control interface for neutral atom-quantum computing and non-destructive state detection |  |

## 졸업생과 이전 구성원

누리집 Team의 Group Alumni에 게시된 5명이다. 학위·과정 칸에는 누리집이 적은 과정명과 재적 기간을 담았다.[^team]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Heonsik Lee | M.S. Student (2023.03–2025.06) |  |
| Hyunbeen Lee | M.S. Student (2023.09–2025.06) |  |
| Hyensu Kim | Undergraduate Student (2023) |  |
| Jaeyong Hwang | Undergraduate Student (2022–2023) |  |
| Yunjeong Kim | Undergraduate Student (2022) |  |

## 최근 논문 목록 (2021–2026)

누리집 Publications의 출판 논문 2편과 Preprints의 심사 중 원고 1편이다. 제목·저자·발표처는 누리집 표기를 따르며 DOI를 함께 적었다. arXiv 항목의 연도는 최초 공개 연도이고, under review는 심사 중이라는 뜻이다. *는 해당 원고가 밝힌 공동 기여, †는 누리집이 밝힌 교신저자 표시다. 교수는 2021년 11월 1일 KAIST 물리학과 조교수로 부임했다고 알려져 있어[^appt], 이 목록에는 부임 전 연구가 섞일 수 있으며 부임 뒤 출판된 논문도 KAIST 소속 성과로 단정하지 않는다.[^pubs][^p2]

**2026**

- Sanghyo Park, Seuk Lee, Keunyoung Lee, Minhyeok Kim, and Donggyu Kim. "Autonomously designed pulses for robust, site-selective control of atomic qubits". *Phys. Rev. Applied, 25, 064057 (2026); DOI <https://doi.org/10.1103/dspx-fgp2>*.

**2025**

- Suwan Kang\*, Minhyeok Kim\*, Sanghyo Park, Heonsik Lee, Keunyoung Lee, and Donggyu Kim (\*equal contribution). "Sensitivity threshold defines the optimal spin subset for ensemble quantum sensing". *arXiv (2025) (under review); DOI <https://doi.org/10.48550/arXiv.2512.10549>*.

**2024**

- Sanghyo Park, Milica Notaros, Aseema Mohanty, Donggyu Kim, Jelena Notaros, and Sara Mouradian†. "Technologies for Modulation of Visible Light and their Applications". *Progress in Quantum Electronics, 100534 (2024) [Invited Review]; DOI <https://doi.org/10.1016/j.pquantelec.2024.100534>*.

## 특허와 특허 출원

누리집 Patents and Patent Applications에서 2022–2025년으로 적은 6건이다. 연도는 누리집의 연도 표기이고 날짜는 게시되어 있지 않다. 교수는 2021년 11월 1일 KAIST 물리학과 조교수로 부임했다고 알려져 있고[^appt], 이 목록에는 교수의 이전 소속 기관에서 수행한 발명이 섞여 있으므로 각 항목에 게시된 주체·발명자와 기관을 함께 적었다. 번호는 누리집 표기 그대로다.[^pubs]

- 2025 · 구조화된 조명을 이용한 고체 상태 양자 메모리의 최적 여기 장치 및 양자 얽힘 중계 방법 (기관 Korea Advanced Institute of Science and Technology (KAIST); 게시 주체 KAIST OQT LAB)
- 2025 · 비균질 스핀 센서 집단에서의 최적 부분집합 선택을 이용한 집단 감도 향상 장치 및 방법 (기관 Korea Advanced Institute of Science and Technology (KAIST); 게시 주체 KAIST OQT LAB)
- 2025 · 원자 큐비트의 정밀 제어를 위한 합성 펄스의 학습 방법과 시스템 (기관 Korea Advanced Institute of Science and Technology (KAIST); 게시 주체 KAIST OQT LAB)
- 2024 · Large-Scale Uniform Optical Focus Arrays with a Phase Spatial Light Modulator (기관 Harvard University and Massachusetts Institue of Technology; 번호 US Patent 11,985,451 (2024); PCT/US2020/19309 (2020); 발명자 Donggyu Kim, A. Keesling, A. Omran, H. Levine, H. Bernien, M. D. Lukin, and D. R. Englund)
- 2022 · Neutral Atom Quantum Information Processor (기관 Harvard University, California Institute of Technology, Massachusetts Institute of Technology; 번호 US Patent 11,380,455B2 (2022); 발명자 A Keesling, H. Bernien, S. Schwartz, H. Levine, A. Omran, M. Lukin, V. Vluletic, M. Endres, M. Greiner, H. Pichler, L. Zhou, S. Wang, S. Choi, Donggyu Kim, A. Zibrov)
- 2022 · Optical Addressing Methods and Apparatus (기관 QuEra Computing Inc.; 번호 PCT/US2022/029554 (2022); 발명자 A. Bylinskii, Donggyu Kim, S. Wang, A. Omran, N. Gemelke, D. Englund, J. Amato-Grill, A. Lukin, N. Wan, and M. Hu)

## 수상과 선정

누리집 Activities의 2025년 5월 COOC 글에 적힌 연구 관련 선정 1건이다. MH는 글의 표기 그대로다. 교수는 2021년 11월 1일 KAIST 물리학과 조교수로 부임했다고 알려져 있으며[^appt], 이 항목의 날짜는 그 뒤다.[^activities]

- 2025-05 · MH의 양자 센싱 연구가 COOC(Conference on Optoelectronics and Optical Communications)에서 outstanding paper로 선정됐다.

## 소식

누리집 Activities에서 연구실 출범과 연구 지원을 알린 2022년 3월 글이다. 교수는 2021년 11월 1일 KAIST 물리학과 조교수로 부임했다고 알려져 있으며[^appt], 이 항목의 날짜는 그 뒤다.[^activities]

- 2022-03 · 연구실 출범과 NRF·IITP·KAIST 도약(UP)의 연구 지원을 알렸다.

## 연락과 위치

- 주소: KAIST 물리학과, 대전광역시 유성구 대학로 291, 34141[^home]
- 교수 연구실: E6-6 #103[^dept]
- 기관 전화: +82-42-350-2539[^dept]
- 교수 이메일: dngkim@kaist.ac.kr[^p1]
[^home]: KAIST OQT LAB, 첫 화면. <https://oqt.kaist.ac.kr/> 관측일 2026-11-07.
[^research]: KAIST OQT LAB, Research. <https://oqt.kaist.ac.kr/research> 관측일 2026-11-07.
[^dept]: KAIST 물리학과, Professor Kim, Donggyu (김동규). <https://physics.kaist.ac.kr/index.php?document_srl=12003&mid=p_people1> 관측일 2026-11-07.
[^team]: KAIST OQT LAB, Team. <https://oqt.kaist.ac.kr/team> 관측일 2026-11-07.
[^pubs]: KAIST OQT LAB, Publications. <https://oqt.kaist.ac.kr/publications> 관측일 2026-11-07.
[^activities]: KAIST OQT LAB, Activities. <https://oqt.kaist.ac.kr/activities> 관측일 2026-11-07.
[^p1]: S. Park 외, D. Kim, Physical Review Applied 25, 064057 (온라인 2026-06-17). <https://doi.org/10.1103/dspx-fgp2> 초록 기준(출판사 논문 페이지). 초록 원문 <https://journals.aps.org/prapplied/abstract/10.1103/dspx-fgp2> 관측일 2026-11-07.
[^p2]: S. I. Kang 외, D. Kim, arXiv:2512.10549 (사전 공개본) (2025). <https://doi.org/10.48550/arXiv.2512.10549> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2512.10549> 관측일 2026-11-07.
[^p3]: S. Park 외, S. Mouradian, arXiv:2403.15606 (사전 공개본·리뷰) (2024). <https://doi.org/10.48550/arXiv.2403.15606> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2403.15606> 관측일 2026-11-07.
[^appt]: 고려대학교 이과대학 뉴스 「[김동규 박사] KAIST 물리학과 조교수 임용」(등록 2022-01-17). <https://science.korea.ac.kr/science-new/announcement/news.do?articleNo=117&category=ALL&mode=view&pageNo=18&searchBgnde=&searchEndde=&searchType=&searchWord=&targetDept=SCIENCE> 관측일 2026-11-07.

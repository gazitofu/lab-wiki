# 양자 소자 연구실 (Quantum Device Lab, QDlab)

**KAIST 전기및전자공학부 · 손영익 교수**

- 분야: 집적 광회로 기반 광 양자 컴퓨팅, 비선형 광학을 이용한 광자 쌍·단일 광자 광원, 광회로 설계·시뮬레이션(자체 소프트웨어 DBEME), 광 지연선과 결합기, 박막 리튬나이오베이트 광회로
- 홈페이지: <https://qdlab.kaist.ac.kr/>
- 근거와 출처: [QDlab 근거 페이지](qdlab-sources.md)

> 빛 알갱이인 광자를 큐비트로 쓰는 양자 컴퓨터를 반도체 칩 위의 광회로로 만들려는 연구실이다. 칩 안에서 광자를 만들고 다루는 소자와, 이를 빠르고 정확하게 설계하는 시뮬레이션 방법을 연구한다.[^home][^research]

## 무엇을 연구하나

연구실은 양자 컴퓨팅과 양자 통신용 새로운 소자를 개발하며, 파동과 큐비트를 제어하는 여러 소자 기술을 써서 집적 광회로와 주문형 반도체 칩(ASIC)으로 양자 광학 시스템을 만든다고 소개한다.[^home] 연구 소개는 양자 컴퓨터를 만드는 주요 방식으로 구글·IBM이 쓰는 초전도 큐비트, 원자의 에너지 준위를 쓰는 이온 트랩, 그리고 연구실이 다루는 선형 광학 양자 컴퓨팅(광자와 선형 광학 소자로 계산하는 방식)을 든다. 집적 광회로는 대량 생산이 쉬워 오류를 스스로 고치는 양자 컴퓨터라는 목표에 유리하지만, 광자 방식은 결과가 확률적이어서 아직 믿을 만한 큐비트 하나도 만들지 못했다는 과제가 있다고 적는다.[^research] 해법은 확률적인 부품을 여러 개 묶어 거의 확정적인 부품으로 만드는 것이고, 이를 위해 확률적 단일 광자 광원, 단일 광자 검출기, 빠른 전자 회로, 광 스위치를 하나로 통합해야 한다.[^research]

연구는 세 갈래로 볼 수 있다. 첫째는 **칩 위의 양자 광원**이다. 연구실은 강한 레이저 펄스를 집적 광회로에 넣어 자발 매개 하향 변환이나 자발 4광파 혼합 같은 비선형 광학 현상으로 광자 쌍을 만들고, 회로를 설계해 광 양자 컴퓨팅에 쓸 만큼 순수하고 효율적인 단일 광자를 얻으려 한다.[^research] 대표 논문에서는 강한 펄스로 구동하는 마이크로 링 공진기에서 생기는 양자 빛을 계산하는 이론을 세웠고,[^p3] 집적 비선형 양자 광학을 폭넓게 모사하는 시뮬레이션 틀과 칩 위의 시간 어긋남 보정 소자를 제안했으며,[^p4] 다른 연구진과 함께 두 종류 광자 쌍 광원의 구별 불가능성을 비교했다.[^p7]

둘째는 **광회로 설계와 시뮬레이션**이다. 연구실은 도파로의 모드 정보를 미리 계산해 데이터로 저장해 두고 꺼내 쓰는 빠른 광소자 시뮬레이션 방법 DBEME를 공개 소프트웨어로 내놓았다.[^software][^news] 대표 논문에서는 이 방법으로 다중 모드 도파로를 기존보다 100–1000배 빠르게 설계했다.[^p1] 다른 논문에서는 빛을 원하는 비율로 나누는 넓은 대역의 결합기와 이를 쓴 파장 분할 다중화 소자를 만들었다.[^p2]

셋째는 **광 지연선과 새로운 광회로 소재**다. 대표 논문에서는 공정 오차에 강하고 손실이 아주 낮은 나노 광 지연선을 만들었고,[^p5] 박막 리튬나이오베이트 광회로에서 열로 굴절률을 바꾸는 효과가 방향에 따라 다른 것을 설명하는 일반 모형을 처음 내놓았다.[^p6]

## 주요 연구 주제

### 1. 칩 위의 양자 광원

강한 펄스 링 공진기의 양자 빛, 집적 비선형 양자 광학 시뮬레이션, 광자 쌍 광원 비교.[^p3][^p4][^p7] 대표 논문 3, 4, 7.

### 2. 광회로 설계·시뮬레이션

데이터 기반 고유 모드 전개(DBEME) 설계, 임의 분배비 결합기.[^p1][^p2] 대표 논문 1, 2.

### 3. 광 지연선과 박막 리튬나이오베이트

저손실 나노 광 지연선, 박막 리튬나이오베이트의 열광학 응답 모형.[^p5][^p6] 대표 논문 5, 6.

## 대표 논문

랩 논문 목록의 2022–2026년 논문 가운데 손영익 교수가 교신저자(랩 표기 †)인 것을 중심으로 연구 주제를 고르게 담았다. 7은 다른 연구진이 이끈 공동 연구다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2025 | [Ultra-fast and accurate multimode waveguide design based on a dataset-based eigenmode expansion method](https://doi.org/10.1364/oe.567425) · Optics Express | 다중 모드 도파로(빛을 여러 모양으로 함께 보내는 통로) 설계를 위한 데이터 기반 광 시뮬레이션 틀을 제안해, 복잡한 설계에서 기존 방법보다 100–1000배 빨랐다. 반지름 30 µm의 실리콘 다중 모드 도파로 굽힘을 1초 안에 상용 3차원 시뮬레이션과 맞먹는 정확도로 계산했고, 수천 번의 최적화를 일반 데스크톱에서 68분 만에 마쳐 원하는 비율로 빛을 나누는 굽힘을 설계했다.[^p1] | 1저자 Jaesung Song, 교신 손영익 |
| 2 | 2025 | [Rapid adiabatic couplers with arbitrary split ratios for broadband DWDM interleaver application](https://doi.org/10.1515/nanoph-2025-0288) · Nanophotonics | 도파로 위치를 비키고 폭을 조절해, 작고 넓은 대역에서 빛을 원하는 비율로 나누는 결합기를 만들었다. 네 가지 목표 비율의 결합기가 160 nm 파장 범위에서 목표의 ±3% 안으로 빛을 나눴고, 이를 써서 8채널 고밀도 파장 분할 다중화(여러 파장에 정보를 나눠 싣는 방식) 소자를 만들었다.[^p2] | 공동 1저자 Daehan Choi·Woo-Joo Kim, 교신 손영익 |
| 3 | 2025 | [Simulating quantum light in lossy microring resonators driven by strong pulses](https://doi.org/10.1103/physrevapplied.23.054045) · Physical Review Applied | 고리 모양 공진기 하나에서 펄스로 광자 쌍을 만드는 양자 이론을 세웠다. 강한 빛에서 생기는 자기 위상 변조 같은 비선형 효과와 광 손실까지 넣어 계산하자, 이 효과들이 전달 특성을 크게 비틀었고, 펌프 빛의 주파수를 알맞게 어긋나게 하면 밝기와 스펙트럼 순도가 좋아짐을 보였다.[^p3] | 1저자 Youngbin Kim, 교신 손영익 |
| 4 | 2024 | [Simulation of integrated nonlinear quantum optics: From nonlinear interferometer to temporal walk-off compensator](https://doi.org/10.1103/physrevapplied.22.064092) · Physical Review Applied | 비선형 양자 광학은 광 양자 컴퓨팅과 양자 통신의 바탕이다. 단열 도파로, 소재의 방향성, 선형 광학 부품, 광자 손실, 검출기까지 정확히 모사하는 시뮬레이션 틀을 만들고, 이를 써서 칩 위에서 펄스의 시간 어긋남을 보정하는 소자를 제안했다. 이 소자는 펌프 출력을 높이지 않고도 광자 쌍 광원의 압축 정도와 양자 주파수 변환 효율을 높인다.[^p4] | 공동 1저자 S. Kim·Youngbin Kim, 교신 손영익 |
| 5 | 2022 | [Robust, ultralow-loss, and broadband light-recycling for a nanophotonic delay line](https://doi.org/10.1364/ol.457213) · Optics Letters | 광 지연선(빛을 일부러 늦게 도착시키는 부품)은 손실이 낮고, 대역이 넓고, 작아야 한다. 공간 모드 다중화로 빛을 되돌려 쓰는 방식에 마흐-젠더 간섭계 설계를 더해 공정 오차 허용도를 크게 높였다. 100 nm 넓은 대역에서 ±10 nm의 공정 오차가 있어도 추가 손실이 0.5 dB 아래였다.[^p5] | 1저자 Y.-S. Koh, 교신 X. Xiong·손영익 |
| 6 | 2026 | [Generalized Model of Anisotropic Thermo-Optic Response on Thin-Film Lithium Niobate Platform](https://doi.org/10.1021/acsphotonics.6c00117) · ACS Photonics | 박막 리튬나이오베이트 광회로에서는 열로 굴절률을 바꾸는 조절이 중요한데, x-컷 결정에서는 그 효과가 도파로 방향과 편광에 따라 다르다. 이 방향 의존성을 편광과 임의의 도파로 방향의 함수로 나타내는 일반 해석 모형을 처음 세우고, 시뮬레이션과 실험으로 검증했다.[^p6] | 공동 1저자 J. Shim·S. Kim, 교신 M. Lončar·손영익 |
| 7 | 2023 | [Do different kinds of photon-pair sources have the same indistinguishability in quantum silicon photonics?](https://doi.org/10.1364/prj.489869) · Photonics Research | 같은 실리콘 광회로 안에서 마이크로 링 공진기와 직선 도파로, 두 종류 광자 쌍 광원을 홍-오우-만델 간섭 실험으로 비교했다. 간섭 선명도는 링 공진기 94%, 직선 도파로 99%였고, 이 차이가 두 광원이 만든 광자 쌍 스펙트럼의 겹침(링 89%, 도파로 98%)과 연결됨을 확인했다.[^p7] | 1저자 J.-M. Lee, 마지막 저자 L. Pavesi(손영익 공저) |

## 교수와 전문 분야

손영익 교수는 서울대 전기공학 학사(2009), 미국 스탠퍼드대 전기공학 석사(2011), 하버드대 응용물리 박사(2018)를 받았다. PsiQuantum에서 연구개발 엔지니어(2018–2020)로 일한 뒤 2020년부터 KAIST 전기및전자공학부 조교수이며, 반도체시스템공학과와 양자대학원에도 소속돼 있다.[^prof] 연구 관심사로 양자 광학, 집적 광학, 양자 컴퓨팅을 든다.[^prof] 박사과정 시절에는 다이아몬드 스핀 큐비트의 결맞음을 변형으로 조절한 연구(Nature Communications, 2018, 표지 논문)를 공동 1저자로 냈다고 논문 목록에 적혀 있다.[^papers] 랩 소식에는 2023년 퀀텀 코리아에서 과학기술정보통신부 장관상을 받았다는 글이 있다.[^news]

논문으로 보면 전문 분야는 세 갈래다.

- **집적 비선형 양자 광학과 칩 위 광자 광원**.[^p3][^p4][^p7]
- **데이터 기반 광회로 설계·시뮬레이션**.[^p1][^p2]
- **저손실 광 지연선과 박막 리튬나이오베이트 광회로**.[^p5][^p6]

## 응용 분야

대표 논문으로 보면 광 양자 컴퓨팅과 양자 통신용 광원·주파수 변환기, 광통신의 파장 분할 다중화 소자, 저전력 광 정보 처리, 박막 리튬나이오베이트 기반 광회로 설계 도구에 닿아 있다.[^p2][^p4][^p5][^p6] 졸업생은 삼성종합기술원, 한국과학기술연구원(KIST) 등으로 진출했다.[^alumni]

## 구성원

2026년 10월 20일 랩 Members 페이지 기준이다. 과정 칸의 괄호는 랩이 적은 시작 학기이고, 연구 관심사와 이메일은 랩이 적은 것이다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Dr. Hyeon Hwang | 박사후연구원 | Integrated photonics, Nonlinear photonics, Quantum photonics, Micro-resonator | hyeon_hwang@kaist.ac.kr |  |
| Dr. Prabal Dweep Khanikar | 박사후연구원 | Diamond Color Centers and Quantum Emitters, Quantum Photonics and Quantum Communication, Semiconductor Optoelectronics and Hybrid Material Systems |  |  |
| Dr. Seung-Ik Han | 박사후연구원 | Quantum co-packaged optics, Photonic integrated circuit packaging, Semiconductor process-based device integration, Multiphysics simulation and device reliability | seungik.han@kaist.ac.kr |  |
| Daehan Choi | 석박사통합과정 (2021 Fall) | Integrated photonics, Electro-optic devices | daehan96@kaist.ac.kr | 2 |
| Jianliang Guo | 석박사통합과정 (2021 Fall) | Detector integration with photonics, Photonics cryogenic packaging | jianliang@kaist.ac.kr |  |
| Woo-Joo Kim | 석박사통합과정 (2022 Fall) | Active Feedforward, Measurement Based Quantum Computer | spacekim@kaist.ac.kr | 2, 4 |
| Jaesung Song | 박사과정 (2025 Spring) | On-chip optical delay line, Quantum memory, Linear photonics simulation | thdwotjd98@kaist.ac.kr | 1 |
| Youngbin Kim | 박사과정 (2025 Spring) | Nonlinear quantum photonics, Quantum frequency conversion | bin1091004@kaist.ac.kr | 3, 4 |
| SeongJin Jeon | 박사과정 (2026 Spring) | Nonlinear quantum photonics, Computational physics | jsj8632@kaist.ac.kr | 3, 4, 6 |
| Jaehun Seung | 박사과정 (2026 Spring) | Hybrid integration, Co-package optics | jaehunsng@kaist.ac.kr |  |
| Fuyi Huang | 석박사통합과정 (2024 Spring) |  | oliviafyh@kaist.ac.kr |  |
| Shuzhen Li | 석사과정 (2024 Fall) |  | lishuzhen@kaist.ac.kr |  |
| Daegyeom Kim | 석사과정 (2025 Fall) | Active feedforward circuit, Cryogenic CMOS design | kk11dd22@kaist.ac.kr |  |
| SeungHwan Choi | 석박사통합과정 (2026 Spring) |  | kcsh38@kaist.ac.kr |  |
| Junhyung Cho | 석사과정 (2026 Fall) | Diamond integrated photonics, Ferroelectric electro-optic devices | junhyungcho@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 이름, 과정·기간, 랩이 적은 다음 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Joonsup Shim | Postdoc (2024 - 2025) | Staff Engineer, Samsung Advanced Institute of Technology (SAIT), Samsung Electronics, South Korea |
| Seonghun Kim | Ph.D. Program (2024.02 - 2026. 06); MS Program (2021.09 - 2024. 02) | Postdoctoral Researcher, Korea Institute of Science and Technology (KIST), South Korea |
| Min-Hyoung Joo | MS Program (2024.02 - 2026. 08) | Graduate Student, Prof. Hansuek Lee's Group, KAIST, South Korea |
| Eric Branderbit | Research Internship (2026.03 - 2026.09) | Physics Student, Drexel University, USA |
| Quentin David | Research Internship (2026.03 - 2026.08) | École Polytechnique, France |

## 최근 논문 목록 (2022–2026)

랩 Publications 페이지의 2022년 이후 논문이다(같은 페이지는 2021년 이전 논문을 "Before 2022"로 묶는다). 저자 이름 뒤 †는 교신저자, *는 같은 기여를 뜻하는 랩 표기다.[^papers]

**2026**

- S. Liu, Q. Lu, P. Hu, Y. Zhong, Y. He, Y. Zhang, Y. Sohn, Y. Su†, and L. Sun†. "Recent Advances in Stimulated Brillouin Scattering in Integrated Photonics". *Advanced Physics Research e70133 (2026)*.
- J. Shim\*, S. Kim\*, S. Lu, J. Yang, S. Jeon, S. Kim, M. Lončar†, and Y.-I. Sohn†. "Generalized Model of Anisotropic Thermo-Optic Response on Thin-Film Lithium Niobate Platform". *ACS Photonics (2026)*.
- C. Yang, J. Wang, S. Tang, Z. Fang, Y.-I. Sohn, H. Xia, B. Li, and F. Qiu†. "Long-term and thermal stability of PZT electro-optic modulators". *Opt. Express, OE 34, 8858 (2026)*.

**2025**

- J. Song and Y.-I. Sohn†. "Ultra-fast and accurate multimode waveguide design based on a dataset-based eigenmode expansion method". *Opt. Express, OE 33, 46815 (2025)*.
- D. Choi\*, W.-J. Kim\*, and Y.-I. Sohn†. "Rapid Adiabatic Couplers with Arbitrary Split Ratios for Broadband DWDM Interleaver Application". *Nanophotonics 14, 3089 (2025)*.
- Y. Kim, S. Jeon, and Y.-I. Sohn†. "Simulating quantum light in lossy microring resonators driven by strong pulses". *Phys. Rev. Applied 23, 054045 (2025)*.
- PsiQuantum Team. "A manufacturable platform for photonic quantum computing". *Nature (2025)*.

**2024**

- S. Kim\*, Y. Kim\*, Y.-D. Yoon, S. Jeon, W.-J. Kim, and Y.-I. Sohn†. "Simulation of integrated nonlinear quantum optics: From nonlinear interferometer to temporal walk-off compensator". *Phys. Rev. Applied 22, 064092 (2024)*.
- Joo, HJ., Liu, J., Chen, M. et al. "Actively tunable laser action in GeSn nanomechanical oscillators". *Nat. Nanotechnol. 19, 1116–1121 (2024)*.
- Jong-Moo Lee†, Jiho Park, Jeongho Bang, Young-Ik Sohn, Alessio Baldazzi, Matteo Sanna, Stefano Azzini, Lorenzo Pavesi. "Quantum states generation and manipulation in a programmable silicon-photonic four-qubit system with high-fidelity and purity". *APL Photonics 9 (7): 076110 (2024)*.
- Guolei Liu, Hongyan Yu, Dasai Ban, Bin Li, Guoqiang Wei, Chen Yang, Jungan Wang, Young-Ik Sohn, Yu Han, Feng Qiu†. "Highly efficient lead zirconate titanate ring modulator". *APL Photonics 9 (6): 066111 (2024)*.

**2023**

- J.-M. Lee, A. Baldazzi, M. Sanna, S. Azzini, J. T. Ahn, M.-L. Lee, Y. Sohn, and L. Pavesi. "Do Different Kinds of Photon-Pair Sources Have the Same Indistinguishability in Quantum Silicon Photonics?". *Photon. Res. 11, 1820 (2023)*.

**2022**

- Y.-S. Koh, X. Xiong†, and Y.-I. Sohn†. "Robust, ultralow-loss, and broadband light-recycling for a nanophotonic delay line". *Opt. Lett. 47, 2330 (2022)*.

## 소식

랩 News 페이지의 논문·수상 소식이다.[^news]

- 2025 · Jaesung's Optics Express paper was selected as a 'Spotlight on Optics' selection; the software Dataset-Based EME (DBEME) is now open-source.
- 2023 · Professor Youngik Sohn was honored with the "Minister's Award" from the Ministry of Science and ICT at 'Quantum Korea 2023'.

## 연락과 위치

- 교수실: KAIST E3-2동 4206호, 학생 연구실: E3-2동 4214–4215호[^prof][^contacts]
- 교수 이메일: youngik.sohn@kaist.ac.kr[^contacts]

[^home]: 연구실 누리집 첫 화면 <https://qdlab.kaist.ac.kr/> (2026-10-20 열람)
[^research]: Research 페이지 <https://qdlab.kaist.ac.kr/Research-1c41e60380da8056b4fec5ef0512642f> (2026-10-20 열람)
[^members]: Members 페이지 <https://qdlab.kaist.ac.kr/Members-1c41e60380da804fb01fd25357440652> (2026-10-20 열람)
[^prof]: 교수 페이지 <https://qdlab.kaist.ac.kr/Young-lk-Sohn-1c41e60380da80e19272e36ef9271902> (2026-10-20 열람)
[^papers]: Publications 페이지 <https://qdlab.kaist.ac.kr/Publications-1c41e60380da80e99431dd5239ea50cc> (2026-10-20 열람)
[^alumni]: Alumni 페이지 <https://qdlab.kaist.ac.kr/Alumni-3fb1e60380da8019a329f1a02b51ae4f> (2026-10-20 열람)
[^news]: News 페이지 <https://qdlab.kaist.ac.kr/News-1c41e60380da8080806cf881da4237f7> (2026-10-20 열람)
[^software]: Software 페이지 <https://qdlab.kaist.ac.kr/Software-2cb1e60380da8072a2aff579056954d1> (2026-10-20 열람)
[^contacts]: Contacts 페이지 <https://qdlab.kaist.ac.kr/Contacts-1c41e60380da802e9eaff8622c3f1d3e> (2026-10-20 열람)
[^p1]: J. Song, Y.-I. Sohn, Optics Express 33, 46815 (온라인 2025-10-28). <https://doi.org/10.1364/oe.567425> 초록 기준.
[^p2]: D. Choi, W.-J. Kim, Y.-I. Sohn, Nanophotonics 14, 3089-3094 (온라인 2025-09-01). <https://doi.org/10.1515/nanoph-2025-0288> 초록 기준.
[^p3]: Y. Kim, S. Jeon, Y.-I. Sohn, Physical Review Applied 23, 054045 (온라인 2025-05-16). <https://doi.org/10.1103/physrevapplied.23.054045> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Kim 외, Y.-I. Sohn, Physical Review Applied 22, 064092 (온라인 2024-12-26). <https://doi.org/10.1103/physrevapplied.22.064092> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: Y.-S. Koh, X. Xiong, Y.-I. Sohn, Optics Letters 47, 2330 (온라인 2022-04-27). <https://doi.org/10.1364/ol.457213> 초록 기준.
[^p6]: J. Shim 외, Y.-I. Sohn, ACS Photonics 13, 2586-2596 (온라인 2026-04-20). <https://doi.org/10.1021/acsphotonics.6c00117> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: J.-M. Lee 외, L. Pavesi, Photonics Research 11, 1820 (온라인 2023-10-16). <https://doi.org/10.1364/prj.489869> 초록 기준.

# 나노스핀트로닉스 연구실 (Nano Spintronics Laboratory, NSL)

**KAIST 신소재공학과 · 박병국 교수**

- 분야: 스핀-궤도 토크(SOT) 자기 메모리(MRAM)와 무자기장 스위칭, 궤도 토크, 전압 제어 자기 이방성과 스핀 논리·메모리 내 연산, 스핀트로닉스 보안(PUF)과 확률 비트, 스핀 토크·스핀 홀 나노 발진기, 스핀 열전
- 대분야: 전기전자·반도체·광학, 소재
- 태그: 자기 메모리[^p1][^p2][^p3], 메모리 내 연산[^overview][^logic], 하드웨어 보안[^p4], 스핀트로닉스[^p7], 테라헤르츠 분광·소자[^overview][^sto], 열전[^overview][^thermo], 궤도 전자공학[^p3], 확률 컴퓨팅[^p6]
- 홈페이지: <https://nanospin.kaist.ac.kr/>
- 근거와 출처: [NSL 근거 페이지](nanospin-sources.md)

> 전자의 전하뿐 아니라 스핀(전자가 가진 자기적 성질)을 이용해, 전원이 꺼져도 데이터가 남고 전력을 적게 쓰는 메모리와 논리 소자를 만드는 연구실이다. 전류로 나노 크기 자성체의 자화 방향을 빠르게 뒤집는 기술을 중심으로, 메모리 안에서 계산하는 소자, 보안 소자, 고주파 발진기, 열로 전기를 만드는 소자까지 연구한다.[^home][^overview]

## 무엇을 연구하나

연구실은 전자의 스핀을 이용하는 새로운 전자 소재와 소자를 개발하고 자성 나노 구조의 물리를 이해하는 것을 목표로 한다. 스핀트로닉스(스핀을 이용하는 전자공학)가 초저전력 비휘발성 메모리, 다시 구성할 수 있는 논리 소자, 사물인터넷 센서, 에너지 수확 소자에 쓰일 수 있다고 소개한다.[^home] 연구는 네 주제로 나뉜다.[^overview]

첫째이자 중심 주제는 **SOT 기반 자기 메모리(MRAM)**다. MRAM은 얇은 자성 박막의 자화 방향으로 0과 1을 저장하는 비휘발성 메모리다. 자화 방향을 전류로 바꾸는 방식에는 스핀 전달 토크와 스핀-궤도 토크(SOT, 전류가 스핀 흐름으로 바뀌며 자성층의 자화 방향을 돌리는 힘)가 있는데, SOT는 박막 면을 따라 전류를 흘려 소자 신뢰성을 높이고 더 빠르게 뒤집을 수 있어, 연구실은 SOT-MRAM을 기초 물리부터 응용까지 연구한다. 외부 자기장 없이 자화를 뒤집는 무자기장 스위칭과 SOT 효율을 높이는 소재도 함께 다룬다.[^mram] 대표 논문에서는 스핀 흐름의 세 가지 편극 방향을 모두 쓰는 3층 구조로 무자기장 스위칭 전류를 낮췄고,[^p1] 전압으로 스위칭 방향을 바꾸는 방법과,[^p2] 스핀 대신 전자의 궤도 운동을 이용하는 궤도 토크를 크게 키운 구리 산화물 구조를 보였다.[^p3]

둘째는 **스핀 논리 소자**다. SOT-MRAM은 큰 스위칭 전류 때문에 트랜지스터가 커져야 하는 한계가 있어, 연구실은 전압 제어 자기 이방성(전압으로 자화가 선호하는 방향의 세기를 바꾸는 효과)과 SOT 스위칭을 결합해 메모리 안에서 기본 계산을 하는 메모리 내 연산(PIM)용 스핀 논리 소자를 개발한다.[^overview][^logic] 대표 논문에서는 무자기장 SOT 스위칭으로 물리적 복제 방지 기능(PUF, 소자마다 다른 미세한 무작위 차이를 보안에 쓰는 기술) 소자를 만들었고,[^p4] 여러 단계 저항을 가진 메모리 내 연산 소자와,[^p5] 0과 1 사이를 무작위로 오가는 확률 비트를 만들었다.[^p6]

셋째는 **스핀 토크 발진기**다. 전류로 자화를 계속 회전시키면 직류를 기가헤르츠–테라헤르츠 대역 교류로 바꾸는 소자를 만들 수 있고, 연구실은 이를 테라헤르츠 광원·검출기로 발전시키려 한다.[^overview][^sto] 대표 논문에서는 전압으로 스핀 홀 나노 발진기의 주파수를 넓게 바꾸고 그 값을 기억하게 했다.[^p7]

넷째는 **스핀 열전**이다. 열과 스핀의 상호작용으로 열을 전기로 바꾸는 에너지 수확 소자를 연구한다.[^overview][^thermo] 대표 논문에서는 자성층을 산화해 스핀 제벡 효과(온도 차로 생긴 스핀 흐름이 전압을 만드는 현상)를 크게 키웠다.[^p8]

## 주요 연구 주제

### 1. SOT 자기 메모리

3층 구조 무자기장 스위칭, 전압 제어 스위칭 방향, 결정성 구리 산화물 궤도 토크.[^p1][^p2][^p3] 대표 논문 1–3.

### 2. 스핀 논리·보안·메모리 내 연산

스핀트로닉스 PUF, 다단계 SOT 메모리 내 연산 소자, 확률 비트.[^p4][^p5][^p6] 대표 논문 4–6.

### 3. 스핀 토크 발진기

전압으로 주파수를 바꾸는 스핀 홀 나노 발진기.[^p7] 대표 논문 7.

### 4. 스핀 열전

산화로 키운 스핀 제벡 효과.[^p8] 대표 논문 8.

## 대표 논문

랩 논문 목록의 2021–2026년 논문 가운데 박병국 교수가 교신저자(랩 표기 *)이거나 마지막 저자인 것에서 네 연구 주제를 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^papers] |
|---|---|---|---|---|
| 1 | 2022 | [Efficient spin–orbit torque in magnetic trilayers using all three polarizations of a spin current](https://doi.org/10.1038/s41928-022-00735-9) · Nature Electronics | 실용적인 SOT 메모리에는 외부 자기장 없이 낮은 전류로 수직 자화(박막 면에 수직인 방향의 자화)를 뒤집는 기술이 필요하다. 자성층이 들어간 구조의 스핀 흐름은 세 방향의 편극(스핀이 향하는 방향)을 갖는데, 기존 연구는 그 일부만 썼다. 아래 자성층의 자화 쉬운 방향이 기울어진 자성/비자성/자성 3층 구조로 세 편극을 모두 써서 무자기장 스위칭 전류를 낮췄고, 스퍼터링(재료를 원자 단위로 떼어 내 기판에 쌓는 박막 공정)으로 만든 다결정(작은 결정들이 모인) 구조에서도 작동해 양산에 쓸 가능성을 보였다.[^p1] | 1저자 Jeongchun Ryu, 교신 Kyung-Jin Lee·박병국 |
| 2 | 2021 | [Electric-field control of field-free spin-orbit torque switching via laterally modulated Rashba effect in Pt/Co/AlOx structures](https://doi.org/10.1038/s41467-021-27459-2) · Nature Communications | 경계면에서 전자의 스핀과 움직임이 엮이는 라쉬바 효과는 금속에서는 전압으로 조절하기 어려웠다. Pt/Co/AlOx 구조에서 전압으로 라쉬바 효과를 옆 방향으로 다르게 만들어 수직 방향 SOT를 생성해, 외부 자기장 없이 자화를 뒤집고 그 방향을 전기로 바꿨다. 이를 프로그램할 수 있는 스핀 논리-메모리 소자에 쓸 수 있다.[^p2] | 1저자 Min-Gu Kang, 교신 박병국 |
| 3 | 2026 | [Giant Orbital Rashba–Edelstein Effect in Crystalline Cu2O/Cu Heterostructures](https://doi.org/10.1002/adma.73522) · Advanced Materials | 스핀 대신 전자의 궤도 운동 흐름이 만드는 궤도 토크는 SOT의 대안으로 떠오르지만, 주로 쓰인 표면 산화 구리는 구조가 불분명했다. 단결정 구리를 조절해 산화한 결정성 Cu2O/Cu 구조에서 궤도 토크 효율이 자연 산화 구리보다 약 7배 컸고, 구리의 높은 전도도와 합쳐 스핀 토크 전도도가 백금보다 컸다.[^p3] | 1저자 San Ko, 마지막 저자 박병국 |
| 4 | 2022 | [Spintronic Physical Unclonable Functions Based on Field-free Spin-orbit Torque Switching](https://doi.org/10.1002/adma.202203558) · Advanced Materials | IrMn/CoFeB/Ta/CoFeB 구조에서 아래층의 교환 바이어스(반강자성층이 맞닿은 자성층의 자화를 한쪽으로 붙잡는 효과) 방향을 조절해 위층 자화가 뒤집히는 방향이 무작위가 되게 하고, 이를 보안용 PUF의 무작위성 원천으로 썼다. 무작위성·고유성이 높고 다시 설정할 수 있으며, 반복 동작에서 비트 오류가 없고 외부 자기장에도 강했다.[^p4] | 1저자 Soogil Lee, 마지막 저자 박병국 |
| 5 | 2025 | [Multilevel Nanoarray Spin–Orbit Torque Device for Process-in-Memory Applications](https://doi.org/10.1021/acs.nanolett.5c02634) · Nano Letters | 프로세서와 메모리 사이의 데이터 이동이 성능을 막는 문제를 줄이려고, 크기·모양이 다른 여러 자성 섬을 한 소자에 넣어 섬마다 뒤집히는 전류가 다르게 했다. 입력 전류로 여러 단계 저항 상태를 정밀하게 만들어 아날로그 메모리 내 연산을, 펄스 입력과 다단계 저항 출력으로 디지털 논리 연산을 보였고, 외부 자기장 없이 나노초 펄스로 동작했다.[^p5] | 1저자 Daekyu Koh, 교신 Dong-Jun Kim·박병국 |
| 6 | 2026 | [Generation of Probabilistic Bits by Exploiting Orthogonal Spin Currents in Magnetic Trilayers](https://doi.org/10.1002/advs.202524371) · Advanced Science | 확률 비트는 0과 1을 무작위로 오가는 비트로, 확률 컴퓨팅의 핵심이다. 기존 나노 소자 방식은 온도와 크기에 민감했는데, 마이크로미터 크기의 Fe/Ti/CoFeB 구조에서 서로 수직인 두 스핀 흐름의 크기와 부호로 SOT 스위칭 확률을 조절해 안정적인 확률 비트를 만들고, 거꾸로도 계산되는 AND 게이트와 확률적 신경망을 보였다.[^p6] | 1저자 Donghyeon Han, 마지막 저자 박병국 |
| 7 | 2022 | [Voltage-driven gigahertz frequency tuning of spin Hall nano-oscillators](https://doi.org/10.1038/s41467-022-31493-z) · Nature Communications | 스핀 홀 나노 발진기(전류로 자화를 계속 회전시켜 고주파 신호를 내는 소자)는 뉴로모픽 계산에 쓸 수 있지만, 전압으로 바꿀 수 있는 주파수는 메가헤르츠 범위였고 유지되지 않았다. 전압 제어 자기 이방성으로 주파수를 최대 2.1 GHz 범위까지 바꾸고, 전압 펄스를 반복하면 주파수가 누적되게 해 생물 시냅스의 강화·약화를 흉내 냈다.[^p7] | 1저자 Jong-Guk Choi, 교신 Kab-Jin Kim·박병국 |
| 8 | 2023 | [Enhanced spin Seebeck effect via oxygen manipulation](https://doi.org/10.1038/s41467-023-39116-x) · Nature Communications | 스핀 제벡 효과는 넓은 면적의 폐열을 간단한 구조로 쓸 수 있지만 변환 효율이 낮다. W/CoFeB/AlOx 구조에서 전압으로 CoFeB 경계면을 산화하자 열전 신호가 10배 정도 커졌고, 산화된 자성층의 약해진 교환 상호작용이 원인이라고 설명했다.[^p8] | 1저자 Jeong-Mok Kim, 교신 박병국 |

## 교수와 전문 분야

박병국 교수는 한양대 금속공학 학사(1994, 최우등), KAIST 재료공학 석사(1999)·박사(2003)를 받았다. 네덜란드 트벤테대 박사후연구원(2003–2006), 영국 히타치 케임브리지 연구소 연구원(2006–2011)을 거쳐 2011년 12월 KAIST 신소재공학과에 부임했고, 2022년 9월부터 교수다. 2020년 케임브리지대 캐번디시 연구소 방문교수를 지냈다.[^prof] 2025년 KAIST 지정석좌교수로 선정됐다고 랩 소식이 적는다.[^news]

교수 페이지는 반강자성체/강자성체/산화물 구조에서 외부 자기장 없이 수직 자화를 SOT로 뒤집은 연구(Nature Nanotechnology, 2016), 반강자성체 기반 터널 접합의 스핀 밸브형 자기저항(Nature Materials, 2011), 스핀 홀 효과 트랜지스터(Science, 2010, 공동 1저자) 등을 주요 논문으로 든다. 같은 페이지에 적힌 수상으로는 KAIST Academic Awards of the year(2022), 과학기술정보통신부 Top Scientist of the Month(2019년 10월), Top 100 National R&D excellence(2018), KAIST's TOP 10 Research Achievements(2018), 한국자기학회 Academic Award(2018), Hitachi Kenkai Research and Development Award(2009) 등이 있다.[^prof] 랩 특허 게시판에는 자기 로직 소자, SOT 자기 메모리, 테라헤르츠 자기 나노 발진 소자, 열전 변환 소자 등 국내외 특허 15건이 있다.[^patents]

논문으로 보면 전문 분야는 세 갈래다.

- **SOT 자기 메모리와 무자기장 스위칭, 궤도 토크**.[^p1][^p2][^p3]
- **스핀트로닉스 기반 보안·메모리 내 연산·확률 컴퓨팅 소자**.[^p4][^p5][^p6]
- **스핀 홀 나노 발진기와 스핀 열전**.[^p7][^p8]

## 응용 분야

대표 논문으로 보면 차세대 비휘발성 메모리와 그 양산 공정, 메모리 안에서 계산하는 AI 반도체, 하드웨어 보안, 확률 컴퓨팅, 뉴로모픽 소자, 폐열 이용 열전 소자에 닿아 있다.[^p1][^p4][^p5][^p6][^p7][^p8] 졸업생은 삼성전자, SK하이닉스, KIST, 한국표준과학연구원 등과 가천대 교수, 일본 도호쿠대 조교수로 진출했다.[^alumni][^news]

## 구성원

2026년 10월 20일 랩 Current 페이지 기준이다. 이름은 랩 표기(성, 이름)를 따랐고 이메일은 랩이 적은 학교 주소다.[^members] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| Kim, Dong-Jun | 박사후연구원 | djkim21c@kaist.ac.kr | 5 |
| Ko, San | 박사후연구원 | kosan32@kaist.ac.kr | 3, 4 |
| Seo, Jangbum | 박사과정 |  |  |
| Seo, Hyeong-Joo | 박사과정 |  |  |
| Kang, MinSeok | 박사과정 | kms3229@kaist.ac.kr | 3, 5, 6 |
| Shin, Soyoung | 박사과정 | ssy1109@kaist.ac.kr |  |
| Kim, Jaegeon | 석사과정 | keemjg@kaist.ac.kr |  |
| Kim, Sunghoon | 석사과정 | sh1114@kaist.ac.kr | 3 |
| You, Joonho | 석사과정 | jackjunho@kaist.ac.kr |  |
| Kim, Junhee | 석사과정 | junhee@kaist.ac.kr |  |
| Lee, Gyeongju | 석사과정 | rudwn0131@kaist.ac.kr |  |
| Kim, Geonah | 석사과정 | kga810@kaist.ac.kr |  |
| Park, Chaebin | 석사과정 | cbpark@kaist.ac.kr |  |
| Tran, Van Duong | 석사과정 | vanduongtran@kaist.ac.kr |  |
| Ha, yeongju | 학부 연구생 | gk0wn@kaist.ac.kr |  |
| Lee, Changho | 학부 연구생 | kevin070419@kaist.ac.kr |  |

## 졸업생과 이전 구성원

랩 Alumni 페이지의 이름, 과정·기간, 랩이 적은 현재 소속이다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Kim, Geunwoo | Ph.D. (2023.03~2026.08) |  |
| Koh, Daekyu | Integrated Master's/Doctoral Cource (2020.03~2026.02) | Korea Institute of Science and Technology (KIST) |
| Kim, Eunseok | M.S. (2024.03~2026.02) | Samsung Electronics |
| Na, Hyeri | M.S. (2024.03~2026.02) | SK Hynix |
| Han, Donghyeon | Ph.D. (2021.03~2025.08) | KRISS |
| Kim, Hyun-Bin | Ph.D. Materials Science and Engineering (2016.03~2025.0.2) |  |
| Park, Yeon Su | M.S. Materials Science and Engineering (2022.09~2025.02) | SK Hynix |
| Kang, Jaimin | Ph.D. (2020.09~2024.08) | Post-doctoral researcher, Northwestern Univ. |
| Hwang, In Kook | Ph.D. (2021.03~2024.08) | Post-doctoral researcher, KIST |
| Kim, Namhee | M.S. Materials Science and Engineering (2022.09~2024.08) | Samsung Electronics |
| Takayuki Shiino | Post-doctoral researcher (2022.04~2024.02) | Post-doctoral researcher, Spintronic materials and device,Barcelona Spain |
| Jeong, Jimin | Ph.D. Candidate (2020.03~2024.02) | Samsung Electronics |
| Lee, Soogil | Post-doctoral researcher (2019.03~2023.08.) | Professor, Gachon Univ. |
| Choi, Jong-Guk | Post-doctoral researcher (2022.10~2023.05) | Post-doctoral researcher, University of Gothenburg |
| Lee, Sanghwa | M.S. (2021.03~2023.02) | SK Hynix |
| Kang, Min-Gu | Ph.D. Materials Science and Engineering (2019.09~2022.08) | Assistant Professor, Tohoku Univ. |
| Kim, Jeong-Mok | Ph.D. Materials Science and Engineering (2018.03~2022.02) | Samsung Electronics |
| Lee, Sungjun | M.S. (2020.03~2022.02) | Samsung Electronics |
| Ryu, Jeongchun | Post-doctoral researcher (2018.04~2021.04) | Post-doctoral researcher, MIT |
| Kim, Dohyoung | M.S. (2019.03~2021.02) |  |
| Choi, Gaeun | M.S. (2019.03~2021.02) | Samsung Electronics |
| Kim, Yoon-Ui | Ph.D. Candidate (2019.09~2020.09) |  |
| Lee, Jae-Wook | Ph.D. (2016.03~2020.02) | Samsung Electronics |
| Park, June-Young | Ph.D. (2015.03~2020.02) | Samsung Electronics |
| Oh, Young-Wan | Ph.D. Candidate (2014.03~2019.02) | Samsung Electronics |
| Yun, Seok Jin | Ph.D. (2013.03~2018.02) | LG chemistry |
| Han, Min-Wook | M.S. (2016.03~2018.02) | Samsung Electronics |
| Kim, Dong-Jun | Ph.D. (2013.03~2018.02) | Post-doctoral researcher, National University of Singapore |
| Jeon, Chul-Yeon | M.S. (2015.09~2017.08) | Ph.D., Swiss Federal Institute of Technology Lausanne. |
| Baek, Seung-Heon | Ph.D. (2013.02~2017.08) | Korea Institute of Science and Technology (KIST) |
| Park, Kyung-Woong | Ph.D. (2013.09~2017.08) | SK Hynix |
| Kim, Dae-Hoon | M.S. Materials Science and Engineering (2015.03~2017.02) | Samsung electronics |
| Lee, Hae-Yeon | Ph.D. Candidate (2016.09~2016.05) | Professor, Rice Univ. |
| Lee, Kyeong-Dong | Research Fellow (2013.09~2016) |  |
| Cho, Soon-Ha | M.S. Materials Science and Engineering (2013.02~2015.02) | Samsung electronics |
| Kim, Young-Min | Post-doctoral researcher (2013.08~2015.02) |  |
| Park, Hee-Gyum | Researcher (2012.02~2013.08) | Ph.D., KIST |

## 최근 논문 목록 (2021–2026)

랩 Journals 게시판의 2021년 이후 논문이다. 저자 이름 뒤 *는 교신저자를 뜻하는 랩 표기다.[^papers]

**2026**

- Donghyeon Han, Chaehyeon Shin, Seok‐Jong Kim, Yunho Jang, Daekyu Koh, Taehwan Kim, Jaeheon Jung, Geon‐Woo Baek, Minseok Kang, Eunseok Kim, Geun‐Hee Lee, Jeongchun Ryu, Makoto Kohda, Junsaku Nitta, Kab‐Jin Kim, Jongsun Park, Kyung‐Jin Lee, Byong‐Guk Park. "Generation of Probabilistic Bits by Exploiting Orthogonal Spin Currents in Magnetic Trilayers". *ADVANCED SCIENCE*.
- Hyeong-Joo Seo, Seok-Jong Kim, Phuoc Cao Van, Hong-Cuong Truong, Dong-Hyeon Han, Geunwoo Kim, Younghun Jo, Jong Hoon Jung, Soojung Kim, Chun-Yeol You, Jong-Ryul Jeong, Kyung-Jin Lee, Byong-Guk Park. "Néel-Vector-Dependent Unconventional Spin-Orbit Torque for Deterministic Field-Free Switching in NiO (110)-Based Trilayers". *ADVANCED SCIENCE*.
- San Ko, Jaimin Kang, Su Jae Kim, Hanhwi Jang, Do-Kyeong Nam, Minseok Kang, Sunghoon Kim, Yeon Sik Jung, Se-Young Jeong, Kab-Jin Kim, Byong-Guk Park. "Giant Orbital Rashba–Edelstein Effect in Crystalline Cu2O/Cu Heterostructures". *Advanced Materials*.
- Minwoo Yu, Moojune Song, Minseok Kang, Mujin You, Yunyoung Hwang, Albert Min Gyu Park, Byong-Guk Park, Kab-Jin Kim, and Junho Suh. "Effect of magnetic anisotropy on magnetoelastic waves in a Ni/LiNbO3 hybrid device". *Physical Review Applied*.
- Yeon-Su Park, Jimin Jeong, Jaimin Kang, Donghyeon Han, San Ko, Kab-Jin Kim, and Byong-Guk Park. "Reconfigurable optical physical unclonable functions based on voltage-controlled magnetic anisotropy". *APL Materials*.
- San Ko, Hyunjin Kim, Donghyeon Han, Jaimin Kang, Phuoc Cao Van, Wonyeong Choi, Sanghoon Kim, Jong-Ryul Jeong, Byong-Guk Park, Albert Min Gyu Park, Kyoung-Whan Kim, Kab-Jin Kim. "Antiferromagnetic domain wall in ferrimagnetic bilayers controlled by magnetic spin Hall effect". *npj Spintronics*.
- JH Yun, K Sim, YS Park, IK Hwang, SH Lim, BG Park\*, H Park\*, SC Baek\*. "Dielectric Capacitance–Voltage Response as a Predictor of Voltage‐Controlled Magnetic Anisotropy Efficiency". *Advanced Materials Interfaces*.
- Geunwoo Kim, Takayuki Shiino, Geun-Hee Lee, Phuoc Cao Van, Jong-Ryul Jeong, Kyung-Jin Lee, and Byong-Guk Park\*. "Electrical Manipulation of Magnon Diffusion Length in Pt/YIG Three-Terminal Devices". *Nano Letters*.

**2025**

- In Cheol Yu, San Ko, Won Tae Kim, Byong-Guk Park, Byoung S. Ham, Kab-Jin Kim & Fabian Rotermund. "Photon energy-dependent ultrafast magnetization dynamics in magnetic heterostructures". *Communications Materials*.
- Daekyu Koh, Dong-Jun Kim\*, Taehwan Kim, Minseok Kang, Duc Duong Viet, Hyejin Hong, Jong-Ryul Jeong, Jongsun Park, and Byong-Guk Park\*. "Multilevel Nanoarray Spin–Orbit Torque Device for Process-in-Memory Applications". *Nano Letters, 25, 1243–1249*.
- Gyung-Min Choi, OukJae Lee, Sunjae Chung, Woojin Kim, Taeyoung Lee, Byong-Guk Park, Seungmo Yang. "Spintronics and magnetic memory devices". *Advances in Physics: X, 10, 1*.
- Dong-Jun Kim, Beom Jin Kim, Heechang Shin, Jeongkeun Kim, Yuchen Pu, Shuhan Yang, Xinhou Chen, Byong-Guk Park, Jong-Hyun Ahn\*, and Hyunsoo Yang\*. "Bio-Resorbable Magnetic Tunnel Junctions". *Advanced Materials, Online*.
- So y. Shin, Donghyeon Han, Soogil Lee\*, and Byong-Guk Park\*. "Enhanced Magnetization Switching Efficiency via Orbital-Current-Induced Torque in Ti/Ta (Pt)/CoFeB/MgO Structures". *Advanced Functional Materials, 35, 2425932*.
- Hyun-jun Lee, Ji-won Yoon, Soeun Ahn, Dong-Soo Han, Byong-Guk Park, Byeong-kwon Ju\*, and Seung-heon Chris Baek\*. "Efficiency Enhancement in Spin-Orbit Torque MRAM with Low Resistivity and High Spin Hall Angle in Ta/Pt Multilayer Channel". *IEEE Transactions on Magnetics, 61(5), 3400805*.
- Min-Gu Kang, Soogil Lee\*, and Byong-Guk Park\*. "Field-free spin-orbit torques switching and its applications". *npj Spintronics, 3, 8*.
- Jimin Jeong, Yeon Su Park, Min-Gu Kang\*, and Byong-Guk Park\*. "Nanosecond Magneto-Ionic Control of Magnetism Using a Resistive Switching HfO2 Gate Oxide". *Adv. Electron. Mater., 11, 2400535*.
- In-Kook Hwang, Min Gu Lee, Jae Bum Jeon, Sang Hyun Nam, Daseul Lee, Changhyeon Lee, Junyoung Kwon, Sung-Gap Im, Young-Hoon Kim\*, Kyung Min Kim\*, and Byong-Guk Park\*. "Visible-Light Chiral Photonic Synapses Based on Hybrid Organic-Inorganic 2D Perovskites". *Adv. Electron. Mater., 11, 2400525*.
- Won-Bin Lee, Seongmun Hwang, Hye-Won Ko, Byong-Guk Park, Kyung-Jin Lee\*, and Gyung-Min Choi\*. "Spin-torque-driven gigahertz magnetization dynamics in the non-collinear antiferromagnet Mn3Sn". *Nature Nanotechnol., 20, 487-493*.
- In Cheol Yu, Jung Hyun Oh, Je-Ho Shim, Kab-Jin Kim, Byong-Guk Park, Dong-Hyun Kim, Kyoung-Whan Kim, Hyun-Woo Lee, Kyung-Jin Lee\*, and Fabian Rotermund\*. "Laser-induced coherent spin change due to spin-orbit coupling". *npj Spintronics, 3, 4*.

**2024**

- Sang J. Park, Phuoc Cao Van, Min-Gu Kang, Hyeon-Jung Jung, Gi-Yeop Kim, Si-Young Choi, Jung-Woo Yoo, Byong-Guk Park, Se Kwon Kim\*, Jong-Ryul Jeong\* and Hyungyu Jin\*. "Enhancing spin pumping by nonlocal manipulation of magnon temperature". *Matter, 7, 12*.
- Junyeong Choi, Geun-Hee Lee, Jiseok Yang, Jaimin Kang, Byong-Guk Park, Albert Min Guy Park, and Kab-Jin Kim\*. "Questioning the validity of spintronic inductors: Potential artifacts in emergent inductance". *Applied Physics Letters, 125, 19*.
- Takayuki Shiino, Phuoc Cao Van, Jong-Guk Choi, Geunwoo Kim, Jong-Ryul Jeong, and Byong-Guk Park\*. "Unconventional angular dependence of spin-orbit torque-induced harmonic Hall resistance in Pt/YIG bilayers". *npj Spintronics, 2, 43*.
- Min-Gu Kang, In-Kook Hwang, Hee-Chang Kyung, Jaimin Kang, Donghyeon Han, Soogil Lee, Junyoung Kwon, Kyung-Jin Lee, Jihyeon Yeom\*, and Byong-Guk Park\*. "Room temperature chiral magnetoresistance in a chiral-perovskite-based perpendicular spin valve". *APL Mater, 12, 081118*.
- Viet Dongquoc, Phuoc Cao Van, Rambabu Kuchi, Trinh Nguyen Thi, Duc Duong Viet, Eui-Tae Kim, Byong-Guk Park, Ji-Wan Kim, and Jong-Ryul Jeong\*. "Extraordinary enhancement of magneto-optical Faraday rotation angle in Bi-YIG/Pt/glass prepared by metal organic decomposition method". *Surfaces and Interfaces, 51, 104652*.
- Jimin Jeong, Yunho Jang, Min-Gu Kang, Seungeon Hwang, Jongsun Park, and Byong-Guk Park\*. "Spintronic Artificial Synapses Using Voltage-Controlled Multilevel Magnetic States". *Adv. Electron. Mater., 10(8), 2300889*.
- Jaimin Kang, Donghyeon Han, Kyungchul Lee, San Ko, Daekyu Koh, Chando Park, Jaesoo Ahn, Minrui Yu, Mahendra Pakala, Sujung Noh, Hansaem Lee, JoonHyun Kwon, Kab-Jin Kim, Jongsun Park, Soogil Lee\*, Jisung Lee\*, and Byong-Guk Park\*. "Highly Reliable Magnetic Memory-Based Physical Unclonable Functions". *ACS Nano, 18, 20, 12853-12860*.
- Kyoung-Whan Kim\*, Byong-Guk Park, and Kyung-Jin Lee. "Spin current and spin-orbit torque induced by ferromagnets". *npj Spintronics, 2, 8*.
- Thanh-Huong Thi Nguyen, Jungmin Park, Jae-Hyun Ha, Soogil Lee, Van Quang Nguyen, Nyun Jong Lee, Byong-Guk Park, Sunglae Cho, Jung-Il Hong\*, and Sanghoon Kim\*, Physical Review Materials, 8. "Giant anisotropy of magnetic damping in an epitaxial Cr/Fe bilayer with the absence of magnetocrystalline anisotropy". *L041401*.
- Qu Yang, Donghyeon Han, Shishun Zhao, Jaimin Kang, Fei Wang, Sung-Chul Lee, Jiayu Lei, Kyung-Jin Lee, Byong-Guk Park, and Hyunsoo Yang\*. "Field-free spin–orbit torque switching in ferromagnetic trilayers at sub-ns timescales". *Nature Communications, 15, 1814*.

**2023**

- Geunwoo Kim, Soogil Lee\*, Sanghwa Lee, Byonggwon Song, Byung-Kyu Lee, Duhyun Lee, Jin Seo Lee, Min Hyeok Lee, Young Keun Kim and Byong-Guk Park\*. "The Influence of Capping Layers on Tunneling Magnetoresistance and Microstructure in CoFeB/MgO/CoFeB Magnetic Tunnel Junctions upon Annealing". *Nanomaterials, 13(18), 2591*.
- Daekyu Koh, Jaimin Kang, Taehwan Kim, Jisung Lee, Sujung Noh, Hansaem Lee, JoonHyun Kwon, Soogil Lee, Jongsun Park, Byong-Guk Park\*. "Improved Robustness against Magnetic Field in Spin–Orbit-Torque-Based Physical Unclonable Functions through Write-Back Operation". *Adv. Electron. Mater., 9, 2201073*.
- Jeong-Mok Kim, Seok-Jong Kim, Min-Gu Kang, Jong-Guk Choi, Soogil Lee, Jaehyeon Park, Cao Van Phuoc, Kyoung-Whan Kim, Kab-Jin Kim, Jong-Ryul Jeong, Kyung-Jin Lee & Byong-Guk Park\*. "Enhanced spin Seebeck effect via oxygen manipulation". *Nature Communications, 14, 3365*.
- Taekhyeon Lee, Jisu Kim, Suhyeok An, Seyeop Jeong, Donghyeon Lee, Dongchan Jeong, Nyun Jong Lee, Ki-Seung Lee, Chun-Yeol You, Byong-Guk Park, Kab-Jin Kim, Sanghoon Kim, and Soogil Lee. "Field-free spin-orbit torque switching of GdCo ferrimagnet with broken lateral symmetry by He ion irradiation". *Acta Materialia, 246, 118705*.
- Dongwook Go, Daegeun Jo, Kyoung-Whan Kim, Soogil Lee, Min-Gu Kang, Byong-Guk Park, Stefan Blügel, Hyun-Woo Lee, and Yuriy Mokrousov. "Long-Range Orbital Torque by Momentum-Space Hotspots". *Phys. Rev. Lett., 130, 246701*.
- Jungkyun Kim, Hakseung Rhee, Myeong Won Son, Juseong Park, Gwangmin Kim, Jae Bum Jeon, Hanchan Song, Geunwoo Kim, Byong-Guk Park, Jeong Hwan Han\*, and Kyung Min Kim\*. "Electromigration Reliability of Barrierless Ruthenium and Molybdenum for Sub-10 nm Interconnection". *ACS Appl. Electron. Mater., 2447-2453*.
- Ji-Hwan Seol, Jae-Hyeon An, Gun-Woo Park, Trinh Nguyen Thi, Duc Duong Viet, Byong-Guk Park, Phuoc Cao Van, Jong-Ryul Jeong. "Development of an annealing process for rapid fabrication of solution-based Y3Fe5O12 thin films". *Thin Solid Films, 774, 139846*.
- Nyun Jong Lee, Heechan Jang, Eunkang Park, Ki-Seung Lee, Seyeop Jeong, Soogil Lee, Byong-Guk Park, Chun-Yeol You, Kyoung-Whan Kim, and Sanghoon Kim. "Quantitative analysis of magnon characteristics with unidirectional magnetoresistance". *Phys. Rev. Applied, 20, 064006*.
- Stanley Abbey, Hanhwi Jang, Brakowaa Frimpong, Naveen Kumar, Woo Hyun Nam, Van Quang Nguyen, Jong Ho Park, Chien Viet Nguyen, Hosun Shin, Jae Yong Song, Su-Dong Park, Sunglae Cho, Chandan Bera, Jaimin Kang, Byong-Guk Park, Muath. "Twisted grain boundary leads to high thermoelectric performance in tellurium crystals". *Energy Environ. Sci., 16, 125-137*.
- Hyun Bin Kim, Seung-Hwan Oh, Young Gyu Jeong, Han Soo Kim, Byong-Guk Park, and Jong-Seok Park. "Effects of heat treatment on the microstructure and flexural mechanical properties of carbon fiber reinforced composite cured by electron beam". *Materials Today Communications, 37, 107181*.

**2022**

- Jong-Guk Choi, Jaehyeon Park, Min-Gu Kang, Doyoon Kim, Jae-Sung Rieh, Kyung-Jin Lee, Kab-Jin Kim\* and Byong-Guk Park\*. "Voltage-driven gigahertz frequency tuning of spin Hall nano-oscillators". *Nature Communications, 13, 3783*.
- Jeongchun Ryu, Ryan Thompson, Jae Yeol Park, Seok-Jong Kim, Gaeun Choi, Jaimin Kang, Han Beom Jeong, Makoto Kohda, Jong Min Yuk, Junsaku Nitta, Kyung-Jin Lee\* and Byong-Guk Park\*. "Efficient spin–orbit torque in magnetic trilayers using all three polarizations of a spin current". *Nature Electronics, 5, 217–223*.
- Soogil Lee, Jaimin Kang, Jeong-Mok Kim, Namhee Kim, Donghyeon Han, Taekhyeon Lee, San Ko, Jiseok Yang, Sanghwa Lee, Sungjun Lee, Daekyu Koh, Min-Gu Kang, Jisung Lee, Sujung Noh, Hansaem Lee, JoonHyun Kwon, Seung-heon Chris Baek, Kab-Jin Kim, and Byong-Guk. "Spintronic Physical Unclonable Functions Based on Field-free Spin-orbit Torque Switching". *Advanced Materials, 34, 2203558*.
- Gaeun Choi, Jeongchun Ryu\*, Ryan Thompson, Jong-Guk Choi, Jimin Jeong, Sungjun Lee, Min-Gu Kang, Makoto Kohda, Junsaku Nitta, and Byong-Guk Park\*. "Thickness dependence of spin–orbit torques in Pt/Co structures on epitaxial substrates". *APL Materials, 10, 011105*.
- Jimin Jeong, Min-Gu Kang, Soogil Lee, Jaimin Kang, Kyung-Jin Lee, and Byong-Guk Park\*. "Reduced Spin-Orbit Torque Switching Current by Voltage-Controlled Easy-Cone States". *Advanced Functional Materials, 32 (8), 2107944*.
- Gaeun Choi,Jeongchun Ryu,Sungjun Lee,Jaimin Kang,Namgyu Noh,Jong Min Yuk,Byong-Guk Park. "Thickness Dependence of Interface-Generated Spin Currents in Ferromagnet/Ti/CoFeB Trilayers". *Adv. Mater. Interfaces, 2201317*.
- Taehwan Kim, Yunho Jang, Min-Gu Kang, Byong-Guk Park, Kyung-Jin Lee, Jongsun Park. "SOT-MRAM Digital PIM Architecture With Extended Parallelism in Matrix Multiplication". *IEEE Transactions on Computers, 71, 2816-2828*.
- Ji-Ho Park, Won Tae Kim, Woonjae Won, Jun-Ho Kang, Soogil Lee, Byong-Guk Park, Byoung S. Ham, Younghun Jo, Fabian Rotermund & Kab-Jin Kim. "Observation of spin-glass-like characteristics in ferrimagnetic TbCo through energy-level-selective approach". *Nature Communications, 13, 5530*.
- Taehwan Kim, Yunho Jang, Student Member, Min-Gu Kang, Byong-Guk Park, Kyung-Jin Lee, and Jongsun Park. "SOT-MRAM Digital PIM Architecture with Extended Parallelism in Matrix Multiplication". *IEEE*.

**2021**

- Min-Gu Kang, Jong-Guk Choi, Jimin Jeong, Jae Yeol Park, Hyeon-Jong Park, Taehwan Kim, Taekhyeon Lee, Kab-Jin Kim, Kyoung-Whan Kim, Jung Hyun Oh, Duc Duong Viet, Jong-Ryul Jeong, Jong Min Yuk, Jongsun Park, Kyung-Jin Lee, and Byong-Guk Park\*. "Electric-field control of field-free spin-orbit torque switching via laterally modulated Rashba effect in Pt/Co/AlOx structures". *Nature Communications, 12, 7111*.
- Jaimin Kang, Jeongchun Ryu\*, Jong-Guk Choi, Taekhyeon Lee, Jaehyeon Park, Soogil Lee, Hanhwi Jang, Yeon Sik Jung, Kab-Jin Kim, and Byong-Guk Park\*. "Current-induced manipulation of exchange bias in IrMn/NiFe bilayer structures". *Nature Communications, 12, 6420*.
- Soogil Lee, Min-Gu Kang, Dongwook Go, Dohyoung Kim, Jun-Ho Kang, Taekhyeon Lee, Geun-Hee Lee, Jaimin Kang, Nyun Jong Lee, Yuriy Mokrousov, Sanghoon Kim, Kab-Jin Kim, Kyung-Jin Lee, and Byong-Guk Park\*. "Efficient conversion of orbital Hall current to spin current for spin-orbit torque switching". *Communications Physics, 4, 234*.
- Ryan Thompson, Jeongchun Ryu\*, Gaeun Choi, Shutaro Karube, Makoto Kohda, Junsaku Nitta, and Byong-Guk Park\*. "Anisotropic Spin-Orbit Torque through Crystal-Orientation Engineering in Epitaxial Pt". *Phys. Rev. Applied, 15, 014055*.
- Soogil Lee, Jeongchun Ryu, and Byong-Guk Park \*. "Magnetization switching through symmetry". *Nature Nanotechnology (News & Views), 16, 227-228*.
- Yunho Jang, Student Member, IEEE, Gyuseong Kang, Taehwan Kim, Student Member, IEEE, Yeongkyo Seo, Kyung-Jin Lee, Member, IEEE, Byong-Guk Park, Member, IEEE, and Jongsun Park, Senior Member, IEEE. "Stochastic SOT device based SNN architecture for On-chip Unsupervised STDP Learning". *IEEE, 1 - 1*.
- Seyeop Jeong, Jongmin Lee, Soogil Lee, Jungmin Park, Donghyeon Lee, Jimin Jeong, Heechan Jang, Eunkang Park Younghun Jo, Nyun Jong Lee, Kyoung-Whan Kim, Byong-Guk Park, Sanghan Lee, Tae Heon Kim, and Sanghoon Kim. "Enhanced spin–orbit torque in Ni81Fe19/Pt bilayer with NdNiO3 contact". *Applied Physics Letters, 119, 212402*.
- Thanh Huong Thi Nguyen, Van Quang Nguyen, Seyeop Jeong, Eunkang Park, Heechan Jang, Nyun Jong Lee, Soogil Lee, Byong-Guk Park, Sunglae Cho, Hyun-Woo Lee\*, Jung-Il Hong\* & Sanghoon Kim\*. "Unidirectional spin Hall magnetoresistance in epitaxial Cr/Fe bilayer from electron-magnon scattering". *Communications physics, 4, 247*.
- Lee, D., Go, D., Park, HJ., Jeong WM., Ko HW., Yun DK., Jo DG., Lee. SG., Go GC., Oh HJ., Kim KJ., Park BG., Min BC., Koo HC., Lee HW.\*, Lee. OJ.\* & Lee. KJ. \*. "Orbital torque in magnetic bilayers". *Nature communications, 12, 6710*.
- 고산, 이근희, 김갑진\*, 박병국. "스핀-궤도 토크 기반 자구벽 다수결 소자". *한국자기학회지, 31, 208-213*.
- Jun-Ho Kang, Albert Min Gyu Park, Soogil Lee, Dohyoung Kim, Seyeop Jung, Sanghoon Kim, Byong-Guk Park, Kab-Jin Kim, et al. "Unconventional Hall effect in metal/ semiconductor hybrid spintronic devices". *Applied Physics Letters, 119, 112401*.
- Ji‑Ho Park, Hye‑Won Ko, Jeong‑Mok Kim, Jungmin Park, Seung‑Young Park, Younghun Jo, Byong‑Guk Park, Se Kwon Kim, Kyung‑Jin Lee\* & Kab‑Jin Kim\*. "Temperature dependence of intrinsic and extrinsic contributions to anisotropic magnetoresistance". *Scientific Reports, 11, 20884*.
- Sungjung Joo, Rekikua Sahilu Alemayehu, Jong-Guk Choi, Byong-Guk Park and Gyung-Min Choi\*. "Magnetic anisotropy and damping constant of Ferrimagnetic GdCo alloy near compensation point". *Materials, 14, 2604*.
- Eui Young Choi, Seok Hyeon Hong, Byong-Guk Park, Prahallad Padhan, Wilfrid Prellier, Seung Young Park, Younghun Jo, Byeong Cheol Min, Ji Won Seo\*. "Current-controlled magnetization using interfacial localizations in heterostructures". *Applied Surface Science, 557, 149871*.
- Trinh Nguyen Thi, Phuoc Cao Van, Duc Duong Viet, Veit Dong Quoc, Ha-yeong Ahn, Viet Anh Cao, Ming-Gu Kang, Byoung-Guk Park\*, and Jong-Ryul Jeong\*. "Morphology-dependent spin Seebeck effect in yttrium iron garnet thin films prepared by metal-organic decomposition". *Ceramics International, 47, 16770-16775*.

## 특허

랩 Patents 게시판의 특허와 출원·등록 번호다.[^patents]

- Magnetic logic device / 자기 로직 소자 (발명자 박병국,김갑진, 이근희; 등록번호 US11362661)
- 게이트 전극을 구비한 자기 소자 / Magnetic Device With Gate Electrode (발명자 박병국, 강민구, 최종국; 출원번호 1020200147207; 등록번호 10-2361064-0000)
- Semiconductor device and semiconductor logic device / 반도체소자 (발명자 박병국, 백승헌, 박경웅; 등록번호 US11205466)
- 자기 로직 소자 / Magnetic Logic Device (발명자 박병국, 김갑진, 이근희; 출원번호 10-2020-0054160; 등록번호 10-2284925)
- 스핀궤도 토크 자기 소자 / Field-free spin-orbit torque based magnetic memory (발명자 박병국,류정춘,강재민; 출원번호 대한민국 10-2019-0114593)
- 저전력 테라헤르쯔 자기 나노 발진 소자 / Low-Power Terahertz Magnetic Nano-oscillators (발명자 박병국, 이경진; 출원번호 대한민국 10-2018-0030023, 10-2019-0162795; 등록번호 대한민국 10-2055999-0000)
- SOT 반도체 소자 및 SOT 반도체 소자의 기록 방법 / SOT Semiconductor Device and Method of Writing Data to SOT Semiconductor Device (발명자 박병국,백승헌; 출원번호 대한민국 10-2017-0117642; 등록번호 대한민국 10-2024876-0000)
- 반도체 소자 및 반도체 로직 소자 / Semiconductor Device and Semiconductor Logic Device (발명자 박병국,백승헌,박경웅; 출원번호 대한민국 10-2017-0101259, US 16285948, CN 201780065165.9, PCT/KR2017/009212)
- 반도체 소자, 반도체 소자 제어 방법 및 광학 스위치 / Semiconductor device, semiconductor device control method and thermo optic switch (발명자 박병국,김동준,전철연; 출원번호 대한민국 10-2017-0005900, 10-2018-0003639, US 15868837; 등록번호 대한민국 10-2060183-0000, US 10,276,780)
- 반도체 소자 / Semiconductor Device (발명자 박병국, 백승헌, 박경웅; 출원번호 대한민국 10-2016-0137412, 10-2019-0046436, US 15723278, JP 2017-203154; 등록번호 대한민국 10-1998268-0000, US 10,360,963)
- 자기 메모리 소자 / Magnetic memory using in-plane current and the method to enhance its efficiency (발명자 박병국, 이해연; 출원번호 대한민국 10-2016-0003151, US 15346170; 등록번호 대한민국 10-1829452-0000)
- 자기 메모리 소자 / Field-free spin-orbit spin transfer torque magnetic random access memory (발명자 박병국,이경진,이현우; 출원번호 대한민국 10-2015-0066853, 10-2016-0125429; 등록번호 대한민국 10-1683440-0000)
- 열전변환 소자 및 그 제조방법 / Thermoelectric conversion device and the manufacturing method thereof (발명자 박병국, 김동준; 출원번호 대한민국 10-2015-0068080; 등록번호 대한민국 10-1685640-0000)
- 자기저항 소자 / Magnetoresistive device (발명자 박병국; 등록번호 EP 2 065 886, US 7,939,870, JP 2009-130371A, CN 100440372C)
- 자기저항 램 및 그의 제조방법 / Magneto-resistive random access memory and method for manufacturing the same (발명자 박병국; 등록번호 대한민국 10-08295560-0000)

## 수상

교수 페이지에 적힌 수상이다.[^prof]

- 2022 Academic Awards of the year, KAIST
- 2021 Best Lecture Awards of the year, KAIST
- Top Scientist of the Month, Oct. 2019: “Development of high efficient spin current generating materials” by Ministry of Science and ICT
- Top 100 National R & D excellence in 2018: “Development of thermal spin current generation” by Ministry of Science and ICT
- KAIST’s TOP 10 Research Achievements of 2018: “Development of reconfigurable spin-based logic device”
- Academic Award 2018 by The Korean Magnetic Society
- 100 Future Technologies and Leading Scientists: “Next generation memory device” by National Academy of Engineering of Korea (2017)
- Top 10 Science News of the Year: “Development of next generation MRAM materials” by the Korean Federation of Science and Technology Societies (2016)
- Hitachi Kenkai Research and Development Award 2009 (Best researcher in Hitachi group)
- 2019 Technology Innovation Awards of College of Engineering, KAIST

## 소식

랩 News 게시판의 2021년 이후 논문·수상·진로 소식이다.[^news]

- 2026-09-02 · 한동현 박사님 Advanced Science 게재
- 2026-09-02 · 박사과정 서형주 학생 Advanced Science 게재
- 2026-09-02 · 박사과정 고산 학생 Advanced Materials 게재
- 2026-09-02 · 석사과정 박연수 학생 APL Materials 게재
- 2026-05-07 · 강민구 박사님 Tohoku University 조교수 부임
- 2026-04-21 · 박사과정 강민석 학생 INTERMAG 2026 "Best Student Oral Presesntation", "IEEE Neil Smith Award" Finalist award …
- 2026-02-23 · Nano Spintronics Lab 안전 관리 우수상 수상
- 2026-01-24 · 박사과정 김근우 학생 Nano Letters 게재
- 2025-11-09 · 김동준 박사님 Conference on Magnetism and Magnetic Materials(MMM 2025) Best Poster Award 수상
- 2025-09-20 · 박사과정 고대규 학생 Nano Letters 게재
- 2025-09-03 · 김동준 박사님 Advanced Materials 게재
- 2025-03-14 · 박병국 교수님 KAIST 지정석좌교수 선정
- 2024-09-13 · 강민석 박사 과정 학생 카이스트 인성 장학생 선정
- 2024-09-13 · 김동준 박사님 Nature Materials 게재
- 2024-09-03 · 신소영 석사 과정 학생 해외 연수
- 2024-08-30 · 김동준 박사 하반기 BK21 사업 신진연구인력 선정
- 2024-07-08 · 강민석 박사과정 학생 2024 ICM 우수 발표상 수상(2024 International Conference on Magnetism Award for Best Poster)
- 2024-06-03 · 강민석 박사과정 학생 2024 하계 한국자기학회 우수 발표상 수상(2024 KMS Award for Best Poster Presentation)
- 2024-02-13 · 제 30회 삼성휴먼테크논문대상 동상 수상
- 2023-07-10 · 국가반도체연구실 선정이 되었습니다.
- 2023-06-09 · 황인국 박사과정 학생 2023 하계 한국자기학회 최우수 발표상 수상(2023 KMS Award for Best Poster Presentation)
- 2023-06-09 · 강재민 박사과정 학생 2023년도 한국자기학회 우수대학원생상 수상 (Jaimin Kang received the best student awards)
- 2023-04-19 · 국가나노기술정책센터 웹진 NOW 4월호(제55호) 발행
- 2023-03-07 · 강민구 박사 신소재공학과 우수논문상 수상 (Dr. Min-Gu Kang received the Best Paper Award)
- 2023-02-22 · 강재민 박사과정 학생 신소재공학과 대학원생 우수 연구포상 (Jaimin Kang received the MSE Outstanding Research Awards Program i…
- 2023-02-22 · 박병국 교수님 제52주년 개교기념식에서 학술상 수상 (Professor Byong-Guk Park received an academic awards of the year)
- 2023-02-14 · 카이랄 스핀트로닉스 워크숍 진행 (Chiral spintronics workshop)
- 2023-01-09 · YTN 사이언스 브라보 K-사이언티스트 출연 (Appearances on YTN science programs - Bravo K-scientist)
- 2022-12-16 · 2022 ENGE 우수 구두 발표상 수상 (2022 ENGE Award for Best OralPresentation)
- 2022-12-16 · 2022 ENGE 우수 구두 발표상 수상 (2022 ENGE Award for Best OralPresentation)
- 2022-12-16 · 2022 ENGE 우수 포스터상 수상 (2022 ENGE Award for Best Poster Presentation)
- 2022-11-30 · 박병국 카이스트 교수팀, 스핀 소자 기반 물리적 복제방지 보안 기술 개발 (기사)
- 2022-07-27 · 최종국 박사과정 학생 국제 학술지 ‘Nature Communications’ 6월 20일 字 게재
- 2022-06-17 · 류정춘 박사님 국제 학술지 ‘Nature Electronics’ 3월 7일 字 게재
- 2022-06-17 · 최가은 석사 졸업생 국제 학술지 ‘APL Materials’ 1월 13일 字 온라인판에 게재
- 2022-06-15 · 강민구, 최종국 박사과정 학생, 박사 학위 디펜스 진행
- 2022-06-15 · 2022 한국자기학회 하계학술대회 우수 포스터 상장 수상
- 2022-02-21 · 28회 삼성휴먼테크논문대상 은상 수상
- 2021-12-24 · ICAMD 우수 포스터 상장 수상
- 2021-12-21 · 자성메모리 기반 지능형 반도체 소재 기술 개발​
- 2021-11-29 · KAIST, 고속 동작 뉴모로픽 자성 소자 핵심 기술 개발
- 2021-11-22 · 정지민 박사과정 학생 국제 학술지 ‘Advanced Functional Materials’ 11월 7일 字 온라인판에 게재
- 2021-03-25 · Congratulation for conferment of M.S. degree in 2021.02 (Gaeun-choi & Dohyoung-Kim)

## 연락과 위치

- 소속: KAIST 신소재공학과(대전 유성구 대학로 291)[^home]
- 교수 이메일: bgpark@kaist.ac.kr[^prof]

[^home]: 연구실 누리집 첫 화면 <https://nanospin.kaist.ac.kr/> (2026-10-20 열람)
[^overview]: Research Overview 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (2026-10-20 열람)
[^mram]: Research MRAM(SOT-based memory) 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub1_2> (2026-10-20 열람)
[^thermo]: Research Spin thermoelectrics 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub1_3> (2026-10-20 열람)
[^sto]: Research Spin torque oscillator 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub1_4> (2026-10-20 열람)
[^logic]: Research Spin-based logic device 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub1_5> (2026-10-20 열람)
[^prof]: Professor 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub2_1> (2026-10-20 열람)
[^members]: Current 페이지 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub2_2> (2026-10-20 열람)
[^alumni]: Alumni 페이지 1–2쪽 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub2_3> (2026-10-20 열람)
[^papers]: Journals 게시판 1–5쪽 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub3_1> (2026-10-20 열람)
[^patents]: Patents 게시판 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (2026-10-20 열람)
[^news]: News 게시판 1–5쪽 <https://nanospin.kaist.ac.kr/bbs/board.php?bo_table=sub4_1> (2026-10-20 열람)
[^p1]: J. Ryu 외, B.-G. Park, Nature Electronics 5, 217-223 (온라인 2022-04-07). <https://doi.org/10.1038/s41928-022-00735-9> 초록 기준(출판사 논문 페이지).
[^p2]: M.-G. Kang 외, B.-G. Park, Nature Communications 12, 7111 (온라인 2021-12-07). <https://doi.org/10.1038/s41467-021-27459-2> 초록 기준.
[^p3]: S. Ko 외, B.-G. Park, Advanced Materials, e73522 (온라인 2026-05-28). <https://doi.org/10.1002/adma.73522> 초록 기준.
[^p4]: S. Lee 외, B.-G. Park, Advanced Materials 34, 2203558 (온라인 2022-10-17). <https://doi.org/10.1002/adma.202203558> 초록 기준.
[^p5]: D. Koh 외, B.-G. Park, Nano Letters 25, 14784-14792 (온라인 2025-10-01). <https://doi.org/10.1021/acs.nanolett.5c02634> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: D. Han 외, B.-G. Park, Advanced Science 13, e24371 (온라인 2026-07-23). <https://doi.org/10.1002/advs.202524371> 초록 기준.
[^p7]: J.-G. Choi 외, B.-G. Park, Nature Communications 13, 3783 (온라인 2022-06-30). <https://doi.org/10.1038/s41467-022-31493-z> 초록 기준.
[^p8]: J.-M. Kim 외, B.-G. Park, Nature Communications 14, 3365 (온라인 2023-06-08). <https://doi.org/10.1038/s41467-023-39116-x> 초록 기준.

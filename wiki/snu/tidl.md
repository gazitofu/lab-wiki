# 삼차원 집적 및 소자 연구실 (Three-Dimensional Integration and Device Lab., TIDL)

**서울대학교 공과대학 전기·정보공학부 · 최우영 교수**

- 분야: 정보 저장·처리용 반도체 소자, 두뇌 모방 소자와 회로, 강유전체 기반 검색·논리 연산, 삼차원 이종집적
- 대분야: 전기전자·반도체·광학
- 태그: 뉴로모픽 소자[^research][^p1], 메모리 반도체 소자[^dept-lab][^p1], 메모리 내 연산[^p2][^p5], 강유전체[^p5][^p6], 멤리스터[^p4], MEMS 미세 기계 소자[^p7][^p8], 3차원 집적[^p7][^p8], 하드웨어 보안[^p8]
- 홈페이지: <https://sites.google.com/view/snutidl>
- 근거와 출처: [TIDL 근거 페이지](tidl-sources.md)

> 정보를 저장하고 계산하는 반도체 소자를 만들며, 두뇌의 정보 처리를 본뜬 소자·회로와 서로 다른 소자를 위아래로 연결하는 삼차원 집적 기술을 연구한다.[^research][^dept-lab]

## 무엇을 연구하나

서울대학교 최우영 교수가 이끄는 반도체 소자(전기적 기능을 수행하는 기본 구성 요소) 연구실이다. 학과 소개는 소자의 집적도(일정한 면적이나 부피 안에 모은 소자의 정도), 전력 소모와 기능의 한계를 연구 대상으로 든다. 아이디어를 세우는 단계부터 모델링(대상의 특성과 동작을 수식이나 계산 규칙으로 나타내는 일), 시뮬레이션(모형을 이용해 동작을 계산하는 일), 공정(소자를 만드는 처리 단계), 제작·측정·분석과 회로 응용까지 다룬다.[^dept-lab]

랩은 연구를 정보 소자와 삼차원 집적(소자와 회로를 높이 방향으로 배치하고 연결하는 일) 두 축으로 소개한다. 정보 소자에는 뉴로모픽(신경세포와 그 연결의 동작을 본뜬 정보 처리), 논리, 아날로그(값을 연속적으로 나타내는 방식), 센서와 메모리(정보를 저장하는 장치나 기능)가 포함된다. 학과 소개는 메모리와 비메모리 반도체, 두뇌 모방 컴퓨팅, 초저전력 반도체와 삼차원 이종집적(종류가 다른 소자나 회로를 높이 방향으로 결합하는 일)을 응용 대상으로 적는다.[^research][^dept-lab]

최근 논문은 정보를 저장하는 소자에서 계산까지 수행하는 메모리 내 연산을 보여 준다. 신경망(신경세포 사이의 연결에서 착안한 계산 모형)의 연결 강도를 나타내는 가중치를 플래시 메모리(블록 단위로 지우고 다시 쓸 수 있는 비휘발성 반도체 메모리)에 저장하고, 그 소자 배열과 신경세포의 기능을 본뜬 뉴런 회로를 함께 연구한다. 비휘발성은 전원을 꺼도 저장 상태가 남는 성질이다. 플래시를 이용한 학습 소자, 수직 낸드 플래시를 이용한 연상 계산, 배열과 뉴런 회로 사이의 오차를 보상하는 회로가 이 갈래에 속한다.[^p1][^p2][^p3]

다른 갈래에서는 강유전체(외부 전기장이 없어도 전기 분극이 남고 그 방향을 전기장으로 바꿀 수 있는 물질)를 이용해 저장 내용의 차이를 계산하거나 논리 기능을 바꾼다. 전기장은 전하에 전기력이 작용하는 공간의 상태이고, 전하는 전기적 상호작용을 일으키는 물질의 성질이며, 전기 분극은 양·음 전하의 치우침이 전기적 방향성을 만드는 현상이다. 또 나노전기기계 소자(Nanoelectromechanical device, 전기적 작용과 나노미터 규모 구조의 기계적 움직임을 결합한 소자)를 반도체 배선층에 집적해 검색과 보안 기능을 구현한다.[^p5][^p6][^p7][^p8]

## 주요 연구 주제

### 메모리 소자와 신경망 회로

소자가 정보를 얼마나 안정되게 저장하는지뿐 아니라, 저장된 값을 계산에 어떻게 쓰고 학습 중에 어떻게 바꿀지도 연구한다. 표준 CMOS(Complementary Metal–Oxide–Semiconductor, 서로 상보적인 두 종류의 트랜지스터를 결합하는 반도체 회로 기술) 공정과 호환되는 NOR(Not OR, 메모리 셀을 병렬로 연결해 개별 위치를 읽는 방식의 플래시 메모리) 플래시 소자로 가중치 증가·감소를 구현한 논문이 있다. 트랜지스터는 전기 신호로 전류의 흐름을 조절하는 소자이고, 전류는 전하가 이동하는 흐름이며, 신호는 정보를 전달하는 물리량의 변화다.[^p1]

수직 낸드 플래시로는 불완전한 입력에서 저장된 정보를 되찾는 연상 계산을 연구한다. 여러 입력을 한꺼번에 읽을 때 생기는 오차는 뉴런 회로에서 보상하고, 저항 변화 메모리(RRAM, Resistive Random-Access Memory, 전기 저항 상태를 바꾸어 정보를 저장하는 메모리)를 층으로 쌓아 신경망 연산을 수행하는 연구도 한다. 저항은 전류의 흐름을 방해하는 정도다.[^p2][^p3][^p4]

### 강유전체를 이용한 검색과 논리 연산

내용 주소화 메모리(CAM, Content-Addressable Memory, 주소 대신 저장 내용과 입력을 비교해 항목을 찾는 메모리)를 이용해 검색을 소자 안에서 수행한다. 강유전체 멤커패시터(입력 이력에 따라 전하를 저장하는 능력이 달라지는 소자)를 이용한 연구에서는 저장 내용과 검색 입력이 다른 정도를 출력의 지연 시간으로 나타낸다. 실험으로 동작을 보이고, 소자를 만드는 과정의 편차와 배선의 영향에 대한 계산도 함께 수행했다.[^p5]

터널 전계 효과 트랜지스터(TFET, Tunnel Field-Effect Transistor, 전기장으로 양자 터널링 전류를 조절하는 트랜지스터)를 이용해 논리 기능을 바꾸는 연구도 있다. 양자 터널링은 고전적으로 넘을 수 없는 에너지 장벽을 입자가 통과하는 현상이다. 강유전체를 결합한 한 소자에서 입력을 기록하고, 읽는 전압(전하를 이동시키는 두 지점 사이의 전기적 에너지 차이를 전하량으로 나눈 값)을 바꾸어 논리 연산의 종류를 선택하는 방법을 제안했다.[^p6]

### 삼차원 집적 나노전기기계 소자

나노전기기계 메모리 스위치와 커패시터(전하를 저장하는 소자)를 CMOS 배선층에 함께 집적하는 검색 구조를 연구한다. 제안한 삼진 내용 주소화 메모리(TCAM, Ternary Content-Addressable Memory)는 저장 비트(이진 정보의 기본 단위)에 일치·불일치를 판단할 값 외에 비교에서 무시할 상태를 둘 수 있다. 소자 실험과 그 측정 결과에 기초한 배열 계산으로 동작을 검토했다.[^p7]

보안 연구에서는 제작 과정에서 기계 구조가 달라붙는 양상의 무작위성을 이용한다. 물리적 복제 방지 함수(PUF, Physically Unclonable Function, 소자마다 생기는 물리적 차이에서 고유한 응답을 만드는 회로)를 이용해 데이터를 저장한 자리에서 암호화와 복호화를 수행하는 방법을 제안하고, 여러 참여자가 자료를 한곳에 모으지 않고 함께 모형을 학습하는 연합학습 환경에서 그 동작을 보였다.[^p8]

## 대표 논문

최우영 교수가 저자이고 서울대 재직 시기에 출판된 논문 중 세 연구 갈래를 보여 주는 8편을 골랐다. 연도는 랩의 권호 표기이며 온라인 공개일은 각주에 따로 적었다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 랩 게시 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Fully CMOS-Compatible 3-T Embedded NOR Flash Memory Achieving 28 ns Long-Term Potentiation/Long-Term Depression for High-Speed Online Training Accelerators](https://doi.org/10.1002/aisy.202500547)[^p1] | 표준 반도체 공정과 호환되는 플래시 소자를 만들고, 학습 때 연결 강도를 올리고 내리는 동작을 실험했다. |
| 2 | 2026 | [Large-Scale and Highly Reliable Hopfield Neural Networks Using Vertical NAND Flash Memory for the In-Memory Associative Computing](https://doi.org/10.1002/aisy.202500655)[^p2] | 수직 낸드 플래시에 연상 계산을 구현해 잡음으로 훼손된 이미지를 복원하고, 값을 갱신하는 방식과 제작 편차의 영향을 살폈다. |
| 3 | 2025 | [Compensated Current Mirror Neuron Circuits for Linear Charge Integration with Ultralow Static Power in Spiking Neural Networks](https://doi.org/10.1002/aisy.202400673)[^p3] | 여러 메모리 소자를 함께 읽을 때 뉴런 회로와 배열 사이에서 생기는 계산 오차를 보상하는 회로를 제안했다. |
| 4 | 2024 | [Synaptic Characteristics and Vector-Matrix Multiplication Operation in Highly Uniform and Cost-Effective Four-Layer Vertical RRAM Array](https://doi.org/10.1002/adfm.202310193)[^p4] | 저항 변화 메모리를 네 층으로 제작하고, 신경세포 연결의 특성을 본뜨는 동작과 신경망에 필요한 곱셈·덧셈을 확인했다. |
| 5 | 2025 | [Time-Domain Content-Addressable Memory Based on Single Ambipolar Ferroelectric Memcapacitor for High-Density and Highly-Precise Distance Function Computation](https://doi.org/10.1002/aelm.202500421)[^p5] | 저장 정보와 검색 정보가 다른 정도를 출력이 늦어지는 시간으로 표현하는 메모리를 제안하고 실험했다. |
| 6 | 2025 | [One-Ferroelectric-Tunnel-FET-Based Reconfigurable Logic Gates](https://doi.org/10.1109/TED.2025.3561710)[^p6] | 강유전체 터널 트랜지스터 하나에서 읽는 전압을 바꾸어 여러 논리 연산을 선택하는 방법을 제안했다. |
| 7 | 2026 | [Ternary Content-Addressable Memory Using One Capacitor and One Nanoelectromechanical Memory Switch for Data-Intensive Applications](https://doi.org/10.1002/aisy.202500586)[^p7] | 반도체 배선층 위에 기계식 메모리 스위치와 커패시터를 함께 만들어, 비교에서 무시할 상태도 저장하는 검색 메모리를 실험했다. |
| 8 | 2025 | [In Situ XOR Encryption for Lightweight Security Using Nanoelectromechanical Physically Unclonable Functions](https://doi.org/10.1002/aisy.202400805)[^p8] | 기계 소자의 제작 차이로 고유한 응답을 만들고, 저장된 자리에서 암호화·복호화를 수행하는 구조를 제안했다. |

## 교수와 전문 분야

최우영 교수는 서울대학교에서 2000년 학사, 2002년 석사, 2006년 박사 학위를 받았다. UC Berkeley 방문연구자·박사후연구원을 거쳐 2008년 9월부터 2022년 2월까지 서강대학교 전자공학과에서 조교수·부교수·정교수로 일했고, 2022년 3월 서울대학교 전기·정보공학부 정교수로 부임했다.[^dept-prof] 랩 소개는 서울대 반도체공동연구소 교육부장(2022–2024), 연구부장(2024년 이후) 경력을 적는다.[^prof]

학과가 명시한 전문 분야는 MOSFET(Metal–Oxide–Semiconductor Field-Effect Transistor, 절연층을 사이에 둔 전극의 전기장으로 반도체 안의 전류를 조절하는 소자), 차세대 메모리·비메모리 소자, 두뇌 모방 소자와 삼차원 이종집적이다. 연구 방법에는 소자의 설계·제작·측정·분석·모델링과 공정·회로 응용이 포함된다.[^dept-prof] 대표 논문에서도 저장 소자의 물리적 동작을 신경망 계산·검색·논리 연산으로 연결하고, 전자 소자와 기계 소자를 같은 배선 구조에 집적하는 방향을 확인할 수 있다.[^p1][^p5][^p6][^p7]

## 응용 분야

학과 소개는 개발 기술이 DRAM(Dynamic Random-Access Memory, 전하로 정보를 저장하며 내용을 주기적으로 다시 써 유지하는 메모리), 플래시와 차세대 메모리, 비메모리 파운드리(다른 기업이 설계한 반도체를 생산하는 제조 사업), 두뇌 모방 컴퓨팅과 삼차원 이종집적 반도체에 적용된다고 적는다.[^dept-lab] 대표 논문은 학습용 반도체 하드웨어, 불완전한 정보의 복원, 내용 기반 검색과 논리 연산, 사물인터넷 기기의 보안을 대상으로 한다.[^p1][^p2][^p5][^p6][^p8]

## 구성원

2026년 10월 26일 People 페이지 기준으로 교수 최우영을 제외한 26명이다. 박사과정 5명, 석박사통합과정 17명, 석사과정 2명, 산학협력교수 1명과 박사후연구원 1명이며 과정과 직함은 원문 표기를 따른다. 시작은 해당 과정이나 직위의 게시 시작 연월이다.[^graduate][^staff] ‘대표 논문 참여’는 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Choi, Kyung Min | 박사과정 | 2023.03 | kmin.choi@snu.ac.kr |  |
| Chang, Jin Ho | 박사과정 | 2023.03 | markho@snu.ac.kr | 1, 2 |
| Bae, Byeong Jun | 박사과정 | 2024.09 | bdia2349@snu.ac.kr |  |
| Cha, Min Seok | 박사과정 | 2026.03 | mindol946@snu.ac.kr |  |
| Yang, Jae Hyuk | 박사과정 | 2026.03 | yhjyuk0326@snu.ac.kr |  |
| Ryu, Min Jeong | 석박사통합과정 | 2022.03 | rminjeong@snu.ac.kr | 5, 6 |
| Lee, Jin Wook | 석박사통합과정 | 2022.03 | j0gab0nit0@snu.ac.kr | 6, 7, 8 |
| Park, Geun Tae | 석박사통합과정 | 2022.03 |  | 1, 7, 8 |
| Yeom, Jae Min | 석박사통합과정 | 2023.03 |  | 6 |
| Lee, Seon Ho | 석박사통합과정 | 2023.03 |  |  |
| Nam, Jae Hyun | 석박사통합과정 | 2024.03 | kingnam15@snu.ac.kr |  |
| Park, Chang Hyeon | 석박사통합과정 | 2024.03 | pch3684@snu.ac.kr |  |
| Park, Ji Won | 석박사통합과정 | 2024.03 | jiwonpark@snu.ac.kr |  |
| Baek, Seung Hun | 석박사통합과정 | 2024.03 | nonlinear0909@snu.ac.kr | 7, 8 |
| Shin, Myeong Su | 석박사통합과정 | 2025.03 |  | 7, 8 |
| Kim, M in Se | 석박사통합과정 | 2025.03 | minsekim@snu.ac.kr |  |
| Choi, Seong Won | 석박사통합과정 | 2025.03 | sungone3@snu.ac.kr |  |
| Son, Seon Woo | 석박사통합과정 | 2025.09 | sonsw1022@snu.ac.kr |  |
| Kim, Min Seung | 석박사통합과정 | 2026.03 | minseungkim@snu.ac.kr |  |
| Kim, Min Se o | 석박사통합과정 | 2026.03 |  |  |
| Kim, Jae Woo | 석박사통합과정 | 2026.03 |  |  |
| Choi, Yong Ho | 석박사통합과정 | 2026.03 | allyong@snu.ac.kr |  |
| Kim, Seong Jin | 석사과정 | 2025.03 |  |  |
| Kim, Min Ji | 석사과정 | 2025.09 | minji2269@snu.ac.kr |  |
| Kim, Jiyoung | 산학협력교수 (University Industry Collaboration Prof.) | 2025 | hbt100@snu.ac.kr |  |
| Woo, Jae Seung | 박사후연구원 (ISRC) | 2026.03 |  | 1, 2, 5, 6, 8 |

## 졸업생과 이전 구성원

People의 Alumni에 적힌 51개 학위 기록이다. 서울대 박사 1명·석사 7명과 서강대 박사 2명·석사 41명으로 구분된다. 최우영 교수의 서울대 부임 전 서강대 재직 시기 기록도 포함하며, 서울대 부임 후에 학위를 마친 서강대 기록도 원문 소속대로 적었다. 학위와 연도, 진로는 랩 게시 표기이며 한 사람이 여러 학위 기록이나 현재 구성원 표에 함께 나타날 수 있다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| Woo, Jae Seung | 박사 (Seoul National University) (2026.02) | 2026.03 ~ Inter-university Semiconductor Research Center (ISRC), Post-doctor |  |
| Park, Chang Heon | 석사 (Seoul National University) (2025.02) |  | In-Memory Boolean Logic Operations Using Charge-Trapping Tunnel Field-Effect Transistors |
| Han, Seung Hyeon | 석사 (Seoul National University) (2025.02) | 2025.03 ~ Samsung Electronics | Impact of Work-Function Variation on Scaled Ferroelectric Field-Effect Transistors |
| Jeong, Yoon Tae | 석사 (Seoul National University) (2025.02) | 2015.03 ~ Samsung Electronics Co.,Ltd | Lifetime Prediction for Hot-Carrier-Induced Degradation of P-MOSFETs in the Subthreshold Region |
| Uhm, Se Hyun | 석사 (Seoul National University) (2025.08) | 2025.09 ~ SK Hynix |  |
| Kim, Kyung Moon | 석사 (Seoul National University) (2026.02) | 2016.03 ~ Samsung Electronics Co., Ltd |  |
| Yang, Da Eun | 석사 (Seoul National University) (2026.02) |  |  |
| Cha, Min Seok | 석사 (Seoul National University) (2026.02) | 2026.03 ~ Seoul National University (EE), Ph.D student |  |
| Lee, Jang Woo | 박사 (Sogang University) (2021) | 2021 ~ 2022 Sogang University (EE), Post-doctor (BK21 FOUR program); 2022 ~ 2023 Seoul National U. (EE), Post-doctor; 2023 ~ SKKU, Post-doctor | Tunnel Field-Effect Transistors (TFETs) as Silicon-Based Synaptic Devices for Neuromorphic Computing Systems |
| Kwon, Hyug Su | 박사 (Sogang University) (2022) | 2022 ~ 2022 Seoul National U. (EE), Post-doctor; 2023 ~ Agency for Defense Development, Researcher | Monolithic Three-Dimensional CMOS–NEM Reconfigurable Logic Circuits |
| Lee, Woo Jun | 석사 (Sogang University) (2011) | 2011 ~ 2015 SK Hynix; 2015 ~ KARI | Tunneling Field-Effect Transistors for Low-Power Circuit Applications |
| Roh, Seung Hyeun | 석사 (Sogang University) (2012) | 2012 ~ SK Hynix | Scaling Trend of Nanoelectromechanical (NEM) Nonvolatile Memory Cells Based on Finite Element Analysis (FEA) |
| Jang, Jung Shik | 석사 (Sogang University) (2012) | 2012 ~ SK Hynix | Hetero-Gate-Dielectric Tunneling Field-Effect Transistors (HG TFETs) for Low-Power Circuit Applications |
| Lee, Min Jin | 석사 (Sogang University) (2012) | 2012 ~ SK Hynix | Analytical Model of Single-Gate Silicon-on-Insulator (SOI) Tunneling Field-Effect Transistors (TFETs) |
| Lee, Kwang Seok | 석사 (Sogang University) (2012) | 2012 ~ Samsung Electronics | Nano-Electromechanical (NEM) Nonvolatile Memory Cells (T cells) for Multi-Bit operation |
| Lee, Gi Bong | 석사 (Sogang University) (2013) | 2013 ~ Samsung Electronics | A Study on Hetero-Gate-Dielectric Tunneling Field-Effect Transistors |
| Han, Bo Ram | 석사 (Sogang University) (2013) | 2013 ~ SK Hynix | Fringe Field Effects on Nano-Electromechanical (NEM) Memory Cells |
| Lee, Hyun Kook | 석사 (Sogang University) (2014) | 2014 ~ Samsung Electronics | Hetero-Gate-Dielectric Tunneling Field-Effect Tran-sistors (HG TFETs) for Highly Energy Efficient ICs |
| Kim, Kwan Yong | 석사 (Sogang University) (2014) | 2014 ~ Samsung Electronics | Lateral Nano-Electromechanical (NEM) Relays for Reconfigurable Logic |
| Kang, Jun Geun | 석사 (Sogang University) (2014) | 2014 ~ SK Hynix | Influence of Random Dopant Fluctuation (RDF) on NAND Flash Memory Cells |
| Han, Jae Hwan | 석사 (Sogang University) (2014) | 2014 ~ SK Hynix | Bit-to-Bit Interference of Multi-Bit Nano-Electro-mechanical Memory Cells (T cells) |
| Choi, Kyung Min | 석사 (Sogang University) (2015) | 2015 ~ Samsung Electronics | Work-Function Variation Effects of Tunneling Field-Effect Transistors (TFETs) |
| Kim, Yong Jun | 석사 (Sogang University) (2015) | 2015 ~ SK Hynix | Nonvolatile Nano-Electromechanical (NEM) Memory Switches for Reconfigurable Logic |
| Park, Jong Han | 석사 (Sogang University) (2016) | 2016 ~ 2017 National NanoFab Center; 2017 ~ 2018 DB Hitek; 2018 ~ ON Semiconductor | Rounded-Corner Tunnel Field-Effect Transistors (RC TFETs) for Performance Enhancement |
| Cheon, Woo Young | 석사 (Sogang University) (2016) | 2016 ~ Samsung Electronics | Subthreshold-Slope-Adjustable Tunnel Field-Effect Transistor- Based Random Access Memories (STRAMs) for Low-Power Storage Devices |
| Kim, Da Som | 석사 (Sogang University) (2016) | 2016 ~ Hanwha Corporation/Defense | Influence of Electron and Hole Distribution on 2T SONOS Embedded NVMon 2T SONOS Embedded NVM |
| Kim, Seung Kyu | 석사 (Sogang University) (2016) | 2016 ~ Samsung Electronics | Three-Dimensional Reconfigurable Logic (RL) Circuits Based on Extremely Low-Power Electron Devices |
| Choi, Song Hun | 석사 (Sogang University) (2016) |  | Process Variation Effects of Tunnel Field Effect Transistors (TFETs) |
| Lim, In Eui | 석사 (Sogang University) (2016) | 2016 ~ STATS ChipPAC Korea | Drain Current Modeling of Sub-70-nm PMOSFETs Dependent on Hot-Carrier Stress Bias Conditions |
| C ha, Tae Min | 석사 (Sogang University) (2017) | 2017 ~ SK Hynix | Process Development for CMOS-Nano-Electro-mechanical System (NEMS) Co-integration |
| Huh, In | 석사 (Sogang University) (2017) | 2017 ~ Samsung Electronics | Mathematical Model of Transition-Metal-Dichalco-genide-Based (TMD-Based) Tunnel Field-Effect Transistors (TFETs) |
| Lee, Ho Moon | 석사 (Sogang University) (2018) | 2018 ~ ASML | Switching Voltage Analysis of Nano-Electromecha-nical (NEM) Memory Switches for CMOS-NEM Hybrid Reconfigurable Logic Applications |
| Jo, Hyun Chan | 석사 (Sogang University) (2019) | 2019 ~ DB Hitek | Encapsulation of NEM Memory Switches for Mono-lithic-Three-Dimensional (M3D) CMOS-NEM Hybrid Circuits |
| Shin, Seong Un | 석사 (Sogang University) (2019) | 2019 ~ SK Hynix | Degradation Modeling of DRAM Storage Capacitors |
| Ko, Ji Wang | 석사 (Sogang University) (2020) | 2020 ~ Samsung Electronics | Scaling of Monolithic 3D CMOS-Nanoelectro-mechanical Reconfigurable Logic Circuits |
| Kang, Min Hee | 석사 (Sogang University) (2020) | 2020 ~ Samsung Electronics | Low-Operation-Voltage Nanoelectromechanical (NEM) Memory Switches using Dynamic Slingshot Operation |
| Kang, Min Woo | 석사 (Sogang University) (2021) | 2021 ~ ASML | Investigation on the Hump Behavior of Gate-Normal Nanowire Tunnel Field-Effect Transistors (NWTFETs) |
| Kwon, Hyeok Jin | 석사 (Sogang University) (2021) |  | Offset Contribution Analysis for DRAM Offset Can-cellation Sensing Scheme |
| Kim, Hye In | 석사 (Sogang University) (2021) | 2021 ~ Samsung Electronics | LTPS (Low-Temperature Polycrystalline Silicon) TFT with an amorphous silicon buffer layer and source/ drain extension |
| Baek, Gwang Ryeol | 석사 (Sogang University) (2021) | 2021 ~ Samsung Electronics | Tri-State Nanoelectromechanical (NEM) Memory Switches for an Efficient Routing in Reconfigurable Logic |
| Lee, Jae Seong | 석사 (Sogang University) (2022) | 2022 ~ Samsung Electronics | Design of Ternary Content-Addressable Memory Using Nanoelectromechanical (NEM) Memory Switches |
| Yoon, Ji Soo | 석사 (Sogang University) (2022) | 2022 ~ Samsung Electronics | Multi-Layer Nanoelectromechanical (NEM) Memory Switches for Efficient Routing Operation |
| Koo, Kyung Min | 석사 (Sogang University) (2022) | 2022 ~ Samsung Electronics | Analysis of the Gate-Diagonal Tunneling Suppression Effect Using Oxide-Trapped Charge |
| Woo, Jae Seung | 석사 (Sogang University) (2022) | 2022 ~ Seoul National U. (EE), PhD student | Investigation of Hot Carrier Injection in Tunnel Field-Effect Transistors |
| Jung, Chae Lin | 석사 (Sogang University) (2023) | 2023 ~ Samsung Electronics | Nonvolatile memory based on a tunneling field-effect transistor (TFET) using HfO2 trapping layer |
| Uhm, Ji Ho | 석사 (Sogang University) (2023) | 2023 ~ Samsung Electronics | Influence of Azimuthal Charge Redistribution on Data Retention of Hemi-Cylindrical Vertical NAND Flash Memory |
| Chang, Jin Ho | 석사 (Sogang University) (2023) | 2023 ~ Seoul National U. (EE), PhD student | Electrical Characteristics of Hemi-Cylindrical Vertical NAND Flash Memory according to Channel Hole Remaining Ratio |
| Lee, Si Youn | 석사 (Sogang University) (2023) | 2023 ~ Samsung Electronics | Snapback Breakdown Voltage Dependence on Source/Drain Configuration in Multi-Finger MOSFETs |
| Nam, Ki Ryung | 석사 (Sogang University) (2023) | 2023 ~ Samsung Electronics | Analysis of Electrical Characteristics of PNPN Tunnel Field-Effect Transistors by Pocket Design |
| Kwak, Kyung Wook | 석사 (Sogang University) (2024) | 2024 ~ Samsung Electronics | Reliability of the Multi-Finger Gate High-Voltage MOSFETs for the NAND Flash Memory |
| Ahn, Seung Hyun | 석사 (Sogang University) (2024) | 2024 ~ Samsung Electronics | Side-Gate MOSFETs for the Suppression of Off-State Breakdown |

## 최근 논문 목록 (2021–2026)

랩 Publication의 2021–2026년 게시 서지 255항목이다. Journal의 학술지 논문 90편과 arXiv 사전 공개본 1편, Conference의 국제 학회 86항목과 국내 학회 78항목을 함께 적었다. 최우영 교수의 2022년 3월 서울대 부임 전 서강대 재직 시기 항목도 포함한다. 연도는 게시 서지의 연도이며, 2021년 항목은 해당 연도 전체를 담았다. arXiv 항목은 사전 공개본으로 표시한다.[^journal][^conference]

**2026**

- Jae Seung Woo, Jin Ho Chang, Geun Tae Park, Min Jeong Ryu, Jin Wook Lee, Seon Ho Lee, Jae Min Yeom, Min Se Kim and Woo Young Choi. "Comparative Scaling Analysis of Charge-Trap TFET and MOSFET Synapses for IR-Drop-Aware Analog Vector-Matrix-Multiplication". *IEEE Transactions on Electron Devices, vol. 73 no. 10, pp. 6077-6083, Oct. 2026*.
- Changhyeon Park, Jaemin Yeom, Jiwon Park, Minjeong Ryu, Minse Kim, and Woo Young Choi. "Buried-Gate Ferroelectric Memcapacitors for Scalable Capacitive Compute-in-Memory". *IEEE Transactions on Electron Devices, vol. 73 no. 10, pp. 6303-6310, Oct. 2026*.
- Junsu Yu, Hwiho Hwang, Hyungjin Kim and Woo Young Choi. "Capacitive In-Memory Vector–Matrix Multiplication Computing With Charge-Trap Memcapacitors". *Nano Convergence, vol. 13, p. 42, Sep. 2026*.
- Yoon Tae Jeong, Jae Seung Woo, Jin Ho Chang, Hye Sun Sung, Hyo Jung Kim, Seung Bo Shim, and Woo Young Choi\*. "Hot-Carrier Lifetime Prediction of P-Channel MOSFETs in the Subthreshold Region". *Journal of Semiconductor Technology and Science, vol. 26, no. 4, pp. 283-291, Aug. 2026*.
- Se Hyun Uhm, Jin Ho Chang, Da Eun Yang, Ki Bong Moon, Jae Duk Lee, and Woo Young Choi. "Novel Side-Gate Vertical NAND Structure for Lateral Migration and Interference Suppression". *IEEE Access, vol. 14 pp. 102316-102323, J un. 2026*.
- Kyung Moon Kim, Jin Ho Chang, Jae Hyun Nam, Da Eun Yang, Jun Hyoung Kim, Suk-Kang Sung, Jaeduk Lee, and Woo Young Choi. "Vertical-NAND Flash Memory With an Intercell Charge Trap Layer for the Improvement of Erase Efficiency and Data Retention". *IEEE Transactions on Electron Devices, vol. 7 no. 5, pp.2763-2771, May 2026*.
- Da Eun Yang, Jin Ho Chang, Jin Wook Lee, Se Hyun Uhm, Kyung Moon Kim, Jae Hyun Nam, Ki Bong Moon, Jaeduk Lee, and Woo Young Choi. "Novel Charge-Ring Vertical NAND Flash Memory for Data Retention Improvement". *IEEE Transactions on Electron Devices, vol. 7 no. 5, pp.2772-2778, May 2026*.
- Min-Ju Lee, Seong-Ho Kim, Ga-Hyun Shin, Jae-Sung Park, Woo Young Choi, and Il Hwan Cho. "Investigation of Ternary Operation 1T DRAM with Double Quantum Well Structure". *Journal of Semiconductor Technology and Science, vol. 26, no. 2, pp. 150-158, Apr. 2026*.
- Jin Ho Chang, Jae Seung Woo, Suk-Kang Sung, Ki-Whan Song, and Woo Young Choi\*. "Large-Scale and Highly Reliable Hopﬁeld Neural Networks Using Vertical NAND Flash Memory for the In-Memory Associative Computing". *Advanced Intelligent Systems, vol.8 no.4, pp. e202500655, Apr. 2026*.
- Jin Wook Lee, Changha Kim, Geun Tae Park, Seung Hun Baek, Myeong Su Shin, and Woo Young Choi. "Ternary Content-Addressable Memory Using One Capacitor and One Nanoelectromechanical Memory Switch for Data-Intensive Applications". *Advanced Intelligent Systems, vol. 8 no. 3, pp. e2500586, Mar. 2026*.
- Jae Hyun Nam, Jin Ho Chang, Kyung Moon Kim, Jin Wook Lee, Da Eun Yang, Suk-Kang Sung, Jun Hyoung Kim, and Woo Young Choi. "Investigation of Hot Carrier Injection During GIDL Erase Operation in 3-D NAND Flash Memory". *IEEE Transactions on Electron Devices, vol. 74 no. 3, pp. 1326-1332, Mar. 2026*.
- Sojoong Kim, Yeonwoo Kim, Woo Young Choi\*, Minsuk Koo\*, and Yoon Kim\*. "A Fully Integrated Analog Processing-in-Memory System Based on Charge-Trap Flash Synapse Arrays and Successive Integration-and-Rescaling Neurons". *Advanced Intelligent Systems,vol. 8 no. 2, pp. e 202501046, Feb. 2026*.
- Jae Seung Woo, Kyoung Min Choi, Geun Tae Park, Jin Ho Chang,and Woo Young Choi\*. "Fully CMOS-Compatible 3-T Embedded NOR Flash Memory Achieving 28 ns Long-Term Potentiation/Long-Term Depression for High-Speed Online Training Accelerators". *Advanced Intelligent Systems,vol. 8 no. 2, pp. 2500547, Feb. 2026*.
- Jiwon Park, Jaemin Yeom, Jin Wook Lee, Minjeong Ryu, Changhyeon Park, and Woo Young Choi. "Impact of Random Phase Distribution on Ferroelectric Tunnel Field-Effect Transistors with Mitigation Strategies for Compute-In-Memory Applications". *IEEE Access, vol. 14 pp. 8610-8617, Jan. 2026*.
- Jaemin Yeom, Jae Seung Woo, Jin Wook Lee, Changhyeon Park, Jiwon Park, Minjeong Ryu, and Woo Young Choi. "Implementation of Ternary Neural Networks Based on Ferroelectric Capacitors". *IEEE Electron Device Letters, vol. 47 no. 1, pp. 73-76, Jan. 2026*.
- [Invited] Woo Young Choi. "From Device Physics to Circuit Co-Design: Multi-Physics Modeling of Monolithic 3D CMOS–NEM Hybrid Circuits". *International Conference on Simulation of Semiconductor Processes and Devices (SISPAD), Kumamoto, Japan, pp. 39-42, Sep. 28-30, 2026*.
- Hyang Kim, Donghyun Ryu, Hyoseob Kim, Woo Young Choi, Min-Hwi Kim. "Demonstration of WL-Wise Programming Scheme for AND-Type Synaptic Flash Array". *International Conference on Solid State Devices and Materials (SSDM), Nagasaki, Japan, pp. 568-569, Sep. 14-17, 2026*.
- Jae Hyun Nam, Jin Ho Chang, Jun Hyoung Kim, Suk-Kang Sung, and Woo Young Choi. "Hot Carrier Injection Dependence on Select Gate Patterns during GIDL Erase Operation in 3D NAND Flash Memory". *International Conference on Solid State Devices and Materials (SSDM), Nagasaki, Japan, pp. 669-670, Sep. 14-17, 2026*.
- Minjeong Ryu, Jae Seung Woo, and Woo Young Choi. "Locality-Sensitive Hashing Engine Based on Ambipolar Ferroelectric Tunnel FETs for Efficient Processor-Associative Memory Interfaces in Edge MANNs". *International Conference on Solid State Devices and Materials (SSDM), Nagasaki, Japan, pp. 566-567, Sep. 14-17, 2026*.
- Geun Tae Park, Jin Wook Lee, Jae Seung Woo, and Woo Young Choi. "Scaling Analysis of Nanoelectromechanical Memory Switches for Binary Neural Networks". *International Conference on Solid State Devices and Materials (SSDM), Nagasaki, Japan, pp. 544-545, Sep. 14-17, 2026*.
- Hojin Shin , Woo Young Choi and IL Hwan Cho. "Investigation of High Temperature Field Effect Transistor Based Static Random Access Memory for Harsh Environment". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Busan, Korea, Jul. 12-14, 2026*.
- Jiwon Park, Jaemin Yeom, Jin Wook Lee, Minjeong Ryu, Changhyeon Park, and Woo Young Choi\*. "Random Phase Distribution Effects and Mitigation in Ferroelectric Tunnel FETs for Compute-in-Memory Applications". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Busan, Korea, Jul. 12-14, 2026*.
- Jae Hyun Nam, Jin Ho Chang, Jun Hyoung Kim, Suk-Kang Sung, and Woo Young Choi\*. "Transient Behavior of Hot Carrier Injection During GIDL Erase in Vertical NAND Flash Memory". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Busan, Korea, Jul. 12-14, 2026*.
- Seung Hun Baek, Jin Wook Lee, Geun Tae Park, Myeong Su Shin, and Woo Young Choi\*. "Variation-Robust Ternary Content-Addressable Memory Based on One Capacitor and One Nanoelectromechanical Memory Switch". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Busan, Korea, Jul. 12-14, 2026*.
- Changhyeon Park, Jaemin Yeom, Jiwon Park, Minjeong Ryu, Minse Kim, and Woo Young Choi\*. "Bureid-Gate Ferroelectric memcapacitors for Scalable Capacitive Compute-in-Memory". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Busan, Korea, Jul. 12-14, 2026*.
- Seong Jin Kim, Jin Wook Lee, Myeong Su Shin, Woo Young Choi\*. "A Monolithic 3-D Integrated Reconfigurable CMOS-NEM Threshold Logic Gate with Intrinsic Sign-Encoding for Energy-Efficient Computing". *2026 IEEE Silicon Nanoelectronic Workshop (SNW), H onolulu, Hawaii, U.S.A, pp. 65-66, Jun. 13-14, 2026*.
- Eun Ji Cho, Woo Young Choi, and Il Hwan Cho. "Characteristics of High-Temperature FET Based Static Random Access Memory". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 828, Jan. 27-30, 2026*.
- Kyu Jin Jung, Woo Young Choi, and Il Hwan Cho. "Analysis on Single-Event Transients in High-Temperature-FETs". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 827, Jan. 27-30, 2026*.
- Hwan Hee Lee, Woo Young Choi, and Il Hwan Cho. "Radiation-Induced Transient Characteristics of Feedback FETs". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 830, Jan. 27-30, 2026*.
- Seon Woo Son, Seon Ho Lee, and Woo Young Choi\*. "Influence of Channel Profiles on Device Variation of 3D Channel-Stacked NAND Flash Memory". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1795, Jan. 27-30, 2026*.
- Seongwon Choi, Byeongjun Bae, Jung-Kyun Kim, Younjin Jang, Kyooho Jung, Jee-Eun Yang, Na-Rae Han, Sangwook Kim, and Woo Young Choi\*. "A Design Guideline for 3D Cylindrical MFMIS IGZO FeFETs". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1845, Jan. 27-30, 2026*.
- Seongjin Kim, Jonghyuk Park, Yeonwoo Kim, and Woo Young Choi\*. "Low-Power Analog CMOS Neuron Circuits for Solving Fan-in Issues in Spiking Neural Network Systems". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1072, Jan. 27-30, 2026*.
- Seon Ho Lee, Seon Woo Son, and Woo Young Choi\*. "Effects of Word-line Profiles on Electrical Variationof 3D Channel-Stacked NAND Flash Memory". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1793, Jan. 27-30, 2026*.
- Seung Hun Baek, Jin Wook Lee, Geun Tae Park, and Woo Young Choi\*. "Nanoelectromechanical Physically Unclonable Function for Resource-Constrained IoT Environments". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1071, Jan. 27-30, 2026*.
- Myeong Su Shin, Geun Tae Park, Jin Wook Lee, and Woo Young Choi\*. "Energy-Efficient Ternary Content-Addressable Memory Based on One Capacitor and One Nanoelectromechanical Memory Switch Memory Cell". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1070, Jan. 27-30, 2026*.
- Min Se Kim, Jae Seung Woo, and Woo Young Choi\*. "High-Speed and Highly Reliable 3-T Embedded NOR Flash Memory for Standard CMOS Process". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1067, Jan. 27-30, 2026*.
- Min Seok Cha and Woo Young Choi\*. "Modeling and Process Design Guideline of Oxide Chemical Mechanical Planarization in CMOS Back-End-of-Line Process". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 917, Jan. 27-30, 2026*.
- Minjeong Ryu, Jae Seung Woo, and Woo Young Choi\*. "Capacitive Time-Domain Ferroelectric Content-Addressable Memory for High-Density and Highly Robust In-Memory Nearest Neighbor Search". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 486, Jan. 27-30, 2026*.
- Min Ji Kim, Ji Young Kim, Young Woo Son, Byung Hyun Lee, and Woo Young Choi\*. "Effect of a Single-Void in Word-line Metal on DRAM Cell Characteristics". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1836, Jan. 27-30, 2026*.
- Jiwon Park and Woo Young Choi\*. "A Hafnia-Based Ferroelectric Tunnel-FET with a Stepped Gate Stack for Reliable Ternary Content Addressable Memory Implementation". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1258, Jan. 27-30, 2026*.
- Jaemin Yeom, Minjeong Ryu, Jae Seung Woo, Jinwook Lee, and Woo Young Choi\*. "Reconfigurable Logic Gates Using a Single Ferroelectric-Tunnel-FET". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1776, Jan. 27-30, 2026*.
- Jae Hyun Nam, Jin Ho Chang, Kyung Moon Kim, Da Eun Yang, Ji Sun Baek, Suk-Kang Sung, and Woo Young Choi\*. "Characteristics of GIDL Erase-induced Hot Carrier Injection in Vertical NAND Flash Memory". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 932, Jan. 27-30, 2026*.
- Jin Ho Chang, Jae Seung Woo, Suk-Kang Sung, Ki-Whan Song, and Woo Young Choi\*. "Hopfield Neural Networks Using Vertical NAND Flash Memory for Large-Scale In-Memory Associative Computing". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 148, Jan. 27-30, 2026*.
- Changhyeon Park and Woo Young Choi\*. "A Hardware-Level Framework for Training and Inference of Capacitive Computing-in-Memory Architecture". *The 33rd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1188, Jan. 27-30, 2026*.

**2025**

- Dong-Oh Kim, Changha Kim, Bosung Jeon, and Woo Young Choi. "A Scalable Cylindrical Ferroelectric Tunnel Junction Architecture Enabling a New Class Memory for AI Applications". *IEEE Transactions on Electron Devices, vol. 72 no. 12, pp. 6722-6728, Dec. 2025*.
- Minjeong Ryu, Jae Seung Woo, Yeonwoo Kim, and Woo Young Choi. "Single-Ferroelectric Memcapacitor-Based Time-Domain Content-Addressable Memory for Highly Precise Distance Function Computation". *arXiv preprint, arXiv:2503.00447, Mar. 2025*.
- Minjeong Ryu, Jae Seung Woo, Yeonwoo Kim, Joo Hyeon Jeon, Sung In Cho, and Woo Young Choi. "Time-Domain Content-Addressable Memory Based on Single Ambipolar Ferroelectric Memcapacitor for High-Density and Highly-Precise Distance Function Computation". *Advanced Electronic Materials, vol. 11 no. 20, pp. e00421, Dec. 2025*.
- Donghyun Ryu, Suyong Park, Seongmin Kim, Hyeon Ho Lee, Sungjun Kim, Woo Young Choi. "Physical reservoir computing system fully implemented using a single flash memory device via tailored decay pulse modulation". *Nano Energy, vol. 146 no. 15, pp. 111525 , Dec. 2025*.
- Donghyun Ryu, Suyong Park, Gimun Kim, Hyeon Ho Lee, Sungjoon Kim, Sungjun Kim\*, and Woo Young Choi\*. "Crystallization-Induced Interface Control in Poly-Si Flash for High Accuracy Neuromorphic Inference". *ACS Applied Electronics Materials, vol. 7 no. 21, pp. 9830-9837, Oct. 2025*.
- Hyoseob Kim, Kyungho Hong, Sungjoon Kim, Woo Young Choi\*, and Min-Hwi Kim\*. "Implementation of Ultra-Low-Power Neural Networks on Quantized and Pruned RRAM Crossbar Arrays". *Materials Horizons, vol. 12 no. 19, pp. 8059 - 8071, Oct. 2025*.
- Suyong Park, Donghyun Ryu, Sungjoon Kim, Woo Young Choi\*, and Sungjun Kim\*. "Fully CMOS Compatible Charge Trap Memory-Based Reservoir Computing System". *Advanced Materials Technologies, vol. 10 no. 19, pp. e00858, Oct. 2025*.
- Kyung Min Koo , Jae Seung Woo , and Woo Young Choi. "Oxide-Trapped-Charge-Induced Gate-Diagonal Tunneling Suppression of Gate-Normal Tunnel Field-Effect Transistors". *IEEE Transactions on Nanotechnology, vol 24, pp.445-451, Sep. 2025*.
- Kyoung Min Choi, Jae Seung Woo, and Woo Young Choi. "Inner Gate Length Modulation of MFMIS Nanosheet FET Memory for Advanced Technology Nodes". *IEEE Access, vol.13 pp. 150517-150522, Aug. 2025*.
- Changha Kim, Jin Wook Lee, Geun Tae Park, Myeong Su Shin, Seung Hun Baek, Jae Seung Woo, and Woo Young Choi. "In Situ XOR Encryption for Lightweight Security Using Nanoelectromechanical Physically Unclonable Functions". *Advanced Intelligent Systems, vol. 7 no. 7, pp. 2400805, Jul. 2025*.
- Kyoung Min Choi and Woo Young Choi. "Analysis and Optimization of Nanosheet FETs With Vertically Nonuniform Source/Drain Etch Profiles". *IEEE Transactions on Electron Devices, vol. 72 no. 6, pp. 2861 - 2867, Jun. 2025*.
- Jaemin Yeom, Minjeong Ryu, Jae Seung Woo, Jin Wook Lee, Seonggeun Kim, Seungwon Go, Sangwan Kim, and Woo Young Choi. "One-Ferroelectric-Tunnel-FET-Based Reconfigurable Logic Gates". *IEEE Transactions on Electron Devices, vol. 72 no. 6, pp. 3302 - 3306, Jun. 2025*.
- Jiseong Im, Jonghyun Ko, Joon Hwang, Jangsaeng Kim, Wonjun Shin, Ryun-Han Koo, Minkyu Park, Sung-Ho Park, Woo Young Choi, Jae-Joon Kim, and Jong-Ho Lee\*. "Multifunctional In-Memory Analog-to-Digital Converterfor Next-Gen Compute-in-Memory Systems". *Advanced Intelligent Systems,vol. 7 no. 5, pp. 2400594, May 2025*.
- Yeonwoo Kim, Bosung Jeon, Jonghyuk Park, Woo Young Choi. "Frame-Unit Operating Neuron Circuits for Hardware Recurrent Spiking Neural Networks". *IEEE Transacions on Electron Devices, vol. 72. no. 4, pp. 1795 - 1801, Apr. 2025*.
- Jae Seung Woo, Chae Lin Jung, Jin Ho Chang, Minjeong Ryu, and Woo Young Choi\*. "Dual-Layer-Per-Array Operation Using Local Polarization Switching of Ferroelectric Tunnel FETs for Massive NeuralNetworks". *Advanced Electronic Materials, vol. 11, no. 4, pp. 2400606, Apr. 2025*.
- Yeonwoo Kim, Bosung Jeon, Jonghyuk Park, and Woo Young Choi. "Time-Frame Integrate-and-Fire Neuron Circuit for Low Energy Inference Hardware Spiking Neural Networks". *IEEE Access, vol. 13, pp. 43728-43740, Mar. 2025*.
- Hwiho Hwang, Junsu Yu, Sangwook Youn, Woo Young Choi,\* and Hyungjin Kim\*. "2C-Ternary Content Addressable Memory in MemcapacitorCrossbar Array with NAND Flash Structure". *Small, vol. 21 no. 9, pp. 2408618, Mar. 2025*.
- Jonghyuk Park, Sungjoon Kim, and Woo Young Choi\*. "Compensated Current Mirror Neuron Circuits for LinearCharge Integration with Ultralow Static Power in SpikingNeural Networks". *Advanced Intelligent Systems, vol. 7, no.2 pp. 2400673, Feb. 2025*.
- Sungjoon Kim, Hyeonseung Ji, Sungjun Kim,\* and Woo Young Choi\*. "Enhanced Reliability and Self-Compliance of Synaptic Arraysfor Multibit Encoded Neuromorphic Systems". *Advanced Electronic Materials, vol. 11, no. 2, pp. 2400282, Feb. 2025*.
- Jonghyuk Park, and Woo Young Choi. "Ultra-Low Static Power Circuits Addressing the Fan-Out Problem of Analog Neuron Circuits in Spiking Neural Networks". *IEEE Access, vol. 12, pp. 5248-5256, Jan. 2025*.
- Kyung Moon Kim, Jin Ho Chang, and Woo Young Choi\*. "Intercell Charge Trap Layer Enabling a Wide Memory Window and High Reliability in Vertical NAND Flash". *International Microprocesses and Nanotechnology Conference (MNC), Tokyo, Japan, Nov. 17-20, 2025*.
- Kyoung Min Choi, Jae Seung Woo, and Woo Young Choi\*. "Electro-Thermal Characteristics of Nanosheet FETs with Vertically Nonuniform Source/Drain Etch Profiles". *International Microprocesses and Nanotechnology Conference (MNC), Tokyo, Japan, Nov. 17-20, 2025*.
- Jae Seung Woo and Woo Young Choi\*. "Comparative Scaling Analysis of Charge-Trap TFET (CT-TFETs) and Charge-Trap MOSFETs (CT-MOSFETs) for Reliable Neuromorphic Synapse Arrays". *International Conference on Solid State Devices and Materials (SSDM), Yokohama, Japan, Sep. 15-18, 2025*.
- Jin Ho Chang, Jae Seung Woo, Jae Hyun Nam, Da Eun Yang, Kyungmoon Kim, and Woo Young Choi\*. "Quantized Neuron-Implementable Ternary-State Vertical NAND Flash Memory for the Highly Reliable Neuromorphic computing". *International Conference on Solid State Devices and Materials (SSDM), Yokohama, Japan, Sep. 15-18, 2025*.
- Geun Tae Park and Woo Young Choi\*. "Binary Neural Network Accelerators Using Nanoelectromechanical Memory Switches". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Nara, Japan, Jul. 3-4, 2025*.
- Jin Wook Lee and Woo Young Choi\*. "Torsion-Assisted Via-Anchor Nanoelectromechanical Memory Switches for Reliable Operation". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Nara, Japan, Jul. 3-4, 2025*.
- Jaemin Yeom, Minjeong Ryu, Jae Seung Woo, Jin Wook Lee, and Woo Young Choi\*. "Logic-in-Memory Using a Single Ferroelectric-Tunnel-FET". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Nara, Japan, Jul. 3-4, 2025*.
- Changwoo Park, Jin Wook Lee, Myeongsu Shin, Seungju Lee, Geun Tae Park, Sungsik Hong, Woo Young Choi, and Jinwook Burm. "An In-Memory Computing Architecture Utilizing A 1Capacitor-1Nanoelectromechanical Switch Devicel". *2025 IEEE International Symposium on Circuits and Systems (ISCAS), London, United Kingdom, May 25-28, 2025*.
- Changhyeon Park, Jaemin Yeom, Jiwon Park and Woo Young Choi. "Buried-Channel-Array-Ferroelectric-Transistors (BCAFTs) for 1-Transistor-DRAM 1T-DRAM) Applications". *Summer Annual Conference of ISE, Yeosu, Korea, Jul. 14-16, 2025*.
- Seon Ho Lee, Hyung Jun Noh, Chang Heon Park, Minseok Cha and Woo Young Choi\*. "Effect of Source Underlap on Hot Electron Injection of Charge-Trapping Tunnel Field Effect Transistors". *The 32 nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 173, Feb. 12-14, 2025*.
- Jaemin Yeom, Jun-bum Lee, and Woo Young Choi\*. "Impact of the Starting Layer on Electrical Properties of Superlattice HZO". *The 32 nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 262, Feb. 12-14, 2025*.
- Minjeong Ryu, Jae Seung Woo, Yeonwoo Kim, and Woo Young Choi\*. "Application-Dependent Bias Scheme Optimization for Ferroelectric-Tunnel-FET-Based One-Transistor Ternary Content-Addressable-Memory". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 400, Feb. 12-14, 2025*.
- Jin Wook Lee, Geun Tae Park, and Woo Young Choi\*. "Torsion-Assisted Via-Anchor Nanoelectromechanical Memory Switches". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1075, Feb. 12-14, 2025*.
- Seung Hun Baek, Geun Tae Park, Myeong Su Shin, and Woo Young Choi. "Observation of Electrode-Gap Narrowing in Nanoelectromechanical(NEM) Memory Switches". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1084, Feb. 12-14, 2025*.
- Jonghyuk Park and Woo Young Choi. "Low-Power Analog CMOS Neuron Circuits for Implementing High-Accuracy Spiking Neural Networks Systems". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1278, Feb. 12-14, 2025*.
- Jae Hyun Nam, Kyung Moon Kim, Jin Ho Chang, Se Hyun Uhm, Da Eun Yang, Suk-Kang Sung, and Woo Young Choi\*. "Effect of Space Length on Hot Carrier Injection during GIDL Erase in Vertical NAND Flash Memory". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1587, Feb. 12-14, 2025*.
- Da Eun Yang, Se Hyun Uhm, Jin Ho Chang, Kyung Moon Kim, Jae Hyun Nam, Jae Duk Lee, Ki Bong Moon, and Woo Young Choi\*. "Effect of Nitride Trap Levels on Hole Lateral Migration and Retention in Vertical NAND Flash Memory". *The 32 nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1387, Feb. 12-14, 2025*.
- Jin Ho Chang, Kyung Moon Kim, Jae Hyun Nam, Da Eun Yang, Se Hyun Uhm, Suk-Kang Sung, and Woo Young Choi\*. "Influence of Channel Hole Profiles on Device Variation of Vertical NAND Flash Memory". *The 32 nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 1401, Feb. 12-14, 2025*.
- Min Seok Cha, Hyung Jun Noh, Chang Heon Park, Seon Ho Lee and Woo Young Choi\*. "Impact of Gate Underlap on Memory Window of Charge Trap TFETs". *The 32th Korean Conference on Semiconductors, Jeongseon, Korea, p. 1367, Feb. 12-14, 2025*.
- Yeonwoo Kim, and Woo Young Choi. "Processing Negative-Valued Spikes in AND-type Synaptic Arrays for Hardware Spiking Neural Networks". *The 32nd2th Korean Conference on Semiconductors, Jeongseon, Korea, p. 1279, Feb. 12-14, 2025*.
- Jiwon Park and Woo Young Choi\*. "Random Phase Distribution Effects of Ferroelectric Tunneling Field-Effect-Transistors (FeTFETs)". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 63, Feb. 12-14, 2025*.
- Gyuweon Jung, Hyeongsu Kim, Chayoung Lee, Jaehyeon Kim, Kangwook Choi, Woo Young Choi, and Jong-Ho Lee. "Intelligent Multimodal Sensors Integrating Gas, Barometric Pressure, and Temperature Sensing". *The 32nd Korean Conference on Semiconductors, Jeongseon, Korea, p. 125, Feb. 12-14, 2025*.

**2024**

- Geun Tae Park, Jin Wook Lee, Jae Seung Woo, and Woo Young Choi. "XNOR Operation of Binary Neural Networks Using Nanoelectromechanical Memory Switches". *IEEE Transactions on Electron Devices, vol. 71, no. 12, pp. 7955 - 7962, Dec. 2024*.
- Jin Wook Lee, Geun Tae Park, Myeong Su Shin, Woo Young Choi. "Torsional-Via-Assisted Nanoelectromechanical Memory Switches". *IEEE Electron Device Letters, vol. 45, no. 12, pp. 2573 - 2576, Dec. 2024*.
- Gyuweon Jung, Kangwook Choi, Suyeon Ju, Jaehyeon Kim, Wonjun Shin, Seongi Lee, Gyuho Yeom, Ryun-Han Koo, Young-Chang Joo, Woo Young Choi, Seungwu Han, and Jong-Ho Lee\*. "Chemisorption Manipulation by Adjusting the Carrier Concentration of the Adsorbent and Its Application to Adsorbate Identification". *ACS Materials Letters, vol. 6, no. 10, pp 4783-4790, Sep. 2024*.
- Sungjoon Kim, Hyeonseung Ji, Kyungchul Park, Hyojin So, Hyungjin Kim, Sungjun Kim\*, and Woo Young Choi\*. "Memristive Architectures Exploiting Self-Compliance Multilevel Implementation on 1 kb Crossbar Arrays for Online and Offline Learning Neuromorphic Applications". *ACS Nano, vol. 18, no. 36, pp 25128-25143, Aug. 2024*.
- Suhyeon Ahn, Junsu Yu, Hwiho Hwang, Min Suk Song, Dayeon Yu, Sungmin Hwang , In-Young Chung, Woo Young Choi , and Hyungjin Kim. "Coupling-Free Readout Scheme for Memcapacitors With NAND Flash Structure". *IEEE Transcations on Electron Devices, vol. 71, no. 8, pp. 4670 - 4676, Aug. 2024*.
- Junsu Yu, Donghyun Ryu, and Woo Young Choi. "A Novel Verification Method of Minimizing Verification Error in AND-Type Flash Arrays". *IEEE Electron Device Letters, vol.45, no. 8, pp. 1472 - 1475, Aug. 2024*.
- Sungjoon Kim, Kyungho Hong, Hyungjin Kim, Min-Hwi Kim,\* and Woo Young Choi\*. "Overshoot-Suppressed Memristor Array with AlN OxygenBarrier for Low-Power Operation in the Intelligent Neuromorphic Systems". *Advanced Intelligent Systems, vol. 6 , no. 8 , pp. 2300797, Aug. 2024*.
- Jiseong Im, Jangsaeng Kim, Joon Hwang, Minkyu Park, Ryun-Han Koo, Jonghyun Ko , Sung-Ho Park, Woo Young Choi, and Jong-Ho Lee. "Vertical AND-Type Flash TFT Array Capable of Accurate Vector-Matrix Multiplication Operations for Hardware Neural Networks". *IEEE Electron Device Letters, vol. 45, no.7, pp. 1385 - 1388, Jul. 2024*.
- Jangsaeng Kim, Jiseong Im, Wonjun Shin, Soochang Lee, Seongbin Oh, Dongseok Kwon, Gyuweon Jung, Woo Young Choi, and Jong-Ho Lee\*. "Demonstration of In-Memory Biosignal Analysis: Novel High-Density and Low-Power 3D Flash Memory Array for Arrhythmia Detection". *Advanced Science, vol. 11 , no. 26 , pp.2308460, Jul. 2024*.
- Kyungchul Park , Sungjoon Kim , Min-Hye Oh , Woo Young Choi \*. "Resting-potential-adjustable soft-reset integrate-and-fire neuron model for highly reliable and energy-efficient hardware-based spiking neural networks". *Neurocomputing, vol.590, p.127762, Jul. 2024*.
- Jin Ho Chang, Jae Seung Woo, Suk-Kang Sung, Ki-Whan Song, and Woo Young Choi. "Ternary-State Vertical NAND Flash Memory for the Improvement of the Density and Accuracy of Quantized Neural Networks". *IEEE Transactions on Electron Devices, vol. 71, no. 6, pp. 3985 - 3988, Jun. 2024*.
- Joon Hwang, Min-Kyu Park, Won-Mook Kang, Ryun-Han Koo, Kyu-Ho Lee, Dongseok Kwon, Woo Young Choi, and Jong-Ho Lee. "NOR-Type Flash Array Based on Four-Terminal TFT Synaptic Devices Capable of Selective Program/Erase Exploiting Fowler-Nordheim Tunneling". *IEEE Electron Device Letters, vol 45, no.6, pp. 1000 - 1003, Jun. 2024*.
- Kangwook Choi, Gyuweon Jung, Wonjun Shin, Jinwoo Park, Chayoung Lee, Donghee Kim, Hunhee Shin, Woo Young Choi, and Jong-Ho Lee\*. "NO2 gas response improvement method by adopting oxygen vacancy controlled In2O3 double sensing layers". *Solid State Electronics, vol. 216, p. 108926, Jun. 2024*.
- Jin Wook Lee, Geun Tae Park, and Woo Young Choi. "Analytical Release Voltage Model of Monolithic 3-D Integrated Nanoelectromechanical Memory Switches". *IEEE Transactions on Electron Devices, vol. 71, no. 5, pp. 3150-3155, May 2024*.
- Sungjoon Kim, Kyungchul Park, Kyungho Hong, Tae-Hyeon Kim, Jinwoo Park, Sangwook Youn, Hyungjin Kim,\* and Woo Young Choi\*. "Overshoot-Suppressed Memristor Crossbar Array with HighYield by AlOx Oxidation for Neuromorphic System". *Advanced Materials Technology, vol. 9, no. 11, pp.2400063, Apr. 2024*.
- Kyungchul Park, Sungjoon Kim, Jong-Hyuk Park, and Woo Young Choi. "A Quantized-Weight-Splitting Method of RRAM Arrays for Neuromorphic Applications". *IEEE Access, vol.12, pp. 59680-59687, Apr. 2024*.
- Changha Kim, Dong-Oh Kim, and Woo Young Choi. "Influence of gate-source/drain overlap on FeFETs". *Solid State Electronics, vol. 214, p. 108862, Apr. 2024*.
- Donghyun Ryu, Junsu Yu, and Woo Young Choi\*. "Reverse Charge Injection Dual-Gate Synaptic Transistors for Effective Weight Update". *IEEE Transactions on Nanotechnology, vol. 23, pp.217-222, Mar. 2024*.
- Bosung Jeon, Seunghwan Song, Jae-Joon Kim, and Woo Young Choi. "Simultaneous Spike Processing for 3D NAND-Based Spiking Neural Networks". *IEEE Electron Device Letters, vol. 45, no. 3, pp. 340-343, Mar. 2024*.
- Kyungchul Park, Sungjoon Kim, Myung-Hyun Baek, Bosung Jeon, Yeon-Woo Kim, and Woo Young Choi. "Neurons with Captive Synaptic Devices for Temperature Robust Spiking Neural Networks". *IEEE Electron Device Letters, vol. 45, no. 3, pp. 492-495, Mar. 2024*.
- Minjeong Ryu and Woo Young Choi. "Surface Stoichiometry Dependence of Ambipolar SiGe Tunnel Field-effect Transistors and Its Effect on the Transient Performance Improvement". *Journal of Semiconductor Technology and Science, vol. 24, no. 1, pp. 1-7, Feb. 2024*.
- Jihyung Kim, Subaek Lee, Sungjoon Kim, Seyoung Yang, Jung-Kyu Lee, Tae-Hyeon Kim, Muhammad Ismail, Chandreswar Mahata, Yoon Kim, Woo Young Choi\*, and Sungjun Kim\*. "Synaptic Characteristics and Vector-Matrix Multiplication Operation in Highly Uniform and Cost-Effective Four-Layer Vertical RRAM Array". *Advanced Functional Materials, vol. 34, no. 8, pp.2310193, Feb. 2024*.
- Minjeong Ryu, Jae Seung Woo, Chae Lin Jung, and Woo Young Choi. "One-Transistor Ternary Content-Addressable Memory Based on Localized Ferroelectric Switching for Massive and Accurate Routing". *IEEE Electron Device Letters, vol. 45, no. 2, pp. 144-147, Feb. 2024*.
- Kyu-Ho Lee, Dongseok Kwon, In-Seok Lee, Joon Hwang, Jiseong Im, Jong-Ho Bae, Woo Young Choi, Sung Yun Woo, and Jong-Ho Lee. "Si-Based Dual-Gate Field-Effect Transistor Array for Low-Power On-Chip Trainable Hardware Neural Networks". *Advanced Intelligent Systems, vol. 6, no. 1, p. 2300490, Jan. 2024*.
- Gyuweon Jung, Hyeongsu Kim, Chayoung Lee, Jaehyeon Kim, Woo Young Choi, and Jong-Ho Lee. "Intelligent Multimodal Sensors Integrating Gas, Barometric Pressure, and Temperature Sensing". *International Electron Devices Meeting (IEDM), San Francisco, USA, Dec. 7-11, 2024*.
- Junsu Yu, Hwiho Hwang, Hyungjin Kim, and Woo Young Choi. "Vertically Stackable Memcapacitor Crossbar Array based on NAND Flash Array Structure". *International Electron Devices Meeting (IEDM), San Francisco, USA, Dec. 7-11, 2024*.
- Soomin Kim, Seongjae Cho, Woo Young Choi, and Hyungcheol Shin. "Processing and Characterization of Polycrystalline Silicon for Ultra-Low-Power Neuromorphic Applications". *Proceedings of 2024 Materials Research Society (MRS) Fall Meeting & Exhibit, EL05.11.03, Boston, MA, USA, Dec. 1–6, 2024*.
- Donghee Kim, Gyuho Yeom, Woo Young Choi, and Jong-Ho Lee\*. "Humidity-Tolerant Neuromorphic Olfactory Systems Based on Hardware-Deployable Spiking Neural Networks and SnOx Resistor-Type Gas Sensors". *International Conference on Solid State Devices and Materials (SSDM), Himeji, Japan, pp. 107-108, Sep. 1-4, 2024*.
- Sangwoo Ryu, Ryun-Han Koo1, Wonjun Shin, Kyung Min Lee , Woo Young Choi and Jong-Ho Lee\*. "Comparative Analysis of Ferroelectric Domain Wall Motion Under Cycling Stress of HfZrO2 Fabricated by Thermal and Plasma-Enhanced Atomic Layer Depositions". *International Conference on Solid State Devices and Materials (SSDM), Himeji, Japan, pp. 107-108, Sep. 1-4, 2024*.
- Jin Ho Chang, Ji Ho Uhm, Joonggyu Kim, Eunmee Kwon, and Woo Young Choi\*. "Highly Robust and Large-Scale Quantized Neural Networks Using Hemi-Cylindrical Vertical NAND Flash Memory". *International Conference on Solid State Devices and Materials (SSDM), Himeji, Japan, pp. 107-108, Sep. 1-4, 2024*.
- Bosung Jeon, and Woo Young Choi\*. "Area-Efficient and Low-Latency 3D NAND-Based Spiking Neural Network". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Jae Seung Woo, and Woo Young Choi\*. "Tunnel-FET-Based Charge Trapping Memory for Low-Power and Large-Scale Neuromorphic Systems". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Changha Kim, Dong-Oh Kim, and Woo Young Choi\*. "Influence of Overlap Capacitance on FeFETs". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Minjeong Ryu, Jae Seung Woo, Chae Lin Jung, and Woo Young Choi\*. "Ternary Content-Addressable Memory Using Local Polarization Switching in Ambipolar Ferroelectric Tunnel-Field Effect Transistors". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Jin Wook Lee, Geuntae Park, and Woo Young Choi\*. "Deformation Transition Model for Release Voltage in Monolithic 3D-Integrated Nanoelectromechanical Memory Switches". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Jin Ho Chang, Jae Seung Woo, Suk-Kang Sung, Ki-Whan Song, and Woo Young Choi\*. "High-Density and High-Accuracy Quantized Neural Architecture Using Dual-Channel Vertical NAND Flash Memory". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Gangneung, Korea, pp. 25-26, Jul. 7-10, 2024*.
- Minjeong Ryu, Jae Seung Woo, and Woo Young Choi. "Investigation on the Local Polarization Scheme in Ferroelectric Tunnel Field-Effect Transistors for Ternary Content-Addressable Memory Applications". *IEEE Silicon Nanoelectronics Workshop (SNW), Honolulu, Hawaii, U.S.A, pp. 101-102, Jun. 15-16, 2024*.
- Bosung Jeon, Jin Ho Chang, and Woo Young Choi. "Background-Pattern-Dependency-Tolerant Weight Transfer Method for Accurate NAND-Flash Based Spiking Neural Networks". *IEEE Silicon Nanoelectronics Workshop (SNW), Honolulu, Hawaii, U.S.A, pp. 41-42, Jun. 15-16, 2024*.
- Yoon Tae Jeong, Jin Ho Chang, Jae Seung Woo, and Woo Young Choi. "Hot Carrier Injection Analysis of High-Current Driving p-MOSFETs". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1302-1304, Jan. 28-31, 2024*.
- Se Hyun Uhm, Jin Ho Chang, and Woo Young Choi. "Vertical NAND Flash Memory for Interference Suppression". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1299-1301, Jan. 28-31, 2024*.
- Seon Ho Lee, Chang Heon Park, Hyung Jun Noh, and Woo Young Choi. "Nonvolatile Memory Based on Tunnel Field-Effect Transistors". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1305-1307, Jan. 28-31, 2024*.
- Seung Hyeon Han and Woo Young Choi. "Variability Analysis of Ferroelectric Tunnel Field-Effect Transistors". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1215-1217, Jan. 28-31, 2024*.
- Minjeong Ryu and Woo Young Choi. "Ferroelectric Tunnel Field-Effect Transistors for Reconfigurable Dynamic Logic-in-Memory Computing". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1092-1094, Jan. 28-31, 2024*.
- Jin Wook Lee and Woo Young Choi. "Release Voltage Analysis of Nanoelectromechanical Memory Switches". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1089-1091, Jan. 28-31, 2024*.
- Jae Seung Woo and Woo Young Choi. "Tunnel FET-based Charge Trapping Memory for Low Power Neuromorphic Systems". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1158-1161, Jan. 28-31, 2024*.
- Jaemin Yeom, Minjeong Ryu, and Woo Young Choi. "Silicon-Germanium (SiGe) Metal-Ferroelectric-Metal-InsulatorSemiconductor (MFMIS) Tunnel Field-Effect Transistors (FeTFETs)". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1192-1194, Jan. 28-31, 2024*.
- Jin Ho Chang, Jae Seung Woo, Suk Kang Sung, Ki Whan Song, and Woo Young Choi. "Dual-Channel Vertical NAND Flash Memory for the High-Density and High-Accuracy Ternary-State Quantized Neural Networks". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1056-1059, Jan. 28-31, 2024*.
- Hyung Jun Noh, Chang Heon Park, Seon Ho Lee, and Woo Young Choi. "TFET-Based Nonvolatile Memory Optimization Regarding Trap Positions". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1204-1206, Jan. 28-31, 2024*.
- Geun Tae Park and Woo Young Choi. "Binary Neural Networks Using Nanoelectromechanical Memory Switches". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1195-1197, Jan. 28-31, 2024*.
- Chang Heon Park, Hyung Jun Noh, Seon Ho Lee, and Woo Young Choi. "Design Optimization of TFET-Based Memory". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1198-1200, Jan. 28-31, 2024*.
- Changha Kim, Dong-Oh Kim, and Woo Young Choi. "Influence of Doping Concentrations of Gate-Source/Drain Overlap Region on MFMIS FeFETs". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1210-1212, Jan. 28-31, 2024*.
- Bosung Jeon and Woo Young Choi. "Variation Mitigation in Analog Neuron Circuits Using SFS-PV Methods for Hardware Spiking Neural Networks". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1098-1100, Jan. 28-31, 2024*.
- Junsu Yu, Donghyun Ryu, and Woo Young Choi. "Impact of Verification Errors on Off-Line Training in AND-Type Flash". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1060-1062, Jan. 28-31, 2024*.
- Jonghyuk Park and Woo Young Choi. "Analog Neuron Circuits for Hardware-Based Spiking Neural Networks". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1201-1203, Jan. 28-31, 2024*.
- Yeonwoo Kim and Woo Young Choi. "Current Mirroring Methods of AND-Type Synaptic Arrays". *International Conference on Electronics, Information, and Communication (ICEIC), Taipei, Taiwan, pp. 1104-1106, Jan. 28-31, 2024*.
- Kyu-Ho Lee, Woo Young Choi, and Jong-Ho Lee. "Operation Principle of Reconfigurable Integrate-and-Fire Neuron Circuit". *The 31st Korean Conference on Semiconductors, Gyeongju, Korea, p. 1368, Jan. 24-26, 2024*.
- Kangwook Choi, Gyuweon Jung, Wonjun Shin,Jinwoo Park, Chayoung Lee, Donghee Kim, Hunhee Shin, Woo Young Choi, and Jong-Ho Lee. "Enhancement of Gas Sensing Performance in CuO Resistor-type Gas Sensors via Pre-Bias Voltage". *The 31st Korean Conference on Semiconductors, Gyeongju, Korea, p. 646, Jan. 24-26, 2024*.
- Subaek Lee, Sungjoon Kim, Hyojin So, Gyeongpyo Kim, Doohyung Kim, Minkang Kim, Juri Kim, Hyesung Nah, Woo Young Choi and Sungjun Kim. "Fabrication and Resistive Switching Characterization of HfOx-based 4-layer VRRAM for High-density Synapse Array". *The 31st Korean Conference on Semiconductors, Gyeongju, Korea, p. 109, Jan. 24-26, 2024*.
- Jin Wook Lee and Woo Young Choi. "Switching Voltage Analysis of Nanoelectromechanical Memory Switches". *The 31st Korean Conference on Semiconductors, Gyeongju, Korea, p. 719, Jan. 24-26, 2024*.
- Geun Tae Park and Woo Young Choi. "Binary Neural Networks Using Nanoelectromechanical Memory Switches". *The 31st Korean Conference on Semiconductors, Gyeongju, Korea, p. 718, Jan. 24-26, 2024*.

**2023**

- Joon Hwang, Ho-Nam Yoo, Kyu-Ho Lee, Jong-Won Back, Min-Kyu Park, Yeongheon Yang, Woo Young Choi, and Jong-Ho Lee. "Accurate SPICE Model for Cells With Tube-Type Poly-Si Channel in Cell Strings of Vertical NAND Flash Memory". *IEEE Transactions on Electron Devices, vol. 70, no. 10, pp. 5469-5474, Oct. 2023*.
- Jae Seung Woo, Chae Lin Jung, Ki Ryung Nam, and Woo Young Choi. "Logic-Compatible Charge-Trapping Tunnel Field Effect Transistors for Low-Power, High-Accuracy, and Large-Scale Neuromorphic Systems". *Advanced Intelligent Systems, vol. 5, no. 11, p. 2300242, Nov. 2023*.
- Jangsaeng Kim, Young-Tak Seo, Wonjun Shin, Woo Young Choi, Byung-Gook Park, and Jong-Ho Lee. "Hardware-Based Noisy Deep Q-Networks Using Low-Frequency Noise of Synaptic Devices for Efficient Exploration". *IEEE Electron Device Letters, vol. 44, no. 9, pp. 1571-1574, Sep. 2023*.
- Gyuweon Jung, Suyeon Ju, Kangwook Choi, Jaehyeon Kim, Seongbin Hong, Jinwoo Park, Wonjun Shin, Yujeong Jeong, Seungwu Han, Woo Young Choi, Jong-Ho Lee. "Reconfigurable Manipulation of Oxygen Content on Metal Oxide Surfaces and Applications to Gas Sensing". *ACS Nano, vol. 17, no. 18, pp. 17790–17798, Aug. 2023*.
- Gyuweon Jung, Jaehyeon Kim, Seongbin Hong, Hunhee Shin, Yujeong Jeong, Wonjun Shin, Dongseok Kwon, Woo Young Choi, Jong-Ho Lee. "Energy Efficient Artificial Olfactory System with Integrated Sensing and Computing Capabilities for Food Spoilage Detection". *Advanced Science, p.2302506, Aug. 2023*.
- Ho-Nam Yoo, Yeongheon Yang, Min-Kyu Park, Woo Young Choi, and Jong-Ho Lee. "Analysis of GIDL Erase Characteristics in Vertical NAND Flash Memory". *Journal of Semiconductor Technology and Science, vol. 23, no. 3, pp. 196-201, Jun. 2023*.
- Siyoun Lee, Seong-Yeon Kim, Haesoon Oh, Jaesung Sim, and Woo Young Choi. "Influence of Hole Current Crowding on Snapback Breakdown in Multi-Finger MOSFETs". *IEEE Access, vol. 11, pp. 60758-60762, Jun. 2023*.
- Ji Ho Uhm, Jin Ho Chang, Joonggyu Kim, Eunmee Kwon, Woo Young Choi. "Azimuthal Charge Redistribution of Hemi-Cylindrical Vertical NAND Flash Memory". *IEEE Electron Device Letters, vol. 44, no. 6, pp. 931-934, Jun. 2023*.
- Ki Ryung Nam, Kwang Soo Kim\*, and Woo Young Choi\*. "Electrical Characterization by Counter-Doped Pocket Design in Tunnel FETs". *IEEE Access, vol. 11, no. 4, pp. 30546-30554, Apr. 2023*.
- Dong-Oh Kim, Changha Kim, Hyun-Min Kim, Jonghyuk Park, Bosung Jeon, Daewoong Kwon, and Woo Young Choi. "Circular ferroelectric tunnel junctions for the improvement of memory window and endurance". *Japanese Journal of Applied Physics, vol. 62, p. SG1044, Apr. 2023*.
- Taejin Jang, Bosung Jeon, Seunghwan Song, and Woo Young Choi. "Diode-Connected Overpass Channel Synaptic Transistors for Extremely-Low-Power Neuromorphic Systems". *IEEE Electron Device Letters, vol. 44, no. 5, pp. 833-836, May 2023*.
- Yeon-Joon Choi, Suhyun Bang, Tae-Hyeon Kim, Kyungho Hong, Sungjoon Kim, Sungjun Kim, Byung-Gook Park, and Woo Young Choi. "Electric-Field-Induced Metal Filament Formation in Cobalt-Based CBRAM Observed by TEM". *ACS Applied Electronic Materials, 5(3), pp. 1834-1843, Mar. 2023*.
- Jaehyeon Kim, Wonjun Shin, Seongbin Hong, Yujeong Jeong, Gyuweon Jung, Woo Young Choi, Jae-Joon Kim, Byung-Gook Park, and Jong-Ho Lee. "A novel pathway to construct gas concentration prediction model in real-world applications: Data augmentation; fast prediction; and interpolation and extrapolation". *Sensors and Actuators B: Chemical, vol. 382, p. 133533, May 2023*.
- Tae-Hyeon Kim, Kyungho Hong, Sungjoon Kim, Jinwoo Park, Sangwook Youn, Jong-Ho Lee, Byung-Gook Park, Hyungjin Kim\*, and Woo Young Choi\*. "Fuse Devices for Pruning in Memristive Neural Network". *IEEE Electron Device Letters, vol. 44, no. 3, pp. 520-523, Mar. 2023*.
- Jae Seung Woo, Jang Woo Lee, and Woo Young Choi. "Quantitative Hot Carrier Injection Analysis of N-Type Tunnel Field-Effect Transistors". *IEEE Access, vol. 11, no. 2, pp. 14943-14950, Feb. 2023*.
- Young Suh Song, Sangwan Kim, Jang Hyun Kim, Garam Kim, Jong-Ho Lee, and Woo Young Choi. "Enhancement of Thermal Characteristics and On-Current in GAA MOSFET by Utilizing AlO-Based Dual-κ Spacer Structure". *IEEE Transactions on Electron Devices, vol. 70, no. 1, pp. 343-348, Jan. 2023*.
- Gyuweon Jung, Jaehyeon Kim, Yujeong Jeong, Jinwoo Park, Wonjun Shin, Woo Young Choi, and Jong-Ho Lee. "New Gas Identification Method Using Gas Sensor-Amplifier Merged Array and In-Memory Computing-Based Preprocessing". *International Electron Devices Meeting, San Francisco, U.S.A., pp. 33.5, Dec, 9-13, 2023*.
- Jangsaeng Kim, Jiseong Im, Jonghyun Ko, Soochang Lee, Dongseok Kwon, Wonjun Shin, Joon Hwang, Ryun-Han Koo, Woo Young Choi, and Jong-Ho Lee. "First Demonstration of Innovative 3D AND-Type Fully-Parallel Convolution Block with Ultra-High Area-and Energy-Efficiency". *International Electron Devices Meeting, San Francisco, U.S.A., pp. 23.4, Dec. 9-13, 2023*.
- Dong-Oh Kim, Changha Kim, Yeonwoo Kim, and Woo Young Choi. "Improvement of Memory Operation through Junctionless Ferroelectric-Metal Field-Effect Transistors". *International Microprocesses and Nanotechnology Conference (MNC), 17P-1-22, Nov. 2023*.
- Geun Tae Park, Jin Wook Lee, Ji Soo Yoon, and Woo Young Choi. "Multi-Layer Nanoelectromechanical (NEM) Memory Switches for Efficient Multi-Path Routing". *International SoC Design Conference (ISOCC), Jeju, Korea, pp. 75, Oct. 25-28, 2023*.
- Jiseong Im, Donghee Kim, Woo Young Choi, and Jong-Ho Lee. "Hardware Implementation of Temporal Encoded Spiking Neural Networks and Its Application to Rapid Gas Detection". *International Conference on Solid State Devices and Materials (SSDM), Nagoya, Japan, pp. 493-494, Sep. 5-8, 2023*.
- Gyuweon Jung, Kangwook Choi, Wonjun Shin, Jinwoo Park, Donghee Kim, Jaehyeon Kim, Hunhee Shin, Chayoung Lee, Woo Young Choi, and Jong-Ho Lee. "High-sensitivity, low-power FET-type NO2 gas sensor using electron concentration control of gas-sensing material". *International Conference on Solid State Devices and Materials (SSDM), Nagoya, Japan, pp. 183-184, Sep. 5-8, 2023*.
- Arati Kumari Shah, Seongjae Cho, Woo Young Choi, and Hyungcheol Shin. "A Capacitor-Truncated Compact Neuron Circuit with Spike Frequency Tunability". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 170-171, Jul. 10-11, 2023*.
- Seung Hyun Ahn, Gyeong Wook Kwak, Siyoun Lee, Seong-Yeon Kim, Haesoon Oh, Jaesung Sim, and Woo Young Choi. "Influence of Channel Width Effect on Snapback Breakdown of MOSFETs". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 104-105, Jul. 10-11, 2023*.
- Gyeong Wook Kwak, Seung Hyun Ahn, Jin Ho Chang, and Woo Young Choi. "Influence of Trapped Electrons in Charge Trap Layers on Oxide Degradation of NAND Flash Memory". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 102-103, Jul. 10-11, 2023*.
- Minjeong Ryu and Woo Young Choi. "Investigation on the Ambipolar Behavior of Si1-xGex Tunnel Field-Effect Transistors". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 90-91, Jul. 10-11, 2023*.
- Jin Wook Lee, Jae Seong Lee, and Woo Young Choi. "Nanoelectromechanical Content-Addressable Memory as Nearest Neighbor Classifier". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 112-113, Jul. 10-11, 2023*.
- Geuntae Park, Jaeseong Lee, and Woo Young Choi. "Content-Addressable Memory Based on Nanoelectromechanical Memory Switches". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 110-111, Jul. 10-11, 2023*.
- Chang Heon Park and Woo Young Choi. "Non-volatile Memory Based on Tunneling Field-Effect Transistors Using Localized Charge Trap Layers". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 108-109, Jul. 10-11, 2023*.
- Jin Ho Chang and Woo Young Choi. "Recessed Channel Hemi-Cylindrical Vertical NAND Flash Memory for the Improvement of the Program/Erase Efficiency and Memory Density". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 58-59, Jul. 10-11, 2023*.
- Jae Seung Woo and Woo Young Choi. "Effective Hot Carrier Injection Programming for TFET-Based Flash Memory". *Asia-Pacific Workshop on Advanced Semiconductor Devices, Yokohama, Japan, pp. 63-64, Jul. 10-11, 2023*.
- Bosung Jeon, Taejin Jang, Seongjae Cho, Hyungcheol Shin, and Woo Young Choi. "Synapse Array with Buried Bottom Gate Structure for Neuromorphic Systems". *IEEE Silicon Nanoelectronics Workshop (SNW), Kyoto, Japan, p. 3-03, Jun. 11-12, 2023*.
- Junsu Yu, Donghyun Ryu, Taejin Jang, and Woo Young Choi. "Influence of Weight Transfer Error on Vector-Matrix Multiplication Using AND Array Architectures". *IEEE Silicon Nanoelectronics Workshop (SNW), Kyoto, Japan, p. P-04, Jun. 11-12, 2023*.
- [Invited] Woo Young Choi. "Monolithic 3D (M3D) Complementary Metal-Oxide-Semiconductor (CMOS)-Nano-Electromechanical (NEM) Hybrid Circuits for Low-Power and High-Speed Reconfigurable Logic (RL) Applications". *IEEE International Conference on Nano/Micro Engineered and Molecular Systems (IEEE NEMS), Jeju, Republic of Korea, p. 183, May 14th-17th, 2023*.
- 이선호, 박창헌, 노형준, 최우영. "터널 전계 효과 트랜지스터 기반 비휘발성 메모리". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 6, Dec. 1, 2023*.
- 염재민, 류민정, 최우영. "SiGe을 이용한 MFMIS TFETs의 performance 향상". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 6, Dec. 1, 2023*.
- 엄세현, 장진호, 최우영. "Interference 억제를 위한 Vertical NAND 구조". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 6, Dec. 1, 2023*.
- 한승현, 최우영. "강유전체 터널링 전계효과 트랜지스터의 불규칙 변이 분석". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 4, Dec. 1, 2023*.
- 박창헌, 최우영. "전하저장형 터널링 트랜지스터의 최적화". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 6, Dec. 1, 2023*.
- 류민정, 최우영. "강유전체 터널링 전계효과 트랜지스터 기반 인-메모리 컴퓨팅". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 6, Dec. 1, 2023*.
- 박종혁, 최우영. "하드웨어 기반 스파이킹 뉴럴 네트워크 구현을 위한 뉴런 회로". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 5, Dec. 1, 2023*.
- 김연우, 최우영. "AND-형 시냅스 어레이의 전류 미러링 방법". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 4, Dec. 1, 2023*.
- 김창하, 김동오, 최우영. "강유전체 전계 효과 트랜지스터에서의 게이트-소스/드레인 오버랩 영역의 도핑 농도 영향 분석". *제6회 반도체공학회 종합학술대회, Seoul, Korea, p. 4, Dec. 1, 2023*.
- Joon Hwang, Min-Kyu Park, Won-Mook Kang, Woo Young Choi, and Jong-Ho Lee. "Effects of Inverter Circuit Size on Analog Pulse-Width Modulation Circuit". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 1013, Feb. 13-15, 2023*.
- Kangwook Choi, Gyuweon Jung, Seongbin Hong, Yujeong Jeong, Wonjun Shin, Jinwoo Park, Donghee Kim, Hunhee Shin, Woo Young Choi, and Jong-Ho Lee. "NO2 Gas Response Improvement of Gas Sensors by Adopting Oxygen Vacancy Controlled In2O3 Bilayer Sensing Films". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 120, Feb. 13-15, 2023*.
- Seongbin Oh, Woo Young Choi and Jong-Ho Lee. "Synaptic Devices Based on 3D-Semicircular NAND Flash Memory". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 782, Feb. 13-15, 2023*.
- Kyungchul Park, Sungjoon Kim, and Woo Young Choi. "A Weight Split Method of RRAM Arrays for Neuromorphic Applications". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 384, Feb. 13-15, 2023*.
- Yeonwoo Kim, Donghyun Ryu, and Woo Young Choi. "Analysis of the Current Mirroring Method for Accurate AND-Type Hardware-Based Neural Network Systems". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 531, Feb. 13-15, 2023*.
- Jonghyuk Park, Kyungchul Park and Woo Young Choi. "Compensation-Circuit-Added Current Mirror for SNN accuracy Improvement". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 532, Feb. 13-15, 2023*.
- Changha Kim, Dong-Oh Kim, Hyun-Min Kim, and Woo Young Choi. "Influence of Gate-Source/Drain Overlap Length on MFMIS FeFETs". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 132, Feb. 13-15, 2023*.
- Junsu Yu, Sungmin Hwang, Taejin Jang, and Woo Young Choi. "Influence of Weight Transfer Error on Vector-Matrix Multiplication Operation". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 533, Feb. 13-15, 2023*.
- Dong-Oh Kim, Changha Kim, Hyun-Min Kim, and Woo Young Choi. "Junctionless Ferroelectric-Metal Field-Effect Transistors (JL FeMFETs)". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 764, Feb. 13-15, 2023*.
- Donghyun Ryu, Yeonwoo Kim, and Woo Young Choi. "Poly-Si Channel Flash Memory-Based Synaptic Devices for Spiking Neural Networks". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 383, Feb. 13-15, 2023*.
- Sungjoon Kim, Kyungho Hong, Tae-Hyeon Kim, Yeon Joon Choi, and Woo Young Choi. "RRAM Array with a Pristine Low Resistance State". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 104, Feb. 13-15, 2023*.
- Kyungho Hong, Sungjoon Kim, Tae-Hyeon Kim, and Woo Young Choi. "RRAM Reset Voltage Control Using Forming Gas Annealing". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 108, Feb. 13-15, 2023*.
- Bosung Jeon, Taejin Jang, Junsu Yu, and Woo Young Choi. "Self-Aligned Asymmetric Double-Gate (SA-ADG) Synaptic Transistors for Neuromorphic Systems". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 763, Feb. 13-15, 2023*.
- Yeon-Joon Choi, Tae-Hyeon Kim, Kyungho Hong, Sungjoon Kim, Sungjun Kim, and Woo Young Choi. "Self-Compliance Effects of the SiOx/SiNy Bilayer in Co CBRAM". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 101, Feb. 13-15, 2023*.
- Min Jeong Ryu and Woo Young Choi. "Effect of Ge Mole Fraction on the Ambipolar Behavior of Si1-xGex Tunnel Field-Effect Transistors". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 768, Feb. 13-15, 2023*.
- Jin Wook Lee, Jae Seong Lee, and Woo Young Choi. "Nearest Neighbor Search Using Nanoelectromechanical (NEM) Memory Switch-Based Content-Addressable Memory". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 296, Feb. 13-15, 2023*.
- Geun Tae Park, Jae Seong Lee, and Woo Young Choi. "Ternary Content-Addressable Memory (TCAM) Using Nanoelectromechanical (NEM) Memory Switches". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 302 Feb. 13-15, 2023*.
- Chang Heon Park and Woo Young Choi. "Tunnel Field-Effect Transistor-Based Charge Trapping Memory for In-Memory Computing". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 779, Feb. 13-15, 2023*.
- Jae Seung Woo and Woo Young Choi. "Performance Enhancement Method of Line Tunnel Field-Effect Transistor (TFET) Using Hot Carrier Degradation". *The 30th Korean Conference on Semiconductors, Jeongseon, Korea, p. 535, Feb. 13-15, 2023*.

**2022**

- Jong-Won Back, Ho-Nam Yoo, Jaehyeon Kim, Min-Kyu Park, Woo Young Choi, and Jong-Ho Lee. "String Current Compensation Method in VNAND Flash for Hardware-Based BNNs". *IEEE Transactions on Electron Devices, vol. 69, no.12, pp. 6717-6721, Dec. 2022*.
- Junmo Lee, Joon Hwang, Youngwoon Cho, Min-Kyu Park, Woo Young Choi, Sangbum Kim, and Jong-Ho Lee. "CRUS: A Hardware-Efficient Algorithm Mitigating Highly Nonlinear Weight Update in CIM Crossbar Arrays for Artificial Neural Networks". *IEEE Journal on Exploratory Solid-State Computational Devices and Circuits, vol. 8, no. 2, pp. 145-154, Dec. 2022*.
- Suhyun Bang, Sungjoon Kim, Kyungho Hong, Kannan Udaya Mohanan, Seongjae Cho\*, and Woo Young Choi\*. "Fabrication and characterization of silicon nano-tip memristor for low-power neuromorphic application". *AIP Advances, vol. 12, no. 12, p.125217, Dec. 2022*.
- Kyu-Ho Lee, Dongseok Kwon, Sung Yun Woo, Jong Hyun Ko, Woo Young Choi, Byung-Gook Park, and Jong-Ho Lee. "Highly Linear Analog Spike Processing Block Integrated With an AND-Type Flash Array and CMOS Neuron Circuits". *IEEE Transactions on Electron Devices, vol. 69, no. 11, pp. 6065-6071, Nov. 2022*.
- Jin Ho Chang, Ji Ho Uhm, Hyug Su Kwon, Eunmee Kwon, and Woo Young Choi. "Influence of Channel Hole Remaining Ratio on Hemi-Cylindrical Vertical NAND Flash Memory". *IEEE E lectron Device Letters, vol. 43, no. 9, pp. 1432 - 1435, Sep. 2022*.
- Jang Woo Lee, Jae Seung Woo, and Woo Young Choi. "Synaptic Tunnel Field-Effect Transistors for Extremely-Low-Power Operation". *IEEE Electron Device Letters, vol. 43, no. 7, pp. 1149-1152, Jul. 2022*.
- Hyug Su Kwon and Woo Young Choi. "Nanoelectromechanical (NEM) Devices for Logic and Memory Applications". *Journal of Semiconductor Technology and Science, vol. 22, no. 3, pp. 188-197, Jun. 2022*.
- Hyunju Kim, Mannhee Cho, Sanghyun Lee, Hyug Su Kwon, Woo Young Choi, and Youngmin Kim. "Content-Addressable Memory System Using a Nanoelectromechanical Memory Switch". *Electronics, vol. 11, no. 3, p. 481, Feb. 2022*.
- Jisoo Yoon, Hyug Su Kwon, and Woo Young Choi. "Multi-Layer Nanoelectromechanical (NEM) Memory Switches for Multi-Path Routing". *IEEE Electron Device Letters, vol. 43, no. 1, pp.162-165, Jan. 2022*.
- Jae Seong Lee, Jisoo Yoon, and Woo Young Choi. "In-Memory Nearest Neighbor Search With Nanoelectromechanical Ternary Content-Addressable Memo ry". *IEEE Electron Device Letter s, vol. 43, no. 1, pp.154-157, Jan. 2022*.
- Gyuweon Jung, Jaehyeon Kim, Wonjun Shin, Seongbin Hong, Yujeong Jeong, Chayoung Lee, Woo Young Choi, and Jong-Ho Lee. "Innovative Gas Sensing Method Using Transient Behavior of FET-Type Sensors with Gate Pulse Input". *International Electron Devices Meeting, San Francisco, U.S.A., pp. 31.2, Dec. 3~7, 2022*.
- Kyungho Hong, Sungjoon Kim, Tae-Hyeon Kim, Hyungjin Kim, and Woo Young Choi. "Extremely-Low-Power RRAM Array with Triple Tunneling Layers". *International Microprocesses and Nanotechnology Conference (MNC), Tokushima, Japan, p.10B-2-3, Nov. 8th-11th, 2022*.
- Dong-Oh Kim, Kitae Lee, Changha Kim, Sihyun Kim, Hyun-Min Kim, Daewoong Kwon, and Woo Young Choi. "Circular Ferroelectric Tunnel Junction for Endurance Improvement". *International Microprocesses and Nanotechnology Conference (MNC), Tokushima, Japan, p.10P-3-12, Nov. 8th-11th, 2022*.
- Jangsaeng Kim, Woo Young Choi, Byung-Gook Park, and Jong-Ho Lee. "Implementation of Homeostasis Functionality in Hardware-Based Spiking Neural Networks Using an STDP Learning Rule". *International Conference on Solid State Devices and Materials (SSDM), Chiba, Japan, p.F-6-04, Sep. 26-29, 2022*.
- Hyeongsu Kim, Inseok Lee, Woo Young Choi, Byung-Gook Park, and Jong-Ho Lee. "Variation-robust Binary Matrix-vector Multiplication Method". *International Conference on Solid State Devices and Materials (SSDM), Chiba, Japan, p.F-6-03, Sep. 26-29, 2022*.
- Seongbin Oh, Seungwhan Kim, Ho-Nam Yoo, Woo Young Choi, and Jong-Ho Lee. "Synaptic Devices Based on 3D-Semicircular NAND Flash Memory". *International Conference on Solid State Devices and Materials (SSDM), Chiba, Japan, p.F-6-02, Sep. 26-29, 2022*.
- Yujeong Jeong, Seongbin Hong, Gyuweon Jung, Wonjun Shin, Woo Young Choi, and Jong-Ho Lee. "H2S Sensing Characteristics of the Amplifier Circuit Consisting of pFET-type and Resistor-type Gas Sensors". *International Conference on Solid State Devices and Materials (SSDM), Chiba, Japan, p.D-3-05, Sep. 26-29, 2022*.
- Jiseong Im, Donghee Kim, Woo Young Choi, and Jong-Ho Lee. "A Neuromorphic Olfactory System Using Temporal Encoded Spiking Neural Networks". *International Conference on Solid State Devices and Materials (SSDM), Chiba, Japan, p.D-3-03, Sep. 26-29, 2022*.
- Gyuweon Jung, Wonjun Shin, Hunhee Shin, Seongbin Hong, Yujeong Jeong, Kangwook Choi, Jinwoo Park, Donghee Kim, Chayoung Lee, Jaehyeon Kim, Woo Young Choi, and Jong-Ho Lee. "Comparison of the H2S gas response characteristics of semiconductor gas sensors (HFGFET-, TFT-, and resistor-type) fabricated on the same wafer". *International Conference on Solid State Devices and Materials (SSDM), Chib a, Japan, p.D-1-01, Sep. 26-29, 2022*.
- Hyug Su Kwon, Jisoo Yoon, and Woo Young Choi. "Monolithic Three-Dimensional (M3D) Integration of Nanoelectromechanical (NEM) Memory Switches". *Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices, Virtual, pp. 111-112, Jul. 7-8, 2022*.
- Jang Woo Lee and Woo Young Choi. "π-shaped Tunnel FETs for Performance Enhancement". *Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices, Virtual, pp. 49-50, Jul. 7-8, 2022*.
- Bu-Il Nam, Youngha Choi, Sungki Hong, Ki-Young Dong, Wontaeck Jung, Sang-Won Park, Soon-Yong Lee, Dooyeun Jung, Byoung-Hee Kim, Eunkyoung Kim, Ki-Whan Song, Jai Hyuk Song, and Woo Young Choi. "Novel Electrical Detection Method for Random Defects on Peripheral Circuits in NAND Flash Memory". *IEEE International Reliability Physics Symposium (IRPS), Dallas, TX, USA, pp. P40-1-P40-4, Mar. 27~31, 2022*.
- Juwon Lee, Junho Seo, Jeonghun Nam, YongLae Kim, Ki-Whan Song, Jai Hyuk Song, and Woo Young Choi. "Electric Field Impact on Lateral Charge Diffusivity in Charge Trapping 3D NAND Flash Memory". *IEEE International Reliability Physics Symposium (IRPS), Dallas, TX, USA, pp. P29-1-P29-5, Mar. 27~31, 2022*.
- Jang Woo Lee, Jae Seung Woo, and Woo Young Choi. "Temperature Dependence of SONOS Tunnel Field-Effect Transistors". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 52, Jan. 24-26, 2022*.
- Hyug Su Kwon and Woo Young Choi. "Performance Comparison of Monolithic Three-Dimensional (M3D) Nanoelectromechanical (NEM) Memory Switches". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 113, Jan. 24-26, 2022*.
- Jae Seung Woo, Kyung Min Koo, and Woo Young Choi. "Gate-Normal Charge Trapped (GCT) Tunnel Field-Effect Transistors (TFETs)". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 151, Jan. 24-26, 2022*.
- Jae Seong Lee and Woo Young Choi. "Nanoelectromechanical-Switch-Based Ternary Content-Addressable Memory (NEMTCAM)". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 113, Jan. 24-26, 2022*.
- Hyeontae Bang, Sangjun Lee, Jae Seung Woo, and Woo Young Choi. "Nanoelectromechanical Memory Switches for Binary Neural Networks". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 140, Jan. 24-26, 2022*.
- Siyoun Lee, Seong-Yeon Kim, Haesoon Oh, Jaesung Sim, and Woo Young Choi. "Snapback Breakdown of MOSFETs Including Self-Heating Effects". *The 29th Korean Conference on Semiconductors, Jeongseon, Korea, p. 52, Jan. 24-26, 2022*.

**2021**

- Jang Woo Lee, Jae Seung Woo, and Woo Young Choi. "Tunneling Field-Effect Transistor for Neuromorphic Application". *Journal of Semiconductor Engineering, vol. 2, no.3, 142-153, Dec. 2021*.
- Jae Seong Lee and Woo Young Choi. "Nanoelectromechanical-Switch-Based Ternary Content-Addressable Memory (NEMTCAM)". *IEEE Transactions on Electron Devices, vol. 68, no. 10, pp.4903-4909, Oct. 2021*.
- Kyung Min Koo, Woo Young Chung, Sang Yi Lee, Gyu Han Yoon, and Woo Young Choi. "Modeling of Statistical Variation Effects on DRAM Sense Amplifier Offset Voltage". *Micromachines, vol. 12, p. 1145, Sep. 2021*.
- Jae Seong Lee and Woo Young Choi. "Nanoelectromechanical-Switch-Based Binary Content-Addressable Memory (NEMBCAM)". *IEEE Access, vol. 9, pp. 70214-70220, May 2021*.
- Shinhee Kim, Jae Yeon Park, Seungwon Go, Hyug Su Kwon, Woo Young Choi, and Sangwan Kim. "A low-power nanoelectromechanical (NEM) device with Al-doped HfO2-based ferroelectric capacitor". *Solid-State Electronics, vol. 175, p. 107956, Jan. 2021*.
- Hye In Kim, Jung Min Sung, Hyung Uk Cho, Yong Jo Kim, Young Gwan Park, and Woo Young Choi. "LTPS TFTs with an Amorphous Silicon Buffer Layer and Source/Drain Extension". *Electronics, vol. 10, no. 1, p. 29, Jan. 2021*.
- Dooyeun Jung, Youngha Choi, Jae In Lee, Bu-il Nam, Ki-Young Dong, Bohchang Kim, Eunkyoung Kim, Ki-Whan Song, Jai Hyuk Song, Myungsuk Kim, and Woo Young Choi. "Electrical Screening Me thod of V-NAND Flash Channel Hole Bending Defects". *Proceedings from the 47th International Symposium for Testing and Failure Analysis (ISTFA). Pho enix, AZ, USA, pp. 306-308, Oct. 31–Nov. 4, 2021*.
- Jeongin Choe, Taehyeon Kim, Saetbyeol Yoon, Sangyong Yoon, Ki-Whan Song, Jai Hyuk Song, Myungsuk Kim, and Woo Young Choi. "Wafer Pattern Recognition for Detecting Process Abnormalities in NAND Flash Me mory Manufacturing". *Proceedings from the 47th International Symposium for Testing and Failure Analysis (ISTFA). Phoenix, AZ, USA, pp. 406-409, Oct. 31–Nov. 4, 2021*.
- Jisuk Kim, Earl Kim, Daehyeon Lee, Taeheon Lee, Daesik Ham, Miju Yang, Wanha Hwang, Jaeyoung Kim, Sangyong Yoon, Youngwook Jeong, Eunkyoung Kim, Ki-Whan Song, Jai Hyuk Song, Myungsuk Kim, and Woo Young Choi. "Machine Learning Based Optimization Technique for High-Capacity V-NAND Flash Memory". *Proceedings from the 47th International Symposium for Testing and Failure Analysis (ISTFA). Phoenix, AZ, USA, pp. 20-22, Oct. 31–Nov. 4, 2021*.
- Jae Seong Lee and Woo Young Choi. "Nonvolatile Content-Addressable Memory using Nanoelectromechanical Memory Switches for Data-Intensive Computation". *Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices, Virtual(Japan), pp. 29-30, Aug. 26-27, 2021*.
- Jae Seung Woo, Jang Woo Lee and Woo Young Choi. "Local Electric Field Concentration of Tunnel Field-Effect Transistors". *Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices, Virtual(Japan), pp. 69-70, Aug. 26-27, 2021*.
- Jang Woo Lee, Jae Seung Woo, and Woo Young Choi. "SONOS 터널링 전계 효과 트랜지스터의 온도 의존성". *제4회 반도체공학회 종합학술대회, Seoul, Korea, pp. 2, Dec. 15, 2021*.
- Gwangryeol Baek, Jisoo Yoon, and Woo Young Choi. "Tri-State Nanoelectromechanical Memory Switches". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 750, Jan. 25-29, 2021*.
- Hyug Su Kwon, and Woo Young Choi. "Tile-to-tile operation of monolithic three-dimensional (M3D) CMOS-Nanoelectromechanical (NEM) Reconfigurable Logic (RL)". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 731, Jan. 25-29, 2021*.
- Jae Seung Woo, Jang Woo Lee and Woo Young Choi. "Hot Carrirer Injection Analysis of Tunnel Field Effect Transistors". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 231, Jan. 25-29, 2021*.
- Kyung Min Koo, Woo Young Chung, Sang Yi Lee, Gyu Han Yoon, and Woo Young Choi. "Modeling of Statistical Variation Effects on DRAM Sense Amplifier Offset Voltage". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 231, Jan. 25-29, 2021*.
- Jae Seong Lee, and Woo Young Choi. "Content-Addressable Memory (CAM) Based on Nanoelectromechanical (NEM) Memory Switches for Low-Energy and High Speed Operation". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 231, Jan. 25-29, 2021*.
- Ha Rim Jeon, Yoon-Suk Kim, Uihui Kwon, and Woo Young Choi. "Compact Model of Metal-Ferroelectric-Insulator-Semiconductor (MFIS) Negative Capacitance FETs". *The 28th Korean Conference on Semiconductors, virtual, Korea, p. 231, Jan. 25-29, 2021*.

## 특허

랩 Patents의 출원일이나 등록일 중 하나라도 2021년 10월 22일–2026년 10월 22일에 드는 48개 번호 항목이다. 하나의 번호 아래 여러 국가의 출원·등록 기록이 있으면 함께 적었다. 최우영 교수의 서울대 부임 전 서강대 재직 시기 출원도 포함하며, 기간 전에 출원했더라도 기간 안에 등록된 항목이 있다.[^patents]

- 불휘발성 메모리 장치, 스토리지 장치, 및 불휘발성 메모리 장치의 소거 방법 (Korean Patent filed 10-2026-0179024 , Sep. 18th, 2026.) (발명자 최우영, 남재현, 이수창, 정의현, 채동혁, 최나영)
- 양극성 강유전체 터널링 전계 효과 트랜지스터 기반의 인-메모리 로컬리티 센서티브 해싱 장치 및 그 동작 방법 (Korean Patent filed 10-2026-0170509 , Sep. 8 th, 2026.) (발명자 최우영, 류민정)
- 저전력 3진 가중치 디지털 연산 장치 및 그 구동방법 (Korean Patent filed 10-2026-0159978, Aug. 25 th, 2026.) (발명자 최우영, 우재승)
- 반도체 장치 (Korean Patent filed 10-2026-0126508, Jul. 9th, 2026.) (발명자 최우영, 이진욱, 백승훈, 신명수)
- 시간도메인 보안 연산 장치 및 이를 이용한 시간도메인 보안 연산 방법 (Korean Patent filed 10-2026-0121451, Jul. 2nd, 2026.) (발명자 최우영, 백승훈, 신명수, 이진욱)
- 내용 주소화 메모리 셀, 이의 제조 방법 및 이를 이용한 내용 주소화 메모리 장치 (Korean Patent filed 10-2026-0043766, Mar. 11th, 2026.) (발명자 최우영, 류민정)
- 나노전기기계 메모리 기반 비트셀 및 이를 포함하는 장치 (Korean Patent filed 10-2026-0013475, Jan. 23rd, 2026. US Patent filed 19/536,364, Feb. 11 th, 2026.) (발명자 최우영, 신명수, 이진욱)
- 인메모리 연산을 수행하는 불휘발성 메모리 장치 및 이를 포함하는 연산 가속기 (Korean Patent filed 10-2026-0007848, Jan. 15th, 2026.) (발명자 최우영, 배병준)
- 임베디드 플래시 메모리 소자, 이의 제조 방법 및 이를 이용한 뉴로모픽 하드웨어 소자 (Korean Patent filed 10-2025-0173580, Nov. 11th, 2025. US Patent filed 19/575,925, Mar. 24 th, 2026. Korean Patent No. 10-3008040, Aug. 18 th, 2026.) (발명자 최우영, 우재승)
- 0차 최적화 기법에서 아날로그 전류 합산 기반 병렬 전방패스를 이용한 인공신경망 학습 장치 및 시스템 (Korean Patent filed 10-2025-0154928, Oct. 23rd, 2025. PCT filed PCT/KR/2026/001441, Jan. 23rd, 2026. US Patent filed 19/545,423, Feb. 20 th, 2026.) (발명자 최우영, 우재승)
- 삼진 CIM연산을 수행하는 메모리 장치 및 그 동작 방법 (Korean Patent filed 10-2025-0117043, Aug. 22nd, 2025. PCT filed PCT/KR2026/003234, Feb. 27th, 2026.) (발명자 최우영, 염재민)
- 내용 주소화 메모리 장치 (Korean Patent filed 10-2025-0085646, Jun. 27th, 2025.) (발명자 최우영, 이진욱, 김창하)
- 반도체 메모리 소자 (Korean Patent filed 10-2025-0075838, Jun. 10th, 2025. US Patent filed 19/463,748, Jan. 29 th, 2026. CN Patent filed 202610206934.3, Feb. 12th, 2026.) (발명자 최우영, 배병준)
- 강유전체 양극성 멤커패시터 기반 시간 도메인 내용 주소화 기억 장치의 연산 정확도 및 스케일러빌리티 향상을 위한 동작 방법 (Korean Patent filed 10-2025-0071243, May 30th, 2025. Priority claim filed 10-2025-0175341, Nov. 19 th, 2025. US Patent filed 19/539,889, Feb. 13 th, 2026.) (발명자 최우영, 류민정)
- 수직형 메모리 장치 (Korean Patent filed 10-2025-006418, May 16th, 2025. US Patent filed 19/678,499, May. 15 th, 2026.) (발명자 최우영, 김경문, 김준형, 성석강)
- 나노전기기계 커패시티브 메모리 소자 및 이의 제조 방법 (Korean Patent filed 10-2025-0024966, Feb. 26th, 2025. US Patent filed 19/775,878, Aug. 14th, 2026. Korean Patent No. 10-3017327, S ep. 4 th, 2026.) (발명자 최우영, 박근태, 이진욱)
- 3차원 반도체 메모리 장치 및 그 동작 방법 (Korean Patent filed 10-2025-0000411, Jan. 2nd, 2025.) (발명자 최우영, 문기봉, 양다은, 이재덕)
- 상보적 데이터 쌍을 활용한 PUF 기반의 인시츄 암호화 방법 및 이를 위한 컴퓨터 장치 (Korean Patent filed 10-2024-0181322, Dec. 9th, 2024. US Patent filed 19/310,909, Aug. 26 th, 2025.) (발명자 최우영, 김창하, 이진욱)
- 메모리 집적도 향상을 위한 반도체 메모리 소자 (Korean Patent filed 10-2024-0179233, Dec. 5th, 2024. US Patent filed 19/409,559, Dec. 4 th, 2025.) (발명자 최우영, 장진호)
- 반도체 장치 및 데이터 저장 시스템 (Korean Patent filed 10-2024-0125611, Sep. 13th, 2024. US Patent filed 19/096,972, Apr. 1st, 2025. CN Patent filed 202510720349.0 , M ay 30th, 2025.) (발명자 최우영, 김동오, 김창하, 이기석)
- 나노 전기기계 커패시티브 메모리 소자 및 그 제조 방법 (Korean Patent filed 10-2024-0085700, Jun. 28th, 2024. Korean Patent No. 10-2909559, Jan. 5 th, 2026.) (발명자 최우영, 이진욱, 박근태)
- 싱글 폴리 구조의 임베디드 플래시 메모리 소자, 이의 제조 방법 및 이를 이용한 뉴로모픽 하드웨어 소자 (Korean Patent filed 10-2024-0065551, May 21st, 2024. Korean Patent No. 10-2888997, Nov. 17 th, 2025. Priority claim filed 10-2024-0065551, May 21st, 2024. PCT filed PCT/KR2024/096811, Dec. 12 th, 2024. US Patent filed 19/123,851, Apr. 24 th, 2025. CN Patent filed 202480004087.1 , Mar. 20 th, 2025.) (발명자 최우영, 우재승)
- 스파이킹 인공 신경망 기반의 나노 전기기계 뉴런 장치 (Korean Patent filed 10-2023-0196970, Dec. 29th, 2023. Korean Patent No. 10-2931606, Feb. 23rd, 2026. Priority claim filed 10-2024-0089754, Jul. 8th, 2024. PCT filed PCT/KR2024/011328, Aug. 1st, 2024. US Patent filed 18/824,524, Sep. 4th, 2024.) (발명자 최우영, 우재승, 박근태)
- 뉴로모픽 메모리 장치 및 이를 이용한 뉴로모픽 시스템 (Korean Patent filed 10-2023-0196971, Dec. 29th, 2023. Priority claim filed 10-2024-0129264, Sep. 24th, 2024. Korean Patent No. 10-2931759, Feb. 23rd, 2026. US Patent filed 18/939,966, Nov. 7th, 2024.) (발명자 최우영, 전보성)
- 나노 전기기계 소자 및 그 제조 방법 (Korean Patent filed 10-2023-0190086, Dec. 22nd, 2023. Priority claim filed 10-2024-0072633, Jun. 3rd, 2024. Korean Patent No. 10-2911335, Jan. 7th, 2026. PCT filed PCT/KR2024/008511, Jul. 10th, 2024. US Patent filed 18/790,360, Jul. 31st, 2024.) (발명자 최우영, 이진욱)
- 트랜지스터의 커패시턴스-전압 특성을 이용한 시간 도메인 내용 주소화 기억 장치 및 동작 방법 (Korean Patent filed 10-2023-0170632, Nov. 30th, 2023. Priority claim filed 10-2024-0025973, Feb. 22nd, 2024. Korean Patent No. 10-3032601, Oct. 8th, 2026. US Patent filed 18/893,127, Sep. 23rd, 2024. CN Patent filed 202411607618.4 , Nov. 12 th, 2024.) (발명자 최우영, 류민정)
- 뉴로모픽 소자 및 그 동작 방법 (Korean Patent filed 10-2023-0171646, Nov. 30 th, 2023. Korean Patent No. 10-2905823, Dec. 24th, 2025. Priority claim fi led 10-2024-0069309, May 28th, 2024 US Patent filed 18/796,752, Aug. 7th, 2024.) (발명자 최우영, 우재승)
- 연상형 메모리 소자 및 그 제조방법 (Korean Patent filed 10-2023-0143938, Oct. 25th, 2023. Korean Patent No. 10-2854189, Aug. 29 th, 2025.) (발명자 최우영, 정상현, 성호근, 박성민, 최영수, 박형호)
- 나노구조체를 갖는 연상형 메모리 소자 및 그 제조방법 (Korean Patent filed 10-2023-0143937, Oct. 25th, 2023. Korean Patent No. 10-2949767, Apr. 3rd, 2026.) (발명자 최우영, 정상현, 성호근, 박성민, 최영수, 박형호)
- 반도체 메모리 장치, 그의 제조 방법 및 그를 포함하는 전자 시스템 (Korean Patent filed 10-2023-0086436, Jul. 4 th, 2023. Korean Patent No. 10-2831991, Jul. 4th, 2025.) (발명자 최우영, 장진호)
- 전하저장형 터널링 트랜지스터 소자 및 그 동작 방법 (Korean Patent filed 10-2023-0044785, A pr. 5 th, 2023. Korean Patent No. 10-2818408, Jun. 4th, 2025. Priority claim filed 10-2024-0044371, Apr. 1st, 2024. PCT filed PCT/KR2024/004316, Apr. 3rd, 2024. US Patent filed 18/836,279, Aug. 6th, 2024.) (발명자 최우영, 박창헌, 우재승, 이장우)
- 반도체 소자의 진공 패키징 방법 및 이에 따라 제조된 반도체 소자 (VACUUM PACKAGING MANUFACTURING METHOD AND SEMICONDUCTOR DEVICES MANUFACTURED THEREBY) (Korean Patent filed 10-2023-0035045, Mar. 17th, 2023. Korean Patent No. 10-2941433, Mar. 16th, 2026. PCT filed PCT/KR2023/019459, Nov. 29 th, 2023. US Patent filed 18/405,328, Jan. 5th, 2024. US Patent No. 12,721,057 Aug. 25 th, 2026. CN Patent filed 202380012901.X , Jan. 18th, 2024.) (발명자 최우영)
- CMOS-NEM 기반 연상형 메모리 증대 신경망 소자 및 그 제조방법 (Korean Patent filed 10-2022-0149014, Nov. 9 th, 2022. Korean Patent No. 10-2785984, Mar. 19th, 2025.) (발명자 최우영, 정상현, 박경호, 김진현, 김상수, 박형호, 최영수, 박덕수, 조주영, 김창환, 황선용, 임웅선, 이동근, 박성민, 김재무, 강수정)
- 곡면형 CMOS-NEM 기반 연상형 메모리 증대 신경망 소자 및 그 제조방법 (Korean Patent filed 10-2022-0149028, Nov. 9th, 2022. Korean Patent No. 10-2785999, Mar. 19th, 2025.) (발명자 최우영, 정상현, 박경호, 김진현, 김상수, 박형호, 최영수)
- Content Addressable Memory Device and Operating Method Thereof (Korean Patent filed 10-2021-0111470, Aug. 24th, 2021. Priority claim filed 10-2022-0104120, Aug. 19th, 2022. Korean Patent No. 10-2646177, Mar. 6th, 2024. US Patent filed 17/893,646, Aug. 23rd, 2022. US Patent No. 12,243,574 Mar. 4th, 2025. PCT filed PCT/KR2022/012624, Aug. 24th, 2022.) (발명자 Woo Young Choi)
- Nano-electromechanical devices (Korean Patent filed 10-2022-0079853, Jun. 29 th, 2022. Korean Patent No. 10-2792251, Apr. 2nd, 2025.) (발명자 Woo Young Choi and Hyug Su Kwon)
- A Ternary Content-Addressable Memory Using a Nanoelectromechanical Memory Switch and Method Thereof (Korean Patent filed 10-2021-0136413, Oct. 14 th, 2021. Korean Patent No. 10-2525833, Apr. 21st, 2023.) (발명자 김영민, 김현주, 조만희, Woo Young Choi, 권혁수)
- Binary neural network and its operation method (Korean Patent filed 10-2021-0091837, Jul. 13th, 2021. Korean Patent No. 10-2610430, Dec. 1st, 2023.) (발명자 Woo Young Choi)
- Neuromorphic computing system (Korean Patent filed 10-2021-0078468, Jun. 17th, 2021. Korean Patent No. 10-2565801, Aug. 7th, 2023.) (발명자 Woo Young Choi, Jang Woo Lee and Jae Seung Woo)
- Content-Addressable Memory and Method for Degree of Match Detection Using them (Korean Patent filed 10-2021-0061883, May. 13th, 2021. Korean Patent No. 10-2490781, Jan. 17th, 2023.) (발명자 Woo Young Choi)
- TUNNELING FIELD EFFECT TRANSISTOR AND FABRICATION METHODS OF THE SAME (Korean Patent filed 10-2020-0172041, Dec. 10th, 2020. Korean Patent No. 10-2570731, Aug. 22nd, 2023.) (발명자 Woo Young Choi and Jaeseung Woo)
- LOW VOLTAGE ELECTROMECHANICAL SWITCH BASED ON DYNAMIC SLINGSHOT OPERATION AND METHOD OF SAME (Korean Patent filed 10-2020-0059750, May. 19th, 2020. Korean Patent No. 10-2605542, Nov. 20 th, 2023.) (발명자 Woo Young Choi)
- 5-TERMINAL NANOELECTROMECHANICAL BASED CONTENT ADDRESSABLE MEMORY DEVICE AND SEARCH DEVICE USING THE SAME (Korean Patent filed 10-2020-0035587, Mar. 24th, 2020. Korean Patent No. 10-2484248, Dec. 29 th, 2022.) (발명자 Woo Young Choi)
- 3-TERMINAL NANOELECTROMECHANICAL BASED CONTENT ADDRESSABLE MEMORY DEVICE AND SEARCH DEVICE USING THE SAME (Korean Patent filed 10-2020-0035591, Mar. 24th, 2020. Korean Patent No. 10-2461477, Oct. 27 th, 2022.) (발명자 Woo Young Choi)
- 3-dimensional NAND flash memory device and method of fabricating the same (Korean Patent filed 10-2020-0031945, Mar. 16th, 2020. US Patent filed 17/203,352, Mar. 16th, 2021. US Patent No. 11,437,401, Sep. 6th, 2022. US Patent filed 17/877,118, Jul. 29 th, 2022. US Patent No. 11,956,963, Apr. 9 th, 2024. Korean Patent No. 10-2908867, Jan. 2nd, 2026.) (발명자 Woo Young Choi)
- Lateral Vacuum Channel Transistor Devices and Their Fabrication (Korean Patent filed 10-2020-0010286, Jan. 29th, 2020. Korean Patent No. 10-2662964, Apr. 29th, 2024.) (발명자 Woo Young Choi and Hyugsu Kwon)
- Non-volatile memory device and method of fabricating the same (Korean Patent filed 10-2016-0094019, Jul. 25th, 2016. Korean Patent No. 10-2395563, May 3rd, 2022. US Patent filed 15/658,293, Jul. 24th, 2017. US Patent No. 9,984,758, May 29th, 2018.) (발명자 Woo Young Choi)
- Non-volatile memory device and method of fabricating the same (Korean Patent filed 10-2016-0088850, Jul. 13th, 2016. Korean Patent No. 10-2635349, Feb. 5th, 2024. US Patent filed 15/647,692, Jul. 12th, 2017. US Patent No. 10,546,934, Jan. 28th, 2020.) (발명자 Woo Young Choi)

## 수상과 선정

2021년 10월 22일–2026년 10월 22일 범위의 Award 게시 21항목과 교수 소개의 2023년 공로상 1항목이다. 최우영 교수의 서울대 부임 전 서강대 재직 시기 항목도 포함한다. 날짜는 누리집 표기이며 교수 소개의 공로상은 연도만 게시되어 있다.[^award][^prof]

- Jin Ho Chang, 우수상, 2026 삼성전자 산학협력 우수논문상, Aug. 19th, 2026.
- Myeong Su Shin, 현장우수포스터상, Korean Conference on Semiconductors (KCS), Jan. 27 th, 2026.
- Jin Wook Lee, Geun Tae Park, Myeong Su Shin, Seung Hun Baek, Jae Seung Woo, Sang Hyun Jung, Jin Wook Bum, Sung In Cho, and Woo Young Choi, 2025년 국가연구개발(R&D) 우수성과 선정, Jan. 30th, 2026.
- Jae Seung Woo and Woo Young Choi, 대상, 제 17회 ICT 논문 공모 대제전, Dec. 18th, 2025.
- Geun Tae Park, Jin Wook Lee, and Woo Young Choi, The 2025 IEEE Electron Devices Society MEMS Student Challenge, Recognition of being a Finalist, Oct. 2025.
- Chang Hyeon Park, 우수논문상, 반도체공학회 하계 종합 학술대회, Jul. 15th, 2025.
- M inseok Cha, 현장우수포스터상, Korean Conference on Semiconductors (KCS), Feb. 14 th, 2025.
- Woo Young Choi, PIM인공지능반도체 핵심기술개발사업(소자) 우수연구성과, PIM인공지능반도체사업단, Nov. 25th, 2024.
- Jae Seung Woo, Young Researcher Poster Award, Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices (AWAD 2024), IEIE & IEICE, Jul. 9th, 2024.
- Jin Wook Lee, Young Researcher Award, Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices (AWAD 2024), IEIE & IEICE, Jul. 9th, 2024.
- Woo Young Choi, Outstanding Teaching Award, Co llege of Engineering, Seoul National University, Apr. 17th, 2024.
- Yeonwoo Kim and Woo Young Choi, 우수논문상, 반도체공학회 종합학술대회, Dec. 1st, 2023.
- Min Jeong Ryu and Woo Young Choi, 우수논문상 (포스터 부문), 반도체공학회 종합학술대회, Dec. 1st, 2023.
- Geun Tae Park, Jin Wook Lee, Ji Soo Yoon, and Woo Young Choi , Best Poster Award, International SoC Design Conference (ISOCC), Oct. 26th, 2023.
- Jin Ho Chang, Young Researcher Award, Asia-Pacific Workshop on Fundamentals and Applications of Advanced Semiconductor Devices (AWAD 2023), IEIE & IEICE, Jul. 11 th, 2023.
- Min Jeong Ryu, 현장우수포스터상, Korean Conference on Semiconductors (KCS), Apr. 12th, 2023.
- Jin Ho Chang, 우수상, Qualcomm Best Paper Award, Qualcomm Korea, Dec. 5th, 2022.
- Hyug Su Kwon, SMDL Best Paper Awards (Guest Prize), SMDL SNU, Feb. 18th, 2022.
- Kyung Min Koo, 학술대회 우수논문상(포스터), 한국전기전자학회, Dec. 17th, 2021.
- Jisoo Yoon, Qualcomm Best Paper Award, Qualcomm Korea, Dec. 10th, 2021.
- Jae Seong Lee, Qualcomm Best Paper Award, Qualcomm Korea, Dec. 10th, 2021.
- 2023년 · 최우영, 공로상, 대한전자공학회

## 연락과 위치

- 교수: 서울대학교 301동 601호, 전화 02-880-1662, 이메일 wooyoung@snu.ac.kr[^prof]
- 학생 사무실: 서울대학교 301동 1014–1015호[^home]
- 측정실: 서울대학교 301동 1052-3호, 행정실: 301동 1019호[^home]
- 산학협력교수 Kim, Jiyoung: 301동 512-3호, 이메일 hbt100@snu.ac.kr[^staff]
- 주소: 서울특별시 관악구 관악로 1 서울대학교, 우편번호 08826[^home]
## 각주

[^home]: 연구실 첫 화면·위치. <https://sites.google.com/view/snutidl>
[^prof]: 교수 소개·경력·연락처. <https://sites.google.com/view/snutidl/people/professor>
[^staff]: 산학협력교수·박사후연구원. <https://sites.google.com/view/snutidl/people/research-prof-post-doc-univ-industry-collaboration-prof>
[^graduate]: 대학원생 명단. <https://sites.google.com/view/snutidl/people/graduate>
[^alumni]: 서울대·서강대 학위별 졸업생. <https://sites.google.com/view/snutidl/people/alumni>
[^research]: 연구의 두 축. <https://sites.google.com/view/snutidl/research/research-topic>
[^journal]: 학술지·사전 공개본 목록. <https://sites.google.com/view/snutidl/publication/journal>
[^conference]: 국제·국내 학회 목록. <https://sites.google.com/view/snutidl/publication/conference>
[^patents]: 출원·등록 목록. <https://sites.google.com/view/snutidl/publication/patents>
[^award]: 수상·선정 목록. <https://sites.google.com/view/snutidl/publication/award>
[^dept-prof]: 학과 교수 소개·2022년 3월 부임·전문 분야. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p874>
[^dept-lab]: 학과 연구실 상세·연구 범위. <https://ece.snu.ac.kr/research-faculty/research/lab?md=view&labidx=118>
[^p1]: J. S. Woo 외, W. Y. Choi, Advanced Intelligent Systems 8, 2500547 (온라인 2025-08-15). <https://doi.org/10.1002/aisy.202500547> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500547>
[^p2]: J. H. Chang 외, W. Y. Choi, Advanced Intelligent Systems 8, e202500655 (온라인 2025-11-18). <https://doi.org/10.1002/aisy.202500655> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500655>
[^p3]: J. Park, S. Kim, W. Y. Choi, Advanced Intelligent Systems 7, 2400673 (온라인 2024-11-24). <https://doi.org/10.1002/aisy.202400673> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202400673>
[^p4]: J. Kim 외, S. Kim, Advanced Functional Materials 34, 2310193 (온라인 2023-11-14). <https://doi.org/10.1002/adfm.202310193> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202310193>
[^p5]: M. Ryu 외, W. Y. Choi, Advanced Electronic Materials 11, e00421 (온라인 2025-10-13). <https://doi.org/10.1002/aelm.202500421> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202500421>
[^p6]: J. Yeom 외, W. Y. Choi, IEEE Transactions on Electron Devices 72, 3302-3306 (2025). <https://doi.org/10.1109/TED.2025.3561710> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/391255747_One-Ferroelectric-Tunnel-FET-Based_Reconfigurable_Logic_Gates>
[^p7]: J. W. Lee 외, W. Y. Choi, Advanced Intelligent Systems 8, 2500586 (온라인 2025-09-02). <https://doi.org/10.1002/aisy.202500586> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500586>
[^p8]: C. Kim 외, W. Y. Choi, Advanced Intelligent Systems 7, 2400805 (온라인 2025-03-26). <https://doi.org/10.1002/aisy.202400805> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/aisy.202400805>

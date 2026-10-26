# 인공지능향 반도체 소자 연구실 (Semiconductor Devices Lab for AI, SDLA)

**서울대학교 첨단융합학부 차세대지능형반도체전공, 공과대학 전기·정보공학부(겸임) · 정규원 조교수**

- 분야: 인공지능용 반도체 소자, 감각 신호 처리, 메모리 소자와 연산 하드웨어
- 대분야: 전기전자·반도체·광학
- 태그: 뉴로모픽 소자[^research][^ferro], 메모리 내 연산[^insensor][^ferro], 메모리 반도체 소자[^dram][^vnand], 강유전체[^ferro], 산화물 반도체[^oxide], MEMS 미세 기계 소자[^tactile]
- 홈페이지: <https://sdla.snu.ac.kr/>
- 근거와 출처: [SDLA 근거 페이지](sdla-sources.md)

> 가스·압력·온도·촉각을 전기 신호로 바꾸는 센서와 정보를 저장하는 반도체를 만들고, 감지·저장·계산을 칩 안에서 연결해 인공지능에 쓰는 연구실이다.[^research][^insensor][^tactile]

## 무엇을 연구하나

SDLA는 정규원 교수가 이끄는 인공지능용 반도체 소자 연구실이다. 반도체 소자는 반도체의 전기적 성질을 이용해 신호를 조절하거나 정보를 처리하는 부품이다. 연구실은 센서, 메모리(데이터를 저장하는 장치), 뉴로모픽 소자(신경세포와 신경세포 사이 연결의 동작을 흉내 내 정보를 처리하는 소자)를 개발하고, 이를 하나의 시스템으로 연결하는 일을 연구한다.[^research] 정 교수는 2024년 9월 서울대학교에 조교수로 부임했으며, 첨단융합학부 차세대지능형반도체전공에 소속되어 있고 전기·정보공학부를 겸임한다.[^ece][^snuti]

첫째 축은 **센서에서 감지와 계산을 함께 하는 일**이다. 센서 내 연산(In-Sensor Computing)은 신호를 얻는 소자·회로에 저장과 계산 기능을 함께 넣는 방식이고, 메모리 내 연산(In-Memory Computing)은 데이터를 저장 장치와 계산 장치 사이로 옮기는 대신 저장 장치 안이나 가까이에서 계산하는 방식이다. 연구실은 가스·습도·압력·온도 센서에 히터(전기로 열을 내는 부품), 증폭기(입력 신호의 크기를 키우는 회로), 비휘발성 메모리(전원을 꺼도 정보가 남는 저장 장치)를 연결한다. 감지 신호가 시간에 따라 변하는 모습이나 전류의 흔들림도 가스를 구별하는 정보로 이용한다.[^insensor] 대표 논문 1은 자극에 따라 감도를 바꾸는 감각 적응을 인공 후각 시스템에 넣어, 배경 가스의 간섭을 걸러 새 가스를 식별하는 방법을 제시했다.[^p1]

둘째 축은 **감각 소자와 그 재료·공정을 다듬는 일**이다. 촉각 센서에서는 정적인 압력과 동적인 진동을 한 소자에서 감지하고, 신호를 읽는 회로와 같은 칩에 집적하는 구조를 연구한다. 집적은 여러 소자나 회로를 하나의 기판이나 칩에 함께 만드는 일이다.[^tactile] 산화물 반도체(산소와 다른 원소가 결합한 반도체 재료)를 쓰는 트랜지스터(전기 신호를 조절하거나 증폭하는 소자)에서는 재료의 조성, 제조 공정, 소자 구조를 바꾸고 결함이 전기적 특성과 장기 안정성에 미치는 영향을 분석한다.[^oxide]

셋째 축은 **정보를 저장하는 소자의 신뢰성과 계산 기능**이다. 강유전체(외부 전기장이 없어도 전기 분극이 남고 그 방향을 전기장으로 뒤집을 수 있는 물질)에서는 반복 동작과 장기 저장 중 정보가 손상되는 원인을 밝히고 재료와 구조를 조절한다. 전기 분극은 물질 안에서 양전하와 음전하의 중심이 서로 치우친 상태를 뜻한다.[^ferro] 또 저장용 축전기(전하를 모아 두는 부품)를 쓰지 않는 디램(Dynamic Random-Access Memory, DRAM, 저장한 정보를 주기적으로 갱신하는 휘발성 반도체 메모리)의 동작 방법과 소자를 입체적으로 쌓는 배열을 연구한다. 휘발성은 전원 공급이 끊어지면 저장 정보가 사라지는 성질이다.[^dram] 수직 낸드 플래시 메모리(Vertical NAND Flash Memory, V-NAND, 블록 단위로 지우고 다시 쓰는 비휘발성 반도체 메모리를 수직으로 쌓은 구조)에서는 쓰기·지우기에 따른 열화와 정보 유지 특성을 분석한다.[^vnand] 대표 논문 2는 강유전체 메모리의 제조 공정과 전류 흔들림의 관계를, 대표 논문 3–6은 플래시 메모리의 정보 유지·동작·내용 검색·신경망(연결된 계산 단위들의 신호 전달을 통해 입력과 출력의 관계를 학습하는 계산 모형) 보안을 다룬다.[^p2][^p3][^p4][^p5][^p6]

## 주요 연구 주제

### 가스·복합 감각 센서와 인공 후각

연구실은 전계효과 트랜지스터(Field-Effect Transistor, FET, 전기장으로 전류가 흐르는 통로를 조절하는 소자)를 이용한 가스·습도·압력·온도 센서를 개발한다. 상보형 금속 산화물 반도체(Complementary Metal-Oxide-Semiconductor, CMOS, 서로 보완되는 두 종류의 트랜지스터를 함께 쓰는 회로 기술) 공정과 호환되는 센서에 히터·증폭기·저장 소자를 연결해 한 칩에서 여러 종류의 자극을 감지하고 신호를 처리하는 것이 목표다. 인공 후각, 환경 감시, 식품 품질 평가, 헬스케어, 로봇을 응용 대상으로 든다.[^insensor] 대표 논문 1은 감지·신호 전달·판단 역할을 하는 인공 신경 소자를 연결하고, 제한된 환경에서 학습한 뒤 여러 환경의 가스를 식별하는 시스템을 보였다.[^p1] 대표 논문 8은 제작한 센서와 신경망용 소자·회로를 합친 플랫폼에서 정확도·면적·지연·에너지의 관계를 분석하고, 히터의 효율과 센서 수가 에너지 소비에 미치는 영향을 짚었다.[^p8]

### 촉각 센서와 산화물 트랜지스터

촉각 연구에서는 스칸듐·알루미늄 질화물(ScAlN)을 쓰는 미세 전자기계 시스템(Micro-Electro-Mechanical Systems, MEMS, 미세한 기계 구조와 전기적 기능을 결합한 장치)을 CMOS 회로와 같은 칩에 만드는 플랫폼을 다룬다. 압력과 진동을 함께 감지하는 이중 모드 소자와 구불구불한 연결 배선을 이용한 유연한 센서 배열을 연구한다.[^tactile] 산화물 소자에서는 비정질(원자 배열에 장거리의 반복 질서가 없는 상태) 산화물 반도체를 이용한 박막(재료를 얇은 층으로 만든 것) 트랜지스터(Thin-Film Transistor, TFT, 반도체 박막을 전류 통로로 쓰는 트랜지스터)의 조성·공정·구조를 연구한다. 산소 빈자리와 수소 관련 결함이 소자 특성에 미치는 영향을 분석하고, 전압을 계속 가했을 때 생기는 불안정성을 제어하는 것이 목표다.[^oxide]

### 강유전체 메모리와 신경망 연산 소자

강유전체 소자의 반복 동작 수명과 정보 유지 손실을 다루며, 전하가 갇히는 결함의 생성과 재료 경계의 열화, 분극이 감소하는 현상을 분석한다. 이 이해를 바탕으로 강유전체를 쓰는 낸드 메모리의 재료·구조를 최적화하고, 인공지능 계산에서 연결의 세기를 나타내는 가중치를 연속적으로 조절하는 소자를 개발한다.[^ferro] 대표 논문 2는 전극을 만드는 스퍼터링(입자로 고체 표면을 때려 방출한 원자를 기판에 쌓는 방법)의 조건이 강유전체 내부 결함과 전류의 무작위 흔들림에 미치는 영향을 분석했다.[^p2] 대표 논문 7은 강유전체 소자 배열에서 무작위 값을 뽑는 기능과 정해진 계산을 수행하는 기능을 함께 구현해 손글씨 숫자와 얼굴 이미지 생성에 이용했다.[^p7]

### 입체 메모리와 메모리 내 연산

디램에서는 축전기 없는 셀(정보를 저장하는 기본 단위)의 신뢰성 있는 동작과 입체 적층 배열을 연구한다.[^dram] 수직 낸드에서는 쓰기 뒤 전하 손실과 문턱 전압(트랜지스터의 전류 통로가 켜지는 기준 전압)의 분포 변화, 반복 쓰기·지우기로 생기는 재료 손상을 분석하고 동작 조건과 알고리즘을 조절한다.[^vnand] 대표 논문 3은 표준 CMOS 공정으로 만드는 내장형 플래시를 제안했고, 대표 논문 4는 수직 낸드에 저장된 내용을 입력과 병렬로 비교하는 검색 구조를 보였다. 대표 논문 5는 칩마다 다른 소자의 물리 특성을 신경망에 이용해 복제와 입력 데이터 복원 공격을 방어했다.[^p3][^p4][^p5]

## 대표 논문

2024년 9월 부임 이후 발표된 논문 중 가스 감지, 강유전체 신뢰성, 플래시 메모리와 연산을 다루는 논문을 골랐다. ‘쉽게 말하면’ 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문 | 쉽게 말하면 |
|---|---|---|---|
| 1 | 2026 | [Intelligent artificial olfactory nervous system with sensory adaptation capabilities](https://doi.org/10.1038/s41467-026-76918-1)[^p1] | 가스에 반응하는 인공 신경 소자의 감도를 자극에 맞춰 바꾸고, 배경 가스의 간섭을 걸러 내는 인공 후각 시스템이다. 제한된 환경에서 학습해도 여러 환경에서 새 가스를 식별할 수 있음을 보였다. |
| 2 | 2025 | [Physical correlation between stochasticity and process-induced damage in ferroelectric memory devices](https://doi.org/10.1186/s40580-025-00505-1)[^p2] | 강유전체 메모리의 윗전극을 만드는 공정 조건에 따라 결함과 전류의 무작위 흔들림이 어떻게 달라지는지 분석했다. 전류가 잘 흐르는 특성과 정보를 안정적으로 읽는 특성을 함께 고려해 공정 조건을 정하는 방법을 제시했다. |
| 3 | 2026 | [2-T Embedded Flash Memory using Standard 28 nm Logic CMOS Technology](https://doi.org/10.1109/LED.2026.3685316)[^p3] | 표준 CMOS 공정에 추가 제조 단계를 넣지 않고 트랜지스터 두 개로 구성한 내장형 플래시 메모리를 제안했다. 배열에서 원하는 셀을 골라 쓰고 지우는 동작을 보였다. |
| 4 | 2026 | [Triple-Level Content-Addressable Vertical NAND Flash Memory](https://doi.org/10.1002/advs.77390)[^p4] | 상용 수직 낸드 메모리의 여러 저장 상태를 이용해 저장 내용과 입력을 병렬로 비교한다. 홀수·짝수 제어선을 나누어 검색하는 방식으로 저장 밀도를 유지하며 검색을 수행했다. |
| 5 | 2026 | [Model-Inversion-Resistant Physical Unclonable Neural Network Using Vertical NAND Flash Memory](https://doi.org/10.1002/advs.74517)[^p5] | 물리적 복제 불가능 신경망(Physical Unclonable Neural Network, PUNN)을 수직 낸드에 구현했다. 칩마다 다른 전류 전달 특성을 이용하고 전방향 학습(Forward-Forward, FF)으로 훈련해, 모델 복제와 출력에서 입력을 복원하는 공격에 대한 방어를 보였다. |
| 6 | 2026 | [Retention improvement in vertical NAND flash memory using block soft erase scheme](https://doi.org/10.1063/5.0310928)[^p6] | 셀을 하나씩 조절하는 대신 블록 안 모든 셀에 한 번의 지우기 신호를 동시에 가해 저장 정보의 유지 특성을 개선하는 방법이다. 상용 수직 낸드 메모리에서 동작과 정보 유지 특성을 실험했다. |
| 7 | 2026 | [CMOS-compatible ferroelectric tunnel junctions integrate stochastic sampling and deterministic computing for image generation](https://doi.org/10.1038/s41467-026-72969-6)[^p7] | 강유전체 소자 배열 하나로 무작위 값을 뽑는 기능과 정해진 계산을 수행하는 기능을 함께 구현했다. 소자의 전압과 값을 읽는 시간을 조절해 손글씨 숫자와 얼굴 이미지를 생성하는 데 이용했다. |
| 8 | 2026 | [Analysis of Accuracy, Area, Latency, and Energy Consumption of Gas-sensing-based In-sensor Neuromorphic Computing](https://doi.org/10.1109/jsen.2026.3678607)[^p8] | 제작한 가스 센서·히터와 신경망용 저장 소자·처리 회로를 합친 플랫폼에서 정확도·회로 면적·응답 지연·에너지의 관계를 분석했다. 지연은 센서가 좌우하고 에너지는 주로 히터가 소비하므로, 센서 수와 히터 효율을 함께 고려해야 한다고 제시했다. |

## 교수와 전문 분야

정규원 교수는 서울대학교 전기·정보공학부에서 학사(2018)와 박사(2023)를 받았다. 2023년 3월부터 2024년 2월까지 서울대학교 반도체공동연구소 연수연구원, 2024년 3–8월 삼성전자 SAIT의 Staff Engineer로 일한 뒤 2024년 9월 서울대학교 조교수로 부임했다.[^ece][^snuti]

공식 교수 소개는 전문 분야를 반도체 재료와 소자로 적고, 차세대 컴퓨팅, 실리콘 로직·메모리·센서 집적 시스템, 피지컬 AI(현실의 물리 환경을 감지하고 그 안에서 행동하는 인공지능)를 위한 센서, 강유전체·디램·낸드 메모리를 연구 분야로 든다.[^ece] 최근 논문으로 보면 센서의 감지와 계산을 잇는 인공 감각 시스템, 제조 공정과 소자 신뢰성의 관계, 메모리 자체를 계산과 검색에 이용하는 하드웨어가 전문 분야다.[^p1][^p2][^p3][^p4][^p5]

## 응용 분야

연구실은 인공 후각과 환경 감시, 식품 품질 평가, 헬스케어·로봇용 지능형 센서를 목표로 한다.[^insensor] 실리콘 층에 계산 회로와 메모리를 만들고 그 위에 여러 자극을 감지하는 센서를 놓는 입체 집적 시스템을 연구하며, 기기 안에서 인공지능을 실행하는 온디바이스 AI(On-Device AI)를 자율주행차와 로봇에 적용하는 방향을 제시한다.[^research] 대표 논문은 가스 식별, 메모리 안의 내용 검색, 신경망의 복제·입력 복원 공격 방어를 다룬다.[^p1][^p4][^p5]

## 구성원

2026년 10월 26일 관측한 Graduate Students 페이지의 11명이다. 과정·시작 연도·연구 주제·학교 이메일은 랩의 게시 표기를 따른다. ‘대표 논문 참여’는 위 논문 표의 번호이며 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^students]

| 이름 | 과정 | 시작 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|---|
| Wooseong Roh | 석박사통합과정 | 2025~ | Sensor/Memory/Thin film transistor | danielroh@snu.ac.kr |  |
| Jeseung Jeong | 석박사통합과정 | 2025~ | Neuromorphic system/Processing in Memory/CMOS analog circuit | jeongjs@snu.ac.kr | 3, 8 |
| Minsun Kim | 석박사통합과정 | 2025~ | Thin film transistor/Oxide Semiconductor | msunny@snu.ac.kr |  |
| Dongbeen Shin | 석박사통합과정 | 2025~ | Neuromorphic system/Processing in Memory/NAND | tomato96923@snu.ac.kr | 4, 5, 6 |
| Jisu Jang | 석박사통합과정 | 2025~ | Ferroelectrics/Non-volatile Memory/Interfaces | jisu0101j@snu.ac.kr |  |
| Siwon Jang | 석박사통합과정 | 2025~ | Tactile Sensor | jk677@snu.ac.kr |  |
| Cheoljin Park | 석박사통합과정 | 2026~ | Gas Sensor Systems / Memory Architectures / 3D Integration | pcj1317@snu.ac.kr |  |
| Seojoon Lee | 석박사통합과정 | 2026~ | Oxide Semiconductor / Ferroelectrics / Sensor | lsj0930@snu.ac.kr |  |
| Dawon Yang | 석박사통합과정 | 2026~ | DRAM/3D Integration/Processing in Memory/Compact Model | dawon.yang@snu.ac.kr |  |
| Anis Nadirah Binti Suaidi | 석사과정 (Samsung Global Scholarship Recipient) | 2025~ | Sensor/Memory/Circuit | anisuaidi@snu.ac.kr |  |
| Jaeyoung Choi | 석박사통합과정 | 2026~ | Computing in Memory / Hardware Aware Machine Learning / CMOS Circuit Design | jychoi42@snu.ac.kr |  |

## 최근 논문 목록 (2021–2026)

학술지 66편, 국제학회 15편, 국내학회 10편이다. 정규원 교수의 개인 연구 이력이 함께 게시된 목록으로, 2024년 9월 조교수 부임 전 항목이 섞여 있다. 연도는 각 항목에 적힌 발표 연월을 따른다. 저자와 제목, 학술지·학회 이름은 랩 게시 표기이며 뜻이 명시된 공동 저자 기호의 설명도 함께 남겼다.[^journals][^conferences]

**2026**

- H. Shin, J. Park, D. Kim, K. Choi, J. Hwang, M.-K. Park, G. Jung, and J.H. Lee. "Low-Frequency Noise Analysis in Sensor-Circuit Integrated Computing System for Selective Gas Detection". *IEEE Sens. J., 2026.09*.
- J. Park, H. Shin, D. Kim, K. Choi, W. Roh, J. Hwang, M.-K. Park, G. Jung, and J.H Lee. "Accurate temperature extraction of embedded polysilicon micro-heaters". *Sens. Actuators B Chem., 2026.09*.
- S.H. Park, J. Im, Y. Yang, R.H. Koo, J. Ko, M. Oh, D. Shin, G. Jung, J.H. Lee. "Triple‐Level Content‐Addressable Vertical NAND Flash Memory". *Adv. Sci., 2026.08*.
- G. Jung, J. Kim, K. Choi, H. Shin, D. Kwon, W. Shin, J. Park, D. Kim, J. Kim, R.H. Koo, W.Y. Choi, J.H.Lee. "Intelligent artificial olfactory nervous system with sensory adaptation capabilities". *Nat. Commun., 2026.08*.
- R.H. Koo, J. Ko, W. Shin, S. Ryu, J. Im, S.H. Park, J. Hwang, M. Song, Y. Cho, J. Kim, G. Jung, D. Kwon, and J.H Lee. "CMOS-compatible ferroelectric tunnel junctions integrate stochastic sampling and deterministic computing for image generation". *Nat. Commun., 2026.05*.
- J. Ko, J. Jeong, J. Im, J. Im, K. M. Lee, K. Choi, G. Jung†, and J.H Lee†. "2-T Embedded Flash Memory using Standard 28 nm Logic CMOS Technology". *IEEE Electron Device Lett., 2026.04, †co-coresponding authors*.
- J. Ko, K. Choi, J. Im, D. Kim, H. Shi n, R.-H. Koo, S.-H. Park, J. Jeong, G. Jung†, and J.H Lee†. "Analysis of Accuracy, Area, Latency, and Energy Consumption of Gas-sensing-based In-sensor Neuromorphic Computing". *IEEE Sens. J., 2026.04, †co-coresponding authors*.
- S.-H. Park‡, D. Shin‡, M. Oh‡, Y. Yang, G. Jung†, and J.H Lee†. "Retention improvement in vertical NAND flash memory using block soft erase scheme". *Appl. Phys. Lett., 2026.04, †co-coresponding authors*.
- S.H. Park, R.H. Koo, J. Ko, J. Im, Y. Yang, M. Oh, D. Shin, G. Jung, J.H. Lee. "Model-Inversion-Resistant Physical Unclonable Neural Network Using Vertical NAND Flash Memory". *Adv. Sci., 2026.02*.
- J. Ko, H. Shin, J. Park, J. Im, D. Kim, K. Choi, R.H. Koo, S.H. Park, W. Shin, G. Jung†, and J.H Lee†. "Low-power NO2 Gas Alarm Platform Using In-memory Latched Comparator". *Sens. Actuators B Chem., 2026.02, †co-coresponding authors*.
- R.H. Koo, J. Im, J. Hwang, S.H. Park, J. Ko, K. Choi, S. Ryu, G. Jung, J.H. Lee. "Noise Fingerprints as a Quantitative Order Parameter for Polarization‐and Defect‐Mediated Switching in Hafnia Ferroelectrics". *Adv. Sci., 2026.02*.
- H. Shin, J. Park, D. Kim, J. Hwang, J. Song, M.K. Park, H. Jang, G. Jung, and J.H Lee. "Design Optimization of Embedded Micro-heater for Reliable Gas Sensing and On-chip Annealing". *Sens. Actuators B Chem., 2026.02*.
- C. Lee, Y. Jeong, R-H. Koo, Y. Choi, K. Choi, G. Jung, J. Kim, S. Hong, J. Im, S-T. Lee, J. Kim, D. Radermacher, W. Shin, and J.H Lee. "Low-frequency noise in CMOS-integrated gas sensors: from a reliability constraint to a selective sensing feature". *Sens. Actuators B Chem., 2026.01*.
- W. Roh, H. Shin, J. Ko, K. Choi, D. Kim, M. Kim, J. Lee, G. Jung. "CMOS-Compatible Gas Source Distance Estimation System using FET-Type Gas Sensors". *IEEE International Symposium on Olfaction and Electronic Nose (ISOEN) , 2026.05*.
- J. Choi and G. Jung\*. "Hebbian-Learning-Based Method for On-Chip Training on NVM Crossbar Hardware". *Korean Conference on Semiconductors (KCS), 2026.01*.
- D. Shin, S.-H. Park, M. Oh, J.H. Lee, and G. Jung\*. "Optimization of Programming Pulse Duration for Energy-Efficient Program Operation in Vertical NAND Flash Memory". *Korean Conference on Semiconductors (KCS), 2026.01*.
- W. Roh, H. Shin, J. Ko, J. Jeong, J.H. Lee, and G. Jung\*. "On-Chip Gas Leak Source Estimation Using Filament Events". *Korean Conference on Semiconductors (KCS), 2026.01*.
- J. Jeong, J. Ko, W. Roh, J.H. Lee, and G. Jung\*. "Fully CMOS-Compatible Analog Content-Addressable Memory Using Single-Poly Embedded Flash Memory". *Korean Conference on Semiconductors (KCS), 2026.01*.
- S. Jang, H. Shin, J.H. Lee, and G. Jung\*. "Microheater‑Centric Design Optimization of TFT‑Type Gas Sensors". *Korean Conference on Semiconduc tors (KCS), 2026.01*.
- M. Kim, D. Kim, S. Kim, J.H. Lee, and G. Jung\*. "Contact Engineering in In₂O₃ Thin Film Transistors Guided by Contact-Dominated Low Frequency Measurement". *Korean Conference on Semiconductors (KCS), 2026.01*.
- J. Jang, R.-H. Koo, J.H. Lee, and G. Jung\*. "Position Effects of HfO2 Interlayers in Ferroelectric Tunnel Junctions". *Korean Conference on Semiconductors (KCS), 2026.01*.
- C. Park, J. Kim, J.H. Lee, and G. Jung\*. "Mixed-Gas Identification Using Silicon FET–Based Gas Sensors and Machine Learning". *Korean Conference on Semiconductors (KCS), 2026.01*.

**2025**

- R-H. Koo, W. Shin, J. Im, S. Ryu, S. Kim, J. Kim, K. Choi, S-H. Park, K. Choi, J. Ko, J. Ji, M. Oh, G. Jung, S-T. Lee, D. Kwon, D. Kwon, and J.H Lee. "A universal re-annealing method for enhancing endurance in hafnia ferroelectric memories: Insights from stochastic noise analysis". *Chaos Solit. Fractals, 2025.10*.
- R-H. Koo, W. Shin, J. Im, S. Kim, S. Ryu, G. Jung, J. Kim, S-H. Park, K. Choi, J. Ko, S-T. Lee, D. Kwon, D. Kwon, and J.H Lee. "Interface percolation and random trap generation in ferroelectric memory: A two-step degradation mechanism explored through low-frequency noise spectroscopy". *Chaos Solit. Fractals, 2025.10*.
- S-H. Park, J. Im, J. Ko, J. Hwang, Y. Yang, J.-W. Back, R-H. Koo, I.-S. Lee, D. Shin, M. Oh, G. Jung, and J.H Lee. "Dynamic pass bias control for temperature-resilient neural networks using vertical NAND flash memory". *Nano Converg., 2025.09*.
- R-H. Koo, S. Kim, J. Im, S. Ryu, K. Choi, S-H. Park, J. Ko, J. Ji, M. Oh, J. Kim, G. Jung, S-T. Lee, D. Kwon, W. Shin, and J.H Lee. "Physical correlation between stochasticity and process-induced damage in ferroelectric memory devices". *Nano Converg., 2025.08*.
- K. Choi, R-H. Koo, J. Park, D. Kim, J. Kim, H. Shin, G. Jung†, and J.H Lee†. "Novel Gas Sensor Signal Acquisition Method: Amplifying Sensor Signals and Enabling Efficient Gas Identification". *Adv. Sci., 2025.04, †co-coresponding authors*.
- H. Shin, J. Park, D. Kim, K. Choi, M.K. Park, J. Hwang, S. Lee, Y.C. Joo, G. Jung†, and J.H Lee†. "Optimization of Co-sputtered Zinc Indium Tin Oxide-based MOSFET-type Sensor for Effective NO2 Gas Detection". *Sens. Actuators B Chem., 2025.01, †co-coresponding authors*.
- H. Shin, J. Park, D. Kim, K. Ch oi, Joon Hwang, M.-K. Park, G. Jung, and J.H. Lee. "Innovative Mixed Gas Discrimination System Using Integrated Self-Cancellation Circuit". *IEEE International Electron Devices Meeting (IEDM), 2025.12*.

**2024**

- R. H. Koo, W. Shin, G. Jung, J. Kim, S. T. Lee, J. Im, S. H. Park, J. Ko, D. Kwon, J.-H. Lee. "Strain–Stress Impact on Ferroelectric Devices: A Multilayer Analysis and Optimization Strategy for Neural Networks". *ACS Mater. Lett. 2024.10*.
- G. Jung‡, K. Choi‡, S. Ju‡, J. Kim, W. Shin, S. Lee, G. Yeom, R. H. Koo, Y. C. Joo, W. Y. Choi, S. W. Han, J.-H. Lee. "Chemisorption Manipulation by Adjusting the Carrier Concentration of the Adsorbent and Its Application to Adsorbate Identification". *ACS Mater. Lett. 2024.09*.
- R. H. Koo, W. Shin, J. Kim, J. Yim, J. Ko, G. Jung, J. Im, S. H. Park, J.J. Kim, S. S. Cheema, D. K. Kwon, J. -H. Lee. "Polarization Pruning: Reliability Enhancement of Hafnia‐Based Ferroelectric Devices for Memory and Neuromorphic Computing". *Adv. Sci. 2024.09*.
- J. Kim, J. Im, S. Oh, W. Shin, G. Jung, S. T. Lee, J.-H. Lee. "Vertical AND-Type Flash Synaptic Cell Stack for High-Density and Reliable Binary Neural Networks". *IEEE Electron Device Lett. 2024.07*.
- R-H. Koo, W. Shin, G. Jung, D. Kwon, J. J. Kim, D. Kwon, J.-H. Lee. "Stochasticity in Ferroelectric Memory Devices with Different Bottom Electrode Crystallinity". *Chaos Solit. Fractals. 2024.06*.
- K. Choi, G. Jung, W. Shin, J. Park, C. Lee, D. Kim. H. Shin, W. Y. Choi, J.-H. Lee. "NO2 gas response improvement method by adopting oxygen vacancy, controlled In2O3 double sensing layers". *Solid State Electron., 2024.06*.
- J. Kim, J. Im, W. Shin, S. Lee, S. Oh, D. Kwon, G. Jung, W. Y. Choi, J.-H. Lee. "Demonstration of In-Memory Biosignal Analysis: Novel High-Density and Low-Power 3D Flash Memory Array for Arrhythmia Detection". *Adv. Sci., 2024.05*.
- J. Park, H. Shin, G. Jung, S. Hong, M.-K. Park, J. Hwang, J.-H. Bae, J.-J. Kim, J.-H. Lee. "On‐Chip Annealing Using Embedded Micro‐Heater for Highly Sensitive and Selective Gas Detection". *Adv. Sci., 2024.05*.
- R-H. Koo, W. Shin, S. Kim, G. Jung, S.-T. Lee, J. J. Kim, D. Kwon, J.-H. Lee. "Examination of Ferroelectric Domain Dynamics in HZO under Endurance Cycling Stress". *IEEE Electron Device Lett., 2024.04*.
- J. Park, G. Jung, W. Shin, D. Kim, K. Choi, H. Shin, M.K. Park, J.J. Kim, J.H. Lee. "Reliability of FET-type gas sensor with asymmetric air-gap micro-heater structure considering thermoelectric effect". *Sens. Actuators B Chem. 2024.04*.
- W. Shin, R.H. Koo, S. Hong, Y. Jeong, G. Jung, S.T. Lee, J.H. Lee. "Proposition of optimal self-curing method in horizontal-floating gate FET-type gas sensors for reliability improvement". *Sens. Actuators B Chem. 2024.04*.
- C. Lee, W. Shin, G. Jung, J. Park, D. Kim, H. Shin, J.J. Kim, and J.H Lee. "CMOS-Compatible Barometric Pressure Field-Effect Transistor-type Sensor". *IEEE Electron Device Lett., 2024.03*.
- Y. Hong‡, G. Jung‡, and J.H Lee. "Improved Performance of FET-type Humidity Sensor with Low-power Embedded Micro-heater". *IEEE Electron Device Lett., 2024.03, ‡co-first authors*.
- G. Jung, H. Kim, C. Lee, J. Kim, W.Y. Choi, and J.H. Lee. "Intelligent Multimodal Sensors Integrating Gas, Barometric Pressure, and Temperature Sensing". *IEEE International Electron Devices Meeting (IEDM), 2024.12*.

**2023**

- W. Shin, R.H. Koo, S. Hong, G. Jung, Y. Jeong, S.T. Lee, and J.H. Lee. "Effects of Sensor Platform Scaling on Signal-to-Noise Ratio in the Resistor-and Horizontal Floating-Gate FET-Type Gas Sensors". *IEEE Trans. Electron Devices, 2023.09*.
- G. Jung, J. Kim, S. Hong, H. Shin, Y. Jeong, W. Shin, D. Kwon, W.Y. Choi, and J.H. Lee. "Energy efficient artificial olfactory system with integrated sensing and computing capabilities for food spoilage detection". *Adv. Sci., 2023.08*.
- G. Jung, S. Ju, K. Choi, J. Kim, S. Hong, J. Park, W. Shin, Y. Jeong, S. Han, W.Y. Choi, and J.H. Lee. "Reconfigurable Manipulation of Oxygen Content on Metal Oxide Surfaces and Applications to Gas Sensing". *ACS NANO, 2023.08*.
- W. Shin, R.H. Koo, S. Hong, Y. Jeong, G. Jung, S.T. Lee, and J.H. Lee. "Annealing Ambient and Film Thickness Dependent NO Response and 1/f Noise Characteristics of IGZO Resistor-Type Gas Sensors". *IEEE Trans. Electron Devices, 2023.08*.
- J. Kim, W. Shin, S. Hong, Y. Jeong, G. Jung, W.Y. Choi, J.J. Kim, B.G. Park, and J.H. Lee. "A novel pathway to construct gas concentration prediction model in real-world applications: data augmentation; fast prediction; and interpolation and extrapolation". *Sens. Actuators B Chem., 2023.05*.
- G. Jung‡, H. Shin‡, S.W. Jeon, Y.H. Lim, S. Hong, D.H. Kim, and J.H. Lee. "Transducer-aware hydroxy-rich-surface indium oxide gas sensor for low-power and high-sensitivity NO2 gas sensing". *ACS Appl. Mater., 2023.04 ‡co-first authors*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, K. Choi, H. Shin, R.H. Koo, J.J. Kim, and J.H. Lee. "Low-frequency noise in gas sensors: A review". *Sens. Actuators B Chem., 2023.05*.
- W. Shin, J. Kim, G. Jung, S. Ju, S.H. Park, Y. Jeong, S. Hong, R.H. Koo, Y. Yang, J.J. Kim, S. Han, and J.H. Lee. "In‐Memory‐Computed Low‐Frequency Noise Spectroscopy for Selective Gas Detection Using a Reducible Metal Oxide". *Adv. Sci., 2023.02*.
- W. Shin, Y. Jeong, M. Kim, J. Lee, R.H. Koo, S. Hong, G. Jung, J.J. Kim, and J.H. Lee. "Recovery of off-state stress-induced damage in FET-type gas sensor using self-curing method". *Discover Nano, 2023.02*.
- S. Hong, Y. Jeong, G. Jung, W. Shin, J. Park, D. Kim, C. Lee, and J.H. Lee. "Macroscopic analysis and design of Si HFGFET gas sensor for sensitive gas detection". *Solid State Electron., 2023.02*.
- J. Park, S. Hong, Y. Jeong, G. Jung, W. Shin, D. Kim, C. Lee, and J.H. Lee. "H2S Gas Sensing Properties in Polysilicon Control-Gate FET-type Gas Sensor". *Solid State Electron., 2023.02*.
- G. Jung, J. Kim. Y. Jeong, J. Park, W. Shin, W.Y. Choi, and J.H. Lee. "New Gas Identification Method Using Gas Sensor-Amplifier Merged Array and In-Memory Computing-Based Preprocessing". *IEEE International Electron Devices Meeting (IEDM), 2023.12*.
- G. Jung, K. Choi, W. Shin, J. Park, D. Kim, J. Kim, H. Shin, C. Lee, W.Y. Choi, and J.H. Lee. "High-sensitivity, low-power FET-type NO2 gas sensor using electron concentration control of gas-sensing material". *International Conference on Solid State Devices and Materials (SSDM), 2023.09*.
- C. Lee, G. Jung, W. Shin, Y. Jeong, J. Park, D. Kim, J.J. Kim, and J.H. Lee. "Temperature Measurement Method Using FET Type Gas Sensor". *IEEE Electron Devices Technology & Manufacturing Conference (EDTM), 2023.03*.

**2022**

- Y. Jeong, S. Hong, G. Jung, W. Shin, C. Lee, J. Park, D. Kim, and J.H. Lee. "Effects of oxygen gas in the sputtering process of the WO3 sensing layer on NO2 sensing characteristics of the FET-type gas sensor". *Solid State Electron., 2022.12*.
- G. Jung‡, S. Hong‡, W. Shin, Y. Jeong, J. Park, D. Kim, and J.H. Lee. "Design optimization of FET-type gas sensor considering device characteristics, sensitivity, power, noise, and SNR". *Sens. Actuators B Chem., 2022.10 ‡co-first authors*.
- J. Park, G. Jung, S. Hong, Y. Jeong, W. Shin, D. Kim, C. Lee, and J.H. Lee. "Analysis of Cr/Au contact reliability in embedded poly-Si micro-heater for FET-type gas sensor". *Sens. Actuators B Chem., 2022.06*.
- W. Shin, Y. Jeong, S. Hong, G. Jung, J. Park, D. Kim, B.G. Park, and J.H. Lee. "Fully Integrated FET-type Gas Sensor with optimized Signal-to-Noise Ratio for H2S gas detection". *Sens. Actuators B Chem., 2022.05*.
- G. Jung, S. Hong, Y. Jeong, W. Shin, J. Park, D. Kim, and J.H. Lee. "Highly Selective and Low-Power Carbon Monoxide Gas Sensor Based on the Chain Reaction of Oxygen and Carbon Monoxide to WO3". *ACS Appl. Mater., 2022.04*.
- W. Shin, J. Yim, J.H. Bae, J.K. Lee, S. Hong, J. Kim, Y. Jeong, D. Kwon, R.H. Koo G. Jung, C. Han, J. Kim, B.G. Park, D. Kwon, and J.H. Lee. "Synergistic improvement of sensing performance in ferroelectric transistor gas sensors using remnant polarization". *Mater. Horiz., 2022.04*.
- W. Shin‡, G. Jung‡, S. Hong, Y. Jeong, J. Park, D. Kim, B.G. Park, and J.H. Lee. "Optimization of channel structure and bias condition for signal-to-noise ratio improvement in Si-based FET-type gas sensor with horizontal floating-gate". *Sens. Actuators B Chem., 2022.04 ‡co-first authors*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, B.G. Park, and J.H. Lee. "Effects of Postdeposition Annealing Ambience on NO2 Gas Sensing Performance in Si-Based FET-Type Gas Sensor". *IEEE Trans Electron Devices., 2022.03*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, B.G. Park, and J.H. Lee. "Effects of Channel Length Scaling on the Signal-to-Noise Ratio in FET-Type Gas Sensor with Horizontal Floating-Gate". *IEEE Electron Device Lett., 2022.03*.
- D. Kim, W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, J.H. Lee. "Effects of Electrode Structure on H2S Sensing and Low-Frequency Noise Characteristics in In2O3-Based Resistor-Type Gas Sensors". *IEEE Sens. J., 2022.02*.
- G. Jung, J. Kim, W. Shin, S. Hong, Y. Jeo ng, C. Lee, W.Y. Choi, and J.H. Lee. "Innovative Gas Sensing Method Using Transient Behavior of FET-type Sensors with Gate Pulse Input". *IEEE International Electron Devices Meeting (IEDM), 2022.12*.
- G. Jung, W. Shin, H. Shin, S. Hong, Y. Jeong, K. Choi, J. Park, D. Kim, C. Lee, J. Kim, W.Y. Choi, and J.H. Lee. "Comparison of the H2S gas response characteristics of semiconductor gas sensors (HFGFET-, TFT-, and resistor-type) fabricated on the same wafer". *International Conference on Solid State Devices and Materials (SSDM), 2022.09*.
- Y. Jeong, S. Hong, G. Jung, W. Shin, W.Y. Choi, and J.H. Lee. "H2S Sensing Characteristics of the Amplifier Circuit Consisting of pFET-type and Resistor-type Gas Sensors". *International Conference on Solid State Devices and Materials (SSDM), 2022.09*.
- G. Jung‡, J. Kim‡, W. Shin, S. Hong, Y. Jeong, J. Park, D. Kim, K. Choi, and J.H. Lee. "Optimal Bias Conditions for FET-type Gas Sensors to Minimize Current Fluctuations". *IEEE International Symposium on Olfaction and Electronic Nose (ISOEN), 2022.05 ‡co-first authors*.
- K. Choi, G. Jung, S. Hong, Y. Jeong, W. Shin, J. Park, C. Lee, D. Kim, and J.H. Lee. "Response Analysis of Resistor-type Gas Sensor with Bias Voltage Condition". *IEEE International Symposium on Olfaction and Electronic Nose (ISOEN), 2022.05*.
- H. Shin, G. Jung, S. Hong, Y. Jeong, W. Shin, J. Park, D. Kim, K. Choi, B.G. Park, J.J. Kim, and J.H. Lee. "Investigation of H2S Gas Response in Resistor- and FET-type Gas Sensors". *IEIE Summer Conference, 2022.06*.

**2021**

- W. Shin, D. Kwon, M. Ryu, J. Kwon, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, and J.H. Lee. "Effects of IGZO film thickness on H2S gas sensing performance: Response, excessive recovery, low-frequency noise, and signal-to-noise ratio". *Sens. Actuators B Chem., 2021.10*.
- D. Kwon‡, G. Jung‡, W. Shin, Y. Jeong, S. Hong, S. Oh, J. Kim, J.H. Bae, B.G. Park, and J.H. Lee. "Efficient fusion of spiking neural networks and FET-type gas sensors for a fast and reliable artificial olfactory system". *Sens. Actuators B Chem., 2021.10 ‡co-first authors*.
- Y. Jeong, S. Hong, G. Jung, W. Shin, J. Park, D. Kim, Y.S. Choi, J.H. Bae, B. H. Hong, and J.H. Lee. "Highly stable Si MOSFET-type humidity sensor with ink-jet printed graphene quantum dots sensing layer". *Sens. Actuators B Chem., 2021.09*.
- D. Kwon‡, G. Jung‡, W. Shin, Y. Jeong, S. Hong, S. Oh, J.H. Bae, B.G. Park, and J.H. Lee. "Low-power and reliable gas sensing system based on recurrent neural networks". *Sens. Actuators B Chem., 2021.08 ‡co-first authors*.
- H. Wang, J. Ma, J. Zhang, Y. Feng, M. T. Vijjapu, S. Yuvaraja, S. G. Surya, K. N. Salama, C. Dong, Y. Wang, Q. Kuang, Z. P. Tshabalala, D. E. Motaung, X. Liu, J. Yang, H. Fu, X. Yang, X. An, S. Zhou, B. Zi, Q. Liu, M. Urso, B. Zhang, A. A. Akande, A. K. Prasad, C. M. Hung, N. Van Duy, N. D. Hoa, K. Wu, C.Zhang, R. Kumar, M. Kumar, Y. Kim, J. Wu, Z. Wu, X. Yang, S. A. Vanalakar, J. Luo, H. Kan, M. Li, H. W. Jang, M. O. Orlandi, A. Mirzaei, H. W. Kim, S. S. Kim, A. S. M. I. Uddin, J. Wang, Y. Xia, C. Wongchoosuk, A. Nag, S. Mukhopadhyay, N. Saxena, P. Kumar, J. S. Do, J. H. Lee, S. Hong, Y. Jeong, G. Jung, W. Shin, J. Park, M. Bruzzi, and C. Zhu. "Gas sensing materials roadmap". *J. Phys. Condens., 2021.07*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, B.G. Park, and J.H. Lee. "Optimization of post-deposition annealing temperature for improved signal-to-noise ratio in In2O3 gas sensor". *Semicond. Sci. Technol., 2021.07*.
- G. Jung, S. Hong, Y. Jeong, W. Shin, J. Park, D. Kim, J.H. Bae, B.G. Park, and J.H. Lee. "Response Comparison of Resistor-and Si FET-Type Gas Sensors on the Same Substrate". *IEEE Trans Electron Devices, 2021.06*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, C. Lee, B.G. Park, and J.H. Lee. "Effect of charge storage engineering on the NO2 gas sensing properties of a WO 3 FET-type gas sensor with a horizontal floating-gate". *Nanoscale, 2021.05*.
- G Jung, Y Hong, S Hong, D Jang, Y Jeong, W Shin, J Park, D Kim, C.B. Jeong, D.U. Kim, K.S. Chang, and J.H. Lee. "A low-power embedded poly-Si micro-heater for gas sensor platform based on a FET transducer and its application for NO2 sensing". *Sens. Actuators B Chem., 2021.05*.
- G. Jung‡, W. Shin‡, S. Hong, Y. Jeong, J. Park, D. Kim, J.H. Bae, B.G. Park, and J.H. Lee. "Comparison of the characteristics of semiconductor gas sensors with different transducers fabricated on the same substrate". *Sens. Actuators B Chem., 2021.05 ‡co-first authors*.
- S. Hong, M. Wu, Y. Hong, Y. Jeong, G. Jung, W. Shin, J. Park, D. Kim, D. Jang, and J.H. Lee. "FET-type gas sensors: A review". *Sens. Actuators B Chem., 2021.03*.
- W. Shin, S. Hong, G. Jung, Y. Jeong, J. Park, D. Kim, D. Jang, B.G. Park, and J.H. Lee. "Improved signal-to-noise-ratio of FET-type gas sensors using body bias control and embedded micro-heater". *Sens. Actuators B Chem., 2021.02*.
- D. Jang, G. Jung, Y. Jeong, S. Hong, and J. H. Lee. "Barometric pressure sensor with air pocket integrated with MOSFETs on the same substrate". *J. Semicond. Technol. Sci., 2021.02*.
- S. Hong, Y. Jeong, G. Jung, W. Shin, J. Park, D. Kim, C. Lee, and J.H Lee. "Gas Sensing Performance of a Gated Lateral pnp-Bipolar Junction Transistor Gas Sensor Having a Horizontal Floating-Gate Structure". *International Conference on Solid State Devices and Materials (SSDM), 2021.09*.
- W. Shin, B. Choi, J. Lee, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, C. Lee, an d J.H. Lee. "Sub-ppm Detection of NO2 Gas using IGZO TFT-type Gas Sensor with Optimal Signal-to-Noise Ratio". *International Conference on Solid State Devices and Materials (SSDM), 2021.09*.
- Y. Jeong, W. Shin, S. Hong, G. Jung, C. Lee, J. Park, D. Kim, and J.H. Lee. "Amplifier Circuit Consisting of the FET-type Gas Sensors with Tunable FET Load". *International Conference on Solid State Devices and Materials (SSDM), 2021.09*.
- W. Shin, S. Hong, Y. Jeong, G. Jung, J. Park, D. Kim, C. Lee, and J.H. Lee. "Effects of Oxygen Flow Rate on the NO 2 Gas Sensing and Low-frequency Noise Ch aracteristics in IGZO Gas Sensors". *International Nanotech Symposium & Exhibition, 2021.07*.
- D. Kim, J. Im, S. Hong, Y. Jeong, G. Jung, W. Shin, J. Park, and J.H. Lee. "A Spiking Neural Network for Time-Efficient Gas Concentration Level Estimation in Resistor-Type Gas Sensors". *IEIE Summer Conference, 2021.06*.

## 특허

2021년 10월 22일부터 2026년 10월 22일 사이 등록 날짜가 적힌 특허 2건이다. 등록 번호와 발명자는 랩 게시 표기다.[^patents]

- 2026-01-20 · 금속 산화물의 산소 농도 재구성 방법 및 상기 방법을 이용한 가스 센서의 구동 방법 (등록번호 10-2916902; 발명자 J.H. Lee, G. Jung; 국가 대한민국)
- 2025-03-17 · 마이크로 히터를 갖는 가스 센서 (등록번호 10-2784778; 발명자 J.H. Lee, J. Park, G. Jung; 국가 대한민국)

## 수상과 펠로십

정규원 교수의 개인 목록에 적힌 2023년 수상·펠로십으로, 모두 2024년 9월 조교수 부임 전 항목이다.[^prof][^snuti]

- 2023 · 한국센서학회 이종흔상
- 2023 · 서울대학교 반도체공동연구소 도연논문상
- 2023 · Brain Korea21 Plus Postdoctoral Fellowship

## 소식

첫 화면의 NEWS & HIGHLIGHTS에 날짜가 적힌 4건이다.[^home]

- 2024-12-08 · 정규원·이종호 연구팀 AI 센서, IEEE 국제전자소자학회(IEDM)의 기술 하이라이트 선정
- 2025 상반기 · 전기·정보공학부 소식지 ECE LIFE에 정규원 신임교수 소개
- 2025-08-20 · 정보통신기획평가원 주간기술동향에 「Edge AI를 위한 지능형 센서」 기고
- 2026-08 · 전자공학회 기고글 게시

## 연락과 위치

- 교수 이메일: gwjung@snu.ac.kr, g.jung@snu.ac.kr[^contact]
- 전화: 02-880-8832[^contact]
- 위치: 서울특별시 관악구 관악로 1 서울대학교 첨단융합학부 18동 404호, 공과대학 전기·정보공학부 301동 1052호[^contact]

## 각주
[^research]: SDLA, Research, 연구 목표·Devices for AI·Artificial Sensory System·Integration for On-Device AI. <https://sdla.snu.ac.kr/research> 관측 2026-10-26.
[^insensor]: SDLA, In-Sensor Computing. 센서·메모리·계산 기능을 소자·회로 수준에서 합치며 CMOS 호환 가스·습도·압력·온도 센서와 비휘발성 메모리 배열을 개발한다고 설명한다. <https://sdla.snu.ac.kr/research/in-sensor-computing> 관측 2026-10-26.
[^tactile]: SDLA, Tactile Sensors. ScAlN 기반 CMOS-MEMS 플랫폼에서 압력과 진동을 동시에 감지하는 소자와 센서 배열 집적을 연구한다고 설명한다. <https://sdla.snu.ac.kr/research/tactile-sensors> 관측 2026-10-26.
[^ferro]: SDLA, Ferroelectric Devices. 강유전체 소자의 열화 원인, 메모리용 재료·구조, 신경망 가중치를 조절하는 소자와 배열을 연구·개발한다고 설명한다. <https://sdla.snu.ac.kr/research/ferroelectric-devices> 관측 2026-10-26.
[^oxide]: SDLA, Oxide Semiconductors. 비정질 산화물 반도체의 조성·공정·소자 구조를 연구하고 결함과 전기적 안정성을 분석한다고 설명한다. <https://sdla.snu.ac.kr/research/oxide-semiconductors> 관측 2026-10-26.
[^dram]: SDLA, 3D DRAM. 축전기 없는 디램 셀의 동작 방법과 입체 적층 배열을 연구한다고 설명한다. <https://sdla.snu.ac.kr/research/3d-dram> 관측 2026-10-26.
[^vnand]: SDLA, V-NAND. 정보 유지 특성과 반복 쓰기·지우기로 생기는 열화를 분석하고 동작 조건을 최적화한다고 설명한다. <https://sdla.snu.ac.kr/research/v-nand> 관측 2026-10-26.
[^ece]: 서울대학교 전기·정보공학부, 정규원 조교수 소개. 소속·직위·학력·경력·연구 분야. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p905> 관측 2026-10-26.
[^snuti]: 서울대학교 첨단융합학부, 차세대지능형반도체전공 정규원 조교수 소개. 소속·직위·부임 연월·이전 경력·수상. <https://snuti.snu.ac.kr/snu__professor/%ec%a0%95%ea%b7%9c%ec%9b%90/> 관측 2026-10-26.
[^prof]: SDLA, Professor. 학력·경력·수상·Scholarship & Fellowship. <https://sdla.snu.ac.kr/people/professor> 관측 2026-10-26.
[^students]: SDLA, Graduate Students. 게시 구성원 11명의 과정·시작 연도·연구 주제·학교 이메일. <https://sdla.snu.ac.kr/people/graduates-students> 관측 2026-10-26.
[^journals]: SDLA, Journal. 항목별 발표 연월과 저자·제목·학술지 및 기호 표기. <https://sdla.snu.ac.kr/publication/journal> 관측 2026-10-26.
[^conferences]: SDLA, Conference, International Conference·Domestic Conference. 항목별 발표 연월과 저자·제목·학회. <https://sdla.snu.ac.kr/publication/conference> 관측 2026-10-26.
[^patents]: SDLA, Patent. 등록 번호 10-2916902(2026-01-20), 10-2784778(2025-03-17). <https://sdla.snu.ac.kr/publication/patent> 관측 2026-10-26.
[^home]: SDLA, 첫 화면 NEWS & HIGHLIGHTS의 날짜와 제목. <https://sdla.snu.ac.kr/sdla> 관측 2026-10-26.
[^contact]: SDLA, Contact. 학교 이메일·전화·18동 404호와 301동 1052호. <https://sdla.snu.ac.kr/contact> 관측 2026-10-26.
[^p1]: G. Jung 외, J.-H. Lee, Nature Communications 17, 9963 (온라인 2026-08-20). <https://doi.org/10.1038/s41467-026-76918-1> 초록 기준(PubMed 등록 초록). 초록 원문 <https://pubmed.ncbi.nlm.nih.gov/42754585/>
[^p2]: R.-H. Koo 외, J.-H. Lee, Nano Convergence 12, 43 (2025). <https://doi.org/10.1186/s40580-025-00505-1> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/395057838_Physical_correlation_between_stochasticity_and_process-induced_damage_in_ferroelectric_memory_devices>
[^p3]: J. Ko 외, J. Lee, IEEE Electron Device Letters (2026). <https://doi.org/10.1109/LED.2026.3685316> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/404014086_2-T_Embedded_Flash_Memory_using_Standard_28_nm_Logic_CMOS_Technology>
[^p4]: S.-H. Park 외, J.-H. Lee, Advanced Science, e77390 (온라인 2026-08-24). <https://doi.org/10.1002/advs.77390> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.77390>
[^p5]: S.-H. Park 외, J.-H. Lee, Advanced Science 13, e74517 (온라인 2026-02-27). <https://doi.org/10.1002/advs.74517> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.74517>
[^p6]: S.-H. Park 외, J.-H. Lee, Applied Physics Letters 128, 152103 (온라인 2026-04-14). <https://doi.org/10.1063/5.0310928> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/403813779_Retention_improvement_in_vertical_NAND_flash_memory_using_block_soft_erase_scheme>
[^p7]: R.-H. Koo 외, J.-H. Lee, Nature Communications 17, 6236 (온라인 2026-05-08). <https://doi.org/10.1038/s41467-026-72969-6> 초록 기준(Crossref 등록 초록).
[^p8]: J. Ko 외, J.-H. Lee, IEEE Sensors Journal 26, 17045-17054 (2026). <https://doi.org/10.1109/jsen.2026.3678607> 초록 기준(OpenAlex 등록 초록).

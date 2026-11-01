# 3차원 집적 광/전자소자 연구실 (3D Integrated Opto-Electronic Device Laboratory, 3D-OEDL)

**KAIST 전기및전자공학부·반도체시스템공학과·반도체공학대학원 · 김상현 부교수**

- 분야: 반도체 소자, 입체 집적, 차세대 계산, 마이크로 LED, 적외선 센서·광회로
- 대분야: 전기전자·반도체·광학
- 태그: 3차원 집적[^stack][^p1][^p2], 뉴로모픽 소자[^compute], 차세대 트랜지스터·논리 소자[^compute], 마이크로 LED[^display][^p3], 광검출기[^imager][^p5], 광학 센서·분광기[^photonics][^p4], 가스 센서[^photonics][^p4], 이징 머신·물리 기반 계산[^p1]
- 홈페이지: <https://www.3doedl.com/>

> 서로 다른 반도체 재료와 소자를 입체적으로 합쳐, 계산·화면 표시·빛 감지를 수행하는 칩을 연구한다.

## 무엇을 연구하나

3D-OEDL은 광전자 소자(빛과 전기 신호를 서로 바꾸거나 함께 다루는 부품)를 연구한다. 화합물 반도체(서로 다른 원소를 결합해 만든 반도체)와 실리콘·게르마늄 계열 재료를 이용해 광전자 집적회로(여러 광전자 부품을 한데 연결한 회로)를 만드는 것이 연구실의 방향이다.[^home]

핵심 제작 방법은 서로 다른 재료의 층을 옮기고 붙여 한 칩 안에 소자를 층마다 쌓는 모놀리식 3차원 집적(monolithic 3D integration, M3D)이다. 위층 소자를 만들 때의 열이 아래층 소자에 영향을 주는 문제를 다룬다. 웨이퍼(반도체 소자를 만드는 재료판)를 접합하고, 원래 자라 있던 반도체 층을 떼어 옮기는 방법으로 화합물 반도체와 게르마늄(반도체 재료로 쓰이는 원소)의 층을 낮은 온도에서 쌓는 공정을 개발했다. 이 집적 기술을 계산 소자, 빛 검출기, 적외선 광회로(빛의 흐름을 제어하거나 빛으로 정보를 처리하도록 구성한 회로)와 마이크로 LED(Micro Light-Emitting Diode, 전류가 흐를 때 빛을 내는 미세한 무기 반도체 소자) 화면으로 연결한다.[^stack]

계산에서는 신경세포와 시냅스(신경세포 사이에서 신호를 전달하는 연결부)의 동작을 흉내 내는 뉴로모픽 소자와, 여러 선택의 조합에서 해를 찾는 이징 머신(선택을 서로 반대인 상태로 나타내고 상태 사이의 상호작용 에너지가 낮아지는 과정으로 해를 찾는 계산기)을 다룬다. 연구실은 위아래로 쌓을 수 있는 인공 신경세포·시냅스 소자를 개발하고 있다.[^compute] 대표 논문에서는 연결 상태를 기억하는 소자와 주기적으로 전기 신호를 내는 소자를 입체적으로 합쳐, 조합 문제를 푸는 계산기를 제안하고 실험·모의 계산으로 평가했다.[^p1]

빛을 내고 받아들이는 소자도 별도 연구 갈래다. 마이크로 LED는 빨강·초록·파랑 소자를 화소(화면을 이루는 영상 표시의 기본 단위)로 쌓아 화면을 만드는 데 초점을 둔다.[^display] 감지 쪽에서는 가시광·적외선 영상 센서와, 각 위치에서 연속된 여러 파장(빛의 공간적 반복 간격) 구간의 정보를 얻는 초분광 영상 센서를 연구한다.[^imager] 중적외선(적외선 중 특정 파장 구간의 빛)을 다루는 게르마늄 광회로를 이용해 기체를 감지하는 센서도 개발 목표다.[^photonics]

## 주요 연구 주제

### 서로 다른 반도체를 쌓는 집적 공정

실리콘을 관통하는 연결 구멍으로 칩을 잇는 방식에는 연결 크기·정렬·밀도 문제가 있다. 연구실은 단결정(원자가 규칙적으로 이어진 하나의 결정) 반도체 층을 옮기고, 서로 다른 재료의 소자를 쌓는 방법을 연구한다.[^stack] 2022년 논문에서는 InGaAs(인듐·갈륨·비소를 결합한 반도체)의 무선 신호용 트랜지스터와 실리콘 신호 변환 회로를 위아래 층으로 집적했다. 아래층 회로는 집적 공정 뒤에도 성능 저하 없이 유효한 신호를 냈다.[^p2]

### 차세대 계산 소자와 기억 가능한 연결

연구실은 화합물 반도체 재료와 게르마늄을 이용한 트랜지스터(전기 신호로 전류를 조절하는 부품)와 인공 신경망(신경세포의 연결에서 착안해 정보를 처리하는 계산 구조)용 소자를 개발한다.[^compute] 이징 머신 논문의 FeFET(ferroelectric field-effect transistor, 강유전성 재료에 남는 전기적 상태를 이용하고 전기장으로 전류를 조절하는 소자)는 계산 소자 사이의 연결 상태를 기억하는 스위치다. 이를 주기적인 전기 신호를 만드는 발진기와 결합해, 문제에 맞춰 연결을 바꾸는 입체 집적 계산기를 구성했다.[^p1] 메모리 소자 연구에서는 HZO(HfZrOx, 하프늄·지르코늄 산화물) 막의 두께 조절, 전자빔(음의 전기를 띤 입자인 전자를 일정 방향으로 모아 보내는 흐름) 처리, 계면층(서로 다른 재료가 맞닿는 경계에 있는 층) 처리를 함께 이용해, 낮은 전압에서 정보를 쓰고 쓴 직후 읽는 동작을 보였다.[^p6]

### 입체 적층 마이크로 LED 화면

빨강·초록·파랑 마이크로 LED를 쌓고 화면의 구동 회로와 결합하는 기술을 연구한다. 웨이퍼 접합과 순차적인 소자 제작으로 고해상도 화면을 구현하려 하며, 가상·증강현실 화면과 홀로그램 화면을 응용 대상으로 든다.[^display] 2025년 논문에서는 산화규소와 산화이트륨을 접합 재료로 써서 풀 컬러 화소를 적층했다. 산화물 접합층을 쓴 청색 소자에서 열 관리와 발광 효율·색 특성의 개선을 보였다.[^p3]

### 적외선 영상과 칩 위의 기체 감지

빛에 반응하는 인공 시냅스, 가시광부터 적외선까지 감지하는 영상 센서와 그 집적 기술을 연구한다.[^imager] 광검출기 논문은 얇은 빛 흡수층에 광학 구조를 더해, 가시광과 적외선 일부 구간에서 빛을 감지하는 소자를 보였다.[^p5] 기체 센서에서는 절연체(전기가 통하기 어려운 물질) 위에 게르마늄을 놓은 광회로를 개발한다.[^photonics] 2024년 연구는 자유지지형(별도의 연속 지지층 없이 형태를 유지하는) 게르마늄 광결정 도파로(빛의 전달 성질이 주기적으로 달라지는 구조를 이용해 빛을 정해진 경로로 보내는 구조)를 만들어 중적외선으로 이산화탄소를 감지했다.[^p4]

## 대표 논문

2021–2026년 연구실 논문 가운데 김상현 교수가 마지막 저자이자 연구실 목록에서 교신저자로 표시된 논문을 골랐다. 입체 집적, 차세대 계산, 마이크로 LED, 광 검출, 기체 센서, 강유전체 트랜지스터를 고르게 담았다. 연도는 인쇄 출판 연도가 있으면 그 연도를 쓰고, 없으면 온라인 출판 연도를 썼다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2025 | [Monolithic 3D Oscillatory Ising Machine Using Reconfigurable FeFET Routing for Large-Scalability and Low-Power Consumption](https://doi.org/10.1002/advs.202413247) · Advanced Science | 여러 선택을 조합해 답을 찾는 문제를 풀기 위해, 연결 상태를 기억하는 강유전체 트랜지스터와 전기 신호를 주기적으로 만드는 발진기를 입체적으로 합친 이징 머신을 제안했다. 트랜지스터의 연결을 제어해 문제의 상호관계를 발진기 사이에 넣는다. 실험과 모의 계산으로 조합 문제를 푸는 동작을 평가했다.[^p1] | 1저자 Joon Pyo Kim, 마지막·교신저자 김상현 |
| 2 | 2022 | [Heterogeneous and Monolithic 3D Integration of III-V-Based Radio Frequency Devices on Si CMOS Circuits](https://doi.org/10.1021/acsnano.2c00334) · ACS Nano | 무선 신호를 다루는 화합물 반도체 소자와 실리콘 전자 회로를 한 칩 안에서 위아래로 합쳤다. 위층에는 특성이 서로 다른 InGaAs 트랜지스터 두 종류를, 아래층에는 연속적인 신호와 숫자로 표현한 신호를 서로 바꾸는 회로를 놓았다. 위층 소자는 두 신호 방식이 섞이면서 생기는 간섭의 영향을 받지 않았고, 아래층 회로도 집적 공정 뒤 성능 저하 없이 유효한 신호를 냈다.[^p2] | 1저자 Jaeyong Jeong, 마지막·교신저자 김상현 |
| 3 | 2025 | [Heterogeneous and Monolithic 3D Integrated Full-Color Micro-Light-Emitting Diodes via CMOS-Compatible Oxide Bonding for µLEDoS](https://doi.org/10.1002/lpor.202402116) · Laser & Photonics Reviews | 빨강·초록·파랑 마이크로 LED를 위아래로 쌓아 풀 컬러 화소를 만들 때의 열 관리와 공정 문제를 다뤘다. 층을 서로 붙이는 재료로 산화규소와 산화이트륨을 사용했다. 산화물로 접합한 청색 소자는 열 관리와 발광 효율·색 특성이 개선되었다. 접합층의 두께도 조절해 화소의 두께를 줄이고 고해상도 화면의 제작 가능성을 높였다.[^p3] | 1저자 Hyun soo Kim, 마지막·교신저자 김상현 |
| 4 | 2024 | [Freestanding Germanium Photonic Crystal Waveguide for a Highly Sensitive and Compact Mid-Infrared On-Chip Gas Sensor](https://doi.org/10.1021/acssensors.4c00941) · ACS Sensors | 게르마늄과 산화이트륨을 이용해 자유지지형 광결정 도파로를 만들고 중적외선 기체 감지에 사용했다. 빛과 물질이 상호작용하는 영역을 넓히고 도파로에서 빛이 새어 나가는 형태가 생기지 않도록 했다. 빛과 기체의 상호작용을 높여 칩 위의 도파로 길이를 줄였으며, 이산화탄소 감지를 보였다.[^p4] | 1저자 Inki Kim, 마지막·교신저자 김상현 |
| 5 | 2024 | [Highly-efficient (>70%) and Wide-spectral (400-1700 nm) sub-micron-thick InGaAs photodiodes for future high-resolution image sensors](https://doi.org/10.1038/s41377-024-01652-6) · Light: Science & Applications | 빛을 흡수하는 층이 두꺼울 때 생기는 화소 간 간섭 문제를 다루기 위해 얇은 InGaAs 광검출기를 만들었다. 빛 흡수층이 얇아져도 빛을 전기 신호로 바꾸는 효율을 유지하도록 광학 구조를 설계했다. 가시광과 적외선 일부 구간에서의 검출을 보였으며, 전자가 소자를 통과하는 시간이 짧아지면 전기적 간섭이 줄어들 것으로 기대했다.[^p5] | 1저자 Dae-Myeong Geum, 마지막·교신저자 김상현 |
| 6 | 2024 | [Low Operating Voltage and Immediate Read-After-Write of HZO-Based Si Ferroelectric Field-Effect Transistors with High Endurance and Retention Characteristics](https://doi.org/10.1002/aelm.202300327) · Advanced Electronic Materials | 하프늄·지르코늄 산화물 기반 실리콘 강유전체 트랜지스터에서 막 두께 조절, 전자빔 처리, 재료 사이 계면층 처리를 함께 이용했다. 낮은 전압에서 정보를 쓰고 쓴 직후 읽는 동작을 보였으며, 반복 동작 내구성과 정보 보존 특성을 개선했다. 장기 보존 기간은 측정 범위를 벗어난 시점까지 계산해 추정한 값으로 제시했다.[^p6] | 1저자 Bong Ho Kim, 마지막·교신저자 김상현 |

## 교수와 전문 분야

김상현 교수는 도쿄대학교 전기공학·정보시스템 분야에서 학사(2009), 석사(2011), 박사(2014)를 받았다. 한국과학기술연구원 연구원·선임연구원으로 일했고, 2017년 7월부터 2018년 6월까지 imec의 3D & Optical I/O 팀에서 Post-doc R&D Specialist로 일했다. 2019년 2월 KAIST 전기및전자공학부 조교수로 부임했으며, 연구실 경력표는 2021년 9월부터 Associate Professor로 적는다. 전기및전자공학부 전임교수 명단도 직위를 부교수로 적는다.[^pi][^ee]

전기및전자공학부는 주요 연구를 「3D적층형 반도체 광소자/전자소자, IOT향 소자 기술」로 소개한다.[^ee] 연구실 소개와 최근 논문을 함께 보면 전문 분야는 서로 다른 반도체의 입체 집적, 계산·메모리 소자, 마이크로 LED와 적외선 광전자 소자의 제작·집적으로 정리할 수 있다.[^stack][^compute][^display][^imager][^photonics] 대표 논문은 서로 다른 반도체와 회로를 합치는 집적 기술,[^p2] 마이크로 LED 화면,[^p3] 적외선 센서·광검출기,[^p4][^p5] 강유전체 트랜지스터,[^p6] 물리 기반 계산[^p1]을 보여 준다.

## 응용 분야

집적 기술의 응용으로 계산 회로, 적외선 감지, 마이크로 LED 화면을 들고 있다.[^stack] 화면 연구는 가상·증강현실용 표시 장치를,[^display] 영상 센서 연구는 패턴 인식과 실시간 영상 처리를,[^imager] 게르마늄 광회로 연구는 중적외선에 반응하는 기체 센서를 지향한다.[^photonics]

## 구성원

2026년 10월 31일 연구실 게시 기준으로 Researchers 2명(박사후연구원 1명·Researcher 1명), Ph.D Candidates 10명, M.S Candidates 16명이다. 시작과 연구 주제는 카드의 표기다.[^researchers][^phd][^ms] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.

| 이름 | 과정 | 시작 | 연구 주제 | 대표 논문 참여 |
|---|---|---|---|---|
| Jun Ho Jang | 박사후연구원 | 25' spring- | IR Imager | 5 |
| Hyun Wook Kim | 연구원 | 26' spring- | 2D Transistor | 1 |
| Shin Hyung Lee | 박사과정 | 23' spring- | Hybrid Laser Diode |  |
| In Ki Kim | 박사과정 | 24' spring- | Mid-IR Photonics | 3, 4 |
| Na Hyun Rheem | 박사과정 | 25' spring- | Monolithic 3D, next generation computing |  |
| Chan Jik Lee | 박사과정 | 25' spring- | Monolithic 3D, High-speed transistor, Power device | 6 |
| Sung Hwan Lee | 박사과정 | 26' spring- | Si logic device, 2D Transistor |  |
| Hyun Su Kim | 박사과정 | 24' spring- | MicroLED |  |
| Yoon Je Suh | 박사과정 | 24' spring- | Monolithic 3D, next generation computing | 6 |
| Dong Gil Kang | 박사과정 | 25' spring- | RF photonics |  |
| Ho Sang Hwang | 박사과정 | 25' fall- | Image sensor |  |
| Seong Min Cho | 박사과정 | 26' fall- | Red micro LED |  |
| Yong Hwan Han | 석사과정 | 25' spring- | Si photonics |  |
| Min Hyeok Lee | 석사과정 | 25' spring- | Power device, On-chip 3D capacitor |  |
| Tae Young Jang | 석사과정 | 25' fall- | Monolithic 3D, Ge device |  |
| Le Hoai Bao | 석사과정 | 25' fall- | Micro LED |  |
| Geon Woo Kim | 석사과정 | 26' spring- | Ferroelectric FET |  |
| Sun Woo An | 석사과정 | 26' spring- | Ge CFET |  |
| Aziret-Sultan Kiyazov | 석사과정 | 26' spring- | On-chip inductor |  |
| Chae Yeon Han | 석사과정 | 26' fall- | High-speed transistor, Power device |  |
| Chae Yeon Kim | 석사과정 | 25' spring- | Monolithic 3D, Micro LED |  |
| Jong Un Beom | 석사과정 | 25' fall- | Ferroelectric FET |  |
| Soo Hyun Kim | 석사과정 | 25' fall- | Mid-IR Photonics |  |
| Se Hwan Kwon | 석사과정 | 26' spring- | Micro LED |  |
| Seo Kang Choi | 석사과정 | 26' spring- | Monolithic 3D, next generation computing |  |
| Been Yun | 석사과정 | 26' spring- | On-chip laser sources |  |
| Tae Beom Kim | 석사과정 | 26' spring- | TBD |  |
| Si Heon Park | 석사과정 | 26' fall- | Monolithic 3D, Power device |  |

## 졸업생과 이전 구성원

2026년 10월 31일 Alumni 페이지의 Ph.D. Graduates / Post-doc. 13명과 M.S. Graduates 10명이다. 학위·과정·기간과 진로는 연구실 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| Dr. Ju Hyeok Park | 2025-2026, Post-doc; 2021-2025, Ph.D.; 2019-2021, M.S. | imec |
| Dr. Seung Yeop Ahn | 2020-2026, Ph.D. | LG Display |
| Dr. Bong Ho Kim | 2021-2025, Ph.D. | Samsung Electronics |
| Dr. Song Hyeon Kuk | 2022-2025, Ph.D.; 2020-2022, M.S. | Georgia Institute of Technology Postdoctoral researcher |
| Dr. Joon Sup Shim | 2020-2024, Ph.D. | Samsung Advanced Institude of Technology |
| Dr. Seong Kwang Kim | 2019-2023, Ph.D. | Samsung Electronics |
| Prof. Dae Myeong Geum | 2019-2022, Post-doc | Inha University Assistant professor |
| Prof. Jae Yong Jeong | 2024-2026, Post-doc; 2021-2024, Ph.D.; 2019-2021, M.S. | UNIST Assistant professor |
| Dr. Hyeong Rak Lim | 2020-2026, Ph.D. | Samsung Electronics |
| Dr. Woo Jin Baek | 2022-2025, Ph.D.; 2020-2022, M.S. | Samsung Display |
| Dr. Joon Pyo Kim | 2022-2025, Ph.D.; 2020-2022, M.S. | Samsung Electronics |
| Dr. Jin Ha Lim | 2019-2023, Ph.D. | Yale University Postdoctoral researcher |
| Dr. Pavlo Bidenko | 2019-2022, Post-doc |  |
| Min Seo Song, M.S. | 2024-2026, M.S. | SK Hynix |
| Min Kyu Ju, M.S. | 2024-2026, M.S. | Samsung Electronics |
| Da Hye Lee, M.S. | 2024-2026, M.S. | Samsung Electronics |
| Dong Ho Gwak, M.S. | 2022-2024, M.S. | KAIST |
| Jae Ho Sim, M.S. | 2020-2022, M.S. | DB HiTek |
| Hyun Jun Lee, M.S. | 2024-2026, M.S. | Seoul National University |
| Hyeon Seong Hwang, M.S. | 2024-2026, M.S. |  |
| Ho Jin Jeong, M.S. | 2023-2025, M.S. | Rebelloins |
| Sung Jun Choi, M.S. | 2022-2024, M.S. | SK Hynix |
| Seung Woo Lee, M.S. | 2020-2022, M.S. | SK Hynix |

## 최근 논문 목록 (2021–2026)

연구실 게시 학술지 논문 82편, 학회 논문·발표 68건, 책 장 1건이다. 연도만 적힌 학술지·책 장은 2021–2026년 구역을 따르고, 날짜가 적힌 학회 항목은 2021년 10월 13일부터 2026년 10월 13일까지를 대상으로 한다. 학술지의 in press는 출판 예정, 책 장의 in press는 연구실 기재 상태다. 2026년 6월 학회 항목의 to be presented도 연구실 기재 상태다. 논문 제목과 저자·발표처는 연구실 표기이며, 저자 이름 뒤의 +·†·^는 누리집 표시다.[^j2026][^j2025][^j2024][^j2023][^j2022][^j2021][^conference][^book]

**2026**

- B. -H. Kim, S. -H. Kuk, H. -S. Hwang, J. Jeong, Y. Park, Y. -J. Suh, J. -P. Kim, C. -J. Lee, S. -K. Kim, D. -M. Geum, B. -J. Cho, S. -H. Kim\*. "Asymmetric Memory Window Recovery Behavior in n/p-FeFETs Revealed by Trap Analysis". *IEEE Transactions on Device and Materials Reliability, in press*.
- H. -S. Hwang, B. -H. Kim, S. -H. Kuk, J. -U. Beom, J. -Y. Jeong, J. -H. Han, M. -H. Lee, S. -H. Kim\*. "Thermally-desorbable GeOx/Ge Interlayer Engineering for Channel Surface Orientation Independent 3D Non-Volatile Memory". *IEEE Electron Device Letters, in press*.
- T. -H. Chung, S. -H. Jung, D. -Y. Kim, H. -J. Choi, W. -J. Baek, S. -H. Kim, K. -J. Lee\*, J. -H. Min\*, and J. -K. Lee\*. "Buried p-Type GaN Activation under V-Pitted n-Type GaN for Tunnel Junction Micro-LEDs". *Optics Express 34, p. 26412 (2026)*.
- H. -R. Lim, S. -K. Kim, H. Jeong, J. Lim, S. -H. Kuk, D. -M. Geum, J. Bae, J. Park, D. Ha, Y. Kim, J. Jeong, S. -H. Kim\*. "Uniaxially Compressively Strained Ge (100)-OI p-MOSFET for High-Performance CFET". *IEEE Transactions on Electron Devices 73, p. 4250 (2026)*.
- J. Shim+, S. Kim+, S. Lu, J. Yang, S. Jeon, S. -H. Kim, M. Loncar, Y. -K. Shon. "Generalized Model of Anisotropic Thermo-Optic Response on Thin-Film Lithium Niobate Platform". *ACS Photonics 13, p. 2586 (2026)*.
- B. Kim, S. -H. Kuk, H. -S. Hwang, J. Jeong, Y. Park, Y. -J. Suh, J. -P. Kim, C. -J. Lee, B. -J. Cho, and S. -H. Kim\*. "Effective Recovery Operation in FeFETs via Suppression of Hole Injection". *IEEE Transactions on Electron Devices 73, p. 2710 (2026)*.
- Y. Kang+, J. Park+, S. -H. Kim\*, D. -M. Geum\*. "Comprehensive Study of Current-Density-Dependent Degradation in AlGaInP/GaInP Based Red Micro-LEDs". *Surfaces and Interfaces 90, 109167 (2026)*.
- S. -Y. Yun+, J. -P. Kim+, J. Jeong, S. -W. Lee, Y. -S. Chung, S. - H. Kim\*, Y. -K. Choi\*. "Scalable Ising machine composed entirely of Si transistors". *Science Advances 12, eadz2384 (2026)*.
- H. -J. Lee+, J. -P. Kim+, S. -H. Kim\*. "Fundamental Challenges, Physical Implementations, and Integration Strategies for Ising Machines in Large-Scale Optimization Tasks". *Advanced Electronic Materials 12, e00682 (2026)*.
- B. Kim, S. -H. Kuk, H. -S. Hwang, J. Jeong, Y. Park, Y. -J. Suh, J. -P. Kim, C. -J. Lee, B. -J. Cho, and S. -H. Kim\*. "Robust Disturb Immunity in AND-Type 1T FeFET Arrays by Electron Detrapping Mode". *IEEE Transactions on Electron Devices 73, p. 1798 (2026)*.
- H. Jung, J. Choi, S. Baek, B. -G. Shin, Y. J. Song\*, H. Jung, J. Kim, J. Jeon\*, G. Kim, H. Park\*, Y. Lee, J. Yoo\*, J. -H. Lee, H. Kim, K. Kang\*, J. Jeong, S. -H. Kim\*, J. Bae, C. -S. Kim, W. -K. Yang, S. Lee, J. Kwon\*, B. -S. Kim, J. -H. Han\*, H. -J. kim, H. -H. Yoon\*, J. Kwon\*, Y. -J. Hong\*. "Advances and Future Challenges in Monolithic 3D Integrated Logic, Power, and Optoelectronics Technologies for Tightly Interconnected Intelligent Systems". *ACS Nano 20, p. 6407 (2026)*.
- J. Park+, E. -J. Youn+, H. -S. Kim, W. -J. Baek, S. -A. Oh, I. -S. Cho, D. -S. Kim, W. -T. Lim, J. -B. Lee, J. -H. Park, J. -G. Kim, J. -H. Min\*, H. -H. Park\*, S. -H. Kim\*. "Hybrid Integration of Tunnel-Junction InGaN/GaN and Wafer-Bonded AlGaInP/GaInP for Full-Color Micro-LEDs". *ACS Applied Materials & Interfaces 18, p. 10067 (2026)*.
- J. Park, W. Baek, H. Kim, D. Jung, H. Kim, B. Kim, Y. -H. Cho, J. Lee, S. -W. Lim, S. -H. Lee, S. Ahn, S. -K. Kim, J. Jeong, J. -P. Kim, J. Lim, J. Shim, D. -M. Geum\*, S. -H. Kim\*. "A monolithic three-dimensional integrated red micro-LED display on silicon using AlInP/GaInP epilayers". *Nature Electronics 9, p. 170 (2026)*.
- B. Kim, S. -K. Kim, S. -H. Kuk, J. Jeong, Y. Park, Y. -J. Suh, J. -P. Kim, C. -J. Lee, D. -M. Geum, B. -J. Cho, and S. -H. Kim\*. "Recovery Operation in HfZrOx-Based FeFETs with Interfacial Layer Scavenging". *IEEE Transactions on Electron Devices 73, p. 807 (2026)*.
- Y. Park+, H. -R. Lim+, J. Jeong, J. -P. Kim, J. Baek, M. Song, S. -K. Kim, S. -H. Kim\*, B. -J. Cho\*. "High-Performance Heterogeneous 3-D Sequential CFETs Using Pulsed Green Laser Annealing". *IEEE Transactions on Electron Devices 73, p. 44 (2026)*.
- C. Kim, J. Park, H. -S. Kim, L. -H. Bao, S. -H. Kim\*. "Enhancement of External Quantum Efficiency in Phosphide-based Red Micro-LEDs Enabled by a Low-optical-loss N-contact layer". *International Meeting on Information Display (IMID), 2026/8, Bexco, Korea*.
- D. Kang, S. -H. Lee, J. Han, J. Kim, S. -G. Ahn, M. Jung, H. -C. Jung, S. -H. Kim\*. "Depletion-Mode III-V/Si SISCAP Mach-Zehnder Modulator Breaking the Efficiency-Bandwidth Trade-Off for Co-Packaged Optics". *Symposium on VLSI Technology and Circuits, 2026/6, Hawai, to be presented*.
- S. -H. Kuk, J. -Y. Jeong, B. -H. Kim, J. -P. Kim, C. Park, D. Kang, H. -S. Hwang, S. -H. Lee, K. Ko, J. -H. Han, S. Datta\*, and S. -H. Kim\*. "High-Field Breakdown Mechanism Limiting Write Endurance in Ferroelectric FET for 3D NAND". *International Reliability Physics Symposium (IRPS), 2026/3, Arizona, US*.

**2025**

- J. Jang, I. -S. Kang, Y. -W. Oh, S. Jung, H. Cho, S. -H. Kim\*. "Spectroscopy using guided-mode resonance InGaAs photodetector array". *ACS Photonics 12, p. 6352 (2025)*.
- W. Byun+, B. -H. Kim+, S. Han, Y. Kang, S. -H. Kim, I. -H. Baek\*, D. -M. Geum\*. "Oxygen Ambient Annealing-Driven Contact Engineering and Channel Property Modulation in Tungsten/InGaZnO Thin-film Transistors for BEOL-Compatible Integration". *Result in Physics 78, p. 108468 (2025)*.
- W. -J. Baek, J. Park, H. -S. Kim, D. -M. Geum, J. -H. Min, T. -H. Chung, S. -H. Kim\*. "Insight on Self-emissive μLEDs Display from Correlation between Surface Current and Efficiency/Emission Properties of Size-dependent μLEDs". *ACS Photonics 12, p. 3525 (2025)*.
- H. -R. Lim, S. -K. Kim, S. W. Lee, Y. Park, J. Jeong, H. Jeong, J. Lim, D. -M. Geum, J. -H. Han, Y. Kim, J. Jeong, B. -J. Cho, S. -H. Kim\*. "Heterogeneous 3D Sequential CFET with Strain-Engineered Ge (100) Top-Channel pMOSFET on Bulk Si (100) nMOSFET". *IEEE Transactions on Electron Devices 72, p. 3422 (2025)*.
- S. -H. Kuk, B. -H. Kim, Y. Park, K. Ko, H. -S. Hwang, B- J. Cho, J. -H. Han, S. -H. Kim\*. "Superior QLC Retention Enhancement of a Large Memory Window FEFET Through Gate-Stack Engineering". *IEEE Transactions on Electron Devices 72, p. 3896 (2025) (Special issue for the extended paper of International Electron Devices Meeting (IEDM) 2024)*.
- J. Jeong+, C. -J. Lee+, S. -J, Choi, N. Rheem, M. Song, Y. -J. Suh, B. -H. Kim, J. -P. Kim, J. Shim, J. Lee, M. Park, Y. Koh, D. -H. Kim, S. -H. Kim\*. "3D On-chip Integration of GaN Power Devices on Power Delivery Network (PDN) with Direct Heat Spreading Layer Bonding for Heterogenous 3D (H3D) Stacked Systems". *IEEE Transactions on Electron Devices 72, p. 2654 (2025) (Special issue for the extended paper of International Electron Devices Meeting (IEDM) 2024)*.
- I. Kim, J. Shim, J. Lim, J. Jeong, B. -H. Kim, S. -H. Kim\*. "Highly-Sensitive Free-Standing Waveguide-Integrated Bolometer on Germanium-on-Insulator Platform for Mid-Infrared on-Chip Spectroscopy". *IEEE Transactions on Electron Devices 72, p. 2733 (2025) (Special issue for the extended paper of International Electron Devices Meeting (IEDM) 2024)*.
- H. -S. Kim, J. Park W. -J. Baek, D. -M. Geum, I. Kim, H. -R. Lim, J. Lim, S. -K. Kim, J. Jeong, J. Shim, J. -H. Min, S. -H. Kim\*. "Heterogeneous and Monolithic 3D integrated Full-Color Micro-Light-Emitting Diodes via CMOS-Compatible Oxide Bonding for µLEDoS". *Laser & Photonics Review 19, 2402116 (2025)*.
- W. -J, Baek, J, -P. Kim, S. -H. Kuk, J. Park, H. -S. Kim, D. -M. Geum, S. -H. Kim\*. "Field-Effect Passivation of GaN-based Blue Micro-light-emitting Diodes". *IEEE Journal of the Electron Device Society 13, p. 303 (2025)*.
- J. Shim, J. Lim, I. Kim, J. Jeong, B. -H. Kim, S. -K. Kim, D. -M. Geum, S. -H. Kim\*. "Room-temperature waveguide-integrated photodetector using bolometric effect for mid-infrared spectroscopy applications". *Light: Science & Applications 14, 125 (2025)*.
- J. -P. Kim, S. -H. Kuk, H. -W. Kim, J. Jeong, J. Park, B. -H. Kim, J. Kim, A. Todri-Sanial, S. -H. Kim\*. "Monolithic 3D Oscillatory Ising Machine using Reconfigurable FeFET Routing for large-scalability and low-power consumption". *Advanced Science 12, 2413247 (2025)*.
- D. Gwak, S. -Y. Ahn, J. Lim, J. Jeong, B. Lee, Y. Kim, S. -H. Kim\*. "Quantum efficiency enhancement using photon-trapping structure on extended SWIR type-II superlattice nBn photodetector". *Optics Express 33, p. 13217 (2025)*.
- J. Jeong, J. Kim\*, S. -H. Kim\*. "High-performance InGaAs HEMTs on GaAs substrate using AlAs/GaAs superlattice buffer-assisted heterostructure growth". *Journal of Alloys and Compounds 1019, 178699 (2025)*.
- S. -Y. Ahn+, J. Lim+, D. -M. Geum, D. Gwak, K. -K. Kang, J. -H. Eom, Y. -H. Kim, S. -H. Kim\*. "Enhanced Broadband Quantum Efficiency in LWIR T2SL Detectors with Guided-Mode Resonance Structure". *Optics Express 33, p. 1898 (2025)*.
- S. -H. Kuk, K. Ko, B. -H. Kim, J. -P. Kim, J. -H. Han, S. -H. Kim\*. "Channel Mobility and Inversion Carrier Density in MFIS FEFET: Deep Insights into Device Physics for Non-Volatile Memory Applications". *IEEE Journal of the Electron Device Society 13, p. 8 (2025)*.
- Y. Shin+, I. Kim+, M. Park+, J. Yoon, S. Baek, S. Eum, H. Yang, Y. Choi, J. Jeong, S. -H. Kim, H. Jung, S. Kim\*, H. Park\*, J. Kwon\*. "Active BSCDN Benchmark Framework with Backside Complementary CNFET Logic Technology". *2025 International Electron Devices Meeting (IEDM), 2025/12, San Francisco, CA, USA*.
- J. Jeong+, C. -J. Lee+, Y. -J. Suh, N. Rheem, B. -H. Kim, J. -P. Kim, J. Park, S. -H. Kim\*. "Heterogeneous 3D Integrated RF Platform: III-V/III-N RF Blocks transfer onto CMOS via Die-to-Wafer Bonding Technology for High-Frequency and High-Density Wireless Communication Systems". *2025 International Electron Devices Meeting (IEDM), 2025/12, San Francisco, CA, USA*.
- J. -P. Kim+, S.- H. Kuk+, J. Jeong, H. -J. Lee, J. Park, B. -H. Kim, J. Kim, S. -H. Kim\*. "A Compact and Energy-Efficient Monolithic-3D Oscillatory Ising Machine with Novel Ferroelectric Multi-Weight Coupling". *2025 International Electron Devices Meeting (IEDM), 2025/12, San Francisco, CA, USA*.
- J. Jeong+, Y. Choi+, S. Kim, H. Kim, J. Kwon\*, S. -H. Kim\*. "Monolithic 3D Integration of III-V HEMTs on Glass Using Ultra-Thin Dielectric Bonding Layer: A High-Frequency and Low-Loss Active Glass Platform for Sub-THz Applications". *2025 International Electron Devices Meeting (IEDM), 2025/12, San Francisco, CA, USA*.
- S. -H. Kim\*. "Toward Highly efficient and High-resolution MicroLED display on CMOS". *International Meeting on Information Display (IMID), 2025/8, Bexco, Korea*.
- J. Park, H. Kim, Y. Kim, W. Baek, S. -H. Lee, H. Kim, D. -M. Geum, J. -P. Kim, J. Jeong, S. -H. Kim\*. "High-Performance Monolithic 3D Integrated Red µLEDoS Display for AR/VR". *International Meeting on Information Display (IMID), 2025/8, Bexco, Korea (Best Poster Paper Award)*.
- S. -H. Kim\*, D. -M. Geum. "Ultra-Thin InGaAs Photodetector for Broadband Image Sensor". *Nano Korea, 2025/7, Incheon, Korea*.
- J. Jeong, J. -T. Lim, Y. -J. Suh, N. Rheem, C. -J. Lee, B. -H. Kim, J. -P. Kim, J. Kim, J. Lee, C. -Y. Kim, S. -H. Kim\*. "Fully Heterogeneous and Monolithic 3D Integrated RF Platform with III-V HEMTs on Si CMOS for Next-Generation Wireless Communication Systems". *Symposium on VLSI Technology and Circuits, 2025/6, Kyoto, Japan*.
- J. Jeong, C. -J. Lee, Y. -J. Suh, N. Rheem, B. -H. Kim, J. -P. Kim, S. -H. Kim\*. "Heterogeneous 3D Integration of Low-Voltage E/D-mode GaN HEMTs on CMOS Chip for Efficient On-Chip Voltage Regulation in Active Power Delivery Networks". *Symposium on VLSI Technology and Circuits, 2025/6, Kyoto, Japan*.
- J. Park, H. Kim, Y. Kim, W. -J. Baek, S. -H. Lee, H. -S. Kim, D. -M. Geum, J. -P. Kim, J. Jeong, S. -H. Kim\*. "High-Performance Monolithic 3D Integrated Red µLEDoS Display for AR/VR". *Symposium on VLSI Technology and Circuits, 2025/6, Kyoto, Japan*.
- S. -H. Kim\*. "Single crystalline semiconductor oscillator for Oscillator-based computing". *European Material Research Society (E-MRS), 2025/5, Strasbourg, France*.
- S. -H. Kim\*, S. -K. Kim, H. -R. Lim, J. Jeong, Y. Park, J. Jeong, J. -P. Kim, B. -H. Kim, D. -M. Geum, Y. Kim, B. -J. Cho. "Heterogeneous 3D CFET with Hybrid Channel Configuration". *Conference of Science&Technology for Integrated Circuits (CSTIC), Semicon China, 2025/3, Shanghai, China*.
- J. Jeong, Y. -J. Suh, N. Rheem, S. -K. Kim, B. -H. Kim, J. -P. Kim, J. Shim, M. Park, J. -T. Lim, M. Seong, J. Lee, K. Kim, D. -M. Geum, J. Kim, W. -S. Sul, W. -C. Lee, C. -Y. Kim, J Lee, S. -H. Kim\*. "Heterogeneous and monolithic 3D (HM3D) Integration of III-V and CMOS for next-generation wireless communication". *IEEE Electron Devices Technology and Manufacturing Conference (EDTM), 2025/3, Hong Kong*.
- S. -H. Kim\*, S. -K. Kim, H. -R. Lim, J. Jeong, Y. Park, J. Jeong, J. -P. Kim, B. -H. Kim, D. -M. Geum, Y. Kim, B. -J. Cho. "Heterogeneous 3D CFET with Hybrid Channel Configuration". *IEEE Electron Devices Technology and Manufacturing Conference (EDTM), 2025/3, Hong Kong*.

**2024**

- J. Jang, D. -M. Geum, I. -S. Kang, Y. -W. Oh, S. Jung, H. Cho, S. -H. Kim\*. "Guided-mode resonance polarization-sensitive narrowband InGaAs photodetector". *Laser & Photonics Review 19, 2401253 (2024)*.
- J. Jeong, S. -K. Kim, Y. -J. Suh, J. Lee, J. Choi, J. -P. Kim, B. -H. Kim, J. Park, J. Shim, N. Rheem, C. -J. Lee, Y. Jo, D. -M. Geum, S. -Y. Park, J. Kim, S. -H. Kim\*. "Cryogenic III-V and Nb electronics integrated on silicon for large-scale quantum computing platforms". *Nature communications 15, 10809 (2024)*.
- D. -M. Geum+, J. Lim+, J. Jang, S. -Y. Ahn, S. -K. Kim, J -S. Shim, B. -H. Kim, J. Park, W. -J. Baek, J. Jeong, S. -H. Kim\*. "Highly-efficient (>70%) and Wide-spectral (400 nm -1700 nm) sub-micron-thick InGaAs photodiodes for future high resolution image sensors". *Light: Science & Applications 13, 311 (2024)*.
- M. Park, M. Seong, J, Jeong, S Lee, J, Song, H. Ko, G. -W. Lee, W. -S. Sul, W. -C. Lee, S. -H. Kim\*, J. Lee\*. "Silicon-based integrated passive device stack for III-V/Si monolithic 3D circuits operating on RF band". *Solid State Electronics 221, 109012 (2024)*.
- J. -P. Kim, H. -W. Kim, J. Jeong, J. Park, S.- H. Kuk, J. Kim, J. Woo, S. -H. Kim\*. "BEOL-compatible 4F2 Oscillator using Vertical InGaAs Biristor for Highly Scalable Monolithic 3D Ising Solver". *Small, 2406822 (2024)*.
- I. Kim, J, Lim, J. -S. Shim, J. Park, S. -Y. Ahn, H. -R. Lim, S. -H. Kim\*. "Free-standing Germanium photonic crystal waveguide for highly sensitive and compact mid-infrared on-chip gas sensor". *ACS Sensors 9, p. 5116 (2024)*.
- S. -H. Kuk, K. Ko, B. -H. Kim, H. -R. Lim, J. -P. Kim, J. -H. Han, S. -H. Kim\*. "Channel Mobility with Higher-κ Doped-HfO2 for CMOS Logic". *IEEE Transactions on Electron Devices 71, p. 6534 (2024)*.
- J. Lim, J. Shim, I. Kim, S. -K. Kim, H. -R. Lim, S. -Y. Ahn, J. Park, D. -M. Geum, S. -H. Kim\*. "Ultrasensitive mid-infrared optical gas sensor based on Germanium-on-insulator photonic circuits with limit-of-detection of sub-ppm level". *ACS Photonics 11, p. 3907 (2024)*.
- J. Lim, J. -S. Shim, I. Kim, S. -K. Kim, D. -M. Geum, S. -H. Kim\*. "Thermally Tunable Microring Resonators based on Germanium-on-Insulator for Mid-Infrared Spectrometer". *APL Photonics 9, 106109 (2024)*.
- HJ. Kim+, D. J. Kim+, J. P. Baek, W. J. Kim, S. -H. Kim, and T.-S. Kim\*. "Intrinsic Thermo-Mechanical Properties of Freestanding TEOS-SiO2 Thin Films Depending on Thickness". *ACS Applied Electronic Materials, 6, 5293-5300 (2024)*.
- J. Jeong, S. -K. Kim, Y. -J. Suh, J. Shim, W. -J. Beak, S. -J. Choi, J. -P. Kim, B. -H. Kim, D. -M. Geum, J. Kim, S. -H. Kim\*. "Thermal Studies of 3D Stacked InGaAs HEMTs and Mitigation Strategy of Self-Heating Effect using Buried Metal Insertion". *IEEE Transactions on Electron Devices 71, p. 4517 (2024)*.
- J. Park+, E. -J. Youn+, W. -J. Baek, E. -K. Chu, H. -S. Kim, D. -M. Geum, J. -P. Kim, B. -H. Kim, S. -H. Kuk, H. -H. Park\*, and S. -H. Kim\*. "Size-dependent optoelectronic characteristics of InGaN/GaN red micro-LEDs on 4-inch Si substrates: High-resolution pixel arrays demonstration". *Optics Express 32, p. 24242 (2024)*.
- S. Kang, I. -P. Roh, S. -H. Kim, M. -H. Kang, D. -M. Geum\*, J -D. Song\*. "High electron mobility in Metamorphic Epitaxial InAs0. 7Sb0. 3 Compounds and its pin photodetector". *Journal of Alloys and Compounds 989, 174255 (2024)*.
- Y. -J. Suh, J. Jeong, B. -H. Kim, S. -H. Kuk, S. -K. Kim, J. -P. Kim, S. -H. Kim\*. "Large Polarization Of Hf0.5Zr0.5Ox Ferroelectric Film On InGaAs With Electric-Field Cycling And Annealing Temperature Engineering". *IEEE Electron Device Letters 45, p. 766 (2024)*.
- S. -H. Kuk, S. -J. Choi, H. -Y. Kim, K. Ko, J. Jeong, D. -M. Geum, J. -H. Han, J. -H. Park, D. Jeon, S. -H. Kim\*. "Heavily-Doped Channel Carrier Mobility in β-Ga2O3 Lateral Accumulation MOSFET". *IEEE Transactions on Electron Devices 71, p. 3429 (2024)*.
- J. Jeong, J. Kim, J. -S. Lee, , Y. -J. Suh, N. Rheem, S. -K. Kim, J. Park, B. -H. Kim, J. -P. Kim, S. -Y. Park, S. -H. Kim\*. "Impact of the channel thickness fluctuation on the subthreshold swing of InGaAs HEMTs at cryogenic temperature down to 4 K for ultra-low power LNAs". *IEEE Transactions on Electron Devices 71, p. 3390 (2024) (Special issue for the extended paper of International Electron Devices Meeting (IEDM) 2023)*.
- S. -K. Kim, H. -R. Lim, J. -J. Jeong, S. -W. Lee, H. -J. Jeong, J. Park, J. -P. Kim, J. Jeong, B. -H. Kim, S. -Y. Ahn, Y. Park, D. -M. Geum, Y. Kim, Y. Baek, B. -J. Cho, S. -H. Kim\*. "Heterogeneous 3D Sequential CFETs with Ge (110) Nanosheet p-FETs on Si (100) bulk n-FETs". *IEEE Transactions on Electron Devices 71, p. 393 (2024)*.
- J. Jeong, M. Park, Y. -J. Suh, J. -T. Lim, M. Seong, J. Lee, K. Kim, N. Rheem, C. -J. Lee, B. -H. Kim, S. -K. Kim, J. -P. Kim, J. Kim, W. -S. Sul, W. -C. Lee, C. -Y. Kim, J. Lee\*, S. -H. Kim\*. "Heterogeneous and Monolithic 3D (HM3D) Integrated RF Circuits: HM3D Integration of InGaAs HEMTs on CMOS-Based Backside Passive Devices". *2024 International Electron Devices Meeting (IEDM), 2024/12, San Francisco, CA, USA*.
- J. Jeong+, C. -J. Lee+, S. -J, Choi, N. Rheem, M. Song, Y. -J. Suh, B. -H. Kim, J. -P. Kim, J. Shim, J. Lee, M. Park, Y. Koh, D. -H. Kim, S. -H. Kim\*. "Vertically Integrated Active Power Delivery Network (PDN) for Heterogenous 3D (H3D) Stacked Systems: 3D On-chip Integration of GaN Power Devices on PDN with Direct Heat Spreading Layer Bonding". *2024 International Electron Devices Meeting (IEDM), 2024/12, San Francisco, CA, USA*.
- I. Kim, J. Shim, J. Lim, J. Jeong, B. -H. Kim, S. -H. Kim\*. "Highly-Sensitive Free-Standing Waveguide-Integrated Bolometer on Germanium-on-Insulator Platform for Mid-Infrared on-Chip Spectroscopy". *2024 International Electron Devices Meeting (IEDM), 2024/12, San Francisco, CA, USA*.
- S. -H. Kuk, B. -H. Kim, Y. Park, K. Ko, H. -S. Hwang, D. Lee, B- J. Cho, J. -H. Han, S. -H. Kim\*. "Superior QLC Retention (10 years, 85°C) and Record Memory Window (12.2 V) by Gate Stack Engineering in Ferroelectric FET: from “MIFIS” to “MIKFIS". *2024 International Electron Devices Meeting (IEDM), 2024/12, San Francisco, CA, USA*.
- S. -H. Kim\*, S. -K. Kim, H. -R. Lim, J. Jeong, J. Jeong, Y. Park, Y. Kim, B. -J. Cho. "Heterogeneous 3D CFET with Ge nanosheet channel". *ECS Prime, 2024/10, Hawai, US*.
- S. -H. Kim\*. "Single crystalline semiconductor oscillator for Oscillator-based computing". *International Conference on IC Design and Technology (ICICDT), 2024/9, Singapore*.
- H. -S. Kim, J. Park, W. Baek, D. -M. Geum, S. -H. Kim\*. "Demonstration of Vertically Stacked Full-Color Micro-LED using CMOS Compatible Oxide Wafer-Bonding Technology". *International Meeting on Information Display (IMID), 2024/8, Bexco, Korea (Best Poster Paper Award)*.
- S. -H. Kim\*. "Single crystalline semiconductor oscillator for Oscillator-based computing". *Device Research Conference (DRC), 2024/6, UMD, US*.
- S. -K. Kim, H. -R. Lim, J. Jeong, Y. Park, J. Park, S. Park, J. Park, D. Ha, B. -J. Cho, S. -H. Kim\*. "Ge(110) GAA Nanosheet / Si(100) Tri-gate Nanosheet Monolithic CFETs Featuring Record-high Hole Mobility". *Symposium on VLSI Technology and Circuits, 2024/6, Hawai, US*.
- N. Rheem+, J. Jeong+, Y. -J. Suh, C. -J. Lee, B. -H. Kim, J. -P. Kim, S. -K. Kim, H. -R. Lim, J. Kim, D. -W.Ahn, J. -H. Han, J. Lee, S. -H. Kim\*. "First Heterogeneous and Monolithic 3D (HM3D) Integration of InGaAs HEMTs and InP/InGaAs DHBTs on Si CMOS for Next-Generation Wireless Communication". *Symposium on VLSI Technology and Circuits, 2024/6, Hawai, US*.
- M. Lee, S. Kim, Y. Shin, IJ. Lim, S. -H. Kim, S. Kim\*. "Design on polarization-independent Germanium-on-Insulator Bragg filter". *IEEE Silicon Photonics Conference, 2024/4, Yokohama, Japan*.
- Y. Shin, J. Lim, S. -H. Kim, S. Kim\*. "Numerical study on thickness-dependent crosstalk optimization in Germanium-on-Insulator platform". *IEEE Silicon Photonics Conference, 2024/4, Yokohama, Japan*.
- Y. Shin, J. Lim, S. -H. Kim, S. Kim\*. "Crosstalk suppression in germanium-on-insulator platform using subwavelength gratings for mid-infrared photonics". *SPIE, 2024/1, San Francisco, US*.
- W. -J. Baek, J. Park, H. -S. Kim, D. -M. Geum, S. -H. Kim\*. "Carrier localization induced size-immunity behavior of green InGaN/GaN micro-light-emitting diodes". *SPIE, 2024/1, San Francisco, US*.

**2023**

- J. Lim, J. Shim, I. Kim, S. -H. Kim\*. "Experimental demonstration of microring resonator based on Germanium-on-insulator platform at mid-infrared range". *Photonics Research 11, p. A80 (2023)*.
- B- H. Kim, S. -H. Kuk, S. -K. Kim, J. -P. Kim, Y. -J. Suh, J. Jeong, C. -J. Lee, D. -M. Geum, Y. -J. Yoon, S. -H. Baek, S. -H. Kim\*. "Low Operating Voltage and Immediate Read-After-Write of HZO-Based Si Ferroelectric Field-Effect Transistors with High Endurance and Retention Characteristics". *Advanced Electronic Materials, 2300327 (2023)*.
- M. Park, J. Song, J. Jeong, J. -T. Lim, J. -H. Song, W. -C. Lee, G. Sim, H. Cho, D. Yoo, M. Kang, H. Ko, J. Lee, K. Yang, C. -Y. Kim, Y. Kim, W. -S. Sul, S. -H. Kim, J. Lee\*. "200-mm Si CMOS Process-Compatible Integrated Passive Stack for Millimeter-Wave Monolithic 3-D integration". *IEEE Transactions on Electron Devices 70, p. 5257 (2023)*.
- S. -H. Kuk, S. Han, B. -H. Kim, J. -P. Kim, S. -K. Kim, S. -Y. Ahn, M. Park, J. -H. Han\*, S. -H. Kim\*. "Examination of Ferroelectric FET for “Cold” Nonvolatile Memory". *IEEE Transactions on Electron Devices 70, p. 4122 (2023)*.
- J. Jeon+, S. -H. Kuk+, A. -J. Cho, S. -H. Beak, S. -H. Kim\*, S. -K. Kim\*. "Memory window enhancement in n-type ferroelectric field-effect transistors by engineering ozone exposure in atomic layer deposition of HfZrOx films". *Applied Physics Letters 122, 232906 (2023)*.
- J. Lim, J. Shim, I. Kim, S. -K. Kim, H. -R. Lim, S. -Y. Ahn, J. Park, D. -M. Geum, S. -H. Kim\*. "Low-Loss and High-Confinement Photonic Platform based on Germanium-on-Insulator at Mid-Infrared Range for Optical Sensing". *IEEE Journal of Lightwave Technology 41, p. 2824 (2023) (Supplementary material)*.
- B. -H. Kim, S. -H. Kuk, S. -K. Kim, J. -P. Kim, Y. -J. Suh, J. Jeong, D. -M. Geum, S. -H. Baek, S. -H. Kim\*. "Effect of Scandium Insertion into the Gate Stack of Ferroelectric Field-Effect Transistors". *IEEE Transactions on Electron Devices 70, p. 1996 (2023)*.
- J. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, S.- H. Kim\*. "Effects of Back Metal on the DC and RF Characteristics of 3D Stacked InGaAs RF Devices for Monolithic 3D RF Applications". *IEEE Electron Device Letters 44, p. 598 (2023)*.
- B- H. Kim, S. -H. Kuk, S. -K. Kim, J. -P. Kim, Y. -J. Suh, J. Jeong, D. -M. Geum, S. -H. Baek, S. -H. Kim\*. "Oxygen Scavenging in HfZrOx-based n/p-FeFETs for Switching Voltage Scaling and Endurance/Retention Improvement". *Advanced Electronic Materials, 2101257 (2023)*.
- W. -J. Baek, J. -H. Park, J. Shim, B. -H. Kim, S. Park, H. -S. Kim, D. -M. Geum\*, and S. -H. Kim\*. "Ultra-Low-Current Driven InGaN Blue Micro Light-Emitting Diodes for Electrically Efficient and Self-Heating Relaxed Microdisplay". *Nature communications 14, 1386 (2023)*.
- J. -P. Kim, S. -K. Kim, S. Park, S- H. Kuk, T. Kim, B. -H. Kim, S. -H. Ahn, Y. -H. Cho, Y. Jeong, S. -Y. Choi, S.- H. Kim\*. "Dielectric-Engineered High-speed, Low-power, Highly-reliable Charge Trap Flash-based Synaptic Device for Neuromorphic Computing Beyond Inference". *Nano Letters 23, p. 451 (2023)*.
- T. Jin†, S. -H. Kim†, J. -H. Han†, D. -H. Ahn, S. -U. An, T. -H. Noh, X. Sun, C. -J. Kim, J. Park, and Y. Kim\*. "Demonstration of programmable light intensity of a micro-LED with a Hf-based ferroelectric ITZO TFT for Mura-free displays". *Nanoscale Advances 5, p. 1316 (2023)*.
- S. -H. Kuk, S. Han, D. -H. Lee, B. -H. Kim, J. -S. Shim, M. Park, J. -H. Han, S. -H. Kim\*. "Logic and Memory Ferroelectric Field-Effect-Transistor Using Reversible and Irreversible Domain Wall Polarization". *IEEE Electron Device Letters 44, p. 36 (2023)*.
- S. -H. Kuk, B. -H. Kim, Y. Park, H. -S. Hwang, J. -H. Han, B. -J. Cho, B. -C. Jang, and S. -H. Kim\*. "Proposal of Block Erase and Verify Schemes for Ferroelectric NAND: Overcoming Critical Challenges from Threshold Voltage Polarity". *International Memory Workshop, 2023/5, Monterey, US*.
- J. Jang, I. -S. Kang, S. Jung, H. Cho, S. -H. Kim\*. "Wavelength – Tunable Grating – Resonance InGaAs Narrowband Photodetector with Infrared Optical PCM, Antimony Triselenide (Sb2Se3)". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- J. -P. Kim†, H. -W. Kim†, J. Jeong, J. Park, S. -K. Kim, J. Kim, J. Woo\*, S. -H. Kim\*. "BEOL-compatible 4F2 Single Crystalline Semiconductor Oscillator for Low-power and Large-scale Oscillatory Neural Network Hardware". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- J. Shim, J. Lim, I. Kim, S. -K. Kim, S. -Y. Ahn, J. Park, J. Jeong, B. -H. Kim, S. Lee, J. An, D. -M. Geum, S. -H. Kim\*. "Fully CMOS-Compatible Room-Temperature Waveguide-Integrated Bolometer Based on Germanium-on-Insulator Platform at Mid-Infrared Operating Beyond 4 μm". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- J. Jeong, S. -J. Choi, J. Shim, E. Kim, S. -K. Kim, B. -H. Kim, J. -P. Kim, Y. -J. Suh, W. -J. Beak, D. -M. Geum, Y. Koh, D. Kim, S. -H. Kim\*. "Thermal Management in Multi-Finger GaN-on-Si HEMTs: Understanding and Mitigating Self-Heating and Thermal Crosstalk for Enhanced Device Reliability". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- J. Jeong, J. Kim, J. -S. Lee, , Y. -J. Suh, N. Rheem, S. -K. Kim, J. Park, B. -H. Kim, J. -P. Kim, S. -Y. Park, S. -H. Kim\*. "Impact of the channel thickness fluctuation on the subthreshold swing of InGaAs HEMTs at cryogenic temperature down to 4 K for ultra-low power LNAs". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- S. -K. Kim, H. -R. Lim, J. Shim, W. Baek, S. Kim, Y. Park, J. Jeong, J. Lim, J. -P. Kim, J. Jeong, B. -H. Kim, D. -M. Geum, B. -J. Cho, S. -H. Kim\*. "Role of Inter-Layer Dielectric on the Electrical and Heat Dissipation Characteristics in the Heterogeneous 3D Sequential CFETs with Ge pFETs on Si nFETs". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- B. -H. Kim, S. -K. Kim, S. -H. Kuk, Y. J. Seo, J. Jeong, J. -P. Kim, S. -H. Kim\*. "IL Scavenging and Recovery Strategies to Improve the Performance and Reliability of HZO-Based FeFETs". *2023 International Electron Devices Meeting (IEDM), 2023/12, San Francisco, CA, USA*.
- S. -H. Kim\*. "Cryogenic InGaAs HEMTs for LNA and routing circuits in Quantum Computing". *International Conference on IC Design and Technology (ICICDT), 2023/9, Tokyo, Japan*.
- S. -H. Kim\*, J. Jeong, S. -K. Kim, Y. -J. Suh, J. Lee, J. Choi, J. Park, J. -P. Kim, B. -H. Kim, Y. Jo, S. -Y. Park, J. Kim. "Cryogenic InGaAs HEMTs for LNA and routing circuits in Quantum Computing". *2023 International conference on Solid State Devices and Materials (SSDM), 2023/9, Nagoya, Japan*.
- S. -H. Kim\*, J. Park, W. Baek, D. -M. Geum. "Monolithic 3D integration of high-resolution MicroLED pixels on CMOS backplane and Re-consideration of the epitaxial structure of LEDs". *International Meeting on Information Display (IMID), 2023/8, Bexco, Korea*.
- W. Baek, J. Park, H. -S. Kim, D. -M. Geum, S. -H. Kim\*. "Surface Current Analysis on Lateral Diffusions of Carriers in Micro-light-emitting Diodes". *International Meeting on Information Display (IMID), 2023/8, Bexco, Korea (Best Poster Paper Award)*.
- J. Jeong, S. -K. Kim, Y. -J. Suh, J. Lee, J. Choi, J. Park, J. -P. Kim, B. -H. Kim, Y. Jo, S. -Y. Park, J. Kim, S. -H. Kim\*. "Cryogenic RF Transistors and Routing Circuits Based on 3D Stackable InGaAs HEMTs with Nb Superconductors for Large-Scale Quantum Signal Processing". *Symposium on VLSI Technology and Circuits, 2023/6, Kyoto, Japan*.
- S.- H. Kuk, J. -H. Han\*, B. -H. Kim, J. -P. Kim, S. -H. Kim\*. "Strategy for 3D Ferroelectric Transistor: Critical Surface Orientation Dependence of HfZrOx on Si". *Symposium on VLSI Technology and Circuits, 2023/6, Kyoto, Japan*.
- S.- H. Kuk, J. -H. Han, B. -H. Kim, J. -P. Kim, S. -H. Kim\*. "Proposal of P-Channel FE NAND with High Drain Current and Feasible Disturbance for Next Generation 3D NAND". *International Memory Workshop, 2023/5, Monterey, US (Best Student Paper Award)*.
- S. -Y. Ahn, J. Lim, J. H. Eom, S. -M. Ryu, H. -J. Lee, Y. -H. Kim, S. -H. Kim\*. "Broadband and high-quantum-efficiency LWIR T2SL nBn detector with guided-mode-resonance structure". *SPIE DCS, 2023/4, Orlando, US*.

**2022**

- J. –S. Shim, J. -H. Lim, D. -M. Geum, J. -B. You, H. Yoon, J. Kim, W. -J. Baek, I. Kim, J. -H. Han, S. -H. Kim\*. "High-sensitivity waveguide-integrated bolometer based on free-carrier absorption for Si photonic sensors". *Optics Express 23, p. 42663 (2022)*.
- J. -P. Kim+, J. Sim+, P. Bidenko, D. -M. Geum, S. -K. Kim, J. Shim, J. Kim\*, S. -H. Kim\*. "Capacitor-less 4F2 DRAM using Vertical InGaAs Junction for Ultimate Cell Scalability". *IEEE Electron Device Letters 43, p. 1834 (2022)*.
- J. -Y. Jeong+, D. -M. Geum+, S. -H. Kim\*. "Heterogeneous and Monolithic 3D Integration Technology for Mixed-Signal ICs". *Electronics 11, 3013 (2022)*.
- B. -H. Kim, S. -H. Kuk. S. -K. Kim, J. -P. Kim, D. -M. Geum, S. -H. Baek, and S. -H. Kim\*. "Oxygen Scavenging of HfZrO2-Based Capacitors for Improving Ferroelectric Properties". *Nanoscale Advances 4, p. 4114 (2022)*.
- P. Bidenko, S. Ahn, K. -K. Kang, H. -J. Lee, Y. H. Kim, S. -H. Kim\*. "The Atomic-scale Mapper for Superlattice Photodetectors Analysis". *Optics Express 30, p. 27868 (2022)*.
- J.- Y. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, D. Kim, E. Jo, H. Jeong, J. Park, J. -H. Jang, S. Choi, I. Kwon\*, S. -H. Kim\*. "Heterogeneous and monolithic 3D integration of III-V-based RF devices on Si CMOS circuits". *ACS Nano 16, p. 9031 (2022)*.
- J. Lim, J. -S. Shim, D. -M. Geum, and S. -H. Kim\*. "Experimental demonstration of Germanium-on-silicon slot waveguides at mid-infrared wavelength". *IEEE Photonics Journal 14, 5828709 (2022)*.
- Y. Kim, D. Yudistira, B. Kunert, M. Baryshnicova, R. Alcotte, C. I. Ozdemir, S. -H. Kim, S. Lardenois, P. Verheyen, J. Van Campenhout, and M. Pantouvaki. "Monolithic GaAs/Si V-groove depletion-type optical phase shifters integrated in a 300 mm Si photonics platform". *Photonics Research 10, p. 1509 (2022)*.
- J. –S. Shim, J. -H. Lim, D. -M. Geum, J. -B. You, H. Yoon, J. Kim, W. -J. Baek, J. -H. Han, S. -H. Kim\*. "TiOx/Ti/TiOx Tri-layer Film-based Waveguide Bolometric Detector for On-chip Si Photonic Sensor". *IEEE Transactions on Electron Devices 69, p. 2151 (2022) (Special issue for the extended paper of International Electron Devices Meeting (IEDM) 2021)*.
- S. –H. Kuk, S. -M. Han, B. -H. Kim, S. -H. Baek, J. -H. Han, S. -H. Kim\*. "An Investigation of HZO-based n/p-FeFET Operation Mechanism and Improved Device Performance by Electron De-trapping Mode". *IEEE Transactions on Electron Devices 69, p. 2080 (2022) (The extended paper of International Electron Devices Meeting (IEDM) 2021)*.
- J. -H. Park, W. -J. Baek, D. -M. Geum\*, S. -H. Kim\*. "Understanding the sidewall passivation effects in AlGaInP/GaInP micro-LED". *Nanoscale Research Letters 17, 29 (2022)*.
- J. -K. Han+, Y. -W. Chung+, J. Sim, J. -M. Yu, G. -B. Lee, S. -H. Kim, Y. -K. Choi\*. "Mnemonic-Opto-Synaptic Transistor for In-sensor Vision system". *Scientific Reports 12, 1818 (2022)*.
- J. Jang, J. Shim, J. Lim, G. -C. Park, J. Kim, D. -M. Geum, S. -H. Kim\*. "Grating-resonance InGaAs narrowband photodetector for multispectral detection in NIR-SWIR region". *2022 International Electron Devices Meeting (IEDM), 2022/12, San Francisco, CA, USA*.
- S. -K. Kim, H. -R. Lim, J. -J. Jeong, S. -W. Lee, J. -P. Kim, J. -Y. Jeong, B. -H. Kim, S. -Y. Ahn, Y. -K. Park, D. -M. Geum, Y. Kim, Y. -K. Baek, B. -J. Cho, S. -H. Kim\*. "Heterogeneous 3D Sequential CFET with Ge (110) Nanosheet p-FET on Si (100) bulk n-FET by Direct Wafer Bonding". *2022 International Electron Devices Meeting (IEDM), 2022/12, San Francisco, CA, USA*.
- J. Lim, J. Shim, I. Kim, S. -K. Kim, H. -R. Lim, S. -Y. Ahn, J. Park, D. -M. Geum, S. -H. Kim\*. "Biochemical spectroscopy based on germanium-on-insulator platform for mid-infrared optical sensor". *2022 International Electron Devices Meeting (IEDM), 2022/12, San Francisco, CA, USA*.
- J. Jeong, S. -K. Kim, J. Kim, J. -S. Lee, J. -P. Kim, B. -H. Kim, Y. -J. Suh, D. -M. Geum, S. -Y. Park, S. -H. Kim\*. "3D Stackable Cryogenic InGaAs HEMT-Based DC and RF Multiplexer/Demultiplexer for Large-Scale Quantum Computing". *2022 International Electron Devices Meeting (IEDM), 2022/12, San Francisco, CA, USA*.
- S. -H. Kim\*. "Monolithic 3D III-V HEMT for future communication and quantum computing". *International Conference on Electronic Materials and Nanotechnology for Green Environment (ENGE), 2022/11, Jeju, Korea*.
- S. -H. Kim\*. "Monolithic 3D III-V HEMT for future communication and quantum computing". *International Conference on IC Design and Technology (ICICDT), 2022/9, Hanoi, Vietnam*.
- J. Shim, J. Lim, D. -M. Geum, J. -B. You, H. Yoon, J. -P. Kim, W. -J. Baek, J. -H. Han, and S. -H. Kim\*. "Free carrier absorption-assisted photodetection using a waveguide-integrated bolometer with flat spectral response for integrated optical sensors". *SPIE Optical Engineering + Applications, 2022/8, San Diego, USA*.
- T. Jin, C. -J. Kim, T. -H. Noh, S. Xinkai, J. -H. Han, S. -H. Kim, Y. Kim\*. "A New Approach to Compensate Threshold Voltage Variation in the Current-driving Display Using a Ferroelectric TFT". *International Meeting on Information Display (IMID), 2022/8, Coex, Korea*.
- J. -H. Lim, J. Shim, S. -K. Kim, H. Lim, S.- W. Lee, D. -M. Geum, S. -H. Kim\*. "Low-loss Germanium-on-insulator passive waveguides for mid-infrared photonics platform". *Optical Sensors and Sensing Congress, 2022/7, Vancouver British Columbia, Canada*.
- S. -H. Kim\*, J. Lim, J. -S. Shim, D. -M. Geum. "Ge-based Mid-infrared integrated photonics platform for Sensing". *Device Research Conference (DRC), 2022/6, Ohio, US*.
- J. Park+, D. -M. Geum+, W. Baek, J. Shieh, S. -H. Kim\*. "Monolithic 3D sequential integration realizing 1600-PPI red micro-LED display on Si CMOS driver IC". *Symposium on VLSI Technology and Circuits, 2022/6, Hawai, US*.
- J. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, J. Lee, S. -Y. Park, S. -H. Kim\*. "3D Stackable cryogenic InGaAs HEMTs for heterogeneous and monolithic 3D integrated highly scalable quantum computing systems". *Symposium on VLSI Technology and Circuits, 2022/6, Hawai, US*.
- D. -M. Geum+, J. Lim+, J. Jang, S. Ahn, S. -K. Kim, J. Shim, B. -H. Kim, J. Park, W. -J. Baek, J. Jeong, S. -H. Kim\*. "A sub-micron-thick InGaAs broadband (400-1700 nm) photodetectors with a high external quantum efficiency (>70%)". *Symposium on VLSI Technology and Circuits, 2022/6, Hawai, US*.
- W. -J. Baek, D. -M. Geum, J. Park, S. -H. Kim\*. "Enhanced External Quantum Efficiency in the Low-Current Region Using Three Terminal GaN-based Blue Micro-Light-Emitting Diodes". *SID Display Week, 2022/5, San Jose, CA, USA*.
- J. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, S. -H. Kim\*. "Heat management in monolithic 3D RF platform". *IEEE Electron Devices Technology and Manufacturing Conference (EDTM), 2022/3, Virtual*.
- S. -Y. Ko, B. -W. Lee, H. -J. Kim, S. -I. Na, J. -B. Kim, P. Bidenko, S. -H. Kim, Y. -H. Kim. "Comparison of InGaAs and type-II superlattice based extended SWIR detectors". *SPIE DCS, Orlando, Florida, USA*.

**2021**

- J. Jang, D. -M. Geum, S. -H. Kim\*. "Broadband Au/n-GaSb Schottky photodetector array with a spectral range from 300 nm to 1700 nm". *Optics Express 29, p. 38894 (2021)*.
- H. -J. Lee, A. Jang, Y. H. Kim, H. Jung, P. Bidenko, S. -H. Kim, M. Kim, J. Nah\*. "Comparative advantages of type-II superlattice barrier over AlGaSb barrier for enhanced performance of InAs/GaSb LWIR nBn photodetectors". *Optics Letters 46, p. 3877 (2021)*.
- Y. Kim, J. -H. Han\*, D. -H. Ahn, S. -H. Kim. "Heterogeneously-integrated optical phase shifters for next-generation modulators and switches on a Silicon photonics platform: A review". *Micromachines 12, p. 625 (2021)*.
- J. Shim, J. Lim, D. -M. Geum, B. H. Kim, S. -Y. Ahn, S. -H. Kim\*. "Tailoring bolometric properties of a TiOx/Ti/TiOx tri-layer film for integrated optical gas sensors". *Optics Express 29, p. 18037 (2021)*.
- D. -M. Geum, S. -K. Kim, H. -R. Lim, J. Park, J. Jeong, J. H. Han, W. J. Choi, H. -J. Kim, S. -H. Kim\*. "Electrical analysis for wafer-bonded interfaces of p+GaAs/n+InGaAs and p+InGaAs/n+InGaAs". *IEEE Electron Device Letters 41, p. 800 (2021)*.
- W. Kim^, P. Bidenko^, J. Kim, J. Sim, J. -K. Han, S. -K. Kim, D. -M. Geum, S. -H. Kim\*, Y. -K. Choi\*. "Vertical InGaAs Biristor for sub-1V Operation". *IEEE Electron Device Letters 42, p. 681 (2021)*.
- J. Jang^, J. Song^, S. S. Lee, S. Jeong, B. J. Lee\*, S. -H. Kim\*. "Analysis of temperature-dependent I-V characteristics of the Au/n-GaSb Schottky diode". *Materials Science in Semiconductor Processing 131, 105882 (2021)*.
- J. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, J. Park, J. -H. Jang, S. -H. Kim\*. "Stackable InGaAs-On-Insulator HEMTs for Monolithic 3D Integration". *IEEE Transactions on Electron Devices 68, p. 2205 (2021)*.
- D. -M. Geum^, S. Kim^, J. Khym, J. Lim, S. -K. Kim, S. -Y. Ahn, T. S. Kim, K. Kang\*, S. -H. Kim\*. "Arrayed MoS2-In0.53Ga0.47As van der Waals Heterostructure for High-speed and Broadband Detection from Visible to Shortwave-infrared Light". *Small 17, 2007357 (2021)*.
- S. -H. Kim^, I. -P. Roh^, J. -H. Han, D. -M. Geum, S. K. Kim, S. -S. Kang, H. -K. Kang, W. C. Lee, S. K. Kim, D. K. Hwang, Y. H. Song\*, J. D. Song\*. "High hole mobility and low leakage thin-body (In)GaSb p-MOSFETs grown on high-bandgap AlGaSb". *IEEE Journal of the Electron Device Society 9, p. 42 (2021)*.
- S. –H. Kuk, S. -M. Han, B. -H. Kim, S. -H. Baek, J. -H. Han, S. -H. Kim\*. "Comprehensive Understanding of the HZO-based n/pFeFET Operation and Device Performance Enhancement Strategy". *2021 International Electron Devices Meeting (IEDM), 2021/12, San Francisco, CA, USA*.
- J. –Y. Jeong, S. -K. Kim, J. Kim, D. -M. Geum, S. -H. Kim. "Monolithic 3D Integrated InGaAs HEMTs on Si for Next-Generation Communication: Record fMAX and Relaxed Self-Heating of Top Devices by a Novel M3D Structure". *2021 International Electron Devices Meeting (IEDM), 2021/12, San Francisco, CA, USA*.
- J. –S. Shim, J. -H. Lim, D. -M. Geum, J. -B. You, H. Yoon, J. Kim, W. -J. Baek, J. -H. Han, S. -H. Kim\*. "TiOx/Ti/TiOx Tri-layer Film-based Waveguide Bolometric Detector for On-Chip Si Photonic Sensors". *2021 International Electron Devices Meeting (IEDM), 2021/12, San Francisco, CA, USA*.
- J. –K. Han+, J. Sim+, D. -M. Geum, S. -K. Kim, J. -M. Yu, J. Kim, S. -H. Kim\*, Y. -K. Choi\*. "3D Stackable Broadband Photoresponsive InGaAs Biristor Neuron for a Neuromorphic Visual System with Near 1 V Operation". *2021 International Electron Devices Meeting (IEDM), 2021/12, San Francisco, CA, USA*.
- J. –S. Shim, J. -H. Lim, D. -M. Geum, J. -B. You, H. Yoon, J. Kim, W. -J. Baek, J. -H. Han, S. -H. Kim\*. "Bolometric photodetection with a TiOx/Ti/TiOx tri-layer film-based waveguide for on-chip silicon photonic sensors". *International Conference on Advanced Materials and Devices, 2021/12, Jeju, Korea*.
- D. -S. Lee\*, S. -H. Kim\*. "Monolithic integration of AlGaInP red and InGaN blue/green LEDs". *Semiconductors and Semimetals, Elsevier Inc., in press (2021)*.

## 수상과 선정

연구실 수상 글 10건이다. 게시일과 수상·선정 연도를 구분했으며, 수상·선정 연도는 2023–2025년이고 게시일은 2023–2026년이다.[^award121][^award122][^award123][^award124][^award125][^award126][^fellowship][^award127][^award128][^award129]

- 2026-01-29 게시 · 2025년 수상·선정 · Chan Jik Lee가 KCS 2025 Samsung Paper Award를 받았다.
- 2026-01-27 게시 · 2024년 수상·선정 · Seong Kwang Kim이 IEEE 2024 Paul Rappaport Award를 받았다.
- 2025-09-11 게시 · 2025년 수상·선정 · Juhyuk Park가 IMID 2025 Best Poster Paper Award를 받았다.
- 2025-06-03 게시 · 2025년 수상·선정 · Inki가 2025 COOC Paper Award를 받았다.
- 2025-02-17 게시 · 2025년 수상·선정 · Dr. Joonsup Shim이 KCS 2025 Best Paper Award를 받았다.
- 2024-10-21 게시 · 2024년 수상·선정 · Hyun Soo가 IMID 2024 Best Poster Paper Award를 받았다.
- 2024-03-26 게시 · 2023년 수상·선정 · Jeong Jae Yong이 2023 IEEE Electron Device Society (EDS) PhD Student Fellowship에 선정되었다.
- 2024-02-07 게시 · 2024년 수상·선정 · Joonsup이 Samsung Humantech Paper Awards 2024에서 동상을 받았다.
- 2023-12-04 게시 · 2023년 수상·선정 · Inki가 Photonics Conference 2023 Best Paper Award를 받았다.
- 2023-10-25 게시 · 2023년 수상·선정 · Woo Jin이 IMID 2023 Best Poster Paper Award를 받았다.

## 연락과 위치

- 연구실: 대전광역시 유성구 대학로 291 KAIST 전기및전자공학부 E3-2, 1230호[^contact]
- 연구실 전화: 042-350-7552[^contact]
- 교수 사무실·연락처: 전기및전자공학부동(E3-2) 1225호, 7452[^ee]
- 교수 이메일: shkim.ee@kaist.ac.kr[^ee]
[^home]: 3D-OEDL 첫 화면, 연구실 소개와 News 수상 요약. <https://www.3doedl.com/> (관측 2026-10-31).
[^pi]: Principal Investigator, 김상현 교수 학력·경력. <https://www.3doedl.com/principal-investigator> (관측 2026-10-31).
[^ee]: KAIST 전기및전자공학부 전임교수 명단, 김상현 부교수 항목. <https://ee.kaist.ac.kr/professor-s1/> (관측 2026-10-31).
[^stack]: III-V & Ge for Power, RF, Logic devices, 층 전사·접합과 모놀리식 3차원 집적 연구 소개. <https://www.3doedl.com/monolithic-3d> (관측 2026-10-31).
[^compute]: Next Generation Computing, 차세대 트랜지스터와 입체 적층 신경세포·시냅스 소자 연구 소개. <https://www.3doedl.com/next-generation-computing> (관측 2026-10-31).
[^display]: MicroLED Display, 적층 RGB 화소와 구동 회로 집적 연구 소개. <https://www.3doedl.com/microled> (관측 2026-10-31).
[^imager]: IR Photodetector & Image Sensor, 광 반응 시냅스와 가시광·적외선·초분광 영상 센서 연구 소개. <https://www.3doedl.com/thin-film-imager> (관측 2026-10-31).
[^photonics]: Near to Mid-IR Photonics, 게르마늄 광회로 기반 기체 센서 연구 소개. <https://www.3doedl.com/mid-ir-photonics> (관측 2026-10-31).
[^researchers]: Researchers, 연구원 2명. <https://www.3doedl.com/post-doc-researchers> (관측 2026-10-31).
[^phd]: Ph.D Candidates, 박사과정 10명. <https://www.3doedl.com/phdcandidates> (관측 2026-10-31).
[^ms]: M.S Candidates, 석사과정 16명. <https://www.3doedl.com/mscandidates> (관측 2026-10-31).
[^alumni]: Alumni, 박사·박사후 구획 13명과 석사 구획 10명. <https://www.3doedl.com/alumni> (관측 2026-10-31).
[^j2026]: Journal papers published in 2026, 15편. <https://www.3doedl.com/copy-of-2025> (관측 2026-10-31).
[^j2025]: Journal papers published in 2025, 15편. <https://www.3doedl.com/2025> (관측 2026-10-31).
[^j2024]: Journal papers published in 2024, 17편. <https://www.3doedl.com/2024> (관측 2026-10-31).
[^j2023]: Journal papers published in 2023, 13편. <https://www.3doedl.com/copy-of-2022> (관측 2026-10-31).
[^j2022]: Journal papers published in 2022, 12편. <https://www.3doedl.com/publication2022> (관측 2026-10-31).
[^j2021]: Journal papers published in 2021, 11편. <https://www.3doedl.com/publication2021> (관측 2026-10-31).
[^conference]: Conferences, 2009–2026년 학회 목록. *는 Corresponding authorship으로 설명. <https://www.3doedl.com/conferences> (관측 2026-10-31).
[^book]: Book Chapters, 2021년 책 장 1건(in press). <https://www.3doedl.com/book-chapters> (관측 2026-10-31).
[^fellowship]: IEEE PhD fellowship 2023, 2024년 3월 26일 게시. <https://www.3doedl.com/post/ieee-phd-fellowship-2023> (관측 2026-10-31).
[^contact]: Contact Information, 연구실 위치·전화. <https://www.3doedl.com/contact> (관측 2026-10-31).
[^award121]: KCS 2025 Samsung Paper Award. <https://www.3doedl.com/post/kcs-2025-samsung-paper-award> (관측 2026-10-31).
[^award122]: IEEE 2024 Paul Rappaport Award. <https://www.3doedl.com/post/ieee-2024-paul-rappaport-award> (관측 2026-10-31).
[^award123]: IMID 2025 Best Poster Paper Award. <https://www.3doedl.com/post/imid-2025-best-poster-paper-award> (관측 2026-10-31).
[^award124]: 2025 COOC Paper Award. <https://www.3doedl.com/post/2025-cooc-paper-award> (관측 2026-10-31).
[^award125]: KCS 2025 Best Paper Award. <https://www.3doedl.com/post/kcs-2025-best-paper-award> (관측 2026-10-31).
[^award126]: IMID 2024 Best Poster Paper Award. <https://www.3doedl.com/post/imid-2023-best-poster-paper-award> (관측 2026-10-31).
[^award127]: Samsung Humantech Paper Awards 2024. <https://www.3doedl.com/post/samsung-humantech-paper-awards-2024> (관측 2026-10-31).
[^award128]: Photonics Conference 2023 Best Paper Award. <https://www.3doedl.com/post/photonics-conference-2023-best-paper-award> (관측 2026-10-31).
[^award129]: IMID 2023 Best Poster Paper Award. <https://www.3doedl.com/post/imid-best-paper-award> (관측 2026-10-31).
[^p1]: J. P. Kim 외, S. Kim, Advanced Science 12, 2413247 (온라인 2025-03-16). <https://doi.org/10.1002/advs.202413247> 초록 기준(출판사 논문 페이지). 초록 원문 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202413247> (관측 2026-10-31).
[^p2]: J. Jeong 외, S. Kim, ACS Nano 16, 9031-9040 (온라인 2022-04-19). <https://doi.org/10.1021/acsnano.2c00334> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/adpr.202000051|10.1002/aelm.202300327|10.1002/lpor.202402116|10.1021/acsnano.2c00334|10.1021/acssensors.4c00941|10.1038/s41377-024-01652-6> (관측 2026-10-31).
[^p3]: H. s. Kim 외, S. H. Kim, Laser & Photonics Reviews 19, 2402116 (온라인 2025-04-19). <https://doi.org/10.1002/lpor.202402116> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/lpor.202402116> (관측 2026-10-31).
[^p4]: I. Kim 외, S. Kim, ACS Sensors 9, 5116-5126 (온라인 2024-10-16). <https://doi.org/10.1021/acssensors.4c00941> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1002/adpr.202000051|10.1002/aelm.202300327|10.1002/lpor.202402116|10.1021/acsnano.2c00334|10.1021/acssensors.4c00941|10.1038/s41377-024-01652-6> (관측 2026-10-31).
[^p5]: D.-M. Geum 외, S. Kim, Light: Science & Applications 13, 311 (온라인 2024-11-15). <https://doi.org/10.1038/s41377-024-01652-6> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1038/s41377-024-01652-6> (관측 2026-10-31).
[^p6]: B. H. Kim 외, S. H. Kim, Advanced Electronic Materials 10, 2300327 (온라인 2023-10-16). <https://doi.org/10.1002/aelm.202300327> 초록 기준(Crossref 등록 초록). 초록 원문 <https://api.crossref.org/works/10.1002/aelm.202300327> (관측 2026-10-31).

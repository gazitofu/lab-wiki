# KAIST Power Electronics Lab.

**KAIST 전기및전자공학부 · 문건우 교수**

- 분야: 전력 변환 회로와 제어, 데이터센터 전원 장치, 전기차 전원과 배터리 충전, 무선 전력 수신, 위성 전원
- 대분야: 전기전자·반도체·광학, 에너지·환경·지구
- 태그: 전력전자 변환기·전력 변환 시스템[^research]
- 홈페이지: <https://sites.google.com/view/kaistpelab>
- 근거와 출처: [KAIST Power Electronics Lab. 근거 페이지](kaistpelab-sources.md)

> 전기를 기기에 필요한 형태로 바꾸는 회로와 제어 방법을 만들고, 데이터센터·전기차·배터리·위성의 전력 공급에 연결하는 연구실이다.[^research][^p2][^p4][^p8]

## 무엇을 연구하나

연구실은 전력전자(반도체 소자로 전기의 흐름과 형태를 바꾸고 제어하는 기술)를 다룬다. 전력은 단위 시간에 전달하거나 소비하는 에너지이고, 전압은 두 지점 사이에서 전하가 가진 전기적 에너지의 차이를 전하의 양으로 나눈 값이다. 전류는 단위 시간에 흐르는 전하의 양이다. 연구 소개는 데이터센터의 전원 장치 개발 이력에 Nvidia·AWS·Intel용 전원 장치를 제시하며, 전기차 전원, 배터리 관리, 소비자 전자기기, 항공우주·국방 전원, 재생에너지를 연구 갈래로 둔다.[^research] 연구실은 전력전자 변환기와 전력 변환 시스템의 회로·제어를 개발한다.[^p2][^p3]

첫 갈래는 **전원 회로의 손실과 잡음 저감**이다. 직류(흐르는 방향이 일정한 전류)를 다른 전압의 직류로 바꾸는 컨버터를 연구한다. 입력 전압에 따라 인덕터(전류 변화에 대응하는 자기장에 에너지를 저장하는 코일)의 특성을 조절해 효율과 입력 전류의 품질을 개선하거나, 결합 인덕터 정류기(자기적으로 연결된 코일을 사용해 전류를 한 방향으로 흐르게 하는 회로)로 공통 모드 잡음(여러 도선에 공통된 방향으로 나타나는 기준점 대비 전기적 흔들림)을 억제한다.[^p1][^p3] 데이터센터에서는 주 전원에 앞서 전압을 높여 조절하는 회로와 대기 전원 회로의 스위치를 통합하고, 켜져 있는 시간과 켜고 끄는 주기를 함께 조절하는 방법을 제안한다.[^p2]

둘째 갈래는 **배터리를 충전하고 모듈 사이의 상태를 맞추는 회로와 제어**다. 전기차의 여러 배터리 모듈(여러 배터리 셀을 묶은 조립 단위)에서 충전과 방전 양방향으로 모듈 간 균형을 맞추면서 저전압 전원을 공급하는 회로를 연구한다.[^p4] 저온에서는 역방향 펄스(일정 시간 동안 반대 방향으로 흐르는 전류)를 넣는 충전 방법과, 충전·방전이 반복되는 주파수(단위 시간에 반복되는 횟수)를 조절해 배터리 자체에서 열이 나도록 하는 방법을 제안한다.[^p5][^p6]

셋째 갈래는 **무선 전력 수신과 위성 전력 공급**이다. 무선 전력 수신기는 들어오는 주파수 대역에 맞춰 정류 동작을 자동으로 바꾸고, 별도 감지 회로나 외부 제어 신호 없이 서로 다른 대역의 무선 충전을 지원하도록 설계한다.[^p7] 저궤도 위성에서는 태양전지 전력 조절기의 직접 충전 제어를 제안하고, 무게·효율·신뢰성과 배터리 수명에 관련된 특성을 분석한다.[^p8]

## 주요 연구 주제

### 1. 전원 회로의 효율과 잡음

입력 전압 변화에 적응하는 가변 인덕터 제어와, 변압기(자기적으로 연결된 코일을 이용해 전압을 바꾸는 장치)에서 생기는 공통 모드 잡음을 상쇄하는 정류 회로를 연구한다. 출력 코일을 결합 인덕터로 바꾸는 방식으로 잡음 억제 회로를 구성한다.[^p1][^p3]

### 2. 데이터센터의 주 전원과 대기 전원 통합

데이터센터 직류 배전용 서버 전원에서 부스트 컨버터(입력보다 높은 직류 전압을 만드는 변환 회로)와 대기 전원 회로의 스위치를 통합한다. 두 출력 전압을 조절하면서 스위치를 켤 때 생기는 손실을 줄이는 회로 구조와 제어가 연구 대상이다.[^p2]

### 3. 전기차 배터리의 균등화와 저온 충전

배터리 모듈 간 균형을 맞추는 회로를 차량의 저전압 전원 회로와 합치고, 저온에서 배터리를 충전하거나 스스로 가열하는 전류 제어를 연구한다. 역방향 전류 펄스를 넣는 충전법과 충전·방전 주파수를 바꾸는 자기 발열법을 다룬다.[^p4][^p5][^p6]

### 4. 무선 충전 수신기와 위성 전원

서로 다른 주파수 대역을 지원하는 무선 충전 수신 회로와, 저궤도 위성의 태양전지에서 배터리로 전력을 공급하는 직접 충전 제어를 연구한다. 수신기 동작의 자동 전환과 위성 전력 조절기의 무게·효율·신뢰성이 각각의 설계 과제다.[^p7][^p8]

## 대표 논문

문건우 교수가 저자로 참여한 KAIST 재직 시기의 논문에서 전원 회로·데이터센터·배터리·무선 전력·위성 전원 갈래를 골랐다. 연도는 초록과 함께 게시된 서지의 출판 연도다. 「쉽게 말하면」 칸은 각 논문의 초록만을 근거로 썼다.

| 번호 | 연도 | 논문·발표처 | 주요 저자 | 쉽게 말하면 |
|---|---|---|---|---|
| 1 | 2025 | [Critical mode boost power factor correction converter with high efficiency and reduced input current distortion using variable inductor](https://doi.org/10.1007/s43236-025-01235-7) · Journal of Power Electronics[^p1] | 1저자 Cheon-Yong Lim, 마지막 저자 Gun-Woo Moon | 입력 전압에 따라 코일의 전류 변화 억제 특성을 바꾼다. 정격 입력에서는 스위칭 빈도를 낮춰 효율과 전류 품질을 개선하고, 다른 입력 조건에서는 사람이 듣는 소음이 생기는 문제를 피하도록 설계했다. |
| 2 | 2024 | [A High Efficiency Boost Preregulator Merging With an Asymmetric LLC Standby Converter in DC Power Distribution System for Data Center](https://doi.org/10.1109/tpel.2024.3379382) · IEEE Transactions on Power Electronics[^p2] | 1저자 Moo-Hyun Park, 마지막 저자 Gun-Woo Moon | 서버의 주 전원 앞단과 대기 전원 회로가 스위치를 함께 쓰게 했다. 두 출력 전압을 조절하고 스위치를 켤 때의 손실을 줄이는 구조를 제안하고 시제품으로 확인했다. |
| 3 | 2024 | [Common-Mode Noise Suppression in Isolated DC-DC Converters Based on Coupled Inductor Rectifier](https://doi.org/10.1109/tie.2024.3360607) · IEEE Transactions on Industrial Electronics[^p3] | 1저자 Taewoo Kim, 마지막 저자 Gun-Woo Moon | 기존 출력 코일을 결합 인덕터로 바꿔 변압기에서 발생하는 공통 모드 잡음을 상쇄한다. 추가 부품 없이 잡음을 낮춰 필터의 부피를 줄이는 방법을 실험했다. |
| 4 | 2023 | [A New Phase Shift Full Bridge dc/dc Converter With Integrated Intermodule Battery Equalization Circuit (IBEC)](https://doi.org/10.1109/tte.2023.3332859) · IEEE Transactions on Transportation Electrification[^p4] | 1저자 Kyung-Hwa Park, 마지막 저자 Gun-Woo Moon | 전기차의 저전압 전원 회로에 배터리 모듈 사이의 균형을 맞추는 회로를 더했다. 충전과 방전 양쪽에서 목표 모듈을 조절하면서 전원을 공급하는 동작을 시제품으로 확인했다. |
| 5 | 2024 | [Reverse-Pulse Charging Method of Lithium Batteries for Stable Charging at Low Temperatures](https://doi.org/10.33961/jecst.2024.00969) · Journal of Electrochemical Science and Technology[^p5] | 1저자 Jae-In Lee, 마지막 저자 Gun-Woo Moon | 저온 충전 중 역방향 전류 펄스를 넣는다. 추가 감지 단자 없이 일정 전류 충전과 같은 평균 전류를 유지하면서, 충전 속도를 유지하고 용량 감소를 완화하는 방법을 제안했다. |
| 6 | 2022 | [Frequency-Variable Resonant Self-Heating Technique for Lithium-Ion Batteries at Low Temperature](https://doi.org/10.1109/taes.2022.3151322) · IEEE Transactions on Aerospace and Electronic Systems[^p6] | 1저자 Sang-Hyeon Ha, 마지막 저자 Gun-Woo Moon | 배터리의 충전·방전 반복 주파수를 바꿔 내부에서 열이 나도록 한다. 배터리의 전류 흐름에 대한 방해가 최소인 조건을 찾아 가열 전류와 가열 속도를 높이는 방법을 제안했다. |
| 7 | 2024 | [Dual-Band Rectifier Using Coupled Inductor for Wireless Power Transfer Receivers](https://doi.org/10.1109/tpel.2024.3521362) · IEEE Transactions on Power Electronics[^p7] | 1저자 Dongmin Kim, 마지막 저자 Gun-Woo Moon | 들어오는 신호의 주파수 대역에 따라 정류 방식이 자동으로 달라지는 무선 충전 수신기다. 별도 감지 회로나 외부 제어 신호 없이 서로 다른 두 대역의 충전을 지원하도록 설계했다. |
| 8 | 2022 | [A New Direct Charging Control for Electrical Power Systems in Low Earth Orbit Satellites](https://doi.org/10.1109/taes.2022.3218495) · IEEE Transactions on Aerospace and Electronic Systems[^p8] | 1저자 Jeong-Eon Park, 마지막 저자 Gun-Woo Moon | 가볍고 신뢰성 있는 저궤도 위성 전원 시스템을 위한 직접 충전 제어다. 태양전지 전력 조절기의 무게·효율·신뢰성과 배터리 충전 전류·온도 변화가 수명에 갖는 이점을 분석했다. |

## 교수와 전문 분야

문건우 교수는 KAIST 전기및전자공학부 소속이다.[^ee] 학부는 주요 연구를 전력전자, 전력 변환기·인버터(직류를 교류로 바꾸는 장치), 능동 전력 필터(전력망의 불필요한 전류 성분을 보상하는 장치), 유연 교류 송전 시스템으로 적는다.[^ee] 미래자동차학제전공 참여교수 소개는 차량 탑재형 충전기, 직류 전압 변환기, 역률 보정 컨버터를 주요 연구 분야로 든다.[^fv]

최근 논문으로 보는 전문 분야는 전력 변환 회로의 구조와 제어, 서버 전원 통합, 전기차 배터리 충전·균등화, 위성 전력 공급이다. 회로 부품을 공유하거나 기존 부품의 연결을 바꾸고, 동작 시간을 조절해 전력 공급의 효율과 품질을 개선하는 연구를 수행한다.[^p1][^p2][^p3][^p4][^p8]

## 응용 분야

연구 소개는 데이터센터 전원, 전기차 전원, 배터리 관리, 소비자 전자기기, 항공우주·국방 전원, 재생에너지를 응용 갈래로 제시한다. 개발 이력에는 액체 냉각을 쓰는 데이터센터 전원 장치와 Apple 어댑터 시제품 등이 올라 있다.[^research] 대표 논문은 서버의 직류 배전, 차량 배터리 모듈 균등화, 저온 배터리 충전과 가열, 무선 충전 수신기, 저궤도 위성 전원으로 이어진다.[^p2][^p4][^p5][^p6][^p7][^p8]

## 구성원

2026년 11월 7일 Current Members 페이지의 학생 12명이다. 과정과 연구 주제는 게시 표기이며, 김성준은 연구실장으로 적혀 있다. 「대표 논문 참여」는 위 표의 번호이며, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 배주현 (Juhyun Bae) | 박사과정 | Military, DC-DC Converter | wngus7158@kaist.ac.kr |  |
| 박정찬 (Jeongchan Park) | 박사과정 | Aerospace, DC-DC Converter | xkxkrxjwu@kaist.ac.kr | 3 |
| 정영훈 (Yeonghun Jeong) | 박사과정 | DC-DC Converter | yeonghunj@kaist.ac.kr |  |
| 김성준 (Seongjun Kim) | 박사과정 | DC-DC Converter | sj.kim@kaist.ac.kr |  |
| 김가희 (Kahee Kim) | 석사과정 | Battery, DC-DC Converter | kaheekim@kaist.ac.kr |  |
| 장하균 (Hagyun Jang) | 석사과정 | DC-DC Converter | gyun11@kaist.ac.kr |  |
| 김인성 (Insung Kim) | 석사과정 | AI Data Center, DC-DC Converter | chaukis0612@kaist.ac.kr |  |
| 김태희 (Taehee Kim) | 석사과정 | DC-DC Converter | taehee.k@kaist.ac.kr |  |
| 김희곤 (Heegon Kim) | 석사과정 | Military, DC-DC Converter | heegkim@kaist.ac.kr |  |
| 박준석 (Junseok Park) | 석사과정 | DC-DC Converter | jspark@kaist.ac.kr |  |
| 조현익 (Hyeonik Jo) | 석사과정 | DC-DC Converter | harold31@kaist.ac.kr |  |
| 최유진 (Yujin Choi) | 학부생 | DC-DC Converter |  |  |

## 졸업생 진로

Alumni 페이지의 박사 50명과 석사 20명이다. 학위와 진로는 누리집 표기다.[^alumni]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 최동민 (Dongmin Choi) | Ph.D. | Samsung Electronics |
| 김태우 (Taewoo Kim) | Ph.D. | Kyungpook National University |
| 박경화 (Kyungwha Park) | Ph.D. | Defense Agency for Technology and Quality |
| 최승현 (Seung-Hyun Choi) | Ph.D. | Korea Hydro & Nuclear Power |
| 이재인 (Jae-In Lee) | Ph.D. | Agency for Defense Development |
| 김재상 (Jae-Sang Kim) | Ph.D. | Samsung Electronics |
| 김동민 (Dongmin Kim) | Ph.D. | Korea University of Technology and Education |
| 이민수 (Minsu Lee) | Ph.D. | Samsung Electronics |
| 박정언 (Jeong-Eon Park) | Ph.D. | Hanbat National University |
| 하상현 (Sang-Hyeon Ha) | Ph.D. | Agency for Defense Development |
| 김기목 (Ki-Mok Kim) | Ph.D. | Hannam University |
| 이영달 (Young-Dal Lee) | Ph.D. | Chonnam National University |
| 박무현 (Moo-Hyun Park) | Ph.D. | Hyundai Motor |
| 김건우 (Keon-Woo Kim) | Ph.D. | Samsung Electronics |
| 한정규 (Jung-Kyu Han) | Ph.D. | Hanbat National University |
| 임천용 (Cheon-Yong Lim) | Ph.D. | Jeonbuk National University |
| 이나영 (Nayoung Lee) | Ph.D. | Hyundai Motor |
| 백재일 (Jaeil Baek) | Ph.D. | KAIST |
| 정연호 (Yeonho Jeong) | Ph.D. | University of Rhode Island |
| 연철오 (Cheol-O Yeon) | Ph.D. | Samsung Electronics |
| 윤한신 (Han-Shin Youn) | Ph.D. | Incheon National University |
| 이재범 (Jae-Bum Lee) | Ph.D. | Korea National University of Transportation |
| 김종우 (Jong-Woo Kim) | Ph.D. | Konkuk University |
| 김준호 (Jun-Ho Kim) | Ph.D. | Keimyung University |
| 조신영 (Shin-Young Cho) | Ph.D. | Agency for Defense Development |
| 김재현 (Jae-Hyun Kim) | Ph.D. | Hyundai Motor |
| 홍주표 (Ju-Pyo Hong) | Ph.D. | Silicon Works |
| 김문영 (Moon-Young Kim) | Ph.D. | Samsung Electronics |
| 문상철 (SangCheol Moon) | Ph.D. | Apple |
| 정신명 (Shin_Myung Jung) | Ph.D. | Korea Railroad Research Institute |
| 김덕유 (Duk-You Kim) | Ph.D. | LG Chem |
| 이근욱 (Keun-Wook Lee) | Ph.D. | LG Chem |
| 김형석 (Hyoung-suk Kim) | Ph.D. | Korea Electrotechnology Research Institute |
| 이일운 (Il-Oun Lee) | Ph.D. | Myongji University |
| 조인호 (In-Ho Cho) | Ph.D. | Korea National University of Transportation |
| 김영도 (Young-Do Kim) | Ph.D. | Hyundai Mobis |
| 김봉철 (Bong-Chul Kim) | Ph.D. | LG Chem |
| 김철호 (Chol-Ho Kim) | Ph.D. | Samsung Display |
| 이병희 (Byoung-Hee Lee) | Ph.D. | Hanbat National University |
| 조대연 (Daeyoun Cho) | Ph.D. | Samsung Display |
| 김재국 (Jae-Kuk Kim) | Ph.D. | Inha University |
| Jacobo | Ph.D. |  |
| 이우진 (Woo-Jin Lee) | Ph.D. | Samsung Display |
| 조규민 (Kyu-Min Cho) | Ph.D. | LG electronics |
| 최성욱 (Seong-Wook Choi) | Ph.D. | Samsung Electro-Mechanics |
| 이강현 (Kang-Hyun Yi) | Ph.D. | Daegu University |
| 박홍선 (Hong-Sun Park) | Ph.D. | SOLUM |
| 오원식 (Won-Sik Oh) | Ph.D. | Samsung Display |
| 김정은 (Chong-Eun Kim) | Ph.D. | Korea National University of Transportation |
| 이성세 (Sung-Sae Lee) | Ph.D. | Korea Aerospace Research Institute |
| 방지훈 (Jihun Bang) | M.S. | Hyundai Motor |
| 김준수 (Joonsu Kim) | M.S. | Hyundai Motor |
| 김재호 (Jaeho Kim) | M.S. | Hyundai Motor |
| 유동현 (Donghyeon Yu) | M.S. | Samsung Electronics |
| 채종윤 (Jongyoon Chae) | M.S. | Georgia Institute of Technology (Ph.D.) |
| 천성문 (Sungmun Cheon) | M.S. | Samsung Electronics |
| 이정수 (Jeong-Soo Lee) | M.S. | Twinius |
| 고승환 (Seung-Hwan Ko) | M.S. | Ohio state university (Ph.D.) |
| 최재원 (Jae-Won Choi) | M.S. | ON Semiconductor |
| 강병구 (Byung-Gu Kang) | M.S. | Hyundai Motor |
| 좌승우 (Seung Woo Jwa) | M.S. | Samsung Electronics |
| 유찬훈 (Chan-Hun Yu) | M.S. | Korea Electrotechnology Research Institute |
| 문정필 (Jung Pil Moon) | M.S. | Samsung Electronics |
| 양덕기 (Deok-Ki Yang) | M.S. | Korea Testing Laboratory |
| 이승현 (Seung-Hyun Lee) | M.S. | LG Chem |
| 임유리 (Yu-Ri Lim) | M.S. | SK Hynix |
| 이희철 (Hee-Chul Lee) | M.S. | Samsung Electronics |
| 이연재 (Yeon-Jae Lee) | M.S. | SK Innovation |
| 김인주 (In-Ju Kim) | M.S. | Agency for Defense Development |
| 유병규 (Byunggyu Yu) | M.S. | Kongju National University |

## 최근 논문 목록 (2021–2026)

학술지·국제학회·국내학회 목록의 논문 58편이다. 제목·저자·발표처와 연월은 연구실 게시 표기이며, DOI는 같은 논문의 등록 서지가 대응하는 경우 덧붙였다.[^journals][^international][^domestic][^bibliography]

**2026**

- Chihyun Ahn, ByeongUk Im, SunHoo Park, Gun-Woo Moon, SangJoon Shin "Conceptual Design of an AAM Tiltrotor via Aircraft-Level Weight-Performance Feedback", International Journal of Aeronautical and Space Sciences. 2026.08.
- Seongjun Kim, Dongmin Choi, Kahee Kim, Jaeil Baek, Gun-Woo Moon, "A Half-Bridge Converter with Coupled Inductor for Electrical Power Systems in Satellites", 2026 International Power Electronics Conference, IPEC-Nagasaki 2026 - ECCE Asia, 일본, 2026.06 DOI: https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597462
- Kahee Kim, Dongmin Choi, Seongjun Kim, Jaeil Baek, Gun-Woo Moon, "A New Full-Bridge Buck-Boost Converter with Coupled-Inductor for EV Solar Roof Application", 2026 International Power Electronics Conference, IPEC-Nagasaki 2026 - ECCE Asia, 일본, 2026.06 DOI: https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11597223
- Yeonghun Jeong, Dongmin Choi, Taewoo Kim, Jaeil Baek, Gun-Woo Moon, "Zero Voltage Switching Technique Using Synchronous Rectifier Control of PWM LLC Resonant Converter for Light Load Efficiency", 2026 International Power Electronics Conference, IPEC-Nagasaki 2026 - ECCE Asia, 일본, 2026.06 DOI: https://doi.org/10.23919/ipec-nagasaki2026-ec64663.2026.11596680
- 김성준, 최동민, 정영훈, 박정언, 한정규, 백재일, 문건우, "인공위성 전기 추진 시스템을 위한 커플드 인덕터 하프-브릿지 컨버터", 2026년도 전력전자학술대회, 2026.07.15
- 김가희, 최동민, 정영훈, 장하균, 한정규, 백재일, 문건우, "EV 솔라 루프 시스템을 위한 결합인덕터 기반의 새로운 풀브릿지 벅-부스트 컨버터", 2026년도 전력전자학술대회, 2026.07.15

**2025**

- Cheon-Yong Lim, Yeonho Jeong, Hyeon-Woo Jeong, Gun-Woo Moon "Critical mode boost power factor correction converter with high efficiency and reduced input current distortion using variable inductor", Journal of Power Electronics, v.26, pp.13-25, 2025.12. DOI: https://doi.org/10.1007/s43236-025-01235-7
- Jaein Lee, Sang-Hyeon Ha, Hyunki Yoon, Jae-Sang kim, Jaeil Baek, Gun-Woo Moon, "Reverse-Pulse Charging Method of Lithium Batteries for Stable Charging at Low Temperatures",  Journal of Electrochemical Science and Technology, v.16, no1, pp.113-128, 2025.01. DOI: https://doi.org/10.33961/jecst.2024.00969
- Dongmin Kim, Jongyoon Chae, Ki-bum Park, Gun-Woo Moon, "Dual-Band Rectifier Using Coupled Inductor for Wireless Power Transfer Receivers," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.40, no.5, pp.7488-7499, 2025.05. DOI: https://doi.org/10.1109/tpel.2024.3521362
- Jong-yoon Chae, Dong-min Kim, Dongmin Choi, Gun-Woo Moon, "New Reverse Mode Control Method of Phase-Shift Full-Bridge Converter for Bidirectional Auxiliary Power Module", 2025 IEEE Applied Power Electronics Conference and Exposition - APEC 미국, 2025.03
- 정영훈, 백재일, 최동민, 이훈준, 김 인성, 도근태, 김수겸, 문건우, "이온추력기용 전력변환시스템의 구성 및 분석",  2025년도 한국추진공학회 학술대회, 대한민국, 2025.12
- 정영훈, 최동민, 김태우, 김성준, 김가희, 문건우, "경부하 효율 향상을 위한 PWM LLC 공진형 컨버터의 동기정류기 제어를 이용한 영전압 스위칭 기법", 2025년도 전력전자학술대회, 대한민국, 2025.07.07
- 최동민, 김성준, 정영훈, 김가희, 문건우, "네트워크 통신용 전원 장치의 DC Bias Modulation을 위한 단일 인덕터 이중 출력 DC-DC 컨버터", 2025년도 전력전자학술대회, 대한민국, 2025.07.07

**2024**

- Taewoo Kim, Dongmin Choi, Seung-Hyun Choi, Gun-Woo Moon, "Improved Natural Current Sharing and Phase-shedding Operation in LLC Resonant Converters With Voltage-Doubler Rectifier," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.39, no.10, pp.13401-13412, 2024.10. DOI: https://doi.org/10.1109/tpel.2024.3422316
- Moo-Hyun Park, Xueshen Zhang, Yeonho Jeong, Gun-Woo Moon, "A High Efficiency Boost Pre-Regulator Merging with an Asymmetric LLC Standby Converter in DC Power Distribution System for Data Center," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.39, no.8, pp.9804-9813, 2024.08. DOI: https://doi.org/10.1109/tpel.2024.3379382
- Jae-Sang Kim, Jung-Kyu Han, Jaeho Kim, Gun-Woo Moon, "A New High-Power Density Tailored Waveform Modulator for Plasma Processing," IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.71, no.11, pp.13932-13942, 2024.11. DOI: https://doi.org/10.1109/tie.2024.3363739
- Taewoo Kim, Jeongchan Park, Keon-Woo Kim, Gun-Woo Moon, "Common-Mode Noise Suppression in isolated DC-DC Converters Based on Coupled Inductor Rectifier," IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.71, no.10, pp.12141-12152, 2024.10. DOI: https://doi.org/10.1109/tie.2024.3360607
- Jongyoon Chae, Minsu Lee, Dongmin Kim, Gun-Woo Moon, "New Gate Control Method of PWM Resonant Converters for Near-Zero-Ripple Fuel Cell Current," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.39, no.5, pp.4974-4980, 2024.05. DOI: https://doi.org/10.1109/tpel.2024.3356589
- Kyung-Hwa Park, Minsu Lee, Gun-Woo Moon, "A new Phase Shift Full Bridge DC/DC Converter with Integrated Inter-module Battery Equalization Circuit (IBEC)," IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, v.10, no.3, pp.6618-6633, 2024.09. DOI: https://doi.org/10.1109/tte.2023.3332859
- Jae-Sang Kim, Taewoo Kim, Juhyun Bae, Jung-Kyu Han, Gun-Woo Moon, "A Hybrid Current Reference Control Method for PFC Converter in Server Power Supply," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.39, no.1, pp.64-70, 2024.01. DOI: https://doi.org/10.1109/tpel.2023.3323555
- Dongmin Choi, Minsu Lee, Taewoo Kim, Jae-Sang Kim, Gun-Woo Moon, "Offset Current Modulation Technique for Wide ZVS Range in Dual Active Bridge (DAB) DC-DC Converter," IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.71, no.8, pp.8741-8751, 2024.08. DOI: https://doi.org/10.1109/tie.2023.3312414
- Minsu Lee, Jongyoon Chae, Gun-Woo Moon, "Primary-Side ZVS PWM Resonant Converter with Near-Zero-Ripple Input Current and High Efficiency for Fuel Cell Applications," IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.71, no.7, pp.7010-7019, 2024.07. DOI: https://doi.org/10.1109/tie.2023.3296763
- Seung-Hyun Choi, Jae-Sang Kim, Joonsu Kim, Jihun Bang, Gun-Woo Moon, "A Decentralized Control Method of Battery Energy Storage Units With Different State of Charge", 2024 IEEE 10th International Power Electronics and Motion Control Conference, IPEMC 2024 - ECCE Asia, 중국, 2024.05  DOI: https://doi.org/10.1109/ipemc-ecceasia60879.2024.10567059
- Dongmin Choi, Jae-Sang Kim, Seung-Hyun Choi, Yeonghun Jeong, Gun-Woo Moon, " A New Voltage Distribution Strategy in Input-Series Connected Dual Active Bridge Converters", 2024 IEEE 10th International Power Electronics and Motion Control Conference, IPEMC 2024 - ECCE Asia, 중국, 2024.05 DOI: https://doi.org/10.1109/ipemc-ecceasia60879.2024.10567739
- 최승현, 김동민, 방지훈, 김성준, 문건우, "모든 부하 조건에서 SoC 밸런싱이 가능한 적응형 드룹 제어 방법", 2024년도 전력전자학술대회, 대한민국, 2024.07.01
- 최동민, 김재상, 정영훈, 김성준, 문건우, "직렬-입력 구조를 갖는 DAB 컨버터의 새로운 전압 분배 제어 기법", 2024년도 전력전자학술대회, 대한민국, 2024.07.01
- 최승현, 박정찬, 방지훈, 문건우, "Urban Air Mobility를 위한 고신뢰성 저중량의 배터리 관리 시스템", 2024년도 한국항공우주학회, 대한민국, 2024.04.03

**2023**

- Dongmin Kim, Jongyoon Chae, Ki-Bum Park, Gun-Woo Moon, "A Self-Oscillated Feedback Network for Push-Pull Resonant Power Converters," IEEE TRANSACTIONS ON POWER ELECTRONICS, v.38, no.11, pp.14249-14261, 2023.11.   DOI: https://doi.org/10.1109/tpel.2023.3303649
- Jeong-Eon Park, Jung-Kyu Han, Ki-Bum Park, Byoung-Hee Lee, Gun-Woo Moon, ''A New Direct Charging Control for Electrical Power Systems in Low Earth Orbit Satellites,'' IEEE TRANSACTIONS ON AEROSPACE AND ELECTRONIC SYSTEMS, v.59, no.3, pp.2566-2578, 2023.06. DOI: https://doi.org/10.1109/taes.2022.3218495
- Taewoo Kim, Seung-Hyun Choi, Dongmin Choi, Jeong-Eon Park, Gun-Woo Moon, ''Double Fault-Tolerant LLC Resonant Converter With Reconfiguration Method,'' IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.70, no.5, pp.4651-4661, 2023.05. DOI: https://doi.org/10.1109/tie.2022.3187590
- Minsu Lee, Dongmin Choi, Jongyoon Chae, Sungmoon Cheon, Gun-Woo Moon, ''Voltage-Balancing Dual-Active-Bridge (VB-DAB) Converter for Bipolar DC Distribution System,'' IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, v.70, no.3, pp.2461-2471, 2023.03. DOI: https://doi.org/10.1109/tie.2022.3172765
- Jeong-Eon Park, Jung-Kyu Han, Seung-Hyun Choi, Gun-Woo Moon, ''Two-Switch Forward Converter With an Integrated Buck Converter for High Bus Voltage in Satellites,'' IEEE TRANSACTIONS ON POWER ELECTRONICS, v.38, no.2, pp.2041-2051, 2023.02. DOI: https://doi.org/10.1109/tpel.2022.3197610
- Donghyeon Yu, Dongmin Choi, Jaeho Kim, Jihun Bang, Gun-Woo Moon, "A Control Method of Two-Switch Forward Converter for High efficiency Under Light Load Conditions", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05  DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213525
- Jeongchan Park, Taewoo Kim, Seung-Hyun Choi, Jae-In Lee, Gun-Woo Moon, "High Efficiency of Asymmetric Half-Bridge Converter with Simple SR Switch Control under Light Load Condition", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05 DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213808
- Taewoo Kim, Jeongchan Park, Donghyeon Yu, Joonsu Kim, Gun-Woo Moon, "A Natural Current Sharing in LLC Resonant Converter and Analysis of the Current Sharing Error", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05  DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213546
- Jae-Sang Kim, Taewoo Kim, Yeong-Hun Jeong, Gun-Woo Moon, "A Hybrid Current Reference Control Method for PFC Converter in Server Power Supply", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05  DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213682
- Seung-Hyun Choi, Jae-Sang Kim, Jongyoon Chae, Juyeon Sim, Gun-Woo Moon, "A Nonlinear Droop Control for Supercapacitor-Hybrid Uninterruptible Power Supplies in DC Microgrids", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05    DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213930
- Minsu Lee, Dongmin Choi, Jongyoon Chae, Kyunghwa Park, Gun-Woo Moon, "Novel Clamp Diode to Mitigate the Voltage Oscillation of Low Voltage Rectifier Diodes in Asymmetric Half-Bridge Converter", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05   DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213708
- Jongyoon Chae, Minsu Lee, Jae Ho Kim, Dongmin Kim, Gun-Woo Moon, "A Simple Gate Control Method for Output Voltage Balancing in Input-Parallel Output-Series Boost Converter", 2023 11th International Conference on Power Electronics and ECCE Asia, ICPE 2023 - ECCE Asia, 대한민국, 2023.05  DOI: https://doi.org/10.23919/icpe2023-ecceasia54778.2023.10213824
- 최동민, 이민수, 방지훈, 정영훈, 문건우, "영전압 스위칭 특성 개선을 위한 DAB 컨버터의 오프셋 전류 변조 기법", 2023년도 전력전자학술대회, 대한민국, 2023.07.04
- 김동민, 최동민, 채종윤, 심주연, 김준수, 문건우, "양방향 위상 천이 풀브리지의 역방향 동작을 위한 최적 게이트 구동 방법", 2023년도 전력전자학술대회, 대한민국, 2023.07.04
- 최승현, 김재상, 김재호, 정영훈, 문건우, "다중 배터리 에너지 저장장치의 충전 상태 균등화를 위한 드룹 제어 방법", 2023년도 전력전자학술대회, 대한민국, 2023.07.04
- 김재상, 김동민, 김태우, 김재호, 문건우, "플라즈마 공정을 위한 새로운 고전력 밀도 맞춤 파형 모듈레이터", 2023년도 전력전자학술대회, 대한민국, 2023.07.04
- 이민수, 최승현, 최동민, 방지훈, 문건우, "낮은 입력 전류 리플을 갖는 연료 전지용 고효율 공진형 PWM 컨버터", 2023년도 전력전자학술대회, 대한민국, 2023.07.04
- 김태우, 박정찬, 유동현, 김준수, 문건우, "부하 분담 기능을 갖는 LLC 공진형 컨버터", 2023년도 전력전자학술대회, 대한민국, 2023.07.04

**2022**

- Juhyun Bae, Jae-Sang Kim, Minsu Lee, Jung-Kyu Han, Gun-Woo Moon, ''High-Efficiency Asymmetrical Half-Bridge Converter With Linear Voltage Gain,'' IEEE TRANSACTIONS ON POWER ELECTRONICS, v.37, no.12, pp.14850-14861, 2022.12. DOI: https://doi.org/10.1109/tpel.2022.3183260
- Sang-Hyeon Ha, Jae-In Lee, Hyunki Yoon, Tae-Ryong Park, Jaeill Baek, Jae-Sang Kim, Gun-Woo Moon, ''Frequency-Variable Resonant Self-Heating Technique for Lithium-Ion Batteries at Low Temperature,'' IEEE TRANSACTIONS ON AEROSPACE AND ELECTRONIC SYSTEMS, v.58, no.4, pp.3399-3410, 2022.08. DOI: https://doi.org/10.1109/taes.2022.3151322
- Seung-Hyun Choi, Jae-Sang Kim, Jeong-Eon Park, Dong-Hyeon Yu, Gun-Woo Moon, "Design of Integral Droop Control for Hybrid Energy Storage System Considering Ramp Rate Characteristic",  2022 International Power Electronics Conference, IPEC-Himeji 2022-ECCE Asia, 일본, 2022.05. DOI: https://doi.org/10.23919/ipec-himeji2022-ecce53331.2022.9806862
- Min-Su Lee, Dong-Min Choi, Ju-Hyun Bae, Jong-Yoon Chae, Gun-Woo Moon, "A New Secondary Clamp Diode for Phase-Shift Full-Bridge Converter",  2022 International Power Electronics Conference, IPEC-Himeji 2022-ECCE Asia, 일본, 2022.05. DOI: https://doi.org/10.23919/ipec-himeji2022-ecce53331.2022.9806924
- Dong-Min Choi, Min-Su Lee, Tae-Woo Dong-Min Kim Kim, Gun-Woo Moon, "A Dual-Active-Bridge (DAB) Converter Based Bidirectional DC/DC Converter with Reduced Link Capacitance",  2022 International Power Electronics Conference, IPEC-Himeji 2022-ECCE Asia, 일본, 2022.05. DOI: https://doi.org/10.23919/ipec-himeji2022-ecce53331.2022.9806915
- Ju-Hyun Bae, Jae-Sang Kim, Min-Su Lee, Park, Jeongchan, Gun-Woo Moon, "High-Efficiency Asymmetrical Half-Bridge Converter with Series Capacitor Rectifier and Linear Voltage Gain",  International Power Electronics Conference, IPEC-Himeji 2022-ECCE Asia, 일본, 2022.05. DOI: https://doi.org/10.23919/ipec-himeji2022-ecce53331.2022.9806978
- 최동민, 이민수, 김태우, 유동현, 문건우, "액티브 필터가 통합된 DAB 컨버터 기반 양방향 DC/DC 컨버터",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.
- 배주현, 김재상, 이민수, 문건우, "직렬 커패시터 정류기를 갖는 고효율 비대칭 하프-브리지 컨버터",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.
- 최승현, 김재상, 박정언, 김태우, 문건우, "하이브리드 에너지 저장장치의 비용 절감을 위한 적응형 적분기 드룹 제어",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.
- 김태우, 최승현, 박정언, 박정찬, 문건우, "단락 고장 대응이 가능한 고밀도, 저비용 LLC 공진형 컨버터",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.
- 이민수, 배주현, 문건우, "위상천이 풀브리지 컨버터를 위한 센터탭 클램프 다이오드",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.
- 김재상, 김태우, 배주현, 문건우, "서버용 전원 장치의 입력 전류 왜곡을 저감한 하이브리드 제어 방법",  2022년도 전력전자학술대회, 대한민국, 2022.07.06.

**2021**

- Ja-Chun Koo, Jung-Eon Park, Gun-Woo Moon, ''Triple Junction GAGET2-ID2 Solar Cell Degradation by Solar Proton Events,'' JOURNAL OF THE KOREAN SOCIETY FOR AERONAUTICAL AND SPACE SCIENCES, v.49, no.12, pp.1019-1025, 2021. DOI: https://doi.org/10.5139/jksas.2021.49.12.1019

## 연락과 위치

- 연구실: (34141) 대전광역시 유성구 대학로 291 KAIST LG이노베이션홀(N24) 4101호[^home][^ee]
- 연구실 전화: 042-350-8075[^home]
- 교수 전화: 042-350-3475[^fv]
- 교수 이메일: gwmoon@kaist.ac.kr[^ee][^fv]

## 각주
[^p1]: C.-Y. Lim, Y. Jeong, H.-W. Jeong, G.-W. Moon, Journal of Power Electronics (2025). <https://doi.org/10.1007/s43236-025-01235-7> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p2]: M.-H. Park, X. Zhang, Y. Jeong, G.-W. Moon, IEEE Transactions on Power Electronics (2024). <https://doi.org/10.1109/tpel.2024.3379382> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p3]: T. Kim, J. Park, K.-W. Kim, G.-W. Moon, IEEE Transactions on Industrial Electronics (2024). <https://doi.org/10.1109/tie.2024.3360607> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p4]: K.-H. Park, M. Lee, G.-W. Moon, IEEE Transactions on Transportation Electrification (2023). <https://doi.org/10.1109/tte.2023.3332859> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p5]: J.-I. Lee 외, G.-W. Moon, Journal of Electrochemical Science and Technology (2024). <https://doi.org/10.33961/jecst.2024.00969> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p6]: S.-H. Ha 외, G.-W. Moon, IEEE Transactions on Aerospace and Electronic Systems (2022). <https://doi.org/10.1109/taes.2022.3151322> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p7]: D. Kim, J. Chae, K.-B. Park, G.-W. Moon, IEEE Transactions on Power Electronics (2024). <https://doi.org/10.1109/tpel.2024.3521362> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^p8]: J.-E. Park 외, G.-W. Moon, IEEE Transactions on Aerospace and Electronic Systems (2022). <https://doi.org/10.1109/taes.2022.3218495> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).
[^home]: Home. <https://sites.google.com/view/kaistpelab> (관측 2026-11-07).
[^research]: Research. <https://sites.google.com/view/kaistpelab/research> (관측 2026-11-07).
[^ee]: KAIST 전기및전자공학부 교수 목록. <https://ee.kaist.ac.kr/professor-s1/> (관측 2026-11-07).
[^fv]: KAIST 미래자동차학제전공 참여교수. <https://fv.kaist.ac.kr/index.php?mid=fv01_03> (관측 2026-11-07).
[^members]: Current Members. <https://sites.google.com/view/kaistpelab/member/current-members> (관측 2026-11-07).
[^alumni]: Alumni. <https://sites.google.com/view/kaistpelab/member/alumni> (관측 2026-11-07).
[^journals]: Journals. <https://sites.google.com/view/kaistpelab/publications/journals> (관측 2026-11-07).
[^international]: International Conferences. <https://sites.google.com/view/kaistpelab/publications/international-conferences> (관측 2026-11-07).
[^domestic]: Domestic Conferences. <https://sites.google.com/view/kaistpelab/publications/domestic-conferences> (관측 2026-11-07).
[^bibliography]: Gun-Woo Moon 저자 논문 서지와 소속. <https://api.openalex.org/works?per-page=200&page=1&sort=publication_date:desc&select=id,doi,title,publication_year,publication_date,type,primary_location,authorships,abstract_inverted_index&filter=author.id:A5020942195,publication_year:2021-2026> (관측 2026-11-07).

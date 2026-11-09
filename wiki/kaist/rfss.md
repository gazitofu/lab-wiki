# RF 시스템 솔루션 연구실 (Radio Frequency System Solution Lab, RFSS)

**KAIST 전기및전자공학부 · 유종원 교수**

- 분야: 안테나와 고주파 시스템, 무선 통신, 무선 전력 전송, 고주파 계측, 유선 통신 채널
- 대분야: 전기전자·반도체·광학
- 태그: 무선·이동통신[^intro], 무선 전력 전송[^intro][^topic]
- 홈페이지: <https://sites.google.com/view/rfss/home>
- 근거와 출처: [RFSS 근거 페이지](rfss-sources.md)

> 전파를 보내고 받는 안테나와 회로를 함께 설계해, 무선 통신·무선 충전·산업용 측정 시스템으로 만드는 연구실이다.[^intro][^topic]

## 무엇을 연구하나

연구실은 미래 무선 통신 환경에 맞춰 효율과 신뢰성을 높이는 RF(Radio Frequency, 전파를 다루는 고주파 영역) 시스템을 연구한다.[^intro] 안테나(전기 신호와 공간을 퍼지는 전자기파를 서로 바꾸는 장치)를 설계하고, 응용에 맞는 주파수(변화가 단위 시간에 반복되는 횟수) 대역에서 실제 시스템을 제작한다. 신호는 정보를 담아 변하는 물리량이고, 전자기파는 전기적 작용과 자기적 작용의 변화가 공간을 따라 퍼지는 파동이다. 설계와 분석을 실제 제작에 연결해 각 시스템의 문제점과 부족한 점을 개선하는 것이 연구 방향이다.[^intro]

무선 통신에서는 빔포밍(여러 안테나에서 나오는 파동을 합쳐 송수신 방향을 정하는 기술)으로 특정 위치에 신호를 보내고 받으며, 위상 배열 안테나(배열된 안테나의 위상을 조절해 방사 방향을 바꾸는 안테나)를 연구한다. 위상은 주기적으로 반복되는 변화가 한 주기 안에서 어디에 있는지를 나타낸다. 연구 소개는 넓은 각도로 방향을 바꾸는 배열, 유전체(전기를 잘 통하지 않으면서 외부 전기적 작용에 반응해 내부 전하 분포가 바뀌는 물질) 렌즈를 쓰는 안테나, 다중 빔 구조, 위성 통신 단말을 주요 대상으로 든다.[^intro][^topic]

무선 전력 전송에서는 전선 없이 기기에 전력을 보내는 무선 충전 시스템을 개발한다.[^intro][^topic] 여러 송신기와 수신기가 함께 있는 입체적인 충전 구조, 효율이 최대가 되는 동작점의 추적, 코일(전선을 감아 자기적 작용을 만들거나 받아들이는 부품) 사이 상호 인덕턴스의 보상과 추적을 다룬다. 상호 인덕턴스는 한 코일의 전류 변화율에 대해 다른 코일에 유도되는 전압의 비례상수다. 연구실은 차세대 무선 충전 규격을 활용하는 전력 전송을 최근 연구 주제로 명시한다.[^intro][^topic]

물리량의 측정과 통신 채널 해석도 연구한다. 벡터 네트워크 분석기(입사한 신호에 대한 반사·통과 신호의 크기와 위상을 주파수에 따라 재는 장치)를 소형·광대역으로 설계하고, 되돌아온 신호로 반도체 공정 챔버(제조 공정이 이루어지는 밀폐 공간)의 상태를 진단한다. 긴 전선에서는 임피던스(교류 전압을 전류로 나눈 비로, 크기와 위상차를 함께 나타내는 값)를 분석하고 통신 시스템을 구현한다. 최근 연구 소개에는 사물인터넷(IoT, Internet of Things, 기기들이 통신망으로 연결되어 정보를 주고받는 체계) 시스템 개발과 실내외에서 전파가 퍼지는 특성의 분석도 포함된다.[^intro][^topic]

## 주요 연구 주제

### 안테나의 방향 제어와 자체 교정

넓은 각도를 향하는 배열 안테나, 여러 빔을 만드는 소자, 고이득 안테나와 배열 구조를 설계한다. 이득은 같은 전력을 모든 방향에 고르게 방사하는 기준 안테나에 대해 특정 방향으로 방사하는 전력의 비다. 대표 논문 1은 서로 직교하는 두 편파(전자기파 전기적 진동 방향의 성질)를 다루는 배열의 자체 교정을, 대표 논문 3은 현장에서 배열 방사 특성을 추정하는 방법을 보여 준다.[^topic][^p1][^p3]

### 여러 기기에 전력을 보내는 무선 충전

여러 송수신기 사이의 결합을 고려한 무선 충전과 효율 추적을 연구한다. 대표 논문 7은 곡면 구조와 기울인 빔을 이용해 수신기에 전력을 모으고, 대표 논문 8은 딥러닝(여러 층의 신경망으로 자료의 표현을 단계적으로 학습하는 기계학습 분야)으로 분산 송신기의 위상을 정한다. 신경망은 연결된 계산 단위의 가중치를 조정하며 입력과 출력 사이 관계를 학습하는 계산 모형이다.[^topic][^p7][^p8]

### 투명 안테나와 전파 에너지 수확

대표 논문 2는 빛이 통과하는 금속망으로 만든 안테나의 고주파 손실을 모형화하고 설계에 반영한다. 대표 논문 5는 에너지 하베스팅(주변에서 얻는 에너지를 모아 기기에 쓸 전력으로 바꾸는 기술)을 위한 안테나와 변환 회로의 효율을 측정하고 맞추는 방법이다. 무선 기기의 외관과 전력 공급에 연결되는 안테나·회로 연구다.[^p2][^p5]

### 고주파 계측과 긴 유선 채널

반도체 공정 챔버의 반사 신호를 재는 장치와 긴 전선의 통신 특성을 연구한다. 대표 논문 6은 공정 챔버 진단용 소형 광대역 계측 장치를 설계하고, 대표 논문 4는 하나의 송신기에 여러 수신기가 연결된 에어컨 통신 채널을 케이블과 회로를 함께 고려해 분석한다.[^topic][^p4][^p6]

## 대표 논문

KAIST 재직 시기의 2021–2026년 논문에서 안테나·배열 교정, 무선 전력 전송, 계측, 유선 채널의 연구 갈래를 함께 보여 주는 논문을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 주요 저자는 저자 순서로 적었다.

| 번호 | 연도 | 논문·발표처 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Dual-Polarized Phased-Array Antenna With Asymmetric Coupled-Line Network and a Matched Observation Combiner for Self-Calibration](https://doi.org/10.1109/lawp.2026.3653565) · IEEE Antennas and Wireless Propagation Letters | 안테나가 연결된 상태에서 이중 편파 배열을 자체 교정하도록 비대칭 결합 선로와 신호 결합기를 설계했다. 두 편파 경로의 결합 응답을 맞추고, 신호를 모을 때 생기는 크기·위상 왜곡을 줄였다. 제작한 배열의 다중 빔 측정은 방사 특성의 뚜렷한 저하 없이 모의 결과와 잘 맞았다.[^p1] | 1저자 Seong-Ju Lim, 마지막 저자 Jong‐Won Yu |
| 2 | 2025 | [High-Transparency and High-Efficiency Miniaturized Wideband Antenna Using Optimized Wired Metal Mesh for IoT Applications](https://doi.org/10.1109/jiot.2025.3647523) · IEEE Internet of Things Journal | 투명 금속망의 고주파 손실을 반영하는 재료 모형을 만들고, 이를 안테나 설계에 적용했다. 제작한 안테나의 광대역 동작을 확인하고 굽힘·온도 변화와 실내 전파 환경에서도 평가했다. 실내 통신 측정으로 사물인터넷 통신에 쓸 가능성을 확인했다.[^p2] | 1저자 Seong‐Jin Kim, 마지막 저자 Jong‐Won Yu |
| 3 | 2025 | [Rapid In-Field 3-D Array Factor Estimation for Active Phased Array Antennas by Sweeping Phase of Excitation Signals](https://doi.org/10.1109/tap.2025.3579864) · IEEE Transactions on Antennas and Propagation | 안테나 소자마다 결합 탐침을 넣고 신호의 위상을 바꾸면서 현장에서 배열의 방향별 특성을 추정했다. 멀리 떨어진 측정 장소나 기계 회전 없이 반구 영역의 특성을 재구성한다. 제작한 배열의 실험에서는 주된 빔 형태, 곁가지 빔의 억제, 빔 왜곡을 포착했다.[^p3] | 1저자 Chan-Hee Lee, 마지막 저자 Jong‐Won Yu |
| 4 | 2025 | [Analysis of multi-load distribution channel characteristics for air conditioner application](https://doi.org/10.1080/09205071.2025.2502776) · Journal of Electromagnetic Waves and Applications | 건물이나 공장에서 송신기 하나가 여러 수신기와 긴 케이블로 연결되는 에어컨 통신 환경을 분석했다. 케이블을 전송선로 이론으로 분석한 뒤 통신 회로와 합쳐 채널 모형을 만들었다. 실제 측정과 모의 결과를 비교해 케이블 특성과 수신 신호의 품질을 평가했다.[^p4] | 1저자 Kyeong-Han Shin, 마지막 저자 Jong‐Won Yu |
| 5 | 2025 | [Enhanced Compact RF Energy Harvesting System Using Two-Port Network of Antenna](https://doi.org/10.1109/lmwt.2025.3543347) · IEEE Microwave and Wireless Technology Letters | 안테나와 정류기(교류를 직류로 바꾸는 회로)를 따로 설계한 뒤 연결하면 성능 평가가 어려운 문제를 다뤘다. 안테나를 신호가 드나드는 단자쌍 두 개의 망으로 바꾸어 반사 특성과 변환 효율을 직접 측정하게 했다. 실험에서는 측정을 바탕으로 연결 회로를 조정해 효율을 높였다.[^p5] | 1저자 Seong‐Jin Kim, 마지막 저자 Jong‐Won Yu |
| 6 | 2024 | [Design of a Compact Broadband Vector Network Analyzer to Diagnose a Semiconductor Process Chamber](https://doi.org/10.1109/tim.2024.3502828) · IEEE Transactions on Instrumentation and Measurement | 반도체 공정 챔버의 상태를 진단하기 위해 소형 광대역 벡터 네트워크 분석기를 설계했다. 이득·위상 검출기로 기준 신호와 반사 신호의 차이를 재고 각 신호 경로를 분석해 장치를 구현했다. 정상·비정상 상태의 시험용 챔버에서 반사 특성을 측정한 뒤 두 상태의 차이를 분석했다.[^p6] | 1저자 Seong‐Jin Kim, 마지막 저자 Sang-Won Lee; 유종원 공저자 |
| 7 | 2023 | [Curved-Retrodirective Beamforming System to Improve Microwave Power Transmission Efficiency in the Fresnel Region](https://doi.org/10.1109/jiot.2023.3263519) · IEEE Internet of Things Journal | 곡면 구조의 빔포밍 시스템으로 마이크로파(센티미터·밀리미터 수준의 파장을 갖는 전파)를 수신기에 모으는 방법이다. 송신 소자가 기울어진 빔 방향에서 높은 이득을 내도록 하고 전송 거리와 송수신 안테나 조건에 맞춘 설계 방법을 제시했다. 모의 계산에서 전력 누출이 줄었고 제작·측정에서 전송 효율 향상을 확인했다.[^p7] | 1저자 Sol Kim, 마지막 저자 ByungKuon Ahn; 유종원 공저자 |
| 8 | 2026 | [Distributed microwave power transmission using deep learning: Simulation and experiment](https://doi.org/10.1016/j.aej.2026.01.038) · Alexandria Engineering Journal | 분산된 송신기에서 수신기에 보내는 전력을 최대화할 위상을 빠르게 정하도록 신경망을 학습시켰다. 최적화된 위상을 미리 배워 기존 방법의 반복 작업을 줄이는 방식이다. 모의 계산과 제작한 시스템의 실험에서 비교한 두 방법과 비슷한 수신 전력을 유지하면서 계산 시간이 짧았다.[^p8] | 1저자 Hyo-Won Lee, 마지막 저자 Sol Kim; 유종원 공저자 |

## 교수와 전문 분야

유종원 교수는 KAIST 전기공학 학사·석사·박사 학위를 받았다. 연구실 경력 소개에는 2004년 2월 KAIST 조교수로 부임하고, 2006년 3월 부교수, 2014년 3월 교수로 재직한다고 적혀 있다. 이전에는 삼성전자, Wide Telecom, Telson에서 일했다.[^prof] 학부는 주요 연구를 RF 미세전자공학과 RF·마이크로파 시스템 집적으로 소개한다.[^dept]

최근 논문으로 보면 전문 분야는 안테나와 배열 시스템을 설계하고 교정하는 기술, 무선 전력 전송과 에너지 변환 회로, 고주파 신호를 측정해 장치 상태와 통신 채널을 분석하는 기술로 묶인다. 안테나 소자 설계에 그치지 않고 결합 회로, 신호 수집, 교정 알고리즘과 실제 시스템 제작을 함께 다루는 것이 특징이다.[^p1][^p3][^p4][^p5][^p6][^p7]

## 응용 분야

연구 소개는 차세대 이동통신과 개인용 위성 통신 단말, 여러 기기의 무선 충전, 고주파를 이용한 공정 챔버 상태 진단을 대상으로 든다.[^intro][^topic] 대표 논문은 투명 사물인터넷 안테나, 에어컨의 긴 유선 통신 채널, 반도체 제조 장비의 상태 측정에 연결된다.[^p2][^p4][^p6] 치료 의자의 전기장(공간의 각 지점에서 단위 전하가 받는 전기력으로 나타내는 물리량)을 재는 무선 센서 개발 논문도 있으며, 전기장에 따라 측정 신호의 증폭 정도를 조절하는 계측 장치를 제안한다.[^medical]

## 구성원

2026년 11월 9일 Current Members 게시 기준으로 박사과정 12명과 석사과정 6명이다. 과정과 학교 이메일은 구성원 쪽 표기를 옮겼다. 「대표 논문 참여」는 위 표의 번호이고, 같은 이름의 저자를 같은 사람으로 보아 표시했다.[^members]

| 이름 | 과정 | 이메일 | 대표 논문 참여 |
|---|---|---|---|
| 차 성 용 (Cha, Sung Yong) | 박사과정 |  |  |
| 이 지 훈 (Lee, Ji-Hoon) | 박사과정 | jihoon4615@kaist.ac.kr | 3, 5 |
| 이 효 원 (Lee, Hyo-Won) | 박사과정 | hyowon_lee@kaist.ac.kr | 8 |
| 조 성 준 (Cho, Sungjun) | 박사과정 | chrischo@kaist.ac.kr |  |
| 이 찬 희 (Lee, Chanhee) | 박사과정 | chanheelee@kaist.ac.kr | 1 |
| 이 기 웅 (Lee, Kee Woong) | 박사과정 | kiwglee@kaist.ac.kr |  |
| 조 현 정 (Cho, Hyeon-Jeong) | 박사과정 | nnncom@kaist.ac.kr | 2 |
| 김 지 영 (Kim, Jiyoung) | 박사과정 | jiyoung0177@kaist.ac.kr |  |
| 임 영 준 (Lim, Young-Jun) | 박사과정 | yjlim@kaist.ac.kr |  |
| 서 영 주 (Seo, Yeong-Ju) | 박사과정 | emily005@kaist.ac.kr |  |
| 유 용 선 (Yoo, Yong-Sun) | 박사과정 | yys0928@kaist.ac.kr |  |
| 구 창 우 (Gu, Chang-Woo) | 박사과정 | cwgu90@kaist.ac.kr |  |
| 김 윤 성 (Kim, Yun-Sung) | 석사과정 | yangji0614@kaist.ac.kr |  |
| 김 준 현 (Kim, Junhyun) | 석사과정 | dean9778@kaist.ac.kr |  |
| 강 해 찬 (Kang, Haechan) | 석사과정 | hckang@kaist.ac.kr |  |
| 이 병 주 (Lee, Byeong-Ju) | 석사과정 | bjl0113@kaist.ac.kr |  |
| 정 원 종 (Jeong, Wonjong) | 석사과정 | wonjong.jeong@kaist.ac.kr |  |
| 장 수 민 (Chang, Su Min) | 석사과정 | sir1618@kaist.ac.kr |  |

## 졸업생 진로

연구실의 박사·석사 졸업생과 박사후연구원 이력을 함께 적었다. 같은 사람의 박사·박사후 이력은 한 행에 합쳤으며, 58명의 학위·과정과 진로는 각 목록의 게시 표기다.[^alumniph][^alumnims][^alumnipost]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 임 원 규 (Lim, Won Gyu) | Ph.D(2008) & Post-Doc(2009) | KARI |
| 김 동 조 (Kim, Dong Zo) | Ph.D(2010) | Samsung Electronics |
| 손 왕 익 (Son, Wang Ik) | Ph.D(2012) | Samsung Electronics |
| 김 기 진 (Kim, Ki Jin) | Ph.D(2013) | KETI |
| 이 왕 상 (Lee, Wang Sang) | Ph.D(2013) | Gyeongsang National University |
| 장 형 석 (Jang, Hyeong Seok) | Ph.D(2014) | Samsung Advanced Institute of Tech. |
| 태 현 성 (Tae, Hyun Sung) | Ph.D(2014) | ADD |
| 이 한 림 (Lee, Han Lim) | Ph.D(2014) | Chung-Ang University |
| 이 원 석 (Lee, Won Seok) | Ph.D(2015) | Samsung Advanced Institute of Tech. |
| 이 동 진 (Lee, Dong Jin) | Ph.D(2017) | KRRI |
| 이 수 지 (Lee, Soo Ji) | Ph.D(2017) | ADD |
| 강 승 태 (Khang, Seung Tae) | Ph.D(2018) | Samsung Advanced Institute of Tech. |
| 여 태 동 (Yeo, Tae Dong) | Ph.D(2019) | Eta Electronics (Start Up Company) |
| 김 진 우 (Kim, Jin Woo) | Ph.D(2019) | DTaQ |
| 황 인 준 (Hwang, In June) | Ph.D(2019) | KRISS |
| 류 지 헌 (Ryu, Ji Heon) | Ph.D(2020) | ADD |
| 김 관 성 (Kim, Kwang Sung) | Ph.D(2020) | ADD |
| 이 진 호 (Lee, Jin Ho) | Ph.D(2020) | ADD |
| 송 원 영 (Song, Won Young) | Ph.D(2020) & Post-Doc.(2020) | ETRI |
| 안 병 권 (Ahn, Byung Kuon) | Ph.D(2021) & Post-Doc(2022) | Soongsil University |
| 채 수 창 (Chae, Soo Chang) | Ph.D(2021) | KETI |
| 조 혜 원 (Jo, Hye Won) | Ph.D(2021) | Samsung Electronics |
| 김 광 석 (Kim, Kwang Seok) | Ph.D(2021) | ETRI Affiliated Research Institute |
| 이 현 익 (Lee, Hyon Ik) | Ph.D(2023) | ADD |
| 오 주 익 (Oh, Ju Ik) | Ph.D(2023) | KRISS |
| 김 구 (Kim, Ghoo) | Ph.D(2023) | Samsung Advanced Institute of Tech. |
| 김 정 욱 (Kim, Jeong Wook) | Ph.D(2023) | Ajou University |
| 유 종 상 (Yu, Jong Sang) | Ph.D(2024) | Samsung Electronics |
| 김 솔 (Kim, Sol) | Ph.D(2024) | Soongsil University |
| 한 상 혁 (Han, Sang Hyuck) | Ph.D(2024) | Samsung Electronics |
| 정 태 희 (Jeong, Tae Hee) | Ph.D(2024) | ADD |
| 김 기 호 (Kim, Ki Ho) | Ph.D(2025) | ADD |
| 조 현 영 (Cho, Hyun Young) | Ph.D(2025) | Samsung Electronics |
| 임 성 주 (Lim, Seongju) | Ph.D(2025) & Post-Doc(2026) | ETRI |
| 김 성 진 (Kim, Seong-Jin) | Ph.D(2026) | ADD |
| 손 광 섭 (Son, Kwang Sup) | M.S(2006) | KAERI |
| 임 형 선 (Lim, Hyung Sun) | M.S(2007) | Samsung Electronics |
| 김 진 현 (Kim, Jin Hyun) | M.S(2007) | ETRI |
| 김 완 규 (Kim, Wan Kyu) | M.S(2008) | ADD |
| 김 동 윤 (Kim, Dong Youn) | M.S(2008) | KT |
| 이 상 윤 (Lee, Sang Yun) | M.S(2009) | Samsung Electronics |
| 정 원 석 (Jeong, Won Seok) | M.S(2009) | Samsung Electronics |
| 박 서 영 (Park, Seo Young) | M.S(2009) | Samsung Electronics |
| 김 보 람 (Kim, Bo Ram) | M.S(2009) | Hyundai Heavy Industries |
| 김 정 후 (Kim, Jeong Hoo) | M.S(2010) | Samsung Electronics |
| 차 성 용 (Cha, Sung Yong) | M.S(2012) | KARI |
| 유 솔 지 (Yoo, Sol Ji) | M.S(2015) | Hyundai Mobis |
| 권 덕 수 (Kwon, Duk Soo) | M.S(2016) | ETRI |
| 김 다 솜 (Kim, Da Som) | M.S(2022) | LG Electronics |
| 김 익 환 (Kim, Ik Hwan) | M.S(2023) | Samsung Electronics |
| 정 희 철 (Jung, Hee Chul) | M.S(2024) | Molex Japan |
| 신 경 한 (Shin, Kyeong Han) | M.S(2025) | SK Hynix |
| 서 동 민 (Seo, Dongmin) | M.S(2026) |  |
| 박 가 영 (Park, Ga-Yeong) | M.S(2026) | Hanwha System |
| 신 동 훈 (Shin, Dong Hoon) | Post-Doc.(2008) | ETRI |
| 문 성 모 (Moon, Seong Mo) | Post-Doc.(2010) | ETRI |
| 김 영 담 (Kim, Young Dam) | Post-Doc.(2019) | Chungnam National University |
| 양 성 준 (Yang, Sung Jun) | Post-Doc.(2020) | Seoul National University of Science& Tech. |

## 최근 5년 논문 목록

2021–2026년 구역의 국제 학술지 논문 31편, 국제 학회 논문 36편, 국내 학회 논문 101편이다. 제목·저자·발표처는 각 게시 목록의 표기이며 연도도 게시 구역을 따른다. DOI가 붙은 항목은 해당 논문 주소를 함께 적었다.[^journals][^conferences][^domestic]

**2026**

- Sol Kim, Byungkuon Ahn, Seong-Ju Lim, Sangmin Oh, Jong-Won Yu and Dae Geun Yang. "Enhanced near-field focusing with amplitude–phase arrays for microwave power transmission: Analysis, design, and experiment". *Ain Shams Engineering Journal, 2026*. DOI: <https://doi.org/10.1016/j.asej.2026.104035>.
- Seong-Ju Lim, Chanhee Lee, Chihyun Cheong, Sol Kim and Jong-Won Yu. "Dual-Polarized Phased-Array Antenna With Asymmetric Coupled-Line Network and a Matched Observation Combiner for Self-Calibration". *IEEE Antennas and Wireless Propagation Letters, 2026*. DOI: <https://doi.org/10.1109/lawp.2026.3653565>.
- Sungjun Cho, Seong-Jin Kim, Ji-Young Kim and Jong-Won Yu. "Compensation of Phase Nonlinearity Arising From Low-Power Operation in Integrated Phase Detectors". *IEEE Microwave and Wireless Technology Letters, 2026*. DOI: <https://doi.org/10.1109/lmwt.2026.3695383>.
- Junseok Ma, Ga-Yeong Park, Geunjung Lee, Hyo-Won Lee, Jong-Won Yu and Dong-Ki Yoon. "Coating-Free Nanoscratching for Liquid-Crystal Alignment on PCB-Compatible Millimeter-Wave Reflective Unit Cells". *Advanced Materials Technologies, 2026*.
- Chanhee Lee, Ji-Young Kim, Young-Jun Lim and Jong-Won Yu. "Radiated LO-Leakage Suppression via Phase-Asynchronous LO Distribution in Direct-Conversion Transmit Arrays". *IEEE Microwave and Wireless Technology Letters, 2026*. DOI: <https://doi.org/10.1109/lmwt.2026.3727759>.
- Hyo-Won Lee, Byungkwan Kim, Jong-Won Yu and Sol Kim. "Distributed microwave power transmission using deep learning: Simulation and experiment". *Alexandria Engineering Journal, Mar. 2026*. DOI: <https://doi.org/10.1016/j.aej.2026.01.038>.
- 조현정, 조성준, 이병주, 이찬희, 유종원. "LCMV 기반 송신 멀티빔 시스템의 Inter-beam Interference 저감". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 이찬희, 김준현, 이효원, 권준, 유종원. "광대역 안테나의 위상 중심 비선형성에 의한 FMCW 레이더의 거리응답 열화 및 완화에 관한 연구". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 김지영, 조성준, 강해찬, 김윤성, 유종원. "S11 Circle-Fitting 기반 내부·외부 품질계수 분리 추출을 이용한 파브리-페로 프로브 상태 진단 방법". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 김윤성, 임영준, 김준현, 김지영, 유종원. "선택적 주파수 이동 비아를 이용한 Cavity-Backed Slot Antenna 설계". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 서영주, 이병주, 임영준, 조현정, 유종원. "유효 주파수 대역 기반 마이크로파 캐비티 내부 물질 위치 센싱 기법". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 이병주, 서영주, 조현정, 강해찬, 유종원. "공진 모드 선형결합 기반 마이크로파 캐비티 내 전기장 집중 기법". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 강해찬, 서영주, 조성준, 김윤성, 유종원. "AI-Based 2D CWT-CNN Model for Defect Classification in Wire Ropes Using Motion-Induced Eddy Current". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 조성준, 조현정, 이병주, 서영주, 유종원. "디지털 빔포밍의 이미지 빔에 의한 간섭 분석 및 억제를 위한 널링 기법". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 김준현, 이찬희, 김지영, 임영준, 유종원. "고정 안테나 구조 FMCW 드론 SAR에서 기준 누설 신호 감산을 이용한 IF/Baseband Noise Floor 저감 연구". *한국전자파학회 하계종합학술대회 8월, 2026*.
- 이지훈, 임영준, 강해찬, 김윤성, 유종원. "고이득 유전체 공진기 안테나의 3D 프린팅 Resolution 단차에 의한 특성 변화 연구". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 이효원, 서동민, 김성진, 박가영, 유종원. "5G 이동통신과 위성 통신 간 간섭 평가를 위한 RF 에뮬레이터 설계". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 김윤성, 조현정, 이효원, 조성준, 유종원. "기판 내 에어갭 위치 변화가 안테나 방사 특성에 미치는 영향 : 전계 분포 관점의 분석". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 강해찬, 이지훈, 서영주, 김지영, 유종원. "ISM 대역 무선 통신을 위한 USRP 기반 MIMO 시스템에서의 이종 변조 방식 구현 및 분석". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 김준현, 이찬희, 임성주, 장수민, 유종원. "낮은 부엽과 일정한 빔 폭을 갖는 L-band 이중 편파 비발디 안테나 설계". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 이찬희, 임영준, 김지영, 임성주, 유종원. "디지털 빔포밍 송신기에서 LO 위상 비동기화를 통한 누설 방사 저감". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 조성준, 김지영, 김윤성, 김준현, 유종원. "B5G 단말기를 위한 3차원 이중 대역 튜너블 안테나 설계". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 김지영, 조성준, 이지훈, 김준현, 유종원. "B5G RF 프론트엔드 시스템을 위한 안테나 튜너에 대한 연구". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 서영주, 이효원, 강해찬, 김성진, 유종원. "다중 수신기의 균일 충전을 위한 3차원 무선 충전 송신기 구조 설계". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 장수민, 조현정, 이찬희, 박가영, 유종원. "Compact Circular Polarization Cavity-Backed Cross Slot Antenna for 1U CubeSat". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 조현정, 김윤성, 임영준, 강해찬, 유종원. "A Wideband Stacked Multilayer Cavity Backed Slot Antenna for 5 GHz Wi-Fi Application". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 박가영, 이지훈, 서영주, 김준현, 유종원. "표면 전류 분포 해석을 통한 마이크로스트립 공진 패치 구조의 손실 메커니즘 분석". *한국전자파학회 동계종합학술대회 2월, 2026*.
- 임영준, 이찬희, 서영주, 이효원, 유종원. "병렬 선로 스위칭 기반의 임피던스 튜너를 이용한 재구성 가능한 전력 분배기". *한국전자파학회 동계종합학술대회 2월, 2026*.

**2025**

- Seong-Jin Kim, Hyeon-Jeong Cho, Jeong-Wook Kim and Jong-Won Yu. "High-Transparency and High-Efficiency Miniaturized Wideband Antenna Using Optimized Wired Metal Mesh for IoT Applications". *IEEE Internet of Things Journal, Dec. 2025*. DOI: <https://doi.org/10.1109/jiot.2025.3647523>.
- Chanhee Lee, Ji-Hoon Lee, Hyuk-Ja Kwon and Jong-Won Yu. "Rapid In-field 3-D Array Factor Estimation for Active Phased Array Antennas by Sweeping Phase of Excitation Signals". *IEEE Transactions on Antennas and Propagations, Jun. 2025*. DOI: <https://doi.org/10.1109/tap.2025.3579864>.
- Kyeong-Han Shin, Seong-Jin Kim, Kwon-Hyung Lee and Jong-Won Yu. "Analysis of multi-load distribution channel characteristics for air conditioner application". *Journal of Electromagnetic Waves and Applications, Jun. 2025*. DOI: <https://doi.org/10.1080/09205071.2025.2502776>.
- Seong-Jin Kim, Hyo-Won Lee, Tae-Dong Yeo, Jeong-Wook Kim, and Jong-Won Yu. "Single-step phase control method under cross-coupling between transmitting coils for omnidirectional wireless power transfer". *AEU-International Journal of Electronics and Communications, Jun. 2025*.
- Seong-Jin Kim, Dong-Min Seo, Ji-Hoon Lee, Sol Kim, and Jong-Won Yu. "Enhanced Compact RF Energy Harvesting System Using Two-Port Network of Antenna". *IEEE Microwave and Wireless Technology Letters, Mar. 2025*. DOI: <https://doi.org/10.1109/lmwt.2025.3543347>.
- Sol Kim, Seong-Jin Kim, Ji-Hoon Lee, Jong-Won Yu, and Dong-Jin Lee. "RF Energy Harvesting for Safe Monitoring of Rail Condition on Autonomous Trains". *IEEE Transactions on Vehicular Technology, Mar. 2025*. DOI: <https://doi.org/10.1109/tvt.2025.3554539>.
- Chanhee Lee, Hyunyoung Cho, ByungKuon Ahn, Woo-Kyung Lee, Jong-Won Yu, and Jeong-Wook Kim. "Design of Dual Polarized FMCW Radar System with Coupler Integrated Lens Antenna for Automotive SAR Application". *IEEE Transactions on Vehicular Technology, Jan. 2025*. DOI: <https://doi.org/10.1109/tvt.2025.3525670>.
- Hyo-Won Lee, Ga-Yeong Park, Ji-Young Kim, Sungjun Cho and Jong-won Yu. "Impact of 5G Adjacent Band Emissions on FSS Downlink Performance". *APMC 2025, Dec. 2025*. DOI: <https://doi.org/10.1109/apmc65046.2025.11379202>.
- Dong-Min Seo, Ji-Hoon Lee, Hyo-Won Lee, Ji-Young Kim and Jong-won Yu. "Analysis of Probe Coupling for Channel Property Optimization in an HVAC Duct". *APMC 2025, Dec. 2025*. DOI: <https://doi.org/10.1109/apmc65046.2025.11379252>.
- Yeong-Ju Seo, Seong-Jin Kim, Hyeon-Jeong Cho, Dong-Min Seo, Ji-Hoon Lee and Jong-Won Yu. "Design of Furniture Embedded 3-D Transmitting Coil for Multi-Receiver Wireless Power Transfer". *APMC 2025, Dec. 2025*. DOI: <https://doi.org/10.1109/apmc65046.2025.11379298>.
- Ji-Young Kim, Sungjun Cho, Seong-Jin Kim, Hyo-Won Lee, Yeong-Ju Seo and Jong-Won Yu. "A Calibration Method Compensating Impedance Difference of Signal Paths in Wideband Reflectometer for Semiconductor Process Chamber". *APMC 2025, Dec. 2025*. DOI: <https://doi.org/10.1109/apmc65046.2025.11379342>.
- Ji-Hoon Lee, Young-Jun Lim, Dongmin Seo, Yeong-Ju Seo, Hyeon-Jeong Cho and Jong-Won Yu. "Pattern-Reconfigurable Antenna with Multi-Permittivity Dielectric Lens Using Dual Layer 3-D Printing Method". *APMC 2025, Dec. 2025*. DOI: <https://doi.org/10.1109/apmc65046.2025.11378107>.
- Seong-Jin Kim, Yeong-Ju Seo, Hyo-Won Lee, Sungjun Cho and Jong-Won Yu. "Design of Expandable Transmitter for Extended Range in Omnidirectional Wireless Power Transfer". *ISAP 2025, Nov. 2025*. DOI: <https://doi.org/10.23919/isap63122.2025.11362084>.
- Sungjun Cho, Seong-Jin Kim, Ji-Young Kim, and Jong-Won Yu. "Phase Nonlinearity Compensation Under Low-Power Conditions in Wideband VNA Systems". *ISAP 2025, Nov. 2025*. DOI: <https://doi.org/10.23919/isap63122.2025.11362105>.
- Ga-Yeong Park, Hyo-Won Lee, Young-Jun Lim, Chanhee Lee, Ji-young Kim and Jong-Won Yu. "Design and Analysis of Phase Configuration in RIS-assisted Communication Systems". *EuMC 2025, Sep. 2025*.
- Hyeon-Jeong Cho, Ji-Hoon Lee, Ji-Young Kim, Dong-Min Seo, Yeong-Ju Seo, and Jong-Won Yu. "Coverage Estimation of 5G mmWave in Indoor Environment considering Human Body Shadowing". *EuMC 2025, Sep. 2025*. DOI: <https://doi.org/10.23919/eumc65286.2025.11235240>.
- Chanhee Lee, Seong-Ju Lim, Young-Jun Lim, Ga-Yeong Park, Chihyun Cheong, and Jong-Won Yu. "Phase-Offset Based Sidelobe Suppression for Co-frequency Multi-beam Systems". *2025 EuMC, Sep. 2025*. DOI: <https://doi.org/10.23919/eumc65286.2025.11234980>.
- Young-Jun Lim, Chanhee Lee, Hyeon-Jeong Cho, Ji-Young Kim, Hyuk-Ja Kwon, and Jong-Won Yu. "Amplitude-Only Measurement Based Calibration for Phased Arrays with Limited Power Detection Range". *EuMC 2025, Sep. 2025*. DOI: <https://doi.org/10.23919/eumc65286.2025.11235170>.
- 조성준, 김성진, 박가영, 서동민, 유종원. "AD8302 위상 검출기의 전력 의존적 비선형성 보정 기법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 김윤성, 조현정, 김지영, 박가영, 유종원. "광대역 특성을 갖는 공진기 배치 슬롯 안테나 설계". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 이효원, 서영주, 조성준, 김지영, 유종원. "능동 스캐닝 기반 다중 공진 모드 캐비티 내 물체 위치 추적 기법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 김성진, 조성준, 이효원, 유종원. "매시브 모드를 이용한 비정형 캐비티 구조의 내부 상태 변화 센싱 기법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 임영준, 김윤성, 서영주, 이지훈, 유종원. "조향각 내 이득 균일성을 제공하는 재구성 전력 분배기 기반 스위치드 빔 안테나". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 조현정, 김지영, 김윤성, 서동민, 유종원. "모드 중첩을 이용한 광대역 마그네틱 다이폴 안테나". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 김준현, 이찬희, 박가영, 조성준, 유종원. "슬롯 패치 안테나의 집적도 향상을 위한 E자형 급전 구조 설계". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 이찬희, 임영준, 김준현, 조현정, 유종원. "위상배열 안테나의 전방향 빔 스캐닝을 이용한 간이 환경에서의 방사 성능 측정 방법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 박가영, 이효원, 이찬희, 김준현, 유종원. "단위 셀의 전력 기여도 기반 선택적 위상 교란을 이용한 지능형 반사 표면의 사이드로브 억제 기법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 이지훈, 임영준, 이효원, 임성주, 유종원. "mm-Wave 위상 배열 안테나 시스템의 극소 다이폴 모델링을 활용한 고장 진단 연구". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 김지영, 조성준, 서동민, 서영주, 유종원. "실시간 프로브 상태 진단을 위한 Fabry-Pérot 구조 기반 프로브 설계". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 서동민, 이지훈, 조현정, 김윤성, 유종원. "다양한 분기 구조를 갖는 원형 도파관의 내부 채널 특성 분석". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 서영주, 이효원, 김준현, 임영준, 유종원. "다중 공진 모드 마이크로파 캐비티의 정밀 전기장 분포 제어를 위한 포트 배치 최적화 기법". *한국전자파학회 하계종합학술대회 8월, 2025*.
- 김성진, 김지영, 조성준, 신경한, 유종원. "딥러닝 기반 광대역 마이크로파 반사 측정법을 이용한 공정 챔버 상태 진단". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 김성진, 신경한, 김윤성, 김광만, 김성학, 이권형, 유종원. "다중 부하를 가지는 장거리 유선 채널 상의 신호 해석 기법". *제35회 통신정보 합동학술대회 4월, 2025*.
- 박가영, 이효원, 이찬희, 조현정, 유종원. "6G Upper-Mid 대역에서의 음영 지역 무선 전력 전송을 위한 지능형 반사 표면의 다중 배치". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 조성준, 이효원, 김성진, 서영주, 신기훈, 유종원. "와이어로프 MFL 신호 검출 내 기생 자기장 영향 분석 및 보정 전략". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 서영주, 김성진, 이효원, 서동민, 유종원. "충전 영역 확장을 위한 Built-in Furniture 무선 충전용 3차원 송신 코일 설계". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 김지영, 김성진, 조성준, 이찬희, 유종원. "광대역을 지원하는 방향성 결합기에 대한 부하 임피던스 변화에 따른 출력 전력 변화 교정 방법". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 이찬희, 신경한, 이효원, 이지훈, 유종원. "주파수가 분할된 Local Oscillation 신호의 무선 송수신을 통해 동기화된 바이스태틱 FMCW SAR". *한국전자파학회 동계종합학술대회, 2월, 2025*.
- 이효원, 조성준, 김성진, 박가영, 신기훈, 유종원. "와이어로프의 결함 검출을 위한 누설 자속 신호의 속도 효과 분석". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 이지훈, 조현정, 임영준, 임성주, 유종원. "단위 모듈 결합을 활용한 Ka-Band 대용량 위상 배열 안테나 시스템 설계". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 임영준, 이지훈, 김지영, 박가영, 유종원. "급전 소자 최소화를 위한 동시 급전 및 위상 천이 기반 패턴 재구성 안테나". *한국전자파학회 동계종합학술대회 2월, 2025*.
- 서동민, 이지훈, 김성진, 서영주, 유종원. "장거리 금속관 내부 분기구조에 따른 채널특성 분석 및 활용방안 제안". *한국전자파학회 동계종합학술대회 2월, 2025*.

**2024**

- Seong-Jin Kim, Heechul Jung, Jeong-Wook Kim, Hanam Kim, Sang-Won Lee, and Jong-Won Yu. "Design of a Compact Broadband Vector Network Analyzer to Diagnose a Semiconductor Process Chamber". *IEEE Transactions on Instrumentation and Measurement, Oct. 2024*. DOI: <https://doi.org/10.1109/tim.2024.3502828>.
- Sang Hyuck Han, Seong-Ju Lim, Jong-Won Yu, and Young-Dam Kim. "Antenna Pattern Measurement for Mobile Terminals via Magnetic Infinitesimal Dipole based Source Reconstruction". *IEEE Access, Jun. 2024*. DOI: <https://doi.org/10.1109/access.2024.3408326>.
- Hyunyoung Cho, Ji-Hoon Lee, Sol Kim, Jong-Won Yu, and Byoungkuon Ahn. "Series-Fed Integrated Lens Antenna for High Gain in Millimeter-Wave Band". *IEEE Antennas and Wireless Propagation Letters, vol. 23, no. 5, pp. 1578-1582, May. 2024*. DOI: <https://doi.org/10.1109/lawp.2024.3363182>.
- Ju-Ik Oh, Jong-Won Yu, and Young-Dam Kim. "Far-field pattern accuracy improvement in planar near-field measurement using infinitesimal dipole modeling". *Journal of Electromagnetic Waves and Applications, 1–13. Apr. 2024*. DOI: <https://doi.org/10.1080/09205071.2024.2354724>.
- Seong-Jin Kim, Seong-Ju Lim, Sung-Jae Hwang, and Jong-Won Yu. "Wireless Electric Field Sensor with Adaptive Voltage Gain for Measuring and Electrical Potential Treatment Chair". *IEEE Transactions on Industrial Electronics, Feb. 2024*. DOI: <https://doi.org/10.1109/tie.2024.3366200>.
- Seong-Jin Kim, Sol Kim, Ji-Hoon Lee, and Jong-Won Yu. "A Compact RF Energy Harvesting System with an Improved Impedance Matching Network". *IEEE Antennas and Wireless Propagation Letters, Vol. 23, pp.289-293, Jan. 2024*. DOI: <https://doi.org/10.1109/lawp.2023.3323355>.
- Seong-Jin Kim, Hyo-Won Lee, Yeong-Ju Seo, Dong-Min Seo, Ji-Young Kim, and Jong-Won Yu. "Current Control for Receiver Power Allocation of Omnidirectional Wireless Power Transfer". *ISAP 2024, Nov. 2024*. DOI: <https://doi.org/10.1109/isap62502.2024.10846123>.
- Ji-Hoon Lee, Hyeon-Jeong Cho, Chanhee Lee, Young-Jun Lim, Sungjun Cho and Jong-Won Yu. "Analysis of 3-D Prited Pattern-Reconfigurable Antenna using Property Variation of Material Infill Process". *ISAP 2024 Nov.2024*. DOI: <https://doi.org/10.1109/isap62502.2024.10846165>.
- Hyo-Won Lee, Kyung-Han Shin, Seong-Jin Kim, Sungjun Cho, Ga-Yeong Park and Jong-Won Yu. "Fast Numerical Simulation of Electric Field Distribution in Dielectric-Loaded Multimode Cavity". *ISAP 2024 Nov.2024*. DOI: <https://doi.org/10.1109/isap62502.2024.10846071>.
- Chanhee Lee, Kyeong-Han Shin, Ji-Hoon Lee, Hyo-Won Lee, Jeong-Wook Kim, Jong-Won Yu. "FMCW Monopulse Radar with an Orthogonally Polarized Dual-Beam Dielectric Resonator Antenna". *ISAP 2024 Nov.2024*. DOI: <https://doi.org/10.1109/isap62502.2024.10846511>.
- Sungjun Cho, Hyo-Won Lee, Seong-Jin Kim, Chanhee Lee, Ji-Hoon Lee, Kihoon Shin and Jong-Won Yu. "A Comprehensive Analysis of 3-D Magnetic Flux Leakage for External and Internal Defects". *ISAP 2024, Nov.2024*. DOI: <https://doi.org/10.1109/isap62502.2024.10846561>.
- Hyeon-Jeong Cho, Ji-Hoon Lee, Kyeong-Han Shin, Jong-Won Yu. "EVM Analysis of Chip-Integrated Phased Array Antenna Using USRP for 5G Communication". *EuMC 2024, Sep. 2024*. DOI: <https://doi.org/10.23919/eumc61614.2024.10732723>.
- 김성진, 김지영, 조성준, 신경한, 유종원. "Portable RF Reflectometer의 온도 영향 분석 및 보상 기법". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 이찬희, 이지훈, 조현정, 임성주, 권혁자, 유종원. "커플러 및 균등 결합분배기 내장과 하다마드 행렬을 이용한 위상 배열 시스템의 고속 진단 및 보정 방안 연구". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 이효원, 신경한, 김성진, 박가영, 유종원. "유전체를 포함한 다중 공진 모드 마이크로파 캐비티 시스템의 전기장 분포 분석을 위한 고속 해석 기법 연구". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 임영준, 이지훈, 조현정, 박가영, 유종원. "mm-Wave Wideband Microstrip to WR-12 Transition Using Stacked Patch with Notch Structure". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 이지훈, 조현정, 임영준, 신경한, 유종원. "77GHz 대역 고이득 유전체 공진기 안테나의 3-D 프린팅 내부채움 구조 및 밀도에 따른 특성 변화 연구". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 조성준, 이효원, 김성진, 서영주, 신기훈, 유종원. "와이어로프 누설 자기장 검출 시스템 설계를 위한 센서 자화 구조 최적화". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 서영주, 김성진, 이효원, 서동민, 유종원. "충전 영역 확장을 위한 3차원 하이브리드 다면체 송신 코일". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 김지영, 김성진, 조성준, 이찬희, 유종원. "Improvement of Gain/Phase Detector Nonlinearity for 5G New Radio". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 조현정, 이지훈, 임영준, 김지영, 유종원. "Periodic Anti-Reflection Cell Design for Dielectric Interface of mmWave Lens Antenna". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 신경한, 이찬희, 이지훈, 이효원, 유종원. "Time Delay Stretched FMCW 레이다의 서로 다른 두 국부 발진 신호 Deramping을 통한 시간 오차 분석". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 서동민, 김성진, 이지훈, 서영주, 유종원. "고층 빌딩 내 금속관 통신을 위한 안테나 최적 결합 연구". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 박가영, 이효원, 이찬희, 조성준, 유종원. "6G 대역에서의 음영 지역 무선 전력 전송을 위한 지능형 반사 표면 Focal Width 분석". *한국전자파학회 하계종합학술대회 8월, 2024*.
- 이효원, 이찬희, 조현영, 유종원. "위성 신호 수신을 위한 Ku-Band 소형 안테나 수신 시스템 설계". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 신경한, 김성진, 임성주, 조현영, 유종원. "Heating Performance 향상을 위해 다중 공진 모드를 이용한 마이크로파 캐비티 오븐". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 정희철, 이효원, 이지훈, 신경한, 유종원. "Accuracy Improvement on Steering Angle of a Phased Array System Using Virtual IMU". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 임성주, 한상혁, 김솔, 유종상, 유종원. "주파수 및 편파 분할을 이용한 다중 빔 안테나 연구". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 김성진, 정희철, 신경한, 이지훈, 유종원. "넓은 충전 영역을 위한 다중 송수신 무선 전력 충전 시스템 연구". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 조현영, 신경한, 이효원, 조현정, 유종원. "A cross-polarization and tilt-beam patch antenna structure with a dielectric sheet and cavity-backed slot fed for high isolation". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 이지훈, 조현정, 이찬희, 김성진, 조성준, 유종원. "단일 포트 원형 편파 특성을 위한 기생 소자 적층을 활용한 패치 안테나 기반 4x4 배열 설계". *한국전자파학회 동계종합학술대회 2월, 2024*.
- 조현정, 이지훈, 김성진, 이효원, 유종원. "Indentation Defected Ground Structure를 이용한 mmWave배열 안테나에서의 상호결합 개선". *한국전자파학회 동계종합학술대회 2월, 2024*.

**2023**

- Sol Kim, Hye-Won Jo, Jeong-Wook Kim, Ju-IK Oh, Jong-Won Yu and Byungkuon Ahn. "Curved-Retrodirective Beamforming System to Improve Microwave Power Transmission Efficiency in the Fresnel Region". *IEEE Internet of Things Journal, Vol.10, pp15012-15024, Sep. 2023*. DOI: <https://doi.org/10.1109/jiot.2023.3263519>.
- Jin Soo Lee\*, Jeong-Wook Kim\*, Jae Hee Lee, Yong Koo Son, Young Bin Kim, Kyoohee Woo, Chanhee Lee, Il-Doo Kim, Jae Young Seok, Jong-Won Yu, Jung Hwan Park, and Keon Jae Lee. "Flash-Induced High-Throughput Porous Graphene via Synergistic Photo-Effects for Electromagnetic Interference Shielding". *Nano-Micro Letters, Vol. 15 pp.191, Aug. 2023*.
- Seong-Jin Kim, Sol Kim, Ji-Hoon Lee, and Jong-Won Yu. "A Compact Broadband Stepped Bow-Tie Antenna for Ambient RF Energy Harvesting". *IEEE Access, Vol.11 pp.60365-60373, Jun. 2023*. DOI: <https://doi.org/10.1109/access.2023.3286535>.
- Hyunyoung Cho, Jae-Ho Lee, Jong-Won Yu, and ByungKuon Ahn. "Series-Fed Coupled Split-Ring Resonator Array Antenna with  Wide Fan-Beam and Low Sidelobe Level for Millimeter-Wave Automotive Radar". *IEEE Trans. on Vehicular Technology, Vol.72 pp.4805-4814, Apr. 2023*. DOI: <https://doi.org/10.1109/tvt.2022.3226294>.
- Sol Kim, Hyun-Jun Dong, Jong-Won Yu, and Han Lim Lee. "Phased Array Calibration System with High Accuracy and Low Complexity". *Elsevier Alexandria Engineering Journal, Vol.69 pp759-770, Feb. 2023*. DOI: <https://doi.org/10.1016/j.aej.2023.02.026>.
- Hyo-Won Lee, Seong-Jin Kim, Ji-Hoon Lee, Heechul Jung, Seongju Lim, Jong-Won Yu. "Optimal Size and Quantization Phase Control Resolution Study of Reconfigurable Intelligent Surface for 6G Wireless Communication System". *APMC 2023 Nov.2023*. DOI: <https://doi.org/10.1109/apmc57107.2023.10439742>.
- Ji-Hoon Lee, Seongju Lim, Seong-Jin Kim, Hyo-Won Lee, Heechul Jung, Jong-Won Yu. "Multi-Crossed Edge Slot with High Mode Patch Antenna for Wide Scanning Linear Phased Array". *APMC 2023 Nov.2023*. DOI: <https://doi.org/10.1109/apmc57107.2023.10439774>.
- Seong-Ju Lim, Ji-Hoon Lee, Heechul Jung, Seong-Jin Kim, Hyo-Won Lee, Jong-Won Yu. "Cylindrical Shaped Quasi Isotropic Wrap Around Antenna for Missile or UAV Communcation". *APMC 2023 Nov.2023*. DOI: <https://doi.org/10.1109/apmc57107.2023.10439889>.
- Seong-Jin Kim, Heechul Jung, Hyo-Won Lee, Seongju Lim, Ji-Hoon Lee, Jong-Won Yu, Jaehyun Kim, Sang Won Lee. "A Method for Diagnosing the Process Chamber Prior to Plasma Processes". *APMC 2023 Nov.2023*. DOI: <https://doi.org/10.1109/apmc57107.2023.10439894>.
- Hyunyoung Cho, Chan-Hee Lee, Jeong-Wook Kim, Sol Kim, and Jong-Won Yu. "Microstrip-Line Type Bruce Array Antenna with Low Sidelobe Level for Millimeter-Wave Radar". *EuMW 2023 Sep.2023*. DOI: <https://doi.org/10.23919/eurad58043.2023.10289280>.
- 조현정, 이지훈, 조현영, 이찬희, 유종원. "직사각형 메탈 루프를 이용한 H-Plane 선형 배열 패치 안테나에서의 상호결합 개선". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 신경한, 이찬희, 김정욱, 조현영, 유종원. "이중편파 바이스태틱 레이다의 편파합성을 통한 저피탐 표적의 탐지 성능 개선 연구". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 정희철, 김성진, 이효원, 유종원. "Design of Passive Beam-Steering Reconfigurable Intelligent Surface with Graphene and Copper Patch". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 이효원, 임성주, 김성진, 정희철, 유종원. "등가 상호 인덕턴스를 이용한 다중 무선 전력 충전 효율 계산". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 이지훈, 조현정, 이찬희, 조현영, 유종원. "단일 포트 원형 편파 특성을 위한 기생 소자 적층을 활용한 패치 안테나 설계". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 김성진, 이효원, 정희철, 김솔, 유종원. "챔버 상태 측정을 위한 벡터 네트워크 분석기 설계". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 조현영, 이지훈, 이찬희, 조현정, 유종원. "Degradation of beam patterns due to ADC/DAC quantization errors in digital beamforming". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 김정욱, 이찬희, 신경한, 김형주, 박경환, 유종원. "벽투과 인명 탐지를 위한 이중 편파 FMCW 레이다 시스템 및 편파 합성 기법에 대한 연구". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 김솔, 김병관, 유종원. "Received Signal Strength based Phase Optimization using Deep Neural Network in Distributed Phased Arrays". *한국전자파학회 하계종합학술대회 8월, 2023*.
- 정희철, 김솔, 이효원, 유종원. "Study on Reconfigurable Intelligent Surface using Graphene in Sub-THz". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 이찬희, 조현영, 이지훈, 유종원. "Suppressing Quantization Lobe of Phased Array Antenna Through Subarray Structure". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 이효원, 김솔, 정희철, 김구, 유종원. "입사각에 다른 지능형 반사 표면의 빔패턴을 고려한 경로 손실 모델". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 이지훈, 조현영, 이찬희, 오주익, 유종원. "기본 모드 패치와 모노폴 메탈 벽 커플링 요소를 활용한 광각 스캐닝 1x4 선형 위상 배열 안테나 설계". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 김성진, 김솔, 이지훈, 유종원. "포트 확장 기법을 적용한 RF 에너지 하베스팅 시스템 설계". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 김정욱, 김성진, 김익환, 김광석, 유종원. "다층 투명 전도성 산화물을 이용한 차량 전면 유리용 고효율 광대역 투명 안테나". *한국전자파학회 동계종합학술대회 2월, 2023*.
- 김솔, 박상현, 최선재, 허승우, 유종원, 이정훈. "Lens Antenna with Wide-Angle Coverage and Spatial Diversity for Microwave Power Transmission of LEO SSPS". *한국전자파학회 동계종합학술대회 2월, 2023*.

**2022**

- Hyunyoung Cho, Hye-Won Jo, Jeong-Wook Kim, Kwang-Seok Kim, and Jong-Won Yu. "Shorted Trapezoidal SIW Antenna with Quasi-Hemispherical Pattern for 2D Wide Scanning Planar Phased Array Antenna". *IEEE Trans.on Antennas and Propagation, Vol.70 pp.7211-7216, Aug. 2022*. DOI: <https://doi.org/10.1109/tap.2022.3161329>.
- Hyonik Lee, Se-Young Kim, Sol Kim, and Jong-Won Yu. "A Digital Filter Bank Based Method for Data Reduction in Spaceborne SAR Electronics". *IEEE Access, pp.100911-100921, Aug. 2022*. DOI: <https://doi.org/10.1109/access.2022.3200385>.
- Ju-Ik Oh, Jeong-Wook Kim, Sang Hyuck Han, Sol Kim, Jong-Won Yu, and In-June Hwang. "Pattern Reconfigurable Dual-Polarized Dipole Antenna With Staggered Parasitic Elements". *IEEE Access, pp.93773-93784, Aug. 2022*. DOI: <https://doi.org/10.1109/access.2022.3202951>.
- Ju-Ik Oh, Sung-Jun Yang, Sol Kim, Jong-Won Yu, and Young-Dam Kim. "Antenna Diagnostics based on Infinitesimal Dipole Modeling with Limited Measurement on Antenna Aperture". *IEEE Antennas and Wireless Propagation Letters, Vol.21 pp.923-927, May.2022*. DOI: <https://doi.org/10.1109/lawp.2022.3151894>.
- Taehee Jeong, Sungyeong Park, Jeong-Wook Kim, and Jong-Won Yu. "Robust CFAR Detector With Ordered Statistic of Sub-Reference Cells in Multiple Target Situations". *IEEE Access, Vol.10 pp.42750-42761, Apr. 2022*. DOI: <https://doi.org/10.1109/access.2022.3168707>.
- Sang Hyuck Han, Ikhwan Kim, Ju-Ik Oh, Hyo-Won Lee Seong-Jin Kim, and Jong-Won Yu. "An Accurate and Simple Method for Measurement of RF Characterization in Thin Substrate". *ISAP 2022 Nov.2022*. DOI: <https://doi.org/10.1109/isap53582.2022.9998792>.
- Hyunyoung Cho, Seong-Ju Lim, Sol Kim, Ju-Ik Oh, Chan-Hee Lee, and Jong-Won Yu. "Series-Fed Slit Ring Resonator Antenna Array With Wide Fan-Beam and High Gain". *ISAP 2022 Nov.2022*. DOI: <https://doi.org/10.1109/isap53582.2022.9998786>.
- Ji-Hoon Lee, Seong-Jin Kim, Sol Kim, Ju-Ik Oh, Chan-Hee Lee, and Jong-Won Yu. "Feasibility Analysis of Ambient RF Energy Harvesting for Low-Power IoT Devices". *ISAP 2022 Nov.2022*. DOI: <https://doi.org/10.1109/isap53582.2022.9998799>.
- Sol Kim, Seong-Jin Kim, Ji-Hoon Lee, Hyunyoung Cho, Hyo-Won Lee, and Jong-Won Yu. "RF Energy Harvesting System for Polarization Independence and Stability of Time-varying Signal". *ISAP 2022 Nov.2022*. DOI: <https://doi.org/10.1109/isap53582.2022.9998823>.
- Hyo-Won Lee, Jeong-Wook Kim, Seong-Jin Kim, Sang Hyuck Han, Ji-Hoon Lee, and Jong-Won Yu. "Wireless Power Charging System with DC Combined 3-Dimensional Receiver". *EuMC 2022 Sep.2022*. DOI: <https://doi.org/10.23919/eumc54642.2022.9924351>.
- Seong-Jin Kim, Jeong-Wook Kim, Hyo-Won Lee, Hyunyoung Cho, Ju-Ik Oh, and Jong-Won Yu. "Design of Multiple-Transmitter WPT System with Angular Misalignment Estimation from Mutual Inductance Tracking". *EuMC 2022 Sep.2022*. DOI: <https://doi.org/10.23919/eumc54642.2022.9924393>.
- Jeong-Wook Kim, Hyo-Won Lee, Sol Kim, Sang Hyuck Han, Ji-Hoon Lee, and Jong-Won Yu. "Circularly Polarized Phased Array System with Pattern Optimization Algorithm for Low SideLobe Level and Scanning Axial Ratio". *EuMC 2022 Sep.2022*. DOI: <https://doi.org/10.23919/eurad54643.2022.9924760>.
- Ju-Ik Oh, Hyunyoung Cho, Ji-Hoon Lee, Sang Hyuck Han, Chanhee Lee, and Jong-Won Yu. "Cavity PCB Process-Based Ka-Band Phased Array With Offset-Fed Aperture Coupled Patch Antenna". *EuMC 2022 Sep.2022*. DOI: <https://doi.org/10.23919/eumc54642.2022.9924420>.
- Jeong-Wook Kim, Sol Kim, Hyunyoung Cho, Soo-Chang Chae, ByungKuon Ahn, and Jong-Won Yu. "Design of Chip Integrated Circularly Polarized Phased Array System". *RFIT 2022 Aug.2022*.
- Sol Kim, Hyunyoung Cho, Jeong-Wook Kim, Hyo-Won Lee, and Jong-Won Yu. "Multi-Beam Metasurface Scheme using Polarization Matching for Improving Resource Efficiency". *RFIT 2022 Aug.2022*. DOI: <https://doi.org/10.1109/rfit54256.2022.9882445>.
- Hyunyoung Cho, Jeong-Wook Kim, Sol Kim, Ji-Hoon Lee, Ju-Ik Oh, and Jong-Won Yu. "Grating Lobe Suppression in Wide-Angle Scanning Phased Array With Large Inter Element Spacing by Subarray Roatation". *RFIT 2022 Aug.2022*. DOI: <https://doi.org/10.1109/rfit54256.2022.9882462>.
- Jeong-Wook Kim, Ju-Ik Oh, Hyunyoung Cho, Ikhwan Kim, and Jong-Won Yu. "Design of mmWave High-Resolution FMCW Radar System with Real-Time Radar State Tracking Method". *GSMM 2022 May.2022*.
- Hyunyoung Cho, Jeong-Wook Kim, Ju-Ik Oh, Chanhee Lee, and Jong-Won Yu. "High Gain Pattern Reconfigurable Dielectric Resonator Antenna for Wide Scanning in E- Band". *GSMM 2022 May.2022*.
- Ju-Ik Oh, Hyunyoung Cho, Jeong-Wook Kim, Ji-Hoon Lee, Sang Hyuck Han, and Jong-Won Yu. "Design of Aperture Coupled Ka-Band Phased Array Antenna Using Cavity PCB Process". *GSMM 2022 May.2022*. DOI: <https://doi.org/10.1109/gsmm53818.2022.9792322>.
- 이찬희, 임성주, 오주익, 유종원. "국부발진기 신호 송신을 위한 바이스태틱 FMCW 레이더 시스템 설계". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 이효원, 김솔, 김구, 유종원. "Determination of Reconfigurable Intelligent Surface Size in 6G Wireless Communication". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 이지훈, 조현영, 오주익, 유종원. "광각 스캐닝을 위한 기본 모드 패치와 모노폴 기반의 금속벽의 커플링을 이용한 안테나 설계". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 김익환, 한상혁, 유종상, 유종원. "Analysis of strip edge conductor loss in mmWave". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 김성진, 김정욱, 이효원, 유종원. "3차원 무선전력충전을 위한 상호 인덕턴스 동시 추적 기법". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 임성주, 김솔, 김정욱, 유종원. "차폐벽을 활용한 안테나 자가 교정 커플러 성능 개선". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 조현영, 이찬희, 이지훈, 유종원. "모노폴과 유사 패턴을 가지는 가운데 급전 패치 안테나". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 김정욱, 조현영, 조혜원, 이지훈, 유종원. "수동 소자로 구성된 편파 위상 변조 통신 수신기 설계". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 김솔, 이지훈, 조현영, 유종원. "Grating Lobe Suppression of Periodic Antenna Array with Large Element". *한국전자파학회 하계종합학술대회 8월, 2022*.
- 조현영, 이지훈, 김솔, 안병권, 유종원. "DRA를 이용한 높은 이득을 가지는 다중빔 방사 소자". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 임성주, 김솔, 김익환, 유종상, 유종원. "원형 실린더 구조 상의 전방향성 방사 패턴을 갖는 배열 안테나". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 이효원, 임성주, 김성진, 유종원. "중거리 무선 전력 충전을 위한 고효율 송신 코일 설계". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 이찬희, 이효원, 한상혁, 유종원. "3~5 GHz의 광대역 FMCW 레이더를 위한 발룬 역할을 하는 저주파 통과 필터 설계". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 이지훈, 조현영, 이찬희, 오주익, 유종원. "광각 스캐닝 위상 배열 안테나 시스템을 위한 다중 슬롯 결합 고차모드 패치 안테나 설계". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 김정욱, 이찬희, 조현영, 유종원. "광대역 광각 원형 편파 능동 위상 배열 시스템에 대한 연구". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 김익환, 한상혁, 김정욱, 유종원. "저손실 얇은 유전체 기판의 RF 특성 추정 기법 정리". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 김솔, 김성진, 이지훈, 이동진, 유종원. "Feasibility Study on Robust Self-powered and Maintanace -free Sensor System for Autonomous Train Control System". *한국전자파학회 동계종합학술대회 2월, 2022*.
- 김성진, 김정욱, 이효원, 유종원. "다중 송신기 간 상호 인덕턴스를 고려한 최적의 무선 전력 충전 효율을 위한 제어 기법". *한국전자파학회 동계종합학술대회 2월, 2022*.

**2021**

- Jeong-Wook Kim, Hye-Won Jo, Kwang-Seok Kim, Ghoo Kim, Soo-Chang Chae, and Jong-Won Yu. "Gain Enhanced Wide Azimuth Beam Antenna Using Half-Mode Substrate Integrated Waveguide Cavity for Automotive Rear-View Mirror Application". *IEEE Trans. on Vehicular Technology, Vol.71 pp.33-40, Nov. 2021*. DOI: <https://doi.org/10.1109/tvt.2021.3130893>.
- Jeong-Wook Kim, Ju-Ik Oh, Kwang-Seok Kim, Jong-Won Yu, Kang-Jae Jung and Il-Nam Cho. "Efficiency-Improved UWB Transparent Antennas Using ITO/Ag/ITO Multilayer Electrode Films". *IEEE Access, Vol.9 pp.165385-165393, Nov.2021*. DOI: <https://doi.org/10.1109/access.2021.3131868>.
- 김정욱, 천형일, 조현영, 이우경, 유종원. "소형 무인 항공기 적용을 위한 X-대역 합성 개구면 레이다 시스템 설계". *한국군사과학기술학회 종합학술대회 11월, 2021*.

## 과제

수행 기간이 2021년 10월 13일–2026년 10월 13일과 겹치는 과제 27건이다. 시작만 적힌 수행 중 과제는 종료일을 덧붙이지 않았고, 지원기관과 기간은 연구실의 게시 표기다.[^projects]

- 항만 크레인 와이어로프 자기신호 해석 고도화 및 AI 성능검증 기술 개발 (지원 해양수산부; 기간 2026.07 ~ ; 상태 수행 중)
- 차세대 회로박 SI 예측 기법 개발 (지원 롯데 에너지머티리얼즈; 기간 2026.05 ~ ; 상태 수행 중)
- 2-in-1 레이더 고주파 부품 시뮬레이션 (지원 한라 IMS; 기간 2026.04 ~; 상태 수행 중)
- 드론 SAR 및 디지털트윈 연계 급경사지 붕괴 위험성 분석 기술개발 (지원 행정안전부; 기간 2025.02 ~; 상태 수행 중)
- 디지털 빔포밍 안테나 설계 기술 (지원 한화 시스템; 기간 2025.01 ~; 상태 수행 중)
- ISM 응용을 위한 지능형 마이크로파 에너지 시스템 핵심 원천기술 개발 (지원 정보통신기획 평가원; 기간 2023.04 ~ ; 상태 수행 중)
- 고주파 신호를 이용한 공정 챔버 모니터링 시스템 (지원 중소기업 기술개발 지원사업; 기간 2023.12 ~ ; 상태 수행 중)
- 다중빔제어 3차원 초지향성 소자를 활용한 mm-Wave/sub-THz 대역의 동시 다중빔 위상 배열 기술 (지원 한국 연구 재단; 기간 2023.03 ~ 2026.02; 상태 이전 과제)
- 6세대 Tbps급 데이터 전송율을 지원하는 sub-THz 대역 무선 전송 및 접속 요소 기술 개발 (지원 정보통신기획 평가원; 기간 2021.01 ~ 2025.12; 상태 이전 과제)
- 다중 무선 충전을 위한 근역 자기장 성형 원천기술 개발 (지원 정보통신기획 평가원; 기간 2021.04 ~ 2025.12; 상태 이전 과제)
- 메탈 외관 디자인의 오디오 제품 안테나 기술 개발 (지원 LG 전자; 기간 2025.03 ~ 2026.01; 상태 이전 과제)
- 160도급 빔포밍 특성의 평판형 배열 안테나 시스템 개발 (지원 민군협력 진흥원; 기간 2021.08 ~ 2025.07; 상태 이전 과제)
- 차세대 SAR에 관한 연구 (지원 국방과학연구소; 기간 2019.12~2025.12; 상태 이전 과제)
- 주거환경 실내 장거리 무선통신을 위한 HVAC Duct 이용 통신 확장 기술 개발 (지원 LG 전자; 기간 2024.01~2025.11; 상태 이전 과제)
- 에어컨 차세대 고속 유선 통신 기술 분석 및 구현기술 연구 (지원 LG 전자; 기간 2023.08~2024.12; 상태 이전 과제)
- 휴대용 ESA 위성통신 단말 제작 (지원 한화 시스템; 기간 2023.08~2024.12; 상태 이전 과제)
- 통신 탑재체용 다중빔포밍 안테나 설계 기술 (지원 한화 시스템; 기간 2021.12~2024.12; 상태 이전 과제)
- 챔버 상태 측정용 1-포트 벡터 네트워크 분석기 개발 (지원 (주) 이서; 기간 2023.01~2023.12; 상태 이전 과제)
- 5G Dual-Tx 동작을 위한 RF Front End 구조 최적화 연구 (지원 삼성전자 MX사업부; 기간 2022.08~2023.12; 상태 이전 과제)
- RF 무선전력전송을 위한 파형 최적화 연구 (지원 KSA; 기간 2023.02~2023.12; 상태 이전 과제)
- 다중빔제어 3차원 초이득 소자를 활용한 mm-Wave/sub-THz대역 대용량 능동 배열 안테나 소형화 및 저전력화 (지원 한국연구재단; 기간 2020.03~2023.02; 상태 이전 과제)
- RF 무선전력전송의 효율 향상 연구 (지원 KSA; 기간 2022.02~2022.12; 상태 이전 과제)
- 저유전 FCCL을 이용한 FPCB 특성 측정 및 밀리미터파 대역 통신부품 개발 (지원 SK넥실리스; 기간 2021.12~2022.11; 상태 이전 과제)
- 차세대 비가시성 소재 및 차량용 광대역 안테나 개발 (지원 LG전자 차세대 표준연구소; 기간 2021.08 ~ 2022.08; 상태 이전 과제)
- 중거리 무선전력전송 효율 향상 연구 (지원 KSA; 기간 2021.02~2021.12; 상태 이전 과제)
- 곡사포탄용 무지향성 안테나 기술 분석 및 구현 (지원 풍산기술 연구소; 기간 2021.02~2021.12; 상태 이전 과제)
- 다중 안테나 기반 동일 자원을 활용한 정보 및 전력 동시 전송 시스템 개발 (지원 정보통신기술진흥센터; 기간 2017.04~2021.12; 상태 이전 과제)

## 수상과 선정

연구실 Awards 목록의 수상 26건이다. 연도만 적힌 항목의 연도는 누리집의 연도 구역 표기이고 날짜는 게시되어 있지 않다. 소식 쪽이 같은 수상의 날짜를 적은 한 항목은 그 날짜를 함께 썼다.[^awards][^news]

- 2025 · 조이흠, 정현석, 이상훈, 이상민, 김선우, 이찬희, 김준현 제 6회 밀리테크 챌린지 부총리 겸 과학기술정보통신부장관상 대상
- 2025 · 김윤성, 조현정, 김지영, 박가영, 유종원 KIEES 2025년도 하계종합학술대회 우수논문상
- 2025-10-27 · 유종원 과학기술정보통신부 표창상
- 2025 · 이효원, 서영주, 조성준, 김지영, 유종원 KIEES 2025년도 하계종합학술대회 우수논문상
- 2025 · 박가영, 이효원, 이찬희, 김준현, 유종원 KIEES 2025년도 하계종합학술대회 우수논문상 IEEE AP-S Seoul Chapter Chair Award
- 2025 · 이찬희, 신경한, 이효원, 이지훈, 유종원 KIEES 2025년도 동계종합학술대회 우수논문상 최우수상
- 2024 · 정현석, 조이흠, 박효열, 이유상, 주민승, 이찬희, 신경한 제 5회 밀리테크 챌린지 육군사관학교장상 우수상
- 2024 · 이찬희, 김성진, 박가영 한화 스페이스허브-KAIST 우주연구센터 주관 2024 Space Grand Challenge 아이디어 공모전 은상
- 2024 · 신경한, 이찬희, 이지훈, 이효원, 유종원 KIEES 2024년도 하계종합학술대회 우수논문상
- 2024 · 이효원, 신경한, 임성주, 유종원 KIEES 2024년도 하계종합학술대회 우수논문상
- 2024 · 신경한, 김성진, 임성주, 조현영, 유종원 KIEES 2024년도 동계종합학술대회 우수논문상
- 2024 · 김성진, 정희철, 신경한, 이지훈, 유종원 KIEES 2024년도 동계종합학술대회 우수논문상
- 2023 · 이지훈, 조현정, 이찬희, 조현영, 유종원 KIEES 2023년도 하계종합학술대회 우수논문상
- 2023 · 신경한, 이찬희, 김정욱, 조현영, 유종원 KIEES 2023년도 하계종합학술대회 우수논문상
- 2023 · 김성진, 이효원, 정희철, 김솔, 유종원 KIEES 2023년도 하계종합학술대회 우수논문상
- 2023 · 김솔 Young-Han Kim Global Leader Scholarship Award
- 2023 · 정희철, 김솔 이효원, 유종원 KIEES 2023년도 동계종합학술대회 우수논문상
- 2023 · 이지훈, 조현영, 이찬희, 오주익, 유종원 KIEES 2023년도 동계종합학술대회 우수논문상
- 2023 · 김솔, 박상현, 최선재, 허승우, 유종원, 이정훈 KIEES 2023년도 동계종합학술대회 우수논문상
- 2022 · 김정욱 Student Competition Finalist, 2022 IEEE International Symposium on Radio-Frequency Integration Technology 최우수상
- 2022 · 이지훈, 조현영, 오주익, 유종원 KIEES 2022년도 하계종합학술대회 우수논문상
- 2022 · 김솔, 이지훈, 조현영, 유종원 KIEES 2022년도 하계종합학술대회 우수논문상
- 2022 · 김정욱 Han Chul-Hi Augustine Scholarship Award : EE Best Researcher Award
- 2022 · 김정욱 Kim Choing-Ki Award : EE Top Research Achievement Award
- 2022 · 김정욱, 이찬희, 조현영, 유종원 KIEES Best Paper Award 우수논문상
- 2022 · 김성진, 김정욱, 이효원, 유종원 KIEES 2022년도 동계종합학술대회 우수논문상

## 소식

2021년 10월 13일–2026년 10월 13일에 해당하는 소식 쪽의 논문 게재 승인·학회 채택 소식 8건이다. 학술지 논문은 「게재 승인」, 학회 논문은 「채택」으로 구분했다.[^news]

- 2025-05-16 · 이찬희·조현정·임영준·박가영의 EuMC 2025 논문 채택을 알렸다.
- 2024-10-25 · 김성진의 IEEE Transactions on Instrumentation and Measurement 논문 게재 승인을 알렸다.
- 2024-09-01 · 김성진·이지훈·이효원·이찬희·조성준의 ISAP 2024 논문 채택을 알렸다.
- 2024-05-22 · 조현정의 EuMC 2024 논문 채택을 알렸다.
- 2024-05-22 · 조현영의 IEEE Antennas and Wireless Propagation Letters 논문 게재 승인을 알렸다.
- 2024-02-13 · 김성진의 IEEE Transactions on Industrial Electronics 논문 게재 승인을 알렸다.
- 2024-01-18 · 김성진의 IEEE Antennas and Wireless Propagation Letters 논문 게재 승인을 알렸다.
- 2023-12-05 · 임성주·김성진·이지훈·이효원의 APMC 논문 채택을 알렸다.

## 연락과 위치

- 교수 이메일: drjwyu67@kaist.ac.kr[^prof]
- 교수 전화: +82-42-350-3478.[^prof]
- 교수 사무실: KAIST E3-2 5204호(연구실 교수 소개), 전기및전자공학부동 E3-2 서 5203호(학부 교수 소개).[^prof][^dept]
- 연구실: KAIST 전기및전자공학부동 E3-2 5210호.[^intro]
- 주소: 대전광역시 유성구 대학로 291, 34141.[^intro]
- 연구실 대표: 이찬희, chanheelee@kaist.ac.kr[^intro][^members]

## 각주
[^intro]: 연구실 소개. <https://sites.google.com/view/rfss/introduction> 관측 2026-11-09.
[^prof]: 유종원 교수 소개. <https://sites.google.com/view/rfss/members/professor> 관측 2026-11-09.
[^members]: 현재 구성원. <https://sites.google.com/view/rfss/members/current-members> 관측 2026-11-09.
[^alumniph]: 박사 졸업생. <https://sites.google.com/view/rfss/members/alumni-ph-d> 관측 2026-11-09.
[^alumnims]: 석사 졸업생. <https://sites.google.com/view/rfss/members/alumni-m-s> 관측 2026-11-09.
[^alumnipost]: 이전 박사후연구원. <https://sites.google.com/view/rfss/members/alumni-post-doctor> 관측 2026-11-09.
[^topic]: 연구 주제. <https://sites.google.com/view/rfss/research/research-topic> 관측 2026-11-09.
[^projects]: 과제. <https://sites.google.com/view/rfss/research/projects> 관측 2026-11-09.
[^journals]: 국제 학술지 논문. <https://sites.google.com/view/rfss/publication/international-journal> 관측 2026-11-09.
[^conferences]: 국제 학회 논문. <https://sites.google.com/view/rfss/publication/international-conference> 관측 2026-11-09.
[^domestic]: 국내 학회 논문. <https://sites.google.com/view/rfss/publication/domestic-conference> 관측 2026-11-09.
[^awards]: 수상. <https://sites.google.com/view/rfss/publication/awards> 관측 2026-11-09.
[^dept]: KAIST 전기및전자공학부 유종원 교수 상세 소개. <https://ee.kaist.ac.kr/professor/12226/> 관측 2026-11-09.
[^news]: 연구실 News. <https://sites.google.com/view/rfss/news> 관측 2026-11-09.
[^p1]: S.-J. Lim 외, J.-W. Yu, IEEE Antennas and Wireless Propagation Letters (2026). <https://doi.org/10.1109/lawp.2026.3653565> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p2]: S.-J. Kim, H.-J. Cho, J.-W. Kim, J.-W. Yu, IEEE Internet of Things Journal (2025). <https://doi.org/10.1109/jiot.2025.3647523> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p3]: C.-H. Lee, J.-H. Lee, H.-J. Kwon, J.-W. Yu, IEEE Transactions on Antennas and Propagation (2025). <https://doi.org/10.1109/tap.2025.3579864> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p4]: K.-H. Shin, S. Kim, K. H. Lee, J.-W. Yu, Journal of Electromagnetic Waves and Applications (2025). <https://doi.org/10.1080/09205071.2025.2502776> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p5]: S.-J. Kim 외, J.-W. Yu, IEEE Microwave and Wireless Technology Letters (2025). <https://doi.org/10.1109/lmwt.2025.3543347> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p6]: S.-J. Kim 외, S.-W. Lee, IEEE Transactions on Instrumentation and Measurement (2024). <https://doi.org/10.1109/tim.2024.3502828> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p7]: S. Kim 외, B. Ahn, IEEE Internet of Things Journal (2023). <https://doi.org/10.1109/jiot.2023.3263519> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^p8]: H.-W. Lee, B. Kim, J.-W. Yu, S. Kim, Alexandria Engineering Journal (2026). <https://doi.org/10.1016/j.aej.2026.01.038> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.
[^medical]: S.-J. Kim 외, Wireless Electric Field Sensor With Adaptive Voltage Gain for Measuring an Electrical Potential Treatment Chair, IEEE Transactions on Industrial Electronics (2024). <https://doi.org/10.1109/tie.2024.3366200> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://openalex.org/A5024677342>. 관측 2026-11-09.

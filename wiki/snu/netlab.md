# 네트워크 연구실 (Network Laboratory, NETLAB)

**서울대학교 공과대학 전기·정보공학부 · 박세웅 교수**

- 분야: 무선 통신 규약과 사물인터넷, 이동통신과 실시간 서비스, 네트워크 보안, 학습 모델의 기기 적응
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^home][^p1][^p2], 컴퓨터 네트워크[^home][^p3][^p4], 네트워크 보안·프라이버시[^home][^p5]
- 홈페이지: <https://sites.google.com/netlab.snu.ac.kr/netlabhome>
- 근거와 출처: [네트워크 연구실 근거 페이지](netlab-sources.md)

> 무선으로 기기들이 자료를 주고받는 규칙과 경로를 설계하고, 이동통신의 실시간 서비스 품질과 기기의 영역 인증, 기기에 맞춘 학습 모델을 연구한다.[^home][^p3][^p4][^p5][^p6]

## 무엇을 연구하나

NETLAB은 무선 네트워크(기기들이 전파로 자료를 주고받도록 연결한 통신망)의 프로토콜(통신 당사자들이 자료를 주고받기 위해 따르는 규칙)을 이론과 실험으로 연구한다. 첫 화면은 이동통신, 사물인터넷(Internet of Things, IoT: 기기들이 인터넷에 연결되어 자료를 주고받는 체계), Wi-Fi(무선 근거리 통신 기술), 네트워크 보안, 학습을 활용한 모바일 응용을 관심 분야로 든다. 무선 신호를 보내고 받는 물리 계층부터 사용자 서비스를 다루는 응용 계층까지 규약을 구현하고 분석한다.[^home]

첫째 갈래는 **서로 다른 무선 기술의 공존과 저전력 기기의 연결**이다. B-hop은 Wi-Fi의 비컨(주변 기기에 통신망 정보를 알리는 신호)이 올 시간을 예측해, BLE(Bluetooth Low Energy, 블루투스 저전력 통신)의 주파수 도약(시간에 따라 사용 주파수를 바꾸는 동작) 시점을 조절한다.[^p1] AURORA는 LoRa(전력 사용을 억제한 장거리 무선 통신 기술)의 멀티홉(여러 중계 기기를 거치는 자료 전달) 망에서 연결마다 확산 계수(처프 신호가 표현하는 정보량과 신호 지속 시간을 정하는 매개변수)를 조절한다. 처프는 주파수가 시간에 따라 변하는 신호다. 연결별 자료 전달 성공률을 예측하고 통신에 쓰는 에너지를 고려해 조절하는 방법이다.[^p2] MobiRPL은 이동하는 기기가 자료를 중계할 수 있도록 라우팅(자료를 목적지까지 보낼 경로를 정하는 절차)을 설계하고 구현했다.[^p3]

둘째 갈래는 **이동통신의 연결과 서비스 품질**이다. QCON은 여러 기지국에 동시에 연결하는 이동통신 기능을 활용해 실시간 영상의 품질을 다룬다. 사용자가 느끼는 서비스 품질(Quality of Experience, QoE)을 무선 접속망(Radio Access Network, RAN: 단말과 기지국을 연결하는 통신망) 안에서 추정하고, 예비 연결을 활용할 시점과 링크(기기 사이의 통신 연결)별 자료 전송을 조절한다. 기지국 운영 정책을 고려하면서 영상 재생이 멈추는 문제를 줄이려는 연구다.[^p4] Research는 이 갈래와 함께 Network Measurement라는 측정 주제도 구분해 둔다.[^research]

이 갈래에는 **수요를 분산하는 요금 설계와 비행 중 연결 품질 측정**도 있다. 시간·지역별 요금을 미리 알려 이동통신 수요를 분산하려고, 강화학습(행동을 시도하고 그 결과의 보상으로 행동 방식을 배우는 방법)을 이용한다. 여러 에이전트(각자 판단해 행동하는 학습 주체)를 함께 학습시키고 각자 지역 정보로 실행하는 요금 결정 방법을 연구했다.[^p7] 드론 연구에서는 실제 비행으로 상공의 이동통신 연결 품질 변화를 확인하고, 사전 학습(새 용도에 적용하기 전에 모델을 미리 학습시키는 과정) 없이 계획된 평면 경로를 따라 비행하면서 고도를 선택하는 방법을 제안했다.[^p8]

셋째 갈래는 **지정된 영역 안의 기기만 허용하는 보안**이다. SWORD는 Wi-Fi의 채널 상태 정보(Channel State Information, CSI: 신호가 통신 경로를 지나며 겪는 변화를 나타내는 정보)를 이용해 기기가 지정한 영역 안에 있는지 판별한다. 한 부류 분류(One-Class Classification, OCC: 한 부류의 자료를 학습해 그 부류에 속하는지 판별하는 방법)를 써서 영역 내부 자료만으로 학습할 수 있게 했다. 기기의 절대 좌표를 구하기보다 허용된 영역 안인지 판단하는 방식이다.[^p5]

넷째 갈래는 **학습 모델을 기기의 자원에 맞추는 방법**이다. 신경망(연결된 계산 단위가 가중치를 조절해 자료의 관계를 학습하는 모형)의 수치를 양자화(값을 유한한 대표값들에 대응시키는 일)할 때 쓰는 비트 폭(수치를 표현하는 비트의 개수)을 바꾸는 연구다. 메타학습(여러 학습 과제를 통해 새로운 과제에 적응하는 방법을 배우는 절차)에 비트 폭을 과제의 일부로 넣어, 학습한 모델을 다른 비트 폭이나 새로운 분류 대상에 맞추도록 했다.[^p6]

## 주요 연구 주제

### 1. 무선 접속과 사물인터넷

Wi-Fi와 BLE의 간섭을 피하는 전송 시점 조절, LoRa 멀티홉의 연결별 적응, 이동하는 저전력 기기의 라우팅을 연구한다.[^p1][^p2][^p3]

### 2. 이동통신과 실시간 서비스

기지국의 다중 연결과 예비 링크를 활용한 실시간 영상 전송, 시간·지역별 요금으로 수요를 분산하는 학습, 드론의 이동통신 품질을 위한 비행 고도 선택을 연구한다.[^p4][^p7][^p8]

### 3. 네트워크 보안과 영역 인증

Wi-Fi 신호가 통신 경로에서 겪는 변화와 학습을 이용해 기기가 지정된 영역 안에 있는지 판별한다.[^p5]

### 4. 학습 모델의 기기 적응

메타학습과 양자화를 결합해 기기의 수치 표현 자원과 새로운 분류 대상에 맞는 신경망 모델을 연구한다.[^p6]

## 대표 논문

2021–2026년 논문 가운데 박세웅 교수가 저자이고 서울대 소속 연구로 게시된 논문을 연구 갈래별로 골랐다. 교수가 마지막 저자인 8편이며, 2026년 논문 2편을 포함한다. “쉽게 말하면” 칸은 각 논문의 초록만을 근거로 썼다. 6번은 ECCV 2022 발표 예정임을 밝힌 arXiv 사전 공개본의 초록을 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2024 | [B-hop: Time-domain Adjustment of BLE Frequency Hopping Against Wi-Fi Beacon Interference](https://doi.org/10.1109/JIOT.2023.3337252) · IEEE Internet of Things Journal | Wi-Fi 접속 장치가 보내는 비컨이 주변 BLE 통신을 방해하는 문제를 다룬다. 비컨이 전송될 시간을 예측하고 BLE가 통신 주파수를 바꾸는 시점을 조절해 충돌을 피하는 B-hop을 만들었다. Wi-Fi와 BLE가 함께 있는 BLE 주 장치에서 작동하며, Wi-Fi 기기나 BLE 종속 기기를 바꾸지 않아도 된다. 시제품과 모의실험으로 주파수만 조절하는 기존 방식보다 성능이 개선됨을 보였다.[^p1] | 1저자 Wonbin Park, 마지막 저자 박세웅 |
| 2 | 2026 | [AURORA: Adaptive Spreading Factor Control for Low-power Multihop LoRa Network](https://doi.org/10.23919/JCN.2025.000084) · Journal of Communications and Networks | 동물 추적처럼 이동 범위를 포괄해야 하는 LoRa 통신에서 연결마다 상태에 맞춰 신호 설정을 바꾸는 방법을 만들었다. 각 확산 계수의 자료 전달 성공률을 예측하고 에너지 효율을 고려해 연결별로 설정을 조절한다. 실내·실외 실험에서 안정적인 통신과 통신 범위 확장을 유지하면서 에너지 사용을 줄였다.[^p2] | 1저자 Eunjeong Park, 마지막·공동 교신저자 박세웅 |
| 3 | 2022 | [MobiRPL: Adaptive, Robust, and RSSI-based Mobile Routing in Low Power and Lossy Networks](https://doi.org/10.23919/JCN.2022.000004) · Journal of Communications and Networks | 전력과 통신 신뢰성에 제약이 있는 망에서 기기가 움직여도 자료 전달 경로를 유지하는 문제를 다룬다. 기존 저전력 통신망의 라우팅 규약을 바탕으로 수신 신호 세기 등을 이용하는 MobiRPL을 구현했다. 이동 상황에서 경로의 신뢰성을 유지하는 데 초점을 맞추고 운영체제 구현, 모의실험, 실제 시험망으로 평가했다.[^p3] | 1저자 Hongchan Kim, 마지막 저자 박세웅 |
| 4 | 2026 | [QCON: Seamless QoE-Aware 5G Streaming via Multi-Connectivity](https://www.usenix.org/conference/nsdi26/presentation/lee) · NSDI 26 | 이동통신 예비 연결을 아끼는 운영 정책 때문에 실시간 영상이 한 연결의 품질 변화에 영향을 받는 문제를 다룬다. 사용자 서비스 품질을 접속망 안에서 추정하고, 그 필요에 맞춰 예비 링크와 여러 링크의 전송을 조절하는 QCON을 제안했다. 영상 중단을 막기 위한 우선순위 기반 재전송 방식도 설계했으며, 실제 통신망 제어 기능을 구현한 시험망에서 평가했다.[^p4] | 1저자 Goodsol Lee, 마지막 저자 박세웅 |
| 5 | 2021 | [Secure Region Detection using Wi-Fi CSI and One-Class Classification](https://doi.org/10.1109/ACCESS.2021.3076176) · IEEE Access | 사물인터넷 기기가 지정된 영역 안에 있을 때만 작동하거나 통신망에 참여하도록 하는 방법이다. 기기의 정확한 좌표 대신 영역 안인지 판별하며, Wi-Fi 채널 상태 정보와 한 부류 분류를 결합한 SWORD를 만들었다. 영역 내부 자료만으로 학습할 수 있고, 실제 환경 실험으로 영역 밖 기기를 거부하는 능력과 영역 안 기기를 허용하는 능력을 평가했다.[^p5] | 1저자 Yongjae Yoo, 마지막·교신저자 박세웅 |
| 6 | 2022 | [Bitwidth-Adaptive Quantization-Aware Neural Network Training: A Meta-Learning Approach](https://arxiv.org/abs/2207.10188) · ECCV 2022, arXiv 사전 공개본 | 기기마다 계산·저장 자원이 다를 때 학습한 신경망을 여러 비트 폭으로 바꾸는 문제를 다룬다. 메타학습 과제에 비트 폭을 포함해 양자화 학습과 결합했다. 기기에 배치한 모델의 비트 폭을 바꾸는 경우와, 적은 예시로 새로운 분류 대상을 배우면서 비트 폭도 바꾸는 경우를 위한 변형을 제안하고 실험했다.[^p6] | 1저자 Jiseok Youn, 마지막 저자 박세웅 |
| 7 | 2025 | [SHIFT: Multi-agent Reinforcement Learning for Spatiotemporal Mobile Traffic Shaping via Dynamic Pricing](https://doi.org/10.1109/tnsm.2025.3618117) · IEEE Transactions on Network and Service Management | 이동통신 수요가 시간·지역별로 몰리는 문제를 동적 요금으로 다룬다. 요금을 미리 알려 이용 수요의 시간·공간 이동을 유도하고 최대 수요를 분산하는 방법이다. 여러 학습 주체를 중앙에서 함께 학습시키고 각자는 지역 정보로 실행하는 강화학습 알고리즘을 제안했다. Telecom-Italia의 실제 통신량 자료로 여러 주체가 참여할 때의 확장성과 최대 수요 감소를 평가했다.[^p7] | 1저자 Sihyun Choi, 마지막 저자 박세웅 |
| 8 | 2025 | [ASCEND: Altitude Selection for High-quality Cellular Connectivity on Drones](https://doi.org/10.1109/tvt.2025.3594092) · IEEE Transactions on Vehicular Technology | 지상 이용자를 중심으로 설치된 이동통신 안테나에 드론이 연결할 때 비행 고도가 연결 품질에 미치는 영향을 다룬다. 실제 드론 실험으로 상공의 연결 품질 변화를 확인하고, 계획된 평면 경로를 따라 비행하면서 고도를 선택하는 강화학습 방법을 제안했다. 사전 학습을 요구하지 않으며, 여러 실제 장소에서 예상 자료 전달 성능의 증가와 연결 품질이 낮은 비행 구간의 비중 감소를 평가했다.[^p8] | 1저자 Yongjae Yoo, 마지막 저자 박세웅 |

## 교수와 전문 분야

학과 교수 소개는 박세웅을 교수로 표시하고, 전문 분야를 네트워크 설계와 성능 분석으로 적는다.[^prof] 연구실 Faculty는 서울대학교 전기·정보공학부 재직 기간을 1994–2026년으로 적고, 2026년 5월부터 한국전자통신연구원(ETRI, Electronics and Telecommunications Research Institute) 원장이라고 소개한다. 관심 분야는 통신망 성능 분석, 스마트 그리드(정보통신으로 전력망의 생산·전달·사용을 관리하는 체계), 유·무선망 자원 할당과 네트워크 보안이다.[^faculty] 대표 논문에서는 무선 기술의 공존과 이동 라우팅, 실시간 이동통신 서비스, 무선 신호 기반 보안과 학습 모델의 기기 적응을 다룬다.[^p1][^p3][^p4][^p5][^p6]

## 응용 분야

동물 추적 같은 사물인터넷의 이동 통신망, 실시간 영상 서비스, 지정된 영역 안에서만 기기를 허용하는 인증, 자원이 서로 다른 기기에 학습 모델을 배치하는 일을 다룬다.[^p2][^p4][^p5][^p6]

## 구성원

People의 현재 Postdoctral Researcher 2명, Ph.D. Students 12명, Master Students 2명이다. 과정·직위는 게시 구획을 따랐다. 대표 논문 참여는 게시 영문 이름을 저자 이름과 대조했고, 같은 이름의 저자를 같은 사람으로 보아 표시했다. 기준일은 2026년 10월 26일이다.[^people]

| 이름 | 과정 | 대표 논문 참여 |
|---|---|---|
| Jihwan Suh | 박사후연구원 | 5, 8 |
| Jiseok Youn | 박사후연구원 | 6 |
| Minsoo Na | 박사과정 |  |
| Youngseok Kim | 박사과정 |  |
| Jinmyeong Lee | 박사과정 |  |
| Dokyun Ryoo | 박사과정 |  |
| Deokjin Kim | 박사과정 |  |
| Subin Huh | 박사과정 | 7 |
| Junha Park | 박사과정 |  |
| Sungbo Eo | 박사과정 | 1, 2 |
| Geonhee Lee | 박사과정 |  |
| Yunseo Nam | 박사과정 |  |
| Juhun Shin | 박사과정 |  |
| Dongrak Choi | 박사과정 | 8 |
| Florissa Yusufi Nurzahra | 석사과정 |  |
| Jewoon Lee | 석사과정 |  |

## 졸업생과 이전 구성원

People의 Alumni에 게시된 전체 126행이다. 박사후연구원 1행, 박사 64행, 박사과정 수료 1행, 석사 59행, 교환학생 1행이며, 서로 다른 학위·구획에 같은 사람이 다시 나올 수 있다. 연월과 진로는 게시 표기다. 학위·과정 연도는 1997–2026년이며 교환학생은 2018년 7월–2019년 1월 방문 기간으로 적혀 있다.[^people]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 박수호 (Suho Park) | Postdoc (Feb. 2004) | KT |
| 양진모 (Jinmo Yang) | Ph.D. (Aug. 2026) | PostDoc@SNU |
| 윤지석 (Jiseok Youn) | Ph.D. (Aug. 2026) | PostDoc@SNU |
| 이굳솔 (Goodsol Lee) | Ph.D. (Feb. 2026) | Nokia Bell Labs |
| 서지환 (Jihwan Suh) | Ph.D. (Feb. 2026) | PostDoc@SNU |
| 박종연 (Jongyeon Park) | Ph.D. (Aug. 2025) | Electronics and Telecommunications Research Institute (ETRI) |
| 유용재 (Yongjae Yoo) | Ph.D. (Feb. 2025) | Mobile eXperience Business, Samsung Electronics |
| 백승우 (Seungwoo Baek) | Ph.D. (Feb. 2025) |  |
| 박정준 (Jeongjun Park) | Ph.D. (Feb. 2025) | System LSI Business, Samsung Electronics |
| 이강현 (Kanghyun Lee) | Ph.D. (Feb. 2025) | Mobile eXperience Business, Samsung Electronics |
| 최시현 (Sihyun Choi) | Ph.D. (Aug. 2024) | System LSI Business, Samsung Electronics |
| 박은정 (Eunjeong Park) | Ph.D. (Aug. 2024) | Samsung Research |
| 이지환 (Jihwan Lee) | Ph.D. (Aug. 2024) | System LSI Business, Samsung Electronics |
| 김정준 (Jungjun Kim) | Ph.D. (Feb. 2024) |  |
| 황선욱 (Sunwook Hwang) | Ph.D. (Aug. 2023) | System LSI Business, Samsung Electronics |
| 김홍찬 (Hongchan Kim) | Ph.D. (Aug. 2023) | Sejong University |
| 곽철영 (Chulyoung Kwak) | Ph.D. (Feb. 2023) | Hyundai Motor Group |
| 이기택 (Kitaek Lee) | Ph.D. (Aug. 2022) | Samsung Research, Samsung Electronics |
| 이명섭 (Myungsup Lee) | Ph.D. (Aug. 2022) | System LSI Business, Samsung Electronics |
| 김지훈 (Jihoon Kim) | Ph.D. (Aug. 2021) | System LSI Business, Samsung Electronics |
| 박원빈 (Wonbin Park) | Ph.D. (Aug. 2021) | Mobile Communication Business, Samsung Electronics |
| 정성훈 (Sunghoon Jung) | Ph.D. (Feb. 2021) | CTO, LG Electronics |
| 이재홍 (Jaehong Yi) | Ph.D. (Feb. 2021) | Samsung Research, Samsung Electronics |
| 최시영 (Siyoung Choi) | Ph.D. (Feb. 2021) | CTO, LG Electronics |
| 최준영 (Junyoung Choi) | Ph.D. (Aug. 2020) | Samsung Research, Samsung Electronics |
| 윤호영 (Hoyoung Yoon) | Ph.D. (Aug. 2020) | Samsung Research, Samsung Electronics |
| 손영욱 (Youngwook Son) | Ph.D. (Aug. 2020) | Postdoc@SNU |
| 김준석 (Junseok Kim) | Ph.D. (Aug. 2020) | System LSI Business, Samsung Electronics |
| 홍승근 (Seung Geun Hong) | Ph.D. (Feb. 2020) | Network Business, Samsung Electronics |
| 이현중 (Hyunjoong Lee) | Ph.D. (Feb. 2020) | Samsung Research, Samsung Electronics |
| 이규진 (Gyujin Lee) | Ph.D. (Feb. 2020) | Mobile Communication Business, Samsung Electronics |
| 양창목 (Changmok Yang) | Ph.D. (Feb. 2020) | Mobile Communication Business, Samsung Electronics |
| 강병준 (Byungjun Kang) | Ph.D. (Feb. 2020) | Samsung Research, Samsung Electronics |
| 임경래 (Gyeongrae Im) | Ph.D. (Aug. 2019) | Electronics and Telecommunications Research Institute (ETRI) |
| 이주현 (Juhyun Lee) | Ph.D. (Aug. 2019) | Mobile Communication Business, Samsung Electronics |
| 허정륜 (Jeongyoon Heo) | Ph.D. (Aug. 2019) | Samsung Research, Samsung Electronics |
| 정승범 (Seungbeom Jeong) | Ph.D. (Aug. 2019) | Samsung Research, Samsung Electronics |
| 옥진우 (Jinwoo Ock) | Ph.D. (Aug. 2019) | Samsung Research, Samsung Electronics |
| 이태섭 (Taeseop Lee) | Ph.D. (Aug. 2017) | Samsung Research, Samsung Electronics |
| 한종훈(Jonghun Han) | Ph.D. (Aug. 2017) | Sejong University |
| 박원형 (Won-hyoung Park) | Ph.D. (Aug. 2017) | SK |
| 강대호 (Daeho Kang) | Ph.D. (Feb. 2016) | Mobile Communication Business, Samsung Electronics |
| 김형신 (Hyung-sin Kim) | Ph.D. (Feb. 2016) | Seoul National University |
| 박세용 (Se-yong Park) | Ph.D. (Feb. 2016) | System LSI Business, Samsung Electronics |
| 박상규 (Sangkyu Park) | Ph.D. (Aug. 2015) | Network Business, Samsung Electronics |
| 임희수 (Heesu Im) | Ph.D. (Aug. 2015) | System LSI Business, Samsung Electronics |
| 장서우 (Seowoo Jang) | Ph.D. (Aug. 2015) | Samsung Research, Samsung Electronics |
| 남창원 (Changwon Nam) | Ph.D. (Feb. 2015) | Trineedle |
| 윤성국 (Sung-Guk Yoon) | Ph.D. (Aug. 2012) | Soongsil University |
| 류선희 (Sun-Heui Ryoo) | Ph.D. (Aug. 2012) | Samsung Network Business ,Samsung Electronics |
| 이종욱 (Jongwook Lee) | Ph.D. (Feb. 2012) | Samsung Advanced Institute of Technology |
| 장혁진 (Hyuk-Chin Chang) | Ph.D. (Aug. 2011) | Samsung System LSI Business, Samsung Electronics |
| 김영욱 (Youngwook Kim) | Ph.D. (Feb. 2010) | Attached Institute of ETRI |
| 박우길 (Wooguil Pak) | Ph.D. (Aug. 2009) | Yeungnam University |
| 김병승 (Byungseung Kim) | Ph.D. (Feb. 2009) | Samsung System LSI Business,Samsung Electronics |
| 김종택 (Jongtack Kim) | Ph.D. (Feb. 2009) | Naver |
| 윤정균 (Jeongkyun Yun) | Ph.D. (Aug. 2008) | Google Korea |
| 이능형 (Neung-Hyung Lee) | Ph.D. (Aug. 2007) | Samsung Network Business, Samsung Electronics |
| 최영준 (Young-June Choi) | Ph.D. (Feb. 2006) | Ajou University |
| 주창희 (Changhee Joo) | Ph.D. (Feb. 2005) | Korea University |
| 최진구 (Jin-Ghoo Choi) | Ph.D. (Feb. 2005) | Yeungnam University |
| 김진호 (Jin-Ho Kim) | Ph.D. (Feb. 2004) | Google |
| 임형규 (Hyoung-Kyu Lim) | Ph.D. (Aug. 2003) | Samsung Network Business, Samsung Electronics |
| 송진한 (Jinhan Song) | Ph.D. (Feb. 2003) | SK Telecom |
| 김준환 (Joonhwan Kim) | Ph.D. (Feb. 2001) | Libergon |
| 이관석 (Gwan-Seok Lee) | Ph.D. Coursework Complete (Aug. 2013) | Samsung Electronics |
| 백선기 (Sunkee Baik) | Master (Aug. 2026) |  |
| 정용훈 (Yonghoon Jeong) | Master (Feb. 2026) | Republic of Korea Naval Academy |
| 최유빈 (Yubin Choi) | Master (Feb. 2026) | University of California, Riverside |
| 김영민 (Youngmin Kim) | Master (Feb. 2026) | Samsung VD Business |
| 박지민 (Jimin Park) | Master (Aug. 2025) | KT |
| 주우성 (Woosung Joo) | Master (Feb. 2024) | Shinhan Bank |
| 김덕진 (Deokjin Kim) | Master (Aug. 2022) | NETLAB Ph.D course |
| 윤예린 (Yelin Yoon) | Master (Aug. 2022) | LG Electronics |
| 최혁주 (Hyeogju Choi) | Master (Aug. 2021) | Jamcoding |
| 박정준 (Jungjun Park) | Master (Aug. 2020) | NETLAB Ph.D course |
| 임수훈 (Suhun Lim) | Master (Feb. 2020) | Memory Division, Samsung Electronics |
| 강성준 (Seongjoon Kang) | Master (Feb.2019) | New York University Tandon School of Engineering |
| 우동연 (Dongyeon Woo) | Master (Feb. 2018) | Hashed |
| 최경산 (Kyungsan Choi) | Master (Aug. 2016) |  |
| 강동규 (Dongkyu Kang) | Master (Aug. 2016) | TmaxSoft |
| 조호수 (Hosoo Cho) | Master (Feb. 2016) | SNU Ph.D course |
| 임명홍 (Minghong Lim) | Master (Aug. 2015) | LG Electronics |
| 이용훈 (Yonghun Lee) | Master (Feb. 2015) | TESCOM |
| Husam Fahmi | Master (Aug. 2014) | Samsung Electronics |
| 최영준 (Youngjun Choi) | Master (Aug. 2014) | Samsung Electronics |
| 이령 (Ryeong Lee) | Master (Aug. 2014) | LG Electronics |
| 서정오 (Jeong-O Seo) | Master (Feb. 2014) | TMAX |
| Elena Emelianova | Master (Aug. 2012) | Samsung Electronics |
| Qu han | Master (Aug. 2012) | Hynix |
| Chuadhry Mujeeb Ahmed | Master (Feb. 2012) | Lecturer |
| Nalin Chakoo | Master (Aug. 2011) | Samsung Electronics |
| Nikolay Kuznetsov | Master (Aug. 2010) | Samsung Electronics |
| 조경탁 (Kyong-Tak Cho) | Master (Feb. 2010) | Netflix |
| 류성한 (Sunghan You) | Master (Feb. 2010) | LS Cable |
| Asim Rasheed | Master (Feb. 2010) | Samsung Electronics |
| 임성수 (Seongsu Lim) | Master (Aug. 2009) | Hyundai Motor Company |
| 옥정엽 (Jeong-Yeob Oak) | Master (Feb. 2009) | Samsung Electronics |
| 김균태 (Kyun-Tae Kim) | Master (Feb. 2009) |  |
| 윤장묵 (Jang Muk Yoon) | Master (Feb. 2008) |  |
| 지리민 (Li min Ji) | Master (Aug. 2007) | Samsung Electronics |
| 정기범 (Ki Bum Jeong) | Master (Aug. 2007) | LG Electronics |
| 동징징 (Jing Jing Dong) | Master (Feb. 2007) | Huawei |
| 이원보 (Won-bo Lee) | Master (Aug. 2006) | Samsung Electronics |
| Abhinav Arora | Master (Feb. 2006) |  |
| 안재현 (Jae Hyun Ahn) | Master (Feb. 2006) |  |
| 손정환 (Junghwan Son) | Master (Feb. 2006) |  |
| 전정현 (Jung Hyun Jun) | Master (Feb. 2005) | Lee & Ko Law Firm |
| 최영배 (Youngbea Choi) | Master (Feb. 2005) |  |
| 대영군 (Yongjun Dai) | Master (Aug. 2004) |  |
| 홍재성 (Jaesung Hong) | Master (Feb. 2004) | SK Telecom |
| 박경미 (Kyungmi Park) | Master (Feb. 2003) | KIM&CHANG Law Firm |
| 손희정 (Heejung Sohn) | Master (Feb. 2003) |  |
| 정흥철 (Heung-Chul Jung) | Master (Feb. 2002) | NHN Investment |
| 서승철 (Seung Chul Seo) | Master (2001) | Samsung Electronics |
| 권일환 (Il Hwan Kwon) | Master (2001) | McKinsey & Company |
| 김진태 (Jin-tae Kim) | Master (Feb. 2001) | SK Telecom |
| 이재영 (Jae Young Lee) | Master (Aug. 2000) |  |
| 이수영 (Sooyoung Lee) | Master (Feb. 2000) | CJ |
| 이동환 (Donghwan Lee) | Master (Feb. 1998) | KIM&CHANG Law Firm |
| Mohamed Malki | Master (Feb. 1998) | Public Service in Colorado, USA |
| 이진솔 (Jinsol Lee) | Master (Feb. 1998) |  |
| 윤선근 (Sunkeun Yoon) | Master (Feb. 1998) | KIM&CHANG Law Firm |
| 김영섭 (Young Sub Kim) | Master (Feb. 1997) | SK Telecom |
| 박용현 (Yong Hyeon Park) | Master (Feb. 1997) |  |
| Abdul Waheed | Exchange Student (Jul. 2018 ~ Jan. 2019) | University of Hazara |

## 최근 논문 목록 (2021–2026)

Publication 하위 목록의 2021–2026년 구역에서 국제 학술지 35편, 국제 학회 44건, 국내 학회 67건을 실었다. 국내 학술지 목록의 게시 연도는 2019년까지다. 학회 목록은 정식 논문과 포스터·시연·초청 논문을 포함한다. 연도는 누리집의 연도 구역을 따랐고, 게재 예정으로 적힌 항목은 그 상태를 표시했다. 날짜 없는 게재 예정 항목도 누리집이 둔 연도 구역을 따른다.[^journals][^conferences][^domestic-journals][^domestic-conferences]

**2026**

- Dokyun Ryoo, Jihwan Suh, Jeongyeup Paek, and Saewoong Bahk. "SAFE: Spatially-Aligned Feature Extraction for Metal Detection via Top-View UWB Radar". *게재 예정: IEEE Internet of Things Journal, 2026*.
- Jongyeon Park, Youngwook Son, Kanghyun Lee, Jonghun Han, and Saewoong Bahk. "Demystifying Multi-Link Device Behavior and Performance under Network Saturation in Wi-Fi 7". *게재 예정: IEEE Transactions on Networking, 2026*.
- Yongjae Yoo, Seungmin Choi, Jeongyeup Paek, and Saewoong Bahk. "Polarization Alignment for Cellular-based Mobile Aerial Communication". *게재 예정: IEEE Transactions on Vehicular Technology, 2026*.
- Younghoon Jeong, Youngwook Son, and Saewoong Bahk. "On the Interference Resilience of Non-Linear Chirp Modulation for LoRa: An Analytical Insight into Energy Scattering Effect". *게재 예정: IEEE Communications Letters, 2026*.
- Jeongjun Park, Sunwook Hwang, Hyeonho Noh, Jin Mo Yang, Hyun Jong Yang and Saewoong Bahk. "ALERT Open Dataset and Input-Size-Agnostic Vision Transformer for Driver Activity Recognition using IR-UWB". *게재 예정: IEEE Access, 2026*.
- Yubin Choi , Yunseo Nam, Dongrak Choi, Jeongyeup Paek, and Saewoong Bahk. "UniQ: A Universal-Rate Quantization Network for Beyond-5G Autoencoder-Based CSI Feedback". *게재 예정: IEEE GLOBCOM 2026, Macau S.A.R., China, Dec 7 - 11, 2026*.
- Jewoon Lee, Youngseok Kim, and Saewoong Bahk. "ROI-Guided Raw Point Filtering for Bandwidth-Efficient V2X Cooperative Perception". *게재 예정: IEEE VTC Fall 2026, Boston, USA, September 06 - 09, 2026*.
- Deokjin Kim, Jeongyeup Paek, and Saewoong Bahk. "Lucid: LiDAR-based UAV Classification and Detection for Airspace Surveillance". *게재 예정: IEEE ICDCS 2026, Seoul, South Korea, June 22 - 25, 2026*.
- Sihyun Choi, Sungbo Eo, Changhee Joo, and Saewoong Bahk. "Interference Prediction and Beam Alignment in 5G Indoor mmWave UDNs". *게재 예정: IEEE WiOpt 2026 , Columbus, OH, USA, June 3-6, 2026*.
- Dongrak Choi, Yongjae Yoo, Yubin Choi, Jeongyeup Paek, and Saewoong Bahk. "Escaping from the Shadow: Bottleneck-Aware UAV Placement for High-Throughput Relaying". *게재 예정: IEEE VTC-Spring, Nice, France, June 9-12, 2026*.
- Youngmin Kim, Dongrak Choi, and Saewoong Bahk. "An Advanced DC-PLC Architecture for Smart Display Systems". *게재 예정: IEEE ICCE 2026, Dubai, UAE, Feb 3-5, 2026*.
- Dokyun Ryoo, Yongjae Yoo, Jeongyeup Paek, and Saewoong Bahk. "NOVA: Navigation Optimization via UWB-Assisted Iterative Path Planning for UAV Delivery". *게재 예정: IEEE INFOCOM 2026, Tokyo, Japan, May 18-21, 2026*.
- Goodsol Lee, Seyeon Kim, Juheon Yi, Junhong Min, Tuan Tran, Kyunghan Lee, and Saewoong Bahk. "PAVE: Mitigating Non-Congestive Delay for Seamless Video Calls over NextG Mobile Networks". *게재 예정: IEEE INFOCOM 2026, Tokyo, Japan, May 18-21, 2026*.
- Goodsol Lee, Junhong Min, Seyeon Kim, Juheon Yi, Kwang Taik Kim, Mung Chiang, Sangtae Ha, Kyunghan Lee, and Saewoong Bahk. "QCON: Seamless QoE-Aware 5G Streaming via Multi-Connectivity". *게재 예정: USENIX Symposium on Network Systems Design and Implementation (NSDI'26), Renton, WA, United States, May 4-6, 2026*.
- 어성보, 박세웅. "2.4 GHz 대역에서 LoRa와 Wi-Fi의 공존 성능 분석". *한국통신학회 동계종합학술발표회 2026, Feb. 04 - 06, 2026*.
- 이제운, 박세웅. "V2X 기반 협력 인지 시스템의 확장성 향상에 관한 연구". *한국통신학회 동계종합학술발표회 2026, Feb. 04 - 06, 2026*.

**2025**

- Jihwan Lee, Youngwook Son, Tiago Koketsu Rodrigue, Yishi Zhu, Chulyoung Kwak, and Saewoong Bahk. "TouchAI: Towards Waterproof Mobile Touchscreen Interface via Acoustic-Inertial Sensing Modalities". *게재 예정: IEEE Internet of Things Journal, 2025*.
- Eunjeong Park, Sungbo Eo, Hongchan Kim, Jeongyeup Paek, and Saewoong Bahk. "AURORA: Adaptive Spreading Factor Control for Low-power Multihop LoRa Network". *게재 예정: The Journal of Communications and Networks, 2025*.
- Sihyun Choi, Taewoo Kang, Subin Huh, Sung-Guk Yoon, and Saewoong Bahk. "SHIFT: Multi-agent Reinforcement Learning for Spatiotemporal Mobile Traffic Shaping via Dynamic Pricing". *게재 예정: IEEE Transactions on Network and Service Management, 2025*.
- Dongrak Choi, Yubin Choi, Yonghoon Jeong, Jeongyeup Paek, and Saewoong Bahk. "D²-PLC: Holistic Design and Implementation of High-Datarate Duplex DC Power Line Communication Network". *IEEE Internet of Things Journal, vol.12, Issue.21, pp. 45325-45340, 2025*.
- Yongjae Yoo, Jihwan Suh, Dongrak Choi, Jeongyeup Paek, and Saewoong Bahk. "ASCEND: Altitude Selection for High-quality Cellular Connectivity on Drones". *게재 예정: IEEE Transactions on Vehicular Technology, 2025*.
- Youngwook Son and Saewoong Bahk. "Bringing Spatial Reuse into Practice for Distributed Wi-Fi Networks: Preamble Detection and Anomalies". *게재 예정: IEEE Journal on Selected Areas in Communications, 2025*.
- Jin Mo Yang, Sunwook Hwang, Jeongjun Park, and Saewoong Bahk. "FrameBoost: Advanced Video Analytics with Inference Trigger Frame Selection via Tracking Error Estimation". *IEEE Access, vol.13, pp. 61748- 61759, April. 2025*.
- Sunkee Baik, Dongrak Choi, and Saewoong Bahk. "Towards Accurate Wi-Fi 6E-based Liquid Sensing in a Static Environment". *ICTC 2025, Jeju Island, Korea, Oct. 14-17, 2025*.
- Yubin Choi, Yunseo Nam, and Saewoong Bahk. "Intelligent Channel State Information Feedback Using Variable-Rate Autoencoder". *ICTC 2025, Jeju Island, Korea, Oct. 14-17, 2025*.
- Junha Park and Saewoong Bahk. "5G Latency Analysis for Optimal TCP Cubic Congestion Control for 5G". *ICTC 2025, Jeju Island, Korea, Oct. 14-17, 2025*.
- Dongrak Choi and Saewoong Bahk. "Experimental Study on mmWave FMCW Radar for Detecting Objects beyond Transparent Barriers". *ICTC 2025, Jeju Island, Korea, Oct. 14-17, 2025*.
- Deokjin Kim and Saewoong Bahk. "Challenges in LiDAR-based Detection of High-Speed UAVs: Experimental Analysis". *ICTC 2025, Jeju Island, Korea, Oct. 14-17, 2025*.
- Junha Park and Saewoong Bahk. "Poster: Seamless Cellular-WLAN Aggregation with Connectivity-Aware Flow Control". *IEEE ICNP 2025 poster, Seoul, Korea, Sep. 23-25, 2025*.
- Dongrak Choi, Yonghoon Jeong, Yubin Choi, and Saewoong Bahk. "Demo: A Programmable High-Throughput Duplex DC-PLC Testbed for Power and Data Integration". *IEEE ICNP 2025 demo, Seoul, Korea, Sep. 23-25, 2025*.
- Youngmin Kim, Kanghyun Lee, Youngwook Son, and Saewoong Bahk. "HActiFi: Towards Practical ISAC for Human Activity Recognition via Smart TV Infrastructure". *IEEE VTC 2025 fall, Chengdu, china, Oct. 19-22, 2025*.
- Jimin Park, Geonhee Lee, Jeongyeup Paek, and Saewoong Bahk. "Cupid: Fast and Reliable Convergecast-over-UWB Protocol for Dense Internet of Things". *IEEE DCOSS-IoT 2025, Tuscany (Lucca), Italy, June 9-11, 2025. (Best paper runner-up)*.
- Youngseok Kim, Sunwook Hwang, Hyung-Sin Kim, and Saewoong Bahk. "ConcreTizer: Model Inversion Attack via Occupancy Classification and Dispersion Control for 3D Point Cloud Restoration". *ICLR 2025, Singapore EXPO, Apr. 24-28, 2025*.
- Kanghyun Lee, Youngwook Son, Jongyeon Park, and Saewoong Bahk. "Enriching Multi-User OFDMA in Wi-Fi Networks with Frequency-Selective Channel Awareness". *IEEE INFOCOM 2025, London, United Kingdom, May 19-22, 2025*.
- Juhun Shin, Goodsol Lee, Jeongyeup Paek, and Saewoong Bahk. "César: Cellular Resource Scheduling-Aware Congestion Control". *IEEE INFOCOM 2025, London, United Kingdom, May. 19-22, 2025*.
- Woosung Joo, Goodsol Lee, and Saewoong Bahk. "Understanding Delayed Reaction of MPTCP Scheduler Over 5G for Realtime Applications". *IEEE WCNC 2025, Milan, Italy, Mar. 24–27, 2025*.
- 박준하, 박세웅. "TCP Cubic Congestion Control의 O-RAN 구조에서의 활용". *한국통신학회 하계종합학술발표회 2025, Jun. 18 - 21, 2025*.
- 이건희, 박세웅. "LoRa backscatter 기술의 연구 동향에 관한 고찰". *한국통신학회 하계종합학술발표회 2025, Jun. 18 - 21, 2025*.
- 허수빈, 박세웅. "셀룰러 환경에서의 L4S 지원을 위한 전송 계층 혼잡 제어에 관한 연구". *한국통신학회 하계종합학술발표회 2025, Jun. 18 - 21, 2025*.
- 최동락, 박세웅. "셀룰러 음영지역 연결을 위한 Relay UAV 배치 알고리즘에 관한 연구". *한국통신학회 하계종합학술발표회 2025, Jun. 18 - 21, 2025*.
- 류도균, 박세웅. "시뮬레이션을 통한 DOP 와 위치 추정 오차의 관계 분석". *제 35회 통신정보 합동학술대회 2025, Apr. 23-Apr.25, 2025*.
- 김덕진, 박세웅. "라이다(LiDAR) 기반 UAV 탐지 연구의 최신 동향과 실질적 적용을 위한 향후 과제". *제 35회 통신정보 합동학술대회 2025, Apr. 23-Apr. 25, 2025*.
- 윤지석, 유용재, 박세웅. "Open-RAN 지능형 네트워크 제어의 운용 효율화 및 다양한 테스트 환경에서의 성능 일반화를 위한 대형 언어 모델 기반 네트워크 제어 기술의 필요성". *한국통신학회 동계종합학술발표회 2025, Feb. 05-07, 2025*.
- 최유빈, 이진명, 박세웅. "Performance Evaluation and Analysis of Dual 5G Multipath TCP in Mobile Environments". *한국통신학회 동계종합학술발표회 2025, Feb. 05-07, 2025*.
- 백선기, 이건희, 박세웅. "6G 기반 Integrated Sensing and Communication". *한국통신학회 동계종합학술발표회 2025, Feb. 05-07, 2025*.
- 김영민, 류도균, 박세웅. "외부 간섭 환경에서 Wi-Fi CSI 데이터 특성 분석". *한국통신학회 동계종합학술발표회 2025, Feb. 05-07, 2025*.

**2024**

- Seungwoo Baek, Siyoung Choi, and Saewoong Bahk. "DACS: User Association and TDMA Framing for Low-latency Services on Integrated Access and Backhaul Networks". *IEEE Transactions on Vehicular Technology, vol.74, Issue.5 , pp 8110-8125, Jan. 2025*.
- Jungjun Kim, Jihwan Lee, and Saewoong Bahk. "Energy-Efficient and Robust Communication in Multi-Connectivity Enabled mmWave Ultra-Dense Networks". *IEEE Transactions on Green Communications and Networking, vol.9, Issue.2 , pp 621-634, August. 2024*.
- Minsoo Na, Jaehyun Lee, Giwan Choi, Takki Yu, Jeongsik Choi, Jinyoung Lee, and Saewoong Bahk. "Operator’s Perspective on 6G: 6G Services, Vision, and Spectrum". *IEEE Communications Magazine, vol.62, Issue.8, pp178-184, August. 2024*.
- Jongyeon Park, Jonghun Han, and Saewoong Bahk. "Adaptive Multilink Channel Access under Cross-link Interference in Next-generation WLANs". *IEEE Internet of Things Journal, vol.11, Issue.14, pp 24685-24697, July. 2024*.
- Hongchan Kim, Geonhee Lee, Juhun Shin, Jeongyeup Paek, and Saewoong Bahk. "Slot-size Adaptation and Utility-based Packet Aggregation for IEEE 802.15.4e Time-Slotted Communication Networks". *IEEE Internet of Things Journal, vol.11, Issue.9 , pp16382-16397 , May. 2024*.
- Wonbin Park, Sungbo Eo, Changhee Joo, and Saewoong Bahk. "B-hop: Time-domain Adjustment of BLE Frequency Hopping Against Wi-Fi Beacon Interference". *IEEE Internet of Things Journal, vol.11, Issue.7 , pp12853-12863 , April. 2024*.
- Sihyun Choi, Siyoung Choi, Goodsol Lee, Sung-Guk Yoon, and Saewoong Bahk. "Deep Reinforcement Learning for Scalable Dynamic Bandwidth Allocation in RAN Slicing with Highly Mobile Users". *IEEE Transactions on Vehicular Technology vol.73, Issue.1, pp576-590 , Jan. 2024*.
- Juhun Shin, Sunkee Baik, and Saewoong Bahk. "Performance Evaluation of OpenAirInterface-based 5G Standalone Testbed". *ICTC 2024, Jeju Island, Korea, Oct. 16-18, 2024*.
- Sihyun Choi, Sungbo Eo, and Saewoong Bahk. "Beam Alignment Methods for 5G mmWave UDNs and their Applicability in Indoor Environments". *ICTC 2024, Jeju Island, Korea, Oct. 16-18, 2024*.
- Sungbo Eo, and Saewoong Bahk. "T-DMB Receiver Implementation based on Open-source Software Suite". *ICTC 2024, Jeju Island, Korea, Oct. 16-18, 2024*.
- Hongchan Kim, Geonhee Lee, Juhun Shin, Jeongyeup Paek, and Saewoong Bahk. "Quick6TiSCH: Accelerating Formation of 6TiSCH Networks with TSCH and RPL". *IEEE MASS 2024 (Invited Paper), Seoul, South Korea , Sep 23 - 25, 2024*.
- Geonhee Lee, Eunjeong Park, Mingyu Park, Jeongyeup Paek, and Saewoong Bahk. "BIC-LoRa: Bits in Chirp Shapes to Boost Throughput in LoRa". *ACM IPSN 2024, Hong Kong, China, May. 13-16, 2024*.
- 이진명, 박세웅. "비면허 mmWave 대역 공존 네트워크에서 NR-U 시스템과 WiGig 시스템의 형평성 분석". *한국통신학회 추계종합학술발표회 2024, Nov. 20-22, 2024*.
- 박준하, 박세웅. "TCP Cubic Congestion Control의 LTE와 5G 환경에서의 성능 분석 및 비교". *한국통신학회 추계종합학술발표회 2024, Nov. 20-22, 2024*.
- 정용훈, 박세웅. "A Study on Direct Current Power Line Communication (DC-PLC) with Applications in Automotive, Maritime, and Aviation". *한국통신학회 추계종합학술발표회 2024, Nov. 20-22, 2024*.
- 박지민, 박세웅. "UWB 기반 Concurrent Ranging 기법 분석". *한국통신학회 하계종합학술발표회 2024, Jun. 19-22, 2024*.
- 최동락, 박세웅. "전력선 통신 기술의 연구 동향과 앞으로의 방향성에 대한 고찰". *한국통신학회 하계종합학술발표회 2024, Jun. 19-22, 2024*.
- 허수빈, 박세웅. "Resource Sharing in Network Slicing via Linear Double Auction". *한국통신학회 하계종합학술발표회 2024, Jun. 19–22, 2024*.
- 김덕진, 박세웅. "무인 항공기의 실내 로컬리제이션 방법에 대한 다양한 연구와 그 한계에 대한 서베이". *한국통신학회 하계종합학술발표회 2024, Jun. 19-22, 2024*.
- 김영석, 황선욱, 박세웅. "다중 에이전트 인지를 위한 오토인코더 기반 특징 데이터 압축기법 연구". *한국통신학회 하계종합학술발표회 2024, Jun. 19-22, 2024*.
- 류도균, 박세웅. "외부 환경에 따른 UWB 센서 TWR 성능 분석". *제 34회 통신정보 합동학술대회 2024, Apr.24-Apr.26, 2024*.
- 유용재, 박세웅. "기지국의 위치 정보를 활용한 연구와 그 한계에 대한 Survey". *제 34회 통신정보 합동학술대회 2024, Apr.24-Apr.26, 2024*.
- 박지민, 박종연, 박세웅. "UWB 동시 전송 시스템의 성능 분석". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 최동락, 유용재, 박세웅. "UAV를 활용한 음영지역 주변 상공 통신 성능 실측 및 분석에 관한 연구". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 이건희, 박세웅. "LoRa non-linear chirp 의 형태에 따른 성능 분석". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 박준하, 박세웅. "5G Multi-RAT 구조에서의 TCP Cubic의 Congestion Control 기법 분석 및 연구". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 어성보, 양진모, 박세웅. "LoRa 기반 다중홉 네트워크 성능 측정". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 윤지석, 박세웅. "비전 모델에 대한 테스트 시기 도메인 적응 기술 동향". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 이진명, 박세웅. "비면허 mmWave 대역에서 공존 네트워크의 단말 밀도에 따른 NR-U 시스템의 성능 분석". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.
- 이굳솔, 박세웅. "5G를 사용하는 모바일 실시간 통신 응용의 에너지 소모 분석". *한국통신학회 동계종합학술발표회 2024, Jan.31-Feb.02, 2024*.

**2023**

- Kanghyun Lee, Juhun Shin, Jongyeon Park, Youngwook Son, and Saewoong Bahk. "Recovering CSI and Data in Dense Network Environments Using IEEE 802.11ax Midamble". *IEEE Access, vol.11, pp. 65858- 68871, June.2023*.
- Seungwoo Baek, and Saewoong Bahk. "A Study on the Scalability and Feasibility of the Space-air Integrated Network". *ICTC 2023, Jeju Island, Korea, Oct. 11-13, 2023*.
- Sunwook Hwang, Youngseok Kim, Seongwon Kim, Saewoong Bahk, and Hyung-Sin Kim. "UpCycling: Semi-supervised 3D Object Detection without Sharing Raw-level Unlabeled Scenes". *in Proc. IEEE/CVF ICCV 2023, Paris, France, Oct. 2-6, 2023*.
- Juhun Shin, Hongchan Kim, Jeongyeup Paek, Saewoong Bahk. "ECA: Exclusive Cell Allocation for Autonomous Scheduling in Time-Slotted Channel Hopping". *IEEE MASS 2023, Toronto, Canada, September 25-27, 2023*.
- Dokyun Ryoo, Yongjae Yoo, Jeongyeup Paek, and Saewoong Bahk. "SPADE: Secure Periodic Advertising using Coded Time-Channel Rendezvous for BLE Audio". *IEEE DCOSS-IoT 2023, Coral Bay, Pafos, Cyprus, June 19-21, 2023*.
- 김덕진, 박세웅. "미래 항공 모빌리티 및 셀룰러 상공 통신을 위한 저궤도 위성통신 연구의 필요성". *한국통신학회 하계종합학술발표회 2023, Jun. 21-24, 2023*.
- 허수빈, 박세웅. "클라우드 컴퓨팅 기반 비전처리 애플리케이션을 위한 공동 전송데이터 압축 및 무선 자원할당 기법에 관한 연구". *한국통신학회 하계종합학술발표회 2023, Jun. 21-24, 2023*.
- 양진모, 곽철영, 박세웅. "문자 감지 어플리케이션을 위한 카메라 센서 조절 연구". *한국통신학회 하계종합학술발표회 2023, Jun. 21-24, 2023*.
- 김영석, 황선욱, 박세웅. "자율주행차량 간 비전정보 공유 과정의 통신 오버헤드 분석". *한국통신학회 하계종합학술발표회 2023, Jun. 21-24, 2023*.
- 유용재, 박세웅. "GPS Enhancement for Pedestrian Using UAV (Unmanned Aerial Vehicle)". *제 33회 통신정보 합동학술대회 2023, Apr. 26-28, 2023*.
- 박정준, 박지민, 박세웅. "UWB Two-Way Ranging 기반의 Human Activity Recognition 을 위한 Feature 추출". *제 33회 통신정보 합동학술대회 2023, Apr. 26-28, 2023*.
- 주우성, 신주훈, 박세웅. "High mobility 에 대한 전통적 셀룰러 시스템의 문제와 해결방안". *제 33회 통신정보 합동학술대회 2023, Apr. 26-28, 2023*.
- 이진명, 박종연, 박세웅. "비면허 mmWave 대역에서 공존 네트워크에 대한 Listen-Before-Receive의 지연시간 분석". *한국통신학회 동계종합학술발표회 2023, Feb. 8-10, 2023*.
- 박준하, 이강현, 박세웅. "O-RAN을 활용한 5G 통신 시스템에서의 성능 향상 기법 연구". *한국통신학회 동계종합학술발표회 2023, Feb. 8-10, 2023*.
- 어성보, 양진모, 박세웅. "야생동물 위치추적 단말기를 위한 에너지 효율적 LoRa MAC 프로토콜 설계". *한국통신학회 동계종합학술발표회 2023, Feb. 8-10, 2023*.
- 류도균, 김정준, 박세웅. "UAV를 이용한 지상-공중 간 통신의 특징 및 활용 방안". *한국통신학회 동계종합학술발표회 2023, Feb. 8-10, 2023*.
- 신주훈, 유용재, 박세웅. "트래픽 과부하 환경에서 Slotframe 크기에 따른 링크 기반 TSCH 스케쥴러의 성능 분석". *한국통신학회 동계종합학술발표회 2023, Feb. 8-10, 2023*.

**2022**

- Jihwan Suh, Yongjae Yoo, Jeongyeup Paek, and Saewoong Bahk. "Deep-Fading Hole Avoidance for Secure Region Detection using Channel State Information". *Journal of Communications and Networks, vol.24, Issue.6, pp. 645 - 654, Dec.2022*.
- Myungsup Lee, Taeseop Lee, Hyung-Sin Kim, and Saewoong Bahk. "Wi-BLE: On Cooperative Operation of Wi-Fi and Bluetooth Low Energy under IPv6". *Journal of Communications and Networks, vol.24, Issue.3, pp. 489 - 502, Aug.2022*.
- Kitaek Lee, Seungwoo Baek, and Saewoong Bahk. "Mobility Management of Multi-hop Mobile Integrated Access and Backhaul Network". *Journal of Communications and Networks, vol.24, Issue.3, pp. 475 - 488, Aug.2022*.
- Jeongjun Park, Hongchan Kim, Hyung-Sin Kim, and Saewoong Bahk. "DualBlock: Adaptive Intra-Slot CSMA/CA for TSCH". *IEEE Access, vol.10, pp. 68819 - 68833, June.2022*.
- Jungjun Kim and Saewoong Bahk. "Blockage-Aware Flow Control in E-UTRA-NR Dual Connectivity for QoS Enhancements". *IEEE Access, vol.10, pp. 68834 - 68845, June.2022*.
- Hongchan Kim, Hyung-sin Kim, and Saewoong Bahk. "MobiRPL: Adaptive, Robust, and RSSI-based Mobile Routing in Low Power and Lossy Networks". *Journal of Communications and Networks, vol.24, Issue.3, pp. 365 - 383, Feb.2022*.
- Sunghoon Jung, and Saewoong Bahk. "Online Control of Traffic Split and Distributed Cell Group State Decisions for Multi-connectivity in 5G and Beyond". *IEEE Transactions on Vehicular Technology, vol.71, no.3, pp. 2843 - 2858, Mar.2022*.
- Felipe Gómez-Cuba, Tommaso Zugno, Junseok Kim, Michele Polese, Saewoong Bahk, and Michele Zorzi. "Hybrid Beamforming in 5G mmWave Networks: a Full-stack Perspective". *IEEE Transactions on Wireless Communications, vol. 21, no.2, pp. 1288 - 1303, Feb.2022*.
- Jiseok Youn, Jaehun Song, Hyung-Sin Kim, and Saewoong Bahk. "Bitwidth-Adaptive Quantization-Aware Neural Network Training: A Meta-Learning Approach". *ECCV 2022, Tel-Aviv, Israel, Oct. 23-27, 2022*.
- Geonhee Lee, Hongchan Kim, and Saewoong Bahk. "Performance Evaluation of TSCH scheduler under Network Size Variations". *ICTC 2022, Jeju Island, Korea, Oct. 19-21, 2022*.
- Youngseok Kim, Sunwook Hwang, and Saewoong Bahk. "A Study on the Feature-level Perception Sharing of Autonomous Vehicles". *IEEE VTS APWCS 2022, Seoul, Korea, Aug. 24-26, 2022*.
- 이굳솔, 박세웅. "UAV 기지국 기반 6G 밀집 네트워크를 위한 도심 트래픽 분석". *한국통신학회 추계종합학술발표회 2022, Nov. 16-18, 2022*.
- 김덕진, 김정준, 이진명, 박세웅. "5G와 LTE 상황에서 여러 어플리케이션의 파워 소모 및 스루풋에 대한 실측 및 고찰". *한국통신학회 하계종합학술발표회 2022, Jun. 22-24, 2022*.
- 유용재, 박세웅. "드론 네트워크 실측을 위한 Cellular Network Parameter 분석". *한국통신학회 하계종합학술발표회 2022, Jun. 22-24, 2022*.
- 윤지석, 이강현, 박세웅. "적응적 인공지능 활용 통신 시스템을 위한 전이 학습 및 메타학습 기술의 다방면으로의 적용 연구 동향". *한국통신학회 하계종합학술발표회 2022, Jun. 22-24, 2022*.
- 양진모, 박세웅. "모바일 음성 언어 처리에서의 연산 오프로딩의 기작 및 효율성 분석". *한국통신학회 하계종합학술발표회 2022, Jun. 22-24, 2022*.
- 최시현, 박세웅. "네트워크 트래픽 분산을 위한 동적 가격 결정 및 심층 강화학습". *제 32회 통신정보 합동학술대회 2022, Apr. 27-29, 2022*.
- 유용재, 박세웅. "미래 항공 모밀리티를 위한 셀룰러 상공망 연구동향 및 실측연구의 필요성". *제 32회 통신정보 합동학술대회 2022, Apr. 27-29, 2022*.
- 김정준, 박세웅. "이동성을 가진 방해물이 존재하는 Dual Connectivity 환경에서 Flow Control의 중요성". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 이건희, 김홍찬, 박세웅. "트래픽 부하에 따른 독점적 자원 할당 방식의 TSCH 스케줄러의 성능 분석". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 박준하, 박세웅. "5G의 Latency 측정 및 원인 분석과 Dual Connectivity Scheduling 측면에서의 해법 연구". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 어성보, 박세웅. "상용 트랜시버에서 LoRa 확산계수의 준직교성 효과 분석". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 윤예린, 박종연, 박세웅. "Study of Multi-Link Device with Power Save Mode in IEEE 802.11be". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 이진명, 이굳솔, 박세웅. "비면허 mmWave 대역에서 IEEE 802.11ad 단말의 위치에 따른 NR-U 시스템의 성능 분석". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.
- 박정준, 박세웅. "TSCH 네트워크에서 발생하는 충돌문제 원인 분석 및 검증". *한국통신학회 동계종합학술발표회 2022, Feb. 9-11, 2022*.

**2021**

- Sunghoon Jung, Saewoong Bahk. "Real-time dual-link transmission control for minimizing power and link switching cost". *Computer Networks, vol.200, Dec. 2021*.
- Siyoung Choi, Jin-Ghoo Choi, and Saewoong Bahk. "Association Control for User Centric Millimeter Wave Communication Systems". *IEEE Transactions on Vehicular Technology, vol.70, no.11, pp. 12001 - 12012, Nov.2021*.
- Jihoon Kim, Jaehong Yi, and Saewoong Bahk. "R-SplitC: Collision Minimization for Cellular Communication in Unlicensed Spectrum". *Journal of Communications and Networks, vol.23, Issue 4, pp. 260-270, Aug. 2021*.
- Hyung-Sin Kim, Jeongyeup Paek, and Saewoong Bahk. "RPLIE: RPL for Indoor Environments under Midterm Link Fluctuations". *Journal of Communications and Networks, vol.23, Issue 3, pp. 201-211, Apr. 2021*.
- Yongjae Yoo, Jihwan Suh, Jeongyeup Paek, and Saewoong Bahk. "Secure Region Detection using Wi-Fi CSI and One-Class Classification". *IEEE Access 2021, vol.9, pp.65906-65913, Apr. 2021*.
- Junseok Kim, Goodsol Lee, Seongwon Kim, Tarik Taleb, Sunghyun Choi, and Saewoong Bahk. "Two-Step Random Access for 5G System: Latest Trends and Challenges". *IEEE Network, vol. 35, Issue 1, pp. 273-279, Mar-Apr. 2021*.
- Byungjun Kang, Jinmo Yang, Jeongyeup Paek, and Saewoong Bahk. "ATOMIC: Adaptive Transmission Power and Message Interval Control for C-V2X Mode 4". *IEEE Access, vol.9 pp. 12309 - 12321, Jan. 2021*.
- Jaehong Yi, Junseok Kim, Kitaek Lee, and Saewoong Bahk. "Performance Analysis of AMC for LTE-LAA under Rayleigh Fading Channel". *ICTC 2021, Jeju Island, Korea, Oct. 20-22, 2021*.
- Myungsup Lee and Saewoong Bahk. "Soft Checksum Method for Error-tolerant Multi-hop Transmission in Wireless Sensor Networks". *ICTC 2021, Jeju Island, Korea, Oct. 20-22, 2021*.
- Kanghyun Lee and Saewoong Bahk. "Performance Evaluation of IEEE 802.11ax Midamble and Impact of Interference". *ICTC 2021, Jeju Island, Korea, Oct. 20-22, 2021*.
- Felipe Gomez-Cuba, Tommaso Zugno, Junseok Kim, Michele Polese, Saewoong Bahk, and Michele Zorzi. "Full-stack Hybrid Beamforming in mmWave 5G Networks". *MedcomNet 2021, June 2021*.
- Eunjeong Park, Hyung-Sin Kim, and Saewoong Bahk. "BLEX: Flexible Multi-Connection Scheduling for Bluetooth Low Energy". *ACM IPSN 2021, Nashville, Tennessee, USA, May 18-21, 2021*.
- Wonbin Park, Dokyun Ryoo, Changhee Joo, and Saewoong Bahk. "BLESS: BLE-aided Swift Wi-Fi Scanning in Multi-protocol IoT Networks". *IEEE INFOCOM 2021, Virtual Conference, May. 10-13, 2021*.
- Junyoung Choi, Jaewon Hur, and Saewoong Bahk. "Push yoUr Password: Secure and Fast WiFi Connection for IoT Devices". *IEEE WCNC 2021, Nanjing, China, Mar. 29 - Apr. 1, 2021*.
- Jin Mo Yang, Hoyoung Yoon, Sunwook Hwang, and Saewoong Bahk. "PRESS: Predictive Assessment of Resource Usage for C-V2V Mode 4". *IEEE WCNC 2021, Nanjing, China, Mar. 29 - Apr. 1, 2021*.
- Hyunjoong Lee, Hyung-Sin Kim, and Saewoong Bahk. "LSR: Link-aware Spatial Reuse in IEEE 802.11ax WLANs". *IEEE WCNC 2021, Nanjing, China, Mar. 29 - Apr. 1, 2021*.
- Changmok Yang, Jinmyeong Lee, and Saewoong Bahk. "Target Wake Time Scheduling Strategies for Uplink Transmissions in IEEE 802.11ax Networks". *IEEE WCNC 2021, Nanjing, China, Mar. 29 - Apr. 1, 2021*.
- 류도균, 박세웅. "BLE Periodic Advertising 동작 및 향후 이용 분야". *한국통신학회 추계종합학술발표회 2021, Nov. 18, 2021*.
- 김영석, 황선욱, 박세웅. "자율주행차량을 위한 Cooperative Perception 기술의 연구 동향". *한국통신학회 추계종합학술발표회 2021, Nov. 18, 2021*.
- 김홍찬, 박세웅. "링크 기반 독점적 자원 할당 방식의 TSCH 스케쥴러의 성능 분석". *한국군사과학기술학회 종합학술대회 2021, Nov. 12, 2021*.
- 박은정, 박세웅. "저전력 블루투스의 다중 연결 지원에 대한 연구". *2021 한국군사과학기술학회 종합학술대회, Nov. 12, 2021*.
- 이굳솔, 이경한, 박세웅. "드론 기지국 충전을 위한 버스 충전소 경로에 따른 트래픽 분석". *한국통신학회 하계종합학술발표회 2021, Jun. 16-18, 2021*.
- 곽철영, 박세웅. "물체 감지 모델을 활용한 화면 속 글자 감지 기법". *한국통신학회 하계종합학술발표회 2021, Jun. 16-18, 2021*.
- 최시현, 박세웅. "심층 강화학습을 활용한 고이동성 상황의 5세대 네트워크 슬라이싱에서 동적 대역폭 할당에 관한 연구". *한국통신학회 하계종합학술발표회 2021, Jun. 16-18, 2021*.
- 이기택, 박세웅. "MmWave 사용자 중심 초고밀도 네트워크 QoS 향상을 위한 DNN 기반 단말 위치 예측 및 BS 연결 기법". *한국통신학회 제 31회 통신정보 합동학술대회 2021, Apr. 28-30, 2021*.
- 윤지석, 박세웅. "A Study on the Quantization-Aware Training Techniques for Better Efficiency". *한국통신학회 제 31회 통신정보 합동학술대회 2021, Apr. 28-30, 2021*.
- 윤예린, 박종연, 박세웅. "Monopolization of Unnecessary Resources using Distributed Antenna Systems in an Uplink Traffic Scenario". *한국통신학회 동계종합학술발표회 2021, Feb. 3-5, 2021*.
- 김영석, 황선욱, 박세웅. "Federated Learning 의 통신효율 향상을 위한 기술의 연구 동향". *한국통신학회 동계종합학술발표회 2021, Feb. 3-5, 2021*.

## 특허

출원일이나 등록일 중 하나라도 2021년 10월 22일–2026년 10월 22일에 드는 게시 항목 27건이다. 국제 특허 3건과 국내 특허 24건이며, 제목·발명자·번호·날짜는 누리집 표기다.[^patents]

- 2023-01-19 · Method for bitwidth-adaptive quantization-aware training based on meta-learning and apparatus for performing the method (발명자 Saewoong Bahk, Hyung-Sin Kim, Jiseok Youn, and Jaehun Song; 번호 PCT/KR2023/000916 (Jan. 19, 2023); 국가 International)
- 2022-04-20 · Semi-Supervised Learning Method for Object Detection in Autonomous Vehicle and Server for Performing Semi-Supervised Learning for Object Detection in Autonomous Vehicle (발명자 Sunwook Hwang, Youngseok Kim, Hyungsin Kim and Saewoong Bahk; 번호 USA: 17/659,878 (Apr. 20, 2022), Issued: US Patent No. 11,495,012 B1 (Nov. 8, 2022); 국가 International)
- 2022-11-03 · 무선 통신 시스템에서 빔을 선택하기 위한 방법 및 장치 (발명자 Jaehong Yi, Sihyun Choi, Saewoong Bahk, Deokhui Lee; 번호 PCT/KR2022/017097 (Nov. 3, 2022); 국가 International)
- 2026-04-24 · 단일 기준 태그 기반 반복적 궤적 보정을 이용한 무인항공기 유도 장치 및 방법 (발명자 박세웅, 류도균; 번호 출원번호 10-2026-0074645, 2026년 04월 24일; 국가 Domestic)
- 2025-02-04 · 통신 시스템에서 TCP를 이용한 연결을 수행하는 방법 및 장치 (발명자 박세웅, 신주훈, 조선우; 번호 출원번호 P20250014026, 2025년 02월 04일; 국가 Domestic)
- 2025-01-03 · 무선 통신 시스템에서 전송 제어 프로토콜(TCP) 혼잡 제어 방법 및 장치 (발명자 박세웅, 신주훈, 조선우, 김동명; 번호 출원번호 P20250000802, 2025년 01월 03일; 국가 Domestic)
- 2025-04-30 · 초광대역 기반 멀티홉 무선 네트워크에서의 동시 전송 방식 데이터 수집 방법 (발명자 박세웅, 박지민, 이건희; 번호 출원번호 10-2025-0057659, 2025년 04월 30일; 국가 Domestic)
- 2025-04-30 · LoRa 통신 장치와 해당 통신 장치가 사용하는 변조 및 복조 방법 (발명자 박세웅, 박은정, 이건희; 번호 출원번호 10-2025-0057644 , 2025년 04월 30일; 국가 Domestic)
- 2025-04-11 · 셀타워 위치 추정 무인 비행장치 (발명자 박세웅, 서지환, 유용재, 최동락; 번호 출원번호 10-2025-0047306 , 2025년 04월 11일; 국가 Domestic)
- 2025-04-11 · 자동 회전 편파 정렬 고속 통신장치 (발명자 박세웅, 유용재, 최동락, 최승민; 번호 출원번호 10-2025-0047305 , 2025년 04월 11일; 국가 Domestic)
- 2024-12-30 · 복셀 기반 특징 데이터로부터 3D 포인트 클라우드 데이터를 복원하는 방법 (발명자 박세웅, 김형신, 김영석, 황선욱; 번호 출원번호 10-2024-0201056, 2024년 12월 30일; 국가 Domestic)
- 2024-12-24 · 셀룰러 음영지역에서 고품질 데이터 전송을 위한 드론 릴레이 배치 장치 (발명자 박세웅, 백정엽, 유용재, 최동락, 최유빈; 번호 출원번호 10-2024-0195602 , 2024년 12월 24일; 국가 Domestic)
- 2024-12-24 · 고도 선택을 통한 드론의 고품질 셀룰러 연결 유지 장치 (발명자 박세웅, 백정엽, 서지환, 유용재, 최동락; 번호 출원번호 10-2024-0195601 , 2024년 12월 24일; 국가 Domestic)
- 2024-08-06 · 인공 지능 모델을 위한 분리 연합 학습 및 추론 방법 및 장치 (발명자 송수은, 박세웅, 윤지석, 김영석; 번호 출원번호 10-2024-0104720, 2024년 08월 06일; 국가 Domestic)
- 2023-08-07 · 도메인 적응, 메타 학습 및 모델 양자화 기반 적응형 고효율 분리 연합 학습 및 추론 방법과 이러한 방법을 수행하는 장치 (발명자 송수은, 박세웅, 윤지석, 김영석; 번호 출원번호 10-2023-0103145, 2023년 08월 07일; 국가 Domestic)
- 2023-03-21 · 모바일 기기의 카메라 노출 제어 방법 및 카메라 노출 제어 시스템 (발명자 박세웅, 곽철영, 양진모, 손성욱, 강병구, 이경한, 김형신; 번호 출원번호10-2023-0036945 , 2023년 03월 21일; 국가 Domestic)
- 2022-12-26 · 메타 학습 기반 적응형 비트폭 양자화 인식 학습 방법 (발명자 박세웅, 김형신, 윤지석, 송재헌; 번호 출원번호 10-2022-0184425, 2022년 12월 26일; 국가 Domestic)
- 2022-12-23 · 자율주행차량 내 물체 인식 모델 개선을 위한 피처 데이터 기반 준지도 방식 학습 방법 및 이러한 방법을 수행하는 장치 (발명자 황선욱, 박세웅, 김형신, 김영석; 번호 출원번호 10-2022-0183113, 2022년 12월 23일, 등록번호 10-2987945, 2026년 7월 2일; 국가 Domestic)
- 2022-10-26 · 무선 통신 시스템에서 빔을 선택하기 위한 방법 및 장치 (발명자 이재홍, 최시현, 박세웅, 이덕희; 번호 출원번호 10-2022-0139228, 2022년 10월 26일; 국가 Domestic)
- 2021-11-05 · BLE에서 적응적인 연결 스케줄링 방법 및 이러한 방법을 수 행하는 장치 (발명자 박은정, 박세웅; 번호 출원번호 10-2021-0151286, 2021년 11월 5일, 등록번호 10-2021-0151286, 2022년 4월 1일; 국가 Domestic)
- 2024-08-20 · 차량 간 통신에서 전송 자원 예측을 기반으로 한 전송 자원 할당 방법 및 이러한 방법을 수행하는 장치 (발명자 박세웅, 양진모, 윤호영, 황선욱; 번호 등록번호 10-2698048-00-00, 2024년 8월 20일; 국가 Domestic)
- 2022-02-18 · 강화 학습을 사용한 UAV BS 기반의 통신 방법 및 이러한 방법을 수행하는 장치 (발명자 박세웅, 이경한, 이굳솔, 이주헌, 이지현; 번호 출원번호 10-2022-0021201, 2022년 2월 18일; 국가 Domestic)
- 2021-11-19 · 자율 주행 차량에서 객체 검출을 위한 준지도 학습 방법 및 이러한 방법을 수행하는 장치 (발명자 황선욱, 김영석, 김형신, 박세웅; 번호 출원번호 10-2021-0160432, 2021년 11월 19일, 등록번호 10-2394024, 2022년 4월 29일; 국가 Domestic)
- 2023-10-20 · 분산 안테나 시스템을 가지는 AP의 동작 방법 및 이러한 방법을 수행하는 장치 (발명자 박세웅, 박종연, 이강현, 윤예린; 번호 출원번호 10-2020-0149220, 2020년 11월 10일, 등록번호 10-2594039, 2023년 10월 20일; 국가 Domestic)
- 2023-11-05 · 미드앰블을 이용한 채널 판단 방법 및 이러한 방법을 수행하는 장치 (발명자 박세웅, 이강현, 박종연, 이진명; 번호 출원번호 10-2020-0149219, 2020년 11월 10일, 등록번호 10-2600192, 2023년 11월 05일; 국가 Domestic)
- 2022-11-14 · 무선 네트워크에서 시분할 다중 접속 자원 스케줄링을 위한 방법 및 장치 (발명자 박세웅, 정승범, 김형신, 백정엽; 번호 출원번호 10-2020-0117801, 2020년 09월 14일, 등록번호 10-2467945-00-00, 2022년 11월 14일; 국가 Domestic)
- 2021-11-01 · 차량 간 통신에서 혼잡 제어를 위한 주기적 메시지 전송 방법 및 장치 (발명자 박세웅, 강병준; 번호 출원번호 10-2019-0176153, 2019년 12월 27일, 등록번호 10-2322347, 2021년 11월 1일; 국가 Domestic)

## 수상

기간 안에 게시된 연구 성과 수상이다. 두 Best paper runner-up 항목의 날짜는 수상일이 따로 제시되지 않아 논문 목록의 학회 기간으로 표시했다.[^notice][^conferences]

- 2025-02-13 · Juhun Shin의 Samsung Humantech Paper Award 은상 수상
- 2025-06-09–11 (학회 기간) · Cupid: Fast and Reliable Convergecast-over-UWB Protocol for Dense Internet of Things · Best paper runner-up
- 2023-06-19–21 (학회 기간) · SPADE: Secure Periodic Advertising using Coded Time-Channel Rendezvous for BLE Audio · Best paper runner-up

## 소식

2021년 10월 25일–2026년 9월 7일의 논문 게재 승인·학회 채택 소식 48건이다. 학술지는 게재 승인, 학회는 채택으로 구분했다. 동일 날짜에 같은 학회 이름으로 게시된 서로 다른 항목은 각각 실었다.[^notice][^home]

- 2026-09-07 · Dokyun의 논문이 IEEE Internet of Things Journal에 게재 승인
- 2026-09-01 · Geonhee의 논문이 IEEE International Conference on Embedded Artificial Intelligence and Sensing System (SenSys'27)에 채택
- 2026-07-27 · Yubin의 논문이 IEEE Global Communications Conference 2026에 채택
- 2026-07-27 · Goodsol의 논문이 USENIX Symposium on Network Systems Design and Implementation (NSDI'27)에 채택
- 2026-07-15 · Jongyeon의 논문이 IEEE Transactions on Networking에 게재 승인
- 2026-06-01 · Yonghoon의 논문이 IEEE Communications Letters에 게재 승인
- 2026-06-01 · Yongjae의 논문이 IEEE Transactions at Vehicular Technology에 게재 승인
- 2026-03-26 · Jewoon의 논문이 IEEE Vehicular Technology Conference에 채택
- 2026-03-20 · Deokjin의 논문이 IEEE ICDCS에 채택
- 2026-03-20 · Sihyun의 논문이 IEEE WiOpt에 채택
- 2026-03-20 · Dongrak의 논문이 IEEE Vehicular Technology Conference에 채택
- 2026-02-07 · Jeongjun의 논문이 IEEE Access에 게재 승인
- 2025-12-12 · 연구실 논문이 IEEE Internet of Things Journal에 게재 승인
- 2025-12-08 · 연구실 논문이 INFOCOM 2026에 채택
- 2025-12-08 · 연구실 논문이 INFOCOM 2026에 채택
- 2025-10-15 · 연구실 논문이 IEEE Transactions on Network and Service Management에 게재 승인
- 2025-08-12 · 연구실 논문이 IEEE Internet of Things Journal에 게재 승인
- 2025-08-08 · 연구실 논문이 IEEE Vehicular Technology Conference에 채택
- 2025-07-22 · 연구실 논문이 IEEE Transactions on Vehicular Technology에 게재 승인
- 2025-07-14 · 연구실 논문이 USENIX Symposium on Network Systems Design and Implementation (NSDI '26)에 채택
- 2025-05-26 · 연구실 논문이 IEEE Journal on Selected Areas in Communications에 게재 승인
- 2025-04-04 · 연구실 논문이 IEEE Access에 게재 승인
- 2025-04-01 · 연구실 논문이 DCOSS에 채택
- 2025-03-10 · 연구실 논문이 ICLR에 채택
- 2024-12-22 · 연구실 논문이 WCNC에 채택
- 2024-12-16 · 연구실 논문이 TVT에 게재 승인
- 2024-12-06 · 연구실 논문이 INFOCOM 2025에 채택
- 2024-12-06 · 연구실 논문이 INFOCOM 2025에 채택
- 2024-07-12 · 연구실 논문이 MASS 2024에 채택
- 2024-02-08 · 연구실 논문이 IoTJ에 게재 승인
- 2024-01-20 · 연구실 논문이 IPSN에 채택
- 2024-01-07 · 연구실 논문이 IoTJ에 게재 승인
- 2023-11-30 · 연구실 논문이 Journal on Internet of Things에 게재 승인
- 2023-08-08 · 연구실 논문이 Transactions on Vehicular Networks에 게재 승인
- 2023-07-18 · 연구실 논문이 ICCV 2023에 채택
- 2023-06-27 · 연구실 논문이 ACCESS에 게재 승인
- 2023-06-27 · 연구실 논문이 MASS 2023에 채택
- 2023-04-14 · 연구실 논문이 DCOSS에 채택
- 2022-12-04 · 연구실 논문이 Journal of Communications and Networks에 게재 승인
- 2022-07-04 · 연구실 논문이 ECCV 2022에 채택
- 2022-06-27 · 연구실 논문이 Journal of Communications and Networks에 게재 승인
- 2022-06-27 · 연구실 논문이 Journal of Communications and Networks에 게재 승인
- 2022-06-27 · 연구실 논문이 IEEE Access에 게재 승인
- 2022-06-27 · 연구실 논문이 IEEE Access에 게재 승인
- 2022-01-19 · 연구실 논문이 Journal of Communications and Networks에 게재 승인
- 2021-11-29 · 연구실 논문이 IEEE Transactions on Vehicular Networks에 게재 승인
- 2021-10-25 · 연구실 논문이 Computer Networks에 게재 승인
- 2021-10-25 · 연구실 논문이 IEEE Transactions on Vehicular Technology에 게재 승인

## 연락과 위치

- 교수 연구실: 132동 208호, 전화 02-880-8414[^contact]
- 연구실: 132동 303호, 전화 02-880-8434[^contact]
- 연구실: 302동 510-1호, 전화 02-880-1813[^contact]
- 교수 이메일: sbahk@snu.ac.kr[^faculty]
- 문의 이메일: captain@netlab.snu.ac.kr[^contact]
[^home]: NETLAB, 「Home」, 연구 소개·Research Topic·Recent Notice. <https://sites.google.com/netlab.snu.ac.kr/netlabhome> (관측 2026-10-26).
[^prof]: 서울대학교 전기·정보공학부, 「박세웅」, 교수 표기·전문 분야. <https://ece.snu.ac.kr/research-faculty/faculty/full-time?md=view&profid=p017> (관측 2026-10-26).
[^people]: NETLAB, 「People」, 현재 구성원과 Alumni. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/people> (관측 2026-10-26).
[^faculty]: NETLAB, 「Saewoong Bahk」, 재직 기간·현재 직위·관심 분야·교수 이메일. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/people/faculty> (관측 2026-10-26).
[^notice]: NETLAB, 「Notice」, 날짜가 붙은 연구 성과 소식. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/notice> (관측 2026-10-26).
[^research]: NETLAB, 「Research」, 연구 주제 구분. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/research> (관측 2026-10-26).
[^journals]: NETLAB, 「International Journals」, 국제 학술지 목록. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/publication/international-journals> (관측 2026-10-26).
[^conferences]: NETLAB, 「International Conferences」, 국제 학회 목록과 수상 표기. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/publication/international-conferences> (관측 2026-10-26).
[^domestic-journals]: NETLAB, 「Domestic Journals」, 국내 학술지 목록. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/publication/domestic_journals> (관측 2026-10-26).
[^domestic-conferences]: NETLAB, 「Domestic Conferences」, 국내 학회 목록. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/publication/domestic-conferences> (관측 2026-10-26).
[^patents]: NETLAB, 「Patents」, 국제·국내 특허 목록. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/publication/patents> (관측 2026-10-26).
[^contact]: NETLAB, 「Contact」, 교수·연구실 위치와 연락처. <https://sites.google.com/netlab.snu.ac.kr/netlabhome/contact> (관측 2026-10-26).

[^p1]: W. Park, S. Eo, C. Joo, S. Bahk, IEEE Internet of Things Journal 11, 12853–12863 (2024). <https://doi.org/10.1109/JIOT.2023.3337252> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/376665364_B-hop_Time-Domain_Adjustment_of_BLE_Frequency_Hopping_Against_Wi-Fi_Beacon_Interference>
[^p2]: E. Park 외, S. Bahk, Journal of Communications and Networks 28, 223–232 (2026). <https://doi.org/10.23919/JCN.2025.000084> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/401233466_AURORA_Adaptive_spreading_factor_control_for_low-power_multihop_LoRa_network>
[^p3]: H. Kim, H.-S. Kim, S. Bahk, Journal of Communications and Networks 24, 365–383 (2022). <https://doi.org/10.23919/JCN.2022.000004> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/358825035_MobiRPL_Adaptive_robust_and_RSSI-based_mobile_routing_in_low_power_and_lossy_networks>
[^p4]: G. Lee 외, S. Bahk, 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26), 1721–1739 (2026). <https://www.usenix.org/conference/nsdi26/presentation/lee> 초록 기준(학회 논문집 페이지 게시 초록). 초록 원문 <https://www.usenix.org/conference/nsdi26/presentation/lee>
[^p5]: Y. Yoo, J. Suh, J. Paek, S. Bahk, IEEE Access 9, 65906–65913 (온라인 2021-04-28). <https://doi.org/10.1109/ACCESS.2021.3076176> 초록 기준(ResearchGate 등록 초록). 초록 원문 <https://www.researchgate.net/publication/351178927_Secure_Region_Detection_using_Wi-Fi_CSI_and_One-Class_Classification>
[^p6]: J. Youn, J. Song, H.-S. Kim, S. Bahk, ECCV 2022 (arXiv 사전 공개본) (온라인 2022-07-20). <https://arxiv.org/abs/2207.10188> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2207.10188>
[^p7]: S. Choi 외, S. Bahk, IEEE Transactions on Network and Service Management (2025). <https://doi.org/10.1109/tnsm.2025.3618117> 초록 기준(OpenAlex 등록 초록).
[^p8]: Y. Yoo 외, S. Bahk, IEEE Transactions on Vehicular Technology (2025). <https://doi.org/10.1109/tvt.2025.3594092> 초록 기준(OpenAlex 등록 초록).

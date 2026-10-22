# 항공우주통신 및 응용지능 연구실 (Aerospace Communications and Applied Intelligence Lab, ACAI)

**KAIST 항공우주공학과 · 최지환 교수**

- 분야: 위성통신(5G·6G 위성·지상 통합망, 위성 탑재 처리 시스템과 알고리즘), 무선통신(여러 무선 규격의 공존, 물리 계층 보안), 기계학습·딥러닝 응용(위성·항공 영상 분할, 여러 센서 자료 처리)
- 대분야: 전기전자·반도체·광학, 컴퓨팅·AI
- 태그: 무선·이동통신[^research][^p5][^p6], 컴퓨터 네트워크[^p1][^p2][^p3], 네트워크 보안·프라이버시[^research][^p4], 위성 원격탐사[^research][^p8], 컴퓨터 비전[^research][^p8]
- 홈페이지: <https://acai-kaist.github.io>
- 근거와 출처: [ACAI 근거 페이지](acai-sources.md)

> 통신 기술과 기계학습·딥러닝을 항공우주공학에 적용하는 연구실로, 5G·6G 위성통신망의 구조와 알고리즘을 설계하고 위성·항공 영상 자료를 분석한다.[^aelab]

## 무엇을 연구하나

연구실은 KAIST 항공우주공학과 최지환 부교수가 이끈다.[^aelab][^aefac] 학과의 연구실 소개는 연구실이 통신과 기계학습·딥러닝 기반 정보통신 기술을 항공우주공학에 적용하며, 5G·6G 위성통신망의 구조와 알고리즘 설계, 위성·항공 영상 자료 분석 같은 연구를 한다고 적고, 연구 분야를 위성·무선통신과 기계학습·딥러닝 응용으로 적는다.[^aelab] 같은 이름의 연구실은 반도체시스템공학과 연구실 명단에도 올라 있고, 그 명단도 연구 분야로 5G·6G 위성통신망 구조와 알고리즘 설계, 위성·항공 영상 자료 분석을 든다.[^sselab]

연구실 누리집의 연구 페이지는 연구를 세 갈래로 나눈다.[^research] 첫째는 위성통신이다. 위성망과 지상망을 하나로 묶는 5G·6G 위성·지상 통합망과, 위성 탑재 처리(on-board processing, 위성 안에서 신호와 데이터를 직접 처리하는 것) 시스템과 알고리즘을 다룬다. 둘째는 무선통신으로, 서로 다른 통신 규격의 무선 시스템이 함께 쓰일 수 있게 하는 공존 기술과 물리 계층 보안(무선 채널의 성질을 이용해 엿듣는 쪽이 정보를 얻지 못하게 하는 보안 기술)을 다룬다. 셋째는 기계학습·딥러닝 응용으로, 위성·항공 영상의 분할(영상 속 각 부분이 어떤 대상에 속하는지 나누는 일)과 여러 센서에서 나온 자료의 처리를 다룬다.[^research]

대표 논문으로 보면 연구는 다섯 갈래로 모인다. 첫째, 저궤도(지구에 가까운 낮은 궤도) 위성을 아주 많이 띄워 함께 운용하는 메가 군집 위성망에서, 위성과 지상 관문국을 잇는 연결을 바꾸는 시점과 위성망을 제어하는 소프트웨어 컨트롤러 배치를 최적화한다(대표 논문 1, 2).[^p1][^p2] 둘째, 위성에서 계산을 처리하는 위성 엣지 컴퓨팅과, 하나의 위성망을 용도별 가상망으로 나눠 쓰는 네트워크 슬라이싱을 설계한다(대표 논문 3).[^p3] 셋째, 다중 빔 위성망에서 암호와 물리 계층 보안을 함께 써서 엿듣기를 막는다(대표 논문 4).[^p4] 넷째, 높은 고도에 떠서 통신을 중계하는 고고도 플랫폼(HAPS)과 무인기로 이루는 공중 통신망의 성능을 분석하고 설계한다(대표 논문 5, 6).[^p5][^p6] 다섯째, 딥러닝으로 심우주 통신 신호를 잡아내고 항공 사진에서 건물을 찾아낸다(대표 논문 7, 8).[^p7][^p8]

연구실 누리집의 과제 페이지는 진행 중인 과제 8건을 적는다. 거대 위성망의 지능형 경로 설정, 6G 소프트웨어 정의 위성망, Q·V 대역(매우 높은 주파수 대역) 고처리량 통신망 알고리즘, 여러 임무를 맡는 저궤도 위성 군집의 우주 통신 교육센터, 도심항공교통(UAM)을 위한 초고신뢰 공중망 연구센터 같은 과제다.[^projects]

## 주요 연구 주제

### 1. 저궤도 위성 메가 군집 네트워크

여러 궤도 높이와 여러 지상 관문국이 있는 메가 군집에서 위성과 관문국을 잇는 연결을 언제 바꿀지 최적화하고, 빠르게 움직이는 위성들을 안정된 논리적 망으로 보이게 하는 가상화로 소프트웨어 정의 네트워킹 컨트롤러에 위성을 바로 배정한다.[^p1][^p2] 대표 논문 1, 2.

### 2. 위성 엣지 컴퓨팅과 네트워크 슬라이싱

사물인터넷 서비스를 위성에서 처리하는 위성 엣지 컴퓨팅의 구조를 분석하고, 지연·계산 전력·전송 전력 감쇠를 함께 고려해 위성의 작업 넘기기 비율과 고도, 슬라이스별 일정 규칙을 정한다.[^p3] 대표 논문 3.

### 3. 위성 통신 보안

엿듣는 쪽의 수에 따라 엿듣기 위험을 추정하고, 위성의 전력 배분·빔 일정·보안 알고리즘 선택을 함께 정해 암호와 물리 계층 보안을 통합한다.[^p4] 대표 논문 4.

### 4. 고고도 플랫폼·무인기 공중 네트워크

원 궤도를 따라 나는 고고도 플랫폼의 하향 통신 성능을 수식으로 분석하고, 테라헤르츠 백홀을 갖춘 여러 무인기의 무선 접속망을 3차원으로 설계한다.[^p5][^p6] 대표 논문 5, 6.

### 5. 인공지능을 쓰는 우주 통신과 항공 영상 분석

심우주 통신 신호의 처음 포착을 시간-주파수 영상에서 물체를 찾는 문제로 바꿔 딥러닝 검출기로 풀고, 항공 사진 속 건물의 모양과 경계를 정확히 나누는 딥러닝 모델을 만든다.[^p7][^p8] 대표 논문 7, 8.

## 대표 논문

랩 Publications 페이지의 2021–2026년 학술지 논문 가운데 최지환 교수가 마지막 저자이거나 랩 목록이 교수를 교신저자로 표시한 논문을 다섯 연구 갈래에 고르게 담도록 골랐다. "쉽게 말하면" 칸은 각 논문의 초록만을 근거로 썼다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자[^pubs] |
|---|---|---|---|---|
| 1 | 2026 | [Multi-Gateway Feeder Link Switching Optimization in Multi-Shell LEO Mega-Constellations](https://doi.org/10.1109/tcomm.2025.3648974) · IEEE Transactions on Communications | 저궤도(LEO) 위성을 아주 많이 띄운 메가 군집으로 이루는 비지상 네트워크(NTN, 위성처럼 하늘에 있는 장비로 이루는 통신망)에서, 위성과 지상 관문국(게이트웨이)을 잇는 피더 링크를 바꾸는 문제를 다뤘다. 저궤도 위성은 빠르게 움직여 피더 링크가 자주 끊기므로 믿을 만한 연결을 유지하는 일이 중요하다. 여러 궤도 껍질(shell)과 여러 관문국이 있는 환경에서, 가상 네트워크 임베딩(VNE, 물리적인 망 위에 필요한 가상망을 배치하는 방법)과 피더 링크 전환 전략을 묶은 두 단계 최적화 틀을 제안했다. 아래 단계는 링크 품질과 전환 횟수의 균형을 맞추려고 한 번 연결할 때 보내는 데이터 양을 최대로 하고, 위 단계는 관문국을 위한 전용 가상망을 짜서 위성과 지상 기반시설의 연결을 높인다. 스타링크 2세대(Starlink Gen II) 군집을 바탕으로 한 시뮬레이션에서 제안 방법은 실제 관문국 배치에서 위성을 100% 활성화했고, 비교 방법은 93%였다.[^p1] | 1저자 S. Kim, 마지막 저자 최지환(교신) |
| 2 | 2025 | [A Scalable Multi-Controller SDN Framework for LEO Mega-Constellation via Topology Virtualization](https://doi.org/10.1109/jiot.2025.3576912) · IEEE Internet of Things Journal | 저궤도 위성 메가 군집을 위해 전 세계 규모로 넓힐 수 있는 다중 컨트롤러 소프트웨어 정의 네트워킹(SDN, 망의 경로 제어를 소프트웨어 컨트롤러가 모아서 맡는 방식) 틀을 제안했다. 빠르게 바뀌는 망 구조와 거대한 규모를 다루려고, 움직이는 위성들을 안정된 논리적 망으로 보이게 하는 토폴로지 가상화와 동적 매핑 전략을 도입해 제어 계층이 끊임없는 구조 변화에 흔들리지 않게 했다. 컨트롤러끼리 자주 협력해야 하는 기존 방식과 달리, 위치에 따른 선형 할당 문제로 세우고 계산식으로 바로 구하는 해를 유도해 추가 협력 없이 위성을 컨트롤러에 바로 배정한다. 스타링크 2세대 군집으로 평가한 결과, 지구에 고정된 구역(셀)들 사이에 부하를 고르게 나누면서 계산 복잡도를 크게 줄였다.[^p2] | 1저자 I. Choi, 마지막 저자 최지환(랩 목록은 교신저자를 S. Kim으로 표기) |
| 3 | 2022 | [Satellite Edge Computing Architecture and Network Slice Scheduling for IoT Support](https://doi.org/10.1109/jiot.2021.3132171) · IEEE Internet of Things Journal | 5G·6G 통신에서 위성은 서비스 범위를 전 지구로 넓히고 3차원 이동성을 높일 수단으로 주목받는다. 사물인터넷(IoT) 서비스는 계산 부담이 비교적 작아, 전력이 제한된 위성에서 계산을 처리하는 위성 엣지 컴퓨팅(SatEC)에 알맞다. IoT를 지원하는 위성 엣지 컴퓨팅의 구조를 분석하고 네트워크 슬라이스(하나의 물리적인 망을 용도별 가상망으로 나눈 조각) 일정 짜기를 제안했다. 먼저 지연, 계산 전력, 전송 전력 감쇠를 함께 고려하는 다목적 최적화 문제를 세우고, 시간에 따라 바뀌는 위성 군집 구조와 여러 서비스 요구 조건에서 위성의 작업 넘기기(offloading) 비율과 고도를 시간 복잡도가 낮은 경험적 알고리즘으로 풀었다. 이어 슬라이스로 나눈 IoT 일정 문제를 세우고, 위성 엣지 다목적 타부 탐색(SE-MOTS)으로 구한 파레토 최적(한 목표를 더 좋게 하면 다른 목표가 나빠지는 균형점)의 비율을 바탕으로 여러 응용의 우선순위를 정하는 규칙을 제안했다. 마지막으로 저궤도(LEO)와 초저궤도(VLEO) 위성망을 비교해 알맞은 위성 고도와 작업 넘기기 전략을 논의했다.[^p3] | 1저자 T. Kim, 마지막 저자 최지환(공동 교신) |
| 4 | 2025 | [An Integration of Cryptography and Physical Layer Security for Multibeam Satellite Systems](https://doi.org/10.1109/tcomm.2024.3440873) · IEEE Transactions on Communications | 위성 신호는 넓게 뿌려지는 방송 성질 때문에 엿듣기 공격에 약하다. 이를 막으려고 물리 계층 보안(PLS)과 암호 기술이 따로 발전해 왔지만, 전력이 제한된 위성에서 하나씩만 쓰면 암호화에 드는 추가 비용과 엿듣는 쪽의 성능에 좌우되는 PLS의 성질 때문에 위성의 전력 소비와 보안 성능이 서로 맞바뀐다. 무선 채널 특성에 맞춰 바뀔 수 있는 PLS와 메시지 자체의 기밀을 지키는 암호의 서로 보완하는 성질을 살려, 다중 빔 위성망에서 둘을 통합했다. 엿듣는 쪽의 수에 따라 독립 공격과 협력 공격 각각의 엿듣기 위험을 추정하고, 전송과 계산에 쓰는 위성 전력 모델과 엿듣기 위험에 맞춘 가우시안 빔포밍(안테나 여러 개의 신호를 조절해 전파를 원하는 방향으로 모으는 기술)을 설계했으며, 비직교 다중 접속(NOMA, 여러 사용자가 같은 시간·주파수 자원을 함께 쓰는 접속 방식) 시스템에서 위성 전력 배분, 빔 일정, 보안 알고리즘 선택의 해를 유도했다. 엿듣기 위험이 커져도 안전한 전송 성능이 좋아짐을 보이고, 암호와 PLS 사이의 맞바꿈을 분석과 시뮬레이션으로 제시했다.[^p4] | 1저자 S. Jeon, 마지막 저자 최지환(공동 교신) |
| 5 | 2026 | [An Analytical Framework for HAPS Downlink Coverage Based on Stochastic Geometry](https://doi.org/10.1109/tcomm.2026.3663511) · IEEE Transactions on Communications | 앞으로의 통신망에서 큰 역할을 할 것으로 기대되는 고고도 플랫폼(HAPS)이 원 궤도를 따라 날며 도시의 휴대 단말 사용자에게 신호를 보내는 현실적인 하향 링크(기지국에서 사용자 쪽으로 가는 통신) 상황을 다뤘다. 확률 기하학(기지국과 사용자의 위치를 무작위 점들로 보고 성능을 수식으로 분석하는 방법)으로 분석하면서, HAPS의 원형 개구 안테나 모델을 반영하려고 시뮬레이션 자료로 근사를 더했다. 서비스 확률(coverage probability)과 평균 전송 용량(ergodic capacity)의 해석식을 유도하고 몬테카를로 시뮬레이션(무작위 표본을 많이 만들어 결과를 어림하는 계산)으로 타당성을 확인했다. 비행 반경·고도 같은 비행 변수가 서비스 확률에 주는 영향은 동시 서비스 사용자 수, 총 송신 전력 같은 통신 변수보다 작았고, 평균 전송 용량은 두 비행 변수가 작을수록 좋아졌으며 고도의 영향이 더 컸다. 비행 반경이 작을수록 망 성능에 유리하지만 기체 설계에 제약이 커지므로, 크기·무게·전력(SWaP) 한계와 통신 성능의 균형에 관한 실제 설계 지침도 제시했다.[^p5] | 1저자 G. Jang, 마지막 저자 최지환(교신) |
| 6 | 2024 | [3D Network Design for Multi-UAV RAN with THz-Empowered Backhaul](https://doi.org/10.1109/twc.2024.3440923) · IEEE Transactions on Wireless Communications | 6G에서 끊김 없는 연결을 이루려면 무인기(UAV)를 쓰는 3차원 망 설계가 필요하다. 무인기와 테라헤르츠(THz, 아주 높은 주파수의 전파) 망을 잇는 일은 유연성과 큰 용량의 잠재력에도 아직 풀리지 않은 문제다. 테라헤르츠 백홀(기지국과 핵심망 사이의 연결)을 갖춘 다중 무인기 무선 접속망(RAN)을 다루고, 사용자 쪽 마지막 연결에는 6GHz 이하 대역의 비직교 다중 접속(NOMA)을 썼다. 종단 간 처리량을 최대로 하려고 무인기의 3차원 배치·송신 전력·NOMA 복호 순서와 백홀 단말의 하이브리드 프리코딩(여러 안테나 신호를 아날로그와 디지털 단계로 나눠 조합하는 방식)·송신 전력을 함께 정하는 최적화 문제를 세우고, 변수를 차례로 최적화하는 과정을 제안했다. 수치 결과로 제안 방식이 다른 기준 방식보다 나음을 보이고, 안테나 구조·안테나 수·송신 전력·간섭에 따른 설계 지침을 제시했다.[^p6] | 1저자 K. Kim, 마지막 저자 최지환(교신) |
| 7 | 2026 | [Object Detection-based Deep Space Communications Signal Acquisition](https://doi.org/10.1109/taes.2026.3706645) · IEEE Transactions on Aerospace and Electronic Systems | 심우주 통신은 신호 대 잡음비가 매우 낮고, 도플러 편이(송신기와 수신기의 상대 운동으로 주파수가 바뀌는 현상)가 크며, 주파수가 시간에 따라 떠돌아 처음에 신호를 잡아내기(포착) 어렵다. 기존의 고속 푸리에 변환(FFT)·단시간 푸리에 변환(STFT) 기반 방법은 1차원에서 가장 큰 봉우리를 찾는 방식이라 PCM/PSK/PM(신호에 정보를 싣는 변조 방식들) 신호의 구조적인 스펙트럼에 속을 수 있다. 처음의 도플러 포착을 시간-주파수 영상에서 물체를 찾는 문제로 바꾼 물체 검출 기반 포착 기법(ODAT)을 제안했다. 최-윌리엄스 분포(신호를 시간-주파수 평면에 나타내는 방법의 하나), 검출기에 맞춘 전처리, YOLOv8 검출기(영상 속 물체의 위치를 상자로 찾아내는 딥러닝 모델)를 묶어, 찾아낸 상자의 모양으로 신호 검출과 도플러 추정을 함께 한다. 우주 통신 표준(CCSDS)에 맞춘 시뮬레이션에서 같은 오경보 조건으로 비교했을 때 기존·최근 방법보다 포착 확률이 높았고, 계산을 더 쓰는 대신 스펙트럼의 모호함에 강하고 상황마다 다시 조정할 필요가 줄었다.[^p7] | 1저자 M. Kim, 마지막 저자 최지환(교신) |
| 8 | 2022 | [Boundary-Oriented Binary Building Segmentation Model with Two Scheme Learning for Aerial Images](https://doi.org/10.1109/tgrs.2021.3089623) · IEEE Transactions on Geoscience and Remote Sensing | 항공 사진에서 건물을 나누어 찾는(분할) 딥러닝 모델이 여럿 나왔지만, 기존 합성곱 신경망(영상 위를 차례로 훑으며 국소적인 특징을 뽑는 신경망) 기반 방법은 건물의 모양과 경계를 정확히 잡지 못했다. 경계를 중시하는 이진 건물 분할 모델(B3SM)을 제안했다. 두 단계 학습(Scheme I·II)에서 첫 단계는 원래 영상을 대략 나눈 지도로 바꾸고, 둘째 단계는 이를 더 세밀하게 다듬으며, 두 단계는 새 연산자인 업샘플링 보간법(USIM)으로 잇는다. 건물 경계의 특징을 잘 뽑도록 경계 중심 손실 함수(B-Loss)를 쓰고, 모양과 경계를 정량 평가하려고 새 지표 B-IoU를 만들었다. 공개 자료와 자체 자료로 비교한 결과 다른 최신 모델보다 건물의 모양과 경계를 더 정확히 찾았다.[^p8] | 1저자 K. Lee, 최지환 교수는 6명 중 5번째 저자(공동 교신), 마지막 저자 J. Y. Hwang |

## 교수와 전문 분야

최지환 교수는 KAIST 항공우주공학과 부교수(Associate Professor)이고, 학과 교수진 목록은 연구 분야를 항공우주 통신(Aerospace Communications)과 기계학습 응용(Applications of Machine Learning)으로 적는다.[^aefac] 서울대학교에서 전기공학 학사(1998)를, 미국 MIT(Massachusetts Institute of Technology)에서 전기공학·컴퓨터과학 석사(2000)와 박사(2006)를 받았다.[^pi]

연구실 누리집의 PI 페이지에 따르면 교수는 2006년 9월부터 2012년 12월까지 미국 Marvell Semiconductor, Inc.의 Wireless R&D Group에서 Senior/Staff/Senior Staff/Principal Systems Engineer로 일했다.[^pi] 2013년 1월부터 2021년 2월까지 DGIST Dept. of Information and Communication Engineering의 조교수·부교수(Assistant/Associate Professor)였고, 그동안 2020년 4–12월 Dean of Information and Library Services를 맡았다.[^pi] 2016년 1월부터 2017년 12월까지 Institute for ICT Promotion(IITP)의 비상근 ICT R&D 기획자(Part-time ICT R&D Planner, RP)를, 2019년 2월부터 2020년 2월까지 미국 샌디에이고의 Samsung Semiconductor, Inc. SoC Lab에서 방문 연구원(Visiting Research Scientist)을 지냈다. 2021년 2월부터 KAIST 항공우주공학과 부교수다.[^pi]

교수는 IEEE Transactions on Aerospace and Electronic Systems(2019–), IEEE Aerospace and Electronic Systems Magazine(2025–), International Journal of Aeronautical and Space Sciences(2025–)의 부편집장(Associate Editor)이다.[^pi] IEEE Globecom 2024의 Selected Area in Communication – Aerial Communications 의장(Chair)과 IEEE ICC 2022의 Web Chair를 맡았고, Samsung Research(2021), Samsung Electronics(2023), Korea Aerospace Industries(KAI, 2024–)의 기술 자문위원(technical advisory board member)이다.[^pi]

랩 논문 목록으로 보면 교수는 박사과정 시절부터 위성통신을 연구해 왔다. 목록에는 날씨 때문에 나빠지는 위성 채널을 예측하고 적응하는 연구, 다중 빔 위성의 하향 링크 전력과 빔 배분 연구(2002–2009년, V. W. S. Chan과 공저)가 있고, 여러 안테나와 직교 주파수 분할 다중화(OFDM, 데이터를 여러 주파수에 나눠 동시에 보내는 방식)를 쓰는 무선 시스템의 추정·복조·자원 배분 논문(2008–2014년)도 있다.[^pubs] KAIST 시기에는 저궤도 메가 군집 위성망, 위성 엣지 컴퓨팅, 위성 보안, 고고도 플랫폼·무인기 공중망, 그리고 딥러닝을 쓰는 신호 포착과 항공 영상 분석으로 넓혀 왔다(대표 논문 1–8).[^p1][^p2][^p3][^p4][^p5][^p6][^p7][^p8]

## 응용 분야

대표 논문들은 여러 관문국이 있는 저궤도 메가 군집에서 전 지구를 잇는 비지상 네트워크의 길을 열고,[^p1] 사물인터넷을 위한 위성 엣지 컴퓨팅의 알맞은 위성 고도와 작업 넘기기 전략을 논의하며,[^p3] 고고도 플랫폼의 크기·무게·전력 한계와 통신 성능의 균형에 관한 실제 설계 지침을 제시한다고 밝힌다.[^p5] 연구실 누리집의 과제 페이지는 Korea Aerospace Research Institute(KARI)의 거대 위성망 지능형 경로 설정 연구, National Research Foundation of Korea(NRF)의 6G 소프트웨어 정의 위성망 연구, Korea Evaluation Institute of Industrial Technology(KEIT)의 Q·V 대역 고처리량 통신망 알고리즘 개발을 교수가 연구책임자(PI)로 맡은 과제로 적는다.[^projects] Korea AeroSpace Administration(KASA)의 미래우주교육센터(Future Space Education Center) 과제에서는 여러 임무를 맡는 저궤도 위성 군집의 우주 통신을 다루고(PI), Institute for Information & Communications Technology Promotion(IITP)의 도심항공교통(UAM)을 위한 초고신뢰 공중망(URAN) ICT 연구센터, Korea Institute for Advancement of Technology(KIAT)의 초광대역 무선 송수신기용 소프트웨어 정의 물리 계층 개발, KAIST의 AI 전환 항공우주 연구센터, 실시간 도시를 위한 자율 공간지능 기반시설 과제에는 공동 연구책임자(co-PI)로 참여한다.[^projects] 랩 논문 목록에는 탄소 중립 우주 데이터센터의 개발을 다룬 Nature Electronics 2025 글과, 딥러닝으로 한 방울에서 여러 맛을 읽는 미각 모사 센서 연구(ACS Applied Materials & Interfaces 2023, 공동 교신저자)도 있다.[^pubs]

## 최근 논문 목록 (2021–2026)

랩 Publications 페이지의 Book Chapter·Journal Articles·Conference Papers 칸에서 연도가 2021–2026년인 38편(학술지 논문 23, 책 속 장 1, 학회 논문 14)이다. 저자 순서와 제목·학술지·학회 이름은 랩 표기 그대로다. 교수 개인의 논문 목록이며, 2021년 항목에는 KAIST 부임 전후의 논문이 섞여 있을 수 있어 모두 현재 KAIST 연구실의 성과로 묶지 않는다.[^pubs]

**2026**

- S. Kim, D. -E. Kim, J. P. Choi. "Self-Orchestrated AP Switching Optimization via Network Uncertainty Awareness for 6G AI-RAN". *IEEE Transactions on Wireless Communications, vol. 25, pp. 22509-22525, 2026*.
- W. Cha, K. Kim, S. Kim, J. Choi, J. P. Choi. "Demand-Aware Cooperative Transmission Design for Energy-Efficient LEO Satellite Networks". *IEEE Transactions on Wireless Communications, vol. 25, pp. 22588-22604, 2026*.
- M. Kim, J. P. Choi. "Object Detection-based Deep Space Communications Signal Acquisition". *IEEE Transactions on Aerospace and Electronic Systems, vol. 62, pp. 13063-13076, 2026*.
- S. Kim, G. Im, J. G. Ryu, J. P. Choi. "Orthogonal Time-Frequency Space Modulation with DFT Precoded Filter Bank Multicarrier". *IEEE Wireless Communications Letters, vol. 15, pp. 2839-2843, 2026*.
- G. Jang, D. -E. Kim, J. P. Choi. "An Analytical Framework for HAPS Downlink Coverage Based on Stochastic Geometry". *IEEE Trans. on Communications, vol. 74, pp. 5122-5137, 2026*.
- S. Kim, I. Choi, Y. Lee, J. P. Choi. "Multi-Gateway Feeder Link Switching Optimization in Multi-Shell LEO Mega-Constellations". *IEEE Trans. on Communications, vol. 74, pp. 2857-2873, 2026*.
- G. Jang, J. P. Choi. "Framework for Evaluating Fixed-Wing HALE Detection Probability under Hostile Ground-Based Radar Surveillance". *IEEE ICC (International Conference on Communications), May 2026*.
- E. Y. Kim, S. Kim, J. P. Choi. "A Two-Layer RSMA Framework for Internal Secrecy in Multibeam Satellite Communications". *IEEE ICC (International Conference on Communications) Workshops, May 2026*.
- D.-e. Kim, S. Kim, J. P. Choi. "Latency-Centric RAN Orchestration with World Model for Satellite-Assisted Mobile Edge Computing". *IEEE ICC (International Conference on Communications) Workshops, May 2026*.
- S. Kim, J. P. Choi. "Explicit LEO Satellite Constellation Design and Coverage Analysis of Clustered Space SDN". *IEEE ICC (International Conference on Communications) Workshops, May 2026*.
- K. Kim, J. P. Choi. "Joint Beamforming and Space-Time Filtering for Cell-Free LEO Satellite ISAC Networks with Non-Uniform ISAC Demands". *IEEE ICC (International Conference on Communications) Workshops, May 2026*.

**2025**

- A. Ablimit, J. P. Choi, Y. S. Ong, Y. Wen. "The Development of Carbon-neutral Data Centres in Space". *Nature Electronics, vol. 8, pp. 1016–1026, Nov. 2025*.
- I. Choi, S. Kim, Y. Lee, J. P. Choi. "A Scalable Multi-Controller SDN Framework for LEO Mega-Constellation via Topology Virtualization". *IEEE Internet of Things Journal, vol. 12, no. 16, pp. 33311-33327, Aug. 2025*.
- G. Jang, J. P. Choi. "HAPS Altitude Optimization for Downlink Communications: Alleviating the Effect of Channel Elevation Angles". *IEEE Trans. on Aerospace and Electronic Systems, vol. 61, no. 4, pp. 9856-9865, Aug. 2025*.
- T. Kim, S. Kim, J. Kwak, J. P. Choi. "Satellite Network Slice Planning with Handover Trigger and DRL-Based Virtual Network Embedding". *IEEE Trans. on Aerospace and Electronic Systems, vol. 61, no. 2, pp. 3193-3204, April 2025*.
- S. Jeon, J. Kwak, J. P. Choi. "An Integration of Cryptography and Physical Layer Security for Multibeam Satellite Systems". *IEEE Trans. on Communications, vol. 73, no. 2, pp. 1087-1099, Feb. 2025*.
- G. Jang, D.-e. Kim, J. P. Choi. "Stochastic Geometry-based Coverage Analysis of HAPS Downlink in Urban Environments". *IEEE Globecom (Global Communications Conference), Dec. 2025*.
- K. Kim, I. Choi, J. P. Choi. "A Low-Latency Handover Framework in Integrated Aerial-LEO Satellite Networks for IoT Connectivity". *IEEE Globecom (Global Communications Conference) Workshops, Dec. 2025*.
- S. Kim, J. P. Choi. "Traffic Splitting of LEO Mega-Constellations with Non-Coherent Cell-Free Massive MIMO Systems". *IEEE ICC (International Conference on Communications), June 2025*.
- K. Kim, J. P. Choi. "Joint Beamforming and Temporal Resource Allocation for RIS-aided Integrated Terrestrial and Aerial Networks Based on Reverse TDD". *IEEE ICC (International Conference on Communications), June 2025*.
- K. Kim, W. Cha, J. P. Choi. "UAV-Aided Delay-Oriented IoT Data Collection Strategies Using a Pattern Search Framework". *IEEE WCNC (Wireless Communications and Networking Conference), March 2025*.

**2024**

- T. Kim, J. Kwak, J. P. Choi. "6G satellite network architecture with onboard computing capabilities". *in “Integration of MTC and Satellites for IoT toward 6G Era,” Editors: Alves, Mikhaylov, Höyhtyä, Wiley/IEEE Press, July 2024*.
- K. Kim, J. P. Choi. "3D Network Design for Multi-UAV RAN with THz-Empowered Backhaul". *IEEE Trans. on Wireless Communications, vol. 23, no. 11, pp. 16437-16452, Nov. 2024*.

**2023**

- H. H. Jung, J. Yea, H. Lee, H. N. Jung, J. Jekal, H. Lee, J. Ha, S. Oh, S. Song, J. Son, T. S. Yu, S. Jung, C. Lee, J. Kwak, J. P. Choi, K.-I. Jang. "Taste Bud-Inspired Single-Drop Multitaste Sensing for Comprehensive Flavor Analysis with Deep Learning Algorithms". *ACS Applied Materials & Interfaces, 2023, 15, 39, 46041–46053, Sept. 2023*.
- T. Kim, J. Kwak, J. P. Choi. "Satellite Network Slice Planning: Architecture, Performance Analysis, and Open Issues". *IEEE Vehicular Technology Magazine, vol. 18, no. 2, pp. 29-38, June 2023*.
- D. Kim, J. P. Choi. "A Reliable Handover Strategy with Second Satellite Selection in LEO Satellite Networks". *IEEE Globecom (Global Communications Conference) Workshops, Dec. 2023*.
- S. Kim, J. P. Choi. "Satellite User Grouping and Multi-Beam Patterning for Generalized Rate-Splitting Multiple Access". *IEEE ICC (International Conference on Communications) Workshops, May 2023*.
- K. Kim, J. P. Choi. "Joint Optimization of UAV Deployment and Power Allocation in Vertical mmWave Backhaul/NOMA Networks". *IEEE ICC (International Conference on Communications), May 2023*.

**2022**

- T. Kim, J. Kwak, J. P. Choi. "Satellite Edge Computing Architecture and Network Slice Scheduling for IoT Support". *IEEE Internet of Things Journal, vol. 9, no. 16, pp. 14938-14951, Aug. 2022*.
- S. Jeon, J. Kwak, J. P. Choi. "Cross-Layer Encryption of CFB-AES-TURBO for Advanced Satellite Data Transmission Security". *IEEE Trans. on Aerospace and Electronic Systems, vol. 58, no. 3, pp. 2192-2205, June 2022*.
- K. Lee, J. Kim, H. Lee, J. Park, J. P. Choi, J. Y. Hwang. "Boundary-Oriented Binary Building Segmentation Model with Two Scheme Learning for Aerial Images". *IEEE Trans. on Geoscience and Remote Sensing, vol. 60, pp. 1-17, 2022*.
- S. Jeon, J. Kwak, J. P. Choi. "Advanced Multibeam Satellite Network Security with Encryption and Beamforming Technologies". *IEEE ICC (International Conference on Communications) Workshops, May 2022*.

**2021**

- Y. Lee, J. P. Choi. "Connectivity Analysis of Mega Constellation Satellite Networks with Optical Inter-Satellite Links". *IEEE Trans. on Aerospace and Electronic Systems, vol. 57, no. 6, pp. 4213-4226, Dec. 2021*.
- M. Hosseinian, J. P. Choi, S.-H. Chang, J. Lee. "Review of 5G NTN Standards Development and Technical Challenges for Satellite Integration with the 5G Network". *IEEE Aerospace and Electronic Systems Magazine, vol. 36, no. 8, pp. 22-31, Aug. 2021*.
- S. Jung, J. P. Choi. "Reliability of Small Satellite Networks with Software-Defined Radio and Enhanced Multiple Access Protocol". *IEEE Trans. on Aerospace and Electronic Systems, vol. 57, no. 3, pp. 1891-1902, June 2021*.
- Y. Na, J. H. Kim, K. Lee, J. Park, J. Y. Hwang, J. P. Choi. "Domain Adaptive Transfer Attack (DATA)-based Segmentation Networks for Building Extraction from Aerial Images". *IEEE Transactions on Geoscience and Remote Sensing, vol. 59, no. 6, pp. 5171 - 5182, June 2021*.
- H. Lee, K. Lee, J. Kim, Y. Na, J. Park, J. P. Choi, J. Y. Hwang. "Local Similarity Siamese Network for Urban Land Change Detection on Remote Sensing Images". *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 14, pp. 4139-4149, 2021*.
- S. Jung, J. P. Choi. "End-to-End Reliability of Satellite Communication Network Systems". *IEEE Systems Journal, vol. 15, no. 1, pp. 791-801, Mar. 2021*.

## 과제

랩 Projects 페이지가 진행 중인 과제(Current Projects)로 적은 8건이다. 과제명·기간·지원 기관·역할은 랩 표기 그대로다.[^projects]

- Living 3D Space: The Autonomous Spatial Intelligence Infrastructure for Real-Time Cities (기간 4/2026-12/2033; 지원 Korea Evaluation Institute of Industrial Technology (KEIT); 역할 co-PI)
- Study on the Intelligent Routing Technology of Mega Satellite Networks (기간 11/2025-10/2026; 지원 Korea Aerospace Research Institute (KARI); 역할 PI)
- Virtualized, Open, and Intelligent 6G Software-defined Satellite Networks (기간 9/2025-8/2028; 지원 National Research Foundation (NRF) of Korea; 역할 PI)
- AI-Transformed Aerospace Research Center (기간 7/2025-12/2029; 지원 Korea Advanced Institute of Science and Technology (KAIST); 역할 co-PI)
- Embedded Software-defined PHY-Layer Enabled on Ultrawideband Wireless Transceiver Solution (기간 8/2024-12/2027; 지원 Korea Institute for Advancement of Technology (KIAT); 역할 co-PI)
- Development of High-throughput Communication Network Algorithms for Q/V Band (기간 7/2024-12/2028; 지원 Korea Evaluation Institute of Industrial Technology (KEIT); 역할 PI)
- Future Space Education Center: Space Communications with Multi-Mission Low-Earth-Orbit Satellite Constellations (기간 4/2022-12/2026; 지원 Korea AeroSpace Administration (KASA); 역할 PI)
- ICT Research Center: Ultra Reliable Aerial Network (URAN) Supporting High-Density Urban Air Mobility (UAM) (기간 7/2021-12/2028; 지원 Institute for Information & Communications Technology Promotion (IITP); 역할 co-PI)

## 연락과 위치

- 교수 연구실: KAIST N7-2동 4308호[^aelab][^aefac]
- 전화: 042-350-3738[^aelab]
- 교수 이메일: jhch@kaist.ac.kr[^pi][^aefac]
- 학과 주소: (34141) 대전광역시 유성구 대학로 291 KAIST 항공우주공학과[^aelab]
[^research]: 연구실 누리집 Research 페이지 <https://acai-kaist.github.io/research/> (Satellite Communications·Wireless Communications·Applications of machine learning and deep learning 칸, 2026-10-22 열람)
[^pi]: 연구실 누리집 PI 페이지 <https://acai-kaist.github.io/pi/> (학력, 경력, 학회·편집 활동, 이메일, 2026-10-22 열람)
[^pubs]: 연구실 누리집 Publications 페이지 <https://acai-kaist.github.io/publications/> (Book Chapter·Journal Articles·Conference Papers 칸, 2026-10-22 열람)
[^projects]: 연구실 누리집 Projects 페이지 <https://acai-kaist.github.io/projects/> (Current Projects, 2026-10-22 열람)
[^aelab]: KAIST 항공우주공학과 연구실 소개 「Aerospace Communications and Applied Intelligence (ACAI) Lab」 <https://ae.kaist.ac.kr/boards/view/board_lab/92> (연구실명, 교수, 연구실 소개, 연구분야, 전화, 오피스, 학과 주소, 2026-10-22 열람)
[^aefac]: KAIST 항공우주공학과 교수진 <https://ae.kaist.ac.kr/boards/lists/board_faculty/sc_category/1/> (직위, 학력, 연구 분야, 이메일, 오피스, 2026-10-22 열람)
[^sselab]: KAIST 반도체시스템공학과 연구실 명단 <https://sse.kaist.ac.kr/research-laboratory/> (2026-10-22 열람)
[^p1]: S. Kim, I. Choi, Y. Lee, J. P. Choi, IEEE Transactions on Communications 74, 2857-2873 (2026). <https://doi.org/10.1109/tcomm.2025.3648974> 초록 기준(Semantic Scholar 등록 초록).
[^p2]: I. Choi, S. Kim, Y. Lee, J. P. Choi, IEEE Internet of Things Journal 12, 33311-33327 (2025). <https://doi.org/10.1109/jiot.2025.3576912> 초록 기준(Semantic Scholar 등록 초록).
[^p3]: T. Kim, J. Kwak, J. P. Choi, IEEE Internet of Things Journal 9, 14938-14951 (2022). <https://doi.org/10.1109/jiot.2021.3132171> 초록 기준(Semantic Scholar 등록 초록).
[^p4]: S. Jeon, J. Kwak, J. P. Choi, IEEE Transactions on Communications 73, 1087-1099 (2025). <https://doi.org/10.1109/tcomm.2024.3440873> 초록 기준(Semantic Scholar 등록 초록).
[^p5]: G. Jang, D.-e. Kim, J. P. Choi, IEEE Transactions on Communications 74, 5122-5137 (2026). <https://doi.org/10.1109/tcomm.2026.3663511> 초록 기준(Semantic Scholar 등록 초록).
[^p6]: K. Kim, J. P. Choi, IEEE Transactions on Wireless Communications 23, 16437-16452 (2024). <https://doi.org/10.1109/twc.2024.3440923> 초록 기준(Semantic Scholar 등록 초록).
[^p7]: M. Kim, J. P. Choi, IEEE Transactions on Aerospace and Electronic Systems 62, 13063-13076 (2026). <https://doi.org/10.1109/taes.2026.3706645> 초록 기준(Semantic Scholar 등록 초록).
[^p8]: K. Lee 외, J. Y. Hwang, IEEE Transactions on Geoscience and Remote Sensing 60, 1-17 (2022). <https://doi.org/10.1109/tgrs.2021.3089623> 초록 기준(Semantic Scholar 등록 초록).

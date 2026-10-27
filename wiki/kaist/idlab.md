# 모빌리티 시스템 혁신 설계 연구실 (Innovative Design for Mobility Systems Laboratory, ID LAB)

**KAIST 조천식모빌리티대학원 · 장인권 교수**

- 분야: 공학 시스템의 최적 설계, 다중 수신 무선전력전송, 차량 경로 최적화, 골격계 영상 재구성과 생체역학 해석
- 대분야: 기계·로봇·제조, 전기전자·반도체·광학
- 태그: 무선 전력 전송[^research][^p1][^p2], 전산역학·수치 해석[^research][^p7], 생체역학[^research][^p6][^p8], 의료 영상 기기·재구성[^research], 수리 최적화·최적화 알고리즘[^research], 설계 최적화(위상·형상 최적화)[^research]
- 홈페이지: <https://idlab.kaist.ac.kr/>
- 근거와 출처: [ID LAB 근거 페이지](idlab-sources.md)

> 무선으로 전력을 보내는 장치, 사람과 차량의 이동 경로, 뼈의 구조와 영상을 컴퓨터로 분석하고 최적화하여 설계하는 연구실이다.[^research][^home]

## 무엇을 연구하나

장인권 교수가 이끄는 ID LAB은 전자기 시스템, 모빌리티 시스템, 생체역학 시스템을 연구한다. 공통 도구는 전산해석(물리 현상이나 시스템의 작동을 컴퓨터로 계산하는 방법)과 최적화(정해진 조건을 만족하면서 목표 값을 최대로 또는 최소로 만드는 해를 찾는 계산)다. 설계에서 바꿀 수 있는 값과 지켜야 할 조건을 정한 다음, 계산을 반복하여 실제 공학 시스템의 설계를 찾는다. 연구실은 이러한 방법으로 사람과 차량의 이동을 위한 시스템을 제안하는 것을 목표로 한다.[^research]

전자기 분야에서는 **다중 수신 무선전력전송**을 다룬다. 이는 전선으로 연결하지 않고 전력을 보내는 장치에서 여러 수신기가 전력을 받는 구조다. 연구실은 수신기 사이의 전자기적 상호작용까지 고려하여 공진 조건(주기적 자극에 반응하는 시스템의 진동 응답이 특정 주파수(단위 시간에 반복되는 진동의 횟수) 부근에서 극대가 되는 조건)과 부하(전력을 공급받아 사용하는 회로나 장치)의 조건을 결정하는 방법을 개발한다. 필요한 정격 전력(기기가 정해진 조건에서 사용하도록 규정된 전력)을 만족하면서 전송 효율을 최대화하는 것이 연구 목표다. 코일의 형상, 공진 회로, 상호 인덕턴스(한 회로의 전류 변화가 다른 회로에 유도하는 전압의 관계를 나타내는 양) 추정과 코일의 위치 어긋남 검출도 소개한다.[^research][^home]

모빌리티 분야에서는 **이동 경로를 수학적으로 표현하고 최적화하는 방법**을 개발한다. 도로 연결망을 전기회로와 대응시켜, 기준 경로와 루프 변수(연결망의 닫힌 경로를 따라 흐르는 양을 나타내는 계산 변수)로 이동 경로를 표현한다. 이 표현은 각 지점으로 들어오고 나가는 교통 흐름의 보존을 자체적으로 만족하도록 만들어졌다. 연구실은 이를 최단 경로 문제(두 지점 사이에서 이동 비용이 최소인 경로를 찾는 문제)와 외판원 문제(모든 방문 지점을 한 번씩 거쳐 출발점으로 돌아오는 최소 비용 경로를 찾는 문제)에 적용한다. 지하철 환승 비용을 고려한 경로와, 학습 자료를 생성하여 신경망(서로 연결된 계산 단위들의 연결 강도를 조정하여 입력과 출력의 관계를 학습하는 모형)으로 경로를 구하는 방법도 연구한다.[^research]

생체역학 분야에서는 **힘을 받는 뼈의 구조 변화와 영상 재구성**을 다룬다. 위상최적설계(설계 영역 안에서 재료의 배치와 연결 관계를 정하는 최적 설계 방법)로 뼈의 구조를 계산하고, 유한요소해석(대상을 요소로 나누어 각 요소의 관계식으로 전체의 물리적 거동을 계산하는 방법)과 딥러닝(여러 단계의 표현을 학습하는 기계학습 방법)을 결합한다. 보행 때 시간에 따라 변하는 힘을 대표하는 정적 하중(시간에 따른 변화와 관성 효과를 무시하고 다루는 힘)으로 나타내는 방법, 임상 영상에서 구분하기 어려운 해면골(뼈 내부에서 연결된 뼈 조직과 빈 공간이 그물 구조를 이루는 부분)의 구조를 재구성하는 방법을 개발한다. 전체 영상을 패치(영상을 나눈 부분 영역)별로 재구성한 뒤 이어 붙이는 접근도 소개한다. 이는 개인별 골강도 평가를 위한 방법 개발이며, 연구 소개는 임상 활용의 가능성으로 설명한다.[^research]

최근 논문에서는 무선충전 장치의 고장을 상호 인덕턴스 추정으로 검출했고,[^p1] 기준 연결선의 흐름을 도입하여 선형계획법(목표식과 조건식이 변수에 대한 일차식으로 이루어진 최적화 방법)으로 경로를 계산했다.[^p3] 구조 연구에서는 보행의 개인차를 반영하는 정적 하중 추출법을 제안하고,[^p6] 인공 뼈에서 반사파(경계와 상호작용한 뒤 되돌아오는 파동)로 탄성계수(힘을 없애면 원래 상태로 돌아오는 변형에서, 단위 면적당 힘과 상대적인 변형 크기의 관계를 나타내는 계수)를 추정하는 측정 구성을 제안했다. 이산요소 모형(개별 입자와 그 접촉 관계로 전체 거동을 계산하는 모형)으로 이 파동과 뼈 시편의 상호작용도 재현했다.[^p7]

## 주요 연구 주제

### 1. 전자기 시스템의 동작 조건과 설계

여러 수신기가 서로 영향을 주는 무선전력전송에서 공진 조건과 부하 조건을 함께 고려한다. 코일 형상과 공진 회로를 설계하고, 상호 인덕턴스를 추정하여 다중 수신 시스템의 동작 상태와 코일 위치 어긋남을 다룬다.[^research][^home]

### 2. 차량과 교통 연결망의 경로 최적화

기준 경로와 루프 변수를 이용하는 경로 표현을 바탕으로, 방문 지점이 정해진 차량의 경로와 두 지점 사이의 최단 경로를 계산한다. 지하철 연결망에서 환승 비용을 반영하고, 최적화로 만든 자료를 이용하는 학습 방법을 연구한다.[^research]

### 3. 뼈의 구조 변화와 골격계 영상 재구성

시간에 따라 반복되는 힘의 영향을 대표 정적 하중으로 반영하고, 위상최적설계로 뼈의 구조 변화를 계산한다. 영상의 부분 영역을 딥러닝으로 재구성하고 이어 붙여 전체 골격 구조를 얻는 방법을 개발한다.[^research]

## 대표 논문

연구실 목록의 2021–2026년 논문 가운데 장인권 교수가 저자인 논문을 전자기 시스템 최적화 2편, 경로 최적화 3편, 구조·생체역학 방법 3편으로 골랐다. 연도는 연구실 목록의 권호 연도다. "쉽게 말하면" 칸은 각 논문의 등록 초록만을 근거로 썼으며, 초록 출처는 각주에 밝혔다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2026 | [Fault Detection of Coil Misalignment in Multi-Receiver Wireless Power Transfer Systems With the Estimated Mutual Inductance](https://doi.org/10.1109/TIE.2026.3675172) · IEEE Transactions on Industrial Electronics | 여러 기기가 한 충전 패드 위에서 움직이면 코일 위치가 어긋날 수 있다. 송신기와 수신기 사이, 수신기들 사이의 상호 인덕턴스를 두 단계로 추정한 뒤, 추정값과 미리 정한 기준을 비교하여 위치 어긋남을 검출하는 방법을 제안했다. 수신기 세 개를 둔 시제품으로 추정과 고장 검출을 검증했다.[^p1] | 1저자 Mingi Kim, 장인권 마지막 저자 |
| 2 | 2021 | [Determination of the Optimal Resonant Condition for Multireceiver Wireless Power Transfer Systems Considering the Transfer Efficiency and Different Rated Powers With Altered Coupling Effects](https://doi.org/10.1109/JESTPE.2020.2983824) · IEEE Journal of Emerging and Selected Topics in Power Electronics | 여러 수신기가 서로 다른 정격 전력을 요구할 때, 그 요구를 모두 만족하면서 전송 효율을 최대화하는 공진 조건을 찾는 방법을 제안했다. 전기적 성능을 계산하는 부분과 최적화하는 부분을 연결하여 설계 변수를 반복 갱신한다. 여러 수신기가 있는 시스템의 배치와 결합 상태를 바꾼 실험으로 방법의 성능과 가능성을 확인했다.[^p2] | 1저자 Seung Beop Lee, 장인권 마지막 저자 |
| 3 | 2025 | [Linear Programming of the Loopwise Route Representation for the Shortest Path Problems by Introducing the Reference Link Flow](https://doi.org/10.1109/ACCESS.2025.3546320) · IEEE Access | 기존 루프 경로 표현을 최적화할 때 필요한 비선형 계산(변수 관계를 일차식으로 나타낼 수 없는 계산)의 부담을 다뤘다. 기준 연결선의 흐름을 먼저 고르고, 이를 이용하여 선형 최적화 문제를 만드는 두 단계 방법을 제안했다. 격자형 연결망 실험에서 기존 정수 선형계획법(일부 또는 모든 변수를 정수로 제한하는 선형 최적화)보다 계산 시간과 해의 정확도가 나은 결과를 얻었다. 다른 차량 경로 문제로의 확장은 후속 연구 가능성으로 제시했다.[^p3] | 1저자 Geunu Kim, 장인권 마지막 저자 |
| 4 | 2023 | [Loop-Wise Route Representation and Its Optimization Formulation for Symmetric Traveling Salesman Problems](https://doi.org/10.1109/TITS.2023.3271313) · IEEE Transactions on Intelligent Transportation Systems | 기준 경로와 연속적인 루프 변수로 차량 경로를 나타내는 방법을 제안했다. 각 지점에서 경로가 이어지는 조건을 별도 제약식 없이 만족하도록 하고, 이를 평면 연결망의 외판원 문제에 적용했다. 네 가지 사례에서 기존 유전 알고리즘(해 후보를 선택하고 그 일부를 서로 조합하거나 바꾸는 과정을 반복하는 최적화 방법)과 비교하여 계산 효율을 평가했다.[^p4] | 1저자 Geunu Kim, 장인권 마지막 저자 |
| 5 | 2022 | [Loopwise Route Representation-Based Topology Optimization for the Shortest Path Problems](https://doi.org/10.1109/ACCESS.2022.3227388) · IEEE Access | 전기회로와 도로 교통 연결망의 유사성에 착안하여, 루프 전류에 대응하는 계산 변수를 도입했다. 이를 바탕으로 이동 비용을 최소화하는 위상최적설계로 최단 경로를 구한다. 각 지점의 흐름 보존을 별도 제약식 없이 만족시키며, 대칭·비대칭 연결망의 격자 사례에서 방법을 확인했다. 일반 차량 경로 문제로의 확장은 가능성으로 남겼다.[^p5] | 1저자 Geunu Kim, 장인권 마지막 저자 |
| 6 | 2022 | [Framework of sampling the subject-specific static loads from the gait cycle of interindividual variation](https://doi.org/10.1016/j.cmpb.2022.107054) · Computer Methods and Programs in Biomedicine | 보행 방식의 개인차를 뼈 구조 계산에 반영하기 위해, 각 보행 주기에서 개인별 정적 하중을 추출하는 방법을 제안했다. 보행 주기를 공통 좌표로 바꾸어 대표 하중을 정하고, 이를 다시 개인별 좌표로 되돌린다. 전체 보행 주기를 사용한 계산과 비교해 뼈 질량 분포와 겉보기 강성의 오차 및 계산 비용을 평가했으며, 정상·비정상 보행 주기에 모두 적용했다.[^p6] | 1저자 Bong Ju Chun, 장인권 마지막 저자 |
| 7 | 2026 | [Interaction of highly nonlinear solitary waves with 3D-printed artificial bone](https://doi.org/10.1080/15376494.2025.2601267) · Mechanics of Advanced Materials and Structures | 뼈의 미세구조를 재현한 인공 시편에서 파동을 반사시켜 뼈의 탄성계수를 추정하는 연구다. 측정 구성을 바꾸고 파동과 시편의 상호작용을 계산하는 이산요소 모형을 개발했다. 반사파의 특징과 시편 탄성계수의 관계를 실험·계산으로 평가했으며, 계산에서 다루지 않은 변형 속도의 영향으로 강성을 낮게 예측하는 한계도 밝혔다.[^p7] | 1저자 Mariam Barakat, 장인권 6명 중 4번째 저자 |
| 8 | 2021 | [Determination of the representative static loads for cyclically repeated dynamic loads: a case study of bone remodeling simulation with gait loads](https://doi.org/10.1016/j.cmpb.2020.105924) · Computer Methods and Programs in Biomedicine | 뼈의 구조가 힘에 반응해 바뀌는 현상을 계산할 때, 반복되는 전체 보행 하중 대신 그 효과를 대표하는 정적 하중과 계수를 찾는 방법을 제안했다. 변형에 저장되는 에너지의 공간 분포 오차를 줄이도록 최적화한 뒤, 비슷한 후보 하중들을 묶어 대표값을 정한다. 전체 보행 주기를 쓰는 계산과 비교하여 뼈의 질량 분포·겉보기 강성 오차와 계산 함수 호출 수를 평가했다.[^p8] | 1저자 Bong Ju Chun, 장인권 마지막 저자 |

## 교수와 전문 분야

장인권 교수(In Gwun Jang)는 KAIST 기계공학 학사(1997), 석사(1999), 박사(2006) 학위를 받았다. 박사학위 논문 주제는 설계 공간을 조정하고 세분하는 진화적 위상최적설계다. 캐나다 Queen’s University에서 박사후연구원으로 재직했고(2006년 11월–2009년 3월), KAIST 해양시스템공학 연구조교수(2009년 4월–2010년 12월)를 거쳐 조천식모빌리티대학원 조교수(2011년 1월–2016년 2월), 부교수(2016년 3월–2024년 8월), 교수(2024년 9월부터)로 경력을 적고 있다.[^members]

전문 분야는 모빌리티 시스템의 최적 설계, 다중 물리 문제의 모형화와 시뮬레이션(대상 시스템의 작동을 모형으로 재현하는 계산), 시스템 공학이다. 연구 소개에서 이를 무선전력전송의 동작 조건, 차량 경로 표현, 뼈의 구조와 영상 재구성으로 구체화한다.[^members][^research] 연구실 구성원 자료의 대학원장 경력 기간은 **2021년 3월–2026년 2월**이다.[^members] 2025년 1월 15일 소식은 한국최적설계학회 정기학술대회의 피도텍 유망연구자상 수상을 알린다.[^notices]

## 응용 분야

연구실은 전기차와 휴대기기 등에 쓰는 무선전력전송, 도로·지하철 연결망의 경로 계산, 개인별 뼈 구조와 골강도 평가 방법을 응용 대상으로 든다. 골격계 연구는 영상 재구성과 역학 계산 방법을 개발하는 접근이다.[^research] 과제 목록에는 로봇 군집 무선충전, 자율주행 기반 도시환경관리, 냉장 전기차량을 이용한 신선물류 배송, 도시교통의 계산 기반 운영을 위한 기술 개발이 올라 있다.[^projects]

## 구성원

2026년 10월 26일 연구실 구성원 자료의 Student 10명이다. 과정과 LAB Leader 표기는 원문을 따랐다. 연구 그룹은 ESO(전자기 시스템 최적화), MSO(모빌리티 시스템 최적화), BSO(생체역학 시스템 최적화)이며, ESO (WPT)와 TBD도 원문 표기다. 시작 시점은 별도로 게시되어 있지 않다.[^members][^research] "대표 논문 참여"는 위 대표 논문 표의 번호이며, 전체 저자 명단에서 이름이 일치한 경우 표시했다.

| 이름 | 과정 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| 강민석 (Minseok Kang) | 박사과정 | ESO (WPT) | seok1598@kaist.ac.kr | 1 |
| 고혁진 (Hyukjin Koh) | 박사과정 | BSO | hyukjin.koh@kaist.ac.kr |  |
| 김정훈 (Jeonghun Kim) | 박사과정 | MSO | jhkim17@kaist.ac.kr | 3 |
| 김창영 (Changyeong Kim) | 박사과정 (LAB Leader) | BSO | kimcy0789@kaist.ac.kr | 3 |
| 박상훈 (Sanghoon Park) | 박사과정 | MSO | sanghoon10233@kaist.ac.kr | 3 |
| 권순열 (Sunyeol Gwon) | 박사과정 | ESO | sy3548@kaist.ac.kr | 1 |
| 이은결 (Eungyeol Lee) | 석사과정 | MSO | eungyeol@kaist.ac.kr |  |
| 이한빈 (Hanbeen Lee) | 석사과정 | ESO | 1218hanbin@kaist.ac.kr |  |
| 정지희 (Jihee Jung) | 석사과정 | TBD | jungjihee9@kaist.ac.kr |  |
| 이순용 (Soonyong Lee) | 석사과정 | TBD | ls.yong@kaist.ac.kr |  |

## 졸업생과 이전 구성원

연구실 구성원 자료의 Alumni 24행으로, 박사 7행과 석사 17행이다. 학위 연도는 2013–2026년이다. 현재 박사과정 학생 6명도 석사 학위 기록으로 이 표에 올라 있다. 같은 자료에서 진로 직위가 다르게 적힌 경우 아래 표에는 공통으로 적힌 기관만 표시한다.[^members]

| 이름 | 학위·과정 (연도) | 랩이 적은 진로 |
|---|---|---|
| 이승법 (Seung Beop Lee) | 박사 (2018) | 전북대학교 |
| 김정진 (Jung Jin Kim) | 박사 (2019) | 계명대학교 |
| 김종호 (Jong Ho Kim) | 박사 (2021) | 대학 (계명대학교) 조교수 |
| 이창우 (Changwoo Lee) | 박사 (2022) | 대학 (아주대학교) 조교수 |
| 천봉주 (Bongju Chun) | 박사 (2022) | 국방과학연구소 |
| 김근우 (Geunu Kim) | 박사 (2023) | 국립부경대학교 |
| 김민기 (Mingi Kim) | 박사 (2023) | 삼성전자 |
| 김헌재 (Heon Jae Kim) | 석사 (2013) | 기업 (현대자동차) 연구원 |
| 김유경 (You Kyung Kim) | 석사 (2014) | 기업 (현대자동차) 연구원 |
| 김진수 (Jinsu Kim) | 석사 (2015) | 기업 (메리츠화재) 연구원 |
| 남지민 (Jimin Nam) | 석사 (2018) | 연구소 (국방과학연구소) 연구원 |
| 노수성 (Su Seong Noh) | 석사 (2020) | 기업 (삼성전자) 연구원 |
| 신상민 (Sangmin Sin) | 석사 (2020) | 기업 (포티투닷) 연구원 |
| 이태양 (Taeyang Lee) | 석사 (2020) | 기업 (컬리) 연구원 |
| 진현우 (Hyunwoo Jin) | 석사 (2021) | 기업 (현대자동차) 연구원 |
| 강민석 (Minseok Kang) | 석사 (2022) | KAIST |
| 고혁진 (Hyukjin Koh) | 석사 (2022) | 대학 (KAIST) 박사과정 |
| 김성용 (Sungyong Kim) | 석사 (2023) | LG전자 |
| 김정훈 (Jeonghun Kim) | 석사 (2025) | KAIST |
| 조원영 (Wonyeong Jo) | 석사 (2025) | 한화에어로스페이스 |
| 김창영 (Changyeong Kim) | 석사 (2025) | KAIST |
| 박상훈 (Sanghoon Park) | 석사 (2026) | 대학 (KAIST) 박사과정 |
| 권순열 (Sunyeol Gwon) | 석사 (2026) | 대학 (KAIST) 박사과정 |
| 이환규 (Hwankyu Lee) | 석사 (2026) | 한국철도공사 |

## 최근 논문 목록 (2021–2026)

무선전력전송과 전동기 설계, 차량·철도 경로 계산, 구조 최적화와 구동 장치 제어, 뼈의 역학 계산·측정 방법을 다룬 논문·학회 발표다. 연구실 논문 자료의 2021–2026년 구역에서 38편(국제 학술지 27편, 국제 학회 9편, 국내 학술지 2편), 학생 프로필에서 중복을 정리한 25편, 총 63편을 싣는다. 연도와 저자 순서는 각 목록 표기다. 학회 항목은 발표·학생 설계 경진대회 표기를 포함한다. 같은 제목이라도 발표 학회나 연도가 다르면 별도 항목이다.[^pubs][^members] 골격계 관련 학술지 논문은 대표 하중 계산과 파동을 이용한 역학적 특성 추정·결함 평가 방법의 개발을 다룬다.[^p6][^p7][^p8][^bio-defect][^bio-modulus]

**2026**

- C. Kim, G. Kim, I. G. Jang. "Linearized Loopwise Route Representation for Solving Symmetric Traveling Salesman Problems without the Origin-Destination Matrix". *IEEE Transactions on Intelligent Transportation Systems*.
- M. Kim, M. Kang, C. Chu, Y. Lee, S. Gwon, I. G. Jang. "Fault Detection of Coil Misalignment in Multi-receiver Wireless Power Transfer Systems with the Estimated Mutual Inductance". *IEEE Transactions on Industrial Electronics, 2026*.
- T. Oh, E. M. Kim, T. -T. Nguyen, H. Jeong, Y. Choi, L. Liebe, S. Lee, H. Jang, G. Chun, I. Kim, K. Jang, H. Ahn, D. Kum, I. G. Jang, D. Lee. "Scalable and interoperable C-V2X framework for real-time intelligent decision support in autonomous mobility". *Communications in Transportation Research, 2026*.
- M. Barakat, S. Yoon, T. -Y. Kim, I. G. Jang, R. Song, A. Schiffer. "Interaction of highly nonlinear solitary waves with 3D-printed artificial bone". *Mechanics of Advanced Materials and Structures, 2026*.
- J. Kim, I. G. Jang. "Topology optimization-based path planning for complex maze networks". *ACSMO, 2026*.
- 김정훈, 장인권. "복잡한 미로 네트워크를 위한 딥러닝 기반 경로 계획". *대한기계학회 CAE 및 응용역학부분 춘계학술대회, 2026*.
- C. Kim and I. G. Jang. "Linearization of Topology Optimization for Traveling Salesman Problem". *Asian Congress of Structural and Multidisciplinary Optimization (ACSMO), 2026*.
- 김창영, 장인권. "위상최적설계 기반 차량 경로 최적화에 대한 선형 정식화". *대한기계학회 CAE 및 응용역학부문 춘계학술대회, 2026*.
- S. Park, I. G. Jang. "Global Optimality in the Linearized Loopwise Route Reperesentation-based Topology Optimization". *Asian Congress of Structural and Multidisciplinary Optimization (ACSMO), 2026*.
- 박상훈, 장인권. "선형화된 루프 경로 표현법 기반 위상최적화에서의 전역 최적성". *대한기계학회 CAE 및 응용역학부문 춘계학술대회, 2026*.

**2025**

- G. Kim, C. Kim, S. Park, J. Kim, I. G. Jang. "Linear Programming of the Loopwise Route Representation for the Shortest Path Problems by Introducing the Reference Link Flow". *IEEE Access, vol. 13, pp. 38856-38864, 2025*.
- M. Kang, S. Gwon, and I. G. Jang. "Stable and practical operation for multi-receiver wireless power transfer systems by estimating mutual inductance estimation". *Wireless Power Technology Conference and Expo (WPTCE, Student design competition) , 2025*.
- M. Kang, S. Gwon, and I. G. Jang. "Determination of the Optimal Load Condition for Multi-receiver Wireless Power Transfer Systems". *World Congress of Structural and Multidisciplinary Optimization (WCSMO), 2025*.
- J. Kim, G. Kim, C. Kim, I. G. Jang. "Deep Learning-based Topology Optimization for Shortest Path Problems". *World Congress of Structural and Multidisciplinary Optimization (WCSMO), 2025*.
- 김정훈, 장인권. "복잡한 미로 네트워크를 위한 딥러닝 기반 경로 계획". *한국ITS학회 추계학술대회, 2025*.
- 김창영, 장인권. "위상최적설계 기반 차량 경로 최적화에 대한 선형 정식화". *대한기계학회 CAE 및 응용역학부문 춘계학술대회 학생경진대회, 2025*.
- S. Park, G. Kim, I. G. Jang. "Post-processing of the loop-wise route representation-based topology optimization for shortest path problems". *World Congress of Structural and Multidisciplinary Optimization (WCSMO), 2025*.
- 박상훈, 김근우, 장인권. "루프표현법과 위상최적설계에 기반한 후처리 방안: 최단 경로 문제 사례". *대한기계학회 CAE 및 응용역학부문 춘계학술대회 학생경진대회, 2025*.
- 박상훈, 장인권. "선형화된 루프 경로 표현법을 이용한 외판원 문제의 2단계 프레임워크". *한국 ITS 학회 추계학술대회, 2025*.

**2024**

- G. Kim, I. G. Jang. "Loopwise Route Representation-based Topology Optimization for Vehicle Routing Problem". *ACSMO 2024*.
- J. Kim, G. Kim, I. G. Jang. "Deep Learning-based Topology Optimization for Shortest Path Problems". *ACSMO 2024*.
- M. Kang, M. Kim, I. G. Jang. "Study on Estimating the Full Mutual Inductance Information in Multi-Receiver Wireless Power Transfer Systems". *IEEE WPTCE 2024*.
- 김정훈, 심지섭, 장인권, 김근우. "전기차 경로 문제를 대상으로 한 루프 방식 경로 표현법의 실도로 네트워크 적용". *대한기계학회논문집 A, 48(11), pp. 749-756 2024*.
- 김정훈, 김근우, 장인권. "딥러닝을 활용한 위상 최적화 가속화: 최단경로 문제 사례". *대한기계학회 CAE 및 응용역학부문 춘계학술대회 학생경진대회, 2024*.
- 김정훈, 김근우, 장인권. "최단 경로 문제를 위한 딥러닝 기반 위상 최적화". *대한기계학회 학술대회, 2024*.
- 김창영, 김근우, 장인권. "루프 표현법과 위상최적설계에 기반한 차량 경로 최적화에 대한 선형화 방안". *대한기계학회 CAE 및 응용역학부문 춘계학술대회 학생경진대회, 2024*.
- 김창영, 김근우, 장인권. "루프 기반 경로 최적화의 계산 가속화를 위한 선형화 방법". *한국ITS학회 추계학술대회, 2024*.
- 박상훈, 김근우, 장인권. "전기회로와 도로교통 간의 유사성을 활용한 루프 기반 최단 경로 탐색법의 후처리 방안". *한국 ITS 학회 추계학술대회, 2024*.

**2023**

- C. Lee, I. G. Jang. "Computationally Efficient Topology Optimization for the SynRMs Based on the Torque Curve Interpolation". *Structural and Multidisciplinary Optimization, vol. 66, no. 172, 2023*.
- G. Kim, H. Jin, M. Kim, K. Jang, I. G. Jang. "Loop-wise Route Representation and Its Optimization Formulation for Symmetric Traveling Salesman Problems". *IEEE Transactions on Intelligent Transportation Systems, vol.24, no. 9, pp. 9490-9500, 2023*.
- C. Lee, I. G. Jang. "Topology Optimization of Synchronous Reluctance Motors Considering the Optimal Current Reference in the Field-weakening and Maximum-torque-per-voltage Regions". *IEEE Transactions on Energy Conversion, vol. 38, no. 3, pp. 1950-1961, 2023*.
- C. Lee, I. G. Jang. "Topology Optimization of the IPMSMs Considering both the MTPA and FW Controls under the Voltage and Current Limitations". *IEEE Transactions on Industrial Electronics, vol. 70, no. 8, pp. 8244-8253, 2023*.
- S. Yoon, A. Schiffer, I. G. Jang, S. Lee, C. Y. Yeun, T. -Y. Kim. "Detection of defects in cellular solids using highly nonlinear solitary waves: a numerical study of the proximal femur". *Biomechanics and Modeling in Mechanobiology, vol. 22, pp. 561-574, 2023*.
- C. Lee, I. G. Jang. "Topology Optimization Framework for Simultaneously Determining the Optimal Structural Design and Current Phase Angle of the IPMSMs for the MTPA Control". *IEEE Transactions on Industrial Electronics, vol. 70, no. 3, pp. 2866-2875, 2023*.
- C. Lee, J. Lee, I. G. Jang. "Topology Optimization for the Manufacturable and Structurally Safe Synchronous Reluctance Motors with Multiple Iron Webs and Bridges". *IEEE Transactions on Industrial Electronics, vol. 70, no. 1, pp. 678-687, 2023*.
- M. Kim, M. Kang, I. G. Jang. "Estimation of the Mutual Inductance in Multi-receiver Wireless Power Transfer Systems". *IEEE WPTCE 2023*.
- S. Kim, G. Kim, I. G. Jang. "Topology Optimization for Vehicle Routing Problems". *WCSMO 2023*.
- 강민석, 김민기, 조원영, 장인권. "무선 충전을 위한 상호 인덕턴스 추정". *한국ITS학회 2023년 추계학술대회, 2023*.
- 고혁진, 김창영, 장인권. "데이터 기반 SKIP-STOP 도시 철도 급행 서비스 최적화: 서울 지하철 4호선의 사례". *한국ITS학회 추계학술대회, 2023*.
- 김정훈, 김근우, 장인권. "딥러닝을 활용한 루프 기반 최단 경로 탐색 방법". *한국ITS학회 추계학술대회, 2023*.
- 김성용, 김정훈, 김근우, 장인권. "대중교통 승객 맞춤형 경로 추천을 위한 루프 기반 경로 최적화: 수도권 전철 적용 사례". *한국 ITS 학회 추계학술대회, 2023*.

**2022**

- G. Kim, S. Kim, I. G. Jang. "Loopwise Route Representation-Based Topology Optimization for the Shortest Path Problems". *IEEE Access, vol. 10, pp. 128835-128846, 2022*.
- D. Kim, Y. Ji, J. Lee, J. Yoo, S. Min, I. G. Jang. "A MATLAB code of node-based topology optimization in 3D arbitrary domain for additive manufacturing". *Structural and Multidisciplinary Optimization, vol. 65, no. 311, 2022*.
- C. Lee, I. G. Jang. "Multi-material Topology Optimization for the PMSMs under the Consideration of the MTPA Control". *Structural and Multidisciplinary Optimization, vol. 65, no. 9, pp. 1-11, 2022*.
- B. J. Chun, I. G. Jang. "Framework of sampling the subject-specific static loads from the gait cycle of interindividual variation". *Computer Methods and Programs in Biomedicine, vol. 225, 2022*.
- J. Kim, J.J. Kim, I. G. Jang. "Integrated topology and shape optimization of the five-spoke steel wheel to improve the natural frequency". *Structural and Multidisciplinary Optimization, vol. 65, no. 78, 2022*.
- K. Choi, J. Byun, S. Lee, I. G. Jang. "Adaptive Equivalent Consumption Minimization Strategy (A-ECMS) for the HEVs With a Near-Optimal Equivalent Factor Considering Driving Conditions". *IEEE Transactions on Vehicular Technology, vol. 71, no. 3, pp. 2538-2549, 2022*.
- M. Kim, I. G. Jang. "Mutual Inductance Estimation for Multi-receiver Wireless Power Systems Using Current Information". *IEEE WPTC 2022*.
- M. Kim, I. G. Jang. "Analytical Investigation of Approximating the Optimal Operating Condition of Multi-receiver Wireless Power Transfer Systems in Real Time". *ACSMO 2022*.
- M. Kang, I. G. Jang. "Determination of the Optimal Load Condition for Multi-receiver Wireless Power Transfer Systems". *ACSMO 2022*.
- C. W. Lee, I. G. Jang. "Two-stage Topology Optimization Framework of a Rare-earth-free Synchronous Reluctance Motor Considering Manufacturability and Structural Safety". *ACSMO 2022*.
- 김종호, 장인권. "최적화에 기반한 분산 구동 메커니즘의 생체 모방 가변 기어링". *대한기계학회 논문집 A, 46(8), pp. 695-701, 2022*.
- 강민석, 김민기, 장인권. "다중수신 무선전력전송 시스템을 위한 최적 부하 조건 결정". *대한기계학회 학술대회, 2022*.

**2021**

- J. H. Kim, K. Choi, I. G. Jang. "Model-Predictive-Control-Based Time-Optimal Trajectory Planning of the Distributed Actuation Mechanism Augmented by the Maximum Performance Evaluation". *Applied Science, vol. 11, no. 16, pp. 7513-1-12, 2021*.
- Y. Joo, Y. Yu, I.G. Jang. "Unit module-based convergence acceleration for topology optimization using the spatiotemporal deep neural network". *IEEE Access, vol. 9, pp. 149766-149779, 2021*.
- C. Lee, I. G. Jang. "Topology optimization of multiple-barrier synchronous reluctance motors with initial random hollow circles". *Structural and Multidisciplinary Optimization, vol. 64, pp. 2213-2224, 2021*.
- J. H. Kim, Y. J. Shin, I. G. Jang. "Evaluating the Maximum Directional Kinematic Capability of a Redundant Manipulator Based on Allowable Velocity and Force". *IEEE Access, vol. 9, pp. 88085-88097, 2021*.
- S. Yoon, A. Schiffer, I. G. Jang, S. Lee, T. -Y. Kim. "Predictions of the elastic modulus of trabecular bone in the femoral head and the intertrochanter: a solitary wave-based approach". *Biomechanics and Modeling in Mechanobiology, vol. 20, pp.1733–1749, 2021*.
- C. Lee, J. Lee, I. G. Jang. "Shape optimization-based design investigation of the switched reluctance motors regarding the target torque and current limitation". *Structural and Multidisciplinary Optimization, vol. 64, pp. 859-870, 2021*.
- B. J. Chun, I. G. Jang. "Determination of the representative static loads for cyclically repeated dynamic loads: a case study of bone remodeling simulation with gait loads". *Computer Methods and Programs in Biomedicine, vol. 200, 2021*.
- J. Yoo, I. G. Jang, I. Lee. "Multi-resolution topology optimization using adaptive isosurface variable grouping (MTOP-aIVG) for enhanced computational efficiency". *Structural and Multidisciplinary Optimization, vol. 63, no. 4, pp. 1743-1766, 2021*.
- S. B. Lee, M. Kim, I. G. Jang. "Determination of the Optimal Resonant Condition for Multi-receiver Wireless Power Transfer Systems Considering the Transfer Efficiency and Different Rated Powers with Altered Coupling Effects". *IEEE Journal of Emerging and Selected Topics in Power Electronics, vol. 9, no. 2, pp.2384-2393, 2021*.
- 강민석, 김민기, 장인권. "다중수신 무선전력전송 시스템의 전송효율 및 정격용량을 고려한 수신기의 DC/DC 컨버터의 최적 듀티비 결정". *한국전자파학회, 2021*.

## 과제와 연구비

과제 자료의 30건 가운데 2021년 10월–2026년 10월과 수행 기간이 겹치는 9건과, 날짜가 있는 소식의 연구비 선정 3건이다. 진행·완료 구분과 연도 단위 기간은 게시 표기를 따른다. 골격계 영상 고해상화 과제는 과제 자료가 2026–2030년, 2026년 3월 23일 선정 소식이 2026–2029년으로 적는다. 해당 소식은 위상최적설계와 확산 모델(자료에 잡음을 더하고 제거하는 과정을 학습해 자료를 생성하는 모형)을 결합한 영상 재구성 방법 개발을 목표로 설명한다.[^projects][^notices] 대표 정적 하중을 이용한 골강도 예측 과제의 방법은 연구 소개에서 뼈의 구조 변화 계산 방법으로 설명한다.[^research]

- 생성AI 선도 인재 양성 사업 (IITP) (기간 2026 ~ 2029; 상태 진행 중)
- 위상최적설계 기반의 확산 모델을 활용한 대규모 3차원 골격계 영상 고해상화 방법 개발 (NRF) (기간 2026 ~ 2030; 상태 진행 중)
- AI 기반 지능형 설계-제조 통합 연구단 (InnoCORE) (기간 2025 ~ 2029; 상태 진행 중)
- 자율주행 Lv.4/4+ 기반 도시환경관리 서비스 기술 개발 (KAIA) (기간 2023 ~ 2027; 상태 진행 중)
- 국토교통 DNA플러스 도로교통분야 융합기술대학원 (KAIA) (기간 2022 ~ 2027; 상태 진행 중)
- 대표 정적 하중 기반의 위상최적설계를 활용한 개인 맞춤형 골강도 변화 예측 방법론 개발 (NRF) (기간 2021 ~ 2024; 상태 완료)
- 로봇향 3.3kW급 군집 무선충전 핵심기술 개발 (IITP) (기간 2022 ~ 2025; 상태 완료)
- 클라우드 엣지 기반 도시교통 브레인 핵심기술 개발 (IITP) (기간 2020 ~ 2023; 상태 완료)
- 저탄소 청정 제주(CFI Jeju)를 위한 냉장 전기차량 기반 신선물류 배송체계 구축 기술 개발 (KAIA) (기간 2022 ~ 2023; 상태 완료)
- 2026.09.01 · 3차원 네트워크에서의 다중 경로 최적화 방법 개발 (역할 연구책임자 김정훈; 지원 한국연구재단; 사업 박사과정생연구장려금지원; 기간 총 2년; 연구비 5천만 원)
- 2025.09.01 · 수신기 간의 간섭을 고려한 상호 인덕턴스 추정 기반의 안정적인 다중 수신 무선충전 기술 개발 (역할 연구책임자 강민석; 지원 한국연구재단; 사업 박사과정생연구장려금지원; 기간 총 2년; 연구비 5천만 원)
- 2023.02.18 · 전기모터의 희토류 저감 및 출력밀도 최대화를 위한 제어전략 연계형 위상최적설계 방법론 개발 (역할 연구책임자 이창우; 지원 한국연구재단; 사업 세종과학펠로우십; 기간 총 5년; 연구비 6.5억 원 내외)

## 특허

연구 소개와 학생 프로필이 게시한 출원·등록 가운데 장인권 교수가 발명자로 적혀 있고 2022–2025년으로 표시된 무선전력전송·경로 계산 11건이다. 국가와 번호가 같은 항목은 하나로 셌다. 제목과 출원·등록 구분은 게시 표기이며 연도만 있는 항목의 월·일은 정하지 않는다.[^research][^members]

- Real-time approximation method and apparatus of mutual inductance between transmitters and receivers for determining optimal operating condition in multiple-receiver wireless power transfer systems (연도 2024; 번호 10-2694022; 상태 등록; 국가 KR)
- Real-time approximation method and apparatus of mutual inductance between transmitters and receivers for determining optimal operating condition in multiple-receiver wireless power transfer systems (연도 2025; 번호 12,301,015 B2; 상태 등록; 국가 US)
- Two-stage method for sequential estimation of all mutual inductance between coils in multi-receiver wireless power transfer systems and device for operating the same (연도 2025; 번호 10-2025-0132299; 상태 출원; 국가 KR)
- Optimal path calculation system and method based on loop variables with post processing applied (연도 2023; 번호 10-2023-0157983; 상태 출원; 국가 KR)
- LEAST COST PATH SELECTION SYSTEM AND METHOD (연도 2024; 번호 10-2024-0144119; 상태 출원; 국가 KR)
- SYSTEM AND METHOD FOR COMPUTING OPTIMAL PATH BASED ON LOOP VARIABLES WITH POST-PROCESSING APPLIED (연도 2024; 번호 18/775,172; 상태 출원; 국가 US)
- LEAST COST PATH SELECTION SYSTEM AND METHOD (연도 2025; 번호 19/080,596; 상태 출원; 국가 US)
- Loop-wise route representation method for vehicle routing problem and the corresponding optimization formulation (연도 2022; 번호 10-2022-0071371; 상태 출원; 국가 KR)
- Loop-wise route representation method for vehicle routing problem and the corresponding optimization formulation (연도 2023; 번호 PCT/KR2023/000080; 상태 국제출원(PCT))
- LOOP-WISE ROUTE REPRESENTATION METHOD FOR VEHICLE ROUTING PROBLEM AND THE CORRESPONDING OPTIMIZATION FORMULATION (연도 2023; 번호 18/150,267; 상태 출원; 국가 US)
- LOOP-WISE ROUTE REPRESENTATION METHOD FOR VEHICLE ROUTING PROBLEM AND THE CORRESPONDING OPTIMIZATION FORMULATION (연도 2023; 번호 23150607.2; 상태 출원; 국가 EP)

## 수상

2021년 10월 13일–2026년 10월 13일의 소식 23건과 학생 프로필에만 있는 2024·2025년 수상 2건이다. 날짜는 소식 게시일이며 제목 안의 수상 연도와 다를 수 있다. 프로필만 근거인 2건은 원문에 적힌 연도만 표시한다.[^notices][^members]

- 2026.05.11 · 2026년 대한기계학회, 우수학위논문상, 김창영
- 2025.12.11 · 2024년 대한기계학회, 우수논문상, 김정훈
- 2025.10.31 · 2025년 한국ITS학회, 우수논문상, 김정훈
- 2025.10.24 · 2025년 한국이공학진흥원, 차세대 공학연구자 우수상, 고혁진
- 2025.04.17 · 2025년 대한기계학회, 우수논문상, 김정훈
- 2025.01.31 · 2025년 대한교통학회, 회장상, 김정훈
- 2025.01.15 · 2025년 한국최적설계학회, 피도텍 유망연구자상, 장인권 교수님
- 2024.10.25 · 2024년 한국ITS 학회, 우수논문상, 박상훈
- 2024.05.22 · 2024년 ACSMO 학회, Young Scientist Award, 김근우
- 2024.05.03 · 2024년 대한기계학회 학생경진대회, 장려상, 김창영
- 2024.04.19 · 2024년 조천식모빌리티대학원, 학업우수상, 김정훈
- 2024.01.17 · 2024년 한국최적설계학회, 우수학위논문상, 김근우
- 2023.11.17 · 2023년 한국ITS학회, 우수논문상, 김정훈
- 2023.05.23 · 2023년 대한기계학회, 우수논문상, 천봉주
- 2023.05.23 · 2023년 대한기계학회, 우수논문상, 고혁진
- 2023.04.07 · 2023년 대한기계학회, 우수학위논문상, 천봉주
- 2023.03.08 · 2023년 대한기계학회, 우수논문상, 이창우
- 2022.06.17 · ACSMO 2022, Young Scientist Award, 이창우
- 2022.06.17 · KAIST 조천식모빌리티대학원, 최우수연구상, 이창우
- 2022.05.23 · 2022년 대한기계학회, 학생경진대회 대상, 고혁진
- 2022.05.23 · 2022년 대한기계학회, 학생경진대회 동상, 김성용
- 2022.05.16 · 2022년 대한기계학회, 우수논문상, 김종호
- 2022.01.13 · KAIST AI Platform Center for Manufacturing, 우수상, 이창우
- 고혁진, 우수조교상, KAIST, 2024.
- 김정훈, 대한기계학회 논문상-우수논문(대한기계학회논문집A), 대한기계학회, 2025.

## 소식

2021년 10월 13일–2026년 10월 13일의 연구비 선정, 해외특허 출원 지원 선정, 기술성과 전시회 선정과 학술행사 안내 12건이다. 날짜는 게시일이며, 해외특허 출원 지원 선정은 특허 등록을 뜻하지 않는다.[^notices]

- 2026.09.01 · 2026년 이공분야 학술연구지원사업(박사과정생연구장려금지원) 선정, 김정훈
- 2026.04.22 · 생성 AI 선도인재양성 사업 과제 선정
- 2026.03.23 · 한국연구재단(NRF) 핵심연구과제 선정
- 2025.09.01 · 2025년 이공분야 학술연구지원사업(박사과정생연구장려금지원) 선정, 강민석
- 2023.03.08 · 2023년 1차 해외특허 출원 지원 대상 선정: 단위 전류당 최대토크 제어성능 및 약계자 제어성능을 고려한 영구자석 삽입형 전기 모터의 위상최적설계 방법 및 장치
- 2023.02.18 · 2023년 한국연구재단 세종과학펠로우십 선정, 이창우
- 2022.11.22 · 2022년 4차 해외특허 출원 지원 대상 선정: 임상 CT 스캔 데이터에서의 심층 학습 기반 패치별 3차원 골 미세구조 재구성 방법 및 장치
- 2022.09.23 · Tech-Biz Korea 2022 기술성과 전시회에서 「올해의 신기술」로 선정되었다.
- 2022.09.01 · 2022년 3차 해외특허 출원 지원 대상 선정: 차량경로문제를 위한 루프 방식의 경로표현법 및 최적화
- 2022.03.02 · 2022년 1차 해외특허 해외특허 출원 지원 대상 선정: 다중 수신 무선전력전송의 최적 동작 상태 결정을 위한 송수신 간의 상호 인덕턴스 실시간 추정 방법 및 장치
- 2021.12.02 · GIST Mini Symposium on AI for ME 안내(행사 표기 2021년 12월 9–10일).
- 2021.12.02 · 2021년 4차 해외특허 출원 지원 대상 선정: 노드-링크 그래프 기반 골 미세구조 표현을 활용한 인공신경망으로 재구성된 골격계 영상의 골 미세구조 연결성 복구를 위한 컴퓨터 장치 및 그의 방법; 하이브리드 차량의 과도특성을 고려한 동력제어 방법 및 장치

## 연락과 위치

- 연구실: 대전광역시 유성구 문지로 193 KAIST 문지캠퍼스 F317[^common]
- 교수 사무실: F404[^department]
- 교수 이메일: igjang@kaist.edu[^members]
- 교수 전화: +82-42-350-1262[^members]
[^home]: 연구실 누리집 첫 화면 자료(home.json), <https://idlab.kaist.ac.kr/data/home.json> (관측일 2026-10-26).
[^common]: 연구실 누리집 공통 안내 자료(common.json), <https://idlab.kaist.ac.kr/data/common.json> (관측일 2026-10-26).
[^members]: 연구실 누리집 구성원 자료(members.json), <https://idlab.kaist.ac.kr/data/members.json> (관측일 2026-10-26).
[^research]: 연구실 누리집 연구 소개 자료(research.json), <https://idlab.kaist.ac.kr/data/research.json> (관측일 2026-10-26).
[^projects]: 연구실 누리집 과제 자료(projects.json), <https://idlab.kaist.ac.kr/data/projects.json> (관측일 2026-10-26).
[^pubs]: 연구실 누리집 논문 자료(publications.json), <https://idlab.kaist.ac.kr/data/publications.json> (관측일 2026-10-26).
[^notices]: 연구실 누리집 소식 자료(notices.json), <https://idlab.kaist.ac.kr/data/notices.json> (관측일 2026-10-26).
[^department]: KAIST 조천식모빌리티대학원 교수 명단, <https://mo.kaist.ac.kr/professor/> (관측일 2026-10-27).
[^p1]: M. Kim 외, I. G. Jang, IEEE Transactions on Industrial Electronics 73, 12967-12979 (2026). <https://doi.org/10.1109/TIE.2026.3675172> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1109/TIE.2026.3675172>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p2]: S. B. Lee, M. Kim, I. G. Jang, IEEE Journal of Emerging and Selected Topics in Power Electronics 9, 2384-2393 (2021). <https://doi.org/10.1109/JESTPE.2020.2983824> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1109/JESTPE.2020.2983824>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p3]: G. Kim 외, I. G. Jang, IEEE Access 13, 38856-38864 (2025). <https://doi.org/10.1109/ACCESS.2025.3546320> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1109/ACCESS.2025.3546320>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p4]: G. Kim 외, I. G. Jang, IEEE Transactions on Intelligent Transportation Systems 24, 9490-9500 (2023). <https://doi.org/10.1109/TITS.2023.3271313> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1109/TITS.2023.3271313>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p5]: G. Kim, S. Kim, I. G. Jang, IEEE Access 10, 128835-128846 (2022). <https://doi.org/10.1109/ACCESS.2022.3227388> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1109/ACCESS.2022.3227388>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p6]: B. J. Chun, I. G. Jang, Computer Methods and Programs in Biomedicine 225, 107054 (2022). <https://doi.org/10.1016/j.cmpb.2022.107054> 초록 기준(Europe PMC 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1016/j.cmpb.2022.107054>. 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.cmpb.2022.107054%22> (관측일 2026-10-27).
[^p7]: M. Barakat 외, A. Schiffer, Mechanics of Advanced Materials and Structures 33, 2601267 (온라인 2026-01-21). <https://doi.org/10.1080/15376494.2025.2601267> 초록 기준(OpenAlex 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1080/15376494.2025.2601267>. 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1007/s10237-021-01473-1|10.1007/s10237-022-01662-6|10.1016/j.cmpb.2020.105924|10.1016/j.cmpb.2022.107054|10.1016/j.eswa.2024.126299|10.1016/j.ijnonlinmec.2023.104458|10.1016/j.irbm.2025.100889|10.1080/15376494.2025.2601267|10.1109/access.2022.3227388|10.1109/access.2025.3546320|10.1109/jestpe.2020.2983824|10.1109/tie.2026.3675172|10.1109/tits.2023.3271313> (관측일 2026-10-27).
[^p8]: B. J. Chun, I. G. Jang, Computer Methods and Programs in Biomedicine 200, 105924 (2021). <https://doi.org/10.1016/j.cmpb.2020.105924> 초록 기준(Europe PMC 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1016/j.cmpb.2020.105924>. 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.cmpb.2020.105924%22> (관측일 2026-10-27).
[^bio-defect]: Detection of defects in cellular solids using highly nonlinear solitary waves: a numerical study of the proximal femur, Biomechanics and Modeling in Mechanobiology 22, 561-574. <https://doi.org/10.1007/s10237-022-01662-6> 초록 기준(Europe PMC 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1007/s10237-022-01662-6>. 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/s10237-022-01662-6%22> (관측일 2026-10-27).
[^bio-modulus]: Predictions of the elastic modulus of trabecular bone in the femoral head and the intertrochanter: a solitary wave-based approach, Biomechanics and Modeling in Mechanobiology 20, 1733-1749. <https://doi.org/10.1007/s10237-021-01473-1> 초록 기준(Europe PMC 등록 초록). 서지 원문 <https://api.crossref.org/works/10.1007/s10237-021-01473-1>. 초록 원문 <https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/s10237-021-01473-1%22> (관측일 2026-10-27).

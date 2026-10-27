# 자동차 지능 및 전동화 연구실 (Automotive Intelligence X Electrification Lab, AXE Lab)

**KAIST 조천식모빌리티대학원·로봇공학학제전공·김재철AI대학원·AX학과·기계공학과·미래자동차학제전공 · 금동석 부교수**

- 분야: 자율주행 인지·지도·경로 계획, 전동화 동력계 설계와 제어, 차량 열관리와 에너지 관리, 이동 로봇
- 대분야: 기계·로봇·제조, 컴퓨팅·AI
- 태그: 자율주행[^av], 전기차[^ep], 컴퓨터 비전[^av][^deptresearch], 강화학습[^deptresearch], 로봇 항법·SLAM[^robots]
- 홈페이지: <https://axelab.kaist.ac.kr/>
- 근거와 출처: [AXE Lab 근거 페이지](axelab-sources.md)

> 자동차가 주변을 인식하고 갈 길을 정하는 기술과, 전기·하이브리드 자동차의 동력·열·에너지를 관리하는 기술을 함께 연구한다.[^av][^ep]

## 무엇을 연구하나

금동석 부교수가 이끄는 AXE Lab은 자동차의 지능화와 전동화를 함께 다룬다. 자율주행 쪽에서는 주변 물체를 알아보는 인지, 다른 차량의 움직임 예측, 차량의 행동과 경로를 결정하는 방법을 연구한다. 전동화 쪽에서는 파워트레인(에너지원에서 바퀴까지 동력을 만들어 전달하는 장치 체계)의 구조와 제어를 다룬다. 조천식모빌리티대학원은 교수를 지능형 모빌리티와 친환경 모빌리티 기술 분야의 전임교수로 소개한다.[^faculty][^deptprof][^av][^ep]

전동화 팀은 배터리 전기차, 하이브리드 전기차(엔진과 전기 모터를 함께 구동원으로 쓰는 차량), 연료전지 전기차(연료와 산소의 전기화학 반응으로 얻은 전기를 사용하는 차량)를 대상으로 한다. 차량 내부의 온도를 다루는 열관리 시스템, 엔진과 배터리 사이의 에너지 사용 배분, 동력 전달 구조, 운전 모드가 바뀌는 과정의 제어가 연구 주제다. 여러 동력원을 오래 안전하게 사용하는 방법을 찾으며, 설계 소개에서는 구조 선택부터 부품의 연결·배치, 실제 제어 장치를 포함한 모의실험까지 이어지는 설계 절차를 설명한다.[^ep][^design]

자율주행 팀은 카메라와 레이다(전파를 이용해 물체의 거리와 움직임 등을 측정하는 장치) 등의 자료를 해석하는 알고리즘부터 학습용 자료 관리와 실제 차량 검증까지 다룬다. 센서 융합(여러 센서의 관측 자료를 결합해 정보를 얻는 방법)으로 주변을 인식하고, 고정밀 지도를 만드는 연구도 한다. 엔드투엔드 자율주행은 센서 입력에서 차량의 주행 결정을 내는 과정까지 연결해 학습하는 접근이다. 이를 위해 자료를 수집·가공·전달하는 데이터 파이프라인, 학습용 정답을 자동으로 붙이는 자동 라벨링, 장면을 모의로 만드는 신경망 시뮬레이터를 연구한다. 신경망은 입력과 출력의 관계를 연결된 계산 단위로 표현해 학습하는 모형이다. 사전 학습은 본래 풀려는 과제에 맞춰 학습하기 전에 다른 자료나 과제로 모형을 미리 학습하는 과정이다.[^av]

연구 소개의 Archive에는 복합 재생에너지 시스템과 이동 로봇도 올라 있다. 복합 재생에너지 시스템에서는 태양광·풍력·배터리·디젤 발전기의 크기와 에너지 배분 전략을 함께 비교한다. 이동 로봇에서는 재난 현장을 탐색하는 지상·공중 이동 로봇과 도심 배송 로봇을 소개한다. 로봇이 자신의 위치를 추정하면서 주변 지도도 만드는 SLAM(Simultaneous Localization and Mapping)을 적용하는 것이 이 갈래의 주제다. 재난 로봇 소개는 공중 이동과 지상 이동 사이를 되돌려 전환하는 구조의 개발을 진행하고 있다고 설명한다.[^energy][^robots]

## 주요 연구 주제

### 1. 전동화 동력계의 구조·에너지·열관리

엔진과 모터를 어떻게 연결할지, 각 동력원을 언제 사용할지, 차량 내부의 열을 어떻게 관리할지를 다룬다. 설계 소개는 동력분기 하이브리드(엔진 동력을 기계 경로와 전기 경로로 나누는 구동 방식)의 연결 구조를 탐색하고, 부품 배치로 바꾼 뒤 검증하는 절차를 제시한다. 에너지 관리에서는 남은 주행 거리와 배터리 충전 상태를 함께 고려하며, 엔진 시동 과정의 승차감과 소요 시간도 연구한다. 최적 제어는 주어진 모형과 제약 아래에서 정한 목표를 가장 잘 달성하는 제어 입력을 찾는 방법이다.[^design][^ep]

대표 논문은 하이브리드 차량의 연결 구조를 가상 설계 공간에서 찾고 실제 구조로 바꾸는 방법과, 시동 모터의 구성이 다른 차량을 같은 기준으로 비교하는 방법을 다룬다. 전자는 연비와 가속 성능을 함께 평가하며, 후자는 시동 시간과 운전자가 요구한 동력의 부족을 함께 평가한다.[^p1][^p2]

### 2. 자율주행을 위한 공간 인지와 지도

서로 다른 센서가 얻은 공간 정보를 합쳐 주변 물체를 찾고, 차량이 어디에 있는지 알아보거나 지도를 만드는 연구다. 카메라 영상과 레이다 자료를 결합하고, 지도 요소의 형상을 점과 연결 관계로 표현한다. 대표 논문의 CRAB(Camera-Radar fusion for reducing depth Ambiguity in Backward projection-based view transformation)는 영상에서 생기는 거리 판단의 모호성을 레이다 정보로 줄이는 방법이며, InstaGraM은 고정밀 지도의 요소를 그래프(대상을 점으로, 대상 사이의 관계를 연결선으로 나타낸 표현)로 학습하는 방법이다.[^av][^p5][^p7]

### 3. 학습 자료와 표현, 판단·경로 계획

새로운 주행 자료를 모으고 학습시키는 과정과, 그 결과로 차량의 행동을 정하는 과정을 함께 연구한다. 강화학습(행동에 따른 보상을 기준으로 행동 방식을 배우는 기계학습 방법)을 이용한 경로 생성과 충돌 회피를 다루며, 누리집은 인지·계획 알고리즘을 실제 차량에 넣어 검증하는 과정을 소개한다. 인지 모델 학습에서는 다른 센서로 학습한 모형의 지식을 전달하는 지식 증류, 장면에서 학습한 특징을 다른 과제에도 쓰는 방법을 연구한다. 특징은 입력 자료에서 계산해 얻은 표현으로, 모델이 판단에 사용하는 정보를 담는다.[^av][^deptresearch][^p4][^p6]

경로 계획의 NPPC(Neural Parametric Planning Cost)는 전문가의 주행 행동에서 비용 함수(경로가 얼마나 바람직한지 평가하는 값의 계산 규칙)를 배운다. 함수의 모양을 정하는 값인 매개변수로 공간상 연속적인 비용을 표현하고 이를 직접 최적화(목표와 제약 아래에서 가장 적합한 해를 찾는 계산)해, 미리 준비한 경로 후보 이외의 움직임도 생성하는 접근이다.[^p3]

### 4. 복합 에너지 시스템과 이동 로봇

Archive의 에너지 연구는 전력망이 없는 지역을 대상으로 발전기와 재생에너지 설비, 배터리를 함께 설계하고 운영하는 문제다. 설비 크기를 바꾸면서 에너지 배분 전략을 비교해 시스템 수명 동안의 비용을 평가한다. 여기서 최적화는 목표와 제약을 정한 뒤 그 조건에서 가장 적합한 해를 찾는 계산이다. 이동 로봇 연구는 지상과 공중을 이동하는 재난 대응 로봇, 경사와 보행자·신호를 고려해야 하는 도심 배송 로봇을 다루며, 위치 추정과 지도 작성을 함께 사용한다.[^energy][^robots]

## 대표 논문

금동석 교수가 저자로 있는 2021–2026년 연구 가운데 전동화 구조 설계·시동 제어 두 편, 경로 계획 한 편, 자율주행 인지·지도·학습 네 편을 골랐다. 「쉽게 말하면」은 각 논문의 초록만을 근거로 썼다. 처음 세 편은 OpenAlex 등록 초록이며 연도도 그 등록 연도다. 나머지 네 편은 arXiv 판 초록을 사용하고, arXiv의 학회 표기가 있는 경우 학회명을 함께 적었다. 교신저자 역할은 표기하지 않는다.

| # | 연도 | 논문 · 학술지 | 쉽게 말하면 | 주요 저자 |
|---|---|---|---|---|
| 1 | 2023 | [Designing a Super-Fast Prius: Systematic Design of Multispeed eCVT via Virtual Design Space](https://doi.org/10.1109/TTE.2023.3255901) · IEEE Transactions on Transportation Electrification | 프리우스의 동력 전달 구조에 고정 기어 모드(회전 속도 사이의 관계가 고정되는 동력 전달 방식)를 추가하는 설계 방법이다. 클러치(회전하는 부품 사이의 동력 전달을 잇거나 끊는 장치)와 기어의 배치를 나열하면 같은 속도 관계를 만드는 중복 구조가 생긴다. 이를 줄이려고 가상 설계 공간에서 연비·가속 성능·등판 가능성을 평가하고, 고른 설계를 실제 다단 구조로 바꾸었다.[^p1] | Toumadher Barhoumi, Dongsuk Kum(마지막 저자 금동석) |
| 2 | 2024 | [A Comparative Study on Optimal Engine-Start Performance of Parallel Hybrid Electric Vehicles with Various Starter Motors](https://doi.org/10.1109/ACCESS.2024.3484942) · IEEE Access | 엔진을 시동하는 모터의 종류와 크기가 다른 세 가지 병렬 하이브리드 차량 구조를 비교했다. 시동 중 차량의 거동을 모형으로 만들고 최적 제어 문제를 풀어, 시동 시간과 요구 동력의 부족을 공통 지표로 평가했다. 작은 전용 시동 모터를 둔 구성이 전용 시동 모터가 없는 구성의 시동 문제를 해결하는 대안이 될 수 있다고 제시했다.[^p2] | Jaeyoon Kim, Kijong Park, Dongwoo Kim, Dongsuk Kum(마지막 저자 금동석) |
| 3 | 2026 | [NPPC: Neural Parametric Planning Cost for End-to-End Autonomous Driving](https://doi.org/10.1109/LRA.2026.3663819) · IEEE Robotics and Automation Letters | 전문가의 경로를 그대로 모방하는 자율주행 계획에서 생기는 편향과 누적 오차를 다뤘다. 전문가의 행동을 설명하는 비용 함수를 매개변수로 학습하고 그 함수를 직접 최적화하는 NPPC를 제안했다. 공간을 고정된 칸으로 나누거나 경로 후보의 점수만 매기는 방식의 한계를 다루며, 주행 자료를 이용한 평가에서 충돌 관련 지표와 주행 점수의 개선을 보고했다.[^p3] | Abi Rahman Syamil, Joonhee Lim, Dongsuk Kum(마지막 저자 금동석) |
| 4 | 2026 | [To View Transform or Not to View Transform: NeRF-based Pre-training Perspective](https://arxiv.org/abs/2603.28090) · ICLR 2026 · arXiv 판 | 신경 방사장(NeRF, Neural Radiance Field: 공간 위치와 보는 방향에 따른 장면의 빛을 신경망으로 표현하는 방법)을 이용한 사전 학습에서, 공간을 고정 격자로 바꾸는 과정과 연속적인 공간 표현이 충돌하는 문제를 다뤘다. 점을 바탕으로 연속적인 공간 표현을 배우는 NeRP3D를 제안하고, 사전 학습한 신경망을 장면 재구성과 물체 검출에 이어 사용했다. nuScenes 자료에서 두 과제의 성능 향상을 보였다.[^p4] | Hyeonjun Jeong, Juyeb Shin, Dongsuk Kum(마지막 저자 금동석) |
| 5 | 2025 | [CRAB: Camera-Radar Fusion for Reducing Depth Ambiguity in Backward Projection based View Transformation](https://arxiv.org/abs/2509.05785) · ICRA 2025 · arXiv 판 | 영상만으로는 같은 방향의 물체가 얼마나 떨어져 있는지 구분하기 어려울 수 있다. 영상에서 얻은 깊이 분포와 레이다의 거리 정보를 함께 써, 지면을 내려다보는 표현으로 바꿀 때 생기는 깊이 모호성을 줄였다. 레이다의 장면 정보도 결합하며 nuScenes에서 물체 검출 성능을 평가했다.[^p5] | In-Jae Lee 외, Dongsuk Kum(마지막 저자 금동석) |
| 6 | 2024 | [LabelDistill: Label-guided Cross-modal Knowledge Distillation for Camera-based 3D Object Detection](https://arxiv.org/abs/2407.10164) · ECCV 2024 · arXiv 판 | 라이다(빛을 이용해 거리를 측정하는 장치)로 학습한 모형의 지식을 카메라 기반 검출기에 전달할 때, 멀리 있거나 가려진 물체에 대한 불완전한 정보도 전달되는 문제를 다뤘다. 정답 표기를 특징으로 바꿔 추가 지도를 제공하고, 두 센서의 고유한 특징을 보존하면서 지식을 전달하는 방법을 제안했다. 검출 성능 지표의 개선을 보고했다.[^p6] | Sanmin Kim 외, Dongsuk Kum(마지막 저자 금동석) |
| 7 | 2023 | [InstaGraM: Instance-level Graph Modeling for Vectorized HD Map Learning](https://arxiv.org/abs/2301.04470) · arXiv 사전 공개본 | 고정밀 지도의 도로 요소를 정해진 모양에 맞추는 대신 점과 연결 관계로 표현했다. 다양한 지도 형상을 구성하는 학습과 요소 사이의 연결을 다루는 전략을 제안했다. 공개 자료 실험에서 지도 작성 성능을 평가하고, 먼 범위의 지도를 구성하는 조건에서도 확장 가능성을 보였다.[^p7] | Juyeb Shin, Hyeonjun Jeong, Francois Rameau, Dongsuk Kum(마지막 저자 금동석) |

## 교수와 전문 분야

금동석(Dongsuk Kum) 부교수는 Worcester Polytechnic Institute에서 기계공학 학사(2003), University of Michigan, Ann Arbor에서 기계공학 석사(2005)와 박사(2010)를 받았다. 2010–2012년에는 General Motors의 Global R&D Propulsion Systems Research Lab에서 Research Scientist로 일했다.[^faculty] 조천식모빌리티대학원 교수 명단은 금동석을 전임 부교수로 적고, 연구실 Faculty는 이 대학원의 부교수와 Robotics Program, Kim Jaechul Graduate School of AI, Department of AX, Department of Mechanical Engineering, Division of Future Vehicle의 Adjunct Professor를 함께 적는다.[^deptlist][^faculty]

교수의 연구 관심은 자율주행, 전동화 추진 시스템, 자율 이동 로봇, 최적 제어다.[^faculty] 연구실의 두 팀 소개로 보면 자동차의 인지·계획 알고리즘과 전동화 동력계의 설계·제어가 연결되는 전문 분야다.[^av][^ep] 대표 논문에서는 하이브리드 동력계의 구조 설계·시동 성능 평가, 전문가의 주행 행동을 반영한 경로 계획, 센서 융합·지도 구성·사전 학습을 확인할 수 있다.[^p1][^p2][^p3][^p4][^p5][^p6][^p7] 학술 활동으로는 Journal of Intelligent and Connected Vehicles, International Journal of Automotive Technology 등의 Associate Editor 활동이 Faculty에 올라 있다.[^faculty]

## 응용 분야

자율주행 연구는 인지·경로 계획 알고리즘을 실제 차량과 운행 환경에서 검증하고, 안전하고 편안한 주행을 구현하는 것을 목표로 한다.[^av] 전동화 연구는 하이브리드·배터리·연료전지 전기차의 에너지 사용과 열관리, 동력 전달 구조를 대상으로 한다.[^ep] Archive는 독립형 에너지 공급 시스템, 재난 현장 탐색과 구조 지원 로봇, 도심 배송 로봇을 응용 대상으로 소개한다.[^energy][^robots]

## 구성원

Students & Researchers의 명단과 각 구성원 상세 쪽에 게시된 25명이다. 과정·연구 주제·학교 이메일은 해당 목록의 표기이며, 교수는 위 절에 따로 적었다. 「대표 논문 참여」는 대표 논문의 전체 저자 이름과 명단의 영문 이름을 대조한 표시다.[^members]

| 이름 | 과정·직위 | 연구 주제 | 이메일 | 대표 논문 참여 |
|---|---|---|---|---|
| Toumadher Barhoumi (투마) | 박사후연구원 | Design and control of electric and hybrid electric vehicles; Optimal control of hybrid electric vehicles | toumadher@kaist.ac.kr | 1 |
| 강상묵 (Sangmuk Kang) | 박사과정 | Vehicle Thermal Management Systems(VTMS) | sangmuk.kang@kaist.ac.kr |  |
| 한상준 (Sangjun Han) | 석사과정 | Vehicle Thermal Management Systems(VTMS) | augustinehan@kaist.ac.kr |  |
| Abi Rahman Syamil (아비) | 박사과정 | Path planning for autonomous vehicles | abiofficialmail@kaist.ac.kr | 3 |
| 황시환 (Sihwan Hwang) | 박사과정 | Uncertainty in 3D perception; Data curation | shhwang0129@kaist.ac.kr | 5, 6 |
| 정현준 (Hyeonjun Jeong) | 박사과정 | Self-Supervised Learning; Spatial AI; Neural Rendering | hyeonjun.jeong@kaist.ac.kr | 4, 6, 7 |
| 신주엽 (Juyeb Shin) | 박사과정 | Computer Vision & Deep Learning; HD Map Learning | juyebshin@kaist.ac.kr | 4, 7 |
| 임준희 (Joonhee Lim) | 박사과정 | Decision-Making and Path Planning using Reinforcement Learning; Collision Avoidance/Mitigation System (CAMS) | kingear3@kaist.ac.kr | 3 |
| 장한빈 (Hanbin Jang) | 박사과정 | Path planning, decision, control | hanbin_jang@kaist.ac.kr |  |
| 이선명 (Seonmyeong Lee) | 박사과정 | Perception for autonomous vehicle; Deep Learning | seonmyeong.lee@kaist.ac.kr |  |
| 김현서 (Hyeonseo Kim) | 박사과정 | HD Map Construction; SLAM | hyeonseo.kim@kaist.ac.kr |  |
| 신희원 (Hiwon Shin) | 석사과정 | Auto Labeling | hiwon.shin@kaist.ac.kr |  |
| 이용재 (Yongjae Lee) | 석박사통합과정 | Decision-Making and Path Planning using Reinforcement Learning | yongjae.lee@kaist.ac.kr |  |
| 김형준 (Hyeongjun Kim) | 박사과정 | Data efficient learning; Visual perception for autonomous driving | hyeongjun.kim@kaist.ac.kr |  |
| 조혜린 (Hyelin Jo) | 박사과정 | Diffusion Model; World Model in Autonomous Driving; Self-Supervised Learning | hyelin.jo@kaist.ac.kr |  |
| Saparkhan Kassymbekov (사파) | 석사과정 | Motion planning | saparkhan.kassymbek@kaist.ac.kr |  |
| Hailemichael Molla Gashaw (미카엘) | 석사과정 | End to end autonomous driving; Decision making | hailegashaw12@kaist.ac.kr |  |
| 이예나 (Yeina Lee) | 석사과정 | World Model | yeina.lee@kaist.ac.kr |  |
| Satyam (사티얌) | 석사과정 | Reinforcement Learning; Decision Making; Optimization | satyam.mishra@kaist.ac.kr |  |
| 박무근 (Moogeun Park) | 석사과정 | World Model; Generative AI; 3D Vision | moogeun.park@kaist.ac.kr |  |
| 김도건 (Dogun Kim) | 석사과정 | Vision-Language-Action Model | dogun.kim@kaist.ac.kr |  |
| 김민규 (Mingyu Kim) | 석사과정 | Path Planning; E2E Autonomous Driving | mingyu_kim@kaist.ac.kr |  |
| 곽준성 (JunSeong Kwak) | 석사과정 | Path Planning; Reinforcement Learning; E2E Autonomous Driving | junseong.kwak@kaist.ac.kr |  |
| 김의성 (Uisung Kim) | 석사과정 | Spatial AI; 3D Vision | uisung.kim@kaist.ac.kr |  |
| 박준혁 (Junhyeok Park) | 석사과정 | Vision-Language-Action Model | junhyeok.park01@kaist.ac.kr |  |

## 졸업생과 이전 구성원

Alumni 두 쪽에 게시된 42명이다. 박사 7명·석사 28명과 Researcher·Research Assistant·Exchange program으로 구분된 이전 구성원 7명을 포함한다. 학위·직함·연도·진로는 원문 표기이며 연도는 2014–2026년이다. 학위논문은 영문 이름과 졸업 연도가 함께 일치하는 항목만 덧붙였다.[^alumni][^theses]

| 이름 | 학위·직함 (연도) | 랩이 적은 진로 | 학위 논문 |
|---|---|---|---|
| 박근영 (Geunyoung Park) | Ph.D. (2026) | 한국과학기술원 (KAIST) |  |
| 나아 (Naa Ashifia Anum) | M.S. (2026) |  |  |
| 송채희 (Chaehee Song) | M.S. (2025) | 한국과학기술원 (KAIST) | Camera-Radar Fusion with Radar Feature Enrichment for 3D Occupancy Prediction (2025) |
| 김원준 (Wonjune Kim) | M.S. (2025) | 한국전자통신연구원 (ETRI) | Class Distribution-Based Active Learning for 3D Occupancy Prediction in Autonomous Driving (2025) |
| 핫 (Truong, Van Hot) | M.S. (2024) |  | Self-supervised Pre-training for Camera-based 3D Object Detection via Cross-modal Distillation and Volumetric Rendering (2024) |
| 김산민 (Sanmin Kim) | Ph.D. (2024) | 국민대학교 (Kookmin University) | Image-based 3D Object Detection for Autonomous Driving: Leveraging Temporal and Spatial Information (2024) |
| 최종민 (Jongmin Choi) | M.S. (2024) |  | Transformer-Based Visual Localization through Cross-View Matching (2024) |
| 이인재 (Injae Lee) | M.S. (2024) |  | Camera-Radar Fusion for Backward Projection based 3D Object Detection (2024) |
| 김영석 (Youngseok Kim) | Ph.D. (2023) | 포티투닷 (42dot) | 3D Object Detection via Multi-Sensor Fusion for Autonomous Driving (2023) |
| 강대준 (Daejun Kang) | Ph.D. (2023) | 한국자동차연구원 (KATECH) | A Study on Meta-Learning-based Continual Learning Framework for Scalability of Motion Prediction Model (2023) |
| 아흐메드 (Ahmed Magd Aly Shehata) | M.S. (2023) | 한국과학기술원 (KAIST) |  |
| 김의현 (Uihyun Kim) | M.S. (2023) | 에이치엘클레무브 (HL Klemove) |  |
| 박준영 (Junyoung Park) | M.S. (2023) | 현대모비스 (HYUNDAI MOBIS) | Intentional non-yielding intelligent driver model development for cut-in & cut-out situations considering interaction with surrounding vehicles (2023) |
| 전형석 (Hyeongseok Jeon) | Ph.D. (2022) | 모라이 (MORAI) | Deep learning based trajectory prediction system for autonomous vehicle using heterogeneous datasets overcoming data defection (2022) |
| 이현호 (Hyunho Lee) | M.S. (2022) | 현대자동차 (HYUNDAI Motors) | Design Optimization of Multi-mode Power-split type Architectures for AWD Hybrid Pickup Trucks (2022) |
| 심상민 (Sangmin Sim) | M.S. (2022) | 현대자동차 (HYUNDAI Motors) | Sequential Image-based 3D Object Detection with Depth-Offset Guided Location Refinement (2022) |
| 박준태 (Juntae Park) | M.S. (2022) | 현대자동차 (HYUNDAI Motors) | Proof of Concept for Dog Clutch-based Electric Transmission System via Preview Control (2022) |
| 김재윤 (Jaeyoon Kim) | M.S. (2021) | 현대자동차 (HYUNDAI Motors) | Comparative Study on Optimal Engine-Start Performance of Parallel Hybrid Electric Vehicles with Various Starter Motors (2021) |
| 유희철 (Heecheol Yoo) | M.S. (2021) | 모라이 (MORAI) | Two-Level Distribution Alignment for Unsupervised Domain Adaptation of LiDAR-based Object Detector (2021) |
| 고명재 (MyeongJae Go) | M.S. (2021) | SK 이노베이션 (SK Innovation) | Simultaneous prediction of peak current and duration time using diffusion induced stress in lithium-ion battery active material (2021) |
| 강주영 (Jooyoung Kang) | M.S. (2020) | 현대자동차 (HYUNDAI Motors) | High-fidelity modeling of dog clutch and its control and design studies based on statistical analysis (2020) |
| 김현준 (Hyunjun Kim) | M.S. (2015) | 한국자동차연구원 (KATECH) | Design Methodology of Input and Output-Split Hybrid Electric Vehicle for Searching an Optimal Configuration (2015) |
| 이기범 (Dr. Kibeom Lee) | Ph.D. (2020) | 가천대학교 (Gachon University) | Emergency Collision Avoidance/Mitigation System: Motion Planning and Control of Autonomous Vehicle (2020) |
| 이건 (Dr. Kun Lee) | Ph.D. (2020) | SK 이노베이션 (SK Innovation) | System design and operation methodologies for hybrid renewable energy systems: Component sizing and optimal control under uncertainties (2020) |
| 김진형 (Jinhyeong Kim) | M.S. (2020) | 포티투닷 (42dot) | Low-Level Radar-Camera Dataset Construction and Sensor Fusion Network for Robust Vehicle Detection (2020) |
| 우동현 (Donghyeon Woo) | M.S. (2020) | 현대자동차 (HYUNDAI Motors) | Predictive Energy Management Strategy on Hybrid Electric Vehicle utilizing Available Future Information (2020) |
| 전승민 (Seunmin Jeon) | M.S (2020) | 모라이 (MORAI) |  |
| 황슬빈 (Seulbin Hwang) | M.S. (2020) | 네이버랩스 (Naver LABS) | Lane-Merging of autonomous vehicle via Finite state machine and Policy-based RL (2020) |
| 김경근 (Kyeongken Kim) | M.S. (2019) | 현대자동차 (HYUNDAI Motors) |  |
| 손영호 (Youngho Son) | M.S. (2017) | 만도 (Mando) | Robust Multi-Lane Detection and Tracking for Automated Highway Driving System (2017) |
| 윤승제 (Seungje Yoon) | M.S. (2017) | 씨메스 (CMES) | Probabilistic Motion Prediction of Surrounding Vehicles via Artificial Neural Network and Its Application for Longitudinal Collision Avoidance System (2017) |
| 강진건 (Jingeon Kang) | M.S. (2016) | 현대모비스 (HYUNDAI MOBIS) | Design Methodology of Inpu- and Outpu-split Hybrid Electric Vehicles with a Speed Reductioin Gear for Selecting an Optimal Configuration (2016) |
| 황재호 (Jaeho Hwang) | M.S. (2016) | 현대자동차 (HYUNDAI Motors) |  |
| 김재환 (Jaehwan Kim) | M.S. (2015) | 에이치엘클레무브 (HL Klemove) |  |
| 캠퍼 파울로 (Paulo Kemper) | M.S. (2014) | Manna CEA | Lithium-ion battery electrochemical model for high-current control applications - Extended Single Particle Model (2014) |
| 이석기 (Seokki Lee) | Researcher (2023) |  |  |
| 우상범 (Sangbeom Woo) | Research Assistant (2021) | 로보티즈 (Robotis) |  |
| 고형선 (Lunaric Ko) | Research Assistant (2020) | 스타트업 |  |
| 이승준 (Seoungjun Lee) | Research Assistant (2018) | University of Pennsylvania (Ph.D. course) |  |
| 에또레 (Ettore Zanetti) | Exchange program (2017) |  | Model Based Control of a Hybrid Heat Pump System for Building Heating (2017) |
| 주형국 (Hyungkook Joo) | Research Assistant (2016) | LG전자 (LG Electronics) |  |
| 시모네 (Simonre Amicabile) | Exchange program (2014) | Fondazione Bruno Kessler, Applied Research on Energy Systems (ARES) |  |

## 최근 논문 목록 (2021–2026)

차량의 인지·예측·경로 계획과 전동화 동력계의 에너지 관리·구조 설계를 다룬다. 연구실 목록의 2021–2026년 구역에 게시된 91항목으로, 국제 학술지 22편·국제 학회와 워크숍 24건·국내 논문과 학회 45건이다. 같은 제목이 다른 발표·출판 구획에 있으면 게시 구획별로 적었다. 연도와 저자·서지는 연구실 표기를 따르며, 날짜 없이 게재 승인·채택으로 적힌 항목은 해당 연도 구역 안에서 그 상태를 표시했다.[^journals][^conferences][^domestic]

**2026**

- Geunyoung Park, Kyunghwan Choi, Dongsuk Kum. "Synthesis of a Link-Level Energy-Time Predictor Toward the Implementation of a Link-based Predictive EMS". *IEEE Access*.
- Geunyoung Park, Sangmuk Kang, Heedae Lee, Joongmyeon Bae, Kyungsub Sung, and Dongsuk Kum. "High-fidelity modeling of the Toyota Mirai FCEV thermal management system: a step toward real-vehicle thermal behavior". *Energy Conversion and Management*.
- Hanbin Jang, Joonhee Lim, Abi Rahman Syamil, Dongsuk Kum. "Reaction-Uncertainty-Aware Motion Planning for Interactive Driving via Conditional Multi-modal Motion Prediction". *IEEE Access*.
- Joonhee Lim, Yongjae Lee, Jangho Shin, Dongsuk Kum. "Continual Reinforcement Learning Framework for Scalable Collision Avoidance and Mitigation System with Packing Strategy". *IEEE Robotics and Automation Letters*.
- Sangmuk Kang, Geunyoung Park, Dongsuk Kum. "Physics-informed neural networks for estimating flooding in a three-dimensional proton exchange membrane fuel cell". *International Journal of Heat and Mass Transfer (게재 승인)*.
- Wonjune Kim, In-Jae Lee, Sihwan Hwang, Sanmin Kim, and Dongsuk Kum. "Class-Distribution Guided Active Learning for 3D Occupancy Prediction in Autonomous Driving". *IEEE Robotics and Automation Letters*.
- Abi Rahman Syamil, Joonhee Lim and Dongsuk Kum. "NPPC: Neural Parametric Planning Cost for End-to-end Autonomous Driving". *IEEE Robotics and Automation Letters*.
- Hyeonseo Kim, Juyeb Shin, Hyeonjun Jeong, Hiwon Shin, Dongsuk Kum. "MapTCL: Temporal Consistency Learning via Bidirectional Alignment for Vectorized HD Map Construction". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Joonhee Lim, Yongjae Lee, Dongsuk Kum. "PlanRL: A Trajectory Planning Architecture for Reinforcement Learning-based Driving Experts". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- Hyeonjun Jeong, Juyeb Shin and Dongsuk Kum. "To View Transform or Not To View Transform: NeRF-based Pre-training Perspective". *International Conference on Learning Representations(ICLR) (채택)*.
- Sihwan Hwang, Sanmin Kim, Hyeonjun Jeong, and Dongsuk Kum. "Reducing Annotation Costs for Autonomous Driving: Scalable Perception via Multi-Level Active Domain Adaptation". *IEEE Intelligent Vehicles Symposium (IV)*.
- 신희원, 금동석. "다중 시퀀스 좌표계 정렬 기반 고정밀 HD Map 오토 라벨링". *2026년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 신희원, 금동석. "불확실성을 고려한 HD Map 오토 라벨링: 확률적 2D-3D 레이블 리프팅과 확산 기반 보정". *2026년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 장한빈, 김종모, 금동석. "MCTS 기반 강화학습을 통한 자율주차에서의 단기적 정책 완화". *2026년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 이용재, 임준희, 금동석. "자율주행을 위한 경로 계획 기반 강화학습 자율주행 전문가". *2026년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- Hailemichael Molla, Satyam Mishra, 임준희, 금동석. "Offline Reward-Guided Trajectory Scoring for Generate-Then-Select Planning in End-to-End Autonomous Driving". *2026년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.

**2025**

- Abi Rahman Syamil and Dongsuk Kum. "Learning Homotopy Prediction for Optimization-Based Trajectory Planners for Autonomous Driving". *International Journal of Automotive Technology*.
- Geunyoung Park, Kyunghwan Choi, Minjun Kim, Eunae Cho, Kyungsub Sung and Dongsuk Kum. "Development of a real-time link-based predictive energy management strategy for extending FCEV lifespan using an experiment-driven degradation model". *Elsevier Applied Energy*.
- Juyeb Shin, Hyeonjun Jeong, Francois Rameau, and Dongsuk Kum. "InstaGraM: Instance-level Graph Modelingfor Vectorized HD Map Learning". *IEEE Transactions on Intelligent Transportation Systems*.
- Chaehee Song, Sanmin Kim, Hyeonjun Jeong, Juyeb Shin, Joonhee Lim and Dongsuk Kum. "REOcc: Camera-Radar Fusion with Radar Feature Enrichment for 3D Occupancy Prediction". *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
- In-Jae Lee, Sihwan Hwang, Youngseok Kim, Wonjune Kim, Sanmin Kim, and Dongsuk Kum. "CRAB: Camera-Radar Fusion for Reducing Depth Ambiguity in Backward Projection based View Transformation". *IEEE International Conference on Robotics and Automation (ICRA)*.
- 이용재, 장한빈, 임준희, 금동석. "End-to-End 자율주행 연구 동향 및 발전 방향: 실험 환경 및 평가 방법을 중심으로". *2025년 한국자동차공학회(KSAE) 추계학술대회, 부산*.
- 이선명, 황시환, 금동석. "분포 기반 데이터 샘플링 및 이수준 최적화를 통한 자율주행 3차원 인지 모델의 연속 학습". *2025년 한국자동차공학회(KSAE) 추계학술대회, 부산*.
- 김형준, 금동석. "효율적인 사전 학습을 위한 온라인 데이터 큐레이션 기반 자율주행 데이터 중복성 완화". *2025년 한국자동차공학회(KSAE) 추계학술대회, 부산*.
- 조혜린, 금동석. "파운데이션 모델을 활용한 디퓨전 기반 BEV 표현 학습". *2025년 한국자동차공학회(KSAE) 추계학술대회, 부산*.
- 박근영, 성경섭, 금동석. "미라이 2세대 기반 통합 열관리 시스템 모델링 및 실주행 데이터 검증". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 신주엽, 금동석. "가우시안 맵 Prior를 활용한 주행 환경 인지". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 정현준, 금동석. "NeRF 기반 사전학습에서 시점 변환을 넘어선 연속적인 3차원 표현 학습". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 황시환, 금동석. "멀티레벨 도메인 적응형 능동학습". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 임준희, 신창호, 금동석. "지속적 강화학습을 통한 충돌 회피 및 경감 시스템의 확장 가능한 학습 프레임워크". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 강상묵, 금동석. "고분자 전해질막 연료 전지의 플러딩 분석을 위한 물리 정보 기반 인공 신경망 프레임워크". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 김현서, 금동석. "정밀도로지도 생성을 위한 이중 명시적 시간적 일관성 기반 도로 객체 검출". *2025년 한국자동차공학회(KSAE) 춘계학술대회, 제주*.
- 장한빈, 임준희, 금동석. "자율주행의 트리 정책 계획을 위한 조건부 다중 경로 예측 및 불확실성에 강건한 비용 평가". *Transactions of KSAE*.

**2024**

- Hyeonjun Jeong, Juyeb Shin, Francois Rameau, and Dongsuk Kum. "Multi-Modal Place Recognition via Vectorized HD Maps and Images Fusion for Autonomous Driving". *IEEE Robotics and Automation Letters*.
- Jaeyoon Kim, Kijong Park, Dongwoo Kim, and Dongsuk Kum. "A Comparative Study on Optimal Engine-Start Performance of Parallel Hybrid Electric Vehicles with Various Starter Motors". *IEEE Access*.
- Geunyoung Park, Kyunghwan Choi, and Dongsuk Kum. "Predictive Control of a Dog-clutch Transmission via a Transformer-based Velocity Prediction". *IEEE Transactions on Vehicular Technology*.
- Kyunghwan Choi, Geunyoung Park, and Dongsuk Kum. "An Analytical Approach to the Predictive Energy Management of Connected HEVs: What Information Do We Need to Guarantee Global Optimality?". *IEEE Transactions on Intelligent Transportation Systems*.
- Sanmin Kim, Youngseok Kim, Sihwan Hwang, Hyeonjun Jeong and Dongsuk Kum. "LabelDistill: Label-guided Cross-modal Knowledge Distillation for Camera-based 3D Object Detection". *European Conference on Computer Vision (ECCV)*.
- Hyeongseok Jeon, Sanmin Kim, Abi Rahman Syamil, Junsoo Kim and Dongsuk Kum. "Beyond the Data Imbalance: Employing the Heterogeneous Datasets for Vehicle Maneuver Prediction". *European Conference on Computer Vision (ECCV)*.
- Geunyoung Park, Kyunghwan Choi and Dongsuk Kum. "Stack Degradation Protection of FCEVs via Predictive Energy Management Strategy with Segmented Roads". *American Control Conference (ACC)*.
- DaeJun Kang, Sanmin Kim and Dongsuk Kum. "Continual Motion Prediction Learning Framework via Meta-Representation Learning and Optimal Memory Buffer Retention Strategy". *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
- Geonho Bang, Kwangjin Choi, Jisong Kim, Dongsuk Kum, and Jun Won Choi. "RadarDistill: Boosting Radar-based Object Detection Performance via Knowledge Distillation from LiDAR Features". *IEEE/CVF Conference on Computer Vision and Pattern Recognition(CVPR)*.
- Jisong Kim, Minjae Seong, Geonho Bang, Dongsuk Kum and JunWon Choi. "RCM-Fusion: Radar-Camera Multi-Level Fusion for 3D Object Detection". *IEEE International Conference on Robotics and Automation (ICRA)*.
- Joonhee Lim,  Kibeom Lee, Jangho Shin and Dongsuk Kum. "Learning Terminal State of the Trajectory Planner: Application for Collision Scenarios of Autonomous Vehicles". *IEEE International Conference on Robotics and Automation (ICRA)*.
- 바후미투마더, 금동석. "도그 클러치를 이용한 다중 모드 하이브리드 전기 자동차의 모드 전환 제어". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- Truong Van Hot, 정현준, 김산민, 금동석. "마스킹 이미지 모델링과 볼륨 렌더링을 통한 카메라 기반 3차원 객체 검출을 위한 자기지도 사전 학습". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- Abi Rahman Syamil, 금동석. "자율주행의 경로 계획을 위한 학습 기반 매개변수 비용 함수". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 송채희, 김산민, 금동석. "레이더 특징을 활용한 카메라 및 레이더 융합 기반 3차원 공간 점유 예측 모델". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 강상묵, 금동석. "물리 정보 기반 인공 신경망을 이용한 고분자 전해질막 연료 전지의 플러딩 발생 조건 분석". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 박근영, 성경섭, 금동석. "수소연료전지 차량의 내구성을 고려한 예측 에너지 관리 전략". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 임준희, 장한빈, 신장호, 금동석. "적대적 운전자 모델을 활용한 충돌 시나리오 생성". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 김현서, 신주엽, 금동석. "정밀도로지도 생성을 위한 시간적 일관성 기반 도로 객체 검출". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 황시환, 김산민, 금동석. "확장가능한 자율주행을 위한 도메인 적응형 능동학습". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 이선명, 금동석. "자율주행 인지 모델의 지속적 학습을 위한 메타러닝 프레임워크". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 김원준, 김산민, 금동석. "효율적인 3차원 공간 점유 예측을 위한 클래스 빈도 분포 기반 능동학습". *2024년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 최종민, 금동석. "교차 시점 매칭 기반 시각적 차량 위치 추정". *2024년 한국자동차공학회(KSAE) 춘계학술대회, 거제*.

**2023**

- Toumadher Barhoumi and Dongsuk Kum. "Designing a Super-fast Prius: Systematic Design of Multi-speed eCVT via Virtual Design Space". *IEEE Transactions on Transportation Electrification*.
- Sanmin Kim, Hyeongseok Jeon, Jun Won Choi, Dongsuk Kum. "Diverse Multiple Trajectory Prediction using a Two-stage Prediction Network trained with Lane Loss". *IEEE Robotics and Automation Letters*.
- Hyeongseok  Jeon, Sanmin Kim, Kibeom Lee, Dae Jun Kang, Jun Won Choi, and Dongsuk Kum. "Are Reactions to Ego Vehicles Predictable without Data?: A Semi-supervised Approach". *IEEE Transactions on Intelligent Transportation Systems*.
- Sanmin Kim, Youngseok Kim, In-Jae Lee and Dongsuk Kum. "Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images". *International Conference on Computer Vision (ICCV) 2023*.
- Youngseok Kim, Sanmin Kim, Juyeb Shin, Jun Won Choi, Dongsuk Kum. "CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception". *International Conference on Computer Vision (ICCV) 2023*.
- Juyeb Shin, Francois Rameau, Hyeonjun Jeong, Dongsuk Kum. "InstaGraM: Instance-level Graph Modeling for Vectorized HD Map Learning". *Workshop on Vision-Centric Autonomous Driving (VCAD) at Conference on Computer Vision and Pattern Recognition (CVPR) 2023*.
- Youngseok Kim, Sanmin Kim, Juyeb Shin, Jun Won Choi, Dongsuk Kum. "CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception". *International Conference on Learning Representations (ICLR) Workshop on Scene Representations for Autonomous Driving*.
- Sihwan Hwang, Sanmin Kim, Youngseok Kim, Dongsuk Kum. "Joint Semi-Supervised and Active Learning via 3D Consistency for 3D Object Detection". *IEEE International Conference on Robotics and Automation (ICRA)*.
- Youngseok Kim, Sanmin Kim, Jun Won Choi, Dongsuk Kum. "CRAFT: Camera-Radar 3D Object Detection with Spatio-Contextual Fusion Transformer". *Thirty-Seventh AAAI Conference on Artificial Intelligence*.
- 강대준, 김산민, 금동석. "경로예측모델을 위한 평생학습 프레임워크 연구". *2023년 한국자동차공학회(KSAE) 추계학술대회, 울산*.
- 황시환, 금동석. "다중센서 기반 3차원 객체 검출 모델의 능동학습". *2023년 한국자동차공학회(KSAE) 추계학술대회, 울산*.
- 이인재, 김영석, 금동석. "카메라-레이더 융합을 통한 Transformer 기반의 3차원 객체 검출 모델 개선". *2023년 한국자동차공학회(KSAE) 추계학술대회, 울산*.
- 임준희, 이기범, 금동석. "통합적 충돌 회피 및 경감 시스템을 위한 강화학습 기반 경로 계획". *2023 한국자동차공학회(KSAE) 춘계학술대회, 평창*.
- 김의현, 금동석. "최적 속도 계획과 에너지 관리 전략을 통한 연료 전지 하이브리드 차량의 연비 최적화". *2023 한국자동차공학회(KSAE) 춘계학술대회, 평창*.

**2022**

- Youngseok Kim, Sanmin Kim, Jun Won Choi, and Dongsuk Kum. "Boosting Monocular 3D Object Detection with Object-Centric Auxiliary Depth Supervision". *IEEE Transactions on Intelligent Transportation Systems*.
- Jie Han, Xiaosong Hu, Yalian Yang, Lech M. Grzesiak, and Dongsuk Kum. "Joint Optimization of Configuration, Component Sizing, and Energy Management for Input-split Hybrid Powertrains". *IEEE Transactions on Vehicular Technology*.
- Seungmin Jeon, Kibeom Lee, and Dongsuk Kum. "Overtaking Decision and Trajectory Planning in Highway via Hierarchical Architecture of Conditional State Machine and Chance Constrained Model Predictive Control". *Robotics and Autonomous Systems*.
- Hwang, Seulbin; Lee, Kibeom; Jeon, Hyeongseok; Kum, Dongsuk. "Autonomous Vehicle Cut-in Algorithm for Lane-Merging Scenarios via Policy-based Reinforcement Learning Nested within Finite State Machine". *IEEE Transactions on Intelligent Transportation Systems*.
- Geunyoung Park, Juntae Park, and Dongsuk Kum. "Preview Control of Dog clutch-based Electric Vehicle Transmission via Dynamic Programming: Proof of Concept". *IEEE Conference on Control Technology and Applications*.
- Sangmin Sim, Youngseok Kim, and Dongsuk Kum. "Sequential Image-based 3D Object Detection with Location Refinement". *IEEE 26th International Conference on Pattern Recognition*.
- Toumadher Barhoumi, Dongsuk Kum. "Systematic Design of Fixed Gear Modes for Novel Multi-mode Architectures: A Prius Case Study". *European Control Conference (ECC)*.
- 정현준, 프랑수아 라미우, 금동석. "벡터화 지도 기반의 자율주행 차량을 위한 위치 추정". *2022년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 신주엽, 프랑수아 라미우, 금동석. "정밀도로지도 매핑을 위한 BEV 도로 객체 검출". *2022년 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 박준영, 금동석. "차량 진입 환경에서의 의도적인 비양보 운전자모델". *2022 한국자동차공학회(KSAE) 추계학술대회, 제주*.
- 박근영, 금동석. "MPC를 활용한 도그 클러치 전동화 변속기의 프리뷰 제어". *2022 한국자동차공학회(KSAE) 춘계학술대회*.
- 황시환, 금동석. "일관성 기반 불확실성 추정을 사용한 3 차원 객체 검출 모델의 능동학습". *2022 한국로봇학회 한국로봇종합학술대회, 평창*.
- 김산민, 김영석, 전형석, 금동석, 이기범. "자율주행 기술 동향 및 발전 방향: AI를 중심으로". *한국자동차공학회 논문집 (Transactions of KSAE)*.

**2021**

- Peng, Baiyu; Sun, Qi; Li, Shengbo Eben; Kum, Dongsuk; Yin, Yuming; Wei, Junqing; Gu, Tianyu. "End-to-End Autonomous Driving Through Dueling Double Deep Q-Network". *AUTOMOTIVE INNOVATION*.
- Jaekyum Kim, Junho Koh, Jin Hyeok Yoo, Yecheol Kim, Dongsuk Kum, Jun Won Choi. "Joint 3D Object Detection and Tracking Using Spatio-Temporal Representation of Camera Image and LiDAR Point Clouds". *Thirty-Sixth AAAI Conference on Artificial Intelligence*.
- B. Kim, S. H. Park, S. Lee, E. Khoshimjonov, D. Kum, J. Kim, J. S. Kim, and J. W. Choi. "LaPred: Lane-aware Prediction of Multi-modal Future Trajectories of Dynamic Agents". *IEEE Computer Vision and Pattern Recognition (CVPR)*.
- 김산민, 금동석, 최준원. "자율주행 차량에서의 차선 수준의 지도 정보를 활용한 차량 경로 예측". *2021년 한국자동차공학회(KSAE) 추계학술대회, 여수, 2021 11월 17일~19일*.
- Toumadher Barhoumi, Dongsuk Kum. "Analysis of Toyota Prius 4th generation-based multi-mode systems using dog clutches". *2021년 한국자동차공학회(KSAE) 춘계학술대회, 대전.세종.충청지회*.
- 박준태, 금동석. "다단 변속기를 가진 상용 전기자동차를 위한 도그 클러치 전동화 변속 시스템 개발". *2021년 한국자동차공학회(KSAE) 추계학술대회, 여수, 2021 11월 17일~19일*.
- 이현호, 금동석. "최적의 동력 분기형 AWD 하이브리드 전기차 아키텍처 탐색". *2021년 한국자동차공학회(KSAE) 추계학술대회, 여수, 2021 11월 17일~19일*.
- 심상민, 금동석. "자율주행을 위한 이미지 시퀀스 기반의 3차원 객체 검출 네트워크". *2021년 한국자동차공학회(KSAE) 추계학술대회, 여수, 2021 11월 17일~19일*.

## 학위논문 (2021–2026)

Dissertation 전체 52편 가운데 2021–2026년 구역의 31편이다. 저자와 제목은 연구실 표기이며, 위의 교수 참여 논문 목록과 별도로 적었다.[^theses]

- 2026 · Hiwon Shin. "Multi-trip Alignment and Uncertainty-aware Reconstruction for HD Map Auto-labeling".
- 2026 · Hyelin Jo. "Diffusion-based Bird's-Eye-View Representation Learning with Semantic Guidance".
- 2026 · Naa Ashifa Anum. "Feasibility Assessment of Dog Clutch Integration in Multi-Mode Power-Split HEVs Under Transient Mode Shift Control".
- 2026 · Hyeongjun Kim. "Data Subset Selection Algorithm for Efficient Pre-training in Autonomous Driving".
- 2025 · Hyeonseo Kim. "Temporal Consistency Learning for Vectorized HD Map Construction".
- 2025 · Sangmuk Kang. "Physics-Informed Neural Networks-based Flooding Analysis of Proton Exchange Membrane Fuel Cells".
- 2025 · Wonjune Kim. "Class Distribution-Based Active Learning for 3D Occupancy Prediction in Autonomous Driving".
- 2025 · Chaehee Song. "Camera-Radar Fusion with Radar Feature Enrichment for 3D Occupancy Prediction".
- 2025 · Sunmyung Lee. "Meta-learning Framework for Continual Learning Autonomous Driving Perception Model".
- 2025 · Hanbin Jang. "Reaction-aware Motion Planning through Multi-modal Motion Prediction".
- 2024 · Jongmin Choi. "Transformer-Based Visual Localization through Cross-View Matching".
- 2024 · Sanmin Kim. "Image-based 3D Object Detection for Autonomous Driving: Leveraging Temporal and Spatial Information".
- 2024 · Truong Van Hot. "Self-supervised Pre-training for Camera-based 3D Object Detection via Cross-modal Distillation and Volumetric Rendering".
- 2024 · Toumadher Barhoumi. "Design and Control of Parallel/Split Architectures with Dog Clutches via Virtual Design Space".
- 2024 · Injae Lee. "Camera-Radar Fusion for Backward Projection based 3D Object Detection".
- 2024 · Joonhee Lim. "Deep Reinforcement Learning-based Collision Avoidance and Mitigation Trajectory Planning through Terminal State Learning".
- 2023 · Daejun Kang. "A Study on Meta-Learning-based Continual Learning Framework for Scalability of Motion Prediction Model".
- 2023 · Youngseok Kim. "3D Object Detection via Multi-Sensor Fusion for Autonomous Driving".
- 2023 · Jun-Young Park. "Intentional non-yielding intelligent driver model development for cut-in & cut-out situations considering interaction with surrounding vehicles".
- 2023 · Hyeonjun Jeong. "Vectorized Map-based Fusion for Visual Place Recognition via Hierarchical Spatial Interaction in Graph".
- 2023 · Juyeb Shin. "Instance-level Graph Modeling for End-to-end Vectorized HD Map Learning".
- 2022 · Hyeongseok Jeon. "Deep learning based trajectory prediction system for autonomous vehicle using heterogeneous datasets overcoming data defection".
- 2022 · Geunyoung Park. "MPC based Preview Control for Dog clutch-based Electric Vehicle Transmission".
- 2022 · Sihwan Hwang. "Semi-supervised Active Learning for 3D Object Detection using Consistency based Uncertainty".
- 2022 · Hyunho Lee. "Design Optimization of Multi-mode Power-split type Architectures for AWD Hybrid Pickup Trucks".
- 2022 · Sangmin Sim. "Sequential Image-based 3D Object Detection with Depth-Offset Guided Location Refinement".
- 2022 · Juntae Park. "Proof of Concept for Dog Clutch-based Electric Transmission System via Preview Control".
- 2021 · Abi Rahman Syamil. "Learning Constraint Identification and Classification for Online Model Predictive Planning at Unsignalized Intersections for Autonomous Vehicles".
- 2021 · Jaeyoon Kim. "Comparative Study on Optimal Engine-Start Performance of Parallel Hybrid Electric Vehicles with Various Starter Motors".
- 2021 · Hee-Cheol Yoo. "Two-Level Distribution Alignment for Unsupervised Domain Adaptation of LiDAR-based Object Detector".
- 2021 · Myeongjae Go. "Simultaneous prediction of peak current and duration time using diffusion induced stress in lithium-ion battery active material".

## 특허

전체 54개 게시항목의 상세 쪽에서 출원일 또는 등록일이 2021-10-13–2026-10-13 안에 드는 것을 확인한 28항목이다. 출원이 기간 이전이어도 등록일이 기간 안인 4항목을 포함한다. 번호·날짜·발명자·국가는 게시된 값을 따르며, 국가가 없는 항목은 따로 보충하지 않았다. 같은 등록번호가 서로 다른 출원번호의 항목에 적혀 있거나 한 항목에 여러 국가·출원일이 있어도 원문 게시 구분을 유지했다.[^patents]

- 차량의 충돌 회피 및 경감을 위한 경로 생성 방법, 경로 생성 시스템, 및 그 학습 방법 (출원일 2025-07-03; 출원번호 10-2026-0122823; 국가 KR; 발명자 금동석, 임준희, 신장호)
- 벡터 인스턴스의 시간적 일관성을 이용한 고정밀 지도 생성 방법 및 장치 (출원일 2026-05-13; 출원번호 10-2026-0086664; 국가 KR; 발명자 금동석, 김현서)
- 3차원 인지 모델의 도메인 적응형 능동학습을 위한 멀티레벨 도메인 분류기 (출원일 2026.01.02; 출원번호 10-2026-0000193; 발명자 금동석, 황시환)
- 자율주행 차량의 3차원 인지 모델을 위한 연속 학습 방법, 장치, 및 컴퓨터프로그램 (출원일 2026-02-05; 출원번호 10-2026-0023143; 국가 KR; 발명자 금동석, 이선명)
- Camera-Radar Fusion for Backward Projection based 3D Perception (출원일 2025-06-30; 출원번호 PCT/KR2025/009160; 국가 PCT; 발명자 금동석, 이인재, 황시환)
- PATH GENERATION SYSTEM FOR VEHICULAR COLLISION AVOIDANCE AND MITIGATION (출원일 2025-06-19; 출원번호 18/637,004; 국가 US; 발명자 Jangho Shin, Dongsuk Kum, Joonhee Lim)
- 다중모드를 구비한 하이브리드 자동차용 구동장치 (출원일 2025.05.13; 출원번호 10-2025-0061716; 발명자 금동석, 바후미 투마더)
- 자율주행 시스템의 경로 계획을 위한 학습기반 매개변수로 형성된 함수 (출원일 2025-02-24; 출원번호 10-2025-0023339; 등록일 2025-12-26; 등록번호 10-2906206; 국가 KR; 발명자 금동석, 아비 라만 샤밀, 이용재)
- 크로스모달 지식증류를 활용한 이미지 기반 3차원 객체 검출 방법 및 장치 (출원일 2025-11-27; 출원번호 10-2025-0184052; 국가 KR; 발명자 금동석, 김산민, 황시환)
- METHOD AND SYSTEM FOR ONLINE MODEL PREDICTIVE PLANNING BASED ON LEARNING IDENTIFICATION AND CLASSIFICATION OF CONSTRAINT (출원일 2024-11-19; 출원번호 18/952,506; 국가 US; 발명자 Dongsuk Kum, Abi Rahman Syamil, Hanbin Jang)
- 시계열 이미지를 이용한 3차원 객체 검출 기술 (출원일 2024.11.07; 출원번호 10-2024-0157318; 발명자 금동석, 김산민)
- 역투영 기반의 3차원 인지를 위한 카메라-레이더 융합 (출원일 2024-10-25; 출원번호 10-2024-0147151; 국가 KR; 발명자 금동석, 이인재, 황시환)
- METHOD AND SYSTEM FOR PERCEIVING TRAFFIC ROAD ENVIRONMENT BASED ON GRAPH REPRESENTATION FOR AUTONOMOUS DRIVING (출원일 2024-10-07; 출원번호 18/908,040; 국가 US; 발명자 Dongsuk Kum, Juyeb Shin)
- 자율주행을 위한 벡터화 고정밀 지도와 이미지를 이용한 다중 모드 장소 인식 방법 및 그 시스템 (출원일 2024-03-20; 출원번호 10-2024-0038340; 등록일 2025-04-28; 등록번호 10-2803338; 국가 KR; 발명자 금동석, 정현준)
- 자율주행을 위한 그래프 기반 조감도 주행 환경 인지 방법 및 그 시스템 (출원일 2024-03-29; 출원번호 10-2024-0043159; 등록일 2025-04-28; 등록번호 10-2803337; 국가 KR; 발명자 금동석, 신주엽)
- 자율주행을 위한 3D 객체 검출 모델의 비지도 손실 기반 능동학습 방법 및 그 시스템 (출원일 2024-03-18; 출원번호 10-2024-0037439; 등록일 2025-04-25; 등록번호 10-2802261; 국가 KR; 발명자 금동석, 황시환)
- 차량의 충돌 회피 및 경감을 위한 경로 생성 시스템 (출원일 2023-12-14; 출원번호 10-2023-0182334; 국가 KR; 발명자 신장호, 금동석, 임준희)
- 제약 조건의 확인 및 분류 학습에 기반한 자율주행 차량의 실시간 모델 예측 제어 기반 계획 방법 및 시스템 (출원일 2023-11-30; 출원번호 10-2023-0171336; 국가 KR; 발명자 금동석, Abi Rahman Syamil, 장한빈)
- SYSTEM AND METHOD FOR PERCEIVING 3-D ENVIRONMENT USING CAMERA AND RADAR (출원일 2023-11-06; 출원번호 18/502,678; 등록일 2026-06-09; 등록번호 12,651,445; 국가 US; 발명자 Dongsuk Kum, Youngseok Kim)
- 카메라와 레이다를 이용한 3차원 환경 인지 시스템 및 그 방법 (출원일 2023-07-24; 출원번호 10-2023-0096379; 등록일 2024-11-06; 등록번호 10-2728715; 국가 KR; 발명자 금동석, 김영석)
- LANE CHANGE SYSTEM OF AUTONOMOUS VEHICLE (출원일 2022-08-02 / 2022-09-19 / 2022-09-20; 출원번호 PCT/KR2022/011370 / 17947800 / 22196698.9; 등록일 2026-03-17; 등록번호 12,576,850; 국가 WO / US / EP; 발명자 Dongsuk Kum, Kibeom Lee, Seulbin Hwang)
- 반응형 미래 예측 모델 기반의 능동적 자율주행 판단 제어 시스템 (출원일 2022-07-20; 출원번호 10-2022-0089652; 국가 KR; 발명자 금동석,전형석)
- 자율주행 자동차의 차선 변경 시스템 (출원일 2022-02-14; 출원번호 10-2022-0018946; 등록일 2025-01-15; 등록번호 10-2757102; 국가 KR; 발명자 금동석, 이기범, 황슬빈)
- 자율주행 자동차의 차선 변경 시스템 (출원일 2021-11-04; 출원번호 10-2021-0150288; 등록일 2025-01-15; 등록번호 10-2757102; 국가 KR; 발명자 금동석, 이기범, 황슬빈)
- ELECTRONIC DEVICE FOR OBTAINING THREE-DIMENSION OBJECT BASED ON CAMERA AND RADAR SENSOR FUSION, AND OPERATING METHOD THEREOF (출원일 2021-03-11; 출원번호 17199043; 등록일 2023-09-12; 등록번호 11.754.701; 국가 US; 발명자 Dongsuk Kum, Youngseok Kim)
- ELECTRONIC DEVICE FOR PREDICTION USING RECURSIVE STRUCTURE AND OPERATING METHOD THEREOF (출원일 2020-12-15; 출원번호 17121829; 등록일 2024-01-02; 등록번호 11.858.535; 국가 US; 발명자 Dongsuk Kum, Sanmin Kim)
- ELECTRONIC DEVICE FOR INTEGRATING AND PREDICTING FUTURE TRAJECTORIES OF UNSPECIFIED NUMBER OF SURROUNDING VEHICLES AND OPERATING METHOD THEREOF (출원일 2020-09-28; 출원번호 17/035,377; 등록일 2024-07-09; 등록번호 12.030.529; 국가 US; 발명자 Dongsuk Kum, Hyeongseok Jeon)
- 재귀 구조를 이용한 예측을 위한 전자 장치 및 그의 동작 방법 (출원일 2020-04-13; 출원번호 10-2020-0044712; 등록일 2023-06-05; 등록번호 10-2541685; 국가 KR; 발명자 금동석, 김산민)

## 과제

전체 진행 과제 9건·완료 과제 25건 가운데 게시된 기간이 2021-10-13–2026-10-13과 겹치는 20건이다. On-going Projects 9건과 Completed Projects 11건을 포함한다. 진행·완료는 누리집 분류로, 기간이 끝났더라도 On-going에 남아 있는 항목은 그 분류대로 적었다.[^ongoing][^completed]

- 신경망 시뮬레이터(월드 모델)를 활용한 고효율 End-to-End 자율주행 핵심기술 개발 및 실차 검증 연구 (기간 2026.03.01-2030.02.28; 지원 한국연구재단; 상태 On-going Projects 게시 구분)
- 강화학습 기반 충돌 회피/경감 알고리즘의 지식 전이 방법론 연구 (기간 2026.03.16~2027.04.15; 지원 현대자동차; 상태 On-going Projects 게시 구분)
- E2E 자율주행 레퍼런스 데이터 구축 및 기반 기술 개발 (기간 2025.07.01~2028.12.31; 지원 산업통상자원부; 상태 On-going Projects 게시 구분)
- VLA 모델 학습·검증용 데이터셋 구축 및 가상 시뮬레이션 기반 검증 기술 개발 (기간 2026.04.01~2029.12.31; 지원 산업통상자원부; 상태 On-going Projects 게시 구분)
- EREV의 연비 향상을 위한 SOC 계획 제어 프레임워크 개발 (기간 2025.08.19 ~ 2026.10.18; 지원 현대자동차; 상태 On-going Projects 게시 구분)
- 자율 주차를 위한 강화학습 기반 주차 경로 생성 기술 개발 (기간 2025.06.01 ~ 2026.05.31; 지원 현대자동차; 상태 On-going Projects 게시 구분)
- 악천후/비정형 환경변화에서의 Seamless 자율주행을 위한 인지/판단 AI SW 핵심 기술 개발 (기간 2023.04.01~2026.12.31; 지원 과학기술정보통신부; 상태 On-going Projects 게시 구분)
- Lv.4 자율주행 차량 테스트베드 환경 구축 (기간 2021.04.01~2027.12.31; 지원 국토교통부; 상태 On-going Projects 게시 구분)
- 국토교통 DNA플러스 도로교통분야 융합기술대학원 (기간 2022.05.01~2027.12.31; 지원 국토교통부; 상태 On-going Projects 게시 구분)
- 강화학습 기반 충돌 회피/경감 알고리즘 고도화를 위한 Sim-to-Real Transfer 방법론 연구 (기간 2024.09.01~2025.09.30; 지원 현대자동차; 상태 Completed Projects 게시 구분)
- 경쟁차 FCEV 통합열관리 모델 해석용 제어기 개발 (기간 2024.06.01 ~ 2025.05.31; 지원 현대자동차; 상태 Completed Projects 게시 구분)
- 클라우드 기반 자율주행 AI 학습 SW 개발 (기간 2021.04.01.~2024.12.31; 지원 과학기술정보통신부; 상태 Completed Projects 게시 구분)
- 클라우드 기반 융합형 자율주행 지능학습 데이터 생성/제공을 위한 데이터 수집·가공 핵심기술 개발 (기간 2021.04.01~2024.12.31; 지원 과학기술정보통신부; 상태 Completed Projects 게시 구분)
- Scene 통합 Risk 예측 및 RL 기반 Integrated Collision Avoidance/Mitigation System (CAMS) (기간 2023.06.01~2024.06.30; 지원 현대자동차; 상태 Completed Projects 게시 구분)
- FCEV 통합열관리 모델 해석용 제어기 개발 (기간 2022.12.07 ~ 2023.12.06; 지원 현대자동차; 상태 Completed Projects 게시 구분)
- Scene 통합 Risk 예측 및 MPC 기반 Integrated Collision Avoidance/Mitigation System (CAMS) (기간 2022.05.16 ~ 2023.05.15; 지원 현대자동차; 상태 Completed Projects 게시 구분)
- 4D 이미징 레이다 센서 기반 데이터 (기간 2022.6.1 ~ 2022.12.31; 지원 한국지능정보사회진흥원; 상태 Completed Projects 게시 구분)
- 도심 자율주행을 위한 주변 객체간 상관관계 기반 경로예측 딥러닝 알고리즘 연구 (기간 2022.03.01 ~ 2022.12.31; 지원 현대 NGV (현대자동차); 상태 Completed Projects 게시 구분)
- 글로벌 환경 적응형 자율주행을 위한  카메라-레이다 융합 인공지능 핵심기술 연구 (기간 2022.03.01~2025.12.31; 지원 한국연구재단; 상태 Completed Projects 게시 구분)
- 재난/재해 정찰 및 구조 보조 로봇 개발 (기간 2016.06.01 ~ 2021.12.31; 지원 정보통신기획평가원; 상태 Completed Projects 게시 구분)

## 수상

소식 목록에 게시된 2025년 수상 3건이다. 연도는 수상 제목을 따르고, 괄호 안에는 소식 게시일을 적었다.[^news]

- 2025 (게시일 2026-01-15) · 이선명 박사과정, 한국자동차공학회 추계학술대회 우수발표 논문상
- 2025 (게시일 2025-07-03) · 임준희 박사과정, 한국자동차공학회 춘계학술대회 우수발표 논문상
- 2025 (게시일 2025-07-03) · 강상묵 박사과정, 한국자동차공학회 춘계학술대회 우수발표 논문상

## 소식

소식·공지 전체 20건 가운데 2021-10-13–2026-10-13 범위의 논문 채택·게재 승인, 자율주행차 임시면허, 공개 성능 평가 소식 6건이다. 맨 앞 날짜는 게시일이며 구성원 과정은 게시 당시 표기다.[^news]

- 2026-03-16 · 강상묵 박사과정의 논문이 International Journal of Heat and Mass Transfer에 게재 승인되었다.
- 2026-01-27 · 정현준 박사과정의 논문이 ICLR 2026에 채택되었다.
- 2024-05-02 · 연구팀이 개발한 자율주행차가 2024년 2월 임시면허를 취득했다는 소식이 게시되었다.
- 2023-07-26 · 김영석·김산민 박사과정의 논문 두 편이 ICCV 2023에 채택되었다.
- 2023-03-28 · 김영석 박사과정의 CRN이 nuScenes Camera+Radar Detection Track에서 1위를 달성했다는 소식이 게시되었다.
- 2022-09-26 · 김영석 박사과정의 CRAFT가 nuScenes Camera+Radar Detection Track에서 1위를 달성했다는 소식이 게시되었다.

## 연락과 위치

- 교수 연구실: 대전광역시 유성구 문지로 193, KAIST 문지캠퍼스 F403호[^faculty][^deptlist]
- 연구실 연락 위치: 같은 주소 Faculty wing F442호[^members]
- 교수 이메일: dskum@kaist.ac.kr[^faculty]
- 교수 전화: +82-42-350-1266[^faculty]
- 연구실 전화와 이메일: +82-42-350-1286, vdclab@kaist.ac.kr[^members]

## 각주
[^faculty]: 연구실 Faculty의 소속·이력·관심 분야. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub1_1> (관측 2026-10-26).
[^av]: Autonomous Vehicles의 AV team vision. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub2_2&sca=AV+team+vision> (관측 2026-10-26).
[^ep]: Electric Powertrain의 EP team vision. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub2_1&sca=EP+team+vision> (관측 2026-10-26).
[^design]: 전동화 동력계 설계·에너지 관리 소개. <https://axelab.kaist.ac.kr/sub2_1.php> (관측 2026-10-26).
[^energy]: Archive의 Hybrid renewable energy system. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub2_3&sca=Hybrid+renewable+energy+system> (관측 2026-10-26).
[^robots]: Archive의 Robot Platform. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub2_4&sca=Robot+Platform> (관측 2026-10-26).
[^members]: Students & Researchers 명단. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub1_2> (관측 2026-10-26).
[^alumni]: Alumni 전체 두 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub1_4> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub1_4&page=2> (관측 2026-10-26).
[^theses]: Dissertation 전체 네 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_4> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_4&page=2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_4&page=3> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_4&page=4> (관측 2026-10-26).
[^journals]: Int. Journal 전체 다섯 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_1> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_1&page=2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_1&page=3> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_1&page=4> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_1&page=5> (관측 2026-10-26).
[^conferences]: Int. Conference 전체 네 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&page=2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&page=3> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_2&page=4> (관측 2026-10-26).
[^domestic]: Domestic Papers 전체 여섯 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3&page=2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3&page=3> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3&page=4> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3&page=5> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_3&page=6> (관측 2026-10-26).
[^patents]: 수록 특허 28항목의 상세 출원일·등록일·번호·발명자 표기. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=85> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=84> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=83> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=82> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=81> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=79> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=78> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=76> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=75> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=80> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=72> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=70> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=69> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=58> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=57> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=56&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=61&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=60&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=55&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=54&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=66&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=52&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=51&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=73&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=65&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=64&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=63&page=2> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub3_5&wr_id=44&page=3> (관측 2026-10-27).
[^ongoing]: On-going Projects 전체 목록. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub4_1> (관측 2026-10-26).
[^completed]: Completed Projects 전체 두 쪽과 충돌 회피·경감 과제 상세 두 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub4_2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub4_2&page=2> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub4_2&wr_id=37> (관측 2026-10-27). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub4_2&wr_id=36> (관측 2026-10-27).
[^news]: News & Notice 전체 두 쪽. <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub5_1> (관측 2026-10-26). <https://axelab.kaist.ac.kr/bbs/board.php?bo_table=sub5_1&page=2> (관측 2026-10-26).
[^deptlist]: KAIST 조천식모빌리티대학원 교수 명단, 전임교수 금동석 항목. <https://mo.kaist.ac.kr/professor/> (관측 2026-10-26).
[^deptprof]: KAIST 조천식모빌리티대학원 금동석 교수 소개. <https://mo.kaist.ac.kr/professor/%EA%B8%88%EB%8F%99%EC%84%9D/> (관측 2026-10-26).
[^deptresearch]: KAIST 조천식모빌리티대학원 AXE 연구성과 소개, 자율주행 인지·움직임 예측·강화학습 경로 생성·전기동력시스템. <https://mo.kaist.ac.kr/research/research-achievements/vdc-lab/> (관측 2026-10-26).
[^p1]: T. Barhoumi, D. Kum, IEEE Transactions on Transportation Electrification (2023). <https://doi.org/10.1109/TTE.2023.3255901> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/access.2024.3484942%7C10.1109/lra.2026.3663819%7C10.1109/tte.2023.3255901> (관측 2026-10-27).
[^p2]: J. Kim, K. Park, D. Kim, D. Kum, IEEE Access (2024). <https://doi.org/10.1109/ACCESS.2024.3484942> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/access.2024.3484942%7C10.1109/lra.2026.3663819%7C10.1109/tte.2023.3255901> (관측 2026-10-27).
[^p3]: A. R. Syamil, J. Lim, D. Kum, IEEE Robotics and Automation Letters (2026). <https://doi.org/10.1109/LRA.2026.3663819> 초록 기준(OpenAlex 등록 초록). 초록 원문 <https://api.openalex.org/works?per-page=50&select=id,doi,title,publication_year,primary_location,abstract_inverted_index&filter=doi:10.1109/access.2024.3484942%7C10.1109/lra.2026.3663819%7C10.1109/tte.2023.3255901> (관측 2026-10-27).
[^p4]: H. Jeong, J. Shin, D. Kum, ICLR 2026 · arXiv 판 (온라인 2026-03-30). <https://arxiv.org/abs/2603.28090> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2603.28090> (관측 2026-10-26).
[^p5]: I.-J. Lee 외, D. Kum, ICRA 2025 · arXiv 판 (온라인 2025-09-06). <https://arxiv.org/abs/2509.05785> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2509.05785> (관측 2026-10-26).
[^p6]: S. Kim 외, D. Kum, ECCV 2024 · arXiv 판 (온라인 2024-07-14). <https://arxiv.org/abs/2407.10164> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2407.10164> (관측 2026-10-26).
[^p7]: J. Shin, H. Jeong, F. Rameau, D. Kum, arXiv 사전 공개본 (온라인 2023-01-10). <https://arxiv.org/abs/2301.04470> 초록 기준(arXiv 판). 초록 원문 <https://arxiv.org/abs/2301.04470> (관측 2026-10-26).
